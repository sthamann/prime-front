#!/usr/bin/env python3
"""Terse stdlib query CLI for the RH concept map."""
from __future__ import annotations

import argparse
import csv
import html
import io
import json
import sys
from collections import Counter, defaultdict, deque
from pathlib import Path

HERE = Path(__file__).resolve().parent
MAP_PATH = HERE / "rh_concept_map.json"
SEED_PATH = HERE / "seed_edges.json"
MAX_LINES = 60


class Map:
    def __init__(self) -> None:
        self.data = json.loads(MAP_PATH.read_text())
        self.nodes = {n["id"]: n for n in self.data["nodes"]}
        self.edges = self.data["edges"]
        self.seed_edges = json.loads(SEED_PATH.read_text())
        self.outgoing: dict[str, list[dict]] = defaultdict(list)
        self.incident: dict[str, list[dict]] = defaultdict(list)
        for edge in self.edges:
            self.outgoing[edge["src"]].append(edge)
            self.incident[edge["src"]].append(edge)
            self.incident[edge["dst"]].append(edge)

    def require(self, id_: str) -> dict:
        if id_ not in self.nodes:
            raise SystemExit(f"unknown concept id: {id_}")
        return self.nodes[id_]

    def adjacency(self, avoid_killed: bool, seed_only: bool = False) -> dict[str, set[str]]:
        source = self.seed_edges if seed_only else self.edges
        graph: dict[str, set[str]] = defaultdict(set)
        for edge in source:
            if edge["rel"] in {"USED_BY", "KILLED_BY", "CO_OCCURS", "INSTANCE_OF"}:
                continue
            if edge["src"] not in self.nodes or edge["dst"] not in self.nodes:
                continue
            if avoid_killed and (
                self.nodes[edge["src"]]["status"] == "KILLED_HERE"
                or self.nodes[edge["dst"]]["status"] == "KILLED_HERE"
            ):
                continue
            graph[edge["src"]].add(edge["dst"])
            graph[edge["dst"]].add(edge["src"])
        return graph

    def shortest_paths(
        self, start: str, goal: str, avoid_killed: bool, max_hops: int = 5
    ) -> list[list[str]]:
        graph = self.adjacency(avoid_killed)
        queue = deque([[start]])
        best = None
        paths = []
        while queue:
            path = queue.popleft()
            hops = len(path) - 1
            if best is not None and hops > best:
                break
            if hops > max_hops:
                continue
            current = path[-1]
            if current == goal:
                best = hops
                paths.append(path)
                continue
            for nxt in sorted(graph.get(current, ())):
                if nxt not in path:
                    queue.append([*path, nxt])
        return paths


def emit(payload, json_mode: bool) -> None:
    if json_mode:
        print(json.dumps(payload, ensure_ascii=False, separators=(",", ":")))
        return
    if isinstance(payload, str):
        lines = payload.splitlines()
    elif isinstance(payload, list):
        lines = [str(x) for x in payload]
    else:
        lines = [json.dumps(payload, ensure_ascii=False)]
    if len(lines) > MAX_LINES:
        lines = [*lines[: MAX_LINES - 1], f"… clipped {len(lines) - MAX_LINES + 1} lines"]
    print("\n".join(lines))


def equivalent_criteria(m: Map) -> list[dict]:
    ids = set()
    for edge in m.edges:
        if edge["rel"] != "EQUIVALENT_TO" or edge["strength"] != "THEOREM":
            continue
        if edge["src"] == "riemann-hypothesis" and edge["dst"] in m.nodes:
            ids.add(edge["dst"])
        if edge["dst"] == "riemann-hypothesis" and edge["src"] in m.nodes:
            ids.add(edge["src"])
    return [
        {
            "id": id_,
            "name": m.nodes[id_]["name"],
            "attempt_count": m.nodes[id_]["attempt_count"],
            "has_attempt": m.nodes[id_]["attempt_count"] > 0,
            "status": m.nodes[id_]["status"],
        }
        for id_ in sorted(ids)
        if m.nodes[id_]["type"] == "CRITERION"
    ]


