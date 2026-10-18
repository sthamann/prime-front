/** Restrained family palette — stable across views. */

export const FAMILY_COLORS: Record<string, string> = {
  WEIL_POSITIVITY_WINDOWS: "#6ea8ff",
  SCREW_SUBORDINATION_LSTAR: "#f0b45a",
  LEAN_FORMALIZATION: "#7dd3a8",
  EXPLICIT_FORMULA_IDENTITY: "#c9a0ff",
  OPERATOR_SPECTRAL: "#ff8a7a",
  RHP_IIKS_TAU: "#5fd0d4",
  TOEPLITZ_MOMENT_POSITIVITY: "#e6d36a",
  MELLIN_PICK_LEE_YANG: "#f48fb1",
  LATTICE_E8_HECKE: "#9ccc65",
  ADELIC_GROUPOID_CONNES: "#80cbc4",
  ARAKELOV_HODGE_INTERSECTION: "#ce93d8",
  CM_CURVE_GEOMETRY: "#ffab91",
  DYNAMICS_CLOCKS_PF: "#90caf9",
  SELBERG_TRACE_CONTACT: "#a5d6a7",
  PRIME_EVENT_LOG_DECODING: "#fff59d",
  SIEVE_FACTORING_GEOMETRY: "#bcaaa4",
  CERTIFICATE_INFRASTRUCTURE: "#b0bec5",
  EXTERNAL_ADJUDICATION: "#ef9a9a",
  OTHER: "#8b919d",
};

export const OUTCOME_STROKE: Record<string, string> = {
  KILLED: "#e85d5d",
  CERTIFIED: "#3dcf8e",
  PROVED: "#2ee6a6",
  OPEN: "#e8b84a",
  INCONCLUSIVE: "#7d8490",
  MEASURED: "#7eb8e8",
  SEALED: "#9aa3b2",
  RESTATED: "#6b7280",
};

export const EDGE_STYLE: Record<
  string,
  { color: string; width: number; dash: string; opacity: number }
> = {
  DEPENDS: { color: "#c9d4e8", width: 1.15, dash: "", opacity: 0.42 },
  SAME_ROUND: { color: "#8fa4c8", width: 0.7, dash: "2 3", opacity: 0.22 },
  SHARED_LEDGER: { color: "#d4b06a", width: 0.85, dash: "5 3", opacity: 0.28 },
  SUPERSEDES: { color: "#e8d08a", width: 1.4, dash: "", opacity: 0.7 },
  SEMANTIC: { color: "#7ec8c4", width: 0.9, dash: "1 4", opacity: 0.32 },
  FAMILY: { color: "#5a6270", width: 0.55, dash: "6 5", opacity: 0.14 },
};

const FALLBACK = [
  "#6ea8ff",
  "#f0b45a",
  "#7dd3a8",
  "#c9a0ff",
  "#ff8a7a",
  "#5fd0d4",
  "#e6d36a",
  "#f48fb1",
];

export function familyColor(family: string): string {
  if (FAMILY_COLORS[family]) return FAMILY_COLORS[family];
  let h = 0;
  for (let i = 0; i < family.length; i++) h = (h * 31 + family.charCodeAt(i)) >>> 0;
  return FALLBACK[h % FALLBACK.length];
}

export function outcomeStroke(outcome: string): string {
  return OUTCOME_STROKE[outcome] || "#8b919d";
}

export function shortFamily(family: string): string {
  return family.replace(/_/g, " ").replace(/\b([A-Z])[A-Z]+\b/g, "$1");
}

export const CONCEPT_TYPE_COLORS: Record<string, string> = {
  OBJECT: "#8eb4e8",
  CRITERION: "#f0c36e",
  THEOREM: "#7dd3a8",
  CLASS: "#c9a0ff",
  GEOMETRY: "#80cbc4",
  TFPT_STRUCTURE: "#ffab91",
  OPERATOR: "#ff8a7a",
  INVARIANT: "#90caf9",
  METHOD: "#b0bec5",
  OPEN_QUESTION: "#e8b84a",
  BARRIER: "#e85d5d",
};

export const CONCEPT_STATUS_STROKE: Record<string, string> = {
  KILLED_HERE: "#e85d5d",
  PROVED_HERE: "#3dcf8e",
  FORMALIZED_LEAN: "#2ee6a6",
  OPEN: "#e8b84a",
  CLASSICAL: "#8b919d",
  CONJECTURAL: "#c9a0ff",
};

export const REL_GROUP_STYLE: Record<string, { color: string; dash: string; arrow: boolean; double: boolean }> = {
  equivalence: { color: "#d4c48a", dash: "", arrow: false, double: true },
  implication: { color: "#9aa8c4", dash: "", arrow: true, double: false },
  requires: { color: "#8fa4c8", dash: "5 4", arrow: false, double: false },
  would_close: { color: "#3dcf8e", dash: "6 4", arrow: true, double: false },
  blocked: { color: "#e85d5d", dash: "", arrow: true, double: false },
  attempts: { color: "#6b7380", dash: "1 4", arrow: false, double: false },
  co_occurs: { color: "#7ec8c4", dash: "2 3", arrow: false, double: false },
};

export function conceptTypeColor(t: string): string {
  return CONCEPT_TYPE_COLORS[t] || "#8b919d";
}

export function conceptStatusStroke(s: string): string {
  return CONCEPT_STATUS_STROKE[s] || "#8b919d";
}

export function strengthStyle(s: string): { width: number; opacity: number } {
  if (s === "THEOREM") return { width: 1.85, opacity: 0.88 };
  if (s === "CONDITIONAL") return { width: 1.3, opacity: 0.62 };
  if (s === "STATISTICAL") return { width: 0.7, opacity: 0.28 };
  return { width: 0.95, opacity: 0.42 };
}

export function heatColor(t: number): string {
  const x = Math.max(0, Math.min(1, t));
  const r = Math.round(18 + x * 210);
  const g = Math.round(28 + x * 140);
  const b = Math.round(48 + (1 - x) * 40);
  return `rgb(${r},${g},${b})`;
}
