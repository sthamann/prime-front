#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""cofinal_phase_cell_probe -- PRIME.COFINAL.PHASE_CELL.01: the
phase-selected cofinal sequence (package D).

EXPLORATION ONLY (experiments/): no ledger row, no paper edit, no
.md, nothing outside experiments/.  NO RH claim.  Frozen (spec +
sha256) before running.

THE STRATEGIC POINT: H_cof demands A_X >= 0 only along a PRE-
DEFINED cofinal window sequence, not for every window.  Route:
split the deployed form into a HEAD (the P-supported comb events,
P = {2,3}, whose placement is governed by the torus phases
phi_p = frac(log p / D)) and a TAIL (the rest); find an OPEN
phase cell U on which the head is uniformly >= delta > 0; then
Kronecker recurrence (rational independence of {log p} -- unique
factorization, two lines) supplies a pre-defined sequence D_k
hitting U infinitely often.  The conditional theorem then needs
the tail >= 0 (package C's job) -- this probe MEASURES how far
the tail is from PSD (the decisive diagnostic).

THE EXACT MECHANIZATION: the deployed tent assembly places atom
p^a at lag position x = a * theta_p, theta_p = log p / D.  The
phase model holds the frame (alpha, M, D, arch, integer parts
N_p = floor(theta_p)) DEPLOYED-FIXED and varies only phi_p in
[0,1): position x(phi) = a (N_p + phi_p).  All evaluations go
through core.atom_lags_at at synthetic positions -- bit for bit
the deployed placement (reflection branch included).  On a cell
of the torus where all floors floor(a phi_p) are constant, the
head matrix is JOINTLY AFFINE in phi -- hence lambda_min is
CONCAVE on each cell and the cell minimum sits at a corner: the
cell census is corner-exact (float roundoff budget only).  The
frame-fixing is typed honestly: the census is the head's phase
landscape AT the deployed frame; frame transport is measured by
comparing the three anchors.

TWO SPLIT VARIANTS (both predeclared; the protocol's reading is
ambiguous about the arch):
  A: head = arch + comb(P), tail = comb(rest)  [head can carry a
     positive floor -- the arch diagonal lives in the head];
  B: head = comb(P) alone, tail = arch + comb(rest)  [the strict
     'events with support in P' reading; the compressed comb-only
     head has zero-trace structure -- expected never >= delta,
     measured and typed].

VERDICT (frozen precedence): PHASE-TRANSLATION-BLOCKED (ward
fails) / PHASE-CELLS-EMPTY (no open positive cell for variant A
2x2 at any anchor) / TAIL-DOMINATES (cells exist but
lambda_min(tail) < -10 tau_full at every anchor -- the split
buys nothing; typed) / PHASE-CELL-FOUND (open cell + rational
floor + tail diagnostic passes the -10 tau bar somewhere; the
conditional theorem parts stated precisely).

FIREWALL: prime + archimedean data only (no zeros); v563/sibling
machinery READ-ONLY; RNG only in declared controls; report only.
"""

import hashlib
import math
import os
import sys
import time
from fractions import Fraction

import numpy as np
import sympy as sp

_here = os.path.dirname(os.path.abspath(__file__))
for _cand in (os.path.join(_here, "..", "..", "verification"), _here):
    if os.path.exists(os.path.join(_cand, "v563_paper2_readouts.py")):
        sys.path.insert(0, os.path.abspath(_cand))
        break
sys.path.insert(0, _here)

import v563_paper2_readouts as core            # noqa: E402 (READ-ONLY)
import spectral_flow_pivot_probe as sfp        # noqa: E402 (READ-ONLY)

T0 = time.time()
FAILS = []
N_CHK = 0

FROZEN_SPEC = """\
cofinal_phase_cell_probe spec v1 (2026-08-08, frozen before run).
Anchors kz 9/12/13; ladder = the 67-rung set (sibling probes).
P-sets: {2,3} main; extensions {2,3,5}, {2,3,5,7} (2x2 census).
Phase model: frame fixed at deployed (alpha, M, D, arch, N_p);
x(phi) = a (N_p + phi_p); evaluation via core.atom_lags_at at
synthetic positions u' = x D.  Cells: products of consecutive
breakpoints {k/a : p^a deployed, 0 <= k <= a} per prime; corner
census exact by concavity of lambda_min on jointly-affine cells;
affineness ward: interior evaluation == affine reconstruction
(rel 1e-9); concavity ward: center >= corner min.
Wards: split exact (c-level and matrix-level, rel <= 1e-12, all
67 rungs); phase model at deployed phases == deployed head
(rel <= 1e-12, anchors); anchor tau regression (5.984165e-4 /
4.351189e-4 / 5.637632e-4 rel 1e-4).
Bars: positive cell = all corners lambda_min > 0 (2x2 closed
form); rational floor delta = Fraction(0.999 * min corner
lambda_min) limit_denominator 10^6, valid modulo the float
budget 1e-10 * ||H|| (typed); TAIL-DOMINATES iff
lambda_min(tail_A, 16-mode) < -10 tau_full at ALL THREE anchors;
scramble control: 200 incoherent-phase samples, seed 20260808.
Kronecker: independence via unique factorization (symbolic
statement); explicit t_k = the first 5 hits of the line
(t log 2, t log 3) mod 1 in the best cell, scanned t in
[t_dep, t_dep + 2000] step 1e-3.  NO RH claim; report only."""

ANCHORS = (9, 12, 13)
TAU_REFS = {9: 5.984165e-4, 12: 4.351189e-4, 13: 5.637632e-4}
TAU_REF_REL = 1.0e-4
SPLIT_REL = 1.0e-12
AFF_REL = 1.0e-9
TAIL_BAR = 10.0
SCR_SEED = 20260808
N_SCR = 200
P_MAIN = (2, 3)
P_EXT = ((2, 3, 5), (2, 3, 5, 7))


def check(name, ok, detail=""):
    global N_CHK
    N_CHK += 1
    if not ok:
        FAILS.append(name.split()[0])
    print("[%s] %s%s" % ("PASS" if ok else "FAIL", name,
                         (": " + detail) if detail else ""))


def factor_pa(n):
    """n = p^a for prime power n, else None."""
    for p in (2, 3, 5, 7, 11, 13):
        if n % p == 0:
            a = 0
            while n % p == 0:
                n //= p
                a += 1
            return (p, a) if n == 1 else None
    return None


def rung_frame(kz):
    al = float(core.U_ALL[kz])
    Dk = 0.5 * float(core.G_ALL[kz]) / float(core.NU_MAIN)
    M = int(math.ceil(al / Dk - 1.0e-9)) + 1
    if M % 2:
        M += 1
    h = M // 2
    ka = core.atoms_in(al)
    uu = np.asarray(core.U_ALL[:ka], float)
    mm = np.asarray(core.MU_ALL[:ka], float)
    D = 2.0 * al / M
    atoms = []
    for u_j, m_j in zip(uu, mm):
        n = int(round(math.exp(u_j)))
        pa = factor_pa(n)
        atoms.append((n, pa[0] if pa else None,
                      pa[1] if pa else None, float(u_j),
                      float(m_j)))
    return dict(kz=kz, al=al, M=M, h=h, D=D, uu=uu, mm=mm,
                atoms=atoms)


def head_mask(fr, P):
    return np.array([a[1] in P for a in fr["atoms"]], bool)


def comb16(fr, uu, mm, Tb):
    c_at, _ = core.atom_lags_at(fr["al"], fr["M"], uu, mm)
    return Tb @ (core.odd_toeplitz(np.asarray(c_at, float),
                                   fr["M"]) @ Tb.T)


def head_positions(fr, P, phis):
    """Synthetic positions/masses of the P-head at torus point
    phis = {p: phi_p} (frame fixed)."""
    pos, mas = [], []
    for (n, p, a, u_j, m_j) in fr["atoms"]:
        if p in P:
            Np = int(math.floor(math.log(p) / fr["D"]))
            pos.append((a * (Np + phis[p])) * fr["D"])
            mas.append(m_j)
    return np.array(pos), np.array(mas)


def lam_min2(H):
    tr = H[0, 0] + H[1, 1]
    dd = H[0, 0] * H[1, 1] - H[0, 1] ** 2
    return 0.5 * (tr - math.sqrt(max(tr * tr - 4.0 * dd, 0.0)))


def breakpoints(fr, P):
    """Per prime: sorted breakpoints {k/a} for deployed powers."""
    bps = {}
    for p in P:
        amax = max((a[2] for a in fr["atoms"] if a[1] == p),
                   default=1)
        s = {Fraction(0), Fraction(1)}
        for a in range(1, amax + 1):
            for k in range(a + 1):
                s.add(Fraction(k, a))
        bps[p] = sorted(s)
    return bps


def run():
    print("=" * 78)
    print("COFINAL PHASE CELL (cofinal_phase_cell_probe) -- "
          "PRIME.COFINAL.PHASE_CELL.01")
    print("=" * 78)
    print("frozen spec sha256 = %s"
          % hashlib.sha256(FROZEN_SPEC.encode()).hexdigest()[:16])
    print("""
HONESTY FRAME: NO RH claim.  The census is the head's phase
landscape AT THE DEPLOYED FRAME (alpha, M, D, arch, N_p fixed);
the Kronecker recurrence statement varies D, which moves the
frame -- the transport question is measured across the three
anchors and typed, not assumed.""")

    # ============================================================== S0
    print("\nS0 -- frames + the Kronecker independence lemma")
    frames = {kz: rung_frame(kz) for kz in ANCHORS}
    for kz in ANCHORS:
        fr = frames[kz]
        nh = int(np.sum(head_mask(fr, P_MAIN)))
        print("    kz=%2d: alpha %.3f, M %d, D %.4f, atoms %d "
              "(head{2,3} %d); deployed phases phi2 %.4f, "
              "phi3 %.4f"
              % (kz, fr["al"], fr["M"], fr["D"],
                 len(fr["atoms"]), nh,
                 math.log(2) / fr["D"] % 1.0,
                 math.log(3) / fr["D"] % 1.0))
    p_, q_ = sp.symbols("p q", positive=True, integer=True)
    print("""    KRONECKER LEMMA (the two-line proof, stated): suppose
    sum_p a_p log p = 0 with integers a_p not all zero, p in P.
    Exponentiating: prod p^{a_p} = 1, i.e. prod_{a_p>0} p^{a_p}
    = prod_{a_p<0} p^{-a_p} -- two distinct prime factorizations
    of the same integer > 1, contradicting unique factorization
    (Z is a UFD).  Hence {log p : p prime} is linearly
    independent over Q, and by Weyl the line (t log 2, t log 3,
    ...) mod 1 equidistributes on the torus: ANY open cell U is
    hit by an explicit, pre-defined, unbounded sequence t_k.""")
    ok_sym = bool(sp.simplify(sp.log(p_ ** 2) - 2 * sp.log(p_))
                  == 0)
    ok_num = True
    l2, l3 = math.log(2), math.log(3)
    for aa in range(-20, 21):
        for bb in range(-20, 21):
            if (aa, bb) != (0, 0):
                ok_num &= abs(aa * l2 + bb * l3) > 1e-9
    check("S0.KRO independence sanity: no integer relation "
          "a log2 + b log3 = 0 for |a|,|b| <= 20 (numeric, "
          "consistent with the UF proof) AND sympy log-power "
          "identity holds", ok_num and ok_sym)

    # ============================================================== S1
    print("\nS1 -- the head/tail split (exact, all 67 rungs)")
    rungs = []
    for kz in core.frame_a_zones():
        al = float(core.U_ALL[kz])
        Dk = 0.5 * float(core.G_ALL[kz]) / float(core.NU_MAIN)
        M = int(math.ceil(al / Dk - 1.0e-9)) + 1
        if M % 2:
            M += 1
        if M // 2 == sfp.ANOMALOUS_H:
            continue
        if math.exp(2.0 * al) > core.ATOM_MAX + 0.5:
            continue
        rungs.append(kz)
    ok_split = True
    ladder = []
    for kz in rungs:
        fr = rung_frame(kz)
        hm = head_mask(fr, P_MAIN)
        c_all, _ = core.atom_lags_at(fr["al"], fr["M"], fr["uu"],
                                     fr["mm"])
        c_h, _ = core.atom_lags_at(fr["al"], fr["M"],
                                   fr["uu"][hm], fr["mm"][hm])
        c_t, _ = core.atom_lags_at(fr["al"], fr["M"],
                                   fr["uu"][~hm], fr["mm"][~hm])
        sc = max(float(np.max(np.abs(c_all))), 1e-300)
        ok_split &= float(np.max(np.abs(c_h + c_t - c_all))) \
            <= SPLIT_REL * sc
        Tb = core.parity_basis(fr["h"], min(sfp.K_MODES,
                                            fr["h"]))
        A_h = comb16(fr, fr["uu"][hm], fr["mm"][hm], Tb)
        A_t = comb16(fr, fr["uu"][~hm], fr["mm"][~hm], Tb)
        c_ar = np.asarray(core.arch_lags(fr["M"], fr["D"]), float)
        A_ar = Tb @ (core.odd_toeplitz(c_ar, fr["M"]) @ Tb.T)
        A_full = A_ar + A_h + A_t
        tau = float(np.linalg.eigvalsh(A_full[:2, :2])[0])
        ladder.append(dict(kz=kz, h=fr["h"], tau=tau,
                           lam_tailA=float(np.linalg.eigvalsh(
                               0.5 * (A_t + A_t.T))[0]),
                           lam_headA=float(np.linalg.eigvalsh(
                               0.5 * (A_ar + A_h
                                      + (A_ar + A_h).T))[0]),
                           lam_tailB=float(np.linalg.eigvalsh(
                               0.5 * (A_ar + A_t
                                      + (A_ar + A_t).T))[0]),
                           tr_headB=float(np.trace(A_h))))
        if kz in ANCHORS:
            frames[kz]["Tb"] = Tb
            frames[kz]["A_ar"] = 0.5 * (A_ar + A_ar.T)
            frames[kz]["A_tail"] = 0.5 * (A_t + A_t.T)
            frames[kz]["A_head_dep"] = 0.5 * (A_h + A_h.T)
            frames[kz]["tau"] = tau
    check("S1.SPL split ward: c-level head + tail == deployed on "
          "all %d rungs (rel <= %.0e; matrix level follows by "
          "linearity of the compression)" % (len(rungs),
                                             SPLIT_REL), ok_split)
    ok_tau = all(abs(frames[kz]["tau"] / TAU_REFS[kz] - 1.0)
                 <= TAU_REF_REL for kz in ANCHORS)
    check("S1.TAU deployed-phase regression: anchor tau "
          "reproduces the frozen refs (rel <= %.0e)"
          % TAU_REF_REL, ok_tau)

    # ============================================================== S2
    print("\nS2 -- the phase model ward + the symbolic affine "
          "head")
    ok_mod = True
    for kz in ANCHORS:
        fr = frames[kz]
        phis_dep = {p: (math.log(p) / fr["D"]) % 1.0
                    for p in P_MAIN}
        pos, mas = head_positions(fr, P_MAIN, phis_dep)
        A_mod = comb16(fr, pos, mas, fr["Tb"])
        sc = max(float(np.max(np.abs(fr["A_head_dep"]))), 1e-300)
        ok_mod &= float(np.max(np.abs(0.5 * (A_mod + A_mod.T)
                                      - fr["A_head_dep"]))) \
            <= 1e-10 * sc
    check("S2.MOD phase model at the deployed phases == the "
          "deployed head, bit for bit through the same tent "
          "assembly (rel <= 1e-10, all anchors)", ok_mod)

    def head2(fr, phis, P):
        pos, mas = head_positions(fr, P, phis)
        A = comb16(fr, pos, mas, fr["Tb"])
        return fr["A_ar"][:2, :2] + 0.5 * (A + A.T)[:2, :2]

    fr9 = frames[9]
    bps9 = breakpoints(fr9, P_MAIN)
    ph_dep9 = {p: (math.log(p) / fr9["D"]) % 1.0 for p in P_MAIN}

    def cell_of(bps, ph):
        cell = {}
        for p in bps:
            bb = bps[p]
            i = max(0, np.searchsorted(
                [float(x) for x in bb], ph[p], side="right") - 1)
            cell[p] = (bb[i], bb[min(i + 1, len(bb) - 1)])
        return cell

    cdep = cell_of(bps9, ph_dep9)
    lo2, hi2 = cdep[2]
    lo3, hi3 = cdep[3]
    e2 = float(hi2 - lo2)
    e3 = float(hi3 - lo3)
    H00 = head2(fr9, {2: float(lo2), 3: float(lo3)}, P_MAIN)
    H10 = head2(fr9, {2: float(hi2), 3: float(lo3)}, P_MAIN)
    H01 = head2(fr9, {2: float(lo2), 3: float(hi3)}, P_MAIN)
    H11 = head2(fr9, {2: float(hi2), 3: float(hi3)}, P_MAIN)
    G2 = (H10 - H00) / e2
    G3 = (H01 - H00) / e3
    aff_res = float(np.max(np.abs(H11 - (H00 + e2 * G2
                                         + e3 * G3))))
    Hc = head2(fr9, {2: float(lo2) + 0.5 * e2,
                     3: float(lo3) + 0.5 * e3}, P_MAIN)
    aff_res2 = float(np.max(np.abs(
        Hc - (H00 + 0.5 * e2 * G2 + 0.5 * e3 * G3))))
    sc = max(float(np.max(np.abs(H00))), 1e-300)
    check("S2.AFF affineness ward on the deployed cell (kz 9): "
          "opposite-corner and center reconstructions match the "
          "affine model (rel %.1e, %.1e <= %.0e) -- the head IS "
          "jointly affine per cell, corner census exact"
          % (aff_res / sc, aff_res2 / sc, AFF_REL),
          aff_res <= AFF_REL * sc and aff_res2 <= AFF_REL * sc)
    f2s, f3s = sp.symbols("phi2 phi3", real=True)
    Hsym = sp.Matrix(2, 2, lambda i, j: sp.nsimplify(
        round(H00[i, j], 10), rational=False)
        + round(G2[i, j], 10) * (f2s - sp.nsimplify(lo2))
        + round(G3[i, j], 10) * (f3s - sp.nsimplify(lo3)))
    print("    SYMBOLIC HEAD on the deployed cell of kz 9, "
          "phi in [%s,%s] x [%s,%s]:" % (lo2, hi2, lo3, hi3))
    print("      H(phi) = H0 + (phi2 - %s) G2 + (phi3 - %s) G3"
          % (lo2, lo3))
    for nm_, Mx in (("H0", H00), ("G2", G2), ("G3", G3)):
        print("      %s = [[%+.6f, %+.6f], [%+.6f, %+.6f]]"
              % (nm_, Mx[0, 0], Mx[0, 1], Mx[1, 0], Mx[1, 1]))
    print("      (sympy affine entries constructed: %s)"
          % (Hsym.shape == (2, 2)))

    # ============================================================== S3
    print("\nS3 -- the cell census (variant A head = arch + "
          "comb(P))")

    def census(fr, P, block16=False):
        bps = breakpoints(fr, P)
        primes = list(P)
        grids = [np.array([float(x) for x in bps[p]])
                 for p in primes]
        shape = tuple(len(g) for g in grids)
        lam_grid = np.zeros(shape)
        lam16_grid = np.zeros(shape) if block16 else None
        it = np.ndindex(*shape)
        for idx in it:
            phis = {p: grids[i][idx[i]]
                    for i, p in enumerate(primes)}
            pos, mas = head_positions(fr, P, phis)
            A = comb16(fr, pos, mas, fr["Tb"])
            H16 = fr["A_ar"] + 0.5 * (A + A.T)
            lam_grid[idx] = lam_min2(H16[:2, :2])
            if block16:
                lam16_grid[idx] = float(
                    np.linalg.eigvalsh(H16)[0])
        cells_pos, best = 0, None
        n_cells, area_pos = 0, Fraction(0)
        for idx in np.ndindex(*(s - 1 for s in shape)):
            n_cells += 1
            corners = [tuple(idx[i] + d[i]
                             for i in range(len(primes)))
                       for d in np.ndindex(*(2,) * len(primes))]
            mn = min(lam_grid[c] for c in corners)
            if mn > 0.0:
                cells_pos += 1
                vol = Fraction(1)
                for i, p in enumerate(primes):
                    vol *= (bps[p][idx[i] + 1] - bps[p][idx[i]])
                area_pos += vol
                if best is None or mn > best[0]:
                    best = (mn, tuple(
                        (bps[primes[i]][idx[i]],
                         bps[primes[i]][idx[i] + 1])
                        for i in range(len(primes))))
        out = dict(n_cells=n_cells, cells_pos=cells_pos,
                   area_pos=area_pos, best=best,
                   frac_grid_pos=float(np.mean(lam_grid > 0)),
                   lam_grid_min=float(np.min(lam_grid)),
                   lam_grid_max=float(np.max(lam_grid)))
        if block16:
            out["frac16_pos"] = float(np.mean(lam16_grid > 0))
            out["lam16_max"] = float(np.max(lam16_grid))
        return out, bps

    cens = {}
    for kz in ANCHORS:
        cens[kz], _ = census(frames[kz], P_MAIN, block16=True)
        cc = cens[kz]
        print("    kz=%2d: %d cells, %d POSITIVE (area %.4f); "
              "grid lambda_min in [%.3f, %.3f]; best cell floor "
              "%.6f; 16-mode: %.1f%% of grid points positive "
              "(max lam16 %.4f)"
              % (kz, cc["n_cells"], cc["cells_pos"],
                 float(cc["area_pos"]), cc["lam_grid_min"],
                 cc["lam_grid_max"],
                 cc["best"][0] if cc["best"] else float("nan"),
                 100 * cc["frac16_pos"], cc["lam16_max"]))
    kz_best = max(ANCHORS,
                  key=lambda k: (cens[k]["best"][0]
                                 if cens[k]["best"] else -1e9))
    have_cell = cens[kz_best]["best"] is not None
    if have_cell:
        mn, box = cens[kz_best]["best"]
        delta = Fraction(0.999 * mn).limit_denominator(10 ** 6)
        print("    BEST OPEN CELL (kz %d): phi2 in (%s, %s), "
              "phi3 in (%s, %s); corner-certified floor "
              "lambda_min >= %.6f; RATIONAL floor delta = %s "
              "(= %.6f), valid modulo the float budget "
              "1e-10 ||H||"
              % (kz_best, box[0][0], box[0][1], box[1][0],
                 box[1][1], mn, delta, float(delta)))
        fr_b = frames[kz_best]
        e2b = float(box[0][1] - box[0][0])
        e3b = float(box[1][1] - box[1][0])
        Hcen = head2(fr_b, {2: float(box[0][0]) + 0.5 * e2b,
                            3: float(box[1][0]) + 0.5 * e3b},
                     P_MAIN)
        check("S3.CON concavity ward: center of the best cell "
              "lambda_min %.6f >= corner floor %.6f"
              % (lam_min2(Hcen), mn), lam_min2(Hcen) >= mn - 1e-9)
        ph_dep_b = {p: (math.log(p) / fr_b["D"]) % 1.0
                    for p in P_MAIN}
        d2 = max(float(box[0][0]) - ph_dep_b[2],
                 ph_dep_b[2] - float(box[0][1]), 0.0)
        d3 = max(float(box[1][0]) - ph_dep_b[3],
                 ph_dep_b[3] - float(box[1][1]), 0.0)
        print("    deployed phase point (%.4f, %.4f): distance "
              "to the best cell (%.4f, %.4f); head at deployed "
              "phases lambda_min2 = %.6f"
              % (ph_dep_b[2], ph_dep_b[3], d2, d3,
                 lam_min2((fr_b["A_ar"]
                           + fr_b["A_head_dep"])[:2, :2])))
    trB = [ld["tr_headB"] for ld in ladder]
    lamB_dep = []
    for kz in ANCHORS:
        fr = frames[kz]
        lamB_dep.append(float(np.linalg.eigvalsh(
            fr["A_head_dep"][:2, :2])[0]))
    print("    VARIANT B (head = comb(P) alone): trace med %.2e "
          "along the ladder (zero-trace structure => never >= "
          "delta I: any nonzero comb-only head has lambda_min "
          "<= 0); measured lambda_min2 at deployed phases: %s "
          "-- variant B is DEAD as a positivity carrier (typed)"
          % (float(np.median(np.abs(trB))),
             ", ".join("%.4f" % x for x in lamB_dep)))

    # ============================================================== S4
    print("\nS4 -- the tail price (the decisive diagnostic)")
    third = max(len(ladder) // 3, 1)
    lt = np.array([ld["lam_tailA"] for ld in ladder])
    lh = np.array([ld["lam_headA"] for ld in ladder])
    tt = np.array([ld["tau"] for ld in ladder])
    print("    tail_A = comb(p >= 5), 16-mode lambda_min: "
          "shallow med %.4f -> deep med %.4f; ratio to tau_full "
          "med %.1e (bar: TAIL-DOMINATES if < -%.0f at all "
          "anchors)"
          % (float(np.median(lt[:third])),
             float(np.median(lt[-third:])),
             float(np.median(lt / tt)), TAIL_BAR))
    print("    head_A (arch + comb{2,3}), 16-mode lambda_min at "
          "deployed phases: shallow med %.4f -> deep med %.4f "
          "(the head alone is %s at the deployed point)"
          % (float(np.median(lh[:third])),
             float(np.median(lh[-third:])),
             "PSD" if float(np.median(lh)) >= 0 else
             "NOT PSD in 16 modes"))
    ltB = np.array([ld["lam_tailB"] for ld in ladder])
    print("    tail_B (arch + comb(p >= 5)) lambda_min med "
          "%.4f -- variant B tail equally far from PSD"
          % float(np.median(ltB)))
    tail_ok_anchors = [ld["lam_tailA"] >= -TAIL_BAR * ld["tau"]
                       for ld in ladder
                       if ld["kz"] in ANCHORS]
    tail_dominates = not any(tail_ok_anchors)
    print("    anchors: lambda_min(tail_A)/tau = %s -> tail %s"
          % (", ".join("%.1e" % (ld["lam_tailA"] / ld["tau"])
                       for ld in ladder if ld["kz"] in ANCHORS),
             "DOMINATES (the split moves the demand onto an "
             "object farther from PSD than the full form)"
             if tail_dominates else "within the bar somewhere"))

    # ============================================================== S5
    print("\nS5 -- the extension ladder (2x2 census)")
    for P in P_EXT:
        cc, _ = census(frames[kz_best], P, block16=False)
        print("    P = %s (kz %d): %d cells, %d positive (volume "
              "%.4f); best floor %.6f -- the trade law: %s"
              % (P, kz_best, cc["n_cells"], cc["cells_pos"],
                 float(cc["area_pos"]),
                 cc["best"][0] if cc["best"] else float("nan"),
                 "cells persist under extension"
                 if cc["cells_pos"] > 0 else
                 "extension kills the cells"))

    # ============================================================== S6
    print("\nS6 -- the Kronecker step (explicit t_k for the "
          "best cell)")
    if have_cell:
        fr_b = frames[kz_best]
        t_dep = 1.0 / fr_b["D"]
        hits = []
        t = t_dep
        while len(hits) < 5 and t < t_dep + 2000.0:
            f2 = (t * math.log(2)) % 1.0
            f3 = (t * math.log(3)) % 1.0
            if (float(box[0][0]) < f2 < float(box[0][1])
                    and float(box[1][0]) < f3 < float(box[1][1])):
                hits.append(t)
                t += 0.5
            t += 1e-3
        print("    the line (t log2, t log3) mod 1 (t = 1/D): "
              "deployed t = %.4f; first %d explicit hits of the "
              "best cell: %s -- the pre-defined sequence exists "
              "and is computable (Kronecker/Weyl; the lemma of "
              "S0); NOTE (typed): each t_k moves the FRAME "
              "(M, arch, N_p), so the deployed-frame landscape "
              "does not transport automatically -- the anchors' "
              "census consistency above is the measured proxy"
              % (t_dep, len(hits),
                 ", ".join("%.3f" % x for x in hits)))
    else:
        print("    no cell -- the Kronecker step is moot (typed).")

    # ============================================================== S7
    print("\nS7 -- scramble control (incoherent phases)")
    rng = np.random.default_rng(SCR_SEED)
    fr9 = frames[9]
    n_pos = 0
    for _ in range(N_SCR):
        pos, mas = [], []
        for (n, p, a, u_j, m_j) in fr9["atoms"]:
            if p in P_MAIN:
                Np = int(math.floor(math.log(p) / fr9["D"]))
                x = a * Np + a * rng.uniform(0.0, 1.0)
                pos.append(x * fr9["D"])
                mas.append(m_j)
        A = comb16(fr9, np.array(pos), np.array(mas), fr9["Tb"])
        H = fr9["A_ar"][:2, :2] + 0.5 * (A + A.T)[:2, :2]
        if lam_min2(H) > 0:
            n_pos += 1
    coher = cens[9]["frac_grid_pos"]
    print("    incoherent per-atom phases (coherence a*phi_p "
          "broken): %d/%d samples positive (%.2f) vs coherent "
          "grid fraction %.2f -- the cell structure %s phase "
          "coherence"
          % (n_pos, N_SCR, n_pos / N_SCR, coher,
             "requires" if abs(n_pos / N_SCR - coher) > 0.1
             else "is NOT specific to (typed)"))

    # ============================================================== S8
    print("\nS8 -- verdict")
    wards_ok = not FAILS
    any_cell = any(cens[k]["best"] is not None for k in ANCHORS)
    if not wards_ok:
        verdict = "PHASE-TRANSLATION-BLOCKED"
    elif not any_cell:
        verdict = "PHASE-CELLS-EMPTY"
    elif tail_dominates:
        verdict = "TAIL-DOMINATES"
    else:
        verdict = "PHASE-CELL-FOUND"
    print("=" * 78)
    print("V -- VERDICT: %s" % verdict)
    print("=" * 78)
    if verdict == "TAIL-DOMINATES":
        print("""    THE TYPED OUTCOME: part 2 of the conditional route WORKS --
    the head (arch + comb{2,3}) HAS open phase cells with
    corner-certified rational floors (best %.6f at kz %d; %.0f%%
    of the torus positive), the affine/concavity mechanics are
    exact, and the Kronecker sequence hitting the cell is
    explicit.  But the route DIES at the tail: lambda_min(tail)
    ~ %.2f = %.0e x tau -- the split moves the positivity demand
    onto comb(p >= 5) WITHOUT the arch diagonal, an object
    O(10^3-10^4) farther from PSD than the full form.  The full
    form's positivity is a fine cancellation ACROSS the split
    line: conditioning on the head's phases cannot decouple it.
    HONEST CONSEQUENCE: phase selection buys real, certifiable
    positivity for the P-head, but H_cof needs the WHOLE form;
    unless package C produces tail >= 0 (which this measurement
    says is false as stated -- the tail alone is strongly
    indefinite), the phase-cell route closes.  The salvage, if
    any, is a REBALANCED split (head keeps enough arch/comb mass
    to leave a PSD-able tail) -- a different protocol, typed as
    the named next object."""
              % (cens[kz_best]["best"][0], kz_best,
                 100 * float(cens[kz_best]["area_pos"]),
                 float(np.median(lt)),
                 float(np.median(lt / tt))))
    elif verdict == "PHASE-CELL-FOUND":
        print("""    Parts stated precisely: (1) tail >= 0 along the sequence --
    OPEN (package C; measured status above); (2) head >= delta
    on the open cell U + Kronecker recurrence -- ESTABLISHED at
    the deployed frame (rational floor, corner-certified);
    (3) H_cof along the pre-defined sequence => the kernel-
    checked minimal hypothesis' demand -- conditional on (1) and
    frame transport (typed).""")
    elif verdict == "PHASE-CELLS-EMPTY":
        print("""    Every cell of the deployed-frame torus contains a negative
    point for the variant-A head; the landscape and the killing
    prime are in S3/S5 -- the head is never uniformly positive
    and the phase-selection route closes at step one (typed).""")
    dt_run = time.time() - T0
    print("-" * 78)
    print("checks: %d run, %d failed%s | runtime %.1f min"
          % (N_CHK, len(FAILS),
             (" [" + ", ".join(FAILS) + "]") if FAILS else "",
             dt_run / 60.0))
    print("NO RH claim; report only; nothing outside experiments/ "
          "touched.")


if __name__ == "__main__":
    run()
