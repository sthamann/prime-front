import type Sigma from "sigma";
import FA2Layout from "graphology-layout-forceatlas2/worker";
import { edgeId, filterNodes } from "./data";
import {
  addRecordNode,
  addTypedEdge,
  makeGraph,
  mountSigma,
  recordEdgeStyle,
  recordNodeStyle,
} from "./gl";
import type { AppState } from "./state";
import type { GraphNode } from "./types";

function hullPoints(nodes: GraphNode[]): Map<string, { x: number; y: number }[]> {
  const g = new Map<string, { x: number; y: number }[]>();
  for (const n of nodes) {
    if (n.x == null || n.y == null) continue;
    const list = g.get(n.family) || [];
    list.push({ x: n.x, y: n.y });
    g.set(n.family, list);
  }
  return g;
}

function convexHull(pts: { x: number; y: number }[]): { x: number; y: number }[] {
  if (pts.length < 3) return pts;
  const p = pts.slice().sort((a, b) => (a.x === b.x ? a.y - b.y : a.x - b.x));
  const cross = (o: { x: number; y: number }, a: { x: number; y: number }, b: { x: number; y: number }) =>
    (a.x - o.x) * (b.y - o.y) - (a.y - o.y) * (b.x - o.x);
  const lower: typeof p = [];
  for (const pt of p) {
    while (lower.length >= 2 && cross(lower[lower.length - 2], lower[lower.length - 1], pt) <= 0) lower.pop();
    lower.push(pt);
  }
  const upper: typeof p = [];
  for (let i = p.length - 1; i >= 0; i--) {
    const pt = p[i];
    while (upper.length >= 2 && cross(upper[upper.length - 2], upper[upper.length - 1], pt) <= 0) upper.pop();
    upper.push(pt);
  }
  upper.pop();
  lower.pop();
  return lower.concat(upper);
}

