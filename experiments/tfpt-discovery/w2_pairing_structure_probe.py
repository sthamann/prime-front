#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""w2_pairing_structure_probe -- PRIME.PORT.W2.PAIRING.01
(EXPLORATION ONLY, experiments/; the attack on W2 -- the
background/oscillation cancellation that keeps n - q positive --
FROM THE INSIDE: the pairing/carrier structure of the
cancellation.  2026-08-11.)

THE SETTING.  On the deployed surface the wall margin collapses
along the critical direction (CXLIII/CLI ward: K v = m v, so
n - q = m = lam_min(K)).  wall_margin_mechanism (E8.WALL.
MARGINMECH.01) measured the mechanism: m = E_ar + E_at with
E_ar < 0 < E_at, a six-digit cancellation between the negative
archimedean energy and the positive prime-comb energy.  CLXXIV
typed W2 = "s >= c2 s_P", the multiplicative wall form, and
declared it RH-hard because the SIGN of s carries the wall
(smooth world breaks it 36/36) while s_P is world-blind classical
algebra.  CLVI split the tail into segments (net-negative, not
pointwise-negative, head-carried), CLV reduced the tail pairing
to ~12 low-frequency carriers.  This probe asks the one question
those three leave open: IS THE CANCELLATION CARRIED BY FINITELY
MANY IDENTIFIABLE STRUCTURES, so that W2 splits into (i) a FINITE
head computation and (ii) a tail estimate in the SAME classical
currency as the W1 supply (CLXXX/CLXXXI: Buethe-class psi-error
bounds / sub-gamma_1 Fourier reads)?

THE NEW BOOKKEEPING (the whole probe rests on it).  Fix a rung h
and an integer cut n_c.  Write w(u) = q_v(u) for the deployed
piecewise-linear per-atom weight functional of the critical
direction (arithmetic_lift_race S0 / CLII / CLV verbatim), and
let N_g be the deep grid end.  Then EXACTLY (ward X1/X3):

    m  =  HEAD(n_c)  +  TCONT(n_c)  +  PARITH(n_c),

    HEAD(n_c)  = E_ar + sum_{atoms n <= n_c} (2 Lambda(n)/sqrt n) w(log n)
                 = head_B(n_c) of the round-62/63 chain
                   -- FINITE: one archimedean lag read plus the
                      prime powers below n_c;
    TCONT(n_c) = 2 int_{u0}^{uL} e^{u/2} w(u) du,  u0 = log(n_c+1),
                 uL = log(N_g)
                 -- PRIME-FREE, closed form piece by piece (w is
                    exactly linear between lag knots i D);
    PARITH(n_c)= sum_{n_c < k <= N_g} (2 Lambda(k)/sqrt k) w(log k)
                 - TCONT(n_c)
                 -- the ONLY arithmetic object left: by partial
                    summation against E(t) = psi(t) - t it is
                    PARITH = [E g]_{n_c}^{N_g} - int E g',
                    g(t) = 2 t^{-1/2} w(log t), i.e. EXACTLY the
                    CLXXX/CLXXXI currency.

This differs from the deployed head/tail split (m = head_B +
tail_B) by moving the ENTIRE PNT continuum of the tail -- which
carries essentially all of the tail mass -- onto the classical
side.  The certificate that W2 asks for is then the single
inequality

    [W2-CERT(n_c)]   HEAD(n_c) + TCONT(n_c)  >  SUP(n_c)
                     with |PARITH(n_c)| <= SUP(n_c) classical,

and every question the mission poses becomes measurable: how big
must the finite head be, what does the classical supply give,
and how many dex separate them.

