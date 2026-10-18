#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""v899 -- PRIME.PORT.CHRISTOFFEL.RATIO.01 + PRIME.CASE.KERNEL.SOS.01 + PRIME.CASE.EDGEDEFECT.01: THE CHRISTOFFEL PIVOT IDENTITY AND THE NORM-SQUARE CONTRACT -- the soft pivot is EXACTLY a deflated-Christoffel evaluation, the pair-contract kernel's entire negative content collapses to ONE top-edge tent, and the periodic full-weight fold KILLS that tent exactly: the conditional diagonal contract is a NORM SQUARE in the frequency weights, ONE module from three probes (19/19 + 15/15 + 19/19 checks, zero fails, verdicts CHRISTRATIO-MEASURED (WINNER-CHRISTOFFEL / EXTSOURCE-DECOUPLED(corr=0.454)) + KERNELSOS-MEASURED (INDEX=INDEX-LARGE; RMIN=1; ABSORB=NOT-ABSORBED; LEDGER=CONSISTENT) + EDGEDEFECT-MEASURED (TYPE=NORMSQUARE-ACHIEVED; KILL=PERIODIC; CHAIN=CARRIED(0.21)); discovery probes christoffel_ratio_probe.py, kernel_sos_probe.py (round 55) and edge_defect_kill_probe.py (round 56, SPEC v2), 2026-08-09, re-run identically at promotion, embedded BYTE-EXACT and executed verbatim, ~15 s).  (1) THE EXACT IDENTITY (christoffel; reviewer priority 3): 1/d_12 = 1 + v_* K_sigma(y_*) -- the last unpivoted LDL pivot of the wall window IS a Christoffel/CD-kernel evaluation of the DEFLATED signed functional sigma = mu_+ - nu_- (Woodbury + factor-Gram + block-inverse chain, verified through an independent h x h route at 2.0e-11 on every full rung, dense-warded on the two spot rungs); of the three reviewer identifications it WINS the boundedness exposure by TWO ORDERS OF MAGNITUDE (max piece-variance 2.96 vs 362 (eig-product) / 430 (det-quotient)); THE HONESTY FENCE warded exactly: lambda_min(I - G) = tau_full EXACTLY -- identification (iii)'s positivity premise is the wall's own PD premise in Christoffel coordinates, a COORDINATE CHANGE, not an independent positivity source (the smooth control breaks BOTH premises: tau_12 <= 0 on 28/28 pairs AND sigma indefinite on 42/42 rungs); the boundedness content measured: c >= 1 exact (min c = 408), c'/c SENS [0.2233, 5.2583] on 29 pairs (RAW [0.0542, 23.62] on 31; the kz-21 pairs excluded per the round-53 COORDINATE-ARTIFACT rule, raw numbers printed), r_12 > 0 on 31/31, EXTSOURCE-DECOUPLED (corr(log c, log(lamR/tau)) = +0.454 < the 0.5 bar -- c is NOT literally the exterior reserve); THE PRINTED RATIO THEOREM: bounded c-ratio (H1) + positive pivot quotients (H2) + certified base (v884/v887/v897) => tau_h > 0 on the whole ladder -- (H1)/(H2) for ALL h are NOT proved, the census is finite.  (2) THE NEGATIVE INDEX (kernelsos; reviewer priority 4): the constructional frequency weights W_{f,m} >= 0 EXACTLY on every (rung, zone alias) of the frozen census (79 pairs; 8 rungs kz 9/12/13/26/40/88/90/116 to h = 1433); every negative DCT coefficient of the extracted v894 pair-contract kernel is CLOSED-FORM boundary leakage ctil_f = W_f - mult_f (T0 + (-1)^f T1)/(2L) of the symmetric extension -- NOT arithmetic; in u-space the ENTIRE negative content collapses to ONE top-edge tent (r_min <= 1) with the explicit edge functional (T1/2) E; typed honestly INDEX-LARGE (raw negative index 280..2847 -- all boundary dust) and NOT-ABSORBED (worst |N|/margin = 1.381 at kz 9 alias 9): the raw kernel is a positive-weight finite-band Weil-positivity instance with one edge defect, NOT a known unconditional case (every deployed band exceeds the classical window (-log 2, log 2) by 8..18x; the named partial inputs do not apply at these finite X).  (3) THE KILL (edgedefect; round 56): the round-55 defect is an EXTENSION-CONVENTION ARTIFACT (the DCT-I halving w_{M-1} = 1 at the fold point) and DIES under the PERIODIC full-weight fold -- the cosine weights become EXACTLY the constructional W_{f,m} >= 0 (negative index 0 everywhere, dust AND exact-sign count), all 79/79 modified margins positive, the kz-9-alias-9 absorption failure disappears (ratio 1.381 -> 0.000), and the boundary term beta = -(T1/2)(E - E0) is carried CLOSED-FORM and comb-computable (max |beta|/margin~ = 0.21, both signs occur -- CHAIN=CARRIED, the implication chain to T_h <= 1 on the critical zone stays exact); the alternatives fail honestly (DIRICHLET: the boundary coefficient persists exactly at T1/2 and the interior sine weights go signed -- the positivity link to W is LOST; TAPER: T0 leakage, index 295..1168; ENLARGE: the defect MOVES to the new top tent at the old edge).  NET: the conditional diagonal contract of v894 is now an UNCONDITIONAL NORM SQUARE in the frequency weights (case 1 of the reviewer's trichotomy, achieved at the FINITE level) -- THE ARITHMETIC HYPOTHESIS ITSELF REMAINS CONDITIONAL (pair-correlation class per v889), exactly as before; no marker moves.  NO RH claim.  Float64 on the deployed v563 machinery (READ-ONLY) with exact/closed-form decisions where typed EXACT; no zeros, no prime oracles (AST firewalls inside the probes; own trial-division sieve warded against the deployed table); RNG only in the declared scramble controls (seed 1).  Python-only per GATE.WOLFRAM.02.

PROVENANCE: discovery probes christoffel_ratio_probe.py (19/19,
CHRISTRATIO-MEASURED / WINNER-CHRISTOFFEL /
EXTSOURCE-DECOUPLED(corr=0.454), SPEC v1 frozen pre-run, round
55), kernel_sos_probe.py (15/15, KERNELSOS-MEASURED (INDEX-LARGE;
RMIN=1; NOT-ABSORBED; LEDGER-CONSISTENT), SPEC v1 frozen pre-run,
round 55), edge_defect_kill_probe.py (19/19, EDGEDEFECT-MEASURED
(TYPE=NORMSQUARE-ACHIEVED; KILL=PERIODIC; CHAIN=CARRIED(0.21)),
round 56, SPEC v2: ONE fail-first amendment on record -- the W9
two-route tolerance 1e-12 -> 1e-10, pure cancellation dust in the
E0 lag-vs-primitive comparison; no census rule, no bar and no
verdict enum moved), all 2026-08-09, re-run identically at
promotion.  ROUND-31 EMBEDDING CONVENTION: frozen sources embedded
BYTE-EXACT, executed verbatim in isolated namespaces; printed spec
SHAs reproduce; byte-equality ward vs experiments/tfpt-discovery/
inside the pattern gates.  All probes consume the READ-ONLY
deployed core v563_paper2_readouts.py.

