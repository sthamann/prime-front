#!/usr/bin/env node
/** Deterministic FA2 + noverlap layout. Writes x,y into graph.json / concepts.json
 *  and splits graph_core.json + records.json. No RH claim. */
import { readFile, writeFile } from "node:fs/promises";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";
import Graph from "graphology";
import forceAtlas2 from "graphology-layout-forceatlas2";
import noverlap from "graphology-layout-noverlap";

const root = join(dirname(fileURLToPath(import.meta.url)), "..");
const dataDir = join(root, "public", "data");
const SEED = 32;
const EDGE_TYPES = ["DEPENDS", "SAME_ROUND", "SHARED_LEDGER", "SUPERSEDES", "SEMANTIC", "FAMILY"];
const LAYOUT_EDGES = new Set(["DEPENDS", "SUPERSEDES", "SHARED_LEDGER"]);

function hash01(s) {
  let h = 2166136261 ^ SEED;
  for (let i = 0; i < s.length; i++) h = Math.imul(h ^ s.charCodeAt(i), 16777619);
  return (h >>> 0) / 4294967296;
}

function dump(path, obj) {
  return writeFile(path, JSON.stringify(obj));
}

function layoutNetwork(nodes, edges) {
  const g = new Graph({ type: "undirected", multi: false, allowSelfLoops: false });
  const families = [...new Set(nodes.map((n) => n.family || "OTHER"))].sort();
  const famAngle = new Map(families.map((f, i) => [f, (i / Math.max(families.length, 1)) * Math.PI * 2]));
  for (const n of nodes) {
    const ang = famAngle.get(n.family || "OTHER") || 0;
    const jitter = hash01(n.id);
    const R = 8 + jitter * 4;
    const size = 2.2 + Math.sqrt(Math.max(n.score || 0.2, 0.2)) * 2.4;
    g.addNode(n.id, {
      x: Math.cos(ang) * R + (jitter - 0.5) * 1.4,
      y: Math.sin(ang) * R + (hash01(n.id + "y") - 0.5) * 1.4,
      size,
    });
  }
  for (const e of edges) {
    const s = typeof e.source === "string" ? e.source : e.source?.id;
    const t = typeof e.target === "string" ? e.target : e.target?.id;
    if (!LAYOUT_EDGES.has(e.type) || !s || !t || s === t) continue;
    if (!g.hasNode(s) || !g.hasNode(t) || g.hasEdge(s, t)) continue;
    g.addEdge(s, t, { weight: e.type === "DEPENDS" ? 2 : 1 });
  }
  const settings = {
    ...forceAtlas2.inferSettings(g),
    barnesHutOptimize: true,
    barnesHutTheta: 0.6,
    gravity: 0.8,
    scalingRatio: 8,
    slowDown: 4,
    strongGravityMode: false,
  };
  const t0 = Date.now();
  forceAtlas2.assign(g, { iterations: 140, settings, getEdgeWeight: "weight" });
  noverlap.assign(g, { maxIterations: 40, settings: { margin: 1.2, ratio: 1.1, speed: 3 } });
  console.log("network FA2+noverlap", g.order, "nodes", g.size, "edges", `${Date.now() - t0}ms`);
  const pos = {};
  g.forEachNode((id, attr) => {
    pos[id] = { x: +attr.x.toFixed(3), y: +attr.y.toFixed(3), size: +attr.size.toFixed(2) };
  });
  return pos;
}

function layoutConcepts(nodes) {
  const FALLBACK = {
    CRITERION: 180,
    OPEN_QUESTION: 140,
    THEOREM: 300,
    OBJECT: 390,
    OPERATOR: 470,
    INVARIANT: 540,
    METHOD: 610,
    GEOMETRY: 690,
    TFPT_STRUCTURE: 770,
    BARRIER: 850,
    CLASS: 930,
  };
  const byType = new Map();
  for (const n of nodes) {
    if (!byType.has(n.type)) byType.set(n.type, []);
    byType.get(n.type).push(n);
  }
  const pos = {};
  for (const [type, list] of byType) {
    list.forEach((n, i) => {
      const ang = (i / Math.max(list.length, 1)) * Math.PI * 2 + hash01(n.id) * 0.08;
      const R = n.layout_hint?.ring_radius || FALLBACK[type] || 500;
      pos[n.id] = {
        x: +(Math.cos(ang) * R).toFixed(2),
        y: +(Math.sin(ang) * R).toFixed(2),
        size: +(3.2 + Math.log1p(n.attempt_count || 0) * 2.1).toFixed(2),
      };
    });
  }
  return pos;
}

