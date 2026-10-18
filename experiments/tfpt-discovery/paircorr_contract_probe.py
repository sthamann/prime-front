#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""paircorr_contract_probe -- PRIME.CASE.PAIRCORR.CONTRACT.01
(EXPLORATION ONLY, experiments/; round 50, follow-up (e): make the
CONDITIONAL diagonal theorem concrete -- extract, print and freeze
the EXACT weighted prime-pair correlation functional whose
nonnegativity implies T_h <= 1 on the critical zone, so the
contract can be registered as a precise conditional reduction.
2026-08-09.)

CONTEXT (machinery verbatim from signed_homotopy_probe /
christoffel_pnt_gamma_probe): round 45 measured the exact envelope
identity (lambda_1 - nu_1) - (lambda_0 - nu_0) = Int_0^1 J_{h,m} dt,
J = sum_f qt_f r_f 1{d_t(f) > 0} p_{t,m}(x_f)^2
    + qt_m r_m 1{d_t(m) < 0},
and typed the gain HOMOTOPY-INDEFINITE-ARITHMETIC with the scaling
control FIRST-ORDER-DOMINATED: the only arithmetic input is
r = the grid residual of the von Mangoldt comb vs PNT.
christoffel_pnt_gamma_probe measured the PNT reference gap NEGATIVE
on every rung, so the needed inequality is
Int_0^1 J dt >= (nu_0 - lambda_0)_m -- the gain must beat the
reference deficit.  christoffel_zone_envelope_probe froze the
critical zone a <= h^{2 theta*}, theta* = 0.700.  THIS probe
regroups the first-order gain into an explicit smoothed prime sum
(the windowed-sum linearity of port_atom_numerator_probe / v882),
extracts the second-order pair kernel on the port-mode subspace,
prints the LaTeX-ready conditional contract, and measures its
finite shadow (the margin ledger).

THE ALGEBRA (exact, frozen): the deployed atom assembly is LINEAR
in the von Mangoldt masses.  With tent_i(u) = (1 - |iD - u|/D)_+
(plus the u < D mirror of the deployed assembly), the symmetric-
extension cosine weights w_i = 1 at i in {0, M-1} else 2, and
theta_f = 2 pi f / L, the per-atom grid response is
    g_f(u) = -(1/2) sum_i tent_i(u) w_i cos(i theta_f),
so the grid residual is r(f) = sum_n mu_n g_f(u_n) - d0at(f)
(mu_n = 2 Lambda(n)/sqrt(n), u_n = log n; d0at = the grid density
of the closed-form PNT lags c0).  Regrouping the fixed-mask first
variation
    J1_{h,m} = sum_f W_{f,m} r(f),
    W_{f,m} = qt_f 1{d0(f) > 0} p_{0,m}(x_f)^2
              + qt_m 1{d0(m) < 0} delta_{fm},
gives the PRIME-SIDE FORM with the explicit node kernel
    K_{h,m}(u) = -(1/2) sum_i tent_i(u) chat_i(m),
    chat_i(m)  = w_i sum_f W_{f,m} cos(i theta_f):
    J1_{h,m} = sum_{n <= X} mu_n K_{h,m}(log n) - K0_{h,m},
    K0_{h,m} = sum_f W_{f,m} d0at(f) = sum_i c0_i chat_i(m).
K_{h,m} is THE WEIGHT the contract needs; everything above is
finite exact linear algebra on the deployed v563 window family.

