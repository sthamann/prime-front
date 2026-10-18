#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""christoffel_ratio_probe -- PRIME.PORT.CHRISTOFFEL.RATIO.01
(EXPLORATION ONLY, experiments/; round 55, reviewer priority 3
('the probably shortest analytic theorem'): identify the soft-flag
constant c_h = d_{12,h}/tau_h as an INDEPENDENT positive
determinant/Christoffel quantity, so that bounded c-ratios +
positive pivot quotients => tau-sign propagation.  2026-08-09.)

THE QUESTION (frozen).  Round 52 (relative_flag_margin_probe,
PRIME.PORT.RELFLAG.01) factored the dangerous soft-flag quotient
EXACTLY as r_12 = (tau'/tau) x (c'/c) with c_h = d_{12,h}/tau_h,
and measured c trendless (quartiles 1163/2117/2930) after the
kz-21 COORDINATE-ARTIFACT (round 53, kz21_outlier_probe:
c(kz21) = 50667 at h = 371, soft-mode weight collapse at window
coordinate 12; spread 124.2 -> 8.5 without it, SENSITIVITY).
The reviewer's three candidate identifications of c as an
independent quantity are derived EXACTLY and measured head to
head; the winner is the coordinate for the ratio theorem.

THE THREE IDENTIFICATIONS (exact algebra on A = I - C_J(h),
12x12, PD rungs; tau = lambda_min(A), d_12 the last unpivoted
LDL^T pivot; all warded):

 (i)   DETERMINANT QUOTIENT.  Pivot algebra: d_k =
       det A^(k) / det A^(k-1) (leading minors), so
         d_12 = det A / det A^(11),
         c = [det A / tau] / det A^(11)
       with A^(11) the leading 11x11 minor -- c is a quotient of
       two hard determinants over the wall scale.

 (ii)  EIGENPRODUCT.  det A = prod_r lambda_r = tau x
       prod_{r != soft} lambda_r (soft := the minimal eigenvalue;
       lambda_soft / tau == 1 IDENTICALLY since tau :=
       lambda_min -- the warded content is det A = prod_r
       lambda_r), so
         c = prod_{r != soft} lambda_r / det A^(11):
       the product of the 11 non-critical eigenvalues over the
       bulk determinant.

 (iii) DEFLATED-CHRISTOFFEL.  On the FULL wall A_full = I - E
       with E = B B^T, B = diag(sqrt(v)) P (P = the orthonormal
       polynomials of the deployed POSITIVE measure mu_+
       evaluated at the folded NEG nodes), Woodbury gives
         (I - E)^{-1} = I + B (I_h - G)^{-1} B^T,
         G = B^T B = sum_j v_j p(y_j) p(y_j)^T,
       where I_h - G is the moment (Gram) matrix of the DEFLATED
       signed functional sigma = mu_+ - nu_- in the mu_+-
       orthonormal basis.  With K_sigma(y, y) := p(y)^T
       (I_h - G)^{-1} p(y) the CD-kernel diagonal of sigma
       (lambda_sigma(y) = 1/K_sigma(y, y) its Christoffel
       function), the resolvent diagonal at the soft coordinate
       j* (fold index 24 = window coordinate 12) is
         (A_full^{-1})_{j*,j*} = 1 + v_* K_sigma(y_*)
       and the Schur block-inverse identity (A_12 = the Schur
       complement of A_full onto the window => A_12^{-1} =
       [A_full^{-1}]_{WW}) closes the chain:
         1/d_12 = (A_12^{-1})_{12,12} = 1 + v_* K_sigma(y_*)
         = 1 + v_* / lambda_sigma(y_*),
         c = d_12 / tau = 1 / (tau (1 + v_* K_sigma(y_*))).
       So d_12 IS a Christoffel evaluation of the deflated
       measure -- vs the plain CD-kernel diagonal E_{j*j*} =
       v_* K_mu(y_*) = T_* (christoffel_hypotheses machinery):
       the diagonal model 1/(1 - T_*) is replaced exactly by the
       deflated kernel.  HONEST NOTE (exact spectra): eig(I - E)
       = {1 - eig(G)} u {1}^(n-h), so lambda_min(I_h - G) =
       tau_full EXACTLY -- the deflated functional is PD iff the
       wall is PD: identification (iii) RELOCATES the positivity
       premise into Christoffel coordinates, it does not weaken
       it.  The independence claim lives in the BOUNDEDNESS
       (C2), not the positivity.

