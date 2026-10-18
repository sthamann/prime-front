import { zipSync, strToU8 } from "fflate";
import type Sigma from "sigma";
import { conceptMatches, filterNodes, edgeId } from "./data";
import {
  conceptsCsv,
  conceptsDot,
  conceptsGEXF,
  conceptsGraphML,
  edgeEndpoints,
  matrixCsv,
  recordsCsv,
  serializeSvgElement,
  toGEXF,
  toGraphML,
  type ConceptExportEdge,
  type ConceptExportNode,
  type ExportNode,
} from "./formats";
import { compositePng } from "./gl";
import { matrixSvgEls } from "./matrices";
import { conceptSvgFromState, networkSvgFromState } from "./snapshot";
import type { AppState } from "./state";

function download(filename: string, blob: Blob): void {
  const a = document.createElement("a");
  a.href = URL.createObjectURL(blob);
  a.download = filename;
  a.click();
  setTimeout(() => URL.revokeObjectURL(a.href), 2000);
}

function downloadText(filename: string, text: string, mime: string): void {
  download(filename, new Blob([text], { type: mime }));
}

function visibleNodes(state: AppState): ExportNode[] {
  return filterNodes(state.bundle.graph.nodes, state.filters);
}

function visibleEdges(state: AppState) {
  const vis = new Set(visibleNodes(state).map((n) => n.id));
  return state.bundle.graph.edges
    .filter((e) => state.filters.edgeTypes.has(e.type))
    .map((e) => {
      const { s, t } = edgeId(e);
      return { source: s, target: t, type: e.type, weight: e.weight };
    })
    .filter((e) => vis.has(e.source) && vis.has(e.target));
}

function currentSvg(state: AppState, stage: HTMLElement): SVGSVGElement | null {
  if (state.view === "network" || state.view === "concepts") return null;
  if (state.view === "matrices") return matrixSvgEls(stage)[0] || null;
  return stage.querySelector("svg");
}

function viewSvgString(state: AppState, stage: HTMLElement): string | null {
  if (state.view === "network") return networkSvgFromState(state);
  if (state.view === "concepts") return conceptSvgFromState(state);
  const svg = currentSvg(state, stage);
  return svg ? serializeSvgElement(svg) : null;
}

async function rasterSvg(xml: string, w: number, h: number): Promise<Blob> {
  const blob = new Blob([xml], { type: "image/svg+xml;charset=utf-8" });
  const url = URL.createObjectURL(blob);
  const img = new Image();
  await new Promise<void>((resolve, reject) => {
    img.onload = () => resolve();
    img.onerror = () => reject(new Error("svg raster failed"));
    img.src = url;
  });
  const canvas = document.createElement("canvas");
  canvas.width = w;
  canvas.height = h;
  const ctx = canvas.getContext("2d");
  if (!ctx) throw new Error("no canvas");
  ctx.fillStyle = "#0b0d12";
  ctx.fillRect(0, 0, w, h);
  ctx.drawImage(img, 0, 0, w, h);
  URL.revokeObjectURL(url);
  return new Promise((resolve, reject) => {
    canvas.toBlob((b) => (b ? resolve(b) : reject(new Error("png blob failed"))), "image/png");
  });
}

export function visibleConcepts(state: AppState): { nodes: ConceptExportNode[]; edges: ConceptExportEdge[] } {
  const f = state.conceptFilters;
  const nodes = state.bundle.concepts.nodes.filter((n) => conceptMatches(n, f));
  const vis = new Set(nodes.map((n) => n.id));
  const edges = state.bundle.concepts.edges
    .filter((e) => vis.has(e.src) && (vis.has(e.dst) || e.rel === "USED_BY" || e.rel === "KILLED_BY"))
    .map((e) => ({ src: e.src, dst: e.dst, rel: e.rel, strength: e.strength, note: e.note }));
  return {
    nodes: nodes.map((n) => ({
      id: n.id,
      name: n.name,
      type: n.type,
      status: n.status,
      alive: n.alive,
      attempt_count: n.attempt_count,
    })),
    edges,
  };
}

export async function exportSvg(state: AppState, stage: HTMLElement): Promise<void> {
  const xml = viewSvgString(state, stage);
  if (!xml) throw new Error("no svg in current view");
  downloadText(`rh-catalog-${state.view}.svg`, xml, "image/svg+xml");
}

export async function exportPng(state: AppState, stage: HTMLElement): Promise<void> {
  const wrap = stage.querySelector(".gl-wrap") as (HTMLElement & { __sigma?: Sigma }) | null;
  if ((state.view === "network" || state.view === "concepts") && wrap?.__sigma) {
    try {
      const blob = await compositePng(wrap.__sigma, wrap.clientWidth || 1200, wrap.clientHeight || 800);
      download(`rh-catalog-${state.view}.png`, blob);
      return;
    } catch {
      /* fall through to SVG raster */
    }
  }
  const xml = viewSvgString(state, stage);
  if (!xml) throw new Error("no svg in current view");
  const svg = currentSvg(state, stage);
  const box = svg?.viewBox.baseVal;
  const w = (box && box.width ? box.width : 1200) * 2;
  const h = (box && box.height ? box.height : 800) * 2;
  download(`rh-catalog-${state.view}.png`, await rasterSvg(xml, w, h));
}

