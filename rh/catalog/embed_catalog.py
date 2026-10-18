#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build incremental embeddings for rh/catalog/rh_semantic_catalog.json.

Text = question + mechanism + result_verdict + failed_because + reusable.
Output (untracked): rh/catalog/embeddings/catalog_embeddings.json
Key = sha256(model + '\\n' + text). Unchanged texts are not re-embedded.

stdlib only. NO RH CLAIM.
"""

from __future__ import annotations

import hashlib
import json
import math
import os
import sys
import time

from openai_service import OpenAIService, load_catalog_records

CATALOG_DIR = os.path.dirname(os.path.abspath(__file__))
EMBED_DIR = os.path.join(CATALOG_DIR, "embeddings")
EMBED_PATH = os.path.join(EMBED_DIR, "catalog_embeddings.json")
TEXT_FIELDS = (
    "question",
    "mechanism",
    "result_verdict",
    "failed_because",
    "reusable",
)


def record_embed_text(record):
    parts = []
    for key in TEXT_FIELDS:
        val = (record.get(key) or "").strip()
        if val:
            parts.append(val)
    return " ".join(parts)


def text_sha256(model, text):
    blob = "%s\n%s" % (model, text)
    return hashlib.sha256(blob.encode("utf-8")).hexdigest()


def load_embeddings(path=None):
    target = path or EMBED_PATH
    if not os.path.isfile(target):
        return None
    with open(target, "r", encoding="utf-8") as fh:
        return json.load(fh)


def embeddings_by_path(payload):
    out = {}
    if not payload:
        return out
    model = payload.get("model")
    rows = payload.get("records")
    if rows is None and isinstance(payload, list):
        rows = payload
    for row in rows or []:
        if not isinstance(row, dict) or not row.get("path"):
            continue
        out[row["path"]] = row
        if model and not row.get("model"):
            row["model"] = model
    return out


def cosine(a, b):
    if not a or not b or len(a) != len(b):
        return 0.0
    dot = 0.0
    na = 0.0
    nb = 0.0
    for x, y in zip(a, b):
        fx = float(x)
        fy = float(y)
        dot += fx * fy
        na += fx * fx
        nb += fy * fy
    if na <= 0.0 or nb <= 0.0:
        return 0.0
    return dot / math.sqrt(na * nb)


def write_embeddings(rows, model, path=None):
    target = path or EMBED_PATH
    os.makedirs(os.path.dirname(target), exist_ok=True)
    dim = len(rows[0]["vector"]) if rows else 0
    payload = {
        "claim_boundary": (
            "Research documentation. NOT evidence for or against the "
            "Riemann Hypothesis in either direction. NO RH CLAIM."
        ),
        "dim": dim,
        "model": model,
        "n": len(rows),
        "records": [
            {
                "model": model,
                "path": row["path"],
                "sha256": row["sha256"],
                "vector": row["vector"],
            }
            for row in rows
        ],
    }
    with open(target, "w", encoding="utf-8") as fh:
        json.dump(payload, fh, ensure_ascii=False, separators=(",", ":"))
        fh.write("\n")
    return payload


def build_embeddings(svc, records):
    existing = embeddings_by_path(load_embeddings())
    planned = []
    reuse = []
    for rec in records:
        path = rec.get("path") or ""
        if not path:
            continue
        text = record_embed_text(rec)
        digest = text_sha256(svc.embed_model, text)
        prev = existing.get(path)
        if (
            prev
            and prev.get("sha256") == digest
            and prev.get("model") == svc.embed_model
            and prev.get("vector")
        ):
            reuse.append(
                {
                    "path": path,
                    "sha256": digest,
                    "vector": prev["vector"],
                }
            )
            continue
        planned.append((path, text, digest))
    new_rows = []
    if planned:
        # empty text still needs a vector; use path as fallback
        texts = [t if t else p for p, t, _d in planned]
        vectors = svc.embed(texts)
        for (path, _text, digest), vec in zip(planned, vectors):
            new_rows.append({"path": path, "sha256": digest, "vector": vec})
    merged = reuse + new_rows
    merged.sort(key=lambda row: row["path"])
    return merged, len(planned), len(reuse)


def main(argv=None):
    argv = list(argv if argv is not None else sys.argv[1:])
    dry = "--dry-run" in argv
    records = load_catalog_records()
    svc = OpenAIService(dry_run=dry)
    t0 = time.time()
    rows, n_new, n_reuse = build_embeddings(svc, records)
    elapsed = time.time() - t0
    if dry:
        sys.stdout.write(
            "embed_catalog dry-run: records=%d new=%d reuse=%d model=%s spent=%.6f\n"
            % (len(rows), n_new, n_reuse, svc.embed_model, svc.spent_usd)
        )
        return 0
    payload = write_embeddings(rows, svc.embed_model)
    sys.stdout.write(
        "embed_catalog: n=%d dim=%d new=%d reuse=%d model=%s time=%.2fs spent=%.6f\n"
        % (
            payload["n"],
            payload["dim"],
            n_new,
            n_reuse,
            svc.embed_model,
            elapsed,
            svc.spent_usd,
        )
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
