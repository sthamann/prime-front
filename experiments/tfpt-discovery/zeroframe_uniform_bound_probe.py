#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""zeroframe_uniform_bound_probe -- PRIME.WALL.ZEROFRAME.UNIFORM.01
(EXPLORATION ONLY, experiments/; 2026-08-11.  THE ALL-H FRONT: turn
the h-flat carrier curve of CXCVII into an analytic architecture --
or map precisely what blocks it.  NO zero-cache expansion.)

THE CONTRACT UNDER ATTACK.  CXCVII (zeroframe_unification_probe,
SPEC dcad3cb2) proved: W2 is EXACTLY the Schur complement of the 7x7
zero-read frame operator F_h on V_h = span{v_h, 6 frame cosines
omega_j = pi j / Lu at the covering cut}; the factor 1 - rho is
positive 75/75; the capacity dimension is FIXED (K*_cap 4/4/5); and
the carrier-only curve c_carr(K=6) = lampen(C_K | N_C)/mu1 =
0.570/1.233/2.223 is FRAME-FLAT (+0.0123 dex/alpha, 2SE 0.0303)
across a full h-decade.  The reduced contract is
  PRIME.WALL.ZEROFRAME.UNIFORM.01: exist K <= 6, c0 > 0 with
  lampen(C_K(h) | N_C(h)) >= c0 mu1(h) for every deployed rung h.
This probe attacks the contract structurally: the carriers sit at
frequencies omega_j <= 5.25 deep inside the zero-free strip
(gamma_1 = 14.134725), only the windows vary with h -- so the
uniform question should decompose into WINDOW ANALYSIS (closed
form, h-asymptotics computable) + a FINITE ARITHMETIC CORE.

WHAT IS MEASURED (typed; kills only where marked WARD).
 (a) ENTRY ASYMPTOTICS -- the continuum closed form.  Every carrier
     block entry is C[a,b] = p_a^T K_h p_b with K_h =
     odd_toeplitz(c_ar + c_at, M); the Hankel lag is EXACTLY
     s_H = 2 alpha - (u_i + u_j) on the midpoint grid.  The D -> 0
     continuum model (derived, then WARDED against the exact
     entries):
       C_cont[a,b] = [ ARCH(G_ab) - (1/2) Sum_j mu_j G_ab(u_j) ]
                     / sqrt(nu_a nu_b),
       G_ab(s) = S_ab(s) - H_ab(s)   (closed trig forms:
       S = both-order cross-correlations of cos(omega_a u),
       cos(omega_b u) on (0, alpha) at shift s; H = the reflected
       Hankel overlap at t = 2 alpha - s; nu_a = alpha/2 +
       sin(2 omega_a alpha)/(4 omega_a)),
       ARCH(G) = -(EULER + LOG_PI) g0 + int_0^{2 alpha}
       [2 g0 e^{-2s} - G(s) e^{-s/2}] / (1 - e^{-2s}) ds
       + g0 |log(1 - e^{-4 alpha})|,   g0 = S_ab(0)/2 - H_ab(0)
     (the Weil archimedean distribution in the deployed w2
     convention, regular at 0 because the discrete w_0 = ac_0
     convention cancels the 1/s singularity).  The h-dependence is
     EXPLICIT: alpha, D, omega only, plus the prime-power comb
     read at closed-form weights -- the mission decomposition.
     WARD: worst relative entry deviation <= CONT_BAR = 5e-2 per
     rung (kill); the relative-error curve vs h and its fitted
     log-log law vs D are REPORTED (the certified-remainder
     surrogate); pencil-bottom tracking |lampen(C_cont|N_cont) -
     lampen(C|N)|/mu1 is reported per rung (the discretization
     price at the bottom).
 (b) THE LIMIT OBJECT -- normalization triad (frozen).
     (N1) Fbar = C/mu1 entrywise: divergence law (fit log10 of the
     median diagonal vs log10 h and vs alpha) -- the honest
     finding anticipated from sizing: NO entrywise limit.
     (N2) the correlation matrix R(h) = D_C^{-1/2} C D_C^{-1/2}
     and the Gram N(h) (unit diagonal by construction): entrywise
     fits y = A + B z with the FROZEN regressor set z in {1/alpha,
     1/sqrt(h), 1/h} (per curve: the regressor with the best R^2,
     declared); R_inf = A-matrix, lampen(R_inf | N_inf) reported
     with the residual scale (the degenerate-limit reading).
     (N3) the bottom curves: c_carr = lampen(C|N)/mu1 == shat *
     cap with cap = lampen(C|N)/m (compression: cap >= 1 free,
     sign-free); FIT + envelope E(z) = |B| z + SAFE max|resid| and
     the crossover z_0 (h_0/alpha_0) where A - E > 0; if the
     envelope cannot certify (scatter), the blocker is typed and
     MAPPED: covariate absorption OLS log10 shat ~ (log10 h,
     kappa = alpha/Lu, log10 nc) with R^2 -- naming how much of
     the band is rung geometry; minimizer-direction drift
     ||x*(h) - x*_ref||_N reported + fitted.
 (c) THE ARITHMETIC SEAT -- three source-side splits per rung
     (anti-circular: all from closed-form lag reads, never from
     eigendata):
     (S1) WINDOW = arch + smooth comb (the deployed smooth world):
     C_win block, lampen(C_win|N_C)/mu1 census (sizing saw
     -2.6e3..-9.6e4: the window alone is HUGELY indefinite);
     C_osc = C - C_win: ||C_osc||_2 curve (sizing: O(1.6) FLAT)
     and the DEMAND law dex(h) = log10(||C_osc||_2 /
     (C0_CAND mu1)) with C0_CAND = 0.570 (the CXCVII candidate
     constant) -- the uniform sharpness the prime reads must
     supply, in CLXXXI currency (combination frequencies
     |omega_a +- omega_b| <= 2 omega_6, all below gamma_1; the
     band is printed per rung with its gamma_1 distance).
     (S2) ZERO COORDINATES at the covering cut (CXCIII machinery
     verbatim inside the CXCVII frame builder, extended to return
     the per-entry pieces): C = E_ar + E_head + E_tcont + E_par
     with E_par = -zs + closed corrections +- TAILB;
     Z = (-zs)-matrix = the pure verified-zero sum (N_Z = 7000
     REUSED, no expansion); CLOSED = C - Z.  Measured:
     ||Z||_2/mu1 law, lampen(CLOSED|N_C)/mu1 census,
     ||TAILB||_2/mu1 law (what the FIXED cache can ever certify at
     the bottom), head-zero anatomy (share of the first N_ANAT =
     30 ordinates in Z, Frobenius), E_head (primes <= nc: the
     finite arithmetic core) norm share.
     Typed: SEAT-PRIME-CARRIED / SEAT-ARCH-CARRIED / SEAT-MIXED by
     the S1 census; Z-PERTURBATIVE / Z-LOADBEARING by whether
     removing Z flips the bottom sign census.
 (d) COMPOSITION -- the honest all-h W2 draft, printed verbatim
     with named gaps: per rung, M_h >= 0 <=> F_h >= 0 (CXCVII
     seat equivalence) and, given C_K > 0, F_h >= 0 <=> the ONE
     scalar seat inequality F00 >= f0^T C_K^{-1} f0 (Schur).  So
     the all-h W2 statement decomposes as [C1: uniform carrier
     bound -- THIS contract, carrier-only, explicit entries] AND
     [C2: the uniform seat inequality, v-seat data,
     DIRECTION-CONDITIONAL].  Every empirical constant is named;
     the composed statement is a CONJECTURE with gaps g1..g5 (fit
     envelope not a theorem; deployed rungs only; prime-carried
     demand; C2 not carrier-reducible -- CXCVII refuted the W1
     minor and the seat stays per-rung data; W1/B-half compose
     separately, T_req curves pending the CXCV lane).
 (e) GATES: predecessor-headline reproduction wards (the ward
     before anything new -- CXCVII numbers verbatim: F00 == m on
     the A1 scale, Schur/det/pivot identities + 1e-8 census 63/75,
     COMPRESS, 1 - rho positive 75/75 + rho med 0.838, c_carr
     band (0.570, 1.233, 2.223) + trend +0.0123, K*_cap (4,4,5) +
     rho-censoring 57/75, SIGN-RESOLVED 0/75, shat band CXLIII,
     heart |PARITH - hat| <= TAILB on every rung x entry); BIT
     ward: the extended frame builder reproduces zf.frame_of
     F/Fz/TB on N_BIT = 6 subset rungs to <= 1e-15; zero-cache
     wards Z1-Z4 verbatim; tau-screens (w2 convention, vs log m)
     on all new margins; controls MUST FIRE (smooth wall < 0 per
     rung; Epstein + scramble break wall AND zero-read heart at
     the declared control cut; off-line impostor gamma_1 -> beta =
     0.75 shifts the (0,0) zero read >= 10x the genuine residual
     -- all CXCVII verbatim, reused).

FROZEN BARS: KMAX = 6; N_Z = 7000; ZETA_TOL = 1e-6; NS_ZETA = 24;
CORR_EPS = 1e-6; ABEL_BAND = (1e-4, 4e-4); N_DEEP = 8 (2 smoke);
KZ_TOP = w2.KZMAX (30 smoke); CTRL_KZ = 9; IMP_BETA = 0.75;
IMP_RATIO_MIN = 10; SCR_MIN = 1; F00_WARD = 1e-10 (CLXXXV W3 / A1
scale); ID_WARD_NUM = 1e-6; ID_CENSUS = 1e-8; COMPRESS_WARD = 1e-6;
MREL_WARD = 1e-10; POL_WARD = 1e-10; ATOM_ID_WARD = 1e-9; RECON_TOL
= 1e-9; SPOT_WARD = 1e-9; BIT_WARD = 1e-15 on N_BIT = 6 geomspaced
subset rungs; CONT_BAR = 5e-2; NS_CONT = 24000; SAFE = 3.0;
TREND_FLAT = 0.05; N_ANAT = 30; C0_CAND = 0.570; reproduction refs
(CXCVII note, full run only): RHO_MED_REF = 0.838 tol 2e-3;
CCARR_REF = (0.570, 1.233, 2.223) tol 2e-3 abs; CCARR_TREND_REF =
+0.0123 tol 1e-3; KCAP_REF = (4, 4, 5) exact; CENSRHO_REF = 57
exact; ID8_REF = 63 exact; SIGNRES_REF = 0 exact; shat SHAT_REF /
SHAT_TOL w2 verbatim; runtime cap declared: 25 min.  Smoke mode
ZUNIF_SMOKE=1: ladder kz <= 30, deep 2, full-only reference wards
deferred (disclosed prints).