export function exportRecordsCsv(state: AppState): void {
  downloadText("rh-catalog-records.csv", recordsCsv(visibleNodes(state)), "text/csv");
}

export function exportRecordsJson(state: AppState): void {
  downloadText(
    "rh-catalog-records.json",
    JSON.stringify(visibleNodes(state), null, 2),
    "application/json",
  );
}

export function exportGraphML(state: AppState): void {
  downloadText("rh-catalog.graphml", toGraphML(visibleNodes(state), visibleEdges(state)), "application/xml");
}

export function exportGEXF(state: AppState): void {
  downloadText("rh-catalog.gexf", toGEXF(visibleNodes(state), visibleEdges(state)), "application/xml");
}

export function exportConcepts(state: AppState): void {
  const cmap = visibleConcepts(state);
  const csvs = conceptsCsv(cmap.nodes, cmap.edges);
  downloadText("concepts-nodes.csv", csvs.nodes, "text/csv");
  downloadText("concepts-edges.csv", csvs.edges, "text/csv");
  downloadText("concepts.graphml", conceptsGraphML(cmap.nodes, cmap.edges), "application/xml");
  downloadText("concepts.gexf", conceptsGEXF(cmap.nodes, cmap.edges), "application/xml");
  downloadText("concepts.dot", conceptsDot(cmap.nodes, cmap.edges), "text/vnd.graphviz");
}

export function exportMatricesCsv(state: AppState): void {
  const m = state.bundle.matrix;
  downloadText("family-x-outcome.csv", matrixCsv(m.family_x_outcome), "text/csv");
  downloadText("family-x-failure.csv", matrixCsv(m.family_x_failure_class), "text/csv");
  downloadText("kind-x-outcome.csv", matrixCsv(m.kind_x_outcome), "text/csv");
}

function countBy(items: { [k: string]: string }[], key: string): Record<string, number> {
  const o: Record<string, number> = {};
  for (const it of items) o[it[key]] = (o[it[key]] || 0) + 1;
  return o;
}

function rowsHtml(obj: Record<string, number>): string {
  return Object.entries(obj)
    .sort((a, b) => b[1] - a[1])
    .map(([k, v]) => `<tr><td>${k}</td><td>${v}</td></tr>`)
    .join("");
}

function gapTable(title: string, rows: string[][]): string {
  if (!rows.length) return `<h3>${title}</h3><p>none</p>`;
  return `<h3>${title} (${rows.length})</h3><table>${rows
    .slice(0, 40)
    .map((r) => `<tr>${r.map((c) => `<td>${c}</td>`).join("")}</tr>`)
    .join("")}</table>`;
}

function summaryHtml(state: AppState, svgSnippets: string[]): string {
  const meta = state.bundle.graph.meta;
  const n = visibleNodes(state);
  const byOut: Record<string, number> = {};
  const byFam: Record<string, number> = {};
  for (const node of n) {
    byOut[node.outcome] = (byOut[node.outcome] || 0) + 1;
    byFam[node.family] = (byFam[node.family] || 0) + 1;
  }
  const cmap = state.bundle.concepts;
  const gaps = state.bundle.gaps;
  const nameOf = (id: string) => cmap.nodes.find((x) => x.id === id)?.name || id;
  const conceptSection = cmap.nodes.length
    ? `<h2>Concept map</h2>
<p>${cmap.nodes.length} concepts · ${cmap.edges.length} edges · ${cmap.generated_at || ""}</p>
<h3>by type</h3><table>${rowsHtml(countBy(cmap.nodes, "type"))}</table>
<h3>by rel</h3><table>${rowsHtml(countBy(cmap.edges, "rel"))}</table>
<h3>by strength</h3><table>${rowsHtml(countBy(cmap.edges, "strength"))}</table>
${gapTable("G1 zero attempts", (gaps.G1 || []).map((x) => [x.id, x.type]))}
${gapTable("G2 unused criteria", (gaps.G2 || []).map((x) => [x.id, x.status]))}
${gapTable("G3 unobserved pairs", (gaps.G3 || []).map((x) => [x.pair.join(" × "), String(x.attempt_score)]))}
${gapTable("G4 barriers", (gaps.G4 || []).map((x) => [x.id, String(x.killed_by)]))}
${gapTable("G5 TFPT bridges", (gaps.G5 || []).map((x) => [nameOf(x.id), x.hops == null ? "no path" : String(x.hops)]))}
${gapTable("G6 open closers", (gaps.G6 || []).map((x) => [x.id, `${x.alive_targets}/${x.target_count}`]))}`
    : "";
  return `<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"/><title>RH corpus catalog — exploration record; no RH claim</title>
<style>body{font:14px/1.45 ui-sans-serif,system-ui;background:#0b0d12;color:#e8eaef;margin:32px} h1{font-size:18px} table{border-collapse:collapse} td,th{border-bottom:1px solid #2a3140;padding:4px 10px;text-align:left} .svg{margin:16px 0;background:#12151c}</style>
</head><body>
<h1>RH corpus catalog — exploration record; no RH claim</h1>
<p>${meta.claim_boundary}</p>
<p>Generated ${meta.generated} · catalog ${meta.catalog_generated || "—"} · nodes ${meta.n_nodes} (filtered ${n.length}) · curated ${meta.n_curated} · draft ${meta.n_draft}</p>
<h2>Outcome</h2><table>${rowsHtml(byOut)}</table>
<h2>Family</h2><table>${rowsHtml(byFam)}</table>
${conceptSection}
${svgSnippets.map((s) => `<div class="svg">${s}</div>`).join("")}
</body></html>`;
}

