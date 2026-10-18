import type { Bundle } from "./data";
import type { ConceptFilters, ConceptNode, Filters, GraphNode, ViewId } from "./types";

type Listener = () => void;

export class AppState {
  bundle: Bundle;
  filters: Filters;
  conceptFilters: ConceptFilters;
  view: ViewId = "network";
  selected: GraphNode | null = null;
  selectedConcept: ConceptNode | null = null;
  highlighted = new Set<string>();
  conceptHighlighted = new Set<string>();
  conceptPathEdges = new Set<string>();
  conceptPathEnds: [string | null, string | null] = [null, null];
  conceptPathHops = -1;
  pinned = new Set<string>();
  similar: { id: string; sim: number }[] = [];
  private listeners: Listener[] = [];

  constructor(bundle: Bundle, filters: Filters, conceptFilters: ConceptFilters) {
    this.bundle = bundle;
    this.filters = filters;
    this.conceptFilters = conceptFilters;
  }

  on(fn: Listener): () => void {
    this.listeners.push(fn);
    return () => {
      this.listeners = this.listeners.filter((x) => x !== fn);
    };
  }

  emit(): void {
    for (const fn of this.listeners) fn();
  }

  setView(v: ViewId): void {
    if (this.view === v) return;
    this.view = v;
    this.emit();
  }

  select(node: GraphNode | null, neighbors?: string[]): void {
    this.selected = node;
    this.selectedConcept = null;
    this.highlighted = new Set(neighbors || []);
    if (node) this.highlighted.add(node.id);
    this.emit();
  }

  selectConcept(node: ConceptNode | null, highlight?: string[]): void {
    this.selectedConcept = node;
    this.selected = null;
    this.conceptHighlighted = new Set(highlight || []);
    if (node) this.conceptHighlighted.add(node.id);
    this.emit();
  }

  highlightConceptChain(ids: string[], edgeKeys: string[] = []): void {
    this.conceptHighlighted = new Set(ids);
    this.conceptPathEdges = new Set(edgeKeys);
    this.emit();
  }

  setPathEnds(a: string | null, b: string | null, hops = -1, ids: string[] = [], edgeKeys: string[] = []): void {
    this.conceptPathEnds = [a, b];
    this.conceptPathHops = hops;
    this.conceptHighlighted = new Set(ids);
    this.conceptPathEdges = new Set(edgeKeys);
    this.emit();
  }

  patchConceptFilters(partial: Partial<ConceptFilters>): void {
    this.conceptFilters = { ...this.conceptFilters, ...partial };
    this.emit();
  }

  openConcept(id: string): void {
    const node = this.bundle.concepts.nodes.find((n) => n.id === id) || null;
    this.view = "concepts";
    this.selectConcept(node, node ? [node.id] : []);
  }

  showConceptInNetwork(id: string): void {
    const paths = this.bundle.concepts.edges
      .filter((e) => e.src === id && (e.rel === "USED_BY" || e.rel === "KILLED_BY"))
      .map((e) => e.dst);
    const recs = this.bundle.graph.nodes.filter((n) => paths.includes(n.path));
    this.view = "network";
    if (recs.length) this.select(recs[0], recs.map((r) => r.id));
    else {
      this.selected = null;
      this.highlighted = new Set();
      this.emit();
    }
  }

  togglePin(id: string): void {
    if (this.pinned.has(id)) this.pinned.delete(id);
    else this.pinned.add(id);
    this.emit();
  }

  patchFilters(partial: Partial<Filters>): void {
    this.filters = { ...this.filters, ...partial };
    this.emit();
  }

  applyMatrixCell(rowKey: "family" | "kind" | "failure", row: string, colKey: "outcome" | "failure_class", col: string): void {
    const next = { ...this.filters };
    if (rowKey === "family") next.families = new Set([row]);
    if (rowKey === "kind") next.kinds = new Set([row]);
    if (colKey === "outcome") next.outcomes = new Set([col]);
    if (colKey === "failure_class") next.failures = new Set([col]);
    this.filters = next;
    this.view = "network";
    this.emit();
  }

  applyRoundBrush(min: number, max: number): void {
    this.filters = { ...this.filters, roundMin: min, roundMax: max };
    this.emit();
  }
}
