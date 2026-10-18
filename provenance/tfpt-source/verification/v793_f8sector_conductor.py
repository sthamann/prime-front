#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""v793 -- PRIME.SECTOR_CONTINUA.01: sector-adapted continua + the conductor functoriality of the Gamma_R rule -- demand (1) of PRIME.POSITIVE_DESCENT.01 becomes finite-level VIABLE and FUNCTORIAL, ONE module from two probes (15/15 + 16/16 checks, controls 3/3 + 3/3, ~2 s; discovery probes f8_sector_continuum_probe.py F8SECTOR-PSD and conductor_functoriality_probe.py CONDUCTOR-FUNCTORIAL, both 2026-08-05).  THE REPAIR (part 1): the f8 character sector, broken at -132..-151 under the register-trivial GL1 continuum (v791 finding F2), is PSD on the ENTIRE frozen ladder once the CP functor transports its OWN explicit-formula continuum (weight-4 archimedean kernel, conductor 8, NO pole, Satake atom masses t_{k+1} = t_1 t_k - t_{k-1}): lambda_min = +1.52e-4 -> +3.20e-5 over X = 4..10 (log-slope -0.241); the chi4 (odd Dirichlet mod 4) sector likewise PSD (+9.14e-5 -> +7.18e-6); GL1 anchor reproduced (+5.29e-5 -> +1.18e-5); THREE-SECTOR COHERENCE with the same battery/window machinery, battery Grams PSD; convention lock: the general arch builder at zeta parameters == v563.arch_lags BIT-IDENTICAL; the eta recurrence exact (a_p = (-4, -2, 24), a_2 = 0 -- the ramified channel EMPTY); Satake == Hecke bookkeeping p^{3k/2} t_k = a_{p^k} - p^3 a_{p^{k-2}} exact in Fractions.  Controls: the WRONG (GL1) continuum under the f8 atoms reproduces the parent breakage at -140.8; scrambled a_p -1.9e+36; Epstein x^2+5y^2 comb -156.  The register MIRROR sector (+,0,0) typed structurally NON-AUTOMORPHIC (sign-flipped comb -6.9; a 1/zeta-type channel with zeros and poles swapped) -- the functor's sector set is the AUTOMORPHIC register characters, not all 128.  THE RULE (part 2): the continuum assignment is ONE closed structure map, chi -> Lambda_chi = q^{s/2} prod_j Gamma_R(s + mu_j) L_an with (mu-list, q, pole) from (degree, weight/parity, ramified-register content) and ONE universal per-Gamma_R-factor kernel (p_e = mu + 1/2, q_e = 2, c0 = -(ln pi + EULER)) plus ln q at lag 0, pole iff trivial: instances zeta {0},1 / chi4 {1},4 / f8 {3/2,5/2},8 / twist {3/2,5/2},16 reproduce all deployed and sibling kernels EXACTLY, incl. the weight-4 kernel through the DUPLICATION identity Gamma_R(z)Gamma_R(z+1) = Gamma_C(z) verified across two independent quadrature structures (dev 2.66e-15).  THE SECOND CUSPIDAL SECTOR: the register-internal twist g = f8 (x) chi_{-4} (coefficients exact and multiplicative, Deligne survives twisting) has conductor 16 DECIDED inside the Atkin-Li bound lcm(8, 16, 4) = 16 by the Fricke ward f(1/(Nt)) = eps N^2 t^4 f(t) at machine precision (N = 16 passes at 6.7e-16 with eps = +1; N = 8/32 fail at 5.2e-1/6.8e-1; anchor: f8 itself W_8-eigenform, eps = +1, 4.4e-16); the twist window with the RULE-derived continuum -- nothing hand-tuned -- is PSD on the whole ladder (+1.97e-4 -> +2.75e-5), FOUR-SECTOR COHERENCE holds, and the conductor datum is LOAD-BEARING: swapping in the q = 8 constant shifts lambda_min by EXACTLY -ln 2 (control C1: -0.693120 = margin - ln 2, four orders of magnitude above the margins) while the PSD margins PIN the conductor from below (q >= 15.9996; Atkin-Li pins q | 16: unique conductor 16, relative width 2.7e-5).  Scrambled twisted a_p -2.3e+39; wrong-N Fricke fires.  B1 typed both parts: sector PSD at finite level is EVIDENCE for the functor architecture (zeros of the twisted L-functions on the line as far as they influence these windows) -- GRH(f8)/GRH(chi4)/GRH(twist) unproven, NOT a theorem.  Stop-list of the closed diagonal-Gram route binding; deployed machinery read-only.  No marker move, NO RH/GRH claim.  Python-only per GATE.WOLFRAM.02.

PROVENANCE: discovery probes f8_sector_continuum_probe.py (2026-08-05, 15/15, 0.7 s, F8SECTOR-PSD; the declared run-1 -> run-2 repair carried verbatim in the original docstring below: the A2 tail cross-check trapezoid rule replaced by GL-48 on geometric cells, no gate/kernel/bar changed) + conductor_functoriality_probe.py (2026-08-05, 16/16, 0.9 s, CONDUCTOR-FUNCTORIAL, first run after freeze, no repairs); both re-run identically at promotion (2026-08-06).  Promoted verbatim, part 2 wrapped in a function scope (v789 precedent); part 2's sibling imports (v563/v755/v766 machinery and f8_sector_continuum_probe/epstein_firewall_probe) resolve against experiments/tfpt-discovery on sys.path -- exactly the probes' own import graph; module-level _LAST1/_LAST2 verdict captures inserted at the single verdict assignments (v791 precedent); numbers unchanged; run() encodes both patterns (v757 precedent).

Original f8_sector_continuum_probe.py docstring (verbatim):
f8_sector_continuum_probe -- PRIME.POSITIVE_DESCENT.01 follow-up
(strand E, second module): the F8-SECTOR CONTINUUM -- the concrete
finite-level falsifier/promoter named by positive_descent_probe
(DESCENT-PARTIAL): does the f8 character sector become PSD when the
CP functor transports its OWN continuum (the twisted-channel explicit
formula: weight-4 archimedean factor, conductor 8, NO pole) with the
character, instead of the register-trivial GL1 arch+pole?

INPUT STATE (parent probe, 2026-08-05, DESCENT-PARTIAL, 30/30): the
GL1 sector of the packet correspondence operator is bit-identical to
the deployed Weil window and is its UNIQUE PSD sector (margins
+5.29e-5 -> +1.18e-5 over X = 4 -> 10); all 23 other sectors break at
O(1)-O(100) because the register-trivial continuum cannot follow the
damped/twisted atom leg (localization: the negativity is carried by
the POLE layer; arch alone stays near-PSD at -3.6..-4.7).  The parent
verdict named the missing CP-functor data: SECTOR-ADAPTED CONTINUA.
This probe builds the first two and decides them.

THE EXACT CONVENTIONS (frozen; derived so that the ZETA case
reproduces the deployed v563 kernel bit-for-bit -- gated Ward A1):
For a completed L-function Lambda(s) = q^{s/2} gamma_oo(s) L_an(s) in
the ANALYTIC normalization (functional equation s -> 1 - s, critical
line Re s = 1/2, the same normalization as the deployed GL1 window),
the explicit formula pairs an even test g (here: the tent-basis
autocorrelations of the dyadic window, D = 1/64) against
    W(g) = arch(g) [+ pole(g) if L has a pole] - sum_n (c(n)/sqrt(n))
                                                  (g(ln n) + g(-ln n)),
and W(g) = sum_rho h(gamma_rho) >= 0 whenever all zeros are on the
line (h = |phi-hat|^2 for g = phi * phi~).  The archimedean term, in
the tent-lag form the deployed machinery uses, is
    arch(g) = c0 g(0) + int_0^oo [2 e^{-q_e u} g(0)
              - e^{-p_e u} (g(u) + g(-u))] / (1 - e^{-q_e u}) du,
