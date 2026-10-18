#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""endpoint_bracket_probe -- PRIME.CASE.ENDPOINT.01
(EXPLORATION ONLY, experiments/; round 51, reviewer priority 6: the
concavity bracket of the diagonal-half homotopy -- does the ONE-SIDED
ENDPOINT DERIVATIVE F'(1) already clear the PNT-reference deficit,
collapsing the pair-correlation contract to a LINEAR signed-Lambda
functional evaluated AT THE TRUTH?  2026-08-09.)

CONTEXT (machinery verbatim from signed_homotopy_probe /
paircorr_contract_probe): with F_m(t) = lambda_{t,m} - nu_{t,m}
along d_t = d_PNT + t (d_truth - d_PNT), the exact envelope identity
gives F'_m(t) = J_{h,m}(t) = sum_f qt_f r_f 1{d_t(f) > 0}
p_{t,m}(x_f)^2 + qt_m r_m 1{d_t(m) < 0} a.e. t; within a fixed mask
chamber lambda_t is CONCAVE in t (a minimum of linear functionals of
mu_t) and the nu side is linear, so F is concave per chamber and
J decreases within each chamber; at a mask crossing J JUMPS (an
entering node has r > 0, a leaving node removes an r < 0 term, an
alias-side nu switch flips the linear term), so the GLOBAL bracket
    F'(1^-)  <=  F(1) - F(0)  <=  F'(0^+)
holds exactly on crossing-free rungs and only up to the (measured)
crossing corrections otherwise.  paircorr_contract_probe froze the
contract: the gain must beat the PNT-reference deficit,
F(1) - F(0) >= deficit_m := (nu_0 - lambda_0)_m, and regrouped the
t = 0 derivative F'(0) = J^(1)_{h,m} into the explicit one-sided
prime sum sum_n mu_n K^(0)_{h,m}(log n) - K0.  THE REVIEWER'S POINT
(this probe): IF F'(1) >= deficit_m already, then by the concavity
bracket F(1) - F(0) >= F'(1) >= deficit -- a ONE-SIDED LOWER BOUND
on the ENDPOINT derivative, a LINEAR signed-Lambda functional
evaluated AT THE TRUTH, suffices, which is much weaker than the
pair-correlation input.  If only F'(0) > deficit but F'(1) <
deficit, the genuine pair-correlation input stands.

THE CIRCULARITY NOTE (frozen up front, honest): F'(1) is linear in
the von Mangoldt masses ONLY AT FIXED KERNEL -- the truth-side
kernel K^(1)_{h,m} carries the truth mask 1{d_1(f) > 0} and the
truth extremizer p_{1,m}, both functionals of the comb itself.  A
theorem from a positive census here would additionally need either
(a) a STABILITY LEMMA p_{1,m} ~ p_{0,m} (and mask stability)
transferring the bound to the PNT-computable K^(0) -- E3 measures
exactly that kernel distance -- or (b) a self-consistent bound: the
one-sided inequality holds for every admissible density in a
neighbourhood class containing d_1.  Stated, not assumed.