PRE-FREEZE SCOUTING DISCLOSURE (2026-08-11, before freezing): TWO
throwaway scratch scripts (deleted) on rungs kz 23/16/52, numbers
SEEN before this spec was frozen: (i) the exact-DST-diagonalization
hypothesis for odd_toeplitz was REFUTED (eigen-residual 0.056..0.15
-- the sine basis does NOT diagonalize the deployed lag class;
the naive full-lag symbol is hugely negative at low k and is NOT
the wall mechanism) -- the symbol route was DROPPED and the
continuum-closed-form route adopted; (ii) carrier-block entries
DIVERGE with depth (C[1,1] = 36.3 -> 135.1 raw) while the pencil
bottom stays mu1-flat -- Fbar = C/mu1 has NO entrywise limit and
the normalization triad above was frozen in response; (iii) the
window-only bottom is hugely negative (lampen(C_win|N)/mu1 =
-2585/-20645/-96026) and ||C_osc||_2 = 1.61/1.55/1.78 ~ O(1)-flat:
SEAT-PRIME-CARRIED is the anticipated verdict and the demand law
~ 2 dex per h-decade is anticipated; (iv) the continuum model hit
rel 1.8e-5..6.6e-3 (kz 23, D = 0.027) and 5e-7..1.1e-6 (kz 52,
D = 0.0058) with the worst entries at the highest combination
frequencies -- CONT_BAR = 5e-2 was set from these numbers with a
~1 dex guard; the D^2 omega^2 error law is anticipated, measured
below.  No success rule, enum or verdict branch was tuned to make
any branch pass: divergence, envelope blockage and prime-carried
seats are first-class typed findings.

SMOKE-RUN DISCLOSURE (2026-08-11, appended after the smokes, full
fail-first history, nothing omitted; ZUNIF_SMOKE=1 = 19-rung
reduced ladder + 2 deep).  SMOKE-1 (v0, exit 1, 15.7 s wall):
ONE ward fail + ONE crash, repaired by three disclosed
amendments, no structural bar, band, enum or success rule moved:
 (i) D1 continuum-model worst PURE-RELATIVE entry deviation
     8.00e-2 > CONT_BAR = 5e-2.  DIAGNOSIS (one deleted
     diagnostic script, disclosed): the worst deviations sit at
     the (6,6) corner on the SHALLOW rungs (kz 23: |C66| = 0.066
     vs block max 36.3, abs error 5.3e-3; kz 9: |C66| = 0.038 vs
     8.1, abs 3.0e-3) -- the highest combination frequency
     2 omega_6 carries the largest D^2 omega^2 tent error AND the
     smallest entry magnitude, so the pure-relative measure
     divides a tiny absolute error by a vanishing scale (exactly
     the CLXXXV amendment-A3 situation).  AMENDMENT A1: the D1
     deviation is measured abs-or-rel against max(|C_ab|,
     SCALE_FLOOR max|C|_block), SCALE_FLOOR = 1e-2; CONT_BAR
     unmoved; the raw pure-relative worst stays REPORTED.
 (ii) crash in the verdict assembly (NameError wst_of_med -- a
     leftover name from a pre-smoke refactor).  AMENDMENT A2:
     bugfix only, v1 label now prints the A1-scale worst +
     median-of-medians.
 (iii) AMENDMENT A3 (typing/prints only, no measured quantity or
     bar moved): the A2/N2 label self-diagnoses
     DEGENERATE-CONSISTENT vs EXTRAPOLATION-NOISY (smoke-1
     measured lampen(R_inf|N_inf) = -30.4 at resid scale 0.45:
     entrywise correlation extrapolation is NOT PSD-consistent at
     smoke scatter -- the label must say so instead of
     'degenerate'); the D3 label diagnoses BOTTOM-NOT-CONTINUUM
     (declared threshold 0.5 mu1) -- smoke-1 measured the
     continuum bottom price at 0.570/1.257/2.011 mu1 == the
     c_carr band itself, i.e. the D -> 0 model does NOT resolve
     the mu1-scale bottom and the floor is carried by the
     DISCRETE grid (a first-class structural finding, typed).
SMOKE-1 measured content (reduced ladder): BIT ward 0.0 exact
6/6; heart 588/588, worst excess -7.66e-04, slack med +2.62 dex;
F00(A1) 2.09e-13; COMPRESS 3.90e-07; 1 - rho positive 21/21 band
2.281e-3/1.689e-1/2.790e-1, rho med 0.8311; c_carr band
0.570/1.262/2.019 trend +0.0328, K*_cap (4,4,5), cens_rho 15/21,
1e-8 census 19/21, sign-res 0; cont-model rung-median band
5.3e-7/1.7e-4/1.7e-3, D-law slope +3.90 (R^2 0.86; +3.67 on the
A1 scale in smoke-2); continuum bottom price 0.570/1.257/2.011
mu1 (BOTTOM-NOT-CONTINUUM); diag divergence +1.58 /log10 h |
+0.608 dex/alpha (R^2 1.00), diag band 0.1/0.4/77.6; R/N
entrywise med resid 1.7e-1/4.3e-2, lampen(R_inf|N_inf) = -30.4
at resid scale 0.45 (EXTRAPOLATION-NOISY); c_carr fit A = 1.681
- 116.7/h (R^2 0.43, resmax 0.525) -> CROSSOVER z_0 = 9.07e-4
(h_0 ~ 1102 on the smoke ladder); cap band 1.002/1.144/1.319,
fit A = 1.268 - 0.478/alpha; covariate R^2 shat 0.56 / c_carr
0.61 / cap 0.42; minimizer drift band 0.000/0.216/0.646;
combination band 3.57/6.91/10.04, min gamma_1 distance 4.09;
SEAT-PRIME-CARRIED (window bottom -1.0e6/-1.0e4/-2.3e3 mu1,
negative 21/21; ||C_osc||_2 1.33/1.61/1.89, slope +0.028
dex/alpha; demand 3.76/4.41/6.41 dex, slope +0.625 dex/alpha);
Z-LOADBEARING (flips 21/21; ||Z||_2/mu1 5.4e1/3.7e2/3.0e4;
lampen((C-Z)|N)/mu1 band -4560/-94.2/-13.5); TAILB/mu1
7.1e1/2.5e2/1.6e4, slope +0.508; head-30 share 0.84/0.95/1.31;
E_head share 0.011/0.131/0.360; controls fire (Epstein/scramble
wall + heart 28/28 each, worst 6.0e2/1.7e3 x TAILB, impostor
6.8e+03 x); screens c_carr PASS(-0.086), cap PASS(-0.017), diag
AMBIG(-0.899), ||C_osc|| PASS(-0.042), Z/mu1 AMBIG(-0.923),
cont-err RELOC(+1.737 -- the D-law seen through the h-m
correlation, declared expected).
SMOKE-2 (v0 + A1/A2/A3, expected green): the confirmation pass;
its numbers must be identical to SMOKE-1 on every quantity the
amendments do not touch.  No bar, band, count, rule or enum moved
after SMOKE-2.

HONEST SCOPE + NO-GO (stated once, repeated in the verdict): every
statement is per-rung on the deployed ladder; the v-seat is a
MEASURED direction (DIRECTION-CONDITIONAL, enters only the
reproduction wards, the Schur/seat curve and the composed draft,
never the carrier analysis); the deep block is FLOAT-LEVEL; fits
and envelopes are EMPIRICAL laws, not theorems; a finite verified
zero sum can never prove RH; the composed all-h statement is a
CONJECTURE with named gaps.  NO RH claim.  No marker moves, no
promotion, no ledger row, stdout only, no edits outside
experiments/.

FIREWALL: AST scan (banned ids zetazero / nzeros / primerange /
isprime / primepi / nextprime / prevprime); v563 READ-ONLY; RNG
only in the declared scramble control (seed 1, inside w2); the
verified cache enters ONLY the zero side of the explicit-formula
ward, the Z/TAILB seat measurement and the impostor control, never
any construction or bound.  PEDIGREE (EXTERNAL-CITED): gamma_1 =
14.134725 (first Riemann ordinate; Titchmarsh / verified cache
head); T0 = 3e12 (Platt-Trudgian 2021); Rosser 1941 N(T) corridor;
Buethe 2018; B_PSI; the classical zero-free region (de la Vallee
Poussin 1896) cited as the tail-side theorem class behind the
zero-free strip below gamma_1 -- constants exactly as in
CLXXXIV/CLXXXIX/CXCIII/CXCVII.

Sources (read-only, SPEC-SHA prefix-warded): zeroframe_unification
_probe (CXCVII, dcad3cb2 -- THE predecessor, frame builder +
minors reused verbatim), w2_pairing_structure_probe (CLXXXV,
8db29e6e), w2_verified_supply_consumption_probe (CXCIII,
921140fa), subgamma_fourier_bound_probe (c7d8810c),
deep_blind_holdout_probe (ext tables), v563_paper2_readouts
(core).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/zeroframe_uniform_bound_probe.py
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

import v563_paper2_readouts as core  # noqa: E402  (READ-ONLY)
import w2_pairing_structure_probe as w2  # noqa: E402  (READ-ONLY)
import subgamma_fourier_bound_probe as subg  # noqa: E402 (READ-ONLY)
import deep_blind_holdout_probe as deep  # noqa: E402  (READ-ONLY)
import lowfreq_discrepancy_gain_probe as lf  # noqa: E402 (READ-ONLY)
import w2_verified_supply_consumption_probe as cxc  # noqa: E402
import zeroframe_unification_probe as zf  # noqa: E402 (READ-ONLY)

SMOKE = os.environ.get("ZUNIF_SMOKE", "") == "1"

PREFIXES = dict(zf="dcad3cb2", w2="8db29e6e", cxc="921140fa",
                subgamma="c7d8810c")

