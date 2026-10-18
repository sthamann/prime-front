import { renderConcepts } from "./concepts";
import {
  attemptsForConcept,
  conceptsForPath,
  defaultConceptFilters,
  defaultFilters,
  emptySidecars,
  filterNodes,
  loadGraphCore,
  loadSidecars,
  mergeRecords,
  similarTo,
} from "./data";
import { exportBundle } from "./export";
import { renderExport } from "./export";
import { renderKills } from "./kills";
import { renderMatrices } from "./matrices";
import { renderNetwork } from "./network";
import {
  CONCEPT_TYPE_COLORS,
  FAMILY_COLORS,
  conceptStatusStroke,
  conceptTypeColor,
  familyColor,
  outcomeStroke,
} from "./palette";
import { AppState } from "./state";
import { renderTimeline } from "./timeline";
import type { ConceptNode, EdgeType, GraphNode, RelGroup, ViewId } from "./types";
import { ALL_EDGE_TYPES, CONCEPT_STATUSES, CONCEPT_TYPES, REL_GROUPS } from "./types";
import "./styles.css";

const VIEWS: { id: ViewId; label: string }[] = [
  { id: "network", label: "Network" },
  { id: "concepts", label: "Concept map" },
  { id: "timeline", label: "Timeline" },
  { id: "matrices", label: "Matrices" },
  { id: "kills", label: "Kill roots" },
  { id: "export", label: "Export" },
];

function el<K extends keyof HTMLElementTagNameMap>(tag: K, cls?: string, html?: string): HTMLElementTagNameMap[K] {
  const n = document.createElement(tag);
  if (cls) n.className = cls;
  if (html != null) n.innerHTML = html;
  return n;
}

function fileLink(abs: string, rel: string, lines?: string): string {
  const href = lines && /^\d+-\d+$/.test(lines)
    ? `cursor://file/${abs}:${lines.split("-")[0]}`
    : `cursor://file/${abs}`;
  return `<a class="file" href="${href}">${esc(rel)}</a><code class="path">${esc(rel)}</code>`;
}

function esc(s: string): string {
  return String(s).replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" })[c]!);
}

function chipSet(
  title: string,
  values: string[],
  selected: Set<string>,
  onChange: (next: Set<string>) => void,
  colorFn?: (v: string) => string,
): HTMLElement {
  const box = el("fieldset", "chipset");
  const lab = el("legend", "", title);
  box.append(lab);
  const tools = el("div", "chip-tools");
  const all = el("button", "ghost", "all");
  const none = el("button", "ghost", "none");
  all.type = "button";
  none.type = "button";
  all.addEventListener("click", () => onChange(new Set(values)));
  none.addEventListener("click", () => onChange(new Set()));
  tools.append(all, none);
  box.append(tools);
  const row = el("div", "chips");
  for (const v of values) {
    const b = el("button", selected.has(v) ? "chip on" : "chip", v.replace(/_/g, " "));
    b.type = "button";
    if (colorFn) b.style.setProperty("--chip", colorFn(v));
    b.addEventListener("click", () => {
      const next = new Set(selected);
      if (next.has(v)) next.delete(v);
      else next.add(v);
      onChange(next);
    });
    row.append(b);
  }
  box.append(row);
  return box;
}