FROZEN PROTOCOL (2026-08-09; constants frozen before the first
measurement run; budget < 20 min):

 RUNGS: heavy kz {9, 12, 13, 26, 40} + the deepest 3 with complete
   atom tables kz {88, 90, 116} (verbatim eligibility and selection
   from christoffel_pnt_gamma_probe / signed_homotopy_probe;
   X <= 4e5).
 ALIASES: all port aliases in the frozen critical zone -- truth neg
   nodes (d_1(f) < 0, f >= 1) with a_{h,f} = 2 h^2 (1 - x_f) <=
   h^{2 theta*}, theta* = 0.700, ranked by a ascending (verbatim).

 E1 THE THREE NUMBERS (every rung, every zone alias):
   F'(0) = J at t = 0 (PNT-side extremal polynomial p_{0,m} + PNT
   masks), F'(1) = J at t = 1 (TRUTH-side extremal polynomial
   p_{1,m} + truth masks -- exact, same envelope formula), and the
   exact endpoint difference Delta_m = F(1) - F(0).  WARDS (kill
   WARD-BROKEN on failure):
     (W-A) prime-side regrouping == grid form at BOTH endpoints:
           F'(0) vs paircorr_contract's J^(1) = S1 - K0 built from
           W^(0), and F'(1) vs the same regrouping built from the
           truth-side W^(1) (masks d_1, weights p_{1,m}^2); rel
           <= 1e-10 per alias against max(|W.r|, sum_n mu_n |K| +
           |K0|) (verbatim W1 denominator);
     (W-B) smooth-subtraction route a (W.d0at) == route b (c0.chat)
           at both endpoints, rel <= 1e-12 (verbatim W2);
     (W-C) endpoint FD ward: second-order one-sided Richardson
           differences inside the first/last crossing-free chamber,
           F'(0) ~ (-3F(0) + 4F(e) - F(2e))/(2e) and F'(1) ~
           (3F(1) - 4F(1-e) + F(1-2e))/(2e), chamber-safe step
           e = min(1e-4, t_first/4, (1 - t_last)/4) per rung (if
           e < 1e-6 the ward is SKIPPED and disclosed); PASS per
           alias iff |FD - F'| <= max(1e-3 |F'|, 1e-9 lambda_end /
           e) -- the relative bar with the additive FD noise
           allowance 1e-9 lambda / e (the lambda evaluation noise
           floor at h ~ 1400, the round-44 v2 lesson; the additive
           form is the v2 amendment below).
   THE BRACKET DEFECT (MEASUREMENT, never a kill -- crossings can
   honestly break the global bracket): per alias the relative
   defects max(0, Delta - F'(0))/s and max(0, F'(1) - Delta)/s,
   s = max(|F'(0)|, |F'(1)|, |Delta|); per rung the max defect, the
   count of aliases with defect > 1e-9, the mask-crossing count in
   (0,1) and the count of alias-side nu crossings (d_0(m) > 0).
   BRACKET-CLEAN flag iff max rel defect <= 1e-9 over all cells.

 E2 THE DECISIVE CENSUS (the deliverable): per (rung, alias) cell:
   PASS iff F'(1) >= deficit_m = (nu_0 - lambda_0)_m = -F_m(0).
   Margin ladder printed per rung (margin = F'(1) - deficit; first
   6 aliases + the argmin row; min/median/pass count).  TYPED:
     ENDPOINT-SUFFICES      iff PASS on ALL critical cells;
     ENDPOINT-PARTIAL       iff PASS on some but not all (failing
                            cells listed);
     ENDPOINT-INSUFFICIENT  iff PASS nowhere (the pair route
                            stands).
   The F'(0) census (F'(0) >= deficit) is printed alongside for the
   reviewer's contrast reading (measurement only).

 E3 THE LINEAR FUNCTIONAL (printed iff E2 passes anywhere; the
   truth-side regrouping itself is always computed for W-A):
   F'(1) = sum_n mu_n K^(1)_{h,m}(log n) - K0^(1) with
   K^(1)_{h,m}(u) = -(1/2) sum_i tent_i(u) w_i sum_f W^(1)_{f,m}
   cos(2 pi i f / L), W^(1)_{f,m} = qt_f 1{d_1(f) > 0}
   p_{1,m}(x_f)^2 + qt_m 1{d_1(m) < 0} delta_{fm} (the same
   regrouping as paircorr_contract P1 with truth-side weights).
   KERNEL COMPARISON per rung at m* = argmin_m F_m(1) and at the
   a-closest alias: cosine corr(K^(0), K^(1)) on the lag grid
   i = 1..M-1, rel L2 distance ||K^(1) - K^(0)|| / ||K^(0)||, both
   peak locations, and the J-value pair.  The circularity statement
   (header) reprinted with the measured kernel distance filled in.

 E4 THE BRACKET LADDER (report): per rung (h ascending) the medians
   over aliases of F'(0), F'(1), Delta, the concavity drop
   gap = F'(0) - F'(1) and gap/|Delta|; the h-trend: log-log slope
   of the median gap vs h (shrinking iff slope < 0).

 C  CONTROLS (kz 9, scramble seed 1, the deployed mirror: positions
   uniform on (0, 2 alpha), same masses): the scramble endpoint
   derivative must go negative -- min over the scramble zone
   aliases (fallback, disclosed if empty: the 8 a-closest scramble
   neg nodes) of F'_scr(1) (residual r_s = d_scr - d_0, truth-side
   formula at d_scr) must be <= 0.  Silent -> CONTROL-DEAD.

 SELF-TESTS (S0, kill PIPELINE on failure): (i) AST firewall clean;
   (ii) endpoint reconstruction (kz 9): the qt-route lambda/nu at
   the zone aliases vs the verbatim folded_measure route, rel
   <= 1e-8, at both t = 0 and t = 1; (iii) quadratic-form self-test
   per rung at both endpoints: sum_j w_j p*^2 == lambda to rel 1e-8
   (verbatim TOL_QF).