FROZEN PROTOCOL (2026-08-09; constants frozen before the first
measurement run; heavy rungs only -- the deep rungs add no new
object here and the round-45 pre-sizing already showed their chain
cost; budget < 20 min):

 RUNGS: heavy kz {9, 12, 13, 26, 40} (verbatim selection).
 ALIASES: all port aliases in the frozen critical zone -- truth
   neg nodes (d1(f) < 0, f >= 1) with a_{h,f} = 2 h^2 (1 - x_f)
   <= h^{2 theta*}, theta* = 0.700, ranked by a ascending
   (verbatim round-45 bookkeeping).

 P1 THE FUNCTIONAL, EXPLICITLY (every heavy rung, every zone
   alias): build W_{f,m} from the t = 0 chain (P2 = p_{0,m}^2 by
   the CD identity, verbatim decompose route), the lag transform
   chat = w * (cos(i theta_f) @ W), the node kernel at the atoms
   K_{h,m}(u_n) (tent interpolation of -chat/2, incl. the u < D
   mirror), the prime sum S1 = sum_n mu_n K(u_n) and the smooth
   subtraction K0.  WARDS (exact algebra, float-route only):
   (W1) prime-side form == grid form:
        |S1 - K0 - W.r| / max(|W.r|, sum_n mu_n |K(u_n)| + |K0|)
        <= 1e-10 per alias;
   (W2) K0 route a (W.d0at) == route b (c0.chat), rel <= 1e-12
        against sum_i |c0_i chat_i|.
   PROFILES printed at the critical alias m* = argmin_m G_1(m)
   and at the a-closest alias (rank 1): K(u) samples on
   u/(2 alpha) in {0.10, 0.30, 0.50, 0.70, 0.85, 0.95, 1.00},
   peak location, the smallest contiguous u-window carrying 90%
   of sum_i |K(iD)| (support width), the number n90 of f-modes
   carrying 90% of sum_f |W_{f,m}| (f >= 1), the |W|-weighted
   mean alias frequency tau = 2 pi f/(L D), and the shape
   correlations corr(K, cos(tau_{m} u)) (Fejer reading) and
   corr(K, 1_window) (short-interval reading).

 P2 THE PAIR PART (frozen rungs kz {9, 40}, verbatim round-45 M4
   machinery): FD Hessian H of Phi(s) = (lambda - nu)_{m*} at
   d0 + sum_i s_i r(f_i) delta_{f_i} on the K_SUB = 12 top-|qt r|
   mask-safe grid modes (eta = 0.05, MASK_SAFE = 4, central FD,
   eta/2 diagonal drift reported); the grid-residual Hessian
   Hg_{ik} = H_{ik} / (r_i r_k) and the effective PRIME PAIR
   KERNEL C_{h,m*}(u, u') = sum_{ik} g_{f_i}(u) Hg_{ik}
   g_{f_k}(u') on a frozen 13 x 13 u-grid over [0, 2 alpha]:
   eigen-signature of H (tol 1e-3 relative), the subspace
   frequencies tau_{f_i}, the ASCII sign map of C (tol 1e-3 of
   max |C|), the diagonal profile C(u, u), and the truth-
   direction quadratic (1/2) 1.H.1 against the measured response
   remainder Delta - A - B at m* (B = the exact crossing part,
   closed form via the occupation times tau_f; reported, never a
   kill -- the subspace captures only the dominant modes).

 P3 THE CONTRACT STATEMENT (the deliverable): print the LaTeX-
   ready conditional theorem block (every object defined by the
   deployed constructions; the implication is exact finite
   calculus, see below) + the HONEST CLASSIFICATION: kernel
   typing per rung at m* by the frozen rules
     KERNEL-SHORTINTERVAL iff width90/(2 alpha) <= 0.25
                          AND n90 > 32
     KERNEL-BANDLIMITED   iff n90 <= 32
                          AND width90/(2 alpha) > 0.25
     KERNEL-MIXED         otherwise;
   contract typing = the majority over the 5 heavy rungs (tie ->
   KERNEL-MIXED).  The classical-family reading printed with the
   measured branch marked: (i) SHORTINTERVAL -> a one-sided
   short-interval prime bound at scale X = e^{2 alpha}, window
   width90 (the needed strength named against the known
   unconditional landscape -- psi(x) short-interval asymptotics
   for widths >= x^{0.525}, zero-free-region error
   exp(-c (log x)^{3/5}) -- named, NOT proved, NOT applicable at
   our tiny X); (ii) BANDLIMITED -> a Fejer-type band-limited
   one-sided explicit-formula positivity at the port frequencies
   (the pair-correlation class).  The demanded relative
   cancellation eps_need = deficit_{h,m*} / (sum_n mu_n |K(u_n)|
   + |K0|) printed per rung (the strength gauge).

 P4 THE NUMERICAL MARGIN LEDGER (every heavy rung, every zone
   alias): LHS(truth) = Delta_m = (lambda_1 - nu_1)_m -
   (lambda_0 - nu_0)_m (the measured total gain; its first-order
   part A_m = J1 printed alongside), RHS = deficit_{h,m} =
   (nu_0 - lambda_0)_m, margin = LHS - RHS = (lambda_1 - nu_1)_m
   (exact identity).  All margins positive = the finite shadow is
   CONSISTENT (measurement, never a kill; the LEDGER flag is
   attached to the verdict).

 C  CONTROLS (kz 9, scramble seed 1, the deployed mirror:
   positions uniform on (0, 2 alpha), same masses): the scramble
   LHS must fall below the deficit -- min_m (LHS_scr - deficit)
   = min_m (lambda_scr - nu_scr)_m <= 0 on the scramble zone
   aliases (fallback, disclosed if the zone set is empty: the 8
   a-closest scramble neg nodes).  Silent -> CONTROL-DEAD.

 SELF-TESTS (S0, kill PIPELINE on failure): (i) AST firewall
   clean; (ii) endpoint reconstruction (kz 9): the qt-route
   lambda/nu at the zone aliases vs the verbatim folded_measure
   route, rel <= 1e-8, at both t = 0 and t = 1; (iii) quadratic-
   form self-test per rung at both endpoints: sum_j w_j p*^2 ==
   lambda to rel 1e-8 (verbatim TOL_QF).

KILLS: chain short anywhere needed / self-test failure / zone
alias set empty on a rung -> PIPELINE-BROKEN; W1 or W2 ward
failure -> WARD-BROKEN; value control silent -> CONTROL-DEAD.
P2/P3/P4 outcomes are MEASUREMENTS, never kills.

VERDICT (frozen enum): PAIRCONTRACT-EXTRACTED (+ KERNEL=<typing>
+ LEDGER=<CONSISTENT | INCONSISTENT k/N>) / PIPELINE-BROKEN /
WARD-BROKEN / CONTROL-DEAD.

SPEC AMENDMENTS (fail-first preserved):
  v1 (2026-08-09): initial freeze.  The M4 constants (K_SUB = 12,
  eta = 0.05, MASK_SAFE = 4, EIG_TOL = 1e-3) are the round-45
  frozen values, reused verbatim; the typing thresholds (0.25 /
  32 / 90%) and the 13 x 13 pair grid are frozen a priori, before
  any kernel was computed.

NO RH claim: the conditional theorem printed here is EXACT finite
calculus on the deployed v563 window family -- the implication
"functional >= deficit => T_h <= 1 at (h, m)" is an identity-level
restatement, and the CONTENT is the extraction and typing of the
explicit kernel K_{h,m} and pair kernel C_{h,m}; the hypothesis
itself is measured (finite shadow), not proved, with no bound, no
rate, no uniformity in h.  No marker moves.

FIREWALL: no zeros, no prime oracles beyond the deployed table
(AST scan: zetazero/nzeros/primerange/isprime/primepi/nextprime/
prevprime banned); v563 READ-ONLY; RNG only in the scramble
control; stdout only.

Sources (read-only): v563_paper2_readouts (window geometry, tent
assembly, arch lags, deployed atom table); signed_homotopy_probe
(envelope identity, decompose, M4 Hessian machinery -- verbatim);
christoffel_pnt_gamma_probe (W2 closed-form PNT lags, folded
measures, Lanczos chain -- verbatim); christoffel_zone_envelope_
probe (theta* = 0.700); port_atom_numerator_probe / v882
(windowed-sum linearity), declared inputs.

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/paircorr_contract_probe.py
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
THETA_STAR = 0.700             # frozen zone exponent (ZONESPLIT.01)
PAIR_RUNGS = (9, 40)           # frozen P2 rungs (round-45 M4 rungs)
K_SUB = 12                     # P2 residual subspace dimension
FD_ETA = 0.05                  # P2 central-difference step
MASK_SAFE = 4.0                # P2 chamber-wall safety factor
EIG_TOL = 1.0e-3               # P2 eigen-signature tolerance
TOL_WARD_PRIME = 1.0e-10       # W1: prime-side form == grid form
TOL_WARD_K0 = 1.0e-12          # W2: K0 route a == route b
TOL_SELF_END = 1.0e-8          # S0.2 endpoint reconstruction
TOL_QF = 1.0e-8                # S0.3 quadratic-form self-test
FRAC_MASS = 0.90               # profile mass fraction (frozen)
SHORT_FRAC = 0.25              # typing: support width bar
BAND_N90 = 32                  # typing: mode count bar
NU_PAIR = 13                   # P2 pair-kernel u-grid size
SIGN_TOL = 1.0e-3              # P2 sign-map tolerance (of max |C|)
PROF_FRACS = (0.10, 0.30, 0.50, 0.70, 0.85, 0.95, 1.00)
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
#  PNT lags: verbatim from signed_homotopy_probe / christoffel_pnt_gamma)

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
    """Folded d_PNT, d_truth, residual, weights, zone aliases, the
    exact occupation times, and the lag blocks c0/c1 of one rung."""
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
    tau = np.where(d0 > 0.0, 1.0, 0.0)
    z0 = d0 == 0.0
    tau[z0] = np.where(d1[z0] > 0.0, 1.0, 0.0)
    tau[up] = 1.0 - ts[up]
    tau[dn] = ts[dn]
    return dict(kz=kz, alpha=alpha, M=M, h=h, L=L, F=F, D=D,
                c_ar=c_ar, c0=c0, c1=c1, uu=uu, mm=mm,
                x=x, a=a, qt=qt, d0=d0, d1=d1, d0at=d0at, r=r,
                al_f=al_f, y_al=x[al_f], tau=tau,
                X=math.exp(2.0 * alpha))


def gap_at(R, dv, al_f, qf=False):
    """Chain of the positive part of dv; per alias the Christoffel
    lambda, target mass nu, gap G (qt route, S0.2-pinned)."""
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
    if qf:
        Ppos = eval_chain(al, be, m0, xs, h)
        U = Ppos @ Phi.T
        out["qf_dev"] = float(np.max(np.abs(
            (ws @ (U * U)) / K - 1.0)))
    return out


# ----------------------------------------------------- P1: the prime kernel
def kernel_block(R, e0):
    """W, chat, K at the atoms, prime sum, smooth subtraction, and
    the two wards (all exact algebra; floats route-tested)."""
    al, be, m0 = e0["chain"]
    h, F, M, L = R["h"], R["F"], R["M"], R["L"]
    Pall = eval_chain(al, be, m0, R["x"], h)        # F x h
    U0 = Pall @ e0["Phi"].T                         # F x n_al
    P2 = (U0 * U0) / e0["Kdiag"] ** 2               # p_{0,m}(x_f)^2
    af = R["al_f"]
    W = (R["qt"] * (R["d0"] > 0.0))[:, None] * P2   # F x n_al
    W[af, np.arange(len(af))] += (R["qt"][af]
                                  * (R["d0"][af] < 0.0))
    A_grid = W.T @ R["r"]
    ii = np.arange(M)
    cosIF = np.cos((2.0 * math.pi / L)
                   * np.outer(ii, np.arange(F).astype(float)))
    w_i = np.where((ii == 0) | (ii == M - 1), 1.0, 2.0)
    chat = (cosIF @ W) * w_i[:, None]               # M x n_al
    del cosIF
    # K at the atoms: tent interpolation of -chat/2 (+ u<D mirror)
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
    return dict(W=W, chat=chat, Kat=Kat, S1=S1, K0=K0a,
                A_grid=A_grid, A_prime=A_prime, Sabs=Sabs,
                ward1=ward1, ward2=ward2, P2=P2)


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
    """P1 profile of K_{h,m} at one alias column m_idx."""
    M, D, F, L = R["M"], R["D"], R["F"], R["L"]
    Ki = -0.5 * kb["chat"][1:, m_idx]        # K(iD), i = 1..M-1
    ug = np.arange(1, M) * D
    jl, jr = min_window(np.abs(Ki), FRAC_MASS)
    width = (jr - jl + 1) * D
    u_frac = width / (2.0 * R["alpha"])
    aw = np.abs(kb["W"][1:, m_idx])
    o = np.argsort(-aw)
    cs = np.cumsum(aw[o])
    n90 = int(np.searchsorted(cs, FRAC_MASS * cs[-1]) + 1)
    tauv = 2.0 * math.pi * np.arange(1, F) / (L * D)
    tau_mean = float((aw @ tauv) / max(float(np.sum(aw)), 1e-300))
    f_m = int(R["al_f"][m_idx])
    tau_m = 2.0 * math.pi * f_m / (L * D)
    cw = np.cos(tau_m * ug)
    corr_fej = float((Ki @ cw) / max(
        float(np.linalg.norm(Ki) * np.linalg.norm(cw)), 1e-300))
    ind = ((ug >= ug[jl]) & (ug <= ug[jr])).astype(float)
    corr_short = float((Ki @ ind) / max(
        float(np.linalg.norm(Ki)
              * math.sqrt(max(float(np.sum(ind)), 1.0))), 1e-300))
    ipk = int(np.argmax(np.abs(Ki)))
    samp = []
    for frc in PROF_FRACS:
        i = min(M - 2, max(0, int(round(frc * (M - 2)))))
        samp.append(float(Ki[i]))
    return dict(Ki=Ki, ug=ug, u_lo=float(ug[jl]), u_hi=float(ug[jr]),
                width=float(width), u_frac=float(u_frac), n90=n90,
                tau_mean=tau_mean, tau_m=tau_m, corr_fej=corr_fej,
                corr_short=corr_short, u_pk=float(ug[ipk]),
                K_pk=float(Ki[ipk]), samp=samp, f_m=f_m)


def type_kernel(u_frac, n90):
    if u_frac <= SHORT_FRAC and n90 > BAND_N90:
        return "KERNEL-SHORTINTERVAL"
    if n90 <= BAND_N90 and u_frac > SHORT_FRAC:
        return "KERNEL-BANDLIMITED"
    return "KERNEL-MIXED"


# --------------------------------------------------- P2: the pair kernel
def g_of_u(R, f, ug):
    """The per-atom grid response g_f(u) on a u-grid (tent + mirror,
    exactly the deployed assembly's linearity)."""
    M, L, D = R["M"], R["L"], R["D"]
    th = 2.0 * math.pi * f / L
    i0 = np.floor(ug / D).astype(int)
    fr = ug / D - i0

    def w_of(i):
        return np.where((i == 0) | (i == M - 1), 1.0, 2.0)

    out = np.zeros(len(ug))
    for i_at, v in ((i0, 1.0 - fr), (i0 + 1, fr)):
        ok = (i_at >= 0) & (i_at <= M - 1) & (v > 0.0)
        out += np.where(ok, v * w_of(i_at) * np.cos(i_at * th),
                        0.0)
    m = ug < D
    out[m] += 1.0 - ug[m] / D
    return -0.5 * out


def pair_hessian(R, m_f):
    """FD Hessian of the gap at the PNT point in the K_SUB residual
    subspace at alias grid index m_f (round-45 M4, verbatim)."""
    y_m = np.array([R["x"][m_f]])
    qt, r, d0, h = R["qt"], R["r"], R["d0"], R["h"]
    cand = np.argsort(-np.abs(qt * r), kind="stable")
    safe = (np.abs(d0) >= MASK_SAFE * FD_ETA * np.abs(r)) \
        & (qt > 0.0)
    idx, skipped = [], 0
    for f in cand:
        if len(idx) == K_SUB:
            break
        if safe[f]:
            idx.append(int(f))
        else:
            skipped += 1
    idx = np.array(idx)

    def phi(svec):
        dv = d0.copy()
        dv[idx] += svec * r[idx]
        pos = (dv > 0.0) & (qt > 0.0)
        al, be, m0, steps = lanczos_chain(
            R["x"][pos], (qt * dv)[pos], h + 1)
        if steps < h + 1:
            return None
        P = eval_chain(al, be, m0, y_m, h)
        lam = 1.0 / float(np.sum(P ** 2))
        return lam - qt[m_f] * max(-dv[m_f], 0.0)

    K = len(idx)
    base = phi(np.zeros(K))
    if base is None:
        return None
    H = np.zeros((K, K))
    diag2 = np.zeros(K)
    for i in range(K):
        for eta in (FD_ETA, 0.5 * FD_ETA):
            sp = np.zeros(K)
            sp[i] = eta
            fp, fm = phi(sp), phi(-sp)
            if fp is None or fm is None:
                return None
            if eta == FD_ETA:
                H[i, i] = (fp - 2.0 * base + fm) / eta ** 2
            else:
                diag2[i] = (fp - 2.0 * base + fm) / eta ** 2
    for i in range(K):
        for k in range(i + 1, K):
            s = np.zeros(K)
            vals = {}
            for si in (+1.0, -1.0):
                for sk in (+1.0, -1.0):
                    s[:] = 0.0
                    s[i] = si * FD_ETA
                    s[k] = sk * FD_ETA
                    v = phi(s)
                    if v is None:
                        return None
                    vals[(si, sk)] = v
            H[i, k] = H[k, i] = (
                vals[(1, 1)] - vals[(1, -1)] - vals[(-1, 1)]
                + vals[(-1, -1)]) / (4.0 * FD_ETA ** 2)
    drift = np.abs(diag2 - np.diag(H)) / np.maximum(
        np.abs(np.diag(H)), 1e-300)
    eig = np.linalg.eigvalsh(0.5 * (H + H.T))
    return dict(idx=idx, skipped=skipped, H=H, eig=eig,
                drift_med=float(np.median(drift)))


# ------------------------------------------------------------------ P3 text
CONTRACT_TEX = r"""
  %% ---- LaTeX-ready conditional contract (stdout deliverable) ----
  \noindent\textbf{Conditional contract
  (PRIME.CASE.PAIRCORR.CONTRACT.01).}
  Fix a rung of the deployed ladder: window length $\alpha$, lag
  grid $M$, $D = 2\alpha/M$, $L = 2M-2$, degree $h = M/2$, cutoff
  $X = e^{2\alpha}$; nodes $x_f = \cos(2\pi f/L)$ and folded
  weights $\tilde q_f = m_f\,4\sin^2(\pi f/L)/(2L)$ ($m_f$ the
  fold multiplicity), $f = 0,\dots,L/2$.  Let $c^{\mathrm{ar}}$ be
  the archimedean lags, $c^{1}$ the deployed tent lags of the von
  Mangoldt comb $\{(\log n,\,2\Lambda(n)/\sqrt n)\}_{n\le X}$,
  $c^{0}$ the closed-form tent lags of the PNT density
  $2e^{u/2}\,du$ on $[0,2\alpha]$, and
  $d^{\,t} = \mathcal F[c^{\mathrm{ar}}+c^{0}+t(c^{1}-c^{0})]$ the
  grid densities, $r = d^{\,1}-d^{\,0}$.  For an alias node $y_m$
  ($d^{\,1}_m<0$) let $\lambda_{t,m}$ be the Christoffel minimum
  of $\int|p|^2\,d\mu_t$ over $\deg p<h$, $p(y_m)=1$,
  $\mu_t=\sum_f \tilde q_f\,[d^{\,t}_f]_+\,\delta_{x_f}$, let
  $\nu_{t,m}=\tilde q_m\,[-d^{\,t}_m]_+$, and let $p_{0,m}$ be the
  $t=0$ minimizer.  Define the node weight
  $W_{f,m}=\tilde q_f\,\mathbf 1\{d^{\,0}_f>0\}\,p_{0,m}(x_f)^2
  +\tilde q_m\,\mathbf 1\{d^{\,0}_m<0\}\,\delta_{fm}$
  and the \emph{prime kernel}
  \[
    K_{h,m}(u) \;=\; -\tfrac12\sum_{i=0}^{M-1}
    \mathrm{tent}_i(u)\,w_i\sum_{f} W_{f,m}\cos(2\pi i f/L),
  \]
  with $\mathrm{tent}_i(u)=(1-|iD-u|/D)_+$ plus the $u<D$ mirror
  of the deployed assembly and $w_i\in\{1,2\}$ the symmetric-
  extension cosine weights.  Then the first-order (fixed-mask)
  gain is \emph{exactly} the smoothed one-sided prime sum
  \[
    J^{(1)}_{h,m} \;=\; \sum_{n\le X}\frac{2\Lambda(n)}{\sqrt n}
    \,K_{h,m}(\log n)\;-\;\int_0^{2\alpha}2e^{u/2}K_{h,m}(u)\,du,
  \]
  and with the response remainder
  $R_{h,m} := \bigl[(\lambda_{1,m}-\nu_{1,m})
  -(\lambda_{0,m}-\nu_{0,m})\bigr]-J^{(1)}_{h,m}$, whose leading
  (quadratic) term is the pair form
  $\tfrac12\sum_{n,n'\le X}\delta\mu_n\,\delta\mu_{n'}
  \,C_{h,m}(\log n,\log n')$ with the measured response kernel
  $C_{h,m}$ (this probe, P2), the following holds by exact finite
  calculus on the deployed family:
  \medskip

  \noindent\textbf{IF} for every rung $h \ge H_0$ of the deployed
  ladder and every critical alias $m$ with
  $a_m = 2h^2(1-y_m) \le h^{1.4}$
  \[
    J^{(1)}_{h,m} \;+\; R_{h,m} \;\;\ge\;\;
    \nu_{0,m}-\lambda_{0,m}
    \qquad\text{(the PNT-reference deficit, computable from
    $d^{\,0}$ alone),}
  \]
  \textbf{THEN} $\lambda_{1,m}\ge\nu_{1,m}$ for all such $(h,m)$,
  i.e.\ the port testing ratio satisfies $T_h \le 1$ on the
  critical zone of the ladder.
  %% ---- end contract block ----"""


def main():
    section("PRIME.CASE.PAIRCORR.CONTRACT.01 -- the explicit "
            "prime-pair correlation contract (EXPLORATION ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s"
          % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
    print("    NO RH claim; no marker moves.")

    print("\nS0 -- firewall + self-tests")
    check("S0.1 AST firewall clean", not ast_scan(BANNED_IDS),
          kill="PIPELINE")

    section("B0 -- rungs (geometry + zone aliases)")
    RG = {}
    for kz in HEAVY:
        R = build_rung(kz)
        RG[kz] = R
        print("    kz %-3d h %4d M %4d F %5d: atoms %5d, X %.3e, "
              "zone aliases %3d (a <= h^1.4 = %8.0f)"
              % (kz, R["h"], R["M"], R["F"], len(R["uu"]),
                 R["X"], len(R["al_f"]), R["h"] ** 1.4),
              flush=True)
    order = sorted(HEAVY, key=lambda kz: RG[kz]["h"])
    ok_al = all(len(RG[kz]["al_f"]) > 0 for kz in HEAVY)
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
        e = gap_at(R9, dv, R9["al_f"])
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

    section("E -- exact endpoints per rung: G_m(t) = lambda - nu, "
            "gain Delta_m, deficit (nu_0 - lambda_0)_m")
    RES = {}
    ok_e = True
    qf_worst = 0.0
    for kz in order:
        R = RG[kz]
        e0 = gap_at(R, R["d0"], R["al_f"], qf=True)
        e1 = gap_at(R, R["d1"], R["al_f"], qf=True)
        if e0 is None or e1 is None:
            ok_e = False
            print("    kz %-3d: CHAIN SHORT at an endpoint" % kz)
            break
        qf_worst = max(qf_worst, e0["qf_dev"], e1["qf_dev"])
        delta = e1["G"] - e0["G"]
        ms = int(np.argmin(e1["G"]))
        RES[kz] = dict(e0=e0, e1=e1, delta=delta, ms=ms)
        print("    kz %-3d h %4d (n_al %2d): deficit max %+.3e | "
              "Delta min %+.3e | margin min %+.3e | m* %d "
              "(f %d, a %.1f)"
              % (kz, R["h"], len(R["al_f"]),
                 float(np.max(-e0["G"])), float(np.min(delta)),
                 float(np.min(e1["G"])), ms + 1,
                 int(R["al_f"][ms]), float(R["a"][R["al_f"][ms]])),
              flush=True)
    check("E0 endpoint chains complete on all rungs", ok_e,
          kill="PIPELINE")
    check("S0.3 quadratic-form self-test (sum w p*^2 == lambda, "
          "both endpoints, all rungs)", ok_e
          and qf_worst <= TOL_QF, "worst rel dev %.2e" % qf_worst,
          kill="PIPELINE")
    if not ok_e:
        return finish(None, None)

    section("P1 -- THE FUNCTIONAL: J1 = sum_n mu_n K_{h,m}(log n) "
            "- K0 (regrouped prime-side form + wards)")
    w1_max = w2_max = 0.0
    types = []
    for kz in order:
        R = RG[kz]
        t_a = time.time()
        kb = kernel_block(R, RES[kz]["e0"])
        RES[kz]["kb"] = kb
        w1_max = max(w1_max, kb["ward1"])
        w2_max = max(w2_max, kb["ward2"])
        ms = RES[kz]["ms"]
        print("    kz %-3d h %4d: ward1(prime==grid) %.2e  "
              "ward2(K0 a==b) %.2e  [%.1f s]"
              % (kz, R["h"], kb["ward1"], kb["ward2"],
                 time.time() - t_a), flush=True)
        for tag, mi in (("m*", ms), ("m1", 0)):
            if tag == "m1" and ms == 0:
                continue
            pr = profile(R, kb, mi)
            lab = type_kernel(pr["u_frac"], pr["n90"])
            if tag == "m*":
                types.append(lab)
                RES[kz]["prof"] = pr
                RES[kz]["ktype"] = lab
            print("      K profile %s (alias %2d, f %4d, a %7.1f):"
                  " J1 %+.3e" % (tag, mi + 1, pr["f_m"],
                                 float(R["a"][R["al_f"][mi]]),
                                 float(kb["A_prime"][mi])))
            print("        K(u) at u/2a %s: %s"
                  % ("/".join("%.2f" % f for f in PROF_FRACS),
                     " ".join("%+.1e" % v for v in pr["samp"])))
            print("        peak |K| %.2e at u %.2f (2a = %.2f) | "
                  "90%% support [%.2f, %.2f] width %.2f "
                  "(frac %.3f) | n90 modes %d | mean tau %.2f "
                  "(alias tau %.2f)"
                  % (abs(pr["K_pk"]), pr["u_pk"],
                     2.0 * R["alpha"], pr["u_lo"], pr["u_hi"],
                     pr["width"], pr["u_frac"], pr["n90"],
                     pr["tau_mean"], pr["tau_m"]))
            print("        shape corr: cos(tau_m u) %+.3f | "
                  "window indicator %+.3f -> %s"
                  % (pr["corr_fej"], pr["corr_short"], lab),
                  flush=True)
    check("P1.W1 prime-side form == grid form (max rel %.2e <= "
          "%.0e)" % (w1_max, TOL_WARD_PRIME),
          w1_max <= TOL_WARD_PRIME, kill="WARD")
    check("P1.W2 smooth subtraction route a == route b (max rel "
          "%.2e <= %.0e)" % (w2_max, TOL_WARD_K0),
          w2_max <= TOL_WARD_K0, kill="WARD")

    section("P2 -- THE PAIR PART: effective prime pair kernel "
            "C_{h,m*}(u, u') on the K_SUB = %d port-mode subspace"
            % K_SUB)
    for kz in PAIR_RUNGS:
        R = RG[kz]
        t_a = time.time()
        ms = RES[kz]["ms"]
        m_f = int(R["al_f"][ms])
        out = pair_hessian(R, m_f)
        if out is None:
            check("P2 chains complete (kz %d)" % kz, False,
                  kill="PIPELINE")
            return finish(None, None)
        H, idx, eig = out["H"], out["idx"], out["eig"]
        emx = float(np.max(np.abs(eig)))
        n_pos = int(np.sum(eig > EIG_TOL * emx))
        n_neg = int(np.sum(eig < -EIG_TOL * emx))
        Hg = H / np.outer(R["r"][idx], R["r"][idx])
        ugp = np.linspace(0.0, 2.0 * R["alpha"], NU_PAIR)
        Gp = np.column_stack([g_of_u(R, int(f), ugp)
                              for f in idx])
        Cp = Gp @ Hg @ Gp.T
        tau_i = 2.0 * math.pi * idx / (R["L"] * R["D"])
        # exact crossing part B at m* (closed form, round-45 M3)
        P2c = RES[kz]["kb"]["P2"][:, ms]
        qr = R["qt"] * R["r"]
        A_ms = float(RES[kz]["kb"]["A_grid"][ms])
        FP = float((qr * R["tau"]) @ P2c
                   + qr[m_f] * (1.0 - R["tau"][m_f]))
        B_ms = FP - A_ms
        C_ms = float(RES[kz]["delta"][ms]) - FP
        quad = 0.5 * float(np.ones(len(idx)) @ H @ np.ones(len(idx)))
        mx = float(np.max(np.abs(Cp)))
        frac_pos = float(np.mean(Cp > SIGN_TOL * mx))
        frac_neg = float(np.mean(Cp < -SIGN_TOL * mx))
        print("    kz %-3d (m* %d, f %d; subspace f = %s; %d "
              "skipped mask-unsafe; FD eta/2 med drift %.3f):"
              % (kz, ms + 1, m_f,
                 [int(f) for f in idx], out["skipped"],
                 out["drift_med"]))
        print("      H spectrum: %s" % " ".join("%+.2e" % v
                                                for v in eig))
        print("      signature (tol %.0e rel): %d pos / %d neg "
              "of %d -> %s" % (EIG_TOL, n_pos, n_neg, len(eig),
                               "INDEFINITE" if n_pos and n_neg
                               else ("NSD" if n_neg else "PSD")))
        print("      subspace frequencies tau_i: %s"
              % " ".join("%.2f" % t for t in tau_i))
        print("      pair kernel C on the %d x %d u-grid: "
              "max |C| %.2e, sign census +%.0f%% / -%.0f%% "
              "(|.| > %.0e max)"
              % (NU_PAIR, NU_PAIR, mx, 100 * frac_pos,
                 100 * frac_neg, SIGN_TOL))
        print("      sign map (rows/cols u = 0 .. 2 alpha):")
        for row in Cp:
            print("        " + "".join(
                "+" if v > SIGN_TOL * mx else
                "-" if v < -SIGN_TOL * mx else "." for v in row))
        dg = np.diag(Cp)
        print("      diagonal C(u,u): %s"
              % " ".join("%+.1e" % v for v in dg[::2]))
        print("      truth-direction quadratic (1/2) 1.H.1 %+.3e "
              "vs measured response C_m* %+.3e (Delta %+.3e = A "
              "%+.3e + B %+.3e + C %+.3e)  [%.1f s]"
              % (quad, C_ms, float(RES[kz]["delta"][ms]), A_ms,
                 B_ms, C_ms, time.time() - t_a), flush=True)
    check("P2.1 pair kernel extracted on the frozen rungs "
          "(measurement)", True)

    section("P3 -- THE CONTRACT STATEMENT (LaTeX-ready) + honest "
            "classification")
    H0 = min(RG[kz]["h"] for kz in HEAVY)
    print(CONTRACT_TEX)
    print("\n  Deployed instantiation: H_0 = %d (the shallowest "
          "deployed rung), theta* = %.3f (zone a <= h^{1.4}), "
          "ladder = the frame-A zones of v563." % (H0, THETA_STAR))
    from collections import Counter
    cnt = Counter(types)
    top, ntop = cnt.most_common(1)[0]
    ktype = top if ntop > len(types) // 2 else "KERNEL-MIXED"
    print("\n  HONEST CLASSIFICATION of the hypothesis:")
    print("    kernel typing at m* per rung: %s -> majority %s"
          % (", ".join("kz%d:%s" % (kz, RES[kz]["ktype"])
                       for kz in order), ktype))
    print("    the functional is a smoothed ONE-SIDED weighted "
          "sum of Lambda(n) - PNT-share at scale X = e^{2 alpha}"
          " (X = %.1e .. %.1e on the heavy rungs);"
          % (min(RG[kz]["X"] for kz in HEAVY),
             max(RG[kz]["X"] for kz in HEAVY)))
    mark = ("(i) MEASURED BRANCH" if ktype == "KERNEL-SHORTINTERVAL"
            else "(i)")
    print("    %s short-interval reading: weight concentrated on "
          "a u-window of width %s log-units -> a one-sided "
          "short-interval prime bound; the known unconditional "
          "landscape (psi asymptotics for widths >= x^{0.525}; "
          "zero-free-region error exp(-c (log x)^{3/5})) is "
          "NAMED, not proved, and not applicable at our tiny X."
          % (mark, "/".join("%.2f" % RES[kz]["prof"]["width"]
                            for kz in order)))
    mark = ("(ii) MEASURED BRANCH" if ktype == "KERNEL-BANDLIMITED"
            else "(ii)")
    print("    %s Fejer/band-limited reading: n90 = %s modes, "
          "mean tau = %s -> a band-limited one-sided explicit-"
          "formula positivity at the port frequencies: the "
          "PAIR-CORRELATION class (consistent with the round-45 "
          "HOMOTOPY-INDEFINITE-ARITHMETIC typing)."
          % (mark, "/".join("%d" % RES[kz]["prof"]["n90"]
                            for kz in order),
             "/".join("%.2f" % RES[kz]["prof"]["tau_mean"]
                      for kz in order)))
    print("    demanded relative cancellation eps_need = "
          "deficit / (sum_n mu_n |K| + |K0|) at m*:")
    for kz in order:
        ms = RES[kz]["ms"]
        dfc = float(-RES[kz]["e0"]["G"][ms])
        eps = dfc / max(float(RES[kz]["kb"]["Sabs"][ms]), 1e-300)
        print("      kz %-3d h %4d: deficit %+.3e  scale %.3e  "
              "eps_need %+.3e"
              % (kz, RG[kz]["h"], dfc,
                 float(RES[kz]["kb"]["Sabs"][ms]), eps))
    check("P3.1 contract printed; kernel typed %s" % ktype, True)

    section("P4 -- THE MARGIN LEDGER (finite shadow): LHS(truth) "
            "vs deficit, margin = (lambda_1 - nu_1)_m")
    n_bad = 0
    n_all = 0
    for kz in order:
        R = RG[kz]
        e0, e1 = RES[kz]["e0"], RES[kz]["e1"]
        A = RES[kz]["kb"]["A_prime"]
        delta = RES[kz]["delta"]
        deficit = -e0["G"]
        margin = e1["G"]
        n_all += len(margin)
        n_bad += int(np.sum(margin <= 0.0))
        print("    kz %-3d h %4d (n_al %d):" % (kz, R["h"],
                                                len(margin)))
        print("      %-4s %-5s %-9s %-11s %-11s %-11s %-11s"
              % ("m", "f", "a_m", "J1(A_m)", "LHS=Delta",
                 "deficit", "margin"))
        show = list(range(min(8, len(margin))))
        im = int(np.argmin(margin))
        if im not in show:
            show.append(im)
        for i in show:
            print("      %-4d %-5d %-9.1f %+.3e  %+.3e  %+.3e  "
                  "%+.3e%s"
                  % (i + 1, int(R["al_f"][i]),
                     float(R["a"][R["al_f"][i]]), float(A[i]),
                     float(delta[i]), float(deficit[i]),
                     float(margin[i]),
                     "  <- min margin" if i == im else ""))
        print("      min margin %+.3e | margins > 0: %d/%d"
              % (float(np.min(margin)),
                 int(np.sum(margin > 0.0)), len(margin)),
              flush=True)
    ledger = ("CONSISTENT" if n_bad == 0
              else "INCONSISTENT %d/%d" % (n_bad, n_all))
    print("    ledger: %s (all margins positive = the finite "
          "shadow of the contract holds on the deployed rungs)"
          % ledger)
    check("P4.1 margin ledger recorded: %s (measurement)"
          % ledger, True)

    section("C -- controls (kz 9, scramble seed %d)"
            % SCRAMBLE_SEED)
    rng = np.random.default_rng(SCRAMBLE_SEED)
    us = np.sort(rng.uniform(0.0, 2.0 * R9["alpha"],
                             size=len(R9["uu"])))
    c_s = np.asarray(core.atom_lags_at(R9["alpha"], R9["M"], us,
                                       R9["mm"])[0], float)
    d_s = grid_density(R9["c_ar"] + c_s)[:R9["F"]]
    ff9 = np.arange(R9["F"])
    neg_s = ff9[(ff9 >= 1) & (d_s < 0.0)]
    neg_s = neg_s[np.argsort(R9["a"][neg_s], kind="stable")]
    al_zone = neg_s[R9["a"][neg_s]
                    <= R9["h"] ** (2.0 * THETA_STAR)]
    fell_back = len(al_zone) == 0
    al_use = al_zone if not fell_back else neg_s[:CTRL_FALLBACK_AL]
    es = gap_at(R9, d_s, al_use)
    e0s = gap_at(R9, R9["d0"], al_use)
    if es is None or e0s is None:
        check("C0 scramble chains complete", False,
              kill="PIPELINE")
        return finish(ktype, ledger)
    lhs_s = es["G"] - e0s["G"]
    dfc_s = -e0s["G"]
    worst = float(np.min(lhs_s - dfc_s))       # == min (lam - nu)_s
    fires = worst <= 0.0
    print("    scramble aliases: %d%s | min (LHS_scr - deficit) "
          "= min (lambda - nu)_scr = %+.3e (real kz 9 min margin "
          "%+.3e) -> %s"
          % (len(al_use),
             " (zone empty -> frozen fallback: %d a-closest neg "
             "nodes)" % CTRL_FALLBACK_AL if fell_back else
             " (zone aliases)",
             worst, float(np.min(RES[9]["e1"]["G"])),
             "FIRES" if fires else "SILENT"), flush=True)
    check("C1 value control fires (scrambled comb: LHS falls "
          "below the deficit)", fires, kill="CONTROL")

    return finish(ktype, ledger)


def finish(ktype, ledger):
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
        VERDICT = "PAIRCONTRACT-EXTRACTED"
    sub = []
    if ktype:
        sub.append("KERNEL=%s" % ktype)
    if ledger:
        sub.append("LEDGER=%s" % ledger)
    print("\n  VERDICT: %s%s"
          % (VERDICT, (" (%s)" % "; ".join(sub)) if sub else ""))
    if VERDICT == "PAIRCONTRACT-EXTRACTED":
        print("  PLAIN ANSWER: the conditional reduction is now "
              "concrete -- T_h <= 1 on the critical zone follows "
              "from the printed one-sided prime-sum inequality "
              "with the explicit kernel K_{h,m} (typed %s) plus "
              "the pair remainder; the contract can be "
              "registered as PRIME.CASE.PAIRCORR.CONTRACT.01."
              % (ktype or "n/a"))
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed"
          % (time.time() - T0, n_tot, n_tot - n_pass))
    return 0 if n_pass == n_tot else 1


if __name__ == "__main__":
    raise SystemExit(main())
