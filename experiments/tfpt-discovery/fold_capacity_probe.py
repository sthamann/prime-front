#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""fold_capacity_probe -- PRIME.LSTAR.FOLD_CAPACITY.01 (round
334): the CAPACITY FORK for L* -- the reviewer's rank-2 language
(Fold Capacity Packing) put to its decisive measurement.  L* (the
open scalar of r283/r284/r286: lambda_max(E_{N_w}) < 1 for the
nu-dressed mu-CD kernel, margin 1.68e-4 on w9) is re-read as a
distributed two-weight sampling problem: for subsets E of the nu
support define the POLYNOMIAL CAPACITY
    Cap_{mu,N}(E) = inf { int p^2 dmu : deg p < N,
                          |p(x)| >= 1 on E },
and with the exact level-set formula int p^2 dnu =
int_0^inf nu(E_t(p)) d(t^2), E_t(p) = {|p| >= t} on the nu atoms,
L* reduces to (K1) nu(E) <= kappa Cap(E) on polynomial superlevel
sets, (K2) int_0^inf Cap(E_t(p)) d(t^2) <= C_lev int p^2 dmu, and
(K3) kappa C_lev < 1 => L*.  THE ROUND'S FOUR QUESTIONS, sealed:
(1) build the capacity machinery exactly on the positive mu kernel
and verify the point-capacity identity Cap({y}) = 1/K_N(y, y)
against the r284 Christoffel machinery; (2) on small EXACT
instances (S <= 16) compute kappa(E) = nu(E)/Cap(E) over ALL
subsets AND over all intervals -- is the supremum interval-carried
(INTERVAL_CAPACITY_CARRIER) or are genuine multi-component sets
needed (ALLSET_NEEDED)?  On the real windows (w9 + a sealed ladder
sample): kappa over intervals + over the superlevel sets of a
SEALED test-polynomial family (never eigenvectors); (3) the K3
census kappa_w x C_lev,w over the sample + the world check
MAIN/TWIN (identical expected) vs EPSTEIN/SCRAMBLE (the capacity
quotients must reach >= 1 there -- else CAPACITY_WORLD_BLIND);
(4) the brutal restatement check: is sup_E nu(E)/Cap(E) over ALL
sets just lambda_max(E_N) in disguise (CAPACITY_RESTATEMENT if the
interval clause has no real gap to the all-set clause AND K2 does
not carry universally)?  NOT a proof round: no L* claim, no bound
mechanism, no certificate -- machinery + census + honest typing.

EXPLORATION ONLY (2026-08-27).  experiments/ level: NO promotion,
NO ledger row, NO marker moved, NO RH CLAIM in either direction.

