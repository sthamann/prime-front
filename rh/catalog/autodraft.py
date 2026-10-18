#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Heuristic DRAFT records for uncurated RH-related paths.

Writes rh/catalog/fragments/auto_drafts.json (regenerated each run).
Never overwrites curated fragments/part_*.json. stdlib only. NO RH CLAIM.
"""

from __future__ import annotations

import glob
import json
import os
import re
import sys

CATALOG_DIR = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(CATALOG_DIR, "..", ".."))
INVENTORY_PATH = os.path.join(REPO, "rh", "INVENTORY.json")
TAXONOMY_PATH = os.path.join(CATALOG_DIR, "taxonomy.json")
FRAGMENTS_DIR = os.path.join(CATALOG_DIR, "fragments")
OUT_DRAFTS = os.path.join(FRAGMENTS_DIR, "auto_drafts.json")

HEAD_BYTES = 80000
ROUND_RE = re.compile(r"\br(\d{3})\b", re.I)
LEDGER_RE = re.compile(r"\b[A-Z]+(?:\.[A-Z0-9-]+)+\.\d{2}\b")
VERDICT_LINE_RE = re.compile(
    r"VERDICT|Verdict|Decision|\bKILLED\b|\bCERTIFIED\b|\bPROVED\b|"
    r"\bINCONCLUSIVE\b|\bSEALED\b|\bGO\b|\bSTOP\b|\bMEASURED\b"
)
OUTCOME_RANK = (
    "KILLED",
    "CERTIFIED",
    "PROVED",
    "INCONCLUSIVE",
    "SEALED",
    "MEASURED",
    "OPEN",
)
SKIP_DIRS = {".git", "__pycache__", ".lake", "lake-packages", "build"}

# Word-boundary RH context on the first 120 lines (working-tree filter).
RH_CONTEXT_RE = re.compile(
    r"\b(?:Riemann|RH\b|zeta|Weil|Gabor|Mellin|explicit formula|von Mangoldt|"
    r"prime comb|Selberg|Hilbert[- ]P[oó]lya|Xi\b|Ξ|critical line|Toeplitz|"
    r"Jensen polynomial|Lee[- ]Yang|de Bruijn|Bernstein|Pick function|screw|"
    r"subordination|L\*|adel|Bost|Connes|scaling site|Hecke|Kneser|Epstein|"
    r"Laguerre|Hurwitz)\b",
    re.I,
)
CONTRACT_RE = re.compile(r"(?:PRIME|WEIL|MELLIN|GEOM|RH|CAS|QGEO|E8)\.")
TAU_GUARD_RE = re.compile(
    r"(?:iiks|toda|riemann[-–]hilbert|painlev).{0,40}\btau\b|"
    r"\btau\b.{0,40}(?:iiks|toda|riemann[-–]hilbert|painlev)",
    re.I,
)

_PATTERN_CACHE = {}


def load_json(path):
    with open(path, "r", encoding="utf-8") as fh:
        return json.load(fh)


def clip_words(text, limit):
    words = (text or "").split()
    return " ".join(words[:limit])


def curated_paths():
    found = set()
    if not os.path.isdir(FRAGMENTS_DIR):
        return found
    for fpath in glob.glob(os.path.join(FRAGMENTS_DIR, "part_*.json")):
        try:
            payload = load_json(fpath)
        except (OSError, json.JSONDecodeError):
            continue
        if not isinstance(payload, list):
            continue
        for item in payload:
            if isinstance(item, dict) and item.get("path"):
                found.add(item["path"])
    return found


def working_tree_paths():
    out = []
    disc = os.path.join(REPO, "experiments", "tfpt-discovery")
    if os.path.isdir(disc):
        for name in sorted(os.listdir(disc)):
            if name.endswith("_probe.py") or name.endswith("_result.json"):
                out.append("experiments/tfpt-discovery/" + name)
    rh_root = os.path.join(REPO, "rh")
    for root, dirs, files in os.walk(rh_root):
        dirs[:] = sorted(d for d in dirs if d not in SKIP_DIRS)
        for name in sorted(files):
            if name.endswith((".py", ".tex", ".lean")):
                full = os.path.join(root, name)
                out.append(os.path.relpath(full, REPO).replace(os.sep, "/"))
    return out


def read_head(rel, limit=HEAD_BYTES):
    path = os.path.join(REPO, rel)
    if not os.path.isfile(path):
        return ""
    try:
        with open(path, "r", encoding="utf-8", errors="replace") as fh:
            return fh.read(limit)
    except OSError:
        return ""


def first_n_lines(text, n=120):
    if not text:
        return ""
    lines = text.splitlines()
    return "\n".join(lines[:n])


def _is_disclaimer_rh(head120, match):
    """'RH' in the firewall line 'NO RH CLAIM' is not RH-context evidence."""
    if match.group(0).upper() != "RH":
        return False
    window = head120[max(0, match.start() - 8) : match.end() + 16]
    return re.search(r"no\s+rh\s+claim", window, re.I) is not None


def evidence_from_text(head120):
    pos = 0
    while True:
        match = RH_CONTEXT_RE.search(head120, pos)
        if not match:
            break
        if _is_disclaimer_rh(head120, match):
            pos = match.end()
            continue
        return match.group(0)
    match = CONTRACT_RE.search(head120)
    if match:
        return match.group(0)
    return None


def rh_related_evidence(rel, head120, sibling_cache):
    if rel.startswith("rh/"):
        return "path:rh/"
    if rel.endswith("_result.json"):
        sib = rel[: -len("_result.json")] + "_probe.py"
        if sib in sibling_cache:
            return sibling_cache[sib]
        sib_head = first_n_lines(read_head(sib))
        ev = rh_related_evidence(sib, sib_head, sibling_cache)
        sibling_cache[sib] = ev
        return ev
    return evidence_from_text(head120)


def first_docstring(text, rel):
    if rel.endswith(".py"):
        match = re.search(r'(?:"""|\'\'\')([\s\S]*?)(?:"""|\'\'\')', text)
        if match:
            return " ".join(match.group(1).split())
    if rel.endswith(".lean"):
        match = re.search(r"/\-([\s\S]*?)\-/", text)
        if match:
            return " ".join(match.group(1).split())
    if rel.endswith(".tex"):
        comments = [
            line.lstrip("%").strip()
            for line in text.splitlines()
            if line.lstrip().startswith("%") and line.lstrip("%").strip()
        ]
        if comments:
            return " ".join(comments[:3])
    return ""