ZC_NPY = os.path.join(_HERE, "verified_zeros_n7000.npy")
N_Z = 7000
ZETA_TOL = 1.0e-6
NS_ZETA = 24
CORR_EPS = 1.0e-6
ABEL_BAND = (1.0e-4, 4.0e-4)

KMAX = 6
CTRL_KZ = 9
IMP_BETA = 0.75
IMP_RATIO_MIN = 10.0
SCR_MIN = 1
F00_WARD = 1.0e-10
ID_WARD_NUM = 1.0e-6
ID_CENSUS = 1.0e-8
COMPRESS_WARD = 1.0e-6
MREL_WARD = 1.0e-10
POL_WARD = 1.0e-10
ATOM_ID_WARD = 1.0e-9
RECON_TOL = 1.0e-9
SPOT_WARD = 1.0e-9
BIT_WARD = 1.0e-15
N_BIT = 6
CONT_BAR = 5.0e-2
SCALE_FLOOR = 1.0e-2
NS_CONT = 24000
SAFE = 3.0
TREND_FLAT = 0.05
N_ANAT = 30
C0_CAND = 0.570
RHO_MED_REF, RHO_MED_TOL = 0.838, 2.0e-3
CCARR_REF, CCARR_TOL = (0.570, 1.233, 2.223), 2.0e-3
CCARR_TREND_REF, CCARR_TREND_TOL = 0.0123, 1.0e-3
KCAP_REF = (4, 4, 5)
CENSRHO_REF = 57
ID8_REF = 63
SIGNRES_REF = 0
N_DEEP = 2 if SMOKE else 8
KZ_TOP = 30 if SMOKE else w2.KZMAX
BANNED_IDS = ("zetazero", "nzeros", "primerange", "isprime",
              "primepi", "nextprime", "prevprime")
EULER = 0.5772156649015328606
LOG_PI = math.log(math.pi)

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


def ast_scan():
    src = open(os.path.abspath(__file__), encoding="utf-8").read()
    tree = ast.parse(src)
    bad = []
    for node in ast.walk(tree):
        name = None
        if isinstance(node, ast.Name):
            name = node.id
        elif isinstance(node, ast.Attribute):
            name = node.attr
        if name and name.lower() in BANNED_IDS:
            bad.append(name)
    return bad


def band(v):
    v = np.asarray(v, float)
    return float(np.min(v)), float(np.median(v)), float(np.max(v))


# ------------------------------------------------------------------
# THE EXTENDED FRAME BUILDER: zf.frame_of verbatim (same op order,
# BIT-warded against the original on a subset) + per-entry split
# pieces (E_ar/E_head/E_tcont/E_par/E_parhat, the pure zero-sum
# matrix Z with head-anatomy, TAILB matrix) + the window/osc blocks
# from the smooth comb (source-side closed lags, no eigendata).
# ------------------------------------------------------------------
def frame_split_of(r, gam, s2t, inv2, inv3, do_spot=False,
                   nc_override=None):
    if nc_override is None and r["ncB"] <= 0:
        return None
    h, M, D = r["h"], r["M"], r["D"]
    alpha, uu, mu = r["alpha"], r["uu"], r["mu"]
    nc = int(nc_override) if nc_override is not None \
        else int(r["ncB"])
    Ng = r["Ng"]
    if nc < 2 or nc >= Ng - 1:
        return None
    u0 = math.log(nc + 1.0)
    uL = math.log(float(Ng))
    Lu = uL - u0
    c_at = np.asarray(core.atom_lags_at(alpha, M, uu, mu)[0], float)
    c_ar = np.asarray(core.arch_lags(M, D), float)
    Kt = core.odd_toeplitz(c_ar + c_at, M)
    ev, V = np.linalg.eigh(Kt)
    m = float(ev[0])
    v = V[:, 0].copy()
    if v[int(np.argmax(np.abs(v)))] < 0.0:
        v = -v
    m_rel = abs(m - r["m"]) / max(abs(r["m"]), 1e-300)
    ii = (np.arange(h) + 0.5) * D
    oms = np.array([math.pi * j / Lu for j in range(1, KMAX + 1)])
    P = np.empty((h, KMAX + 1))
    P[:, 0] = v
    for j in range(1, KMAX + 1):
        p = np.cos(oms[j - 1] * ii)
        P[:, j] = p / float(np.linalg.norm(p))
    N = P.T @ P
    N = 0.5 * (N + N.T)
    nn = r["nn"]
    i_cut = int(np.searchsorted(nn, nc, side="right")) - 1
    tg = cxc.tail_grid(D, float(gam[-1]))
    abel = subg.abel_upper(tg, 1.0 / tg[:-1] ** 2,
                           n_start=float(N_Z))
    lw = [core.lag_weights_from_v(P[:, a], h)
          for a in range(KMAX + 1)]
    n_b = KMAX + 1
    Fp = np.zeros((n_b, n_b))
    Fz = np.zeros((n_b, n_b))
    TB = np.zeros((n_b, n_b))
    E_ar = np.zeros((n_b, n_b))
    E_head = np.zeros((n_b, n_b))
    E_tc = np.zeros((n_b, n_b))
    E_par = np.zeros((n_b, n_b))
    Zm = np.zeros((n_b, n_b))
    Zh = np.zeros((n_b, n_b))
    pol_dev = atom_dev = recon_dev = 0.0
    heart_ex = -1e18
    heart_slack = []
    spot_dev = 0.0
    pcs = []
    metas = []
    for a in range(n_b):
        for bb in range(a, n_b):
            Wab = 0.5 * (core.lag_weights_from_v(
                P[:, a] + P[:, bb], h) - lw[a] - lw[bb])
            e_ar = float(c_ar @ Wab)
            qa = mu * w2.q_read(Wab, uu, D, M)
            e_at = float(qa.sum())
            f_pr = e_ar + e_at
            f_mat = float(P[:, a] @ (Kt @ P[:, bb]))
            pol_dev = max(pol_dev, abs(f_pr - f_mat)
                          / max(1.0, abs(f_pr)))
            atom_dev = max(atom_dev, abs(float(c_at @ Wab) - e_at)
                           / max(1.0, abs(e_at)))
            head_at = float(qa[:i_cut + 1].sum()) if i_cut >= 0 \
                else 0.0
            t_int = e_at - head_at
            pc0 = w2.weight_pieces(Wab, u0, uL, D, M)
            tcont = w2.tcont_of(pc0)
            par = t_int - tcont
            sp = dict(nc=nc, u0=u0, uL=uL, tcont=tcont, par=par,
                      t_int=t_int)
            row_ab = dict(r)
            row_ab["Wv"] = Wab
            pc = cxc.phi_cont_of(row_ab, sp)
            recon_dev = max(recon_dev,
                            cxc.recon_of(row_ab, sp, pc))
            pcs.append(pc)
            metas.append((a, bb, e_ar, head_at, tcont, par, f_pr,
                          sp, row_ab))
    v_all = np.unique(np.concatenate([pc["v"] for pc in pcs]))
    Jm = np.zeros((len(v_all), len(pcs)))
    for c_i, pc in enumerate(pcs):
        idx = np.searchsorted(v_all, pc["v"])
        Jm[idx, c_i] += pc["J"]
    zs = np.zeros(len(pcs))
    zs_head = np.zeros(len(pcs))
    for i0 in range(0, len(gam), 1000):
        g = gam[i0:i0 + 1000]
        E = np.exp(1j * np.outer(g, v_all))
        blk = 4.0 * np.sum(
            (-(E @ Jm) / (g ** 2)[:, None]).real, axis=0)
        zs += blk
        if i0 == 0:
            gh = gam[:N_ANAT]
            Eh = np.exp(1j * np.outer(gh, v_all))
            zs_head += 4.0 * np.sum(
                (-(Eh @ Jm) / (gh ** 2)[:, None]).real, axis=0)
    for c_i, (pc, meta) in enumerate(zip(pcs, metas)):
        a, bb, e_ar, head_at, tcont, par, f_pr, sp, row_ab = meta
        par_hat = (-zs[c_i] - pc["triv"] - pc["ramp_at"]
                   + pc["ramp_cont"] + pc["ext_cont"]
                   - pc["ext_at"])
        dps = 4.0 * pc["sd"] * (pc["vmax"] * inv2 + 2.0 * inv3) \
            * cxc.DPS_ERR
        tailb = (4.0 * pc["sd"] * abel
                 + 4.0 * math.exp(0.5 * pc["vmax"]) * pc["sd"]
                 * s2t + dps
                 + 1e-12 * (1.0 + abs(pc["triv"])))
        heart = abs(par - par_hat)
        heart_ex = max(heart_ex, heart - tailb)
        heart_slack.append(math.log10(max(tailb, 1e-300)
                                      / max(heart, 1e-300)))
        Fp[a, bb] = Fp[bb, a] = f_pr
        Fz[a, bb] = Fz[bb, a] = e_ar + head_at + tcont + par_hat
        TB[a, bb] = TB[bb, a] = tailb
        E_ar[a, bb] = E_ar[bb, a] = e_ar
        E_head[a, bb] = E_head[bb, a] = head_at
        E_tc[a, bb] = E_tc[bb, a] = tcont
        E_par[a, bb] = E_par[bb, a] = par
        Zm[a, bb] = Zm[bb, a] = -zs[c_i]
        Zh[a, bb] = Zh[bb, a] = -zs_head[c_i]
        if do_spot and a == 0 and bb == 0:
            ph_v, tb_v = cxc.direct_read(row_ab, sp, pc, gam,
                                         abel, s2t, inv2, inv3)
            spot_dev = max(abs(par_hat - ph_v)
                           / max(1.0, abs(ph_v)),
                           abs(tailb - tb_v)
                           / max(tailb, 1e-300))
    pc00 = pcs[0]
    eat00 = metas[0][6] - metas[0][2]
    # window / osc blocks from the smooth comb (source-side)
    ug, mg = w2.smooth_comb(alpha)
    c_sm = np.asarray(core.atom_lags_at(alpha, M, ug, mg)[0], float)
    Kw = core.odd_toeplitz(c_ar + c_sm, M)
    Fw = P.T @ Kw @ P
    Fw = 0.5 * (Fw + Fw.T)
    return dict(kz=r["kz"], h=h, alpha=alpha, m=m, mu1=r["mu1"],
                v=v, P=P, N=N, F=Fp, Fz=Fz, TB=TB, oms=oms,
                Lu=Lu, nc=nc, u0=u0, D=D, m_rel=m_rel, pol=pol_dev,
                atom=atom_dev, recon=recon_dev, heart_ex=heart_ex,
                heart_slack=heart_slack, spot=spot_dev,
                pc00=pc00, par00=metas[0][5], zs00=float(zs[0]),
                f00_scale=max(1.0, abs(eat00)),
                lam_sm=r.get("lam_sm"),
                n_inband=int(np.sum(oms <= w2.OMEGA_C)),
                E_ar=E_ar, E_head=E_head, E_tc=E_tc, E_par=E_par,
                Z=Zm, Zhead=Zh, Fw=Fw,
                uu=np.asarray(uu, float),
                mu_at=np.asarray(mu, float))