with the closed tail int_W^oo 2 e^{-q_e u}/(1 - e^{-q_e u}) du
= -(2/q_e) ln(1 - e^{-q_e W}).  The three channels decided here:
  ZETA (deployed GL1, validation Ward only):
      gamma_oo = pi^{-s/2} Gamma(s/2):
      c0 = -EULER - ln pi, p_e = 1/2, q_e = 2, PLUS the pole term
      (v716 pole_lags_closed, read-only).  Gate A1: this reproduces
      v563.arch_lags to <= 1e-12 -- the convention lock.
  CHI4 (the odd Dirichlet character mod 4; a genuine mu4-register
      sector of the parent packet -- sp/in = p mod 4):
      Lambda(s, chi) = (pi/4)^{-(s+1)/2} Gamma((s+1)/2) L(s, chi):
      c0 = ln(4/pi) - EULER, p_e = 3/2, q_e = 2, NO pole; atoms
      chi4(n) 2 Lambda(n)/sqrt(n) at ln n, odd n only (conductor 4
      kills the 2-adic channel); chi4(n) = +1/-1 for n = 1/3 mod 4.
  F8 (the weight-4 level-8 newform f8 = eta(2t)^4 eta(4t)^4 -- the C2
      sign channel of the packet, Th0 - Th2 = -8 f8 on odd n):
      Lambda(s) = 8^{s/2} (2 pi)^{-(s+3/2)} Gamma(s+3/2) L_an(s),
      L_an(s) = sum a_n n^{-(s+3/2)} ... i.e. a_n^an = a_n / n^{3/2}:
      gamma'/gamma(1/2 + ir) = (1/2) ln 8 - ln 2pi + psi(2 + ir):
      c0 = ln 8 - 2 ln 2pi - 2 EULER, p_e = 2, q_e = 1, NO pole
      (cuspidal); atoms at u = k ln p with the SATAKE masses
      mu(p^k) = 2 t_k(p) ln p / p^{k/2},
      t_0 = 2, t_1 = a_p / p^{3/2}, t_{k+1} = t_1 t_k - t_{k-1}
      (alpha_p beta_p = 1 for p odd; |t_k| <= 2 by Deligne), and NO
      2-adic atoms (a_2 = 0, conductor 8 -- the ramified channel is
      empty, exactly the parent's register honesty point).

GATES (frozen before the run):
  A1  convention lock: the general arch builder at the ZETA parameters
      reproduces v563.arch_lags(640, 1/64) to max abs <= 1e-12.
  A2  twisted kernels well-formed: d = 0 lags finite; far lags
      negative and decaying; closed tails match a brute cross-check.
  P1  f8 atom layer exact: a_p from the independent eta recurrence
      (int64 + python-int ward), a_p = (-4, -2, 24) at p = 3, 5, 7,
      a_2 = 0; |t_k| <= 2 on every reachable (p, k); t_k ==
      (a_{p^k} - p^3 a_{p^{k-2}})/p^{3k/2} exact-rationally for p = 3,
      k <= 8 (Satake == Hecke bookkeeping).
  D1  THE DECIDER: the f8-sector window (weight-4 arch, no pole, f8
      Satake atoms) is PSD on ALL rungs M = 256..640 (lambda_min >=
      -1e-10 ||T||_2); margins and trend reported.
  D2  the chi4 sector with ITS adapted continuum is PSD on all rungs.
  D3  the GL1 anchor (deployed c_full, read-only) is PSD on all rungs
      (the parent margins reproduced).
  D4  TWO-SECTOR COHERENCE (the structural gate): the SAME battery /
      window machinery with sector-adapted continua is PSD in the GL1
      AND f8 (AND chi4) sectors SIMULTANEOUSLY on every rung -- the
      coherence the CP functor needs.
  B1  honest baseline (typed, always printed): f8-sector PSD at finite
      level is EVIDENCE for the functor architecture (zeros of L(f8)
      lie on the line as far as computed; GRH(f8) is unproven), NOT a
      theorem.  No RH claim, no GRH claim.
CONTROLS (must fire):
  C1  WRONG continuum: the GL1 arch+pole under the f8 Satake atoms
      must break PSD massively (the parent's breakage reproduced from
      the other side); bar: lambda_min(top) < -10.
  C2  scrambled a_p (frozen LCG permutation of the a_p values across
      the odd primes, masses rebuilt): breaks PSD on the CORRECT f8
      continuum; bar: lambda_min(top) < 0.
  C3  Epstein x^2 + 5y^2 comb (epstein_firewall_probe read-only,
      Lambda_E via lattice count + Dirichlet division) on the f8
      continuum: breaks PSD; bar: lambda_min(top) < 0.
NAMED READOUTS (reported, never gated): the sign-flipped f8 comb on
the f8 continuum (the "mirror of f8" -- no L-function behind it); the
typed statement that the register MIRROR sector (+,0,0) admits NO
adapted continuum in the automorphic category (its atom side is
+Lambda(n)/sqrt(n) uniformly = a 1/zeta-type channel with zeros and
poles swapped -- there is no positivity target to adapt to), so the
CP functor's sector set is the AUTOMORPHIC characters, not all 128
register characters.

VERDICT ENUM (frozen):
  F8SECTOR-PSD     = A1/A2/P1 pass, D1-D4 pass, C1-C3 fire: the
      sector-adapted-continua demand of PRIME.POSITIVE_DESCENT.01 is
      finite-level VIABLE; the functor now needs the sector continua
      as functorial data (contract update in the report).
  F8SECTOR-PARTIAL = wards + controls ok, f8 PSD on >= 4 rungs but a
      gate among D1-D4 fails (name it).
  F8SECTOR-DEAD    = the f8 sector stays broken with its OWN continuum
      (D1 fails on > 3 rungs), or a convention ward fails, or a
      control is void: the functor architecture fails its first
      falsifier -- typed plainly.

RESULTS (2026-08-05, 15/15 checks, controls 3/3, 0.7 s; verdict
F8SECTOR-PSD).  Declared repair between run 1 and run 2: the A2 tail
cross-check used a trapezoid rule whose ~1.5e-5 endpoint error at the
1/u singularity failed its own bar; replaced by GL-48 on geometric
cells (dev 3.6e-15).  No gate, kernel, or bar was changed.
  *  A1 convention lock: general builder == v563.arch_lags, max abs
     dev 0.0 (bit-identical).  A2: d = 0 lags finite (f8 +7.590372,
     chi4 +4.133993), far lags negative/decaying, tail closed form ==
     brute (3.6e-15).
  *  P1: a_p = (-4, -2, 24), a_2 = 0 (ramified channel empty); 2518
     Satake atoms, |t_k| <= 2 everywhere (max 1.999631); Satake ==
     Hecke bookkeeping exact (p = 3, k <= 8, Fractions).
  *  D1 THE DECIDER: the f8 sector with its OWN continuum is PSD on
     ALL rungs, lambda_min = +1.52e-4 / +8.64e-5 / +6.14e-5 /
     +4.96e-5 / +4.15e-5 / +3.71e-5 / +3.20e-5 (X = 4..10, log-slope
     -0.241 per X unit).  The parent's f8-twist breakage (-132..-151)
     was ENTIRELY the wrong continuum.
  *  D2 chi4: PSD on all rungs, +9.14e-5 -> +7.18e-6 (slope -0.413).
     D3 GL1 anchor reproduced: +5.29e-5 -> +1.18e-5 (slope -0.239).
     D4 three-sector coherence PASSES: GL1 + chi4 + f8 simultaneously
     PSD on every rung; battery Grams PSD through all three sectors.
     Measured shape: all sectors live in the SAME thin-margin class
     with slow depth decay -- the pole is NOT the sole margin driver.
  *  Controls: C1 wrong continuum -1.408e+2 (parent band reproduced);
     C2 scrambled a_p -1.9e+36; C3 Epstein -1.560e+2.  Named readout:
     sign-flipped f8 comb -6.912 (the mirror-type non-automorphic
     channel indeed carries no positivity).
  *  B1 typed: evidence for the functor architecture, NOT a theorem.

FENCES: NO RH claim, NO GRH(f8) claim.  Stop-list of the closed
diagonal-Gram route binding: windows/battery/pole machinery reused
READ-ONLY, nothing re-gated, no fixed-d variants.  [C neu] semantics;
exploration only; ONE new file; writes nothing.  AST firewall: no
prime tables / zeta symbols (own sieve, own eta recurrence).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/f8_sector_continuum_probe.py

Original conductor_functoriality_probe.py docstring (verbatim):
conductor_functoriality_probe -- PRIME.POSITIVE_DESCENT.01,
third module (strand E): the CONDUCTOR-FUNCTORIALITY GATE -- the next
falsifier named by f8_sector_continuum_probe (F8SECTOR-PSD): show the
continuum assignment chi -> (c0, p_e, q_e, pole flag, conductor) is
ONE closed structure map (not a case table), and decide a SECOND
independent cuspidal sector -- the register-internal twist
f8 (x) chi_{-4} -- with the RULE-DERIVED continuum.

INPUT STATE (sibling probe, 2026-08-05, F8SECTOR-PSD, 15/15): the f8
and chi4 sectors are PSD on the full frozen ladder with their own
explicit-formula continua (f8: +1.52e-4 -> +3.20e-5; chi4: +9.14e-5
-> +7.18e-6; GL1 anchor +5.29e-5 -> +1.18e-5); the wrong (GL1)
continuum reproduces the parent breakage at -140.8; the mirror-type
register sectors are typed structurally non-automorphic.  The sibling
verdict named gate (1b): exhibit chi -> continuum as a functorial
assignment and test a second cuspidal sector from the same rule.

THE CLOSED RULE (frozen -- the standard completed-L recipe, stated as
ONE map and verified on all four sectors as instances):
    An automorphic sector chi of the register carries
        Lambda_chi(s) = q^{s/2} PROD_j Gamma_R(s + mu_j) L_an(chi, s),
        Gamma_R(z) = pi^{-z/2} Gamma(z/2),
    in the ANALYTIC normalization (functional equation s -> 1 - s),
    with (mu-list, q, pole) determined by (degree, parity/weight,
    ramified-register content):
        GL1 character, parity a:  mu = {a},                q = cond(chi),
                                  pole iff chi trivial;
        GL2 hol. newform, wt k :  mu = {(k-1)/2, (k+1)/2}, q = cond,
                                  no pole (cuspidal).
    The tent-lag continuum follows by ONE kernel lemma per Gamma_R
    factor (no per-sector choice):
        arch_chi(g) = ln(q) g(0) + SUM_j K_{mu_j}(g),
        K_mu(g) = -(ln pi + EULER) g(0)
                  + int_0^oo [2 e^{-2u} g(0)
                    - e^{-(mu + 1/2) u} (g(u) + g(-u))] / (1 - e^{-2u}) du,
    i.e. per factor p_e = mu + 1/2, q_e = 2, c0 = -(ln pi + EULER),
    plus the single conductor constant ln q at lag 0.  INSTANCES:
      zeta       : mu = {0}          , q = 1  (pole)   -> the deployed
                   GL1 kernel (gate R1a: == v563.arch_lags bit-level);
      chi_{-4}   : mu = {1}          , q = 4  (no pole) -> the sibling
                   chi4 kernel (gate R1b, <= 1e-12);
      f8         : mu = {3/2, 5/2}   , q = 8  (no pole) -> the sibling
                   weight-4 Gamma_C kernel via the DUPLICATION identity
                   Gamma_R(z) Gamma_R(z+1) = Gamma_C(z) (gate R1c,
                   <= 1e-9: two independent quadrature structures --
                   the strongest one-rule Ward);
      f8 (x) chi4: mu = {3/2, 5/2}   , q = 16 (no pole) -- NOTHING
                   hand-tuned: same mu-list as f8 (weight unchanged by
                   twisting), conductor from the twist bound + the
                   Fricke ward below.
THE TWIST (the second cuspidal sector, register-internal):
    g = f8 (x) chi_{-4}: a_g(n) = chi_{-4}(n) a_f8(n) (zero on even n;
    a_2(f8) = 0 already), weight 4, trivial nebentypus (chi^2 = 1),
    real coefficients.  CONDUCTOR: Atkin-Li (1978), "Twists of
    newforms and pseudo-eigenvalues of W-operators", Thm 3.1: for a
    newform of level N and a primitive twist chi mod m, cond(f x chi)
    divides lcm(N, m^2, m cond(chi_f)) = lcm(8, 16, 4) = 16 here; the
    EXACT conductor is decided numerically by the Fricke ward (T2):
    on the imaginary axis the weight-4 eigenform property reads
        f(1/(N t)) = eps N^2 t^4 f(t),   f(t) = SUM a(n) e^{-2 pi n t},
    which must hold to <= 1e-8 over the frozen t-grid for the TRUE N
    (and must FAIL for wrong N -- sub-control).  Anchor: f8 itself at
    N = 8 (its own Fricke eigenvalue reported).
GATES (frozen before the run):
  R1a/b/c  the rule instances (above).
  T1   twist layer exact: a_g multiplicative on 25 sampled coprime
       pairs (integer arithmetic); a_g(even) = 0; |t_k| <= 2 on every
       reachable (p, k) (Deligne survives twisting, |chi| = 1).
  T2   conductor: Fricke ward passes for exactly one N in {8, 16, 32}
       and it is N = 16, |eps| = 1; f8 anchor passes at N = 8.
  D1   THE DECIDER: the twist sector with the RULE-derived continuum
       (mu = {3/2, 5/2}, q = 16) is PSD on all rungs X = 4..10
       (bar -1e-10 ||T||_2).
  D2   FOUR-SECTOR COHERENCE: GL1 + chi4 + f8 + twist simultaneously
       PSD on every rung, same battery/window machinery (battery
       Grams PSD through all four).
  P0   conductor pinning (readout, gated as consistency): lambda_min
       is EXACTLY linear in ln q (identity shift), so PSD pins
       ln q >= ln 16 - lambda_min(top); with the Atkin-Li bound
       q | 16 from above, q = 16 is the unique admissible conductor;
       relative pinning width = lambda_min(top) ~ 1e-5.
CONTROLS (must fire):
  C1   THE DISCRIMINATING CONTROL: the twist sector under the
       UNTWISTED f8 continuum (q = 8, everything else identical) must
       break: the diagonal drops by exactly ln 2, so lambda_min ~
       margin - 0.693 < -0.5.  The conductor datum is load-bearing.
  C2   scrambled twisted a_p (frozen LCG permutation) explodes on the
       correct continuum (bar < 0).
  C3   wrong-N Fricke (N = 8 on the twist) fails by > 1e-2
       (sub-control inside T2).
NAMED (never gated): the register mirror (+,0,0) stays typed
non-automorphic (re-asserted; no positivity demand); sign-flipped
twist comb readout.
VERDICT ENUM (frozen):
  CONDUCTOR-FUNCTORIAL = R1 + T1/T2 + D1 + D2 + P0 pass, C1-C3 fire:
      the assignment is ONE map; demand (1) of
      PRIME.POSITIVE_DESCENT.01 upgrades to a functorial statement;
      what remains is the infinite-level CP extension (named in the
      contract update).
  CONDUCTOR-PARTIAL    = rule + twist PSD but a named gate fails.
  CONDUCTOR-AD-HOC     = the twist needs hand-tuning (D1 fails with
      the rule continuum): the assignment is a case table -- typed.

RESULTS (2026-08-05, first run after freeze, 16/16 checks, controls
3/3, 0.9 s; verdict CONDUCTOR-FUNCTORIAL; no repairs):
  *  R1a zeta == deployed and R1b chi4 == sibling: max dev 0.0
     (bit-level); R1c DUPLICATION WARD: the two-Gamma_R build equals
     the sibling Gamma_C weight-4 kernel to 2.66e-15 -- the rule is
     one map, verified across two independent quadrature structures.
  *  T1: twist coefficients exact and multiplicative; 2518 Satake
     atoms, |t_k| <= 2 (max 1.999631).
  *  T2 FRICKE: f8 anchor eps = +1 (4.4e-16); the twist passes at
     N = 16 ONLY (6.7e-16, eps = +1); N = 8 fails at 5.2e-1, N = 32
     at 6.8e-1: conductor(f8 x chi4) = 16, decided numerically at
     machine precision inside the Atkin-Li bound.
  *  D1: twist sector PSD on ALL rungs with the rule continuum,
     lambda_min = +1.97e-4 -> +2.75e-5 (X = 4..10).
  *  D2: FOUR-SECTOR COHERENCE holds (GL1 +5.29e-5 -> +1.18e-5, chi4
     +9.14e-5 -> +7.18e-6, f8 +1.52e-4 -> +3.20e-5, twist as above);
     battery Grams PSD through all four sectors.
  *  P0: lambda_min exactly linear in ln q (shift ward -6.931e-1 ==
     margin - ln 2); PSD pins q >= 15.999561, Atkin-Li pins q | 16:
     unique conductor 16, relative pinning width 2.7e-5.
  *  Controls: C1 untwisted (q = 8) continuum on the twist:
     lambda_min = -0.693120 = margin - ln 2 EXACTLY (deterministic
     identity shift -- the conductor datum is load-bearing at 4
     orders of magnitude above the margins); C2 scrambled a_p:
     -2.3e+39; C3 wrong-N Fricke fails at 5.2e-1.  Named: sign-
     flipped twist comb -6.73 (non-automorphic, breaks as typed).

FENCES: NO RH / GRH claim (B1 of the sibling probe carries over: PSD
here is finite-level EVIDENCE, zeros of L(g) on the line as far as
they influence the windows, nothing proven).  Stop-list of the closed
Gram route binding; deployed machinery reused READ-ONLY; exploration
only; ONE new file; writes nothing.  AST firewall: no prime tables /
zeta symbols (own sieve, own eta recurrence, sibling helpers
imported).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/conductor_functoriality_probe.py
"""

import ast
import hashlib
import math
import os
import sys
import time

import numpy as np
import scipy.linalg as sla

_VERIFY = os.path.dirname(os.path.abspath(__file__))
_DISCOVERY = os.path.abspath(os.path.join(_VERIFY, "..", "experiments",
                                          "tfpt-discovery"))
sys.path.insert(0, _DISCOVERY)
sys.path.insert(0, _VERIFY)

_LAST1 = {}
_LAST2 = {}

import v563_paper2_readouts as core          # noqa: E402  (deployed atoms)
import v716_moonshot_arch_glue as glue       # noqa: E402  (pole lags)
import v755_simpler_schur_recursion as srp   # noqa: E402  (tower channels)
import v766_handoff_bulk as hbp              # noqa: E402  (frozen battery)
import epstein_firewall_probe as epx         # noqa: E402  (control comb)

FROZEN_SPEC = """\
F8-SECTOR-CONTINUUM spec v1 (frozen 2026-08-05, before the first run).
Grid D = 1/64, M_TOP = 640, alpha_top = 5, rungs 256..640 step 64
(X = 4..10); N cap 22050 (reach e^10 = 22026).
Kernels (analytic normalization, tent-lag form, ZETA convention lock):
  zeta: c0 = -EULER - ln pi, p_e = 1/2, q_e = 2, pole = v716 closed;
  chi4: c0 = ln(4/pi) - EULER, p_e = 3/2, q_e = 2, no pole,
        atoms chi4(n) 2 Lambda(n)/sqrt(n), odd n;
  f8  : c0 = ln 8 - 2 ln 2pi - 2 EULER, p_e = 2, q_e = 1, no pole,
        atoms 2 t_k(p) ln p / p^{k/2} at k ln p, odd p only
        (t_1 = a_p p^{-3/2}, t_{k+1} = t_1 t_k - t_{k-1}; a from the
        independent eta recurrence).
Gates A1 (<= 1e-12), A2, P1, D1-D4 (PSD bar -1e-10 ||T||_2), B1 typed;
controls C1 (< -10), C2 (< 0), C3 (< 0); named readouts sign-flip f8,
mirror-sector statement.  Verdict enum F8SECTOR-PSD / -PARTIAL / -DEAD.
LCG seed 20260805.  Runtime cap ~20 min.  NO RH / GRH claim; stop-list
binding; writes nothing.
"""

DGRID = 1.0 / 64.0
M_TOP = 640
ALPHA_TOP = 0.5 * M_TOP * DGRID
RUNGS = (256, 320, 384, 448, 512, 576, 640)
N_CAP = 22050
PSD_BAR = 1.0e-10
EULER = 0.5772156649015328606
EP_NCAP = 34000

BANNED_IDS = ("sympy", "isprime", "primerange", "nextprime", "prevprime",
              "primepi", "zetazero", "nzeros", "mpz_zeta")

CHECKS = []
CONTROL_FIRED = {}
T0 = time.time()
_LCG = [20260805]

_GLX, _GLW = np.polynomial.legendre.leggauss(48)


def lcg(n):
    _LCG[0] = (1103515245 * _LCG[0] + 12345) % (1 << 31)
    return _LCG[0] % n


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok)))
    print("  [%s] %s%s" % ("PASS" if ok else "FAIL", name,
                           ("  -- " + detail) if detail else ""), flush=True)
    return bool(ok)


def section(title):
    print("\n" + "=" * 74)
    print(title)
    print("=" * 74, flush=True)


# ==================================================================== G0
def g0_firewall():
    section("G0 -- SHA-frozen spec + AST firewall + environment")
    sha = hashlib.sha256(FROZEN_SPEC.encode("utf-8")).hexdigest()
    print("    FROZEN_SPEC SHA-256 = %s" % sha)
    src = open(os.path.abspath(__file__), encoding="utf-8").read()
    tree = ast.parse(src)
    bad = []
    for node in ast.walk(tree):
        name = None
        if isinstance(node, ast.Name):
            name = node.id
        elif isinstance(node, ast.Attribute):
            name = node.attr
        elif isinstance(node, (ast.Import, ast.ImportFrom)):
            mods = [al.name for al in node.names]
            if isinstance(node, ast.ImportFrom) and node.module:
                mods.append(node.module)
            for m in mods:
                if any(b in m for b in BANNED_IDS):
                    bad.append(m)
            continue
        if name and name.lower() in BANNED_IDS:
            bad.append(name)
    check("G0.1 no prime-table / zeta symbols in this file", not bad,
          "found %s" % bad if bad else "clean")
    print("    python %s, numpy %s, scipy %s"
          % (sys.version.split()[0], np.__version__,
             __import__("scipy").__version__))


# =============================================== S1 general arch builder
def arch_lag_far(s, D, p_e, q_e):
    """-int tent_s(u) e^{-p u} / (1 - e^{-q u}) du, s >= D (GL-48 per
    half cell) -- the v563 far-cell structure with general exponents."""
    s = np.asarray(s, dtype=float).reshape(-1, 1)
    out = np.zeros(s.shape[0])
    for lo, hi in ((s - D, s), (s, s + D)):
        mid = 0.5 * (lo + hi)
        half = 0.5 * (hi - lo)
        w = mid + half * _GLX[None, :]
        val = ((1.0 - np.abs(s - w) / D) * np.exp(-p_e * w)
               / (-np.expm1(-q_e * w)))
        out -= half[:, 0] * (val @ _GLW)
    return out


def arch_lag_near(s, D, p_e, q_e, c0):
    """d = 0 (and any |s| < D) lag: constants + combined singular cell
    + closed counterterm tail -- the v563 near-cell structure with
    general exponents and constant."""
    s = abs(float(s))
    tri_s = max(0.0, 1.0 - s / D)
    W = s + D
    pts = sorted({0.0, s, D - s, W})
    pts = [p for p in pts if 0.0 <= p <= W]
    tot = 0.0
    for lo, hi in zip(pts[:-1], pts[1:]):
        if hi <= lo:
            continue
        mid = 0.5 * (lo + hi)
        half = 0.5 * (hi - lo)
        w = mid + half * _GLX
        S = 0.5 * (np.maximum(0.0, 1.0 - np.abs(s - w) / D)
                   + np.maximum(0.0, 1.0 - np.abs(s + w) / D))
        val = ((tri_s * np.exp(-q_e * w) - S * np.exp(-p_e * w))
               / (-np.expm1(-q_e * w)))
        tot += half * float(np.dot(_GLW, val))
    tail = tri_s * (-(2.0 / q_e) * math.log1p(-math.exp(-q_e * W)))
    return c0 * tri_s + 2.0 * tot + tail


def arch_lags_general(M, D, p_e, q_e, c0):
    sv = np.arange(M) * D
    out = np.empty(M)
    far = sv >= D
    out[far] = arch_lag_far(sv[far], D, p_e, q_e)
    for i in np.nonzero(~far)[0]:
        out[i] = arch_lag_near(sv[i], D, p_e, q_e, c0)
    return out


KERNELS = {
    "zeta": dict(p_e=0.5, q_e=2.0, c0=-EULER - math.log(math.pi),
                 pole=True,
                 label="pi^{-s/2} Gamma(s/2)          (GL1, deployed)"),
    "chi4": dict(p_e=1.5, q_e=2.0,
                 c0=math.log(4.0 / math.pi) - EULER, pole=False,
                 label="(pi/4)^{-(s+1)/2} Gamma((s+1)/2)  (odd Dirichlet"
                       " mod 4)"),
    "f8": dict(p_e=2.0, q_e=1.0,
               c0=math.log(8.0) - 2.0 * math.log(2.0 * math.pi)
               - 2.0 * EULER, pole=False,
               label="8^{s/2} (2pi)^{-(s+3/2)} Gamma(s+3/2)  (weight-4"
                     " newform, level 8)"),
}


def s1_kernels():
    section("S1 -- the twisted archimedean kernels (exact conventions) "
            "+ the ZETA convention lock")
    print("    tent-lag form: arch(g) = c0 g(0) + int [2 e^{-q u} g(0) "
          "- e^{-p u}(g(u)+g(-u))]/(1-e^{-q u}) du")
    for name, K in KERNELS.items():
        print("      %-4s: gamma_oo = %s" % (name, K["label"]))
        print("            p_e = %.1f, q_e = %.1f, c0 = %+.12f, pole = %s"
              % (K["p_e"], K["q_e"], K["c0"], K["pole"]))
    t0 = time.time()
    mine = arch_lags_general(M_TOP, DGRID, KERNELS["zeta"]["p_e"],
                             KERNELS["zeta"]["q_e"],
                             KERNELS["zeta"]["c0"])
    depl = core.arch_lags(M_TOP, DGRID)
    dev = float(np.max(np.abs(mine - depl)))
    check("A1 CONVENTION LOCK: general builder at zeta parameters == "
          "v563.arch_lags (max abs dev %.2e <= 1e-12)" % dev,
          dev <= 1.0e-12, "%.1f s" % (time.time() - t0))

    arch_c4 = arch_lags_general(M_TOP, DGRID, KERNELS["chi4"]["p_e"],
                                KERNELS["chi4"]["q_e"],
                                KERNELS["chi4"]["c0"])
    arch_f8 = arch_lags_general(M_TOP, DGRID, KERNELS["f8"]["p_e"],
                                KERNELS["f8"]["q_e"],
                                KERNELS["f8"]["c0"])
    # brute cross-check of the closed counterterm tail (A2): GL-48 on
    # geometric cells [W 2^k, W 2^{k+1}] (the integrand is ~2/(q u)
    # at the left endpoint -- geometric cells resolve it exactly)
    q = KERNELS["f8"]["q_e"]
    W = DGRID
    brute = 0.0
    for k in range(48):
        lo, hi = W * 2.0 ** k, W * 2.0 ** (k + 1)
        mid, half = 0.5 * (lo + hi), 0.5 * (hi - lo)
        u = mid + half * _GLX
        brute += half * float(np.dot(
            _GLW, 2.0 * np.exp(-q * u) / (-np.expm1(-q * u))))
    closed = -(2.0 / q) * math.log1p(-math.exp(-q * W))
    okA2 = (np.isfinite(arch_f8).all() and np.isfinite(arch_c4).all()
            and abs(brute - closed) <= 1.0e-9
            and np.all(arch_f8[1:] < 0) and np.all(arch_c4[1:] < 0)
            and arch_f8[10] > arch_f8[5] and arch_c4[10] > arch_c4[5])
    check("A2 twisted kernels well-formed: d = 0 finite (f8 %+.6f, "
          "chi4 %+.6f); far lags negative and decaying; closed tail == "
          "brute quadrature (dev %.1e)"
          % (arch_f8[0], arch_c4[0], abs(brute - closed)), okA2)
    return dict(arch_zeta=depl, arch_c4=arch_c4, arch_f8=arch_f8)


# =============================================== S2 f8 atom layer
def s2_f8_atoms():
    section("S2 -- the f8 Satake atom layer (independent eta recurrence)")
    t0 = time.time()
    # f8 = q prod (1-q^{2m})^4 (1-q^{4m})^4 via log-derivative recurrence
    tk = np.zeros(N_CAP + 1, dtype=np.int64)
    for d in range(2, N_CAP + 1, 2):
        e_d = 4 + (4 if d % 4 == 0 else 0)
        tk[d::d] += d * e_d
    g = np.zeros(N_CAP, dtype=np.int64)
    g[0] = 1
    for n in range(1, N_CAP):
        s = int(np.dot(tk[1:n + 1], g[n - 1::-1]))
        q, r = divmod(-s, n)
        assert r == 0
        g[n] = q
    a = np.zeros(N_CAP + 1, dtype=np.int64)
    a[1:] = g
    ok_ward = True
    for _ in range(20):
        n = 1 + lcg(N_CAP - 1)
        s = sum(int(tk[k]) * int(g[n - k]) for k in range(1, n + 1)
                if tk[k])
        ok_ward &= (-s == n * int(g[n]))
    check("P1.1 eta recurrence exact (int64 + python-int ward on 20 "
          "sampled steps); a_p = (%d, %d, %d) == (-4, -2, 24); a_2 = %d "
          "== 0 (conductor 8: the ramified channel is EMPTY)"
          % (a[3], a[5], a[7], a[2]),
          ok_ward and (a[3], a[5], a[7]) == (-4, -2, 24) and a[2] == 0,
          "%.1f s" % (time.time() - t0))

    # own smallest-factor sieve for the prime/prime-power structure
    spf = np.zeros(N_CAP + 1, dtype=np.int64)
    for p in range(2, N_CAP + 1):
        if spf[p] == 0:
            spf[p::p] = np.where(spf[p::p] == 0, p, spf[p::p])
    primes = [p for p in range(3, N_CAP + 1, 2) if spf[p] == p]

    # Satake masses on all reachable (p, k)
    pos, mas = [], []
    tmax = 0.0
    npk = 0
    for p in primes:
        if math.log(p) >= 2.0 * ALPHA_TOP:
            break
        t1 = float(a[p]) / p ** 1.5
        tkm1, tkk = 2.0, t1
        k = 1
        u = math.log(p)
        while u < 2.0 * ALPHA_TOP:
            mass = 2.0 * tkk * math.log(p) / p ** (0.5 * k)
            pos.append(u)
            mas.append(mass)
            tmax = max(tmax, abs(tkk))
            npk += 1
            tkm1, tkk = tkk, t1 * tkk - tkm1
            k += 1
            u = k * math.log(p)
    order = np.argsort(np.array(pos))
    pos = np.array(pos)[order]
    mas = np.array(mas)[order]
    check("P1.2 Satake layer: %d atoms (p odd, k >= 1, u < 10); "
          "|t_k| <= 2 everywhere (max %.6f) -- Deligne bound realized"
          % (npk, tmax), tmax <= 2.0 + 1e-12)

    # Satake == Hecke bookkeeping: t_k = (a_{p^k} - p^3 a_{p^{k-2}})
    #                                    / p^{3k/2}, exact rationals p=3
    from fractions import Fraction as Fr
    ok_hecke = True
    tprev, tcur = Fr(2), Fr(int(a[3]))          # scaled: T_k = t_k p^{3k/2}
    # use the integer-scaled recursion T_{k+1} = a_p T_k - p^3 T_{k-1}
    for k in range(1, 9):
        pk = 3 ** k
        ref = Fr(int(a[pk]) - (27 * int(a[pk // 9]) if k >= 2 else 0))
        if tcur != ref:
            ok_hecke = False
        tprev, tcur = tcur, Fr(int(a[3])) * tcur - 27 * tprev
    check("P1.3 Satake == Hecke bookkeeping: p^{3k/2} t_k == a_{p^k} - "
          "p^3 a_{p^{k-2}} EXACT (p = 3, k = 1..8, Fractions)", ok_hecke)
    return dict(a=a, pos=pos, mas=mas, spf=spf)


# =============================================== S3 sector windows
def ladder(lag):
    out = []
    for M in RUNGS:
        T = sla.toeplitz(lag[:M])
        lam = float(sla.eigvalsh(T, subset_by_index=[0, 0])[0])
        nrm = float(sla.norm(T, 2))
        out.append((M, lam, nrm))
    return out


def log_slope(vals):
    if any(v <= 0 for v in vals):
        return None
    Xs = np.array([M * DGRID for M in RUNGS])
    y = np.log(np.array(vals))
    A = np.vstack([np.ones(len(Xs)), Xs]).T
    cf, *_ = np.linalg.lstsq(A, y, rcond=None)
    return float(cf[1])


def s3_sectors(kern, f8):
    section("S3 -- the sector windows with their ADAPTED continua "
            "(the decider)")
    # GL1 anchor: deployed build (read-only)
    ka, masks, dev = srp.channel_masks(ALPHA_TOP)
    check("S3.0 tower comb consistency (deployed masses ward)",
          dev <= 1.0e-12, "rel dev %.1e, ka = %d" % (dev, ka))
    c_gl1 = srp.continuum_lags(M_TOP)
    for cnl in ("ro", "re", "sp", "in"):
        c_gl1 = c_gl1 + srp.atom_channel_lags(ALPHA_TOP, M_TOP,
                                              masks[cnl])
    # chi4 sector: odd deployed atoms, signed by n mod 4, own continuum
    nvals = np.array([int(round(math.exp(float(core.U_ALL[i]))))
                      for i in range(ka)], dtype=np.int64)
    odd = nvals % 2 == 1
    sgn = np.where(nvals % 4 == 1, 1.0, -1.0)
    pos4 = core.U_ALL[:ka][odd]
    mas4 = (core.MU_ALL[:ka] * sgn)[odd]
    cat4, _d = core.atom_lags_at(ALPHA_TOP, M_TOP, pos4, mas4)
    c_c4 = kern["arch_c4"] + cat4
    # f8 sector: Satake atoms, own continuum
    catf, _d = core.atom_lags_at(ALPHA_TOP, M_TOP, f8["pos"], f8["mas"])
    c_f8 = kern["arch_f8"] + catf

    lads = {"GL1 (deployed anchor)": ladder(c_gl1),
            "chi4 (adapted continuum)": ladder(c_c4),
            "f8 (adapted continuum)": ladder(c_f8)}
    print("    PSD table (lambda_min per rung, X = M/64):")
    print("      sector                    | " +
          " | ".join("X=%-2d" % int(M * DGRID) for M in RUNGS))
    psd = {}
    for name, lad in lads.items():
        psd[name] = all(lam >= -PSD_BAR * nrm for _M, lam, nrm in lad)
        print("      %-25s | %s  [%s]"
              % (name, " | ".join("%+.2e" % lam for _M, lam, _n in lad),
                 "PSD" if psd[name] else "NEG"))
        sl = log_slope([lam for _M, lam, _n in lad])
        print("        margin trend: factor %.2f over X = 4 -> 10, "
              "log-slope %s per X unit"
              % (lad[0][1] / lad[-1][1] if lad[-1][1] > 0 else
                 float("nan"),
                 "%.3f" % sl if sl is not None else "n/a"))
    ok1 = check("D1 THE DECIDER: the f8 sector with its OWN continuum "
                "(weight-4 arch, no pole, Satake atoms) is PSD on ALL "
                "%d rungs -- the parent's f8-twist breakage "
                "(-132..-151) was the WRONG continuum"
                % len(RUNGS), psd["f8 (adapted continuum)"])
    ok2 = check("D2 the chi4 sector with its adapted continuum is PSD "
                "on all rungs", psd["chi4 (adapted continuum)"])
    ok3 = check("D3 the GL1 anchor (deployed) is PSD on all rungs "
                "(parent margins reproduced)",
                psd["GL1 (deployed anchor)"])
    ok4 = check("D4 MULTI-SECTOR COHERENCE: GL1 + chi4 + f8 "
                "simultaneously PSD on every rung with the same "
                "battery/window machinery -- the coherence the CP "
                "functor needs", ok1 and ok2 and ok3)

    # battery Grams through the sectors (v766 battery R = 1, read-only)
    bat = hbp.battery(1.0)
    Fm = np.stack([v for _n, v in bat], axis=1)
    nR = Fm.shape[0]
    gmin = {}
    for name, lag in (("GL1", c_gl1), ("chi4", c_c4), ("f8", c_f8)):
        F = np.zeros((M_TOP, Fm.shape[1]))
        F[:nR] = Fm
        T = sla.toeplitz(lag[:M_TOP])
        Gm = F.T @ T @ F
        gmin[name] = float(np.linalg.eigvalsh(0.5 * (Gm + Gm.T))[0])
    check("S3.5 frozen-battery Grams PSD through all three sectors at "
          "the top rung (min eig GL1/chi4/f8 = %.1e / %.1e / %.1e)"
          % (gmin["GL1"], gmin["chi4"], gmin["f8"]),
          all(v >= -1.0e-12 for v in gmin.values()))
    print("    B1 HONEST BASELINE (typed): the f8/chi4 sector PSD at "
          "finite level is EVIDENCE for the functor architecture --\n"
          "       it reflects the zeros of L(f8)/L(chi4) lying on the "
          "critical line as far as they influence these windows.\n"
          "       GRH(f8) is UNPROVEN: this is a consistency "
          "measurement, NOT a theorem, and no GRH/RH claim is made.")
    return dict(c_gl1=c_gl1, c_c4=c_c4, c_f8=c_f8, lads=lads, psd=psd)


# =============================================== S4 controls + readouts
def s4_controls(kern, f8, ss3):
    section("S4 -- must-fail controls + named readouts")
    # C1 wrong continuum: GL1 arch + pole under the f8 Satake atoms
    catf, _d = core.atom_lags_at(ALPHA_TOP, M_TOP, f8["pos"], f8["mas"])
    c_wrong = srp.continuum_lags(M_TOP) + catf
    lam = float(sla.eigvalsh(sla.toeplitz(c_wrong[:M_TOP]),
                             subset_by_index=[0, 0])[0])
    CONTROL_FIRED["C1"] = lam < -10.0
    check("C1 WRONG continuum (GL1 arch+pole under f8 atoms): "
          "lambda_min(top) = %+.3e < -10 (the parent's sector breakage "
          "reproduced from the other side)" % lam, CONTROL_FIRED["C1"])

    # C2 scrambled a_p on the CORRECT f8 continuum
    spf = f8["spf"]
    primes = [p for p in range(3, N_CAP + 1, 2) if spf[p] == p]
    avals = [int(f8["a"][p]) for p in primes]
    perm = list(range(len(avals)))
    for i in range(len(perm) - 1, 0, -1):
        j = lcg(i + 1)
        perm[i], perm[j] = perm[j], perm[i]
    pos_s, mas_s = [], []
    for pi, p in enumerate(primes):
        if math.log(p) >= 2.0 * ALPHA_TOP:
            break
        t1 = float(avals[perm[pi]]) / p ** 1.5
        tkm1, tkk = 2.0, t1
        k = 1
        u = math.log(p)
        while u < 2.0 * ALPHA_TOP:
            pos_s.append(u)
            mas_s.append(2.0 * tkk * math.log(p) / p ** (0.5 * k))
            tkm1, tkk = tkk, t1 * tkk - tkm1
            k += 1
            u = k * math.log(p)
    cat_s, _d = core.atom_lags_at(ALPHA_TOP, M_TOP,
                                  np.array(pos_s), np.array(mas_s))
    lam_s = float(sla.eigvalsh(sla.toeplitz(
        (kern["arch_f8"] + cat_s)[:M_TOP]),
        subset_by_index=[0, 0])[0])
    CONTROL_FIRED["C2"] = lam_s < 0.0
    check("C2 scrambled a_p (LCG permutation across the odd primes, "
          "correct f8 continuum): lambda_min(top) = %+.3e < 0"
          % lam_s, CONTROL_FIRED["C2"])

    # C3 Epstein x^2 + 5y^2 comb on the f8 continuum
    r1 = epx.lattice_r1(EP_NCAP)
    b = np.asarray(r1, float) / 2.0
    lamE = epx.dirichlet_vonmangoldt(b, EP_NCAP)
    supp = np.nonzero(np.abs(lamE) > 1.0e-9)[0]
    supp = supp[(supp >= 2)]
    posE = np.log(supp.astype(float))
    keep = posE < 2.0 * ALPHA_TOP
    posE = posE[keep]
    masE = 2.0 * lamE[supp[keep]] / np.sqrt(supp[keep].astype(float))
    catE, _d = core.atom_lags_at(ALPHA_TOP, M_TOP, posE, masE)
    lam_e = float(sla.eigvalsh(sla.toeplitz(
        (kern["arch_f8"] + catE)[:M_TOP]),
        subset_by_index=[0, 0])[0])
    CONTROL_FIRED["C3"] = lam_e < 0.0
    check("C3 Epstein x^2+5y^2 comb (%d negative Lambda_E sites) on "
          "the f8 continuum: lambda_min(top) = %+.3e < 0"
          % (int(np.sum(lamE[2:] < -1.0e-9)), lam_e),
          CONTROL_FIRED["C3"])

    # named readouts (never gated)
    catm, _d = core.atom_lags_at(ALPHA_TOP, M_TOP, f8["pos"],
                                 -f8["mas"])
    lam_m = float(sla.eigvalsh(sla.toeplitz(
        (kern["arch_f8"] + catm)[:M_TOP]),
        subset_by_index=[0, 0])[0])
    print("    NAMED READOUT (not gated): sign-flipped f8 comb on the "
          "f8 continuum: lambda_min(top) = %+.3e" % lam_m)
    print("    NAMED STATEMENT (typed): the register MIRROR sector "
          "(+,0,0) admits NO adapted continuum in the automorphic\n"
          "      category -- its atom side (+Lambda(n)/sqrt(n) "
          "uniformly) is a 1/zeta-type channel (zeros <-> poles "
          "swapped),\n      so there is no positivity target to adapt "
          "to.  CONSEQUENCE for the functor: the CP sector set is the "
          "set of\n      AUTOMORPHIC characters of the register (GL1, "
          "chi4-type Dirichlet sectors, the f8 channel), not all 128 "
          "register\n      characters.  The parent's 23 broken sectors "
          "split into: repairable-by-adapted-continuum (automorphic) "
          "and\n      structurally-non-automorphic (mirror-type)."
          )
    return lam, lam_s, lam_e, lam_m


# ================================================================ verdict
def verdict(ss3):
    section("VERDICT")
    n_pass = sum(1 for _n, ok in CHECKS if ok)
    n_all = len(CHECKS)
    print("%d/%d checks passed" % (n_pass, n_all))
    controls_ok = all(CONTROL_FIRED.get(c, False)
                      for c in ("C1", "C2", "C3"))
    wards_ok = all(ok for n, ok in CHECKS
                   if n.startswith(("A1", "A2", "P1", "S3.0")))
    f8_lad = ss3["lads"]["f8 (adapted continuum)"]
    f8_psd_rungs = sum(1 for _M, lam, nrm in f8_lad
                       if lam >= -PSD_BAR * nrm)
    d_ok = ss3["psd"]["f8 (adapted continuum)"] \
        and ss3["psd"]["chi4 (adapted continuum)"] \
        and ss3["psd"]["GL1 (deployed anchor)"]
    if not wards_ok or not controls_ok or f8_psd_rungs <= 3:
        v = "F8SECTOR-DEAD (%s)" % (
            "convention ward failed" if not wards_ok else
            "control void: %s" % [c for c in ("C1", "C2", "C3")
                                  if not CONTROL_FIRED.get(c, False)]
            if not controls_ok else
            "the f8 sector stays broken with its OWN continuum "
            "(%d/7 rungs PSD): the functor architecture fails its "
            "first falsifier" % f8_psd_rungs)
    elif d_ok and n_pass == n_all:
        v = "F8SECTOR-PSD"
    else:
        fails = [n for n, ok in CHECKS if not ok]
        v = "F8SECTOR-PARTIAL (%s)" % ("; ".join(fails[:3])
                                       if fails else "gate detail")
    print("VERDICT: %s" % v)
    if v == "F8SECTOR-PSD":
        print("""
F8-SECTOR CONTINUUM -- F8SECTOR-PSD.  The first falsifier of the
sector-adapted-continua demand PASSES:
  * The f8 sector, broken at -132..-151 under the register-trivial
    GL1 continuum (parent probe), is PSD on the ENTIRE frozen ladder
    once the CP functor transports its OWN continuum (weight-4 arch
    kernel, conductor 8, no pole, Satake atom masses) -- with margins
    in the same thin-margin class as the GL1 anchor (~3x fatter).
  * The chi4 (odd Dirichlet mod 4) sector -- a genuine mu4-register
    sector -- is likewise PSD with its adapted continuum.
  * MULTI-SECTOR COHERENCE holds: GL1 + chi4 + f8 are simultaneously
    PSD on every rung with the SAME battery/window machinery -- the
    finite-level shape of the CP functor's naturality square.
  * Controls: the wrong continuum reproduces the parent breakage; a_p
    scramble and Epstein break the correct continuum.  The mirror
    sector is typed as structurally non-automorphic (no adapted
    continuum exists) -- the functor's sector set is the automorphic
    characters, not all 128.
  * B1: evidence for the functor architecture, NOT a theorem
    (GRH(f8)/GRH(chi4)/RH all unproven).  NO claim beyond the frozen
    windows.""")
    print("total runtime %.1f s" % (time.time() - T0))
    return v


def contract_update(ss3):
    section("RECOMMENDED CONTRACT UPDATE -- PRIME.POSITIVE_DESCENT.01 "
            "(report only; nothing written)")
    print("""\
    UPDATE to the three-object demand of PRIME.POSITIVE_DESCENT.01
    (parent report), after the first falsifier PASSED:
      (1) SECTOR-ADAPTED CONTINUA -- status upgrade [finite-level
          VIABLE]: the f8 and chi4 sectors are PSD on the full frozen
          ladder with their own explicit-formula continua (f8:
          +1.52e-4 -> +3.20e-5; chi4: +9.14e-5 -> +7.18e-6; GL1
          anchor: +5.29e-5 -> +1.18e-5).  The demand sharpens to:
          (1a) the functor's sector set is the AUTOMORPHIC register
          characters (GL1, the Dirichlet mu4 sectors, the f8/C2
          channel); the mirror-type sectors are structurally
          non-automorphic (sign-flipped f8 comb: lambda_min = -6.9)
          and carry no positivity demand; (1b) the continuum
          assignment chi -> (c0, p_e, q_e, pole flag, conductor) must
          be shown FUNCTORIAL (compatible with the register
          composition measured in the parent: sigma3/f8 channel
          arithmetic, conductor = ramified-register content:
          1 / 4 / 8 here).
      (2) SECTOR-PSD PERSISTENCE now reads: for EVERY automorphic
          sector, the sector window with its adapted continuum stays
          PSD as X -> infinity (GL1 = Weil positivity; f8/chi4 = the
          GRH-type statements for the twisted channels).  The
          measured finite-level shape: ALL THREE sectors sit in the
          same thin-margin PSD class with slow depth decay (log-slope
          per X unit: GL1 -0.239, f8 -0.241, chi4 -0.413) -- the
          moving-edge phenomenon of the closed route persists in mild
          form in every sector, pole or no pole, so the pole is NOT
          the sole thin-margin driver; the persistence demand is a
          genuinely infinite-level statement in each sector.
      (3) THE CARRIER INTERTWINER is unchanged (the population ->
          unit-modulus sign step), but gains a target: the intertwined
          carrier evaluation must land, sector by sector, on EXACTLY
          these adapted explicit formulas (the Satake mass recursion
          t_{k+1} = t_1 t_k - t_{k-1} IS the analytic image of the
          parent's p^3-corrected packet recursion -- the bookkeeping
          identity p^{3k/2} t_k = a_{p^k} - p^3 a_{p^{k-2}} was
          verified exactly here).
    STOP CONDITIONS unchanged: no RH/GRH claim, stop-list of the
    closed Gram route binding, closed-route objects reused read-only.
    NEXT FALSIFIER (named): the conductor-functoriality gate (1b) --
    exhibit the continuum assignment as a monoid map from the
    ramified-register content to (conductor, gamma shift), and test a
    SECOND cuspidal sector (e.g. the weight-4 level-16 channel of the
    mu4 register) with the same machinery.""")


def main():
    print("=" * 74)
    print("F8-SECTOR CONTINUUM -- the first falsifier of the "
          "sector-adapted-continua")
    print("demand of PRIME.POSITIVE_DESCENT.01 (parent: DESCENT-PARTIAL)")
    print("=" * 74)
    g0_firewall()
    kern = s1_kernels()
    f8 = s2_f8_atoms()
    ss3 = s3_sectors(kern, f8)
    s4_controls(kern, f8, ss3)
    v = verdict(ss3)
    _LAST1["verdict"] = v
    contract_update(ss3)
    n_pass = sum(1 for _n, ok in CHECKS if ok)
    return 0 if (n_pass == len(CHECKS)
                 and not v.startswith("F8SECTOR-DEAD")) else 1


_run_part1 = main


def _run_part2():
    """Part 2: conductor_functoriality_probe.py, promoted verbatim in a
    function scope (v789 precedent)."""
    import ast
    import hashlib
    import math
    import os
    import sys
    import time

    import numpy as np
    import scipy.linalg as sla


    import v563_paper2_readouts as core            # noqa: E402
    import v755_simpler_schur_recursion as srp     # noqa: E402
    import v766_handoff_bulk as hbp                # noqa: E402
    import f8_sector_continuum_probe as fsc        # noqa: E402  (sibling,
    #                                          import-safe: main() guarded)

    FROZEN_SPEC = """\
CONDUCTOR-FUNCTORIALITY spec v1 (frozen 2026-08-05, before the first
run).  Grid D = 1/64, M_TOP = 640, rungs 256..640 step 64; N cap
22050.  THE RULE: Lambda_chi = q^{s/2} prod_j Gamma_R(s + mu_j) L_an;
kernel = ln(q) at lag 0 + sum_j GammaR-factor kernels
(p_e = mu_j + 1/2, q_e = 2, c0 = -(ln pi + EULER)); pole iff trivial.
Instances: zeta {0},1; chi4 {1},4; f8 {3/2,5/2},8; twist {3/2,5/2},16.
Gates R1a (bit/1e-12 vs deployed), R1b (1e-12), R1c duplication
(1e-9), T1 (25 coprime pairs, Deligne), T2 Fricke (1e-8 pass at one N
= 16, anchor f8@8; wrong-N > 1e-2), D1/D2 (PSD bar -1e-10 ||T||_2),
P0 pinning.  Controls C1 (< -0.5), C2 (< 0), C3 (> 1e-2).  Fricke
t-grid {0.19, 0.22, 0.28, 0.33, 0.40} (kept away from the W_N fixed
points 1/sqrt(N) = 0.177 / 0.25 / 0.354 where R is trivial or 0/0;
NaN ratios count as ward failure), series cap n <= 3000.  LCG
seed 20260805.  Verdict enum CONDUCTOR-FUNCTORIAL / -PARTIAL /
-AD-HOC.  NO RH/GRH claim; stop-list binding; writes nothing.
"""

    DGRID = 1.0 / 64.0
    M_TOP = 640
    ALPHA_TOP = 0.5 * M_TOP * DGRID
    RUNGS = (256, 320, 384, 448, 512, 576, 640)
    N_CAP = 22050
    PSD_BAR = 1.0e-10
    EULER = 0.5772156649015328606
    LOG_PI = math.log(math.pi)
    FRICKE_T = (0.19, 0.22, 0.28, 0.33, 0.40)
    FRICKE_NCAP = 3000

    BANNED_IDS = ("sympy", "isprime", "primerange", "nextprime", "prevprime",
                  "primepi", "zetazero", "nzeros", "mpz_zeta")

    CHECKS = []
    CONTROL_FIRED = {}
    T0 = time.time()
    _LCG = [20260805]


    def lcg(n):
        _LCG[0] = (1103515245 * _LCG[0] + 12345) % (1 << 31)
        return _LCG[0] % n


    def check(name, ok, detail=""):
        CHECKS.append((name, bool(ok)))
        print("  [%s] %s%s" % ("PASS" if ok else "FAIL", name,
                               ("  -- " + detail) if detail else ""), flush=True)
        return bool(ok)


    def section(title):
        print("\n" + "=" * 74)
        print(title)
        print("=" * 74, flush=True)


    # ==================================================================== G0
    def g0_firewall():
        section("G0 -- SHA-frozen spec + AST firewall + environment")
        sha = hashlib.sha256(FROZEN_SPEC.encode("utf-8")).hexdigest()
        print("    FROZEN_SPEC SHA-256 = %s" % sha)
        src = open(os.path.abspath(__file__), encoding="utf-8").read()
        bad = []
        for node in ast.walk(ast.parse(src)):
            name = None
            if isinstance(node, ast.Name):
                name = node.id
            elif isinstance(node, ast.Attribute):
                name = node.attr
            elif isinstance(node, (ast.Import, ast.ImportFrom)):
                mods = [al.name for al in node.names]
                if isinstance(node, ast.ImportFrom) and node.module:
                    mods.append(node.module)
                bad += [m for m in mods if any(b in m for b in BANNED_IDS)]
                continue
            if name and name.lower() in BANNED_IDS:
                bad.append(name)
        check("G0.1 no prime-table / zeta symbols in this file", not bad,
              "found %s" % bad if bad else "clean")
        print("    python %s, numpy %s, scipy %s"
              % (sys.version.split()[0], np.__version__,
                 __import__("scipy").__version__))


    # ==================================================== S1 THE CLOSED RULE
    def rule_arch_lags(mus, q):
        """THE structure map: mu-list + conductor -> tent-lag continuum.
    One universal Gamma_R-factor kernel per mu, one ln(q) at lag 0.
    Nothing else is free."""
        out = np.zeros(M_TOP)
        for mu in mus:
            out += fsc.arch_lags_general(M_TOP, DGRID, mu + 0.5, 2.0,
                                         -(LOG_PI + EULER))
        out[0] += math.log(q)
        return out


    SECTOR_DATA = {
        #  name          mu-list         q   pole
        "zeta":  (( 0.0,),        1,  True),
        "chi4":  (( 1.0,),        4,  False),
        "f8":    ((1.5, 2.5),     8,  False),
        "twist": ((1.5, 2.5),    16,  False),
    }


    def s1_rule():
        section("S1 -- THE CLOSED RULE (one structure map) + instance gates")
        print("    RULE: Lambda_chi(s) = q^{s/2} prod_j Gamma_R(s + mu_j) "
              "L_an(chi, s);   kernel = ln(q) e_0 + sum_j K_{mu_j},")
        print("          K_mu: p_e = mu + 1/2, q_e = 2, c0 = -(ln pi + "
              "EULER);   pole iff chi trivial.  Instances:")
        for nm, (mus, q, pole) in SECTOR_DATA.items():
            print("      %-5s: mu = %-12s q = %-3d pole = %s"
                  % (nm, str(list(mus)), q, pole))
        lag = {nm: rule_arch_lags(mus, q)
               for nm, (mus, q, _p) in SECTOR_DATA.items()}

        dev_a = float(np.max(np.abs(lag["zeta"] - core.arch_lags(M_TOP,
                                                                 DGRID))))
        check("R1a rule instance zeta {mu=0, q=1} == DEPLOYED "
              "v563.arch_lags (max abs dev %.2e <= 1e-12)" % dev_a,
              dev_a <= 1.0e-12)
        sib_c4 = fsc.arch_lags_general(M_TOP, DGRID, 1.5, 2.0,
                                       math.log(4.0 / math.pi) - EULER)
        dev_b = float(np.max(np.abs(lag["chi4"] - sib_c4)))
        check("R1b rule instance chi4 {mu=1, q=4} == sibling chi4 kernel "
              "(max abs dev %.2e <= 1e-12)" % dev_b, dev_b <= 1.0e-12)
        sib_f8 = fsc.arch_lags_general(
            M_TOP, DGRID, 2.0, 1.0,
            math.log(8.0) - 2.0 * math.log(2.0 * math.pi) - 2.0 * EULER)
        dev_c = float(np.max(np.abs(lag["f8"] - sib_f8)))
        check("R1c DUPLICATION WARD: rule instance f8 {mu=3/2,5/2, q=8} "
              "(two Gamma_R kernels) == sibling Gamma_C kernel "
              "(independent quadrature structure; max abs dev %.2e <= "
              "1e-9) -- Gamma_R(z) Gamma_R(z+1) = Gamma_C(z)" % dev_c,
              dev_c <= 1.0e-9)
        print("    (the -2 ln 2 constant offset between the two forms is "
              "absorbed by the counterterm integral, as the duplication\n"
              "     identity demands -- verified numerically above, not "
              "assumed)")
        return lag


    # ==================================================== S2 the twist layer
    def eta_f8(ncap):
        """a_n of f8 = eta(2t)^4 eta(4t)^4 by the log-derivative
    recurrence (int64, exact; sibling-validated construction)."""
        tk = np.zeros(ncap + 1, dtype=np.int64)
        for d in range(2, ncap + 1, 2):
            tk[d::d] += d * (4 + (4 if d % 4 == 0 else 0))
        g = np.zeros(ncap, dtype=np.int64)
        g[0] = 1
        for n in range(1, ncap):
            s = int(np.dot(tk[1:n + 1], g[n - 1::-1]))
            q, r = divmod(-s, n)
            assert r == 0
            g[n] = q
        a = np.zeros(ncap + 1, dtype=np.int64)
        a[1:] = g
        return a


    def chi4(n):
        if n % 2 == 0:
            return 0
        return 1 if n % 4 == 1 else -1


    def s2_twist():
        section("S2 -- the twist g = f8 (x) chi_{-4}: coefficients, "
                "Deligne, conductor (Fricke ward)")
        t0 = time.time()
        a = eta_f8(N_CAP)
        ag = np.array([chi4(n) * int(a[n]) for n in range(N_CAP + 1)],
                      dtype=np.int64)
        ok_anchor = ((int(a[3]), int(a[5]), int(a[7])) == (-4, -2, 24)
                     and (int(ag[3]), int(ag[5]), int(ag[7]))
                     == (4, -2, -24) and int(ag[2]) == 0)
        ok_mult = True
        for _ in range(25):
            m = 3 + 2 * lcg(60)
            n = 3 + 2 * lcg(60)
            if math.gcd(m, n) != 1 or m * n > N_CAP:
                continue
            ok_mult &= int(ag[m * n]) == int(ag[m]) * int(ag[n])
        check("T1.1 twist coefficients exact: a_g(3,5,7) = (+4,-2,-24) = "
              "chi4 * (-4,-2,24); a_g(even) = 0; multiplicative on "
              "sampled coprime odd pairs (integer arithmetic)",
              ok_anchor and ok_mult
              and not np.any(ag[2::2]), "%.1f s" % (time.time() - t0))

        # Satake masses for the twist (and Deligne)
        spf = np.zeros(N_CAP + 1, dtype=np.int64)
        for p in range(2, N_CAP + 1):
            if spf[p] == 0:
                spf[p::p] = np.where(spf[p::p] == 0, p, spf[p::p])
        primes = [p for p in range(3, N_CAP + 1, 2) if spf[p] == p]

        def satake_comb(ap_of_p):
            pos, mas = [], []
            tmax = 0.0
            for p in primes:
                u1 = math.log(p)
                if u1 >= 2.0 * ALPHA_TOP:
                    break
                t1 = float(ap_of_p(p)) / p ** 1.5
                tkm1, tkk = 2.0, t1
                k, u = 1, u1
                while u < 2.0 * ALPHA_TOP:
                    pos.append(u)
                    mas.append(2.0 * tkk * math.log(p) / p ** (0.5 * k))
                    tmax = max(tmax, abs(tkk))
                    tkm1, tkk = tkk, t1 * tkk - tkm1
                    k += 1
                    u = k * u1
            return np.array(pos), np.array(mas), tmax

        pos_g, mas_g, tmax_g = satake_comb(lambda p: ag[p])
        pos_f, mas_f, _tf = satake_comb(lambda p: a[p])
        check("T1.2 twist Satake layer: %d atoms; |t_k| <= 2 everywhere "
              "(max %.6f) -- Deligne survives twisting (|chi| = 1)"
              % (len(pos_g), tmax_g), tmax_g <= 2.0 + 1e-12)

        # T2 -- Fricke ward: f(1/(N t)) = eps N^2 t^4 f(t), weight 4
        print("    T2 conductor: Atkin-Li (1978, Thm 3.1) bound "
              "cond(f8 x chi4) | lcm(8, 4^2, 4) = 16; exact value by the "
              "Fricke ward:")
        nv = np.arange(1, FRICKE_NCAP + 1, dtype=float)

        def f_series(coeff, t):
            return float(np.dot(coeff[1:FRICKE_NCAP + 1],
                                np.exp(-2.0 * math.pi * nv * t)))

        def fricke_dev(coeff, N):
            R = [f_series(coeff, 1.0 / (N * t))
                 / (N ** 2 * t ** 4 * f_series(coeff, t)) for t in FRICKE_T]
            if any(math.isnan(r) or math.isinf(r) for r in R):
                return float("inf"), 0
            eps = round(sum(R) / len(R))
            return max(abs(r - eps) for r in R), eps

        afl = a.astype(float)
        agl = ag.astype(float)
        dev_f8, eps_f8 = fricke_dev(afl, 8)
        check("T2.1 anchor: f8 itself is a W_8 eigenform, eps = %+d "
              "(max |R - eps| = %.1e <= 1e-8)" % (eps_f8, dev_f8),
              dev_f8 <= 1.0e-8 and abs(eps_f8) == 1)
        devs = {N: fricke_dev(agl, N) for N in (8, 16, 32)}
        for N, (d, e) in devs.items():
            print("      twist @ N = %-2d : max |R - eps| = %.3e "
                  "(nearest eps = %+d)" % (N, d, e))
        ok_16 = devs[16][0] <= 1.0e-8 and abs(devs[16][1]) == 1
        ok_unique = all(devs[N][0] > 1.0e-2 for N in (8, 32))
        check("T2.2 the twist passes the Fricke ward at N = 16 ONLY "
              "(eps = %+d); wrong N in {8, 32} fail by > 1e-2 -- "
              "conductor(f8 x chi4) = 16" % devs[16][1],
              ok_16 and ok_unique)
        CONTROL_FIRED["C3"] = devs[8][0] > 1.0e-2
        check("C3 wrong-N Fricke control (N = 8 on the twist) FAILS as "
              "it must (dev %.2e > 1e-2)" % devs[8][0],
              CONTROL_FIRED["C3"])
        return dict(pos_g=pos_g, mas_g=mas_g, pos_f=pos_f, mas_f=mas_f,
                    primes=primes, ag=ag)


    # ============================================ S3 four-sector coherence
    def lam_min(lagv, M):
        T = sla.toeplitz(lagv[:M])
        lam = float(sla.eigvalsh(T, subset_by_index=[0, 0])[0])
        return lam, float(sla.norm(T, 2))


    def s3_sectors(lag, tw):
        section("S3 -- the four-sector PSD ladder (rule-derived continua "
                "only)")
        # GL1: deployed build (anchor, read-only)
        ka, masks, dev = srp.channel_masks(ALPHA_TOP)
        check("S3.0 tower comb consistency (deployed masses ward)",
              dev <= 1.0e-12, "rel dev %.1e, ka = %d" % (dev, ka))
        c_gl1 = srp.continuum_lags(M_TOP)
        for cnl in ("ro", "re", "sp", "in"):
            c_gl1 = c_gl1 + srp.atom_channel_lags(ALPHA_TOP, M_TOP,
                                                  masks[cnl])
        nvals = np.array([int(round(math.exp(float(core.U_ALL[i]))))
                          for i in range(ka)], dtype=np.int64)
        odd = nvals % 2 == 1
        sgn = np.where(nvals % 4 == 1, 1.0, -1.0)
        cat4, _d = core.atom_lags_at(ALPHA_TOP, M_TOP,
                                     core.U_ALL[:ka][odd],
                                     (core.MU_ALL[:ka] * sgn)[odd])
        catf, _d = core.atom_lags_at(ALPHA_TOP, M_TOP, tw["pos_f"],
                                     tw["mas_f"])
        catg, _d = core.atom_lags_at(ALPHA_TOP, M_TOP, tw["pos_g"],
                                     tw["mas_g"])
        combs = {
            "GL1 (deployed anchor)": c_gl1,
            "chi4 (rule continuum)": lag["chi4"] + cat4,
            "f8 (rule continuum)": lag["f8"] + catf,
            "f8xchi4 (rule continuum)": lag["twist"] + catg,
        }
        print("    PSD table (lambda_min per rung, X = M/64):")
        print("      sector                    | " +
              " | ".join("X=%-2d" % int(M * DGRID) for M in RUNGS))
        psd, top = {}, {}
        for name, cv in combs.items():
            row = [lam_min(cv, M) for M in RUNGS]
            psd[name] = all(l >= -PSD_BAR * n for l, n in row)
            top[name] = row[-1][0]
            print("      %-25s | %s  [%s]"
                  % (name, " | ".join("%+.2e" % l for l, _n in row),
                     "PSD" if psd[name] else "NEG"))
        ok1 = check("D1 THE DECIDER: the twist sector f8 x chi4 with the "
                    "RULE-derived continuum {mu = 3/2, 5/2; q = 16} -- "
                    "nothing hand-tuned -- is PSD on ALL %d rungs"
                    % len(RUNGS), psd["f8xchi4 (rule continuum)"])
        ok2 = check("D2 FOUR-SECTOR COHERENCE: GL1 + chi4 + f8 + twist "
                    "simultaneously PSD on every rung, same machinery",
                    all(psd.values()))

        # battery Grams through all four sectors
        bat = hbp.battery(1.0)
        Fm = np.stack([v for _n, v in bat], axis=1)
        F = np.zeros((M_TOP, Fm.shape[1]))
        F[:Fm.shape[0]] = Fm
        gmin = {}
        for name, cv in combs.items():
            T = sla.toeplitz(cv[:M_TOP])
            Gm = F.T @ T @ F
            gmin[name] = float(np.linalg.eigvalsh(0.5 * (Gm + Gm.T))[0])
        check("S3.5 frozen-battery Grams PSD through all FOUR sectors "
              "(min eigs %s)" % ", ".join("%.0e" % v for v in
                                          gmin.values()),
              all(v >= -1.0e-12 for v in gmin.values()))

        # P0 conductor pinning: lambda_min is exactly linear in ln q
        lm = top["f8xchi4 (rule continuum)"]
        qmin = 16.0 * math.exp(-lm)
        shift = lam_min((lag["twist"] + catg
                         - np.eye(1, M_TOP, 0)[0] * math.log(2.0)), M_TOP)[0]
        ok_lin = abs(shift - (lm - math.log(2.0))) <= 1.0e-8
        check("P0 CONDUCTOR PINNING: lambda_min is exactly linear in "
              "ln q (identity shift verified: %.3e == %.3e - ln 2); PSD "
              "pins q >= 16 exp(-%.2e) = %.6f, Atkin-Li pins q | 16: the "
              "unique admissible conductor is 16 (relative width %.1e)"
              % (shift, lm, lm, qmin, lm), ok_lin)
        print("    B1 (carried over, typed): the twist-sector PSD is "
              "finite-level EVIDENCE (zeros of L(f8 x chi4) on the line "
              "as far\n       as they influence these windows); GRH-type "
              "statements unproven; NO RH/GRH claim.")
        return dict(combs=combs, psd=psd, top=top, catg=catg)


    # ================================================ S4 remaining controls
    def s4_controls(lag, tw, ss3):
        section("S4 -- controls + named readouts")
        catg = ss3["catg"]
        # C1 discriminating control: untwisted f8 continuum (q = 8) on the
        # twist sector -- ONLY the conductor constant differs (-ln 2 on
        # the diagonal)
        lam, _n = lam_min(lag["f8"] + catg, M_TOP)
        CONTROL_FIRED["C1"] = lam < -0.5
        check("C1 DISCRIMINATING CONTROL: the twist sector under the "
              "UNTWISTED f8 continuum (q = 8): lambda_min(top) = %+.6f "
              "< -0.5 (= margin - ln 2 = %+.6f; the conductor datum is "
              "load-bearing at 4 orders of magnitude above the margins)"
              % (lam, ss3["top"]["f8xchi4 (rule continuum)"]
                 - math.log(2.0)), CONTROL_FIRED["C1"])

        # C2 scrambled twisted a_p on the correct rule continuum
        primes = tw["primes"]
        avals = [int(tw["ag"][p]) for p in primes]
        perm = list(range(len(avals)))
        for i in range(len(perm) - 1, 0, -1):
            j = lcg(i + 1)
            perm[i], perm[j] = perm[j], perm[i]
        pos_s, mas_s = [], []
        for pi, p in enumerate(primes):
            u1 = math.log(p)
            if u1 >= 2.0 * ALPHA_TOP:
                break
            t1 = float(avals[perm[pi]]) / p ** 1.5
            tkm1, tkk = 2.0, t1
            k, u = 1, u1
            while u < 2.0 * ALPHA_TOP:
                pos_s.append(u)
                mas_s.append(2.0 * tkk * math.log(p) / p ** (0.5 * k))
                tkm1, tkk = tkk, t1 * tkk - tkm1
                k += 1
                u = k * u1
        cat_s, _d = core.atom_lags_at(ALPHA_TOP, M_TOP, np.array(pos_s),
                                      np.array(mas_s))
        lam_s, _n = lam_min(lag["twist"] + cat_s, M_TOP)
        CONTROL_FIRED["C2"] = lam_s < 0.0
        check("C2 scrambled twisted a_p (LCG permutation, correct rule "
              "continuum): lambda_min(top) = %+.3e < 0" % lam_s,
              CONTROL_FIRED["C2"])

        # named readouts
        catm, _d = core.atom_lags_at(ALPHA_TOP, M_TOP, tw["pos_g"],
                                     -tw["mas_g"])
        lam_m, _n = lam_min(lag["twist"] + catm, M_TOP)
        print("    NAMED READOUT (not gated): sign-flipped twist comb on "
              "the rule continuum: lambda_min(top) = %+.3e" % lam_m)
        print("    NAMED (re-asserted, typed): the register mirror sector "
              "(+,0,0) remains NON-AUTOMORPHIC -- no completed L-function "
              "has\n      +Lambda(n)/sqrt(n) atoms uniformly (1/zeta-type "
              "channel, zeros <-> poles swapped); it carries NO "
              "positivity demand\n      and is OUTSIDE the domain of the "
              "rule map.  The rule's domain is the automorphic register "
              "characters; this probe\n      extends the verified domain "
              "to their twists (closure under the register group law "
              "chi4 (x) f8-channel).")


    # ================================================================ verdict
    def verdict(ss3):
        section("VERDICT")
        n_pass = sum(1 for _n, ok in CHECKS if ok)
        n_all = len(CHECKS)
        print("%d/%d checks passed" % (n_pass, n_all))
        controls_ok = all(CONTROL_FIRED.get(c, False)
                          for c in ("C1", "C2", "C3"))
        rule_ok = all(ok for n, ok in CHECKS if n.startswith("R1"))
        twist_ok = ss3["psd"]["f8xchi4 (rule continuum)"]
        coher_ok = all(ss3["psd"].values())
        if not twist_ok:
            v = ("CONDUCTOR-AD-HOC (the twist sector FAILS with the "
                 "rule-derived continuum -- the assignment is a case "
                 "table after all)")
        elif not (rule_ok and controls_ok):
            v = "CONDUCTOR-PARTIAL (%s)" % (
                "rule instance gate failed" if not rule_ok else
                "control void: %s" % [c for c in ("C1", "C2", "C3")
                                      if not CONTROL_FIRED.get(c, False)])
        elif coher_ok and n_pass == n_all:
            v = "CONDUCTOR-FUNCTORIAL"
        else:
            fails = [n for n, ok in CHECKS if not ok]
            v = "CONDUCTOR-PARTIAL (%s)" % ("; ".join(fails[:3]))
        print("VERDICT: %s" % v)
        if v == "CONDUCTOR-FUNCTORIAL":
            print("""
CONDUCTOR-FUNCTORIALITY -- CONDUCTOR-FUNCTORIAL.  The assignment
chi -> continuum is ONE closed structure map, not a case table:
  * THE RULE (q^{s/2} prod Gamma_R(s + mu_j), universal per-factor
    kernel, ln q at lag 0, pole iff trivial) reproduces all deployed
    and sibling kernels as instances -- including the weight-4 kernel
    through the DUPLICATION identity, two independent quadrature
    structures agreeing to 1e-12.
  * THE SECOND CUSPIDAL SECTOR f8 (x) chi_{-4} (register-internal,
    conductor 16 by Atkin-Li + the Fricke ward, nothing hand-tuned)
    is PSD on the entire ladder with the rule-derived continuum.
  * FOUR-SECTOR COHERENCE holds (GL1 + chi4 + f8 + twist, same
    machinery), and the conductor datum is LOAD-BEARING: swapping in
    the q = 8 constant breaks the twist sector by ln 2 -- four orders
    of magnitude above the margins -- while the PSD margins pin the
    conductor from below to relative width ~1e-5.
  * WHAT REMAINS for PRIME.POSITIVE_DESCENT.01: the INFINITE-LEVEL CP
    EXTENSION -- (i) sector-PSD persistence X -> infinity per
    automorphic sector (GRH-type, unproven, the honest open core);
    (ii) the register-group closure of the rule map (all twists of
    the verified sectors -- finite-level machinery now exists);
    (iii) the carrier intertwiner landing on these explicit formulas
    exactly (Satake == packet recursion, verified in the sibling).""")
        print("total runtime %.1f s" % (time.time() - T0))
        return v


    def contract_update():
        section("RECOMMENDED CONTRACT UPDATE -- PRIME.POSITIVE_DESCENT.01 "
                "(report only; nothing written)")
        print("""\
    Demand (1) upgrades from 'sector-adapted continua exist
    finite-level' (sibling) to a FUNCTORIAL statement:
      (1-F) THE CONTINUUM FUNCTOR: on the automorphic register
            characters, chi -> Lambda_chi = q(chi)^{s/2}
            prod_j Gamma_R(s + mu_j(chi)) with (mu, q, pole) given by
            the closed rule (degree, weight/parity, ramified-register
            content); verified instances: GL1 (q=1, pole), chi4
            (q=4), f8 (q=8), f8 x chi4 (q=16).  The register group
            law is respected: the twist sector receives its continuum
            from the SAME rule with the Atkin-Li/Fricke conductor --
            no hand-tuning (gate C1 shows the conductor constant is
            load-bearing at ln 2 against ~1e-5 margins, and P0 shows
            the finite-level margins PIN the conductor from below).
      (2)   SECTOR-PSD PERSISTENCE (unchanged, now four sectors): the
            windows with rule-derived continua stay PSD as X -> oo in
            every automorphic sector -- the honest infinite-level
            core (GRH-type, unproven; finite-level margins all in the
            same thin-margin class with slow depth decay).
      (3)   THE CARRIER INTERTWINER (unchanged): must land sector by
            sector on EXACTLY these rule-derived explicit formulas.
    NEXT FALSIFIER (named): the INFINITE-LEVEL CP EXTENSION gate --
    formalize the finite-level windows as a net of CP maps on the
    packet algebra and identify the exact limit object whose
    positivity is demanded (the Weil/GRH positivity per sector); on
    the measurement side, the depth-trend decomposition (does the
    margin decay -0.24/X saturate or cross zero -- oscillation-aware,
    higher rungs).  STOP CONDITIONS unchanged: no RH/GRH claim,
    stop-list binding, deployed objects read-only.""")


    def main():
        print("=" * 74)
        print("CONDUCTOR-FUNCTORIALITY -- the rule map + the second "
              "cuspidal sector")
        print("(follow-up to F8SECTOR-PSD; parent chain: DESCENT-PARTIAL)")
        print("=" * 74)
        g0_firewall()
        lag = s1_rule()
        tw = s2_twist()
        ss3 = s3_sectors(lag, tw)
        s4_controls(lag, tw, ss3)
        v = verdict(ss3)
        _LAST2["verdict"] = v
        contract_update()
        n_pass = sum(1 for _n, ok in CHECKS if ok)
        return 0 if (n_pass == len(CHECKS)
                     and not v.startswith("CONDUCTOR-AD-HOC")) else 1

    rc = main()
    return rc, list(CHECKS)


def run():
    """run_all entry point (combined adjudication): part 1 must be 15/15
    (F8SECTOR-PSD), part 2 must be 16/16 (CONDUCTOR-FUNCTORIAL)."""
    rc1 = _run_part1()
    fails1 = [n for (n, ok) in CHECKS if not ok]
    v1 = _LAST1.get("verdict", "")
    part1_ok = (rc1 == 0 and not fails1 and len(CHECKS) == 15
                and v1 == "F8SECTOR-PSD")
    print("\n[%s] PART-1 PATTERN GATE: expected 15/15 (F8SECTOR-PSD) -- "
          "got %d checks, fails: %s, verdict: %s"
          % ("PASS" if part1_ok else "FAIL", len(CHECKS),
             fails1 or "none", v1))
    rc2, chks2 = _run_part2()
    fails2 = [n for (n, ok) in chks2 if not ok]
    v2 = _LAST2.get("verdict", "")
    part2_ok = (rc2 == 0 and not fails2 and len(chks2) == 16
                and v2 == "CONDUCTOR-FUNCTORIAL")
    print("\n[%s] PART-2 PATTERN GATE: expected 16/16 "
          "(CONDUCTOR-FUNCTORIAL) -- got %d checks, fails: %s, verdict: %s"
          % ("PASS" if part2_ok else "FAIL", len(chks2),
             fails2 or "none", v2))
    ok = part1_ok and part2_ok
    print("\nCOMBINED ADJUDICATION: %s -- F8SECTOR-PSD + "
          "CONDUCTOR-FUNCTORIAL: the sector-adapted-continua demand of "
          "PRIME.POSITIVE_DESCENT.01 passes its first falsifier (the f8 "
          "sector is PSD on the full ladder with its own weight-4/"
          "conductor-8/no-pole continuum; three-sector coherence) and the "
          "continuum assignment is ONE closed Gamma_R structure map, not a "
          "case table (duplication ward 2.7e-15; the second cuspidal "
          "sector f8 x chi_-4 lands PSD with the rule continuum at the "
          "Atkin-Li/Fricke conductor 16; the conductor datum load-bearing "
          "at exactly ln 2; four-sector coherence).  Sector PSD stays "
          "finite-level EVIDENCE -- GRH-type statements unproven.  "
          "NO RH/GRH claim."
          % ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(run())
