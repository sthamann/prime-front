# Prime Front verification

After the 2026-10-18 ownership split this project registers **326 modules** and maintains **410 ledger rows**. These are source counts, not a count of independent proofs.

The suite preserves the original module and claim identifiers. Five mixed modules retain their original IDs with separate scopes: v705 (full prime application here; physical NS/deck D1–D3 in TFPT), v807 (full prime-window study here; exact RR/Serre algebra also in TFPT), v817 (prime packet instance here), v849 (cofinal Weil mirror here), and v853 (Mangoldt incidence identity here). tfpt_constants.py and v310/v774 are dependency copies; their presence does not turn TFPT physical premises into RH conclusions.

Run from the repository root:

```sh
python3 verification/run_all.py
python3 verification/run_all.py --shard 1/6
python3 verification/make_script_index.py
python3 verification/audit_sync.py
```

Each registered module can also run directly. Install the repository requirements first; a subset of original modules needs experimental sources at the preserved relative paths. `run_all.py` executes the stated module checks and returns nonzero on a failed check. `audit_sync.py` checks source/registry/generated-surface consistency and executes no Lean proof. A full numerical suite and a fresh Lean build are separate operations.

Single sources: `script_registry.csv` (module index), `script_clusters.csv` (group metadata), `status_ledger.csv` (claim status). Generated indices must be regenerated through `make_script_index.py`. The original mathematical scopes, honest negative patterns, open hypotheses and historical module IDs remain authoritative.

An executed finite check does not establish the Riemann hypothesis or complete a physical field theory.
