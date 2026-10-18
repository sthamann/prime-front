#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""three_gap_mask_probe -- LEMMA.THREE_GAP_MASK.01 (round 395):
THE THREE-GAP STRUCTURE OF THE FOLD MASK, occupation regularity
as a theorem after r393/r394 named the last two analytic rests
as hanging on nu-occupation (not F1, not checkerboard, not
equidistribution).

Coexistence: r393 proved F1 necessary not sufficient (random F1
jump 1.18 OUT; periodic 1100/1010/110 IN).  r394 proved
checkerboard is a coin (0.504) and scramble holds the sign map
while dying on occupation.  Both rests named the SAME missing
object: source occupation regularity of the nu-mask on the
cosine grid, between periodic and random.  The candidate was
Steinhaus three-gap of the folded log(p^k) sequence.

THE FROZEN QUESTION.  Does every canonical nu-mask have
blockwise <= B distinct gap lengths (B small, 3-5) with
source-defined values and drift control, and does THAT
property (not F1 alone) imply the d2 log tau box and upgrade
the Assist census to a class statement?

LEGS (lemma-first; exits PROVED / REFUTED / REDUZIERT):
  A  Measure the mask.  Exact nu-gap spectra in grid steps on
     core-42 + EXT-sample + chi: nuniq per dyadic block, values,
     drift.  Compare periodic (1-2 gaps), random F1 (many),
     two-period (1 gap, rho_AP=1).  Does 3/8-floor or MED-CAP
     8/3 follow from the gap spectrum?
  B  Structure SATZ.  Steinhaus for {n alpha}; local three-gap
     of integer-log (PNT-free, f'' of log) with drift census
     for small n.  Honest: which blocks need finite census.
  C  Mask => box.  Numeric then theorem-attempt: F1 +
     rho_AP<1/5 + blockwise <=B-gap => box?  Discriminator:
     {n alpha} masks vs random-F1 vs random F1-legal <=3-gap
     concatenations (wrapping).  If random 3-gap is IN, three-
     gap is the missing lemma; if OUT, more is missing.
  D  Assist + kills.  lambda_max on synthetic 3-gap vs random
     F1; two-period dies on non-periodicity; random F1 on the
     gap spectrum; scramble on both; dyadic-cut mutants.

CALIBRATION DISCLOSURE.  w9 / core-42 / EXT-sample / chi gap
spectra, Steinhaus checks, integer-log local nuniq, wrapping
3-gap vs {n alpha} vs random-F1 last-12, and Assist lambda at
n0 on h=40 synthetics were first measured in /tmp (r395_cal.py,
r395_cal2.py, r395_cal3.py, r395_cal4.py) on the same
constructors, 2026-08-28.  Frozen floors/ceilings below are
that measurement, sealed as gates.  No two-commit pre-blind
freeze: pins disclosed.  Builder fallback: core-42 + EXT kz97
(cheap) + chi sample; MAIN-85 and EXT windows with S>5000
skipped (kz69 window_data ~77 s).

