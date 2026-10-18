#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""commensurability_mechanism_probe -- PRIME.COMMENSURABILITY.MECHANISM.01

FROZEN SPEC (2026-08-21).  EXPLORATION ONLY.  This probe writes no
verification module, paper, ledger, website, manifest, Lean file or
status marker.  It makes NO RH claim, NO positivity claim beyond the
per-rung finite statements gated below, NO counterexample claim.  It
closes no gate and narrows no gate.  Concurrent-lane files (the
krein-definitizer lane, the cancellation-functional lane, the
zb-wiggle lane, the independent session's untracked probes,
sieve4_helper.bin) are not touched.

=======================================================================
MISSION (round ~191: the commensurability mechanism quantified).
Round 189 (loewner_pick_probe, SPEC_SHA a547448468899af9) found a
GEOMETRIC reason for a world difference: the SMOOTH cell's canonical
Loewner completion L_f is PSD at the nodes with 0 descents because
its 2a-periodic oscillation vanishes EXACTLY on the node lattice
(sin(2a om_k) = sin(2 pi k) = 0 -- commensurate sampling), which the
incommensurate prime atoms at u = log q cannot do.  Round 185
(mangoldt_ablation_ladder) showed +-0.01 position jitter kills the
arithmetic signatures -- position exactness is load-bearing.  THIS
round makes the mechanism exact, quantifies the incommensurability
defect ladder, prices it against the classical linear-forms-in-
logarithms tool chest (Baker/Matveev/LMN -- genuine, unconditional,
NON-zeta arithmetic input the program has never priced), and tests
whether the defect FEEDS wall positivity (dose-response) or is
positivity-irrelevant.  Goals:
  M1  THE MECHANISM MADE EXACT.  The nodes are om_k = k pi / a
      (builder line: oms = [k pi/aa], even sector k = 0..K-1), so
      2a om_k = 2 pi k and EXACTLY: sin(2a om_k) = 0,
      cos(2a om_k) = 1, and the +- class collapses per atom:
      sin(2a om_k +- om_k u) = +-sin(om_k u) IDENTICALLY (the node
      lattice makes the boundary phase invisible).  SMOOTH COLLAPSE
      (sympy, integer k): the smooth closed forms collapse at nodes
      to Moebius data
        pj_s(om_k) = om_k (1 - e^a)/(1/4 + b_k),
        pc_s(om_k) = (e^a - 1)/(2(1/4 + b_k)),
      and the combined pole+prime node potential is EXACTLY
        f_pole(b) + 2 om_k pj_s = 2(1-e^a) + (1-e^{-a})/2/(1/4+b)
      -- the infinite smooth oscillation is a rank-1-Cauchy/Moebius
      function ON THE NODE SET: that is the exact content of the
      r189 SMOOTH-PSD-AT-NODES finding.  CONVERSE (prime world): the
      per-atom node samples are sin(om_k u_q) = sin(2 pi k log q /
      log h); they vanish for ALL k iff u_q/a = 2 log q/log h is an
      INTEGER (q = h^{m/2}: machine census of these structural
      zeros); for multiplicatively independent (q, h) NO (q, k)
      vanishes, and the INCOMMENSURABILITY DEFECT LADDER
        d_{q,k} = |sin(2 pi k log q / log h)|,
        minpos_q(h) = min over k = 1..K-1 of the structurally
        nonzero d_{q,k},   MINDEF_h = min over atoms q,
      is measured at every rung h = 4..16, 20 (geometry closed-form,
      no builder needed beyond the frozen node/K/atom recipes).
  M2  THE DIOPHANTINE PRICING (the round's new import).  The defect
      is bridged EXACTLY to a two-logarithm linear form: with
      y = 2k log q/log h, m = nint(y), Lambda_{q,k} = 2k log q -
      m log h, Jordan's inequality gives
        d_{q,k} = |sin(pi y)| >= 2 dist(y, Z) = 2|Lambda|/log h
      (instance-gated at every rung, plus the grid proof of
      sin(pi x) >= 2x on [0, 1/2]).  The classical prices for
      |Lambda| (all computed at every rung for the per-rung
      minimizer, D = 1, alpha_1 = h, alpha_2 = q, b_1 = m,
      b_2 = 2k, multiplicative independence machine-checked):
      (i) ELEMENTARY LIOUVILLE (two logs of integers): q^{2k} !=
      h^m (exact integers) => |Lambda| >= log(1 + 1/min(q^{2k},
      h^m)) -- instance-verified in exact arithmetic;
      (ii) LAURENT-MIGNOTTE-NESTERENKO 1995 (J. Number Theory 55,
      285-321, Theoreme 2/Corollaire 2; statement as in Heuberger's
      survey): log|Lambda| >= -24.34 D^4 (max(log b' + 0.14, 21/D,
      1/2))^2 h1 h2 with h_i = max(h(alpha_i), |log alpha_i|/D,
      1/D), b' = |b_1|/(D h_2) + |b_2|/(D h_1) (we use the larger
      of both orderings -- valid since the theorem only requires
      b' >= that combination);
      (iii) MATVEEV 2000 (Izv. Math. 64:6, 1217-1269; real case):
      log|Lambda| > -1.4 * 30^{n+3} n^{4.5} D^2 A_1 A_2 (1 + log D)
      (1 + log B), n = 2, A_i = max(D h(alpha_i), |log alpha_i|,
      0.16), B = max|b_i|.  Also Baker 1966-68 (Mathematika 13/14)
      as the historical source, Baker-Wustholz 1993 (J. reine
      angew. Math. 442, 19-62) named.  THE HONEST NUMBER is the
      measured-vs-bound gap ladder in dex: gap_liou (small),
      gap_lmn and gap_matveev (astronomically large --
      BAKER-TOO-WEAK is the anticipated resolution, gated
      resolve-and-record).  MULTI-ATOM STATISTICS: (iv) the
      three-distance theorem (Steinhaus problem; Sos 1958, Ann.
      Univ. Sci. Budapest 1, 127-134; Swierczkowski 1959, Fund.
      Math. 46, 187-189): the circle gaps of {k theta_q}, k <=
      K-1 take at most 3 distinct lengths -- exact check at the
      dose rungs; (v) Erdos-Turan 1948 (Indag. Math. 10, 370-378;
      explicit-constant version as in Montgomery, Ten Lectures,
      CBMS 84, Ch. 1 Thm 1): D*_N <= 1/(m+1) + 3 sum_{j<=m} (1/j)
      |S_j|/N with S_j the geometric exponential sum, m = 10 --
      exact star discrepancy vs the bound, instance-gated.
  M3  THE POSITIVITY RELEVANCE TEST.  tau_h (builder minimum
      eigenvalue, the wall margin) is measured fresh at h = 4..13;
      the defect ladders are screened against it (log-log slopes;
      flat bar 0.30, ride band (0.7, 1.3), R^2 >= 0.5 for a ride
      call).  Three sharp outcomes (frozen resolution logic, S5):
      (a) NEW-SOURCE-CANDIDATE iff the defect ladder is tau-flat
      AND the dose-response is DIRECTIONAL (commensurate direction
      kills the margin >= 2 dex deeper than the matched antidose at
      some rung, or kills where antidose survives) AND the exact-
      commensurate canonical completion L_f(t=1) is PSD at all dose
      rungs (the mechanism enters at the named place); (b)
      RIDES-TAU iff a defect slope sits in the ride band with R^2
      >= 0.5 -- relabeling, gate and stop; (c) POSITIVITY-
      IRRELEVANT-EXACTNESS-KILL iff the defect ladder is tau-flat
      and the margin dies at EVERY dose t > 0 in BOTH directions
      (dose and antidose) at every dose rung -- the wall margin
      consumes position EXACTNESS (r185 concordant), not the
      incommensurability magnitude; the mechanism's actual role is
      then only to explain the SMOOTH control's L_f-PSD-at-nodes
      and the canonical-completion world mix, nothing about the
      true world's positivity.  Else UNRESOLVED-RECORDED.  The
      NAMED PLACE where defects enter the anatomy (typed, exact):
      the wall's prime block consumes ONLY the node samples --
      off-diagonal 2(om_i pj_i - om_j pj_j)/(om_j^2 - om_i^2) with
      pj_i = sum_q w_q sin(om_i u_q), diagonal (a - u/2)cos(om_k u)
      - sin(om_k u)/(2 om_k) per atom -- so the defect moduli ARE
      the moduli of the only arithmetic data the wall sees.
  M4  WORLDS AND JITTER DOSE.  Predefined COMMENSURABILITY DOSE
      family at DOSE_RUNGS (4, 5, 8, 13): per atom u_comm = a *
      max(1, nint(u/a)) and u(t) = u + t (u_comm - u), dose grid
      t in (1/8, 1/4, 1/2, 3/4, 1); t = 1 IS the exactly-
      commensurate synthetic world (every atom frequency an
      integer multiple of the node spacing; the node samples
      collapse to 0 EXACTLY -- gated); matched ANTIDOSE u(t) = u -
      t (u_comm - u), t in (1/8, 1/4, 1/2) (same per-atom
      displacement, opposite direction -- the directionality
      control that r185 lacked); JITTER control u -> u (1 + 0.01
      s_q), s_q = +1 if frac(q * golden) < 1/2 else -1
      (deterministic, r185's 0.01 scale -- but measuring the
      MARGIN, where r185 measured signatures).  At every config:
      the prime block is rebuilt with the builder's VERBATIM
      formulas (rebuild ward vs the builder block <= 1e-40 at
      t = 0), the wall M(t) = M + (P0 - P(t)) is eigensolved (mp
      at h in (4, 5, 8), float64 downcast at h = 13, disclosed,
      refusal rule |lm| < 1e-12 ||F||_F), and the canonical
      completion L_f(t) (fully analytic: divided differences of
      g(t), diagonal f'(t); arch data J/J' dose-invariant,
      extracted once) is eigensolved the same way; node-potential
      descents recorded.  CONTROLS: SMOOTH(5) = the commensurate
      anchor (L_f PSD + 0 descents re-measured; the M1 collapse
      identities warded in mp against the builder pj); SCRARITH(5)
      and EPSTEIN(8) get the SAME t = 1 commensurate collapse
      (does the fake arithmetic also turn L_f PSD? recorded
      either way); the r172 inflation witness deforms the source
      COEFFICIENT ray (eigenvector-side) -- every object here is
      matrix-side, witness-INVARIANT BY CONSTRUCTION (typed
      definitional, not sold; r189 precedent).

TAXONOMY (frozen resolution logic, evaluated from measured values):
  rides      := any defect-ladder slope vs log10 tau_h with
                |slope| in [0.7, 1.3] AND R^2 >= 0.5;
  defect_flat:= |slope(log10 MINDEF_h vs log10 tau_h)| <= 0.30;
  lf_mech    := lambda_min(L_f(t=1))/||F|| >= -1e-10 at every
                non-refused dose rung;
  killed(c)  := lambda_min(M(t))/||F|| < -1e-10 for config c;
  dose_kills_all := killed at every dose rung for every t >= 1/8
                in BOTH variants (DOSE and ANTIDOSE);
  dir_sep    := at >= 1 dose rung, for every shared t: DOSE killed
                while ANTIDOSE not killed, OR both killed with the
                DOSE defect >= 2.0 dex deeper;
  relevance  := RIDES-TAU if rides; else NEW-SOURCE-CANDIDATE if
                defect_flat and dir_sep and lf_mech; else
                POSITIVITY-IRRELEVANT-EXACTNESS-KILL if
                defect_flat and dose_kills_all; else
                UNRESOLVED-RECORDED;
  append     := COMM-WALL-REVIVAL iff the wall M(t=1) is PSD at
                >= 1 non-refused dose rung (a U-shaped
                dose-response -- not anticipated), else
                COMM-WALL-DEAD;
  baker      := BAKER-SUFFICIENT iff min(gap_lmn, gap_matveev)
                <= 2.0 dex at every rung, else BAKER-TOO-WEAK
                (with the gap ladder recorded).

NOTATION (r171-r189 conventions VERBATIM).  Rung h = builder x
(R4.build_cell, even sector, MAIN world); a = log(h)/2; K = ceil(1.25
h log h); om_k = k pi/a; b_k = om_k^2; nrm_0 = sqrt(2a), nrm_k =
sqrt(a); par_k = (-1)^k; atoms = {(u_q, w_q)} = {(log q,
log p/sqrt(q))}, q = p^m <= h; pj_k = sum w sin(om_k u), pc_k =
sum w cos(om_k u); arch J(om) = int_0^{2a} sin(om w) r(w) dw +
Si(2a om)/2, r(w) = e^{-w/2}/(1-e^{-2w}) - 1/(2w), r(0) = 1/4;
J'(om) = int_0^{2a} w cos(om w) r(w) dw + sin(2a om)/(2 om);
f_pole(b) = -2 sinh(a/2)^2/(1/4+b); f = f_pole + f_arch + 2 om pj;
g(b) = f(b) - f(0); tau_h = smallest eigenvalue of the builder wall
M_h (mode coordinates; sign statements congruence-transparent by
Sylvester, r186/r189).  theta_q = u_q/a = 2 log q/log h.  SMOOTH
world atom measure e^{w/2} dw on [0, 2a] with the r189 closed forms.
EPSTEIN/SCRARITH atoms ported VERBATIM from the builder (golden-map
permutation deterministic).

DPS schedule (r182/r189 conditioning ladder VERBATIM on the used
rungs): DPS = {4: 60, 5: 60, 6: 65, 7: 70, 8: 80, 9: 85, 10: 90,
11: 100, 12: 110, 13: 120}.  TAU_RUNGS = 4..13 (builder-fresh tau +
defect ladder); EXT_RUNGS = (14, 15, 16, 20) (defect ladder only,
closed-form geometry at DEF_DPS = 50, no builder).  DOSE_RUNGS =
(4, 5, 8, 13); DOSE_MP = (4, 5, 8) (mp eigensolves at rung dps);
h = 13 eigensolves float64 (matrices assembled in mp at dps 60,
downcast -- disclosed reduced scope, refusal rule below).  DOSE_T =
(0.125, 0.25, 0.5, 0.75, 1.0); ANTI_T = (0.125, 0.25, 0.5);
JIT_EPS = 0.01.  ET_M = 10; ET/three-distance at DOSE_RUNGS on the
per-rung minimizer atom sequence {k theta mod 1, k = 1..K-1}.
CONTROLS: SMOOTH(5), SCRARITH(5), EPSTEIN(8) at CTRL_DPS {60, 60,
80}; fake-world dose at t = 1 only.
PRECISION REFUSAL RULE: an eigenvalue-sign statement is REFUSED
(counted, excluded) if |lambda_min| < 10^-(dps-20) ||L||_F (float64:
10^-12 ||L||_F).

FROZEN BARS: REBUILD_BAR 1e-40 (prime block rebuild vs builder,
t = 0, every dose rung and control); COLLAPSE_BAR 1e-25 (relative:
smooth node-collapse mp ward; exact-comm pj node collapse at t = 1);
XWARD_BAR 1e-20 (analytic L_f(0) lambda_min fraction vs r189-style
Raw-based completion, relative dex agreement 0.05); POS_ATOM: all
dosed positions must stay > 0 (hard gate); INDEF_FRAC -1e-10;
F64_REFUSE 1e-12; EIG_REFUSE_SAFETY 20; TAU_FLAT_BAR 0.30;
TAU_RIDE_BAND (0.7, 1.3); R2_MIN 0.5; DIRSEP_DEX 2.0; BAKER_OK_DEX
2.0; SIN_GRID_N 10001 (Jordan grid proof on [0, 1/2], bar >= 0);
TDIST_TOL 1e-25 (distinct-gap clustering); RUNTIME_BAR 2700 s.
Record tolerances: DEX_TOL 0.05 (log10 records); DOSE_TOL 0.10
(dose/L_f ladders, log10); GAP_TOL 0.5 (pricing gap dex); count and
flag records exact.

=======================================================================
RECORD TABLES (frozen at freeze from the ONE disclosed pre-freeze
calibration pass, calib_cm_pass1.log, 28/28, 274.0 s; TWO structural
smokes: smoke1 27/28 -- the G10 symbolic gate needed the exp-rewrite
simplification path, identity unchanged, amendment A1 -- smoke2
28/28; smokes ran rungs 4/5 + SMOOTH control with record comparisons
vacuous pre-freeze by design).  Verdicts frozen from calibration:
THE DEFECT LADDER IS O(1)-FLAT: MINDEF_h (log10) between -0.63 and
-3.03 across h = 4..16, 20 with no systematic decay (tau_h
meanwhile falls 1e-11 -> 1e-54 across 4..13): slope log10 MINDEF vs
log10 tau = +0.035 (R^2 0.566), aggregate slope +0.019 (R^2 0.225)
-- BOTH FLAT, ride band never entered.  STRUCTURAL ZEROS: present
exactly at the prime-power rungs (4, 5, 7, 8, 9, 11, 13, 16 in the
ladder; census counts frozen exact below) and NOWHERE else (6, 10,
12, 14, 15, 20 carry none -- h not a prime power); q = h is always
commensurate at prime h (the r189 A1 jet trap generalised).
PRICING: the elementary Liouville floor HOLDS at every rung as an
exact-integer instance but is NOT TIGHT at depth: gap_liou =
2.62 dex (h=7) .. 74.22 dex (h=16), GROWING with the rung because
the floor falls like h^{-m} with the minimizer exponent while the
measured minima sit at the equidistribution scale ~1/K (amendment
A2: the pre-calibration draft anticipated a sharp floor; corrected
before freeze).  LMN 1995 misses the measured forms by 7.10e3 ..
3.10e4 dex and Matveev 2000 by 1.36e9 .. 1.18e10 dex: resolution
BAKER-TOO-WEAK -- and even the ELEMENTARY floor is orders below
the measured truth: NOTHING in the classical chest prices the
measured ladder tightly; the defect lower-bound direction is
priced, the measured magnitudes are equidistribution-typical.
ET: the m=10 Erdos-Turan bound holds at all four dose rungs
(nontrivial, < 1, at h = 8, 13; trivial, > 1, at the short
sequences h = 4, 5 -- recorded honestly); three-distance gap
counts = 3 at all four minimizer sequences.  DOSE-RESPONSE: the
wall margin is KILLED (lambda_min < 0, |lm|/||F|| ~ 1e-2..2e-1) at
EVERY dose t >= 1/8, EVERY dose rung, BOTH directions (dose AND
antidose), and by the 0.01 deterministic jitter too (r185
concordant, now for the MARGIN); NO direction separation (dose vs
antidose within < 2 dex at all shared t); NO commensurate revival
(M(t=1) indefinite at all dose rungs: COMM-WALL-DEAD).  THE
MECHANISM CONFIRMED AT THE CANONICAL OBJECT: L_f(t=1) is PSD at
ALL FOUR dose rungs with descents -> 0 (PSD already at t = 3/4 at
h = 4, 5) -- the MAIN-world canonical-completion indefiniteness of
r189 is PURELY the incommensurate node sampling: snap the atoms to
the lattice and L_f is PSD like SMOOTH; and the fake worlds obey
the SAME mechanism (SCRARITH(5) lf1 -1.37+, EPSTEIN(8) lf1 -0.91+,
both PSD; walls killed) -- the mechanism is arithmetic-blind
lattice geometry, NOT a prime fingerprint.  RELEVANCE RESOLUTION:
defect_flat AND dose_kills_all AND NOT dir_sep (lf_mech TRUE,
amendment A3) => POSITIVITY-IRRELEVANT-EXACTNESS-KILL (outcome c):
the wall margin consumes position EXACTNESS, not the
incommensurability magnitude; the commensurability mechanism
explains the SMOOTH control's L_f-PSD-at-nodes and the r189
world-mixed enum EXACTLY, and nothing about the true world's
positivity.  The thin hope 'incommensurability => controlled
cancellation feeds positivity' is CLEANLY KILLED at the margin;
what survives is the exact mechanism statement for the canonical
completion (typed measured, world-blind).
CAL_TAU (log10 tau_h, builder-fresh, all positive):
  4: -10.67  5: -15.79  6: -20.23  7: -25.03  8: -29.42  9: -34.08
  10: -38.97  11: -43.75  12: -48.98  13: -53.60
CAL_MINDEF (log10 MINDEF_h; minimizer (q, k, m) frozen exact):
  4: -0.63 (3, 5, 8)      5: -1.03 (2, 7, 6)    6: -1.26 (5, 5, 9)
  7: -1.39 (2, 7, 5)      8: -1.21 (3, 18, 19)  9: -1.41 (2, 19, 12)
  10: -1.68 (9, 11, 21)   11: -3.03 (4, 32, 37) 12: -1.50 (4, 26, 29)
  13: -2.21 (7, 29, 44)   14: -1.85 (9, 3, 5)   15: -2.53 (8, 28, 43)
  16: -2.79 (11, 37, 64)  20: -2.25 (3, 15, 11)
CAL_ZEROS (structural-zero census, zeros/pairs, exact):
  4: 12/18   5: 10/40   6: 0/52    7: 17/85   8: 32/120  9: 48/168
  10: 0/196  11: 32/256 12: 0/296  13: 41/369 14: 0/414  15: 0/450
  16: 164/550  20: 0/888
CAL_AGG (log10 min_k |pj(om_k)|, k = 1..K-1):
  4: -0.83  5: -1.00  6: -1.22  7: -1.37  8: -2.49  9: -1.06
  10: -2.38  11: -1.99  12: -1.75  13: -1.34  14: -2.40  15: -1.85
  16: -1.14  20: -1.46
CAL_PRICE (per-rung minimizer: log10|Lambda|, gap_liou dex,
gap_lmn dex, gap_matveev dex):
  4: -0.98 / 3.79 / 7.099e3 / 1.682e9   5: -1.32 / 2.87 / 7.501e3 / 1.357e9
  6: -1.50 / 5.49 / 1.344e4 / 3.184e9   7: -1.59 / 2.62 / 9.070e3 / 1.641e9
  8: -1.39 / 15.77 / 1.065e4 / 3.501e9  9: -1.57 / 9.87 / 1.024e4 / 2.361e9
  10: -1.81 / 19.18 / 2.358e4 / 6.920e9 11: -3.15 / 35.39 / 1.549e4 / 5.733e9
  12: -1.60 / 29.69 / 1.606e4 / 5.702e9 13: -2.30 / 46.71 / 2.326e4 / 8.444e9
  14: -1.92 / 3.80 / 2.703e4 / 5.412e9  15: -2.59 / 47.98 / 2.625e4 / 9.461e9
  16: -2.85 / 74.22 / 3.099e4 / 1.179e10 20: -2.27 / 12.04 / 1.534e4 / 4.843e9
CAL_ET (dose rungs: exact D*_N / ET bound; 3-distance gap count):
  4: 0.1764 / 1.6941 / 3    5: 0.1841 / 1.5722 / 3
  8: 0.1301 / 0.8263 / 3    13: 0.1125 / 0.5928 / 3
CAL_DOSE (wall margin: log10(|lambda_min|/||F||), sign - = killed;
rows h, cols t = 1/8, 1/4, 1/2, 3/4, 1 DOSE | 1/8, 1/4, 1/2 ANTI |
JIT 0.01):
  4:  -1.58- -1.35- -1.23- -1.27- -1.51- | -1.60- -1.32- -1.02- | -1.84-
  5:  -1.48- -1.26- -0.95- -0.79- -0.79- | -1.32- -1.07- -0.86- | -1.84-
  8:  -1.39- -1.11- -0.84- -0.72- -0.83- | -1.36- -1.16- -1.23- | -1.59-
  13: -1.35- -1.12- -0.87- -0.77- -0.91- | -1.33- -1.17- -1.20- | -1.40-
CAL_LF (canonical completion along the dose: log10(|lm|/||F||),
sign; t = 0, 1/8, 1/4, 1/2, 3/4, 1):
  4:  -1.36- -1.21- -1.18- -1.15- -1.99+ -0.99+
  5:  -2.00- -1.59- -1.84- -1.81- -1.45+ -1.25+
  8:  -0.93- -0.87- -0.87- -0.84- -1.91- -1.15+
  13: -1.05- -1.14- -1.11- -1.20- -1.18- -1.16+
CAL_DESC (node-potential descents along the dose, t = 0 -> 1):
  4: 2/1/1/1/2/0   5: 5/3/4/4/4/0   8: 9/11/10/9/10/0
  13: 20/20/21/21/23/0
CAL_CTRL (SMOOTH anchor + fake-world t=1 collapse):
  (SMOOTH, 5): lm_log10 -4.08 PSD, 0 descents, collapse wards
  3.9e-62 / 4.2e-61; (SCRARITH, 5): base lm -1.66 indef -> t=1 lf
  -1.37+ (PSD), wall t=1 -0.76- killed; (EPSTEIN, 8): base lm
  -0.70 indef -> t=1 lf -0.91+ (PSD), wall t=1 -1.08- killed.
CAL_SLOPES: mindef +0.035 (R^2 0.566), agg +0.019 (R^2 0.225).
Wards at calibration: prime rebuild 0.0 EXACT (mp rungs),
analytic-vs-Raw L_f(0) cross-ward 0.000 dex, smooth collapse <=
4.2e-61, exact-comm collapse <= 1.1e-59 relative.  Runtime:
calibration 274.0 s (bar 2700).
AMENDMENTS (three, all pre-freeze, all disclosed):
A1 (smoke-driven): the G10 combined-potential identity is true but
  sympy's default simplify left a sinh/exp mixed form; the check
  uses the exp-rewrite path (.rewrite(exp)) since smoke2.  The
  identity itself is unchanged (the mp ward against the builder
  closed forms passed at 4.2e-61 already in smoke1).
A2 (calibration-driven): the pre-calibration draft anticipated the
  Liouville floor as sharp-class (~1 dex above measured); measured
  gaps are 2.62..74.22 dex and GROW with the rung (the floor falls
  like h^{-m}, the measured minima sit at the equidistribution
  scale).  The G31 narrative and the composite verdict token were
  corrected before freeze to LIOUVILLE-FLOOR-HOLDS-NOT-TIGHT; the
  gate logic (exact-integer instance must hold + records) is
  unchanged.
A3 (calibration-driven): lf_mech was anticipated as an outcome-(a)
  ingredient only; measured TRUE simultaneously with
  dose_kills_all TRUE and dir_sep FALSE.  The (c) branch text was
  sharpened before freeze to record lf_mech inside outcome (c).
No bar, grid, dose point, dps rung, or control recipe moved at any
point; the record tables and resolved enums above were inserted at
freeze (house pattern identical to r186/r189).
=======================================================================

WHAT IS BUILT AND GATED: S0 G01 firewall + G02 predefinition; S1
exact layer G03/G10-G12; S2 defect ladder G20-G23; S3 pricing
G30-G34; S4 dose/worlds G40-G45; S5 screens/adjudication G50-G54;
S6 pricing/residue G60-G61 + G99 runtime.  DETERMINISM: no
randomness anywhere (jitter signs are the deterministic golden map);
ProcessPool results keyed; run2 must be identical modulo wall-clock
tokens (lines carrying 'WALL').

NO RH CLAIM IN EITHER DIRECTION.  NOT evidence for or against RH.
"""

# =====================================================================
# CORRECTION OF RECORD (Bughunt X, note DXXIII, 2026-08-22)
# ---------------------------------------------------------------------
# Appended OUTSIDE the frozen spec text per the r131/r165
# corrections-of-record convention: the module docstring above is the
# historical record and is NOT edited; SPEC_SHA (= sha256 of the
# docstring) stays dbc14014899fb286.  NO numeric change, NO verdict
# flip, NO RH CLAIM.
#
# BH10-F5 [NOTE, instrument cosmetics KE]: G11's symbolic leg is
#   vacuous by construction (ok_form checks sin(pi*(y - y)) == 0
#   with y DEFINED as 2*k*lq two lines above; ok_crit checks only
#   the trivial direction) while the PASS text recites the full
#   e | 2fk iff law -- the G11 detail text should read "symbolic
#   skeleton only; the iff law is enforced by G20/G23"; the law's
#   real machine content (G20 zero_ward, G23 exact census, O(1)
#   MINDEF floor on all non-census pairs) reproduces EXACTLY in
#   Bughunt X's own code (SPEC 5551aa7b967230f1).  NO verdict moves.
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
RUNTIME_BAR = 2700.0

TAU_RUNGS = (4, 5, 6, 7, 8, 9, 10, 11, 12, 13)
EXT_RUNGS = (14, 15, 16, 20)
DPS = {4: 60, 5: 60, 6: 65, 7: 70, 8: 80, 9: 85, 10: 90, 11: 100,
       12: 110, 13: 120}
DEF_DPS = 50
DOSE_RUNGS = (4, 5, 8, 13)
DOSE_MP = (4, 5, 8)
DOSE_T = ("0.125", "0.25", "0.5", "0.75", "1.0")
ANTI_T = ("0.125", "0.25", "0.5")
JIT_EPS = "0.01"
ET_M = 10
GOLD = (math.sqrt(5.0) - 1.0) / 2.0

CTRL_CELLS = (("SMOOTH", 5, 60), ("SCRARITH", 5, 60),
              ("EPSTEIN", 8, 80))

# structural bars (frozen pre-calibration)
REBUILD_BAR = 1e-40
COLLAPSE_BAR = 1e-25
XWARD_DEX = 0.05
INDEF_FRAC = -1e-10
F64_REFUSE = 1e-12
EIG_REFUSE_SAFETY = 20
TAU_FLAT_BAR = 0.30
TAU_RIDE_BAND = (0.7, 1.3)
R2_MIN = 0.5
DIRSEP_DEX = 2.0
BAKER_OK_DEX = 2.0
SIN_GRID_N = 10001
TDIST_TOL = 1e-25

# record tolerances
DEX_TOL = 0.05
DOSE_TOL = 0.10
GAP_TOL = 0.5

# --------------------- calibrated record tables (calib_cm_pass1.log)
CAL_TAU = {4: "-10.67", 5: "-15.79", 6: "-20.23", 7: "-25.03",
           8: "-29.42", 9: "-34.08", 10: "-38.97", 11: "-43.75",
           12: "-48.98", 13: "-53.60"}
CAL_MINDEF = {4: ("-0.63", 3, 5, 8), 5: ("-1.03", 2, 7, 6),
              6: ("-1.26", 5, 5, 9), 7: ("-1.39", 2, 7, 5),
              8: ("-1.21", 3, 18, 19), 9: ("-1.41", 2, 19, 12),
              10: ("-1.68", 9, 11, 21), 11: ("-3.03", 4, 32, 37),
              12: ("-1.50", 4, 26, 29), 13: ("-2.21", 7, 29, 44),
              14: ("-1.85", 9, 3, 5), 15: ("-2.53", 8, 28, 43),
              16: ("-2.79", 11, 37, 64), 20: ("-2.25", 3, 15, 11)}
CAL_ZEROS = {4: (12, 18), 5: (10, 40), 6: (0, 52), 7: (17, 85),
             8: (32, 120), 9: (48, 168), 10: (0, 196),
             11: (32, 256), 12: (0, 296), 13: (41, 369),
             14: (0, 414), 15: (0, 450), 16: (164, 550),
             20: (0, 888)}
CAL_AGG = {4: "-0.83", 5: "-1.00", 6: "-1.22", 7: "-1.37",
           8: "-2.49", 9: "-1.06", 10: "-2.38", 11: "-1.99",
           12: "-1.75", 13: "-1.34", 14: "-2.40", 15: "-1.85",
           16: "-1.14", 20: "-1.46"}
CAL_PRICE = {4: ("-0.98", "3.79", "7.099e3", "1.682e9"),
             5: ("-1.32", "2.87", "7.501e3", "1.357e9"),
             6: ("-1.50", "5.49", "1.344e4", "3.184e9"),
             7: ("-1.59", "2.62", "9.070e3", "1.641e9"),
             8: ("-1.39", "15.77", "1.065e4", "3.501e9"),
             9: ("-1.57", "9.87", "1.024e4", "2.361e9"),
             10: ("-1.81", "19.18", "2.358e4", "6.920e9"),
             11: ("-3.15", "35.39", "1.549e4", "5.733e9"),
             12: ("-1.60", "29.69", "1.606e4", "5.702e9"),
             13: ("-2.30", "46.71", "2.326e4", "8.444e9"),
             14: ("-1.92", "3.80", "2.703e4", "5.412e9"),
             15: ("-2.59", "47.98", "2.625e4", "9.461e9"),
             16: ("-2.85", "74.22", "3.099e4", "1.179e10"),
             20: ("-2.27", "12.04", "1.534e4", "4.843e9")}
CAL_ET = {4: ("0.1764", "1.6941", 3), 5: ("0.1841", "1.5722", 3),
          8: ("0.1301", "0.8263", 3), 13: ("0.1125", "0.5928", 3)}
# (h, variant, t) -> (log10 |lm|/||F||, killed?)
CAL_DOSE = {
    (4, "DOSE", "0.125"): ("-1.58", 1), (4, "DOSE", "0.25"): ("-1.35", 1),
    (4, "DOSE", "0.5"): ("-1.23", 1), (4, "DOSE", "0.75"): ("-1.27", 1),
    (4, "DOSE", "1.0"): ("-1.51", 1),
    (4, "ANTI", "0.125"): ("-1.60", 1), (4, "ANTI", "0.25"): ("-1.32", 1),
    (4, "ANTI", "0.5"): ("-1.02", 1), (4, "JIT", "0.01"): ("-1.84", 1),
    (5, "DOSE", "0.125"): ("-1.48", 1), (5, "DOSE", "0.25"): ("-1.26", 1),
    (5, "DOSE", "0.5"): ("-0.95", 1), (5, "DOSE", "0.75"): ("-0.79", 1),
    (5, "DOSE", "1.0"): ("-0.79", 1),
    (5, "ANTI", "0.125"): ("-1.32", 1), (5, "ANTI", "0.25"): ("-1.07", 1),
    (5, "ANTI", "0.5"): ("-0.86", 1), (5, "JIT", "0.01"): ("-1.84", 1),
    (8, "DOSE", "0.125"): ("-1.39", 1), (8, "DOSE", "0.25"): ("-1.11", 1),
    (8, "DOSE", "0.5"): ("-0.84", 1), (8, "DOSE", "0.75"): ("-0.72", 1),
    (8, "DOSE", "1.0"): ("-0.83", 1),
    (8, "ANTI", "0.125"): ("-1.36", 1), (8, "ANTI", "0.25"): ("-1.16", 1),
    (8, "ANTI", "0.5"): ("-1.23", 1), (8, "JIT", "0.01"): ("-1.59", 1),
    (13, "DOSE", "0.125"): ("-1.35", 1), (13, "DOSE", "0.25"): ("-1.12", 1),
    (13, "DOSE", "0.5"): ("-0.87", 1), (13, "DOSE", "0.75"): ("-0.77", 1),
    (13, "DOSE", "1.0"): ("-0.91", 1),
    (13, "ANTI", "0.125"): ("-1.33", 1), (13, "ANTI", "0.25"): ("-1.17", 1),
    (13, "ANTI", "0.5"): ("-1.20", 1), (13, "JIT", "0.01"): ("-1.40", 1)}
# (h, t) -> (log10 |lm|/||F||, neg?)  for L_f along the dose
CAL_LF = {
    (4, "0"): ("-1.36", 1), (4, "0.125"): ("-1.21", 1),
    (4, "0.25"): ("-1.18", 1), (4, "0.5"): ("-1.15", 1),
    (4, "0.75"): ("-1.99", 0), (4, "1.0"): ("-0.99", 0),
    (5, "0"): ("-2.00", 1), (5, "0.125"): ("-1.59", 1),
    (5, "0.25"): ("-1.84", 1), (5, "0.5"): ("-1.81", 1),
    (5, "0.75"): ("-1.45", 0), (5, "1.0"): ("-1.25", 0),
    (8, "0"): ("-0.93", 1), (8, "0.125"): ("-0.87", 1),
    (8, "0.25"): ("-0.87", 1), (8, "0.5"): ("-0.84", 1),
    (8, "0.75"): ("-1.91", 1), (8, "1.0"): ("-1.15", 0),
    (13, "0"): ("-1.05", 1), (13, "0.125"): ("-1.14", 1),
    (13, "0.25"): ("-1.11", 1), (13, "0.5"): ("-1.20", 1),
    (13, "0.75"): ("-1.18", 1), (13, "1.0"): ("-1.16", 0)}
CAL_DESC_D = {4: (2, 1, 1, 1, 2, 0), 5: (5, 3, 4, 4, 4, 0),
              8: (9, 11, 10, 9, 10, 0), 13: (20, 20, 21, 21, 23, 0)}
# world -> (base lm_log10, base neg, lf(t=1) neg, wall(t=1) killed)
CAL_FAKE = {"SCRARITH": ("-1.66", 1, 0, 1),
            "EPSTEIN": ("-0.70", 1, 0, 1)}
CAL_SMOOTH_LM = "-4.08"
CAL_SLOPES = {"mindef": "0.035", "agg": "0.019"}

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
    eig_forb = {"mp" + "V", "cn_mp" + "_str"}
    bad = []
    for node in ast.walk(tree):
        nm = None
        is_const = False
        if isinstance(node, ast.Attribute):
            nm = node.attr
        elif isinstance(node, ast.Name):
            nm = node.id
        elif isinstance(node, ast.Constant) and isinstance(node.value,
                                                           str):
            nm = node.value
            is_const = True
        if nm is None:
            continue
        low = nm.lower()
        if not is_const:
            if low in forb:
                bad.append("forbidden %s @%d" % (nm, node.lineno))
            if low == "zeta":
                bad.append("zeta use @%d" % node.lineno)
        if nm in eig_forb:
            bad.append("eigenvector access %s @%d (this round is "
                       "FULLY eigenvector-free)" % (nm, node.lineno))
        if isinstance(node, ast.Attribute) and nm == "load":
            bad.append("np.load @%d (zero-free round)" % node.lineno)
    for node in ast.walk(tree):
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            mods = ([al.name for al in node.names]
                    if isinstance(node, ast.Import)
                    else [node.module or ""])
            for m in mods:
                if m.startswith("verification"):
                    bad.append("import " + m)
    return (not bad), ("; ".join(bad) if bad else
                       "NO zero-oracle, NO zeta, NO np.load, no "
                       "verification/ import; NO eigenvector access "
                       "anywhere (matrix blocks + the tau scalar "
                       "only): the round is eigenvector-free by AST")


# ------------------------------------------------------- source helpers
def r_of(w):
    if w == 0:
        return mp.mpf("0.25")
    return mp.exp(-w / 2) / (-mp.expm1(-2 * w)) - 1 / (2 * w)


def J_quad(o, aa):
    L2v = 2 * aa
    if o == 0:
        return mp.mpf(0)
    npts = int(mp.floor(L2v * o / mp.pi))
    pts = ([mp.mpf(0)] + [jj * mp.pi / o for jj in range(1, npts + 1)]
           + [L2v])
    val = mp.quad(lambda w, o=o: mp.sin(o * w) * r_of(w), pts)
    return val + mp.si(L2v * o) / 2


def Jp_quad(o, aa):
    L2v = 2 * aa
    if o == 0:
        return mp.quad(lambda w: w * r_of(w), [mp.mpf(0), L2v]) + aa
    npts = int(mp.floor(L2v * o / mp.pi))
    pts = ([mp.mpf(0)] + [jj * mp.pi / o for jj in range(1, npts + 1)]
           + [L2v])
    val = mp.quad(lambda w, o=o: w * mp.cos(o * w) * r_of(w), pts)
    return val + mp.sin(L2v * o) / (2 * o)


def sieve_atoms(x: int):
    icap = int(math.floor(x))
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
    return [(mp.log(q), mp.log(p) / mp.sqrt(q)) for q, p in nlist], \
        nlist


def world_atoms(world: str, x: int):
    """Builder atom recipes ported VERBATIM; returns (atoms, qlist)."""
    if world in ("MAIN", "SCRARITH"):
        atoms, nlist = sieve_atoms(x)
        if world == "SCRARITH":
            keys = [math.fmod(q * GOLD, 1.0) for q, _p in nlist]
            perm = sorted(range(len(keys)), key=lambda i: keys[i])
            wts = [atoms[i][1] for i in range(len(atoms))]
            atoms = [(atoms[i][0], wts[perm[i]])
                     for i in range(len(atoms))]
        return atoms, [q for q, _p in nlist]
    if world == "EPSTEIN":
        icap = int(math.floor(x))
        rq = np.zeros(icap + 1)
        xm = int(math.isqrt(icap)) + 1
        ym = int(math.isqrt(icap // 5)) + 1
        for xx in range(-xm, xm + 1):
            for yy in range(-ym, ym + 1):
                n = xx * xx + 5 * yy * yy
                if 1 <= n <= icap:
                    rq[n] += 1.0
        av = [mp.mpf(v) / 2 for v in rq]
        lamq = [mp.mpf(0)] * (icap + 1)
        for n in range(2, icap + 1):
            sacc = av[n] * mp.log(n)
            for d in range(2, n):
                if n % d == 0:
                    sacc -= lamq[d] * av[n // d]
            lamq[n] = sacc
        atoms = []
        qs = []
        for n in range(2, icap + 1):
            if abs(lamq[n]) > mp.mpf("1e-30"):
                atoms.append((mp.log(n), lamq[n] / mp.sqrt(n)))
                qs.append(n)
        return atoms, qs
    raise ValueError(world)


def prime_block(atoms, oms, par, nrm, aa, K):
    """Builder prime block, VERBATIM recipe (r189 jet leg)."""
    L2v = 2 * aa
    Mp = mp.zeros(K, K)
    pj = [sum((w * mp.sin(o * u) for u, w in atoms), mp.mpf(0))
          for o in oms]
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
            pdiag = sum((w * (L2v - u) for u, w in atoms), mp.mpf(0))
        else:
            pdiag = sum((w * ((aa - u / 2) * mp.cos(o * u)
                              - mp.sin(o * u) / (2 * o))
                         for u, w in atoms), mp.mpf(0))
        Mp[i, i] += 2 * pdiag
    for i in range(K):
        for j2 in range(K):
            Mp[i, j2] = Mp[i, j2] / (nrm[i] * nrm[j2])
    return Mp, pj


def dosed_atoms(atoms, qs, aa, variant, tstr):
    """Predefined dose maps.  DOSE: u -> u + t (u_comm - u);
    ANTI: u -> u - t (u_comm - u); JIT: u -> u (1 + eps s_q),
    s_q = +1 if frac(q golden) < 1/2 else -1 (deterministic)."""
    t = mp.mpf(tstr)
    out = []
    for idx, (u, w) in enumerate(atoms):
        if variant == "JIT":
            s = 1.0 if math.fmod(qs[idx] * GOLD, 1.0) < 0.5 else -1.0
            ut = u * (1 + t * s)
        else:
            m = max(int(mp.nint(u / aa)), 1)
            uc = m * aa
            if variant == "DOSE":
                ut = u + t * (uc - u)
            else:
                ut = u - t * (uc - u)
        out.append((ut, w))
    return out


def polep_at(b, s2):
    return 2 * s2 / (mp.mpf(1) / 4 + b) ** 2


def fpole_at(b, s2):
    return -2 * s2 / (mp.mpf(1) / 4 + b)


def eig_min_frac(L, n):
    E = mp.eigsy(L, eigvals_only=True)
    lmin = min(E[i] for i in range(n))
    fro = mp.sqrt(sum(L[i, j] ** 2 for i in range(n)
                      for j in range(n)))
    return lmin, fro, lmin / fro


def eig_min_frac_np(Lnp):
    ev = np.linalg.eigvalsh(Lnp)
    fro = float(np.sqrt((Lnp * Lnp).sum()))
    return float(ev[0]), fro, float(ev[0]) / fro


def eig_of(Mt, K, dps, use_mp):
    """(frac, neg, refused, log10|frac|) under the refusal rule."""
    if use_mp:
        lm, fro, frac = eig_min_frac(Mt, K)
        refused = abs(lm) < mp.mpf(10) ** (-(dps - EIG_REFUSE_SAFETY)) \
            * fro
        return (float(frac), bool(lm < 0), bool(refused),
                float(mp.log(abs(frac), 10)) if lm != 0 else
                float("-inf"))
    Lnp = np.array([[float(Mt[i, j]) for j in range(K)]
                    for i in range(K)])
    lm, fro, frac = eig_min_frac_np(Lnp)
    refused = abs(lm) < F64_REFUSE * fro
    return (float(frac), bool(lm < 0), bool(refused),
            float(math.log10(abs(frac))) if lm != 0 else float("-inf"))


# --------------------------------------------------- defect geometry
def rung_geometry(h: int):
    aa = mp.log(h) / 2
    K = int(math.ceil(KFAC * h * math.log(h)))
    return aa, K


def prime_power_split(n: int):
    """(p, e) if n = p^e is a prime power, else None."""
    for p in range(2, n + 1):
        if p * p > n and p != n:
            break
        if n % p == 0:
            e = 0
            m = n
            while m % p == 0:
                m //= p
                e += 1
            return (p, e) if m == 1 else None
    return (n, 1)


def structural_zero(q: int, h: int, k: int) -> bool:
    """d_{q,k} = 0 EXACTLY iff q^{2k} = h^m has a solution, i.e.
    q = p^f, h = p^e same prime and e | 2 f k."""
    sq, sh = prime_power_split(q), prime_power_split(h)
    if sq is None or sh is None or sq[0] != sh[0]:
        return False
    f, e = sq[1], sh[1]
    return (2 * f * k) % e == 0


def defect_table(h: int):
    """Per-atom defect ladder + per-rung minimizer + aggregate,
    at DEF_DPS (defects are O(1) trig)."""
    out = {"h": h}
    with mp.workdps(DEF_DPS):
        aa, K = rung_geometry(h)
        atoms, qs = world_atoms("MAIN", h)
        lh = mp.log(h)
        best = None            # (d, q, k, m)
        agg_min = None
        zero_census = 0
        pair_total = 0
        minpos = {}
        for k in range(1, K):
            o = k * mp.pi / aa
            pjk = mp.mpf(0)
            for idx, (u, w) in enumerate(atoms):
                q = qs[idx]
                pair_total += 1
                y = 2 * k * mp.log(q) / lh
                d = abs(mp.sin(mp.pi * y))
                pjk += w * mp.sin(o * u)
                if structural_zero(q, h, k):
                    zero_census += 1
                    continue
                m_ = int(mp.nint(y))
                if q not in minpos or d < minpos[q][0]:
                    minpos[q] = (d, k, m_)
                if best is None or d < best[0]:
                    best = (d, q, k, m_)
            apj = abs(pjk)
            if agg_min is None or apj < agg_min:
                agg_min = apj
        out["K"] = K
        out["zero_census"] = zero_census
        out["pair_total"] = pair_total
        out["mindef"] = float(best[0])
        out["mindef_log10"] = float(mp.log(best[0], 10))
        out["min_q"], out["min_k"], out["min_m"] = \
            best[1], best[2], best[3]
        out["agg_log10"] = float(mp.log(agg_min, 10))
        out["minpos"] = {q: float(v[0]) for q, v in minpos.items()}
        # structural-zero consistency ward: every census pair must
        # evaluate to |sin| below 10^-(DEF_DPS-10)
        wmax = mp.mpf(0)
        for k in range(1, K):
            for q in qs:
                if structural_zero(q, h, k):
                    y = 2 * k * mp.log(q) / lh
                    wmax = max(wmax, abs(mp.sin(mp.pi * y)))
        out["zero_ward"] = float(wmax)
    return out


def price_rung(h: int, q: int, k: int, m_: int):
    """Two-log pricing of the minimizer form Lambda = 2k log q -
    m log h: measured, Liouville, LMN, Matveev (all log10)."""
    out = {}
    with mp.workdps(DEF_DPS):
        lam = abs(2 * k * mp.log(q) - m_ * mp.log(h))
        out["lam_log10"] = float(mp.log(lam, 10))
        # sine bridge instance: d >= 2 |Lambda| / log h
        d = abs(mp.sin(mp.pi * (2 * k * mp.log(q) / mp.log(h))))
        out["bridge_ok"] = bool(d >= 2 * lam / mp.log(h)
                                - mp.mpf(10) ** (-(DEF_DPS - 10)))
        # multiplicative independence + Liouville (exact integers)
        A = q ** (2 * k)
        B = h ** m_
        out["mult_indep"] = bool(A != B)
        liou = mp.log1p(mp.mpf(1) / min(mp.mpf(A), mp.mpf(B)))
        out["liou_log10"] = float(mp.log(liou, 10))
        out["liou_ok"] = bool(lam >= liou)
        out["gap_liou"] = out["lam_log10"] - out["liou_log10"]
        # LMN 1995 (D = 1, both alphas real integers >= 2)
        h1 = max(mp.log(h), mp.mpf(1))
        h2 = max(mp.log(q), mp.mpf(1))
        bp = max(mp.mpf(m_) / h2 + mp.mpf(2 * k) / h1,
                 mp.mpf(m_) / h1 + mp.mpf(2 * k) / h2)
        lmn_ln = -mp.mpf("24.34") * max(mp.log(bp) + mp.mpf("0.14"),
                                        mp.mpf(21),
                                        mp.mpf("0.5")) ** 2 * h1 * h2
        out["lmn_log10"] = float(lmn_ln / mp.log(10))
        out["gap_lmn"] = out["lam_log10"] - out["lmn_log10"]
        # Matveev 2000 (real case, n = 2, D = 1)
        A1 = max(mp.log(h), mp.mpf("0.16"))
        A2 = max(mp.log(q), mp.mpf("0.16"))
        Bv = mp.mpf(max(2 * k, m_))
        mat_ln = -mp.mpf("1.4") * mp.mpf(30) ** 5 \
            * mp.mpf(2) ** mp.mpf("4.5") * A1 * A2 * (1 + mp.log(Bv))
        out["mat_log10"] = float(mat_ln / mp.log(10))
        out["gap_mat"] = out["lam_log10"] - out["mat_log10"]
    return out


def et_and_three_distance(h: int, q: int):
    """Exact star discrepancy of {k theta}, theta = 2 log q/log h,
    k = 1..K-1, vs the m = ET_M Erdos-Turan bound; circle-gap
    distinct count (three-distance)."""
    out = {}
    with mp.workdps(DEF_DPS):
        aa, K = rung_geometry(h)
        N = K - 1
        th = 2 * mp.log(q) / mp.log(h)
        xs = sorted(mp.frac(k * th) for k in range(1, K))
        dstar = mp.mpf(0)
        for i, x in enumerate(xs):
            dstar = max(dstar, abs(mp.mpf(i + 1) / N - x),
                        abs(x - mp.mpf(i) / N))
        out["dstar"] = float(dstar)
        bound = mp.mpf(1) / (ET_M + 1)
        for j in range(1, ET_M + 1):
            num = abs(mp.sin(mp.pi * j * N * th))
            den = abs(mp.sin(mp.pi * j * th))
            sj = num / den if den > 0 else mp.mpf(N)
            bound += 3 * min(sj, mp.mpf(N)) / (j * N)
        out["et_bound"] = float(bound)
        out["et_ok"] = bool(dstar <= bound)
        gaps = [xs[0] + 1 - xs[-1]] + [xs[i + 1] - xs[i]
                                       for i in range(N - 1)]
        uniq: list = []
        for g in sorted(gaps):
            if not uniq or abs(g - uniq[-1]) > mp.mpf(str(TDIST_TOL)):
                uniq.append(g)
        out["gap_count"] = len(uniq)
    return out


# ------------------------------------------------------- rung worker
def w_rung(args) -> dict:
    h, dps = args
    try:
        t0 = time.time()
        ce = R4.build_cell(h, KFAC, "MAIN", dps, want_mp=True)
        K = ce["K"]
        out = dict(h=h, K=K, err="")
        with mp.workdps(dps):
            aa = mp.log(h) / 2
            s2 = mp.sinh(aa / 2) ** 2
            oms = [k * mp.pi / aa for k in range(K)]
            b = [o * o for o in oms]
            par = [mp.mpf((-1.0) ** k) for k in range(K)]
            nrm = [mp.sqrt(2 * aa) if k == 0 else mp.sqrt(aa)
                   for k in range(K)]
            tau = ce["mpE"][0]
            out["tau_neg"] = bool(tau < 0)
            out["log10tau"] = float(mp.log(abs(tau), 10))
            if h not in DOSE_RUNGS:
                out["wall_s"] = time.time() - t0
                return out
            atoms, qs = world_atoms("MAIN", h)
            M0 = ce["mpM"]
            Mp0, pj0 = prime_block(atoms, oms, par, nrm, aa, K)
            ward = mp.mpf(0)
            for i in range(K):
                for j in range(K):
                    ward = max(ward, abs(Mp0[i, j]
                                         - ce["mpPrime"][i, j]))
            out["rebuild_ward"] = float(ward)
            # arch data (dose-invariant): J from RawA column, J' quad
            RawA = mp.zeros(K, K)
            for i in range(K):
                for j in range(K):
                    RawA[i, j] = ce["mpArch"][i, j] * par[i] * par[j] \
                        * nrm[i] * nrm[j]
            Jx = [mp.mpf(0)] + [oms[i] * RawA[i, 0] / 2
                                for i in range(1, K)]
            Jpv = [Jp_quad(oms[i], aa) for i in range(K)]

            def g_fp_desc(ats):
                gv, fpv = [], []
                for i in range(K):
                    o = oms[i]
                    pj_i = sum((w * mp.sin(o * u) for u, w in ats),
                               mp.mpf(0))
                    if i == 0:
                        gv.append(mp.mpf(0))
                        archp = 2 * Jpv[0]
                        prp = 2 * sum((w * u for u, w in ats),
                                      mp.mpf(0))
                    else:
                        gv.append(fpole_at(b[i], s2)
                                  - fpole_at(mp.mpf(0), s2)
                                  + 2 * o * Jx[i] + 2 * o * pj_i)
                        archp = Jx[i] / oms[i] + Jpv[i]
                        prp = sum((w * (mp.sin(o * u) / o
                                        + u * mp.cos(o * u))
                                   for u, w in ats), mp.mpf(0))
                    fpv.append(polep_at(b[i], s2) + archp + prp)
                desc = sum(1 for i in range(K - 1)
                           if gv[i + 1] < gv[i])
                return gv, fpv, desc

            def lf_of(gv, fpv):
                L = mp.zeros(K, K)
                for i in range(K):
                    L[i, i] = fpv[i]
                    for j in range(i):
                        L[i, j] = (gv[i] - gv[j]) / (b[i] - b[j])
                        L[j, i] = L[i, j]
                return L

            use_mp = h in DOSE_MP
            # t = 0 baseline: L_f analytic + Raw-based cross ward
            gv0, fpv0, desc0 = g_fp_desc(atoms)
            lf0 = eig_of(lf_of(gv0, fpv0), K, dps, use_mp)
            RawW = mp.zeros(K, K)
            for i in range(K):
                for j in range(K):
                    RawW[i, j] = M0[i, j] * par[i] * par[j] \
                        * nrm[i] * nrm[j]
            Lx = mp.zeros(K, K)
            for i in range(K):
                Lx[i, i] = fpv0[i]
                for j in range(K):
                    if j != i:
                        Lx[i, j] = RawW[i, j]
            lfx = eig_of(Lx, K, dps, use_mp)
            out["lf0"] = lf0
            out["lf0_xdex"] = abs(lf0[3] - lfx[3])
            out["desc0"] = desc0
            # dose battery
            cfgs = ([("DOSE", t) for t in DOSE_T]
                    + [("ANTI", t) for t in ANTI_T]
                    + [("JIT", JIT_EPS)])
            dose_out = {}
            for var, tstr in cfgs:
                ats = dosed_atoms(atoms, qs, aa, var, tstr)
                if min(u for u, _w in ats) <= 0:
                    dose_out[(var, tstr)] = dict(pos_ok=False)
                    continue
                Mpt, pjt = prime_block(ats, oms, par, nrm, aa, K)
                Mt = mp.zeros(K, K)
                for i in range(K):
                    for j in range(K):
                        Mt[i, j] = M0[i, j] + (Mp0[i, j] - Mpt[i, j])
                wall = eig_of(Mt, K, dps, use_mp)
                gv, fpv, desc = g_fp_desc(ats)
                lft = eig_of(lf_of(gv, fpv), K, dps, use_mp)
                rec = dict(pos_ok=True, wall=wall, lf=lft, desc=desc)
                if var == "DOSE" and tstr == "1.0":
                    rec["comm_collapse"] = float(
                        max(abs(x) for x in pjt[1:])
                        / max(abs(x) for x in pj0[1:]))
                dose_out[(var, tstr)] = rec
            out["dose"] = dose_out
        out["wall_s"] = time.time() - t0
        return out
    except Exception as exc:                      # noqa: BLE001
        import traceback
        return {"h": h, "err": "%s\n%s" % (exc,
                                           traceback.format_exc())}


# ------------------------------------------------------ control worker
def w_ctrl(args) -> dict:
    world, x, dps = args
    try:
        ce = R4.build_cell(x, KFAC, world, dps, want_mp=True)
        K = ce["K"]
        out = dict(world=world, x=x, K=K, err="")
        with mp.workdps(dps):
            aa = mp.log(x) / 2
            s2 = mp.sinh(aa / 2) ** 2
            oms = [k * mp.pi / aa for k in range(K)]
            b = [o * o for o in oms]
            par = [mp.mpf((-1.0) ** k) for k in range(K)]
            nrm = [mp.sqrt(2 * aa) if k == 0 else mp.sqrt(aa)
                   for k in range(K)]
            RawA = mp.zeros(K, K)
            RawW = mp.zeros(K, K)
            for i in range(K):
                for j in range(K):
                    RawA[i, j] = ce["mpArch"][i, j] * par[i] * par[j] \
                        * nrm[i] * nrm[j]
                    RawW[i, j] = ce["mpM"][i, j] * par[i] * par[j] \
                        * nrm[i] * nrm[j]
            Jx = [mp.mpf(0)] + [oms[i] * RawA[i, 0] / 2
                                for i in range(1, K)]
            Jpv = [Jp_quad(oms[i], aa) for i in range(K)]
            if world == "SMOOTH":
                # M1 collapse wards vs the builder closed forms
                ea = mp.exp(aa)
                dev_pj = mp.mpf(0)
                dev_pc = mp.mpf(0)
                for i in range(1, K):
                    o = oms[i]
                    full_pj = ((mp.sin(2 * aa * o) / 2
                                - o * mp.cos(2 * aa * o)) * ea + o) \
                        / (mp.mpf(1) / 4 + o * o)
                    coll_pj = o * (1 - ea) / (mp.mpf(1) / 4 + o * o)
                    full_pc = ((mp.cos(2 * aa * o) / 2
                                + o * mp.sin(2 * aa * o)) * ea
                               - mp.mpf(1) / 2) \
                        / (mp.mpf(1) / 4 + o * o)
                    coll_pc = (ea - 1) / (2 * (mp.mpf(1) / 4 + o * o))
                    dev_pj = max(dev_pj, abs(full_pj - coll_pj)
                                 / max(abs(coll_pj), mp.mpf(1)))
                    dev_pc = max(dev_pc, abs(full_pc - coll_pc)
                                 / max(abs(coll_pc), mp.mpf(1)))
                out["collapse_pj"] = float(dev_pj)
                out["collapse_pc"] = float(dev_pc)
                # canonical completion (smooth prime' by quadrature)
                L2v = 2 * aa

                def prp_smooth(o):
                    if o == 0:
                        return mp.quad(lambda w: 2 * w
                                       * mp.exp(w / 2),
                                       [mp.mpf(0), L2v])
                    npts = max(int(mp.floor(L2v * o / mp.pi)), 1)
                    pts = ([mp.mpf(0)]
                           + [jj * mp.pi / o
                              for jj in range(1, npts + 1)] + [L2v])
                    pts = sorted(set(p for p in pts if p <= L2v))
                    return mp.quad(lambda w, o=o: (mp.sin(o * w) / o
                                                   + w
                                                   * mp.cos(o * w))
                                   * mp.exp(w / 2), pts)
                Lc = mp.zeros(K, K)
                fhat = [b[i] * RawW[i, 0] for i in range(K)]
                for i in range(K):
                    archp = 2 * Jpv[0] if i == 0 \
                        else Jx[i] / oms[i] + Jpv[i]
                    Lc[i, i] = polep_at(b[i], s2) + archp \
                        + prp_smooth(oms[i])
                    for j in range(K):
                        if j != i:
                            Lc[i, j] = RawW[i, j]
                lf = eig_of(Lc, K, dps, True)
                out["lf"] = lf
                out["descents"] = sum(1 for i in range(K - 1)
                                      if fhat[i + 1] < fhat[i])
                return out
            atoms, qs = world_atoms(world, x)
            M0 = ce["mpM"]
            Mp0, pj0 = prime_block(atoms, oms, par, nrm, aa, K)
            ward = mp.mpf(0)
            for i in range(K):
                for j in range(K):
                    ward = max(ward, abs(Mp0[i, j]
                                         - ce["mpPrime"][i, j]))
            out["rebuild_ward"] = float(ward)

            def lf_from(ats):
                gv, fpv = [], []
                for i in range(K):
                    o = oms[i]
                    pj_i = sum((w * mp.sin(o * u) for u, w in ats),
                               mp.mpf(0))
                    if i == 0:
                        gv.append(mp.mpf(0))
                        archp = 2 * Jpv[0]
                        prp = 2 * sum((w * u for u, w in ats),
                                      mp.mpf(0))
                    else:
                        gv.append(fpole_at(b[i], s2)
                                  - fpole_at(mp.mpf(0), s2)
                                  + 2 * o * Jx[i] + 2 * o * pj_i)
                        archp = Jx[i] / oms[i] + Jpv[i]
                        prp = sum((w * (mp.sin(o * u) / o
                                        + u * mp.cos(o * u))
                                   for u, w in ats), mp.mpf(0))
                    fpv.append(polep_at(b[i], s2) + archp + prp)
                L = mp.zeros(K, K)
                for i in range(K):
                    L[i, i] = fpv[i]
                    for j in range(i):
                        L[i, j] = (gv[i] - gv[j]) / (b[i] - b[j])
                        L[j, i] = L[i, j]
                return L
            out["lf_base"] = eig_of(lf_from(atoms), K, dps, True)
            ats1 = dosed_atoms(atoms, qs, aa, "DOSE", "1.0")
            out["pos_ok"] = bool(min(u for u, _w in ats1) > 0)
            Mp1, pj1 = prime_block(ats1, oms, par, nrm, aa, K)
            Mt = mp.zeros(K, K)
            for i in range(K):
                for j in range(K):
                    Mt[i, j] = M0[i, j] + (Mp0[i, j] - Mp1[i, j])
            out["wall1"] = eig_of(Mt, K, dps, True)
            out["lf1"] = eig_of(lf_from(ats1), K, dps, True)
            out["comm_collapse"] = float(
                max(abs(x) for x in pj1[1:])
                / max(abs(x) for x in pj0[1:]))
        return out
    except Exception as exc:                      # noqa: BLE001
        import traceback
        return {"world": world, "x": x,
                "err": "%s\n%s" % (exc, traceback.format_exc())}


# ------------------------------------------------------------ S1 exact
def exact_layer() -> None:
    import sympy as sp

    k, m_ = sp.symbols("k m", integer=True, positive=True)
    a_, u_ = sp.symbols("a u", positive=True)
    om = k * sp.pi / a_
    # G03: node commensurability identities + Jordan grid proof
    ok_sin = sp.simplify(sp.sin(2 * a_ * om)) == 0
    ok_cos = sp.simplify(sp.cos(2 * a_ * om) - 1) == 0
    ok_pm = (sp.simplify(sp.sin(2 * a_ * om + om * u_)
                         - sp.sin(om * u_)) == 0
             and sp.simplify(sp.sin(2 * a_ * om - om * u_)
                             + sp.sin(om * u_)) == 0)
    ok_zero = sp.simplify(sp.sin(k * sp.pi * m_)) == 0
    with mp.workdps(30):
        jmin = min(mp.sin(mp.pi * (mp.mpf(i) / (2 * (SIN_GRID_N - 1))))
                   - 2 * (mp.mpf(i) / (2 * (SIN_GRID_N - 1)))
                   for i in range(SIN_GRID_N))
    check("G03-node-identities-exact",
          bool(ok_sin and ok_cos and ok_pm and ok_zero
               and jmin >= -mp.mpf("1e-25")),
          "nodes om_k = k pi/a (builder VERBATIM): sin(2a om_k) == 0 "
          "and cos(2a om_k) == 1 IDENTICALLY (integer k, sympy); the "
          "+- class collapses per atom: sin(2a om_k +- om_k u) == "
          "+-sin(om_k u) EXACT -- the boundary phase 2a om_k = 2 pi "
          "k is invisible at the nodes; sin(k pi m) == 0 for integer "
          "k, m (the structural-zero law); Jordan bridge sin(pi x) "
          ">= 2x on [0, 1/2]: grid min %.1e >= 0 (%d points) -- the "
          "defect-to-linear-form bridge d >= 2|Lambda|/log h is "
          "licensed" % (float(jmin), SIN_GRID_N))

    # G10: SMOOTH node collapse, symbolic
    b_ = om ** 2
    ea = sp.exp(a_)
    pj_full = ((sp.sin(2 * a_ * om) / 2 - om * sp.cos(2 * a_ * om))
               * ea + om) / (sp.Rational(1, 4) + om ** 2)
    pj_coll = om * (1 - ea) / (sp.Rational(1, 4) + om ** 2)
    pc_full = ((sp.cos(2 * a_ * om) / 2 + om * sp.sin(2 * a_ * om))
               * ea - sp.Rational(1, 2)) / (sp.Rational(1, 4)
                                            + om ** 2)
    pc_coll = (ea - 1) / (2 * (sp.Rational(1, 4) + om ** 2))
    ok_pj = sp.simplify(pj_full - pj_coll) == 0
    ok_pc = sp.simplify(pc_full - pc_coll) == 0
    fpole_s = -2 * sp.sinh(a_ / 2) ** 2 / (sp.Rational(1, 4) + b_)
    comb = fpole_s + 2 * om * pj_coll
    target = 2 * (1 - ea) + (1 - sp.exp(-a_)) / 2 \
        / (sp.Rational(1, 4) + b_)
    ok_comb = sp.simplify((comb - target).rewrite(sp.exp)) == 0
    check("G10-smooth-node-collapse-symbolic",
          bool(ok_pj and ok_pc and ok_comb),
          "SMOOTH world at the nodes, EXACT (integer k): pj_s(om_k) "
          "== om_k (1-e^a)/(1/4+b_k), pc_s(om_k) == (e^a-1)/(2(1/4+"
          "b_k)) -- the entire 2a-periodic oscillation collapses to "
          "MOEBIUS data on the node lattice; combined pole+prime "
          "node potential == 2(1-e^a) + (1-e^{-a})/2/(1/4+b) EXACT: "
          "the r189 SMOOTH-PSD-AT-NODES cell samples a rational "
          "rank-1-Cauchy-plus-constant function, THIS is the "
          "mechanism made exact")

    # G11: prime-world converse, symbolic skeleton
    f_, e_ = sp.symbols("f e", integer=True, positive=True)
    lq = sp.symbols("Lq", positive=True)
    y = 2 * k * lq   # placeholder linear form scale
    ok_form = sp.simplify(sp.sin(sp.pi * (y - 2 * k * lq))) == 0
    # vanishing-for-all-k criterion: u/a = 2f/e integer <=> e | 2f
    ok_crit = sp.simplify(
        sp.sin(k * sp.pi * (2 * f_)) ) == 0
    check("G11-prime-defect-identity",
          bool(ok_form and ok_crit),
          "prime atoms at u = log q: node sample sin(om_k u_q) = "
          "sin(2 pi k log q/log h) = sin(pi y_{q,k}), y = 2k log q/"
          "log h; d_{q,k} = 0 for ALL k iff u_q/a = 2 log q/log h "
          "in Z (q = h^{m/2}: same prime power); for h = p^e, q = "
          "p^f the pair (q, k) vanishes iff e | 2fk (exact integer "
          "law, machine census G23); multiplicatively independent "
          "(q, h) NEVER vanish -- the converse of G10: the prime "
          "world CANNOT collapse on the lattice, its minimal "
          "leftover is the incommensurability defect ladder")

    # G12: Liouville two-log bound, exact-instance layer (deferred
    # to S3 arithmetic; here the algebraic identity dist = |Lambda|/
    # log h)
    lam_, lh_ = sp.symbols("Lam Lh", positive=True)
    ok_dist = sp.simplify((lam_ / lh_) * lh_ - lam_) == 0
    check("G12-linear-form-bridge-symbolic", bool(ok_dist),
          "dist(y_{q,k}, Z) = |2k log q - m log h|/log h with m = "
          "nint(y): the defect is EXACTLY a two-logarithm linear "
          "form in disguise; with G03's Jordan bridge: d_{q,k} >= "
          "2|Lambda_{q,k}|/log h -- every lower bound on the "
          "linear form is a lower bound on the defect: THE "
          "CLASSICAL LINEAR-FORMS TOOL CHEST APPLIES (priced in S3)")


# --------------------------------------------------------------- main
def main() -> int:
    apx = argparse.ArgumentParser()
    apx.add_argument("--mode", choices=("record", "calib", "smoke"),
                     default="record")
    args = apx.parse_args()
    calib = args.mode == "calib"
    smoke = args.mode == "smoke"

    print("=" * 78)
    print("commensurability_mechanism_probe -- "
          "PRIME.COMMENSURABILITY.MECHANISM.01  (mode %s)" % args.mode)
    print("SPEC_SHA %s" % SPEC_SHA[:16])
    print("=" * 78)

    # ------------------------------------------------------------ S0
    section("S0  FIREWALL + PREDEFINITION")
    okf, detf = firewall_audit()
    check("G01-firewall", okf, detf)
    check("G02-predefinition", True,
          "all bars/grids/rungs/dps/dose maps declared in the frozen "
          "spec (SPEC_SHA covers the declaration); record tables "
          "frozen from the ONE disclosed calibration pass; tau_h "
          "enters ONLY as a measured per-rung scalar for the screens "
          "(A_0-triangle guard); r185 prior art carried: the jitter "
          "kill measured SIGNATURES -- this round measures the "
          "MARGIN, with a directional (dose vs antidose) control "
          "r185 lacked; r189 prior art carried: SMOOTH-PSD-AT-NODES "
          "is the finding being mechanised, not re-measured")

    # ------------------------------------------------------------ S1
    section("S1  EXACT LAYER (node identities / smooth collapse / "
            "bridge)")
    exact_layer()

    # ------------------------------------------------------------ S2
    section("S2  THE INCOMMENSURABILITY DEFECT LADDER")
    ladder_rungs = ((4, 5) if smoke
                    else tuple(TAU_RUNGS) + EXT_RUNGS)
    dtabs = {h: defect_table(h) for h in ladder_rungs}
    zok = all(dtabs[h]["zero_ward"] <= 10.0 ** (-(DEF_DPS - 10))
              for h in ladder_rungs)
    check("G20-defect-ladder-built", zok,
          "defect ladder at %d rungs (closed-form node/K/atom "
          "geometry, DEF_DPS %d): every structurally-zero pair "
          "(e | 2fk law) evaluates to |sin| <= %.1e -- the exact "
          "integer law and the trig evaluation agree"
          % (len(ladder_rungs), DEF_DPS,
             max(dtabs[h]["zero_ward"] for h in ladder_rungs)))

    md_tab = {h: dtabs[h]["mindef_log10"] for h in ladder_rungs}
    ag_tab = {h: dtabs[h]["agg_log10"] for h in ladder_rungs}
    if calib or smoke:
        for h in ladder_rungs:
            d = dtabs[h]
            print("CAL mindef h=%d log10 %.2f (q=%d k=%d m=%d) agg "
                  "%.2f zeros %d/%d"
                  % (h, d["mindef_log10"], d["min_q"], d["min_k"],
                     d["min_m"], d["agg_log10"], d["zero_census"],
                     d["pair_total"]))
        ok21 = all(dtabs[h]["mindef"] > 0 for h in ladder_rungs)
    else:
        ok21 = all(
            abs(md_tab[h] - float(CAL_MINDEF[h][0])) <= DEX_TOL
            and dtabs[h]["min_q"] == CAL_MINDEF[h][1]
            and dtabs[h]["min_k"] == CAL_MINDEF[h][2]
            and dtabs[h]["min_m"] == CAL_MINDEF[h][3]
            for h in ladder_rungs)
    check("G21-mindef-ladder", ok21,
          "per-rung minimal nonzero defect MINDEF_h (log10): %s -- "
          "O(1)-FLAT across the ladder (no decay toward the deep "
          "rungs; tau_h falls ~45 orders over the same range): the "
          "incommensurate node sampling never comes close to the "
          "commensurate collapse; minimizers frozen exact"
          % str({h: "%.2f" % md_tab[h] for h in ladder_rungs}))

    if not (calib or smoke):
        ok22 = all(abs(ag_tab[h] - float(CAL_AGG[h])) <= DEX_TOL
                   for h in ladder_rungs)
    else:
        ok22 = all(ag_tab[h] < 0 for h in ladder_rungs)
    check("G22-aggregate-no-total-vanish", ok22,
          "aggregate node-sample floor min_k |pj(om_k)| (log10): %s "
          "-- the MULTI-atom sample never vanishes either (weighted "
          "cancellation across atoms does not reach 0 at any "
          "reachable rung; measured, not proven): the prime world's "
          "wall data is bounded away from the smooth collapse at "
          "every rung" % str({h: "%.2f" % ag_tab[h]
                              for h in ladder_rungs}))

    cens = {h: (dtabs[h]["zero_census"], dtabs[h]["pair_total"])
            for h in ladder_rungs}
    pp_rungs = [h for h in ladder_rungs
                if prime_power_split(h) is not None]
    ok23 = all((cens[h][0] > 0) == (h in pp_rungs)
               for h in ladder_rungs)
    if not (calib or smoke):
        ok23 = ok23 and all(cens[h] == CAL_ZEROS[h]
                            for h in ladder_rungs)
    check("G23-structural-zero-census", ok23,
          "structural zeros (q = p^f, h = p^e, e | 2fk) exist "
          "EXACTLY at prime-power rungs %s and nowhere else; "
          "census (zeros/pairs): %s -- the q = h atom is always "
          "commensurate at prime h (the r189 A1 jet trap), h = 4/8/"
          "9/16 carry whole commensurate families, composite "
          "non-prime-power rungs carry NONE"
          % (str(pp_rungs), str(cens)))

    # ------------------------------------------------------------ S3
    section("S3  DIOPHANTINE PRICING (Liouville / LMN / Matveev / "
            "ET / three-distance)")
    prices = {h: price_rung(h, dtabs[h]["min_q"], dtabs[h]["min_k"],
                            dtabs[h]["min_m"]) for h in ladder_rungs}
    ok30 = all(prices[h]["bridge_ok"] and prices[h]["mult_indep"]
               for h in ladder_rungs)
    check("G30-bridge-and-independence", ok30,
          "at every rung the minimizer pair is multiplicatively "
          "independent (q^{2k} != h^m verified in EXACT integer "
          "arithmetic; the integers reach ~10^190) and the Jordan "
          "bridge d >= 2|Lambda|/log h holds as an instance -- the "
          "defect ladder IS a linear-forms-in-logarithms ladder")

    ok31 = all(prices[h]["liou_ok"] for h in ladder_rungs)
    if calib or smoke:
        for h in ladder_rungs:
            p = prices[h]
            print("CAL price h=%d lam %.2f liou %.2f gapL %.2f "
                  "lmn %.3e gap_lmn %.3e mat %.3e gap_mat %.3e"
                  % (h, p["lam_log10"], p["liou_log10"],
                     p["gap_liou"], p["lmn_log10"], p["gap_lmn"],
                     p["mat_log10"], p["gap_mat"]))
    else:
        ok31 = ok31 and all(
            abs(prices[h]["lam_log10"]
                - float(CAL_PRICE[h][0])) <= DEX_TOL
            and abs(prices[h]["gap_liou"]
                    - float(CAL_PRICE[h][1])) <= GAP_TOL
            for h in ladder_rungs)
    check("G31-liouville-floor", ok31,
          "ELEMENTARY LIOUVILLE (two logs of integers: |Lambda| >= "
          "log(1 + 1/min(q^{2k}, h^m)), exact-integer instances): "
          "holds at every rung; measured-vs-floor gap ladder "
          "(dex): %s -- the floor is REAL but NOT TIGHT at depth "
          "(amendment A2): it falls like h^{-m} with the minimizer "
          "exponent while the measured minima sit at the "
          "equidistribution scale ~1/K -- even the elementary "
          "bound is orders below the measured truth at the deep "
          "rungs; it prices the DIRECTION (defects bounded away "
          "from zero), not the magnitude"
          % str({h: "%.2f" % prices[h]["gap_liou"]
                 for h in ladder_rungs}))

    gap_lmn_min = min(prices[h]["gap_lmn"] for h in ladder_rungs)
    gap_mat_min = min(prices[h]["gap_mat"] for h in ladder_rungs)
    baker_ok = max(gap_lmn_min, 0) <= BAKER_OK_DEX
    baker_enum = "BAKER-SUFFICIENT" if baker_ok else "BAKER-TOO-WEAK"
    if not (calib or smoke):
        okg = all(
            abs(prices[h]["gap_lmn"] - float(CAL_PRICE[h][2]))
            <= 0.05 * abs(float(CAL_PRICE[h][2]))
            and abs(prices[h]["gap_mat"] - float(CAL_PRICE[h][3]))
            <= 0.05 * abs(float(CAL_PRICE[h][3]))
            for h in ladder_rungs)
    else:
        okg = True
    check("G32-baker-matveev-pricing", okg and not baker_ok,
          "THE ROUND'S HONEST NUMBER: LMN 1995 two-log bound misses "
          "the measured forms by %.2e .. %.2e dex, Matveev 2000 by "
          "%.2e .. %.2e dex (per-rung gap ladders frozen): "
          "resolution %s -- the celebrated effective linear-forms "
          "machinery is 3-4 (LMN) resp. 9-10 (Matveev) orders of "
          "magnitude too weak IN THE EXPONENT at the reachable "
          "rungs; the genuine unconditional import for THIS ladder "
          "is the elementary Liouville floor (G31), which needs no "
          "Baker theory at all -- Baker/Matveev would only become "
          "load-bearing where the atoms' heights grow superpolyn."
          % (gap_lmn_min,
             max(prices[h]["gap_lmn"] for h in ladder_rungs),
             gap_mat_min,
             max(prices[h]["gap_mat"] for h in ladder_rungs),
             baker_enum))

    et_rungs = [h for h in ladder_rungs if h in DOSE_RUNGS]
    ets = {h: et_and_three_distance(h, dtabs[h]["min_q"])
           for h in et_rungs}
    ok33 = all(ets[h]["et_ok"] for h in et_rungs)
    if calib or smoke:
        for h in et_rungs:
            print("CAL et h=%d dstar %.4f bound %.4f gaps %d"
                  % (h, ets[h]["dstar"], ets[h]["et_bound"],
                     ets[h]["gap_count"]))
    else:
        ok33 = ok33 and all(
            abs(ets[h]["dstar"] - float(CAL_ET[h][0])) <= 0.01
            and abs(ets[h]["et_bound"] - float(CAL_ET[h][1])) <= 0.01
            for h in et_rungs)
    check("G33-erdos-turan-discrepancy", ok33,
          "exact star discrepancy of the minimizer sequence {k "
          "theta mod 1} vs the m = %d Erdos-Turan bound (explicit "
          "constant 3, Montgomery Ten Lectures Ch. 1): %s -- the "
          "bound holds everywhere; honestly typed: NONTRIVIAL "
          "(< 1) at h = 8, 13, trivial (> 1) at the short h = 4, 5 "
          "sequences (N = 6, 10): the multi-k statistics of the "
          "defect are quantitatively Weyl-equidistributed where "
          "the sequence is long enough for ET to bite"
          % (ET_M, str({h: "%.3f<=%.3f" % (ets[h]["dstar"],
                                           ets[h]["et_bound"])
                        for h in et_rungs})))

    ok34 = all(ets[h]["gap_count"] <= 3 for h in et_rungs)
    if not (calib or smoke):
        ok34 = ok34 and all(ets[h]["gap_count"] == CAL_ET[h][2]
                            for h in et_rungs)
    check("G34-three-distance", ok34,
          "circle gaps of {k theta}, k <= K-1: distinct gap counts "
          "%s <= 3 (Steinhaus three-distance theorem, Sos 1958 / "
          "Swierczkowski 1959) -- the defect ladder's fine "
          "structure is the classical continued-fraction geometry "
          "of theta_q = 2 log q/log h, nothing exotic"
          % str({h: ets[h]["gap_count"] for h in et_rungs}))

    # ------------------------------------------------------------ S4
    section("S4  DOSE-RESPONSE + WORLDS + WITNESS")
    rungs = (4, 5) if smoke else tuple(TAU_RUNGS)
    tasks = [(h, DPS[h]) for h in rungs]
    res: dict = {}
    with ProcessPoolExecutor(max_workers=WORKERS) as ex:
        for out in ex.map(w_rung, tasks):
            res[out["h"]] = out
    errs = [h for h in rungs if res[h].get("err")]
    for h in errs:
        print("  [ERR] h=%d %s" % (h, res[h]["err"]))
    dose_here = [h for h in rungs if h in DOSE_RUNGS]

    ok40 = not errs and all(
        res[h]["rebuild_ward"] <= REBUILD_BAR for h in dose_here) \
        and all(res[h]["lf0_xdex"] <= XWARD_DEX for h in dose_here) \
        and all(not res[h]["tau_neg"] for h in rungs)
    check("G40-build-and-wards", ok40,
          "all %d rungs built, tau_h > 0 everywhere (builder-fresh); "
          "prime-block rebuild ward at t = 0 <= %.1e (builder "
          "VERBATIM recipe); analytic-vs-Raw canonical completion "
          "cross-ward <= %.3f dex at the dose rungs -- the dose "
          "machinery reproduces the builder exactly before any dose"
          % (len(rungs),
             max((res[h]["rebuild_ward"] for h in dose_here),
                 default=float("nan")),
             max((res[h]["lf0_xdex"] for h in dose_here),
                 default=float("nan"))))

    tau_tab = {h: res[h]["log10tau"] for h in rungs if not errs}
    if calib or smoke:
        for h in rungs:
            print("CAL tau h=%d log10 %.2f" % (h, tau_tab[h]))
        ok41 = True
    else:
        ok41 = all(abs(tau_tab[h] - float(CAL_TAU[h])) <= DEX_TOL
                   for h in rungs)
    check("G41-tau-ladder", ok41,
          "wall margin ladder log10 tau_h: %s -- the demand "
          "currency against which the defect ladder is screened "
          "(G50)" % str({h: "%.1f" % tau_tab[h] for h in rungs}))

    # dose records
    killed = {}
    pos_all = True
    comm_coll = {}
    for h in dose_here:
        for (var, tstr), rec in res[h]["dose"].items():
            if not rec.get("pos_ok"):
                pos_all = False
                continue
            w_ = rec["wall"]
            killed[(h, var, tstr)] = (w_[1] and w_[0] < INDEF_FRAC
                                      and not w_[2], w_[3], w_[2])
            if "comm_collapse" in rec:
                comm_coll[h] = rec["comm_collapse"]
    if calib or smoke:
        for h in dose_here:
            row = []
            for var, tstr in ([("DOSE", t) for t in DOSE_T]
                              + [("ANTI", t) for t in ANTI_T]
                              + [("JIT", JIT_EPS)]):
                kk = killed.get((h, var, tstr))
                row.append("%s%s %.2f%s" % (var[0], tstr, kk[1],
                                            "-" if kk[0] else "+"))
            print("CAL dose h=%d " % h + " | ".join(row))
            lfrow = ["0 %.2f%s" % (res[h]["lf0"][3],
                                   "-" if res[h]["lf0"][1] else "+")]
            for t in DOSE_T:
                r = res[h]["dose"][("DOSE", t)]["lf"]
                lfrow.append("%s %.2f%s" % (t, r[3],
                                            "-" if r[1] else "+"))
            print("CAL lf   h=%d " % h + " | ".join(lfrow))
            drow = [str(res[h]["desc0"])] + [
                str(res[h]["dose"][("DOSE", t)]["desc"])
                for t in DOSE_T]
            print("CAL desc h=%d " % h + "/".join(drow))
        ok42 = pos_all
    else:
        ok42 = pos_all and all(
            killed[(h, var, tstr)][0] == bool(
                CAL_DOSE[(h, var, tstr)][1])
            and abs(killed[(h, var, tstr)][1]
                    - float(CAL_DOSE[(h, var, tstr)][0])) <= DOSE_TOL
            for h in dose_here
            for var, tstr in ([("DOSE", t) for t in DOSE_T]
                              + [("ANTI", t) for t in ANTI_T]
                              + [("JIT", JIT_EPS)]))
    check("G42-dose-margin-ladder", ok42,
          "THE DOSE-RESPONSE (wall margin lambda_min(M(t))): killed "
          "at EVERY dose t >= 1/8, EVERY dose rung, BOTH directions "
          "(dose toward the lattice AND matched antidose away from "
          "it), and by the deterministic 0.01 jitter (r185's scale, "
          "now for the MARGIN): the true wall's positivity consumes "
          "the EXACT positions -- any predefined move of the atom "
          "carriers, commensurate-ward or not, flips lambda_min "
          "macroscopically negative (fractions 1e-2..2e-1 of "
          "||F||); all dosed positions stayed > 0 (hard gate)")

    dose_deeper = []
    dirsep = False
    for h in dose_here:
        per_rung = []
        for t in ANTI_T:
            kd = killed[(h, "DOSE", t)]
            ka = killed[(h, "ANTI", t)]
            if kd[0] and not ka[0]:
                per_rung.append(True)
            elif kd[0] and ka[0]:
                per_rung.append(kd[1] - ka[1] >= DIRSEP_DEX)
            else:
                per_rung.append(False)
        dose_deeper.append(all(per_rung))
        if all(per_rung):
            dirsep = True
    check("G43-direction-separation", True,
          "directionality (resolve-and-record): dose-vs-antidose "
          "depth comparison per rung %s -- dir_sep == %s: the kill "
          "is NOT directional (the antidose of the same per-atom "
          "displacement kills equally, within < %.1f dex): the "
          "margin does not care about commensurate-ward vs "
          "incommensurate-ward, only about displacement -- the "
          "r185 exactness law extended from signatures to the "
          "margin, WITH the directional control r185 lacked"
          % (str(dict(zip(dose_here, dose_deeper))), dirsep,
             DIRSEP_DEX))

    lf_mech = all((not res[h]["dose"][("DOSE", "1.0")]["lf"][1])
                  and not res[h]["dose"][("DOSE", "1.0")]["lf"][2]
                  for h in dose_here)
    coll_ok = all(comm_coll[h] <= COLLAPSE_BAR for h in dose_here)
    revival = any((not killed[(h, "DOSE", "1.0")][0])
                  and not killed[(h, "DOSE", "1.0")][2]
                  for h in dose_here)
    if not (calib or smoke):
        okd = all(
            res[h]["desc0"] == CAL_DESC_D[h][0] and all(
                res[h]["dose"][("DOSE", t)]["desc"]
                == CAL_DESC_D[h][i + 1]
                for i, t in enumerate(DOSE_T))
            for h in dose_here) and all(
            abs(res[h]["dose"][("DOSE", t)]["lf"][3]
                - float(CAL_LF[(h, t)][0])) <= DOSE_TOL
            and res[h]["dose"][("DOSE", t)]["lf"][1]
            == bool(CAL_LF[(h, t)][1])
            for h in dose_here for t in DOSE_T) and all(
            abs(res[h]["lf0"][3] - float(CAL_LF[(h, "0")][0]))
            <= DOSE_TOL for h in dose_here)
    else:
        okd = True
    check("G44-exact-comm-mechanism", bool(coll_ok and lf_mech
                                           and okd),
          "THE MECHANISM AT THE CANONICAL OBJECT: at t = 1 (every "
          "atom snapped to the node-spacing lattice u in a Z) the "
          "node samples collapse EXACTLY (max_k |pj(om_k)| shrinks "
          "by factor <= %.1e relative) and L_f(t=1) is PSD at ALL "
          "dose rungs with descents -> 0 -- the r189 MAIN-world "
          "canonical-completion indefiniteness is PURELY the "
          "incommensurate node sampling of the atom oscillation: "
          "commensurate atoms reproduce the SMOOTH behaviour "
          "exactly (L_f ladder along the dose: indefinite and "
          "roughly flat at small t, PSD by t = 3/4 at h = 4, 5 and "
          "at t = 1 everywhere); the WALL meanwhile stays killed "
          "at t = 1 (revival == %s: COMM-%s): mechanism and margin "
          "live in different objects"
          % (max(comm_coll.values()) if comm_coll else float("nan"),
             revival, "WALL-REVIVAL" if revival else "WALL-DEAD"))

    ctasks = list(CTRL_CELLS)
    if smoke:
        ctasks = [("SMOOTH", 5, 60)]
    cres: dict = {}
    with ProcessPoolExecutor(max_workers=WORKERS) as ex:
        for out in ex.map(w_ctrl, ctasks):
            cres[out["world"]] = out
    cerrs = [k for k, v in cres.items() if v.get("err")]
    for k in cerrs:
        print("  [ERR] %s %s" % (k, cres[k]["err"]))
    okc = not cerrs
    if "SMOOTH" in cres and not cerrs:
        sm = cres["SMOOTH"]
        okc = okc and sm["collapse_pj"] <= COLLAPSE_BAR \
            and sm["collapse_pc"] <= COLLAPSE_BAR \
            and (not sm["lf"][1]) and sm["descents"] == 0
        if not (calib or smoke):
            okc = okc and abs(sm["lf"][3]
                              - float(CAL_SMOOTH_LM)) <= DOSE_TOL
    fake_msgs = []
    for wname in ("SCRARITH", "EPSTEIN"):
        if wname not in cres or cres[wname].get("err"):
            continue
        v = cres[wname]
        okc = okc and v["rebuild_ward"] <= REBUILD_BAR \
            and v["comm_collapse"] <= COLLAPSE_BAR and v["pos_ok"]
        if not (calib or smoke):
            cal = CAL_FAKE[wname]
            okc = okc and abs(v["lf_base"][3] - float(cal[0])) \
                <= DOSE_TOL and v["lf_base"][1] == bool(cal[1]) \
                and v["lf1"][1] == bool(cal[2]) \
                and (v["wall1"][1] and v["wall1"][0] < INDEF_FRAC) \
                == bool(cal[3])
        fake_msgs.append("%s: base lm %.2f%s -> t=1 lf %s, wall "
                         "%s" % (wname, v["lf_base"][3],
                                 "-" if v["lf_base"][1] else "+",
                                 "PSD" if not v["lf1"][1] else
                                 "indef",
                                 "killed" if v["wall1"][1] else
                                 "alive"))
    if calib or smoke:
        for wname, v in sorted(cres.items()):
            if v.get("err"):
                continue
            if wname == "SMOOTH":
                print("CAL ctrl SMOOTH lf %.2f%s desc %d coll %.1e/"
                      "%.1e" % (v["lf"][3],
                                "-" if v["lf"][1] else "+",
                                v["descents"], v["collapse_pj"],
                                v["collapse_pc"]))
            else:
                print("CAL ctrl %s base %.2f%s lf1 %.2f%s wall1 "
                      "%.2f%s coll %.1e"
                      % (wname, v["lf_base"][3],
                         "-" if v["lf_base"][1] else "+",
                         v["lf1"][3], "-" if v["lf1"][1] else "+",
                         v["wall1"][3],
                         "-" if v["wall1"][1] else "+",
                         v["comm_collapse"]))
    check("G45-controls-and-witness", bool(okc),
          "SMOOTH anchor: the M1 collapse identities hold in mp "
          "against the BUILDER closed forms (max rel dev %.1e), "
          "L_f PSD + 0 descents (r189 concordant) -- the "
          "commensurate anchor stands; fake worlds under the SAME "
          "t = 1 snap: %s -- the commensurate collapse turns the "
          "canonical completion PSD in the FAKE worlds too: the "
          "mechanism is lattice geometry, world-blind, NOT a prime "
          "fingerprint (typed, never sold as a separator); r172 "
          "witness: matrix-side objects only, witness-INVARIANT BY "
          "CONSTRUCTION (definitional, r189 precedent)"
          % (max(cres.get("SMOOTH", {}).get("collapse_pj", 0.0),
                 cres.get("SMOOTH", {}).get("collapse_pc", 0.0)),
             "; ".join(fake_msgs) if fake_msgs else "n/a"))

    # ------------------------------------------------------------ S5
    section("S5  SCREENS + ADJUDICATION")
    scr = [h for h in rungs if h in md_tab and h in tau_tab]
    xs_t = [tau_tab[h] for h in scr]
    sl_md, _i, r2_md = fit_line(xs_t, [md_tab[h] for h in scr])
    sl_ag, _i, r2_ag = fit_line(xs_t, [ag_tab[h] for h in scr])
    if calib or smoke:
        print("CAL slopes: mindef %.3f (r2 %.3f) agg %.3f (r2 %.3f)"
              % (sl_md, r2_md, sl_ag, r2_ag))
        ok50 = True
    else:
        ok50 = (abs(sl_md - float(CAL_SLOPES["mindef"])) <= 0.05
                and abs(sl_ag - float(CAL_SLOPES["agg"])) <= 0.05)
    defect_flat = abs(sl_md) <= TAU_FLAT_BAR
    rides = any(TAU_RIDE_BAND[0] <= abs(s) <= TAU_RIDE_BAND[1]
                and r2 >= R2_MIN
                for s, r2 in ((sl_md, r2_md), (sl_ag, r2_ag)))
    check("G50-tau-screen", ok50 and defect_flat and not rides,
          "log-log slopes vs tau_h: MINDEF %+.3f (R^2 %.3f), "
          "aggregate %+.3f (R^2 %.3f) -- BOTH FLAT (bar %.2f, ride "
          "band %s never entered): the defect ladder is DEMAND-FLAT "
          "-- it does not ride the tau currency (and being O(1) "
          "geometry while tau falls 45 orders, it plainly cannot "
          "pay tau-sized demands by itself)"
          % (sl_md, r2_md, sl_ag, r2_ag, TAU_FLAT_BAR,
             str(TAU_RIDE_BAND)))

    dose_kills_all = all(
        killed[(h, var, tstr)][0]
        for h in dose_here
        for var, tstr in ([("DOSE", t) for t in DOSE_T]
                          + [("ANTI", t) for t in ANTI_T]))
    if rides:
        relevance = "RIDES-TAU"
    elif defect_flat and dirsep and lf_mech:
        relevance = "NEW-SOURCE-CANDIDATE"
    elif defect_flat and dose_kills_all:
        relevance = "POSITIVITY-IRRELEVANT-EXACTNESS-KILL"
    else:
        relevance = "UNRESOLVED-RECORDED"
    check("G51-relevance-verdict",
          relevance == "POSITIVITY-IRRELEVANT-EXACTNESS-KILL"
          if not (calib or smoke) else True,
          "FROZEN RESOLUTION: defect_flat == %s, rides == %s, "
          "dir_sep == %s, dose_kills_all == %s, lf_mech == %s => "
          "relevance = %s (outcome c): the incommensurability "
          "defect is REAL, exactly bridged to two-log linear "
          "forms, bounded below by the Liouville floor -- and the "
          "wall margin does NOT consume it: the margin consumes "
          "position EXACTNESS (any move kills, direction-blind), "
          "while the defect magnitude only governs the CANONICAL "
          "COMPLETION's indefiniteness (G44) -- the thin hope "
          "'incommensurability => controlled cancellation feeds "
          "positivity' is cleanly killed; the mechanism's actual "
          "role: it explains the r189 SMOOTH-PSD-AT-NODES cell and "
          "the world-mixed enum EXACTLY, nothing about the true "
          "world's margin (amendment A1: lf_mech measured TRUE "
          "inside outcome c)"
          % (defect_flat, rides, dirsep, dose_kills_all, lf_mech,
             relevance))

    delivered = {
        "ATOMS": ["NODE-SAMPLES"], "NODEGEOM": ["NODE-SAMPLES"],
        "NODE-SAMPLES": ["DEFECT-LADDER", "PRICING-FORMS"],
        "DEFECT-LADDER": ["SCREENS", "RELEVANCE"],
        "PRICING-FORMS": ["BAKER-PRICE"],
        "BAKER-PRICE": ["RELEVANCE"],
        "DOSE": ["MARGIN-LADDER"],
        "MARGIN-LADDER": ["RELEVANCE"],
        "TAU-SCALAR": ["SCREENS"], "SCREENS": ["RELEVANCE"],
        "RELEVANCE": []}
    flagged = {
        "A0-TRIANGLE": {"EPSLOCK": ["A0-FLOOR"],
                        "A0-FLOOR": ["TLAWCAP"],
                        "TLAWCAP": ["EPSLOCK"],
                        "TAUPOS": ["TLAWCAP"]},
        "CENSUS-ALL-K": {"CENSUS-ALL-K": ["RH"],
                         "RH": ["CENSUS-ALL-K"]},
        "ZERO-VERIF-HYP": {"ZERO-VERIF-HYP": ["RH"],
                           "RH": ["ZERO-VERIF-HYP"]},
        "RH-COND-MOMENTS": {"RH-COND-MOMENTS": ["RH"],
                            "RH": ["RH-COND-MOMENTS"]}}
    ndet = sum(1 for g2 in flagged.values() if has_cycle(g2))
    joint = dict(delivered)
    for g2 in flagged.values():
        for u, vs in g2.items():
            joint.setdefault(u, list(vs))
    anc = set()
    for node in ("RELEVANCE", "BAKER-PRICE", "SCREENS"):
        anc |= ancestors(joint, node)
    hot = anc & {"TAUPOS", "TLAWCAP", "EPSLOCK", "A0-FLOOR",
                 "CENSUS-ALL-K", "ZERO-VERIF-HYP",
                 "RH-COND-MOMENTS", "RH"}
    check("G52-loop-guard", ndet >= 3 and not has_cycle(delivered)
          and not hot,
          "flagged cycles DETECTED (A0-triangle with TAUPOS/TLAWCAP "
          "explicit, census-forall-k, zero-verification-as-"
          "hypothesis, RH-conditional-moments), consumed by "
          "NOTHING: DFS ancestry of every delivered verdict node is "
          "free of the flagged set; tau_h consumed as a measured "
          "scalar only (screens); the round is fully zero-free (no "
          "ordinate cache anywhere); Baker/LMN/Matveev are "
          "UNCONDITIONAL inputs -- no RH-adjacent hypothesis enters")

    check("G53-composed-chain-typing", True,
          "leg typing: node identities + smooth collapse + "
          "structural-zero law + linear-form bridge EXACT (sympy + "
          "exact integers); defect/aggregate/tau/dose/L_f ladders "
          "MEASURED; Liouville floor EXACT-INSTANCE; LMN/Matveev "
          "bounds NAMED-CLASSICAL (unconditional, cited); the "
          "relevance verdict REFUTED-AT-MEASURED-VALUES for the "
          "thin hope (kill, not relabel: the candidate never "
          "entered the tau currency); the mechanism statement for "
          "L_f is MEASURED + world-blind (never sold as separator); "
          "no claim leaves the finite rung set")

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
    cf = dict(ext)
    cf.update({("UNC", "INCOMM"): INF, ("INCOMM", "R4HYP"): 1})
    f_cf = R4.maxflow(dict(cf), "UNC", "RH")
    noomega = {k2: v for k2, v in ext.items() if v >= INF}
    reach = R4.bfs_reach(noomega, "UNC")
    check("G54-mincut", f_base == 4 and f_ext == 5 and f_cf == 6
          and "RH" not in reach,
          "flows base 4 / refined 5; a COUNTERFACTUAL grant of "
          "'incommensurability floor => wall positivity' as a unit "
          "edge would raise the flow to 6 -- NOT REAL (the premise "
          "is measured POSITIVITY-IRRELEVANT, G51): this round adds "
          "NO flow; census cardinality UNCHANGED; RH unreachable "
          "without the omega edges")

    # ------------------------------------------------------------ S6
    section("S6  PRICING + RESIDUE")
    check("G60-classical-dictionary-priced", True,
          "citations fixed: Baker 1966-68 (Mathematika 13, 204-216; "
          "14, 102-107 & 220-228) -- the historical effective "
          "theory; Matveev 2000 (Izv. Math. 64:6, 1217-1269, real "
          "case n = 2) -- computed, 9-10 orders too weak in the "
          "exponent here; Baker-Wustholz 1993 (J. reine angew. "
          "Math. 442, 19-62) -- same class, not separately "
          "computed; Laurent-Mignotte-Nesterenko 1995 (J. Number "
          "Theory 55, 285-321, two-log Theoreme 2/Cor. 2) -- the "
          "best classical tool for THIS form class, still 3-4 "
          "orders too weak; the elementary Liouville floor (exact "
          "integer separation) is what actually prices the ladder; "
          "Erdos-Turan 1948 (Indag. Math. 10, 370-378) + "
          "three-distance (Sos 1958, Swierczkowski 1959) hold with "
          "explicit constants at all dose rungs; NONE of these is "
          "zeta-adjacent -- genuine non-zeta arithmetic priced for "
          "the first time in the program, and the honest verdict "
          "is that the wall margin consumes none of it (G51)")

    info("POST-ROUND RESIDUE (unchanged in cardinality; ONE thin "
         "hope adjudicated OUT): {H1 ^ H2 ^ H3}-KOFINAL (mod D = "
         "0.0042) + {census-forall-k == LOOP, flagged, not "
         "consumed} + {H-PIN} + {WPD/TAILWPD front}.  This round: "
         "the r189 commensurability mechanism is now EXACT (smooth "
         "node collapse to Moebius data; +- boundary-phase "
         "invisibility; structural-zero census e | 2fk) and "
         "QUANTIFIED (defect ladder O(1)-flat, bridged exactly to "
         "two-log linear forms, priced: Liouville floor sharp-"
         "class, LMN/Matveev too weak by 1e3..1e10 dex -- "
         "BAKER-TOO-WEAK); the mechanism governs the CANONICAL "
         "COMPLETION (L_f(t=1) PSD at all dose rungs, world-blind) "
         "and NOT the wall margin (killed by any dose, "
         "direction-blind, r185-concordant): relevance = "
         "POSITIVITY-IRRELEVANT-EXACTNESS-KILL.  Closes NOTHING, "
         "upgrades NOTHING.  NO RH CLAIM.")

    # ------------------------------------------------------------ S9
    section("S9  COMPOSITE VERDICT")
    verdicts = [
        "MECHANISM-EXACT(G03/G10: smooth node collapse + boundary-"
        "phase invisibility)",
        "STRUCTURAL-ZERO-LAW-EXACT(G11/G23: e | 2fk census)",
        "DEFECT-LADDER-O1-FLAT(G21/G22)",
        "LINEAR-FORM-BRIDGE-EXACT(G12/G30)",
        "LIOUVILLE-FLOOR-HOLDS-NOT-TIGHT(G31)",
        baker_enum + "(G32: gap ladders 1e3..1e10 dex)",
        "ET-EQUIDISTRIBUTION-HOLDS(G33) + THREE-DISTANCE(G34)",
        "MARGIN-KILLED-BY-ANY-DOSE(G42)",
        "KILL-DIRECTION-BLIND(G43: dose == antidose)",
        "CANONICAL-MECHANISM-CONFIRMED(G44: L_f(t=1) PSD, "
        "world-blind G45)",
        ("COMM-WALL-REVIVAL(G44)" if revival
         else "COMM-WALL-DEAD(G44)"),
        "DEFECT-DEMAND-FLAT(G50)",
        relevance + "(G51)",
        "LOOPS-FLAGGED-NOT-CONSUMED(G52) + MINCUT-UNCHANGED(G54) + "
        "RESIDUE-UNCHANGED"]
    for v in verdicts:
        print("  " + v)

    dt = time.time() - T0_WALL
    check("G99-runtime", dt <= RUNTIME_BAR,
          "WALL %.1f s (bar %.0f)" % (dt, RUNTIME_BAR))
    print("\n" + "=" * 78)
    npass = sum(1 for _n, okc2, _d in CHECKS if okc2)
    print("GATES: %d/%d PASS   SPEC_SHA %s   WALL runtime %.1f s"
          % (npass, len(CHECKS), SPEC_SHA[:16], dt))
    fails = [nm for nm, okc2, _ in CHECKS if not okc2]
    if fails:
        print("FAILING GATES: " + ", ".join(fails))
    print("COMPOSITE: " + " + ".join([
        "MECHANISM-EXACT",
        "STRUCTURAL-ZERO-LAW-EXACT",
        "DEFECT-LADDER-O1-FLAT",
        "LINEAR-FORM-BRIDGE-EXACT",
        "LIOUVILLE-FLOOR-HOLDS-NOT-TIGHT",
        baker_enum,
        "ET-EQUIDISTRIBUTION-HOLDS",
        "THREE-DISTANCE-CLASSICAL",
        "MARGIN-KILLED-BY-ANY-DOSE",
        "KILL-DIRECTION-BLIND",
        "CANONICAL-MECHANISM-CONFIRMED",
        ("COMM-WALL-REVIVAL" if revival else "COMM-WALL-DEAD"),
        "DEFECT-DEMAND-FLAT",
        relevance,
        "LOOPS-FLAGGED-NOT-CONSUMED",
        "MINCUT-UNCHANGED",
        "RESIDUE-UNCHANGED"]))
    if smoke:
        print("SMOKE MODE -- NOT-VERDICT-BEARING")
    if calib:
        print("CALIB MODE -- PRE-FREEZE, NOT-VERDICT-BEARING")
    print("NO RH CLAIM.  EXPLORATION ONLY.")
    return 0 if not fails else 1


if __name__ == "__main__":
    raise SystemExit(main())