function dossierHtml(n: GraphNode, linkedConcepts: ConceptNode[] = []): string {
  const arts = n.artifacts || {};
  const artBits = [
    arts.probe ? fileLink(joinAbs(n, arts.probe), arts.probe) : "",
    arts.result_json ? fileLink(joinAbs(n, arts.result_json), arts.result_json) : "",
    arts.tex ? fileLink(joinAbs(n, arts.tex), arts.tex) : "",
    ...(arts.lean || []).map((p) => fileLink(joinAbs(n, p), p)),
    ...(arts.figures || []).map((p) => fileLink(joinAbs(n, p), p)),
  ].filter(Boolean);
  const readme = n.readme_lines
    ? `<p class="readme">README ${esc(n.readme_lines)}</p>`
    : "";
  return `
    <header>
      <span class="dot" style="background:${familyColor(n.family)};box-shadow:0 0 0 2px ${outcomeStroke(n.outcome)}"></span>
      <div>
        <h2>${esc(n.round || "—")}</h2>
        <p class="muted">${esc(n.family)} · ${esc(n.kind)} · ${esc(n.outcome)}</p>
      </div>
    </header>
    <dl>
      <dt>path</dt><dd>${fileLink(n.abs_path, n.path, n.readme_lines)}</dd>
      <dt>question</dt><dd>${esc(n.question || "—")}</dd>
      <dt>mechanism</dt><dd>${esc(n.mechanism || "—")}</dd>
      <dt>verdict</dt><dd>${esc(n.result_verdict || "—")}</dd>
      <dt>solved</dt><dd>${esc(n.solved || "—")}</dd>
      <dt>failed because</dt><dd>${esc(n.failed_because || "—")}</dd>
      <dt>failure class</dt><dd>${esc(n.failure_class)}</dd>
      <dt>rh relevance</dt><dd>${esc(n.rh_relevance)}</dd>
      <dt>reusable</dt><dd>${esc(n.reusable || "—")}</dd>
      <dt>ledger</dt><dd>${esc((n.ledger_ids || []).join(", ") || "—")}</dd>
      <dt>depends on</dt><dd>${esc((n.depends_on || []).join(", ") || "—")}</dd>
      <dt>confidence</dt><dd>${esc(n.confidence)}${n.draft ? " · draft" : ""}${n.needs_review ? " · needs review" : ""}</dd>
      <dt>score</dt><dd>${n.score}</dd>
    </dl>
    ${readme}
    <div class="arts">${artBits.join("")}</div>
    ${
      linkedConcepts.length
        ? `<div class="similar"><h3>concepts</h3>${linkedConcepts
            .map((c) => `<button type="button" class="jump-c" data-id="${esc(c.id)}">${esc(c.name)}</button>`)
            .join("")}</div>`
        : ""
    }
  `;
}

function conceptDossierHtml(n: ConceptNode, state: AppState): string {
  const repo = state.bundle.graph.nodes[0]?.abs_path
    ? state.bundle.graph.nodes[0].abs_path.slice(0, state.bundle.graph.nodes[0].abs_path.length - state.bundle.graph.nodes[0].path.length)
    : "";
  const srcs = (n.sources || [])
    .map((s) => {
      if (s.includes("/") || s.endsWith(".py") || s.endsWith(".tex") || s.endsWith(".lean")) {
        return fileLink(repo + s, s);
      }
      return `<span>${esc(s)}</span>`;
    })
    .join("");
  const attempts = attemptsForConcept(state.bundle.concepts, n.id);
  const attHtml = attempts
    .map((e) => {
      const rec = state.bundle.graph.nodes.find((r) => r.path === e.dst);
      const badge = rec?.outcome || e.rel;
      return `<li><button type="button" class="jump-rec" data-path="${esc(e.dst)}">${esc(rec?.round || e.dst.split("/").pop() || e.dst)}</button> <span class="tag">${esc(badge)}</span></li>`;
    })
    .join("");
  const grouped = new Map<string, typeof state.bundle.concepts.edges>();
  for (const e of state.bundle.concepts.edges) {
    if (e.src !== n.id && e.dst !== n.id) continue;
    if (e.rel === "USED_BY" || e.rel === "KILLED_BY") continue;
    const list = grouped.get(e.rel) || [];
    list.push(e);
    grouped.set(e.rel, list);
  }
  const edgeHtml = [...grouped.entries()]
    .map(([rel, list]) => {
      const items = list
        .map((e) => {
          const other = e.src === n.id ? e.dst : e.src;
          const nm = state.bundle.concepts.nodes.find((x) => x.id === other)?.name || other;
          return `<li><button type="button" class="jump-c" data-id="${esc(other)}">${esc(nm)}</button> <small>${esc(e.strength)}</small>${e.note ? ` — ${esc(e.note)}` : ""}</li>`;
        })
        .join("");
      return `<dt>${esc(rel)}</dt><dd><ul>${items}</ul></dd>`;
    })
    .join("");
  return `
    <header>
      <span class="dot" style="background:${conceptTypeColor(n.type)};box-shadow:0 0 0 2px ${conceptStatusStroke(n.status)}"></span>
      <div>
        <h2>${esc(n.name)}</h2>
        <p class="muted">${esc(n.type)} · ${esc(n.status)}${n.alive ? "" : " · dimmed"}</p>
      </div>
    </header>
    <dl>
      <dt>definition</dt><dd>${esc(n.definition)}</dd>
      <dt>aliases</dt><dd>${esc((n.aliases || []).join(", ") || "—")}</dd>
      <dt>tags</dt><dd>${esc((n.tags || []).join(", ") || "—")}</dd>
      <dt>attempts</dt><dd>${n.attempt_count}</dd>
      <dt>sources</dt><dd class="arts">${srcs || "—"}</dd>
    </dl>
    <div class="similar">
      <h3>attempts</h3>
      <ul>${attHtml || "<li class='muted'>—</li>"}</ul>
      <button type="button" id="show-net">show in network</button>
    </div>
    <dl>${edgeHtml}</dl>
  `;
}

