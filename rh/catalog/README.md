# RH semantic catalog

Research documentation of the RH corpus. **No RH claim** in either
direction. Rebuild `python3 rh/catalog/build_catalog.py` (catalog +
`analysis/paths_report.json`). Check: `--check` → `CATALOG CHECK OK`.
Standalone paths: `python3 rh/catalog/analysis/analyze_paths.py`.
Query: `python3 rh/catalog/rhcat.py stats|search|kills|open|check-new|todo`.

Generated (never hand-edit): `rh_semantic_catalog.json`, `INDEX.md`,
`stats.json`. Hand-edit `taxonomy.json`, `schema.json`, and `fragments/`.
Drafts: `fragments/auto_drafts.json` from `autodraft.py` (`draft=true`);
curated `part_*.json` always override.

## fragments/

| part | covers |
|---|---|
| 1–7 | initial extraction (`rh/`, `verification/` v955+, discovery probes, problem notes) |
| 8 | full-tree sweep of `verification/` + prime-front docs |
| 9 | Kneser groupoid + CM.ISOGENY chat-claim |
| 10 | parabolic detline2 |
| 11 | positive-cone blindness |
| 12 | clock combinations |
| 13 | π conformity |
| 14 | census QSM normflow |
| 15 | none — bridge-2 object search produced no probe |
| 16 | Hecke index theorem |
| 17 | evolve harness |
| 18 | Lean arch-rate falsification |
| 19 | all-place Tate / finite-carrier audit, T49 correction; heat-Gabor ℋ restatement + dyadic NB capture η_k |

## analysis/

| file | role |
|---|---|
| `analyze_paths.py` | standalone path report |
| `paths_report.json`, `paths_report_728.json`, `paths_report_diff.json` | catalog path reports |
| `full_tree_sweep.json` | verification/ + prime-front sweep |
| `orphan_triage.{json,md}` | unused [E] identities |
| `prime_story.{json,md}` | prime-front narrative |
| `event_log_function.{json,md}` | event-log / scale-generator |
| `compiler_necessity.{json,md}` | compiler necessity |
| `pi_prime_correlations.{json,md}` | π / prime correlations |
| `positivity_origin_search.{json,md}` | positivity origin |
| `bridge2_direct_search.md` | bridge-2 shape (direct) |
| `bridge2_object_search.{json,md}` | bridge-2 object / literature |
| `geometry_audit.{json,md}` | geometry frameworks vs fixed bridge-2 shape |
| `all_place_tate_audit.{json,md}` | Calabi--Yau Tate factor, finite-carrier no-go, Rankin erratum, A1--A7 all-place contract |
| `hecke_index_theorem.{json,md}` | `TFPT.HECKE.INDEX.01` (experiment-only) |
| `evolve_props_report.md` | evolve harness (3→2) |
| `llm_consistency.json` | LLM vs curated enum disagreements |

## map/

See `map/README.md`. Seeds + extract + `build_map.py` → `rh_concept_map.json`.
Proposal files are review surfaces only, not map contents:
`proposed_additions.json` and `proposed_additions_<topic>.json`
(`bridge2`, `compiler`, `cone`, `eventlog`, `geometry`, `index`, `nb`, `pi`, `positivity`, `qsm`).

## viewer/

See `viewer/README.md`. Network / concept map use sigma.js v3 (WebGL) on
precomputed layouts. First paint: `viewer/public/data/graph_core.json`;
dossiers from `viewer/public/data/records.json`.

```bash
cd rh/catalog/viewer
npm install
npm run build-data   # build_graph.py → public/data/*.json
npm run dev          # http://localhost:5173
npm run build && npm start
npm run export
```

## Tools

| script | role |
|---|---|
| `rhcat.py` | search / family / kills / open / dossier / check-new / semsearch / new |
| `build_catalog.py` | merge fragments + drafts; `--check` is the audit gate |
| `autodraft.py` | regenerate `auto_drafts.json` (`--llm --only-new` optional) |
| `openai_service.py` | shared OpenAI helper (key from env or `~/.config/tfpt/openai.env`) |
| `embed_catalog.py` | incremental embeddings → `embeddings/catalog_embeddings.json` |
| `llm_consistency.py` | classify all records; writes `analysis/llm_consistency.json` |

`semsearch` is cosine over `embeddings/` (keyword fallback if absent).
LLM helpers are optional; default hard budget $5; cached hits are free.
`build.sh gen` runs `--llm` + embeddings only when `TFPT_LLM_CATALOG=1`
and the key resolves. Audit is offline. Cache: `cache/llm_cache.jsonl`.

## Wiring

| piece | path |
|---|---|
| rule | `.cursor/rules/rh-catalog.mdc` — check-new before a probe; fragment after each round |
| skill | `.cursor/skills/rh-corpus-search/SKILL.md` — catalog search before / after RH work |
| skill | `.cursor/skills/rh-sync/SKILL.md` — INVENTORY / suite / paper after a sealed round |
| hook | `.cursor/hooks/rh_catalog_refresh.py` — `afterFileEdit` on `rh/` and discovery probes |

Workflow: `rhcat.py check-new` → probe → `rhcat.py new` + fragment →
`build_catalog.py` + `rh-sync`. Enums live in `taxonomy.json`.