KILLS: chain short anywhere needed / self-test failure / zone alias
set empty on a rung -> PIPELINE-BROKEN; W-A / W-B / W-C ward
failure -> WARD-BROKEN; value control silent -> CONTROL-DEAD.
E1 bracket defect, E2 census, E3, E4 are MEASUREMENTS, never kills.

VERDICT (frozen enum): ENDPOINT-MEASURED (+ TYPE=<ENDPOINT-SUFFICES
| ENDPOINT-PARTIAL | ENDPOINT-INSUFFICIENT> + BRACKET=<CLEAN |
CROSSING-CORRECTED max defect>) / PIPELINE-BROKEN / WARD-BROKEN /
CONTROL-DEAD.

SPEC AMENDMENTS (fail-first preserved):
  v1 (2026-08-09): initial freeze.  The alias bookkeeping, chain,
  regrouping algebra and scramble mirror are verbatim round-45/50
  machinery; the census rule (all / some / none) and the
  bracket-defect bar 1e-9 were frozen before any number was
  computed.  The v1 W-C pass rule was rel <= 1e-3 against the
  denominator max(|F'|, 1e-9 lambda / e).
  v2 (2026-08-09, after the first full run; fail-first preserved):
  the first run returned WARD-BROKEN on exactly one cell -- W-C at
  kz 88, t = 1, alias 1 measured rel 1.16e-3 vs the 1e-3 bar, with
  |F'(1)| = 9.2e-11 at that alias; every other ward passed (W-A
  <= 9.8e-15, W-B <= 1.1e-14, all other W-C <= 2.2e-4).  Diagnosis
  (run before amending, disclosed): the eps-scan 1e-4 / 5e-5 /
  2.5e-5 gives abs defect 1.06e-13 / 1.65e-13 / 4.09e-13 -- the
  defect GROWS as e shrinks (abs defect x e ~ 1e-17 constant), the
  signature of the lambda evaluation NOISE floor, not of stencil
  truncation (a Richardson-extrapolated stencil makes it worse,
  2.0e-3, as extrapolation amplifies noise); across all deep
  rungs/endpoints the measured abs defect is 0.02..0.13 of the
  modeled floor 1e-9 lambda / e.  The v1 rule put the floor INSIDE
  a max() denominator, so whenever floor < |F'| < 1000 floor it
  still demanded certifying the FD below its own noise -- exactly
  the failing cell.  v2 makes the allowance ADDITIVE: PASS iff
  |FD - F'| <= max(1e-3 |F'|, 1e-9 lambda / e) per alias (the
  measured worst cell sits at 0.02 of the allowance).  The bar
  1e-3, the step rule, the stencil and every other ward are
  untouched; every E1/E2/E3/E4/C number of the first run is
  unchanged by this amendment (the ward is a pass/fail gate only).

NO RH claim: every number is finite exact linear algebra /
calculus on the deployed v563 window family; a positive census is
a MEASURED finite shadow of a would-be linear reduction, not a
bound, no rate, no uniformity in h, and carries the circularity
caveat verbatim.  No marker moves.

FIREWALL: no zeros, no prime oracles beyond the deployed table
(AST scan: zetazero/nzeros/primerange/isprime/primepi/nextprime/
prevprime banned); v563 READ-ONLY; RNG only in the scramble
control; stdout only.

