import Graph from "graphology";
import Sigma from "sigma";
import type { EdgeDisplayData, NodeDisplayData } from "sigma/types";
import { familyColor, conceptTypeColor, EDGE_STYLE, REL_GROUP_STYLE, strengthStyle } from "./palette";
import type { ConceptNode, EdgeType, GraphNode } from "./types";
import { REL_TO_GROUP } from "./types";

export const ZOOM_HIDE: Record<string, number> = {
  SEMANTIC: 0.82,
  FAMILY: 0.82,
  SAME_ROUND: 0.82,
  SHARED_LEDGER: 0.92,
};

function zoomBand(ratio: number): number {
  if (ratio > 0.92) return 0;
  if (ratio > 0.82) return 1;
  return 2;
}

export function makeGraph() {
  return new Graph({ type: "undirected", multi: true, allowSelfLoops: false });
}

export function addRecordNode(g: Graph, n: GraphNode): void {
  if (g.hasNode(n.id)) return;
  g.addNode(n.id, {
    x: n.x ?? 0,
    y: n.y ?? 0,
    size: n.size ?? 3,
    label: n.round || n.path.split("/").pop() || n.id,
    color: familyColor(n.family),
    outcome: n.outcome,
    family: n.family,
    kind: n.kind,
    draft: n.draft,
    path: n.path,
  });
}

export function addConceptNode(g: Graph, n: ConceptNode): void {
  if (g.hasNode(n.id)) return;
  g.addNode(n.id, {
    x: n.x ?? 0,
    y: n.y ?? 0,
    size: n.size ?? 4,
    label: n.name,
    color: conceptTypeColor(n.type),
    ctype: n.type,
    status: n.status,
    alive: n.alive,
  });
}

export function addTypedEdge(g: Graph, id: string, s: string, t: string, etype: string, extra?: Record<string, unknown>): void {
  if (!g.hasNode(s) || !g.hasNode(t) || s === t) return;
  if (g.hasEdge(id)) return;
  g.addEdgeWithKey(id, s, t, { etype, ...extra });
}

export function mountSigma(
  container: HTMLElement,
  graph: Graph,
  opts: {
    nodeReducer: (node: string, data: Record<string, unknown>) => Partial<NodeDisplayData>;
    edgeReducer: (edge: string, data: Record<string, unknown>) => Partial<EdgeDisplayData>;
    onClick: (id: string, ev: { event: { original: Event } }) => void;
    onEnter: (id: string) => void;
    onLeave: () => void;
    renderLabels: boolean;
  },
): Sigma {
  if (container.clientWidth < 8 || container.clientHeight < 8) {
    container.style.minHeight = "240px";
  }
  const sigma = new Sigma(graph, container, {
    allowInvalidContainer: true,
    renderLabels: opts.renderLabels,
    renderEdgeLabels: false,
    hideEdgesOnMove: true,
    hideLabelsOnMove: true,
    labelRenderedSizeThreshold: 7,
    labelDensity: 0.35,
    labelFont: "SF Pro Text, Segoe UI, system-ui, sans-serif",
    labelColor: { color: "#d7dde8" },
    labelSize: 11,
    defaultNodeColor: "#8b919d",
    defaultEdgeColor: "#3a4250",
    minCameraRatio: 0.05,
    maxCameraRatio: 6,
    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    nodeReducer: opts.nodeReducer as any,
    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    edgeReducer: opts.edgeReducer as any,
  });
  sigma.on("clickNode", (e) => opts.onClick(e.node, e));
  sigma.on("enterNode", (e) => opts.onEnter(e.node));
  sigma.on("leaveNode", () => opts.onLeave());
  let lastBand = zoomBand(sigma.getCamera().ratio);
  sigma.getCamera().on("updated", () => {
    const band = zoomBand(sigma.getCamera().ratio);
    if (band === lastBand) return;
    lastBand = band;
    sigma.refresh();
  });
  (container as HTMLElement & { __sigma?: Sigma }).__sigma = sigma;
  markFirstFrame();
  return sigma;
}

export function markFirstFrame(): void {
  const w = window as Window & { __viewerPerf?: { firstFrame?: number } };
  if (w.__viewerPerf?.firstFrame) return;
  requestAnimationFrame(() => {
    if (!w.__viewerPerf) w.__viewerPerf = {};
    if (!w.__viewerPerf.firstFrame) w.__viewerPerf.firstFrame = performance.now();
  });
}