function joinAbs(n: GraphNode, rel: string): string {
  if (rel.startsWith("/")) return rel;
  const root = n.abs_path.replace(/\/[^/]+$/, "");
  const repo = n.abs_path.slice(0, n.abs_path.length - n.path.length);
  return repo + rel;
}

async function boot(): Promise<void> {
  const app = document.querySelector("#app");
  if (!app) throw new Error("#app missing");
  app.innerHTML = `<div class="boot">loading catalog…</div>`;
  const graph = await loadGraphCore();
  const bundle = { graph, ...emptySidecars() };
  const filters = defaultFilters(graph, bundle.timeline);
  const state = new AppState(bundle, filters, defaultConceptFilters());

  app.innerHTML = "";
  const header = el("header", "top");
  header.innerHTML = `
    <div class="brand">
      <strong>RH corpus catalog</strong>
      <span>exploration record; no RH claim</span>
    </div>
    <nav class="tabs" role="tablist"></nav>
    <div class="search">
      <input id="q" type="search" placeholder="Search path, round, question, concept…" autocomplete="off"/>
      <button type="button" id="sim" ${bundle.vectors ? "" : "disabled"} title="Similar to selected">Similar</button>
    </div>
    <div class="meta-pill" id="counts"></div>
  `;
  const tabs = header.querySelector(".tabs")!;
  for (const v of VIEWS) {
    const b = el("button", "tab", v.label);
    b.type = "button";
    b.dataset.view = v.id;
    b.addEventListener("click", () => state.setView(v.id));
    tabs.append(b);
  }

  const filtersEl = el("aside", "filters");
  const stage = el("main", "stage");
  const dossier = el("aside", "dossier");
  dossier.innerHTML = `<p class="muted">Select a record.</p>`;
  app.append(header, filtersEl, stage, dossier);

  function paintConceptFilters(): void {
    const f = state.conceptFilters;
    const cmap = bundle.concepts;
    filtersEl.innerHTML = "";
    const vis = cmap.nodes.filter((n) => {
      if (!f.types.has(n.type) || !f.statuses.has(n.status)) return false;
      if (f.aliveOnly && !n.alive) return false;
      return true;
    }).length;
    filtersEl.append(el("p", "filter-count", `${vis} / ${cmap.nodes.length} concepts`));
    const q = header.querySelector("#q") as HTMLInputElement;
    q.value = f.query;
    q.placeholder = "Search name, alias, tag…";
    filtersEl.append(
      chipSet("type", [...CONCEPT_TYPES], f.types, (s) => state.patchConceptFilters({ types: s }), conceptTypeColor),
      chipSet("status", [...CONCEPT_STATUSES], f.statuses, (s) => state.patchConceptFilters({ statuses: s }), conceptStatusStroke),
      chipSet("rel group", [...REL_GROUPS], f.relGroups, (s) => state.patchConceptFilters({ relGroups: s as Set<RelGroup> })),
    );
    const strength = el("fieldset", "rounds");
    strength.innerHTML = `<legend>strength ≥ ${["STATISTICAL", "HEURISTIC", "CONDITIONAL", "THEOREM"][f.minStrength]}</legend>`;
    const sl = el("input") as HTMLInputElement;
    sl.type = "range";
    sl.min = "0";
    sl.max = "3";
    sl.value = String(f.minStrength);
    sl.addEventListener("change", () => state.patchConceptFilters({ minStrength: Number(sl.value) }));
    strength.append(sl);
    filtersEl.append(strength);
    const toggles = el("fieldset", "toggles");
    toggles.innerHTML = `<legend>scope</legend>`;
    toggles.append(
      toggle("alive only", f.aliveOnly, (v) => state.patchConceptFilters({ aliveOnly: v })),
      toggle("show attempts", f.showAttempts, (v) => {
        const next = new Set(f.relGroups);
        if (v) next.add("attempts");
        else next.delete("attempts");
        state.patchConceptFilters({ showAttempts: v, relGroups: next });
      }),
      toggle("avoid killed", f.avoidKilled, (v) => state.patchConceptFilters({ avoidKilled: v })),
      toggle("labels", f.showLabels, (v) => state.patchConceptFilters({ showLabels: v })),
    );
    filtersEl.append(toggles);
    const legend = el("div", "legend");
    legend.innerHTML =
      `<h3>types</h3>` +
      CONCEPT_TYPES.map((t) => `<div><i style="background:${CONCEPT_TYPE_COLORS[t]}"></i>${esc(t.replace(/_/g, " "))}</div>`).join("");
    filtersEl.append(legend);
  }

  function paintFilters(): void {
    if (state.view === "concepts") {
      paintConceptFilters();
      return;
    }
    const f = state.filters;
    const g = bundle.graph;
    filtersEl.innerHTML = "";
    const vis = filterNodes(g.nodes, f).length;
    filtersEl.append(el("p", "filter-count", `${vis} / ${g.meta.n_nodes} visible`));

    const q = header.querySelector("#q") as HTMLInputElement;
    q.value = f.query;
    q.placeholder = "Search path, round, question…";

    filtersEl.append(
      chipSet("kind", g.meta.orders.kinds, f.kinds, (s) => state.patchFilters({ kinds: s })),
      chipSet("outcome", g.meta.orders.outcomes, f.outcomes, (s) => state.patchFilters({ outcomes: s }), outcomeStroke),
      chipSet("family", g.meta.orders.families, f.families, (s) => state.patchFilters({ families: s }), familyColor),
      chipSet("rh relevance", g.meta.orders.rh_relevances, f.relevances, (s) => state.patchFilters({ relevances: s })),
      chipSet("failure class", g.meta.orders.failure_classes, f.failures, (s) => state.patchFilters({ failures: s })),
    );

    const toggles = el("fieldset", "toggles");
    toggles.innerHTML = `<legend>scope</legend>`;
    toggles.append(
      toggle("curated only", f.curatedOnly, (v) => state.patchFilters({ curatedOnly: v })),
      toggle("include unnumbered", f.includeUnnumbered, (v) => state.patchFilters({ includeUnnumbered: v })),
      toggle("family hulls", f.showHulls, (v) => state.patchFilters({ showHulls: v })),
      toggle("labels", f.showLabels, (v) => state.patchFilters({ showLabels: v })),
    );
    filtersEl.append(toggles);

    const rounds = el("fieldset", "rounds");
    rounds.innerHTML = `<legend>round ${f.roundMin}–${f.roundMax}</legend>`;
    const a = el("input") as HTMLInputElement;
    const b = el("input") as HTMLInputElement;
    a.type = b.type = "range";
    a.min = b.min = String(bundle.timeline.items.length ? bundle.timeline.min_round : (g.meta.round_min ?? 0));
    a.max = b.max = String(bundle.timeline.items.length ? bundle.timeline.max_round : (g.meta.round_max ?? 0));
    a.value = String(f.roundMin);
    b.value = String(f.roundMax);
    const sync = () => {
      const lo = Math.min(Number(a.value), Number(b.value));
      const hi = Math.max(Number(a.value), Number(b.value));
      state.patchFilters({ roundMin: lo, roundMax: hi });
    };
    a.addEventListener("change", sync);
    b.addEventListener("change", sync);
    rounds.append(a, b);
    filtersEl.append(rounds);

    const edges = el("fieldset", "edges");
    edges.innerHTML = `<legend>edges</legend>`;
    for (const t of ALL_EDGE_TYPES) {
      const n = g.meta.edges_by_type[t] || 0;
      edges.append(
        toggle(`${t.toLowerCase()} (${n})`, f.edgeTypes.has(t), (on) => {
          const next = new Set(f.edgeTypes);
          if (on) next.add(t);
          else next.delete(t);
          state.patchFilters({ edgeTypes: next as Set<EdgeType> });
        }),
      );
    }
    filtersEl.append(edges);

    const legend = el("div", "legend");
    legend.innerHTML = `<h3>families</h3>` + g.meta.orders.families
      .map((fam) => `<div><i style="background:${FAMILY_COLORS[fam] || familyColor(fam)}"></i>${esc(fam.replace(/_/g, " "))}</div>`)
      .join("");
    filtersEl.append(legend);
  }

  function toggle(label: string, on: boolean, cb: (v: boolean) => void): HTMLElement {
    const row = el("label", "switch");
    const input = el("input") as HTMLInputElement;
    input.type = "checkbox";
    input.checked = on;
    input.addEventListener("change", () => cb(input.checked));
    row.append(input, document.createTextNode(label));
    return row;
  }

  let dispose: (() => void) | null = null;
  let lastView: ViewId | null = null;

  function mountView(): void {
    if (lastView === state.view && dispose) return;
    dispose?.();
    lastView = state.view;
    if (state.view === "network") dispose = renderNetwork(stage, state);
    else if (state.view === "concepts") dispose = renderConcepts(stage, state);
    else if (state.view === "timeline") dispose = renderTimeline(stage, state);
    else if (state.view === "matrices") dispose = renderMatrices(stage, state);
    else if (state.view === "kills") dispose = renderKills(stage, state);
    else dispose = renderExport(stage, state, stage);
  }

  function paintChrome(): void {
    header.querySelectorAll(".tab").forEach((t) => {
      t.classList.toggle("on", (t as HTMLElement).dataset.view === state.view);
    });
    const pill = header.querySelector("#counts")!;
    if (state.view === "concepts") {
      pill.textContent = `${bundle.concepts.nodes.length} concepts · ${bundle.concepts.edges.length} edges`;
    } else {
      const vis = filterNodes(bundle.graph.nodes, state.filters).length;
      pill.textContent = `${vis} shown · ${bundle.graph.meta.n_curated} curated · ${bundle.graph.meta.n_draft} draft`;
    }
    if (state.view === "concepts" && state.selectedConcept) {
      dossier.innerHTML = conceptDossierHtml(state.selectedConcept, state);
      dossier.querySelector("#show-net")?.addEventListener("click", () => {
        if (state.selectedConcept) state.showConceptInNetwork(state.selectedConcept.id);
      });
      dossier.querySelectorAll(".jump-c").forEach((b) => {
        b.addEventListener("click", () => state.openConcept((b as HTMLElement).dataset.id || ""));
      });
      dossier.querySelectorAll(".jump-rec").forEach((b) => {
        b.addEventListener("click", () => {
          const rec = bundle.graph.nodes.find((x) => x.path === (b as HTMLElement).dataset.path) || null;
          if (rec) {
            state.select(rec);
            state.setView("network");
          }
        });
      });
    } else if (state.selected) {
      const linked = conceptsForPath(bundle.concepts, state.selected.path);
      dossier.innerHTML = dossierHtml(state.selected, linked);
      dossier.querySelectorAll(".jump-c").forEach((b) => {
        b.addEventListener("click", () => state.openConcept((b as HTMLElement).dataset.id || ""));
      });
    } else {
      dossier.innerHTML = `<p class="muted">${state.view === "concepts" ? "Select a concept. Shift-click two nodes for a path." : "Select a record."}</p>`;
    }
    if (state.similar.length && state.selected) {
      const box = el("div", "similar");
      box.innerHTML =
        `<h3>similar</h3>` +
        state.similar
          .map((s) => {
            const n = bundle.graph.nodes.find((x) => x.id === s.id);
            return `<button type="button" data-id="${esc(s.id)}">${esc(n?.round || s.id.split("/").pop() || s.id)} <small>${s.sim.toFixed(2)}</small></button>`;
          })
          .join("");
      box.querySelectorAll("button").forEach((b) => {
        b.addEventListener("click", () => {
          const n = bundle.graph.nodes.find((x) => x.id === (b as HTMLElement).dataset.id) || null;
          if (n) state.select(n);
        });
      });
      dossier.append(box);
    }
  }

  let filterSig = "";
  const sig = () =>
    JSON.stringify({
      view: state.view,
      k: [...state.filters.kinds],
      o: [...state.filters.outcomes],
      f: [...state.filters.families],
      r: [...state.filters.relevances],
      x: [...state.filters.failures],
      c: state.filters.curatedOnly,
      u: state.filters.includeUnnumbered,
      a: state.filters.roundMin,
      b: state.filters.roundMax,
      q: state.filters.query,
      e: [...state.filters.edgeTypes],
      h: state.filters.showHulls,
      l: state.filters.showLabels,
      ct: [...state.conceptFilters.types],
      cs: [...state.conceptFilters.statuses],
      cr: [...state.conceptFilters.relGroups],
      cm: state.conceptFilters.minStrength,
      ca: state.conceptFilters.aliveOnly,
      cat: state.conceptFilters.showAttempts,
      ck: state.conceptFilters.avoidKilled,
      cq: state.conceptFilters.query,
      cl: state.conceptFilters.showLabels,
    });

  state.on(() => {
    const s = sig();
    if (s !== filterSig) {
      filterSig = s;
      paintFilters();
    }
    paintChrome();
    mountView();
  });

  (header.querySelector("#q") as HTMLInputElement).addEventListener("input", (ev) => {
    const val = (ev.target as HTMLInputElement).value;
    if (state.view === "concepts") state.patchConceptFilters({ query: val });
    else state.patchFilters({ query: val });
  });
  (header.querySelector("#sim") as HTMLButtonElement).addEventListener("click", () => {
    if (!bundle.vectors || !state.selected) return;
    state.similar = similarTo(state.selected.id, bundle.vectors, 12);
    state.emit();
  });

  window.addEventListener("keydown", (ev) => {
    if ((ev.metaKey || ev.ctrlKey) && ev.key.toLowerCase() === "e") {
      ev.preventDefault();
      exportBundle(state, stage).catch((err) => console.error(err));
    }
  });

  filterSig = sig();
  paintFilters();
  paintChrome();
  mountView();

  void (async () => {
    await mergeRecords(graph);
    const rest = await loadSidecars(graph);
    Object.assign(bundle, rest);
    const simBtn = header.querySelector("#sim") as HTMLButtonElement | null;
    if (simBtn) simBtn.disabled = !bundle.vectors;
    state.emit();
  })();
}

boot().catch((err) => {
  const app = document.querySelector("#app");
  if (app) app.innerHTML = `<div class="boot err">${esc(String(err))}</div>`;
  console.error(err);
});