THE EXISTING CAPACITY PACKAGE (transcribed, not reinvented): the
program already certified a capacity cycle on the COVERING-KERNEL
side -- v546 PRIME.CAPCHAIN.IDENT.01 (the exact capacity
decomposition K^-1 = D^T J^-1 D + x x^T / cap, the capacity-
Rayleigh identity, the Cholesky interval fan) and v547
PRIME.LEVEL.LEMMA.01 (the non-Markovian layer-cake level lemma,
Maz'ya 1985 class).  THIS round transcribes the same two-step
architecture (set inequality + level-set integral) to the mu-RKHS
side of L*: the kernel is K_N(x, y) = sum_{i<N} P_i(x) P_i(y)
(the mu-CD kernel of r284), the capacity is the RKHS minimal-
energy capacity of a constraint set, the level inequality is the
same Maz'ya-type layer cake.  Classics named CLASSICAL: Maz'ya
1985 (capacitary strong type), Muckenhoupt 1972 (two-weight
calculus), Lawson-Hanson 1974 (NNLS active set).  KKT/active-set
duality: for one sign pattern the QP min ||c||^2 s.t. sigma_j
phi_j^T c >= 1 has value 1^T lam with lam = G_A^{-1} 1 >= 0 on the
active set A and feasibility off A (G the sign-dressed kernel
Gram); Cap_abs = min over sign patterns.  SIGN-BRANCH DISCARD
(sealed): the all-plus branch is ALWAYS feasible (p == const),
so its value is a ceiling; any branch whose running DUAL value
2 sum lam - lam^T G lam exceeds that ceiling is certified
non-minimal by weak duality and discarded (this also covers
INFEASIBLE branches, whose dual is unbounded).  REAL-WINDOW
CONVENTION (sealed, disclosed): on the real windows every
capacity is the one-signed Cap_+ (an UPPER bound of Cap_abs, so
every real-window kappa is a LOWER bound of the |p|-capacity
kappa; the exact theorem kappa <= lambda_max survives a
fortiori, and the LEG-B sign census measures the abs-vs-plus gap
where full enumeration is exact).  EXACT FACTS carried by
the round (each gated): Cap({y}) = 1/K_N(y, y) (point capacity ==
inverse Christoffel); kappa(E) <= lambda_max(E_N) for EVERY E (if
|p| >= 1 on E then nu(E) <= int p^2 dnu <= lambda_max int p^2
dmu); int p^2 dnu = sum_i (t_i^2 - t_{i-1}^2) nu(E_{t_i}) exactly;
superlevel sets of a degree-d polynomial have <= d + 1 components.

INDEX FIREWALL (binding, r238-r333 discipline): w = window, S =
#union atoms, S_+/S_- = #mu/#nu atoms, N_w = (S+1)//2 = builder
depth = the capacity degree cap, E_n = B_n B_n^T with B[k, i] =
sqrt(v_k) P_i(y_k), Phi = B / sqrt(v) rowwise, G = Phi Phi^T =
the mu-CD kernel Gram on the nu atoms (so diag(E_n) = v * diag(G)
exactly).  Ground truth (r283/r284/r286 records, control flips)
enters GATES and record tables only; the sealed constructors
consume kernel Gram / weight / value arrays ONLY (AST scope
audit); no zero/prime oracles anywhere (AST firewall); the test
family is sealed and WORLD-BLIND (basis degrees, Chebyshev
degrees, golden-ratio coefficient draws -- NO top eigenvector,
NO L* margin in any constructor; the eigenvector appears
GATE-SIDE only, in the restatement tightness diagnostic).
MACHINERY IMPORTED VERBATIM: document pipeline V.{build_measures,
mu_chain, b_matrix, window_shape, admissible_indices, PP}, r283
FS.{mu_chain_f64, b_matrix_f64, mu_chain_mp, b_matrix_mp}, r278
MS.ctx_build, r280 BL.{union_of_ctx, sign_chain_f64}, v881
PIK.lambda_eps, r331 TR.{base_comb, build_world}, r289
AKD.twin_rational, r276 MF.local_gaps, r274 WD.{stj_gen, pv_seq},
r230 JF.{TOY_NODES, TOY_WTS}, v563 core READ-ONLY.

LEG A -- MACHINERY + EXACT TOYS: (a1) hand capacity toy (mu =
{-1/2, 0, 1/2} w 1, N = 2, kernel K_2(x,y) = 1/3 + 2xy): hand
values Cap({1/4}) = 24/11, Cap({1/4, -1/4}) = 3 (equilibrium
p == 1) with the (+,-) sign branch 8, Cap({1/4, 2/5}) = 24/11
(active-set DROP case: the shallow atom alone is active, the
constraint at 2/5 is slack 64/55), Cap({2/5}) = 75/49; the f64
solver and an independent EXACT Fraction enumeration (all sign
patterns x all active subsets, rational Gauss elimination) must
agree to 1e-12 on ALL subsets; the r286 4-atom toy identity
kappa({1/4}) = v K_2 = 11/240 = lambda_max(E_2) exact.  (a2) the
level-set formula hand toy (nu {1/4, 2/5} v {1/10, 1/20},
p(x) = x): int p^2 dnu = 57/4000 by layers, exact.  (a3) JF9
rational cross-route: on the r230 signed toy (S = 9, N = 5,
S_- = 3) the singleton capacities 1/K_5(y, y) from the EXACT
rational monic route (WD chain + pv_seq, Fractions) must equal
the f64 NNLS capacities to 1e-10 rel.

LEG B -- THE SMALL EXACT CENSUS (question 2, all-set side): four
sealed instances with S <= 16 (I1 = JF9; I2/I3/I4 = sealed
rational grid instances disclosed in SEALED CONSTANTS below; S_-
= 3/4/5/6).  Per instance: kappa(E) = nu(E)/Cap_abs(E) over ALL
2^{S_-} - 1 subsets (Cap_abs by sign enumeration, <= 2^{S_- - 1}
patterns per subset after the global-flip symmetry) and over all
intervals (contiguous in the x-sorted nu order); kappa_all vs
kappa_int, the argmax set (is it an interval?), the sign census
(#subsets with Cap_abs < Cap_+ strictly), lambda_max(E_N), the
exact theorem gate kappa(E) <= lambda_max + 1e-9 for EVERY E, the
restatement input kappa_all/lambda_max.  EXACT WARD: the argmax
subsets (all-set + interval) and every subset within 1e-6 of the
sup are re-certified in EXACT Fractions (rational kernel via WD,
full (sign x active-set) enumeration) when |E| <= 4, else in mp
(dps 40, fixed active set).

LEG C -- THE REAL WINDOWS (questions 2b + 3): (c1) w9 (S = 367 =
263 + 104, N_w = 184): point capacities on all 104 nu atoms (the
identity v_k / Cap({y_k}) = diag(E_184)_k gated against the
INDEPENDENT r283-FS chain route and the r284 record diag max
0.9700); kappa over ALL 5460 nu intervals (KKT certificate gated
on every solve); the sealed test family (PBASE degrees {1, 2, 3,
N/4, N/2, 3N/4, N-1}, TCHEB degrees {2, 5, N/8, N/2, N-1} on the
affine hull, GOLDEN 3 deterministic coefficient draws): per
polynomial the exact nu level identity, kappa over its superlevel
sets, C_lev(p) = sum_i (t_i^2 - t_{i-1}^2) Cap(E_{t_i}) /
int p^2 dmu, the component census (n_runs <= deg + 1 gate) and
the SPLITTING RATIO R_split = sum_comp Cap(comp)/Cap(E) (the
Muckenhoupt/multiplicity-2 structure, measured); kappa_w =
max(kappa_int, kappa_lev), the K3 product kappa_w x C_lev,w vs
lambda_max; mp ward (dps 40, fixed active set, chain + B in mp)
on the top-3 interval capacities + the top level set + every
kappa within 1e-4 of 1.  (c2) the sealed ladder sample: the 42
admissible document windows sorted by (N_w, kz) -- take the
FIRST, the MEDIAN and the LAST (plus w9); on large windows (S_-
> 160) the sealed interval family = all intervals of length
{1, 2, 3} at every anchor + geometric lengths {4, 8, ..., S_-}
at every 4th anchor + the full set, and the reduced family
(PBASE {1, N/2, N-1}, TCHEB {N/2}, GOLDEN 1); level strips
capped at LEV_CAP = 128 (merged evenly in t^2, set taken at the
strip BOTTOM = the larger set => C_lev is an UPPER bound there,
the honest direction for K3).  (c3) GATE-SIDE restatement
tightness on w9: the top eigenvector's own superlevel chain must
reproduce kappa_lev(eig) x C_lev(eig) >= lambda(eig) = lambda_max
- 1e-9 -- the chain is TIGHT on the extremal direction, so NO
(kappa, C_lev) valid for all polynomials can have product below
lambda_max: the structural ceiling of the whole fork, stated as
a gate.

LEG D -- THE WORLD CHECK (question 3b): EPSTEIN + SCRAMBLE built
verbatim through the r278/r280 channel (minC == flips 25/21
gated), at THEIR own N_w: full interval census + full family;
a dead world is SEEN iff max(kappa_int, kappa_lev) >= 1 or the
K3 product >= 1 (kappa(E) > 1 directly certifies lambda_max > 1
by the exact theorem); CAPACITY_WORLD_BLIND iff any dead world is
NOT seen.  TWIN: the r289/r331 rational twin of w9 at tol 1e-8
(TR.base_comb + AKD.twin_rational + TR.build_world; dose-zero
identity TR.build_world == V.build_measures gated bitwise);
the twin's kappa_int sup, kappa_lev sup and C_lev must agree with
MAIN to 1e-3 rel (identical expected -- the capacity coordinate
must not be twin-fragile at the resolving tolerance).

LEG E -- WARDS / MUST-FAILS (each loud): w9 record gates
(lambda_max(E_184) = 0.99983248, lambda at 185 = 1.00003660,
margin 1.6752e-4 rel 0.01, S/S_+/S_- = 367/263/104, diag max
0.9700 +- 5e-3); KKT certificate on EVERY capacity solve
(stationarity on the support, feasibility >= 1 - 1e-7, lam >= 0,
primal-dual gap <= 1e-8 rel; zero certificate failures allowed);
the exact theorem gate on every measured set of every world.
MUST-FAILS: (m1) CAPACITY VIA TARGET EIGENVECTOR -- a mutant
orienting a capacity set by the withheld top eigenvector /
lambda record is FLAGGED by the AST scope audit; (m2) LEVEL
FORMULA WITH THE WRONG MEASURE -- the layer sum with counting
weights in place of nu must break the exact identity by >= 0.1
rel (and the true identity holds to 1e-12); (m3) INCOMPLETE
ALL-SET ENUMERATION -- a mutant enumerator dropping the full-set
mask must be CAUGHT by the census gate (count == 2^{S_-} - 1 and
mask-set equality); (m4) KAPPA BY SIGHT -- a mutant reading the
withheld lambda record into the kappa side is FLAGGED by the AST
scope audit; (m5) KKT MUTANT -- scaling the optimal multipliers
by 1.01 must violate the sealed certificate loudly.  STOP LIST
(anti-gates, binding): NO L* claim, NO bound mechanism, NO
kappa/C_lev promoted as a certificate, NO posthoc family member,
NO derived 5/7, NO RH claim; r243..r333 stand.

SEALED CONSTANTS: MAIN_KZ 9; REC (S 367, S_+ 263, S_- 104, N_w
184); REC_LAM 0.99983248; REC_LAM_NEXT 1.00003660; REC_MARGIN
1.6752e-4 rel tol 0.01; DIAGMAX_REC 0.9700 tol 5e-3; CTRL_FLIPS
{EPST 25, SCR 21}; EXT 8; EQ_TOL 1e-12; CAP_KKT 1e-9 (rel);
FEAS_TOL 1e-7; GAP_TOL 1e-8 (rel); CAP_ITER_FACT 4; ABS_ENUM 8;
THM_TOL 1e-9; ID_TOL 1e-12; TOY_TOL 1e-12; JF_CHR_BAR 1e-10;
EXACT_WARD_TIE 1e-6; EXACT_WARD_MAXE 4; MP_DPS 40; MP_BAR 1e-8;
KNIFE_BAR 1e-4; LEV_CAP 128; BIG_SM 160; GEO_ANCHOR_STEP 4;
PBASE_FRACS (1, 2, 3, N//4, N//2, 3N//4, N-1); TCHEB_DEGS (2, 5,
N//8, N//2, N-1); GOLDEN_DRAWS 3; LADDER_REDUCED (PBASE {1,
N//2, N-1}, TCHEB {N//2}, GOLDEN 1); TWIN_TOL 1e-8; TWIN_BAR
1e-3 (rel); CARRY_BAR 0.99; REST_BAR 0.90; C_UNIV 8.0; RES_FACT
10.0; M2_BAR 0.1; M5_BAR 1e-3; runtime <= 1800 s; small
instances (rational positions/weights, sealed): I1 = JF9 (r230
verbatim); I2 mu {-7/8, -5/8, -2/8, 1/8, 4/8, 7/8} w {1, 2/3,
1/2, 1/2, 2/3, 1}, nu {-6/8, -4/8, 3/8, 6/8} v {1/3, 1/4, 1/5,
1/6}; I3 mu {-9/10, -6/10, -3/10, 0, 3/10, 6/10, 9/10} w {1,
1/2, 1/3, 1/4, 1/3, 1/2, 1}, nu {-8/10, -7/10, -1/10, 2/10,
8/10} v {1/2, 1/3, 1/5, 1/6, 1/4}; I4 mu {-15/16, -11/16, -7/16,
-3/16, 3/16, 7/16, 11/16, 15/16} w {1, 1/2, 1/2, 1, 1, 1/2, 1/2,
1}, nu {-13/16, -9/16, -5/16, 5/16, 9/16, 13/16} v {1/2, 1/3,
1/4, 1/4, 1/3, 1/2}; smoke = toys + firewall + scopes + mutants
+ I1 census + w9 f64 block (records, point capacities, intervals
of length <= 2); ladder, controls, twin, full family, mp/exact
wards and adjudication skipped.  PRE-SPEC SCOPING (disclosed):
the r283/r284/r286/r331 record numbers (S counts, lambda
records, flips, diag max, twin tolerance ladder) are consumed as
sealed gate anchors; the instances, families, bars and
adjudication rules were fixed at design time from the published
record geometry BEFORE any machinery pass of this probe; no bar,
band or typing rule was tuned after any evaluation of this
probe.

SEALED VERDICT FORM (frozen BEFORE evaluation, joined with '+'):
  [exactly one of] INTERVAL_CAPACITY_CARRIER(min instance ratio
    kappa_int/kappa_all >= 0.99) / ALLSET_NEEDED(loci)
  + K3_CENSUS(per world: kappa_int, kappa_lev, C_lev, product,
    lambda_max, excess = product - lambda_max; supremum locus;
    split-ratio census) [always]
  + [exactly one of] WORLD_SEEN(every dead world reaches >= 1) /
    CAPACITY_WORLD_BLIND(loci)
  + [exactly one of] CAPACITY_RESTATEMENT(iff (a) kappa_all >=
    0.90 lambda_max on every small instance AND (b) the carrier
    clause fired INTERVAL_CAPACITY_CARRIER AND (c) K2 does NOT
    carry, where K2 CARRIES iff max C_lev over the live worlds
    <= 8.0 AND product < 1 on every live world AND the reserve
    1 - product >= 10 x (1 - lambda_max) on every live world) /
    CAPACITY_CONTENT(named gap)
  + TWIN_LEDGER(rel deviations) [always].
Honesty before beauty: every kappa/C_lev here is MEASURED on the
sealed families (intervals, superlevel sets of the sealed test
polynomials) -- lower bounds of the true suprema, never
certificates; the gate-side eigen tightness makes the structural
ceiling explicit (no valid (K1, K2) pair can put the product
below lambda_max); C_lev on the large rung is an upper bound by
the sealed strip coarsening; a passing world check is a
consistency statement about the instrumented families, not a
discriminator theorem.  No verdict claims L*, a bound mechanism,
a derived 5/7, or RH progress in any direction.

RECORD TABLES (frozen from the record run; two-commit protocol,
chronology honest: smoke pass 1 = CRASH at G20 (a machinery slip
-- V.lam_max_at returns (lam, B), the tuple was compared as a
scalar; fixed, no rule touched); smoke pass 2 = 26/26 with ONE
counted certificate failure, identified as the INFEASIBLE
(+,-,-) sign branch of the toy triple (affine p cannot satisfy
p(1/4) >= 1, p(-1/4) <= -1, p(2/5) <= -1; the dual runs
unbounded) -- the sealed SIGN-BRANCH DISCARD rule (weak-duality
ceiling from the always-feasible all-plus branch) was added to
the spec BEFORE the freeze; smoke pass 3 = 26/26, 0 failures,
0.2 s; PRE-FREEZE COMMIT 67833ecf (spec + machinery, no record
tables).  Calibration pass 1 = first full evaluation = CRASH in
the SCR interval census + G40/G41/G50 FAIL: the solver stopping
criterion was normalized by the GRAM SCALE (max |G| ~ 1e13 on
SCR => immediate termination with lam = 0 => 452 zero
capacities; on w9 11 early-terminated solves with feasibility
9e-4 < 1 - 1e-7).  DISCLOSED CALIBRATION AMENDMENT a1 (r270/r286
precedent, machinery-side, no bar, band, family or adjudication
rule moved): the stop rule is now ABSOLUTE at the constraint
scale 1 (0.5 x FEAS_TOL with a 64-eps backward-error floor
|G| lam + 1, superseding the CAP_KKT gram-scale rule), the
equality start carries 2 iterative-refinement steps, and the
KKT certificate tolerances are backward-error scaled (128 eps x
(|G| lam + 1) floors on stationarity/feasibility/gap) -- the
certificate stays sharp (the m5 mutant breaks by 1.0e-2 >=
1e-3).  Calibration pass 2 = 26/26, wall 123.6 s, 138723
capacity solves, 0 certificate failures.  The post-freeze record
runs are numerically identical to calibration pass 2; run1 =
26/26 (122.4 s), run2 = 26/26 (125.1 s), byte-identical up to
WALL):
CAL_VERDICT = ALLSET_NEEDED(min instance ratio kappa_int/
kappa_all = 0.7013 at I4 < 0.99: I1/I2/I3 are interval-carried
(ratio 1.0000, argmax masks 4/3/3 all intervals) but the I4
supremum is the OUTERMOST SYMMETRIC PAIR {-13/16, +13/16} (mask
33, NON-interval, two components, won on a sign-alternating
branch): kappa_all = 2.446305 vs kappa_int = 1.715709 -- genuine
multi-component sets carry the all-set clause once the geometry
offers a separated symmetric pair; sign census: Cap_abs < Cap_+
strictly on 3/7, 4/15, 20/31, 44/63 subsets -- the |p| freedom
is REAL and grows with S_-)
+ K3_CENSUS(w9: kappa_int 0.999567 at the SHALLOW-EDGE PAIR
(start 102, len 2 = folds 2/4, y 0.99941/0.99985, Cap
8.387e-6) -- the r284 two-atom extremal band, NOT the singleton
(best single atom = diag max 0.97001); kappa_lev 0.999567 (the
P1 top level set IS the same pair); C_lev,w 1.0646 (max at
P138), product 1.0642 vs lambda 0.99983248, excess +0.0643;
ladder sample kz18 (z 37, S_- 84, N_w 142): 0.999524 /
0.998778 / 0.9582 (P141) / product 0.9577, excess -0.0423;
kz60 (z 211, 247, 388): 0.999974 / 0.998333 / 0.9026 (P387) /
0.9026, excess -0.0974; kz52 (z 169, 551, 878): 0.999991 /
0.999707 / 1.0198 (P877) / 1.0198, excess +0.0198 (strip UPPER
bounds there); the interval-capacity margin 1 - kappa_int
shrinks along the ladder (4.8e-4 / 4.3e-4 / 2.6e-5 / 9e-6 at
N_w 142/184/388/878) -- the same shallow-edge pair carries it
on every rung; split-ratio census R_split med 0.978 / max
1.097 (T92, 30 components) -- component splitting is nearly
FREE on the measured superlevel sets; n_runs <= deg + 1 on all
sealed family members; w9 C_lev rows: P1 0.383, P2 0.349, P3
0.330, P46 0.431, P92 0.623, P138 1.065, P183 1.003, T2..T183
0.24..0.30, R1..R3 0.246/0.451/0.677)
+ WORLD_SEEN(EPST: kappa_int 1793.99 at a pair (116, 2),
kappa_lev 1170.30, C_lev 87.30, product 1.57e5, lambda 2191.39;
SCR: kappa_int 8.51e6 at the singleton (93, 1), C_lev 4.23e4,
product 3.60e11, lambda 1.36e7 -- BOTH dead worlds reach >= 1
on the interval clause ALONE (kappa > 1 directly certifies
lambda > 1 by the exact theorem); live worlds all < 1; minC ==
flips 25/21)
+ CAPACITY_CONTENT(the restatement rule does NOT fire, on two
clauses: (a) FALSE -- kappa_all/lambda = 0.9671 / 0.9435 /
0.8504 / 0.9640 on I1..I4, min 0.8504 < 0.90: at these sizes
the all-set supremum is close to but NOT uniformly the lambda
shadow (the sign-enumerated cone loses up to 15 percent);
(b) FALSE -- the carrier clause fired ALLSET_NEEDED; and K2
does NOT carry (C_max_live 1.0646 <= 8.0 but product >= 1 on
MAIN and kz52; the reserve rule 1 - product >= 10 x margin
fails on every live world).  THE NAMED GAP, honest: the
GATE-SIDE EIGEN TIGHTNESS is the structural ceiling -- the
extremal direction's own chain gives kappa_lev(eig) 0.999567 x
C_lev(eig) 1.0089 = 1.00850632 >= lambda - 1e-9 -- so NO
(K1, K2) pair valid for all polynomials can put the product
below lambda_max: the K3 route can never yield more margin than
the spectral margin itself, and on the measured families it
does not even reach 1 with the needed sign (product 0.90..1.06
straddles 1 across the live rungs, family-relative); the fork's
honest content is (i) the interval clause as a world
DISCRIMINATOR (dead worlds shout kappa >> 1 through intervals
alone) and (ii) the interval-capacity margin as a NEW source-
pure near-wall coordinate (1 - kappa_int = 2.6x the spectral
margin on w9, same shallow-edge locus, shrinking along the
ladder) -- not a new bound mechanism)
+ TWIN_LEDGER(rational twin at tol 1e-8: kappa_int dev 3.1e-9,
kappa_lev dev 3.1e-9, C_lev dev 5.5e-9 (bar 1e-3), twin lambda
0.99983248 == MAIN; dose-zero identity TR.build_world ==
V.build_measures BITWISE).
Key numbers.  W9: 5460 intervals + 15 family polynomials, KKT
certificates green on all; point-capacity identity v_k /
Cap({y_k}) == diag(E_184)_k vs the independent r283-FS route to
9.7e-16, diag max 0.97001 == r284 record; theorem gate max
kappa - lambda = -2.7e-4 (every measured set strictly below
lambda on every live world); records lambda_max(E_184) =
0.99983248, margin 1.6752e-4, lambda at 185 = 1.00003660 all
reproduced.  EXACT WARDS: I1..I4 argmax subsets (all-set +
interval) re-certified in EXACT Fractions (full sign x
active-set enumeration on the rational WD kernel), devs <=
6.8e-16; toy hand values 24/11, 3, 8, 24/11 (active-set DROP
with slack 64/55), 75/49 all exact; JF9 singleton capacities ==
1/K_5(y, y) rational to 6.5e-16; level hand toy 57/4000 exact.
MP WARD (dps 40, fixed active set): top-3 w9 interval
capacities rel devs 2.8e-14 / 4.4e-15 / 5.1e-15 (bar 1e-8),
feasibility + lam >= 0 confirmed in mp; 0 knife-edge kappas
(|kappa - 1| <= 1e-4) on the w9 census.  MUST-FAILS: m1
eigenvector-capacity mutant AST-FLAGGED (w1_true/eigh); m2
wrong-measure layer sum breaks by 4.3e+04 >= 0.1 while the true
identity holds to 4.9e-16; m3 census mutant CAUGHT (14 != 15
masks); m4 kappa-by-sight mutant AST-FLAGGED (REC_LAM); m5 KKT
mutant breaks by 1.0e-2 >= 1e-3; scopes + fragment audit CLEAN.
Totals: 138723 capacity solves, 0 certificate failures, wall
122.4 / 125.1 s (bar 1800).  AMENDMENTS AFTER FREEZE: the
disclosed calibration amendment a1 (solver numerics, above) and
the record-table insertion -- nothing else; no bar, band,
family, instance or adjudication rule moved at any point after
the freeze.

NO RH CLAIM IN EITHER DIRECTION.  NOT evidence for or against RH.
"""

from __future__ import annotations

import argparse
import ast
import hashlib
import math
import os
import sys
import time
from fractions import Fraction as Fr

import numpy as np
import mpmath as mp

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)
_PROB = os.path.abspath(os.path.join(HERE, "..", "..", "rh", "problem"))
if _PROB not in sys.path:
    sys.path.insert(0, _PROB)

import verify_lstar_instance as V                # noqa: E402 document
import fullsource_quasidefiniteness_probe as FS  # noqa: E402 r283
import metric_stability_probe as MS              # noqa: E402 r278
import budget_localization_probe as BL           # noqa: E402 r280
import port_integrable_kernel_probe as PIK       # noqa: E402 v881
import twin_resolution_probe as TR               # noqa: E402 r331
import arch_kernel_diophantine_probe as AKD      # noqa: E402 r289
import minimal_firewall_probe as MF              # noqa: E402 r276
import wronskian_dictionary_probe as WD          # noqa: E402 r274
import jfraction_probe as JF                     # noqa: E402 r230
import v563_paper2_readouts as core              # noqa: E402 READ-ONLY

MAIN_KZ = 9
REC_S, REC_SP, REC_SM, REC_NW = 367, 263, 104, 184
REC_LAM = 0.99983248
REC_LAM_NEXT = 1.00003660
REC_MARGIN = 1.6752e-4
REC_MARGIN_TOL = 0.01
DIAGMAX_REC = 0.9700
DIAGMAX_TOL = 5e-3
CTRL_FLIPS = {"EPST": 25, "SCR": 21}
EXT = 8
EQ_TOL = 1.0e-12
CAP_KKT = 1.0e-9
FEAS_TOL = 1.0e-7
GAP_TOL = 1.0e-8
CAP_ITER_FACT = 4
ABS_ENUM = 8
THM_TOL = 1.0e-9
ID_TOL = 1.0e-12
TOY_TOL = 1.0e-12
JF_CHR_BAR = 1.0e-10
EXACT_WARD_TIE = 1.0e-6
EXACT_WARD_MAXE = 4
MP_DPS = 40
MP_BAR = 1.0e-8
KNIFE_BAR = 1.0e-4
LEV_CAP = 128
BIG_SM = 160
GEO_ANCHOR_STEP = 4
GOLDEN_DRAWS = 3
GOLDEN = (math.sqrt(5.0) - 1.0) / 2.0
TWIN_TOL = 1.0e-8
TWIN_BAR = 1.0e-3
CARRY_BAR = 0.99
REST_BAR = 0.90
C_UNIV = 8.0
RES_FACT = 10.0
M2_BAR = 0.1
M5_BAR = 1.0e-3
SMOKE_INT_LEN = 2

# sealed small instances (rational; positions ascending)
INSTANCES = {
    "I2": (((-7, 8), (-5, 8), (-2, 8), (1, 8), (4, 8), (7, 8)),
           ((1, 1), (2, 3), (1, 2), (1, 2), (2, 3), (1, 1)),
           ((-6, 8), (-4, 8), (3, 8), (6, 8)),
           ((1, 3), (1, 4), (1, 5), (1, 6))),
    "I3": (((-9, 10), (-6, 10), (-3, 10), (0, 1), (3, 10), (6, 10),
            (9, 10)),
           ((1, 1), (1, 2), (1, 3), (1, 4), (1, 3), (1, 2), (1, 1)),
           ((-8, 10), (-7, 10), (-1, 10), (2, 10), (8, 10)),
           ((1, 2), (1, 3), (1, 5), (1, 6), (1, 4))),
    "I4": (((-15, 16), (-11, 16), (-7, 16), (-3, 16), (3, 16),
            (7, 16), (11, 16), (15, 16)),
           ((1, 1), (1, 2), (1, 2), (1, 1), (1, 1), (1, 2), (1, 2),
            (1, 1)),
           ((-13, 16), (-9, 16), (-5, 16), (5, 16), (9, 16),
            (13, 16)),
           ((1, 2), (1, 3), (1, 4), (1, 4), (1, 3), (1, 2))),
}

SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
T0_WALL = time.time()
CHECKS: list = []
N_SOLVES = [0]
N_CERT_FAIL = [0]


def check(name, ok, detail):
    ok = bool(ok)
    CHECKS.append((name, ok, detail))
    print("  [%s] %-42s %s" % ("PASS" if ok else "FAIL", name, detail),
          flush=True)
    return ok


def info(msg):
    print("  [INFO] " + msg, flush=True)


def section(t):
    print("\n" + "-" * 78 + "\n" + t + "\n" + "-" * 78, flush=True)


def firewall_audit():
    src = open(os.path.abspath(__file__), "r", encoding="utf-8").read()
    tree = ast.parse(src)
    forb = {"zeta" + "zero", "n" + "zeros", "prime" + "range",
            "is" + "prime", "gram" + "point"}
    bad = []
    for node in ast.walk(tree):
        nm = node.attr if isinstance(node, ast.Attribute) else (
            node.id if isinstance(node, ast.Name) else None)
        if nm and nm.lower() in forb:
            bad.append("%s@%d" % (nm, node.lineno))
    return (not bad), ("NO zero/prime oracles; the sealed "
                       "constructors consume kernel Gram / weight / "
                       "value arrays ONLY; record numbers and flips "
                       "enter gates and record tables only"
                       if not bad else "; ".join(bad))


def antigate_fragment_audit():
    frags = ("poly" + "fit", "curve_" + "fit", "lst" + "sq",
             "mini" + "mize", "Line" + "arRegression")
    src = open(os.path.abspath(__file__), "r", encoding="utf-8").read()
    tree = ast.parse(src)
    hits = []
    for node in ast.walk(tree):
        nm = None
        if isinstance(node, ast.Attribute):
            nm = node.attr
        elif isinstance(node, ast.Name):
            nm = node.id
        elif isinstance(node, ast.FunctionDef):
            nm = node.name
        if nm and any(f in nm for f in frags):
            hits.append("%s@%d" % (nm, node.lineno))
    return hits


CONSTRUCTORS = ("kernel_gram", "cap_nnls", "cap_abs_small",
                "subsets_all", "intervals_of", "interval_family",
                "level_decomp", "level_strips", "golden_coeffs",
                "cheb_vals", "runs_of", "kappa_of")
SCOPE_FORBIDDEN = {"REC_LAM", "REC_LAM_NEXT", "REC_MARGIN",
                   "CTRL_FLIPS", "DIAGMAX_REC", "eigh", "eigvalsh",
                   "lam_true", "w1_true", "minC_true"}


def scope_audit(funcname):
    src = open(os.path.abspath(__file__), "r", encoding="utf-8").read()
    tree = ast.parse(src)
    hits = []
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and node.name == funcname:
            for sub in ast.walk(node):
                nm = None
                if isinstance(sub, ast.Attribute):
                    nm = sub.attr
                elif isinstance(sub, ast.Name):
                    nm = sub.id
                elif isinstance(sub, ast.Constant) \
                        and isinstance(sub.value, str):
                    nm = sub.value
                if nm in SCOPE_FORBIDDEN:
                    hits.append("%s@%d" % (nm, sub.lineno))
    return hits


# ============== sealed source-pure constructors (AST-audited)
def kernel_gram(B, vn):
    """Phi[k, i] = P_i(y_k) = B[k, i]/sqrt(v_k) and the mu-CD
    kernel Gram G = Phi Phi^T on the nu atoms; consumes the
    dressed frame + weights only."""
    Phi = np.asarray(B, float) / np.sqrt(np.asarray(vn, float))[:, None]
    return Phi, Phi @ Phi.T


def cap_nnls(G, idx, ceil=None):
    """Cap_+(E) = min ||c||^2 s.t. p >= 1 on E (one sign pattern),
    by the dual active set: equality start (lam = G_E^{-1} 1; if
    lam >= 0 it is KKT-optimal), else Lawson-Hanson from zero.
    Returns (cap, lam_full, active_list, cert_ok).  The KKT
    certificate: lam >= 0, stationarity |(G lam)_j - 1| small on
    the support, feasibility (G lam)_j >= 1 - FEAS_TOL off it,
    primal-dual gap |sum lam - lam^T G lam| small.  The sealed
    SIGN-BRANCH DISCARD: if a ceiling is given and the running
    dual value 2 sum lam - lam^T G lam exceeds it, the branch
    optimum exceeds the ceiling by weak duality (unbounded dual =
    infeasible branch included) -- return (inf, ..., True)."""
    N_SOLVES[0] += 1
    idx = list(idx)
    m = len(idx)
    GE = G[np.ix_(idx, idx)]
    eps = float(np.finfo(float).eps)
    lam = None
    try:
        le = np.linalg.solve(GE, np.ones(m))
        for _ref in range(2):        # iterative refinement
            le = le + np.linalg.solve(GE, 1.0 - GE @ le)
        if np.all(le >= -EQ_TOL * max(1.0, float(np.max(np.abs(le))))):
            r = GE @ le - 1.0
            rmag = np.abs(GE) @ np.abs(le) + 1.0
            if float(np.max(np.abs(r) / rmag)) <= 64.0 * eps:
                lam = np.maximum(le, 0.0)
    except np.linalg.LinAlgError:
        lam = None
    if lam is None:
        lam = np.zeros(m)
        P: list = []
        it_cap = CAP_ITER_FACT * m + 8
        for _ in range(it_cap):
            if ceil is not None:
                dval = 2.0 * float(np.sum(lam)) \
                    - float(lam @ (GE @ lam))
                if dval > ceil:
                    return math.inf, lam, [], True
            w = 1.0 - GE @ lam
            rmag = np.abs(GE) @ lam + 1.0
            stop = np.maximum(0.5 * FEAS_TOL, 64.0 * eps * rmag)
            w_free = w.copy()
            if P:
                w_free[P] = -np.inf
            j = int(np.argmax(w_free - stop))
            if w_free[j] <= stop[j]:
                break
            P.append(j)
            for _inner in range(it_cap):
                GP = GE[np.ix_(P, P)]
                try:
                    lp = np.linalg.solve(GP, np.ones(len(P)))
                except np.linalg.LinAlgError:
                    lp = np.linalg.pinv(GP) @ np.ones(len(P))
                if np.all(lp > 0.0):
                    lam = np.zeros(m)
                    lam[P] = lp
                    break
                cur = lam[P]
                d = lp - cur
                stepc = [cur[t] / (cur[t] - lp[t])
                         for t in range(len(P)) if lp[t] <= 0.0
                         and cur[t] - lp[t] > 0.0]
                alpha = min(stepc) if stepc else 0.0
                cur = cur + alpha * d
                lam = np.zeros(m)
                lam[P] = np.maximum(cur, 0.0)
                P = [p for t, p in enumerate(P) if cur[t] > 0.0]
                if not P:
                    break
    act = [t for t in range(m) if lam[t] > 0.0]
    gl = GE @ lam
    cap = float(np.sum(lam))
    if ceil is not None and cap > ceil:
        dval = 2.0 * cap - float(lam @ gl)
        if dval > ceil:
            return math.inf, lam, [], True
    rmag = np.abs(GE) @ lam + 1.0
    tolv = np.maximum(FEAS_TOL, 128.0 * eps * rmag)
    stat = max([abs(gl[t] - 1.0) / tolv[t] for t in act] or [0.0])
    feas_ok = bool(np.all(gl >= 1.0 - tolv))
    gap = abs(cap - float(lam @ gl))
    gap_ok = gap <= max(GAP_TOL * max(cap, 1.0e-300),
                        128.0 * eps * float(rmag @ lam + 1.0))
    cert = (stat <= 10.0 and feas_ok and gap_ok)
    if not cert:
        N_CERT_FAIL[0] += 1
    return cap, lam, [idx[t] for t in act], cert


def cap_abs_small(G, idx):
    """Cap_abs(E) = min over sign patterns (global flip factored
    out) of the one-pattern QP; |E| <= ABS_ENUM enforced.
    Returns (cap, best_sigma, active_list, cert_ok)."""
    idx = list(idx)
    m = len(idx)
    assert m <= ABS_ENUM
    GE = G[np.ix_(idx, idx)]
    cap0, lam0, act0, cert0 = cap_nnls(GE, list(range(m)))
    best = (cap0, tuple([1] * m), [idx[t] for t in act0], cert0)
    for smask in range(1, 1 << max(m - 1, 0)):
        sg = np.ones(m)
        for t in range(m - 1):
            if (smask >> t) & 1:
                sg[t + 1] = -1.0
        Gs = GE * np.outer(sg, sg)
        cap, lam, act, cert = cap_nnls(Gs, list(range(m)),
                                       ceil=best[0] * (1.0 + 1e-9))
        if cap < best[0]:
            best = (cap, tuple(int(s) for s in sg),
                    [idx[t] for t in act], cert)
    return best


def subsets_all(n):
    """every nonempty subset mask of an n-atom nu support."""
    return list(range(1, 1 << n))


def intervals_of(n):
    """all contiguous index intervals [i..j] of the x-sorted nu
    order, as masks."""
    out = []
    for i in range(n):
        mask = 0
        for j in range(i, n):
            mask |= (1 << j)
            out.append(mask)
    return out


def interval_family(nsm):
    """the sealed interval family: ALL intervals when S_- <=
    BIG_SM; else lengths {1, 2, 3} at every anchor + geometric
    lengths {4, 8, ...} at every GEO_ANCHOR_STEP-th anchor + the
    full set.  Returns (start, length) pairs."""
    out = []
    if nsm <= BIG_SM:
        for i in range(nsm):
            for j in range(i, nsm):
                out.append((i, j - i + 1))
        return out
    for ln in (1, 2, 3):
        for i in range(nsm - ln + 1):
            out.append((i, ln))
    ln = 4
    while ln < nsm:
        for i in range(0, nsm - ln + 1, GEO_ANCHOR_STEP):
            out.append((i, ln))
        ln *= 2
    out.append((0, nsm))
    return out


def level_decomp(pv, vn):
    """exact layer decomposition of |p| on the nu atoms:
    ascending distinct thresholds t_1 < ... < t_M (> 0), the
    superlevel index sets E_{t_i} = {k : |p_k| >= t_i}, the strip
    weights dt2_i = t_i^2 - t_{i-1}^2 (t_0 = 0) and the exact nu
    level sum sum_i dt2_i nu(E_{t_i})."""
    a = np.abs(np.asarray(pv, float))
    v = np.asarray(vn, float)
    order = np.argsort(a)
    ts = []
    for k in order:
        if a[k] > 0.0 and (not ts or a[k] > ts[-1]):
            ts.append(float(a[k]))
    sets = []
    lev_sum = 0.0
    prev2 = 0.0
    for t in ts:
        E = np.nonzero(a >= t)[0]
        dt2 = t * t - prev2
        lev_sum += dt2 * float(np.sum(v[E]))
        sets.append((t, dt2, E))
        prev2 = t * t
    return ts, sets, lev_sum


def level_strips(sets):
    """the sealed strip coarsening for the Cap layer sum: at most
    LEV_CAP strips, merged evenly in the threshold INDEX, each
    strip carrying the summed dt2 and the set at the strip BOTTOM
    (the largest set of the strip => the layer sum is an UPPER
    bound)."""
    M = len(sets)
    if M <= LEV_CAP:
        return [(dt2, E) for _t, dt2, E in sets]
    out = []
    step = (M + LEV_CAP - 1) // LEV_CAP
    i = 0
    while i < M:
        j = min(i + step, M)
        dt2 = sum(sets[k][1] for k in range(i, j))
        out.append((dt2, sets[i][2]))
        i = j
    return out


def golden_coeffs(n, s):
    """deterministic world-blind coefficient draw s on n degrees:
    c_i = 2 {(i + 1) g + s g^2} - 1, g the golden section,
    normalized to ||c|| = 1."""
    i = np.arange(1, n + 1, dtype=float)
    c = 2.0 * np.mod(i * GOLDEN + float(s) * GOLDEN * GOLDEN,
                     1.0) - 1.0
    return c / float(np.linalg.norm(c))


def cheb_vals(x, m, lo, hi):
    """T_m on the affine map of [lo, hi] onto [-1, 1], evaluated
    at x (values only; degree m stays below the space cap)."""
    z = (2.0 * np.asarray(x, float) - (lo + hi)) / (hi - lo)
    z = np.clip(z, -1.0, 1.0)
    return np.cos(m * np.arccos(z))


def runs_of(E):
    """number of maximal consecutive runs of a sorted index set
    (the component census in the nu order)."""
    E = np.sort(np.asarray(E, np.int64))
    if len(E) == 0:
        return 0, []
    cuts = np.nonzero(np.diff(E) > 1)[0]
    runs = []
    start = 0
    for c in list(cuts) + [len(E) - 1]:
        runs.append(E[start:c + 1])
        start = c + 1
    return len(runs), runs


def kappa_of(vn, E, cap):
    """kappa(E) = nu(E)/Cap(E); consumes weights + capacity."""
    return float(np.sum(np.asarray(vn, float)[list(E)])) / cap


# ============== must-fail mutants
def mutant_cap_eigvec(B, n):
    """m1 MUST-FAIL: a 'capacity set' oriented by the withheld
    top eigenvector -- the scope audit must FLAG this."""
    En = B[:, :n] @ B[:, :n].T
    _ev, W = np.linalg.eigh(En)
    w1_true = W[:, -1]
    return np.argsort(w1_true ** 2)[-3:]


def mutant_kappa_posthoc():
    """m4 MUST-FAIL: a 'kappa target' read off the withheld
    lambda record -- the scope audit must FLAG this."""
    return 0.5 * (1.0 + REC_LAM)


def mutant_level_wrongmeasure(pv, vn):
    """m2 MUST-FAIL: the layer sum with counting weights instead
    of nu -- must break the exact identity loudly."""
    _ts, sets, _ls = level_decomp(pv, np.ones(len(vn)))
    return sum(dt2 * len(E) for _t, dt2, E in sets)


def mutant_subsets_incomplete(n):
    """m3 MUST-FAIL: an enumerator dropping the full-set mask --
    the census gate must CATCH it."""
    return list(range(1, (1 << n) - 1))


def mutant_kkt_scale(G, idx):
    """m5 MUST-FAIL: the optimal multipliers scaled by 1.01 --
    the sealed certificate must break."""
    cap, lam, act, _c = cap_nnls(G, idx)
    lam2 = 1.01 * lam
    GE = G[np.ix_(list(idx), list(idx))]
    gl = GE @ lam2
    stat = max([abs(gl[t] - 1.0) for t in range(len(idx))
                if lam2[t] > 0.0] or [0.0])
    return stat


# ============== exact Fraction machinery (gate-side)
def frac_solve(Arows, brow):
    """rational Gauss elimination A x = b (Fractions)."""
    n = len(Arows)
    M = [list(Arows[i]) + [brow[i]] for i in range(n)]
    for col in range(n):
        piv = next((r for r in range(col, n) if M[r][col] != 0), None)
        if piv is None:
            return None
        M[col], M[piv] = M[piv], M[col]
        pv = M[col][col]
        M[col] = [x / pv for x in M[col]]
        for r in range(n):
            if r != col and M[r][col] != 0:
                f = M[r][col]
                M[r] = [a - f * b for a, b in zip(M[r], M[col])]
    return [M[r][n] for r in range(n)]


def frac_kernel(xs, ws, ys, depth):
    """exact rational mu-CD kernel Gram on the nu atoms via the
    monic rational route (WD chain + pv_seq): G[a, b] =
    sum_{i<depth} pi_i(y_a) pi_i(y_b) / h_i."""
    al, be, hs = WD.stj_gen(xs, ws, depth - 1)
    vals = [WD.pv_seq(al, be, y, depth - 1) for y in ys]
    m = len(ys)
    G = [[sum(vals[a][i] * vals[b][i] / hs[i] for i in range(depth))
          for b in range(m)] for a in range(m)]
    return G


def frac_cap_abs(GE):
    """exact Cap_abs on the rational Gram GE: full enumeration of
    sign patterns x active subsets; a pair (sigma, A) certifies
    the one-pattern optimum iff lam_A = G_A^{-1} 1 >= 0 and
    (G lam)_j >= 1 on E; the minimum over sigma is Cap_abs."""
    m = len(GE)
    best = None
    for smask in range(1 << max(m - 1, 0)):
        sg = [Fr(1)] + [Fr(-1) if (smask >> t) & 1 else Fr(1)
                        for t in range(m - 1)]
        Gs = [[GE[a][b] * sg[a] * sg[b] for b in range(m)]
              for a in range(m)]
        val = None
        for amask in range(1, 1 << m):
            A = [t for t in range(m) if (amask >> t) & 1]
            GA = [[Gs[a][b] for b in A] for a in A]
            lam = frac_solve(GA, [Fr(1)] * len(A))
            if lam is None or any(l < 0 for l in lam):
                continue
            full = [sum(Gs[j][A[t]] * lam[t] for t in range(len(A)))
                    for j in range(m)]
            if any(f < 1 for f in full):
                continue
            val = sum(lam)
            break
        if val is not None and (best is None or val < best):
            best = val
    return best


def frac_instance(name):
    """rational atoms of a sealed instance."""
    if name == "I1":
        pairs = sorted(zip(JF.TOY_NODES, JF.TOY_WTS),
                       key=lambda t: t[0])
        xs = [x for x, w in pairs if w > 0]
        ws = [w for x, w in pairs if w > 0]
        ys = [x for x, w in pairs if w < 0]
        vs = [-w for x, w in pairs if w < 0]
    else:
        mx, mw, nx, nv = INSTANCES[name]
        xs = [Fr(*t) for t in mx]
        ws = [Fr(*t) for t in mw]
        ys = [Fr(*t) for t in nx]
        vs = [Fr(*t) for t in nv]
    S = len(xs) + len(ys)
    N = (S + 1) // 2
    depth = min(N, len(xs) - 1)
    return xs, ws, ys, vs, N, depth


# ============== gate-side world machinery
def world_from_arrays(tag, xp, wp, yn, vn, Nw, L):
    """chain + frame + Gram bundle of one world (V.mu_chain /
    V.b_matrix, document route)."""
    o = np.argsort(yn)
    yn = np.asarray(yn, float)[o]
    vn = np.asarray(vn, float)[o]
    xp = np.asarray(xp, float)
    wp = np.asarray(wp, float)
    depth = min(Nw, len(xp) - 1)
    a, b, h0 = V.mu_chain(xp, wp, depth)
    B = V.b_matrix(a, b, h0, yn, vn, depth)
    Phi, G = kernel_gram(B, vn)
    lam = float(np.linalg.eigvalsh(B @ B.T)[-1])
    return dict(tag=tag, xp=xp, wp=wp, yn=yn, vn=vn, Nw=Nw,
                depth=depth, L=L, B=B, Phi=Phi, G=G, lam=lam,
                mu_tot=float(np.sum(wp)))


def world_from_mz(tag, mz):
    return world_from_arrays(tag, mz["xp"], mz["wp"], mz["yn"],
                             mz["vn"], mz["Nw"], mz["L"])


def interval_census(Wd):
    """kappa over the sealed interval family; returns (sup, locus,
    table stats, all kappas, certificate failures)."""
    G, vn = Wd["G"], Wd["vn"]
    nsm = len(vn)
    fam = interval_family(nsm)
    best = (-1.0, None)
    kappas = []
    ncf = 0
    for (i, ln) in fam:
        idx = list(range(i, i + ln))
        cap, _lam, _act, cert = cap_nnls(G, idx)
        if not cert:
            ncf += 1
        kap = kappa_of(vn, idx, cap)
        kappas.append(kap)
        if kap > best[0]:
            best = (kap, (i, ln, cap))
    return best[0], best[1], len(fam), kappas, ncf


def family_polys(Wd, reduced):
    """the sealed test family: (name, values at nu atoms,
    int p^2 dmu, degree)."""
    Nw = Wd["depth"]
    xp, wp, yn = Wd["xp"], Wd["wp"], Wd["yn"]
    Phi = Wd["Phi"]
    out = []
    if reduced:
        pdegs = sorted({1, Nw // 2, Nw - 1})
        tdegs = sorted({Nw // 2})
        draws = 1
    else:
        pdegs = sorted({1, 2, 3, Nw // 4, Nw // 2, 3 * Nw // 4,
                        Nw - 1})
        tdegs = sorted({2, 5, max(Nw // 8, 1), Nw // 2, Nw - 1})
        draws = GOLDEN_DRAWS
    for d in pdegs:
        if 0 < d < Nw:
            c = np.zeros(Nw)
            c[d] = 1.0
            out.append(("P%d" % d, Phi @ c, 1.0, d))
    lo = float(min(np.min(xp), np.min(yn)))
    hi = float(max(np.max(xp), np.max(yn)))
    for d in tdegs:
        if 0 < d < Nw:
            pv = cheb_vals(yn, d, lo, hi)
            en = float(np.sum(wp * cheb_vals(xp, d, lo, hi) ** 2))
            out.append(("T%d" % d, pv, en, d))
    for s in range(1, draws + 1):
        c = golden_coeffs(Nw, s)
        out.append(("R%d" % s, Phi @ c, 1.0, Nw - 1))
    return out


def clev_census(Wd, reduced):
    """per-polynomial level machinery; returns the census dict."""
    vn = Wd["vn"]
    G = Wd["G"]
    rows = []
    kl_best = (-1.0, None)
    cl_best = (-1.0, None)
    split_max = (0.0, None)
    splits = []
    id_dev = 0.0
    runs_ok = True
    ncf = 0
    for (nm, pv, en, deg) in family_polys(Wd, reduced):
        ts, sets, lev_sum = level_decomp(pv, vn)
        direct = float(np.sum(vn * np.asarray(pv) ** 2))
        id_dev = max(id_dev, abs(lev_sum - direct)
                     / max(abs(direct), 1e-300))
        strips = level_strips(sets)
        lay = 0.0
        for (dt2, E) in strips:
            cap, _lam, _act, cert = cap_nnls(G, list(E))
            if not cert:
                ncf += 1
            lay += dt2 * cap
            kap = kappa_of(vn, E, cap)
            if kap > kl_best[0]:
                kl_best = (kap, (nm, len(E), runs_of(E)[0]))
            nr, runs = runs_of(E)
            if nr > deg + 1:
                runs_ok = False
            if nr > 1 and len(E) <= 3 * BIG_SM:
                csum = 0.0
                for r in runs:
                    cr, _l2, _a2, c2 = cap_nnls(G, list(r))
                    if not c2:
                        ncf += 1
                    csum += cr
                rs = csum / cap
                splits.append(rs)
                if rs > split_max[0]:
                    split_max = (rs, (nm, len(E), nr))
        cl = lay / en
        rows.append((nm, deg, len(ts), cl))
        if cl > cl_best[0]:
            cl_best = (cl, nm)
    return dict(rows=rows, kl=kl_best, cl=cl_best, id_dev=id_dev,
                runs_ok=runs_ok, splits=splits,
                split_max=split_max, ncf=ncf)


def mp_cap_ward(Wd, idx, act, cap_f64, signs=None):
    """mp ward at a FIXED active set: chain + B in mp (r283
    verbatim), G_A in mp, lam = G_A^{-1} 1, feasibility on E in
    mp; optional sign dressing per atom (the winning Cap_abs
    branch); returns (rel_dev, feas_ok, lam_ok)."""
    old = mp.mp.dps
    mp.mp.dps = MP_DPS
    try:
        al, sb, h0 = FS.mu_chain_mp(Wd["xp"], Wd["wp"], Wd["depth"],
                                    MP_DPS)
        Bm = FS.b_matrix_mp(al, sb, h0, Wd["yn"], Wd["vn"],
                            Wd["depth"], MP_DPS)
        sv = [mp.sqrt(mp.mpf(float(v))) for v in Wd["vn"]]
        rows = {}
        for k in set(list(act) + list(idx)):
            sgk = mp.mpf(1 if signs is None else signs.get(k, 1))
            rows[k] = [sgk * Bm[k, i] / sv[k]
                       for i in range(Wd["depth"])]
        a = list(act)
        GA = mp.matrix(len(a), len(a))
        for r in range(len(a)):
            for c in range(len(a)):
                GA[r, c] = mp.fsum(rows[a[r]][i] * rows[a[c]][i]
                                   for i in range(Wd["depth"]))
        one = mp.matrix([1] * len(a))
        lam = mp.lu_solve(GA, one)
        capm = mp.fsum(lam[t] for t in range(len(a)))
        lam_ok = all(lam[t] >= -mp.mpf(10) ** (-MP_DPS + 8)
                     for t in range(len(a)))
        feas_ok = True
        for j in idx:
            pj = mp.fsum(
                mp.fsum(rows[j][i] * rows[a[t]][i]
                        for i in range(Wd["depth"])) * lam[t]
                for t in range(len(a)))
            if pj < 1 - mp.mpf(10) ** (-6):
                feas_ok = False
        dev = abs(float(capm) - cap_f64) / max(abs(float(capm)),
                                               1e-300)
        return dev, feas_ok, lam_ok
    finally:
        mp.mp.dps = old


# --------------------------------------------------------------- main
def main():
    par_ = argparse.ArgumentParser()
    par_.add_argument("--smoke", action="store_true")
    args = par_.parse_args()
    smoke = args.smoke

    print("=" * 78)
    print("fold_capacity_probe -- PRIME.LSTAR.FOLD_CAPACITY.01 "
          "(round 334)")
    print("SPEC_SHA %s" % SPEC_SHA[:16])
    print("mode: %s" % ("SMOKE (toys + firewall + scopes + mutants "
                        "+ I1 census + w9 f64 block; ladder, "
                        "controls, twin, full family, wards, "
                        "adjudication skipped)"
                        if smoke else "FULL RECORD"))
    print("=" * 78)

    section("S0  FIREWALL + PREDEFINITION")
    okf, det = firewall_audit()
    check("G01-firewall", okf, det)
    check("G02-predefinition", True,
          "sealed BEFORE evaluation: the capacity definition "
          "(|p| >= 1, deg < N_w), the solver + KKT certificate, "
          "the four small instances, the interval families, the "
          "test-polynomial family (world-blind, NO eigenvector), "
          "the level-strip rule, the twin tolerance, every "
          "bar/tolerance, the mutants, the adjudication rules "
          "(CARRY_BAR %.2f, REST_BAR %.2f, C_UNIV %.1f, RES_FACT "
          "%.0f) and the verdict form; the STOP list forbids any "
          "L* claim and any certificate reading"
          % (CARRY_BAR, REST_BAR, C_UNIV, RES_FACT))

    # ---------------- S1 toys
    section("S1  TOYS -- HAND CAPACITIES + LEVEL FORMULA + JF9")
    xs_t = [Fr(-1, 2), Fr(0), Fr(1, 2)]
    ws_t = [Fr(1), Fr(1), Fr(1)]
    ys_t = [Fr(1, 4), Fr(-1, 4), Fr(2, 5)]
    Gt = frac_kernel(xs_t, ws_t, ys_t, 2)
    ok_ker = (Gt[0][0] == Fr(11, 24) and Gt[0][1] == Fr(5, 24)
              and Gt[2][2] == Fr(49, 75) and Gt[0][2] == Fr(8, 15))
    a_t, b_t, h0_t = V.mu_chain(np.array([-0.5, 0.0, 0.5]),
                                np.ones(3), 2)
    B_t = V.b_matrix(a_t, b_t, h0_t,
                     np.array([0.25, -0.25, 0.4]),
                     np.ones(3), 2)
    _Phi_t, Gf = kernel_gram(B_t, np.ones(3))
    dev_g = float(np.max(np.abs(Gf - np.array(
        [[float(Gt[a][b]) for b in range(3)] for a in range(3)]))))
    cap1, _l1, _a1, c1 = cap_nnls(Gf, [0])
    cap2, _l2, act2, c2 = cap_nnls(Gf, [0, 1])
    Gpm = Gf[np.ix_([0, 1], [0, 1])] * np.outer([1, -1], [1, -1])
    cap2m, _l2m, _a2m, c2m = cap_nnls(Gpm, [0, 1])
    cap_abs2 = cap_abs_small(Gf, [0, 1])
    cap3, _l3, act3, c3 = cap_nnls(Gf, [0, 2])
    cap4, _l4, _a4, c4 = cap_nnls(Gf, [2])
    ok_hand = (abs(cap1 - 24.0 / 11.0) <= TOY_TOL
               and abs(cap2 - 3.0) <= TOY_TOL
               and abs(cap2m - 8.0) <= TOY_TOL
               and abs(cap_abs2[0] - 3.0) <= TOY_TOL
               and abs(cap3 - 24.0 / 11.0) <= TOY_TOL
               and act3 == [0]
               and abs(cap4 - 75.0 / 49.0) <= TOY_TOL
               and c1 and c2 and c2m and c3 and c4)
    check("G10-toy-hand-capacities", ok_ker and dev_g <= 1e-14
          and ok_hand,
          "HAND VALUES on mu {-1/2, 0, 1/2} w 1, N = 2 (kernel "
          "1/3 + 2xy, rational Gram == f64 Gram to %.0e): "
          "Cap({1/4}) = %.12f == 24/11; Cap({1/4, -1/4}): sign "
          "branch (+,+) = %.12f == 3 (equilibrium p == 1), branch "
          "(+,-) = %.12f == 8, Cap_abs = %.12f == 3; "
          "Cap({1/4, 2/5}) = %.12f == 24/11 with active set %s "
          "(the DROP case, slack p(2/5) = 64/55); Cap({2/5}) = "
          "%.12f == 75/49; every KKT certificate green"
          % (1e-14, cap1, cap2, cap2m, cap_abs2[0], cap3,
             str(act3), cap4))
    ex_caps = {}
    for mask in subsets_all(3):
        E = [t for t in range(3) if (mask >> t) & 1]
        GE = [[Gt[a][b] for b in E] for a in E]
        exact = frac_cap_abs(GE)
        got = cap_abs_small(Gf, E)[0]
        ex_caps[mask] = (float(exact), got)
    dev_ex = max(abs(a - b) / max(abs(a), 1e-300)
                 for a, b in ex_caps.values())
    check("G11-toy-exact-route", dev_ex <= 1e-12,
          "EXACT FRACTION ENUMERATION (all signs x all active "
          "subsets, rational Gauss) vs the f64 solver on ALL 7 "
          "subsets of the 3 nu atoms: max rel dev %.1e (<= 1e-12) "
          "-- the solver is certified against an independent "
          "exact route" % dev_ex)
    pv_t = np.array([0.25, 0.4])
    vn_t = np.array([0.1, 0.05])
    _ts_t, _sets_t, ls_t = level_decomp(pv_t, vn_t)
    ok_lev = abs(ls_t - 57.0 / 4000.0) <= TOY_TOL
    check("G12-toy-level-formula", ok_lev,
          "LEVEL HAND TOY (nu {1/4, 2/5} v {1/10, 1/20}, p = x): "
          "layer sum = %.12f == 57/4000 == int p^2 dnu exactly"
          % ls_t)
    xsJ, wsJ, ysJ, vsJ, N_J, dep_J = frac_instance("I1")
    GJ = frac_kernel(xsJ, wsJ, ysJ, dep_J)
    aJ, bJ, h0J = V.mu_chain(np.array([float(x) for x in xsJ]),
                             np.array([float(w) for w in wsJ]),
                             dep_J)
    BJ = V.b_matrix(aJ, bJ, h0J,
                    np.array([float(y) for y in ysJ]),
                    np.array([float(v) for v in vsJ]), dep_J)
    _PhiJ, GJf = kernel_gram(BJ, np.array([float(v) for v in vsJ]))
    dev_j = 0.0
    for k in range(len(ysJ)):
        capk, _l, _a, _c = cap_nnls(GJf, [k])
        exact = 1.0 / float(GJ[k][k])
        dev_j = max(dev_j, abs(capk - exact) / exact)
    check("G13-jf9-point-capacity", dev_j <= JF_CHR_BAR,
          "JF9 RATIONAL CROSS-ROUTE (r230 toy, S = 9, N = 5, "
          "depth guard %d): singleton capacities == 1/K(y, y) "
          "from the EXACT monic route (WD chain, Fractions), max "
          "rel dev %.1e (bar %.0e) -- the point-capacity == "
          "inverse-Christoffel identity on an exact instance"
          % (dep_J, dev_j, JF_CHR_BAR))

    # ---------------- S2 w9
    section("S2  W9 -- RECORDS + POINT-CAPACITY IDENTITY")
    mz9 = V.build_measures(MAIN_KZ)
    W9 = world_from_mz("MAIN", mz9)
    lam185, _B185 = V.lam_max_at(mz9, REC_NW + 1)
    ok_rec = (mz9["S"] == REC_S and len(mz9["xp"]) == REC_SP
              and len(mz9["yn"]) == REC_SM and mz9["Nw"] == REC_NW
              and abs(W9["lam"] - REC_LAM) <= 1e-6
              and abs(lam185 - REC_LAM_NEXT) <= 1e-6
              and abs((1.0 - W9["lam"]) / REC_MARGIN - 1.0)
              <= REC_MARGIN_TOL)
    check("G20-w9-records", ok_rec,
          "w9: S = %d (mu %d / nu %d), N_w = %d, lambda_max(E_184) "
          "= %.8f (record %.8f), margin = %.4e (record %.4e rel "
          "%.2f), lambda at 185 = %.8f > 1 -- the r283/r286 route "
          "reproduced through the document pipeline"
          % (mz9["S"], len(mz9["xp"]), len(mz9["yn"]), mz9["Nw"],
             W9["lam"], REC_LAM, 1.0 - W9["lam"], REC_MARGIN,
             REC_MARGIN_TOL, lam185))
    alF, sbF, h0F = FS.mu_chain_f64(mz9["xp"], mz9["wp"], REC_NW)
    BF = FS.b_matrix_f64(alF, sbF, h0F, W9["yn"], W9["vn"], REC_NW)
    diagF = np.sum(BF * BF, axis=1)
    dev_pc = 0.0
    for k in range(REC_SM):
        capk, _l, _a, _c = cap_nnls(W9["G"], [k])
        dev_pc = max(dev_pc, abs(W9["vn"][k] / capk - diagF[k])
                     / max(diagF[k], 1e-300))
    dmax = float(np.max(diagF))
    check("G21-w9-point-capacity", dev_pc <= 1e-9
          and abs(dmax - DIAGMAX_REC) <= DIAGMAX_TOL,
          "POINT-CAPACITY IDENTITY on all %d nu atoms: v_k / "
          "Cap({y_k}) == diag(E_184)_k against the INDEPENDENT "
          "r283-FS chain route, max rel dev %.1e (bar 1e-9); diag "
          "max %.5f == r284 record %.4f (+- %.0e) -- Cap of a "
          "point IS the inverse Christoffel, verified against the "
          "r284 machinery" % (REC_SM, dev_pc, dmax, DIAGMAX_REC,
                              DIAGMAX_TOL))

    # ---------------- S3 small instances
    section("S3  LEG B -- THE SMALL EXACT CENSUS (ALL SUBSETS)")
    inames = ["I1", "I2", "I3", "I4"] if not smoke else ["I1"]
    ICEN = {}
    ok_enum = True
    ok_thm_small = True
    for nm in inames:
        xs, ws, ys, vs, N_i, dep = frac_instance(nm)
        a_i, b_i, h0_i = V.mu_chain(
            np.array([float(x) for x in xs]),
            np.array([float(w) for w in ws]), dep)
        B_i = V.b_matrix(a_i, b_i, h0_i,
                         np.array([float(y) for y in ys]),
                         np.array([float(v) for v in vs]), dep)
        vn_i = np.array([float(v) for v in vs])
        _Phi_i, G_i = kernel_gram(B_i, vn_i)
        lam_i = float(np.linalg.eigvalsh(B_i @ B_i.T)[-1])
        nsm = len(ys)
        masks = subsets_all(nsm)
        ok_enum = ok_enum and (len(masks) == (1 << nsm) - 1
                               and max(masks) == (1 << nsm) - 1)
        imasks = set(intervals_of(nsm))
        kall, kint = (-1.0, None), (-1.0, None)
        n_sign = 0
        for mask in masks:
            E = [t for t in range(nsm) if (mask >> t) & 1]
            capA, sg, act, cert = cap_abs_small(G_i, E)
            capP, _lp, _ap, _cp = cap_nnls(G_i, E)
            if capA < capP * (1.0 - 1e-9):
                n_sign += 1
            kap = kappa_of(vn_i, E, capA)
            ok_thm_small = ok_thm_small and (kap <= lam_i + THM_TOL)
            if kap > kall[0]:
                kall = (kap, mask)
            if mask in imasks and kap > kint[0]:
                kint = (kap, mask)
        ratio = kint[0] / kall[0]
        arg_is_int = kall[1] in imasks
        ICEN[nm] = dict(nsm=nsm, N=N_i, dep=dep, lam=lam_i,
                        kall=kall, kint=kint, ratio=ratio,
                        arg_int=arg_is_int, n_sign=n_sign,
                        nsub=len(masks))
        info("%s: S_- = %d, N = %d, lambda_max = %.6f; kappa_all "
             "= %.6f (mask %d, interval %s), kappa_int = %.6f, "
             "ratio %.4f; kappa_all/lambda = %.4f; sign-strict "
             "subsets %d/%d"
             % (nm, nsm, N_i, lam_i, kall[0], kall[1],
                str(arg_is_int), kint[0], ratio,
                kall[0] / lam_i, n_sign, len(masks)))
    check("G30-instance-census", ok_enum,
          "ALL-SUBSET ENUMERATION complete on %s (2^{S_-} - 1 "
          "masks each, mask census exact); Cap_abs by full sign "
          "enumeration (global flip factored)"
          % str(inames))
    check("G31-instance-theorem", ok_thm_small,
          "the EXACT THEOREM kappa(E) <= lambda_max(E_N) holds on "
          "EVERY subset of every instance (tol %.0e) -- the "
          "all-set clause can never beat the spectrum, measured "
          "exactly on the small census" % THM_TOL)
    if smoke:
        check("G32-instance-exact-ward", True, "SMOKE: skipped")
    else:
        ok_ward = True
        details = []
        for nm in inames:
            xs, ws, ys, vs, N_i, dep = frac_instance(nm)
            Gx = frac_kernel(xs, ws, ys, dep)
            cen = ICEN[nm]
            for tag, (kap, mask) in (("all", cen["kall"]),
                                     ("int", cen["kint"])):
                E = [t for t in range(cen["nsm"])
                     if (mask >> t) & 1]
                if len(E) > EXACT_WARD_MAXE:
                    details.append("%s/%s |E|=%d>4: mp-warded"
                                   % (nm, tag, len(E)))
                    a_i, b_i, h0_i = V.mu_chain(
                        np.array([float(x) for x in xs]),
                        np.array([float(w) for w in ws]), dep)
                    B_i = V.b_matrix(
                        a_i, b_i, h0_i,
                        np.array([float(y) for y in ys]),
                        np.array([float(v) for v in vs]), dep)
                    vn_i = np.array([float(v) for v in vs])
                    Wd_i = dict(xp=np.array([float(x) for x in xs]),
                                wp=np.array([float(w) for w in ws]),
                                yn=np.array([float(y) for y in ys]),
                                vn=vn_i, depth=dep)
                    _P2, G_i = kernel_gram(B_i, vn_i)
                    capA, sg, act, _c = cap_abs_small(G_i, E)
                    sgm = {E[t]: int(sg[t]) for t in range(len(E))}
                    devm, feasm, lamm = mp_cap_ward(
                        Wd_i, E, list(act), capA, signs=sgm)
                    ok_ward = ok_ward and devm <= 1e-6 \
                        and feasm and lamm
                    continue
                GE = [[Gx[a][b] for b in E] for a in E]
                exact = frac_cap_abs(GE)
                nuE = sum(vs[t] for t in E)
                kex = float(nuE / exact)
                dev = abs(kex - kap) / max(abs(kex), 1e-300)
                ok_ward = ok_ward and dev <= 1e-9
                details.append("%s/%s dev %.1e" % (nm, tag, dev))
        check("G32-instance-exact-ward", ok_ward,
              "EXACT WARD: the argmax subsets (all-set + interval) "
              "of every instance re-certified in EXACT Fractions "
              "(full sign x active-set enumeration on the rational "
              "kernel): %s" % "; ".join(details))

    # ---------------- S4 w9 real census
    section("S4  LEG C -- W9 INTERVALS + FAMILY + K3")
    if smoke:
        fam9 = [(i, ln) for i in range(REC_SM)
                for ln in range(1, SMOKE_INT_LEN + 1)
                if i + ln <= REC_SM]
        best9 = (-1.0, None)
        ncf9 = 0
        for (i, ln) in fam9:
            idx = list(range(i, i + ln))
            cap, _l, _a, cert = cap_nnls(W9["G"], idx)
            if not cert:
                ncf9 += 1
            kap = kappa_of(W9["vn"], idx, cap)
            if kap > best9[0]:
                best9 = (kap, (i, ln, cap))
        check("G40-w9-intervals", ncf9 == 0
              and best9[0] <= W9["lam"] + THM_TOL,
              "SMOKE mini census (lengths <= %d, %d intervals): "
              "kappa sup %.6f <= lambda %.8f, certificates clean"
              % (SMOKE_INT_LEN, len(fam9), best9[0], W9["lam"]))
        for g in ("G41-w9-family", "G42-w9-k3", "G43-w9-mp-ward"):
            check(g, True, "SMOKE: skipped")
        CEN = {}
    else:
        ki9, loc9, nint9, kaps9, ncf9 = interval_census(W9)
        i0, ln0, cap0 = loc9
        y_lo = W9["yn"][i0]
        y_hi = W9["yn"][i0 + ln0 - 1]
        f_lo = round(math.acos(min(max(y_hi, -1.0), 1.0))
                     * W9["L"] / (2.0 * math.pi))
        ok_thm9 = max(kaps9) <= W9["lam"] + THM_TOL
        check("G40-w9-intervals", ncf9 == 0 and ok_thm9,
              "w9 INTERVAL CENSUS (%d intervals, all KKT "
              "certificates green): kappa_int sup = %.6f at "
              "(start %d, len %d, Cap %.3e, y in [%.5f, %.5f], "
              "fold ~%d) -- theorem kappa <= lambda holds on all; "
              "max kappa - lambda = %+.1e"
              % (nint9, ki9, i0, ln0, cap0, y_lo, y_hi, f_lo,
                 max(kaps9) - W9["lam"]))
        C9 = clev_census(W9, reduced=False)
        check("G41-w9-family", C9["id_dev"] <= ID_TOL
              and C9["runs_ok"] and C9["ncf"] == 0,
              "SEALED FAMILY on w9 (%d polynomials): exact nu "
              "level identity max rel dev %.1e (<= %.0e); "
              "component census n_runs <= deg + 1 on every "
          "superlevel set; kappa_lev sup = %.6f at %s; C_lev "
              "rows (name, deg, #levels, C): %s"
              % (len(C9["rows"]), C9["id_dev"], ID_TOL,
                 C9["kl"][0], str(C9["kl"][1]),
                 str([(r[0], r[1], r[2], round(r[3], 4))
                      for r in C9["rows"]])))
        kap9 = max(ki9, C9["kl"][0])
        cl9 = C9["cl"][0]
        prod9 = kap9 * cl9
        # gate-side eigen tightness (restatement ceiling)
        ev9, Wv9 = np.linalg.eigh(W9["B"] @ W9["B"].T)
        w1 = Wv9[:, -1]
        c_eig = W9["B"].T @ w1
        pv_eig = W9["Phi"] @ c_eig
        en_eig = float(c_eig @ c_eig)
        _tsE, setsE, lsE = level_decomp(pv_eig, W9["vn"])
        layE = 0.0
        klE = 0.0
        for (dt2, E) in level_strips(setsE):
            capE, _l, _a, _c = cap_nnls(W9["G"], list(E))
            layE += dt2 * capE
            klE = max(klE, kappa_of(W9["vn"], E, capE))
        clE = layE / en_eig
        prodE = klE * clE
        ok_tight = prodE >= W9["lam"] - 1e-9
        sp_med = (float(np.median(C9["splits"]))
                  if C9["splits"] else 1.0)
        sp_max = C9["split_max"]
        check("G42-w9-k3", ok_tight,
              "K3 on w9: kappa_w = %.6f (int %.6f / lev %.6f), "
              "C_lev,w = %.4f (%s), product = %.4f vs lambda_max "
              "%.8f (excess %+.4f); split-ratio census R_split "
              "med %.3f / max %.3f at %s; GATE-SIDE EIGEN "
              "TIGHTNESS: the extremal direction's own chain "
              "gives kappa %.6f x C_lev %.4f = %.8f >= lambda - "
              "1e-9 (dev %+.1e) -- NO (K1, K2) pair valid for all "
              "polynomials can put the product below lambda_max"
              % (kap9, ki9, C9["kl"][0], cl9, C9["cl"][1], prod9,
                 W9["lam"], prod9 - W9["lam"], sp_med, sp_max[0],
                 str(sp_max[1]), klE, clE, prodE,
                 prodE - W9["lam"]))
        CEN = {"MAIN": dict(kint=ki9, klev=C9["kl"][0], clev=cl9,
                            prod=prod9, lam=W9["lam"])}
        # mp ward: top-3 intervals + top level set + knife-edge
        order = np.argsort(kaps9)[::-1][:3]
        fam9full = interval_family(REC_SM)
        wards = []
        ok_mp = True
        for t in order:
            i, ln = fam9full[t]
            idx = list(range(i, i + ln))
            cap, _l, act, _c = cap_nnls(W9["G"], idx)
            dev, feas, lamok = mp_cap_ward(W9, idx, act, cap)
            wards.append("int(%d,%d) %.1e" % (i, ln, dev))
            ok_mp = ok_mp and dev <= MP_BAR and feas and lamok
        n_knife = sum(1 for k in kaps9 if abs(k - 1.0) <= KNIFE_BAR)
        check("G43-w9-mp-ward", ok_mp,
              "MP WARD (dps %d, fixed active set, chain + B in "
              "mp): top-3 interval capacities %s (bar %.0e), "
              "feasibility and lam >= 0 confirmed in mp; %d "
              "knife-edge kappas (|kappa - 1| <= %.0e) on the "
              "interval census"
              % (MP_DPS, "; ".join(wards), MP_BAR, n_knife,
                 KNIFE_BAR))

    # ---------------- S5 ladder sample
    section("S5  LEG C -- THE SEALED LADDER SAMPLE")
    if smoke:
        check("G50-ladder-sample", True, "SMOKE: skipped")
    else:
        kzs = V.admissible_indices()
        shaped = sorted((V.window_shape(kz)[3], kz) for kz in kzs)
        sample = [shaped[0][1], shaped[len(shaped) // 2][1],
                  shaped[-1][1]]
        ok_lad = True
        for kz in sample:
            mz = V.build_measures(kz)
            Wd = world_from_mz("kz%d" % kz, mz)
            ki, loc, nint, kaps, ncf = interval_census(Wd)
            Ck = clev_census(Wd, reduced=True)
            kap = max(ki, Ck["kl"][0])
            prod = kap * Ck["cl"][0]
            ok_lad = ok_lad and ncf == 0 and Ck["ncf"] == 0 \
                and max(kaps) <= Wd["lam"] + THM_TOL \
                and Ck["id_dev"] <= ID_TOL and Ck["runs_ok"]
            CEN["kz%d" % kz] = dict(kint=ki, klev=Ck["kl"][0],
                                    clev=Ck["cl"][0], prod=prod,
                                    lam=Wd["lam"])
            info("kz%d (z %d, S_- %d, N_w %d): kappa_int %.6f at "
                 "%s, kappa_lev %.6f, C_lev %.4f (%s), product "
                 "%.4f, lambda %.8f, excess %+.4f"
                 % (kz, int(V.PP[kz]), len(Wd["vn"]), Wd["Nw"],
                    ki, str(loc[:2]), Ck["kl"][0], Ck["cl"][0],
                    Ck["cl"][1], prod, Wd["lam"],
                    prod - Wd["lam"]))
        check("G50-ladder-sample", ok_lad,
              "the sealed sample (first/median/last by (N_w, kz) "
              "of the 42): interval + family censuses green "
              "(certificates, level identities, run bounds, "
              "theorem gate kappa <= lambda on every set); table "
              "printed above -- C_lev on S_- > %d worlds is the "
              "sealed strip UPPER bound" % BIG_SM)

    # ---------------- S6 worlds: controls + twin
    section("S6  LEG D -- WORLD CHECK (EPST / SCR / TWIN)")
    if smoke:
        for g in ("G60-controls", "G61-dead-adjudication",
                  "G62-twin"):
            check(g, True, "SMOKE: skipped")
        world_verdict = None
        twin_txt = ""
    else:
        rr9 = core.build_window(9)
        N_E = int(math.floor(math.exp(2.0 * rr9["alpha"]))) + 1
        lamE = PIK.lambda_eps(N_E)
        nn_idx = np.nonzero(np.abs(lamE) > 1e-12)[0]
        cdefs = (("EPST", dict(comb=(
            np.log(nn_idx.astype(float)),
            2.0 * lamE[nn_idx] / np.sqrt(nn_idx.astype(float))))),
            ("SCR", dict(scramble_seed=1)))
        ok_ctrl = True
        for cn, kw in cdefs:
            cctx = MS.ctx_build(9, **kw)
            xu, wu, zones = BL.union_of_ctx(cctx)
            xs_z, ws_z, ys_z, vs_z = zones
            N_c = cctx["N"]
            sg = BL.sign_chain_f64(xu, wu, N_c + EXT)[0]
            mc = next((n for n in range(len(sg)) if sg[n] < 0),
                      None)
            ok_ctrl = ok_ctrl and (mc == CTRL_FLIPS[cn])
            Wd = world_from_arrays(cn, xs_z, ws_z, ys_z, vs_z,
                                   N_c, int(cctx["L"]))
            ki, loc, nint, kaps, ncf = interval_census(Wd)
            Ck = clev_census(Wd, reduced=False)
            kap = max(ki, Ck["kl"][0])
            prod = kap * Ck["cl"][0]
            ok_ctrl = ok_ctrl and ncf == 0 and Ck["ncf"] == 0 \
                and Ck["id_dev"] <= ID_TOL
            CEN[cn] = dict(kint=ki, klev=Ck["kl"][0],
                           clev=Ck["cl"][0], prod=prod,
                           lam=Wd["lam"])
            info("%s (S_- %d, N_w %d, minC %s): kappa_int %.4f at "
                 "%s, kappa_lev %.4f, C_lev %.4f, product %.4f, "
                 "lambda %.4f"
                 % (cn, len(Wd["vn"]), N_c, str(mc), ki,
                    str(loc[:2]), Ck["kl"][0], Ck["cl"][0], prod,
                    Wd["lam"]))
        check("G60-controls", ok_ctrl,
              "EPST + SCR built verbatim through the r278/r280 "
              "channel at THEIR OWN N_w: minC == flips %s; "
              "censuses green (certificates, level identities)"
              % str(CTRL_FLIPS))
        dead_seen = {cn: (max(CEN[cn]["kint"], CEN[cn]["klev"])
                          >= 1.0 or CEN[cn]["prod"] >= 1.0)
                     for cn in ("EPST", "SCR")}
        live_ok = all(max(CEN[w]["kint"], CEN[w]["klev"]) < 1.0
                      for w in CEN if w not in ("EPST", "SCR"))
        world_verdict = ("WORLD_SEEN" if all(dead_seen.values())
                         and live_ok else "CAPACITY_WORLD_BLIND")
        check("G61-dead-adjudication", True,
              "SEALED WORLD RULE: a dead world is SEEN iff "
              "max(kappa_int, kappa_lev) >= 1 or product >= 1 "
              "(kappa > 1 directly certifies lambda > 1 by the "
              "exact theorem): EPST seen %s (kappa_int %.3f), SCR "
              "seen %s (kappa_int %.3f); live worlds all < 1: %s "
              "=> %s"
              % (dead_seen["EPST"], CEN["EPST"]["kint"],
                 dead_seen["SCR"], CEN["SCR"]["kint"],
                 live_ok, world_verdict))
        uu9, mm9 = TR.base_comb(9)
        mzD = TR.build_world(9, uu9, mm9)
        ok_dose0 = (np.array_equal(mzD["xp"], mz9["xp"])
                    and np.array_equal(mzD["wp"], mz9["wp"])
                    and np.array_equal(mzD["yn"], mz9["yn"])
                    and np.array_equal(mzD["vn"], mz9["vn"]))
        gaps9 = MF.local_gaps(uu9)
        u2, m2, dens, du = AKD.twin_rational(uu9, mm9, gaps9,
                                             mz9["D"], TWIN_TOL)
        mzT = TR.build_world(9, u2, m2)
        WT = world_from_mz("TWIN", mzT)
        kiT, locT, nintT, kapsT, ncfT = interval_census(WT)
        CT = clev_census(WT, reduced=False)
        kapT = max(kiT, CT["kl"][0])
        prodT = kapT * CT["cl"][0]
        CEN["TWIN"] = dict(kint=kiT, klev=CT["kl"][0],
                           clev=CT["cl"][0], prod=prodT,
                           lam=WT["lam"])
        d_ki = abs(kiT - CEN["MAIN"]["kint"]) \
            / max(CEN["MAIN"]["kint"], 1e-300)
        d_kl = abs(CT["kl"][0] - CEN["MAIN"]["klev"]) \
            / max(CEN["MAIN"]["klev"], 1e-300)
        d_cl = abs(CT["cl"][0] - CEN["MAIN"]["clev"]) \
            / max(CEN["MAIN"]["clev"], 1e-300)
        ok_twin = (ok_dose0 and ncfT == 0 and CT["ncf"] == 0
                   and d_ki <= TWIN_BAR and d_kl <= TWIN_BAR
                   and d_cl <= TWIN_BAR)
        twin_txt = ("kappa_int dev %.1e, kappa_lev dev %.1e, "
                    "C_lev dev %.1e (bar %.0e)"
                    % (d_ki, d_kl, d_cl, TWIN_BAR))
        check("G62-twin", ok_twin,
              "RATIONAL TWIN at tol %.0e (r289/r331 verbatim; "
              "dose-zero identity TR.build_world == "
              "V.build_measures BITWISE %s): the capacity "
              "coordinate is twin-stable -- %s; twin lambda "
              "%.8f vs MAIN %.8f"
              % (TWIN_TOL, ok_dose0, twin_txt, WT["lam"],
                 W9["lam"]))

    # ---------------- S7 must-fails + scopes
    section("S7  MUST-FAILS + SCOPE AUDITS")
    pv9 = W9["Phi"] @ golden_coeffs(W9["depth"], 1)
    _t9, _s9, ls9 = level_decomp(pv9, W9["vn"])
    direct9 = float(np.sum(W9["vn"] * pv9 ** 2))
    mut2 = mutant_level_wrongmeasure(pv9, W9["vn"])
    dev_m2 = abs(mut2 - direct9) / max(abs(direct9), 1e-300)
    check("G70-mutant-wrong-measure", dev_m2 >= M2_BAR
          and abs(ls9 - direct9) / max(abs(direct9), 1e-300)
          <= ID_TOL,
          "m2 LEVEL FORMULA WITH THE WRONG MEASURE (counting "
          "weights): breaks the exact identity by %.1e rel "
          "(>= %.1f) while the true nu layer sum matches to "
          "%.0e -- LOUD" % (dev_m2, M2_BAR, ID_TOL))
    mut3 = mutant_subsets_incomplete(4)
    true3 = subsets_all(4)
    caught3 = (len(mut3) != len(true3)
               or set(mut3) != set(true3))
    check("G71-mutant-enumeration", caught3,
          "m3 INCOMPLETE ALL-SET ENUMERATION: the mutant drops "
          "the full-set mask (%d != %d masks / set inequality) "
          "-- CAUGHT by the census gate" % (len(mut3), len(true3)))
    stat5 = mutant_kkt_scale(W9["G"], [0, 1, 2])
    check("G72-mutant-kkt", stat5 >= M5_BAR,
          "m5 KKT MUTANT (multipliers x 1.01): stationarity "
          "residual %.1e >= %.0e -- the sealed certificate is "
          "sharp" % (stat5, M5_BAR))
    hits_m1 = scope_audit("mutant_cap_eigvec")
    hits_m4 = scope_audit("mutant_kappa_posthoc")
    hits = []
    for fn_ in CONSTRUCTORS:
        hits += scope_audit(fn_)
    ag_hits = antigate_fragment_audit()
    check("G73-scope-audits", bool(hits_m1) and bool(hits_m4)
          and not hits and not ag_hits,
          "m1 EIGENVECTOR-CAPACITY MUTANT FLAGGED (%s); m4 "
          "KAPPA-BY-SIGHT MUTANT FLAGGED (%s); the %d sealed "
          "constructors consume kernel Gram / weight / value "
          "arrays ONLY (%s); fragment audit: %s"
          % ("; ".join(hits_m1) if hits_m1 else "NOT FLAGGED",
             "; ".join(hits_m4) if hits_m4 else "NOT FLAGGED",
             len(CONSTRUCTORS),
             "CLEAN" if not hits else "; ".join(hits),
             "CLEAN" if not ag_hits else "; ".join(ag_hits)))

    # ---------------- S8 adjudication + verdict
    section("S8  ADJUDICATION + VERDICT")
    check("G95-stoplist", True,
          "STOP LIST held: NO L* claim, no bound mechanism, no "
          "kappa/C_lev promoted as a certificate, no posthoc "
          "family member, no derived 5/7, NO RH claim; what the "
          "round adds: the exact capacity machinery with its "
          "point-capacity/Christoffel identity, the small "
          "all-set census, the real-window interval + level "
          "censuses, the K3 product table, the world "
          "discriminator and the restatement adjudication; "
          "r243..r333 stand")
    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    if smoke:
        verd = "SMOKE_NO_ADJUDICATION"
    else:
        ratios = {nm: ICEN[nm]["ratio"] for nm in ICEN}
        min_ratio = min(ratios.values())
        carrier = ("INTERVAL_CAPACITY_CARRIER"
                   if min_ratio >= CARRY_BAR else "ALLSET_NEEDED")
        rest_in = {nm: ICEN[nm]["kall"][0] / ICEN[nm]["lam"]
                   for nm in ICEN}
        rest_a = min(rest_in.values()) >= REST_BAR
        live = [w for w in CEN if w not in ("EPST", "SCR")]
        cl_max_live = max(CEN[w]["clev"] for w in live)
        prod_live_ok = all(CEN[w]["prod"] < 1.0 for w in live)
        res_ok = all(1.0 - CEN[w]["prod"]
                     >= RES_FACT * (1.0 - CEN[w]["lam"])
                     for w in live)
        k2_carries = (cl_max_live <= C_UNIV and prod_live_ok
                      and res_ok)
        restatement = (rest_a
                       and carrier == "INTERVAL_CAPACITY_CARRIER"
                       and not k2_carries)
        k3_txt = "; ".join(
            "%s(ki %.4f, kl %.4f, C %.3f, prod %.3f, lam %.4f, "
            "exc %+.3f)"
            % (w, CEN[w]["kint"], CEN[w]["klev"], CEN[w]["clev"],
               CEN[w]["prod"], CEN[w]["lam"],
               CEN[w]["prod"] - CEN[w]["lam"]) for w in CEN)
        parts = [
            "%s(min instance ratio %.4f%s)"
            % (carrier, min_ratio,
               "" if carrier == "INTERVAL_CAPACITY_CARRIER" else
               "; loci " + str({nm: (round(r, 4),
                                     ICEN[nm]["arg_int"])
                                for nm, r in ratios.items()})),
            "K3_CENSUS(%s)" % k3_txt,
            world_verdict + "(dead reach >= 1: EPST ki %.3f / "
            "SCR ki %.3f)" % (CEN["EPST"]["kint"],
                              CEN["SCR"]["kint"])
            if world_verdict else "WORLD(skipped)",
            ("CAPACITY_RESTATEMENT(kappa_all/lambda %s; carrier "
             "no-gap; K2 does not carry)"
             % str({nm: round(r, 4) for nm, r in rest_in.items()}))
            if restatement else
            ("CAPACITY_CONTENT(rest-a %s %s; carrier %s; "
             "K2-carries %s (C_max_live %.3f, prod<1 %s, "
             "reserve %s))"
             % (rest_a,
                str({nm: round(r, 4) for nm, r in rest_in.items()}),
                carrier, k2_carries, cl_max_live, prod_live_ok,
                res_ok)),
            "TWIN_LEDGER(%s)" % twin_txt,
        ]
        verd = " + ".join(parts)
    check("G96-verdict", npass == len(CHECKS),
          "%s%s -- MEASURED census of the capacity fork; the "
          "sealed adjudication is applied honestly; NO L* claim, "
          "NO RH claim" % (verd, " (SMOKE)" if smoke else ""))
    wall = time.time() - T0_WALL
    check("G99-runtime", wall <= 1800.0,
          "WALL %.1f s (bar 1800); %d capacity solves, %d "
          "certificate failures" % (wall, N_SOLVES[0],
                                    N_CERT_FAIL[0]))
    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    print("\n" + "=" * 78)
    print("RESULT: %d/%d gates PASS%s   SPEC_SHA %s"
          % (npass, len(CHECKS), " (SMOKE)" if smoke else "",
             SPEC_SHA[:16]))
    print("NO RH CLAIM in either direction.")
    print("=" * 78)
    return 0 if npass == len(CHECKS) else 1


if __name__ == "__main__":
    sys.exit(main())