# ------------------------------------------------------------------
# THE CONTINUUM CLOSED FORM (entry asymptotics, D -> 0)
# ------------------------------------------------------------------
def _segv(k, phi, L):
    """int_0^L cos(k u + phi) du, vectorized over phi/L, k scalar."""
    phi = np.asarray(phi, float)
    L = np.asarray(L, float)
    if abs(k) < 1e-14:
        return L * np.cos(phi)
    return (np.sin(k * L + phi) - np.sin(phi)) / k


def _S_ab(oa, ob, s, al):
    """both-order continuum cross-correlation at shift s >= 0."""
    s = np.asarray(s, float)
    L = np.maximum(al - s, 0.0)
    v = 0.5 * (_segv(oa - ob, -ob * s, L)
               + _segv(oa + ob, ob * s, L))
    v = v + 0.5 * (_segv(ob - oa, -oa * s, L)
                   + _segv(ob + oa, oa * s, L))
    return np.where(s < al, v, 0.0)


def _H_ab(oa, ob, s, al):
    """continuum Hankel overlap: int p_a(u) p_b(t - u) du at
    t = 2 al - s."""
    s = np.asarray(s, float)
    t = 2.0 * al - s
    lo = np.maximum(0.0, t - al)
    hi = np.minimum(al, t)
    L = np.maximum(hi - lo, 0.0)
    v = 0.5 * (_segv(oa + ob, (oa + ob) * lo - ob * t, L)
               + _segv(oa - ob, (oa - ob) * lo + ob * t, L))
    return np.where(L > 0.0, v, 0.0)


def cont_block(alpha, oms, uu, mu):
    """The continuum closed-form carrier block C_cont (KMAX x KMAX)
    + Gram N_cont: ARCH(G) - (1/2) sum mu_j G(u_j), all closed trig
    forms; h enters ONLY through (alpha, omega_j) + the deployed
    prime-power comb."""
    K = len(oms)
    C = np.zeros((K, K))
    Ncont = np.zeros((K, K))
    nu = np.array([alpha / 2.0
                   + math.sin(2.0 * o * alpha) / (4.0 * o)
                   for o in oms])
    ss = (np.arange(NS_CONT) + 0.5) * (2.0 * alpha / NS_CONT)
    dv = 2.0 * alpha / NS_CONT
    emh = np.exp(-0.5 * ss)
    em2 = np.exp(-2.0 * ss)
    den = -np.expm1(-2.0 * ss)
    for a in range(K):
        for b in range(a, K):
            oa, ob = oms[a], oms[b]
            g0 = float(_S_ab(oa, ob, 0.0, alpha)) * 0.5 \
                - float(_H_ab(oa, ob, 0.0, alpha))
            G = _S_ab(oa, ob, ss, alpha) - _H_ab(oa, ob, ss, alpha)
            arch = -(EULER + LOG_PI) * g0 \
                + float(np.sum((g0 * 2.0 * em2 - G * emh) / den)) \
                * dv \
                + g0 * (-math.log1p(-math.exp(-4.0 * alpha)))
            Gu = _S_ab(oa, ob, uu, alpha) - _H_ab(oa, ob, uu, alpha)
            at = -0.5 * float(mu @ Gu)
            val = (arch + at) / math.sqrt(nu[a] * nu[b])
            C[a, b] = C[b, a] = val
            nab = 0.5 * float(_segv(oa - ob, 0.0, alpha)
                              + _segv(oa + ob, 0.0, alpha))
            Ncont[a, b] = Ncont[b, a] = nab \
                / math.sqrt(nu[a] * nu[b])
    return C, Ncont


# ------------------------------------------------------------------
# fits: frozen regressor selection + envelope + crossover
# ------------------------------------------------------------------
def fit_limit(hs, als, y):
    hs = np.asarray(hs, float)
    als = np.asarray(als, float)
    y = np.asarray(y, float)
    good = np.isfinite(y)
    best = None
    for name, z in (("1/alpha", 1.0 / als), ("1/sqrt(h)",
                                             1.0 / np.sqrt(hs)),
                    ("1/h", 1.0 / hs)):
        a, b, r2 = w2.ols_line(z[good], y[good])
        res = y[good] - a - b * z[good]
        cand = dict(A=a, B=b, r2=r2, zname=name,
                    resmax=float(np.max(np.abs(res))),
                    z=z)
        if best is None or (np.isfinite(r2)
                            and r2 > best["r2"]):
            best = cand
    return best


def crossover(fit):
    """z_0 with A - (|B| z + SAFE resmax) > 0 for z < z_0;
    None if the envelope never certifies."""
    gap = fit["A"] - SAFE * fit["resmax"]
    if gap <= 0.0:
        return None
    if abs(fit["B"]) < 1e-300:
        return float("inf")
    return gap / abs(fit["B"])


def finish(labels):
    section("V -- FROZEN VERDICT")
    passed = sum(1 for _n, ok in CHECKS if ok)
    if KILLS:
        verdict = {"K1": "PIPELINE-BROKEN", "K2": "WARD-BROKEN",
                   "K3": "ALGEBRA-BROKEN"}[KILLS[0]]
    else:
        verdict = " / ".join(labels.get(k, "-")
                             for k in ("v0", "v1", "v2", "v3",
                                       "v4", "v5"))
    print("\n  VERDICT: %s" % verdict)
    print("""
  HONEST SCOPE: every statement is per-rung on the deployed
  ladder; the v-seat is a MEASURED direction
  (DIRECTION-CONDITIONAL); the deep block is FLOAT-LEVEL; fits and
  envelopes are EMPIRICAL laws, not theorems; the composed all-h
  statement is a CONJECTURE with named gaps; a finite verified
  zero sum can never prove RH.  NO RH claim; no marker moves; no
  promotion.""")
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed"
          % (time.time() - T0, len(CHECKS), len(CHECKS) - passed))
    if any(not ok for _n, ok in CHECKS):
        print("FAILED: %s" % [nm for nm, ok in CHECKS if not ok])
    return 0 if passed == len(CHECKS) else 1