def gaps(m: Map) -> dict:
    g1 = [
        {"id": n["id"], "type": n["type"]}
        for n in m.nodes.values()
        if n["attempt_count"] == 0
    ]
    used_sources = {e["src"] for e in m.edges if e["rel"] == "USED_BY"}
    g2 = [
        {"id": n["id"], "status": n["status"]}
        for n in m.nodes.values()
        if n["type"] == "CRITERION" and n["id"] not in used_sources
    ]

    co_pairs = {
        frozenset((e["src"], e["dst"]))
        for e in m.edges if e["rel"] == "CO_OCCURS"
    }
    graph = m.adjacency(False, seed_only=True)
    candidate_pairs = set()
    for src, first in graph.items():
        if not m.nodes[src]["alive"]:
            continue
        for dst in first:
            if m.nodes[dst]["alive"]:
                candidate_pairs.add(tuple(sorted((src, dst))))
            for dst2 in graph.get(dst, ()):
                if src != dst2 and m.nodes[dst2]["alive"]:
                    candidate_pairs.add(tuple(sorted((src, dst2))))
    g3 = []
    for left, right in candidate_pairs:
        if frozenset((left, right)) in co_pairs:
            continue
        score = m.nodes[left]["attempt_count"] + m.nodes[right]["attempt_count"]
        g3.append({"pair": [left, right], "attempt_score": score})
    g3.sort(key=lambda row: (-row["attempt_score"], row["pair"]))

    killed = Counter(
        e["src"] for e in m.edges
        if e["rel"] == "KILLED_BY" and e["src"] in m.nodes
    )
    g4 = [
        {"id": n["id"], "killed_by": killed[n["id"]]}
        for n in m.nodes.values() if n["type"] == "BARRIER"
    ]
    g4.sort(key=lambda row: (-row["killed_by"], row["id"]))

    targets = [row["id"] for row in equivalent_criteria(m)]
    g5 = []
    for n in sorted(m.nodes.values(), key=lambda x: x["id"]):
        if n["type"] != "TFPT_STRUCTURE":
            continue
        options = []
        for target in targets:
            paths = m.shortest_paths(n["id"], target, True)
            if paths:
                options.extend(paths)
        options.sort(key=lambda p: (len(p), p))
        g5.append({
            "id": n["id"],
            "path": options[0] if options else [],
            "hops": len(options[0]) - 1 if options else None,
        })

    g6 = []
    for n in sorted(m.nodes.values(), key=lambda x: x["id"]):
        if n["type"] != "OPEN_QUESTION":
            continue
        targets_ = sorted({
            e["dst"] for e in m.outgoing[n["id"]]
            if e["rel"] == "WOULD_CLOSE" and e["dst"] in m.nodes
        })
        g6.append({
            "id": n["id"],
            "targets": targets_,
            "alive_targets": sum(m.nodes[x]["alive"] for x in targets_),
            "target_count": len(targets_),
        })
    return {"G1": g1, "G2": g2, "G3": g3, "G4": g4, "G5": g5, "G6": g6}


def export_map(m: Map, format_: str, out: Path) -> None:
    concept_ids = set(m.nodes)
    attempt_ids = sorted({
        endpoint
        for e in m.edges
        for endpoint in (e["src"], e["dst"])
        if endpoint not in concept_ids
    })
    if format_ == "csv":
        buffer = io.StringIO()
        writer = csv.DictWriter(
            buffer, fieldnames=["src", "dst", "rel", "strength", "source", "weight", "note"]
        )
        writer.writeheader()
        for edge in m.edges:
            writer.writerow({key: edge.get(key, "") for key in writer.fieldnames})
        out.write_text(buffer.getvalue())
        return
    if format_ == "md":
        by_type = Counter(n["type"] for n in m.nodes.values())
        by_rel = Counter(e["rel"] for e in m.edges)
        lines = ["# RH concept map", "", m.data["claim_boundary"], "", "## Node types"]
        lines += [f"- {k}: {v}" for k, v in sorted(by_type.items())]
        lines += ["", "## Relations"]
        lines += [f"- {k}: {v}" for k, v in sorted(by_rel.items())]
        out.write_text("\n".join(lines) + "\n")
        return
    if format_ == "dot":
        lines = ["digraph rhmap {"]
        for n in m.nodes.values():
            label = n["name"].replace('"', '\\"')
            lines.append(f'  "{n["id"]}" [label="{label}"];')
        for path in attempt_ids:
            lines.append(f'  "{path}" [shape=box,label="{path}"];')
        for e in m.edges:
            lines.append(f'  "{e["src"]}" -> "{e["dst"]}" [label="{e["rel"]}"];')
        lines.append("}")
        out.write_text("\n".join(lines) + "\n")
        return

    graphml = format_ == "graphml"
    root = "graphml" if graphml else "gexf"
    graph_open = '<graph edgedefault="directed">' if graphml else '<graph mode="static" defaultedgetype="directed"><nodes>'
    lines = [f'<?xml version="1.0" encoding="UTF-8"?>', f"<{root}>", graph_open]
    for n in m.nodes.values():
        label = html.escape(n["name"], quote=True)
        if graphml:
            lines.append(f'<node id="{n["id"]}"><data key="label">{label}</data></node>')
        else:
            lines.append(f'<node id="{n["id"]}" label="{label}"/>')
    for path in attempt_ids:
        escaped = html.escape(path, quote=True)
        if graphml:
            lines.append(f'<node id="{escaped}"><data key="label">{escaped}</data></node>')
        else:
            lines.append(f'<node id="{escaped}" label="{escaped}"/>')
    if not graphml:
        lines.append("</nodes><edges>")
    for index, e in enumerate(m.edges):
        src, dst, rel = map(lambda x: html.escape(str(x), quote=True), (e["src"], e["dst"], e["rel"]))
        if graphml:
            lines.append(f'<edge id="e{index}" source="{src}" target="{dst}"><data key="rel">{rel}</data></edge>')
        else:
            lines.append(f'<edge id="e{index}" source="{src}" target="{dst}" label="{rel}"/>')
    lines.append("</graph>" if graphml else "</edges></graph>")
    lines.append(f"</{root}>")
    out.write_text("\n".join(lines) + "\n")


