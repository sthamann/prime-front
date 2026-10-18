#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""v847 -- PRIME.WEDGE.LAGRANGE.01 + PRIME.CELLCONE.TRANSPORT.01: the two remaining v5.4 architecture decisions, each an honest negative with a typed positive core -- the sign-register wedge lift EXISTS as exact algebra where the naive signed Lagrange provably cannot but the frame-uniform relational law dies on the SAME uniformity wall as the commutant no-go, and the completed-cell Lorentz transport BREAKS the cone at the n = 2 cell on every rung with the monotone ray cascade to the compiler null direction (5,-3,4) CONFIRMED and the Epstein control INVERTED, ONE module from two probes (13 + 9 checks with the two frozen-honest FAILS S5.SCR and S5.C3 kept and pattern-gated, NOT refit; verdicts WEDGE-PARTIAL and CONE-BROKEN + RAY-EDGE-CONFIRMED; discovery probes relational_lagrange_probe.py and cell_cone_transport_probe.py, 2026-08-07, re-run identically at promotion, promoted VERBATIM with no downscoping, ~6 s).  PART A, THE WEDGE (work package C): LEVEL A, the naive signed Lagrange no-go is EXACT (sympy: the wedge squares are linearly independent, so the pair weights are FORCED W_rs = w_r w_s -- no reweighting of a fixed signed family can make the expansion nonneg); the negative pair mass is real and forced (P-/det ~ 2.0e4..3.2e4; 25-31% of P- carried by the arch/pole block B, which is NEGATIVE definite in this compression -- kz9 eigen -2.285/-1.139, the typed run-1 finding: a manifestly nonneg wedge family must rebuild even B from comb material).  LEVEL B, the sign-register lift WORKS: the C2 register turns the Moebius sign into difference geometry (symbolic: e+ (x) a + e- (x) b compresses under chi = (1,-1)/sqrt2 to (a-b)(a-b)^T/2 EXACTLY), and the lifted cone contains Ah at floor grade on EVERY anchor (exact LP, resid <= 8.9e-16) -- nonneg wedge weights EXIST pointwise where level A provably cannot.  LEVEL C FAILS (the substance): one frozen theta across frames reaches only ~15% relative (design 0.170/0.151, HELD-OUT 0.153) while the floor certificate needs ~4.5 orders deeper (tau/||Ah|| = 4.4e-5); even the per-frame 8-class law cannot reach floor grade -- the commutant no-go TRANSPORTED: in both routes the wall is UNIFORMITY IN THE WINDOW, not the sign.  THE ONE HONEST CONTROL MISS (S5.SCR, kept as frozen FAIL): the scramble blows the level-C residual x7.5 against the frozen x10 bar -- a law that itself only reaches ~15% has bounded structure to break; typed, not excused.  The Epstein control fires (off-pp Lambda_F mass 336.37 with 6 NEGATIVE sites; zeta comb off-pp mass 0).  PART B, THE CELL CONE (work package D): the completed cells (atom kick + its Stieltjes/mass-matched continuum increment; two predeclared grouping rules G1/G2, both PARTITIONING [U0, 2 alpha]) telescope EXACTLY from A_0 = B - S_pnt to Ah (worst rel 3.4e-15); the congruence calculus is exact (Phi^T J Phi = c J at 2.2e-16 with c = det-ratio, the literal J-inequality honestly typed as ON-CONE); the certified envelope reproduces (min e1 = 4.8546 >= 4.331).  THE MEASUREMENT: BOTH groupings EXIT the Lorentz cone on 67/67 rungs, first exit at the n = 2 cell (median cell index 1-2), out-of-cone fraction median 0.34 (G1) / 0.89 (G2), endpoint back INSIDE the cone on 67/67 rungs (= the certified tau > 0); J-defect census G1 49.6% / G2 12.1% expanding cells.  THE RAY CASCADE (sub-verdict): r_end 0.5700 -> 0.8018 monotone (Kendall vs alpha +1.000) and the angle to the compiler null ray (5,-3,4) = (g_car, -N_fam, |mu4|) falls 46.26 -> 34.39 deg (Kendall -1.000) -- RAY-EDGE-CONFIRMED on both groupings.  The incomplete-cell contrast fires 67/67 (the completion is load-bearing); equal-weight and wrong-norm controls fire 14/14.  THE INVERTED EPSTEIN SIGNATURE (S5.C3, kept as frozen FAIL): the mass-matched Epstein comb does NOT break the cone transport (0/14 exits) while the TRUE von Mangoldt comb does -- the cone dips are the true comb's own small-x fluctuation psi(x) - x (the n = 2 cell), which the smoother Epstein representation numbers do not reproduce; the arithmetic sits IN the violations; the frozen must-break prediction pointed the wrong way and is kept.  HONEST CONSEQUENCE: neither route delivers a second proof architecture; together with v846 all three v5.4 architectures die on the same finer-than-statistical substance (typed TV / uniformity / renormalization walls) -- constant wedge laws and unrenormalized small-n cell transports are stop-listed; the named next objects are an h-DEPENDENT weight law and a renormalized cell map.  NO RH claim.  Python-only per GATE.WOLFRAM.02.

PROVENANCE: discovery probes relational_lagrange_probe.py (13 run, 1
frozen-honest FAIL S5.SCR, verdict WEDGE-PARTIAL) and
cell_cone_transport_probe.py (9 run, 1 frozen-honest FAIL S5.C3,
verdict CONE-BROKEN; the declared run-1 implementation corrections
are in the frozen probe docstring, no bar changed), both 2026-08-07,
re-run identically at promotion; this module runs both frozen
protocols VERBATIM (the FROZEN_SPEC constant and the G1/G2 grouping
rules embedded byte-exact so the printed SHA-256 values reproduce;
the two FAILS are EXPECTED and pattern-gated per the v829/v831/v843
preregistered-honest precedent -- the bars are NOT refit; runtime
~6 s).  The original probe docstrings live verbatim in
experiments/tfpt-discovery/.