def sentences(blob):
    parts = re.split(r"(?<=[.!?])\s+", blob.strip()) if blob else []
    return [p.strip() for p in parts if p.strip()]


def keyword_regex(word):
    cached = _PATTERN_CACHE.get(word)
    if cached is not None:
        return cached
    low = word.lower()
    if low == "tau":
        _PATTERN_CACHE[word] = TAU_GUARD_RE
        return TAU_GUARD_RE
    escaped = re.escape(low)
    prefix = r"\b" if re.match(r"^[a-z0-9]", low) else ""
    suffix = r"\b" if re.search(r"[a-z0-9]$", low) else ""
    compiled = re.compile(prefix + escaped + suffix, re.I)
    _PATTERN_CACHE[word] = compiled
    return compiled


def score_table(haystack, table):
    scores = {}
    for enum_id, words in (table or {}).items():
        total = 0
        for word in words:
            if word:
                total += len(keyword_regex(word).findall(haystack))
        if total:
            scores[enum_id] = total
    return scores


def pick_enum(scores, default):
    if not scores:
        return default, []
    ranked = sorted(scores.items(), key=lambda kv: (-kv[1], kv[0]))
    winner = ranked[0][0]
    secondary = [k for k, _ in ranked[1:] if k != "OTHER"]
    return winner, secondary