export async function exportBundle(state: AppState, stage: HTMLElement): Promise<void> {
  const nodes = visibleNodes(state);
  const edges = visibleEdges(state);
  const svgs: string[] = [];
  const allSvg = [...stage.querySelectorAll("svg")];
  for (const svg of allSvg) {
    try {
      svgs.push(serializeSvgElement(svg as SVGSVGElement));
    } catch {
      /* ignore */
    }
  }
  const files: Record<string, Uint8Array> = {
    "summary.html": strToU8(summaryHtml(state, svgs)),
    "records.csv": strToU8(recordsCsv(nodes)),
    "records.json": strToU8(JSON.stringify(nodes, null, 2)),
    "graph.graphml": strToU8(toGraphML(nodes, edges)),
    "graph.gexf": strToU8(toGEXF(nodes, edges)),
    "family-x-outcome.csv": strToU8(matrixCsv(state.bundle.matrix.family_x_outcome)),
    "family-x-failure.csv": strToU8(matrixCsv(state.bundle.matrix.family_x_failure_class)),
    "kind-x-outcome.csv": strToU8(matrixCsv(state.bundle.matrix.kind_x_outcome)),
  };
  const cmap = visibleConcepts(state);
  const csvs = conceptsCsv(cmap.nodes, cmap.edges);
  files["concepts-nodes.csv"] = strToU8(csvs.nodes);
  files["concepts-edges.csv"] = strToU8(csvs.edges);
  files["concepts.graphml"] = strToU8(conceptsGraphML(cmap.nodes, cmap.edges));
  files["concepts.gexf"] = strToU8(conceptsGEXF(cmap.nodes, cmap.edges));
  files["concepts.dot"] = strToU8(conceptsDot(cmap.nodes, cmap.edges));
  files["concepts.json"] = strToU8(JSON.stringify(state.bundle.concepts));
  files["gaps_report.json"] = strToU8(JSON.stringify(state.bundle.gaps));
  try {
    files["network.svg"] = strToU8(networkSvgFromState(state));
    files["concepts.svg"] = strToU8(conceptSvgFromState(state));
  } catch {
    /* ignore */
  }
  svgs.forEach((s, i) => {
    files[`view-${i}.svg`] = strToU8(s);
  });
  const zipped = zipSync(files);
  download("rh-catalog-report.zip", new Blob([zipped], { type: "application/zip" }));
}

export function renderExport(host: HTMLElement, state: AppState, stage: HTMLElement): () => void {
  host.innerHTML = "";
  host.className = "stage export-stage";
  const card = document.createElement("section");
  card.className = "export-card";
  card.innerHTML = `
    <h2>Export</h2>
    <p class="muted">Current filters apply to records and graph dumps. ⌘/Ctrl+E builds the report bundle.</p>
    <div class="export-grid">
      <button type="button" data-act="svg">Current view SVG</button>
      <button type="button" data-act="png">Current view PNG (2×)</button>
      <button type="button" data-act="csv">Filtered records CSV</button>
      <button type="button" data-act="json">Filtered records JSON</button>
      <button type="button" data-act="graphml">GraphML</button>
      <button type="button" data-act="gexf">GEXF</button>
      <button type="button" data-act="mx">Matrices CSV</button>
      <button type="button" data-act="cmap">Concept GraphML / GEXF / DOT / CSV</button>
      <button type="button" data-act="zip">Report bundle ZIP</button>
    </div>
    <p class="status muted" id="export-status"></p>`;
  host.append(card);
  const status = card.querySelector("#export-status") as HTMLElement;
  const run = async (act: string) => {
    status.textContent = "working…";
    try {
      if (act === "svg") await exportSvg(state, stage);
      else if (act === "png") await exportPng(state, stage);
      else if (act === "csv") exportRecordsCsv(state);
      else if (act === "json") exportRecordsJson(state);
      else if (act === "graphml") exportGraphML(state);
      else if (act === "gexf") exportGEXF(state);
      else if (act === "mx") exportMatricesCsv(state);
      else if (act === "cmap") exportConcepts(state);
      else if (act === "zip") await exportBundle(state, stage);
      status.textContent = "done";
    } catch (err) {
      status.textContent = err instanceof Error ? err.message : String(err);
    }
  };
  card.querySelectorAll("button").forEach((btn) => {
    btn.addEventListener("click", () => run((btn as HTMLElement).dataset.act || ""));
  });
  return () => {
    host.innerHTML = "";
  };
}

export { edgeEndpoints };
