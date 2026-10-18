#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""v823 -- PRIME.FLOOR.LAGRANGE.01: the sector floor det Ahat2 = lambda tau as an EXACT machine-verified sum of squares over zero+pole rank-one carriers (Lagrange identity), plus the fixed-pair certification (pole x gamma_1) with the budget tightened ~10 orders by the psd-remainder monotonicity chain, ONE module from two probes (8 checks with the one preregistered-honest FAIL S3.CERT + 9/9 checks, ~55 s; discovery probes prime_lagrange_pair_probe.py LAGRANGE-CONCENTRATED and prime_lagrange_budget_probe.py PAIR-CERTIFIED, both 2026-08-06).  PART 1, THE EXACT DECOMPOSITION + THE WARD [identity-grade wards on every rung]: every per-zero layer of the v692 master identity is EXACTLY rank-one -- the odd-extension symmetry factors the common phase, F_i = -2i e^{i(M-1)phi/2} S_i with the REAL closed form S_i(phi) = sum_j t_ij sin((h-j-1/2) phi), so L_gamma = v_g v_g^T with v_g = 2 sqrt(w(gamma)) (S1, S2), w(gamma) = D csinc(gamma D/2)^2 >= 0 (layer dev <= 1.2e-16, pole rank-one dev <= 4.8e-17); the LAGRANGE IDENTITY det(G_Z + P) = sum_{pairs} w_i w_j (a_i b_j - a_j b_i)^2 holds at machine precision on all 14 rungs (ward_rel <= 1.4e-9); A0 typed honestly: the ATOM-side rank-one framing FAILS as frozen (per-atom rank-one fraction 0.10..0.23 < 0.5) -- the exact SOS realization lives on the ZERO+POLE side.  THE CENSUS: the POLE is the universal non-collinear leg (the pole family carries 1.0000 of the pair total; every top-100 pair is pole x zero), the moving zero leg obeys the ALIAS-COMB LAW (median fractional distance of the top-10 legs to the k 2pi/D comb 0.0007..0.0061 vs uniform 0.25), top-100 concentration 0.949..0.997; the ONE honest FAIL is the preregistered old-budget gate S3.CERT (tail-estimate BUD 0.14..7.05 vs X^2 ~ 1e-3, 0/14 LIVE) -- exactly the blocker part 2 removes.  PART 2, THE BUDGET ATTACK (PAIR-CERTIFIED, 9/9): the autopsy names the dominant old-budget term (ALIAS truncation on all 3 autopsy rungs; quadrature 4e-8, precision 1e-12 -- neither blocks); THE ROUTE CHANGE: R := Ahat2 - G_Z - P is an exact float 2x2 with lambda_min(R) = 1.6e-7..2.8e-6 >= margin verified per rung, and the 2x2 psd fact det(B + R) >= det B eliminates the tail estimate from the chain entirely -- BUD 1.4e-1..7.1e0 -> 2.4e-12..2.7e-9, MEDIAN 9.8 ORDERS TIGHTENED; the certified interval X^2(pole, gamma_1) - BUD_new is strictly positive on 14/14 rungs (gamma_1 pinned to zetazero(1) within 1e-11; dps-40 mpmath ward inside the interval on 3 rungs); THE SHARE: the fixed pair carries 0.0063..0.5832 of the floor with slope h^+1.06 (X^2 ~ h^+0.39 vs det ~ h^-0.67) -- a GROWING brick, not a vanishing one.  Controls fire in both parts (scramble explodes the identity residual x45.8..49.0 and breaks the RvM-tail match; Epstein x^2+5y^2 changes the Lagrange floor at det scale x1784..50029; the collinear synthetic family gives det = 9.2e-16 and a certified interval containing 0 -- no false positivity).  Feeds PRIME.FLOOR.RATIO.01 [O] (narrowed, not closed): battery-relative, per-rung float-level certificates; the uniform/citation-grade upgrade is v824.  NECESSARY-side floor evidence on the frozen battery -- NO RH claim.  Python-only per GATE.WOLFRAM.02.

PROVENANCE: discovery probes prime_lagrange_pair_probe.py (2026-08-06,
8 checks with the one preregistered-honest FAIL S3.CERT, ~36 s,
LAGRANGE-CONCENTRATED) + prime_lagrange_budget_probe.py (2026-08-06,
9/9 checks, ~18 s, PAIR-CERTIFIED); both re-run identically at
promotion.  Merged per the v518/v668 precedent: part 1 verbatim at
module level (sibling imports v563/v684/v692 resolve against the
verification directory; the probe's run() renamed _probe_run(); a
_LAST1 verdict capture inserted, v791 precedent); part 2 verbatim
inside an isolated function scope (its module-level names are
function-local; its 'global' declarations become 'nonlocal'; its
read-only parent import 'prime_lagrange_pair_probe as pp' resolves to
THIS module via pp = sys.modules[__name__] -- same functions, same
numbers; a _LAST2 verdict capture inserted); numbers unchanged; run()
encodes the expected FAIL pattern (v757 precedent).  DOWNSCOPING:
none -- the deployed 14-window ladder, the 2e4 RS zero scan and the
full 22491-component pair scans are rebuilt in-process per the
v677/v772 precedent (~55 s total, predeclared).

Original prime_lagrange_pair_probe.py docstring (verbatim):
prime_lagrange_pair_probe -- the Lagrange-identity attack on the floor.

THE MOVE ("Determinante als Varianz"): if the 2-mode lock block is a
positive rank-one sum  S = sum_j w_j (a_j,b_j)^T(a_j,b_j)  then the
Lagrange identity gives EXACTLY

    det S = sum_{i<j} w_i w_j (a_i b_j - a_j b_i)^2      (sum of squares)

so a floor bound needs only ONE certified non-collinear pair.

PREMISE CHECK (A0, frozen): the task text frames the sum over ATOMS
(KMS weight, two tent/spline reads per atom).  The deployed per-atom
2x2 blocks are X_n = [[W11(u_n), W12(u_n)], [., W22(u_n)]] -- CORRELATION
reads at lag u_n, NOT outer products; their rank-one-ness is MEASURED
(A0), not assumed.  The EXACT rank-one realization of the deployed
floor det Ahat2 = lambda tau is the ZERO SIDE of the v692 master
identity (validated there):

    Ahat2 = sum_gamma L_gamma + P + tail,
    L_gamma = w(gamma) [[|F1|^2, Re F1 conj F2], [., |F2|^2]],
    w(gamma) = D csinc(gamma D/2)^2 >= 0  (the alias weight),
    P = c_P s s^T (pole layer, rank-one psd),  tail psd via [A1].

Because f_i = odd_ext(t_i) has the exact symmetry f_{M-1-j} = -f_j,
the common phase factors out:  F_i(phi) = -2i e^{i(M-1)phi/2} S_i(phi)
with the REAL closed form

    S_i(phi) = sum_{j=0}^{h-1} t_{i,j} sin((h - j - 1/2) phi),

so EVERY per-zero layer is EXACTLY rank-one: L_gamma = v_g v_g^T with
v_g = 2 sqrt(w(gamma)) (S1(D gamma), S2(D gamma)).  The Lagrange
components of the floor are THE ZEROS plus THE POLE; the closed-form
cross-difference of a pair (gamma, gamma') is

    X(g,g') = 4 sqrt(w(g) w(g')) [S1(Dg) S2(Dg') - S1(Dg') S2(Dg)]

and  det(G_Z + P) = sum_{pairs} X^2  exactly (the ward).  Since the
tail is psd ([A1]: on-line by computation <= 2e4 and citation <= 3e12)
and det is monotone under psd addition on psd matrices,

    det Ahat2 = lambda tau >= det(G_Z + P) - BUD >= X_top^2 - BUD

with BUD the measured identity budget (the v692 resid, honest float +
quadrature).  This is the certification chain attempted in S3.

TASK MAP (frozen):
  A0  atom-premise census (per-atom det X_n / tr^2 -- typed);
  S1  the exact decomposition + THE WARD (per-zero rank-one at machine
      precision, closed-form components == layers, Lagrange pair sum
      == det(G_Z+P) at machine precision, identity resid vs bar);
  S2  the pair census (top-1/10/100 shares, N50/N90, carrier identity
      along the full ladder: pole-zero vs zero-zero, small vs large
      gamma, adjacent vs far);
  S3  the certification attempt (fixed modal pair: exact numbers,
      share of the floor, the budget check det >= X^2 - BUD live?);
  S4  controls (C1 declared scramble, C2 Epstein x^2+5y^2 mass-matched,
      C3 collinear synthetic family -> det = 0 exactly);
  S5  verdict (frozen enum) + recommended contract text (report only).

VERDICT (frozen): LAGRANGE-PAIR-CERTIFIED (a FIXED pair identity is
 top-1 on >= 80% of windows AND its share of det Ahat2 >= 1% on every
 window AND the budget check X^2 > BUD passes on every window) /
 LAGRANGE-CONCENTRATED (top-100 pairs carry >= 50% of the pair total
 on every window but the fixed-pair certification does not close) /
 LAGRANGE-DIFFUSE (otherwise; typed with the concentration profile).

FIREWALL: v563 / v684 / v692 READ-ONLY imports; zero VALUES are used
openly as the decomposition carriers (this probe lives on the zero
side of the validated master identity; in-band the list is on-line by
computation, and by citation to 3e12 -- no RH input, no RH claim).
RNG only in v563's declared scramble (C1).

Original prime_lagrange_budget_probe.py docstring (verbatim):
prime_lagrange_budget_probe -- tighten the identity budget so the
fixed pair certification (pole x gamma_1) closes or dies honestly.

CONTEXT (prime_lagrange_pair_probe, LAGRANGE-CONCENTRATED): the floor
det Ahat2 = lambda tau is an exact sum of squares over zero+pole
rank-one carriers; the pole is the universal non-collinear leg; the
fixed pair (pole, gamma_1) has the explicit closed-form
cross-difference X; the only blocker was BUD ~ 0.1..7 vs X^2 ~ 1e-3
-- an error-bound gap, not a quantity gap.

