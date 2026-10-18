#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""make_inventory.py -- regenerate rh/INVENTORY.json.

The inventory is the machine-readable register of every RH-relevant
file in the repository that the rh/ workspace REFERENCES (it never
copies them).  Pinned entries carry the SHA-256 of the file content
at inventory time; run_rh.py uses them as a drift detector.  Living
documents (ledger, program paper, notes) are registered unpinned
(sha256 recorded for information, drift reported as INFO only).

Usage:  python rh/verification/make_inventory.py            (from repo root)
        python rh/verification/make_inventory.py --check    (diff only, write nothing)
        python rh/verification/make_inventory.py --force    (override the row-loss guard)

No-row-loss guard: parallel rh-sync rounds extend INVENTORY.json
additively, so a stale ENTRIES head silently DROPPED their rows on
blind regeneration twice (r306-r316, then r334-r354).  The script
now reads the existing INVENTORY.json before writing and REFUSES to
write (exit 2) if any row present there would be lost; --force
overrides (only when a removal is intentional).  --check writes
nothing and exits 1 on any non-volatile difference between a fresh
regeneration and the committed file (volatile by design: the
'generated' date and the sha256/bytes of pin=false living
documents).
"""

import hashlib
import json
import os
import sys
from datetime import date

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
OUT = os.path.join(REPO, "rh", "INVENTORY.json")

VER = "verification"
EXP = "experiments/tfpt-discovery"

_R285_STATUS = "L* decomposition round (33/33): L* split candidate-wise into (D) the per-atom diagonal condition v_k K_{N_w}(y_k) < 1 - delta and (C) the coherence condition assist = lambda_max/maxdiag - 1 < delta', with EXACT bookkeeping (multiplicative identity lambda = maxdiag x (1+assist), budget equivalence margin > 0 <=> rho < 1 gated at every degree; additive Weyl form measured coarse, slack 0.287).  VERDICT DECOMPOSITION_EXACT(ladder budgets 42/42: maxdiag_Nw 0.9343..0.9941 with sp(N, maxdiag) +0.65 -- the per-atom budget TIGHTENS toward 1 with N; assist_Nw 0.0059..0.0702 with sp -0.65 -- the coherent assist SHRINKS: no fixed delta/delta' budget supported; controls rip at (C): at their crossing maxdiag 0.26..0.38, assist 1.69..2.99, offdiag share 0.63..0.75) + PERATOM_CLASSICAL(binding atom = the shallow-u ARCH edge below the first prime on 42/42 rungs, w9 top-5 = folds 2/4/6/8/10 near-degenerate; classical arcsine yardstick typed COMPARISON_ONLY: measured growth at the binding atom p = 0.38 is SUB-classical (bulk law 1), n*_bind = 58 vs n_DIAG = 187 (1.68 octaves), coverage 0/42 -- (D) survives BECAUSE the discrete kernel grows sub-classically: the provability route for (D) must be a discrete bound) + the b3 SURPRISE: (D) is NOT world-blind at window scale (controls' n_DIAG = 50..91 << 184 vs MAIN 187 > 185: (D) itself separates; the clean split 'D blind + C carries all arithmetic' is REFUTED as stated, while at the DEATH degree the split is clean) => sealed COHERENCE_UNSTRUCTURED by the blind_D clause (the assist itself separates: MAIN 0.0195 at crossing vs controls 1.69..2.99, K_D2 MAIN_SEPARATING; z-scores: MAIN z_v = -3.15 destructive vs controls +4.95..+12.44 constructive -- sign-clean, band-MIXED) + ENSEMBLE_POSITION(MAIN's wall assist is the extreme LOW outlier of both conservation-gated ensembles (sign 16 reps, scramble 12 reps, pct 0.00): the near-single-atom wall is MAIN-specific; early coherence scramble-generic pct 0.75).  mp dps-60 ward incl. maxdiag_184; NO L* claim, NO RH CLAIM"

_R286_STATUS = "L* margin-scaling round (29/29): the decay law of the spectral L* margin 1 - lambda_max(E_{N_w}) and the large-S counterexample hunt, run on the STANDALONE document pipeline (rh/problem/verify_lstar_instance.py imported verbatim; flagship AND every new anchor builder-cross-checked <= 2.9e-15).  VERDICT MARGIN_LAW(POWER preferred, MAD 0.608 vs exp 0.850; alpha = 3.05 vs S / 3.06 vs N_w / 2.39 vs z; halves 3.67/2.07, curvature -1.60 -- the law FLATTENS at large S, the honest anti-extrapolation flag; driver: the decay is the cancellation sharpening c_w -> 1 (exact identity margin = (1-maxdiag)(1-c_w), c_w range 0.9944..0.999991; slope of log(1-c_w) -2.377 vs the diagonal's -0.693); extremal shallow-edge band persists 42/42, PR median 1.81) + NO_CROSSING_EXTENDED(the sealed extension rule -- the document admissibility rule with the window cap lifted, z^2 <= table cap -- admits 83 candidates; the first 15 by (N_w, kz): N_w 942..1218, S 1883..2435, z 101..547, ALL margins sign-safe positive under the sealed tier protocol (f64 two-route equivalence + mp dps-30/45 staggered on every sub-1e-5 rung: 32/42 + 15/15 mp-verified, worst f64-vs-mp rel dev 6.6e-6): min +1.806e-8 at kz=119 (z=529), max +3.314e-7 -- NO counterexample, the triple-verification protocol never fired) + QN_RECONCILED(the r258 terminal bordered ratio q_N measured on the same 57 rungs: q_N < 1 on 57/57 with min(1-q_N) = 0.019 and spearman(1-q_N, N_w) = +0.35 = FLAT (r258 reproduced) while the spectral margin falls 4.0 decades (spearman -0.87) -- TWO DIFFERENT OBJECTS; exact Rayleigh lambda_max >= ||B[:, N_w-1]||^2 on 42/42 (median terminal Rayleigh 0.448, far below lambda ~0.999998); degree sector: the extremal coefficient vector is FULL-SECTOR (terminal-degree share median 1.9e-8, top-decile 0.002, degree PR median 188) -- the terminal pivot cannot see the sector the spectral margin lives in; HARMLESS adjudication (calibration amendments a1/a2 disclosed in the spec, the original symmetric rule's outcome printed permanently): no crossing + extended census O(1) + margin slope -3.33 >= pre-wall loading-speed slope -4.44 - 1.0 (margin/v8 in 19..652, median 144: the margin falls SLOWER than the local loading speed, the benign direction) + q_N flat-positive => the margin decay is the spectral SIGNATURE of the known O(1) wall offset (kinematic eigenvalue-density shrinkage), not an approach to failure) + CENSUS_EXTENDED(minC - N_w on the 15 new anchors {0:1, 1:10, 2:2, 3:1, 4:1}, max +4 <= 8 -- the O(1) wall offset SURVIVES beyond the family cap; equivalence margin > 0 <=> minC >= N_w two-routes 57/57) + DETECTOR_LEDGER(EXTRAP_CALIBRATED: the 42-rung power fit predicts all 15 extension margins inside the 1-decade band, max dev 0.78 dec; no-mp/short-fit/admissibility-cap/posthoc-window mutants all flagged; scopes + fragment audit clean).  NO L* claim, NO RH claim."

_L2_STATUS = "L2 standard-framework census (25/25, the 30-pct lane): WHICH classical deterministic cancellation framework captures the level-2 block sums P_j?  Four sealed frames, each an exact per-rung bound on |sum P_j| = |R|, tested against the r272 flip condition delta' > 0.21 and the 7-exception certification.  VERDICT FRAMEWORK_PARTIAL: F1 DISCREPANCY/Erdos-Turan (Abel form D* x V) dies loudly (both factors grow, delta' -0.21, cert 0/7, paircorr FIRE); F2 VAN DER CORPUT at the frozen H = ceil(sqrt(m)) -- an EXACT world-blind THEOREM, no constant, no fit -- delivers delta' +0.31 > 0.21 and certifies 6/7 exceptions (all but kz15; ladder 38/42, demand max +0.04); F3 Salem-Zygmund sub-Gauss (measured constant C med 0.90 max 1.68, spread 1.86 STABLE, controls covered) delta' +0.38, 6/7; F4 MDS/Azuma against the sign-bin chain filtration (md_ratio 0.29, C4 max 0.68 stable, covered) delta' +0.41, 6/7 -- sealed key adjudicates F4, the honest edge is F2 (exact theorem at 6/7).  kz15 razor misses 0.07-0.12 dec on every surviving frame.  AUTOCORRELATION_PROFILE surprise: only 5/44 rungs (0 exceptions) have a positive root-scale cancellation deficit -- the block sequence REINFORCES on 39/44 worlds ((sum P)^2 > sum P^2): the c3 cancellation is already absorbed INTO the P_j magnitudes; the classical frames win by sqrt(m)-count economy, not by lag structure. L2 lemma candidate: the vdC form as a provable chain statement + the r269 kz15 exact-finite certificate.  mp dps-60 wards; r272 regressions exact.  NO RH claim."

_R288_STATUS = "L* destructive-coherence anatomy (31/31): WHAT about the exact prime-comb source makes the nu interference in the mu frame DESTRUCTIVE (the r285 z_v = -3.15 address)?  All E signs come from the mu-CD kernel K_n between nu positions; phases measured against the zeros of the mu-orthonormal P_{N_w} (Jacobi eigenvalues of the chain; Sturm counts, midpoint alternation and mp dps-60 edge wards exact).  VERDICT SIGN_ANATOMY(the CARRIER MAP: neg fraction 0.503 at N_w but band-structured -- fold distance 1-2 is 87 pct POSITIVE (in-phase), distance 3-4 is 80 pct NEGATIVE (antiphase); the top mode at N_w rides the in-phase adjacent pairs (band 1-2 = +0.68 of |T|, ARCH-ARCH +0.74) while the wall destructivity in the source frame at the crossing (X_v = -0.0517, C_off -0.1046) is carried by the ANTIPHASE next-nearest 3-4 fold ARCH-ARCH pairs (-0.105); controls at their crossing ALL constructive, C_off +0.30..+1.00 -- total sign reversal) + SAMPLING_BLIND(the pure sinc/CD sign formula reaches 0.728 plain / 0.878 |E|-weighted on MAIN, controls 0.81..0.83 -- below the 0.90 bar: only a PARTIAL sign mechanism) + SOURCE_SEPARATOR_NOT_FOUND(the sealed phase-dispersion candidate K_S1 = R = 0.352 is WORLD_BLIND (dead worlds bracket MAIN from both sides) and ensemble-GENERIC (pct 0.44/0.25); chain correlations sp(K_S1, assist_cross) only +0.12/+0.24 -- the plain dispersion does not predict the wall; honest negative) + DIFFERENT_OBJECTS(the r287 block object REINFORCES on w9 (canc = -4.5e-2 < 0, pipeline gates exact) while the kernel-side wall interference is destructive: the r287 magnitude absorption and the kernel destructivity are TWO coordinates) + the DOSE-CURVE FINDING: under conservation-faithful union jitter the phase field barely rotates (turn rate 0.24/dose == static prediction 0.23 -- the chain zeros CO-MOVE; quarter turn would need dose ~1.0) yet z_v flips destructive -> constructive already at dose 0.005 and the depth collapses to 0.71 N_w: the destructive coherence sits in hyper-fine alignments far below the median phase resolution -- the r276 metric firewall is sharper than any phase-rotation account, MEASURED (r276 P2_JIT quoted COMPARISON_ONLY, different channel).  Ensembles = the 28 r285 replicates with identical seeds (records re-gated: assist_cross med 1.89/3.99, MAIN pct 0.00/0.00); equidistribution statistics typed MEASUREMENT_ONLY (forbidden as proof premises).  NO L* claim, NO RH claim."

_R289_STATUS = "L* arch-kernel diophantine relevance test (42/42; strict reviewer contract: no proof attack, no Baker/Matveev application -- need documentation only): the four questions on the r288 hyper-fine coherence, decided by a sealed THREE-WAY twin adjudication.  VERDICT METRIC_ONLY: the RATIONAL twin (every tent center log n replaced by a small-denominator rational multiple of Delta via CF convergents, denominators <= 5.7e4, position cost <= 2.1e-9 = 1e-8 x local gap, weights/cells/on-node family conserved exactly) KEEPS the FULL signature identically -- minC 184, crossing 185, z_v -3.149, carrier band 3-4 -0.105, AA -0.056, mp dps-60 ward at the 1.7e-4 margin -- every exact log-linear-form relation destroyed with ZERO effect; the SHUFFLE twin (tent-split fractions permuted among the atoms, fraction distribution/cells/weights preserved exactly, assignment destroyed) loses totally (depth 0.21, z_v +4.4) but at effective metric dose 0.12 gap where the plain jitter ladder already loses (collapse between theta 1e-3 and 3e-3): fully metric-explained, Baker unnecessary on all tested scales.  Q1 (kernel-degree anatomy): X_v decomposes exactly over CD degrees (sum identity 8e-16); the destructivity is carried by the MID degree band 50-75 pct (-3.17 z-units all pairs / -2.48 carrier set), NOT the terminal degrees (-0.99); at dose 0.005 with degree and frame FIXED no kernel band moves O(1) (all <= 0.01 z) -- the O(1) mover is the CROSSING RELOCATION itself (pivot cascade 185 -> ~131), while the phase field stands still (dphi 0.0012; r288 anchor reproduced with identical seeds).  Q2 (sub-gap attribution): the tent-split fractions {log n / Delta} = {46 log2 n} are the ONLY sub-grid entry of the source into the weights (two-node completeness 4.2e-14; fraction DIFFERENCES underdetermine, global-shift mutant 0.80 LOUD; folded weights typed DOWNSTREAM_COMPLETE); gradient chain d/dfrac = Delta d/du exact (r278 Hellmann-Feynman re-gate 3.1e-07); comb channel at 0.005 (positions grid-frozen): terminal |dlg| 0.47 = O(1) while dphi 0.0067 -- 29x below the sealed 100x bar, honest SUBGAP_CARRIER NOT_SEALED (the r288 200x was a union-channel statement).  Q3 (linear forms, DOCUMENTATION_ONLY): Delta = log2/46 EXACT; 8/70 atoms on-node => 28 EXACT 2-power resonances {46 log2 2^(a-b)} = 0 inside the window; min nonzero |{46 log2(n/m)}| = 1.34e-6 at (181, 241); attribution tops at the small primes n = 3, 7, 25, 8, 29, 17; need exponent ~8.9 vs Baker/Matveev-class ~7e4 (~7900x weaker in the exponent) -- diophantine input only matters for the UNBOUNDED family; fraction detectors WORLD_BLIND.  The measured METRIC THRESHOLD: the coherence needs the fraction PROFILE at ~1e-3 of the local gap and is indifferent to its number-theoretic exactness.  NO L* claim, NO RH claim."

_R290_STATUS = "L* profile-space geometry of the working set (32/32; SPEC_SHA f953dd71): after r289 METRIC_ONLY the round maps WHERE in weight-profile space the destructive coherence survives.  Profile = the signed lag density on the fixed grid (linear in the tent-split fractions at fixed cells, r289 completeness); distances = theta_eq in the exact LAG coordinate with the ANALYTIC reference 0.5 sum m g / Delta = 125.75 (amendment a1, demanded by the sealed self-consistency gate: the density-L1 realization was ill-conditioned, ~37 pct seed noise).  VERDICT BASIN_GEOMETRY(onset map over five sealed interpolation paths MAIN -> SMOOTH/SCR/EPST/ENS-replicate/RIDGE at the NEAR = 0.90 bar: world-directed axes die at theta_eq 4e-5..2.3e-4 -- 5..50x BELOW the 1e-3..3e-3 jitter threshold: the rim is strongly ANISOTROPIC; all onsets GRADUAL (soft shoulder s 0.95 -> 0.77..0.89, no cliff; |kappa| <= 0.08 quasi-linear decay); ISOTROPY = TUBE (killfrac 1.00 at 3e-3 over 16 conservation-gated random directions, 0.38/0.62/1.00 at 5e-4/1e-3/2e-3 -- NEAR-radius ~5e-4..2e-3, consistent with the r285 ensemble pct 0.00); SMOOTH direction = a privileged killer axis (onset 1.36e-4) yet ORTHOGONAL to the first-order wall gradient (cos -3e-5): collective, not gradient-linear) + RIDGE_MAP(the r280 OPT axis rebuilt (theta_up 3.873e-5 anchor exact, endpoint minC 185): the crest LIFTS the wall (minC 185) at extension factors 1..8 = theta_eq 1.5e-4..1.2e-3 -- inside a tube where half the random directions already kill -- and only dies at 2.4e-3) + ALL_FUNCTIONALS_BLIND(the four sealed source-pure profile scalars -- antiphase 3-4 autocorrelation (r288 carrier), total variation, perturbative r278 gradient alignment, mid-band 50-75 pct deviation energy (r289 flip carrier) -- ALL fail to predict the survival depth over the 187-point test set (best sp +0.263, bars 0.5/0.8) and none separates the worlds non-trivially: the coherence functional, if it exists as a closed profile scalar, is NOT among these classes; the working set stays implicitly characterized).  Channel identity gated bitwise on MAIN (union, minC, crossing, z_v, rho vs crossing_from_B); r288/r289 records + r289 jitter-ladder anchor (exact seeds) + r285 control flips 25/21/27/25 + 28 replicates (ENS_SIGN as exact density sign-flips, rep-0 identity gated) reproduced.  NO L* claim, NO RH claim."

_R291_STATUS = 'L* ridge anatomy (30/30; SPEC_SHA bb512c17): the r280/r290 raising axis as an analysis object.  VERDICT RIDGE_SECTION(k_min = 9 at the matched dose; MATCHED-DOSE BUDGET_THRESHOLD PERFECT: one scalar m_star in (1.280, 1.291] separates lift from no-lift over all 18 factor-1 subset cases -- the side-selected first-order wall budget -sum c_j dose with a ~1.3 second-order resistance factor is the near-threshold story; carriers at factor 1: PRIME + HEAD + XIPOS; top-9 atoms n = 2, 3, 5, 13, 11, 4, 29, 7, 89 (small-prime head-heavy, NOT one-atom); GLOBAL rule violated by exactly one overdrive retraction, TOP6 at factor 8 (margin 9.09, minC back to 184, fully alive)) + RIDGE_NO_FIXPOINT(PLATEAU(185): the step-controlled r280 recipe saturates at minC 185 from iterate 1 and NEVER reaches 186; the axis decoheres after iterate 3 (cos +0.92/+1.00/+0.43 then negative) and every full step is rejected thereafter -- a one-degree crest plateau, no stationary better world) + LIFT_MAIN_SPECIFIC(the same iteration from EPSTEIN terminates at step 0 (theta_up 5.03e10 = first-order flat wall c_25 = -2.0e-11); the matched-dose ladder 7.75e-5..0.1 never lifts EPSTEIN) + NONLOCAL_BLIND(best F5S ridge projection sp +0.471 < 0.6 and below the trivial size baseline |sp(F0)| 0.881; F6 rank-2 lethality Gram (train/test split-sealed) +0.137, F7 antiphase deviation pair correlation -0.463 -- the third functional class family stays blind, the working set remains implicitly characterized) + SMOOTH_ANATOMY(SMOOTH_COLLECTIVE_2ND_ORDER: direction PR 112 of dim 368 delocalized; margin curvature d2 -23.3 Richardson-stable vs same-length random -0.98, ratio 23.7 >= 10 -- a genuine quadratic wall valley, NOT an r259-style higher-order resummation gap).  w9/metric/control/ridge anchors gated (REF 125.75, flips 25/21/27/25, theta_up 3.873e-5, r290 map facs 1/4/8 + death at 16 reproduced); amendments a1-a3 disclosed (r290 pinned metric quadruple, 1e-9 conservation-gate headroom, matched-dose/global reporting split).  NO L* claim, NO RH claim.'

_R292_STATUS = "L* curvature two-form round (36/36; SPEC_SHA 050821ff): after the r291 budget-threshold anatomy the round measures whether the working set is characterized by a curvature TWO-FORM.  The margin Hesse form at MAIN over a sealed 29-direction set (3 world axes + ridge + the 9 ridge atoms + 16 fresh conservation-gated random directions, theta_eq-normalized; 3-step diagonals + the full 406-pair polarization matrix, expansion-identity crosscheck 15/15).  VERDICT HESSIAN_SPECTRUM(HESSIAN_LOW_RANK(1) in the sealed L2 spectral metric: ONE eigendirection carries 92.5 pct of sum|lam| = 0.452, a pure on-support DENS combination -- NOT the SMOOTH axis (|cos| 0.07) and NOT the ridge (RIDGE_CURV_FLAT, L2-rank 28/29: the lift axis sits in the flattest curvature sector, exactly the r291 expectation); all 29 diagonals negative -- a genuine multi-directional quadratic valley) + EPSTEIN_CONTRAST(EPST_CURV_FLAT ratio 5.4e-15: the first-order flat EPSTEIN wall is ALSO second-order structureless in the log-h channel -- MAIN's wall has curvature structure, EPSTEIN's has none) + THRESHOLD_NOT_EXPLAINED(the measured log|h_184| quadratic term along the 18 r291 matched-dose sub-directions is NEGATIVE on all 18 (q_R median -0.911; one-sided cubic-triple solve, linear identity vs the analytic budget max rel dev 0.0033) -- a second-order ASSIST, not resistance: the corrected budgets b - q/2 still separate PERFECTLY but the bracket midpoint moves to 1.761, AWAY from the naive flip level 1 -- the r291 ~1.3x factor is a near-flip nonlinearity invisible to low-order jets; m* stays an emergent threshold object) + RETRACTION_HIGHER_ORDER(B2(8) = 27.6 and B3(8) = 150.9 both over-predict lift vs the measured TOP6 factor-8 retraction: not explained at second or third order, honest) + CURVATURE_BLIND(the split-sealed two-form functionals F10 curvature energy / F11 budget+curvature / F12 Rayleigh reach sp +0.884/+0.672/+0.186 on the disjoint 94-point test corpus vs the size baseline |sp(F0)| = 0.907 -- the FOURTH honest negative under the sealed rule, but the closest miss of the whole functional program: 0.023 below the baseline where the r290/r291 classes lost by 0.4-0.6; AUC(dead) 0.097).  w9/metric/control/ridge anchors + the full r291 threshold regression (18 margins max abs dev 5e-4, bracket (1.280, 1.291], TOP6 retraction, top-9 atoms) + SMOOTH d2 -23.31 (ratio 23.7) + EPSTEIN first-order flatness re-gated; amendments a1-a4 disclosed (Hessian step-ladder halved at the measured margin-valid scale, one-sided estimator for the side-selected budget kink, fractional-dose conservation-gate pad 1e-7, L2-unit-consistent ridge display).  NO L* claim, NO RH claim."

_R293_STATUS = "L* metric reconciliation round (43/43; SPEC_SHA 33c44cc6): the r292 near-miss adjudicated.  Leg A seals THREE metrics BEFORE any functional evaluation (M1 theta_eq, M2 L2 on the signed density, M3 = the curvature metric sqrt(x |H_tr| x) with the spectral-absolute-value rule; distortion factors max/min M2-M1 11.0 / M3-M1 59.5 / M3-M2 123.5, largest-deviation sector DENS = the r292 top-eigenaxis sector; positive-mass share of H_tr 0.0052).  VERDICT METRIC_RECONCILED(F10 in M2): THE HAMMER LANDED -- evaluated against the size baseline OF ITS OWN METRIC, the split-sealed curvature energy F10 beats a baseline for the first time in four rounds (sp +0.884 vs sp(F0_M2) -0.860, home margin +0.024) AND holds FUNCTIONAL_BEYOND_BASELINE (partial spearman sp(F10, s | F0_M2) = +0.423 >= 0.4 on the 94-point test split, sign-stable +0.826 on the train-side replica) -- the FIRST predictive closed functional of the working set; PROMOTION CANDIDATE flagged for the next consolidation wave (nothing promoted here) + MIX_CONTROL(MIX_IS_CAUSE: the r292 mixed margin -0.023 vs the reconciled home margin +0.024 -- the theta_eq-vs-L2 metric mix WAS the cause of the r292 near-miss) + the m* resolution: all 8 selected flips (4 closest lifters + 4 closest non-lifters by |b - 1.2853|) are SIMPLE ZEROS of h_184 (alpha = 1.000 +- 0.003 on both sides; 225 gated wall evaluations, conservation exact, death watch clean, every flip lands at minC 185 with h_185 < 0) but MSTAR_NO_LAW: the per-direction thresholds m*_dir = b x f* range 1.13..1.39 (XIPOS 1.1295 .. TOP6 1.3931) -- NO fixed safety distance to the singularity in budget, theta_eq, L2 or curvature units (gap spreads 3.0/3.0/3.8/10.2 vs bar 1.25): the r291 'one scalar m*' bracket was a fixed-dose artifact, the ~1.3 factor is TYPICAL, not universal + RETRACTION_SIDE(the TOP6 factor-8 retraction IS a second simple h_184 zero at f_ret = 7.107, lift window (1.226, 7.107) -- on the side the monotone budget prognosis (8.07 and rising) is structurally blind to; h_185 sign +1 there) + BASELINE_ANATOMY(F0_DIRECTIONAL: median within-band |sp| 0.370 > 0.3, dead-only sp -0.890 / alive-only -0.005 -- the baseline is NOT a pure radius artifact, the r290-r292 absolute-sp bars stand as drawn).  w9/metric/control/ridge anchors + the full r291 threshold regression + the COMPLETE r292 spectroscopy (trace share 0.925, lam_top -0.418, SMOOTH |cos| 0.07, ridge rank 28/29) and contest (F10 +0.884 / F0_M1 -0.907 / AUC 0.097 on the bit-identical 94-point split) re-gated; amendment a1 disclosed (the Leg-C death watch redrawn from the raw h_185 sign to the real criterion minC < 184 -- diagnostic display fix, no bar moved).  NO L* claim, NO RH claim."

_R294_STATUS = "L* F10 stability round (42/42; SPEC_SHA 88c6fd1e): the r293 promotion candidate stress-tested BEFORE consolidation wave 8, exactly as the r293 worker demanded.  Leg A (the sealed promotion bar, fixed before any corpus was built): FIVE fresh seed-disjoint 147-point corpora (seeds 294000+1000k; same conservation discipline and r293 test-family mixture; tags pairwise disjoint and disjoint from the r292 training tags, gated) against the UNCHANGED hash-sealed r293 H_tr (sha256 gate 3447ed198a56, re-training mutant CAUGHT): the |sp| WIN over the home L2 baseline replicates on EVERY corpus (5/5: F10 +0.675..+0.787 vs F0_M2 -0.660..-0.714, margins +0.003..+0.115) BUT the partial-correlation channel does NOT replicate at its r293 magnitude (partials +0.248..+0.555, median 0.299; only 2/5 clear the sealed +0.3 bar, two miss by <= 0.003) => sealed verdict F10_FRAGILE (win 5/5, part 2/5, full 2/5) -- promotion precondition NOT met, recommendation NO for wave 8; the r293 partial +0.423 was the TOP of the fresh distribution, not the center.  Leg B robustness: TRAIN_ROBUST (leave-3-out jackknife sigma 0.0101 <= 0.012) + RANK2_CARRIES (the top DENS eigenaxis alone reaches +0.855 and misses the 0.860 baseline by 0.005; two whitened eigendirections suffice; top-axis DENS coefficient-mass share 0.989) + STEP_STABLE (half FD ladder sp(F10_mid, F10_half) = 0.9995; the double ladder MARGIN_INVALID with 4 non-finite margins = the r292-a1 NaN boundary reproduced and excluded by the sealed rule).  Leg C window transport (w7/w11, complete window-own chains: walls NREF_w 59/63, extraction dose caps 0.157/0.068 after the measured w11 full-ridge collapse, ladders unhalved, 67-point window corpora, window-local survival readout, 0 censored): KNIFE-EDGE -- w11 beats its own L2 baseline by +0.002, w7 loses by 0.009 => WINDOW_PARTIAL(w11); the solid transport finding is MECHANISM CONSTANCY: the top curvature eigenaxis is a DENS combination on w7/w9/w11 alike (coefficient-mass shares 0.795/0.989/0.834).  Leg D: L2_NOT_DENS -- the DENS-neutralized baseline (six DENS eigenaxes rescaled to the typical curvature per unit L2, scales c_j 2.2..75.6) is WEAKER than plain L2 (sp -0.828 vs -0.860) and the partial vs it RISES to +0.586: the F10 information is not the DENS-sector length distortion; why L2 is the right coordinate stays open.  Anchors complete (w9; the FULL r293 contest bit-identical incl. tag SHA a76cc578 and partials +0.423/+0.826; r292 spectroscopy 0.925/-0.418); must-fails m1 hash-seal / m2 seed-reuse (146 tags) / m3 conservation / m4 window category error (dimension-blocked, disclosed control) all CAUGHT.  NO promotion, NO L* claim, NO RH claim."

_R295_STATUS = "L* F10 sp-hardening round (44/44; SPEC_SHA 4d7d8095): the two r294 fronts executed -- harden the partial-free |sp| statement on a LARGE ensemble, and dissect the partial channel by direction family.  Leg A (the sealed THREE-CLAUSE hardening bar, fixed before any corpus was built and untouchable): TWENTY fresh seed-disjoint 147-point corpora (seeds 300000+1000k; the FULL forbidden-seed set of r292/r293/r294 -- 192 seeds -- enumerated and gated, zero overlap; r294 corpus protocol verbatim) against the UNCHANGED H_tr (hash gated == the published r294 seal 3447ed198a56): F10 wins the |sp| contest on 14/20 corpora (margins -0.079..+0.125, median +0.028, six losses incl. -0.041/-0.057/-0.079) => sealed verdict F10_SP_MAJORITY -- the HARDENED bar (>= 18/20 AND margin median >= +0.02 AND no loss beyond 0.02) fails on TWO clauses: the r294 5/5 was itself TOP-OF-DISTRIBUTION, exactly the way the r293 partial was; the partial-free ranking statement is a DOCUMENTED REGULARITY (19/25 combined fresh-corpus census), NOT a theorem candidate; promotion recommendation NO for wave 8; Leg C (candidate statement) VOID by the sealed rule.  PARTIAL20 median +0.279 IQR [+0.182, +0.401] range [-0.133, +0.566] (the r293 +0.423 confirmed top-of-distribution; PARTIAL_STD = the full 147-point-mix partial sealed as the standardized statistic of future rounds).  Leg B partial anatomy (pooled 2921 points, MAIN once): NO family reaches the STRONG 0.4 bar -- PATH +0.156 / WORLD +0.245 / FRAC +0.067 NULL / DENS +0.104 (regime split disclosed; ATOM/RIDGE structurally absent by the unchanged split seal): the beyond-distance information is diffuse, strongest on structured deviations toward dead worlds, near-null on random FRAC rays; the r293-composition-matched subsample (87 points per corpus, the PATH-heavy r293 mix 0.46/0.29/0.17) lifts the median partial to +0.346 -- the sealed gain clause (+0.067 >= +0.05) PASSES but the level clause fails by 0.004 (0.346 < 0.35) => R293_LUCK under the sealed adjudication: composition explains PART of the r293/r294 partial discrepancy, the rest was n=94 sampling noise.  Leg D bycatch: L2_VIA_CONSERVATION formally (the eta_0 conservation projection leaves the contest exactly invariant, |sp| shifts 0.0000) but near-tautological (projected-out eta_0 share median 2.9e-30, max 3.2e-3): 'why L2' stays open in substance, weakness disclosed in the verdict.  Anchors complete (w9; the FULL r293 contest bit-identical incl. tag SHA a76cc578, partial +0.423/+0.826 and the family census 1/5/40/25/15/8; r292 spectroscopy 0.925/-0.418; the COMPLETE r294 core rebuilt bitnear: 5-corpus table, jackknife sigma 0.0101, rank sp +0.855/+0.863/+0.884, DENS share 0.989); must-fails m1 hash / m2 seed collision (26 overlaps flagged on the r294 base) / m3 bar sharpness (every clause has teeth, both directions) / m4 conservation all CAUGHT.  NO promotion, NO L* claim, NO RH claim."

_R296_STATUS = "L* DENS-identity round (39/39; SPEC_SHA ffb413c8): the reviewer hard fork on the r292 curvature axis -- is the 92.5-pct DENS top eigendirection e_top mathematically identifiable and coupled to the L* extremizer?  ONE sealed candidate library, hash-frozen BEFORE any cosine: T1 = grad_delta lambda_max(E_184) via Hellmann-Feynman from the extremal eigenvector phi* (envelope theorem dlam = int p*^2 d(dnu) - lam int p*^2 d(dmu), fold-map pullback with the s_l envelope; FD ward worst rel dev 3.8e-7 on 6 sealed coordinates at the re-measured margin-valid step; lam2/lam3 gradients as excluded controls), the von Mangoldt family (all/prime-only/prime-power-only), the local-metric family (fold-gap deviations / 1-over-log / r289 fraction profile), the kernel diagonals at N_w (Christoffel / E-diag / CD-diag), the 4-dim moment-gradient subspace T5, 8 nulls + a decoy; PRIMARY metric = the in-span cosine cos(e_top, P_D T) on the 29-direction span (e_top exists only there), raw/lag/capture honesty columns per candidate; bars 0.80/0.40 sealed.  VERDICT DENS_WORLD_BLIND(T5_MOMENTS 0.825 downgraded; WORLD-DOWNGRADE) + T1_COUPLING(cos_span +0.394 -- THE COUPLING NUMBER: below the sealed 0.40 bar, above the 0.331 noise max, below noise+pad 0.431; the lam3 control couples HARDER (-0.574): what coupling exists is a near-crossing eigenvalue-BAND property, not top-specific) + COS_TABLE(every arithmetic T2/T3/T4 member <= 0.38, all within reach of the noise reference; T3_LOCALGAP degenerate -- the gap profile is constant on the 367/368-occupied fold grid, disclosed) + WORLD_CONTRAST(the T5 moment-subspace root share HOLDS at EPST 0.571 / SCR 0.603 >= 0.40 => construction-adjacent low-moment smoothness, the sealed downgrade fires PART -> BLIND; DISCLOSED TENSION: both control values sit BELOW their own null-quadruple maxima 0.758/0.691 -- the absolute 0.40 collapse bar is near-unreachable for a 4-dim subspace in a 12-dim span, the downgrade is conservative and the sealed rule stands unmoved; EPST's margin channel at its OWN wall degree 25 carries Richardson-STABLE curvature structure -- r292's flatness was the log-h channel, a different object, disclosed) + WINDOW_TRANSPORT(w7 0.930 / w9 0.825 / w11 0.942 for T5 -- but the w7/w11 values sit AT their window null maxima 0.923/0.734 (12-dim spans); T1_w 0.179/0.314 below window noise; window DENS shares 0.795/0.834 == r294, class rule 3/3 hold, no window downgrade).  THE FORK ANSWER: the DENS top axis is NOT identifiable with any sealed arithmetic density, and at the sealed bar NOT the L*-gradient direction (T1 misses PART by 0.006, honest); the only above-chance structure is its low-moment smoothness (0.825 vs ~0.4 chance at w9); raw-grid overlaps <= 0.08 with every candidate at captures <= 0.36 -- the axis is dominated by structure no on-support arithmetic profile in the library represents.  Anchors complete (w9 + metric + flips + ridge/top9 + lambda_max(E_184) = 0.99983248 dev 4.1e-9 + r283 top-5 + EPSTEIN first-order flatness + the FULL r292 spectroscopy rebuilt verbatim incl. the DENS05/04/03/01 loadings); amendments a1-a4 disclosed pre-freeze (evenness gate conditioning at libm precision, FD coordinate/step re-anchoring at the measured margin-valid scale, the r294 0.989 share correctly re-typed as the 18-direction training-form record, hardening repetition pinned to the ACTUAL best member incl. the subspace rule); must-fails m1 wrong-normalization / m2 unprojected / m3 seal-break / m4 decoy all CAUGHT/HELD.  NO L* claim, NO RH claim."

_R297_STATUS = "L2 vdC chain-provenance round (27/27; SPEC_SHA e42a76eb; reviewer routing after the r296 DENS close: resources to the L2 front): can the vdC INPUT (the P-variance / autocorrelation scaling) be derived source-purely from the chain, turning the v964-S0 van der Corput theorem plus input into delta' > 0.21 as a theorem on the generic half?  VERDICT TARGET_INEQUALITY_FROZEN(the weakest sufficient input bound, all constants live: sigma := slope(S_F/M^2) <= sigma* = 2 x (slope(eps_c2/M) - 0.21) - slope(pref) = -0.516; measured sigma -0.714 -- the truth clears the target with 0.198 sigma margin = 0.099 in delta': what is missing is not room, it is provenance; exact slope additivity 2.6e-16; m2 pad-sharpness: sigma* composes to delta' = 0.21 EXACTLY, the pad-dropped mutant to 0) + ROUTE_TABLE(three source-pure provenance routes, every chain step EXACT on 47 worlds incl. broken-arithmetic controls -- world-blind by the same algebra: B1 PAIR-IDENTITY (A(0) <= gapmax x eps_c2 via the r271 alternation identity) delta' -0.112, break: gapmax/M slope -0.535 vs needed <= -1.178 -- the MAX pair gap falls far slower than the mean amplitude (B_amp -0.81): the Jacobi near-balance is a MEAN statement, its extreme is not chain-controlled; B2 NODE-DENSITY (A(0) <= 2 maxM sumM; r273 root-scale trace) delta' -0.097, the boundary POSITIONS are near-equidistributed with FALLING discrepancy (D_rank med 0.024, slope -0.42 -- provable terrain) but the MASS imbalance n x maxM/sumM GROWS (slope +0.244): node density supplies the count, not the decay; B3 FEJER/PARSEVAL (per-run Cauchy-Schwarz + the symbolic sum rule sum w x^2 pi_k^2 = h_{k+1} + a_k^2 h_k + b_k^2 h_{k-1} PROVED exact in Fractions) delta' -0.097 -- with THE SURPRISE OF THE ROUND: the chain is EXACTLY ORTHOGONAL w.r.t. the WINDOW measure (cross/diag devs 0.000 across kz15/kz20/mains/EPST/SCR) while BORDER and WDIFF break (cross med ~1.1): the Parseval attachment point EXISTS; what remains is the measure transfer (the vdC input lives on the BORDER union) and the signed-to-absolute gap (med 4.3, slope +0.217, mixed-sign weights)) + CHAIN_PROVENANCE_PARTIAL(B3_PARSEVAL, gap: slope miss 0.307) + KZ15_NOTE(structurally outside for all three routes, misses 0.57/0.86/0.91 dec -- the r270 exact-finite certificate remains the permanent closure).  Leg C void; the common obstruction named: every universal majorization of A(0) through MAGNITUDES pays a growing max/mean imbalance factor; the SIGNED structure carrying sigma = -0.71 is what magnitude chains cannot see.  The two assets left for the lane: the exact window-measure orthogonality (a bordered-form transfer statement window -> border union is the concrete named object) and the falling rank-coordinate equidistribution.  Anchor regression exact (r287 delta'(F2) +0.309, cert 6/7 + 38/42, kz15 miss 0.096 dec; r272 sp +0.67 / gamma_true +0.453 / sl_c2 +0.196; r270 reserve 0.0268; v964-S0 vdC set re-computed green in Fractions); amendments a1 (index bugfix after smoke crash) / a2 (reporting precision) disclosed, no bar moved; mp dps-60 deep wards.  NO L2 lemma claim, NO RH claim."

_R298_STATUS = "L2 window-border transfer round (28/28; SPEC_SHA 05e831be; the r297 asset-1 attachment point executed): does an exact, sign-preserving transfer statement exist from the WINDOW measure (where the chain is exactly orthogonal and the Parseval sum rule is proved) to the BORDER form (where the vdC input S_F lives)?  VERDICT DECOMPOSITION_EXACT(S_F = B(omega,omega) + B(Delta,omega+beta) with Delta = border (-) window and B the frozen positional Fejer block kernel -- S_F re-derived as the Fejer quadratic form B(beta,beta) of the border measure, kernel reproduction worst 7.5e-16 against the sealed r287 pipeline; the identity exact to 8.8e-16 of the decomposition scale on 47 worlds incl. broken-arithmetic controls; per-block attribution t_j = PDelta_j phi_j sums exactly; the LINEAR corollary MEASURED: the window image of the drive functional VANISHES at float precision (2.2e-12 main / 6.4e-12 deep) -- the drive is 100 pct transfer at the linear level) + TRANSFER_DOMINANT(the sealed three-way adjudication: NOT subdominant, NOT the r259/r261 near-cancellation -- the window main term is EMPTY: MAIN/M^2 med -3.94 dec, two decades BELOW S_F med -2.00 dec, slope -1.386 collapsing; T > 0 on 42/42, share med 0.99; the omega-Delta cross term negligible (med -1.4e-4) => S_F ~ B(PDelta,PDelta): THE VDC INPUT IS THE FEJER ENERGY OF THE DIFFERENCE MEASURE ITSELF; sigma = -0.714 is the decay exponent of this ONE named source-pure quantity; the in-T sign cancellation sum|t_j|/|T| med 1.69 grows at +0.207 -- the r297 imbalance factor localized INSIDE T; m2 mustfail: the magnitude version |Delta| breaks the identity by 1.7e+0 of scale LOUD -- the r297 magnitude error certified; controls EPST/SCR same class, WORLD-BLIND) + IMBALANCE_NOTE(BROAD_BASED: dropping the top-1/top-3 mass runs lowers the imbalance slope +0.244 -> +0.188/+0.197, not below the 0.5x bar -- no outlier carrier; the connection stat sp(block mass, |t_j|) med +0.69: the mass-imbalance carriers ARE the T carriers -- the two r297 gap halves are ONE structure) + Leg C VOID (no candidate theorem; the precisely narrowed wave-9 gap object: prove the Fejer-energy decay of Delta).  Anchors bit-near (sigma -0.714 / sigma* -0.516 / sl_c2 +0.196 / sl_pref +0.489; D_rank med 0.024 sl -0.42; imb sl +0.244; WINDOW orth HOLDS 5.1e-7, BORDER cross med 1.101; sum rule re-proved exact in Fractions, wrong-b^2 mutant CAUGHT); amendments a1 (toy-constant hand-arithmetic fix after smoke) / a2 (reporting text) disclosed, no bar moved; mp dps-60 deep wards.  NO L2 lemma claim, NO RH claim."

_R300_STATUS = "L2 diag-target round (31/31; SPEC_SHA 55218b5d; the r299 frozen rest pair executed: can the diagonal decay sl_D <= sigma* = -0.516 -- margin 0.055, THIN -- be derived source-purely, and the ratio flatness with it?): the exact participation anatomy of the ONE positive quantity D = sum PDelta_j^2 plus three derivation routes and the exact kernel-envelope ratio majorant.  VERDICT DIAG_ANATOMY(n_eff = L1^2/D med 37.41 slope +0.963; the EXACT decomposition sl_D = 2 x sl_L1 - sl_neff = 2 x (+0.196) - (+0.963) = -0.571 (dev 6.7e-16): the entire diagonal decay is the participation growth net of a mildly growing L1 mass -- 'many small instead of few large' is now a measured identity; second coordinates sl_mx -0.542, sl_fill -0.225; class shares A/Bv/cross 0.64/0.16/+0.20; D band shares 0.27/0.26/0.46 -- D itself is BROADBAND: the r299 LOWPASS character of B is pure kernel weighting) + ROUTE_TABLE(B1 chain-norm CS on the |dw| measure valid 47/47 but composed -0.384 FAILS sigma* by 0.133 AND the |dw| identity census BREAKS (cross med 0.932) -- the proven sum rule does NOT attach to the difference measure, the chain-norm shortcut is closed honestly; B2 max x L1 valid 47/47 composed -0.346 FAILS by 0.170 -- the max IS atom-controlled (a single c-value distance, mx/maxatom med 1.07): the irreducible loss is the fill decay -0.225, invisible to every max x mass bound; B3 NEFF: needed slope(n_eff) >= 2 sl_L1 - sigma* = +0.908 (disclosed: an exact reparametrization of DIAG_TARGET), measured +0.963 MET margin 0.055; D_rank(Delta) slope -0.117 falling, sp(D_rank, n_eff) -0.81 -- the equidistribution bridge is real but correlational) + DIAG_SPLIT(B3(NEFF_TARGET)) + RATIO_BOUNDED_STRUCTURAL(the exact kernel envelope F_H <= min(H, 1/(H sin^2)) gives B/D <= R_env med 1.61 with slope -0.122 <= +0.05 on 47/47 -- the ratio half of the r299 rest pair is settled at the structural level; the lobe-width heuristic REFUTED, sp(B/D, q50) -0.47) + REST_FROZEN(ONE inequality remains: NEFF_TARGET slope(n_eff) >= +0.908, measured +0.963, margin 0.055) + WORLD_SENSITIVE(the FILL class separates MAIN (FILL_LOW) from both dead controls (FILL_HIGH) -- the second world-separating class of the lane after the r299 O-sign class).  Anchors bit-near (r297 sigma/sigma*, r298 full set, r299 full set incl. sl_D -0.571 / ratio 1.29/-0.168 / full overlap 42/42); m1 participation mutant 8/3 exact, m2 swapped max/L1 toy 2 exact + real 0.84/0.72 of D LOUD, m3 wrong-h sum rule CAUGHT in Fractions, m4a/m4b scope-flagged; amendment a1 (reconstruction scale floor on the degenerate SMOOTH Delta == 0) disclosed, no bar moved; mp dps-60 deep wards.  NO L2 lemma claim, NO RH claim."

_R301_STATUS = "L2 neff-target round (32/32; SPEC_SHA 6f8cc404; the r300 frozen rest executed: why does n_eff = L1^2/D grow ~N, and can slope(n_eff) >= 2 sl_L1 - sigma* = +0.908 -- measured +0.963, margin 0.055 THIN -- be derived source-purely?): the Renyi order anatomy, the jackknife margin stability and three derivation routes.  VERDICT NEFF_ANATOMY(the order family N_2/N_3/N_4/N_inf med 37.41/27.88/24.04/15.47 grows at nearly ONE exponent +0.963/+0.926/+0.894/+0.738 (tail N_4/N_2 slope only -0.069): ECHT anti-concentration, not a broadening tail; positional IQR flat -0.005 -- the count grows, the footprint stays) + STABILITY(jackknife min/max +0.936/+0.979, 0/42 below NEED -- NO MARGIN_FRAGILE, the margin survives every single-rung removal; half-ladder lo/hi +0.982/+0.802: the deep half flattens below +0.908, the honest anti-extrapolation flag) + ROUTE_TABLE(B1 THE STRUCTURAL FINDING: n_eff = n_act/(1 + CV^2) EXACTLY (module-own Fractions re-proof, ward <= 6.8e-16 on 47 worlds) with the PERFECT count link n_act == m on 42/42 -- the effective-carrier count IS the constructive level-2 block count, growing at +1.002; B2 the exact weighted-discrepancy interval chain (|w_j/W - lambda_j| <= 2 delta_w, a star-discrepancy theorem, wards 0.0 on 47 worlds) FAILS by 0.834: the |dc|-WEIGHTED discrepancy (med 0.167, slope -0.017) is 10x the raw D_rank and near-flat -- the r300 bridge correlation lived on the raw positions, the max-based equidistribution shortcut is closed honestly; B3 the difference profile decorrelates at lag ONE (l_loc med 1.0, slope -0.036), n_eff_atom slope +0.942 coupled sp +0.96 -- but the LOCAL sum-rule census BREAKS 24/24 (cross med 0.93): the |dw| non-orthogonality is scale-free, no local energy identity attaches) + NEFF_SPLIT(B1(UNIF_TARGET) | B3(MIX_TARGET)) + REST_FROZEN(strictly smaller than r300's: the ONE remaining inequality is UNIF_TARGET -- slope(1 + CV^2) <= sl_nact - NEED = +0.094, measured +0.039, margin 0.055: the growth statement became a BOUNDEDNESS statement about the block profile of |PDelta|; NEFF_DERIVED missed only the sealed CV_FLAT clause, sl_cv2p +0.039 > 0) + WORLD_SENSITIVE(the UNIF class does NOT separate: MAIN CV^2 1.03 bracketed by EPST 0.72 and SCR 2.76 -- unlike the O-sign and FILL classes, quasi-uniformity is not where the arithmetic lives; r300 PART/FILL classes reproduced EXACTLY).  Anchors bit-near (r297 sigma/sigma*, r298 full set, r299 full set, r300 full set incl. n_eff 37.41 / sl_neff +0.963 / adds 6.7e-16); m1a/m1b Fractions identity mutants break 9 and 7/24 exact, m2a halved discrepancy prefactor 0.3 exact, m2b transposed aggregation matrix 37/55 exact + colsum flag, m3 overlapping sub-ladders CAUGHT, m4 synthetic one-block collapse to n_eff == 1 exact, m5a/m5b scope-flagged; smoke-stage identifier rename disclosed, no bar moved; mp dps-60 deep wards.  NO L2 lemma claim, NO RH claim.; consumed by v967 (wave 10, embedded byte-exact, smoke stage)"

_R302_STATUS = "L2 unif-target round (30/30; SPEC_SHA 36df9424; the r301 frozen rest executed: why is the block profile of |PDelta| quasi-uniform -- slope(1 + CV^2) <= sl_nact - NEED = +0.094, measured +0.039, margin 0.055 -- and can it be derived source-purely?): the exact CV^2 class decomposition, the distribution-stationarity census, the exact per-half depth attribution and three derivation routes.  VERDICT CV2_ANATOMY(between shares SIGN/BAND/PAT med 0.012/0.216/0.111 -- no sealed carrier rule fires: the mild rise is STRUCTURELESS, within-class) + PROFILE_STATIONARY(normalized pooled KS(G1,G3) 0.043 / KS(G2,G3) 0.021 / KS(G1,G2) 0.026, all far under the sealed 0.125 over a 3x depth range -- the |PDelta| block profile has ONE stable normalized distribution: CV^2 boundedness is its second moment, and the r299 pointwise-cconv negative was the wrong convergence notion, convergence in DISTRIBUTION) + DEPTH(the r301 half-ladder flag resolved: the deep-half flattening of n_eff (+0.982 -> +0.802) is carried ENTIRELY by the CV^2 head (+0.228), NOT the count (+1.030, additivity exact per half); the sealed finite-size model fires TRANSIENT_1_OVER_N (m2 group medians 2.07/2.02/2.00 fall along an exact 1/N law onto A = 1.973, held-out dev 0.002 <= 0.05, approached from ABOVE) -- DEPTH_HALF_MISS stands as an honest flag, DEPTH_CAVEAT does NOT fire; jackknife of sl_cv2p 0/42 above UNIF_NEED) + ROUTE_TABLE(B1 THE STRUCTURAL FINDING: the exact coherence identity 1 + CV^2 = n_act chi/(surv^2 n_eff_atom) with chi = D/Q the in-block coherence factor (module-own Fractions re-proof, ward <= 6.0e-16 on 47 worlds, per-block Cauchy-Schwarz cap chi <= kmax slack 0.0) -- chi med 0.630 DESTRUCTIVE and falling (-0.060), surv flat (-0.020), the lag-1 anti-correlation rho_1 = -0.22 is its atom-level mechanism; composed slope +0.039 == sl_cv2p exact (5.4e-16); B2 the local-pattern route closed honestly on BOTH clauses (PAT12 within-share 0.685 > 0.5 -- the node pattern does NOT determine |PDelta|; k-profile ks 0.181 > 0.125); B3 the localized-perturbation gain g/N med 1.079 vs the sealed damping bar 1.0 -- the recursion responds AT the polynomial-degree rate, miss 0.079 honest) + UNIF_DERIVED(B1 + A2: the sealed clause fired -- chi non-growing + stationary profile + 1/N transient + count link 42/42) + CANDIDATE_THEOREM(wave-10 candidate NOT promoted, every hypothesis typed MEASURED: the ONE remaining measured growth statement is ATOM_TARGET -- slope(n_eff_atom) >= sl_nact + sl_chi - 2 sl_surv - UNIF_NEED = +0.888, measured +0.942, margin 0.055: the block-level uniformity became an atom-level anti-concentration statement about the c-difference profile itself) + WORLD_NOTE(the coherence identity holds on 47 worlds by algebra -- world-blind as the charter demands; UNIF non-separation reproduced, MAIN 1.03 bracketed by EPST 0.72 / SCR 2.76).  Anchors bit-near (r297 sigma/sigma*, r300 participation set, r301 full set incl. orders/count-link/halves/jackknife); m1 wrong-class-weight 3/4 exact, m2 unnormalized-KS mustfail re-anchored to the relative form (a1 disclosed, original 0.335 < 0.5 printed permanently; CAUGHT 8x), m3 lag-0 double counting 5/7 exact, m4 two-point synthetic CV^2 729/196 LOUD on every route, m5a/m5b scope-flagged; smoke-stage m3 fix + a2 label reporting disclosed, no adjudication bar moved; mp dps-60 deep wards.  NO L2 lemma claim, NO RH claim.; consumed by v967 (wave 10, embedded byte-exact, smoke stage)"

_R303_STATUS = "L2 atom-target round with HARD REGRESS AUDIT (26/26; SPEC_SHA 375e9f2b; the two mandatory questions of round 303 adjudicated under sealed rules): (Q1) is the thrice-identical 0.055 margin of the r300/r301/r302 cascade ONE algebraic number?  VERDICT MARGIN_CHAIN + REGRESS_CONFIRMED: the four target margins m_D/m_NEFF/m_UNIF/m_ATOM all equal +0.0547 with invariance devs <= 9e-16 (module-own margin_chain, re-proved exact in Fractions on a rational slope set: all four margins 3/50 EXACT; the frozen halves_slope estimator is exactly log-additive over the r300/r301/r302 product identities) -- the cascade is an exact DICTIONARY around ONE measured core S = sigma* - sl_D = +0.0547 (the r299 DIAG margin), NOT three reductions; the r297 sigma level is NOT the core: sigma* - sigma = +0.1976 = S + ratio surplus (sl_D - sigma) +0.1429 EXACT, and the charter's 1/2-conversion conjecture is REFUTED ((sigma*-sigma)/2 = +0.0988 != +0.0547; the factor 2 lives only in NEED = 2 sl_L1 - sigma* and cancels in every margin difference); further reduction rounds may NOT be counted as progress on the inequality.  (Q2) does the slack follow from the lag-1 mixing structure -- the FIRST non-tautological mechanism test of the lane: sealed synthetic dc rearrangements per rung (exact marginal = bitwise multiset permutation, rho_1 steered by seeded greedy swaps to matched / zero / flipped targets, 8 replicates, 1008 builds, convergence 1008/1008, fixed points <= 0.024).  VERDICT MIXING_INSUFFICIENT with a MONOTONE mechanism ladder: chi real 0.630 -> (a) matched 0.764 -> (b) zero 1.029 -> (c) flipped 1.342; end margin +0.055 -> +0.057 -> +0.032 -> -0.044 -- flipping the mixing sign KILLS the target inequality, removing it shrinks the margin, matching rho_1 reproduces the slopes and the end margin (+0.057 vs +0.055) but NOT the destructive-coherence level (chi miss 0.134 > 0.05): the within-block structure beyond lag 1 carries the rest; BYCATCH THEOREM-GRADE FACT: n_eff_atom = L1a^2/Q is a pure MARGINAL functional (invariance 1.0e-15 on all 1008 builds) -- ATOM_TARGET's growth lives in the value distribution alone, the mixing lives in chi/CV^2/D: the r302 A2 stationarity and the mixing are complementary, not redundant.  RHO_SIGN census honest: S1 < 0 on 41/42 only (one rung positive -- the adjacent-pi orthogonality connection cannot be a per-rung theorem in raw form; Fractions-exact negative certificates on the two smallest rungs).  CONSEQUENCE (ii): the reduction cascade r297->r302 is CLOSED as a dictionary; the honest next object is the joint short-range law of the dc profile (rho_1..rho_k / within-block coherence), not another coordinate change.  Mustfails m1 wrong-1/2-factor breaks by exactly sl_L1 = 1/5 (Fractions) / m2 unmatched marginal LOUD 5.9e-1 / m3 seed collision CAUGHT / m4 swapped D/Q breaks 48/35 EXACT / m5a+m5b scope-flagged; NO amendment after freeze; mp dps-60 deep wards.  NO L2 lemma claim, NO RH claim.; consumed by v967 (wave 10, embedded byte-exact, smoke stage)"

_R304_STATUS = "L2 short-range-law round (37/37; SPEC_SHA 2cc5d23f; the reviewer contract executed under the r303 hard rule -- NO coordinate change, only the named mechanism object): (Q1) is the dc-profile anti-correlation genuinely short-range and summable?  MEASURED AND FROZEN: the centered lag profile rho_1..16 over all 42 rungs is a STABLE PERIOD-4 COMB (med -0.222/-0.140/+0.089/+0.130, then recurring strong lags at k = 4m and 4m+2 up to 16: +0.13..+0.16 at 4m, -0.14..-0.15 at 4m+2; halves-stable 3/3 sign agreement; world-specific -- EPST/SCR differ), NOT a decaying tail; the sealed short-range rule (|med rho_j| <= 0.05 for all j > k0 <= 8) finds NO k0 => VERDICT LONGRANGE_STRUCTURE + LAW_LONGRANGE (the reviewer stop case fires on the LETTER of the rule); the reviewer condition SPLITS: the net covariance NC(16) = 1 + 2 sum med rho_k = 0.712 < 1 HOLDS (net-negative) while summability-with-small-tail FAILS (SUM(16) = 1.563, no decay); the zero-sum tautology 1 + 2 sum_all rho_k = 0 for mean-removed finite profiles disclosed and gated live (F1, 3.5e-15) -- the truncated NC is the content.  THE STRUCTURAL COUNTERPOINT (F2, exact): chi = D/Q = 1 + 2 sum_k T_k/Q with T_k the within-block lag-k cross sums (recomposition ward 4.7e-16 on every non-degenerate world) shows the chi-RELEVANT structure IS short-range: real shares c_1 -0.345 / c_2 -0.139 / c_3 +0.068 / c_4 +0.028, sum(5..16) -0.026, tail(>16) 0.000 -- the long-range comb is INVISIBLE to chi; the r303 chi-level miss 0.134 is attributed to k <= 3 (dominated by lag 2: +0.181).  (Q2) does lag-k matching close the r303 gap?  LAGK_MATCH (rho_1..8 steered jointly per rung, module-own swap_arrange_k, 252 builds, convergence 252/252 at tol 0.02, marginal bitwise, natom invariance 8.5e-16): chi 0.652 vs real 0.630 -- the destructive LEVEL now reproduces (|d| 0.022 <= 0.05; the r303 rho_1-only family missed by 0.134) BUT the slopes break (sl_cv2p miss 0.028, sl_D miss 0.027, both > 0.02; margin +0.082): the exact COMPLEMENT of r303 (a) -- the mechanism is TWO-SCALE (level from the short lags, slopes from the rung-wise lag-1 trend); no lag-matching family reproduces both within the sealed bands.  The graduated reviewer ladder (absolute rho_1 targets +0.2/0.0/-0.1/-0.2/-0.3, 840 builds, 840/840 converged): chi 1.361/1.019/0.889/0.765/0.632 MONOTONE in rho_1; margin +0.036/+0.074/+0.019/+0.045/+0.059 NOT monotone -- HONEST NEGATIVE: absolute-level targets do not kill the inequality; the r303 kill (-0.044) came from per-rung FLIPPED targets: the margin responds to the rung-wise trend of rho_1, not its level.  SIGN_PATTERN: ladder med signs of S_1..4 = -/-/+/+ with Fractions-EXACT certificates on both smallest rungs (kz18, kz23: 4/4 match).  Leg 0 anchors bit-near (r297-r302 full set; margin chain +0.0547 x 4 invariance <= 8.7e-16; the r303 three-family ladder REPLICATED with the same seeds: chi 0.764/1.029/1.342, margins +0.057/+0.032/-0.044; RHO_SIGN 41/42, alt 0.523).  CONSEQUENCE (iii): the lane's global-profile mixing route is CLOSED (documented stop): L2 <=> anti-concentration of an explicit block field with LONG-RANGE (period-4 comb) structure; what survives as honest structure: the exact within-block short-range decomposition of chi, the two-scale mechanism split, NC < 1 and the exact sign pattern -- typed MEASURED, no proof target claimed on the closed route.  Mustfails m1 factor-1 net covariance 1/2 != 0 EXACT + chi decomposition 6/7 vs 5/7 EXACT / m2 unmatched marginal LOUD 5.9e-1 / m3 uncentered field 3/4 EXACT + real 0.028 / m4 family smuggle dev 0.332 > 0.02 CAUGHT / m5a+m5b scope-flagged; pre-record G32 print fix disclosed, NO amendment after freeze; seeds 2100 collision-free; mp dps-60 deep wards.  NO L2 lemma claim, NO RH claim.; consumed by v967 (wave 10, embedded byte-exact, smoke stage)"

_R299_STATUS = "L2 Fejer decay round (32/32; SPEC_SHA f432e944; the r298 gap object executed: can the decay of the Delta Fejer energy B(PDelta,PDelta) -- sigma <= sigma* = -0.516 -- be derived source-purely from position equidistribution plus a controllable signed-mass statement?): the module-own EXACT spectral representation B = (1/L) sum_k F_H(theta_k) |Dhat(k)|^2 (frozen L rule, recomposition + Parseval + magnitude-majorization wards <= 7.1e-16 on 47 worlds) plus three source-pure derivation routes.  VERDICT SPECTRUM_MAP(LOWPASS: band shares LOW/MID/EDGE med 0.93/0.04/0.02, band slopes -0.758/-0.014/-0.979, q50 med 0.19 main-lobe units -- sigma is a LOW-FREQUENCY phenomenon, not broadband) + ROUTE_TABLE(B1 ERDOS-TURAN/ABEL valid 47/47 but composed slope +1.948 FAILS sigma* by 2.464 (position/kernel factor +1.504 GROWS, Abel mass term V^2 +0.444 grows -- the r297 magnitude wall recurs at the frequency level; MASS_TARGET frozen and NOT MET by 2.464); B2 PAIR/DIAGONAL valid 47/47: sl_D -0.571 MEETS sigma* -0.516 (margin 0.055), O < 0 on 13/42 only (the PDelta pair field REINFORCES in the majority, the r287 border pattern carries over), ratio B/D med 1.29 slope -0.168 FALLING; B3 OVERLAP valid 47/47 with THE STRUCTURAL FINDING: FULL-SUPPORT overlap on 42/42 rungs -- the border and window unions share EVERY position, Delta_fresh == 0 identically: Delta IS a pure c-value difference measure on one shared node set; cconv med 0.86 slope +0.045, the relative c-difference does NOT fall -- the decay is aggregate cancellation of a non-converging difference profile, class OV_DOM) + DECAY_SPLIT(B2 DIAG_TARGET: prove sl_D <= sigma* (a magnitude-density bound on ONE positive quantity, measured margin 0.055) + ratio flatness (measured -0.168); B3 CVALUE_TARGET: prove the c-value convergence rate) + CANDIDATE_THEOREM(conditional, wave-9 candidate NOT promoted: Leg-B bound + frozen rest hypotheses => sigma <= sigma* => r297 target => v964-S0 vdC => delta' > 0.21 generic half) + CANC_LOCUS(the in-T cancellation gap G = B_abs - B is ENTIRELY low-band (1.01/-0.01/-0.00) and NOT carried by the mass blocks (sp(Mb, c_j) med -0.01, coincidence 3/42 vs the +0.69 energy coupling)) + WORLD_SENSITIVE(disclosed: the O-sign class separates MAIN (reinforcing, O_POS) from EPST/SCR (cancelling, O_NEG) -- the first world-separating sign class of the L2 lane).  Anchors bit-near (sigma -0.714 / sigma* -0.516 / D_rank 0.024 sl -0.42 / imb +0.244; r298 share 0.99, sl_MAIN -1.386, canc 1.69 sl +0.207, overlap w9 367; identity/kernel/attribution 8.8e-16/7.5e-16/5.4e-16); Fractions ET section exact (Abel resummation dev 0, position-bound equality witness, dropped-terminal 0 < 2 and halved-prefactor 2 > 1 mutants CAUGHT, v964-S0 T4 anchor); m1 wrong-Fejer-weight 2/3 exact, m2 magnitude-pair 1.3e+0/4.6e+0 LOUD, m3 tolerant-overlap-split CAUGHT with silent recomposition; amendments a1 (O-sign class into the world-blindness conjunction per the sealed spec text) / a2 (full-support overlap count print) disclosed, no bar moved; mp dps-60 deep wards.  NO L2 lemma claim, NO RH claim."

_R306_STATUS = "L2 Renyi-3 round (27/27; SPEC_SHA 3bb365e1; reviewer plan section 5 -- the sharpest new fiber attack, explicitly sanctioned as NEW information after the r304 documented stop: POINTWISE instead of slope, cubic moment instead of the closed max/discrepancy routes; contract PRIME.L2.ATOM.RENYI3.01, experiments-side, NO ledger row): prove or refute sum_j q_j^3 <= C (log m)^A / m^2 pointwise on every rung of the atomic |PDelta| profile, A in {0,1,2} preregistered, C frozen on the first 5 rungs.  VERDICT RENYI3_GO(C = 1.069, A = 2): the inequality HOLDS on ALL 57 rungs (42 core + the 15 r286 extension anchors N_w 942..1218) with GROWING reserve (trend -0.322 on both frozen estimators; deepest 15 rungs at reserve 2.6..5.7); A = 0 fails (the third shape moment M_3 = m^2 S_3 rises +0.153 before decaying -- the disclosed algebraic prior), A = 1 fails on exactly the two near-critical rungs kz53/kz67 (1.4-1.9 percent under C_2): polylog-SQUARED is the honest sharp form.  Via the exact Renyi/Hill chain (two Lagrange witnesses, Fractions dev 0; Lean-ready statement printed) the GO fixes the NEW POINTWISE PROOF TARGET of the fiber: n_eff = N_2 >= N_3 >= m/(1.034 log m) -- asymptotically above every demanded power m^0.888.  Anatomy: the cubic mass is a NARROW-BAND functional (97 percent within a factor 4 of q_max) carried ever more BROADLY (top-8 share 0.780 falling -0.268; strict triples 92 percent of the cube) -- no heavy-few obstruction; minimal sufficient statement named SHAPE3_TARGET (M_3 polylog-bounded, the third-moment sibling of the r302-proven M_2 stationarity 1.973, M_2 med here 2.03).  WORLD_SENSITIVE with the right sign: EPSTEIN holds, SCRAMBLE BREAKS the bound 1.67x -- the law is recursion structure, not block combinatorics.  Leg 0 anchors bit-near (Renyi family 37.41/27.88/24.04/15.47 at +0.963/+0.926/+0.894/+0.738; core slack S = +0.0547 dev 6.7e-16; count link 42/42 AND 15/15 on the extension).  Honest negatives: C_2 frozen on the shallowest rung, kz53/kz67 margin 1.4-1.9 percent; the GO fixes a proof TARGET, it proves nothing beyond the 57 rungs; the atom-level (dc) sibling stays unformalized.  Must-fails m1-m4 CAUGHT/LOUD (1/64 exact; prereg breach set ward + C_full/C_cal 2.10; L1^3 factor; one-atom 212x) + scope mutants flagged.  Deterministic run1/run2; NO RH CLAIM in either direction; consumed by v968 (wave 11, embedded byte-exact, smoke stage)"

_R307_STATUS = "L* fixed-head kill round (28/28; SPEC_SHA ec2bb008; reviewer adjudication section 4 solution C -- the cheapest kill test of proof architecture C (fixed head + contractive tail), deciding whether the r284 near-one-atom anatomy is descriptive or proof-relevant; contract PRIME.LSTAR.FIXED_HEAD.01, experiments-side, NO ledger row): in the mu-orthonormal frame E = E_H + E_T with H = the first r FLAT ARCHIMEDEAN EDGE atoms below the first prime (u < log 2); two sealed window-fixed orderings (ORDER_FOLD ascending fold; ORDER_W9X = the frozen w9 extremal rank permutation, regated exactly); lambda_max(E_T(r)) measured for r = 0..16 on 77 windows (42 core + 15 r286 anchors + 20 NEW deeper windows N_w 1218..1650, S up to 3299).  VERDICT HEAD_GROWS: NO fixed r <= 8 exists (best candidate min reserve 6.54e-6 at r = 8 FOLD, four decades below the sealed 1e-2 bar; a fixed r_min <= 16 exists on 15/77 windows only, all N_w <= 434; sp(reserve(8), S) = -0.93 with TS slope -3.15 == the r286 margin-law class: removing a FIXED head changes the prefactor, not the decay class) BUT the FULL edge (13..96 atoms, GROWING with the window, sp(edge, N_w) = +0.98) restores a macroscopic reserve on 77/77 (min 2.19e-3, median amplification 3.1e4): the near-one-atom anatomy is REAL and proof-relevant AS A COORDINATE, refuted AS A FIXED DIMENSION -- architecture C in its fixed-head form is dead; the honest successor object is the window-dependent head of size ~ log2/(2 Delta_w), whose own reserve decays slowly (TS -0.87, disclosed).  SCHUR_LEDGER exact: det(I - E) = det(I - E_T) det(S_H) worst 3.4e-8 on 57/57 at r = 8 (rational-EXACT on the JF9 toy: S_H = 5079569347/6986834571); border-augmented identity det(I - E_T) det(S_aug) = det(I - E) D_N worst 2.1e-6 with D_N = (5/7)(1 - q_N) from the INDEPENDENT r244 bordered-chain route (q_N < 1 on 57/57, min gap 0.0195, r286 reproduced; the Christoffel W-identity t^T (I - E)^{-1} t = sum rho gated 4.4e-13 on w9 and exactly on the toy); lambda_min(S_H(8)) > 0 on 57/57 BUT == the wall margin to 4 digits and anchor-MONOTONE (sp -0.92, TS -3.33) along the r286 margin decay -- the hoped-for simplification is EMPTY: S_H carries the whole problem; the border is inert (S_aug positive 57/57, degradation factor >= 0.873 -- BORDER_BREAKS_HEAD did not fire).  TWIN_METRIC_OK (r289 rational twin verbatim: fold sets == MAIN, r_min 3/3 == 3/3 both orders, max |dreserve| 1.0e-7 over r = 0..16 -- diophantine input irrelevant on the head coordinate).  CONTROL_COLLECTIVE (EPST lambda 2191 -> 2189 at r = 16, SCR 1.4e7 -> 3.2e4: no small head rescues a dead world -- the architecture reads MAIN-specific structure).  Tail anatomy: after edge removal the tail rides its own near-single-atom Christoffel profile on the bulk atoms (maxdiag 0.862..0.992, gain <= 1.089); Gershgorin/Schur-test row sums 1.5..3.6, < 1 on 0/57 -- the classical bounds stay dead on the tail.  Structural exactness: reserve monotone in r + interlacing lambda_max(E_T) <= lambda_max(E) EXACT on 77 x both orders (sign safety inherits from the r286 mp-verified margins); mp spots 3/3 at dps 30 (worst rel dev 2.8e-14).  Must-fails: m1 target-inverse ordering AST-FLAGGED (ordering constructors clean of eigensolvers) / m2 Woodbury wrong sign breaks the det identity 0.163 LOUD / m3 monomial frame hides the toy wall (4.36 -> 0.85, rel 0.805) LOUD / m4 r = 0 degenerate exact.  Four pre-spec sizing scratches disclosed in the spec (they saw the likely outcome; bars sized before freeze, no rule tuned after any evaluation).  Deterministic run1/run2; NO L* claim, NO RH CLAIM in either direction; consumed by v968 (wave 11, embedded byte-exact, smoke stage)"

_R308_STATUS = "L* block-Green DISCOVERY round (30/30; SPEC_SHA d5147850; reviewer adjudication par.4 solution A, plan round '305': automated search for a matrix-valued discrete Green identity on fourfold fold blocks -- the route replacing the failed scalar profile functionals (r290-r295), the cancellation-losing absolute-value majorants (r297/r299/r300) and the irrelevant diophantine relations (r289 METRIC_ONLY); experiments-side, NO ledger row): does the augmented form Q(p,t) = int p^2 d(mu-nu) + 2t u(p) + B t^2 (v958 bordered object, B = S_{N-2} + 5/7) admit an EXACT decomposition Q = sum_r Delta_r^T G_r Delta_r + (5/7)t^2 with sealed fourfold-block coordinates (first/second differences, the r288 antiphase layer_i - layer_{i+2} coordinates, local gross-mass mean, border t) and source-pure blocks G_r?  VERDICT IDENTITY_EXISTS + BLOCK_INDEFINITE_MAIN + FEAS_DIAG world separation + CONTROL_LEDGER + R282_DEMARCATION: the identity EXISTS everywhere (exact Fractions with entrywise reconstruction on TOY4-hand/SM0-SM3/MINI16, dof 15..219; f64 residuals 4.0e-14..8.1e-14 on w9, the r289 rational twin, EPST/SCR/SMOOTH and all 57 rungs at DEG_A = 8; kernel exclusion 100 percent) -- existence is the disclosed EASY half (linear in G, hugely underdetermined); the sealed eigenvalue-free minimum-Frobenius selection is indefinite EVERYWHERE (even on the positive-class SM0: the SELECTION, not the world, produces indefiniteness; w9 -1.3e-02 rel, 199/364 negative blocks) => BLOCK_INDEFINITE_MAIN on the letter of the sealed rule; THE ROUND'S CENTRAL MEASUREMENT (sealed diagnosis clause, amendment a1 calibration-stage: uniform two-stage Dykstra schedule 200/2000 for every world): the SDP-like feasibility census SEPARATES THE WORLDS -- w9@DEG_A and twin@DEG_A converge to GENUINELY ALL-PSD block families (min eig rel +6.6e-16 / +2.0e-17 at affine residual 3.7e-14, 200 steps) while EPST/SCR stall at -0.45/-0.49 after 2000 steps: on the restricted DEG_A subspace, where every world's target is positive definite and NOTHING is theorem-forced, MAIN and its diophantine-trivialized twin admit an all-psd fourfold-block Green decomposition and the two hard controls (at this schedule) do not -- the first block-level world discriminator of the L* lane, ONE-SIDED (non-convergence proves no infeasibility) and diagnosis-grade only; SMOOTH@A marginal (-1.3e-05, its crossing 28 == DEG_B boundary role); w9/twin@DEG_B = 28 stay OPEN (-4.2e-05 after 2000).  DEG_B disclosure: control crossings 26/22/28, so control negativity at DEG_B is FORCED by theorem given existence -- gated live on EPST/SCR (held), never sold as discovery.  Anchors: w9 367/263/104, crossing 185; r288 carrier pin z_v -3.149 destructive; r282 pin N_2(MAINLIKE) exact; B_w9 = 8.368649 with 182 nonnegative rho_k.  R282 demarcation: the Kasteleyn/SOS refutations concern the FULL signed configuration class (every cell, h_n itself); this identity lives on the RESTRICTED subspace deg p <= 8/28 << N_w plus border -- different language, no contradiction.  Must-fails: cholesky-of-target FLAGGED, omitted remainder breaks by EXACTLY 5/7 at (t,t), posthoc family FLAGGED, partial coverage exact defect 4.5e+01 LOUD.  Honest: a feasibility census fixes a TARGET (find a sealed CONSTRUCTIVE psd G rule on MAIN, extend to DEG_B, prove the world split), it proves neither L* nor any cofinal statement.  Deterministic run1/run2; NO RH CLAIM in either direction; consumed by v968 (wave 11, embedded byte-exact, smoke stage)"

_R309_STATUS = "L* paired-cone PILOT round (33/33; SPEC_SHA f8d99877; reviewer adjudication par.4 solution B / plan round 306 -- the third full proof architecture: positive and negative source processed PAIRWISE as rank-one updates of the augmented form, base and border together; contract PRIME.LSTAR.PAIRED_CONE.01, experiments-side, NO ledger row): the r308/v958 augmented form A = [[H, u], [u^T, B]] is rebuilt EXACTLY as an ordered signed rank-one stream (sealed base = 5/7 t-floor + reserved/unmatched mu atoms; one signed budget step |S_{N-2}|; nu atoms greedy-matched to their nearest free mu partner; every border atom split exactly into a +/- pair), and at every negative step the reviewer reserve r = 1 - L_bb + L_ab^2/(1 + L_aa) is measured -- the Sherman-Morrison cancellation as an EXPLICIT POSITIVE SQUARE, with the det dictionary det(M1) = (1 + L_aa) det(M), det(M2) = r det(M1) exact on the toys (hand toy PC4: reserve 7/9, dets 9/14 -> 27/14 -> 3/2) and f64-warded on w9 (recon 4.8e-16, mp ward dps 60 dev 3.0e-13).  VERDICT DECOMP_EXACT + MAIN_RESERVE_POSITIVE + CONE_PARTIAL + WORLD_DISCRIMINATOR(all three sealed stats WORLD_BLIND) + MUSTFAIL_LEDGER: MAIN survives the ordered chain at BOTH caps with macroscopic margin (w9 min r +0.9011 at DEG_A = 8 / +0.3232 at DEG_B = 28; the r289 rational twin bit-near; 57/57 ladder rungs all-positive, min +0.7357@kz97) and w9's two tightest pair reserves sit EXACTLY on the r284 extremal folds {2, 4}; the reviewer's decisive cone question SPLITS: the sealed mass-ratio cone r >= 1 - c_1 v/w_a (c_1 = 8.5436 frozen on the 5 shallowest rungs) is SOUND -- ZERO violations on all 20714 pointwise test steps (52 rungs + w9 + twin) -- but certifies only 56 percent of the steps (bounds > 0 on 11643/20714), while the sharper local shield cone r >= 1 - c_2 v/SM2 overshoots exactly where it is positive (54/54 positive bounds violated, every violated step has true r >= +0.901): the reserve is PREDICTABLE in the sound direction from one source quantity but no sealed local phi is yet a certificate -- the named successor object is a phi with a base-depth term (the DEG_A base carries most of the reserve; not retro-fitted); the info test is SILENT by the sealed letter (pooled tightest decile best |sp| 0.50 at pair distance; on w9 alone the mass-ratio/shield features reach -0.61/-0.58, reported) and the reviewer-B4 O(log N) fold-bit register is measured IRRELEVANT at this cap (max |sp| 0.32).  Honest world census: at DEG_A the ordered PAIR reserve is WORLD-BLIND (controls' pair phases all positive, EPST +0.5712 / SCR +0.7796 / SMOOTH +0.9627); the ENTIRE EPST/SCR indefiniteness at DEG_A is the negative BUDGET step (S_{N-2} = -3.992 / -5.237 past the flip -- the r243 budget coordinate reads the wall, amendment-a1 disclosure: the design-time 'every DEG_A target is PD' sentence was corrected, spec-prose + reporting only, no bar or rule moved); DEG_B control breaks forced by theorem, disclosed (EPST/SCR budget step; SMOOTH boundary -7.08 at pair step 4).  Anti-circularity at r275 sharpness: the o1/o2 + forced-tail-sum pin re-run exact; target-inverse cone mutant (Minv_true) and posthoc-pairing mutant (r_true) FLAGGED by the AST scope audit; wrong-sign Sherman-Morrison caught by the exact det dictionary (dev 8/9 EXACT); order-break mutant changes the reserve by EXACTLY 4/9 while the reconstruction stays exact (the r-sequence, not the sum, is the ordered object).  Honest: a passing cone fixes a TARGET for proof work; this round proves neither L* nor any cofinal statement.  Deterministic run1/run2; NO RH CLAIM in either direction; consumed by v968 (wave 11, embedded byte-exact, smoke stage)"

_R311_STATUS = "L* block-Green NONTRIVIALITY round (34/34; SPEC_SHA fac7a8df; the reviewer's MANDATORY round before any constructive G-search; contract PRIME.LSTAR.BLOCKGREEN.NONTRIVIALITY.01, experiments-side, NO ledger row): is the r308 psd block family stronger and more local than Q >= 0, or a sparse-Gram/chordal restatement whose SDP separates the worlds by force?  VERDICT STRICT_SOURCE_CONE (with the binding SEPARATION MECHANISM clause) + SPAN_LEDGER + SIGN_EQUIVALENCE_LEDGER + R308_DEMARCATION -- BOTH reviewer scenarios are true at once, on different layers: (1) THE r308 WORLD SEPARATION IS FULLY THE BUDGET SIGN -- the sparsity graph of the Delta coordinates (band-3 atom cliques + universal border vertex t) is CHORDAL on every size incl. the full w9 S=367 graph (MCS + Tarjan-Yannakakis, maximal cliques == the 364 sealed blocks; C4/C5 control non-chordal), each block spans its full local R^5, so on EVALUATION space the image cone is exactly the chordal pattern-psd cone (Agler et al./Grone et al. -- restatement there); the control targets A_sys are INDEFINITE at DEG_A through the one negative budget diagonal (EPST -3.992 / SCR -5.237, the r309 amendment quantified: lambda_min rel -0.86/-1.00 vs w9/twin +8.4e-4 PD), so the r308 Dykstra separation was theorem-forced; the trivial common dual Y_t = e_t e_t^T (ONE rational entry -- the r243 budget positivity S_{N-2} >= 0, the KNOWN wall reading) closes the r308 one-sided stalls two-sidedly, predicts the two NEW blind scramble worlds 2/2 (seeds 2/3, S = -6.20/-6.15, both stall), and the DECISIVE ablations seal it: EPST/SCR with (t,t) <- |S| become PD and the Dykstra CONVERGES (+2.5e-16 / -5.1e-11), w9 with the EPST budget transplanted dies (-0.449) -- flip ONE scalar and the separation inverts; the exact SCHUR-TAIL LEMMA (s(A_sys@cap d) = S_{N-2} - sum_{k<=d} F_k^2/h_k, exact on SM0/SM1) shows the wall sign enters the target mechanically as the budget rho-tail, and decides all four r308 small-model OPEN stalls as trivially target-indefinite (even the positive-class SM0: s = -(rho_3..rho_8) = -7.08e-2 EXACT); SMOOTH's marginality is a BOUNDARY target (S = +3.48, lambda_min rel +2e-16).  BUT (2) THE CONE IS GENUINELY STRICT on the compressed subspace -- the round's second discovery: 0/16 sealed random in-span PD samples decompose (w9A 0/6, MINI16 0/6, SM1 0/4; staged Dykstra 200/2000/20000), every MINI16/SM1 stall carries a VALID polished-numeric Farkas dual (worst compression -1e-16..-1.4e-8 at <Y,Q> = -1), and MINI#0 + SM1#0 carry FULLY EXACT in-span rational certificates (exact Chebyshev basis, den 1e6, d = 1e-6, <Y,Q> < 0 exact rational; MINI16 = the real-w9 miniature with EXACT full span rank 55/55) -- C_w is STRICTLY smaller than span cap S_+: block membership is a genuinely stronger property than positivity, which MAIN + twin HAVE at DEG_A and generic positive forms LACK; the ambient span layer is also exact (codims TOY4 0 / SM0 11 / SM1 11 / SM2 2 / SM3 1 / MINI16 0 / w9A 4 / w9B 236, exact annihilators with all compressions zero, SM1 rank-one ambient counter-model with exact rational Farkas).  Protocol audits: r308 feas_diag AST-clean (objective-free, no target spectra), start ablation clean (zero start converges, random start -8.5e-9 at the amended 1e-8 bar; EPST stalls from every start).  w9@DEG_B stays honestly OPEN (PD-thin +2.4e-6, -1.78e-5 after 20000, dual diverges -- one-sided).  Consequence: the planned R312 rank-one-conductivity round premised on the r308 world discriminator is DEAD in that form (the discriminator was the wall sign); the re-scoped GO object is cone MEMBERSHIP (why the bordered-Hankel world targets sit inside the strict cone while generic PD forms do not).  Must-fails: wrong-sign Farkas rejected exact / wall-z FLAGGED / wrong-graph + C4/C5 caught / eigvecs_target sampler FLAGGED.  Three disclosed calibration amendments (dual divergence guard + sealed stage-3 consistency; START_NEAR bar; certificate bookkeeping + exact-Chebyshev-basis certification -- the four-way verdict selection rule never moved).  Deterministic run1/run2; NO L* claim, NO RH CLAIM in either direction; consumed by v968 (wave 11, embedded byte-exact, smoke stage)"

_R312_STATUS = "L* block-Green MEMBERSHIP round (32/32; SPEC_SHA 6c32f749; THE ONE construction round granted by the reviewer tree after r311's STRICT_SOURCE_CONE; contract PRIME.LSTAR.BLOCKGREEN.MEMBERSHIP.01, experiments-side, NO ledger row): does a source-pure constructive rule write down an explicit psd block family G_r = sum_l c_{r,l} v_l v_l^T (c >= 0) for the bordered-Hankel world targets, over the VORAB-sealed 22-generator library in the D basis (fold distances 1/2, antiphase 3/4, the r307 arch coordinates, border-vs-interior pairs D_a +- D6, symmetric/antisymmetric four-block modes), with an explicit coefficient formula c_{r,l}(source quantities)?  VERDICT COEFFICIENT_SIGN_WALL + MEMBERSHIP_ANATOMY + W9B_STATUS(OPEN) + R311_DEMARCATION -- the library SPAN carries the w9 identity exactly (unconstrained rel 2.4e-13; abstract span 15/21 exact) but the CONE does not: deterministic Lawson-Hanson NNLS stalls at rel 4.7e-4 (support 35, not capped) with a VERIFIED I-polished Farkas certificate (delta 1e-4, min normalized column product +9.7e-5, <y,q> = -0.9975), and the certificate mass localizes on the border/budget row (t-row fraction 0.58254 >= WALL_FRAC 0.5; at deg 28 even 0.725) -- the identity forces negative coefficients exactly on the wall coordinates: the sign question of the c IS the wall in the constructive language too; twin type-identical (METRIC_ONLY holds); EXACT GRADE on the miniatures: SM1 and MINI16 carry FULLY EXACT I-polished rational Farkas certificates (den 100, delta 1/10000, <Y,q> = -0.9988 / -1.0000 exact rational < 0, all 154/286 exact column products >= 0), and on SM1 even the library SPAN fails exactly ([M_lib | q] rank 41, EXISTS FALSE -- the sharpest small-model form of the wall); rung census 1/57 NNLS-feasible (worst rel 8e-4 at kz12) -- the sign wall is uniform across the ladder; the four sealed formula candidates PHI_A..PHI_D (masses, tent fractions, budget share, per-type table; calibrate-on-w9 / freeze / verify-on-57+twin) never fire (best calibration rel 7.7e-3 = PHI_D >> FORM_BAR 1e-8).  MEMBERSHIP ANATOMY (the round's discovery): the converged r308 Dykstra family on w9@A is high-rank {rank3: 17, rank4: 79, rank5: 268} and library-ALIGNED (top-eigvec alignment med 0.9973) with library-cone share med 0.976 -- 97.6 percent of the psd family lives in the sealed rank-one cone and the WHOLE membership obstruction sits in the remaining 2.4 percent of SDD-forbidden negative cross mixtures; dual anatomy of the 10 r311 sample duals: the generic-missing directions are low/mid-degree INTERIOR mass (|z_t| med 0.000 max 0.087, dominant degree indices 1..6), not border mass.  w9@deg28 stays honestly OPEN, two-sidedly hardened (staged anchor -1.784e-5 == the r311 record; library NNLS@B infeasible, same wall class; +80000 extension steps improve only -1.78e-5 -> -7.66e-6, a slow tail consistent with asymptotic feasibility, NOT decided; strengthened dual POCS at OMEGA 0.1 / 8000 iters runs but polishes invalid = no certificate).  Leg 0 bit-near on the identical rng stream (0/6 + 0/6 + 0/4 strictness, 10/10 polished duals, both exact certificates -0.9999977 / -0.9999930, Y_t values, chordality 364 cliques == blocks).  CONSEQUENCE (sealed reviewer tree): NOT a GO -- lane A closes as cone language with the membership mechanism NAMED (block-psd membership WITHOUT rank-one-SDD membership, obstructed at the budget/border sign), resources move to the fiber.  Must-fails: eigvecs_target library mutant FLAGGED / negative-c REJECTED loud / log-relation consumer EXPOSED by the MAIN-vs-twin comparison (0.886 >= 0.3) / exact recomposition break CAUGHT.  Two disclosed calibration amendments (a1 f64 I-polish certificate bookkeeping, the twin of the sealed exact I-polish; a2 the m3 harness probes the r289 rationalization variable u/Delta) -- the four-way adjudication tree never moved.  Deterministic run1/run2; NO L* claim, NO RH CLAIM in either direction; consumed by v968 (wave 11, embedded byte-exact, smoke stage)"

_R313_STATUS = "L2 Renyi-3 proof-form FORK round (32/32; SPEC_SHA 6505dd10; reviewer plan: triple incidence vs four-step Floquet -- two sealed proof architectures for the r306 pointwise cubic law sum q^3 <= C (log m)^A / m^2, executed side by side; contract PRIME.L2.RENYI3.PROOF_FORK.01, experiments-side, NO ledger row; reviewer instruction binding: the universal constant may be COARSER than the r306 sharp 1.069, and the theorem must not depend on von-Mangoldt arithmetic -- sought class RecursiveDifferenceProfile with MAIN + EPSTEIN in, SCRAMBLE out).  VERDICT BOTH_PARTIAL(named remnants): (R3A -- triple incidence) the raw atomic presentation is EXACT (P_j = sum of local c-differences; fold groups = beta/omega pairs at one position; block ward 3.9e-16 on 61 live worlds) and the cube splits EXACTLY into T1 diagonal / T2 two-equal / T3 near (shared fold) / T4 far (fully separated); med signed shares +0.38 / +2.15 / -1.14 / -0.42 -- the types CANCEL against each other, they are not independently small; proof hope (i) is EXACT (fold multiplicity UNIFORMLY 2 on 57/57 -- the class bound MULT_CAP = 2 is structural) and hope (iii) is REAL (TC_far med 0.069, the far triples telescope away 93 percent of their abs mass, falling); per-type prereg at A = 2 (first-5-frozen C): T2 HOLDS 0/57 (C 1.910, trend -0.400), T3 HOLDS 0/57 (C 1.053, trend -0.299), T1 FAILS 2/57 (kz55 2.54x, kz53 1.70x, trend -0.122) and T4 FAILS 1/57 (kz55 1.84x, trend -0.186) -- shallow-calibration artifacts of the r306 A <= 1 kind (trends fall), but the sealed rule stands: COMPOSITION REFUTED-IN-FORM; world census: SCRAMBLE violates exactly T2 (2.85x) but EPSTEIN also violates T2/T3 while its TOTAL holds the r306 bound -- MAIN-frozen per-type constants are NOT world-portable.  (R3B -- four-step Floquet) the local transfer step is REAL and EXACT (r_{k+1} = t_k + ap_k r_k + bp_k r_{k-1}, ward 8.0e-13/1.9e-12/6.6e-14, SMOOTH deg-skipped; det dictionary 4.4e-16) but the four-step monodromy on the split cubic mode space EXPANDS: med sr 1.0600, contracting rungs 0/57, product exponent +1.917 vs required -2.0 -- after r304 (single step) and this round (period-4 Floquet) NO transfer-operator contraction form of the cubic law remains open at the chain level.  CLASS finding (the sharpest honest negative): the sealed four-block comb property P4 excludes SCRAMBLE but ALSO EPSTEIN; every other sealed candidate (P1 fold, P2 recursion, P3 multiplicity, P5 mass, P6 assignment, CP4 telescope) is world-BLIND -- NO boolean property separates worlds the way the r306 total bound does: the separation lives in the SIZE of the type terms, the class needs a QUANTITATIVE membership functional; the m4 shuffle instance is rejected by P6 (293/300 atoms outside their interval) while mass conservation still holds on it.  Anchors bit-near r306/r304 (C-table 11.875/3.564/1.069, A2 0/57 + trend -0.322, comb -0.222/-0.140/+0.089/+0.130, NC(16) 0.829).  Must-fails m1 double-diagonal break == 3 S3 EXACT / m2 unsplit conservation mode toy break 1/2 EXACT (live clause vacuous, disclosed) / m3 magnitude telescope toy break 1 EXACT + real dev 9.4e-1 / m4 shuffle rejected / m5a+m5b scope-flagged; two disclosed smoke-stage code fixes (degenerate-guard extension, mass denominator), one reporting edit -- no bar or rule moved.  Deterministic run1/run2; NO RH CLAIM in either direction; consumed by v968 (wave 11, embedded byte-exact, smoke stage)"

_R314_STATUS = "L2 signed-cubic-flux round, part 1 -- EXACT ALGEBRA ONLY (29/29; SPEC_SHA 841b3196; reviewer contract after the r313 adjudication: not a better triple class but the SIGNED CUBE BOOKKEEPING -- with x_j = (PDelta)_j, sigma_j = sign(x_j), expand |x_j|^3 = sigma_j x_j^3 over the r313 fold genealogy into the signed cubic tensor C_{abc} = sum_j sigma_j x_{j,a} x_{j,b} x_{j,c} and decompose C_cube = DeltaF + C_collision + C_boundary; contract PRIME.L2.RENYI3.SIGNED_CUBIC_FLUX.01, experiments-side, NO ledger row; quantification deferred to R315/R316 by contract).  VERDICT SIGNED_CUBE_IDENTITY with a VANISHING boundary: sum_j |x_j|^3 = DeltaF + C_collision + C_boundary holds EXACTLY -- on w9 decided in EXACT Fractions on the real data (35 blocks / 150 fold groups: brute tensor enumeration == Newton aggregates == flux telescope with every dev the rational number 0; Fraction(float) is exact on dyadic f64 atoms) and to 4.5e-17 in f64 on all 57 rungs + mains + EPST/SCR (bar 1e-13).  THE DIVERGENCE FORM IS LOCAL: far triples enter as telescoping edge fluxes dF = 3 G (s1^2 - s2) consuming only the transported prefix state (s1, s2) along the position-ordered fold groups (telescope Newton-vs-path worst 4.1e-16); the opening-flux lemma F_1 = G^3 - 3 G G^2 + 2 G^3 == 0 is cubic algebra, so C_boundary == 0 -- the sealed language class closes WITHOUT remainder (disclosed: the razor acts before the genealogy; an unmasked presentation would re-introduce a boundary term).  THE COLLISION SPACE IS EXACTLY COUNTABLE by the banked r313 multiplicity-2 asset: config counts full/pair/far == n / 3n(n-1) / n(n-1)(n-2) (sum n^3) and atom-triple count 3 p1 p2 - 2 p3 == 8(n + 3n(n-1)) EXACT on 61/61 live worlds (w9: 150 full / 1656 pair / 1770 far configs, 14448 collision atom triples).  MEASURED PREVIEW for R315/R316 (labeled, no bound claim): med signed shares DeltaF -0.4226 (falling -0.422), C_pair +0.5980, C_full +0.8537 (rising +0.213) -- the two collision terms together (+1.45) carry the cube against the negative far flux; flux cancellation FC med 0.629 falling -0.141; world table w9 -0.452/+0.823/+0.629 FC 0.617 / w13 -0.541/+0.430/+1.111 / EPSTEIN -2.695/-2.652/+6.347 FC 0.101 / SCRAMBLE -0.171/+0.856/+0.315 FC 0.693; SCRAMBLE localization census names the FULL-collision column (dev 0.63 vs MAIN med) -- but EPSTEIN sits far from MAIN in every share while holding the r306 total bound: single shares do NOT separate worlds, Phi_3 must combine the divergence-form STRUCTURE (sealing discipline: R315 defines Phi_3 from structure, NOT from these record tables).  Anchors bit-near r313 (type shares +0.3808/+2.1542/-1.1442/-0.4226, TC_far 0.069/-0.050, fold multiplicity == 2 on 57/57, block ward 3.9e-16).  Must-fails: m1 sigma dropped, toy break 2 EXACT + w9 dev 1.8e0 LOUD / m2 double-counted fold group, breaks 2 and 98 EXACT + w9 4.6e-1 CAUGHT / m3 unordered support, per-edge break (0, 108, 108) EXACT with the total permutation-blind disclosed + w9 edgewise 7.7e-1 LOUD / m4 mult-blind count, break 56 EXACT (8 vs 64) + w9 8.75e-1 CAUGHT / m5a+m5b scope-flagged.  ONE disclosed reporting-only edit after smoke (m3 print format); no bar, band, rule or verdict rule moved.  Deterministic run1/run2; nothing here bounds anything -- part 1 is bookkeeping only; NO RH CLAIM in either direction; consumed by v968 (wave 11, embedded byte-exact, smoke stage)"

_R315_STATUS = "L2 signed-cubic-flux round, part 2 -- THE Phi_3 MEMBERSHIP FUNCTIONAL (29/29; SPEC_SHA 92d35a3a; reviewer contract part 2: define Phi_3 IN ADVANCE from the r314 divergence-form STRUCTURE, normalized to the Renyi-3 scale NORM = m^2/((log m)^2 L^3), and run the blind world test; contract PRIME.L2.RENYI3.SIGNED_CUBIC_FLUX.01, experiments-side, NO ledger row).  THREE SEALED CANDIDATES: Phi3a = NORM(|COLL| + |BND| + |DFLUX|) [reviewer raw], Phi3b = NORM|COLL| [combined signed collision sum], Phi3c = NORM|COLL|*FCIX [flux-corrected]; honesty conditions machine-audited (AST identifier scan: no cubic-target read-back; sealed literal scan: no r314 world-table number in any builder -- the e1/e2 mutants prove both audits bite); the literal |cube - DeltaF| form is adjudicated READ-BACK-ADJACENT and demoted to a diagnostic column (== Phi3b to 1.6e-15).  VERDICT PHI3_ALL_BLIND on the sealed letter: no candidate passes all four reviewer criteria -- C0 a/b/c = 2.6261/1.5052/0.9400 (first-5 freeze, r306 protocol); K3 boundedness FAILS 2/57 on all three candidates and K2 world-rank FAILS, and the ENTIRE failure sits on kz55 + kz67 (a 4.61/2.73, b 2.55/1.89, c 2.43/1.73; kz55 alone tops SCRAMBLE 2.39 and blows the b/c bands 66/88 vs bar 30) -- the SAME near-critical family as r306 A<=1 and the r313 T1/T4 constants, with every trend FALLING (-0.40..-0.77): a shallow-calibration artifact of the known kind, but the mid-ladder rule was not sealed and is not applied post hoc.  The LOCAL CAUSE is named by the probe's own coordinates: kz55/kz67 carry FCIX 0.955/0.915 vs med 0.629 -- exactly the rungs where the intra-block flux cancellation DIES (the R316-relevant discovery: the FCIX -> 1 stratum is the obstruction, and FCIX is source-pure and computable in advance).  What HOLDS of the reviewer table: EPSTEIN holds all three frozen bounds (2.3545/1.3615/0.1375 <= C0; Phi3c separates it 7x downward via its world FC 0.101), the rational twin w13 is near-identical to w9 (factor 1.10/1.07/1.17 <= 3.0 -- the strongest twin result of the lane), the SCRAMBLE cause is named COLL (component devs dflux 1.33 / coll 3.69 / fcix 0.10, K4 fires), and candidate a passes its band bar 22.85 <= 30.  Leg C contrasts both fired: the multiplicity-3 control (first atom of every mult-2 fold group split into two half atoms -- G1/blocks/positions/mass preserved BITWISE, dev 0.0) breaks the collision count bound 48762 vs 14448 (uniform toy 216 vs 64, break 152 EXACT) and is rejected by the cap while Phi_3 is provably BLIND to it (the multiplicity cap is a necessary CLASS side condition, disclosed); the assignment shuffle (seed 315001, r313-m4 base) is rejected 289/300 with the flux profile broken edgewise 1.0e0 and mass matched 4.0e-17.  Anchors bit-near r314/r306 (shares -0.4226/+0.5980/+0.8537, FC 0.629/-0.141, mult == 2 on 57/57, identity wards 4.5e-17, r306 C_2 1.069 with 0/57).  Must-fails: e1 cubic read-back AST-CAUGHT / e2 r314-table calibration literal-CAUGHT / e3 mult-2-built control ACCEPTED as normal (sharpness 14448 == 14448) / e4 wrong normalization exponent LOUD (factor m = 35 exact) / m5a+m5b scope-flagged.  NO amendment after freeze except the record-table insertion.  Deterministic run1/run2; honest: ALL_BLIND stands -- the divergence-form structure with first-5-frozen constants is NOT the membership functional; the kz55/kz67 + FCIX-stratum diagnosis is post-hoc census, no rule; nothing here bounds anything; NO RH CLAIM in either direction; consumed by v968 (wave 11, embedded byte-exact, smoke stage)"

_R316_STATUS = "L2 signed-cubic-flux round, part 3 -- THE TWO-REGIME BOUND (35/35; SPEC_SHA 5c28b12b; reviewer contract part 3: formulate the pointwise Renyi-3 bound as a coupled two-regime statement over the source-pure FCIX stratum with theta = 0.85 sealed from the r315 record gap and a MID-LADDER calibration sealed in advance (CAL_START = n//3, N_CAL = 5, small-m ranks certified individually); contract PRIME.L2.RENYI3.SIGNED_CUBIC_FLUX.01, experiments-side, NO ledger row).  FOUR SEALED REGIME MAJORANTS, all >= rho_2 by exact algebra warded live (worst slack 6.5e-16 on 69 worlds): PhiL2 = NORM(|COLL|+|BND|+FE) [flux-index form], PhiL1 = NORM(|COLL|+|BND|+|DFLUX|) [r315 raw], PhiH2 = NORM(CNT3+|BND|+FE) [the multiplicity-2 collision COUNTING majorant, CNT3 = sum_j (n_j+3n_j(n_j-1)) gmax_j^3], PhiH1 = (m QMAX/log m)^2 [concentration]; purity machine-audited (AST + record-literal scans; e1 theta-posthoc, e2 cubic read-back, e2b literal calibration all CAUGHT).  VERDICT TWO_REGIME_DEAD(L fails; H fails) on the sealed letter -- and the anatomy is the round's find: (1) the FCIX stratum is NOT the near-critical family: the mid-ladder freeze is killed on the regime-L side by kz53 (rho_2 1.049 with BULK-NORMAL FCIX 0.654) and deep spikes kz83/kz105 -- the obstruction family cuts ACROSS the flux-cancellation stratum; (2) rho_2 itself is not below its mid-ladder window (kz53 1.049 / kz83 0.779 vs cal-window max 0.458): ANY tight pointwise majorant fails at kz53 under a mid-ladder freeze -- the r306 first-5 protocol was not a shallow-calibration artifact but load-bearing (the profile is non-monotone with recurring near-critical spikes); (3) the REGIME-H MECHANICS OBJECT delivered as census: the FCIX outliers kz55/kz67 are near-ONE-BLOCK worlds -- TOP1 cube share 0.558/0.785 vs 0.18 regime-L med (dev 2.68, the named discriminator; kz55 additionally 10x compensation kappa 0.105); concentration (candidate i), not counting tightness (dev 0.53), distinguishes them -- but kz67 misses the mid-window H constants by 1.4x/2.6x and kz55 fell into the small-m set (rank 20/65), so the H test stratum was ONE rung.  What HOLDS: anchors bit-near (r314 shares/FC/mult, r315 C0 2.6261/1.5052/0.9400 + FCIX outliers 0.955/0.915, r306 C_2 1.069 with 0/57); EXT2 extension clean (8 deep anchors to N_w 1393, all mult 2, NO new H member -- the FCIX stratum did not grow with depth); the 21-rung small-m certificate table (C_small 1.0694 = the r306 shallow maximum); the class machinery intact (EPSTEIN/twin/main admitted, twin band 1.04 = the strongest of the lane, SCRAMBLE rejected via COLL attribution 3.69 + edgewise flux break 290/300 with matched mass, mult-3 control rejected via cap with all four majorants provably blind).  Must-fails: e1 AST+toy CAUGHT / e2 AST-CAUGHT / e2b literal-CAUGHT / e3 split overlap 1 EXACT vs sealed 0 / e4 mult-3 cap + count break 48762 vs 14448 / m5a+m5b flagged.  NO amendment after freeze except the record-table insertion.  Deterministic run1/run2; R317 direction typed census-grade: the regime coordinate must capture the near-critical family itself (TOP1/QMAX separates kz55/kz67; kz53 needs a second coordinate) or the spikes become a certified exception family (r287-F2 pattern); nothing here bounds anything; NO RH CLAIM in either direction; consumed by v968 (wave 11, embedded byte-exact, smoke stage)"

_R317_STATUS = "L2 exception-families round -- reviewer fork (b): THE EXCEPTION-FAMILY CENSUS (38/38; SPEC_SHA 04fbe5c0; reviewer contract after the r314-r316 trilogy: the statement form 'all sufficiently large generic windows + explicitly classified exception FAMILIES', with the HARD GATE sealed in advance -- at most TWO source-pure exception families plus the generic theorem, any uncovered violator / family growth / world leak fires WHAC_A_MOLE by contract; contract PRIME.L2.RENYI3.EXCEPTION_FAMILIES.01, experiments-side, NO ledger row).  TWO SEALED CLASS FUNCTIONALS, both source-pure (AST + record-literal audited; consumed inputs: ONE r316 two-regime-state column + rank order): F_A = rank-local QMAX spike ratio (CONCENTRATION), F_B = rank-local PhiL2 spike ratio (DIVERGENCE-MASS SPIKE), window W = 5; thresholds frozen by the sealed largest-gap rule (k <= 6, gap >= 1.25) BEFORE any bound evaluation, class table printed before any bound table.  VERDICT WHAC_A_MOLE(kz53, kz83) on the sealed letter -- the hard gate fired exactly as the contract demands: the sealed rule recovers B = {kz55, kz67} (the r315/r316 FCIX pair, F_B 7.23/4.96 with a clean 1.78 gap; finite certificates C_B = 1.0536 <= the r306 shallow max, PhiL2-warded, non-growing, 0 EXT2 members) but class A stays EMPTY (best gap 1.233 misses the sealed 1.25 bar by 0.017), and on the 63-rung complement the mid-ladder generic constant C_gen = 0.4579 (frozen at kz34, m_0 = 84) is violated by exactly the two uncovered rungs kz53 (rho 1.0493) and kz83 (0.7791) -- a third exception form would be needed, NO third class added, abort by contract, recommendation back to fork (a).  THE CENSUS BEHIND THE LETTER IS THE ROUND'S FIND: the F_A TOP-3 are EXACTLY kz53 (2.47), kz83 (2.39), kz67 (2.38) -- the rank-local QMAX ratio ranks the complete mid/deep near-critical family on top, REFUTING at census level the r316 conjecture that kz53 needs a second coordinate; but the distribution below is a CONTINUUM (1.93, 1.90, 1.74, ...), not a gap-separated family, and the F_B continuum over-ranks kz12 (2.79, rho 0.38 -- a PhiL2 spike that is NOT a rho spike) above kz53 (2.70): threshold classification on these coordinates cannot cover kz53/kz83 without swallowing harmless rungs -- the exception-family FORM (sealed thresholds) is the wrong statement shape for a spike CONTINUUM.  What HOLDS: anchors bit-near incl. the COMPLETE r316 anatomy (ladder n = 65, H = {55, 67}, split 21|5|39, C_L2 0.7476, the 8-violator set, TOP1 0.558/0.785, rho anchors, C_small 1.0694); generic complement trend FALLS (-0.170, reserve med 2.06 -- with the B pair excepted the rest has growing reserve except at the two named spikes); 21 small-m certificates; world machinery intact (twin band 1.04, SCRAMBLE rejected via COLL 3.69 + edgewise shuffle break 288/300 with matched mass).  Must-fails: e1 third-class-after-sight AST-FLAGGED + seal_family_count REFUSES 3 families + gate maps uncovered violators to WHAC_A_MOLE / e2 threshold-after-sight AST-FLAGGED + toy thr break / e3 class-readback (cm/S3) AST-CAUGHT / e4 circular certificate caught by the declared-set ward EXACT + LOUD toy / m5a+m5b scope-flagged.  Protocol disclosure: prefilled placeholder record tables removed COMPLETELY before the first run (the r316 error class, disclosed in the spec); NO amendment after freeze except the record-table insertion.  Deterministic run1/run2; R318 direction typed census-grade: fork (a) with the QMAX local ratio as a continuous regime COORDINATE (bound rho_2 BY the coordinate, not classify by threshold), or the generic constant at the r306 first-5 scale where no exception family is needed on the measured ladder; nothing here bounds anything; NO RH CLAIM in either direction; consumed by v969 (wave 12, embedded byte-exact, smoke stage)"

_R318_STATUS = "L* INDEFINITE-FORK round -- the NEW idea class after the L*-language stop: PONTRYAGIN/KREIN INDEX vs SIGN REGULARITY (25/25; SPEC_SHA f2d98683; reviewer perspective shift after r312's 97.6/2.4 membership anatomy: 'the signedness itself is the mathematical object that is not yet understood' -- L* reformulated from squeezing out positivity to 'where may the negative signature live', with the core-question inversion: are the 2.4 percent negative cross mixtures the FINGERPRINT of the right indefinite theorem?  ONE theoretical representation test under the binding stop rule (both routes world-blind/restatement => FORK_DEAD, lane stop); contract PRIME.LSTAR.INDEFINITE_FORK.01, experiments-side, NO ledger row).  VERDICT P2_MAIN_SPECIFIC(fingerprint verbatim: the cross-mixture residual of the converged r308 Dykstra family lives LAWFULLY on the ANTIPHASE pair (D3, D4) with fixed sign -1, modal share med 0.699, 12/12 sealed rungs + the r289 rational twin EXACT ((2,3), -1, 0.692 -- METRIC_ONLY holds), while the dead controls break by PATTERN, not merely by bar: EPST/SCR put their residual on the ARCH-MEAN x BORDER pair (4, 5) with shares 0.953/1.000 and d6-class 0.962/1.000 vs MAIN 0.027 -- honest caveat typed with the letter: the control fingerprints are measured on NON-psd-feasible 200-step iterates (feas -0.45/-0.49, the r308 non-convergence), labeled ITERATE; dig site named per the stop rule: WHY does the 2.4 percent negative cross mixture live on the antiphase pair with a fixed negative sign, stably over the ladder and the twin) + INDEX_LANGUAGE(the P1 route closes as LANGUAGE: the index bookkeeping is EXACT -- spectral count #{sigma(B_n) > 1} == mp pivot count #{h_k < 0} at window AND guarded deep depth on all seven worlds (SCR deep 66/65 inside its gray band 6, the single tolerated case) -- but the index statement 'n_+(window) == N_w' is a total RESTATEMENT of L* (equivalence with minC >= N_w on 3 exact toys + 7 real worlds, both truth values realized), the global inequality n_+ >= N_w is VACUOUS (carried by the mu-channel majority S_+/N_w = 1.23..1.96 on every world incl. controls), and the negative-subspace invariants are ALL WORLD_BLIND under the r281 distance rule (NEG_LOW/NEG_MED/NEG_PR; NEG_LOW is NOT a proxy of the crossing location -- the negative directions do not live at minC, but their location carries no world separation either); Krein angular test typed INDEPENDENT (spearman(ANG, rho_win) +0.536 < 0.9, reported only)) + SIGNATURE_TABLE(window index defect w9/w13/twin 0/0/0 EXACT -- n_+ == N_w at the window, the index form of half-filling survival -- vs EPST 55 / SCR 37 / SMOOTH 4 / HL2 31: the control flips ARE negative directions inside the window; deep inertia 43@262 / 36@236 / 43@262 / 80@225 / 66@272 / 6@360 / 58@278; ladder 42/42 window defect 0) + FINGERPRINT(consensus (2,3) sign -1 med share 0.699, per-rung 0.605..0.780 over kz 9/12/13/14/15/18/20/22/23/29/32/33, cone-share med 0.970..0.982 -- the 97.6/2.4 anatomy is ladder-uniform) + R312_DEMARCATION.  P2 SR half honest negative: NO census object is MAIN-specifically sign-regular (E./A.principal score 1.000 but world-blind/not separating; every orientation-sensitive census coin-flip ~0.50 on MAIN) => the variation-diminishing implication chain to L* FAILS AT ITS PREMISE ON MAIN (PREMISE_FAILS_ON_MAIN).  Leg 0 bit-near (w9 367/263/104/184/184, B 8.368649, mp budget 104 == S_-, crossing 185; r312 pins: Dykstra CONV +6.6e-16, cone share 0.9760/0.9520/0.9778, alignment 0.9973).  Must-fails: m1 wrong signature convention 3 != 2 exact CAUGHT / m2 transposed census exact CAUGHT / m3 circular-lever mutant AST-FLAGGED / m4 single-rung consensus REJECTED (>= 10 rungs forced).  Protocol disclosures: prefilled placeholder record tables removed COMPLETELY before the first run (the r316 error class); smoke pass 1 aborted on an fp_consensus tiebreak-type harness bug (fixed at smoke stage); ONE reporting-only amendment a1 (the verdict-letter dig-site label derived from the MEASURED modal pair -- the draft had pre-named the border column, contradicted by d6-class 0.027; no bar, rule or tree moved).  Deterministic run1/run2; R319 direction typed census-grade: the antiphase (D3, D4) negative cross mixture as the object of the indefinite-theorem hunt -- its sign law is world-separating in SHAPE, exactly the precondition the reviewer's inversion needs; nothing here proves anything -- NO L* claim, NO RH CLAIM in either direction; consumed by v969 (wave 12, embedded byte-exact, smoke stage)"

_R321_STATUS = "L2 continuous-coordinate round -- reviewer fork (a) in the r317-sharpened form: THE SLIDING CUBIC BOUND (39/39; SPEC_SHA e68883ad; the r317 abort demanded the statement-shape change: bound rho_2 BY the single source-pure coordinate F_A = rank-local QMAX ratio (r317 import, W = 5) instead of classifying by threshold; contract PRIME.L2.RENYI3.CONTINUOUS_COORDINATE.01, experiments-side, NO ledger row).  SEALED: the exact concentration bracket qmax PhiH1 <= rho_2 <= PhiH1 = (F_A B)^2 with the source-pure baseline B = medloc x m/log m (derived algebra, warded two-sided live on 69 worlds); a three-form MONOTONE g-family with mid-ladder calibration and derivation-strength precedence (G_SQ b F^2 with b = (max cal B)^2 -- consumes NO target value; G_TT c1 + c2 F^3, the r317-named heuristic; G_LIN a F), the fit-free upper-envelope rule on the declared test split, gain bar 1.5 and a four-branch verdict tree sealed in advance.  VERDICT SLIDING_BOUND_GO(G_SQ) on the sealed letter: rho_2 <= 1.3056 x F_A^2 pointwise with 0/39 mid-ladder test violations AND all four named r316/r317 violators INSIDE (kz53/kz83/kz67/kz55 at reserves 7.0..9.6 -- exactly what killed every flat mid-ladder constant since r316 is absorbed by the coordinate); reserve min/med 2.71/5.35, trend -0.341 falling (growing reserve); the test envelope is STRICTLY monotone in F_A (bin Spearman +1.000, top bin 1.0536 at F_med 2.15), bulk Spearman +0.84 -- stronger than the r317 continuum reading; gain 15.95.  CANDIDATE THEOREM (sliding cubic bound) printed: sum q^3 <= 1.3056 F_A(w)^2 (log m)^2/m^2 for m >= 73 + 21 small-m certificates (C_small 1.0694); COROLLARY: F_A <= 2.47 measured => uniform C_impl = 7.97 (disclosed 7.5x looser than the r306 first-5 constant 1.069 -- the round buys FORM: one gliding bound, no regimes, no exceptions, not sharpness).  THE TWO HONEST STRUCTURAL FINDS: (1) the pure-algebra transfer route does NOT close -- B is NOT bounded by its cal max (test max 1.4088 = 1.23x cal max 1.1426, trend +0.122 rising): the G_SQ certificate holds on the measured rho_2 directly because the bracket's qmax slack falls faster than B^2 rises; the proof-side object is the qmax-share rho_2/(F_A^2 B^2); (2) SCRAMBLE is NOT rejected by the coordinate bound alone (its inflated cube comes with an inflated concentration ratio F_ins 2.00, covered at 5.21) -- the rejection is carried by the r317 class side condition (COLL attribution 3.69, seeded shuffle 321001 with 294/300 atoms displaced and matched mass), honestly typed: the sliding bound is not world-separating by itself.  Anchors bit-near incl. the complete r316 anatomy AND the complete r317 census (F_A top-3 (53, 83, 67) = 2.47/2.39/2.38 ordered, gap-B {55, 67} THR_B 3.7157, class A EMPTY, complement C_gen 0.4579 with violators (53, 83)); w9/w13/EPSTEIN admitted at the sliding bound (rho_2 0.458/0.461/0.368 <= g(F_ins) 0.90/1.55/1.29), twin band 1.04.  Must-fails: e1 g-posthoc AST + toy CAUGHT / e2 coordinate cubic read-back AST-CAUGHT / e3 envelope-on-cal declared-set ward EXACT / e4 monotonicity break LOUD 1.0625 / m5a+m5b scope-flagged.  Protocol disclosure: prefilled placeholder record tables removed COMPLETELY before the first run (the r316/r317 error class); NO amendment after freeze except the record-table insertion.  Deterministic run1/run2; R322 direction typed census-grade: the provenance question is now source-pure, local and split in two -- (a) is F_A bounded (max 2.47, the near-critical family is its top), (b) what bounds the qmax-share rho_2/(F_A^2 B^2) -- the median-of-max shape law (the r302 M_2 stationarity 1.973 pins the second moment of the same shape); nothing here bounds anything beyond the measured rungs; NO RH CLAIM in either direction; consumed by v969 (wave 12, embedded byte-exact, smoke stage)"

_R322_STATUS = "L* antiphase-sign-law round -- THE DIG after the r318 fork decision (25/25; SPEC_SHA 761b51d4; contract PRIME.LSTAR.ANTIPHASE_SIGN_LAW.01, experiments-side, NO ledger row; the three dig questions: (1) is the (D3, D4) antiphase sign law of the block-Green cross-mixture residual iteration- and construction-invariant, and what do FAIR control objects carry (the r318 caveat: control fingerprints were ITERATE-grade); (2) is the law identity-forced (exact forced-component analysis of the linear identity constraints on the (D3, D4) sector); (3) does the theorem candidate 'psd cone part + antiphase-supported fixed-sign residual' certify on 57 rungs + twin?).  VERDICT ALGORITHM_ARTIFACT on the sealed tree: the law breaks under the sealed random-start variants -- their accepted near-feasible points (staged to 20000 Dykstra steps, min eig rel -8.5e-9/-1.2e-9, r311 START_NEAR class) carry modal pair (0, 2) with shares 0.310/0.264 and cone share med 0.782: the sign law AND the r312 97.6/2.4 cone anatomy are properties of the LEAST-NORM-PROXIMAL DYKSTRA BASIN, not of the psd solution set as a whole; the canonical protocol variants LSTART/LONG/ZERO/REV all carry the law exactly ((2, 3), -1, share 0.692; projection order irrelevant) AND coincide within rel 2e-7 -- exactly 9/15 variant pairs distinct = precisely the pairs involving the random starts: the sampled psd intersection has (at least) two basins and the law is the fingerprint of the proximal one.  HARDENING of the r318 caveat on FAIR objects: the least-norm census reproduces the r318 shape contrast construction-fairly (w9/twin (2,3) -1 0.698 vs EPST/SCR (4,5) -1 1.000 d6 1.000 -- the r318 control-iterate pattern is the least-norm pattern), BUT the budget-ablated CONVERGED controls split: EPST-abl CARRIES the MAIN law stronger than MAIN itself (share 0.742 vs 0.692, CONV +2.5e-16) while SCR-abl breaks the share bar (0.379, d6 0.371) => FAIR_CONTROL_CARRIES 1/2 -- the r318 pattern dichotomy does NOT survive fair convergence; the separation on fair objects is a mixed share margin, not a dichotomy.  FORCED COMPONENT exact: TOY4 calibrator machine-exact (free fraction 0, value 4/7 == the r308 G10 hand pin); SM1 phi_23 exact free fraction 0.47671 with forced value +5.101e-1 POSITIVE; MINI16 exact rowspace membership FALSE; w9 f64 free 0.635 value +0.12 -- the negative sign law is carried ENTIRELY by the free/selection directions (the disclosed D3 = -(D2 + 2 D1) in-block dependence is the structural reason); exact_forced FALSE.  ANATOMY: sign consistency 1.000 (every (2,3)-dominant block has R[2,3] < 0; 92.3 percent of ALL blocks), position-structured (thirds 0.289/0.860/0.926 -- a mid/tail law of the fold order), MAG scale-stable over the 12 sealed rungs (spearman vs S -0.168).  COUPLING: K1 block-local antiphase mass pairing g_j g_{j+2} + g_{j+1} g_{j+3} spearman +0.8114 (the strongest measured correlate, below the sealed 0.9 bar), K2 5/7-reserve -0.832, K3 r288 carrier |z_v| +0.252 -- all UNCOUPLED.  CANDIDATE: 57/57 rungs + twin certified censally at the sealed bars (CONV + pair + sign + share >= 0.5 + cone med >= 0.95; worst share 0.605@kz23), but demoted by the main letter (basin-selected family) and by L5 (a fair control carries the pattern); missing links L1-L5 all open.  Must-fails: m1 unconverged-iterate census REJECTED as ITERATE (the r318 caveat machine-enforced) / m2 permuted-family census (3,4) != (2,3) CAUGHT / m3 wrong-identity-sign -4/7 != +4/7 CAUGHT exact / m4 read-back mutant AST-FLAGGED.  Protocol disclosures: draft record block removed COMPLETELY before the first run (the r316/r318 error class); ONE amendment a1 (gate typing only: the invariance gate is MEASURED and the sealed tree adjudicates -- the negative branch is a verdict letter, not a probe failure; the letter is identical across passes; no bar, acceptance rule, statistic or tree moved).  Deterministic run1/run2; R323 direction typed census-grade: the selection-geometry question -- WHY does the least-norm-proximal basin organize its indefiniteness on the antiphase pair (best reporting-grade hook: the block-local antiphase mass pairing at +0.81) -- and whether ANY canonical source-pure selection rule reproduces the basin (the r312 COEFFICIENT_SIGN_WALL says no formula so far); nothing here proves anything -- NO L* claim, NO RH CLAIM in either direction; consumed by v969 (wave 12, embedded byte-exact, smoke stage)"

_R324PRE_STATUS = "PRE-WORK PROBE of round r324, SUPERSEDED mid-round by the binding reviewer course correction (the F_A-boundedness hunt demoted as a potentially unnecessarily strong statement -- the cleaner decomposition is QMAX x M_2; the round's binding contract is qmax_m2_origin_probe.py below); stays sealed and citable, its banked record (M_2 stationarity, m2 column + freeze + violator set, share majorant) is consumed as ANCHORS by the r324 probe.  Original record: L2 F_A-provenance round -- the terminal main lane after the r321 SLIDING_BOUND_GO (36/36; SPEC_SHA 9a6696f8; contract PRIME.L2.RENYI3.FA_PROVENANCE.01, experiments-side, NO ledger row; the two provenance halves of the r321 sliding bound executed: (a) is F_A bounded -- distributional route (sealed stationary-null resample: 200 seeded replicates of full synthetic QMAX ladder columns drawn iid from the pooled r302-stationary normalized block profile, donors = ladder minus the named spike ranks, declared-set warded) and structural route (NEW EXACT factorization QMAX = s x a with s = in-block survival <= 1, a = atom-mass share of the argmax block, warded 2.2e-16 live); (b) what bounds the qmax share sigma = rho_2/(F_A B)^2 -- NEW EXACT intermediate inequality sigma <= m2/(m qmax) (from sum q^3 <= qmax sum q^2, Fractions-proved, warded two-sided live on 69 worlds), converting the r302 M_2 stationarity into the pointwise transfer rho_2 <= m2 x F_A x B/log m).  VERDICT FA_BOUNDED_DISTRIBUTIONAL + QMAX_SHARE_OPEN + NOT_COMPOSED on the sealed trees: (1) the r302 stationarity EXPLAINS the coordinate -- KS(F_A real, F_A* resampled) = 0.0982 <= 0.125 and the ladder maximum 2.47 sits INSIDE the stationary max law (p_max 0.090 >= 0.05; envelope C_F 3.357, q95 2.583): F_A <= C_F is a distribution-statement candidate; DISCLOSED tension: per-rank p at the named spikes 0.005/0.000/0.000 -- WHERE the extremes sit (exactly the near-critical rungs) is not explained by the exchangeable null, the rank-identity question is the sharpened residue; (2) the structural census REFUTES a single mechanism: kz53 is a SURVIVAL spike at an edge-adjacent atom-poor block (F_s 1.72, edge distance 0.01, 6 atoms) while kz67 is an ATOM-MASS concentration at an interior atom-rich block (F_a 2.09, 12 atoms), kz83 mixed -- no common carrier, the exact majorant F_A <= a/medloc does not mid-ladder certify (4 violations); (3) share letter OPEN with the mechanism measured: stationarity reproduces on the 65-rung ladder TIGHTER than the r302 core (KS 0.023/0.016 vs 0.043; m2_inf census 2.081 vs rec 1.973), sigma trend -0.584 falling (the r321 'share falls faster than B^2 rises' mechanism measured directly), but C_M2 = 2.2557 is violated by exactly the named spikes (m2 3.05..3.19, +35..42 pct) -- THE F_A SPIKE AND THE m2 SPIKE ARE THE SAME OBJECT seen in the third vs second moment; (4) strongest bycatch: the composed bound rho_2 <= 2.2557 x F_A x B/log m holds 0/39 MEASURED with named coverage 4/4 (reserves 1.23..1.81), LINEAR in F_A where r321 was quadratic -- census, not certificate (the m2 clause fails by seal).  Slim anchor set bit-near (r306 C_2 1.069 0/57, r316 rho quartet + C_small, r317 top-3 EXACT ordered + gap-B, r321 b 1.3056 + 0/39 + named 4/4).  Must-fails: e1 resample-peek AST + toy CAUGHT / e2 spike-donor pool declared-set ward EXACT / e3 share-posthoc rho AST + toy CAUGHT / e4 QQ overlap ward EXACT / m5a+m5b scope-flagged.  Protocol disclosure: prefilled placeholder record tables removed COMPLETELY before the first run (the r316/r317/r321 error class); NO amendment after freeze except the record-table insertion.  Deterministic run1/run2; R325 direction typed census-grade: ONE local question left -- the second-moment excess of the near-critical rungs vs the stationary bulk (m2 tail law via the same resample machinery, or the atom-level genealogy of the heterogeneous argmax blocks); nothing here bounds anything beyond the measured rungs; NO RH CLAIM in either direction; consumed by v970 (wave 13, embedded byte-exact, smoke stage)"

_R324_STATUS = "L2 QMAX x M2 origin round -- the reviewer-sharpened terminal main lane after the r321 SLIDING_BOUND_GO (36/36; SPEC_SHA dc36cacb; contract PRIME.L2.RENYI3.QMAX_M2_ORIGIN.01, experiments-side, NO ledger row; BINDING COURSE CORRECTION mid-round, disclosed: the F_A-boundedness hunt of the sealed pre-work probe (fa_provenance_probe.py, r324-pre) demoted as a potentially unnecessarily strong statement that creates an artificial wall -- for the needed power N_2 >~ m^0.888 asymptotically F_A log m = O(m^{0.112-eps}) suffices; the cleaner decomposition is QMAX x M_2; the banked pre-work reproduced bit-near as anchors and disclosed pre-spec).  S0 EXACT (Fractions + live on 69 worlds): the interpolation M_3 <= qmax x M_2 AND M_2 <= qmax (worst slack 0.0), hence rho_2 <= (m qmax)(m M_2)/(log m)^2 -- the r321 bracket upper improved by exactly the factor M_2/qmax <= 1; the identity F_A x B x log m == m x qmax warded 2.7e-16: F_A is the rank-local normalization of m qmax, NO black correction factor.  S1 M_2-EXPORT: pointwise m M_2 <= C_2 = 2.2557 (mid-ladder freeze) FAILS 7/39 exactly on the banked violator set (kz53 3.1528 / kz28 / kz67 3.1938 / kz109 / kz76 / kz61 / kz83 3.0490) -- the reviewer's 'export should carry' expectation REFUTED pointwise at the mid-ladder freeze (disclosed pre-spec, sealed rule adopted verbatim, not tuned); test trend +0.014 FLAT, envelope C_2env 3.1938; the DISTRIBUTIONAL r302 export GO (stationarity KS 0.0230/0.0158 <= 0.125).  S2 MULTISCALE PILEUP (the reviewer mechanism hypothesis, four measurements on the canonical dyadic source-scale decomposition s = floor(log2(vmax/|atom|)) of the argmax block): (1) scale recomposition EXACT 2.2e-16; (2) fold multiplicity <= 2 admitted on ALL 69 live worlds (the r314-proven cap); (3) per-scale mass C_PIL 9.3583 FAILS 11/39 (worst kz67 22.4) -- clause REFUTED; (4) active scales nsc_rel/log m max 2.026, C_NSC 2.0258 HOLDS 0/39 -- the O(log m) scale count CERTIFIES pointwise; direct m qmax <= C_INF log m (C_INF 1.7481) FAILS 5/39 named 1/4; the exact pileup chain m qmax <= nsc x pil warded 0.0 live.  HARDNESS CENSUS ANSWERED: the named near-critical spikes are NOT multiscale convergence -- ONE near-maximal source scale dominates the argmax block (kz53 s0 = 13.78 of G 13.02 at nsc 5 == ladder med; kz83 s0 12.71; kz67 s0 22.38 at nsc 7): the pileup tip is a SINGLE HEAVY SCALE -- the reviewer hypothesis REFUTED in clause (3) and CONFIRMED in clause (4).  VERDICT PILEUP_GROWS_SUBCRITICAL(+0.172) on the sealed six-letter tree (TARGET_LEAK / FA_RESTATEMENT / QMAX_MULTISCALE_GO / M2_GO_QMAX_OPEN / PILEUP_GROWS_SUBCRITICAL / PILEUP_SUPERCRITICAL): growth exponents fit-free dyadic halves-slope over the 39 test rungs e(G/log m) +0.158 + e(m M_2) +0.014 = e_tot +0.172 < CRIT 0.224 (= 2 x (1 - 0.888); the reviewer's 0.112 is the F_A-side equivalent -- this route is LINEAR in m qmax where r321 was quadratic in F_A, the budget doubles), stability halves +0.141/-0.160 both subcritical (the second half FALLING) -- DECIDED; by the reviewer contract a sufficient first-class outcome, not a failure.  S3 COMPOSITION typed MEASURED: sum q^3 <= 8.941 x (log m) x m^{+0.172}/m^2 => N_3 >= m^{0.914}/sqrt(8.941 log m), N_2 >= N_3 (r306 exact chain) => N_2 >= m^0.888 for all m >= m_0* = 10^59.6 => slope(n_eff) >= +0.908 => sigma <= sigma* = -0.516 => the r297 target => the v964-S0 vdC theorem => delta' > 0.21 => the terminal_positive_main edge; all measured m <= 274 closed by the finite certificates (r306 0/57 + this round's tables); the gap (274, 10^59.6) is the DISCLOSED extrapolation hypothesis -- no cofinal claim.  Slim anchors bit-near (r306 C_2 1.069 0/57, r316 rho quartet + C_small + n 65, r321 b 1.3056 0/39 named 4/4, r324-pre KS 0.0230/0.0158 + m2 med/max 2.051/3.194 + C_M2 2.2557 + the seven-violator set EXACT).  Must-fails: e1 scale-drop recomposition break LOUD exactly 1 / e2 3-fold toy genealogy REFUSED by mult_ward while all live worlds admit at exactly 2 / e3 M_3 read-back AST-CAUGHT / e4 scale-cutoff posthoc AST + toy CAUGHT twice / m5a+m5b scope-flagged.  Protocol disclosures: the course correction documented in the docstring; the banked pre-work outcomes disclosed pre-spec (the genuinely open quantities -- scale profiles, pil/nsc columns, all S2 constants and violation counts, the hardness census, both exponents -- computed only after the freeze); ONE calibration-pass fix BEFORE the record freeze (the m_0* solver searched linear space to 1e18 and missed the honest 10^59.6 -- moved to log space, the sealed rule unchanged); NO amendment after freeze except the record-table insertion.  Deterministic run1/run2 (byte-identical up to the runtime line); R326 direction typed census-grade: the single-heavy-scale anatomy of the near-critical argmax blocks (what caps the TOP source scale's mass at one block -- the mult-2 cap holds uniformly, so the cap must come from the per-group mass law, the local mass balance of the dominant fold group), and whether the subcritical exponent is stable under deeper anchors; nothing here bounds anything beyond the measured rungs; NO RH CLAIM in either direction; consumed by v970 (wave 13, embedded byte-exact, smoke stage)"

_R325_STATUS = "Extraction-repair fork round -- the new main strand after the R319 red team: the three reviewer variants for repairing the RH-connection seam (rh/ cofinality runs in the ANCHOR direction; H_cof demands the MESH-refinement direction, measured inadmissible with false floors) measured in their machine-checkable halves (18/18; SPEC_SHA 31277f91 final with record, freeze-run 57e50d36; contract PRIME.EXTRACTION.ORDER_REPAIR_FORK.01, experiments-side, NO ledger row).  VERDICT: primary ELEMENTWISE_STABILIZATION_GO + co-letters CANONICAL_MESH_REBUILD_GO + SIGNED_DEFECT_CORRECTION_GO(SIGN) + ANCHOR_ONLY_INSUFFICIENT on the sealed tree.  (A) On the NATIVE dense class (dyadic step-function autocorrelations, the v749 'Weil form of step functions' class, elements sealed by seed) ALL THREE channels (comb/arch/pole) of the canonical tower windows stabilize EXACTLY at the predicted finite anchor onset alpha* = (n_g+1)D0/2 (comb rel dev 0.0/3.3e-18 above onset, 2.7e-2..5.3e-2 below -- real onset) and the value is CONSTANT under dyadic mesh refinement (comb 3.3e-18, arch 1.5e-15, pole 2.0e-17): the elementwise architecture consumes NO mesh-cofinal ladder and NO transport -- the R310 finite_forms_converge_to_weil shape generalizes from the Lean comb channel to every channel on the native class, incl. the derived tent-read identity L_cat(F) = -sum mu_n (I_D F)(u_n) gated at 1e-12.  (B) v749 T1.4b reproduced: every deployed frame-A window IS a directly rebuilt tower member at rel dev 0.0 (three picks); the direct rebuild ladder is PD per stage with honestly falling margins (lambda_min/c_0 1.33e-5 -> 3.34e-6 -> 6.92e-7, reported not consumed); the dyadic transport identity holds at 8.0e-17 but variant B never uses it.  (C) On the sealed non-native C^2 class (quartic L=2.3, Hann L=2.9) the per-channel quadrature defect is ONE-SIGNED (comb NEGATIVE, arch POSITIVE, pole POSITIVE, all stages), falls at the D^2 class rate per channel (ratios 3.6..9.0; the TOTAL ratio 2.2..3.3 is reported only -- comb/arch sign opposition cancels there, an honest structural record), and sits inside the RIGOROUS closed-form interpolation envelope |E_ch| <= (D^2/8)||F''|| K_ch -- controlled on its own, no wall margin anywhere; the C^0 tent element's comb defect is EXACTLY 0 (its off-grid kink cells contain no prime-power atom, recorded fluke); the anchor-only floor is real: at fixed mesh the anchor ladder stabilizes at E_tot CONSTANT +1.77e-4/+1.59e-4 (the R319 false-floor mechanism on this probe's own elements).  Protocol disclosures: prefilled record block removed before the first run (r316/r317 class); three smoke-harness fixes BEFORE the freeze (grid-element closing zero knot -- np.interp jump, the kernel reads were wrong by ~1e-6 while the lag identity was machine-exact; decay gate retyped total -> per-channel after the smoke run measured the sign cancellation; smoke index); only post-freeze change the record insertion.  Must-fails m1 anchor-only adversary / m2 nearest-neighbour atom placement / m3 corrupted transport weights / m4 membership corruption all CAUGHT.  Deterministic run1/run2.  The fork consequence (analytic, next.txt note): the repair statement for the next Lean round is the elementwise quantifier set (canonical family + per-element predefined finite stabilization + window-local positivity premise), NOT a new mesh theory; nothing here proves any window positivity, any local lemma, or anything about zeta zeros; NO RH CLAIM in either direction; consumed by v970 (wave 13, embedded byte-exact, smoke stage)"

_R327_STATUS = "L2 fold-group mass-cap round -- the r324 follow-up question on the terminal main lane: WHAT caps the mass of the dominant fold group of the argmax block (34/34; SPEC_SHA 11e4fd401ff77583 final with record, freeze 71f8b7b423a3f847; contract PRIME.L2.RENYI3.GROUP_MASS_CAP.01, experiments-side, NO ledger row; the r324 hardness census had located the near-critical spikes in a SINGLE heavy source scale -- this round descends one level to the fold GROUP).  NEW EXACT MACHINERY (module-own, source-pure, all warded live on 69 worlds): the per-group mass ledger on the identical r314 fold segmentation (G1/mult/gblk == genealogy at 0.0), the partition sum_g gabs == A1_j (3.4e-16), the L1 recomposition sum_j |sum_g G1_g| == L (0.0), the TWO-ANCESTOR bound gabs_g <= mult_g x gmax_g <= 2 x vmax (slack 0.0 -- the proven mult-2 cap as a mass statement) and the exact CAP CHAIN m qmax <= ng x hgn (slack 0.0).  Q1 ANATOMY ANSWERED -- sealed letter SOURCE (med named ratio 1.057 >= RATIO_BAR 0.5): the r324 heavy scale IS a single fold group at the two sharpest spikes, and the STRUCTURAL FINDING of the round: on ALL 65 rungs the heaviest group of the argmax block is EXACTLY ONE beta/omega fold pair (window-atom histogram [0, 65, 0]: one bulk + one window atom at one position) with median alignment 1.000 -- the two ancestors REINFORCE, no internal cancellation; kz53: the single pair carries 88.8 pct of the argmax block's atom mass at gap 0.076 (the second group 13x lighter) -- the spike is literally ONE bulk/window coincidence; kz67 is the exception shape (6 groups, bshare 0.416); position thirds [21, 29, 15] mid-heavy (the r322 mid/tail echo).  Q2 CAP CANDIDATES -- VERDICT CAP_PARTIAL on the sealed six-letter tree (TARGET_LEAK / RECOMP_BREAK / LAMBDA_PAIR_CAP_GO / BALANCE_CAP_GO / HEAVY_GROUP_UNBOUNDED / CAP_PARTIAL): (i) the lambda-pair route hga <= 2 vmaxb is EXACT but the source-size coordinate lvb = 2 m vmaxb/L FAILS the mid-ladder freeze 19/39 (C_LV 1.1838; kz55 6.85 / kz53 5.77 / kz83 4.61 / kz67 4.13, named 0/4) -- the von-Mangoldt size analogy does NOT close as a polylog cap; (ii) the direct group cap hgn <= C_HG (log m)^A fails at A = 1 (18/39) AND A = 2 (8/39, kz53 3.2x), minimal A = None; (iii) THE GROUP COUNT CERTIFIES: ng(argmax block) <= 2.6351 x log m with 0/39 violations and named 4/4 (ng med 5 max 13) -- the third certified O(log m) count of the lane (after the r324 scale count 2.0258).  EXPONENTS (fit-free dyadic halves-slope): e(hgn/log m) = -0.200 FALLING and e(lvb/log m) = -0.261 FALLING (the heavy-group coordinate DECAYS with depth -- the spike set is a shallow/mid phenomenon, not growth), e(ngl) +0.293, e_route +0.106 < CRIT 0.224 but halves +0.411/-1.183 STRADDLE -- UNDECIDED by the sealed stability rule: HEAVY_GROUP_UNBOUNDED does NOT fire, and the honest reading is that the cap route is subcritical in the median but pointwise-blocked by the same named spike family as every mid-ladder constant since r316.  Q3: no certifying cap -> the r324 MEASURED composition stands unchanged (sum q^3 <= 8.941 (log m) m^{+0.172}/m^2, N_2 >= m^0.888 for m >= m_0* = 10^59.6, the gap (274, 10^59.6) the disclosed extrapolation hypothesis); measured cap-route envelope max(ngl x hgL) 2.616.  Slim anchors bit-near (r306 C_2 1.069 0/57, r316 n 65 + rho quartet + C_small, r324 C_NSC 2.0258/C_PIL 9.3583/C_INF 1.7481 with violation counts 0/11/5 EXACT + named scale masses 3/3 + e_tot +0.172, r324-pre C_M2 2.2557 + seven-violator set EXACT).  Must-fails: e1 group-drop recomposition break LOUD exactly 1 / e2 wrong-window-max two-ancestor break exactly 1 CAUGHT / e3 cap-posthoc AST(rho) + toy CAUGHT twice / e4 qmax-readback AST-CAUGHT (the q_max record cannot enter the cap side) / m5a+m5b scope-flagged.  Protocol: smoke pass 1 34/34 (0.4 s) NO amendment; calibration pass 1 = first full evaluation 34/34 (36.4 s) NO amendment; only post-freeze change the record-table insertion; deterministic run1/run2 byte-identical up to the runtime line.  R-next direction typed census-grade: the spike cap, if it exists, is a statement about WHERE the single heavy beta/omega coincidence can sit (the bulk/window pairing at one position -- a source-geometry question), not about group counting (certified) or group multiplicity (proven); alternatively the honest end state of the route is the r324 MEASURED composition.  Nothing here bounds anything beyond the measured rungs; NO RH CLAIM in either direction; consumed by v970 (wave 13, embedded byte-exact, smoke stage)"

_R329_STATUS = "EXT3 fresh-anchor audit repair (r328A finding A2 + r328C finding C1: the 65-rung class ladder was the test set across r306..r327, the F_A coordinate was r317-selected and r321-certified on the same set, and the ladder is large-gap selected by construction) -- 12 genuinely NEW windows that appeared in NO previous round, tested pointwise against the FOUR FROZEN constants of the lane with NOTHING recalibrated (33/33; SPEC_SHA bbfaf1990bd37061 final with record, freeze 29d1b80627a616f9; pre-freeze commit 604b8aaf / record commit 8cbd95f9 under the two-commit freeze protocol; contract PRIME.AUDIT.EXT3_FRESH_ANCHORS.01, experiments-side, NO ledger row).  SELECTION (sealed, source-pure, machine-checked disjoint from the 80-kz used ledger = 70 frame-A + 35 r286-rule ranks): the frame-A anchor CONSTRUCTION verbatim (h ~ 4 log z / gap) with only the CHOICE changed -- stratum B = 6 small-gap mid-zone anchors (z 127..227 inside the core zone range, grel 0.28..0.53 vs ladder med 1.32) + stratum A = 6 deepest fresh windows (N_w 2389..2577); ALL 12 deeper than every prior window (N_w 1721..2577 > 1650); four A-queue candidates were the first POSITIVE_PREFIX failures ever seen on this construction (nf 2125..2468).  MAIN VERDICT EXT3_VIOLATIONS + EXPONENT_SHIFTED + SMALL_GAP_DIFFERENT(rho2 med x10.29, F_A med x3.21): (b) the r306 uniform constant C = 1.069 BREAKS on the four sharpest small-gap anchors (kz51 rho_2 7.6196 = 7.1x, kz54 3.0x, kz62 2.2x, kz42 2.1x) -- the first-5-frozen constant is a LARGE-GAP-family statement, now said with numbers; (a) the r321 sliding bound b F_A^2 = 1.3056 F_A^2 covers exactly those four spikes with reserves 5.0..6.1 at the FROZEN constant (the coordinate carries genuine independent evidence beyond its calibration set) but misses four QUIET anchors (F_A 0.27..0.39, excess 1.05x..1.40x; convention-sensitive: under the r321 insertion-rule coordinate all four are INSIDE) -- the named successor question is a floor term below the ladder's sampled F_A range, r330+ material, NOT a recalibration; (c) the r324 scale count C_NSC = 2.0258 HOLDS 12/12 (min reserve 1.6); (d) the r327 group count C_NG = 2.6351 HOLDS 12/12 (min reserve 1.8) -- both O(log m) counting constants generalize choice-robustly.  e_tot census on the fresh set -1.660 vs record +0.172 = cohort-composition effect (typed, census-grade).  All five frozen-rule reproductions bit-near on the 65 ladder (C_2 1.069 0/57, b 1.3056 0/39 named 4/4, C_NSC 0/39, C_NG 0/39 named 4/4, rho quartet + C_small).  Must-fails: e1 anchor collision CAUGHT exact, e2 constant recalibration AST(rho) + toy CAUGHT twice, e3 gap-rule-after-sight AST(rho) + toy CAUGHT, e4 target read-back AST(cm) CAUGHT, m5a/m5b scope-flagged.  Protocol: smoke 32/32 (0.5 s) NO amendment; calibration pass 1 = first full evaluation 33/33 (214.5 s) NO amendment; record run1/run2 byte-identical up to WALL and identical to the calibration pass; only post-freeze edit the record-table insertion.  Nothing here bounds anything beyond the 12 measured fresh windows + the 65-rung ladder; NO RH CLAIM in either direction"

_R330_STATUS = "Second-living-world audit repair (r328C finding C3, the missing positive control) -- a Dirichlet-L comb (primitive real character chi mod 3) as the first LIVING second world next to the dead EPSTEIN/SCRAMBLE/SMOOTH controls (24/24; SPEC_SHA 665260180de9bbc7 final with record, pre-freeze commit 2b1b69ce / record commit 4f2e4f52 -- the first round under the two-commit freeze protocol; contract PRIME.AUDIT.SECOND_LIVING_WORLD.01, experiments-side, NO ledger row).  CONSTRUCTION (sealed, v563-gauge exact): MAIN positions log(p^k) unchanged; DIRICHLET weights chi(n) x MU_ALL bitwise (chi = 0 atoms dropped); DIRICHLET_ABS = MU_ALL restricted to (n,3) = 1 (pure atom removal); MAIN frame (ARCH lags, smooth border, window depth) kept -- NOT a GRH-faithful Dirichlet window (Gamma parity / conductor NOT modeled, disclosed limit); trivial-twist identity BITWISE (the comb interface IS the v563 gauge).  SEVEN-PROPERTY BATTERY at frozen MAIN constants on the identical 42-rung (N, kz)-sorted ladder, VERDICT SECOND_WORLD_SPLITS: SHARED by the chi-twisted world = NEFF_GROWTH (sl_neff +0.527 vs MAIN +0.963, above the sealed half-magnitude bar), FILL (med 0.436 FILL_LOW vs MAIN 0.434 -- the r300 world-separating class now stands on n = 2 living arithmetics vs 2 dead controls), MULT2 (max mult 2 on 42/42, two-ancestor slack <= 0 exact, one-pair mixed share med 1.00 on all three worlds); SPLIT (retyped as MAIN/zeta-side idiosyncrasies INSIDE THIS FRAME) = HALF_FILLING (DIR nf None 0/42, depth ratio med 0.080, w9 nf 24; ABS 0/42, med 0.125, w9 nf 37 -- REMOVING THE THREE p = 3 ATOMS ALONE kills the wall at control depth), RENYI3_C2 (DIR 32/42 violations of the live-frozen r306 constant 1.069434, max rho_2 27.6; ABS 37/42, max 149), SIGMA_DECAY (sl_D +0.793 / +1.343 -- the diagonal GROWS), O_SIGN (O_NEG 27/42 / 28/42 -- control side of the r299 class); ABS additionally splits NEFF_GROWTH (+0.272).  MAIN anchors re-derived bit-near through the identical channel (nf None 42/42, sl_D -0.5710, n_eff med 37.41 slope +0.963, C_2 refreeze 1.069434 with 0/42, O < 0 on 13/42 EXACT, control flips 25/21/27, EPST rho_2 0.368 HOLDS / SCR 1.780 VIOLATES).  Must-fails: m1 wrong character period CAUGHT exact (witness n = 1), m2 halved v563 gauge CAUGHT (rel dev 0.5 exact), m3 constants recalibration from the second world CAUGHT structurally (declared set != frozen MAIN_FIRST5; DIR rho max 27.645 never adopted), m4 MAIN contamination of the second-world constructors AST-FLAGGED.  Disclosed calibration amendments a1 (violation count against the live-frozen full-precision C_2 instead of the 4-decimal record literal) + a2 (contribution-ward deep bar 1e-4 for N > 400 flipped chains -- one conditioning outlier 2.0e-5 at kz31; no class rule or adjudication rule moved).  HONEST LIMIT (binding): the round cannot distinguish 'wall is zeta-specific' from 'wall needs the matched Gamma/conductor frame' -- the GRH-faithful Dirichlet window is the named follow-up.  Deterministic run1/run2.  Nothing here proves any window positivity or anything about zeta or L(s, chi) zeros; NO RH CLAIM in either direction"

_R331_STATUS = "METRIC_ONLY resolution audit repair (r328C finding C2: the r289 switch was adjudicated at the w9 wall margin 1.7e-4 and might be construction-blind at the 1.8e-8 anchors of the r286 ladder) -- the twin disturbance measured in margin units over the ladder, a variable-precision twin sweep at the tight anchors, and a genuine diophantine counter-test (24/24; SPEC_SHA f871fe84acdc0526 final with record, freeze 8d771fae0a374fa8; pre-freeze commit b8319121 / record commit a45d4560 under the two-commit freeze protocol; contract PRIME.AUDIT.TWIN_RESOLUTION.01, experiments-side, NO ledger row; seed-free deterministic).  MACHINERY: the standalone document pipeline (verify_lstar_instance) with a verbatim explicit-comb re-expression identity-gated BITWISE on every anchor; r289 twin constructors + r286 sign-safety tiers + audit_no_mp verbatim; mp dps-30 PAIR deltas on every sub-1e-5 margin, dps-45 pairs on decision stages, delta floor 1e-13 (the mp-exact-B/f64-eigensolve resolution).  MAIN VERDICT METRIC_ONLY_CONFIRMED_AT_RESOLUTION(margins 1.675e-4 .. 1.806e-8 over 11 anchors; t* = 1e-6 on all sweep anchors; all counter-tests keep): (1) THE RESOLUTION TABLE -- at the r289 precision 1e-8 the twin footprint |Delta_m| is 3.4+ ORDERS below EVERY margin (11/11 RESOLVE, worst ratio 3.66e-4 at kz98 margin 1.95e-8; kz119 margin 1.806e-8 ratio 1.91e-4; minC preserved everywhere): the audit's feared blindness at the tight anchors does NOT occur -- the margin responds to the rationalization far more weakly than 1:1 in gap units; (2) THE PRECISION SWEEP (tols 1e-3/1e-6/1e-8/1e-10 on kz9/64/98/119): 1e-3 is BLIND everywhere (signature broken, ratios 1.3..8.6e5), from 1e-6 down everything RESOLVES -- t* = 1e-6 uniformly (kz98 the closest call: ratio 9.87e-2 just under RES_BAR 0.1, dps-45 confirmed); denominator censuses are the dual ladder (q med 19..981809; q max <= 3.9e8 on constructible atoms << 2^53); the f64 construction floor censused honestly (14606/23725 floor atoms at 1e-10 on kz98/kz119 -- sub-1e-10 twin precision not constructible in this pipeline); (3) THE COUNTER-TEST (golden-ratio detune, weights bitwise, gap structure preserved <= 1e-4, exact resonances demonstrably destroyed 28 -> 0 on w9): w9 CT1/CT2 KEEP (delta 4e-8/8e-8 at margin 1.7e-4) and kz119 CT1 (24574 atoms) + CT2 KEEP (delta +4.7e-11 mp pair, ratio 2.6e-3 at margin 1.8e-8) -- the genuinely diophantine direction cannot crack the wall at any resolving dose, wall anchor or tightest anchor: METRIC_ONLY doubly confirmed, now WITH a resolution certificate on the tight range.  Regressions: w9 records + mp staffel dev 4.1e-9; r286 sweep-anchor margins rel <= 0.05 + offsets +0/+2/+1/+1 exact; r289 twin at 1e-8 reproduced with the NEW number Delta_m = +2.263e-9 = 1.4e-5 of the wall margin.  Must-fails: m1 collision twin (tol 4.0) CAUGHT by the strict-order gate (4 collisions); m2 metric perturber (eps 0.05, gap change 6.2e-2) REJECTED by the CT admissibility gate; m3 no-mp ledger entry FLAGGED (r286 detector, real 41-stage ledger clean); m4 target-readback twin AST-FLAGGED, constructors + fragment audit clean.  Disclosed calibration amendments a1-a3 (du-gate rounding slack 4 ulp; cell/node gates budget-scoped with in-budget node landings censused; f64-vs-mp cross-ward floor 1e-11 = the f64 noise floor -- classification always consumes the mp pair delta; no twin construction, class bar, delta-source policy or verdict rule moved) + protocol disclosure (a drafted record block was removed BEFORE the first run, r316 class).  Honest negatives: sub-floor twin precision open; near-resonance (vs exact-resonance) structure untested; the resolved set is 11 anchors x 4 tolerances, a finite census, not a family theorem; consequence bookkeeping for earlier rounds stays with the coordinator.  Deterministic run1/run2 identical up to WALL (453.7 s / 462.8 s).  Nothing here proves any window positivity; NO RH CLAIM in either direction"

_R333_STATUS = "Beta/omega companion-orbit packing round -- reviewer rank 1 after the r327 carrier finding (the dominant group of the argmax block is EXACTLY ONE beta/omega fold pair on all 65 rungs): to every heavy pair g* a companion set O(g*) constructed CANONICALLY FROM ITS SOURCE DATA (same dyadic gmax bin + same fold parity (nwin, sign(G1)) + the maximal inner interval, BOUNDARY_F 0.10) -- NOT a similarity search (the e4 mutant proves it); theorem clauses (T1) |O| >= c_0 m/(log m)^a, (T2) weight comparability inside the band, (T3) overlap <= 2 (34/34; SPEC_SHA 02b22672e1c3f91d final with record, freeze 5567af41c0d4bc82, pre-freeze commit 279ba0dd / record commit 55d4a832 -- two-commit freeze protocol; contract PRIME.TERMINAL.COMPANION_PACKING.01, experiments-side, NO ledger row; EXT3 anchors NOT adopted -- r329 record uncommitted at spec time, disclosed).  THE TWO THEOREM-GRADE POSITIVES: (T2) THE BAND DISCIPLINE CERTIFIES EXACTLY -- inside one dyadic gmax bin the two-ancestor bound forces 1/4 < gabs(g)/gabs(g') < 4 (derived algebra, Fractions extremes toy sharp near 1/4; live rmin worst 0.2819 > 0.25 and cband worst 3.5473 < 4 on all 69 worlds): b = 0, c_1 = 1/4, the r327 lambda-pair failure repaired at band level; (T3) overlap is PARTITION-EXACT (max membership 1 <= 2, the factor-2 reserve unused); the composed chain q_max <= A1*/L <= ng hga/L <= Q_b = ng kappa/(|O| rmin) has worst slack violation 0.0 (exact algebra live; kappa = L1_atom/L the measured cancellation transfer, a stable factor ~3-4, min 3.18 -- NOT the blocker).  MAIN VERDICT ORBIT_TOO_SHORT on the sealed six-letter tree (TARGET_LEAK / WEIGHT_COMPARABILITY_FAIL / COMPANION_PACKING_POLYLOG / BOUNDARY_FINITE_HEAD / COMPANION_PACKING_SUBCRITICAL / ORBIT_TOO_SHORT): T1 fails at ALL a in (0, 1, 2) (min-cal c_0 0.0238/0.1055/0.4674, violations 18/17/15 of 39, named 0/4) and the composed bound fails at all a (C_Q 233.7/54.5/12.7, violations 19/14/10, named 0/4); the subcritical fallback delta = e(hgn) = -0.004 < 0.112 but halves +0.148/+0.674 STRADDLE -- UNDECIDED by the sealed stability rule.  THE STRUCTURAL FINDING OF THE ROUND: THE BOUNDARY CASE IS THE RULE, NOT THE EXCEPTION -- on 44/65 rungs the dominant pair sits in the outer 10-percent margin of the masked support (edge distance d* med 0.072, min 0.002), the inner-interval orbit is EMPTY at three of four named spikes (kz53/kz83/kz55 |O| = 0; kz67 |O| = 2) while the ONE-SIDED census shows same-key companions DO exist on the edge side (kz53/kz83/kz55: 1 each, up to 25 at kz37): the spike coincidence is an EDGE phenomenon and any viable packing theorem must be stated one-sidedly at the edge, not on the inner interval.  SPIKE HARDNESS TEST: all four named rungs are SMALL_ORBIT + HEAVY_BAND simultaneously (hgn 14.89/13.43/10.30/15.17 vs med 3.70 AND |O| 0/0/2/0 vs med 5, all at s* = 0, three in case B) -- both mechanisms fire together.  WORLDS: twin w13 identical protocol (all exact wards live); EPSTEIN 10 occupied bands vs w9 13, live orbit; SCRAMBLE |O| = 0 -- the orbit construction DECAYS on SCRAMBLE as predicted.  Slim anchors bit-near (r314 identity 4.5e-17; r306 C_2 1.069 0/57; r316 n 65 + rho quartet + C_small; r327 C_NG 2.6351 0-viol named 4/4 + nwin histogram (0, 65, 0) EXACT + kz53 bshare 0.888 + gap med 0.807 + align med 1.000 + thirds (21, 29, 15) EXACT).  Must-fails: e1 orbit-after-qmax-sight AST-CAUGHT (trs) / e2 band-posthoc CAUGHT twice (AST rho + toy width 2 != 0) / e3 synthetic overlap triple LOUD (break 1 EXACT, 3 > 2 REFUSED) / e4 similarity-pick CAUGHT (exact toy set mismatch, wrong-parity group selected) / m5a+m5b scope-flagged.  Protocol: smoke 34/34 (0.5 s) NO amendment; calibration = first full evaluation 34/34 (36.9 s) NO amendment; only post-freeze change the record-table insertion; deterministic run1/run2 timing-normalized diff EMPTY.  R-next direction typed census-grade: the one-sided EDGE companion construction (the boundary case as the main case) or the martingale second route; the r324 MEASURED composition (m_0* 10^59.6) stays the honest state of the terminal route.  Nothing here bounds anything beyond the measured rungs; NO RH CLAIM in either direction"

_R334_STATUS = "Capacity-fork round for L* (reviewer rank 2: the Fold Capacity Packing language -- L* re-read as a distributed two-weight sampling problem via the polynomial capacity Cap_{mu,N}(E) = inf{int p^2 dmu : deg p < N, |p| >= 1 on E}, the exact level-set formula and the K1/K2/K3 chain) -- machinery + census + honest typing, NO L* claim (26/26; SPEC_SHA d5698a1d2d9c96c3 final with record; pre-freeze commit 67833ecf / record commit 9bf3a0aa under the two-commit freeze protocol; contract PRIME.LSTAR.FOLD_CAPACITY.01, experiments-side, NO ledger row; deterministic run1/run2).  MACHINERY (certified): dual active-set capacity solver with KKT certificate on every solve (138723 solves, 0 failures), exact-Fraction enumeration route (all signs x all active subsets on the rational WD kernel) reproducing the f64 solver to 6.8e-16 on every argmax subset, hand toys 24/11 / 3 / 8 / 75/49 exact, point-capacity identity Cap({y}) = 1/K_N(y,y) verified against the independent r283-FS Christoffel route on all 104 w9 atoms (9.7e-16; diag max 0.97001 == r284 record), mp dps-40 wards <= 2.8e-14.  VERDICT ALLSET_NEEDED + WORLD_SEEN + CAPACITY_CONTENT (restatement rule does NOT fire, on two clauses): (1) INTERVAL-VS-ALL-SET on the four small exact instances (S <= 16, ALL 2^{S_-}-1 subsets, Cap_abs by full sign enumeration): I1/I2/I3 interval-carried (ratio 1.0000) but I4's supremum is the outermost symmetric NON-interval pair (kappa_all 2.446 vs kappa_int 1.716, ratio 0.7013 < 0.99) -- genuine multi-component sets carry the all-set clause once the geometry offers a separated symmetric pair; sign census: Cap_abs < Cap_+ strictly on up to 44/63 subsets.  (2) K3 CENSUS on w9 + ladder sample (kz18/kz60/kz52) with the sealed world-blind family: kappa_int(w9) = 0.999567 carried by the SHALLOW-EDGE PAIR folds 2/4 (the r284 two-atom extremal band, NOT the singleton 0.97001); the interval-capacity margin 1 - kappa_int (4.8e-4 / 4.3e-4 / 2.6e-5 / 9e-6 at N_w 142/184/388/878) shrinks along the ladder like the r286 spectral margin, same locus -- a NEW source-pure near-wall coordinate; C_lev 0.90..1.06, products 0.90..1.06 straddle 1 across the live rungs: K3 with these families has NO reserve.  (3) THE STRUCTURAL CEILING (gate-side): the extremal direction's own chain gives kappa_lev(eig) x C_lev(eig) = 1.00850632 >= lambda_max - 1e-9 -- no (K1, K2) pair valid for all polynomials can put the product below lambda_max: the capacity route can never yield more margin than the spectral margin itself.  (4) WORLD CHECK: EPST kappa_int 1793.99 / SCR 8.51e6 -- BOTH dead worlds reach >= 1 on the interval clause alone (kappa > 1 directly certifies lambda > 1); MAIN/TWIN < 1 everywhere; rational twin at 1e-8 twin-stable (kappa/C_lev devs <= 5.5e-9, dose-zero bitwise).  Split-ratio census R_split med 0.978 / max 1.097: component splitting is nearly free on the measured superlevel sets (the Muckenhoupt structure is benign here).  Must-fails: m1 eigenvector-capacity + m4 kappa-by-sight AST-FLAGGED, m2 wrong-measure layer sum breaks 4.3e4, m3 incomplete enumeration CAUGHT, m5 KKT mutant breaks 1.0e-2; infeasible sign branches discarded by the sealed weak-duality ceiling.  Disclosed calibration amendment a1 (solver numerics: absolute constraint-scale stopping, iterative refinement, backward-error-scaled certificate tolerances; no bar, band, family or adjudication rule moved).  Honest limits: every kappa/C_lev is measured on sealed families (lower bounds of the true suprema, never certificates); C_lev on S_- > 160 worlds is a strip upper bound; the world check is a consistency statement about the instrumented families.  Nothing here proves any window positivity; NO RH CLAIM in either direction"

_R335_STATUS = "One-sided edge-companion formulation after the r333 structural finding (the boundary case as the main case): for every dominant beta/omega pair g* a ONE-SIDED edge orbit O_e (same dyadic gmax bin + same fold parity, window [ps, ps +- R] toward the interior, R = the masked support radius W/2, a-priori parameter-free) PLUS the margin mass/ancestor census, combined into the exact DICHOTOMY q_max <= min(Q_e, M_b) with Q_e = ng kappa/(|O_e| rmin_e) (partition chain) and M_b = ng kappa S_marg/L1 (via gabs(g*) <= S_marg, exact) -- EITHER many companions OR small edge mass (36/36; SPEC_SHA 950c9b9ee96298e0 final with record, freeze a1f4c0dd97edcbf4, pre-freeze commit ec0fd5d5 / record commit 3fa88d02 -- two-commit freeze protocol; contract PRIME.TERMINAL.EDGE_PACKING.01, experiments-side, NO ledger row; EXT3 = the r329 record 12 anchors ADOPTED as pure test rows, committed 8cbd95f9 checked via git log).  MAIN VERDICT EDGE_ORBIT_ALSO_SHORT on the sealed five-letter tree (TARGET_LEAK / WEIGHT_COMPARABILITY_FAIL / EDGE_PACKING_GO / EDGE_PARTIAL / EDGE_ORBIT_ALSO_SHORT): no clause certifies -- T1-edge fails at all a (c_0 0.0595/0.2637/1.1686, viol 43/40/38 of 51, named 0/4); mass arm C_M 141.8/33.1/7.7 with 17/15/11 violations; dichotomy C_D 141.84/33.06/7.71 with 14/11/6 violations (worst kz73/kz76/kz61 + deep kz95/kz98/kz109).  THE TWO STRUCTURAL FINDINGS: (1) THE SPIKES FLIP TO COVERED -- the MASS arm covers all four named rungs at EVERY a (kz53 B^D_1 12.51 / kz83 20.47 / kz67 2.62 / kz55 11.86 vs C_D(1) 33.06, reserves 1.6x-12.6x, all four typed arm M): the r333 spike blocker is resolved POINTWISE AT THE NAMED RUNGS by the edge-mass clause; what violates now is the mid-band family (margin share 0.18-0.28, both arms 6-10).  (2) THE INWARD WINDOW MISSES THE EDGE COMPANIONS: at the named spikes |O_e| = 1 (g* alone; 6 inner-empty rungs gained 0) -- the r333 one-sided same-key companions sit OUTWARD of g* (between the support edge and ps), not inward; the spike coverage comes ENTIRELY from the mass arm.  THEOREM-GRADE PIECES CARRIED: T2 band discipline on the edge orbit (rmin_e worst 0.3162 > 1/4, cband_e worst 3.1630 < 4 on 81 live worlds), T3 overlap partition-exact (membership 1 <= 2), BOTH arms exact live (worst slack violation 0.0), arm partition exact (O 15 / M 62 of 77); kappa med 3.840 min 3.1726.  CERT: delta = e(hgn) = -0.004 halves +0.148/+0.674 STRADDLE (exact r333 continuity, census only); e(B^D_1) = +0.517; EXT3 cohort e(m Q_dich) = -3.313 (census-grade), no EXT3 rung among the worst dichotomy violators at a = 1.  WORLDS: twin w13 identical protocol; EPSTEIN operates (|O_e| 6); SCRAMBLE |O_e| = 2 vs inner 0 -- the one-sided orbit does NOT decay on SCRAMBLE the way the two-sided did (honest negative: the support-radius reach is permissive).  Slim anchors bit-near (r314 identity 4.5e-17; r306 C_2 1.069 0/57; r316 n 65 + rho quartet + C_small; r333 record: boundary 44/65 EXACT, |O_in| 5/0/52 EXACT, named inner quartet (0,0,2,0) EXACT, named hgn quartet, d* med 0.072, inner band worst 0.2819/3.5473 bit-near).  Must-fails: e1 reach-after-sight CAUGHT twice (AST rho + toy 1.0 != 0.5) / e2 arm double-count LOUD (sum 4 != 3, break 1 EXACT) / e3 orbit-after-qmax-sight AST-CAUGHT (trs) / e4 mass-from-target AST-CAUGHT (S3) / m5a+m5b scope-flagged.  Protocol: smoke 36/36 (0.6 s) NO amendment; calibration = first full evaluation 36/36 (159.9 s) NO amendment; only post-freeze change the record-table insertion; deterministic run1/run2 timing-normalized diff EMPTY (165.7/161.2 s).  Named successor typed: the packing language is exhausted at the edge -- the reviewer's martingale second route (NAMED ONLY, not executed); the r324 MEASURED composition (m_0* 10^59.6) stays the honest state of the terminal route.  Nothing here bounds anything beyond the measured rungs; NO RH CLAIM in either direction"

_R336_STATUS = "Chebyshev Toeplitz+Hankel parity-section round for L* (reviewer rank 3, the last pre-authorized L* arm after the r334 capacity cap): map the window hull affinely onto [-1,1], x = cos theta; with the signed cosine moments c_r = sum (mu_j - nu_j) cos(r theta_j) the EXACT identity int p^2 d(mu-nu) = sum a_k a_l (c_|k-l| + c_{k+l})/2 makes the L* matrix a finite Toeplitz+Hankel parity section, congruent (exact rational congruence M = S V_+^T T_M(c) V_+ S) to the EVEN parity compression of the full symmetric Toeplitz section -- the mirror of the v549/v550 odd-sector step-over machinery (25/25; SPEC_SHA 9e4bf4f129405a64 final with record; pre-freeze commit d38b43c1 / record commit in the same change -- two-commit freeze protocol; contract PRIME.LSTAR.PARITY_SECTION.01, experiments-side, NO ledger row).  THE THREE KILL TESTS ADJUDICATED: (1) representation EXACT -- toy identity bit-equal in Fractions (113856919/26790750), parity dilatation exact, f64 identity 2.2e-15 on w9 / <= 5.9e-15 on the ladder sample (bar 1e-12), section flip signs clean (min eig M_184 = +5.7e-8 > 0 > -1.2e-8 = M_185, negative inertia exactly 1) -- CARRIES; (2) world-comparative negative-window geometry -- PARITY_WORLD_BLIND: all four sealed statistics blind under the r281 distance rule; the near-separation (Fejer floor at N_w positive on MAIN/TWIN +2.16e-3, negative on EPST/SCR/HL2 -1.205/-0.804/-0.655) is broken by SMOOTH, a dead world (crossing 28) with POSITIVE Fejer floor +2.05e-3 -- SMOOTH dies without local negative mass, so no local symbol statistic of this family is world-complete -- FAILS; (3) blind predictor (source-pure, Fejer-primary, AST-audited) -- PREDICTOR_ORDERING: 42/42 rungs IN the sealed 1-octave band (max dev 0.224; w9 n_pred 216 vs crossing 185), spearman +0.999, but controls 1/4 in band (EPST 80 vs 26, SCR 37 vs 22 IN, SMOOTH None, HL2 98 vs 26) -- LAW not awarded, the ordering rides the N_w scaling -- PARTIAL.  MAIN VERDICT: PARITY_FINITESECTION_CARRIER (f_366 attains -5.07 in 127 negative zones, total measure 0.2766 pi, while the 184-section is PD -- the positivity IS a finite-section effect) + NEGATIVE_WINDOW_STEP_OVER(clause ii: the Fejer mean is positive on all 183 active parity modes of MAIN and TWIN while 34 Dirichlet readings sit in Gibbs zones -- the mean steps over, exactly the T151 template) + PARITY_WORLD_BLIND + PREDICTOR_ORDERING + SCHUR_LEDGER(Fejer block size 0 and positive floor on 42/42 rungs, min +4.44e-4 at kz64; dead Fejer blocks 34/29/0/11 -- the C3 shape holds with the EMPTY block on every live rung).  THE HONEST CENTRAL NEGATIVE: the w9 Fejer floor does NOT dip at the crossing (+2.16e-3 at 184, +1.99e-3 at 185) -- the L* flip is NOT a local-mass event at Fejer resolution, it lives in the sharper two-atom extremal of r284; the predictor fires at crossing +9..+39 (the Fejer width must shrink past the wall).  BANKED: the Fejer floor as a SECOND source-pure near-wall coordinate (falls ~5x along the ladder where 1 - kappa_int falls ~50x -- not the same number in disguise).  Must-fails m1/m3 exact CAUGHT (odd-parity and unmapped-window differences exactly nonzero in Fractions), m2/m4 AST-FLAGGED.  Deterministic run1/run2 byte-identical up to WALL (5.0 s).  With kill test 2 failed and kill test 3 partial, the reviewer's own rule reads: the parity-section lane does NOT stay open as an L* proof arm; its exact coordinate (C1) and the Fejer floor are banked.  Nothing here bounds anything beyond the measured rungs; NO RH CLAIM in either direction"

_R337_STATUS = "Fold-martingale round for the terminal (the reviewer's second route, pre-named at r333/r335, after the exhaustion of the packing language): the signed fold-group masses of the argmax block read as an adapted process along the SEALED dyadic source-scale filtration (adjudicated a-priori BEFORE the freeze against m-sorted order: parameter-free / theorem-adjacent / canonical coarse-to-fine; the e3 mutant proves the protocol audit bites), with the exact telescope X_K == x_{j*}, the exact CS ward zr <= sqrt(n_act) and the exact identity q_max = zr kappa sqrt(V)/L1 warded live (37/37; SPEC_SHA 617a83a6b3105acb final with record, freeze 5460c2fa54983956, pre-freeze commit 30ac0cb5 / record commit d0d272e3 -- two-commit freeze protocol; contract PRIME.TERMINAL.FOLD_MARTINGALE.01, experiments-side, NO ledger row; EXT3 = the 12 r329 anchors as pure test rows, r335 adoption verbatim).  MAIN VERDICT MARTINGALE_STRUCTURE_ONLY on the sealed five-letter tree (TARGET_LEAK / NOT_A_MARTINGALE / WORLD_BLIND / MARTINGALE_MAXIMAL_GO / MARTINGALE_STRUCTURE_ONLY): the structure IS there -- the Z-maximal certification carries at the Azuma form zr <= C_Z(1) sqrt(log m), C_Z(1) = 0.7364, 0 test violations of 51 incl. all 12 EXT3, named 4/4 (even the bounded form b = 0 misses by only 2) -- but the derived maximal arm is too weak: B^C_a fails at every a (viol 18/13/11), mid-band 5/6, no m_0*.  THE THREE STRUCTURAL FINDINGS: (1) the certification is tight but nearly structureless -- c* med 0.949: ONE increment dominates the quadratic variation (the r324 single-heavy-scale finding recurs in SIGNED form), zr med 1.1012 essentially flat; contraction med exactly 0.500 (supermartingale surrogate at the threshold); (2) THE MID-BAND BLOCKER DISSOLVES under the martingale arm -- head-to-head at a = 1: kz73 B^D_1 54.40 -> B^C_1 0.399 / kz76 53.59 -> 0.483 / kz61 48.91 -> 0.755 / kz95 41.96 -> 0.352 / kz98 41.68 -> 0.400 / kz109 40.90 -> 0.299 vs C_C(1) 0.5293: coverage 5/6 (only kz61 at 1.43x), improvement 70x-180x over the r335 dichotomy, pointwise q_max <= A_z on 77/77 rungs; (3) the violation margin MIGRATES to the deep anchors and the spikes -- A_z undercuts the mass arm on every rung (letters A 77 / M 0), the freeze collapses 33.06 -> 0.5293, and the new a = 1 violators are EXT3 kz51 2.09 / kz62 2.03 / kz54 1.72 / kz123 1.72 / kz125 1.04 + named kz53 1.05 / kz67 0.845 / kz83 0.721: the r335 mass-arm spike coverage is LOST inside the min (a two-constant certification, each arm against its own freeze, is NOT this round's sealed contract -- named residual direction only).  CERT: e(B^Z_1) = e(B^C_1) = +0.059 vs the r324 route's +0.172 (3x flatter measured growth, but the pointwise cert fails); delta = e(hgn) = -0.004 halves straddle (exact r333/r335 continuity).  WORLDS: twin identical protocol; EPSTEIN zr 1.027 contr 0.0; SCRAMBLE zr 1.1159 / contr 0.500 vs ladder med 1.1012 / 0.500 -- DISTINGUISHED by a 1.3-percent zr margin ONLY (honest negative: the zr statistic is essentially world-blind in magnitude; the arithmetic content lives in the calibrated constants, not in the existence of the structure).  Slim anchors bit-near (r314 identity 4.5e-17; r306 C_2 1.069 0/57; r316 n 65 + rho quartet + C_small; r333 record boundary 44/65 + named inner quartet + band; r335 record arms O 15 / M 62 EXACT + named B^D_1 quartet + C_D(1) 33.0599 viol 11 EXACT + the a = 2 violator set == the mid-band six EXACT + edge band 0.3162/3.1630; r324 chain e_tot +0.172 EXACT + C_M2 2.2557 + the seven m2 violators EXACT + m_0* solve 10^59.6).  Must-fails: e1 zward-posthoc CAUGHT twice (AST rho + toy 3.0 != 1.0) / e2 increment-from-qmax AST-CAUGHT (trs) / e3 filtration-posthoc protocol-CAUGHT twice (AST rho + toy order (2,1,0) != (0,1,2)) / e4 bin-drop LOUD (break 1 EXACT) / m5a+m5b scope-flagged.  Protocol: smoke pass 1 = 33/37 (the probe's own scope audit caught the combined-arm letter 'Z', a withheld identifier; disclosed pre-freeze fix: letter renamed to 'A', no rule moved), smoke pass 2 = 37/37; calibration = first full evaluation 37/37 (166.8 s) NO amendment; only post-freeze change the record-table insertion; deterministic run1/run2 timing-normalized diff EMPTY (176.5/169.7 s).  Direction typed census-grade: the mid-band is no longer the blocker -- the residual margin is the deep-anchor/spike family under the collapsed freeze; the r324 MEASURED composition (m_0* 10^59.6) stays the honest state of the terminal route.  Nothing here bounds anything beyond the measured rungs; NO RH CLAIM in either direction"

_R339_STATUS = 'Density-martingale / moment-dictionary round for the terminal (round 339, the reviewer reformulation: transport of mass density through the fold genealogy instead of a maximum): the canonical fold genealogy over the m final atoms a_i = |PDelta_i| (Leg 0 adjudicated and SEALED BEFORE the freeze: the iterated r270 adjacent pairing, PAIR_OFFSET 0 -- parameter-free / construction-canonical / position-contiguous; balanced bisection kept as the sensitivity alternative; leaves-inside-blocks refused; the e4 protocol mutant proves the audit bites), with X_k = d(V_k)/d(root) a nonnegative martingale from mass conservation ALONE and the exact moment dictionary E[X_inf^2] == m M_2, E[X_inf^3] == m^2 M_3 (36/36; SPEC_SHA 822d6bff564d88ba final with record, freeze a845041cdf866543, pre-freeze commit 907ebfd1 / record commit 7863495f -- two-commit freeze protocol; contract PRIME.L2.FOLD_DENSITY_DICTIONARY.01, experiments-side, NO ledger row; EXT3 = the 12 r329 anchors as pure test rows, r335 adoption verbatim; INDEPENDENT of r337 by the reviewer verdict-reading rule -- r337 tested the RAW signed fold-mass process, the density per remaining descendant is a martingale by algebra).  MAIN VERDICT LOCAL_INFLATION_SUPERCRITICAL on the sealed five-letter tree (TARGET_LEAK / MASS_TREE_NOT_CANONICAL / DENSITY_MARTINGALE_EXACT / GOODTREE_A2_ONLY / LOCAL_INFLATION_SUPERCRITICAL): NEITHER Gamma budget certifies -- the full budget W_F = prod_k Gamma_max(k) violates 44/43/40 of 51 at a = 1/2/3 (C_F 39.9133/8.9841/2.0222, named 1/4), the good tree (heavy jumps max R_c > 3/2 removed, the band-floor 1/4 tie) violates 33/20/11 (C_G 2.8325/0.6393/0.1443); e(W_F) = +0.956 DECIDED supercritical (halves +1.700/+1.756) -- the worst-case per-level product language is capped too, said honestly.  THE EXACT LAYER STANDS AT THEOREM GRADE: the martingale identity exact on 81 live worlds (per-node 2.2e-16, unit mean 4.4e-16, cubic recursion 1.2e-15, envelope viol 0.0, Jensen 0.0; Fractions BIT-EQUALITY on w9 + w13, 76 nodes, symbolic dev == 0) and the dictionary exact against the r324 chain (4.9e-16 / 7.8e-16 / 2.5e-16) -- the terminal target IS E[X_inf^3] <= C (log m)^A, and the banked r306 C_2 = 1.069 (0/57, re-gated here) already certifies A = 2 on the 57-rung set.  THE THREE STRUCTURAL FINDINGS: (1) THE GAP IS THE FINDING -- the true expectation e(m^2 M_3) = +0.112 grows 8x slower than the worst-case budget e(W_F) = +0.956: Gamma_max is dominated by NEAR-LEAF DEGENERATE PAIRS (per-level med profile 1.05 -> 3.99 pressing against the balanced-pair ceiling 4; the deep half of the levels carries med 0.712 of log W_F) where hardly any PATH MASS sits -- the measured reason the naive Reverse-Holder budget fails, and the concrete R341 instruction: the Bellman argument must weight Gamma by path probability, not take per-level maxima.  (2) NO sharp world or family separation in the Gamma_max census (named spikes W_F med 324.33 vs mid-band 404.57 vs ladder 265.54; SCRAMBLE W_F 51.76 BELOW the ladder median 223.86 -- the census is world-blind in this reading, honest negative) but the DICTIONARY itself separates (SCRAMBLE m^2 M_3 = 20.59 vs ladder med 6.22); the worst W_F violators are the EXT3 deep anchors kz42 (18.29x at a = 3, W_F 4364.9) + kz51/62/123/54/125 -- the r337 deep-anchor margin recurs in the density language.  (3) the predictable log drift is strictly <= 0 (Jensen-exact, profile sum -1.1392, monotone-deepening toward the leaves) but NOT period-4 (r4 0.934 / r4c 0.957 vs R4_BAR 0.5; per-rung r4 med 0.784 on the 42 rungs with K >= 8) -- the clause-5 coboundary subtraction does not apply (nothing to subtract exactly).  Census: alt-tree W_F med 487.03 (the sealed pairing tree is the SHARPER canonical form); hsh med 0.872 max 1.000, heavy rungs 77/77; levels K 5..10; kz53 is the ONE spike with its Gamma argmax mid-tree (level 2, Gk* 4.303 -- the r324 single-heavy-scale event visible as an early heavy fold) while every mid-band rung inflates at the LAST fold level; bridge envelope (NOT composed) a = 3: 18.2922 would give m_0* 10^30.4 vs the r324 route 10^59.6 -- typed envelope only, preparation for R341.  Must-fails: e1 wrong child weighting CAUGHT exact (break 1/10) / e2 dictionary m-for-m^2 CAUGHT exact (break 5/3) / e3 Gamma-from-target AST-CAUGHT (S3) / e4 tree-posthoc protocol-CAUGHT twice (AST rho + toy offset 1 != 0) / m5a+m5b scope-flagged.  Protocol: smoke 36/36 (0.7 s) NO amendment; calibration = first full evaluation 36/36 (170.4 s) NO amendment; only post-freeze change the record-table insertion; deterministic run1/run2 timing-normalized diff EMPTY (169.7/168.9 s).  Direction typed census-grade: the exact density martingale + moment dictionary are BANKED machinery for R341 (Bellman with path-probability weights); the r324 MEASURED composition (m_0* 10^59.6) stays the honest state of the terminal route.  Nothing here bounds anything beyond the measured rungs; NO RH CLAIM in either direction'

_R340_STATUS = "Weighted Cauchy-Binet transport round for L* (round 340, the new L* base architecture after the r334 capacity cap and the r336 parity blindness: transport instead of norm bound): the signed Cauchy-Binet split D_n = det H_n(mutilde) = sum_E W - sum_O W with W(I) = (prod |w_i|) Delta(x_I)^2 makes L* the family of weighted inequalities sum_O W < sum_E W for n <= N_w (Sylvester dictionary gated); the transport candidate is an exact flow on the sealed canonical fold-exchange graph (companions = nearest free mu atoms per side, step cap 2, position adjacency == fold adjacency gated on w9; exact edge ratio W(J)/W(I) = (|w_x|/|w_y|) prod ((x-z)/(y-z))^2 bit-equal on 192 small-model edges + w9 golden-config log ward 2.3e-14), and max-flow = weighted Hall duality is measured with exact integer Dinic + full 2^|O|-1 Hall-cut enumeration on the small exact models (26/26; SPEC_SHA 86587b4895e95689 final with record, freeze 82c4d1839386a853; two-commit protocol pre-freeze 3736af89 / record in the same change; contract PRIME.LSTAR.CAUCHYBINET_HALL_TRANSPORT.01, experiments-side, NO ledger row).  MAIN VERDICT: CUT_REDUCTION_FAIL -- the interval-Hall reduction (the round's central structural hypothesis: minimal weighted Hall cuts = Gale-order interval ideals, which would have re-read 1-kappa_int as a dual Hall slack) is REFUTED at the smallest exact scale: 5 of 9 fully enumerated loci carry NON-ideal argmin cuts (antichain sections and mid-order singletons pinned to the shallow negative atoms; the principal-ideal family misses the exact minimum by 1.17x..10.2x, growing toward half-filling) + SOURCE_EXCHANGE_INSUFFICIENT (one live locus: on the PD instance I2 the elementary edge set fails to cover exactly at half-filling depth n = N = 5, deficiency 0.023 -- everywhere else coverage is integer-exact with strict reserve D_n > 0: TOY 2/2, F1 3/3, F2 4/4, I2 4/5) + EXTREMAL_CUT NOT carried (W9EDGE binding cut = up-ideal, 236/504 members, dual slack -6.18e-2; W-fraction containing BOTH r284 extremal atoms (folds 2/4) = 3.86e-3 << 0.9 -- the extremal pair is a spectral object, not the Hall-cut carrier) + TRANSPORT_WORLD_BLIND (THE STRUCTURAL FINDING: the shallow-edge prefix of EVERY world, MAIN included, is locally indefinite from n = 2 on its own configuration space -- W9EDGE D signs +,-,-,-,+,+ with resolved relative deficit -9.7e-3, controls break at n = 1; the full-window positivity is a GLOBAL rescue, not a local edge property, the flow-side mirror of r336 PARITY_WORLD_BLIND) + NEW_COORDINATE (the ladder edge Hall slack is NEGATIVE on 42/42 rungs, -0.13..-0.18, while every margin is positive -- sign-opposite to 1-lambda_max and to the r334 1-kappa_int column: a new coordinate, not a restatement) + TWIN_LEDGER (same generator, dual slack rel dev 4.8e-8, dose-zero bitwise).  Exact anchors: w9 D_1 = 3.473206 and D_2 = 2.514889 bit-equal over all 67161 pair configurations (E 3.041804 / O 0.526915); hand toy D_1 = 5/3, D_2 = 5/6 (E 1 / O 1/6), D_3 = -1/48; JF9 + I2/I3/I4 identities bit-equal at every n.  Must-fails: m1 unsquared ratio exact diff 6 CAUGHT; m2 posthoc edge library AST-FLAGGED + toy value CAUGHT twice; m3 flow-gift AST-FLAGGED (REC_LAM); m4 Kasteleyn gauge shifts D_2 by exactly 2 sum_O = 1/3 (the r282 no-go boundary reproduced) CAUGHT; m5 cut-census CAUGHT (14 != 15).  Protocol: smoke pass 1 = 23/26 (two gate-side must-fail witness slips, fixed pre-freeze, disclosed), smoke pass 2 = 26/26; calibration = first full evaluation 26/26 (39.9 s) NO amendment; record runs 40.7/40.4 s timing-normalized diff EMPTY.  Consequence typed honestly: the reviewer's interval-Hall route to a quotable theorem does NOT open (no R341 GO); what is banked: the exact Cauchy-Binet/Hall machinery, the local-edge indefiniteness of every world, and the sign-opposite edge coordinate.  Nothing here bounds anything beyond the measured models; NO RH CLAIM in either direction"

_R342_STATUS = "Two-atom-extremal round for L* (round 342, the U1 main find of the r338 door-2 full revision solved as its own problem): at the binding point L* is EXACTLY the determinant condition c^2 < (1-d1)(1-d2) with d_k = v_k K_N(y_k,y_k) = E_kk, c = sqrt(v1 v2) K_N(y1,y2) = E_12 at the r284 shallow-edge pair (folds 2/4, below log 2), and the probe measures the mp-exact (d1,d2,c) ladder on 42 core + 15 r286 extension + the 12 r329 EXT3 anchors as PURE TEST rows + the rational twin, with sealed fits against the DISCLOSED r338 /tmp priors (-0.71/-0.66/-3.13), the exact Schur sufficiency dressing (L* <=> {lambda_rest < 1} AND {dressed pair determinant}), the source-explicit weight dictionary (digamma closed form F_A(xi) = -log pi + Re psi(1/4 + i xi/2) for the arch layer + the EXACT two-cell tent closed form of the prime layer), and the sealed world census PR/kappa_int incl. the FIRST kappa_int evaluation on SMOOTH and HL2 (38/38; SPEC_SHA b09f8ccdcfdedc16 final with record, freeze 4ca125c7906149bf, pre-freeze commit bdc0b439 / record commit 5c80e561 -- two-commit freeze protocol; contract PRIME.LSTAR.PAIR_EXTREMAL.01, experiments-side, NO ledger row).  MAIN VERDICT PAIR_LAW_FOUND on the sealed four-letter tree (PAIR_LAW_FOUND / PAIR_CARRIES / RESTATEMENT / BLIND): L1 the p/q/c laws are halves-stable on the 57 (slopes -0.754/-0.645/-0.697, curvatures +0.305/+0.299/+0.308 <= 0.35) + L2 the EXT3 pure test extends (11/11/11 of 12 in the 0.5-decade band) + L3 the source dictionary carries (median v_pred rel dev < 1e-4, max 9e-4; digamma dictionary devs 1e-5..2.4e-3 at bar 0.02 -- the pair weights are CLOSED-FORM source objects) + L4 the alpha composition closes (alpha_pair 3.341 vs alpha_full 3.332 vs composed 3.333; 42-only 3.059 == r286 3.06); kernel side law-grade, not closed-form.  + PAIR_WORLD_COMPLETE(union {PR >= 3.0} u {kappa_int >= 1}: dead 4/4, live spared on both) with the HONEST STRUCTURE: the PR clause ALONE FAILS (at their OWN N_w the dead worlds are also concentrated, PR 1.80..2.92 < 3.0; the r338 'PR 5-10 diffuse' lives at the crossing degrees, reproduced 7.02/9.72/4.97/8.29 == r284) while the KAPPA_INT CLAUSE ALONE IS WORLD-COMPLETE: EPST 1794 / SCR 8.509e6 (== r334 records) / SMOOTH 2.193 / HL2 1964 (first evaluation -- the U2 gap closed) all >= 1, live MAIN/TWIN 0.999567 < 1 -- the first measured world-complete criterion of the L* lane.  THE STRUCTURAL FINDINGS: (1) the pair is folds (2,4) on 69/69 windows, pair mass 0.9352..0.9994, PR 1.61..1.94 -- the two-atom extremal is LADDER-UNIVERSAL incl. the fresh deep family; (2) the entire alpha ~ 3.3 decay is the bookkeeping-exact composition a_p + a_q + rho_r - a_(p+q) with the OPEN analytic remainder rho_r = 2.624 (the cancellation exponent of r_det = 1 - c^2/pq, halves-curved -0.767 -- the concretized specialist question); (3) THE R343 MATERIAL: the rest margin 1 - lambda_rest decays parallel to the full margin (slope -3.276, offset ~20x) while the Schur-DRESSED pair reserve r'_det is FLAT (slope +0.018, w9 value 0.303) -- the dressed determinant condition does not degrade with depth, the O(1) certificate candidate; (4) EXT3_FAMILY_BREAK([56]): kz56 has R2 = 1.836 > 1.5 -- the r338 2x2-uniformity reading (12-40 percent) does not extend unmodified to the small-gap family (R2 cohort medians core42 0.205 / ext15 0.188 / ext3B 0.437 / ext3A 0.557, the r329 lesson measured again); (5) the r285 sub-classical Christoffel exponent 0.38 is the deep-rung LATE-window growth (six-rung census, late slopes 0.336..0.608).  Honest negatives: PR alone does not separate (SCR even has pair mass 0.922 at its own N_w -- what separates is whether the pair block crosses 1); r_det is halves-curved; the kernel side (why v_k K_N -> 1 with deficit ~N^-0.7 at the hard edge) remains without closed form.  Disclosed calibration amendments a1/a2 (numerics normalizations: det residual against pq + c^2; depth-scaled mp m2 bars), nothing else moved.  EXT3 margins all positive (first L*-lane evaluation of the r329 anchors, min 4.20e-9 at kz127).  Deterministic run1/run2 byte-identical up to WALL (214.6/212.3 s).  Nothing here bounds anything beyond the measured rungs; NO RH CLAIM in either direction"

_R341_STATUS = 'Path-weighted Bellman / Reverse-Holder round for the terminal (round 341, the terminal main round after the r339 dictionary: the two-arm theorem candidate with path-probability weights instead of per-level maxima, executing the r339 build instruction and the r337 two-constant directive -- each arm certified against its OWN freeze): on the sealed iterated r270 pairing tree (FDD machinery imported verbatim) the probe put the exact PATH LAYER at theorem grade -- the cubic-tilted tower identity E[X_inf^3] == E_Q[prod_k Gamma(V_k)] with steps p~_c = p_c R_c^3/Gamma(v) (the naive untilted E_P[prod Gamma] is FALSE, toy break 7/18 EXACT = must-fail e1), the Phi-Gamma identity sum_c Phi(c)/Phi(v) == Gamma(v) with Phi = A^3/n^2, the stopped leaf partition at tau = first heavy level (max R_c > R* = 3/2) with the exact hand-off E3h <= (m q_max)^2 msh (the r335 q_max currency entering the cubic layer exactly, reserve med 4.8x min 2.1x), and the good eps-chain B_k with exact envelope E3g <= W_B = prod(1 + eps_k) -- all Fractions BIT-EQUAL on w9 + w13 + three sealed toys (7/18, 6/125, 20/9, 261/125, 31/16 = 43/32 + 19/32, slack 3/16), f64 worst 8.6e-16 on 81 live worlds (38/38; SPEC_SHA 7a9cf6b3fe24d0d7 final with record, freeze f0d2c744c46942bc, pre-freeze commit 86f523e8 / record commit 70d01ef8 -- two-commit freeze protocol; contract PRIME.L2.FOLD_DENSITY_REVERSE_HOLDER.01, experiments-side, NO ledger row; EXT3 = the 12 r329 anchors as pure test rows; r339 record anchors W_F med 265.54 / e(W_F) +0.956 / e(m2M3) +0.112 and the r324 chain e_tot +0.172 ALL reproduced bit-near).  MAIN VERDICT PATHWEIGHT_ALSO_SUPERCRITICAL on the sealed six-letter tree (TARGET_LEAK / BELLMAN_STATE_NOT_EXACT / RH3_BELLMAN_GO / RH3_BELLMAN_PARTIAL / GOODTREE_A2_ONLY / PATHWEIGHT_ALSO_SUPERCRITICAL): NO arm certifies on its own mid-ladder freeze -- heavy arm C_H = 1.7305/0.3875/0.0868 at a = 1/2/3 with viol 11/11/9 of 51 and NAMED 0/4 (worst violators the EXT3 deep anchors kz51 7.61x / kz54 3.17x / kz62 2.31x / kz42 2.22x -- the deep-anchor margin recurs INSIDE the heavy arm); Form 1 (integrated eps-chain) C_B = 0.4867/0.1113/0.0259 with viol 2/1/1 -- the SINGLE persistent violator is the named spike kz55 (W_B 2.888, 1.41x at a = 2), named 3/4, midband 6/6, EXT3 CLEAN; Form 2 (Psi-weight Bellman, prefactor 1, Psi = (C0 + ln n)^A, six sealed combos) certifies NOWHERE (best (3, 1.0): 23 composed node violations on 17/77 rungs, max ratio 1.237 -- the disclosed a-priori mid-tree risk of skewed-but-good pairs is real).  HONEST LETTER-READING: the name overstates the negative -- the measured path-weighted exponents are NOT supercritical (e(W_B) = -0.214, e(E3h) = +0.313; e(E3g) = -173.3 is a degenerate statistic from good-tree-empty rungs, disclosed); what fails is the freeze-pointwise certification, each arm by a different structured violator family.  THE THREE STRUCTURAL FINDINGS: (1) the r339 thesis CONFIRMED QUANTITATIVELY -- path weighting deflates the worst case 21x at the median (E_P[prod Gamma] med 12.53 vs W_F med 265.54; per-path log-product MAX med 4.20 vs log W_F med 5.58, deflation med 0.80; the path-weighted per-level profile stays 1.05..1.80 where Gamma_max climbs 1.05 -> 3.99; near-ceiling nodes Gamma > 3 carry pm3 med 0.161 of path mass and c3s med 0.173 of E3 -- the near-leaf degenerate pairs ARE defused).  (2) THE STOP AT R* = 3/2 IS TOO EARLY ON THE PATH-MASS SCALE -- the heavy arm inherits essentially everything: hsh med 0.872, msh med 0.833, E3h share of E3 med 0.944 (w9/kz61/kz73/kz130 have an EMPTY good tree), modal stop level 1 (the mid-band stops its WHOLE leaf mass at the first fold level -- the r339 last-level anatomy describes Gamma_max position, not path mass); the split is strongly threshold-UNSTABLE: R_ALT = 7/4 moves hsh med to 0.266 and the E3h share to 0.386 -- R* is a tuning surface, not a canonical constant; WHERE between 3/2 and 7/4 the arms equilibrate is the named open question.  (3) THE GOOD ARM IS ONE RUNG FROM CERTIFYING (kz55 only; eps sums med 0.42 max 2.49 vs loglog m med 1.63, consistent with the reviewer A loglog m + C reading at census grade; the EXT3 deep anchors are Form-1 CLEAN -- the deep-anchor problem lives entirely in the heavy arm).  WORLDS: the path-weighted budget is ALSO world-blind (SCRAMBLE W_B 1.214 inside the ladder range, E3h share 0.997; EPSTEIN the only world where the good arm carries the majority, share 0.427; the dictionary E3 = 20.59 stays the only sharp separator -- honest negative, the r339 blindness recurs).  COMPOSITION typed ENVELOPE ONLY (no certifying letter, NO theorem candidate this round): the a = 3 envelopes [1.3091 + 0.0650] (log m)^3 would give the polylog m_0* = 10^24.0 vs the r324 measured route 10^59.6 and the r306 census reading 10^13.5 -- the honest state of the route REMAINS the r324 measured composition until an arm certifies.  Must-fails: e1 untilted tower CAUGHT exact (7/18) / e2 psi-posthoc protocol-CAUGHT twice (AST rho + toy pick 3 != 1) / e3 rstar-from-target AST-CAUGHT (S3) / e4 tilt-without-n CAUGHT exact (6/125) + m5a/m5b scope-flagged.  Protocol: smoke 38/38 (0.7 s, run pre-commit, disclosed) NO amendment; calibration = first full evaluation 38/38 (170.0 s) NO amendment; only post-freeze change the record-table insertion; deterministic run1/run2 timing-normalized diff EMPTY (168.3/179.0 s).  Direction typed census-grade: the R* mass-balance question and the kz55/heavy-arm freeze structure are the named material for the next terminal round; the r324 MEASURED composition (m_0* 10^59.6) stays the honest state of the terminal route.  Nothing here bounds anything beyond the measured rungs; NO RH CLAIM in either direction'

_R343_STATUS = "Pair-coupling round for L* (round 343, the r342 O(1) certificate candidate under fire: the dressed pair reserve r'_det -- exact anatomy, honest refutation attempt on fresh families, lower-bound adjudication, and the second Schur clause lambda_rest < 1 with its peeling structure): the round's exact spine is the RESOLVENT-CORRELATION IDENTITY r'_det = 1 - M12^2/(M11 M22) with M = the 2x2 pair block of (I-E)^{-1} (gated per rung against the independent full-inverse route, dev <= 1e-6, w9 8.9e-14, plus EXACT-Fractions wards on JF9/I2 via the rational H = (diag(1/v_r) - G_r)^{-1} route incl. the exact leading-minors criterion for lambda_rest < 1), and the exact spectral decomposition Delta d_k = sum alpha_m^2/(1-delta_m), Delta c = sum alpha_m beta_m/(1-delta_m) over the rest eigenmodes (gated 1e-9, measured 2e-13) -- the contract's exact formula r'_det = f(bare scalars, rest coupling vectors) (38/38; SPEC_SHA 9ffc2705f326d625 final with record, freeze a24718fcb8c72f85, pre-freeze commit e652071f / record commit 95fcdcae -- two-commit freeze protocol; contract PRIME.LSTAR.PAIR_COUPLING.01, experiments-side, NO ledger row; ladder = 42 core + 15 r286 extension + 12 r329 EXT3 as BLIND pure-test rows (their dressed columns were never printed in r342) + 6 fresh EXT4 windows from a sealed source-pure selection: domain cap z^2 <= 400000 (the family's von Mangoldt table cap -- the undomained depth-queue head kz277 z=1583 builds a truncated-comb NON-instance, margin -228, an s2 scoping fact), stratum B4 kz72/75/66 small-gap in-zone + stratum A4 kz113/111/108 deepest fresh, N_w 2656..3181 = the deepest L*-lane windows ever measured, all margins positive 3.0e-9..1.6e-8).  MAIN VERDICT DRESSED_RESERVE_DECAYS(soft: FLAT_57 curvature) on the sealed five-letter tree (TARGET_LEAK / RESTATEMENT / O1_CERTIFIED / FLAT_CENSUS / DECAYS) -- read precisely: EVERY HARD KILL CLAUSE MISSES (slope_57 = +0.018 dead flat == the r342 prior; EXT3 blind rows 12/12 inside the 0.5-decade band, n_low 0 -- incl. kz56, the Klein-gap breaker of the bare R2 band, whose dressed reserve 0.1605 is IN band: the dressing absorbs exactly the family effect that breaks the bare 2x2 uniformity; EXT4 6/6 in band; no row near the 0.01 floor -- r'_det spans 0.1383..0.5361 with both extremes MID-ladder), but the sealed FLAT clause fails on the halves-curvature bar (curv -0.426 > 0.35, a bar inherited from the r342 decay-law convention applied to a flat O(1) column with ~x2 scatter, sealed before sight and applied honestly): the O(1) candidate is NOT refuted on any family and NOT certified flat under the sealed clause -- letter of record soft decay, census content typed.  THE STRUCTURAL FINDINGS: (1) ANATOMY -- the dressing eats the bare reserve and coupling in near-exact proportion (medians Delta d1/p = 1.000, Delta c/c = -1.000 to 3 decimals; w9 0.9718/-0.9730), the dressed correlation is pinned at rho' ~ 0.846, the dressed pair margin IS the full margin (m2'/margin 1.0003..1.031 -- the dressed 2x2 is a near-exact lambda_max carrier), and the absorption is multi-mode (w9 top-1 share 0.19); (2) THE BOUND AUTOPSY (Leg C closed honestly): the theorem-grade relaxation chain R2-R4 (triangle + Cauchy-Schwarz + operator tail) certifies ZERO of 75 rows at every K -- the dressing works by the SIGNED cancellation Delta c ~ -c, so |c| + |Delta c| overshoots the cancelled |c'| by 73x (w9) and worse with depth (sign autopsy to -2.4e11 at kz130): an O(1) lower bound must control the signed cancellation, equivalently the gap ratio and top-2 geometry -- the concretized specialist question, no census certificate promoted, KERNEL_CLOSED_FORM stays FALSE; (3) TOP2_SPECTRAL_OBJECT (gated): median |r'_2/r'_det - 1| = 0.0634, K_res median 2 max 3 over all 75 rows -- r'_det is numerically a TOP-2 spectral object, its flat O(1) content IS the flat gap ratio g21 = (1-lambda_2)/(1-lambda_1) (median 8.2, slope +0.049; kz56 sits at 16.0 with the reserve unmoved) plus bounded top-2 eigenvector geometry: the R344 coordinate; (4) LAMBDA_REST_LEDGER: slope -3.276 == the r342 prior bit-near, offset (1-lambda_rest)/margin median 21.0x range 8.8..54.2, and on the six instrumented worlds lambda_rest ALONE separates dead from live (EPST 2191 / SCR 1.06e6 / SMOOTH 2.211 / HL2 2776 >= 1 vs MAIN/TWIN 0.996338; exact Schur equivalence gate 6/6; kappa_int anchors == r334/r342 records at 5 percent); (5) PEELING_STRUCTURE_FOUND: the rest block is again a shallow-edge two-atom extremal (median rest-pair mass 0.9902 on the 57, min 0.6917 at kz44; level-2 dressed reserve r''_det 0.2296..0.89, EXT3/EXT4 medians 0.60/0.66), and the w9 level-k cascade peels folds (2,4)->(6,8)->(10,12) with monotonically falling lambda_rest_k and growing reserve -- concentration persists to level 3 and breaks at level 4 (mass 3e-4): a level-2 recursion statement, not an induction; (6) RESTATEMENT does NOT fire (median bare-shadow dev 0.9997): the dressing is real content, not a lambda_max read-off.  Honest negatives: the sealed FLAT clause failed on curvature -- a curvature-aware flatness protocol for O(1) columns is R344 protocol material (defined before the next record, not retrofitted); the EXT4 rows are disclosed-seen (s3 scoping), only the EXT3 rows carry blind weight (they carried it 12/12); the R2-R4 certificate chain is measured dead.  Protocol: smoke pass 1 = 35/38 (two pre-freeze machinery findings: the Fraction ward demanded minors positivity but JF9 has lambda_rest 1.6656 -- corrected to sign agreement; the w9 d/c anchor bar sat below the r342 6-decimal print precision -- sized 2e-5), smoke pass 2 = 38/38; calibration = first full evaluation 38/38 (141.1 s) NO amendment; record run1/run2 = 38/38 byte-identical up to WALL (147.4/141.6 s).  Nothing here bounds anything beyond the measured rungs; NO L* claim, NO RH CLAIM in either direction"

_R344_STATUS = "Two-scale balance round for the terminal lane (round 344, the named r341 follow-up: the R* mass balance and the two-scale freeze -- contract PRIME.L2.FOLD_TWO_SCALE_BALANCE.01, experiments-side, NO ledger row): the stop threshold R runs over the sealed grid (3/2, 8/5, 5/3, 12/7, 7/4, 2) on the r341 exact path layer (FBR.path_bellman_state imported verbatim, every exact ward -- tilted tower / stopped partition / eps-chain envelope / Phi-Gamma / heavy hand-off -- live at ALL SIX grid points, Fractions bit-equal at the two sealed pins 3/2 and 12/7 on w9+w13), with the sealed choice FORMULA R_HAT = argmin over eligible R of max(e_H(R), e_G(R)), two-scale freezes per the r337 directive (C_H on the hand-off column (m q_max)^2 msh -- the r335 mass-arm currency; C_G on the eps-chain column W_B; both mid-ladder max-cal), the banked r321 sliding bound 1.3056 F_A^2 as the frozen THIRD arm (never recalibrated; F_A via EFP.local_ratio on the module-own q_max column, EXT3 rows via the r321 insertion rule), and the disjunctive MIN-COVERAGE test (each rung covered by >= 1 arm on its own scale) on the 51 test rows (41/41; SPEC_SHA 06375c3ade846178 final with record, freeze bf16912825178c44, two-commit protocol: pre-freeze d875647c / record dfb8d1c1; amendment a1 disclosed: two anchor-GATE reading fixes only -- the r341 narrative 'E3h med 5.86' identified as the derived display med(E3) x med(share), the r341 'kz51 7.61x' identified as the column value E3h/(log m)^2 -- no sealed surface touched).  MAIN VERDICT TWO_SCALE_PARTIAL(the min-coverage CERTIFIES at R_HAT = 7/4 at a = 1 -- 0 violations on the 51 test rows, named 4/4, midband 6/6 -- but the sealed stop rule is NOT CANONICAL: the dyadic halves pick 8/5 vs 7/4; R* remains a tuning surface in the exponent language, said honestly).  HEADLINE FINDINGS: (1) THE MASS-BALANCE CURVE IS MEASURED (four interior grid points new): hsh med [0.872, 0.603, 0.371, 0.291, 0.266, 0.000], E3h share med [0.944, 0.771, 0.491, 0.447, 0.386, 0.000], W_B med [1.489, 2.410, 3.206, 3.659, 3.796, 6.096], empty-good [23, 11, 7, 7, 7, 2]; at R = 2 the algebraic pair limit fires as derived (no pair ever heavy, 71/77 rungs lose the heavy arm, eligibility guard fired); THE ARM EXPONENTS CROSS EXACTLY ONCE -- e_H = [+0.313, +0.377, +0.358, +0.373, +0.149, deg], e_G = [-0.214, -0.075, +0.153, +0.159, +0.225, +0.464], the equilibration point sits in the gap (12/7, 7/4): the crossing is real, its LOCATION is not halves-stable on this ladder; (2) THE THREE-ARM MIN-COVERAGE CERTIFIES AT EVERY GRID POINT already at a = 1 (at R_HAT: C_H(1) = 3.9859, C_G(1) = 1.1409; at R = 2 the heavy freeze is empty and good + third carry alone); the r341 component-AND form still fails at R_HAT (viol 13/10/10) -- the complementarity (disjunctive) form is what certifies, exactly the r337 directive; THE THIRD ARM IS LOAD-BEARING: 8 of 51 test rows covered ONLY by the r321 bound, including the ENTIRE EXT3-B deep-anchor family 6/6 (kz51 F_A(ins) 5.54 ratio 0.19 = reserve 5.3x -- the r329 out-of-sample reading reproduces at the frozen banked constant under the insertion convention); (3) THE PARTITION IS NOT hsh-IDENTIFIABLE (honest negative): the sealed rule hsh >= 1/2 -> heavy predicts the minimal covering arm on only 7/51 covered test rows, 20 rows are covered only by the non-predicted arm -- the covering-arm partition is posthoc relative to the hsh coordinate, a source-side predictor remains open; (4) kz55 ANATOMY: eps-argmax at level 1 of K = 7 -- the EARLY-level class (same class as the r339 kz53 level-2 anomaly); rebalancing does NOT absorb it (W_B 2.888 -> 8.459 at R_HAT, still above the good freeze) but the THIRD arm covers it comfortably (F_A 1.63, ratio 0.14): the single r341 Form-1 violator is a sliding-bound row, not an eps-chain row; (5) THE HONEST COMPOSITION: E[X_inf^3] <= [3.9859 + 1.1409] (log m)^1 + 1.3056 x 5.54^2 (log m)^2 pointwise on the covered set => m_0* = 10^22.6 -- BEATS the r324 measured route 10^59.6 and the r341 envelope typing 10^24.0 (now WITH a certifying cover, which r341 did not have), still above the r306 census reading 10^13.5; F_Amax = 5.54 is the kz51 insertion value, the uniform constant inherits the deep-anchor spike, disclosed.  WORLDS (census): the BALANCE CURVE separates where the r341 single-point budget was world-blind -- ladder hsh med falls 0.872 -> 0.266 across the grid while SCRAMBLE stays heavy-flat (0.867 -> 0.667, E3h share 0.997 -> 0.993 at 7/4), twin w13 collapses fast (share 0.961 -> 0.042), EPSTEIN good-dominated from the start.  Anchors bit-near (r306 C_2 / r316 / r324-pre / r339 record / r324 chain / r341 record COMPLETE incl. both banked R* columns, freezes, exponents, envelope solve 10^24.0 and r306 census solve 10^13.5 / r321 F_A top-3 2.47/2.39/2.38).  Must-fails: e1 rhat-posthoc protocol-CAUGHT twice (AST rho + toy pick 4 != 0), e2 partition-posthoc protocol-CAUGHT twice, e3 cheavy-from-target AST-CAUGHT (S3), e4 hand-off without msh CAUGHT exact (break 49/32 Fractions) + m5a/m5b FLAGGED.  Protocol: smoke pass 1 = 41/41 (0.8 s, pre-commit); calibration pass 1 = 38/41 (the three FAILs were the a1 gate-reading bugs, disclosed); calibration pass 3 = 41/41 (164.8 s); record run1/run2 byte-identical up to WALL.  Nothing here bounds anything beyond the measured rungs; a certifying cover fixes a theorem candidate with explicit constants, it proves NO cofinal law; NO RH CLAIM in either direction"

_R345_STATUS = "Gap-ratio primary-coordinate round for L* (round 345, the named r343 follow-up: g21 = (1-lambda_2)/(1-lambda_1) and the top-2 eigenvector geometry at the pair promoted to primary coordinates -- contract PRIME.LSTAR.GAP_RATIO.01, experiments-side, NO ledger row): the round's exact spine is the TWO-LEVEL FORMULA r'_2 = g21 (t2-t1)^2/((g21+t1^2)(g21+t2^2)) with the pair angles t_k = w_2(i_k)/w_1(i_k) -- an exact algebraic identity for the correlation reserve of the top-2-truncated resolvent at the pair, gated per rung against the independent topk_shadow route (max dev 4.0e-15 over 75 rows, bar 1e-9) with an independent resolvent-spectrum route for g21 (mu1/mu2 of (I-E)^{-1}, devs 1.2e-12..1.6e-8, anti-circular) (35/35; SPEC_SHA 1f99235a1d870e42 final with record, freeze 7d61df830ed54cf2, two-commit protocol: pre-freeze 4a1362a0 / record 4e5e1270; NO amendments after freeze; ladder = 42 core + 15 r286 extension + 12 r329 EXT3 + the 6 r343 EXT4 windows adopted as-is, N_w to 3181).  MAIN VERDICT GAP_RATIO_PRIMARY_CERTIFIED on the sealed seven-letter tree (TARGET_LEAK / RESTATEMENT / TOP2_BREAKS_AT_LOW_CONCENTRATION / CERTIFIED / CANCELLATION_LAW_FOUND / FLAT_CENSUS / NOT_FLAT) -- the first certificate-grade letter on the O(1) coordinate of the L* lane: the CURVATURE-HONEST FLATNESS PROTOCOL (sealed a priori, the explicit r343 mandate: CH1 band |log10(x/med57)| <= 0.5 on ALL 75 rows, CH2 Theil-Sen slope <= 0.15 AND the separation-restricted pairwise-slope quantile CI [q05,q95] containing 0, CH3 no monotone cohort drift > 0.3 dec) passes ALL clauses on BOTH candidates (r'_det: 0 band outliers, slope_75 +0.028, CI [-0.739,+0.825]; g21: 0 band outliers, max |dev| 0.380 dec, slope_75 +0.031, CI [-0.971,+0.985]; cohort medians non-monotone both) WHILE THE OLD r343 CLAUSE FAILS BOTH CANDIDATES on its halves-curvature bar, reproduced bit-near (rdetp +0.018/curv -0.426, g21 +0.049/curv +0.601; EXT3 12/12 and EXT4 6/6 in band under BOTH protocols): the r343 soft-decay letter is re-adjudicated as a PROTOCOL artifact, both protocols printed side by side -- the halves-curvature bar reads the ~x2 scatter of a flat O(1) column as decay, the scatter-honest CI reads it as flat; median top-2 dev 0.0634 <= 0.15; the sealed KILL on the concentration-weak census (union of the two 6-row deciles of rest-pair mass and pair mass = 11 rows incl. the named kz44 argmin 0.6917 and kz59 argmin 0.9352) does NOT fire (median two-level dev 0.1432 <= 0.30 -- the weak rungs double the ladder median, single worst kz28 0.4192, honest; K_res > 3 on 0/11; g21 band violations 0/11) and is KILL_ABSORBED_BY_K3 (median top-3 dev 0.0163: the K <= 3 shadow is ~9x tighter exactly where K = 2 weakens).  + CANCELLATION_LAW_FOUND(delta 2.668) as ADDITIVE TAG -- the r343 bound-autopsy question answered as a measured structure statement: the mirror residual c'/c = |1 + Delta c/c| decays as N_w^-2.67 on the 57 (halves curv -0.189 <= 0.35, EXT3 10/12 in band with n_low 0 (both misses HIGH side), EXT4 6/6; bookkeeping slope(c') - slope(c) = -2.703 vs -2.668) -- 'the rest space mirrors the pair cross-term up to O(N_w^-2.7)'; the path/mode anatomy: the DIRECT overlap u1.u2 carries the mirror's bulk (rho_0 median 0.839, w9 0.579) while the mode profile is multi-mode (M90 median 30, top-1 share 0.275) -- order-0-dominated in PATHS, multi-mode in MODES; WORLD COLUMN: the finite-order mirror rho_32 = 0.9225 on both live worlds but DIVERGES on all four dead worlds (SMOOTH +7.9e6 to SCR -6.5e195, lambda_rest >= 1 explodes the path series) -- the mirroring exists only where lambda_rest < 1, a census.  STRUCTURAL FINDINGS: (1) the top-2 pair geometry is ladder-stable (angle medians t1 -0.4744 / t2 +1.1162; g21 spans 3.43..19.71); (2) the SECOND eigenvector lives dominantly on the pair too (w2 pair mass median 0.552; w9: pair 0.604 vs peel-pair 0.385) and lambda_2 is NOT the rest-block top anywhere ((1-lambda_2)/(1-lambda_rest) median 0.42) -- the lambda_2 carrier is the pair's second angle first; the peel-fold weight dictionary predicts to 7e-3 (weight side closed-form, kernel side census-grade, r342 negative #4 stands); (3) RESTATEMENT does not fire (median fixed-angle inversion dev 0.1009 > 0.05): g21 is NOT r'_det plus a constant angle -- the angle column carries real window-dependence; (4) the world g21 census refutes the s1 sign conjecture honestly (dead worlds have lambda_2 > 1 too): the separation is g21 < 1 on dead 4/4 vs > 7.5 on live 2/2, magnitude census; lambda_rest separation and kappa_int anchors re-gated.  Honest negatives: the certificate is a sealed census on 75 finite windows, never an asymptotic theorem, and r343's letter was correct under its own seal (the re-adjudication changes the protocol, not the data); the K = 2 truncation IS strained at weak concentration; delta 2.67 sits below the margin exponent 3.33 (real gap or c'-column curvature -- typed R346 question via c'^2 = (1-r'_det) p'q' with m2' == margin).  Deterministic run1/run2 byte-identical up to WALL (62.0/61.6 s).  Nothing here bounds anything beyond the measured rungs; NO L* claim, NO RH CLAIM in either direction"

_R346_STATUS = "Cover-canonization round for the terminal lane (round 346, the named r344 follow-up: the three residues of the r344 cover -- canonical stop criterion, source-side partition predictor, F_Amax defusal -- contract PRIME.L2.COVER_CANONIZATION.01, experiments-side, NO ledger row): the ENTIRE r344 scaffold re-executed through the same code path and anchor-gated against the r344 record (balance curve at all six grid points, R_HAT = 7/4 with halves (8/5, 7/4), freezes C_H/C_G 3.9859/1.1409 at a = 1, min-coverage 0/51 at EVERY grid point, third-arm-only 8 with EXT3-B 6/6, partition 7/51 + nonpred 20, F_Amax 5.54, kz55 eps-argmax level 1, composed m_0* 10^22.6 -- ALL reproduced bit-near), then three sealed canonization legs (45/45; SPEC_SHA 95559d5de07b304e final with record, freeze 306dba57867f2170, two-commit protocol: pre-freeze 9fcc081b / record bfe70fcf; NO amendment -- calibration pass 1 = first full evaluation = 45/45).  MAIN VERDICT COVER_CANONIZED + PREDICTOR_FOUND(P02) on the sealed four-letter tree (TARGET_LEAK / CANON_STATE_NOT_EXACT / COVER_CANONIZED / COVER_CENSUS_ONLY, flags THRESHOLD_NOT_CANONICAL / PREDICTOR_FOUND / FAMAX_DEFUSED).  HEADLINE FINDINGS: (1) LEG A -- the stop rule canonizes via the INTRINSIC PAIR-CEILING FORMULA, not via the exponent crossing: K1 (R_ALG = GAMMA_CEIL^(1/3) = 4^(1/3) = 1.5874 -> grid 8/5, index 1, interior, DATA-FREE -- the same derived algebra that makes R = 2 the pair limit) CERTIFIES at a = 1, landing exactly on the grid point one r344 dyadic half picked; K4 (the R-FREE ENVELOPE: HB min over grid indices 0..4 positive-guarded, W_B min over all six, mid-ladder max-cal) ALSO certifies at a = 1 with C_H_ENV 3.9859 + C_G_ENV 0.4867 -- the good envelope drops to the W_B(3/2) freeze and the threshold disappears by construction; K2 (first-equilibrated) and K3 (pooled interpolated crossing, R_CROSS 1.7407) both pick 7/4 and are formally halves-stable BUT ONLY VIA THE NO-CROSSING FALLBACK -- neither dyadic half shows a sign change at all (halves e_G collapse to -0.3..-1.4): the crossing LOCATION stays halves-invisible on this ladder, the exponent language stays soft, said honestly (THRESHOLD_NOT_CANONICAL stays silent by the sealed letter, the fallback anatomy disclosed).  (2) LEG B -- residue 2 CLOSED at the sealed bars: the sealed rule P02 (F_A >= 1.5 -> THIRD ARM, else HEAVY; one source-pure feature, the r329 SPIKE_FA record threshold) predicts a COVERING arm on 51/51 test rows -- core 39/39, OUT-OF-SAMPLE EXT3 12/12, non-degenerate (sealed 12-rule threshold family, max 2 features, all thresholds a-priori; selection = max core accuracy; bars core >= 0.80 / OOS >= 0.75); the exact-priority-label census gives 46/51 vs the r344 hsh baseline 7/51 -- the cover's working partition is spike-vs-rest in the F_A coordinate, not heavy-vs-good in the hsh coordinate; runner-ups P04 (F_A >= 2.0) 50/51, P07 (depth > 1650) 48/51, P05 (grel < 0.85) 47/51.  (3) LEG C -- residue 3 stays OPEN (honest negative): the six sharp spike rows kz53/kz67/kz51/kz54/kz42/kz62 are covered ONLY by the third arm at EVERY a in (1, 2, 3) -- the uniform rescue fails for V1 (class split at 1.5) and V2 (P90 = 1.917), FAMAX_DEFUSED stays silent, the uniform composition keeps F_Amax = 5.54 and m_0* = 10^22.6 UNCHANGED; the CLASS-CONDITIONAL reading (disclosed two-statement census): the QUIET-class statement with cap 1.39 solves to m_0* = 10^16.1 (V2 cap 1.91: 10^17.5) with the 13-row spike family as NAMED pointwise-certified exceptions -- 2/3 of the log-distance toward the r306 census 10^13.5, NOT a uniform bound; V3 floor census (max(F_A, 0.58)): only kz33/kz128 sit below the floor (non-test), nothing added or lost -- the open r329 below-range validity question stays open.  (4) LEG D -- the honest composition table: r344 baseline 10^22.6; K1 headline (8/5, a = 1, C_H 6.8806 + C_G 1.0151 + third term) m_0* 10^22.6 -- the third-arm term dominates the solve, the stop-point choice is nearly free in m_0*; vs r324 10^59.6 / r341 envelope 10^24.0 / r306 census 10^13.5; cofinal typing: census = all freeze constants + coverage counts + accuracies; law candidates = the K1 ceiling formula (derived algebra, certifies), the banked r321 sliding form (again out-of-sample-clean), the P02 predictor (OOS-confirmed); missing = any bound beyond the measured rungs + a spike-free uniform constant.  (5) WORLDS (census): w9 F_A(ins) 0.83 -> P02 H, QUIET; twin w13 1.09 -> H, QUIET; EPSTEIN 1.00 -> H, QUIET; SCRAMBLE 2.00 -> P02 T, class SPIKE -- the scrambled world is the only control the class rule flags as spike-family.  Anchors bit-near (r306 C_2 / r316 / r324-pre / r339 / r324 chain / r341 record COMPLETE / r321 F_A top-3 / THE r344 RECORD COMPLETE); Fractions bit-equality at the two sealed pins 3/2 + 12/7 on w9 + w13 EXACT; must-fails e1 pred-from-coverage protocol-CAUGHT twice (AST rho + toy ('T', 'G')), e2 clsrule-posthoc protocol-CAUGHT twice, e3 envelope double-count CAUGHT exact (break 147/32 Fractions), e4 crossing-posthoc protocol-CAUGHT twice + m5a/m5b FLAGGED.  Protocol: smoke 45/45 (1.1 s, pre-commit); calibration pass 1 = 45/45 (177.8 s, NO amendment); record run1/run2 byte-identical up to WALL (171.9/169.9 s).  Nothing here bounds anything beyond the measured rungs; a certifying cover fixes a theorem candidate with explicit constants, it proves NO cofinal law; NO RH CLAIM in either direction"

_R347_STATUS = "Delta-alpha closure round for L* (round 347, the named r345 follow-up: the one-line identity -- does the margin exponent follow from the cancellation law? -- contract PRIME.LSTAR.DELTA_ALPHA_CLOSURE.01, experiments-side, NO ledger row): the round's exact spine is the ONE-LINE IDENTITY m2'(p'+q'-m2') = p'q' - c'^2 = p'q' r'_det (both eigenvalue deficits of the dressed 2x2 are the roots of t^2 - (p'+q')t + (p'q'-c'^2); exact Fractions on the hand toy, f64 max residual 3.3e-9 on 75/75 rows at the backward-error scale, definitional ward c'^2 == (1-r'_det)p'q' at 1.8e-16) (34/34; SPEC_SHA bd1aa7f393da057f final with record, freeze 99100cea2358fe56, two-commit protocol: pre-freeze 95f7f944 / record 8e489331; NO amendments after freeze; one pre-freeze machinery finding disclosed: an arithmetic slip in the w9 aspect anchor constant, corrected before the freeze commit).  MAIN VERDICT ALPHA_CLOSED on the sealed four-letter tree (TARGET_LEAK / ACCOUNTING_GAP / ALPHA_CLOSED / ALPHA_CLOSED_CENSUS) -- THE MARGIN EXPONENT FOLLOWS FROM THE CANCELLATION LAW: all four sealed closures hit inside the 0.1 bar (C1 identity route |alpha 3.332 - alpha_id 3.382| = 0.050; C2 margin bridge 0.001; C3 cancellation bookkeeping |slope(c') -3.401 - (-0.697 - 2.668)| = 0.035; C4 THE ONE LINE |alpha 3.332 - (a_c 0.697 + delta 2.668)| = 0.033), the bridge clause m2' == margin holds protocol-graded on all 75 rows (max |m2'/margin - 1| = 0.0605 <= 0.10, ratio slope +0.0001), CURV_FLAT(r'_det) re-gates under the r345 protocol verbatim (0 band outliers of 75), both AUX aspect bands hold 0 out (p'/q' max 0.231 dec, (p'+q')/c' max 0.101 dec -- the flat-aspect step that turns the identity into the one line), and the delta-law (delta 2.668, curv -0.189, EXT3 10/12 high-side, EXT4 6/6) + c-law (curv +0.308, EXT3 11/12) re-gate.  BUILDING BLOCKS TYPED: identity THEOREM-GRADE; bridge + flatness certificates CERTIFIED CENSUS (sealed protocols, 0 violations); a_c and delta FIT-CENSUS laws with sealed honesty meters (weight side closed-form: digamma 2.4e-3, v_pred 9.0e-4 on the six sample rungs) -- the open analytic remainder of the L* margin law is REDUCED from rho_r = 2.624 (r342) to the single cancellation exponent delta.  + DRESSED_FACTOR_CENSUS (Leg C, honest): the dressed-dictionary GO clause does NOT fire (p'/p, q'/q fail the flat protocol loudly -- the dressed diagonals do NOT inherit the bare dictionary slopes unchanged) and the residual-law tag does not fire either (q'/q halves-curved -0.508 > 0.35): the factor laws are typed census, p'/p ~ N^-2.609 and q'/q ~ N^-2.665 with the universality census |delta_p - delta| = 0.059, |delta_q - delta| = 0.003 -- the dressing eats p, q, c near a COMMON rate, census-grade.  + MIRROR_WORLD_CLAUSE_SEALED (Leg D): mirror exists iff lambda_rest < 1, live iff |rho_32 - 1| <= 0.5 -- live 2/2 (MAIN/TWIN rho_32 0.9225), dead 4/4 diverge (SMOOTH +7.9e6 .. SCR -6.5e198), and the r330 DIRICHLET second worlds enter the L* lane for the first time, TYPED DEAD-SIDE (DIR lambda_rest 3.97e37 series NONFINITE; ABS 2.28e5 series -3.85e176): the r330 half-filling split restates structurally in the E-Gram frame -- the chi-twist and even the bare p=3 atom removal destroy the rest-block contraction; typed, not forced.  Sealed 57-fits (slope | curv): p' -3.422 | +0.022, q' -3.359 | -0.241, c' -3.401 | -0.140, m2' -3.334 | -0.368, s' -3.381 | -0.124; dressed-decay EXT3/EXT4 misses ALL high side (n_low 0 everywhere -- the deep family decays slower than the 57-fit, the r286 curvature restated as census).  Honest negatives: delta is NOT derived from the source (one measured exponent instead of three, the typed specialist question); the closure holds ON the 57-fit family (deep extension carries the known curvature); alpha_id - alpha = 0.050 is Theil-Sen non-additivity across curved columns (the identity itself holds per row at 3.3e-9); no second living arithmetic exists inside the MAIN frame (GRH-faithful Dirichlet frame = named follow-up).  Anchors bit-near (w9 records / r343 dressed row / r345 c'/c + g21 + rho_32 / r343 medians / kz56 + span / all seven fit priors + four curvature priors).  Must-fails: m1 wrong normalization CAUGHT exact (1.7e-1 at w9), m2/m3/m4/m5 AST-FLAGGED (posthoc closure bar, circular alpha, lambda readback, posthoc mirror bar).  Deterministic run1/run2 byte-identical up to WALL (49.9/50.2 s).  Nothing here bounds anything beyond the measured rungs; NO L* claim, NO RH CLAIM in either direction"

_R348_STATUS = "Delta source-anatomy round for L* (round 348, the named r347 follow-up: the order-0 mirror as an object + the resolvent rate-equality theorem candidate delta_p == delta_q == delta -- contract PRIME.LSTAR.DELTA_SOURCE_ANATOMY.01, experiments-side, NO ledger row): two exact spines -- (i) the ORDER-0 SPLIT Delta c = u1.u2 + sum_m alpha_m beta_m delta_m/(1-delta_m) (direct path + resolvent enhancement; Fractions exact on the hand toy, f64 max 5.8e-14 on 75/75, bookkeeping c'/c == (1-rho_0) - rho_hi at 3.6e-8) and (ii) the TWO-LEVEL DRESSED-SCALAR IDENTITY p'_2 = m(g21 a2^2+b2^2)/Dt^2, q'_2 = m(g21 a1^2+b1^2)/Dt^2, c'_2 = m(g21 a1 a2+b1 b2)/Dt^2 (Fractions exact on the rank-2 model: 121/250, 79/250, 72/250; cross-tie r'_2 = 4375/9559 == the r345 formula) (34/34; SPEC_SHA 307814e9ef67e8a1 final with record, freeze b43a635184c44d3c, two-commit protocol: pre-freeze 0d0849e6 / record 665ea4f6; NO amendment -- calibration pass 1 = first full evaluation = 34/34).  MAIN VERDICT RATE_EQUALITY_THEOREM on the sealed five-letter tree (TARGET_LEAK / DELTA_SOURCE_DERIVED / RATE_EQUALITY_THEOREM / ORDER0_LAW_FOUND / DELTA_IRREDUCIBLE) -- THE COMMON DRESSING RATE IS THE MARGIN RATE: under top-2 dominance with flat geometry every dressed scalar is margin x an O(1) geometry factor, hence delta_x = alpha - a_x exactly (rate toys: the naive equality holds IFF a_p == a_q == a_c and breaks by exactly the bare spread; a tau = 0.4 angle drift separates the dressed slopes by 0.453 -- flat geometry is load-bearing); LIVE certified census: E1 CURV_FLAT (r345 protocol verbatim) passes on ALL THREE margin-pinning ratios p'/m, q'/m, |c'|/m (slopes -0.056/+0.016/-0.025, 0 out/0 hard of 75 each), E2 two-level truncation median 0.0879 <= 0.20, E3 sign 75/75, E4 theorem image max |delta_x - (alpha - a_x)| = 0.033 <= 0.1 -- the r347 universality census (0.059/0.003) is upgraded to its exact form: the delta_x differ by exactly the bare-rate spread (0.056/0.053), and delta == alpha - a_c LOSES ITS INDEPENDENT-LAW STATUS; the irreducible measured rest of the L* margin law is the pair {alpha, a_c}.  + ORDER0_LAW(delta_0 0.401, curv +0.094, EXT3 12/12, EXT4 6/6) with CARRIES_DELTA REFUTED (|0.401 - 2.668| = 2.267 > 0.5): the r347-sketch hypothesis dies cleanly -- u1.u2/c does NOT carry the N^-2.67 law; the delta law is an INTER-ORDER NEAR-CANCELLATION (y0 = 1 - rho_0 slope -0.401 and rho_hi -0.393 are twin slow laws whose difference is the c'/c column, pinned to the margin scale by the resolvent; depth census |c'/c|/y0 median 1.48e-3).  + DICT_T0_GO(median 0.0177 <= 0.10 over the six sample rungs; w9 honest worst 0.195): the WEIGHT side of the order-0 overlap products is dictionary-explicit (r342 digamma/tent v_pred inside measured kernel rows); kernel side census-grade (r342 negative #4 never upgraded).  + WEAK_FAMILY_STRAINED (honest: kz28 scalar shadows up to 0.91, median 0.377 > 0.35 on kz28/kz44/kz59; worst arbitrated row kz23 at 4.06 -- K = 2 is a median instrument on the scalars, not per-row).  + MIRROR_WORLD_CLAUSE_SEALED (r347 reproduced bit-near: live 2/2 rho_32 0.9225, dead 4/4 diverge, DIR/ABS typed dead-side) with the NEW rho_0 world column: live 0.5787 vs dead EPST -220 / SCR -1.06e6 / SMOOTH +1.76 / HL2 -3.05e3 -- the order-0 quota separates by size-or-sign on 5 of 6 std worlds (SMOOTH same sign wrong size; census, no bar).  Mode census medians: top-1 0.2746, M90 30, T0 arch-rim ATOM share 0.8158, top-mode peel-pair mass 0.0142 -- the mirror carriers are delocalized modes, arch-rim in atom terms.  Anchors bit-near (w9 records / r347 closure row / r345 mirror anchors / all ten fit priors + three curvature priors / cohort medians rho_0 0.8392, M90 30, top-1 0.2746, bridge 1.0058).  Must-fails: m1 wrong resolvent weight CAUGHT exact (3.2e-1 at w9), m5 wrong coupling sign CAUGHT exact (1.7e-1 at w9, 1/3 on the toy), m2/m3/m4 AST-FLAGGED (posthoc mode quantile, delta_0 readback, planted-target toy).  Deterministic run1/run2 byte-identical up to WALL (63.6/63.5 s).  Nothing here bounds anything beyond the measured rungs; alpha and a_c stay underived from the source; NO L* claim, NO RH CLAIM in either direction"

_R349_STATUS = 'Third-arm spike-law round for the terminal cover (round 349, the named r346 residue: the r321 sliding coverage of the F_A >= 1.5 spike family as a law -- contract PRIME.L2.THIRDARM_LAW.01, experiments-side, NO ledger row): the ENTIRE r344/r346 scaffold re-executed anchor-gated bit-near (cover 0/51 at every grid point at a=1, C_H/C_G 3.9859/1.1409, P02 39/39 + EXT3 12/12, K1 idx 1 cert 6.8806+1.0151, K4 3.9859+0.4867, V1 13 spikes cap 1.39 m0 10^16.1, V2 1.917 10^17.5, six-spike set {42,51,53,54,62,67} + ratios 0.19/0.16/0.29/0.31) (44/44; SPEC_SHA 9b593e63762ee698 final with record, freeze 0016e2f1596978da, two-commit protocol: pre-freeze b2ef45ea / record 609346e6; one DISCLOSED print-level amendment a1 between calibration passes -- the sealed every-hole-NAMED requirement extended to the EXT4 misses, no bar/band/rule moved; a pre-run placeholder removal disclosed, r321 protocol-error class).  THE EXACT SPINE (warded <= 9.3e-16 on 87 live worlds): the sliding reserve FACTORIZES EXACTLY, RSV = GSQ F_A^2/rho_2 = (GSQ/B^2) x (pk/M2q) x (pk M2q/sum q^3), and via the r324 identity pk = F_A B log m/m the dominance form reads rho_2 = D pk (F_A B)^2 with D = sum q^3/pk^3; r306 NORM identity independently recomputed from the genealogy column (8.4e-16), r324 identity F_A medloc == pk (1.6e-16), Fractions pins EXACT.  MAIN VERDICT EXCEPTIONS_REMAIN + RESERVE_FLAT(-0.33) + EXCEPTIONS_DISSOLVED(13/13) + HOLES([111, 75]) on the sealed six-letter tree -- THE HONEST SPLIT: (1) the RAW class law rho_2 <= 1.3056 F_A^2 on F_A >= 1.5 holds with ZERO hard violations on all 23 family rows across 65 ladder + 12 EXT3 + 6 fresh EXT4 anchors (the r343/r345 L*-lane list kz72/75/66/113/111/108, FIRST entry into the cubic lane, all POSITIVE_PREFIX-admitted; ALL SIX are spike-class under the insertion coordinate F_ins 1.58..6.68 -- the deep fresh pool is spike-dominated), including the new out-of-sample record F_ins 6.68 (kz111, covered at reserve 1.11); the 13 r346 class-conditional exceptions DISSOLVE 13/13 (reserves 3.2..12.1) and the hand-off is SEAMLESS (every test row below 1.5 heavy/good-covered at (R_HAT, a=1), 0 holes; boundary band [1.125, 2.0] census 22 rows); (2) the SEALED reserve floor RHO_BAR = 1.5 is UNDERCUT out-of-sample by exactly the two deepest fresh EXT4 spikes kz111/kz75 (reserves 1.11/1.07) -> CERT False -- the honest family floor is ~1.1, and the family F_A ceiling GROWS out-of-sample (5.54 -> 6.68): the r346 census ceiling is not stable; (3) THE RESERVE ANATOMY: the reserve is the CONCENTRATION DEPTH 1/(D pk) (family median log10 shares S_const/S_M2/S_dom = +0.01/+0.64/+0.26; NOT the calibration slack -- B^2 > GSQ on 7/17 family rows, the r321 pure-algebra caveat restated -- and NO log factors appear in the exact factorization), and it is FLAT-to-eroding in F_A (rc_fam -0.331, envelope bins argmin 2, neither sealed monotonicity bar fires): upward safety comes only from the measured D pk B^2 ceiling (max 0.409 <= GSQ/1.5 = 0.870 on the 77 sealed rows, ~1.2 on the EXT4 misses); (4) the DOMINANCE structure is real but misses the sealed contrast bar: family med D 1.79 (bar 2.5 met), max 2.13 (bar 6.0 met), the six sharp spikes D 1.07..2.06 near-single-atom cubes, quiet med 5.03 -> contrast 2.8x < 3.0 -> DOM_OK False, THIRDARM_LAW_DERIVED stays unfired; the mechanism reading (r324 identity + near-dominance + measured concentration ceiling) stands as census; (5) worlds: SCRAMBLE is spike-class and COVERED (F_ins 2.00, D 1.72, rsv 2.9) -- the class statement is ARITHMETIC-FREE by measurement, a pure concentration-size statement, no world separation claimed (the r321 class-side rejection carries that load).  m_0* table: uniform 10^22.6 UNCHANGED (family F_A ceiling stays census), two-statement composite 10^22.6 (spike side binding), V1 10^16.1 / V2 10^17.5 reprinted; the honest yield is the TYPE census of the 10^16.1 reading (13/13 exceptions dissolve on the sealed cover cohort) MINUS the new EXT4 reserve erosion.  Must-fails: e1 reserve-bar-posthoc + e2 f0-posthoc protocol-CAUGHT twice each (AST rho + toys 0.5/2.0 vs sealed 1.5/1.5), e3 dominance-circular CAUGHT twice (AST qm + Fractions pin 7/2 vs 28/27), e4 wrong-log-power CAUGHT exact (break == 2), m5a/m5b FLAGGED.  Deterministic run1/run2 byte-identical up to WALL (cal 329.5/334.4 s).  Nothing here bounds anything beyond the measured rungs; the named rests are a stable reserve floor at the honest ~1.1 scale and the family growth law m q_max <= C log m; NO RH CLAIM in either direction'

_R350_STATUS = "Alpha source-anatomy round for L* (round 350, the named r348 follow-up: the kernel side of the margin legislation as an object -- can the pair {alpha, a_c} be closed source-side? -- contract PRIME.LSTAR.ALPHA_SOURCE_ANATOMY.01, experiments-side, NO ledger row): three exact spines -- (i) THE KERNEL COLUMNS K11 = d1/v1, K22 = d2/v2, K12 = c/sqrt(v1 v2), kappa = K12/sqrt(K11 K22) with the INDEPENDENT Christoffel-Darboux ward: K_N at the pair atoms recomputed from the mu-chain recursion coefficients via the CD endpoint/confluent formulas, == the Gram route at max 1.2e-10 on the six-rung sample (K_N is SOURCE-COMPUTABLE; the open question is its LAW, not its value); (ii) THE PINNING IDENTITIES exact in Fractions on TWO rank-2 models (m2'_2 == margin IDENTICALLY -- the bridge is 1 in the top-2 truncation; p'q' - c'^2 == margin^2 g21/Dt^2, model dets 7/100 and 3/25; c' == margin x G) -- the r348 twin near-cancellation is ALGEBRAIC SELF-CONSISTENCY of the resolvent equation, with the pinned corollary slope(y0 - rho_hi) == -(alpha - a_c) (residual 0.033); (iii) THE SLOPE BOOKKEEPING (BK2 Christoffel saturation |s_K11 + s_v1 - s_d1| = 0.018/0.016: the diagonal kernel growths ARE the reciprocal weight laws; BK3 backward-CS 0.0016: a_c == (a_p + a_q)/2 to 0.002) (33/33; SPEC_SHA c3998c87777c975c final with record, freeze f7d622d8e975b265, two-commit protocol: pre-freeze e3f53e1a / record 24f8ca0d; TWO DISCLOSED calibration amendments a1/a2 of the r342-a1 class -- the BK1 and route-A after-fit slope sums measured 0.137/0.170 of pure Theil-Sen non-additivity on the strongly curved weight columns (v1 fitted -1.791 vs two-point -1.18; the pointwise identities hold at 1e-16), re-measured at the pointwise dictionary-reconstruction scale (max 5.5e-4, bar 1e-2) and compose-then-fit (exact on exact powers); the after-fit sums stay printed as CENSUS, no adjudication bar/band/candidate/verdict rule moved).  MAIN VERDICT ALPHA_SOURCE_CLOSED AT CANDIDATE-LAW GRADE on the sealed four-letter tree (TARGET_LEAK / ALPHA_SOURCE_CLOSED / KERNEL_LAW_FOUND / KERNEL_IRREDUCIBLE) -- the exponent chain of the L* margin closes source-side with ONE census member: alpha == 3/4[cand a_p] + 2/3[cand a_q] + rho_r 2.624[census] - a_(p+q) 0.690 = 3.352 vs alpha_meas 3.332 (dev 0.019 <= 0.1); route A independently: alpha_bal = -slope(sqrt(vpred1 vpred2)[DICT] x |K12|[KERNEL] x c'/c[PINNING]) = 3.401 (dev 0.068 <= 0.1); BLOCKS TYPED: weights WOERTERBUCH (the r342 digamma/tent dictionary carries the across-ladder weight LAWS: |s_v - s_vpred| = 0.0000/0.0000 at slopes -1.791/-1.683), deficits CANDIDATE-LAW (a_p 0.7539 hits [3/4, 2x0.38] clauses CLEAN curv +0.305 EXT3 11/12 EXT4 5/6 low 0; a_q 0.6446 hits [2/3, 1-0.38] CLEAN; a_kappa 0.7111 hits [2/3, 3/4] CLEAN -- every ambiguity printed: the 57-window ladder cannot separate the candidate families, a hit is NOT an identification), pinning THEOREM-grade (Fractions exact + certified census: bridge max 0.0605 <= 0.10, det-shadow median 0.0731 <= 0.35 (max 0.80, weak rungs, r348 caveat), CURV_FLAT 3/3 on p'/m, q'/m, |c'|/m), rho_r CENSUS (halves-curved -0.767 since r342 -- the r338 q1 backward-CS question in its sharpest form, THE single non-dictionary non-theorem non-candidate block).  + PINNING_THEOREM + DELTA0_CANDIDATE(delta_0 0.401 re-gates bit-near; hits [0.38, 2/5] -- both sealed candidates hit and are mutually unresolvable at this depth; twin ward 0.0087).  THE KERNEL STECKBRIEF (this round's new numbers, 57-fit): s_v1 -1.791 / s_v2 -1.683 (dictionary-grade), g_K11 +1.786 / g_K22 +1.683 (== reciprocal weights via BK2), g_K12 +0.902 THE ONE DIRTY CENSUS COLUMN (no candidate hits, curv +0.500, EXT3 5/12 -- the honest kernel rest: the CROSS-kernel growth at discrete arch-rim atoms resists where the diagonal growths reduce to the dictionary), a_kappa 0.711; REL1 (perfect correlation) fails by 0.832 as expected, REL2 (sqrt decorrelation, g_K12 == (g_K11+g_K22)/4) hits at 0.035 but stays census (dirty clauses).  BY-CATCH: the y0 world column separates live from dead BY SIZE OR SIGN on 6/6 std worlds (live +0.4213 vs EPST +221 / SCR +1.06e6 / SMOOTH -0.758 / HL2 +3.05e3; the r348 rho_0 column separated only 5/6 -- SMOOTH flips sign in the y0 coordinate); TWIN-PAIR TYPING: on every dead world lambda_rest >= 1, the rho_hi series diverges -- the r348 twin slow laws are a live-world structure.  Anchors bit-near (w9 records / r347 closure row / r348 order-0 row + pinning ratios / all seven fit priors + five curvature priors / cohort medians rho_0 0.8392, bridge 1.0058 / this round's s1 kernel-column scoping anchors).  Must-fails: m1 CD without b_{N-1} CAUGHT exact (1.2e0 at w9, 4.0e0 toy), m4 double-counted weight share CAUGHT exact (break == |s_v1+s_v2|/2 = 1.100), m2/m3/m5 AST-FLAGGED (ALPHA_REC readback, posthoc candidate, planted-target family).  Deterministic run1/run2 byte-identical up to WALL (62.0/61.8 s).  Honest negatives: ALPHA_SOURCE_CLOSED is candidate-law grade, never an asymptotic derivation (3/4 vs 2x0.38 at distance 0.01 inside the 0.05 bar -- unresolved); g_K12 and rho_r are the named rests; nothing here bounds anything beyond the measured rungs; NO L* claim, NO RH CLAIM in either direction"

_R351_STATUS = 'Family growth-law round for the terminal cover (round 351, the named r349 successor: m q_max <= C log m as a law, equivalently F_A B <= C via the EXACT r324 identity -- the CONVENTION-FREE law coordinate FAB = m q_max/log m -- plus the stable reserve floor at the honest ~1.1 scale; contract PRIME.L2.QMAX_GROWTH_LAW.01, experiments-side, NO ledger row): the r349 census/controls/EXT3/EXT4 scaffold re-executed anchor-gated bit-near (r349 family record EXACT: 17 rows, RSV 3.19/7.03/12.06, rc_fam -0.331, D 1.79/2.13/5.03, D pk B^2 0.409, shares +0.01/+0.64/+0.26; EXT4 record EXACT: six SPIKE, F_ins (1.58, 2.03, 3.11, 4.22, 5.53, 6.68), holes kz111/kz75 rsv 1.11/1.07; r324 direct record through the FAB column: C_INF 1.7481 with violator set {53, 61, 67, 76, 83} EXACT and e_G +0.158; r329 counting record C_NSC 2.0258 0/39 + C_NG 2.6351 0/39) plus a FRESH EXT5 TRANCHE by the r343 selection rule verbatim on the extended used ledger (used 98, domain-capped fresh 17, stratum B5 kz79/81/65 in-zone small-gap + A5 kz103/135/106 deepest, N_w 1771..2812, POSITIVE_PREFIX 6/6, no queue failures; the IN-ZONE FRESH POOL IS EXHAUSTED after this tranche -- documented) (43/43; SPEC_SHA 67102e4cb2aa17e6 final with record, freeze d556c758701c3a60, two-commit protocol: pre-freeze 8131ab53 / record 080d3711; NO amendment after freeze; scoping pass disclosed: selection enumeration + two wpack timings only, no bound value computed).  MAIN VERDICT GROWTH_LAW_CERTIFIED + FLOOR_ERODES(10^3.7) + INZONE_POOL_EXHAUSTED + EXT5_CLEAN(6) on the sealed six-letter tree: (1) THE GROWTH LAW HOLDS AT A FROZEN CEILING -- C_FAB = max FAB over the 83 sealed rows = 14.93 at kz111 (EXT4; the record-derived expectation ~7.44 from kz51 was LOW by 2x: the EXT4 FAB column had never been computed); the fresh test: ZERO violations on all six EXT5 rows (FAB 2.04..9.71, max kz135 35 pct below the ceiling), rc_small = Spearman(m, FAB | small-gap family) = +0.243 < +0.5 -- no growth clause fires: m q_max <= 14.93 log m holds on every measured row of every cohort (89 rows) and on all four instrumented worlds (SCRAMBLE FAB 2.09 -- the law is ARITHMETIC-FREE by measurement), the FIRST uniform growth statement of the lane that survives a fresh tranche; (2) the F_A census ceiling ticks up AGAIN (kz79 F_ins 6.69 > the r349 record 6.68; uniform solve at the new ceiling 10^23.5) while the FAB ceiling STANDS -- the convention-free law coordinate is measurably more stable out-of-sample than the rank-local F_A coordinate; (3) the SOURCE DERIVATION stays open, typed honestly: K3 pileup cap BREAKS on fresh (kz65 pil 184.64 > frozen 177.97) and is vacuous, K4 group cap holds 0/6 but vacuous (implied ceilings 360/470 >> 4 x max FAB), K2 Klein-gap formula FAB grel <= 11.87 holds 0/6 with Spearman(grel, FAB | family) = -0.623 (the gap geometry genuinely sets the q_max scale, census -- grel has no measured lower bound) -> src_ok False, GROWTH_LAW_DERIVED unfired; the FRESH COUNT TEST (first EXT4/EXT5 measurement): nsc_rel/log m <= 2.0258 AND ngj/log m <= 2.6351 hold 12/12 (min reserves 1.59/2.77) -- the O(log m) counting side choice-robust on a THIRD consecutive fresh cohort; (4) THE FLOOR HOLDS AT 1.05 BUT ERODES: cert2 True on all 28 family rows (min RSV 1.07 at kz75; the five EXT5 family rows come in at RSV 2.22..3.38, NO new floor hole) BUT e_RSV = -0.649 (halves-slope vs m) and rc_fam351 = -0.600 (vs the r349 ladder+EXT3 prior -0.331): the census extrapolation crosses RSV = 1 at log10 m ~ 3.7 -- FLOOR_ERODES, the r349 floor question answered NEGATIVELY (no stable floor > 1 certified; anatomy: the floor rows kz111/kz75 are the largest-FAB deepest-pk spikes, med pk 0.142 vs 0.069 comfortable -- the reserve dies exactly where the law coordinate peaks); (5) THE COMPOSITION MOVES THE HONEST UNIFORM m_0* BY ~4 DECADES: the class-free polylog route rho_2 <= C_FAB C_M2ENV/log m (14.93 x 26.01) solves m_0* = 10^18.9 UNIFORM with no spike/quiet split -- vs 10^22.6 (r349 record) / 10^23.5 (moved census-F ceiling) / 10^16.1-10^17.5 (class-conditional, non-uniform) / 10^13.5 (r306 census); cofinal typing: C_FAB/C_M2ENV freeze-census over 89 rows (extrapolation hypothesis stands), the floor letter is the open spike-arm need, src_ok False is the open mechanism, finite closure to m = 660, no second world -- and the next fresh teeth need a NEW construction family.  Exact spine warded on 91 live worlds: FAB identity 2.0e-16, r324 interpolation + pileup chain m q_max <= nsc x pil + group chain m q_max <= ngj x hgn all one-sided 0.0, NORM identity 9.0e-16, reserve decomposition 1.0e-15, Fractions pins exact.  Must-fails: e1 stale-qmax-record readback CAUGHT twice (AST qm + Fractions 1/2 vs 3/4), e2 fresh-selection-posthoc protocol-CAUGHT twice (AST rho + toy (2,3) vs (1,2)), e3 wrong-log-power CAUGHT exact (break == 2), e4 floor-bar-posthoc protocol-CAUGHT twice (AST rho + toy 0.5 vs 1.05), m5a/m5b FLAGGED.  Deterministic run1/run2 byte-identical up to WALL (cal 397.6 s).  Nothing here bounds anything beyond the measured rungs; a certified growth law is a LAW CANDIDATE with a frozen census constant, not a cofinal theorem; the named rests are the source formula (K3/K4 vacuity, the g21-style mechanism question) and the eroding reserve floor; NO RH CLAIM in either direction'

_R352_STATUS = "Rho_r source-anatomy round for L* (round 352, the named r350 follow-up: the LAST census member of the closed exponent chain -- the cancellation exponent rho_r = 2.624 of the bare reserve r_det = 1 - c^2/pq -- plus the g_K12 second-instrument lane; contract PRIME.LSTAR.RHOR_SOURCE_ANATOMY.01, experiments-side, NO ledger row): the exact spine -- the WEIGHT-FREE kernel correlation rho_K = K12^2/(K11 K22) = c^2/(d1 d2) (the weights cancel) with the exact identities (i) c^2 == rho_K d1 d2, (ii) r_det == 1 - rho_K d1 d2/(pq), (iii) the additive split r_det == (1 - rho_K) + rho_K(p + q - 1)/(pq), verified at machine precision on all 81 rows and in exact Fractions on the r342 hand toy (rho_K = 1/8, r_det = 23/24) (33/33; SPEC_SHA dc6bbd2cdfde8bbf final with record, freeze ad7a56682b4ecfd7, two-commit protocol: pre-freeze 88aae425 / record eb794e3a; ONE disclosed PRINT-ONLY amendment a1 = the EXT5 in/low band ledger field, the r349 every-hole-named precedent, no bar/rule moved).  MAIN VERDICT RHOR_REDUCED (ONE-OBJECT GRADE) on the sealed three-letter tree (TARGET_LEAK / RHOR_REDUCED / RHOR_IRREDUCIBLE) -- THE TWO NAMED RESTS OF r350 ARE ONE OBJECT: the leading laws cancel (|s_csq - s_pq| = 0.0004, the BK3 image -- rho_r is a SECOND-ORDER object, not composable from the candidate laws), and at the sealed common leading law A_LEAD = 17/12 the deficit fine structure phi_D = log(pq) + A_LEAD ln N and the kernel fine structure phi_K = log(c^2) + A_LEAD ln N are ONE SHARED WANDER: corr 0.999998, each column wanders 0.8787 nats while their difference is 0.0017 nats (500x smaller) -- and that difference IS the log reserve pointwise (phi_D - phi_K == -log(c^2/pq)), so rho_r is EXACTLY the decay of the shared-wander difference (|s_LR - s_rdet| = 0.0002; LR curv -0.767 == rdet curv: no clean power law in the weight-free normalization either -- a reduction AND identification, NOT a source derivation of 2.624).  + RHOK_LAW_FOUND(a_kap 0.7111 re-gates CLEAN (curv +0.328, EXT3 11/12, EXT4 5/6 low 0), hits [2/3, 3/4] mutually unresolvable; rho_K inherits a_rhoK = 2 a_kap = 1.4222 exactly, image [4/3, 3/2], doubled curv +0.656 disclosed) + DECOR_REFUTED(slope(1 - rho_K) = +0.0006: the kernel DECORRELATES -- the round's naming hypothesis refuted cleanly, the r348 CARRIES_DELTA motif; the carrier is the saturation of c^2/pq) + GK12_EXPLAINED(the one dirty r350 column factorizes pointwise as K12 == c[CLEAN law, curv +0.308]/sqrt(v1 v2)[closed-form dictionary] at recon 5.5e-4; the CD-recursion SECOND INSTRUMENT reproduces the Gram route on ALL 81 rows (max 7.4e-10 incl. N_w 5690) with an IDENTICAL refit law (1.5e-11): the dirtiness is a STRUCTURE effect, not a route effect; REL2 honest-negative: Q = K12/(K11 K22)^(1/4) FAILS the r345 flat protocol loudly (21 out / 8 hard, 1.21 dec) -- the r350 slope hit 0.035 was an after-fit artifact) + CANDIDATES_UNRESOLVED(sealed separation instrument on the 24-row deep cohort: a_p 3/4-vs-0.76 needs log10 N* = 29.5, a_q 2/3-vs-0.62 needs 8.3 (closer-count leans 0.62!), delta_0 0.38-vs-2/5 needs 4.7 -- the nearest resolvable ambiguity; the closer-count leans are census, never identifications) + EXT5(the r343 selection rule verbatim at the RAISED h cap (3400, 6000]: kz 69/107/101/99/115/89, N_w 4237..5690 = THE DEEPEST L*-WINDOWS EVER MEASURED, 1.8x the EXT4 record -- margins ALL POSITIVE 1.5e-9..4.0e-9: the L* condition holds 1.8x deeper out of sample; the bare laws p/q/c/kap EXTEND in-band while margin/reserve/K12 sit uniformly HIGH side of the 57-fit: the deep decay FLATTENS out of sample, the opposite side from the r342 EXT3 steepening -- census, the running-exponent question named for r353).  Balance re-gated: alpha == a_p + a_q + rho_r - a_(p+q) at dev 0.001, candidate image 3.352 (dev 0.019); the chain fully typed woerterbuch/candidate/satz/second-order -- THE SPECIALIST PACKAGE IS FINAL: ONE object (the r338-q1 backward-CS fine structure = the shared wander), all exponents measured, all identities exact.  Worlds: the rho_K census separates live below dead only by a thin 3.8x floor (SMOOTH) and the bare r_det sign does NOT separate (prints positive on all six dead at own N_w -- the r342 crossing lives in the DIAGONAL d >= 1) -- no new world criterion claimed; lambda_rest 4/4 vs 2/2 + kappa_int records re-gated.  Must-fails: m1 wrong normalization CAUGHT exact (7.6e4 at w9 + 2/69 Fractions), m4 CD-prefactor CAUGHT exact (1.2e0) + gram-readback AST-FLAGGED, m5 wrong REL2 power CAUGHT exact (0.850), m2/m3 AST-FLAGGED.  Deterministic run1/run2 byte-identical up to WALL (89.5/83.7 s).  Nothing here bounds anything beyond the measured rungs; the named rest is the SHARED WANDER phi (rms 0.88 nats, the single unexplained function of the L* margin legislation) and the curved rho_r value itself; NO L* claim, NO RH CLAIM in either direction"

_R353_STATUS = "Second construction family + preregistered erosion kill (round 353, the named r351 follow-up: the in-zone frame-A pool is exhausted, all 89 rows come from ONE construction family, and the reserve floor erodes towards a census crossing at log10 m ~ 3.7 -- is there a SECOND admissible window family on the same canonical source, and do the FAB law + the spike coverage survive there?; contract PRIME.L2.SECOND_FAMILY_EROSION.01, experiments-side, NO ledger row): frame-B = the HALF-RESOLUTION TENT FRAME NU_B = 2 (the window aspect NU in the mesh D = 0.5 gap/NU is the ONE construction parameter every round r238..r351 held fixed at 4; canonical von-Mangoldt tent assembly, archimedean lags and chain machinery VERBATIM -- no smoothing, the CLXVI lesson respected; the NU = 4 reproduction ward is EXACT: bit-identical wpack on w9 and pool == frame_a_zones 70/70), sealed selection on the extended used ledger (used 104, fresh 24 at h_B <= 4000 and z^2 <= 400000; stratum BZ in-zone grel-ascending kz69/kz80 -- the in-zone frame-B pool has EXACTLY 2 members, exhaustion disclosed up front -- + stratum BD deepest kz133/129/124/117/107/101), the full r351 89-row surface re-executed anchor-gated bit-near (r349 family + EXT4 records EXACT; r324 C_INF 1.7481 + violators + e_G +0.158; r329 C_NSC 2.0258 / C_NG 2.6351; r351 growth record C_FAB 14.93 @ kz111 + EXT5 FAB max 9.71 @ kz135 + kz79 F_ins 6.69 + rc_small +0.243; r351 floor record 28 family rows + min RSV 1.07 @ kz75 + e_RSV -0.649 + rc_fam -0.600 + C_M2ENV 26.01 + m_0* 10^18.9 + C_K2(83) 11.87 + rc_gap -0.623) (45/45; SPEC_SHA bd89e3316c332ded final with record, freeze 2c0e1c150b5721a8, two-commit protocol: pre-freeze ac4fbe28 / record b5e7f892; NO amendment after freeze; scoping disclosed: pool enumeration at NU in {2, 6, 8} + two wpack timings + the NU = 4 check, no bound value computed).  MAIN VERDICT SECOND_FAMILY_BUILT + FAB_LAW_BREAKS_ON_B([(kz117, 17.78), (kz124, 18.07)]) + FLOOR_KILLS([(kz124, 0.63), (kz129, 0.95)]) + GREL_LOWER_BOUND_CANDIDATE(0.187, 63.4) + BZ_POOL_EXHAUSTED(2) + NEW_DEPTH_RECORD(m 812) + NEW_FAB_RECORD(kz124, 18.07) on the sealed four-letter tree: (1) THE SECOND FAMILY EXISTS AND ADMITS CLEANLY -- all 8 sealed candidates pass POSITIVE_PREFIX + chain-completeness (N_w 1792..3972, 0 queue failures, mult <= 2 + non-degenerate 8/8; the r329 frame-A admission boundary nf 2125..2468 does NOT bind the half-resolution frame); every row SMALL-gap and SPIKE; the lane depth record moves to m = 812 = log10 2.91 (vs 660; the 3.7 crossing target NOT reached -- lever extension, disclosed); (2) THE r351 FAB CEILING IS A PER-FAMILY CENSUS, NOT A CROSS-FAMILY LAW: kz124 FAB 18.07 and kz117 17.78 both exceed the frozen C_FAB 14.93 (up to +21 pct) and the combined SMALL-gap trend rc_small +0.569 crosses the +0.5 growth bar for the first time -- the law keeps its FORM on frame-B (C' = 18.07) but the frozen constant is family-indexed; (3) THE PREREGISTERED KILL FIRED, EARLIER THAN THE EXTRAPOLATION PREDICTED: kz124 (m 757) RSV 0.63 and kz129 (m 787) RSV 0.95 breach RSV_KILL = 1.00 (kz133 at 1.00 bar-miss) -- the sliding spike coverage GSQ F^2 >= rho_2 is FINITE, dying at m ~ 760 on the second family instead of the extrapolated m ~ 5000 (combined 36-row fit e_RSV -0.889 / rc -0.706 / crossing log10 m ~ 3.4: the erosion ACCELERATES cross-family); the r346/r349 three-arm cover is bounded to the measured frame-A range and the cofinal reading needs a FOURTH mechanism (or a family-indexed sliding constant -- both typed honestly); the kill rows are again the largest-FAB rows: the reserve dies exactly where the law coordinate peaks, now on BOTH families; (4) THE K2 KLEIN-GAP PRODUCT IS THE CROSS-FAMILY SURVIVOR: FAB grel <= 11.87 holds 0/8 (max 5.95; the EXT5 rows do not lift the 83-row constant) -- the only frozen constant of the lane that carries across the aspect change; g_min = 0.187 yields the first non-vacuous implied ceiling 63.4 <= 4 x 18.07 (GREL_LOWER_BOUND_CANDIDATE, census); the r329 counting constants hold 8/8 (reserves 1.61/2.79) -- the O(log m) counting side survives its FOURTH fresh cohort and FIRST cross-family test; (5) the synthesis moves the ceilings backwards honestly: C_FAB' 18.07 / C_M2ENV' 44.18 -> class-free polylog m_0* = 10^20.5 (+1.6 decades vs r351); the five r351 holes retyped: freeze-census CONFIRMED (ceilings move out-of-family), floor KILLED, source formula ADVANCED (K2X + measured gap floor; K3/K4 untested), finite closure to m = 812, second WORLD still open (frame-B is a second construction, not a second arithmetic).  Worlds: w9B FAB 1.53 / w13B twin 1.64 (protocol carries); frame-B SCRAMBLE @ kz80 breaks AT ADMISSION (nf = 3).  Exact spine on 101 live worlds: FAB identity 2.0e-16, interpolation/pileup/group chains one-sided 0.0, NORM 9.0e-16, decomposition 1.0e-15, frame-B contribution ward 1.4e-12 (a-priori bar 1e-3).  Must-fails: e1 nu-posthoc protocol-CAUGHT twice (AST rho + toy 8 vs 2), e2 admit-posthoc protocol-CAUGHT twice ((2,3) vs (1,2)), e3 killbar-posthoc protocol-CAUGHT twice (0.5 vs 1.00), e4 wrong-log CAUGHT exact (break == 2), m5a/m5b FLAGGED.  Deterministic run1/run2 byte-identical up to WALL (cal 614.4 s).  Honest negatives: the depth gain is 0.09 decades; kz69/kz101/kz107 anchor ZONES were touched by the parallel r352 L*-lane EXT5 (margins only, different window construction -- anchor-zone overlap disclosed, no law column shared); nothing here bounds anything beyond the measured rungs; NO RH CLAIM in either direction"

_R354_STATUS = 'Phi-wander anatomy round for L* (round 354, the named r352 follow-up: the shared wander phi -- the single unexplained function of the L* margin legislation -- as its own lane, plus the running-exponent model of the EXT5 high-side flattening; contract PRIME.LSTAR.PHI_WANDER.01, experiments-side, NO ledger row): 33/33 sealed; SPEC_SHA f9db84da7f0f6f6e final with record, freeze c37ac54e9cbe41e9, two-commit protocol: pre-freeze 8b1361e9 / record 4be9d3a6; TWO disclosed calibration amendments a1/a2 (measurement-scale/robustness class: the reduced-builder ward at the natural lambda scale; finite-log usable-row clause on the world census channel -- no adjudication bar, band, family, block, feature or candidate list moved).  MAIN VERDICT PHI_DICTIONARY_GO on the sealed tree (TARGET_LEAK / PHI_DICTIONARY_GO / PHI_OPAQUE) -- THE PHI LANE IS SOURCE-SIDE CLOSED AT COMPUTABILITY GRADE: the pointwise composition c_pred = sqrt(vpred1 vpred2) x K12cd (closed-form digamma/tent weights x recursion-computable cross kernel, no measured kernel column consumed) reconstructs c on all 85 rows at max 5.52e-4 and predicts the kernel fine structure at corr 1.0000000 / rms ratio 0.0004 (phi rms 1.0489 nats on the 85) -- honesty: a computability closure, NOT a closed form and NOT a derivation of the wander.  + PHI_CARRIER_CENSUS(no single CD source block passes the sealed clauses; the reading: P2/PG (the pair-geometry composite) carries the SHAPE (corr 0.887) at 2.4x amplitude while the weight block W is ANTI-correlated (-0.72) -- phi is a TWO-BLOCK INTERFERENCE of pair-geometry against dictionary weights, localized, not reduced) + PHI_NFUNC_CENSUS(phi is NOT a function of N alone: N-adjacency ratio 0.911 on 74 pairs; grel/lnz do not carry, ratios 0.81/0.91 -- the wander is pair-local) + RUNNING_CENSUS(the two-parameter model s(N) = s_inf + b/lnN does NOT collapse the cohorts: the 0.88-nat wander defeats the 0.5-dec band on margin/rdet/K12 (viol 18/6/25 of 85 vs pure 20/7/26); s_inf(margin) 1.65 vs s_pure 3.33 = FLATTER, census-grade, candidate images far; the clean bare columns p/q/y0r DO collapse at 0 violations but their pure power also holds) + DELTA0_UNRESOLVED(the sealed r352 separation instrument on the EXTENDED 28-row deep set via the exact reduced route y0r = 1 + (u1.u2)/c, warded 6.6e-14 on the 75: a_p needs log10 N* 31.5, a_q 8.5 with the 0.62-lean confirmed 27/28, delta_0 5.4 (the r352 4.7 GROWS -- deeper is not cleaner) and the running re-arithmetic moves every depth farther; THE POOL TRUTH: the admissible pool is EXHAUSTED at h 7942 = 10^3.90 -- delta_0 is UNDECIDABLE inside the document frame, typed for the specialists) + EXT6(the r343 rule at h (6000, 60000] finds exactly 4 fresh windows kz 133/129/124/117, N_w 6532..7942 = THE DEEPEST L* WINDOWS EVER MEASURED, 1.4x the EXT5 record -- MARGINS ALL POSITIVE 1.13e-10..1.70e-9: the L* condition holds 1.4x deeper out of sample; the flattening CONTINUES AND SPREADS: margin/rdet/LR/rhoK/K12 all HIGH side, now the bare p/kap laws sit 2/4 with out-rows high too) + WORLD/TWIN(first world test of the fine structure: MAIN mini corr 0.999994; ABS shares the phi coupling at corr 0.9988 / 3x amplitude, DIR degenerate at corr 1.0 / 67 nats, SMOOTH/SCR below the usable minimum, EPST/HL2 not ladderable -- the coupling is NOT live-exclusive where measurable, only amplitudes separate, census; twin pointwise phi devs <= 1.9e-7 nats, dose-zero bitwise 6/6).  Must-fails: m1 A_LEAD-after-sight AST-FLAGGED, m2 c-readback AST-FLAGGED + no-prefactor CAUGHT exact (1.195), m3 running-after-sight AST-FLAGGED, m4 feature-from-target AST-FLAGGED, m5 flipped running term CAUGHT exact (4.07 dec).  Deterministic run1/run2 byte-identical up to WALL (128.6/129.6 s).  Nothing here bounds anything beyond the measured rungs; the named rest is the two-block cancellation ratio (why P2 and W cancel to 0.88 nats -- the sharpest remaining form of the r338-q1 question); NO L* claim, NO RH CLAIM in either direction'

_R355_STATUS = 'K2 source formula round (round 355, the reviewer fork after r353: terminal lane on K2/Klein-gap geometry ONLY -- a source-pure statement controlling q_max from a LOWER gap bound, plus the source-side origin of the gap bound itself; contract PRIME.L2.K2_SOURCE_FORMULA.01, experiments-side, NO ledger row): 47/47 sealed; SPEC_SHA 1f14bd938ba78cc4 final with record, freeze b0dd5a93a9d5b790, two-commit protocol: pre-freeze 94f0683a / record 397a1032; NO amendment after freeze (calibration pass 1 = first full evaluation = 47/47, 816.8 s); scoping disclosed: NU = 3 pool enumeration (16 fresh, in-zone EMPTY at every aspect) + two admission timings, no bound value computed.  MAIN VERDICT K2_LAW_CERTIFIED_NU_FREE + K2_SOURCE_CHAIN_OPEN + GMIN_LAW(e_g -0.252, mono 0.80) + INZONE_EXHAUSTED_ALL_NU(0) + K2_TEST_MAX(kz103, NU3, 10.62) + GMIN_IMPLIED(NONE, e_impl +0.29) + NU_RATIO_CENSUS(med 0.19) on the sealed five-letter tree: (1) K2 SURVIVES ITS SECOND INDEPENDENCE TEST -- THE WINDOW ASPECT: the frozen C_2 = 11.87 (max FAB grel over the 89 sealed r351 rows) holds with ZERO violations on all 25 test rows (8-row frame-B regate + 12/12 admitted NU-test rebuilds of the sealed six zones kz111/75/51/65/79/103 at NU in {2, 3} + the 5/5 fresh NU = 3 field kz99/115/89/86/132, N_w 2961..3805, 0 queue failures, 0 post-eval drops); closest call kz103 at NU 3 (10.62, 11 pct below); the census contrast: the bare FAB coordinate is aspect-WILD (kz99 NU3 FAB 19.38 = NEW lane record above the r353 18.07; kz103 3.69 -> 12.98; median FAB(NU2)/FAB(NU4) 0.19) while the K2 product absorbs it all -- the gap product is the aspect-stable coordinate, the FAB ceiling is C(NU, family) census; (2) THE SOURCE CHAIN CLOSES EXACTLY, ITS CENSUS CAPS ARE VACUOUS: FAB grel <= (ngj/log m)(hgn grel) one-sided exact on 118 live worlds (r327 group chain) and the mesh identity h - NU u in (0, 1.5] (u = alpha/gap, the NU-free depth coordinate) EXACT on every pool zone at all three aspects -- WHERE grel enters is now construction algebra; but C_H = max hgn grel = 141.71 / C_P = max pil grel = 141.53 (both kz111) imply 373.4 / 286.7 >> the a-priori bar 47.5 (0 test violations, but vacuous -- the r351 K3/K4 vacuity repeats at the grel-sharpened caps; the chain loses at the heavy-group step, bshare med 0.41 off-family); the r329 counting constants hold on all 17 NU rows (reserves 1.35/1.81 -- FIFTH cohort, FIRST aspect test); (3) THE LOWER GAP BOUND IS A SLOW MEASURED LAW BUT SUPERCRITICAL AS A CEILING ROUTE: g_min(u) over 130 admissible zones (6 dyadic bins, minima 0.482 -> 0.187, mono 0.80, halves-slope -0.252, GMIN_LAW census; the depth-gap coupling h = NU u partly builds this in, disclosed); e_impl = -e_g/e_um = +0.286 > CRIT_EXP 0.224 -> the growing ceiling C_2/g_min(m) has NO m_0*; the flat-floor route at the pool floor 0.187 gives C_FAB^K2 = 63.4 -> m_0* = 10^23.5 (3 decades worse than the r353 direct 10^20.5) -- the K2 detour needs a genuinely diophantine floor, not the measured envelope (NO Baker bounds attempted, the r289/r331 lesson).  Cofinal typing: SATZ links = r324 identity + r327 group chain + mesh identity + dictionary q_max; CENSUS rest = C_2 (2 families + 3 aspects), C_NG, C_H/C_P (vacuous), g_min -- the whole spike mechanism reduces to the census-to-law promotion of [gap floor] x [counting] x [heavy-group mass], the diophantine gap floor the named rest.  Worlds: w9B FABg 0.74 / w13B twin 1.35 / EPSTEIN 0.41; frame-B SCRAMBLE @ kz80 breaks AT ADMISSION (nf 3, r353 reproduced).  Must-fails: e1 hfun-posthoc protocol-CAUGHT twice, e2 c2-posthoc protocol-CAUGHT twice, e3 nu-shared protocol-CAUGHT twice + the live freshness ward (strict N(NU2) < N(NU3) < N(NU4) on 12 admitted test rows), e4 wrong-log CAUGHT exact (break == 2), m5a/m5b FLAGGED.  Deterministic run1/run2 byte-identical up to WALL (852.0/794.4 s).  Honest negatives: the in-zone fresh pool is exhausted at EVERY aspect (the fresh field tests the out-of-zone deep regime only); the source formula stays open (caps vacuous); nothing here bounds anything beyond the measured rungs; NO RH CLAIM in either direction'

_R356_STATUS = "Borodin dual-hole round (round 356, the ONE approved internal L* round after the DCCIV idea search -- Sol's Borodin particle-hole contract plus Fable's AC-class falsifier as co-deliverable; contract PRIME.LSTAR.DUAL_HOLE.01, experiments-side, NO ledger row): 34/34 sealed; SPEC_SHA 36141c0ae9ed8f35 final with record, freeze 5d277d576df75d3a, two-commit protocol: pre-freeze 58bb09bb / record 5d351e90; ZERO amendments after freeze (calibration pass 1 = first full evaluation = 34/34, 115.0 s); scoping disclosed (s1 four rungs, s2 world channel machinery, s3 EXT6 timing + f64 resolution truth).  MAIN VERDICT DUALITY_REPARAM_ONLY + AC_CLASS_EXCLUDED + ANTI_DESIGN_GATED + RESERVE_LOCALIZED: (1) THE ALGEBRA IS EXACT ON THE WHOLE LADDER -- lift to eta = mu + nu, Q = E(I+E)^{-1} (Fractions 0, f64 <= 7.6e-12 on 85 rows), Borodin complementation Pi_N^u = D(I - Pi_{N-1}^{u_vee})D at half filling S = 2N-1 (support gate BITWISE 85/85: the union support IS the full cosine grid and the r228 half-filling law IS the rank condition), spectral map margin == 2 - 1/lambda_min(R) (L* IS R > I/2, measured live to lambda_min - 1/2 = +6e-11 at EXT6), pair identities c == eps1 eps2 (R^{-1})_{12} / p == 2 - (R^{-1})_{11} -- the r342 pair block IS the (1,2) minor of 2I - R^{-1}; the reciprocal weight u_vee == c_j (1-x)/|f| EXACT incl. endpoint halving (route A == B <= 5e-9, B == C 4.4e-16); (2) THE R354 ANTI-CORRELATION IS DUALITY ALGEBRA: corr(psi57 DW, psi57 W) = -0.999998 gated -- +log|f| vs -log|f| by design; (3) NO COMPRESSION: no dual block (DW/DK/GC) passes the sealed carrier clauses (best GC leave-out 1.021; compression clause vs the in-run r354 four-block base 0.966 does NOT fire; the sum block DW+DK = log c^2 - GC is near-tautological, corr 0.9991, excluded by design) -- the duality is a REPARAMETRIZATION, the L* lane is FINAL at the specialist memo; (4) RESERVE_LOCALIZED (census-grade positive finding): the LOCAL dual 2x2 block (R_pair)^{-1} predicts the log reserve without p/q/c readback and without global inversion -- corr(psi57) +0.9982 / leave-out 0.068 on the 57, EXT PURETEST +0.9828 / 0.165 on 28 deep rows: the 500x cancellation is carried by the local dual two-point data; (5) AC_CLASS_EXCLUDED (for the memo): rescaled pair positions family-constant against pi^2 f^2/4 (max dev 0.33/N_w, folds (2,4) uniform on 85/85) while a_rhoK = 1.4222 == the r352 record where the Lubinsky-type AC/Bessel class demands rho_K -> const -- the window-kernel universality class is NOT the AC class; (6) DEMARCATION vs r227/r228 machine-checked: the old signed-Hankel duality died on zero weights (R_DUAL_OBSTRUCTED), the positive lift has u > 0 everywhere and the dual weight finite -- the obstruction is structurally absent, and the DUAL_WALL_EQUIVALENT death pattern materialized exactly as the enum anticipated (as DUALITY_REPARAM_ONLY, typed).  Worlds: MAIN mini corr 0.994 GATE, all four dead worlds LOSE (reserve cone EMPTY off the wall 0/6 each; lambda_min(R) - 1/2 = -0.083..-0.500 vs MAIN positive), TWIN dual-pointwise 7.8e-4 nats (bar 1e-3, 1.3x headroom disclosed); EXT6 f64 sign truth disclosed (kz133 margin_dual flips sign inside the ~5e-10 resolution).  Must-fails m1-m6 loud/AST (P'-unsquared, rank-N, mu-only nodes, mass permutation, R_12-local, LR/c readbacks).  Deterministic run1/run2 byte-identical up to WALL (117.1/114.9 s).  NO L* claim, NO RH CLAIM in either direction"

_R357_STATUS = "GRH-faithful matched Dirichlet frame round (round 357, the reviewer rank-2 fork after the r355 substance condition -- the missing second arithmetic demanded by both lanes since r338-U5; contract PRIME.WORLD.DIRICHLET_MATCHED_FRAME.01, experiments-side, NO ledger row): 33/33 sealed; SPEC_SHA 4bf1a94b03c7d227 final with record, freeze 4be4777fd6ec5bdf, two-commit protocol: pre-freeze 1381f6ea / record a953ab29; ONE disclosed calibration amendment a1 (the r330-a1 representation lesson exactly: the r329 counting constants ARE the frame-A ladder maxima kz16/kz36, re-frozen live at full precision, anchor-gated at 5e-4; no adjudication rule moved).  THE FRAME DERIVATION (Leg 0, sealed): for chi mod q odd (a = 1) the completed Lambda(s, chi) = (q/pi)^((s+a)/2) Gamma((s+a)/2) L(s, chi) gives the matched arch density F_A^chi(xi) = -log(pi/q) + Re psi((1+2a)/4 + i xi/2); in lag space this is EXACTLY the document arch_A body with kernel e^{-w/2} -> e^{-(1/2+a)w} and constant -(gamma+log pi) -> -(gamma+log(pi/q)) (Gauss digamma integral gated 0.0 at a = 1; trivial frame a = 0, q = 1 reproduces zeta's arch/prime/build/terminal layers BITWISE; matched border companion = smooth comb through the SAME chi arch; chi mod 3 comb == the r330 DSW comb bitwise).  MAIN VERDICT SECOND_ARITHMETIC_LIVES + MECHANISMS_TRANSFER(TWO_ATOM, DET_COND, DICT) + K2_CENSUS + DICTIONARY_TRANSFERS + PHI_CENSUS + R330_READJUDICATION + CHI4_LEDGER(ALIVE) + CONTROL_LEDGER + CONVENTION_LEDGER: (1) THE WALL LIVES ON THE MATCHED FRAME -- THE r330 DEATH WAS A FRAME ARTIFACT: chi mod 3 holds the E-Gram wall on 42/42 windows (margins 8.10e-6..3.34e-3 ALL positive, minC None to the window depth) AND the terminal half-filling wall (nf None 42/42 -- the SAME comb that died at nf 24 through the unmatched frame, baseline-gated); chi mod 4 identical (42/42 + 42/42): living-world evidence n = 1 -> 3 arithmetics on 126 windows; (2) the verbatim r330 battery re-adjudication (identical class rules, identical live-frozen C_2 = 1.069434): ALL FOUR r330 splits RETYPED_FRAME_ARTIFACT -- HALF_FILLING CTRL->MAIN, RENYI3_C2 CTRL(32/42, max 27.6x)->MAIN(0/42), SIGMA_DECAY SPLIT(+0.793)->MAIN(-0.578), O_SIGN CTRL->MAIN(O<0 on 20/42); battery 7/7 MAIN-side, status ALIVE for both characters; (3) PINNING FINE STRUCTURE (fresh coordinate): MAIN pins at minC_ext == N_w+1 exactly; the chi worlds are NEAR-pinned (offsets 0..9, chi3 med 1.5, exactly pinned 8/42) -- the exact half-filling pinning is so far zeta's sharpest signature, census; (4) K2 SPLITS: the frozen C_2 = 11.87 holds 0/126 (MAIN max FABg 6.95 / chi3 4.73 / chi4 5.16 -- the Klein-gap product is ARITHMETIC-ROBUST census, now 2 families + 3 aspects + 3 arithmetics) BUT the r329 counting constants BREAK on the second arithmetic (chi3 kz33 nscl +19 pct / kz14 ngl +28 pct, chi4 1 violation) -- the O(log m) counting side is ZETA-CALIBRATED census, sealed letter K2_CENSUS; (5) DICTIONARY_TRANSFERS: v_pred with the chi offset predicts the second arithmetic's nu weights at median 4e-4 / max 3.3e-3 over 42 rungs, density dictionary <= 7.5e-3 at the sample pair folds -- the r342 weight dictionary is explicit-formula-generic; (6) PHI DOES NOT TRANSFER (the honest negative): co-wander corr 0.9817 / rmsr 0.3187 = 3x suppression vs MAIN 439x on the identical instrument (clauses 0.99/0.2) -- the chi pair sits FAR from the binding point (r_det med 0.247 vs MAIN 1e-2..1e-6, PR med 1.26, two delocalized rungs): the 500x suppression is the signature of NEAR-CANCELLATION, which only zeta's world exhibits at these depths -- information about the BINDING REGIME, not the frame; (7) CONTROLS: rational twin of the chi comb carries (devs <= 7.9e-6); matched-frame SCRAMBLE breaks (E-margin -2.6e+2, minC 38/184, nf 37) -- the matched frame does NOT rescue a scrambled comb.  Must-fails: m1 conductor dropped -> density shift == log 3 EXACT (3.8e-15); m2 wrong parity -> 0.24 >= 0.2 loud; m3 permuted character table CAUGHT at the named witnesses; m4 MAIN-arch dictionary -> 4.43 >= 0.5 loud; m5 C_2 recalibration protocol-CAUGHT twice (AST fabg_true + toy 3.0 != 1.0); m6 MAIN blend AST-FLAGGED.  Deterministic run1/run2 byte-identical up to WALL (20.1 s).  READING: wall, battery, two-atom mechanisms, determinant condition, weight dictionary and the K2 gap product are EXPLICIT-FORMULA-GENERIC; zeta-graded remain the exact pinning, the near-saturated reserve, the 500x phi suppression and the counting constants -- the L* margin legislation is a statement about how CLOSE zeta sits to the wall; the chi worlds obey the same law far from it.  NO RH CLAIM, NO GRH CLAIM in either direction"

_R358_STATUS = "The weighted small-gap Carleson packing (round 358, reviewer contract T1 PRIME.L2.K2.LOCAL_GAP_CARLESON.01, theorem-first: replace the r355 global-minimum composition -- one small gap sets the bound for the entire mass, supercritical e_impl +0.286 -- by the weighted DISTRIBUTION of the small gaps; experiments-side, NO ledger row): 20/20 sealed; SPEC_SHA fb2d499fd984cef3 final with record, freeze 8831b1410849f1b4, two-commit protocol pre-freeze 9141d3e7 / record f0f034a2; NO amendment after freeze (calibration pass 1 = first full evaluation = 20/20, 711.3 s); scoping disclosed (machinery validation at w9 only: quantization 5.7e-14, w9 g in [0.875, 1.5], S_r = 0 -- every deep column genuinely open).  THE SEALED g_i COORDINATE: block centers of the r314 fold groups on the theta grid LL = 4N-2 (positions + block ids only, values NOT consumed), one-sided min gaps in grid units, EFA.grel_col normalization VERBATIM (w = 5) -- the zone-grel convention one level down; q_i = |x_i|/L (r339 FDD leaf convention); the mesh identity h - NU u in (0, 3/2] re-warded EXACT on (114, 70) pool zones -- the coincidence is mesh-parametrized, fit-free.  MAIN VERDICT QUADRATIC_LAW_PARTIAL(T1@all four) + SIEVE_CORE_OPEN on 181 rows (89 frame A + 8 frame B + 42 chi3 + 42 chi4; anchors bit-near: C_K2X 11.87 at kz111, the r353 8-row FAB/grel table + K2 max 5.95, the r357 chi maxima 4.73/5.16/6.95): (1) THE CORE HOLDS -- T2' IS A 0-VIOLATION CENSUS THEOREM ON ALL FOUR ARITHMETIC/FAMILY WORLDS: the quadratic packing law S_r = sum_{g_i <= 2^-r} q_i <= 2^{-2r}(1+r)^2 holds POINTWISE on all 181 rows at every dyadic level r = 1..12 with a-priori bars sealed BEFORE any evaluation (no calibration needed); the whole small-gap mass lives at r = 1 (max S_1 = 0.017/0.005/0.024/0.044 per family, carried by 12+4+1+3 rows), S_r = 0 IDENTICALLY for r >= 2, and the minimal normalized local gap of the entire round is 0.375: gaps below one quarter of the local median DO NOT OCCUR in either construction family or any of the three arithmetics -- very tight coincidences do not exist AT ALL on the admitted surface, let alone with mass; T2val max 1.29/1.33/1.14/1.13, C_G_cens 0.100 at A = 2 (dyadic summation T2' => T2 warded exact one-sided 0.0); (2) T1 IS DEPTH-GRADED CENSUS, NOT A FIRST-K LAW (the honest partial): the r306 first-K freeze fails the localization on ALL FOUR families (frame A C_K 2.45 vs test max 15.93 at kz111, 27/84; frame B 4.91 vs 23.70 at kz117, 6/6; chi3 1.52 vs 3.91 at kz32, 14/37; chi4 1.62 vs 3.09, 12/37) -- the local product (m q_i/log m) g_i grows with depth exactly like the K2 product (the max rows ARE the K2 spike rows): the localization is the right coordinate but a shallow-rows freeze is the wrong constant rule at every level (the r324/r351 lesson measured locally); the packing FORM with a-priori bars is the family-robust statement; (3) the small-ball band structure (building block D) carries as census: 1033 dyadic source bands, 0 violations of SB_r <= 2^{-2r}(1+r)^2; the stress spikes kz51/kz111 have NO sub-half gap at all (min g 0.533/0.571) -- the spike atoms are NOT tight-gap atoms; band alignment med 0.24..0.28 BELOW the 0.5 floor: comparability holds in MASS form, not signed-survival form (typed honestly, the sieve target is the mass form); (4) the composition is pure polylog but census-expensive: M_3 <= C_K^2 C_G (log m)^4/m^2 with the measured ceilings gives m_0* = 10^23.5 vs r351 10^18.9 / r353 10^20.5 / r306 census 10^13.5 -- C_K enters SQUARED where FAB enters once; the winning form needs a family-uniform T1 constant RULE; all exact wards close (M3 composition 0.0 one-sided, N2 >= N3 181/181, quantization 9.1e-13, mult <= 2 on 181/181, FAB identity 2.0e-16, K2 chain 0.0, FDD dictionary 2.5e-16); (5) typing: SATZ = fold multiplicity 2 + mesh identity/quantization + dyadic summation + N2 >= N3 + the M3 algebra; DICTIONARY = FDD q_i + band mass comparability; CERTIFIED CENSUS = T2' 0/181x12 + small-ball 0/1033 + min-g floor 0.375; OPEN (named specialist questions) = (i) the in-the-mean sieve: for the folded log p^k phases prove sum_{i in B, g_i <= t} a_i <= C t^2 (log m)^B sum_B a_i per dyadic source band (small-ball / large sieve on average, NO pointwise Baker bounds), (ii) the family-uniform T1 constant rule.  SCRAMBLES: all three matched channels (frame-A w9 nf 21 / frame-B kz80 nf 3 / chi3 w9 nf 37) break at P1 = POSITIVE_PREFIX ADMISSION under the sealed precondition order -- the packing's binding source precondition is the admission of the arithmetic comb itself; twin devs 1.0e-7.  Must-fails: e1 g-from-q protocol-CAUGHT twice; e2 global-gmin CAUGHT exact (the mutant breaks the sealed bar at S_2 1.00 > 0.5625 where the true column passes -- the r355 supercriticality reproduced as a mutant); e3 hidden frame-A constant protocol-CAUGHT twice; e4 bars-posthoc protocol-CAUGHT twice; e5 wrong mesh interval CAUGHT exact; m6a/m6b FLAGGED.  Deterministic run1/run2 byte-identical up to WALL (711.3 s).  NO RH CLAIM in either direction"

_R359_STATUS = "The exact critical Schur block in the positive dual space (round 359, reviewer contract L1 PRIME.LSTAR.DUAL.SCHUR_WRONSKIAN.01, the favourable pre-attempt before the RHP project; experiments-side, NO ledger row): 33/33 sealed; SPEC_SHA d00fdc96a3667a52 final with record, freeze f42fa664e6970863, two-commit protocol pre-freeze ad74f3e0 / record b96f819d; two disclosed calibration amendments a1/a2 (shallow coupling/res-minor bars re-sized inside the disclosed 1/eps noise class; Sturm census lists per world -- representation only, no adjudication rule moved).  THE EXACT IDENTITY CHAIN (theorem-grade skeleton, Fractions-exact on a rational 5-atom model, graded green on 85 MAIN + 42 chi3 + 42 chi4 rows): with M = R - I/2 the Schur split {M > 0} <=> {M_CC > 0} AND {S_N > 0}; Sylvester bordered minors (S_N)_kl det M_CC == det M_{C+k,C+l} (the reserve as a ratio of bordered minors, rest block inside the border); the CD/Casoratian structure of R in the two consecutive dual orthonormal polynomials; the discrete IIKS commutator identity: the off-diagonal of the dual resolvent (I - 2R)^-1 IS the Casoratian of resolvent-dressed consecutive dual OPs; coupling adjugate identity (S_N)_12 == 2 (A^-1)_12 det S_N and the resolvent-minor form det S_N x 4[(A^-1)11 (A^-1)22 - (A^-1)12^2] == 1.  MAIN VERDICT ASYMPTOTICS_REQUIRED + STURM_CENSUS: the binding thesis is the round's sharpest measurement (bind = lamS/eps in [1.0003, 1.0605] med 1.0058 on the 74 resolvable rows -- the critical 2x2 Schur block CARRIES the full L* margin; det S_N tracks margin^2, slope -6.742 vs -6.665); NO standalone explicit P_N exists at the sealed bars (the Christoffel-class candidate misses by ~14 orders; the diagonal-parametrix form misses by exactly the measured cross share, med 0.702 -- the off-diagonal Casoratian term carries 46..84 pct of the resolvent minor); P_N is NOT a margin readout (restatement corr +0.9924 < 0.999): L2/CRITICAL_SATURATION is the named non-optional next step with the precise object (A^-1)_kk at the critical pair + the cross share as handoff; the Sturm sign pattern is NEAR-WALL-GRADED, not universal (84/85 MAIN rows in one interlaced-straddle pattern, the single deviation kz133 = the disclosed r356 f64 sign-resolution row; far from saturation P_N < 0 on 12/42 chi3 and 13/42 chi4 rows -- a globally positive standalone P_N is excluded at census grade, the universal Sturm carrier refuted, the near-wall pattern banked with the named theorem type discrete Sturm interlacing / Markov-Stieltjes); the rest clause (the reviewer's L2 clause) is positive on every live row but DECAYS PARALLEL (slope -3.276 vs margin -3.332, rest/eps med 20.3) -- phrase it relatively in L2; the matched scramble breaks at the NAMED precondition R_CC > I/2 (-0.4962) while every algebraic ward passes and the pair Schur block alone stays positive (+1.37e-2): pair-only reasoning would misclassify the dead world.  Must-fails: m1/m2/m5 AST (withheld lamR/margin/detS columns); m3 pair-only 4.07 nats + Fractions-exact; m4 wrong dual-OP indices 2.02 rel + Fractions-exact; m6 non-consecutive 1.08 rel + Fractions-exact.  Deterministic, record run1/run2 byte-identical up to WALL (136.3 / 150.1 s).  NO L* claim, NO RH claim in either direction"

_R360_STATUS = "The critical saturation scaffold (round 360, reviewer contract L2 PRIME.LSTAR.DUAL.CRITICAL_SATURATION.01, triggered by the r359 ASYMPTOTICS_REQUIRED handoff; experiments-side, NO ledger row): 34/34 sealed; SPEC_SHA ea24936c46407f48 final with record, freeze 75f8ee55436ab173, two-commit protocol pre-freeze 8a835dc8 / record 130a0889; ZERO amendments after freeze (calibration pass 1 = first full evaluation = 34/34, 153.7 s); scoping s1/s2 disclosed in the spec.  THE EXACT OBJECTS: the occupation duality o_eta + o_dual == 1 on every union node (diagonal of the r356 Borodin complementation, Fractions-exact on the toy, <= 2.2e-11 live) with the exact trace ward sum o_dual == N_w - 1; the sealed zero-temperature obstacle solver (FISTA 3000 iters, water-filling projection, KKT gates) for the BKMM constrained equilibrium with field -log u_vee.  MAIN VERDICT SATURATION_EDGE_CONFIRMED + GAMMA_PARAMETRIX_CENSUS + M0_PARTIAL(3.332) + REST_RELATIVE_CENSUS: (1) the QP dual-void block == folds {1,2,3} with clean KKT on 4/4 sealed instances (kz 9/44/56/130) -- by the exact complement the PRIMAL SATURATED block -- and THE CRITICAL PAIR (2,4) STRADDLES ITS EDGE 3|4; the exact-occupation fold-1 anomaly census 85/85 (dev1 in [-0.333, -0.253], pair folds flat); the chi contrast is a DIFFERENT partition (fold-1 anomaly 0/42 + 0/42, both chi QPs occupy fold 1) -- the reviewer's step-B object, census grade; (2) t_geo = eps sqrt((A^-1)_11 (A^-1)_22) is margin-locked (slope -0.009 on the 57, range [0.2216, 0.2865] med 0.2536 on all 74 resolvable rows + chi w9 in band); the resolvent diagonals carry the margin exponent (+3.365/+3.292 vs 3.332), not the 0.38/1.79 weight families; (3) alpha = 3.332 hit at 0.002 (fresh lamS slope -3.334; s_infty 1.65 rejected at 1.684), bind med 1.0058 == r359, but kappa_S wanders 4.88x > 1.5: THE FULL M_0 COLLAPSE IS REFUTED -- the L1 target needs a relative/projective form; (4) the relative rest clause is THEOREM at c = 1 (Cauchy interlacing + Schur eigenvalue inequality, toy exact + live 74/74) and MAIN census at c >= 8.8, but the chi ladders dip to the interlacing line (mins 1.0 on 3 + 8 rows): RELATIVE_REST_CERTIFIED correctly did NOT fire -- the c > 1 margin is NOT world-uniform; (5) wander cancellation measured: corr(psi57 log detS, -psi57 log(a11 a22)) = +0.9835, share-term rms ratio 0.204.  Worlds: twin dose-zero bitwise (occupation devs 3.8e-8); scramble breaks at the named R_CC clause (-0.4962) with no saturation edge.  Must-fails: m1 unconstrained equilibrium 92.7x cap, m2/m3/m4 AST (withheld margin/detS/a11 columns), m5 weight shuffle 0.798, m6 wrong rank 1.17e-2 + Fractions-exact.  Reviewer-step typing (the handoff deliverable): (A) theorem (r356); (B) saturation edge confirmed census-grade, asymptotic equilibrium theorem OPEN; (C) parametrix census, Gamma derivation OPEN; (D) adjugate theorem + measured cancellation + M_0 partial; (E) rigorous error OPEN.  Deterministic, run1/run2 byte-identical (172.2/157.0 s).  NO L* CLAIM, NO RH CLAIM in either direction; mincut unchanged."

_R361_STATUS = "The mean sieve on the folded log-p^k phases, adjudicated floor-first (round 361, PRIME.L2.MEAN_SIEVE.01, the named theorem rest of the terminal lane after r358; experiments-side, NO ledger row): 21/21 sealed; SPEC_SHA 1bec71757eb909d7 final with record, freeze 0dafa3b962e337b3, two-commit protocol pre-freeze 7f17e3cf / record 2d7d0376; ZERO amendments after freeze (calibration pass 1 = first full evaluation = 21/21, 655.6 s).  MAIN VERDICT FLOOR_THEOREM -- the r358 0.375 floor IS construction algebra: the exact Fractions ledger (integer theta-grid positions, exact block centers/gaps/window medians) reproduces the r358 float ledger bitwise on all 181 rows (89 frame A + 8 frame B + 42 chi3 + 42 chi4; collisions 0, rounding 9.1e-13); SEP-SATZ (the algebraic half, derived a priori: adjacent block centers of n_i/n_j distinct grid integers on disjoint contiguous supports separate by >= (n_i+n_j)/2) holds EXACT with 0/32547 violations; MED-CAP med_i <= (8/3) sep_i (the named missing half) holds 0/32728 with worst ratio EXACTLY 1.000 saturated AT the floor atom (chi4 kz53: gap 3/2, med 4 == (8/3)(3/2)) -- the pointwise chain g_i >= sep_i/med_i >= 3/8 closes on every atom, the constant 8/3 is tight, and min g over the round is EXACTLY the mesh rational 3/8 (only 5 sub-half atoms exist: 3/8 x2, 5/12, 5/11 x2; frame-B min 1/2); the SCRAMBLE floor contrast is measurable and SURVIVES arithmetic destruction (all three matched channels break at P1 admission nf 21/3/37 as sealed, but their partial builds carry gap floors 0.778/0.421/0.750, all >= 3/8, and all three scrambled worlds are STILL grid-quantized qdev <= 4.5e-13 -- the quantization and the floor are fold-machinery construction, not log p^k arithmetic).  T2' trivializes modulo MED-CAP (S_r == 0 for r >= 2 forced).  The continuous-t sieve census (t = j/32, bar t^2(1+log2(1/t))^2 == r358 pack_bar at dyadic t, warded exact) holds 0-violation on 181 rows x 16 t AND 1033 bands x 16 t with mean headroom 0.0014; steckbrief: the MV large-sieve spacing input IS SEP-SATZ, both open sieve parts reduce to MED-CAP as the single remaining lemma.  The direct composition M_3 <= (8/3)^2 C_K^2 (log m)^2/m^2 (C_G and two log powers drop) gives m_0* = 10^16.1 at the measured census ceiling C_K = 23.70 (vs r358 Carleson 10^23.5, 7.4 decades) and 10^10.0 rule-conditional at the per-family freeze 4.91 -- below the r306 census 10^13.5 IF the family-uniform T1 constant rule existed: that rule is now THE single remaining quantitative rest.  Disclosed epistemics: theorem-grade = the pointwise chain closes on the surface with a saturated, scramble-robust cap; the paper lemma MED-CAP is the one remaining formal step.  Anchors bit-near (r358 record full set); twin 1.0e-7; must-fails f1-f5 + m6a/m6b CAUGHT/FLAGGED.  Deterministic, record run1/run2 byte-identical up to WALL (761.3/774.2 s).  NO RH claim in either direction"

_R362_STATUS = "The augmented Borodin-Uvarov duality -- L-dagger as ONE dual object (round 362, the reviewer moonshot PRIME.LDAGGER.AUGMENTED_DUALITY.01; experiments-side, NO ledger row): 30/30 sealed; SPEC_SHA 7d810a9ab7db5c67 final with record, freeze 83b97cd57563e737, two-commit protocol pre-freeze 62ca2bfa / record b8adbf01; three disclosed calibration amendments a1/a2/a3 (chi equivalence retyped two-sided after the FIRST full evaluation found TERMINAL-DEAD chi rungs -- a finding, not a failure; chi border-Schur bar re-sized in the near-cancellation class; twin bar re-sized in the disclosed deepest-rung 1/margin twin-dose class; NO MAIN clause, bar or route moved, every MAIN gate passed at first evaluation).  MAIN VERDICT AUGMENTED_DUALITY_EXACT(route ii) + BORDER_IN_LOCAL_BLOCK: with beta = b/sqrt(B_w) the mu-orthonormal border ray (b_i = int phat_i dsigma, the smooth-comb border measure; B_w = S_{N-2} + 5/7 the r241/r243 budget), v = B_m beta its node-side CD image, gamma = beta.beta and D the r356 sign matrix, the bordered dual resolvent R-dagger := [[R^-1, Dv], [(Dv)^T, 1+gamma]]^-1 satisfies EXACTLY (Fractions toys + graded bars on 75 MAIN + 42 chi3 + 42 chi4 rows + kz133 deep): (A1) G-dagger = D-dagger (R-dagger^-1 - I) D-dagger -- the r356 Borodin complementation extends to the augmented node Gram; (A2) margin-dagger = 2 - 1/lambda_min(R-dagger) (spectral map, similarity-exact); (A3) L-dagger <=> R-dagger > I/2; (A4) the Y-block of R-dagger is a Sherman-Morrison rank-1 deformation of R (the border = a rank-1 Schlesinger/Uvarov insertion at the DUAL RESOLVENT level -- the v958 reading transported to the dual side); (A5) L-dagger <=> L* AND Terminal in dual coordinates with the frame-invariant q-dagger = gamma + v^T (I-E)^-1 v == u^T H^-1 u / B_w == the r266 crit1 coordinate, and the terminal dictionary 1 - q-dagger == (5/7)(1 - q_N)/B_w; (A6) the border-Schur closed form: Schur of R-dagger - I/2 onto the border coordinate == (1-q-dagger)/(2(1+q-dagger)) exactly, and by the Schur quotient the SAME value is carried inside the local 3x3 block (pair + border) -- the border fiber sits in the SAME local object, the moonshot clause made exact; (A7) interlacing lambda_k(R-dagger) <= lambda_k(R) <= lambda_{k+1}(R-dagger).  Measured: bind-dagger in [1.0003, 1.0608] med 1.0056 on the 74 resolvable MAIN rows (the augmented 3x3 block carries the full L-dagger margin AND the terminal fiber); the equivalence census exact and TWO-SIDED including six TERMINAL-DEAD chi rungs (chi3 [15,19,23,33,39], chi4 [20], q_N up to 1.33: lambda_min(R-dagger) - 1/2 goes negative EXACTLY as the theorem demands -- both truth directions live on real windows); kz15 compression mdag/margin = 0.8716 (the two lanes couple spectrally where the terminal channel is tight); share-dagger == the r359 cross share (0.6990 vs 0.6973 at w9, ladder med 0.708 vs 0.702) -- the rank-1 deformation does NOT move the critical resolvent structure at the pair: the r360 saturation lane can consume R-dagger verbatim, ONE critical saturation theorem for the bordered dual resolvent would close BOTH lanes.  Route adjudication honest: route (i) (literal virtual node) DEAD on real windows twice (representability spread 56.8; every border atom collides bitwise with a union grid node), surviving as the exact toy bridge (single-atom border: (S+1)-node Uvarov complementation Fractions-exact at the SHIFTED rank N, S-dagger = 2N -- the half-filling arithmetic moves by exactly one; the literal (S+1)-point dual kernel == route (ii) up to sign conjugation); RANK_SHIFT_MISMATCH correctly off.  Scramble breaks named two prongs (border cone EMPTY at chain flip n = 37 + algebra world-blind at fallback budget with the named R-block clause -0.4963); twin dose-zero bitwise, aug devs 1.2e-3 <= 2.5e-3.  Must-fails 6/6 (m1 budget factor exact 8.382399, m2 rank shift Fractions-exact, m3 AST margin-readback, m4 SM sign 4.9e-3, m5 collision ward, m6 wrong frame 0.769).  Honest: the equivalence is a REPRESENTATION -- L-dagger stays exactly as open as L* AND Terminal, no margin was created; EXT5 + 3 EXT6 rows sealed out of the augmented layer (budget, disclosed; kz133 deep census inside the f64 floor).  Deterministic, record run1/run2 byte-identical up to WALL (507.5/485.0 s).  NO L* claim, NO terminal claim, NO RH claim in either direction"

_R363_STATUS = "The internal full attack on R-dagger > I/2 -- two sharp internal angles, shared machinery, proof-first (round 363, PRIME.LSTAR.DUAL.INTERNAL_ATTACK.01; experiments-side, NO ledger row): 32/32 sealed; SPEC_SHA 09786c2e7b71c9a4 final with record, freeze fd7613339dfc18a0, two-commit protocol pre-freeze de7c55ec / record 4ee4543c; ZERO amendments after freeze (calibration pass 1 = first full evaluation = 32/32, 149.6 s; record run1/run2 byte-identical up to WALL 133.4/140.6 s).  MAIN VERDICT BOTH_PARTIAL(PINNING_REFUTED+EDGE_GAP_LEMMA_NAMED + TERMINAL_RANK_DEAD + STURM_CANONICAL_CENSUS(84/85 MAIN, chi MAY tip, scramble MUST tip) + COMPOSITION_TYPED + INTERNAL_LIMIT).  ANGLE A: BKMM Thm 2.3 node-pinning REFUTED at census grade on 74 resolvable MAIN rows (sat Hurwitz max 0.462 vs bar 0.15; bulk median 0.257; sat LARGER than bulk, not smaller; pin3 in (0.15, 0.55) on 74/74 -- Gauss-like pair-gap placement, O(1) not exponential, ratios do not shrink in N).  Canonical Sturm census 84/85 (miss kz133 = f64 floor, the r359 row); interpolated-zero interlacing 85/85; zero-count == degree 0-miss graded.  The remaining lemma is EDGE-GAP: why a zero of each consecutive dual OP occupies the unique pair-gap (y2, y1) -- classical Sturm/Markov gives interlacing and the count, not the placement.  The r360 zone {1,2,3} is DUAL-VOID (primal-sat), so dual-OP pinning if it applied would live in the BULK.  ANGLE B: exact CD update R_{n+1}=R_n+vv^T (Fractions rank-1 + trace 1 on the toy; w9 residual 3.3e-17); n_cross/N_w = 183/184, 140/142, 435/436, 877/878 on RANK_KZ -- TERMINAL-RANK (gap 1-2), so Loewner cannot start from a certified small-n head (r282 Toda warning, measured); window-ladder LC_EDGE2 36/71 violations, LC_UVEE 32/71 -- INDUCTION_GO does not fire.  COMPOSITION (74 resolvable): Schur split SATZ 74/74; Cauchy rest>=eps SATZ 74/74; detS>0 and rest>0 CENSUS 74/74; r362 A5/A7 gated at w9.  The hoped chain Sturm => det S_N > 0 => [c=1] R > I/2 has TWO measured gaps: Sturm does not give det S_N without P_N, W_N signs; c=1 does not give rest>0 (scramble: lamS +1.37e-2, rest -0.4962 -- the live counterexample).  Worlds: chi3 30/42 and chi4 29/42 keep the Sturm pattern (MAY tip -- consistent, not proof-load); chi w9 pin3 1.039/1.038 OUTSIDE the MAIN band; scramble straddle FAILS (n_mid 3, zeros_in_pair 2/2).  Twin dose-zero bitwise, |dlog| 6.9e-4, |dpin3| 6.0e-10.  Must-fails 5/5 (m1 Toda AST, m2 circular pinning AST, m3 bar-by-sight AST, m4 wrong OP indices, m5 c=1 misquote).  Anchors w9: pin3 0.293/0.310, sat_max 0.310, bulk 0.267, n_cross 183, lamRd 0.500041459, q-dagger 0.933044.  Honest: both internal angles need genuine new analysis (edge-gap placement as SATZ; rest positivity as SATZ; an induction with a loss term that actually holds) -- INTERNAL_LIMIT measured, the external RHP/BKMM path remains open as a documented option, not a freeze.  NO L* claim, NO R-dagger claim, NO RH claim in either direction"

_R367_STATUS = "The Haynsworth two-rank inertia cut -- G1 (edge-gap) and G2 (rest positivity) bypassed by evaluating the final two-rank transition directly (round 367, the Sol-pilot candidate PRIME.LSTAR.DUAL.FINAL_TWO_RANK_INERTIA.01; experiments-side, NO ledger row): 34/34 sealed; SPEC_SHA e0d79840fd7c9446 final with record, freeze 471879d1858e4c57, two-commit protocol pre-freeze c9ecbadd / record (this change); ONE disclosed calibration amendment a1 (G33/G34 retyped CENSUS after the FIRST full evaluation found P1_VACUOUS 29/74 -- A0 already PD at rank N-3 -- the Sol 4/4 RANK_KZ sample was terminal-rank biased; 0-violation stays in the GO letter; NO bar, P1/P2 definition, scramble named-break, Haynsworth SATZ or RESTATE_CORR moved; cal1 31/34 245.0 s, cal2 34/34 217.8 s).  THE THEOREM (finite algebra, Lean-shaped, Fractions LDL on the 4-node toy): A0 = R_{N-3}-I/2, U = [u_{N-3}, u_{N-2}] the two last dual OP columns via the r363 CD update, K2 = I_2 + U^T A0^{-1} U (AST: never from det R_{N-1}); P1 Inertia(A0)=(|Y|-1,1,0) AND P2 det K2<0 imply R_{N-1}-I/2 = A0+UU^T > 0 via Haynsworth additivity on the bordered matrix [[A0,U],[U^T,-I_2]] -- only the two premises contain arithmetic; implication one-way (sufficient not necessary).  MAIN VERDICT PREMISE_FAILS(P1_VACUOUS nneg=0 on 29/74 resolvable, P2 fails on the same set; OVERLOAD nneg>=2 is 0/74) + THREE_RANK_Y_CENSUS(K3mix 4/4, Ypd 4/4, one-shot full-R-dagger OFF) + A5_LIFT_LEDGER(4/4 RANK_KZ) + NEGDIR_LEDGER(REST-HOSTED 42/45 P1-true) + SOURCE_LEDGER(slope +0.543, corr_margin -0.0064, NOT restatement) + WORLD_LEDGER(chi MAY tip) + TWIN_LEDGER + SCRAMBLE_BREAK(named P1, P2 survives) + MUSTFAIL_LEDGER.  LEG A: toy SATZ (Inertia(A0)=(3,1,0), det K2=-7, M PD, additivity exact; swapped premises and wrong +I2 sign CAUGHT exact); Sol pilot bit-near at w9 sigma(K2)=(-2.7938, 1.8036) detK=-5.0389 nneg=1; live implication P1 AND P2 => M>0 on 74/74 resolvable; Lean form haynsworth_two_rank in the spec (not proved here).  LEG B: P1 exact-one 45/74, VACUOUS 29/74, OVERLOAD 0/74; P2 45/74 identical set; -det K2 on P2-true [1.157, 1126.389]; rest-hosted 42/45 (r359 pair-Schur already positive at rank N-3, G2-rest IS P1's remaining negative); scramble nneg=21 named P1 break, P2 survives detK=-8.881; twin |dlog(-det K2)|=1.4e-6; chi3 21/42 (w9 vacuous), chi4 19/42 (w9 holds).  LEG C: Theil-Sen +0.543 => SRC_FLAT not the margin rate -3.332; restatement corr -0.0064 << 0.999 -- NOT a restatement, -det K2 is a genuine 2x2 source object; TWO_RANK_INERTIA_GO and INERTIA_RESTATEMENT do not fire.  LEG D: A5 lift 4/4; three-rank Y-block K3 mixed 4/4 and Y-block PD 4/4 (two-rank + SM-PSD); one-shot full R-dagger from A0-dagger OFF (border is not a CD column); THREE_RANK_LDAGGER_GO stays off.  LEG E: must-fails 5/5 (m1 AST det-readback, m2 wrong sign exact, m3 wrong U, m4 wrong inertia tol protocol, m5 swapped premises exact).  Deterministic, record run1/run2 byte-identical up to WALL (236.0/228.9 s).  NO L* claim, NO R-dagger claim, NO RH claim in either direction"

_R368_STATUS = "The weighted L2-T1 -- the exact identity instead of the broken supremum (round 368, Sol rank 2, G4, PRIME.L2.T1_WEIGHTED_L2.01; experiments-side, NO ledger row): 20/20 sealed; SPEC_SHA 6d6da15ec8dd0cd7 final with record, freeze 4a89ec1051877c09, two-commit protocol pre-freeze e1521f94 / record b5a9a00f; ZERO amendments after freeze (calibration pass 1 = first full evaluation = 20/20, 708.8 s; record run1/run2 byte-identical up to WALL 674.0/631.4 s).  MAIN VERDICT WEIGHTED_L2_CENSUS+SPIKES_DOMINATE_PI -- the identity is SATZ, G4 is NOT replaced.  LEG A: M_3 == ((log m)^2/m^2) T_2 E_pi(F^2) with pi_i = (q_i/g_i^2)/T_2 closes EXACT (Fractions toy M_3 = 5/32; f64 worst rel 5.5e-16 on all 181 rows, bar 1e-12); T_2 E_pi == (m^2/(log m)^2) M_3 is TAUTOLOGICAL at the same 5.5e-16 -- T_2 is FACTORIZED, not absorbed.  LEG B: a-priori bars (C_F, B) = (1.0, 2.0) fail on 3/181, exactly the K2-spike rows (FRAME_A kz111 E_pi 52.276 vs bar 41.258; FRAME_B kz117 58.424 vs 42.09; FRAME_B kz124 75.691 vs 43.948); chi3/chi4 CLEAN (max 1.144/0.649, 0/42+0/42); C_F_cens = 1.722.  Depth slope POWER (tercile MAX-ratio of C_obs 16.414 vs bar 4.0; shallow max E_pi 1.165 vs deep 75.691).  Leave-family-out FAILS on FRAME_B (C_fit 1.267, viol 2/8 at kz117/kz124) and CARRIES on A/chi3/chi4 -- family-uniformity answered DIRECTLY and negatively.  Spike anatomy MIXED: kz111 IS pi-light (share 0.337, g_i* 1.333) -- the Sol thesis holds there; kz117 DOMINATES (share 0.909, max F 23.70) -- the weighted mean IS the spike, the retyping is useless on that row; named bit fires.  LEG C: m_0* = 10^29.8 (C_G 0.100 x C_F_cens 1.722, A+B=4) WORSE than r358 Carleson 10^23.5 and r361 floor 10^16.1/10^10.0; floor-T2 10^19.7.  Cofinal rest unchanged: MED-CAP as a lemma (V2) + a family-uniform T1/E_pi THEOREM.  LEG D: scrambles P1_ADMISSION x3 (nf 21/3/37) with measurable E_pi on partial builds 2.440/11.807/3.620; twin 1.6e-07; must-fails e1 exact (25/64 != 5/32), e2/e3/e4 protocol-CAUGHT twice, m6a/m6b FLAGGED.  Anchors bit-near (r358 T1 2.45/4.91/1.52/1.62 vs 15.93/23.70/3.91/3.09, C_G 0.100, min g 0.375, stress 0.533/0.571).  NO RH claim in either direction"

_R369_STATUS = "The mixed low-rank form of M-dagger plus generalized Haynsworth -- reviewer sequence step 1, algebra only (round 369, PRIME.LDAGGER.MIXED_HAYNSWORTH.01; experiments-side, NO ledger row): 20/20 sealed; SPEC_SHA 138d09978ff79556 final with record, freeze 5a4a20db973700ba, two-commit protocol pre-freeze 6ae366a2 / record 6072921f; ZERO amendments after freeze (calibration pass 1 = first full evaluation = 20/20, 29.2 s; record run1/run2 byte-identical up to WALL 29.2/28.9 s).  MAIN VERDICT MIXED_UPDATE_EXACT + HAYNSWORTH_MIXED_SATZ + PHI_LEDGER + JSIG_CENSUS + MUSTFAIL_LEDGER.  THE DERIVATION (explicit, not fitted): R-dagger = blkdiag(R, 0) + (1/den)[s;-1][s;-1]^T (r362 A4) and R = R_{N-3} + u1 u1^T + u2 u2^T (r363), so M-dagger = blkdiag(A0, -1/2) + U J U^T with U the two last dual CD columns plus the SM vector (s,-1) and J = diag(1, 1, 1/den) from the Sherman-Morrison denominator.  Signature twin J_sig = diag(1, 1, sign(den)) after scaling column 3.  THE r367 WARNING IS RESOLVED AS A FORM: the border is not a third unaugmented CD column, but on the R-dagger level Sherman-Morrison DOES supply a third column with explicit J; NO_LOWRANK_BOUNDARY_FORM does not fire.  LEG A: Fractions toy residual EXACT 0 (den = 23/30); live residual <= 1.04e-14 on the 10-row algebra sample (9, 15, 18, 20, 42, 44, 52, 56, 119, 130; bar 1e-10) + w9 1.9e-15 + kz15 1.9e-15 (near-terminal, q_N 0.9376) + chi3-w9 1.3e-15.  LEG B: generalized Haynsworth SATZ for arbitrary invertible symmetric J -- Fractions 4-node toy with INDEFINITE J = diag(1,1,-1): In(H)=(4,3,0) == In(A)+In(-Phi) == In(-J^{-1})+In(M) EXACT; Lean form haynsworth_mixed in the spec (not proved here; R373); r367 haynsworth_two_rank is the J = I_2 special case.  LEG C: Phi_N(0) = J^{-1} + U^T A^{-1} U; w9 sigma = (-2.8132, -0.06648, 1.8039) det 0.3374 -- the two LARGE eigenvalues TRACK r367 K2 (-2.7938, 1.8036), the small extra negative IS the border direction; signature balance In(A)+In(-Phi)==In(-J^{-1})+In(M-dagger) on 10/10 + chi3-w9; dichotomy P1-true 8/10 In(A) nneg=2 (A0 + pad) and In(Phi) nneg=2, VACUOUS kz42/kz130 2/10 In(A) nneg=1 (pad only) -- the r367 P1_VACUOUS class in the 3x3 picture; chi3-w9 additionally In(Phi) nneg=1; OVERLOAD 0/10.  LEG D: must-fails 4/4 (m1 J=I_3 fitted-scale residual 0.375 + AST, m2 wrong sign 1.249 + Fractions exact, m3 two-rank Y-only 2.467e-3 + the OTHER r367 balance, m4 AST lamRd readback).  JSIG HONEST: empirical J_sig = I_3 on 10/10 live sample rows (den in [1.460, 1.646], all positive); the mixed SIGNATURE of J is the FORM plus the synthetic den<0 branch (G12, den = -17.326), not a Lorentz J on MAIN; the mixed-NESS of the update on the family is A indefinite + Phi mixed.  Algebra sample only (no 85-row ladder; existing records are the anchors).  NO L* claim, NO R-dagger claim, NO RH claim in either direction"

_R370_STATUS = "The matrix-valued Weyl phase index -- reviewer sequence step 2 after the r369 stop, the main test of the new central architecture (round 370, PRIME.LDAGGER.MATRIX_WEYL_INDEX.01; experiments-side, NO ledger row): 31/31 sealed; SPEC_SHA b12b5fc38301767b final with record, freeze f6e1a704fcaf838b, two-commit protocol pre-freeze e44af3cd / record (this change); ONE disclosed instrument amendment a1 (cal1 killed on EXT6 Nw~8000 mixed+eigh, ~16 min in, 81/85 already PD; census Xi := nneg Phi(0), EXT6 dropped from the Weyl ladder, G30 still verifies the sealed selection; NO bar, kill-test, scramble named-break, dictionary named-break or verdict letter moved; cal2 = first complete full evaluation 31/31, 716.4 s; record run1/run2 byte-identical up to WALL 707.9/704.3 s).  MAIN VERDICT NO_JACOBI_LINEARIZATION(named: border Cauchy r_n is not a homogeneous dual solution, residual 3.615e-02 at w9 / 0.354 toy; A0 is a dense CD Gram on Y not a node-Jacobi; r359 IIKS does not z-lift to A0, rel 1.003) + PHASE_RESTATEMENT(real-line Xi = nneg Phi(0); Haynsworth already equates positivity control with M-dagger PD -- the Wronskian route that would replace hBal by an oriented Casoratian count does not close; the 2x2 (p, q) Casoratian exists and is source-pure but does not factor det Phi) + PHI_MONOTONE_SATZ + PHASE_CENSUS + MUSTFAIL_LEDGER.  CANONICAL_PHASE_CARRIER does NOT fire (70-pct resource trigger stays off).  LEG A: Phi_N(z) = J^{-1}+U^T(A-z)^{-1}U is the block resolvent (A0-eigh + pad); Fractions matrix-det lemma at z=-2 det Phi = 2293/150 exact (TARGET char poly -- SATZ skeleton, not the source dictionary); Phi' succeq 0 exact on the toy; live min eig Phi' = 8.949e-09 on 18/18 admissible Z_GRID nodes (2 skipped near poles); w9 Phi(0) sigma = (-2.8132, -0.06648, 1.8039) det 0.3374, LARGE pair TRACKS r367 K2; mixed residual 1.9e-15; den = 1.601114.  LEG B: the 3x3 dictionary FAILS at a named place -- dual p and dual-measure Cauchy q satisfy the three-term recurrence (p-rec 0, q-rec 1.2e-14, 2x2 Casoratian drift 3.1e-12); border r_n residual 3.615e-02 NOT a homogeneous dual solution, so there is no 3x3 Jacobi Casoratian of (p, q, r); node-basis IIKS for (A0)^{-1} with the two CD columns rel 1.003; C_N > 0 is therefore not constructed.  LEG C: census Xi := nneg Phi(0); MAIN 81 rows (a1 EXT6 dropped) resolvable 74/74 want_pd, Xi==nnegPhi, ctrl iff PD, balance (bar 74+); printed 81/81 PD, Xi dichotomy 49 (Xi=2) / 32 (Xi=1); twin WORLD_KZ |dXi|=0, |dlog det Phi|=3.8e-06 nats; chi3-w9 VACUOUS POSITIVE (nnegA0=0, nnegPhi=1, q_N=0.247); six terminal-dead classified NEGATIVE (chi3 5/5, chi4 1/1, built 42/42) via want_pd False / ctrl False / q_N>1 -- Xi follows nnegPhi and is 0 on kz23/33/20, 1 on kz15/19/39 (not a magic Xi value); scramble seed 1 named-breaks at nnegA0=21 AND border nf=37 (ok_mix False); oriented anatomy at w9: 2 nneg-jumps, each interval contains a pole of A (pad -1/2 and A0's negative) -- phase turns at A's poles, not at named Y-nodes; shadow corr(Xi, log|margin|)=+0.2013.  LEG D: kill-test 7 two layers -- a source-free PD target M=I_5+UU^T is AUTO-RECOGNIZED by Haynsworth (restatement of M PD); the Wronskian dictionary is UNDEFINED there, so the source-specific index SATZ does not fire.  LEG E: must-fails 4/4 (kernel-Green AST, wrong Green residual 14100 vs (A0)^{-1}, z-grid-by-sight AST, lamRd/margin/detM readbacks AST).  NO L* claim, NO R-dagger claim, NO RH claim in either direction"

_R371_STATUS = "The exterior-square kill test of the canonical CD two-form -- reviewer solution 3, ONE run (round 371, PRIME.LSTAR.DUAL.COMPOUND_CD.01; experiments-side, NO ledger row): 30/30 sealed; SPEC_SHA 3b5b3c887d515ffd final with record, freeze 85b31ee99180bf64 / file SHA c7860a863ef19983, two-commit protocol pre-freeze ac7c0b0b / record 13af4c78; ONE disclosed instrument amendment a1 (G35 second raw 1e-8 floor disagreed with r367 Rayleigh inertia on 10/45 P1 near-zeros -- product formula nneg(wedge2)=nneg*npos from the SAME inertia now the constructor; SHARE_BAR, sign definition, MAJ construction, scramble named-break, identity bars and GO letters NOT moved; first full evaluation 28/30 266.4 s; record run1/run2 byte-identical up to WALL 283.3/239.3 s).  MAIN VERDICT SIGNATURE_PARTIAL(wterm<0 45/45, share>=0.50 27/45) + CAPTURE_HOLDS_CENSUS(nneg-1 45/45 via identity (12) == P2) + OVERLOAD_CENSUS_ONLY(cert_lt2 0/45, scramble MAJ>2) + AND2_LEDGER + WORLD_LEDGER + TWIN_LEDGER + SCRAMBLE_BREAK + MUSTFAIL_LEDGER.  LEG A: identities SATZ -- (12) Fractions toy det K2=-7=1+q11+q22+wterm exact (wterm=-4); f64 graded 74/74 maxerr 5.7e-10, live 1e-10 on 72/74 (kz37/kz95 at 5.7e-10/5.0e-10 sit in mid grade 1e-9); (13) Fractions CD-telescope exact, live dressing 74/74 maxerr 9.1e-17, c_N=1/b_{N-3} in (1.92, 2.06) all positive; wrong wedge2 convention lambda_i+lambda_j CAUGHT exact.  LEG B (the kill test): the canonical wedge SIGN is STABLE on the nneg-1 branch (wterm<0 45/45, range [-637.7, -1.32], 0 flips) -- NOT the r318 coin-flip of original-matrix minors; capture (14) holds 45/45 by algebra (not independent arithmetic); the wedge2-subspace share is NOT stable (majority 27/45, min 0.001, med 0.601, max 0.905 -- the Sol 4/4 sample 0.67..0.78 was terminal-rank biased); COMPOUND_SIGNATURE_STABLE does not fire; nneg(wedge2 A0)=|Y|-1 on 45/45 (product formula, a1); r367 dichotomy reproduced P1 45 / vacuous 29 / overload 0 on 74 resolvable.  LEG C: Gershgorin-Stieltjes MAJ=n_hit on the branch [67, 1425] >> 2, isolation 0/45, cert_lt2 0/45 -- the construction does NOT certify ind_-<2; occupation diagonal of A0 is n_diagneg=0 on the whole nneg-1 branch (min diag>0, the remaining negative is off-diagonal); scramble MAJ=49>2 (vacuity test holds) and n_diagneg=24; OVERLOAD_MAJORANT_GO stays off; nneg<=1 remains the r367 census.  LEG D: twin |d wterm|=6.2e-5 bitwise dose-zero; chi3 21/42 nneg-1 all wterm<0 (w9 PD world-separating); chi4 19/42 nneg-1 all wterm<0; scramble named P1 nneg=21, P2 survives, wterm=-3.022 measured.  Must-fails 5/5.  Honesty: the canonical two-form has a STABLE SOURCE SIGN and an UNSTABLE wedge2-subspace share; capture is algebra; the overload theorem stays census.  NO L* claim, NO RH claim in either direction"

_R372_STATUS = "The source-Jacobi Pruefer one-defect test -- V2 and T1 jointly, the spike extracted not averaged (round 372, reviewer solution 2 / Terminal, PRIME.TERMINAL.SOURCE_PRUFER_ONE_DEFECT.01; experiments-side, NO ledger row): 27/27 sealed; SPEC_SHA 778403f6c5f898e9 final with record, freeze ad13a2abd3dca0f2 / file SHA d998f309ddb44900e2e76e5390663ee1b7eb146b3d59452133394efb4ce1a99f, two-commit protocol pre-freeze 279c0f92 / record (this change); ONE disclosed instrument amendment a1 (twin_rational arity copied from the r368 channel -- first full evaluation crashed at G91 before any adjudication; NO bar, letter, turning rule, C_STAR, C_REST, uniqueness definition or verdict tree moved; cal2 = first complete full evaluation 27/27, 616.4 s; record run1/run2 byte-identical up to WALL 747.9/644.3 s).  MAIN VERDICT SPIKE_NOT_UNIQUE.  LEG A: the Pruefer-to-run dictionary is SATZ -- floor(theta/pi) runs of the chain-accumulated Jacobi Pruefer phase equal the sign-runs of v2 on ALL 181 live rows (89+8+42+42); XOR identity sign(ct)=sign(w x v2) 181/181; Fractions toy (2,2,2,2) exact; N2>=N3 181/181; interior chain progress min 2.062 (circular mutant is 0 -- not a restatement of the sign field); Jacobi positivity gam_next>0 through deg N-2 on 181/181 (L* certified on this surface).  LEG B: the one-defect thesis is REFUTED at census grade -- NOT_UNIQUE 181/181, MAIN unique 0/97, max n_turn 310 (w9 already 12/6/9/7); the sealed slope-outlier rule (SLOPE_RATIO 2.0, SLOPE_MIN 0.50, MERGE_GAP 4) sees the zero-crossing jumps of a step-like discrete Pruefer phase, not a unique turning block; SPIKE_NOT_UNIQUE is the letter, the bar was not moved after sight.  Spike coincidence FAILS on kz111/117/124: canonical i*=0 (left edge) vs argmax-q 168/140/111; q* of that diagnostic group 4.3e-3 / 5.1e-3 / 4.9e-4, not the r368 mass spikes -- THE SAME RULE does not carry the three named rows.  LEG C: two-part bound after dominant-cluster extraction does NOT replace T1 -- rest-T1 F_i a-priori (1.0, 2.0) has 0/181 violations only because (log m)^2 is large on deep rows while F_rest still equals the global max 23.704 (the spike was not extracted); rest-M3 violates 24/181 (max 94.893 vs C_REST 1.0); q*-score of the wrong group is vacuously below C_STAR.  V2 holds 181/181 with 0 phase-pattern violators, but V2-from-phase is NO: uniqueness failed, so the regularity that would exclude (...,r,r,1,1,1) is not the one-turning theorem; bulk monotone at MONO_FRAC 0.90 only 23/181 (min frac 0.854).  LEG D: composition does not pay -- m0* = 10^24.9 (measured C*_obs 0.898 + C_rest_obs 94.893, A=2) WORSE than r361 floor 10^16.1 / 10^10.0; cofinal rest unchanged: V2 as a lemma + a family-uniform T1 theorem; the one-defect extraction is not that theorem.  LEG E: scrambles P1_ADMISSION x3 (nf 21/3/37, n_turn 7/40/3); twin 1.8e-08; must-fails e1-e5 + m6a/m6b.  Cofinal typing: dictionary + XOR + V2-combinatorics are SATZ (modulo L* positivity for the phase to be well-defined); uniqueness, coincidence, rest-T1, q*, m0* are CENSUS.  NO L* claim, NO RH claim in either direction"

_R377_STATUS = (
    "Post-cap pivots of the signed source -- P2 as alternation, "
    "P1 as a single prefix defect (round 377, LEMMA.POSTCAP_PIVOTS.01; "
    "lemma-first, experiments-side census, NO ledger row): 18/18 full / "
    "9/9 smoke; SPEC_SHA b7167c3756c9b7a6; census first measured in /tmp "
    "then sealed as frozen tallies (disclosed calibration, not a "
    "two-commit pre-blind freeze).  GOAL A (P2-POSTCAP h_N h_{N+1}<0 on "
    "every canonical window) REFUTED: 35/85 MAIN LATE/NONE, explicit kz12 "
    "first_neg=N+2 detK=+12.4632 nnegA=0 Mpd.  Dictionary SATZ (Fractions "
    "toy detK=-196/35719 both routes; live (detK<0)==(sN*sNp1<0) on pins).  "
    "nneg-1 branch alternation CENSUS 50/50 MAIN (PINNED_N 19 + PINNED_Np1 "
    "31).  Aliasing P_X and T_{S+k}=(-1)^j T_k SATZ; sign of h_N h_{N+1} "
    "still an H_N^{-1} readback (kill).  GOAL B (ind_- H_{N+2}<=1) CENSUS "
    "85/85 MAIN + 84/84 chi, scramble named-break first=21 nneg=37; Sturm "
    "uniqueness not proved.  Frozen MAIN classes PINNED_N 19 / PINNED_Np1 "
    "31 / LATE 23 / NONE 12 / DOUBLE 0 / EARLY 0 / MULTI 0; P2 50/85; "
    "P1 85/85; free 85/85.  CHI3 P2 21/42; CHI4 P2 19/42.  NONE hunt "
    "offsets {4,5,8}.  Dead chi still P1.  Companion "
    "rh/problem/postcap_pivots.tex + verify_postcap_steps.py 16/16 "
    "POSTCAP STEPS VERIFIED.  NO L* claim, NO RH claim"
)

_R381_STATUS = (
    "G_eps lemma from the source (round 381, LEMMA.G_EPS.01, "
    "lemma-first; experiments-side, NO ledger row): 17/17 full / "
    "14/14 smoke; SPEC_SHA 60ce9bc28fc7f171; identities first "
    "measured in /tmp then sealed (disclosed calibration).  "
    "AUSGANG REDUZIERT to the pair (C_eps, R2).  SATZ: first-order "
    "Jacobi d gamma_k / d w_j = (p_k(x_j)^2 - gamma_k p_{k-1}(x_j)^2) "
    "/ h_{k-1} (Fractions toy |CD-FO|/|FO|=2.092e-4 at eps=1/200; "
    "FRAME-A w9 FO vs FD rel 5.446e-4).  Jacobi-(0,1) and cosine-grid "
    "mesh remain r379 SATZ.  L^inf of Fejer-stripped d_arm is O(1) "
    "(w9 ||eps_mu||_inf=5.166) -- crude FO majorant ~3 >> 1/16; "
    "cancellation is essential.  Jump half is NOT implied by the box "
    "(log(5/3)=0.5108 > 2/5).  Lambda(n)<=log n PNT-free (trial "
    "division n=2..120).  Second-order midpoint remainder along "
    "Fejer-ref -> actual at n=40: |quad|/|lin|_last12=1.013 "
    "(NOT dominated).  FRAME-A w9 G_eps holds (signed last-12 "
    "0.03417 jump 0.2493); mu-only last-12 0.02605 jump 0.1224; "
    "mass_nu/mu=0.0611.  SCRAMBLE seed=1 named-breaks last-12 "
    "|g-1/4|=6.841 (lag |c_q| is NOT the separator).  Slow-then-fast "
    "block is a STEP obstruction, not an FO-formula fail.  Companion "
    "rh/problem/g_eps_lemma.tex + verify_g_eps.py 13/13 "
    "G_EPS LEMMA VERIFIED.  NO L* claim, NO RH claim"
)

_R382_STATUS = (
    "Pivot-band entry lemma (round 382, LEMMA.PIVOT_ENTRY.01, "
    "lemma-first; experiments-side, NO ledger row): 17/17 full / "
    "10/10 smoke; SPEC_SHA b7f53a93daf790bc; identities and flank "
    "tallies first measured in /tmp then sealed (disclosed "
    "calibration).  AUSGANG REDUZIERT to n0=floor(2N/5) under "
    "the (2/3)-flank condition.  SATZ: RKHS sum bound; pair-energy "
    "identity; Christoffel comparison h_k(w) >= (1-lam) h_k(mu); "
    "5-atom 2-vs-1 interlacing (h0,h1,h2>0, h3=-144/7); 3-atom "
    "flank ratio 1/3 with h0=4,h1=6,h2=-3; equal two-period H1=0; "
    "clustered run-of-3 H3<0 before half-filling.  CENSUS: MAIN "
    "F1 (max_len<=2) 85/85, F2 (rmax<1) 85/85, F2_23 (rmax<=2/3) "
    "78/85 (EXT-heavy 69,96,97,99,107,117,129); core-42 nh67=0 "
    "max d50=0.0402; dead chi 6/6 satisfy F1+F2_23.  KILL: "
    "scramble max_len=5 rmax=2.71 first_neg=21 < n0=73 and "
    "lam(E_22)>1; two-period c=1 first_neg=0; clustered run-6 "
    "first_neg=2.  Two-period c=2/3 first_neg ~ N/2 (S=81: 20 "
    "vs n0=16) is the binding adversary against raising kappa "
    "to 1.  Named remainder for n0=N-1: L2 CD-kernel tail on "
    "flank blocks (r285 coherence).  Companion "
    "rh/problem/pivot_entry_lemma.tex + verify_pivot_entry.py "
    "14/14 PIVOT ENTRY STEPS VERIFIED.  NO L* claim, NO RH claim"
)

_R383_STATUS = (
    "Compose premises (R)(L)(Z) (round 383, LEMMA.COMPOSE.PREMISES.01, "
    "lemma-first; experiments-side, NO ledger row): 20/20 full / "
    "12/12 smoke; SPEC_SHA 146b0b45ad872d7e; constants first "
    "measured in /tmp then sealed (disclosed calibration, WALL "
    "622.3 s).  SATZ: Fejer identity + bilinear CS; r298 split "
    "S_F=B(omega,omega)+B(Delta,omega+beta); Z=Zloc+t_bulk "
    "(Lean canonical_split; NOT sum Pd); L2 identity "
    "M3=((log m)^2/m^2) T2 E_pi(F^2); Lambda(n)<=log n by trial "
    "division; pref<=sqrt(m)+1; T1-floor algebra under g_i>=3/8.  "
    "(R) REDUCED: R0=4 on 181/181 (sup 2.916788 at FRAME-A kz37; "
    "mutant R0/2=2 fails 17/181 and DC toy R=3.6875); cofinal "
    "ratio open; trivial envelope H_max=29 too coarse.  Fold "
    "pairing as a live SATZ REFUTED (pair_w med 0.512); MAIN "
    "empty is CENSUS (med MAIN/S_F=0.0086), not a pairing "
    "theorem.  (L) REDUCED: Lambda=3 on 181/181 (max 2.126195 "
    "at FRAME-B kz124); von Mangoldt triangle slope +0.307 on "
    "A does NOT prove gamma<1/4; measured L1 slope +0.202 on "
    "the 42 is not a theorem.  T1-combo does NOT carry as a "
    "theorem (kz111 E_pi=52.276, kz117 E_pi=75.691; identity "
    "SATZ, T2<=1.329<(8/3)^2).  (Z) REDUCED on FRAME-A "
    "(Z0=4/5, 89/89, max 0.755675 at kz16) and FRAME-B 8/8 "
    "and the 42-rung ladder 42/42; REFUTED family-uniform on "
    "chi (CHI3 {15,19,23,33,39}, CHI4 {20}; 175/181 |Zloc|<M).  "
    "Finite-head Chebyshev REFUTED (n_edge 167..4689).  KILL: "
    "scramble seed=1 named-breaks (L) on the T1/M3 polylog "
    "(M3=2.288e-2 > r306 1.374e-2) without breaking R0 or "
    "Lambda; gamma=1/4 fails T1-vs-phi algebra.  Companion "
    "rh/problem/compose_premises.tex + verify_compose_premises.py "
    "16/16 COMPOSE PREMISES VERIFIED.  NO L* claim, NO RH claim"
)

_R385_STATUS = (
    "Christoffel quietness (round 385, LEMMA.CHRISTOFFEL_QUIET.01, "
    "lemma-first; experiments-side, NO ledger row): 19/19 full / "
    "13/13 smoke; SPEC_SHA 03bde46ec27d98ff; identities, discrepancy, "
    "Q-profiles, FO=gamma dQ, scramble k_Q>=1, two-period lambda vs Q, "
    "and core-42 / MAIN-85 / chi3-42 tallies first measured in /tmp "
    "(r385_cal.py, r385_cal2.py, r385_cal3.py) then sealed (disclosed "
    "calibration).  AUSGANG REDUZIERT.  SATZ: T_k^2=(1+T_{2k})/2; "
    "TV(cos 2k theta)=4k; Chebyshev-Gauss Q_k==1 on the equal-weight "
    "cosine grid; FO_k[-nu]=gamma_k (Q_k-Q_{k-1}); one-Rayleigh "
    "h_k(1-Q_k).  Chebyshev sampling of nu stays at mass ratio alpha "
    "under the TRIVIAL Weyl bound (|S_m|<=mass(nu) already gives "
    "Q^T<=2 alpha ~0.12<1).  The deduction 'therefore mu-OP Q_k<=qbar "
    "from 3/8-floor + Koksma' is false: w9 last-12 Q=0.389 vs "
    "alpha=0.061, deformation 0.335, k D*=33.4 does not close; "
    "|Q-alpha|/(k D*)=0.0089=o(k D*) but the error still grows.  "
    "Weyl |S_{2k}|/mass in (0.04,0.33) -- TRIVIAL, not PNT, not "
    "subconvex, not RH-equivalent (the Chebyshev-Weyl route never "
    "reaches a zeta-quality demand).  CENSUS: core-42 Qmax in "
    "[0.164,0.483]<1 (n_fail=0); 11 small-N last-12 |FO| max="
    "0.01182<1/32; MAIN-85 D* in [0.105,0.212]; chi3-42 D* in "
    "[0.125,0.248] (181-pack builder skipped as too expensive, "
    "disclosed).  KILL: scramble seed=1 Q crosses 1 at k=70 "
    "(last-12 4.8e6); two-period c=2/3 Q==0.683<1 AND "
    "lambda_max(E_22)>1 -- Q<1 is NOT the floor plate; c=1 kills "
    "at h_0 (Q0=1.025).  EXT-heavy 7 at depth 200 Qmax in "
    "[0.127,0.221]<0.25 (leisheit holds; r_max up to 0.879 is a "
    "flank-mass fact).  Remaining: Fejer/d_arm deformation "
    "Delta_k=Q_k-Q_k^T (live C_eps term) and coherence assist "
    "(r382 L2 remainder).  Companion rh/problem/christoffel_quiet.tex "
    "+ verify_christoffel_quiet.py 13/13 CHRISTOFFEL QUIET VERIFIED.  "
    "NO L* claim, NO RH claim"
)

_R386_STATUS = (
    "Living-ladder (Z') and cofinal R0 (round 386, "
    "LEMMA.COMPOSE.PREMISES2.01, lemma-first; experiments-side, "
    "NO ledger row): 20/20 full / 12/12 smoke; SPEC_SHA "
    "82d07e568591c9fd; constants first measured in /tmp "
    "(tfpt_r386_cal.py, WALL 628.2 s) then sealed (disclosed "
    "calibration).  TWO LETTERS.  (Z') REDUCED: Z0'=21/25=0.84 "
    "on the living ladder 175/175 (FRAME-A 89 + FRAME-B 8 + "
    "chi with q_N<1); living sup |Z_loc|=0.833870 at CHI4 kz46 "
    "(exceeds r383 Z0=4/5; mutant 4/5 FAILS).  Death channel "
    "|Z_loc|>=M iff |Z|>=M iff q_N>1 is a biconditional CENSUS "
    "181/181; the six dead chi are exactly CHI3 {15,19,23,33,39} "
    "and CHI4 {20} (terminal-dead sprouts, q_N in [1.040,1.330]).  "
    "SATZ: death triangle; Fejer CS; w9 dictionary "
    "q_N=rho_{N-1}/(5/7)=(7/5)Z^2.  Finite-head Chebyshev "
    "REFUTED (n_edge 167..4689; triangle 2.86..14.51 grows).  "
    "Uniform-cancel * triangle REFUTED (cancel_max*tri_max="
    "4.08>M); cancellation is essential (med 0.055) not a SATZ.  "
    "(R) REDUCED: R0=4 census (sup 2.916788 at kz37); MAIN/D <= "
    "3/10 on 181/181 (max 0.129976, slope -1.16 CENSUS); CS SATZ "
    "181/181 tight at kz37; CS+FAB does NOT prove O(polylog) "
    "(FAB_max 18.07>14.93, FAB controls Pd not Pw).  Named "
    "remainder B(omega+beta,omega+beta)<=K D (R-star Bsum/D="
    "2.975<4).  KILL: DC toy MAIN/D=3.6875 breaks field-"
    "independent C_MAIN; mutant Z0=4/5 fails living CHI4-46; "
    "scramble does NOT break (Z') or R0.  Companion "
    "rh/problem/compose_premises2.tex + "
    "verify_compose_premises2.py 16/16 COMPOSE PREMISES2 "
    "VERIFIED.  NO L* claim, NO RH claim"
)


_R387_STATUS = (
    "Coherence assist (round 387, LEMMA.COHERENCE_ASSIST.01, "
    "lemma-first; experiments-side, NO ledger row): 20/20 full / "
    "14/14 smoke; SPEC_SHA 6005359e0bafadb2; identities, w9 walk, "
    "two-period/scramble/cluster, core-42 AP-fraction and k_gersh, "
    "EXT-heavy angle stats and Dirichlet max-rows first measured "
    "in /tmp (r387_cal.py, r387_cal2.py) then sealed (disclosed "
    "calibration).  AUSGANG REDUZIERT.  SATZ: Chebyshev-T CD = "
    "[D_{k-1}(th-ph)+D_{k-1}(th+ph)]/(2pi); bookkeeping lambda = "
    "maxdiag*(1+assist) exact (2x2 equality lam=3 assist=1/2); "
    "Gershgorin/Schur majorant; cosine mesh Delta=pi/S; F1 "
    "run-of-2 => dmin = 1 mesh; two-period = global AP "
    "(rho_AP=1).  The deduction 'therefore assist <= (1-Q)/Q from "
    "3/8-separation + Gershgorin' is false: w9 k_gersh=21 << "
    "n0=73 << N-1=183 (k*/N=0.109); core-42 k_gersh in [8,32] "
    "all < n0, k_g/N max=0.114 < 2/5; dmin/dmed = 1/3 < 3/8 "
    "(3/8-floor does not upgrade nu-angle gaps).  Wall w9 k=183: "
    "lam=0.999830 maxdiag=0.9614 assist=0.0399 (r285 range; r385 "
    "'assist 1.54' mixed Q_k~0.39 with maxdiag(E)); Gershgorin "
    "assist 13.32, cancellation 0.997.  Named property rho_AP = "
    "L_AP/n_nu < 1/5 kills the two-period (rho_AP=1, Dirichlet "
    "max-row k=22 = 0.858 vs source 0.291) and HOLDS on EXT-heavy "
    "7 (rho_AP <= 0.033, lam_80 < 1, sharpest 0.9965 at kz97); "
    "core-42 rho_AP in [0.034, 0.168], cv > 1/2; mutant bar "
    "0.03 FAILS.  KILL: two-period c=2/3 Q==0.683 AND lam22>1; "
    "c=1 lam1=1.025; clustered run-3 k_lam=15 < n0=16 rho_AP=1; "
    "run-2 k_lam=21 > n0 (F1 allows); scramble seed=1 rho_AP=0.064 "
    "HOLDS, dies on product (k_lam=22, k_maxd=50).  Remaining: "
    "SIGNED mu-CD off-diagonal (true assist; unsigned/Gershgorin "
    "closed as too crude).  n0=floor(2N/5) NOT improved; "
    "n0=N-1 open with that remainder.  Companion "
    "rh/problem/coherence_assist.tex + "
    "verify_coherence_assist.py 13/13 COHERENCE ASSIST VERIFIED.  "
    "NO L* claim, NO RH claim"
)

_R388_STATUS = (
    "Delta-deformation (round 388, LEMMA.DELTA_DEFORMATION.01, "
    "lemma-first; experiments-side, NO ledger row): 19/19 full / "
    "12/12 smoke; SPEC_SHA 5613d035ac6bc11d; identities, w9 "
    "Delta/FO/eps, R2 mu-path and Fejer-path midpoint ratios, "
    "scramble osc vs dDelta, two-period eps=0, and core-42 / "
    "MAIN-85 / chi3-42 tallies first measured in /tmp "
    "(r388_cal.py, r388_cal2.py) then sealed (disclosed "
    "calibration).  AUSGANG REDUZIERT.  SATZ: FO=gamma "
    "(dQ^T + dDelta); monic gamma homogeneous in total mass; "
    "Fejer-pure two-period eps=0 implies FO=0.  Osc-Geronimus "
    "|dDelta|<=C osc(eps on nu) holds on MAIN with C*=0.0056 "
    "and does NOT close C_eps (majorant g(dQT+C* osc) reaches "
    "0.191>1/32, closes 5/42; C x 2 already overshoots on w9 "
    "maj=0.0327).  Consecutive Q is uncorrelated with "
    "||eps||_inf (corr=0.025) and with osc_nu (corr=-0.287).  "
    "R2 on the mu-reference is NOT dominated: n=40 "
    "|quad|/|lin|=0.8615 (Fejer-path 1.0127 reproduced); full "
    "n=182 ratio 0.6403; |R2|/|FO| last-12=4.19; small-N n=40 "
    "ratios in [0.559,1.126] all > 1/4.  CENSUS: 11 small-N "
    "last-12 |FO| MAIN 0.01182 and chi3 0.01541 both <1/32 "
    "(181-pack skipped).  KILL: scramble seed=1 osc_nu=3.54 "
    "< MAIN 8.76 but dDelta=2.16e6 (C_emp=6.1e5).  Two-period "
    "S=81 c=2/3 is the control (eps=0, FO=0).  Remaining: "
    "C_eps as cancelled last-12 pairing (not an eps-size "
    "bound); R2 of the finite mu->mu-nu step; G_eps^mu as the "
    "Jacobi box of Fejer x d_arm (r342 dictionary v_pred<1e-4 "
    "is the right language for the sibling).  Companion "
    "rh/problem/delta_deformation.tex + "
    "verify_delta_deformation.py 13/13 DELTA DEFORMATION "
    "VERIFIED.  NO L* claim, NO RH claim"
)


_R389_STATUS = (
    "Weyl energy of cancellation (round 389, LEMMA.WEYL_ENERGY.01, "
    "lemma-first; experiments-side, NO ledger row): 27/27 full / "
    "19/19 smoke; SPEC_SHA c93fdc413980bf4a; identities, w9 "
    "energy/Parseval/spectrum/FO, scramble and two-period spectra, "
    "core-42 / EXT-heavy / chi3-42 tallies first measured in /tmp "
    "(tfpt_r389_cal.py, WALL 2.1 s) then sealed (disclosed "
    "calibration).  AUSGANG REDUZIERT.  SATZ: Chebyshev energy "
    "Phi=(1/pi)C0^2+(2/pi)Sigma_{m<k} C_m^2; off=Phi-diag with "
    "explicit v^2 Weyl diagonal; Q^T=(C0+C_{2k})_nu/(C0+C_{2k})_mu; "
    "pi_k^2 Weyl via Chebyshev coeffs; finite-grid Parseval "
    "Sigma_{q<2S} |S_q|^2 = 2S Sigma v^2 ratio=1 (S=21 and w9).  "
    "MAIN/chi at quadratic-mean (core-42 mean/qm in [0.661,1.018]; "
    "|C|/mass max <0.41 trivial Weyl, not PNT; HHI <0.12).  "
    "Two-period S=81 is a comb (|C_S|/mass=1, HHI=0.727) -- "
    "rho_AP=1 iff spectral concentration on a progression.  "
    "FO^T last-12=0.00496 and small-N max 0.01650 both <1/32: the "
    "Chebyshev piece of C_eps CLOSES at quadratic-mean; dDelta is "
    "the live remainder.  Assist is NOT the Chebyshev all-ones "
    "energy (1^T E^T 1 / n_nu=0.114 vs lam=0.99983; wall v otimes v "
    "off negative).  Z_loc Chebyshev proxy cancel=0.47 != r386 "
    "median 0.055.  von Mangoldt mean/qm=0.718 > equal 0.403 "
    "(weights do NOT buy cosine cancellation).  KILL: mutant c_q=1 "
    "rel=0.108; missing diag |Phi-off|/|off|=2.78; scramble holds "
    "QM (mean/qm=0.947, HHI=0.007) and diverges at m=380,354,30 "
    "(dies on the mu-OP remainder, not nu-Weyl).  Remaining: "
    "Weyl energy of the mu-OP Chebyshev-coefficient Gram -- of "
    "phi* (assist), of consecutive alpha_k (dDelta / C_eps), of "
    "the edge-masked drive (Z_loc).  Companion "
    "rh/problem/weyl_energy.tex + verify_weyl_energy.py 14/14 "
    "WEYL ENERGY VERIFIED.  NO L* claim, NO RH claim"
)

_R390_STATUS = (
    "G_eps^mu, the sibling lemma of the positive mu-chain "
    "(round 390, LEMMA.G_EPS_MU.01, lemma-first; experiments-side, "
    "NO ledger row): 24/24 full / 18/18 smoke; SPEC_SHA "
    "c2c9c3f2d1eacd5e; Jacobi-(0,1), Chebyshev-U quarters, "
    "w9 mu/Fejer-occupied/signed-Fejer last-12, full-grid "
    "Bernstein-Szego residual, kappa, perm 20 seeds, two-period "
    "weight, and the core-42 census first measured in /tmp "
    "(r390_cal.py, r390_cal2.py, r390_cal3.py) then sealed "
    "(disclosed calibration).  Builder fallback: core-42 only "
    "(MAIN-85 aborted >2 min on EXT).  AUSGANG REDUZIERT.  SATZ: "
    "Jacobi-(0,1) g=n(n+1)/(2n+1)^2 over Q; Chebyshev-U "
    "p2=x^2-1/4 so gamma_k=1/4; monic gamma homogeneous; "
    "full-grid Fejer is Bernstein-Szego discrete "
    "(max|g-1/4|_{k>=2}=1.836e-6 at w9, union=S++S-).  "
    "Occupied-Fejer ALREADY IN |g-1/4| (w9 0.03596; core-42 max "
    "0.04892) -- the r381 0.071 was SIGNED Fejer.  Jump of "
    "occupied-Fejer is razor-thin (max 0.3942 vs 2/5, margin "
    "0.0058).  d_arm pulls IN on 40/42 and is load-bearing for "
    "JUMP headroom (mu maxd=0.03304 maxj=0.2469).  Ratio bound "
    "kappa=4200.6 is true-and-useless.  NOT construction-pure: "
    "perm of the same weights on the same nodes kills 17/20 "
    "(seed 3: 0.07445/0.4590).  scramble_seed=1 mu-only OUT "
    "(occupation moves).  Two-period weight a=0.95 stays IN.  "
    "No m4 (smallest core n=140 IN).  Remaining: F_eps "
    "(Fejer-on-occupied = node deletion from Bernstein-Szego) "
    "AND W_eps (r342 digamma/tent multiplier vs scramble-of-"
    "weights).  Companion rh/problem/g_eps_mu.tex + "
    "verify_g_eps_mu.py 13/13 G_EPS_MU LEMMA VERIFIED.  "
    "NO L* claim, NO RH claim"
)

_R391_STATUS = (
    "Construction-pure (R) and (L) (round 391, "
    "LEMMA.CONSTRUCTION_PURE.RL.01, lemma-first; experiments-side, "
    "NO ledger row): 23/23 full / 15/15 smoke; SPEC_SHA "
    "6699da51c8546495; toys, w9/kz37/scramble pins, weight-rand "
    "and geometry mutants, CORE-42 + CHI3-42 census first "
    "measured in /tmp (tfpt_r391_cal.py, tfpt_r391_cal2.py, "
    "tfpt_r391_cal3.py) then sealed (disclosed calibration).  "
    "Builder fallback: CORE-42 + CHI3-42 (181-pack and FRAME-B 8 "
    "exceeded 2 min, skipped).  TWO LETTERS.  SATZ: Euclidean "
    "split ||Sigma||^2+||Delta||^2 = 2(||Pb||^2+||Pw||^2) and "
    "nrmS/D=(1+eta)/(1-eta); CS counting L1^2 <= m D; Fejer "
    "Gram; DC Rayleigh 3.6875; atom Gershgorin of K is lambda<=H "
    "(too coarse).  (R) REDUCED: K=4 construction-class "
    "(CORE-42 max Bsum/D=2.8196 at kz19, 0/42 >4, 9/42 >2 so "
    "K/2 FAILS; CHI3-42 max 2.746 at kz67; R-star kz37 "
    "2.975<4); independent weight-rand at frozen geometry HOLDS "
    "(permute/gauss/rademacher/expon/dirichlet max 2.44 on w9); "
    "positive alignment Pw=a Pb with a=0.3 BREAKS and a->+1 is "
    "unbounded -- no field-independent K.  Superblock "
    "Gershgorin REFUTED as SATZ (fully-DD only 4/42, min "
    "dd_frac=0.667).  Geometry kill is DC-flatten / sign-kill "
    "(w9 5.67 / 6.13), NOT merged folds (merge_pairs 1.21).  "
    "White-block class: nrmS/D med=0.999, cos med=-0.0006, "
    "ray max=3.099.  (L) REDUCED: CORE-42 L1 slope +0.2017 "
    "<1/4 (matches r383 +0.202); CHI3 +0.182; CS-gamma 0.214 "
    "<1/4 is the D-decay translation (tautological with "
    "n_eff~m / r301 n_act==m); triangle +0.307 still does not "
    "close; DC L1=m is the geometry kill of field-independent "
    "gamma<1/4.  (C) COMPOSE- still needs (Z') + M3<=phi + Dict "
    "+ the two census envelopes; r389 Weyl energy owns the "
    "SIGNED objects (assist, C_eps, Z_loc), not (R)(L).  "
    "Scramble does NOT break (R) or (L).  Companion "
    "rh/problem/construction_rl.tex + "
    "verify_construction_rl.py 17/17 CONSTRUCTION PURE RL "
    "VERIFIED.  NO L* claim, NO RH claim"
)

_R392_STATUS = (
    "Deletion transform (round 392, LEMMA.DELETION_TRANSFORM.01, "
    "lemma-first; experiments-side, NO ledger row): 22/22 full / "
    "19/19 smoke; SPEC_SHA e4d6ced026e12433; Uvarov gamma-ratio "
    "over Q, S=5/7/9 deletions, w9 formula identity, Assist/"
    "dDelta readouts, AP vs clustered vs scramble, and the "
    "core-42 census first measured in /tmp (r392_cal.py .. "
    "r392_cal5.py) then sealed (disclosed calibration).  "
    "Builder fallback: core-42 only.  AUSGANG REDUZIERT.  SATZ: "
    "gamma_n(mu)=gamma_n(sigma)*tau_{n+1} tau_{n-1}/tau_n^2 with "
    "tau_n=det(I-K_n[Xi] W), tau_0=1 (Hankel det lemma); block = "
    "iterated over Q (5-atom 5/48,8/75,5/81 and 8/45,4/15); "
    "Bernstein-Szego specialises to (1/4)*tau-ratio up to the "
    "r390 residual 1.85e-6.  w9 formula vs occupied-Fejer "
    "maxerr=8.993e-15.  Assist Uvarov(mu+nu) lam=0.999830 "
    "assist=0.0399 canc=0.9970 (r387 reproduced); dDelta12="
    "0.04946 Dmax=0.3347 (r388 reproduced).  Occupied-Fejer "
    "kernel does NOT carry Assist (lam=10.12).  NOT proved: "
    "F_eps from rho_AP<1/5 -- AP every-2 stays at gamma=1/4; "
    "clustered run=3 kills (j=0.462); scramble seed=3 jump="
    "0.4438 OUT; kz55 jump 0.3942 margin 0.0058 is census.  "
    "Cancellation of Assist sits in the SIGNS of K^mu[Xi], not "
    "the positive tau-quotients of gamma.  Remaining: bound "
    "d2 log tau under F1-bounded nu-runs (F_eps rest); "
    "Sign-Schur of K^mu[Xi] (Assist rest).  V3' allows relaxing "
    "JUMP (A_15 fails at scale 2.0) -- not moved.  Companion "
    "rh/problem/deletion_transform.tex + "
    "verify_deletion_transform.py 14/14 DELETION TRANSFORM "
    "VERIFIED.  NO L* claim, NO RH claim"
)

_R393_STATUS = (
    "Tau field under F1 (round 393, LEMMA.TAU_FIELD.01, "
    "lemma-first; experiments-side, NO ledger row): 26/26 full / "
    "20/20 smoke; SPEC_SHA c3f6b3b94caa78d0; 1x1/2x2 tau over Q, "
    "cluster decomp identity, rank-1 locality, w9 F1 census "
    "(102 clusters), coupling share, AP / run-3 / center-pair / "
    "scramble F1, random-F1 counterexample, and the core-42 "
    "census first measured in /tmp (r393_cal.py .. r393_cal7.py) "
    "then sealed (disclosed calibration).  Builder fallback: "
    "core-42 only.  AUSGANG REDUZIERT.  SATZ: F1 splits Xi into "
    "singletons and pairs; tau_cluster is 1x1 SM / 2x2 det; "
    "d2 log tau = sum_c d2 log tau_c + d2 log kappa (w9 maxerr "
    "0); rho_n = tau_{n+1}/tau_n = 1-(W pi)^T (I-KW)^{-1} pi so "
    "d2 = Delta log rho (volume does not enter linearly).  w9 "
    "last-12 |d2|=0.1553 |e^{d2}-1|=0.1438 coupling 0.049 "
    "(~31%, load-bearing); L1(clusters)=0.436 > log(5/4)=0.223 "
    "(triangle FAILS).  F1 is NECESSARY (run-3 j=0.4619 OUT at "
    "2/5 and JUMP'=0.45) and NOT SUFFICIENT (random F1 half-fill "
    "h=80 j=1.179 OUT; isolated center pair j=0.4183 OUT at 2/5 "
    "IN at 0.45).  Scramble seed=3 is an F1/cluster break "
    "(max_len=6, j=0.4438).  Core-42 0/42 OUT at 2/5, maxj="
    "0.3942 (kz55) is census even after legal JUMP'=0.45 "
    "(V3' A_15 air; A_15 first fails at scale 2.0).  Remaining: "
    "L*-occupation regularity (the gap between F1-legal cosine "
    "masks and folded half-filling), sibling to Sign-Schur.  "
    "Companion rh/problem/tau_field.tex + "
    "verify_tau_field.py 13/13 TAU FIELD VERIFIED.  "
    "NO L* claim, NO RH claim"
)

_R394_STATUS = (
    "Sign-Schur of the Uvarov image (round 394, LEMMA.SIGN_SCHUR.01, "
    "lemma-first; experiments-side, NO ledger row): 24/24 full / "
    "19/19 smoke; SPEC_SHA f77a50fee61dd4c5; Dirichlet sign and "
    "envelope identities, 2x2 Z-matrix counterexample, w9 Chebyshev/"
    "checkerboard mass-agreements, |E| mutant, two-period in-phase "
    "and too-late anti-checkerboard, scramble seed=1 envelope, and "
    "the core-42 census first measured in /tmp (r394_cal.py, "
    "r394_cal2.py, r394_cal3.py) then sealed (disclosed "
    "calibration).  Builder fallback: core-42 only (1.1 s).  "
    "AUSGANG REDUZIERT.  SATZ: Chebyshev-CD signs on the cosine "
    "grid are Dirichlet-zonal; |D_n(a)| <= min(2n+1, 1/|sin(a/2)|); "
    "[[1,-c],[-c,1]] has lambda=1+c > maxdiag so the hoped "
    "M-matrix bound is FALSE even with perfect conjugacy.  "
    "REFUTED: checkerboard / rank-1 conjugability as the Assist "
    "mechanism (w9 CB ww=0.504; core-42 CB ww in [0.429, 0.512]).  "
    "CENSUS: mass-weighted Chebyshev-sign inheritance w9 ww=0.810 "
    "(pair-count uw=0.721); last-12 ww in [0.801, 0.829]; core-42 "
    "ww in [0.810, 0.894]; 42/42 lam<1.  NOT proved: source-defined "
    "conjugacy => lambda_max<1 to any k*>2N/5 (oracle bound_pos="
    "1.90>1 at the wall; entry k=73 NN neg_share=0.039 "
    "constructive).  KILL: two-period k=22 NN 40/0 in-phase "
    "lam=1.0288>1; k=40 -CB agree=1 too late (maxd=1.317); "
    "scramble seed=1 Cheb ww=0.788 HOLDS, lam=9.17e6 (envelope/"
    "occupation); mutant |E| lam=1.683>1 (gA=13.32 sign-blind).  "
    "Remaining: Dirichlet/Abel (Weyl) energy of the mu-OP Gram "
    "(r389 rest) -- Sign-Schur as a bipartition is the wrong "
    "language.  Companion rh/problem/sign_schur.tex + "
    "verify_sign_schur.py 14/14 SIGN SCHUR VERIFIED.  "
    "NO L* claim, NO RH claim"
)

_R395_STATUS = (
    "Three-gap of the fold mask (round 395, LEMMA.THREE_GAP_MASK.01, "
    "lemma-first; experiments-side, NO ledger row): 29/29 full / "
    "21/21 smoke; SPEC_SHA 4f246d22f6f0abe2; Steinhaus on Z/q "
    "(309/309 Farey+Fibonacci), additive a+b=c, thinning kill, "
    "PNT-free integer-log local 3-gap n0>=512, small-n drift "
    "census, w9/core-42/chi/EXT-kz97 gap spectra, wrapping 3-gap "
    "vs {n alpha} vs random-F1 discriminator, Assist lambda split, "
    "scramble/two-period/dyadic-cut kills first measured in /tmp "
    "(r395_cal.py .. r395_cal4.py) then sealed (disclosed "
    "calibration).  Builder fallback: core-42 + EXT kz97 + chi "
    "sample (MAIN-85 and EXT S>5000 skipped).  AUSGANG REFUTED.  "
    "SATZ: Steinhaus nuniq<=3 on Z/q; integer-log local 3-gap for "
    "n>=512 M<=64 (PNT-free, f'' of log); small n0<=64 is a "
    "census (nuniq 8..19).  REFUTED: the nu-mask is globally or "
    "blockwise 3-gap (w9 nuniq=12, core-42 in [8,18] 0/42 <=5, "
    "EXT nuniq grows to 13 at kz97 / 25 at kz69); nuniq<=3 + F1 "
    "+ rho_AP<1/5 implies the d2 log tau box (wrap(1,2,3) j=2.33 "
    "OUT; mechanical phi d=0.1016 OUT on the box; wrap(2,3,4) "
    "isolated-singles 8/8 IN at h=80 is a different class).  "
    "3/8-floor and MED-CAP 8/3 are NOT shadows of the cosine-grid "
    "gap spectrum (dmin/dmed=1/3<3/8, dmax/dmin=23>8/3).  KILL: "
    "two-period lam22=1.0288>1 (rho_AP=1); random F1 j=1.179 "
    "(many gaps); scramble seed=3 slide12<=3 = 0; dyadic-cut "
    "shift moves block nuniq.  Assist at n0: randF1 lam=2.01, "
    "wrap234 lam=0.997, 1010 lam=1.405 -- separates sparse "
    "3-gap from random F1, does not identify the source "
    "(2-3-dominated histogram + sparse tail).  Remaining: that "
    "histogram, strictly smaller than three-gap, still the "
    "occupation object of both F_eps and Assist.  Companion "
    "rh/problem/three_gap_mask.tex + "
    "verify_three_gap_mask.py 11/11 THREE GAP MASK VERIFIED.  "
    "NO L* claim, NO RH claim"
)

_R396_STATUS = (
    "Isolation of the fold mask (round 396, LEMMA.ISOLATION.01, "
    "lemma-first; experiments-side, NO ledger row): 29/29 full / "
    "22/22 smoke; SPEC_SHA eb6dca0e0d28d1d3; pair census w9/core-42/"
    "chi/EXT-kz97, PNT-free folded-small-integer non-adjacency, "
    "atom-fold packing, wrap(2,3,4) nref-60 vs nref-h discriminator, "
    "pair injection, fat-tail, Assist/Gershgorin, scramble/two-period/"
    "pair-counter/denser-isolated kills first measured in /tmp "
    "(r396_cal.py, r396_cal2.py) then sealed (disclosed "
    "calibration).  Builder fallback: core-42 + EXT kz97 + chi "
    "sample (MAIN-85 and EXT S>5000 skipped).  AUSGANG REFUTED.  "
    "SATZ: folded consecutive n=2..64 are not adjacent on L=734 "
    "(PNT-free, log monotone); wrap(2,3,4) is isolated; pair counts "
    "on named windows are machine identities; Dirichlet envelope at "
    "sep 2 is still >>1 (12.59 on S=79).  REFUTED: P(N)/n_nu -> 0 "
    "or P <= constant (w9=2, core [0,16] med 4 zero 3/42, kz97=22, "
    "dens O(0.03) stable); pairs are small-n log collisions (atom "
    "n~211 near the cap lands on a pair bin); isolated + thin tail "
    "=> d2 log tau box (h=40 wrap234 3/12 IN; h=80 nref=60 8/8 is "
    "a truncation, nref=80 2/8; denser wrap223 0/8; fat tail HELPS "
    "6/8); isolated => lambda<1 (1010 lam=1.405); isolation + hull "
    "=> Gershgorin<1 (gersh=1.768 gA=6.10); singleton 1x1 chain is "
    "a SATZ of the box (the isolated class does not sit in the box "
    "at natural depth).  KILL: wrap(1,2,3) dens=0.222 j=2.327 OUT; "
    "randF1 dens=0.417 j=7.032 OUT; two-period lam22=1.0288>1; "
    "scramble dens=0.431; pair-counter mutant gap-2=44 vs gap-1=2; "
    "inject k=1 already 0/8 IN.  Core 42/42 IN at JUMP with "
    "corr(pairs,j)=-0.38 (pair count does not drive the source "
    "jump).  Remaining: the r395 2-3 histogram with a sparse tail "
    "-- pair density ~2% is a SHADOW of that shape, not a closing "
    "lemma.  Companion rh/problem/isolation_lemma.tex + "
    "verify_isolation_lemma.py 10/10 ISOLATION LEMMA VERIFIED.  "
    "NO L* claim, NO RH claim"
)

_R398_STATUS = (
    "High-moment inertia kill-test of P1 (round 398, "
    "PRIME.LDAGGER.HIGH_MOMENT_INERTIA.01, reviewer-preregistered "
    "before the source-Weyl campaign; experiments-side, NO ledger "
    "row): 30/30 full / 21/21 smoke; SPEC_SHA bb1dcf6ab66a6156; "
    "moments, near-1/2 counts, scramble nneg=21, two-period, Twin, "
    "living/dead chi first measured in /tmp (r398_cal.py, "
    "r398_cal2.py) then sealed (disclosed calibration).  Builder "
    "fallback NOT taken: full census wall 5.6 s (bar 120 s) on "
    "core-42 + MAIN-85 sample + chi3/chi4-42 + Twin.  AUSGANG "
    "KILL_FAIL.  SATZ: pointwise 1_{r<1/2} <= [2(1-r)]^{2d} "
    "(Fractions r=2/5 d=2: 1296/625); cycle-sum tr(A^k) = closed "
    "walks (2x2 tr(A^2)=35/72 exact; 3x3 k=4 walk-sum dev 6.9e-18); "
    "0 ⪯ R_{N-3} ⪯ I on the named census; traces via even "
    "powers agree with spectral sums (w9 |M-M_ev|=3.6e-14).  "
    "REFUTED as a route: a FIXED d in {2,3,4,6,8} with "
    "2^{2d} tr((I-R_{N-3})^{2d}) < 2 and growing reserve.  FRAME-A "
    "w9: nneg=1 rmin=0.46153 M_d=(33.48, 26.79, 22.75, 18.23, "
    "16.03) ALL >= 2; near-1/2 counts (5, 24, 37) for "
    "delta=0.01/0.05/0.1; 36 eigs in [1/2, 3/5]; FTI residual 0.  "
    "Core-42: 42/42 contractions, nneg in {0,1}, M2 in "
    "[33.22, 224.5], Nmin=142 M2=34.86 -> Nmax=878 M2=224.5 "
    "(reserve SHRINKS).  MAIN-85 sample continues the growth "
    "(kz119 M2=287.9; EXT kz69 N=5690 M2=1079).  Twin kz 9/18/52 "
    "|d M2| <= 2e-5, nneg identical.  Living chi3 37/37 M2 in "
    "[28.03, 183.4]; living chi4 41/41 M2 in [26.90, 178.7]; all "
    ">= 2.  Dead chi3 5/5 M2 in [35.98, 63.55]; dead chi4-20 "
    "M2=33.75 -- control holds, test NOT a world separator (living "
    "also >= 2).  need_d: NONE on nneg=1 (w9 min at d=11 still "
    "15.06 then diverges; kz18 min M5=28.66 then M30=1.5e5); on "
    "nneg=0 bulk-only d~512..1024 growing with 1/gap (forbidden).  "
    "KILL: scramble nneg=21 M2=148 M8=2.65e5 explodes; two-period "
    "S=21 nneg=4 rmin=0 M2=52; nopref mutant 81/625 < 1; odd "
    "power on R=diag(2/5,2) sum < 0.  Cycle-sum is NOT the R399 "
    "target.  Companion rh/problem/high_moment_inertia.tex + "
    "verify_high_moment.py 12/12 HIGH MOMENT VERIFIED.  "
    "NO L* claim, NO R-dagger claim, NO RH claim"
)

_R399_STATUS = (
    "Source-pure Weyl energy of the centered mass difference "
    "(round 399, PRIME.SOURCE.WEYL_ENERGY.THEOREM.01, reviewer "
    "5.2/5.3 after DCCLXII and the r398 KILL_FAIL; "
    "experiments-side, NO ledger row): 29/29 full / 22/22 smoke; "
    "SPEC_SHA c5a74fda2d455a52; identities, w9/kz18/kz52 "
    "Dirichlet, CD energies, selected a_k=2^k, core-42 slopes, "
    "assist correlation, scramble / two-period / chi, MVT ratios "
    "first measured in /tmp (r399_cal.py, r399_cal2.py) then "
    "sealed (disclosed calibration).  Builder fallback NOT taken: "
    "full census wall 1.5 s (bar 120 s).  AUSGANG REFUTED (decay "
    "E^bulk -> 0 at the CD-transfer norm).  SATZ: tent interpolant "
    "dP[j] = -Sum Lambda(n) n^{-1/2} K_j(log n) (w9 maxdev "
    "2.5e-13, kz18 2.0e-13, kz52 3.9e-12); Fejer Laplacian "
    "IFFT(Fejer odot dP) = Delta cP_ext / L (Q-exact 6-cycle, "
    "w9 8.7e-19); C_0=C_1=0; cap outside CD band so E^bulk = E; "
    "transfer omega from r389 Chebyshev-CD at depth N_w-3.  "
    "REFUTED as decay: core-42 E in [1.178, 5.983] slope "
    "dlogE/dlog N_w = +0.542; mean C^2/qm in [0.427, 0.848] "
    "(quadratic-mean); selected a_k=2^k k=3..9 E = 0.033..0.869 "
    "not monotone to 0.  Honesty gate: Montgomery-Vaughan MVT "
    "crude/E = 3139 (w9) .. 4.2e5 (N_w=878); the needed "
    "sub-QM exponent is RH-near, hence circular as a route to "
    "R^dagger > 1/2 I, and is contradicted by the census.  "
    "Bridge corr(E/N_w, assist)=0.18 (named norm, not a closing "
    "majorant).  KILL: scramble E=3.39 > 1.2 x MAIN (centered d "
    "SEES log-n cancellation; r389 nu-QM did not); two-period "
    "HHI=0.629 comb at m=S; mutant omega=1 is a scale; drop-edge "
    "vacuous (already zero); dead chi3-15 E=1.69 and living "
    "chi3-9 E=1.47 both O(1).  Prime-power lag ratio 0.23, "
    "series absolutely convergent.  Companion "
    "rh/problem/source_weyl_energy.tex + verify_source_weyl.py "
    "11/11 SOURCE WEYL VERIFIED.  "
    "NO L* claim, NO R-dagger claim, NO RH claim"
)


_R400_STATUS = (
    "Bulk one-defect threshold/phase form of the frame "
    "inequality (round 400, PRIME.LDAGGER.BULK_ONE_DEFECT.01, "
    "reviewer 5.4 after the r399 circularity verdict and in "
    "parallel with r401; experiments-side, NO ledger row): "
    "27/27 full / 22/22 smoke; SPEC_SHA 91a4afa27f249fbb; "
    "reference inertia, lift rank, cluster r_eff, vneg-dcent "
    "cosine, phase table, scramble punch-through, dead/living "
    "chi nneg, core-42 lam2-gap first measured in /tmp "
    "(r400_cal.py, r400_cal2.py, r400_cal3.py) then sealed "
    "(disclosed calibration).  Builder fallback NOT taken: "
    "full census wall 5.5 s (bar 120 s) on core-42 + "
    "chi3/chi4-42 + Twin.  AUSGANG FORM_T REFUTED (rank-1) / "
    "FORM_P REFUTED.  SATZ: frame implication A+C ell ell^T "
    "succeq c I => ind_- <= 1 (Fractions A=diag(-1,2) C=2); "
    "rank-r interlacing (diag(-1,-1)+e0 e0^T kills one, never "
    "two); Weyl nneg(A+B)<=nneg(A)+nneg(B).  REFUTED as rank-1: "
    "the r390 Bernstein-Szego dual on Y has nneg_ref=49; MAIN "
    "kills 48 (need rank>=48 by interlacing); lift on the "
    "reference-negative space r_eff=9.55 lead=0.105 numerical "
    "rank=49; whole-B spectral-free r_eff=14.91.  Occupied-I "
    "(tiny nu floor) is DEGENERATE (depth N-3>|Y| saturates "
    "R^ref=I, disclosed, not the r390 object).  Source ell = "
    "dcent on Y is orthogonal to v_neg (cosine 0.0075); frame "
    "fails for every C in the scan; pair mass 0.151 rest-hosted "
    "(r367).  Core-42 42/42 nneg in {0,1} (28 P1 + 14 vacuous), "
    "gap2=lam2-1/2 in [4.3e-8, 2.0e-4] (razor, not MVT-scale).  "
    "FORM_P: consecutive C_m signs do NOT track ind_- (MAIN "
    "rho1=-0.341 nneg=1 vs scramble -0.363 nneg=21; E 1.81 vs "
    "3.39 factor <2).  Gate: sub-band MVT is unconditional but "
    "does not see P1 (dcent orthogonal to v_neg; low-band energy "
    "already ~0).  KILL: scramble nneg=21 killed only 14 of 35, "
    "rmin=0.0036 punches through 1/2; two-period nneg=4 killed=0; "
    "threshold x2 (lam2>=1) FALSE; omit-ell hypothesis fails.  "
    "Dead chi3 5/5 and chi4-20 nneg in {0,1}; living chi3 37/37 "
    "and chi4 41/41 nneg<=1 -- P1 is NOT world-separating; dead "
    "chi die at sch>0 (r401), not at the bulk.  Twin-9 nneg/ncl "
    "bit-identical.  Companion rh/problem/bulk_one_defect.tex + "
    "verify_bulk_one_defect.py 12/12 BULK ONE DEFECT VERIFIED.  "
    "NO L* claim, NO R-dagger claim, NO RH claim"
)

_R401_STATUS = (
    "Augmented 3x3 edge signature (round 401, "
    "PRIME.LDAGGER.EDGE_SIGNATURE.01, reviewer 5.5 after DCCLXII, "
    "parallel to r399; experiments-side, NO ledger row): 33/33 full / "
    "23/23 smoke; SPEC_SHA 395673f2b0b1cee5; mixed 3x3, shift, sch "
    "sign, (a,b), r375 pair, isotropic E, scramble nf, two-period "
    "nnegA0, Twin, chi live/dead first measured in /tmp (r401_cal.py, "
    "r401_cal2.py, r401_cal3.py) then sealed (disclosed calibration).  "
    "Builder fallback NOT taken: full wall 41.7 s (bar 120 s) on "
    "core-42 + chi3/4-42 + EXT-6 (kz69 N=5690 mixed-invert dropped, "
    "disclosed; compactness already at N=3022).  AUSGANG "
    "EDGE_SIGNATURE_MODEL.  SATZ: mixed form (Fractions den=23/30); "
    "Haynsworth additivity; reconstruction D^T Phi D = Phi_edge(a,b) "
    "identically (||E||=2.22e-15 at w9, max 4.4e-14 on P1); model "
    "lemma ind_-(Phi_edge)=2 on the P1 chart and =1 on the vacuous "
    "chart (Haynsworth on the explicit 3x3; det=+/-1); 64-pt disk "
    "R=3.2 nneg=2 gmin=0.082.  CENSUS: shift ind_-(Phi)=1+ind_-(A0) "
    "42/42 MAIN (28 P1 Phi=2, 14 vac Phi=1), living chi3 37/37, "
    "living chi4 41/41, EXT-6, Twin |d tau|~1e-7; J>0 den in "
    "[1.46, 1.63]; tau=(a,b) |tau| max 3.144 on P1, EXT smaller "
    "(0.075 at N=1119); r375 (xi,eta) compact trend-free but "
    "Spearman(|tau|, xi)=0.12 -- not the 3x3 moduli; isotropic "
    "reconstruction ||E||/g=80.7 at w9 (candidate i KILL as model); "
    "QMAX Spearman 0.26 (candidate ii KILL).  TWO-SIDED: dead chi3 "
    "5/5 sch>0 shift FAILS; dead chi4-20 Phi=0 sch=+0.023.  KILL: "
    "scramble nnegA0=21 border nf=37; two-period nnegA0=4; drop-border "
    "shift by 0; wrong-sign J residual 867/115.  Cofinal K NOT proved.  "
    "Companion rh/problem/edge_signature.tex + "
    "verify_edge_signature.py 13/13 EDGE SIGNATURE VERIFIED.  "
    "NO L* claim, NO R-dagger claim, NO RH claim"
)

_R403_STATUS = (
    "P1 construction class (round 403, "
    "PRIME.LDAGGER.P1_CONSTRUCTION.01, lemma-first after DCCLXVII "
    "and r400: is lam2(R_{N-3})>=1/2 a theorem of the fold mask "
    "with arbitrary sign-conforming weights?; experiments-side, "
    "NO ledger row): 25/25 full / 21/21 smoke; SPEC_SHA "
    "ba6817f54dc2b654; class nneg tables, mild-noise break, Gram "
    "rest, omit/only-Gram, scale residual, sample killed, chi-perm "
    "first measured in /tmp (r403_cal.py, r403_cal2.py, "
    "r403_cal3.py) then sealed (disclosed calibration).  Builder "
    "fallback NOT taken: full wall 0.7 s (bar 120 s).  AUSGANG "
    "P1_CONSTRUCTION_REFUTED.  SATZ: rank-1 interlacing "
    "(diag(-1,-1)+e0 e0^T kills one); PSD+ND need not lift "
    "(diag(-1,-1)+0.1 I still nneg=2); R(c w)=R(w) "
    "(||R-R(7w)||_F=3.0e-13).  REFUTED as a construction class: "
    "fixed-mask permute nneg in {20,21,21,22}; gauss {18..24}; "
    "expon {11..15}; dirichlet {11..18}; rademacher-flatten "
    "nneg=2; mild 1e-4 already 1/6 nneg>1.  mu*3 nneg=0, nu*3 "
    "nneg=65 (relative scale is load-bearing).  Separating "
    "invariant is the weight-to-position assignment, not the "
    "sign mask.  48=49-1 is MAIN tautology "
    "(nneg_ref=49,48,54,124,141 on the sample; perm leaves tens "
    "of negatives).  n_half(R^ref) grows 13,27,38,62,65 -- not "
    "a single exact 1/2 mode.  Gram candidate CENSUS on MAIN: "
    "B|_neg PSD rest=0 49/49, omit-Gram nneg=49, only-Gram "
    "nneg=13 (cross terms finish the lift); permute/scramble "
    "rest=0.14/0.15 -- Gram is MAIN-weight, not class.  KILL: "
    "scramble nneg=21; two-period nneg=4 killed=0; signflip "
    "nneg~90; dead chi3-15 nneg=1 on true weights, perm nneg=20.  "
    "Sample {9,22,33,78,82} MAIN nneg=1, perm 24/30/44/96/102; "
    "EXT kz82 n=341.  Companion rh/problem/p1_construction.tex + "
    "verify_p1_construction.py 11/11 P1 CONSTRUCTION VERIFIED.  "
    "NO L* claim, NO R-dagger claim, NO RH claim"
)

_R404_STATUS = (
    "Source one-defect Gram (round 404, "
    "PRIME.LDAGGER.SOURCE_ONE_DEFECT_GRAM.01, reviewer DCCLXIX "
    "after r403: is Q^T A0 Q = F F^T - ell ell^T source-explicit "
    "from Lambda(p^r), log(p^r), Fold, Tent, Digamma, explicit "
    "BS modes, one null mode?; experiments-side, NO ledger row): "
    "21/21 full / 19/19 smoke; SPEC_SHA c0260053d759bd14; "
    "Loewner nsum, Euler alignment, analytic principal angles, "
    "defect seat, mutant residuals first measured in /tmp "
    "(r404_cal.py, r404_cal2.py, r404_cal3.py) then sealed "
    "(disclosed calibration).  Builder fallback NOT taken: "
    "full wall 0.2 s (bar 120 s).  AUSGANG CHOLESKY_TAUTOLOGY / "
    "SOURCE_GRAM_NOT_EXACT -- class 3 not reached, stop rule "
    "fires.  SATZ: Chebyshev T2 T1=(T3+T1)/2 over Q; Cauchy "
    "kernel telescopes over Q; Loewner "
    "(psi(z)-conj psi(w))/(z-conj w)=nsum 1/((m+z)(m+conj w)) "
    "to 4.6e-41 at dps 40; folded weights linear in lags "
    "(||w-(wP+wA)||=3.5e-16); Q^T A0 Q already PD on FRAME-A "
    "(nneg=0, lam_min=5.227e-3) so the one defect of A0 is NOT "
    "in the ref-negative compression.  LEG 0: no Chebyshev-U "
    "k-subset of size 49 recovers Vn (maxang 90 deg; greedy "
    "needs all 104 modes) -- numerical projector of A_ref "
    "remains the control (class 2 coordinates).  LEG 2: Euler "
    "Gram vs M residual 209, alignment 0.767 -- correlation, "
    "not identity; tent/fold is linear at the weight layer, "
    "not at the CD Gram.  LEG 3: Loewner identity holds on "
    "the function; Cauchy-Gram vs A0 residual 207, alignment "
    "with M 0.098 -- the arch block of A0 is not this Loewner "
    "matrix.  LEG 4: only-Gram nneg=13; ||B_cross||/||B||=0.617 "
    "rank 104; stacked Euler/tent YY-blocks do not equal B.  "
    "LEG 5: |cos|(v-,1)=0.007; |cos|(v-,Vn)=0.762 mixed with "
    "the complement; |cos|(Q^T 1, vQ)=0.069 -- ones-mode is "
    "not the null mode.  CLASS 1 control: Cholesky of M rest "
    "2.3e-16 on MAIN; permute nneg_M=6 (M not PD) -- tautology "
    "of MAIN-PD, not a source law.  Mutants stay O(1) "
    "(Lambda-perm 314, jitter 209, logn-amp 249, digamma-3/4 "
    "38) -- nothing explodes from residual 0.  Companion "
    "rh/problem/one_defect_gram.tex + "
    "verify_one_defect_gram.py 11/11 ONE DEFECT GRAM VERIFIED.  "
    "NO L* claim, NO R-dagger claim, NO RH claim"
)

_R405_STATUS = (
    "Edge contractive lift (round 405, "
    "PRIME.LDAGGER.EDGE_CONTRACTIVE_LIFT.01, reviewer DCCLXIX "
    "secs. 8 and 12, 35 pct lane after r401/r404: can the missing "
    "Euler null mode be written ell=V c from geometric recurrences "
    "with 1-||c||^2 a manifest positive source sum equal to "
    "kappa(a,b)(-sch) in the r401 Sylvester chart?; "
    "experiments-side, NO ledger row): 30/30 full / 25/25 smoke; "
    "SPEC_SHA b91e6629ee86ce23; Euler-tail residuals, Woodbury "
    "Delta, kappa_closed over Q, disk Parseval, tail-vs-border "
    "relres, ones-split (Delta, c2, kappa) on w9 / core-42 / "
    "chi3 first measured in /tmp (r405_cal.py, r405_cal2.py) "
    "then sealed (disclosed calibration).  Builder fallback NOT "
    "taken: full wall 12.1 s (bar 120 s).  AUSGANG "
    "EDGE_LIFT_PARTIAL.  SATZ: Euler tail 1-z^{K+1}=(1-z)Sum z^r "
    "over Q (z=1/3 K=5 lhs=728/729); disk Parseval "
    "(1-q)Sum q^r=1-q^{K+1} (q=1/2 K=6 ||c||^2=127/128 reserve "
    "1/128); Woodbury Delta=kappa_closed(-sch) with "
    "kappa_closed=-(1-eta) det K2/det K_W over Q (eta=13/12, "
    "Delta=7/36, sch=21/8, kappa=-2/27); 2-pt Cauchy Gram "
    "det=1/72>0.  CENSUS: geometric reconstruction of the "
    "constant on Y residual 8e-16 (explicit nu_p, no optimiser); "
    "ones-split Woodbury w9 Delta=2.110e-3 c2=0.99789 "
    "kappa=0.0315 sch=-0.06696; core-42 Delta>0 42/42 "
    "kappa>0 42/42 0<c2<1 42/42 Delta in [6.7e-6, 2.11e-3].  "
    "Worlds: living chi3 37/37 kappa>0 c2<1; dead chi3 5/5 "
    "sch>0 kappa<0 AND c2<1 -- overflow ||c||>1 REFUTED; death "
    "remains sch>0 (r401).  REFUTED: SM-border = aggregated "
    "z^{K+1} (relres 0.996 corr 0.07); geometric disk sum "
    "O(1e-1) vs Woodbury Delta O(1e-5..1e-3) not the same "
    "scalar; kappa is not a function of (a,b) alone.  OPEN: "
    "source c for the mixed A0 defect (r404 class-3 stop; "
    "|cos|(v-,1)=0.007; v_- vs geometric V relres=0.81).  "
    "KILL: omit tail residual 0.049; wrong-sign J residual "
    "867/115; scramble nneg=21; weight-perm nneg=23 ((G) "
    "breaks before the lift); node jitter does NOT break the "
    "Euler-tail identity (identity in z).  Companion "
    "rh/problem/edge_contractive_lift.tex + "
    "verify_edge_lift.py 12/12 EDGE LIFT VERIFIED.  "
    "NO L* claim, NO R-dagger claim, NO RH claim"
)

_R407_STATUS = (
    "Dual intertwiner (round 407, "
    "PRIME.LDAGGER.DUAL_INTERTWINER.01, shared remainder of "
    "r404/r405 after DCCLXXI/DCCLXXII: transport the Euler/"
    "Digamma Gram through the dual resolvent; experiments-side, "
    "NO ledger row): 29/29 full / 26/26 smoke; SPEC_SHA "
    "2ee74c59b57ed1c6; formula residuals, C-spectrum, nu-rank, "
    "sandwich direction, Euler moment Gram, kill table first "
    "measured in /tmp (r407_cal.py, r407_cal2.py, r407_cal3.py) "
    "then sealed (disclosed calibration).  Builder fallback NOT "
    "taken: full wall 2.4 s (bar 120 s).  AUSGANG "
    "INTERTWINER_EXACT / NU_RANK_NOT_ONE -- P1 REDUZIERT to "
    "lam_2(C)>=1.  SATZ over Q: Hankel G(mu-nu)=G(mu)-G(nu); "
    "Euler split; Woodbury eta=5/6 det=11; "
    "R=C(I+C)^{-1}=I-(I+C)^{-1}; inverse Loewner-antitone; FL "
    "dictionary nneg(R-I/2)={lam(C)<1}.  FORMULA: R = "
    "A G^{-1} A^T = C(I+C)^{-1} with C the mu-only dual CD "
    "Gram on Y (chain-stable Cholesky of G_+); w9 "
    "||C(I+C)^{-1}-R||=1.84e-14, FL 1.46e-13, Cmin=0.85712, "
    "lam2(C)=1.00018, Cmin/(1+Cmin)=0.46153=rmin.  SIGNED: "
    "dual consumes |wu|; signed u gives n_neg_ud=|Y|=104.  "
    "LEG B: source Hankel linear 9.2e-16; Euler prime-pos "
    "G=FF^T rest 1.55e-16 (SOURCE_GRAM_EXACT on the moment "
    "layer); dual G vs source G rel 141 -- not the G that R "
    "inverts.  LEG C REFUTED as rank-1: rank G_nu=104=N_nu, "
    "rank(R-C)=104 reff=1.18; dual CD tail rank-2 (r363) does "
    "not isolate the A0 defect.  LEG D: C-R = "
    "C(I+C)^{-1}C ⪰ 0 (wrong direction for R⪰I/2).  CENSUS: "
    "core-42 nneg=C#<1 on 42/42 (P1 28 / vacuous 14); live "
    "chi3 37/37; dead chi3 5/5 FULFILL the transport (death "
    "is sch>0).  KILL: scramble 21=21; permute 20=20; depth "
    "n+1 rel 0.031 rank-1; Lambda-perm of prime-pos weights "
    "source-G rel 0.54; node-jitter of G(nu) rel 0.014.  "
    "Companion rh/problem/dual_intertwiner.tex + "
    "verify_dual_intertwiner.py 12/12 DUAL INTERTWINER "
    "VERIFIED.  NO L* claim, NO R-dagger claim, NO RH claim"
)

_R408_STATUS = (
    "C-threshold / sampling (round 408, "
    "PRIME.LDAGGER.C_THRESHOLD.01, follow-up of r407 after "
    "DCCLXXIII: at most one lam(C)<1 as Nyquist-at-density-1/2; "
    "experiments-side, NO ledger row): 26/26 full / 22/22 smoke; "
    "SPEC_SHA cb03729fa76c98bd; C anatomy, 1010 spectra, thinning, "
    "densify, worlds, core dmin/kpeak first measured in /tmp "
    "(r408_cal.py, r408_cal2.py, r408_cal3.py) then sealed "
    "(disclosed calibration).  Builder fallback NOT taken: full "
    "wall 2.7 s (bar 120 s).  AUSGANG NYQUIST_REFUTED / "
    "AT_MOST_ONE_CENSUS.  SATZ over Q: 2x2 coherence det(C-I)=-2; "
    "Rayleigh lam_min<=dmin; rank B 3x2 => det C=0; Cauchy "
    "principal of a diagonal.  FORMULA C=BB^T = dressed mu-dual "
    "CD kernel on Y.  w9: dens=0.283 not 1/2, n=181>|Y|=104, "
    "Cmin=0.85712 C2=1.00018 nC=1, dmin=1.656 dmean=33.1 "
    "(diag not ~1), kpeak=52=|Y|/2 ones=0.007 end=0.529 F1=2.  "
    "LEG B REFUTED: 2PER S=20 dens=1/2 nC=3 Cmin=0 (zeros); "
    "S=21 c=2/3 nC=4.  LEG C: SCR nC=21 dmin=0.367 F1=15 "
    "(sparser than source); PERM nC=20 dmin=0.148 same Y; "
    "CHI9 nC=0; CHI15 nC=1 (dictionary holds).  LEG D: thin 0.30 "
    "nC=0 Cmin=1.016; flip+10 nC=8; frozen Cauchy 0.857->0.929; "
    "depth n+1 Cmin=0.99996.  CENSUS core-42 nC in {0,1} "
    "(14/28), dmin in [1.097,1.656], nC=1 => kfrac>=0.85, "
    "nC=0 => endmass=1.  Companion rh/problem/c_threshold.tex + "
    "verify_c_threshold.py 9/9 C THRESHOLD VERIFIED.  NO L* "
    "claim, NO R-dagger claim, NO RH claim"
)

_R409_STATUS = (
    "Borodin-Birkhoff intertwiner (round 409, "
    "PRIME.RDAGGER.BORODIN_BIRKHOFF_INTERTWINER.01, reviewer "
    "'R407', our R409 because R407/R408 are taken; follow-up of "
    "r407 after DCCLXXIV: source-pure min-norm Birkhoff "
    "extension as graph of the r356 dual resolvent; "
    "experiments-side, NO ledger row): 37/37 full / 31/31 smoke; "
    "SPEC_SHA baee9fc568d8e4ee; graph identity, Q three-basis, "
    "SEQ innovations, T-dagger assembly, Phi mismatch, Krein "
    "miss, dead-chi flip first measured in /tmp (r409_cal.py, "
    "r409_cal2.py, r409_cal3.py, r409_cal4.py, r409_cal5.py) "
    "then sealed (disclosed calibration).  Builder fallback NOT "
    "taken: full wall 110.4 s (bar 120 s).  AUSGANG "
    "ONE_DEFECT_TRANSPORT_CENSUS.  SATZ over Q: three bases "
    "identical S0; ker dim = d0-|Y|; "
    "W^{1/2}(W+S0)^{-1}W^{1/2} = Hankel CD = C(I+C)^{-1}; "
    "Woodbury Theta=22/29.  FORMULA T0 = Chebyshev CLS of "
    "min-norm interpolant Y->X in P_<d0, d0=Nw-3 (Jacobi-free; "
    "no R/A0/eig/Cholesky).  w9: ||Rg-R||=2.16e-14, "
    "||T0||=1.08014, nneg(I-TT)=nA0=nD0=1, SEQ nneg=1 at "
    "index 36 val=-0.5117.  LEG C REFUTED as literal: "
    "Theta_terminal = C^T Phi_N C, Schur(ZI) ev vs Phi ev "
    "rel 0.96 (Phi is the Woodbury template).  LEG D REFUTED: "
    "unfitted Krein align 3e-4 rel 3.37; positive Gram "
    "excluded.  CENSUS: core-42 SEQ nneg<=1 on 42/42 (24/18); "
    "SEQ = ind_-(A0) only 32/42 (10 undercounts, all 0!=1).  "
    "KILL: Pi_K=0 rest 28.5; Euler-on-Y vs A0 rel 282; "
    "u^vee=1/u breaks Q; d0+/-1 breaks Q; virtual-star "
    "spread 56.8; permute nneg=20 rest 3.3e-12; scramble "
    "nneg=21 SEQ 12; jitter nneg 1->20.  LEG F dictionary: "
    "T^dagger*T^dagger = (R^dagger)^{-1}-I rest 7.4e-14 "
    "(uses r362 Gram, not a new R-dagger theorem); six "
    "terminal-dead chi all ||T^dagger||>1.  Companion "
    "rh/problem/borodin_birkhoff_intertwiner.tex + "
    "verify_borodin_birkhoff.py 11/11 BORODIN BIRKHOFF "
    "VERIFIED.  NO L* claim, NO R-dagger claim, NO RH claim"
)

_R410_STATUS = (
    "Hole-Nyquist defect (round 410, "
    "PRIME.LDAGGER.HOLE_NYQUIST_DEFECT.01, follow-up of "
    "r407/r408/r409 after DCCLXXV/DCCLXXVI: d_i>=1 via test "
    "poly + why off-diagonal mass hits only the hole-Nyquist "
    "mode; experiments-side, NO ledger row): 21/21 full / "
    "20/20 smoke; SPEC_SHA 1ec4122ecc019cd6; Y-Lagrange "
    "bounds, Chebyshev-CD, Fourier off-fraction, sequential "
    "birth, Bernstein/T0, permute K-split first measured in "
    "/tmp (r410_cal.py, r410_cal2.py, r410_cal3.py, "
    "r410_cal4.py) then sealed (disclosed calibration).  "
    "Builder fallback NOT taken: full wall 3.6 s (bar 120 s).  "
    "AUSGANG N TESTPOLY_REFUTED / DMIN_CENSUS; AUSGANG S "
    "FOURIER_REFUTED / BERNSTEIN_REFUTED / SEQ_REDUCED.  "
    "SATZ over Q: RK K=1/h0; degree obstruction 1/2>1/3; "
    "C_ii=ud K; Rayleigh.  w9 Y-Lagrange deg=103<181 "
    "bmax=0.071 #b>=1=0/104 min(d/b)=94; cheb-CD m=n "
    "#b>=1=81/104 bmin=4.9e-4.  Fourier off_frac=0.968 "
    "band8=0.177.  Theta-prefix: k=32 nC=0 Cmin=1.00014; "
    "k=37 nC=1 Cmin=0.99991; k=104 nC=1 C2=1.00018.  "
    "||T0 v_Nyq||=0.656 < ||T0||=1.080.  PERM dmin=0.1479 "
    "is K-collapse (K=0.148, same Y); SCR dmin=0.367.  "
    "core-42 dmin in [1.097,1.656], nC>1 nowhere.  "
    "Companion rh/problem/hole_nyquist.tex + "
    "verify_hole_nyquist.py 9/9 HOLE NYQUIST VERIFIED.  "
    "NO L* claim, NO R-dagger claim, NO RH claim"
)

_R411_STATUS = (
    "Threshold identity / energy split (round 411, "
    "PRIME.LDAGGER.THRESHOLD_IDENTITY.01, follow-up of r409 "
    "after DCCLXXVI/DCCLXXVII: ||T0||=1/sqrt(lam_min(C)) is "
    "the dual energy split on the quotient; exact ||T0||=1 "
    "on PD REFUTED; experiments-side, NO ledger row): 20/20 "
    "full / 17/17 smoke; SPEC_SHA 090cbc12b41cb27d; "
    "dictionary residuals, Cmin-1 table, Fourier-vs-SV, Q "
    "projection, sequential Cmin, permute/1010 first "
    "measured in /tmp (r411_cal.py, r411_cal2.py, "
    "r411_cal3.py) then sealed (disclosed calibration).  "
    "Builder fallback NOT taken: full wall 23.4 s (bar 120 s).  "
    "AUSGANG ENERGY_SPLIT_EXACT / SATURATION_REFUTED.  SATZ "
    "over Q: T*T=C^{-1}; P_Y is kernel; proj-id 1.3e-15; "
    "uvee=1/u and d0-1 break.  FORMULA ||T||=1/sqrt(Cmin) "
    "w9 1.080138437324 to 1e-14, ||TT-Cinv||=6.6e-14.  "
    "Excess = C-ev0 = top SV (corr 1); Fourier face "
    "||T vF||=0.656 < 1.080 (R410).  PD: kz42 Cmin-1="
    "+4.565e-8, kz130 +4.90e-9, core-42 PD 14/14 in "
    "[1.33e-7, 7.54e-5] -- none exact 0.  k=36/37 is "
    "lam_min crossing (Klast=6.94, not a Christoffel hole).  "
    "KILL: PERM nC=20 Kmin=0.148; SCR nC=21 ||T||=16.66; "
    "1010 ||T||=165; chi9 <1 / chi15 >1.  Companion "
    "rh/problem/threshold_identity.tex + "
    "verify_threshold_identity.py 9/9 THRESHOLD IDENTITY "
    "VERIFIED.  NO L* claim, NO R-dagger claim, NO RH claim"
)

_R413_STATUS = (
    "Hole top mode (round 413, "
    "PRIME.RDAGGER.HOLE_TOP_MODE.01, reviewer primary test "
    "after DCCLXXIX: is the defect the top OP of the hole "
    "measure, and is T0 contractive on that complement?; "
    "experiments-side, NO ledger row): 23/23 full / 19/19 "
    "smoke; SPEC_SHA 9b0e69fefd5ff609; formula, corr, "
    "projected lambda_min, leftover sigma, mass ratio, "
    "permute/scramble, mutants, core-42 / chi / EXT first "
    "measured in /tmp (r413_cal.py, r413_cal2.py, "
    "r413_cal3.py) then sealed (disclosed calibration).  "
    "Builder fallback NOT taken: full wall 23.2 s (bar 120 s).  "
    "AUSGANG TOP_MODE_REFUTED.  SATZ over Q: Lagrange "
    "identity on deg <= q-2, three bases; "
    "pi_{q-1}(y_i)=c/(omega_i P_Y'(y_i)); v_top from Y, "
    "u^vee, P_Y' only (constructor audit: no eig/SVD/"
    "target).  w9 corr(v_top, C-ev0)=0.6766 > Fourier 0.278 "
    "(better than R410 0.386, not the excess).  PRIMARY "
    "FAILS on flagship MAIN: lambda_min(proj)=-0.04763, "
    "n_over=1, leftover sigma=1.02354 (||T||=1.08014).  "
    "QD fails for p==1 (mass_X/Y=1.35713); min-norm saves "
    "constants (||T v_1||=0.359) and does not save HTM.  "
    "core-42: P1 hold 4/28, PD 14/14 trivial.  chi live-P1 "
    "1/37, live-PD 41/41, dead 4/6 (architecture 'dead "
    "must hold' FAILS).  EXT P1 119/35/109/69 all break.  "
    "KILLS: PERM n_over=20; SCR n_over=20; unsigned P' and "
    "random leave sigma~||T||.  Companion "
    "rh/problem/hole_top_mode.tex + "
    "verify_hole_top_mode.py 9/9 HOLE TOP MODE VERIFIED.  "
    "Reviewer order: one clean MAIN violation closes the "
    "route.  NO L* claim, NO R-dagger claim, NO RH claim"
)

_R415_STATUS = (
    "Top-mode edge (round 415, "
    "PRIME.RDAGGER.TOP_MODE_EDGE.01, reviewer DCCLXXIX "
    "parallel to r413: -sch=beta-alpha as the edge of the "
    "barycentric hole-top mode v_i ~ 1/(sqrt(u^vee) P_Y'); "
    "experiments-side, NO ledger row): 26/26 full / 22/22 "
    "smoke; SPEC_SHA 0911860fd986649d; v_top vs T0-SV, Euler "
    "projection, Woodbury eta/r/Delta vs sch, H=A0+vv^T "
    "inertia, closed-kappa mismatch, geo-span, ones control, "
    "MAIN-18 cosine, core-42 + chi3/chi4 sign census first "
    "measured in /tmp (r415_cal.py, r415_cal2.py, "
    "r415_cal3.py, r415_cal4.py) then sealed (disclosed "
    "calibration).  Builder fallback NOT taken: full wall "
    "19.6 s (bar 120 s).  AUSGANG CHART_IDENTITY_EXACT / "
    "TOP_MODE_NOT_DEFECT.  SATZ over Q: Euler tail; disk "
    "Parseval; alpha=(eta-1)/kappa, beta=r^T K^{-1}r/kappa, "
    "beta-alpha=-sch (eta=13/12, Delta=7/36, sch=21/8, "
    "kappa=-2/27, alpha=-9/8, beta=-15/4).  w9: "
    "cos(v_top,v_SV)=0.6766 != 1; alpha_T=-0.07302 "
    "(contractive) vs true SV +0.16670; Euler energy="
    "|<1,v_top>|^2=0.01192 != |alpha_T|; geo-relres=0.74; "
    "Woodbury Delta=4.830e-3 kappa_emp=0.07214 nnegH=1; "
    "ones control reproduces r405 (Delta=2.110e-3, "
    "c2=0.99789, kappa=0.03151); closed kappa formula "
    "mismatches.  MAIN-18 cos(v_top,vneg)=0.058.  CENSUS: "
    "MAIN 42/42 beta>alpha (=sch<0); living chi 78 "
    "beta>alpha; dead chi 6 beta<alpha; identity residual "
    "2e-17; H PD only 18/42.  KILL: wrong omega cos=0.38; "
    "fake P' cos=0.17; PERM nneg=20 SCR=21; K2 mixed on "
    "live AND dead (border omitted).  Companion "
    "rh/problem/top_mode_edge.tex + "
    "verify_top_mode_edge.py 9/9 TOP MODE EDGE VERIFIED.  "
    "NO L* claim, NO R-dagger claim, NO RH claim"
)

_R416_STATUS = (
    "De Branges continuation index (round 416, "
    "PRIME.RDAGGER.DEBRANGES_CONTINUATION.01, reviewer "
    "DCCLXXIX path B after HTM closed: is P1 a "
    "Hermite-Biehler / Potapov index theorem on the two "
    "finite OP systems -- kappa(Theta)<=1, equivalently "
    "Pruefer phase dominance with one winding?; "
    "experiments-side, NO ledger row): 25/25 full / 20/20 "
    "smoke; SPEC_SHA 68a6ee35a0dd9b29; Wronskian over Q, "
    "degree balance, HB interlacing, yyA/yyS, Herglotz of "
    "both Stieltjes transforms, nneg(T0) mismatch, "
    "permute/scramble, B=A mutant, MAIN-42 + chi 78+6 "
    "first measured in /tmp (r416_cal.py, r416_cal2.py, "
    "r416_cal3.py, r416_cal4.py, r416_cal5.py) then sealed "
    "(disclosed calibration).  Builder fallback NOT taken: "
    "full wall 10.5 s (bar 120 s).  AUSGANG "
    "PHASE_DOMINANCE_REFUTED / HB_CENSUS.  SATZ over Q: "
    "monic 3-atom X, W(p2,q2)=-gamma_1 independent of z "
    "(gamma_1=252000/3463321); disc(p2)=17761/19600>0 so "
    "q2-zero interlaces.  SATZ: HB interlacing of (p_n,q_n) "
    "on MAIN 42/42, chi 84/84, toy, permute, scramble.  "
    "w9 balance |X|=263 |Y|=104 d0=181 n_X=181 n_Y=103; "
    "both Herglotz; nneg(I-TT)=1 ||T||=1.08014.  PRIMARY "
    "FAILS: combinatorial Ruecklauf yyA=3 not <=1; yyS=24; "
    "nnegT != yyA; loc vs T0-SV spans [0.059,1] on MAIN.  "
    "MAIN-42 yyA min/med/max 0/4/15; P1 yyA<=1 only 3/28; "
    "PD yyA==0 only 3/14; corr(yyA,nneg)=-0.17.  chi live "
    "med 7 max 26; dead med 2 max 4 (death is fewer, not "
    "more).  KILLS: PERM yyA=4 nneg=20 (world-separator "
    "silent on the phase counter); SCR yyA=16 != 21; B=A "
    "breaks interlacing by degree; full-measure Uvarov "
    "path index 0 cannot see the truncated interpolant.  "
    "Counting argument via the fold partition is closed.  "
    "Companion rh/problem/debranges_index.tex + "
    "verify_debranges_index.py 9/9 DEBRANGES INDEX "
    "VERIFIED.  NO L* claim, NO R-dagger claim, NO RH claim"
)

_R417_STATUS = (
    "Source Schur sign (round 417, "
    "PRIME.RDAGGER.SOURCE_SCH_SIGN.01, reviewer DCCLXXXIII "
    "last non-dead internal lever: sch<0 from the source "
    "via the r401 Sylvester chart, never previously "
    "attacked source-pure; experiments-side, NO ledger "
    "row): 31/31 full / 19/19 smoke; SPEC_SHA "
    "f2905f2a10fddc51; Woodbury + chart formulae over Q, "
    "w9 residuals, sign-map grids, core-42 + EXT-6 + "
    "selected 2^k trend, dead-chi geometry, pivot cross, "
    "scramble/two-period/drop-border/false-chart first "
    "measured in /tmp (r417_cal.py, r417_cal2.py) then "
    "sealed (disclosed calibration).  Builder fallback "
    "NOT taken: full wall 41.2 s (bar 120 s).  AUSGANG "
    "CHART_SCH_EXACT / LIMIT_CENSUS / RATE_OPEN.  SATZ "
    "over Q: sch = den-2 + s^T(A0+Ucd Ucd^T)^{-1}s "
    "(Woodbury) equals P1 sch=phibb+a_un^2-b_un^2 and "
    "VAC sch=phibb-(a_un^2+b_un^2); P1 toy -2/3, VAC "
    "toy -7/6.  Normalized tau cannot see the sign (d3 "
    "quotients it).  VAC phibb<0: whole disk sch<0; P1 "
    "hyperbola, large |a_un| is the danger.  w9 sch="
    "-0.06696, Q=0.33193, dist=0.241, false-chart "
    "2 a_un^2=0.03797.  CORE-42 42/42 sch<0; Q in "
    "[0.283,0.502] den in [1.460,1.652] -- sch is the "
    "O(0.04) difference of two O(1) terms, not the r375 "
    "K2-excess; vac detK>0 so sch is not the r377 "
    "product.  TREND: |t| slope -0.41 falling; |sch| "
    "slope +0.09 FLAT; EXT-119 N=1119 |t|=0.075; "
    "selected k=5,9 sch<0.  tau_inf=0 census; "
    "sch(tau_inf) not a function of normalized tau.  "
    "RATE_OPEN: |t|~N^{-0.47} not derived from Uvarov/"
    "fold (PNT-free form, no k0).  Dead chi 6/6 sch>0, "
    "dist med 0.011 vs live 0.180, 3/5 disk-escape; "
    "dead P1 keeps detK<0.  Companion "
    "rh/problem/source_sch_sign.tex + "
    "verify_source_sch.py 10/10 SOURCE SCH SIGN "
    "VERIFIED.  NO L* claim, NO R-dagger claim, NO RH claim"
)

_R418_STATUS = (
    "Border-border sign (round 418, "
    "PRIME.RDAGGER.PHI_BB_SIGN.01, reviewer DCCLXXXIV "
    "after r417 reduced cofinal sch<0 to phibb<0 plus "
    "|tau_un|->0; phibb is the asymptotic edge-sign "
    "carrier and was never attacked; experiments-side, "
    "NO ledger row): 30/30 full / 19/19 smoke; SPEC_SHA "
    "6ef3a327d623c955; Q-split + C-resolvent, w9 pins, "
    "core-42 P1/VAC mechanisms, pole-share, defect-mutant, "
    "EXT-6 + selected 2^k + chi live/dead, scramble/"
    "two-period/drop-border/false-c_J/r377 first "
    "measured in /tmp (r418_cal.py) then sealed "
    "(disclosed calibration).  Builder fallback NOT "
    "taken: full wall 40.4 s (bar 120 s).  AUSGANG "
    "SPLIT_EXACT / UNIFORM_REFUTED / POLE_NOT_DOMINANT.  "
    "SATZ over Q: phibb = c_J + s^T A0^{-1} s with "
    "c_J = den-2 and A0^{-1} = 2(C+I)(C-I)^{-1}; P1 "
    "toy phibb=-3, VAC toy -1, pole-save toy noD flips "
    "+4.  w9 phibb=-0.08562, c_J=-0.39889, Sigma="
    "0.31326, D=-0.01465, R_+=0.32792, noD=-0.07097 "
    "(flagship NOT pole-saved); C-res 1e-12; false c_J "
    "+1.914.  CORE-42: P1 28/28 phibb<0; VAC 8/14 "
    "phibb<0 and 6/14 overflow at kz 12,13,16,19,39,49 "
    "-- uniform phibb<0 REFUTED.  c_J in [-0.540,"
    "-0.348] all <0; Sigma>0 on VAC.  Defect-saves "
    "3/28 (kz 21,29,36); |D|/|phibb| med 0.076 -- "
    "pole-dominance REFUTED on living P1.  TWO "
    "MECHANISMS: P1 c_J+R_+ already <0 on 25/28; VAC "
    "phibb<0 iff c_J<-Sigma.  TREND slope -0.09 flat "
    "O(0.05).  EXT-6 all phibb<0; selected k=4,5,6,7,9 "
    "phibb<0 (census, no k0).  Dead chi: phibb is NOT "
    "the sole life/death carrier (dead P1 keep phibb<0, "
    "chi3-15 D=-1.22 pole ON DEATH; dead VAC phibb>0).  "
    "Companion rh/problem/phi_bb_sign.tex + "
    "verify_phi_bb.py 10/10 PHI BB SIGN VERIFIED.  "
    "NO L* claim, NO R-dagger claim, NO RH claim"
)

_R419_STATUS = (
    "Vacuous overflow (round 419, "
    "PRIME.RDAGGER.VACUOUS_OVERFLOW.01, reviewer "
    "DCCLXXXV: the r417/r418 tension -- tau_un->0 "
    "so sch->phibb vs 6/14 VAC phibb>0 still live; "
    "experiments-side, NO ledger row): 24/24 full / "
    "16/16 smoke; SPEC_SHA 4809213ddff8cddd; H1/H2/H3 "
    "+ C_min + razor overlap + dead-VAC separator + "
    "scramble/two-period/drop-tau first measured in "
    "/tmp (r419_cal.py, r419_cal2.py) then sealed "
    "(disclosed calibration).  Builder fallback NOT "
    "taken: full wall 78.9 s (bar 120 s).  AUSGANG "
    "H3_REFUTED / RAZOR_POLE_REFUTED / TAU_SAVE_FINITE "
    "/ COFINAL_OPEN.  H1: the 6 stay phibb>0 on "
    "N[151,540], signed slope -0.003 (FLAT, no cross); "
    "N-ranges overlap healthy VAC; EXT/selected VAC "
    "phibb<0 (census, not a law on the 6).  H2: r417 "
    "|t| fall is VAC-driven (slope -1.24) not P1 "
    "(+0.05 FLAT); the 6 live NOW by tau2>phibb; a "
    "cofinal tau floor fails.  H3 REFUTED: VAC "
    "terciles 3/14 -> 7/14, EXT 3/6.  RAZOR-POLE "
    "REFUTED: all 14 VAC at Cmin-1 in [1.3e-7,7.5e-5], "
    "healthy CLOSER; s-overlap ~1e-10, razor share "
    "<=0.022.  r377 prod=+1 on every VAC.  LIFE: live "
    "OVF tau2>phibb; dead VAC tau2<phibb.  Companion "
    "rh/problem/vacuous_overflow.tex + "
    "verify_vacuous_overflow.py 8/8 VACUOUS OVERFLOW "
    "VERIFIED.  NO L* claim, NO R-dagger claim, NO RH claim"
)

_R420_STATUS = (
    "c_J vs Sigma threshold (round 420, "
    "PRIME.RDAGGER.CJ_SIGMA_THRESHOLD.01, reviewer "
    "DCCLXXXVI: cofinal VAC c_J<-Sigma as the r419 "
    "reduction of sch<0; experiments-side, NO ledger "
    "row): 20/20 full / 15/15 smoke; SPEC_SHA "
    "46409e2f11820dd6; den identity, occupation, "
    "naive Sigma bound, reserve trend, selected "
    "k=4..9, EXT, dead VAC, P1 one-balance, scramble/"
    "drop-2 first measured in /tmp (r420_cal.py) then "
    "sealed (disclosed calibration).  Builder fallback "
    "NOT taken: full wall 37.0 s (bar 120 s).  AUSGANG "
    "DEN_EXACT / BOUND_LOOSE / RESERVE_SHRINKS / "
    "COFINAL_OPEN.  SATZ: den=1+||bvec||^2/B_w - vt·s "
    "with B_w=S_{N-2}+5/7; w9 den=1.60111 gam=0.6778 "
    "Bw=8.382.  ALL 42 den in [1.460,1.652]<2, "
    "gap-to-2 [0.348,0.540] O(1) FLAT.  Sigma O(0.40) "
    "on moderate C-modes (lam_w 3.2..4.6); razor share "
    "<=3e-7; naive occupied-max bound 200..24000 x "
    "Sigma (LOOSE).  ||s||^2~0.06 FLAT.  Reserve "
    "OKV [0.011,0.068], OVF <0, EXT VAC [0.029,0.037]; "
    "selected k=4..9 all R>0 but SHRINKS 0.105->0.038 "
    "(hoped O(1) gap REFUTED).  ONE BALANCE: "
    "phibb=c_J+Sigma on both charts; P1 R_+/|Sigma| "
    "med 1.009.  The 6 remain a named finite class.  "
    "Companion rh/problem/cj_sigma.tex + "
    "verify_cj_sigma.py 8/8 CJ SIGMA VERIFIED.  "
    "NO L* claim, NO R-dagger claim, NO RH claim"
)

_R421_STATUS = (
    "reserve limit (round 421, "
    "PRIME.RDAGGER.RESERVE_LIMIT.01, reviewer "
    "DCCLXXXVII: does R=-phibb go to 0 or to "
    "R_inf>0 on selected a_k=2^k; experiments-side, "
    "NO ledger row): 22/22 full / 16/16 smoke; "
    "SPEC_SHA 234a1113450c476f; selected k=4..9, "
    "EXT, T0-Cgap dictionary, Sigma channels, AIC "
    "M1/M2/M3, dead/overflow/scramble first measured "
    "in /tmp (r421_cal.py, r421_cal_deep.py) then "
    "sealed (disclosed calibration).  Builder "
    "fallback TAKEN for k=8 only: /tmp wall 226 s "
    "N=5690, R=0.04763 PINNED not re-gated live.  "
    "Full wall 39.3 s (bar 120 s).  k=10 kz197 "
    "N=4071 border_fail (29.5 s); k=11 N=12508 "
    "skipped.  AUSGANG FLOOR_PREFERRED / LOG_KILLED "
    "/ K10_BORDER_FAIL / COFINAL_OPEN.  SATZ: "
    "R=-phibb; T0-1=-(C_min-1)/2 on VAC (ratio "
    "1.0000).  REFUTED: M3 R~c/log k (DeltaAIC "
    "18.4).  REDUZIERT: M1 wins vs k with "
    "R_inf=+0.0298 (vs a_k +0.034); M2 loses "
    "DeltaAIC 6.9; EXT VAC sit in [0.0285,0.0373].  "
    "den FLAT [1.48,1.65]; Sigma channel = n_eff "
    "broadens (18->146), s2 flat O(0.06), lam_w "
    "mild.  Three saturation scales, NOT one "
    "exponent (budget O(0.5) / razor 1e-6 / "
    "edge-balance O(0.04)).  Companion "
    "rh/problem/reserve_limit.tex + "
    "verify_reserve_limit.py 8/8 RESERVE LIMIT "
    "VERIFIED.  NO L* claim, NO R-dagger claim, "
    "NO RH claim"
)

_R422_STATUS = (
    "Sigma limit (round 422, "
    "PRIME.RDAGGER.SIGMA_LIMIT.01, reviewer "
    "DCCLXXXVIII: limsup Sigma < 2-den_inf on "
    "selected a_k=2^k, source-pure; experiments-side, "
    "NO ledger row): 16/16 full / 12/12 smoke; "
    "SPEC_SHA d81fc5fcb4e87711; occ spectra, "
    "Stieltjes identity, near-1 masses, KS, "
    "1-pole/Cauchy density attempt, overflow, "
    "dead chi, EXT first measured in /tmp "
    "(r422_cal.py) then sealed (disclosed).  "
    "Builder fallback TAKEN for k=8 occ (r421 "
    "pin, 226 s).  Full wall 31.9 s (bar 120 s).  "
    "AUSGANG STIELTJES_EXACT / DENSITY_REFUTED / "
    "NEAR1_STABLE / LIMITS_OPEN.  SATZ: "
    "Sigma=2||s||^2+4 s^T(C-I)^{-1}s = 2 sum occ g.  "
    "REFUTED: 1-pole / Cauchy closed occ density "
    "(rel 0.73 / 0.95); n_eff growth as pole-creep.  "
    "REDUZIERT: near-1 mass O(0.01) stable; KS "
    "falls 0.14->0.04; EXT Sigma<=0.469; den_inf "
    "and Sigma_inf NOT constructed.  Companion "
    "rh/problem/sigma_limit.tex + "
    "verify_sigma_limit.py 7/7 SIGMA LIMIT "
    "VERIFIED.  NO L* claim, NO R-dagger claim, "
    "NO RH claim"
)

_R423_STATUS = (
    "den limit (round 423, "
    "PRIME.RDAGGER.DEN_LIMIT.01, reviewer "
    "DCCLXXXIX: den_k -> den_inf < 2 source-pure "
    "or limsup den <= dbar < 2 explicit; "
    "experiments-side, NO ledger row): 16/16 full "
    "/ 13/13 smoke; SPEC_SHA 156933164983782f; "
    "gamma anatomy, ||b||^2 vs S, vts, core-42, "
    "selected, EXT, dead chi first measured in "
    "/tmp (r423_cal.py) then sealed (disclosed).  "
    "Builder fallback TAKEN for k=8 (r421 pin "
    "den=1.56855).  Full wall 37.2 s (bar 120 s).  "
    "AUSGANG FORMULA_EXACT / GAMMA_LT1_CENSUS / "
    "LIMIT_OPEN / SUBSUM_REFUTED.  SATZ: "
    "den=1+gam-vts.  Hierarchy (i) not reached.  "
    "Hierarchy (ii): gam<1 on 42/42+EXT+dead "
    "(max 0.724), NOT a chain SATZ; ||b||^2 is "
    "NOT a subsum of S (prefix 0.92->0.65).  "
    "Hierarchy (iii): den<=1.652, gap>=0.348, "
    "dbar=1.66 census.  vts>0 on all "
    "([0.067,0.096]).  Dead den<2.  Companion "
    "rh/problem/den_limit.tex + "
    "verify_den_limit.py 7/7 DEN LIMIT "
    "VERIFIED.  NO L* claim, NO R-dagger claim, "
    "NO RH claim"
)

_R424_STATUS = (
    "gamma chain (round 424, "
    "PRIME.RDAGGER.GAMMA_CHAIN.01, reviewer "
    "DCCXC: ||b||^2 <= B_w = S_{N-2}+5/7 as a "
    "border-chain theorem so gamma<1; "
    "experiments-side, NO ledger row): 18/18 full "
    "/ 15/15 smoke; SPEC_SHA 0c85977b0a25576e; "
    "b vs mu-side Parseval, w_k = b_k^2/rho_k, "
    "||b||^2 vs S vs B_w, unnorm mutant, "
    "permute/scramble, core-42, selected, EXT, "
    "dead chi first measured in /tmp "
    "(r424_cal.py, r424_cal2.py) then sealed "
    "(disclosed).  Builder fallback TAKEN for "
    "k=8 (r421 pin gamma=0.6386).  Full wall "
    "30.2 s (bar 120 s).  AUSGANG BESSEL_EXACT / "
    "W_TERM_REFUTED / SHARP_CENSUS / GAMMA_OPEN.  "
    "SATZ: b_k = <sigma, phat_k^mu>, ||b||^2 == "
    "mu_side_budget.  REFUTED: uniform w_k <= "
    "wbar<1 (~43% of terms >1).  CENSUS: "
    "||b||^2 <= 0.80 S (k=5 max 0.799); gamma<1 "
    "on 42/42+EXT+dead (max 0.724).  Dead keep "
    "gamma<1; scramble border_fail; unnorm "
    "gamma=2.51>1.  Companion "
    "rh/problem/gamma_chain.tex + "
    "verify_gamma_chain.py 7/7 GAMMA CHAIN "
    "VERIFIED.  NO L* claim, NO R-dagger claim, "
    "NO RH claim"
)

_R425_STATUS = (
    "cross-chain gamma (round 425, "
    "PRIME.RDAGGER.CROSS_CHAIN_GAMMA.01, reviewer "
    "DCCXCI: ||b||^2 < B_w as a cross-chain "
    "theorem; experiments-side, NO ledger row): "
    "17/17 full / 14/14 smoke; SPEC_SHA "
    "458ee51d6db76776; kernel Loewner, ||G||_op, "
    "q_N vs B_w, dead q_N>1, unnorm, core-42 "
    "first measured in /tmp (r425_cal.py, "
    "r425_cal2.py, r425_cal3.py) then sealed "
    "(disclosed).  Builder fallback TAKEN for "
    "k=8 (r421 pin gamma=0.6386).  Full wall "
    "30.9 s (bar 120 s).  AUSGANG B2_LE_S_SATZ / "
    "QN_BRIDGES_BW / DEAD_NEEDS_SLACK / "
    "COFINAL_OPEN.  SATZ: ||b||^2 <= S "
    "(K_mu ≼ K_{mu-nu} on P_<N).  Posted "
    "||b||^2 < B_w REDUZIERT to q_N<1.  On the "
    "v960 42-rung q_N<1 census it composes to "
    "gamma<1.  Dead q_N=1.21,1.33>1 (S>B_w; "
    "slack still saves gamma).  ||G||_op^2=1.  "
    "Companion rh/problem/cross_chain_gamma.tex + "
    "verify_cross_chain.py 6/6 CROSS CHAIN "
    "VERIFIED.  NO L* claim, NO R-dagger claim, "
    "NO RH claim"
)


_R427_STATUS = (
    "campaign audit R397-R426 (round 427, "
    "PRIME.RDAGGER.CAMPAIGN_AUDIT.01, reviewer "
    "DCCXCIV: adversarial re-verification of "
    "load-bearing campaign numbers; "
    "experiments-side, NO ledger row): 52/52 "
    "full / 44/44 smoke; SPEC_SHA "
    "b317327d451ab0c6; independent r367 "
    "A0+I/2 vs dense Chebyshev-Hankel C, "
    "full-carrier dual, KKT ||T0||, truncated "
    "PD Grams, AIC re-fit, four death "
    "coordinates, grep code-class hunt.  "
    "Two-run smoke byte-identical.  AUSGANG "
    "0 BUG / 2 SUSPECT / 5 CLEAN.  CLEAN: "
    "intertwiner R=C(I+C)^{-1} on kz9/17/12 "
    "(w9 formula 3.38e-12, dictionary "
    "ind_-=#{lam C<1}); QD mass 1.357130 "
    "from one full-carrier dual (subset-P' "
    "would give 1.525); KKT ||T0||_w9="
    "1.080138437324, kappa(C)=2.086e3 so "
    "kz42 pin 4.57e-8 is 56x eigvalsh noise, "
    "r409 1.00000 is display rounding; "
    "kernel Loewner on PD truncated Grams "
    "n=16 (indefinite Q-toy blocks the "
    "hypothesis); 6/6 dead qN>1 <=> "
    "|Z|_term>=sqrt(5/7) <=> sch>0, live "
    "chi3-9 does not fire.  SUSPECT: floor "
    "vs k M1 R_inf=+0.02983 but vs N winner "
    "M3 (k=8 N=5690 > k=9 N=1433; k=8 point "
    "is a builder pin); disclosed k=8 pin "
    "circularity r421->r425 and float64 "
    "eigvalsh razors.  No round verdict of "
    "R397-R426 changes.  Companion "
    "rh/problem/campaign_audit.tex + "
    "verify_campaign_audit.py 9/9 CAMPAIGN "
    "AUDIT NOTE VERIFIED.  NO L* claim, NO "
    "R-dagger claim, NO RH claim"
)


_R428_STATUS = (
    "q_N reopened on the selected sequence "
    "(round 428, PRIME.TERMINAL.QN_REOPENED.01, "
    "reviewer: terminal lane with the new "
    "coordinate arsenal; experiments-side, NO "
    "ledger row): 23/23 full / 19/19 smoke; "
    "SPEC_SHA fc2c617a6bd34c6c; four-coordinate "
    "census, COMPOSE envelopes, razor-overlap "
    "vs Nyquist, P1/VAC split, dead chi, "
    "scramble, false-anchor kz=16 first "
    "measured in /tmp (r428_cal.py, "
    "r428_cal2.py) then sealed (disclosed).  "
    "Builder fallback TAKEN for k=8 (r421 pin, "
    "N=5690).  Full wall 12.1 s (bar 120 s).  "
    "AUSGANG SELECTED_MARGIN_GO / "
    "OVERLAP_VAC_ONLY / ZLOC_WINS / "
    "COFINAL_OPEN.  Selected q_N in "
    "[0.00070, 0.3828], min-margin 0.617 vs "
    "42er 0.0195 at kz=16.  COMPOSE R<=1.40 "
    "<<4, L1<=0.63<<3, |Z_loc|<=0.487<1/2.  "
    "REFUTED: razor-overlap as a global fourth "
    "death coordinate (P1 living share up to "
    "3.6e-2 overlaps dead; VAC 4-order split "
    "survives; kz=16 near-dead has share "
    "5.4e-9).  Nyquist face of C_min REFUTED "
    "on VAC (cos -0.007 vs P1 -0.386).  "
    "Winner |Z_loc|; sublemma |Z_loc|<=1/2 on "
    "MAIN selected (k=3 tight; scramble "
    "breaks it).  Companion "
    "rh/problem/qn_reopened.tex + "
    "verify_qn_reopened.py 6/6 QN REOPENED "
    "VERIFIED.  NO L* claim, NO R-dagger "
    "claim, NO RH claim"
)


_R429_STATUS = (
    "selected |Z_loc| head bound "
    "(round 429, PRIME.TERMINAL.ZLOC_HEAD_BOUND.01, "
    "reviewer: terminal lane after r428; experiments-side, "
    "NO ledger row): 24/24 full / 18/18 smoke; SPEC_SHA "
    "cb57a725042119da; Z_loc = t_loc + chain identity "
    "SATZ (canonical_split, pins 0.486846 / 0.157211 / "
    "0.227187); unsigned triangle / Chebyshev / left-right "
    "Abel REFUTED on selected (tri 2.24..19.24, two-point "
    "slope +0.72, no k0); |Z_loc|<=1/2 remains a finite "
    "census (k=3 tight, scramble 0.524); hoped L1<=3/5 "
    "FAILS at k=9 (0.628), 2/3 works; R<=1.396<3/2 census.  "
    "First measured in /tmp (r429_cal.py) then sealed "
    "(disclosed).  No k=8 rebuild.  Full wall 4.2 s.  "
    "AUSGANG FORMULA_SATZ / TRIANGLE_REFUTED / "
    "BOUND_CENSUS / NO_K0.  Companion "
    "rh/problem/zloc_head.tex + "
    "verify_zloc_head.py 6/6 ZLOC HEAD VERIFIED.  "
    "NO L* claim, NO R-dagger claim, NO RH claim"
)


_R431_STATUS = (
    "source Potapov factor "
    "(round 431, PRIME.RDAGGER.SOURCE_POTAPOV_FACTOR.01, "
    "reviewer discovery 1 of 2 after DCCXCVII; experiments-side, "
    "NO ledger row): 17/17 full / 17/17 smoke; SPEC_SHA "
    "64eabb7c2448dd48; unipotent Redheffer product of "
    "point-mass 2x2 factors equals the Cauchy m-function of "
    "X EXACT over Q (z=7/3 gives -7471/22950); Cauchy-pi "
    "identity for Lagrange S0 at kdim=0 EXACT; Gate 3 "
    "REFUTED: Pick(product) is PD (kappa=0) while "
    "I-T0*T0 has nneg=1 on the kdim=0 toy (D11=-1744/2025) "
    "and on w9/kz15/kz18 (||T||=1.08014/1.10672/1.24966).  "
    "Source-order growing-Y Uvarov has 0 negative pivots "
    "(min 3.25e-7); lag-local fold(c^P_p) nneg 18/19/15 "
    "for p=2/3/5 -- NOT simpler (stop rule 3).  PERM 20 / "
    "JIT 19 / SCR 21; twin nneg=1 bit-near.  First measured "
    "in /tmp (r431_cal.py, r431_cal2.py, r431_cal3.py) then "
    "sealed (disclosed).  Full wall 0.2 s.  AUSGANG "
    "SOURCE_FACTOR_NOT_FOUND.  Companion "
    "rh/problem/source_potapov.tex + "
    "verify_source_potapov.py 7/7 SOURCE POTAPOV VERIFIED.  "
    "NO L* claim, NO R-dagger claim, NO RH claim"
)



_R431_AUDIT_STATUS = (
    "adversarial focus-audit of R431 "
    "SOURCE_FACTOR_NOT_FOUND "
    "(round 431-AUDIT, reviewer DCCXCVII Q1-Q3; "
    "experiments-side, NO ledger row): 22/22 full / "
    "21/21 smoke; SPEC_SHA 72f5484cc290b740; "
    "independent constructors (no import of "
    "source_potapov_probe).  Q1 CONFIRMED: "
    "Blaschke-Potapov factors with source "
    "alpha=x+i|w| and u=(2,x) do not commute "
    "(||[B0,B1]||=5.561e-2) and are J-unitary on R; "
    "the Homma Redheffer star equals the chain "
    "product (6.0e-17) and on unipotents is the "
    "mass sum (residual 0); J-kernel Pick of the "
    "positive-mass product is PD (nneg=0, "
    "lam_min=4.679e-3).  Closure lemma: any finite "
    "J-product of source-pure positive-mass factors "
    "stays in S_0 (Krein-Langer kappa additive, "
    "cannot increase).  Inverse-Blaschke of the Arch "
    "atom has J-kernel nneg=2, rel vs D0=0.777 -- "
    "not the interpolant residual.  Q2 CONFIRMED: "
    "m_X(7/3)=-7471/22950 EXACT; D0 inertia (1,1,0) "
    "D11=-1744/2025; P_X (2,0,0); w9 "
    "lam_min(P_X)=8.67731 ind_-(I-TT)=1; "
    "source-order Uvarov 0/104 min=3.248e-7 vs "
    "r409 index 36; lag-local 18/19/15.  Q3 "
    "CONFIRMED: Cauchy-pi = Lagrange on the five-atom "
    "toy AND a second 6-node Q-window (D0 inertia "
    "(1,2,0), P_X (3,0,0)).  Full wall 0.2 s.  "
    "AUSGANG CONFIRMED (NOT_FOUND stands, including "
    "the non-commutative check).  Companion "
    "rh/problem/r431_audit.tex + "
    "verify_r431_audit.py 7/7 R431 AUDIT NOTE "
    "VERIFIED.  NO L* claim, NO R-dagger claim, "
    "NO RH claim"
)


_R433_STATUS = (
    "edge as Redheffer / Schur step "
    "(round 433, PRIME.RDAGGER.EDGE_REDHEFFER_COMPLETION.01, "
    "reviewer DCCXCVII Teil D; experiments-side, "
    "NO ledger row): 27/27 full / 24/24 smoke; SPEC_SHA "
    "8371b954f4d56847; R->R^dagger IS the terminating "
    "2x2-block Redheffer star of Theta=[[A,U],[U^T,0_3]] "
    "with E=J=diag(I_2, 1/den) SATZ (Q residual 0, den=23/30; "
    "w9 residual 1.9e-15; sequential CD-then-border equals "
    "the packed 3x3).  Last Potapov pivot extracted from "
    "the border of M^dagger (r362 sch_b / q^dagger), NOT "
    "defined from sch: delta := 1-q^dagger = "
    "4 sch_b/(1+2 sch_b) = -sch with c'=1 "
    "(Q: sch=-187/450, sch_b=187/1426, delta=187/450).  "
    "delta = c (1/4-|Z_loc|^2) REFUTED as world-blind "
    "(selected c in [0.155, 5.51]; living CHI3-9 and "
    "vacuous MAIN kz12/16: delta>0 but qtr<0).  "
    "Energy form delta=1-|alpha_edge|^2 with "
    "|alpha_edge|^2=q^dagger.  Dead chi 6/6 via delta<0; "
    "living MAIN+chi delta>0; scramble nnegA0=21 "
    "(bulk already dead).  k=3: |Z_loc|=0.486846, "
    "air 0.013154, delta=0.071564>0.  Kills: drop-border "
    "(no 3x3 pivot); ones-Woodbury Delta 2.11e-3 != "
    "delta 0.067; r263 q_N=(7/5)Z^2 on full Z not Z_loc.  "
    "First measured in /tmp (r433_cal.py, r433_cal2.py) "
    "then sealed (disclosed; ID_RES=2e-12, ID_CENSUS=2e-7).  "
    "No k=8 rebuild.  Full wall 9.0 s.  Builder fallback "
    "NOT taken.  AUSGANG REDHEFFER_EXACT / "
    "PIVOT_IS_ONE_MINUS_QDAG / QUARTER_NOT_UNIVERSAL.  "
    "Companion rh/problem/edge_redheffer.tex + "
    "verify_edge_redheffer.py 8/8 EDGE REDHEFFER VERIFIED.  "
    "NO L* claim, NO R-dagger claim, NO RH claim"
)


_R435_STATUS = (
    "P1 as an overload bound "
    "(round 435, PRIME.RDAGGER.P1_OVERLOAD.01, "
    "reviewer DCCCII first half of two-case inertia, "
    "source-pure, no margin; experiments-side, "
    "NO ledger row): 23/23 full / 20/20 smoke; SPEC_SHA "
    "d032621d5417873f; nested mu-CD C(n)=B[:,:n]B[:,:n].T "
    "is rank-1 Loewner SATZ (nC antitone, drop <= 1; "
    "dictionary nC(N_w-3)=n_-(A0)).  w9 nC 104 -> 43(|Y|) "
    "-> 1(181), hit1=178 last six (2,2,1,1,1,1).  "
    "GK / Cauchy-pi universal n_-<=1 REFUTED: Q 2x2 toy "
    "inertia (1,1,0) det=-3740/243; 3x3 nneg 2,1,0; "
    "mass-imbalanced 2x2 ND inertia (0,2,0) "
    "det=113/2880000.  PERM nC(|Y|)=54 nCend=20 never "
    "hits 1; JITTER 19; SCRAMBLE 21; 2PER nmax<|Y| "
    "nCend=4.  Core-42 42/42 nCend in {0,1} (28 P1 / "
    "14 VAC); living chi3 37/37 + chi4 41/41 and dead "
    "chi3 5/5 + chi4-20 all nCend in {0,1}.  False depth "
    "N_w-1 lifts MAIN to nC=0.  First measured in /tmp "
    "(r435_cal.py, r435_cal2.py, r435_cal3.py) then "
    "sealed (disclosed).  Full wall 13.6 s.  Builder "
    "fallback NOT taken.  AUSGANG DEPTH_CHAIN_EXACT / "
    "GK_UNIVERSAL_REFUTED / SAVE_RATE_CENSUS.  Companion "
    "rh/problem/p1_overload.tex + "
    "verify_p1_overload.py 8/8 P1 OVERLOAD VERIFIED.  "
    "NO L* claim, NO R-dagger claim, NO RH claim"
)


_R436_STATUS = (
    "P2 determinant as reverse-CS / rank-1 "
    "(round 436, PRIME.RDAGGER.P2_DETERMINANT.01, "
    "reviewer Hauptlane second half; experiments-side, "
    "NO ledger row): 26/26 full / 19/19 smoke; SPEC_SHA "
    "d596aecc4dff3ef1; SATZ det K2 = det(K2_+)-Q with "
    "Q = p^T adj(K2_+) p = ||p||^2 + p^T adj(R_+) p "
    "(Q-toy det=-7 = 2-9); C_min = psi_- (r407 cosine=1); "
    "nneg-1 45/74 detK<0, -det in [1.157, 1126.389]; "
    "Rayleigh excess min 0.2746 at kz18; "
    "coarse ||p||^2 > lmax(K2_+) sufficient SATZ 44/45 "
    "KILLED at kz46 (same window as r375 Cauchy); "
    "anatomy MIXED Ta=25 Td=4 Tx=16; "
    "alternation 45/45 iff detK<0 (r377 dictionary); "
    "vacuous 29/74 no pole detK>0 (14/42 core); "
    "dead chi CHI3-15 nneg-1 detK=-122.91 (P2 stays; "
    "sch is NOT this product, r417); "
    "drop-psi w9 det(K2_+)=5.958>0; wrong J=-I det=+0.941; "
    "scramble nneg=21 hypothesis empty.  "
    "Remainder: p^T K2_+^{-1} p > 1 (CD--C_min coupling).  "
    "First measured in /tmp (r436_cal.py, r436_cal2.py) "
    "then sealed (disclosed).  Full wall 42.3 s.  "
    "Builder fallback NOT taken.  AUSGANG REDUZIERT / "
    "IDENTITY_EXACT / ANATOMY_MIXED / COARSE_KILLED_AT_KZ46 / "
    "ALTERNATION_EXPLAINED.  Companion "
    "rh/problem/p2_determinant.tex + "
    "verify_p2_determinant.py 8/8 P2 DETERMINANT VERIFIED.  "
    "NO L* claim, NO R-dagger claim, NO RH claim"
)


_R438_STATUS = (
    "evolutionary certificate search "
    "(round 438, PRIME.SEARCH.EVOLUTIONARY_CERTIFICATE.01, "
    "reviewer search lane after DCCCII; experiments-side, "
    "NO ledger row): 29/29 full / 29/29 smoke; SPEC_SHA "
    "d6c1624b82717fba; hard train/holdout split "
    "(fitness = MAIN {9,18,20} only; chi3/chi4 + EXT-35 + "
    "Selected k>=7 NEVER in any fitness loop).  "
    "Track A grammar GP (seed 43801, pop 24 gen 10): "
    "best min-cos 0.1010 expr INVPY; four canonical "
    "psi candidates 0.007-0.71 on w9, uniform vtop "
    "0.058 at kz18; source NNLS for lam2-1 and q^dagger "
    "relres >> 1.  Track B: source NNLS onto -det K2 "
    "relres 13.2; r375 identity live on w9 "
    "(fact=-5.038869, gamma/lam=1.846) but uses psi_-; "
    "B2 family P=t0 I+t1 diag(u), v=v_top remainder "
    "lmin=-0.261 not PSD.  Track C canonical cut dn=0: "
    "nC<=1 on 11/11 CORE, closest C2-1=2.245e-7 at "
    "kz52; holdout 7/7 nC in {0,1}; weight-scale GA "
    "nC=1.  Truncation dn=-2 inflates nC=2 on "
    "{5,18,22,38,52} -- r395 class, NOT a falsifier.  "
    "Q toys residual 0 (ONES-Y, r375 det=-7, B2 Rest=0).  "
    "PERM nC=21 SCR nC=21; illegal CHI3 a=0 nC=3.  "
    "First measured in /tmp (r438_cal.py, r438_cal2.py, "
    "r438_cal3.py) then sealed (disclosed).  Full wall "
    "1.7 s.  Builder fallback NOT taken.  AUSGANG "
    "A:NOT_FOUND / B:NOT_FOUND / C:NOT_FOUND.  Companion "
    "rh/problem/evolutionary_certificate.tex + "
    "verify_evolutionary_cert.py 10/10 EVOLUTIONARY CERT "
    "VERIFIED.  NO L* claim, NO R-dagger claim, NO RH claim"
)


_R439_STATUS = (
    "interpolant residual Loewner/Bezout "
    "(round 439, PRIME.RDAGGER.INTERPOLATION_RESIDUAL_LOEWNER_BEZOUT.01, "
    "reviewer DCCCIV; experiments-side, NO ledger row): "
    "25/25 full / 22/22 smoke; SPEC_SHA 7a0b53f06d2c7564; "
    "rank(Y D0 - D0 Y)=2 EXACT on 5-atom and 6-node Q toys; "
    "w9/kz15/kz18 sigma3/sigma2 = 9.42e-15 / 1.08e-14 / "
    "4.41e-15 (mpmath dps40 w9 9.42e-15, sigma3=1.30e-15); "
    "S0 = K_YY^{-1} EXACT (RKHS of P_<d0> on X); "
    "kdim=0 dressed Loewner SATZ Delta D0 Delta = "
    "L_{-m-tilde} + diag(w_Y (P_Y')^2); D0 itself is NOT "
    "ones-Loewner at |Y|>=3 (ones-res 40073273/275164890); "
    "nY=2 old trap documented (L_f nneg=0, diag carries "
    "nneg=1).  B1 Bez(P_Y, Q=interp(m-tilde)) FAIL "
    "(Cauchy-pi rational is m-like with P_X poles, not "
    "P_Y); Sturm last -7466971/10681442 != 1-q^d=187/450.  "
    "CInd of m-tilde/P' is 52 vs nneg(D0)=1 -- not P1.  "
    "Worlds: MAIN nneg=1; CHI3-9 nneg=0; CHI3-15 nneg=1; "
    "PERM/JIT/SCR 20/19/21 (rank-2 survives).  First "
    "measured in /tmp (r439_cal.py .. r439_cal4_sturm.py) "
    "then sealed (disclosed).  Full wall 2.9 s.  Builder "
    "fallback NOT taken.  AUSGANG "
    "RESIDUAL_LOEWNER_PLUS_CONTROLLED_DIAGONAL.  Companion "
    "rh/problem/residual_loewner.tex + "
    "verify_residual_loewner.py 7/7 RESIDUAL LOEWNER "
    "VERIFIED.  NO L* claim, NO R-dagger claim, NO RH claim"
)


_R440_STATUS = (
    "mean tau index "
    "(round 440, PRIME.RDAGGER.MEAN_TAU_INDEX.01, "
    "reviewer DCCCIV fallback lane; experiments-side, "
    "NO ledger row): 28/28 full / 28/28 smoke; SPEC_SHA "
    "3807189a56e259da; T1 kappa^dagger = "
    "ind_-(R^dagger-1/2 I) = #{s in (0,1): tau^dagger(s)=0} "
    "SATZ (Q 2x2 kappa=1 exact; r409 5-atom C pin kappa=0; "
    "w9 three-way 0 at 2e-14).  T2 integrand Jacobi SATZ "
    "(FD rel 4.8e-8); Q winding 1.000; window contour "
    "is the COLLAR BOSS (r=0.40 winds 0, r=0.499 "
    "fractional -1.77; gap_right 3.0e-3 -> 1.9e-8 on "
    "selected k=3..9).  Source: CD residual 2e-12; "
    "cyclic TT* / Dirichlet diagonal / slogdet at 1.4e-14.  "
    "MI2 linearity 4e-15; Lean landing site "
    "exists_index_zero_of_block_mean_lt_one (r430).  "
    "Census: selected 6/6 kappa=0, core-42 42/42 kappa=0 "
    "mean=0<1 (NO kappa>=1 trend); dead chi 6/6 kappa=1; "
    "live CHI3-9 kappa=0.  Kills: trG 50.9 vs 53.0 both "
    ">>1; M2 32.96 vs 39.01 both >>2 (r398); tau(0.5)>0 "
    "on living AND dead (s is a counting variable); "
    "scramble nneg=21.  k=8 not rebuilt.  First measured "
    "in /tmp (r440_cal.py, r440_cal2.py) then sealed "
    "(disclosed).  Full wall 9.3 s.  Builder fallback "
    "NOT taken.  AUSGANG IDENTITIES_EXACT / "
    "COLLAR_BOSS_QUANTIFIED / BLOCK_MEAN_CENSUS / "
    "UNCONDITIONAL_OPEN.  Companion "
    "rh/problem/mean_tau_index.tex + "
    "verify_mean_tau.py 8/8 MEAN TAU INDEX VERIFIED.  "
    "NO L* claim, NO R-dagger claim, NO RH claim"
)


_R441_STATUS = (
    "diagonal lifts Loewner "
    "(round 441, PRIME.RDAGGER.DIAGONAL_LIFTS_LOEWNER.01, "
    "reviewer DCCCX; experiments-side, NO ledger row): "
    "17/17 full / 13/13 smoke; SPEC_SHA 1de031a3dbd907af; "
    "L_m = C diag(w pi^2) C^T EXACT (5-atom L inertia "
    "(0,2,0), 6-node (0,3,0)); X-between-Y does NOT set "
    "L-inertia.  Lift count SATZ n_-(W-K^{-1}) = "
    "#{lambda(W^{1/2} K W^{1/2})<1} (kdim=0: n_below_-1).  "
    "d_min>1 => n_-<=1 REFUTED (6-node dmin=210157/57600 "
    "and n_-=2).  Selected census: w9/kz15/18/52 n_lt1=1; "
    "c22 gap_lo=0.99981; CHI3-9 n_lt1=0; CHI3-15 n_lt1=1; "
    "PERM/JIT/SCR 20/19/21 dmin<1.  diag(D0) is not the "
    "carrier.  Pair form fails at kdim>0.  First measured "
    "in /tmp (r441_cal.py, r441_cal2.py) then sealed "
    "(disclosed).  Full wall 0.4 s.  Builder fallback "
    "NOT taken.  AUSGANG REDUZIERT.  Companion "
    "rh/problem/diag_lifts_loewner.tex + "
    "verify_diag_lifts.py 6/6 DIAG LIFTS VERIFIED.  "
    "NO L* claim, NO R-dagger claim, NO RH claim"
)

_R442_STATUS = (
    "unconditional block mean "
    "(round 442, PRIME.RDAGGER.UNCONDITIONAL_BLOCK_MEAN.01, "
    "reviewer-R439 after r440; experiments-side, NO ledger row): "
    "19/19 full / 19/19 smoke; SPEC_SHA bc5644a9924f2eab; "
    "LEMMA SATZ kappa^dagger = 1{q^dagger > 1} (Q q=263/450; "
    "w9 three-way 0 at 1e-15; selected 6/6; dead chi 6/6).  "
    "Source q^dagger = (1/Bw) b^T (I-C)^{-1} b residual 1.2e-15.  "
    "Selected q^dagger 0.891..0.962 mean 0.931794 NOT falling "
    "(k=5 dip then rise); EXT-6 mean 0.964; core-42 42/42 q<1 "
    "mean 0.961 min 0.908 max 0.9985 (kz16), 4 near>0.99 still "
    "living.  UNSIGNED |b|-envelope w9=38.5; |sigma| kz17=2.10 "
    "kz116=87 REFUTED as <1 majorant.  MI2 4e-15; soft trG/M2 "
    "blind.  k=8 not rebuilt.  First measured in /tmp "
    "(r442_cal.py, r442_cal2.py) then sealed (disclosed).  "
    "Full wall 39.1 s.  Builder fallback NOT taken.  AUSGANG "
    "REDUZIERT / DICTIONARY_EXACT / UNSIGNED_MAJORANT_REFUTED / "
    "SELECTED_POINTWISE_CENSUS / MEAN_BOUND_OPEN.  Companion "
    "rh/problem/block_mean.tex + verify_block_mean.py 8/8 "
    "BLOCK MEAN VERIFIED.  NO L* claim, NO R-dagger claim, "
    "NO RH claim"
)

_R443_STATUS = (
    "selected delta floor "
    "(round 443, PRIME.RDAGGER.DELTA_FLOOR_SELECTED.01, "
    "r421 floor in the r442/r433 coordinate; experiments-side, "
    "NO ledger row): 17/17 full / 17/17 smoke; SPEC_SHA "
    "80a676a7c804bdc8; CHART SATZ delta = R + tau-correction "
    "(Q P1 sch=-2/3 VAC -7/6; selected 6/6 residual 0).  "
    "k=6,7 VAC rest P1; tau^2 -> 0 so delta tracks R.  "
    "AIC k=5..9 no k8: M1 delta_inf=+0.02670 DeltaAIC 6.0 "
    "(R_inf=+0.02911; with k=8 pin 0.02982 r421 replay).  "
    "Full k=3..9 prefers M3 (k=5 bump).  vs N winner M2 "
    "(r427 illegal).  EXT-6 delta [0.02636, 0.04519].  "
    "kz16 delta=0.00151 << 0.027 (R<0).  Dead CHI3-15 "
    "delta=-0.023.  k=8/10+ not rebuilt (k=10 border_chain "
    "timeout 20s; CG never reached).  First measured in "
    "/tmp (r443_cal.py, r443_cal2.py) then sealed.  Full "
    "wall 30.7 s.  AUSGANG REDUZIERT / CHART_EXACT / "
    "SLICE_FLOOR_PREFERRED / FULL_SEQUENCE_UNSETTLED / "
    "KZ16_SELECTED_SPECIFIC / DEEP_LOCKED / COFINAL_OPEN.  "
    "Companion rh/problem/delta_floor.tex + "
    "verify_delta_floor.py 6/6 DELTA FLOOR VERIFIED.  "
    "NO L* claim, NO R-dagger claim, NO RH claim"
)

_R444_STATUS = (
    "signed border mean "
    "(round 444, PRIME.RDAGGER.SIGNED_BORDER_MEAN.01, "
    "last analytic object of the RH path after r442; "
    "experiments-side, NO ledger row): "
    "21/21 full / 21/21 smoke; SPEC_SHA 16ac676cfc571660; "
    "TRIPLE SUM SATZ q^dagger = sum_{a,a'} (sigma_a sigma_a'/Bw) "
    "<phi(t_a),(I-C)^{-1} phi(t_a')> (Q 9=5+4; w9 recon 1.4e-16).  "
    "POLE/REG SATZ (Q 10/3=2+4/3; selected residual 1e-12).  "
    "POLE_NOT_CARRIER: selected pole share <= 0.0031, mean "
    "q_pole=8.6e-4; q_reg IS q (0.928->0.962); near-1 cluster "
    "k=9 n=65 share 0.008.  DIAGONAL_OVERFLOWS from k=7 "
    "(q_diag 2.27 / 40.78; mean 7.629>1); q_off load-bearing "
    "(-1.33 / -39.82).  corr(K_off, cos dlog)=0.026.  "
    "DEAD_CHI 6/6 pole overshoot (q_reg<1, q_pole>1-q_reg); "
    "drop-pole mutant false life.  Unsigned 38.49 / 2.10 / 87.1 "
    "r442 regression.  Bound inventory: diag/CS/MVT/Gallagher "
    "unconditional fail; pole-sum reduction REFUTED; missing "
    "signed strength is regular off-diagonal cancellation "
    "matching q_diag growth against a window-dependent OP "
    "kernel (not k(log n/n')) -- ZIRKULAER, second verdict "
    "after r399.  First measured in /tmp (r444_cal.py, "
    "r444_cal2.py) then sealed (disclosed).  Full wall 4.5 s.  "
    "Builder fallback NOT taken.  AUSGANG ZIRKULAER / "
    "TRIPLE_SUM_EXACT / POLE_NOT_CARRIER / DIAGONAL_OVERFLOWS / "
    "OFFDIAG_LOADBEARING / DEAD_CHI_POLE_OVERSHOOT.  Companion "
    "rh/problem/signed_border_mean.tex + "
    "verify_signed_border.py 8/8 SIGNED BORDER MEAN VERIFIED.  "
    "NO L* claim, NO R-dagger claim, NO RH claim"
)



_R445_STATUS = (
    "deep builder "
    "(round 445, PRIME.INFRA.DEEP_BUILDER.01, unlock "
    "border_chain_pack for selected k=10/11/12; "
    "experiments-side, NO ledger row): "
    "25/25 full / 24/24 smoke; SPEC_SHA 57831e610b545e75; "
    "HOTSPOT unused Lanczos in HS.window_data "
    "(k=10 20.57 s = the r443 wall; slim atoms 0.18 s; "
    "chain 0.29 s).  Bit-gate k=3..9 |dq|=0 at 1e-12 "
    "(atoms bitwise vs HS.window_data; numpy canonical).  "
    "numba ulp k=9 |dq|=5.6e-9 bar 1e-8.  "
    "k=8 LIVE CROSS: R=0.047628 den=1.568548 Sig=0.383825 "
    "P1, r421 pin CONFIRMED, r427 circularity closed; "
    "delta=0.047488 q^dagger=0.952512 (8.2 s).  "
    "k=10/11/12 NOT ABD-living: k=10 107 sign-flips from "
    "n=3788 (formula-literal delta=0.000419, pos=0.031823); "
    "k=11 839 flips, B_w explodes to 21434 "
    "(delta=0.996548 not a sequence point); k=12 chain "
    "aborts at n=12737 / N=45444.  AIC ABD-ok k=5..9 with "
    "live k=8: M1 delta_inf=+0.02741 DeltaAIC 5.11 (r443 "
    "without k=8: +0.02670 / 6.01) -- slice floor stands, "
    "deep windows do not decide floor vs decay.  Full "
    "k=3..9 still M3.  vs N M2 (r427 illegal).  Dead chi "
    "new-builder delta=-0.023181.  mpmath kz17 1.1e-16.  "
    "First measured in /tmp (r445_cal.py, r445_cal2.py) "
    "then sealed.  AUSGANG INFRA_UNLOCKED / "
    "K8_CROSS_CONFIRMED / DEEP_NOT_ABD_LIVING / "
    "SLICE_FLOOR_PREFERRED / FULL_SEQUENCE_UNSETTLED / "
    "COFINAL_OPEN.  Companion rh/problem/deep_builder.tex "
    "+ verify_deep_builder.py 7/7 DEEP BUILDER VERIFIED.  "
    "NO L* claim, NO R-dagger claim, NO RH claim"
)

_R446_STATUS = (
    "deep ABD adjudication "
    "(round 446, PRIME.INFRA.DEEP_ABD_ADJUDICATION.01; "
    "experiments-side, NO ledger row): "
    "lemma-first, exactly one question -- are the r445 "
    "ABD breaks at selected k=10/11/12 REAL or FLOAT?  "
    "VERDICT REAL.  mpmath k=10 dps 40 full (503 s): "
    "first flip still n=3788, "
    "eta=-7.938908159491412e-14 rel=1.150853124516389e-6, "
    "n_flip=115 pos_ok=False.  dps 60 to n=3793: first "
    "pivot BIT-IDENTICAL.  Sign stable under dps raise "
    "-- not a float64 recurrence artefact (r427 ward "
    "does not rescue).  k=11 first flip same near-null "
    "class (rel 4.81e-8); B_w explosion is signed rho "
    "after flips.  k=12 class ETA_UNDERFLOW (eta=0 at "
    "n=12737 after first flip n=12654).  Mesh: no "
    "ABD-living neighbour of kz197 (193..201) or kz339 "
    "(337..341); last observed living kz=136 (N=1641); "
    "kz=137 already dead.  pp_kz rounding does not move "
    "k=10/11/12 (exact 2^k on U-grid).  Sequence "
    "definition is NOT repairable by small m-variation "
    "at the 2^k anchors -- construction finding.  "
    "r397 cofinality (a_k->inf, Delta_k->0) is not "
    "ABD-cofinality.  r445 slice floor stands "
    "(no new deep delta point).  Dead chi -0.023181.  "
    "k=5/k=8/k=9 mpmath prefix confirms float.  "
    "First measured in /tmp (r446_k10_mp.log, "
    "r446_k10_dps60.json) then sealed.  AUSGANG REAL / "
    "MESH_DOES_NOT_REPAIR / LAST_LIVE_KZ_136 / "
    "K12_ETA_UNDERFLOW / SLICE_FLOOR_STANDS / "
    "COFINAL_ABD_OPEN.  Companion rh/problem/deep_abd.tex "
    "+ verify_deep_abd.py DEEP ABD VERIFIED.  "
    "NO L* claim, NO R-dagger claim, NO RH claim"
)

_R447_STATUS = (
    "exact-atom adjudication "
    "(round 447, PRIME.INFRA.EXACT_ATOM_ADJUDICATION.01; "
    "experiments-side, NO ledger row): "
    "lemma-first, exactly one question -- does the TRUE "
    "k=10 window live when atoms are built in mpmath "
    "from exact integer sources?  VERDICT EXACT_DEAD.  "
    "Exact vs float64 atoms: positions rel 4.44e-16 "
    "(1 ulp), k=10 weights rel 6.33e-15 -- float64-log "
    "/ fold are NOT the source.  k=10 exact-atom chain "
    "dps 50 (530 s): first flip STILL n=3788, "
    "eta=-8.853149582220489e-14 rel=1.255988618504423e-6, "
    "n_flip=115 pos_ok=False.  dps 70 to n=3793: first n "
    "and eta BIT-IDENTICAL.  Divergence vs float chain "
    "rel>1e-8 at n=218 (abs ~1e-15, same sign); no "
    "sign-split.  k=9 exact-atom prefix 80 confirms "
    "float.  kz=137 atoms rel 4.44e-16.  n/N=0.931.  "
    "THIS 2^k family does not feed the frequently "
    "quantifier; other cofinal families are a reviewer "
    "fork.  r445 slice floor stands (no delta_10).  "
    "First measured in /tmp (r447_k10.json, "
    "r447_dps70.json) then sealed.  AUSGANG EXACT_DEAD / "
    "ATOM_ULP_ONLY / FLIP_STABLE_3788 / BAND_ENDS / "
    "SLICE_FLOOR_STANDS / "
    "THIS_FAMILY_FREQUENTLY_FALSIFIED.  Companion "
    "rh/problem/exact_atom.tex + verify_exact_atom.py "
    "EXACT ATOM VERIFIED.  "
    "NO L* claim, NO R-dagger claim, NO RH claim"
)

_R448_STATUS = (
    "exact living band "
    "(round 448, PRIME.INFRA.EXACT_LIVING_BAND.01; "
    "experiments-side, NO ledger row): "
    "lemma-first, exactly one question -- does the "
    "EXACT band live cofinally, and is kz197 a 2^k "
    "resonance?  VERDICT NOT_COFINAL / "
    "COMMENSURABILITY_REFUTED / NEXT_ODD_FAILS / "
    "ZETA_CHAIN_DEATH / LAST_LIVE_136_EXACT.  "
    "Float mesh: kz136 lives; every sampled kz>=137 "
    "is float-dead.  Exact kz230 (generic a=1259) "
    "dies at n=1818 = float, dps 50=70 bit-identical "
    "-- 2^k anchors are not special.  Exact kz170 "
    "dies at n=5515 = float.  Exact kz137 dies at "
    "n=8283 (n/N=0.998), not float 7511 "
    "(location-lie).  kz197 is an in-chain zeta "
    "death (q_N=-1.682, |Z_loc|=0.033 living-small, "
    "|Z|=1.132, n/N=0.931), not a dead-chi pole "
    "overshoot.  Predefined next-odd-after-2^k lives "
    "k<=9, dies k=10; 3*2^{k-1} dies at k=9; 3^k "
    "dies at k=6.  r445 slice floor stands.  First "
    "measured in /tmp then sealed.  Companion "
    "rh/problem/exact_band.tex + verify_exact_band.py "
    "EXACT BAND VERIFIED.  "
    "NO L* claim, NO R-dagger claim, NO RH claim"
)

_R449_STATUS = (
    "flip vs stabilization "
    "(round 449, PRIME.INFRA.FLIP_VS_STABILIZATION.01; "
    "experiments-side, NO ledger row): "
    "lemma-first, exactly one question -- do the "
    "deep-window chain flips sit inside or beyond "
    "n_stab?  VERDICT TAIL_ONLY.  n_stab via "
    "Chebyshev-moment Fenster-Vergleich (skip m0/m1; "
    "eps-robust 1e-6..1e-2): kz136:175 live, "
    "kz137:175 flip 8283, kz170:194 flip 5515, "
    "kz197:406 flip 3788, kz230:194 flip 1818, "
    "kz500:1525 flip 9564.  ALL flips past n_stab. "
    "Prefix-80 q^dagger living, delta in "
    "[0.093,0.129]; r445 slice floor stands.  "
    "Dead CHI3-15 n_flip=0 q=1.023 (edge, no "
    "prefix-hit).  Mincut already consumes "
    "stabilized fullRead; Python ABD-dead is a "
    "tail statement.  First measured in /tmp then "
    "sealed.  Companion rh/problem/flip_vs_stab.tex "
    "+ verify_flip_vs_stab.py FLIP VS STAB VERIFIED.  "
    "NO L* claim, NO R-dagger claim, NO RH claim, "
    "NO anti-RH claim"
)

_R450_STATUS = (
    "prefix mincut "
    "(round 450, PRIME.RDAGGER.PREFIX_MINCUT.01; "
    "experiments-side, NO ledger row): "
    "lemma-first, three questions -- n_stab-compression "
    "delta (not prefix-80), n_stab scaling, Lean name.  "
    "VERDICT M2_UNDECIDED / PREFIX_OBJECT_SPLIT / "
    "NSTAB_GROWS / CHI_PREFIX_LIVES / LEAN_IDENT_RFL.  "
    "Object: r362/r369 pack at n_stab, "
    "B_w = cumsum(rho)[nstar-2]+5/7.  Living full vs "
    "n_stab-delta NOT close (rel 0.97-3.62).  Deep "
    "n_stab-delta 136:0.12908 137:0.09989 170:0.10591 "
    "197:0.11214 230:0.12674 500:0.09287 (N=17847).  "
    "Slice-only M1 +0.02741 stands; mixed and "
    "object-pure n_stab charts prefer M2 (no decided "
    "positive floor).  n_stab ~ 0.0417 a^1.273, "
    "n_stab/N falls 0.021-0.11.  CHI3-15 full q=1.023 "
    "dead; prefix n=40 q=0.863 living (death in last "
    "3 grades).  Lean: "
    "frequently_selected_prefix_augDualResolvent_ge_half "
    "Iff.rfl-identical to the mincut; census stays 5.  "
    "First measured in /tmp then sealed.  Companion "
    "rh/problem/prefix_mincut.tex + "
    "verify_prefix_mincut.py PREFIX MINCUT VERIFIED.  "
    "NO L* claim, NO R-dagger claim, NO RH claim, "
    "NO anti-RH claim"
)


_R451_STATUS = (
    "nstab transition anatomy "
    "(round 451, PRIME.RDAGGER.NSTAB_TRANSITION.01; "
    "experiments-side, NO ledger row): "
    "lemma-first, exactly one question -- what "
    "changes at n_stab?  Three single-window "
    "profiles (conditioning / n_res / q^dagger_n).  "
    "VERDICT TRANSITION_SMOOTH / RES_MISMATCH / "
    "PREFIX_Q_PLATEAU.  n_stab reproduced (r449 "
    "method, eps-robust).  n_res = L/2, "
    "n_stab/n_res in [0.010, 0.094] on 13 windows "
    "(RES_MISMATCH; prefix bandlimited).  OP "
    "beta~1/2 through n_stab, no Christoffel cliff.  "
    "q^dagger_n CONSTANT on n<=n_stab of EVERY "
    "window (std<1e-4, q*<1), including kz137/"
    "170/500.  Exit not universal: CLIFF at "
    "n_stab+1 on {17,116,136,197,230,500}; "
    "DELAYED on {5,9,26,43}; CONTINUES past "
    "2 n_stab on {69,137,170}.  SCRAMBLE "
    "(theta-jitter) kills the plateau (n_stab->2, "
    "q wanders, n_res blows up).  n_stab is a "
    "sufficient operational cut, not a unique "
    "mechanical cliff.  First measured in /tmp "
    "then sealed.  Companion "
    "rh/problem/nstab_transition.tex + "
    "verify_nstab_transition.py NSTAB TRANSITION "
    "VERIFIED.  "
    "NO L* claim, NO R-dagger claim, NO RH claim, "
    "NO anti-RH claim"
)

_R452_STATUS = (
    "plateau theorem "
    "(round 452, PRIME.RDAGGER.PLATEAU_THEOREM.01; "
    "experiments-side, NO ledger row): "
    "lemma-first SATZ attack on the r451 Schur "
    "plateau (names the plateau, not a kink).  "
    "VERDICT PLATEAU_IDENTITY_PROVED / "
    "QSTAR_UNDECIDED.  Grade-0 evaluation of "
    "the exact pack: b0 = M_d/sqrt(mu_0), "
    "C00 = nu_0/mu_0, B_w = M_d+5/7 on "
    "rho-tail 0, hence "
    "q_* = M_d/(M_d+5/7) whenever "
    "M_d = mu_0-nu_0 (every kz>=69, residual "
    "<5e-5).  A(i) chain-zero REFUTED "
    "(|Cb|/|b|~0.09).  A(ii) value law "
    "REFUTED (sister 136/137: m>=2 rel "
    "1.88e-9, same n_stab=175, q* differs "
    "by 0.029; value is M_d 4.817 vs 6.436).  "
    "Constancy <=> rho_n=0 (CLIFF is the "
    "first rho!=0; 137 continues).  q* trend "
    "is M_d growing; whether M_d is unbounded "
    "stays open (AIC M2 vs a, sister kills "
    "an a-law).  Cofinality of n_stab REDUCED "
    "to degreewise fold-moment convergence "
    "(rel_m2 ~ 2.06e-4 a^{-1.90}).  SCRAMBLE "
    "kills latch and plateau.  First measured "
    "in /tmp then sealed.  Companion "
    "rh/problem/plateau_theorem.tex + "
    "verify_plateau_theorem.py PLATEAU THEOREM "
    "VERIFIED.  "
    "NO L* claim, NO R-dagger claim, NO RH claim, "
    "NO anti-RH claim"
)

_R453_STATUS = (
    "border mass inequality "
    "(round 453, PRIME.RDAGGER.BORDER_MASS_INEQUALITY.01; "
    "experiments-side, NO ledger row): "
    "lemma-first, the r452 SATZ turns the prefix "
    "mincut into err(rho) <= (5/7)/(M_d+5/7).  "
    "VERDICT BOUND_PROVED / "
    "MASS_CLASSICAL_REDUCED_GROWING / RACE_WON.  "
    "Exact pack identity q_n = S_{n-1}/B_w and "
    "delta = (5/7-rho_n)/B_w (residual <=5e-14), "
    "hence q_n<1 <=> rho_n<5/7 and the first-leak "
    "increment is g = rho_n/B_w (sister CLIFF "
    "predicted exactly; 137 CONTINUES).  M_d is "
    "the signed folded m_0 (MAIN equality on "
    "kz>=69), grows with log N (corr 0.992; "
    "sister is N not a).  At fixed n in "
    "{20,40,80,160} err/margin <= 3e-5 on the "
    "plateau (RACE_WON).  First measured in /tmp "
    "then sealed.  Companion "
    "rh/problem/border_mass.tex + "
    "verify_border_mass.py BORDER MASS VERIFIED.  "
    "NO L* claim, NO R-dagger claim, NO RH claim, "
    "NO anti-RH claim"
)

_R454_STATUS = (
    "limit object "
    "(round 454, PRIME.RDAGGER.LIMIT_OBJECT.01; "
    "experiments-side, NO ledger row): "
    "lemma-first, the r453 cofinal collapse "
    "(prefix h>0 and rho_n<5/7) is a property "
    "of a limit object once the folded moments "
    "converge degreewise.  "
    "VERDICT LIMIT_CLASSICAL / "
    "LIMITCHAIN_ALIVE_200 / CHAIN_DOCUMENTED.  "
    "For j>=2, m_inf[j] = m_ARCH[j] (MAIN-ARCH "
    "break == n_stab on kz17/116/136; deep "
    "windows agree through the computed prefix).  "
    "PNT-world (same fold, comb -> dpsi~e^u du) "
    "agrees at 7.7e-6 (kz17) / 5.9e-11 (kz137); "
    "ARCH agrees at 1e-15.  m0,m1 have no finite "
    "limit (arch mass grows).  rho_j(inf)=0 +/- "
    "1e-4 through j=200 (worst measured 7.3e-6 "
    "on kz197); mu-chain h0>0 min b>0 through "
    "200 on kz500.  [L1] MEASURED, [L2] MEASURED "
    "(Lipschitz dq/dm_2 ~ 0.09), [L3] MEASURED "
    "for j<=200 / OPEN as a theorem.  First "
    "measured in /tmp then sealed.  Companion "
    "rh/problem/limit_object.tex + "
    "verify_limit_object.py LIMIT OBJECT "
    "VERIFIED.  "
    "NO L* claim, NO R-dagger claim, NO RH claim, "
    "NO anti-RH claim"
)

_R455_STATUS = (
    "arch chain theorem "
    "(round 455, PRIME.RDAGGER.ARCH_CHAIN_THEOREM.01; "
    "experiments-side, NO ledger row): "
    "lemma-first, the ARCH fold is the 3-lag "
    "identity m_j = -1/2 c_{j-1}+c_j-1/2 c_{j+1}, "
    "not a named Jacobi family.  "
    "VERDICT L3_PROVED / L1_PNT_SUFFICIENT / "
    "CHAIN_MAPPED.  "
    "[L1] is elementary: c^P_i=0 for "
    "(i+1)Delta < log 2, so MAIN=ARCH through "
    "J_P-2; n_stab=J_P-1 on "
    "{17,116,136,197,230,500}.  "
    "PNT is surplus (PNT-ARCH >> MAIN-ARCH).  "
    "NOT RH_CIRCULAR.  "
    "[L3] h>0 classical on the mu-chain; "
    "rho_n=0 on 1..J_B-1 with "
    "J_B=BG_DU/Delta (smooth_comb starts at "
    "0.01); rho_0=M_d is the exception.  "
    "Eventual per fixed n.  "
    "First measured in /tmp then sealed.  "
    "Companion rh/problem/arch_chain.tex + "
    "verify_arch_chain.py ARCH CHAIN VERIFIED.  "
    "NO L* claim, NO R-dagger claim, NO RH claim, "
    "NO anti-RH claim"
)

_R456_STATUS = (
    "prefix vacuity red-team "
    "(round 456, PRIME.RDAGGER.VACUITY_REDTEAM.01; "
    "experiments-side, NO ledger row): "
    "adversarial worlds test of the r450-r455 "
    "prefix-mincut.  VERDICT VACUOUS_CONFIRMED.  "
    "Lean consumption is the full-cap cone "
    "(selectedWindowConeSemidef at W.cap, combHankel) "
    "plus fullRead = arch-comb+pole; the meshExp "
    "guard is a mesh filter on f, not n_stab.  "
    "r450 Iff.rfl is a naming, not a truncation.  "
    "MAIN vs ARCH-only, identical fold: prefix "
    "q^dagger world-blind (kz69 n_stab dq=3.33e-16; "
    "kz17 n=8 dq=2.22e-16); arithmetic onset at "
    "J_P (kz17 dq=0.05166; kz69 n_f dq=0.005698).  "
    "combRead tent U=2 is 1.7458508391553806 "
    "(n=2,3,4,5,7); U=0.5 is 0.  M_d is arch mass.  "
    "r455 eventually-per-n covers the blind zone, "
    "not U_f/Delta.  Honest object = R^dagger at "
    "depth ~U_f/Delta, or full cap for forall f.  "
    "TAIL_ONLY vs U=2 stands; vs forall f it fails.  "
    "r449-r455 retyped as prime-blind anatomy "
    "(r303 dictionary).  First measured in /tmp "
    "then sealed.  Companion "
    "rh/problem/vacuity_redteam.tex + "
    "verify_vacuity_redteam.py VACUITY REDTEAM "
    "VERIFIED.  "
    "NO L* claim, NO R-dagger claim, NO RH claim, "
    "NO anti-RH claim"
)

_R457_STATUS = (
    "J_P increment "
    "(round 457, PRIME.RDAGGER.JP_INCREMENT.01; "
    "experiments-side, NO ledger row): "
    "accepts r456 VACUOUS_CONFIRMED; studies "
    "MAIN-ARCH from J_P to full cap.  "
    "VERDICT INCREMENT_DRIFT / RACE_EATS_K10 / "
    "LEMMA_REDUCED.  "
    "kz17 post-J_P Delta rho 77/77 positive "
    "(drift, not cancellation); cliff dq=0.05166.  "
    "ARCH full-cap signed pack is ill-conditioned; "
    "baseline is q* at J_P.  Race Delta q/(1-q*): "
    "0.49..0.78 ALIVE on kz17/69/116/136; 0.996 "
    "EATS margin at k=10 (kz197); 2.16 overshoot "
    "kz230.  Death is accumulated (flip 3788 >> "
    "J_P=407).  Reduction is r453 at cap on "
    "j>=J_P; NOT r429 Z_loc alias.  Cofinal "
    "(1-eps) race REFUTED by k=10.  SCRAMBLE "
    "q(30)>1.  First measured in /tmp then sealed.  "
    "Companion rh/problem/jp_increment.tex + "
    "verify_jp_increment.py JP INCREMENT VERIFIED.  "
    "NO L* claim, NO R-dagger claim, NO RH claim, "
    "NO anti-RH claim"
)

_R458_STATUS = (
    "cofinal family "
    "(round 458, PRIME.RDAGGER.COFINAL_FAMILY.01; "
    "experiments-side, NO ledger row): "
    "lemma-first, three questions -- Lean-admissible "
    "(a,m) requirements, living census, candidate "
    "family.  VERDICT FAMILY_CANDIDATE / "
    "TABLE_CAP_ARTEFACT / RESIDUAL_DEEP_DEATH.  "
    "Selected.lean: any prime-power a_k->inf, "
    "m_k->inf covers; named a_k=2^k, "
    "m_k=k*2^{floor sqrt k}-1.  Sealed SCAN_KZ "
    "76 windows BEFORE first pack: capped frame-A "
    "55 live / 21 dead, wall a=631/641 "
    "(=sqrt TABLE_CAP).  Holdout a<=631 is 19/19 "
    "on the capped chart; N<=1641 fails (14/19).  "
    "Lean-native selectedMesh k=5..16 all cap-live "
    "(k=10 q=0.9319618718590412).  Full a^2 comb "
    "revives kz197 (2^10) and kz230 (exact dps=50 "
    "n_flip=0); Lean k=10 q unchanged.  kz137 "
    "stays dead at N=8300 (first 7308).  r329 "
    "EXT3 was F_A/cubic, not q^dagger.  First "
    "measured in /tmp then sealed.  Companion "
    "rh/problem/cofinal_family.tex + "
    "verify_cofinal_family.py COFINAL FAMILY "
    "VERIFIED.  "
    "NO L* claim, NO R-dagger claim, NO RH claim, "
    "NO anti-RH claim"
)

_R459_STATUS = (
    "fullcomb cleanup "
    "(round 459, PRIME.RDAGGER.FULLCOMB_CLEANUP.01; "
    "experiments-side, NO ledger row): "
    "lemma-first, three contaminated findings.  "
    "VERDICT RACE_TREND_BROKEN / "
    "LEANFAM_EXACT_ALIVE(12) / "
    "KZ137_OUTSIDE_MINCUT.  "
    "r457 race at kz197/230 ran on TABLE_CAP=4e5; "
    "full a^2 comb: 17=0.493 69=0.539 116=0.713 "
    "136=0.784 138=0.759 197=0.724 230=0.770 "
    "(all <1, monotone broken after 136; fit M2; "
    "only-old M1).  Lean selectedMesh k=5..12 "
    "race in 0.607..0.758, not to 1; exact dps=50 "
    "n_flip=0 at k=10,11,12; k=14 a^2 budget limit.  "
    "kz137 inventory complete ka=34856/34856 still "
    "dead (pack n_flip=103, mass-chain first 7308); "
    "Lean a=641 selectedMesh k=9/10 lives "
    "(race 0.453/0.534) -- death is frame-A "
    "gap-coupling, outside the mincut.  "
    "First measured in /tmp then sealed.  Companion "
    "rh/problem/fullcomb_cleanup.tex + "
    "verify_fullcomb_cleanup.py FULLCOMB CLEANUP "
    "VERIFIED.  "
    "NO L* claim, NO R-dagger claim, NO RH claim, "
    "NO anti-RH claim"
)

_R460_STATUS = (
    "race proof attempt "
    "(round 460, PRIME.RDAGGER.RACE_PROOF_ATTEMPT.01; "
    "experiments-side, NO ledger row): OUTCOME PARTIAL.  "
    "PROVED exact spectral race identity "
    "q=sum |<u,e_j>|^2/(1-lambda_j), Schur equivalence, "
    "two-band sufficient criterion, and fixed-r plateau "
    "cardinality 2r+1.  Full a^2 comb k=5..12: "
    "29/29 full gates; race 0.607..0.758; raw norm "
    "upper bound 4.825..4991.649 and Gershgorin negative "
    "on all rows; optimized two-band certificate succeeds "
    "only at k=5 (0.910<1), fails k=6..12; full-depth "
    "ARCH chain flips 3..8 times.  Exact remaining gap: "
    "source-derived control of the normalized border "
    "vector's spectral measure near lambda=1 for infinitely "
    "many selected k.  Raw norm/Gershgorin acknowledged as "
    "r387/r429 majorant aliases, not new mechanisms.  "
    "First measured in /tmp then sealed.  Companion "
    "rh/problem/race_proof.tex + verify_race_proof.py "
    "RACE PROOF ATTEMPT VERIFIED -- OUTCOME PARTIAL.  "
    "NO L* claim, NO R-dagger claim, NO RH claim, "
    "NO anti-RH claim"
)

_R461_STATUS = (
    "narrow-band Weil consistency probe "
    "(round 461, PRIME.RDAGGER.NARROWBAND_WEIL.01; "
    "experiments-side, NO ledger row): "
    "VERDICT FORK_SHARPENED.  GridElement is an even dyadic "
    "piecewise-linear autocorrelation; the formal endpoint is "
    "forall GridElement, weilForm>=0, not RH.  The spectral/zero "
    "side and density/continuity completion are absent; the "
    "historical endpoint takes unasserted "
    "`ArchGaussMellinDigammaIdentity` explicitly plus the named "
    "`SelectedACapPsdImpliesPlainReads` bridge; no arch sorryAx.  "
    "In the r459 builder "
    "U_k=N_k Delta_k=k log(2)/2 and L_k=U_k/2; k=5..12 gives "
    "U=1.732868..4.158883, beyond both the classical U<log(2) "
    "prime-blind range and the recent arXiv:2608.24827 U<=1.6 "
    "certificate from k=5 onward.  Conditional depth counts are "
    "1,3,5,7,18,22,26,30; race remains 0.606566..0.757783.  "
    "Completed mincut translation: cofinal compact-window Weil "
    "positivity, equivalent to the full Weil criterion after the "
    "missing dictionary.  First measured in /tmp then sealed.  "
    "Companion rh/problem/narrowband_weil.tex + "
    "verify_narrowband_weil.py NARROWBAND WEIL VERIFIED.  "
    "NO L* claim, NO R-dagger claim, NO RH claim, NO anti-RH claim.  "
    "r638L G14 text gate updated after root-cause reproduction; "
    "smoke 21/21 twice byte-identical; SPEC_SHA "
    "ff617711041fee52fe2ebdc9a54ddaf4f0b0ccc30933506c34e809e1bae7d59a; "
    "no RH claim"
)

_R462_STATUS = (
    "end-to-end gap map (historical sealed diagnostic) "
    "(round 462, PRIME.RDAGGER.ENDTOEND_GAPMAP.01; "
    "experiments-side, NO ledger row): "
    "VERDICT HIDDEN_GAP_FOUND.  Adversarial audit of the "
    "FrequentlySelected->RH route: the literal Lean "
    "ExactPrimeSource/ExactFold/combHankel object disagreed with "
    "the production Python builder at k=5,9,10 and the minimal "
    "proof-path declarations were misaligned.  First measured in "
    "/tmp then sealed (gapmap_probe.py smoke 15/15, SPEC_SHA "
    "80439f55924ba591).  Companion rh/problem/endtoend_gapmap.tex + "
    "verify_gapmap.py.  NOT rerun in run_rh: r463 invalidates the "
    "old success condition by repairing the Lean object; row kept "
    "as sealed historical diagnostic only.  NO L* claim, NO R-dagger "
    "claim, NO RH claim, NO anti-RH claim"
)

_R463_STATUS = (
    "Lean fidelity repair probe "
    "(round 463, PRIME.RDAGGER.LEAN_FIDELITY_REPAIR.01; "
    "experiments-side, NO ledger row): "
    "VERDICT FAITHFUL_OBJECT_PINNED / BRIDGES_TYPED / CENSUS_8.  "
    "Independent numerical mirror of RH/FaithfulFold.lean at "
    "k=5,9,10 (11/11 smoke/full gates, SPEC_SHA 0ef28519b5969b8a).  "
    "FaithfulFold replaces the raw-atom cosine fold with the "
    "production pipeline; archRead is concrete lag pairing.  "
    "Endpoint renamed internal_weil_nonneg_of_frequently_selected; "
    "RH/ExternalBridges.lean types dense extension, explicit-formula "
    "identification, and Mathlib RiemannHypothesis as honest sorry "
    "candidates (Lean sorry census 5->8).  First measured in /tmp "
    "then sealed.  Companion rh/problem/lean_fidelity.tex + "
    "verify_lean_fidelity.py LEAN FIDELITY REPAIR VERIFIED (9/9).  "
    "NO L* claim, NO R-dagger claim, NO RH claim, NO anti-RH claim"
)

_R464_STATUS = (
    "inner Lean bridges probe "
    "(round 464, PRIME.RDAGGER.INNER_BRIDGES.01; "
    "experiments-side, NO ledger row): "
    "VERDICT FINITE_PSD_CLOSED / ARCH_LAGS_TRANSCRIBED / "
    "TWO_NAMED_REMAINDERS.  The finite implication from an exact "
    "selected-window quadratic representation and A_cap PSD to plain "
    "read nonnegativity is proved.  Production Archimedean near/far "
    "lag integrals are concrete; the remaining analytical seam is "
    "arch_gauss_mellin_digamma_identity.  Smoke 11/11, SPEC_SHA "
    "2ffca3dfca4b23bf; Lean sorry census remains 8.  Companion "
    "rh/problem/inner_bridges.tex + verify_inner_bridges.py "
    "INNER BRIDGES VERIFIED (9/9).  NO L* claim, NO R-dagger claim, "
    "NO RH claim, NO anti-RH claim"
)

_R638L_RESEAL_NOTE = (
    ".  r638L claim-boundary repair retires the overstrong "
    "`arch_gauss_mellin_digamma_identity` and gauge-mismatched "
    "`standard_explicit_formula_identification` asserting theorems "
    "to unasserted Props; historical arch extraction APIs now take "
    "`ArchGaussMellinDigammaIdentity` explicitly; full Lean build "
    "3578 jobs with exactly five sorries; affected text/census "
    "probes were rerun twice byte-identically; no RH claim"
)

_R467_STATUS = (
    "overlap mechanism probe "
    "(round 467, PRIME.RDAGGER.OVERLAP_MECHANISM.01; "
    "experiments-side, NO ledger row): "
    "VERDICT STUCK(QUALITATIVE_ALIGNMENT_REAL; "
    "ABEL_CURRENCY_TOO_COARSE; "
    "SOURCE_TO_BORDER_BASIS_BRIDGE_MISSING).  "
    "Qualitative alignment is real (top MAIN modes "
    "low-frequency, corr +0.745, ARCH aligns, scramble "
    "destroys tiny MAIN alignment), but even measured "
    "exact U_r give Abel band factors 91.7..1.19e5 and "
    "the >1e3 stop gate fires on k=7..12.  u is the "
    "smooth-border functional after the MAIN OP basis "
    "change, not the raw prime-lag vector.  Smoke "
    "17/17, SPEC_SHA 7ec07cccc7372ba9, commit "
    "a0e9aa4d.  Companion "
    "rh/problem/overlap_mechanism.tex + "
    "verify_overlap_mechanism.py OVERLAP MECHANISM "
    "NOTE VERIFIED -- VERDICT STUCK.  "
    "NO L* claim, NO R-dagger claim, NO RH claim, "
    "NO anti-RH claim"
)

_R468_STATUS = (
    "octave renormalization "
    "(round 468, PRIME.RDAGGER.OCTAVE_RENORMALIZATION.01; "
    "experiments-side, NO ledger row): "
    "VERDICT OCTAVE_NOT_CAUCHY / EDGE_TWO_POINTS / "
    "REDUCTION_ALIAS.  Live source is n<a (r465 tents "
    "vanish for n>=a), not the a^2-octave.  Active-octave "
    "weight and Rosser-Schoenfeld psi bound both grow; "
    "isolated octave at k=11 moves q by +0.220 while "
    "total dq is -0.012.  Intra dq oscillates through "
    "k=15.  Block edges 8->9 (+0.045) and 15->16 "
    "(+0.018) are two points, not a 2^{-r} law.  "
    "r-sequence: 9->10 is intra r=3.  New k=13..16 "
    "interval-certified live.  Quantifier cut is an "
    "alias (r303).  Smoke 24/24, SPEC_SHA "
    "0e693815a86ef0ff.  Companion "
    "rh/problem/octave_renorm.tex + "
    "verify_octave_renorm.py OCTAVE RENORM VERIFIED.  "
    "NO L* claim, NO R-dagger claim, NO RH claim, "
    "NO anti-RH claim"
)

_R469_STATUS = (
    "correlation wall judgment "
    "(round 469, PRIME.RDAGGER.CORRELATION_WALL_JUDGMENT.01; "
    "adjudication note, NO probe, NO census, NO ledger row): "
    "VERDICT U1 INTERNALLY_EXHAUSTED / U2 EXTEND_AND_REFRAME / "
    "U3 REDIRECT_TO_FIXED_L.  U1: eight candidate languages "
    "adjudicated (self-consistency/fixed point, transfer "
    "operator/thermodynamic formalism, microlocal/semiclassical, "
    "determinantal/Fredholm, Sarnak-Mobius disjointness, free "
    "probability, Loewner/Christoffel minorant, quantifier "
    "renormalization); only the microlocal candidate survives the "
    "new methodological scramble filter, and executing it needs "
    "the retained RHP polynomial asymptotics plus power-saving "
    "cancellation for sum Lambda(n) n^{-1/2+it}.  Two sealed "
    "restatements are supplied as diagnosis: the dual extremal "
    "form of q-dagger (dossier A5 in Christoffel/Markov "
    "coordinates, extremizer = omega-Riesz representer of the "
    "smooth border functional) and the determinant ratio "
    "1-q = det A / det(I-C); both explain why every pairing bound "
    "loses the measured 10^2..10^5 and why that slack matches the "
    "r467 scramble factor 28.5..5.3e5.  r461 nestedness is "
    "restated judicially: the cofinal target is, modulo the named "
    "bridges, the full Weil criterion, hence not a lemma.  Core "
    "closed for rounds; resources redirected to the fixed-L "
    "unconditional classical lane "
    "(SelectedReadQuadraticRepresentation, "
    "arch_gauss_mellin_digamma_identity, fixed-support "
    "density/continuity) and to the external package.  Binding "
    "anti-list with a mandatory scramble gate.  No probe, no new "
    "theorem, no new census.  "
    "NO L* claim, NO R-dagger claim, NO RH claim, NO anti-RH claim"
)

_R470_STATUS = (
    "quadratic representation obstruction "
    "(round 470, PRIME.RDAGGER.QUADREP.01; "
    "experiments-side, NO ledger row): "
    "VERDICT OBSTRUCTION_SEALED.  F1(i) of the r469 U3 directive.  "
    "SelectedReadQuadraticRepresentation is retained unweakened "
    "(meshExp guard only, steps unbounded).  Lean proves "
    "exists_mesh_compatible_steps_gt_cap (k=5, meshExp=19, "
    "steps=11, cap=10) and "
    "quadraticRepresentation_refuted_of_negative_read.  "
    "Named obstruction SelectedOnsetCompatibleNegativeRead: "
    "at k=5 an onset-compatible GridElement (meshExp=3, steps=24, "
    "elementAnchor=21<=32) has native Hessian rank 24 > cap+1=11 "
    "with lambda_min(T)=-0.042885425277 (2 negative eigenvalues) "
    "while A_cap is PD (lambda_min=6.61842e-8, qdag=0.877898027321).  "
    "A negative native read cannot be a quadratic value of a PSD "
    "cap.  Smoke 10/10, SPEC_SHA 74de4e263ac7fd7b; Lean sorry "
    "census remains 8.  Companion rh/problem/quadrep.tex + "
    "verify_quadrep.py QUADREP VERIFIED (6/6).  "
    "NO L* claim, NO R-dagger claim, NO RH claim, NO anti-RH claim"
)

_R471_STATUS = (
    "classical Guinand-Weil grid certificates "
    "(round 471, PRIME.RDAGGER.CLASSICAL_CERT.01; "
    "experiments-side, NO ledger row): "
    "VERDICT GRID_CERTIFIED(L_max=2.7726).  F2 of the r469 U3 "
    "directive.  Dictionary-free Q(g)=A-P+Pi on piecewise-constant "
    "h supported in [-L,L]; interval Toeplitz Q_L; validated "
    "Cholesky.  Calibration L=0.8 green (n=8,16,24); Yoshida/"
    "Bombieri L=0.30 green; then L_5, 1.0..2.0, L_8, L_12, L_16 "
    "all GRID_CERTIFIED.  Type is NEVER lambda_*(L)>=0; gap named "
    "F2b (modulus of continuity at fixed L).  Scramble-sensitive "
    "(literal log n).  Smoke 14/14, full 25/25, SPEC_SHA "
    "18eb2a33651585f5.  Companion rh/problem/classical_cert.tex + "
    "verify_classical_cert.py CLASSICAL CERT VERIFIED -- "
    "GRID_CERTIFIED(L_max=2.7726).  "
    "NO L* claim, NO R-dagger claim, NO RH claim, NO anti-RH claim"
)

_R473_STATUS = (
    "extraction-joint redesign "
    "(round 473, PRIME.RDAGGER.EXTRACTION_JOINT_REDESIGN.01; "
    "experiments-side, NO ledger row): "
    "VERDICT ARTEFACT + POLY_BRIDGE_PROVED.  F1 foundation after "
    "the r470 obstruction, under the r469 U3 contract.  At the "
    "k=5 sealed witness, classical Q(g_f)=+0.0769078530458283 "
    "while fullRead=-0.0428854252772195; the gap is the arch "
    "tent error 0.1197932783230478 (comb exact, pole native, "
    "ghat_min>0).  Lean proves selectedACapPsdImpliesPolynomialReads "
    "(PSD A_cap => deg<cap reads >=0; PrimeWindow.hankel_quadform) "
    "and fullRead_weilForm_gap_eq_arch.  Named outer bridge "
    "SelectedPolynomialApproximatesGrid.  Redesigned joint "
    "FrequentlySelectedPolynomialJoint; fixed-k readout "
    "weilForm >= -2 err_arch.  Historical FREQ endpoint retained.  "
    "No infinitely-many-k statement.  Smoke 13/13, SPEC_SHA "
    "0650125bd812c1f8; Lean sorry census remains 8.  Companion "
    "rh/problem/extraction_joint.tex + verify_extraction_joint.py "
    "EXTRACTION JOINT VERIFIED (6/6).  "
    "NO L* claim, NO R-dagger claim, NO RH claim, NO anti-RH claim"
)

_R474_STATUS = (
    "classical Weil modulus upgrade "
    "(round 474, PRIME.RDAGGER.MODULUS_UPGRADE.01; "
    "experiments-side, NO ledger row): "
    "VERDICT PARTIAL.  F2b of the r469 U3 directive.  "
    "Lemmas PROVED: C_P=2 S_eff(L) with S_eff exact and "
    "zero at L=0.3; C_Pi=8 sinh(L); Jackson 1/pi^2 and "
    "1/pi on H^2 interpolants; combination implication "
    "R_grid > omega => Q >= (R-omega)||h||^2 on the first "
    "Dirichlet H^2 ball.  Quantitative close STUCK: every "
    "sealed mesh is SHORT, including YB L=0.3 "
    "(omega 0.140 vs R_grid 0.0083).  Modulus too crude "
    "(arch 1/w on the first-order cross term).  "
    "Smoke 11/11, full 21/21, SPEC_SHA 45db1c92384913e8.  "
    "Companion rh/problem/modulus_upgrade.tex + "
    "verify_modulus_upgrade.py MODULUS UPGRADE VERIFIED -- "
    "PARTIAL.  NO L* claim, NO R-dagger claim, NO RH claim, "
    "NO anti-RH claim"
)

_R475_STATUS = (
    "arch identity isolation and tent rate "
    "(round 475, PRIME.RDAGGER.ARCH_IDENTITY_AND_RATE.01; "
    "experiments-side, NO ledger row): "
    "VERDICT IDENTITY_ISOLATED + RATE_O_DELTA2 (numeric large-support) "
    "+ FIXED_CONSTANT_FALSIFIED (r475-repair).  F1(ii) not closed "
    "as exact equality: productionArchDelta_tendsto_atTop proved "
    "(Delta = log a/(m+1) -> +infty at fixed m); Mathlib v4.29.1 "
    "still lists Gauss integral as TODO, isolated as named Prop "
    "GaussDigammaIntegralRepresentation (not a sorry).  "
    "weilArchSide is now the concrete u-space pairing.  "
    "O(Delta_k^2) rate numerically supported (ratios 3.85-3.99 on "
    "k=5-12); fixed archRateConst = 4(1+1/64)^2 = 4.1259765625 "
    "FALSIFIED in the small-support regime (steps=1, meshExp=6, "
    "x0=1: err/Delta^2 = 8.0283458222 > 4.1259765625; Lean-certified "
    "endpoint-kink defect -theta(1-theta)/2).  Named Prop "
    "SelectedArchErrorQuadraticRate kept with falsification comment; "
    "correct interface is SelectedArchErrorQuadraticRateExists "
    "(exists C(f)); selectedArchError_tendsto_zero_of_rateExists "
    "proved; SelectedArchWeightedInterpolationEstimate OPEN.  "
    "Witness table k=5..12: err=0.119793278323 at Delta=0.1732867951 "
    "(k=5..8, err/D2=3.9893) and err=0.028876619985 at "
    "Delta=0.0866433976 (k=9..12, err/D2=3.8466).  "
    "Smoke 9/9, SPEC_SHA e8a49c5895d3d382; Lean sorry census "
    "remains 5 (five protected).  Companion rh/problem/arch_rate.tex + "
    "verify_arch_rate.py ARCH RATE VERIFIED (6/6).  "
    "NO L* claim, NO R-dagger claim, NO RH claim, NO anti-RH claim"
)

_R475_REPAIR_STATUS = (
    "Lean repair of the r475 fixed-constant rate "
    "(round r475-repair, Lean-only, NO sealed probe, NO ledger row): "
    "RH/SelectedArchErrorQuadraticRateClassical.lean (238 lines).  "
    "SelectedArchErrorQuadraticRate (fixed archRateConst = "
    "4(1+1/64)^2 = 4.1259765625) FALSIFIED in the small-support "
    "regime (steps=1, meshExp=6, x0=1: err_arch/Delta^2 = "
    "8.0283458222 > 4.1259765625; also 4.4488, 7.13-7.24).  "
    "endpointKink_cell_integral_defect proved exactly "
    "(-theta(1-theta)/2); meshSix_endpointCoefficient_exceeds_archRateConst "
    "proved; intervalIntegral_affineInterpolation_error_le_one_twelfth "
    "proved; selectedArchGridEndpoint corrected to (floor(b/Delta)+1)*Delta "
    "(numerical identity with selectedArchError to 2.3e-25).  "
    "SelectedArchErrorQuadraticRateExists (exists C(f)) is the "
    "correct interface; selectedArchError_tendsto_zero_of_rateExists "
    "proved; SelectedArchWeightedInterpolationEstimate OPEN.  "
    "O(Delta^2) rate itself not refuted (large-support ratios "
    "3.9893 / 3.8466).  lake build 3578 jobs green; five protected "
    "sorries unchanged.  Catalog part_18 KILLED/LOSSY_CONSTANT.  "
    "NO L* claim, NO R-dagger claim, NO RH claim, NO anti-RH claim"
)

_R476_STATUS = (
    "classical Weil crossterm sharpening "
    "(round 476, PRIME.RDAGGER.CROSSTERM_SHARPENING.01; "
    "experiments-side, NO ledger row): "
    "VERDICT UNCONDITIONAL(L_max=2.7726) on the first "
    "Dirichlet H^2 ball (NOT lambda_*(L)>=0).  Route B: "
    "the ball is span{cos(pi x/(2L))}; 1-mode Rayleigh "
    "from closed g, regularized A, psi algebraic tail.  "
    "YB gate PASS r in [1.163e-2, 1.180e-2], P=0.  All 12 "
    "schedule points H2BALL_POS through L_16=2.7726 "
    "(r_lo=3.45e-6).  sigma_A(0)=-(gamma+log pi)-(pi/2+3 log 2) "
    "~ -5.372.  Peano C0 in [16.16596, 16.16597].  "
    "Smoke 15/15, full 25/25, SPEC_SHA a123650e757b912d.  "
    "Companion rh/problem/crossterm.tex + "
    "verify_crossterm.py CROSSTERM VERIFIED -- "
    "UNCONDITIONAL(L_max=2.7726).  "
    "NO L* claim, NO R-dagger claim, NO RH claim, "
    "NO anti-RH claim"
)

_R477_STATUS = (
    "classical Weil high-mode dominance "
    "(round 477, PRIME.RDAGGER.HIGHMODE_DOMINANCE.01; "
    "experiments-side, NO ledger row): "
    "VERDICT ARCHITECTURE_STANDS(0.3,0.8,1.0).  "
    "Frequency form A=(1/2pi) int sigma_A |hat h|^2 with "
    "sigma_A = Re psi(1/4+it/2)-log pi, Bose identity "
    "sealed at 6 frequencies.  Prime range n<=e^{2L}.  "
    "High-mode t0 sealed: 22 / 4300 / 2.44e5.  Crude "
    "Schur coupling bound fails (YB crude ~-125); direct "
    "2x2 (constant, first Dirichlet) PD at all three L "
    "(Schur_lo 4.67e-2, 7.41e-2, 3.55e-2).  YB gate PASS "
    "(P=0).  Not lambda_*(L)>=0.  Smoke 18/18, full 28/28, "
    "SPEC_SHA 57fd2de61c6fdcc9.  Companion "
    "rh/problem/highmode.tex + verify_highmode.py "
    "HIGHMODE VERIFIED -- ARCHITECTURE_STANDS(0.3,0.8,1.0).  "
    "NO L* claim, NO R-dagger claim, NO RH claim, "
    "NO anti-RH claim"
)

_R478_STATUS = (
    "classical Weil end-to-end fixed-L "
    "(round 478, PRIME.RDAGGER.ENDTOEND_FIXEDL.01; "
    "experiments-side, NO ledger row): "
    "VERDICT PARTIAL(0.3-even-5x5-PD|tail-Schur).  "
    "Even Fourier Gram at L=0.3 (P=0, t0=22) PD for "
    "N=2,3,4,5: 2x2 charpoly lmin in [1.731e-2,1.826e-2], "
    "Higham mu>=8.30e-3 / 2.46e-3 (N=2,3); N=4,5 "
    "congruence-certified PD.  Tail Schur OPEN "
    "(HS correction 6.78e-2 > Higham3).  Not "
    "lambda_*(0.3)>=0.  L=0.8 even Fourier 3x3 with "
    "exact rank-3 P indefinite; best substructure r477 "
    "2x2 Schur_lo=7.41e-2; N~2190 Chol ~3.50e9 flops.  "
    "sigma_P almost-periodic, gain<=1.010 at L=0.8 "
    "(no L>1.6 unlock).  Smoke 17/17, full 27/27, "
    "SPEC_SHA 138cbf9410486418.  Companion "
    "rh/problem/endtoend_fixedl.tex + "
    "verify_endtoend_fixedl.py ENDTOEND_FIXEDL VERIFIED -- "
    "PARTIAL(0.3-even-5x5-PD|tail-Schur).  "
    "NO L* claim, NO R-dagger claim, NO RH claim, "
    "NO anti-RH claim"
)

_R479_STATUS = (
    "classical Weil lambda_*(0.3) keystone "
    "(round 479, PRIME.RDAGGER.LAMBDASTAR_03_KEYSTONE.01; "
    "experiments-side, NO ledger row): "
    "VERDICT REDUCED(kappa_high<=1.79e-2 at t*=8,N=5).  "
    "P=0 so Q=A+Pi, A multiplier, Pi rank one per parity.  "
    "t_c in [6.289835988836902, 6.289835988836904] via "
    "digamma identity; tr(K)=2L t_c/pi in "
    "[1.201270186632830, 1.201270186632832].  "
    "Minorant sigma(0)K+Pi INDEFINITE (interlacing).  "
    "Even Fourier N=2..5 PD (r478); odd n=1 r>=0.300.  "
    "At (t*,N)=(8,5): c_tail>=0.2408, kappa_low<=6.43e-3; "
    "closes iff kappa_high<=1.79e-2 (OPEN).  Not "
    "lambda_*(0.3)>=0.  Smoke 10/10, full 22/22, "
    "SPEC_SHA 7a234db34c2ec6f0.  Companion "
    "rh/problem/lambdastar03.tex + "
    "verify_lambdastar03.py LAMBDASTAR03 VERIFIED -- "
    "REDUCED(kappa_high<=1.79e-2 at t*=8,N=5).  "
    "NO L* claim, NO R-dagger claim, NO RH claim, "
    "NO anti-RH claim"
)

_R480_STATUS = (
    "classical Weil kappa_high at L=0.3 "
    "(round 480, PRIME.RDAGGER.KAPPA_HIGH.01; "
    "experiments-side, NO ledger row): "
    "VERDICT REDUCED(refined-Schur; crude-kappa_high-killed@0.30).  "
    "Named r479 bound ||P_5 A_+ (1-P_5)||<=1.79e-2 is FALSE: "
    "Nyström n=48 T=150 gives kappa_high~2.91e-1 "
    "(stable vs n=64); every scanned (t*,N) stays >0.25.  "
    "Edge modes n=3,4 have 1-lambda=O(1) and couple O(sigma) "
    "to the tail; crude sqrt(mu_3 c_tail) mixes directions.  "
    "Fourier-HS not reused.  Refined even 3x3 Schur "
    "S=B-CC^T/c_tail is numerically PD (lmin~5.69e-3); "
    "odd ~0.207.  Interval S>0 OPEN.  Not "
    "lambda_*(0.3)>=0.  Smoke 14/14, full 23/23, "
    "SPEC_SHA 7be2cb1dcc994ba6.  Companion "
    "rh/problem/kappa_high.tex + "
    "verify_kappa_high.py KAPPA_HIGH VERIFIED -- "
    "REDUCED(refined-Schur; crude-kappa_high-killed@0.30).  "
    "NO L* claim, NO R-dagger claim, NO RH claim, "
    "NO anti-RH claim"
)

_R481_STATUS = (
    "classical Weil Schur certificate at L=0.3 "
    "(round 481, PRIME.RDAGGER.SCHUR_CERTIFICATE.01; "
    "experiments-side, NO ledger row): "
    "VERDICT REDUCED(interval-FT+IBP-tail).  "
    "epsilon=lambda_6(K_8)<=1.46e-8 lifts from Nyström "
    "(entire sinc, GL remainder <1e-80, residual 1e-16); "
    "c_tail>=0.2408 PROVED.  Fourier route (b) KILL "
    "(Q_0n ~ 1/n tail eats Schur).  sigma^2 Plancherel "
    "is not ||A u|| on [-L,L].  IBP envelope pad ~0.76 "
    "on mode 4 KILL.  Working basis: Nyström-Slepian "
    "interpolant.  Interval FT + oscillatory [T,inf) "
    "OPEN.  Not lambda_*(0.3)>=0.  Smoke 14/14, full 21/21, "
    "SPEC_SHA c81a0b2490cfb475.  Companion "
    "rh/problem/schur_cert.tex + "
    "verify_schur_cert.py SCHUR_CERT VERIFIED -- "
    "REDUCED(interval-FT+IBP-tail).  "
    "NO L* claim, NO R-dagger claim, NO RH claim, "
    "NO anti-RH claim"
)

_R491_STATUS = (
    "outer bridges final-density audit and reduction "
    "(round 491, PRIME.RDAGGER.OUTER_BRIDGES.03; "
    "experiments-side structural seal, NO ledger row): "
    "VERDICT HIDDEN_GAP_FOUND / DENSITY_BRIDGE_REDUCED.  "
    "The r489 completion has three components, not two.  Polar "
    "normalization corrected to +2*cosh; one-cell pin "
    "2.042015443302091.  fullWeilArchSide is concrete.  The L2 "
    "witness has Lipschitz and support-length contracts; explicit "
    "dyadicSampleGrid uses floor(R*2^m) cells and has a proved support "
    "bound.  Remaining exact targets: sampled autocorrelation "
    "convergence, singular arch continuity, finite-hat pole integral.  "
    "Smoke 12/12, SPEC_SHA baaafe714f54eb07; verifier 7/7.  "
    "Lean sorry census 8 -> 8 (external 3).  r547 census-gate "
    "update: project-sorry-census expected 7 -> 9 (tracked set "
    "Source/Elementwise/Canonical/ExternalBridges/GaborSeparation; "
    "GaborSeparation carries 2 named inputs).  Probe SHA "
    "re-pinned; SPEC_SHA unchanged.  NO L* claim, NO R-dagger "
    "claim, NO RH claim, NO anti-RH claim"
)

_R492_STATUS = (
    "0.3 keystone judgment "
    "(round 492, PRIME.RDAGGER.KEYSTONE_JUDGMENT.01; "
    "adjudication note, NO probe, NO verifier, NO census, "
    "NO ledger row, NO sealed pin): "
    "VERDICT U1 IDEA_NAMED(kernel-Loewner) / "
    "U2 PROCEED_UNDER_BUDGET / U3 REDIRECT_TO_KERNEL_LANE.  "
    "U1: four of five proposed candidates die, three "
    "structurally.  Smooth t-cutoff misdiagnosed: the 1/t tails "
    "are forced by u(+-L) != 0, i.e. by the compact time support, "
    "and max(-sigma_A,0) is Lipschitz (corner, not jump).  "
    "Fredholm trace powers dead twice: with the shift "
    "B = A^- + sI >= sI makes K = B^{1/2} R_s^{-1} B^{1/2} lie in "
    "no Schatten class (lambda_n(R) ~ log(n/4L) from "
    "sigma_A ~ log(t/2pi)), so (tr K^m)^{1/m} = infinity for every "
    "m; without the shift tr((A^- R^{-1})^m) is not an integral of "
    "explicit kernels, R^{-1} on L^2[-L,L] being the unavailable "
    "finite-interval Wiener-Hopf inverse.  Smoothing "
    "preconditioner incompatible with supp in [-L,L]; the only "
    "support-preserving congruence M_w buys epsilon in the tail "
    "against epsilon^2 in the margin.  Other L is real but weaker "
    "(lambda_min^even 9.49e-2 / 3.34e-2 / 7.57e-3 / 1.33e-3 at "
    "L = 0.20 / 0.25 / 0.30 / 0.3465): L = 0.25 becomes the "
    "calibration rung only.  NAMED IDEA (the judge own): the "
    "classical x-space Weil kernel form "
    "Q_W(h) = int_0^{2L} k(x)(g(0)-g(x))dx - c_L g(0) + Pi(h) "
    "with k(x) = e^{x/2}/sinh(x), "
    "c_L = int_0^{2L}(k - 1/x)dx + log(4L) + gamma + log(pi) = "
    "2.192404911132 at L = 0.3, plus the observation that "
    "I - Re tau_x >= 0 for every x, so EVERY truncation of the "
    "x-integral is Loewner-safe: no off-space term, no tail, no "
    "jet, no garbage mode.  The remainder is one bounded "
    "Hilbert-Schmidt eigenvalue bound with an explicit C^infty "
    "kernel on the compact box [-L,L]^2.  Calibrated against three "
    "sealed numbers: sigma_A(0) = -5.3721834192256654; first "
    "Dirichlet 1.18025e-2 inside the r476 hull [1.150,1.192]e-2 "
    "(r486 midpoint 1.178e-2); odd lambda_min 2.2257e-1 against "
    "r483/r485/r486 0.211/0.221/0.226.  Even operator lambda_min "
    "7.5720e-3, Legendre Galerkin spread 2.5e-5 between N = 6 and "
    "N = 36 (spectral, no garbage).  Measured closing budget at "
    "cutoff [1e-2,3e-2], n = 401: 4.2375e-3 - 3*6.77e-4 = "
    "2.20e-3 > 0.  FREE DIAGNOSIS: the r488/r490 premise "
    "R-not-coercive / inf spec R = 0 is FALSE; "
    "<u,A^+u> >= sigma_A(t_1)(1 - lambda_0(K_{t_1}))||u||^2 gives "
    "R >= 1.5685e-2 I at t_1 = 8.2 (Slepian calibration "
    "lambda_0(K_{t_c}) = 0.8593909212 vs 0.859391, "
    "lambda_0(K_8) = 0.9350520466 vs 0.935); the shift s = 0.05 is "
    "not mandatory, but the amplifier 1/c_R = 64 is worse than "
    "1/s = 20, so the lane is not rescued -- the premise is "
    "anti-listed, no verdict regressed.  U2: the keystone is worth "
    "it only in the kernel form and only under a three-round "
    "budget; the kernel lane dominates the r471 F2b fallback "
    "(no point evaluations, hence no density/continuity gap) and "
    "scales better than the frequency route (the prime term enters "
    "as an explicit bounded translation sum).  F3 Guinand-Weil "
    "fixed-L is the Lean explicit-formula bridge (r487: 16-28 "
    "rounds; r489: density bridge at one named sorry), unaffected.  "
    "U3: R494 = PRIME.RDAGGER.KERNEL_LOEWNER.01 under a three-gate "
    "contract (G1 identity with three stop-condition calibration "
    "hits, G2 Loewner truncation budget, G3 finite section with "
    "hard NO-GO at n <= 800); the frequency-side 0.3 lane is closed "
    "permanently; twenty kills consolidated into six families plus "
    "four pre-listed kernel-lane pads.  No probe, no new theorem, "
    "no new census, no sealed pin.  "
    "NO L* claim, NO R-dagger claim, NO RH claim, NO anti-RH claim"
)

_R494_STATUS = (
    "x-space Weil-kernel Loewner certificate at L=0.3 "
    "(round 494, PRIME.RDAGGER.KERNEL_LOEWNER.01; "
    "experiments-side fixed-support theorem, NO ledger row): "
    "VERDICT PROVED(c=2.1000e-3).  G1 three stop hits PASS: "
    "sigma_A(0)=-5.3721834192256654; Dirichlet "
    "1.18025311091317e-2 inside [1.150,1.192]e-2; odd section "
    "2.2256359052e-1 with Pi_odd=-2<sinh>^2.  "
    "c_L in [2.19240491113,2.19240491114].  G2: zero-extension "
    "translation boundary strips retained, I-Re R_x >= 0; quintic "
    "C2 cutoff [0.01,0.03], kappa_w=3.698008040298977, omitted "
    "prefix booked, diagnostic loss 3.3344388074e-3.  G3: n=401 "
    "Legendre section lambda_max=1.501365606961153; exact HS tail "
    "<=7.0457565325e-4 < finite margin/3; complete 2x off-block "
    "charge gives 3*tail=2.1137269598e-3; certified operator floor "
    "2.1220149285e-3, sealed at c=2.1e-3.  Hard n<=800 NO-GO does "
    "not fire.  Smoke/full 17/17, SPEC_SHA "
    "2e6d71138dff454025641443a9c77f8018d36827dcf94cc35f1696dae9deda47; "
    "verifier 6/6.  Galerkin values remain upper-bound diagnostics.  "
    "No L* claim, no R-dagger claim, NO RH claim, NO anti-RH claim"
)

_R495_STATUS = (
    "adversarial kernel-Loewner red team at L=0.3 "
    "(round 495, PRIME.RDAGGER.KERNEL_LOEWNER_REDTEAM.01; "
    "experiments-side audit, NO ledger row): "
    "VERDICT CONFIRMED(c=2.1000e-3).  A1 independently derives the "
    "digamma x-space identity; five non-calibration tests agree to "
    "max 5.736e-21 and c_L=2.1924049111319992553 is stable at "
    "50/80 dps.  A2 zero-extension translation is exact over Q on "
    "6/6 step/shift tests; interval-only norms omit positive boundary "
    "masses 1/5..1.  A3 false doubled-c_L world is correctly negative "
    "(Rayleigh -1.924951, chain -2.188168).  A4 independent "
    "Clenshaw-Curtis order 1025 gives lambda_max=1.501365808845941, "
    "r_401=6.7948686839e-4, kappa_w=3.6980080402989774465, and "
    "cutoff loss 3.3346406923e-3.  A5 measures off-HS 1.8049712e-4 "
    "and nonzero QQ-HS 6.2971739e-4; both are included, with direct "
    "charge 9.9071e-4 below the sealed 3r charge 2.1137e-3.  "
    "Outward floor 2.12201489025e-3.  Smoke/full 11/11, SPEC_SHA "
    "431251a9bcfd40a12d36f5e4a2bc76751afdcdd980a177f9de9597687e21a053; "
    "verifier 6/6.  No L* claim, no R-dagger claim, NO RH claim, "
    "NO anti-RH claim"
)

_R496_STATUS = (
    "kernel-Loewner scaling test at L=0.8 "
    "(round 496, PRIME.RDAGGER.KERNEL_LOEWNER.02; "
    "experiments-side method no-go, NO ledger row): "
    "VERDICT NO_GO(kernel-Loewner-compact-tail@L=0.8).  "
    "G0: c_L=3.5598735700355446 and factor-two prime g(0) mass "
    "2 sum Lambda(n)/sqrt(n)=2.9419735252236205 for n=2,3,4.  "
    "G1 PASS: five dps-50 x/frequency tests agree within 5.499e-14; "
    "r495-A2 zero-extension 6/6 exact over Q; r471 n=24 "
    "mu_lo=1.32253673213734e-4; r477 r(1)=8.02740549e-2 and "
    "Schur_lo=7.41382775e-2.  G2 NO_GO: best booked cutoff "
    "[0.001,0.003] has n=101 section lmin=-1.610673303e-4, hence "
    "every containing section through n=800 remains nonpositive by "
    "interlacing.  G3 NO_GO: exact arch HS tail r_101=9.122410180 "
    "with full 3r=27.367230540; bounded prime translations are "
    "noncompact, with measured 101-to-301 off-block op norm "
    "0.939496613.  Smoke/full 15/15, SPEC_SHA "
    "63f590d43c9ed63e8419c99ddd6b9110e58a7f419d6445de71932aa4575cba97.  "
    "Method no-go only; no anti-positivity theorem.  No L* claim, "
    "no R-dagger claim, NO RH claim, NO anti-RH claim"
)

_R502_STATUS = (
    "0.8 rung judgment "
    "(round 502, PRIME.RDAGGER.L08_JUDGMENT.01; "
    "adjudication note, NO probe, NO verifier, NO census, "
    "NO ledger row, NO sealed pin): "
    "VERDICT U1 BLOCKED(no-certifiable-gap@L>=0.45) / "
    "U2 LADDER_RESTS_REDIRECT_TO_BRIDGE_LANE / "
    "U3 ANTI_LIST_EXTENDED.  "
    "The r496 no-go is reproduced from an independent implementation: "
    "all four cutoff rows (-1.610673e-4, -8.176622e-4, -2.284102e-3, "
    "-3.032258e-2), all four kappa_w (7.3770530633, 6.6829061429, "
    "6.1992956339, 5.0654766992), HS 19.2177 and r_101 9.12241; the "
    "matching booking is (B), prime translations retained as "
    "operators (booking (A) gives -3.8688).  "
    "U1: both r496 obstructions are mis-specified because the target "
    "does not exist at the claimed size.  An explicit odd Legendre "
    "degree-13 witness gives lambda_*(0.8) <= 1.8170e-14, evaluated "
    "at dps=30 in the x-space form as 1.81691694981e-14 and bracketed "
    "from below by the nonnegative spectral side of the explicit "
    "formula over the first 60 zeta zeros, 1.442289883e-14 (79 "
    "percent); the gamma_1 term is 1.061e-26, i.e. "
    "|hat h(gamma_1)| ~ 7.3e-14 against ||hat h||^2 = 2 pi.  Controls "
    "reproduce: L=0.8 constant mode 0.0802740549593 inside the r477 "
    "hull with 60-zero partial 0.07050676638; L=0.3 even minimiser "
    "0.0075718518899 with partial 0.007040224407.  Ceiling ladder "
    "(Galerkin upper bounds, n=81): 7.5715e-3 (L=0.30), 1.3294e-3 "
    "(0.34657), 1.8136e-4 (0.40), 1.6166e-5 (0.45), 9.3448e-7 (0.50), "
    "1.6096e-9 (0.60), 4.8745e-13 (0.70), below float floor from 0.75; "
    "archimedean floor lambda_min(A+Pi) = +7.5715e-3, +1.3294e-3, "
    "-7.8049e-2, -2.0521e-1, -3.2224e-1, -5.3588e-1, -7.3394e-1, "
    "-9.2648e-1, and -12.5178 at the r471 top rung L_16=2.7726; "
    "channel cancellation depth 2.1 digits at L=0.3 rising to 13.6 at "
    "L=0.8.  Four candidate refinements calibrated then killed: "
    "K1 finer window (the deficit really does vanish -- -1.3454e-5, "
    "-9.0685e-7, -9.2299e-8, -6.9242e-9, -7.4437e-11 -- and its limit "
    "is the ceiling; positivity at the witness needs x_0 < 4.59e-8, "
    "hence n >~ 3.5e7 modes); K2 prime-free error block via a scalar "
    "(closed-form almost-periodic sup pi_0.8 = 2.13500217689506 at "
    "c = -1/(2 sqrt 2) since log 4 = 2 log 2, and the sharper "
    "boundary-strip minorant sum a_n = 1.4709867626 with step "
    "potential levels 0.4907286/0.9808577/0.3465736/0 -- both dead, "
    "certificate between -2.40 and -3.87 because "
    "lambda_min(A+Pi) < 0); K3 primes as a joint finite-parametric "
    "object (exact per node: Re R_a is 1/2 times the adjacency of the "
    "path graph on m = ceil(2L/a) vertices, measured lambda_max "
    "0.707107 = cos(pi/4) for log 2 and 0.500000 = cos(pi/3) for "
    "log 3 and log 4; impossible jointly, log 3 / log 2 irrational); "
    "K4 strip-booked cutoff (exact and Loewner-legal, but the witness "
    "has h(+-L)^2 = 9.84e-14, the ceiling's own order).  "
    "U2: the r493e assembly grid_dense_extension consumes NON-STRICT "
    "positivity uniform in the support length, so a fixed-L gap is "
    "off-target; the lambda_* ladder is closed as a proof route for "
    "every L > (log 2)/2, r494/r495 stand, resources go to the bridge "
    "lane, and a mandatory feasibility pre-gate measures cancellation "
    "depth before any scheme is proposed.  "
    "U3: new family F-VII (fixed-L margin objects read as proof "
    "targets) with N5-N10; the r492 U2-ranking entry 'same machine up "
    "the r471 schedule' is withdrawn.  "
    "The ceiling is an UPPER bound on a quantity RH predicts to be "
    "nonnegative; a small positive lambda_* is exactly what RH "
    "predicts, and both representations return a positive value.  "
    "NO counterexample, NO anti-positivity statement.  No L* claim, "
    "no R-dagger claim, NO RH claim, NO anti-RH claim"
)

_R535_STATUS = (
    "numerical red-team of fullWeil_separates_offCritical_zeros "
    "(round 535, PRIME.RDAGGER.WEIL_SEPARATION_REDTEAM.01; "
    "experiments-side, NO ledger row): "
    "VERDICT INCONCLUSIVE(truncation=beta=0.51,gamma=1000.00,"
    "margin=-5.118815e-07,tail_heur=1.267461e+00,"
    "reason=omitted_online_uncontrolled).  "
    "49/49 injected off-critical zeros truncated-negative, but "
    "gamma=1000 is not certified (omitted on-line mass ~+1.27 "
    "swamps margins; Lipschitz tail certifies 0/49).  "
    "Do NOT attack the Lean separation sorry before a "
    "height-uniform construction exists.  Smoke-capable, "
    "SPEC_SHA "
    "c1d7caf1002067e6103f44d5470ddcdc4db321fd4918337ef813924dce8a0a15.  "
    "Separation stays [O].  No L* claim, no R-dagger claim, "
    "NO RH claim, NO anti-RH claim"
)

_R536_STATUS = (
    "kernel-Loewner lambda*(L) window map "
    "(round 536, PRIME.RDAGGER.KERNEL_LOEWNER.WINDOW.01; "
    "experiments-side method result, NO ledger row): "
    "VERDICT WINDOW_MAPPED(L_max=0.300000, "
    "lambda_at_Lmax=2.1220149285e-03, "
    "tail_alt=GO(block-Schur-tail)).  "
    "Frozen r494 method on the grid 0.30-0.80; only L=0.30 "
    "certifies; dies at the 3x HS tail before the first prime "
    "node (L=0.3125 fail); block-Schur tail (2||off||+||rest||, "
    "m=800) recovers +7.152e-4 at L=0.3125.  "
    "FRAMING: r502 already closed the lambda*-ladder as a PROOF "
    "route for L >= 0.45 -- r536 is a method result about tail "
    "bounds, NOT a reopened positivity window.  "
    "SPEC_SHA "
    "82d1409e6924d928e7442fe805486d840f0220b858a89387a3b1de3706e40dca.  "
    "No L* claim, no R-dagger claim, NO RH claim, NO anti-RH claim"
)

_R537_STATUS = (
    "external mpmath audit of the r534 honest contour identity "
    "(round 537, experiments-side, NO ledger row): "
    "VERDICT AUDIT_CLEAN(max_rel_err=5.8852501e-5)+"
    "DICTIONARY_RESOLVES(map=g_tilde(u)=g(u)*cosh(u/2);"
    "class_not_preserved=true).  "
    "200 zeros, 40 digits: all identities confirmed within the "
    "truncation budget, NO Lean definition bug.  The "
    "(1+n^{-1}) vs 2/sqrt(n) mismatch is pointwise resolvable "
    "via g -> g*cosh(u/2) but that map does NOT preserve the "
    "autocorrelation class (mapped Fourier transforms go "
    "negative), so same-test identification stays genuinely "
    "obstructed; surplus Lambda(n)(1-n^{-1/2})^2 has no "
    "universal positivity direction on the class.  "
    "Terminology: the actual right contour edge is Re=2 "
    "(not 17/16; 17/16 is the reflected left-edge Dirichlet "
    "line).  Determinism fix: RUNTIME_SECONDS wall-clock line "
    "removed from stdout; smoke now byte-identical.  "
    "SPEC_SHA "
    "00075ab3233b7630a3d0a4652ba079b88e8a5afc3718810c6f9221f8e8531dc8.  "
    "Corpus identification stays [O].  No L* claim, "
    "no R-dagger claim, NO RH claim, NO anti-RH claim"
)

_R539_STATUS = (
    "centered even Hermite-Gaussian Weil-separation precheck "
    "(round 539, PRIME.RDAGGER.WEIL_GAUSSIAN_SEPARATION.01; "
    "experiments-side, NO ledger row): "
    "VERDICT INCONCLUSIVE_TRUNCATION(worst=beta=0.51,gamma=5,"
    "trunc=-9.377491e-13,n_trunc_neg=25/56,n_cert_neg=25/56).  "
    "Exponential hat decay FIXES the r535 tail (certified omitted "
    "on-line charge = 0 on all 25 winning cells, Trudgian JNT 134 "
    "(2014) CERTIFIED label + crude-safe C=4); 25/56 cells "
    "certified-negative for gamma<=14.13 with live prime coupling "
    "(no Yoshida collapse); ALL gamma>=30 fail at truncation -- a "
    "transform centered at 0 has no mass at t~gamma.  No Lean "
    "Gaussian-campaign mandate; diagnosis: frequency shift needed.  "
    "SPEC_SHA "
    "87a2a2356e937e30a69a19db6ab6976257d40619074d6c3531545a89a9465657.  "
    "Separation stays [O].  No L* claim, no R-dagger claim, "
    "NO RH claim, NO anti-RH claim"
)

_R540_STATUS = (
    "on-line nulling inside the compact Weil class "
    "(round 540, PRIME.RDAGGER.WEIL_ONLINE_NULL_SEPARATION.01; "
    "experiments-side, NO ledger row): "
    "VERDICT SUPPORT_VS_HEIGHT(frontier=R=2,N=20:none;R=4,N=20:none;"
    "R=8,N=20:none;R=2,N=50:none;R=4,N=50:none;R=8,N=50:none;"
    "R=2,N=100:none;R=4,N=100:none;R=8,N=100:none).  "
    "Nullspaces nontrivial (dim 50-180, residual <=3.8e-13), "
    "r535 regression anchor exact, but 0/135 cells "
    "Lipschitz-certified (tail charge +77..+2.5e4 vs margins "
    "<=96); gamma=1000 does not even couple "
    "(Nyquist omega_max=K*pi/R <= 346).  Compact-class nulling "
    "is CLOSED as a certification path; confirms noncompact "
    "route priority.  SPEC_SHA "
    "d09ff8f680650958c528b618285d50b22b51d1a5d397e6cc9ce196109c2fed26.  "
    "Separation stays [O].  No L* claim, no R-dagger claim, "
    "NO RH claim, NO anti-RH claim"
)

_R541_STATUS = (
    "Gabor/wavepacket height-uniform Weil-separation precheck "
    "(round 541, PRIME.RDAGGER.WEIL_GABOR_SEPARATION.01; "
    "experiments-side, NO ledger row): "
    "VERDICT SEPARATION_GO_GABOR(min_certified_margin=-3.557041e+00, "
    "worst=beta=0.51,gamma=1e+04, "
    "scaling=a~const,omega~gamma-pi*a/sigma).  "
    "Gabor wavepackets h=p(t)e^{-a t^2}cos(omega t) (p even deg<=4) "
    "separate 42/42 cells INCLUDING gamma=10000 with certified "
    "on-line mass (exact first 100 ordinates + Trudgian envelope "
    "integral around +/-omega -- NO zetazero enumeration at height "
    "10^4).  Clean scaling law a=sigma^2/64, "
    "omega=gamma-pi*sigma/64 (sigma=beta-1/2), off-line "
    "enhancement e^{sigma^2/2a}=e^{32}; prime coupling live "
    "(eta in [1.3e-2,0.998], no Yoshida collapse); 11/11 checks, "
    "G5 anchor reproduces r539 to 8.9e-16.  Honest boundary: "
    "finite quadratic-form search in a 3-D subclass + cited "
    "Trudgian majorant -- a negative certified Rayleigh is NOT "
    "yet a theorem for the class; the three Lean lemmas needed "
    "are named (class def, closed-form/enhancement identity, "
    "Trudgian on-line majorant).  Certified numerical precheck, "
    "Lean campaign licensed, no claim.  SPEC_SHA "
    "f7c832d6640c84390982309065a70f426ccee42a0388e0636af2f110882af919.  "
    "Separation stays [O].  No L* claim, no R-dagger claim, "
    "NO RH claim, NO anti-RH claim"
)

_R542_STATUS = (
    "Gabor-wavepacket reduction architecture "
    "(rounds 542-550, PRIME.RDAGGER.WEIL_GABOR.SEPARATION_ARCH.01; "
    "Lean-only then sealed scout; NO ledger row, NO RH claim): "
    "RH/GaborSeparation.lean types the noncompact Gabor class, "
    "closed-form identities (sorry-free), and the logical "
    "reduction gabor_inputs_to_mathlib_rh.  r543 discharged the "
    "pure-Gabor integral representation (Mathlib "
    "integral_cexp_quadratic).  r546/r547 discharged the "
    "Path-A increment (GaborIncrementBound = "
    "2*zetaZerosInDiskCardBoundInner).  r548/r550 renormalized "
    "GaborExplicitFormula to the classical identity "
    "Z = Pole - Prime_comb + Arch with combMass = 2*Lambda/sqrt(n); "
    "gaborPrimeSide (1+1/n) removed as a false contour inversion; "
    "new defs gaborZeroSide/gaborPrimeComb/gaborPoleSide/"
    "gaborArchSide; gabor_explicitFormula_to_spectral sorry-free.  "
    "Endpoint still depends on GaborSeparationForAllZeros [O].  "
    "r558 split GaborSeparationPrecheck / ForAllZeros; "
    "GaborExplicitFormula moved to RH/GaborExplicitFormula.lean "
    "r581 discharged gabor_vertical_arithmetic_remainder "
    "(now a theorem).  "
    "r610: GaborLowHeightZeroFree T0=4 unasserted Prop "
    "(classically true, first zero 14.1347, not in Mathlib); "
    "pole term exactly pi*e^{1/8} (gaborHat_pure_one_zero); "
    "zero side <= 19/20 of it; "
    "gaborSpectralFormula_refuted_of_lowHeight; axioms "
    "propext/Classical.choice/Quot.sound.  "
    "r612: asserting theorem gabor_separationForAllZeros deleted; "
    "Prop GaborSeparationForAllZeros retained unasserted "
    "(OVERSPECIFIED/believed-false).  This file has 0 sorry.  "
    "r599/r600 vacuity audit: gaborSpectralFormula subtracts "
    "hat(1) and is not the Weil functional; old hpos is FALSE.  "
    "Live object gaborZeroSide (hpos*).  Live endpoints "
    "GaborZeroSideSeparatesOffCriticalZeros, "
    "GaborZeroSideCriterionToMathlibRH, "
    "gabor_zeroSide_criterion_to_mathlib_rh, "
    "gabor_zeroSide_inputs_to_mathlib_rh, "
    "gabor_zeroSide_pure_criterion_iff_rh (pure family, "
    "takes hsep = GaborZeroSideForAllZeros; r605A "
    "FORALL_ZERO_OVERSPECIFIED), gabor_zeroSide_criterion_iff_rh "
    "(all F, extra hypothesis hline).  Historical wrappers "
    "VACUOUS (r600).  Theorems: gaborHat_criticalLine_nonneg, "
    "gaborHat_one_nonneg, gaborSpectralFormula_eq, "
    "gaborSpectralFormula_neg_of_small_zero_side, "
    "gaborSpectralFormula_refuted (conditional on "
    "Z(F0) < pi e^{1/8}).  Trudgian is inactive Path B "
    "(named Prop, no sorry).  "
    "r605A: GaborZeroSideForAllZeros is the prescribed-packet "
    "pointwise form (scalingGaborTest a=sigma^2/64, "
    "omega=gamma-pi a/sigma) and is OVERSPECIFIED.  "
    "Conditional reduction only; Input 1 (integral) and Input 2 "
    "(increment) PROVED, Input 3 (EF) PROVED as a theorem "
    "(r581); r634L: pureGaborTest_coeffs (rfl) and "
    "pureGaborTest_admissible (GaborSeparation.lean L156-162); "
    "feeds gabor_explicitFormula_pure.  Separation stays [O].  "
    "Tracked sorry census 9 -> 8 at r581 (GaborSeparation 1; "
    "GaborExplicitFormula 0); stays 8 through r605; 8 -> 7 at "
    "r612 (GaborSeparation 0); stays 7 at r634L.  "
    "File 2181 lines, 0 sorry.  NO RH CLAIM"
)

_R543_STATUS = (
    "pure-Gabor bilateral Gaussian integral "
    "(round 543, Lean-only, NO sealed probe, NO ledger row): "
    "RH/GaborIntegral.lean proves "
    "pureGaborHat_integral_representation sorry-free via "
    "Mathlib integral_cexp_quadratic (complex Gaussian).  "
    "No zeta-zero statement, no RH claim.  Closes one of the "
    "four named r542 classical inputs (the integral "
    "representation).  Census of the tracked set later "
    "moves 11 -> 10 at this discharge, then 10 -> 9 at r547.  "
    "NO RH CLAIM"
)

_R544_STATUS = (
    "Gabor uniformity scout "
    "(round 544, PRIME.RDAGGER.WEIL_GABOR.UNIFORM_INEQUALITY.01; "
    "experiments-side sealed probe, NO ledger row): "
    "VERDICT SCOUT_NEGATIVE_ALL_GRID_BUT_GLOBAL_PROOF_BLOCKED.  "
    "Probe experiments/tfpt-discovery/"
    "gabor_uniform_inequality_probe.py; 15/15 scan points "
    "strongly negative; two byte-identical runs.  "
    "SPEC_SHA 82da6ced1dc11fcf1224a33e8d606440de8e13e4534e2c2ca3d0619fd524c7bd; "
    "probe SHA 0f00e346b3080752e0ec15bd393ba0c02c3bf3461bfb4b3a78f8ad24f3ac6df0.  "
    "Pole term helps and is exponentially suppressed.  "
    "Unit-bin counting without Gaussian-density transfer "
    "yields only R lesssim log gamma -- NOT a global "
    "inequality.  Two missing controls named: (1) Gauss "
    "density transfer from the discrete zero sum to the "
    "continuous envelope; (2) off-line zeros outside the "
    "selected FE quadruple.  Companion RH/GaborInequality.lean "
    "is sorry-free (symbolic kernel only; does not discharge "
    "GaborSeparationInequality).  Separation stays [O].  "
    "NO RH CLAIM"
)

_R545_STATUS = (
    "Trudgian roadmap (round 545, analysis only, no artefact): "
    "Path A chosen -- unit increment from existing repo lemmas "
    "(zetaZerosInDiskCardBoundInner).  Path B (exact Trudgian "
    "constants) stays inactive.  No Lean change, no probe, "
    "no RH claim"
)

_R546_STATUS = (
    "local zero-count increment bound "
    "(round 546, Lean-only, NO sealed probe, NO ledger row): "
    "RH/ZeroIncrement.lean proves zeta_unit_increment and "
    "gaborIncrementBound_holds sorry-free.  Explicit constant "
    "2*zetaZerosInDiskCardBoundInner.  Owns gaborZeroCount so "
    "GaborSeparation can import without a cycle.  Path A "
    "increment is a theorem; Trudgian remains inactive Path B.  "
    "This counting bound is NOT by itself a uniform Gabor "
    "inequality (r544 remaining bricks stand).  NO RH CLAIM"
)

_R547_STATUS = (
    "GaborSeparation Path-A discharge "
    "(round 547, Lean-only rebuild of RH/GaborSeparation.lean; "
    "NO sealed probe, NO ledger row): "
    "Trudgian premise unloaded; live counting input is the "
    "proved GaborIncrementBound.  Endpoint "
    "gabor_inputs_to_mathlib_rh depends only on "
    "GaborExplicitFormula + GaborSeparationInequality.  "
    "Tracked sorry census 10 -> 9 (GaborSeparation carries 2).  "
    "Conditional reduction only; no RH claim; separation "
    "stays [O]"
)

_R548_STATUS = (
    "Gabor explicit-formula numerical identity "
    "(round 548; experiments-side sealed probe, NO ledger row): "
    "VERDICT EF_CONFIRMED(max_resid=9.36e-3, A=36/36, "
    "B_scharf=0/24).  Probe experiments/tfpt-discovery/"
    "weil_gabor_explicit_formula_probe.py.  Classical identity "
    "Z = Pole - Prime_comb + Arch confirmed; Lean (1+1/n) prime "
    "side identified as a false contour inversion (comb "
    "2*Lambda/sqrt(n) is the correct gauge).  SPEC_SHA "
    "1c641853ec1f7ad00b3c2c3e0708c224ecd43d107b8f79a2c6f848c658068048; "
    "probe SHA "
    "16f8f59638b091f09fef3e44561f70388f6ba7d26e0093471c77fbd7a03191b9.  "
    "Separation stays [O].  No RH claim"
)

_R549_STATUS = (
    "Gabor discrete density-transfer scout "
    "(round 549, PRIME.RDAGGER.WEIL_GABOR.DENSITY_TRANSFER.01; "
    "experiments-side sealed probe, NO ledger row): "
    "VERDICT TRANSFER_UNIFORM(bound=15079.6447372) + "
    "OFFLINE_ADVERSARIAL(config=beta=0.51,gamma=14,"
    "beta_prime=0.99,gamma_prime=13.9995091261,"
    "Q=1.03983262001e+33374).  Probe experiments/tfpt-discovery/"
    "gabor_density_transfer_probe.py.  Discrete Gaussian "
    "density transfer is uniform; an increment-compliant "
    "off-line configuration remains adversarial.  SPEC_SHA "
    "60dbea7a517ede8a2de1e1d0b1d29be97a91ac11eba6fa4d2e008b782e7aeb2f; "
    "probe SHA "
    "2304b734386e08823747759fa6df4f70677d789299d9fd56cbc5fcb10a749b05.  "
    "Separation stays [O].  No RH claim"
)

_R551_STATUS = (
    "Gabor extremal-selection scout "
    "(round 551, PRIME.RDAGGER.WEIL_GABOR.EXTREMAL_SELECTION.01; "
    "experiments-side sealed probe, NO ledger row): "
    "VERDICT SELECTION_CONDITIONAL(condition=spectral_gap:"
    "sigma_prime/sigma<=0.919354897686;gleichstand_unrepaired;"
    "even_phase_inadmissible).  Probe experiments/tfpt-discovery/"
    "gabor_extremal_selection_probe.py.  Budget "
    "B/|Q_sel|=141.62 is gamma-free; off-line control stays "
    "conditional (tie unrepaired; even phase inadmissible).  "
    "SPEC_SHA "
    "616d5a4adb9727ace94ea27201966d4ea4ac0085bc8e64c796c3e9ca35a4b4d3; "
    "probe SHA "
    "603d13420612e26febd2e271b16b2381a683b02ab14bc4b0ad50fd2bb99d6277.  "
    "Separation stays [O].  No RH claim"
)

_R552_STATUS = (
    "discrete Gaussian theta-lobe bound "
    "(round 552, Lean-only, NO sealed probe, NO ledger row): "
    "RH/GaborThetaBound.lean proves gauss_binMax_tsum_le <= "
    "Theta_lobe(a) = 3 + 2*Sum exp(-m^2/2a) center-independently, "
    "plus bin_partial_summation and gauss_online_mass_uniform, "
    "sorry-free.  RH.lean imports the module.  "
    "RH/GaborInequality.lean adds the alias "
    "gauss_density_transfer_binMax.  Discrete density transfer "
    "is PROVED; the log-factor remainder and the continuous "
    "TrudgianGaussianMeasureTransfer stay open.  This is not "
    "a uniform Gabor separation inequality.  r579 adds "
    "varC / bin_partial_summation_varC (log occupancy).  "
    "Separation stays [O].  Tracked sorry census 9 -> 8 at "
    "r581.  NO RH CLAIM"
)

_R552_INEQ_STATUS = (
    "Gabor inequality kernel plus discrete transfer alias "
    "(rounds 544/552; NO ledger row): r544 companion "
    "RH/GaborInequality.lean is sorry-free (symbolic kernel; "
    "does not discharge GaborSeparationInequality).  r552 adds "
    "the alias gauss_density_transfer_binMax to the proved "
    "discrete bin-max bound in GaborThetaBound.lean.  "
    "r579/r580 add gauss_density_transfer_binMax_log "
    "(log-occupancy Finset transfer).  "
    "Continuous TrudgianGaussianMeasureTransfer remains open.  "
    "Separation stays [O].  NO RH CLAIM"
)

_R553_STATUS = (
    "Gabor config-first quantifier-flip scout "
    "(round 553, PRIME.RDAGGER.WEIL_GABOR.CONFIG_FIRST.01; "
    "experiments-side sealed probe, NO ledger row): "
    "VERDICT_A WITNESS_LOSES(config=cluster:k=5:unit|s=0.25|g=14), "
    "VERDICT_B WITNESS_LOSES(config=game:k=10:w=5*sqrt(a)).  "
    "Probe experiments/tfpt-discovery/"
    "gabor_config_first_probe.py.  Quantifier flip tested: "
    "neither the 1-packet nor the 2-packet Gabor class beats "
    "every increment-compliant configuration; class extension "
    "(2-packet) is not sufficient.  Honest negative: the Gabor "
    "class alone does not prove the forall-Z exists-h form "
    "under pure counting control.  SPEC_SHA "
    "d9e4e335f14afbca51cf0ed9e6b98ce82ed062d05a11106c247e8e4bb52985ee; "
    "probe SHA "
    "f2d763032196b55755cf9ef1a8195552e886927f1fe81b4701b402434bdd058b.  "
    "Separation stays [O].  No RH claim"
)

_R554_STATUS = (
    "Gabor mixture-witness scout "
    "(round 554, PRIME.RDAGGER.WEIL_GABOR.MIXTURE_WITNESS.01; "
    "experiments-side sealed probe, NO ledger row): leftover "
    "scale is nonlinear; r553 loss claimed as a pick artefact "
    "(dissent).  Later settled by r559/r560: leftover is not a "
    "faithful Weil proxy.  Probe experiments/tfpt-discovery/"
    "gabor_mixture_witness_probe.py.  SPEC_SHA "
    "7af671184671880b47d80353cc447891b998162cbdd325f971e90cb5259bfeb8; "
    "probe SHA "
    "f0f8ed3e070abef09a0a5c54a358c48a9ef3a851d86df25dda53f9820a7a9457.  "
    "Separation stays [O].  No RH claim"
)

_R555_STATUS = (
    "Gabor hat analytic foundations "
    "(rounds 555/587, Lean-only, NO sealed probe, NO ledger row): "
    "RH/GaborHatAnalytic.lean proves entirety, FE-symmetry "
    "hat_W(1-s)=hat_W(s), three-lobe bound, and Gaussian strip "
    "decay, sorry-free.  r587: poly-in-t majorant "
    "norm_gaborHat_le_poly_three_lobe "
    "(||hat|| <= C(sigma)*(1+|t|)^8*threeLobe) is a THEOREM.  "
    "Does not prove GaborExplicitFormula.  "
    "Tracked sorry census stays 8.  NO RH CLAIM"
)

_R557_SUM_STATUS = (
    "Gabor zero-summability "
    "(rounds 557/587, Lean-only, NO sealed probe, NO ledger row): "
    "RH/GaborZeroSummable.lean proves "
    "summable_gaborHat_over_zeros sorry-free.  "
    "r587: summable_gaborHat_over_zeros_quartic is a THEOREM.  "
    "Tracked sorry census stays 8.  NO RH CLAIM"
)

_R557_HORIZ_STATUS = (
    "Gabor horizontal edges "
    "(round 557, Lean-only, NO sealed probe, NO ledger row): "
    "RH/GaborHorizontalEdges.lean proves "
    "gabor_horizontal_edges_tendsto_zero sorry-free.  "
    "Tracked sorry census stays 9.  NO RH CLAIM"
)

_R557_CONT_STATUS = (
    "Gabor contour residue identity "
    "(rounds 557/r631L, Lean-only, NO sealed probe, NO ledger row): "
    "RH/GaborContourResidue.lean proves "
    "gabor_contour_identity_fixed_T sorry-free.  "
    "r631L docstring: GaborContourLimitRemainder is PROVED "
    "(gaborContourLimitRemainder_holds, r576); not an unasserted "
    "hole.  Tracked sorry census stays 7.  NO RH CLAIM"
)

_R558_EF_STATUS = (
    "Gabor explicit-formula wiring "
    "(rounds 558/564/570/572/576/581/r634L, Lean-only, NO sealed "
    "probe, NO ledger row): RH/GaborExplicitFormula.lean (220 "
    "lines) proves gabor_explicitFormula_of_remainders sorry-free.  "
    "r564 adds right-vertical inversion, Fourier inversion, and "
    "of_parts.  r570/r572/r576 reduce of_parts to the arch "
    "remainder; r581 discharges gabor_vertical_arithmetic_remainder "
    "as a THEOREM (gaborArchContourShift_holds + "
    "gaborArchDigammaIdentification_holds; no sorryAx).  "
    "r634L: gabor_explicitFormula_pure is UNCONDITIONAL for "
    "admissible pure F (coeffs <1,0,0>): gaborZeroSide F = "
    "gaborPoleSide F - gaborPrimeComb F + gaborArchSide F "
    "(both remainders theorems).  Remaining EF brick: "
    "GaborHatQuarticExplicitRemainder (non-pure quartics only).  "
    "Tracked sorry census stays 7.  NO RH CLAIM"
)

_R560_STATUS = (
    "Gabor honest Weil game "
    "(round 560, PRIME.RDAGGER.WEIL_GABOR.HONEST_FORM.01; "
    "experiments-side sealed probe, NO ledger row): "
    "VERDICT HONEST_WITNESS_WINS(all=52, "
    "worst_margin=-6.03480709688e+123).  Probe "
    "experiments/tfpt-discovery/gabor_honest_weil_game_probe.py.  "
    "W_honest = Q_off + R_on (no R_ref, no -3.56 credit).  "
    "Settles the r553/r554 leftover dispute on this catalog; "
    "the forall-Z proof stays open.  SPEC_SHA "
    "4e27e628ac1d6634b96f21a05ff6cf9cffc5f3debe9c02503b72e4e5d97f8682; "
    "probe SHA "
    "990ccd20719cade97374a5134238301a15f77cb9266803a603e86e352ee208bd.  "
    "Separation stays [O].  No RH claim"
)

_R561_STATUS = (
    "Gabor uniform dominance scout "
    "(round 561, PRIME.RDAGGER.WEIL_GABOR.UNIFORM_DOMINANCE.01; "
    "experiments-side sealed probe, NO ledger row): "
    "VERDICT DOMINANCE_UNIFORM(rule="
    "isolation_shrink_from_lock_afac=1/8, ...).  "
    "Probe experiments/tfpt-discovery/"
    "gabor_uniform_dominance_probe.py.  Signed-refuted by "
    "r563/r566 (gamma<0 double-count / plus-lobe); canonically "
    "repaired in r567.  Pin kept because the probe is sealed.  "
    "SPEC_SHA "
    "80beb0a2cf0dd049ba72a25e9f39300737a74a5ad859f121cc9bf7991bc0d138; "
    "probe SHA "
    "519a3895668a96bd13f887ab915fefb41e6196a05171878fb11b5b1098c18993.  "
    "Separation stays [O].  No RH claim"
)

_R562_DOM_STATUS = (
    "Gabor isolation-shrink dominance "
    "(rounds 562/568/569/571/589, Lean-only, NO sealed probe, "
    "NO ledger row): RH/GaborDominance.lean first cut (r562) "
    "proves truncated theta, Q=4 Re hat_W, isolationShrink "
    "sorry-free.  r568 replaces GaborDominanceBound by the "
    "canonical weighted form (GaborCanonicalConfig, gamma>0, "
    "omega>0, floor-free).  r569/r571 discharge T_gap=0 after "
    "isolation, host quadrupole Q<0 under a0=gaborSmallnessA, "
    "and assembly; GaborDominanceBound IS A THEOREM "
    "(no sorryAx).  r573 audit STATEMENT_WEAKENED: finite "
    "proxy (K_bin=43 unproved for genuine zeros; R_on defined "
    "only; singleton junction).  r589 L2: Bridge A docstring "
    "BRIDGE_A_IS_RH_CORE (not a translation lemma); Bridge B "
    "has no Isolation->Scaling monotonicity transfer.  Does "
    "not discharge gabor_separationForAllZeros.  Tracked "
    "sorry census 9 -> 8 at r581.  NO RH CLAIM"
)

_R563_STATUS = (
    "Gabor dominance red-team "
    "(round 563, PRIME.RDAGGER.WEIL_GABOR.DOMINANCE_REDTEAM.01; "
    "experiments-side sealed probe, NO ledger row): "
    "VERDICT REDTEAM_BREAKS(config=sec:equal_sigma_twin_at_-omega, "
    "...).  Probe experiments/tfpt-discovery/"
    "gabor_dominance_redteam_probe.py.  Breaks the r561 rule on "
    "a gamma<0 plus-lobe twin; 0/46 breaks on gamma>0 cells.  "
    "SPEC_SHA "
    "32df8b0424e1b7ba67339b2e734976dc8cf194be8f850e457f3189b87909dbd9; "
    "probe SHA "
    "21a4bbffccdbf05bb8534aab6b4ef20a6185b3873a0a605dcecb7ee04fdaa794.  "
    "Separation stays [O].  No RH claim"
)

_R564_VERT_STATUS = (
    "Gabor vertical T->inf identification "
    "(rounds 564/r581, Lean-only, NO sealed probe, NO ledger row): "
    "RH/GaborVertical.lean proves "
    "gabor_rightVerticalIntegral_eq_prime_sum and "
    "gabor_hat_fourier_inversion sorry-free; no asserting "
    "sorry in this file.  GaborVerticalArithmeticRemainder is "
    "proved (r581) via gaborArchDigammaIdentification_holds; "
    "r634L docstring correction.  Remaining EF brick for "
    "non-pure quartics: GaborHatQuarticExplicitRemainder.  "
    "Tracked sorry census stays 7.  NO RH CLAIM"
)

_R565_STATUS = (
    "Gabor scramble-gate late declaration "
    "(round 565, PRIME.RDAGGER.WEIL_GABOR.SCRAMBLE_GATE.01; "
    "experiments-side sealed probe, NO ledger row): "
    "VERDICT GATE_PASS(mode=needs_no_cancellation, "
    "worst_cell=sig=0.4900/gam=14.0000/r541_lock).  "
    "Probe experiments/tfpt-discovery/"
    "gabor_scramble_gate_probe.py.  Full r541/r548 Weil form "
    "is scramble-insensitive because the bound uses no prime "
    "cancellation.  SPEC_SHA "
    "e8ffb5ca6267092ac07491aa6afd3c4c47cc059f92a1ebe773db308229c3f267; "
    "probe SHA "
    "8be16697e3ea910276364fc9236dcd44a09d02080507759e5ccce20c6afb7830.  "
    "Separation stays [O].  No RH claim"
)

_R567_STATUS = (
    "Gabor canonical dominance "
    "(round 567, PRIME.RDAGGER.WEIL_GABOR.CANONICAL_DOMINANCE.01; "
    "experiments-side sealed probe, NO ledger row): "
    "VERDICT CANONICAL_DOMINANCE_HOLDS(cells=119, "
    "worst_margin=0.990408, bound_conservative=all).  "
    "Probe experiments/tfpt-discovery/"
    "gabor_canonical_dominance_probe.py.  Canonical rule+bound "
    "on 119/119 cells; forall-Z proof stays open.  SPEC_SHA "
    "0073591b08fc8c30397af12242c25f09c73c5a54b0e03acb77a26bf8a9e978f8; "
    "probe SHA "
    "c0781a083cdfdfef0ff166bd415644c2963a3a96b3a140b795859da52b88af63.  "
    "Separation stays [O].  No RH claim"
)

_RH_ROOT_STATUS = (
    "RH.lean root imports (r542-r617L): ZeroIncrement before "
    "GaborSeparation; also imports GaborHatAnalytic, "
    "GaborInequality, GaborThetaBound, GaborZeroSummable, "
    "GaborFEMultiplicity, GaborHorizontalEdges, "
    "GaborContourResidue, GaborVertical, "
    "GaborAutocorrelation, GaborLeftVertical, GaborArchDigamma, "
    "GaborArchContour, GaborVerticalLimit, "
    "GaborExplicitFormula, GaborDominance, GaborDominanceProof, "
    "GaborDominanceAssembly, GaborDominanceLog, "
    "GaborSpectralBridge, GaborDominanceLog2, "
    "GaborArithmeticSeparator, GaborExposedOrbit, "
    "GaborCountableCriterion, "
    "GaborOuterTail, "
    "GaborWindowGlue, GaborAnchoredWitness, "
    "CoxeterCompletion, PrimeLogIndependence.  GaborIntegral "
    "is imported via GaborSeparation.  EF for the Gabor class "
    "is a theorem (r581).  GaborDominanceBoundLog2 is a "
    "theorem (r583).  r590: existential arithmetic "
    "separator module.  r593/r595: outer-tail + window-glue "
    "modules.  r596-r600: anchored-witness module "
    "(log-glue + zeroSide<0 at own packet; cover residual; "
    "r600: GaborSpectralToArithmetic_holds is the pole-sign "
    "lemma hat(1)>=0, NOT RH-core).  r599/r600 vacuity: "
    "live object gaborZeroSide (hpos*); historical "
    "gabor_inputs_to_mathlib_rh VACUOUS.  "
    "r605: GaborExposedOrbit module (sorry-free existential "
    "pure-Gabor separator).  "
    "r610: GaborLowHeightZeroFree T0 unasserted Prop in "
    "GaborSeparation; gaborSpectralFormula_refuted_of_lowHeight.  "
    "r612: GaborCountableCriterion module; asserting "
    "gabor_separationForAllZeros retired; tracked sorry census "
    "8 -> 7; module count 53 -> 54.  "
    "r617L: CoxeterCompletion + PrimeLogIndependence modules; "
    "module count 54 -> 56; tracked sorry census stays 7.  "
    "Conditional Gabor reduction only; "
    "no RH claim"
)


_R569_PROOF_STATUS = (
    "Gabor dominance T_gap / host quadrupole "
    "(rounds 569/597, Lean-only, NO sealed probe, NO ledger row): "
    "RH/GaborDominanceProof.lean proves T_gap=0 after isolation, "
    "host quadrupole Q<0 under cap a0=gaborSmallnessA "
    "(gamma^2/512 term uniform in gamma>0), and eta>9/10.  "
    "GaborDominanceBound is assembled in GaborDominanceAssembly "
    "(named remainder X at this cut).  r597: "
    "isolationShrinkOfConfig_admissible_of_le (free-width "
    "chain for the anchored witness).  Does not discharge "
    "gabor_separationForAllZeros.  NO RH CLAIM"
)

_R570_LEFT_STATUS = (
    "Gabor left vertical "
    "(round 570, Lean-only, NO sealed probe, NO ledger row): "
    "RH/GaborLeftVertical.lean closes the left vertical "
    "(gaborLeftPrimeReflection_holds via FE + dual L-series "
    "inversion).  of_parts reduced to (hlim, harch, hhalf).  "
    "Digamma spec sharpened: psi(1/4)=-gamma-3log2-pi/2.  "
    "NO RH CLAIM"
)

_R571_ASM_STATUS = (
    "Gabor dominance assembly "
    "(rounds 571/597, Lean-only, NO sealed probe, NO ledger row): "
    "RH/GaborDominanceAssembly.lean is sorry-free "
    "(packing + budget: T_far<=1/70, T_plus<=1/100, "
    "R_on/E<=1/100 vs eta>9/10).  GaborDominanceBound IS A "
    "THEOREM (no sorryAx).  r573 later types the statement as "
    "STATEMENT_WEAKENED (finite proxy).  r597: "
    "foreign_not_in_peakWindow_of_le (peak emptiness is a "
    "radius fact on the free-width chain).  Does not discharge "
    "gabor_separationForAllZeros.  NO RH CLAIM"
)

_R572_ACF_STATUS = (
    "Gabor autocorrelation closed form "
    "(round 572, Lean-only, NO sealed probe, NO ledger row): "
    "RH/GaborAutocorrelation.lean proves the ACF closed form "
    "and GaborHalfCombReal sorry-free.  of_parts reduced to "
    "(hlim, harch).  NO RH CLAIM"
)

_R574_LOG_STATUS = (
    "Gabor dominance log cap "
    "(rounds 574/575/597/598, Lean-only, NO sealed probe, "
    "NO ledger row): "
    "RH/GaborDominanceLog.lean sets gaborKBinAt gamma = "
    "2*C_inner*(1+log(gamma+3)) exactly at the counting "
    "theorem; counting => log-compliance PROVED "
    "(singleton+strip).  r575: GaborDominanceBoundLog IS A "
    "THEOREM (LogFarPacking+RemainderBudgetLog+AssemblyLog "
    "sorry-free under sharpened far-cap gaborFarSmallnessA).  "
    "r597: gaborHonestWeilLeMajorantLog_of_le (free-width "
    "chain).  r598: helpers gaborFarTailLog_mono_abs, "
    "gaborLogWeightedTheta_two_le_gammaCap "
    "(|omega(a)|<=gamma-star) for retuned-omega htail.  "
    "Does not discharge gabor_separationForAllZeros.  "
    "NO RH CLAIM"
)

_R576_VLIM_STATUS = (
    "Gabor contour vertical limit "
    "(round 576, Lean-only, NO sealed probe, NO ledger row): "
    "RH/GaborVerticalLimit.lean proves "
    "gaborContourVerticalLimit_holds sorry-free (Landau-gap "
    "T-sequence, horizontal edges Gauss*log^3, rectangle "
    "exhaustion).  of_parts reduced to (harch).  NO RH CLAIM"
)

_R577_DIG_STATUS = (
    "Gabor arch Digamma on the critical line "
    "(round 577, Lean-only, NO sealed probe, NO ledger row): "
    "RH/GaborArchDigamma.lean proves chi'/chi(1/2+it)=omega(t) "
    "sorry-free via GammaR reflection "
    "(logDeriv_zetaFEFactor_criticalLine).  Digamma "
    "identification leaves 2 named remainders (closed r581).  "
    "NO RH CLAIM"
)

_R578_ARCH_STATUS = (
    "Gabor arch contour pairing "
    "(rounds 578/581, Lean-only, NO sealed probe, NO ledger row): "
    "RH/GaborArchContour.lean closes the pairing "
    "(gaborArchCriticalPairingReal_holds) and proves the "
    "fixed-T residue oint (chi'/chi) hat = -2*pi*i*hat(0) "
    "(pole split, strip pole-freeness).  r581 discharges "
    "T->inf: gaborArchContourShift_holds (T_k=k+2, no Landau).  "
    "NO RH CLAIM"
)

_R579_SPEC_STATUS = (
    "Gabor spectral bridges "
    "(rounds 579-589, Lean-only, NO sealed probe, NO ledger row): "
    "RH/GaborSpectralBridge.lean: log-occupancy Gauss transfer "
    "(varC/binMax_log), three-lobe Finset bound, unweighted "
    "truncation compliance of genuine zeros, exhaustion "
    "algebra.  r584: gaborLogThreeLobeMajorant_le_closed "
    "THEOREM (Closed budget dominates the Finset-transfer "
    "majorant); pure On/Off split of_summable / of_pure.  "
    "r585: gaborHat_star_pure, "
    "gaborHat_fe_quadrupole_eq_four_re, "
    "gaborCriticalLineMassLeLogMajorant_holds; HONEST: "
    "weight-4 quadrupole tsum over all Im>0 double-counts.  "
    "r586: gaborOffLineMassEqWeightedQuadrupoleTsum_holds "
    "THEOREM in honest FD form (Re>1/2 and Im>0, weight 4, "
    "+ real-axis remainder); double-count prop documented "
    "dead.  r587: unrestricted On/Off-split "
    "gaborZeroSideEqOffPlusOn_holds is a THEOREM; quartic "
    "weighted hat summability.  r588: "
    "gaborWeightedQuadrupoleLimitEqFDTsum_holds; "
    "riemannZeta_ne_zero_of_mem_Ioo (zeta != 0 on (0,1) "
    "real, via r509 Euler-Maclaurin, not Eta); "
    "gaborOffLineRealAxisMass_eq_zero; weighted Bridge-6 "
    "identification "
    "gaborWeightedQuadrupoleLimitEqOffLineMass_holds is a "
    "THEOREM.  Unweighted identification only _of_simple.  "
    "r589: FD window -> BoundLog2 hypotheses "
    "(gaborWeightedTruncation_boundLog2_hyps); named "
    "GaborWeightedTruncationGammaDistinct and "
    "GaborWeightedTruncationNegLog; GaborTruncationUniformNeg "
    "does NOT follow from BoundLog2 (packet retunes).  "
    "Remaining named rest: GaborTruncationUniformNeg, "
    "GaborWeightedTruncationGammaDistinct, living sorry "
    "gabor_separationForAllZeros.  Tracked sorry census "
    "stays 8.  Finite/conditional only.  NO RH CLAIM"
)

_R582_FE_STATUS = (
    "Gabor FE multiplicity on the open strip "
    "(rounds 582/585, Lean-only, NO sealed probe, NO ledger row): "
    "RH/GaborFEMultiplicity.lean proves "
    "riemannZetaMultiplicity_eq_one_sub_all (m(z)=m(1-z) via "
    "Lambda(s)=Lambda(1-s) on the open strip) and "
    "sum_multiplicity_stripZerosWindow_le (Jensen+FE fold: "
    "unit window sum m <= 2*C_inner*(1+log(|N|+3))), "
    "sorry-free.  Weighted truncation compliance is a "
    "theorem.  r585: riemannZetaMultiplicity_eq_conj "
    "(m(bar rho)=m(rho) via Schwarz reflection) sorry-free.  "
    "Does not discharge gabor_separationForAllZeros.  "
    "Tracked sorry census stays 8.  NO RH CLAIM"
)

_R583_LOG2_STATUS = (
    "Gabor dominance BoundLog2 "
    "(rounds 582/583/589/597, Lean-only, NO sealed probe, "
    "NO ledger row): "
    "RH/GaborDominanceLog2.lean.  r582 packs BoundLog2 "
    "(omega-dependent R_on_log) sorry-free; r583 closes "
    "GaborRemainderBudgetLog2 and proves "
    "GaborDominanceBoundLog2 as a THEOREM (both R_on_log/E "
    "branches via online_exp_le_log; hat-side closed "
    "linear-central+far-tail form).  Axioms [propext, "
    "Classical.choice, Quot.sound]; no sorryAx.  "
    "r584-r588 discharge the r583 named remainders as "
    "theorems (tsum<=Closed; unrestricted On/Off-split; "
    "weighted Bridge-6 identification).  r589: every nonempty "
    "weighted FD window is BoundLog2 input "
    "(gaborWeightedTruncationNegLog_holds theorem; lock "
    "margin n-free; singleton card=1 supplies "
    "gammaDistinct+hostIsolated); "
    "gabor_dominanceLog2_implies_separation is pure logic "
    "on two named bridge hypotheses.  r597: free-width "
    "chain gaborHonestWeilLeMajorantLog2_of_le, "
    "gaborRemainderBudgetLog2_of_le, "
    "gaborHonestWeilLog_lt_etaMargin_of_le / "
    "_lockMargin_of_le (feeds anchored zeroSide<0 at own "
    "packet).  Finite/conditional proxy only.  Does not "
    "discharge gabor_separationForAllZeros.  Tracked sorry "
    "census stays 8.  NO RH CLAIM"
)

_R590_ARITH_STATUS = (
    "Gabor existential arithmetic separator "
    "(round 590, Lean-only, NO sealed probe, NO ledger row): "
    "RH/GaborArithmeticSeparator.lean.  Named unasserted "
    "GaborArithmeticSeparatesOffCriticalZeros (forall "
    "off-critical zero exists admissible F with "
    "gaborArithmeticFormula F < 0).  Sorry-free: "
    "gabor_separation_of_arithmetic_separators (EF + "
    "separator => GaborSeparatesOffCriticalZeros) and "
    "gabor_arithmetic_inputs_to_mathlib_rh (parallel "
    "Mathlib chain WITHOUT scalingGaborTest; old chain "
    "unchanged).  Named unasserted: "
    "GaborFixedPacketCofinalNegAt and "
    "gabor_arithmetic_separator_of_cofinal_neg.  L2 r589 "
    "verdict BRIDGE_A_IS_RH_CORE recorded in docstring.  "
    "r600: live gabor_arithmetic_zeroSide_inputs_to_mathlib_rh; "
    "historical gabor_separation_of_arithmetic_separators / "
    "gabor_arithmetic_inputs_to_mathlib_rh marked VACUOUS.  "
    "r605A: gabor_zeroSide_pure_criterion_iff_rh takes hsep "
    "as premise (GaborZeroSideForAllZeros / prescribed "
    "scalingGaborTest packet) and is OVERSPECIFIED; live "
    "unconditional iff is "
    "gabor_zeroSide_pure_criterion_iff_rh_unconditional in "
    "GaborExposedOrbit.lean.  "
    "Living sorry remains gabor_separationForAllZeros.  "
    "Tracked sorry census stays 8.  Finite/conditional "
    "only.  NO RH CLAIM"
)

_R591_STATUS = (
    "Gabor fixed-packet cofinal-negativity scout "
    "(round 591, PRIME.RDAGGER.WEIL_GABOR.FIXED_PACKET_COFINAL.01; "
    "experiments-side sealed probe, NO ledger row): "
    "VERDICT (a) strict sigma'<=sigma-0.02 "
    "COFINAL_NEG_HOLDS(hosts=9, worst_Wred=-0.995192); "
    "(b) weak (tie allowed) COFINAL_NEG_BREAKS 0/9 "
    "(r551 killer, Wred=+14.005); (c) free sigma'<=0.49 "
    "COFINAL_NEG_BREAKS 0/9 (r549, +inf).  epsilon floor: "
    "0.005 holds 9/9, 0.001 MIXED 8/9.  Interpretation: "
    "GaborFixedPacketCofinalNegAt tenable ONLY WITH "
    "EXTREMALITY, not as r590 formulated without the gap.  "
    "Probe experiments/tfpt-discovery/"
    "gabor_fixed_packet_cofinal_probe.py.  SPEC_SHA "
    "cd9af7ce0c1ed42786d3ebc006c0de6c28d912e6738e9195967578c3bfebb26f; "
    "probe SHA "
    "b614d5833f4e3ee9b41044116b6c0df6d58dc10ce52abd2454077f10fd0accd7.  "
    "Two runs bit-identical, seed 20260902, CHECKS 7/7.  "
    "Separation stays [O].  No RH claim"
)

_R592_STATUS = (
    "Gabor window-adaptive tail scout "
    "(round 592, PRIME.RDAGGER.WEIL_GABOR.WINDOW_ADAPTIVE_TAIL.01; "
    "experiments-side sealed probe, NO ledger row): "
    "VERDICT locally-adaptive-globally-fixed CONDITIONAL.  "
    "A MIXED 36 rescued / 12 broken (all 12 = float64 omega "
    "collapse at near-tie delta=1e-8, W_red=+1, IEEE artefact); "
    "B/C/D HOLDS + TAIL_METRIC_OK (worst W_red=-0.9904, T=0 "
    "underflow).  L2-numerator sup=-0.7687 NOT_REACHED.  "
    "Probe experiments/tfpt-discovery/"
    "gabor_window_adaptive_tail_probe.py.  SPEC_SHA "
    "de35efea8c8cd4ac803aef1cc4c4f33b5fdde7c7dc8d434e061c037231ad8d4b; "
    "probe SHA "
    "1a77a6502251236cda405e782f4fe147e483c44838815b698b99e8d778144603.  "
    "Two runs bit-identical, seed 20260902, CHECKS 15/15.  "
    "Separation stays [O].  No RH claim"
)

_R593_STATUS = (
    "Gabor outer tail (rounds 593/594, Lean-only, NO sealed "
    "probe, NO ledger row): RH/GaborOuterTail.lean.  "
    "r593: strip-width beats window distance "
    "(gaborOuterTail_num_le_neg_quarter, "
    "abs_gaborQuadrupole_outer_le_exp); exact R near-tie "
    "(gaborWindowAdaptiveRule_exists; r592 float64 collapse "
    "has NO R counterpart); endpoint "
    "gabor_window_adaptive_inputs_to_mathlib_rh sorry-free.  "
    "r594: BOTH tail Props are THEOREMS -- "
    "gaborOuterTail_tsum_le_exp / GaborOuterTailTsumLeExp_holds "
    "(FD indicator tsum over |Im rho - omega| >= R); "
    "GaborOuterTailSmallerThanLocalMargin_holds "
    "(forall eps exists a0(omega,eps)<=1 forall a<a0: "
    "tail < eps*E).  Multiplicity-weighted Finset bound "
    "mass-independent, rate exp(-1/(8a)) kept.  Axioms "
    "[propext, Classical.choice, Quot.sound]; no sorryAx.  "
    "Named unasserted: GaborWindowAdaptiveCofinalNeg, "
    "gabor_arithmetic_separator_of_window_adaptive.  "
    "r600: live gabor_window_adaptive_zeroSide_inputs_to_mathlib_rh; "
    "historical gabor_window_adaptive_inputs_to_mathlib_rh "
    "marked VACUOUS (consumed false hpos).  Living sorry remains "
    "gabor_separationForAllZeros.  Tracked sorry census "
    "stays 8.  Finite/conditional only.  NO RH CLAIM"
)

_R595_STATUS = (
    "Gabor three-term window+tail glue "
    "(round 595, Lean-only, NO sealed probe, NO ledger row): "
    "RH/GaborWindowGlue.lean sorry-free.  Three-term glue "
    "(gaborHonestWeil_window_add_outer, "
    "gaborHonestWeil_le_window_plus_theta); catalog negativity "
    "(gaborCanonicalConfig_honestWeil_neg, "
    "gaborHonestWeil_glue_neg_of_small_isolation); per-T "
    "checkpoint (gaborWeightedTruncation_windowAdaptive_"
    "existsDelta / lockDelta; factor T-free, E not).  Named "
    "unasserted: GaborWindowAdaptiveUniformDelta (T-uniform "
    "delta missing because of lex host-retune -- r592 "
    "condition, not missing algebra) and "
    "gabor_window_adaptive_uniform_to_cofinal.  Axioms "
    "[propext, Classical.choice, Quot.sound]; no sorryAx.  "
    "Living sorry remains gabor_separationForAllZeros.  "
    "Tracked sorry census stays 8.  Finite/conditional only.  "
    "NO RH CLAIM"
)

_R596_STATUS = (
    "Gabor anchored window witness "
    "(rounds 596-600, Lean-only, NO sealed probe, NO ledger row): "
    "RH/GaborAnchoredWitness.lean.  L2 verdict ANKER_TEILWEISE "
    "(anchor removes host-retune + float64 collapse; three "
    "gaps: omega-self-consistent window, equal-ordinate "
    "sigma-clusters, log-budget glue).  r596: "
    "GaborAnchoredWindowWitnessAt type-bundle (all hyps "
    "explicit, hcover omega-self-consistent); sorry-free "
    "log-glue (R_on -> R_on_log); "
    "gaborAnchored_zeroSide_neg_of_isolationPacket "
    "(witness => spectral zero-side < 0 at shrink width).  "
    "r597: GaborBoundLog2AtAdmissibleWidth discharged "
    "(gaborBoundLog2AtAdmissibleWidth_holds); "
    "gaborAnchored_zeroSide_neg (witness => zeroSide < 0 "
    "at OWN (a,omega)).  r598: singleton fragment + htail "
    "at retuned omega(a) (exists_gaborFundSingleton_htail); "
    "cover isolated as GaborAnchoredCoverAt (ordinate "
    "isolation); exists_gaborAnchored_of_cover / "
    "gaborAnchoredCoverAt_to_nonempty.  HONEST: hcover "
    "for genuine zeros open (ordinate clusters); "
    "multi-point window open.  GaborAnchoredWitnessExists "
    "NOT asserted.  r600: GaborSpectralToArithmetic_holds "
    "is a THEOREM (pole-sign lemma hat(1)>=0, NOT RH-core); "
    "also gaborArithmeticFormula_neg_of_zeroSide_neg, "
    "rh_implies_gaborZeroSide_nonneg (pure), "
    "rh_implies_gaborZeroSide_nonneg_of_onLine.  Named "
    "unasserted: GaborAnchoredWitnessExists, "
    "gabor_anchored_to_arithmetic_separator.  "
    "L2 STOP: no UniformDelta / separator / existence "
    "claims.  Axioms [propext, Classical.choice, "
    "Quot.sound]; no sorryAx.  Living sorry remains "
    "gabor_separationForAllZeros.  Tracked sorry census "
    "stays 8.  Finite/conditional only.  NO RH CLAIM"
)

_R601_STATUS = (
    "Gabor Weil positivity subfamily scout "
    "(round 601; experiments-side sealed probe, NO ledger row): "
    "VERDICT DOMINANCE_FAILS.  132 cells, EF sanity <= 1.4e-15 "
    "with 2000 zeros, NEG_NUM=0, POS_CERT 38 only for "
    "omega >= omega0(a) (~500 at a=0.5 down to 10 at a>=3); "
    "no a<=5 omega-uniform.  Cancellation exponent "
    "exp((1/8+d^2/2)/a) near zeros confirmed (pred 3.01 / "
    "meas 3.53).  Fixed-a Gabor family is a Bombieri/"
    "Connes-Consani sub-family, not hpos*.  Probe "
    "experiments/tfpt-discovery/"
    "gabor_weil_positivity_subfamily_probe.py.  SPEC_SHA "
    "cae570b458e53de6252745af0c881b6a2ebf4bcfc33d2e2c98985f52057e75cc; "
    "probe SHA "
    "b7089c71de9918c90a2b80bbea489ef938723a3021370baaebc183dd7494354b.  "
    "Two runs bit-identical.  Separation stays [O].  No RH claim"
)

_R603_STATUS = (
    "Two-key GP inequality search on Lambda(n) "
    "(round 603, PRIME.INEQUALITY.EVOSEARCH.01; "
    "experiments-side sealed probe, NO ledger row): "
    "Grid verdict SURVIVORS_FOUND(1378) but parent audit "
    "discriminatively EMPTY -- survivors are convergent-constant "
    "comparisons on Re s=1 (|Sc(1,2)| <= |Sc(1,14.134725)| "
    "<-> 0.4218 <= 1.6238 = |Re zeta'/zeta(1+it)|) or grid "
    "artefacts (sine-sum zero at X=15737).  Controls C1-C4 "
    "all DENSITY (local jitter p^{0.6} moves psi ~1e2; "
    "beta=0.75 fake zero amplitude 2108 < 6908 = 0.5*sqrt(X)*log X "
    "at 1e6, visible only from X~1e10).  Lessons: relative "
    "jitter ~5 percent, beta=0.9 kill world, only s=1/2 "
    "error-term terminals.  Probe experiments/tfpt-discovery/"
    "prime_inequality_evosearch_probe.py.  SPEC_SHA "
    "0f29c05bdfd8440b35eafb3fe51a957ac0148990dce666f0f401832beec20c43; "
    "probe SHA "
    "06d2ac9a6b7fe0f648e6c22052ba6ad0491bc1a05d954ab0eb23e078733511e2.  "
    "CHECKS 13/13, two runs bit-identical.  Separation stays [O].  "
    "No RH claim"
)

_R604_STATUS = (
    "TFPT-spectrum vs zeta-ordinate cross-correlation scout "
    "(round 604; experiments-side sealed probe, NO ledger row): "
    "VERDICT ARTIFACT.  Positives fire z(log 2/3/5/7) = "
    "6.00/7.96/9.12/9.33.  Candidates omega1=2.583 z=-0.58 "
    "(0.018 from log 13); only z>=5 is omega1+2*omega2 = 4.489 "
    "= log 89, dies under unfolding (prime-line alias).  "
    "T2: 274 complex dims vs 138 gamma<=300, mean |Delta|=0.912, "
    "p_shift=0.922, p_poisson=0.821, p_gue=0.008 (null-calibration "
    "residual, not signal).  Resonance 18.097 mid-gap.  T3 "
    "Kuiper p>=0.28 all four moduli.  Probe "
    "experiments/tfpt-discovery/tfpt_spectrum_zero_crosscorr_probe.py.  "
    "SPEC_SHA "
    "264e0c53b87a36a069750ea6f402e0a8d38d3952671b69f6a4f8b71ea23633e9; "
    "probe SHA "
    "748ae5098d87b49a83e6efb1cb7f66813b50f9700d6adc67a95c7cad6c4df853; "
    "PAYLOAD_SHA prefix 7fdab80e; ZEROS_SHA prefix 2a3fd52c "
    "(N=4000 from verified_zeros_n7000.npy).  CHECKS 7/7, two "
    "runs diff empty, ~28 s.  Separation stays [O].  No RH claim"
)

_R605N_STATUS = (
    "Gabor exposed-orbit + phase-lock scout "
    "(round 605N, PRIME.RDAGGER.GABOR.EXPOSED_ORBIT.01; "
    "experiments-side sealed probe, NO ledger row): "
    "VERDICT EXPOSED_ORBIT_HOLDS.  9/9 configs negative at n=0, "
    "normalised limit -4m(rho*) exact, tail bound holds, "
    "40/40 checks, byte-identical reruns.  Probe "
    "experiments/tfpt-discovery/gabor_exposed_orbit_probe.py.  "
    "SPEC_SHA "
    "1a4bf9493be71ad1c33d1eb25123e3e1021cd0fa0e3d3ded5d1a0663b69e4cde; "
    "probe SHA "
    "c99998c4ef8371eee59c2ef392a7a247a4babcda0d7697ffd4881db1ffacb273.  "
    "Separation stays [O].  No RH claim"
)

_R605BC_STATUS = (
    "Gabor exposed-orbit existential separator "
    "(rounds 605B+C, Lean-only module, NO ledger row; "
    "r605C-AUDIT independent read-only STATEMENT_SOUND): "
    "RH/GaborExposedOrbit.lean (1734 lines, new module) "
    "sorry-free.  gaborScore, ExposedOrbit structure, "
    "exists_exposedOrbit_of_not_rh, phase lock cos=-1, "
    "three-lobe majorant Re hat(rho*) <= "
    "-(pi/4a)e^{M/2a}+(3pi/4a)e^{(M-Delta)/2a}, "
    "gaborExposedOrbitAssembly_holds, endpoints "
    "exists_negative_pureGabor_of_not_rh (hasm), "
    "gabor_zeroSide_pure_criterion_iff_rh_of_assembly (hasm), "
    "gabor_zeroSide_pure_criterion_iff_rh_unconditional : "
    "(forall a omega ha, 0 <= gaborZeroSide "
    "(pureGaborTest a omega ha)) <-> RiemannHypothesis.  "
    "#print axioms = [propext, Classical.choice, Quot.sound].  "
    "Census at landing 8 (Canonical 3, Source 1, Elementwise 1, "
    "GaborSeparation 1, ExternalBridges 2); live 7 after r612.  "
    "RH <=> nonnegativity of the pure Gabor zero-side on the "
    "two-parameter family (a, omega); zero-side only -- no "
    "prime-side/explicit-formula claim; positivity of "
    "gaborZeroSide itself remains open.  This is NOT an RH "
    "proof: the Weil test space is reduced to a two-parameter "
    "pure Gabor family on the zero side.  r605A: prescribed "
    "packet GaborZeroSideForAllZeros is "
    "FORALL_ZERO_OVERSPECIFIED.  NO RH CLAIM"
)

_R606_STATUS = (
    "Connes prolate residual-gap scout "
    "(rounds 606/606b, experiments-side sealed probe, NO ledger row): "
    "FIRST RUN (r606, 6-9 mode, t_cut=150): VERDICT INCONCLUSIVE; "
    "mu jumped to 5.9 and g<0 at L>=0.6 (discretisation artefact; "
    "r478 small blocks fail at L=0.8); CCM Poisson k_lambda "
    "Davis-Kahan eta=0.13/0.093/0.029 at L=0.3/0.4/0.5, breakdown "
    "L>=0.6 attributed to the uniform position grid.  "
    "ADDENDUM r606b (tall ladder; dual-run byte-identical, ~0.4 s): "
    "VERDICT INCONCLUSIVE(evals-not-converged, disc-disagree>5pct).  "
    "No L meets successive-N < 1 pct AND Slepian/Fourier "
    "discretisation agreement < 5 pct; the wall is discretisation "
    "(Slepian lambda_2 pollution beyond N=12-24, Fourier odd-mode "
    "~2 pct, t_cut=1000 blocked by spatial Nyquist), not a GO/STOP "
    "on eta.  The r606 mu~5.9 jump is gone (k tracks lambda_1); "
    "lambda_1^e slightly negative (-3e-6..-8e-6) at L>=0.5 but "
    "unconverged -> NOT a Chuk contradiction; NREAL theta-hat[0,30] "
    "= 2,3,3,4,4,4 vs Riemann count 3 (plateaus at 4, does not tend "
    "to the Riemann count).  Lane CLOSED -- superseded by r611 "
    "(OBS_NOT_CONVERGING) and the KILLED(FACTORIZATION) typing of "
    "the prolate route; diagnostic only.  Probe "
    "experiments/tfpt-discovery/connes_prolate_residual_gap_probe.py.  "
    "SPEC_SHA "
    "115c0409a907d44308da58ab7308f0242dcc8036ed167d1c30f43e3af33529fe; "
    "probe SHA "
    "aeef52a6d40cbcbe5c19b4cccf84b987cfa3e4002813abbf4b29159be4cd8295.  "
    "No RH claim"
)

_R607_STATUS = (
    "Event Lindblad two-key scout "
    "(round 607, PRIME.EVENT.LINDBLAD.01; "
    "experiments-side sealed probe, NO ledger row): "
    "VERDICT KILLED(RECOORDINATIZATION).  Lindblad CP <=> "
    "lambda_min(Q_W) to 1e-15 in TRUE/SCRAMBLE/EPSTEIN/WPERM "
    "worlds; diagonal compensator Sigma lambda diverges "
    "~2e^{X/2}; Euler-Pick Gram needs 10 scalars; labels "
    "decorative; 15/15 checks.  Probe "
    "experiments/tfpt-discovery/event_lindblad_twokey_probe.py.  "
    "SPEC_SHA "
    "3abe6b9b7964aee4dc15d3e1e0fa466224c5fb4b85574f7a35c8a8581a9ddd71; "
    "probe SHA "
    "3c1db81b1dcf10fce59bc836670846fa3881312cfe2182b4706a9fcd5b25cff0.  "
    "Method no-go.  Separation stays [O].  No RH claim"
)

_R608_STATUS = (
    "Gabor tropical heat / source-budget scout "
    "(round 608, GABOR.TROPICAL.01; experiments-side sealed probe, "
    "NO ledger row): VERDICT TROPICAL_CONFIRMED.  "
    "2a*log|Z| -> F(omega) with error <= 6.77*a*log(1/a); "
    "on-line F = -dist(omega,{gamma})^2 <= 0; synthetic beta=0.9 "
    "gives F=+0.16.  Correct heat equation "
    "d_a hat = (1/2) d_ww hat - hat/(2a) (rel 3e-9) on traveling "
    "lobes; cross lobe 2e^{(delta^2-omega^2)/2a} carries residual "
    "-delta^2/(2a^2) so U=sqrt(a)*Z is NOT a heat solution "
    "(dyadic heat-semigroup criterion FALSE for this family).  "
    "Source-side budget B(a)=2.05/4.18/13.6 at a=0.2/0.1/0.05, "
    "c~1/8, saddle n=e^{1/(2a)}; EF residual 4e-11 at a=0.2 with "
    "2000 zeros.  Consequence: HEAT.SOURCE lane = NOGO T1 "
    "(RH-strength cancellation), STOP.  Probe "
    "experiments/tfpt-discovery/gabor_tropical_heat_probe.py.  "
    "SPEC_DESIGN "
    "0008f535ddf1aec0f7a5651a12eed28d2db01603995390827c16ae6cc801b5ec; "
    "sealed-run SPEC prefix 6fcc507d; probe SHA "
    "574c1cc2888169b918bfe97e5d5c127b039f07f2063e081e73d22ef6995107ec.  "
    "CHECKS 9/9.  Separation stays [O].  No RH claim"
)

_R609_STATUS = (
    "E8 directed readout scout "
    "(round 609; experiments-side sealed probe, NO ledger row): "
    "VERDICT E8_READOUT_SEALED(7/8).  Seifert S+S^T=A, "
    "charpoly(-S^{-1}S^T)=Phi_30, rank(S-S^T)=8; H_8 weight "
    "enumerator 1+14y^4+y^8, 240=16+14*16, S(3,4,8), "
    "srg(120,56,28,24) eig 56/8/-4 mult 1/35/84; N(n)=240 sigma_3(n) "
    "n<=10; tau(n) n<=8 (A_P(1)=1658880); E_4^3-E_6^2=1728 Delta; "
    "(Z/30)^x ~= C_2 x C_4 != C_2^3, character table = H_2 tensor F_4; "
    "E_6 oplus A_2 index 3, Smith (1^6,3,3), roots 72+6+162.  "
    "C7 NOT_TESTED at probe time; C7 later supplied in "
    "note_e8_gaussian_code.tex L372-461 (explicit 8x8 = H_2 tensor F_4, "
    "permutation [0,1,4,3,5,2,7,6]); Gauss-code transform still "
    "undefined (open remark rem:c7-audit).  TFPT-side exact "
    "structure; no prime bridge shown; promotion to verification/ "
    "is a pending user decision.  Probe "
    "experiments/tfpt-discovery/e8_directed_readout_probe.py.  "
    "SPEC_SHA "
    "3edfb82499d80cecff6afb8da3b4533888b1dd042e7a8943e8caea1bdee581a3; "
    "probe SHA "
    "9ab0a6386b084ef4f45f938970dee8d3b78db2a7839edda3f8ac3acac71333c8.  "
    "CHECKS 49/49.  No RH claim"
)

_R611_STATUS = (
    "Connes observable Aubin-Nitsche scout "
    "(round 611, CONNES.OBSERVABLE.AUBIN-NITSCHE.01; "
    "experiments-side sealed probe, NO ledger row): "
    "VERDICT OBS_NOT_CONVERGING.  Hybrid Q_lambda lambda_min ~ -1e-5 "
    "for L>=0.5 (r606 discretisation crash removed, t_cut-stable); "
    "eta_obs(1.2) TRUE 0.667/6.3e-3/3.7e-4 at L=0.3/0.4/0.5 then "
    "RISING 1.6e-2/5.6e-2/9.0e-2/0.150 at L=0.6-1.0 (p=-8.1); "
    "OFFLINE ~ TRUE (0.109 at L=1.0) -> blind to injected off-line "
    "zero at gamma=20; WPERM 0.69, SCRAMBLE 0.20; identity (8) "
    "4.6e-11.  Consequence: Herglotz/Aubin-Nitsche closure route "
    "(Solution 1) STOP as a lane; PROLATE.GABOR.ALIGN moot.  "
    "r606b CLOSED (INCONCLUSIVE(evals-not-converged, disc-disagree>5pct); superseded by r611 OBS_NOT_CONVERGING and KILLED(FACTORIZATION); diagnostic only).  "
    "Probe experiments/tfpt-discovery/"
    "connes_observable_aubin_nitsche_probe.py.  SPEC_SHA "
    "647335a638ef8c589f116a1e7aba7e7b651fc585e5d79c4d8006848c8786c002; "
    "probe SHA "
    "9360774660b4e3ba79066642c92e461d6f49c3c8163f13eff1e2d45639a6af69.  "
    "CHECKS 12/12.  Method no-go.  Separation stays [O].  No RH claim"
)

_R612_STATUS = (
    "Gabor countable rational-packet criterion "
    "(round 612, Lean-only module, NO sealed probe, NO ledger row): "
    "RH/GaborCountableCriterion.lean (historical r612 pin; 163 lines then).  "
    "SUPERSEDED by _R612C_STATUS (continuity proved).  Historical r612 theorem "
    "gabor_zeroSide_rational_criterion_iff_rh (hcont) : "
    "(forall (a omega : Q) (ha : 0<(a:R)), "
    "0 <= gaborZeroSide (pureGaborTest a omega ha)) "
    "<-> RiemannHypothesis; gabor_zeroSide_rational_of_rh "
    "(converse without continuity); "
    "gabor_zeroSide_nonneg_of_rational.  "
    "#print axioms = [propext, Classical.choice, Quot.sound].  "
    "Companion r612 edit in GaborSeparation.lean: asserting "
    "theorem gabor_separationForAllZeros deleted; Prop "
    "GaborSeparationForAllZeros retained unasserted with "
    "OVERSPECIFIED/believed-false docstring.  "
    "Tracked sorry census 8 -> 7 (Canonical 3, Source 1, "
    "Elementwise 1, ExternalBridges 2; GaborSeparation 0).  "
    "Module count 53 -> 54.  Conditional/finite only.  NO RH CLAIM"
)

_R613_STATUS = (
    "Ordered-E8 Herglotz canonical-system scout "
    "(round 613, PRIME.E8.ORDERED.HERGLOTZ.01; "
    "experiments-side sealed probe, NO ledger row): "
    "VERDICT NO_IDENTIFICATION.  Weyl function Herglotz "
    "(min Im-eig +3.5e-3), (JH)^2=0 exact; at eps=0 all jumps "
    "commute -> order decorative (max 1e-14) (same lesson as r607); "
    "at eps=0.05 order/labels non-decorative (16.6/12.0) but "
    "residuals at Euler points TRUE 0.66-2.5 ~ SCRAMBLE/WPERM "
    "0.66/0.64, 2.36/2.36; twirl chain E_full<E7<E3 breaks "
    "(4.5>3.1).  Consequence: ordered-E8 Herglotz canonical "
    "system (Paket C) dead as a lane.  Probe "
    "experiments/tfpt-discovery/prime_e8_ordered_herglotz_probe.py.  "
    "SPEC_SHA "
    "01b4a8be9dd1530a817a83c38a5aba9e1b2ba483cafd93405dede71516da2ac9; "
    "probe SHA "
    "c89fc1ceb70f7ec8e1f0ce9d3af630c4c4329b7f972684cce78a717b44c5aeb9.  "
    "Method no-go.  Separation stays [O].  No RH claim"
)

_R615_STATUS = (
    "Semilocal first-prime-step scout "
    "(round 615, PRIME.SEMILOCAL.FIRSTSTEP.01; "
    "experiments-side sealed probe, NO ledger row): "
    "VERDICT FIRSTSTEP_LEAKAGE_CONTROLLED.  Weil window form with "
    "exactly one prime (L in (0.3466, 0.5493), w2 = sqrt(2) log 2 = 0.98026).  "
    "Ritz lambda*(L) equals zero-side leakage to 1e-4-1e-5 at all L; "
    "extremal vector Slepian-like (overlap with psi0 >= 0.9989, "
    ">= 99.8 percent spectral mass below gamma1 = 14.1347), no character "
    "change at the prime entry.  lambda*(0.30) = 7.57e-3 (v1017 padded "
    "floor 2.1e-3, factor 3.6), lambda*(0.40) = 1.85e-4, "
    "lambda*(0.549) = 5.80e-8 with POLE +1.30 / ARCH -1.29 / PRIME 1.78e-2 "
    "(cancellation depth 2.25e7).  Pinning at L=0.52: delta_crit = 2.5e-5 "
    "relative on w2, eps_crit = +4.1e-5/-1.7e-6 on the atom position, "
    "WPERM -0.135, SCRAMBLE -0.33/-0.18/-0.047.  Certificate obstruction: "
    "shift cross-block norm 0.50 for N=40/80/160 (no decay), Schur "
    "requirement R = 0.25/lambda* = 1.4e3 (L=0.40) ... 4.45e6 (0.549) "
    "=> r496 confirmed for every window containing a prime.  Mechanism (T9): "
    "minimizer of fictitious prime-free POLE+ARCH is purely odd with "
    "POLE = -2 <h, sinh(u/2)>^2 < 0 and ARCH < 0, g(log 2) < 0, so "
    "-w2 g(log 2) carries positivity (L=0.40: -0.018 - 0.060 + 0.130 = +0.053); "
    "odd sector turns negative at L ~ 0.372, prime 2 enters at 0.3466 "
    "(margin Delta L ~ 0.025).  Named open lemma "
    "PRIME.SEMILOCAL.ODDSECTOR.EDGE.01 [O]: for odd h on [-L,L], "
    "w2 |g_h(log 2)| >= 2 <h, sinh(u/2)>^2 + |ARCH_-(h)|.  Fence: window "
    "forms with L ~< 16 cannot detect off-line zeros (r605 scaling "
    "a = sigma^2/64 needs u-support ~8/sigma); first prime step is far "
    "weaker than RH.  Probe experiments/tfpt-discovery/"
    "semilocal_firststep_probe.py.  SPEC_SHA "
    "04f9c9ec20f8cea556d79c39c26567eecc9e83fb99a48dedfc98b1ce7be5df1e; "
    "probe SHA "
    "3a0741def031cfa41f54cdf11fc332bb77723ad5c4efd8e0900ed16a13ac5052.  "
    "CHECKS 26/26.  No RH claim"
)

_R616_STATUS = (
    "Higher-moment inertia scout "
    "(round 616, PRIME.INERTIA.HIGHERMOMENT.01; "
    "experiments-side sealed probe, NO ledger row): "
    "VERDICT C_CAPPED.  k=2 reproduces Alpoge-Furman 2/3 (psi0) and "
    "ceiling 0.6818287.  Tr(W^3) at bandwidth one is not unconditional "
    "(Sum |xi_j| <= 3 > 2 = Rudnick-Sarnak 1996 support for zeta; "
    "Hejhal 1994 hexagon under RH; Montgomery 1973 and "
    "Goldston-Montgomery 1987 under RH; MV diagonal X^k <= T^{2-eps} "
    "fails for k >= 3) => p3^uncond = p2 = 0.6818.  GUE ideal input n+: "
    "0.75 -> 5/6 -> 31/36; simple-on-line 0.6818 -> 0.6818 -> 0.7222.  "
    "Finite moments never force negative index 0.  Probe "
    "experiments/tfpt-discovery/inertia_highermoment_probe.py.  SPEC_SHA "
    "fef4a72f6ab38aa64e8bd9256e51f16bd6ca30945a4ba0038af6a8e252446a6b; "
    "probe SHA "
    "26ee62ae2b13de0dd31ea7c5abbb17fb731a29b1fef52cef9ab58c85454e9d29.  "
    "CHECKS 16/16.  Follow-up to r267; no RH claim"
)

_R617_STATUS = (
    "E8 Coxeter Euler completion scout "
    "(round 617, E8.COXETER.EULER.COMPLETION.01; "
    "experiments-side sealed probe, NO ledger row): "
    "VERDICT COMPLETION_EXACT.  Tr C = -1; Phi_30 Moebius identity; "
    "(1-x) Phi_30 = 1 - x^2 - x^3 + x^6 + x^7 - x^9; "
    "D_E8(s) = zeta(6s) zeta(10s) zeta(15s)/[zeta(2s) zeta(3s) zeta(5s) zeta(30s)] "
    "residuals at X=10^6: 1.28e-4 (s=0.75), 3.5e-14 (1.5); det2 scalar "
    "control e^{P(s)}/zeta(s) 1.75e-14; class statement (scalar -1, "
    "A1 -> 1/zeta(2s); A2 -> 1/zeta(3s); E6 -> zeta(4s) zeta(6s)/"
    "[zeta(2s) zeta(3s) zeta(12s)]; negative control B2 (trace 0) -> "
    "zeta(2s)/[zeta(s) zeta(4s)] divergent at 0.75); Beurling-generic.  "
    "Typed no-go E8.COXETER.REGULARIZED_SPLIT.NO_GO.01: det2 removes "
    "exactly the trace term; RH content = analytic continuation of "
    "P(s) = Sum mu(k)/k log zeta(k s); constructions controlling only "
    "the Hilbert-Schmidt part cannot isolate 1/zeta(s) (explains "
    "r607/r613 conceptually).  Fence: The trace-free completion is "
    "zero-free and pole-free in Re s > 1/2. The splitting into the "
    "scalar zeta channel and the Coxeter channel is open and "
    "RH-equivalent. No RH claim.  Promotion to verification/ "
    "(v1018/v1019) is in progress.  Probe experiments/tfpt-discovery/"
    "e8_coxeter_euler_completion_probe.py.  SPEC_SHA "
    "5aa3935bd4d5698caa889d62dafba4b7efe62a7b3132d07ab62299c22dd03f8c; "
    "probe SHA "
    "6ac6bab28a355d3b2b3a98114c32586211cbdec0b2712e8e6c60511e03d12c21.  "
    "CHECKS 45/45.  No RH claim"
)

_R618_STATUS = (
    "Jensen / E8-compiler rigidity scout "
    "(round 618, PRIME.JENSEN.E8COMPILER.RIGIDITY.01; "
    "experiments-side sealed probe, NO ledger row): "
    "VERDICT COMPILERS_STRUCTURALLY_RIGID.  Two no-gos: (A) Seifert-compiler "
    "rigidity -- Coxeter monodromy spectrum is a congruence invariant "
    "(Phi_30 for 12 random M S M*); Cayley-transformed Jensen polynomials "
    "C_{n,8} of Xi vary with n and miss the 30th-root grid by >= 0.0168; "
    "blocks d=2..7 give Phi_2^2, Phi_2 Phi_3, Phi_5, Phi_2 Phi_8, "
    "Phi_3 Phi_12, Phi_2 Phi_18; (B) rank-one MSS mixed characteristic "
    "polynomial = det(xI - Sum A_e) exactly; required coefficient ratios "
    "c_{n+1}/c_n (0.0231 -> 0.0169, n=0..6) nonlinear in zero power sums.  "
    "Data: a0 = xi(1/2) = 0.497120778, Turan n <= 12, J_{n,d} hyperbolic "
    "d <= 8, n <= 4 (consistent with GORZ 2019, nothing new).  Fence: "
    "both compilers are generic real-rootedness certificates; existence "
    "for all (n,d) <=> RH; E8 RH-neutral.  Probe "
    "experiments/tfpt-discovery/jensen_compiler_rigidity_probe.py.  "
    "SPEC_SHA "
    "bc8d86246dc253c3944a41f0db23d8791c4275fbb2c4af9f8011006e612cc774; "
    "probe SHA "
    "29ccf1c7d9c2557aa2b4567795598dc6f485835d74dc20b0b2c805d5369463de.  "
    "CHECKS 43/43.  No RH claim"
)

_R617L_COX_STATUS = (
    "E8 Coxeter completion algebraic core "
    "(round 617L, Lean-only module, NO sealed probe, NO ledger row): "
    "RH/CoxeterCompletion.lean (96 lines, imported in RH.lean).  "
    "Theorems cyclotomic30_explicit, moebius_identity_30, "
    "completion_explicit, completion_linear_coeff_zero, "
    "trace_eq_neg_one_of_charpoly_cyclotomic30.  "
    "#print axioms = [propext, Classical.choice, Quot.sound].  "
    "Analytic Euler-product corollary not formalized.  Fence: "
    "The trace-free completion is zero-free and pole-free in Re s > 1/2. "
    "The splitting into the scalar zeta channel and the Coxeter channel "
    "is open and RH-equivalent.  Tracked sorry census stays 7.  "
    "Module count 54 -> 56 (with PrimeLogIndependence).  NO RH CLAIM"
)

_R617L_LOG_STATUS = (
    "Q-linear independence of {log p} "
    "(round 617L, Lean-only module, NO sealed probe, NO ledger row): "
    "RH/PrimeLogIndependence.lean (160 lines, imported in RH.lean).  "
    "Theorems linearIndependent_log_primes (full Q-linear independence "
    "of {log p}; Mathlib had no such lemma) and log_ratio_irrational.  "
    "#print axioms = [propext, Classical.choice, Quot.sound].  "
    "Corollary (prose): finite-order clocks cannot carry {log p}.  "
    "Tracked sorry census stays 7.  Module count 54 -> 56 "
    "(with CoxeterCompletion).  NO RH CLAIM"
)

_R612C_STATUS = (
    "Gabor countable rational-packet criterion "
    "(rounds 612/612C, Lean-only module, NO sealed probe, "
    "NO ledger row): RH/GaborCountableCriterion.lean "
    "(568 lines, imported in RH.lean).  r612: asserting "
    "theorem gabor_separationForAllZeros deleted; Prop "
    "GaborSeparationForAllZeros retained unasserted with "
    "OVERSPECIFIED/believed-false docstring; census 8 -> 7.  "
    "r612C: gaborZeroSideContinuous_holds proves "
    "GaborZeroSideContinuous (joint continuity on {a>0} x R "
    "via local uniform Gaussian majorant "
    "||hat|| <= (pi/a0) exp((1/8+omega1^2/2)/a0) "
    "exp(-t^2/(4 a1)) and continuousOn_tsum; summability via "
    "summable_gauss_over_zeros); theorem "
    "gabor_zeroSide_rational_criterion_iff_rh_unconditional : "
    "(forall (a omega : Q) (ha : 0<(a:R)), "
    "0 <= gaborZeroSide (pureGaborTest a omega ha)) "
    "<-> RiemannHypothesis -- UNCONDITIONAL.  "
    "r634L: gabor_primeSide_rational_criterion_iff_rh : "
    "(forall (a omega : Q) (ha : 0<(a:R)), "
    "0 <= gaborPoleSide - gaborPrimeComb + gaborArchSide "
    "of pureGaborTest a omega) <-> RiemannHypothesis -- "
    "fully prime/archimedean-side Pi1 form, UNCONDITIONAL "
    "(uses gabor_explicitFormula_pure).  "
    "#print axioms = [propext, Classical.choice, Quot.sound].  "
    "Named-open list shrinks by one at r612C; tracked sorry "
    "census stays 7.  NO RH CLAIM"
)

_R619_STATUS = (
    "Support-relay census scout "
    "(round 619, PRIME.SUPPORT.RELAY.CENSUS.01; "
    "experiments-side sealed probe, NO ledger row): "
    "VERDICT RELAY_UNIVERSAL.  Prime powers q <= 32 "
    "(18 events), entry L_j = (1/2) log q; every ancestor "
    "form Q_{j-1} (without the newest event) fails a finite "
    "lead after entry: Delta_j = 0.011-0.028, nearly constant "
    "(2: 0.0279, 3: 0.0123, 4: 0.0146, 5: 0.0111, 7: 0.0105, "
    "8: 0.0140, 9: 0.0125, 11: 0.0116, 13: 0.0131, 16: 0.0166, "
    "17: 0.0126, 19: 0.0144, 23: 0.0141, 25: 0.0170, "
    "27: 0.0181, 29: 0.0151, 31: 0.0147, 32: 0.0221); failing "
    "mode always odd, reflection-symmetric edge sector w.r.t. "
    "the newest event (g < 0), edge mass 0.07-0.65; newest "
    "weight restores positivity (all 18).  lambda* decay "
    "slopes per interval -50 / -77 / -79 (global -68.6; "
    "Slepian -28.3; r615 -44.8) -> super-exponential "
    "(Landau-Widom plunge); lambda* underflows SVD range "
    "beyond L ~ 1.4.  Controls: SCRAMBLE first failure 0.376, "
    "WPERM 0.402, EPSTEIN (2^k only) 0.564 ~ L_3 + 0.015 -- "
    "each control breaks at entry + lead.  Detection "
    "threshold (synthetic off-line zero injected into the "
    "zero side): L_det(beta=0.6, gamma=20) = 0.55, "
    "(0.75, 20) = 0.55, (0.6, 50) = 0.80, (0.9, 20) = 0.50.  "
    "PARENT TYPING: the RELAY_UNIVERSAL criteria "
    "(Delta_j >= 0, g < 0, repair) are consequences of "
    "Q_j succeq 0 (RH-consistency), not a mechanism; the "
    "informative results are the constant leads "
    "(\"greedy consumption\": each prime power becomes "
    "load-bearing within Delta L ~ 0.015), the control "
    "breaks at entry+lead, the super-exponential decay, and "
    "L_det -- windows with L >~ 0.5 are hypersensitive "
    "off-line detectors (a nulled zero displaced by sigma "
    "contributes -sigma^2 |d hat f|^2, beating the tiny "
    "lambda*), hence relay steps beyond L ~ 0.5 are "
    "RH-in-a-box statements, not elementary finite problems.  "
    "Fence: window positivity for the scanned L is "
    "RH-consistent; no RH claim.  Probe "
    "experiments/tfpt-discovery/support_relay_census_probe.py.  "
    "SPEC_SHA "
    "7299737ded85418e4e88fea1356f378ec4c2c077c7d35a09211cc7980a88553d; "
    "RESULT_SHA prefix e0379485; probe SHA "
    "fcfa7771f2522e4458a7f2cb4dc20a68974bb2ca4f0239ea7c877da76193da4a.  "
    "CHECKS 12/12.  No RH claim.  CORRECTED BY r635: the constant-lead / greedy-law reading Delta ~ 0.015 nearly constant across 18 events is WITHDRAWN (N=80 double-precision artefact).  Converged leads Delta_2=0.0253, Delta_3=0.0083, Delta_4=0.0064 (0.00606 at N=160), Delta_5=0.0034 (0.00275 at N=160); q>=7 UNMEASURABLE at 40-digit prime-side floor (probe: 'later events already indefinite at entry'; Delta=0, conv=0, q=7 lam_min=-7.0e-11).  RELAY_UNIVERSAL verdict, entry census, odd/edge failing mode, and L_det table UNAFFECTED."
)

_R620_STATUS = (
    "P2 reflection-factor scout "
    "(round 620, PRIME.P2.REFLECTION.FACTOR.01; "
    "experiments-side sealed probe, NO ledger row): "
    "VERDICT MIXED_SECTOR.  Exact identity for odd h, "
    "d = log 2, overlap I = [d-L, L], reflection "
    "(Rf)(x) = f(d-x): g_h(d) = -(||f_+||^2 - ||f_-||^2); "
    "prime term -w2 g = w2(||f_+||^2 - ||f_-||^2) "
    "(stabilizes symmetric edge sector, destabilizes "
    "antisymmetric).  dim E_-(A^{odd}) = 1 for L >= 0.38 "
    "(lambda_min -2.4e-2 at 0.38 -> -0.43 at 0.549); mass "
    "of the negative vector inner/+/ -: 0.85/0.15/0.005 "
    "(0.38), 0.71/0.28/0.01 (0.40), 0.50/0.48/0.02 (0.43), "
    "0.06/0.94/0.001 (0.549) -- migrates from inner to "
    "R-symmetric edge; antisymmetric sector safe without "
    "the prime (lambda_min(A|P_-) - w2 = +5.7 -> +0.29); "
    "cross term 0.12-0.28; oriented inequality "
    "lambda_min(A^{odd} + w2(P_+ - P_-)) = lambda*(L) >= 0 "
    "everywhere.  The parent's earlier |g| lemma is "
    "mis-stated (prime hurts on P_-) -> RETYPE the contract "
    "PRIME.SEMILOCAL.ODDSECTOR.EDGE.01 to the oriented form: "
    "for odd h on [-L, L]: <h, (POLE+ARCH) h> + "
    "w2(||f_+||^2 - ||f_-||^2) >= 0; the negative direction "
    "of POLE+ARCH migrates from the inner region to the "
    "R-symmetric edge sector; the antisymmetric edge sector "
    "is safe without the prime -- status stays [O]; the "
    "repair is a quantitative dominance with margin "
    "lambda*(L), not an exact sector identity.  Probe "
    "experiments/tfpt-discovery/p2_reflection_factor_probe.py.  "
    "SPEC_SHA "
    "7c8e73b7d4f27fedd0e34b8d6c4df7b6e95120e369b0a76b0ab51cc840edc1ee; "
    "probe SHA "
    "194fe9e5abcb4886bd927bf6b3fa921008917afc0d82364f742f4891706bc438.  "
    "CHECKS 73/73.  No RH claim"
)

_R621_STATUS = (
    "P2 digamma-duplication scout "
    "(round 621, PRIME.P2.DIGAMMA.DUPLICATION.01; "
    "experiments-side sealed probe, NO ledger row): "
    "VERDICT DUPLICATION_CONSTANT_ONLY.  Duplication "
    "psi(z)+psi(z+1/2) = 2 psi(2z) - 2 log 2 verified 2e-25; "
    "operator identity ARCH_1/4 = ARCH_C - ARCH_3/4 - "
    "2 log 2 * G to 2e-15; the prime-2 operator "
    "P_2 = -w2 T_{log 2} vs span{ARCH_3/4, G}: residual "
    "0.997-0.998 on the whole odd space (0.71 -> 0.23 on "
    "E_-), HS cosine <= 0.005, fitted beta ~ 0.06 "
    "(not -2 log 2).  Translation != constant.  T4: the "
    "Q(i) form POLE + ARCH_C stays positive without its "
    "norm-2 prime (lambda_min +0.59 at 0.549); Gamma_C "
    "without the constant fails at 0.38 like zeta -- the "
    "conductor constant carries, not the 3/4 channel.  "
    "No-go: the prime-2 repair is not a duplication factor "
    "of the archimedean operator.  Probe "
    "experiments/tfpt-discovery/"
    "p2_digamma_duplication_probe.py.  SPEC_SHA "
    "78f47c87a6877ada8cf96969e0e7b0c79969fa723bdf3036f10ca6efc8f6992e; "
    "probe SHA "
    "dff2e1b3d9c9155434625cf8e5f80049d368633fc6ea6097bebdb88896b17557.  "
    "CHECKS 37/37.  No RH claim"
)

_R622_STATUS = (
    "Support Darboux-transport scout "
    "(round 622, PRIME.SUPPORT.DARBOUX.01; "
    "experiments-side sealed probe, NO ledger row): "
    "VERDICT TRANSPORT_FEASIBLE_NORULE.  Scaled family "
    "Qtilde(L) = U_L^* Q_L U_L on L^2[-1,1]; transport "
    "identity d_L Qtilde + X^* Qtilde + Qtilde X + c Qtilde "
    "= Y^* Y: with X = 0 feasible for "
    "c = c0(L) = -lambda_min(Qtilde^{-1/2} d_L Qtilde "
    "Qtilde^{-1/2}) (finite: 26 at 0.25, 63 at 0.3466-, "
    "spike 368 at prime entry, 84 at 0.38, 1614 at 0.549); "
    "prime-free c0 ~ -d log lambda*/dL (ratio 1.06-1.52), "
    "with prime up to 33x larger (extra modes) but << 1/lambda*; "
    "no two-term closed-form law for c(L) (rms 347; fails "
    "at the kink and at 0.549); forbidden "
    "X0 = -1/2 Qtilde^{-1} d_L Qtilde not in the source "
    "algebra (projection residual 0.88 -> 1.0); the algebra "
    "produces rate 0 vs required 31.8/46.0; the prime is "
    "not the PSD obstruction, it spikes c0.  Typing: the "
    "transport formulation relocates the tiny margins into "
    "the scalar c0(L) (relative form of the wall); no "
    "source-side rule.  Probe "
    "experiments/tfpt-discovery/support_darboux_probe.py.  "
    "SPEC_SHA "
    "27ffd017df86ec8f321032c075598e946a5892610f41881cb8eee4b782f6a90b; "
    "PAYLOAD prefix e1031d17; probe SHA "
    "845bb93720b7cecae55d003fcb11021ac1338d79f292a45f0f0267f96c49bbd5.  "
    "CHECKS 64/64.  No RH claim"
)

_R623_STATUS = (
    "Semilocal P2 dilation scout "
    "(round 623, PRIME.SEMILOCAL.P2.DILATION.01; merged user rounds "
    "r623 tower + r624 dilation; experiments-side sealed probe, "
    "NO ledger row): VERDICT P2_DILATION_STRUCTURALLY_BLOCKED.  "
    "The 2-adic channel of the Weil form is the multiplier "
    "m2(t) = log 2 * (1 - P_r(t log 2)), r = 2^{-1/2}, P_r the "
    "Poisson kernel (= boundary value of the de Branges-Rovnyak "
    "kernel of the Blaschke factor b(z) = (z-r)/(1-r z)); one Euler "
    "factor generates the whole rung ladder 2^k (active rungs: [2] "
    "for L <= 0.65, [2,4]+3 for L in {0.72, 0.80}); identity residual "
    "4.9e-12.  Obstructions to the proposed PSD block "
    "[[A_S, B*],[B, C]] with Schur complement Q_L: the ancestor "
    "POLE+ARCH has lambda_min = -0.078 (L=0.40), -0.229, -0.367, "
    "-0.430 (0.549), -0.536, -0.636, -0.773, -0.926 (0.80) -> cannot "
    "be a PSD principal block; the 2-channel operator M2 is indefinite "
    "(n+/n- 9/9 at 0.40 ... 14/10 at 0.80) with numerical rank/N "
    "0.75-1.0 (not rank one) -> cannot be -B* C^{-1} B; the generic "
    "dilation [[Q+M2-, sqrt(M2-)],[sqrt(M2-), I]] has lambda_min "
    "tracking lambda*(L) (1.82e-4 vs 1.81e-4 at 0.40) -> tautological.  "
    "No manifest local SOS in the named factors: ||N||/lambda_min(P) = "
    "2.75-5.27 (negative part never dominated).  Literature: "
    "Connes-Consani 2021 (Selecta) Thm 1 positivity only for support "
    "[2^{-1/2}, 2^{1/2}] (archimedean); CCM arXiv:2310.18423 §4.6 Sonin "
    "space without a positivity theorem; arXiv:2403.01247 Jacobi matrices "
    "for S={infty,p} (q = 1/p); zeta-cycles numerical -> no published "
    "unconditional first prime step.  Typing (parent): each prime is a "
    "positive channel entering the Weil form with the wrong sign "
    "(constant minus Poisson kernel); positivity is not manifest; the "
    "semilocal dilation lane is NOT opened (user rule: dead on No).  "
    "Probe experiments/tfpt-discovery/semilocal_p2_dilation_probe.py.  "
    "SPEC_SHA "
    "5890676d194739b1de05adf74482dc1fb6498ba56b16d663522801035df9e6b3; "
    "probe SHA "
    "d1bec728c5329dd8d20c2c50752f2dd165bddd17da23505b0dd79563b0b8215b.  "
    "CHECKS 128/128.  No RH claim"
)

_R625_STATUS = (
    "IIKS vanishing-metric scout "
    "(round 625, PRIME.IIKS.VANISHING.METRIC.01; experiments-side "
    "sealed probe, NO ledger row): VERDICT IIKS_NO_METRIC_IN_CLASS "
    "(prose: NOT_TESTABLE_IN_CORPUS_FORM).  For the corpus discrete "
    "IIKS/CD object (v563/PIK/tau_symbolic/v955, r265 cross-ratio ODE "
    "reproduced 3.9e-9) the jump J_s = I - 2 pi i s f g^T on the real "
    "CD nodes; Zhou vanishing lemma there requires J* = J^{-1}, which "
    "FAILS (rel 2.56e-2 on WPERM kz9), and det J = 1 at s* while "
    "tau(s*) = det(I - s* E) = 0 (log|tau| ~ -38) -> this J is NOT "
    "the RHP jump equivalent to tau(s) != 0; the H = I dissipativity "
    "J + J* succeq 0 (holds on TRUE with min eigenvalue 1.93-1.99 AND "
    "on WPERM despite tau-zeros) is the wrong sufficient condition "
    "and is dropped.  Contractive metrics H - J* H J succeq 0 in "
    "source-explicit classes (scalar, diag(w1,w2) with "
    "w in {|z|^alpha, e^{beta |z|}, arch^gamma, comb^delta}, "
    "s-dependent scalars, Sylvester rho): best H = diag(arch^1.50, "
    "arch^1.50), TRUE worst margin -8.17e-10 (r625 first pass "
    "-3.36e-7; bar -1e-12), WPERM -7.9e-9 ... -4.4e-4, EPSTEIN "
    "-2.7e-2 ... -6e11, SCRAMBLE -3e6 ... -9e57; controls fail "
    "pointwise before their tau-zero (5/5).  Typing (parent): the "
    "vanishing-lemma route is NOT testable on the corpus discrete "
    "object -- it first needs the genuine Riemann-Hilbert problem "
    "whose solvability is equivalent to the window determinant "
    "(continuous IIKS kernel, correct contour/symmetry); the "
    "near-miss margins are therefore not evidence either way.  "
    "Probe experiments/tfpt-discovery/iiks_vanishing_metric_probe.py.  "
    "SPEC_SHA "
    "7a4257e3d9e7185a3e447d4e3320b259ade5e4212ed91793c04dc0c358593db9; "
    "NUM_SHA prefix 2d066e2d; probe SHA "
    "973a1ce25d042acb14574b484b38b00bda8922ad05a41c84e31969f6c33aae2b.  "
    "CHECKS 19/19.  No RH claim"
)

_R626_STATUS = (
    "Xi finite-free collision scout "
    "(round 626, XI.FINITEFREE.COLLISION.01; exploration scout; "
    "experiments-side sealed probe, NO ledger row): VERDICT "
    "COLLISION_DETECTOR_CALIBRATED_NO_BARRIER.  Identity "
    "d/dt log|Disc(P_t)| = 4 * Phi_N(P_t) along the dBN heat flow "
    "(rel error 8.9e-11) -> the collision barrier int Phi dt < inf "
    "is equivalent to Disc != 0 along the path (no independent "
    "content).  Taylor sections of Xi are not real-rooted at t = 0: "
    "N = 6/8/12 have 0 real roots; the gamma_1 pair becomes real "
    "only at N = 16-20 (|z - gamma_1| = 4.4e-4 / 1.1e-7), the second "
    "real root is not gamma_2 (17.23/19.39 vs 21.02); t0(N) = 7.78, "
    "9.13, 11.43, 13.08, 14.97 is always a spurious far-pair "
    "collision; inner collisions at t_c > 0 for every N.  Detector "
    "calibrated on the hyperbolic control "
    "S_N = Pi (1 - x^2/gamma_k^2): eps_crit = -3.65e-4 (a1, N = 8), "
    "t_c = 0.597, log10|Phi| up to 7.90.  Coefficient side: Turan on "
    "c_n = n! a_n holds (min ratio 1.02), Newton/Laguerre on the "
    "sections fails (0.51); no simple coefficient inequality implies "
    "inner Disc > 0.  Probe "
    "experiments/tfpt-discovery/xi_finitefree_collision_probe.py.  "
    "SPEC_SHA "
    "c7cef97475d9d66be6c877081aaee6ef91a8bf7b059c72b91d0ceeeb4111417c; "
    "NUM_SHA prefix f533d168; probe SHA "
    "c475006327b042819a06f449f8f1ffd89052d23bdac533a5e3bf8814be78b918.  "
    "CHECKS 51/51.  No RH claim"
)

_R627_STATUS = (
    "A-F two-moment optimizer scout "
    "(round 627, PRIME.INERTIA.TWOMOMENT.OPT.01; "
    "experiments-side sealed probe, NO ledger row): "
    "VERDICT NO_GAIN.  A-F two-moment functional "
    "R(psi) = [int psi^2 + iint |u-v| psi(u) psi(v)]/(int psi)^2, "
    "p = 2 - R on supp psi subset [-1/2, 1/2]; Euler-Lagrange "
    "(I+K)psi = lambda * 1 => psi'' + 2 psi = 0 => unique "
    "critical point psi* = cos(sqrt(2) t) (Montgomery-Taylor), "
    "p* = 0.6725007037 (N = 8-64 identical, omega-scan optimum "
    "sqrt(2)); positivity slack (min 0.760 > 3/4); the proved "
    "ceiling 0.6818287 bounds the richer two-moment + on/off-block "
    "certificate, not the window optimum; gap 9.3e-3 not closable "
    "by window optimization.  Probe "
    "experiments/tfpt-discovery/af_twomoment_optimizer_probe.py.  "
    "SPEC_SHA "
    "9b95f564e71001d728d4801abb1c23a2c094d9f3c6a663883519d08ec231e451; "
    "probe SHA "
    "da1a91181661b8c0775539fb0e3894e1ab088b2cea7fbf8209a8ed4f613b8eb3.  "
    "CHECKS 17/17.  No RH claim"
)

_R628_STATUS = (
    "Window-box verifier scout "
    "(round 628, PRIME.WINDOW.BOX.VERIFIER.01; "
    "experiments-side sealed probe, NO ledger row): "
    "VERDICT COMPRESSION_CERTIFIED_BOX_NUMERICAL.  Interval-certified "
    "(40 digits, interval Cholesky/Weyl) positivity of the finite "
    "window compression: lambda_min >= 1.05e-7 (L = 0.55, N = 24, "
    "primes {2,3}), >= 6.1e-11 (0.65, N = 40), >= 9.3e-17 "
    "(0.80, N = 40, {2,3,4}) -- cancellation depth up to 6e14.  "
    "Rigorous zero-free box NOT closed: the unconditional on-line "
    "majorant via Trudgian |S(T)| <= 0.112 log T + 0.278 log log T "
    "+ 2.51 (JNT 134, 2014) is ~1e7 too loose; numerical box "
    "nonempty (L = 0.80: beta_min = 0.55 for gamma <= 25 and 50/60; "
    "0.70 at 30; 0.80-0.90 at 35-45); log Gamma_num = -1.24 + 6.86 L "
    "(sigma = 0.1).  Missing lemma: local zero-density bound or "
    "enumerated zeros (then Booker/Turing-equivalent).  Typed as "
    "the explicit-formula verification method (Booker, Exp. Math. 15 "
    "(2006)) in window form.  Probe "
    "experiments/tfpt-discovery/window_box_verifier_probe.py.  "
    "SPEC_SHA "
    "36c0e66a71c6b8a3dc7db7682e8d63b4eaa63876ecb5396b68fbdd778faf749e; "
    "NUM_SHA prefix 84aaf685; probe SHA "
    "9c99ed6a19881be92944ad144e871c5e7b06d48f39f273d33aad56be2f724570.  "
    "CHECKS 12/12.  No RH claim"
)

_R629_STATUS = (
    "Certificate-class atlas scout "
    "(round 629, PRIME.CERTIFICATE.ATLAS.01; "
    "experiments-side sealed probe, NO ledger row): "
    "VERDICT ATLAS_NO_NEW_UNCONDITIONAL_GAIN.  LP over hypothetical "
    "zero configurations: A1 two-moment reproduces 1 - p0 = 0.3181713 "
    "(p0 = 0.6818287); A2 + N(T)/S(T): unchanged; A3 + prime-free "
    "window positivity (CC 2021): redundancy 0 (min slack 2.2e-4); "
    "A6 + Huxley zero density: unchanged (off-line mass forced to "
    "sigma <= 1/12, already at sigma -> 0).  Conditional rows: "
    "GUE k = 3 -> 5/6, k = 4 -> 31/36; pair correlation "
    "alpha_max = 1.5/2/inf -> 0.7046/0.7159/0.7500.  Reading: only "
    "correlation input beyond support 1 buys proportion.  Probe "
    "experiments/tfpt-discovery/certificate_class_atlas_probe.py.  "
    "SPEC_SHA "
    "0bf7c64f8b1d463157abac3d6f1840aa5081c0e0e6186c18eff04e44311b0481; "
    "probe SHA "
    "4dae1fbe3d02f0b323692bc63a7a80ff6002835b7da064bb847c4bcf8646a448.  "
    "CHECKS 15/15.  No RH claim"
)

_R632_STATUS = (
    "Jet-deflated L_det scout "
    "(round 632, PRIME.WINDOW.JETDEFLATION.01; reviewer-proposed; "
    "experiments-side sealed probe, NO ledger row): "
    "VERDICT JET_GAIN_SMALL.  Baseline reproduces r619 L_det "
    "(0.55/0.50/0.80).  Deflation hat f^{(r)}(20) = 0: m = 0 no "
    "gain (G = 0), m = 1 G = 0.40 (L_det 0.55 -> 0.95 at (0.6, 20)), "
    "control at gamma = 50 moves 0.10-0.20; deflating the first "
    "eight true zeros: G = 0.65 and sector Ritz floor at L = 0.6 "
    "jumps 1.76e-9 -> 2.02.  Coverage kill: deflating all zeros up "
    "to Gamma = 50 already needs dim K/N = 0.50 (above Nyquist 31.8), "
    "Gamma = 100 -> 1.45 (sector collapses), Gamma = 200 -> 3.95 -> "
    "sectorization is not a cheap RH-free statement "
    "(recoordinatization).  Deflation at 20 does not touch the "
    "odd-sector failure (peak frequency 4.6/3.9).  Probe "
    "experiments/tfpt-discovery/jet_deflated_ldet_probe.py.  "
    "SPEC_SHA "
    "31a29760f5a13f17427fc45069730153c2786c91355252f7ea44f4795bb92688; "
    "RESULT_SHA prefix 6299cedc; probe SHA "
    "63ecb68fa164746d0004db2948496c563b0588cf9dc613f5851835c67338f9c1.  "
    "CHECKS 14/14.  No RH claim"
)

_R630_STATUS = (
    "Margin-law symbolic-regression scout "
    "(rounds 630/630b, PRIME.MARGIN.LAW.SYMREG.01; "
    "experiments-side sealed probe, NO ledger row): "
    "FIRST RUN: VERDICT MARGIN_LAW_UNRESOLVED.  L_cross = 0.3716, "
    "double-precision SVD floor L = 0.78; 19/19, 166 s, dual-run "
    "identical.  ADDENDUM r630b (tall QR, 40 digits, "
    "N in {40,60,80,120,160}, L in [0.30,1.40]): decision "
    "N_LIMITED_ARTIFACT -- lambda*(L) converges in N for L<=1 "
    "(35/36 points, rel. change 120->160 median 4.8e-2) but NOT "
    "for L>1 (0/20); converged log-slopes -50.6 (band 0.3-0.6, "
    "N-stable to 3 digits) and -116 (band 0.6-1.0, stable for "
    "N>=80); lambda*_160(0.6) = 1.65e-9, lambda*_160(1.0) = "
    "9.93e-30; no converged holdout, descriptive quadratic C = 95.5 "
    "(neither 2 gamma_1 = 28.27 nor gamma_1^2/pi = 63.6) -- both "
    "the Widom-L^2 and the -2 gamma_1 L^2 readings unsupported.  "
    "N2: converged minimizer nulls 4707-4831 of 5000 zeros "
    "(frequency-sparse).  N3 synthetic controls (alpha = fitted "
    "decay constant): true 169, constant-density 101, all ordinates "
    "scaled to first zero at 10: 105, at 20: 271, only first zero "
    "moved to 20: 172 -> density-driven (Landau-Widom plunge from "
    "the unconditional N(T) profile of the low band), not "
    "band-edge; RH-neutral.  N4 dBN gap functional B_k on 4999 "
    "gaps: max 41.8, p99 11.5, median 2.13, fraction B_k < 2 = "
    "0.470 (0.515 after compressing one gap by 0.3) -> no universal "
    "gap barrier.  The r619 log-slopes -77/-79 at L = 0.9-1.4 were "
    "measured at fixed N = 80 beyond the SVD floor and are "
    "N-artifacts (corrected by r630b); r619 verdicts RELAY_UNIVERSAL, "
    "leads Delta ~ 0.015, L_det table are unaffected.  Probe "
    "experiments/tfpt-discovery/margin_law_symreg_probe.py.  "
    "SPEC_SHA "
    "87febb97aaee5dcdad9b9d5a543fd5f22c4803059c16232b2f2c9ef8cc843aee; "
    "RESULT_SHA prefix a0765d7f; probe SHA "
    "5b3d112576ff6d8672bb42d3f80077eb7916f6b524e8dbaa380076b6f2e7b90f.  "
    "CHECKS 19/19.  No RH claim"
)

_R633_STATUS = (
    "Frontier follow-ups scout "
    "(round 633, PRIME.FRONTIER.FOLLOWUPS.01; follow-ups on sealed "
    "objects; experiments-side sealed probe, NO ledger row): "
    "16/16, 18 s, dual-run identical.  F1 A_COMPACT_OTHER(p~1.02): "
    "a_max(sigma, gamma*) = c sigma^{1.024} (log gamma*)^{-1.65} "
    "(r^2 0.945, n = 24), linear in sigma, not sigma^2 (mechanism: "
    "phase threshold cos(sigma(gamma-omega)/2a) < 0 <=> "
    "a < sigma|gamma*-omega|/pi, not the amplitude gain); a0 = 0.720 "
    "at (sigma, gamma*) = (1/2, 20), extrapolated 0.714 at gamma_1; "
    "true zeros min_omega Z(a, omega) > 0 for a in {1,5,25,100,250}; "
    "adversarial sigma = 1/2 negative only at a = 1 "
    "(Z = -3.86e-4 at gamma_1).  Parent typing: compactification "
    "removes only the a -> inf end (RH-blind wide-frequency packets); "
    "the RH-relevant end a -> 0 stays unbounded; a Lean theorem would "
    "need an external explicit N(T)/gap bridge -> cosmetic, not "
    "pursued.  F2 FORWARD_INCREASES_MARGIN: Hellmann-Feynman = "
    "Loewner to 1e-15; c(L) = d_t log lambda* = +0.315/+0.582/+0.764 "
    "at L = 0.40/0.55/0.80 (lambda* 1.89e-4/5.70e-8/2.02e-17), "
    "t* = -3.18/-1.72/-1.31 (O(1), not vacuous); with injection "
    "(beta, gamma) = (0.6, 20) at L = 0.55: d_t lambda* < 0.  Typing: "
    "sign discriminates on/off-line but the monotonicity runs in the "
    "proof-useless direction -> detector, no lever.  "
    "F3 RANDOM_EULER_REFUTED: lambda_min(POLE+ARCH) = "
    "-0.0783/-0.430/-0.926 at L = 0.40/0.549/0.80 (reproduces r623 "
    "to 1e-3); MC 200 Haar phase draws at L = 0.55: mean lambda_min "
    "= -0.496, std 0.317, 99.5 pct negative, vs true lambda* = "
    "5.70e-8; coherence C(L) = 1 at h0 (all g_{h0}(log q) same sign); "
    "Baker: required delta = O(1) vs toy linear-forms bound 4.6e-8 "
    "-> 7.3 decades.  Typing: window positivity beyond L_cross is "
    "arithmetic phase coherence of the prime terms; magnitude-only "
    "and Diophantine-approximation arguments are dead as a class "
    "(measured no-go; promotion candidate with r615/r619).  "
    "F4 LEAD_LAW_INVARIANT: growth exponent alpha = 8.18 "
    "(target 2p+1 = 7); argmin of the fitted margin + overlap laws "
    "predicts 0/18 leads within 20 pct -> Delta ~ 0.015 is not a "
    "corollary of those laws; open descriptive invariant.  Probe "
    "experiments/tfpt-discovery/frontier_followups_probe.py.  "
    "SPEC_SHA "
    "ee7c7ba7e616add967455f2efdefaf00a326a8b78be7253cf10504016907ebf1; "
    "RESULT_SHA prefix 814abdf5; probe SHA "
    "9f5287e7f9fbf174bff5b54b935de7212b3c94f4c92c020f5749569d99011839.  "
    "CHECKS 16/16.  No RH claim.  CORRECTED BY r637: F3 RANDOM_EULER_REFUTED (99.5 pct negative under Haar) STANDS; the phrase 'coherence C(L)=1 / phase coherence' is NOT the mechanism -- C=1 is generic for minimizers and holds for the negative Haar draws too.  CORRECTED BY r635/r636: F4 LEAD_LAW_INVARIANT is VOID (based on withdrawn N=80 Delta~0.015 values)."
)

_R635_STATUS = (
    "Relay-lead precision scout "
    "(round 635, PRIME.RELAY.LEAD.PRECISION.01; "
    "experiments-side sealed probe, NO ledger row): "
    "VERDICT LEAD_PARTIAL.  11/11, 1260 s, dual-run identical.  "
    "r619 predecessor was the frozen D2 form (events q' < q only); "
    "D1 (true minus q) implemented, identical here.  mp Cholesky "
    "PSD-boundary bisection, N in {80,120,160}, damped Legendre: "
    "converged leads Delta_2=0.0253, Delta_3=0.0083, "
    "Delta_4=0.0064 (0.00606 at N=160), Delta_5=0.0034 "
    "(0.00275 at N=160); Delta/s_q = 0.125/0.058/0.058/0.020; "
    "lambda*(L_q) = 1.36e-3 / 5.93e-8 / 8.72e-13 / 8.69e-17; "
    "initial negative rate r_q = 3.38e-2 / 3.14e-6 / 7.35e-11 / "
    "1.32e-15.  Probe why: 'positive N-stable leads only at "
    "small L_q (4/18 events; later events already indefinite at "
    "entry)'.  For q=7..32 the probe reports Delta=0 with "
    "lambda_min<0 already at L_q, conv=0 (q=7: L=0.973, "
    "lambda_min=-6.99e-11).  Probe does not mark floor-limited.  "
    "PARENT TYPING: (i) the r619 'greedy law' Delta ~ 0.015 "
    "nearly constant across 18 events was an N = 80 "
    "double-precision artefact -- WITHDRAWN; the converged leads "
    "decrease steeply (0.025 -> 0.003) and track the collapsing "
    "entry margin; (ii) for q >= 7 the value lambda_min < 0 "
    "'at entry' is NOT a negativity of the true form "
    "(RH-consistency and the r628 certification forbid it: the "
    "true form for L < L_7 equals the D2 predecessor); it means "
    "lambda*(L_7 ~ 0.97) ~ 1e-25 lies below the accuracy floor "
    "of the 40-digit prime-side builder (~1e-17..1e-20) -> "
    "Delta_q for q >= 7 is UNMEASURABLE at this precision, not "
    "zero.  Not spacing-limited (s_31 = 0.0159 but Delta "
    "undetermined there).  Probe "
    "experiments/tfpt-discovery/relay_lead_precision_probe.py.  "
    "SPEC_SHA "
    "28db9bef54dd4cd67608d01df842f02364a688dbfcafb4274fdebcac4ea1c820; "
    "RESULT_SHA "
    "3457e907c2c5c9ef8bf3c160ae0636c186ad5f51b390d51018e208c58fafc265; "
    "probe SHA "
    "36c06826fcd3461c76098f72d94b2faab4ddf4a20ce162acee5cbd9857dfe749.  "
    "CHECKS 11/11.  No RH claim"
)

_R636_STATUS = (
    "Relay-lead law scout "
    "(round 636, PRIME.RELAY.LEAD.LAW.01; "
    "experiments-side sealed probe, NO ledger row): "
    "VERDICT LEAD_LAW_PARTIAL.  6/6, 0.5 s, dual-run identical.  "
    "Only four converged leads = training set, holdout empty; "
    "peak relative errors: M1 margin/rate linear 18.4 (q=5), "
    "M1 quadratic 4.39 (q=2-4 within 12-18 pct, q=5 fails), "
    "M2 edge-sliver competition 1.96, M3 grammar "
    "c0 + w^3 + lambda c^2 0.0026 (3 parameters on 4 points -- "
    "interpolant, no evidence), M4 spacing 48.8 / alpha s 2.70 "
    "(alpha=0.074).  No model < 20 pct on all four; spacing "
    "does not win; with four points there is nothing to derive.  "
    "PARENT TYPING: the 'lead law' as a message is dissolved -- "
    "Delta_q is a corollary of the margin collapse, not a "
    "separate invariant; r633-F4 LEAD_LAW_INVARIANT referred to "
    "the withdrawn N=80 values and is void.  Probe "
    "experiments/tfpt-discovery/relay_lead_law_probe.py.  "
    "SPEC_SHA "
    "6bf7a7ee31e3f41736bb04dc97ca1370aaf6c8ad1ff80379408b9012b694054b; "
    "RESULT_SHA "
    "2a6bd720b7494840e7235475b446e2b1cd8a71263a92efaac789cff04ae25aa9; "
    "probe SHA "
    "ee2deb462adf5487965b97a8b1349c7ea4bf8660c5077d2b543e2ffc1de1d2ad.  "
    "CHECKS 6/6.  No RH claim"
)

_R637_STATUS = (
    "Relay vote-map scout "
    "(round 637, PRIME.RELAY.VOTE.MAP.01; "
    "experiments-side sealed probe, NO ledger row): "
    "14/14, 27.7 min dual, mp 40 digits N=80 (N=120 check agrees "
    "at L=0.55/0.80).  Worker verdict VOTE_MODE_SPECIFIC "
    "(k_thr=3) + FLIP_COUNTEREXAMPLE.  C0=1 at all nine "
    "L in [0.40,1.00]; modes k=0,1,2 unanimous at all L, "
    "k>=3 split (70/90 (L,k)); h0 is R_q-EVEN-dominant on every "
    "overlap (||f-||^2/||f+||^2 = 0.33..0.99 < 1): at the "
    "critical mode every present prime term ADDS positivity "
    "(g = +(||f+||^2 - ||f-||^2)), consistent with the odd/edge "
    "failing mode of the predecessor (r619/r620) where the "
    "missing prime would have added.  Flip test: 0/19 R_q-odd "
    "flips lower Q (first: L=0.40, q=2, Delta Q = +4.30e-3) -> "
    "FLIP_COUNTEREXAMPLE, the variational lemma in the odd "
    "sector is refuted.  Controls: SCRAMBLE minimizer C=1 at "
    "ALL L (incl. 5 events at L=1.0), POLE+ARCH ancestor C=1 at "
    "all L; WPERM splits from L=0.90 (0.715, 0.444), EPSTEIN "
    "from 0.70 (0.941).  Euler coherence testable only for "
    "2 vs 4 below L=1: agreement 27/36=0.75, h0 agrees at "
    "L=0.90/1.00.  Haar MC: L=0.45 frac_neg 0.955 with "
    "frac_unanimous 1.000; L=0.55 1.000/1.000; L=0.70 "
    "1.000/0.865, corr(C, lambda_min)=-0.17.  PARENT TYPING: "
    "unanimity is GENERIC -- a geometric property of "
    "edge-localized low minimizers of translation-type forms "
    "(SCRAMBLE reproduces it at every L), not an arithmetic "
    "message; the coherence index C is not a positivity "
    "predictor (Haar draws unanimous yet negative).  Probe "
    "experiments/tfpt-discovery/relay_vote_map_probe.py.  "
    "SPEC_SHA "
    "44bf67f8ba7d07d3e03450e310412e4cc93478dae5b345a2158df52191a64cfc; "
    "RESULT_SHA prefix 540557ad; probe SHA "
    "fc5c1426c996df526faeb3f8f50f84367b5d7563e173ff63c682fce892e2ce3d.  "
    "CHECKS 14/14.  No RH claim"
)

_R638_STATUS = (
    "First-contact + Selberg square-completion scout "
    "(round 638, GABOR.CONTACT.SELBERG.01; experiments-side "
    "sealed probe, NO ledger row): 14/14, ~338 s dual, "
    "byte-identical.  Object: pure-Gabor zero side G(a,w) = "
    "POLE - PRIME + ARCH (r608 identity A); attack: at a first "
    "touching point (a*,w*) the contact conditions plus Selberg "
    "symmetry Lambda log + Lambda*Lambda = Lambda_2 should yield "
    "an operator L with LG = ||A||^2 + R >= 0.  Pre-registered "
    "Toeplitz gate: the Selberg convolution term sum_N "
    "(Lambda*Lambda)(N) psi(log N) is a HANKEL form in "
    "(log m, log n); a square needs the kernel [psi(u_i+u_j)] "
    "PSD.  T2: on 466 prime-power nodes (n <= 3000), 15 "
    "operator-generated psi = t^k e^{-t/2} e^{-a t^2/2} "
    "{cos, sin, 1}(omega t) with k <= 4, 15 cells (a,omega) in "
    "{1,0.5,0.3,0.1,0.05} x {14.13,30,100}: best PSD-combination "
    "lambda_min = -0.0097 ... -0.0568 (Frobenius-normalised, "
    "tolerance -1e-9), GATE_PASS 0/15; DC 2x2-minor violation "
    "fraction 1.0 everywhere (Gaussian factor "
    "e^{-a(u_i-u_j)^2}) -> TOEPLITZ_GATE_FAIL.  G3: the only "
    "squares compatible with the prime-side frequency support "
    "{log n} are Euler-local sum_p |A_p|^2; their Fejer-Riesz "
    "DC cost DC_lower/(POLE+ARCH) = 3.28 (a=0.3, omega=50), "
    "4.35 (0.3, 30), 8.39 (0.3, 14.13) -> "
    "EULER_LOCAL_SQUARE_COSTS_TRIVIAL_MAJORANT.  T3 (synthetic "
    "off-line catalogs on 2000 on-line ordinates): first contact "
    "a* = 0.1418/0.0877/0.0370/0.1126 for (sigma,gamma0) = "
    "(0.4,100)/(0.25,100)/(0.1,100)/(0.4,250), omega*-gamma0 = "
    "0.66/0.62/0.61/0.55 vs pi a*/(2 sigma) = 0.56/0.55/0.58/"
    "0.44, off-line/on-line block ratio 1.0000 at contact; "
    "d_a Z = (1/2) d^2_omega Z at contact with r_heat <= "
    "1.6e-16 (cos) / 1.5e-16 (lobe): the two contact conditions "
    "are ONE (CONTACT_CONDITIONS_COLLAPSE); m(a*/2, a*/4, a*/8) "
    "all negative (NEGATIVITY_DOWNSET; the heat semigroup runs "
    "small a -> large a).  T4 (true zeta, prime side to n <= "
    "4.6e6, EF sanity 2.2e-14): G >= 0 on omega in [10,50] for "
    "a = 1/0.5/0.3 (min 3.0e-4 / 1.2e-7 / 2.2e-12); at the 8-9 "
    "local minima per a the Selberg part of d^2_omega PRIME has "
    "the helpful sign in 0.25/0.22/0.33 (MAIN) vs 0.22/0.31/"
    "0.22 (SCRAMBLE) vs 0.29/0.20/0.20 (WPERM): "
    "SELBERG_SIGN_INDEFINITE + WORLD_BLIND; median "
    "|Selberg_1|/|Lambda_2,1| = 1.33/0.88/0.74 -- the Selberg "
    "split relocates the cancellation between two equal-size "
    "parts (same finding as CCCXXXI SELBERG-INSUFFICIENT on the "
    "window object).  PARENT TYPING: the square-completion "
    "engine of the first-contact attack is structurally "
    "unavailable -- Selberg's convolution is Hankel (frequencies "
    "log m + log n), squares of prime Dirichlet polynomials are "
    "Toeplitz (log m - log n); the compatible Euler-local "
    "squares cost the trivial majorant; single-sum (Lambda_2, "
    "Lambda) terms cannot repair a non-PSD Hankel part "
    "(bordered-matrix argument).  The first-contact frame itself "
    "carries one differential condition, not two.  Lane "
    "GABOR.CONTACT.SELBERG.01 = KILLED(STRUCTURAL), STOP.  Probe "
    "experiments/tfpt-discovery/gabor_first_contact_selberg_probe.py.  "
    "SPEC_SHA "
    "22a9284272e345a690dc7550c401f1bd7090647381b0061bce50b2a64d0c3aa8; "
    "RESULT_SHA prefix 58a36aff; probe SHA "
    "2ab532bceeb0dfd9bb863ab40fda2b87ea9c187b658fe7ef9223f75360e751f9.  "
    "CHECKS 14/14.  No RH claim"
)

_R639_STATUS = (
    "Lamzouri Hilbert-variant adjudication "
    "(round 639, PRIME.PORT.EXTERNAL.HILBERT_VARIANT.ADJUDICATION.01; "
    "experiments-side sealed probe, NO ledger row): "
    "23/23, 22 s, dual-run identical.  EXTERNAL arXiv:2609.02882v1 "
    "(Lamzouri, 2026-09-02): new proof of the Alpoge--Furman/Anthropic "
    "theorem (>= 0.6725 simple on the line, >= 0.83625 distinct) "
    "replacing the finite Weil-form matrix + rank-trace inequality "
    "by a Hilbert-space (Bessel) inequality on L^2(-1/2,1/2) and "
    "applying Montgomery pair correlation in the unconditional "
    "BGSTB24 Lemma 5 form (supp f in [-1,1]).  VERDICT "
    "PROPOSITION_REBUILT + SAME_CLASS(TWO_MOMENT) + CONSTANTS_IDENTICAL "
    "+ WALL_LOCATION_CONFIRMED(SUPPORT_ONE) + MT_OPTIMAL_SUPPORTED "
    "+ NO_IMPORT(UNCHANGED) + SOURCE_NOTE(AXIOMPROVER).  Proposition "
    "rebuilt exactly on 921 synthetic conjugation-invariant "
    "multisets (3 windows x 307 instances; Bessel, three range "
    "inequalities, Sum alpha_j = |Z|; min slack -1.8e-15, bound "
    "saturates at n).  Class: C_eta = Q(0) + 2 int_0^1 alpha "
    "Q(alpha) == r267 functional R(eta^2) to 1.7e-15 (R(psi_0) = "
    "4/3, R(psi_MT) = C_MT = 1.3274992963206); bound 2N - HS^2 "
    "== A--F chain 4 tr G - 2N - HS^2 at tr G = N (sympy) -> atlas "
    "class A1 unchanged, ceiling 0.6818287 applies.  Constants: "
    "C_0 = 2 - C_MT = 0.672500703679 == r627 p* (2e-11), "
    "C_1 = 0.836250351840, gap to p_0 9.328e-3.  Wall: Q = eta^2 "
    "* eta^2 vanishes for |alpha| >= 1 exactly; widening supp eta "
    "to (-0.6, 0.6) puts 2.8 pct of the Q mass beyond 1 (BGSTB "
    "inapplicable) -- the sole arithmetic input is the proven "
    "pair-correlation range |alpha| <= 1 = r267 X <= T boundary "
    "= PAIRCORR wall; under the PCC form factor min(|alpha|,1): "
    "p(lambda) = 0.6725/0.866/0.932/0.976/0.989/0.996 at lambda "
    "= 0.5/0.75/1/1.5/2/3 (monotone; GLSS25 limit 1); p(0.5) sits "
    "1.0e-5 above C_0 (product quadrature of the |u-v| kink, "
    "inside the frozen 2e-4 tolerance; the kink-split value is "
    "C_MT).  MT optimality: 200 random admissible psi all R >= "
    "C_MT (min excess 0.41), local second difference >= 1.9e-6.  "
    "Lean: AxiomProver certificates -- Proposition unconditional, "
    "Theorem modulo BGSTB Lemma 5 + Riemann--von Mangoldt as "
    "hypotheses (contrast A--F v1.0 kernel-checked modulo EnclOK).  "
    "Renumbered 638 -> 639 before sealing (638 taken by r638L and "
    "a parallel probe).  Probe "
    "experiments/tfpt-discovery/lamzouri_hilbert_adjudication_probe.py.  "
    "SPEC_SHA "
    "4bc444228a9ae6a488c4b70eac77fcdbad8e15370df42bd359faaf060c046b38; "
    "probe SHA "
    "61fbb4b93e8c640f5fe0c39c43355779cff86cc9efc80b2a01cc7bc4cda9d654.  "
    "CHECKS 23/23.  Follow-up to r267/r616/r627; no RH claim"
)

_R490_STATUS = (
    "classical Weil operator residual at L=0.3 "
    "(round 490, PRIME.RDAGGER.OPERATOR_RESIDUAL.01; "
    "experiments-side, NO ledger row): "
    "VERDICT STUCK(off/s=5.86-eats-1000x; "
    "GL-tiny-not-the-certificate;+FINAL_CHECKPOINT).  "
    "r488 G-certificate (N=5, s=0.05, BS=0.99439) "
    "is Galerkin-level; operator leftover "
    "(1-P_5)A+ u_1 / s = 5.86 vs margin 5.6e-3 "
    "(eats ~1000x).  Even ground already 8.1e-2.  "
    "Raising M does not help; [T,inf) tail grows.  "
    "Full-space GL leftover of truncated A+ is "
    "tiny at n>=96 (3e-6) but is NOT the "
    "certificate residual.  B1 (dps-Nyström) "
    "does not help: off-space is float-visible.  "
    "Round 10 of the 0.3 keystone; no eleventh "
    "form.  Smoke 11/11, full 16/16, "
    "SPEC_SHA 162707324dc6b05c.  Companion "
    "rh/problem/operator_residual.tex + "
    "verify_operator_residual.py "
    "OPERATOR_RESIDUAL VERIFIED -- "
    "STUCK(off/s=5.86-eats-1000x; "
    "GL-tiny-not-the-certificate;+FINAL_CHECKPOINT).  "
    "NO L* claim, NO R-dagger claim, NO RH claim, "
    "NO anti-RH claim"
)

_R489_STATUS = (
    "outer bridges fixed-support channel reduction "
    "(round 489, PRIME.RDAGGER.OUTER_BRIDGES.02; "
    "experiments-side structural seal, NO ledger row): "
    "VERDICT COMB_CLOSED / POLAR_INTEGRAL_CLOSED / "
    "DENSE_COMPLETION_ONE_SORRY.  Topology is uniform convergence "
    "on a common fixed support plus L1; the autocorrelation witness "
    "is compactly supported in L2.  Common-anchor finite comb "
    "continuity and the bounded-cosh standard polar integral "
    "continuity are proved.  The remaining density package is the "
    "transparent conjunction of dyadic L2 step/autocorrelation "
    "density, r475 u-space arch continuity, and the r376 native-grid "
    "pole integral dictionary.  Smoke 12/12, "
    "SPEC_SHA 9952567c0a594287; verifier 6/6.  Lean sorry census "
    "9 -> 8 (external 4 -> 3).  r547 census-gate update: "
    "project-sorry-census expected 7 -> 9 (tracked set "
    "Source/Elementwise/Canonical/ExternalBridges/GaborSeparation; "
    "GaborSeparation carries 2 named inputs).  Probe SHA "
    "re-pinned; SPEC_SHA unchanged.  NO L* claim, NO R-dagger "
    "claim, NO RH claim, NO anti-RH claim"
)

_R488_STATUS = (
    "classical Weil resolvent solve at L=0.3 "
    "(round 488, PRIME.RDAGGER.RESOLVENT_SOLVE.01; "
    "experiments-side, NO ledger row): "
    "VERDICT REDUCED(R-not-coercive; "
    "s=0.05-G-cert-N5-BS=0.994; operator-R-gap-open).  "
    "lambda_min(R) collapses with n (0.337/0.106/0.076 "
    "at n=48/96/128); shift s=0.05 mandatory.  "
    "s=0 recovers r486 BSE=0.993651.  "
    "G-certificate G^{1/2} B G^{1/2} at s=0.05 is "
    "0.99415 (N=3) / 0.99439 (N=5); residual 2e-16.  "
    "N=3+|sig0|*rest/s OVERSHOOTS 1.078 (not a SATZ).  "
    "N=5 tail 5.5e-7, GBG+bud/s=0.99440.  "
    "Operator R vs Galerkin R gap OPEN.  "
    "Smoke 12/12, full 18/18, SPEC_SHA 2ce1bae7228fb033.  "
    "Companion rh/problem/resolvent_solve.tex + "
    "verify_resolvent_solve.py RESOLVENT_SOLVE VERIFIED -- "
    "REDUCED(R-not-coercive; s=0.05-G-cert-N5-BS=0.994; "
    "operator-R-gap-open).  "
    "NO L* claim, NO R-dagger claim, NO RH claim, "
    "NO anti-RH claim"
)

_R487_STATUS = (
    "outer bridges lane start "
    "(round 487, PRIME.RDAGGER.OUTER_BRIDGES.01; "
    "experiments-side structural seal, NO ledger row): "
    "VERDICT OUTER_LANE_TYPED / DENSE_LIMIT_REDUCED / "
    "ZETA_INTERFACE_PROVED.  FullWeilTest is a continuous even "
    "fixed-support real autocorrelation.  Dense extension is split "
    "into fullWeil_fixedSupport_grid_density and "
    "fullWeil_channel_continuity; channel-limit assembly, closed-cone "
    "positivity, and the public wrapper are proved.  The Mathlib "
    "RiemannHypothesis interface is proved from the named "
    "off-critical separation brick.  Mathlib has riemannZeta and "
    "Mellin transform/inversion/Mellin-to-Dirichlet infrastructure, "
    "but no ZetaZero enumeration, multiplicity API, or Guinand--Weil "
    "formula.  Smoke 12/12, SPEC_SHA 5ea36777bc6077e6; verifier 6/6.  "
    "Lean sorry census 8 -> 9 because the old density sorry was "
    "honestly split into two.  r547 census-gate update: "
    "project-sorry-census expected 7 -> 9 (tracked set "
    "Source/Elementwise/Canonical/ExternalBridges/GaborSeparation; "
    "GaborSeparation carries 2 named inputs).  Probe SHA "
    "re-pinned; SPEC_SHA unchanged.  NO L* claim, NO R-dagger "
    "claim, NO RH claim, NO anti-RH claim"
)

_R486_STATUS = (
    "classical Weil Woodbury/Birman-Schwinger enemy "
    "representation at L=0.3 "
    "(round 486, PRIME.RDAGGER.WOODBURY_MINF.01; "
    "experiments-side, NO ledger row): "
    "VERDICT REDUCED(enemy-3dim-BS<1; Q_E-Higham; "
    "operator-Rinv-open).  "
    "Route (b)/(ii) first: A- = |sigma| 1_{|t|<t_c} has "
    "tr(K_tc)=1.201 and Slepian (0.859, 0.314, 0.027); "
    "enemy is 3 certified modes (no garbage).  "
    "BS lmax=0.99409 (E012 0.99365), margin 5.91e-3; "
    "Schur of R does not move the margin.  "
    "Q_E Higham mu>=2.87e-3.  r476 Dirichlet Q=1.178e-2 "
    "hits [1.150e-2, 1.192e-2].  Trace-rest after 012 "
    "7.81e-4.  Operator R^{-1}=(A++Pi)^{-1} OPEN.  "
    "Route (a) not opened.  Smoke 16/16, full 23/23, "
    "SPEC_SHA 7f306746b2a2b517.  "
    "Companion rh/problem/woodbury_minf.tex + "
    "verify_woodbury_minf.py WOODBURY_MINF VERIFIED -- "
    "REDUCED(enemy-3dim-BS<1; Q_E-Higham; "
    "operator-Rinv-open).  "
    "NO L* claim, NO R-dagger claim, NO RH claim, "
    "NO anti-RH claim"
)

_R485_STATUS = (
    "classical Weil weighted Schur at L=0.3 "
    "(round 485, PRIME.RDAGGER.WEIGHTED_SCHUR.01; "
    "experiments-side, NO ledger row): "
    "VERDICT REDUCED(A-GO; finite-S_w-PD; "
    "operator-M_inf-open)+CHECKPOINT.  "
    "A-FIRST GO: leftover C of {psi_0..psi_8} into "
    "orthocomplement on n=96 has hi-frac [30,150] vs "
    "[8,30] = 0.991; C[0,8] F=2.74e-10 (epsilon edge); "
    "top-SV Q_A[0,150]/c_tail=4.49.  "
    "Finite S_w=B-C D^{-1} C^T PD: T=150 lmin=6.38e-3 "
    "(Higham mu>=2.59e-3) vs S_flat=5.18e-3; "
    "dmin(D)=0.152 < c_tail (T=150 undershoot); "
    "T=400 dmin=1.49, S_w=7.23e-3.  "
    "Operator M_inf on true L2 complement OPEN "
    "(same leftover species as r483/r484).  "
    "Last structurally new 0.3 idea; keystone frozen.  "
    "Smoke 15/15, full 21/21, SPEC_SHA 1d61f8c270a38c6a.  "
    "Companion rh/problem/weighted_schur.tex + "
    "verify_weighted_schur.py WEIGHTED_SCHUR VERIFIED -- "
    "REDUCED(A-GO; finite-S_w-PD; operator-M_inf-open)"
    "+CHECKPOINT.  "
    "NO L* claim, NO R-dagger claim, NO RH claim, "
    "NO anti-RH claim"
)

_R484_STATUS = (
    "classical Weil block completion at L=0.3 "
    "(round 484, PRIME.RDAGGER.BLOCK_COMPLETION.01; "
    "experiments-side, NO ledger row): "
    "VERDICT STUCK(20x-drop-falsified@n96; "
    "jets>=10-garbage@n128; QR-IBP-kills-S).  "
    "Garbage criterion: |u(L)| n vs 2n; psi_0..6 certified, "
    "psi_8 marginal, psi_10+ O(1) at n<=128 "
    "(lambda_10 at binary64 floor).  "
    "n=96 leftover after psi_10/18/20 = 1.38e-1 / 9.60e-2 / "
    "4.40e-2 (drop 10->18 is 1.43x, not 20x); factor ~183 "
    "vs budget 2.4e-4.  r483 leftover 2.76e-2 was n=48 "
    "undercount.  QR even-Legendre leftover O(0.08); "
    "sinc-IBP of QR kills S (lmin~-0.065).  Enlarge-B "
    "recovers kappa_high~0.29.  Not lambda_*(0.3)>=c.  "
    "Smoke 12/12, full 24/24, SPEC_SHA cd69a3e49978cf55.  "
    "Companion rh/problem/block_completion.tex + "
    "verify_block_completion.py BLOCK_COMPLETION VERIFIED -- "
    "STUCK(20x-drop-falsified@n96; jets>=10-garbage@n128; "
    "QR-IBP-kills-S).  "
    "NO L* claim, NO R-dagger claim, NO RH claim, "
    "NO anti-RH claim"
)

_R483_STATUS = (
    "classical Weil Filon enclosure of the two integral "
    "classes at L=0.3 "
    "(round 483, PRIME.RDAGGER.FILON_ENCLOSURE.01; "
    "experiments-side, NO ledger row): "
    "VERDICT REDUCED(finite-S-interval-PD; "
    "leftover-C-HS=2.74e-2-vs-budget-2.4e-4).  "
    "Filon [0,150] rem <=2.5e-5, midpoints hit r480/r481 "
    "to 1.7e-7.  Exp-sum Ci-to-inf KILL (lminS~-1.6).  "
    "4-term IBP tail keeps finite even S PD "
    "(Higham mu>=1.20e-3, would-be c_*=1.68e-4).  "
    "Leftover ||C||_F modes 12,14 = 2.76e-2 vs IBP-inflated "
    "budget 2.4e-4 (deficit factor ~115).  "
    "Not lambda_*(0.3)>=c.  Smoke 17/17, full 27/27, "
    "SPEC_SHA 54613b4a2a038342.  Companion "
    "rh/problem/filon_enclosure.tex + "
    "verify_filon_enclosure.py FILON_ENCLOSURE VERIFIED -- "
    "REDUCED(finite-S-interval-PD; leftover-C-HS=2.74e-2-vs-budget-2.4e-4).  "
    "NO L* claim, NO R-dagger claim, NO RH claim, "
    "NO anti-RH claim"
)

_R482_STATUS = (
    "classical Weil Carleson anatomy at the spectral edge "
    "(round 482, PRIME.RDAGGER.CARLESON_EDGEBAND.01; "
    "experiments-side, NO ledger row): "
    "VERDICT STUCK(SR_FAILS_FINITE_CENSUS;"
    "RESTRICTED_LARGE_SIEVE_IS_TARGET;"
    "STRICT_F_SCRAMBLE_PREMISE_FALSE).  "
    "Finite uniform envelope F_k(t)<=0.666528 t^1.25 "
    "for k=5..16, t<=1/2 (all exact jumps; not cofinal).  "
    "Pooled log-log F~0.019002 t^1.274663 (Delta-AIC=-23.70); "
    "individual exponent excess -0.631..+2.765.  "
    "Optimized SR 1.055..2.700 closes NONE of the twelve "
    "windows with q_k<1 already.  Christoffel overshoot "
    "105..7.64e7; local Plancherel 5.52e3..3.59e4.  "
    "Restricted large sieve is TARGET after MAIN-dependent "
    "orthogonalization.  Strict F scramble premise FALSE "
    "(reverses 2/12); danger mass scramble-sensitive 12/12.  "
    "Not a Carleson law, not lambda_*.  Smoke 15/15, full 29/29, "
    "SPEC_SHA c007a877653449ee.  Companion "
    "rh/problem/carleson_edgeband.tex + "
    "verify_carleson_edgeband.py VERIFIED carleson_edgeband "
    "-- STUCK(SR_FAILS_FINITE_CENSUS;"
    "RESTRICTED_LARGE_SIEVE_IS_TARGET;"
    "STRICT_F_SCRAMBLE_PREMISE_FALSE).  "
    "NO L* claim, NO R-dagger claim, NO RH claim, "
    "NO anti-RH claim"
)

_R366_STATUS = "The edge-gap lemma via Markov-Stieltjes mass counting -- the last sharp internal attempt after the r363 INTERNAL_LIMIT (round 366, PRIME.LSTAR.DUAL.EDGE_GAP_MS.01; experiments-side, NO ledger row): 30/30 sealed; SPEC_SHA 2b75c2668f0ca545 final with record, freeze 4164a1c1a1bd3aaf, two-commit protocol pre-freeze dbf340ab / record (this change); two disclosed calibration amendments a1/a2 (MS sandwich f64 floor on 15/85 mid/deep MAIN, max high-side 1.7e-7 at kz133, G33 retyped to graded maxdev; chi shallow sum-lambda bar 1e-12 -> 1e-11 after 2/42 + 1/42 chi rows at 7.4e-12 with sandwich 0/0; NO forcing candidate, SCALED_BAND, MINC_HALF or verdict letter moved).  MAIN VERDICT MS_CENSUS(M1-gap SATZ + M3-sandwich SATZ + M4-sum-lambda SATZ + M5-scaled REFUTED + M6-chr-endpoint REFUTED + M7-dictionary-force OPEN/NO + Z=1 CENSUS 84/85) + REST_NECESSARY_ONLY + STURM_CANONICAL_CENSUS(84/85 MAIN, chi MAY tip, scramble MUST tip) + COMPOSITION_TYPED + INTERNAL_EXHAUSTED.  LEG A: true Gauss zeros (vectorized bisection of p_n, 52 steps) give sum lambda = U to 3e-15 at w9 (mp dps-30 3e-15) and the classical MS sandwich Lambda_{j-1} <= M_left(z_j) <= Lambda_j as SATZ in exact arithmetic; discrete gap theorem SATZ; zero-count == degree 85/85 graded.  THE MASS-FORCING CANDIDATES ARE REFUTED: CAND_SCALED (n M_I/U in (0.5, 1.5)) 0/74 resolvable MAIN; CAND_GE1 (M_I > chr_pair) 0/74.  The pair-gap is DUAL-VOID (w9 M_I = 6.83e-5, U = 520.27, n M_I/U = 2.40e-5) -- proportional counting predicts Z = 0, measured Z = 1 lives in the O(1) MS buffer which cannot distinguish 0 from 1.  Dictionary: M_I IS the closed route-B weight at fold 3; comparing it to Christoffel numbers needs the OP kernel, NOT in the Digamma/tent/reciprocal dictionary.  EDGE-GAP remains OPEN as a theorem.  LEG B: min_diag(R_CC) > 1/2 on 74/74 resolvable (0 C-nodes below 1/2) -- NECESSARY, SATZ (lambda_min <= min diag); Gershgorin >= 0 on 0/74 -- NOT sufficient.  Fold-1 occupation is a UNION mu-atom, not a C-node.  Scramble minC 0.186 < 1/2 (23 C-nodes below) -- named occupation break.  REST_MASS_GO does not fire.  COMPOSITION (74 resolvable): Schur split SATZ 74/74; Cauchy rest>=eps SATZ 74/74; detS>0 and rest>0 CENSUS 74/74; r362 A5/A7 gated at w9.  The r363 hoped chain still has TWO gaps.  Worlds: chi3 30/42 and chi4 29/42 keep Sturm (MAY tip); CAND_SCALED 0/42+0/42; scramble straddle FAILS (n_mid 3, zeros_in_pair 2/2) AND rest -0.4962 AND minC 0.186.  Twin dose-zero bitwise, |dlog| 6.9e-4, |d M_I| 9.7e-10.  Must-fails 5/5 (m1 off-by-one MS 183 viol, m2 bar-by-sight AST, m3 occ-from-rest AST, m4 circular Christoffel AST, m5 wrong gap 0 vs 1).  Honest: both mass paths fail to close the two r363 theorem-loci -- INTERNAL_EXHAUSTED, the internal full attack (pinning then mass) is finished at measured grade; the external RHP path stays a documented option.  Deterministic, record run1/run2 byte-identical up to WALL (260.3/267.2 s).  NO L* claim, NO R-dagger claim, NO RH claim in either direction"

# (path, role, round, ledger_ids, status, pin) -- kept in exact
# sync with rh/INVENTORY.json: every rh-sync/promotion wave that
# touches the inventory MUST extend this list in the same change
# (a stale list here would silently DROP rows on regeneration).
ENTRIES = [
    # -- certified RH theorem modules (load-bearing suite) --
    (f"{VER}/v955_tau_iiks_toda_dictionary.py", "verification_module",
     "r224-r226",
     ["PRIME.PORT.TAU.FINITE.IIKS.01",
      "PRIME.PORT.TAU.NOPOLE.COFINAL.01",
      "PRIME.PORT.TAU.01"],
     "[E] finite IIKS/Toda dictionary; [O] no-pole cofinal", True),
    (f"{VER}/v956_signedmoment_halffilling_duality.py", "verification_module",
     "r228-r231",
     ["PRIME.FREEMOMENT.JFRACTION.01",
      "PRIME.JACOBI.DUAL.REVERSAL.01",
      "PRIME.FREEMOMENT.POSITIVEPREFIX.01"],
     "[E] half-filling/duality/L-gauge; [O] positive prefix", True),
    (f"{VER}/v958_bordered_tau_readout_dictionary.py", "verification_module",
     "r244-r253",
     ["PRIME.PORT.RHP.BORDERED.READOUT.01",
      "PRIME.PORT.RHP.FULLSOURCE.BASEFIBER.01"],
     "[E] bordered dictionary + error formulas + PSD base; [O] "
     "base/fiber campaign", True),
    (f"{VER}/v959_coupledtau_terminal_dictionary.py", "verification_module",
     "r256-r259",
     ["PRIME.PORT.RHP.COUPLEDTAU.TERMINAL.01",
      "PRIME.PORT.COUPLEDTAU.TERMINAL_CROSSRATIO.01",
      "PRIME.PORT.FULLSOURCE.PREFIX_RESUMMATION.01"],
     "[E] coupled-tau recursion + bilinear form + telescope; [O] "
     "the two last edges", True),
    (f"{VER}/v960_terminal_surface_closure.py", "verification_module",
     "r260-r275",
     ["PRIME.PORT.COUPLEDTAU.SURFACE_CLOSURE.01",
      "PRIME.PORT.COUPLEDTAU.TERMINAL_CROSSRATIO.01"],
     "[E] terminal-surface closure: 42/42 census certified (41 "
     "mechanism + kz15 exact-finite), two-branch theorem, phase "
     "bounds, universal pair theorem H1-H4 (H5 open); [O] cofinal "
     "front (lemma L2)", True),
    (f"{VER}/v961_midpoint_orientation_dictionary.py", "verification_module",
     "r274-r278",
     ["PRIME.PORT.RHP.MIDPOINT.ORIENTATION_DICTIONARY.01",
      "PRIME.PORT.RHP.MIDPOINT.ORIENTED_THEOREM.01",
      "PRIME.PORT.WALL.METRIC_FIREWALL.01"],
     "[E] midpoint-orientation dictionary (Casoratian = h_n, "
     "augmented telescope) + Maslov census GO (R2, atom-Sturm "
     "refuted) + metric-firewall measurements; [O] oriented "
     "midpoint theorem (rounds 279-281 executed and consumed in "
     "wave 5 via v962) + global metric firewall", True),
    (f"{VER}/v962_halffilling_pinning_theory.py", "verification_module",
     "r279-r281",
     ["PRIME.WALL.HALFFILLING_PINNING_THEORY.01",
      "PRIME.PORT.RHP.MIDPOINT.ORIENTED_THEOREM.01",
      "PRIME.PORT.REPRESENTATION.CONTEST.01",
      "PRIME.PORT.RHP.FULLSOURCE.QUASIDEFINITENESS.01"],
     "[E] the half-filling pinning theory: T1 moment counting "
     "(free pivots exactly h_0..h_{N_w-1}, why-half-filling "
     "answered by counting) + T2 crossing budget (#(h<0) = S_-, "
     "Jacobi/Sylvester, world-blind) + T3 two-sided parity "
     "(h-blind, census bilanz + 87376-case exhaustion) + T4 main "
     "window reduction (the entire open statement is minC >= N_w "
     "<=> forall n < N_w : h_n > 0) plus the four refutations "
     "NO_UNIVERSAL_O1_PINNING / NO_EXTREMALITY / "
     "NO_GENERIC_MASLOV_OBSTRUCTION / NO_SIMPLE_OFFSET_LAW; probes"
     " r279/r280/r281 embedded byte-exact (smoke stage); Lean: "
     "free_window_positivity = the fog-free central sorry, T1/T4 "
     "proved, T2 stated, upper_pinning_not_universal guard; [O] "
     "representation contest + full-source quasi-definiteness (in "
     "flight, not consumed)",
     True),
    (f"{VER}/v963_lstar_reduction_dictionary.py", "verification_module",
     "r282-r285",
     ["PRIME.LSTAR.REDUCTION_DICTIONARY.01",
      "PRIME.LSTAR.SUBORDINATION.01",
      "PRIME.PORT.REPRESENTATION.CONTEST.01",
      "PRIME.PORT.RHP.FULLSOURCE.QUASIDEFINITENESS.01"],
     "[E] the L* reduction dictionary: the r283 A2 chain (mu-frame "
     "congruence minor_k(D_mu - G) == D_k(mutilde) exact; frame "
     "contraction h > 0 through the window <=> lambda_max(E_m) < 1;"
     " crossing exactly at minC + 1; pigeonhole ceiling minC <= "
     "S_+; capacity-as-counting refuted by the rank-one pair) => "
     "L* IS THE CANONICAL REDUCTION (int p^2 dnu < int p^2 dmu for "
     "deg p < N_w, equivalently lambda_max(E_{N_w}) < 1); the r285 "
     "decomposition bookkeeping (lambda = maxdiag x (1 + assist) "
     "exact, budget equivalence sign-exact); the r282 four-language"
     " elimination as named negative gates (CONTEST_ALL_DEAD -- SOS"
     " iff empty negative register, Kasteleyn orientation iff S_- ="
     " 0, Hamiltonian-PSD == h > 0, dual-pair sync by theorem; the "
     "common reason: every classical language forces positivity "
     "exactly for the positive measure class); typed measurements: "
     "one-atom-vs-collective dichotomy, (D) separates, sub-"
     "classical p = 0.38, ensemble LOW_OUTLIER, the first two "
     "MAIN_SEPARATING detectors, the honest DCXX margin decay (min "
     "1.4175e-7 at z = 233; r286 in flight, NOT consumed); probes "
     "r282/283/284/285 embedded byte-exact (smoke stage); Lean: "
     "lstar_subordination = the wave-6 canonical sorry, "
     "lstar_implies_free_window PROVED; [O] the L* contract "
     "PRIME.LSTAR.SUBORDINATION.01 with the standalone document "
     "rh/problem/",
     True),
    (f"{VER}/v964_lstar_coherence_census.py", "verification_module",
     "r286-r289",
     ["PRIME.LSTAR.COHERENCE_CENSUS.01",
      "PRIME.PORT.L2.VDC_LEMMA.01",
      "PRIME.LSTAR.SUBORDINATION.01",
      "PRIME.PORT.COUPLEDTAU.TERMINAL_CROSSRATIO.01"],
     "[E] the L* coherence census: the r286 margin-scaling "
     "clarification (15 new anchors N_w 942-1218 ALL mp-sign-safe "
     "positive, min +1.806e-8 -- NO counterexample; O(1) census "
     "offset survives, max +4; flattening power law alpha ~ 3.05, "
     "driver c_w -> 1; HARMLESS quantified; q_N reconciled; "
     "EXTRAP_CALIBRATED 15/15), the r287 vdC theorem (the exact, "
     "constant-free, arithmetic-free van der Corput inequality at "
     "H = ceil(sqrt(m)) delivers delta' = +0.309 > 0.21 world-blind"
     " and certifies 6/7 + 38/42; F1 discrepancy dead; module-own "
     "exact proof route: Fejer window-sum identity + covering "
     "identity + Cauchy-Schwarz, wrong-prefactor must-fail), the "
     "r288 carrier map (antiphase next-nearest ARCH-ARCH pairs, "
     "z_v = -3.149, total control reversal, finest alignments below"
     " phase resolution; honest negatives SAMPLING_BLIND / "
     "SOURCE_SEPARATOR_NOT_FOUND / DIFFERENT_OBJECTS) and the r289 "
     "METRIC_ONLY adjudication (the rational twin keeps the full "
     "signature identical -- the diophantine route excluded; metric"
     " coherence threshold 1e-3..3e-3 gap; tent-split fractions the"
     " only sub-gap entry, completeness 4.2e-14; Baker ~7900x too "
     "weak AND unnecessary); probes r286/287/288/289 embedded "
     "byte-exact (smoke stage); Lean: no new statement -- the hole "
     "stays lstar_subordination; [O] PRIME.PORT.L2.VDC_LEMMA.01 "
     "(the chain origin of the P-variance scaling) + the L* "
     "contract at the wave-7 state (open front: the profile "
     "functional; r290 in flight, not consumed)",
     True),
    (f"{VER}/v965_lstar_curvature_arc.py", "verification_module",
     "r290-r295",
     ["PRIME.LSTAR.CURVATURE_ARC.01",
      "PRIME.LSTAR.CLOSED_FUNCTIONAL.01",
      "PRIME.LSTAR.SUBORDINATION.01"],
     "[E] the L* curvature arc: the r290 basin geometry (the working "
     "set is a soft-shouldered anisotropic TUBE in the exact theta_eq "
     "LAG coordinate -- killfrac 0.38/0.62/1.00 at 5e-4/1e-3/2e-3; "
     "world axes kill 5-50x earlier; the SMOOTH axis a privileged yet "
     "gradient-orthogonal killer; the r280 ridge REAL, minC 185 at "
     "factors 1..8), the r291 ridge anatomy (the lift is a FIRST-ORDER "
     "BUDGET phenomenon with one threshold in (1.280, 1.291] over all "
     "18 matched-dose cases, k_min 9, one TOP6@8 retraction; NO fixed "
     "point -- plateau 185; LIFT_MAIN_SPECIFIC; SMOOTH collective-"
     "quadratic ratio 23.7), the r292 curvature spectroscopy (all 29 "
     "diagonals negative, RANK-1 DENS valley 92.5 pct, lam_top -0.418;"
     " not SMOOTH, not the ridge; m* and the retraction invisible to "
     "jets; EPSTEIN second-order structureless), the r293 metric "
     "reconciliation (three metrics sealed first; F10 home margin "
     "+0.024, MIX_IS_CAUSE; all 8 flips SIMPLE h_184 zeros alpha = 1; "
     "MSTAR_NO_LAW; the TOP6 retraction a second simple zero at f_ret "
     "7.107) -- plus the module-own exact S0 (polarization identity, "
     "budget telescope, doubling law, sealed decision bars, pure "
     "Fractions with mutant must-fails); probes r290..r295 embedded "
     "byte-exact (smoke stage); Lean: no new statement -- the hole "
     "stays lstar_subordination; HONEST NEGATIVES load-bearing: "
     "ALL_FUNCTIONALS_BLIND over five class families, r294 "
     "F10_FRAGILE (win 5/5, part 2/5) and r295 F10_SP_MAJORITY "
     "(14/20) -- F10 UNPROMOTED per the sealed bars, R293_LUCK, "
     "L2_VIA_CONSERVATION near-tautological; [O] "
     "PRIME.LSTAR.CLOSED_FUNCTIONAL.01 (loss-corpus forensics, the "
     "rank-2 DENS core, why L2) + the L* contract at the wave-8 state "
     "(no round in flight at this cut)",
     True),
    (f"{VER}/v966_l2_reduction_chain.py", "verification_module",
     "r296-r300",
     ["PRIME.L2.REDUCTION_CHAIN.01",
      "PRIME.L2.NEFF_TARGET.01",
      "PRIME.PORT.L2.VDC_LEMMA.01",
      "PRIME.LSTAR.CLOSED_FUNCTIONAL.01",
      "PRIME.PORT.COUPLEDTAU.TERMINAL_CROSSRATIO.01"],
     "[E] the L2 reduction chain: the r296 DENS fork closed honestly "
     "(DENS_WORLD_BLIND -- the coupling number cos(e_top, grad "
     "lambda_max) = +0.394 below the sealed 0.40 bar, lam3 couples "
     "harder -0.574, every arithmetic candidate <= 0.38, the moment "
     "subspace construction-adjacent on both dead controls; the lane "
     "routed to L2 per the pre-adjudicated reviewer fork), the r297 "
     "target inequality (sigma <= sigma* = 2(sl_c2 - 0.21) - sl_pref "
     "= -0.516, measured -0.714, margin 0.198 -- provenance missing, "
     "not room; CHAIN_PROVENANCE_PARTIAL(B3), the chain exactly "
     "orthogonal on the WINDOW measure), the r298 exact sign-"
     "preserving transfer (S_F = B(omega,omega) + B(Delta,omega+beta) "
     "at 8.8e-16 on 47 worlds; TRANSFER_DOMINANT: the window main "
     "term EMPTY, S_F ~ B(PDelta,PDelta) -- the vdC input IS the "
     "Fejer energy of the difference measure), the r299 decay split "
     "(LOWPASS 0.93; FULL-SUPPORT overlap 42/42 -- Delta a pure "
     "c-value difference; ET/Abel dead +1.948; the live edge sl_D "
     "-0.571 <= sigma* margin 0.055 with falling ratio -0.168) and "
     "the r300 diagonal anatomy (sl_D = 2 sl_L1 - sl_neff EXACT; "
     "both magnitude routes closed honestly; RATIO_BOUNDED_"
     "STRUCTURAL: R_env falls -0.122) -- plus the module-own exact "
     "S0 (sigma*-composition, Fejer-block decomposition identity, "
     "participation identity with the machine-checked DIAG<->NEFF "
     "equivalence, kernel envelope with equality witnesses, the five "
     "sealed verdict bars as exact decision logic, pure Fractions "
     "with tipping mutants); probes r296..r300 embedded byte-exact "
     "(smoke stage); Lean: no new statement -- NEFF_TARGET is a "
     "measured ladder-slope aggregate, not an exact finite identity, "
     "and a universal ladder form would be refutable (the r273 "
     "guard pattern); the hole stays lstar_subordination; THE CHAIN: "
     "[NEFF_TARGET open] => DIAG => sigma <= sigma* => r297 target "
     "=> v964 vdC => delta' > 0.21 generic -- ONE inequality "
     "remains; [O] PRIME.L2.NEFF_TARGET.01 (slope(n_eff) >= +0.908, "
     "measured +0.963, margin 0.055; D_rank bridge sp -0.81 "
     "correlational; r301 in flight, not consumed)",
     True),
    (f"{VER}/v967_l2_cascade_closure.py", "verification_module",
     "r301-r304",
     ["PRIME.L2.CASCADE_CLOSURE.01",
      "PRIME.L2.NEFF_TARGET.01",
      "PRIME.L2.REDUCTION_CHAIN.01",
      "PRIME.PORT.L2.VDC_LEMMA.01",
      "PRIME.PORT.COUPLEDTAU.TERMINAL_CROSSRATIO.01"],
     "[E] the cascade closure and the documented lane stop: the "
     "wave-9 rest targets executed to their end -- r301 NEFF_SPLIT "
     "(n_eff = n_act/(1 + CV^2) EXACT with the perfect count link "
     "n_act == m on 42/42; the Renyi family at ONE exponent: echt "
     "anti-concentration; jackknife-stable margin; the rest "
     "relocated onto UNIF_TARGET) and r302 UNIF_DERIVED(B1 + A2), "
     "the FIRST DERIVED of the lane (PROFILE_STATIONARY with an "
     "exact 1/N transient onto 1.973; the coherence identity 1 + "
     "CV^2 = n_act chi/(surv^2 n_eff_atom) EXACT; chi = 0.63 "
     "destructive, falling; the rest relocated onto ATOM_TARGET) "
     "-- then the r303 REGRESS AUDIT: all four margins are ONE "
     "algebraic number S = sigma* - sl_D = +0.0547 (invariance <= "
     "9e-16; the 1/2-conjecture refuted) => REGRESS_CONFIRMED, the "
     "cascade r297 -> r302 RETYPED as an exact reduction DICTIONARY "
     "(coordinate finding, not six proof steps; the hard rule "
     "binds: a round counts only with NEW information); the first "
     "causal coordinate found (rho_1 ladder monotone on 1008 "
     "sealed builds, the flip KILLS the inequality at margin "
     "-0.044) but MIXING_INSUFFICIENT (chi-level miss 0.134); "
     "n_eff_atom a pure MARGINAL functional (1e-15 on all builds); "
     "and the r304 SHORT-RANGE LAW: the global lag profile is a "
     "STABLE, WORLD-SPECIFIC PERIOD-4 COMB, no k0 <= 8 -- "
     "LONGRANGE_STRUCTURE + LAW_LONGRANGE, the sealed reviewer "
     "stop case fires; the reviewer condition SPLITS (NC(16) = "
     "0.712 < 1 HOLDS, summability FAILS at 1.563); the "
     "chi-relevant structure IS short-range (chi = 1 + 2 sum "
     "T_k/Q exact, the r303 gap at k <= 3, lag-2-dominated); "
     "lag-8 matching hits the chi level (0.022) but breaks the "
     "slopes (0.028/0.027): THE MECHANISM IS TWO-SCALE -- plus "
     "the module-own exact S0 (margin-invariance algebra with the "
     "halved-need mutant breaking by exactly sl_L1 = 1/5, "
     "coherence identity in product form, chi-lag decomposition, "
     "zero-sum tautology with the truncated-NC content, period-4 "
     "comb certificate, -/-/+/+ sign-pattern certificate with the "
     "kz18/kz23 Fractions pins, the four sealed verdict bars as "
     "exact decision logic with tipping mutants, the lane-stop "
     "composition gate; pure Fractions, no probe imports); probes "
     "r301..r304 embedded byte-exact (smoke stage); Lean: no new "
     "statement -- the stop carries no new exact target form (the "
     "period-4 comb and the two-scale split are measured "
     "finite-window aggregates, not exact finite identities; a "
     "universal ladder form would be refutable, the r273 guard "
     "pattern); the hole stays lstar_subordination; THE DOCUMENTED "
     "STOP: the global-profile mixing route of the L2 lane is "
     "CLOSED -- L2 generic <=> anti-concentration of an explicit "
     "block field with long-range period-4 structure; return with "
     "new tools; what stands: the exact identity dictionary, the "
     "two-scale split, NC < 1, the sign pattern, the marginal "
     "invariance; [O] PRIME.L2.NEFF_TARGET.01 retyped to the "
     "documented stop state; no round in flight at this cut",
     True),
    (f"{VER}/v968_architecture_adjudication.py", "verification_module",
     "r305-r316",
     ["PRIME.LSTAR.ARCHITECTURE_ADJUDICATION.01",
      "PRIME.SOURCE.RANKONE.UPDATE.IDENTITY.01",
      "PRIME.SOURCE.TENSOR.MECHANISM.01",
      "PRIME.L2.RENYI3.PROVENANCE.01",
      "PRIME.LSTAR.SUBORDINATION.01",
      "PRIME.LSTAR.CLOSED_FUNCTIONAL.01"],
     "[E] the architecture adjudication: the architecture day "
     "r305-r316 frozen in the reviewer's binding FOUR-LEVEL STRUCTURE "
     "-- LEVEL 1 real formal theorems (Lean, already green, NO Lean "
     "change ships with this module: lstar_terminal_implies_master "
     "(r305: L* + terminal q_N < 1 => full master positivity; "
     "augmented_prefix_positive and free_window_positivity "
     "corollaries), the four closed Inertia theorems, the real "
     "PrimeWindow construction (r310), source exactness + mass "
     "conservation of any folding + the strong stabilization form "
     "(r310b), the r309 rank-one update identities, Hill monotonicity "
     "+ the Renyi-3 => N_2 bridge; sorry census 9 -> 5, the two TRUE "
     "holes stand alone: lstar_subordination + "
     "terminal_positive_main); LEVEL 2 certified finite statements "
     "(Renyi-3 on 57 rungs at C = 1.069 / A = 2; fixed-head census "
     "77/77; block-Green identity + strict cone with exact rational "
     "Farkas certificates; paired-cone soundness on 20714 steps; fold "
     "multiplicity exactly 2; 93 percent far-triple cancellation; the "
     "signed cubic identity with vanishing boundary, Fractions-exact; "
     "the 21 small-m certificates); LEVEL 3 negative architecture "
     "decisions (FIXED_HEAD_DEAD; PAIRED_CONE_NO_INDUCTION + "
     "WORLD_BLIND, B does not overtake A; the r308 discriminator = "
     "budget sign / chordal restatement; COEFFICIENT_SIGN_WALL -- Lane "
     "A closed as cone language with the mechanism named: block-psd "
     "membership without rank-one SDD, obstructed at the budget/border "
     "sign; FLOQUET_EXPANDING; TRIPLE_TYPE_MAJORANTS_WRONG; "
     "PHI3_ALL_BLIND; TWO_REGIME_DEAD with the anatomy: the "
     "obstruction family cuts across the FCIX stratum, first-5 "
     "load-bearing, kz55/kz67 near-one-block); LEVEL 4 open mechanisms "
     "(the constructive PSD-G rule as a question, the signed cubic "
     "flux theorem, the quantitative source functional, "
     "crossing_budget, the definitional source bridge, L*, the "
     "terminal) -- plus the module-own exact S0 (Hill/Lagrange chain "
     "with the bridge, the opening-flux lemma F_1 == 0 with the flux "
     "telescope, the collision counting identity with the exact "
     "factor-8 mutant break, an r311-class exact rational Farkas "
     "mini-certificate, the TEN sealed verdict bars as exact decision "
     "logic with tipping mutants, the four-level composition gate; "
     "pure Fractions, no probe imports); probes r306..r316 embedded "
     "byte-exact (smoke stage); THE CLAIM SPLIT (binding, NOT one "
     "TRANSFER title): PRIME.SOURCE.RANKONE.UPDATE.IDENTITY.01 [E] "
     "identities only, PRIME.SOURCE.TENSOR.MECHANISM.01 [O] the open "
     "mechanism; PRIME.L2.RENYI3.PROVENANCE.01 [O]: the GO stands, the "
     "provenance open (trilogy: identity exact, functional blind, "
     "two-regime dead; R317 fork at the reviewer); universality "
     "classes: base fine-metric (METRIC_ONLY, twin invariance), fiber "
     "recursive (EPSTEIN holds, SCRAMBLE breaks) -- shared algebra, "
     "not necessarily shared mechanism; reviewer maturity 4 -> 5 "
     "(formal architecture 9.5) typed as a REVIEWER ASSESSMENT; "
     "nothing is proved cofinally, L* stays THE open center; no round "
     "in flight at this cut (R317 waits on the reviewer fork)",
     True),
    (f"{VER}/v969_forks_and_redteam.py", "verification_module",
     "r317-r322",
     ["PRIME.REDTEAM.EXTRACTION_AUDIT.01",
      "PRIME.L2.RENYI3.SLIDING_BOUND.01",
      "PRIME.L2.RENYI3.PROVENANCE.01",
      "PRIME.LSTAR.SUBORDINATION.01"],
     "[E]/[O] the red-team morning and the two forks: the r319 "
     "extraction-chain audit (three kernel-checked type "
     "inconsistencies three levels above the boxes -- U1 bridge x "
     "terminal via B = -1, U2 bridge x L* via the mesh-level-0 "
     "total node collision and p = X - 1, U3 pair_margin_main "
     "forces its source predicate empty -- plus the mesh-vs-anchor "
     "cofinality seam; the honest chain verdict: two lemmata => "
     "window-local master positivity ONLY) and the r320 repair "
     "(bridge retype with u/B fidelity + separation discipline + "
     "budget_pos; SourceExact for the arch/border finding; "
     "pair_margin_main retyped onto the canonical extraction with "
     "signRuns_sum + canonical_split PROVED; three permanent "
     "sorry-free guards; sorry-free witness at anchor 2, atoms "
     "{2,3,4}, mesh level 4 via 2^7 < 3^5 < 2^8; census 5 -> 5 "
     "with two typed retypes) frozen as "
     "PRIME.REDTEAM.EXTRACTION_AUDIT.01 [E]; the fiber fork frozen "
     "as PRIME.L2.RENYI3.SLIDING_BOUND.01 [O] (the r321 theorem "
     "candidate sum q^3 <= 1.3056 F_A^2 (log m)^2/m^2 for m >= 73 "
     "with all four named violators inside at reserves 7.0..9.6; "
     "honest: C_impl 7.97 = 7.5x looser than r306, form not "
     "sharpness; the provenance question split in two: F_A "
     "bounded? / qmax-share?; the r317 WHAC_A_MOLE abort "
     "documented) and the base fork closed honestly (r318 "
     "P2_MAIN_SPECIFIC with P1 banked as language; r322 "
     "ALGORITHM_ARTIFACT: the antiphase sign law and the 97.6/2.4 "
     "anatomy are least-norm-proximal Dykstra-basin properties, "
     "the selection-geometry question the named residual); the "
     "module-own exact S0 (concentration bracket, the U1-U3 "
     "witnesses in exact arithmetic, the r320 separation/"
     "canonical-split certificates, six sealed verdict bars with "
     "tipping mutants, the wave-12 composition gate; NO Lean "
     "call); probes r317/r318/r321/r322 embedded byte-exact "
     "(smoke stage; r321 imports the embedded r317, r322 the "
     "embedded r318); the Lean rounds r319/r320 consumed as "
     "REPORTS (artifacts in rh/lean/, re-verified by lake build + "
     "run_rh.py); reviewer adjudication addendum: the two true "
     "holes named WINDOW-LOCAL (Level B of the three-level proof "
     "graph A/B/C), the false cofinality direction documented NOT "
     "solved, SourceExact -> CanonicalPrimeWindow + "
     "sourceExact_buildPrimeWindow the named open Lean target; "
     "rounds R324 (terminal QMAX x M_2) and R325 (extraction "
     "repair) in flight, deliberately NOT consumed at this cut",
     True),
    (f"{VER}/v970_extraction_and_composition.py", "verification_module",
     "r323-r327",
     ["PRIME.EXTRACTION.ELEMENTWISE.01",
      "PRIME.L2.RENYI3.MEASURED_COMPOSITION.01",
      "PRIME.L2.RENYI3.SLIDING_BOUND.01",
      "PRIME.L2.RENYI3.PROVENANCE.01"],
     "[E]/[O] the extraction repair and the terminal composition: "
     "the r325 extraction-repair fork (ELEMENTWISE_STABILIZATION_GO "
     "-- the repair statement is a QUANTIFIER statement, not a mesh "
     "theory: on the native v749 class all three channels stabilize "
     "exactly at the predicted finite anchor onset alpha* = "
     "(n_g + 1) D_0/2 and are constant under dyadic mesh "
     "refinement; no mesh-cofinal ladder, no transport, H_cof is "
     "not needed and is replaced as the target route; B = "
     "construction substrate, C = quantified density step, the "
     "anchor-only floor real) and the r326 Lean implementation "
     "(rh/lean/RH/Elementwise.lean, consumed as a REPORT: "
     "sourceExact_buildPrimeWindow PROVED, the comb stabilization "
     "elementwise PROVED, weil_nonneg_of_windowlocal PROVED -- "
     "extraction without the ladder; sorry census 5 -> 8 with three "
     "typed Level-C statements, the wave-12 census reservation "
     "partially discharged) frozen as "
     "PRIME.EXTRACTION.ELEMENTWISE.01 [E] with the honest "
     "new-connection formulation verbatim (two window-local lemmata "
     "over the canonical family + the elementwise architecture + "
     "cited classics => RH; open links: arch/pole transcription, "
     "compression bridge, source completion); the terminal lane "
     "frozen as PRIME.L2.RENYI3.MEASURED_COMPOSITION.01 [O] (r324 "
     "PILEUP_GROWS_SUBCRITICAL +0.172 < 0.224 after the reviewer "
     "course correction with the r324-pre pre-work banked: F_A "
     "de-black-boxed via the exact identity F_A x B x log m == m x "
     "q_max, the O(log m) scale count certified C_NSC 2.0258 0/39, "
     "the per-scale mass refuted -- the near-critical windows are "
     "ONE heavy source scale; the composition typed MEASURED: sum "
     "q^3 <= 8.941 (log m) m^{+0.172}/m^2 => N_2 >= m^0.888 for m "
     ">= m_0* = 10^59.6, the gap (274, 10^59.6) the disclosed "
     "extrapolation hypothesis; r328B independent chain audit "
     "carried as a chain annotation, the record sealed: the bar "
     "0.224 used the ATOM-level need 0.888, the block-level need "
     "is 908/1002 = 0.9062 -- chain-honest bar 0.188, the verdict "
     "survives 0.172 < 0.188, m_0* chain-honest 10^238, exact "
     "gate S0-T5d; r327 CAP_PARTIAL with SOURCE "
     "anatomy: the heaviest group of the argmax block is EXACTLY "
     "ONE beta/omega fold pair on all 65 rungs, kz53 = one "
     "bulk/window coincidence at 88.8 pct; the Lambda-pair cap "
     "refuted, the group count certified C_NG 2.6351 0/39 -- the "
     "third O(log m) count; direction: the coincidence geometry); "
     "the module-own exact S0 (interpolation with slack exactly "
     "1/36, the F_A identity, the r327 group ledger, the r325 "
     "onset formula as an exact toy stabilization, the m_0* "
     "log-space solver rebuilt verbatim with the disclosed "
     "linear-space bug caught, the r328B chain-audit gate S0-T5d, "
     "six sealed verdict bars with "
     "tipping mutants, the wave-13 composition gate; NO Lean "
     "call); probes r324-pre/r324/r325/r327 embedded byte-exact "
     "(smoke stage; r324 imports the embedded r324-pre, r327 the "
     "embedded r324-pre and r324); the r323 abort consumed as a "
     "NOTE (clean, before any write access, nothing counts as a "
     "round) and the r326 Lean round as a REPORT (artifacts in "
     "rh/lean/, re-verified by lake build + run_rh.py); the "
     "window-local positivity premise proved nowhere; the two true "
     "window-local Lean holes unchanged; L* stays paused; the "
     "r328A/B/C adversarial audits read-only, reports with the "
     "coordinator; no measurement round in flight at this cut",
     True),
    (f"{VER}/v978_terminal_density_martingale.py", "verification_module",
     "r339+r341 (wave 14)",
     ["PRIME.TERMINAL.DENSITY_MARTINGALE.01",
      "PRIME.L2.RENYI3.MEASURED_COMPOSITION.01"],
     "[E] the terminal density-martingale layer, re-derived from "
     "scratch (sympy symbolic + pure Fractions, no probe imports): "
     "the density per remaining descendant is a martingale from mass "
     "conservation alone; the moment dictionary E[X^2] == m M_2, "
     "E[X^3] == m^2 M_3, max X == m q_max (the terminal target IS a "
     "martingale moment; the banked r306 C_2 = 1.0694 certifies the "
     "A = 2 polylog form on the 57-rung set); the tilted tower "
     "E[X^3] == E_Q[prod Gamma] with steps p~ = p R^3/Gamma (the "
     "untilted reading breaks by an exact Fraction); the Phi-Gamma "
     "telescope; the exact hand-off E3h <= (m q_max)^2 msh; the "
     "algebraic pair ceiling Gamma <= 4 via 4R - R^3 = R(2-R)(2+R); "
     "the sealed r339/r341 verdicts re-run as exact decision logic "
     "on the frozen record aggregates with tipping mutants "
     "(LOCAL_INFLATION_SUPERCRITICAL: the target grows 8x slower "
     "than the worst-case budget; PATHWEIGHT_ALSO_SUPERCRITICAL "
     "letter-honest: 21x deflation, R* = 3/2 a tuning surface); "
     "no inequality promoted -- the r324 MEASURED composition "
     "stays the terminal end state; NO RH claim", True),
    (f"{VER}/v979_cover_growth_k2.py", "verification_module",
     "r344/r346/r351/r353/r355 (wave 14)",
     ["PRIME.L2.COVER_GROWTH_K2.01",
      "PRIME.L2.RENYI3.SLIDING_BOUND.01"],
     "[E] the three-arm cover, the growth law and the K2 two-family "
     "law, Frame-A-typed: the FAB identity F_A B == m q_max/log m "
     "exact; the data-free K1 formula R_ALG = 4^(1/3) -> grid 8/5 "
     "interior via exact cube midpoint comparisons; the r355 mesh "
     "identity h - NU u in (0, 3/2] exact; the sealed r344/r346/"
     "r351/r353/r355 verdicts re-run on the frozen aggregates with "
     "tipping mutants (the first certifying three-arm cover 0/51 at "
     "m_0* 10^22.6; the P02 predictor 51/51; the growth ceiling "
     "C_FAB = 14.93 with the fresh tranche 0/6 and polylog m_0* "
     "10^18.9; THE BINDING r353 FRAME-A RESTRICTION: frame B breaks "
     "the ceiling +21 pct and kills the reserve floor at m ~ 760 -- "
     "the sliding coverage is FINITE; K2 <= 11.87 the sole "
     "cross-family survivor, NU-free over three aspects, source "
     "chain exactly closed with vacuous caps); the honest m_0* "
     "ledger all Frame-A census; NO cofinal claim, NO RH claim",
     True),
    (f"{VER}/v980_lstar_margin_chain.py", "verification_module",
     "r345/r347/r348/r350/r352/r354 (wave 14)",
     ["PRIME.LSTAR.MARGIN_CHAIN.01",
      "PRIME.LSTAR.SUBORDINATION.01"],
     "[E] the closed L* margin-law chain: the one-line identity "
     "m2'(p'+q'-m2') == p'q'-c'^2 (Vieta, symbolic); the two-level "
     "dressed-scalar theorem (121/250, 79/250, 72/250 by hand; "
     "cross-tie r'_2 = 4375/9559 == the r345 formula; Lagrange "
     "identity symbolic); the pinning theorem (orthonormal top-2 "
     "geometry => the dressed charpoly factors as (t-m)(t-m g21): "
     "m2' == margin identically, both sealed models); the "
     "rate-equality theorem in exact ratio form; the rho_K "
     "identities (toy 1/8, 23/24); the sealed r345/r347/r348/r350/"
     "r352/r354 verdicts re-run on the frozen aggregates with "
     "tipping mutants (GAP_RATIO_PRIMARY_CERTIFIED with the r343 "
     "soft decay re-adjudicated as a protocol artifact; ALPHA_CLOSED "
     "alpha = a_c + delta residual 0.033; RATE_EQUALITY_THEOREM "
     "live; ALPHA_SOURCE_CLOSED at candidate grade; RHOR_REDUCED "
     "one object at 500x; PHI_DICTIONARY_GO computability; "
     "DELTA0_UNRESOLVED pool exhausted 10^3.90); the lane FROZEN as "
     "a specialist problem at rh/problem/lstar_problem.tex; "
     "SUBORDINATION stays [O]; NO L* claim, NO RH claim", True),
    (f"{VER}/v981_lstar_borodin_duality.py", "verification_module",
     "r356 (wave 14)",
     ["PRIME.LSTAR.DUAL_HOLE.01",
      "PRIME.LSTAR.SUBORDINATION.01"],
     "[E] the Borodin particle-hole duality: the complementation "
     "Pi_N^u + G Pi_{N-1}^{u_vee} G^{-1} == I bit-exact at half "
     "filling S = 2N-1 with the reciprocal dual weight u_vee = "
     "1/(u P'^2) and a RATIONAL conjugator (no square roots; the "
     "dropped-P'^2 and rank-N mutants break exactly); the "
     "L-ensemble roundtrip; the spectral map charpoly(E) == "
     "charpoly(R^{-1} - I) symbolic => L* <=> R > (1/2) I and "
     "margin == 2 - 1/lam_min(R) (both directions realized); the "
     "pair identities p/q == 2 - (R^{-1})_kk; the half-filling "
     "lemma (the r228 law IS Borodin's rank condition); the "
     "cosine-lattice closed forms => u_vee PROPTO c_j(1-x_j)/|f|: "
     "the r354 anti-correlation of the two phi blocks is DUALITY "
     "ALGEBRA BY DESIGN; the sealed r356 verdict re-run on the "
     "frozen aggregates (support 85/85 bitwise, honest verdict "
     "DUALITY_REPARAM_ONLY -- the lane goes final to the memo; "
     "RESERVE_LOCALIZED and AC_CLASS_EXCLUDED banked census-side); "
     "SUBORDINATION stays [O]; NO L* claim, NO RH claim", True),
    (f"{VER}/v982_dirichlet_matched_frame.py", "verification_module",
     "r357 (wave 14)",
     ["PRIME.WORLD.DIRICHLET_MATCHED_FRAME.01",
      "PRIME.L2.COVER_GROWTH_K2.01"],
     "[E] the matched Dirichlet frame and the second arithmetic: "
     "the GRH-faithful chi-arch side DERIVED symbolically from "
     "Lambda(s, chi) -- F_A^chi(xi) == -log(pi/q) + Re psi((1+2a)/4 "
     "+ i xi/2) for a = 0/1 (parity and conductor from the "
     "functional equation alone); the trivial reduction a = 0, "
     "q = 1 IS the zeta dictionary; the conductor shift == log 3 "
     "exact; the parity kernel e^{-w/2} -> e^{-(3/2)w} at 30 "
     "digits; the sealed r357 verdict re-run on the frozen "
     "126-window aggregates with tipping mutants "
     "(SECOND_ARITHMETIC_LIVES: the r330 death was a frame "
     "artifact, the wall holds on n = 3 arithmetics; the verbatim "
     "r330 battery retypes all four splits; mechanisms transfer "
     "while the zeta-graded signatures do not; K2 0/126 -- the "
     "third independent test; the matched scramble breaks: the "
     "wall needs the arithmetic); kein Satz, NO RH claim, NO GRH "
     "claim", True),
    # -- read-only deployed core consumed by every probe --
    (f"{VER}/v563_paper2_readouts.py", "readonly_core",
     "phase2",
     ["PRIME.PAPER2.READOUT.01"],
     "[E] deployed builder core", True),
    (f"{VER}/v881_carleson_port_geometry.py", "verification_module",
     "port lane",
     ["PRIME.PORT.SCHUR.01",
      "PRIME.PORT.INTEGRABLE.01",
      "PRIME.PORT.LIMIT.01"],
     "[E]/[O] port geometry (upstream of the tau lane)", True),
    (f"{VER}/v894_diagonal_refinement.py", "verification_module",
     "r26 contract",
     ["PRIME.CASE.PAIRCORR.CONTRACT.01"],
     "[O] the PAIRCORR wall contract (the measured wall)", True),
    # -- the sealed campaign probes (experiments side, frozen) --
    (f"{EXP}/centered_basefiber_probe.py", "sealed_probe",
     "r250",
     ["PRIME.PORT.RHP.CENTERED_BASEFIBER.01"],
     "measurement: OUTER_MODEL_FAILS + FIBER_BEYOND_MODEL", True),
    (f"{EXP}/corner_provenance_probe.py", "sealed_probe",
     "r251a",
     ["PRIME.PORT.CORNER.PROVENANCE.01"],
     "adjudication: CORNER_INTERFACE_ONLY(FALL3)", True),
    (f"{EXP}/targetreadout_error_probe.py", "sealed_probe",
     "r251",
     ["PRIME.PORT.RHP.TARGETREADOUT.ERROR.01"],
     "consumed by v958: READOUT_FORMULAS_EXACT", True),
    (f"{EXP}/base_gauge_constant_probe.py", "sealed_probe",
     "r252",
     ["PRIME.PORT.RHP.BASE.GAUGE_CONSTANT.01"],
     "consumed by v958: NO_GLOBAL_GAUGE + CONTOUR_R1_EXACT", True),
    (f"{EXP}/schlesinger_pairing_probe.py", "sealed_probe",
     "r253",
     ["PRIME.PORT.RHP.FIBER.SCHLESINGER_PAIRING.01"],
     "consumed by v958: TAU_RATIO_EXACT + POLE_REMOVAL_EXACT", True),
    (f"{EXP}/offdiag_gram_probe.py", "sealed_probe",
     "r254",
     ["PRIME.PORT.RHP.FIBER.OFFDIAG_GRAM.01"],
     "measurement: OFFDIAG_EXTENSIVE_CONFIRMED", True),
    (f"{EXP}/nodebands_base_probe.py", "sealed_probe",
     "r255",
     ["PRIME.PORT.RHP.BASE.NODEBANDS.01"],
     "measurement: DRIFT_NOT_BAND_LOCALIZED", True),
    (f"{EXP}/baseborder_factorial_probe.py", "sealed_probe",
     "r256",
     ["PRIME.PORT.FIBER.BASEBORDER.FACTORIAL.01"],
     "consumed by v959: EFFECTS_MIXED_COUPLEDTAU + firewall", True),
    (f"{EXP}/coupledtau_probe.py", "sealed_probe",
     "r257",
     ["PRIME.PORT.RHP.FULLSOURCE.COUPLEDTAU.01"],
     "consumed by v959: COUPLED_RECURSION_EXACT", True),
    (f"{EXP}/budget_anatomy_probe.py", "sealed_probe",
     "r258",
     ["PRIME.PORT.RHP.BUDGET.ANATOMY.01"],
     "consumed by v959: TELESCOPE_EXACT + TERMINAL_Q_LAW", True),
    (f"{EXP}/parametrix_pass_probe.py", "sealed_probe",
     "r259",
     ["PRIME.PORT.RHP.PARAMETRIX.PASS.01"],
     "consumed by v959: PARAMETRIX_FAILED (three honest negatives)", True),
    (f"{EXP}/terminal_crossratio_probe.py", "sealed_probe",
     "r260",
     ["PRIME.PORT.COUPLEDTAU.TERMINAL_CROSSRATIO.01"],
     "measurement: TERMINAL_CROSSRATIO_MEASURED(42/42), no GO; "
     "consumed by v960 (wave 4, embedded byte-exact, smoke stage)", True),
    (f"{EXP}/prefix_resummation_probe.py", "sealed_probe",
     "r261",
     ["PRIME.PORT.FULLSOURCE.PREFIX_RESUMMATION.01"],
     "adjudication: three exact representations, three no-gos", True),
    (f"{EXP}/terminal_triangle_probe.py", "sealed_probe",
     "r262",
     ["PRIME.PORT.COUPLEDTAU.TERMINAL_TRIANGLE.01"],
     "measurement: TRIANGLE_PARTIAL_IMPROVED(38/42); consumed by "
     "v960 (wave 4, embedded byte-exact, smoke stage)", True),
    (f"{EXP}/cancellation_adjudication_probe.py", "sealed_probe",
     "r263",
     ["PRIME.PORT.COUPLEDTAU.CANCELLATION_ADJUDICATION.01"],
     "adjudication: TWO_BRANCH_DECOMPOSITION_EXACT + RHP "
     "reduction; consumed by v960 (wave 4, embedded byte-exact, "
     "smoke stage)", True),
    (f"{EXP}/quenched_opening_probe.py", "sealed_probe",
     "r264",
     ["PRIME.PORT.RHP.QUENCHED.OPENING.01"],
     "campaign charter frozen (SHA 7b9e751d) + RHP dictionary", True),
    (f"{EXP}/s_monotonicity_probe.py", "sealed_probe",
     "r265",
     ["PRIME.PORT.RHP.QUENCHED.S_MONOTONICITY.01"],
     "adjudication: DEFINITENESS_WALL_EQUIVALENT", True),
    (f"{EXP}/border_resolvent_identity_probe.py", "sealed_probe",
     "r266",
     ["PRIME.PORT.RHP.QUENCHED.BORDER_RESOLVENT_IDENTITY.01"],
     "exploration: border-dressed resolvent identity search", True),
    (f"{EXP}/ranktrace_adjudication_probe.py", "sealed_probe",
     "r267",
     ["PRIME.PORT.EXTERNAL.RANKTRACE_CEILING.ADJUDICATION.01"],
     "external adjudication: arXiv:2608.13637 CEILING_IS_OUR_WALL", True),
    (f"{EXP}/drive_local_asymptotics_probe.py", "sealed_probe",
     "r268",
     ["PRIME.PORT.RHP.QUENCHED.DRIVE_LOCAL_ASYMPTOTICS.01"],
     "measurement: DRIVE_LOCAL_PARTIAL(b3F0.20, cert 1/7: kz22); "
     "consumed by v960 (wave 4, embedded byte-exact, smoke stage)", True),
    (f"{EXP}/phase_bulk_bound_probe.py", "sealed_probe",
     "r269",
     ["PRIME.PORT.RHP.QUENCHED.PHASE_BULK_BOUND.01"],
     "measurement: PHASE_BOUND_PARTIAL(c3F0.30, cert 6/7; kz15 "
     "rest 0.12 dec); consumed by v960 (wave 4, embedded "
     "byte-exact, smoke stage)", True),
    (f"{EXP}/kz15_boss_probe.py", "sealed_probe",
     "r270",
     ["PRIME.PORT.RHP.QUENCHED.KZ15_BOSS.01"],
     "adjudication: KZ15_EXACT_ONLY (b3 interval certificate "
     "closes kz15 margin +0.0268 width 1.5e-92 dps 640; b1 level-2"
     " cert 5/7, kz15 miss 0.06 dec; SPLIT_RULE_FAILED) -- surface"
     " 41/42 mechanism + kz15 exact-finite; consumed by v960 (wave"
     " 4, embedded byte-exact, smoke stage)", True),
    (f"{EXP}/universal_pair_theorem_probe.py", "sealed_probe",
     "r271",
     ["PRIME.PORT.COUPLEDTAU.UNIVERSAL_PAIR_THEOREM.01"],
     "theorem form + measurement: UNIVERSAL_STILL_PARTIAL(c2PAIR "
     "5/7; b2LEVEL2 leaves kz39 0.002 / kz15 0.06 dec) + Lean "
     "rh/lean/RH/PairBound.lean; consumed by v960 (wave 4, "
     "embedded byte-exact, smoke stage)", True),
    (f"{EXP}/l2_scaling_anatomy_probe.py", "sealed_probe",
     "r272",
     ["PRIME.PORT.COUPLEDTAU.L2_SCALING_ANATOMY.01"],
     "pure anatomy: TREND_CARRIER(A_pairs, alpha +1.01 beta -0.81 "
     "gamma -0.01) + BOUND_COARSENESS_CONFIRMED (truth rest falls,"
     " margin_true rises; H5 not contradicted) + SLACK_RANKING(c3 "
     "beyond-blind-level-2) + FLIP_CONDITION(delta 0.21 of "
     "available gamma_true 0.45, TRUTH_ALLOWS); consumed by v960 "
     "(wave 4, embedded byte-exact, smoke stage)", True),
    (f"{EXP}/euler_mechanism_probe.py", "sealed_probe",
     "r273",
     ["PRIME.PORT.COUPLEDTAU.EULER_MECHANISM.01"],
     "mechanism round (Euler perturbation ladder, 4 surgeries x 3 "
     "thetas x 3 reps x 42 rungs): PERTURBATION_INSENSITIVE (no "
     "stage collapses gamma_true; ~0.45 is near the generic sqrt "
     "baseline) + FIREWALL_MAP(pp = 0.00 -- every surgery kills "
     "free-prefix positivity at degrees 33-101: the wall, not the "
     "cancellation rate, is the arithmetic fingerprint); consumed "
     "by v960 (wave 4, embedded byte-exact, smoke stage)", True),
    (f"{EXP}/wronskian_dictionary_probe.py", "sealed_probe",
     "r274",
     ["PRIME.PORT.RHP.MIDPOINT.WRONSKIAN_DICTIONARY.01"],
     "exact dictionary D_n <-> Wronskian (32/32): "
     "WRONSKIAN_DICTIONARY_GO (base Casoratian == h_n with c' = 1;"
     " h-free midpoint form == node polynomial L -- the r231 "
     "sign-blindness as an identity; augmented border-paired "
     "Casoratian == h_n S_n, so D_{n+1} = B - W^aug/W^base; h-free"
     " normalization c = 1 through the dual second kind, exact on "
     "toys and at mp on the real comb incl. kz15/kz52 wards) + "
     "ORIENTATION_PREVIEW (Pruefer band 0 < dTheta < pi == h_n > 0"
     " exact; MAIN in-band through the free window; control exits "
     "25/21/27 degree-exact; w9 winding 262/366 measured, first "
     "exit at 184 = N_w) -- the Maslov round is freed; consumed by"
     " v961 (wave 4, embedded byte-exact, smoke stage)", True),
    (f"{EXP}/kyp_memory_probe.py", "sealed_probe",
     "r275",
     ["PRIME.PORT.COUPLEDTAU.KYP_MEMORY.01"],
     "two-sided no-go: KYP_INFEASIBLE(uniform classes -- exact o1 "
     "fiber forcing + o2 descent on 46/46 worlds) + "
     "KYP_IS_TARGET_INVERSE(Riccati memory forced to carry the "
     "exact signed tail sums, budget = Z^2 + sum b^2, fingerprint "
     "sp +1.00; certifies SCRAMBLE -- friendliness signature) + "
     "CURRENCY_READING(QM-AM overhead med +0.15 dec, generic "
     "census 8/42) -- the l^1 -> l^2 currency reform does NOT "
     "carry in state-space/KYP form; consumed by v960 (wave 4, "
     "embedded byte-exact, smoke stage)", True),
    (f"{EXP}/minimal_firewall_probe.py", "sealed_probe",
     "r276",
     ["PRIME.PORT.WALL.MINIMAL_FIREWALL.01"],
     "dose-response round (wall survival depth s = nf/N_w vs "
     "surgery dose; 5 surgeries -- neighbor swap / support jitter "
     "/ family decoupling / grid sign permutation / grid magnitude"
     " permutation -- x SINGLE + theta 0.02..0.25 x windows "
     "w9/kz18/kz55 = 360 worlds, exact h-chain flips "
     "mp-counter-checked at dps 40 incl. the v956 boundary flip AT"
     " N_w = 184): FIREWALL_LAW (P1/P2/B1/B2 GRADED + P3 "
     "INTERMEDIATE; shallow saturating deficit laws D ~ theta^b, b"
     " +0.04..+1.09 -- NOT all-or-nothing) + PROPERTY_RANKING "
     "(support exactness most wall-critical: P2_JIT tol 0.343 < "
     "B2_MAG 0.389 < B1_SIGN 0.536 < P1_SWAP 0.621 < P3_FAM 0.700;"
     " jitter at 2 percent of the local atom gap already costs 3/4"
     " of the depth) + CONTINUUM_VS_JUMP(CONTINUUM, 48/90 MIDDLE "
     "stages: single ops survive at median 0.88-1.00, the v956 "
     "control level 0.11-0.15 is reached only inside the graduated"
     " ladder) + V956_PLACEMENT(min 0.109 at B2_MAG@0.15, "
     "CONTROL_TOUCHED) + N_TRANSPORT(MAP_TRANSPORTS, sp "
     "+0.84/+0.86); consumed by v961 (wave 4, embedded byte-exact,"
     " smoke stage)", True),
    (f"{EXP}/maslov_census_probe.py", "sealed_probe",
     "r277",
     ["PRIME.PORT.RHP.MIDPOINT.MASLOV_CENSUS.01"],
     "blind Pruefer/Maslov census (29/29): MASLOV_CENSUS_GO (rule "
     "R2 = interlacing/reality of the Jacobi zeros, selected by "
     "the sealed training cascade on w9 + 4 smallest-N rungs + "
     "scramble(seed 2) variants; blind 37/37 rungs + w12/w13/w26 "
     "SAFE full depth, controls fire 26/22/28 = flips 25/21/27 + 1"
     " within the sealed +-1; r259 energy-branch separation "
     "17/6/9; NOT h-equivalent -- 79 pattern mismatches vs the 78 "
     "h re-entry pivots) + CENTRAL FINDING: the RAW atom-counted "
     "Sturm census is NOT the winding quantity -- on MAIN it "
     "breaks at n = 56/48 with h positive (zeros escape the atom "
     "hull, then pair inside single gaps: signed Sturm separation "
     "genuinely fails), while the interlacing/reality structure "
     "breaks at exactly nf + 1 everywhere (w9 continuation fire "
     "185 = N_w + 1); STURM_CHAIN_VERIFIED honestly not awarded "
     "(c1 refuted); Sturm rotation #eig < x* == n - #signchanges "
     "exact; kz15 + kz52 mp census wards; the oriented midpoint "
     "theorem is the named next round; consumed by v961 (wave 4, "
     "embedded byte-exact, smoke stage)", True),
    (f"{EXP}/metric_stability_probe.py", "sealed_probe",
     "r278",
     ["PRIME.PORT.WALL.METRIC_STABILITY.01"],
     "metric stability round (from the r276 dose-response "
     "continuum to the local law; exact Hellmann-Feynman gradients"
     " d log h_n/du_j = <wdot_j, pihat_n^2>/h_n and border/CD "
     "gradients dF_n/du_j = -<wdot_j, pihat_n B_n> through the "
     "sealed tent-grid channel, FD/Richardson/mp-gated to 1e-7; "
     "on-node geometry disclosed: the 2-power family sits EXACTLY "
     "on tent nodes (w9 alpha = log 16), one-sided derivative "
     "pairs side-selected): METRIC_STABILITY_LAW(TAME curvature, "
     "validity window theta* med 8.0e-4 [w9] / 1.2e-4 [kz55] -- "
     "25x..170x BELOW the smallest r276 dose 0.02) + "
     "GRADIENT_EXPLAINS_DOSE(PARTIAL, ratio 0.41, flip dev 3.00 --"
     " the 0.02 collapse is already a nonlinear cascade) + "
     "U_PROFILE(PREDICTIVE, sp(A, lethality) -0.82; BOTTOM-loaded:"
     " small primes 2/3/5 carry the gap-weighted sensitivity, hull"
     " correlation -0.80..-0.83, margin map tracks at +0.83) + "
     "N_TREND(SHRINKING, b_L -1.09, decade 17.3 -- no fragility "
     "growth, NO uniform constant) + "
     "MAINWINDOW_PREDICATE(PERTURBATIVE_ONLY: MetricNear(c, MAIN, "
     "theta) <= theta*(w) inherits margin >= margin_MAIN - L_D(w) "
     "theta per window; MAIN positivity stays the open center); "
     "consumed by v961 (wave 4, embedded byte-exact, smoke stage)", True),
    (f"{EXP}/oriented_theorem_probe.py", "sealed_probe",
     "r279",
     ["PRIME.PORT.RHP.MIDPOINT.ORIENTED_THEOREM.01"],
     "oriented-midpoint proof round (32/32): the two-sided index "
     "bilanz (left degree n vs dual degree S-1-n against the S "
     "common nodes of the gauge polynomial L): STEP5_OPEN (no "
     "non-restatement candidate kips at N_w: C1 tight-two-sided "
     "never fires anywhere -- a world-blind THEOREM; C2 union "
     "reality / C3 shared gap / C4 left-in-D die at degrees 1..4 "
     "on every world; C5 = first crossing is the h restatement, 78"
     " pattern mismatches = the r274 re-entry pivots) + "
     "OBSTRUCTION_REFUTED (3 exact rational toy counterexamples: "
     "the two-sided compatibility state does NOT forbid the "
     "crossing) + TWO_SIDED_PARITY_THEOREM (T2 node-identity "
     "signs, 246212 gates; T3 forced-gap parity: union occupancy "
     "ODD in every weight-agreement gap, EVEN in every "
     "disagreement gap, at EVERY degree, h-sign-blind; T3' census "
     "bilanz c + c# = (S-1) - |D| + 2 scD, exhaustion-proved k <= "
     "8) + CROSSING_BUDGET_THEOREM (Jacobi/Sylvester: #(h_n < 0 "
     "over the FULL continuation) == S_- = #negative atoms EXACTLY"
     " on every world: w9 104, w13 98, EPST/SCR/SMOOTH 141/94/6, "
     "kz15 121, kz52 551) + "
     "MAIN_SPECIFICITY(LOCALIZATION_IS_THE_ARITHMETIC: the "
     "machinery is world-blind on all controls pre+post flip; the "
     "ENTIRE arithmetic is WHERE the fixed budget is spent -- "
     "mains/wards at min C = N_w +0/+2/+1/+0, controls at "
     "25/21/27); amendments a1-a3 disclosed (R2 anchor == min C + "
     "1, localization equality NOT universal -- w13 crosses at N_w"
     " + 2); the b3 gap statement (Lean-suitable): forall n < N_w "
     ": h_n > 0, i.e. min C >= N_w -- the localization of the "
     "Jacobi-fixed budget is the named open center; consumed by v962 "
     "(wave 5, embedded byte-exact, smoke stage)", True),
    (f"{EXP}/budget_localization_probe.py", "sealed_probe",
     "r280",
     ["PRIME.PORT.WALL.BUDGET_LOCALIZATION.01"],
     "budget-localization anatomy round (29/29): "
     "LOCALIZATION_CENSUS (ALL 42 rungs: offsets min C - N_w "
     "distribution {+0: 18, +1: 10, +2: 6, +3: 6, +4: 1, +5: 1}, "
     "max +5 at kz43, sp(offset, N) = +0.096 over N in "
     "[142, 878] -- O(1), no N-growth; v956/r279 anchors "
     "0/2/2/3/1 + kz15 +1 + kz52 +0 exact; half-filling N_w == "
     "(S+1)//2 on 42/42; mp dps-40 arbitration exact; controls "
     "25/21/27; dose link: min C == nf definitional, the r276 "
     "P2_JIT depth medians 0.250/0.207 reproduced with the exact "
     "seeds -- dose curve and budget localization are ONE "
     "coordinate) + MAIN_NOT_MAXIMAL (the round's core finding: "
     "the w9 extremal localization min C = N_w is NOT a local "
     "maximum of the localization functional -- the r278-gradient "
     "directions OPT/OPT_SAFE/SMALLPRIME push min C 184 -> 185 "
     "PAST half-filling at theta 7.7e-5..1.6e-4, all mp-"
     "confirmed; the b3 variational hypothesis is REFUTED in its "
     "local-maximum form; kz15/w13 offset windows: first-order "
     "raisers exist, none verifies at the tested doses -- "
     "UNRESOLVED) + CRITICALITY_STRUCTURED (cos_w(grad h_minC, "
     "grad h_minC-1) = -0.97 on all three worlds: the crossing "
     "log-gradient is anti-aligned with the last free pivot -- "
     "the h-sign flip of a raw-gradient lockstep; rho_crit 245 = "
     "the 1/|h_minC| inflation of the shallow crossing) + "
     "DUAL_TRANSLATION_EXACT (toys exact in rationals: "
     "h_{S-m} h#_{m-1} == 1, sign h#_k == sign h_{S-1-k}, D_n == "
     "prod h_k; w9 mp: min C >= N_w <=> ALL S_- = 104 dual "
     "negative pivots confined to the lower dual half, and w9 "
     "SATURATES the bound exactly: max neg dual pivot 182 == "
     "S - 1 - N_w) + DUAL_RESTATEMENT (dual negative-mass "
     "fraction 0.424, no isolated carrier) + "
     "MOMENT_PERTURBATION_RANGE(X_weyl = 2 of N_w = 184: the "
     "natural mu/nu Weyl minor-perturbation argument carries 1.1 "
     "percent of the way; PAIRCORR detector: Weyl X = 1/2/6/2 on "
     "EPST/SCR/SMOOTH/HL2 (SMOOTH exceeds MAIN) and the raw-"
     "moment rest zone are BOTH world-blind -- neither carries "
     "the localization); amendments a1-a3 disclosed (Richardson "
     "FD protocol, dual-mirror slice bug fix, wording); NO "
     "localization claim from the census; consumed by v962 "
     "(wave 5, embedded byte-exact, smoke stage)", True),
    (f"{EXP}/halffilling_pinning_probe.py", "sealed_probe",
     "r281",
     ["PRIME.PORT.WALL.HALFFILLING_PINNING.01"],
     "halffilling-pinning round (28/28): UPPER_PINNING_MEASURED (C"
     " = 5 over the 42-rung census; the v956 boundary statement "
     "'the wall dies immediately past the cap' is carried by TWO "
     "computational paths + an mp dps-40 ward on five windows = "
     "MEASUREMENT, not a symbolic theorem; the only PROVEN upper "
     "side is the pigeonhole ceiling minC <= S - S_- from the r279"
     " budget theorem -- w9: 184 <= 263 = p, 79 degrees above N_w;"
     " world-blind O(1) upper pinning REFUTED exactly: the "
     "single-tiny-negative toy measure has minC = S-1, offset = "
     "N_w - 2, unbounded in S -- any O(1) upper pinning must "
     "consume the comb structure) + OFFSET_UNSTRUCTURED (six "
     "sealed source-pure tail-coupling candidates vs offset over "
     "the 42 rungs: max |spearman| = 0.273 << 0.75 -- no "
     "predictive offset formula in this census; honest negative) +"
     " RELAY_CONDITION_FOUND(B_n = [beta_n > 0], RESTATEMENT: no "
     "h-blind margin proxy predicts the flip location on all five "
     "worlds; the r280 anti-alignment cos_w = -0.97 is the h-sign "
     "flip of a raw-gradient lockstep, cos_raw = +0.96..+0.98 at "
     "every crossing; all four dead-world crossings type CREEPING "
     "-- crossing type does not separate the worlds) + "
     "PINNING_DECOMPOSED (the program finding: COUNTING THEOREM "
     "exact -- the free pivots are exactly h_0..h_{N_w-1}, h_{N_w}"
     " is the first forced pivot (toys in rationals, w9 mp dps-200"
     " L-recurrence residual 7.6e-157, forced-fraction profile "
     "exact), so 'why half-filling' = THE FREE MOMENTS END THERE; "
     "the lower side minC >= N_w == 'all free pivots positive' "
     "stays the open center).  Regressions: r280 census "
     "distribution + anchors + flips + cosines exact; v956 quotes "
     "byte-gated.  NO RH claim.; consumed by v962 (wave 5, "
     "embedded byte-exact, smoke stage)",
     True),
    (f"{EXP}/representation_contest_probe.py", "sealed_probe",
     "r282",
     ["PRIME.PORT.REPRESENTATION.CONTEST.01"],
     "representation-contest round (30/30): the north-star "
     "question 'what IS h_n' run as a four-language contest with "
     "one brutal gate (structural forcing of MAIN positivity + "
     "provable rejection of an early-dying control; calibrated on "
     "the positive-class toy POSLIKE). K1 RHP/MONODROMY typed "
     "REPRESENTATION_RESTATEMENT (Pontryagin split h_n = P_n - N_n"
     " exact at every degree on all four toys; the "
     "|m|^2/sum-of-squares structure exists iff the negative "
     "register is empty -- true exactly on POSLIKE, false on every"
     " signed toy incl. MAINLIKE with N/P = 0.538 at the last free"
     " degree; w9 negfrac 0.498 at the wall; the surviving clause "
     "N < P is h > 0 verbatim) + K2 HODGE/INTERSECTION typed "
     "REPRESENTATION_NOT_CONSTRUCTIBLE (the Kasteleyn/orientation "
     "question answered by FULL EXHAUSTION: the coherent linear "
     "orientation class over the Cauchy-Binet configuration space "
     "is EXACTLY {+-sign w} on all four toys (2^S gauges each), "
     "the quadratic/edge class collapses at the n = 3 cells; the "
     "unique surviving gauge changes the value by exactly 2 x "
     "negative mass (exact defect at n = 1; w9 0.1152, S_- = 104) "
     "-- coherence and value preservation are simultaneously "
     "possible iff S_- = 0: the orientation exists exactly for the"
     " positive class, and MAIN is signed; the r261 no-go upgraded"
     " from pairing failure to class obstruction) + K3 DE "
     "BRANGES/CANONICAL SYSTEM typed REPRESENTATION_RESTATEMENT "
     "(Hamiltonian PSD through degree n <=> h_0..h_n > 0 exact "
     "bookkeeping; the only independent shadow, R2 interlacing, "
     "lags +1 on every flipping world -- toys minC + 1 exact, "
     "controls 26/22/28/26 == flip + 1, w9 SAFE through n = 183: "
     "the shadow detects, it never forbids; the |beta| repair "
     "changes the measure at k = 4 exactly) + K4 OPERATOR/DUAL "
     "PAIR typed REPRESENTATION_WORLD_BLIND (h_n h#_{S-1-n} == 1 "
     "exact on all four toys => sign sync holds IDENTICALLY in "
     "every world through every flip -- the v956 dual pair adds no"
     " second constraint; global positive structures are killed by"
     " the r279 budget theorem #(h<0) = S_-) + CONTEST_ALL_DEAD "
     "(the program finding: the pivot positivity has NO "
     "representation in the four classical languages at this "
     "resolution -- each language forces positivity exactly for "
     "the positive measure class, and MAIN is signed; the lower "
     "side stays the open center).  Detector: D1 negfrac / D2 "
     "defect / D4 sync WORLD_BLIND, D3 fire/N separates but is "
     "DECLARED h-reading (decoration).  Amendment a1 (smoke stage,"
     " gate-side m4 loudness form) disclosed.  NO RH claim.; "
     "consumed by v963 (wave 6, embedded byte-exact, smoke stage)",
     True),
    (f"{EXP}/fullsource_quasidefiniteness_probe.py", "sealed_probe",
     "r283",
     ["PRIME.PORT.RHP.FULLSOURCE.QUASIDEFINITENESS.01"],
     "fullsource-quasidefiniteness round (26/26): the big RHP "
     "attack (full source -> monodromy property -> "
     "quasi-definiteness, three sealed candidates). VERDICT "
     "MECHANISM_PARTIAL(A2 monodromy factorization over the "
     "positive/negative part: in the mu-orthonormal frame the full"
     " Hankel form is I - M_n with the node Gram E_n = B_n B_n^T "
     "EXACTLY the v881/r224 IIKS kernel (mu-CD kernel dressed by "
     "the nu weights); steps s1-s4 EXACT -- split, unit-triangular"
     " congruence minor_k(D_mu - G) == D_k(mutilde) (rationals on "
     "five toys, slogdet dev 3.4e-9 on w9), frame contraction h>0 "
     "window <=> lambda_max(E_m) < 1, monotone rank-one loading =>"
     " lambda_max crosses 1 EXACTLY at minC+1; WORLD TEST exact on"
     " all seven worlds: MAIN w9 185 == minC+1, w13 171 == N+3, "
     "kz15 205 == N+2, controls EPST/SCR/SMOOTH/HL2 26/22/28/26 =="
     " flip+1 == the r277 R2 fire degrees -- the contraction IS "
     "the split-source form of the r277 reality/interlacing "
     "condition; s5 capacity: the pigeonhole ceiling minC <= S_+ "
     "RE-PROVED in the frame (null-polynomial witness, exact on "
     "five toys), capacity-as-COUNTING REFUTED exactly (rank-one "
     "pair eps/big: same rank, same support, opposite window fate;"
     " the deciding value is metric 1.25e-13 vs 1.25e+2); MISSING "
     "LEMMA L* formal: for MAIN every real polynomial p with deg p"
     " < N_w has int p^2 dnu < int p^2 dmu, i.e. "
     "lambda_max(E_{N_w}) < 1 (measured margin 1 - rho_184 = "
     "1.68e-4, top eigs 0.99983/0.99874/0.99597 -- broadly tight, "
     "not single-mode); given s1-s4 this ONE scalar <=> full "
     "free-window quasi-definiteness) + A3_COLLAPSES_TO_A2 "
     "(Fredholm zero-freeness of det(I - s E_{N_w}) on (0,1] IS "
     "the contraction scalar: s* = 1/rho dictionary + "
     "degree-resolved slogdet co-location 185/26) + A1_DEAD "
     "(Schwarz reflection symmetry of the real jump data holds "
     "identically on every world = WORLD_BLIND, cannot carry; the "
     "classical additional condition -- residue "
     "positivity/Herglotz -- fails on MAIN ITSELF (S_- = 104 "
     "negative residues); the windowed eta* anatomy is world-blind"
     " by the sealed distance rule; the additional condition "
     "collapses onto L*) + DETECTOR_LEDGER (K_A2 rho_20 "
     "WORLD_BLIND -- honest: the early-degree contraction VALUE "
     "does not separate; K_A3 1/rho_40 MAIN_SEPARATING; "
     "triangle/Gershgorin bound dead at n = 21 << 185; "
     "target-inverse and posthoc-window mutants FLAGGED; full "
     "source consumed, no truncation).  The RHP language holds "
     "exactly ONE invariant on this question and it is the "
     "contraction scalar; the lower side (L* itself) stays the "
     "open center.  NO RH claim.; consumed by v963 (wave 6, "
     "embedded byte-exact, smoke stage)",
     True),
    (f"{EXP}/lstar_two_measure_probe.py", "sealed_probe",
     "r284",
     ["PRIME.PORT.LSTAR.TWO_MEASURE_ANATOMY.01"],
     "L* two-measure anatomy round (30/30): the r283 missing lemma"
     " L* read as a TWO-MEASURE SUBORDINATION problem (nu 104 "
     "atoms strictly mu-subordinate, 263 atoms, on deg < N_w).  "
     "VERDICT SHIELDING_BLIND (the source-pure pairing geometry is"
     " a builder-channel property: on w9 EVERY nu atom sits one "
     "fold step from a mu atom, interlacing 100/104 all-mu-"
     "neighbored, and the four dead controls mirror the same "
     "near-perfect pairing -- all four sealed geometry statistics "
     "WORLD_BLIND by the r281 distance rule) + NYQUIST_ORDERING("
     "MAX sp +0.998 over 46 worlds, HONEST: carried by the trivial"
     " N_w scaling of the ladder; the sealed band |log2(n_pred/"
     "crossing)| <= 1 with n_pred = L/(4s) FAILS on all four "
     "controls, devs 1.48..3.06 octaves -- the controls die at "
     "22..28 DESPITE near-perfect pairing: the support-geometry "
     "form of the resolution/shielding hypothesis is refuted where"
     " it matters) + CHRISTOFFEL_RANGE(the round's core: exact "
     "sandwich max_k v_k K_n(y_k) <= lambda_max(E_n) <= trace(E_n)"
     " gated everywhere; on w9 the trace/triangle side crosses at "
     "n_CS = 10 while the pure single-atom Christoffel bound "
     "crosses at n_DIAG = 187, only TWO degrees above the true "
     "crossing 185: MAIN's wall crossing is a NEAR-SINGLE-ATOM "
     "Christoffel event (coherent assist gain rho/maxdiag = 1.031 "
     "at N_w; aggregate slack trace/rho = 50.2 -- destructive nu "
     "coherence, the cancellation story in the two-measure "
     "coordinate), while on ALL FOUR controls n_DIAG is never "
     "reached by their crossing: control death is a COLLECTIVE "
     "mode) + EXTREMAL_ANATOMY(the near-breaking direction is "
     "99.7 percent TWO background atoms at the shallow-u hull edge"
     " below the first prime (folds 2 and 4, u = 0.03/0.06, "
     "x -> +1, the two weakest-shielded nu atoms, PR 1.89), NOT "
     "the small primes -- SMALLP_DEPLETED, the r278 chain-"
     "sensitivity profile and the extremal near-null direction are"
     " different coordinates; controls at crossing are MORE "
     "diffuse (PR 4.97..9.72); top-3 eigenvectors ONE_BAND, three "
     "oscillatory modes of one edge band) + DETECTOR_LEDGER(all "
     "seven sealed stats WORLD_BLIND -- the separation lives in "
     "the range structure, not in any sealed scalar).  mp dps-60 "
     "ward: rho_184 = 0.99983248 < 1 < 1.00003660 = rho_185.  "
     "Regressions: r283 spectral records, r281 42-rung census "
     "distribution + anchors, control flips 25/21/27/25.  NO RH "
     "claim.; consumed by v963 (wave 6, embedded byte-exact, "
     "smoke stage)",
     True),
    (f"{EXP}/christoffel_decomposition_probe.py", "sealed_probe",
     "r285",
     ["PRIME.PORT.LSTAR.CHRISTOFFEL_DECOMPOSITION.01"],
     _R285_STATUS + "; consumed by v963 (wave 6, embedded "
     "byte-exact, smoke stage)",
     True),
    (f"{EXP}/lstar_margin_scaling_probe.py", "sealed_probe",
     "r286",
     ["PRIME.PORT.LSTAR.MARGIN_SCALING.01"],
     _R286_STATUS + "; consumed by v964 (wave 7, embedded byte-exact, smoke stage)",
     True),
    (f"{EXP}/l2_deterministic_cancellation_probe.py", "sealed_probe",
     "r287",
     ["PRIME.PORT.L2.DETERMINISTIC_CANCELLATION.01"],
     _L2_STATUS + "; consumed by v964 (wave 7, embedded byte-exact, smoke stage)",
     True),
    (f"{EXP}/destructive_coherence_probe.py", "sealed_probe",
     "r288",
     ["PRIME.PORT.LSTAR.DESTRUCTIVE_COHERENCE.01"],
     _R288_STATUS + "; consumed by v964 (wave 7, embedded byte-exact, smoke stage)",
     True),
    (f"{EXP}/arch_kernel_diophantine_probe.py", "sealed_probe",
     "r289",
     ["PRIME.PORT.LSTAR.ARCH_KERNEL_DIOPHANTINE_ANATOMY.01"],
     _R289_STATUS + "; consumed by v964 (wave 7, embedded byte-exact, smoke stage)",
     True),
    (f"{EXP}/profile_functional_probe.py", "sealed_probe",
     "r290",
     ["PRIME.PORT.LSTAR.PROFILE_FUNCTIONAL.01"],
     _R290_STATUS + "; consumed by v965 (wave 8, embedded byte-exact, smoke stage)",
     True),
    (f"{EXP}/ridge_anatomy_probe.py", "sealed_probe",
     "r291",
     ["PRIME.PORT.LSTAR.RIDGE_ANATOMY.01"],
     _R291_STATUS + "; consumed by v965 (wave 8, embedded byte-exact, smoke stage)",
     True),
    (f"{EXP}/curvature_form_probe.py", "sealed_probe",
     "r292",
     ["PRIME.PORT.LSTAR.CURVATURE_FORM.01"],
     _R292_STATUS + "; consumed by v965 (wave 8, embedded byte-exact, smoke stage)",
     True),
    (f"{EXP}/metric_reconciliation_probe.py", "sealed_probe",
     "r293",
     ["PRIME.PORT.LSTAR.METRIC_RECONCILIATION.01"],
     _R293_STATUS + "; consumed by v965 (wave 8, embedded byte-exact, smoke stage)",
     True),
    (f"{EXP}/f10_stability_probe.py", "sealed_probe",
     "r294",
     ["PRIME.PORT.LSTAR.F10_STABILITY.01"],
     _R294_STATUS + "; consumed by v965 (wave 8, embedded byte-exact, smoke stage)",
     True),
    (f"{EXP}/f10_sp_hardening_probe.py", "sealed_probe",
     "r295",
     ["PRIME.PORT.LSTAR.F10_SP_HARDENING.01"],
     _R295_STATUS + "; consumed by v965 (wave 8, embedded byte-exact, smoke stage)",
     True),
    (f"{EXP}/dens_identity_probe.py", "sealed_probe",
     "r296",
     ["PRIME.PORT.LSTAR.DENS_IDENTITY.01"],
     _R296_STATUS
     + "; consumed by v966 (wave 9, embedded "
     "byte-exact, smoke stage)",
     True),
    (f"{EXP}/vdc_chain_provenance_probe.py", "sealed_probe",
     "r297",
     ["PRIME.PORT.L2.VDC_CHAIN_PROVENANCE.01",
      "PRIME.PORT.L2.VDC_LEMMA.01"],
     _R297_STATUS
     + "; consumed by v966 (wave 9, embedded "
     "byte-exact, smoke stage)",
     True),
    (f"{EXP}/window_border_transfer_probe.py", "sealed_probe",
     "r298",
     ["PRIME.PORT.L2.WINDOW_BORDER_TRANSFER.01",
      "PRIME.PORT.L2.VDC_LEMMA.01"],
     _R298_STATUS
     + "; consumed by v966 (wave 9, embedded "
     "byte-exact, smoke stage)",
     True),
    (f"{EXP}/fejer_decay_probe.py", "sealed_probe",
     "r299",
     ["PRIME.PORT.L2.FEJER_DECAY.01",
      "PRIME.PORT.L2.VDC_LEMMA.01"],
     _R299_STATUS
     + "; consumed by v966 (wave 9, embedded "
     "byte-exact, smoke stage)",
     True),
    (f"{EXP}/diag_target_probe.py", "sealed_probe",
     "r300",
     ["PRIME.PORT.L2.DIAG_TARGET.01",
      "PRIME.PORT.L2.VDC_LEMMA.01"],
     _R300_STATUS
     + "; consumed by v966 (wave 9, embedded "
     "byte-exact, smoke stage)",
     True),
    (f"{EXP}/neff_target_probe.py", "sealed_probe",
     "r301",
     ["PRIME.PORT.L2.NEFF_TARGET.01",
      "PRIME.L2.NEFF_TARGET.01",
      "PRIME.PORT.L2.VDC_LEMMA.01"],
     _R301_STATUS,
     True),
    (f"{EXP}/unif_target_probe.py", "sealed_probe",
     "r302",
     ["PRIME.PORT.L2.UNIF_TARGET.01",
      "PRIME.L2.NEFF_TARGET.01",
      "PRIME.PORT.L2.VDC_LEMMA.01"],
     _R302_STATUS,
     True),
    (f"{EXP}/atom_target_probe.py", "sealed_probe",
     "r303",
     ["PRIME.PORT.L2.ATOM_TARGET.01",
      "PRIME.L2.NEFF_TARGET.01",
      "PRIME.PORT.L2.VDC_LEMMA.01"],
     _R303_STATUS,
     True),
    (f"{EXP}/shortrange_law_probe.py", "sealed_probe",
     "r304",
     ["PRIME.PORT.L2.SHORTRANGE_LAW.01",
      "PRIME.L2.NEFF_TARGET.01",
      "PRIME.PORT.L2.VDC_LEMMA.01"],
     _R304_STATUS,
     True),
    (f"{EXP}/renyi3_probe.py", "sealed_probe",
     "r306",
     [],
     _R306_STATUS,
     True),
    (f"{EXP}/fixed_head_probe.py", "sealed_probe",
     "r307",
     [],
     _R307_STATUS,
     True),
    (f"{EXP}/block_green_probe.py", "sealed_probe",
     "r308",
     [],
     _R308_STATUS,
     True),
    (f"{EXP}/paired_cone_probe.py", "sealed_probe",
     "r309",
     [],
     _R309_STATUS,
     True),
    (f"{EXP}/blockgreen_nontriviality_probe.py", "sealed_probe",
     "r311",
     [],
     _R311_STATUS,
     True),
    (f"{EXP}/blockgreen_membership_probe.py", "sealed_probe",
     "r312",
     [],
     _R312_STATUS,
     True),
    (f"{EXP}/renyi3_proof_fork_probe.py", "sealed_probe",
     "r313",
     [],
     _R313_STATUS,
     True),
    (f"{EXP}/signed_cubic_flux_probe.py", "sealed_probe",
     "r314",
     [],
     _R314_STATUS,
     True),
    (f"{EXP}/phi3_functional_probe.py", "sealed_probe",
     "r315",
     [],
     _R315_STATUS,
     True),
    (f"{EXP}/two_regime_bound_probe.py", "sealed_probe",
     "r316",
     [],
     _R316_STATUS,
     True),
    (f"{EXP}/exception_families_probe.py", "sealed_probe",
     "r317",
     [],
     _R317_STATUS,
     True),
    (f"{EXP}/indefinite_fork_probe.py", "sealed_probe",
     "r318",
     [],
     _R318_STATUS,
     True),
    (f"{EXP}/continuous_coordinate_probe.py", "sealed_probe",
     "r321",
     [],
     _R321_STATUS,
     True),
    (f"{EXP}/antiphase_sign_law_probe.py", "sealed_probe",
     "r322",
     [],
     _R322_STATUS,
     True),
    (f"{EXP}/fa_provenance_probe.py", "sealed_probe",
     "r324-pre",
     [],
     _R324PRE_STATUS,
     True),
    (f"{EXP}/qmax_m2_origin_probe.py", "sealed_probe",
     "r324",
     [],
     _R324_STATUS,
     True),
    (f"{EXP}/extraction_order_probe.py", "sealed_probe",
     "r325",
     [],
     _R325_STATUS,
     True),
    (f"{EXP}/group_mass_cap_probe.py", "sealed_probe",
     "r327",
     [],
     _R327_STATUS,
     True),
    (f"{EXP}/ext3_fresh_anchors_probe.py", "sealed_probe",
     "r329",
     [],
     _R329_STATUS,
     True),
    (f"{EXP}/dirichlet_secondworld_probe.py", "sealed_probe",
     "r330",
     [],
     _R330_STATUS,
     True),
    (f"{EXP}/twin_resolution_probe.py", "sealed_probe",
     "r331",
     [],
     _R331_STATUS,
     True),
    (f"{EXP}/companion_orbit_packing_probe.py", "sealed_probe",
     "r333",
     [],
     _R333_STATUS,
     True),
    (f"{EXP}/fold_capacity_probe.py", "sealed_probe",
     "r334",
     [],
     _R334_STATUS,
     True),
    (f"{EXP}/edge_packing_dichotomy_probe.py", "sealed_probe",
     "r335",
     [],
     _R335_STATUS,
     True),
    (f"{EXP}/lstar_parity_section_probe.py", "sealed_probe",
     "r336",
     [],
     _R336_STATUS,
     True),
    (f"{EXP}/fold_martingale_probe.py", "sealed_probe",
     "r337",
     [],
     _R337_STATUS,
     True),
    (f"{EXP}/fold_density_dictionary_probe.py", "sealed_probe",
     "r339",
     [],
     _R339_STATUS,
     True),
    (f"{EXP}/cauchybinet_hall_probe.py", "sealed_probe",
     "r340",
     [],
     _R340_STATUS,
     True),
    (f"{EXP}/pair_extremal_probe.py", "sealed_probe",
     "r342",
     [],
     _R342_STATUS,
     True),
    (f"{EXP}/fold_bellman_reverse_holder_probe.py", "sealed_probe",
     "r341",
     [],
     _R341_STATUS,
     True),
    (f"{EXP}/pair_coupling_probe.py", "sealed_probe",
     "r343",
     [],
     _R343_STATUS,
     True),
    (f"{EXP}/fold_two_scale_balance_probe.py", "sealed_probe",
     "r344",
     [],
     _R344_STATUS,
     True),
    (f"{EXP}/gap_ratio_primary_probe.py", "sealed_probe",
     "r345",
     [],
     _R345_STATUS,
     True),
    (f"{EXP}/fold_cover_canonization_probe.py", "sealed_probe",
     "r346",
     [],
     _R346_STATUS,
     True),
    (f"{EXP}/delta_alpha_closure_probe.py", "sealed_probe",
     "r347",
     [],
     _R347_STATUS,
     True),
    (f"{EXP}/delta_source_anatomy_probe.py", "sealed_probe",
     "r348",
     [],
     _R348_STATUS,
     True),
    (f"{EXP}/thirdarm_spike_law_probe.py", "sealed_probe",
     "r349",
     [],
     _R349_STATUS,
     True),
    (f"{EXP}/alpha_source_anatomy_probe.py", "sealed_probe",
     "r350",
     [],
     _R350_STATUS,
     True),
    (f"{EXP}/qmax_growth_law_probe.py", "sealed_probe",
     "r351",
     [],
     _R351_STATUS,
     True),
    (f"{EXP}/rhor_source_anatomy_probe.py", "sealed_probe",
     "r352",
     [],
     _R352_STATUS,
     True),
    (f"{EXP}/second_family_erosion_probe.py", "sealed_probe",
     "r353",
     [],
     _R353_STATUS,
     True),
    (f"{EXP}/phi_wander_anatomy_probe.py", "sealed_probe",
     "r354",
     [],
     _R354_STATUS,
     True),
    (f"{EXP}/k2_source_formula_probe.py", "sealed_probe",
     "r355",
     [],
     _R355_STATUS,
     True),
    (f"{EXP}/borodin_dual_hole_probe.py", "sealed_probe",
     "r356",
     [],
     _R356_STATUS,
     True),
    (f"{EXP}/dirichlet_matched_frame_probe.py", "sealed_probe",
     "r357",
     [],
     _R357_STATUS,
     True),
    # -- the standalone problem statement (rh/problem/) --
    ("rh/problem/lstar_problem.tex", "problem_statement",
     "r283 companion",
     ["PRIME.PORT.RHP.FULLSOURCE.QUASIDEFINITENESS.01"],
     "the missing lemma L* as a fully standalone open problem for "
     "external mathematicians (no project vocabulary): mu/nu defined "
     "from first principles (von Mangoldt comb, tent sampling, "
     "archimedean lag function, circulant spectral density, "
     "folding), the S = 367 instance tabulated, Hankel / CD-kernel / "
     "sampling equivalents, neutral numerical record (42/42 hold; "
     "margins 1.68e-4 down to 1.42e-7, shrinking with S), "
     "moment-counting meaning of the degree bound (S+1)/2; "
     "the 2026-08-25 update paragraph (57/57 instances positive, "
     "flattening power law, the rational-twin fact: the problem is "
     "NOT diophantine, the metric threshold 1e-3..3e-3 gap); "
     "since 2026-08-27 the freeze memo section 'The frozen state "
     "(August 2026): one object' (reviewer decision: the L* lane "
     "FROZEN as specialist problem): the fully typed chain "
     "(dictionary weights / candidate deficits / theorem-grade "
     "pinning / computability closure), the one object (phi_D = "
     "log(pq) + (17/12) ln N and phi_K = log(c^2) + (17/12) ln N "
     "are one shared wander, corr 0.999998, 0.88 nats each vs "
     "0.0017 nats difference -- factor ~500 -- whose difference IS "
     "pointwise the log reserve with rho_r = 2.624 its decay; "
     "two-block interference: pair geometry +0.887 at 2.4x "
     "amplitude against the anti-correlated weight wander -0.72), "
     "the three specialist questions in final form (q1 backward-CS "
     "= the cancellation ratio, q2 sub-classical Christoffel "
     "growth with candidates unresolvable below 10^5.4+, q3 the "
     "resolution paradox), and the honest census frame (85 windows "
     "to N_w 7942, all margins positive, pool exhausted at "
     "10^3.90); since 2026-08-27 (evening) additionally the closing "
     "subsection 'Placement in the literature, and addressees': the "
     "multi-point Uvarov-transform dictionary (Kwon et al. 2001 / "
     "Aktas-Area-Perez 2022: I + Lambda K_n similar to I - E_n), "
     "the discrete-hard-edge / BKMM-saturation-regime placement "
     "(rho_K ~ N^-1.42 measured excludes the AC/Lubinsky class at "
     "family-constant rescaled positions a_j = 2N^2(1-y_j); "
     "saturation adjacency marked as hypothesis) and the four "
     "addressee communities; since 2026-08-27 (late evening) the "
     "closing addendum 'the particle-hole reparametrization (round "
     "356)': the exactly equivalent form L* <=> R > (1/2) I via "
     "Borodin 2002 duality at half filling (reciprocal weight "
     "u_vee prop kappa (1-x)/|f|, exact spectral map margin = 2 - "
     "1/lambda_min(R), pair block = the (1,2) minor of 2I - "
     "R^{-1}; theorem-grade identities on measured inputs), the "
     "anti-correlation of the two wander blocks re-typed as "
     "duality algebra by design (+log|f| vs -log|f|, gated "
     "-0.999998 -- the one-object question narrows to the ~500x "
     "smallness of the difference alone), and the census-grade "
     "reserve localization in the local dual 2x2 block "
     "((R_pair)^{-1} predicts the log reserve, +0.9982 / puretest "
     "+0.9828) -- no compression (the duality is a "
     "reparametrization), the AC-class exclusion independently "
     "re-gated; explicitly NO claim -- L* stays [O]", True),
    ("rh/problem/verify_lstar_instance.py", "problem_check",
     "r283 companion",
     ["PRIME.PORT.RHP.FULLSOURCE.QUASIDEFINITENESS.01"],
     "standalone rebuild of the document's mu/nu construction "
     "(numpy/mpmath only) cross-checked against the repository "
     "builders: atoms/weights agree to 4e-16 rel, lambda_max(E_184) "
     "= 0.99983248 / lambda_max(E_185) = 1.00003660 reproduced with "
     "dps-60 mpmath ward, inequality gated on monomials + 500 "
     "random polynomials; 12/12 gates, final line LSTAR INSTANCE "
     "VERIFIED; optional --ladder sweeps all 42 admissible windows "
     "(all margins positive, min 1.42e-7 at kz64)", True),
    ("rh/problem/lstar_problem.pdf", "problem_statement",
     "r283 companion",
     [],
     "compiled PDF of lstar_problem.tex (recompiled artefact, "
     "registered unpinned)", False),
    ("rh/problem/rdagger_saturation.tex", "problem_statement",
     "r360+r362 companion, updated r367-r373 / r412 / r426 / R-DOSSIER DCCXCVII",
     [],
     "specialist dossier on the bordered dual resolvent R-dagger "
     "(reviewer priority 4; updated after r367-r373): definition of "
     "R-dagger as the rank-1 bordered dual hole kernel [[R^{-1}, Dv],"
     "[(Dv)^T, 1+gamma]]^{-1}; exact duality package (A1)-(A7); "
     "critical 3x3 Schur block; pair (2,4) straddles saturation-block "
     "edge 3|4; observed exponent alpha = 3.332; relative "
     "error-operator form.  PRIMARY question after the two-rank "
     "inertia cut is the MINIMAL form (P1) ind_-(R_{N-3}-1/2 I) <= 1 "
     "(census: overload 0/74, dichotomy 45 nneg-1 / 29 already-PD) "
     "and (P2) det K2 <= -c0 < 0 on the nneg-1 branch "
     "(-det K2 in [1.157, 1126.389], floor 0.50, corr -0.0064); "
     "Haynsworth (haynsworth_two_rank, haynsworth_mixed) and the "
     "R-dagger layer Lean sorry-free (census 7); mixed 3x3 form "
     "M-dagger = blkdiag(A0,-1/2)+U J U^T with J=diag(1,1,1/den); "
     "wedge-sign census, Phi-monotonicity, Pruefer dictionary; "
     "named dead ends (no 3x3 Jacobi Casoratian residual 3.615e-2, "
     "phase restatement, r366 O(1) mass buffer, r363 edge pinning). "
     "The older RHP/BKMM saturation question (BKMM 2007 Thm 2.7/"
     "Rem 2.8) is retained as the stronger variant.  Finite census, "
     "no asymptotics, no claim; a proof of (P1)+(P2) lands via the "
     "kernel-checked chain at window-local master positivity.  "
     "r426 adds the edge-balance chain (eight identities, "
     "P1/VAC/tot separators, floor R_inf~0.030, two open "
     "limits q_N<1 and Sigma_inf; Lean RH/EdgeBalance.lean "
     "sorry-free, census stays 5).  "
     "R-DOSSIER DCCXCVII: two cancellation cores (bulk four "
     "killed vectors + QD 1.357130 + min-norm 0.359 + r399 "
     "circularity; terminal Z_loc formula + selected margin "
     "0.617 vs 0.0195); r427 audit 0 BUG/5 CLEAN/2 SUSPECT "
     "(kernel-Loewner definiteness hypothesis explicit); "
     "open Potapov program S_<=1 bulk / S_0 edge via Redheffer "
     "pivot 1/4-|Z_loc|^2, semidefinite+frequently quantifiers.  "
     "Refutation table 28 closed routes.  "
     "Explicitly NO RH claim -- L* and L-dagger stay [O]", True),
    ("rh/problem/rdagger_saturation.pdf", "problem_statement",
     "r360+r362 companion, updated r367-r373",
     [],
     "compiled PDF of rdagger_saturation.tex (recompiled artefact, "
     "registered unpinned)", False),
    ("rh/problem/medcap_lemma.tex", "problem_statement",
     "r361 companion",
     [],
     "proof attempt for the r361 MED-CAP lemma med_i <= (8/3) sep_i "
     "(reviewer priority 1): SEP-SATZ proved as cut geometry "
     "(d_i = empty_i + (n_i+n_{i+1})/2); tiling (empty==0, hull-solid) "
     "implies gap_i = sep_i identically, so MED-CAP reduces to an "
     "order-statistic bound on the block-length sequence n_i; the "
     "tiled composition n=(1,2,8^10) violates with ratio 16/3 (C2) "
     "-- MED-CAP is NOT interval geometry; the saturating prefix "
     "(1,2,6,5,4,4) at chi4 kz53 realises med=4, sep=3/2, ratio 8/3 "
     "exact (edge window: third-smallest of five neighbour-gaps); "
     "tiling census 134 windows / 15428 atoms, 0 empty, 0 hull holes, "
     "0 MED-CAP violations; remainder X_n = the n-sequence forbids a "
     "C2 jump at small-sep loci (sign-run pairing of an arbitrary "
     "+/- colouring does NOT forbid C2).  Finite identities plus a "
     "named combinatorial remainder; NO RH claim", True),
    ("rh/problem/verify_medcap_steps.py", "problem_check",
     "r361 companion",
     [],
     "machine check of every numbered lemma in medcap_lemma.tex: "
     "standalone Fractions geometry (window convention, SEP identity, "
     "tiling => gap=sep, C2 16/3, short C2 ratio 4, saturating prefix "
     "8/3, random tiled violators, ledger toy) plus construction "
     "cross-check (chi4 kz53 prefix (1,2,6,5,4,4) two atoms g=3/8; "
     "four w9 worlds tiled and MED-CAP clean).  11/11 gates, final "
     "line MEDCAP STEPS VERIFIED", True),
    ("rh/problem/medcap_lemma.pdf", "problem_statement",
     "r361 companion",
     [],
     "compiled PDF of medcap_lemma.tex (recompiled artefact, "
     "registered unpinned)", False),
    ("rh/problem/xn_invariant.tex", "problem_statement",
     "r364 companion",
     [],
     "proof attempt for the r361 remainder X_n (the length-sequence "
     "invariant of the folded sign field): pairing of positive run "
     "lengths proves n=1 only as the odd tail at theta-min, forbids "
     "prefixes (2,1) and (1,1), and isolates the unique possible "
     "sep=3/2 locus as the edge pair (1,2); pairing does NOT forbid "
     "C2 (random paired runs still violate; Chebyshev colourings do "
     "not produce (1,2)).  On the 134-window surface n=1 occurs 32 "
     "times (always index 0), (1,2) occurs once (chi4 kz53, "
     "saturating prefix (1,2,6,5,4,4), nearest n>=7 at index 7).  "
     "Named remainder V2: local run-length regularity of the "
     "bordered-chain polynomial v2 at the 20pct x-mask (no 6-plateau "
     "after three singleton runs).  Minimal grid-consistent violator "
     "named.  Finite identities plus a named analytic remainder; "
     "NO RH claim", True),
    ("rh/problem/verify_xn_steps.py", "problem_check",
     "r364 companion",
     [],
     "machine check of every numbered lemma in xn_invariant.tex: "
     "standalone pairing combinatorics (n=1 only odd tail, no (2,1) "
     "or (1,1), small-sep only edge (1,2), C2 16/3 still violates, "
     "short C2 third=6, saturating and single-spike n=7 with return "
     "to 4 both third=4, random paired violators, Chebyshev x-mask "
     "0 C2) plus construction cross-check (sign(ct)=sign(w x v2); "
     "n_i equals paired smooth-grid runs; n=1 at index 0 and four "
     "w9 worlds have no (1,2); chi4 kz53 prefix "
     "(1,2,6,5,4,4,4,8) third=4 ratio 8/3, nearest n>=7 at 7).  "
     "12/12 gates, final line XN STEPS VERIFIED", True),
    ("rh/problem/xn_invariant.pdf", "problem_statement",
     "r364 companion",
     [],
     "compiled PDF of xn_invariant.tex (recompiled artefact, "
     "registered unpinned)", False),
    ("rh/problem/v2_regularity.tex", "problem_statement",
     "r365 companion",
     [],
     "proof attempt for the r364 remainder V2 (run-length regularity "
     "of the bordered-chain polynomial v2 at the 20pct x-mask): v2 is "
     "the degree-(N-2) arithmetic OP evaluated on smooth-border nodes "
     "(source Jacobi, not mesh-only); w is the explicit smooth-fold arm "
     "sign.  Flip-XOR of the product is proved; the tempting 2-regular "
     "reduction is FALSE (11/8000 random products with a 2-regular "
     "factor still violate V2); Chebyshev x-mask never ends (1,1,1); "
     "Chebyshev x Nyquist-burst never violates; (1,1,1) yields prefix "
     "(1,2) iff the run-count is odd.  On the 134-window surface V2 "
     "holds (0 violators); two colouring triples, both regular, only "
     "one odd (chi4 kz53, w-driven saturator).  Hydra ward "
     "REGRESS_DETECTED: V2 is the final named lemma of the MED-CAP "
     "chain; T2' holds modulo V2; T1 unchanged.  Finite identities "
     "plus a named freeze; NO RH claim", True),
    ("rh/problem/verify_v2_steps.py", "problem_check",
     "r365 companion",
     [],
     "machine check of every numbered lemma in v2_regularity.tex: "
     "standalone product XOR, 2-regular reduction refuted, Chebyshev "
     "x-mask 0 (1,1,1), Chebyshev x Nyquist-burst 0 V2-viol, random "
     "products do violate, plateau violator (3^8,1,1,1) pairs to "
     "n=(1,2,6^4) and fails MED-CAP, spike (2^8,3,3,1,1,1) holds V2 "
     "and third=4, (1,1,1) gives (1,2) iff odd; construction pins "
     "(four w9 single-arm no triple; chi4 kz53 w-driven regular "
     "(1,2,6,5,4,4); chi3 kz16 v2-triple even n0=2; sign identity).  "
     "12/12 gates, final line V2 STEPS VERIFIED", True),
    ("rh/problem/v2_regularity.pdf", "problem_statement",
     "r365 companion",
     [],
     "compiled PDF of v2_regularity.tex (recompiled artefact, "
     "registered unpinned)", False),
    ("rh/problem/v2_lemma_v3.tex", "problem_statement",
     "r374 companion",
     [],
     "lemma-first attack on the r365 remainder V2 (round 374): "
     "neither proved nor refuted in the construction.  Proved: "
     "exact two-point Wronskian step formula for the scaled pair "
     "(v_{N-2}, v_{N-3}) (Lagrange identity over Q; f64 residual "
     "1.0e-15 on the pins); at the +x 20pct mask sign(x) is "
     "constant so the colouring is sign(w) sign(v2); finite "
     "contrast dichotomy on rigid Pruefer steps (constant steps "
     "never violate; slow-then-fast (0.4^21, 2.8^3) does, "
     "(1.0^21, 2.0^3) does not).  "
     "Refuted as abstract Jacobi-positivity: an 8x scale of the "
     "last 12 gamma on chi3 w9 is a v2-violator (scale 6 is not).  "
     "Weight-cluster (gap-then-spike at 8x and 64x) never violates and "
     "breaks Jacobi positivity.  Reduced to the strictly smaller "
     "finite profile lemma V3': the last 14 Pruefer steps at the "
     "mask lie in A_15 (V2-regular for every incoming remainder "
     "eta).  Path A on the six pins (0 eta-violators; every "
     "(1,1,1) is V2-regular).  Chain "
     "T2' <= 3/8 <= MED-CAP <= X_n <= V2 <= V3'.  Finite "
     "identities plus a named reduction; NO RH claim", True),
    ("rh/problem/verify_v2_lemma.py", "problem_check",
     "r374 companion",
     [],
     "machine check of every numbered lemma in v2_lemma_v3.tex: "
     "Lagrange identity over Q, combinatorial violator vs spike, "
     "constant-step 0 violators, slow-fast contrast dichotomy "
     "(347/1001 vs 0), Archimedes r=3 dwell bound, Chebyshev "
     "x-mask 0 (1,1,1), Chebyshev theta-compress 19 (1,1,1) and "
     "0 V2-viol; construction pins (Wronskian residual 1.0e-15, "
     "Path A 0 eta-violators on six pins, kz16 triple regular "
     "and every eta-111 regular, source gamma bounds, 8x last-12 "
     "gamma violator / scale 6 not, +x mask x>0, r372 dictionary, "
     "colouring V2 and kz53 w-driven regular, weight-cluster "
     "boost 8 and 64).  16/16 gates, "
     "final line V2 LEMMA V3 VERIFIED", True),
    ("rh/problem/v2_lemma_v3.pdf", "problem_statement",
     "r374 companion",
     [],
     "compiled PDF of v2_lemma_v3.tex (recompiled artefact, "
     "registered unpinned)", False),
    ("rh/problem/p2_lemma_proof.tex", "problem_statement",
     "r375 companion",
     [],
     "proof attempt for LEMMA.P2.01 (round 375, lemma-first): "
     "on nneg-1, K2 = (I+R+) - ww^T/lam_minus with w = U^T psi_minus, "
     "det K2 = det(I+R+) (1 - gamma/lam_minus) SATZ (Fractions 4-node "
     "toy det K2 = -7 exact; six scalars alpha,beta,lam,ruu,rvv,ruv); "
     "sign of det K2 is carried by the dressed overlap gamma - lam; "
     "det(I+R+) = 1+tr R++det R+ >= 1 is a sum of positive Gram terms; "
     "P1 does not imply P2 (tiny-overlap adversary det K2 > 0); the "
     "delta-term of N is load-bearing (kz46 Cauchy-sufficient fails, "
     "P2 holds); P2 is NOT the r359 bind ratio (fold-pair Schur already "
     "PD at rank N-3 on 45/45, rest-hosted 42/45).  REDUCED to the "
     "dressed-overlap inequality gamma > (1+eps) lam_minus, which "
     "implies -det K2 >= eps via det(I+R+)>=1 and does not consume "
     "lam_min(S_N).  Named remainder: source expansion of U^T psi_minus "
     "via dual CD weights and the Borodin dual mode of R_{N-3}-I/2.  "
     "Finite identities plus a named remainder; NO L* claim, NO RH claim",
     True),
    ("rh/problem/verify_p2_steps.py", "problem_check",
     "r375 companion",
     [],
     "machine check of every numbered lemma in p2_lemma_proof.tex: "
     "standalone Fractions factorization (identity 12, six-scalar Q, "
     "det K2 = det(I+R+)(1-gamma/lam), sign carrier, det(I+R+)>=1, "
     "tiny-overlap adversary) plus construction pins (w9 rest-hosted "
     "factorization; kz18 well-conditioned min excess 0.2746; kz46 "
     "delta-term necessary; chi3-w9 vacuous PD / chi4-w9 nneg-1; "
     "scramble named P1 nneg=21; RANK_KZ all gamma>lam).  12/12 gates, "
     "final line P2 STEPS VERIFIED", True),
    ("rh/problem/p2_lemma_proof.pdf", "problem_statement",
     "r375 companion",
     [],
     "compiled PDF of p2_lemma_proof.tex (recompiled artefact, "
     "registered unpinned)", False),
    ("rh/problem/postcap_pivots.tex", "problem_statement",
     "r377 companion",
     [],
     "lemma-first attack on P2-POSTCAP and P1-SINGLE-DEFECT in "
     "source pivot coordinates (round 377): dictionary SATZ "
     "(det K2 = H_N(w) H_{N-3}(a)/(H_{N+2}(w) H_{N-1}(a)) = "
     "-196/35719 on the five-atom toy; P2 iff h_N h_{N+1}<0; "
     "P1 iff ind_- H_{N+2}<=1 weak).  Node polynomial and "
     "Chebyshev aliasing SATZ.  Goal A as a universal law "
     "REFUTED (kz12 LATE, 35/85 MAIN).  nneg-1 alternation "
     "CENSUS 50/50.  Aliasing does not yield the sign without "
     "H_N^{-1}.  Goal B CENSUS 85/85 MAIN + 84/84 chi, scramble "
     "breaks.  Finite identities plus a named census; NO RH claim",
     True),
    ("rh/problem/verify_postcap_steps.py", "problem_check",
     "r377 companion",
     [],
     "machine check of every numbered lemma in postcap_pivots.tex: "
     "Fractions dictionary and complement, inertia complement, "
     "nonzero adversary, Stieltjes=Hankel, P_X nodes, Chebyshev "
     "and moment aliasing, low-mode no-defect; construction pins "
     "(w9 PINNED_N, kz12 LATE counterexample, kz15 PINNED_Np1, "
     "chi3-w9 vacuous, scramble EARLY, live dictionary, dead "
     "chi3-15 still P1).  16/16 gates, "
     "final line POSTCAP STEPS VERIFIED", True),
    ("rh/problem/postcap_pivots.pdf", "problem_statement",
     "r377 companion",
     [],
     "compiled PDF of postcap_pivots.tex (recompiled artefact, "
     "registered unpinned)", False),
    ("rh/problem/compose_lemma.tex", "problem_statement",
     "r378 companion",
     [],
     "lemma-first attack on LEMMA.COMPOSE.01 (round 378): the "
     "slope chain M3 -> N3 -> N2 -> Fejer energy -> van der Corput "
     "-> H5 -> q_N<1 is rewritten as a pointwise inequality chain "
     "with explicit constants.  vdC at H=max(2,ceil sqrt m) is "
     "SATZ (v964-S0); pref <= sqrt(m)+1 SATZ; participation and "
     "Renyi SATZ; kernel envelope SATZ; T1-floor algebra SATZ "
     "conditional on 8/3 and C_K.  REDUCED to COMPOSE-: if "
     "S_F<=R0 D, L1<=Lambda, |Z_loc|<=Z0<M, M3<=phi(m) then "
     "|Z|<M (and q_N<1 given the r263 dictionary).  phi(m) = "
     "(M-Z0)^4 / (pref^2 R0^2 Lambda^4) with pref<=sqrt(m)+1, "
     "M=sqrt(5/7).  Pointwise H5-need with bounded L1,R0 is "
     "beta=1/2; the 0.888/0.908 convention is a slope-proxy for "
     "1/2+2 gamma.  H5/PairMarginLaw is a sister sufficient "
     "condition, not an extra vdC-route premise.  Log-complete "
     "m0: 10^25.81 (C_K=4.91) / 10^32.85 (C_K=23.70); r361 "
     "published 10^10.0/10^16.1 drop 2 log log m (ratios "
     "0.4517/0.5351 < 1).  Remaining lemmas: (R)(L)(Z)(T1)(V3') "
     "(Dict)(Head).  Finite identities plus named remainders; "
     "NO RH claim",
     True),
    ("rh/problem/verify_compose_lemma.py", "problem_check",
     "r378 companion",
     [],
     "machine check of every numbered lemma in compose_lemma.tex: "
     "standalone Fractions (Fejer identity, vdC covering+CS, "
     "H-rule pref, participation, Renyi, interpolation, kernel "
     "envelope, sigma* arithmetic, T1-floor algebra, log-complete "
     "m0, two-branch dictionary) plus construction pins (four w9 "
     "worlds; chi4 kz53 floor 3/8; 42-rung FRAME-A certificate "
     "qZ<1 42/42, F2-split 42/42, cheap triangle 35/42, exceptions "
     "(15,20,22,36,38,39,52), vdC-F2 38/42, H5-sister 21/42, min "
     "q-margin 0.0195; T1 implication 181/181 on 89 A + 8 B + "
     "42 chi3 + 42 chi4).  15/15 gates, "
     "final line COMPOSE LEMMA VERIFIED", True),
    ("rh/problem/compose_lemma.pdf", "problem_statement",
     "r378 companion",
     [],
     "compiled PDF of compose_lemma.tex (recompiled artefact, "
     "registered unpinned)", False),
    ("rh/problem/v3prime_proof.tex", "problem_statement",
     "r379 companion",
     [],
     "lemma-first attack on V3' (round 379): neither proved nor "
     "refuted in the construction.  Proved: cosine-grid mesh "
     "x=cos(2 pi k/L) with L=4h-2 (M=2h, L=2M-2); at the +x 20pct "
     "mask consecutive bulk nodes are equidistant in arccos "
     "(Delta-theta ratio 1 on 181 windows); equal weights on the "
     "occupied cosine nodes reproduce Chebyshev coefficients "
     "(g1=1/2, |gk-1/4|<1e-5 for k>=2); Fejer factor is Jacobi-(0,1) "
     "with |gn-1/4|=1/(4(2n+1)^2); two-period profiles about pi/2 "
     "with amplitude a<=0.85 lie in A_15 (a blocked rearrangement "
     "of the same extremes need not); coherent last-12 gamma scale "
     "1.5 stays in A_15, scale 2.0 leaves it (actual v2-violator at "
     "6.5-8).  Reduced to the coefficient box G_eps: last twelve "
     "|gk-1/4|<=1/16 and |log(g_{k+1}/gk)|<=2/5.  On the 181-window "
     "surface G_eps holds (max last-3 0.0375, last-12 0.0519, jump "
     "0.337) and V3' holds (0 remainder-violators).  Klein-gap and "
     "chi are not exceptions.  Chain T2' <= ... <= V2 <= V3' <= "
     "G_eps.  Finite identities plus a named reduction; NO RH claim",
     True),
    ("rh/problem/verify_v3prime.py", "problem_check",
     "r379 companion",
     [],
     "machine check of every numbered lemma in v3prime_proof.tex: "
     "L=4h-2 integer identity, Jacobi-(0,1) over Q, monic Chebyshev "
     "quarters, WKB band at x=3/5 eps=1/16, two-period A15 a<=0.85, "
     "constant pi/2, contrast block regression, interleave-vs-block; "
     "construction pins (Delta-theta ratio 1, G_eps, Path A 0 "
     "eta-violators, +x mask, equal-weight Chebyshev, coherent ray "
     "1.5 in / 2.0 out / 8 v2-viol, kz46 ratio 5.85 in A15, kz16 "
     "eta-111 regular).  17/17 gates, "
     "final line V3PRIME LEMMA VERIFIED", True),
    ("rh/problem/v3prime_proof.pdf", "problem_statement",
     "r379 companion",
     [],
     "compiled PDF of v3prime_proof.tex (recompiled artefact, "
     "registered unpinned)", False),
    ("rh/problem/g_eps_lemma.tex", "problem_statement",
     "r381 companion",
     [],
     "lemma-first attack on G_eps (round 381): first-order Jacobi "
     "perturbation SATZ; L^inf of d_arm too crude for the 1/16 box; "
     "jump not implied by the box (log(5/3)>2/5); second-order "
     "remainder not dominated.  Reduced to the pair (C_eps, R2): "
     "the explicit FO pairing against reference OP squares, and "
     "the Taylor remainder of the finite mu -> mu-nu (or "
     "Fejer-ref -> actual) step.  Scramble named-breaks last-12.  "
     "Finite identities plus a named reduction; NO RH claim",
     True),
    ("rh/problem/verify_g_eps.py", "problem_check",
     "r381 companion",
     [],
     "machine check of every numbered lemma in g_eps_lemma.tex: "
     "FO formula over Q, quadratic remainder Theta(eps^2), "
     "Jacobi-(0,1) over Q, jump comparison, Lambda(n)<=log n, "
     "Chebyshev quarters; construction pins (FO vs FD, G_eps and "
     "mu-only on FRAME-A w9, R2 midpoint ratio, scramble kill, "
     "L^inf crude, two-period vs block).  13/13 gates, "
     "final line G_EPS LEMMA VERIFIED", True),
    ("rh/problem/g_eps_lemma.pdf", "problem_statement",
     "r381 companion",
     [],
     "compiled PDF of g_eps_lemma.tex (recompiled artefact, "
     "registered unpinned)", False),
    ("rh/problem/pivot_entry_lemma.tex", "problem_statement",
     "r382 companion",
     [],
     "lemma-first attack on the pivot-band entry (round 382): "
     "RKHS sum, pair energy, Christoffel comparison SATZ; "
     "5-atom interlacing and 3-atom flank toys SATZ; equal "
     "two-period and clustered run-of-3 named kills.  Reduced "
     "to n0=floor(2N/5) under (F1)+(F2_{2/3}) (max nu-run <= 2 "
     "and nu-mass <= 2/3 flanking mu-mass).  MAIN F1 85/85, "
     "F2 85/85, F2_23 78/85; scramble named-breaks; two-period "
     "c=2/3 is the binding half-filling adversary.  Named "
     "remainder for n0=N-1: L2 CD tail on flank blocks.  "
     "Finite identities plus a named reduction; NO RH claim",
     True),
    ("rh/problem/verify_pivot_entry.py", "problem_check",
     "r382 companion",
     [],
     "machine check of every numbered lemma in "
     "pivot_entry_lemma.tex: standalone Fractions (energy "
     "identity, 5-atom interlacing, equal two-period H1=0, "
     "clustered H3<0, 3-atom flank, RKHS one-atom, Christoffel "
     "comparison, beta2 sign) plus construction pins (w9 "
     "flank entry n0=73, scramble kill first=21, dead chi3-15, "
     "two-period S=81 table, clustered S=21, lambda wall).  "
     "14/14 gates, final line PIVOT ENTRY STEPS VERIFIED", True),
    ("rh/problem/pivot_entry_lemma.pdf", "problem_statement",
     "r382 companion",
     [],
     "compiled PDF of pivot_entry_lemma.tex (recompiled "
     "artefact, registered unpinned)", False),
    ("rh/problem/compose_premises.tex", "problem_statement",
     "r383 companion",
     [],
     "lemma-first attack on the three COMPOSE- input premises "
     "(R)(L)(Z) (round 383): Fejer identity, r298 split, "
     "Z=Zloc+t_bulk, L2 identity, Lambda<=log, H-rule and phi "
     "SATZ.  Fold pairing as a live SATZ REFUTED (pair_w med "
     "0.512).  (R) REDUCED to census R0=4 (sup 2.917 at kz37; "
     "mutant R0/2=2 fails).  (L) REDUCED to Lambda=3 (max "
     "2.126); triangle gamma REFUTED; T1-combo E_pi REFUTED "
     "as a theorem (kz111 E_pi=52.276).  (Z) REDUCED on "
     "FRAME-A (Z0=4/5, 89/89) and REFUTED family-uniform on "
     "chi (6 windows).  Finite identities plus named "
     "reductions; NO RH claim",
     True),
    ("rh/problem/verify_compose_premises.py", "problem_check",
     "r383 companion",
     [],
     "machine check of every numbered lemma in "
     "compose_premises.tex: toys (period-2, DC mutant, CS, "
     "L2 identity, gamma=1/4 algebra, Lambda<=log), H-rule "
     "and phi, construction pins (w9, scramble M3-kill of "
     "(L), kz37 R-star, kz16 Z-star, kz111 E_pi spike).  "
     "16/16 gates, final line COMPOSE PREMISES VERIFIED", True),
    ("rh/problem/compose_premises.pdf", "problem_statement",
     "r383 companion",
     [],
     "compiled PDF of compose_premises.tex (recompiled "
     "artefact, registered unpinned)", False),
    ("rh/lean/RH/FlankEntry.lean", "lean_module",
     "r384",
     [],
     "r384 kernel-anchor of the r382 entry lemma: F1/F2c and "
     "named Prop FlankEntryPrefix on existing SignedAtoms; "
     "pair-energy identity, h0/h1, 3-atom flank and clustered "
     "H3=-28500 toys PROVED over Q; Christoffel k=0,1 PROVED; "
     "named Prop ChristoffelPivotBound for general k; bridge "
     "FlankEntryPrefix + adaptive_band_from_entry PROVED.  "
     "Zero sorry; census stays 5.  NO RH claim",
     True),
    ("rh/lean/RH/Selected.lean", "lean_module",
     "r397/r638L",
     [],
     "r397 exact selected domain: RealCanonicalWindow (R-fields, "
     "extends PrimeWindow) plus total construction W^R(a,m) = "
     "ExactFold(ExactPrimeSource, ExactArch, ExactBorder, "
     "ExactBudget); selected sequence a_k=2^k, "
     "m_k=k*2^floor(sqrt(k))-1 with Delta_k=2^{-r_k}*log 2, "
     "a_k->inf, Delta_k->0 PROVED; reduction "
     "weil_nonneg_of_selected_windows (plain fullRead along the "
     "sequence; consumes existing arch sorry); named mincut "
     "selected_augDualResolvent_gt_half.  lstar_canonical / "
     "terminal_q_canonical degraded to alternative route.  "
     "Zero sorry in this file; census stays 5.  r638L: arch "
     "contract is explicit; file remains sorry-free.  NO RH claim",
     True),
    ("rh/lean/RH/OneDefect.lean", "lean_module",
     "r406",
     [],
     "r406 general one-defect absorption as finite matrix algebra: "
     "indNeg_sub_rankOne_le_one (H PosDef => ind_-(H-ell ell^T)<=1), "
     "posDef_sub_rankOne_iff (rank-1 Schur), woodbury_inv, "
     "oneDefect_update_posDef_iff (H-ell ell^T+U J U^T PosDef iff "
     "0<Delta), posDef_of_contractive_lift, cMin_normSq / "
     "posDef_gram_sub_rankOne_iff PROVED.  Independent of "
     "source-side R404/R405.  Zero sorry; census stays 5.  "
     "NO RH claim",
     True),
    ("rh/lean/RH/EdgeBalance.lean", "lean_module",
     "r426",
     [],
     "r426 edge-balance chain as finite algebra: Woodbury-sch "
     "corollary of oneDefectDelta (sch=(den-1)-Delta at J=I; "
     "den=1 iff one-defect PosDef), 3x3 chart trichotomy "
     "(sch=phi-(eps_a a^2+eps_b b^2)), vacuous tau^2-separator "
     "(sch<0 iff tau^2>phi), den=1+gamma-v_t.s with "
     "den<2 iff gamma<1+v_t.s, gamma-bridge ||b||^2<=S<B_w.  "
     "Named Props BorderIsMuParseval / BorderLoewnerLeS / "
     "QNLtOne.  Zero sorry; census stays 5.  NO RH claim",
     True),
    ("rh/problem/christoffel_quiet.tex", "problem_statement",
     "r385 companion",
     [],
     "lemma-first attack on the common Christoffel-quietness "
     "core of G_eps and L* (round 385): T_k^2, TV, Chebyshev-Gauss "
     "and FO=gamma dQ SATZ; Chebyshev sampling of nu SATZ at "
     "trivial Weyl (Q^T<=2 alpha).  Geometric deduction to mu-OP "
     "Q_k from 3/8-floor + Koksma REFUTED as a closing bound "
     "(w9 last-12 Q=0.389 vs alpha=0.061; k D*=33.4).  Q<1 is "
     "not the floor plate (two-period c=2/3: Q==0.683 and "
     "lambda_max(E_22)>1).  Reduced to the pair (Delta, C).  "
     "Weyl scale trivial, not PNT/subconvex/RH-equivalent.  "
     "Finite identities plus a named reduction; NO RH claim",
     True),
    ("rh/problem/verify_christoffel_quiet.py", "problem_check",
     "r385 companion",
     [],
     "machine check of every numbered lemma in "
     "christoffel_quiet.tex: standalone Fractions/trig (T_k^2, "
     "TV=4k, trivial Weyl, Chebyshev-Gauss Q==1, one-Rayleigh "
     "h0(1-Q0)=2, two-period Q span 0) plus construction pins "
     "(w9 alpha/Q12/FO/D*, FO identity, Koksma failure, Weyl "
     "scale, scramble k_Q>=1, two-period lambda wall, EXT kz69 "
     "at depth 200).  13/13 gates, final line "
     "CHRISTOFFEL QUIET VERIFIED", True),
    ("rh/problem/christoffel_quiet.pdf", "problem_statement",
     "r385 companion",
     [],
     "compiled PDF of christoffel_quiet.tex (recompiled "
     "artefact, registered unpinned)", False),
    ("rh/problem/compose_premises2.tex", "problem_statement",
     "r386 companion",
     [],
     "lemma-first attack on living-ladder (Z') and cofinal R0 "
     "(round 386): death triangle SATZ; Fejer CS SATZ; w9 "
     "dictionary gated.  (Z') REDUCED to Z0'=21/25 on the "
     "living 175 (sup 0.833870 at CHI4 kz46; r383 4/5 fails).  "
     "Death channel |Z_loc|>=M iff q_N>1 CENSUS 181/181.  "
     "Finite-head Chebyshev and uniform-cancel*triangle "
     "REFUTED.  (R) REDUCED: MAIN/D<=3/10 census; CS+FAB does "
     "not prove O(polylog); named remainder "
     "B(omega+beta,omega+beta)<=K D.  Finite identities plus "
     "named reductions; NO RH claim",
     True),
    ("rh/problem/verify_compose_premises2.py", "problem_check",
     "r386 companion",
     [],
     "machine check of every numbered lemma in "
     "compose_premises2.tex: toys (DC C_MAIN-kill, period-2, "
     "CS, death triangle, Z0' vs M), H-rule extras, "
     "construction pins (w9 dict, scramble non-break, kz37 "
     "grams, living CHI4-46, dead CHI3-15, 4/5 mutant).  "
     "16/16 gates, final line COMPOSE PREMISES2 VERIFIED", True),
    ("rh/problem/compose_premises2.pdf", "problem_statement",
     "r386 companion",
     [],
     "compiled PDF of compose_premises2.tex (recompiled "
     "artefact, registered unpinned)", False),
    ("rh/problem/coherence_assist.tex", "problem_statement",
     "r387 companion",
     [],
     "lemma-first attack on the coherence-assist remainder of L* "
     "after r385 (round 387): Chebyshev-Dirichlet CD, bookkeeping "
     "and Gershgorin SATZ; cosine mesh SATZ; two-period = global "
     "AP SATZ.  Geometric deduction to assist <= (1-Q)/Q from "
     "3/8-separation + Gershgorin REFUTED as a closing bound "
     "(w9 k_gersh=21 << n0=73; k_g/N <= 0.114 on core-42).  "
     "Named property rho_AP < 1/5 kills the two-period and holds "
     "on EXT-heavy 7.  Reduced to the signed mu-CD off-diagonal.  "
     "Finite identities plus a named reduction; NO RH claim",
     True),
    ("rh/problem/verify_coherence_assist.py", "problem_check",
     "r387 companion",
     [],
     "machine check of every numbered lemma in "
     "coherence_assist.tex: standalone (Chebyshev-Dirichlet CD, "
     "2x2 bookkeeping/Gershgorin, two-period AP, mesh, "
     "1/3<3/8) plus construction pins (w9 k_gersh/wall/AP, "
     "Dirichlet max-row, two-period lambda, scramble, c=1, "
     "clustered run-3).  13/13 gates, final line "
     "COHERENCE ASSIST VERIFIED", True),
    ("rh/problem/coherence_assist.pdf", "problem_statement",
     "r387 companion",
     [],
     "compiled PDF of coherence_assist.tex (recompiled "
     "artefact, registered unpinned)", False),
    ("rh/problem/delta_deformation.tex", "problem_statement",
     "r388 companion",
     [],
     "lemma-first attack on the Delta-deformation closing of "
     "C_eps after r381/r385 (round 388): FO-split and "
     "homogeneity SATZ; Fejer-pure two-period SATZ.  "
     "Osc-Geronimus as a closing bound REFUTED (C*=0.0056 "
     "majorant 0.191>1/32; scramble smaller osc, dDelta 1e6).  "
     "R2 on the mu-reference NOT dominated (|quad|/|lin|=0.861 "
     "at n=40, 0.640 at full; |R2|/|FO|=4.19).  Reduced to the "
     "r381 triple G_eps^mu ^ C_eps ^ R2.  Finite identities "
     "plus a named reduction; NO RH claim",
     True),
    ("rh/problem/verify_delta_deformation.py", "problem_check",
     "r388 companion",
     [],
     "machine check of every numbered lemma in "
     "delta_deformation.tex: standalone Fractions/trig "
     "(gamma homogeneous, one-Rayleigh, Fejer-pure S=21, "
     "Neumann bar, Chebyshev-Gauss, split toy) plus "
     "construction pins (w9 Delta/FO/eps, split residual, "
     "R2 mu and Fejer n=40, C x 2 mutant, scramble kill, "
     "two-period control).  13/13 gates, final line "
     "DELTA DEFORMATION VERIFIED", True),
    ("rh/problem/delta_deformation.pdf", "problem_statement",
     "r388 companion",
     [],
     "compiled PDF of delta_deformation.tex (recompiled "
     "artefact, registered unpinned)", False),
    ("rh/problem/weyl_energy.tex", "problem_statement",
     "r389 companion",
     [],
     "lemma-first attack on the Weyl energy of cancellation "
     "after four majorant routes died (round 389): Chebyshev "
     "energy, off=Phi-diag, Q^T as C_{2k} ratio, pi_k^2 Weyl "
     "and finite-grid Parseval SATZ.  MAIN/chi at quadratic-mean; "
     "two-period is a spectral comb (rho_AP=1).  FO^T closes "
     "C_eps at QM; assist is not the Chebyshev all-ones energy; "
     "Z_loc is not the Chebyshev x T_k^2 proxy.  Reduced to the "
     "mu-OP Chebyshev-coefficient Gram.  Finite identities plus "
     "a named reduction; NO RH claim",
     True),
    ("rh/problem/verify_weyl_energy.py", "problem_check",
     "r389 companion",
     [],
     "machine check of every numbered lemma in "
     "weyl_energy.tex: standalone Fractions/trig/Parseval "
     "(energy, off=Phi-diag, mutants, Q^T, S=21 Parseval) plus "
     "construction pins (w9 energy/Parseval/QM/FO, wall assist, "
     "two-period comb, scramble QM).  14/14 gates, final line "
     "WEYL ENERGY VERIFIED", True),
    ("rh/problem/weyl_energy.pdf", "problem_statement",
     "r389 companion",
     [],
     "compiled PDF of weyl_energy.tex (recompiled "
     "artefact, registered unpinned)", False),
    ("rh/problem/g_eps_mu.tex", "problem_statement",
     "r390 companion",
     [],
     "lemma-first attack on G_eps^mu after r381/r388 "
     "(round 390): Jacobi-(0,1) and Chebyshev-U SATZ; "
     "full-grid Fejer Bernstein-Szego SATZ.  Occupied-Fejer "
     "already in |g-1/4|; signed-Fejer 0.071 is C_eps.  "
     "Ratio bound kappa=4200 useless.  Permutation kill: "
     "NOT construction-pure.  Reduced to F_eps "
     "(Fejer-on-occupied) ^ W_eps (digamma/tent multiplier).  "
     "Finite identities plus a named reduction; NO RH claim",
     True),
    ("rh/problem/verify_g_eps_mu.py", "problem_check",
     "r390 companion",
     [],
     "machine check of every numbered lemma in "
     "g_eps_mu.tex: standalone Fractions (Jacobi-(0,1), "
     "Chebyshev-U, homogeneity, jump, small full-grid, "
     "ratio-bound toy) plus construction pins (w9 mu/"
     "Fejer-occ/signed-Fejer, full-grid residual, kappa, "
     "perm kill, scramble-seed mu, two-period weight).  "
     "13/13 gates, final line G_EPS_MU LEMMA VERIFIED", True),
    ("rh/problem/g_eps_mu.pdf", "problem_statement",
     "r390 companion",
     [],
     "compiled PDF of g_eps_mu.tex (recompiled "
     "artefact, registered unpinned)", False),
    ("rh/problem/construction_rl.tex", "problem_statement",
     "r391 companion",
     [],
     "lemma-first attack on construction-pure (R) and (L) "
     "(round 391): Euclidean split and eta identity SATZ; "
     "CS counting L1^2 <= m D SATZ; Fejer Gram SATZ.  "
     "Block-Gershgorin REFUTED.  (R) reduced to the "
     "white-block class with census K=4; (L) reduced to "
     "slope +0.202 construction-class.  Finite identities "
     "plus named reductions; NO RH claim",
     True),
    ("rh/problem/verify_construction_rl.py", "problem_check",
     "r391 companion",
     [],
     "machine check of every numbered lemma in "
     "construction_rl.tex: standalone Fractions (CS counting, "
     "eta split, K vs K/2) plus construction pins (w9 "
     "white-block, scramble non-break, kz37, weight-rand, "
     "DC/align/merge mutants).  17/17 gates, final line "
     "CONSTRUCTION PURE RL VERIFIED", True),
    ("rh/problem/construction_rl.pdf", "problem_statement",
     "r391 companion",
     [],
     "compiled PDF of construction_rl.tex (recompiled "
     "artefact, registered unpinned)", False),
    ("rh/problem/deletion_transform.tex", "problem_statement",
     "r392 companion",
     [],
     "lemma-first attack on the deletion algebra of occupied "
     "Fejer after r389/r390 (round 392): Uvarov gamma-ratio "
     "SATZ; Bernstein-Szego specialisation SATZ; w9 identity "
     "9e-15.  F_eps from rho_AP<1/5 REFUTED as a closing "
     "deduction (AP deletion stays IN; clustered run>=3 kills; "
     "kz55 jump 0.3942 is census).  Assist/dDelta are exact "
     "Uvarov readouts; cancellation sits in signs of K^mu[Xi].  "
     "Reduced to d2 log tau under F1, and Sign-Schur.  Finite "
     "identities plus a named reduction; NO RH claim",
     True),
    ("rh/problem/verify_deletion_transform.py", "problem_check",
     "r392 companion",
     [],
     "machine check of every numbered lemma in "
     "deletion_transform.tex: standalone Fractions (one-point "
     "and block Uvarov, S=5/7/9, Chebyshev-U, jump, tau_0=1) "
     "plus construction pins (w9 identity, Assist, dDelta, "
     "Fejer-not-Assist, AP in / clustered out, scramble "
     "seed=3).  14/14 gates, final line "
     "DELETION TRANSFORM VERIFIED", True),
    ("rh/problem/deletion_transform.pdf", "problem_statement",
     "r392 companion",
     [],
     "compiled PDF of deletion_transform.tex (recompiled "
     "artefact, registered unpinned)", False),
    ("rh/problem/tau_field.tex", "problem_statement",
     "r393 companion",
     [],
     "lemma-first attack on d2 log tau under F1 after r392 "
     "(round 393): 1x1/2x2 tau SATZ; cluster decomp SATZ; "
     "rank-1 locality SATZ (d2 = Delta log rho).  F1 necessary "
     "(run-3 3x3 kills) and not sufficient (random F1 half-fill "
     "leaves JUMP').  Coupling ~31% load-bearing; L1 triangle "
     "does not close.  JUMP'=0.45 legal V3' air, still census.  "
     "Reduced to L*-occupation regularity.  Finite identities "
     "plus a named reduction; NO RH claim",
     True),
    ("rh/problem/verify_tau_field.py", "problem_check",
     "r393 companion",
     [],
     "machine check of every numbered lemma in "
     "tau_field.tex: standalone Fractions (1x1 SM, 2x2, kappa, "
     "tau_0=1, JUMP air) plus construction pins (w9 F1 split, "
     "rank-1, decomp, coupling, AP in / run-3 out, scramble "
     "F1-break, coupling mutant).  13/13 gates, final line "
     "TAU FIELD VERIFIED", True),
    ("rh/problem/tau_field.pdf", "problem_statement",
     "r393 companion",
     [],
     "compiled PDF of tau_field.tex (recompiled "
     "artefact, registered unpinned)", False),
    ("rh/problem/sign_schur.tex", "problem_statement",
     "r394 companion",
     [],
     "lemma-first attack on the sign binding of the Uvarov "
     "image K^mu[Xi] after r392 (round 394): Dirichlet zonal "
     "signs and envelope SATZ; 2x2 Z-matrix bound FALSE.  "
     "Checkerboard / rank-1 conjugability REFUTED (mass-weighted "
     "agree 1/2).  Mass-weighted Chebyshev inheritance is census "
     "81-89%, not a SATZ.  No source-defined k*>2N/5.  Reduced "
     "to the Weyl energy of the mu-OP Gram (r389 rest).  Finite "
     "identities plus a named reduction; NO RH claim",
     True),
    ("rh/problem/verify_sign_schur.py", "problem_check",
     "r394 companion",
     [],
     "machine check of every numbered lemma in "
     "sign_schur.tex: standalone (Dirichlet sign/envelope, "
     "Chebyshev-CD, 2x2 Z-matrix, bookkeeping, checkerboard "
     "rank-1, mesh step) plus construction pins (w9 Assist, "
     "Cheb/CB mass-agree, |E| mutant, two-period in-phase and "
     "too-late anti-CB, scramble envelope).  14/14 gates, "
     "final line SIGN SCHUR VERIFIED", True),
    ("rh/problem/sign_schur.pdf", "problem_statement",
     "r394 companion",
     [],
     "compiled PDF of sign_schur.tex (recompiled "
     "artefact, registered unpinned)", False),
    ("rh/problem/three_gap_mask.tex", "problem_statement",
     "r395 companion",
     [],
     "lemma-first attack on the three-gap structure of the "
     "fold nu-mask after r393/r394 (round 395): Steinhaus on "
     "Z/q SATZ; PNT-free integer-log local 3-gap SATZ for "
     "n>=512.  REFUTED: the nu-mask is globally/blockwise "
     "3-gap; nuniq<=3 implies the d2 log tau box.  3/8-floor "
     "and MED-CAP 8/3 are not mask-spectrum shadows.  Finite "
     "identities plus a named refutation; NO RH claim",
     True),
    ("rh/problem/verify_three_gap_mask.py", "problem_check",
     "r395 companion",
     [],
     "machine check of every numbered lemma in "
     "three_gap_mask.tex: standalone (Steinhaus Z/q, additive "
     "a+b=c, thinning, log-local, small-n census, 3/8 and 8/3 "
     "shadows) plus construction pins (w9 nuniq=12, slide "
     "partial, discriminator, scramble, Assist split).  11/11 "
     "gates, final line THREE GAP MASK VERIFIED", True),
    ("rh/problem/three_gap_mask.pdf", "problem_statement",
     "r395 companion",
     [],
     "compiled PDF of three_gap_mask.tex (recompiled "
     "artefact, registered unpinned)", False),
    ("rh/problem/isolation_lemma.tex", "problem_statement",
     "r396 companion",
     [],
     "lemma-first attack on isolation / pair density of the "
     "fold nu-mask after r395 (round 396): folded small integers "
     "not adjacent SATZ; packing O(n_atom) not smallness.  "
     "REFUTED: P/n_nu -> 0 or P constant; isolated => box; "
     "isolated => lambda<1; isolation + hull => Gershgorin<1.  "
     "Finite identities plus a named refutation; NO RH claim",
     True),
    ("rh/problem/verify_isolation_lemma.py", "problem_check",
     "r396 companion",
     [],
     "machine check of every numbered lemma in "
     "isolation_lemma.tex: standalone (w9 two pairs, folded "
     "small integers, packing, wrap234 isolated, hull >>1) "
     "plus construction pins (h=40 not uniform IN, pair-rich "
     "OUT, 1010 lambda>1 and Gershgorin open, two-period/"
     "scramble, injection and fattail).  10/10 gates, "
     "final line ISOLATION LEMMA VERIFIED", True),
    ("rh/problem/isolation_lemma.pdf", "problem_statement",
     "r396 companion",
     [],
     "compiled PDF of isolation_lemma.tex (recompiled "
     "artefact, registered unpinned)", False),
    ("rh/problem/high_moment_inertia.tex", "problem_statement",
     "r398 companion",
     [],
     "lemma-first kill-test of P1 via a fixed even cycle-moment "
     "of R_{N-3} after DCCLXII (round 398): pointwise bound SATZ; "
     "cycle-sum SATZ on a toy.  KILL_FAIL: no d in {2,3,4,6,8} "
     "gives 2^{2d} tr((I-R)^{2d}) < 2 with growing reserve.  Cause "
     "is a cluster of eigenvalues at 1/2.  Finite identities plus "
     "a named kill-test; NO RH claim",
     True),
    ("rh/problem/verify_high_moment.py", "problem_check",
     "r398 companion",
     [],
     "machine check of every numbered lemma in "
     "high_moment_inertia.tex: standalone (Fractions bound, "
     "nopref, odd mutant, 2x2 cycle-sum, frozen d-set, 3x3 "
     "walk-sum) plus construction pins (w9 contraction/FTI, "
     "moments, scramble nneg=21, two-period, dead chi, living "
     "chi3 nneg=0).  12/12 gates, final line HIGH MOMENT VERIFIED",
     True),
    ("rh/problem/high_moment_inertia.pdf", "problem_statement",
     "r398 companion",
     [],
     "compiled PDF of high_moment_inertia.tex (recompiled "
     "artefact, registered unpinned)", False),
    ("rh/problem/source_weyl_energy.tex", "problem_statement",
     "r399 companion",
     [],
     "lemma-first attack on the source-pure Weyl energy of the "
     "centered mass difference after DCCLXII 5.2/5.3 (round 399): "
     "Dirichlet interpolant SATZ; Fejer Laplacian SATZ; CD-transfer "
     "norm named.  REFUTED: E^bulk -> 0; sits at quadratic-mean and "
     "grows.  Honesty gate: unconditional MVT fails, a closing bound "
     "would be RH-near (circular).  Finite identities plus a named "
     "refutation; NO RH claim",
     True),
    ("rh/problem/verify_source_weyl.py", "problem_check",
     "r399 companion",
     [],
     "machine check of every numbered lemma in "
     "source_weyl_energy.tex: standalone (Fractions stencil, "
     "Laplacian convolution, energy-path firewall) plus construction "
     "pins (w9 representation/Laplacian/C0=C1=0/E-pin, kz18/kz52 "
     "Dirichlet, scramble, two-period, dead/living chi, selected "
     "k=4<k=6, MVT ratio).  11/11 gates, final line SOURCE WEYL "
     "VERIFIED", True),
    ("rh/problem/source_weyl_energy.pdf", "problem_statement",
     "r399 companion",
     [],
     "compiled PDF of source_weyl_energy.tex (recompiled "
     "artefact, registered unpinned)", False),
    ("rh/problem/bulk_one_defect.tex", "problem_statement",
     "r400 companion",
     [],
     "lemma-first threshold/phase form of the frame inequality "
     "after DCCLXII 5.4 and the r399 circularity verdict "
     "(round 400): frame implication SATZ; rank-r interlacing "
     "SATZ; Weyl SATZ.  FORM_T REFUTED as rank-1 (BS dual on Y "
     "has 49 negatives; MAIN kills 48).  FORM_P REFUTED (C_m "
     "phases do not track ind_-).  Dead chi satisfy P1 (death "
     "is edge).  Finite identities plus a named census; NO RH claim",
     True),
    ("rh/problem/verify_bulk_one_defect.py", "problem_check",
     "r400 companion",
     [],
     "machine check of every numbered lemma in "
     "bulk_one_defect.tex: standalone (Fractions frame, "
     "omit-ell, rank-1 interlacing, Weyl, threshold x2) plus "
     "construction pins (w9 lift rank/orthogonality/source-frame "
     "failure, scramble nneg=21, two-period, dead/living chi, "
     "phase-blindness).  12/12 gates, final line "
     "BULK ONE DEFECT VERIFIED", True),
    ("rh/problem/bulk_one_defect.pdf", "problem_statement",
     "r400 companion",
     [],
     "compiled PDF of bulk_one_defect.tex (recompiled "
     "artefact, registered unpinned)", False),
    ("rh/problem/edge_signature.tex", "problem_statement",
     "r401 companion",
     [],
     "lemma-first 3x3 edge signature after DCCLXII 5.5 (round 401): "
     "reconstruction SATZ; model lemma SATZ on both charts.  "
     "CENSUS: living worlds land in compact K with g*>0; dead chi "
     "leave by sch>0.  Cofinal K not proved.  Finite identities plus "
     "a named census; NO RH claim",
     True),
    ("rh/problem/verify_edge_signature.py", "problem_check",
     "r401 companion",
     [],
     "machine check of every numbered lemma in "
     "edge_signature.tex: standalone (Fractions mixed form, "
     "mixed Haynsworth, both charts at the origin, det=1, "
     "drop-border, 64-pt disk) plus construction pins (w9 shift "
     "and reconstruction, dead chi3-15, scramble nneg=21, "
     "two-period, living chi3-9).  13/13 gates, "
     "final line EDGE SIGNATURE VERIFIED", True),
    ("rh/problem/edge_signature.pdf", "problem_statement",
     "r401 companion",
     [],
     "compiled PDF of edge_signature.tex (recompiled "
     "artefact, registered unpinned)", False),
    ("rh/problem/p1_construction.tex", "problem_statement",
     "r403 companion",
     [],
     "lemma-first P1 construction class after DCCLXVII and r400 "
     "(round 403): interlacing SATZ; incomplete PSD lift SATZ; "
     "scale invariance SATZ.  P1_CONSTRUCTION_REFUTED (fixed-mask "
     "weight-rand kills P1; invariant is the von Mangoldt "
     "assignment, not the fold mask).  Finite identities plus a "
     "named census; NO RH claim",
     True),
    ("rh/problem/verify_p1_construction.py", "problem_check",
     "r403 companion",
     [],
     "machine check of every numbered lemma in "
     "p1_construction.tex: standalone (rank-1 interlacing, "
     "PSD-incomplete, threshold 1/2) plus construction pins "
     "(w9 Gram/omit/scale, permute, rademacher, mild 1e-4, "
     "scramble, two-period, dead chi weights vs perm).  "
     "11/11 gates, final line P1 CONSTRUCTION VERIFIED", True),
    ("rh/problem/p1_construction.pdf", "problem_statement",
     "r403 companion",
     [],
     "compiled PDF of p1_construction.tex (recompiled "
     "artefact, registered unpinned)", False),
    ("rh/problem/one_defect_gram.tex", "problem_statement",
     "r404 companion",
     [],
     "lemma-first source one-defect Gram after DCCLXIX and r403 "
     "(round 404): Chebyshev addition SATZ; Cauchy kernel SATZ; "
     "Loewner identity SATZ; fold-linear SATZ; Q^T A0 Q PD SATZ.  "
     "CHOLESKY_TAUTOLOGY / SOURCE_GRAM_NOT_EXACT (class 3 not "
     "reached; Euler/Digamma/Uvarov residuals O(1); analytic "
     "Fourier subset does not recover Vn; ones-mode is not the "
     "null mode).  Finite identities plus a named class audit; "
     "NO RH claim",
     True),
    ("rh/problem/verify_one_defect_gram.py", "problem_check",
     "r404 companion",
     [],
     "machine check of every numbered lemma in "
     "one_defect_gram.tex: standalone (Chebyshev addition, "
     "Cauchy kernel, Loewner psi-nsum, lag-linearity) plus "
     "construction pins (w9 PD compression, Fourier subset, "
     "Euler/Loewner residuals, only-Gram/cross, Cholesky "
     "tautology vs permute, ones-mode, Lambda-perm mutant).  "
     "11/11 gates, final line ONE DEFECT GRAM VERIFIED", True),
    ("rh/problem/one_defect_gram.pdf", "problem_statement",
     "r404 companion",
     [],
     "compiled PDF of one_defect_gram.tex (recompiled "
     "artefact, registered unpinned)", False),
    ("rh/problem/edge_contractive_lift.tex", "problem_statement",
     "r405 companion",
     [],
     "lemma-first edge contractive lift after DCCLXIX secs. 8 "
     "and 12 (round 405): Euler tail SATZ; disk Parseval SATZ; "
     "Woodbury-Schur kappa_closed SATZ; Cauchy Gram SATZ.  "
     "EDGE_LIFT_PARTIAL (ones-lift residual 0; border=tail "
     "REFUTED; dead overflow REFUTED; kappa not a function of "
     "(a,b) alone; A0-defect c OPEN).  Finite identities plus "
     "a named census; NO RH claim",
     True),
    ("rh/problem/verify_edge_lift.py", "problem_check",
     "r405 companion",
     [],
     "machine check of every numbered lemma in "
     "edge_contractive_lift.tex: standalone (Euler tail, "
     "omit-tail, disk Parseval, Woodbury kappa_closed, Cauchy "
     "Gram, wrong-sign J) plus construction pins (w9 geometric "
     "ones residual, ones-split Delta/c2/kappa, border vs tail, "
     "dead/live chi3, scramble/permute).  12/12 gates, "
     "final line EDGE LIFT VERIFIED", True),
    ("rh/problem/edge_contractive_lift.pdf", "problem_statement",
     "r405 companion",
     [],
     "compiled PDF of edge_contractive_lift.tex (recompiled "
     "artefact, registered unpinned)", False),
    ("rh/problem/dual_intertwiner.tex", "problem_statement",
     "r407 companion",
     [],
     "lemma-first dual intertwiner after DCCLXXI/DCCLXXII "
     "and r404/r405 (round 407): Hankel/Woodbury/FL SATZ; "
     "R=C(I+C)^{-1} SATZ; Euler moment SOURCE_GRAM_EXACT on "
     "the moment layer.  INTERTWINER_EXACT / NU_RANK_NOT_ONE "
     "(P1 REDUZIERT to lam_2(C)>=1; nu-rank = N_nu; sandwich "
     "wrong direction; Euler source G is not the G that R "
     "inverts).  Finite identities plus a named reduction; "
     "NO RH claim",
     True),
    ("rh/problem/verify_dual_intertwiner.py", "problem_check",
     "r407 companion",
     [],
     "machine check of every numbered lemma in "
     "dual_intertwiner.tex: standalone (Hankel linearity, "
     "Euler split, Woodbury, R=C(I+C)^{-1}, inverse antitone, "
     "FL dictionary) plus construction pins (w9 formula/FL/C, "
     "Euler moment vs dual G, nu-rank/sandwich, scramble/"
     "permute/dead chi, kz9+kz55).  12/12 gates, "
     "final line DUAL INTERTWINER VERIFIED", True),
    ("rh/problem/dual_intertwiner.pdf", "problem_statement",
     "r407 companion",
     [],
     "compiled PDF of dual_intertwiner.tex (recompiled "
     "artefact, registered unpinned)", False),
    ("rh/problem/c_threshold.tex", "problem_statement",
     "r408 companion",
     [],
     "lemma-first C-threshold / sampling after r407 "
     "(round 408): 2x2 coherence / Rayleigh / rank / Cauchy "
     "SATZ; Nyquist-at-density-1/2 REFUTED; source nC<=1 "
     "CENSUS.  NYQUIST_REFUTED / AT_MOST_ONE_CENSUS.  "
     "Finite identities plus a named refutation and a named "
     "census; NO RH claim",
     True),
    ("rh/problem/verify_c_threshold.py", "problem_check",
     "r408 companion",
     [],
     "machine check of every numbered lemma in "
     "c_threshold.tex: standalone (2x2 coherence, Rayleigh, "
     "rank deficiency, Cauchy) plus construction pins (w9 "
     "anatomy, C=BB^T and 1010 zeros, scramble/permute, "
     "thin/densify/Cauchy, chi + kz55).  9/9 gates, "
     "final line C THRESHOLD VERIFIED", True),
    ("rh/problem/c_threshold.pdf", "problem_statement",
     "r408 companion",
     [],
     "compiled PDF of c_threshold.tex (recompiled "
     "artefact, registered unpinned)", False),
    ("rh/problem/borodin_birkhoff_intertwiner.tex", "problem_statement",
     "r409 companion",
     [],
     "lemma-first Borodin-Birkhoff intertwiner after r407 "
     "(round 409): source-pure min-norm CLS graph identity "
     "SATZ; Phi_N literal Theta=C^T Phi C REFUTED; Krein "
     "unfitted REFUTED; SEQ n_neg^inn<=1 CENSUS.  "
     "ONE_DEFECT_TRANSPORT_CENSUS.  Finite identities plus "
     "named refutations and a named census; NO RH claim",
     True),
    ("rh/problem/verify_borodin_birkhoff.py", "problem_check",
     "r409 companion",
     [],
     "machine check of every numbered lemma in "
     "borodin_birkhoff_intertwiner.tex: standalone (three "
     "bases, graph=CD, Woodbury, two mutants) plus "
     "construction pins (w9 graph/inertia/SEQ, Pi_K=0 and "
     "Euler-direct, scramble/permute/jitter, Phi/Krein miss, "
     "T^dagger vs r362, dead chi).  11/11 gates, "
     "final line BORODIN BIRKHOFF VERIFIED", True),
    ("rh/problem/borodin_birkhoff_intertwiner.pdf", "problem_statement",
     "r409 companion",
     [],
     "compiled PDF of borodin_birkhoff_intertwiner.tex "
     "(recompiled artefact, registered unpinned)", False),
    ("rh/problem/hole_nyquist.tex", "problem_statement",
     "r410 companion",
     [],
     "lemma-first hole-Nyquist defect after r407/r408/r409 "
     "(round 410): RK/degree/C_ii/Rayleigh SATZ; Y-Lagrange "
     "test-poly REFUTED; Fourier-block REFUTED; Bernstein "
     "REFUTED; d_i>=1 CENSUS; sequential birth REDUCED.  "
     "TESTPOLY_REFUTED / DMIN_CENSUS + FOURIER_REFUTED / "
     "BERNSTEIN_REFUTED / SEQ_REDUCED.  Finite identities "
     "plus named refutations; NO RH claim",
     True),
    ("rh/problem/verify_hole_nyquist.py", "problem_check",
     "r410 companion",
     [],
     "machine check of every numbered lemma in "
     "hole_nyquist.tex: standalone (RK, degree, C_ii, "
     "Rayleigh) plus construction pins (Y-Lagrange, "
     "cheb-CD/dmin, scramble/permute K-collapse, "
     "Fourier/sequential, chi/1010/kz55).  9/9 gates, "
     "final line HOLE NYQUIST VERIFIED", True),
    ("rh/problem/hole_nyquist.pdf", "problem_statement",
     "r410 companion",
     [],
     "compiled PDF of hole_nyquist.tex (recompiled "
     "artefact, registered unpinned)", False),
    ("rh/problem/threshold_identity.tex", "problem_statement",
     "r411 companion",
     [],
     "lemma-first threshold identity / energy split after "
     "r409 (round 411): ||T0||=1/sqrt(lam_min(C)) SATZ; "
     "energy split on K0^perp SATZ; exact ||T0||=1 on PD "
     "REFUTED; k=37 as Christoffel hole REFUTED.  "
     "ENERGY_SPLIT_EXACT / SATURATION_REFUTED.  Finite "
     "identities plus a named refutation; NO RH claim",
     True),
    ("rh/problem/verify_threshold_identity.py", "problem_check",
     "r411 companion",
     [],
     "machine check of every numbered lemma in "
     "threshold_identity.tex: standalone (T*T=Cinv, kernel, "
     "projection, two mutants) plus construction pins (w9 "
     "dictionary/Fourier miss, kz42 gap, k=36/37, "
     "permute/scramble/1010, chi).  9/9 gates, "
     "final line THRESHOLD IDENTITY VERIFIED", True),
    ("rh/problem/threshold_identity.pdf", "problem_statement",
     "r411 companion",
     [],
     "compiled PDF of threshold_identity.tex "
     "(recompiled artefact, registered unpinned)", False),
    ("rh/problem/hole_top_mode.tex", "problem_statement",
     "r413 companion",
     [],
     "lemma-first hole top mode after DCCLXXIX (round 413): "
     "Lagrange/OP formula SATZ over Q; v_top source-pure; "
     "HTM primary test REFUTED on MAIN; QD REFUTED for "
     "p==1; dead-chi-hold REFUTED.  TOP_MODE_REFUTED.  "
     "Finite identities plus a named refutation; NO RH claim",
     True),
    ("rh/problem/verify_hole_top_mode.py", "problem_check",
     "r413 companion",
     [],
     "machine check of every numbered lemma in "
     "hole_top_mode.tex: standalone (Lagrange, GS formula, "
     "constructor audit, toy HTM) plus construction pins "
     "(w9 corr/primary fail, leftover+QD mass, "
     "permute/scramble/unsigned P', chi, core-42 P1).  "
     "9/9 gates, final line HOLE TOP MODE VERIFIED", True),
    ("rh/problem/hole_top_mode.pdf", "problem_statement",
     "r413 companion",
     [],
     "compiled PDF of hole_top_mode.tex "
     "(recompiled artefact, registered unpinned)", False),
    ("rh/problem/top_mode_edge.tex", "problem_statement",
     "r415 companion",
     [],
     "lemma-first top-mode edge after DCCLXXIX (round 415): "
     "Woodbury-Schur -sch=beta-alpha SATZ; v_top is not the "
     "T0/A0 defect; Euler on v_top is constant content.  "
     "CHART_IDENTITY_EXACT / TOP_MODE_NOT_DEFECT.  Finite "
     "identities plus named refutations; NO RH claim",
     True),
    ("rh/problem/verify_top_mode_edge.py", "problem_check",
     "r415 companion",
     [],
     "machine check of every numbered lemma in "
     "top_mode_edge.tex: standalone (Euler tail, disk "
     "Parseval, alpha/beta over Q) plus construction pins "
     "(w9 Euler vs alpha_T, v_top vs SV, chart identity + "
     "ones=r405, chi sign, permute/scramble/omega, MAIN-18 "
     "/ K2 mixed).  9/9 gates, final line TOP MODE EDGE "
     "VERIFIED", True),
    ("rh/problem/top_mode_edge.pdf", "problem_statement",
     "r415 companion",
     [],
     "compiled PDF of top_mode_edge.tex "
     "(recompiled artefact, registered unpinned)", False),
    ("rh/problem/debranges_index.tex", "problem_statement",
     "r416 companion",
     [],
     "lemma-first de Branges / Potapov index after "
     "DCCLXXIX path B (round 416): HB interlacing SATZ; "
     "Wronskian over Q; phase dominance with kappa<=1 "
     "REFUTED on MAIN (yyA=3).  PHASE_DOMINANCE_REFUTED / "
     "HB_CENSUS.  Finite identities plus a named "
     "refutation; NO RH claim",
     True),
    ("rh/problem/verify_debranges_index.py", "problem_check",
     "r416 companion",
     [],
     "machine check of every numbered lemma in "
     "debranges_index.tex: standalone (Wronskian, disc, "
     "constructor audit, toy HB) plus construction pins "
     "(w9 balance/HB/Herglotz, yyA=3 primary fail, "
     "permute/scramble, MAIN-42 + chi).  9/9 gates, "
     "final line DEBRANGES INDEX VERIFIED", True),
    ("rh/problem/debranges_index.pdf", "problem_statement",
     "r416 companion",
     [],
     "compiled PDF of debranges_index.tex "
     "(recompiled artefact, registered unpinned)", False),
    ("rh/problem/source_sch_sign.tex", "problem_statement",
     "r417 companion",
     [],
     "lemma-first source Schur sign after DCCLXXXIII "
     "(round 417): Woodbury and Sylvester-chart formulae "
     "SATZ; tau->0 census; rate not source-derived.  "
     "CHART_SCH_EXACT / LIMIT_CENSUS / RATE_OPEN.  "
     "Finite identities plus a named census; NO RH claim",
     True),
    ("rh/problem/verify_source_sch.py", "problem_check",
     "r417 companion",
     [],
     "machine check of every numbered lemma in "
     "source_sch_sign.tex: standalone (Woodbury/chart "
     "over Q, sign-map grids, drop-border) plus "
     "construction pins (w9 identity+pivot, dead chi, "
     "scramble/two-period, MAIN-42 + EXT-119).  10/10 "
     "gates, final line SOURCE SCH SIGN VERIFIED", True),
    ("rh/problem/source_sch_sign.pdf", "problem_statement",
     "r417 companion",
     [],
     "compiled PDF of source_sch_sign.tex "
     "(recompiled artefact, registered unpinned)", False),
    ("rh/problem/phi_bb_sign.tex", "problem_statement",
     "r418 companion",
     [],
     "lemma-first border-border sign after DCCLXXXIV "
     "(round 418): phibb = c_J + Sigma SATZ; uniform "
     "phibb<0 REFUTED on the named census; pole-"
     "dominance REFUTED on living P1.  SPLIT_EXACT / "
     "UNIFORM_REFUTED / POLE_NOT_DOMINANT.  Finite "
     "identities plus a named refutation; NO RH claim",
     True),
    ("rh/problem/verify_phi_bb.py", "problem_check",
     "r418 companion",
     [],
     "machine check of every numbered lemma in "
     "phi_bb_sign.tex: standalone (Q-split, C-"
     "resolvent, pole-save mutant, drop-border) plus "
     "construction pins (w9 identity+no-flip, dead "
     "chi, scramble/two-period, MAIN-42 + EXT-119).  "
     "10/10 gates, final line PHI BB SIGN VERIFIED", True),
    ("rh/problem/phi_bb_sign.pdf", "problem_statement",
     "r418 companion",
     [],
     "compiled PDF of phi_bb_sign.tex "
     "(recompiled artefact, registered unpinned)", False),
    ("rh/problem/vacuous_overflow.tex", "problem_statement",
     "r419 companion",
     [],
     "lemma-first vacuous overflow after DCCLXXXV "
     "(round 419): H3 REFUTED, razor-pole REFUTED, "
     "the six live by tau at finite N; cofinal VAC "
     "sch<0 OPEN.  H3_REFUTED / RAZOR_POLE_REFUTED / "
     "TAU_SAVE_FINITE / COFINAL_OPEN.  Finite "
     "identities plus named refutations; NO RH claim",
     True),
    ("rh/problem/verify_vacuous_overflow.py", "problem_check",
     "r419 companion",
     [],
     "machine check of every numbered lemma in "
     "vacuous_overflow.tex: standalone (VAC chart, "
     "drop-tau, drop-border) plus construction pins "
     "(kz12 overflow, kz26+razor, dead VAC, "
     "scramble/two-period, CORE + EXT).  8/8 "
     "gates, final line VACUOUS OVERFLOW VERIFIED", True),
    ("rh/problem/vacuous_overflow.pdf", "problem_statement",
     "r419 companion",
     [],
     "compiled PDF of vacuous_overflow.tex "
     "(recompiled artefact, registered unpinned)", False),
    ("rh/problem/cj_sigma.tex", "problem_statement",
     "r420 companion",
     [],
     "lemma-first c_J vs Sigma after DCCLXXXVI "
     "(round 420): den formula SATZ; naive Sigma "
     "bound LOOSE; reserve SHRINKS.  DEN_EXACT / "
     "BOUND_LOOSE / RESERVE_SHRINKS / COFINAL_OPEN.  "
     "Finite identities plus a named refutation of "
     "the O(1) gap; NO RH claim",
     True),
    ("rh/problem/verify_cj_sigma.py", "problem_check",
     "r420 companion",
     [],
     "machine check of every numbered lemma in "
     "cj_sigma.tex: standalone (den over Q, drop-"
     "border) plus construction pins (w9 den, kz26 "
     "bound, kz12 overflow, dead VAC, CORE den<2 + "
     "selected shrink).  8/8 gates, final line "
     "CJ SIGMA VERIFIED", True),
    ("rh/problem/cj_sigma.pdf", "problem_statement",
     "r420 companion",
     [],
     "compiled PDF of cj_sigma.tex "
     "(recompiled artefact, registered unpinned)", False),
    ("rh/problem/reserve_limit.tex", "problem_statement",
     "r421 companion",
     [],
     "lemma-first reserve limit after DCCLXXXVII "
     "(round 421): M1 floor preferred; M3 log "
     "model KILLED; k=10 border-fails.  "
     "FLOOR_PREFERRED / LOG_KILLED / "
     "K10_BORDER_FAIL / COFINAL_OPEN.  Finite "
     "identities plus a named AIC census; NO RH "
     "claim",
     True),
    ("rh/problem/verify_reserve_limit.py", "problem_check",
     "r421 companion",
     [],
     "machine check of every numbered lemma in "
     "reserve_limit.tex: standalone (R over Q, "
     "T0 lin, drop-border) plus construction pins "
     "(w9 R, kz26 dictionary, kz12 overflow, AIC "
     "M1, dead VAC).  8/8 gates, final line "
     "RESERVE LIMIT VERIFIED", True),
    ("rh/problem/reserve_limit.pdf", "problem_statement",
     "r421 companion",
     [],
     "compiled PDF of reserve_limit.tex "
     "(recompiled artefact, registered unpinned)", False),
    ("rh/problem/sigma_limit.tex", "problem_statement",
     "r422 companion",
     [],
     "lemma-first Sigma limit after DCCLXXXVIII "
     "(round 422): Stieltjes SATZ; closed occ "
     "density REFUTED; near-1 STABLE; limits "
     "OPEN.  STIELTJES_EXACT / DENSITY_REFUTED / "
     "NEAR1_STABLE / LIMITS_OPEN.  Finite "
     "identity plus a named census; NO RH claim",
     True),
    ("rh/problem/verify_sigma_limit.py", "problem_check",
     "r422 companion",
     [],
     "machine check of every numbered lemma in "
     "sigma_limit.tex: standalone (Stieltjes over "
     "Q, g=1 mutant, drop-border) plus "
     "construction pins (w9 identity, kz26 "
     "near-1, kz12 overflow, dead razor).  7/7 "
     "gates, final line SIGMA LIMIT VERIFIED", True),
    ("rh/problem/sigma_limit.pdf", "problem_statement",
     "r422 companion",
     [],
     "compiled PDF of sigma_limit.tex "
     "(recompiled artefact, registered unpinned)", False),
    ("rh/problem/den_limit.tex", "problem_statement",
     "r423 companion",
     [],
     "lemma-first den limit after DCCLXXXIX "
     "(round 423): formula SATZ; gam<1 census; "
     "den_inf not constructed; ||b||^2 not a "
     "subsum of S.  FORMULA_EXACT / "
     "GAMMA_LT1_CENSUS / LIMIT_OPEN / "
     "SUBSUM_REFUTED.  NO RH claim",
     True),
    ("rh/problem/verify_den_limit.py", "problem_check",
     "r423 companion",
     [],
     "machine check of every numbered lemma in "
     "den_limit.tex: standalone (den over Q, "
     "drop-vts, drop-border) plus construction "
     "pins (w9 formula, not-subsum, kz26, dead).  "
     "7/7 gates, final line DEN LIMIT VERIFIED", True),
    ("rh/problem/den_limit.pdf", "problem_statement",
     "r423 companion",
     [],
     "compiled PDF of den_limit.tex "
     "(recompiled artefact, registered unpinned)", False),
    ("rh/problem/gamma_chain.tex", "problem_statement",
     "r424 companion",
     [],
     "lemma-first gamma chain after DCCXC "
     "(round 424): mu-Parseval SATZ; termwise "
     "w_k REFUTED; ||b||^2 <= 0.80 S census; "
     "gamma<1 OPEN.  BESSEL_EXACT / "
     "W_TERM_REFUTED / SHARP_CENSUS / "
     "GAMMA_OPEN.  NO RH claim",
     True),
    ("rh/problem/verify_gamma_chain.py", "problem_check",
     "r424 companion",
     [],
     "machine check of every numbered lemma in "
     "gamma_chain.tex: standalone (Bessel over "
     "Q, gamma bookkeeping, drop-vts) plus "
     "construction pins (w9 Parseval, w_k, "
     "kz26, dead/scramble/unnorm).  7/7 "
     "gates, final line GAMMA CHAIN VERIFIED", True),
    ("rh/problem/gamma_chain.pdf", "problem_statement",
     "r424 companion",
     [],
     "compiled PDF of gamma_chain.tex "
     "(recompiled artefact, registered unpinned)", False),
    ("rh/problem/cross_chain_gamma.tex", "problem_statement",
     "r425 companion",
     [],
     "lemma-first cross-chain gamma after DCCXCI "
     "(round 425): ||b||^2 <= S SATZ; posted "
     "||b||^2 < B_w via q_N<1; dead q_N>1; "
     "cofinal OPEN.  B2_LE_S_SATZ / "
     "QN_BRIDGES_BW / DEAD_NEEDS_SLACK / "
     "COFINAL_OPEN.  NO RH claim",
     True),
    ("rh/problem/verify_cross_chain.py", "problem_check",
     "r425 companion",
     [],
     "machine check of every numbered lemma in "
     "cross_chain_gamma.tex: standalone (kernel "
     "over Q, ray, q_N bridge) plus construction "
     "pins (w9 b2<=S, ||G||_op=1, k=5/dead/"
     "unnorm).  6/6 gates, final line CROSS "
     "CHAIN VERIFIED", True),
    ("rh/problem/cross_chain_gamma.pdf", "problem_statement",
     "r425 companion",
     [],
     "compiled PDF of cross_chain_gamma.tex "
     "(recompiled artefact, registered unpinned)", False),
    ("rh/problem/campaign_audit.tex", "problem_statement",
     "r427 companion",
     [],
     "adversarial campaign audit of R397-R426 "
     "(round 427): independent re-computation "
     "of seven load-bearing targets.  0 BUG / "
     "2 SUSPECT / 5 CLEAN.  No round verdict "
     "flips.  NO RH claim",
     True),
    ("rh/problem/verify_campaign_audit.py", "problem_check",
     "r427 companion",
     [],
     "machine check of every numbered lemma in "
     "campaign_audit.tex: standalone (FL "
     "dictionary, Hankel linear, Loewner PD, "
     "indefinite block over Q) plus "
     "construction pins (w9 intertwiner, QD "
     "1.357, KKT ||T0||, floor vs k/N, live "
     "chi3-9).  9/9 gates, final line CAMPAIGN "
     "AUDIT NOTE VERIFIED", True),
    ("rh/problem/campaign_audit.pdf", "problem_statement",
     "r427 companion",
     [],
     "compiled PDF of campaign_audit.tex "
     "(recompiled artefact, registered unpinned)", False),
    ("rh/problem/qn_reopened.tex", "problem_statement",
     "r428 companion",
     [],
     "lemma-first reopen of cofinal q_N<1 on the "
     "selected sequence a_k=2^k (round 428): "
     "selected margin 0.617 vs 42er 0.0195; "
     "razor-overlap VAC-only; |Z_loc| wins; "
     "Nyquist face REFUTED on VAC.  "
     "SELECTED_MARGIN_GO / OVERLAP_VAC_ONLY / "
     "ZLOC_WINS / COFINAL_OPEN.  NO RH claim",
     True),
    ("rh/problem/verify_qn_reopened.py", "problem_check",
     "r428 companion",
     [],
     "machine check of every numbered lemma in "
     "qn_reopened.tex: standalone (dictionary "
     "over Q, Z0_sel=1/2, orthogonality) plus "
     "construction pins (pp-map, w9 four "
     "coords, VAC overlap / Nyquist / dead-15 "
     "/ kz=16).  6/6 gates, final line QN "
     "REOPENED VERIFIED", True),
    ("rh/problem/qn_reopened.pdf", "problem_statement",
     "r428 companion",
     [],
     "compiled PDF of qn_reopened.tex "
     "(recompiled artefact, registered unpinned)", False),
    ("rh/problem/zloc_head.tex", "problem_statement",
     "r429 companion",
     [],
     "lemma-first selected |Z_loc|<=1/2 head bound "
     "(round 429): identity SATZ; unsigned/Chebyshev/Abel "
     "REFUTED on selected; bound remains a finite census, "
     "no k0.  FORMULA_SATZ / TRIANGLE_REFUTED / "
     "BOUND_CENSUS / NO_K0.  NO RH claim",
     True),
    ("rh/problem/verify_zloc_head.py", "problem_check",
     "r429 companion",
     [],
     "machine check of every numbered lemma in "
     "zloc_head.tex: standalone (dictionary over Q, "
     "split, 1/2<M) plus construction pins (w9 formula, "
     "triangle/scramble/dead-15, kz=16 + k=3,4,5 half).  "
     "6/6 gates, final line ZLOC HEAD VERIFIED", True),
    ("rh/problem/zloc_head.pdf", "problem_statement",
     "r429 companion",
     [],
     "compiled PDF of zloc_head.tex "
     "(recompiled artefact, registered unpinned)", False),
    ("rh/problem/source_potapov.tex", "problem_statement",
     "r431 companion",
     [],
     "lemma-first source Potapov factorisation after "
     "DCCXCVII (round 431): unipotent Redheffer product "
     "equals Cauchy m_X SATZ; Cauchy-pi identity for "
     "Lagrange S0 SATZ; Pick(product) congruent to "
     "I-T0*T0 REFUTED (kappa 0 vs 1).  "
     "SOURCE_FACTOR_NOT_FOUND.  Finite identities plus "
     "a named refutation; NO RH claim",
     True),
    ("rh/problem/verify_source_potapov.py", "problem_check",
     "r431 companion",
     [],
     "machine check of every numbered lemma in "
     "source_potapov.tex: standalone (Redheffer=Cauchy, "
     "Cauchy-pi, Gate 3 fail, constructor audit) plus "
     "construction pins (w9/kz15/kz18 Pick mismatch, "
     "source-order Uvarov, permute/scramble/twin).  "
     "7/7 gates, final line SOURCE POTAPOV VERIFIED", True),
    ("rh/problem/source_potapov.pdf", "problem_statement",
     "r431 companion",
     [],
     "compiled PDF of source_potapov.tex "
     "(recompiled artefact, registered unpinned)", False),
    ("rh/problem/r431_audit.tex", "problem_statement",
     "r431-AUDIT companion",
     [],
     "adversarial focus-audit of R431 "
     "SOURCE_FACTOR_NOT_FOUND: positive-mass "
     "J-products stay in S_0 (non-commuting "
     "Blaschke-Potapov + Redheffer star); R431 "
     "numbers reproduced; Cauchy-pi on a second "
     "Q-window.  CONFIRMED.  NO RH claim",
     True),
    ("rh/problem/verify_r431_audit.py", "problem_check",
     "r431-AUDIT companion",
     [],
     "machine check of every numbered lemma in "
     "r431_audit.tex: standalone (Cauchy sum, "
     "Cauchy-pi, BP non-commute, Redheffer star, "
     "second window) plus construction pins "
     "(w9 P_X / I-TT, Uvarov orders).  7/7 gates, "
     "final line R431 AUDIT NOTE VERIFIED", True),
    ("rh/problem/r431_audit.pdf", "problem_statement",
     "r431-AUDIT companion",
     [],
     "compiled PDF of r431_audit.tex "
     "(recompiled artefact, registered unpinned)", False),
    ("rh/problem/edge_redheffer.tex", "problem_statement",
     "r433 companion",
     [],
     "lemma-first Redheffer identification of R->R^dagger "
     "(round 433): last Potapov pivot delta=1-q^dagger=-sch "
     "(c'=1); the quarter is not a universal multiple.  "
     "REDHEFFER_EXACT / PIVOT_IS_ONE_MINUS_QDAG / "
     "QUARTER_NOT_UNIVERSAL.  NO RH claim",
     True),
    ("rh/problem/verify_edge_redheffer.py", "problem_check",
     "r433 companion",
     [],
     "machine check of every numbered lemma in "
     "edge_redheffer.tex: standalone (Redheffer mixed "
     "form over Q, sequential CD-then-border, last-pivot "
     "dictionary, 1/4<5/7 + drop-border) plus construction "
     "pins (w9 Redheffer/identity, k=3 margin, dead "
     "CHI3-15 / living CHI3-9, ones-Woodbury kill).  "
     "8/8 gates, final line EDGE REDHEFFER VERIFIED", True),
    ("rh/problem/edge_redheffer.pdf", "problem_statement",
     "r433 companion",
     [],
     "compiled PDF of edge_redheffer.tex "
     "(recompiled artefact, registered unpinned)", False),
    ("rh/problem/p1_overload.tex", "problem_statement",
     "r435 companion",
     [],
     "lemma-first P1 overload bound (round 435): "
     "n_-(A0)<=1 is a crossing budget of the nested "
     "mu-CD chain on Y; Cauchy-pi / GK universal cap "
     "REFUTED over Q; selected save-rate CENSUS.  "
     "DEPTH_CHAIN_EXACT / GK_UNIVERSAL_REFUTED / "
     "SAVE_RATE_CENSUS.  NO RH claim",
     True),
    ("rh/problem/verify_p1_overload.py", "problem_check",
     "r435 companion",
     [],
     "machine check of every numbered lemma in "
     "p1_overload.tex: standalone (2x2 toy det, "
     "depth lift, 3x3 GK fail, 2x2 ND witness, "
     "constructor audit) plus construction pins "
     "(w9 nC curve, permute/scramble/two-period, "
     "false depth N_w-1).  8/8 gates, final line "
     "P1 OVERLOAD VERIFIED", True),
    ("rh/problem/p1_overload.pdf", "problem_statement",
     "r435 companion",
     [],
     "compiled PDF of p1_overload.tex "
     "(recompiled artefact, registered unpinned)", False),
    ("rh/problem/p2_determinant.tex", "problem_statement",
     "r436 companion",
     [],
     "lemma-first reverse-CS / rank-1 decomposition of "
     "det K2 on the nneg-1 branch (round 436): identity "
     "SATZ, coarse lmax bound killed at kz46, anatomy "
     "MIXED, remainder p^T K2_+^{-1} p > 1.  "
     "REDUZIERT / IDENTITY_EXACT / ANATOMY_MIXED / "
     "COARSE_KILLED_AT_KZ46 / ALTERNATION_EXPLAINED.  "
     "NO RH claim",
     True),
    ("rh/problem/verify_p2_determinant.py", "problem_check",
     "r436 companion",
     [],
     "machine check of every numbered lemma in "
     "p2_determinant.tex: standalone (reverse-CS over Q, "
     "J-plus-R split, drop-psi toy, tiny-overlap adversary) "
     "plus construction pins (w9 identity + C_min, "
     "kz18 floor / kz46 coarse kill, kz12 vacuous + "
     "CHI3-15 nneg-1, scramble / wrong J).  "
     "8/8 gates, final line P2 DETERMINANT VERIFIED", True),
    ("rh/problem/p2_determinant.pdf", "problem_statement",
     "r436 companion",
     [],
     "compiled PDF of p2_determinant.tex "
     "(recompiled artefact, registered unpinned)", False),
    ("rh/problem/evolutionary_certificate.tex", "problem_statement",
     "r438 companion",
     [],
     "evolutionary certificate search (round 438): "
     "grammar GP / SOS-LP / adversarial grid with a hard "
     "train/holdout split.  A:NOT_FOUND / B:NOT_FOUND / "
     "C:NOT_FOUND.  Truncation nC=2 is r395, not a "
     "two-case falsifier.  Finite identities plus named "
     "search negatives; NO RH claim",
     True),
    ("rh/problem/verify_evolutionary_cert.py", "problem_check",
     "r438 companion",
     [],
     "machine check of every numbered lemma in "
     "evolutionary_certificate.tex: standalone Q toys "
     "(ONES-Y, r375, B2 split, nneg=2 detector) plus "
     "construction pins (w9 C/cosines, INVPY uniform, "
     "train MAIN-only, permute/scramble, illegal a=0, "
     "selected k=7 nC=0).  10/10 gates, final line "
     "EVOLUTIONARY CERT VERIFIED", True),
    ("rh/problem/evolutionary_certificate.pdf", "problem_statement",
     "r438 companion",
     [],
     "compiled PDF of evolutionary_certificate.tex "
     "(recompiled artefact, registered unpinned)", False),
    ("rh/problem/residual_loewner.tex", "problem_statement",
     "r439 companion",
     [],
     "lemma-first interpolant residual Loewner/Bezout "
     "(round 439): disp rank 2 SATZ, S0=K_YY^{-1} SATZ, "
     "kdim=0 dressed Loewner SATZ, B1 Bez(P_Y,Q) miss.  "
     "RESIDUAL_LOEWNER_PLUS_CONTROLLED_DIAGONAL.  "
     "NO RH claim",
     True),
    ("rh/problem/verify_residual_loewner.py", "problem_check",
     "r439 companion",
     [],
     "machine check of every numbered lemma in "
     "residual_loewner.tex: standalone Q toys "
     "(disp rank, Cauchy-pi, K^{-1}, dressed Loewner, "
     "ones-residual, B1 miss, Sturm != 1-q^d) plus "
     "construction pins (w9 disp+Kinv, permute/scramble/"
     "chi census).  7/7 gates, final line "
     "RESIDUAL LOEWNER VERIFIED", True),
    ("rh/problem/residual_loewner.pdf", "problem_statement",
     "r439 companion",
     [],
     "compiled PDF of residual_loewner.tex "
     "(recompiled artefact, registered unpinned)", False),
    ("rh/problem/mean_tau_index.tex", "problem_statement",
     "r440 companion",
     [],
     "lemma-first mean tau-winding (round 440): T1/T2/MI2 "
     "SATZ, collar anatomy of the s=1 cluster, source "
     "Dirichlet integrand, selected+core mean 0<1, dead "
     "chi kappa=1.  IDENTITIES_EXACT / "
     "COLLAR_BOSS_QUANTIFIED / BLOCK_MEAN_CENSUS / "
     "UNCONDITIONAL_OPEN.  NO RH claim",
     True),
    ("rh/problem/verify_mean_tau.py", "problem_check",
     "r440 companion",
     [],
     "machine check of every numbered lemma in "
     "mean_tau_index.tex: standalone (Q T1 kappa=1, "
     "T2 winding, r409 toy kappa=0, MI2 linearity) plus "
     "construction pins (w9 three-way + collar, CD/cyclic "
     "source form, dead/live chi + soft mutants).  "
     "8/8 gates, final line MEAN TAU INDEX VERIFIED", True),
    ("rh/problem/mean_tau_index.pdf", "problem_statement",
     "r440 companion",
     [],
     "compiled PDF of mean_tau_index.tex "
     "(recompiled artefact, registered unpinned)", False),
    ("rh/problem/diag_lifts_loewner.tex", "problem_statement",
     "r441 companion",
     [],
     "lemma-first DIAG_LIFTS (round 441): Gram SATZ, "
     "lift-count SATZ, interlacing-inertia REFUTED, "
     "d_min=>n_-<=1 REFUTED.  REDUZIERT.  NO RH claim",
     True),
    ("rh/problem/verify_diag_lifts.py", "problem_check",
     "r441 companion",
     [],
     "machine check of every numbered lemma in "
     "diag_lifts_loewner.tex: standalone Q toys "
     "(Gram, L ND, lift count, 6-node refute) plus "
     "construction pins (w9 WK, kz52, permute/chi).  "
     "6/6 gates, final line DIAG LIFTS VERIFIED", True),
    ("rh/problem/diag_lifts_loewner.pdf", "problem_statement",
     "r441 companion",
     [],
     "compiled PDF of diag_lifts_loewner.tex "
     "(recompiled artefact, registered unpinned)", False),
    ("rh/problem/block_mean.tex", "problem_statement",
     "r442 companion",
     [],
     "lemma-first unconditional block mean (round 442): "
     "kappa^dagger = 1{q^dagger>1} SATZ; unsigned Chebyshev "
     "majorant REFUTED; Selected+core pointwise living; "
     "mean bound OPEN.  REDUZIERT.  NO RH claim",
     True),
    ("rh/problem/verify_block_mean.py", "problem_check",
     "r442 companion",
     [],
     "machine check of every numbered lemma in "
     "block_mean.tex: standalone (Q pivot dictionary, "
     "living toy, MI2) plus construction pins (w9 "
     "dictionary+source, selected k=3..5, dead/live chi).  "
     "8/8 gates, final line BLOCK MEAN VERIFIED", True),
    ("rh/problem/block_mean.pdf", "problem_statement",
     "r442 companion",
     [],
     "compiled PDF of block_mean.tex "
     "(recompiled artefact, registered unpinned)", False),
    ("rh/problem/delta_floor.tex", "problem_statement",
     "r443 companion",
     [],
     "lemma-first selected delta floor (round 443): "
     "chart SATZ; floor preferred on k=5..9 slice; "
     "full sequence unsettled; kz16 below.  REDUZIERT.  "
     "NO RH claim",
     True),
    ("rh/problem/verify_delta_floor.py", "problem_check",
     "r443 companion",
     [],
     "machine check of every numbered lemma in "
     "delta_floor.tex: standalone (Q P1/VAC charts, "
     "frozen slice AIC) plus construction pins (w9 "
     "chart, kz16 below, dead chi + k=10 lock).  "
     "6/6 gates, final line DELTA FLOOR VERIFIED", True),
    ("rh/problem/delta_floor.pdf", "problem_statement",
     "r443 companion",
     [],
     "compiled PDF of delta_floor.tex "
     "(recompiled artefact, registered unpinned)", False),
    ("rh/problem/signed_border_mean.tex", "problem_statement",
     "r444 companion",
     [],
     "lemma-first signed border mean (round 444): "
     "triple-sum SATZ; pole not the carrier; diagonal "
     "overflows; off-diagonal load-bearing; bound "
     "ZIRKULAER (second circularity after r399).  "
     "NO RH claim",
     True),
    ("rh/problem/verify_signed_border.py", "problem_check",
     "r444 companion",
     [],
     "machine check of every numbered lemma in "
     "signed_border_mean.tex: standalone (Q triple sum, "
     "pole split, diag not whole) plus construction pins "
     "(w9 identity+split, selected k=3..5, dead/live chi).  "
     "8/8 gates, final line SIGNED BORDER MEAN VERIFIED", True),
    ("rh/problem/signed_border_mean.pdf", "problem_statement",
     "r444 companion",
     [],
     "compiled PDF of signed_border_mean.tex "
     "(recompiled artefact, registered unpinned)", False),
    ("rh/problem/deep_builder.tex", "problem_statement",
     "r445 companion",
     [],
     "lemma-first deep builder (round 445): unused "
     "Lanczos hotspot; k=8 live pin; k=10/11/12 not "
     "ABD-living; slice floor with live k=8.  "
     "INFRA_UNLOCKED.  NO RH claim",
     True),
    ("rh/problem/verify_deep_builder.py", "problem_check",
     "r445 companion",
     [],
     "machine check of every numbered lemma in "
     "deep_builder.tex: standalone (Q q^dagger formula, "
     "frozen slice AIC with k=8) plus construction pins "
     "(w9 skip-Lanczos, k=8 map, deep maps, dead chi).  "
     "7/7 gates, final line DEEP BUILDER VERIFIED", True),
    ("rh/problem/deep_builder.pdf", "problem_statement",
     "r445 companion",
     [],
     "compiled PDF of deep_builder.tex "
     "(recompiled artefact, registered unpinned)", False),
    ("rh/problem/deep_abd.tex", "problem_statement",
     "r446 companion",
     [],
     "lemma-first deep ABD adjudication (round 446): "
     "k=10/11/12 breaks are REAL; mesh repair at the "
     "2^k anchors fails; last living kz=136.  "
     "COFINAL_ABD_OPEN.  NO RH claim",
     True),
    ("rh/problem/verify_deep_abd.py", "problem_check",
     "r446 companion",
     [],
     "machine check of every numbered lemma in "
     "deep_abd.tex: standalone (REAL pins, slice "
     "floor stands) plus construction pins "
     "(k=10 float flip, k=12 class, last-live, "
     "dead chi).  7/7 gates, final line "
     "DEEP ABD VERIFIED", True),
    ("rh/problem/deep_abd.pdf", "problem_statement",
     "r446 companion",
     [],
     "compiled PDF of deep_abd.tex "
     "(recompiled artefact, registered unpinned)", False),
    ("rh/problem/exact_atom.tex", "problem_statement",
     "r447 companion",
     [],
     "lemma-first exact-atom adjudication (round 447): "
     "k=10 is EXACT_DEAD; atoms are ulp-close to float64; "
     "this 2^k family does not feed frequently.  "
     "NO RH claim",
     True),
    ("rh/problem/verify_exact_atom.py", "problem_check",
     "r447 companion",
     [],
     "machine check of every numbered lemma in "
     "exact_atom.tex: standalone (EXACT_DEAD pins, "
     "atom-ulp, slice floor) plus construction pins "
     "(k=5 exact atoms/chain, k=10 float flip, dead "
     "chi).  7/7 gates, final line EXACT ATOM VERIFIED",
     True),
    ("rh/problem/exact_atom.pdf", "problem_statement",
     "r447 companion",
     [],
     "compiled PDF of exact_atom.tex "
     "(recompiled artefact, registered unpinned)", False),
    ("rh/problem/exact_band.tex", "problem_statement",
     "r448 companion",
     [],
     "lemma-first exact living band (round 448): "
     "NOT_COFINAL; 2^k commensurability refuted; "
     "kz197 is a zeta-chain death; next-odd family "
     "fails at k=10.  NO RH claim",
     True),
    ("rh/problem/verify_exact_band.py", "problem_check",
     "r448 companion",
     [],
     "machine check of every numbered lemma in "
     "exact_band.tex: standalone (NOT_COFINAL pins, "
     "kz197 coords, slice floor) plus construction "
     "pins (kz136 live, kz230 float, next-odd wall, "
     "dead chi).  7/7 gates, final line EXACT BAND "
     "VERIFIED",
     True),
    ("rh/problem/exact_band.pdf", "problem_statement",
     "r448 companion",
     [],
     "compiled PDF of exact_band.tex "
     "(recompiled artefact, registered unpinned)", False),

    ("rh/problem/flip_vs_stab.tex", "problem_statement",
     "r449 companion",
     [],
     "lemma-first flip vs stabilization (round 449): "
     "TAIL_ONLY; every measured chain flip sits "
     "past n_stab; prefix-R^dagger lives.  "
     "NO RH claim, NO anti-RH claim",
     True),
    ("rh/problem/verify_flip_vs_stab.py", "problem_check",
     "r449 companion",
     [],
     "machine check of every numbered lemma in "
     "flip_vs_stab.tex: standalone (TAIL_ONLY, "
     "flip>n_stab, slice floor) plus construction "
     "pins (kz17 n_stab, kz197 prefix-80, dead "
     "chi).  6/6 gates, final line FLIP VS STAB "
     "VERIFIED",
     True),
    ("rh/problem/flip_vs_stab.pdf", "problem_statement",
     "r449 companion",
     [],
     "compiled PDF of flip_vs_stab.tex "
     "(recompiled artefact, registered unpinned)", False),

    ("rh/problem/prefix_mincut.tex", "problem_statement",
     "r450 companion",
     [],
     "lemma-first prefix mincut (round 450): "
     "M2_UNDECIDED; n_stab-compression of R^dagger "
     "is the frequently-cone; living full vs prefix "
     "split; chi prefix lives.  "
     "NO RH claim, NO anti-RH claim",
     True),
    ("rh/problem/verify_prefix_mincut.py", "problem_check",
     "r450 companion",
     [],
     "machine check of every numbered lemma in "
     "prefix_mincut.tex: standalone (M2_UNDECIDED, "
     "slice M1, pure M2, n_stab grows) plus "
     "construction pins (kz17 split, chi split).  "
     "7/7 gates, final line PREFIX MINCUT "
     "VERIFIED",
     True),
    ("rh/problem/prefix_mincut.pdf", "problem_statement",
     "r450 companion",
     [],
     "compiled PDF of prefix_mincut.tex "
     "(recompiled artefact, registered unpinned)", False),

    ("rh/problem/nstab_transition.tex", "problem_statement",
     "r451 companion",
     [],
     "lemma-first n_stab transition anatomy (round 451): "
     "TRANSITION_SMOOTH; RES_MISMATCH; "
     "PREFIX_Q_PLATEAU.  "
     "NO RH claim, NO anti-RH claim",
     True),
    ("rh/problem/verify_nstab_transition.py", "problem_check",
     "r451 companion",
     [],
     "machine check of every numbered lemma in "
     "nstab_transition.tex: standalone "
     "(TRANSITION_SMOOTH, RES_MISMATCH, "
     "PREFIX_Q_PLATEAU) plus construction pins "
     "(kz17 n_stab/n_res, q-cliff, scramble).  "
     "6/6 gates, final line NSTAB TRANSITION "
     "VERIFIED",
     True),
    ("rh/problem/nstab_transition.pdf", "problem_statement",
     "r451 companion",
     [],
     "compiled PDF of nstab_transition.tex "
     "(recompiled artefact, registered unpinned)", False),

    ("rh/problem/plateau_theorem.tex", "problem_statement",
     "r452 companion",
     [],
     "lemma-first plateau identity (round 452): "
     "PLATEAU_IDENTITY_PROVED; QSTAR_UNDECIDED; "
     "q_* = M_d/(M_d+5/7) on M_d = mu_0-nu_0.  "
     "NO RH claim, NO anti-RH claim",
     True),
    ("rh/problem/verify_plateau_theorem.py", "problem_check",
     "r452 companion",
     [],
     "machine check of every numbered lemma in "
     "plateau_theorem.tex: standalone "
     "(PLATEAU_IDENTITY_PROVED, QSTAR_UNDECIDED, "
     "sister A(ii) REFUTED) plus construction "
     "pins (kz17 grade-0, rho cliff, scramble).  "
     "6/6 gates, final line PLATEAU THEOREM "
     "VERIFIED",
     True),
    ("rh/problem/plateau_theorem.pdf", "problem_statement",
     "r452 companion",
     [],
     "compiled PDF of plateau_theorem.tex "
     "(recompiled artefact, registered unpinned)", False),

    ("rh/problem/border_mass.tex", "problem_statement",
     "r453 companion",
     [],
     "lemma-first border-mass inequality (round 453): "
     "BOUND_PROVED; MASS_CLASSICAL_REDUCED_GROWING; "
     "RACE_WON.  "
     "NO RH claim, NO anti-RH claim",
     True),
    ("rh/problem/verify_border_mass.py", "problem_check",
     "r453 companion",
     [],
     "machine check of every numbered lemma in "
     "border_mass.tex: standalone "
     "(BOUND_PROVED, MASS_CLASSICAL_REDUCED_GROWING, "
     "RACE_WON, sister g-cliff) plus construction "
     "pins (M_d vs N, race n=20, scramble).  "
     "6/6 gates, final line BORDER MASS VERIFIED",
     True),
    ("rh/problem/border_mass.pdf", "problem_statement",
     "r453 companion",
     [],
     "compiled PDF of border_mass.tex "
     "(recompiled artefact, registered unpinned)", False),

    ("rh/problem/limit_object.tex", "problem_statement",
     "r454 companion",
     [],
     "lemma-first folded-moment limit object (round 454): "
     "LIMIT_CLASSICAL; LIMITCHAIN_ALIVE_200; "
     "CHAIN_DOCUMENTED.  "
     "NO RH claim, NO anti-RH claim",
     True),
    ("rh/problem/verify_limit_object.py", "problem_check",
     "r454 companion",
     [],
     "machine check of every numbered lemma in "
     "limit_object.tex: standalone "
     "(LIMIT_CLASSICAL, LIMITCHAIN_ALIVE_200, "
     "CHAIN_DOCUMENTED, m_inf pins, MAIN=ARCH) plus "
     "construction pins (rho_16, Lipschitz, "
     "drop-500).  "
     "6/6 gates, final line LIMIT OBJECT VERIFIED",
     True),
    ("rh/problem/limit_object.pdf", "problem_statement",
     "r454 companion",
     [],
     "compiled PDF of limit_object.tex "
     "(recompiled artefact, registered unpinned)", False),

    ("rh/problem/arch_chain.tex", "problem_statement",
     "r455 companion",
     [],
     "lemma-first ARCH fold and conditional chain (round 455): "
     "L3_PROVED; L1_PNT_SUFFICIENT; "
     "CHAIN_MAPPED.  "
     "NO RH claim, NO anti-RH claim",
     True),
    ("rh/problem/verify_arch_chain.py", "problem_check",
     "r455 companion",
     [],
     "machine check of every numbered lemma in "
     "arch_chain.tex: standalone "
     "(L3_PROVED, L1_PNT_SUFFICIENT, "
     "CHAIN_MAPPED, 3-lag identity, sympy rho) plus "
     "construction pins (n_stab=p0-1, MAIN-ARCH "
     "kernel, J_B).  "
     "6/6 gates, final line ARCH CHAIN VERIFIED",
     True),
    ("rh/problem/arch_chain.pdf", "problem_statement",
     "r455 companion",
     [],
     "compiled PDF of arch_chain.tex "
     "(recompiled artefact, registered unpinned)", False),

    ("rh/problem/vacuity_redteam.tex", "problem_statement",
     "r456 companion",
     [],
     "prefix vacuity red-team (round 456): "
     "VACUOUS_CONFIRMED.  Iff.rfl is a naming; "
     "Python prefix is prime-blind; arithmetic "
     "at J_P and combRead.  "
     "NO RH claim, NO anti-RH claim",
     True),
    ("rh/problem/verify_vacuity_redteam.py", "problem_check",
     "r456 companion",
     [],
     "machine check of every numbered lemma in "
     "vacuity_redteam.tex: standalone "
     "(VACUOUS_CONFIRMED, comb pin, Iff.rfl naming) "
     "plus construction pins (kz17 prefix/J_P, "
     "kz69 n_stab/n_f).  "
     "6/6 gates, final line VACUITY REDTEAM VERIFIED",
     True),
    ("rh/problem/vacuity_redteam.pdf", "problem_statement",
     "r456 companion",
     [],
     "compiled PDF of vacuity_redteam.tex "
     "(recompiled artefact, registered unpinned)", False),

    ("rh/problem/jp_increment.tex", "problem_statement",
     "r457 companion",
     [],
     "lemma-first J_P increment (round 457): "
     "INCREMENT_DRIFT; RACE_EATS_K10; "
     "LEMMA_REDUCED.  "
     "NO RH claim, NO anti-RH claim",
     True),
    ("rh/problem/verify_jp_increment.py", "problem_check",
     "r457 companion",
     [],
     "machine check of every numbered lemma in "
     "jp_increment.tex: standalone "
     "(INCREMENT_DRIFT, RACE_EATS_K10, "
     "LEMMA_REDUCED, r456 accepted, cliff, "
     "Delta-rho drift) plus construction pins "
     "(kz17 race, k=10 eats margin, scramble).  "
     "6/6 gates, final line JP INCREMENT VERIFIED",
     True),
    ("rh/problem/jp_increment.pdf", "problem_statement",
     "r457 companion",
     [],
     "compiled PDF of jp_increment.tex "
     "(recompiled artefact, registered unpinned)", False),

    ("rh/problem/cofinal_family.tex", "problem_statement",
     "r458 companion",
     [],
     "lemma-first cofinal family (round 458): "
     "FAMILY_CANDIDATE; TABLE_CAP_ARTEFACT; "
     "RESIDUAL_DEEP_DEATH.  "
     "NO RH claim, NO anti-RH claim",
     True),
    ("rh/problem/verify_cofinal_family.py", "problem_check",
     "r458 companion",
     [],
     "machine check of every numbered lemma in "
     "cofinal_family.tex: standalone "
     "(FAMILY_CANDIDATE, grid 76, a-wall, "
     "Lean mesh) plus construction pins "
     "(lean k=10, kz197 capped-dead).  "
     "6/6 gates, final line COFINAL FAMILY "
     "VERIFIED",
     True),
    ("rh/problem/cofinal_family.pdf", "problem_statement",
     "r458 companion",
     [],
     "compiled PDF of cofinal_family.tex "
     "(recompiled artefact, registered unpinned)", False),

    ("rh/problem/fullcomb_cleanup.tex", "problem_statement",
     "r459 companion",
     [],
     "lemma-first fullcomb cleanup (round 459): "
     "RACE_TREND_BROKEN; LEANFAM_EXACT_ALIVE(12); "
     "KZ137_OUTSIDE_MINCUT.  "
     "NO RH claim, NO anti-RH claim",
     True),
    ("rh/problem/verify_fullcomb_cleanup.py", "problem_check",
     "r459 companion",
     [],
     "machine check of every numbered lemma in "
     "fullcomb_cleanup.tex: standalone "
     "(verdicts, frame-A race break, Lean band, "
     "Lean mesh) plus construction pins "
     "(kz17 race, lean k=10, lean a=641).  "
     "7/7 gates, final line FULLCOMB CLEANUP "
     "VERIFIED",
     True),
    ("rh/problem/fullcomb_cleanup.pdf", "problem_statement",
     "r459 companion",
     [],
     "compiled PDF of fullcomb_cleanup.tex "
     "(recompiled artefact, registered unpinned)", False),

    ("rh/problem/race_proof.tex", "problem_statement",
     "r460 companion",
     [],
     "full proof attempt at the selected-window race: "
     "OUTCOME PARTIAL; spectral reduction and two-band "
     "criterion proved; cofinal source-derived spectral-"
     "overlap estimate remains open.  "
     "NO RH claim, NO anti-RH claim",
     True),
    ("rh/problem/verify_race_proof.py", "problem_check",
     "r460 companion",
     [],
     "machine check of every numbered theorem in "
     "race_proof.tex: exact rational spectral/two-band "
     "wards plus full-comb k=5..12 construction pins.  "
     "10/10 gates, final line RACE PROOF ATTEMPT "
     "VERIFIED -- OUTCOME PARTIAL",
     True),
    ("rh/problem/race_proof.pdf", "problem_statement",
     "r460 companion",
     [],
     "compiled PDF of race_proof.tex "
     "(recompiled artefact, registered unpinned)", False),

    ("rh/problem/overlap_mechanism.tex", "problem_statement",
     "r467 companion",
     [],
     "lemma-first overlap mechanism (round 467): "
     "STUCK(QUALITATIVE_ALIGNMENT_REAL; "
     "ABEL_CURRENCY_TOO_COARSE; "
     "SOURCE_TO_BORDER_BASIS_BRIDGE_MISSING).  "
     "NO RH claim, NO anti-RH claim",
     True),
    ("rh/problem/verify_overlap_mechanism.py", "problem_check",
     "r467 companion",
     [],
     "machine check of every numbered lemma in "
     "overlap_mechanism.tex: standalone "
     "(verdicts, Abel lemma, anatomy, stop "
     "gate) plus construction pins "
     "(k=5..12 top modes, band factors).  "
     "9/9 gates, final line OVERLAP MECHANISM "
     "NOTE VERIFIED -- VERDICT STUCK",
     True),
    ("rh/problem/overlap_mechanism.pdf", "problem_statement",
     "r467 companion",
     [],
     "compiled PDF of overlap_mechanism.tex "
     "(recompiled artefact, registered unpinned)", False),

    ("rh/problem/octave_renorm.tex", "problem_statement",
     "r468 companion",
     [],
     "lemma-first octave renormalization (round 468): "
     "OCTAVE_NOT_CAUCHY; EDGE_TWO_POINTS; "
     "REDUCTION_ALIAS.  "
     "NO RH claim, NO anti-RH claim",
     True),
    ("rh/problem/verify_octave_renorm.py", "problem_check",
     "r468 companion",
     [],
     "machine check of every numbered lemma in "
     "octave_renorm.tex: standalone "
     "(verdicts, r-sequence, isolated octave, "
     "weight growth) plus construction pins "
     "(k=5, 8->9 edge, Delta-halving).  "
     "7/7 gates, final line OCTAVE RENORM "
     "VERIFIED",
     True),
    ("rh/problem/octave_renorm.pdf", "problem_statement",
     "r468 companion",
     [],
     "compiled PDF of octave_renorm.tex "
     "(recompiled artefact, registered unpinned)", False),

    ("rh/problem/correlation_wall_judgment.tex", "problem_statement",
     "r469",
     [],
     _R469_STATUS,
     True),
    ("rh/problem/correlation_wall_judgment.pdf", "problem_statement",
     "r469",
     [],
     "compiled PDF of correlation_wall_judgment.tex "
     "(recompiled artefact, registered unpinned)", False),

    ("rh/problem/quadrep.tex", "problem_statement",
     "r470",
     [],
     _R470_STATUS,
     True),
    ("rh/problem/verify_quadrep.py", "problem_check",
     "r470 companion/r638L",
     [],
     "machine check of r470 obstruction: original channel "
     "unweakened, quantifier witness proved, named signed "
     "obstruction, historical sorry census 8, numeric probe.  "
     "6/6 gates, final line QUADREP VERIFIED.  r638L reseal: "
     "project census 5, external 1; no RH claim",
     True),
    ("rh/problem/quadrep.pdf", "problem_statement",
     "r470",
     [],
     "compiled PDF of quadrep.tex "
     "(recompiled artefact, registered unpinned)", False),


    ("rh/problem/classical_cert.tex", "problem_statement",
     "r471",
     [],
     _R471_STATUS,
     True),
    ("rh/problem/verify_classical_cert.py", "problem_check",
     "r471 companion",
     [],
     "machine check of classical_cert.tex: note tokens "
     "(GRID_CERTIFIED vs lambda_*(L), F2b, scramble, "
     "dictionary-free, L=0.8 calibration), smoke run, "
     "sealed CERT_PINS/SHAPE_PINS.  6/6 gates, final line "
     "CLASSICAL CERT VERIFIED -- GRID_CERTIFIED(L_max=2.7726)",
     True),
    ("rh/problem/classical_cert.pdf", "problem_statement",
     "r471",
     [],
     "compiled PDF of classical_cert.tex "
     "(recompiled artefact, registered unpinned)", False),

    ("rh/problem/extraction_joint.tex", "problem_statement",
     "r473",
     [],
     _R473_STATUS,
     True),
    ("rh/problem/verify_extraction_joint.py", "problem_check",
     "r473 companion/r638L",
     [],
     "machine check of r473 extraction joint: polynomial "
     "bridge proved, named approx and redesigned joint, "
     "historical endpoint retained, artefact pins, historical "
     "sorry census 8, numeric probe.  6/6 gates, final line "
     "EXTRACTION JOINT VERIFIED.  r638L reseal: project census "
     "5, external 1; no RH claim",
     True),
    ("rh/problem/extraction_joint.pdf", "problem_statement",
     "r473",
     [],
     "compiled PDF of extraction_joint.tex "
     "(recompiled artefact, registered unpinned)", False),

    ("rh/problem/modulus_upgrade.tex", "problem_statement",
     "r474",
     [],
     _R474_STATUS,
     True),
    ("rh/problem/verify_modulus_upgrade.py", "problem_check",
     "r474 companion",
     [],
     "machine check of modulus_upgrade.tex: note tokens "
     "(PARTIAL, SHORT, F2b, scramble, S_eff, Jackson), "
     "smoke run, S_eff(YB)=0, omega pins.  6/6 gates, "
     "final line MODULUS UPGRADE VERIFIED -- PARTIAL",
     True),
    ("rh/problem/modulus_upgrade.pdf", "problem_statement",
     "r474",
     [],
     "compiled PDF of modulus_upgrade.tex "
     "(recompiled artefact, registered unpinned)", False),

    ("rh/problem/arch_rate.tex", "problem_statement",
     "r475",
     [],
     _R475_STATUS,
     True),
    ("rh/problem/verify_arch_rate.py", "problem_check",
     "r475 companion/r638L/r475-repair",
     [],
     "machine check of r475 arch rate: weilArchSide concrete, "
     "Gauss named not sorry, O(Delta^2) rate named (numeric "
     "large-support ratios 3.85-3.99), tendsto proved, "
     "exact-identity historically sorry retained, artefact pins, "
     "historical sorry census 8, numeric probe.  6/6 gates, "
     "final line ARCH RATE VERIFIED.  r638L reseal: arch contract "
     "unasserted, project census 5, external 1.  r475-repair: "
     "fixed archRateConst FALSIFIED (8.0283 > 4.1259765625); "
     "Exists C(f) OPEN; no RH claim",
     True),
    ("rh/problem/arch_rate.pdf", "problem_statement",
     "r475",
     [],
     "compiled PDF of arch_rate.tex "
     "(recompiled artefact, registered unpinned)", False),

    ("rh/problem/crossterm.tex", "problem_statement",
     "r476",
     [],
     _R476_STATUS,
     True),
    ("rh/problem/verify_crossterm.py", "problem_check",
     "r476 companion",
     [],
     "machine check of crossterm.tex: note tokens "
     "(UNCONDITIONAL, H2BALL_POS, scramble, YB, psi tail), "
     "smoke run, YB r_lo>0, L_16 pin.  6/6 gates, "
     "final line CROSSTERM VERIFIED -- "
     "UNCONDITIONAL(L_max=2.7726)",
     True),
    ("rh/problem/crossterm.pdf", "problem_statement",
     "r476",
     [],
     "compiled PDF of crossterm.tex "
     "(recompiled artefact, registered unpinned)", False),

    ("rh/problem/highmode.tex", "problem_statement",
     "r477",
     [],
     _R477_STATUS,
     True),
    ("rh/problem/verify_highmode.py", "problem_check",
     "r477 companion",
     [],
     "machine check of highmode.tex: note tokens "
     "(ARCHITECTURE_STANDS, e^{2L}, Re psi, Schur, YB), "
     "smoke run, t0 and Schur pins.  6/6 gates, "
     "final line HIGHMODE VERIFIED -- "
     "ARCHITECTURE_STANDS(0.3,0.8,1.0)",
     True),
    ("rh/problem/highmode.pdf", "problem_statement",
     "r477",
     [],
     "compiled PDF of highmode.tex "
     "(recompiled artefact, registered unpinned)", False),

    ("rh/problem/endtoend_fixedl.tex", "problem_statement",
     "r478",
     [],
     _R478_STATUS,
     True),
    ("rh/problem/verify_endtoend_fixedl.py", "problem_check",
     "r478 companion",
     [],
     "machine check of endtoend_fixedl.tex: note tokens "
     "(PARTIAL, e^{2L}, Re psi, Hilbert-Schmidt, "
     "almost periodic), smoke run, 2x2/3x3 and K_P pins.  "
     "6/6 gates, final line ENDTOEND_FIXEDL VERIFIED -- "
     "PARTIAL(0.3-even-5x5-PD|tail-Schur)",
     True),
    ("rh/problem/endtoend_fixedl.pdf", "problem_statement",
     "r478",
     [],
     "compiled PDF of endtoend_fixedl.tex "
     "(recompiled artefact, registered unpinned)", False),

    ("rh/problem/lambdastar03.tex", "problem_statement",
     "r479",
     [],
     _R479_STATUS,
     True),
    ("rh/problem/verify_lambdastar03.py", "problem_check",
     "r479 companion",
     [],
     "machine check of lambdastar03.tex: note tokens "
     "(REDUCED, e^{2L}, Re psi, interlacing, YB), "
     "smoke run, t_c and remainder pins.  6/6 gates, "
     "final line LAMBDASTAR03 VERIFIED -- "
     "REDUCED(kappa_high<=1.79e-2 at t*=8,N=5)",
     True),
    ("rh/problem/lambdastar03.pdf", "problem_statement",
     "r479",
     [],
     "compiled PDF of lambdastar03.tex "
     "(recompiled artefact, registered unpinned)", False),

    ("rh/problem/kappa_high.tex", "problem_statement",
     "r480",
     [],
     _R480_STATUS,
     True),
    ("rh/problem/verify_kappa_high.py", "problem_check",
     "r480 companion",
     [],
     "machine check of kappa_high.tex: note tokens "
     "(REDUCED, e^{2L}, refined Schur, Fourier-HS not reused, YB), "
     "smoke run, crude-kill and Schur pins.  6/6 gates, "
     "final line KAPPA_HIGH VERIFIED -- "
     "REDUCED(refined-Schur; crude-kappa_high-killed@0.30)",
     True),
    ("rh/problem/kappa_high.pdf", "problem_statement",
     "r480",
     [],
     "compiled PDF of kappa_high.tex "
     "(recompiled artefact, registered unpinned)", False),

    ("rh/problem/schur_cert.tex", "problem_statement",
     "r481",
     [],
     _R481_STATUS,
     True),
    ("rh/problem/verify_schur_cert.py", "problem_check",
     "r481 companion",
     [],
     "machine check of schur_cert.tex: note tokens "
     "(REDUCED, e^{2L}, IBP, Fourier-HS not reused, YB, "
     "spherical Bessel), smoke run, epsilon pins.  6/6 gates, "
     "final line SCHUR_CERT VERIFIED -- "
     "REDUCED(interval-FT+IBP-tail)",
     True),
    ("rh/problem/schur_cert.pdf", "problem_statement",
     "r481",
     [],
     "compiled PDF of schur_cert.tex "
     "(recompiled artefact, registered unpinned)", False),

    ("rh/problem/carleson_edgeband.tex", "problem_statement",
     "r482",
     [],
     _R482_STATUS,
     True),
    ("rh/problem/verify_carleson_edgeband.py", "problem_check",
     "r482 companion",
     [],
     "machine check of carleson_edgeband.tex: note tokens "
     "(STUCK, 0.666528, 0.274663, STRICT_F_SCRAMBLE_PREMISE_FALSE, "
     "RESTRICTED_LARGE_SIEVE_IS_TARGET, No RH claim), "
     "curve seal, SR pins.  "
     "final line VERIFIED carleson_edgeband "
     "-- STUCK(SR_FAILS_FINITE_CENSUS;"
     "RESTRICTED_LARGE_SIEVE_IS_TARGET;"
     "STRICT_F_SCRAMBLE_PREMISE_FALSE)",
     True),
    ("rh/problem/carleson_edgeband.pdf", "problem_statement",
     "r482",
     [],
     "compiled PDF of carleson_edgeband.tex "
     "(recompiled artefact, registered unpinned)", False),


    ("rh/problem/filon_enclosure.tex", "problem_statement",
     "r483",
     [],
     _R483_STATUS,
     True),
    ("rh/problem/verify_filon_enclosure.py", "problem_check",
     "r483 companion",
     [],
     "machine check of filon_enclosure.tex: note tokens "
     "(REDUCED, e^{2L}, Filon, leftover, Fourier-HS not reused, "
     "Yoshida--Bombieri, sign bookkeeping), smoke run, "
     "deficit pins.  6/6 gates, "
     "final line FILON_ENCLOSURE VERIFIED -- "
     "REDUCED(finite-S-interval-PD; leftover-C-HS=2.74e-2-vs-budget-2.4e-4)",
     True),
    ("rh/problem/filon_enclosure.pdf", "problem_statement",
     "r483",
     [],
     "compiled PDF of filon_enclosure.tex "
     "(recompiled artefact, registered unpinned)", False),


    ("rh/problem/block_completion.tex", "problem_statement",
     "r484",
     [],
     _R484_STATUS,
     True),
    ("rh/problem/verify_block_completion.py", "problem_check",
     "r484 companion",
     [],
     "machine check of block_completion.tex: note tokens "
     "(STUCK, e^{2L}, garbage, QR, leftover, Fourier-HS not reused, "
     "Yoshida--Bombieri), smoke run, deficit pins.  6/6 gates, "
     "final line BLOCK_COMPLETION VERIFIED -- "
     "STUCK(20x-drop-falsified@n96; jets>=10-garbage@n128; QR-IBP-kills-S)",
     True),
    ("rh/problem/block_completion.pdf", "problem_statement",
     "r484",
     [],
     "compiled PDF of block_completion.tex "
     "(recompiled artefact, registered unpinned)", False),

    ("rh/problem/weighted_schur.tex", "problem_statement",
     "r485",
     [],
     _R485_STATUS,
     True),
    ("rh/problem/verify_weighted_schur.py", "problem_check",
     "r485 companion",
     [],
     "machine check of weighted_schur.tex: note tokens "
     "(REDUCED+CHECKPOINT, A-GO, e^{2L}, weighted, "
     "orthocomplement, Fourier-HS not reused, "
     "Yoshida--Bombieri), smoke run, A-GO and S_w pins.  "
     "6/6 gates, "
     "final line WEIGHTED_SCHUR VERIFIED -- "
     "REDUCED(A-GO; finite-S_w-PD; operator-M_inf-open)"
     "+CHECKPOINT",
     True),
    ("rh/problem/weighted_schur.pdf", "problem_statement",
     "r485",
     [],
     "compiled PDF of weighted_schur.tex "
     "(recompiled artefact, registered unpinned)", False),

    ("rh/problem/woodbury_minf.tex", "problem_statement",
     "r486",
     [],
     _R486_STATUS,
     True),
    ("rh/problem/verify_woodbury_minf.py", "problem_check",
     "r486 companion",
     [],
     "machine check of woodbury_minf.tex: note tokens "
     "(REDUCED, enemy-3dim, Birman, Woodbury, e^{2L}, "
     "Fourier-HS not reused, Yoshida--Bombieri), smoke "
     "run, enemy-spectrum and BS pins.  6/6 gates, "
     "final line WOODBURY_MINF VERIFIED -- "
     "REDUCED(enemy-3dim-BS<1; Q_E-Higham; "
     "operator-Rinv-open)",
     True),
    ("rh/problem/woodbury_minf.pdf", "problem_statement",
     "r486",
     [],
     "compiled PDF of woodbury_minf.tex "
     "(recompiled artefact, registered unpinned)", False),

    ("rh/problem/outer_bridges.tex", "problem_statement",
     "r487",
     [],
     _R487_STATUS,
     True),
    ("rh/problem/verify_outer_bridges.py", "problem_check",
     "r487 companion/r638L",
     [],
     "machine check of r487 outer bridges: density decomposition, "
     "sorry-free positivity transfer and zeta interface wrapper, "
     "historically four external bricks, structural smoke.  "
     "6/6 gates, final line OUTER BRIDGES VERIFIED.  r638L "
     "reseal: external census 1, project census 5; no RH claim",
     True),
    ("rh/problem/outer_bridges.pdf", "problem_statement",
     "r487",
     [],
     "compiled PDF of outer_bridges.tex "
     "(recompiled artefact, registered unpinned)", False),

    ("rh/problem/resolvent_solve.tex", "problem_statement",
     "r488",
     [],
     _R488_STATUS,
     True),
    ("rh/problem/verify_resolvent_solve.py", "problem_check",
     "r488 companion",
     [],
     "machine check of resolvent_solve.tex: note tokens "
     "(REDUCED, R-not-coercive, Birman, e^{2L}, "
     "Fourier-HS not reused, Yoshida--Bombieri, r486), "
     "smoke run, shift and G-certificate pins.  6/6 gates, "
     "final line RESOLVENT_SOLVE VERIFIED -- "
     "REDUCED(R-not-coercive; s=0.05-G-cert-N5-BS=0.994; "
     "operator-R-gap-open)",
     True),
    ("rh/problem/resolvent_solve.pdf", "problem_statement",
     "r488",
     [],
     "compiled PDF of resolvent_solve.tex "
     "(recompiled artefact, registered unpinned)", False),

    ("rh/problem/outer_bridges2.tex", "problem_statement",
     "r489",
     [],
     _R489_STATUS,
     True),
    ("rh/problem/verify_outer_bridges2.py", "problem_check",
     "r489 companion/r638L",
     [],
     "machine check of r489 outer bridges: uniform fixed-support "
     "topology, compact L2 witness, comb and polar-integral continuity, "
     "historical one dense completion sorry, structural smoke.  "
     "6/6 gates, final line OUTER BRIDGES 2 VERIFIED.  r638L "
     "reseal: external census 1, project census 5; no RH claim",
     True),
    ("rh/problem/outer_bridges2.pdf", "problem_statement",
     "r489",
     [],
     "compiled PDF of outer_bridges2.tex "
     "(recompiled artefact, registered unpinned)", False),

    ("rh/problem/operator_residual.tex", "problem_statement",
     "r490",
     [],
     _R490_STATUS,
     True),
    ("rh/problem/verify_operator_residual.py", "problem_check",
     "r490 companion",
     [],
     "machine check of operator_residual.tex: note tokens "
     "(STUCK, FINAL_CHECKPOINT, off/s, 5.86, Birman, "
     "e^{2L}, Fourier-HS not reused, Yoshida--Bombieri, "
     "r488, B1, ideas), smoke run, A-nogo and r488 "
     "midpoint pins.  6/6 gates, final line "
     "OPERATOR_RESIDUAL VERIFIED -- "
     "STUCK(off/s=5.86-eats-1000x; "
     "GL-tiny-not-the-certificate;+FINAL_CHECKPOINT)",
     True),
    ("rh/problem/operator_residual.pdf", "problem_statement",
     "r490",
     [],
     "compiled PDF of operator_residual.tex "
     "(recompiled artefact, registered unpinned)", False),

    ("rh/problem/outer_bridges3.tex", "problem_statement",
     "r491",
     [],
     _R491_STATUS,
     True),
    ("rh/problem/verify_outer_bridges3.py", "problem_check",
     "r491 companion/r638L",
     [],
     "machine check of r491 outer bridges: polar sign, concrete full "
     "arch, explicit dyadic construction and support bound, exact pole "
     "hat seam, historically honest unchanged census, structural "
     "smoke.  7/7 gates, final line OUTER BRIDGES 3 VERIFIED -- "
     "REDUCED.  r638L reseal: external census 1, project census 5; "
     "no RH claim",
     True),
    ("rh/problem/outer_bridges3.pdf", "problem_statement",
     "r491",
     [],
     "compiled PDF of outer_bridges3.tex "
     "(recompiled artefact, registered unpinned)", False),

    ("rh/problem/keystone_judgment.tex", "problem_statement",
     "r492",
     [],
     _R492_STATUS,
     True),
    ("rh/problem/keystone_judgment.pdf", "problem_statement",
     "r492",
     [],
     "compiled PDF of keystone_judgment.tex "
     "(recompiled artefact, registered unpinned)", False),

    ("rh/problem/kernel_loewner.tex", "problem_statement",
     "r494",
     [],
     _R494_STATUS,
     True),
    ("rh/problem/verify_kernel_loewner.py", "problem_check",
     "r494 companion",
     [],
     "machine check of kernel_loewner.tex: theorem and claim-boundary "
     "tokens, zero-extension convention, three calibration hits, "
     "booked cutoff, exact HS tail with 2x off-block charge, sealed "
     "smoke rerun.  6/6 gates, final line KERNEL LOEWNER VERIFIED -- "
     "PROVED(c=2.1000e-3)",
     True),
    ("rh/problem/kernel_loewner.pdf", "problem_statement",
     "r494",
     [],
     "compiled PDF of kernel_loewner.tex "
     "(recompiled artefact, registered unpinned)", False),

    ("rh/problem/kernel_redteam.tex", "problem_statement",
     "r495",
     [],
     _R495_STATUS,
     True),
    ("rh/problem/verify_kernel_redteam.py", "problem_check",
     "r495 companion",
     [],
     "machine check of kernel_redteam.tex: independent derivation and "
     "audit tokens, sealed probe contract, exact rational boundary tests, "
     "false-world failure, complete HS block accounting, outward floor "
     "arithmetic, and under-60-second smoke rerun.  6/6 gates, final line "
     "KERNEL REDTEAM VERIFIED -- CONFIRMED(c=2.1000e-3)",
     True),
    ("rh/problem/kernel_redteam.pdf", "problem_statement",
     "r495",
     [],
     "compiled PDF of kernel_redteam.tex "
     "(recompiled artefact, registered unpinned)", False),

    ("rh/problem/kernel_loewner08.tex", "problem_statement",
     "r496", [], _R496_STATUS, True),
    ("rh/problem/verify_kernel_loewner08.py", "problem_check",
     "r496 companion", [],
     "machine check of method-no-go boundary, factor-two prime balance, "
     "G1 calibrations, exact 3x HS tail, prime off-block, and smoke; "
     "final line VERIFIED kernel_loewner08 r496 NO_GO", True),
    ("rh/problem/kernel_loewner08.pdf", "problem_statement",
     "r496", [], "compiled PDF of kernel_loewner08.tex "
     "(recompiled artefact, registered unpinned)", False),

    ("rh/problem/l08_judgment.tex", "problem_statement",
     "r502",
     [],
     _R502_STATUS,
     True),
    ("rh/problem/l08_judgment.pdf", "problem_statement",
     "r502",
     [],
     "compiled PDF of l08_judgment.tex "
     "(recompiled artefact, registered unpinned)", False),

    ("rh/lean/RH/ExternalBridges.lean", "lean_module",
     "r517-r532/r638L",
     [],
     "Lean-only outer-bridge campaign r517-r532 "
     "(commits 4bf75f4f..7fb2dbb0; no sealed probe).  "
     "r517 CONTOUR_IDENTITY contour_identity_fixed_T; "
     "r518 GAP_WIRED exists_gap_height; r519 BC_WIRED "
     "norm_logDeriv_le_of_log_norm_le; r520 LANDAU_SUM_WIRED "
     "gap sum O(log^2 T); r521 LANDAU_WIRED "
     "horizontalEdgeLandauBound theorem; r522 CONTOUR_RESTATED "
     "contour_identity_fixed_T_of; r523 WINDOW+PSI "
     "exists_gap_sequence_landau; r524 LANDAU_A "
     "horizontalEdgeLandauBound_of_gap; r525 PSI_OPEN route A; "
     "r526 PSI_ANCHORED DigammaHorizontalLogBound theorem; "
     "r527 SLIVER_WIRED sliverEdgeBound_negIm; r528 "
     "HORIZONTALS_CLOSED horizontalEdgesTendstoZero; r529 "
     "LEFT_EDGE leftEdgeLogDerivBound; r530 LIMIT_IDENTITY "
     "contourIdentityLimitAlongGaps (spectral side of the "
     "explicit formula); r531 HAT_INVERSION hat_fourier_inversion "
     "(standardExplicitFormula now the spectral pairing); "
     "r532 RIGHT_PRIME rightVerticalIntegral_eq_prime_sum "
     "(2 Lambda/sqrt(n) gauge pinned, unclaimed).  "
     "Theorems (not OPEN): fullWeil_dyadic_sample_convergence, "
     "gridPoleHatIntegralIdentity, fullWeil_channel_continuity.  "
     "Remaining external sorrys: "
     "standard_explicit_formula_identification, "
     "fullWeil_separates_offCritical_zeros.  "
     "Sorry census was 7 through r538 (external 2, internal 5).  "
     "r542-r553 Gabor campaign is a separate module "
     "(RH/GaborSeparation.lean / GaborThetaBound.lean); this "
     "file is unchanged as the compact/honest-Weil carrier.  "
     "Living document.  r638L: corpus assertion retired; honest "
     "theorem retained; external census 2->1.  "
     "NO RH CLAIM",
     False),
    ("rh/lean/RH/Open.lean", "lean_module",
     "r517-r638L",
     [],
     "r517-r532 census blocks plus r542-r612 Gabor-input "
     "notes in RH/Open.lean.  Tracked sorry census 9 -> 8 at "
     "r581 (GaborSeparation 1; GaborExplicitFormula 0; "
     "ExternalBridges still 2); stays 8 through r605; "
     "8 -> 7 at r612 (GaborSeparation 0).  "
     "EF for the Gabor class is a Lean theorem (r581).  "
     "Canonical constant + log + BoundLog2 dominance are "
     "theorems (r571/r575/r583); r573 audit "
     "STATEMENT_WEAKENED (finite proxy).  r584-r588: "
     "tsum<=Closed, unrestricted On/Off-split, and weighted "
     "Bridge-6 identification are theorems; zeta != 0 on "
     "(0,1) real.  r589: window->BoundLog2 bridge theorem; "
     "L2 verdict BRIDGE_A_IS_RH_CORE (singleton route is "
     "not a translation lemma).  r590: existential "
     "arithmetic endpoint + parallel Mathlib chain.  "
     "r591: fixed-packet cofinal only with extremality.  "
     "r592: window-adaptive tail CONDITIONAL (IEEE omega-floor "
     "at extreme near-tie).  r593/r594: outer-tail theorem "
     "(tsum<=exp and tail<eps*E).  r595: three-term glue + "
     "per-T checkpoint; named gap GaborWindowAdaptiveUniformDelta.  "
     "r596-r598: L2 ANKER_TEILWEISE; log-glue theorem; "
     "zeroSide<0 at own packet; Cover is the remaining "
     "geometric rest.  r599/r600 vacuity audit (r602 docs): "
     "old hpos on gaborSpectralFormula is FALSE; live object "
     "gaborZeroSide (hpos*); GaborSpectralToArithmetic_holds "
     "is the pole-sign lemma hat(1)>=0, NOT RH-core; "
     "historical Mathlib wrappers VACUOUS (r600).  "
     "GaborAnchoredWitnessExists NOT asserted.  "
     "Open: GaborAnchoredCoverAt (ordinate clusters), "
     "GaborAnchoredWitnessExists, "
     "GaborWindowAdaptiveUniformDelta (T-uniform delta; "
     "lex host-retune), GaborTruncationUniformNeg, "
     "GaborWeightedTruncationGammaDistinct, "
     "GaborFixedPacketCofinalNegAt (extremality gap), "
     "r612: asserting gabor_separationForAllZeros deleted; "
     "Prop GaborSeparationForAllZeros retained unasserted "
     "(OVERSPECIFIED/believed-false); GaborCountableCriterion "
     "module (r612C: rational-packet iff RH unconditional; "
     "GaborZeroSideContinuous proved).  r610: GaborLowHeightZeroFree "
     "T0 unasserted; gaborSpectralFormula_refuted_of_lowHeight.  "
     "r605-r607/r608/r609/r611/r613 documented in Open.lean "
     "docstrings.  Named open tsum Z(F0)<pi e^{1/8} and "
     "on-line positivity beyond pure family (drop hline).  "
     "r631L: sorry classification R/T/A (census stays 7; no "
     "closure).  r634L docstring: live endpoint is the "
     "unconditional pure EF gabor_explicitFormula_pure plus "
     "prime-side criterion gabor_primeSide_rational_criterion_iff_rh "
     "(RH <=> forall rational (a, omega): POLE - PRIME + ARCH >= 0; "
     "axioms propext/Classical.choice/Quot.sound); remaining EF "
     "brick GaborHatQuarticExplicitRemainder (non-pure quartics).  "
     "Conditional Gabor reduction only; separation stays [O].  "
     "r638L retires the overstrong arch exact-equality and "
     "gauge-mismatched corpus EF asserting theorems to "
     "unasserted Props; project census 7->5; no RH claim.  "
     "NO RH CLAIM",
     True),
    ("rh/lean/RH/Audit.lean", "lean_module",
     "r517-r634L/r638L",
     [],
     "r517-r532 axiom/audit trail of the outer-bridge campaign "
     "(contour identity through RIGHT_PRIME).  r612: #print "
     "lines updated for GaborCountableCriterion; tracked "
     "Gabor/window sorry census 8 -> 7.  r617L: #print lines "
     "updated for CoxeterCompletion and PrimeLogIndependence; "
     "tracked sorry census stays 7; module count 54 -> 56.  "
     "r612C: #print axioms for gaborZeroSideContinuous_holds "
     "and gabor_zeroSide_rational_criterion_iff_rh_unconditional; "
     "named-open list shrinks by one; census stays 7.  "
     "r634L: #print axioms for gabor_explicitFormula_pure and "
     "gabor_primeSide_rational_criterion_iff_rh "
     "(propext/Classical.choice/Quot.sound; no sorryAx); "
     "census stays 7.  r638L: retired assertions are no longer "
     "#printed; project census 7->5.  NO RH CLAIM",
     True),

    # -- frozen libraries the modules embed byte-exact --
    (f"{EXP}/tau_symbolic_probe.py", "frozen_library",
     "r224",
     ["PRIME.PORT.TAU.SYMBOLIC.01"],
     "embedded in v955", True),
    (f"{EXP}/lax_conditioned_probe.py", "frozen_library",
     "r225",
     ["PRIME.PORT.LAX2.CONDITIONED.01"],
     "embedded in v955", True),
    (f"{EXP}/hirota_sign_probe.py", "frozen_library",
     "r226",
     ["PRIME.PORT.HIROTA.SIGN.01"],
     "embedded in v955; library for v956/v959", True),
    (f"{EXP}/fermiedge_classify_probe.py", "frozen_library",
     "r227",
     [],
     "builder library for v956 (classification round)", True),
    (f"{EXP}/holedual_probe.py", "frozen_library",
     "r228",
     ["PRIME.PORT.SIGNEDMOMENT.HOLEDUAL.01"],
     "embedded in v956", True),
    (f"{EXP}/pontryagin_maxpos_probe.py", "frozen_library",
     "r229",
     ["PRIME.PORT.PONTRYAGIN.MAXPOS.01"],
     "embedded in v956", True),
    (f"{EXP}/jfraction_probe.py", "frozen_library",
     "r230",
     ["PRIME.PORT.FREEMOMENT.JFRACTION.01"],
     "embedded in v956", True),
    (f"{EXP}/rhp_midpoint_probe.py", "frozen_library",
     "r231",
     ["PRIME.PORT.RHP.FREEMOMENT.MIDPOINT.01"],
     "embedded in v956", True),
    (f"{EXP}/szego_equilibrium_probe.py", "frozen_library",
     "r232a",
     [],
     "frozen library (equilibrium QP) for v959 probes", True),
    (f"{EXP}/principal_bessel_probe.py", "frozen_library",
     "r243",
     [],
     "frozen library (budget definition B = S_{N-2} + 5/7)", True),
    (f"{EXP}/bordered_hankel_probe.py", "frozen_library",
     "r244",
     ["PRIME.PORT.RHP.BORDERED.READOUT.01"],
     "embedded in v958", True),
    (f"{EXP}/bordered_finite_rank_probe.py", "frozen_library",
     "r245",
     [],
     "embedded in v958 (Schlesinger rank-1 insertion)", True),
    (f"{EXP}/border_centering_probe.py", "frozen_library",
     "r248",
     [],
     "embedded in v958 (centering congruence)", True),
    # -- living documents (registered, unpinned) --
    (f"{VER}/status_ledger.csv", "ledger",
     "-",
     ["(all PRIME.* rows; the ledger wins on any status disagreement)"],
     "living document -- drift is expected, reported as INFO", False),
    ("tfpt_prime_front.tex", "program_prose",
     "-",
     [],
     "living document -- the program prose of the prime front", False),
    ("experiments/next.txt", "campaign_notes",
     "notes DLXXIX-DXCVII",
     [],
     "living document -- German campaign notes (newest at bottom)", False),
    (f"{EXP}/local_gap_carleson_probe.py", "sealed_probe",
     "r358",
     [],
     _R358_STATUS,
     True),
    (f"{EXP}/schur_wronskian_dual_probe.py", "sealed_probe",
     "r359",
     [],
     _R359_STATUS,
     True),
    (f"{EXP}/critical_saturation_probe.py", "sealed_probe",
     "r360",
     [],
     _R360_STATUS,
     True),
    (f"{EXP}/mean_sieve_floor_probe.py", "sealed_probe",
     "r361",
     [],
     _R361_STATUS,
     True),
    (f"{EXP}/augmented_borodin_duality_probe.py", "sealed_probe",
     "r362",
     [],
     _R362_STATUS,
     True),
    (f"{EXP}/canonical_sturm_induction_probe.py", "sealed_probe",
     "r363",
     [],
     _R363_STATUS,
     True),
    (f"{EXP}/edge_gap_ms_probe.py", "sealed_probe",
     "r366",
     [],
     _R366_STATUS,
     True),
    (f"{EXP}/final_two_rank_inertia_probe.py", "sealed_probe",
     "r367",
     [],
     _R367_STATUS,
     True),
    (f"{EXP}/weighted_l2_t1_probe.py", "sealed_probe",
     "r368",
     [],
     _R368_STATUS,
     True),
    (f"{EXP}/mixed_haynsworth_probe.py", "sealed_probe",
     "r369",
     [],
     _R369_STATUS,
     True),
    (f"{EXP}/matrix_weyl_index_probe.py", "sealed_probe",
     "r370",
     [],
     _R370_STATUS,
     True),
    (f"{EXP}/compound_cd_wedge_probe.py", "sealed_probe",
     "r371",
     [],
     _R371_STATUS,
     True),
    (f"{EXP}/source_prufer_one_defect_probe.py", "sealed_probe",
     "r372",
     [],
     _R372_STATUS,
     True),
    (f"{EXP}/postcap_pivots_probe.py", "sealed_probe",
     "r377",
     [],
     _R377_STATUS,
     True),
    (f"{EXP}/g_eps_lemma_probe.py", "sealed_probe",
     "r381",
     [],
     _R381_STATUS,
     True),
    (f"{EXP}/pivot_entry_lemma_probe.py", "sealed_probe",
     "r382",
     [],
     _R382_STATUS,
     True),
    (f"{EXP}/compose_premises_probe.py", "sealed_probe",
     "r383",
     [],
     _R383_STATUS,
     True),
    (f"{EXP}/christoffel_quiet_probe.py", "sealed_probe",
     "r385",
     [],
     _R385_STATUS,
     True),
    (f"{EXP}/compose_premises2_probe.py", "sealed_probe",
     "r386",
     [],
     _R386_STATUS,
     True),
    (f"{EXP}/coherence_assist_probe.py", "sealed_probe",
     "r387",
     [],
     _R387_STATUS,
     True),
    (f"{EXP}/delta_deformation_probe.py", "sealed_probe",
     "r388",
     [],
     _R388_STATUS,
     True),
    (f"{EXP}/weyl_energy_probe.py", "sealed_probe",
     "r389",
     [],
     _R389_STATUS,
     True),
    (f"{EXP}/g_eps_mu_probe.py", "sealed_probe",
     "r390",
     [],
     _R390_STATUS,
     True),
    (f"{EXP}/construction_pure_rl_probe.py", "sealed_probe",
     "r391",
     [],
     _R391_STATUS,
     True),
    (f"{EXP}/deletion_transform_probe.py", "sealed_probe",
     "r392",
     [],
     _R392_STATUS,
     True),
    (f"{EXP}/tau_field_probe.py", "sealed_probe",
     "r393",
     [],
     _R393_STATUS,
     True),
    (f"{EXP}/sign_schur_probe.py", "sealed_probe",
     "r394",
     [],
     _R394_STATUS,
     True),
    (f"{EXP}/three_gap_mask_probe.py", "sealed_probe",
     "r395",
     [],
     _R395_STATUS,
     True),
    (f"{EXP}/isolation_lemma_probe.py", "sealed_probe",
     "r396",
     [],
     _R396_STATUS,
     True),
    (f"{EXP}/high_moment_inertia_probe.py", "sealed_probe",
     "r398",
     [],
     _R398_STATUS,
     True),
    (f"{EXP}/source_weyl_energy_probe.py", "sealed_probe",
     "r399",
     [],
     _R399_STATUS,
     True),
    (f"{EXP}/bulk_one_defect_probe.py", "sealed_probe",
     "r400",
     [],
     _R400_STATUS,
     True),
    (f"{EXP}/edge_signature_probe.py", "sealed_probe",
     "r401",
     [],
     _R401_STATUS,
     True),
    (f"{EXP}/p1_construction_probe.py", "sealed_probe",
     "r403",
     [],
     _R403_STATUS,
     True),
    (f"{EXP}/one_defect_gram_probe.py", "sealed_probe",
     "r404",
     [],
     _R404_STATUS,
     True),
    (f"{EXP}/edge_contractive_lift_probe.py", "sealed_probe",
     "r405",
     [],
     _R405_STATUS,
     True),
    (f"{EXP}/dual_intertwiner_probe.py", "sealed_probe",
     "r407",
     [],
     _R407_STATUS,
     True),
    (f"{EXP}/c_threshold_probe.py", "sealed_probe",
     "r408",
     [],
     _R408_STATUS,
     True),
    (f"{EXP}/borodin_birkhoff_intertwiner_probe.py", "sealed_probe",
     "r409",
     [],
     _R409_STATUS,
     True),
    (f"{EXP}/hole_nyquist_probe.py", "sealed_probe",
     "r410",
     [],
     _R410_STATUS,
     True),
    (f"{EXP}/threshold_identity_probe.py", "sealed_probe",
     "r411",
     [],
     _R411_STATUS,
     True),
    (f"{EXP}/hole_top_mode_probe.py", "sealed_probe",
     "r413",
     [],
     _R413_STATUS,
     True),
    (f"{EXP}/top_mode_edge_probe.py", "sealed_probe",
     "r415",
     [],
     _R415_STATUS,
     True),
    (f"{EXP}/debranges_index_probe.py", "sealed_probe",
     "r416",
     [],
     _R416_STATUS,
     True),
    (f"{EXP}/source_sch_sign_probe.py", "sealed_probe",
     "r417",
     [],
     _R417_STATUS,
     True),
    (f"{EXP}/phi_bb_sign_probe.py", "sealed_probe",
     "r418",
     [],
     _R418_STATUS,
     True),
    (f"{EXP}/vacuous_overflow_probe.py", "sealed_probe",
     "r419",
     [],
     _R419_STATUS,
     True),
    (f"{EXP}/cj_sigma_probe.py", "sealed_probe",
     "r420",
     [],
     _R420_STATUS,
     True),
    (f"{EXP}/reserve_limit_probe.py", "sealed_probe",
     "r421",
     [],
     _R421_STATUS,
     True),
    (f"{EXP}/sigma_limit_probe.py", "sealed_probe",
     "r422",
     [],
     _R422_STATUS,
     True),
    (f"{EXP}/den_limit_probe.py", "sealed_probe",
     "r423",
     [],
     _R423_STATUS,
     True),
    (f"{EXP}/gamma_chain_probe.py", "sealed_probe",
     "r424",
     [],
     _R424_STATUS,
     True),
    (f"{EXP}/cross_chain_gamma_probe.py", "sealed_probe",
     "r425",
     [],
     _R425_STATUS,
     True),
    (f"{EXP}/campaign_audit_probe.py", "sealed_probe",
     "r427",
     [],
     _R427_STATUS,
     True),
    (f"{EXP}/qn_reopened_probe.py", "sealed_probe",
     "r428",
     [],
     _R428_STATUS,
     True),
    (f"{EXP}/zloc_head_probe.py", "sealed_probe",
     "r429",
     [],
     _R429_STATUS,
     True),
    (f"{EXP}/source_potapov_probe.py", "sealed_probe",
     "r431",
     [],
     _R431_STATUS,
     True),
    (f"{EXP}/r431_audit_probe.py", "sealed_probe",
     "r431-AUDIT",
     [],
     _R431_AUDIT_STATUS,
     True),
    (f"{EXP}/edge_redheffer_probe.py", "sealed_probe",
     "r433",
     [],
     _R433_STATUS,
     True),
    (f"{EXP}/p1_overload_probe.py", "sealed_probe",
     "r435",
     [],
     _R435_STATUS,
     True),
    (f"{EXP}/p2_determinant_probe.py", "sealed_probe",
     "r436",
     [],
     _R436_STATUS,
     True),
    (f"{EXP}/evolutionary_certificate_probe.py", "sealed_probe",
     "r438",
     [],
     _R438_STATUS,
     True),
    (f"{EXP}/residual_loewner_probe.py", "sealed_probe",
     "r439",
     [],
     _R439_STATUS,
     True),
    (f"{EXP}/mean_tau_index_probe.py", "sealed_probe",
     "r440",
     [],
     _R440_STATUS,
     True),
    (f"{EXP}/diag_lifts_loewner_probe.py", "sealed_probe",
     "r441",
     [],
     _R441_STATUS,
     True),
    (f"{EXP}/block_mean_probe.py", "sealed_probe",
     "r442",
     [],
     _R442_STATUS,
     True),
    (f"{EXP}/delta_floor_probe.py", "sealed_probe",
     "r443",
     [],
     _R443_STATUS,
     True),
    (f"{EXP}/signed_border_mean_probe.py", "sealed_probe",
     "r444",
     [],
     _R444_STATUS,
     True),
    (f"{EXP}/deep_builder_probe.py", "sealed_probe",
     "r445",
     [],
     _R445_STATUS,
     True),
    (f"{EXP}/deep_abd_probe.py", "sealed_probe",
     "r446",
     [],
     _R446_STATUS,
     True),
    (f"{EXP}/exact_atom_probe.py", "sealed_probe",
     "r447",
     [],
     _R447_STATUS,
     True),
    (f"{EXP}/exact_band_probe.py", "sealed_probe",
     "r448",
     [],
     _R448_STATUS,
     True),
    (f"{EXP}/flip_vs_stab_probe.py", "sealed_probe",
     "r449",
     [],
     _R449_STATUS,
     True),
    (f"{EXP}/prefix_mincut_probe.py", "sealed_probe",
     "r450",
     [],
     _R450_STATUS,
     True),
    (f"{EXP}/nstab_transition_probe.py", "sealed_probe",
     "r451",
     [],
     _R451_STATUS,
     True),
    (f"{EXP}/plateau_theorem_probe.py", "sealed_probe",
     "r452",
     [],
     _R452_STATUS,
     True),
    (f"{EXP}/border_mass_probe.py", "sealed_probe",
     "r453",
     [],
     _R453_STATUS,
     True),
    (f"{EXP}/limit_object_probe.py", "sealed_probe",
     "r454",
     [],
     _R454_STATUS,
     True),
    (f"{EXP}/arch_chain_probe.py", "sealed_probe",
     "r455",
     [],
     _R455_STATUS,
     True),
    (f"{EXP}/vacuity_redteam_probe.py", "sealed_probe",
     "r456",
     [],
     _R456_STATUS,
     True),
    (f"{EXP}/jp_increment_probe.py", "sealed_probe",
     "r457",
     [],
     _R457_STATUS,
     True),
    (f"{EXP}/cofinal_family_probe.py", "sealed_probe",
     "r458",
     [],
     _R458_STATUS,
     True),
    (f"{EXP}/fullcomb_cleanup_probe.py", "sealed_probe",
     "r459",
     [],
     _R459_STATUS,
     True),
    (f"{EXP}/race_proof_probe.py", "sealed_probe",
     "r460",
     [],
     _R460_STATUS,
     True),
    (f"{EXP}/narrowband_weil_probe.py", "sealed_probe",
     "r461/r638L",
     [],
     _R461_STATUS,
     True),
    (f"{EXP}/gapmap_probe.py", "sealed_historical_probe",
     "r462",
     [],
     _R462_STATUS,
     True),
    (f"{EXP}/lean_fidelity_probe.py", "sealed_probe",
     "r463/r638L",
     [],
     _R463_STATUS + _R638L_RESEAL_NOTE,
     True),
    (f"{EXP}/inner_bridges_probe.py", "sealed_probe",
     "r464/r638L",
     [],
     _R464_STATUS + _R638L_RESEAL_NOTE,
     True),
    (f"{EXP}/overlap_mechanism_probe.py", "sealed_probe",
     "r467",
     [],
     _R467_STATUS,
     True),
    (f"{EXP}/octave_renorm_probe.py", "sealed_probe",
     "r468",
     [],
     _R468_STATUS,
     True),
    (f"{EXP}/quadrep_probe.py", "sealed_probe",
     "r470",
     [],
     _R470_STATUS,
     True),
    (f"{EXP}/classical_cert_probe.py", "sealed_probe",
     "r471",
     [],
     _R471_STATUS,
     True),
    (f"{EXP}/extraction_joint_probe.py", "sealed_probe",
     "r473",
     [],
     _R473_STATUS,
     True),
    (f"{EXP}/modulus_upgrade_probe.py", "sealed_probe",
     "r474",
     [],
     _R474_STATUS,
     True),
    (f"{EXP}/arch_rate_probe.py", "sealed_probe",
     "r475/r638L",
     [],
     _R475_STATUS + _R638L_RESEAL_NOTE,
     True),
    (f"{EXP}/crossterm_probe.py", "sealed_probe",
     "r476",
     [],
     _R476_STATUS,
     True),
    (f"{EXP}/highmode_probe.py", "sealed_probe",
     "r477",
     [],
     _R477_STATUS,
     True),
    (f"{EXP}/endtoend_fixedl_probe.py", "sealed_probe",
     "r478",
     [],
     _R478_STATUS,
     True),
    (f"{EXP}/lambdastar03_probe.py", "sealed_probe",
     "r479",
     [],
     _R479_STATUS,
     True),
    (f"{EXP}/kappa_high_probe.py", "sealed_probe",
     "r480",
     [],
     _R480_STATUS,
     True),
    (f"{EXP}/schur_cert_probe.py", "sealed_probe",
     "r481",
     [],
     _R481_STATUS,
     True),
    (f"{EXP}/carleson_edgeband_probe.py", "sealed_probe",
     "r482",
     [],
     _R482_STATUS,
     True),
    (f"{EXP}/filon_enclosure_probe.py", "sealed_probe",
     "r483",
     [],
     _R483_STATUS,
     True),
    (f"{EXP}/block_completion_probe.py", "sealed_probe",
     "r484",
     [],
     _R484_STATUS,
     True),
    (f"{EXP}/weighted_schur_probe.py", "sealed_probe",
     "r485",
     [],
     _R485_STATUS,
     True),
    (f"{EXP}/woodbury_minf_probe.py", "sealed_probe",
     "r486",
     [],
     _R486_STATUS,
     True),
    (f"{EXP}/outer_bridges_probe.py", "sealed_probe",
     "r487/r638L",
     [],
     _R487_STATUS + _R638L_RESEAL_NOTE,
     True),
    (f"{EXP}/resolvent_solve_probe.py", "sealed_probe",
     "r488",
     [],
     _R488_STATUS,
     True),
    (f"{EXP}/outer_bridges2_probe.py", "sealed_probe",
     "r489/r638L",
     [],
     _R489_STATUS + _R638L_RESEAL_NOTE,
     True),
    (f"{EXP}/operator_residual_probe.py", "sealed_probe",
     "r490",
     [],
     _R490_STATUS,
     True),
    (f"{EXP}/outer_bridges3_probe.py", "sealed_probe",
     "r491/r638L",
     [],
     _R491_STATUS + _R638L_RESEAL_NOTE,
     True),
    (f"{EXP}/kernel_loewner_probe.py", "sealed_probe",
     "r494",
     [],
     _R494_STATUS,
     True),
    (f"{EXP}/kernel_redteam_probe.py", "sealed_probe",
     "r495",
     [],
     _R495_STATUS,
     True),
    (f"{EXP}/kernel_loewner08_probe.py", "sealed_probe",
     "r496",
     [],
     _R496_STATUS,
     True),
    (f"{EXP}/weil_separation_redteam_probe.py", "sealed_probe",
     "r535",
     [],
     _R535_STATUS,
     True),
    (f"{EXP}/kernel_loewner_window_probe.py", "sealed_probe",
     "r536",
     [],
     _R536_STATUS,
     True),
    (f"{EXP}/honest_contour_audit_probe.py", "sealed_probe",
     "r537",
     [],
     _R537_STATUS,
     True),
    (f"{EXP}/weil_gaussian_separation_probe.py", "sealed_probe",
     "r539",
     [],
     _R539_STATUS,
     True),
    (f"{EXP}/weil_online_null_separation_probe.py", "sealed_probe",
     "r540",
     [],
     _R540_STATUS,
     True),
    (f"{EXP}/weil_gabor_separation_probe.py", "sealed_probe",
     "r541",
     [],
     _R541_STATUS,
     True),
    ("rh/lean/RH.lean", "lean_module",
     "r542-r617L",
     [],
     _RH_ROOT_STATUS,
     True),
    ("rh/lean/RH/GaborSeparation.lean", "lean_module",
     "r542-r634L",
     [],
     _R542_STATUS,
     True),
    ("rh/lean/RH/GaborIntegral.lean", "lean_module",
     "r543",
     [],
     _R543_STATUS,
     True),
    ("rh/lean/RH/GaborInequality.lean", "lean_module",
     "r544/r552/r579",
     [],
     _R552_INEQ_STATUS,
     True),
    (f"{EXP}/gabor_uniform_inequality_probe.py", "sealed_probe",
     "r544",
     [],
     _R544_STATUS,
     True),
    ("rh/lean/RH/ZeroIncrement.lean", "lean_module",
     "r546",
     [],
     _R546_STATUS,
     True),
    (f"{EXP}/weil_gabor_explicit_formula_probe.py", "sealed_probe",
     "r548",
     [],
     _R548_STATUS,
     True),
    (f"{EXP}/gabor_density_transfer_probe.py", "sealed_probe",
     "r549",
     [],
     _R549_STATUS,
     True),
    (f"{EXP}/gabor_extremal_selection_probe.py", "sealed_probe",
     "r551",
     [],
     _R551_STATUS,
     True),
    ("rh/lean/RH/GaborThetaBound.lean", "lean_module",
     "r552/r579",
     [],
     _R552_STATUS,
     True),
    (f"{EXP}/gabor_config_first_probe.py", "sealed_probe",
     "r553",
     [],
     _R553_STATUS,
     True),
    (f"{EXP}/gabor_mixture_witness_probe.py", "sealed_probe",
     "r554",
     [],
     _R554_STATUS,
     True),
    ("rh/lean/RH/GaborHatAnalytic.lean", "lean_module",
     "r555/r587",
     [],
     _R555_STATUS,
     True),
    ("rh/lean/RH/GaborZeroSummable.lean", "lean_module",
     "r557/r587",
     [],
     _R557_SUM_STATUS,
     True),
    ("rh/lean/RH/GaborHorizontalEdges.lean", "lean_module",
     "r557",
     [],
     _R557_HORIZ_STATUS,
     True),
    ("rh/lean/RH/GaborContourResidue.lean", "lean_module",
     "r557/r631L",
     [],
     _R557_CONT_STATUS,
     True),
    ("rh/lean/RH/GaborExplicitFormula.lean", "lean_module",
     "r558/r564/r581/r634L",
     [],
     _R558_EF_STATUS,
     True),
    (f"{EXP}/gabor_honest_weil_game_probe.py", "sealed_probe",
     "r560",
     [],
     _R560_STATUS,
     True),
    (f"{EXP}/gabor_uniform_dominance_probe.py", "sealed_probe",
     "r561",
     [],
     _R561_STATUS,
     True),
    ("rh/lean/RH/GaborDominance.lean", "lean_module",
     "r562/r568/r571/r589",
     [],
     _R562_DOM_STATUS,
     True),
    (f"{EXP}/gabor_dominance_redteam_probe.py", "sealed_probe",
     "r563",
     [],
     _R563_STATUS,
     True),
    ("rh/lean/RH/GaborVertical.lean", "lean_module",
     "r564/r581",
     [],
     _R564_VERT_STATUS,
     True),
    (f"{EXP}/gabor_scramble_gate_probe.py", "sealed_probe",
     "r565",
     [],
     _R565_STATUS,
     True),
    (f"{EXP}/gabor_canonical_dominance_probe.py", "sealed_probe",
     "r567",
     [],
     _R567_STATUS,
     True),
    ("rh/lean/RH/GaborLeftVertical.lean", "lean_module",
     "r570",
     [],
     _R570_LEFT_STATUS,
     True),
    ("rh/lean/RH/GaborAutocorrelation.lean", "lean_module",
     "r572",
     [],
     _R572_ACF_STATUS,
     True),
    ("rh/lean/RH/GaborVerticalLimit.lean", "lean_module",
     "r576",
     [],
     _R576_VLIM_STATUS,
     True),
    ("rh/lean/RH/GaborArchDigamma.lean", "lean_module",
     "r577",
     [],
     _R577_DIG_STATUS,
     True),
    ("rh/lean/RH/GaborArchContour.lean", "lean_module",
     "r578/r581",
     [],
     _R578_ARCH_STATUS,
     True),
    ("rh/lean/RH/GaborDominanceProof.lean", "lean_module",
     "r569/r597",
     [],
     _R569_PROOF_STATUS,
     True),
    ("rh/lean/RH/GaborDominanceAssembly.lean", "lean_module",
     "r571/r597",
     [],
     _R571_ASM_STATUS,
     True),
    ("rh/lean/RH/GaborDominanceLog.lean", "lean_module",
     "r574/r575/r597/r598",
     [],
     _R574_LOG_STATUS,
     True),
    ("rh/lean/RH/GaborSpectralBridge.lean", "lean_module",
     "r579-r589",
     [],
     _R579_SPEC_STATUS,
     True),
    ("rh/lean/RH/GaborFEMultiplicity.lean", "lean_module",
     "r582/r585",
     [],
     _R582_FE_STATUS,
     True),
    ("rh/lean/RH/GaborDominanceLog2.lean", "lean_module",
     "r582/r583/r589/r597",
     [],
     _R583_LOG2_STATUS,
     True),
    ("rh/lean/RH/GaborArithmeticSeparator.lean", "lean_module",
     "r590/r600/r605A",
     [],
     _R590_ARITH_STATUS,
     True),
    (f"{EXP}/gabor_fixed_packet_cofinal_probe.py", "sealed_probe",
     "r591",
     [],
     _R591_STATUS,
     True),
    (f"{EXP}/gabor_window_adaptive_tail_probe.py", "sealed_probe",
     "r592",
     [],
     _R592_STATUS,
     True),
    ("rh/lean/RH/GaborOuterTail.lean", "lean_module",
     "r593/r594/r600",
     [],
     _R593_STATUS,
     True),
    ("rh/lean/RH/GaborWindowGlue.lean", "lean_module",
     "r595",
     [],
     _R595_STATUS,
     True),
    ("rh/lean/RH/GaborAnchoredWitness.lean", "lean_module",
     "r596-r600",
     [],
     _R596_STATUS,
     True),
    (f"{EXP}/gabor_weil_positivity_subfamily_probe.py", "sealed_probe",
     "r601",
     [],
     _R601_STATUS,
     True),
    (f"{EXP}/prime_inequality_evosearch_probe.py", "sealed_probe",
     "r603",
     [],
     _R603_STATUS,
     True),
    (f"{EXP}/tfpt_spectrum_zero_crosscorr_probe.py", "sealed_probe",
     "r604",
     [],
     _R604_STATUS,
     True),
    (f"{EXP}/gabor_exposed_orbit_probe.py", "sealed_probe",
     "r605N",
     [],
     _R605N_STATUS,
     True),
    ("rh/lean/RH/GaborExposedOrbit.lean", "lean_module",
     "r605B/r605C",
     [],
     _R605BC_STATUS,
     True),
    (f"{EXP}/connes_prolate_residual_gap_probe.py", "sealed_probe",
     "r606",
     [],
     _R606_STATUS,
     True),
    (f"{EXP}/event_lindblad_twokey_probe.py", "sealed_probe",
     "r607",
     [],
     _R607_STATUS,
     True),
    (f"{EXP}/gabor_tropical_heat_probe.py", "sealed_probe",
     "r608",
     [],
     _R608_STATUS,
     True),
    (f"{EXP}/e8_directed_readout_probe.py", "sealed_probe",
     "r609",
     [],
     _R609_STATUS,
     True),
    (f"{EXP}/connes_observable_aubin_nitsche_probe.py", "sealed_probe",
     "r611",
     [],
     _R611_STATUS,
     True),
    ("rh/lean/RH/GaborCountableCriterion.lean", "lean_module",
     "r612C/r634L",
     [],
     _R612C_STATUS,
     True),
    (f"{EXP}/prime_e8_ordered_herglotz_probe.py", "sealed_probe",
     "r613",
     [],
     _R613_STATUS,
     True),
    (f"{EXP}/semilocal_firststep_probe.py", "sealed_probe",
     "r615",
     [],
     _R615_STATUS,
     True),
    (f"{EXP}/inertia_highermoment_probe.py", "sealed_probe",
     "r616",
     [],
     _R616_STATUS,
     True),
    (f"{EXP}/e8_coxeter_euler_completion_probe.py", "sealed_probe",
     "r617",
     [],
     _R617_STATUS,
     True),
    (f"{EXP}/jensen_compiler_rigidity_probe.py", "sealed_probe",
     "r618",
     [],
     _R618_STATUS,
     True),
    ("rh/lean/RH/CoxeterCompletion.lean", "lean_module",
     "r617L",
     [],
     _R617L_COX_STATUS,
     True),
    ("rh/lean/RH/PrimeLogIndependence.lean", "lean_module",
     "r617L",
     [],
     _R617L_LOG_STATUS,
     True),
    (f"{EXP}/support_relay_census_probe.py", "sealed_probe",
     "r619",
     [],
     _R619_STATUS,
     True),
    (f"{EXP}/p2_reflection_factor_probe.py", "sealed_probe",
     "r620",
     [],
     _R620_STATUS,
     True),
    (f"{EXP}/p2_digamma_duplication_probe.py", "sealed_probe",
     "r621",
     [],
     _R621_STATUS,
     True),
    (f"{EXP}/support_darboux_probe.py", "sealed_probe",
     "r622",
     [],
     _R622_STATUS,
     True),
    (f"{EXP}/semilocal_p2_dilation_probe.py", "sealed_probe",
     "r623",
     [],
     _R623_STATUS,
     True),
    (f"{EXP}/iiks_vanishing_metric_probe.py", "sealed_probe",
     "r625",
     [],
     _R625_STATUS,
     True),
    (f"{EXP}/xi_finitefree_collision_probe.py", "sealed_probe",
     "r626",
     [],
     _R626_STATUS,
     True),
    (f"{EXP}/af_twomoment_optimizer_probe.py", "sealed_probe",
     "r627",
     [],
     _R627_STATUS,
     True),
    (f"{EXP}/window_box_verifier_probe.py", "sealed_probe",
     "r628",
     [],
     _R628_STATUS,
     True),
    (f"{EXP}/certificate_class_atlas_probe.py", "sealed_probe",
     "r629",
     [],
     _R629_STATUS,
     True),
    (f"{EXP}/margin_law_symreg_probe.py", "sealed_probe",
     "r630",
     [],
     _R630_STATUS,
     True),
    (f"{EXP}/jet_deflated_ldet_probe.py", "sealed_probe",
     "r632",
     [],
     _R632_STATUS,
     True),
    (f"{EXP}/frontier_followups_probe.py", "sealed_probe",
     "r633",
     [],
     _R633_STATUS,
     True),
    (f"{EXP}/relay_lead_precision_probe.py", "sealed_probe",
     "r635",
     [],
     _R635_STATUS,
     True),
    (f"{EXP}/relay_lead_law_probe.py", "sealed_probe",
     "r636",
     [],
     _R636_STATUS,
     True),
    (f"{EXP}/relay_vote_map_probe.py", "sealed_probe",
     "r637",
     [],
     _R637_STATUS,
     True),
    (f"{EXP}/gabor_first_contact_selberg_probe.py", "sealed_probe",
     "r638",
     [],
     _R638_STATUS,
     True),
    (f"{EXP}/lamzouri_hilbert_adjudication_probe.py", "sealed_probe",
     "r639",
     [],
     _R639_STATUS,
     True),
    ("rh/lean/RH/SelectedArchErrorQuadraticRateClassical.lean", "lean_module",
     "r475-repair",
     [],
     _R475_REPAIR_STATUS,
     True),
]



def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def _normalized(doc):
    """Copy of an inventory doc with the volatile fields removed
    (the 'generated' date; sha256/bytes of pin=false living docs)."""
    d = {k: v for k, v in doc.items() if k != "generated"}
    ents = []
    for e in d.get("entries", []):
        e = dict(e)
        if not e.get("pin"):
            e.pop("sha256", None)
            e.pop("bytes", None)
        ents.append(e)
    d["entries"] = ents
    return d


def main():
    argv = set(sys.argv[1:])
    check = "--check" in argv
    force = "--force" in argv
    entries = []
    missing = []
    for rel, role, rnd, ids, status, pin in ENTRIES:
        p = os.path.join(REPO, rel)
        if not os.path.isfile(p):
            missing.append(rel)
            continue
        entries.append({
            "path": rel,
            "role": role,
            "round": rnd,
            "ledger_ids": ids,
            "status": status,
            "pin": pin,
            "sha256": sha256(p),
            "bytes": os.path.getsize(p),
        })

    old = None
    if os.path.isfile(OUT):
        with open(OUT, encoding="utf-8") as f:
            old = json.load(f)

    # no-row-loss guard: a stale ENTRIES head must never silently
    # drop rows that parallel syncs added to the actual inventory.
    # (--check never writes; dropped rows show up in its diff report.)
    if old is not None and not check:
        new_paths = {e["path"] for e in entries}
        lost = [e["path"] for e in old.get("entries", [])
                if e["path"] not in new_paths]
        if lost:
            print("ROW-LOSS GUARD: regeneration would DROP %d row(s) "
                  "present in %s:" % (len(lost), OUT))
            for p in lost:
                print("  -", p)
            if not force:
                print("REFUSING to write.  The committed INVENTORY.json "
                      "is the truth (ledger-wins): sync the ENTRIES head "
                      "in this script first, or pass --force if the "
                      "removal is intentional.")
                return 2
            print("--force given: writing despite row loss.")

    doc = {
        "workspace": "rh/",
        "generated": date.today().isoformat(),
        "claim_boundary": ("Research documentation.  NOT evidence for or "
                           "against the Riemann Hypothesis in either "
                           "direction.  NO RH CLAIM.  Mincut base 4 / "
                           "refined 5.  The status ledger wins on any "
                           "disagreement."),
        "note": ("rh/ references these files, it never copies them.  "
                 "pin=true entries are frozen: a SHA-256 mismatch is a "
                 "FAIL in rh/verification/run_rh.py.  pin=false entries "
                 "are living documents: drift is reported as INFO."),
        "entries": entries,
    }

    if check:
        if old is None:
            print("--check: %s does not exist" % OUT)
            return 1
        if _normalized(doc) == _normalized(old):
            print("--check: regeneration matches %s  (%d entries, "
                  "%d pinned; only volatile fields may differ)" % (
                      OUT, len(entries),
                      sum(1 for e in entries if e["pin"])))
            return 1 if missing else 0
        print("--check: regeneration DIFFERS from %s:" % OUT)
        old_by = {e["path"]: e for e in old.get("entries", [])}
        new_by = {e["path"]: e for e in entries}
        for p in old_by:
            if p not in new_by:
                print("  DROPPED:", p)
        for p in new_by:
            if p not in old_by:
                print("  ADDED:", p)
        if ([e["path"] for e in old.get("entries", []) if e["path"] in new_by]
                != [e["path"] for e in entries if e["path"] in old_by]):
            print("  ORDER differs for common paths")
        for e_new in entries:
            e_old = old_by.get(e_new["path"])
            if e_old is None:
                continue
            for k in ("role", "round", "ledger_ids", "status", "pin"):
                if e_old.get(k) != e_new[k]:
                    print("  FIELD %s differs: %s" % (k, e_new["path"]))
            if e_new["pin"] and (e_old.get("sha256") != e_new["sha256"]
                                 or e_old.get("bytes") != e_new["bytes"]):
                print("  PINNED sha256/bytes differ: %s" % e_new["path"])
        return 1

    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(doc, f, indent=2, ensure_ascii=False)
        f.write("\n")
    print("wrote %s  (%d entries, %d pinned)" % (
        OUT, len(entries), sum(1 for e in entries if e["pin"])))
    try:
        os.system("%s %s && %s %s --quiet" % (sys.executable, os.path.join(REPO, "rh", "catalog", "autodraft.py"), sys.executable, os.path.join(REPO, "rh", "catalog", "build_catalog.py")))
    except Exception:
        pass
    if missing:
        print("MISSING (not registered):")
        for m in missing:
            print("  -", m)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
