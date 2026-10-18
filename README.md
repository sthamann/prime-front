# Prime Front

Independent research on prime numbers, the Weil form, spectral constructions,
factorisation and the Riemann hypothesis. [Website](https://prime.fixpoint-theory.com)
· [Research diary](https://prime.fixpoint-theory.com/research)
· [Publications](https://prime.fixpoint-theory.com/publications)
· [Verification](https://prime.fixpoint-theory.com/verification)

This project was separated from [TFPT](https://github.com/sthamann/tfpt) on
18 October 2026. TFPT now focuses on its physical compiler and its own tests.
Original claim/module IDs and scoped statuses are preserved. **There is no
claim of a proof of the Riemann hypothesis, a general fast factorisation
algorithm, or a physical derivation from finite numerical checks.** Historic
wording is a source record, not a current endorsement of every claim.

## What lives here

- Root `*.tex` and `documents/`: dedicated papers plus original sections
  extracted from mixed TFPT documents; source ranges and hashes are recorded
  in `provenance/latex-section-map.json`.
- `verification/`: the independent Python suite, registry and status ledger.
  Generic physical-math dependencies copied here are identified separately.
- `experiments/`: prime/RH probes, sealed results and campaign notes.
  The historical `tfpt-discovery` directory name preserves import paths.
- `rh/`: the original inventory, Lean research, semantic catalog, paper,
  exclusions and conditional/open statements.
- `website/`: the independent Next.js site, research archive and media.
- `provenance/`: byte-identical originals, checksums and the migration map.
  Full mixed originals are archival; the active papers are the scoped files
  at the root. No mathematical status is promoted by this migration.

## Reproduce

```sh
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/python verification/run_all.py
python3 scripts/check_migration.py
bash build.sh audit
cd website && npm ci && npm run build
```

`run_all.py --shard INDEX/COUNT` uses one-based shards (see `--help`).
`bash build.sh notes` recompiles all active papers with TeX Live/MacTeX;
`bash build.sh website` mirrors current papers and verification sources.

The legacy sealed campaign is available separately as
`python rh/verification/run_rh.py --fast --skip-lean`. Some historical probes
require the original local Mathlib package cache or platform-specific
floating-point behaviour. Its result must be reported separately from the
portable integrity, import and source-mirror checks. A successful finite or
conditional verification does not establish RH. Lean research may contain
explicit hypotheses or `sorry`; consult the source and `rh/lean/README.md`.

The catalog's historic external references remain provenance records. Its
active source-index configuration is portable and scoped to this repository;
it does not scan the separate TFPT project or private task folders.
