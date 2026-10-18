#!/usr/bin/env python3
"""Extract sourced concept-to-attempt links from the RH semantic catalog."""
from __future__ import annotations

import argparse
import itertools
import json
import os
import re
import sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
CATALOG_DIR = HERE.parent
CATALOG = CATALOG_DIR / "rh_semantic_catalog.json"
PART8 = CATALOG_DIR / "fragments" / "part_8.json"
FIELDS = ("question", "mechanism", "result_verdict", "failed_because", "path")


def load_records() -> list[dict]:
    payload = json.loads(CATALOG.read_text())
    records = payload if isinstance(payload, list) else payload.get("records", [])
    by_path = {r.get("path"): r for r in records if r.get("path")}
    if PART8.exists():
        extra = json.loads(PART8.read_text())
        for record in extra if isinstance(extra, list) else extra.get("records", []):
            if record.get("path"):
                by_path[record["path"]] = {**by_path.get(record["path"], {}), **record}
    return sorted(by_path.values(), key=lambda r: r.get("path", ""))


def compile_lexicon(lexicon: dict[str, list[str]]) -> dict[str, list[re.Pattern]]:
    compiled = {}
    for concept_id, aliases in lexicon.items():
        patterns = []
        for alias in aliases:
            escaped = re.escape(alias)
            patterns.append(re.compile(r"(?<!\w)" + escaped + r"(?!\w)", re.IGNORECASE))
        compiled[concept_id] = patterns
    return compiled


def mentions(text: str, patterns: dict[str, list[re.Pattern]]) -> set[str]:
    return {
        concept_id
        for concept_id, regexes in patterns.items()
        if any(regex.search(text) for regex in regexes)
    }


def llm_mentions(records: list[dict], lexicon: dict[str, list[str]]) -> dict[str, set[str]]:
    """Optional conservative mention expansion for at most 200 central records."""
    if not os.environ.get("OPENAI_API_KEY"):
        print("llm=skipped(no OPENAI_API_KEY)", file=sys.stderr)
        return {}
    sys.path.insert(0, str(CATALOG_DIR))
    from openai_service import OpenAIService  # type: ignore

    service = OpenAIService(budget_usd=float(os.environ.get("RHMAP_LLM_BUDGET", "2")))
    candidates = [
        r for r in records
        if r.get("rh_relevance") in {"EQUIVALENCE", "LOAD_BEARING_OPEN"}
    ][:200]
    ids = sorted(lexicon)
    schema = {
        "title": "concept_mentions",
        "type": "object",
        "additionalProperties": False,
        "properties": {
            "concept_ids": {
                "type": "array",
                "items": {"type": "string", "enum": ids},
            }
        },
        "required": ["concept_ids"],
    }
    system = (
        "Identify only explicit mentions of supplied concept ids in an RH-corpus "
        "record. Do not infer implications or truth. Return concept_ids only."
    )
    found: dict[str, set[str]] = {}
    for record in candidates:
        text = "\n".join(str(record.get(k) or "") for k in FIELDS)
        prompt = "Allowed concepts:\n" + ", ".join(ids) + "\nRecord:\n" + text[:6000]
        try:
            payload = service.chat_json(system, prompt, schema, max_tokens=300)
        except Exception as exc:
            print(f"llm=stopped({type(exc).__name__})", file=sys.stderr)
            break
        chosen = {x for x in payload.get("concept_ids", []) if x in lexicon}
        if chosen:
            found[record["path"]] = chosen
    print(f"llm_records={len(candidates)} llm_paths={len(found)}", file=sys.stderr)
    return found


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--llm", action="store_true", help="add optional heuristic LLM mentions")
    args = parser.parse_args()
    lexicon = json.loads((HERE / "lexicon.json").read_text())
    patterns = compile_lexicon(lexicon)
    records = load_records()
    llm_found = llm_mentions(records, lexicon) if args.llm else {}
    edges: list[dict] = []
    co_counts: Counter[tuple[str, str]] = Counter()
    used_count = killed_count = llm_count = 0

    for record in records:
        path = record.get("path")
        if not path:
            continue
        full_text = "\n".join(str(record.get(key) or "") for key in FIELDS)
        found = mentions(full_text, patterns)
        failed = mentions(str(record.get("failed_because") or ""), patterns)
        for concept_id in sorted(found):
            edges.append({
                "src": concept_id, "dst": path, "rel": "USED_BY",
                "strength": "HEURISTIC", "source": f"catalog:{path}",
                "note": f"Lexical mention in catalog record; outcome={record.get('outcome', '')}.",
            })
            used_count += 1
        if record.get("outcome") == "KILLED":
            for concept_id in sorted(found & failed):
                edges.append({
                    "src": concept_id, "dst": path, "rel": "KILLED_BY",
                    "strength": "HEURISTIC", "source": f"catalog:{path}",
                    "note": f"Concept occurs in failed_because; class={record.get('failure_class', '')}.",
                })
                killed_count += 1
        for concept_id in sorted(llm_found.get(path, set()) - found):
            edges.append({
                "src": concept_id, "dst": path, "rel": "USED_BY",
                "strength": "HEURISTIC", "source": "llm",
                "note": "Optional model-classified explicit mention; no implication inferred.",
            })
            found.add(concept_id)
            llm_count += 1
        for pair in itertools.combinations(sorted(found), 2):
            co_counts[pair] += 1

    kept_co = 0
    for (left, right), weight in sorted(co_counts.items()):
        if weight < 3:
            continue
        edges.append({
            "src": left, "dst": right, "rel": "CO_OCCURS",
            "strength": "STATISTICAL", "source": "catalog-cooccurrence",
            "note": "Concept aliases occur in the same catalog records.",
            "weight": weight,
        })
        kept_co += 1

    output = {
        "claim_boundary": "Research map only. No claim for or against RH.",
        "records_scanned": len(records),
        "edges": edges,
        "counts": {
            "used_by": used_count,
            "killed_by": killed_count,
            "llm_used_by": llm_count,
            "co_occurs": kept_co,
        },
    }
    (HERE / "extracted_edges.json").write_text(
        json.dumps(output, ensure_ascii=False, indent=2) + "\n"
    )
    print(
        f"records={len(records)} used_by={used_count} killed_by={killed_count} "
        f"llm={llm_count} co_occurs={kept_co} total={len(edges)}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
