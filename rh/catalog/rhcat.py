#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""rhcat — compact CLI over rh/catalog/rh_semantic_catalog.json.

stdlib only. Lines clip at 120 chars unless --json. NO RH CLAIM.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys

CATALOG_DIR = os.path.dirname(os.path.abspath(__file__))
CATALOG_PATH = os.path.join(CATALOG_DIR, "rh_semantic_catalog.json")
TAXONOMY_PATH = os.path.join(CATALOG_DIR, "taxonomy.json")
FRAGMENTS_DIR = os.path.join(CATALOG_DIR, "fragments")
AUTO_DRAFTS_PATH = os.path.join(FRAGMENTS_DIR, "auto_drafts.json")
LINE_WIDTH = 120

STOPWORDS = frozenset(
    "a an the of and to in for with on by is it as at or be from that this "
    "an are was were been being into over under via vs versus not no nor "
    "its their his her our your".split()
)

TOKEN_RE = re.compile(r"[a-z0-9*]+", re.I)
ROUND_TOKEN_RE = re.compile(r"r\d+", re.I)


def clip(text, width=LINE_WIDTH):
    text = " ".join(str(text).split())
    if len(text) <= width:
        return text
    return text[: width - 3] + "..."


def load_catalog():
    if not os.path.isfile(CATALOG_PATH):
        sys.stderr.write(
            "catalog missing: run python3 rh/catalog/build_catalog.py\n"
        )
        sys.exit(2)
    with open(CATALOG_PATH, "r", encoding="utf-8") as fh:
        payload = json.load(fh)
    if isinstance(payload, list):
        return payload
    return payload.get("records") or []


def load_taxonomy():
    with open(TAXONOMY_PATH, "r", encoding="utf-8") as fh:
        return json.load(fh)


def emit_json(obj):
    sys.stdout.write(
        json.dumps(obj, indent=2, sort_keys=True, ensure_ascii=False) + "\n"
    )


def flatten_strings(obj):
    if obj is None:
        return
    if isinstance(obj, str):
        yield obj
        return
    if isinstance(obj, dict):
        for val in obj.values():
            yield from flatten_strings(val)
        return
    if isinstance(obj, (list, tuple)):
        for val in obj:
            yield from flatten_strings(val)


def one_line(rec):
    bits = [
        rec.get("round") or "-",
        rec.get("family") or "-",
        rec.get("outcome") or "-",
        rec.get("failure_class") or "-",
        rec.get("path") or "-",
    ]
    return clip("  ".join(bits))


def compact_hits(records, extra_field=None):
    lines = []
    for rec in records:
        line = one_line(rec)
        lines.append(line)
        extra = (rec.get(extra_field) or "").strip() if extra_field else ""
        if extra:
            lines.append(clip("  " + extra))
    return lines


def filter_family(records, family_id):
    return [
        r
        for r in records
        if r.get("family") == family_id or family_id in (r.get("family_secondary") or [])
    ]


def round_tokens(round_s):
    return [m.group(0).lower() for m in ROUND_TOKEN_RE.finditer(round_s or "")]


def dossier_match(rec, query):
    q = query.strip()
    path = rec.get("path") or ""
    if "/" in q or q.endswith(".py") or q.endswith(".lean") or q.endswith(".tex"):
        return path == q or path.endswith(q) or q in path
    q_low = q.lower()
    if ROUND_TOKEN_RE.fullmatch(q_low):
        return q_low in round_tokens(rec.get("round") or "")
    return (rec.get("round") or "") == q or path == q or path.endswith(q)


def tokenize(text):
    out = []
    for tok in TOKEN_RE.findall(text or ""):
        low = tok.lower()
        if low in STOPWORDS or len(low) < 2:
            continue
        out.append(low)
    return out


def overlap_score(query_tokens, rec):
    blob = " ".join(
        [
            rec.get("mechanism") or "",
            rec.get("question") or "",
            rec.get("failed_because") or "",
        ]
    )
    rec_tokens = set(tokenize(blob))
    if not query_tokens or not rec_tokens:
        return 0.0, 0
    inter = query_tokens & rec_tokens
    if not inter:
        return 0.0, 0
    union = query_tokens | rec_tokens
    return len(inter) / float(len(union)), len(inter)