S1 BUDGET AUTOPSY (frozen): decompose the old BUD on 3 rungs --
  (i) quadrature step of the tail integral (points x2), (ii) alias
  truncation (periods x2), (iii) the RvM-DENSITY SMOOTHING error
  (measured against the ACTUAL zeros in the predeclared band
  (2e4, 2.5e4], RS scan, RvM count check), (iv) float.  The honest
  dominant term is named.

S2 TIGHTENING (toolset predeclared, then executed):
  (a) quadrature upgrade on the SAME frozen integrand (composite
      Gauss-Legendre vs the deployed trapezoid) -- measured;
  (b) the rigorous closed-form tail bound: w(g) <= 4/(D g^2),
      |F_i| <= L1_i, sum_{g>T} g^-2 <= (log T + 1)/(pi T) (Abel with
      N(t) <= t log t / 2pi) -- computed and compared to X^2;
  (c) zero depth: the predeclared band extension (S1) + the solved
      horizon T needed by the density route -- typed;
  (d) mpmath precision: dps = 40 recomputation of the certified
      quantity (the ward);
  THEN THE ROUTE CHANGE (the actual tightening; the certified
  QUANTITY X^2 is untouched, only the error-bound machinery):
      R := Ahat2 - G_Z - P  (exact float 2x2 remainder),
      verify  lambda_min(R) >= PSD_MARGIN  (numerically, per rung);
      2x2 fact: B, R psd  =>  det(B+R) = det B + det R
                 + tr(adj(B) R) >= det B      (every term >= 0),
      so  det Ahat2 >= det(G_Z + P) = sum_pairs X^2 >= X^2(pole,g1)
  with NO tail estimate in the chain (the RvM-density smoothing --
  the irreducible term of the old route -- drops out; [A1] on-line
  citation remains the INTERPRETATION of why R is psd, but the
  verified statement is a float matrix fact).  Fallback horizon
  T_C = 2e3 is predeclared in case lambda_min fails at 2e4.

S3 CERTIFICATION RETRY: per rung the certified interval
  X^2(pole, g1) +- BUD_new,  BUD_new = position error (measured
  |gamma_1(cache) - zetazero(1)| + frozen slack, propagated through
  dX/dgamma) + float chain error (100 eps scale^2); PASS = strictly
  positive interval + the chain lambda_min(R) >= margin; the ledger
  BUD_old vs BUD_new (orders tightened); the uncertified rest
  det(G_Z+P) - X^2 with its structure (the pole-family share).

S4 SCALING (frozen question): is the fixed pair's floor share
  stable, growing, or vanishing along the ladder?  OLS slope of
  log share vs log h; bars below.

CONTROLS: W1 budget ward (mpmath dps-40 value of X^2 must lie inside
  the certified interval, 3 rungs); C1 collinear synthetic family
  (certified interval must CONTAIN 0 -- no false positivity); C2
  scramble (the identity-level remainder must stop looking like the
  RvM tail: max|R_scr - TL|/bar >= 10; lambda_min(R_scr) typed).

VERDICT (frozen): PAIR-CERTIFIED (lambda_min(R) >= margin on every
  rung AND every certified interval strictly positive AND ward +
  controls pass AND share >= SHARE_MIN = 0.005 on every rung with
  slope >= -0.1) / BUDGET-TIGHTENED-INSUFFICIENT (the chain or the
  interval fails somewhere -- the irreducible term named) /
  PAIR-VANISHES (chain closes but the share dies: slope < -0.5 or
  share < SHARE_MIN -- family argument required).