def infer_kind(rel, scores):
    low = rel.lower()
    if low.endswith(".lean"):
        return "FORMALIZATION"
    if "audit" in low or "chuk" in low:
        return "EXTERNAL_AUDIT"
    if low.endswith("_result.json"):
        return "CERTIFICATE"
    if low.endswith("_probe.py") or "/tfpt-discovery/" in low:
        return "ATTACK"
    if low.endswith(".tex") or "readme" in low:
        return "DOCUMENTATION"
    if "catalog" in low or "hook" in low:
        return "TOOLING"
    kind, _ = pick_enum(scores, "OTHER")
    return kind


def infer_role(rel, inv_entry):
    if inv_entry and inv_entry.get("role"):
        return inv_entry["role"]
    if rel.endswith(".lean"):
        return "lean_module"
    if rel.endswith(".tex"):
        return "paper"
    if rel.endswith("_result.json"):
        return "probe_result"
    if rel.endswith("_probe.py"):
        return "working_probe"
    if rel.startswith("verification/"):
        return "verification_module"
    return "working_tree"


def infer_outcome(lines):
    blob = "\n".join(lines)
    mapped = blob.replace("STOP", "KILLED").replace("GO", "CERTIFIED")
    for token in OUTCOME_RANK:
        if re.search(r"\b%s\b" % token, mapped):
            return token
    if re.search(r"\bMEASURED\b", blob):
        return "MEASURED"
    return "OPEN"


def infer_failure(outcome, text, table):
    if outcome != "KILLED":
        return "NOT_APPLICABLE", ""
    parens = re.findall(r"\(([^)]{0,200})\)", text)
    blob = " ".join(parens).lower() + " " + text[:4000].lower()
    scores = score_table(blob, table)
    klass, _ = pick_enum(scores, "NOT_APPLICABLE")
    reason = clip_words(parens[0] if parens else "", 40)
    return klass, reason


def infer_relevance(family, kind):
    if family == "SIEVE_FACTORING_GEOMETRY":
        return "UNRELATED"
    if family == "EXPLICIT_FORMULA_IDENTITY":
        return "IDENTITY_SIDE"
    if family in ("CERTIFICATE_INFRASTRUCTURE", "LEAN_FORMALIZATION") or kind in (
        "TOOLING",
        "DOCUMENTATION",
    ):
        return "INFRASTRUCTURE"
    if kind == "EXTERNAL_AUDIT" or family == "EXTERNAL_ADJUDICATION":
        return "INFRASTRUCTURE"
    return "FINITE_FRAGMENT"


def artifacts_for(rel):
    arts = {
        "probe": None,
        "result_json": None,
        "tex": None,
        "lean": [],
        "figures": [],
    }
    if rel.endswith("_probe.py") or (
        rel.endswith(".py") and "tfpt-discovery" in rel
    ):
        arts["probe"] = rel
    if rel.endswith("_result.json"):
        arts["result_json"] = rel
        stem = rel[: -len("_result.json")] + "_probe.py"
        if os.path.isfile(os.path.join(REPO, stem)):
            arts["probe"] = stem
    if rel.endswith(".tex"):
        arts["tex"] = rel
    if rel.endswith(".lean"):
        arts["lean"] = [rel]
    return arts


