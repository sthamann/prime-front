#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""inner_zone_linear_probe -- PRIME.CASE.INNERLINEAR.01
(EXPLORATION ONLY, experiments/; round 52, named object (c): the
INNER-ZONE LINEAR ROUTE of the diagonal half -- the refinement
opened by ENDPOINT-PARTIAL.  2026-08-09.)

CONTEXT (machinery verbatim from endpoint_bracket_probe /
paircorr_contract_probe / signed_homotopy_probe): round 51 measured
the one-sided endpoint derivative F'(1) of the diagonal-half
homotopy against the PNT-reference deficit and typed the census
ENDPOINT-PARTIAL: F'(1) >= deficit passes on ALL small-a cells of
the deep rungs with monotone margins, fails at shallow rungs and at
the zone edge a ~ h^{1.4}; the truth/PNT kernel distance
||K^(1) - K^(0)|| / ||K^(0)|| is 0.16..0.4 deep (p1 ~ p0 stability
plausible) and 0.89 shallow; the concavity drop F'(0) - F'(1)
shrinks at log-log slope -1.5.  christoffel_zone_envelope_probe
froze the critical zone a <= h^{2 theta*}, theta* = 0.700;
paircorr_contract_probe froze the kernel regrouping
J = sum_n mu_n K_{h,m}(log n) - K0 and the deficit ledger.  THIS
probe asks: is there an INNER exponent theta_in < theta* such that
on the inner zone {a <= h^{2 theta_in}} the LINEAR route (the
one-sided endpoint bound F'(1) >= deficit) covers EVERYTHING on the
deep half -- so the genuinely hard part (the pair-correlation
input) contracts from the whole zone to the MIDDLE BAND
h^{2 theta_in} < a <= h^{1.4}?

FROZEN PROTOCOL (2026-08-09; constants frozen before the first
measurement run; budget < 20 min):

 RUNGS: heavy kz {9, 12, 13, 26, 40} + the deepest 3 with complete
   atom tables kz {88, 90, 116} (verbatim round-51 selection;
   X <= 4e5).  DEEP HALF = the 4 highest-h rungs of the 8 (sorted
   by (h, kz) ascending).
 ALIASES: all port aliases in the frozen critical zone -- truth
   neg nodes (d_1(f) < 0, f >= 1) with a_{h,f} = 2 h^2 (1 - x_f)
   <= h^{2 theta*}, theta* = 0.700, ranked by a ascending
   (verbatim).  Per rung: deficit_m = (nu_0 - lambda_0)_m =
   -F_m(0), the endpoint derivatives F'(0) = J at t = 0 and
   F'(1) = J at t = 1 (exact envelope formula, verbatim round-51),
   the exact full difference Delta_m = F(1) - F(0), the linear
   margin margin1 = F'(1) - deficit and the full margin
   marginF = Delta - deficit = (lambda_1 - nu_1)_m (exact
   identity).

 Z1 THE INNER EXPONENT: for theta_in in the frozen grid
   {0.40, 0.50, 0.60, 2/3, 0.70} restrict to the inner cells
   a_m <= h^{2 theta_in}; census per rung: pass iff margin1 >= 0
   on every inner cell.  ELIGIBILITY of a grid theta_in
   (pre-registered): (i) the inner set is NONEMPTY on every
   deep-half rung (a vacuous census does not count), (ii) 100%
   pass on every deep-half rung, (iii) POSITIVE MARGIN TREND: all
   deep-half inner min margins > 0 and the least-squares slope of
   log(min margin) vs log(h) over the 4 deep-half rungs is > 0.
   theta_in* = the LARGEST eligible grid theta_in.  Census table
   printed for ALL 8 rungs (the shallow failures stay disclosed).
   TYPED: INNER-ZONE(theta_in*) iff some grid point is eligible,
   else INNER-EMPTY.

 Z2 THE MIDDLE-BAND ACCOUNTING (at theta_in*; if INNER-EMPTY, at
   the frozen fallback 2/3, disclosed, for the record): the BAND =
   zone cells with h^{2 theta_in*} < a_m <= h^{1.4}.  Per rung:
   n_band, n_zone, the band fraction n_band/n_zone, the band
   census under the FULL nonlinear difference (pass iff
   marginF >= 0 -- the homotopy truth; this is where the
   pair-correlation input remains), min/median band marginF, the
   per-cell table (first 6 + argmin).  The h-trend of the band
   fraction: least-squares slope of log(fraction) vs log(h) over
   the rungs with a nonempty band (SHRINKING iff slope < 0;
   n/a if < 3 usable rungs, disclosed).

 Z3 THE STABILITY LEMMA SHADOW (deep-half rungs): per INNER-zone
   alias (not just the critical one) the kernel distance
   relK_m = ||K^(1)_m - K^(0)_m|| / ||K^(0)_m|| and the cosine
   corr(K^(0)_m, K^(1)_m) on the lag grid i = 1..M-1 (verbatim
   round-51 E3 comparison, extended to the full inner profile);
   per rung the profile rows (first 10 + argmax relK), max and
   median relK.  THE LINEAR-ROUTE THEOREM SKELETON printed with
   the measured numbers filled in: IF (i) p1 ~ p0 stability at the
   measured level on the inner zone (kernel transfer error
   controlled by the printed relK profile), AND (ii) the ONE-SIDED
   linear bound sum_n mu_n K^(0)_{h,m}(log n) - K0 >= deficit_m +
   stability-error on the inner zone, THEN T_h <= 1 on the inner
   zone; the remaining hard part is the BAND, not the zone.  The
   K^(0) census (F'(0) >= deficit, the PNT-computable side) is
   printed alongside on the inner cells; the transfer gap
   F'(0) - F'(1) per inner cell is the measured stability-error
   scale.  THE BAND SIZE, honestly: per deep rung the band alias
   fraction n_band/n_zone, the band nu_1-mass fraction
   sum_band nu_1 / sum_zone nu_1 and the band deficit fraction
   sum_band deficit / sum_zone deficit.

 Z4 THE CLASSICAL FORM OF THE INNER HYPOTHESIS (report; all 8
   rungs): the PNT-side kernels K^(0)_m restricted to the inner
   zone, profiled exactly as paircorr_contract P1/P3: per alias
   n90 = the number of f-modes carrying 90% of sum_f |W_{f,m}|
   (f >= 1), the 90%-mass support width fraction u_frac =
   width90/(2 alpha) (smallest contiguous u-window carrying 90%
   of sum_i |K(iD)|), and the |W|-weighted mean alias frequency
   tau_mean.  Printed per rung: inner rows (first 8) and band
   rows (first 6) + the inner/band medians.  FROZEN comparative
   reading per rung (needs both sets nonempty): the inner kernels
   are SOFTER iff median u_frac(inner) <= median u_frac(band) AND
   median tau_mean(inner) <= median tau_mean(band).  TYPED:
   CLASSICAL=INNER-SOFTER iff softer on a strict majority of the
   comparable rungs, INNER-NOT-SOFTER else, n/a iff < 2 rungs
   comparable (band empty almost everywhere).

 C  CONTROLS (kz 9, scramble seed 1, the deployed mirror:
   positions uniform on (0, 2 alpha), same masses; frozen control
   exponent theta_ctrl = 2/3, frozen BEFORE theta_in* is known):
   the scramble INNER census must BREAK -- with scramble aliases
   = scramble neg nodes with a <= h^{2 theta_ctrl} (fallback,
   disclosed if empty: the 8 a-closest scramble neg nodes), the
   min over them of F'_scr(1) - deficit_scr must be < 0
   (deficit_scr = (nu_0 - lambda_0) at the scramble alias nodes;
   F'_scr(1) = the truth-side envelope formula at d_scr with
   residual r_s = d_scr - d_0, verbatim round-51 control).
   Silent -> CONTROL-DEAD.

 WARDS (kill WARD-BROKEN on failure; verbatim round-50/51):
   (W-A) prime-side regrouping == grid form at BOTH endpoints,
         rel <= 1e-10 per alias against max(|W.r|, sum_n mu_n |K|
         + |K0|);
   (W-B) smooth-subtraction route a (W.d0at) == route b (c0.chat)
         at both endpoints, rel <= 1e-12.
   (The round-51 W-C endpoint FD ward is NOT repeated here: the
   identical F' values were FD-certified in round 51; dropping a
   passed ward adds no risk and saves 16 chain builds.)

 SELF-TESTS (S0, kill PIPELINE on failure): (i) AST firewall
   clean; (ii) endpoint reconstruction (kz 9): the qt-route
   lambda/nu at the zone aliases vs the verbatim folded_measure
   route, rel <= 1e-8, at both t = 0 and t = 1; (iii) quadratic-
   form self-test per rung at both endpoints: sum_j w_j p*^2 ==
   lambda to rel 1e-8 (verbatim TOL_QF).

KILLS: chain short anywhere needed / self-test failure / zone
alias set empty on a rung -> PIPELINE-BROKEN; W-A / W-B ward
failure -> WARD-BROKEN; value control silent -> CONTROL-DEAD.
Z1 / Z2 / Z3 / Z4 outcomes are MEASUREMENTS, never kills:
INNER-EMPTY is a finding.

VERDICT (frozen enum): INNERLINEAR-MEASURED (+ TYPE=<INNER-
ZONE(theta_in*) | INNER-EMPTY> + BAND=<n cells, SHRINKING |
NON-SHRINKING | n/a> + STABILITY=<max inner relK deep> +
CLASSICAL=<INNER-SOFTER | INNER-NOT-SOFTER | n/a>) /
PIPELINE-BROKEN / WARD-BROKEN / CONTROL-DEAD.

SPEC AMENDMENTS (fail-first preserved):
  v1 (2026-08-09): initial freeze.  The rung set, alias
  bookkeeping, envelope formula, kernel regrouping, wards and the
  scramble mirror are verbatim round-50/51 machinery; the inner
  grid {0.40, 0.50, 0.60, 2/3, 0.70}, the eligibility rule
  (nonempty + 100% deep pass + positive trend), the Z2 fallback
  2/3, the Z4 softness rule and the control exponent 2/3 were all
  frozen before any number was computed.
  v2 (2026-08-09, after the first full run; fail-first preserved):
  the first run returned INNERLINEAR-MEASURED with TYPE=INNER-EMPTY
  and every ward green -- the deep-half census is 100% at theta_in
  = 0.40 and 0.50 but the ABSOLUTE min-margin h-trend is -1.05, so
  criterion (iii) fails.  Because every scale of the problem
  (deficit, F'(0), F'(1)) itself shrinks like ~ h^-1 on this
  ladder, the absolute trend conflates the global scale shrinkage
  with a genuine margin decay.  v2 ADDS two DISCLOSED diagnostics
  to the Z1 print for census-passing grid points, both pure
  measurements: (a) the scale-normalized trend, the least-squares
  slope of log(h x min margin) vs log(h) over the deep half, and
  (b) the round-51-style within-rung monotonicity flag per deep
  rung (margin1 non-increasing along a ascending).  The
  ELIGIBILITY RULE AND THE TYPED OUTCOME ARE UNCHANGED (v1 rule;
  the first-run verdict INNER-EMPTY stands); no bar moved, no
  measured number changed.

NO RH claim: every number is finite exact linear algebra /
calculus on the deployed v563 window family; a frozen theta_in*
is an inner-zone split of the finite ladder shadow, not a bound,
no rate, no uniformity in h, and the linear route carries the
round-51 circularity caveat verbatim (K^(1) is truth-built; the
transfer to K^(0) NEEDS the stability lemma whose measured shadow
Z3 prints).  No marker moves.

FIREWALL: no zeros, no prime oracles beyond the deployed table
(AST scan: zetazero/nzeros/primerange/isprime/primepi/nextprime/
prevprime banned); v563 READ-ONLY; RNG only in the scramble
control; stdout only.

Sources (read-only): v563_paper2_readouts (window geometry, tent
assembly, arch lags, deployed atom table); endpoint_bracket_probe
(endpoint derivatives, wards, deep-rung selection -- verbatim);
signed_homotopy_probe (envelope identity, eval machinery --
verbatim); paircorr_contract_probe (kernel regrouping W/chat/K,
profile machinery n90/width90/tau, deficit ledger -- verbatim);
christoffel_pnt_gamma_probe (W2 closed-form PNT lags, folded
measures, Lanczos chain); christoffel_zone_envelope_probe
(theta* = 0.700), declared inputs.

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/inner_zone_linear_probe.py
"""

import ast
import hashlib
import math
import os
import sys
import time

import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
_VERIFY = os.path.abspath(os.path.join(_HERE, "..", "..",
                                       "verification"))
sys.path.insert(0, _HERE)
sys.path.insert(0, _VERIFY)

import v563_paper2_readouts as core        # noqa: E402  (READ-ONLY)

HEAVY = (9, 12, 13, 26, 40)
DEEP3 = (88, 90, 116)          # frozen (round-51 selection)
RUNGS = tuple(sorted(set(HEAVY) | set(DEEP3)))
THETA_STAR = 0.700             # frozen zone exponent (ZONESPLIT.01)
INNER_GRID = (0.40, 0.50, 0.60, 2.0 / 3.0, 0.70)   # Z1 frozen grid
THETA_FALLBACK = 2.0 / 3.0     # Z2 fallback iff INNER-EMPTY
THETA_CTRL = 2.0 / 3.0         # C: frozen control exponent
TOL_WARD_PRIME = 1.0e-10       # W-A: prime-side form == grid form
TOL_WARD_K0 = 1.0e-12          # W-B: K0 route a == route b
TOL_SELF_END = 1.0e-8          # S0.2 endpoint reconstruction
TOL_QF = 1.0e-8                # S0.3 quadratic-form self-test
FRAC_MASS = 0.90               # Z4 profile mass fraction (frozen)
SHOW_Z1 = 8                    # Z1: all 8 rungs printed
SHOW_BAND = 6                  # Z2: band rows shown per rung
SHOW_STAB = 10                 # Z3: inner profile rows per rung
SHOW_IN = 8                    # Z4: inner rows shown per rung
MIN_TREND_RUNGS = 3            # Z2: rungs needed for a slope
SCRAMBLE_SEED = 1
CTRL_FALLBACK_AL = 8           # C: a-closest neg nodes fallback
BANNED_IDS = ("zetazero", "nzeros", "primerange", "isprime",
              "primepi", "nextprime", "prevprime")

CHECKS = []
KILLS = []
T0 = time.time()


def check(name, ok, detail="", kill=None):
    CHECKS.append((name, bool(ok)))
    if kill and not ok:
        KILLS.append(kill)
    print("  [%s] %s%s" % ("PASS" if ok else "FAIL", name,
                           ("  -- " + detail) if detail else ""),
          flush=True)
    return bool(ok)


def section(title):
    print("\n" + "=" * 74)
    print(title)
    print("=" * 74, flush=True)


def ast_scan(banned):
    src = open(os.path.abspath(__file__), encoding="utf-8").read()
    bad = []
    for node in ast.walk(ast.parse(src)):
        name = None
        if isinstance(node, ast.Name):
            name = node.id
        elif isinstance(node, ast.Attribute):
            name = node.attr
        if name and name.lower() in banned:
            bad.append(name)
    return bad


# ------------------------------------------------------------------ pipeline
# (grid density, folded measures, Lanczos chain, CD kernel, W2 closed-form
#  PNT lags: verbatim from endpoint_bracket_probe / paircorr_contract_probe)

def grid_density(c):
    c = np.asarray(c, float)
    a = np.concatenate([c, c[-2:0:-1]])
    d = np.fft.fft(a)
    assert float(np.max(np.abs(d.imag))) <= 1e-9 * max(
        1.0, float(np.max(np.abs(d.real))))
    return d.real


def folded_measure(d_arm, L, sign=+1.0):
    jj = np.arange(L)
    keep = (sign * d_arm) > 0.0
    jj = jj[keep]
    th = 2.0 * math.pi * jj / L
    wt = (np.abs(d_arm[keep]) / (2.0 * L)) * 4.0 * np.sin(
        th / 2.0) ** 2
    fold = np.minimum(jj, L - jj)
    uf, inv = np.unique(fold, return_inverse=True)
    wagg = np.zeros(len(uf))
    np.add.at(wagg, inv, wt)
    xs = np.cos(2.0 * math.pi * uf / L)
    m = wagg > 1e-300
    return xs[m], wagg[m], uf[m]


def lanczos_chain(x, w, n):
    m0 = float(np.sum(w))
    m = len(x)
    Q = np.zeros((m, n))
    Q[:, 0] = np.sqrt(w) / math.sqrt(m0)
    al = np.zeros(n)
    be = np.zeros(max(n - 1, 0))
    steps = n
    for k in range(n):
        z = x * Q[:, k]
        al[k] = float(Q[:, k] @ z)
        z = z - al[k] * Q[:, k]
        if k > 0:
            z = z - be[k - 1] * Q[:, k - 1]
        for _ in range(2):
            z = z - Q[:, :k + 1] @ (Q[:, :k + 1].T @ z)
        if k == n - 1:
            break
        bnorm = float(np.linalg.norm(z))
        if bnorm <= 1e-14:
            steps = k + 1
            break
        be[k] = bnorm
        Q[:, k + 1] = z / bnorm
    return al[:steps], be[:max(steps - 1, 0)], m0, steps


def eval_chain(al, be, m0, y, n):
    P = np.zeros((len(y), n))
    P[:, 0] = 1.0 / math.sqrt(m0)
    if n > 1:
        P[:, 1] = (y - al[0]) * P[:, 0] / be[0]
    for k in range(1, n - 1):
        P[:, k + 1] = ((y - al[k]) * P[:, k]
                       - be[k - 1] * P[:, k - 1]) / be[k]
    return P


def _prim(u, A, B):
    """Primitive of (A + B u) 2 e^{u/2}: 4 e^{u/2} (A + B (u - 2))."""
    return 4.0 * np.exp(0.5 * u) * (A + B * (u - 2.0))


def cont_lags(alpha, M, seg_lo, seg_hi, seg_sc):
    """W2 closed-form PNT tent lags (verbatim, incl. i=0 mirror)."""
    D = 2.0 * alpha / M
    c = np.zeros(M)
    for lo, hi, sc in zip(seg_lo, seg_hi, seg_sc):
        i0 = max(0, int(math.floor(lo / D)) - 1)
        i1 = min(M - 1, int(math.ceil(hi / D)) + 1)
        ii = np.arange(i0, i1 + 1, dtype=float)
        val = np.zeros(len(ii))
        a = np.maximum((ii - 1.0) * D, lo)          # rising piece
        b = np.minimum(ii * D, hi)
        m = b > a
        val[m] += (_prim(b[m], 1.0 - ii[m], 1.0 / D)
                   - _prim(a[m], 1.0 - ii[m], 1.0 / D))
        a = np.maximum(ii * D, lo)                  # falling piece
        b = np.minimum((ii + 1.0) * D, hi)
        m = b > a
        val[m] += (_prim(b[m], 1.0 + ii[m], -1.0 / D)
                   - _prim(a[m], 1.0 + ii[m], -1.0 / D))
        if i0 == 0:                                 # i = 0 reflection
            a0, b0 = max(0.0, lo), min(D, hi)
            if b0 > a0:
                val[0] += (_prim(b0, 1.0, -1.0 / D)
                           - _prim(a0, 1.0, -1.0 / D))
        c[i0:i1 + 1] -= 0.5 * sc * val
    return c


# --------------------------------------------------------- rung construction
def build_rung(kz):
    """Folded d_PNT, d_truth, residual, weights and zone aliases of
    one rung (verbatim round-51)."""
    rr = core.build_window(kz)
    alpha, M, h, D = rr["alpha"], rr["M"], rr["h"], rr["D"]
    assert abs(D - 2.0 * alpha / M) <= 1e-12 * D
    uu = np.asarray(rr["uu"], float)
    mm = 2.0 * np.asarray(rr["lam"], float)
    c_ar = np.asarray(core.arch_lags(M, D), float)
    c1 = np.asarray(core.atom_lags_at(alpha, M, uu, mm)[0], float)
    c0 = np.asarray(cont_lags(alpha, M, [0.0], [2.0 * alpha],
                              [1.0]), float)
    L = 2 * M - 2
    F = L // 2 + 1
    d1 = grid_density(c_ar + c1)[:F]
    d0 = grid_density(c_ar + c0)[:F]
    d0at = grid_density(c0)[:F]
    r = d1 - d0
    ff = np.arange(F)
    x = np.cos(2.0 * math.pi * ff / L)
    a = 2.0 * h * h * (1.0 - x)
    mult = np.where((ff == 0) | (ff == L // 2), 1.0, 2.0)
    qt = mult * 4.0 * np.sin(math.pi * ff / L) ** 2 / (2.0 * L)
    al_f = ff[(ff >= 1) & (d1 < 0.0)
              & (a <= h ** (2.0 * THETA_STAR))]
    al_f = al_f[np.argsort(a[al_f], kind="stable")]
    return dict(kz=kz, alpha=alpha, M=M, h=h, L=L, F=F, D=D,
                c_ar=c_ar, c0=c0, c1=c1, uu=uu, mm=mm,
                x=x, a=a, qt=qt, d0=d0, d1=d1, d0at=d0at, r=r,
                al_f=al_f, y_al=x[al_f], a_al=a[al_f],
                X=math.exp(2.0 * alpha))


def eval_state(R, dv, resid, al_f, need_J=True, qf=False):
    """Chain of the positive part of dv; per alias the Christoffel
    lambda, target mass nu, gap F = lambda - nu, and (optionally)
    the envelope derivative J built with residual `resid` and the
    masks of dv (verbatim round-51)."""
    pos = (dv > 0.0) & (R["qt"] > 0.0)
    xs = R["x"][pos]
    ws = (R["qt"] * dv)[pos]
    h = R["h"]
    al, be, m0, steps = lanczos_chain(xs, ws, h + 1)
    if steps < h + 1:
        return None
    Phi = eval_chain(al, be, m0, R["x"][al_f], h)   # n_al x h
    K = np.sum(Phi ** 2, axis=1)
    lam = 1.0 / K
    nu = R["qt"][al_f] * np.maximum(-dv[al_f], 0.0)
    out = dict(lam=lam, nu=nu, G=lam - nu, chain=(al, be, m0),
               Phi=Phi, Kdiag=K, pos=pos)
    if need_J or qf:
        Ppos = eval_chain(al, be, m0, xs, h)
        U = Ppos @ Phi.T                            # n_pos x n_al
        if need_J:
            S = ((R["qt"] * resid)[pos] @ (U * U)) / K ** 2
            out["J"] = S + (R["qt"][al_f] * resid[al_f]
                            * (dv[al_f] < 0.0))
        if qf:
            out["qf_dev"] = float(np.max(np.abs(
                (ws @ (U * U)) / K - 1.0)))
    return out


# --------------------------------------- the prime-side regrouping (P1 alg.)
def kernel_block(R, e, dm):
    """W_{f,m}, chat, kernel at the atoms, prime sum, smooth
    subtraction and the two wards, from the state e (chain of the
    density with mask dm); verbatim paircorr_contract P1,
    generalized to either endpoint via dm (round-51)."""
    al, be, m0 = e["chain"]
    h, F, M, L = R["h"], R["F"], R["M"], R["L"]
    Pall = eval_chain(al, be, m0, R["x"], h)        # F x h
    U0 = Pall @ e["Phi"].T                          # F x n_al
    P2 = (U0 * U0) / e["Kdiag"] ** 2                # p_m(x_f)^2
    af = R["al_f"]
    W = (R["qt"] * (dm > 0.0))[:, None] * P2        # F x n_al
    W[af, np.arange(len(af))] += (R["qt"][af] * (dm[af] < 0.0))
    A_grid = W.T @ R["r"]
    ii = np.arange(M)
    cosIF = np.cos((2.0 * math.pi / L)
                   * np.outer(ii, np.arange(F).astype(float)))
    w_i = np.where((ii == 0) | (ii == M - 1), 1.0, 2.0)
    chat = (cosIF @ W) * w_i[:, None]               # M x n_al
    del cosIF
    uu, D = R["uu"], R["D"]
    i0 = np.floor(uu / D).astype(int)
    fr = uu / D - i0
    v0 = np.where((i0 >= 0) & (i0 <= M - 1), 1.0 - fr, 0.0)
    v1 = np.where((i0 + 1 >= 0) & (i0 + 1 <= M - 1), fr, 0.0)
    Kat = -0.5 * (v0[:, None] * chat[np.clip(i0, 0, M - 1)]
                  + v1[:, None] * chat[np.clip(i0 + 1, 0, M - 1)])
    mir = uu < D
    if np.any(mir):
        Kat[mir] += -0.5 * ((1.0 - uu[mir] / D)[:, None]
                            * chat[0][None, :])
    S1 = R["mm"] @ Kat
    K0a = W.T @ R["d0at"]
    K0b = R["c0"] @ chat
    A_prime = S1 - K0a
    Sabs = np.abs(R["mm"]) @ np.abs(Kat) + np.abs(K0a)
    ward1 = float(np.max(np.abs(A_prime - A_grid)
                         / np.maximum(np.maximum(np.abs(A_grid),
                                                 Sabs), 1e-300)))
    ward2 = float(np.max(np.abs(K0b - K0a)
                         / np.maximum(np.abs(R["c0"])
                                      @ np.abs(chat), 1e-300)))
    return dict(W=W, chat=chat, A_grid=A_grid, A_prime=A_prime,
                Sabs=Sabs, ward1=ward1, ward2=ward2)


# ----------------------------------------------- Z4 profiles (paircorr P1)
def min_window(mass, frac):
    """Smallest contiguous index window with >= frac of sum(mass)."""
    tot = float(np.sum(mass))
    target = frac * tot
    jl, csum, best = 0, 0.0, None
    for jr in range(len(mass)):
        csum += mass[jr]
        while csum - mass[jl] >= target:
            csum -= mass[jl]
            jl += 1
        if csum >= target and (best is None
                               or jr - jl < best[1] - best[0]):
            best = (jl, jr)
    return best


def profile(R, kb, m_idx):
    """n90 / width90 / tau_mean of K^(0)_{h,m} at one alias column
    (verbatim paircorr_contract profile, reduced to the three
    numbers Z4 needs)."""
    M, D, F, L = R["M"], R["D"], R["F"], R["L"]
    Ki = -0.5 * kb["chat"][1:, m_idx]        # K(iD), i = 1..M-1
    jl, jr = min_window(np.abs(Ki), FRAC_MASS)
    u_frac = ((jr - jl + 1) * D) / (2.0 * R["alpha"])
    aw = np.abs(kb["W"][1:, m_idx])
    o = np.argsort(-aw)
    cs = np.cumsum(aw[o])
    n90 = int(np.searchsorted(cs, FRAC_MASS * cs[-1]) + 1)
    tauv = 2.0 * math.pi * np.arange(1, F) / (L * D)
    tau_mean = float((aw @ tauv) / max(float(np.sum(aw)), 1e-300))
    return n90, float(u_frac), tau_mean


def loglog_slope(hs, ys):
    """Least-squares slope of log(y) vs log(h); None if unusable."""
    hs = [h for h, y in zip(hs, ys) if y > 0.0]
    yy = [y for y in ys if y > 0.0]
    if len(yy) < 2 or len(yy) < len(ys):
        return None
    return float(np.polyfit(np.log(hs), np.log(yy), 1)[0])


def main():
    section("PRIME.CASE.INNERLINEAR.01 -- the inner-zone linear "
            "route of the diagonal half (EXPLORATION ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s"
          % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
    print("    NO RH claim; no marker moves.")

    print("\nS0 -- firewall + self-tests")
    check("S0.1 AST firewall clean", not ast_scan(BANNED_IDS),
          kill="PIPELINE")

    section("B0 -- rungs (geometry, zone aliases, deep half)")
    RG = {}
    for kz in RUNGS:
        R = build_rung(kz)
        RG[kz] = R
        print("    kz %-3d h %4d F %5d: atoms %5d, X %.3e, zone "
              "aliases %3d (a <= h^1.4 = %8.0f)"
              % (kz, R["h"], R["F"], len(R["uu"]), R["X"],
                 len(R["al_f"]), R["h"] ** 1.4), flush=True)
    order = sorted(RUNGS, key=lambda kz: (RG[kz]["h"], kz))
    deep = tuple(order[len(order) // 2:])
    print("    deep half (4 highest-h rungs): kz %s"
          % ", ".join(str(kz) for kz in deep))
    ok_al = all(len(RG[kz]["al_f"]) > 0 for kz in RUNGS)
    check("B0.1 zone alias sets nonempty on every rung", ok_al,
          kill="PIPELINE")
    if not ok_al:
        return finish({})

    # S0.2 endpoint reconstruction vs verbatim folded route (kz 9)
    R9 = RG[9]
    dev_end = 0.0
    for tv in (0.0, 1.0):
        dv = R9["d0"] if tv == 0.0 else R9["d1"]
        d_full = np.concatenate([dv, dv[-2:0:-1]])
        xs, ws, _uf = folded_measure(d_full, R9["L"], +1.0)
        ys, vs, uf_n = folded_measure(d_full, R9["L"], -1.0)
        al, be, m0, steps = lanczos_chain(xs, ws, R9["h"] + 1)
        if steps < R9["h"] + 1:
            check("S0.2 endpoint chain (verbatim route)", False,
                  kill="PIPELINE")
            return finish({})
        Pn = eval_chain(al, be, m0, R9["y_al"], R9["h"])
        lam_ref = 1.0 / np.sum(Pn ** 2, axis=1)
        pos_map = {int(f): float(v) for f, v in zip(uf_n, vs)}
        nu_ref = np.array([pos_map.get(int(f), 0.0)
                           for f in R9["al_f"]])
        e = eval_state(R9, dv, R9["r"], R9["al_f"], need_J=False)
        if e is None:
            check("S0.2 endpoint chain (qt route)", False,
                  kill="PIPELINE")
            return finish({})
        dev_end = max(dev_end, float(np.max(
            np.abs(e["lam"] / lam_ref - 1.0))))
        dev_end = max(dev_end, float(np.max(
            np.abs(e["nu"] - nu_ref)
            / np.maximum(np.abs(nu_ref), 1e-300))))
    check("S0.2 endpoint reconstruction == verbatim folded route "
          "(kz 9, t = 0 and 1)", dev_end <= TOL_SELF_END,
          "rel sup dev %.2e" % dev_end, kill="PIPELINE")

    section("E -- endpoints, derivatives, margins + wards "
            "(verbatim round-51 quantities)")
    RES = {}
    ok_e = True
    qf_worst = 0.0
    wA_max = wB_max = 0.0
    for kz in order:
        R = RG[kz]
        t_a = time.time()
        e0 = eval_state(R, R["d0"], R["r"], R["al_f"], need_J=True,
                        qf=True)
        e1 = eval_state(R, R["d1"], R["r"], R["al_f"], need_J=True,
                        qf=True)
        if e0 is None or e1 is None:
            ok_e = False
            print("    kz %-3d: CHAIN SHORT at an endpoint" % kz)
            break
        qf_worst = max(qf_worst, e0["qf_dev"], e1["qf_dev"])
        kb0 = kernel_block(R, e0, R["d0"])
        kb1 = kernel_block(R, e1, R["d1"])
        wa0 = float(np.max(np.abs(e0["J"] - kb0["A_prime"])
                           / np.maximum(np.maximum(
                               np.abs(kb0["A_grid"]),
                               kb0["Sabs"]), 1e-300)))
        wa1 = float(np.max(np.abs(e1["J"] - kb1["A_prime"])
                           / np.maximum(np.maximum(
                               np.abs(kb1["A_grid"]),
                               kb1["Sabs"]), 1e-300)))
        wA_max = max(wA_max, wa0, wa1)
        wB_max = max(wB_max, kb0["ward2"], kb1["ward2"])
        deficit = -e0["G"]
        RES[kz] = dict(e0=e0, e1=e1, kb0=kb0, kb1=kb1,
                       deficit=deficit,
                       margin1=e1["J"] - deficit,
                       margin0=e0["J"] - deficit,
                       marginF=e1["G"])
        print("    kz %-3d h %4d (n_al %2d): F'(0) med %+.3e | "
              "F'(1) med %+.3e | deficit med %+.3e | W-A %.1e/"
              "%.1e W-B %.1e/%.1e  [%.1f s]"
              % (kz, R["h"], len(R["al_f"]),
                 float(np.median(e0["J"])),
                 float(np.median(e1["J"])),
                 float(np.median(deficit)), wa0, wa1,
                 kb0["ward2"], kb1["ward2"],
                 time.time() - t_a), flush=True)
    check("E0 endpoint chains complete on all rungs", ok_e,
          kill="PIPELINE")
    check("S0.3 quadratic-form self-test (sum w p*^2 == lambda, "
          "both endpoints, all rungs)", ok_e
          and qf_worst <= TOL_QF, "worst rel dev %.2e" % qf_worst,
          kill="PIPELINE")
    if not ok_e:
        return finish({})
    check("E.W-A prime-side regrouping == envelope F' at both "
          "endpoints (max rel %.2e <= %.0e)"
          % (wA_max, TOL_WARD_PRIME), wA_max <= TOL_WARD_PRIME,
          kill="WARD")
    check("E.W-B smooth subtraction route a == route b (max rel "
          "%.2e <= %.0e)" % (wB_max, TOL_WARD_K0),
          wB_max <= TOL_WARD_K0, kill="WARD")

    labels = {}

    # ------------------------------------------------------------ Z1
    section("Z1 -- THE INNER EXPONENT: census F'(1) >= deficit on "
            "{a <= h^(2 theta_in)}, theta_in in the frozen grid")
    elig = {}
    for th in INNER_GRID:
        rows = []
        deep_ok = True
        deep_h, deep_min, deep_mono = [], [], []
        for kz in order:
            R, res = RG[kz], RES[kz]
            sel = R["a_al"] <= R["h"] ** (2.0 * th)
            n_in = int(np.sum(sel))
            mg = res["margin1"][sel]
            npass = int(np.sum(mg >= 0.0)) if n_in else 0
            mn = float(np.min(mg)) if n_in else float("nan")
            rows.append((kz, R["h"], n_in, npass, mn))
            if kz in deep:
                if n_in == 0 or npass < n_in:
                    deep_ok = False
                deep_h.append(R["h"])
                deep_min.append(mn if n_in else float("nan"))
                deep_mono.append(bool(np.all(np.diff(mg) <= 0.0))
                                 if n_in >= 2 else None)
        trend = None
        if all(np.isfinite(v) and v > 0.0 for v in deep_min):
            trend = float(np.polyfit(np.log(deep_h),
                                     np.log(deep_min), 1)[0])
        ok = deep_ok and trend is not None and trend > 0.0
        elig[th] = ok
        print("\n    theta_in = %.3f  (inner cut a <= h^%.3f):"
              % (th, 2.0 * th))
        for kz, h, n_in, npass, mn in rows:
            tagd = " deep" if kz in deep else ""
            print("      kz %-3d h %4d: inner %2d cells, pass "
                  "%2d/%-2d, min margin %s%s"
                  % (kz, h, n_in, npass, n_in,
                     "%+.3e" % mn if np.isfinite(mn) else "  n/a ",
                     tagd))
        print("      deep half: 100%% pass %s | margin trend "
              "slope %s | ELIGIBLE %s"
              % ("YES" if deep_ok else "no",
                 "%+.3f" % trend if trend is not None else "n/a",
                 "YES" if ok else "no"), flush=True)
        if deep_ok:                       # v2 disclosed diagnostics
            tnorm = None
            if all(np.isfinite(v) and v > 0.0 for v in deep_min):
                tnorm = float(np.polyfit(
                    np.log(deep_h),
                    np.log(np.array(deep_h)
                           * np.array(deep_min)), 1)[0])
            print("      v2 diagnostics (measurement only, rule "
                  "untouched): normalized slope of log(h x min "
                  "margin) %s | within-rung margin1 monotone "
                  "along a (deep): %s"
                  % ("%+.3f" % tnorm if tnorm is not None
                     else "n/a",
                     " ".join(("yes" if m else "no")
                              if m is not None else "n/a"
                              for m in deep_mono)), flush=True)
    cand = [th for th in INNER_GRID if elig[th]]
    theta_in = max(cand) if cand else None
    if theta_in is not None:
        z1_label = "INNER-ZONE(theta_in*=%.3f)" % theta_in
        print("\n    FROZEN: theta_in* = %.3f -- the largest grid "
              "exponent with a 100%% deep-half linear census and a "
              "positive margin trend." % theta_in)
    else:
        z1_label = "INNER-EMPTY"
        print("\n    INNER-EMPTY: no grid theta_in is eligible -- "
              "the linear route covers no stable inner zone on the "
              "deep half (honest).")
    labels["TYPE"] = z1_label
    check("Z1.1 typed: %s (measurement)" % z1_label, True)
    th_use = theta_in if theta_in is not None else THETA_FALLBACK
    if theta_in is None:
        print("    Z2/Z3/Z4 run at the frozen fallback theta_in = "
              "%.3f, purely for the record (disclosed)."
              % THETA_FALLBACK)

    # ------------------------------------------------------------ Z2
    section("Z2 -- THE MIDDLE-BAND ACCOUNTING: cells with "
            "h^(2 x %.3f) < a <= h^1.4 under the FULL difference"
            % th_use)
    n_band_tot = 0
    hs_frac, fr_frac = [], []
    band_bad = 0
    for kz in order:
        R, res = RG[kz], RES[kz]
        band = R["a_al"] > R["h"] ** (2.0 * th_use)
        res["band"] = band
        n_zone = len(R["al_f"])
        n_band = int(np.sum(band))
        n_band_tot += n_band
        frac = n_band / n_zone
        hs_frac.append(R["h"])
        fr_frac.append(frac)
        if n_band == 0:
            print("    kz %-3d h %4d: band EMPTY (zone %d cells "
                  "all inner)" % (kz, R["h"], n_zone))
            continue
        mgF = res["marginF"][band]
        mg1 = res["margin1"][band]
        npass = int(np.sum(mgF >= 0.0))
        band_bad += n_band - npass
        print("    kz %-3d h %4d: band %2d/%2d cells (frac %.2f) | "
              "FULL margin: pass %2d/%-2d min %+.3e med %+.3e | "
              "linear margin min %+.3e"
              % (kz, R["h"], n_band, n_zone, frac, npass, n_band,
                 float(np.min(mgF)), float(np.median(mgF)),
                 float(np.min(mg1))))
        idx = np.nonzero(band)[0]
        show = list(idx[:SHOW_BAND])
        im = int(idx[np.argmin(mgF)])
        if im not in show:
            show.append(im)
        print("      %-4s %-5s %-9s %-11s %-11s %-11s"
              % ("m", "f", "a_m", "marginF", "margin1", "deficit"))
        for i in show:
            print("      %-4d %-5d %-9.1f %+.3e  %+.3e  %+.3e%s"
                  % (i + 1, int(R["al_f"][i]), float(R["a_al"][i]),
                     float(res["marginF"][i]),
                     float(res["margin1"][i]),
                     float(res["deficit"][i]),
                     "  <- min marginF" if i == im else ""),
                  flush=True)
    n_frac_pos = sum(1 for v in fr_frac if v > 0.0)
    slope = (loglog_slope(hs_frac, fr_frac)
             if n_frac_pos >= MIN_TREND_RUNGS else None)
    if slope is not None:
        band_trend = "SHRINKING" if slope < 0.0 else "NON-SHRINKING"
        print("\n    band fraction h-trend: log-log slope %+.3f "
              "-> %s with depth" % (slope, band_trend))
    else:
        band_trend = "n/a"
        print("\n    band fraction h-trend: n/a (%d rungs with a "
              "nonempty band, or empty-band rungs break the "
              "log fit -- disclosed)" % n_frac_pos)
    labels["BAND"] = "%d cells, %s" % (n_band_tot, band_trend)
    print("    band total: %d cells over the 8 rungs; FULL-margin "
          "failures in the band: %d (the nonlinear truth ledger)"
          % (n_band_tot, band_bad))
    check("Z2.1 band accounting recorded (measurement)", True)

    # ------------------------------------------------------------ Z3
    section("Z3 -- THE STABILITY LEMMA SHADOW: ||K^(1) - K^(0)|| / "
            "||K^(0)|| per inner-zone alias (deep half)")
    stab_max = 0.0
    gap_max_deep = 0.0
    for kz in deep:
        R, res = RG[kz], RES[kz]
        inner = ~res["band"]
        idx = np.nonzero(inner)[0]
        relv, corrv = [], []
        for i in idx:
            K0i = -0.5 * res["kb0"]["chat"][1:, i]
            K1i = -0.5 * res["kb1"]["chat"][1:, i]
            den = max(float(np.linalg.norm(K0i)), 1e-300)
            relv.append(float(np.linalg.norm(K1i - K0i)) / den)
            cd = max(float(np.linalg.norm(K0i)
                           * np.linalg.norm(K1i)), 1e-300)
            corrv.append(float((K0i @ K1i) / cd))
        relv = np.array(relv)
        corrv = np.array(corrv)
        stab_max = max(stab_max, float(np.max(relv)))
        gap = res["e0"]["J"][idx] - res["e1"]["J"][idx]
        gap_max_deep = max(gap_max_deep,
                           float(np.max(np.abs(gap))))
        n_pass0 = int(np.sum(res["margin0"][idx] >= 0.0))
        print("    kz %-3d h %4d: inner %d aliases | relK max %.3f "
              "med %.3f | corr min %+.4f | K^(0) census F'(0) >= "
              "deficit: %d/%d"
              % (kz, R["h"], len(idx), float(np.max(relv)),
                 float(np.median(relv)), float(np.min(corrv)),
                 n_pass0, len(idx)))
        show = list(range(min(SHOW_STAB, len(idx))))
        ix = int(np.argmax(relv))
        if ix not in show:
            show.append(ix)
        print("      %-4s %-5s %-9s %-7s %-8s %-11s %-11s"
              % ("m", "f", "a_m", "relK", "corr", "F'(0)-F'(1)",
                 "margin1"))
        for j in show:
            i = idx[j]
            print("      %-4d %-5d %-9.1f %-7.3f %+.4f  %+.3e  "
                  "%+.3e%s"
                  % (i + 1, int(R["al_f"][i]), float(R["a_al"][i]),
                     float(relv[j]), float(corrv[j]),
                     float(gap[j]), float(res["margin1"][i]),
                     "  <- max relK" if j == ix else ""),
                  flush=True)
    labels["STABILITY"] = "max inner relK %.3f (deep)" % stab_max
    print("\n    THE LINEAR-ROUTE THEOREM SKELETON (measured "
          "shadow filled in):")
    print("      IF   (i)  p_{1,m} ~ p_{0,m} + mask stability on "
          "the inner zone {a <= h^%.3f} at the measured level "
          "(kernel distance <= %.3f, deep half)," % (2.0 * th_use,
                                                     stab_max))
    print("           (ii) the ONE-SIDED linear bound  sum_n mu_n "
          "K^(0)_{h,m}(log n) - K0 >= deficit_m + stability-error "
          "there (measured transfer gap |F'(0) - F'(1)| <= %.3e "
          "on the deep inner cells)," % gap_max_deep)
    print("      THEN T_h <= 1 on the inner zone of the ladder; "
          "the pair-correlation input is needed only on the BAND "
          "h^%.3f < a <= h^1.4 -- the hard part is now a BAND, "
          "not the zone." % (2.0 * th_use))
    print("      (Circularity caveat verbatim round-51: K^(1) is "
          "truth-built; without (i) the census does not transfer "
          "to the PNT-computable K^(0).)")
    print("\n    THE BAND SIZE, honestly (deep half):")
    for kz in deep:
        R, res = RG[kz], RES[kz]
        band = res["band"]
        nu1 = res["e1"]["nu"]
        dfc = res["deficit"]
        fr_al = float(np.mean(band))
        s_nu = float(np.sum(nu1))
        s_df = float(np.sum(dfc))
        fr_nu = float(np.sum(nu1[band])) / max(s_nu, 1e-300)
        fr_df = float(np.sum(dfc[band])) / max(abs(s_df), 1e-300)
        print("      kz %-3d h %4d: alias fraction %.3f | nu_1-"
              "mass fraction %.3f | deficit fraction %.3f"
              % (kz, R["h"], fr_al, fr_nu, fr_df))
    check("Z3.1 stability profile + skeleton recorded "
          "(measurement)", True)

    # ------------------------------------------------------------ Z4
    section("Z4 -- THE CLASSICAL FORM: n90 / width90 / tau of the "
            "inner K^(0) kernels vs the band (all rungs)")
    softer_votes = []
    for kz in order:
        R, res = RG[kz], RES[kz]
        band = res["band"]
        idx_in = np.nonzero(~band)[0]
        idx_bd = np.nonzero(band)[0]
        prof = {}
        for i in np.concatenate([idx_in, idx_bd]):
            prof[int(i)] = profile(R, res["kb0"], int(i))
        print("    kz %-3d h %4d (2 alpha = %.2f): inner %d, band "
              "%d aliases" % (kz, R["h"], 2.0 * R["alpha"],
                              len(idx_in), len(idx_bd)))
        print("      %-6s %-4s %-5s %-9s %-5s %-7s %-6s"
              % ("set", "m", "f", "a_m", "n90", "u_frac", "tau"))
        for tag, ids, nshow in (("inner", idx_in, SHOW_IN),
                                ("band", idx_bd, SHOW_BAND)):
            for i in ids[:nshow]:
                n90, uf, tm = prof[int(i)]
                print("      %-6s %-4d %-5d %-9.1f %-5d %-7.3f "
                      "%-6.2f" % (tag, i + 1, int(R["al_f"][i]),
                                  float(R["a_al"][i]), n90, uf,
                                  tm))
            if len(ids) > nshow:
                print("      %-6s ... +%d more rows"
                      % (tag, len(ids) - nshow))
        if len(idx_in) and len(idx_bd):
            med = {}
            for tag, ids in (("in", idx_in), ("bd", idx_bd)):
                med[tag] = tuple(float(np.median(
                    [prof[int(i)][k] for i in ids]))
                    for k in range(3))
            softer = (med["in"][1] <= med["bd"][1]
                      and med["in"][2] <= med["bd"][2])
            softer_votes.append(softer)
            print("      medians: inner n90 %.0f u_frac %.3f tau "
                  "%.2f | band n90 %.0f u_frac %.3f tau %.2f -> "
                  "inner %s"
                  % (med["in"][0], med["in"][1], med["in"][2],
                     med["bd"][0], med["bd"][1], med["bd"][2],
                     "SOFTER" if softer else "not softer"),
                  flush=True)
        else:
            print("      medians: n/a (inner or band empty on "
                  "this rung)", flush=True)
    if len(softer_votes) >= 2:
        n_soft = sum(softer_votes)
        # strict majority per the frozen rule
        cls = ("INNER-SOFTER" if n_soft * 2 > len(softer_votes)
               else "INNER-NOT-SOFTER")
        print("\n    reading: inner kernels softer on %d/%d "
              "comparable rungs -> %s (a %s classical hypothesis "
              "on the inner zone than on the band)"
              % (n_soft, len(softer_votes), cls,
                 "potentially WEAKER" if cls == "INNER-SOFTER"
                 else "NOT visibly weaker"))
    else:
        cls = "n/a"
        print("\n    reading: fewer than 2 comparable rungs -> "
              "CLASSICAL=n/a (disclosed)")
    labels["CLASSICAL"] = cls
    check("Z4.1 classical-form profiles recorded: %s "
          "(measurement)" % cls, True)

    # ------------------------------------------------------------ C
    section("C -- controls (kz 9, scramble seed %d, theta_ctrl = "
            "%.3f frozen)" % (SCRAMBLE_SEED, THETA_CTRL))
    rng = np.random.default_rng(SCRAMBLE_SEED)
    us = np.sort(rng.uniform(0.0, 2.0 * R9["alpha"],
                             size=len(R9["uu"])))
    c_s = np.asarray(core.atom_lags_at(R9["alpha"], R9["M"], us,
                                       R9["mm"])[0], float)
    d_s = grid_density(R9["c_ar"] + c_s)[:R9["F"]]
    r_s = d_s - R9["d0"]
    ff9 = np.arange(R9["F"])
    neg_s = ff9[(ff9 >= 1) & (d_s < 0.0)]
    neg_s = neg_s[np.argsort(R9["a"][neg_s], kind="stable")]
    al_inner = neg_s[R9["a"][neg_s]
                     <= R9["h"] ** (2.0 * THETA_CTRL)]
    fell_back = len(al_inner) == 0
    al_use = al_inner if not fell_back else neg_s[:CTRL_FALLBACK_AL]
    es = eval_state(R9, d_s, r_s, al_use, need_J=True)
    e0s = eval_state(R9, R9["d0"], r_s, al_use, need_J=False)
    if es is None or e0s is None:
        check("C0 scramble chains complete", False,
              kill="PIPELINE")
        return finish(labels)
    mg_s = es["J"] - (-e0s["G"])
    worst = float(np.min(mg_s))
    fires = worst < 0.0
    sel9 = RG[9]["a_al"] <= R9["h"] ** (2.0 * THETA_CTRL)
    real9 = (float(np.min(RES[9]["margin1"][sel9]))
             if np.any(sel9) else float("nan"))
    print("    scramble inner aliases: %d%s | min (F'_scr(1) - "
          "deficit_scr) = %+.3e (real kz 9 inner min margin1 "
          "%+.3e) -> %s"
          % (len(al_use),
             " (inner empty -> frozen fallback: %d a-closest neg "
             "nodes)" % CTRL_FALLBACK_AL if fell_back else
             " (inner zone)",
             worst, real9, "FIRES" if fires else "SILENT"),
          flush=True)
    check("C1 value control fires (scramble breaks the inner "
          "linear census)", fires, kill="CONTROL")

    return finish(labels)


def finish(labels):
    section("V -- FROZEN VERDICT")
    n_pass = sum(1 for _n, okk in CHECKS if okk)
    n_tot = len(CHECKS)
    if "PIPELINE" in KILLS:
        VERDICT = "PIPELINE-BROKEN"
    elif "WARD" in KILLS:
        VERDICT = "WARD-BROKEN"
    elif "CONTROL" in KILLS:
        VERDICT = "CONTROL-DEAD"
    else:
        VERDICT = "INNERLINEAR-MEASURED"
    sub = ["%s=%s" % (k, labels[k]) for k in
           ("TYPE", "BAND", "STABILITY", "CLASSICAL")
           if k in labels]
    print("\n  VERDICT: %s%s"
          % (VERDICT, (" (%s)" % "; ".join(sub)) if sub else ""))
    if VERDICT == "INNERLINEAR-MEASURED" and "TYPE" in labels:
        if labels["TYPE"].startswith("INNER-ZONE"):
            print("  PLAIN ANSWER: YES on the finite shadow -- an "
                  "inner zone exists on which the LINEAR endpoint "
                  "route covers the deep half with growing "
                  "margins; the genuinely hard (pair-correlation) "
                  "part contracts to the printed middle BAND, "
                  "modulo the p1 ~ p0 stability lemma whose "
                  "measured shadow Z3 prints.")
        else:
            print("  PLAIN ANSWER: NO -- no grid inner exponent "
                  "gives a stable 100% deep-half linear census; "
                  "the pair-correlation input stands on the whole "
                  "zone.")
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed"
          % (time.time() - T0, n_tot, n_tot - n_pass))
    return 0 if n_pass == n_tot else 1


if __name__ == "__main__":
    raise SystemExit(main())
