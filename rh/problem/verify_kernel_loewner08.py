#!/usr/bin/env python3
"""Verify the round-496 L=0.8 kernel/Loewner method-no-go note."""
from __future__ import annotations

import hashlib
import pathlib
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
PROBE = ROOT / "experiments/tfpt-discovery/kernel_loewner08_probe.py"
NOTE = ROOT / "rh/problem/kernel_loewner08.tex"
PDF = ROOT / "rh/problem/kernel_loewner08.pdf"

EXPECTED_SPEC_SHA = (
    "63f590d43c9ed63e8419c99ddd6b9110e58a7f419d6445de71932aa4575cba97"
)
REQUIRED_NOTE_FRAGMENTS = (
    r"\texttt{NO\_GO(kernel-Loewner-compact-tail@L=0.8)}",
    "2.9419735252236204555039093902",
    "$-1.6106733\\cdot10^{-4}$",
    "27.367230540",
    "0.939496613",
    "No RH claim",
)


def fail(message: str) -> None:
    print("VERIFY FAILED:", message)
    raise SystemExit(1)


def main() -> None:
    if not PROBE.is_file() or not NOTE.is_file() or not PDF.is_file():
        fail("probe, TeX note, or PDF missing")

    namespace: dict[str, object] = {"__name__": "kernel_loewner08_seal"}
    source = PROBE.read_text(encoding="utf-8")
    sys.path.insert(0, str(PROBE.parent))
    exec(compile(source, str(PROBE), "exec"), namespace)
    actual_spec_sha = namespace.get("SPEC_SHA")
    if actual_spec_sha != EXPECTED_SPEC_SHA:
        fail("SPEC_SHA drift: %s" % actual_spec_sha)

    note_text = NOTE.read_text(encoding="utf-8")
    for fragment in REQUIRED_NOTE_FRAGMENTS:
        if fragment not in note_text:
            fail("note fragment missing: %s" % fragment)
    if EXPECTED_SPEC_SHA not in note_text:
        fail("note does not pin the probe SPEC_SHA")
    if "lambda_*(0.8)\\ge c" not in note_text:
        fail("method target is not stated")

    probe_run = subprocess.run(
        [sys.executable, str(PROBE), "--smoke"],
        cwd=ROOT,
        check=False,
        capture_output=True,
        text=True,
        timeout=60,
    )
    if probe_run.returncode != 0:
        fail("smoke probe failed\n" + probe_run.stdout + probe_run.stderr)
    required_output = (
        "G1 PASS; G2 NO_GO; G3 NO_GO",
        "VERDICT NO_GO(kernel-Loewner-compact-tail@L=0.8)",
        "ALL CHECKS PASSED (15/15)",
    )
    for fragment in required_output:
        if fragment not in probe_run.stdout:
            fail("probe output missing: %s" % fragment)

    pdf_digest = hashlib.sha256(PDF.read_bytes()).hexdigest()
    if PDF.stat().st_size < 100_000:
        fail("PDF unexpectedly small")

    print("probe SPEC_SHA", actual_spec_sha)
    print("pdf SHA256", pdf_digest)
    print("VERIFIED kernel_loewner08 r496 NO_GO")


if __name__ == "__main__":
    main()