FROZEN FROM /tmp (live re-gated, not fitted):
  * Steinhaus on Z: multiples of p mod q, N=1..q, nuniq<=3 on
    every tested Farey pair (Fibonacci and 1..30 coprime).
    Float {k alpha} nuniq<=3 on 35/36 (phi N=400 is a rounding
    artefact, not a counterexample).
  * Integer-log local 3-gap (PNT-free): n0>=512, M<=64, L=800
    circular nuniq<=3.  Small n (n0<=64) nuniq 4..19 -- drift
    census, not a SATZ.  n0=128 M=8 already <=3.
  * w9: S=367 n_nu=104 nuniq=12 (NOT 3), gap1 count=2 (= the
    two F1 pairs), dmin/dmed=1/3 < 3/8, dmax/dmin=23 > 8/3.
    slide12 <=3 frac=0.45, <=5 frac=0.74.  Dyadic L=4: <=3
    in 7/9, <=5 in 9/9.  Pre-fold circle nuniq=12 identical
    histogram.  3/8-floor and MED-CAP 8/3 do NOT follow from
    the cosine-grid gap spectrum (they live on the r361
    log-sieve block packing, a different object).
  * Core-42: nuniq in [8,18] med 13; 0/42 <=3, 0/42 <=5,
    2/42 <=8.  slide12<=3 in [0.31,0.60] med 0.45;
    slide12<=5 in [0.64,0.92] med 0.78.  gap1 count (pairs)
    in [0,16] med 4.  dmin/dmed in [1/3, 1].
  * EXT kz97 S=2429 nuniq=13 slide12<=3=0.41; kz96 nuniq=20;
    kz69 nuniq=25 (GROWS with S -- no bounded B).
  * chi3/chi4 sample nuniq 10..15, slide12<=3 0.21..0.62.
  * Scramble seed=3: nuniq=15, slide12<=3 = 0.00.
  * Discriminator h=40: tiles 1010/1100/110 IN; random F1
    nuniq=5 j=7.03 OUT; wrapping (1,2,3) seed=7 j=2.33 OUT;
    wrapping (2,3,4) 4/20 IN.  h=80: random F1 j=1.179 OUT
    (r393 reproduced); {n alpha} F1-legal 8/8 IN among the
    hyp-passing alphas; wrapping (2,3,4) 12/12 IN;
    wrapping (1,2,3) 2/12 IN -- random 3-gap with F1-pairs
    is NOT the box.  Mechanical phi h=80 d=0.1016 OUT on
    the box (j=0.329 IN at JUMP).
  * Assist h=40 n0=16: random F1 lam=2.01>1; wrapping
    (2,3,4) lam=0.997<1; 1010 lam=1.405>1; two-period
    c=2/3 lam22=1.0288>1 (r387/r394 reproduced).

AUSGANG REFUTED (the Drei-Gap-Maske lemma as stated).
SATZ: Steinhaus three-gap of {k alpha} on Z/q (rational) and
on the tested irrationals; PNT-free integer-log local three-
gap for n>=512.  REFUTED: the nu-mask of a canonical window
is globally or blockwise 3-gap (core nuniq 8-18, grows on
EXT); nuniq<=3 + F1 + rho_AP<1/5 implies the d2 log tau box
(random wrapping (1,2,3) OUT; mechanical phi OUT on the box).
3/8-floor and MED-CAP 8/3 are NOT shadows of the cosine-grid
gap spectrum.  Remaining: the 2-3-dominated histogram with a
sparse large-gap tail (prime-power thinning of the log
skeleton) -- still the occupation object of both F_eps and
Assist, now named strictly smaller than three-gap.  No RH
claim.

MACHINERY: r226 hirota_sign.window_data, r390 full_grid /
mu_gams, r392 match_indices / last12, r387 two_period /
make_B, r283 admissible_indices, r382 chi_mz.

