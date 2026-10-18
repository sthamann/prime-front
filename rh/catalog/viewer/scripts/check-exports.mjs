#!/usr/bin/env node
/** Headless export check against public/data/graph.json. No RH claim. */
import { mkdir, readFile, writeFile } from "node:fs/promises";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const root = join(dirname(fileURLToPath(import.meta.url)), "..");
const dataDir = join(root, "public", "data");
const outDir = join(root, "export-out");

function csvEscape(s) {
  const t = s == null ? "" : String(s);
  if (/[",\n]/.test(t)) return `"${t.replace(/"/g, '""')}"`;
  return t;
}

function xmlEscape(s) {
  return String(s)
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;");
}

function recordsCsv(nodes) {
  const cols = [
    "id",
    "path",
    "round",
    "kind",
    "family",
    "outcome",
    "failure_class",
    "rh_relevance",
    "draft",
    "score",
  ];
  const lines = [cols.join(",")];
  for (const n of nodes) lines.push(cols.map((c) => csvEscape(n[c])).join(","));
  return lines.join("\n") + "\n";
}

function toGraphML(nodes, edges) {
  const nodeXml = nodes
    .map(
      (n) =>
        `    <node id="${xmlEscape(n.id)}"><data key="family">${xmlEscape(n.family)}</data><data key="outcome">${xmlEscape(n.outcome)}</data></node>`,
    )
    .join("\n");
  const edgeXml = edges
    .map(
      (e, i) =>
        `    <edge id="e${i}" source="${xmlEscape(e.source)}" target="${xmlEscape(e.target)}"><data key="etype">${xmlEscape(e.type)}</data></edge>`,
    )
    .join("\n");
  return `<?xml version="1.0" encoding="UTF-8"?>
<graphml xmlns="http://graphml.graphdrawing.org/xmlns">
  <key id="family" for="node" attr.name="family" attr.type="string"/>
  <key id="outcome" for="node" attr.name="outcome" attr.type="string"/>
  <key id="etype" for="edge" attr.name="type" attr.type="string"/>
  <graph id="G" edgedefault="undirected">
${nodeXml}
${edgeXml}
  </graph>
</graphml>
`;
}

function simpleSvg(nodes, w = 800, h = 600) {
  const circles = nodes
    .slice(0, 400)
    .map((n, i) => {
      const x = 40 + (i % 20) * 36;
      const y = 40 + Math.floor(i / 20) * 28;
      return `<circle cx="${x}" cy="${y}" r="5" fill="#7eb0ff"/>`;
    })
    .join("");
  return `<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="${w}" height="${h}" viewBox="0 0 ${w} ${h}">
  <rect width="${w}" height="${h}" fill="#0b0d12"/>
  ${circles}
</svg>
`;
}

function assert(cond, msg) {
  if (!cond) throw new Error(msg);
}

const graph = JSON.parse(await readFile(join(dataDir, "graph.json"), "utf8"));
const matrix = JSON.parse(await readFile(join(dataDir, "matrix.json"), "utf8"));
assert(Array.isArray(graph.nodes) && graph.nodes.length > 0, "no nodes");
assert(Array.isArray(graph.edges), "no edges");
assert(matrix.family_x_outcome?.cells, "no matrix");

const nodes = graph.nodes;
const edges = graph.edges.map((e) => ({
  source: typeof e.source === "string" ? e.source : e.source.id,
  target: typeof e.target === "string" ? e.target : e.target.id,
  type: e.type,
}));

await mkdir(outDir, { recursive: true });
const csv = recordsCsv(nodes);
const graphml = toGraphML(nodes, edges);
const svg = simpleSvg(nodes);
await writeFile(join(outDir, "records.csv"), csv);
await writeFile(join(outDir, "graph.graphml"), graphml);
await writeFile(join(outDir, "network.svg"), svg);

assert(csv.split("\n").length > nodes.length, "csv short");
assert(graphml.includes("<graphml") && graphml.includes("</graphml>"), "graphml broken");
assert(svg.includes("<svg") && svg.includes("</svg>"), "svg broken");
assert((graph.meta.n_nodes || 0) === nodes.length, "meta n_nodes mismatch");

const concepts = JSON.parse(await readFile(join(dataDir, "concepts.json"), "utf8"));
const gaps = JSON.parse(await readFile(join(dataDir, "gaps_report.json"), "utf8"));
assert(Array.isArray(concepts.nodes) && concepts.nodes.length > 0, "no concepts");
assert(Array.isArray(concepts.edges), "no concept edges");
assert(gaps.G1 && gaps.G5, "gaps missing G1/G5");

function conceptsCsv(cnodes, cedges) {
  const nCols = ["id", "name", "type", "status", "alive", "attempt_count"];
  const eCols = ["src", "dst", "rel", "strength"];
  const nLines = [nCols.join(",")];
  for (const n of cnodes) nLines.push(nCols.map((c) => csvEscape(n[c])).join(","));
  const eLines = [eCols.join(",")];
  for (const e of cedges) eLines.push(eCols.map((c) => csvEscape(e[c])).join(","));
  return { nodes: nLines.join("\n") + "\n", edges: eLines.join("\n") + "\n" };
}

function conceptsGraphML(cnodes, cedges) {
  const nodeXml = cnodes
    .map((n) => `    <node id="${xmlEscape(n.id)}"><data key="type">${xmlEscape(n.type)}</data></node>`)
    .join("\n");
  const edgeXml = cedges
    .map((e, i) => `    <edge id="e${i}" source="${xmlEscape(e.src)}" target="${xmlEscape(e.dst)}"><data key="rel">${xmlEscape(e.rel)}</data></edge>`)
    .join("\n");
  return `<?xml version="1.0" encoding="UTF-8"?>
<graphml xmlns="http://graphml.graphdrawing.org/xmlns">
  <key id="type" for="node" attr.name="type" attr.type="string"/>
  <key id="rel" for="edge" attr.name="rel" attr.type="string"/>
  <graph id="concepts" edgedefault="directed">
${nodeXml}
${edgeXml}
  </graph>
</graphml>
`;
}

function conceptsDot(cnodes, cedges) {
  const n = cnodes.map((x) => `  "${x.id}" [label="${x.name}"];`).join("\n");
  const e = cedges.map((x) => `  "${x.src}" -> "${x.dst}" [label="${x.rel}"];`).join("\n");
  return `digraph concepts {\n${n}\n${e}\n}\n`;
}

const csvs = conceptsCsv(concepts.nodes, concepts.edges);
const cGraphml = conceptsGraphML(concepts.nodes, concepts.edges);
const cDot = conceptsDot(concepts.nodes, concepts.edges);
const cSvg = simpleSvg(concepts.nodes.map((n) => ({ id: n.id })));
await writeFile(join(outDir, "concepts-nodes.csv"), csvs.nodes);
await writeFile(join(outDir, "concepts-edges.csv"), csvs.edges);
await writeFile(join(outDir, "concepts.graphml"), cGraphml);
await writeFile(join(outDir, "concepts.dot"), cDot);
await writeFile(join(outDir, "concepts.svg"), cSvg);

assert(csvs.nodes.split("\n").length > concepts.nodes.length, "concept csv short");
assert(cGraphml.includes("<graphml") && cGraphml.includes("</graphml>"), "concept graphml broken");
assert(cDot.includes("digraph"), "dot broken");
assert(cSvg.includes("<svg"), "concept svg broken");

const byType = {};
for (const e of edges) byType[e.type] = (byType[e.type] || 0) + 1;
const byRel = {};
for (const e of concepts.edges) byRel[e.rel] = (byRel[e.rel] || 0) + 1;
console.log(
  JSON.stringify(
    {
      ok: true,
      nodes: nodes.length,
      edges: edges.length,
      edges_by_type: byType,
      concepts: concepts.nodes.length,
      concept_edges: concepts.edges.length,
      concept_rels: byRel,
      gaps: Object.fromEntries(["G1", "G2", "G3", "G4", "G5", "G6"].map((k) => [k, (gaps[k] || []).length])),
      wrote: [
        "export-out/records.csv",
        "export-out/graph.graphml",
        "export-out/network.svg",
        "export-out/concepts-nodes.csv",
        "export-out/concepts-edges.csv",
        "export-out/concepts.graphml",
        "export-out/concepts.dot",
        "export-out/concepts.svg",
      ],
    },
    null,
    2,
  ),
);
