import { filterNodes, edgeId, conceptMatches } from "./data";
import { familyColor, conceptTypeColor } from "./palette";
import type { AppState } from "./state";

function esc(s: string): string {
  return String(s).replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" })[c]!);
}

export function networkSvgFromState(state: AppState, w = 1200, h = 800): string {
  const nodes = filterNodes(state.bundle.graph.nodes, state.filters).filter((n) => n.x != null && n.y != null);
  const vis = new Set(nodes.map((n) => n.id));
  const edges = state.bundle.graph.edges
    .filter((e) => state.filters.edgeTypes.has(e.type))
    .map((e) => {
      const { s, t } = edgeId(e);
      return { s, t, type: e.type };
    })
    .filter((e) => vis.has(e.s) && vis.has(e.t));
  const xs = nodes.map((n) => n.x as number);
  const ys = nodes.map((n) => n.y as number);
  const minX = Math.min(...xs);
  const maxX = Math.max(...xs);
  const minY = Math.min(...ys);
  const maxY = Math.max(...ys);
  const sx = (x: number) => ((x - minX) / Math.max(maxX - minX, 1e-6)) * (w - 40) + 20;
  const sy = (y: number) => ((y - minY) / Math.max(maxY - minY, 1e-6)) * (h - 40) + 20;
  const pos = new Map(nodes.map((n) => [n.id, { x: sx(n.x as number), y: sy(n.y as number), r: n.size || 3 }]));
  const lines = edges
    .map((e) => {
      const a = pos.get(e.s);
      const b = pos.get(e.t);
      if (!a || !b) return "";
      return `<line x1="${a.x.toFixed(1)}" y1="${a.y.toFixed(1)}" x2="${b.x.toFixed(1)}" y2="${b.y.toFixed(1)}" stroke="#5a6270" stroke-width="0.5" opacity="0.35"/>`;
    })
    .join("");
  const circles = nodes
    .map((n) => {
      const p = pos.get(n.id)!;
      return `<circle cx="${p.x.toFixed(1)}" cy="${p.y.toFixed(1)}" r="${p.r}" fill="${familyColor(n.family)}" stroke="#0b0d12" stroke-width="0.5"/>`;
    })
    .join("");
  return `<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="${w}" height="${h}" viewBox="0 0 ${w} ${h}">
  <rect width="${w}" height="${h}" fill="#0b0d12"/>
  <g>${lines}</g><g>${circles}</g>
</svg>`;
}

export function conceptSvgFromState(state: AppState, w = 1200, h = 800): string {
  const nodes = state.bundle.concepts.nodes.filter((n) => conceptMatches(n, state.conceptFilters) && n.x != null);
  const vis = new Set(nodes.map((n) => n.id));
  const edges = state.bundle.concepts.edges.filter((e) => vis.has(e.src) && vis.has(e.dst) && e.rel !== "USED_BY" && e.rel !== "KILLED_BY");
  const xs = nodes.map((n) => n.x as number);
  const ys = nodes.map((n) => n.y as number);
  const minX = Math.min(...xs, 0);
  const maxX = Math.max(...xs, 1);
  const minY = Math.min(...ys, 0);
  const maxY = Math.max(...ys, 1);
  const sx = (x: number) => ((x - minX) / Math.max(maxX - minX, 1e-6)) * (w - 40) + 20;
  const sy = (y: number) => ((y - minY) / Math.max(maxY - minY, 1e-6)) * (h - 40) + 20;
  const pos = new Map(nodes.map((n) => [n.id, { x: sx(n.x as number), y: sy(n.y as number) }]));
  const lines = edges
    .map((e) => {
      const a = pos.get(e.src);
      const b = pos.get(e.dst);
      if (!a || !b) return "";
      return `<line x1="${a.x.toFixed(1)}" y1="${a.y.toFixed(1)}" x2="${b.x.toFixed(1)}" y2="${b.y.toFixed(1)}" stroke="#5a6270" stroke-width="0.6" opacity="0.4"/>`;
    })
    .join("");
  const circles = nodes
    .map((n) => {
      const p = pos.get(n.id)!;
      return `<circle cx="${p.x.toFixed(1)}" cy="${p.y.toFixed(1)}" r="${n.size || 4}" fill="${conceptTypeColor(n.type)}" stroke="#0b0d12"/>`;
    })
    .join("");
  return `<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="${w}" height="${h}" viewBox="0 0 ${w} ${h}">
  <rect width="${w}" height="${h}" fill="#0b0d12"/>
  <title>${esc("RH corpus catalog — exploration record; no RH claim")}</title>
  <g>${lines}</g><g>${circles}</g>
</svg>`;
}