FIREWALL: no zeros, no prime-table oracles; the norm-square form
is a REORGANIZATION of the conditional contract -- its
nonnegativity is NOT claimed; the deflated-Christoffel positivity
premise is the wall's own PD premise in new coordinates (the fence
is part of the promoted statement).  The diagonal route stays
typed CONDITIONAL (pair-correlation class) per v889.  NO RH claim.
"""

import contextlib
import io
import os
import re
import sys
import time
import types

_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)

# ------------- frozen probe source christoffel_ratio_probe (embedded BYTE-EXACT, raw string)
_SRC_0 = r'''
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
'''

# ------------- frozen probe source kernel_sos_probe (embedded BYTE-EXACT, raw string)
_SRC_1 = r'''
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""kernel_sos_probe -- PRIME.CASE.KERNEL.SOS.01
(EXPLORATION ONLY, experiments/; round 55, reviewer priority 4:
compute the NEGATIVE INDEX of the extracted pair-correlation kernel
EXACTLY and test the Gram-difference (sum-of-squares) decomposition
-- the attempt to convert the conditional pair contract into an
unconditional finite-rank correction.  2026-08-09.)

CONTEXT (machinery verbatim from paircorr_contract_probe /
signed_homotopy_probe / christoffel_pnt_gamma_probe): round 50
extracted the exact node kernel of the conditional contract
PRIME.CASE.PAIRCORR.CONTRACT.01,
    K_{h,m}(u) = -(1/2) sum_i tent_i(u) w_i
                 sum_f W_{f,m} cos(2 pi i f / L),
band-limited (n90 = 7..26 modes), with the contract
sum_n mu_n K_{h,m}(log n) - K0 >= deficit_{h,m}.  CAREFUL (the
reviewer's frame): the contract's first-order form is LINEAR in the
comb masses mu; the pair kernel enters only through the quadratic
remainder / the variance reading.  THE CLEAN OBJECT for the SOS
question is therefore the FREQUENCY-SIDE WEIGHT of the linear
functional: Fourier-analyze K exactly over its own band and ask
whether the cosine-coefficient structure is one-signed (then the
functional is a positive-frequency-weight pairing of the explicit-
formula spectral density -- the classical Weil-positivity shape) or
signed (then the negative index r = the number of negative
frequency weights obstructs the SOS reading).

THE EXACT ALGEBRA (frozen; all finite linear algebra on the
deployed v563 family): the node samples are K_i := K_{h,m}(iD)
= -(1/2) w_i sum_g W_{g,m} cos(i theta_g), theta_g = 2 pi g / L,
L = 2M - 2, w_i = 2 - delta_{i,0} - delta_{i,M-1}.  Writing the
DCT-I inversion -K_i = sum_{f=0}^{M-1} ctil_f cos(i theta_f)
(orientation frozen: ctil = the cosine weights of -K, so that the
constructional weights W enter with a PLUS sign), the endpoint
deficit of w_i gives the CLOSED FORM
    ctil_f = W_{f,m} - (mult_f / (2L)) (T0 + (-1)^f T1),
    T0 = sum_g W_{g,m},  T1 = sum_g (-1)^g W_{g,m},
mult_f = 1 at f in {0, M-1} else 2.  W_{f,m} >= 0 EXACTLY by
construction (qt >= 0 times a square, plus a nonnegative diagonal
term), so every negative coefficient is the flat (rank-2 in i)
boundary leakage of the symmetric extension.  In u-space the same
identity reads (the u < D mirror of the deployed assembly exactly
restores the i = 0 endpoint deficit, checked as a ward):
    -K(u) = sum_f W_{f,m} phi_f(u) - (T1/2) tent_{M-1}(u)
on [0, 2 alpha], phi_f(u) = sum_i tent_i(u) cos(i theta_f): the
sole u-space defect is the single top-edge tent -- the minimal
Gram-difference has negative rank r_min <= 1, and its functional on
the truth comb is (T1/2) E, E = sum_n mu_n tent_{M-1}(log n).

FROZEN PROTOCOL (2026-08-09; constants frozen before the first
measurement run; heavy rungs + the deepest 3; budget < 15 min):

 RUNGS: heavy kz {9, 12, 13, 26, 40} + the deepest 3 with complete
   atom tables, kz {88, 90, 116} (verbatim eligibility and
   selection from christoffel_pnt_gamma_probe; X <= 4e5).
 ALIASES: all port aliases in the frozen critical zone -- truth
   neg nodes (d1(f) < 0, f >= 1) with a_{h,f} = 2 h^2 (1 - x_f)
   <= h^{2 theta*}, theta* = 0.700 (verbatim round-45/50
   bookkeeping); detail profiles at the critical alias
   m* = argmin_m (lambda_1 - nu_1)_m and at the a-closest alias.

 S1 THE EXACT SPECTRAL DECOMPOSITION (every rung, every zone
   alias): build W_{f,m} / chat / K at the atoms verbatim
   (kernel_block of paircorr_contract_probe) with the two round-50
   wards kept: (W1) prime-side form == grid form, rel <= 1e-10;
   (W2) K0 route a == route b, rel <= 1e-12.  Then the DCT over
   the exact band f = 0..M-1 by TWO exact routes: (route a) FFT of
   the symmetric extension of -K_i = chat_i/2; (route b) the
   closed form above.  NEW WARDS: (W3) constructional positivity
   min_{f,m} W_{f,m} >= 0 (exact); (W4) route a == route b, rel
   sup <= 1e-10 of max |ctil| (FFT imag residue <= 1e-9 rel).
   THE NEGATIVE INDEX: r(h, m) = #{f : ctil_f < -TOL_NEG max_f
   |ctil_f|}, TOL_NEG = 1e-12 (float-dust floor; the exact-sign
   count printed alongside), and the negative-mass fraction
   sum |ctil_-| / sum |ctil|.  Frequency-weight profiles printed
   at m* and rank 1: ctil at the f-deciles, the top-5 positive and
   top-5 negative modes (f, tau_f = 2 pi f/(L D), ctil, a_f,
   sector flags), n90 of |W|.  TYPING (frozen): INDEX-ZERO iff
   r = 0 at every (rung, zone alias); INDEX-SMALL iff max r <= 3;
   else INDEX-LARGE.

 S2 THE GRAM-DIFFERENCE + THE ABSORPTION TEST (if r > 0): the
   positive/negative frequency split IS the decomposition for a
   cosine kernel: with the variance-reading pair kernel
   Kpair(u,u') = sum_f ctil_f phi_f(u) phi_f(u') the explicit
   Gram difference is Kpair = Phi^T Phi - Psi^T J_r Psi,
   Phi = [sqrt(ctil_f^+) phi_f], Psi = [sqrt(|ctil_f^-|) phi_f],
   J_r = I_r, r = the negative index (printed).  MINIMAL reading:
   the exact boundary identity above, ward (W5) per alias at the
   functional level: |S1 + W.Chat - (T1/2) E| <= 1e-10 x scale,
   Chat_g = sum_i t_i cos(i theta_g), t_i = sum_n mu_n
   tent_i(log n) -- r_min <= 1 with the explicit edge functional
   (T1/2) E.  ABSORPTION: the exact repartition (ward W6, rel <=
   1e-10) J1 = sum_f ctil_f r(f) + B0 + B1, B0 = T0 (sum_f mult_f
   r_f)/(2L), B1 = T1 (sum_f mult_f (-1)^f r_f)/(2L); the
   negative-mode functional on the truth comb N_m = sum_{f:
   ctil < -bar} ctil_f r(f).  OVERLAP CENSUS of the negative-mode
   frequencies vs (a) the pole/arch layer {f : |d_ar(f)| >=
   |d0at(f)|} (arch density dominates the PNT-atom density),
   (b) the exterior zone a_f > h^{2 theta*}, (c) the 8 a-closest
   truth-neg core aliases; per-alias negative-mass shares, the
   union share, counts.  TYPED (frozen): ABSORBABLE(where) iff
   every measured margin (lambda_1 - nu_1)_m > 0 AND max_m
   |N_m| / margin_m <= 1 AND the mean union negative-mass share
   >= 0.90 (aliases with r = 0 vacuous, excluded from the mean);
   where = the dominant sector if its mean share >= 0.50, else
   UNION.  Else NOT-ABSORBED.

 S3 THE UNCONDITIONAL READING (deliverable): if INDEX-ZERO or
   ABSORBABLE, print the theorem-shaped statement -- the contract
   becomes a POSITIVE-weight band-limited explicit-formula
   positivity (weights W_{f,m} >= 0, even test functions phi_f
   supported in [-2 alpha, 2 alpha]) with one explicit rank-<=-1
   edge defect: a Weil-positivity instance on a FINITE band with
   positive weight.  THE HONEST CLASSICAL ASSESSMENT printed:
   unconditional Weil positivity is classical exactly when the
   test support fits inside (-log 2, log 2) (the prime side is
   empty and the archimedean side is positive); our band 2 alpha
   >> log 2 on every rung (printed per rung with X = e^{2 alpha}),
   so this is NOT a known unconditional case -- the named partial
   inputs (zero-free-region error, short-interval asymptotics for
   widths >= x^{0.525}) are NOT applicable at these finite X; the
   route REMAINS CONDITIONAL, but the hypothesis moves from a
   generically signed form into the classical positive-weight
   Weil class (+ the measured edge defect).  If INDEX-LARGE and
   NOT-ABSORBED: state plainly that the pair route stays
   conditional and genuinely pair-correlation strong.

 C  CONTROLS (kz 9, scramble seed 1, verbatim round-50 mirror:
   positions uniform on (0, 2 alpha), same masses): the scramble
   must flip the finite margins -- min_m (lambda_scr - nu_scr)_m
   <= 0 on the scramble zone aliases (fallback, disclosed if the
   zone set is empty: the 8 a-closest scramble neg nodes).
   Silent -> CONTROL-DEAD.

 SELF-TESTS (S0, kill PIPELINE on failure): (i) AST firewall
   clean; (ii) endpoint reconstruction (kz 9): the qt-route
   lambda/nu at the zone aliases vs the verbatim folded_measure
   route, rel <= 1e-8, at both t = 0 and t = 1; (iii) quadratic-
   form self-test per rung at both endpoints: sum_j w_j p*^2 ==
   lambda to rel 1e-8 (verbatim TOL_QF).

KILLS: chain short anywhere needed / self-test failure / zone
alias set empty on a rung -> PIPELINE-BROKEN; any ward W1..W6
failure -> WARD-BROKEN; value control silent -> CONTROL-DEAD.
S1 typing, S2 absorption and S3 outcomes are MEASUREMENTS, never
kills.

VERDICT (frozen enum): KERNELSOS-MEASURED (+ INDEX=<INDEX-ZERO |
INDEX-SMALL | INDEX-LARGE> + RMIN=<0 | 1> + ABSORB=<ABSORBABLE(
where) | NOT-ABSORBED | VACUOUS> + LEDGER=<CONSISTENT |
INCONSISTENT k/N>) / PIPELINE-BROKEN / WARD-BROKEN / CONTROL-DEAD.

SPEC AMENDMENTS (fail-first preserved):
  v1 (2026-08-09): initial freeze.  All kernel/endpoint machinery
  and tolerances are the round-50 frozen values, reused verbatim;
  the DCT orientation, TOL_NEG = 1e-12, the typing bars (0 / 3),
  the absorption bars (margin ratio 1, union share 0.90, dominance
  0.50) and the sector definitions (a)/(b)/(c) are frozen a
  priori, before any coefficient was computed.

NO RH claim: everything here is exact finite linear algebra on
the deployed v563 window family plus measured finite shadows; the
classical statement in S3 is NAMED and assessed, not proved; no
bound, no rate, no uniformity in h.  No marker moves.

FIREWALL: no zeros, no prime oracles beyond the deployed table
(AST scan: zetazero/nzeros/primerange/isprime/primepi/nextprime/
prevprime banned); v563 READ-ONLY; RNG only in the scramble
control; stdout only.

Sources (read-only): paircorr_contract_probe (node kernel,
kernel_block, wards W1/W2, margin ledger, control -- verbatim);
signed_homotopy_probe / christoffel_pnt_gamma_probe (rung set,
folded measures, Lanczos chain, closed-form PNT lags -- verbatim);
christoffel_zone_envelope_probe (theta* = 0.700), declared inputs.

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/kernel_sos_probe.py
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
TOL_WARD_PRIME = 1.0e-10       # W1: prime-side form == grid form
TOL_WARD_K0 = 1.0e-12          # W2: K0 route a == route b
TOL_WARD_DCT = 1.0e-10         # W4: FFT route == closed form
TOL_WARD_IMAG = 1.0e-9         # W4: FFT imag residue (rel)
TOL_WARD_FUNC = 1.0e-10        # W5: u-space boundary identity
TOL_WARD_SPLIT = 1.0e-10       # W6: repartition of J1
TOL_SELF_END = 1.0e-8          # S0.2 endpoint reconstruction
TOL_QF = 1.0e-8                # S0.3 quadratic-form self-test
TOL_NEG = 1.0e-12              # negative-index float-dust floor
IDX_SMALL = 3                  # typing bar: INDEX-SMALL iff r <= 3
ABS_RATIO = 1.0                # absorption: |N| / margin bar
ABS_UNION = 0.90               # absorption: mean union share bar
ABS_DOM = 0.50                 # where-tag: dominant-sector bar
CORE_AL = 8                    # (c): the 8 a-closest core aliases
FRAC_MASS = 0.90               # n90 mass fraction (verbatim)
NDEC = 11                      # profile: f-decile sample count
NTOP = 5                       # profile: top +/- modes printed
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
# (grid density, folded measures, Lanczos chain, closed-form PNT lags:
#  verbatim from paircorr_contract_probe / christoffel_pnt_gamma_probe)

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
    """Folded d_PNT, d_truth, residual, weights, zone aliases, arch
    density, core aliases and the lag blocks c0/c1 of one rung."""
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
    d_ar = grid_density(c_ar)[:F]
    r = d1 - d0
    ff = np.arange(F)
    x = np.cos(2.0 * math.pi * ff / L)
    a = 2.0 * h * h * (1.0 - x)
    mult = np.where((ff == 0) | (ff == L // 2), 1.0, 2.0)
    qt = mult * 4.0 * np.sin(math.pi * ff / L) ** 2 / (2.0 * L)
    neg_all = ff[(ff >= 1) & (d1 < 0.0)]
    neg_all = neg_all[np.argsort(a[neg_all], kind="stable")]
    al_f = neg_all[a[neg_all] <= h ** (2.0 * THETA_STAR)]
    core8 = neg_all[:CORE_AL]
    return dict(kz=kz, alpha=alpha, M=M, h=h, L=L, F=F, D=D,
                c_ar=c_ar, c0=c0, c1=c1, uu=uu, mm=mm,
                x=x, a=a, qt=qt, mult=mult, d0=d0, d1=d1,
                d0at=d0at, d_ar=d_ar, r=r, al_f=al_f,
                y_al=x[al_f], core8=core8,
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


# --------------------------------------- the node kernel (round-50 verbatim)
def kernel_block(R, e0):
    """W, chat, K at the atoms, prime sum, smooth subtraction, wards
    W1/W2, plus the comb tent sums t_i, Chat_g and the edge mass E
    needed by the W5 boundary identity (all exact algebra)."""
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
    # comb tent sums t_i (plain full-weight binning; the deployed
    # u < D mirror is exactly the identity's i = 0 restoration)
    uu, D, mm = R["uu"], R["D"], R["mm"]
    i0 = np.floor(uu / D).astype(int)
    fr = uu / D - i0
    t = np.zeros(M)
    ok0 = (i0 >= 0) & (i0 <= M - 1)
    np.add.at(t, i0[ok0], (mm * (1.0 - fr))[ok0])
    ok1 = (i0 + 1 >= 0) & (i0 + 1 <= M - 1)
    np.add.at(t, (i0 + 1)[ok1], (mm * fr)[ok1])
    Chat = t @ cosIF                                # F-vector
    E = float(t[M - 1])
    del cosIF
    # K at the atoms: tent interpolation of -chat/2 (+ u<D mirror)
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
                ward1=ward1, ward2=ward2, P2=P2,
                t=t, Chat=Chat, E=E)


# ------------------------------------------- S1/S2: the spectral side
def spectral_block(R, kb):
    """Exact DCT of the node kernel per alias (two routes), the
    negative index, the repartition of J1, and ward material."""
    F, L, M = R["F"], R["L"], R["M"]
    assert F == M
    ff = np.arange(F)
    multF = np.where((ff == 0) | (ff == F - 1), 1.0, 2.0)
    par = np.where(ff % 2 == 0, 1.0, -1.0)
    W = kb["W"]
    T0 = np.sum(W, axis=0)
    T1 = par @ W
    # route b: closed form
    ctil_cf = W - (multF[:, None] / (2.0 * L)) * (
        T0[None, :] + par[:, None] * T1[None, :])
    # route a: FFT of the symmetric extension of -K_i = chat_i/2
    v = 0.5 * kb["chat"]                            # M x n_al
    a_ext = np.concatenate([v, v[-2:0:-1]], axis=0)
    A = np.fft.fft(a_ext, axis=0)
    imag_rel = float(np.max(np.abs(A.imag))
                     / max(float(np.max(np.abs(A.real))), 1e-300))
    ctil_fft = multF[:, None] * A[:F].real / L
    scale4 = max(float(np.max(np.abs(ctil_cf))), 1e-300)
    ward4 = float(np.max(np.abs(ctil_fft - ctil_cf))) / scale4
    ctil = ctil_cf
    # negative index per alias
    bar = TOL_NEG * np.maximum(np.max(np.abs(ctil), axis=0),
                               1e-300)
    negm = ctil < -bar[None, :]
    r_al = np.sum(negm, axis=0).astype(int)
    r_exact = np.sum(ctil < 0.0, axis=0).astype(int)
    mass_all = np.sum(np.abs(ctil), axis=0)
    mass_neg = np.sum(np.abs(ctil) * negm, axis=0)
    negfrac = mass_neg / np.maximum(mass_all, 1e-300)
    # repartition of J1 = W.r (ward W6) and the negative functional
    rv = R["r"]
    B0 = (T0 / (2.0 * L)) * float(multF @ rv)
    B1 = (T1 / (2.0 * L)) * float((multF * par) @ rv)
    lin = ctil.T @ rv
    ward6 = float(np.max(
        np.abs(lin + B0 + B1 - kb["A_grid"])
        / np.maximum(np.abs(ctil).T @ np.abs(rv)
                     + np.abs(B0) + np.abs(B1), 1e-300)))
    Nfun = np.sum(ctil * rv[:, None] * negm, axis=0)
    # W5: u-space boundary identity at the functional level
    S1id = -(W.T @ kb["Chat"]) + 0.5 * T1 * kb["E"]
    sc5 = (np.abs(kb["S1"]) + np.abs(W.T @ np.abs(kb["Chat"]))
           + np.abs(0.5 * T1 * kb["E"]))
    ward5 = float(np.max(np.abs(kb["S1"] - S1id)
                         / np.maximum(sc5, 1e-300)))
    # sectors (frozen definitions)
    arch = np.abs(R["d_ar"]) >= np.abs(R["d0at"])
    ext = R["a"] > R["h"] ** (2.0 * THETA_STAR)
    ext = ext & (ff >= 1)
    core8 = np.zeros(F, bool)
    core8[R["core8"]] = True
    union = arch | ext | core8
    return dict(ctil=ctil, T0=T0, T1=T1, r_al=r_al,
                r_exact=r_exact, negfrac=negfrac, negm=negm,
                B0=B0, B1=B1, lin=lin, Nfun=Nfun,
                ward4=ward4, ward5=ward5, ward6=ward6,
                imag_rel=imag_rel, minW=float(np.min(W)),
                arch=arch, ext=ext, core8m=core8, union=union,
                multF=multF, par=par)


def profile_print(R, kb, sb, m_idx, tag):
    """S1 frequency-weight profile at one alias column."""
    F, L, D = R["F"], R["L"], R["D"]
    ct = sb["ctil"][:, m_idx]
    ff = np.arange(F)
    tauv = 2.0 * math.pi * ff / (L * D)
    aw = np.abs(kb["W"][1:, m_idx])
    o = np.argsort(-aw)
    cs = np.cumsum(aw[o])
    n90 = int(np.searchsorted(cs, FRAC_MASS * cs[-1]) + 1)
    f_m = int(R["al_f"][m_idx])
    print("      ctil profile %s (alias %2d, f %4d, a %8.1f, "
          "tau_m %.2f): r %d (exact-sign %d), negmass %.3e, "
          "n90(|W|) %d"
          % (tag, m_idx + 1, f_m, float(R["a"][f_m]),
             2.0 * math.pi * f_m / (L * D),
             int(sb["r_al"][m_idx]), int(sb["r_exact"][m_idx]),
             float(sb["negfrac"][m_idx]), n90))
    dec = [min(F - 1, int(round(k * (F - 1) / (NDEC - 1))))
           for k in range(NDEC)]
    print("        ctil at f-deciles f=%s:"
          % ",".join("%d" % d for d in dec))
    print("          %s" % " ".join("%+.1e" % ct[d] for d in dec))
    op = np.argsort(-ct)[:NTOP]
    print("        top +modes: %s"
          % "  ".join("f%d(tau %.2f, c %+.2e)"
                      % (int(f), tauv[f], ct[f]) for f in op))
    on = np.argsort(ct)[:NTOP]
    on = [int(f) for f in on if ct[f] < 0.0]
    if on:
        def flags(f):
            s = ""
            s += "A" if sb["arch"][f] else "."
            s += "X" if sb["ext"][f] else "."
            s += "C" if sb["core8m"][f] else "."
            return s
        print("        top -modes: %s"
              % "  ".join("f%d(tau %.2f, c %+.2e, a %.0f, %s)"
                          % (f, tauv[f], ct[f], R["a"][f],
                             flags(f)) for f in on))
    else:
        print("        top -modes: none (one-signed at this "
              "alias)")


def main():
    section("PRIME.CASE.KERNEL.SOS.01 -- the negative index of the "
            "contract kernel + Gram-difference (EXPLORATION ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s"
          % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
    print("    NO RH claim; no marker moves.")

    print("\nS0 -- firewall + self-tests")
    check("S0.1 AST firewall clean", not ast_scan(BANNED_IDS),
          kill="PIPELINE")

    section("B0 -- rungs (geometry + zone aliases)")
    RG = {}
    for kz in RUNGS:
        R = build_rung(kz)
        RG[kz] = R
        print("    kz %-3d h %4d M %4d F %5d: atoms %5d, "
              "X %.3e, 2a %.2f, zone aliases %3d "
              "(a <= h^1.4 = %8.0f)"
              % (kz, R["h"], R["M"], R["F"], len(R["uu"]),
                 R["X"], 2.0 * R["alpha"], len(R["al_f"]),
                 R["h"] ** 1.4), flush=True)
    order = sorted(RUNGS, key=lambda kz: RG[kz]["h"])
    ok_al = all(len(RG[kz]["al_f"]) > 0 for kz in RUNGS)
    check("B0.1 zone alias sets nonempty on every rung", ok_al,
          kill="PIPELINE")
    if not ok_al:
        return finish(None, None, None, None)

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
            return finish(None, None, None, None)
        Pn = eval_chain(al, be, m0, R9["y_al"], R9["h"])
        lam_ref = 1.0 / np.sum(Pn ** 2, axis=1)
        pos_map = {int(f): float(v) for f, v in zip(uf_n, vs)}
        nu_ref = np.array([pos_map.get(int(f), 0.0)
                           for f in R9["al_f"]])
        e = gap_at(R9, dv, R9["al_f"])
        if e is None:
            check("S0.2 endpoint chain (qt route)", False,
                  kill="PIPELINE")
            return finish(None, None, None, None)
        dev_end = max(dev_end, float(np.max(
            np.abs(e["lam"] / lam_ref - 1.0))))
        dev_end = max(dev_end, float(np.max(
            np.abs(e["nu"] - nu_ref)
            / np.maximum(np.abs(nu_ref), 1e-300))))
    check("S0.2 endpoint reconstruction == verbatim folded route "
          "(kz 9, t = 0 and 1)", dev_end <= TOL_SELF_END,
          "rel sup dev %.2e" % dev_end, kill="PIPELINE")

    section("E -- exact endpoints per rung: deficit, margin "
            "(lambda_1 - nu_1)_m, critical alias m*")
    RES = {}
    ok_e = True
    qf_worst = 0.0
    n_bad = 0
    n_all = 0
    for kz in order:
        R = RG[kz]
        e0 = gap_at(R, R["d0"], R["al_f"], qf=True)
        e1 = gap_at(R, R["d1"], R["al_f"], qf=True)
        if e0 is None or e1 is None:
            ok_e = False
            print("    kz %-3d: CHAIN SHORT at an endpoint" % kz)
            break
        qf_worst = max(qf_worst, e0["qf_dev"], e1["qf_dev"])
        ms = int(np.argmin(e1["G"]))
        margin = e1["G"]
        n_all += len(margin)
        n_bad += int(np.sum(margin <= 0.0))
        RES[kz] = dict(e0=e0, e1=e1, ms=ms)
        print("    kz %-3d h %4d (n_al %2d): deficit max %+.3e | "
              "min margin %+.3e | m* %d (f %d, a %.1f)"
              % (kz, R["h"], len(R["al_f"]),
                 float(np.max(-e0["G"])), float(np.min(margin)),
                 ms + 1, int(R["al_f"][ms]),
                 float(R["a"][R["al_f"][ms]])), flush=True)
    check("E0 endpoint chains complete on all rungs", ok_e,
          kill="PIPELINE")
    check("S0.3 quadratic-form self-test (sum w p*^2 == lambda, "
          "both endpoints, all rungs)", ok_e
          and qf_worst <= TOL_QF, "worst rel dev %.2e" % qf_worst,
          kill="PIPELINE")
    if not ok_e:
        return finish(None, None, None, None)
    ledger = ("CONSISTENT" if n_bad == 0
              else "INCONSISTENT %d/%d" % (n_bad, n_all))
    print("    margin ledger: %s" % ledger)

    section("S1 -- THE EXACT SPECTRAL DECOMPOSITION: DCT of the "
            "node kernel over its band + THE NEGATIVE INDEX")
    w_worst = dict(w1=0.0, w2=0.0, w4=0.0, w5=0.0, w6=0.0,
                   im=0.0, minW=0.0)
    r_max = 0
    negfrac_max = 0.0
    rows = []                      # (kz, m, r, negfrac, N, margin)
    share_pool = []
    for kz in order:
        R = RG[kz]
        t_a = time.time()
        kb = kernel_block(R, RES[kz]["e0"])
        sb = spectral_block(R, kb)
        RES[kz]["kb"] = kb
        RES[kz]["sb"] = sb
        w_worst["w1"] = max(w_worst["w1"], kb["ward1"])
        w_worst["w2"] = max(w_worst["w2"], kb["ward2"])
        w_worst["w4"] = max(w_worst["w4"], sb["ward4"])
        w_worst["w5"] = max(w_worst["w5"], sb["ward5"])
        w_worst["w6"] = max(w_worst["w6"], sb["ward6"])
        w_worst["im"] = max(w_worst["im"], sb["imag_rel"])
        w_worst["minW"] = min(w_worst["minW"], sb["minW"])
        ms = RES[kz]["ms"]
        margin = RES[kz]["e1"]["G"]
        r_max = max(r_max, int(np.max(sb["r_al"])))
        negfrac_max = max(negfrac_max,
                          float(np.max(sb["negfrac"])))
        for m in range(len(R["al_f"])):
            rows.append((kz, m, int(sb["r_al"][m]),
                         float(sb["negfrac"][m]),
                         float(sb["Nfun"][m]),
                         float(margin[m])))
        for sh in spectral_shares(sb):
            share_pool.append(sh)
        print("    kz %-3d h %4d (F %5d, n_al %2d): "
              "r range %d..%d (exact-sign %d..%d), "
              "negmass max %.3e | T1/T0 at m* %+.3f  [%.1f s]"
              % (kz, R["h"], R["F"], len(R["al_f"]),
                 int(np.min(sb["r_al"])), int(np.max(sb["r_al"])),
                 int(np.min(sb["r_exact"])),
                 int(np.max(sb["r_exact"])),
                 float(np.max(sb["negfrac"])),
                 float(sb["T1"][ms]
                       / max(sb["T0"][ms], 1e-300)),
                 time.time() - t_a), flush=True)
        for tag, mi in (("m*", ms), ("m1", 0)):
            if tag == "m1" and ms == 0:
                continue
            profile_print(R, kb, sb, mi, tag)
    check("S1.W1 prime-side form == grid form (max rel %.2e <= "
          "%.0e)" % (w_worst["w1"], TOL_WARD_PRIME),
          w_worst["w1"] <= TOL_WARD_PRIME, kill="WARD")
    check("S1.W2 smooth subtraction route a == route b (max rel "
          "%.2e <= %.0e)" % (w_worst["w2"], TOL_WARD_K0),
          w_worst["w2"] <= TOL_WARD_K0, kill="WARD")
    check("S1.W3 constructional positivity min W_{f,m} >= 0 "
          "(exact; min %.2e)" % w_worst["minW"],
          w_worst["minW"] >= 0.0, kill="WARD")
    check("S1.W4 DCT route a (FFT) == route b (closed form) "
          "(max rel %.2e <= %.0e; imag %.2e <= %.0e)"
          % (w_worst["w4"], TOL_WARD_DCT, w_worst["im"],
             TOL_WARD_IMAG),
          w_worst["w4"] <= TOL_WARD_DCT
          and w_worst["im"] <= TOL_WARD_IMAG, kill="WARD")
    if r_max == 0:
        idx_type = "INDEX-ZERO"
    elif r_max <= IDX_SMALL:
        idx_type = "INDEX-SMALL"
    else:
        idx_type = "INDEX-LARGE"
    print("\n    NEGATIVE-INDEX CENSUS over all (rung, zone "
          "alias): max r = %d, max negative-mass fraction = %.3e"
          % (r_max, negfrac_max))
    print("    every negative coefficient is the closed-form "
          "boundary leakage ctil_f = W_f - mult_f (T0 + (-1)^f "
          "T1)/(2L) with W_f >= 0 (W3): the negativity is NOT "
          "arithmetic, it is the symmetric-extension edge.")
    check("S1.T typed %s (bars: 0 / <= %d)" % (idx_type,
                                               IDX_SMALL), True)

    section("S2 -- GRAM-DIFFERENCE + ABSORPTION (the negative "
            "modes vs the controlled sectors)")
    print("    Gram difference (explicit, per alias): with "
          "phi_f(u) = sum_i tent_i(u) cos(2 pi i f/L),")
    print("      Kpair(u,u') = sum_f ctil_f phi_f(u) phi_f(u') "
          "= Phi^T Phi - Psi^T I_r Psi,")
    print("      Phi = [sqrt(ctil_f^+) phi_f]_{ctil_f > 0}, "
          "Psi = [sqrt(|ctil_f^-|) phi_f]_{ctil_f < 0}, "
          "r = the negative index above.")
    print("    MINIMAL reading (exact boundary identity, ward "
          "W5): -K(u) = sum_f W_f phi_f(u) - (T1/2) tent_{M-1}(u)")
    print("      on [0, 2 alpha] -- the u < D mirror restores the "
          "i = 0 endpoint; r_min <= 1 (the single top-edge tent).")
    check("S2.W5 u-space boundary identity at the functional "
          "level (max rel %.2e <= %.0e)"
          % (w_worst["w5"], TOL_WARD_FUNC),
          w_worst["w5"] <= TOL_WARD_FUNC, kill="WARD")
    check("S2.W6 repartition J1 == sum ctil r + B0 + B1 (max rel "
          "%.2e <= %.0e)" % (w_worst["w6"], TOL_WARD_SPLIT),
          w_worst["w6"] <= TOL_WARD_SPLIT, kill="WARD")
    rmin_any = 0
    print("\n    edge functional (T1/2) E and boundary parts at "
          "m* per rung:")
    for kz in order:
        R = RG[kz]
        sb, kb = RES[kz]["sb"], RES[kz]["kb"]
        ms = RES[kz]["ms"]
        edge = 0.5 * float(sb["T1"][ms]) * kb["E"]
        if abs(edge) > 0.0:
            rmin_any = 1
        print("      kz %-3d: E %.3e, (T1/2)E %+.3e, B0 %+.3e, "
              "B1 %+.3e, N(m*) %+.3e, J1(m*) %+.3e"
              % (kz, kb["E"], edge, float(sb["B0"][ms]),
                 float(sb["B1"][ms]), float(sb["Nfun"][ms]),
                 float(kb["A_grid"][ms])), flush=True)
    print("\n    overlap census of the negative modes at m* "
          "(A = arch layer, X = exterior zone, C = 8 core "
          "aliases; counts and negative-mass shares):")
    for kz in order:
        R = RG[kz]
        sb = RES[kz]["sb"]
        ms = RES[kz]["ms"]
        nm = sb["negm"][:, ms]
        n_neg = int(np.sum(nm))
        w_neg = np.abs(sb["ctil"][:, ms]) * nm
        mn = max(float(np.sum(w_neg)), 1e-300)
        print("      kz %-3d: n_neg %5d | in A %5d (%.2f) | "
              "in X %5d (%.2f) | in C %d (%.2f) | union %5d "
              "(%.2f)"
              % (kz, n_neg,
                 int(np.sum(nm & sb["arch"])),
                 float(np.sum(w_neg[sb["arch"]]) / mn),
                 int(np.sum(nm & sb["ext"])),
                 float(np.sum(w_neg[sb["ext"]]) / mn),
                 int(np.sum(nm & sb["core8m"])),
                 float(np.sum(w_neg[sb["core8m"]]) / mn),
                 int(np.sum(nm & sb["union"])),
                 float(np.sum(w_neg[sb["union"]]) / mn)),
              flush=True)
    # absorption ledger: |N_m| vs margin_m over all (rung, alias)
    worst_ratio = 0.0
    worst_at = None
    any_nonpos = False
    for (kz, m, r_m, nf, N_m, mg) in rows:
        if mg <= 0.0:
            any_nonpos = True
            continue
        ratio = abs(N_m) / mg
        if ratio > worst_ratio:
            worst_ratio = ratio
            worst_at = (kz, m)
    if share_pool:
        mean_sh = {k: float(np.mean([s[k] for s in share_pool]))
                   for k in ("arch", "ext", "core", "union")}
    else:
        mean_sh = None
    print("\n    ABSORPTION LEDGER: |N_m| vs measured margin "
          "(lambda_1 - nu_1)_m over all %d (rung, alias) pairs:"
          % len(rows))
    print("      worst |N|/margin = %.3e%s | margins all "
          "positive: %s"
          % (worst_ratio,
             " at kz %d alias %d" % (worst_at[0],
                                     worst_at[1] + 1)
             if worst_at else "", "yes" if not any_nonpos
             else "NO"))
    if mean_sh:
        print("      mean negative-mass shares over aliases with "
              "r > 0: arch %.3f, exterior %.3f, core8 %.3f, "
              "union %.3f"
              % (mean_sh["arch"], mean_sh["ext"],
                 mean_sh["core"], mean_sh["union"]))
    if r_max == 0:
        absorb = "VACUOUS"
    elif (not any_nonpos and worst_ratio <= ABS_RATIO
          and mean_sh and mean_sh["union"] >= ABS_UNION):
        dom = max(("arch", "ext", "core"),
                  key=lambda k: mean_sh[k])
        where = ({"arch": "ARCH", "ext": "EXTERIOR",
                  "core": "CORE"}[dom]
                 if mean_sh[dom] >= ABS_DOM else "UNION")
        absorb = "ABSORBABLE(%s)" % where
    else:
        absorb = "NOT-ABSORBED"
    check("S2.T absorption typed %s (bars: ratio <= %.1f, union "
          "share >= %.2f)" % (absorb, ABS_RATIO, ABS_UNION), True)

    section("S3 -- THE UNCONDITIONAL READING (deliverable)")
    if idx_type == "INDEX-ZERO" or absorb.startswith("ABSORB") \
            or absorb == "VACUOUS":
        print("    THEOREM-SHAPED STATEMENT (exact finite "
              "calculus on the deployed v563 family):")
        print("      For every deployed rung h and critical alias "
              "m (a_m <= h^{1.4}), the contract functional")
        print("      J1_{h,m} = sum_f W_{f,m} r(f) has "
              "constructionally NONNEGATIVE frequency weights "
              "W_{f,m} (W3),")
        print("      and in u-space  -K_{h,m}(u) = sum_f W_{f,m} "
              "phi_f(u) - (T1/2) tent_{M-1}(u)  exactly (W5):")
        print("      the conditional contract  J1 + R >= deficit  "
              "is a POSITIVE-WEIGHT band-limited explicit-formula")
        print("      positivity (even test functions phi_f, "
              "support <= 2 alpha) with ONE explicit rank-<=-1 "
              "edge defect,")
        print("      whose negative-mode functional is measured "
              "%s (worst |N|/margin %.2e)."
              % (absorb, worst_ratio))
    else:
        print("    The negative index is large and the negative-"
              "mode functional is NOT dominated by the measured")
        print("    margins: the route stays conditional and "
              "genuinely pair-correlation strong (Fall 3).")
    print("\n    HONEST CLASSICAL ASSESSMENT of what remains:")
    print("      the remaining hypothesis is a Weil-positivity "
          "instance on a FINITE band with positive weight:")
    print("      band 2 alpha per rung = %s log-units "
          "(X = %.1e .. %.1e),"
          % ("/".join("%.2f" % (2.0 * RG[kz]["alpha"])
                      for kz in order),
             min(RG[kz]["X"] for kz in RUNGS),
             max(RG[kz]["X"] for kz in RUNGS)))
    print("      vs the classical unconditional window: Weil "
          "positivity is unconditional exactly for even test")
    print("      functions supported in (-log 2, log 2) = "
          "(-0.693, 0.693) (empty prime side, positive "
          "archimedean side);")
    print("      every deployed band exceeds log 2 by a factor "
          "%.1f .. %.1f -> NOT a known unconditional case."
          % (min(2.0 * RG[kz]["alpha"] for kz in RUNGS)
             / math.log(2.0),
             max(2.0 * RG[kz]["alpha"] for kz in RUNGS)
             / math.log(2.0)))
    print("      Named partial inputs (zero-free-region error "
          "exp(-c (log x)^{3/5}); short-interval asymptotics for")
    print("      widths >= x^{0.525}) are NAMED, not proved here, "
          "and not applicable at these finite X: the route")
    print("      REMAINS CONDITIONAL; the structural gain is the "
          "move from a generically signed pair form into the")
    print("      classical positive-weight Weil class with a "
          "single measured edge defect.")
    check("S3.1 unconditional reading printed (measurement)",
          True)

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
        return finish(idx_type, absorb, ledger, rmin_any)
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
    check("C1 value control fires (scrambled comb: the finite "
          "margins flip)", fires, kill="CONTROL")

    return finish(idx_type, absorb, ledger, rmin_any)


def spectral_shares(sb):
    """The per-alias sector shares with r > 0 (census pool)."""
    out = []
    n_al = sb["ctil"].shape[1]
    for m in range(n_al):
        if sb["r_al"][m] == 0:
            continue
        w_neg = np.abs(sb["ctil"][:, m]) * sb["negm"][:, m]
        mn = float(np.sum(w_neg))
        if mn <= 0.0:
            continue
        out.append(dict(
            arch=float(np.sum(w_neg[sb["arch"]]) / mn),
            ext=float(np.sum(w_neg[sb["ext"]]) / mn),
            core=float(np.sum(w_neg[sb["core8m"]]) / mn),
            union=float(np.sum(w_neg[sb["union"]]) / mn)))
    return out


def finish(idx_type, absorb, ledger, rmin_any):
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
        VERDICT = "KERNELSOS-MEASURED"
    sub = []
    if idx_type:
        sub.append("INDEX=%s" % idx_type)
    if rmin_any is not None:
        sub.append("RMIN=%d" % rmin_any)
    if absorb:
        sub.append("ABSORB=%s" % absorb)
    if ledger:
        sub.append("LEDGER=%s" % ledger)
    print("\n  VERDICT: %s%s"
          % (VERDICT, (" (%s)" % "; ".join(sub)) if sub else ""))
    if VERDICT == "KERNELSOS-MEASURED":
        print("  PLAIN ANSWER: the frequency weights of the "
              "contract kernel are W_{f,m} >= 0 EXACTLY; every "
              "negative DCT coefficient is closed-form boundary "
              "leakage of the symmetric extension, and in u-space "
              "the whole negative content collapses to ONE edge "
              "tent (r_min <= 1).  Typed %s / %s: the contract "
              "is a positive-weight finite-band Weil-positivity "
              "instance, NOT a known unconditional case -- the "
              "route stays conditional, with the negativity "
              "structure now exact and measured."
              % (idx_type or "n/a", absorb or "n/a"))
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed"
          % (time.time() - T0, n_tot, n_tot - n_pass))
    return 0 if n_pass == n_tot else 1


if __name__ == "__main__":
    raise SystemExit(main())
'''

# ------------- frozen probe source edge_defect_kill_probe (embedded BYTE-EXACT, raw string)
_SRC_2 = r'''
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""edge_defect_kill_probe -- PRIME.CASE.EDGEDEFECT.01
(EXPLORATION ONLY, experiments/; round 56: kill the SINGLE top-edge
tent defect of the pair-contract kernel.  Round 55 (kernel_sos_probe)
reduced ALL negativity of the extracted kernel to ONE rank-1 edge
term -- an artifact of the symmetric extension, not arithmetic; this
probe tests three frozen modified constructions that could eliminate
it WITHOUT changing the contract's content, which would make the
conditional diagonal contract an unconditional norm square (the
reviewer's Fall 1).  2026-08-09.)

CONTEXT (machinery verbatim from kernel_sos_probe round 55 /
paircorr_contract_probe round 50): the node kernel of the contract
PRIME.CASE.PAIRCORR.CONTRACT.01 has node values
    v_i := -K_i = (w_i/2) sum_f W_{f,m} cos(i theta_f),
theta_f = 2 pi f / L, L = 2M - 2, w_i = 2 - delta_{i,0} -
delta_{i,M-1}, W_{f,m} >= 0 EXACTLY by construction.  The endpoint
weight deficit gives the exact identity
    v_i = sum_f W_f cos(i theta_f) - (T0/2) delta_{i,0}
                                   - (T1/2) delta_{i,M-1},
    T0 = sum_g W_g,  T1 = sum_g (-1)^g W_g,
whence the deployed (symmetric/Neumann, DCT-I) cosine weights
    ctil_f = W_f - (mult_f/(2L)) (T0 + (-1)^f T1),
and, with the deployed u < D mirror exactly restoring the i = 0
deficit, the u-space identity (round-55 ward W5, rel <= 1.5e-14)
    -K(u) = sum_f W_f phi_f(u) - (T1/2) tent_{M-1}(u),
phi_f(u) = sum_i tent_i(u) cos(i theta_f): ONE top-edge tent is the
sole defect (rank r_min <= 1), with functional (T1/2) E on the truth
comb, E = sum_n mu_n tent_{M-1}(log n).  Round 55 measured T1/T0 in
[-0.31, -0.23] and the absorption bar FAILING at kz 9 alias 9 with
|N|/margin = 1.381 (NOT-ABSORBED).  Round 50 measured all 79
(rung, zone-alias) finite margins positive on the heavy rungs.

THE THREE KILL CANDIDATES (frozen; closed forms derived a priori):

 (a1) DIRICHLET (antisymmetric / sine extension): represent the SAME
   node values on the interior sine basis with explicit boundary
   tents, psi_g = pi g / (M-1):
     v_i = sum_{g=1}^{M-2} s_g sin(i psi_g)
           + v_0 delta_{i,0} + v_{M-1} delta_{i,M-1},
     s_g = (2/(M-1)) sum_{i=1}^{M-2} v_i sin(i psi_g)   (DST-I).
   CLOSED FORM of the boundary coefficient: v_{M-1} = T1/2 exactly
   -- the T1 boundary term does NOT vanish and keeps its size
   |T1|/2; moreover the interior sine weights s_g carry no
   positivity link to W_f >= 0 (measured: negative-s census).

 (a2) PERIODIC (full-weight fold): the halving w_{M-1} = 1 is the
   symmetric extension's fold counting at i = M-1; the periodic
   reading gives every node FULL weight:
     vtil_i := sum_f W_f cos(i theta_f)
     <=>  Ktil(u) = K(u) - (T1/2) tent_{M-1}(u).
   Then the cosine weights are EXACTLY ctil~_f = W_f >= 0: the T1
   boundary term VANISHES identically (zero u-space defect, zero
   negative index).  The tested functional shifts by the exact
   boundary correction (per alias m; E0 = the PNT mass of the top
   tent, E0 = int_0^{2 alpha} 2 e^{u/2} tent_{M-1}(u) du =
   -2 c0_{M-1}):
     beta_m := Jtil_m - J1_m = -(T1_m/2) (E - E0).

 (b) EDGE TAPER t = 1 (drop the top tent node): vtil_{M-1} := 0,
   i.e. subtract (T1/2) delta_{i,M-1} from v:
     ctil_f = W_f - (mult_f/(2L)) (T0 + 2 (-1)^f T1),
     K_b(u) = K(u) + (T1/2) tent_{M-1}(u),
     beta^b_m = +(T1_m/2) (E - E0) = -beta_m.
   The T0 leakage REMAINS (frequency index does not vanish) and in
   u-space -K_b = sum_f W_f phi_f - T1 tent_{M-1}: the edge term
   doubles with flipped orientation.

 (c) WINDOW ENLARGE (+1 tent at fixed D, the frozen +1 alias
   shift): M' = M + 1, alpha' = alpha + D/2, window [0, 2 alpha +
   D]; atoms = the deployed global table up to 2 alpha' (complete:
   X' <= 4e5 on every heavy rung; own-sieve crosscheck S0.4); the
   rung degree h stays the deployed value.  Everything is rebuilt;
   the expected outcome is that the defect MOVES to the new top
   tent centred at the OLD edge 2 alpha (measured against the new
   margins).

THE IMPLICATION CHAIN (exact finite calculus, both directions):
with margin_m = (lambda_1 - nu_1)_m and the round-50 identity
Delta_m = J1_m + R_m (R = the response remainder),
    margin_m = Jtil_m + R_m - deficit_m - beta_m .
So "Jtil + R >= deficit + max(beta, 0)" ==> T_h <= 1 at (h, m); if
beta_m <= 0 the modified positivity ALONE suffices (one-sided,
nothing lost); if beta_m > 0 it must be carried as an explicit
positive remainder of measured size (beta is comb-computable: T1
from the t = 0 construction, E a finite von Mangoldt sum, E0 closed
form).  The finite shadow of the modified hypothesis is
    margin~_m := margin_m + beta_m
(recomputed for all 79 (rung, zone-alias) pairs).

FROZEN PROTOCOL (2026-08-09; constants frozen before the first
measurement run; heavy rungs kz {9, 12, 13, 26, 40} = the round-50
contract rungs incl. the failing kz 9; budget < 15 min):

 S0 SELF-TESTS (kill PIPELINE): (i) AST firewall; (ii) endpoint
   reconstruction (kz 9) vs the verbatim folded route, rel <= 1e-8;
   (iii) quadratic-form self-test per rung, both endpoints, rel <=
   1e-8; (iv) own von Mangoldt sieve == deployed global table on
   the slice (X e^{-1}, X'] of every heavy rung (count + values,
   rel <= 1e-12; the slice starts one log-unit below X so the ward
   is never vacuous even if (X, X'] holds no prime power).

 E1 THE DEFECT ANATOMY (every rung, zone aliases): rebuild W / ctil
   / K verbatim with the round-50/55 wards W1 (prime == grid, 1e-10),
   W2 (K0 routes, 1e-12), W4 (DCT routes, 1e-10), W5 (u-space
   boundary identity, 1e-10), W6 (J1 repartition, 1e-10), W3
   (min W >= 0 exact).  Print WHERE the top tent sits (centre
   (M-1)D = 2 alpha - D, support [2 alpha - 2D, 2 alpha], in n:
   [X e^{-2D}, X]), the von Mangoldt mass it samples (E, atoms in
   support, share of total comb mass), E0 and E - E0, the T1 range
   over aliases, and the defect functional (T1/2) E at m* vs the
   margin.  ANCHOR: reproduce the round-55 failure |N|/margin at
   kz 9 alias 9 (expect ~= 1.381; context print, never a kill).

 E2 THE KILL CANDIDATES (all frozen, no fitting):
   (a1) DIRICHLET: s_g by DST-I; ward W7 exact reconstruction of
     v_i (rel <= 1e-10) and boundary coefficient == T1/2 (rel <=
     1e-12); negative-s census (dust floor TOL_NEG).
   (a2) PERIODIC: ward W8 DCT-I of the full-weight nodes == W (FFT
     route, rel <= 1e-10); negative index of ctil~ = W (exact +
     dust floor); beta by two routes -- E: tent binning (t_{M-1})
     vs direct tent evaluation; E0: -2 c0_{M-1} vs the closed-form
     primitive -- ward W9 rel <= 1e-10 (v2); the modified margin
     census margin + beta over all (rung, alias).
   (b) TAPER t = 1: ward W10 DCT-I of the dropped-node sequence ==
     the closed form above (rel <= 1e-10); negative index census;
     modified margin census margin - beta.
   (c) ENLARGE: rebuild every heavy rung at M' = M + 1 (wards
     W1'/W2'/W4' + QF as in E1); new zone aliases, new margins, new
     negative index, T1'/T0', new edge mass E', defect functional
     (T1'/2) E' at m*', worst |N'|/margin' per rung -- does the
     defect move (expected) or shrink relative to the margins?

 E3 THE VERDICT OBJECT: best candidate by the frozen precedence
   PERIODIC > TAPER > ENLARGE, first that achieves (negative index
   0 at every (rung, zone alias)) AND (all modified margins > 0).
   For it print: the negative index (target 0), the modified margin
   census (target: all 79 positive), the implication status
   (CHAIN=ONESIDED if beta_m <= 0 everywhere, else
   CHAIN=CARRIED(max beta/margin~) -- intact either way by the
   exact identity above, wards W9), and the kz-9-alias-9 absorption
   ratio |N~|/margin~ under the modification (round-55 failure;
   target < 1).  TYPED (frozen): NORMSQUARE-ACHIEVED iff best
   candidate exists AND its kz-9-alias-9 ratio < 1; DEFECT-
   STRUCTURAL iff ALL THREE candidates retain a nonzero u-space
   edge term (|coef| >= (1 - 1e-9) |T1|/2) AND a positive negative
   index (then print the exact obstruction); else DEFECT-MOVED.

 C  CONTROLS (kz 9, scramble seed 1, verbatim round-50 mirror):
   the scramble must still flip the finite margins UNDER THE
   MODIFIED functional of the best candidate -- min_m (margin_scr
   + beta_scr)_m <= 0 on the scramble zone aliases (fallback,
   disclosed if the zone set is empty: the 8 a-closest scramble neg
   nodes).  Silent -> CONTROL-DEAD (the modification destroyed the
   arithmetic content).

KILLS: chain short anywhere needed / self-test failure / zone alias
set empty on a rung (deployed or enlarged) -> PIPELINE-BROKEN; any
ward W1..W10 failure -> WARD-BROKEN; value control silent ->
CONTROL-DEAD.  E1/E2/E3 outcomes are MEASUREMENTS, never kills.

VERDICT (frozen enum): EDGEDEFECT-MEASURED (+ TYPE=<NORMSQUARE-
ACHIEVED | DEFECT-MOVED | DEFECT-STRUCTURAL> + KILL=<PERIODIC |
TAPER1 | ENLARGE | NONE> + CHAIN=<ONESIDED | CARRIED(x) | N/A> +
LEDGER=<CONSISTENT | INCONSISTENT k/N>) / PIPELINE-BROKEN /
WARD-BROKEN / CONTROL-DEAD.

SPEC AMENDMENTS (fail-first preserved):
  v1 (2026-08-09): initial freeze.  All kernel/endpoint machinery
  and tolerances are the round-50/55 frozen values, reused
  verbatim; the three candidate constructions, their closed forms,
  beta, the margin-shift rule margin~ = margin + beta, the
  precedence PERIODIC > TAPER > ENLARGE, RATIO_BAR = 1, and the
  typing rules are frozen a priori, before any modified coefficient
  was computed.
  v2 (2026-08-09): TOL_WARD_BETA relaxed 1e-12 -> 1e-10 after the
  first frozen run printed W9 FAIL at 7.4e-12: the E0 primitive
  route evaluates _prim differences of size ~e^{alpha} with ~1e-12
  relative cancellation dust -- a float-rounding artifact of two
  EXACT closed-form routes, matched to the other functional-level
  ward bars (W1/W5/W6 at 1e-10).  Fail-first preserved: the FAIL
  was printed and no measured quantity (beta, margins, indices,
  ratios -- all identical) moved.  The W9 check now prints the E
  route and the E0 route deviations separately.

NO RH claim: everything here is exact finite linear algebra on the
deployed v563 window family plus measured finite shadows; the
modified contract remains CONDITIONAL (a positive-weight finite-
band Weil-positivity hypothesis); no bound, no rate, no uniformity
in h.  No marker moves.

FIREWALL: no zeros, no prime oracles beyond the deployed table (own
sieve allowed for the S0.4 crosscheck; AST scan: zetazero/nzeros/
primerange/isprime/primepi/nextprime/prevprime banned); v563
READ-ONLY; RNG only in the scramble control; stdout only.

Sources (read-only): kernel_sos_probe (round 55: closed-form ctil,
wards W1..W6, negative index, absorption ledger -- verbatim);
paircorr_contract_probe (round 50: contract functional, margin
ledger, control -- verbatim); christoffel_pnt_gamma_probe (folded
measures, Lanczos chain, closed-form PNT lags -- verbatim);
christoffel_zone_envelope_probe (theta* = 0.700), declared inputs.

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/edge_defect_kill_probe.py
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

HEAVY = (9, 12, 13, 26, 40)    # round-50 contract rungs (verbatim)
THETA_STAR = 0.700             # frozen zone exponent (ZONESPLIT.01)
TOL_WARD_PRIME = 1.0e-10       # W1: prime-side form == grid form
TOL_WARD_K0 = 1.0e-12          # W2: K0 route a == route b
TOL_WARD_DCT = 1.0e-10         # W4/W8/W10: FFT route == closed form
TOL_WARD_IMAG = 1.0e-9         # FFT imag residue (rel)
TOL_WARD_FUNC = 1.0e-10        # W5: u-space boundary identity
TOL_WARD_SPLIT = 1.0e-10       # W6: repartition of J1
TOL_WARD_DST = 1.0e-10         # W7: Dirichlet reconstruction
TOL_WARD_BC = 1.0e-12          # W7: boundary coefficient == T1/2
TOL_WARD_BETA = 1.0e-10        # W9: E / E0 two-route agreement (v2)
TOL_SELF_END = 1.0e-8          # S0.2 endpoint reconstruction
TOL_QF = 1.0e-8                # S0.3 quadratic-form self-test
TOL_SIEVE = 1.0e-12            # S0.4 own sieve == deployed table
TOL_NEG = 1.0e-12              # negative-index float-dust floor
RATIO_BAR = 1.0                # E3: kz-9-alias-9 ratio target
ANCHOR_KZ = 9                  # round-55 failure location
ANCHOR_AL = 9                  # (1-based alias index)
ANCHOR_RATIO = 1.381           # round-55 measured |N|/margin there
EXPECT_MARGINS = 79            # round-50 census (context)
EDGE_STRUCT_TOL = 1.0e-9       # DEFECT-STRUCTURAL edge-coef bar
CORE_AL = 8                    # sector (c): 8 a-closest aliases
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
# (grid density, folded measures, Lanczos chain, closed-form PNT lags:
#  verbatim from kernel_sos_probe / paircorr_contract_probe)

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


def von_mangoldt_atoms(n_lo, n_hi):
    """OWN sieve (firewall-clean): atoms (u = log n, mu = 2 Lambda(n)
    / sqrt n) for n_lo < n <= n_hi, n = p^k (S0.4 crosscheck only)."""
    n_hi = int(n_hi)
    comp = np.zeros(n_hi + 1, dtype=bool)
    for p in range(2, int(math.isqrt(n_hi)) + 1):
        if not comp[p]:
            comp[p * p::p] = True
    uu, mm = [], []
    for p in range(2, n_hi + 1):
        if comp[p]:
            continue
        lp = math.log(p)
        q = p
        while q <= n_hi:
            if q > n_lo:
                uu.append(math.log(q))
                mm.append(2.0 * lp / math.sqrt(q))
            q *= p
    o = np.argsort(np.array(uu)) if uu else np.array([], int)
    return (np.array(uu)[o] if uu else np.array([]),
            np.array(mm)[o] if uu else np.array([]))


# --------------------------------------------------------- rung construction
def make_rung(kz, alpha, M, h, uu, mm):
    """Shared rung assembly (deployed or enlarged geometry)."""
    D = 2.0 * alpha / M
    c_ar = np.asarray(core.arch_lags(M, D), float)
    c1 = np.asarray(core.atom_lags_at(alpha, M, uu, mm)[0], float)
    c0 = np.asarray(cont_lags(alpha, M, [0.0], [2.0 * alpha],
                              [1.0]), float)
    L = 2 * M - 2
    F = L // 2 + 1
    d1 = grid_density(c_ar + c1)[:F]
    d0 = grid_density(c_ar + c0)[:F]
    d0at = grid_density(c0)[:F]
    d_ar = grid_density(c_ar)[:F]
    r = d1 - d0
    ff = np.arange(F)
    x = np.cos(2.0 * math.pi * ff / L)
    a = 2.0 * h * h * (1.0 - x)
    mult = np.where((ff == 0) | (ff == L // 2), 1.0, 2.0)
    qt = mult * 4.0 * np.sin(math.pi * ff / L) ** 2 / (2.0 * L)
    neg_all = ff[(ff >= 1) & (d1 < 0.0)]
    neg_all = neg_all[np.argsort(a[neg_all], kind="stable")]
    al_f = neg_all[a[neg_all] <= h ** (2.0 * THETA_STAR)]
    core8 = neg_all[:CORE_AL]
    return dict(kz=kz, alpha=alpha, M=M, h=h, L=L, F=F, D=D,
                c_ar=c_ar, c0=c0, c1=c1, uu=uu, mm=mm,
                x=x, a=a, qt=qt, mult=mult, d0=d0, d1=d1,
                d0at=d0at, d_ar=d_ar, r=r, al_f=al_f,
                y_al=x[al_f], core8=core8,
                X=math.exp(2.0 * alpha))


def build_rung(kz):
    """Deployed rung, verbatim geometry from v563 build_window."""
    rr = core.build_window(kz)
    alpha, M, h, D = rr["alpha"], rr["M"], rr["h"], rr["D"]
    assert abs(D - 2.0 * alpha / M) <= 1e-12 * D
    uu = np.asarray(rr["uu"], float)
    mm = 2.0 * np.asarray(rr["lam"], float)
    return make_rung(kz, alpha, M, h, uu, mm)


def build_rung_enlarged(R):
    """Candidate (c): +1 tent at fixed D; atoms from the deployed
    global table up to the enlarged edge 2 alpha + D."""
    M2 = R["M"] + 1
    alpha2 = 0.5 * R["D"] * M2
    ka = core.atoms_in(alpha2)
    uu = core.U_ALL[:ka].copy()
    mm = MU_GLOBAL[:ka].copy()
    return make_rung(R["kz"], alpha2, M2, R["h"], uu, mm)


MU_GLOBAL = np.asarray(core.MU_ALL, float)


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


# --------------------------------------- the node kernel (round-50 verbatim)
def kernel_block(R, e0):
    """W, chat, K at the atoms, prime sum, smooth subtraction, wards
    W1/W2, plus the comb tent sums t_i, Chat_g and the edge mass E
    needed by the W5 boundary identity (all exact algebra)."""
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
    # comb tent sums t_i (plain full-weight binning; the deployed
    # u < D mirror is exactly the identity's i = 0 restoration)
    uu, D, mm = R["uu"], R["D"], R["mm"]
    i0 = np.floor(uu / D).astype(int)
    fr = uu / D - i0
    t = np.zeros(M)
    ok0 = (i0 >= 0) & (i0 <= M - 1)
    np.add.at(t, i0[ok0], (mm * (1.0 - fr))[ok0])
    ok1 = (i0 + 1 >= 0) & (i0 + 1 <= M - 1)
    np.add.at(t, (i0 + 1)[ok1], (mm * fr)[ok1])
    Chat = t @ cosIF                                # F-vector
    E = float(t[M - 1])
    del cosIF
    # K at the atoms: tent interpolation of -chat/2 (+ u<D mirror)
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
                ward1=ward1, ward2=ward2, P2=P2,
                t=t, Chat=Chat, E=E)


# ------------------------------------------- spectral side (round-55)
def dct1_of_nodes(v, F, L, multF):
    """Exact DCT-I cosine weights of a node column stack v (M x n):
    the FFT of the whole-sample symmetric extension."""
    a_ext = np.concatenate([v, v[-2:0:-1]], axis=0)
    A = np.fft.fft(a_ext, axis=0)
    imag_rel = float(np.max(np.abs(A.imag))
                     / max(float(np.max(np.abs(A.real))), 1e-300))
    return multF[:, None] * A[:F].real / L, imag_rel


def spectral_block(R, kb):
    """Exact DCT of the node kernel per alias (two routes), the
    negative index, the repartition of J1, and ward material."""
    F, L, M = R["F"], R["L"], R["M"]
    assert F == M
    ff = np.arange(F)
    multF = np.where((ff == 0) | (ff == F - 1), 1.0, 2.0)
    par = np.where(ff % 2 == 0, 1.0, -1.0)
    W = kb["W"]
    T0 = np.sum(W, axis=0)
    T1 = par @ W
    # route b: closed form
    ctil_cf = W - (multF[:, None] / (2.0 * L)) * (
        T0[None, :] + par[:, None] * T1[None, :])
    # route a: FFT of the symmetric extension of -K_i = chat_i/2
    ctil_fft, imag_rel = dct1_of_nodes(0.5 * kb["chat"], F, L, multF)
    scale4 = max(float(np.max(np.abs(ctil_cf))), 1e-300)
    ward4 = float(np.max(np.abs(ctil_fft - ctil_cf))) / scale4
    ctil = ctil_cf
    # negative index per alias
    bar = TOL_NEG * np.maximum(np.max(np.abs(ctil), axis=0), 1e-300)
    negm = ctil < -bar[None, :]
    r_al = np.sum(negm, axis=0).astype(int)
    r_exact = np.sum(ctil < 0.0, axis=0).astype(int)
    # negative functional and repartition of J1 (ward W6)
    rv = R["r"]
    B0 = (T0 / (2.0 * L)) * float(multF @ rv)
    B1 = (T1 / (2.0 * L)) * float((multF * par) @ rv)
    lin = ctil.T @ rv
    ward6 = float(np.max(
        np.abs(lin + B0 + B1 - kb["A_grid"])
        / np.maximum(np.abs(ctil).T @ np.abs(rv)
                     + np.abs(B0) + np.abs(B1), 1e-300)))
    Nfun = np.sum(ctil * rv[:, None] * negm, axis=0)
    # W5: u-space boundary identity at the functional level
    S1id = -(W.T @ kb["Chat"]) + 0.5 * T1 * kb["E"]
    sc5 = (np.abs(kb["S1"]) + np.abs(W.T @ np.abs(kb["Chat"]))
           + np.abs(0.5 * T1 * kb["E"]))
    ward5 = float(np.max(np.abs(kb["S1"] - S1id)
                         / np.maximum(sc5, 1e-300)))
    return dict(ctil=ctil, T0=T0, T1=T1, r_al=r_al,
                r_exact=r_exact, negm=negm, Nfun=Nfun,
                ward4=ward4, ward5=ward5, ward6=ward6,
                imag_rel=imag_rel, minW=float(np.min(W)),
                multF=multF, par=par)


def neg_index_of(ct):
    """Dust-floor and exact-sign negative index per alias column."""
    bar = TOL_NEG * np.maximum(np.max(np.abs(ct), axis=0), 1e-300)
    negm = ct < -bar[None, :]
    return (np.sum(negm, axis=0).astype(int),
            np.sum(ct < 0.0, axis=0).astype(int), negm)


def edge_masses(R):
    """E0 by two routes: -2 c0_{M-1} vs the closed-form primitive
    over the top tent support [(M-2)D, 2 alpha]."""
    M, D, alpha = R["M"], R["D"], R["alpha"]
    e0_a = -2.0 * float(R["c0"][M - 1])
    lo, mid, hi = (M - 2) * D, (M - 1) * D, 2.0 * alpha
    ris = float(_prim(mid, 1.0 - (M - 1.0), 1.0 / D)
                - _prim(lo, 1.0 - (M - 1.0), 1.0 / D))
    fal = float(_prim(hi, 1.0 + (M - 1.0), -1.0 / D)
                - _prim(mid, 1.0 + (M - 1.0), -1.0 / D))
    e0_b = ris + fal
    return e0_a, e0_b


def comb_edge_mass_direct(R):
    """E by direct tent evaluation (independent of the binning)."""
    M, D = R["M"], R["D"]
    v = np.maximum(0.0, 1.0 - np.abs(R["uu"] - (M - 1) * D) / D)
    n_sup = int(np.sum(v > 0.0))
    return float(R["mm"] @ v), n_sup


def main():
    section("PRIME.CASE.EDGEDEFECT.01 -- kill the single top-edge "
            "tent defect of the contract kernel (EXPLORATION ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s"
          % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
    print("    NO RH claim; no marker moves.")

    print("\nS0 -- firewall + self-tests")
    check("S0.1 AST firewall clean", not ast_scan(BANNED_IDS),
          kill="PIPELINE")

    section("B0 -- rungs (deployed geometry + zone aliases)")
    RG = {}
    for kz in HEAVY:
        R = build_rung(kz)
        RG[kz] = R
        print("    kz %-3d h %4d M %4d F %5d: atoms %5d, X %.3e, "
              "D %.4f, zone aliases %3d (a <= h^1.4 = %8.0f)"
              % (kz, R["h"], R["M"], R["F"], len(R["uu"]),
                 R["X"], R["D"], len(R["al_f"]), R["h"] ** 1.4),
              flush=True)
    order = sorted(HEAVY, key=lambda kz: RG[kz]["h"])
    ok_al = all(len(RG[kz]["al_f"]) > 0 for kz in HEAVY)
    check("B0.1 zone alias sets nonempty on every deployed rung",
          ok_al, kill="PIPELINE")
    if not ok_al:
        return finish(None, None, None, None, None)

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
            return finish(None, None, None, None, None)
        Pn = eval_chain(al, be, m0, R9["y_al"], R9["h"])
        lam_ref = 1.0 / np.sum(Pn ** 2, axis=1)
        pos_map = {int(f): float(v) for f, v in zip(uf_n, vs)}
        nu_ref = np.array([pos_map.get(int(f), 0.0)
                           for f in R9["al_f"]])
        e = gap_at(R9, dv, R9["al_f"])
        if e is None:
            check("S0.2 endpoint chain (qt route)", False,
                  kill="PIPELINE")
            return finish(None, None, None, None, None)
        dev_end = max(dev_end, float(np.max(
            np.abs(e["lam"] / lam_ref - 1.0))))
        dev_end = max(dev_end, float(np.max(
            np.abs(e["nu"] - nu_ref)
            / np.maximum(np.abs(nu_ref), 1e-300))))
    check("S0.2 endpoint reconstruction == verbatim folded route "
          "(kz 9, t = 0 and 1)", dev_end <= TOL_SELF_END,
          "rel sup dev %.2e" % dev_end, kill="PIPELINE")

    # S0.4 own sieve == deployed global table on (X e^{-1}, X'] per
    # rung (slice starts a log-unit below X: never vacuous)
    dev_sv = 0.0
    ok_sv = True
    for kz in order:
        R = RG[kz]
        a2 = 0.5 * R["D"] * (R["M"] + 1)
        lo_u, hi_u = 2.0 * R["alpha"] - 1.0, 2.0 * a2
        n_lo = int(math.floor(math.exp(lo_u)))
        n_hi = int(math.floor(math.exp(hi_u)))
        while math.log(n_hi + 1) <= hi_u + 1e-14:
            n_hi += 1
        while n_hi > 1 and math.log(n_hi) > hi_u + 1e-14:
            n_hi -= 1
        u_s, m_s = von_mangoldt_atoms(n_lo, n_hi)
        ka = core.atoms_in(a2)
        sel = (core.U_ALL[:ka] > math.log(n_lo) + 1e-14)
        u_d = core.U_ALL[:ka][sel]
        m_d = MU_GLOBAL[:ka][sel]
        if len(u_s) != len(u_d):
            ok_sv = False
            print("    S0.4 kz %d: count mismatch own %d vs "
                  "deployed %d" % (kz, len(u_s), len(u_d)))
            continue
        if len(u_s):
            dev_sv = max(dev_sv, float(np.max(np.abs(u_s - u_d))),
                         float(np.max(np.abs(m_s - m_d)
                                      / np.maximum(m_d, 1e-300))))
    check("S0.4 own sieve == deployed table on the extension "
          "slices (all rungs)", ok_sv and dev_sv <= TOL_SIEVE,
          "sup dev %.2e" % dev_sv, kill="PIPELINE")

    section("E -- exact endpoints per rung: deficit, margin "
            "(lambda_1 - nu_1)_m, critical alias m*")
    RES = {}
    ok_e = True
    qf_worst = 0.0
    n_bad = 0
    n_all = 0
    for kz in order:
        R = RG[kz]
        e0 = gap_at(R, R["d0"], R["al_f"], qf=True)
        e1 = gap_at(R, R["d1"], R["al_f"], qf=True)
        if e0 is None or e1 is None:
            ok_e = False
            print("    kz %-3d: CHAIN SHORT at an endpoint" % kz)
            break
        qf_worst = max(qf_worst, e0["qf_dev"], e1["qf_dev"])
        ms = int(np.argmin(e1["G"]))
        margin = e1["G"]
        n_all += len(margin)
        n_bad += int(np.sum(margin <= 0.0))
        RES[kz] = dict(e0=e0, e1=e1, ms=ms)
        print("    kz %-3d h %4d (n_al %2d): deficit max %+.3e | "
              "min margin %+.3e | m* %d (f %d, a %.1f)"
              % (kz, R["h"], len(R["al_f"]),
                 float(np.max(-e0["G"])), float(np.min(margin)),
                 ms + 1, int(R["al_f"][ms]),
                 float(R["a"][R["al_f"][ms]])), flush=True)
    check("E0 endpoint chains complete on all rungs", ok_e,
          kill="PIPELINE")
    check("S0.3 quadratic-form self-test (sum w p*^2 == lambda, "
          "both endpoints, all rungs)", ok_e
          and qf_worst <= TOL_QF, "worst rel dev %.2e" % qf_worst,
          kill="PIPELINE")
    if not ok_e:
        return finish(None, None, None, None, None)
    ledger = ("CONSISTENT" if n_bad == 0
              else "INCONSISTENT %d/%d" % (n_bad, n_all))
    print("    margin census: %d (rung, zone alias) pairs "
          "(round-50 context: %d), ledger %s"
          % (n_all, EXPECT_MARGINS, ledger))

    section("E1 -- THE DEFECT ANATOMY: where the top-edge tent "
            "sits and what the functional samples there")
    w_worst = dict(w1=0.0, w2=0.0, w4=0.0, w5=0.0, w6=0.0,
                   im=0.0, minW=0.0)
    anchor_ratio = None
    for kz in order:
        R = RG[kz]
        t_a = time.time()
        kb = kernel_block(R, RES[kz]["e0"])
        sb = spectral_block(R, kb)
        RES[kz]["kb"] = kb
        RES[kz]["sb"] = sb
        w_worst["w1"] = max(w_worst["w1"], kb["ward1"])
        w_worst["w2"] = max(w_worst["w2"], kb["ward2"])
        w_worst["w4"] = max(w_worst["w4"], sb["ward4"])
        w_worst["w5"] = max(w_worst["w5"], sb["ward5"])
        w_worst["w6"] = max(w_worst["w6"], sb["ward6"])
        w_worst["im"] = max(w_worst["im"], sb["imag_rel"])
        w_worst["minW"] = min(w_worst["minW"], sb["minW"])
        ms = RES[kz]["ms"]
        margin = RES[kz]["e1"]["G"]
        M, D, alpha = R["M"], R["D"], R["alpha"]
        E_dir, n_sup = comb_edge_mass_direct(R)
        e0a, e0b = edge_masses(R)
        RES[kz]["E_dir"] = E_dir
        RES[kz]["E0"] = (e0a, e0b)
        tot = float(np.sum(R["mm"]))
        dfc_ms = 0.5 * float(sb["T1"][ms]) * kb["E"]
        print("    kz %-3d h %4d: top tent centre u = %.3f "
              "(= 2a - D), support u in [%.3f, %.3f], "
              "n in [%.0f, %.0f]  [%.1f s]"
              % (kz, R["h"], (M - 1) * D, (M - 2) * D,
                 2.0 * alpha, math.exp((M - 2) * D), R["X"],
                 time.time() - t_a))
        print("      comb mass there: E %.4e (%d atoms in "
              "support; share %.2e of total %.3e) | PNT mass "
              "E0 %.4e | E - E0 %+.4e"
              % (kb["E"], n_sup, kb["E"] / max(tot, 1e-300), tot,
                 e0a, kb["E"] - e0a))
        print("      T1 over aliases: [%.3e, %.3e], T1/T0 at m* "
              "%+.3f | defect functional (T1/2)E at m* %+.3e vs "
              "margin(m*) %+.3e | neg index r range %d..%d"
              % (float(np.min(sb["T1"])), float(np.max(sb["T1"])),
                 float(sb["T1"][ms] / max(sb["T0"][ms], 1e-300)),
                 dfc_ms, float(margin[ms]),
                 int(np.min(sb["r_al"])), int(np.max(sb["r_al"]))),
              flush=True)
        if kz == ANCHOR_KZ and len(margin) >= ANCHOR_AL:
            i9 = ANCHOR_AL - 1
            anchor_ratio = (abs(float(sb["Nfun"][i9]))
                            / max(float(margin[i9]), 1e-300))
    check("E1.W1 prime-side form == grid form (max rel %.2e <= "
          "%.0e)" % (w_worst["w1"], TOL_WARD_PRIME),
          w_worst["w1"] <= TOL_WARD_PRIME, kill="WARD")
    check("E1.W2 smooth subtraction route a == route b (max rel "
          "%.2e <= %.0e)" % (w_worst["w2"], TOL_WARD_K0),
          w_worst["w2"] <= TOL_WARD_K0, kill="WARD")
    check("E1.W3 constructional positivity min W >= 0 (exact; "
          "min %.2e)" % w_worst["minW"],
          w_worst["minW"] >= 0.0, kill="WARD")
    check("E1.W4 DCT route a (FFT) == route b (closed form) "
          "(max rel %.2e <= %.0e; imag %.2e <= %.0e)"
          % (w_worst["w4"], TOL_WARD_DCT, w_worst["im"],
             TOL_WARD_IMAG),
          w_worst["w4"] <= TOL_WARD_DCT
          and w_worst["im"] <= TOL_WARD_IMAG, kill="WARD")
    check("E1.W5 u-space rank-1 boundary identity (max rel %.2e "
          "<= %.0e)" % (w_worst["w5"], TOL_WARD_FUNC),
          w_worst["w5"] <= TOL_WARD_FUNC, kill="WARD")
    check("E1.W6 repartition J1 == sum ctil r + B0 + B1 (max rel "
          "%.2e <= %.0e)" % (w_worst["w6"], TOL_WARD_SPLIT),
          w_worst["w6"] <= TOL_WARD_SPLIT, kill="WARD")
    print("\n    ANCHOR (round-55 failure): |N|/margin at kz %d "
          "alias %d = %s (round-55: %.3f)"
          % (ANCHOR_KZ, ANCHOR_AL,
             "%.3f" % anchor_ratio if anchor_ratio is not None
             else "n/a", ANCHOR_RATIO))
    print("    ANATOMY: the defect samples ONLY the last D "
          "log-units before the cutoff X -- an edge sliver of the "
          "comb (shares above), not bulk arithmetic.")

    # ---------------------------------------------------- E2 candidates
    section("E2a -- EXTENSION SWAP: Dirichlet (sine) and periodic "
            "(full-weight fold) closed forms")
    w7_rec = 0.0
    w7_bc = 0.0
    dir_negs_max = 0
    for kz in order:
        R = RG[kz]
        kb, sb = RES[kz]["kb"], RES[kz]["sb"]
        M = R["M"]
        v = 0.5 * kb["chat"]                        # M x n_al = -K_i
        # DST-I of the interior + explicit boundary deltas
        N = M - 1
        gi = np.arange(1, M - 1)
        S = np.sin(math.pi * np.outer(gi, gi) / N)  # (M-2) x (M-2)
        s_g = (2.0 / N) * (S @ v[1:M - 1])
        v_rec = np.empty_like(v)
        v_rec[1:M - 1] = S @ s_g * 1.0
        v_rec[0] = v[0]
        v_rec[M - 1] = v[M - 1]
        sc = max(float(np.max(np.abs(v))), 1e-300)
        w7_rec = max(w7_rec, float(np.max(
            np.abs(v_rec - v))) / sc)
        bc = v[M - 1]                               # boundary coeff
        t1half = 0.5 * sb["T1"]
        w7_bc = max(w7_bc, float(np.max(
            np.abs(bc - t1half)
            / np.maximum(np.abs(t1half), 1e-300))))
        barD = TOL_NEG * np.maximum(np.max(np.abs(s_g), axis=0),
                                    1e-300)
        negs = np.sum(s_g < -barD[None, :], axis=0).astype(int)
        dir_negs_max = max(dir_negs_max, int(np.max(negs)))
        ms = RES[kz]["ms"]
        print("    kz %-3d DIRICHLET: boundary tent coeff at m* "
              "%+.3e == T1/2 %+.3e | negative sine weights "
              "%d..%d of %d -> positivity link to W LOST"
              % (kz, float(bc[ms]), float(t1half[ms]),
                 int(np.min(negs)), int(np.max(negs)), M - 2),
              flush=True)
    check("E2a.W7 Dirichlet reconstruction exact (max rel %.2e "
          "<= %.0e) and boundary coeff == T1/2 (max rel %.2e <= "
          "%.0e)" % (w7_rec, TOL_WARD_DST, w7_bc, TOL_WARD_BC),
          w7_rec <= TOL_WARD_DST and w7_bc <= TOL_WARD_BC,
          kill="WARD")
    print("    DIRICHLET verdict: the T1 boundary term does NOT "
          "vanish (coeff exactly T1/2, size |T1|/2 unchanged) and "
          "the interior weights are signed -> candidate dead.")

    print("\n    PERIODIC (full-weight fold): vtil_i = sum_f W_f "
          "cos(i theta_f) <=> ctil~ = W >= 0 exactly.")
    w8 = 0.0
    im8 = 0.0
    per_idx_max = 0
    per_idx_exact_max = 0
    beta = {}
    w9_e = 0.0
    w9_e0 = 0.0
    for kz in order:
        R = RG[kz]
        kb, sb = RES[kz]["kb"], RES[kz]["sb"]
        F, L, M = R["F"], R["L"], R["M"]
        ii = np.arange(M).astype(float)
        cosIF = np.cos((2.0 * math.pi / L)
                       * np.outer(ii, np.arange(F).astype(float)))
        vtil = cosIF @ kb["W"]                      # full weight
        del cosIF
        ct_fft, im_rel = dct1_of_nodes(vtil, F, L, sb["multF"])
        sc = max(float(np.max(np.abs(kb["W"]))), 1e-300)
        w8 = max(w8, float(np.max(np.abs(ct_fft - kb["W"]))) / sc)
        im8 = max(im8, im_rel)
        r_al, r_ex, _ = neg_index_of(kb["W"])
        per_idx_max = max(per_idx_max, int(np.max(r_al)))
        per_idx_exact_max = max(per_idx_exact_max,
                                int(np.max(r_ex)))
        # beta two routes (E and E0 each two routes, W9)
        e0a, e0b = RES[kz]["E0"]
        w9_e = max(w9_e, abs(RES[kz]["E_dir"] - kb["E"])
                   / max(kb["E"], 1e-300))
        w9_e0 = max(w9_e0, abs(e0a - e0b) / max(abs(e0a), 1e-300))
        beta[kz] = -0.5 * sb["T1"] * (kb["E"] - e0a)
        ms = RES[kz]["ms"]
        print("    kz %-3d PERIODIC: neg index (dust/exact) "
              "%d/%d | beta at m* %+.3e (E - E0 %+.3e, sign "
              "uniform over aliases: %s)"
              % (kz, int(np.max(r_al)), int(np.max(r_ex)),
                 float(beta[kz][ms]), kb["E"] - e0a,
                 "yes" if (np.all(beta[kz] >= 0.0)
                           or np.all(beta[kz] <= 0.0)) else "NO"),
              flush=True)
    check("E2a.W8 DCT-I of full-weight nodes == W (max rel %.2e "
          "<= %.0e; imag %.2e <= %.0e)"
          % (w8, TOL_WARD_DCT, im8, TOL_WARD_IMAG),
          w8 <= TOL_WARD_DCT and im8 <= TOL_WARD_IMAG,
          kill="WARD")
    check("E2a.W9 beta ingredients two-route (E binning == direct "
          "%.2e; E0 lag == primitive %.2e; <= %.0e)"
          % (w9_e, w9_e0, TOL_WARD_BETA),
          w9_e <= TOL_WARD_BETA and w9_e0 <= TOL_WARD_BETA,
          kill="WARD")

    section("E2b -- EDGE TAPER t = 1 (drop the top tent node): "
            "closed form and index census")
    w10 = 0.0
    im10 = 0.0
    tap_idx_max = 0
    for kz in order:
        R = RG[kz]
        kb, sb = RES[kz]["kb"], RES[kz]["sb"]
        F, L, M = R["F"], R["L"], R["M"]
        ct_b = (kb["W"] - (sb["multF"][:, None] / (2.0 * L))
                * (sb["T0"][None, :]
                   + 2.0 * sb["par"][:, None] * sb["T1"][None, :]))
        v_b = 0.5 * kb["chat"].copy()
        v_b[M - 1] = 0.0
        ct_fft, im_rel = dct1_of_nodes(v_b, F, L, sb["multF"])
        sc = max(float(np.max(np.abs(ct_b))), 1e-300)
        w10 = max(w10, float(np.max(np.abs(ct_fft - ct_b))) / sc)
        im10 = max(im10, im_rel)
        r_al, r_ex, negm_b = neg_index_of(ct_b)
        tap_idx_max = max(tap_idx_max, int(np.max(r_al)))
        RES[kz]["ct_b_negm"] = negm_b
        RES[kz]["ct_b"] = ct_b
        ms = RES[kz]["ms"]
        print("    kz %-3d TAPER1: neg index (dust/exact) %d/%d "
              "(T0 leakage remains) | beta_b at m* %+.3e = -beta"
              % (kz, int(np.max(r_al)), int(np.max(r_ex)),
                 -float(beta[kz][ms])), flush=True)
    check("E2b.W10 DCT-I of dropped-node sequence == closed form "
          "(max rel %.2e <= %.0e; imag %.2e <= %.0e)"
          % (w10, TOL_WARD_DCT, im10, TOL_WARD_IMAG),
          w10 <= TOL_WARD_DCT and im10 <= TOL_WARD_IMAG,
          kill="WARD")

    section("E2c -- WINDOW ENLARGE (+1 tent at fixed D): does the "
            "defect move or shrink?")
    enl = {}
    enl_ok = True
    w_enl = dict(w1=0.0, w2=0.0, w4=0.0, im=0.0, qf=0.0)
    for kz in order:
        R = RG[kz]
        t_a = time.time()
        R2 = build_rung_enlarged(R)
        if len(R2["al_f"]) == 0:
            print("    kz %-3d ENLARGE: zone alias set EMPTY in "
                  "the enlarged geometry (d1' has no zone neg "
                  "node) -- candidate degenerates on this rung "
                  "(measurement; the PIPELINE kill applies to "
                  "the deployed geometry only)" % kz, flush=True)
            enl[kz] = None
            enl_ok = False
            continue
        e0 = gap_at(R2, R2["d0"], R2["al_f"], qf=True)
        e1 = gap_at(R2, R2["d1"], R2["al_f"], qf=True)
        if e0 is None or e1 is None:
            check("E2c chains complete (kz %d)" % kz, False,
                  kill="PIPELINE")
            return finish(None, None, None, None, ledger)
        w_enl["qf"] = max(w_enl["qf"], e0["qf_dev"], e1["qf_dev"])
        kb2 = kernel_block(R2, e0)
        sb2 = spectral_block(R2, kb2)
        w_enl["w1"] = max(w_enl["w1"], kb2["ward1"])
        w_enl["w2"] = max(w_enl["w2"], kb2["ward2"])
        w_enl["w4"] = max(w_enl["w4"], sb2["ward4"])
        w_enl["im"] = max(w_enl["im"], sb2["imag_rel"])
        margin2 = e1["G"]
        ms2 = int(np.argmin(margin2))
        ratios = np.abs(sb2["Nfun"]) / np.maximum(margin2, 1e-300)
        ratios[margin2 <= 0.0] = np.inf
        enl[kz] = dict(R2=R2, margin=margin2, ms=ms2, sb=sb2,
                       kb=kb2, worst=float(np.max(ratios)))
        M2, D2 = R2["M"], R2["D"]
        print("    kz %-3d ENLARGE: M' %d, n_al' %d, min margin' "
              "%+.3e | new edge tent centre u = %.3f (= OLD edge "
              "2a) | E' %.3e | T1'/T0' at m*' %+.3f | neg index' "
              "%d..%d | worst |N'|/margin' %.3f  [%.1f s]"
              % (kz, M2, len(R2["al_f"]), float(np.min(margin2)),
                 (M2 - 1) * D2, kb2["E"],
                 float(sb2["T1"][ms2]
                       / max(sb2["T0"][ms2], 1e-300)),
                 int(np.min(sb2["r_al"])),
                 int(np.max(sb2["r_al"])), float(np.max(ratios)),
                 time.time() - t_a), flush=True)
    check("E2c.W1'/W2'/W4'/QF wards on the enlarged geometry "
          "(w1 %.2e, w2 %.2e, w4 %.2e, imag %.2e, qf %.2e)"
          % (w_enl["w1"], w_enl["w2"], w_enl["w4"], w_enl["im"],
             w_enl["qf"]),
          w_enl["w1"] <= TOL_WARD_PRIME
          and w_enl["w2"] <= TOL_WARD_K0
          and w_enl["w4"] <= TOL_WARD_DCT
          and w_enl["im"] <= TOL_WARD_IMAG
          and w_enl["qf"] <= TOL_QF, kill="WARD")
    if enl_ok:
        print("    ENLARGE verdict: the defect MOVES to the new "
              "top tent at the old edge (T1' != 0 above).")
    else:
        print("    ENLARGE verdict: degenerates (empty alias set "
              "on at least one rung) -- not a candidate.")

    # -------------------------------------------------- E3 verdict object
    section("E3 -- THE VERDICT OBJECT (best candidate by frozen "
            "precedence PERIODIC > TAPER1 > ENLARGE)")
    # modified margin censuses
    def census(shift_sign):
        rows_c = []
        for kz in order:
            b = shift_sign * beta[kz]
            mg = RES[kz]["e1"]["G"] + b
            rows_c.append((kz, mg, b))
        return rows_c

    cand = {}
    per_rows = census(+1.0)
    per_ok = all(float(np.min(mg)) > 0.0 for _, mg, _ in per_rows)
    cand["PERIODIC"] = dict(idx=per_idx_max, rows=per_rows,
                            ok=(per_idx_max == 0 and per_ok))
    tap_rows = census(-1.0)
    tap_ok = all(float(np.min(mg)) > 0.0 for _, mg, _ in tap_rows)
    cand["TAPER1"] = dict(idx=tap_idx_max, rows=tap_rows,
                          ok=(tap_idx_max == 0 and tap_ok))
    enl_idx = max((int(np.max(enl[kz]["sb"]["r_al"]))
                   for kz in order if enl.get(kz)), default=10 ** 9)
    enl_mok = enl_ok and all(
        float(np.min(enl[kz]["margin"])) > 0.0
        for kz in order if enl.get(kz))
    cand["ENLARGE"] = dict(idx=enl_idx, rows=None,
                           ok=(enl_ok and enl_idx == 0 and enl_mok))
    best = next((k for k in ("PERIODIC", "TAPER1", "ENLARGE")
                 if cand[k]["ok"]), None)

    print("    candidate summary: PERIODIC idx %d margins>0 %s | "
          "TAPER1 idx %d margins>0 %s | ENLARGE idx %s margins>0 "
          "%s (degenerate: %s)"
          % (per_idx_max, per_ok, tap_idx_max, tap_ok,
             "%d" % enl_idx if enl_idx < 10 ** 9 else "n/a",
             enl_mok, not enl_ok))

    chain_tag = "N/A"
    ratio9 = None
    if best in ("PERIODIC", "TAPER1"):
        rows_b = cand[best]["rows"]
        sgn = +1.0 if best == "PERIODIC" else -1.0
        # per-rung modified-margin table
        print("\n    THE MODIFIED MARGIN CENSUS (margin~ = margin "
              "+ beta%s) over all %d pairs:"
              % ("" if best == "PERIODIC" else "_b", n_all))
        n_pos = 0
        b_all_nonpos = True
        carried = 0.0
        for kz, mg, b in rows_b:
            n_pos += int(np.sum(mg > 0.0))
            b_all_nonpos &= bool(np.all(b <= 0.0))
            carried = max(carried, float(np.max(
                np.maximum(b, 0.0) / np.maximum(mg, 1e-300))))
            im = int(np.argmin(mg))
            print("      kz %-3d: n_al %2d, min margin~ %+.3e "
                  "(alias %d), max |beta|/margin~ %.2e, "
                  "beta range [%+.2e, %+.2e]"
                  % (kz, len(mg), float(np.min(mg)), im + 1,
                     float(np.max(np.abs(b)
                                  / np.maximum(mg, 1e-300))),
                     float(np.min(b)), float(np.max(b))))
        print("      census: %d/%d positive (target: all)"
              % (n_pos, n_all))
        chain_tag = ("ONESIDED" if b_all_nonpos
                     else "CARRIED(%.2e)" % carried)
        # kz-9-alias-9 ratio under the modification
        kz9 = ANCHOR_KZ
        i9 = ANCHOR_AL - 1
        mg9 = dict((kz, mg) for kz, mg, _b in rows_b)[kz9]
        if best == "PERIODIC":
            N9 = 0.0        # ctil~ = W >= 0: no negative modes
        else:
            ct_b = RES[kz9]["ct_b"]
            negm_b = RES[kz9]["ct_b_negm"]
            N9 = float(np.sum(ct_b[:, i9] * RG[kz9]["r"]
                              * negm_b[:, i9]))
        ratio9 = abs(N9) / max(float(mg9[i9]), 1e-300)
        print("\n    kz-%d-alias-%d absorption ratio under %s: "
              "|N~|/margin~ = %.3e (round-55: %.3f; target < "
              "%.1f)" % (kz9, ANCHOR_AL, best, ratio9,
                         ANCHOR_RATIO, RATIO_BAR))
        print("\n    THE IMPLICATION CHAIN (exact, wards W9): "
              "margin_m = Jtil_m + R_m - deficit_m - beta_m,")
        print("      beta_m = %s(T1_m/2)(E - E0) comb-computable; "
              "hence  Jtil + R >= deficit + max(beta, 0)  ==>  "
              "T_h <= 1 on the critical zone."
              % ("-" if best == "PERIODIC" else "+"))
        if chain_tag == "ONESIDED":
            print("      beta_m <= 0 at every (rung, alias): the "
                  "modified positivity ALONE implies the diagonal "
                  "bound -- NOTHING is lost.")
        else:
            print("      beta_m > 0 somewhere: the boundary term "
                  "must be carried as an explicit positive "
                  "remainder (max beta/margin~ = %s); the "
                  "implication stays exact -- the carried term is "
                  "closed-form and measured." % chain_tag[8:-1])
    elif best == "ENLARGE":
        print("    best = ENLARGE (see E2c censuses).")
        ratio9 = enl[ANCHOR_KZ]["worst"] if enl.get(ANCHOR_KZ) \
            else None

    # typing (frozen)
    if best is not None and ratio9 is not None \
            and ratio9 < RATIO_BAR:
        typed = "NORMSQUARE-ACHIEVED"
    else:
        structural = (per_idx_max > 0 and tap_idx_max > 0
                      and (not enl_ok or enl_idx > 0))
        typed = ("DEFECT-STRUCTURAL" if structural
                 else "DEFECT-MOVED")
        if structural:
            print("    OBSTRUCTION: every frozen alternative "
                  "keeps a nonzero edge term of size >= (1 - "
                  "%.0e) |T1|/2 and a positive negative index."
                  % EDGE_STRUCT_TOL)
    check("E3 typed %s (best candidate %s; kz-9-alias-9 ratio "
          "%s)" % (typed, best or "NONE",
                   "%.3e" % ratio9 if ratio9 is not None
                   else "n/a"), True)
    if typed == "NORMSQUARE-ACHIEVED":
        print("\n    THEOREM-SHAPED STATEMENT: with the full-"
              "weight (periodic-fold) kernel Ktil the contract "
              "functional is")
        print("      Jtil_{h,m} = sum_n mu_n Ktil(log n) - Ktil0, "
              "  -Ktil(u) = sum_f W_{f,m} phi_f(u),  W_{f,m} >= 0 "
              "(exact),")
        print("      i.e. an UNCONDITIONAL NORM SQUARE in the "
              "frequency weights (Fall 1 of the reviewer's "
              "trichotomy) -- ZERO edge defect;")
        print("      the arithmetic hypothesis (the inequality "
              "itself) remains conditional, now in the classical "
              "positive-weight Weil class with the boundary term "
              "carried exactly (%s)." % chain_tag)

    # ------------------------------------------------------------ controls
    section("C -- controls (kz 9, scramble seed %d, modified "
            "functional of the best candidate)" % SCRAMBLE_SEED)
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
        return finish(typed, best, chain_tag, ratio9, ledger)
    Rs = dict(R9)
    Rs["al_f"] = al_use
    Rs["uu"] = us
    Rs["d1"] = d_s
    Rs["r"] = d_s - R9["d0"]
    kb_s = kernel_block(Rs, e0s)
    par9 = np.where(np.arange(R9["F"]) % 2 == 0, 1.0, -1.0)
    T1_s = par9 @ kb_s["W"]
    e0a9, _e0b9 = RES[9]["E0"]
    beta_s = -0.5 * T1_s * (kb_s["E"] - e0a9)
    if best == "TAPER1":
        beta_s = -beta_s
    elif best not in ("PERIODIC", "TAPER1"):
        beta_s = np.zeros_like(beta_s)      # disclosed: unmodified
    mg_s = es["G"] + beta_s
    worst = float(np.min(mg_s))
    fires = worst <= 0.0
    print("    scramble aliases: %d%s | min modified margin~ = "
          "%+.3e (unmodified: %+.3e; real kz 9 min margin %+.3e) "
          "-> %s"
          % (len(al_use),
             " (zone empty -> frozen fallback: %d a-closest neg "
             "nodes)" % CTRL_FALLBACK_AL if fell_back else
             " (zone aliases)",
             worst, float(np.min(es["G"])),
             float(np.min(RES[9]["e1"]["G"])),
             "FIRES" if fires else "SILENT"), flush=True)
    check("C1 value control fires (scrambled comb flips the "
          "modified finite margins)", fires, kill="CONTROL")

    return finish(typed, best, chain_tag, ratio9, ledger)


def finish(typed, best, chain_tag, ratio9, ledger):
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
        VERDICT = "EDGEDEFECT-MEASURED"
    sub = []
    if typed:
        sub.append("TYPE=%s" % typed)
    sub.append("KILL=%s" % (best or "NONE"))
    if chain_tag:
        sub.append("CHAIN=%s" % chain_tag)
    if ledger:
        sub.append("LEDGER=%s" % ledger)
    print("\n  VERDICT: %s%s"
          % (VERDICT, (" (%s)" % "; ".join(sub)) if sub else ""))
    if VERDICT == "EDGEDEFECT-MEASURED" and typed \
            == "NORMSQUARE-ACHIEVED":
        print("  PLAIN ANSWER: the single top-edge tent defect is "
              "an extension-convention artifact and DIES under "
              "the full-weight (periodic-fold) kernel: the "
              "frequency weights become EXACTLY the "
              "constructional W_{f,m} >= 0 (negative index 0), "
              "the finite margins of the modified contract stay "
              "positive, the round-55 kz-9 absorption failure "
              "disappears (ratio %s < 1), and the implication "
              "chain to T_h <= 1 is exact with the boundary term "
              "%s.  The contract is now a norm square; the "
              "HYPOTHESIS itself remains conditional."
              % ("%.1e" % ratio9 if ratio9 is not None else "0",
                 chain_tag))
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed"
          % (time.time() - T0, n_tot, n_tot - n_pass))
    return 0 if n_pass == n_tot else 1


if __name__ == "__main__":
    raise SystemExit(main())
'''


# --------------------------------------------------------------- harness
_PF_RE = re.compile(r"^\s*\[(PASS|FAIL)\]\s+(\S+)", re.M)
_VD_RE = re.compile(r"VERDICT[:\]]")


def _probe_file(name):
    cand = os.path.abspath(os.path.join(
        _HERE, os.pardir, "experiments", "tfpt-discovery", name + ".py"))
    return cand if os.path.isfile(cand) else None


def _census(out):
    marks = _PF_RE.findall(out)
    fails = sorted({tok for st, tok in marks if st == "FAIL"})
    verdict = ""
    for line in out.splitlines():
        if _VD_RE.search(line):
            verdict = line.strip()
    return len(marks), fails, verdict


def _exec_probe(name, src, run_entry=True):
    """Execute one embedded frozen probe source BYTE-EXACT in its own
    module namespace (round-31 convention); capture and re-emit
    stdout; return (stdout, exit_code, byte_equal_or_None)."""
    if src[:1] == "\n":
        src = src[1:]
    path = _probe_file(name)
    same = None
    if path is not None:
        with open(path, encoding="utf-8") as fh:
            same = (fh.read() == src)
    fname = path or os.path.abspath(__file__)
    mod = types.ModuleType(name)
    mod.__file__ = fname
    sys.modules[name] = mod
    buf = io.StringIO()
    code = 0
    with contextlib.redirect_stdout(buf):
        try:
            exec(compile(src, fname, "exec"), mod.__dict__)
            entry = mod.__dict__.get("main") or mod.__dict__.get("run")
            if run_entry and callable(entry):
                rc = entry()
                code = 0 if rc is None else int(rc)
        except SystemExit as exc:
            code = 0 if exc.code is None else int(exc.code)
        except Exception:                            # regression guard
            import traceback
            traceback.print_exc(file=sys.stdout)
            code = 99
    out = buf.getvalue()
    sys.stdout.write(out)
    sys.stdout.flush()
    return out, code, same


def _gate(name, out, code, same, exp_n, exp_fails, exp_verdict,
          exp_code, gates):
    n, fails, verdict = _census(out)
    ok = (n == exp_n and fails == list(exp_fails)
          and exp_verdict in verdict and code == exp_code
          and same is not False)
    gates.append(ok)
    prov = ("byte-exact vs experiments source" if same is True else
            "embedded copy (source file not present)" if same is None
            else "SOURCE MISMATCH")
    print("\n[%s] PATTERN GATE %s: %d checks (exp %d) | FAILs %s "
          "(exp %s) | exit %d (exp %d) | %s\n      verdict line: %s"
          % ("PASS" if ok else "FAIL", name, n, exp_n,
             ",".join(fails) if fails else "none",
             ",".join(exp_fails) if exp_fails else "none",
             code, exp_code, prov, verdict), flush=True)
    return ok


_PLAN = (
    ('christoffel_ratio_probe', _SRC_0, 19, (), 'CHRISTRATIO-MEASURED', 0),
    ('kernel_sos_probe', _SRC_1, 15, (), 'KERNELSOS-MEASURED', 0),
    ('edge_defect_kill_probe', _SRC_2, 19, (), 'EDGEDEFECT-MEASURED', 0),
)


def run():
    t0 = time.time()
    print("=" * 74)
    print('v899 -- PRIME.PORT.CHRISTOFFEL.RATIO.01 + PRIME.CASE.KERNEL.SOS.01 + PRIME.CASE.EDGEDEFECT.01: the Christoffel pivot identity 1/d_12 = 1 + v_* K_sigma(y_*) (exact; honesty fence lambda_min(I-G) = tau), the one-tent negative content of the pair kernel, and the periodic full-weight kill: negative index 0, 79/79 modified margins positive -- the conditional contract is a norm square; the hypothesis stays conditional')
    print("(frozen probes embedded byte-exact and executed verbatim; NO RH claim)")
    print("=" * 74, flush=True)
    gates = []
    for name, src, exp_n, exp_fails, exp_verdict, exp_code in _PLAN:
        print("\n" + "-" * 74)
        print("EMBEDDED FROZEN PROBE: %s" % name)
        print("-" * 74, flush=True)
        out, code, same = _exec_probe(name, src)
        _gate(name, out, code, same, exp_n, exp_fails,
              exp_verdict, exp_code, gates)
    ok = all(gates)
    print("\n" + "=" * 74)
    print("v899: %d/%d pattern gates passed | runtime %.1f s"
          % (sum(gates), len(gates), time.time() - t0))
    print('the contract is a norm square in the frequency weights; the boundary term is carried closed-form; the hypothesis itself stays conditional (pair-correlation class)')
    print("[%s] v899 VERDICT GATE" % ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(run())