FIREWALL: no zeros anywhere (prime side only); v563 READ-ONLY;
mpmath = the zero-free constant C_TH only; RNG only in the declared
scramble (seed 20260807); own spf sieves.  NO RH claim.
"""

import ast
import hashlib
import inspect
import math
import os
import sys
import time
from fractions import Fraction as Fr

import numpy as np
import sympy as sp
from scipy.optimize import linprog, nnls

_here = os.path.dirname(os.path.abspath(__file__))
if _here not in sys.path:
    sys.path.insert(0, _here)

import v563_paper2_readouts as core        # noqa: E402  (READ-ONLY)
from mpmath import mp, zeta, diff as mpdiff  # noqa: E402 (VALUES only)

EXPECTED_A = "WEDGE-PARTIAL"
EXPECTED_B = "CONE-BROKEN"
EXPECTED_FAILS_A = ["S5.SCR"]
EXPECTED_FAILS_B = ["S5.C3"]
N_CHECKS_A = 13
N_CHECKS_B = 9

_VERDICTS = {}

T0 = time.time()
FAILS_A = []
N_CHK = 0

# ---------------------------------------- probe-A constants
ANCHORS = (9, 12, 13)
DESIGN, HELD_OUT = (9, 12), 13
TAU_REFS = {9: 5.984165e-4, 12: 4.351189e-4, 13: 5.637632e-4}
TAU_REF_REL = 1.0e-4
ID_BAR = 1.0e-9
LAG_BAR = 1.0e-8
FLOOR_FAC = 0.10          # floor grade: ||resid||_2 <= 0.10 tau_X
FORMULA_REL = 0.05        # formula grade: rel resid <= 5%
SCR_SEED = 20260807
SCR_BLOW = 10.0
LADDER_XMAX = 2048.0
PERSIST_MIN = 0.90
EPS_OFFPP = 1.0e-12
CLASSES = ("B1", "B2", "Y", "Z", "NPY", "NPZ", "DCH", "DPO")


def check(name, ok, detail=""):
    global N_CHK
    N_CHK += 1
    if not ok:
        FAILS_A.append(name.split()[0])
    print("[%s] %s%s" % ("PASS" if ok else "FAIL", name,
                         (": " + detail) if detail else ""))


def sieve_spf(nmax):
    spf = list(range(nmax + 1))
    p = 2
    while p * p <= nmax:
        if spf[p] == p:
            for q in range(p * p, nmax + 1, p):
                if spf[q] == q:
                    spf[q] = p
        p += 1
    return spf


def factorize(n, spf):
    f = {}
    while n > 1:
        p = spf[n]
        f[p] = f.get(p, 0) + 1
        n //= p
    return f


def mu_of(n, spf):
    f = factorize(n, spf)
    if any(a > 1 for a in f.values()):
        return 0
    return -1 if len(f) % 2 else 1


def is_pp(n, spf):
    return len(factorize(n, spf)) == 1


def divisors(n, spf):
    ds = [1]
    for p, a in factorize(n, spf).items():
        ds = [d * p ** k for d in ds for k in range(a + 1)]
    return sorted(ds)


# ------------------------------------------------- frame machinery
def site_E(rr, u):
    """The additive per-site 2x2 (E = -Xn read at position u)."""
    x11 = core.spline_project(rr["W11"], u, rr["D"], rr["M"])
    x22 = core.spline_project(rr["W22"], u, rr["D"], rr["M"])
    x12 = core.spline_project(rr["W12"], u, rr["D"], rr["M"])
    return -np.array([[x11, x12], [x12, x22]])


def eig_pairs(M2):
    """EXACT signed eigen split of a symmetric 2x2:
    M2 == sum of e_i v_i v_i^T over both pairs (no clipping)."""
    ev, V = np.linalg.eigh(M2)
    return [(float(ev[1]), V[:, 1].copy()),
            (float(ev[0]), V[:, 0].copy())]


def sym3(M2):
    return np.array([M2[0, 0], M2[1, 1], M2[0, 1]])


def m_of(v):
    return np.outer(v, v)


def frame_data(kz, scramble=None):
    """Everything the levels need for one frame."""
    rr = core.build_window(kz, scramble_seed=scramble) \
        if scramble is not None else core.build_window(kz)
    lam = np.asarray(rr["lam"], float)
    Xn = np.asarray(rr["Xn"], float)
    B = np.asarray(rr["B"], float)
    Ah = np.asarray(rr["Ah"], float)
    nv = np.rint(np.exp(np.asarray(rr["uu"], float))).astype(int)
    X = int(math.floor(math.exp(2.0 * float(rr["alpha"])) + 0.5))
    E = [-np.array([[Xn[j, 0], Xn[j, 2]], [Xn[j, 2], Xn[j, 1]]])
         for j in range(len(lam))]
    return dict(rr=rr, lam=lam, B=B, Ah=Ah, nv=nv, X=X, E=E,
                tau=float(np.linalg.eigvalsh(Ah)[0]))


def lifted_family(fd, spf):
    """The frozen direction family + class tags + magnitudes.

    Eigenparts are assigned to classes BY SIGN of their signed
    mass (exact split, nothing dropped); magnitudes are |mass|.
    NOTE (typed run-1 finding): the arch/pole block B is NEGATIVE
    definite in the 2-mode parity compression, so B1/B2 carry |B|
    magnitudes and the DPO partner is the dominant |B| direction
    (there is no positive structural leg in this compression)."""
    lam, nv, E = fd["lam"], fd["nv"], fd["E"]
    b_ev, Vb = np.linalg.eigh(fd["B"])
    i_dom = int(np.argmax(np.abs(b_ev)))
    b_dom_dir = Vb[:, i_dom].copy()
    b_dom_mag = abs(float(b_ev[i_dom]))
    dirs = [Vb[:, i_dom].copy(), Vb[:, 1 - i_dom].copy()]
    tags = ["B1", "B2"]
    mags = [b_dom_mag, abs(float(b_ev[1 - i_dom]))]

    def add_parts(M2, w, tag_p, tag_m):
        best_p, best_m = (0.0, None), (0.0, None)
        for e, v in eig_pairs(M2):
            val = w * e
            if val > 0:
                dirs.append(v)
                tags.append(tag_p)
                mags.append(val)
                if val > best_p[0]:
                    best_p = (val, v)
            elif val < 0:
                dirs.append(v)
                tags.append(tag_m)
                mags.append(-val)
                if -val > best_m[0]:
                    best_m = (-val, v)
        return best_p, best_m

    ev_parts = []
    for j in range(len(lam)):
        bp, bm = add_parts(E[j], float(lam[j]), "Y", "Z")
        ev_parts.append((bp[0], bp[1], bm[0], bm[1]))
    # non-prime-power mother sites (net-zero weight; |mu| mass)
    n_npp = 0
    for N in range(2, fd["X"] + 1):
        if is_pp(N, spf):
            continue
        wN = 0.0
        for d in divisors(N, spf):
            m = N // d
            if m >= 2 and mu_of(d, spf) != 0:
                wN += math.log(m)
        if wN <= 0:
            continue
        wN /= math.sqrt(N)
        add_parts(site_E(fd["rr"], math.log(N)), wN, "NPY", "NPZ")
        n_npp += 1
    # p-chain difference directions (n_j = p n_k both in support)
    idx = {int(n): j for j, n in enumerate(nv)}
    n_ch = 0
    for j, n in enumerate(nv):
        if int(n) < 2:
            continue                      # scramble guard
        f = factorize(int(n), spf)
        p = next(iter(f))
        if f[p] >= 2 and (int(n) // p) in idx:
            k = idx[int(n) // p]
            cj, zj = ev_parts[j][2], ev_parts[j][3]
            pk, yk = ev_parts[k][0], ev_parts[k][1]
            if cj > 0 and pk > 0:
                v = math.sqrt(cj) * zj - math.sqrt(pk) * yk
                nrm = float(np.linalg.norm(v))
                if nrm > 1e-14:
                    dirs.append(v / nrm)
                    tags.append("DCH")
                    mags.append(math.sqrt(cj * pk))
                    n_ch += 1
    # difference directions vs the dominant |B| leg
    for j in range(len(lam)):
        cj, zj = ev_parts[j][2], ev_parts[j][3]
        if cj > 0 and b_dom_mag > 0:
            v = math.sqrt(cj) * zj - math.sqrt(b_dom_mag) * b_dom_dir
            nrm = float(np.linalg.norm(v))
            if nrm > 1e-14:
                dirs.append(v / nrm)
                tags.append("DPO")
                mags.append(math.sqrt(cj * b_dom_mag))
    return dirs, tags, mags, ev_parts, n_npp, n_ch


def cone_lp(dirs, target):
    """min sum W s.t. sum W_r dir_r dir_r^T = target, W >= 0."""
    A = np.stack([sym3(m_of(v)) for v in dirs], axis=1)
    b = sym3(target)
    res = linprog(np.ones(A.shape[1]), A_eq=A, b_eq=b,
                  bounds=(0, None), method="highs")
    if not res.success:
        return False, np.inf, None
    resid = A @ res.x - b
    M = np.array([[resid[0], resid[2]], [resid[2], resid[1]]])
    return True, float(np.linalg.norm(M, 2)), res.x


def class_mats(dirs, tags, mags):
    """M_c = sum_{r in c} mag_r dir_r dir_r^T per frozen class."""
    out = {c: np.zeros((2, 2)) for c in CLASSES}
    for v, t, g in zip(dirs, tags, mags):
        out[t] += g * m_of(v)
    return out

# ---------------------------------------- probe-B (cell cone) frozen spec
FROZEN_SPEC_B = """\
PRIME.CELLCONE.TRANSPORT.01 spec v1 (2026-08-07, frozen before the
run).  Ladder: frame_a_zones minus h = 1292 (anomalous, v586) minus
incomplete combs (e^{2 alpha} > ATOM_MAX); full per-cell detail on
the 3 smallest-h rungs; controls on the stride-5 subset.  Objects:
Ah = B - S (shipped), tau = eig2_min(Ah); continuum model = v818
convention (U0 = 2 ln(-C_TH/4), C_TH = -2 zeta'(1/2)/zeta(1/2),
GRID_PER_D = 4, grid umax = 2 alpha + 1e-9, cumulative evaluated at
2 alpha); tau_pnt = eig2_min(B - S_pnt).  Completed flow: A_0 =
B - S_pnt; A_k = A_0 + sum_{j<=k} (Chat_j - lam_j Xhat_j); grouping
G1 = left Stieltjes intervals (U0, u_1], (u_1, u_2], ..., last cell
absorbs (u_{K-1}, 2 alpha]; G2 = mass-matched intervals e^{v_j/2} =
e^{U0/2} + 0.5 cumsum(mm)_j capped at 2 alpha, tail to last cell.
WARDS (all must pass; else INVALID): tau refs kz 9/12/13 =
5.984165e-4 / 4.351189e-4 / 5.637632e-4 rel <= 1e-4; envelope
e1 = (tau/tau_pnt) h^{3/2} >= 4.335*0.999 on ALL rungs; telescoping
|A_K - Ah|_max <= 1e-9 ||Ah||_max and |sum Chat - S_pnt|_max <=
1e-9 ||S_pnt||_max per rung per grouping; Phi spot identity
||Phi^T J Phi - c J||_max <= 1e-8 * max(c,1) and ||Phi L(A_k) -
L(A_{k+1})||max <= 1e-8 ||L(A_{k+1})|| on the spot cells (smallest
rung: cells 0, K/2, K-1, every 500th).  BARS: cone = lambda_min > 0
strictly at every cell incl. base; J-defect jdef_k =
det(A_{k+1})/det(A_k) - 1, violation iff jdef_k > JDEF_TOL = 1e-9;
MB_FRAC = 0.9 (incomplete contrast: fraction of rungs with cone
exit); CTRL_FRAC = 0.5 (controls, stride-5 subset); control fire =
[cone exit on >= CTRL_FRAC of subset rungs] OR [median over subset
of the path max |dnull| >= DNULL_FAC = 10 x the real completed
flow's]; RAY clause: RAY-EDGE-CONFIRMED iff Kendall(alpha, r_end)
>= 0.8 AND Kendall(alpha, angle_end to (5,-3,4)) <= -0.8 across the
ladder (sub-verdict only).  VERDICT (order): INVALID if any ward
fails or runtime > 1800 s; CELLS-PRESERVE-CONE iff both groupings
have zero cone exits and zero J-violations on all rungs AND
contrast >= MB_FRAC AND all must-break controls (C2, C3, C5) fire;
CONE-BROKEN iff both groupings exit the cone on >= 0.5 of rungs;
else CONE-PARTIAL (census typed: p = 2, k >= 2, p mod 4, u/2alpha
decile; control surprises named).  No prediction is frozen for the
per-cell J-census (measured as it falls); the incomplete contrast
is predicted to fire (mass-forced).  NO RH claim; writes nothing.
"""

GRID_PER_D = 4.0
STRIDE = 5
ANOMALOUS_H = 1292
ENV_C = 4.335
ENV_GUARD = 0.999
WARD_REL = 1.0e-9
PHI_REL = 1.0e-8
JDEF_TOL = 1.0e-9
MB_FRAC = 0.9
CTRL_FRAC = 0.5
DNULL_FAC = 10.0
KEN_BAR = 0.8
WRONG_FAC = 2.0
N_DETAIL = 3
RUNTIME_CAP = 1800.0
RAY = np.array([5.0, -3.0, 4.0])
J3 = np.diag([1.0, -1.0, -1.0])
BANNED_IDS = ("zetazero", "nzeros", "primerange", "isprime", "primepi",
              "nextprime", "prevprime", "find_zeros",
              "second_sheet_zero")

mp.dps = 30
C_TH = float(-2 * mpdiff(lambda s: zeta(s), 0.5) / zeta(0.5))
U0 = 2.0 * math.log(-C_TH / 4.0)

CHECKS = []
FAILS_B = []


def check_b(name, ok, detail=""):
    CHECKS.append((name, bool(ok)))
    if not ok:
        FAILS_B.append(name.split()[0])
    print("  [%s] %s%s" % ("PASS" if ok else "FAIL", name,
                           ("  -- " + detail) if detail else ""),
          flush=True)


def ast_zero_firewall(src_path):
    with open(src_path, "r", encoding="utf-8") as fh:
        tree = ast.parse(fh.read())
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            f = node.func
            nm = f.attr if isinstance(f, ast.Attribute) else (
                f.id if isinstance(f, ast.Name) else "")
            if nm in BANNED_IDS:
                return False
    return True


def kendall_tau(x, y):
    n = len(x)
    conc = disc = 0
    for i in range(n):
        for j in range(i + 1, n):
            s = (x[j] - x[i]) * (y[j] - y[i])
            if s > 0:
                conc += 1
            elif s < 0:
                disc += 1
    return (conc - disc) / max(n * (n - 1) // 2, 1)


def spf_sieve(nmax):
    """Own smallest-prime-factor sieve (census typing only)."""
    s = np.zeros(nmax + 1, dtype=np.int64)
    for p in range(2, int(math.isqrt(nmax)) + 1):
        if s[p] == 0:
            s[p * p::p] = np.where(s[p * p::p] == 0, p, s[p * p::p])
    for n in range(2, nmax + 1):
        if s[n] == 0:
            s[n] = n
    return s


# ------------------------------------------------- continuum machinery
def pnt_grid(rr):
    """The v818 pnt cell grid: edges + 2x2 spline reads per cell."""
    Mz, D, alpha = rr["M"], rr["D"], rr["alpha"]
    delta = D / GRID_PER_D
    umax = 2.0 * alpha + 1e-9
    n_cells = int(math.ceil((umax - U0) / delta))
    edges = U0 + delta * np.arange(n_cells + 1)
    reads = np.empty((n_cells, 3))
    for j in range(n_cells):
        u_j = 0.5 * (edges[j] + edges[j + 1])
        reads[j, 0] = core.spline_project(rr["W11"], u_j, D, Mz)
        reads[j, 1] = core.spline_project(rr["W22"], u_j, D, Mz)
        reads[j, 2] = core.spline_project(rr["W12"], u_j, D, Mz)
    return edges, reads


def cum_reads(edges, reads, bpts):
    """Exact cumulative continuum 2x2 read (as (n,3) triples) up to
    each breakpoint: full cells by prefix sum, boundary cell by the
    exact clipped mass 2(e^{u/2} - e^{edge/2})."""
    e_half = np.exp(edges / 2.0)
    m_full = 2.0 * (e_half[1:] - e_half[:-1])
    pref = np.vstack([np.zeros(3),
                      np.cumsum(m_full[:, None] * reads, axis=0)])
    b = np.asarray(bpts, float)
    idx = np.clip(np.searchsorted(edges, b, side="right") - 1,
                  0, len(reads) - 1)
    part = 2.0 * (np.exp(b / 2.0) - e_half[idx])
    return pref[idx] + part[:, None] * reads[idx]


def breaks_G1(uu, alpha):
    """Left Stieltjes pairing: cell j ends at u_j; last cell absorbs
    the tail to 2 alpha."""
    b = np.array(uu, float)
    b[-1] = 2.0 * alpha
    return b


def breaks_G2(mm, alpha):
    """Mass-matched (mu*log relational) pairing: e^{v_j/2} = e^{U0/2}
    + 0.5 cumsum(mm)_j, capped at 2 alpha; tail to last cell."""
    v = 2.0 * np.log(math.exp(U0 / 2.0) + 0.5 * np.cumsum(mm))
    v = np.minimum(v, 2.0 * alpha)
    v[-1] = 2.0 * alpha
    return v


def cell_increments(edges, reads, bpts):
    """Chat_j triples for a partition given by breakpoints (b_0 = U0
    implicit): exact, telescoping to the full S_pnt."""
    cum = cum_reads(edges, reads, bpts)
    out = np.empty_like(cum)
    out[0] = cum[0]
    out[1:] = np.diff(cum, axis=0)
    return out


# ------------------------------------------------- the flow engine
def path_stats(A0_tri, deltas):
    """Vectorized path of A_k = A0 + cumsum(deltas); returns per-state
    arrays (K+1 incl. base) of the Lorentz/cone quantities and the
    per-cell J-defects (K)."""
    a11 = A0_tri[0] + np.concatenate([[0.0], np.cumsum(deltas[:, 0])])
    a22 = A0_tri[1] + np.concatenate([[0.0], np.cumsum(deltas[:, 1])])
    a12 = A0_tri[2] + np.concatenate([[0.0], np.cumsum(deltas[:, 2])])
    t = a11 + a22
    x = a11 - a22
    y = 2.0 * a12
    det = a11 * a22 - a12 ** 2
    R = np.hypot(0.5 * x, a12)
    lmin = 0.5 * t - R
    lmax = 0.5 * t + R
    q = t * t - x * x - y * y
    nrm2 = t * t + x * x + y * y
    dnull = q / np.maximum(nrm2, 1e-300)
    uvec = np.stack([t, x, y], axis=1)
    cosr = (uvec @ RAY) / np.maximum(
        np.linalg.norm(uvec, axis=1) * np.linalg.norm(RAY), 1e-300)
    ang = np.degrees(np.arccos(np.clip(cosr, -1.0, 1.0)))
    with np.errstate(divide="ignore", invalid="ignore"):
        jdef = det[1:] / np.where(det[:-1] != 0.0, det[:-1], np.nan) - 1.0
    r_dom = np.where(np.abs(a12) > 1e-300,
                     (lmax - a11) / np.where(a12 != 0.0, a12, 1.0),
                     np.where(a11 >= a22, 0.0, np.inf))
    return dict(a11=a11, a22=a22, a12=a12, t=t, det=det, lmin=lmin,
                lmax=lmax, dnull=dnull, ang=ang, jdef=jdef, r=r_dom)


def flow_summary(ps):
    lmin = ps["lmin"]
    cone_ok = bool(np.all(lmin > 0.0))
    first_exit = int(np.argmax(lmin <= 0.0)) if not cone_ok else -1
    out = lmin <= 0.0
    n_out = int(out.sum())
    last_out = int(len(out) - 1 - np.argmax(out[::-1])) if n_out else -1
    runs = 0
    if n_out:
        d = np.diff(out.astype(int))
        starts = np.where(d == 1)[0]
        runs = len(starts) + (1 if out[0] else 0)
    jd = ps["jdef"]
    valid = np.isfinite(jd)
    nviol = int(np.sum(jd[valid] > JDEF_TOL))
    return dict(cone_ok=cone_ok, first_exit=first_exit,
                n_out=n_out, frac_out=n_out / max(len(out), 1),
                last_out=last_out, n_out_runs=runs,
                min_lmin=float(np.min(lmin)),
                min_rel=float(np.min(lmin / np.maximum(ps["lmax"],
                                                       1e-300))),
                nviol=nviol, ncell=int(len(jd)),
                frac_viol=nviol / max(len(jd), 1),
                worst_jdef=float(np.nanmax(jd)) if len(jd) else 0.0,
                max_dnull=float(np.max(np.abs(ps["dnull"]))),
                dnull_end=float(ps["dnull"][-1]),
                r_end=float(ps["r"][-1]), ang_end=float(ps["ang"][-1]),
                ang_min=float(np.min(ps["ang"])),
                ang_argmin=float(np.argmin(ps["ang"]) /
                                 max(len(ps["ang"]) - 1, 1)))


# ------------------------------------------------- the Phi spot gate
def sqrt2(A):
    w, V = np.linalg.eigh(A)
    return V @ np.diag(np.sqrt(np.maximum(w, 0.0))) @ V.T


def tri_mat(tri):
    return np.array([[tri[0], tri[2]], [tri[2], tri[1]]])


def lorentz_of(M):
    """The 3x3 Lorentz action of the congruence X -> M^T X M in the
    (t, x, y) coordinates."""
    basis = (0.5 * np.eye(2), 0.5 * np.diag([1.0, -1.0]),
             np.array([[0.0, 0.5], [0.5, 0.0]]))
    Phi = np.empty((3, 3))
    for i, E in enumerate(basis):
        Y = M.T @ E @ M
        Phi[:, i] = (Y[0, 0] + Y[1, 1], Y[0, 0] - Y[1, 1],
                     2.0 * Y[0, 1])
    return Phi


def phi_spot(Aprev, Anext):
    """M_k, Phi_k and the exact-identity residuals for one cell.
    Returns None when the map does not exist (state not PD -- exactly
    the cone-exit event the census measures; declared robustness
    guard, no bar changed)."""
    if float(np.linalg.eigvalsh(Aprev)[0]) <= 0.0 \
            or float(np.linalg.eigvalsh(Anext)[0]) <= 0.0:
        return None
    S = sqrt2(Aprev)
    Sinv = np.linalg.inv(S)
    IA = np.eye(2) + Sinv @ (Anext - Aprev) @ Sinv
    wmin = float(np.linalg.eigvalsh(IA)[0])
    if wmin <= 0.0:
        return None
    M = Sinv @ sqrt2(IA) @ S
    Phi = lorentz_of(M)
    c = float(np.linalg.det(M)) ** 2
    res_id = float(np.max(np.abs(Phi.T @ J3 @ Phi - c * J3)))
    uP = np.array([Aprev[0, 0] + Aprev[1, 1], Aprev[0, 0] - Aprev[1, 1],
                   2.0 * Aprev[0, 1]])
    uN = np.array([Anext[0, 0] + Anext[1, 1], Anext[0, 0] - Anext[1, 1],
                   2.0 * Anext[0, 1]])
    res_map = float(np.max(np.abs(Phi @ uP - uN))) \
        / max(float(np.max(np.abs(uN))), 1e-300)
    lam_lit = float(np.max(np.linalg.eigvalsh(Phi.T @ J3 @ Phi - J3)))
    return dict(c=c, res_id=res_id, res_map=res_map, lam_lit=lam_lit)


# ------------------------------------------------- controls: Epstein
def epstein_atoms(alpha):
    """Atoms of the x^2 + 5 y^2 comb (n >= 2 represented): positions
    log n, raw masses r_Q(n)/sqrt(n) (v818 recipe, verbatim)."""
    Nmax = int(math.floor(math.exp(2.0 * alpha)))
    cnt = np.zeros(Nmax + 1)
    for xx in range(0, int(math.isqrt(Nmax)) + 1):
        rem = Nmax - xx * xx
        if rem < 0:
            break
        yy = np.arange(0, int(math.isqrt(rem // 5)) + 1)
        n = xx * xx + 5 * yy * yy
        mult = (2.0 if xx > 0 else 1.0) * np.where(yy > 0, 2.0, 1.0)
        np.add.at(cnt, n, mult)
    nn = np.nonzero(cnt[2:])[0] + 2
    return np.log(nn.astype(float)), cnt[nn] / np.sqrt(nn.astype(float))


def atom_reads(rr, uuX):
    """Per-atom 2x2 spline reads at custom positions (the build_window
    Xn recipe at explicit u)."""
    Mz, D = rr["M"], rr["D"]
    out = np.empty((len(uuX), 3))
    for i, u in enumerate(uuX):
        out[i, 0] = core.spline_project(rr["W11"], u, D, Mz)
        out[i, 1] = core.spline_project(rr["W22"], u, D, Mz)
        out[i, 2] = core.spline_project(rr["W12"], u, D, Mz)
    return out


def eig2_min(A):
    return float(np.linalg.eigvalsh(A)[0])


# ====== PART A -- relational_lagrange_probe.py (frozen probe, verbatim)
def part_a():
    global N_CHK, FAILS_A, T0
    T0 = time.time()
    N_CHK = 0
    FAILS_A = []
    print("=" * 78)
    print("RELATIONAL LAGRANGE (relational_lagrange_probe) -- the "
          "sign-register wedge on the lock block")
    print("=" * 78)
    print("""
HONESTY FRAME: NO RH claim; prime side only (no zeros anywhere).
Three-level typing is forced by the 2x2 compression: canonical
weights (level A, the naive no-go), free per-frame weights (level
B, the lift's existence question), one relational law across
frames (level C, the substance).  Design frames kz 9, 12;
held-out validation kz 13.""")

    # ============================================================== S0
    print("\nS0 -- lock block conventions + wards")
    spf = sieve_spf(4096)
    fds = {kz: frame_data(kz) for kz in ANCHORS}
    for kz in ANCHORS:
        fd = fds[kz]
        lam, Xn = fd["lam"], np.asarray(fd["rr"]["Xn"], float)
        C = np.array([[np.sum(lam * Xn[:, 0]), np.sum(lam * Xn[:, 2])],
                      [np.sum(lam * Xn[:, 2]), np.sum(lam * Xn[:, 1])]])
        dev = float(np.max(np.abs(fd["B"] - C - fd["Ah"]))) \
            / max(1.0, float(np.max(np.abs(fd["B"]))))
        ok_tau = abs(fd["tau"] / TAU_REFS[kz] - 1.0) <= TAU_REF_REL
        check("S0.ID kz=%d: Ah == B - sum lam Xn (rel %.1e <= %.0e) "
              "AND tau = %.6e vs frozen ref (rel %.1e <= %.0e)"
              % (kz, dev, ID_BAR, fd["tau"],
                 abs(fd["tau"] / TAU_REFS[kz] - 1.0), TAU_REF_REL),
              dev <= ID_BAR and ok_tau)
    # lambda convention + mother pair (exact relational address)
    fd9 = fds[9]
    devl = 0.0
    for j, n in enumerate(fd9["nv"]):
        f = factorize(int(n), spf)
        p, a = next(iter(f.items()))
        devl = max(devl, abs(fd9["lam"][j] * math.sqrt(n)
                             / math.log(p) - 1.0))
    check("S0.LAM lam_j == Lambda(n)/sqrt(n) on kz=9 (worst rel "
          "%.1e <= 1e-9) -- mother pair (1, p^a)[+a log p] + "
          "(p, p^(a-1))[-(a-1) log p] nets Lambda exactly" % devl,
          devl <= 1.0e-9)
    # exact mu*log ward on integer exponent vectors, all n <= X13
    X13 = fds[13]["X"]
    ok_ml = True
    for n in range(2, X13 + 1):
        acc = {}
        for d in divisors(n, spf):
            mu = mu_of(d, spf)
            if mu == 0:
                continue
            for p, a in factorize(n // d, spf).items():
                acc[p] = acc.get(p, 0) + mu * a
        acc = {p: c for p, c in acc.items() if c != 0}
        f = factorize(n, spf)
        want = {next(iter(f)): 1} if len(f) == 1 else {}
        ok_ml &= (acc == want)
    check("S0.MUL [EXACT] mu * log == Lambda on integer exponent "
          "vectors for ALL n <= %d (incl. zero at every non-prime-"
          "power -- the mother space's net-zero sites)" % X13, ok_ml)

    # ============================================================== S1
    print("\nS1 -- LEVEL A: the naive signed Lagrange (canonical "
          "weights, the exact no-go)")
    # sympy uniqueness lemma (generic 3-atom family, exact)
    a1, a2, a3, b1, b2, b3, w1, w2, w3 = sp.symbols(
        "a1 a2 a3 b1 b2 b3 w1 w2 w3")
    vv = [(a1, b1), (a2, b2), (a3, b3)]
    ww = [w1, w2, w3]
    M = sp.zeros(2, 2)
    for (av, bv), wv in zip(vv, ww):
        M += wv * sp.Matrix([[av * av, av * bv], [av * bv, bv * bv]])
    pair_sum = sum(ww[i] * ww[j]
                   * (vv[i][0] * vv[j][1] - vv[j][0] * vv[i][1]) ** 2
                   for i in range(3) for j in range(i + 1, 3))
    lem1 = sp.simplify(sp.expand(M.det() - pair_sum)) == 0
    wedges = [sp.expand((vv[i][0] * vv[j][1]
                         - vv[j][0] * vv[i][1]) ** 2)
              for i in range(3) for j in range(i + 1, 3)]
    pts = [(1, 2, 3, 5, 7, 11), (2, 3, 5, 7, 11, 13),
           (1, 1, 2, 3, 5, 8), (3, 1, 4, 1, 5, 9),
           (2, 7, 1, 8, 2, 8), (1, 4, 1, 4, 2, 1)]
    rows = []
    for pt in pts:
        sub = dict(zip((a1, a2, a3, b1, b2, b3), pt))
        rows.append([int(wq.subs(sub)) for wq in wedges])
    rk = np.linalg.matrix_rank(np.array(rows, float))
    check("S1.LEM [SYMBOLIC] Lagrange identity exact (det == pair "
          "sum: %s) AND the wedge squares are linearly independent "
          "(rank %d = 3) => the pair weights are FORCED W_rs = "
          "w_r w_s: over a fixed signed family NO reweighting can "
          "make the expansion nonneg" % (lem1, rk),
          lem1 and rk == 3)
    for kz in ANCHORS:
        fd = fds[kz]
        comps, ctag = [], []     # EXACT signed rank-one family
        b_ev, Vb = np.linalg.eigh(fd["B"])
        comps += [(float(b_ev[1]), Vb[:, 1]),
                  (float(b_ev[0]), Vb[:, 0])]
        ctag += ["B", "B"]
        for j in range(len(fd["lam"])):
            for e, v in eig_pairs(fd["E"][j]):
                w = float(fd["lam"][j]) * e
                if w != 0.0:
                    comps.append((w, v))
                    ctag.append("E+" if w > 0 else "E-")
        Wv = np.array([c[0] for c in comps])
        Vm = np.stack([c[1] for c in comps])
        S_chk = (Vm.T * Wv) @ Vm
        wedge = Vm[:, 0][:, None] * Vm[:, 1][None, :] \
            - Vm[:, 1][:, None] * Vm[:, 0][None, :]
        PW = np.triu(np.outer(Wv, Wv) * wedge ** 2, 1)
        det_pair = float(np.sum(PW))
        det_true = float(np.linalg.det(fd["Ah"]))
        pos = float(np.sum(PW[PW > 0]))
        neg = -float(np.sum(PW[PW < 0]))
        dev = abs(det_pair - det_true)
        bar = max(LAG_BAR * abs(det_true), 1e-12 * (pos + neg))
        rec = float(np.max(np.abs(S_chk - fd["Ah"]))) \
            / max(1.0, float(np.max(np.abs(fd["Ah"]))))
        isB = np.array([t == "B" for t in ctag])
        negBmask = (PW < 0) & (isB[:, None] | isB[None, :])
        negB = -float(np.sum(PW[negBmask]))
        check("S1.WARD kz=%d signed Lagrange: family rebuilds Ah "
              "(rel %.1e) AND det Ah == signed pair sum (dev %.1e "
              "<= %.1e float budget); P+ = %.3e, P- = %.3e "
              "(P-/det = %.1f; %.0f%% of P- involves the NEGATIVE-"
              "definite arch block B) -- the naive negative mass "
              "is REAL and forced"
              % (kz, rec, dev, bar, pos, neg, neg / det_true,
                 100.0 * negB / max(neg, 1e-300)),
              rec <= 1e-9 and dev <= bar and neg > 0)

    # ============================================================== S2
    print("\nS2 -- the sign-register mechanism (symbolic) + the "
          "lifted family census")
    x1, x2, y1, y2 = sp.symbols("x1 x2 y1 y2")
    av = sp.Matrix([x1, x2])
    bv = sp.Matrix([y1, y2])
    vfull = sp.Matrix([x1, x2, y1, y2])      # e+ (x) a + e- (x) b
    chiI = sp.Matrix([[1, 0, -1, 0], [0, 1, 0, -1]]) / sp.sqrt(2)
    comp = chiI * vfull
    lhs = sp.expand(comp * comp.T)
    rhs = sp.expand((av - bv) * (av - bv).T / 2)
    cross = sp.expand(rhs - (av * av.T + bv * bv.T) / 2)
    mech_ok = sp.simplify(lhs - rhs) == sp.zeros(2, 2)
    check("S2.MECH [SYMBOLIC] the C2 sign register: the coherent "
          "mother atom e+ (x) a + e- (x) b compresses under chi = "
          "(1,-1)/sqrt2 to (a-b)(a-b)^T/2; the Moebius MINUS "
          "re-enters exactly as the completed square's cross term "
          "-(ab^T + ba^T)/2 -- sign -> difference geometry, the "
          "input class the position-blind no-go never saw",
          mech_ok, "cross = %s" % sp.srepr(cross[0, 1])[:60])
    print("    mechanism report: which pairs acquire the register "
          "treatment --")
    print("      within one event n = p^a the mother pair shares "
          "ONE read matrix E_n: wedge = 0, the completion is "
          "trivial (net weight Lambda);")
    print("      the negative arithmetic mass at (p, p^(a-1)) is "
          "chain-addressed: partner = the event p^(a-1) (DCH "
          "class) and the dominant |B| leg (DPO class);")
    print("      the analytic eigen-negativity z_j (source (i)) "
          "is what the naive SOS pays for -- the lift's new "
          "material is DCH/DPO differences + the net-zero non-pp "
          "mother sites (NPY/NPZ).")
    bev9 = np.linalg.eigvalsh(fds[9]["B"])
    print("    TYPED RUN-1 FINDING: the arch/pole block B is "
          "NEGATIVE definite in this compression (kz=9 eigen "
          "%.3f, %.3f) -- the naive negative mass includes the "
          "ENTIRE structural block; a manifestly nonneg wedge "
          "family must rebuild even B from comb material"
          % (float(bev9[0]), float(bev9[1])))
    fams = {}
    for kz in ANCHORS:
        fams[kz] = lifted_family(fds[kz], spf)
        dirs, tags, mags, _, n_npp, n_ch = fams[kz]
        cnt = {c: tags.count(c) for c in CLASSES}
        print("    kz=%d family: %d directions (%s); %d non-pp "
              "mother sites, %d p-chain pairs"
              % (kz, len(dirs),
                 " ".join("%s %d" % (c, cnt[c]) for c in CLASSES),
                 n_npp, n_ch))

    # ============================================================== S3
    print("\nS3 -- LEVEL B: per-frame cone feasibility (free "
          "nonneg weights)")
    lift_ok_all = True
    for kz in ANCHORS:
        fd = fds[kz]
        dirs, tags, mags, ev_parts, _, _ = fams[kz]
        naive = [v for v, t in zip(dirs, tags)
                 if t in ("B1", "B2", "Y")]
        okN, rN, _ = cone_lp(naive, fd["Ah"])
        okL, rL, WL = cone_lp(dirs, fd["Ah"])
        gateN = okN and rN <= FLOOR_FAC * fd["tau"]
        gateL = okL and rL <= FLOOR_FAC * fd["tau"]
        lift_ok_all &= gateL
        act = {}
        if WL is not None:
            for t, w in zip(tags, WL):
                if w > 1e-12:
                    act[t] = act.get(t, 0) + 1
        print("    kz=%d: naive-positive cone %s (resid %.1e vs "
              "floor bar %.1e) | LIFTED cone %s (resid %.1e) -- "
              "active classes %s"
              % (kz, "FEASIBLE" if gateN else "infeasible/short",
                 rN, FLOOR_FAC * fd["tau"],
                 "FEASIBLE" if gateL else "infeasible/short", rL,
                 act))
    check("S3.B level B: the lifted family's cone contains Ah at "
          "floor grade on all anchors -- nonneg wedge weights "
          "EXIST pointwise (the decisive existence answer)",
          lift_ok_all)

    # ============================================================== S4
    print("\nS4 -- LEVEL C: the relational LAW (one theta across "
          "frames; design 9+12, held-out 13)")
    A_rows, b_rows = [], []
    for kz in DESIGN:
        mats = class_mats(*fams[kz][:3])
        A_rows.append(np.stack([sym3(mats[c]) for c in CLASSES],
                               axis=1))
        b_rows.append(sym3(fds[kz]["Ah"]))
    A_d = np.vstack(A_rows)
    b_d = np.concatenate(b_rows)
    theta, _ = nnls(A_d, b_d)
    print("    theta (NNLS, >= 0): %s"
          % "  ".join("%s %.3e" % (c, t)
                      for c, t in zip(CLASSES, theta)))
    grades = {}
    for kz in ANCHORS:
        mats = class_mats(*fams[kz][:3])
        S = sum(theta[i] * mats[c] for i, c in enumerate(CLASSES))
        R = S - fds[kz]["Ah"]
        r2 = float(np.linalg.norm(R, 2))
        rel = r2 / float(np.linalg.norm(fds[kz]["Ah"], 2))
        grades[kz] = (rel, r2, R)
        print("    kz=%d %s: rel resid %.3e (formula bar %.2f) | "
              "||resid||/tau = %.2e (floor bar %.2f)"
              % (kz, "design " if kz in DESIGN else "HELD-OUT",
                 rel, FORMULA_REL, r2 / fds[kz]["tau"], FLOOR_FAC))
    c_formula = all(g[0] <= FORMULA_REL for g in grades.values())
    c_floor = all(g[1] <= FLOOR_FAC * fds[kz]["tau"]
                  for kz, g in grades.items())
    print("    LEVEL C DECISION (feeds the verdict, not a ward): "
          "formula grade %s (<= %.2f rel on design AND held-out), "
          "floor grade %s" % (c_formula, FORMULA_REL, c_floor))
    # where does uniformity die: the same 8-class law solved
    # PER FRAME (3 eq, 8 unknowns -- the class granularity alone)
    for kz in ANCHORS:
        mats = class_mats(*fams[kz][:3])
        A_f = np.stack([sym3(mats[c]) for c in CLASSES], axis=1)
        th_f, _ = nnls(A_f, sym3(fds[kz]["Ah"]))
        r_f = float(np.linalg.norm(A_f @ th_f
                                   - sym3(fds[kz]["Ah"])))
        print("    kz=%d per-frame class law: resid %.2e "
              "(/tau %.1e) -- the 8-class granularity %s reach "
              "floor grade even frame-wise"
              % (kz, r_f, r_f / fds[kz]["tau"],
                 "CAN" if r_f <= FLOOR_FAC * fds[kz]["tau"]
                 else "CANNOT"))
    print("    honest resolution statement: the floor lives at "
          "tau/||Ah|| = %.1e -- the held-out law residual sits "
          "%.1f orders ABOVE what a wedge floor certificate "
          "needs"
          % (fds[13]["tau"] / float(np.linalg.norm(fds[13]["Ah"],
                                                   2)),
             math.log10(max(grades[13][1]
                            / (FLOOR_FAC * fds[13]["tau"]),
                            1e-300))))

    # ============================================================== S5
    print("\nS5 -- controls")
    fd_s = frame_data(9, scramble=SCR_SEED)
    fam_s = lifted_family(fd_s, spf)
    mats_s = class_mats(*fam_s[:3])
    S_s = sum(theta[i] * mats_s[c] for i, c in enumerate(CLASSES))
    r_s = float(np.linalg.norm(S_s - fd_s["Ah"], 2))
    base9 = max(grades[9][1], 1e-12 * float(
        np.linalg.norm(fds[9]["Ah"], 2)))
    _scr_ratio = r_s / base9
    check("S5.SCR scramble (seed %d) blows the level-C residual: "
          "%.3e vs true %.3e (x%.1f >= %.0f) -- the law is comb-"
          "structure-specific" % (SCR_SEED, r_s, grades[9][1],
                                  _scr_ratio, SCR_BLOW),
          _scr_ratio >= SCR_BLOW)
    # Epstein h=2: signed off-pp Lambda_F (Euler sensitivity)
    XE = 258
    rq = np.zeros(XE + 1)
    for x in range(0, int(math.isqrt(XE)) + 1):
        for y in range(0, int(math.isqrt(max(XE - x * x, 0) // 5))
                       + 1):
            n = x * x + 5 * y * y
            if 2 <= n <= XE:
                rq[n] += (2 if x > 0 else 1) * (2 if y > 0 else 1)
    aE = rq / 2.0
    aE[1] = 1.0

    def lam_F(a):
        LF = np.zeros(XE + 1)
        for n in range(2, XE + 1):
            s = a[n] * math.log(n)
            for d in divisors(n, spf)[:-1]:
                if d >= 2:
                    s -= LF[d] * a[n // d]
            LF[n] = s / a[1] if a[1] != 0 else 0.0
        return LF

    LF_E = lam_F(aE)
    LF_Z = lam_F(np.ones(XE + 1))
    offE = sum(abs(LF_E[n]) for n in range(2, XE + 1)
               if not is_pp(n, spf))
    negE = sum(1 for n in range(2, XE + 1)
               if LF_E[n] < -1e-9)
    offZ = sum(abs(LF_Z[n]) for n in range(2, XE + 1)
               if not is_pp(n, spf))
    check("S5.EPS Epstein x^2+5y^2 (h = 2): off-prime-power "
          "Lambda_F mass %.2f > 0 with %d NEGATIVE sites (its "
          "mother weights are signed/negative -- no Euler product, "
          "the relational lift is zeta-specific); zeta comb "
          "off-pp mass %.1e == 0" % (offE, negE, offZ),
          offE > EPS_OFFPP and negE > 0 and offZ <= 1e-9)

    # ============================================================== S6
    print("\nS6 -- verdict")
    # exactness/mechanism wards block the translation; control
    # bar misses are typed in the verdict text, not converted
    # into a translation block
    wards_ok = not any(k.startswith(("S0.", "S1.", "S2."))
                       for k in FAILS_A)
    persist = None
    if c_floor and lift_ok_all:
        n_pass, n_all = 0, 0
        for kz in core.frame_a_zones():
            al = float(core.U_ALL[kz])
            if math.exp(2.0 * al) > LADDER_XMAX:
                continue
            fd = frame_data(kz)
            fam = lifted_family(fd, spf)
            mats = class_mats(*fam[:3])
            S = sum(theta[i] * mats[c]
                    for i, c in enumerate(CLASSES))
            r = float(np.linalg.norm(S - fd["Ah"], 2))
            n_all += 1
            n_pass += (r <= FLOOR_FAC * fd["tau"])
        persist = n_pass / max(n_all, 1)
        print("    ladder persistence (X <= %.0f): %d/%d = %.2f"
              % (LADDER_XMAX, n_pass, n_all, persist))
    if not wards_ok:
        verdict = "WEDGE-TRANSLATION-BLOCKED"
    elif c_floor and lift_ok_all and persist is not None \
            and persist >= PERSIST_MIN:
        verdict = "RELATIONAL-WEDGE-CLOSES"
    elif c_floor and lift_ok_all:
        verdict = "WEDGE-LOCK-ONLY"
    elif lift_ok_all:
        verdict = "WEDGE-PARTIAL"
    else:
        verdict = "WEDGE-OBSTRUCTED"
    print("=" * 78)
    print("V -- VERDICT: %s" % verdict)
    print("=" * 78)
    if verdict == "WEDGE-PARTIAL":
        R13 = grades[13][2]
        print("""    THE TYPED OUTCOME: the sign-register lift WORKS at the
    existence level -- nonneg wedge weights exist on every anchor
    (level B feasible at floor grade), where the naive signed
    family PROVABLY cannot (level A: forced weights, P- > 0,
    ~25-31%% of it carried by the NEGATIVE-definite arch block).
    The decisive question of task 1 answers YES.  What fails is
    the RELATIONAL LAW (level C): one frozen theta across frames
    reaches only ~15%% relative (formula grade %s), and the floor
    needs the identity ~4.5 orders deeper; the held-out residual
    in (a11, a22, a12) coordinates is %s.
    OBSTRUCTION COMPARISON (task 4): this is the commutant no-go
    TRANSPORTED, not a new obstruction: there the unique
    position-blind Gram G = diag(1,-1,-1) failed PSD (constant
    certificates die, pointwise ones exist); here pointwise
    nonneg wedge certificates EXIST per frame but the frame-
    uniform relational law cannot reach floor grade -- in both
    routes the wall is UNIFORMITY IN THE WINDOW, not the sign.
    The Moebius sign is fully absorbable by the C2 register (the
    mechanism is exact algebra); the residual hardness is the
    window-analytic eigen-negativity of the reads, which is
    position-dependent in exactly the way constant laws cannot
    track.  CONTROL NOTE: the scramble contrast measured x%.1f
    against the frozen x%.0f bar -- a law that itself only
    reaches ~15%% has bounded structure to break; the miss is
    typed, not excused.  HONEST CONSEQUENCE: work package C does
    not deliver a second proof architecture; it delivers the
    sharpened statement that BOTH failed routes die on the same
    uniformity wall -- the named next object would be an
    h-DEPENDENT (but analytically controlled) weight law, not a
    constant one."""
              % (c_formula,
                 np.array2string(sym3(R13), precision=2),
                 _scr_ratio, SCR_BLOW))
    _VERDICTS["a"] = verdict
    dt_run = time.time() - T0
    print("-" * 78)
    print("checks: %d run, %d failed%s | runtime %.1f min"
          % (N_CHK, len(FAILS_A),
             (" [" + ", ".join(FAILS_A) + "]") if FAILS_A else "",
             dt_run / 60.0))
    print("NO RH claim; report only; nothing outside experiments/ "
          "touched.")


# ====== PART B -- cell_cone_transport_probe.py (frozen probe, verbatim)
def part_b():
    global T0
    T0 = time.time()
    spec_hash = hashlib.sha256(FROZEN_SPEC_B.encode()).hexdigest()
    g1_hash = hashlib.sha256(
        inspect.getsource(breaks_G1).encode()).hexdigest()
    g2_hash = hashlib.sha256(
        inspect.getsource(breaks_G2).encode()).hexdigest()
    print("=" * 78)
    print("PRIME.CELLCONE.TRANSPORT.01 -- completed cells as Lorentz "
          "cone transport")
    print("=" * 78)
    print(FROZEN_SPEC_B)
    print("SPEC sha256   : %s" % spec_hash)
    print("G1 rule sha256: %s" % g1_hash)
    print("G2 rule sha256: %s" % g2_hash)
    print("U0 = %.6f (C_TH = %.6f)" % (U0, C_TH))

    # ============================================================== S0
    print("\nS0 -- firewall")
    check_b("S0.AST no zero/prime-table loader (banned ids absent); "
          "mpmath = the zero-free constant C_TH only; no RNG anywhere",
          ast_zero_firewall(__file__))

    # ============================================================== S1
    print("\nS1 -- ladder + wards")
    rows = []
    for kz in core.frame_a_zones():
        rr = core.build_window(kz)
        if rr["h"] == ANOMALOUS_H:
            continue
        if math.exp(2.0 * rr["alpha"]) > core.ATOM_MAX + 0.5:
            continue
        rows.append(dict(rr=rr, kz=kz, h=rr["h"], alpha=rr["alpha"],
                         tau=eig2_min(rr["Ah"])))
    rows.sort(key=lambda w: w["alpha"])
    print("    %d regular complete rungs, alpha %.3f..%.3f, h %d..%d"
          % (len(rows), rows[0]["alpha"], rows[-1]["alpha"],
             min(w["h"] for w in rows), max(w["h"] for w in rows)))

    ref_ok = True
    ref_txt = []
    for kz, tref in TAU_REFS.items():
        tk = eig2_min(core.build_window(kz)["Ah"])
        rel = abs(tk - tref) / tref
        ref_ok = ref_ok and rel <= TAU_REF_REL
        ref_txt.append("kz%d %.6e (rel %.1e)" % (kz, tk, rel))
    check_b("S1.REF tau references reproduce margin_law: %s (bar %.0e)"
          % ("; ".join(ref_txt), TAU_REF_REL), ref_ok)

    # continuum grids + envelope ward + telescoping wards per rung
    env_min = float("inf")
    tel_worst = 0.0
    cw_worst = 0.0
    for w in rows:
        rr = w["rr"]
        edges, reads = pnt_grid(rr)
        w["edges"], w["reads"] = edges, reads
        S_pnt = tri_mat(cum_reads(edges, reads,
                                  [2.0 * rr["alpha"]])[0])
        w["S_pnt"] = S_pnt
        A0 = rr["B"] - S_pnt
        w["A0"] = A0
        w["tau_pnt"] = eig2_min(A0)
        e1 = (w["tau"] / w["tau_pnt"]) * w["h"] ** 1.5
        w["e1"] = e1
        env_min = min(env_min, e1)
        uu, lam, Xn = rr["uu"], rr["lam"], rr["Xn"]
        w["mm"] = 2.0 * lam
        for gname in ("G1", "G2"):
            b = (breaks_G1(uu, rr["alpha"]) if gname == "G1"
                 else breaks_G2(w["mm"], rr["alpha"]))
            Chat = cell_increments(edges, reads, b)
            csum = Chat.sum(axis=0)
            cw = float(np.max(np.abs(tri_mat(csum) - S_pnt))) \
                / max(float(np.max(np.abs(S_pnt))), 1e-300)
            cw_worst = max(cw_worst, cw)
            deltas = Chat - lam[:, None] * Xn
            A0t = (A0[0, 0], A0[1, 1], A0[0, 1])
            ps = path_stats(A0t, deltas)
            Aend = tri_mat((ps["a11"][-1], ps["a22"][-1],
                            ps["a12"][-1]))
            tel = float(np.max(np.abs(Aend - rr["Ah"]))) \
                / max(float(np.max(np.abs(rr["Ah"]))), 1e-300)
            tel_worst = max(tel_worst, tel)
            w[gname] = dict(breaks=b, deltas=deltas, ps=ps,
                            summ=flow_summary(ps))
    check_b("S1.ENV the certified envelope reproduces: min e1 = %.4f >= "
          "%.4f (= %.3f x %.3f) on all %d rungs"
          % (env_min, ENV_C * ENV_GUARD, ENV_C, ENV_GUARD, len(rows)),
          env_min >= ENV_C * ENV_GUARD)
    check_b("S1.TEL the completed flow TELESCOPES exactly per rung per "
          "grouping: worst |A_K - Ah| rel %.2e and worst "
          "|sum Chat - S_pnt| rel %.2e (bar %.0e) -- the completed "
          "cells are a PARTITION of the certified objects"
          % (tel_worst, cw_worst, WARD_REL),
          tel_worst <= WARD_REL and cw_worst <= WARD_REL)

    # Phi spot identity gate (smallest rung, G1)
    w0 = rows[0]
    ps0 = w0["G1"]["ps"]
    K0 = len(w0["G1"]["deltas"])
    spots = sorted(set([0, K0 // 2, K0 - 1]
                       + list(range(0, K0, 500))))
    worst_id = worst_map = 0.0
    lit_lines = []
    n_spot = 0
    for k in spots:
        Ap = tri_mat((ps0["a11"][k], ps0["a22"][k], ps0["a12"][k]))
        An = tri_mat((ps0["a11"][k + 1], ps0["a22"][k + 1],
                      ps0["a12"][k + 1]))
        sp = phi_spot(Ap, An)
        if sp is None:
            continue
        n_spot += 1
        worst_id = max(worst_id, sp["res_id"] / max(sp["c"], 1.0))
        worst_map = max(worst_map, sp["res_map"])
        if len(lit_lines) < 4:
            lit_lines.append("cell %d: c = %.6f, lam_max(Phi^TJPhi-J) "
                             "= %+.2e (= max(c-1,1-c) as derived)"
                             % (k, sp["c"], sp["lam_lit"]))
    check_b("S1.PHI the congruence/Lorentz identity holds on %d spot "
          "cells (smallest rung): worst ||Phi^TJPhi - cJ|| rel %.1e, "
          "worst |Phi L(A_k) - L(A_{k+1})| rel %.1e (bar %.0e)"
          % (n_spot, worst_id, worst_map, PHI_REL),
          worst_id <= PHI_REL and worst_map <= PHI_REL)
    print("    HONESTY (the literal J-inequality): "
          + "; ".join(lit_lines))
    print("    -> the frozen J-contractivity reading is ON-CONE: "
          "jdef = det-ratio - 1 <= 0.")

    # ============================================================== S2
    print("\nS2 -- the completed flow, per-rung census (both groupings)")
    spf = spf_sieve(int(core.ATOM_MAX) + 1)
    for gname in ("G1", "G2"):
        print("\n  grouping %s:" % gname)
        print("    %5s %7s %6s | %5s %10s %8s | %5s %6s %5s | %6s "
              "%8s | %7s %7s"
              % ("h", "alpha", "K", "cone", "min_lmin", "min_rel",
                 "n_out", "f_out", "1st", "nJvio", "fracJ",
                 "r_end", "ang_end"))
        for w in rows:
            s = w[gname]["summ"]
            print("    %5d %7.3f %6d | %5s %10.2e %8.1e | %5d %6.3f "
                  "%5d | %6d %8.4f | %7.4f %7.3f"
                  % (w["h"], w["alpha"], s["ncell"],
                     "IN" if s["cone_ok"] else "EXIT",
                     s["min_lmin"], s["min_rel"], s["n_out"],
                     s["frac_out"], s["first_exit"], s["nviol"],
                     s["frac_viol"], s["r_end"], s["ang_end"]))
    # per-cell detail on the smallest rungs (G1)
    print("\n  per-cell detail, %d smallest rungs (G1): first 12 cells "
          "+ 5 worst-jdef cells" % N_DETAIL)
    for w in sorted(rows, key=lambda v: v["h"])[:N_DETAIL]:
        ps = w["G1"]["ps"]
        jd = w["G1"]["ps"]["jdef"]
        uu = w["rr"]["uu"]
        nn = np.rint(np.exp(uu)).astype(np.int64)
        print("    rung h = %d (alpha %.3f, K = %d):"
              % (w["h"], w["alpha"], len(jd)))
        print("      %5s %8s %6s | %10s %10s %10s | %8s"
              % ("cell", "n", "u/2a", "lmin_k+1", "jdef", "dnull",
                 "r_k+1"))
        order = list(range(min(12, len(jd))))
        worst = list(np.argsort(-np.nan_to_num(jd, nan=-1e30))[:5])
        for k in order + [k for k in worst if k not in order]:
            print("      %5d %8d %6.3f | %10.2e %+10.2e %10.2e | %8.4f"
                  % (k, nn[k], uu[k] / (2 * w["alpha"]),
                     ps["lmin"][k + 1], jd[k], ps["dnull"][k + 1],
                     ps["r"][k + 1]))

    # census typing of J-violating cells (both groupings, all rungs)
    print("\n  J-defect census typing (jdef > %.0e), all rungs:"
          % JDEF_TOL)
    census = {}
    for gname in ("G1", "G2"):
        cls = dict(total=0, viol=0, p2=0, kge2=0, p1m4=0, p3m4=0,
                   dec=np.zeros(10))
        vd = np.zeros(10)
        td = np.zeros(10)
        for w in rows:
            jd = w[gname]["ps"]["jdef"]
            uu = w["rr"]["uu"]
            nn = np.rint(np.exp(uu)).astype(np.int64)
            frac = uu / (2.0 * w["alpha"])
            deci = np.clip((frac * 10).astype(int), 0, 9)
            viol = np.nan_to_num(jd, nan=-1e30) > JDEF_TOL
            cls["total"] += len(jd)
            cls["viol"] += int(viol.sum())
            np.add.at(td, deci, 1)
            np.add.at(vd, deci[viol], 1)
            for n in nn[viol]:
                p = int(spf[n])
                k = 0
                m = int(n)
                while m > 1:
                    m //= p
                    k += 1
                if p == 2:
                    cls["p2"] += 1
                elif p % 4 == 1:
                    cls["p1m4"] += 1
                else:
                    cls["p3m4"] += 1
                if k >= 2:
                    cls["kge2"] += 1
        with np.errstate(divide="ignore", invalid="ignore"):
            decf = np.where(td > 0, vd / np.maximum(td, 1), 0.0)
        census[gname] = cls
        print("    %s: %d/%d cells J-expand (%.1f%%); of the "
              "violators: p=2 %d, p=1(4) %d, p=3(4) %d, k>=2 %d; "
              "violation fraction by u/2alpha decile: %s"
              % (gname, cls["viol"], cls["total"],
                 100.0 * cls["viol"] / max(cls["total"], 1),
                 cls["p2"], cls["p1m4"], cls["p3m4"], cls["kge2"],
                 np.array2string(decf, precision=2)))

    # ============================================================== S3
    print("\nS3 -- the cascade / boundary-ray analysis")
    aas = [w["alpha"] for w in rows]
    ray_sub = {}
    for gname in ("G1", "G2"):
        r_end = [w[gname]["summ"]["r_end"] for w in rows]
        a_end = [w[gname]["summ"]["ang_end"] for w in rows]
        kt_r = kendall_tau(aas, r_end)
        kt_a = kendall_tau(aas, a_end)
        ok = kt_r >= KEN_BAR and kt_a <= -KEN_BAR
        ray_sub[gname] = ok
        argmins = [w[gname]["summ"]["ang_argmin"] for w in rows]
        print("    %s: r_end %.4f -> %.4f (Kendall vs alpha %+.3f), "
              "angle to (5,-3,4) %.3f -> %.3f deg (Kendall %+.3f); "
              "closest path approach to the ray at relative cell "
              "position median %.3f -- %s"
              % (gname, r_end[0], r_end[-1], kt_r, a_end[0],
                 a_end[-1], kt_a, float(np.median(argmins)),
                 "RAY-EDGE-CONFIRMED" if ok else "RAY-EDGE-OPEN"))
    print("    (sub-verdict only; the compiler ray (5,-3,4) is the "
          "exact null direction q = 0, v807)")

    # ============================================================== S4
    print("\nS4 -- the incomplete-cell contrast (must break; "
          "mass-forced, stated)")
    n_exit = 0
    exit_pos = []
    for w in rows:
        rr = w["rr"]
        deltas = -(rr["lam"][:, None] * rr["Xn"])
        ps = path_stats((w["A0"][0, 0], w["A0"][1, 1], w["A0"][0, 1]),
                        deltas)
        s = flow_summary(ps)
        if not s["cone_ok"]:
            n_exit += 1
            fe = s["first_exit"]
            exit_pos.append(rr["uu"][min(fe, len(rr["uu"]) - 1)]
                            / (2.0 * rr["alpha"]) if fe > 0 else 0.0)
    frac = n_exit / len(rows)
    check_b("S4.INC naive cells (atom kick alone, no continuum piece, "
          "same base Ah_pnt) EXIT the cone on %d/%d rungs (%.2f >= "
          "%.2f); first-exit u/2alpha median %.3f -- the corpus's "
          "additive-granularity negative reproduced: the completion "
          "is load-bearing"
          % (n_exit, len(rows), frac, MB_FRAC,
             float(np.median(exit_pos)) if exit_pos else float("nan")),
          frac >= MB_FRAC)

    # ============================================================== S5
    print("\nS5 -- controls (stride-%d subset, G1 pairing unless "
          "stated)" % STRIDE)
    sub = rows[::STRIDE]
    real_dnull_med = float(np.median(
        [w["G1"]["summ"]["max_dnull"] for w in sub]))

    # C1 order swap (measured, both groupings)
    print("  C1 order swap (cells applied in decreasing u; endpoint "
          "identical by additivity):")
    for gname in ("G1", "G2"):
        n_exit_sw = 0
        end_dev = 0.0
        for w in sub:
            deltas = w[gname]["deltas"][::-1]
            ps = path_stats((w["A0"][0, 0], w["A0"][1, 1],
                             w["A0"][0, 1]), deltas)
            s = flow_summary(ps)
            if not s["cone_ok"]:
                n_exit_sw += 1
            Aend = tri_mat((ps["a11"][-1], ps["a22"][-1],
                            ps["a12"][-1]))
            end_dev = max(end_dev,
                          float(np.max(np.abs(Aend - w["rr"]["Ah"])))
                          / float(np.max(np.abs(w["rr"]["Ah"]))))
        fwd_exits = sum(0 if w[gname]["summ"]["cone_ok"] else 1
                        for w in sub)
        print("    %s reversed: cone exits %d/%d (forward: %d/%d); "
              "endpoint dev %.1e -- ORDER %s for the path"
              % (gname, n_exit_sw, len(sub), fwd_exits, len(sub),
                 end_dev,
                 "MATTERS" if n_exit_sw != fwd_exits else
                 "does not decide cone membership"))

    def control_flow(w, uuX, lamX, XnX, cont_fac=1.0,
                     base_fac=1.0):
        """One control flow on rung w: custom atoms + G1 pairing;
        continuum scaled by cont_fac; base B - base_fac*S_pnt."""
        rr = w["rr"]
        b = breaks_G1(uuX, rr["alpha"])
        Chat = cont_fac * cell_increments(w["edges"], w["reads"], b)
        deltas = Chat - lamX[:, None] * XnX
        A0 = rr["B"] - base_fac * w["S_pnt"]
        ps = path_stats((A0[0, 0], A0[1, 1], A0[0, 1]), deltas)
        return flow_summary(ps)

    # C2 equal-weight scramble
    n_exit_eq = 0
    dn_eq = []
    for w in sub:
        rr = w["rr"]
        mm_eq = np.full(len(rr["uu"]),
                        float(np.sum(w["mm"])) / len(rr["uu"]))
        s = control_flow(w, rr["uu"], 0.5 * mm_eq, rr["Xn"])
        if not s["cone_ok"]:
            n_exit_eq += 1
        dn_eq.append(s["max_dnull"])
    eq_fire = (n_exit_eq / len(sub) >= CTRL_FRAC
               or float(np.median(dn_eq)) >= DNULL_FAC * real_dnull_med)
    check_b("S5.C2 [must-break] equal-weight scramble (positions kept, "
          "masses -> ladder mean, total matched): cone exits %d/%d, "
          "median path max|dnull| %.2e vs real %.2e (fire iff exits "
          ">= %.1f or dnull >= %.0fx) -- %s"
          % (n_exit_eq, len(sub), float(np.median(dn_eq)),
             real_dnull_med, CTRL_FRAC, DNULL_FAC,
             "fires" if eq_fire else "does NOT fire"), eq_fire)

    # C3 Epstein comb
    n_exit_ep = 0
    dn_ep = []
    ep_exit_pos = []
    for w in sub:
        rr = w["rr"]
        uuE, mE_raw = epstein_atoms(rr["alpha"])
        kap = float(np.sum(w["mm"])) / float(np.sum(mE_raw))
        XnE = atom_reads(rr, uuE)
        s = control_flow(w, uuE, 0.5 * kap * mE_raw, XnE)
        if not s["cone_ok"]:
            n_exit_ep += 1
            fe = s["first_exit"]
            ep_exit_pos.append(uuE[min(max(fe - 1, 0), len(uuE) - 1)]
                               / (2.0 * rr["alpha"]))
        dn_ep.append(s["max_dnull"])
    ep_fire = (n_exit_ep / len(sub) >= CTRL_FRAC
               or float(np.median(dn_ep)) >= DNULL_FAC * real_dnull_med)
    check_b("S5.C3 [must-break] Epstein x^2+5y^2 comb (mass-matched, "
          "same completion): cone exits %d/%d, median path "
          "max|dnull| %.2e; first-exit u/2alpha %s -- %s"
          % (n_exit_ep, len(sub), float(np.median(dn_ep)),
             ("median %.3f" % float(np.median(ep_exit_pos)))
             if ep_exit_pos else "n/a",
             "fires" if ep_fire else "does NOT fire"), ep_fire)

    # C5 wrong pole normalization
    n_exit_wr = 0
    for w in sub:
        rr = w["rr"]
        s = control_flow(w, rr["uu"], rr["lam"], rr["Xn"],
                         cont_fac=WRONG_FAC, base_fac=WRONG_FAC)
        if not s["cone_ok"]:
            n_exit_wr += 1
    wr_fire = n_exit_wr / len(sub) >= CTRL_FRAC
    check_b("S5.C5 [must-break] wrong pole normalization (continuum "
          "density x %.1f, self-consistent base B - %.1f S_pnt; "
          "endpoint still telescopes to Ah): cone exits %d/%d -- %s"
          % (WRONG_FAC, WRONG_FAC, n_exit_wr, len(sub),
             "fires" if wr_fire else "does NOT fire"), wr_fire)

    # ============================================================== S6
    print("\n" + "=" * 78)
    print("S6 -- VERDICT")
    print("=" * 78)
    runtime = time.time() - T0
    WARD_IDS = ("S0.AST", "S1.REF", "S1.ENV", "S1.TEL", "S1.PHI")
    ward_fails = [f for f in FAILS_B if f in WARD_IDS]
    valid = not ward_fails and runtime <= RUNTIME_CAP
    cone_all = {g: all(w[g]["summ"]["cone_ok"] for w in rows)
                for g in ("G1", "G2")}
    jzero = {g: census[g]["viol"] == 0 for g in ("G1", "G2")}
    exit_frac = {g: sum(0 if w[g]["summ"]["cone_ok"] else 1
                        for w in rows) / len(rows)
                 for g in ("G1", "G2")}
    contrast_ok = frac >= MB_FRAC
    controls_ok = eq_fire and ep_fire and wr_fire
    if not valid:
        verdict = "INVALID"
    elif (cone_all["G1"] and cone_all["G2"] and jzero["G1"]
          and jzero["G2"] and contrast_ok and controls_ok):
        verdict = "CELLS-PRESERVE-CONE"
    elif exit_frac["G1"] >= 0.5 and exit_frac["G2"] >= 0.5:
        verdict = "CONE-BROKEN"
    else:
        verdict = "CONE-PARTIAL"
    print("""
  VERDICT: %s
    cone preserved at every cell:  G1 %s (exit fraction %.2f), G2 %s
      (exit fraction %.2f)
    per-cell J-contraction (jdef <= %.0e): G1 %d/%d violations
      (%.1f%%), G2 %d/%d (%.1f%%)
    incomplete contrast fires: %s (%.2f of rungs)
    must-break controls: equal-weight %s, Epstein %s, wrong-norm %s
    ray sub-verdict: G1 %s, G2 %s
""" % (verdict,
       "YES" if cone_all["G1"] else "no", exit_frac["G1"],
       "YES" if cone_all["G2"] else "no", exit_frac["G2"],
       JDEF_TOL,
       census["G1"]["viol"], census["G1"]["total"],
       100.0 * census["G1"]["viol"] / max(census["G1"]["total"], 1),
       census["G2"]["viol"], census["G2"]["total"],
       100.0 * census["G2"]["viol"] / max(census["G2"]["total"], 1),
       "YES" if contrast_ok else "NO", frac,
       "fires" if eq_fire else "NO", "fires" if ep_fire else "NO",
       "fires" if wr_fire else "NO",
       "RAY-EDGE-CONFIRMED" if ray_sub["G1"] else "RAY-EDGE-OPEN",
       "RAY-EDGE-CONFIRMED" if ray_sub["G2"] else "RAY-EDGE-OPEN"))
    if verdict == "CONE-BROKEN":
        for g in ("G1", "G2"):
            fe = [w[g]["summ"]["first_exit"] for w in rows]
            fo = [w[g]["summ"]["frac_out"] for w in rows]
            nr = [w[g]["summ"]["n_out_runs"] for w in rows]
            lo = [w[g]["summ"]["last_out"]
                  / max(w[g]["summ"]["ncell"], 1) for w in rows]
            end_in = sum(1 for w in rows
                         if w[g]["ps"]["lmin"][-1] > 0.0)
            print("  TYPED (%s): first exit at cell index median %d "
                  "(the n = 2 cell if 0); fraction of path states "
                  "out of cone median %.3f; out-runs per rung median "
                  "%d; last out-of-cone state at relative position "
                  "median %.3f; endpoint back inside the cone on "
                  "%d/%d rungs (= the certified tau > 0)"
                  % (g, int(np.median(fe)), float(np.median(fo)),
                     int(np.median(nr)), float(np.median(lo)),
                     end_in, len(rows)))
    if not ep_fire:
        print("  CONTROL SURPRISE (typed, kept as frozen with its "
              "FAIL): the mass-matched Epstein comb does NOT break "
              "the cone transport while the TRUE von Mangoldt comb "
              "does -- the cone dips are driven by the true comb's "
              "own small-x fluctuation E(x) = psi(x) - x (the n = 2 "
              "cell), which the smoother Epstein representation "
              "numbers do not reproduce; the frozen must-break "
              "prediction pointed the wrong way.")
    if verdict == "CELLS-PRESERVE-CONE":
        print("""  WHAT THE INFINITE STATEMENT WOULD NEED (named exactly):
    (i)   the UNCONDITIONAL completed-cell inequality: for every
          prime power n, the completed increment Chat_n - lam_n
          Xhat_n keeps A > 0 and det non-increasing FROM THE
          CONSTRUCTION (an explicit inequality between the local
          von Mangoldt mass and its Stieltjes continuum share on the
          deployed reads) -- replacing this probe's measured census;
    (ii)  a uniform Birkhoff/Wojtkowski contraction modulus for the
          composed congruence flow in the Lorentz cone metric
          (the v773 missing piece, now on the 2x2 lock surface);
    (iii) the boundary transition: the composed flow's limit
          direction is the null ray (5,-3,4) with the transversal
          reserve tau > 0 at every finite stage -- the v818 amplifier
          floor rho > 0 restated as cone non-degeneracy.""")
    print("""
  HONESTY: this is a FINITE transport measurement on %d deployed
  rungs (2-mode lock compression).  Cone preservation of the
  completed flow is a statement about the hybrid window (atoms below
  the horizon, density above) -- it does NOT bound the infinite
  ladder, does NOT provide the uniform capture constant, and the
  per-cell J-census is measured, not derived.  The incomplete
  contrast is mass-forced (its firing confirms the bookkeeping, not
  arithmetic).  NO RH claim.""" % len(rows))
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed%s"
          % (runtime, len(CHECKS), len(FAILS_B),
             ("  " + ",".join(FAILS_B)) if FAILS_B else ""))
    print("[VERDICT] %s" % verdict)
    _VERDICTS["b"] = verdict
    return 0 if valid else 1


def run():
    global N_CHK
    t_all = time.time()
    N_CHK = 0
    FAILS_A.clear()
    CHECKS.clear()
    FAILS_B.clear()
    _VERDICTS.clear()
    print("=" * 74)
    print("v847 -- PRIME.WEDGE.LAGRANGE.01 + PRIME.CELLCONE."
          "TRANSPORT.01")
    print("(the TWO frozen-honest FAILS S5.SCR + S5.C3 are EXPECTED "
          "and pattern-gated,")
    print(" NOT refit; NO RH claim)")
    print("=" * 74 + "\n")
    part_a()
    n_a, fails_a = N_CHK, list(FAILS_A)
    print()
    rc_b = part_b()
    n_b, fails_b = len(CHECKS), list(FAILS_B)
    ok = (n_a == N_CHECKS_A and fails_a == EXPECTED_FAILS_A
          and n_b == N_CHECKS_B and fails_b == EXPECTED_FAILS_B
          and rc_b == 0
          and _VERDICTS.get("a") == EXPECTED_A
          and _VERDICTS.get("b") == EXPECTED_B)
    print("\n" + "=" * 74)
    print("v847: %d/%d checks passed, %d expected-honest FAILS [%s] | "
          "verdicts %s + %s | runtime %.1f s"
          % (n_a + n_b - len(fails_a) - len(fails_b), n_a + n_b,
             len(fails_a) + len(fails_b),
             ", ".join(fails_a + fails_b), _VERDICTS.get("a"),
             _VERDICTS.get("b"), time.time() - t_all))
    print("NO RH claim; all three v5.4 architectures (v846 Schur/"
          "spectral, the wedge, the")
    print("cell cone) die on the same finer-than-statistical substance "
          "-- constant wedge")
    print("laws and unrenormalized small-n cell transports are "
          "stop-listed.")
    print("[%s] PATTERN GATE: expected %d + %d checks with exactly the "
          "TWO frozen-honest FAILS %s + %s and verdicts %s + %s (got "
          "%d + %d, fails %s, verdicts %s + %s)"
          % ("PASS" if ok else "FAIL", N_CHECKS_A, N_CHECKS_B,
             ",".join(EXPECTED_FAILS_A), ",".join(EXPECTED_FAILS_B),
             EXPECTED_A, EXPECTED_B, n_a, n_b,
             ",".join(fails_a + fails_b) or "none",
             _VERDICTS.get("a"), _VERDICTS.get("b")))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(run())
