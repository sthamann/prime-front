#!/usr/bin/env python3
"""Merge, validate, and publish the RH concept map."""
from __future__ import annotations

import json
import re
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
CATALOG_DIR = HERE.parent
REPO = HERE.parents[2]
VIEWER_OUT = CATALOG_DIR / "viewer" / "public" / "data" / "concepts.json"
CLAIM_BOUNDARY = "Typed research documentation only. No claim for or against RH."


def read_json(path: Path):
    return json.loads(path.read_text())


def catalog_records() -> dict[str, dict]:
    payload = read_json(CATALOG_DIR / "rh_semantic_catalog.json")
    records = payload if isinstance(payload, list) else payload.get("records", [])
    by_path = {r["path"]: r for r in records if r.get("path")}
    part8 = CATALOG_DIR / "fragments" / "part_8.json"
    if part8.exists():
        extra = read_json(part8)
        for record in extra if isinstance(extra, list) else extra.get("records", []):
            if record.get("path"):
                by_path[record["path"]] = {**by_path.get(record["path"], {}), **record}
    return by_path


def validate_schema(payload: dict) -> None:
    schema = read_json(HERE / "schema.json")
    try:
        from jsonschema import Draft7Validator
    except ImportError:
        errors: list[str] = []

        def resolve(spec: dict) -> dict:
            if "$ref" not in spec:
                return spec
            current = schema
            for part in spec["$ref"].removeprefix("#/").split("/"):
                current = current[part]
            return current

        def check(value, spec: dict, path: str) -> None:
            spec = resolve(spec)
            expected = spec.get("type")
            type_ok = {
                "object": isinstance(value, dict),
                "array": isinstance(value, list),
                "string": isinstance(value, str),
                "integer": isinstance(value, int) and not isinstance(value, bool),
                "boolean": isinstance(value, bool),
            }.get(expected, True)
            if not type_ok:
                errors.append(f"{path}: expected {expected}")
                return
            if "enum" in spec and value not in spec["enum"]:
                errors.append(f"{path}: not in enum")
            if isinstance(value, str):
                if len(value) < spec.get("minLength", 0):
                    errors.append(f"{path}: below minLength")
                if spec.get("pattern") and not re.fullmatch(spec["pattern"], value):
                    errors.append(f"{path}: pattern mismatch")
            if isinstance(value, int) and value < spec.get("minimum", value):
                errors.append(f"{path}: below minimum")
            if isinstance(value, list):
                if len(value) < spec.get("minItems", 0):
                    errors.append(f"{path}: below minItems")
                for index, item in enumerate(value):
                    check(item, spec.get("items", {}), f"{path}[{index}]")
            if isinstance(value, dict):
                properties = spec.get("properties", {})
                for required in spec.get("required", []):
                    if required not in value:
                        errors.append(f"{path}: missing {required}")
                if spec.get("additionalProperties") is False:
                    for key in value.keys() - properties.keys():
                        errors.append(f"{path}: unexpected {key}")
                for key, item in value.items():
                    if key in properties:
                        check(item, properties[key], f"{path}.{key}")

        check(payload, schema, "$")
        if errors:
            raise ValueError(
                f"schema validation failed ({len(errors)} errors)\n"
                + "\n".join(errors[:20])
            )
    else:
        errors = sorted(Draft7Validator(schema).iter_errors(payload), key=lambda e: list(e.path))
        if errors:
            details = "\n".join(f"{list(e.path)}: {e.message}" for e in errors[:20])
            raise ValueError(f"schema validation failed ({len(errors)} errors)\n{details}")


def main() -> int:
    nodes = read_json(HERE / "seed_nodes.json")
    seed_edges = read_json(HERE / "seed_edges.json")
    extracted_path = HERE / "extracted_edges.json"
    extracted = read_json(extracted_path) if extracted_path.exists() else {"edges": []}
    records = catalog_records()
    node_ids = {n["id"] for n in nodes}
    if len(node_ids) != len(nodes):
        raise ValueError("duplicate node id")

    merged: dict[tuple, dict] = {}
    for edge in [*seed_edges, *extracted.get("edges", [])]:
        if edge["src"] not in node_ids:
            raise ValueError(f"unknown source node: {edge['src']}")
        if edge["rel"] in {"USED_BY", "KILLED_BY"}:
            if edge["dst"] not in records:
                raise ValueError(f"unknown attempt path: {edge['dst']}")
        elif edge["dst"] not in node_ids:
            raise ValueError(f"unknown destination node: {edge['dst']}")
        key = (edge["src"], edge["dst"], edge["rel"], edge["source"])
        merged[key] = edge
    edges = list(merged.values())

    attempts_by_node: dict[str, set[str]] = defaultdict(set)
    live_attempt_by_node: dict[str, bool] = defaultdict(bool)
    for edge in edges:
        if edge["rel"] not in {"USED_BY", "KILLED_BY"} or edge["dst"] not in records:
            continue
        path = edge["dst"]
        record = records[path]
        attempts_by_node[edge["src"]].add(path)
        reusable = record.get("reusable")
        if record.get("outcome") != "KILLED" or bool(reusable):
            live_attempt_by_node[edge["src"]] = True

    for node in nodes:
        node["attempt_count"] = len(attempts_by_node[node["id"]])
        classical_theorem = node["status"] == "CLASSICAL" and node["type"] == "THEOREM"
        node["alive"] = bool(classical_theorem or live_attempt_by_node[node["id"]])

    payload = {
        "claim_boundary": CLAIM_BOUNDARY,
        "generated_at": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "nodes": sorted(nodes, key=lambda n: n["id"]),
        "edges": sorted(
            edges,
            key=lambda e: (e["src"], e["rel"], e["dst"], e["source"]),
        ),
    }
    validate_schema(payload)
    (HERE / "rh_concept_map.json").write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n"
    )

    type_radii = {
        "OPEN_QUESTION": 140, "CRITERION": 220, "THEOREM": 300,
        "OBJECT": 390, "OPERATOR": 470, "INVARIANT": 540,
        "METHOD": 610, "GEOMETRY": 690, "TFPT_STRUCTURE": 770,
        "BARRIER": 850, "CLASS": 930,
    }
    viewer = json.loads(json.dumps(payload))
    for node in viewer["nodes"]:
        node["layout_hint"] = {
            "group": node["type"],
            "ring_radius": type_radii[node["type"]],
        }
    VIEWER_OUT.parent.mkdir(parents=True, exist_ok=True)
    VIEWER_OUT.write_text(json.dumps(viewer, ensure_ascii=False, indent=2) + "\n")
    print(
        f"validated nodes={len(nodes)} edges={len(edges)} "
        f"attempt_paths={len(records)} viewer={VIEWER_OUT.relative_to(REPO)}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
