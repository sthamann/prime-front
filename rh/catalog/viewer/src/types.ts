export type EdgeType =
  | "DEPENDS"
  | "SAME_ROUND"
  | "SHARED_LEDGER"
  | "SUPERSEDES"
  | "SEMANTIC"
  | "FAMILY";

export interface Artifacts {
  probe?: string | null;
  result_json?: string | null;
  tex?: string | null;
  lean?: string[];
  figures?: string[];
}

export interface GraphNode {
  id: string;
  path: string;
  abs_path: string;
  round: string;
  round_num: number;
  role: string;
  ledger_ids: string[];
  kind: string;
  family: string;
  family_secondary: string[];
  outcome: string;
  failure_class: string;
  rh_relevance: string;
  question: string;
  mechanism: string;
  result_verdict: string;
  solved: string;
  failed_because: string;
  reusable: string;
  depends_on: string[];
  artifacts: Artifacts;
  confidence: string;
  draft: boolean;
  needs_review: boolean;
  reconciled: unknown;
  superseded_by: string | string[] | null;
  readme_lines: string;
  status_raw: string;
  score: number;
  size?: number;
  x?: number;
  y?: number;
  vx?: number;
  vy?: number;
  fx?: number | null;
  fy?: number | null;
}

export interface GraphEdge {
  source: string | GraphNode;
  target: string | GraphNode;
  type: EdgeType;
  weight?: number;
}

export interface GraphMeta {
  claim_boundary: string;
  generated: string;
  catalog_generated: string | null;
  n_nodes: number;
  n_edges: number;
  edges_by_type: Record<string, number>;
  n_curated: number;
  n_draft: number;
  semantic: boolean;
  n_vectors: number;
  taxonomy: {
    families: Record<string, string>;
    kinds: Record<string, string>;
    outcomes: Record<string, string>;
    failure_classes: Record<string, string>;
    rh_relevances: Record<string, string>;
  };
  orders: {
    families: string[];
    outcomes: string[];
    kinds: string[];
    failure_classes: string[];
    rh_relevances: string[];
  };
  edge_types?: string[];
  round_min?: number;
  round_max?: number;
  layout?: { engine: string; iterations: number; seed: number };
}

export interface GraphData {
  meta: GraphMeta;
  nodes: GraphNode[];
  edges: GraphEdge[];
}

export interface MatrixBlock {
  rows: string[];
  cols: string[];
  cells: { row: string; col: string; n: number }[];
}

export interface MatrixData {
  meta: { generated: string; n_nodes: number };
  family_x_outcome: MatrixBlock;
  family_x_failure_class: MatrixBlock;
  kind_x_outcome: MatrixBlock;
  curated_vs_draft: { curated: number; draft: number; needs_review: number };
  t1: unknown[];
}

export interface TimelineItem {
  id: string;
  round: string;
  round_num: number;
  family: string;
  outcome: string;
  kind: string;
  draft: boolean;
  score: number;
}

export interface TimelineData {
  items: TimelineItem[];
  min_round: number;
  max_round: number;
  n_unnumbered: number;
}

export interface KillMember {
  round: string;
  path: string;
}

export interface KillCluster {
  root_phrase?: string;
  failure_class?: string;
  count: number;
  structural_root?: string;
  members: KillMember[];
}

export interface KillsData {
  killed_total: number | null;
  by_failure_class: KillCluster[];
  clusters: KillCluster[];
}

export interface OrphanRow {
  rank: number;
  round: string;
  path: string;
  family: string;
  reusable: string;
  potential: string;
  consumer_family: string;
}

export interface OrphansData {
  eligible_total: number | null;
  ranked: OrphanRow[];
}

export interface PairRow {
  a: string;
  b: string;
  screen: string;
  why: string;
  constraint: string;
}

export interface PairsData {
  family_count: number | null;
  observed_pairs: number | null;
  never_tried_count: number | null;
  pairs: PairRow[];
  top_8: unknown[];
}

export interface ConflictRecord {
  round: string;
  path: string;
  outcome: string;
  verdict: string;
}

export interface ConflictItem {
  object: string;
  family: string;
  records: ConflictRecord[];
  reconciliation: string;
}

export interface ConflictsData {
  items: ConflictItem[];
}

export interface MissChain {
  round: string;
  path: string;
}

export interface MissItem {
  name: string;
  chain: MissChain[];
  new_theorem?: string;
  loss_free?: string;
  assessment?: string;
  assessment_why?: string;
  smallest_test?: string;
}

export interface MissesData {
  verdict: string;
  surviving_candidates: MissItem[];
  nearest_misses: MissItem[];
}

export interface VectorsData {
  dim: number;
  ids: string[];
  vectors: number[][];
}

export type ViewId = "network" | "timeline" | "matrices" | "kills" | "concepts" | "export";

export type ConceptType =
  | "OBJECT"
  | "CRITERION"
  | "THEOREM"
  | "CLASS"
  | "GEOMETRY"
  | "TFPT_STRUCTURE"
  | "OPERATOR"
  | "INVARIANT"
  | "METHOD"
  | "OPEN_QUESTION"
  | "BARRIER";

export type ConceptStatus =
  | "CLASSICAL"
  | "PROVED_HERE"
  | "FORMALIZED_LEAN"
  | "CONJECTURAL"
  | "KILLED_HERE"
  | "OPEN";

