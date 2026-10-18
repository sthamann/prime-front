import type {
  ConceptEdge,
  ConceptFilters,
  ConceptNode,
  ConceptsData,
  ConflictsData,
  EdgeType,
  Filters,
  GapsData,
  GraphData,
  GraphEdge,
  GraphNode,
  KillsData,
  MatrixData,
  MissesData,
  OrphansData,
  PairsData,
  TimelineData,
  VectorsData,
} from "./types";
import {
  ALL_EDGE_TYPES,
  CONCEPT_STATUSES,
  CONCEPT_TYPES,
  EMPTY_CONCEPTS,
  EMPTY_GAPS,
  REL_GROUPS,
  REL_TO_GROUP,
  STRENGTH_RANK,
} from "./types";

export interface Bundle {
  graph: GraphData;
  matrix: MatrixData;
  timeline: TimelineData;
  kills: KillsData;
  orphans: OrphansData;
  pairs: PairsData;
  conflicts: ConflictsData;
  misses: MissesData;
  vectors: VectorsData | null;
  concepts: ConceptsData;
  gaps: GapsData;
}

async function fetchJson<T>(url: string): Promise<T> {
  const res = await fetch(url);
  if (!res.ok) throw new Error(`${url} ${res.status}`);
  return res.json() as Promise<T>;
}

type CoreNode = Pick<
  GraphNode,
  | "id"
  | "x"
  | "y"
  | "size"
  | "kind"
  | "outcome"
  | "family"
  | "round"
  | "draft"
  | "path"
  | "score"
  | "round_num"
  | "rh_relevance"
  | "failure_class"
>;

export interface GraphCoreFile {
  meta: GraphData["meta"];
  nodes: CoreNode[];
  edges: [number, number, number][];
}

const RECORD_STUB: Pick<
  GraphNode,
  | "abs_path"
  | "role"
  | "ledger_ids"
  | "family_secondary"
  | "question"
  | "mechanism"
  | "result_verdict"
  | "solved"
  | "failed_because"
  | "reusable"
  | "depends_on"
  | "artifacts"
  | "confidence"
  | "needs_review"
  | "reconciled"
  | "superseded_by"
  | "readme_lines"
  | "status_raw"
> = {
  abs_path: "",
  role: "",
  ledger_ids: [],
  family_secondary: [],
  question: "",
  mechanism: "",
  result_verdict: "",
  solved: "",
  failed_because: "",
  reusable: "",
  depends_on: [],
  artifacts: {},
  confidence: "",
  needs_review: false,
  reconciled: null,
  superseded_by: null,
  readme_lines: "",
  status_raw: "",
};

const EMPTY_BLOCK = { rows: [] as string[], cols: [] as string[], cells: [] as { row: string; col: string; n: number }[] };

export const EMPTY_MATRIX: MatrixData = {
  meta: { generated: "", n_nodes: 0 },
  family_x_outcome: EMPTY_BLOCK,
  family_x_failure_class: EMPTY_BLOCK,
  kind_x_outcome: EMPTY_BLOCK,
  curated_vs_draft: { curated: 0, draft: 0, needs_review: 0 },
  t1: [],
};

export const EMPTY_TIMELINE: TimelineData = { items: [], min_round: 0, max_round: 0, n_unnumbered: 0 };
export const EMPTY_KILLS: KillsData = { killed_total: null, by_failure_class: [], clusters: [] };
export const EMPTY_ORPHANS: OrphansData = { eligible_total: null, ranked: [] };
export const EMPTY_PAIRS: PairsData = { family_count: null, observed_pairs: null, never_tried_count: null, pairs: [], top_8: [] };
export const EMPTY_CONFLICTS: ConflictsData = { items: [] };
export const EMPTY_MISSES: MissesData = { verdict: "", surviving_candidates: [], nearest_misses: [] };

export function emptySidecars(): Omit<Bundle, "graph"> {
  return {
    matrix: EMPTY_MATRIX,
    timeline: EMPTY_TIMELINE,
    kills: EMPTY_KILLS,
    orphans: EMPTY_ORPHANS,
    pairs: EMPTY_PAIRS,
    conflicts: EMPTY_CONFLICTS,
    misses: EMPTY_MISSES,
    vectors: null,
    concepts: EMPTY_CONCEPTS,
    gaps: EMPTY_GAPS,
  };
}

function nodeFromCore(n: CoreNode): GraphNode {
  return { ...RECORD_STUB, ...n, draft: !!n.draft };
}

export function expandCore(core: GraphCoreFile): GraphData {
  const types = (core.meta.edge_types || ALL_EDGE_TYPES) as EdgeType[];
  const nodes = core.nodes.map(nodeFromCore);
  const edges: GraphEdge[] = [];
  for (const trip of core.edges) {
    const [si, ti, k] = trip;
    const s = nodes[si];
    const t = nodes[ti];
    const type = types[k];
    if (!s || !t || !type) continue;
    edges.push({ source: s.id, target: t.id, type });
  }
  return {
    meta: { ...core.meta, n_nodes: nodes.length, n_edges: edges.length },
    nodes,
    edges,
  };
}