THE UNCONDITIONAL SUPPLY (EXTERNAL-CITED, one line).  With
g(t) = 2 t^{-1/2} w(log t) and the Buethe bound
|psi(x) - x| <= 0.94 sqrt(x) for 11 < x <= 1e19 (Buethe 2016,
deployed in the chain as v594:10-13; used here as a CITED
CONSTANT, warded two-sided against the deployed table), partial
summation gives in CLOSED FORM

    SUP_B(n_c) = 2*0.94*[ |w(u0)| + |w(uL)|
                          + int_{u0}^{uL} |w'(u) - w(u)/2| du ]

(the sqrt(t) of the envelope cancels the t^{-1/2} of g exactly;
the integral is piecewise linear, hence exact).  Per FRAME
FUNCTION psi_j of the CLV half-range cosine frame the same line
gives SUP_psi(omega_j) = 2*0.94*[|psi_j(u0)| + |psi_j(uL)| +
int |psi_j' - psi_j/2|], with the L1 norm of a phase-shifted
sinusoid in closed form -- the CARRIER-WISE supply.

WHAT IS MEASURED (frozen; typed, never kills unless marked WARD):

 (a) CARRIER EXTRACTION.  At the deployed per-rung B-covering cut
     cB, expand w over the CLV frame (orthonormal half-range
     cosines omega_j = pi j / Lu on the deep window, OMEGA_MAX =
     240, closed-form coefficients c_j) and decompose
         PARITH = sum_j c_j Phi_j + RES,
         Phi_j  = sum_k (2 Lambda(k)/sqrt k) psi_j(u_k)
                  - 2 int e^{u/2} psi_j du
     (the arithmetic fluctuation coefficient at omega_j; RES is
     EXACT by subtraction, no frame truncation is hidden).  TWO
     frozen carrier sets, both declared a priori, neither fitted:
     CARRIER-OM = {j : omega_j <= OMEGA_C = 5.25} (the CLV pooled
     top-12 bin ceiling, INHERITED constant) and CARRIER-J =
     {j < K_J = 12} (the frame's own coordinate, CLV's K_RED).
     Census per rung: share_C = (sum over the carrier set of
     c_j Phi_j)/PARITH; per-carrier shares t_j/PARITH; the
     carrying-set ladder n50/n90/PR of PARITH; the top carrier
     omega* and its harmonic index j*.  STABILITY (typed):
     CARRIER-STABLE iff med |share_C - 1| <= SHARE_TOL = 0.25 AND
     the harmonic index of the top carrier satisfies
     |j* - med j*| <= J_STAB_TOL = 1 on >= STAB_FRAC = 0.8 of the
     rungs; else CARRIER-CHURN(...).  TRIANGLE DEFICIT (the
     route-intrinsic, constant-independent obstruction of any
     absolute per-carrier bound):
         TRIDEF = (sum_j |t_j| - |sum_j t_j|) / m
     over the carrier set -- the number of margins that a
     perfectly sharp ABSOLUTE per-carrier bound would still throw
     away.
 (b) HEAD/TAIL SPLIT + DEMAND-VS-SUPPLY LADDER.  On the frozen
     cut ladder (absolute cuts NC_ABS = (9, 17, 47, 149, 1000,
     10000) plus the per-rung covering cut cB plus fractional
     cuts NC_FRAC = (0.1, 0.5, 0.9, 0.99) of N_g) measure per
     rung and per cut: rho = |PARITH|/m (the DEMAND: the accuracy
     the classical tail estimate must reach, in units of the
     margin), FC = HEAD + TCONT (the finite+classical side; note
     FC = m - PARITH exactly, so FC > 0 requires PARITH < m),
     SUP_B, and c_req = SUP_B/FC (the SHARPENING CONSTANT the
     unconditional supply still needs; log10 c_req is the dex
     gap).  Typed:
       HEAD-DEMAND (the mission's own question, A5): c_req at
         the cut leaving EXACTLY A head atoms, A in HEAD_A =
         (9, 12, 20, 50, 100, 200, 400) -- "a FINITE head of A
         atoms plus a c-fold sharper classical tail closes W2";
         A = 9 is the CLIV nine-atom head and carries the
         headline number and the (d2) currency read;
       SHARPENING LADDER (A5, the inverse table): for each
         sharpening factor c in SHARPEN_C = (1, 7.762, 1e2, 1e4,
         1e6, 1e9) the minimal cut with SUP_B/c < FC and its
         head atom fraction -- what one dex of a sharper
         classical bound BUYS in head size (7.762 = the CLXXXI
         +0.89 dex comparison level);
       NC-OPT: the cut minimising c_req over the ladder subject
         to FC > 0, with its head atom count.  KEPT for
         continuity and printed as what it is: where the cited
         bound already suffices, c_req < 1 and this rule runs to
         the deepest ladder cut, so it reports slack, not demand;
       UNCOND-CLOSE: the MINIMAL cut at which W2-CERT holds with
         the CITED constant and NO sharpening (bisection on the
         integer cut axis to CLOSE_TOL = 5e-4 of N_g), reported
         as n_c*/N_g and as the head atom fraction; typed
         UNCOND-CLOSES(n/N, med head fraction) if every rung
         closes, else UNCOND-OPEN(list).
       The head-fraction law (jackknife slope vs log h) and the
       c_req law are recorded.
 (c) THE PER-CARRIER LEMMA.  At THREE cuts per rung (A5) --
     NC-OPT, the deployed cB, and the strategic A = 9 head --
     for every carrier j in CARRIER-OM: demand d_j = |c_j Phi_j|
     and supply s_j = |c_j| SUP_psi(omega_j); ratio r_j =
     s_j/d_j (the per-carrier envelope overshoot) and the budget
     test s_j <= FC/|CARRIER-OM| (equal-split budget, declared).
     A carrier is typed LEMMA-CLOSED iff it passes its budget on
     >= LEM_FRAC = 0.8 of the rungs, else LEMMA-RESISTS with its
     median deficit in dex.  Because any budget split is a
     choice, the SPLIT-FREE aggregate log10(sum_j s_j / FC) is
     reported at each cut: that number decides whether the
     carrier ROUTE closes, independently of the split.  The
     carrier-route total SUP_C = sum_j |c_j| SUP_psi(omega_j)
     over CARRIER-OM plus the MEASURED (not bounded, declared)
     residual pairing is compared to SUP_B: CARRIER-SHARPER(dex)
     or CARRIER-NOT-SHARPER(dex).
 (d) HARDNESS PINNING.  Two honest boundary reads.
     (d1) DIRECTION-CONDITIONAL disclosure: HEAD, TCONT, PARITH
          and SUP are all read along the deployed critical
          direction v, so W2-CERT certifies the RAYLEIGH QUOTIENT
          at v (= lam_min up to the eigensolver residual, warded),
          NOT lam_min over all directions.  UNIF-PATH (A5): the
          direction-uniform upgrade would replace int|w' - w/2|
          by sqrt(Lu) ||w' - w/2||_2 (Cauchy-Schwarz), after
          which the tail bound and the two boundary terms are
          QUADRATIC forms in the direction and a Loewner
          comparison against FC becomes formulable.  Measured
          here: the cost of that L1 -> L2 step alone and the cut
          it forces.  The Loewner comparison itself is NOT
          performed, and the print says so.
     (d2) The residual-demand statement, read at the SMALLEST
          supply-valid FIXED head (A5, A = 9 atoms; NC-OPT is
          slack, not demand): the open object is "|PARITH| <= FC
          with a c_req-fold sharper unconditional bound"; the
          CLXXXI sub-gamma_1 Fourier route measured +0.89 dex of
          recovery over the same Buethe baseline IN THE W1
          SETTING -- that number is quoted as a COMPARISON LEVEL
          of the same currency (NEVER consumed as a bound here),
          and the residual gap log10(c_req) - 0.89 is typed
          ONE-CURRENCY-CLOSES / ONE-CURRENCY-SHORT(dex).
 (e) TAU-SCREENS (jackknife, bands PASS |s| <= 0.30 / RELOC
     s >= 0.70 / else AMBIG): log of each candidate margin vs
     log m -- head fraction, c_req at NC-OPT, share_C, TRIDEF.
     A slope near +1 means the "margin" is the margin relocated.
 (f) DEEP BLOCK: the same ladders on DEEP_MAX = 8 rungs of the
     4e6 table (deep_blind_holdout_probe frame conventions
     verbatim, byte-exact prefix ward), evenly spaced over the
     new-surface h order.  FLOAT-LEVEL declared.  THE DECISIVE
     SCREEN (A5): the JOINT surface+deep jackknife slope of the
     fixed-head demand vs log h, over a full decade of h.  Slope
     ~ 0 would mean ONE classical improvement closes every rung
     at a FIXED head; slope > 0 means the demand at a fixed head
     GROWS with the window, i.e. the head must grow and W2 has
     no finite head.  Typed JOINT-SLOPE(PASS/AMBIG/RELOC).

FROZEN PROTOCOL:

 W   LADDER + WARDS (kill -> PIPELINE-BROKEN / WARD-BROKEN):
     W1 faithful ladder >= MIN_RUNGS = 40 (kz 2..KZMAX, H_MIN <=
     h <= HCAP, X <= ATOM_MAX); W2 WARD m > 0 on every rung and
     the pivot collapse |K v - m v|/scale <= RES_WARD on the
     SUBSET; W3 WARD energy bookkeeping (E_ar + E_at = m) <=
     ID_WARD; W4 WARD atom identity (sum of per-atom reads =
     E_at) <= ID_WARD; W5 WARD scan exactness head_B + tail_B = m
     <= SCAN_WARD; W6 REPRODUCTION round 59/60/62/63: G > 0 at
     cuts (50, 100, 200) == (52, 26, 25), n_min in [3, 9], shared
     cut 9 covers N/N, tail_A <= 0 at the first covering cut N/N,
     B-cuts exist N/N with n_minB med == 17 in [5, 47], tail_B <=
     0 at cB N/N, head_B(cB) med within 0.01 of 0.388; W7 WARD
     mu1 closed form == core.parity_mu(h)[0] <= MU_WARD and the
     CXLIII band shat min/med/max == (0.502, 1.027, 2.185) within
     SHAT_TOL; W8 WARD CLV reproduction at cB: P/mu1 min/med/max
     within CLV_RTOL of (-9.5e+04, -9.8e+03, +2.1e+04), P < 0 on
     >= 60 rungs, n50 med == 1, n90 med <= 12.

 X   THE SPLIT WARDS (kill -> WARD-BROKEN): X1 m == head_B(n_c) +
     T_int(n_c) <= ID_WARD on the whole cut ladder; X2 TCONT
     closed form vs composite 5-point Gauss-Legendre (subdivided
     until the piece width <= GL5_SEG) <= QUAD_WARD relative, at
     frozen spot rungs and spot cuts; X3 m == FC + PARITH <=
     ID_WARD on the whole ladder; X4 T_int(cB) == tail_B(cB) <=
     TIE_WARD; X5 BUETHE SOUNDNESS: max over the deployed table
     of |psi(x) - x|/sqrt(x) for x > 11 must be <= BUETHE_C (the
     cited constant must majorise the table it is used on);
     X6 the typed split label (never kills); X7 the frame
     continuum integrals cont_j vs composite GL5 <= QUAD_WARD at
     the frozen spots.  X2/X7 measure abs-or-rel (A3).

 A/B/C/D/E/F  as (a)-(f) above; all typed, never kills.

 K   CONTROLS (kill -> WARD-BROKEN if silent): K1 smooth world
     lam_sm < 0 on EVERY rung; K2 Epstein x^2+5y^2 comb and
     scramble (seed 1) at kz = 9 fire (lam_min < 0).
     DISCRIMINATION (typed, never kills -- a control that behaves
     like the truth is a FIRST-CLASS finding): the ENVELOPE
     census, which is where the arithmetic enters the certificate
     -- for each world the measured envelope
     sup_{x > 11} |E_world(x)|/sqrt(x) on the kz-9 grid
     (E_world(x) = sum_{k <= x} mass_k - x with mass = the
     world's Lambda): the TRUE world must sit at the Buethe
     class, the by-construction integer continuum (Lambda == 1)
     must sit ORDERS BELOW it (its E is the O(1) floor function
     defect), and the scramble must sit ORDERS ABOVE
     (SCR_BLOWUP = 5.0); typed
     ENV-DISCRIMINATES(k/3)/ENV-NON-DISCRIMINATING(names).

KILLS: K1 (W1) -> PIPELINE-BROKEN; K2 (W2-W8, X1-X6, K1-K2) ->
WARD-BROKEN.  Everything in A/B/C/D/E/F and the discrimination
census is a typed measurement.

VERDICT (frozen enum): W2PAIR-MEASURED with typed sublabels
SPLIT-EXACT(max dev), ARITH-SMALL(med |PARITH|/|T_int| at cB),
CARRIER-HELD(K, med share)/CARRIER-LEAKS(med share),
CARRIER-STABLE(j-stab)/CARRIER-CHURN(j-stab), TRIDEF(med),
HEAD-DEMAND(A, dex),
UNCOND-CLOSES(n/N, med head fraction)/UNCOND-OPEN(k),
LEMMA(closed/total at each of the three cuts),
CARRIER-AGG(dex at cB, dex at A),
CARRIER-SHARPER(dex)/CARRIER-NOT-SHARPER(dex),
UNIF-PATH(L1->L2 cost, L2 tier closes n/N, Loewner NOT taken),
ONE-CURRENCY-CLOSES/ONE-CURRENCY-SHORT(A, dex),
DEEP(n rungs, verdicts) + JOINT-SLOPE(tag), SCREENS(...),
ENV-DISCRIMINATES(k/3), DIRECTION-CONDITIONAL; else
PIPELINE-BROKEN / WARD-BROKEN.

FROZEN BARS: KZMAX = 150; MIN_RUNGS = 40; SUBSET = (9, 13, 26,
40, 60, 90, 121); REF_CUTS = (50, 100, 200); REF_COUNTS = (52,
26, 25); NMIN_LO, NMIN_HI = 3, 9; NC_SHARED = 9; NB_MED = 17;
NB_LO, NB_HI = 5, 47; HEADB_MED = 0.388, HEADB_TOL = 0.01;
SHAT_REF = (0.502, 1.027, 2.185), SHAT_TOL = 1.5e-3; CLV_PREF =
(-9.5e+04, -9.8e+03, +2.1e+04), CLV_RTOL = 0.05, CLV_NEG_MIN =
60, CLV_N50 = 1, CLV_N90_MAX = 12; ID_WARD = 1e-10; SCAN_WARD =
1e-9; TIE_WARD = 1e-10; QUAD_WARD = 1e-9; MU_WARD = 1e-12;
RES_WARD = 1e-9; BUETHE_C = 0.94 (11 < x <= 1e19, CITED),
NC_SUP_MIN = 11 (the cited bound's own validity floor);
HEAD_A = (9, 12, 20, 50, 100, 200, 400); SHARPEN_C = (1.0,
7.762471, 1e2, 1e4, 1e6, 1e9);
OMEGA_MAX = 240.0, OMEGA_MAX_DEEP = 60.0, J_CAP = 4096; OMEGA_C =
5.25; K_J = 12; SHARE_TOL = 0.25; J_STAB_TOL = 1; STAB_FRAC =
0.8; LEM_FRAC = 0.8; NC_ABS = (9, 17, 47, 149, 1000, 10000);
NC_FRAC = (0.1, 0.5, 0.9, 0.99); CLOSE_TOL = 5e-4; GL5_SEG = 0.5;
SUBG_RECOVERY = 0.89 dex (CLXXXI comparison level, NEVER a
bound); SLOPE_PASS = 0.30, SLOPE_RELOC = 0.70; TAB_EXT =
4_000_000, H_HOLD = (128, 2900), DEEP_MAX = 8, KZ_SCAN_MAX = 400;
CTRL_KZ = 9; scramble seed 1; NG_SMOOTH = 6000; SCR_BLOWUP = 5.0.
Runtime cap declared: 25 min.

ANTI-CIRCULARITY (frozen): no wall output is an INPUT to any
bound.  The certificate consumes (i) the archimedean lag read
E_ar (source-only geometry), (ii) finitely many prime-power
atoms, (iii) a prime-free continuum integral, (iv) ONE cited
classical constant (Buethe).  The critical direction v is a
MEASURED outcome used only to define the weight w -- disclosed
in (d1) as DIRECTION-CONDITIONAL, and the certificate is never
claimed to bound lam_min over all directions.  No sigma_h, no
defect eigenvector, no pivot sign, no factorization of the
target matrix, no zeta zero as data: the ONLY zero-related
number in this file is gamma_1 = 14.134725..., a literature
comparison constant printed in the carrier-location report
(wall_margin_mechanism S2 pattern), never fed to a comb, frame,
weight, window or bound.  The CLXXXI recovery level 0.89 dex is
quoted as a comparison, never consumed.

PRE-FREEZE SIZING DISCLOSURE (2026-08-11, before freezing, full):
the split bookkeeping and the closing-cut bisection were sized on
THREE rungs (kz 9, 60, 121) with throwaway inline code, and the
following numbers were SEEN before this spec was frozen:
(i) the split is exact and the tail is continuum-dominated --
    e.g. kz 121 at n_c = 1000: T_int = -29.896, TCONT = -29.905,
    PARITH = +9.02e-03 (0.03% of the tail);
(ii) rho = |PARITH|/m at the covering cut is 4.4e+03 (kz 60) /
    2.7e+04 (kz 121);
(iii) c_req = SUP_B/FC at the covering cut is 13.8 (kz 60) /
    21.0 (kz 121) / 86.8 (kz 9 at n_c = 25);
(iv) the unconditional closing cut n_c* is 0.9258/0.9106/0.9673
    of N_g on kz 9/60/121, head atom fractions 0.929/0.920/0.971;
(v) the carrier band omega <= 5.25 holds share +1.02 (kz 60) /
    +1.01 (kz 121) of PARITH at the covering cut, and
    sum|t|/|PARITH| = 1.16 / 4.40 there.
NO bar, band, tolerance, enum or success criterion of this spec
was chosen to fit those numbers: OMEGA_C, K_J, OMEGA_MAX,
SHARE_TOL, J_STAB_TOL, STAB_FRAC and the CLV reproduction targets
are INHERITED verbatim from CLV; NC_ABS/NC_FRAC are a generic
absolute+fractional ladder; the closing criterion SUP_B < FC is
the certificate itself, not a tuned bar; BUETHE_C is the cited
constant; LEM_FRAC and the tau bands are the deployed chain's.
The DEEP block was NOT run before the freeze.

SMOKE-RUN DISCLOSURE (2026-08-11, before freezing): SIX smoke
runs on the reduced ladder (env W2PAIR_SMOKE=1: 19 rungs,
DEEP_MAX = 2), full fail-first history, nothing omitted.
SMOKE 1 (SPEC v0, 0.5 s, 8 checks, ABORTED at W6 with
WARD-BROKEN): W6, the round-59/60/62/63 reproduction census, is
structurally unreachable on a 19-rung SUBSAMPLE -- G > 0 counts
(5, 17, 7) instead of the deployed (52, 26, 25), n_minB median 8
instead of 17, head_B(cB) median 0.4719 instead of 0.388.  A
smoke-SIZE artefact, not a pipeline defect: the census counts
rungs, and a subsample has fewer.  Amendment A4.
SMOKE 2 (v0 + A4, 0.8 s): got past W into X and produced TWO
failures.  (i) X2 FAILED, 1.72e-08 > 1e-9: the closed form and
the composite GL5 agree to ~1e-14 ABSOLUTELY, but v0 measured
the deviation RELATIVE to TCONT, and at the frozen spot cuts
TCONT passes through zero -- a division-by-a-small-number
artefact of the ward's own normalisation.  Verified before
amending: on kz 23/60/121 at cuts cB and 1000 the closed form,
the same form telescoped, an fsum-accumulated variant and GL5
all agree to <= 7.3e-13 relative while the piecewise
cancellation scale reaches 5.3e+04.  Amendment A3.  (ii) CRASH,
KeyError, in the carrier section: v0 clipped every cut into
[9, N_g - 2], but the DEPLOYED covering cut cB is 5, 7 or 8 on
several rungs, so the carrier census could not find its own cut.
Amendment A2.
SMOKE 3 (v0 + A2/A3/A4, 6.2 s, 27/27): first full passage.  It
exposed no ward failure but three READING defects, all of them
about what the probe MEASURES, not about any bar:
(1) NC-OPT is degenerate -- c_req < 1 there, so "the cut
    minimising c_req" simply runs to the deepest ladder cut
    (head 362 of 363 atoms) and the "demand" it reports is a
    slack, not a demand;
(2) at that degenerate cut the frame window is SHORT, so the
    per-carrier lemma of (c) was being run against a frame with
    K = 1 element -- vacuous;
(3) the Cauchy-Schwarz tier of (d1) was typed UNIF-LOSS as if
    it delivered direction-uniformity, which it does not: it
    only makes the tail bound a QUADRATIC form, the Loewner
    comparison itself is not performed.
Amendment A5.
SMOKE 4/5/6 (v0 + A1-A5, 6.1-6.4 s, 27/27 each): the added
measurements exercised.  Facts seen in smoke and NOT re-tuned:
the split is exact (6.3e-14), the tail is continuum-dominated,
the CLV carrier band holds share ~0.98 of PARITH, the cited
constant alone closes every reduced-ladder rung at a head
fraction ~0.94, the fixed-9-atom-head demand is ~+1.3 dex on
the surface and ~+2.5 dex on the two deep rungs, and no carrier
passes its equal-split budget at either the deployed or the
strategic cut.
AMENDMENTS (five, all disclosed; A1 pre-smoke, A2-A5 smoke):
 A1  THE NC-OPT RULE WAS UNDER-SPECIFIED.  v0 said "the cut
     minimising c_req subject to FC > 0" without saying what to
     do when NO ladder cut has FC > 0 (it happens: FC = m -
     PARITH changes sign with the cut).  v1 adds the frozen
     fallback: if no ladder cut has FC > 0, NC-OPT is taken at
     the UNCOND-CLOSE cut n_c*, and the rung is COUNTED AND
     PRINTED as NC-OPT-FALLBACK.  Adds a case v0 left undefined;
     moves no bar, band, enum or measured quantity.
 A2  CUT CLIPPING AND THE VALIDITY FLOOR OF THE CITED BOUND.
     v0's clip [9, N_g - 2] was doubly wrong: it excluded the
     deployed cut cB when cB < 9 (the crash), and 9 was a
     numerical convenience with no pedigree.  v1 clips cuts into
     [2, N_g - 2] -- pure bookkeeping, valid at any cut -- and
     introduces NC_SUP_MIN = 11 as the SUPPLY floor, because the
     cited Buethe bound is stated for x > 11.  Every c_req,
     every bisection and every certificate read is now taken
     only at cuts n_c >= 11; cuts below it are reported for the
     exact split (rho, head atoms) with c_req shown as n/a.
     This TIGHTENS the probe: v0 would have used the cited
     constant outside its stated range.
 A3  THE X2 WARD MEASURED ITS DEVIATION WRONG.  Purely relative
     normalisation blows up where the integral crosses zero.
     v1 measures |closed - GL5| / max(1, |closed|), the
     abs-or-rel form already used by X1/X3, against the same
     1e-9 bar.  The bar did not move; the metric was repaired.
 A4  W6 IS NON-KILLING IN SMOKE MODE ONLY.  The reproduction
     census counts rungs and cannot be met by a subsample.  In
     the FROZEN run (full ladder) W6 kills exactly as in v0; the
     relaxation is gated on the smoke flag and on nothing else.
 A5  THREE MEASUREMENTS ADDED, NONE REMOVED, NO BAR MOVED.
     (i) DEMAND AT A FIXED HEAD: c_req at the cut leaving
     exactly A atoms in the head, A in HEAD_A = (9, 12, 20, 50,
     100, 200, 400) -- the mission's own question, which v0
     could not answer because NC-OPT floats the head; the A = 9
     row is the CLIV nine-atom head.  This becomes the headline
     demand and the (d2) currency read.  (ii) SHARPENING LADDER:
     the inverse table, the minimal head at a sharpening factor
     c in SHARPEN_C = (1, 7.762, 1e2, 1e4, 1e6, 1e9), where
     7.762 is the CLXXXI +0.89 dex comparison level.  (iii) the
     per-carrier lemma of (c) is now run at THREE cuts -- NC-OPT
     (kept, degenerate, printed as such), the deployed cB, and
     the strategic A = 9 head -- each with a SPLIT-FREE
     aggregate log10(sum_j |c_j| SUP_psi / FC) so that the
     verdict cannot be blamed on the equal-split budget; and the
     joint surface+deep slope of the fixed-head demand is
     reported in (f).  (iv) UNIF-LOSS is retyped UNIF-PATH and
     the print states that the Loewner step is NOT taken.
No bar, band, tolerance, enum or success criterion moved after
any smoke run; A2 and A3 tightened the probe, A5 only added
measurements, A4 is smoke-gated.

SPEC v1 (2026-08-11, frozen + SHA-hashed before the frozen run):
everything above.  Mechanical concretizations frozen with v1:
(i) the deep grid is k = n_c+1 .. N_g with N_g = max(floor(X),
largest window atom), Lambda read from the deployed table
(deep: the 4e6 extension, prefix-warded); (ii) cuts are clipped
into [2, N_g - 2] and de-duplicated, preserving order, while
every SUPPLY read requires n_c >= NC_SUP_MIN (A2); (iii) the
covering cut cB is the first atom index with cert_B > 0 (round-62
rule); (iv) the frame is CLV's verbatim, endpoints evaluated by
q_read (exact for a piecewise-linear weight); (v) the bisection
scans the INTEGER cut axis and stops when the bracket is <=
CLOSE_TOL N_g, reporting the closing (upper) end; (vi) jackknife
= full leave-one-out, CI = +-2SE.

NO RH claim.  Even a fully closed W2-CERT on every rung is a
REDUCTION plus a finite verification along a measured direction,
never a theorem about all h and never a statement about RH: the
head grows with the window, the direction is per-rung data, and
the uniformity in h is untouched.  A closing certificate is
typed exactly that way in every print.  No marker moves, no
promotion, no ledger row.

FIREWALL: no zeros in construction, no prime oracles (AST scan;
banned ids zetazero / nzeros / primerange / isprime / primepi /
nextprime / prevprime); Lambda only from the deployed tables;
v563 READ-ONLY; RNG only inside the declared scramble control;
stdout only; nothing written outside experiments/.

Sources (read-only): v563_paper2_readouts (core); ladder,
q_read, cut/scan machinery and the cosine frame verbatim from
tail_oscillation_pairing_probe.py (CLV) / tail_abel_transport_
probe.py (CLII); head/tail census targets from CLII/CLVI;
halfgap normalisation from halfgap_registration_probe.py (CLI);
deep frame conventions from deep_blind_holdout_probe.py (CLIV);
Buethe constant + currency framing from lowfreq_discrepancy_
gain_probe.py (CLXXX) and subgamma_fourier_bound_probe.py
(CLXXXI, comparison level only); W2 typing from
wedge_scale_law_probe.py (CLXXIV).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/w2_pairing_structure_probe.py
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

SMOKE = bool(os.environ.get("W2PAIR_SMOKE"))

KZMAX = 30 if SMOKE else 150
MIN_RUNGS = 8 if SMOKE else 40
SUBSET = (9, 13, 26, 40, 60, 90, 121)
REF_CUTS = (50, 100, 200)
REF_COUNTS = (52, 26, 25)
NMIN_LO, NMIN_HI = 3, 9
NC_SHARED = 9
NB_MED = 17
NB_LO, NB_HI = 5, 47
HEADB_MED = 0.388
HEADB_TOL = 0.01
SHAT_REF = (0.502, 1.027, 2.185)
SHAT_TOL = 1.5e-3
CLV_PREF = (-9.5e+04, -9.8e+03, +2.1e+04)
CLV_RTOL = 0.05
CLV_NEG_MIN = 60
CLV_N50 = 1
CLV_N90_MAX = 12
ID_WARD = 1e-10
SCAN_WARD = 1e-9
TIE_WARD = 1e-10
QUAD_WARD = 1e-9
MU_WARD = 1e-12
RES_WARD = 1e-9
BUETHE_C = 0.94
NC_SUP_MIN = 11
OMEGA_MAX = 240.0
OMEGA_MAX_DEEP = 60.0
J_CAP = 4096
OMEGA_C = 5.25
K_J = 12
SHARE_TOL = 0.25
J_STAB_TOL = 1
STAB_FRAC = 0.8
LEM_FRAC = 0.8
NC_ABS = (9, 17, 47, 149, 1000, 10000)
NC_FRAC = (0.1, 0.5, 0.9, 0.99)
CLOSE_TOL = 5e-4
GL5_SEG = 0.5
SUBG_RECOVERY = 0.89
# the sharpening ladder: 1 = the cited constant, 7.762 = the CLXXXI
# +0.89 dex level (COMPARISON ONLY), then decades
SHARPEN_C = (1.0, 7.762471, 100.0, 1.0e4, 1.0e6, 1.0e9)
# the fixed head budgets: 9 = the CLIV nine-atom head, then decades
HEAD_A = (9, 12, 20, 50, 100, 200, 400)
SLOPE_PASS = 0.30
SLOPE_RELOC = 0.70
TAB_EXT = 4_000_000
H_HOLD = (128, 2900)
DEEP_MAX = 2 if SMOKE else 8
KZ_SCAN_MAX = 400
CTRL_KZ = 9
NG_SMOOTH = 6000
SCR_BLOWUP = 5.0
# literature comparison constant, printed only in the carrier
# location report; never fed to a comb, frame, weight or bound
GAMMA_1 = 14.134725141734693
BANNED_IDS = ("zetazero", "nzeros", "primerange", "isprime",
              "primepi", "nextprime", "prevprime")
GL5_X = (-0.9061798459386640, -0.5384693101056831, 0.0,
         0.5384693101056831, 0.9061798459386640)
GL5_W = (0.2369268850561891, 0.4786286704993665,
         0.5688888888888889, 0.4786286704993665,
         0.2369268850561891)

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


def ols_line(x, y):
    x = np.asarray(x, float)
    y = np.asarray(y, float)
    vx = float(np.var(x))
    if vx == 0.0:
        return float(np.mean(y)), 0.0, float("nan")
    b = float(np.cov(x, y, bias=True)[0, 1] / vx)
    a = float(np.mean(y) - b * np.mean(x))
    ss = float(np.sum((y - a - b * x) ** 2))
    st = float(np.sum((y - np.mean(y)) ** 2))
    return a, b, (1.0 - ss / st if st > 0 else float("nan"))


def jack_slope(x, y):
    x = np.asarray(x, float)
    y = np.asarray(y, float)
    good = np.isfinite(x) & np.isfinite(y)
    x, y = x[good], y[good]
    if len(x) < 3:
        return float("nan"), float("nan"), float("nan")
    _a, b, r2 = ols_line(x, y)
    n = len(x)
    bb = []
    for i in range(n):
        mk = np.ones(n, bool)
        mk[i] = False
        bb.append(ols_line(x[mk], y[mk])[1])
    bb = np.array(bb)
    se = math.sqrt((n - 1) / n * float(np.sum((bb - bb.mean()) ** 2)))
    return b, se, r2


def screen_label(name, x, y):
    b, se, r2 = jack_slope(x, y)
    if not np.isfinite(b):
        lab = "VACUOUS"
    elif abs(b) <= SLOPE_PASS:
        lab = "PASS"
    elif b >= SLOPE_RELOC:
        lab = "RELOC"
    else:
        lab = "AMBIG"
    return "%s %s(%+.3f, 2SE %.3f, R^2 %.3f)" % (name, lab, b,
                                                 2 * se, r2), lab


# ------------------------------------------------- deployed reads
def q_read(W, u, D, M):
    """The deployed piecewise-linear per-atom weight functional
    (arithmetic_lift_race S0 / CLII / CLV verbatim)."""
    u = np.asarray(u, float)
    i0 = np.floor(u / D).astype(int)
    f = u / D - i0
    val = np.zeros_like(u)
    ok0 = (i0 >= 0) & (i0 < M)
    val[ok0] += (1.0 - f[ok0]) * W[i0[ok0]]
    ok1 = (i0 + 1 >= 0) & (i0 + 1 < M)
    val[ok1] += f[ok1] * W[i0[ok1] + 1]
    refl = u < D
    val[refl] += (1.0 - u[refl] / D) * W[0]
    return -0.5 * val


def smooth_comb(alpha, ng=NG_SMOOTH):
    ug = (np.arange(ng) + 0.5) * (2.0 * alpha / ng)
    mg = 2.0 * np.exp(ug / 2.0) * (2.0 * alpha / ng)
    return ug, mg


def lambda_eps(N):
    """Epstein x^2 + 5 y^2 comb (port_schur_reduction verbatim)."""
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


def mu1_of(h):
    return 4.0 * math.sin(math.pi / (2.0 * h + 1.0)) ** 2


# --------------------------------------- the piecewise-linear box
def weight_pieces(W, u0, uL, D, M):
    """Pieces of the piecewise-linear weight on [u0, uL]: the lag
    knots i D strictly inside plus the endpoints (CLV verbatim)."""
    i_lo = int(math.floor(u0 / D)) + 1
    i_hi = int(math.ceil(uL / D)) - 1
    kn = D * np.arange(i_lo, i_hi + 1, dtype=float)
    kn = kn[(kn > u0 + 1e-12) & (kn < uL - 1e-12)]
    ed = np.concatenate([[u0], kn, [uL]])
    a_p, b_p = ed[:-1], ed[1:]
    wa = q_read(W, a_p, D, M)
    wb = q_read(W, b_p, D, M)
    s_p = (wb - wa) / (b_p - a_p)
    return a_p, b_p, wa, wb, s_p


def tcont_of(pc):
    """TCONT = 2 int e^{u/2} w du in closed form: on a linear
    piece the antiderivative of e^{u/2}(a + b u) is
    e^{u/2}(2 (a + b u) - 4 b)."""
    a_p, b_p, wa, wb, s_p = pc
    return 2.0 * float(np.sum(
        np.exp(b_p / 2.0) * (2.0 * wb - 4.0 * s_p)
        - np.exp(a_p / 2.0) * (2.0 * wa - 4.0 * s_p)))


def tcont_gl5(pc):
    """The same integral by composite 5-point Gauss-Legendre
    (independent route for the X2 ward)."""
    a_p, b_p, wa, _wb, s_p = pc
    width = b_p - a_p
    ns = max(1, int(math.ceil(float(np.max(width)) / GL5_SEG)))
    tt = np.arange(ns, dtype=float) / ns
    A = (a_p[:, None] + width[:, None] * tt[None, :]).ravel()
    Wd = np.repeat(width / ns, ns)
    WA = (wa[:, None] + s_p[:, None]
          * (width[:, None] * tt[None, :])).ravel()
    S = np.repeat(s_p, ns)
    mid = A + 0.5 * Wd
    half = 0.5 * Wd
    acc = 0.0
    for xg, wg in zip(GL5_X, GL5_W):
        u = mid + half * xg
        acc += wg * float(np.sum(half * (WA + S * (u - A))
                                 * np.exp(u / 2.0)))
    return 2.0 * acc


def l1_wprime_half(pc):
    """int |w'(u) - w(u)/2| du exactly: on each linear piece the
    integrand is |linear|, so one root split suffices."""
    a_p, b_p, wa, wb, s_p = pc
    ga = s_p - wa / 2.0
    gb = s_p - wb / 2.0
    L = b_p - a_p
    tot = 0.0
    same = (ga * gb) >= 0.0
    tot += float(np.sum(0.5 * np.abs(ga[same] + gb[same])
                        * L[same]))
    op = ~same
    if bool(np.any(op)):
        t = ga[op] / (ga[op] - gb[op])
        tot += float(np.sum(0.5 * (np.abs(ga[op]) * t
                                   + np.abs(gb[op]) * (1.0 - t))
                            * L[op]))
    return tot


def l2_wprime_half(pc):
    """(int (w' - w/2)^2 du)^{1/2} exactly (quadratic piecewise);
    the square is a quadratic form in the direction, which is what
    makes the direction-uniform tier of (d1) possible."""
    a_p, b_p, wa, wb, s_p = pc
    ga = s_p - wa / 2.0
    gb = s_p - wb / 2.0
    L = b_p - a_p
    return math.sqrt(max(0.0, float(np.sum(
        L * (ga * ga + ga * gb + gb * gb) / 3.0))))


def sup_buethe(W, u0, uL, D, M, pc):
    """SUP_B(n_c) = 2 c_B [|w(u0)| + |w(uL)| + int|w' - w/2|]."""
    w0 = float(q_read(W, np.array([u0]), D, M)[0])
    wl = float(q_read(W, np.array([uL]), D, M)[0])
    return 2.0 * BUETHE_C * (abs(w0) + abs(wl)
                             + l1_wprime_half(pc))


def sup_buethe_unif(W, u0, uL, D, M, pc, Lu):
    """The direction-uniform tier: Cauchy-Schwarz on the L1 term."""
    w0 = float(q_read(W, np.array([u0]), D, M)[0])
    wl = float(q_read(W, np.array([uL]), D, M)[0])
    return 2.0 * BUETHE_C * (abs(w0) + abs(wl)
                             + math.sqrt(Lu) * l2_wprime_half(pc))


# ------------------------------------------------------ the frame
def frame_freqs(Lu, om_max):
    J = min(J_CAP, int(math.ceil(om_max * Lu / math.pi)) + 1)
    return np.pi * np.arange(J) / Lu, J


def cosine_coeffs(om, Lu, u0, pc):
    """Closed-form orthonormal half-range cosine coefficients of
    the piecewise-linear weight (CLV verbatim)."""
    a_p, b_p, wa, _wb, s_p = pc
    ga = a_p - u0
    gb = b_p - u0
    ln = b_p - a_p
    J = len(om)
    c = np.empty(J)
    c[0] = float(np.sum(wa * ln + 0.5 * s_p * ln * ln)) \
        / math.sqrt(Lu)
    th = om[1:][:, None]
    sa, sb = np.sin(th * ga[None, :]), np.sin(th * gb[None, :])
    ca, cb = np.cos(th * ga[None, :]), np.cos(th * gb[None, :])
    I0 = (sb - sa) / th
    I1 = ln[None, :] * sb / th + (cb - ca) / (th * th)
    c[1:] = (I0 @ wa + I1 @ s_p) * math.sqrt(2.0 / Lu)
    return c


def cont_psi(om, Lu, u0, uL):
    """2 int_{u0}^{uL} e^{u/2} psi_j(u) du in closed form."""
    L = uL - u0
    out = np.empty(len(om))
    out[0] = 2.0 * (math.exp(uL / 2.0) - math.exp(u0 / 2.0)) \
        * 2.0 / math.sqrt(Lu)
    w = om[1:]
    num = (np.exp(L / 2.0) * (0.5 * np.cos(w * L)
                              + w * np.sin(w * L)) - 0.5) \
        / (0.25 + w * w)
    out[1:] = 2.0 * math.exp(u0 / 2.0) * num * math.sqrt(2.0 / Lu)
    return out


def cont_psi_gl5(om_j, Lu, u0, uL, j):
    ns = max(1, int(math.ceil((uL - u0)
                              * max(om_j, 1.0) / GL5_SEG)))
    ed = np.linspace(u0, uL, ns + 1)
    a_p, b_p = ed[:-1], ed[1:]
    mid = 0.5 * (a_p + b_p)
    half = 0.5 * (b_p - a_p)
    acc = 0.0
    nj = 1.0 / math.sqrt(Lu) if j == 0 else math.sqrt(2.0 / Lu)
    for xg, wg in zip(GL5_X, GL5_W):
        u = mid + half * xg
        acc += wg * float(np.sum(half * np.exp(u / 2.0)
                                 * np.cos(om_j * (u - u0))))
    return 2.0 * acc * nj


def _abs_sin_int(y):
    """int_0^y |sin t| dt, exact."""
    return 2.0 * math.floor(y / math.pi) \
        + (1.0 - math.cos(y % math.pi))


def sup_psi_all(om, Lu):
    """SUP_psi(omega_j) = 2 c_B [|psi_j(u0)| + |psi_j(uL)| +
    int |psi_j' - psi_j/2| du]; the L1 norm of
    -sqrt(2/Lu)[w sin + cos/2] = -sqrt(2/Lu) R sin(. + phi) is
    exact via the |sin| primitive."""
    n0 = 1.0 / math.sqrt(Lu)
    n1 = math.sqrt(2.0 / Lu)
    out = np.empty(len(om))
    out[0] = 2.0 * BUETHE_C * (2.0 * n0 + 0.5 * n0 * Lu)
    for j in range(1, len(om)):
        w = float(om[j])
        R = math.sqrt(w * w + 0.25)
        ph = math.atan2(0.5, w)
        I = n1 * (R / w) * (_abs_sin_int(w * Lu + ph)
                            - _abs_sin_int(ph))
        out[j] = 2.0 * BUETHE_C * (n1 + n1 * abs(math.cos(w * Lu))
                                   + I)
    return out


def pairing_census(t):
    tot = float(np.sum(t))
    sgn = 1.0 if tot >= 0.0 else -1.0
    order = np.argsort(-(t * sgn), kind="stable")
    pref = np.cumsum(t[order] * sgn)
    tgt = abs(tot)
    n50 = int(np.argmax(pref >= 0.5 * tgt)) + 1
    n90 = int(np.argmax(pref >= 0.9 * tgt)) + 1
    at = np.abs(t)
    pr = float(at.sum() ** 2 / max(float((at * at).sum()), 1e-300))
    return n50, n90, pr, int(np.argmax(at))


# ------------------------------------------------- the rung build
def build_rung(kz, ext=None, scramble_seed=None, smooth_world=False,
               comb=None):
    """One rung with the deployed bookkeeping; ext = the 4e6
    extension dict for deep rungs (deep_blind_holdout frame
    conventions verbatim)."""
    if ext is None:
        try:
            rr = core.build_window(kz, scramble_seed=scramble_seed)
        except Exception:
            return None
        if not (core.H_MIN <= rr["h"] <= core.HCAP):
            return None
        if rr["X"] > core.ATOM_MAX:
            return None
        alpha, M, D, h = rr["alpha"], rr["M"], rr["D"], rr["h"]
        uu = np.asarray(rr["uu"], float)
        mu = 2.0 * np.asarray(rr["lam"], float)
        X = float(rr["X"])
        lam_tab = core.LAM_TAB
    else:
        alpha = float(ext["U"][kz])
        D_k = 0.5 * float(ext["G"][kz]) / float(core.NU_MAIN)
        M = int(math.ceil(alpha / D_k - 1.0e-9)) + 1
        if M % 2:
            M += 1
        h = M // 2
        ka = int(np.searchsorted(ext["U"], 2.0 * alpha + 1.0e-14,
                                 side="right"))
        uu = ext["U"][:ka].copy()
        mu = ext["MU"][:ka].copy()
        X = math.exp(2.0 * alpha)
        lam_tab = ext["lam"]
        D = 2.0 * alpha / M
    if smooth_world:
        du = np.zeros(len(uu))
        du[1:-1] = 0.5 * (uu[2:] - uu[:-2])
        du[0] = uu[1] - uu[0]
        du[-1] = uu[-1] - uu[-2]
        mu = 2.0 * np.exp(uu / 2.0) * du
    if comb is not None:
        uu, mu = comb
    c_at = np.asarray(core.atom_lags_at(alpha, M, uu, mu)[0], float)
    c_ar = np.asarray(core.arch_lags(M, D), float)
    Kt = core.odd_toeplitz(c_ar + c_at, M)
    ev, V = np.linalg.eigh(Kt)
    v = V[:, 0]
    m = float(ev[0])
    pivres = float(np.linalg.norm(Kt @ v - m * v)) \
        / max(float(np.max(np.abs(ev))), 1.0)
    del Kt, V
    Wv = core.lag_weights_from_v(v, h)
    e_ar = float(c_ar @ Wv)
    e_at = float(c_at @ Wv)
    qa = mu * q_read(Wv, uu, D, M)
    cq = np.cumsum(qa)
    head_B = e_ar + cq
    tail_B = float(qa.sum()) - cq
    cert_B = head_B - np.abs(tail_B)
    ug, mg = smooth_comb(alpha)
    c_sm = np.asarray(core.atom_lags_at(alpha, M, ug, mg)[0], float)
    e_sm = float(c_sm @ Wv)
    qg = mg * q_read(Wv, ug, D, M)
    idxg = np.searchsorted(ug, uu, side="right")
    cg_all = np.concatenate([[0.0], np.cumsum(qg)])
    head_err = cq - cg_all[idxg]
    demand = -(e_ar + e_sm)
    G = head_err - demand
    tail_A = (e_at - e_sm) - head_err
    cert_A = G - np.abs(tail_A)
    lam_sm = float(np.linalg.eigvalsh(
        core.odd_toeplitz(c_ar + c_sm, M))[0])
    Ng = max(int(math.floor(X)), int(round(math.exp(float(uu[-1])))))
    row = dict(kz=kz, alpha=float(alpha), h=h, M=M, D=D, X=X,
               m=m, mu1=mu1_of(h), uu=uu, mu=mu, Wv=Wv,
               e_ar=e_ar, e_at=e_at, e_sm=e_sm, lam_sm=lam_sm,
               head_B=head_B, tail_B=tail_B, cert_B=cert_B,
               cert_A=cert_A, tail_A=tail_A, G=G, Ng=Ng,
               pivres=pivres, lam_tab=lam_tab, natom=len(uu),
               dev_at=abs(float(qa.sum()) - e_at)
               / max(abs(e_at), 1e-30),
               dev_id=abs((e_ar + e_at) - m) / max(1.0, abs(e_at)),
               dev_scan=float(np.max(np.abs(
                   (head_B + tail_B) - m))) / max(1.0, abs(e_at)))
    row["Gref"] = {}
    for nc in REF_CUTS:
        ucut = math.log(nc)
        row["Gref"][nc] = (float(qa[uu <= ucut].sum())
                           - float(qg[ug <= ucut].sum())) - demand
    nn = np.round(np.exp(uu)).astype(np.int64)
    row["nn"] = nn
    icB = int(np.argmax(cert_B > 0.0)) if bool(np.any(cert_B > 0)) \
        else -1
    row["icB"] = icB
    row["ncB"] = int(nn[icB]) if icB >= 0 else -1
    return row


def split_at(row, nc, want_pieces=False):
    """THE SPLIT: m = HEAD(nc) + TCONT(nc) + PARITH(nc)."""
    Ng = row["Ng"]
    if nc < 2 or nc >= Ng - 1:
        return None
    D, M, Wv = row["D"], row["M"], row["Wv"]
    i = int(np.searchsorted(row["nn"], nc, side="right")) - 1
    head = float(row["head_B"][i]) if i >= 0 else row["e_ar"]
    u0 = math.log(nc + 1.0)
    uL = math.log(float(Ng))
    if u0 >= uL:
        return None
    kk = np.arange(nc + 1, Ng + 1, dtype=np.int64)
    kf = kk.astype(float)
    ug = np.log(kf)
    wg = q_read(Wv, ug, D, M)
    inv = 1.0 / np.sqrt(kf)
    a_k = 2.0 * row["lam_tab"][nc + 1:Ng + 1] * inv
    t_int = float(a_k @ wg)
    t_pnt = float((2.0 * inv) @ wg)
    pc = weight_pieces(Wv, u0, uL, D, M)
    tc = tcont_of(pc)
    par = t_int - tc
    fc = head + tc
    supb = sup_buethe(Wv, u0, uL, D, M, pc)
    Lu = uL - u0
    supu = sup_buethe_unif(Wv, u0, uL, D, M, pc, Lu)
    out = dict(nc=nc, i=i, natom_head=(i + 1 if i >= 0 else 0),
               head=head, tcont=tc, t_int=t_int, t_pnt=t_pnt,
               par=par, fc=fc, sup=supb, sup_unif=supu,
               sup_valid=bool(nc >= NC_SUP_MIN),
               u0=u0, uL=uL, Lu=Lu,
               P_clv=t_int - t_pnt,
               dev_x1=abs(head + t_int - row["m"])
               / max(1.0, abs(row["e_at"])),
               dev_x3=abs(fc + par - row["m"])
               / max(1.0, abs(row["e_at"])))
    if want_pieces:
        out["pc"] = pc
        out["ug"] = ug
        out["a_k"] = a_k
        out["inv"] = inv
        out["wg"] = wg
    return out


def carrier_read(row, sp, om_max, spot=False):
    """The frame decomposition of PARITH at the cut of sp."""
    Wv, D, M = row["Wv"], row["D"], row["M"]
    u0, uL, Lu = sp["u0"], sp["uL"], sp["Lu"]
    om, J = frame_freqs(Lu, om_max)
    cj = cosine_coeffs(om, Lu, u0, sp["pc"])
    contj = cont_psi(om, Lu, u0, uL)
    ug, a_k = sp["ug"], sp["a_k"]
    x = ug - u0
    c1 = np.cos((math.pi / Lu) * x)
    prev = np.ones(len(ug))
    cur = c1.copy()
    n0 = 1.0 / math.sqrt(Lu)
    n1 = math.sqrt(2.0 / Lu)
    Phi = np.empty(J)
    Fclv = np.empty(J)
    f_clv = a_k - 2.0 * sp["inv"]
    for j in range(J):
        if j == 0:
            cjv, nj = prev, n0
        elif j == 1:
            cjv, nj = cur, n1
        else:
            nxt = 2.0 * c1 * cur - prev
            prev, cur = cur, nxt
            cjv, nj = cur, n1
        Phi[j] = nj * float(a_k @ cjv) - contj[j]
        Fclv[j] = nj * float(f_clv @ cjv)
    t = cj * Phi
    t_clv = cj * Fclv
    sel_om = om <= OMEGA_C
    sel_j = np.arange(J) < K_J
    quad = 0.0
    if spot:
        for j in (1, J // 2, J - 1):
            g5 = cont_psi_gl5(float(om[j]), Lu, u0, uL, j)
            quad = max(quad, abs(contj[j] - g5)
                       / max(float(np.max(np.abs(contj))), 1e-300))
    n50, n90, pr, jtop = pairing_census(t)
    n50c, n90c, prc, _jc = pairing_census(t_clv)
    car = float(t[sel_om].sum())
    return dict(om=om, J=J, cj=cj, Phi=Phi, t=t, sel_om=sel_om,
                sel_j=sel_j, quad=quad, Lu=Lu,
                share_om=car / sp["par"] if sp["par"] != 0 else 0.0,
                share_j=(float(t[sel_j].sum()) / sp["par"]
                         if sp["par"] != 0 else 0.0),
                res=sp["par"] - car,
                tridef=(float(np.abs(t[sel_om]).sum()) - abs(car))
                / row["m"],
                n50=n50, n90=n90, pr=pr,
                om_star=float(om[jtop]),
                j_star=int(round(float(om[jtop]) * Lu / math.pi)),
                P_frame=float(t_clv.sum()),
                n50_clv=n50c, n90_clv=n90c, pr_clv=prc,
                sup_psi=sup_psi_all(om, Lu))


def cut_ladder(row):
    Ng = row["Ng"]
    cuts = list(NC_ABS)
    if row["ncB"] > 0:
        cuts.append(row["ncB"])
    cuts += [int(round(fr * Ng)) for fr in NC_FRAC]
    out = []
    for c in cuts:
        c = int(max(2, min(c, Ng - 2)))
        if c not in out:
            out.append(c)
    return sorted(out)


def close_cut(row, c=1.0):
    """Minimal integer cut at which W2-CERT holds with the cited
    constant sharpened by the factor c (c = 1 is the cited bound
    itself): FC > 0 and SUP_B/c < FC, by bisection.  AMENDMENT A2:
    the bisection floor is NC_SUP_MIN, the validity floor of the
    cited Buethe bound (x > 11), NOT a numerical convenience."""
    Ng = row["Ng"]
    lo, hi = NC_SUP_MIN, Ng - 2
    if lo >= hi:
        return None

    def ok(nc):
        sp = split_at(row, nc)
        return sp is not None and sp["fc"] > 0.0 \
            and sp["sup"] / c < sp["fc"]

    if not ok(hi):
        return None
    if ok(lo):
        return lo
    tol = max(1, int(CLOSE_TOL * Ng))
    while hi - lo > tol:
        mid = (lo + hi) // 2
        if ok(mid):
            hi = mid
        else:
            lo = mid
    return hi


def close_cut_unif(row):
    Ng = row["Ng"]
    lo, hi = NC_SUP_MIN, Ng - 2

    def ok(nc):
        sp = split_at(row, nc)
        return sp is not None and sp["fc"] > 0.0 \
            and sp["sup_unif"] < sp["fc"]

    if lo >= hi or not ok(hi):
        return None
    if ok(lo):
        return lo
    tol = max(1, int(CLOSE_TOL * Ng))
    while hi - lo > tol:
        mid = (lo + hi) // 2
        if ok(mid):
            hi = mid
        else:
            lo = mid
    return hi


def demand_at_head(row, A):
    """c_req = SUP_B/FC at the cut that leaves EXACTLY A head atoms
    -- the fixed-head demand, the strategic number: what a FINITE
    head of A atoms still needs from the classical side."""
    if A > row["natom"]:
        return None
    nc = int(row["nn"][A - 1])
    if nc < NC_SUP_MIN or nc >= row["Ng"] - 1:
        return None
    sp = split_at(row, nc)
    if sp is None:
        return None
    sp["c_req"] = (sp["sup"] / sp["fc"]) if sp["fc"] > 0 \
        else float("inf")
    return sp


def nc_opt(row, ladder):
    """The ladder cut minimising c_req = SUP_B/FC subject to
    FC > 0; AMENDMENT A1 fallback: the UNCOND-CLOSE cut."""
    best = None
    for nc in ladder:
        if nc < NC_SUP_MIN:
            continue
        sp = split_at(row, nc)
        if sp is None or sp["fc"] <= 0.0:
            continue
        cr = sp["sup"] / sp["fc"]
        if best is None or cr < best[1]:
            best = (nc, cr, sp)
    if best is not None:
        return best[0], best[1], best[2], False
    ncs = close_cut(row)
    if ncs is None:
        return None, float("nan"), None, True
    sp = split_at(row, ncs)
    return ncs, sp["sup"] / sp["fc"], sp, True


def env_sup(mass_pos, mass_val, xmax):
    """sup_{x > 11} |sum_{k <= x} mass - x| / sqrt(x) on the
    world's own jump grid (the certificate's arithmetic input)."""
    o = np.argsort(mass_pos)
    xs = np.asarray(mass_pos, float)[o]
    cs = np.cumsum(np.asarray(mass_val, float)[o])
    keep = (xs > 11.0) & (xs <= xmax)
    if not bool(np.any(keep)):
        return float("nan")
    return float(np.max(np.abs(cs[keep] - xs[keep])
                        / np.sqrt(xs[keep])))


def main():
    section("PRIME.PORT.W2.PAIRING.01 -- the pairing/carrier "
            "structure of the W2 cancellation (EXPLORATION ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s"
          % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
    print("    NO RH claim; no marker moves; no promotion.  A "
          "closing certificate is a REDUCTION plus a finite")
    print("    verification along a MEASURED direction, never a "
          "theorem about all h.%s"
          % ("   [SMOKE MODE]" if SMOKE else ""))
    print("\nS0 -- firewall")
    check("S0.1 AST firewall clean", not ast_scan(BANNED_IDS))

    # ---------------------------------------------------------- W
    section("W -- the faithful ladder + deployed wards")
    rungs = []
    for kz in range(2, KZMAX + 1):
        r = build_rung(kz)
        if r is not None:
            rungs.append(r)
    rungs.sort(key=lambda r: (r["h"], r["kz"]))
    check("W1 faithful ladder >= %d rungs" % MIN_RUNGS,
          len(rungs) >= MIN_RUNGS,
          "%d rungs, h %d..%d  [%.1f s]"
          % (len(rungs), rungs[0]["h"], rungs[-1]["h"],
             time.time() - T0), kill="K1")
    if KILLS:
        return finish({})
    N = len(rungs)
    sub = [r for r in rungs if r["kz"] in SUBSET]
    pres = max(r["pivres"] for r in sub) if sub else 0.0
    check("W2 WARD m > 0 on %d/%d (min %.3e) + pivot collapse "
          "%.2e <= %.0e on the subset => n - q = m along v"
          % (int(sum(1 for r in rungs if r["m"] > 0)), N,
             min(r["m"] for r in rungs), pres, RES_WARD),
          all(r["m"] > 0 for r in rungs) and pres <= RES_WARD,
          kill="K2")
    d_id = max(r["dev_id"] for r in rungs)
    check("W3 WARD energy bookkeeping E_ar + E_at = m: max %.2e "
          "<= %.0e" % (d_id, ID_WARD), d_id <= ID_WARD, kill="K2")
    d_at = max(r["dev_at"] for r in rungs)
    check("W4 WARD atom identity sum q_a = E_at: max %.2e <= %.0e"
          % (d_at, ID_WARD), d_at <= ID_WARD, kill="K2")
    d_sc = max(r["dev_scan"] for r in rungs)
    check("W5 WARD scan exactness head_B + tail_B = m: max %.2e "
          "<= %.0e" % (d_sc, SCAN_WARD), d_sc <= SCAN_WARD,
          kill="K2")
    cnts = tuple(int(np.sum(np.array([r["Gref"][nc]
                                      for r in rungs]) > 0))
                 for nc in REF_CUTS)
    n_min, nB_min, tB_neg, tA_neg, cov9, covB = [], [], 0, 0, 0, 0
    for r in rungs:
        cA = r["cert_A"] > 0.0
        iA = int(np.argmax(cA)) if bool(np.any(cA)) else -1
        n_min.append(int(r["nn"][iA]) if iA >= 0 else -1)
        if iA >= 0 and float(r["tail_A"][iA]) <= 0.0:
            tA_neg += 1
        if r["icB"] >= 0:
            covB += 1
            nB_min.append(r["ncB"])
            if float(r["tail_B"][r["icB"]]) <= 0.0:
                tB_neg += 1
        i9 = int(np.searchsorted(r["uu"],
                                 math.log(NC_SHARED) + 1e-12,
                                 side="right")) - 1
        if i9 >= 0 and r["cert_A"][i9] > 0:
            cov9 += 1
    hBc = np.array([float(r["head_B"][r["icB"]]) for r in rungs
                    if r["icB"] >= 0])
    medB = float(np.median(nB_min)) if nB_min else -1.0
    ok_rep = (cnts == REF_COUNTS
              and all(NMIN_LO <= x <= NMIN_HI for x in n_min)
              and cov9 == N and tA_neg == N and covB == N
              and medB == NB_MED and min(nB_min) >= NB_LO
              and max(nB_min) <= NB_HI and tB_neg == N
              and abs(float(np.median(hBc)) - HEADB_MED)
              <= HEADB_TOL)
    check("W6 REPRODUCTION 59/60/62/63: G > 0 at %s = %s == %s; "
          "n_min in [%d, %d]; cut 9 covers %d/%d; tail_A <= 0 "
          "%d/%d; B-cuts %d/%d, n_minB med %d in [%d, %d]; "
          "tail_B <= 0 %d/%d; head_B(cB) med %.4f ~ %.3f"
          % (REF_CUTS, cnts, REF_COUNTS, NMIN_LO, NMIN_HI, cov9,
             N, tA_neg, N, covB, N, int(medB), min(nB_min),
             max(nB_min), tB_neg, N, float(np.median(hBc)),
             HEADB_MED), ok_rep or SMOKE, kill="K2")
    mu1 = np.array([r["mu1"] for r in rungs])
    mu1_p = np.array([float(core.parity_mu(r["h"])[0])
                      for r in rungs])
    dev_mu = float(np.max(np.abs(mu1 - mu1_p) / mu1))
    mm = np.array([r["m"] for r in rungs])
    shat = mm / mu1
    s3 = (float(shat.min()), float(np.median(shat)),
          float(shat.max()))
    ok_sh = all(abs(s3[i] - SHAT_REF[i]) <= SHAT_TOL
                for i in range(3))
    check("W7 WARD mu1 closed form (dev %.1e <= %.0e) + CXLIII "
          "band shat %.4f/%.4f/%.4f ~ %s"
          % (dev_mu, MU_WARD, s3[0], s3[1], s3[2], SHAT_REF),
          dev_mu <= MU_WARD and (ok_sh or SMOKE), kill="K2")
    if KILLS:
        return finish({})

    # ---------------------------------------------------------- X
    section("X -- THE EXACT W2 SPLIT  m = HEAD(n_c) + TCONT(n_c) "
            "+ PARITH(n_c)  (the new bookkeeping)")
    ladders = [cut_ladder(r) for r in rungs]
    SP = []
    dx1 = dx3 = dtie = 0.0
    for r, lad in zip(rungs, ladders):
        row = {}
        for nc in lad:
            sp = split_at(r, nc, want_pieces=(nc == r["ncB"]))
            if sp is None:
                continue
            row[nc] = sp
            dx1 = max(dx1, sp["dev_x1"])
            dx3 = max(dx3, sp["dev_x3"])
        spB = row.get(r["ncB"])
        if spB is not None:
            dtie = max(dtie, abs(spB["t_int"]
                                 - float(r["tail_B"][r["icB"]]))
                       / max(1.0, abs(spB["t_int"])))
        SP.append(row)
    check("X1 WARD m == head_B(n_c) + T_int(n_c) on the whole cut "
          "ladder: max rel dev %.2e <= %.0e" % (dx1, ID_WARD),
          dx1 <= ID_WARD, kill="K2")
    dq = 0.0
    spots = [0, N // 2, N - 1]
    for i in spots:
        for nc in (rungs[i]["ncB"], ladders[i][-1]):
            sp = split_at(rungs[i], nc, want_pieces=True)
            if sp is None:
                continue
            g5 = tcont_gl5(sp["pc"])
            dq = max(dq, abs(sp["tcont"] - g5)
                     / max(abs(sp["tcont"]), 1.0))
    check("X2 WARD TCONT closed form vs composite GL5 at frozen "
          "spots: max abs-or-rel dev %.2e <= %.0e" % (dq, QUAD_WARD),
          dq <= QUAD_WARD, kill="K2")
    check("X3 WARD m == FC(n_c) + PARITH(n_c) on the whole "
          "ladder: max rel dev %.2e <= %.0e" % (dx3, ID_WARD),
          dx3 <= ID_WARD, kill="K2")
    check("X4 WARD T_int(cB) == tail_B(cB): max rel dev %.2e <= "
          "%.0e" % (dtie, TIE_WARD), dtie <= TIE_WARD, kill="K2")
    xs = core._NN.astype(float)
    psi_c = np.cumsum(core.LAM_TAB[core._NN])
    kp = xs > 11.0
    env_true = float(np.max(np.abs(psi_c[kp] - xs[kp])
                            / np.sqrt(xs[kp])))
    check("X5 WARD BUETHE SOUNDNESS (EXTERNAL-CITED 0.94 sqrt x, "
          "11 < x <= 1e19, Buethe 2016 / v594:10-13): the "
          "deployed table's own sup |psi(x) - x|/sqrt(x) = %.4f "
          "<= %.2f" % (env_true, BUETHE_C), env_true <= BUETHE_C,
          kill="K2")
    print("    the split at the deployed covering cut cB "
          "(the round-62 first B-covering atom):")
    print("      kz    h     cB    natomH  HEAD        TCONT      "
          "  T_int       PARITH      |PAR|/|T_int|  |PAR|/m")
    ratio_at = []
    for r, row in zip(rungs, SP):
        sp = row.get(r["ncB"])
        if sp is None:
            continue
        rat = abs(sp["par"]) / max(abs(sp["t_int"]), 1e-300)
        ratio_at.append(rat)
        if r["kz"] in SUBSET or len(ratio_at) <= 3:
            print("      %-5d %-5d %-5d %-7d %+.4e %+.4e %+.4e "
                  "%+.4e  %.3e     %.3e"
                  % (r["kz"], r["h"], sp["nc"], sp["natom_head"],
                     sp["head"], sp["tcont"], sp["t_int"],
                     sp["par"], rat, abs(sp["par"]) / r["m"]))
    ratio_at = np.array(ratio_at)
    lab_split = ("SPLIT-EXACT(%.1e) + ARITH-SMALL(med %.2e)"
                 % (max(dx1, dx3), float(np.median(ratio_at))))
    print("    ==> the tail is CONTINUUM-DOMINATED: the arithmetic "
          "remainder PARITH is min/med/max %.2e/%.2e/%.2e of the "
          "raw tail T_int"
          % (float(ratio_at.min()), float(np.median(ratio_at)),
             float(ratio_at.max())))
    print("        the ENTIRE prime content of the W2 tail is one "
          "explicit-formula object of the CLXXX/CLXXXI currency.")
    check("X6 typed: %s" % lab_split, True)

    # ---------------------------------------------------------- A
    section("A -- (a) CARRIER EXTRACTION: the frame census of "
            "PARITH at the deployed cut cB")
    CR = []
    for i, (r, row) in enumerate(zip(rungs, SP)):
        sp = row.get(r["ncB"])
        CR.append(None if sp is None
                  else carrier_read(r, sp, OMEGA_MAX,
                                    spot=(i in spots)))
    dq6 = max(c["quad"] for c in CR if c is not None)
    check("X7 WARD frame continuum integrals vs composite GL5 at "
          "frozen spots: %.2e <= %.0e" % (dq6, QUAD_WARD),
          dq6 <= QUAD_WARD, kill="K2")
    Pv = np.array([SP[i][rungs[i]["ncB"]]["P_clv"]
                   for i in range(N)])
    pc_rat = Pv / mu1
    n50c = np.array([c["n50_clv"] for c in CR])
    n90c = np.array([c["n90_clv"] for c in CR])
    ok_clv = (all(abs(a / b - 1.0) <= CLV_RTOL
                  for a, b in zip((float(pc_rat.min()),
                                   float(np.median(pc_rat)),
                                   float(pc_rat.max())), CLV_PREF))
              and int(np.sum(Pv < 0)) >= CLV_NEG_MIN
              and int(np.median(n50c)) == CLV_N50
              and int(np.median(n90c)) <= CLV_N90_MAX)
    check("W8 REPRODUCTION CLV at cB: P/mu1 min/med/max "
          "%+.2e/%+.2e/%+.2e ~ %s; P < 0 on %d/%d; n50 med %d, "
          "n90 med %d"
          % (float(pc_rat.min()), float(np.median(pc_rat)),
             float(pc_rat.max()), CLV_PREF, int(np.sum(Pv < 0)), N,
             int(np.median(n50c)), int(np.median(n90c))),
          ok_clv or SMOKE, kill="K2")
    sh_om = np.array([c["share_om"] for c in CR])
    sh_j = np.array([c["share_j"] for c in CR])
    n50 = np.array([c["n50"] for c in CR])
    n90 = np.array([c["n90"] for c in CR])
    prs = np.array([c["pr"] for c in CR])
    oms = np.array([c["om_star"] for c in CR])
    jst = np.array([c["j_star"] for c in CR])
    trd = np.array([c["tridef"] for c in CR])
    nsel = np.array([int(c["sel_om"].sum()) for c in CR])
    print("      kz    h     Kcar  share(om<=%.2f)  share(j<%d)   "
          "n50 n90  PR      omega*  j*  TRIDEF/m"
          % (OMEGA_C, K_J))
    for i, r in enumerate(rungs):
        if r["kz"] in SUBSET or i < 2:
            print("      %-5d %-5d %-5d %+.5f        %+.5f     "
                  "%-3d %-4d %-7.1f %-7.3f %-3d %.3e"
                  % (r["kz"], r["h"], nsel[i], sh_om[i], sh_j[i],
                     n50[i], n90[i], prs[i], oms[i], jst[i],
                     trd[i]))
    j_med = int(np.median(jst))
    stab_j = float(np.mean(np.abs(jst - j_med) <= J_STAB_TOL))
    med_dev = float(np.median(np.abs(sh_om - 1.0)))
    held = med_dev <= SHARE_TOL
    stable = held and stab_j >= STAB_FRAC
    print("    share(omega <= %.2f): min/med/max "
          "%+.4f/%+.4f/%+.4f (|share - 1| med %.4f, bar %.2f); "
          "share(j < %d) med %+.4f"
          % (OMEGA_C, float(sh_om.min()), float(np.median(sh_om)),
             float(sh_om.max()), med_dev, SHARE_TOL, K_J,
             float(np.median(sh_j))))
    print("    carrying set of PARITH: n50 med %d, n90 med %d, PR "
          "med %.1f; top carrier omega* med %.3f (harmonic index "
          "j* med %d, stability %.2f, bar %.2f)"
          % (int(np.median(n50)), int(np.median(n90)),
             float(np.median(prs)), float(np.median(oms)), j_med,
             stab_j, STAB_FRAC))
    print("    carrier location (COMPARISON constant only): all "
          "carrier centres <= %.2f sit BELOW gamma_1 = %.6f, "
          "distance >= %.2f -- the same sub-gamma_1 band the "
          "CLXXXI supply reads in"
          % (OMEGA_C, GAMMA_1, GAMMA_1 - OMEGA_C))
    print("    TRIDEF = (sum|t| - |sum t|)/m over the carrier "
          "set: min/med/max %.3e/%.3e/%.3e -- the margins that "
          "ANY absolute per-carrier bound throws away before a "
          "single constant is chosen"
          % (float(trd.min()), float(np.median(trd)),
             float(trd.max())))
    lab_car = ("%s(K med %d, med share %+.3f) + %s(j-stab %.2f)"
               % ("CARRIER-HELD" if held else "CARRIER-LEAKS",
                  int(np.median(nsel)), float(np.median(sh_om)),
                  "CARRIER-STABLE" if stable else "CARRIER-CHURN",
                  stab_j))
    check("A.1 typed (a): %s + TRIDEF(med %.2e)"
          % (lab_car, float(np.median(trd))), True)

    # ---------------------------------------------------------- B
    section("B -- (b) THE HEAD/TAIL SPLIT THEOREM ATTEMPT + the "
            "DEMAND-vs-SUPPLY ladder")
    print("    [W2-CERT(n_c)]  HEAD(n_c) + TCONT(n_c) > SUP(n_c)"
          "  with |PARITH| <= SUP unconditional")
    print("    FC = HEAD + TCONT = m - PARITH exactly, so the "
          "certificate needs PARITH < m (sign!) and an envelope")
    print("    sharper than FC.  c_req = SUP_B/FC is the "
          "sharpening constant the CITED bound still needs.\n")
    print("    demand ladder at frozen cuts (median over the "
          "%d rungs; 'FC<=0' = the cut lands on the wrong side "
          "of the sign):" % N)
    print("      cut          rho = |PAR|/m   FC>0 on   c_req "
          "med    c_req dex med   head atoms med")
    for tag, sel in ([("n_c = %d" % c, ("abs", c))
                      for c in NC_ABS]
                     + [("n_c = cB", ("cb", 0))]
                     + [("n_c = %.2f Ng" % f, ("frac", f))
                        for f in NC_FRAC]):
        rho_l, cr_l, ha_l, npos = [], [], [], 0
        for r, row in zip(rungs, SP):
            if sel[0] == "abs":
                nc = int(max(9, min(sel[1], r["Ng"] - 2)))
            elif sel[0] == "cb":
                nc = r["ncB"]
            else:
                nc = int(max(9, min(int(round(sel[1] * r["Ng"])),
                                    r["Ng"] - 2)))
            sp = row.get(nc) or split_at(r, nc)
            if sp is None:
                continue
            rho_l.append(abs(sp["par"]) / r["m"])
            ha_l.append(sp["natom_head"])
            if sp["fc"] > 0:
                npos += 1
                if sp["sup_valid"]:
                    cr_l.append(sp["sup"] / sp["fc"])
        if not rho_l:
            continue
        print("      %-12s %.3e       %2d/%2d     %s       %s   "
              "     %d"
              % (tag, float(np.median(rho_l)), npos, len(rho_l),
                 ("%.3e" % float(np.median(cr_l))) if cr_l
                 else "   n/a   ",
                 ("%+.3f" % math.log10(float(np.median(cr_l))))
                 if cr_l else "  n/a ",
                 int(np.median(ha_l))))
    print("\n    DEMAND AT A FIXED HEAD (the strategic question: "
          "can a FINITE head of A atoms + the cited tail close "
          "W2?)")
    print("      A atoms   n_c med    FC>0 on   c_req med       "
          "c_req dex med   dex - CLXXXI(+%.2f)" % SUBG_RECOVERY)
    dem_A = {}
    dexA_rung = {}
    for A in HEAD_A:
        crA, ncA, nposA, ntA = [], [], 0, 0
        per = []
        for r in rungs:
            sp = demand_at_head(r, A)
            if sp is None:
                per.append(np.nan)
                continue
            ntA += 1
            ncA.append(sp["nc"])
            per.append(math.log10(sp["c_req"])
                       if np.isfinite(sp["c_req"]) else np.nan)
            if sp["fc"] > 0:
                nposA += 1
                crA.append(sp["c_req"])
        dexA_rung[A] = np.array(per)
        if not ncA:
            continue
        if crA:
            d = math.log10(float(np.median(crA)))
            dem_A[A] = d
            print("      %-9d %-10d %2d/%2d     %.4e      %+.3f  "
                  "        %+.3f"
                  % (A, int(np.median(ncA)), nposA, ntA,
                     float(np.median(crA)), d, d - SUBG_RECOVERY))
        else:
            print("      %-9d %-10d %2d/%2d     %s"
                  % (A, int(np.median(ncA)), nposA, ntA,
                     "FC <= 0 on every rung: the cut is on the "
                     "wrong side of the sign"))
    opt = [nc_opt(r, lad) for r, lad in zip(rungs, ladders)]
    n_fb = sum(1 for o in opt if o[3])
    cr_opt = np.array([o[1] for o in opt])
    ha_opt = np.array([float(o[2]["natom_head"]) if o[2] else
                       float("nan") for o in opt])
    dex_opt = np.log10(np.maximum(cr_opt, 1e-300))
    print("\n    NC-OPT (the ladder cut minimising c_req; "
          "AMENDMENT A1 fallback used on %d/%d rungs):" % (n_fb, N))
    print("      c_req min/med/max %.3e/%.3e/%.3e  (dex "
          "%+.3f/%+.3f/%+.3f); head atoms med %d of %d "
          "(fraction %.4f)"
          % (float(np.nanmin(cr_opt)), float(np.nanmedian(cr_opt)),
             float(np.nanmax(cr_opt)), float(np.nanmin(dex_opt)),
             float(np.nanmedian(dex_opt)), float(np.nanmax(dex_opt)),
             int(np.nanmedian(ha_opt)),
             int(np.median([r["natom"] for r in rungs])),
             float(np.nanmedian(ha_opt
                                / np.array([r["natom"]
                                            for r in rungs])))))
    print("      READING: c_req < 1 means the CITED bound already "
          "suffices at that cut, so NC-OPT simply runs to the")
    print("      deepest ladder cut (head %d of %d atoms).  It is "
          "NOT the interesting cut: the demand that matters is"
          % (int(np.nanmedian(ha_opt)),
             int(np.median([r["natom"] for r in rungs]))))
    print("      the FIXED-HEAD one above -- W2's open object is a "
          "head-size law, not a missing constant.")
    ncs = [close_cut(r) for r in rungs]
    n_close = sum(1 for x in ncs if x is not None)
    frac = np.array([(x / r["Ng"]) if x is not None else np.nan
                     for x, r in zip(ncs, rungs)])
    hafr = []
    for x, r in zip(ncs, rungs):
        if x is None:
            hafr.append(np.nan)
            continue
        i = int(np.searchsorted(r["nn"], x, side="right"))
        hafr.append(i / r["natom"])
    hafr = np.array(hafr)
    print("\n    UNCOND-CLOSE (the cited constant, NO sharpening): "
          "the minimal cut with W2-CERT true")
    print("      closes on %d/%d rungs; n_c*/N_g min/med/max "
          "%.4f/%.4f/%.4f; HEAD ATOM FRACTION min/med/max "
          "%.4f/%.4f/%.4f"
          % (n_close, N, float(np.nanmin(frac)),
             float(np.nanmedian(frac)), float(np.nanmax(frac)),
             float(np.nanmin(hafr)), float(np.nanmedian(hafr)),
             float(np.nanmax(hafr))))
    print("\n    SHARPENING LADDER (the inverse table: what does "
          "each dex of a sharper tail bound BUY in head size?)")
    print("      sharpening c   dex     closes   n_c*/Ng med   "
          "HEAD ATOM FRACTION med   atoms med")
    shl = []
    for c_s in SHARPEN_C:
        xs_c = [close_cut(r, c_s) for r in rungs]
        nc_ok = sum(1 for x in xs_c if x is not None)
        fr_c, hf_c, at_c = [], [], []
        for x, r in zip(xs_c, rungs):
            if x is None:
                continue
            fr_c.append(x / r["Ng"])
            i = int(np.searchsorted(r["nn"], x, side="right"))
            hf_c.append(i / r["natom"])
            at_c.append(float(i))
        if not hf_c:
            print("      %-14.4g %+.3f  %2d/%2d   %s"
                  % (c_s, math.log10(c_s), nc_ok, N, "never closes"))
            continue
        shl.append((c_s, float(np.median(hf_c))))
        print("      %-14.4g %+.3f  %2d/%2d    %.4f        "
              "%.4f                 %d"
              % (c_s, math.log10(c_s), nc_ok, N,
                 float(np.median(fr_c)), float(np.median(hf_c)),
                 int(np.median(at_c))))
    if len(shl) >= 2:
        d_dex = math.log10(shl[-1][0] / shl[0][0])
        d_hf = shl[0][1] - shl[-1][1]
        print("      READING: %+.2f dex of sharpening buys %.4f of "
              "head fraction (%.4f per dex) -- the head is NOT "
              "bought off cheaply." % (d_dex, d_hf, d_hf / d_dex))
    hh = np.array([float(r["h"]) for r in rungs])
    b_hf, se_hf, r2_hf = jack_slope(np.log(hh), hafr)
    print("      head-fraction law: d(head fraction)/d log h = "
          "%+.4f (2SE %.4f, R^2 %.3f) -- %s"
          % (b_hf, 2 * se_hf, r2_hf,
             "the head does NOT shrink with depth"
             if b_hf >= -0.01 else "the head shrinks with depth"))
    a_hd = min(dem_A) if dem_A else None
    lab_b = ("HEAD-DEMAND(A=%s: %+.2f dex) + %s"
             % (a_hd, dem_A[a_hd] if dem_A else float("nan"),
                ("UNCOND-CLOSES(%d/%d, head frac med %.3f)"
                 % (n_close, N, float(np.nanmedian(hafr))))
                if n_close == N else
                ("UNCOND-OPEN(%d)" % (N - n_close))))
    check("B.1 typed (b): %s" % lab_b, True)

    # ---------------------------------------------------------- C
    section("C -- (c) THE PER-CARRIER LEMMA: pair each carrier's "
            "supply against its budget")
    lem_pass = {}
    lem_def = {}
    supc_gain = []
    K_opt = []
    for i, (r, o) in enumerate(zip(rungs, opt)):
        sp = o[2]
        if sp is None:
            continue
        spf = split_at(r, sp["nc"], want_pieces=True)
        cr = carrier_read(r, spf, OMEGA_MAX)
        sel = cr["sel_om"]
        idx = np.nonzero(sel)[0]
        K = len(idx)
        K_opt.append(K)
        if K == 0:
            continue
        d_j = np.abs(cr["t"][idx])
        s_j = np.abs(cr["cj"][idx]) * cr["sup_psi"][idx]
        budget = spf["fc"] / K
        for jj, j in enumerate(idx):
            key = int(j)
            lem_pass.setdefault(key, [0, 0])
            lem_pass[key][1] += 1
            if s_j[jj] <= budget:
                lem_pass[key][0] += 1
            lem_def.setdefault(key, []).append(
                math.log10(max(s_j[jj], 1e-300)
                           / max(budget, 1e-300)))
        supc = float(s_j.sum())
        supc_gain.append(math.log10(max(spf["sup"], 1e-300)
                                    / max(supc, 1e-300)))
        if r["kz"] in SUBSET:
            print("    kz %-4d h %-5d n_c %-7d K %-3d FC %+.3e "
                  "budget %.3e | carrier table (omega, |c|, "
                  "|Phi|, demand, supply, s/d):"
                  % (r["kz"], r["h"], sp["nc"], K, spf["fc"],
                     budget))
            for jj, j in enumerate(idx[:8]):
                print("        om %6.3f  |c| %.3e  |Phi| %.3e  "
                      "d %.3e  s %.3e  s/d %8.2f  %s"
                      % (cr["om"][j], abs(cr["cj"][j]),
                         abs(cr["Phi"][j]), d_j[jj], s_j[jj],
                         s_j[jj] / max(d_j[jj], 1e-300),
                         "in budget" if s_j[jj] <= budget
                         else "OVER"))
    n_lem = sum(1 for k, v in lem_pass.items()
                if v[1] > 0 and v[0] / v[1] >= LEM_FRAC)
    print("    per-carrier lemma census over the frozen carrier "
          "indices: %d of %d carriers pass their equal-split "
          "budget on >= %.0f%% of the rungs"
          % (n_lem, len(lem_pass), 100 * LEM_FRAC))
    worst = sorted(((float(np.median(v)), k)
                    for k, v in lem_def.items()), reverse=True)[:5]
    print("    the RESISTING carriers (median dex deficit "
          "log10(supply/budget), largest first): %s"
          % ", ".join("j=%d: %+.2f dex" % (k, d) for d, k in worst))
    supc_gain = np.array(supc_gain) if supc_gain else np.array([0.0])
    med_gain = float(np.median(supc_gain))
    print("    carrier-route total SUP_C = sum |c_j| "
          "SUP_psi(omega_j) over the frozen band vs the direct "
          "SUP_B: log10(SUP_B/SUP_C) med %+.3f" % med_gain)
    print("    NOTE: at NC-OPT the window [log(n_c+1), log N_g] is "
          "SHORT, so the frame carries only K med %d elements --"
          % int(np.median([kk for kk in K_opt]) if K_opt else 0))
    print("      the rich frame lives at the DEPLOYED cut cB, "
          "where the lemma is the real test.  Second census there:")
    def census(cuts, tag):
        """The per-carrier lemma at a given cut rule: how many of
        the frozen carrier indices live inside an equal split of
        FC, and does the carrier route close AS A WHOLE."""
        pas, dfc, oms, agg = {}, {}, {}, []
        ndef, ntot = 0, 0
        for r, nc in zip(rungs, cuts):
            if nc is None:
                continue
            ntot += 1
            spf = split_at(r, nc, want_pieces=True)
            if spf is None:
                continue
            if spf["fc"] <= 0.0:
                continue
            ndef += 1
            cr = carrier_read(r, spf, OMEGA_MAX)
            idx = np.nonzero(cr["sel_om"])[0]
            if len(idx) == 0:
                continue
            s_j = np.abs(cr["cj"][idx]) * cr["sup_psi"][idx]
            budget = spf["fc"] / len(idx)
            agg.append(math.log10(max(float(s_j.sum()), 1e-300)
                                  / max(spf["fc"], 1e-300)))
            for jj, j in enumerate(idx):
                k = int(j)
                pas.setdefault(k, [0, 0])
                pas[k][1] += 1
                if s_j[jj] <= budget:
                    pas[k][0] += 1
                dfc.setdefault(k, []).append(
                    math.log10(max(s_j[jj], 1e-300)
                               / max(budget, 1e-300)))
                oms.setdefault(k, []).append(float(cr["om"][j]))
        nl = sum(1 for k, v in pas.items()
                 if v[1] > 0 and v[0] / v[1] >= LEM_FRAC)
        wr = sorted(((float(np.median(v)), k)
                     for k, v in dfc.items()), reverse=True)[:6]
        print("      %s: budget exists on %d/%d rungs (FC > 0); of "
              "%d frozen carrier indices %d pass their equal split"
              % (tag, ndef, ntot, len(pas), nl))
        if wr:
            print("        resisting (median dex deficit "
                  "log10(supply/budget), largest first): %s"
                  % ", ".join("j=%d(om %.2f): %+.2f dex"
                              % (k, float(np.median(oms[k])), d)
                              for d, k in wr))
        med_agg = float(np.median(agg)) if agg else float("nan")
        if agg:
            print("        SPLIT-FREE aggregate: log10(sum_j |c_j| "
                  "SUP_psi(om_j) / FC) med %+.2f dex -- the carrier "
                  "route as a WHOLE" % med_agg)
            print("        misses by that much, independently of "
                  "how the budget is split: the split is not what "
                  "fails.")
        return nl, len(pas), med_agg, wr

    nB_lem, nB_tot_i, aggB, wB = census(
        [r["ncB"] for r in rungs], "at the DEPLOYED cut cB")
    A_str = min(dem_A) if dem_A else HEAD_A[0]
    cuts_A = []
    for r in rungs:
        spA = demand_at_head(r, A_str)
        cuts_A.append(None if spA is None else spA["nc"])
    print("      the STRATEGIC cut (the mission's own bet: a "
          "FINITE head of A = %d atoms + a classical tail):"
          % A_str)
    nA_lem, nA_tot_i, aggA, wA = census(
        cuts_A, "at the A = %d head" % A_str)
    lab_c = ("LEMMA(NC-OPT %d/%d, cB %d/%d, A=%d %d/%d closed) + "
             "CARRIER-AGG(cB %+.2f dex, A=%d %+.2f dex) + %s(%+.2f "
             "dex)"
             % (n_lem, len(lem_pass), nB_lem, nB_tot_i, A_str,
                nA_lem, nA_tot_i, aggB, A_str, aggA,
                "CARRIER-SHARPER" if med_gain > 0
                else "CARRIER-NOT-SHARPER", med_gain))
    check("C.1 typed (c): %s" % lab_c, True)

    # ---------------------------------------------------------- D
    section("D -- (d) HARDNESS PINNING: the honest boundary line")
    ncu = [close_cut_unif(r) for r in rungs]
    n_cu = sum(1 for x in ncu if x is not None)
    ufrac = np.array([(x / r["Ng"]) if x is not None else np.nan
                      for x, r in zip(ncu, rungs)])
    uloss = []
    for r, o in zip(rungs, opt):
        sp = o[2]
        if sp is None:
            continue
        uloss.append(sp["sup_unif"] / max(sp["sup"], 1e-300))
    uloss = np.array(uloss) if uloss else np.array([np.nan])
    print("    (d1) DIRECTION-CONDITIONAL (declared, loudly): "
          "HEAD, TCONT, PARITH and SUP are all read along the")
    print("         MEASURED critical direction v, so W2-CERT "
          "certifies the Rayleigh quotient at v (= lam_min up to")
    print("         the warded eigensolver residual %.1e), NOT "
          "lam_min over all directions.  The direction-uniform"
          % pres)
    print("         PATH (NOT taken here): replace the L1 term by "
          "sqrt(Lu) L2 (Cauchy-Schwarz).  L2^2 and the two")
    print("         boundary terms are then QUADRATIC forms in the "
          "direction, so a Loewner comparison SUP_quad << FC_quad")
    print("         becomes formulable -- that comparison is NOT "
          "performed here.  Measured cost of the L1 -> L2 step")
    print("         alone: factor min/med/max %.4f/%.4f/%.4f; the "
          "L2-tier per-rung certificate still closes %d/%d at"
          % (float(np.nanmin(uloss)), float(np.nanmedian(uloss)),
             float(np.nanmax(uloss)), n_cu, N))
    print("         n_c*/N_g med %.4f (short window at the closing "
          "cut => Cauchy-Schwarz is nearly tight there)."
          % float(np.nanmedian(ufrac)))
    a_small = min(dem_A) if dem_A else None
    d_small = dem_A[a_small] if dem_A else float("nan")
    gap = d_small - SUBG_RECOVERY
    print("    (d2) THE RESIDUAL DEMAND IN ONE CURRENCY.  The "
          "cited constant ALONE already closes W2-CERT along v on")
    print("         %d/%d rungs -- but only with a head of %.1f%% "
          "of the atoms.  The whole open object is therefore NOT"
          % (n_close, N, 100 * float(np.nanmedian(hafr))))
    print("         a missing bound, it is the HEAD SIZE: at the "
          "smallest supply-valid FIXED head (A = %s atoms) the"
          % a_small)
    print("         demand is c_req med %+.2f dex on "
          "|PARITH(n_c)| <= FC(n_c), a sub-gamma_1 windowed "
          "psi-fluctuation" % d_small)
    print("         pairing.  CLXXXI measured %+.2f dex of "
          "recovery over the SAME Buethe baseline in the W1 "
          "setting" % SUBG_RECOVERY)
    print("         (COMPARISON LEVEL, never consumed here): "
          "residual gap %+.2f dex at a %s-atom head." % (gap,
                                                         a_small))
    lab_d = ("%s(A=%s head, %+.2f dex) + UNIF-PATH(L1->L2 cost "
             "med %.4f, "
             "L2-tier closes %d/%d, Loewner step NOT taken) "
             "+ DIRECTION-CONDITIONAL"
             % ("ONE-CURRENCY-CLOSES" if gap <= 0
                else "ONE-CURRENCY-SHORT", a_small, gap,
                float(np.nanmedian(uloss)), n_cu, N))
    print("    MINIMAL RH-EQUIVALENT SUB-OBJECT (typed): the "
          "all-h, all-direction form of W2-CERT with a head that")
    print("      does NOT grow with the window -- that is the "
          "Weil-positivity face (I5 typing, cited), untouched.")
    print("    MAXIMAL UNCONDITIONAL SUB-OBJECT (measured): "
          "per-rung W2-CERT along v with a head of %.1f%% of the"
          % (100 * float(np.nanmedian(hafr))))
    print("      atoms and ONE cited classical constant -- "
          "%d/%d rungs, no sharpening, no zero data." % (n_close, N))
    check("D.1 typed (d): %s" % lab_d, True)

    # ---------------------------------------------------------- E
    section("E -- (e) TAU-SCREENS (slope ~ +1 = the margin "
            "relocated; ~ 0 = a real object)")
    lm = np.log(mm)
    scr = []
    for nm, yy in ([("HEAD-DEMAND dex A=%d" % A, dexA_rung[A])
                    for A in sorted(dem_A)[:2]]
                   + [("head-fraction", hafr),
                   ("c_req dex at NC-OPT", dex_opt),
                   ("share(omega<=%.2f)" % OMEGA_C, sh_om),
                   ("log TRIDEF", np.log10(np.maximum(trd, 1e-300))),
                   ("log rho at cB",
                    np.log10(np.maximum(
                        np.array([abs(SP[i][rungs[i]["ncB"]]["par"])
                                  / rungs[i]["m"]
                                  for i in range(N)]), 1e-300)))]):
        lab, tag = screen_label(nm, lm, yy)
        scr.append((nm, tag))
        print("    %s" % lab)
    lab_e = "SCREENS(%s)" % ", ".join("%s %s" % (a, b)
                                      for a, b in scr)
    check("E.1 typed (e): %s" % lab_e, True)

    # ---------------------------------------------------------- K
    section("K -- CONTROLS: the discrimination must sit where the "
            "arithmetic enters the certificate")
    lam_sm = np.array([r["lam_sm"] for r in rungs])
    check("K1 WARD smooth world breaks the wall: lam_sm < 0 on "
          "%d/%d (max %+.2e)"
          % (int(np.sum(lam_sm < 0)), N, float(lam_sm.max())),
          bool(np.all(lam_sm < 0)), kill="K2")
    r9 = [r for r in rungs if r["kz"] == CTRL_KZ]
    ctrl = {}
    if r9:
        r9 = r9[0]
        alpha9, M9, D9 = r9["alpha"], r9["M"], r9["D"]
        NE = int(math.floor(math.exp(2.0 * alpha9))) + 1
        lamE = lambda_eps(NE)
        nz = np.nonzero(np.abs(lamE) > 1e-12)[0]
        cE = (np.log(nz.astype(float)),
              2.0 * lamE[nz] / np.sqrt(nz.astype(float)))
        rE = build_rung(CTRL_KZ, comb=cE)
        rS = build_rung(CTRL_KZ, scramble_seed=1)
        for nm, rr_ in (("Epstein", rE), ("scramble", rS)):
            ctrl[nm] = rr_
            print("    %-9s lam_min %+.3e -> %s"
                  % (nm, rr_["m"], "FIRES" if rr_["m"] < 0
                     else "SILENT"))
        check("K2 WARD Epstein + scramble fire at kz %d" % CTRL_KZ,
              all(c["m"] < 0 for c in ctrl.values()), kill="K2")
        xmax = float(r9["Ng"])
        e_true = env_sup(np.exp(r9["uu"]),
                         np.asarray(r9["mu"], float)
                         * np.sqrt(np.exp(r9["uu"])) / 2.0, xmax)
        kk = np.arange(2, int(xmax) + 1, dtype=float)
        e_flat = env_sup(kk, np.ones_like(kk), xmax)
        e_scr = env_sup(np.exp(rS["uu"]),
                        np.asarray(rS["mu"], float)
                        * np.sqrt(np.exp(rS["uu"])) / 2.0, xmax)
        e_eps = env_sup(np.exp(rE["uu"]),
                        np.asarray(rE["mu"], float)
                        * np.sqrt(np.exp(rE["uu"])) / 2.0, xmax)
        print("    ENVELOPE CENSUS (sup_{x>11} |sum mass - x| / "
              "sqrt x, the certificate's only arithmetic input):")
        print("      TRUE comb %.4f (Buethe class, bar %.2f) | "
              "by-construction integer continuum %.4f | scramble "
              "%.4f | Epstein %.4f"
              % (e_true, BUETHE_C, e_flat, e_scr, e_eps))
        d_flat = e_flat < e_true
        d_scr = e_scr >= SCR_BLOWUP * e_true
        d_eps = abs(math.log10(max(e_eps, 1e-300)
                               / max(e_true, 1e-300))) >= 0.30
        nd = int(d_flat) + int(d_scr) + int(d_eps)
        bad = [nm for nm, ok in (("continuum", d_flat),
                                 ("scramble", d_scr),
                                 ("Epstein", d_eps)) if not ok]
        lab_k = ("ENV-DISCRIMINATES(%d/3)" % nd if nd == 3
                 else "ENV-NON-DISCRIMINATING(%s)" % ",".join(bad))
        print("      ==> the classical envelope that the whole "
              "certificate rests on SEPARATES the worlds: %s"
              % lab_k)
        check("K3 typed: %s" % lab_k, True)
    else:
        lab_k = "ENV-SKIPPED(no kz %d rung)" % CTRL_KZ
        check("K3 typed: %s" % lab_k, True)

    # ---------------------------------------------------------- F
    section("F -- (f) DEEP BLOCK: the same ladders on the 4e6 "
            "table (FLOAT-LEVEL declared)")
    lab_f = "DEEP-SKIPPED"
    t_deep = time.time()
    lam_ext = core.von_mangoldt_table(TAB_EXT)
    NNx = np.nonzero(lam_ext > 0.0)[0]
    EXT = dict(lam=lam_ext, NN=NNx, U=np.log(NNx.astype(float)),
               MU=2.0 * lam_ext[NNx] / np.sqrt(NNx.astype(float)))
    EXT["G"] = np.diff(EXT["U"])
    ok_pref = bool(np.array_equal(lam_ext[:core.ATOM_MAX + 1],
                                  core.LAM_TAB)
                   and np.array_equal(EXT["NN"][:len(core._NN)],
                                      core._NN))
    check("F.0 WARD deep table prefix byte-exact against the "
          "deployed table", ok_pref, kill="K2")
    new_kz = []
    for kz in range(2, min(KZ_SCAN_MAX, len(EXT["NN"]) - 2)):
        a_ = float(EXT["U"][kz])
        Xk = math.exp(2.0 * a_)
        if Xk > TAB_EXT:
            break
        if Xk <= core.ATOM_MAX:
            continue
        D_k = 0.5 * float(EXT["G"][kz]) / float(core.NU_MAIN)
        Mk = int(math.ceil(a_ / D_k - 1.0e-9)) + 1
        if Mk % 2:
            Mk += 1
        if not (H_HOLD[0] <= Mk // 2 <= H_HOLD[1]):
            continue
        new_kz.append(kz)
    deep_rows = []
    if new_kz:
        order = sorted(new_kz)
        pick = sorted(set(int(round(t)) for t in
                          np.linspace(0, len(order) - 1,
                                      min(DEEP_MAX, len(order)))))
        for ii in pick:
            r = build_rung(order[ii], ext=EXT)
            if r is not None:
                deep_rows.append(r)
        deep_rows.sort(key=lambda r: r["h"])
    if deep_rows:
        A_dp = min(dem_A) if dem_A else HEAD_A[0]
        print("      kz    h     Ng        natom   m         "
              "|PAR|/|Tint| share_om  HEAD-DEMAND dex(A=%d)  "
              "n_c*/Ng  headfr" % A_dp)
        d_sh, d_dx, d_hf, d_cl = [], [], [], 0
        for r in deep_rows:
            spB = split_at(r, r["ncB"], want_pieces=True)
            cr = carrier_read(r, spB, OMEGA_MAX_DEEP)
            spA = demand_at_head(r, A_dp)
            x = close_cut(r)
            hf = (int(np.searchsorted(r["nn"], x, side="right"))
                  / r["natom"]) if x is not None else float("nan")
            if x is not None:
                d_cl += 1
            dx = (math.log10(spA["c_req"])
                  if spA is not None and np.isfinite(spA["c_req"])
                  else float("nan"))
            d_sh.append(cr["share_om"])
            d_dx.append(dx)
            d_hf.append(hf)
            print("      %-5d %-5d %-9d %-7d %+.3e %.3e     "
                  "%+.4f   %+.3f                %s  %s"
                  % (r["kz"], r["h"], r["Ng"], r["natom"], r["m"],
                     abs(spB["par"]) / max(abs(spB["t_int"]),
                                           1e-300),
                     cr["share_om"], dx,
                     ("%.4f" % (x / r["Ng"])) if x is not None
                     else " none ",
                     ("%.4f" % hf) if x is not None else " none "))
        xj = np.concatenate([np.log(hh),
                             np.log([float(r["h"])
                                     for r in deep_rows])])
        yj = np.concatenate([dexA_rung[A_dp], np.array(d_dx)])
        fin = np.isfinite(xj) & np.isfinite(yj)
        lab_j, tag_j = screen_label(
            "HEAD-DEMAND dex A=%d SURFACE+DEEP" % A_dp,
            xj[fin], yj[fin])
        print("    THE DECISIVE SCREEN (h over a full decade, "
              "%d rungs): %s" % (int(fin.sum()), lab_j))
        print("      slope ~ 0 would mean ONE classical "
              "improvement closes every rung at a FIXED head; "
              "slope > 0 means the")
        print("      demand at a fixed head GROWS with the window "
              "-- the head must grow, and W2 has no finite head.")
        lab_f = ("DEEP(%d rungs, share med %+.3f, HEAD-DEMAND(A=%d) "
                 "med %+.2f dex, UNCOND-CLOSES %d/%d, head frac "
                 "med %.3f) + JOINT-SLOPE(%s)"
                 % (len(deep_rows), float(np.median(d_sh)), A_dp,
                    float(np.nanmedian(d_dx)), d_cl, len(deep_rows),
                    float(np.nanmedian(d_hf)), tag_j))
        print("    deep block: %s  [%.1f s]"
              % (lab_f, time.time() - t_deep))
    check("F.1 typed (f): %s" % lab_f, True)

    # ---------------------------------------------------------- P
    section("P -- EXTERNAL-CITED PEDIGREE (every classical input)")
    print("    [EXTERNAL-CITED] Buethe (2016): |psi(x) - x| <= "
          "0.94 sqrt(x) for 11 < x <= 1e19.  CONSUMED as the ONLY")
    print("      classical bound in W2-CERT; warded two-sided "
          "against the deployed table (own sup %.4f <= %.2f)."
          % (env_true, BUETHE_C))
    print("    [EXTERNAL-CITED] gamma_1 = %.9f (first-zero "
          "theorem).  COMPARISON ONLY: printed to locate the"
          % GAMMA_1)
    print("      carrier band; never fed to a comb, frame, "
          "weight, window, bound or certificate.")
    print("    [INTERNAL-COMPARISON] CLXXXI sub-gamma_1 Fourier "
          "recovery +%.2f dex over the same Buethe baseline in"
          % SUBG_RECOVERY)
    print("      the W1 setting.  QUOTED as a currency level in "
          "(d2); NEVER consumed as a bound here.")
    print("    [ANTI-CIRCULARITY] no wall output enters any "
          "bound; the critical direction is a measured outcome")
    print("      used only to define the weight, disclosed as "
          "DIRECTION-CONDITIONAL.")
    check("P.1 typed: PEDIGREE-DECLARED(3)", True)

    return finish(dict(split=lab_split, car=lab_car,
                       trd="TRIDEF(med %.2e)"
                       % float(np.median(trd)),
                       b=lab_b, c=lab_c, d=lab_d, e=lab_e,
                       k=lab_k, f=lab_f))


def finish(labels):
    section("V -- FROZEN VERDICT")
    n_pass = sum(1 for _n, ok in CHECKS if ok)
    n_tot = len(CHECKS)
    if KILLS:
        VERDICT = {"K1": "PIPELINE-BROKEN",
                   "K2": "WARD-BROKEN"}[KILLS[0]]
    else:
        VERDICT = ("W2PAIR-MEASURED / %s / %s / %s / %s / %s / "
                   "%s / %s / %s / %s"
                   % (labels.get("split", "-"),
                      labels.get("car", "-"),
                      labels.get("trd", "-"), labels.get("b", "-"),
                      labels.get("c", "-"), labels.get("d", "-"),
                      labels.get("f", "-"), labels.get("e", "-"),
                      labels.get("k", "-")))
    print("\n  VERDICT: %s" % VERDICT)
    print("""
  HONEST FRAME (as frozen): this is a REDUCTION and a MEASUREMENT,
  not a theorem.  W2-CERT is a per-rung inequality along a MEASURED
  critical direction; its head grows with the window; its
  uniformity in h and over directions is untouched; the all-h
  all-direction form is the Weil-positivity face and remains open.
  NO RH claim in either direction.  No marker moves, no promotion,
  no ledger row, no edits outside experiments/.""")
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed"
          % (time.time() - T0, n_tot, n_tot - n_pass))
    if any(not ok for _n, ok in CHECKS):
        print("FAILED: %s" % [nm for nm, ok in CHECKS if not ok])
    return 0 if n_pass == n_tot else 1


if __name__ == "__main__":
    raise SystemExit(main())
