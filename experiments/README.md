# Prime Front experiments

This directory contains exploratory prime-number, factorisation and RH work.
Experiments are separate from the registered checks in `../verification/` and
from formal statements in `lean4-carrier-rigidity/` and `../rh/lean/`.
An experiment, a finite check and a Lean theorem have different scopes; none
of these directory names establishes the Riemann hypothesis.

- `tfpt-discovery/`: arithmetic and spectral probes, their local helper copies
  and sealed fixtures. The historical directory name keeps imports stable.
- `pi-prime-event-log-2026-09-08/`: prime-event and factorisation experiments.
- `double-cover-rh-audit-2026-09-08/`: conditional double-cover/RH bridge study.
- `theory-contracts/universalraum-closure-round-20260914/`: measured requirements
  of the Universalraum-to-Weil bridge, not a physical TFPT derivation.
- `lean4-carrier-rigidity/`: finite and conditional formal support; see its README.
- `next.txt`: the extracted arithmetic research diary.

The original mixed TFPT introduction is archived under
`../provenance/tfpt-source/experiments/README.md`. Current physical TFPT
experiments live only in https://github.com/sthamann/tfpt/tree/main/experiments.

Use the repository Python environment to run a probe from the repository root,
for example `python experiments/tfpt-discovery/ihara_ground_truth_probe.py`.
Some sealed historical probes retain old absolute fallback paths byte-for-byte;
their first candidate is the local directory. The project boundary audit
requires the local `classical_cert_probe.py` anchor, so those fallbacks are
never needed. Integrity checks retain the original source pins.