export async function loadGraphCore(): Promise<GraphData> {
  try {
    return expandCore(await fetchJson<GraphCoreFile>("data/graph_core.json"));
  } catch {
    return fetchJson<GraphData>("data/graph.json");
  }
}

export async function mergeRecords(graph: GraphData): Promise<void> {
  try {
    const recs = await fetchJson<Record<string, Partial<GraphNode>>>("data/records.json");
    for (const n of graph.nodes) {
      const r = recs[n.id];
      if (r) Object.assign(n, r);
    }
  } catch {
    /* dossier stubs remain */
  }
}

export async function loadSidecars(graph: GraphData): Promise<Omit<Bundle, "graph">> {
  const [matrix, timeline, kills, orphans, pairs, conflicts, misses] = await Promise.all([
    fetchJson<MatrixData>("data/matrix.json"),
    fetchJson<TimelineData>("data/timeline.json"),
    fetchJson<KillsData>("data/kills.json"),
    fetchJson<OrphansData>("data/orphans.json"),
    fetchJson<PairsData>("data/pairs.json"),
    fetchJson<ConflictsData>("data/conflicts.json"),
    fetchJson<MissesData>("data/misses.json"),
  ]);
  let vectors: VectorsData | null = null;
  if (graph.meta.semantic) {
    try {
      const v = await fetchJson<VectorsData>("data/vectors.json");
      if (v.dim > 0 && v.ids.length) vectors = v;
    } catch {
      vectors = null;
    }
  }
  let concepts: ConceptsData = EMPTY_CONCEPTS;
  let gaps: GapsData = EMPTY_GAPS;
  try {
    concepts = await fetchJson<ConceptsData>("data/concepts.json");
  } catch {
    concepts = EMPTY_CONCEPTS;
  }
  try {
    gaps = await fetchJson<GapsData>("data/gaps_report.json");
  } catch {
    gaps = EMPTY_GAPS;
  }
  return { matrix, timeline, kills, orphans, pairs, conflicts, misses, vectors, concepts, gaps };
}

export async function loadBundle(): Promise<Bundle> {
  const graph = await loadGraphCore();
  await mergeRecords(graph);
  const rest = await loadSidecars(graph);
  return { graph, ...rest };
}

export function defaultConceptFilters(): ConceptFilters {
  return {
    types: new Set(CONCEPT_TYPES),
    statuses: new Set(CONCEPT_STATUSES),
    relGroups: new Set(REL_GROUPS.filter((g) => g !== "attempts")),
    minStrength: 0,
    aliveOnly: false,
    showAttempts: false,
    avoidKilled: false,
    query: "",
    showLabels: true,
  };
}

export function conceptMatches(n: ConceptNode, f: ConceptFilters): boolean {
  if (!f.types.has(n.type)) return false;
  if (!f.statuses.has(n.status)) return false;
  if (f.aliveOnly && !n.alive) return false;
  if (f.query.trim()) {
    const q = f.query.trim().toLowerCase();
    const hay = [n.id, n.name, n.definition, ...(n.aliases || []), ...(n.tags || [])]
      .join(" ")
      .toLowerCase();
    if (!hay.includes(q)) return false;
  }
  return true;
}

export function conceptEdgeVisible(e: ConceptEdge, f: ConceptFilters, vis: Set<string>): boolean {
  const group = REL_TO_GROUP[e.rel];
  if (group === "attempts" && !f.showAttempts) return false;
  if (!f.relGroups.has(group) && !(group === "attempts" && f.showAttempts)) return false;
  if ((STRENGTH_RANK[e.strength] ?? 0) < f.minStrength) return false;
  if (group === "attempts") return vis.has(e.src);
  return vis.has(e.src) && vis.has(e.dst);
}

export function conceptsForPath(concepts: ConceptsData, path: string): ConceptNode[] {
  const ids = new Set<string>();
  for (const e of concepts.edges) {
    if ((e.rel === "USED_BY" || e.rel === "KILLED_BY") && e.dst === path) ids.add(e.src);
  }
  return concepts.nodes.filter((n) => ids.has(n.id));
}

export function attemptsForConcept(concepts: ConceptsData, id: string): ConceptEdge[] {
  return concepts.edges.filter((e) => e.src === id && (e.rel === "USED_BY" || e.rel === "KILLED_BY"));
}

export function edgeKey(e: { src: string; dst: string; rel: string }): string {
  return `${e.src}|${e.rel}|${e.dst}`;
}