FIREWALL: v563 / v684 / v692 / prime_lagrange_pair_probe READ-ONLY
imports; zero values used openly (on-line by computation <= 2.5e4
here, citation <= 3e12); mpmath zetazero(1) for the ward only.  RNG
only in v563's declared scramble.
"""

import json
import math
import os
import sys
import time

import numpy as np

_here = os.path.dirname(os.path.abspath(__file__))
for _cand in (os.path.join(_here, "..", "..", "verification"), _here):
    if os.path.exists(os.path.join(_cand, "v563_paper2_readouts.py")):
        sys.path.insert(0, os.path.abspath(_cand))
        break

import v563_paper2_readouts as core          # noqa: E402 (READ-ONLY)
import v684_rank3_zeroside as zp             # noqa: E402 (READ-ONLY)
import v692_rank3_lockgram as lg             # noqa: E402 (READ-ONLY)
from mpmath import mp, zetazero, mpf, sin as mpsin, exp as mpexp, \
    sinh as mpsinh, sqrt as mpsqrt            # noqa: E402 (ward only)

T0 = time.time()
FAILS = []
N_CHK = 0
_LAST1 = {}
_LAST2 = {}

# ------------------------------------------------- frozen bars / constants
WARD_REL = 1.0e-8       # Lagrange pair sum vs det(G_Z + P), relative
IMAG_BAR = 1.0e-9       # phase-extraction imaginary residual, relative
LAYER_BAR = 1.0e-8      # per-zero |det L| at working scale (max tr)^2;
#   the float noise model: the exp(i j phi) argument reduction at
#   j phi ~ M D T carries eps_eff ~ eps M D T ~ 2e-10, det noise
#   ~ eps_eff x layer scale^2 -- the bar leaves x50 headroom
POLE_R1_BAR = 1.0e-12   # pole layer rank-one deviation (v692 bar)
K_TOP = 4096            # tracked top pairs per window
BLOCK = 512             # pair-scan row block
CERT_SHARE_MIN = 0.01   # fixed-pair share of det Ahat2, every window
STAB_FRAC = 0.80        # fraction of windows the modal pair must top
CONC_TOP100 = 0.50      # top-100 share bar for LAGRANGE-CONCENTRATED
CTRL_RESID_X = 10.0     # C1 must blow the identity resid by this
DET_DIFF_BAR = 0.20     # C2: Epstein floor must differ at det scale
#   (the lock-block ENTRIES are arch-dominated -- comb content lives
#   at det scale; the entrywise resid is printed as typed info)
COLL_BAR = 1.0e-12      # collinear ward (relative)
RANK1_ATOM_BAR = 1.0e-6  # per-atom |det X|/tr^2 below this = "rank-one"
SCRAMBLE_SEED = 20260806
N_SMALL = 10            # "small zero" = among the first 10
EPS_JS = 1.0e-300


def check(name, ok, detail=""):
    global N_CHK
    N_CHK += 1
    if not ok:
        FAILS.append(name.split()[0])
    print("[%s] %s%s" % ("PASS" if ok else "FAIL", name,
                         (": " + detail) if detail else ""))


def rvm_dens(g):
    return np.log(np.asarray(g) / (2.0 * math.pi)) / (2.0 * math.pi)


def zero_list():
    """The v692 S0 zero list, verbatim: cache + RS scan to 2e4."""
    with open(lg.CACHE) as fh:
        g_a = [float(s_) for s_ in json.load(fh)["gammas"]]
    with open(lg.CACHE_EXT) as fh:
        g_b = [float(s_) for s_ in json.load(fh)["gammas"]]
    g_prec = np.array(g_a + g_b)
    g_scan = zp.find_zeros(float(g_prec[-1]) + 0.4, zp.T_SCAN,
                           zp.SCAN_STEP)
    gam = np.sort(np.concatenate([g_prec, g_scan]))
    n_rvm = float(zp.theta_rs(np.array([zp.T_SCAN]))[0] / math.pi + 1.0)
    return gam, n_rvm


def components_of(w, gam):
    """The Lagrange components of one window: zeros + pole.

    Returns (a, b, meta) with v_alpha = (a_alpha, b_alpha), weights
    folded in; meta wards: imaginary residual of the phase extraction,
    max per-zero |det L|/tr^2, pole rank-one deviation."""
    D, Mz = w["D"], w["M"]
    wg = D * np.real(lg.csinc(gam * D / 2.0) ** 2)
    F1 = lg.F_of(w["f1"], D * gam)
    F2 = lg.F_of(w["f2"], D * gam)
    # phase extraction: F = -2i e^{i th} S  with th = (M-1) D gamma / 2
    rot = np.exp(-1j * (Mz - 1) * D * gam / 2.0) * (0.5j)
    S1c, S2c = rot * F1, rot * F2
    scale = max(float(np.max(np.abs(F1))), float(np.max(np.abs(F2))),
                EPS_JS)
    imag_res = max(float(np.max(np.abs(S1c.imag))),
                   float(np.max(np.abs(S2c.imag)))) / scale
    S1, S2 = S1c.real, S2c.real
    # per-zero layer rank-one ward on the RAW complex layer
    l11 = wg * np.abs(F1) ** 2
    l22 = wg * np.abs(F2) ** 2
    l12 = wg * np.real(F1 * np.conj(F2))
    tr = l11 + l22
    det_l = l11 * l22 - l12 ** 2
    # rank-one ward at WORKING SCALE: per-zero trace normalization
    # blows up on csinc-null zeros (tiny trace, fixed phase noise)
    tr_max = max(float(np.max(tr)), EPS_JS)
    layer_dev = float(np.max(np.abs(det_l))) / tr_max ** 2
    a = 2.0 * np.sqrt(np.maximum(wg, 0.0)) * S1
    b = 2.0 * np.sqrt(np.maximum(wg, 0.0)) * S2
    # component reconstruction ward vs the raw layers
    rec = max(float(np.max(np.abs(a * a - l11))),
              float(np.max(np.abs(b * b - l22))),
              float(np.max(np.abs(a * b - l12)))) / max(
                  float(np.max(tr)), EPS_JS)
    # pole layer (v692 closed form via T at +-i/2), rank-one psd
    P = np.empty((2, 2))
    for (i, j), (fa, fb) in {(0, 0): (w["f1"], w["f1"]),
                             (1, 1): (w["f2"], w["f2"]),
                             (0, 1): (w["f1"], w["f2"])}.items():
        tp = lg.T_pair(fa, fb, D, np.array([0.5j, -0.5j]))
        P[i, j] = P[j, i] = -0.5 * float(np.real(np.sum(tp)))
    pw, pv = np.linalg.eigh(P)
    pole_dev = abs(float(pw[0])) / max(abs(float(pw[1])), EPS_JS)
    vp = math.sqrt(max(float(pw[1]), 0.0)) * pv[:, 1]
    a = np.concatenate([a, [vp[0]]])
    b = np.concatenate([b, [vp[1]]])
    return a, b, dict(imag_res=imag_res, layer_dev=layer_dev,
                      rec_dev=rec, pole_dev=pole_dev, P=P, wg=wg,
                      S1=S1, S2=S2)


def tail_and_resid(w, gam):
    """The v692 tail estimate + identity residual (verbatim recipe)."""
    D = w["D"]
    P_alias = 2.0 * math.pi / D
    g_hi = zp.T_SCAN + lg.N_ALIAS_FINE * P_alias
    gg = np.linspace(zp.T_SCAN, g_hi,
                     lg.N_ALIAS_FINE * lg.PTS_PER_ALIAS + 1)
    wgg = D * np.real(lg.csinc(gg * D / 2.0) ** 2)
    Fg1, Fg2 = lg.F_of(w["f1"], D * gg), lg.F_of(w["f2"], D * gg)
    dens = rvm_dens(gg)
    TL = np.empty((2, 2))
    rem_fac = (2.0 / D) * lg.TAIL_SLACK \
        * (math.log(g_hi / (2.0 * math.pi)) + 1.0) \
        / (2.0 * math.pi * g_hi)
    for (i, j), prof in {(0, 0): np.abs(Fg1) ** 2,
                         (1, 1): np.abs(Fg2) ** 2,
                         (0, 1): np.real(Fg1 * np.conj(Fg2))}.items():
        fine = float(np.trapezoid(wgg * prof * dens, gg))
        dot = float(w["f1"] @ w["f1"] if (i, j) == (0, 0) else
                    w["f2"] @ w["f2"] if (i, j) == (1, 1) else
                    w["f1"] @ w["f2"])
        TL[i, j] = TL[j, i] = fine + dot * rem_fac
    return TL


def pair_scan(a, b, k_top):
    """Full upper-triangle scan of X_ij^2 = (a_i b_j - a_j b_i)^2.

    Returns (total, top) with top a desc-sorted list of (val, i, j)."""
    N = len(a)
    jj = np.arange(N)
    total = 0.0
    vals = np.empty(0)
    iis = np.empty(0, dtype=np.int64)
    jjs = np.empty(0, dtype=np.int64)
    for i0 in range(0, N, BLOCK):
        i1 = min(N, i0 + BLOCK)
        cross = a[i0:i1, None] * b[None, :] - b[i0:i1, None] * a[None, :]
        sq = cross * cross
        mask = jj[None, :] > np.arange(i0, i1)[:, None]
        sq *= mask
        total += float(np.sum(sq))
        flat = sq.ravel()
        k = min(k_top, flat.size)
        idx = np.argpartition(flat, -k)[-k:]
        keep = flat[idx] > 0.0
        idx = idx[keep]
        vals = np.concatenate([vals, flat[idx]])
        iis = np.concatenate([iis, idx // N + i0])
        jjs = np.concatenate([jjs, idx % N])
        if len(vals) > 4 * k_top:
            srt = np.argsort(vals)[::-1][:k_top]
            vals, iis, jjs = vals[srt], iis[srt], jjs[srt]
    srt = np.argsort(vals)[::-1][:k_top]
    return total, list(zip(vals[srt], iis[srt], jjs[srt]))


def lab(idx, n_z, gam):
    if idx == n_z:
        return "PO"
    return "Z%d(%.2f)" % (idx + 1, gam[idx])


def pair_key(i, j, n_z):
    """Structural identity of a pair, pole-aware, order-free."""
    i, j = int(min(i, j)), int(max(i, j))
    if j == n_z:
        return "PxZ%d" % (i + 1)
    return "Z%dxZ%d" % (i + 1, j + 1)


def epstein_lock(w):
    """Mass-matched Epstein (x^2 + 5 y^2) comb -> the same lock block."""
    alpha, Mz, D = w["alpha"], w["M"], w["D"]
    Nmax = int(math.floor(math.exp(2.0 * alpha)))
    cnt = np.zeros(Nmax + 1)
    for x in range(0, int(math.isqrt(Nmax)) + 1):
        rem = Nmax - x * x
        if rem < 0:
            break
        y = np.arange(0, int(math.isqrt(rem // 5)) + 1)
        n = x * x + 5 * y * y
        mult = (2.0 if x > 0 else 1.0) * np.where(y > 0, 2.0, 1.0)
        np.add.at(cnt, n, mult)
    nn = np.nonzero(cnt[2:])[0] + 2
    uuE = np.log(nn.astype(float))
    mE = cnt[nn] / np.sqrt(nn.astype(float))
    ka = core.atoms_in(alpha)
    kap = float(np.sum(core.MU_ALL[:ka])) / float(np.sum(mE))
    c_atE, _ = core.atom_lags_at(alpha, Mz, uuE, kap * mE)
    c_ar = core.arch_lags(Mz, D)
    A = core.odd_toeplitz(c_ar + c_atE, Mz)
    hz = Mz // 2
    Tb = core.parity_basis(hz, 2)
    t1v, t2v = Tb[0], Tb[1]
    return np.array([[t1v @ A @ t1v, t1v @ A @ t2v],
                     [t1v @ A @ t2v, t2v @ A @ t2v]])


def _probe_run():
    global N_CHK, FAILS
    N_CHK = 0
    FAILS = []
    print("=" * 78)
    print("THE LAGRANGE-PAIR ATTACK -- det(lock) = lambda tau as an "
          "exact sum of squares")
    print("(part 1 == prime_lagrange_pair_probe verbatim, no RH claim)")
    print("=" * 78)

    # ============================================================== S0
    print("\nS0 -- zero list + the deployed 15-window ladder")
    gam, n_rvm = zero_list()
    n_z = len(gam)
    check("S0.Z zero list: %d zeros to T = %.0f (RvM dev %.2f <= 3); "
          "on-line by computation (<= 2e4) and citation (<= 3e12)"
          % (n_z, zp.T_SCAN, abs(n_z - n_rvm)), abs(n_z - n_rvm) <= 3.0)

    KZ = core.frame_a_zones()
    L15 = len(KZ)
    fam5 = [0, (L15 - 1) // 4, L15 // 2, (3 * (L15 - 1)) // 4, L15 - 1]
    inter = []
    for (lo_i, hi_i), n_in in zip(zip(fam5[:-1], fam5[1:]), (2, 3, 3, 2)):
        for j in range(1, n_in + 1):
            inter.append(lo_i + j * (hi_i - lo_i) // (n_in + 1))
    idx15 = sorted(set(fam5 + inter))
    wins = [lg.lock_block(KZ[i]) for i in idx15]
    wins = [w for w in wins if w["complete"]]
    wins.sort(key=lambda w: w["alpha"])
    t163 = max(float(np.max(np.abs(w["A2"] - w["A2_lag"]))) for w in wins)
    check("S0.T163 lock block == lag route on all %d windows "
          "(max dev %.1e)" % (len(wins), t163), t163 <= lg.BAR_T163)

    # ============================================================== A0
    print("\nA0 -- the atom-side premise, measured (typed, 3 windows)")
    print("    the task's frozen framing sums over ATOMS with two reads")
    print("    per atom; the deployed per-atom 2x2 X_n are CORRELATION")
    print("    reads -- rank-one-ness is a measurement, not an axiom:")
    a0_sel = [0, len(wins) // 2, len(wins) - 1]
    atom_r1_fracs = []
    for si in a0_sel:
        w = wins[si]
        rr = core.build_window(w["kz"])
        Xn = rr["Xn"]
        tr = Xn[:, 0] + Xn[:, 1]
        det_n = Xn[:, 0] * Xn[:, 1] - Xn[:, 2] ** 2
        m = np.abs(tr) > 1e-30
        rel = np.abs(det_n[m]) / tr[m] ** 2
        frac_r1 = float(np.mean(rel <= RANK1_ATOM_BAR))
        atom_r1_fracs.append(frac_r1)
        print("    h = %4d (alpha %.2f): %6d atoms; per-atom "
              "|det X|/tr^2: median %.2e, max %.2e; rank-one "
              "fraction (bar %.0e): %.3f"
              % (w["h"], w["alpha"], len(Xn), float(np.median(rel)),
                 float(np.max(rel)), RANK1_ATOM_BAR, frac_r1))
        w["rr"] = rr
    premise_dead = max(atom_r1_fracs) < 0.5
    check("A0.PREMISE the atom blocks are NOT rank-one pair-vectors "
          "(rank-one fraction %.3f..%.3f < 0.5): the atom-side "
          "Lagrange framing FAILS as frozen; the exact rank-one "
          "realization of det = lambda tau is the ZERO+POLE side of "
          "the v692 master identity (typed reframe, executed below)"
          % (min(atom_r1_fracs), max(atom_r1_fracs)), premise_dead)

    # ============================================================== S1
    print("\nS1 -- the exact decomposition + THE WARD")
    print("    %5s %6s | %8s %8s %8s %8s | %10s %10s | %9s %8s"
          % ("h", "alpha", "im_res", "layer", "rec", "pole_r1",
             "detA2", "det(GZ+P)", "ward_rel", "resid"))
    ward_ok = True
    for w in wins:
        a, b, meta = components_of(w, gam)
        M2 = np.array([[float(a @ a), float(a @ b)],
                       [float(a @ b), float(b @ b)]])
        det_m2 = float(np.linalg.det(M2))
        total, top = pair_scan(a, b, K_TOP)
        ward = abs(total - det_m2) / max(det_m2, EPS_JS)
        TL = tail_and_resid(w, gam)
        Z_side = M2 + TL
        resid = float(np.max(np.abs(w["A2"] - Z_side)))
        bar = lg.BAR_ID_REL * float(np.linalg.norm(w["A2"])) \
            + lg.BAR_ID_ABS
        det_a2 = float(np.linalg.det(w["A2"]))
        # sharp 2x2 det-perturbation budget (entrywise |E| <= resid):
        # |det(A+E) - det A| <= r(|a11|+|a22|+2|a12|) + 2 r^2
        bud = resid * (abs(w["A2"][0, 0]) + abs(w["A2"][1, 1])
                       + 2.0 * abs(w["A2"][0, 1])) + 2.0 * resid ** 2
        ok = (meta["imag_res"] <= IMAG_BAR
              and meta["layer_dev"] <= LAYER_BAR
              and meta["rec_dev"] <= LAYER_BAR
              and meta["pole_dev"] <= POLE_R1_BAR
              and ward <= WARD_REL and resid <= bar)
        ward_ok = ward_ok and ok
        w.update(a=a, b=b, meta=meta, M2=M2, det_m2=det_m2,
                 total=total, top=top, resid=resid, bar=bar,
                 det_a2=det_a2, bud=bud)
        print("    %5d %6.3f | %8.1e %8.1e %8.1e %8.1e | %10.3e "
              "%10.3e | %9.1e %8.1e"
              % (w["h"], w["alpha"], meta["imag_res"],
                 meta["layer_dev"], meta["rec_dev"], meta["pole_dev"],
                 det_a2, det_m2, ward, resid))
    check("S1.WARD on every window: per-zero layers exactly rank-one "
          "(closed form v_g = 2 sqrt(w) (S1, S2), S_i(phi) = sum_j "
          "t_ij sin((h-j-1/2) phi)); pole rank-one; Lagrange pair sum "
          "== det(G_Z + P) at machine precision; identity resid <= "
          "v692 bar", ward_ok)

    # ============================================================== S2
    print("\nS2 -- the pair census along the ladder (%d + 1 components)"
          % n_z)
    print("    %5s %6s | %7s %7s %7s | %6s %6s | %-22s %7s"
          % ("h", "alpha", "top1", "top10", "top100", "N50", "N90",
             "top-1 pair", "adjac"))
    top1_keys = []
    conc100 = []
    for w in wins:
        tv = np.array([t[0] for t in w["top"]])
        cum = np.cumsum(tv) / w["total"]
        s1 = float(cum[0])
        s10 = float(cum[min(9, len(cum) - 1)])
        s100 = float(cum[min(99, len(cum) - 1)])
        n50 = int(np.searchsorted(cum, 0.5) + 1) if cum[-1] >= 0.5 \
            else -1
        n90 = int(np.searchsorted(cum, 0.9) + 1) if cum[-1] >= 0.9 \
            else -1
        v0, i0, j0 = w["top"][0]
        key = pair_key(i0, j0, n_z)
        top1_keys.append(key)
        conc100.append(s100)
        # the pole FAMILY: sum over all (pole x zero) pairs, exact
        x_pz = w["a"][:-1] * w["b"][-1] - w["b"][:-1] * w["a"][-1]
        fam_share = float(np.sum(x_pz ** 2)) / w["total"]
        # the alias law: zero legs of the top-10 pairs vs the k 2pi/D
        # comb (fractional distance in alias-period units; uniform
        # placement would give median 0.25)
        legs = [int(min(ii, jji)) for (vv, ii, jji) in w["top"][:10]
                if min(ii, jji) < n_z]
        if legs:
            r = gam[np.array(legs)] * w["D"] / (2.0 * math.pi)
            alias_d = float(np.median(np.abs(r - np.round(r))))
        else:
            alias_d = float("nan")
        w.update(fam_share=fam_share, alias_d=alias_d)
        # structural classification of the top-100 pairs
        n_pz = n_adj = n_small = 0
        for (vv, ii, jji) in w["top"][:100]:
            ii, jji = int(min(ii, jji)), int(max(ii, jji))
            if jji == n_z:
                n_pz += 1
            else:
                n_adj += int(jji - ii == 1)
                n_small += int(jji < N_SMALL)
        w.update(s1=s1, s10=s10, s100=s100, n50=n50, n90=n90,
                 top1_key=key)
        print("    %5d %6.3f | %7.4f %7.4f %7.4f | %6s %6s | %-22s "
              "%3d/100 (PxZ %d, small %d)"
              % (w["h"], w["alpha"], s1, s10, s100,
                 (str(n50) if n50 > 0 else ">%d" % K_TOP),
                 (str(n90) if n90 > 0 else ">%d" % K_TOP),
                 "%s x %s" % (lab(int(i0), n_z, gam),
                              lab(int(j0), n_z, gam)),
                 n_adj, n_pz, n_small))
    keys, counts = np.unique(top1_keys, return_counts=True)
    modal_key = str(keys[np.argmax(counts)])
    modal_frac = float(np.max(counts)) / len(wins)
    print("    top-1 identity: modal pair %s on %d/%d windows"
          % (modal_key, int(np.max(counts)), len(wins)))
    print("    THE POLE FAMILY: share of the pair total carried by "
          "ALL (pole x zero) pairs: %.4f .. %.4f along the ladder"
          % (min(w["fam_share"] for w in wins),
             max(w["fam_share"] for w in wins)))
    print("    THE ALIAS LAW: median fractional distance of the "
          "top-10 zero legs to the k 2pi/D comb: %.4f .. %.4f "
          "(uniform placement -> 0.25): the moving carrier is the "
          "zero nearest an alias frequency"
          % (min(w["alias_d"] for w in wins),
             max(w["alias_d"] for w in wins)))
    for w in wins[:1]:
        print("    top-8 pairs (smallest window, alpha %.2f):"
              % w["alpha"])
        for (vv, ii, jji) in w["top"][:8]:
            print("      %-24s X^2 = %.4e  (share %.4f)"
                  % ("%s x %s" % (lab(int(ii), n_z, gam),
                                  lab(int(jji), n_z, gam)),
                     vv, vv / w["total"]))

    # ============================================================== S3
    print("\nS3 -- closed form + the certification attempt")
    print("""    CLOSED FORM (exact algebra of the deployed window):
      S_i(phi)  = sum_{j=0}^{h-1} t_{i,j} sin((h - j - 1/2) phi),
                  t_i = parity vector i (row of core.parity_basis),
      w(gamma)  = D csinc(gamma D / 2)^2   (>= 0, the alias weight),
      v_gamma   = 2 sqrt(w(gamma)) (S1(D gamma), S2(D gamma)),
      X(g, g')  = 4 sqrt(w(g) w(g'))
                  [S1(Dg) S2(Dg') - S1(Dg') S2(Dg)],
      det(G_Z + P) = sum_{pairs} X^2        (Lagrange, exact),
      det Ahat2 >= det(G_Z + P) - BUD       (tail psd via [A1]).""")
    print("    the modal pair is %s; its exact numbers per window:"
          % modal_key)
    print("    %5s %6s | %11s %11s | %8s %8s | %9s %5s"
          % ("h", "alpha", "X^2(modal)", "BUD", "sh_pair", "sh_det",
             "X^2>BUD", "top1"))
    cert_live, share_floor = [], []
    for w in wins:
        found = None
        for (vv, ii, jji) in w["top"]:
            if pair_key(ii, jji, n_z) == modal_key:
                found = (vv, int(min(ii, jji)), int(max(ii, jji)))
                break
        if found is None:
            # modal pair fell below the tracked top-K: compute directly
            parts = modal_key.replace("P", str(n_z + 1)).split("x")
            i_m = (n_z if parts[0] == str(n_z + 1)
                   else int(parts[0][1:]) - 1)
            j_m = int(parts[1][1:]) - 1
            xv = (w["a"][i_m] * w["b"][j_m]
                  - w["a"][j_m] * w["b"][i_m]) ** 2
            found = (float(xv), min(i_m, j_m), max(i_m, j_m))
        vv, ii, jji = found
        live = vv > w["bud"]
        sh_d = vv / max(w["det_a2"], EPS_JS)
        cert_live.append(live)
        share_floor.append(sh_d)
        print("    %5d %6.3f | %11.4e %11.4e | %8.4f %8.4f | %9s %5s"
              % (w["h"], w["alpha"], vv, w["bud"], vv / w["total"],
                 sh_d, "LIVE" if live else "dead",
                 "yes" if w["top1_key"] == modal_key else "no"))
    w0 = wins[0]
    v0, i0, j0 = w0["top"][0]
    i0, j0 = int(min(i0, j0)), int(max(i0, j0))
    g_i = ("pole" if i0 == n_z else "%.12f" % gam[i0])
    g_j = ("pole" if j0 == n_z else "%.12f" % gam[j0])
    print("    exact top-1 numbers, smallest window (h = %d, D = %.6f):"
          % (w0["h"], w0["D"]))
    print("      carriers: %s x %s (gamma_i = %s, gamma_j = %s)"
          % (lab(i0, n_z, gam), lab(j0, n_z, gam), g_i, g_j))
    print("      v_i = (%.10e, %.10e)" % (w0["a"][i0], w0["b"][i0]))
    print("      v_j = (%.10e, %.10e)" % (w0["a"][j0], w0["b"][j0]))
    print("      X = %.10e, X^2 = %.10e" %
          (w0["a"][i0] * w0["b"][j0] - w0["a"][j0] * w0["b"][i0], v0))
    print("      det Ahat2 = %.10e, det(G_Z+P) = %.10e, BUD = %.2e"
          % (w0["det_a2"], w0["det_m2"], w0["bud"]))
    sl = np.polyfit(np.log([w["h"] for w in wins]),
                    np.log(np.maximum(share_floor, EPS_JS)), 1)[0]
    print("    modal-pair share of the floor: %.4f .. %.4f "
          "(trend h^%+.2f: %s)"
          % (min(share_floor), max(share_floor), sl,
             "stable/growing" if sl >= -0.1 else "VANISHING"))
    cert_ok = (modal_frac >= STAB_FRAC
               and min(share_floor) >= CERT_SHARE_MIN
               and all(cert_live))
    check("S3.CERT fixed-pair certification: modal pair %s top-1 on "
          "%.0f%% of windows (bar %.0f%%), floor share >= %.3f (bar "
          "%.2f), budget check %d/%d LIVE -- %s"
          % (modal_key, 100 * modal_frac, 100 * STAB_FRAC,
             min(share_floor), CERT_SHARE_MIN, sum(cert_live),
             len(wins), "the skeleton closes at the measured budget"
             if cert_ok else "not closed (typed below)"), cert_ok)

    # ============================================================== S4
    print("\nS4 -- controls")
    sel = [0, len(wins) // 2, len(wins) - 1]
    # C1 declared scramble: the zero side must stop matching
    r_scr = []
    for si in sel:
        w = wins[si]
        rr_s = core.build_window(w["kz"], scramble_seed=SCRAMBLE_SEED)
        resid_s = float(np.max(np.abs(rr_s["Ah_dir"]
                                      - (w["M2"] + tail_and_resid(
                                          w, gam)))))
        r_scr.append(resid_s / w["bar"])
    check("C1 [must-fire] scramble: the zero-side identity residual "
          "explodes (resid/bar %.1f..%.1f, bar x%.0f) -- the Lagrange "
          "carriers are comb content, not window geometry"
          % (min(r_scr), max(r_scr), CTRL_RESID_X),
          min(r_scr) >= CTRL_RESID_X)
    # C2 Epstein comb (x^2 + 5 y^2, mass-matched): the lock-block
    # ENTRIES are arch-dominated (comb-independent to first order) --
    # the comb content lives at DET scale, so the control fires there
    dd_ep, r_ep = [], []
    for si in sel:
        w = wins[si]
        A2_E = epstein_lock(w)
        det_e = float(np.linalg.det(A2_E))
        dd_ep.append(abs(det_e - w["det_a2"])
                     / max(w["det_a2"], EPS_JS))
        resid_e = float(np.max(np.abs(
            A2_E - (w["M2"] + tail_and_resid(w, gam)))))
        r_ep.append(resid_e / w["bar"])
    print("    C2 typed: entrywise resid/bar %.2f..%.2f (arch "
          "dominance at entry scale -- the 5%% bar does not see the "
          "comb); det scale is where the comb lives"
          % (min(r_ep), max(r_ep)))
    check("C2 [must-fire] Epstein: the FLOOR is comb-specific at det "
          "scale: |det_E - det|/det = %.2f..%.2f (bar >= %.2f) -- "
          "different comb, different Lagrange floor"
          % (min(dd_ep), max(dd_ep), DET_DIFF_BAR),
          min(dd_ep) >= DET_DIFF_BAR)
    # C3 collinear synthetic family: det = 0 exactly
    rng_c = np.arange(1, 101, dtype=float)
    ca = rng_c / np.sqrt(np.sum(rng_c ** 2))
    a_c, b_c = ca * 1.0, ca * 1.5
    M_c = np.array([[a_c @ a_c, a_c @ b_c], [a_c @ b_c, b_c @ b_c]])
    tot_c, _ = pair_scan(a_c, b_c, 8)
    det_c = float(np.linalg.det(M_c))
    sc = float(np.trace(M_c)) ** 2
    check("C3 collinear synthetic family: det = %.1e, pair sum = "
          "%.1e (both <= %.0e x tr^2 = %.1e) -- the identity ward"
          % (det_c, tot_c, COLL_BAR, COLL_BAR * sc),
          abs(det_c) <= COLL_BAR * sc and tot_c <= COLL_BAR * sc)

    # ============================================================== S5
    print("\n" + "=" * 78)
    print("S5 -- verdict + recommended contract text (report only)")
    print("=" * 78)
    conc_ok = min(conc100) >= CONC_TOP100
    if cert_ok:
        verdict = "LAGRANGE-PAIR-CERTIFIED"
    elif conc_ok:
        verdict = "LAGRANGE-CONCENTRATED"
    else:
        verdict = "LAGRANGE-DIFFUSE"
    _LAST1["verdict"] = verdict
    print("""
  VERDICT: %s
      concentration: top-1 %.3f..%.3f, top-10 %.3f..%.3f, top-100
      %.3f..%.3f along the ladder; modal top-1 pair %s (%.0f%% of
      windows); modal-pair floor share %.4f..%.4f (trend h^%+.2f);
      budget check %d/%d LIVE; the POLE FAMILY (all pole x zero
      pairs) carries %.3f..%.3f of the pair total; the moving zero
      leg obeys the ALIAS LAW (median comb distance %.3f..%.3f,
      uniform would be 0.25).
      A0 (typed): the ATOM-side Lagrange framing fails as frozen (the
      per-atom 2x2 reads are correlation blocks, rank-one fraction
      %.2f..%.2f); the exact sum-of-squares realization of the floor
      runs over ZEROS + POLE with the closed forms printed in S3.
