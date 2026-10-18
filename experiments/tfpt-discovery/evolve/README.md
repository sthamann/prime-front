# Selected-window program evolution

Experiment-only FunSearch-style harness for three named Lean propositions.
It evolves executable formula programs, scores them on deterministic finite
measurements, and writes every proposal and fitness value to `results/`.

Run:

```bash
experiments/tfpt-discovery/.venv/bin/python \
  experiments/tfpt-discovery/evolve/evolve_props.py
```

The tool reuses:

- `arch_rate_probe.py` and `extraction_joint_probe.py` for the exact corpus
  definitions of the arch tent read and classical arch pairing;
- `cofinal_family_probe.py` and `deep_builder_probe.py` for the selected
  full-cap operator;
- `weil_window_profile_scout.py` and its converged Galerkin profile.

If `OPENAI_API_KEY` is present in the process environment, the OpenAI service
is available under a hard USD 25 budget. Without that environment variable,
the run uses the deterministic local mutation library. The current program
does not need remote proposals; this keeps numerical scoring reproducible.

The 45-minute kill switch is checked between windows. Seed: `20260904`.

Scope:

- T1 fits explicit quadratic-rate majorants on six native profile families.
- T2 measures Jackson-style polynomial approximation, but does not conflate
  that classical norm bound with the Lean scalar read dictionary.
- T3 measures the selected augmented dual-resolvent margin, evolves a held-out
  classifier, and imports the scout's hardest-window Galerkin minimizers.

Firewall: arithmetic-side data and classical kernels only. No RH claim and no
anti-RH claim. Results are measurements, not verification-suite evidence.
