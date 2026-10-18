# RH corpus catalog viewer

Exploration record of the semantic catalog. **No RH claim.**

## Run

```bash
cd rh/catalog/viewer
npm install
npm run build-data   # python3 build_graph.py → public/data/*.json
npm run dev          # Vite at http://localhost:5173
npm start            # vite preview (production-like)
npm run build        # dist/
npm run export       # headless CSV / GraphML / SVG check
```

`build-data` reads `rh/catalog/rh_semantic_catalog.json`, `analysis/paths_report.json`, `taxonomy.json`, and optionally `embeddings/catalog_embeddings.json`. Counts are never hard-coded. Missing embeddings → `meta.semantic=false`, no SEMANTIC edges / vectors.

## Data schema (`public/data/`)

| File | Contents |
|---|---|
| `graph.json` | full `meta`, nodes (catalog fields + `x,y,size`), typed edges |
| `graph_core.json` | first-paint: id, x, y, size, kind, outcome, family, round, draft, path + compact edges |
| `records.json` | dossier fields, merged after first paint |
| `vectors.json` | 32-d PCA rows for “similar to selected” |
| `matrix.json` | family×outcome, family×failure_class, kind×outcome, curated vs draft |
| `timeline.json` | per-record round glyphs |
| `kills.json` / `orphans.json` / `pairs.json` / `conflicts.json` / `misses.json` | T2–T6 |

Edge types: `DEPENDS`, `SAME_ROUND`, `SHARED_LEDGER`, `SUPERSEDES`, `SEMANTIC` (cosine ≥ 0.45, top-3), `FAMILY` (star to family hub).

## Views

Network and Concept map use sigma.js v3 (WebGL) on graphology graphs. Positions are precomputed by `scripts/layout.mjs` (ForceAtlas2 + noverlap, seed 32) during `npm run build-data` — the browser does not run a force simulation by default. Re-layout in the Network tab runs FA2 in a Web Worker for 2.5s. First paint loads `graph_core.json`; dossier fields arrive from `records.json` after paint. Family hulls default off.

Network (precomputed layout, optional hulls, dossier), Timeline (brush → round filter), Matrices (click cell → network filter), Kill roots (sunburst + tables), Export (SVG / PNG 2× / CSV / JSON / GraphML / GEXF / ZIP). Shortcut ⌘/Ctrl+E = report bundle.

File links use `cursor://file/<abs path>` plus the plain repo path. Rebuild data after catalog changes.

## Concept map

Tab **Concept map** reads `public/data/concepts.json` (from `rh/catalog/map/build_map.py`) and `public/data/gaps_report.json` (copied from `rh/catalog/map/` by `npm run build-data`). Proposed-addition drafts are not loaded.

Radial layout by `layout_hint` / type; GAPS panel is G1–G6. Shift-click two nodes for shortest paths ≤ 5 hops (`avoid killed` skips `KILLED_HERE`). “Show attempts” pulls `USED_BY` / `KILLED_BY` catalog paths in as satellites. Record dossiers list linked concepts; concept dossiers jump back to the network.

Exports: concept GraphML / GEXF / DOT / CSV, plus `concepts.json`, `gaps_report.json`, and the concept SVG in the report ZIP.