export function renderNetwork(host: HTMLElement, state: AppState): () => void {
  host.innerHTML = "";
  host.className = "stage network-stage";
  const wrap = document.createElement("div");
  wrap.className = "gl-wrap";
  const hull = document.createElement("canvas");
  hull.className = "hull-layer";
  const tooltip = document.createElement("div");
  tooltip.className = "tip";
  const tools = document.createElement("div");
  tools.className = "gl-tools";
  tools.innerHTML = `<button type="button" id="relayout">re-layout</button>`;
  host.append(wrap, hull, tools, tooltip);

  const graph = makeGraph();
  let sigma: Sigma | null = null;
  let fa2: FA2Layout | null = null;
  let lastKey = "";
  let hoverId: string | null = null;

  function neighborsOf(id: string): string[] {
    try {
      return graph.neighbors(id);
    } catch {
      return [];
    }
  }

  function rebuildGraph(): void {
    const visible = filterNodes(state.bundle.graph.nodes, state.filters);
    const vis = new Set(visible.map((n) => n.id));
    const keepN = new Set(visible.map((n) => n.id));
    graph.forEachNode((id) => {
      if (!keepN.has(id)) graph.dropNode(id);
    });
    for (const n of visible) {
      if (!graph.hasNode(n.id)) addRecordNode(graph, n);
    }
    const keepE = new Set<string>();
    for (const e of state.bundle.graph.edges) {
      if (!state.filters.edgeTypes.has(e.type)) continue;
      const { s, t } = edgeId(e);
      if (!vis.has(s) || !vis.has(t)) continue;
      const eid = `${e.type}|${s}|${t}`;
      keepE.add(eid);
      if (!graph.hasEdge(eid)) addTypedEdge(graph, eid, s, t, e.type);
    }
    graph.forEachEdge((eid) => {
      if (!keepE.has(eid)) graph.dropEdge(eid);
    });
  }

  function drawHulls(): void {
    const ctx = hull.getContext("2d");
    if (!ctx || !sigma) return;
    const w = wrap.clientWidth || 1;
    const h = wrap.clientHeight || 1;
    if (hull.width !== w || hull.height !== h) {
      hull.width = w;
      hull.height = h;
    }
    ctx.clearRect(0, 0, w, h);
    if (!state.filters.showHulls) return;
    const groups = hullPoints(filterNodes(state.bundle.graph.nodes, state.filters));
    ctx.lineWidth = 1;
    for (const [fam, pts] of groups) {
      const hullPts = convexHull(pts);
      if (hullPts.length < 3) continue;
      ctx.beginPath();
      hullPts.forEach((p, i) => {
        const v = sigma!.graphToViewport(p);
        if (i === 0) ctx.moveTo(v.x, v.y);
        else ctx.lineTo(v.x, v.y);
      });
      ctx.closePath();
      ctx.fillStyle = "rgba(126,176,255,0.04)";
      ctx.strokeStyle = "rgba(126,176,255,0.18)";
      void fam;
      ctx.fill();
      ctx.stroke();
    }
  }

  function attach(): void {
    if (sigma) {
      sigma.kill();
      sigma = null;
    }
    sigma = mountSigma(wrap, graph, {
      renderLabels: state.filters.showLabels,
      nodeReducer: (id, data) =>
        recordNodeStyle(data, {
          selected: state.selected?.id === id,
          highlighted: state.highlighted.has(id),
          dim: state.highlighted.size > 0 && !state.highlighted.has(id),
        }),
      edgeReducer: (eid, data) => {
        const ratio = sigma?.getCamera().ratio ?? 1;
        const etype = String(data.etype || "");
        const hidden = !state.filters.edgeTypes.has(etype as never);
        const dim = state.highlighted.size > 0;
        return recordEdgeStyle(data, ratio, { hidden, dim });
      },
      onClick: (id) => {
        const node = state.bundle.graph.nodes.find((n) => n.id === id) || null;
        state.select(node, neighborsOf(id));
      },
      onEnter: (id) => {
        hoverId = id;
        const n = state.bundle.graph.nodes.find((x) => x.id === id);
        if (!n) return;
        tooltip.hidden = false;
        tooltip.innerHTML = `<strong>${esc(n.round || "—")}</strong><span>${esc(n.family)}</span><span>${esc(n.outcome)} · ${esc(n.kind)}</span>`;
      },
      onLeave: () => {
        hoverId = null;
        tooltip.hidden = true;
      },
    });
    sigma.getCamera().on("updated", drawHulls);
    wrap.addEventListener("mousemove", (ev) => {
      if (!hoverId) return;
      const rect = host.getBoundingClientRect();
      tooltip.style.left = `${ev.clientX - rect.left + 12}px`;
      tooltip.style.top = `${ev.clientY - rect.top + 10}px`;
    });
    drawHulls();
  }

  function topoKey(): string {
    const f = state.filters;
    return [
      [...f.kinds].join(),
      [...f.outcomes].join(),
      [...f.families].join(),
      [...f.relevances].join(),
      [...f.failures].join(),
      f.curatedOnly,
      f.roundMin,
      f.roundMax,
      f.includeUnnumbered,
      f.query,
      [...f.edgeTypes].join(),
      f.showLabels,
    ].join("|");
  }

  function apply(): void {
    const k = topoKey();
    if (k !== lastKey) {
      lastKey = k;
      rebuildGraph();
      if (!sigma) attach();
      else {
        sigma.setSetting("renderLabels", state.filters.showLabels);
        sigma.refresh();
      }
    } else if (sigma) {
      sigma.refresh();
    }
    drawHulls();
  }

  tools.querySelector("#relayout")?.addEventListener("click", () => {
    if (fa2?.isRunning()) {
      fa2.stop();
      return;
    }
    fa2 = new FA2Layout(graph, {
      settings: { barnesHutOptimize: true, gravity: 0.7, scalingRatio: 6, slowDown: 8 },
    });
    fa2.start();
    setTimeout(() => {
      fa2?.stop();
      fa2?.kill();
      fa2 = null;
      graph.forEachNode((id, attr) => {
        const n = state.bundle.graph.nodes.find((x) => x.id === id);
        if (n) {
          n.x = attr.x as number;
          n.y = attr.y as number;
        }
      });
      sigma?.refresh();
      drawHulls();
    }, 2500);
  });

  const ro = new ResizeObserver(() => drawHulls());
  ro.observe(wrap);
  const off = state.on(() => {
    if (state.view === "network") apply();
  });
  lastKey = "";
  apply();

  return () => {
    off();
    ro.disconnect();
    fa2?.kill();
    sigma?.kill();
    host.innerHTML = "";
  };
}

function esc(s: string): string {
  return s.replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" })[c]!);
}

export function networkSvgEl(_host: HTMLElement): SVGSVGElement | null {
  return null;
}

export function networkSigma(host: HTMLElement): Sigma | null {
  const wrap = host.querySelector(".gl-wrap") as (HTMLElement & { __sigma?: Sigma }) | null;
  return wrap?.__sigma || null;
}