def cmd_search(records, pattern, as_json):
    try:
        cre = re.compile(pattern)
    except re.error as exc:
        sys.stderr.write("bad regex: %s\n" % exc)
        return 2
    hits = []
    for rec in records:
        blob = "\n".join(flatten_strings(rec))
        if cre.search(blob):
            hits.append(rec)
    if as_json:
        emit_json(hits)
        return 0
    sys.stdout.write(clip("search %s  n=%d" % (pattern, len(hits))) + "\n")
    for line in compact_hits(hits, "question"):
        sys.stdout.write(line + "\n")
    return 0


def cmd_family(records, family_id, as_json):
    hits = filter_family(records, family_id)
    if as_json:
        emit_json(hits)
        return 0
    sys.stdout.write(clip("family %s  n=%d" % (family_id, len(hits))) + "\n")
    for line in compact_hits(hits, "question"):
        sys.stdout.write(line + "\n")
    return 0


def cmd_kind(records, kind_id, as_json):
    hits = [r for r in records if r.get("kind") == kind_id]
    if as_json:
        emit_json(hits)
        return 0
    sys.stdout.write(clip("kind %s  n=%d" % (kind_id, len(hits))) + "\n")
    for line in compact_hits(hits, "question"):
        sys.stdout.write(line + "\n")
    return 0


def cmd_kills(records, failure_class, as_json):
    hits = [r for r in records if r.get("outcome") == "KILLED"]
    if failure_class:
        hits = [r for r in hits if r.get("failure_class") == failure_class]
    if as_json:
        emit_json(hits)
        return 0
    label = "kills" + ((" class=" + failure_class) if failure_class else "")
    sys.stdout.write(clip("%s  n=%d" % (label, len(hits))) + "\n")
    for line in compact_hits(hits, "failed_because"):
        sys.stdout.write(line + "\n")
    return 0


def cmd_open(records, as_json):
    hits = [r for r in records if r.get("rh_relevance") == "LOAD_BEARING_OPEN"]
    if as_json:
        emit_json(hits)
        return 0
    sys.stdout.write(clip("open LOAD_BEARING_OPEN  n=%d" % len(hits)) + "\n")
    for line in compact_hits(hits, "question"):
        sys.stdout.write(line + "\n")
    return 0


def cmd_reusable(records, family_id, as_json):
    hits = [r for r in records if (r.get("reusable") or "").strip()]
    if family_id:
        hits = filter_family(hits, family_id)
    if as_json:
        emit_json(hits)
        return 0
    label = "reusable" + ((" family=" + family_id) if family_id else "")
    sys.stdout.write(clip("%s  n=%d" % (label, len(hits))) + "\n")
    for line in compact_hits(hits, "reusable"):
        sys.stdout.write(line + "\n")
    return 0


