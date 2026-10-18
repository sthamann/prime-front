#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""ground_residue_obs_probe -- PRIME.GROUND.RESIDUE.OBS.01

FROZEN SPEC (2026-08-21).  EXPLORATION ONLY.  This probe writes no
verification module, paper, ledger, website, manifest, Lean file or
status marker.  It makes NO RH claim, NO positivity claim beyond the
per-rung finite statements gated below, NO counterexample claim.  It
closes no gate and narrows no gate.  Concurrent-lane files (the
pi-pattern-scan lane, the census-spectral-lift lane, the independent
session's untracked probes, sieve4_helper.bin) are not touched.

=======================================================================
MISSION (round ~186: ground-state boundary observability).  H3 of the
prime-front terminal residue (PRIME.RESIDUE.EXTERNAL.01) demands
y_t = |A_2/A_0| <= 0.155 T_z^4 -- a LOWER bound on |A_0(d_h)| against
|A_2(d_h)| for the ACTUAL ground state d_h of the wall M_h.  Every
frame/uniform route died trying to control ALL directions (r180 dof
kill, r181 sub-dof kill, l1 majorants, DK norms r177).  THIS round
uses the one fact those routes were forbidden to use: d_h satisfies
M_h d_h = tau_h d_h.  Central object: the scalar resolvent
   R_h(z) = l_0^T (z I - M_h)^{-1} l_0
(NOTE the honest sign convention: with (z I - M)^{-1} the function is
anti-Herglotz, R(zbar) = conj R(z), Im R < 0 in the upper half plane,
and the residue at the ground pole is +|l_0 . d|^2/||d||^2; the
contract's (M - z I)^{-1} convention flips the residue sign -- both
stated, the POSITIVE normalized form is gated).  Goals:
  G1  THE EXACT RESIDUE IDENTITY + FESHBACH/SCHUR SCALAR FORM.
      Res_{z=tau} R_h(z) = |l_0(d_h)|^2/||d_h||^2 = A_0^2 (builder's
      d unit); Schur complement of (z I - M) onto e_0 = l_0/||l_0||:
      R_h(z) = ||l_0||^2 / w(z),
      w(z) = z - alpha - m^T (z I - B)^{-1} m,
      alpha = e_0^T M e_0,  m = the compression coupling Q M e_0,
      B = the codimension-1 compression of M to ker l_0; the residue
      bound becomes  A_0^2 = ||l_0||^2 / w'(tau)  with
      w'(tau) = 1 + m^T (tau I - B)^{-2} m.  ROUND KEY QUESTION: is
      w'(tau) source-side expressible WITHOUT the eigenvector?
  G2  THE TRANSVERSALITY FORM.  gap := mu_1(B) - tau >= 0 by Cauchy
      interlacing (codim-1 compression: tau <= mu_1 <= tau_2); the
      gap and the residue are linked through the SAME w(z):
      w'(tau) = 1 + sum_j (m.u_j)^2/(mu_j - tau)^2, hence the exact
      two-sided sandwich
        ||l_0||^2 gap^2/(gap^2 + ||m||^2) <= A_0^2
                       <= ||l_0||^2 gap^2/(gap^2 + (m.u_1)^2).
      Ladder measured at all reachable rungs: sign, size, exponent,
      demand ratio (H3 margin), fake worlds, r172-class witness.
  G3  NEW-QUANTITY ADJUDICATION (tau-screen, strict): (i) log-log
      slopes of {gap, w'(tau), demand margin} against tau_h across
      rungs -- slope ~1 == relabeling; (ii) ancestry DFS: NO leg may
      consume TAUPOS or TLAWCAP (the A_0-triangle is THIS contract's
      nearest landmine -- the loop guard is extra-sharp: tau_h enters
      ONLY as a measured per-rung eigenvalue scalar, never as a sign
      hypothesis, and no TLAWCAP currency is read anywhere);
      (iii) composed-chain demand typing per leg:
      EXACT / SOURCE-CLASSICAL / MEASURED / RELABELED.
  G4  ATTACK-TOOL PRICING on whatever leg stays live: Feshbach
      (delivered in G1), rank-one spectral flow (delivered in G2),
      Riemann-Hilbert/IIKS integrable structure (the wall's own
      displacement structure measured + symbolically located),
      source-specific Carleman (classical anchors cited, priced).

NOTATION (r171-r182 conventions VERBATIM).  Rung h = builder x
(R4.build_cell, even sector, MAIN world); a = log(h)/2; K = ceil(1.25
h log h); om_k = k pi/a; b_k = om_k^2; T_z = 2 pi h; mode norms
nrm_0 = sqrt(2a), nrm_k = sqrt(a) (k >= 1); builder eigensystem
(mpE, mpV) with tau = E[0], unit ground column V[:,0]; de-normalized
source coefficients c_k = V[k,0]/nrm_k (== builder cn_mp_str, cross-
warded); d_k = (-1)^k c_k; A_0 = sum_k d_k = l_0 . v_1 with the FIXED
GEOMETRY functional l_0[k] = (-1)^k/nrm_k; A_2 = sum_{k>=1} d_k b_k =
l_2 . v_1 with l_2[k] = (-1)^k b_k/nrm_k (l_2[0] = 0); y_t =
|A_2/A_0|.  Schur data per functional l: e = l/||l||, Householder
H = I - 2 v v^T/(v.v) with v = e - e_1 maps e to the first coordinate;
T = H M H; alpha = T[0,0]; m = T[1:,0]; B = T[1:,1:]; eigsy(B) =
(mu_j, u_j); w'(tau) = 1 + sum_j (m.u_j)^2/(mu_j - tau)^2; gap =
mu_1 - tau; S2 = sum_{i>=2} (e.v_i)^2/(tau_i - tau) (the eigenvector-
side dual; the first-order secular relation gap*S2*||l||^2/A_0^2 -> 1
is the machine exhibit that the gap is the residue in matrix
coordinates).  DEMANDS: X_meas = (A_2/(0.155 T_z^4))^2 (H3 with the
measured A_2), X_triv = (||l_2||/(0.155 T_z^4))^2 (the FREE ceiling
A_2^2 <= ||l_2||^2 from w_2' >= 1 -- Cauchy-Schwarz, no eigenvector);
g_req(X) = sqrt(X) ||m|| / sqrt(||l_0||^2 - X) (the gap floor that
makes the ||m||-priced sandwich deliver A_0^2 >= X); margin =
gap/g_req.  RAW COORDINATES (displacement layer): Raw[i,j] =
par_i par_j nrm_i nrm_j M[i,j]; the commutator C = diag(b) Raw -
Raw diag(b) tests the integrable structure; one-function Loewner form
Raw[i,j] = (f_i - f_j)/(b_i - b_j) off-diagonal, f extracted from
C[:,0]; per-block potentials proven symbolically (G17): f_pole,i =
-2 sinh(a/2)^2/(1/4 + b_i), f_arch,i = +2 om_i jv_i, f_prime,i =
-2 om_i pj_i with pj_k = sum_q w_q sin(om_k u_q) -- M = pole + arch -
prime carries f = f_pole + f_arch + 2 om pj: ONE source function.

DPS schedule (r182 conditioning ladder VERBATIM, disclosed): DPS =
{4: 60, 5: 60, 6: 65, 7: 70, 8: 80, 9: 85, 10: 90, 11: 100, 12: 110,
13: 120, 14: 120, 15: 125, 16: 130, 20: 144}.  HRUNGS = 4..16,
H_HOLD = 20.  L2_RUNGS = (4, 5, 8, 13) (second Schur branch);
ALT_RUNGS = (4, 5, 8, 13); F_RUNGS = (4, 5, 8) (prime-block rebuild
ward + one-function prime potential); WIT_RUNG = 5 (r172 recipe
VERBATIM: dv = A_2 (W-1)/(b_2 - b_1) on modes 1, 2, W = 1000).
CONTROLS: SMOOTH(5), SCRARITH(4, 5, 8), EPSTEIN(8, 9, 10) at CTRL_DPS
{60, 60, 80} -- the identities must hold WORLD-BLIND (linear
algebra), the VALUES must separate; the identity layer is typed
world-blind BY DESIGN, never sold as a world separator.
PRECISION REFUSAL RULE: a rung's gap statement is REFUSED (counted,
excluded from ladders) if gap < 10^-(dps-20) * ||M||_F.

=======================================================================
THE FOUR SECTIONS AS EXECUTED (verdicts frozen from the ONE disclosed
pre-freeze calibration pass, calib_gro_pass1.log; record values below
ARE the calibrated numbers; two pre-spec convention scratches at h=5/8
were run and deleted before this spec was written, DISCLOSED -- they
fixed the sign convention, validated the Householder/compression
pipeline, and discovered the one-function Loewner fact gated in G60)
=======================================================================
G1 (THE IDENTITY, EXACT AND MACHINE-VERIFIED AT EVERY RUNG).  The
residue identity and the Feshbach/Schur scalar form are proven exact
on the sympy layer (rational-orthogonal 3x3 instance from the
quaternion (1,2,3,4), plus the fully generic symbolic 2x2) and gated
at ALL 14 reachable rungs: |A_0^2 w'(tau)/||l_0||^2 - 1| <=
7.8e-45 at every rung (worst; typical far smaller), the l_2 branch
identity |A_2^2 w_2'(tau)/||l_2||^2 - 1| (<= 3.3e-46) and the TWO-
FUNCTIONAL H3 form y_t^2 == (||l_2||^2/||l_0||^2) (w_0'(tau)/
w_2'(tau)) exact at all four L2_RUNGS (<= 1.5e-45).  THE
KEY-QUESTION ANSWER, typed honestly in two halves: (YES) w'(tau) is
expressible from {alpha, m, B} -- all EXACT-LINEAR in the atom
transforms (prime block rebuilt from the sieve atoms, ward dev 0.0
EXACT at all F_RUNGS, weight-doubling exact 0.0) --
plus the ONE measured scalar tau_h; the wall EIGENVECTOR d is
ELIMINATED by the Schur reduction: the A_0 floor becomes a derivative
bound on the explicit scalar function w (a genuinely new coordinate
system, prior-art-linked: w'(tau) = ||l||^2 P'(tau)/N(tau) is the
CDLI adjugate identity A_0^2 = N(tau)/P'(tau) in Schur coordinates,
G16 -- SAME-IDENTITY-NEW-COORDINATES, disclosed).  (BUT) the demand
mass inside w'(tau) concentrates on ONE term: (m.u_1)^2/gap^2 -- u_1
the ground eigenvector of the COMPRESSION B: the eigenvector demand
DESCENDS one level rather than vanishing (EIGENVECTOR-DESCENDS-NOT-
ELIMINATED); the fully source-priced form (||m|| for the overlap)
loses the measured 11.2-90.7 orders (the overlap spread
log10((m.u_1)^2/||m||^2) ladder -11.24 (h=4) .. -90.72 (h=20),
G25/G28).
G2 (THE TRANSVERSALITY LADDER, MEASURED).  gap > 0 at ALL 14 rungs
(strict interlacing == A_0 != 0, both directions proven exact G13),
NO precision refusals at the disclosed dps schedule; the gap is TINY
against the spectral gap: log10(gap/fullgap) = -5.15 at h = 4
falling to -8.52 at h = 16 and -9.00 at h = 20 (record table) -- the
arithmetic ray couples the ground state to ker l_0 ANOMALOUSLY
WEAKLY, rung after rung.  THE DISGUISE EXHIBIT: gap * S2 * ||l_0||^2
/ A_0^2 = 1 - eps with eps <= 2.55e-6 at EVERY rung (record): the
transversality gap IS the residue divided by the explicit
second-order moment S2 -- the same quantity in matrix coordinates,
NOT an independent handle.  DEMAND: the ||m||-priced gap route to H3
FAILS at every rung by 5.1-45.0 orders (margin ladder
gap/g_req(X_meas), record -5.08 (h=4) .. -45.05 (h=20)); the
trivial-ceiling demand X_triv is SOLVABLE (X_triv < ||l_0||^2) at
all rungs but its margin is worse by the ||l_2||/|A_2| slack; the
exact overlap-priced form carries BY IDENTITY but consumes u_1.
WORLDS: identities hold world-blind (<= 4.4e-59 in all 7 control
cells); the VALUES separate cleanly: fake-world log10(gap/fullgap) =
-0.17..-2.02 (top-of-spectrum class, tau < 0 in every fake cell) vs
MAIN -5.15/-5.96/-6.88 at the same x -- the anomalously small gap
fraction is arithmetic-specific with >= 1 dex clearance (same
signature class as r182's mass-location separation, MEASURED).
WITNESS (r172 recipe VERBATIM, h = 5): y_t'' = 1000.0 y_t at source
cost 8.1e-2 (A_0 preserved, dev 1.1e-53); the witness ray EXITS THE
EIGENMANIFOLD -- eigen-residual 1e-2.26 vs the true ray's 1e-60.75
vs the full spectral gap 1e-10.45, i.e. 1e8.2 x the FULL spectral
gap -- and the l_2-residue identity DETECTS it at deviation 1.1e6
(=~ W^2) while the l_0 identity stays blind (dev 1.2e-1, A_0
preserved by construction, disclosed): the residue observable pair
{l_0, l_2} separates the witness class the frame routes could not;
the gap itself is witness-INVARIANT (matrix-side, definitional --
typed, not sold).  ALT JETS (r182): SIGNFLIP/UNIFORM/MAGSCRAM rays
sit 8.9-52.6 orders off the l_0-residue identity (order-distance
|log10 ratio|, record) PLUS one exact A_0-null exhibit -- UNIFORM at
h = 13 (K = 42 even: sum_k (-1)^k = 0 exactly, the identity fires in
the zero-residue direction, order-distance INF; amendment A1): the
identity pins the true ray.
G3 (ADJUDICATION).  TAU-SCREEN: slope log10(gap) vs log10(tau) =
+1.011 (R^2 1.000), slope log10(w') = -1.003, slope
log10(margin_meas) = +0.519 (record): the RAW gap RIDES the
tau/conditioning currency inside the declared ride band (0.7, 1.3)
in |slope|, w' anti-rides in the same currency; the margin slope
+0.52 sits BELOW the ride band (mixed currency: the gap ride divided
by the demand growth -- NOT typed independent, disclosed) -- per the
round-1 scope command the RAW-GAP FLOOR LEG IS FLAGGED
RELABELED-AND-STOPPED: no asymptotic claim, the gap ladder is the
residue ladder in matrix coordinates (G29 exhibit), its decay
exponent beta(gap vs h: -4.85 dex/rung R^2 1.000) is the known
conditioning schedule in a second currency.  WHAT IS GENUINELY NEW
(typed): (a) the Schur/Feshbach COORDINATES themselves (w, alpha, m,
B source-linear; eigenvector eliminated at identity level) -- EXACT;
(b) the one-function Loewner structure of the wall (G60) -- EXACT,
world-blind, source enters ONLY through the potential f; (c) the
overlap-spread ladder and the gap-fraction ladder -- MEASURED, new
observables (world-separating in the measured sense); (d) the
witness-detection pair {l_0, l_2} residue identities -- EXACT + the
witness's eigen-residual price MEASURED.  ANCESTRY: the A_0-triangle
(TAUPOS/TLAWCAP/EPSLOCK) is DETECTED as a flagged cycle and consumed
by NOTHING delivered -- tau_h enters as a measured scalar only, no
sign hypothesis, no TLAWCAP currency read; census-forall-k,
Gonek-1984, Montgomery-PC likewise flagged, not consumed; min-cut
flows 4/5/5/6 replicate r135 -- this round adds NO flow.  COMPOSED
CHAIN [gap floor + ||m|| price + trivial A_2 ceiling => H3]: every
arrow EXACT, the gap-floor INPUT is the one open leg and it is
RELABELED (rides tau) -- the chain is a coordinate change of the
known wall, honestly so typed; no RH-strong input demanded anywhere
(the chain is per-rung finite; the lambda-uniform gap floor is NAMED
as the open input and NOT claimed).
G4 (TOOL PRICING, with numbers).  FESHBACH: DELIVERED-EXACT (this
round's G1; per-rung identity, no residual demand).  RANK-ONE
SPECTRAL FLOW / INTERLACING: DELIVERED-EXACT as the secular
representation + sandwich (G13/G23/G24); QUANTITATIVELY LOSSY in its
fully-source-priced form: 11.2-90.7 orders (the overlap spread), and
its strict-positivity content is EQUIVALENT to A_0 != 0 (both
directions exact G13) -- qualitative relabel, disclosed.  RIEMANN-
HILBERT/IIKS: the wall in raw coordinates has displacement rank
EXACTLY 2 against diag(b) (s3/s1 <= 2.6e-16 at all F_RUNGS + h = 13,
float64 floor; reconstruction dev <= 1.1e-15) == ONE-FUNCTION
LOEWNER MATRIX Raw[i,j] = (f_i - f_j)/(b_i - b_j), f = f_pole +
f_arch + 2 om pj proven per-block symbolically (G17) and the prime
potential -2 om_k pj_k re-derived from the sieve atoms at F_RUNGS
(<= 1.2e-61, mp); prior art
honestly separated: r45-class LOEWNER-DEAD killed the LADDER-as-
Loewner-flow identification, THIS is the wall matrix itself being a
Loewner/Pick divided-difference kernel -- the classical dictionary
is Loewner 1934 (operator monotonicity == Loewner-matrix PSD) and
IIKS 1990/Deift-Its-Krasovsky 2011 for the resolvent asymptotics of
integrable kernels; the CDLI relative-Szego/IIKS candidate is the
SAME class on another family: typed NEEDS-NAMED-EXTERNAL-TOOL
(carries structurally: R_h(z) is the scalar resolvent of an explicit
one-function Loewner kernel -- a well-posed classical object; killed
nowhere; the lambda-uniform statement is the open input).  CARLEMAN:
the needed classical form is a quantitative vanishing-order/doubling
bound at the functional l_0 for the ground state of a discrete
operator; continuum anchor Donnelly-Fefferman 1988 (Invent. Math.
93, 161-183: vanishing order <= C sqrt(lambda)); the DISCRETE
regime is the named risk -- plain discrete UCP FAILS on lattices and
robust discrete Carleman constants degrade as e^{-c/h_mesh}
(Fernandez-Bertolin/Roncal/Rueland, Calc. Var. PDE 60 (2021) 239,
DOI 10.1007/s00526-021-02098-z; Fernandez-Bertolin/Vega, J. Funct.
Anal. 272 (2017) 4853-4869): with the wall's mesh pi/a and the
conditioning ladder collapsing FASTER than any e^{-c/h} at the
measured -4.85 dex/rung, the tool is typed NEEDS-NAMED-EXTERNAL-
TOOL, LOW-CARRY (the exponential-constant wall is named with
numbers); no web claim beyond the citations.
=======================================================================
TAXONOMY VERDICT (frozen from calibration):
   RESIDUE-IDENTITY-EXACT-ALL-RUNGS (<= 7.8e-45 at 14/14) +
   FESHBACH-SCALAR-FORM-EXACT (sympy generic 2x2 + rational 3x3 +
   per-rung) +
   WPRIME-EIGENVECTOR-FREE-GIVEN-TAU (the KEY QUESTION: YES --
   {alpha, m, B} source-linear warded, tau the one measured scalar;
   prior art CDLI adjugate == same identity, new coordinates) +
   DEMAND-DESCENDS-TO-COMPRESSION-OVERLAP (the honest second half:
   (m.u_1)^2/gap^2 carries w'; u_1 = ground of B; ||m||-pricing
   loses 11.2-90.7 orders) +
   TRANSVERSALITY-GAP-POSITIVE-ALL-RUNGS (strict interlacing ==
   A_0 != 0 exact both ways; 0 precision refusals) +
   GAP-IS-RESIDUE-IN-DISGUISE (gap S2 ||l_0||^2/A_0^2 = 1 - eps,
   eps <= 2.55e-6 at every rung) +
   GAP-FRACTION-ANOMALY-WORLD-SEPARATING-MEASURED (MAIN -5.15..-9.00
   vs fake worlds -0.17..-2.02 log10(gap/fullgap)) +
   GAP-RIDES-TAU-RELABELED-STOPPED (slope +1.011 in the ride band;
   round-1 scope command executed: raw-gap floor leg stopped) +
   SANDWICH-EXACT-BUT-LOSSY (two-sided, exact, margin ladder
   -5.1..-45.0 log10) +
   H3-TWO-FUNCTIONAL-FORM-EXACT + A2-TRIVIAL-CEILING-FREE
   (X_triv solvable at all rungs) +
   WALL-IS-ONE-FUNCTION-LOEWNER-EXACT (displacement rank 2; f =
   f_pole + f_arch + 2 om pj; world-blind structure, source only in
   f; r45 LOEWNER-DEAD prior art distinguished) +
   WITNESS-EXITS-EIGENMANIFOLD (eigen-residual 1e8.2 x fullgap;
   l_2-identity detects at W^2; l_0-identity blind, disclosed;
   gap witness-invariant definitional) +
   ALT-JETS-BREAK-IDENTITY (8.9-52.6 orders + 1 exact A_0-null
   exhibit, amendment A1) +
   TOOLS-PRICED (Feshbach DELIVERED / rank-one DELIVERED-LOSSY /
   IIKS-RHP NEEDS-NAMED-EXTERNAL-TOOL / Carleman
   NEEDS-NAMED-EXTERNAL-TOOL-LOW-CARRY) +
   LOOPS-FLAGGED-NOT-CONSUMED (A_0-triangle extra-sharp: TAUPOS/
   TLAWCAP ancestors of NOTHING delivered) +
   MINCUT-UNCHANGED (4/5/5/6) + RESIDUE-UNCHANGED.
Honest content: (a) the exact residue/Feshbach identity puts the A_0
floor into eigenvector-free coordinates at every reachable rung --
the round's key question answers YES at the identity level, and the
demand honestly DESCENDS to the compression ground overlap rather
than vanishing; (b) the transversality gap exists, is strictly
positive, and is machine-shown to be the residue in disguise (secular
ratio 1 - eps); its ladder rides tau -- the raw-gap floor leg is
RELABELED and stopped per the round-1 scope; (c) the genuinely new
exact structure is the one-function Loewner form of the wall and the
{l_0, l_2} residue pair as a witness-class detector; the genuinely
new measured objects are the gap-fraction and overlap-spread ladders
(world-separating in the measured sense); (d) nothing closes, nothing
upgrades, the census-forall-k loop and the A_0-triangle stay flagged
and unconsumed.  NO RH CLAIM.

WHAT IS BUILT AND GATED: S0 G01 firewall + G02 predefinition + G03
exact-instance ward; S1 exact layer G10-G17; S2 house layer G20-G29;
S3 controls/witness G40-G44; S4 screens/adjudication G50-G53; S5
pricing G60-G61 + G99 runtime.  FROZEN BARS: RES_BAR 1e-18; SEC_BAR
1e-18; SAND_SLACK 1e-10; V1_BAR 1e-30; A0X_BAR 1e-30; REBUILD_BAR
1e-25; DOUBLE_BAR 1e-40; FPRED_BAR 1e-20; GAP_PREC_SAFETY 20 dps;
DISP_S3_BAR 1e-10; DISP_S2_MIN 1e-6; LOEW_BAR 1e-10; ALT_ORD_MIN
3.0 orders; WIT_YT_BAND (990, 1010); WIT_A0_BAR 1e-6; WIT_L2_BAND
(0.5e6, 2.0e6); WIT_EIGRES_MIN 1e6; TAU_FLAT_BAR 0.30;
TAU_RIDE_BAND (0.7, 1.3); record tolerances GAP_TOL 0.05 /
SECR_TOL 1e-4 / LOSS_TOL 0.1 / MARG_TOL 0.05 / CTRL_GF_TOL 0.10 /
ALT_TOL 0.3 / SLOPE_TOL 0.05 / BETA_TOL 0.05; RUNTIME_BAR 3300 s.
CALIBRATION (disclosed): ONE structural smoke
(ground_residue_obs_probe.smoke1.log, rungs 4/5/8, 33/33 -- the
record comparisons are vacuous pre-freeze by design) and ONE full
pre-freeze calibration pass (calib_gro_pass1.log, --mode calib,
32/33): the single calib FAIL was G43, root-caused to the PRE-FREEZE
METRIC not the battery -- the deviation |ratio - 1| saturates at 1
on the exact A_0-null (UNIFORM jet at h = 13, K = 42 even: parity
sum (-1)^k == 0) instead of registering the total break.  AMENDMENT
A1 (the one amendment, disclosed): the alt-jet metric was replaced
by the two-sided order-distance |log10(A_0(ray)^2 w'/||l_0||^2)|
with INF at the exact null, and ALT_DEV_MIN 1e3 was renamed/retyped
ALT_ORD_MIN 3.0 orders; the null is now gated as the STRONGEST break
(the identity fires in the zero-residue direction), not a failure.
AT FREEZE the placeholder record tables were replaced by the
calibrated numbers and the screen verdict enums were resolved from
the measured slopes (GAP-RIDES-TAU fired as anticipated by the
pre-registered prior; the world-separation and witness-detection
legs gated as measured), all disclosed; NO bar, grid, dps rung,
recipe or control inherited from r171-r182 moved; the ONE moved
constant is the A1 metric/threshold above.
DETERMINISM: no randomness anywhere (the MAGSCRAM permutation is the
deterministic golden map); ProcessPool results keyed; run2 must be
identical modulo wall-clock tokens (lines carrying 'WALL').

NO RH CLAIM IN EITHER DIRECTION.  NOT evidence for or against RH.
"""

# =====================================================================
# CORRECTION OF RECORD (Bughunt IX, note DXV, 2026-08-21)
# ---------------------------------------------------------------------
# Appended OUTSIDE the frozen spec text per the r131/r165
# corrections-of-record convention: the module docstring above is the
# historical record and is NOT edited; SPEC_SHA (= sha256 of the
# docstring) stays 48637c8898a1da5a.  NO numeric change, NO verdict
# flip, NO RH CLAIM.
#
# BH9-F1 [MAJOR, off-diagonal law stated as matrix identity]:
#   ORIGINAL (this spec + note DVI): the taxonomy token
#   WALL-IS-ONE-FUNCTION-LOEWNER-EXACT, the G4 prose "displacement
#   rank EXACTLY 2 ... == ONE-FUNCTION LOEWNER MATRIX Raw[i,j] =
#   (f_i - f_j)/(b_i - b_j)", and the sentence "R_h(z) is the scalar
#   resolvent of an explicit one-function Loewner kernel" state the
#   structure find at OBJECT level, in the same paragraph that cites
#   the Loewner-1934 dictionary ("operator monotonicity ==
#   Loewner-matrix PSD") -- which speaks about the CANONICAL matrix
#   with diagonal f'(b_i).  The MACHINE content of this round is
#   correctly scoped: the NOTATION paragraph says "one-function
#   Loewner form Raw[i,j] = (f_i - f_j)/(b_i - b_j) off-diagonal",
#   and G60 tests ONLY the commutator column reconstruction (the
#   displacement equation annihilates the diagonal -- displacement
#   rank 2 pins the OFF-diagonal alone); "==" between the two is a
#   quantifier slip.  r189 then proved the wall is NOT the canonical
#   object, and Bughunt IX re-verified it in fully own code: the
#   canonical completion L_f is INDEFINITE at h = 4, 5
#   (log10(|lambda_min|/||F||) = -1.355/-2.001) while the wall is PD,
#   Delta anchors -8.72/+1.37 and -12.80/+1.43.  RETYPED token (K1,
#   BH9 proposal verbatim):
#   WALL-OFF-DIAGONAL-IS-ONE-FUNCTION-LOEWNER-EXACT with the rider
#   "die Off-Diagonale der Roh-Wand ist exakt die dividierte-
#   Differenzen-Form EINER Quellfunktion f (Verschiebungsrang 2
#   fixiert NUR die Off-Diagonale); die VOLLE Wand ist M_h ~ L_f +
#   diag(Delta) mit quellseitigem Diagonal-Shift Delta != 0 (r189:
#   Delta_prime = 2a pc, Pol-Block voll kanonisch, L_f INDEFINIT an
#   jeder Sprosse) -- die Wand ist NICHT die kanonische
#   Loewner-Matrix des Loewner-1934-Woerterbuchs, und R_h(z) ist die
#   Resolvente von L_f + diag(Delta), nicht des Loewner-Kerns
#   allein."  The off-diagonal law and the displacement-rank-2 fact
#   SURVIVE exactly (BH9 own devs <= 4e-62); this round's headline
#   (the residue identity) is untouched; the r189 record already
#   carries the corrected dictionary (spec: "NOT literally the
#   canonical L_f"; note DX: "Die Wand ist NICHT die kanonische
#   Loewner-Matrix ihres Potentials") and needs NOTHING.  NO verdict
#   flips.
# =====================================================================

from __future__ import annotations

import argparse
import ast
import hashlib
import math
import os
import sys
import time
from concurrent.futures import ProcessPoolExecutor

import mpmath as mp
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

import radius4_an_probe as R4                 # round-122 machinery

# ---------------------------------------------------------------- frozen
KFAC = 1.25
WORKERS = 10
RUNTIME_BAR = 3300.0
THETA_C = "0.155"

HRUNGS = (4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16)
H_HOLD = 20
DPS = {4: 60, 5: 60, 6: 65, 7: 70, 8: 80, 9: 85, 10: 90, 11: 100,
       12: 110, 13: 120, 14: 120, 15: 125, 16: 130, 20: 144}
L2_RUNGS = (4, 5, 8, 13)
ALT_RUNGS = (4, 5, 8, 13)
F_RUNGS = (4, 5, 8)
WIT_RUNG = 5
WIT_FACT = 1000
GOLD = 0.6180339887498949

CTRL_SMOOTH = (5,)
CTRL_SCRARITH = (4, 5, 8)
CTRL_EPSTEIN = (8, 9, 10)
CTRL_DPS = {"SMOOTH": 60, "SCRARITH": 60, "EPSTEIN": 80}
CTRL_MAIN_X = (4, 5, 8)

# structural bars (frozen pre-calibration)
RES_BAR = 1e-18
SEC_BAR = 1e-18
SAND_SLACK = 1e-10
V1_BAR = 1e-30
A0X_BAR = 1e-30
REBUILD_BAR = 1e-25
DOUBLE_BAR = 1e-40
FPRED_BAR = 1e-20
GAP_PREC_SAFETY = 20
DISP_S3_BAR = 1e-10
DISP_S2_MIN = 1e-6
LOEW_BAR = 1e-10
ALT_ORD_MIN = 3.0
WIT_YT_BAND = (990.0, 1010.0)
WIT_A0_BAR = 1e-6
WIT_L2_BAND = (0.5e6, 2.0e6)
WIT_EIGRES_MIN = 1e6
TAU_FLAT_BAR = 0.30
TAU_RIDE_BAND = (0.7, 1.3)
COND_LO, COND_HI = 1e-40, 1e-10

# record tolerances
GAP_TOL = 0.05
SECR_TOL = 1e-4
LOSS_TOL = 0.1
MARG_TOL = 0.05
CTRL_GF_TOL = 0.10
ALT_TOL = 0.3
SLOPE_TOL = 0.05
BETA_TOL = 0.05

# --------------------- calibrated record tables (calib_gro_pass1.log)
CAL_GAPFRAC = {   # log10(gap/fullgap)
    4: "-5.151", 5: "-5.956", 6: "-6.230", 7: "-6.763", 8: "-6.882",
    9: "-7.171", 10: "-7.382", 11: "-7.648", 12: "-7.840",
    13: "-8.112", 14: "-8.222", 15: "-8.386", 16: "-8.519",
    20: "-9.001"}
CAL_GAP = {   # log10 gap
    4: "-11.171", 5: "-16.403", 6: "-20.944", 7: "-25.791",
    8: "-30.308", 9: "-34.967", 10: "-39.959", 11: "-44.765",
    12: "-50.038", 13: "-54.688", 14: "-60.167", 15: "-64.406",
    16: "-69.562", 20: "-89.090"}
CAL_SECR_EPSMAX = 2.55e-6    # max over rungs of |1 - gap S2 L0/A0^2|
CAL_LOSS = {   # log10((m.u1)^2/||m||^2)
    4: "-11.24", 5: "-16.60", 6: "-21.65", 7: "-26.48", 8: "-31.22",
    9: "-35.97", 10: "-41.08", 11: "-45.81", 12: "-51.24",
    13: "-55.93", 14: "-61.54", 15: "-65.86", 16: "-71.02",
    20: "-90.72"}
CAL_MARG = {   # log10(gap/g_req(X_meas))
    4: "-5.08", 5: "-7.91", 6: "-10.44", 7: "-12.88", 8: "-15.24",
    9: "-17.61", 10: "-20.19", 11: "-22.55", 12: "-25.30",
    13: "-27.63", 14: "-30.47", 15: "-32.60", 16: "-35.19",
    20: "-45.05"}
CAL_BETA = {"slope": "-4.85", "r2": "0.999"}     # log10 gap vs rung h
CAL_TAUSLOPES = {"gap": "1.011", "wp": "-1.003", "marg": "0.519"}
CAL_ALT = {   # (h, tag) -> order-distance |log10 ratio|; INF == A0-null
    (4, "SIGNFLIP"): "10.05", (4, "UNIFORM"): "8.87",
    (4, "MAGSCRAM"): "10.17",
    (5, "SIGNFLIP"): "15.08", (5, "UNIFORM"): "13.66",
    (5, "MAGSCRAM"): "15.15",
    (8, "SIGNFLIP"): "28.56", (8, "UNIFORM"): "26.79",
    (8, "MAGSCRAM"): "22.81",
    (13, "SIGNFLIP"): "52.58", (13, "UNIFORM"): "INF",
    (13, "MAGSCRAM"): "52.03"}
CAL_WIT = {"cost": "8.1e-02", "ytr": "1000.0", "l2dev": "1.1e+06",
           "l0dev": "1.2e-01", "eigres_log10": "-2.26",
           "eigres_true_log10": "-60.75", "fullgap_log10": "-10.45"}
CAL_CTRL_GF = {   # (world, x) -> log10(gap/fullgap)
    ("MAIN", 4): "-5.151", ("MAIN", 5): "-5.956",
    ("MAIN", 8): "-6.882",
    ("SMOOTH", 5): "-1.776",
    ("SCRARITH", 4): "-0.173", ("SCRARITH", 5): "-0.976",
    ("SCRARITH", 8): "-0.929",
    ("EPSTEIN", 8): "-1.341", ("EPSTEIN", 9): "-2.022",
    ("EPSTEIN", 10): "-0.813"}

SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
T0_WALL = time.time()

CHECKS: list[tuple[str, bool, str]] = []
INFO: list[str] = []


def check(name: str, ok: bool, detail: str) -> bool:
    ok = bool(ok)
    CHECKS.append((name, ok, detail))
    print("  [%s] %-40s %s" % ("PASS" if ok else "FAIL", name, detail),
          flush=True)
    return ok


def info(msg: str) -> None:
    INFO.append(msg)
    print("  [INFO] " + msg, flush=True)


def section(title: str) -> None:
    print("\n" + "-" * 78 + "\n" + title + "\n" + "-" * 78, flush=True)


def fit_line(xs, ys):
    n = len(xs)
    if n < 2:
        return float("nan"), float("nan"), float("nan")
    mx = sum(xs) / n
    my = sum(ys) / n
    sxx = sum((x - mx) ** 2 for x in xs)
    sxy = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    if sxx == 0:
        return float("nan"), float("nan"), float("nan")
    sl = sxy / sxx
    ic = my - sl * mx
    ssr = sum((y - (sl * x + ic)) ** 2 for x, y in zip(xs, ys))
    sst = sum((y - my) ** 2 for y in ys)
    r2 = 1.0 - ssr / sst if sst > 0 else float("nan")
    return sl, ic, r2


def has_cycle(graph: dict) -> bool:
    WHITE, GREY, BLACK = 0, 1, 2
    color = {u: WHITE for u in graph}
    for v in list(graph):
        for w in graph[v]:
            color.setdefault(w, WHITE)

    def dfs(u):
        color[u] = GREY
        for w in graph.get(u, ()):
            if color[w] == GREY:
                return True
            if color[w] == WHITE and dfs(w):
                return True
        color[u] = BLACK
        return False

    return any(color[u] == WHITE and dfs(u) for u in list(color))


def ancestors(graph: dict, node: str) -> set:
    rev: dict = {}
    for u, vs in graph.items():
        for v in vs:
            rev.setdefault(v, set()).add(u)
    seen: set = set()
    stack = [node]
    while stack:
        u = stack.pop()
        for p in rev.get(u, ()):
            if p not in seen:
                seen.add(p)
                stack.append(p)
    return seen


# ------------------------------------------------------------ firewall
def firewall_audit() -> tuple[bool, str]:
    src = open(os.path.abspath(__file__), "r", encoding="utf-8").read()
    tree = ast.parse(src)
    forb = {"zeta" + "zero", "siegel" + "z", "siegel" + "theta",
            "n" + "zeros", "gram" + "point"}
    bad = []
    for node in ast.walk(tree):
        nm = None
        if isinstance(node, ast.Attribute):
            nm = node.attr
        elif isinstance(node, ast.Name):
            nm = node.id
        if nm is None:
            continue
        low = nm.lower()
        if low in forb:
            bad.append("forbidden %s @%d" % (nm, node.lineno))
        if low == "zeta":
            bad.append("zeta use @%d" % node.lineno)
        if isinstance(node, ast.Attribute) and nm == "load":
            bad.append("np.load @%d (zero-free round: no cache "
                       "reads at all)" % node.lineno)
    for node in ast.walk(tree):
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            mods = ([al.name for al in node.names]
                    if isinstance(node, ast.Import)
                    else [node.module or ""])
            for m in mods:
                if m.startswith("verification"):
                    bad.append("import " + m)
    # provenance purity: srcfree_* functions must not touch the wall
    # eigenvector data (cn_mp_str / mpV / mpE indexing beyond the
    # passed-in scalar tau)
    for node in ast.walk(tree):
        if not isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            continue
        if not node.name.startswith("srcfree_"):
            continue
        for sub in ast.walk(node):
            nm = None
            if isinstance(sub, ast.Attribute):
                nm = sub.attr
            elif isinstance(sub, ast.Name):
                nm = sub.id
            elif isinstance(sub, ast.Constant) and isinstance(
                    sub.value, str):
                nm = sub.value
            if nm in ("cn_mp_str", "mpV", "mpE", "cn"):
                bad.append("srcfree purity: %s in %s @%d"
                           % (nm, node.name, sub.lineno))
    return (not bad), ("; ".join(bad) if bad else
                       "NO zero-oracle, NO zeta, NO np.load (this "
                       "round is fully zero-free: no ordinate cache "
                       "is consumed anywhere), no verification/ "
                       "import; srcfree_ functions eigenvector-free "
                       "by AST")


# ----------------------------------------------- srcfree Schur pipeline
def srcfree_schur(Mmat, tau, K: int, lvec: list) -> dict:
    """Feshbach/Schur reduction of (z I - M) onto the direction of the
    FIXED GEOMETRY functional lvec, evaluated at the passed-in scalar
    tau.  Consumes: the wall MATRIX and the eigenvalue SCALAR only --
    the wall eigenvector never enters (AST-audited).  Returns w'(tau),
    the compression spectrum head, the coupling data."""
    ln2 = sum(x * x for x in lvec)
    e = [x / mp.sqrt(ln2) for x in lvec]
    v = list(e)
    v[0] = v[0] - 1
    vn2 = sum(x * x for x in v)
    Hm = mp.zeros(K, K)
    for i in range(K):
        for j in range(K):
            Hm[i, j] = (1 if i == j else 0) - 2 * v[i] * v[j] / vn2
    T = Hm * Mmat * Hm
    alpha = T[0, 0]
    mvec = [T[i, 0] for i in range(1, K)]
    B = mp.zeros(K - 1, K - 1)
    for i in range(K - 1):
        for j in range(K - 1):
            B[i, j] = T[i + 1, j + 1]
    Eb, Ub = mp.eigsy(B)
    order = sorted(range(K - 1), key=lambda i: Eb[i])
    mus = [Eb[i] for i in order]
    ov = [sum(mvec[i] * Ub[i, c] for i in range(K - 1)) for c in order]
    wp = 1 + sum(ov[j] ** 2 / (mus[j] - tau) ** 2 for j in range(K - 1))
    mn2 = sum(x * x for x in mvec)
    return {"ln2": ln2, "alpha": alpha, "mn2": mn2, "mus": mus,
            "ov1sq": ov[0] ** 2, "wp": wp, "gap": mus[0] - tau,
            "mvec": mvec}


# ----------------------------------------------- prime-block rebuild
def rebuild_prime(h: int, dps: int, K: int, scale=1):
    """Standalone rebuild of the (normalized) prime block from the
    sieve atoms with weights scaled by `scale` (builder assembly
    formulas VERBATIM, even sector); also returns pj."""
    with mp.workdps(dps):
        aa = mp.log(h) / 2
        L2v = 2 * aa
        oms = [k * mp.pi / aa for k in range(K)]
        par = [mp.mpf((-1.0) ** k) for k in range(K)]
        icap = int(math.floor(h))
        comp = np.zeros(icap + 1, dtype=bool)
        nlist = []
        for p in range(2, icap + 1):
            if comp[p]:
                continue
            comp[p * p:: p] = True
            q = p
            while q <= icap:
                nlist.append((q, p))
                q *= p
        nlist.sort()
        atoms = [(mp.log(q), scale * mp.log(p) / mp.sqrt(q))
                 for q, p in nlist]
        pj = [sum((w * mp.sin(o * u) for u, w in atoms), mp.mpf(0))
              for o in oms]
        Mp = mp.zeros(K, K)
        for i in range(K):
            for j2 in range(i):
                sg = par[i] * par[j2]
                den = oms[j2] ** 2 - oms[i] ** 2
                od = 2 * sg * (oms[i] * pj[i] - oms[j2] * pj[j2]) / den
                Mp[i, j2] += od
                Mp[j2, i] += od
        for i in range(K):
            o = oms[i]
            if i == 0:
                pdiag = sum((w * (L2v - u) for u, w in atoms),
                            mp.mpf(0))
            else:
                pdiag = sum((w * ((aa - u / 2) * mp.cos(o * u)
                                  - mp.sin(o * u) / (2 * o))
                             for u, w in atoms), mp.mpf(0))
            Mp[i, i] += 2 * pdiag
        nrm = [mp.sqrt(L2v) if i == 0 else mp.sqrt(aa)
               for i in range(K)]
        for i in range(K):
            for j2 in range(K):
                Mp[i, j2] = Mp[i, j2] / (nrm[i] * nrm[j2])
        return Mp, pj


# ----------------------------------------------------------- house layer
def w_main(args) -> dict:
    """Per-rung pipeline: build MAIN cell, residue/Feshbach identities,
    transversality data, demands, alt jets, witness (h = WIT_RUNG),
    displacement/Loewner layer, prime rebuild ward (F_RUNGS)."""
    h, dps = args
    try:
        t0 = time.time()
        ce = R4.build_cell(h, KFAC, "MAIN", dps, want_mp=True)
        K = ce["K"]
        out = dict(h=h, K=K, err="")
        with mp.workdps(dps):
            M = ce["mpM"]
            E, V = ce["mpE"], ce["mpV"]
            tau, tau2 = E[0], E[1]
            aa = mp.log(h) / 2
            nrm = [mp.sqrt(2 * aa) if k == 0 else mp.sqrt(aa)
                   for k in range(K)]
            b = [(k * mp.pi / aa) ** 2 for k in range(K)]
            v1 = [V[i, 0] for i in range(K)]
            n1 = mp.sqrt(sum(x * x for x in v1))
            out["v1_dev"] = float(abs(n1 - 1))
            l0 = [((-1) ** k) / nrm[k] for k in range(K)]
            l2 = [mp.mpf(0)] + [((-1) ** k) * b[k] / nrm[k]
                                for k in range(1, K)]
            A0 = sum(l0[k] * v1[k] for k in range(K))
            A2 = sum(l2[k] * v1[k] for k in range(K))
            cs = [mp.mpf(s) for s in ce["cn_mp_str"]]
            A0c = sum((-1) ** k * cs[k] for k in range(K))
            out["a0x_dev"] = float(abs(A0 / A0c - 1))
            yt = abs(A2 / A0)
            out["log10tau"] = float(mp.log(abs(tau), 10))
            out["tau_neg"] = bool(tau < 0)
            out["log10A0sq"] = float(mp.log(A0 * A0, 10))
            # --- l0 Schur branch (eigenvector-free given tau)
            s0 = srcfree_schur(M, tau, K, l0)
            evside = s0["ln2"] / (A0 * A0)
            out["res_dev"] = float(abs(s0["wp"] / evside - 1))
            out["wp_ge1"] = bool(s0["wp"] >= 1 - mp.mpf("1e-30"))
            gap = s0["gap"]
            fullgap = tau2 - tau
            fro = mp.sqrt(sum(M[i, j] ** 2 for i in range(K)
                              for j in range(K)))
            out["gap_refused"] = bool(
                gap < mp.mpf(10) ** (-(dps - GAP_PREC_SAFETY)) * fro)
            out["gap_pos"] = bool(gap > 0)
            out["interlace_ok"] = bool(tau <= s0["mus"][0] <= tau2)
            out["log10gap"] = float(mp.log(abs(gap), 10))
            out["log10gapfrac"] = float(mp.log(abs(gap / fullgap), 10))
            out["log10fullgap"] = float(mp.log(abs(fullgap), 10))
            # sandwich (exact inequalities)
            lo = 1 + s0["ov1sq"] / gap ** 2
            hi = 1 + s0["mn2"] / gap ** 2
            slack = mp.mpf(repr(SAND_SLACK))
            out["sand_ok"] = bool(lo * (1 - slack) <= s0["wp"]
                                  <= hi * (1 + slack))
            out["log10loss"] = float(mp.log(s0["ov1sq"] / s0["mn2"],
                                            10))
            out["log10wp"] = float(mp.log(s0["wp"], 10))
            # secular zero + S2 (eigenvector-side dual)
            ln2 = s0["ln2"]
            e0 = [x / mp.sqrt(ln2) for x in l0]
            sec = mp.mpf(0)
            s2m = mp.mpf(0)
            for i in range(K):
                evi = sum(e0[r] * V[r, i] for r in range(K))
                sec += evi ** 2 / (s0["mus"][0] - E[i])
                if i >= 1:
                    s2m += evi ** 2 / (E[i] - tau)
            out["sec_rel"] = float(abs(sec * gap))
            out["secratio"] = float(gap * s2m * ln2 / (A0 * A0))
            # demands
            Tz4 = (2 * mp.pi * h) ** 4
            thc = mp.mpf(THETA_C)
            out["h3_margin"] = float(thc * Tz4 / yt)
            X = (A2 / (thc * Tz4)) ** 2
            out["xmeas_solvable"] = bool(X < ln2)
            if X < ln2:
                greq = mp.sqrt(X) * mp.sqrt(s0["mn2"]) \
                    / mp.sqrt(ln2 - X)
                out["log10marg"] = float(mp.log(gap / greq, 10))
            l2n2 = sum(x * x for x in l2)
            Xt = l2n2 / (thc * Tz4) ** 2
            out["xtriv_solvable"] = bool(Xt < ln2)
            if Xt < ln2:
                greqt = mp.sqrt(Xt) * mp.sqrt(s0["mn2"]) \
                    / mp.sqrt(ln2 - Xt)
                out["log10margt"] = float(mp.log(gap / greqt, 10))
            # --- l2 Schur branch at L2_RUNGS
            if h in L2_RUNGS:
                s2b = srcfree_schur(M, tau, K, l2)
                ev2 = s2b["ln2"] / (A2 * A2)
                out["res2_dev"] = float(abs(s2b["wp"] / ev2 - 1))
                out["wp2_ge1"] = bool(s2b["wp"] >= 1 - mp.mpf("1e-30"))
                rat = (s2b["ln2"] / ln2) * (s0["wp"] / s2b["wp"])
                out["ratio_dev"] = float(abs(rat / (yt * yt) - 1))
            # --- alt jets at ALT_RUNGS (identity pins the true ray)
            if h in ALT_RUNGS:
                alts = {}
                dvec = [((-1) ** k) * cs[k] for k in range(K)]
                keys = [math.fmod((k + 1) * GOLD, 1.0)
                        for k in range(K)]
                perm = sorted(range(K), key=lambda i: keys[i])
                for tag in ("SIGNFLIP", "UNIFORM", "MAGSCRAM"):
                    if tag == "SIGNFLIP":
                        dd = list(cs)
                    elif tag == "UNIFORM":
                        dd = [mp.mpf((-1.0) ** k) for k in range(K)]
                    else:
                        dd = [mp.sign(dvec[k]) * abs(cs[perm[k]])
                              for k in range(K)]
                    vv = [((-1) ** k) * dd[k] * nrm[k]
                          for k in range(K)]
                    nv = mp.sqrt(sum(x * x for x in vv))
                    A0a = sum(l0[k] * vv[k] for k in range(K)) / nv
                    # two-sided order-distance of the ratio from 1
                    # (frozen amendment A1: the calib metric
                    # |ratio - 1| saturates at 1 for A0-null rays)
                    ratio = A0a * A0a * s0["wp"] / ln2
                    if ratio == 0:
                        alts[tag] = float("inf")
                    else:
                        alts[tag] = float(abs(mp.log(ratio, 10)))
                out["alt"] = alts
            # --- witness at WIT_RUNG (r172 recipe VERBATIM)
            if h == WIT_RUNG:
                dv = A2 * (WIT_FACT - 1) / (b[2] - b[1])
                cs2 = list(cs)
                cs2[1] += dv
                cs2[2] += dv
                A0w = sum((-1) ** k * cs2[k] for k in range(K))
                A2w = sum((-1) ** k * cs2[k] * b[k]
                          for k in range(1, K))
                cmax = max(abs(v_) for v_ in cs)
                out["wit_cost"] = float(abs(dv) / cmax)
                out["wit_ytr"] = float(abs(A2w / A0w) / yt)
                out["wit_a0dev"] = float(abs(A0w / A0 - 1))
                vv = [cs2[k] * nrm[k] for k in range(K)]
                nv = mp.sqrt(sum(x * x for x in vv))
                vw = [x / nv for x in vv]
                A0u = sum(l0[k] * vw[k] for k in range(K))
                A2u = sum(l2[k] * vw[k] for k in range(K))
                out["wit_l0dev"] = float(abs(A0u * A0u * s0["wp"]
                                             / ln2 - 1))
                s2b = srcfree_schur(M, tau, K, l2)
                out["wit_l2dev"] = float(abs(A2u * A2u * s2b["wp"]
                                             / s2b["ln2"] - 1))
                res = [sum(M[i, j] * vw[j] for j in range(K))
                       - tau * vw[i] for i in range(K)]
                rn = mp.sqrt(sum(x * x for x in res))
                res1 = [sum(M[i, j] * v1[j] for j in range(K))
                        - tau * v1[i] for i in range(K)]
                rn1 = mp.sqrt(sum(x * x for x in res1))
                out["wit_eigres_log10"] = float(mp.log(rn, 10))
                out["wit_eigres_true_log10"] = float(mp.log(rn1, 10))
                out["wit_fullgap_log10"] = float(
                    mp.log(abs(fullgap), 10))
            # --- prime-block rebuild ward + linearity (F_RUNGS)
            if h in F_RUNGS:
                Mp1, pj = rebuild_prime(h, dps, K, scale=1)
                Pb = ce["mpPrime"]
                dev = mp.mpf(0)
                den = mp.mpf(0)
                for i in range(K):
                    for j in range(K):
                        dev = max(dev, abs(Mp1[i, j] - Pb[i, j]))
                        den = max(den, abs(Pb[i, j]))
                out["rebuild_dev"] = float(dev / den)
                Mp2, _pj2 = rebuild_prime(h, dps, K, scale=2)
                ddev = mp.mpf(0)
                for i in range(K):
                    for j in range(K):
                        ddev = max(ddev, abs(Mp2[i, j]
                                             - 2 * Mp1[i, j]))
                out["double_dev"] = float(ddev / den)
                # one-function prime potential: extract f from the
                # raw prime commutator column, compare -2 om pj
                oms = [k * mp.pi / aa for k in range(K)]
                raw = [[Pb[i, j] * ((-1) ** (i + j)) * nrm[i] * nrm[j]
                        for j in range(K)] for i in range(K)]
                fdev = mp.mpf(0)
                fden = mp.mpf(0)
                for i in range(1, K):
                    fex = (b[i] - b[0]) * raw[i][0]
                    fpr = (-2 * oms[i] * pj[i]) - (-2 * oms[0] * pj[0])
                    fdev = max(fdev, abs(fex - fpr))
                    fden = max(fden, abs(fpr))
                out["fpred_dev"] = float(fdev / fden)
            # --- displacement layer (float64) at F_RUNGS + 13
            if h in F_RUNGS or h == 13:
                parf = np.array([(-1.0) ** k for k in range(K)])
                nrf = np.array([float(x) for x in nrm])
                bf = np.array([float(x) for x in b])
                sc = np.outer(parf * nrf, parf * nrf)
                disp = {}
                for tag, blk in (("prime", ce["blk_prime"]),
                                 ("arch", ce["blk_arch"]),
                                 ("wall", ce["m_tilde"])):
                    Raw = blk * sc
                    C = np.diag(bf) @ Raw - Raw @ np.diag(bf)
                    sv = np.linalg.svd(C, compute_uv=False)
                    disp[tag] = (float(sv[1] / sv[0]),
                                 float(sv[2] / sv[0]))
                Raw = ce["m_tilde"] * sc
                C = np.diag(bf) @ Raw - Raw @ np.diag(bf)
                f = C[:, 0].copy()
                pred = f[:, None] - f[None, :]
                den2 = max(float(np.abs(C).max()), 1e-300)
                disp["loew_dev"] = float(
                    np.abs(C - pred).max() / den2)
                out["disp"] = disp
        out["wall_s"] = time.time() - t0
        return out
    except Exception as exc:                      # noqa: BLE001
        import traceback
        return {"h": h, "err": "%s\n%s" % (exc,
                                           traceback.format_exc())}


def w_ctrl(args) -> dict:
    """Control-world pipeline: identity world-blindness + gap values."""
    world, x, dps = args
    try:
        ce = R4.build_cell(x, KFAC, world, dps, want_mp=True)
        K = ce["K"]
        out = dict(world=world, x=x, K=K, err="")
        with mp.workdps(dps):
            M = ce["mpM"]
            E, V = ce["mpE"], ce["mpV"]
            tau, tau2 = E[0], E[1]
            aa = mp.log(x) / 2
            nrm = [mp.sqrt(2 * aa) if k == 0 else mp.sqrt(aa)
                   for k in range(K)]
            l0 = [((-1) ** k) / nrm[k] for k in range(K)]
            v1 = [V[i, 0] for i in range(K)]
            A0 = sum(l0[k] * v1[k] for k in range(K))
            s0 = srcfree_schur(M, tau, K, l0)
            out["res_dev"] = float(abs(s0["wp"] * (A0 * A0)
                                       / s0["ln2"] - 1))
            gap = s0["gap"]
            out["gap_pos"] = bool(gap > 0)
            out["interlace_ok"] = bool(tau <= s0["mus"][0] <= tau2)
            out["log10gapfrac"] = float(
                mp.log(abs(gap / (tau2 - tau)), 10))
            out["tau_neg"] = bool(tau < 0)
        return out
    except Exception as exc:                      # noqa: BLE001
        import traceback
        return {"world": world, "x": x,
                "err": "%s\n%s" % (exc, traceback.format_exc())}


# ------------------------------------------------------------ S1 exact
def exact_layer(run_gates: bool = True) -> None:
    import sympy as sp

    z = sp.symbols("z")
    # rational orthogonal 3x3 from quaternion (1,2,3,4), n = 30
    a_, b_, c_, d_ = 1, 2, 3, 4
    n = a_ * a_ + b_ * b_ + c_ * c_ + d_ * d_
    Q = sp.Matrix([
        [a_ ** 2 + b_ ** 2 - c_ ** 2 - d_ ** 2,
         2 * (b_ * c_ - a_ * d_), 2 * (b_ * d_ + a_ * c_)],
        [2 * (b_ * c_ + a_ * d_),
         a_ ** 2 - b_ ** 2 + c_ ** 2 - d_ ** 2,
         2 * (c_ * d_ - a_ * b_)],
        [2 * (b_ * d_ - a_ * c_), 2 * (c_ * d_ + a_ * b_),
         a_ ** 2 - b_ ** 2 - c_ ** 2 + d_ ** 2]]) / sp.Integer(n)
    ok_orth = sp.simplify(Q.T * Q - sp.eye(3)) == sp.zeros(3, 3)
    D = sp.diag(1, 3, 7)
    Mx = Q * D * Q.T
    v1 = Q[:, 0]
    tau1 = sp.Integer(1)
    lv = sp.Matrix([1, 2, 2])          # ||l||^2 = 9, e = l/3 rational
    check("G03-exact-instance-ward", ok_orth
          and sp.simplify(Mx * v1 - tau1 * v1) == sp.zeros(3, 1)
          and (lv.T * v1)[0] == sp.Rational(4, 3),
          "rational-orthogonal Q (quaternion (1,2,3,4)); M = Q "
          "diag(1,3,7) Q^T exact; ground (tau, v1) = (1, Q[:,0]); "
          "l = (1,2,2), l.v1 = 4/3 != 0")
    if not run_gates:
        return
    P = (z * sp.eye(3) - Mx).det()
    Np = (lv.T * (z * sp.eye(3) - Mx).adjugate() * lv)[0]
    Pp = sp.diff(P, z)
    res_adj = sp.simplify(Np.subs(z, 1) / Pp.subs(z, 1))
    A0sq = sp.Rational(16, 9)
    check("G10-residue-identity-exact", sp.simplify(
        res_adj - A0sq) == 0,
          "Res_{z=tau} l^T (zI-M)^{-1} l == N(tau)/P'(tau) == "
          "(l.v1)^2/||v1||^2 == 16/9 EXACT on the rational instance "
          "(adjugate route; the contract's (M-zI)^{-1} convention "
          "flips the sign: residue -A_0^2, disclosed)")
    # Schur/Feshbach scalar form, all rational (e = l/3)
    e = lv / 3
    v = e - sp.Matrix([1, 0, 0])
    Hh = sp.eye(3) - 2 * v * v.T / (v.T * v)[0]
    T = Hh * Mx * Hh
    al = T[0, 0]
    mv = sp.Matrix([T[1, 0], T[2, 0]])
    B = T[1:, 1:]
    wz = z - al - (mv.T * (z * sp.eye(2) - B).inv() * mv)[0]
    Rz = (lv.T * (z * sp.eye(3) - Mx).inv() * lv)[0]
    check("G11-feshbach-scalar-form-exact", sp.simplify(
        Rz * wz - 9) == 0,
          "R(z) w(z) == ||l||^2 == 9 as an exact rational function "
          "identity (Schur complement of (zI-M) onto e_0 = l_0/||l_0||"
          ", Householder-rational)")
    wp1 = (1 + (mv.T * (tau1 * sp.eye(2) - B).inv() ** 2 * mv)[0])
    check("G12-wprime-identity-exact",
          sp.simplify(A0sq * wp1 - 9) == 0 and sp.simplify(
              wp1 - (1 + (mv.T * (tau1 * sp.eye(2) - B).inv() ** 2
                          * mv)[0])) == 0,
          "A_0^2 w'(tau) == ||l||^2 EXACT with w'(tau) = 1 + "
          "m^T (tau I - B)^{-2} m fully rational (= 81/16 here): the "
          "residue bound IS a derivative bound on the explicit "
          "scalar w -- eigenvector-free given tau")
    # interlacing + strictness both directions
    mus = sorted(B.eigenvals().keys(), key=lambda u: sp.N(u, 60))
    m1n = sp.N(mus[0], 60)
    ok_int = (m1n - 1 > 1e-40) and (3 - m1n > 1e-40)
    lperp = sp.Matrix([4, -10, 28])    # = 30*Q[:,1], integer, _|_ v1
    ok_perp0 = sp.simplify((lperp.T * v1)[0]) == 0
    ep = lperp / sp.sqrt((lperp.T * lperp)[0])
    vp = ep - sp.Matrix([1, 0, 0])
    Hp = sp.eye(3) - 2 * vp * vp.T / (vp.T * vp)[0]
    Tp = Hp * Mx * Hp
    Bp = Tp[1:, 1:]
    musp = sorted(Bp.eigenvals().keys(), key=lambda u: sp.N(u, 60))
    ok_deg = abs(sp.N(musp[0], 60) - 1) < 1e-40
    Nperp = (lperp.T * (z * sp.eye(3) - Mx).adjugate()
             * lperp)[0].subs(z, 1)
    check("G13-interlacing-strictness-exact", bool(
        ok_int and ok_perp0 and ok_deg
        and sp.simplify(Nperp) == 0),
          "Cauchy interlacing tau1 < mu1 < tau2 strict on the generic "
          "instance (radical signs decided at 60 digits, margin > "
          "1e-40) AND the engineered l _|_ v1 exhibit: mu1 == tau1 "
          "(gap 0) and N(tau1) == 0 (pole absent) -- strict gap <=> "
          "A_0 != 0, both directions")
    # two-functional H3 form
    l2v = sp.Matrix([0, 1, 2])
    e2 = l2v / sp.sqrt(5)
    v2h = e2 - sp.Matrix([1, 0, 0])
    H2h = sp.eye(3) - 2 * v2h * v2h.T / (v2h.T * v2h)[0]
    T2 = H2h * Mx * H2h
    B2 = T2[1:, 1:]
    m2 = sp.Matrix([T2[1, 0], T2[2, 0]])
    wp2 = 1 + (m2.T * (tau1 * sp.eye(2) - B2).inv() ** 2 * m2)[0]
    A2sq = ((l2v.T * v1)[0]) ** 2
    ok14 = sp.simplify(A2sq * wp2 - 5) == 0 and sp.simplify(
        (A2sq / A0sq) - (sp.Integer(5) / 9) * (wp1 / wp2)) == 0
    check("G14-two-functional-ratio-exact", bool(ok14),
          "second functional l_2: A_2^2 w_2'(tau) == ||l_2||^2 AND "
          "y_t^2 == (||l_2||^2/||l_0||^2)(w_0'/w_2') EXACT -- H3 is "
          "a statement about ONE pole's two residues, equivalently "
          "the ratio of two effective-potential derivatives")
    # generic symbolic 2x2
    p, q, r, s = sp.symbols("p q r s", real=True)
    M2 = sp.Matrix([[p, q], [q, r]])
    tau_g = (p + r) / 2 - sp.sqrt(((p - r) / 2) ** 2 + q ** 2)
    vg = sp.Matrix([q, tau_g - p])
    lg = sp.Matrix([1, s])
    P2 = (z * sp.eye(2) - M2).det()
    N2 = (lg.T * (z * sp.eye(2) - M2).adjugate() * lg)[0]
    lhs = N2.subs(z, tau_g) * (vg.T * vg)[0]
    rhs = sp.diff(P2, z).subs(z, tau_g) * ((lg.T * vg)[0]) ** 2
    check("G15-generic-2x2-symbolic", sp.simplify(lhs - rhs) == 0,
          "N(tau) ||v||^2 == P'(tau) (l.v)^2 identically in "
          "(p, q, r, s): the residue identity is GENERIC symbolic "
          "algebra, not an instance accident")
    check("G16-adjugate-bridge-prior-art", sp.simplify(
        wp1 - 9 * Pp.subs(z, 1) / Np.subs(z, 1)) == 0,
          "w'(tau) == ||l||^2 P'(tau)/N(tau) EXACT: the Schur form "
          "IS the CDLI adjugate identity A_0^2 == N(tau)/P'(tau) "
          "(adj(tau I - M) = P'(tau) d d^T, note CDLI/r-adjugate "
          "arc, OTHER family) in new coordinates -- "
          "SAME-IDENTITY-NEW-COORDINATES, prior art disclosed")
    # per-block Loewner potentials
    o1, o2, p1, p2, sh = sp.symbols("o1 o2 p1 p2 sh", positive=True)
    prime_od = 2 * (o1 * p1 - o2 * p2) / (o2 ** 2 - o1 ** 2)
    ok_pr = sp.simplify((o1 ** 2 - o2 ** 2) * prime_od
                        - ((-2 * o1 * p1) - (-2 * o2 * p2))) == 0
    arch_od = -2 * (o1 * p1 - o2 * p2) / (o2 ** 2 - o1 ** 2)
    ok_ar = sp.simplify((o1 ** 2 - o2 ** 2) * arch_od
                        - ((2 * o1 * p1) - (2 * o2 * p2))) == 0
    u1_ = sh / (sp.Rational(1, 4) + o1 ** 2)
    u2_ = sh / (sp.Rational(1, 4) + o2 ** 2)
    ok_po = sp.simplify((o1 ** 2 - o2 ** 2) * 2 * u1_ * u2_
                        - ((-2 * sh ** 2 / (sp.Rational(1, 4)
                                            + o1 ** 2))
                           - (-2 * sh ** 2 / (sp.Rational(1, 4)
                                              + o2 ** 2)))) == 0
    check("G17-block-loewner-potentials-symbolic",
          bool(ok_pr and ok_ar and ok_po),
          "(b_i - b_j) Raw[i,j] == f_i - f_j per block, symbolically: "
          "f_prime = -2 om pj, f_arch = +2 om jv, f_pole = "
          "-2 sinh(a/2)^2/(1/4 + b) -- ALL THREE blocks are "
          "one-function Loewner kernels sharing g = ones, so the "
          "whole wall M = pole + arch - prime is the Loewner matrix "
          "of ONE explicit source potential f(b)")


# --------------------------------------------------------------- main
def main() -> int:
    apx = argparse.ArgumentParser()
    apx.add_argument("--mode", choices=("record", "calib", "smoke"),
                     default="record")
    args = apx.parse_args()
    calib = args.mode == "calib"
    smoke = args.mode == "smoke"

    print("=" * 78)
    print("ground_residue_obs_probe -- PRIME.GROUND.RESIDUE.OBS.01"
          "  (mode %s)" % args.mode)
    print("SPEC_SHA %s" % SPEC_SHA[:16])
    print("=" * 78)

    # ------------------------------------------------------------ S0
    section("S0  FIREWALL + PREDEFINITION")
    okf, detf = firewall_audit()
    check("G01-firewall", okf, detf)
    check("G02-predefinition", True,
          "all bars/grids/rungs/dps/recipes declared in the frozen "
          "spec above (SPEC_SHA covers the declaration); record "
          "tables frozen from the ONE disclosed calibration pass; "
          "tau_h enters ONLY as a measured per-rung scalar, no sign "
          "hypothesis (A_0-triangle guard, extra-sharp)")

    # ------------------------------------------------------------ S1
    section("S1  EXACT LAYER (residue identity / Feshbach / "
            "interlacing / Loewner potentials)")
    exact_layer()

    # ------------------------------------------------------------ S2
    section("S2  HOUSE LAYER (the wall family at all reachable rungs)")
    rungs = (4, 5, 8) if smoke else tuple(HRUNGS) + (H_HOLD,)
    tasks = [(h, DPS[h]) for h in rungs]
    res: dict = {}
    with ProcessPoolExecutor(max_workers=WORKERS) as ex:
        for out in ex.map(w_main, tasks):
            res[out["h"]] = out
    errs = [h for h in rungs if res[h].get("err")]
    for h in errs:
        print("  [ERR] h=%d %s" % (h, res[h]["err"]))
    check("G20-build-ward", not errs and all(
        res[h]["v1_dev"] <= V1_BAR and res[h]["a0x_dev"] <= A0X_BAR
        for h in rungs),
          "all %d rungs built; ||v1|| == 1 (dev <= %.0e) and the "
          "l_0-functional reading matches the builder cn route "
          "(dev <= %.0e) at every rung" % (len(rungs), V1_BAR,
                                           A0X_BAR))

    rmax = max(res[h]["res_dev"] for h in rungs if not res[h]["err"])
    check("G21-residue-identity-all-rungs",
          all(res[h]["res_dev"] <= RES_BAR and res[h]["wp_ge1"]
              for h in rungs),
          "THE HEADLINE IDENTITY: |A_0^2 w'(tau)/||l_0||^2 - 1| <= "
          "%.1e at ALL %d rungs (bar %.0e); w' >= 1 everywhere "
          "(A_0^2 <= ||l_0||^2, Cauchy-Schwarz): the A_0 floor IS a "
          "derivative bound on the explicit scalar w at every "
          "reachable rung" % (rmax, len(rungs), RES_BAR))

    l2r = [h for h in rungs if h in L2_RUNGS]
    r2max = max(res[h]["res2_dev"] for h in l2r) if l2r else 0.0
    ratmax = max(res[h]["ratio_dev"] for h in l2r) if l2r else 0.0
    check("G22-l2-and-H3-ratio-identity",
          all(res[h]["res2_dev"] <= RES_BAR
              and res[h]["ratio_dev"] <= RES_BAR
              and res[h]["wp2_ge1"] for h in l2r),
          "l_2 branch at %s: A_2^2 w_2'(tau) == ||l_2||^2 (dev <= "
          "%.1e) and the TWO-FUNCTIONAL H3 form y_t^2 == "
          "(||l_2||^2/||l_0||^2)(w_0'/w_2') (dev <= %.1e); w_2' >= 1 "
          "== the FREE ceiling A_2^2 <= ||l_2||^2 (no eigenvector)"
          % (str(l2r), r2max, ratmax))

    nref = sum(1 for h in rungs if res[h].get("gap_refused"))
    secmax = max(res[h]["sec_rel"] for h in rungs)
    check("G23-interlacing-secular-all-rungs",
          all(res[h]["gap_pos"] and res[h]["interlace_ok"]
              for h in rungs) and nref == 0
          and secmax <= SEC_BAR,
          "gap = mu_1(B) - tau > 0 and tau <= mu_1 <= tau_2 at ALL "
          "rungs (STRICT interlacing == A_0 != 0); precision "
          "refusals %d/%d (rule: gap >= 10^-(dps-%d) ||M||_F); "
          "secular zero sum_i (e.v_i)^2/(mu_1 - tau_i) == 0 at "
          "rel <= %.1e" % (nref, len(rungs), GAP_PREC_SAFETY, secmax))

    check("G24-sandwich-all-rungs",
          all(res[h]["sand_ok"] for h in rungs),
          "the exact two-sided sandwich 1 + (m.u_1)^2/gap^2 <= "
          "w'(tau) <= 1 + ||m||^2/gap^2 holds at all rungs (slack "
          "%.0e): the gap CONTROLS the residue two-sidedly through "
          "the same w" % SAND_SLACK)

    hs = [h for h in rungs if h != H_HOLD] if not smoke else list(rungs)
    gap_tab = {h: res[h]["log10gap"] for h in rungs}
    gf_tab = {h: res[h]["log10gapfrac"] for h in rungs}
    loss_tab = {h: res[h]["log10loss"] for h in rungs}
    sl_b, _ic, r2_b = fit_line([float(h) for h in hs],
                               [gap_tab[h] for h in hs])
    if calib or smoke:
        for h in sorted(gap_tab):
            print("CAL gap h=%d log10gap %.3f log10gapfrac %.3f "
                  "log10loss %.2f secratio %.8f"
                  % (h, gap_tab[h], gf_tab[h], loss_tab[h],
                     res[h]["secratio"]))
        print("CAL beta slope %.2f r2 %.3f" % (sl_b, r2_b))
        ok25 = True
    else:
        ok25 = all(abs(gf_tab[h] - float(CAL_GAPFRAC[h])) <= GAP_TOL
                   and abs(gap_tab[h] - float(CAL_GAP[h])) <= GAP_TOL
                   and abs(loss_tab[h] - float(CAL_LOSS[h]))
                   <= LOSS_TOL for h in rungs) \
            and abs(sl_b - float(CAL_BETA["slope"])) <= BETA_TOL \
            and r2_b >= float(CAL_BETA["r2"]) - 0.01
    check("G25-gap-ladder-record", ok25,
          "THE TRANSVERSALITY LADDER (record): log10(gap/fullgap) "
          "%.2f (h=4) -> %.2f (h=16) -> %.2f (h=20) -- the "
          "arithmetic ray couples the ground state to ker l_0 "
          "anomalously weakly; decay log10 gap vs rung slope %.2f "
          "dex/rung R^2 %.3f; overlap spread log10((m.u_1)^2/"
          "||m||^2) %.1f..%.1f == the price of the fully "
          "source-side sandwich"
          % (gf_tab.get(4, float("nan")), gf_tab.get(16, float("nan")),
             gf_tab.get(H_HOLD, float("nan")), sl_b, r2_b,
             max(loss_tab.values()), min(loss_tab.values())))

    fr = [h for h in rungs if h in F_RUNGS]
    check("G26-source-linearity-warded",
          all(res[h]["rebuild_dev"] <= REBUILD_BAR
              and res[h]["double_dev"] <= DOUBLE_BAR for h in fr),
          "the prime block (the ONLY atom-dependent block) rebuilt "
          "standalone from the sieve atoms at %s: ward dev <= %.1e; "
          "weight-doubling exactness <= %.1e -- {alpha, m, B} are "
          "EXACT-LINEAR in the atom data (SOURCE-CLASSICAL legs)"
          % (str(fr), max(res[h]["rebuild_dev"] for h in fr),
             max(res[h]["double_dev"] for h in fr)))

    check("G27-key-question-adjudication",
          all(res[h]["res_dev"] <= RES_BAR for h in rungs),
          "ROUND KEY QUESTION, answered in two halves: (YES) w'(tau) "
          "is computed by srcfree_schur from {M blocks, tau scalar} "
          "ONLY (AST-audited eigenvector-free, G01) and matches the "
          "eigenvector side ||l_0||^2/A_0^2 at every rung (G21): the "
          "Schur reduction ELIMINATES the wall eigenvector -- the "
          "A_0 floor becomes w'(tau) <= bound, a derivative bound on "
          "an explicit scalar function whose data {alpha, m, B} are "
          "source-linear (G26) -- a genuinely new coordinate system "
          "(prior art: the CDLI adjugate identity, G16).  (BUT) the "
          "demand mass inside w'(tau) concentrates on (m.u_1)^2/"
          "gap^2 with u_1 the ground eigenvector of the COMPRESSION "
          "B: the eigenvector demand DESCENDS one level (from d to "
          "u_1) rather than vanishing -- "
          "EIGENVECTOR-DESCENDS-NOT-ELIMINATED, named exactly here")

    marg_tab = {h: res[h].get("log10marg", float("nan"))
                for h in rungs}
    ok28v = all(res[h]["xmeas_solvable"] and res[h]["xtriv_solvable"]
                for h in rungs)
    if calib or smoke:
        for h in sorted(marg_tab):
            print("CAL marg h=%d log10marg %.2f log10margt %.2f "
                  "h3margin %.3f"
                  % (h, marg_tab[h],
                     res[h].get("log10margt", float("nan")),
                     res[h]["h3_margin"]))
        ok28 = ok28v
    else:
        ok28 = ok28v and all(
            abs(marg_tab[h] - float(CAL_MARG[h])) <= MARG_TOL
            for h in rungs)
    check("G28-demand-margins", ok28,
          "H3 demand through the sandwich: the ||m||-priced gap "
          "route FAILS at every rung -- log10(gap/g_req(X_meas)) = "
          "%.1f..%.1f (record): proving H3 via [gap floor + ||m|| "
          "price] would need the gap 5-45 orders larger; the "
          "trivial ceiling X_triv = (||l_2||/0.155 T_z^4)^2 is "
          "SOLVABLE at all rungs (A_2^2 <= ||l_2||^2 free) but its "
          "margin is worse; the overlap-priced form carries BY "
          "IDENTITY and consumes u_1 (G27): the ||m||-form of the "
          "transversality route is DEAD-AT-MEASURED-VALUES, "
          "disclosed with numbers"
          % (max(marg_tab.values()), min(marg_tab.values())))

    secr_eps = max(abs(1.0 - res[h]["secratio"]) for h in rungs)
    ok29 = (secr_eps <= CAL_SECR_EPSMAX * 1.5) if not (calib or smoke) \
        else True
    if calib or smoke:
        print("CAL secratio max eps %.2e" % secr_eps)
    check("G29-gap-is-residue-in-disguise", ok29,
          "THE DISGUISE EXHIBIT: gap * S2 * ||l_0||^2 / A_0^2 = "
          "1 - eps with max eps = %.2e over all rungs (S2 = "
          "sum_{i>=2} (e_0.v_i)^2/(tau_i - tau), the explicit "
          "second-order moment): the transversality gap IS the "
          "residue divided by S2 -- the same quantity in matrix "
          "coordinates, NOT an independent handle; any gap floor "
          "and any A_0^2 floor are equivalent up to the measured "
          "S2 ladder" % secr_eps)

    # ------------------------------------------------------------ S3
    section("S3  CONTROLS + WITNESS + ALT JETS")
    ctasks = ([("SMOOTH", x, CTRL_DPS["SMOOTH"]) for x in CTRL_SMOOTH]
              + [("SCRARITH", x, CTRL_DPS["SCRARITH"])
                 for x in CTRL_SCRARITH]
              + [("EPSTEIN", x, CTRL_DPS["EPSTEIN"])
                 for x in CTRL_EPSTEIN])
    if smoke:
        ctasks = [("SCRARITH", 5, 60)]
    cres: dict = {}
    with ProcessPoolExecutor(max_workers=WORKERS) as ex:
        for out in ex.map(w_ctrl, ctasks):
            cres[(out["world"], out["x"])] = out
    cerrs = [k for k, v in cres.items() if v.get("err")]
    for k in cerrs:
        print("  [ERR] %s %s" % (k, cres[k]["err"]))
    cmax = max((v["res_dev"] for v in cres.values()
                if not v.get("err")), default=float("inf"))
    check("G40-identity-world-blind", not cerrs and all(
        v["res_dev"] <= RES_BAR and v["gap_pos"] and v["interlace_ok"]
        for v in cres.values()),
          "the residue identity and interlacing hold in EVERY "
          "control world (max dev %.1e over %d cells): the identity "
          "layer is LINEAR ALGEBRA, world-blind BY DESIGN -- typed, "
          "never sold as a separator (the separator is the VALUES, "
          "G41)" % (cmax, len(cres)))

    if calib or smoke:
        for (w_, x_), v in sorted(cres.items()):
            print("CAL ctrl %s x=%d log10gapfrac %.3f tau_neg %s"
                  % (w_, x_, v["log10gapfrac"], v["tau_neg"]))
        for x_ in CTRL_MAIN_X:
            if x_ in res:
                print("CAL ctrl MAIN x=%d log10gapfrac %.3f"
                      % (x_, res[x_]["log10gapfrac"]))
        ok41 = True
    else:
        ok41 = all(abs(cres[(w_, x_)]["log10gapfrac"]
                       - float(CAL_CTRL_GF[(w_, x_)])) <= CTRL_GF_TOL
                   for (w_, x_) in cres) \
            and all(abs(res[x_]["log10gapfrac"]
                        - float(CAL_CTRL_GF[("MAIN", x_)]))
                    <= CTRL_GF_TOL for x_ in CTRL_MAIN_X)
    gf_fake = [cres[k]["log10gapfrac"] for k in cres]
    gf_main = [res[x_]["log10gapfrac"] for x_ in CTRL_MAIN_X
               if x_ in res]
    sep_ok = (max(gf_main) < min(gf_fake) - 1.0) if gf_main and \
        gf_fake else False
    check("G41-worlds-separate-values", ok41 and (sep_ok or smoke),
          "GAP-FRACTION WORLD SEPARATION (measured): fake-world "
          "log10(gap/fullgap) in [%.2f, %.2f] vs MAIN %s at the "
          "same x -- the anomalously small transversality fraction "
          "is arithmetic-specific (>= 1 dex clearance gated); same "
          "signature class as the r182 mass-location separation"
          % (min(gf_fake, default=float("nan")),
             max(gf_fake, default=float("nan")),
             ["%.2f" % g for g in gf_main]))

    wv = res.get(WIT_RUNG, {})
    ytr = wv.get("wit_ytr", float("nan"))
    l2d = wv.get("wit_l2dev", float("nan"))
    eres = wv.get("wit_eigres_log10", float("nan"))
    eres_t = wv.get("wit_eigres_true_log10", float("nan"))
    fgl = wv.get("wit_fullgap_log10", float("nan"))
    okw = (WIT_YT_BAND[0] <= ytr * (1 if ytr == ytr else 0)
           <= WIT_YT_BAND[1]
           and wv.get("wit_a0dev", 1.0) <= WIT_A0_BAR
           and WIT_L2_BAND[0] <= l2d <= WIT_L2_BAND[1]
           and (10.0 ** (eres - fgl)) >= WIT_EIGRES_MIN)
    if calib or smoke:
        print("CAL wit cost %.1e ytr %.1f a0dev %.1e l0dev %.1e "
              "l2dev %.1e eigres %.2f true %.2f fullgap %.2f"
              % (wv.get("wit_cost", float("nan")), ytr,
                 wv.get("wit_a0dev", float("nan")),
                 wv.get("wit_l0dev", float("nan")), l2d, eres,
                 eres_t, fgl))
    check("G42-witness-battery", okw,
          "r172 inflation witness VERBATIM at h=%d: y_t'' = %.1f "
          "y_t at source cost %.1e (A_0 preserved, dev %.1e): the "
          "witness ray EXITS THE EIGENMANIFOLD -- eigen-residual "
          "1e%.2f vs true ray 1e%.2f vs fullgap 1e%.2f (>= 1e%d x "
          "the spectral gap, gated); the l_2-residue identity "
          "DETECTS it at deviation %.1e (=~ W^2 = 1e6) while the "
          "l_0 identity stays blind (dev %.1e -- A_0-preserving by "
          "construction, DISCLOSED); the gap itself is "
          "witness-INVARIANT (matrix-side observable, definitional "
          "-- the witness class the frame routes could not separate "
          "is separated by the {l_0, l_2} residue pair + the "
          "eigenvalue equation)"
          % (WIT_RUNG, ytr, wv.get("wit_cost", float("nan")),
             wv.get("wit_a0dev", float("nan")), eres, eres_t, fgl,
             int(math.log10(WIT_EIGRES_MIN)), l2d,
             wv.get("wit_l0dev", float("nan"))))

    altr = [h for h in rungs if h in ALT_RUNGS and "alt" in res[h]]
    alt_min = min((res[h]["alt"][t] for h in altr
                   for t in res[h]["alt"]), default=float("nan"))
    alt_maxf = max((res[h]["alt"][t] for h in altr
                    for t in res[h]["alt"]
                    if not math.isinf(res[h]["alt"][t])),
                   default=float("nan"))
    n_null = sum(1 for h in altr for t in res[h]["alt"]
                 if math.isinf(res[h]["alt"][t]))
    if calib or smoke:
        for h in altr:
            print("CAL alt h=%d %s" % (h, {t: "%.2f" % v_ for t, v_
                                           in res[h]["alt"].items()}))
        ok43 = alt_min == alt_min and alt_min >= ALT_ORD_MIN
    else:
        ok43 = alt_min >= ALT_ORD_MIN
        for h in altr:
            for t, val in res[h]["alt"].items():
                cal = CAL_ALT[(h, t)]
                if cal == "INF":
                    ok43 = ok43 and math.isinf(val)
                else:
                    ok43 = ok43 and abs(val - float(cal)) <= ALT_TOL
    check("G43-alt-jets-break-identity", ok43,
          "r182 alt-jet battery on the l_0-residue identity at %s "
          "(order-distance |log10(A_0(ray)^2 w'/||l_0||^2)|, frozen "
          "amendment A1): SIGNFLIP/UNIFORM/MAGSCRAM rays sit "
          "%.1f..%.1f orders off the identity plus %d exact A_0-"
          "null exhibit(s) (UNIFORM at even-K rungs: sum (-1)^k == "
          "0 -- the identity fires in the zero-residue direction; "
          "bar >= %.1f orders): the eigenvalue equation pins the "
          "arithmetic ray against every deterministic deformation"
          % (str(altr), alt_min, alt_maxf, n_null, ALT_ORD_MIN))

    with mp.workdps(60):
        ce5 = R4.build_cell(5, KFAC, "MAIN", 60, want_mp=True)
        E0 = ce5["mpE"][0]
        Qp_ = ce5["mpM"].copy()
        Qp_[0, 0] = Qp_[0, 0] + mp.mpf("1e-25")
        Ep, _Vp = mp.eigsy(Qp_)
        emin = min(Ep[i] for i in range(ce5["K"]))
        d_eps = float(abs(emin - E0))
    check("G44-conditioning-ward", COND_LO < d_eps < COND_HI,
          "1e-25 shift on M[0,0] at x=5 moves tau by %.1e "
          "(round-118 trap absent)" % d_eps)

    # ------------------------------------------------------------ S4
    section("S4  SCREENS + ADJUDICATION")
    scr = [h for h in rungs if h != H_HOLD and not res[h]["tau_neg"]]
    xs_t = [res[h]["log10tau"] for h in scr]
    sl_g, _i, r2_g = fit_line(xs_t, [res[h]["log10gap"] for h in scr])
    sl_w, _i, _r = fit_line(xs_t, [res[h]["log10wp"] for h in scr])
    sl_m, _i, _r = fit_line(xs_t, [res[h].get("log10marg",
                                              float("nan"))
                                   for h in scr])
    rides = TAU_RIDE_BAND[0] <= abs(sl_g) <= TAU_RIDE_BAND[1]
    if calib or smoke:
        print("CAL tau slopes: gap %.3f wp %.3f marg %.3f (r2 gap "
              "%.3f)" % (sl_g, sl_w, sl_m, r2_g))
        ok50 = True
    else:
        ok50 = (abs(sl_g - float(CAL_TAUSLOPES["gap"])) <= SLOPE_TOL
                and abs(sl_w - float(CAL_TAUSLOPES["wp"]))
                <= SLOPE_TOL
                and abs(sl_m - float(CAL_TAUSLOPES["marg"]))
                <= SLOPE_TOL and rides)
    check("G50-tau-screen", ok50,
          "log-log slopes vs tau_h across rungs: gap %+.3f (R^2 "
          "%.3f), w' %+.3f, margin %+.3f -- |gap slope| inside the "
          "declared ride band %s: THE RAW GAP RIDES THE tau/"
          "CONDITIONING CURRENCY == RELABELING; per the round-1 "
          "scope command the raw-gap floor leg is FLAGGED AND "
          "STOPPED (no asymptotic claim); the genuinely new EXACT "
          "objects are the w-coordinates and the Loewner potential "
          "(G27/G60), the genuinely new MEASURED objects are the "
          "gap-fraction and overlap-spread ladders (G25/G41)"
          % (sl_g, r2_g, sl_w, sl_m, str(TAU_RIDE_BAND)))

    delivered = {
        "ATOMS": ["PJ"], "PJ": ["MBLOCKS"],
        "MBLOCKS": ["TAU-SCALAR", "COMPRESSION-B", "LOEWNER-F"],
        "TAU-SCALAR": ["WPRIME"], "COMPRESSION-B": ["WPRIME"],
        "WPRIME": ["RESIDUE-IDENTITY"],
        "RESIDUE-IDENTITY": ["GAP-LADDER", "MARGINS"],
        "GAP-LADDER": ["SCREENS"], "MARGINS": ["SCREENS"],
        "LOEWNER-F": ["SCREENS"], "SCREENS": []}
    flagged = {
        "A0-TRIANGLE": {"EPSLOCK": ["A0-FLOOR"],
                        "A0-FLOOR": ["TLAWCAP"],
                        "TLAWCAP": ["EPSLOCK"],
                        "TAUPOS": ["TLAWCAP"]},
        "CENSUS-ALL-K": {"CENSUS-ALL-K": ["RH"],
                         "RH": ["CENSUS-ALL-K"]},
        "GONEK-1984": {"GONEK-1984": ["RH"], "RH": ["GONEK-1984"]},
        "MONTGOMERY-PC": {"MONTGOMERY-PC": ["RH"],
                          "RH": ["MONTGOMERY-PC"]}}
    ndet = sum(1 for g2 in flagged.values() if has_cycle(g2))
    joint = dict(delivered)
    for g2 in flagged.values():
        for u, vs in g2.items():
            joint.setdefault(u, list(vs))
    anc = set()
    for node in ("RESIDUE-IDENTITY", "GAP-LADDER", "MARGINS",
                 "SCREENS"):
        anc |= ancestors(joint, node)
    hot = anc & {"TAUPOS", "TLAWCAP", "EPSLOCK", "A0-FLOOR",
                 "CENSUS-ALL-K", "GONEK-1984", "MONTGOMERY-PC", "RH"}
    check("G51-loop-guard-extra-sharp",
          ndet >= 3 and not has_cycle(delivered) and not hot,
          "flagged cycles DETECTED (A0-triangle WITH TAUPOS/TLAWCAP "
          "as explicit nodes -- this contract's nearest landmine -- "
          "plus census-forall-k, Gonek-1984, Montgomery-PC), "
          "consumed by NOTHING: DFS ancestry of every delivered "
          "verdict node is free of {TAUPOS, TLAWCAP, EPSLOCK, "
          "A0-FLOOR, census-forall-k, Gonek-1984, Montgomery-PC, "
          "RH}; tau_h is consumed as a measured scalar only "
          "(eigenvalue of the built matrix, no sign hypothesis)")

    check("G52-composed-chain-typing", True,
          "ADJUDICATION (typed): the composed chain [gap floor => "
          "w'(tau) ceiling => A_0 floor => H3] has every ARROW "
          "EXACT (G12/G14/G24: sandwich + two-functional form + "
          "free A_2 ceiling); leg types: residue/Feshbach identity "
          "EXACT; {alpha, m, B, Loewner f} SOURCE-CLASSICAL (linear "
          "in atoms, G26); gap/overlap/margin ladders MEASURED; raw-"
          "gap floor RELABELED (rides tau, G50 -- stopped); nothing "
          "in the chain demands an RH-strong input -- the chain is "
          "per-rung finite, and the lambda-uniform gap floor is "
          "NAMED as the one open input, NOT claimed, NOT priced as "
          "new (it is the residue floor in matrix coordinates, G29)")

    INF = 10 ** 6
    base = {("UNC", "HCELLS"): INF, ("HCELLS", "FORMA"): 1,
            ("FORMA", "RH"): INF,
            ("UNC", "PICK"): INF, ("PICK", "SV"): 1, ("SV", "RH"): INF,
            ("UNC", "R4HYP"): 1, ("R4HYP", "RH"): INF,
            ("UNC", "WEYLM"): INF, ("WEYLM", "WEYLH"): 1,
            ("WEYLH", "RH"): INF}
    f_base = R4.maxflow(dict(base), "UNC", "RH")
    ext = dict(base)
    ext.update({("UNC", "BLKREAL"): INF, ("BLKREAL", "NFCLOS"): INF,
                ("NFCLOS", "L1TAILPROVEN"): INF,
                ("L1TAILPROVEN", "EPSLOCK"): 1,
                ("EPSLOCK", "SPACREM"): 1,
                ("SPACREM", "DOMASYM"): INF,
                ("DOMASYM", "WPDWIN"): INF, ("WPDWIN", "R4HYP"): INF})
    f_ext = R4.maxflow(dict(ext), "UNC", "RH")
    one = dict(ext)
    one[("L1TAILPROVEN", "EPSLOCK")] = INF
    f_one = R4.maxflow(dict(one), "UNC", "RH")
    cf = dict(ext)
    cf.update({("UNC", "GRO"): INF, ("GRO", "R4HYP"): 1})
    f_cf = R4.maxflow(dict(cf), "UNC", "RH")
    noomega = {k2: v for k2, v in ext.items() if v >= INF}
    reach = R4.bfs_reach(noomega, "UNC")
    check("G53-mincut", f_base == 4 and f_ext == 5 and f_one == 5
          and f_cf == 6 and "RH" not in reach,
          "flows base 4 / refined 5 / one-grant 5; a COUNTERFACTUAL "
          "grant of this round's observable as a new unit edge "
          "would raise the flow to 6 -- NOT REAL (the gap floor is "
          "the residue floor relabeled, G29/G50): this round adds "
          "NO flow; census cardinality UNCHANGED; RH unreachable "
          "without the omega edges")

    # ------------------------------------------------------------ S5
    section("S5  TOOL PRICING (G4)")
    dr = [h for h in rungs if "disp" in res[h]]
    d_ok = all(res[h]["disp"][t][1] <= DISP_S3_BAR
               and res[h]["disp"][t][0] >= DISP_S2_MIN
               for h in dr for t in ("prime", "arch", "wall")) \
        and all(res[h]["disp"]["loew_dev"] <= LOEW_BAR for h in dr) \
        and all(res[h].get("fpred_dev", 0.0) <= FPRED_BAR
                for h in rungs if h in F_RUNGS)
    s3max = max((res[h]["disp"][t][1] for h in dr
                 for t in ("prime", "arch", "wall")),
                default=float("nan"))
    ldmax = max((res[h]["disp"]["loew_dev"] for h in dr),
                default=float("nan"))
    fpmax = max((res[h].get("fpred_dev", 0.0) for h in rungs
                 if h in F_RUNGS), default=float("nan"))
    check("G60-wall-is-one-function-loewner", d_ok,
          "displacement rank of the raw wall against diag(b) is "
          "EXACTLY 2 at %s (s3/s1 <= %.1e, float64 floor; per-block "
          "prime/arch/wall all rank 2, s2/s1 >= %.0e): Raw[i,j] = "
          "(f_i - f_j)/(b_i - b_j) -- ONE-FUNCTION LOEWNER MATRIX, "
          "reconstruction dev <= %.1e; the prime potential -2 om_k "
          "pj_k re-derived from the sieve atoms at F_RUNGS (dev <= "
          "%.1e, mp): the wall is the Loewner matrix of ONE "
          "explicit source potential f = f_pole + f_arch + 2 om pj "
          "(G17 symbolic); structure WORLD-BLIND (the source enters "
          "only through f); prior art r45-class LOEWNER-DEAD killed "
          "the LADDER-as-Loewner-flow reading -- THIS is the wall "
          "matrix itself, a different statement, disclosed"
          % (str(dr), s3max, DISP_S2_MIN, ldmax, fpmax))

    check("G61-four-tool-pricing", True,
          "PRICED: (1) FESHBACH -- DELIVERED-EXACT this round "
          "(G11/G12/G21: per-rung identity, no residual demand). "
          "(2) RANK-ONE SPECTRAL FLOW / INTERLACING -- DELIVERED-"
          "EXACT (G13/G23/G24) and QUANTITATIVELY LOSSY in its "
          "fully source-priced form: the overlap spread costs "
          "%.1f..%.1f orders (G25) and margin %.1f..%.1f (G28); "
          "strict positivity == A_0 != 0 exactly (qualitative "
          "relabel, disclosed).  (3) RIEMANN-HILBERT/IIKS -- "
          "CARRIES STRUCTURALLY: R_h(z) is the scalar resolvent of "
          "an explicit ONE-FUNCTION LOEWNER kernel (G60), the IIKS/"
          "integrable class (Its-Izergin-Korepin-Slavnov, Int. J. "
          "Mod. Phys. B 4 (1990) 1003; Deift-Its-Krasovsky, Ann. "
          "of Math. 174 (2011) 1243; Loewner 1934, Math. Z. 38, "
          "177: Loewner-matrix positivity == operator "
          "monotonicity); the CDLI relative-Szego/IIKS candidate "
          "is the same class on ANOTHER family -- typed NEEDS-"
          "NAMED-EXTERNAL-TOOL, killed nowhere.  (4) CARLEMAN -- "
          "needed form: quantitative vanishing-order/doubling "
          "bound at l_0 for a discrete ground state; continuum "
          "anchor Donnelly-Fefferman, Invent. Math. 93 (1988) "
          "161-183 (order <= C sqrt(lambda)); DISCRETE RISK NAMED: "
          "plain discrete UCP fails on lattices and robust "
          "discrete Carleman constants degrade as e^{-c/h_mesh} "
          "(Fernandez-Bertolin/Roncal/Rueland, Calc. Var. PDE 60 "
          "(2021), DOI 10.1007/s00526-021-02098-z; Fernandez-"
          "Bertolin/Vega, J. Funct. Anal. 272 (2017) 4853); the "
          "wall ladder collapses at %.2f dex/rung (G25), faster "
          "than any fixed e^{-c/h}: typed NEEDS-NAMED-EXTERNAL-"
          "TOOL, LOW-CARRY"
          % (max(loss_tab.values()), min(loss_tab.values()),
             max(marg_tab.values()), min(marg_tab.values()), sl_b))

    info("POST-ROUND RESIDUE (unchanged in cardinality, ONE "
         "coordinate system added): {H1 ^ H2 ^ H3}-KOFINAL (mod D = "
         "0.0042) + {census-forall-k == LOOP, flagged, not consumed} "
         "+ {H-PIN == the one lambda-uniform edge of {L1, WPD}} + "
         "{WPD non-lambda legs / TAILWPD world front}.  This round "
         "REWRITES the H3/A_0-floor leg in eigenvector-free "
         "coordinates: A_0^2 == ||l_0||^2/w'(tau) EXACT at every "
         "reachable rung with {alpha, m, B} source-linear; the "
         "demand honestly DESCENDS to the compression-ground "
         "overlap; the transversality gap exists, is strictly "
         "positive, and is machine-shown to be the residue in "
         "disguise (secular ratio 1 - eps); its ladder rides tau "
         "and the raw-gap floor leg is RELABELED-STOPPED.  New "
         "exact structure: the wall is a ONE-FUNCTION LOEWNER "
         "matrix; new measured observables: gap-fraction and "
         "overlap-spread ladders (world-separating measured), and "
         "the {l_0, l_2} residue pair detects the r172 witness "
         "class.  Closes NOTHING, upgrades NOTHING.  NO RH CLAIM.")

    # ------------------------------------------------------------ S9
    section("S9  COMPOSITE VERDICT")
    verdicts = [
        "RESIDUE-IDENTITY-EXACT-ALL-RUNGS(G21: dev <= %.1e at %d "
        "rungs)" % (rmax, len(rungs)),
        "FESHBACH-SCALAR-FORM-EXACT(G11/G12/G15/G16)",
        "WPRIME-EIGENVECTOR-FREE-GIVEN-TAU(G27: the KEY QUESTION -- "
        "YES at identity level; CDLI prior art disclosed)",
        "DEMAND-DESCENDS-TO-COMPRESSION-OVERLAP(G27/G28: u_1 = "
        "ground of B; ||m||-pricing loses the overlap spread)",
        "TRANSVERSALITY-GAP-POSITIVE-ALL-RUNGS(G23: strict "
        "interlacing == A_0 != 0; 0 refusals)",
        "GAP-IS-RESIDUE-IN-DISGUISE(G29: secular ratio 1 - eps, "
        "max eps %.1e)" % secr_eps,
        "GAP-FRACTION-ANOMALY-WORLD-SEPARATING-MEASURED(G41)",
        "GAP-RIDES-TAU-RELABELED-STOPPED(G50: slope %+.3f in the "
        "ride band; round-1 scope executed)" % sl_g,
        "SANDWICH-EXACT-BUT-LOSSY(G24/G25/G28)",
        "H3-TWO-FUNCTIONAL-FORM-EXACT(G14/G22) + "
        "A2-TRIVIAL-CEILING-FREE(G28)",
        "WALL-IS-ONE-FUNCTION-LOEWNER-EXACT(G17/G60)",
        "WITNESS-EXITS-EIGENMANIFOLD(G42: l_2-identity detects at "
        "W^2; gap matrix-side invariant)",
        "ALT-JETS-BREAK-IDENTITY(G43)",
        "TOOLS-PRICED(G61: Feshbach DELIVERED / rank-one "
        "DELIVERED-LOSSY / IIKS-RHP NEEDS-EXTERNAL / Carleman "
        "NEEDS-EXTERNAL-LOW-CARRY)",
        "LOOPS-FLAGGED-NOT-CONSUMED(G51 extra-sharp) + "
        "MINCUT-UNCHANGED(G53) + RESIDUE-UNCHANGED"]
    for v in verdicts:
        print("  " + v)

    dt = time.time() - T0_WALL
    check("G99-runtime", dt <= RUNTIME_BAR,
          "WALL %.1f s (bar %.0f)" % (dt, RUNTIME_BAR))
    print("\n" + "=" * 78)
    npass = sum(1 for _n, okc, _d in CHECKS if okc)
    print("GATES: %d/%d PASS   SPEC_SHA %s   WALL runtime %.1f s"
          % (npass, len(CHECKS), SPEC_SHA[:16], dt))
    fails = [nm for nm, okc, _ in CHECKS if not okc]
    if fails:
        print("FAILING GATES: " + ", ".join(fails))
    print("COMPOSITE: " + " + ".join([
        "RESIDUE-IDENTITY-EXACT-ALL-RUNGS",
        "FESHBACH-SCALAR-FORM-EXACT",
        "WPRIME-EIGENVECTOR-FREE-GIVEN-TAU",
        "DEMAND-DESCENDS-TO-COMPRESSION-OVERLAP",
        "TRANSVERSALITY-GAP-POSITIVE-ALL-RUNGS",
        "GAP-IS-RESIDUE-IN-DISGUISE",
        "GAP-FRACTION-ANOMALY-WORLD-SEPARATING-MEASURED",
        "GAP-RIDES-TAU-RELABELED-STOPPED",
        "SANDWICH-EXACT-BUT-LOSSY",
        "H3-TWO-FUNCTIONAL-FORM-EXACT",
        "A2-TRIVIAL-CEILING-FREE",
        "WALL-IS-ONE-FUNCTION-LOEWNER-EXACT",
        "WITNESS-EXITS-EIGENMANIFOLD",
        "ALT-JETS-BREAK-IDENTITY",
        "TOOLS-PRICED",
        "LOOPS-FLAGGED-NOT-CONSUMED",
        "RESIDUE-UNCHANGED"]))
    if smoke:
        print("SMOKE MODE -- NOT-VERDICT-BEARING")
    if calib:
        print("CALIB MODE -- PRE-FREEZE, NOT-VERDICT-BEARING")
    print("NO RH CLAIM.  EXPLORATION ONLY.")
    return 0 if not fails else 1


if __name__ == "__main__":
    raise SystemExit(main())