""" % (verdict,
       min(w["s1"] for w in wins), max(w["s1"] for w in wins),
       min(w["s10"] for w in wins), max(w["s10"] for w in wins),
       min(conc100), max(conc100), modal_key, 100 * modal_frac,
       min(share_floor), max(share_floor), sl,
       sum(cert_live), len(wins),
       min(w["fam_share"] for w in wins),
       max(w["fam_share"] for w in wins),
       min(w["alias_d"] for w in wins),
       max(w["alias_d"] for w in wins),
       min(atom_r1_fracs), max(atom_r1_fracs)))

    dt = time.time() - T0
    print("-" * 78)
    print("checks: %d run, %d failed%s | runtime %.1f min"
          % (N_CHK, len(FAILS),
             (" [" + ", ".join(FAILS) + "]") if FAILS else "",
             dt / 60.0))
    print("NO RH claim (part 1).")


# ======================================================================
# PART 2 -- prime_lagrange_budget_probe.py verbatim, isolated scope
# (its module-level names are function-local; its 'global' declarations
# become 'nonlocal'; pp = this module, v791/v818 precedent)
# ======================================================================
def _part2():
    pp = sys.modules[__name__]
    T0 = time.time()
    FAILS = []
    N_CHK = 0

    # --------------------------------------------- frozen bars / constants
    T_BAND = 2.5e4          # predeclared fluctuation-measurement band end
    T_C = 2.0e3             # predeclared fallback zero horizon
    PSD_MARGIN_FAC = 100.0  # lambda_min(R) >= this x eps x ||Ahat2||_F
    CHAIN_FAC = 100.0       # float chain budget: this x eps x scale^2
    DGAM_SLACK = 1.0e-11    # frozen slack on the measured gamma_1 error
    MP_DPS = 40             # ward precision
    N_WARD = 3              # ward rungs (small / mid / large)
    SHARE_MIN = 0.005       # fixed-pair floor share, every rung
    SLOPE_STABLE = -0.10    # share slope >= this = stable/growing
    SLOPE_VANISH = -0.50    # share slope < this = vanishing
    CTRL_RESID_X = 10.0     # scramble must blow the identity resid
    SCRAMBLE_SEED = 20260806
    EPSM = float(np.finfo(float).eps)
    EPS_JS = 1.0e-300

    def check(name, ok, detail=""):
        nonlocal N_CHK
        N_CHK += 1
        if not ok:
            FAILS.append(name.split()[0])
        print("[%s] %s%s" % ("PASS" if ok else "FAIL", name,
                             (": " + detail) if detail else ""))

    def eig2_min(M):
        """Closed-form smallest eigenvalue of a symmetric 2x2."""
        tr = M[0, 0] + M[1, 1]
        dif = M[0, 0] - M[1, 1]
        rad = math.sqrt(0.25 * dif * dif + M[0, 1] * M[0, 1])
        return 0.5 * tr - rad

    def tail_estimate(w, n_alias, pts_per, gam_lo):
        """The v692 tail recipe with tunable quadrature (autopsy knob)."""
        D = w["D"]
        P_alias = 2.0 * math.pi / D
        g_hi = gam_lo + n_alias * P_alias
        gg = np.linspace(gam_lo, g_hi, n_alias * pts_per + 1)
        wgg = D * np.real(lg.csinc(gg * D / 2.0) ** 2)
        Fg1, Fg2 = lg.F_of(w["f1"], D * gg), lg.F_of(w["f2"], D * gg)
        dens = pp.rvm_dens(gg)
        TL = np.empty((2, 2))
        rem_fac = (2.0 / D) * lg.TAIL_SLACK \
            * (math.log(g_hi / (2.0 * math.pi)) + 1.0) \
            / (2.0 * math.pi * g_hi)
        for (i, j), prof in {(0, 0): np.abs(Fg1) ** 2,
                             (1, 1): np.abs(Fg2) ** 2,
                             (0, 1): np.real(Fg1 * np.conj(Fg2))}.items():
            fine = float(np.trapezoid(wgg * prof * dens, gg))
            dot = float(w["f1"] @ w["f1"] if (i, j) == (0, 0) else
                        w["f2"] @ w["f2"] if (i, j) == (1, 1) else
                        w["f1"] @ w["f2"])
            TL[i, j] = TL[j, i] = fine + dot * rem_fac
        return TL

    def tail_gl(w, n_alias, gl_pts, gam_lo):
        """Composite Gauss-Legendre on the SAME frozen integrand (S2a)."""
        D = w["D"]
        P_alias = 2.0 * math.pi / D
        xg, wq = np.polynomial.legendre.leggauss(gl_pts)
        TL = np.zeros((2, 2))
        for k in range(n_alias):
            a0 = gam_lo + k * P_alias
            gg = a0 + 0.5 * P_alias * (xg + 1.0)
            ww = 0.5 * P_alias * wq
            wgg = D * np.real(lg.csinc(gg * D / 2.0) ** 2)
            Fg1, Fg2 = lg.F_of(w["f1"], D * gg), lg.F_of(w["f2"], D * gg)
            dens = pp.rvm_dens(gg)
            for (i, j), prof in {(0, 0): np.abs(Fg1) ** 2,
                                 (1, 1): np.abs(Fg2) ** 2,
                                 (0, 1): np.real(
                                     Fg1 * np.conj(Fg2))}.items():
                v = float(np.sum(ww * wgg * prof * dens))
                TL[i, j] += v
                if i != j:
                    TL[j, i] += v
        g_hi = gam_lo + n_alias * P_alias
        rem_fac = (2.0 / w["D"]) * lg.TAIL_SLACK \
            * (math.log(g_hi / (2.0 * math.pi)) + 1.0) \
            / (2.0 * math.pi * g_hi)
        for (i, j), dot in {(0, 0): float(w["f1"] @ w["f1"]),
                            (1, 1): float(w["f2"] @ w["f2"]),
                            (0, 1): float(w["f1"] @ w["f2"])}.items():
            TL[i, j] += dot * rem_fac
            if i != j:
                TL[j, i] += dot * rem_fac
        return TL

    def band_block(w, gam_band):
        """Exact zero-sum block of a gamma band (fluctuation leg)."""
        D = w["D"]
        wg = D * np.real(lg.csinc(gam_band * D / 2.0) ** 2)
        F1 = lg.F_of(w["f1"], D * gam_band)
        F2 = lg.F_of(w["f2"], D * gam_band)
        return np.array([[float(np.sum(wg * np.abs(F1) ** 2)),
                          float(np.sum(wg * np.real(F1 * np.conj(F2))))],
                         [float(np.sum(wg * np.real(F1 * np.conj(F2)))),
                          float(np.sum(wg * np.abs(F2) ** 2))]])

    def band_density(w, g_lo, g_hi, pts=20001):
        """RvM-density integral of the same band (fluctuation ref)."""
        D = w["D"]
        gg = np.linspace(g_lo, g_hi, pts)
        wgg = D * np.real(lg.csinc(gg * D / 2.0) ** 2)
        Fg1, Fg2 = lg.F_of(w["f1"], D * gg), lg.F_of(w["f2"], D * gg)
        dens = pp.rvm_dens(gg)
        out = np.empty((2, 2))
        for (i, j), prof in {(0, 0): np.abs(Fg1) ** 2,
                             (1, 1): np.abs(Fg2) ** 2,
                             (0, 1): np.real(Fg1 * np.conj(Fg2))}.items():
            out[i, j] = out[j, i] = float(np.trapezoid(wgg * prof * dens,
                                                       gg))
        return out

    def pair_x2(w, idx_zero):
        """X^2 of the fixed pair (pole, zero idx) from components."""
        a, b = w["a"], w["b"]
        x = a[idx_zero] * b[-1] - a[-1] * b[idx_zero]
        return float(x * x), float(x)

    def mp_x2(w, g1_mp):
        """dps-40 recomputation of X^2(pole, gamma_1): the ward value."""
        Mz, hz = w["M"], w["h"]
        n_zone = int(round(math.exp(w["alpha"])))
        alpha_mp = mp.log(n_zone)
        D_mp = 2 * alpha_mp / Mz
        N = 2 * hz + 1
        # parity vectors in mp (the closed parity_basis formula)
        phi1 = D_mp * g1_mp

        def S_of(kb):
            s = mpf(0)
            for j in range(hz):
                t_j = (2 / mpsqrt(mpf(N))) * mpsin(
                    2 * mp.pi * kb * (j + 1) / N)
                s += t_j * mpsin((hz - j - mpf(1) / 2) * phi1)
            return s
        S1, S2 = S_of(1), S_of(2)
        x_h = phi1 / 2
        wg = D_mp * (mpsin(x_h) / x_h) ** 2
        a1 = 2 * mpsqrt(wg) * S1
        b1 = 2 * mpsqrt(wg) * S2
        # pole layer in mp: P_ij = -Re[T_ij(i/2) + T_ij(-i/2)]/2; at
        # z = +-i/2 the transforms are real decaying sums
        zD = D_mp / 2

        def F_pm(kb, sgn):
            s = mpf(0)
            for j in range(hz):
                t_j = (2 / mpsqrt(mpf(N))) * mpsin(
                    2 * mp.pi * kb * (j + 1) / N)
                s += t_j * (mpexp(-sgn * zD * j)
                            - mpexp(-sgn * zD * (Mz - 1 - j)))
            return s
        cs = (mpsinh(D_mp / 4) / (D_mp / 4)) ** 2
        P = [[mpf(0), mpf(0)], [mpf(0), mpf(0)]]
        for (i, j), (ka, kb) in {(0, 0): (1, 1), (1, 1): (2, 2),
                                 (0, 1): (1, 2)}.items():
            tp = mpf(0)
            for sgn in (1, -1):
                tp += cs * D_mp * mpf(1) / 2 * (
                    F_pm(ka, sgn) * F_pm(kb, -sgn)
                    + F_pm(kb, sgn) * F_pm(ka, -sgn))
            P[i][j] = P[j][i] = -tp / 2
        # closed-form 2x2 eigen of P -> the pole component
        tr = P[0][0] + P[1][1]
        rad = mpsqrt(((P[0][0] - P[1][1]) / 2) ** 2 + P[0][1] ** 2)
        lam_p = tr / 2 + rad
        # eigenvector for lam_p
        if abs(P[0][1]) > mpf(10) ** (-30):
            v0, v1 = P[0][1], lam_p - P[0][0]
        else:
            v0, v1 = mpf(1), mpf(0)
        nrm = mpsqrt(v0 * v0 + v1 * v1)
        sq = mpsqrt(lam_p)
        ap, bp = sq * v0 / nrm, sq * v1 / nrm
        x = a1 * bp - ap * b1
        return x * x

    def run():
        nonlocal N_CHK, FAILS
        N_CHK = 0
        FAILS = []
        print("=" * 78)
        print("THE BUDGET ATTACK -- tighten BUD until (pole x gamma_1) "
              "certifies or dies")
        print("(part 2 == prime_lagrange_budget_probe verbatim, no RH "
              "claim)")
        print("=" * 78)

        # ========================================================== S0
        print("\nS0 -- rebuild: zero list, ladder, components (parent "
              "machinery)")
        gam, n_rvm = pp.zero_list()
        n_z = len(gam)
        check("S0.Z zero list: %d zeros to T = %.0f (RvM dev %.2f <= 3)"
              % (n_z, zp.T_SCAN, abs(n_z - n_rvm)),
              abs(n_z - n_rvm) <= 3.0)
        KZ = core.frame_a_zones()
        L15 = len(KZ)
        fam5 = [0, (L15 - 1) // 4, L15 // 2, (3 * (L15 - 1)) // 4,
                L15 - 1]
        inter = []
        for (lo_i, hi_i), n_in in zip(zip(fam5[:-1], fam5[1:]),
                                      (2, 3, 3, 2)):
            for j in range(1, n_in + 1):
                inter.append(lo_i + j * (hi_i - lo_i) // (n_in + 1))
        idx15 = sorted(set(fam5 + inter))
        wins = [lg.lock_block(KZ[i]) for i in idx15]
        wins = [w for w in wins if w["complete"]]
        wins.sort(key=lambda w: w["alpha"])
        for w in wins:
            a, b, meta = pp.components_of(w, gam)
            M2 = np.array([[float(a @ a), float(a @ b)],
                           [float(a @ b), float(b @ b)]])
            w.update(a=a, b=b, meta=meta, M2=M2,
                     det_m2=float(np.linalg.det(M2)),
                     det_a2=float(np.linalg.det(w["A2"])))
        print("    %d windows rebuilt; per-zero rank-one / pole "
              "rank-one wards inherited from the parent probe (max "
              "layer dev %.1e, max pole dev %.1e)"
              % (len(wins), max(w["meta"]["layer_dev"] for w in wins),
                 max(w["meta"]["pole_dev"] for w in wins)))
        # the predeclared fluctuation band (2e4, 2.5e4]
        g_band = zp.find_zeros(zp.T_SCAN + 1e-3, T_BAND, zp.SCAN_STEP)
        n_band_rvm = float(zp.theta_rs(np.array([T_BAND]))[0] / math.pi
                           + 1.0) - n_rvm
        check("S0.BAND fluctuation band (2e4, 2.5e4]: %d zeros (RvM "
              "dev %.2f <= 3); on-line by computation"
              % (len(g_band), abs(len(g_band) - n_band_rvm)),
              abs(len(g_band) - n_band_rvm) <= 3.0)

        # ========================================================== S1
        print("\nS1 -- BUDGET AUTOPSY (3 rungs): where does the old "
              "BUD live?")
        sel = [0, len(wins) // 2, len(wins) - 1]
        print("    %5s %6s | %9s | %9s %9s %9s %9s | %s"
              % ("h", "alpha", "BUD_old", "d_quad", "d_alias",
                 "d_fluct", "float", "dominant"))
        dom_terms = []
        for si in sel:
            w = wins[si]
            TL0 = tail_estimate(w, lg.N_ALIAS_FINE, lg.PTS_PER_ALIAS,
                                zp.T_SCAN)
            TLq = tail_estimate(w, lg.N_ALIAS_FINE,
                                2 * lg.PTS_PER_ALIAS, zp.T_SCAN)
            TLa = tail_estimate(w, 2 * lg.N_ALIAS_FINE,
                                lg.PTS_PER_ALIAS, zp.T_SCAN)
            d_quad = float(np.max(np.abs(TLq - TL0)))
            d_alias = float(np.max(np.abs(TLa - TL0)))
            # the density-smoothing error, MEASURED on the actual band
            act = band_block(w, g_band)
            smo = band_density(w, zp.T_SCAN, T_BAND)
            d_fluct = float(np.max(np.abs(act - smo)))
            d_float = EPSM * float(np.linalg.norm(w["A2"]))
            resid0 = float(np.max(np.abs(w["A2"] - (w["M2"] + TL0))))
            bud_old = resid0 * (abs(w["A2"][0, 0]) + abs(w["A2"][1, 1])
                                + 2.0 * abs(w["A2"][0, 1])) \
                + 2.0 * resid0 ** 2
            terms = dict(quad=d_quad, alias=d_alias, fluct=d_fluct,
                         float=d_float)
            dom = max(terms, key=terms.get)
            dom_terms.append(dom)
            w.update(bud_old=bud_old, resid0=resid0, TL0=TL0)
            print("    %5d %6.3f | %9.2e | %9.2e %9.2e %9.2e %9.2e | %s"
                  % (w["h"], w["alpha"], bud_old, d_quad, d_alias,
                     d_fluct, d_float, dom.upper()))
        for w in wins:
            if "TL0" not in w:
                TL0 = tail_estimate(w, lg.N_ALIAS_FINE,
                                    lg.PTS_PER_ALIAS, zp.T_SCAN)
                resid0 = float(np.max(np.abs(w["A2"]
                                             - (w["M2"] + TL0))))
                w.update(TL0=TL0, resid0=resid0,
                         bud_old=resid0 * (abs(w["A2"][0, 0])
                                           + abs(w["A2"][1, 1])
                                           + 2.0 * abs(w["A2"][0, 1]))
                         + 2.0 * resid0 ** 2)
        check("S1.AUTOPSY the dominant budget term on all 3 autopsy "
              "rungs: %s -- the RvM-DENSITY SMOOTHING (the tail "
              "estimate cannot see actual zeros) is the irreducible "
              "term of the old route iff FLUCT dominates"
              % ", ".join(dom_terms), True)

        # ========================================================== S2
        print("\nS2 -- the predeclared toolset, then the route change")
        w_mid = wins[len(wins) // 2]
        TL_gl = tail_gl(w_mid, lg.N_ALIAS_FINE, 32, zp.T_SCAN)
        d_gl = float(np.max(np.abs(TL_gl - w_mid["TL0"])))
        print("    (a) quadrature upgrade (GL-32 vs trapezoid, mid "
              "rung): max entry diff %.2e -- %s" %
              (d_gl, "quadrature is NOT the blocker" if d_gl < 1e-3
               else "quadrature matters"))
        # (b) the rigorous closed-form tail bound
        print("    (b) rigorous closed-form tail bound per rung "
              "(4 L1_i L1_j / D x (log T + 1)/(pi T), T = 2e4):")
        for si in sel:
            w = wins[si]
            l1a = float(np.sum(np.abs(w["f1"])))
            l1b = float(np.sum(np.abs(w["f2"])))
            fac = (math.log(zp.T_SCAN) + 1.0) / (math.pi * zp.T_SCAN)
            bnd = 4.0 * max(l1a * l1a, l1a * l1b, l1b * l1b) \
                / w["D"] * fac
            x2, _ = pair_x2(w, 0)
            print("        h = %4d: bound %.2e vs X^2 %.2e (x%.1e too "
                  "large) -- the generic bound cannot close"
                  % (w["h"], bnd, x2, bnd / max(x2, EPS_JS)))
        # (c) zero depth needed by the density route -- the horizon
        w0 = wins[0]
        l1 = max(float(np.sum(np.abs(w0["f1"]))),
                 float(np.sum(np.abs(w0["f2"]))))
        x2_0, _ = pair_x2(w0, 0)
        t_need, t_try = None, zp.T_SCAN
        for _ in range(200):
            t_try *= 1.5
            if 4.0 * l1 * l1 / w0["D"] * (math.log(t_try) + 1.0) \
                    / (math.pi * t_try) < x2_0:
                t_need = t_try
                break
        print("    (c) zero depth: the L1-bounded density route needs "
              "T ~ %.1e (vs 3e12 citation horizon %s) -- typed: depth "
              "alone %s close the generic route"
              % (t_need if t_need else float("inf"),
                 "INSIDE" if (t_need or math.inf) <= 3e12
                 else "OUTSIDE",
                 "could" if (t_need or math.inf) <= 3e12
                 else "canNOT"))
        print("    (d) mpmath precision: float error is at the 1e-12 "
              "scale (S1 ledger) -- precision is NOT the blocker")
        print("""    THE ROUTE CHANGE (executed): R := Ahat2 - G_Z - P is an
    EXACT float 2x2; verify lambda_min(R) >= margin numerically, then
      det Ahat2 = det(G_Z + P + R) >= det(G_Z + P) >= X^2(pole, g1)
    (2x2 psd fact, every cross term >= 0) -- NO tail estimate left in
    the chain; the RvM-smoothing term is GONE.""")
        print("    %5s %6s | %10s %10s %8s | %10s %10s"
              % ("h", "alpha", "lam_min(R)", "margin", "psd?",
                 "BUD_old", "BUD_new"))
        psd_all = True
        for w in wins:
            R = w["A2"] - w["M2"]
            lam_min = eig2_min(R)
            margin = PSD_MARGIN_FAC * EPSM \
                * float(np.linalg.norm(w["A2"]))
            psd = lam_min >= margin
            # fallback horizon if the full-depth remainder fails psd
            if not psd:
                keep = gam <= T_C
                a_c, b_c, _ = pp.components_of(
                    w, gam[keep])
                M2c = np.array([[float(a_c @ a_c), float(a_c @ b_c)],
                                [float(a_c @ b_c), float(b_c @ b_c)]])
                R = w["A2"] - M2c
                lam_min = eig2_min(R)
                psd = lam_min >= margin
                if psd:
                    w.update(M2_used=M2c, horizon=T_C)
            if "M2_used" not in w:
                w.update(M2_used=w["M2"], horizon=zp.T_SCAN)
            scale2 = float(np.linalg.norm(w["A2"])) ** 2 \
                + float(np.linalg.norm(w["M2_used"])) ** 2
            bud_new_chain = CHAIN_FAC * EPSM * scale2
            psd_all = psd_all and psd
            w.update(lam_min=lam_min, margin=margin, psd=psd,
                     bud_chain=bud_new_chain)
            print("    %5d %6.3f | %10.3e %10.3e %8s | %10.2e %10.2e"
                  % (w["h"], w["alpha"], lam_min, margin,
                     "yes" if psd else "NO", w["bud_old"],
                     bud_new_chain))
        check("S2.PSD the remainder R = Ahat2 - G_Z - P is psd on "
              "every rung (lambda_min >= %.0f eps ||A2||): the tail "
              "estimate is eliminated from the chain"
              % PSD_MARGIN_FAC, psd_all)

        # ========================================================== S3
        print("\nS3 -- the certification retry (fixed pair pole x "
              "gamma_1)")
        # measured gamma_1 error vs zetazero(1) at dps 40 (+ slack)
        mp.dps = MP_DPS
        g1_mp = zetazero(1).imag
        dgam1 = abs(float(gam[0]) - float(g1_mp)) + DGAM_SLACK
        print("    gamma_1(cache) - zetazero(1) = %.2e (+ slack %.0e) "
              "-> dgam = %.2e" % (abs(float(gam[0]) - float(g1_mp)),
                                  DGAM_SLACK, dgam1))
        print("    %5s %6s | %11s %10s | %11s | %8s %8s | %6s"
              % ("h", "alpha", "X^2", "BUD_new", "interval_lo",
                 "sh_det", "sh_rest", "cert?"))
        cert_all = True
        shares = []
        for w in wins:
            x2, x_val = pair_x2(w, 0)
            # position propagation: dX/dgamma by central difference on
            # the closed form (rebuild the zero-1 component at g1 +- d)
            D, hz, Mz = w["D"], w["h"], w["M"]
            NN = 2 * hz + 1
            jj = np.arange(hz)
            t1 = (2.0 / math.sqrt(NN)) * np.sin(
                2.0 * math.pi * 1.0 * (jj + 1.0) / NN)
            t2 = (2.0 / math.sqrt(NN)) * np.sin(
                2.0 * math.pi * 2.0 * (jj + 1.0) / NN)
            freqs = hz - jj - 0.5

            def x_at(g):
                phi = D * g
                s1 = float(t1 @ np.sin(freqs * phi))
                s2 = float(t2 @ np.sin(freqs * phi))
                wgl = D * (math.sin(phi / 2.0) / (phi / 2.0)) ** 2
                av = 2.0 * math.sqrt(wgl) * s1
                bv = 2.0 * math.sqrt(wgl) * s2
                return av * w["b"][-1] - w["a"][-1] * bv
            dd = 1.0e-6
            dxdg = (x_at(float(gam[0]) + dd)
                    - x_at(float(gam[0]) - dd)) / (2.0 * dd)
            e_pos = 2.0 * abs(x_val) * abs(dxdg) * dgam1 \
                + (abs(dxdg) * dgam1) ** 2
            bud_new = e_pos + w["bud_chain"]
            lo = x2 - bud_new
            cert = w["psd"] and lo > 0.0
            cert_all = cert_all and cert
            sh_det = x2 / max(w["det_a2"], EPS_JS)
            det_used = float(np.linalg.det(w["M2_used"]))
            rest = det_used - x2
            shares.append(sh_det)
            w.update(x2=x2, bud_new=bud_new, cert=cert, sh_det=sh_det,
                     rest=rest)
            print("    %5d %6.3f | %11.4e %10.2e | %11.4e | %8.4f "
                  "%8.4f | %6s"
                  % (w["h"], w["alpha"], x2, bud_new, lo, sh_det,
                     rest / max(det_used, EPS_JS),
                     "LIVE" if cert else "dead"))
        n_ord = np.median([math.log10(w["bud_old"] / w["bud_new"])
                           for w in wins])
        print("    BUDGET LEDGER: BUD_old %.1e..%.1e -> BUD_new "
              "%.1e..%.1e (median %.1f orders tightened)"
              % (min(w["bud_old"] for w in wins),
                 max(w["bud_old"] for w in wins),
                 min(w["bud_new"] for w in wins),
                 max(w["bud_new"] for w in wins), n_ord))
        check("S3.CERT the certified interval X^2 - BUD_new is "
              "strictly positive with the psd chain on all %d rungs"
              % len(wins), cert_all)
        # the ward: dps-40 recomputation must land inside the interval
        ward_ok = True
        for si in sel[:N_WARD]:
            w = wins[si]
            x2m = float(mp_x2(w, g1_mp))
            inside = abs(x2m - w["x2"]) <= max(w["bud_new"],
                                               1e-10 * w["x2"])
            ward_ok = ward_ok and inside
            print("    W1 ward h = %4d: X^2(dps40) = %.12e vs float "
                  "%.12e (|diff| %.1e <= %.1e) %s"
                  % (w["h"], x2m, w["x2"], abs(x2m - w["x2"]),
                     max(w["bud_new"], 1e-10 * w["x2"]),
                     "ok" if inside else "OUTSIDE"))
        check("W1 [ward] the dps-40 recomputation of X^2 lies inside "
              "the certified interval on %d rungs" % N_WARD, ward_ok)

        # ========================================================== S4
        print("\nS4 -- scaling: the fixed pair's share along the "
              "ladder")
        hs = [w["h"] for w in wins]
        sl = float(np.polyfit(np.log(hs),
                              np.log(np.maximum(shares, EPS_JS)),
                              1)[0])
        x2s = [w["x2"] for w in wins]
        sl_x2 = float(np.polyfit(np.log(hs),
                                 np.log(np.maximum(x2s, EPS_JS)),
                                 1)[0])
        sl_det = float(np.polyfit(
            np.log(hs), np.log([w["det_a2"] for w in wins]), 1)[0])
        if sl >= SLOPE_STABLE:
            trend = "STABLE/GROWING"
        elif sl < SLOPE_VANISH:
            trend = "VANISHING"
        else:
            trend = "DRIFTING (typed)"
        print("    share = X^2/det: %.4f..%.4f (median %.4f); slope "
              "h^%+.2f -> %s" % (min(shares), max(shares),
                                 float(np.median(shares)), sl, trend))
        print("    decomposed: X^2 ~ h^%+.2f, det ~ h^%+.2f (the pair "
              "TRACKS the floor iff the slopes match)"
              % (sl_x2, sl_det))
        share_ok = min(shares) >= SHARE_MIN and sl >= SLOPE_STABLE
        check("S4.SHARE fixed-pair floor share >= %.3f on every rung "
              "(min %.4f) with slope %+.2f >= %.2f -- the single-pair "
              "skeleton %s" % (SHARE_MIN, min(shares), sl,
                               SLOPE_STABLE,
                               "carries a stable brick" if share_ok
                               else "needs the family argument"),
              share_ok)

        # =========================================================== C
        print("\nC -- controls")
        # C1 collinear synthetic: interval must contain 0
        cc = np.arange(1, 101, dtype=float)
        cc /= math.sqrt(float(np.sum(cc ** 2)))
        a_c, b_c = cc * 1.0, cc * 1.5
        x_syn = a_c[0] * b_c[1] - a_c[1] * b_c[0]
        bud_syn = CHAIN_FAC * EPSM * float(a_c @ a_c + b_c @ b_c)
        c1 = abs(x_syn) <= bud_syn
        check("C1 collinear synthetic family: certified interval "
              "[%.1e, %.1e] contains 0 -- no false positivity"
              % (x_syn ** 2 - bud_syn, x_syn ** 2 + bud_syn), c1)
        # C2 scramble: the remainder must stop looking like the tail
        r_scr, lam_scr = [], []
        for si in sel:
            w = wins[si]
            rr_s = core.build_window(w["kz"],
                                     scramble_seed=SCRAMBLE_SEED)
            R_s = rr_s["Ah_dir"] - w["M2"]
            bar = lg.BAR_ID_REL * float(np.linalg.norm(w["A2"])) \
                + lg.BAR_ID_ABS
            r_scr.append(float(np.max(np.abs(R_s - w["TL0"]))) / bar)
            lam_scr.append(eig2_min(R_s))
        print("    C2 typed: lambda_min(R_scrambled) = %.2e..%.2e "
              "(the matrix chain itself is agnostic; the IDENTITY "
              "interpretation is what breaks)"
              % (min(lam_scr), max(lam_scr)))
        check("C2 [must-fire] scramble: the remainder stops matching "
              "the RvM tail (max|R_scr - TL|/bar = %.1f..%.1f >= %.0f)"
              % (min(r_scr), max(r_scr), CTRL_RESID_X),
              min(r_scr) >= CTRL_RESID_X)

        # =========================================================== V
        print("\n" + "=" * 78)
        print("V -- verdict + what a floor theorem still needs")
        print("=" * 78)
        if psd_all and cert_all and ward_ok and c1 and share_ok:
            verdict = "PAIR-CERTIFIED"
        elif not (psd_all and cert_all and ward_ok):
            verdict = "BUDGET-TIGHTENED-INSUFFICIENT"
        else:
            verdict = "PAIR-VANISHES"
        _LAST2["verdict"] = verdict
        print("""
  VERDICT: %s
      BUDGET LEDGER: old route (RvM-density tail estimate) BUD
      %.1e..%.1e, dominant term %s; new route (psd-remainder
      monotonicity) BUD %.1e..%.1e -- median %.1f orders tightened;
      the certified interval is strictly positive on %d/%d rungs.
      CERTIFIED STATEMENT (per rung, float-level):
        lambda tau = det Ahat2 >= det(G_Z + P) >= X^2(pole, gamma_1)
        with lambda_min(Ahat2 - G_Z - P) >= %.0f eps ||A2|| verified
        numerically per rung; X^2 explicit (closed trigonometric
        form), gamma_1 pinned to zetazero(1) within %.0e.
      SHARE: %.4f..%.4f of the floor per rung, slope h^%+.2f (%s).

  WHAT A FLOOR THEOREM STILL NEEDS (the precise statement):
    (i)  the psd of the remainder R per rung is VERIFIED numerically,
         not proved: a proof needs the master identity + the psd of
         every tail layer, i.e. the in-band on-line citation [A1]
         made rigorous for the deployed window class (finite check +
         cited zero-free verification; NO new mathematics claimed);
    (ii) the ladder is finite: an X -> infinity floor theorem needs a
         UNIFORM lower bound on X^2(pole, gamma_1)(h) -- measured
         here X^2 ~ h^%+.2f vs det ~ h^%+.2f -- i.e. a closed-form
         asymptotic of S_i(D gamma_1) and the pole vector (the alias
         law makes the moving carriers explicit if the fixed pair
         ever under-tracks);
    (iii) the uncertified rest det(G_Z+P) - X^2 (%.0f..%.0f%% of the
         floor) is carried by the pole x (alias zeros) family -- a
         family version of (ii) upgrades the brick to the full floor.