def cmd_dossier(records, query, as_json):
    hits = [r for r in records if dossier_match(r, query)]
    if as_json:
        emit_json(hits)
        return 0
    if not hits:
        sys.stdout.write(clip("dossier %s  n=0" % query) + "\n")
        return 0
    sys.stdout.write(clip("dossier %s  n=%d" % (query, len(hits))) + "\n")
    for rec in hits:
        sys.stdout.write(clip("--- %s ---" % rec.get("path")) + "\n")
        keys = (
            "path",
            "round",
            "role",
            "kind",
            "family",
            "outcome",
            "failure_class",
            "rh_relevance",
            "confidence",
            "question",
            "mechanism",
            "result_verdict",
            "solved",
            "failed_because",
            "reusable",
            "status_raw",
            "readme_lines",
        )
        for key in keys:
            val = rec.get(key)
            if val is None or val == "" or val == []:
                continue
            sys.stdout.write(clip("%s: %s" % (key, val)) + "\n")
        lids = rec.get("ledger_ids") or []
        if lids:
            sys.stdout.write(clip("ledger_ids: " + ", ".join(lids)) + "\n")
        sec = rec.get("family_secondary") or []
        if sec:
            sys.stdout.write(clip("family_secondary: " + ", ".join(sec)) + "\n")
        deps = rec.get("depends_on") or []
        if deps:
            sys.stdout.write(clip("depends_on: " + ", ".join(deps)) + "\n")
        arts = rec.get("artifacts") or {}
        for key in ("probe", "result_json", "tex"):
            if arts.get(key):
                sys.stdout.write(clip("artifacts.%s: %s" % (key, arts[key])) + "\n")
        for key in ("lean", "figures"):
            if arts.get(key):
                sys.stdout.write(
                    clip("artifacts.%s: %s" % (key, ", ".join(arts[key]))) + "\n"
                )
        window = rec.get("readme_lines") or ""
        if window:
            sys.stdout.write(
                clip("README window: rh/README.md lines %s (do not read whole file)" % window)
                + "\n"
            )
        elif rec.get("round"):
            sys.stdout.write(
                clip("README window: unset; grep rh/README.md for %s" % rec["round"])
                + "\n"
            )
    return 0


def _scope_counts(rows):
    return {
        "n": len(rows),
        "open": sum(1 for r in rows if r.get("rh_relevance") == "LOAD_BEARING_OPEN"),
        "certified_or_proved": sum(
            1 for r in rows if r.get("outcome") in ("CERTIFIED", "PROVED")
        ),
        "killed": sum(1 for r in rows if r.get("outcome") == "KILLED"),
        "reusable": sum(1 for r in rows if (r.get("reusable") or "").strip()),
    }


def curated_only(records, include_drafts):
    if include_drafts:
        return records
    return [r for r in records if not r.get("draft")]


def cmd_stats(records, as_json):
    stats_path = os.path.join(CATALOG_DIR, "stats.json")
    if os.path.isfile(stats_path):
        with open(stats_path, "r", encoding="utf-8") as fh:
            stats = json.load(fh)
    else:
        stats = {"n_records": len(records)}
    curated = [r for r in records if not r.get("draft")]
    drafts = [r for r in records if r.get("draft")]
    c_counts = _scope_counts(curated)
    d_counts = _scope_counts(drafts)
    stats["curated"] = c_counts
    stats["drafts"] = d_counts
    if as_json:
        emit_json(stats)
        return 0
    sys.stdout.write(
        clip(
            "records=%d curated=%d drafts=%d review=%d viol=%d"
            % (
                stats.get("n_records", len(records)),
                c_counts["n"],
                d_counts["n"],
                stats.get("n_needs_review", 0),
                stats.get("n_validation_violations", 0),
            )
        )
        + "\n"
    )
    sys.stdout.write(
        clip(
            "curated: open=%d cert/proved=%d killed=%d reusable=%d"
            % (
                c_counts["open"],
                c_counts["certified_or_proved"],
                c_counts["killed"],
                c_counts["reusable"],
            )
        )
        + "\n"
    )
    sys.stdout.write(
        clip(
            "drafts: open=%d cert/proved=%d killed=%d reusable=%d"
            % (
                d_counts["open"],
                d_counts["certified_or_proved"],
                d_counts["killed"],
                d_counts["reusable"],
            )
        )
        + "\n"
    )
    for label, key in (
        ("kind", "by_kind"),
        ("outcome", "by_outcome"),
        ("fail", "by_failure_class"),
        ("rel", "by_rh_relevance"),
    ):
        mapping = stats.get(key) or {}
        bits = ["%s=%d" % (k, v) for k, v in mapping.items() if v]
        if bits:
            sys.stdout.write(clip(label + ": " + " ".join(bits)) + "\n")
    return 0


def round_sort_tuple(round_s):
    nums = [int(tok[1:]) for tok in ROUND_TOKEN_RE.findall(round_s or "")]
    if nums:
        return (0, nums[0], round_s or "")
    return (1, 0, round_s or "")