NO RH CLAIM.  Finite identities, a named refutation, named
kills.  Research documentation, not a theorem of RH.
"""
from __future__ import annotations

import argparse
import ast
import hashlib
import math
import os
import sys
import time

import numpy as np

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DISC = os.path.dirname(os.path.abspath(__file__))
PROB = os.path.join(REPO, "rh", "problem")
for p in (DISC, PROB):
    if p not in sys.path:
        sys.path.insert(0, p)

import deletion_transform_probe as D  # noqa: E402
import g_eps_mu_probe as P  # noqa: E402
import hirota_sign_probe as HS  # noqa: E402
import port_integrable_kernel_probe as PIK  # noqa: E402
import verify_lstar_instance as V  # noqa: E402
import coherence_assist_probe as CA  # noqa: E402

BOX = 1.0 / 16.0
JUMP = 2.0 / 5.0
JUMP_RELAX = 0.45
THREE_EIGHTHS = 3.0 / 8.0
MEDCAP = 8.0 / 3.0
SCR_SEED = 3
CORE_N = 42
PHI = (math.sqrt(5.0) - 1.0) / 2.0

# disclosed /tmp pins
W9_NUNIQ = 12
W9_GAP1 = 2
W9_DMIN, W9_DMED, W9_DMAX = 1, 3, 23
W9_SL12_3 = (0.35, 0.55)
W9_SL12_5 = (0.65, 0.85)
W9_DY4_LE5 = 9
CORE_NUNIQ = (8, 18)
CORE_SL3 = (0.30, 0.65)
CORE_SL5 = (0.60, 0.95)
LOG_N0_STAR = 512
RAND_F1_J_FLOOR = 0.50
NALPHA_J_BAR = 0.40
KGAP123_J_FLOOR = 0.80
ASSIST_RAND_FLOOR = 1.50
ASSIST_234_CEIL = 1.05
SCR_SL3_BAR = 0.05
EXT97_NUNIQ_FLOOR = 10

SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
CHECKS = []
T0 = time.time()


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok)))
    print("  [%s] %-44s %s" % ("PASS" if ok else "FAIL", name, detail),
          flush=True)
    return bool(ok)


def section(t):
    print("\n" + "=" * 78)
    print(t)
    print("=" * 78, flush=True)


def firewall_audit():
    src = open(os.path.abspath(__file__), "r", encoding="utf-8").read()
    tree = ast.parse(src)
    forb = {"zeta" + "zero", "n" + "zeros", "prime" + "range",
            "is" + "prime", "gram" + "point"}
    bad = []
    for node in ast.walk(tree):
        nm = node.attr if isinstance(node, ast.Attribute) else (
            node.id if isinstance(node, ast.Name) else None)
        if nm and nm.lower() in forb:
            bad.append("%s@%d" % (nm, node.lineno))
    return (not bad), ("NO zero/prime oracles; window_data / "
                       "full_grid / log-monotone only"
                       if not bad else "; ".join(bad))


def last12(g):
    return D.last12(g)


def in_box(g, jump=JUMP):
    d, j = last12(g)
    return d <= BOX + 1e-12 and j <= jump + 1e-12, d, j


def gaps_of(idx, circular=False, modulus=None):
    g = np.sort(np.asarray(idx, int))
    if len(g) < 2:
        return np.array([], dtype=int)
    d = np.diff(g)
    if circular:
        mod = int(modulus if modulus is not None else int(g[-1]) + 1)
        d = np.concatenate([d, [mod - int(g[-1]) + int(g[0])]])
    return d


def spectrum(d):
    if len(d) == 0:
        return dict(nuniq=0, uniq=(), counts=(), dmin=0, dmed=0, dmax=0,
                    ratio=0.0, steinhaus=True)
    u, c = np.unique(d, return_counts=True)
    dmin = int(np.min(d))
    dmed = int(np.median(d))
    dmax = int(np.max(d))
    stein = True
    if len(u) == 3:
        stein = int(u[0]) + int(u[1]) == int(u[2])
    elif len(u) > 3:
        stein = False
    return dict(nuniq=int(len(u)),
                uniq=tuple(int(x) for x in u),
                counts=tuple(int(x) for x in c),
                dmin=dmin, dmed=dmed, dmax=dmax,
                ratio=dmin / max(dmed, 1), steinhaus=stein)


def sliding_nuniq(idx, win=12):
    g = np.sort(np.asarray(idx, int))
    if len(g) < win + 1:
        return []
    out = []
    step = max(1, win // 4)
    for i in range(0, len(g) - win, step):
        out.append(len(np.unique(np.diff(g[i:i + win + 1]))))
    return out


def dyadic_nuniq(idx, S, level=4, min_pts=6, offset=0):
    g = np.sort(np.asarray(idx, int))
    B = 1 << level
    width = S / B
    nu = []
    for b in range(B):
        lo = int(round(b * width + offset)) % S
        hi = int(round((b + 1) * width + offset))
        if offset == 0:
            sub = g[(g >= int(round(b * width)))
                    & (g < int(round((b + 1) * width)))]
        else:
            # wrap-aware slice
            lo = int(round(b * width + offset))
            hi = int(round((b + 1) * width + offset))
            sub = g[((g - offset) % S >= int(round(b * width)))
                    & ((g - offset) % S < int(round((b + 1) * width)))]
        if len(sub) < min_pts:
            continue
        nu.append(spectrum(gaps_of(sub, False))["nuniq"])
    return nu


def f1_of(m):
    run = mx = 0
    for v in np.asarray(m, bool).tolist():
        run = run + 1 if v else 0
        mx = max(mx, run)
    return mx <= 2, mx


def rho_ap_simple(m):
    idx = np.where(m)[0]
    n = len(idx)
    if n < 3:
        return 1.0
    best = 2
    for i in range(n):
        for j in range(i + 1, min(i + 6, n)):
            delta = int(idx[j] - idx[i])
            if delta <= 0:
                continue
            cnt = 2
            expect = int(idx[j]) + delta
            k = j + 1
            while k < n:
                if int(idx[k]) == expect:
                    cnt += 1
                    expect += delta
                elif int(idx[k]) > expect:
                    break
                k += 1
            if cnt > best:
                best = cnt
    return best / n


def occ_fejer(xf, wf, m_nu, nref):
    keep = ~m_nu
    n = min(int(keep.sum()) - 2, nref)
    g = P.mu_gams(xf[keep], wf[keep], n)
    ok, d, j = in_box(g)
    return ok, d, j


def wrap_kgap(S, gapset, seed=7):
    rng = np.random.default_rng(seed)
    gaps = list(gapset)
    others = [x for x in gaps if x != 1] or gaps
    seq = []
    covered = 0
    last_one = False
    while covered < S - max(gaps):
        g = int(rng.choice(gaps))
        if g == 1 and last_one:
            g = int(rng.choice(others))
        seq.append(g)
        covered += g
        last_one = (g == 1)
    rest = S - covered
    if rest >= 1:
        seq.append(int(rest))
    m = np.zeros(S, dtype=bool)
    pos = 0
    for g in seq:
        if pos < S:
            m[pos] = True
        pos += g
    return m


def nalpha_mask(S, alpha, fill=0.45):
    m = np.zeros(S, dtype=bool)
    target = int(round(fill * S))
    seen = set()
    k = 1
    while len(seen) < target and k < 40 * S:
        j = int(math.floor(S * ((k * alpha) % 1.0))) % S
        seen.add(j)
        m[j] = True
        k += 1
    return m


def random_f1_mask(S, fill=0.45, seed=2):
    rng = np.random.default_rng(seed)
    m = np.zeros(S, dtype=bool)
    target = int(round(fill * S))
    i = nnu = 0
    while i < S and nnu < target:
        if rng.random() < 0.35:
            i += 1
            continue
        if rng.random() < 0.45 or i + 1 >= S or nnu + 2 > target:
            m[i] = True
            nnu += 1
            i += 2
        else:
            m[i] = m[i + 1] = True
            nnu += 2
            i += 3
    return m


def mask_idx(kz, scramble_seed=None):
    d = HS.window_data(kz, scramble_seed=scramble_seed)
    N = int(d["n_max"])
    xf, wff = P.full_grid(N)
    idx = np.asarray(D.match_indices(xf, d["ys"]), int)
    return d, N, xf, wff, idx


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def steinhaus_rational(p, q, N):
    """Exact three-gap of the first N multiples of p on Z/q."""
    pts = sorted({(k * p) % q for k in range(N)})
    if len(pts) < 2:
        return True, 0
    d = [pts[i + 1] - pts[i] for i in range(len(pts) - 1)]
    d.append(q - pts[-1] + pts[0])
    return len(set(d)) <= 3, len(set(d))


def log_block_nuniq(n0, M, Lgrid=800):
    pts = np.unique([int(Lgrid * (math.log(n) / math.log(2.0) % 1.0)) % Lgrid
                     for n in range(n0, n0 + M)])
    if len(pts) < 4:
        return 0
    return spectrum(gaps_of(pts, True, Lgrid))["nuniq"]


def mz_from_mask(xf, wf, m):
    return dict(xp=xf[~m], wp=wf[~m], yn=xf[m], vn=wf[m],
                Nw=(len(xf) + 1) // 2, S=len(xf))


def lam_at(mz, k):
    B = CA.make_B(mz, k)
    G = B @ B.T if B.shape[0] <= B.shape[1] else B.T @ B
    return float(np.linalg.eigvalsh(G)[-1])


def part_a_steinhaus():
    section("S1  LEG B -- STEINHAUS THREE-GAP (CLASSICAL, PNT-FREE)")
    n_bad = 0
    n_tot = 0
    # Fibonacci convergents (exact)
    fib = [1, 1]
    while fib[-1] < 500:
        fib.append(fib[-1] + fib[-2])
    for i in range(3, len(fib) - 1):
        p, q = fib[i], fib[i + 1]
        g = gcd(p, q)
        p, q = p // g, q // g
        for N in (q // 2, q, max(3, q - 1)):
            ok, nu = steinhaus_rational(p, q, N)
            n_tot += 1
            if not ok:
                n_bad += 1
    # all coprime p/q with q<=30
    for q in range(3, 31):
        for p in range(1, q):
            if gcd(p, q) != 1:
                continue
            ok, nu = steinhaus_rational(p, q, q)
            n_tot += 1
            if not ok:
                n_bad += 1
    check("G01-Steinhaus-rational-exact",
          n_bad == 0 and n_tot > 50,
          "nuniq<=3 on %d/%d Farey+Fibonacci (Z/q exact)" % (n_tot, n_tot))

    # additive law on a witnessed 3-gap (phi, N between Fibonaccis)
    a = PHI
    found = None
    for Nadd in range(4, 30):
        pts = np.sort(np.array([((k * a) % 1.0) for k in range(1, Nadd + 1)]))
        dd = np.diff(pts)
        dd = np.concatenate([dd, [pts[0] + 1.0 - pts[-1]]])
        u = np.unique(np.round(dd, 8))
        if len(u) == 3 and abs(u[0] + u[1] - u[2]) < 1e-7:
            found = (Nadd, tuple(float(x) for x in u))
            break
    check("G02-Steinhaus-additive-a+b=c",
          found is not None,
          "phi N=%s uniq~%s a+b=c (float 1e-7)" % (
              found[0], tuple("%.4f" % x for x in found[1]))
          if found else "none")

    # thinning kills three-gap: a subset of a 3-gap set need not be 3-gap
    q = 89
    p = 55
    pts = sorted({(k * p) % q for k in range(40)})
    rng = np.random.default_rng(395)
    sub = sorted(rng.choice(pts, size=20, replace=False).tolist())
    dd = [sub[i + 1] - sub[i] for i in range(len(sub) - 1)]
    dd.append(q - sub[-1] + sub[0])
    n_sub = len(set(dd))
    check("G03-thinning-kills-three-gap",
          n_sub > 3,
          "40-pt Steinhaus subset of 20 has nuniq=%d>3 "
          "(prime-thinning is NOT three-gap-preserving)" % n_sub)


def part_b_log_local():
    section("S2  LEG B -- INTEGER-LOG LOCAL THREE-GAP (PNT-FREE)")
    n_big_bad = 0
    n_big = 0
    for n0 in (512, 1024, 2048):
        for M in (8, 16, 32, 64):
            nu = log_block_nuniq(n0, M)
            n_big += 1
            if nu > 3:
                n_big_bad += 1
    check("G10-log-local-large-n-three-gap",
          n_big_bad == 0 and n_big == 12,
          "n0>=512 M<=64: nuniq<=3 on %d/%d (PNT-free, f''~1/n^2)"
          % (n_big - n_big_bad, n_big))

    small = []
    for n0 in (4, 8, 16, 32, 64):
        small.append(log_block_nuniq(n0, 32))
    check("G11-log-small-n-census",
          min(small) >= 4,
          "n0=4..64 M=32 nuniq=%s -- FAST DRIFT, finite census not SATZ"
          % (small,))

    n128 = log_block_nuniq(128, 8)
    check("G12-log-onset",
          n128 <= 3,
          "n0=128 M=8 nuniq=%d (onset of the local SATZ)" % n128)


def part_c_source_mask():
    section("S3  LEG A -- SOURCE MASK GAP SPECTRUM (w9)")
    d9, N9, xf9, wf9, idx9 = mask_idx(9)
    S9 = len(xf9)
    sp = spectrum(gaps_of(idx9, False))
    g1 = sp["counts"][sp["uniq"].index(1)] if 1 in sp["uniq"] else 0
    check("G20-w9-not-three-gap",
          sp["nuniq"] == W9_NUNIQ and g1 == W9_GAP1
          and sp["dmin"] == W9_DMIN and sp["dmed"] == W9_DMED
          and sp["dmax"] == W9_DMAX,
          "nuniq=%d gap1=%d dmin/dmed/dmax=%d/%d/%d n_nu=%d S=%d"
          % (sp["nuniq"], g1, sp["dmin"], sp["dmed"], sp["dmax"],
             len(idx9), S9))

    sl = sliding_nuniq(idx9, 12)
    f3 = float(np.mean([x <= 3 for x in sl]))
    f5 = float(np.mean([x <= 5 for x in sl]))
    check("G21-w9-local-partial-three-gap",
          W9_SL12_3[0] < f3 < W9_SL12_3[1]
          and W9_SL12_5[0] < f5 < W9_SL12_5[1],
          "slide12 <=3=%.2f <=5=%.2f (PARTIAL, not a block SATZ)"
          % (f3, f5))

    dy4 = dyadic_nuniq(idx9, S9, level=4)
    check("G22-w9-dyadic-L4",
          len(dy4) >= 8 and max(dy4) <= 5
          and sum(x <= 3 for x in dy4) >= 5,
          "L=4 nuniq=%s <=5 %d/%d <=3 %d/%d"
          % (dy4, sum(x <= 5 for x in dy4), len(dy4),
             sum(x <= 3 for x in dy4), len(dy4)))

    check("G23-three-eighths-not-from-mask",
          sp["ratio"] < THREE_EIGHTHS - 1e-12,
          "dmin/dmed=%.3f < 3/8=0.375 (r361 floor is NOT a mask shadow)"
          % sp["ratio"])
    check("G24-MEDCAP-not-from-mask",
          sp["dmax"] / max(sp["dmin"], 1) > MEDCAP + 1.0,
          "dmax/dmin=%.1f > 8/3 (MED-CAP is the log-sieve packing, "
          "not cosine-grid gaps)" % (sp["dmax"] / max(sp["dmin"], 1)))

    b9 = PIK.build_rung(9)
    jj = np.arange(b9["L"])[b9["d"] < 0]
    spc = spectrum(gaps_of(jj, True, b9["L"]))
    check("G25-prefold-same-nuniq",
          spc["nuniq"] == W9_NUNIQ,
          "pre-fold circle nuniq=%d (= post-fold mask)" % spc["nuniq"])
    return idx9, S9, xf9, wf9


def part_d_discriminator(smoke):
    section("S4  LEG C -- IMPLICATION DISCRIMINATOR")
    xf40, wf40 = P.full_grid(40)
    S40 = len(xf40)
    m1010 = np.array([i % 2 == 0 for i in range(S40)], bool)
    m1100 = np.array([i % 4 < 2 for i in range(S40)], bool)
    ok10, d10, j10 = occ_fejer(xf40, wf40, m1010, 40)
    ok11, d11, j11 = occ_fejer(xf40, wf40, m1100, 40)
    sp10 = spectrum(gaps_of(np.where(m1010)[0], False))
    sp11 = spectrum(gaps_of(np.where(m1100)[0], False))
    check("G30-periodic-tiles-IN",
          ok10 and ok11 and sp10["nuniq"] == 1 and sp11["nuniq"] == 2,
          "1010 nuniq=%d IN j=%.4f; 1100 nuniq=%d IN j=%.4f"
          % (sp10["nuniq"], j10, sp11["nuniq"], j11))

    mR = random_f1_mask(S40, 0.45, 2)
    okR, dR, jR = occ_fejer(xf40, wf40, mR, 40)
    spR = spectrum(gaps_of(np.where(mR)[0], False))
    f1R, mxR = f1_of(mR)
    check("G31-random-F1-many-gaps-OUT",
          f1R and spR["nuniq"] >= 5 and (not okR) and jR > RAND_F1_J_FLOOR,
          "F1 nuniq=%d j=%.4f OUT (F1 not sufficient, r393)"
          % (spR["nuniq"], jR))

    m123 = wrap_kgap(S40, (1, 2, 3), 7)
    ok123, d123, j123 = occ_fejer(xf40, wf40, m123, 40)
    sp123 = spectrum(gaps_of(np.where(m123)[0], True, S40))
    f1123, _ = f1_of(m123)
    rap123 = rho_ap_simple(m123)
    check("G32-random-3gap-123-OUT",
          f1123 and sp123["nuniq"] <= 3 and (not ok123)
          and j123 > KGAP123_J_FLOOR,
          "wrap(1,2,3) nuniq=%d F1=%s rho_AP=%.3f j=%.4f OUT -- "
          "three-gap is NOT the missing lemma"
          % (sp123["nuniq"], f1123, rap123, j123))

    rap10 = rho_ap_simple(m1010)
    check("G33-two-period-is-global-AP",
          rap10 > 0.99 and sp10["nuniq"] == 1,
          "1010 rho_AP=%.3f nuniq=1 (non-periodicity is the other clause)"
          % rap10)

    if smoke:
        return

    xf80, wf80 = P.full_grid(80)
    S80 = len(xf80)
    mR80 = random_f1_mask(S80, 0.45, 2)
    ok80, d80, j80 = occ_fejer(xf80, wf80, mR80, 60)
    check("G34-random-F1-h80-OUT",
          (not ok80) and j80 > RAND_F1_J_FLOOR,
          "h=80 random F1 j=%.4f OUT (r393 pin)" % j80)

    mphi = nalpha_mask(S80, math.sqrt(2.0) - 1.0, 0.45)
    okphi, dphi, jphi = occ_fejer(xf80, wf80, mphi, 60)
    f1phi, mxphi = f1_of(mphi)
    rapphi = rho_ap_simple(mphi)
    check("G35-nalpha-F1-h80-IN",
          f1phi and rapphi < 0.20 and okphi and jphi < NALPHA_J_BAR,
          "nalpha sqrt2-1 F1 rho_AP=%.3f IN j=%.4f d=%.4f "
          "(Steinhaus POINT-SET at large S can sit in the box)"
          % (rapphi, jphi, dphi))

    n_in234 = n_in123 = 0
    n_seed = 8
    for seed in range(n_seed):
        ok2, _, _ = occ_fejer(xf80, wf80, wrap_kgap(S80, (2, 3, 4), seed), 60)
        ok1, _, _ = occ_fejer(xf80, wf80, wrap_kgap(S80, (1, 2, 3), seed), 60)
        n_in234 += int(ok2)
        n_in123 += int(ok1)
    check("G36-wrap-234-vs-123-h80",
          n_in234 >= 6 and n_in123 <= 4,
          "wrap(2,3,4) IN %d/%d; wrap(1,2,3) IN %d/%d -- "
          "isolated-single 3-gap IN, F1-pair 3-gap OUT"
          % (n_in234, n_seed, n_in123, n_seed))


def part_e_kills(idx9, S9, smoke):
    section("S5  LEG D -- ASSIST + KILLS")
    _ds, _Ns, _xfs, _ws, idxs = mask_idx(9, scramble_seed=SCR_SEED)
    sps = spectrum(gaps_of(idxs, False))
    sls = sliding_nuniq(idxs, 12)
    f3s = float(np.mean([x <= 3 for x in sls])) if sls else 1.0
    check("G40-scramble-kills-local-three-gap",
          sps["nuniq"] >= 12 and f3s < SCR_SL3_BAR,
          "seed=3 nuniq=%d slide12<=3=%.2f (occupation break)"
          % (sps["nuniq"], f3s))

    mz23 = CA.two_period(81, 2.0 / 3.0)
    lam22 = lam_at(mz23, 22)
    check("G41-two-period-assist-OUT",
          lam22 > 1.0,
          "c=2/3 lam22=%.4f>1 (rho_AP=1 kill, r387/r394)" % lam22)

    xf40, wf40 = P.full_grid(40)
    S40 = len(xf40)
    mR = random_f1_mask(S40, 0.45, 2)
    m234 = wrap_kgap(S40, (2, 3, 4), 7)
    m1010 = np.array([i % 2 == 0 for i in range(S40)], bool)
    n0 = int(2 * ((S40 + 1) // 2) / 5)
    lamR = lam_at(mz_from_mask(xf40, wf40, mR), n0)
    lam234 = lam_at(mz_from_mask(xf40, wf40, m234), n0)
    lamAP = lam_at(mz_from_mask(xf40, wf40, m1010), n0)
    check("G42-assist-spectrum-separates",
          lamR > ASSIST_RAND_FLOOR and lam234 < ASSIST_234_CEIL
          and lamAP > 1.0,
          "lam_n0 randF1=%.3f wrap234=%.3f 1010=%.3f "
          "(sparse 3-gap near 1, random F1 and AP >1)"
          % (lamR, lam234, lamAP))

    # dyadic-cut mutant: offset the L=4 partition
    dy0 = dyadic_nuniq(idx9, S9, level=4, offset=0)
    dy1 = dyadic_nuniq(idx9, S9, level=4, offset=S9 // 32)
    check("G43-block-boundary-mutant",
          max(dy0) >= 4 and dy0 != dy1,
          "L=4 nuniq offset0=%s offset S/32=%s "
          "(canonical cut already not 3-gap; the count MOVES with the cut)"
          % (dy0, dy1))

    if smoke:
        return


def part_f_census():
    section("S6  FULL CENSUS -- core-42 + chi + EXT-kz97")
    core = list(V.admissible_indices())
    check("G50-ladder-size", len(core) == CORE_N, "core %d" % len(core))
    nu_c, f3s, f5s = [], [], []
    for i, kz in enumerate(core):
        _d, N, xf, _w, idx = mask_idx(kz)
        sp = spectrum(gaps_of(idx, False))
        sl = sliding_nuniq(idx, 12)
        nu_c.append(sp["nuniq"])
        f3s.append(float(np.mean([x <= 3 for x in sl])) if sl else 0.0)
        f5s.append(float(np.mean([x <= 5 for x in sl])) if sl else 0.0)
        if (i + 1) % 14 == 0:
            print("    ... %d/42 t=%.1f" % (i + 1, time.time() - T0),
                  flush=True)
    check("G51-core42-global-nuniq-grows",
          min(nu_c) >= CORE_NUNIQ[0] and max(nu_c) <= CORE_NUNIQ[1]
          and sum(x <= 5 for x in nu_c) == 0,
          "nuniq [%d, %d] med=%.1f; <=5: 0/%d -- NOT a bounded-B SATZ"
          % (min(nu_c), max(nu_c), float(np.median(nu_c)), CORE_N))
    check("G52-core42-local-partial",
          CORE_SL3[0] <= min(f3s) and max(f3s) <= CORE_SL3[1]
          and CORE_SL5[0] <= min(f5s) and max(f5s) <= CORE_SL5[1],
          "slide12<=3 [%.2f, %.2f] <=5 [%.2f, %.2f]"
          % (min(f3s), max(f3s), min(f5s), max(f5s)))

    import pivot_entry_lemma_probe as PE  # noqa: E402
    import dirichlet_matched_frame_probe as DMF  # noqa: E402
    chi_nu = []
    for kz, q in ((15, DMF.Q_CHI3), (19, DMF.Q_CHI3), (23, DMF.Q_CHI3),
                  (20, DMF.Q_CHI4)):
        mz = PE.chi_mz(kz, q)
        N = int(mz["Nw"])
        xf, _ = P.full_grid(N)
        idx = np.asarray(D.match_indices(xf, mz["yn"]), int)
        chi_nu.append(spectrum(gaps_of(idx, False))["nuniq"])
    check("G53-chi-not-three-gap",
          min(chi_nu) >= 8 and max(chi_nu) <= 18,
          "chi nuniq=%s" % chi_nu)

    _d, N, xf, _w, idx = mask_idx(97)
    sp97 = spectrum(gaps_of(idx, False))
    check("G54-EXT-kz97-nuniq-grows",
          sp97["nuniq"] >= EXT97_NUNIQ_FLOOR,
          "kz97 S=%d nuniq=%d (bounded-B FAILS at EXT scale)"
          % (len(xf), sp97["nuniq"]))


def main():
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke

    print("=" * 78)
    print("three_gap_mask_probe -- LEMMA.THREE_GAP_MASK.01 (round 395)")
    print("SPEC_SHA %s" % SPEC_SHA[:16])
    print("mode: %s" % ("SMOKE" if smoke else "FULL"))
    print("=" * 78)

    section("S0  FIREWALL")
    okf, det = firewall_audit()
    check("G00-firewall", okf, det)

    part_a_steinhaus()
    part_b_log_local()
    idx9, S9, xf9, wf9 = part_c_source_mask()
    part_d_discriminator(smoke)
    part_e_kills(idx9, S9, smoke)
    if not smoke:
        part_f_census()

    n_fail = sum(1 for _n, ok in CHECKS if not ok)
    n_ok = len(CHECKS) - n_fail
    print("\nRESULT: %d/%d gates PASS%s   SPEC_SHA %s   (%.1fs)"
          % (n_ok, len(CHECKS),
             "" if n_fail == 0 else "  ** FAIL **",
             SPEC_SHA[:16], time.time() - T0))
    tag = ("THREE GAP MASK LEMMA SMOKE" if smoke else "THREE GAP MASK LEMMA")
    if n_fail == 0:
        print(tag + " VERIFIED")
        return 0
    print(tag + " FAILED %d" % n_fail)
    return 1


if __name__ == "__main__":
    sys.exit(main())
