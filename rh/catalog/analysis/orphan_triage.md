# Orphan identity triage

Research-map output only. No claim for or against RH.

Source note: `v535_v954_E_orphans` contains and declares **101**, not 102, records.

## Counts

| Scope | Count |
|---|---:|
| FINITE_WINDOW | 69 |
| FORMAL | 29 |
| STRUCTURAL | 3 |

| Reuse class | Count |
|---|---:|
| LEVER | 0 |
| INPUT | 67 |
| DEAD_END | 34 |
| UNKNOWN | 0 |

Feed memberships overlap.

| Feed | Total | LEVER | INPUT | DEAD_END | UNKNOWN |
|---|---:|---:|---:|---:|---:|
| LSTAR | 11 | 0 | 7 | 4 | 0 |
| QN_TERMINAL | 8 | 0 | 8 | 0 | 0 |
| I5_WEIL_WALL | 49 | 0 | 25 | 24 | 0 |
| WEIGHT4_GL1_BRIDGE | 10 | 0 | 10 | 0 | 0 |
| HALFDENSITY_GEOMETRY | 12 | 0 | 9 | 3 | 0 |
| PRIME_PHASE_COHERENCE | 18 | 0 | 16 | 2 | 0 |
| SCALE_LAW_LAMBDA | 22 | 0 | 18 | 4 | 0 |
| NONE | 8 | 0 | 2 | 6 | 0 |

## LEVER adjudication

No orphan meets the strict LEVER rule.

- `v630` and `v643` are STRUCTURAL dictionaries for the Weil/Suzuki measure, but add no inequality toward strict two-measure subordination.
- `v951` is STRUCTURAL, but its own honesty block identifies the result as an algebraic restatement of the Weil wall.
- The r600+ cross-check therefore yields no surviving contract sketch.
- Kill roots checked: structural mismatch, lossy/nonuniform constant, no bridge, world blindness, restatement, no cofinal bridge, and renamed mechanism.

## DEAD_END reasons

| Reason | Count |
|---|---:|
| Finite-window or cofinal ceiling | 13 |
| Failed or falsified mechanism | 10 |
| Restatement, loop, or no independent inequality | 5 |
| Superseded or legacy reading | 3 |
| Structural obstruction or indefinite lift | 2 |
| Lossy bound cannot reach determinant margin | 1 |

## Overlap / edge candidates

- Closed deterministic parity-lag kernel: `v587`, `v588`, `v591`, `v592`, `v593`, `v595`. Add `v595 SUPERSEDES v593` for residual attribution.
- Suzuki/Weil measure dictionary: `v630`, `v640`, `v642`, `v643`, `v761`. Add `v643 SUPERSEDES` the smooth-open/convention readings in `v630`/`v640`/`v642`.
- Finite Weil trace/moments: `v719`, `v727`. `v727` extends determinacy; it does not supersede the trace dictionary.
- Nested Schur/tau chain: `v749`, `v755`, `v759`, `v883`. Use `EXTENDS`, not `SUPERSEDES`.
- Wall autocorrelation/sign law: `v951`, `v953`. `v953` extends `v951` with the sign implication and h=4,5 Sturm certificates.
- Krein coordinates: `v734`, `v946` concern different objects; use `RELATED`, not `SUPERSEDES`.

## Honesty check

No docstring claims a stronger certified status than its ledger row after applying its explicit scope riders.

`v755` still says “exploration only / no ledger row” inside promoted source text; this understates rather than overstates the current ledger status.

## Surprising items

1. Only three of 101 records are genuinely STRUCTURAL; most exact-looking results are explicitly finite or per-instance.
2. The strongest direct dictionary, `v643`, reaches the exact Weil measure but contributes no inequality to L*.
3. `v951` reaches the classical Weil archimedean kernel structurally, yet explicitly proves that its cancellation functional is the wall under another name.