def draft_record(rel, inv_entry, text, taxonomy, evidence):
    keys = taxonomy.get("keywords") or {}
    hay = (rel + "\n" + text[:12000]).lower()
    fam_scores = score_table(hay, keys.get("families"))
    kind_scores = score_table(hay, keys.get("kinds"))
    family, secondary = pick_enum(fam_scores, "OTHER")
    kind = infer_kind(rel, kind_scores)

    rounds = ["r" + m.group(1) for m in ROUND_RE.finditer(text + " " + rel)]
    if inv_entry and inv_entry.get("round"):
        round_s = inv_entry["round"]
    elif rounds:
        uniq = sorted(set(rounds), key=lambda x: int(x[1:]))
        round_s = uniq[0] if len(uniq) == 1 else "%s-%s" % (uniq[0], uniq[-1])
    else:
        round_s = ""

    ledgers = list(dict.fromkeys(LEDGER_RE.findall(text)))
    if inv_entry and inv_entry.get("ledger_ids"):
        ledgers = list(inv_entry["ledger_ids"])

    v_lines = [ln.strip() for ln in text.splitlines() if VERDICT_LINE_RE.search(ln)]
    v_lines = v_lines[:8]
    outcome = infer_outcome(v_lines)
    verdict = " | ".join(clip_words(ln, 20) for ln in v_lines)

    docs = sentences(first_docstring(text, rel))
    question = clip_words(docs[0] if docs else "", 30)
    mechanism = clip_words(docs[1] if len(docs) > 1 else (docs[0] if docs else ""), 30)

    fail_class, fail_because = infer_failure(
        outcome, text, keys.get("failure_classes")
    )
    rec = {
        "path": rel,
        "round": round_s,
        "role": infer_role(rel, inv_entry),
        "ledger_ids": ledgers,
        "status_raw": (inv_entry or {}).get("status") or (v_lines[0] if v_lines else ""),
        "kind": kind,
        "family": family,
        "family_secondary": secondary[:4],
        "question": question,
        "mechanism": mechanism,
        "result_verdict": verdict,
        "outcome": outcome,
        "solved": "",
        "failed_because": fail_because,
        "failure_class": fail_class,
        "rh_relevance": infer_relevance(family, kind),
        "artifacts": artifacts_for(rel),
        "reusable": "",
        "depends_on": sorted(set(rounds), key=lambda x: int(x[1:]))[:8],
        "readme_lines": "",
        "confidence": "low",
        "needs_review": True,
        "draft": True,
        "rh_related_evidence": evidence or "",
    }
    if inv_entry and inv_entry.get("sha256"):
        rec["inventory_sha256"] = inv_entry["sha256"]
    return rec


def main(argv=None):
    quiet = "--quiet" in (argv or sys.argv[1:])
    if not os.path.isfile(INVENTORY_PATH):
        sys.stderr.write("FATAL: missing %s\n" % INVENTORY_PATH)
        return 1
    inventory = load_json(INVENTORY_PATH)
    taxonomy = load_json(TAXONOMY_PATH)
    by_inv = {
        e["path"]: e
        for e in (inventory.get("entries") or [])
        if isinstance(e, dict) and e.get("path")
    }
    already = curated_paths()
    candidates = []
    for path in list(by_inv) + working_tree_paths():
        if path not in already and path not in candidates:
            candidates.append(path)

    sibling_cache = {}
    drafts = []
    excluded = 0
    for rel in candidates:
        text = read_head(rel)
        head120 = first_n_lines(text)
        if rel in by_inv:
            evidence = "inventory"
        else:
            evidence = rh_related_evidence(rel, head120, sibling_cache)
        if not evidence:
            excluded += 1
            continue
        drafts.append(draft_record(rel, by_inv.get(rel), text, taxonomy, evidence))

    drafts.sort(key=lambda r: (r.get("round") or "", r.get("path") or ""))
    os.makedirs(FRAGMENTS_DIR, exist_ok=True)
    with open(OUT_DRAFTS, "w", encoding="utf-8") as fh:
        json.dump(drafts, fh, indent=2, sort_keys=True, ensure_ascii=False)
        fh.write("\n")
    if not quiet:
        sys.stdout.write(
            "autodraft: %d drafts, %d excluded, %d curated skipped -> %s\n"
            % (
                len(drafts),
                excluded,
                len(already),
                os.path.relpath(OUT_DRAFTS, REPO),
            )
        )
    return 0


if __name__ == "__main__":
    sys.exit(main())
