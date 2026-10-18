#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""isolation_lemma_probe -- LEMMA.ISOLATION.01 (round 396):
ISOLATION OF THE FOLD MASK, pair density as a theorem after
r395 named the occupation rest as a 2-3 histogram with a
sparse tail and two F1 pairs on FRAME-A (not three-gap).

Coexistence: r395 refuted blockwise three-gap (w9 nuniq=12;
wrap(1,2,3) OUT; wrap(2,3,4) isolated-singles 8/8 IN at h=80
nref=60).  The discriminator trace: wrap(2,3,4) lambda=0.997
even when random, wrap(1,2,3) with gap-1 pairs 1/8 IN, random
F1 pair-rich OUT, source 2 pairs / 104 atoms (w9).

THE FROZEN QUESTION.  (1) Is the pair density of the nu-mask
source-countably small -- gap-1 pairs only where two log(n)
collide on the fold/grid, with P(N)/n_nu -> 0 or P <= a fixed
constant, PNT-free from log-density?  (2) Do isolated masks
(all gaps >= 2) with a thin large-gap tail satisfy the d2 log
tau box AND lambda_max < 1, so the finitely many 2x2 pair
blocks are an explicit remainder and the singleton chain is a
SATZ?  (3) Does isolation plus the Dirichlet hull
|D_n| <= 1/|sin(a/2)| close Gershgorin where r394 died
(gA=13.32)?