export type ConceptRel =
  | "EQUIVALENT_TO"
  | "IMPLIES"
  | "IMPLIED_BY"
  | "REDUCES_TO"
  | "SPECIAL_CASE_OF"
  | "GENERALIZES"
  | "INSTANCE_OF"
  | "REALIZES"
  | "TRANSFORM_OF"
  | "DUAL_TO"
  | "REQUIRES"
  | "WOULD_CLOSE"
  | "BLOCKED_BY"
  | "USED_BY"
  | "KILLED_BY"
  | "CO_OCCURS";

export type ConceptStrength = "THEOREM" | "CONDITIONAL" | "HEURISTIC" | "STATISTICAL";

export type RelGroup =
  | "equivalence"
  | "implication"
  | "requires"
  | "would_close"
  | "blocked"
  | "attempts"
  | "co_occurs";

export interface ConceptLayoutHint {
  group?: string;
  ring_radius?: number;
}

export interface ConceptNode {
  id: string;
  type: ConceptType;
  name: string;
  aliases: string[];
  definition: string;
  status: ConceptStatus;
  sources: string[];
  tags: string[];
  attempt_count: number;
  alive: boolean;
  layout_hint?: ConceptLayoutHint;
  size?: number;
  x?: number;
  y?: number;
  vx?: number;
  vy?: number;
  fx?: number | null;
  fy?: number | null;
}

export interface ConceptEdge {
  src: string;
  dst: string;
  rel: ConceptRel;
  strength: ConceptStrength;
  source: string;
  note: string;
  weight?: number;
}

export interface ConceptsData {
  claim_boundary: string;
  generated_at?: string;
  nodes: ConceptNode[];
  edges: ConceptEdge[];
}

export interface GapsG1 { id: string; type: string }
export interface GapsG2 { id: string; status: string }
export interface GapsG3 { pair: [string, string] | string[]; attempt_score: number }
export interface GapsG4 { id: string; killed_by: number }
export interface GapsG5 { id: string; path: string[]; hops: number | null }
export interface GapsG6 { id: string; targets: string[]; alive_targets: number; target_count: number }

export interface GapsData {
  G1: GapsG1[];
  G2: GapsG2[];
  G3: GapsG3[];
  G4: GapsG4[];
  G5: GapsG5[];
  G6: GapsG6[];
}

export interface ConceptFilters {
  types: Set<string>;
  statuses: Set<string>;
  relGroups: Set<RelGroup>;
  minStrength: number;
  aliveOnly: boolean;
  showAttempts: boolean;
  avoidKilled: boolean;
  query: string;
  showLabels: boolean;
}

export const CONCEPT_TYPES: ConceptType[] = [
  "OBJECT",
  "CRITERION",
  "THEOREM",
  "CLASS",
  "GEOMETRY",
  "TFPT_STRUCTURE",
  "OPERATOR",
  "INVARIANT",
  "METHOD",
  "OPEN_QUESTION",
  "BARRIER",
];

export const CONCEPT_STATUSES: ConceptStatus[] = [
  "CLASSICAL",
  "PROVED_HERE",
  "FORMALIZED_LEAN",
  "CONJECTURAL",
  "KILLED_HERE",
  "OPEN",
];

export const REL_GROUPS: RelGroup[] = [
  "equivalence",
  "implication",
  "requires",
  "would_close",
  "blocked",
  "attempts",
  "co_occurs",
];

export const REL_TO_GROUP: Record<ConceptRel, RelGroup> = {
  EQUIVALENT_TO: "equivalence",
  DUAL_TO: "equivalence",
  IMPLIES: "implication",
  IMPLIED_BY: "implication",
  REDUCES_TO: "implication",
  SPECIAL_CASE_OF: "implication",
  GENERALIZES: "implication",
  INSTANCE_OF: "implication",
  REALIZES: "implication",
  TRANSFORM_OF: "implication",
  REQUIRES: "requires",
  WOULD_CLOSE: "would_close",
  BLOCKED_BY: "blocked",
  USED_BY: "attempts",
  KILLED_BY: "attempts",
  CO_OCCURS: "co_occurs",
};

export const STRENGTH_RANK: Record<ConceptStrength, number> = {
  STATISTICAL: 0,
  HEURISTIC: 1,
  CONDITIONAL: 2,
  THEOREM: 3,
};

export const EMPTY_CONCEPTS: ConceptsData = {
  claim_boundary: "Research documentation. NO RH CLAIM.",
  nodes: [],
  edges: [],
};

export const EMPTY_GAPS: GapsData = { G1: [], G2: [], G3: [], G4: [], G5: [], G6: [] };

export interface Filters {
  kinds: Set<string>;
  outcomes: Set<string>;
  families: Set<string>;
  relevances: Set<string>;
  failures: Set<string>;
  curatedOnly: boolean;
  roundMin: number;
  roundMax: number;
  includeUnnumbered: boolean;
  query: string;
  edgeTypes: Set<EdgeType>;
  showHulls: boolean;
  showLabels: boolean;
}

export const ALL_EDGE_TYPES: EdgeType[] = [
  "DEPENDS",
  "SAME_ROUND",
  "SHARED_LEDGER",
  "SUPERSEDES",
  "SEMANTIC",
  "FAMILY",
];