Sources (read-only): v563_paper2_readouts (window geometry, tent
assembly, arch lags, deployed atom table); signed_homotopy_probe
(envelope identity, eval machinery, crossing bookkeeping --
verbatim); paircorr_contract_probe (kernel regrouping W/chat/K,
wards W1/W2, deficit ledger -- verbatim); christoffel_pnt_gamma_
probe (W2 closed-form PNT lags, folded measures, Lanczos chain);
christoffel_zone_envelope_probe (theta* = 0.700), declared inputs.

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/endpoint_bracket_probe.py
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
DEEP3 = (88, 90, 116)          # frozen (christoffel_pnt_gamma_probe)
RUNGS = tuple(sorted(set(HEAVY) | set(DEEP3)))
THETA_STAR = 0.700             # frozen zone exponent (ZONESPLIT.01)
TOL_WARD_PRIME = 1.0e-10       # W-A: prime-side form == grid form
TOL_WARD_K0 = 1.0e-12          # W-B: K0 route a == route b
TOL_FD_WARD = 1.0e-3           # W-C: endpoint FD relative bar
EPS_FD = 1.0e-4                # W-C: reference FD step
EPS_FD_MIN = 1.0e-6            # W-C: below this, skip + disclose
NOISE_REL = 1.0e-9             # W-C: lambda evaluation noise floor
TOL_SELF_END = 1.0e-8          # S0.2 endpoint reconstruction
TOL_QF = 1.0e-8                # S0.3 quadratic-form self-test
BRACKET_CLEAN = 1.0e-9         # E1: rel defect bar for CLEAN flag
SHOW_ROWS = 6                  # E2: ladder rows shown per rung
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
#  PNT lags: verbatim from signed_homotopy_probe / paircorr_contract_probe)

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
    """Folded d_PNT, d_truth, residual, weights, zone aliases and the
    exact crossing bookkeeping of one rung (verbatim round-45/50)."""
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
    up = (d0 < 0.0) & (d1 > 0.0) & (qt > 0.0)
    dn = (d0 > 0.0) & (d1 < 0.0) & (qt > 0.0)
    ts = np.full(F, np.nan)
    ts[up | dn] = -d0[up | dn] / r[up | dn]
    breaks = np.unique(ts[up | dn])
    return dict(kz=kz, alpha=alpha, M=M, h=h, L=L, F=F, D=D,
                c_ar=c_ar, c0=c0, c1=c1, uu=uu, mm=mm,
                x=x, a=a, qt=qt, d0=d0, d1=d1, d0at=d0at, r=r,
                al_f=al_f, y_al=x[al_f], breaks=breaks,
                X=math.exp(2.0 * alpha))


def eval_state(R, dv, resid, al_f, need_J=True, qf=False):
    """Chain of the positive part of dv; per alias the Christoffel
    lambda, target mass nu, gap F = lambda - nu, and (optionally) the
    envelope derivative J built with residual `resid` and the masks
    of dv (at dv = d_t, resid = r this is F'_m(t) exactly)."""
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
    """W_{f,m} from the state e (chain/extremizer of the density with
    mask dm), chat, kernel at the atoms, prime sum, smooth
    subtraction and the two wards (paircorr_contract P1, verbatim,
    generalized to either endpoint via dm)."""
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
    return dict(chat=chat, A_grid=A_grid, A_prime=A_prime,
                Sabs=Sabs, ward1=ward1, ward2=ward2)


def fd_endpoint(R, res, side):
    """W-C: chamber-safe second-order one-sided Richardson FD of F'
    at t = 0 (side 0) or t = 1 (side 1).  Returns (max ratio
    |FD - F'| / allowance, eps, skipped) with the v2 additive
    allowance max(TOL_FD_WARD |F'|, NOISE_REL lambda / eps); pass
    iff the ratio <= 1."""
    br = R["breaks"]
    t_first = float(br[0]) if len(br) else 1.0
    t_last = float(br[-1]) if len(br) else 0.0
    gap = t_first if side == 0 else (1.0 - t_last)
    eps = min(EPS_FD, gap / 4.0)
    if eps < EPS_FD_MIN:
        return None, eps, True
    if side == 0:
        e1 = eval_state(R, R["d0"] + eps * R["r"], R["r"],
                        R["al_f"], need_J=False)
        e2 = eval_state(R, R["d0"] + 2.0 * eps * R["r"], R["r"],
                        R["al_f"], need_J=False)
        if e1 is None or e2 is None:
            return None, eps, None
        fd = (-3.0 * res["e0"]["G"] + 4.0 * e1["G"]
              - e2["G"]) / (2.0 * eps)
        Jref, lam_end = res["J0"], res["e0"]["lam"]
    else:
        e1 = eval_state(R, R["d1"] - eps * R["r"], R["r"],
                        R["al_f"], need_J=False)
        e2 = eval_state(R, R["d1"] - 2.0 * eps * R["r"], R["r"],
                        R["al_f"], need_J=False)
        if e1 is None or e2 is None:
            return None, eps, None
        fd = (3.0 * res["e1"]["G"] - 4.0 * e1["G"]
              + e2["G"]) / (2.0 * eps)
        Jref, lam_end = res["J1"], res["e1"]["lam"]
    allow = np.maximum(TOL_FD_WARD * np.abs(Jref),
                       NOISE_REL * lam_end / eps)
    return float(np.max(np.abs(fd - Jref) / allow)), eps, False