LEGS (lemma-first; exits PROVED / REFUTED / REDUZIERT):
  A  Count pairs on core-42 + EXT-kz97 + chi; map (n,n') on
     w9; PNT-free packing of consecutive log-atoms vs folded
     consecutive integers.
  B  Class discriminator: wrap(2,3,4) family vs nref; inject
     0/1/2/5/10 pairs; fat-tail isolated; denser wrap(2,2,3).
  C  Singleton chain / Assist: lambda and Gershgorin on
     isolated vs 1010 vs injected pairs vs source; Dirichlet
     envelope at sep 2.
  D  Kills: wrap(1,2,3) on pair density; random F1 on density
     + tail; two-period on rho_AP; scramble; pair-counter
     mutant (gap-2 != gap-1); tail x2.

CALIBRATION DISCLOSURE.  w9 / core-42 / EXT-kz97 / chi pair
counts, atom-fold provenance, wrap(2,3,4) nref-60 vs nref-h,
pair injection, fat-tail, Assist/Gershgorin were first
measured in /tmp (r396_cal.py, r396_cal2.py) on the same
constructors, 2026-08-28.  Frozen floors/ceilings below are
that measurement, sealed as gates.  No two-commit pre-blind
freeze: pins disclosed.  Builder fallback: core-42 + EXT kz97
+ chi sample (MAIN-85 and EXT S>5000 skipped).

FROZEN FROM /tmp (live re-gated, not fitted):
  * w9: 2 pairs / 104 atoms, dens=0.0192, locs (13,14),(67,68).
    Atom-fold hits: n=exp(u)=211 on a pair bin (near the cap
    X=256), n=97 at dist 2 -- NOT small prime powers.  Folded
    consecutive integers n=2..64: 0 adjacent on L=734.
    Atom-fold adjacencies=18, same-bin=9, vs 2 cosine pairs
    (aggregation).  Consecutive atoms with du<2D: 24/69 --
    PNT-free packing is O(n_atom), not o(n_nu).
  * Core-42: pairs in [0,16] med 4; dens in [0, 0.0405] med
    0.017; 3/42 zero-pair (kz 12,13,32, all IN).  42/42 IN at
    JUMP.  corr(pairs, jump)=-0.38 (pairs do NOT drive the
    source jump; max-pair kz=52 has 16 pairs and j=0.099).
  * EXT kz97: 22 pairs / 795, dens=0.0277 (grows in count,
    density stays O(0.03), not -> 0 and not a fixed constant).
  * chi: (15,19,23,20) pairs 4,6,0,4 dens 0.040/0.039/0/0.041.
  * wrap(2,3,4) isolated (pairs=0, maxrun=1) F1.  h=40 nref=40:
    3/12 IN (NOT uniform).  h=80 nref=60: 8/8 IN (r395 pin,
    truncation census).  h=80 nref=80: 2/8 IN.  The 8/8 is an
    nref artefact, not a class SATZ of isolation.
  * wrap(2,2,3) denser isolated: 0/8 IN.  wrap(3,4,5) sparser:
    5/8 IN.  Fill, not isolation, moves the box.
  * Inject k pairs into wrap234 h=40: k=0 -> 1/8 IN; k=1 ->
    0/8; k=10 -> 0/8 j up to 3.86.  Threshold is not '2 like
    the source' -- even 0 pairs is not enough on this class.
  * Fat tail (punch dmax=60): 6/8 IN vs thin isolated ~1/8.
    Fat tail HELPS.  Source dmax/dmin=23 is not the kill.
  * Assist h=40 n0=16: wrap234 lam=0.9968<1 gersh=1.768>1
    gA=6.10; inj2 lam=1.020; wrap123 lam=1.858; randF1 2.010;
    1010 isolated lam=1.405>1.  Isolation does not imply
    lambda<1 (1010) and does not close Gershgorin.  Dirichlet
    1/sin(Delta theta) at sep 2 is 12.6 on S=79, still >>1.
  * two-period lam22=1.0288>1; scramble seed=3 pairs=44/102
    dens=0.431 OUT j=0.563.

AUSGANG REFUTED (the Isolation lemma as stated).
SATZ: folded consecutive small integers are not adjacent
(PNT-free, log monotone); wrap(2,3,4) is isolated; pair
counts on named windows are machine identities; Dirichlet
envelope at sep 2 is still >>1.  REFUTED: P(N)/n_nu -> 0 or
P <= constant (core max 16, kz97=22, dens O(0.03) stable);
pairs come from small-n log collisions (they come from large
n near the cap, after fold); isolated + thin tail => box
(h=40 3/12 IN; nref=h kills the r395 8/8; denser isolated
0/8; fat tail helps); isolated => lambda<1 (1010); isolation
+ hull => Gershgorin<1 (gersh=1.77); singleton 1x1 chain is a
SATZ of the box (the isolated class does not sit in the box
at natural depth).  Remaining: the r395 2-3 histogram with a
sparse tail -- pair density ~2% is a SHADOW of that shape,
not a closing lemma.  No RH claim.

MACHINERY: r226 hirota_sign.window_data, r390 full_grid /
mu_gams, r392 match_indices / last12, r387 two_period /
make_B, r283 admissible_indices, r382 chi_mz, r395 wrap_kgap.

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

import three_gap_mask_probe as T  # noqa: E402
import g_eps_mu_probe as P  # noqa: E402
import port_integrable_kernel_probe as PIK  # noqa: E402
import coherence_assist_probe as CA  # noqa: E402
import verify_lstar_instance as V  # noqa: E402

BOX = T.BOX
JUMP = T.JUMP
SCR_SEED = 3
CORE_N = 42
W9_PAIRS = 2
W9_NNU = 104
CORE_PAIRS = (0, 16)
CORE_ZERO = 3
CORE_DENS_MAX = 0.045
EXT97_PAIRS_FLOOR = 18
EXT97_DENS = (0.015, 0.040)
WRAP40_IN_BAR = 5
ASSIST_234_CEIL = 1.05
GERSH_FLOOR = 1.20
GA_FLOOR = 3.0
INJ10_J_FLOOR = 0.50
SCR_DENS_FLOOR = 0.30
PACK_CLOSE_FLOOR = 20
ATOM_ADJ_FLOOR = 10

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


def n_pairs_of(idx):
    g = np.sort(np.asarray(idx, int))
    if len(g) < 2:
        return 0, []
    locs = np.where(np.diff(g) == 1)[0]
    pairs = [(int(g[i]), int(g[i + 1])) for i in locs]
    return len(pairs), pairs


def inject_k_pairs(m, k, seed=396):
    m = np.asarray(m, bool).copy()
    S = len(m)
    rng = np.random.default_rng(seed)
    placed = 0
    for _ in range(2000):
        if placed >= k:
            break
        occ = np.where(m)[0]
        cands = []
        for i in occ:
            if i + 1 >= S or m[i + 1]:
                continue
            if i > 0 and m[i - 1]:
                continue
            if i + 2 < S and m[i + 2]:
                continue
            cands.append(int(i))
        if not cands:
            break
        i = int(rng.choice(cands))
        m[i + 1] = True
        placed += 1
    return m, placed


def fattail_isolated(S, dmax, seed=396, gapset=(2, 3, 4)):
    m = T.wrap_kgap(S, gapset, seed)
    idx = np.where(m)[0]
    if len(idx) < 8:
        return m
    mid = len(idx) // 2
    lo = int(idx[mid])
    hi = min(S - 1, lo + int(dmax) - 1)
    m[lo + 1:hi] = False
    m[lo] = True
    if hi < S:
        m[hi] = True
    return m


def gersh_at(mz, k):
    B = CA.make_B(mz, k)
    E = B @ B.T
    diag = np.diag(E)
    off = np.abs(E).copy()
    np.fill_diagonal(off, 0.0)
    gersh = float(np.max(diag + off.sum(axis=1)))
    gA = float(np.max(off.sum(axis=1) / np.maximum(diag, 1e-30)))
    lam = float(np.linalg.eigvalsh(E)[-1]) if E.shape[0] else 0.0
    return lam, gersh, gA


def folded_consec_adj(n_lo, n_hi, Lgrid):
    adj = 0
    prev = None
    for n in range(n_lo, n_hi):
        x = int(Lgrid * (math.log(n) / math.log(2.0) % 1.0)) % Lgrid
        f = min(x, Lgrid - x)
        if prev is not None and abs(f - prev) == 1:
            adj += 1
        prev = f
    return adj


def atom_fold_stats(kz=9):
    import v563_paper2_readouts as core  # noqa: E402
    rr = core.build_window(kz)
    uu = np.asarray(rr["uu"], float)
    Dmesh = float(rr["D"])
    M = int(rr["M"])
    folds = []
    ns = []
    for u in uu:
        i0 = int(math.floor(u / Dmesh))
        i0 = max(0, min(M - 1, i0))
        folds.append(min(i0, M - i0))
        ns.append(math.exp(u))
    folds = np.array(folds)
    af = np.sort(folds)
    n_adj = int(np.sum(np.diff(af) == 1)) if len(af) > 1 else 0
    du = np.diff(np.sort(uu))
    n_close = int(np.sum(du < 2.0 * Dmesh)) if len(du) else 0
    return dict(uu=uu, D=Dmesh, M=M, folds=folds, ns=ns,
                n_adj=n_adj, n_close=n_close, n_atom=len(uu),
                L=int(PIK.build_rung(kz)["L"]))


def part_a_pairs():
    section("S1  LEG A -- PAIR CENSUS AND PNT-FREE PACKING")
    _d, N, xf, _w, idx = T.mask_idx(9)
    npair, locs = n_pairs_of(idx)
    dens = npair / max(len(idx), 1)
    check("G01-w9-pairs-two",
          npair == W9_PAIRS and len(idx) == W9_NNU
          and locs == [(13, 14), (67, 68)],
          "w9 pairs=%d/%d dens=%.4f locs=%s" % (npair, len(idx), dens, locs))

    st = atom_fold_stats(9)
    adj_small = folded_consec_adj(2, 64, st["L"])
    check("G02-small-n-folded-not-adjacent",
          adj_small == 0,
          "folded consec n=2..64 adj=%d on L=%d (PNT-free, not "
          "the small-prime mechanism)" % (adj_small, st["L"]))

    pair_bins = [13, 14, 67, 68]
    hit_cap = any(abs(f - b) == 0 and n > 50
                  for n, f in zip(st["ns"], st["folds"])
                  for b in pair_bins)
    check("G03-pairs-are-large-n-fold",
          hit_cap,
          "an atom n=exp(u)>50 lands on a pair bin (cap-scale, "
          "not n < e^{1/delta} small-n collisions)")

    check("G04-packing-not-o-natom",
          st["n_close"] >= PACK_CLOSE_FLOOR,
          "consec atoms du<2D: %d/%d -- PNT-free packing is "
          "O(n_atom), not P/n_nu -> 0" % (st["n_close"], st["n_atom"] - 1))
    check("G05-atom-fold-adj-gt-cosine-pairs",
          st["n_adj"] >= ATOM_ADJ_FLOOR and st["n_adj"] > W9_PAIRS,
          "atom-fold adj=%d vs cosine pairs=%d (aggregation, "
          "not a Steinhaus remainder)" % (st["n_adj"], W9_PAIRS))
    return xf, idx, N


def part_b_class(smoke):
    section("S2  LEG B -- ISOLATED CLASS IS NOT THE BOX")
    xf40, wf40 = P.full_grid(40)
    S40 = len(xf40)
    m234 = T.wrap_kgap(S40, (2, 3, 4), 7)
    f1, mx = T.f1_of(m234)
    np234, _ = n_pairs_of(np.where(m234)[0])
    check("G10-wrap234-is-isolated",
          f1 and mx <= 1 and np234 == 0,
          "F1 maxrun=%d pairs=%d fill=%.3f" % (mx, np234, float(m234.mean())))

    n_in = 0
    js = []
    for seed in range(12):
        ok, _d, j = T.occ_fejer(xf40, wf40, T.wrap_kgap(S40, (2, 3, 4), seed),
                                40)
        n_in += int(ok)
        js.append(j)
    check("G11-wrap234-h40-not-uniform-IN",
          n_in <= WRAP40_IN_BAR and n_in < 12,
          "h=40 nref=40 IN %d/12 j[%.4f,%.4f] -- isolation is "
          "NOT a class SATZ of the box" % (n_in, min(js), max(js)))

    n1 = n10 = 0
    j10s = []
    for seed in range(8):
        m0 = T.wrap_kgap(S40, (2, 3, 4), seed)
        m1, _p = inject_k_pairs(m0, 1, seed=396 + seed)
        m10, _p2 = inject_k_pairs(m0, 10, seed=396 + seed)
        ok1, _, _ = T.occ_fejer(xf40, wf40, m1, 40)
        ok10, _, j10 = T.occ_fejer(xf40, wf40, m10, 40)
        n1 += int(ok1)
        n10 += int(ok10)
        j10s.append(j10)
    check("G14-pair-injection-no-source-threshold",
          n1 <= 2 and n10 == 0 and max(j10s) > INJ10_J_FLOOR,
          "inject k=1 IN %d/8; k=10 IN %d/8 jmax=%.3f -- the "
          "source's 2 pairs is NOT a closing threshold"
          % (n1, n10, max(j10s)))

    m123 = T.wrap_kgap(S40, (1, 2, 3), 7)
    np123, nnu123 = n_pairs_of(np.where(m123)[0])[0], int(m123.sum())
    ok123, _, j123 = T.occ_fejer(xf40, wf40, m123, 40)
    check("G15-wrap123-dies-on-pair-density",
          (not ok123) and np123 / max(nnu123, 1) > 0.15 and j123 > 0.80,
          "wrap(1,2,3) pairs=%d/%d dens=%.3f j=%.4f OUT"
          % (np123, nnu123, np123 / max(nnu123, 1), j123))

    mR = T.random_f1_mask(S40, 0.45, 2)
    npR, nnuR = n_pairs_of(np.where(mR)[0])[0], int(mR.sum())
    okR, _, jR = T.occ_fejer(xf40, wf40, mR, 40)
    check("G16-randF1-dies-on-pairs",
          (not okR) and npR / max(nnuR, 1) > 0.30 and jR > 0.50,
          "randF1 pairs=%d/%d dens=%.3f j=%.4f OUT"
          % (npR, nnuR, npR / max(nnuR, 1), jR))

    m1010 = np.array([i % 2 == 0 for i in range(S40)], bool)
    np10, _ = n_pairs_of(np.where(m1010)[0])
    ok10, _, j10 = T.occ_fejer(xf40, wf40, m1010, 40)
    check("G17-1010-isolated-but-AP",
          np10 == 0 and ok10 and T.rho_ap_simple(m1010) > 0.99,
          "1010 pairs=0 IN j=%.4f rho_AP=%.3f (isolation without "
          "non-periodicity is the two-period class)" % (
              j10, T.rho_ap_simple(m1010)))

    n_fat = n_thin = 0
    for seed in range(8):
        okf, _, _ = T.occ_fejer(
            xf40, wf40, fattail_isolated(S40, 60, seed), 40)
        okt, _, _ = T.occ_fejer(
            xf40, wf40, T.wrap_kgap(S40, (2, 3, 4), seed), 40)
        n_fat += int(okf)
        n_thin += int(okt)
    check("G18-fat-tail-helps-not-kills",
          n_fat >= n_thin and n_fat >= 4,
          "fattail dmax=60 IN %d/8 vs wrap234 %d/8 -- thin tail "
          "is the WRONG clause" % (n_fat, n_thin))

    n223 = 0
    for seed in range(8):
        ok, _, _ = T.occ_fejer(xf40, wf40, T.wrap_kgap(S40, (2, 2, 3), seed),
                               40)
        n223 += int(ok)
    check("G31-denser-isolated-OUT",
          n223 == 0,
          "wrap(2,2,3) IN %d/8 -- denser isolated half-filling "
          "kills the box (fill, not pairs)" % n223)

    if smoke:
        return xf40, wf40, S40, m234, m123, mR, m1010

    xf80, wf80 = P.full_grid(80)
    n60 = n80 = 0
    for seed in range(8):
        m = T.wrap_kgap(len(xf80), (2, 3, 4), seed)
        ok60, _, _ = T.occ_fejer(xf80, wf80, m, 60)
        ok80, _, _ = T.occ_fejer(xf80, wf80, m, 80)
        n60 += int(ok60)
        n80 += int(ok80)
    check("G12-h80-nref60-truncation-census",
          n60 == 8,
          "h=80 nref=60 wrap234 IN %d/8 (r395 pin; NOT a SATZ)" % n60)
    check("G13-h80-nref-h-not-uniform",
          n80 <= 4,
          "h=80 nref=80 wrap234 IN %d/8 -- the 8/8 dies at "
          "natural depth" % n80)
    return xf40, wf40, S40, m234, m123, mR, m1010


def part_c_assist(xf40, wf40, S40, m234, m123, mR, m1010):
    section("S3  LEG C -- ASSIST: ISOLATION DOES NOT CLOSE GERSHGORIN")
    n0 = int(2 * ((S40 + 1) // 2) / 5)
    lam234, g234, gA234 = gersh_at(T.mz_from_mask(xf40, wf40, m234), n0)
    check("G20-wrap234-lam-near-one",
          lam234 < ASSIST_234_CEIL,
          "wrap234 lam=%.4f < %.2f at n0=%d (census, not SATZ)"
          % (lam234, ASSIST_234_CEIL, n0))
    check("G21-gershgorin-still-open",
          g234 > GERSH_FLOOR and gA234 > GA_FLOOR,
          "gersh=%.3f gA=%.3f -- isolation + Dirichlet hull "
          "does NOT close Gershgorin (r394 rest survives)"
          % (g234, gA234))

    lam10 = T.lam_at(T.mz_from_mask(xf40, wf40, m1010), n0)
    check("G22-1010-isolated-lam-gt-one",
          lam10 > 1.0,
          "1010 isolated lam=%.4f>1 (isolation =/> lambda<1)"
          % lam10)

    m2, _ = inject_k_pairs(m234, 2, 396)
    lam2 = T.lam_at(T.mz_from_mask(xf40, wf40, m2), n0)
    check("G23-two-injected-pairs-lam-gt-one",
          lam2 > 1.0,
          "wrap234+2pairs lam=%.4f>1 (source-typical pair count "
          "already leaves lambda<1 on this class)" % lam2)

    mz23 = CA.two_period(81, 2.0 / 3.0)
    lam22 = T.lam_at(mz23, 22)
    check("G24-two-period-rhoAP",
          lam22 > 1.0,
          "c=2/3 lam22=%.4f>1 (rho_AP kill, unchanged r387/r394)"
          % lam22)

    dth = 2.0 * math.pi / S40
    env2 = 1.0 / abs(math.sin(dth))
    check("G25-dirichlet-hull-still-huge",
          env2 > 5.0,
          "1/sin(Delta theta)=%.2f at sep 2 on S=%d >>1 "
          "(hull bound does not become useful under isolation)"
          % (env2, S40))
    return n0


def part_d_kills():
    section("S4  LEG D -- NAMED KILLS")
    _ds, _Ns, _xfs, _ws, idxs = T.mask_idx(9, scramble_seed=SCR_SEED)
    nps, _ = n_pairs_of(idxs)
    denss = nps / max(len(idxs), 1)
    check("G30-scramble-pair-density",
          denss > SCR_DENS_FLOOR,
          "scramble seed=3 pairs=%d/%d dens=%.3f (occupation "
          "break, pair-rich)" % (nps, len(idxs), denss))

    _d, _N, _xf, _w, idx9 = T.mask_idx(9)
    g9 = np.sort(idx9)
    g1 = int(np.sum(np.diff(g9) == 1))
    g2 = int(np.sum(np.diff(g9) == 2))
    check("G32-pair-counter-mutant",
          g2 != g1 and g2 > g1,
          "w9 gap-1=%d gap-2=%d -- counting gap-2 as pairs is "
          "a different (false) counter" % (g1, g2))


def part_e_census():
    section("S5  FULL CENSUS -- core-42 + chi + EXT-kz97")
    core = list(V.admissible_indices())
    check("G50-ladder-size", len(core) == CORE_N, "core %d" % len(core))
    pc, dens, js, oks = [], [], [], []
    for i, kz in enumerate(core):
        _d, N, xf, wf, idx = T.mask_idx(kz)
        npair, _ = n_pairs_of(idx)
        m = np.zeros(len(xf), bool)
        m[idx] = True
        ok, _d2, j = T.occ_fejer(xf, wf, m, N)
        pc.append(npair)
        dens.append(npair / max(len(idx), 1))
        js.append(j)
        oks.append(ok)
        if (i + 1) % 14 == 0:
            print("    ... %d/42 t=%.1f" % (i + 1, time.time() - T0),
                  flush=True)
    n_zero = sum(x == 0 for x in pc)
    corr = float(np.corrcoef(np.array(pc, float), np.array(js, float))[0, 1])
    check("G51-core42-pairs-grow",
          min(pc) == CORE_PAIRS[0] and max(pc) == CORE_PAIRS[1]
          and n_zero == CORE_ZERO and max(dens) <= CORE_DENS_MAX,
          "pairs [%d, %d] zero %d/42 dens max=%.4f -- P not a "
          "fixed constant" % (min(pc), max(pc), n_zero, max(dens)))
    check("G52-core42-pairs-do-not-drive-jump",
          all(oks) and corr < 0.0,
          "42/42 IN at JUMP; corr(pairs,j)=%.3f < 0 -- pair "
          "count is not the source jump" % corr)

    import pivot_entry_lemma_probe as PE  # noqa: E402
    import dirichlet_matched_frame_probe as DMF  # noqa: E402
    import deletion_transform_probe as DT  # noqa: E402
    chi_p = []
    for kz, q in ((15, DMF.Q_CHI3), (19, DMF.Q_CHI3), (23, DMF.Q_CHI3),
                  (20, DMF.Q_CHI4)):
        mz = PE.chi_mz(kz, q)
        N = int(mz["Nw"])
        xf, _ = P.full_grid(N)
        idx = np.asarray(DT.match_indices(xf, mz["yn"]), int)
        chi_p.append(n_pairs_of(idx)[0] / max(len(idx), 1))
    check("G53-chi-pair-density-small",
          max(chi_p) <= 0.06 and min(chi_p) >= 0.0,
          "chi dens=%s (same O(0.04) class, including a "
          "zero-pair window)" % [round(x, 4) for x in chi_p])

    _d, _N, xf97, _w, idx97 = T.mask_idx(97)
    np97, _ = n_pairs_of(idx97)
    den97 = np97 / max(len(idx97), 1)
    check("G54-EXT-kz97-count-grows-dens-stable",
          np97 >= EXT97_PAIRS_FLOOR
          and EXT97_DENS[0] <= den97 <= EXT97_DENS[1],
          "kz97 pairs=%d/%d dens=%.4f -- P grows, P/n_nu stays "
          "O(0.03), not -> 0" % (np97, len(idx97), den97))


def main():
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke

    print("=" * 78)
    print("isolation_lemma_probe -- LEMMA.ISOLATION.01 (round 396)")
    print("SPEC_SHA %s" % SPEC_SHA[:16])
    print("mode: %s" % ("SMOKE" if smoke else "FULL"))
    print("=" * 78)

    section("S0  FIREWALL")
    okf, det = firewall_audit()
    check("G00-firewall", okf, det)

    part_a_pairs()
    xf40, wf40, S40, m234, m123, mR, m1010 = part_b_class(smoke)
    part_c_assist(xf40, wf40, S40, m234, m123, mR, m1010)
    part_d_kills()
    if not smoke:
        part_e_census()

    n_fail = sum(1 for _n, ok in CHECKS if not ok)
    n_ok = len(CHECKS) - n_fail
    print("\nRESULT: %d/%d gates PASS   SPEC_SHA %s   (%.1fs)" % (
        n_ok, len(CHECKS), SPEC_SHA[:16], time.time() - T0))
    if n_fail == 0:
        print("ISOLATION LEMMA %sVERIFIED" % (
            "SMOKE " if smoke else ""))
        return 0
    print("ISOLATION LEMMA FAILED %d" % n_fail)
    return 1


if __name__ == "__main__":
    sys.exit(main())