const graph = JSON.parse(await readFile(join(dataDir, "graph.json"), "utf8"));
const netPos = layoutNetwork(graph.nodes, graph.edges);
for (const n of graph.nodes) {
  const p = netPos[n.id];
  if (p) {
    n.x = p.x;
    n.y = p.y;
    n.size = p.size;
  }
}

const idIndex = new Map(graph.nodes.map((n, i) => [n.id, i]));
const compactEdges = [];
for (const e of graph.edges) {
  const s = typeof e.source === "string" ? e.source : e.source?.id;
  const t = typeof e.target === "string" ? e.target : e.target?.id;
  const si = idIndex.get(s);
  const ti = idIndex.get(t);
  const k = EDGE_TYPES.indexOf(e.type);
  if (si == null || ti == null || k < 0) continue;
  compactEdges.push([si, ti, k]);
}

const numbered = graph.nodes.map((n) => n.round_num).filter((x) => typeof x === "number" && x >= 0);
const core = {
  meta: {
    claim_boundary: graph.meta.claim_boundary,
    generated: graph.meta.generated,
    catalog_generated: graph.meta.catalog_generated,
    n_nodes: graph.nodes.length,
    n_edges: graph.edges.length,
    edges_by_type: graph.meta.edges_by_type,
    n_curated: graph.meta.n_curated,
    n_draft: graph.meta.n_draft,
    semantic: graph.meta.semantic,
    n_vectors: graph.meta.n_vectors,
    taxonomy: graph.meta.taxonomy,
    orders: graph.meta.orders,
    edge_types: EDGE_TYPES,
    round_min: numbered.length ? Math.min(...numbered) : 0,
    round_max: numbered.length ? Math.max(...numbered) : 0,
    layout: { engine: "forceatlas2+noverlap", iterations: 140, seed: SEED },
  },
  nodes: graph.nodes.map((n) => ({
    id: n.id,
    x: n.x,
    y: n.y,
    size: n.size,
    kind: n.kind,
    outcome: n.outcome,
    family: n.family,
    round: n.round,
    draft: !!n.draft,
    path: n.path,
    score: n.score,
    round_num: n.round_num,
    rh_relevance: n.rh_relevance,
    failure_class: n.failure_class,
  })),
  edges: compactEdges,
};

const records = {};
for (const n of graph.nodes) {
  records[n.id] = {
    abs_path: n.abs_path,
    role: n.role,
    ledger_ids: n.ledger_ids,
    family_secondary: n.family_secondary,
    question: n.question,
    mechanism: n.mechanism,
    result_verdict: n.result_verdict,
    solved: n.solved,
    failed_because: n.failed_because,
    reusable: n.reusable,
    depends_on: n.depends_on,
    artifacts: n.artifacts,
    confidence: n.confidence,
    needs_review: n.needs_review,
    reconciled: n.reconciled,
    superseded_by: n.superseded_by,
    readme_lines: n.readme_lines,
    status_raw: n.status_raw,
  };
}

await dump(join(dataDir, "graph.json"), graph);
await dump(join(dataDir, "graph_core.json"), core);
await dump(join(dataDir, "records.json"), records);

try {
  const concepts = JSON.parse(await readFile(join(dataDir, "concepts.json"), "utf8"));
  const cpos = layoutConcepts(concepts.nodes || []);
  for (const n of concepts.nodes || []) {
    const p = cpos[n.id];
    if (p) {
      n.x = p.x;
      n.y = p.y;
      n.size = p.size;
    }
  }
  await dump(join(dataDir, "concepts.json"), concepts);
  console.log("concepts laid out", (concepts.nodes || []).length);
} catch (err) {
  console.warn("concepts layout skipped", err instanceof Error ? err.message : err);
}

console.log(
  JSON.stringify({
    core_nodes: core.nodes.length,
    core_edges: core.edges.length,
    ok: true,
  }),
);