def main():
    section("PRIME.WALL.ZEROFRAME.UNIFORM.01 -- the uniform lower "
            "frame bound on the FIXED carrier space "
            "(EXPLORATION ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s"
          % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
    shas = dict(
        zf=hashlib.sha256(zf.__doc__.encode("utf-8")).hexdigest(),
        w2=hashlib.sha256(w2.__doc__.encode("utf-8")).hexdigest(),
        cxc=hashlib.sha256(cxc.__doc__.encode("utf-8")).hexdigest(),
        subgamma=hashlib.sha256(
            subg.__doc__.encode("utf-8")).hexdigest())
    for tag in sorted(shas):
        print("    %-8s SPEC SHA-256 = %s" % (tag, shas[tag]))
    print("    PEDIGREE (EXTERNAL-CITED): gamma_1 = %.6f (first "
          "Riemann ordinate); T0 = %.1e (Platt-Trudgian 2021); "
          "Rosser 1941 N(T) corridor (%.3f, %.3f, %.3f); Buethe "
          "2018; B_PSI = %.5f; classical zero-free region (de la "
          "Vallee Poussin 1896) as the tail-side theorem class; "
          "verified ordinates: local cache, builder disclosed "
          "(CLXXXIX)."
          % (subg.GAMMA1, subg.T0_RH, subg.ROSSER_A, subg.ROSSER_B,
             subg.ROSSER_C, core.B_PSI))
    if SMOKE:
        print("    *** SMOKE MODE: ladder kz <= %d, %d deep, "
              "full-only reference wards deferred ***"
              % (KZ_TOP, N_DEEP))
    check("S0 AST firewall clean", not ast_scan(), kill="K2")
    ok_pref = all(shas[k][:8] == v for k, v in PREFIXES.items())
    check("S0b predecessor SPEC prefixes reproduced (%s)"
          % "/".join(PREFIXES[k] for k in sorted(PREFIXES)),
          ok_pref, kill="K2")

    # ------------------------------------------------------------ Z
    section("Z -- the verified-zero cache (CLXXXIX wards verbatim; "
            "REUSED, no expansion)")
    check("Z0 cache present", os.path.exists(ZC_NPY), kill="K1")
    if KILLS:
        return finish({})
    gam = np.load(ZC_NPY)
    t_c = float(gam[-1])
    check("Z1 census %d == %d, increasing, first == gamma_1 "
          "(dev %.1e)" % (len(gam), N_Z, abs(gam[0] - subg.GAMMA1)),
          len(gam) == N_Z and bool(np.all(np.diff(gam) > 0.0))
          and abs(gam[0] - subg.GAMMA1) <= 2.0e-6, kill="K2")
    kk = np.arange(1, N_Z + 1, dtype=float)
    up_r = subg.n_up(gam + CORR_EPS)
    lo_r = subg.n_lo(gam + CORR_EPS)
    up_l = subg.n_up(np.maximum(gam - CORR_EPS, 2.0))
    lo_l = subg.n_lo(np.maximum(gam - CORR_EPS, 2.0))
    n_ok = int(np.sum((kk <= up_r) & (kk >= lo_r)
                      & (kk - 1.0 <= up_l) & (kk - 1.0 >= lo_l)))
    check("Z2 Rosser-corridor consistency per index (%d/%d both "
          "sides)" % (n_ok, N_Z), n_ok == N_Z, kill="K2")
    from mpmath import mp as _mp, mpc as _mpc
    from mpmath import zeta as _zf
    _mp.dps = 20
    idx = np.unique(np.geomspace(1, N_Z, NS_ZETA).astype(int)) - 1
    worst_z = max(float(abs(_zf(_mpc(0.5, float(gam[i])))))
                  for i in idx)
    check("Z3 independent zeta spot check <= %.0e at %d ordinates "
          "(worst %.1e)" % (ZETA_TOL, len(idx), worst_z),
          worst_z <= ZETA_TOL, kill="K2")
    check("Z4 T_c = %.4f below T0" % t_c, t_c < subg.T0_RH,
          kill="K2")
    inv2 = float(np.sum(1.0 / gam ** 2))
    inv3 = float(np.sum(1.0 / gam ** 3))
    s2t = subg.s2_tail()

    # ------------------------------------------------------------ W
    section("W -- the CLXXXV ladder + deep block (CXCVII selection "
            "verbatim)")
    rungs = []
    for kz in range(2, KZ_TOP + 1):
        r = w2.build_rung(kz)
        if r is not None:
            rungs.append(r)
    rungs.sort(key=lambda r: (r["h"], r["kz"]))
    NL = len(rungs)
    check("W1 CLXXXV ladder census %d %s  [%.1f s]"
          % (NL, "== 67" if not SMOKE else ">= 8 (smoke)",
             time.time() - T0),
          (NL == 67) if not SMOKE else (NL >= 8), kill="K1")
    if KILLS:
        return finish({})
    sub = [r for r in rungs if r["kz"] in w2.SUBSET]
    pres = max(r["pivres"] for r in sub) if sub else 0.0
    check("W2 WARD m > 0 on %d/%d + pivot collapse %.1e <= %.0e"
          % (sum(1 for r in rungs if r["m"] > 0), NL, pres,
             w2.RES_WARD),
          all(r["m"] > 0 for r in rungs) and pres <= w2.RES_WARD,
          kill="K2")
    mm_l = np.array([r["m"] for r in rungs])
    shat_l = mm_l / np.array([r["mu1"] for r in rungs])
    s3 = band(shat_l)
    if not SMOKE:
        check("W3 CXLIII band shat %.4f/%.4f/%.4f ~ %s"
              % (s3 + (w2.SHAT_REF,)),
              all(abs(s3[i] - w2.SHAT_REF[i]) <= w2.SHAT_TOL
                  for i in range(3)), kill="K2")
    else:
        print("    (smoke: shat band %.4f/%.4f/%.4f -- full ward "
              "deferred)" % s3)
        check("W3 deferred in smoke (disclosed)", True)
    check("W4 cB coverage %d/%d"
          % (sum(1 for r in rungs if r["ncB"] > 0), NL),
          all(r["ncB"] > 0 for r in rungs), kill="K2")
    # extended tables + deep selection (CXCVII verbatim)
    lam_ext = deep.build_ext_tables()
    dev = float(np.max(np.abs(lam_ext[:core.ATOM_MAX + 1]
                              - core.LAM_TAB)))
    check("W5 deep-table fidelity (overlap dev %.1e)" % dev,
          dev == 0.0 and deep.TAB_EXT == w2.TAB_EXT, kill="K2")
    NN_e = deep.EXT["NN"]
    psi_e = np.cumsum(lam_ext[NN_e])
    lf.ENV.update(lf.table_sups(NN_e, psi_e, deep.TAB_EXT))
    check("W6 Buethe envelope warded on the table (sup %.4f <= "
          "%.2f)" % (lf.ENV["BUETHE_SUP"], lf.BUETHE),
          lf.ENV["BUETHE_SUP"] <= lf.BUETHE, kill="K2")
    tg0 = cxc.tail_grid(rungs[0]["D"], t_c)
    abel0 = subg.abel_upper(tg0, 1.0 / tg0[:-1] ** 2,
                            n_start=float(N_Z))
    check("W7 Abel tail base %.4e in [%.0e, %.0e]"
          % ((abel0,) + ABEL_BAND),
          ABEL_BAND[0] <= abel0 <= ABEL_BAND[1], kill="K2")
    EXT = dict(lam=lam_ext, NN=NN_e,
               U=np.log(NN_e.astype(float)),
               MU=2.0 * lam_ext[NN_e] / np.sqrt(NN_e.astype(float)))
    EXT["G"] = np.diff(EXT["U"])
    new_kz = []
    for kz in range(2, min(w2.KZ_SCAN_MAX, len(EXT["NN"]) - 2)):
        a_ = float(EXT["U"][kz])
        Xk = math.exp(2.0 * a_)
        if Xk > w2.TAB_EXT:
            break
        if Xk <= core.ATOM_MAX:
            continue
        D_k = 0.5 * float(EXT["G"][kz]) / float(core.NU_MAIN)
        Mk = int(math.ceil(a_ / D_k - 1.0e-9)) + 1
        if Mk % 2:
            Mk += 1
        if not (w2.H_HOLD[0] <= Mk // 2 <= w2.H_HOLD[1]):
            continue
        new_kz.append(kz)
    deep_rows = []
    if new_kz:
        order = sorted(new_kz)
        pick = sorted(set(int(round(t)) for t in
                          np.linspace(0, len(order) - 1,
                                      min(N_DEEP, len(order)))))
        for ii_ in pick:
            r = w2.build_rung(order[ii_], ext=EXT)
            if r is not None:
                deep_rows.append(r)
        deep_rows.sort(key=lambda r: r["h"])
    all_rows = [(r, False) for r in rungs] \
        + [(r, True) for r in deep_rows]

    # ------------------------------------------------------------ F
    section("F -- frames with the extended split builder "
            "(zero-read warded; BIT ward vs zf.frame_of)")
    frames = []
    pol_w = atom_w = recon_w = spot_w = m_w = 0.0
    heart_w = -1e18
    slack_all = []
    for i, (r, is_deep) in enumerate(all_rows):
        fr = frame_split_of(r, gam, s2t, inv2, inv3, do_spot=True)
        if fr is None:
            continue
        fr["deep"] = is_deep
        frames.append(fr)
        pol_w = max(pol_w, fr["pol"])
        atom_w = max(atom_w, fr["atom"])
        recon_w = max(recon_w, fr["recon"])
        spot_w = max(spot_w, fr["spot"])
        m_w = max(m_w, fr["m_rel"])
        heart_w = max(heart_w, fr["heart_ex"])
        slack_all.extend(fr["heart_slack"])
        if (i + 1) % 15 == 0:
            print("    ... %d frames  [%.1f s]"
                  % (i + 1, time.time() - T0), flush=True)
    NF = len(frames)
    NE = (KMAX + 1) * (KMAX + 2) // 2
    n_deep_fr = sum(1 for fr in frames if fr["deep"])
    print("    %d frames (%d deep), %d zero-read entries each  "
          "[%.1f s]" % (NF, n_deep_fr, NE, time.time() - T0))
    check("F0 frame census %d (deep %d)" % (NF, n_deep_fr),
          NF >= (8 if SMOKE else 70)
          and n_deep_fr == len(deep_rows), kill="K1")
    check("F1 WARD polarization: worst %.2e <= %.0e"
          % (pol_w, POL_WARD), pol_w <= POL_WARD, kill="K2")
    check("F2 WARD atom identity: worst %.2e <= %.0e"
          % (atom_w, ATOM_ID_WARD), atom_w <= ATOM_ID_WARD,
          kill="K2")
    check("F3 WARD CXCIII bookkeeping recon: worst %.2e <= %.0e"
          % (recon_w, RECON_TOL), recon_w <= RECON_TOL, kill="K2")
    check("F4 WARD zero-read HEART |PARITH - hat| <= TAILB on "
          "every rung x entry (worst excess %.2e; slack med "
          "%+.2f dex)" % (heart_w, float(np.median(slack_all))),
          heart_w <= 0.0, kill="K2")
    check("F5 WARD m consistency: worst %.2e <= %.0e"
          % (m_w, MREL_WARD), m_w <= MREL_WARD, kill="K2")
    check("F6 WARD SPOT vs CXCIII direct_read: worst %.2e <= %.0e"
          % (spot_w, SPOT_WARD), spot_w <= SPOT_WARD, kill="K2")
    # BIT ward: the extended builder == zf.frame_of on a subset
    hs_f = np.array([fr["h"] for fr in frames], float)
    pick_bit = sorted(set(
        int(round(t)) for t in np.geomspace(1, NF, N_BIT) - 1.0))
    bit_w = 0.0
    for ib in pick_bit:
        fr = frames[ib]
        src = next(r for r, _d in all_rows
                   if r["kz"] == fr["kz"] and r["h"] == fr["h"])
        fo = zf.frame_of(src, gam, s2t, inv2, inv3, do_spot=False)
        bit_w = max(bit_w,
                    float(np.max(np.abs(fr["F"] - fo["F"]))),
                    float(np.max(np.abs(fr["Fz"] - fo["Fz"]))),
                    float(np.max(np.abs(fr["TB"] - fo["TB"]))))
    check("F7 WARD BIT consistency vs zf.frame_of on %d subset "
          "rungs: worst %.2e <= %.0e"
          % (len(pick_bit), bit_w, BIT_WARD),
          bit_w <= BIT_WARD, kill="K2")

    # ------------------------------------------------------------ R
    section("R -- PREDECESSOR HEADLINE REPRODUCTION (the ward "
            "before anything new; CXCVII verbatim)")
    minors = [zf.minors_of(fr) for fr in frames]
    dev_f00 = dev_piv = dev_det = dev_cmp = 0.0
    n_c8 = n_pos_fac = n_npd = 0
    for mo in minors:
        d = mo["dev"]
        dev_f00 = max(dev_f00, d["f00"])
        if "piv" in d:
            dev_piv = max(dev_piv, d["piv"])
            if np.isfinite(d.get("det", float("nan"))):
                dev_det = max(dev_det, d["det"])
            if max(d["f00"], d["piv"], d.get("det", 0.0)) \
                    <= ID_CENSUS:
                n_c8 += 1
        dev_cmp = max(dev_cmp, d["compress"])
        rho = mo["rho"][KMAX]
        if rho is not None and rho < 1.0:
            n_pos_fac += 1
        if mo["lf_pen"] is None:
            n_npd += 1
    check("R1 WARD F00 == m (A1 scale): worst %.2e <= %.0e"
          % (dev_f00, F00_WARD), dev_f00 <= F00_WARD, kill="K2")
    check("R2 WARD Schur identities (pivot %.2e, det %.2e) <= "
          "%.0e" % (dev_piv, dev_det, ID_WARD_NUM),
          max(dev_piv, dev_det) <= ID_WARD_NUM, kill="K2")
    check("R3 WARD COMPRESS lampen(F|N) == m: worst %.2e <= %.0e "
          "(N not PD on %d)" % (dev_cmp, COMPRESS_WARD, n_npd),
          dev_cmp <= COMPRESS_WARD and n_npd == 0, kill="K2")
    rhoK = np.array([mo["rho"][KMAX] for mo in minors
                     if mo["rho"][KMAX] is not None])
    fac = 1.0 - rhoK
    rho_med = float(np.median(rhoK))
    check("R4 WARD 1 - rho positive %d/%d (band %.3e/%.3e/%.3e)"
          % ((n_pos_fac, NF) + band(fac)),
          n_pos_fac == NF, kill="K2")
    al_all = np.array([fr["alpha"] for fr in frames])
    mu1_all = np.array([fr["mu1"] for fr in frames])
    m_all = np.array([fr["m"] for fr in frames])
    cK = np.array([mo["cpen"][KMAX] if mo["cpen"][KMAX] is not None
                   else np.nan for mo in minors])
    c_carr = cK / mu1_all
    lg_cK = np.log10(np.maximum(c_carr, 1e-300))
    bK, seK, r2K = w2.jack_slope(al_all, lg_cK)
    c3 = band(c_carr[np.isfinite(c_carr)])
    ks_cap, cens_rho = [], 0
    for fr, mo in zip(frames, minors):
        kc = next((K for K in range(1, KMAX + 1)
                   if mo["cpen"][K] is not None
                   and mo["cpen"][K] / fr["m"] <= zf.CAP_BAR),
                  KMAX + 1)
        ks_cap.append(kc)
        kr = next((K for K in range(1, KMAX + 1)
                   if mo["rho"][K] is not None
                   and mo["rho"][K] >= zf.RHO_BAR), KMAX + 1)
        cens_rho += int(kr == KMAX + 1)
    kc3 = tuple(int(x) for x in band(ks_cap))
    n_res = 0
    for fr in frames:
        lminN = float(np.linalg.eigvalsh(fr["N"])[0])
        if lminN <= 0.0:
            continue
        dF = float(np.linalg.norm(fr["TB"], 2))
        lfp = zf.lampen(fr["F"], fr["N"])
        if lfp is not None and dF / lminN < lfp:
            n_res += 1
    if not SMOKE:
        check("R5 rho med %.4f ~ %.3f (tol %.0e)"
              % (rho_med, RHO_MED_REF, RHO_MED_TOL),
              abs(rho_med - RHO_MED_REF) <= RHO_MED_TOL, kill="K2")
        check("R6 c_carr(%d) band %.4f/%.4f/%.4f ~ %s (tol %.0e)"
              % ((KMAX,) + c3 + (CCARR_REF, CCARR_TOL)),
              all(abs(c3[i] - CCARR_REF[i]) <= CCARR_TOL
                  for i in range(3)), kill="K2")
        check("R7 c_carr trend %+.4f dex/alpha ~ %+.4f (tol %.0e; "
              "2SE %.4f R^2 %.3f)"
              % (bK, CCARR_TREND_REF, CCARR_TREND_TOL,
                 2 * seK, r2K),
              abs(bK - CCARR_TREND_REF) <= CCARR_TREND_TOL,
              kill="K2")
        check("R8 K*_cap band %s == %s, rho-censored %d == %d, "
              "1e-8 census %d == %d, SIGN-RESOLVED %d == %d"
              % (kc3, KCAP_REF, cens_rho, CENSRHO_REF, n_c8,
                 ID8_REF, n_res, SIGNRES_REF),
              kc3 == KCAP_REF and cens_rho == CENSRHO_REF
              and n_c8 == ID8_REF and n_res == SIGNRES_REF,
              kill="K2")
    else:
        print("    (smoke: rho med %.4f, c_carr band %.3f/%.3f/"
              "%.3f trend %+.4f, K*_cap %s, cens_rho %d, 1e-8 "
              "census %d/%d, sign-res %d -- full refs deferred)"
              % ((rho_med,) + c3 + (bK, kc3, cens_rho, n_c8, NF,
                                    n_res)))
        check("R5-R8 deferred in smoke (disclosed)", True)

    # ------------------------------------------------------------ D
    section("D -- ENTRY ASYMPTOTICS: the continuum closed form vs "
            "the exact entries (the analytic ward)")
    err_med_r, err_wst_r, err_raw_r, dlam_r, Ds_r = [], [], [], [], []
    for fr in frames:
        Cb = fr["F"][1:, 1:]
        NCb = fr["N"][1:, 1:]
        Cc, Ncc = cont_block(fr["alpha"], fr["oms"], fr["uu"],
                             fr["mu_at"])
        # amendment A1 (CLXXXV-A3 precedent): abs-or-rel scale --
        # the near-zero (6,6) corner entry divides a D^2 omega^2
        # absolute error by a vanishing entry scale; the deviation
        # is measured against max(|C_ab|, SCALE_FLOOR max|C|);
        # the raw pure-relative worst stays reported.
        blk = float(np.max(np.abs(Cb)))
        sc = np.maximum(np.abs(Cb), SCALE_FLOOR * blk)
        rel = np.abs(Cc - Cb) / sc
        raw = np.abs(Cc - Cb) / np.maximum(np.abs(Cb), 1e-30)
        iu = np.triu_indices(KMAX)
        err_med_r.append(float(np.median(rel[iu])))
        err_wst_r.append(float(np.max(rel[iu])))
        err_raw_r.append(float(np.max(raw[iu])))
        le = zf.lampen(Cb, NCb)
        lc = zf.lampen(Cc, Ncc)
        dlam_r.append(abs(lc - le) / fr["mu1"]
                      if (le is not None and lc is not None)
                      else float("nan"))
        Ds_r.append(fr["D"])
        fr["c_carr"] = (le / fr["mu1"]) if le is not None \
            else float("nan")
        fr["cap"] = (le / fr["m"]) if le is not None \
            else float("nan")
        fr["Cb"], fr["NCb"] = Cb, NCb
    err_med = np.array(err_med_r)
    err_wst = np.array(err_wst_r)
    err_raw = np.array(err_raw_r)
    med_of_med = float(np.median(err_med))
    wst_all = float(np.max(err_wst))
    check("D1 WARD continuum model worst entry deviation (A1 "
          "abs-or-rel scale, floor %.0e max|C|) %.2e <= %.0e "
          "(rung-median band %.2e/%.2e/%.2e; RAW pure-rel worst "
          "%.2e at the near-zero (6,6) corner, reported)"
          % ((SCALE_FLOOR, wst_all, CONT_BAR) + band(err_med)
             + (float(np.max(err_raw)),)),
          wst_all <= CONT_BAR, kill="K2")
    bD, seD, r2D = w2.jack_slope(np.log10(np.array(Ds_r)),
                                 np.log10(np.maximum(err_wst,
                                                     1e-300)))
    check("D2 typed: entry-error law log10(err) vs log10(D): "
          "slope %+.2f (2SE %.2f, R^2 %.2f) -- the D^2-class "
          "remainder law" % (bD, 2 * seD, r2D), True)
    dlam = np.array(dlam_r)
    print("    bottom tracking |lampen(C_cont|N_cont) - "
          "lampen(C|N)|/mu1: band %.3f/%.3f/%.3f"
          % band(dlam[np.isfinite(dlam)]))
    dlam_med = float(np.median(dlam[np.isfinite(dlam)]))
    # amendment A3 (typing only): the label diagnoses whether the
    # D -> 0 model resolves the mu1-scale bottom (price < 0.5 mu1)
    # or the floor is carried by the discrete grid itself.
    d3lab = ("BOTTOM-CONTINUUM-TRACKED(med %.3f mu1)" % dlam_med) \
        if dlam_med < 0.5 else \
        ("BOTTOM-NOT-CONTINUUM(med price %.3f mu1 ~ the bottom "
         "itself: the mu1 floor is carried by the DISCRETE grid; "
         "any analytic route must keep the lattice corrections, "
         "the naive D -> 0 limit loses the floor)" % dlam_med)
    check("D3 typed: %s" % d3lab, True)

    # ------------------------------------------------------------ A
    section("A -- THE LIMIT OBJECT: normalization triad + "
            "envelope/crossover")
    hs = np.array([fr["h"] for fr in frames], float)
    diag_med = np.array([float(np.median(np.diag(fr["Cb"])))
                         for fr in frames])
    b_dg, se_dg, r2_dg = w2.jack_slope(np.log10(hs),
                                       np.log10(diag_med))
    b_da, _se_da, r2_da = w2.jack_slope(al_all, np.log10(diag_med))
    check("A1 typed (N1): Fbar = C/mu1 has NO entrywise limit -- "
          "median diagonal grows: slope %+.2f /log10 h (R^2 %.2f) "
          "| %+.3f dex/alpha (R^2 %.2f); diag band %.1f/%.1f/%.1f"
          % ((b_dg, r2_dg, b_da, r2_da) + band(diag_med)),
          True)
    # (N2) correlation + Gram entrywise limits
    iu = np.triu_indices(KMAX, k=1)
    R_stack = np.empty((NF, len(iu[0])))
    N_stack = np.empty((NF, len(iu[0])))
    for i, fr in enumerate(frames):
        dg = np.sqrt(np.diag(fr["Cb"]))
        R = fr["Cb"] / np.outer(dg, dg)
        R_stack[i] = R[iu]
        N_stack[i] = fr["NCb"][iu]
    R_inf = np.eye(KMAX)
    N_inf = np.eye(KMAX)
    res_R, res_N = [], []
    for j in range(len(iu[0])):
        fR = fit_limit(hs, al_all, R_stack[:, j])
        fN = fit_limit(hs, al_all, N_stack[:, j])
        R_inf[iu[0][j], iu[1][j]] = R_inf[iu[1][j], iu[0][j]] \
            = fR["A"]
        N_inf[iu[0][j], iu[1][j]] = N_inf[iu[1][j], iu[0][j]] \
            = fN["A"]
        res_R.append(fR["resmax"])
        res_N.append(fN["resmax"])
    lam_Rinf = zf.lampen(R_inf, N_inf)
    lam_Rv = lam_Rinf if lam_Rinf is not None else float("nan")
    res_scale = float(np.max(res_R))
    # amendment A3 (typing only): self-diagnosing label -- the
    # extrapolated pencil is only meaningful when |lampen| is
    # within the fit-residual scale.
    r_lab = ("DEGENERATE-CONSISTENT(lampen %+.3e within resid "
             "scale %.1e)" % (lam_Rv, res_scale)) \
        if abs(lam_Rv) <= SAFE * res_scale else \
        ("EXTRAPOLATION-NOISY(lampen %+.3e beyond resid scale "
         "%.1e: entrywise correlation extrapolation is not "
         "PSD-consistent at this scatter)" % (lam_Rv, res_scale))
    check("A2 typed (N2): correlation/Gram entrywise fits (med "
          "resid %.1e / %.1e) -> %s"
          % (float(np.median(res_R)), float(np.median(res_N)),
             r_lab), True)
    # (N3) bottom curves + envelope + crossover
    cc = np.array([fr["c_carr"] for fr in frames])
    cap = np.array([fr["cap"] for fr in frames])
    shat_f = m_all / mu1_all
    fit_c = fit_limit(hs, al_all, cc)
    x0_c = crossover(fit_c)
    fit_cap = fit_limit(hs, al_all, cap)
    lab_c = ("CROSSOVER(z_0 %.3g in %s: uniform positivity "
             "certified by the fit envelope for z < z_0)"
             % (x0_c, fit_c["zname"])) if x0_c is not None else \
        ("ENVELOPE-BLOCKED(scatter %.3f >= A %.3f / SAFE %.0f: "
         "the fit envelope cannot certify -- the blocker is the "
         "per-rung geometric band, not an h-trend)"
         % (fit_c["resmax"], fit_c["A"], SAFE))
    check("A3 typed (N3): c_carr fit A = %.3f + %.3f %s (R^2 "
          "%.3f, resmax %.3f) -> %s"
          % (fit_c["A"], fit_c["B"], fit_c["zname"], fit_c["r2"],
             fit_c["resmax"], lab_c), True)
    check("A4 typed: cap = c_carr/shat band %.3f/%.3f/%.3f "
          "(compression floor 1 free), fit A = %.3f + %.3f %s "
          "(R^2 %.3f, resmax %.3f)"
          % (band(cap[np.isfinite(cap)]) +
             (fit_cap["A"], fit_cap["B"], fit_cap["zname"],
              fit_cap["r2"], fit_cap["resmax"])), True)
    # covariate absorption: how much of the band is rung geometry
    kap = np.array([fr["alpha"] / fr["Lu"] for fr in frames])
    lg_nc = np.log10(np.array([fr["nc"] for fr in frames], float))
    X = np.column_stack([np.log10(hs), kap, lg_nc,
                         np.ones(NF)])

    def _ols_r2(y):
        good = np.isfinite(y)
        beta, *_ = np.linalg.lstsq(X[good], y[good], rcond=None)
        res = y[good] - X[good] @ beta
        st = float(np.sum((y[good] - np.mean(y[good])) ** 2))
        return 1.0 - float(np.sum(res ** 2)) / st if st > 0 \
            else float("nan")
    r2_shat = _ols_r2(np.log10(np.maximum(shat_f, 1e-300)))
    r2_cc = _ols_r2(lg_cK)
    r2_cap = _ols_r2(np.log10(np.maximum(cap, 1e-300)))
    check("A5 typed: covariate absorption OLS(log10 h, kappa, "
          "log10 nc) R^2: shat %.2f, c_carr %.2f, cap %.2f -- "
          "the mapped blocker share" % (r2_shat, r2_cc, r2_cap),
          True)
    # minimizer drift
    xs = []
    for fr in frames:
        try:
            L = np.linalg.cholesky(fr["NCb"])
        except np.linalg.LinAlgError:
            xs.append(None)
            continue
        Li = np.linalg.inv(L)
        Wm = Li @ fr["Cb"] @ Li.T
        w_, U = np.linalg.eigh(0.5 * (Wm + Wm.T))
        x = Li.T @ U[:, 0]
        x = x / math.sqrt(float(x @ (fr["NCb"] @ x)))
        if x[int(np.argmax(np.abs(x)))] < 0.0:
            x = -x
        xs.append(x)
    ref = xs[int(np.argmax(hs))]
    drift = np.array([float(np.linalg.norm(x - ref))
                      if x is not None else np.nan for x in xs])
    fit_dr = fit_limit(hs, al_all, drift)
    check("A6 typed: minimizer drift ||x*(h) - x*_deepest||_N "
          "band %.3f/%.3f/%.3f, fit A = %.3f + %.3f %s (R^2 %.2f)"
          % (band(drift[np.isfinite(drift)]) +
             (fit_dr["A"], fit_dr["B"], fit_dr["zname"],
              fit_dr["r2"])), True)
    om_hi = np.array([2.0 * fr["oms"][-1] for fr in frames])
    print("    combination-frequency band |omega_a +- omega_b| "
          "<= 2 omega_%d: %.3f/%.3f/%.3f; min gamma_1 distance "
          "%.3f (all reads BELOW the first ordinate)"
          % ((KMAX,) + band(om_hi) +
             (float(subg.GAMMA1 - np.max(om_hi)),)))

    # ------------------------------------------------------------ C
    section("C -- THE ARITHMETIC SEAT: window / prime-osc / "
            "zero-coordinate splits")
    lam_win, osc2, zn2, tb2, lam_cl = [], [], [], [], []
    head_share, zhead_share, flip = [], [], 0
    for fr in frames:
        Cb, NCb = fr["Cb"], fr["NCb"]
        Cw = fr["Fw"][1:, 1:]
        Co = Cb - Cw
        lw_ = zf.lampen(Cw, NCb)
        lam_win.append((lw_ / fr["mu1"]) if lw_ is not None
                       else float("nan"))
        osc2.append(float(np.linalg.norm(Co, 2)))
        Zb = fr["Z"][1:, 1:]
        zn2.append(float(np.linalg.norm(Zb, 2)) / fr["mu1"])
        tb2.append(float(np.linalg.norm(fr["TB"][1:, 1:], 2))
                   / fr["mu1"])
        lcl = zf.lampen(Cb - Zb, NCb)
        lam_cl.append((lcl / fr["mu1"]) if lcl is not None
                      else float("nan"))
        if lcl is not None and fr["c_carr"] == fr["c_carr"]:
            if (lcl > 0.0) != (fr["c_carr"] > 0.0):
                flip += 1
        zf_n = float(np.linalg.norm(fr["Z"][1:, 1:]))
        zh_n = float(np.linalg.norm(fr["Zhead"][1:, 1:]))
        zhead_share.append(zh_n / max(zf_n, 1e-300))
        head_share.append(
            float(np.linalg.norm(fr["E_head"][1:, 1:], 2))
            / max(float(np.linalg.norm(Cb, 2)), 1e-300))
    lam_win = np.array(lam_win)
    osc2 = np.array(osc2)
    zn2 = np.array(zn2)
    tb2 = np.array(tb2)
    lam_cl = np.array(lam_cl)
    n_wneg = int(np.sum(lam_win < 0.0))
    b_osc, se_osc, r2_osc = w2.jack_slope(
        al_all, np.log10(np.maximum(osc2, 1e-300)))
    demand = np.log10(osc2 / (C0_CAND * mu1_all))
    b_dem, se_dem, r2_dem = w2.jack_slope(al_all, demand)
    if n_wneg >= NF // 2:
        seat_lab = ("SEAT-PRIME-CARRIED(window bottom %.1e/%.1e/"
                    "%.1e mu1, negative %d/%d; ||C_osc||_2 "
                    "%.2f/%.2f/%.2f with slope %+.3f dex/alpha "
                    "R^2 %.2f -- O(1)-FLAT; demand %.2f/%.2f/%.2f "
                    "dex, slope %+.3f dex/alpha)"
                    % (band(lam_win[np.isfinite(lam_win)])
                       + (n_wneg, NF) + band(osc2)
                       + (b_osc, r2_osc) + band(demand)
                       + (b_dem,)))
    elif n_wneg == 0:
        seat_lab = "SEAT-ARCH-CARRIED(window bottom positive %d/%d)" \
            % (NF - n_wneg, NF)
    else:
        seat_lab = "SEAT-MIXED(window negative %d/%d)" % (n_wneg,
                                                          NF)
    check("C1 typed: %s" % seat_lab, True)
    z_lab = ("Z-PERTURBATIVE(||Z||_2/mu1 %.1e/%.1e/%.1e; "
             "bottom-sign flips removing Z: %d/%d)"
             % (band(zn2) + (flip, NF))) if flip == 0 else \
        ("Z-LOADBEARING(flips %d/%d; ||Z||_2/mu1 %.1e/%.1e/%.1e)"
         % ((flip, NF) + band(zn2)))
    check("C2 typed: %s at N_Z = %d (REUSED)" % (z_lab, N_Z), True)
    b_tb, _se_tb, r2_tb = w2.jack_slope(al_all, np.log10(tb2))
    check("C3 typed: ||TAILB||_2/mu1 band %.1e/%.1e/%.1e, slope "
          "%+.3f dex/alpha (R^2 %.2f) -- what the FIXED cache can "
          "certify at the bottom (SIGN-RESOLVED %d/%d reproduced)"
          % (band(tb2) + (b_tb, r2_tb, n_res, NF)), True)
    check("C4 typed: zero anatomy -- first %d ordinates carry "
          "share %.2f/%.2f/%.2f of ||Z||_F; finite core E_head "
          "(primes <= nc) norm share %.3f/%.3f/%.3f"
          % ((N_ANAT,) + band(zhead_share) + band(head_share)),
          True)
    print("    lampen((C - Z)|N)/mu1 band %.3f/%.3f/%.3f vs "
          "c_carr band %.3f/%.3f/%.3f"
          % (band(lam_cl[np.isfinite(lam_cl)])
             + band(cc[np.isfinite(cc)])))

    # ------------------------------------------------------------ G
    section("G -- CONTROLS (must fire; CXCVII verbatim, reused)")
    check("G0 WARD smooth world lam_sm < 0 on %d/%d rungs"
          % (sum(1 for r, _d in all_rows if r["lam_sm"] < 0.0),
             len(all_rows)),
          all(r["lam_sm"] < 0.0 for r, _d in all_rows), kill="K2")
    r9 = next((r for r in rungs if r["kz"] == CTRL_KZ), None)
    if r9 is None:
        r9 = w2.build_rung(CTRL_KZ)
    NE9 = int(math.floor(math.exp(2.0 * r9["alpha"]))) + 1 \
        if r9 is not None else 0
    ctrls = {}
    if r9 is not None:
        lamE = w2.lambda_eps(NE9)
        nnE = np.nonzero(np.abs(lamE) > 1e-12)[0]
        ctrls["Epstein"] = w2.build_rung(
            CTRL_KZ, comb=(np.log(nnE.astype(float)),
                           2.0 * lamE[nnE]
                           / np.sqrt(nnE.astype(float))))
        ctrls["scramble"] = w2.build_rung(CTRL_KZ, scramble_seed=1)
    nc_ctrl = int(r9["ncB"]) if (r9 is not None
                                 and r9["ncB"] > 0) else w2.NB_MED
    ctrl_fire, ctrl_heart = {}, {}
    for name, rc in ctrls.items():
        if rc is None:
            ctrl_fire[name] = True
            ctrl_heart[name] = -1
            print("    %-9s: chain dead -> fires" % name)
            continue
        ctrl_fire[name] = rc["m"] < 0.0
        frc = zf.frame_of(rc, gam, s2t, inv2, inv3,
                          nc_override=nc_ctrl)
        if frc is None:
            ctrl_heart[name] = 0
            continue
        iu9 = np.triu_indices(KMAX + 1)
        n_break = int(np.sum((np.abs(frc["F"] - frc["Fz"])
                              > frc["TB"])[iu9]))
        worst = float(np.max((np.abs(frc["F"] - frc["Fz"])
                              / np.maximum(frc["TB"],
                                           1e-300))[iu9]))
        ctrl_heart[name] = n_break
        moc = zf.minors_of(frc)
        lcp = moc["cpen"][KMAX]
        print("    %-9s: m %+.3e (%s); heart breaks %d/%d entries "
              "(worst %.1e x TAILB); carrier bottom/|m| %+.2f"
              % (name, rc["m"],
                 "fires" if ctrl_fire[name] else "SILENT",
                 n_break, NE, worst,
                 (lcp / abs(rc["m"])) if lcp is not None
                 else float("nan")), flush=True)
    check("G1 WARD Epstein + scramble fire at kz %d (wall level)"
          % CTRL_KZ, all(ctrl_fire.get(k, False)
                         for k in ("Epstein", "scramble")),
          kill="K2")
    check("G2 WARD scramble breaks the zero-read heart on >= %d "
          "entries (%d/%d)"
          % (SCR_MIN, max(ctrl_heart.get("scramble", 0), 0), NE),
          ctrl_heart.get("scramble", 0) >= SCR_MIN
          or ctrl_heart.get("scramble") == -1, kill="K2")
    check("G3 typed: Epstein heart census %d/%d entries"
          % (max(ctrl_heart.get("Epstein", 0), 0), NE), True)
    fr9 = next((fr for fr in frames if fr["kz"] == CTRL_KZ
                and not fr["deep"]), None)
    if fr9 is None and r9 is not None:
        fr9 = frame_split_of(r9, gam, s2t, inv2, inv3)
    if fr9 is not None:
        pc9 = fr9["pc00"]
        g1 = float(gam[0])
        on_pair = 4.0 * float((-(np.exp(1j * g1 * pc9["v"])
                                 @ pc9["J"]) / g1 ** 2).real)
        dlt = IMP_BETA - 0.5
        quad = 2.0 * (cxc.hat_seg_c(pc9["edges"], pc9["fvals"],
                                    pc9["slopes"],
                                    dlt + 1j * g1).real
                      + cxc.hat_seg_c(pc9["edges"], pc9["fvals"],
                                      pc9["slopes"],
                                      -dlt + 1j * g1).real)
        shift = abs(on_pair - quad)
        res9 = abs(fr9["F"][0, 0] - fr9["Fz"][0, 0])
        ratio = shift / max(res9, 1e-300)
        check("G4 CONTROL off-line impostor (gamma_1 -> beta = "
              "%.2f) shifts the (0,0) zero read by %.3e = %.1e x "
              "the genuine residual (>= %.0f)"
              % (IMP_BETA, shift, ratio, IMP_RATIO_MIN),
              ratio >= IMP_RATIO_MIN, kill="K2")
    else:
        check("G4 impostor seat unavailable (kz %d)" % CTRL_KZ,
              False, kill="K2")

    # ------------------------------------------------------------ T
    section("T -- TAU-SCREENS (w2 convention, vs log m)")
    lg_m = np.log10(np.maximum(m_all, 1e-300))
    scr = []
    for nm, y in (("c_carr(%d)" % KMAX, lg_cK),
                  ("cap", np.log10(np.maximum(cap, 1e-300))),
                  ("diag", np.log10(np.maximum(diag_med,
                                               1e-300))),
                  ("||C_osc||", np.log10(np.maximum(osc2,
                                                    1e-300))),
                  ("Z/mu1", np.log10(np.maximum(zn2, 1e-300))),
                  ("cont-err", np.log10(np.maximum(err_wst,
                                                   1e-300)))):
        s, _l = w2.screen_label(nm, lg_m, y)
        scr.append(s)
        print("    screen %s" % s)
    check("T1 tau-screens recorded (%d; diag RELOC expected -- "
          "it IS the declared divergence law)" % len(scr), True)

    # ------------------------------------------------------ verdict
    v1lab = ("CONT-MODEL(worst %.1e, med-of-med %.1e, D-law "
             "%+.2f)" % (wst_all, med_of_med, bD))
    if x0_c is not None:
        v2lab = ("BOTTOM-LIMIT-POSITIVE(A %.3f, %s, z_0 %.3g)"
                 % (fit_c["A"], fit_c["zname"], x0_c))
    else:
        v2lab = ("BOTTOM-FLAT-ENVELOPE-BLOCKED(A %.3f, scatter "
                 "%.3f, geometry-R^2 %.2f)"
                 % (fit_c["A"], fit_c["resmax"], r2_cc))
    v3lab = seat_lab.split("(")[0] + "+" + z_lab.split("(")[0]
    schur_s = shat_f * fac if len(fac) == NF else None
    if schur_s is not None:
        v4lab = ("SCHUR-HALF(s = shat(1-rho) band %.1e/%.1e/%.1e, "
                 "positive %d/%d)"
                 % (band(schur_s) + (int(np.sum(schur_s > 0)),
                                     NF)))
    else:
        v4lab = "SCHUR-HALF(n/a)"
    v5lab = ("CONTROLS(wall 2/2, scramble heart %d, impostor ok) "
             "+ REPRO(CXCVII green)"
             % max(ctrl_heart.get("scramble", 0), 0))
    v0lab = "UNIFORM-ARCHITECTURE-MEASURED"

    print("\n    THE COMPOSED ALL-H W2 DRAFT (CONJECTURE, named "
          "gaps -- printed verbatim):")
    print("      Per deployed rung h: M_h >= 0 <=> F_h >= 0 "
          "(CXCVII seat equivalence, warded) and, GIVEN "
          "C_K(h) > 0, F_h >= 0 <=> F00(h) >= f0(h)^T C_K(h)^{-1} "
          "f0(h) (Schur criterion).  Draft statement:")
    print("      [C1, THIS contract] exist K <= %d, c0 > 0 "
          "(measured candidate c0 = %.3f = min c_carr): "
          "lampen(C_K(h)|N_C(h)) >= c0 mu1(h) for all h;"
          % (KMAX, float(np.nanmin(cc))))
    print("      [C2, the seat half] F00(h) >= f0(h)^T C_K(h)^"
          "{-1} f0(h), i.e. 1 - rho_K(h) >= 0 -- measured "
          "positive %d/%d, min %.1e (DIRECTION-CONDITIONAL);"
          % (n_pos_fac, NF, float(np.min(fac))))
    print("      then W2_h = m_h = Schur_K/(1 - rho_K) > 0 for "
          "all h; composes with W1 (own chain, T_req curves "
          "pending the CXCV lane) and the B-half for the wall.")
    print("      NAMED GAPS: g1 the c_carr envelope is a FIT and "
          "it is %s; g2 deployed rungs only (the ladder is a "
          "discrete h-set, rung geometry alpha/D/nc is data); "
          "g3 the carrier bound is PRIME-CARRIED: the window "
          "part alone is indefinite (%d/%d negative) and the "
          "prime-osc reads must be controlled to %.1f..%.1f dex "
          "below their own size at the combination frequencies "
          "(<= %.2f, all >= %.2f below gamma_1) -- the CLXXXI/"
          "CLXXXVI phase-sensitive currency, growing %+.2f "
          "dex/alpha; g4 the FIXED zero cache certifies nothing "
          "at the bottom (||TAILB||/mu1 med %.1e) -- the uniform "
          "arithmetic input must be an h-uniform phase-sensitive "
          "bound, not a finite zero list; g5 C2 stays v-seat "
          "data (CXCVII refuted the W1-minor unification; the "
          "seat is per-rung measured direction)."
          % (("BLOCKED by the geometric scatter" if x0_c is None
              else "certifying below z_0"), n_wneg, NF,
             float(np.min(demand)), float(np.max(demand)),
             float(np.max(om_hi)),
             float(subg.GAMMA1 - np.max(om_hi)), b_dem,
             float(np.median(tb2))))
    return finish(dict(v0=v0lab, v1=v1lab, v2=v2lab, v3=v3lab,
                       v4=v4lab, v5=v5lab))


if __name__ == "__main__":
    raise SystemExit(main())