def main():
    section("PRIME.CASE.ENDPOINT.01 -- the concavity bracket + the "
            "one-sided endpoint derivative census (EXPLORATION "
            "ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s"
          % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
    print("    NO RH claim; no marker moves.")

    print("\nS0 -- firewall + self-tests")
    check("S0.1 AST firewall clean", not ast_scan(BANNED_IDS),
          kill="PIPELINE")

    section("B0 -- rungs (geometry, zone aliases, crossing "
            "bookkeeping)")
    RG = {}
    for kz in RUNGS:
        R = build_rung(kz)
        RG[kz] = R
        br = R["breaks"]
        print("    kz %-3d h %4d F %5d: atoms %5d, X %.3e, zone "
              "aliases %3d (a <= h^1.4 = %8.0f), crossings %4d "
              "in [%.4f, %.4f]"
              % (kz, R["h"], R["F"], len(R["uu"]), R["X"],
                 len(R["al_f"]), R["h"] ** 1.4, len(br),
                 float(br[0]) if len(br) else float("nan"),
                 float(br[-1]) if len(br) else float("nan")),
              flush=True)
    order = sorted(RUNGS, key=lambda kz: RG[kz]["h"])
    ok_al = all(len(RG[kz]["al_f"]) > 0 for kz in RUNGS)
    check("B0.1 zone alias sets nonempty on every rung", ok_al,
          kill="PIPELINE")
    if not ok_al:
        return finish(None, None)

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
            return finish(None, None)
        Pn = eval_chain(al, be, m0, R9["y_al"], R9["h"])
        lam_ref = 1.0 / np.sum(Pn ** 2, axis=1)
        pos_map = {int(f): float(v) for f, v in zip(uf_n, vs)}
        nu_ref = np.array([pos_map.get(int(f), 0.0)
                           for f in R9["al_f"]])
        e = eval_state(R9, dv, R9["r"], R9["al_f"], need_J=False)
        if e is None:
            check("S0.2 endpoint chain (qt route)", False,
                  kill="PIPELINE")
            return finish(None, None)
        dev_end = max(dev_end, float(np.max(
            np.abs(e["lam"] / lam_ref - 1.0))))
        dev_end = max(dev_end, float(np.max(
            np.abs(e["nu"] - nu_ref)
            / np.maximum(np.abs(nu_ref), 1e-300))))
    check("S0.2 endpoint reconstruction == verbatim folded route "
          "(kz 9, t = 0 and 1)", dev_end <= TOL_SELF_END,
          "rel sup dev %.2e" % dev_end, kill="PIPELINE")

    section("E1 -- THE THREE NUMBERS: F'(0), F'(1), Delta = F(1) - "
            "F(0) per (rung, alias) + wards + bracket defect")
    RES = {}
    ok_e = True
    qf_worst = 0.0
    wA_max = wB_max = 0.0
    fdC_worst = 0.0            # max over rungs of (dev / bar), W-C
    fd_skipped = []
    defect_max = 0.0
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
        J0, J1 = e0["J"], e1["J"]
        delta = e1["G"] - e0["G"]
        res = dict(e0=e0, e1=e1, J0=J0, J1=J1, delta=delta,
                   ms=int(np.argmin(e1["G"])))
        RES[kz] = res
        # W-A / W-B: prime-side regrouping at both endpoints
        kb0 = kernel_block(R, e0, R["d0"])
        kb1 = kernel_block(R, e1, R["d1"])
        res["kb0"], res["kb1"] = kb0, kb1
        wa0 = float(np.max(np.abs(J0 - kb0["A_prime"])
                           / np.maximum(np.maximum(
                               np.abs(kb0["A_grid"]),
                               kb0["Sabs"]), 1e-300)))
        wa1 = float(np.max(np.abs(J1 - kb1["A_prime"])
                           / np.maximum(np.maximum(
                               np.abs(kb1["A_grid"]),
                               kb1["Sabs"]), 1e-300)))
        wA_max = max(wA_max, wa0, wa1)
        wB_max = max(wB_max, kb0["ward2"], kb1["ward2"])
        # W-C: endpoint FD wards (chamber-safe, additive allowance)
        fd_txt = ""
        for side in (0, 1):
            dev, eps, skip = fd_endpoint(R, res, side)
            if skip is None:
                check("E1 FD chains complete (kz %d)" % kz, False,
                      kill="PIPELINE")
                return finish(None, None)
            if skip:
                fd_skipped.append((kz, side, eps))
                fd_txt += "  FD t=%d SKIPPED (e %.1e)" % (side, eps)
            else:
                fdC_worst = max(fdC_worst, dev)
                fd_txt += ("  FD t=%d dev/allow %.2e (e %.1e)"
                           % (side, dev, eps))
        # bracket defect (measurement)
        scale = np.maximum(np.maximum(np.abs(J0), np.abs(J1)),
                           np.abs(delta))
        d_hi = np.maximum(delta - J0, 0.0) / np.maximum(scale,
                                                        1e-300)
        d_lo = np.maximum(J1 - delta, 0.0) / np.maximum(scale,
                                                        1e-300)
        dmax = float(max(np.max(d_hi), np.max(d_lo)))
        defect_max = max(defect_max, dmax)
        n_bad = int(np.sum((d_hi > BRACKET_CLEAN)
                           | (d_lo > BRACKET_CLEAN)))
        n_nu_cross = int(np.sum(R["d0"][R["al_f"]] > 0.0))
        res["defect"] = dmax
        ms = res["ms"]
        print("    kz %-3d h %4d (n_al %2d): F'(0) med %+.3e | "
              "F'(1) med %+.3e | Delta med %+.3e | m* %d: "
              "F'(0) %+.3e  F'(1) %+.3e  Delta %+.3e"
              % (kz, R["h"], len(R["al_f"]),
                 float(np.median(J0)), float(np.median(J1)),
                 float(np.median(delta)), ms + 1,
                 float(J0[ms]), float(J1[ms]),
                 float(delta[ms])))
        print("      wards: W-A t0 %.2e t1 %.2e | W-B %.2e/%.2e |"
              "%s" % (wa0, wa1, kb0["ward2"], kb1["ward2"],
                      fd_txt))
        print("      bracket F'(1) <= Delta <= F'(0): max rel "
              "defect %.2e | aliases beyond %.0e: %d/%d | mask "
              "crossings %d, alias nu-crossings %d  [%.1f s]"
              % (dmax, BRACKET_CLEAN, n_bad, len(R["al_f"]),
                 len(R["breaks"]), n_nu_cross,
                 time.time() - t_a), flush=True)
    check("E0 endpoint chains complete on all rungs", ok_e,
          kill="PIPELINE")
    check("S0.3 quadratic-form self-test (sum w p*^2 == lambda, "
          "both endpoints, all rungs)", ok_e
          and qf_worst <= TOL_QF, "worst rel dev %.2e" % qf_worst,
          kill="PIPELINE")
    if not ok_e:
        return finish(None, None)
    check("E1.W-A prime-side regrouping == envelope F' at both "
          "endpoints (max rel %.2e <= %.0e)"
          % (wA_max, TOL_WARD_PRIME), wA_max <= TOL_WARD_PRIME,
          kill="WARD")
    check("E1.W-B smooth subtraction route a == route b (max rel "
          "%.2e <= %.0e)" % (wB_max, TOL_WARD_K0),
          wB_max <= TOL_WARD_K0, kill="WARD")
    check("E1.W-C endpoint FD wards (worst dev/allowance %.2e <= "
          "1; %d skipped-disclosed)" % (fdC_worst,
                                        len(fd_skipped)),
          fdC_worst <= 1.0, kill="WARD")
    bracket_flag = ("CLEAN" if defect_max <= BRACKET_CLEAN
                    else "CROSSING-CORRECTED max %.1e" % defect_max)
    check("E1.1 bracket defect measured: %s (measurement, never a "
          "kill)" % bracket_flag, True)

    section("E2 -- THE DECISIVE CENSUS: F'(1) >= deficit_m = "
            "(nu_0 - lambda_0)_m per critical cell")
    n_pass = n_all = 0
    fails = []
    pass0 = 0
    for kz in order:
        R = RG[kz]
        res = RES[kz]
        deficit = -res["e0"]["G"]
        margin = res["J1"] - deficit
        margin0 = res["J0"] - deficit
        ok_cells = margin >= 0.0
        n_pass += int(np.sum(ok_cells))
        n_all += len(margin)
        pass0 += int(np.sum(margin0 >= 0.0))
        for i in np.nonzero(~ok_cells)[0]:
            fails.append((kz, int(i) + 1, int(R["al_f"][i]),
                          float(margin[i])))
        print("    kz %-3d h %4d (n_al %d): pass %d/%d | margin "
              "F'(1)-deficit min %+.3e med %+.3e | F'(0)-deficit "
              "min %+.3e (contrast)"
              % (kz, R["h"], len(margin), int(np.sum(ok_cells)),
                 len(margin), float(np.min(margin)),
                 float(np.median(margin)), float(np.min(margin0))))
        print("      %-4s %-5s %-9s %-11s %-11s %-11s %-11s"
              % ("m", "f", "a_m", "F'(1)", "deficit", "margin",
                 "F'(0)"))
        show = list(range(min(SHOW_ROWS, len(margin))))
        im = int(np.argmin(margin))
        if im not in show:
            show.append(im)
        for i in show:
            print("      %-4d %-5d %-9.1f %+.3e  %+.3e  %+.3e  "
                  "%+.3e%s"
                  % (i + 1, int(R["al_f"][i]),
                     float(R["a"][R["al_f"][i]]),
                     float(res["J1"][i]), float(deficit[i]),
                     float(margin[i]), float(res["J0"][i]),
                     "  <- min margin" if i == im else ""),
                  flush=True)
    if n_pass == n_all:
        etype = "ENDPOINT-SUFFICES"
    elif n_pass > 0:
        etype = "ENDPOINT-PARTIAL"
    else:
        etype = "ENDPOINT-INSUFFICIENT"
    print("    census: %d/%d cells pass (F'(0) contrast census: "
          "%d/%d) -> %s" % (n_pass, n_all, pass0, n_all, etype))
    if fails and etype == "ENDPOINT-PARTIAL":
        print("    failing cells (kz, m, f, margin): %s"
              % "; ".join("(%d, %d, %d, %+.2e)" % c
                          for c in fails[:20])
              + (" ... +%d more" % (len(fails) - 20)
                 if len(fails) > 20 else ""))
    check("E2.1 decisive census typed: %s (measurement)" % etype,
          True)

    section("E3 -- THE LINEAR FUNCTIONAL: truth-side kernel K^(1) "
            "vs PNT-side K^(0) + the circularity statement")
    if n_pass > 0:
        for kz in order:
            R = RG[kz]
            res = RES[kz]
            ms = res["ms"]
            for tag, mi in (("m*", ms), ("m1", 0)):
                if tag == "m1" and ms == 0:
                    continue
                K0i = -0.5 * res["kb0"]["chat"][1:, mi]
                K1i = -0.5 * res["kb1"]["chat"][1:, mi]
                ug = np.arange(1, R["M"]) * R["D"]
                den = max(float(np.linalg.norm(K0i)
                                * np.linalg.norm(K1i)), 1e-300)
                corr = float((K0i @ K1i) / den)
                rel = float(np.linalg.norm(K1i - K0i)
                            / max(np.linalg.norm(K0i), 1e-300))
                p0 = float(ug[int(np.argmax(np.abs(K0i)))])
                p1 = float(ug[int(np.argmax(np.abs(K1i)))])
                print("    kz %-3d %s (alias %2d, f %4d): "
                      "corr(K0,K1) %+.4f | ||K1-K0||/||K0|| %.3f |"
                      " peaks u %.2f -> %.2f (2a %.2f) | J: "
                      "F'(0) %+.3e -> F'(1) %+.3e"
                      % (kz, tag, mi + 1, int(R["al_f"][mi]),
                         corr, rel, p0, p1, 2.0 * R["alpha"],
                         float(res["J0"][mi]),
                         float(res["J1"][mi])), flush=True)
        print("\n    CIRCULARITY (what a theorem would need): "
              "F'(1) = sum_n mu_n K^(1)(log n) - K0^(1) is linear "
              "in the masses ONLY AT FIXED KERNEL; K^(1) carries "
              "the truth mask and the truth extremizer p_{1,m} -- "
              "both functionals of the comb.  Needed: (a) a "
              "stability lemma p_{1,m} ~ p_{0,m} + mask stability "
              "(the measured kernel distances above gauge it), "
              "transferring the census to the PNT-computable "
              "K^(0); or (b) a self-consistent one-sided bound "
              "over an admissible density class containing d_1.")
    else:
        print("    census empty (no cell passes) -> E3 comparison "
              "suppressed per the frozen spec; the pair route "
              "stands.")
    check("E3.1 linear-functional reading recorded (measurement)",
          True)

    section("E4 -- THE BRACKET LADDER (medians over aliases; h "
            "ascending) + the h-trend of the concavity drop")
    print("    %-5s %-5s %-4s %-11s %-11s %-11s %-11s %-9s"
          % ("kz", "h", "n_al", "F'(0)", "F'(1)", "Delta",
             "gap=F'0-F'1", "gap/|D|"))
    hh, gg = [], []
    for kz in order:
        R = RG[kz]
        res = RES[kz]
        gap = res["J0"] - res["J1"]
        mg = float(np.median(gap))
        md = float(np.median(np.abs(res["delta"])))
        print("    %-5d %-5d %-4d %+.3e  %+.3e  %+.3e  %+.3e  "
              "%7.3f"
              % (kz, R["h"], len(R["al_f"]),
                 float(np.median(res["J0"])),
                 float(np.median(res["J1"])),
                 float(np.median(res["delta"])), mg,
                 mg / max(md, 1e-300)))
        if mg > 0.0:
            hh.append(math.log(R["h"]))
            gg.append(math.log(mg))
    if len(hh) >= 3:
        slope = float(np.polyfit(hh, gg, 1)[0])
        print("    h-trend of the median gap: log-log slope %+.3f "
              "-> the concavity drop is %s with depth"
              % (slope, "SHRINKING" if slope < 0.0 else
                 "NOT shrinking"))
    else:
        slope = float("nan")
        print("    h-trend: fewer than 3 rungs with positive "
              "median gap -- no slope fitted (disclosed).")
    check("E4.1 bracket ladder recorded (measurement)", True)

    section("C -- controls (kz 9, scramble seed %d)"
            % SCRAMBLE_SEED)
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
    al_zone = neg_s[R9["a"][neg_s]
                    <= R9["h"] ** (2.0 * THETA_STAR)]
    fell_back = len(al_zone) == 0
    al_use = al_zone if not fell_back else neg_s[:CTRL_FALLBACK_AL]
    es = eval_state(R9, d_s, r_s, al_use, need_J=True)
    if es is None:
        check("C0 scramble chain completes", False,
              kill="PIPELINE")
        return finish(etype, bracket_flag)
    j1s = float(np.min(es["J"]))
    fires = j1s <= 0.0
    print("    scramble aliases: %d%s | min F'_scr(1) = %+.3e "
          "(real kz 9 min F'(1) = %+.3e) -> %s"
          % (len(al_use),
             " (zone empty -> frozen fallback: %d a-closest neg "
             "nodes)" % CTRL_FALLBACK_AL if fell_back else
             " (zone aliases)",
             j1s, float(np.min(RES[9]["J1"])),
             "FIRES" if fires else "SILENT"), flush=True)
    check("C1 value control fires (scramble drives the endpoint "
          "derivative negative)", fires, kill="CONTROL")

    return finish(etype, bracket_flag)


def finish(etype, bracket_flag):
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
        VERDICT = "ENDPOINT-MEASURED"
    sub = []
    if etype:
        sub.append("TYPE=%s" % etype)
    if bracket_flag:
        sub.append("BRACKET=%s" % bracket_flag)
    print("\n  VERDICT: %s%s"
          % (VERDICT, (" (%s)" % "; ".join(sub)) if sub else ""))
    if VERDICT == "ENDPOINT-MEASURED" and etype:
        if etype == "ENDPOINT-SUFFICES":
            print("  PLAIN ANSWER: YES on the finite shadow -- the "
                  "one-sided endpoint derivative F'(1) clears the "
                  "deficit on EVERY critical cell, so the contract "
                  "collapses to a LINEAR signed-Lambda functional "
                  "at the truth, modulo the measured bracket/"
                  "crossing corrections and the circularity caveat "
                  "(E3).")
        elif etype == "ENDPOINT-PARTIAL":
            print("  PLAIN ANSWER: PARTLY -- F'(1) clears the "
                  "deficit on some cells only; the linear route "
                  "covers those, the genuine pair-correlation "
                  "input stands on the listed failing cells.")
        else:
            print("  PLAIN ANSWER: NO -- F'(1) clears the deficit "
                  "nowhere; the one-sided endpoint bound is too "
                  "weak and the pair-correlation contract stands "
                  "as the needed input.")
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed"
          % (time.time() - T0, n_tot, n_tot - n_pass))
    return 0 if n_pass == n_tot else 1


if __name__ == "__main__":
    raise SystemExit(main())
