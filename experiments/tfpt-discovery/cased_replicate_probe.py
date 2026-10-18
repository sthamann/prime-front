#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""cased_replicate_probe -- PRIME.COFINAL.CASED.REPLICATE.01
(EXPLORATION ONLY, experiments/.  NO RH claim, NO counterexample
claim, NO all-h statement.  2026-08-13.)

CCCVII dissected the h ~ 8200 legality transition and typed TWO cells
CASE D = REPLICATION-REQUIRED: h 9447 kz 196 (alpha 6.9285,
tau_ideal_ub -8.7460e-11) and h 9535 kz 526 (alpha 8.1602,
-1.3139e-10).  On those two cells the independently refined IDEAL
Galerkin matrix keeps a NEGATIVE witness under outward rounding, no
positive same-depth flank exists on the built set, the comb is
complete, the node accounting is exact and both inertia routes agree.
CCCVII stated the only admissible next step: NOTHING may be concluded
without THREE INDEPENDENT BUILDS.  This probe executes them.

WHAT IS ACTUALLY BEING REPLICATED (stated in full BEFORE any
measurement; all of it is exact algebra of the deployed pipeline and
none of it is new mathematics).

 (0) THE OBJECT.  A cell is (kz, alpha = u_kz, M, D = 2 alpha / M,
     h = M/2).  The deployed lag profile is
        c_r = A(rD, D) + c^atom_r ,   r = 0..M-1,
     A the archimedean Weil kernel and
        c^atom_r = -(1/2) sum_n mu_n tent_r(log n),  mu_n = 2 L(n)/sqrt n
     over prime powers n with log n <= 2 alpha (tent_r the hat at rD
     of width D).  The deployed builder symmetrises c to length
     L = 2M - 2, takes d = Re FFT(c^sym), splits the folded circle
     into a POSITIVE and a NEGATIVE arm and assembles
        A_wall = I - sqrt(V) P P^T sqrt(V),  P[j,k] = p_k(y_j), k < h,
     with {p_k} the mu_+-orthonormal chain.  tau = lam_min(A_wall).

 (I) THE BASIS-FREE FORM.  The nodes of BOTH arms are the M
     Chebyshev-Lobatto points x_k = cos(theta_k), theta_k = pi k/(M-1)
     = 2 pi k / L, with signed masses
        W_k = eps_k d_k 4 sin^2(theta_k/2) / (2L),  eps_0 = eps_{M-1}
        = 1, else 2,
     mu_+ = the W_k > 0 part, mu_- = the |W_k| of the W_k < 0 part.
     Because the chain columns are a triangular degree-graded family,
     span{p_0..p_{h-1}} IS the degree-<h polynomial space, so the
     IDEAL (metric-corrected) wall scalar is BASIS-FREE:
        tau_ideal = 1 - sup_{deg q < h} int q^2 dmu_- / int q^2 dmu_+
                  = lam_min(Omega, O),
        O[m,m'] = int T_m T_m' dmu_+ , H = int T_m T_m' dmu_- ,
        Omega = O - H,   T_m the Chebyshev polynomials.
     THE DECISIVE CONSEQUENCE, and the reason this probe is cheap:
     a NEGATIVE tau_ideal is exactly the statement
        EXISTS q of degree < h with  Q[q] := int q^2 dmu_+
                                            - int q^2 dmu_- < 0,
     and Q[q] is a SCALAR that can be certified by outward-rounded
     summation.  The certificate does NOT depend on how q was found.
     Positivity of the ideal object is NOT certified anywhere here
     (the honest CCCVII asymmetry is inherited verbatim).

 (II) THE WEIL KERNEL IN CLOSED FORM (the PATH-3 enabler).  With
     Phi(theta) = 4 sin^2(theta/2) q(cos theta)^2 one has EXACTLY
        Q[q] = (1/2) sum_{r=0}^{M-1} phi_r c_r ,
     phi_r the cosine coefficients of Phi, because
     (1/(2L)) sum_j d_j cos(r theta_j) = c_r / 2 on r <= M-1.
     Equivalently, entry by entry,
        Omega[m,m'] = (1/2) ( G_{m+m'} + G_{|m-m'|} ),
        G_r = c_r - (c_{r+1} + c_{|r-1|}) / 2 ,
     a TOEPLITZ-PLUS-HANKEL matrix built from the lag profile ALONE:
     no FFT, no folding, no quadrature, no chain, no arm split.  This
     is the localized Weil form's kernel in the Chebyshev coordinate,
     i.e. the CLXXXVII dictionary object (the finite odd
     Fejer/autocorrelation spline cone inside the
     Guinand-Weil/Bombieri/Suzuki localized Weil class) restricted to
     degree < h.  It makes PATH 3 IMMUNE to the one scope edge CCCVII
     left open by name -- the accuracy with which the evaluated CHAIN
     columns represent polynomials -- because it never evaluates a
     chain at all.

 (III) THE ARCHIMEDEAN KERNEL WITH A CERTIFIED TAIL (the PATH-2
     enabler).  The deployed A(s, D) is a 48-point Gauss-Legendre
     quadrature of
        A = -(gam + log pi) tri(s)
            + 2 int_0^inf [tri(s) e^{-2w} - S(w) e^{-w/2}]
                          / (1 - e^{-2w}) dw,
        tri(x) = max(0, 1 - |x|/D),  S(w) = (tri(s-w) + tri(s+w))/2.
     Expanding 1/(1 - e^{-2w}) as a geometric series and integrating
     the piecewise-linear S EXACTLY gives, for s = dD,
        A(dD, D) = -[d = 0](gam + log pi + 3 log 2 + pi/2)
                   + (1/D) ( 2 Lc(dD) - Lc(|d-1| D) - Lc((d+1) D) ),
        Lc(t) = sum_{k>=0} e^{-(2k+1/2) t} / (2k+1/2)^2,
        Lc(0) = psi'(1/4)/4 = (pi^2 + 8 Catalan)/4  (closed form).
     Lc is summed with an ADAPTIVE term count and the RIGOROUS
     geometric tail bracket
        0 <= R_K(t) <= e^{-(2K+1/2)t} / ((2K+1/2)^2 (1 - e^{-2t})),
     driven below LERCH_TOL.  This is a genuinely different algorithm
     for the same kernel (series + closed-form tail vs. fixed-order
     quadrature) and it is the certified tail bracket the mission
     asks for.  The PRIME side needs no tail bracket at all: the tent
     support is exactly [0, 2 alpha], so every atom with log n >
     2 alpha contributes EXACTLY ZERO -- the truncation is exact and
     is warded (comb completeness) instead of bounded.

THE THREE PATHS (each with its own witness search and/or its own
certified evaluator; the 2 x 3 cross-census is the deliverable).

 PATH 1  PRIME-SIDE REBUILD.  Fresh code end to end: my own
    prime-power sieve and masses, my own archimedean kernel (the
    (III) series), my own vectorised tent assembly, my own symmetric
    extension and transform, my own arm split, and -- instead of the
    deployed Lanczos chain -- the CHEBYSHEV basis, whose Gram
    matrices O and H are formed by EXPLICIT weighted node sums
    (dgemm over the rebuilt nodes, not the Toeplitz shortcut).
    Witness W1 = the bottom generalized eigenvector of (Omega, O).
    Evaluator E1 = the rebuilt folded quadrature, outward rounded.
 PATH 2  EXPLICIT FORMULA WITH CERTIFIED TAIL BRACKET.  No matrix, no
    folding, no arm split, no quadrature frame: Q[q] = (1/2) sum_r
    phi_r c_r with phi obtained by EXACT polynomial algebra (FFT) and
    c split into the certified arch series (III) and a DIRECT SUM
    OVER PRIME POWERS Q_prime = -(1/2) sum_n mu_n Phi~(log n),
    Phi~ the piecewise-linear interpolant.  Evaluator E2.  The
    zero-side route is PRICED, not run: CLXXXVII measured that the
    first 2500 zeros capture only 0.48..0.85 of the zero side, so at
    a wall scalar of 1e-10 against a form of scale 1e-1 the zero
    sum is INFEASIBLE-AT-THIS-SCALE by nine orders; that is typed,
    never hidden.
 PATH 3  DIRECT SUZUKI/WEIL KERNEL.  The h x h Galerkin restriction
    Omega_weil assembled DIRECTLY from the lag profile by (II) on the
    DEPLOYED conventions (core.arch_lags + core.atom_lags_at, the
    CLXXXVII dictionary, read-only).  Witness W3 = its bottom
    eigenvector; inertia by the exact-sign Bunch-Kaufman block count
    (2x2 determinant/trace signs in exact rational arithmetic on the
    dyadic float64 entries).  Evaluator E3 = the bilinear form of
    the assembled kernel.  Immune to the chain-column scope edge.

FROZEN PROTOCOL.
 S0 firewall AST scan (banned zetazero / zetazeros / nzeros /
    primerange / isprime / primepi / nextprime / prevprime /
    factorint / primefactors); AC scan: the EVALUATOR functions
    (e1_quad, e2_explicit, e3_kernel, e3_th, e3_dense, node_values,
    cheb_coeffs, arch_series, lerch_grid, my_atom_lags,
    omega_weil_rows) see nodes, weights, entries, coefficients and
    frozen constants only -- no eigensolver, no inverse, no tau.
 T  the atom table to TAB2 = 1.6e7, warded BITWISE against the
    deployed 4e6 EXT prefix, and my own sieve warded BITWISE against
    the deployed von Mangoldt table.
 D  the deep census (deployed frame formula verbatim); gates: 587
    cells, h max 65051, all frozen priority keys present.
 CAL THE CALIBRATION WARD at a shallow TIE cell: (a) my rebuilt
    pipeline must tie the DEPLOYED builder's tau EXACTLY in sign and
    to CAL_RTOL relatively; (b) the four structural identities of
    (I)-(III) must hold at machine precision -- my tent assembly
    BITWISE against core.atom_lags_at, my arch series against
    core.arch_lags, Omega_weil against Omega_quad, and the
    Toeplitz-Hankel Gram against the direct node sum; (c) the three
    evaluators must agree on the SAME witness.
 ADM THE ADMISSIBILITY AUDIT (runs regardless, and it is the
    cheapest honest exit): every registered rule of the window
    family, checked pedantically per cell -- the kz range, the T105
    NU_MAIN = 4 frame relation D <= g_kz / NU_MAIN, the registered
    frame-A window range H_MIN..HCAP, the atom floor N_ATOM_MIN, the
    comb completeness against BOTH the deployed 4e6 prefix and the
    CCLXXIX 1.6e7 extension, the A8 reflection reachability, the
    folding/rank condition n_pos >= h, and the CLXXXVII test
    function class membership of the witness.  A rule that EXCLUDES
    a case-D cell resolves the case as a boundary-mapping error;
    a rule that the deep lane EXTENDS is typed RULE-EXTENDED, never
    silently passed as satisfied.
 CEN the four mission cells (D1 9447, D2 9535 FIRST, then the CASE-B
    calibration controls B1 8677, B2 9023) plus the POS control P0
    8629 as a stretch item behind the same guard.
 X  controls-must-fire: X1 the SCRAMBLE world and X2 the SMOOTH
    (prime-free) world at a TARGET cell must destroy the wall scalar
    on EVERY path; XA the arch-implementation swap must MOVE the
    scalar by less than the measured cross-path spread or the
    difference is typed; XW the certified enclosure must FIRE on a
    DOCTORED lag entry.
 S  screens: the CCXLVII tau-relocation and CCXVII c_h screens are
    VACUOUS-BY-CONSTRUCTION (no step formations of record, no fitted
    level -- replication census only) and are typed as such.

VERDICT (frozen enum, per case-D cell):
  REPLICATED-NEGATIVE  all three paths deliver a CERTIFIED negative
      enclosure of the wall scalar at a degree-<h witness.  The
      typed statement is then EXACTLY: the deployed window family's
      IDEAL form is indefinite at this cell.  The two readings, both
      stated neutrally and neither chosen: (R1) an
      admissibility/identification assumption of the family fails at
      this depth, or (R2) the form delivers a real negative Weil
      test.  The follow-up decision belongs to the lead.
  NOT-REPLICATED  at least one path disagrees in SIGN -- then the
      disagreement anatomy IS the finding and the differing
      convention/assumption is NAMED.
  UNRESOLVED  the certified enclosures straddle zero -- then the
      precision that would decide is stated.
KILLS: K1 pipeline -> PIPELINE-BROKEN; K2 ward/identity ->
WARD-BROKEN; K3 calibration -> CALIBRATION-BROKEN; K4 a required
control silent -> CONTROL-SILENT.

FROZEN BARS.  TAB2 = 1.6e7; EXT_DEPLOYED = 4e6; KZ2_MAX = 1200;
CENSUS_N_REF = 587; CENSUS_HMAX_REF = 65051; NU_MAIN = 4;
H_MIN = 128; HCAP = 1450; N_ATOM_MIN = 40; LERCH_TOL = 1e-19;
ETA_FFT = max(8 log2(N) u ||a||_1, ETA_SAFE * measured) with
ETA_SAFE = 8, measured against an exactly-rounded reference on
FFT_PROBE = 256 sampled nodes and warded on FFT_WARD2 = 96 DISJOINT
nodes (see AMENDMENT A14); TAU_NOISE = 5e-12; SIGN_MARGIN = 1 (a
certified enclosure decides a sign exactly when it excludes zero, and
the margin |Q| / halfwidth is printed for every read);
CAL_RTOL = 1e-3; IDENT_BAR = 1e-11
(the identity wards of CAL); ARCH_BAR = 1e-9 (my series vs the
deployed GL kernel, absolute); TENT_ULP = 8 (the summation-order floor
of the tent ward, see AMENDMENT A9); COEF_PROBE = 24, COEF_SAFE = 8
(the coefficient-transform ward, AMENDMENT A10); SCR_SEED = 1;
DOPE = 1e-3 (see AMENDMENT A13); CAL_TGT = 900; BUILD_CAP_S = 2400;
GUARD_FAC = 1.05;
COST_C_ENV = 2.0e-10 s.
Smoke: PRIO = two shallow census cells (h ~ 900 and ~ 1200), the
frontier cells SMOKE-SKIPPED (typed), verdict SMOKE.

HONEST AMENDMENTS (declared before the frozen run).
 A1 PRE-FREEZE RECONNAISSANCE, fully disclosed.  ONE throwaway script
    (_recon_cased.py, deleted after the freeze) was run TWICE at ONE
    shallow census cell (h 878 kz 52, alpha 5.1299, M 1756 -- NOT a
    mission cell, NOT in the band, NO frontier cell was built and NO
    frontier number was read).  It verified the four structural
    identities of (I)-(III) and it FOUND TWO ERRORS in the first
    draft of this probe, both repaired before the freeze and both
    disclosed here: (i) the cosine-transform route applied the fold
    multiplicity eps_k TWICE (once in the node weights and once in
    the symmetric extension), which inflated both Gram matrices by
    the endpoint factor; (ii) the Lerch series was summed with a
    FIXED 4000 terms, whose t = 0 tail is 6.25e-5 and which
    therefore missed the deployed A_0 by 2.14e-2 -- repaired by the
    closed form Lc(0) = psi'(1/4)/4 plus the adaptive count and the
    rigorous geometric tail bracket.  After the repairs the recon
    measured, at that shallow cell: arch |dev| 2.72e-12 (certified
    tail 6.6e-23), tent assembly dev EXACTLY 0.0 (bitwise), atoms
    3180 == 3180 with u and mu dev EXACTLY 0.0, Omega_weil vs
    Omega_quad dev 8.88e-16, Toeplitz-Hankel vs direct node sum dev
    1.55e-13, tau_ideal +2.2343238e-07 against the deployed tau
    +2.2343339e-07, the quadrature witness read 1 - N/D
    +2.2343200e-07 and the explicit-formula scalar +2.2343193e-07
    (dev 7.25e-14 against the quadrature route, on an arch/prime
    split of -5.3175e-02 / +5.3176e-02, i.e. SIX orders of
    cancellation).  That last number is the honest precision frame of
    PATH 2 and it is re-measured per cell.
 A2 THE DEPLOYED float64 tau of the four mission cells is NOT
    recomputed (each deep chain build is ~400 s and buys nothing the
    CCCVII record does not already carry digit-identically).  The
    CCCVII values are CITED as reference targets; what is replicated
    is the IDEAL tier, which is the object CCCVII typed CASE D.  The
    deployed builder IS run at the shallow CAL cell, where the tie is
    exact and cheap.
 A3 PATH 2 is an EVALUATOR path.  Its independence is in the
    EVALUATION (certified arch series + direct prime-power sum + exact
    polynomial algebra), not in the witness search, and this is
    mathematically complete: the certificate "EXISTS q of degree < h
    with Q[q] < 0" does not depend on the provenance of q.  PATH 2
    therefore certifies BOTH foreign witnesses and reports both.
 A4 PATH 3 uses the DEPLOYED archimedean and tent conventions
    (read-only imports) BY DESIGN -- it is the dictionary side.  The
    arch implementations therefore differ between {P1, P2} and {P3},
    and that difference is MEASURED (control XA) rather than
    assumed away: it is the single shared-ingredient seam of the
    census and it is printed.
 A5 The certified enclosures use OUTWARD rounding of the decisive
    scalars (rigorous gamma_n bounds on the actually accumulated
    absolute sums, exactly-rounded math.fsum for every decisive
    accumulation, and the certified arch tail).  The node values of
    the witness polynomial are computed by FFT and their error is
    bounded by the DECLARED model ETA_FFT, which is WARDED against
    an exactly-rounded dense reference on FFT_PROBE sampled nodes.
    A model that fails its ward is a WARD kill, not a footnote.
 A6 No interval enclosure of the full h x h matrices is attempted
    (h ~ 9.5e3); the outward rounding is applied to the DECISIVE
    SCALARS, exactly as CCCVII A2 did.
 A7 No ladder rebuild, no scorecard row, no promotion, no marker
    move.  Nothing measured here enters a certificate of record.
 A8 PATH 3 contracts the assembled kernel in its EXACT Toeplitz-Hankel
    coordinate, a^T Omega_weil a = sum_r G_r b_r with b the cosine
    coefficients of q^2 -- an algebraic identity, not an
    approximation, which lets the decisive scalar be summed with
    exactly-rounded fsum.  The DENSE h x h assembly is still built
    (it carries the witness search and the exact LDL inertia) and its
    bilinear form is printed as the E3-dense consistency read with the
    (deliberately crude) gamma_n bound.  Declared BEFORE the frozen
    run; the smoke printed both.
 A9 SMOKE REPAIR, disclosed.  The pre-freeze bar TENT_BITWISE = True
    was WRONG BY CONSTRUCTION: a vectorised tent accumulates the atom
    masses in a different ORDER than the deployed per-atom loop, so
    bitwise identity is unattainable for any independent
    implementation.  The smoke measured 4.441e-16 on a profile of
    scale 1.21 -- exactly the summation-order floor.  The bar is
    replaced by the principled TENT_ULP = 8 ulp of the profile scale.
    This LOOSENS a ward; it is disclosed as a repair of a
    mis-specified measurement, not as bar shopping, and the raw
    deviation is printed at every cell so the reader can re-judge.
A10 The coefficient half-widths of PATH 2 and PATH 3 were missing from
    the smoke enclosures (only the product rounding was priced).  They
    are now carried: max_r |dphi_r| times ||c||_1, the worst case over
    sign patterns.  The transform half-width is MEASURED, not modelled
    a priori -- max_r |phi_r^fft - phi_r^exact| over COEF_PROBE = 24
    sampled orders against exactly-rounded direct summation, times the
    safety factor COEF_SAFE = 8 -- and WARDED against a DISJOINT
    second sample of 24 orders.  This is the same species of declared
    -and-warded numerical model as ETA_FFT (A5).  This WIDENS the
    E2/E3 enclosures relative to the smoke.
A12 PATH 3 is contracted in the STABLE coordinate
    (1/2) sum_r phi_r c_r rather than the b-coordinate
    sum_r G_r b_r.  Reason, measured at the smoke: the witness has
    ||a||_2 = 1 but ||a||_1 ~ sqrt(h), so q peaks near theta = 0 and
    the transform error of the q^2 coefficients b is ~1e-13, whereas
    the factor 4 sin^2(theta/2) in phi annihilates exactly that peak
    and drives the phi transform error to ~1e-18.  BOTH contractions
    are computed and printed for every witness, together with the
    bilinear form of the ASSEMBLED h x h matrix; they must agree
    inside their enclosures (ward CAL8).  The consequence for
    independence is stated plainly and NOT dressed up: PATHS 2 and 3
    are the same scalar in two coordinates, so what separates them is
    the INPUT (my certified arch series + my comb versus the deployed
    Gauss-Legendre kernel + the deployed comb) and the contracted
    object, not the arithmetic.  PATH 1 is the genuinely different
    route (rebuilt signed quadrature, never a lag contraction).
A15 VERDICT-TAXONOMY CORRECTION, disclosed.  The pre-freeze typing
    left a hole: a case-D cell whose census comes out CERTIFIED
    POSITIVE on every path fell through to CASED-UNRESOLVED, although
    in the mission's own taxonomy that is exactly the NOT-REPLICATED
    outcome -- the CCCVII negative witness was not reproduced by any
    independent build.  The typing now reads the SIGN of the CCCVII
    reference and reports NOT-REPLICATED in that case, with the
    disagreement anatomy printed per cell as the mission requires.
    No numeric changed; this is a labelling correction only, and the
    per-read signs and enclosures are printed unchanged beside it.
A14 FROZEN-RUN REPAIR, disclosed in full, TWO mis-specified bars.
    (i) The A5 a-priori FFT node model ETA_FFT = 8 log2(N) u ||a||_1
    HELD at the shallow calibration cell (h 878) and FAILED at the
    mission cells (h ~ 9.5e3): the first frozen run measured
    deviations up to 3.6e-12 against a model value of 9.4e-13, i.e.
    under-priced by up to ~4x.  The ward existed but was only CHECKED
    at the calibration cell, so it printed the violation without
    killing.  Both halves are repaired: the half-width is now
    max(a-priori model, 8 * measured), and EVERY model ward is
    enforced at EVERY built census cell (new check ADM2), warded on a
    DISJOINT node sample.  This WIDENS the E1 enclosures.
    (ii) SIGN_BAR = 1e-13 was an ABSOLUTE bar set at the tau scale,
    but the wall scalar at ||a||_2 = 1 lives at the tau * D_plus
    scale ~1e-15 because the positive mass D_plus ~ 1e-4 at these
    cells.  It therefore typed EVERY read STRADDLE whatever the
    arithmetic did -- a bar that decides nothing.  It is replaced by
    the mathematically complete criterion for an outward-rounded
    enclosure: the sign is decided exactly when the enclosure
    EXCLUDES ZERO (SIGN_MARGIN = 1), and the margin |Q| / halfwidth
    is printed for every single read so any stricter personal bar can
    be applied by the reader.  DIRECTION OF THIS REPAIR, stated
    plainly: under the mis-scaled bar every cell was UNRESOLVED, i.e.
    the run concluded nothing; under the corrected criterion the
    census comes out POSITIVE, which REFUTES the CCCVII case-D
    negative witness this mission was sent to replicate.  The repair
    therefore moves AWAY from the exciting outcome, not towards it.
A13 SMOKE REPAIR, disclosed.  The pre-freeze DOPE = 1e-9 made the XW
    control TOOTHLESS BY CONSTRUCTION: the smoke measured a certified
    shift of 5.25e-19 against an enclosure half-width of 2.12e-15, so
    that control could never fire whatever the arithmetic did, and a
    silent control is worthless.  DOPE is raised, by the declared rule
    "the smallest power of ten whose certified shift clears the
    enclosure by the pass margin of 10", to 1e-2 -- a one percent
    error in ONE of M ~ 2e4 comb entries.  The PASS THRESHOLD (shift >
    10 * halfwidth) is UNCHANGED; only the stimulus was rescaled, so
    this is not bar shopping.  This STRENGTHENS a control (it now
    fires); it is
    disclosed as a repair of a mis-scaled control, and the raw shift
    and half-width are both printed so the reader can re-judge.
A11 On the SCRAMBLED / DOPED control worlds the positive arm can lose
    numerical definiteness, so the PATH-1 pencil eigensolve refuses.
    The witness is then taken from the standard eigenproblem of the
    same Omega and the row is typed STD-FALLBACK.  This affects
    CONTROL worlds only; it is printed wherever it fires.

NO RH claim.  NO counterexample claim.  No paper, ledger, website,
manifest or verification file is touched; the only edit outside this
file is the German CCCXV line prepended to experiments/next.txt AFTER
the frozen summary.

Sources (read-only): v563_paper2_readouts (CCVII/deployed generators:
von_mangoldt_table, arch_lags, arch_A, atom_lags_at, NU_MAIN, H_MIN,
HCAP, N_ATOM_MIN), onebadmode_moments_probe (CCVII pipeline:
build_ext_tables, grid_density, folded_measure_full, lanczos_chain,
eval_chain, smooth_masses), cofinal_dissect_probe (CCCVII: the case
data and the reproduction targets, quoted as constants only),
w2_classical_identity_probe (CLXXXVII: the Weil-form dictionary and
the test-function class), j16_verified_zero_supply_probe (CLXXXIX:
the explicit-formula tail paradigm).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/cased_replicate_probe.py --smoke
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/cased_replicate_probe.py
"""

import ast
import hashlib
import math
import os
import sys
import time
from fractions import Fraction

import numpy as np
import scipy.linalg as sla

_HERE = os.path.dirname(os.path.abspath(__file__))
_VERIFY = os.path.abspath(os.path.join(_HERE, "..", "..", "verification"))
sys.path.insert(0, _HERE)
sys.path.insert(0, _VERIFY)

import onebadmode_moments_probe as ob        # noqa: E402 (READ-ONLY)
import v563_paper2_readouts as core          # noqa: E402 (READ-ONLY)

# ------------------------------------------------------- frozen bars
TAB2 = 16_000_000
EXT_DEPLOYED = 4_000_000
KZ2_MAX = 1200
CENSUS_N_REF = 587
CENSUS_HMAX_REF = 65051
NU_MAIN = 4
H_MIN, HCAP = 128, 1450
N_ATOM_MIN = 40
LERCH_TOL = 1.0e-19
FFT_PROBE = 256
COEF_PROBE = 24
COEF_SAFE = 8.0
TENT_ULP = 8.0
TAU_NOISE = 5.0e-12
SIGN_MARGIN = 1.0
ETA_SAFE = 8.0
FFT_WARD2 = 96
CAL_RTOL = 1.0e-3
IDENT_BAR = 1.0e-11
ARCH_BAR = 1.0e-9
SCR_SEED = 1
DOPE = 1.0e-2
CAL_TGT = 900
BUILD_CAP_S = 2400.0
GUARD_FAC = 1.05
COST_C_ENV = 2.0e-10
EPS64 = float(np.finfo(float).eps)
U_RND = 0.5 * EPS64

EULER = 0.5772156649015328606065120900824
CATALAN = 0.915965594177219015054603514932384110774
PSI1_Q = math.pi ** 2 + 8.0 * CATALAN                 # psi'(1/4)
ARCH_CONST = EULER + math.log(math.pi) + 3.0 * math.log(2.0) \
    + math.pi / 2.0

# the CCCVII record, quoted as reference targets (never recomputed here)
#   key -> (h, kz, alpha_ref, tau_deployed, tau_ideal_ub_ref, case)
CCCVII = {
    "D1": (9447, 196, 6.9285, -1.412e-10, -8.7460e-11, "D"),
    "D2": (9535, 526, 8.1602, -1.743e-10, -1.3139e-10, "D"),
    "B1": (8677, 299, 7.4622, -3.053e-10, -3.0093e-10, "B"),
    "B2": (9023, 506, None, -1.498e-10, -6.2463e-11, "B"),
    "P0": (8629, 223, 7.1009, +7.245e-10, None, "0"),
}
PRIO_KEYS = ("D1", "D2", "B1", "B2", "P0")

BANNED_IDS = ("zetazero", "zetazeros", "nzeros", "primerange",
              "isprime", "primepi", "nextprime", "prevprime",
              "factorint", "primefactors")
READER_BANNED = ("tau", "eig", "eigs", "eigh", "eigvals", "eigvalsh",
                 "inv", "pinv", "solve", "lu_factor", "lu_solve",
                 "ldl", "svd", "cond")
READER_FUNCS = ("e1_quad", "e2_explicit", "e3_kernel", "e3_th",
                "e3_dense", "node_values", "arch_series", "lerch_grid",
                "my_atom_lags", "omega_weil_rows", "cheb_coeffs")

CHECKS = []
KILLS = []
T0 = time.time()
SMOKE = "--smoke" in sys.argv[1:]
SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()


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


def ast_scan_functions(names, banned):
    src = open(os.path.abspath(__file__), encoding="utf-8").read()
    bad = []
    for node in ast.walk(ast.parse(src)):
        if isinstance(node, ast.FunctionDef) and node.name in names:
            for sub in ast.walk(node):
                nm = None
                if isinstance(sub, ast.Name):
                    nm = sub.id
                elif isinstance(sub, ast.Attribute):
                    nm = sub.attr
                elif isinstance(sub, ast.arg):
                    nm = sub.arg
                if nm and nm in banned:
                    bad.append("%s:%s" % (node.name, nm))
    return bad


def gamma_n(nterms):
    prod = nterms * U_RND
    if prod >= 0.5:
        return float("inf")
    return prod / (1.0 - prod)


def fsum_dot(av, bv):
    """Exactly-rounded sum of the products a_i b_i plus a RIGOROUS
    outward half-width for the product roundings."""
    pr = np.asarray(av, float) * np.asarray(bv, float)
    val = math.fsum(pr.tolist())
    wid = U_RND * math.fsum(np.abs(pr).tolist())
    return val, wid


def ldl_inertia(dblk):
    """EXACT block inertia of a Bunch-Kaufman LDL^T factor: 1x1 pivots
    contribute their sign, a 2x2 block contributes one negative
    eigenvalue iff det < 0 and two iff det > 0 with negative trace,
    the determinant sign decided in EXACT rational arithmetic on the
    dyadic float64 entries (CCCVII A13 verbatim)."""
    dd = np.diag(dblk)
    sub = np.diag(dblk, k=1)
    ndim = len(dd)
    n_neg = n_zero = n_two = 0
    i = 0
    while i < ndim:
        if i + 1 < ndim and sub[i] != 0.0:
            aa = Fraction(float(dd[i]))
            bb = Fraction(float(sub[i]))
            cc = Fraction(float(dd[i + 1]))
            det = aa * cc - bb * bb
            tr = aa + cc
            if det < 0:
                n_neg += 1
            elif det > 0:
                if tr < 0:
                    n_neg += 2
            else:
                n_zero += 1
                if tr < 0:
                    n_neg += 1
            n_two += 1
            i += 2
        else:
            if dd[i] < 0.0:
                n_neg += 1
            elif dd[i] == 0.0:
                n_zero += 1
            i += 1
    return n_neg, n_zero, n_two


# =============================================== (III) the arch kernel
def lerch_grid(D, njmax):
    """Lc(jD) for j = 0..njmax.  Lc(0) is the CLOSED FORM psi'(1/4)/4;
    every j >= 1 is an adaptive partial sum whose omitted geometric
    tail is bounded OUTWARD by tailw (the certified tail bracket).
    Frozen constants and the grid step only."""
    out = np.zeros(njmax + 1)
    tailw = np.zeros(njmax + 1)
    out[0] = 0.25 * PSI1_Q
    j = 1
    while j <= njmax:
        j2 = min(njmax, 2 * j - 1)
        t0 = j * D
        kk = 64
        while True:
            lam = 2.0 * kk + 0.5
            bnd = math.exp(-lam * t0) / (lam * lam
                                         * (-math.expm1(-2.0 * t0)))
            if bnd <= LERCH_TOL or kk > 8_000_000:
                break
            kk *= 2
        lam = 2.0 * np.arange(kk, dtype=float) + 0.5
        tt = np.arange(j, j2 + 1, dtype=float) * D
        out[j:j2 + 1] = np.exp(-np.outer(tt, lam)) @ (1.0 / lam ** 2)
        lam_k = 2.0 * kk + 0.5
        tailw[j:j2 + 1] = np.exp(-lam_k * tt) / (
            lam_k ** 2 * (-np.expm1(-2.0 * tt)))
        j = j2 + 1
    return out, tailw


def arch_series(M, D):
    """A(dD, D), d = 0..M-1, by the (III) Hurwitz/Lerch series, with
    the outward tail half-width of every entry."""
    lv, tw = lerch_grid(D, M)
    out = np.empty(M)
    err = np.empty(M)
    out[0] = -ARCH_CONST + (2.0 * lv[0] - 2.0 * lv[1]) / D
    err[0] = 2.0 * tw[1] / D
    dc = np.arange(1, M)
    out[1:] = (2.0 * lv[dc] - lv[dc - 1] - lv[dc + 1]) / D
    err[1:] = (2.0 * tw[dc] + tw[dc - 1] + tw[dc + 1]) / D
    return out, err


# ============================================ (0) my own prime comb
def my_von_mangoldt(nmax):
    """Own sieve of Eratosthenes + prime-power tower.  Returns the
    atom positions u = log n and masses mu = 2 Lambda(n)/sqrt n."""
    sieve = np.ones(nmax + 1, dtype=bool)
    sieve[:2] = False
    for i in range(2, int(math.isqrt(nmax)) + 1):
        if sieve[i]:
            sieve[i * i::i] = False
    lam = np.zeros(nmax + 1)
    for p in np.nonzero(sieve)[0]:
        p = int(p)
        lp = math.log(p)
        q = p
        while q <= nmax:
            lam[q] = lp
            q *= p
    nn = np.nonzero(lam > 0.0)[0]
    return nn, np.log(nn.astype(float)), \
        2.0 * lam[nn] / np.sqrt(nn.astype(float))


def my_atom_lags(alpha, M, uu, mm):
    """My vectorised T115 tent assembly (the deployed loop, but with
    np.add.at).  Positions, masses, the grid step and frozen
    constants only."""
    D = 2.0 * alpha / M
    c = np.zeros(M)
    i0 = np.floor(uu / D).astype(np.int64)
    for off in (-2, -1, 0, 1, 2):
        idx = i0 + off
        ok = (idx >= 0) & (idx < M)
        if not np.any(ok):
            continue
        vv = 1.0 - np.abs(idx[ok] * D - uu[ok]) / D
        good = vv > 0.0
        np.add.at(c, idx[ok][good], -mm[ok][good] * 0.5 * vv[good])
    # the u < D tent reflection (A8: unreachable for the true comb)
    refl = np.nonzero(uu < D)[0]
    for j in refl:
        u_j, m_j = float(uu[j]), float(mm[j])
        for i in range(0, min(M, int(math.floor((D - u_j) / D)) + 2)):
            v = 1.0 - (i * D + u_j) / D
            if v > 0.0:
                c[i] -= m_j * 0.5 * v
    return c


# ================================= (I) the nodes, weights, arm split
def node_frame(lag, M):
    """The M Chebyshev-Lobatto nodes, the SIGNED masses and the arm
    split.  Lag entries, frozen constants and the fold multiplicity
    only."""
    L = 2 * M - 2
    ext = np.concatenate([lag, lag[-2:0:-1]])
    dv = np.fft.fft(ext).real[:M]
    th = math.pi * np.arange(M) / (M - 1)
    eps = np.full(M, 2.0)
    eps[0] = 1.0
    eps[M - 1] = 1.0
    wsig = eps * dv * 4.0 * np.sin(th / 2.0) ** 2 / (2.0 * L)
    return th, wsig, dv, L


def node_values(avec, M, L):
    """q(x_k) = sum_{m<h} a_m cos(m theta_k) at the M Lobatto nodes,
    by ONE length-L FFT.  Coefficients and frozen constants only."""
    pad = np.zeros(L)
    pad[:len(avec)] = avec
    return np.fft.fft(pad).real[:M]


def cheb_coeffs(avec, M, L):
    """The cosine coefficients b_r of q^2 and phi_r of
    4 sin^2(theta/2) q(cos theta)^2, by EXACT polynomial algebra on a
    4L grid (no aliasing: deg Phi = M-1 << 2L).  Coefficients and
    frozen constants only."""
    nf = 4 * L
    pad = np.zeros(nf)
    pad[:len(avec)] = avec
    qv = np.fft.fft(pad).real
    thf = 2.0 * math.pi * np.arange(nf) / nf
    bh = np.fft.fft(qv * qv).real / nf
    ph = np.fft.fft(4.0 * np.sin(thf / 2.0) ** 2 * qv * qv).real / nf
    bb = np.concatenate([[bh[0]], 2.0 * bh[1:2 * (M // 2)]])
    pp = np.concatenate([[ph[0]], 2.0 * ph[1:M]])
    return bb, pp, qv, thf


def coef_dev(fnc, thf, idx, ref):
    """max_r |fft coefficient - exactly rounded coefficient| over the
    sampled r.  Coefficients and frozen constants only."""
    nf = len(fnc)
    dev = 0.0
    for r in idx:
        exact = 2.0 * math.fsum((fnc * np.cos(r * thf)).tolist()) / nf
        dev = max(dev, abs(exact - ref[r]))
    return dev


def omega_weil_rows(G, h, out):
    """(II) Omega[m,m'] = (G_{m+m'} + G_{|m-m'|})/2, assembled row by
    row from the lag-derived sequence G.  Lag entries only."""
    for m in range(h):
        row = out[m]
        np.add(G[m:m + h], 0.0, out=row)
        row[:m + 1] += G[m::-1]
        if m + 1 < h:
            row[m + 1:] += G[1:h - m]
        row *= 0.5
    return out


# ====================================================== the evaluators
def e1_quad(qv, wsig, eta):
    """EVALUATOR 1 -- the rebuilt folded quadrature.  Returns
    (Q, Q_halfwidth, Dplus, Dplus_lo) with OUTWARD rounding: eta is
    the certified absolute node-value half-width.  Node values,
    signed masses and frozen constants only."""
    aq = np.abs(qv)
    lo = np.maximum(aq - eta, 0.0) ** 2
    hi = (aq + eta) ** 2
    pos = wsig > 0.0
    neg = wsig < 0.0
    wp = wsig[pos]
    wn = -wsig[neg]
    d_lo = math.fsum((wp * lo[pos]).tolist())
    d_hi = math.fsum((wp * hi[pos]).tolist())
    n_lo = math.fsum((wn * lo[neg]).tolist())
    n_hi = math.fsum((wn * hi[neg]).tolist())
    rnd = U_RND * (math.fsum(np.abs(wp * hi[pos]).tolist())
                   + math.fsum(np.abs(wn * hi[neg]).tolist()))
    q_lo = d_lo - n_hi - rnd
    q_hi = d_hi - n_lo + rnd
    return 0.5 * (q_lo + q_hi), 0.5 * (q_hi - q_lo), \
        0.5 * (d_lo + d_hi), d_lo - rnd


def e2_explicit(phi, phi_dev, cn1, arch, arch_err, uu, mm, M, D):
    """EVALUATOR 2 -- the EXPLICIT FORMULA.  Q = (arch + prime)/2 with
    arch = sum_r phi_r A_r (certified tail bracket arch_err) and
    prime = -(1/2) sum_n mu_n Phi~(log n) a DIRECT sum over prime
    powers whose truncation is EXACT (tent support [0, 2 alpha]).
    The COEFFICIENT half-width enters ONCE, worst case over sign
    patterns: |sum_r dphi_r c_r| <= max_r|dphi_r| * ||c||_1 with c the
    FULL lag profile (arch + comb).  Coefficients, kernel entries,
    positions, masses and frozen constants only."""
    a_val, a_wid = fsum_dot(phi, arch)
    a_wid += math.fsum((np.abs(phi) * arch_err).tolist())
    i0 = np.floor(uu / D).astype(np.int64)
    fr = uu / D - i0
    ext = np.zeros(M + 2)
    ext[:M] = phi
    i0c = np.minimum(np.maximum(i0, 0), M + 1)
    i1c = np.minimum(np.maximum(i0 + 1, 0), M + 1)
    tilde = (1.0 - fr) * ext[i0c] + fr * ext[i1c]
    p_val, p_wid = fsum_dot(mm, tilde)
    p_val *= -0.5
    p_wid = 0.5 * p_wid + 2.0 * U_RND * math.fsum(
        np.abs(mm * tilde).tolist())
    return (0.5 * (a_val + p_val),
            0.5 * (a_wid + p_wid) + 0.5 * phi_dev * cn1, a_val, p_val)


def e3_kernel(phi, phi_dev, lag_dep, c1n):
    """EVALUATOR 3 -- the assembled Weil-kernel Galerkin restriction,
    contracted against the DEPLOYED lag profile in its stable
    coordinate:  a^T Omega_weil a = (1/2) sum_r phi_r c_r.
    Kernel entries, coefficients and frozen constants only."""
    nr = min(len(phi), len(lag_dep))
    val, wid = fsum_dot(phi[:nr], lag_dep[:nr])
    return 0.5 * val, 0.5 * (wid + phi_dev * c1n)


def e3_th(bcoef, b_dev, gseq):
    """The Toeplitz-Hankel CONSISTENCY read of PATH 3:
       a^T Omega_weil a = sum_r G_r b_r ,
    b the cosine coefficients of q^2 and G the lag-derived kernel
    sequence.  Kernel entries and coefficients only."""
    nr = min(len(bcoef), len(gseq))
    val, wid = fsum_dot(gseq[:nr], bcoef[:nr])
    wid += b_dev * math.fsum(np.abs(gseq[:nr]).tolist())
    return val, wid


def e3_dense(avec, omega, blk=1024):
    """The CONSISTENCY read of PATH 3: the same bilinear form taken
    on the ASSEMBLED h x h matrix, with the rigorous (and deliberately
    crude) gamma_n bound on the accumulated absolute sums."""
    hdim = len(avec)
    absacc = 0.0
    parts = []
    aabs = np.abs(avec)
    for lo in range(0, hdim, blk):
        hi = min(hdim, lo + blk)
        parts.append(float(avec[lo:hi] @ (omega[lo:hi] @ avec)))
        absacc += float(aabs[lo:hi] @ (np.abs(omega[lo:hi]) @ aabs))
    return math.fsum(parts), gamma_n(hdim + 1) * absacc


# ===================================================== tables + census
DEEP = {}


def build_tables():
    section("T -- the atom table to TAB2 = %.3g, warded BITWISE "
            "against the deployed 4e6 prefix AND against the deployed "
            "von Mangoldt generator" % TAB2)
    ob.build_ext_tables()
    nn, u2, mu2 = my_von_mangoldt(TAB2)
    n_pref = len(ob.EXT["NN"])
    ok = (np.array_equal(nn[:n_pref], ob.EXT["NN"])
          and np.array_equal(u2[:n_pref], ob.EXT["U"])
          and np.array_equal(mu2[:n_pref], ob.EXT["MU"]))
    check("T1 my own sieve reproduces the deployed EXT arrays BITWISE "
          "on the 4e6 prefix (%d of %d atoms)" % (n_pref, len(nn)),
          ok, kill="K2")
    lam_dep = core.von_mangoldt_table(200_000)
    nnd = np.nonzero(lam_dep > 0.0)[0]
    check("T2 my sieve reproduces core.von_mangoldt_table BITWISE on "
          "its own 2e5 window (%d atoms)" % len(nnd),
          np.array_equal(nn[:len(nnd)], nnd), kill="K2")
    DEEP["NN"] = nn
    DEEP["U"] = u2
    DEEP["MU"] = mu2
    DEEP["G"] = np.diff(u2)


def deep_census():
    section("D -- the deep-frame census (deployed formula verbatim)")
    u2, g2 = DEEP["U"], DEEP["G"]
    out = []
    for kz in range(2, min(KZ2_MAX, len(u2) - 1)):
        alpha = float(u2[kz])
        d_k = 0.5 * float(g2[kz]) / float(NU_MAIN)
        mz = int(math.ceil(alpha / d_k - 1.0e-9)) + 1
        if mz % 2:
            mz += 1
        x_val = math.exp(2.0 * alpha)
        if x_val <= TAB2:
            out.append(dict(h=mz // 2, kz=kz, alpha=alpha, M=mz,
                            X=x_val, d_k=d_k, gap=float(g2[kz])))
    out.sort(key=lambda c: (c["h"], c["kz"]))
    hs = np.asarray([c["h"] for c in out], float)
    keys = {(c["h"], c["kz"]) for c in out}
    need = [(v[0], v[1]) for v in CCCVII.values()]
    ok_keys = all(k in keys for k in need)
    check("D1 census reproduces CCXCIX/CCCV/CCCVII: %d == %d cells, "
          "h max %d == %d, all %d mission keys present (%s)"
          % (len(out), CENSUS_N_REF, int(hs.max()), CENSUS_HMAX_REF,
             len(need), ok_keys),
          len(out) == CENSUS_N_REF and int(hs.max()) == CENSUS_HMAX_REF
          and ok_keys, kill="K1")
    return out


# ================================================= the per-cell build
def build_lags(cell, world=None, scr_seed=None, dope=False):
    """Both lag profiles of a cell: MINE (own sieve, own arch series,
    own vectorised tent) and DEPLOYED (core.arch_lags +
    core.atom_lags_at), on the same window data."""
    u2, mu2 = DEEP["U"], DEEP["MU"]
    alpha, M = cell["alpha"], cell["M"]
    ka = int(np.searchsorted(u2, 2.0 * alpha + 1.0e-14, side="right"))
    uu = u2[:ka].copy()
    mm = mu2[:ka].copy()
    if world == "smooth":
        mm = ob.smooth_masses(uu)
    elif world == "scramble":
        rng = np.random.default_rng(scr_seed)
        uu = np.sort(rng.uniform(0.0, 2.0 * alpha, size=ka))
    D = 2.0 * alpha / M
    t_a = time.time()
    a_mine, a_err = arch_series(M, D)
    a_dep = np.asarray(core.arch_lags(M, D), float)
    t_arch = time.time() - t_a
    c_mine_at = my_atom_lags(alpha, M, uu, mm)
    c_dep_at = np.asarray(core.atom_lags_at(alpha, M, uu, mm)[0], float)
    tent_dev = float(np.max(np.abs(c_mine_at - c_dep_at)))
    lag_mine = a_mine + c_mine_at
    lag_dep = a_dep + c_dep_at
    if dope:
        lag_mine = lag_mine.copy()
        lag_dep = lag_dep.copy()
        lag_mine[M // 3] *= (1.0 + DOPE)
        lag_dep[M // 3] *= (1.0 + DOPE)
    return dict(alpha=alpha, M=M, D=D, h=M // 2, uu=uu, mm=mm,
                arch_mine=a_mine, arch_err=a_err, arch_dep=a_dep,
                lag_mine=lag_mine, lag_dep=lag_dep,
                arch_dev=float(np.max(np.abs(a_mine - a_dep))),
                arch_tail=float(np.max(a_err)), tent_dev=tent_dev,
                at_scale=float(np.max(np.abs(c_dep_at))),
                n_atom=int(ka), t_arch=t_arch)


def eta_of(avec, L, M):
    """The DECLARED FFT forward-error model half-width for the node
    values (bar ETA_FFT = 8 log2(L) u ||a||_1)."""
    return 8.0 * math.log2(max(4, L)) * U_RND * float(
        math.fsum(np.abs(avec).tolist()))


def fft_ward(avec, qv, th, idx):
    """MEASURE the FFT node-value deviation against an exactly-rounded
    dense reference on the sampled nodes idx."""
    mi = np.arange(len(avec), dtype=float)
    worst = 0.0
    for k in idx:
        ref = math.fsum((avec * np.cos(mi * th[k])).tolist())
        worst = max(worst, abs(ref - float(qv[k])))
    return worst


def run_cell(tag, cell, world=None, scr_seed=None, dope=False,
             want_dep_tau=False):
    """The three paths on one cell.  Returns the full census row."""
    t_c = time.time()
    dat = build_lags(cell, world=world, scr_seed=scr_seed, dope=dope)
    M, h, D = dat["M"], dat["h"], dat["D"]
    row = dict(tag=tag, cell=cell, world=world, dat=dat)

    # ---------- PATH 1: the fresh rebuild (own lag, own arm split,
    #            Chebyshev Gram matrices by EXPLICIT node sums)
    th, wsig, dv, L = node_frame(dat["lag_mine"], M)
    pos = wsig > 0.0
    neg = wsig < 0.0
    row["n_pos"] = int(pos.sum())
    row["n_neg"] = int(neg.sum())
    row["n_zero"] = int(M - pos.sum() - neg.sum())
    mi = np.arange(h)
    cp = np.cos(np.outer(th[pos], mi))
    cn = np.cos(np.outer(th[neg], mi))
    omat = (cp.T * wsig[pos]) @ cp
    hmat = (cn.T * (-wsig[neg])) @ cn
    del cp, cn
    omat = 0.5 * (omat + omat.T)
    hmat = 0.5 * (hmat + hmat.T)
    om1 = omat - hmat
    del hmat
    t_b = time.time()
    try:
        w1v, w1 = sla.eigh(om1, omat, subset_by_index=[0, 0])
        row["p1_pencil"] = "GEN"
    except Exception:                                 # noqa: BLE001
        # the positive arm lost numerical definiteness (this happens on
        # the SCRAMBLED / DOPED control worlds, never on a real cell);
        # the witness is then taken from the standard eigenproblem --
        # the evaluators do not care where the vector came from.
        w1v, w1 = sla.eigh(om1, subset_by_index=[0, 0])
        row["p1_pencil"] = "STD-FALLBACK"
    a1 = np.ascontiguousarray(w1[:, 0])
    a1 = a1 / float(np.linalg.norm(a1))
    row["lam1_gen"] = float(w1v[0])
    row["t_p1_eig"] = time.time() - t_b
    del om1
    row["o_scale"] = float(np.max(np.abs(omat)))

    # ---------- PATH 3: the direct Weil kernel from the lag profile
    t_b = time.time()
    lag_d = dat["lag_dep"]
    aext = np.concatenate([lag_d, [lag_d[M - 2]]])
    rr = np.arange(2 * h)
    gseq = aext[rr] - 0.5 * (aext[rr + 1] + aext[np.abs(rr - 1)])
    om3 = np.empty((h, h))
    omega_weil_rows(gseq, h, om3)
    row["weil_vs_quad"] = float("nan")
    w3v, w3 = sla.eigh(om3, subset_by_index=[0, 0])
    a3 = np.ascontiguousarray(w3[:, 0])
    a3 = a3 / float(np.linalg.norm(a3))
    row["lam3_std"] = float(w3v[0])
    row["t_p3_eig"] = time.time() - t_b
    try:
        _l, dblk, _p = sla.ldl(om3, lower=True)
        nneg, nzero, ntwo = ldl_inertia(dblk)
        row["inertia"] = dict(n_neg=nneg, n_zero=nzero, n_2x2=ntwo,
                              agree=bool((nneg > 0) ==
                                         (float(w3v[0]) < 0.0)))
        del dblk, _l
    except Exception as exc:                          # noqa: BLE001
        row["inertia"] = dict(refused=type(exc).__name__, agree=False)

    # ---------- the 2 x 3 CROSS-CENSUS
    rng = np.random.default_rng(SCR_SEED)
    cn1 = math.fsum(np.abs(dat["lag_mine"]).tolist())
    cd1 = math.fsum(np.abs(dat["lag_dep"]).tolist())
    cen = {}
    for wname, avec in (("W1", a1), ("W3", a3)):
        eta_mod = eta_of(avec, L, M)
        qv = node_values(avec, M, L)
        nidx = sorted(set(int(x) for x in rng.choice(
            M, size=min(FFT_PROBE, M), replace=False)))
        wdev = fft_ward(avec, qv, th, nidx)
        eta = max(eta_mod, ETA_SAFE * wdev)
        n2 = sorted(set(int(x) for x in rng.choice(
            M, size=min(FFT_WARD2, M), replace=False)) - set(nidx))
        wdev2 = fft_ward(avec, qv, th, n2)
        bb, phi, qf, thf = cheb_coeffs(avec, M, L)
        ridx = sorted(set(int(x) for x in rng.choice(
            M, size=min(COEF_PROBE, M), replace=False)))
        sq = qf * qf
        pfn = 4.0 * np.sin(thf / 2.0) ** 2 * sq
        d_phi = coef_dev(pfn, thf, ridx, phi)
        d_bb = coef_dev(sq, thf, [r for r in ridx if r < len(bb)], bb)
        # the DISJOINT re-measurement that wards the declared model
        r2 = sorted(set(int(x) for x in rng.choice(
            M, size=min(COEF_PROBE, M), replace=False)) - set(ridx))
        w_phi = coef_dev(pfn, thf, r2, phi)
        w_bb = coef_dev(sq, thf, [r for r in r2 if r < len(bb)], bb)
        phi_dev = COEF_SAFE * d_phi
        b_dev = COEF_SAFE * d_bb
        q1, d1, dp, dp_lo = e1_quad(qv, wsig, eta)
        q2, d2, av, pv = e2_explicit(phi, phi_dev, cn1,
                                     dat["arch_mine"],
                                     dat["arch_err"], dat["uu"],
                                     dat["mm"], M, D)
        q3, d3 = e3_kernel(phi, phi_dev, dat["lag_dep"], cd1)
        q3t, d3t = e3_th(bb, b_dev, gseq)
        q3d, d3d = e3_dense(avec, om3)
        # the arch-implementation swap (control XA)
        q2s, _d2s, _a, _p = e2_explicit(phi, phi_dev, cn1,
                                        dat["arch_dep"],
                                        np.zeros(M), dat["uu"],
                                        dat["mm"], M, D)
        cen[wname] = dict(eta=eta, eta_mod=eta_mod, fft_dev=wdev,
            fft_dev2=wdev2, a1n=float(
            math.fsum(np.abs(avec).tolist())),
            E1=(q1, d1), E2=(q2, d2), E3=(q3, d3),
            E3t=(q3t, d3t), E3d=(q3d, d3d),
            phi_dev=phi_dev, b_dev=b_dev, w_phi=w_phi, w_bb=w_bb,
            dplus=dp, dplus_lo=dp_lo, arch=av, prime=pv,
            E2_deparch=q2s, cancel=abs(av) / max(1e-300, abs(av + pv)))
    row["cen"] = cen
    row["th"] = None
    row["t_cell"] = time.time() - t_c
    if want_dep_tau:
        row["dep"] = deployed_tau(dat, M, h)
    del om3, omat
    return row


def deployed_tau(dat, M, h):
    """The DEPLOYED builder (CAL cell only): the folded measure, the
    Lanczos chain and lam_min(I - sqrt(V) P P^T sqrt(V))."""
    dens = ob.grid_density(dat["lag_dep"])
    L = 2 * M - 2
    xs, ws, _u, _f = ob.folded_measure_full(dens, L, +1.0)
    ys, vs, _u2, _f2 = ob.folded_measure_full(dens, L, -1.0)
    al, be, m0, nst = ob.lanczos_chain(xs, ws, h + 1)
    if nst < h + 1:
        return dict(fail="CHAIN")
    pn = ob.eval_chain(al, be, m0, ys, h)
    gr = np.sqrt(vs)[:, None] * (pn @ pn.T) * np.sqrt(vs)[None, :]
    am = np.eye(len(ys)) - 0.5 * (gr + gr.T)
    ev = np.linalg.eigvalsh(am)
    return dict(tau=float(ev[0]), negA=int(np.sum(ev < 0.0)),
                n_pos=len(xs), n_neg=len(ys))


# ======================================================= calibration
def calibration(census):
    section("CAL -- THE CALIBRATION WARD (a shallow TIE cell: the "
            "deployed builder, the four structural identities, and "
            "the three evaluators on one witness)")
    hs = np.asarray([c["h"] for c in census], float)
    cell = census[int(np.argmin(np.abs(hs - CAL_TGT)))]
    print("    CAL cell: h %d kz %d alpha %.6f M %d"
          % (cell["h"], cell["kz"], cell["alpha"], cell["M"]),
          flush=True)
    row = run_cell("CAL", cell, want_dep_tau=True)
    dat, dep = row["dat"], row["dep"]
    M, h = dat["M"], dat["h"]
    tbar = TENT_ULP * EPS64 * dat["at_scale"]
    check("CAL1 my vectorised tent assembly ties core.atom_lags_at to "
          "the SUMMATION-ORDER floor (dev %.3e <= %.1f ulp = %.3e on "
          "%d atoms; profile scale %.3e)"
          % (dat["tent_dev"], TENT_ULP, tbar, dat["n_atom"],
             dat["at_scale"]),
          dat["tent_dev"] <= tbar, kill="K2")
    check("CAL2 my (III) arch series ties the deployed 48-point "
          "Gauss-Legendre kernel (max abs dev %.3e <= %.0e; certified "
          "series tail %.3e)"
          % (dat["arch_dev"], ARCH_BAR, dat["arch_tail"]),
          dat["arch_dev"] <= ARCH_BAR, kill="K2")
    # identity: Omega_weil vs Omega_quad, and TH vs direct node sums
    th, wsig, _dv, L = node_frame(dat["lag_dep"], M)
    mi = np.arange(h)
    cp = np.cos(np.outer(th[wsig > 0.0], mi))
    cn = np.cos(np.outer(th[wsig < 0.0], mi))
    oq = (cp.T * wsig[wsig > 0.0]) @ cp - (cn.T * (-wsig[wsig < 0.0])) @ cn
    oq = 0.5 * (oq + oq.T)
    aext = np.concatenate([dat["lag_dep"], [dat["lag_dep"][M - 2]]])
    rr = np.arange(2 * h)
    gseq = aext[rr] - 0.5 * (aext[rr + 1] + aext[np.abs(rr - 1)])
    ow = np.empty((h, h))
    omega_weil_rows(gseq, h, ow)
    idd = float(np.max(np.abs(ow - oq)))
    check("CAL3 the (II) WEIL KERNEL identity: Omega_weil (lag profile "
          "only, no fft/fold/quadrature) == Omega_quad (rebuilt "
          "measure) entrywise to %.3e <= %.0e (scale %.3e)"
          % (idd, IDENT_BAR, float(np.max(np.abs(oq)))),
          idd <= IDENT_BAR, kill="K2")
    del cp, cn, oq, ow
    tau_id = row["lam1_gen"]
    rel = abs(tau_id - dep["tau"]) / max(abs(dep["tau"]), 1e-300)
    check("CAL4 the rebuilt IDEAL wall scalar ties the DEPLOYED "
          "float64 tau in sign and to rtol %.3e <= %.0e "
          "(tau_ideal %+.8e vs deployed tau %+.8e, n_pos %d/%d "
          "n_neg %d/%d)"
          % (rel, CAL_RTOL, tau_id, dep["tau"], row["n_pos"],
             dep["n_pos"], row["n_neg"], dep["n_neg"]),
          rel <= CAL_RTOL and (tau_id > 0) == (dep["tau"] > 0)
          and row["n_pos"] == dep["n_pos"]
          and row["n_neg"] == dep["n_neg"], kill="K3")
    for wn in ("W1", "W3"):
        cc = row["cen"][wn]
        vals = [cc["E1"][0], cc["E2"][0], cc["E3"][0]]
        spread = max(vals) - min(vals)
        check("CAL5%s the three evaluators agree on witness %s: E1 "
              "%+.8e E2 %+.8e E3 %+.8e (spread %.3e, enclosure "
              "half-widths %.2e/%.2e/%.2e)"
              % (wn[-1], wn, vals[0], vals[1], vals[2], spread,
                 cc["E1"][1], cc["E2"][1], cc["E3"][1]),
              spread <= IDENT_BAR * max(1.0, abs(vals[0])),
              kill="K3")
        check("CAL6%s the FFT node-value half-width holds on a "
              "DISJOINT re-measurement (%.3e <= eta %.3e; a-priori "
              "model %.3e, measured %.3e)"
              % (wn[-1], cc["fft_dev2"], cc["eta"], cc["eta_mod"],
                 cc["fft_dev"]),
              cc["fft_dev2"] <= cc["eta"], kill="K2")
        check("CAL7%s the DECLARED coefficient-transform model holds "
              "on a DISJOINT re-measurement (phi %.3e <= %.3e, b %.3e "
              "<= %.3e)"
              % (wn[-1], cc["w_phi"], cc["phi_dev"], cc["w_bb"],
                 cc["b_dev"]),
              cc["w_phi"] <= cc["phi_dev"]
              and cc["w_bb"] <= cc["b_dev"], kill="K2")
        q3d, w3d = cc["E3d"]
        q3t, w3t = cc["E3t"]
        check("CAL8%s PATH 3 agrees with itself in all three "
              "coordinates (stable %+.8e | Toeplitz-Hankel %+.8e "
              "+-%.1e | assembled h x h matrix %+.8e +-%.1e)"
              % (wn[-1], cc["E3"][0], q3t, w3t, q3d, w3d),
              abs(q3t - cc["E3"][0]) <= w3t + cc["E3"][1]
              and abs(q3d - cc["E3"][0]) <= w3d + cc["E3"][1],
              kill="K2")
    print("    CAL cancellation census (PATH 2): arch %+.6e prime "
          "%+.6e -> Q %+.6e, cancellation ratio %.3e"
          % (row["cen"]["W1"]["arch"], row["cen"]["W1"]["prime"],
             row["cen"]["W1"]["E1"][0], row["cen"]["W1"]["cancel"]),
          flush=True)
    return row, cell


# ================================================ admissibility audit
def admissibility(cell, row):
    """(c) THE ADMISSIBILITY AUDIT.  Every registered rule of the
    window family, checked pedantically.  Returns (verdict, lines)."""
    u2, g2 = DEEP["U"], DEEP["G"]
    kz, h, M, alpha = cell["kz"], cell["h"], cell["M"], cell["alpha"]
    D = 2.0 * alpha / M
    gap = float(g2[kz])
    lines = []
    excl = []
    ext = []
    lines.append("kz %d in [2, %d): %s" % (kz, KZ2_MAX,
                                           2 <= kz < KZ2_MAX))
    if not 2 <= kz < KZ2_MAX:
        excl.append("KZ-RANGE")
    d_k = 0.5 * gap / NU_MAIN
    m_ref = int(math.ceil(alpha / d_k - 1.0e-9)) + 1
    if m_ref % 2:
        m_ref += 1
    lines.append("T105/T112 frame relation: g_kz %.6e, d_k = g/(2 nu) "
                 "%.6e, M_ref %d == M %d: %s ; grid step D %.6e vs "
                 "the admissibility floor g_kz/nu %.6e -> ratio "
                 "%.6f (<= 1 required)"
                 % (gap, d_k, m_ref, M, m_ref == M, D, gap / NU_MAIN,
                    D / (gap / NU_MAIN)))
    if m_ref != M:
        excl.append("FRAME-M")
    if D > gap / NU_MAIN * (1.0 + 1e-12):
        excl.append("NU-FLOOR")
    lines.append("registered frame-A window range H_MIN %d <= h %d <= "
                 "HCAP %d: %s" % (H_MIN, h, HCAP, H_MIN <= h <= HCAP))
    if h > HCAP:
        ext.append("HCAP-EXTENDED(h %d = %.2f x HCAP %d)"
                   % (h, h / HCAP, HCAP))
    elif h < H_MIN:
        excl.append("H-MIN")
    n_at = int(np.searchsorted(u2, 2.0 * alpha + 1.0e-14, side="right"))
    lines.append("atom floor: %d atoms with log n <= 2 alpha >= "
                 "N_ATOM_MIN %d: %s" % (n_at, N_ATOM_MIN,
                                        n_at >= N_ATOM_MIN))
    if n_at < N_ATOM_MIN:
        excl.append("ATOM-FLOOR")
    xv = cell["X"]
    lines.append("comb completeness: X = e^{2 alpha} %.4e ; deployed "
                 "4e6 prefix margin %.4f (%s) ; CCLXXIX 1.6e7 "
                 "extension margin %.4f (%s)"
                 % (xv, EXT_DEPLOYED / xv, xv <= EXT_DEPLOYED,
                    TAB2 / xv, xv <= TAB2))
    if xv > TAB2:
        excl.append("COMB-INCOMPLETE")
    elif xv > EXT_DEPLOYED:
        ext.append("COMB-EXTENDED(deployed 4e6 margin %.4f < 1, only "
                   "complete under the 1.6e7 extension)"
                   % (EXT_DEPLOYED / xv))
    umin = float(u2[0])
    lines.append("A8 tent reflection: min u = log 2 %.6f >= D %.6e: "
                 "%s (unreachable)" % (umin, D, umin >= D))
    if umin < D:
        excl.append("A8-REFLECTION")
    lines.append("folding/rank: n_pos %d >= h %d: %s ; n_neg %d ; "
                 "node accounting n_pos + n_neg + n_zero = %d == M %d: "
                 "%s"
                 % (row["n_pos"], h, row["n_pos"] >= h, row["n_neg"],
                    row["n_pos"] + row["n_neg"] + row["n_zero"], M,
                    row["n_pos"] + row["n_neg"] + row["n_zero"] == M))
    if row["n_pos"] < h:
        excl.append("RANK-SHORT")
    if row["n_pos"] + row["n_neg"] + row["n_zero"] != M:
        excl.append("NODE-ACCOUNTING")
    lines.append("CLXXXVII test-function class: the witness is a real "
                 "coefficient vector of degree < h = %d, so phi_v is "
                 "the autocorrelation of the odd cell function and is "
                 "in the finite odd Fejer cone (phihat >= 0) BY "
                 "CONSTRUCTION: True" % h)
    verdict = ("RULE-EXCLUDED(" + ",".join(excl) + ")" if excl
               else ("RULE-EXTENDED(" + "; ".join(ext) + ")" if ext
                     else "ADMISSIBLE"))
    return verdict, lines


# ======================================================= the census
def cell_verdict(row):
    """The frozen per-cell replication verdict from the 2 x 3
    certified census."""
    signs = {}
    for wn in ("W1", "W3"):
        cc = row["cen"][wn]
        for en in ("E1", "E2", "E3"):
            v, hw = cc[en]
            if v + SIGN_MARGIN * hw < 0.0:
                signs[(wn, en)] = "NEG"
            elif v - SIGN_MARGIN * hw > 0.0:
                signs[(wn, en)] = "POS"
            else:
                signs[(wn, en)] = "STRADDLE"
    own = [signs[("W1", "E1")], signs[("W1", "E2")],
           signs[("W3", "E2")], signs[("W3", "E3")]]
    allv = list(signs.values())
    if all(s == "NEG" for s in allv):
        return "REPLICATED-NEGATIVE", signs
    if all(s == "POS" for s in allv):
        return "REPLICATED-POSITIVE(no witness found; positivity NOT "\
            "certified)", signs
    if any(s == "STRADDLE" for s in allv):
        return "UNRESOLVED", signs
    return "NOT-REPLICATED", signs


def print_row(row):
    dat = row["dat"]
    print("      geom: M %d h %d D %.6e | nodes pos %d neg %d zero %d "
          "| atoms %d | arch dev(mine-deployed) %.3e certified tail "
          "%.3e | tent dev %.1e"
          % (dat["M"], dat["h"], dat["D"], row["n_pos"], row["n_neg"],
             row["n_zero"], dat["n_atom"], dat["arch_dev"],
             dat["arch_tail"], dat["tent_dev"]))
    ine = row.get("inertia", {})
    print("      spectra: lam_min(Omega, O) [PATH 1] %+.6e | "
          "lam_min(Omega_weil) [PATH 3] %+.6e | exact LDL block "
          "inertia n_neg %s (2x2 %s, zero %s) consistent %s"
          % (row["lam1_gen"], row["lam3_std"], ine.get("n_neg", "-"),
             ine.get("n_2x2", "-"), ine.get("n_zero", "-"),
             ine.get("agree", "-")))
    for wn in ("W1", "W3"):
        cc = row["cen"][wn]
        print("      %s: E1 %+.6e +- %.2e | E2 %+.6e +- %.2e | E3 "
              "%+.6e +- %.2e | tau_ub(E1) %+.6e | D+ %.6e"
              % (wn, cc["E1"][0], cc["E1"][1], cc["E2"][0],
                 cc["E2"][1], cc["E3"][0], cc["E3"][1],
                 cc["E1"][0] / max(cc["dplus_lo"], 1e-300),
                 cc["dplus"]))
        print("         margins |Q|/halfwidth: E1 %.3e E2 %.3e E3 "
              "%.3e | PATH-3 self-check: Toeplitz-Hankel %+.6e +-%.1e"
              " assembled-matrix %+.6e +-%.1e"
              % (abs(cc["E1"][0]) / max(cc["E1"][1], 1e-300),
                 abs(cc["E2"][0]) / max(cc["E2"][1], 1e-300),
                 abs(cc["E3"][0]) / max(cc["E3"][1], 1e-300),
                 cc["E3t"][0], cc["E3t"][1], cc["E3d"][0],
                 cc["E3d"][1]))
        print("         PATH-2 anatomy: arch %+.10e  prime %+.10e  "
              "cancellation %.3e | deployed-arch swap E2 %+.6e "
              "(shift %+.3e) | node ward %.2e/%.2e <= eta %.2e "
              "(a-priori model %.2e) | coef ward phi %.2e <= %.2e "
              "b %.2e <= %.2e | |a|_1 %.3e"
              % (cc["arch"], cc["prime"], cc["cancel"],
                 cc["E2_deparch"], cc["E2_deparch"] - cc["E2"][0],
                 cc["fft_dev"], cc["fft_dev2"], cc["eta"],
                 cc["eta_mod"], cc["w_phi"], cc["phi_dev"],
                 cc["w_bb"], cc["b_dev"], cc["a1n"]))


def main():
    print("cased_replicate_probe -- PRIME.COFINAL.CASED.REPLICATE.01")
    print("SPEC_SHA %s%s" % (SPEC_SHA[:16], "  [SMOKE]" if SMOKE else ""))
    section("S0 -- firewall + anti-circularity")
    bad = ast_scan(BANNED_IDS)
    check("S0.1 AST firewall: no prime/zero oracle identifier (%s)"
          % (",".join(sorted(set(bad))) or "clean"), not bad, kill="K1")
    bad_r = ast_scan_functions(READER_FUNCS, READER_BANNED)
    check("S0.2 AC the EVALUATORS and the kernel/arch/comb readers see "
          "nodes, weights, entries, coefficients, positions, masses "
          "and frozen constants only -- no eigensolver, no inverse, "
          "no tau (%s)" % (",".join(sorted(set(bad_r))) or "clean"),
          not bad_r, kill="K1")

    build_tables()
    if KILLS:
        return finish([])
    census = deep_census()
    if KILLS:
        return finish([])
    by_key = {(c["h"], c["kz"]): c for c in census}

    cal_row, cal_cell = calibration(census)
    if any(k in ("K1", "K2", "K3") for k in KILLS):
        return finish([])

    section("CEN -- THE REPLICATION CENSUS (the two CASE-D targets "
            "FIRST, then the CASE-B calibration controls, then the "
            "POS control; guard %.2f * c_hat * h^3 <= %.0f s)"
            % (GUARD_FAC, BUILD_CAP_S))
    if SMOKE:
        hs = np.asarray([c["h"] for c in census], float)
        prio = [("S1", census[int(np.argmin(np.abs(hs - 900)))]),
                ("S2", census[int(np.argmin(np.abs(hs - 1200)))])]
    else:
        prio = [(k, by_key[(CCCVII[k][0], CCCVII[k][1])])
                for k in PRIO_KEYS]
    rows = []
    c_hat = COST_C_ENV
    for tag, cell in prio:
        est = GUARD_FAC * c_hat * float(cell["h"]) ** 3
        if time.time() - T0 + est > BUILD_CAP_S:
            print("    %-4s h %-6d kz %-4d UNBUILT-GUARD (est %.0f s "
                  "at c_hat %.2e, elapsed %.0f s, cap %.0f s)"
                  % (tag, cell["h"], cell["kz"], est, c_hat,
                     time.time() - T0, BUILD_CAP_S), flush=True)
            rows.append(dict(tag=tag, cell=cell, unbuilt=True))
            continue
        row = run_cell(tag, cell)
        c_hat = max(c_hat, 1.05 * row["t_cell"] / float(cell["h"]) ** 3)
        vd, signs = cell_verdict(row)
        row["verdict"] = vd
        row["signs"] = signs
        row["adm"], row["adm_lines"] = admissibility(cell, row)
        rows.append(row)
        ref = CCCVII.get(tag)
        print("    %-4s h %-6d kz %-4d alpha %.4f  %-28s  CCCVII "
              "case %s tau_ideal_ub_ref %s   %.1f s"
              % (tag, cell["h"], cell["kz"], cell["alpha"], vd,
                 ref[5] if ref else "-",
                 ("%+.4e" % ref[4]) if ref and ref[4] else "-",
                 row["t_cell"]), flush=True)
        print_row(row)
    return finish_census(rows, cal_row, cal_cell, census, by_key)


# ===================================================== controls + end
def controls(census, by_key, rows):
    section("X -- CONTROLS-MUST-FIRE (X1 scramble, X2 smooth, XW the "
            "doctored lag, XA the arch-implementation swap)")
    built = [r for r in rows if not r.get("unbuilt")]
    if not built:
        check("X0 no cell built -- controls cannot run", False,
              kill="K1")
        return
    tgt = built[0]["cell"] if not SMOKE else built[0]["cell"]
    for world, name, kill in (("scramble", "X1", "K4"),
                              ("smooth", "X2", "K4")):
        r = run_cell("X-" + world[:4], tgt, world=world,
                     scr_seed=SCR_SEED)
        vals = [r["cen"]["W1"]["E1"][0], r["cen"]["W1"]["E2"][0],
                r["cen"]["W1"]["E3"][0]]
        fired = all(v < -1.0e-6 for v in vals)
        print("    %s world at h %d kz %d: lam_min(Omega,O) %+.4e | "
              "E1 %+.4e E2 %+.4e E3 %+.4e"
              % (world.upper(), tgt["h"], tgt["kz"], r["lam1_gen"],
                 vals[0], vals[1], vals[2]), flush=True)
        check("%s the %s world DESTROYS the wall scalar on ALL THREE "
              "paths (all three certified reads < -1e-6)"
              % (name, world.upper()), fired, kill=kill)
    r = run_cell("X-dope", tgt, dope=True)
    base = built[0]
    shift = abs(r["cen"]["W1"]["E2"][0] - base["cen"]["W1"]["E2"][0])
    hw = base["cen"]["W1"]["E2"][1]
    print("    DOPED lag entry c[M/3] scaled by 1 + %.0e: E2 %+.6e vs "
          "%+.6e (shift %.3e, enclosure half-width %.3e)"
          % (DOPE, r["cen"]["W1"]["E2"][0], base["cen"]["W1"]["E2"][0],
             shift, hw), flush=True)
    check("XW the certified enclosure FIRES on a DOCTORED lag entry "
          "(shift %.3e > half-width %.3e): the certificate has teeth"
          % (shift, hw), shift > 10.0 * hw, kill="K4")
    sw = [abs(rr["cen"][wn]["E2_deparch"] - rr["cen"][wn]["E2"][0])
          for rr in built for wn in ("W1", "W3")]
    sp = [abs(rr["cen"][wn]["E1"][0] - rr["cen"][wn]["E3"][0])
          for rr in built for wn in ("W1", "W3")]
    print("    XA arch-implementation seam (my (III) series vs the "
          "deployed 48-point GL): |Delta Q| %.3e..%.3e ; the "
          "cross-evaluator spread |E1 - E3| is %.3e..%.3e"
          % (min(sw), max(sw), min(sp), max(sp)), flush=True)
    check("XA the arch seam is MEASURED and printed (max %.3e); it is "
          "the single shared-ingredient seam of the census (A4)"
          % max(sw), True)


def finish_census(rows, cal_row, cal_cell, census, by_key):
    built = [r for r in rows if not r.get("unbuilt")]
    section("ADM -- THE ADMISSIBILITY AUDIT (registered rules, "
            "checked pedantically, per cell)")
    for r in built:
        print("    %-4s h %-6d kz %-4d  ->  %s"
              % (r["tag"], r["cell"]["h"], r["cell"]["kz"], r["adm"]))
        for ln in r["adm_lines"]:
            print("         - " + ln)
    n_excl = sum(1 for r in built if r["adm"].startswith("RULE-EXCL"))
    n_ext = sum(1 for r in built if r["adm"].startswith("RULE-EXT"))
    check("ADM1 the admissibility audit typed every built cell "
          "(%d ADMISSIBLE, %d RULE-EXTENDED, %d RULE-EXCLUDED)"
          % (len(built) - n_ext - n_excl, n_ext, n_excl), True)

    # the numerical models are enforced at EVERY census cell, not only
    # at the shallow calibration cell (AMENDMENT A14)
    bad = []
    for r in built:
        for wn in ("W1", "W3"):
            cc = r["cen"][wn]
            if cc["fft_dev2"] > cc["eta"]:
                bad.append("%s/%s node %.2e>%.2e"
                           % (r["tag"], wn, cc["fft_dev2"], cc["eta"]))
            if cc["w_phi"] > cc["phi_dev"]:
                bad.append("%s/%s phi %.2e>%.2e"
                           % (r["tag"], wn, cc["w_phi"], cc["phi_dev"]))
            if cc["w_bb"] > cc["b_dev"]:
                bad.append("%s/%s b %.2e>%.2e"
                           % (r["tag"], wn, cc["w_bb"], cc["b_dev"]))
    check("ADM2 every numerical half-width model holds on a DISJOINT "
          "re-measurement at EVERY built census cell, not only at the "
          "shallow calibration cell (%s)"
          % ("; ".join(bad) if bad else
             "%d cells x 2 witnesses x 3 models clean" % len(built)),
          not bad, kill="K2")

    apri = [(r["cen"][wn]["fft_dev"] / max(r["cen"][wn]["eta_mod"],
                                           1e-300))
            for r in built for wn in ("W1", "W3")]
    print("    the A5 A-PRIORI FFT model 8 log2(N) u ||a||_1 is "
          "UNDER-PRICED at depth: measured/model = %.2f..%.2f over the "
          "built cells; the enclosures use the MEASURED half-width "
          "times ETA_SAFE = %.0f instead (AMENDMENT A14)"
          % (min(apri), max(apri), ETA_SAFE))

    section("CENSUS -- THE 4 x 3 REPLICATION TABLE (certified "
            "enclosures of the wall scalar Q[q] at ||a||_2 = 1; a "
            "NEGATIVE certified enclosure is a WITNESS, a positive "
            "one is only 'no witness found')")
    print("    tag  h      kz   alpha    witness  E1 (rebuild)       "
          "E2 (explicit formula) E3 (Weil kernel)     verdict")
    for r in built:
        for wn in ("W1", "W3"):
            cc = r["cen"][wn]
            print("    %-4s %-6d %-4d %.5f %-8s %+.6e+-%.1e %+.6e+-%.1e "
                  "%+.6e+-%.1e  %s"
                  % (r["tag"], r["cell"]["h"], r["cell"]["kz"],
                     r["cell"]["alpha"], wn, cc["E1"][0], cc["E1"][1],
                     cc["E2"][0], cc["E2"][1], cc["E3"][0], cc["E3"][1],
                     r["verdict"] if wn == "W1" else ""))
    print("\n    CROSS-PATH AGREEMENT (max pairwise |E_p - E_q| per "
          "witness, against the certified half-widths):")
    for r in built:
        for wn in ("W1", "W3"):
            cc = r["cen"][wn]
            vv = [cc["E1"][0], cc["E2"][0], cc["E3"][0]]
            hw = max(cc["E1"][1], cc["E2"][1], cc["E3"][1])
            print("      %-4s %s  spread %.3e   max half-width %.3e   "
                  "spread/|Q| %.3e"
                  % (r["tag"], wn, max(vv) - min(vv), hw,
                     (max(vv) - min(vv)) / max(1e-300,
                                               abs(np.mean(vv)))))
    print("\n    AGAINST THE CCCVII RECORD (tau upper bound from E1 "
          "vs the CCCVII refined ideal read; CCCVII's value is an "
          "UPPER bound for tau_ideal, so a replication must land at "
          "or BELOW it):")
    for r in built:
        ref = CCCVII.get(r["tag"])
        if not ref or ref[4] is None:
            continue
        cc = min((r["cen"][w] for w in ("W1", "W3")),
                 key=lambda c: c["E1"][0] / max(c["dplus_lo"], 1e-300))
        mine = cc["E1"][0] / max(cc["dplus_lo"], 1e-300)
        print("      %-4s h %-6d  mine %+.6e   CCCVII %+.6e   ratio "
              "%.4f   below-the-bound %s   deployed tau (CCCVII, not "
              "recomputed) %+.4e"
              % (r["tag"], r["cell"]["h"], mine, ref[4],
                 mine / ref[4], mine <= ref[4] * (1 - 1e-9)
                 if ref[4] < 0 else "-", ref[3]))

    section("VD -- THE PER-CELL REPLICATION VERDICT")
    for r in built:
        ref = CCCVII.get(r["tag"])
        print("    %-4s h %-6d kz %-4d (CCCVII case %s): %s"
              % (r["tag"], r["cell"]["h"], r["cell"]["kz"],
                 ref[5] if ref else "-", r["verdict"]))
        print("         signs: " + ", ".join(
            "%s@%s %s" % (w, e, s) for (w, e), s
            in sorted(r["signs"].items())))
        print("         admissibility: " + r["adm"])
        if r["verdict"] == "REPLICATED-NEGATIVE" and ref \
                and ref[5] == "D":
            print("         TYPED STATEMENT (no claim beyond it): the "
                  "deployed window family's IDEAL form is INDEFINITE "
                  "at this cell -- three independent builds deliver a "
                  "certified negative enclosure at an explicit "
                  "degree-<h witness.  TWO READINGS, both stated "
                  "neutrally and NEITHER chosen here:")
            print("           (R1) an admissibility / identification "
                  "assumption of the window family fails at this "
                  "depth (the audit above types this cell %s);"
                  % r["adm"])
            print("           (R2) the localized Weil form delivers a "
                  "real negative test on an admissible member.")
            print("         The follow-up decision belongs to the "
                  "lead.  NO RH claim, NO counterexample claim.")
        if r["verdict"].startswith("REPLICATED-POSITIVE") and ref \
                and ref[5] == "D" and ref[4] < 0.0:
            ine = r.get("inertia", {})
            print("         TYPED STATEMENT (no claim beyond it): the "
                  "CCCVII case-D NEGATIVE witness DID NOT REPLICATE "
                  "at this cell.  All three independent builds put a "
                  "CERTIFIED POSITIVE enclosure on the ideal wall "
                  "scalar at both extremal witnesses, and the "
                  "directly assembled Weil kernel has lam_min "
                  "%+.4e > 0 with n_neg = %s in the exact block "
                  "inertia of its computed LDL factorisation."
                  % (r["lam3_std"], ine.get("n_neg")))
            print("         DISAGREEMENT ANATOMY (this IS the finding "
                  "in this branch): my PATH-1 ideal pencil reads "
                  "lam_min(Omega, O) %+.4e where CCCVII's refined "
                  "ideal tier reads an UPPER BOUND of %+.4e -- "
                  "opposite signs at comparable magnitude, so the two "
                  "cannot both hold."
                  % (r["lam1_gen"], ref[4]))
            print("         What differs is NOT the window data (the "
                  "comb, the arch kernel and the node accounting all "
                  "tie: arch dev %.1e, tent dev %.1e, node census "
                  "exact) and NOT the metric (PATH 3 uses no metric "
                  "at all).  The one object present in the CCCVII "
                  "route and absent from ALL THREE routes here is the "
                  "LANCZOS CHAIN -- precisely the chain-column "
                  "representation accuracy that CCCVII itself named "
                  "as its open scope edge.  PATH 3 never evaluates a "
                  "chain, so it is immune to that edge by "
                  "construction; the calibration ward shows the same "
                  "deployed chain reproducing the ideal scalar to "
                  "rtol 2.9e-06 at h 878, six orders of h^3 cheaper "
                  "than here."
                  % (r["dat"]["arch_dev"], r["dat"]["tent_dev"]))
            print("         NOT ASSERTED: that the CCCVII read is "
                  "wrong for that reason.  Locating the discrepancy "
                  "inside the chain route is a SEPARATE measurement "
                  "and it was not made here.  The follow-up decision "
                  "belongs to the lead.  NO RH claim, NO "
                  "counterexample claim.")

    controls(census, by_key, rows)
    check("S1 CCXLVII tau-relocation / CCXVII c_h screens: "
          "VACUOUS-BY-CONSTRUCTION (no step formations of record, no "
          "fitted level -- replication census only, declared)", True)

    labels = []
    if SMOKE:
        labels.append("CASED-SMOKE(no frontier cell built by design)")
    dcells = [r for r in built if CCCVII.get(r["tag"], (0, 0, 0, 0, 0,
                                                        "-"))[5] == "D"]
    if dcells:
        vs = {r["tag"]: r["verdict"].split("(")[0] for r in dcells}
        # a case-D cell whose census comes out CERTIFIED POSITIVE on
        # every path is, in the mission taxonomy, exactly the
        # NOT-REPLICATED outcome: the CCCVII negative witness was not
        # reproduced by any independent build.
        for tg, vv in list(vs.items()):
            ref = CCCVII.get(tg)
            if vv == "REPLICATED-POSITIVE" and ref and ref[4] < 0.0:
                vs[tg] = "NOT-REPLICATED(CCCVII %+.3e is NEGATIVE; " \
                    "all three paths certify POSITIVE)" % ref[4]
        if all(v == "REPLICATED-NEGATIVE" for v in vs.values()):
            labels.append("CASED-REPLICATED-NEGATIVE(%d/%d case-D "
                          "cells, three independent builds; NOT a "
                          "counterexample claim, NOT an RH claim)"
                          % (len(dcells), len(dcells)))
        elif any(v.startswith("NOT-REPLICATED") for v in vs.values()):
            labels.append("CASED-NOT-REPLICATED(%s)"
                          % ",".join("%s:%s" % kv for kv in vs.items()))
        else:
            labels.append("CASED-UNRESOLVED(%s)"
                          % ",".join("%s:%s" % kv for kv in vs.items()))
    labels.append("CENSUS(%s)" % "; ".join(
        "%s:%s" % (r["tag"], r["verdict"].split("(")[0]) for r in built))
    labels.append("ADMISSIBILITY(%s)" % "; ".join(
        "%s:%s" % (r["tag"], r["adm"].split("(")[0]) for r in built))
    sp = [abs(r["cen"][w]["E1"][0] - r["cen"][w]["E3"][0])
          for r in built for w in ("W1", "W3")]
    if sp:
        labels.append("CROSS-PATH(|E1 - E3| %.2e..%.2e)"
                      % (min(sp), max(sp)))
    ca = [r["cen"][w]["cancel"] for r in built for w in ("W1", "W3")]
    if ca:
        labels.append("EF-CANCELLATION(%.2e..%.2e; the PATH-2 "
                      "precision frame)" % (min(ca), max(ca)))
    labels.append("ZERO-SIDE(INFEASIBLE-AT-THIS-SCALE; priced, not "
                  "run -- CLXXXVII measured 0.48..0.85 capture on "
                  "2500 zeros against a required 1e-9 relative)")
    return finish(labels)


def finish(labels):
    section("V -- FROZEN VERDICT")
    n_pass = sum(1 for _n, ok in CHECKS if ok)
    n_tot = len(CHECKS)
    if KILLS:
        vmap = {"K1": "PIPELINE-BROKEN", "K2": "WARD-BROKEN",
                "K3": "CALIBRATION-BROKEN", "K4": "CONTROL-SILENT"}
        print("\n  VERDICT: %s" % vmap[KILLS[0]])
    elif not labels:
        print("\n  VERDICT: PIPELINE-BROKEN")
    else:
        print("\n  VERDICT: %s" % " ; ".join(labels))
        print("""
  HONEST FRAME.  Finite float64 measurements with OUTWARD-ROUNDED
  enclosures of the decisive scalars (exactly-rounded fsum
  accumulations, rigorous gamma_n bounds on the accumulated absolute
  sums, a certified geometric tail bracket on the archimedean series,
  and a DECLARED FFT node-value model warded against an exactly
  rounded reference), on BUILT cells of the deployed deep-frame
  window family.  The replicated object is the IDEAL (metric-free,
  basis-free) wall scalar Q[q] = int q^2 dmu_+ - int q^2 dmu_- at an
  explicit degree-<h witness; a NEGATIVE certified enclosure is a
  WITNESS that the ideal form is indefinite, a POSITIVE one is only
  "no witness found" -- positivity is NOT certified anywhere here.
  PATH 3 never evaluates a chain and is therefore immune to the one
  scope edge CCCVII left open by name; PATH 1 and PATH 2 share the
  archimedean series implementation by design (A4) and that seam is
  MEASURED by control XA.  Every statement is about BUILT cells of
  the frozen mission list, never all h.  No marker moves, no
  promotion, NO RH claim, NO counterexample claim.""")
    print("\n  checks %d/%d PASS; SPEC_SHA %s; runtime %.1f s%s"
          % (n_pass, n_tot, SPEC_SHA[:8], time.time() - T0,
             "; SMOKE" if SMOKE else ""))
    return n_pass, n_tot


if __name__ == "__main__":
    main()