FROZEN PROTOCOL (all truth full-window rungs, frame-A zones,
h <= H_DEEP_MAX = 900; machinery verbatim from
relative_flag_margin_probe / kz21_outlier_probe):

 C1  THE THREE IDENTIFICATIONS, EXACTLY.  Per full rung print
     the ladder (kz, h, tau_full, tau_12, d_12, c, m_def =
     v_* K_sigma(y_*), (1-T_*)/d_12, lamR/tau_full).  WARDS
     (kill -> WARD-BROKEN):
       W-C1a  d_12 (minor quotient, slogdet route) ==
              1/(A_12^{-1})_{12,12} (inverse route), rel <=
              ID_WARD = 1e-9; leading-minor signs all +1.
       W-C1b  det A == prod_r lambda_r (12x12 eig route), log
              dev <= max(DET_WARD = 1e-8, 100 eps / tau_12);
              AND c == prod_{r != soft} lambda_r / det A^(11),
              same bar (identification (ii) exact up to the
              lambda_soft/tau ratio == 1 by construction).
       W-C1c  THE DEFLATION CHAIN: 1/d_12 == 1 + m_def, rel <=
              max(CHR_WARD_FLOOR = 1e-8, CHR_COND_FAC = 1e3 x
              eps / tau_full) per rung (two INDEPENDENT routes
              through different matrices; the bar is the honest
              floating-point floor of the 1/tau_full
              conditioning).
       W-C1d  c >= 1 - CGE1_WARD (= 1e-9) and tau_12 > 0 on
              every full truth rung (PD premise of the ladder).
       W-C1e  SPOT WARDS on the N_SPOT = 2 shallowest full-
              window+full-core rungs with h <= H_SPOT_MAX = 150
              (dense routes affordable there): tau_full ==
              lambda_min(A_full) dense (abs <= SPOT_WARD_ABS =
              1e-10); lamR == lambda_min(R) dense (abs <=
              SPOT_WARD_ABS); (A_12^{-1})_{12,12} ==
              [A_full^{-1}]_{j*,j*} dense solve == 1 + m_def
              (rel <= SPOT_WARD = 1e-8) -- the factor-Gram
              spectral identity and the block-inverse identity
              verified against dense linear algebra.
       W-C1f  REPRODUCTION (round 52/53 printed ledgers): 37
              full-window rungs; raw c quartiles q25/med/q75
              within 2e-2 of 1163/2117/2930; c(kz21) within
              2e-2 of 50667 at h == 371.

 C2  THE POSITIVITY SOURCE / EXPOSURE.  c > 0 is automatic on
     the PD ladder (both factors positive); the CONTENT is
     boundedness.  Decompose log c = log det A - log tau -
     log det A^(11) into the two pieces each identification
     names:
       (i)   N = log det A,            D = log tau + log det A11
       (ii)  N = log det A - log tau,  D = log det A11
       (iii) N = log d_12,             D = log tau
     and per identification print var(N), var(D), the OLS
     slopes of N and D vs log h, and corr(N, D), on the
     SENSITIVITY set (kz 21 excluded per the round-53
     COORDINATE-ARTIFACT rule; raw 37-rung values printed
     alongside).  TYPED WINNER (frozen rule, never kills):
     argmin_k max(var N_k, var D_k) -- the identification whose
     pieces are individually most bounded, i.e. whose
     boundedness of c depends least on cancellation ->
     WINNER-DETQUOT / WINNER-EIGPROD / WINNER-CHRISTOFFEL
     (ties, not expected: lowest k).  THE EXTERIOR CONNECTION:
     on full-window+full-core rungs print corr(log c,
     log(lamR/tau_full)) (raw AND sensitivity; the DECISIVE
     number) and the ratio ladder c/(lamR/tau_full) with
     quartiles -- is the measured 210..2200 exterior reserve
     (deepcore_schur) the SOURCE of c's boundedness?  TYPED
     (never kills): EXTSOURCE-COUPLED(corr) iff the sensitivity
     corr >= EXT_CORR_BAR = 0.5, else EXTSOURCE-DECOUPLED(corr).
     WARD (kill -> WARD-BROKEN): >= MIN_EXT_RUNGS = 25 rungs
     carry both objects.

 C3  THE RATIO THEOREM SHADOW.  On consecutive full-window
     pairs (round-52 census: 31): r_12 = d'_12/d_12 > 0 census,
     the c-ratio ladder c'/c printed in full; [m, M] = min/max
     RAW (31 pairs) and SENSITIVITY (pairs touching kz 21
     excluded, expected 29; the round-53 rule -- raw numbers
     stand, the typed range is the sensitivity one, said
     plainly).  THE THEOREM STATEMENT PRINTED with measured
     constants: IF 0 < m <= c'/c <= M for all h (bounded
     c-ratios, from the winner identification + the exterior
     reserve) AND r_12 > 0 for all h (positive pivot quotients;
     by (iii) equivalently the deflated functional stays PD --
     the SAME statement as the wall's PD in Christoffel
     coordinates) THEN tau'/tau = r_12 / (c'/c) > 0 (exact
     algebra), and with the certified base (v884/v887, declared
     inputs) tau_h > 0 on the whole ladder.  HONESTY LINE: which
     half is measured (r_12 > 0 on all pairs, c'/c in [m, M],
     the exterior reserve) vs which needs the theorem (both
     hypotheses for ALL h; nothing here proves them).  WARD
     (kill -> WARD-BROKEN): pair census == 31 and r_12 > 0 on
     every pair.

 C   CONTROLS (kill -> WARD-BROKEN if silent):
     C-S  smooth world (B1 LATTICE-SMOOTH masses m_n =
          2 e^{u_n/2} du_n on the true lattice, verbatim): the
          c-machinery must lose its PD premise -- REPRODUCTION:
          28 smooth full-window pairs with base tau_12 <= 0 on
          28/28 (relative_congruence / round-52 C2a verbatim);
          AND the (iii) premise breaks IDENTICALLY: tau_full =
          1 - lambda_max(G) < 0 (deflated functional indefinite)
          on >= 1 smooth rung, count + first h printed.
     C-E  Epstein x^2+5y^2 comb + scramble (seed 1) at kz 9:
          frame death OR neg(A) > 0 OR tau_12 <= 0; channel
          printed.

 W   PIPELINE WARDS (kill -> PIPELINE-BROKEN): W0 truth ladder
     == 42 rungs (deepcore reachable census); W0c truth
     full-window census == 37 (hirota); W0d >= 30 full-core
     rungs; W0e >= 2 spot rungs (h <= 150, full window + core).

KILLS: KP a W ward breaks -> PIPELINE-BROKEN; KW a C1/C2/C3
ward breaks OR a control stays silent -> WARD-BROKEN.  Typed
labels (winner, EXTSOURCE) report, never kill.

VERDICT (frozen enum): CHRISTRATIO-MEASURED with typed sublabels
WINNER-DETQUOT / WINNER-EIGPROD / WINNER-CHRISTOFFEL (C2 winner)
and EXTSOURCE-COUPLED(corr) / EXTSOURCE-DECOUPLED(corr) (C2
exterior); else PIPELINE-BROKEN / WARD-BROKEN.