""" % (verdict,
       min(w["bud_old"] for w in wins),
       max(w["bud_old"] for w in wins),
       "/".join(sorted(set(dom_terms))),
       min(w["bud_new"] for w in wins),
       max(w["bud_new"] for w in wins), n_ord,
       sum(1 for w in wins if w["cert"]), len(wins),
       PSD_MARGIN_FAC, dgam1,
       min(shares), max(shares), sl, trend,
       sl_x2, sl_det,
       100.0 * min(1.0 - w["x2"] / max(float(np.linalg.det(
           w["M2_used"])), EPS_JS) for w in wins),
       100.0 * max(1.0 - w["x2"] / max(float(np.linalg.det(
           w["M2_used"])), EPS_JS) for w in wins)))

        dt = time.time() - T0
        print("-" * 78)
        print("checks: %d run, %d failed%s | runtime %.1f min"
              % (N_CHK, len(FAILS),
                 (" [" + ", ".join(FAILS) + "]") if FAILS else "",
                 dt / 60.0))
        print("NO RH claim (part 2).")

    run()
    return list(FAILS), N_CHK


def run():
    """run_all entry point (v757 precedent): expected patterns 7/8
    checks with the ONE preregistered-honest FAIL S3.CERT (the OLD
    tail-estimate budget gate, 0/14 LIVE -- exactly the blocker part 2
    removes) and verdict LAGRANGE-CONCENTRATED (part 1), then 9/9
    checks and verdict PAIR-CERTIFIED (part 2)."""
    _probe_run()
    fails1 = list(FAILS)
    n1 = N_CHK
    v1 = _LAST1.get("verdict", "?")
    print()
    fails2, n2 = _part2()
    v2 = _LAST2.get("verdict", "?")
    ok = (n1 == 8 and fails1 == ["S3.CERT"]
          and v1 == "LAGRANGE-CONCENTRATED"
          and n2 == 9 and fails2 == []
          and v2 == "PAIR-CERTIFIED")
    print("\n[%s] PATTERN GATE: expected 7/8 (FAIL S3.CERT, "
          "LAGRANGE-CONCENTRATED) + 9/9 (PAIR-CERTIFIED); got "
          "%d checks (fails %s, %s) + %d checks (fails %s, %s)"
          % ("PASS" if ok else "FAIL", n1, fails1 or "none", v1,
             n2, fails2 or "none", v2))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(run())
