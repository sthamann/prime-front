#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Classify every catalog record and list enum disagreements vs curated values.

Writes rh/catalog/analysis/llm_consistency.json. Never modifies fragments.
Default: print a dry-run cost estimate, then run only if total_usd < 5.
`--dry-run` prints the estimate and exits.

stdlib only. NO RH CLAIM.
"""

from __future__ import annotations

import json
import os
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed

from openai_service import (
    OpenAIService,
    load_catalog_records,
    load_taxonomy,
)

CATALOG_DIR = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.path.join(CATALOG_DIR, "analysis")
OUT_PATH = os.path.join(OUT_DIR, "llm_consistency.json")
COMPARE_FIELDS = ("kind", "family", "outcome", "failure_class")
AUTO_BUDGET = 5.0


def disagreements_for(record, classified):
    diffs = {}
    for field in COMPARE_FIELDS:
        curated = record.get(field)
        predicted = classified.get(field)
        if curated != predicted:
            diffs[field] = {"curated": curated, "llm": predicted}
    return diffs


def write_report(payload, path=None):
    target = path or OUT_PATH
    os.makedirs(os.path.dirname(target), exist_ok=True)
    with open(target, "w", encoding="utf-8") as fh:
        json.dump(payload, fh, indent=2, sort_keys=True, ensure_ascii=False)
        fh.write("\n")
    return target


def _row_from_classified(rec, classified, svc):
    diffs = disagreements_for(rec, classified)
    if not diffs:
        return None
    return {
        "path": rec.get("path"),
        "round": rec.get("round"),
        "draft": bool(rec.get("draft")),
        "needs_review": bool(rec.get("needs_review")),
        "disagreements": diffs,
        "llm_rationale": classified.get("rationale") or "",
        "llm_model": classified.get("_model") or svc.model,
        "llm": {
            "kind": classified.get("kind"),
            "family": classified.get("family"),
            "family_secondary": classified.get("family_secondary") or [],
            "outcome": classified.get("outcome"),
            "failure_class": classified.get("failure_class"),
            "rh_relevance": classified.get("rh_relevance"),
            "confidence": classified.get("confidence"),
        },
    }


def run_pass(svc, records, taxonomy, workers=3):
    rows = []
    by_field = {field: 0 for field in COMPARE_FIELDS}
    workers = max(1, int(workers))

    def classify_one(rec):
        try:
            return rec, svc.classify_record(rec, taxonomy), None
        except Exception as exc:
            return rec, None, str(exc)

    if workers == 1 or len(records) < 2:
        classified_pairs = [classify_one(rec) for rec in records]
    else:
        classified_pairs = []
        with ThreadPoolExecutor(max_workers=workers) as pool:
            futs = [pool.submit(classify_one, rec) for rec in records]
            done = 0
            for fut in as_completed(futs):
                classified_pairs.append(fut.result())
                done += 1
                if done % 100 == 0 or done == len(futs):
                    sys.stderr.write(
                        "llm_consistency: %d/%d spent=%.4f\n"
                        % (done, len(futs), svc.spent_usd)
                    )
    errors = []
    for rec, classified, err in classified_pairs:
        if err or classified is None:
            errors.append({"path": rec.get("path"), "error": err or "classify failed"})
            continue
        row = _row_from_classified(rec, classified, svc)
        if row is None:
            continue
        for field in row["disagreements"]:
            by_field[field] += 1
        rows.append(row)
    rows.sort(key=lambda r: (r.get("path") or ""))
    return {
        "claim_boundary": (
            "Research documentation. NOT evidence for or against the "
            "Riemann Hypothesis in either direction. NO RH CLAIM."
        ),
        "n_records": len(records),
        "n_disagreements": len(rows),
        "n_errors": len(errors),
        "errors": errors[:50],
        "by_field": by_field,
        "spent_usd": round(svc.spent_usd, 6),
        "model": svc.model,
        "records": rows,
    }


def main(argv=None):
    argv = list(argv if argv is not None else sys.argv[1:])
    dry_only = "--dry-run" in argv
    records = load_catalog_records()
    taxonomy = load_taxonomy()
    estimator = OpenAIService(dry_run=True, budget_usd=AUTO_BUDGET)
    estimate = estimator.estimate_cost(len(records))
    sys.stdout.write(
        "llm_consistency estimate: n=%d chat=%s total_usd=%.4f budget=%.2f\n"
        % (
            estimate["n_records"],
            estimate["chat_model"],
            estimate["total_usd"],
            AUTO_BUDGET,
        )
    )
    sys.stdout.write(
        json.dumps(estimate, indent=2, sort_keys=True, ensure_ascii=False) + "\n"
    )
    if dry_only:
        return 0
    if estimate["total_usd"] >= AUTO_BUDGET:
        sys.stdout.write(
            "STOP: estimate %.4f USD >= %.2f; not calling the API\n"
            % (estimate["total_usd"], AUTO_BUDGET)
        )
        return 2
    svc = OpenAIService(dry_run=False, budget_usd=AUTO_BUDGET)
    report = run_pass(svc, records, taxonomy)
    write_report(report)
    sys.stdout.write(
        "llm_consistency: n=%d disagree=%d errors=%d kind=%d family=%d "
        "outcome=%d failure_class=%d spent=%.6f -> %s\n"
        % (
            report["n_records"],
            report["n_disagreements"],
            report.get("n_errors", 0),
            report["by_field"]["kind"],
            report["by_field"]["family"],
            report["by_field"]["outcome"],
            report["by_field"]["failure_class"],
            report["spent_usd"],
            os.path.relpath(OUT_PATH, os.path.join(CATALOG_DIR, "..", "..")),
        )
    )
    top = report["records"][:10]
    for row in top:
        fields = ",".join(sorted(row["disagreements"]))
        sys.stdout.write(
            "  %s  [%s]  %s\n"
            % (row.get("path") or "-", fields, row.get("llm_rationale") or "")
        )
    return 0


if __name__ == "__main__":
    sys.exit(main())