FROZEN BARS: H_DEEP_MAX = 900; JWIN = (2,4,...,24); NW = 12;
CORE_J = (2,4,...,16); N_RUNGS_EXP = 42; N_FULLWIN_FROZEN = 37;
REF_N_TRUTH_PAIRS = 31; REF_N_SENS_PAIRS = 29; REF_N_SMOOTH_PAIRS
= 28; MIN_CORE_RUNGS = 30; MIN_EXT_RUNGS = 25; KZ_STAR = 21;
H_STAR = 371; REF_C21 = 50667 (rtol 2e-2); REF_Q25/MED/Q75 =
1163/2117/2930 (rtol 2e-2); ID_WARD = 1e-9; DET_WARD = 1e-8 (+
100 eps/tau_12 conditioning guard); CHR_WARD_FLOOR = 1e-8;
CHR_COND_FAC = 1e3; CGE1_WARD = 1e-9; SPOT_WARD = 1e-8;
SPOT_WARD_ABS = 1e-10; N_SPOT = 2; H_SPOT_MAX = 150; EXT_CORR_BAR
= 0.5; CTRL_KZ = 9; scramble seed 1; EPS = 2.220446049250313e-16.

SPEC v1 (2026-08-09, frozen + SHA-hashed before the first run):
everything above.  Mechanical concretizations frozen with v1:
(i) core.build_window results are memoized per (kz, seed)
(round-52 verbatim); (ii) ONE Gram E per rung; C_J is built by
the VERBATIM big Schur solve (round-52/53); all FULL-wall
spectral reductions (tau_full, neg counts, lamR) use the exact
factor-Gram identity eig(I - E) = {1 - eig(G)} u {1}^(n-h)
(h x h instead of n x n; spot-warded dense, W-C1e); (iii)
SENSITIVITY statistics = leave-kz-21-out per the round-53
COORDINATE-ARTIFACT diagnosis; typed labels use the sensitivity
values, raw values always printed first; (iv) variances are
population variances (np.var, ddof 0); quartiles np.percentile
linear; OLS slope as in round 52; (v) logs of determinants via
slogdet (signs warded +1); (vi) smooth/control rungs run LIGHT
(G + 12-window only; no core split).

HONEST FRAME: all three identifications are EXACT algebra on PD
rungs -- warded bookkeeping, zero content by themselves.  The
content is (a) WHICH decomposition carries the boundedness with
the least cancellation (measured, typed), (b) whether the
exterior reserve is correlated with c (measured), and (c) the
measured [m, M] of the c-ratio.  The census is FINITE: nothing
here proves the ratio bound or the pivot positivity beyond the
deployed rungs; identification (iii)'s positivity premise is the
wall's own PD premise in different coordinates (said above,
printed again in C3).  NO RH claim.  No marker moves.

FIREWALL: no zeros, no prime oracles (AST scan; banned ids
zetazero / nzeros / primerange / isprime / primepi / nextprime /
prevprime); v563 READ-ONLY; RNG only inside the declared
scramble control; stdout only.

Sources (read-only): v563_paper2_readouts (build_window,
atom_lags_at, arch_lags -- verbatim); c-ladder + 12-window +
smooth-world machinery verbatim from relative_flag_margin_probe
(PRIME.PORT.RELFLAG.01) and kz21_outlier_probe
(PRIME.PORT.KZ21.01: the COORDINATE-ARTIFACT diagnosis, the
spectral identity (A^{-1})_{12,12} = sum_r |psi_r(12)|^2 /
lambda_r); exterior margin machinery from
deepcore_schur_reduction_probe (PRIME.PORT.DEEPCORE.SCHUR.01:
lamR/tau trendless 210..2200); Christoffel-function reading per
christoffel_hypotheses_probe (PRIME.CASE.HYPOTHESES.01:
lambda_h(y) = 1/K(y, y), T_m = nu~_m K(y_m, y_m)); v884/v887
base certificates -- declared inputs, not re-run.

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/christoffel_ratio_probe.py
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
NW = 12
CORE_J = (2, 4, 6, 8, 10, 12, 14, 16)
N_RUNGS_EXP = 42
N_FULLWIN_FROZEN = 37
REF_N_TRUTH_PAIRS = 31
REF_N_SENS_PAIRS = 29
REF_N_SMOOTH_PAIRS = 28
MIN_CORE_RUNGS = 30
MIN_EXT_RUNGS = 25
KZ_STAR = 21
H_STAR = 371
REF_C21 = 50667.0
REF_C21_RTOL = 2e-2
REF_Q25, REF_MED, REF_Q75 = 1163.0, 2117.0, 2930.0
REF_Q_RTOL = 2e-2
ID_WARD = 1e-9
DET_WARD = 1e-8
CHR_WARD_FLOOR = 1e-8
CHR_COND_FAC = 1e3
CGE1_WARD = 1e-9
SPOT_WARD = 1e-8
SPOT_WARD_ABS = 1e-10
N_SPOT = 2
H_SPOT_MAX = 150
EXT_CORR_BAR = 0.5
CTRL_KZ = 9
EPS = 2.220446049250313e-16
BANNED_IDS = ("zetazero", "nzeros", "primerange", "isprime",
              "primepi", "nextprime", "prevprime")
WINNER_NAME = ("WINNER-DETQUOT", "WINNER-EIGPROD",
               "WINNER-CHRISTOFFEL")

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


# --------- pipeline, verbatim (relative_flag_margin / kz21 chain)
def grid_density(c):
    c = np.asarray(c, float)
    a = np.concatenate([c, c[-2:0:-1]])
    d = np.fft.fft(a)
    assert float(np.max(np.abs(d.imag))) <= 1e-9 * max(
        1.0, float(np.max(np.abs(d.real))))
    return d.real


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


def lambda_eps(N):
    """Epstein x^2+5y^2 comb (port_schur_reduction verbatim)."""
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


_WIN_CACHE = {}


def window_of(kz, scramble_seed=None):
    """SPEC v1 (i): pure memoization of core.build_window."""
    key = (kz, scramble_seed)
    if key not in _WIN_CACHE:
        rr = core.build_window(kz, scramble_seed=scramble_seed)
        _WIN_CACHE[key] = dict(
            h=rr["h"], M=rr["M"], D=rr["D"], alpha=rr["alpha"],
            n_atom=rr["n_atom"],
            uu=np.asarray(rr["uu"], float).copy(),
            lam=np.asarray(rr["lam"], float).copy(),
            c_ar=np.asarray(core.arch_lags(rr["M"], rr["D"]),
                            float))
    return _WIN_CACHE[key]