export function recordNodeStyle(
  data: Record<string, unknown>,
  opts: { selected?: boolean; dim?: boolean; highlighted?: boolean },
): Partial<NodeDisplayData> {
  const family = String(data.family || "");
  const outcome = String(data.outcome || "");
  const draft = !!data.draft;
  let color = familyColor(family);
  if (outcome === "KILLED") color = mix(color, "#e85d5d", 0.45);
  else if (outcome === "PROVED" || outcome === "CERTIFIED") color = mix(color, "#3dcf8e", 0.28);
  if (opts.dim) color = fade(color, 0.18);
  else if (draft) color = fade(color, 0.7);
  return {
    ...data,
    x: Number(data.x),
    y: Number(data.y),
    size: Number(data.size || 3) * (opts.selected ? 1.35 : 1),
    color,
    label: String(data.label || ""),
    hidden: false,
    highlighted: !!opts.selected || !!opts.highlighted,
    forceLabel: !!opts.selected,
    zIndex: opts.selected ? 2 : 1,
  };
}

export function conceptNodeStyle(
  data: Record<string, unknown>,
  opts: { selected?: boolean; dim?: boolean; path?: boolean },
): Partial<NodeDisplayData> {
  const type = String(data.ctype || "");
  const status = String(data.status || "");
  let color = conceptTypeColor(type);
  if (status === "KILLED_HERE") color = mix(color, "#e85d5d", 0.5);
  else if (status === "PROVED_HERE" || status === "FORMALIZED_LEAN") color = mix(color, "#3dcf8e", 0.3);
  if (opts.dim) color = fade(color, 0.16);
  else if (data.alive === false) color = fade(color, 0.4);
  if (opts.path) color = mix(color, "#e8d08a", 0.45);
  return {
    ...data,
    x: Number(data.x),
    y: Number(data.y),
    size: Number(data.size || 4) * (opts.selected ? 1.4 : 1),
    color,
    label: String(data.label || ""),
    hidden: false,
    highlighted: !!opts.selected || !!opts.path,
    forceLabel: !!opts.selected,
    zIndex: opts.selected || opts.path ? 2 : 1,
  };
}

export function recordEdgeStyle(
  data: Record<string, unknown>,
  ratio: number,
  opts: { hidden: boolean; dim?: boolean },
): Partial<EdgeDisplayData> {
  const etype = String(data.etype || "") as EdgeType;
  const st = EDGE_STYLE[etype] || EDGE_STYLE.DEPENDS;
  const zoomHide = ZOOM_HIDE[etype];
  const hideZoom = zoomHide != null && ratio > zoomHide;
  return {
    hidden: opts.hidden || hideZoom,
    color: opts.dim ? fade(st.color, 0.14) : st.color,
    size: st.width,
    zIndex: 0,
  };
}

export function conceptEdgeStyle(
  data: Record<string, unknown>,
  opts: { hidden: boolean },
): Partial<EdgeDisplayData> {
  const rel = String(data.rel || "");
  const group = REL_TO_GROUP[rel as keyof typeof REL_TO_GROUP];
  const st = REL_GROUP_STYLE[group] || REL_GROUP_STYLE.implication;
  const sw = strengthStyle(String(data.strength || "HEURISTIC"));
  return {
    hidden: opts.hidden,
    color: st.color,
    size: sw.width,
    zIndex: opts.hidden ? 0 : 1,
  };
}

export function compositePng(sigma: Sigma, w: number, h: number): Promise<Blob> {
  const canvases = sigma.getCanvases();
  const out = document.createElement("canvas");
  out.width = w;
  out.height = h;
  const ctx = out.getContext("2d");
  if (!ctx) return Promise.reject(new Error("no canvas"));
  ctx.fillStyle = "#0b0d12";
  ctx.fillRect(0, 0, w, h);
  for (const key of ["edges", "nodes", "labels", "hover", "mouse"]) {
    const c = canvases[key];
    if (c) ctx.drawImage(c, 0, 0, w, h);
  }
  return new Promise((resolve, reject) => {
    out.toBlob((b) => (b ? resolve(b) : reject(new Error("png blob failed"))), "image/png");
  });
}

function mix(a: string, b: string, t: number): string {
  const pa = hex(a);
  const pb = hex(b);
  const m = (i: number) => Math.round(pa[i] * (1 - t) + pb[i] * t);
  return `rgb(${m(0)},${m(1)},${m(2)})`;
}

function fade(c: string, a: number): string {
  const p = hex(c);
  return `rgba(${p[0]},${p[1]},${p[2]},${a})`;
}

function hex(c: string): [number, number, number] {
  if (c.startsWith("rgb")) {
    const m = c.match(/[\d.]+/g) || ["128", "128", "128"];
    return [Number(m[0]), Number(m[1]), Number(m[2])];
  }
  const h = c.replace("#", "");
  const n = parseInt(h.length === 3 ? h.split("").map((x) => x + x).join("") : h, 16);
  return [(n >> 16) & 255, (n >> 8) & 255, n & 255];
}