def main(argv=None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    json_mode = "--json" in argv
    argv = [item for item in argv if item != "--json"]
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="command", required=True)
    show = sub.add_parser("show"); show.add_argument("id")
    neighbors = sub.add_parser("neighbors"); neighbors.add_argument("id"); neighbors.add_argument("--rel")
    path = sub.add_parser("path"); path.add_argument("a"); path.add_argument("b"); path.add_argument("--avoid-killed", action="store_true")
    sub.add_parser("equivalents")
    sub.add_parser("gaps")
    export = sub.add_parser("export"); export.add_argument("--format", choices=["graphml", "gexf", "dot", "csv", "md"], required=True); export.add_argument("out")
    sub.add_parser("stats")
    args = parser.parse_args(argv)
    m = Map()

    if args.command == "show":
        node = m.require(args.id)
        result = {**node, "edges": m.incident[args.id][:40]}
        emit(result, json_mode)
    elif args.command == "neighbors":
        m.require(args.id)
        rows = [
            e for e in m.incident[args.id]
            if args.rel is None or e["rel"] == args.rel
        ]
        emit(rows[:59], json_mode)
    elif args.command == "path":
        m.require(args.a); m.require(args.b)
        paths = m.shortest_paths(args.a, args.b, args.avoid_killed)
        emit({"hops": len(paths[0]) - 1 if paths else None, "paths": paths}, json_mode)
    elif args.command == "equivalents":
        rows = equivalent_criteria(m)
        if json_mode:
            emit(rows, True)
        else:
            emit([f"{r['id']}: attempts={r['attempt_count']} status={r['status']}" for r in rows], False)
    elif args.command == "gaps":
        result = gaps(m)
        (HERE / "gaps_report.json").write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
        if json_mode:
            emit(result, True)
        else:
            lines = []
            for key in ("G1", "G2", "G3", "G4", "G5", "G6"):
                lines.append(f"{key} count={len(result[key])}")
                lines += [json.dumps(row, ensure_ascii=False) for row in result[key][:8]]
            emit(lines, False)
    elif args.command == "export":
        out = Path(args.out)
        export_map(m, args.format, out)
        emit({"format": args.format, "out": str(out), "nodes": len(m.nodes), "edges": len(m.edges)}, json_mode)
    elif args.command == "stats":
        result = {
            "nodes": len(m.nodes), "edges": len(m.edges),
            "node_types": dict(sorted(Counter(n["type"] for n in m.nodes.values()).items())),
            "relations": dict(sorted(Counter(e["rel"] for e in m.edges).items())),
            "strengths": dict(sorted(Counter(e["strength"] for e in m.edges).items())),
            "attempt_links": sum(e["rel"] in {"USED_BY", "KILLED_BY"} for e in m.edges),
            "alive_nodes": sum(n["alive"] for n in m.nodes.values()),
        }
        emit(result, json_mode)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