def ols_ab(x, y):
    """OLS y = a + b x -> (a, b)."""
    x = np.asarray(x, float)
    y = np.asarray(y, float)
    xm, ym = float(np.mean(x)), float(np.mean(y))
    b = float(np.sum((x - xm) * (y - ym))
              / np.sum((x - xm) ** 2))
    return ym - b * xm, b


def quart_row(v):
    v = np.asarray(v, float)
    q = np.percentile(v, [25, 50, 75])
    return (float(np.min(v)), float(q[0]), float(q[1]),
            float(q[2]), float(np.max(v)))


def anatomy(kz, scramble_seed=None, comb=None, mode="truth"):
    """One rung -> ONE Gram E on the folded neg nodes -> the
    12-window compression C_J (verbatim big Schur solve) + the
    factor Gram G = B^T B (SPEC v1 (ii): tau_full, neg counts,
    lamR from the exact identity eig(I-E) = {1-eig(G)} u
    {1}^(n-h)) + the deflated-Christoffel mass m_def at the soft
    coordinate.  mode 'truth' adds the fixed-core exterior; E is
    retained on shallow spot rungs (h <= H_SPOT_MAX) for W-C1e.
    """
    rr = window_of(kz, scramble_seed=scramble_seed)
    h, M, D, alpha = rr["h"], rr["M"], rr["D"], rr["alpha"]
    if h > H_DEEP_MAX:
        return "TOO-DEEP"
    uu = rr["uu"]
    mm = 2.0 * rr["lam"]
    if comb is not None:
        uu, mm = comb
    c_at, _ = core.atom_lags_at(alpha, M, uu, mm)
    d = grid_density(rr["c_ar"] + np.asarray(c_at, float))
    L = 2 * M - 2
    xs, ws, _ = folded_measure(d, L, +1.0)
    ys, vs, uf_n = folded_measure(d, L, -1.0)
    al, be, m0, steps = lanczos_chain(xs, ws, h + 1)
    if steps < h + 1 or np.any(be <= 0):
        return None
    Pn = eval_chain(al, be, m0, ys, h)
    B = np.sqrt(vs)[:, None] * Pn
    E = B @ B.T
    E = 0.5 * (E + E.T)
    n = E.shape[0]
    out = dict(kz=kz, h=h, n=n)
    # factor Gram: exact full-wall spectral reductions (h x h)
    G = B.T @ B
    G = 0.5 * (G + G.T)
    egG = np.linalg.eigvalsh(G)
    out["tau_full"] = float(1.0 - egG[-1])
    out["negA"] = int(np.sum(egG > 1.0))
    idx = {int(j): k for k, j in enumerate(uf_n)}
    if mode == "truth":
        out["core_ok"] = all(j in idx for j in CORE_J)
        if out["core_ok"]:
            ic = np.array([idx[j] for j in CORE_J], dtype=int)
            Gx = G - B[ic].T @ B[ic]
            egx = np.linalg.eigvalsh(0.5 * (Gx + Gx.T))
            out["lamR"] = float(1.0 - egx[-1])
            out["negR"] = int(np.sum(egx > 1.0))
    # 12-window compression (verbatim big Schur solve)
    jav = [j for j in JWIN if j in idx]
    out["full"] = (len(jav) == len(JWIN))
    if out["full"]:
        iw = [idx[j] for j in jav]
        io = [k for k in range(n) if k not in set(iw)]
        IO = np.eye(len(io)) - E[np.ix_(io, io)]
        try:
            CJ = (E[np.ix_(iw, iw)]
                  + E[np.ix_(iw, io)] @ np.linalg.solve(
                      IO, E[np.ix_(io, iw)]))
            out["CJ"] = 0.5 * (CJ + CJ.T)
        except np.linalg.LinAlgError:
            out["full"] = False
    if out["full"]:
        jstar = idx[JWIN[-1]]
        p = Pn[jstar]
        mdef = float(vs[jstar]
                     * (p @ np.linalg.solve(np.eye(h) - G, p)))
        out["jstar"] = jstar
        out["m_def"] = mdef
        out["tstar"] = float(E[jstar, jstar])
        if mode == "truth" and h <= H_SPOT_MAX:
            out["E"] = E
    return out


def win_attrs(r):
    """Per-rung 12-window objects: slogdets, minor-quotient d_12,
    inverse route, eigenvalues, the three identification values."""
    A = np.eye(NW) - r["CJ"]
    sg12, ld12 = np.linalg.slogdet(A)
    sg11, ld11 = np.linalg.slogdet(A[:11, :11])
    r["sg_ok"] = (sg12 == 1.0 and sg11 == 1.0)
    r["ld12"], r["ld11"] = float(ld12), float(ld11)
    r["d12"] = math.exp(ld12 - ld11) * sg12 * sg11
    ew = np.linalg.eigvalsh(A)
    r["ew"] = ew
    r["tau12"] = float(ew[0])
    Ainv = np.linalg.inv(A)
    r["a1212"] = float(Ainv[11, 11])
    r["c"] = r["d12"] / r["tau12"] if r["tau12"] != 0.0 \
        else float("inf")
    # W-C1a: minor quotient vs inverse route (same 12x12 matrix)
    r["dev_inv"] = (abs(r["d12"] - 1.0 / r["a1212"])
                    / max(abs(r["d12"]), 1e-300))
    # W-C1b: det == prod eigs; c == prod-noncrit/det11 (id (ii))
    if np.all(ew > 0.0):
        lsum = float(np.sum(np.log(ew)))
        r["dev_det"] = abs(ld12 - lsum)
        c2 = math.exp(float(np.sum(np.log(ew[1:]))) - ld11)
        r["c_eig"] = c2
        r["dev_c2"] = abs(r["c"] - c2) / max(abs(r["c"]), 1e-300)
    else:
        r["dev_det"] = float("inf")
        r["dev_c2"] = float("inf")
    # W-C1c: deflation chain 1/d12 == 1 + m_def (independent route)
    r["dev_chr"] = (abs(1.0 / r["d12"] - (1.0 + r["m_def"]))
                    / max(abs(1.0 / r["d12"]), 1e-300))
    return r


