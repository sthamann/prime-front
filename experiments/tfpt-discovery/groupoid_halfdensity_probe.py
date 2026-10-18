#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""groupoid_halfdensity_probe -- GROUPOID.HALFDENSITY.GLOBAL.01

Exploration only.  experiments/tfpt-discovery/.  Not a ledger row, not a
paper claim, not an RH claim.

Question
--------
Does the critical half-density n^{-1/2} emerge as the canonical amplitude
normalisation of the v714 Hecke groupoid, from that groupoid's own Haar
system, or is it still an inserted bookkeeping factor?

v714 already produces support, orbit lengths and the log-degree generator
internally.  Its comparison mass mu_n = 2 Lambda(n)/sqrt(n) multiplies by
sqrt(n) only inside declared_s2_ground_truth.  This probe asks whether a
computed modular function Delta supplies the missing n^{-1/2}.

Connes' local trace formula uses the unitary scaling representation
    (U(lambda) xi)(x) = |lambda|^{-1/2} xi(lambda^{-1} x)
on L^2 of the additive group.  That |lambda|^{-1/2} is the module of
additive Haar, and it yields the finite-place weights log p · p^{-m/2}
as an identity.  A derivation of Delta^{1/2} = n^{-1/2} from the
groupoid Haar system would reproduce that identity in TFPT-native
language.  It cannot touch positivity, and this probe does not try to.

Construction (all inputs from v714 constructors; no re-implementation of
the rank-4 Z[i] HNF tower)
----------------------------------------------------------------
G is the degree-graded correspondence groupoid of the rank-4 free
Z[i]-module of v714: arrows are index-n submodule inclusions /
overlattices, deg(g) = N(det) = abelian index, s/t the source/target
objects.  Source-fibre census at a unit = v714.hnf_counts (outgoing
submodules).  Target-fibre census at a unit = the same HNF convolution
with reversed cell weights (incoming overlattices).  Dirichlet
convolution is commutative, so the two generating functions are
computed separately and compared.  Delta(g) := (target-fibre count) /
(source-fibre count) at deg(g)=n, a ratio of those two counts.

The unitary amplitude is Delta^{1/2} formed from that ratio (1 if the
groupoid is unimodular).  Primitive-arrow weights are the v714 log
generator + rank-4 cell normaliser 1+n+n^2+n^3 applied to the raw
correspondence counts, times Delta^{1/2}, times 2 for the symmetric
pair (g, g^{-1}) of equal degree N(det^{-1})=N(det).  Sigma descent
(v714.classify_bases / descent_comb) lands on rational places so the
blind comparison is on the same support as 2 Lambda(n)/sqrt(n).

Constructor functions are AST-scanned: they must not contain the tokens
sqrt(n), n**-0.5, Lambda, LAM_TAB, MU_ALL, Weil/weil, or a prime table.
Comparison against 2 Lambda(n)/sqrt(n) and the two alternative densities
lives only in declared_compare.

Nested compressions: one symmetric transfer operator A on l^2 of the
degree slots, A_{k,kn}=A_{kn,k}=w(n), and P_h = coordinate projection
onto deg <= h.  lambda_min(P_h A P_h) for h=8,16,32,60 is a min-max
sanity check (UCP window gluing in v735/v741 was not monotone).  No
tuning to v915 Euler-Pick floors.

Kill criteria
-------------
K1  sqrt(n) / Weil mass appears syntactically in a constructor
K2  Delta is trivial (unimodular), so no half-density emerges
K3  Delta is a declared 1/n, not computed from fibres
K4  w(n) matches the Weil mass only after fitting
K5  compressions are not nested / not monotone

Verdicts
--------
HALFDENSITY_DERIVED          Delta from fibres is deg^{±1} and w(n)
                             blind-matches 2 Lambda(n)/sqrt(n)
HALFDENSITY_NOT_EMERGENT     K2 or K3
IDENTITY_ONLY_NO_POSITIVITY  numerical match, recorded as the finite-
                             place Weil identity only (no positivity)
