#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""eta_margin_source_probe -- PRIME.PORT.ETASOURCE.01
(EXPLORATION ONLY, experiments/; round 52, named object (a): find
the SOURCE of the non-decaying inheritance margin eta_h -- the one
unexplained object of the program.  2026-08-09.)

THE QUESTION (frozen): relative_congruence_probe (round 51) made
the inheritance exact -- A_{h+1} = A_h^{1/2}(I + H_h)A_h^{1/2},
H_h = A_h^{-1/2} Delta_h A_h^{-1/2} on the 12x12 window, margin
eta_h = 1 + lambda_min(H_h) -- and measured the margin ladder:
min eta = 0.0050, median 0.29, NO decay (power slope +0.108)
while tau_h = lambda_min(A_h) collapses at slope -2.74; every
single-source regression (block mass / ||Delta||_F / tau / gap /
soft overlap) reached R^2 <= 0.103: MARGIN-UNEXPLAINED.
deepcore_schur_reduction_probe located the wall in the fixed 8x8
Schur core S_h (lambda_min(S) = tau to 8 digits; core inheritance
eta_core min 0.0315, median 0.398; lambda_min(R)/tau trendless,
ratio range ~210..2200); pivot_factor_probe showed the soft flag
k = 12 carries the collapse scale.  WHY does eta_h not decay?

THE HYPOTHESIS (frozen before the run): the eta margin is a
CORE-vs-EXTERIOR decomposition effect -- the dangerous direction
of H_h lives in the soft/core subspace where the WALL scale (tau)
rules, but eta measures the RELATIVE increment, and relative to
A ~ tau on the core the increment is O(1)-bounded because the
increment and the operator COLLAPSE AT THE SAME RATE (both are
sections of the same arithmetic object).  Concretely: if Delta
restricted to the dangerous direction scales like tau (not like a
fixed size), then H_soft = Delta_soft / A_soft ~ O(1) -- the
non-decay of eta is the statement "the increment respects the
wall scale".

THE LADDER (frozen, relative_congruence verbatim): all frame-A
zones (core.frame_a_zones()) with h <= 900, sorted by (h, kz);
consecutive FULL-WINDOW pairs (both rungs carry all 12 indices of
J = {2, 4, ..., 24}; typed skips counted); truth + smooth-mass
world (B1 LATTICE-SMOOTH masses m_n = 2 e^{u_n/2} du_n, midpoint
cells, lattice_parametrix verbatim); Epstein/scramble frame
status reported (C1).  ONE Gram build per rung feeds BOTH the
12x12 window compression (relative_congruence verbatim) and the
full-wall Schur split (deepcore_schur_reduction verbatim) -- the
two probes computed the identical E_h independently; sharing it
is exact.

COORDINATE FREEZES: on a full window the alias order is exactly
JWIN = (2, 4, ..., 24) (warded); CORE aliases = {2, ..., 16} =
window positions 0..7; EXTERIOR aliases = {18, ..., 24} =
positions 8..11.  The minimizer v_min is the A_h^{-1/2}-
transported, Euclidean-normalized eigenvector of H_h at
lambda_min (the round-51 "ovl" object): it solves the generalized
problem Delta_h v = lambda_min A_h v in window coordinates, so
coordinate masses and Rayleigh quotients are read there.