def corr(x, y):
    return float(np.corrcoef(np.asarray(x, float),
                             np.asarray(y, float))[0, 1])


def main():
    section("PRIME.PORT.CHRISTOFFEL.RATIO.01 -- c = d_12/tau as "
            "an independent Christoffel quantity (EXPLORATION "
            "ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s"
          % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
    print("    NO RH claim; no marker moves.")
    print("\nS0 -- firewall")
    check("S0.1 AST firewall clean (no zero/prime oracles)",
          not ast_scan(BANNED_IDS))

    # ------------------------------------------------------------ W
    section("W -- build the truth + smooth ladders (frame-A "
            "zones, h <= %d; ONE Gram per rung)" % H_DEEP_MAX)
    truth, smooth = [], []
    n_toodeep, n_dead_t, n_dead_s = 0, 0, 0
    for kz in core.frame_a_zones():
        r = anatomy(kz, mode="truth")
        if r == "TOO-DEEP":
            n_toodeep += 1
            continue
        if r is None:
            n_dead_t += 1
            continue
        truth.append(r)
        uu = window_of(kz)["uu"]
        rs = anatomy(kz, comb=(uu, smooth_masses(uu)),
                     mode="smooth")
        if isinstance(rs, dict):
            smooth.append(rs)
        else:
            n_dead_s += 1
    truth.sort(key=lambda r: (r["h"], r["kz"]))
    smooth.sort(key=lambda r: (r["h"], r["kz"]))
    print("    truth: %d rungs (h %d..%d; %d TOO-DEEP zones, %d "
          "chain deaths) | smooth: %d rungs (%d deaths)  [%.1f s]"
          % (len(truth), truth[0]["h"], truth[-1]["h"],
             n_toodeep, n_dead_t, len(smooth), n_dead_s,
             time.time() - T0))
    check("W0 truth ladder == %d rungs (deepcore census)"
          % N_RUNGS_EXP, len(truth) == N_RUNGS_EXP,
          "%d" % len(truth), kill="KP")
    fullw = [r for r in truth if r.get("full") and "CJ" in r]
    check("W0c truth full-window census %d == %d (hirota frozen)"
          % (len(fullw), N_FULLWIN_FROZEN),
          len(fullw) == N_FULLWIN_FROZEN, kill="KP")
    fullc = [r for r in truth if r.get("core_ok")]
    check("W0d >= %d full-core rungs" % MIN_CORE_RUNGS,
          len(fullc) >= MIN_CORE_RUNGS, "%d" % len(fullc),
          kill="KP")
    spot = [r for r in truth
            if r.get("full") and r.get("core_ok") and "E" in r]
    check("W0e >= %d spot rungs (h <= %d, full window + core): "
          "%s" % (N_SPOT, H_SPOT_MAX,
                  [(r["kz"], r["h"]) for r in spot[:N_SPOT]]),
          len(spot) >= N_SPOT, kill="KP")
    if KILLS:
        return finish({})

    # ------------------------------------------------------------ C1
    section("C1 -- THE THREE IDENTIFICATIONS, EXACTLY (warded "
            "algebra on every full rung)")
    for r in fullw:
        win_attrs(r)
    sg_all = all(r["sg_ok"] for r in fullw)
    dev_inv = max(r["dev_inv"] for r in fullw)
    check("W-C1a d_12 = det A/det A^(11) == 1/(A_12^-1)_{12,12}: "
          "max rel %.1e <= %.0e; leading-minor signs all +1: %s"
          % (dev_inv, ID_WARD, sg_all),
          dev_inv <= ID_WARD and sg_all, kill="KW")
    dev_det = max(r["dev_det"] for r in fullw)
    dev_c2 = max(r["dev_c2"] for r in fullw)
    bar_det = max(DET_WARD,
                  100.0 * EPS / min(r["tau12"] for r in fullw))
    check("W-C1b det A == prod eigs (max log dev %.1e) AND c == "
          "prod-noncrit-eigs/det A^(11) (max rel %.1e) <= %.1e; "
          "lambda_soft/tau == 1 identically (tau := lambda_min)"
          % (dev_det, dev_c2, bar_det),
          dev_det <= bar_det and dev_c2 <= bar_det, kill="KW")
    chr_worst = max(r["dev_chr"]
                    / max(CHR_WARD_FLOOR,
                          CHR_COND_FAC * EPS / r["tau_full"])
                    for r in fullw)
    dev_chr = max(r["dev_chr"] for r in fullw)
    check("W-C1c DEFLATION CHAIN 1/d_12 == 1 + v_* K_sigma(y_*) "
          "(independent h x h route): max rel %.1e; worst "
          "dev/bar %.3f <= 1 (bar max(%.0e, %.0e eps/tau_full))"
          % (dev_chr, chr_worst, CHR_WARD_FLOOR, CHR_COND_FAC),
          chr_worst <= 1.0, kill="KW")
    c_min = min(r["c"] for r in fullw)
    tau_min = min(r["tau12"] for r in fullw)
    check("W-C1d c >= 1 (exact, min c = %.3f) and tau_12 > 0 on "
          "every full rung (min %.3e)" % (c_min, tau_min),
          c_min >= 1.0 - CGE1_WARD and tau_min > 0.0, kill="KW")
    # spot wards: dense routes on the shallow rungs
    ok_spot = True
    for r in spot[:N_SPOT]:
        A = np.eye(r["n"]) - r["E"]
        evA = np.linalg.eigvalsh(A)
        d1 = abs(r["tau_full"] - float(evA[0]))
        # rebuild the core seats from the window (positions
        # recomputed; exterior = all nodes minus CORE_J)
        w = window_of(r["kz"])
        dd = grid_density(w["c_ar"] + np.asarray(
            core.atom_lags_at(w["alpha"], w["M"], w["uu"],
                              2.0 * w["lam"])[0], float))
        _, _, ufn = folded_measure(dd, 2 * w["M"] - 2, -1.0)
        idxs = {int(j): k for k, j in enumerate(ufn)}
        ic = np.array([idxs[j] for j in CORE_J], dtype=int)
        ib = np.array([k for k in range(r["n"])
                       if k not in set(ic.tolist())], dtype=int)
        evR = np.linalg.eigvalsh(A[np.ix_(ib, ib)])
        d2 = abs(r["lamR"] - float(evR[0]))
        e = np.zeros(r["n"])
        e[r["jstar"]] = 1.0
        ajj = float(np.linalg.solve(A, e)[r["jstar"]])
        d3 = abs(r["a1212"] - ajj) / abs(ajj)
        d4 = abs((1.0 + r["m_def"]) - ajj) / abs(ajj)
        ok = (d1 <= SPOT_WARD_ABS and d2 <= SPOT_WARD_ABS
              and d3 <= SPOT_WARD and d4 <= SPOT_WARD)
        ok_spot &= ok
        print("    spot kz %-3d h %-4d: |tau_full - dense| %.1e, "
              "|lamR - dense| %.1e, blockinv rel %.1e, woodbury "
              "rel %.1e -> %s"
              % (r["kz"], r["h"], d1, d2, d3, d4,
                 "ok" if ok else "FAIL"))
        del r["E"]
    check("W-C1e SPOT WARDS (factor-Gram spectra + block-inverse"
          " + Woodbury vs dense) on %d shallow rungs" % N_SPOT,
          ok_spot, kill="KW")
    print("\n    THE LADDER (37 truth full-window rungs):")
    print("    %-4s %-4s %-10s %-10s %-11s %-9s %-11s %-9s %s"
          % ("kz", "h", "tau_full", "tau_12", "d_12", "c_h",
             "m_def", "(1-T*)/d12", "lamR/tauf"))
    for r in fullw:
        rat_ext = (r["lamR"] / r["tau_full"]
                   if "lamR" in r else float("nan"))
        print("    %-4d %-4d %-10.3e %-10.3e %-11.3e %-9.1f "
              "%-11.3e %-9.3f %8.1f%s"
              % (r["kz"], r["h"], r["tau_full"], r["tau12"],
                 r["d12"], r["c"], r["m_def"],
                 (1.0 - r["tstar"]) / r["d12"], rat_ext,
                 "   <-- kz-21 artifact" if r["kz"] == KZ_STAR
                 else ""))
    cs = np.array([r["c"] for r in fullw])
    mn, q1, q2, q3, mx = quart_row(cs)
    star = [r for r in fullw if r["kz"] == KZ_STAR]
    c21 = star[0]["c"] if star else float("nan")
    h21 = star[0]["h"] if star else -1
    print("\n    raw c quartiles: min %.1f q25 %.1f med %.1f "
          "q75 %.1f max %.1f" % (mn, q1, q2, q3, mx))
    check("W-C1f REPRODUCTION: q25/med/q75 %.0f/%.0f/%.0f == "
          "%.0f/%.0f/%.0f (rtol %.0e); c(kz%d) %.1f == %.0f at "
          "h == %d"
          % (q1, q2, q3, REF_Q25, REF_MED, REF_Q75, REF_Q_RTOL,
             KZ_STAR, c21, REF_C21, H_STAR),
          abs(q1 / REF_Q25 - 1.0) <= REF_Q_RTOL
          and abs(q2 / REF_MED - 1.0) <= REF_Q_RTOL
          and abs(q3 / REF_Q75 - 1.0) <= REF_Q_RTOL
          and abs(c21 / REF_C21 - 1.0) <= REF_C21_RTOL
          and h21 == H_STAR, kill="KW")
    if KILLS:
        return finish({})

    # ------------------------------------------------------------ C2
    section("C2 -- THE POSITIVITY SOURCE: which identification "
            "exposes the boundedness (SENS = leave-kz-21-out)")
    print("    c > 0 is AUTOMATIC on the PD ladder (d_12 > 0 and"
          " tau > 0: both factors positive); the content is")
    print("    boundedness -- measured below as the variance/"
          "trend of each identification's two pieces.")
    sens = [r for r in fullw if r["kz"] != KZ_STAR]
    lh = np.log([r["h"] for r in sens])
    ld12 = np.array([r["ld12"] for r in sens])
    ld11 = np.array([r["ld11"] for r in sens])
    lt = np.log([r["tau12"] for r in sens])
    lc = np.log([r["c"] for r in sens])
    pieces = (("(i)   det-quotient", ld12, lt + ld11),
              ("(ii)  eig-product ", ld12 - lt, ld11),
              ("(iii) christoffel ", ld12 - ld11, lt))
    print("\n    exposure table (SENS, %d rungs; var = "
          "population variance of the log piece):" % len(sens))
    print("    %-20s %-10s %-10s %-10s %-9s %-9s %s"
          % ("identification", "var N", "var D", "max-var",
             "slope N", "slope D", "corr(N,D)"))
    worst = []
    for name, N, Dv in pieces:
        vN, vD = float(np.var(N)), float(np.var(Dv))
        _, bN = ols_ab(lh, N)
        _, bD = ols_ab(lh, Dv)
        cND = corr(N, Dv)
        worst.append(max(vN, vD))
        print("    %-20s %-10.3f %-10.3f %-10.3f %-+9.3f "
              "%-+9.3f %+.6f" % (name, vN, vD, max(vN, vD),
                                 bN, bD, cND))
    iwin = int(np.argmin(worst))
    winner = WINNER_NAME[iwin]
    print("    var(log c) = %.3f (the shared residual; raw "
          "37-rung var(log c) = %.3f)"
          % (float(np.var(lc)),
             float(np.var(np.log([r["c"] for r in fullw])))))
    check("C2.1 typed WINNER (frozen argmin max-piece-variance):"
          " %s (max-vars %s)"
          % (winner, " / ".join("%.2f" % v for v in worst)),
          True)
    # exterior connection
    ext = [r for r in fullw if "lamR" in r]
    ext_s = [r for r in ext if r["kz"] != KZ_STAR]
    check("C2.2 >= %d rungs carry both c and lamR: %d"
          % (MIN_EXT_RUNGS, len(ext)),
          len(ext) >= MIN_EXT_RUNGS, kill="KW")
    cr_raw = corr(np.log([r["c"] for r in ext]),
                  np.log([r["lamR"] / r["tau_full"]
                          for r in ext]))
    cr_sens = corr(np.log([r["c"] for r in ext_s]),
                   np.log([r["lamR"] / r["tau_full"]
                           for r in ext_s]))
    rat = np.array([r["c"] / (r["lamR"] / r["tau_full"])
                    for r in ext_s])
    rmn, rq1, rq2, rq3, rmx = quart_row(rat)
    lamr_t = [r["lamR"] / r["tau_full"] for r in ext]
    print("\n    THE EXTERIOR CONNECTION (deepcore reserve "
          "lamR/tau_full, range [%.0f, %.0f] on %d rungs):"
          % (min(lamr_t), max(lamr_t), len(ext)))
    print("    corr(log c, log(lamR/tau_full)) = %+.4f raw "
          "(%d) / %+.4f SENS (%d)  <-- the decisive number"
          % (cr_raw, len(ext), cr_sens, len(ext_s)))
    print("    ratio ladder c/(lamR/tau_full) (SENS): min %.3f "
          "q25 %.3f med %.3f q75 %.3f max %.3f"
          % (rmn, rq1, rq2, rq3, rmx))
    ext_coupled = cr_sens >= EXT_CORR_BAR
    b_ext = ("EXTSOURCE-COUPLED(corr=%.3f)" % cr_sens
             if ext_coupled
             else "EXTSOURCE-DECOUPLED(corr=%.3f)" % cr_sens)
    check("C2.3 typed: %s (bar %.2f on the SENS corr)"
          % (b_ext, EXT_CORR_BAR), True)
    print("    reading: c is NOT literally the exterior "
          "Christoffel mass -- the exact (iii) mass is m_def = "
          "v_* K_sigma(y_*)")
    print("    with c tau (1 + m_def) = 1 identically; whether "
          "the 210..2200 exterior reserve SOURCES c's")
    print("    boundedness is exactly the printed correlation, "
          "%s at bar %.2f."
          % ("coupled" if ext_coupled else "decoupled",
             EXT_CORR_BAR))

    # ------------------------------------------------------------ C3
    section("C3 -- THE RATIO THEOREM SHADOW (pairs; kz-21 per "
            "the frozen round-53 sensitivity rule)")
    rows = []
    for ra, rb in zip(truth[:-1], truth[1:]):
        if not (ra.get("full") and rb.get("full")
                and "c" in ra and "c" in rb):
            continue
        rows.append(dict(ha=ra["h"], hb=rb["h"],
                         kza=ra["kz"], kzb=rb["kz"],
                         r12=rb["d12"] / ra["d12"],
                         trat=rb["tau12"] / ra["tau12"],
                         crat=rb["c"] / ra["c"]))
    n_pos = sum(1 for row in rows if row["r12"] > 0.0)
    check("W-C3a pair census %d == %d AND r_12 > 0 on %d/%d "
          "pairs (positive pivot quotients, measured)"
          % (len(rows), REF_N_TRUTH_PAIRS, n_pos, len(rows)),
          len(rows) == REF_N_TRUTH_PAIRS
          and n_pos == len(rows), kill="KW")
    print("\n    the c-ratio ladder (%d pairs):" % len(rows))
    print("    %-14s %-11s %-11s %-9s %s"
          % ("step", "r_12", "tau'/tau", "c'/c", ""))
    for row in rows:
        touch = KZ_STAR in (row["kza"], row["kzb"])
        print("    h %3d->%3d    %-11.3e %-11.3e %-9.4f%s"
              % (row["ha"], row["hb"], row["r12"], row["trat"],
                 row["crat"],
                 "   <-- kz-21 pair (excluded in SENS)"
                 if touch else ""))
    crat_raw = np.array([row["crat"] for row in rows])
    rows_s = [row for row in rows
              if KZ_STAR not in (row["kza"], row["kzb"])]
    crat_s = np.array([row["crat"] for row in rows_s])
    m_raw, M_raw = float(np.min(crat_raw)), float(np.max(crat_raw))
    med_raw = float(np.median(crat_raw))
    m_s, M_s = float(np.min(crat_s)), float(np.max(crat_s))
    med_s = float(np.median(crat_s))
    print("\n    c'/c RAW  (%d pairs): min %.4f med %.4f max "
          "%.4f" % (len(rows), m_raw, med_raw, M_raw))
    print("    c'/c SENS (%d pairs, kz-21 pairs excluded per "
          "round-53 COORDINATE-ARTIFACT): min %.4f med %.4f "
          "max %.4f" % (len(rows_s), m_s, med_s, M_s))
    check("C3.1 SENS pair census == %d (raw numbers stand; the "
          "typed [m, M] is the sensitivity range, said plainly)"
          % REF_N_SENS_PAIRS, len(rows_s) == REF_N_SENS_PAIRS,
          "%d" % len(rows_s), kill="KW")
    print("""
    THE RATIO THEOREM (shape; measured constants in brackets;
    NOTHING here is a proof beyond the deployed rungs):

      IF   (H1) 0 < m <= c_{h+1}/c_h <= M for ALL h
                [MEASURED: SENS [%.4f, %.4f] on %d pairs;
                 RAW [%.4f, %.4f] on %d pairs -- NOT proved;
                 candidate source: the %s coordinate
                 + the exterior reserve lamR >= c_R tau,
                 measured %.0f..%.0f, coupling corr %+.3f]
      AND  (H2) d_{12,h} > 0 for ALL h (positive pivot
                quotients r_12 > 0)
                [MEASURED: %d/%d pairs; by identification (iii)
                 d_12 = 1/(1 + v_* K_sigma) > 0 whenever the
                 DEFLATED functional sigma = mu_+ - nu_- stays
                 PD at degree < h -- which is EXACTLY the wall's
                 own PD premise (lambda_min(I-G) = tau_full):
                 a coordinate change, NOT an independent
                 positivity source -- said honestly]
      THEN tau_{h+1}/tau_h = r_12 / (c_{h+1}/c_h) > 0
                (exact algebra, round-52 factorization), and
                with the certified base (v884/v887, declared
                inputs) tau_h > 0 on the WHOLE ladder.

    HONEST SPLIT: measured -- r_12 > 0 on all pairs, c'/c in
    [m, M], the exterior reserve and its coupling to c; needs
    the theorem -- (H1) and (H2) for ALL h.  The shortest-
    theorem candidate is (H1) in the winner coordinate: a
    two-sided bound on a Christoffel-quotient ratio."""
          % (m_s, M_s, len(rows_s), m_raw, M_raw, len(rows),
             winner, min(lamr_t), max(lamr_t), cr_sens,
             n_pos, len(rows)))
    check("C3.2 theorem shape printed with measured constants",
          True)

    # ------------------------------------------------------------ C
    section("C -- controls: the c/Christoffel machinery must "
            "BREAK off the truth comb")
    sfull = [r for r in smooth if r.get("full") and "CJ" in r]
    for r in sfull:
        A = np.eye(NW) - r["CJ"]
        r["tau12"] = float(np.linalg.eigvalsh(A)[0])
    spairs = []
    for ra, rb in zip(smooth[:-1], smooth[1:]):
        if ra.get("full") and rb.get("full") \
                and "tau12" in ra and "tau12" in rb:
            spairs.append((ra, rb))
    n_cone = sum(1 for ra, _rb in spairs if ra["tau12"] <= 0.0)
    print("  C-S  smooth 12-window: %d pairs, base tau_12 <= 0 "
          "(c = d_12/tau loses its meaning as a positive scale) "
          "on %d/%d" % (len(spairs), n_cone, len(spairs)))
    sneg = [r for r in smooth if r["tau_full"] < 0.0]
    print("       smooth deflated functional: tau_full = "
          "1 - lambda_max(G) < 0 (sigma indefinite -> K_sigma "
          "is NOT a Christoffel")
    print("       function of a PD functional) on %d/%d rungs; "
          "first at h = %s"
          % (len(sneg), len(smooth),
             sneg[0]["h"] if sneg else "n/a"))
    check("C-S smooth world breaks BOTH premises: %d pairs == "
          "%d with cone-exit %d/%d AND sigma indefinite on >= 1"
          " rung (%d)"
          % (len(spairs), REF_N_SMOOTH_PAIRS, n_cone,
             len(spairs), len(sneg)),
          len(spairs) == REF_N_SMOOTH_PAIRS
          and n_cone == len(spairs) and len(sneg) >= 1,
          kill="KW")
    print("  C-E  Epstein/scramble at kz %d:" % CTRL_KZ)
    rr9 = window_of(CTRL_KZ)
    N_E = int(math.floor(math.exp(2.0 * rr9["alpha"]))) + 1
    lamE_ = lambda_eps(N_E)
    nn = np.nonzero(np.abs(lamE_) > 1e-12)[0]
    ok_c = True
    for nmc, kw in (("Epstein",
                     dict(comb=(np.log(nn.astype(float)),
                                2.0 * lamE_[nn]
                                / np.sqrt(nn.astype(float))))),
                    ("scramble", dict(scramble_seed=1))):
        try:
            rc = anatomy(CTRL_KZ, mode="ctrl", **kw)
        except (np.linalg.LinAlgError, AssertionError):
            rc = None
        if not isinstance(rc, dict):
            print("       %-8s: chain dies (%r) -> FIRES (frame "
                  "death)" % (nmc, rc))
            continue
        tau12c = None
        if rc.get("full") and "CJ" in rc:
            tau12c = float(np.linalg.eigvalsh(
                np.eye(NW) - rc["CJ"])[0])
        fired = (rc["negA"] > 0
                 or (tau12c is not None and tau12c <= 0.0))
        ok_c &= fired
        print("       %-8s: neg(A) %d | tau_12 %s -> %s"
              % (nmc, rc["negA"],
                 ("%+.3e" % tau12c) if tau12c is not None
                 else "n/a (window not full)",
                 "FIRES" if fired else "SILENT"))
    check("C-E controls fire (frame death or neg(A) > 0 or "
          "tau_12 <= 0)", ok_c, kill="KW")

    return finish(dict(winner=winner, ext=b_ext, m_s=m_s,
                       M_s=M_s, m_raw=m_raw, M_raw=M_raw,
                       cr=cr_sens))


def finish(labels):
    section("V -- FROZEN VERDICT")
    n_pass = sum(1 for _n, okk in CHECKS if okk)
    n_tot = len(CHECKS)
    if KILLS:
        VERDICT = {"KP": "PIPELINE-BROKEN",
                   "KW": "WARD-BROKEN"}[KILLS[0]]
        print("\n  VERDICT: %s" % VERDICT)
    else:
        VERDICT = ("CHRISTRATIO-MEASURED / %(winner)s / %(ext)s"
                   % labels)
        print("\n  VERDICT: %s" % VERDICT)
        print("  (c'/c SENS [%(m_s).4f, %(M_s).4f], RAW "
              "[%(m_raw).4f, %(M_raw).4f]; exterior coupling "
              "corr %(cr)+.3f)" % labels)
    print("""
  HONEST FRAME (as frozen): the three identifications are exact
  warded algebra on PD rungs; the content is the measured
  exposure of the boundedness, the exterior coupling, and the
  finite [m, M] of the c-ratio.  Identification (iii)'s
  positivity premise is the wall's own PD premise in Christoffel
  coordinates -- a coordinate change, not an independent source.
  The census is FINITE; the ratio bound and the pivot positivity
  are NOT proved beyond the deployed rungs.  NO RH claim.  No
  marker moves.""")
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed"
          % (time.time() - T0, n_tot, n_tot - n_pass))
    return 0 if n_pass == n_tot else 1


if __name__ == "__main__":
    raise SystemExit(main())