def cmd_todo(records, as_json):
    hits = [
        r
        for r in records
        if r.get("needs_review") or r.get("draft")
    ]
    hits.sort(
        key=lambda r: (round_sort_tuple(r.get("round") or ""), r.get("path") or ""),
        reverse=True,
    )
    if as_json:
        emit_json(hits)
        return 0
    sys.stdout.write(clip("todo needs_review/draft  n=%d" % len(hits)) + "\n")
    for rec in hits:
        mark = "draft" if rec.get("draft") else "review"
        sys.stdout.write(
            clip(
                "%s  %s  %s  %s  %s"
                % (
                    rec.get("round") or "-",
                    mark,
                    rec.get("family") or "-",
                    rec.get("outcome") or "-",
                    rec.get("path") or "-",
                )
            )
            + "\n"
        )
    return 0


def _curated_paths():
    found = set()
    if not os.path.isdir(FRAGMENTS_DIR):
        return found
    for name in sorted(os.listdir(FRAGMENTS_DIR)):
        if not name.startswith("part_") or not name.endswith(".json"):
            continue
        fpath = os.path.join(FRAGMENTS_DIR, name)
        try:
            payload = json.load(open(fpath, encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            continue
        if isinstance(payload, list):
            for item in payload:
                if isinstance(item, dict) and item.get("path"):
                    found.add(item["path"])
    return found


def _load_auto_drafts():
    if not os.path.isfile(AUTO_DRAFTS_PATH):
        return []
    try:
        payload = json.load(open(AUTO_DRAFTS_PATH, encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return []
    return payload if isinstance(payload, list) else []


def cmd_new(records, path, as_json):
    rel = path.replace("\\", "/")
    if rel in _curated_paths():
        sys.stderr.write("already curated: %s\n" % rel)
        return 1
    draft = None
    for item in _load_auto_drafts():
        if isinstance(item, dict) and item.get("path") == rel:
            draft = dict(item)
            break
    if draft is None:
        for rec in records:
            if rec.get("path") == rel:
                draft = dict(rec)
                break
    if draft is None:
        sys.stderr.write("no auto-draft or catalog row for %s; run autodraft.py\n" % rel)
        return 1
    draft.pop("draft", None)
    draft["needs_review"] = True
    draft["confidence"] = "low"
    tokens = ROUND_TOKEN_RE.findall(draft.get("round") or "")
    slug = tokens[0].lower() if tokens else re.sub(
        r"[^A-Za-z0-9._-]+", "_", draft.get("round") or "unk"
    ) or "unk"
    out_path = os.path.join(FRAGMENTS_DIR, "part_new_%s.json" % slug)
    existing = []
    if os.path.isfile(out_path):
        try:
            payload = json.load(open(out_path, encoding="utf-8"))
            if isinstance(payload, list):
                existing = payload
        except (OSError, json.JSONDecodeError):
            existing = []
        if any(isinstance(x, dict) and x.get("path") == rel for x in existing):
            sys.stderr.write("already in %s\n" % os.path.relpath(out_path))
            return 1
    existing.append(draft)
    os.makedirs(FRAGMENTS_DIR, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as fh:
        json.dump(existing, fh, indent=2, sort_keys=True, ensure_ascii=False)
        fh.write("\n")
    if as_json:
        emit_json({"wrote": os.path.relpath(out_path), "path": rel, "record": draft})
        return 0
    sys.stdout.write(
        clip("wrote %s  complete the fragment then build_catalog.py" % os.path.relpath(out_path))
        + "\n"
    )
    return 0


def _keyword_check_rows(records, description, limit=10):
    qtoks = set(tokenize(description))
    scored = []
    for rec in records:
        jaccard, n_inter = overlap_score(qtoks, rec)
        if n_inter <= 0:
            continue
        killed = rec.get("outcome") == "KILLED"
        scored.append((jaccard, n_inter, killed, rec))
    scored.sort(
        key=lambda row: (-row[2], -row[0], -row[1], row[3].get("round") or "", row[3].get("path") or "")
    )
    payload = []
    for jaccard, n_inter, killed, rec in scored[:limit]:
        payload.append(
            {
                "round": rec.get("round"),
                "path": rec.get("path"),
                "family": rec.get("family"),
                "outcome": rec.get("outcome"),
                "failure_class": rec.get("failure_class"),
                "jaccard": round(jaccard, 4),
                "overlap": n_inter,
                "score": round(jaccard, 4),
                "source": "keyword",
                "mechanism": rec.get("mechanism") or "",
                "failed_because": rec.get("failed_because") or "",
            }
        )
    return qtoks, payload


def _semantic_rank(records, query, k=10, killed_first=False):
    try:
        from embed_catalog import cosine, embeddings_by_path, load_embeddings
        from openai_service import OpenAIService, key_resolves
    except ImportError as exc:
        return None, "semantic helpers unavailable (%s)" % exc
    payload = load_embeddings()
    if not payload:
        return None, "embeddings absent"
    if not key_resolves():
        return None, "no resolvable API key"
    try:
        svc = OpenAIService(embed_model=payload.get("model"))
        vectors = svc.embed([query])
    except Exception as exc:
        return None, "embed failed: %s" % exc
    if not vectors or not vectors[0]:
        return None, "empty query embedding"
    qvec = vectors[0]
    by_path = {r.get("path"): r for r in records}
    scored = []
    for path, row in embeddings_by_path(payload).items():
        rec = by_path.get(path)
        if not rec:
            continue
        score = cosine(qvec, row.get("vector") or [])
        scored.append((score, rec.get("outcome") == "KILLED", rec))
    if killed_first:
        scored.sort(key=lambda row: (-row[1], -row[0], row[2].get("path") or ""))
    else:
        scored.sort(key=lambda row: (-row[0], row[2].get("path") or ""))
    out = []
    for score, _killed, rec in scored[:k]:
        out.append(
            {
                "round": rec.get("round"),
                "path": rec.get("path"),
                "family": rec.get("family"),
                "outcome": rec.get("outcome"),
                "failure_class": rec.get("failure_class"),
                "cosine": round(score, 4),
                "score": round(score, 4),
                "source": "semantic",
                "mechanism": rec.get("mechanism") or "",
                "failed_because": rec.get("failed_because") or "",
            }
        )
    return out, None


def _print_hit_rows(rows, score_key):
    for row in rows:
        mark = "KILL" if row.get("outcome") == "KILLED" else row.get("outcome")
        sys.stdout.write(
            clip(
                "%s  %s  %s  %s  %s=%.2f"
                % (
                    row.get("round") or "-",
                    mark,
                    row.get("family") or "-",
                    row.get("failure_class") or "-",
                    score_key,
                    float(row.get(score_key) or row.get("score") or 0.0),
                )
            )
            + "\n"
        )
        extra = row.get("failed_because") or row.get("mechanism")
        if extra:
            sys.stdout.write(clip("  " + extra) + "\n")


def cmd_semsearch(records, query, k, as_json):
    hits, err = _semantic_rank(records, query, k)
    if err:
        sys.stdout.write(
            clip("semsearch: %s; falling back to keyword search" % err) + "\n"
        )
        return cmd_search(records, re.escape(query), as_json)
    if as_json:
        emit_json(hits)
        return 0
    sys.stdout.write(clip("semsearch  k=%d  n=%d" % (k, len(hits))) + "\n")
    _print_hit_rows(hits, "cosine")
    return 0


def cmd_check_new(records, description, as_json):
    qtoks, keyword = _keyword_check_rows(records, description, limit=10)
    semantic, sem_err = _semantic_rank(records, description, k=10, killed_first=True)
    payload = {
        "keyword": keyword,
        "semantic": semantic or [],
        "semantic_note": sem_err,
    }
    if as_json:
        emit_json(payload)
        return 0
    sys.stdout.write(
        clip("check-new  tokens=%d  keyword=%d" % (len(qtoks), len(keyword))) + "\n"
    )
    if not keyword:
        sys.stdout.write("no keyword overlap in mechanism/question/failed_because\n")
    else:
        _print_hit_rows(keyword, "jaccard")
    if sem_err:
        sys.stdout.write(clip("check-new semantic: %s" % sem_err) + "\n")
        return 0
    sys.stdout.write(
        clip("check-new semantic  hits=%d  (KILLED first)" % len(payload["semantic"]))
        + "\n"
    )
    _print_hit_rows(payload["semantic"], "cosine")
    return 0


def build_parser():
    common = argparse.ArgumentParser(add_help=False)
    common.add_argument(
        "--json", action="store_true", help="machine-readable JSON output"
    )
    scope = argparse.ArgumentParser(add_help=False)
    scope.add_argument(
        "--include-drafts",
        action="store_true",
        help="include auto-drafts (default: curated only)",
    )
    scope.add_argument(
        "--curated-only",
        action="store_true",
        default=True,
        help="exclude auto-drafts (default)",
    )
    parser = argparse.ArgumentParser(
        prog="rhcat",
        description="Query the RH semantic catalog (no RH claims).",
        parents=[common],
    )
    sub = parser.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("search", parents=[common], help="regex over all text fields")
    p.add_argument("regex")

    p = sub.add_parser("family", parents=[common], help="records in a family id")
    p.add_argument("id")

    p = sub.add_parser("kind", parents=[common], help="records of a kind id")
    p.add_argument("id")

    p = sub.add_parser("kills", parents=[common, scope], help="KILLED records")
    p.add_argument("--class", dest="kill_class", default=None, metavar="X")

    sub.add_parser("open", parents=[common, scope], help="LOAD_BEARING_OPEN records")

    p = sub.add_parser(
        "reusable", parents=[common, scope], help="records with reusable notes"
    )
    p.add_argument("--family", dest="family_id", default=None, metavar="X")

    p = sub.add_parser("dossier", parents=[common], help="full record + README window")
    p.add_argument("query", help="round id (r645) or path")

    sub.add_parser("stats", parents=[common], help="catalog counts")

    p = sub.add_parser(
        "check-new",
        parents=[common, scope],
        help="keyword + semantic overlap vs prior mechanism/question/failed_because",
    )
    p.add_argument("description")

    p = sub.add_parser(
        "semsearch",
        parents=[common],
        help="cosine search over catalog embeddings (falls back to keyword)",
    )
    p.add_argument("query")
    p.add_argument("--k", type=int, default=10, metavar="N")

    sub.add_parser("todo", parents=[common], help="needs_review / draft records")

    p = sub.add_parser("new", parents=[common], help="curated skeleton from auto-draft")
    p.add_argument("path")
    return parser


def main(argv=None):
    parser = build_parser()
    args = parser.parse_args(argv)
    records = load_catalog()
    as_json = bool(getattr(args, "json", False))
    include_drafts = bool(getattr(args, "include_drafts", False))
    scoped = curated_only(records, include_drafts)
    cmd = args.cmd
    if cmd == "search":
        return cmd_search(records, args.regex, as_json)
    if cmd == "family":
        return cmd_family(records, args.id, as_json)
    if cmd == "kind":
        return cmd_kind(records, args.id, as_json)
    if cmd == "kills":
        return cmd_kills(scoped, args.kill_class, as_json)
    if cmd == "open":
        return cmd_open(scoped, as_json)
    if cmd == "reusable":
        return cmd_reusable(scoped, args.family_id, as_json)
    if cmd == "dossier":
        return cmd_dossier(records, args.query, as_json)
    if cmd == "stats":
        return cmd_stats(records, as_json)
    if cmd == "check-new":
        return cmd_check_new(scoped, args.description, as_json)
    if cmd == "semsearch":
        return cmd_semsearch(records, args.query, max(1, int(args.k)), as_json)
    if cmd == "todo":
        return cmd_todo(records, as_json)
    if cmd == "new":
        return cmd_new(records, args.path, as_json)
    parser.error("unknown command")
    return 2


if __name__ == "__main__":
    sys.exit(main())