FROZEN PROTOCOL (2026-08-09; all bars frozen before the run):

 W   PIPELINE WARDS (kill -> PIPELINE-BROKEN): W1 >= 30 truth
     rungs; W1b the atom prefix law exact; W2 every truth full-
     window rung carries jav == JWIN in order (the coordinate
     freeze); W3 >= 20 truth full-window pairs; W4 >= 30 truth
     full-core wall rungs (Schur machinery).

 R0  THE EXACT CONGRUENCE + REPRODUCTION (round-51 anchor; kill
     -> WARD-BROKEN): per truth pair H_h = A^{-1/2} Delta A^{-1/2}
     with (a) SYMMETRIZATION ||H - H^T||/||H|| <= 1e-12,
     (b) RECONSTRUCTION ||A^{1/2}(I+H)A^{1/2} - A_{h+1}||/
     ||A_{h+1}|| <= 1e-10, (c) RAYLEIGH IDENTITY
     |v_min^T Delta v_min / v_min^T A v_min - lambda_min|
     / max(1, |lambda_min|) <= 1e-9 on every step (the exact
     generalized-eigenpair ward -- S2's ratio IS lambda_min),
     (d) LEDGER: 31 truth pairs, min eta = 0.0050, max(-lambda
     _min) = 0.9950 (tol 5.001e-5), median eta = 0.29 (tol
     5.001e-3), (e) SLOPES: full-ladder power slope of eta =
     +0.108 (tol 5.001e-4) and of tau = -2.74 (tol 5.001e-3).

 S1  THE MINIMIZER ANATOMY: per step the coordinate census of
     v_min -- w_core = sum of squared entries on positions 0..7,
     w_ext = 1 - w_core, and the soft-mode overlap ovl =
     |<v_min, s_h>| (s_h = eigenvector of A_h at tau_h).  Full
     ladder printed.  Step classes (frozen DOM_BAR = 0.75):
     CORE-DOMINANT (w_core >= 0.75) / EXTERIOR-DOMINANT (w_ext >=
     0.75) / MIXED; census printed.  h-TREND: OLS slope + R^2 of
     w_core vs log h.  TYPED (by the ladder median): SEAT-CORE
     iff med w_core >= 0.75; SEAT-EXTERIOR iff med w_core <=
     0.25; SEAT-MIXED otherwise.

 S2  THE SCALE-MATCHING TEST (the hypothesis): per step the raw
     increment scale d_h = |v_min^T Delta_h v_min| and the
     operator scale a_h = v_min^T A_h v_min; both ladders and the
     ratio d_h/a_h (= -lambda_min for lambda_min < 0; warded in
     R0.c) printed with a_h/tau_h.  Sign census: steps with
     lambda_min < 0 (the fits run on those; count printed).  THE
     DECISIVE FITS (OLS in log-log vs h): slope b_d of d_h, slope
     b_a of a_h, printed against b_tau.  TYPED (frozen MATCH_TOL
     = 0.5, COLLAPSE_BAR = -1.0): SCALE-MATCHED(b_d, b_a) iff
     |b_d - b_a| <= 0.5 AND max(b_d, b_a) <= -1.0 (both collapse
     at one rate -- the hypothesis holds: eta is scale-free
     because numerator and denominator are sections of one
     object); SCALE-MATCHED-SHALLOW iff |b_d - b_a| <= 0.5 but
     collapse fails; SCALE-MISMATCHED otherwise.  REPORT: the
     per-step fit residuals corr(resid_d, resid_a) and the
     variance ratio var(resid_d - resid_a)/var(resid_d) -- the
     "one object" signature beyond the slopes.

 S3  THE CORE-RESTRICTED MARGIN: (i) window-internal restricted
     margins per step -- eta_core8 = lambda_min(A_cc^{-1/2}
     A'_cc A_cc^{-1/2}) on the 8x8 core block, eta_ext4 likewise
     on the 4x4 exterior block; WARD (exact subspace inequality,
     kill -> WARD-BROKEN): eta_full <= min(eta_core8, eta_ext4)
     + 1e-10 on every step (the generalized Rayleigh quotient on
     a coordinate subspace can only rise).  (ii) THE SCHUR CORE
     REPRODUCTION (deepcore machinery, full wall A = I - E on
     all folded neg nodes, S_h = B - X R^{-1} X^T at the fixed
     aliases {2..16}): eta_core^schur = lambda_min(S_h^{-1/2}
     S_{h+1} S_h^{-1/2}) over consecutive full-core pairs with
     PD base; WARDS (kill -> WARD-BROKEN; refs per SPEC v2 = the
     deepcore printed ledger): min = 0.0315 (tol 5.001e-5),
     median = 0.3975 (tol 5.001e-5), max |lamS/tau - 1| =
     6.271e-05 and max |lamS*wcore/tau - 1| = 8.379e-08 (the
     round-51 "S = tau to 8 digits" object), both within
     relative 1.001e-3.
     THE BINDING ANSWER: min over the ladder of eta_full vs
     eta_core8 vs eta_ext4 (same frame; the reviewer arithmetic
     eta_full 0.0050 < eta_core^schur 0.0315 printed alongside);
     rho_mix = min eta_full / min(min eta_core8, min eta_ext4).
     TYPED: BIND-CORE / BIND-EXT by which window block min is
     smaller, + MIXING-ESSENTIAL iff rho_mix <= 0.5 else
     MIXING-MARGINAL; the S1 anatomy at the argmin step of
     eta_full printed (the mixing measured, tying S1 to S3).

 S4  THE PREDICTION TEST (the payoff): from the S2 fitted power
     laws, eta_pred(h) = 1 - exp(fit_d(log h))/exp(fit_a(log h))
     on the fitted steps; compare to the measured eta ladder by
     LINEAR-space R^2 = 1 - SS_res/SS_tot (log space breaks if
     eta_pred <= 0; nonpositive predictions counted and printed).
     TYPED (frozen): ETA-EXPLAINED iff R^2 >= 0.8 (the margin is
     the ratio of two tau-law sections; the SOURCE question then
     becomes "why is the section ratio < 1" -- a relative-density
     statement about consecutive windows of ONE object);
     ETA-PARTIAL iff 0.3 <= R^2 < 0.8; ETA-OPEN otherwise
     (honest).

 C   CONTROLS: (C1, kz 9, must fire, kill -> WARD-BROKEN per the
     frozen enum) Epstein (lambda_eps recursion comb) + scramble
     (seed 1): the compressed frame must die (exterior
     supercritical OR lam(C_J) > 1 OR window unavailable);
     channel reported.  (C2, report + reproduction ward, kill ->
     WARD-BROKEN) the smooth world: round-51 v2(ii) measured 28
     smooth full-window pairs, ALL CONE-EXITED (A_h indefinite on
     every pair) -- reproduced here (28 pairs, 0 PD bases) and
     REPORTED; no smooth eta ladder exists.

KILLS: K1 a W ward breaks -> PIPELINE-BROKEN; KW an R0/S3 ward,
a reproduction ward, or a control breaks -> WARD-BROKEN.  S1/S2/
S4 labels and the S3 binding label are TYPED, never kill.

VERDICT (frozen enum): ETASOURCE-MEASURED / <SEAT-*> /
<SCALE-*> / <BIND-*> / <ETA-*>; else PIPELINE-BROKEN /
WARD-BROKEN.

FROZEN BARS: H_DEEP_MAX = 900; JWIN = (2,...,24); CORE positions
0..7 (aliases 2..16), EXTERIOR positions 8..11 (aliases 18..24);
ASYM_WARD 1e-12; RECON_WARD 1e-10; RAY_WARD 1e-9; SUB_WARD 1e-10;
DOM_BAR 0.75; SEAT bars 0.75/0.25; MATCH_TOL 0.5; COLLAPSE_BAR
-1.0; PRED_R2_BAR 0.8; PRED_PARTIAL_BAR 0.3; MIX_BAR 0.5;
reproduction refs: 31 truth pairs / min eta 0.0050 / max(-lam)
0.9950 / med eta 0.29 / slope eta +0.108 / slope tau -2.74 / 28
smooth pairs all CONE-EXITED / eta_core^schur min 0.0315 med
0.3975 / lamS-ledger deviations 6.271e-05 and 8.379e-08 (SPEC
v2); CTRL_KZ 9; scramble seed 1.

SPEC v1 (2026-08-09, frozen + SHA-hashed before the first run):
everything above, with the S3 Schur wards as first frozen: min
eta_core = 0.0315 (tol 5.001e-5), median = 0.398 (tol 5.001e-4,
transcribed from the round-51 contract citation), and max
|lamS/tau - 1| <= 1e-6 (transcribed from the citation "S = tau
to 8 digits").  Mechanical concretizations frozen with v1:
(i) core.build_window results are cached per kz and shared
between the truth window rung, the smooth window rung, and the
wall Schur rung (pure memoization of a deterministic function,
deepcore precedent); (ii) the S2/S4 fits use the step's FIRST
rung depth h_a (round-51 trend convention) and run over the
steps with lambda_min < 0 (log of a positive increment scale);
(iii) the Schur inheritance ladder replicates deepcore's
inherit_ladder skip logic verbatim (both rungs core-complete,
base S PD and base rung neg(A) = 0).

SPEC v2 (2026-08-09, after run 1; fail-first preserved): run 1
passed 18/20 checks; the two FAILS were the S3 Schur wards whose
reference values had been TRANSCRIBED FROM ROUNDED CITATIONS
instead of the predecessor's printed ledger.  The predecessor
(deepcore_schur_reduction_probe) was re-run in-session (16/16
green) and its ledger reads: max |lamS/tau - 1| = 6.271e-05
(EXACTLY what run 1 measured, 6.27e-05 -- the citation "S = tau
to 8 digits" refers to the PRODUCT lamS*wcore/tau, ledger max
|.-1| = 8.379e-08); truth eta_core min 0.0315 med 0.3975 max
7.4287 over 39 steps / 2 skips (run 1: 0.0315 / 0.3975 / 7.4287
/ 39 / 2 -- identical; the citation's "0.398" was a rounding of
0.3975 that sits exactly 5.0e-4 from the printed value, outside
tol by construction).  AMENDMENT (reference repair only, no
probe object, no bar philosophy, no typed label moved; every
run-1 measured number stands): the S3.2 ward now REPRODUCES the
ledger (|dev/6.271e-05 - 1| <= 1.001e-3, plus the product object
|dev_prod/8.379e-08 - 1| <= 1.001e-3, wcore = squared core mass
of the wall soft mode, deepcore verbatim), and the S3.3 median
ref is the ledger value 0.3975 (tol 5.001e-5, print precision).

NO RH claim: eta ladders, coordinate censuses and power-law fits
on finite-h window truncations are measurements on the deployed
v563 ladder, not theorems about zeros.  No marker moves.

FIREWALL: no zeros, no prime oracles (AST scan; banned ids
zetazero / nzeros / primerange / isprime / primepi / nextprime /
prevprime); v563 READ-ONLY; RNG only inside the declared scramble
control; stdout only.

Sources (read-only): v563_paper2_readouts (build_window,
atom_lags_at, arch_lags, U_ALL / MU_ALL prefix law -- verbatim);
window compression + congruence machinery + smooth-mass world
verbatim from relative_congruence_probe.py
(PRIME.PORT.RELCONG.01, round 51) via
factor_avoidance_euler_probe.py / lattice_parametrix_probe.py;
full-wall Schur split + core inheritance verbatim from
deepcore_schur_reduction_probe.py (PRIME.PORT.DEEPCORE.SCHUR.01);
soft-flag context from pivot_factor_probe.py
(PRIME.PORT.PIVOTFACTOR.01); certified base rungs v884/v887
(cited, not re-run).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/eta_margin_source_probe.py
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

H_DEEP_MAX = 900
JWIN = tuple(range(2, 25, 2))
CORE_J = (2, 4, 6, 8, 10, 12, 14, 16)
N_CORE = 8
MIN_RUNGS = 30
MIN_PAIRS = 20
MIN_CORE_RUNGS = 30
MIN_COMMON_J = 8
ASYM_WARD = 1e-12
RECON_WARD = 1e-10
RAY_WARD = 1e-9
SUB_WARD = 1e-10
DOM_BAR = 0.75
SEAT_HI = 0.75
SEAT_LO = 0.25
MATCH_TOL = 0.5
COLLAPSE_BAR = -1.0
PRED_R2_BAR = 0.8
PRED_PARTIAL_BAR = 0.3
MIX_BAR = 0.5
CTRL_KZ = 9
BANNED_IDS = ("zetazero", "nzeros", "primerange", "isprime",
              "primepi", "nextprime", "prevprime")

# reproduction refs (round-51 printed ledgers)
REF_N_TRUTH_PAIRS = 31
REF_TRUTH_MINETA = 0.0050
REF_TRUTH_MAXNEG = 0.9950
REF_TRUTH_MEDETA = 0.29
REF_SLOPE_ETA = +0.108
REF_SLOPE_TAU = -2.74
REF_N_SMOOTH_PAIRS = 28
REF_SMOOTH_PD = 0
REF_CORE_MINETA = 0.0315
REF_CORE_MEDETA = 0.3975          # SPEC v2: deepcore ledger
REF_LAMS_TAU_DEV = 6.271e-05      # SPEC v2: deepcore ledger
REF_LAMS_PROD_DEV = 8.379e-08     # SPEC v2: deepcore ledger
REL_LEDGER_TOL = 1.001e-3
TOL4 = 5.001e-5
TOL3 = 5.001e-4
TOL2 = 5.001e-3

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


# --------- pipeline, verbatim from relative_congruence_probe
def grid_density(c):
    c = np.asarray(c, float)
    a = np.concatenate([c, c[-2:0:-1]])
    d = np.fft.fft(a)
    assert float(np.max(np.abs(d.imag))) <= 1e-9 * max(
        1.0, float(np.max(np.abs(d.real))))
    return d.real


def lambda_eps(N):
    r = np.zeros(N + 1)
    s = int(math.isqrt(N)) + 1
    for x in range(-s, s + 1):
        for y in range(-s, s + 1):
            v = x * x + 5 * y * y
            if 1 <= v <= N:
                r[v] += 1.0
    a = r / 2.0
    lam = np.zeros(N + 1)
    for n in range(2, N + 1):
        acc = a[n] * math.log(n)
        for dd in range(2, n):
            if n % dd == 0:
                acc -= lam[dd] * a[n // dd]
        lam[n] = acc
    return lam


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


def build_E(kz, scramble_seed=None, comb=None, rr_cache=None):
    """One rung -> full folded-neg Gram E (shared by the window
    compression AND the wall Schur split; both predecessors
    computed this identical object)."""
    rr = (rr_cache if rr_cache is not None
          else core.build_window(kz, scramble_seed=scramble_seed))
    h, M, D, alpha = rr["h"], rr["M"], rr["D"], rr["alpha"]
    uu = np.asarray(rr["uu"], float)
    mm = 2.0 * np.asarray(rr["lam"], float)
    if comb is not None:
        uu, mm = comb
    c_at, _ = core.atom_lags_at(alpha, M, uu, mm)
    c_ar = np.asarray(core.arch_lags(M, D), float)
    d = grid_density(c_ar + c_at)
    L = 2 * M - 2
    if h > H_DEEP_MAX:
        return "TOO-DEEP"
    xs, ws, _ = folded_measure(d, L, +1.0)
    ys, vs, uf_n = folded_measure(d, L, -1.0)
    al, be, m0, steps = lanczos_chain(xs, ws, h + 1)
    if steps < h + 1 or np.any(be <= 0):
        return None
    Pn = eval_chain(al, be, m0, ys, h)
    E = np.sqrt(vs)[:, None] * (Pn @ Pn.T) * np.sqrt(vs)[None, :]
    E = 0.5 * (E + E.T)
    return dict(kz=kz, h=h, alpha=alpha, E=E, uf_n=uf_n)


def win_of(bE):
    """12x12 window compression (relative_congruence verbatim)."""
    E, uf_n = bE["E"], bE["uf_n"]
    out = dict(kz=bE["kz"], h=bE["h"], alpha=bE["alpha"],
               lamE=float(np.linalg.eigvalsh(E)[-1]))
    idx = {int(j): k for k, j in enumerate(uf_n)}
    jav = [j for j in JWIN if j in idx]
    out["full"] = (len(jav) == len(JWIN))
    if len(jav) >= MIN_COMMON_J:
        iw = [idx[j] for j in jav]
        io = [k for k in range(E.shape[0]) if k not in set(iw)]
        Eo = E[np.ix_(io, io)]
        IO = np.eye(len(io)) - Eo
        CJ = (E[np.ix_(iw, iw)]
              + E[np.ix_(iw, io)] @ np.linalg.solve(
                  IO, E[np.ix_(io, iw)]))
        CJ = 0.5 * (CJ + CJ.T)
        out["CJ"] = CJ
        out["jav"] = jav
        out["lamO"] = float(np.linalg.eigvalsh(Eo)[-1])
        out["lamC"] = float(np.linalg.eigvalsh(CJ)[-1])
    return out


def wall_of(bE):
    """Full-wall Schur split at the fixed core aliases
    (deepcore_schur_reduction verbatim)."""
    E, uf_n = bE["E"], bE["uf_n"]
    n = E.shape[0]
    A = np.eye(n) - E
    evA, VA = np.linalg.eigh(A)
    out = dict(kz=bE["kz"], h=bE["h"], n=n,
               tau=float(evA[0]), negA=int(np.sum(evA < 0.0)))
    idx = {int(j): k for k, j in enumerate(uf_n)}
    out["core_ok"] = all(j in idx for j in CORE_J)
    if not out["core_ok"]:
        return out
    ic = np.array([idx[j] for j in CORE_J], dtype=int)
    out["wcore"] = float(np.sum(VA[ic, 0] ** 2))
    icset = set(ic.tolist())
    ib = np.array([k for k in range(n) if k not in icset],
                  dtype=int)
    B = A[np.ix_(ic, ic)]
    X = A[np.ix_(ic, ib)]
    R = A[np.ix_(ib, ib)]
    evR = np.linalg.eigvalsh(R)
    out["lamR"] = float(evR[0])
    S = B - X @ np.linalg.solve(R, X.T)
    S = 0.5 * (S + S.T)
    out["S"] = S
    out["lamS"] = float(np.linalg.eigvalsh(S)[0])
    return out


def eps_comb(rr):
    N_E = int(math.floor(math.exp(2.0 * rr["alpha"]))) + 1
    lamE_ = lambda_eps(N_E)
    nn = np.nonzero(np.abs(lamE_) > 1e-12)[0]
    return (np.log(nn.astype(float)),
            2.0 * lamE_[nn] / np.sqrt(nn.astype(float)))


# ------------------------------------------- smooth-mass world (B1)
def cell_widths(uu):
    du = np.zeros(len(uu))
    du[1:-1] = 0.5 * (uu[2:] - uu[:-2])
    du[0] = uu[1] - uu[0]
    du[-1] = uu[-1] - uu[-2]
    return du


def smooth_masses(uu):
    """B1 LATTICE-SMOOTH masses m_n = 2 e^{u_n/2} du_n (verbatim)."""
    return 2.0 * np.exp(np.asarray(uu, float) / 2.0) \
        * cell_widths(np.asarray(uu, float))


# ------------------------------------------- congruence machinery
def restricted_eta(Aa, Ab, pos):
    """eta on a coordinate subspace: lambda_min of
    A_pp^{-1/2} A'_pp A_pp^{-1/2} (= 1 + lambda_min(H_pp))."""
    P = np.ix_(pos, pos)
    w, V = np.linalg.eigh(Aa[P])
    Wm = V @ np.diag(w ** -0.5) @ V.T
    return float(np.linalg.eigvalsh(Wm @ Ab[P] @ Wm)[0])


def eta_pairs(rungs):
    """Consecutive full-window pairs: the exact congruence, the
    transported minimizer, its anatomy, the Rayleigh scales and
    the restricted margins (truth PD branch)."""
    rows = []
    n_skip = 0
    n = len(JWIN)
    core_pos = list(range(N_CORE))
    ext_pos = list(range(N_CORE, n))
    for ra, rb in zip(rungs[:-1], rungs[1:]):
        if not (ra.get("full") and rb.get("full")):
            n_skip += 1
            continue
        Aa = np.eye(n) - ra["CJ"]
        Ab = np.eye(n) - rb["CJ"]
        DC = ra["CJ"] - rb["CJ"]           # A_{h+1} = A_h + DC
        ew, Vw = np.linalg.eigh(Aa)
        row = dict(ha=ra["h"], hb=rb["h"], kza=ra["kz"],
                   kzb=rb["kz"], pd=bool(ew[0] > 0.0),
                   tau=float(ew[0]), gap=float(ew[1] - ew[0]),
                   dnorm=float(np.linalg.norm(DC)))
        if not row["pd"]:
            rows.append(row)
            continue
        Wisq = Vw @ np.diag(ew ** -0.5) @ Vw.T
        Wsq = Vw @ np.diag(ew ** 0.5) @ Vw.T
        H = Wisq @ DC @ Wisq
        nH = float(np.linalg.norm(H))
        row["asym"] = (float(np.linalg.norm(H - H.T))
                       / max(nH, 1e-300))
        Hs = 0.5 * (H + H.T)
        lam, U = np.linalg.eigh(Hs)
        recon = Wsq @ (np.eye(n) + Hs) @ Wsq
        row["rec"] = (float(np.linalg.norm(recon - Ab))
                      / max(float(np.linalg.norm(Ab)), 1e-300))
        row["lam_min"] = float(lam[0])
        row["eta"] = 1.0 + float(lam[0])
        vmin = Wisq @ U[:, 0]
        vmin = vmin / float(np.linalg.norm(vmin))
        row["ovl"] = float(abs(vmin @ Vw[:, 0]))
        row["w_core"] = float(np.sum(vmin[:N_CORE] ** 2))
        row["w_ext"] = 1.0 - row["w_core"]
        row["a"] = float(vmin @ (Aa @ vmin))
        row["s_ray"] = float(vmin @ (DC @ vmin))
        row["ray_dev"] = (abs(row["s_ray"] / row["a"]
                              - row["lam_min"])
                          / max(1.0, abs(row["lam_min"])))
        row["eta_c8"] = restricted_eta(Aa, Ab, core_pos)
        row["eta_e4"] = restricted_eta(Aa, Ab, ext_pos)
        rows.append(row)
    return rows, n_skip


def schur_inherit(walls):
    """deepcore inherit_ladder verbatim (truth): eta_core^schur
    per consecutive full-core pair with PD base."""
    rows, n_hard, n_skip = [], 0, 0
    for r1, r2 in zip(walls, walls[1:]):
        if not (r1.get("core_ok") and r2.get("core_ok")):
            n_skip += 1
            continue
        if r1["lamS"] <= 0.0 or r1["negA"] > 0:
            n_hard += 1
            continue
        w, V = np.linalg.eigh(r1["S"])
        Wm = V @ np.diag(1.0 / np.sqrt(w)) @ V.T
        eta = float(np.linalg.eigvalsh(Wm @ r2["S"] @ Wm)[0])
        rows.append((r1["h"], r2["h"], eta))
    return rows, n_hard, n_skip


def ols(x, y):
    """OLS y = a + b x; returns (a, b, R^2)."""
    x = np.asarray(x, float)
    y = np.asarray(y, float)
    b = float(np.cov(x, y, bias=True)[0, 1] / np.var(x))
    a = float(np.mean(y) - b * np.mean(x))
    ss = float(np.sum((y - a - b * x) ** 2))
    st = float(np.sum((y - np.mean(y)) ** 2))
    return a, b, (1.0 - ss / st if st > 0 else float("nan"))


def quart(v):
    q = np.percentile(np.asarray(v, float), [25, 50, 75])
    return "q25 %.4f  med %.4f  q75 %.4f" % tuple(q)


def main():
    section("PRIME.PORT.ETASOURCE.01 -- the SOURCE of the "
            "non-decaying inheritance margin (EXPLORATION ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s"
          % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
    print("    NO RH claim; no marker moves.")
    print("\nS0 -- firewall")
    check("S0.1 AST firewall clean", not ast_scan(BANNED_IDS))

    # ------------------------------------------------------------ W
    section("W -- build the ladders (one Gram per rung -> window "
            "compression + wall Schur split; h <= %d)"
            % H_DEEP_MAX)
    rungs, srungs, walls = [], [], []
    rrs = {}
    n_smooth_dead = 0
    for kz in core.frame_a_zones():
        rr = core.build_window(kz)
        bE = build_E(kz, rr_cache=rr)
        if not isinstance(bE, dict):
            continue
        rrs[kz] = rr
        rungs.append(win_of(bE))
        walls.append(wall_of(bE))
        uu = np.asarray(rr["uu"], float)
        bS = build_E(kz, comb=(uu, smooth_masses(uu)),
                     rr_cache=rr)
        if isinstance(bS, dict):
            srungs.append(win_of(bS))
        else:
            n_smooth_dead += 1
    rungs.sort(key=lambda r: (r["h"], r["kz"]))
    srungs.sort(key=lambda r: (r["h"], r["kz"]))
    walls.sort(key=lambda r: (r["h"], r["kz"]))
    print("    truth: %d rungs, h %d .. %d | smooth-mass: %d "
          "rungs, %d chain/window deaths  [%.1f s]"
          % (len(rungs), rungs[0]["h"], rungs[-1]["h"],
             len(srungs), n_smooth_dead, time.time() - T0))
    pref_dev = max(float(np.max(np.abs(
        2.0 * np.asarray(rr["lam"], float)
        - np.asarray(core.MU_ALL, float)[:int(rr["n_atom"])])))
        for rr in rrs.values())
    check("W1 >= %d truth rungs built" % MIN_RUNGS,
          len(rungs) >= MIN_RUNGS, "%d rungs" % len(rungs),
          kill="K1")
    check("W1b atom prefix law exact (max |mm - MU_ALL prefix| "
          "%.1e == 0)" % pref_dev, pref_dev == 0.0, kill="K1")
    jav_ok = all(r["jav"] == list(JWIN) for r in rungs
                 if r.get("full"))
    check("W2 coordinate freeze: jav == JWIN in order on every "
          "truth full-window rung", jav_ok, kill="K1")
    n_full_core = sum(1 for r in walls if r.get("core_ok"))
    check("W4 >= %d truth full-core wall rungs" % MIN_CORE_RUNGS,
          n_full_core >= MIN_CORE_RUNGS,
          "%d full-core" % n_full_core, kill="K1")
    if KILLS:
        return finish({})

    trows_all, n_skip_t = eta_pairs(rungs)
    srows_all, n_skip_s = eta_pairs(srungs)
    trows = [r for r in trows_all if r["pd"]]
    check("W3 >= %d truth full-window pairs (%d skips), all "
          "bases PD" % (MIN_PAIRS, n_skip_t),
          len(trows) >= MIN_PAIRS
          and len(trows) == len(trows_all),
          "%d pairs" % len(trows), kill="K1")
    if KILLS:
        return finish({})

    # ------------------------------------------------------------ R0
    section("R0 -- the exact congruence + the round-51 anchor "
            "(%d truth pairs)" % len(trows))
    asym_max = float(np.max([r["asym"] for r in trows]))
    rec_max = float(np.max([r["rec"] for r in trows]))
    ray_max = float(np.max([r["ray_dev"] for r in trows]))
    check("R0.a SYMMETRIZATION WARD: max ||H - H^T||/||H|| "
          "%.2e <= %.0e" % (asym_max, ASYM_WARD),
          asym_max <= ASYM_WARD, kill="KW")
    check("R0.b RECONSTRUCTION WARD: max rel "
          "||A^{1/2}(I+H)A^{1/2} - A_{h+1}|| %.2e <= %.0e"
          % (rec_max, RECON_WARD), rec_max <= RECON_WARD,
          kill="KW")
    check("R0.c RAYLEIGH IDENTITY WARD: max |vDv/vAv - lam_min| "
          "%.2e <= %.0e (S2's ratio IS lambda_min)"
          % (ray_max, RAY_WARD), ray_max <= RAY_WARD, kill="KW")
    etas = np.array([r["eta"] for r in trows])
    min_eta = float(np.min(etas))
    med_eta = float(np.median(etas))
    max_neg = float(np.max([-r["lam_min"] for r in trows]))
    check("R0.d LEDGER: %d pairs == %d, min eta %.4f == %.4f, "
          "max(-lam_min) %.4f == %.4f, med eta %.4f == %.2f"
          % (len(trows), REF_N_TRUTH_PAIRS, min_eta,
             REF_TRUTH_MINETA, max_neg, REF_TRUTH_MAXNEG,
             med_eta, REF_TRUTH_MEDETA),
          len(trows) == REF_N_TRUTH_PAIRS
          and abs(min_eta - REF_TRUTH_MINETA) <= TOL4
          and abs(max_neg - REF_TRUTH_MAXNEG) <= TOL4
          and abs(med_eta - REF_TRUTH_MEDETA) <= TOL2,
          kill="KW")
    lha = np.log([r["ha"] for r in trows])
    _, b_eta, r2_eta = ols(lha, np.log(etas))
    _, b_tau, r2_tau = ols(lha, np.log([r["tau"] for r in trows]))
    check("R0.e SLOPES: eta %+0.4f == %+0.3f (tol %.0e), tau "
          "%+0.4f == %+0.2f (tol %.0e)"
          % (b_eta, REF_SLOPE_ETA, TOL3, b_tau, REF_SLOPE_TAU,
             TOL2),
          abs(b_eta - REF_SLOPE_ETA) <= TOL3
          and abs(b_tau - REF_SLOPE_TAU) <= TOL2, kill="KW")

    # ------------------------------------------------------------ S1
    section("S1 -- THE MINIMIZER ANATOMY: where does the "
            "dangerous direction live?")
    print("    (v_min = A^{-1/2}-transported unit minimizer; "
          "w_core = mass on positions 0..7 = aliases 2..16)")
    print("    step        eta      w_core  w_ext   ovl(soft)  "
          "class")
    n_cd = n_ed = n_mx = 0
    for r in trows:
        if r["w_core"] >= DOM_BAR:
            cls = "CORE-DOMINANT"
            n_cd += 1
        elif r["w_ext"] >= DOM_BAR:
            cls = "EXTERIOR-DOMINANT"
            n_ed += 1
        else:
            cls = "MIXED"
            n_mx += 1
        print("    h %3d->%3d  %.4f   %.4f  %.4f  %.4f     %s"
              % (r["ha"], r["hb"], r["eta"], r["w_core"],
                 r["w_ext"], r["ovl"], cls))
    wc = np.array([r["w_core"] for r in trows])
    med_wc = float(np.median(wc))
    _, b_wc, r2_wc = ols(lha, wc)
    print("\n    CENSUS: CORE-DOMINANT %d | EXTERIOR-DOMINANT %d "
          "| MIXED %d of %d steps (bar %.2f)"
          % (n_cd, n_ed, n_mx, len(trows), DOM_BAR))
    print("    w_core ladder: %s | soft ovl: %s"
          % (quart(wc), quart([r["ovl"] for r in trows])))
    print("    h-TREND: w_core ~ a + b log h with b %+0.4f "
          "(R^2 %.3f)" % (b_wc, r2_wc))
    seat = ("SEAT-CORE" if med_wc >= SEAT_HI
            else "SEAT-EXTERIOR" if med_wc <= SEAT_LO
            else "SEAT-MIXED")
    check("S1.1 typed: %s (median w_core %.4f; bars %.2f/%.2f)"
          % (seat, med_wc, SEAT_HI, SEAT_LO), True)

    # ------------------------------------------------------------ S2
    section("S2 -- THE SCALE-MATCHING TEST: do d_h = |vDv| and "
            "a_h = vAv collapse at ONE rate?")
    neg = [r for r in trows if r["lam_min"] < 0.0]
    print("    sign census: lambda_min < 0 on %d/%d steps "
          "(fits run on those)" % (len(neg), len(trows)))
    print("    step        d=|vDv|     a=vAv       d/a     "
          "a/tau     tau")
    for r in neg:
        print("    h %3d->%3d  %.4e  %.4e  %.4f  %7.3f  %.3e"
              % (r["ha"], r["hb"], abs(r["s_ray"]), r["a"],
                 abs(r["s_ray"]) / r["a"], r["a"] / r["tau"],
                 r["tau"]))
    lhn = np.log([r["ha"] for r in neg])
    ld = np.log([abs(r["s_ray"]) for r in neg])
    la = np.log([r["a"] for r in neg])
    a_d, b_d, r2_d = ols(lhn, ld)
    a_a, b_a, r2_a = ols(lhn, la)
    print("\n    THE DECISIVE FITS (log-log vs h, %d steps):"
          % len(neg))
    print("      d_h = |v^T Delta v| : slope %+0.4f  (R^2 %.3f)"
          % (b_d, r2_d))
    print("      a_h = v^T A v       : slope %+0.4f  (R^2 %.3f)"
          % (b_a, r2_a))
    print("      tau_h (reference)   : slope %+0.4f  (R^2 %.3f)"
          % (b_tau, r2_tau))
    print("      slope gap |b_d - b_a| = %.4f (MATCH_TOL %.2f); "
          "|b_d - b_tau| = %.4f, |b_a - b_tau| = %.4f"
          % (abs(b_d - b_a), MATCH_TOL, abs(b_d - b_tau),
             abs(b_a - b_tau)))
    res_d = ld - (a_d + b_d * lhn)
    res_a = la - (a_a + b_a * lhn)
    cres = float(np.corrcoef(res_d, res_a)[0, 1])
    vratio = (float(np.var(res_d - res_a))
              / max(float(np.var(res_d)), 1e-300))
    print("      ONE-OBJECT SIGNATURE (report): corr(resid_d, "
          "resid_a) = %.4f; var(resid_d - resid_a)/var(resid_d) "
          "= %.4f" % (cres, vratio))
    matched = abs(b_d - b_a) <= MATCH_TOL
    collapsing = max(b_d, b_a) <= COLLAPSE_BAR
    scale = ("SCALE-MATCHED(b_d=%+.3f, b_a=%+.3f)" % (b_d, b_a)
             if matched and collapsing
             else "SCALE-MATCHED-SHALLOW(b_d=%+.3f, b_a=%+.3f)"
             % (b_d, b_a) if matched
             else "SCALE-MISMATCHED(b_d=%+.3f, b_a=%+.3f)"
             % (b_d, b_a))
    check("S2.1 typed: %s (|b_d - b_a| %.4f <= %.2f: %s; both "
          "<= %.1f: %s)"
          % (scale, abs(b_d - b_a), MATCH_TOL, matched,
             COLLAPSE_BAR, collapsing), True)

    # ------------------------------------------------------------ S3
    section("S3 -- THE CORE-RESTRICTED MARGIN: window blocks "
            "(same frame) + the Schur core (round-51 anchor)")
    print("    step        eta_full   eta_core8  eta_ext4   "
          "min-block   w_core")
    sub_dev = 0.0
    for r in trows:
        mb = min(r["eta_c8"], r["eta_e4"])
        sub_dev = max(sub_dev, r["eta"] - mb)
        print("    h %3d->%3d  %.4f     %.4f     %.4f     "
              "%-9s   %.4f"
              % (r["ha"], r["hb"], r["eta"], r["eta_c8"],
                 r["eta_e4"],
                 "core" if r["eta_c8"] <= r["eta_e4"] else "ext",
                 r["w_core"]))
    check("S3.1 SUBSPACE WARD: eta_full <= min(eta_core8, "
          "eta_ext4) on every step (max excess %.2e <= %.0e)"
          % (sub_dev, SUB_WARD), sub_dev <= SUB_WARD, kill="KW")

    lamS_dev = float(np.max([abs(r["lamS"] / r["tau"] - 1.0)
                             for r in walls if r.get("core_ok")]))
    prod_dev = float(np.max([abs(r["lamS"] * r["wcore"]
                                 / r["tau"] - 1.0)
                             for r in walls if r.get("core_ok")]))
    check("S3.2 SCHUR LEDGER REPRODUCTION (SPEC v2): max "
          "|lamS/tau - 1| %.3e == %.3e, max |lamS*wcore/tau - 1| "
          "%.3e == %.3e (rel tol %.0e; the round-51 'S = tau to "
          "8 digits' is the product object)"
          % (lamS_dev, REF_LAMS_TAU_DEV, prod_dev,
             REF_LAMS_PROD_DEV, REL_LEDGER_TOL),
          abs(lamS_dev / REF_LAMS_TAU_DEV - 1.0) <= REL_LEDGER_TOL
          and abs(prod_dev / REF_LAMS_PROD_DEV - 1.0)
          <= REL_LEDGER_TOL, kill="KW")
    crows, n_hard_c, n_skip_c = schur_inherit(walls)
    cetas = np.array([e for *_x, e in crows])
    cmin = float(np.min(cetas))
    cmed = float(np.median(cetas))
    print("    eta_core^schur ladder (%d steps, %d hard, %d "
          "skips): min %.4f  med %.4f  max %.4f"
          % (len(crows), n_hard_c, n_skip_c, cmin, cmed,
             float(np.max(cetas))))
    check("S3.3 SCHUR-CORE REPRODUCTION: min eta_core %.4f == "
          "%.4f, med %.4f == %.4f (tol %.0e; SPEC v2 ledger "
          "refs)"
          % (cmin, REF_CORE_MINETA, cmed, REF_CORE_MEDETA, TOL4),
          abs(cmin - REF_CORE_MINETA) <= TOL4
          and abs(cmed - REF_CORE_MEDETA) <= TOL4, kill="KW")

    min_c8 = float(np.min([r["eta_c8"] for r in trows]))
    min_e4 = float(np.min([r["eta_e4"] for r in trows]))
    rho_mix = min_eta / min(min_c8, min_e4)
    kmin = int(np.argmin(etas))
    print("\n    THE BINDING ANSWER (ladder minima): eta_full "
          "%.4f | eta_core8 %.4f | eta_ext4 %.4f | "
          "eta_core^schur %.4f"
          % (min_eta, min_c8, min_e4, cmin))
    print("    reviewer arithmetic: eta_full min %.4f < "
          "eta_core^schur min %.4f -- but the two live in "
          "DIFFERENT frames" % (min_eta, cmin))
    print("    (12x12 window congruence vs 8x8 wall Schur "
          "complement); the SAME-FRAME window comparison")
    print("    carries the binding answer, and the S1 anatomy at "
          "the binding step h %d->%d gives the mixing:"
          % (trows[kmin]["ha"], trows[kmin]["hb"]))
    print("    w_core = %.4f, w_ext = %.4f, eta_core8 = %.4f, "
          "eta_ext4 = %.4f, eta_full = %.4f"
          % (trows[kmin]["w_core"], trows[kmin]["w_ext"],
             trows[kmin]["eta_c8"], trows[kmin]["eta_e4"],
             trows[kmin]["eta"]))
    bind = ("BIND-CORE" if min_c8 <= min_e4 else "BIND-EXT")
    mixl = ("MIXING-ESSENTIAL" if rho_mix <= MIX_BAR
            else "MIXING-MARGINAL")
    check("S3.4 typed: %s + %s (rho_mix = min eta_full / min "
          "block = %.4f, bar %.2f)"
          % (bind, mixl, rho_mix, MIX_BAR), True)

    # ------------------------------------------------------------ S4
    section("S4 -- THE PREDICTION TEST: eta_pred = 1 - "
            "d_fit(h)/a_fit(h) from the two fitted tau-law "
            "sections")
    eta_meas = np.array([r["eta"] for r in neg])
    eta_pred = 1.0 - np.exp((a_d - a_a) + (b_d - b_a) * lhn)
    n_nonpos = int(np.sum(eta_pred <= 0.0))
    print("    step        eta        eta_pred   resid")
    for i, r in enumerate(neg):
        print("    h %3d->%3d  %.4f    %+.4f    %+.4f"
              % (r["ha"], r["hb"], eta_meas[i], eta_pred[i],
                 eta_meas[i] - eta_pred[i]))
    ss_res = float(np.sum((eta_meas - eta_pred) ** 2))
    ss_tot = float(np.sum((eta_meas - np.mean(eta_meas)) ** 2))
    r2_pred = 1.0 - ss_res / ss_tot if ss_tot > 0 else float(
        "nan")
    print("\n    nonpositive predictions: %d/%d; linear-space "
          "prediction R^2 = %.4f (bars %.2f / %.2f)"
          % (n_nonpos, len(neg), r2_pred, PRED_R2_BAR,
             PRED_PARTIAL_BAR))
    pred = ("ETA-EXPLAINED" if r2_pred >= PRED_R2_BAR
            else "ETA-PARTIAL" if r2_pred >= PRED_PARTIAL_BAR
            else "ETA-OPEN")
    check("S4.1 typed: %s (prediction R^2 %.4f)"
          % (pred, r2_pred), True)
    if pred == "ETA-EXPLAINED":
        print("    THE SOURCE QUESTION MOVES: the margin is the "
              "ratio of two tau-law sections of ONE object;")
        print("    'why eta > 0' becomes 'why is the section "
              "ratio < 1' -- a relative-density statement")
        print("    about consecutive windows of the same "
              "arithmetic object.")

    # ------------------------------------------------------------ C
    section("C -- controls")
    spd = [r for r in srows_all if r["pd"]]
    print("  C2 -- smooth world: %d full-window pairs (%d "
          "skips), %d with PD base (round-51 v2(ii): all "
          "CONE-EXITED)" % (len(srows_all), n_skip_s, len(spd)))
    check("C2 smooth reproduction: %d pairs == %d, PD bases %d "
          "== %d (all CONE-EXITED -- no smooth eta ladder "
          "exists; REPORTED)"
          % (len(srows_all), REF_N_SMOOTH_PAIRS, len(spd),
             REF_SMOOTH_PD),
          len(srows_all) == REF_N_SMOOTH_PAIRS
          and len(spd) == REF_SMOOTH_PD, kill="KW")
    print("  C1 -- Epstein/scramble (kz %d, frame must die):"
          % CTRL_KZ)
    ok1 = True
    for nmc, kw in (("Epstein",
                     dict(comb=eps_comb(rrs[CTRL_KZ]),
                          rr_cache=rrs[CTRL_KZ])),
                    ("scramble", dict(scramble_seed=1))):
        try:
            bC = build_E(CTRL_KZ, **kw)
            rc = win_of(bC) if isinstance(bC, dict) else bC
        except (np.linalg.LinAlgError, AssertionError):
            rc = None
        if not isinstance(rc, dict):
            print("    %-8s: rung not built (%r) -> FRAME DIES"
                  % (nmc, rc))
            continue
        if "lamC" not in rc:
            print("    %-8s: window unavailable -> FRAME DIES"
                  % nmc)
            continue
        fired = (rc["lamO"] > 1.0) or (rc["lamC"] > 1.0)
        ok1 &= fired
        print("    %-8s: lam(out) %.3e | lam(C_J) %.3e -> fires "
              "via %s"
              % (nmc, rc["lamO"], rc["lamC"],
                 "EXTERIOR" if rc["lamO"] > 1.0 else
                 "WINDOW" if rc["lamC"] > 1.0 else "NOTHING"))
    check("C1 CONTROLS FIRE (frame death or supercriticality)",
          ok1, kill="KW")

    return finish(dict(seat=seat, scale=scale, bind=bind,
                       mixl=mixl, pred=pred, min_eta=min_eta,
                       b_d=b_d, b_a=b_a, r2_pred=r2_pred,
                       med_wc=med_wc, min_c8=min_c8,
                       min_e4=min_e4, cmin=cmin))


def finish(lab):
    section("V -- FROZEN VERDICT")
    n_pass = sum(1 for _n, okk in CHECKS if okk)
    n_tot = len(CHECKS)
    if KILLS:
        VERDICT = {"K1": "PIPELINE-BROKEN",
                   "KW": "WARD-BROKEN"}[KILLS[0]]
        print("\n  VERDICT: %s" % VERDICT)
    else:
        VERDICT = ("ETASOURCE-MEASURED / %(seat)s / %(scale)s / "
                   "%(bind)s + %(mixl)s / %(pred)s" % lab)
        print("\n  VERDICT: %s" % VERDICT)
        print("  (min eta %(min_eta).4f; median w_core "
              "%(med_wc).4f; slopes b_d %(b_d)+.3f vs b_a "
              "%(b_a)+.3f; window block minima core8 "
              "%(min_c8).4f / ext4 %(min_e4).4f; schur core min "
              "%(cmin).4f; prediction R^2 %(r2_pred).4f)" % lab)
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed"
          % (time.time() - T0, n_tot, n_tot - n_pass))
    return 0 if n_pass == n_tot else 1


if __name__ == "__main__":
    raise SystemExit(main())