export function shortestConceptPaths(
  nodes: ConceptNode[],
  edges: ConceptEdge[],
  a: string,
  b: string,
  maxHops = 5,
  avoidKilled = false,
): { hops: number; paths: string[][] } {
  const killed = new Set(nodes.filter((n) => n.status === "KILLED_HERE").map((n) => n.id));
  const adj = new Map<string, string[]>();
  const add = (u: string, v: string) => {
    if (!adj.has(u)) adj.set(u, []);
    adj.get(u)!.push(v);
  };
  for (const e of edges) {
    if (e.rel === "USED_BY" || e.rel === "KILLED_BY") continue;
    if (avoidKilled && e.rel === "KILLED_BY") continue;
    if (avoidKilled && killed.has(e.src) && e.src !== a && e.src !== b) continue;
    if (avoidKilled && killed.has(e.dst) && e.dst !== a && e.dst !== b) continue;
    add(e.src, e.dst);
    add(e.dst, e.src);
  }
  const dist = new Map<string, number>();
  const parents = new Map<string, string[]>();
  const q = [a];
  dist.set(a, 0);
  for (let i = 0; i < q.length; i++) {
    const u = q[i];
    const du = dist.get(u) ?? 0;
    if (du >= maxHops) continue;
    for (const v of adj.get(u) || []) {
      if (avoidKilled && killed.has(v) && v !== a && v !== b) continue;
      const nv = du + 1;
      if (!dist.has(v)) {
        dist.set(v, nv);
        parents.set(v, [u]);
        q.push(v);
      } else if (dist.get(v) === nv) {
        parents.get(v)!.push(u);
      }
    }
  }
  if (!dist.has(b)) return { hops: -1, paths: [] };
  const hops = dist.get(b)!;
  const paths: string[][] = [];
  const walk = (cur: string, acc: string[]) => {
    if (cur === a) {
      paths.push([a, ...acc.slice().reverse()]);
      return;
    }
    for (const p of parents.get(cur) || []) walk(p, [...acc, cur]);
  };
  walk(b, []);
  return { hops, paths };
}

export function defaultFilters(graph: GraphData, timeline: TimelineData): Filters {
  return {
    kinds: new Set(graph.meta.orders.kinds),
    outcomes: new Set(graph.meta.orders.outcomes),
    families: new Set(graph.meta.orders.families),
    relevances: new Set(graph.meta.orders.rh_relevances),
    failures: new Set(graph.meta.orders.failure_classes),
    curatedOnly: false,
    roundMin: timeline.items.length ? timeline.min_round : (graph.meta.round_min ?? timeline.min_round),
    roundMax: timeline.items.length ? timeline.max_round : (graph.meta.round_max ?? timeline.max_round),
    includeUnnumbered: true,
    query: "",
    edgeTypes: new Set<EdgeType>(
      ALL_EDGE_TYPES.filter((t) => t === "DEPENDS" || t === "SUPERSEDES" || t === "SHARED_LEDGER"),
    ),
    showHulls: false,
    showLabels: false,
  };
}

export function nodeMatches(n: GraphNode, f: Filters): boolean {
  if (!f.kinds.has(n.kind)) return false;
  if (!f.outcomes.has(n.outcome)) return false;
  if (!f.families.has(n.family)) return false;
  if (!f.relevances.has(n.rh_relevance)) return false;
  if (!f.failures.has(n.failure_class)) return false;
  if (f.curatedOnly && n.draft) return false;
  if (n.round_num < 0) {
    if (!f.includeUnnumbered) return false;
  } else if (n.round_num < f.roundMin || n.round_num > f.roundMax) {
    return false;
  }
  if (f.query.trim()) {
    const q = f.query.trim().toLowerCase();
    const hay = [
      n.path,
      n.round,
      n.question,
      n.mechanism,
      n.result_verdict,
      n.solved,
      n.failed_because,
      n.family,
      n.kind,
      n.outcome,
      ...(n.ledger_ids || []),
    ]
      .join(" ")
      .toLowerCase();
    if (!hay.includes(q)) return false;
  }
  return true;
}

export function filterNodes(nodes: GraphNode[], f: Filters): GraphNode[] {
  return nodes.filter((n) => nodeMatches(n, f));
}

export function edgeId(e: GraphEdge): { s: string; t: string } {
  const s = typeof e.source === "string" ? e.source : e.source.id;
  const t = typeof e.target === "string" ? e.target : e.target.id;
  return { s, t };
}

export function cosine(a: number[], b: number[]): number {
  let dot = 0;
  for (let i = 0; i < a.length; i++) dot += a[i] * b[i];
  return dot;
}

export function similarTo(
  id: string,
  vectors: VectorsData,
  k = 12,
): { id: string; sim: number }[] {
  const i = vectors.ids.indexOf(id);
  if (i < 0) return [];
  const q = vectors.vectors[i];
  const scored: { id: string; sim: number }[] = [];
  for (let j = 0; j < vectors.ids.length; j++) {
    if (j === i) continue;
    scored.push({ id: vectors.ids[j], sim: cosine(q, vectors.vectors[j]) });
  }
  scored.sort((a, b) => b.sim - a.sim);
  return scored.slice(0, k);
}

export function basename(p: string): string {
  const i = p.lastIndexOf("/");
  return i >= 0 ? p.slice(i + 1) : p;
}