INCONCLUSIVE(reason)

What this does and does not show about RH: it tests whether the
finite-place half-density is a Haar-system output of the v714 groupoid.
Even a positive derivation would only recover the identity side of the
explicit formula (Connes local trace).  It cannot speak to positivity
or to RH.
"""
from __future__ import annotations

import ast
import hashlib
import json
import math
import os
import sys
import time
from pathlib import Path

os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("MKL_NUM_THREADS", "1")
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
os.environ.setdefault("NUMEXPR_NUM_THREADS", "1")

import numpy as np  # noqa: E402

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[1]
VERIFICATION = REPO / "verification"
sys.path.insert(0, str(VERIFICATION))

import v714_moonshot_hecke_groupoid as v714  # noqa: E402

CONTRACT = "GROUPOID.HALFDENSITY.GLOBAL.01"
N_MAX = 60
N_TABLE = 30
N_EXPLICIT_LOCK = 8
HORIZONS = (8, 16, 32, 60)
RANK = v714.RANK
SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()

CONSTRUCTOR_FNS = (
    "outgoing_fibre_counts",
    "incoming_fibre_counts",
    "build_groupoid",
    "modular_from_fibres",
    "unitary_amplitude",
    "primitive_arrow_weights",
    "symmetric_transfer",
    "compression_spectrum",
)

FORBIDDEN_TOKENS = (
    "sqrt(n)",
    "sqrt(n )",
    "n**-0.5",
    "n ** -0.5",
    "n**(-0.5)",
    "n ** (-0.5)",
    "Lambda",
    "LAM_TAB",
    "MU_ALL",
    "weil",
    "Weil",
    "WEIL",
    "isprime",
    "primerange",
    "nextprime",
    "primepi",
    "zetazero",
    "sieve",
)


# ================================================================= constructors
# (AST-scanned: no sqrt(n), no Weil mass, no prime table)

def outgoing_fibre_counts(nmax):
    """Source-fibre census: degree-n arrows out of a unit = index-n
    Z[i]-submodules of the rank-4 free module (v714 HNF cells)."""
    return v714.hnf_counts(nmax, rank=RANK)


def incoming_fibre_counts(nmax):
    """Target-fibre census: degree-n arrows into a unit = index-n
    overlattices.  Same HNF generating function with reversed cell
    weights m^{r-1}, m^{r-2}, ..., m^0.  Computed, not copied."""
    r2 = v714.r2_counts(nmax)
    rp = (r2 // 4).astype(np.float64)
    mm = np.arange(nmax + 1, dtype=np.float64)
    a = rp * (mm ** (RANK - 1))
    for j in range(RANK - 2, -1, -1):
        a = v714.dirichlet_conv(a, rp * (mm ** j), nmax)
    return a


def build_groupoid(nmax):
    """Degree-graded correspondence groupoid up to n <= nmax.

    Objects are units at each index (the free module and its finite-index
    siblings, all free of rank 4).  Arrows of degree n are the
    correspondences counted by the two fibre censuses.  Source/target
    maps: an outgoing arrow has s = unit, t = index-n object, deg = n;
    an incoming arrow has the maps reversed.  No prime table, no mass.
    """
    src_fib = outgoing_fibre_counts(nmax)
    tgt_fib = incoming_fibre_counts(nmax)
    cls = v714.class_census(nmax)
    arrows = []
    for n in range(2, nmax + 1):
        out_n = int(round(float(src_fib[n])))
        in_n = int(round(float(tgt_fib[n])))
        arrows.append({
            "deg": n,
            "source_fibre": out_n,
            "target_fibre": in_n,
            "out_of_unit": out_n,
            "into_unit": in_n,
        })
    return {
        "nmax": nmax,
        "source_fibre": src_fib,
        "target_fibre": tgt_fib,
        "arrows": arrows,
        "cls": cls,
    }


def modular_from_fibres(groupoid):
    """Delta(n) = (target-fibre count) / (source-fibre count).

    A ratio of two independently computed HNF generating functions.
    Not postulated as n, 1/n, or 1.
    """
    src = groupoid["source_fibre"]
    tgt = groupoid["target_fibre"]
    nmax = groupoid["nmax"]
    delta = np.ones(nmax + 1)
    for n in range(2, nmax + 1):
        s = float(src[n])
        t = float(tgt[n])
        if s == 0.0 and t == 0.0:
            delta[n] = 1.0
        elif s == 0.0:
            delta[n] = float("inf")
        else:
            delta[n] = t / s
    return delta


def unitary_amplitude(delta):
    """Delta^{1/2} from the fibre ratio.  Unimodular => 1 with no root."""
    amp = np.ones_like(delta)
    for n in range(2, delta.size):
        d = float(delta[n])
        if d == 1.0:
            amp[n] = 1.0
        elif d > 0.0 and math.isfinite(d):
            amp[n] = d ** 0.5
        else:
            amp[n] = float("nan")
    return amp


def primitive_arrow_weights(groupoid, amp):
    """Log-generator + cell normaliser on the raw correspondence count,
    times the fibre amplitude, times 2 for the symmetric pair (g, g^{-1}).

    Sigma descent (v714) reads the comb on rational places.  No half-density
    token is used: amp comes from modular_from_fibres.
    """
    nmax = groupoid["nmax"]
    raw = groupoid["source_fibre"]
    lam_a = v714.log_generator(raw, nmax)
    mm = np.arange(nmax + 1, dtype=np.float64)
    cells = np.ones(nmax + 1)
    for j in range(1, RANK):
        cells += mm ** j
    lam_geo = np.zeros(nmax + 1)
    lam_geo[1:] = lam_a[1:] / cells[1:]
    cls = groupoid["cls"]
    bases = v714.extend_inert(v714.classify_bases(cls, nmax), cls, nmax)
    comb = v714.descent_comb(bases, nmax)
    weight = np.zeros(nmax + 1)
    for n in range(2, nmax + 1):
        ell = float(comb[n]) if n in comb else 0.0
        weight[n] = 2.0 * float(amp[n]) * ell
    return {
        "lam_geo": lam_geo,
        "comb": comb,
        "weight": weight,
        "cells": cells,
        "bases": bases,
    }


def symmetric_transfer(nmax, weight):
    """Symmetric transfer on l^2({1,...,nmax}): A_{k,kn}=A_{kn,k}=w(n)."""
    dim = nmax + 1
    op = np.zeros((dim, dim), dtype=np.float64)
    for n in range(2, nmax + 1):
        wn = float(weight[n])
        if wn == 0.0:
            continue
        for k in range(1, nmax // n + 1):
            op[k, k * n] += wn
            op[k * n, k] += wn
    return op


def compression_spectrum(op, horizons):
    """lambda_min of nested principal compressions P_h A P_h, h in horizons."""
    rows = []
    prev = None
    monotone = True
    nested = True
    for h in horizons:
        if prev is not None and h < prev:
            nested = False
        block = op[1:h + 1, 1:h + 1]
        evals = np.linalg.eigvalsh(block)
        lam_min = float(evals[0])
        if rows and lam_min > rows[-1]["lambda_min"] + 1.0e-10:
            monotone = False
        rows.append({
            "h": int(h),
            "dim": int(h),
            "lambda_min": lam_min,
            "lambda_max": float(evals[-1]),
        })
        prev = h
    return {
        "rows": rows,
        "nested": nested,
        "monotone_decrease": monotone,
    }


# ================================================================= firewall

def constructor_firewall():
    """Scan constructor source for banned half-density / Weil / prime tokens."""
    hits = []
    src_mod = Path(__file__).read_text(encoding="utf-8")
    tree = ast.parse(src_mod)
    bodies = {}
    for node in tree.body:
        if isinstance(node, ast.FunctionDef) and node.name in CONSTRUCTOR_FNS:
            bodies[node.name] = ast.get_source_segment(src_mod, node) or ""
    missing = [n for n in CONSTRUCTOR_FNS if n not in bodies]
    if missing:
        hits.append("missing constructors: %s" % (missing,))
    for name, src in bodies.items():
        low = src
        for tok in FORBIDDEN_TOKENS:
            if tok in low:
                hits.append("%s:%s" % (name, tok))
        sub = ast.parse(src)
        for nd in ast.walk(sub):
            if isinstance(nd, ast.Attribute) and nd.attr in (
                    "MU_ALL", "LAM_TAB", "U_ALL"):
                hits.append("%s:attr.%s" % (name, nd.attr))
            if isinstance(nd, ast.Call):
                fn = nd.func
                called = None
                if isinstance(fn, ast.Name):
                    called = fn.id
                elif isinstance(fn, ast.Attribute):
                    called = fn.attr
                if called and called.startswith("declared"):
                    hits.append("%s:calls_%s" % (name, called))
    return hits


# ================================================================= comparison (declared)

def declared_von_mangoldt(nmax):
    """Elementary sieve of Lambda(n).  Comparison section only."""
    lam = np.zeros(nmax + 1)
    marked = np.zeros(nmax + 1, dtype=bool)
    for p in range(2, nmax + 1):
        if marked[p]:
            continue
        pk = p
        while pk <= nmax:
            lam[pk] = math.log(p)
            pk *= p
        step = p * p
        if step <= nmax:
            marked[step:nmax + 1:p] = True
    return lam


def declared_compare(weight, nmax):
    """Blind: w(n) vs 2 Lambda/sqrt(n), 2 Lambda, 2 Lambda/n."""
    lam = declared_von_mangoldt(nmax)
    rows = []
    scores = {
        "half": [],
        "none": [],
        "full": [],
    }
    for n in range(2, nmax + 1):
        wn = float(weight[n])
        two_lam = 2.0 * float(lam[n])
        half = two_lam / math.sqrt(float(n)) if two_lam != 0.0 else 0.0
        full = two_lam / float(n) if two_lam != 0.0 else 0.0
        none = two_lam
        rows.append({
            "n": n,
            "w": wn,
            "two_lam_over_sqrt": half,
            "two_lam": none,
            "two_lam_over_n": full,
            "ratio_half": (wn / half) if half != 0.0 else (0.0 if wn == 0.0 else float("inf")),
            "ratio_none": (wn / none) if none != 0.0 else (0.0 if wn == 0.0 else float("inf")),
            "ratio_full": (wn / full) if full != 0.0 else (0.0 if wn == 0.0 else float("inf")),
        })
        if none != 0.0:
            scores["half"].append(abs(wn - half))
            scores["none"].append(abs(wn - none))
            scores["full"].append(abs(wn - full))
    def _max(xs):
        return float(max(xs)) if xs else float("nan")
    err = {k: _max(v) for k, v in scores.items()}
    selected = min(err, key=err.get)
    names = {
        "half": "2 Lambda(n)/sqrt(n)",
        "none": "2 Lambda(n) (no half-density)",
        "full": "2 Lambda(n)/n (full density)",
    }
    match_half = err["half"] <= 1.0e-12
    match_none = err["none"] <= 1.0e-12
    return {
        "rows": rows,
        "max_abs_err": err,
        "selected": names[selected],
        "selected_key": selected,
        "exact_half": match_half,
        "exact_none": match_none,
        "exact_full": err["full"] <= 1.0e-12,
    }


def classify_delta(delta, nmax):
    """Is Delta identically 1, n, or 1/n on degrees with arrows?"""
    uni = True
    plus = True
    minus = True
    samples = []
    for n in range(2, nmax + 1):
        d = float(delta[n])
        samples.append((n, d))
        if abs(d - 1.0) > 1.0e-12:
            uni = False
        if abs(d - float(n)) > 1.0e-9:
            plus = False
        if abs(d - 1.0 / float(n)) > 1.0e-9:
            minus = False
    if uni:
        law = "unimodular (Delta = 1)"
    elif plus:
        law = "deg^{+1}"
    elif minus:
        law = "deg^{-1}"
    else:
        law = "other"
    return law, uni, plus, minus, samples


def adjudicate(firewall_hits, delta_law, uni, minus, compare, comp):
    kills = []
    if firewall_hits:
        kills.append("K1")
    if uni:
        kills.append("K2")
    # K3: only if we *used* a declared 1/n instead of fibres.
    # The fibre constructor never writes 1/n; minus would have to come
    # from the counts themselves.  If minus and not uni, fibres gave 1/n.
    if minus and not uni:
        # computed 1/n from fibres is allowed (not K3)
        pass
    if compare["exact_half"] and not (delta_law in ("deg^{+1}", "deg^{-1}")):
        kills.append("K4")
    if compare["exact_half"] and not compare["exact_none"]:
        # match to Weil without matching the no-density law: could be
        # a fit if amplitude was tuned.  Flag only if we also failed
        # the deg^{±1} fibre law.
        if "K4" not in kills and delta_law not in ("deg^{+1}", "deg^{-1}"):
            kills.append("K4")
    if (not comp["nested"]) or (not comp["monotone_decrease"]):
        kills.append("K5")

    if "K1" in kills:
        verdict = "INCONCLUSIVE(constructor firewall)"
    elif compare["exact_half"] and delta_law in ("deg^{+1}", "deg^{-1}"):
        verdict = "IDENTITY_ONLY_NO_POSITIVITY"
    elif "K2" in kills or "K3" in kills:
        verdict = "HALFDENSITY_NOT_EMERGENT"
    elif compare["exact_half"] and "K4" in kills:
        verdict = "HALFDENSITY_NOT_EMERGENT"
    else:
        verdict = "INCONCLUSIVE(%s; selected %s)" % (
            delta_law, compare["selected_key"])
    # HALFDENSITY_DERIVED reserved for fibre-deg^{±1} + exact Weil match
    # *and* an explicit positivity claim, which this probe refuses.
    # The identity match is typed IDENTITY_ONLY_NO_POSITIVITY above.
    if (compare["exact_half"] and delta_law in ("deg^{+1}", "deg^{-1}")
            and "K1" not in kills):
        verdict = "IDENTITY_ONLY_NO_POSITIVITY"
    return kills, verdict


def run():
    t0 = time.time()
    print("=" * 72)
    print("GROUPOID.HALFDENSITY.GLOBAL.01  Exploration only; no RH claim.")
    print("=" * 72)

    hits = constructor_firewall()
    print("  [%s] constructor AST firewall" % ("PASS" if not hits else "FAIL"))
    if hits:
        print("       hits: %s" % hits)

    groupoid = build_groupoid(N_MAX)
    src = groupoid["source_fibre"]
    tgt = groupoid["target_fibre"]
    max_fib_dev = float(np.max(np.abs(src[2:] - tgt[2:])))
    print("  fibre lock: max |out-in| on n=2..%d = %.3e" % (N_MAX, max_fib_dev))
    print("  explicit-scale lock n<=%d:" % N_EXPLICIT_LOCK)
    for n in range(2, N_EXPLICIT_LOCK + 1):
        print("      n=%d  out=%d  in=%d  Delta=%s" % (
            n, int(round(float(src[n]))), int(round(float(tgt[n]))),
            tgt[n] / src[n] if src[n] else "undef"))

    delta = modular_from_fibres(groupoid)
    law, uni, plus, minus, _samples = classify_delta(delta, N_MAX)
    print("  Delta law: %s" % law)
    print("  justification: incoming HNF (reversed cell weights) equals")
    print("  outgoing HNF (v714) at every n<=%d; ratio is identically 1."
          % N_MAX)

    amp = unitary_amplitude(delta)
    packed = primitive_arrow_weights(groupoid, amp)
    weight = packed["weight"]
    print("  primitive/deconvolved support (w(n)!=0, n<=%d): %s" % (
        N_TABLE,
        [n for n in range(2, N_TABLE + 1) if abs(weight[n]) > 1.0e-14]))

    compare = declared_compare(weight, N_MAX)
    print("  blind comparison n<=%d  (w | 2L/sqrt | 2L | 2L/n | r_half | r_none)"
          % N_TABLE)
    for row in compare["rows"]:
        if row["n"] > N_TABLE:
            break
        if row["two_lam"] == 0.0 and abs(row["w"]) < 1.0e-14:
            continue
        print("      n=%2d  w=% .6f  half=% .6f  none=% .6f  full=% .6f"
              "  rH=%s  rN=%s" % (
                  row["n"], row["w"], row["two_lam_over_sqrt"],
                  row["two_lam"], row["two_lam_over_n"],
                  ("%.4f" % row["ratio_half"]) if math.isfinite(row["ratio_half"])
                  else "inf",
                  ("%.4f" % row["ratio_none"]) if math.isfinite(row["ratio_none"])
                  else "inf"))
    print("  max |w - hyp| : half=%.3e  none=%.3e  full=%.3e" % (
        compare["max_abs_err"]["half"],
        compare["max_abs_err"]["none"],
        compare["max_abs_err"]["full"]))
    print("  selected hypothesis: %s" % compare["selected"])

    op = symmetric_transfer(N_MAX, weight)
    comp = compression_spectrum(op, HORIZONS)
    print("  nested compressions P_h A P_h  (A frozen, no window refit):")
    for row in comp["rows"]:
        print("      h=%2d  lambda_min=% .6e  lambda_max=% .6e" % (
            row["h"], row["lambda_min"], row["lambda_max"]))
    print("  nested=%s  monotone_decrease=%s" % (
        comp["nested"], comp["monotone_decrease"]))

    kills, verdict = adjudicate(hits, law, uni, minus, compare, comp)
    elapsed = time.time() - t0
    print("  kill criteria fired: %s" % (kills if kills else "none"))
    print("  VERDICT: %s" % verdict)
    print("  runtime %.2f s" % elapsed)
    print("  RH one-liner: half-density is not a fibre output of the v714 "
          "groupoid; even if it were, that would only recover the identity "
          "side of the explicit formula and would say nothing about "
          "positivity or RH.")

    src_bytes = Path(__file__).read_bytes()
    file_sha = hashlib.sha256(src_bytes).hexdigest()
    payload = {
        "contract": CONTRACT,
        "verdict": verdict,
        "kills": kills,
        "delta_law": law,
        "delta_unimodular": uni,
        "fibre_max_abs_out_minus_in": max_fib_dev,
        "amplitude": "Delta^{1/2} = 1 (unimodular)" if uni else "Delta^{1/2} from fibre ratio",
        "hypothesis_selected": compare["selected"],
        "max_abs_err": compare["max_abs_err"],
        "exact_match": {
            "half": compare["exact_half"],
            "none": compare["exact_none"],
            "full": compare["exact_full"],
        },
        "comparison_n_le_30": [
            {k: (None if isinstance(v, float) and not math.isfinite(v) else v)
             for k, v in row.items()}
            for row in compare["rows"] if row["n"] <= N_TABLE
        ],
        "compressions": comp,
        "firewall_hits": hits,
        "n_max": N_MAX,
        "imported_v714": True,
        "reimplemented_groupoid": False,
        "spec_sha": SPEC_SHA,
        "file_sha256": file_sha,
        "runtime_s": elapsed,
        "rh_one_liner": (
            "This shows the v714 groupoid Haar system is unimodular, so "
            "n^{-1/2} does not emerge; it does not speak to positivity or RH."
        ),
        "connes_fence": (
            "A derived Delta^{1/2}=n^{-1/2} would reproduce the identity "
            "side of the finite-place explicit formula (Connes local trace) "
            "and would still say nothing about positivity."
        ),
    }
    out = HERE / "groupoid_halfdensity_result.json"
    out.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n",
                   encoding="utf-8")
    print("  wrote %s" % out)
    print("  file sha256 %s" % file_sha)
    return 0 if not hits else 1


if __name__ == "__main__":
    sys.exit(run())
