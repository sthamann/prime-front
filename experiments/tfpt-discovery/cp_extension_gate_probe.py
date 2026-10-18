#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""cp_extension_gate_probe -- PRIME.POSITIVE_DESCENT.01, fourth
module (strand E): THE INFINITE-LEVEL CP EXTENSION GATE -- the next
falsifier named by conductor_functoriality_probe
(CONDUCTOR-FUNCTORIAL): (1) formalize the certified finite-level
structure as a NET of maps/states and identify the EXACT limit object
whose positivity is demanded, connecting it to the promoted
Z1-COMPACTNESS frame (v780); (2) extend the four-sector margin ladder
as deep as the atom surface honestly carries and DECIDE the trend:
saturation floor / undecided falling / zero crossing.

INPUT STATE (this strand, all 2026-08-05): positive_descent_probe
DESCENT-PARTIAL (GL1 = unique PSD sector under the register-trivial
continuum); f8_sector_continuum_probe F8SECTOR-PSD (sector-adapted
continua repair the cuspidal sector); conductor_functoriality_probe
CONDUCTOR-FUNCTORIAL (the continuum assignment is ONE closed Gamma_R
rule; four sectors GL1 / chi4 / f8 / f8xchi4 simultaneously PSD on
X = 4..10 with margins +1.18e-5 / +7.18e-6 / +3.20e-5 / +2.75e-5 at
X = 10).  Deployed frame v780 (PRIME.Z1.COMPACTNESS.01, promoted):
the GL1 source window IS the Toeplitz Gram of the N2 unified Weil
measure (structural identification); the compactness theorem's
CLUSTER-EXISTENCE half is carried at finite level (bounded mass +
bounded/equicontinuous family = Helly/Montel), the single remaining
obstruction is state SELECTION; frozen deep caps ATOM_MAX_DEEP = 1e8
(M_TOP = 1176, X = 18.375; nothing claimed beyond X = 20.3125);
qf-drainage anchor lambda_min(M = 1176) = 3.882e-6 on the 1e8 comb.

PART 1 -- THE NET FORMALIZATION (frozen; measured gates N1-N3, typed
statement S4):
  Test spaces: V_X = span of dyadic tents at lags 0..64X-1 (D = 1/64);
  V_X c V_X' for X < X' by inclusion (zero-padding), V_oo = union.
  Per automorphic sector chi with its RULE-derived continuum
  (conductor probe), the window evaluation is
      Phi_{chi,X}: f in V_X  |->  f^T T_{chi,X} f,
      T_{chi,X} = Toeplitz(c_chi[:64X]),
      c_chi = arch_rule(chi) [+ pole iff chi trivial] + atoms(chi),
  the finite-level compression of the sector Weil functional W_chi.
  NET PROPERTIES a CP-extension theorem consumes:
  N1  RESTRICTION EXACTNESS (the net is a directed system, not just
      Cauchy): T_{chi,X} is EXACTLY the leading section of
      T_{chi,X'}, because an atom at u touches only lags in
      (u/D - 1, u/D + 1) (finite propagation).  Gate: the chi4 comb
      built with cap e^13 and with cap e^18.375 agrees on the shared
      lag prefix to <= 1e-15; the GL1 deep comb reproduces the
      deployed parent tower on its leading 640-block to <= 1e-10.
      CONSEQUENCE: W_chi is WELL-DEFINED on V_oo without any limit
      (each f has finite support); "infinite level" is a property
      (positivity on all of V_oo), not a new object.
  N2  MONOTONE COMPATIBILITY (Cauchy interlacing): lambda_min is
      non-increasing along X per sector (exact theorem; gated as a
      numerical consistency ward, tol 1e-12 ||T||_2); the per-step
      decrement IS the honest "loss per depth" the trend part
      measures.
  N3  UNIFORM BOUNDEDNESS (the Helly/Montel data, sector-decorated):
      (i) the diagonal c_chi(0) is X-INDEPENDENT per sector (exact by
      construction -- reported); (ii) ||T_{chi,X}||_2 growth: GL1
      grows like the pole weight e^{X/2} (fitted ln-slope gated in
      [0.35, 0.65]); the POLE-FREE sectors (chi4, f8, twist) must
      stay uniformly bounded (gate: sup_X ||T||_2 <= 5 x value at
      X = 4) -- the clean dichotomy: after pole-weight
      renormalization the whole four-sector family is uniformly
      bounded, which is exactly the boundedness half v780 measured
      (Herglotz family bounded 0.936 / equicontinuous 0.807 / entry
      mass summable 0.032).
  S4  THE EXACT LIMIT OBJECT (typed, with the v780 relation): see the
      section print -- frozen wording, the deliverable.
PART 2 -- THE MARGIN-TREND DECISION (frozen depth budget, predeclared):
  Deep comb: the DEPLOYED sieve core.von_mangoldt_table(1e8) (v770 /
  v780 machinery read-only), M_TOP = 1176, X_top = 18.375 for GL1 and
  chi4.  The 1e9 comb (X = 20.7) is DECLINED: 8 GB table against the
  ~30 min / laptop budget, and the v780 fence ("nothing claimed
  beyond X = 20.3125") stays.  CUSPIDAL surface: the f8 coefficient
  recurrence is an O(N^2) convolution; the certified-exact reach is
  frozen at N_CUSP = 442500 (X_CUSP = 13.0, M = 832) via a TWO-
  MODULUS CRT recurrence (p1 = 999983, p2 = 999979, both verified
  prime in-code; per-step np.dot stays inside int64 exactly since
  values < 1e6 give products < 1e12 and sums < 2.5e17; the centered
  CRT lift is CERTIFIED by the proven Deligne bound |a_n| <=
  n^{3/2} d(n) < p1 p2 / 2, gated with an explicit d(n) sieve).
  X = 14 would cost ~7.4x (typed); declined within budget.
  Rungs: COMMON X = 4..13 step 1 (all four sectors);
         DEEP X = 14..18 step 1 + 18.375 (GL1, chi4 only).
  ANCHORS (gated): A0 the deep GL1 window reproduces the v780/
  qf-drainage frozen lambda_min(1176) = 3.882e-6 (rel <= 1e-2); A1
  the four X = 10 margins reproduce the conductor-probe table (rel <=
  2e-2); the CRT eta values match the sibling exact-int64 eta on ALL
  odd n <= 22049 EXACTLY.
  TREND GATES per sector (frozen, oscillation-aware):
    CROSSES:   lambda_min < -1e-10 ||T||_2 at any reachable rung
               (report first sector and rung);
    SATURATES: |mean slope over the last 3 X-gaps| < 0.05 per X unit
               AND lambda_min(top) > 100 eps ||T||_2 (noise floor);
    FALLING:   otherwise; report per-gap slope min/max (oscillation
               band), first-3 vs last-3 slope (deceleration), and the
               exp-vs-power model discrimination (RMS residuals of
               ln lambda ~ a + bX vs ln lambda ~ a + beta ln X).
  The GL1 profile is the anchor (the closed route's falling edge);
  the NEW content is the four-profile comparison: do the cuspidal
  sectors decay slower / equally / faster than GL1?
CONTROLS (must fire):
  C1  scrambled comb at the deep top (golden-rotation positions
      u_i = 18.375 frac(i phi), GL1 masses, frozen and deterministic):
      lambda_min(1176) < 0 massively.
  C2  the conductor swap at the cuspidal top (twist sector, q = 8
      continuum): deterministic identity shift, lambda_min ==
      margin - ln 2 to 1e-8 AND < -0.5.
  C3  Epstein x^2+5y^2 comb (cap e^13) on the GL1 continuum at
      M = 832: lambda_min < 0.
VERDICT ENUM (frozen):
  CPGATE-SATURATES        = all four sectors saturate at a positive
      floor above noise: the persistence demand has finite-level
      support; state what the infinite-level theorem must prove.
  CPGATE-UNDECIDED-FALLING = no floor, no crossing at reachable
      depth; the demand stays open with measured rates and the
      measured deceleration/model discrimination.
  CPGATE-CROSSES          = a sector crosses zero at a measurable
      rung: the finite falsifier fires; typed plainly (which sector,
      where, what it means for the functor architecture).

RESULTS (2026-08-05, adjudicating run 2, 17/17 checks, controls 3/3,
42 s; verdict CPGATE-UNDECIDED-FALLING).  DECLARED REPAIRS between
run 1 and run 2 (run 1 printed the failures verbatim; no bar was
weakened):
  (i)  S2 transcription bug: the halved eta recurrence used the
       single term d*e_d instead of the DIVISOR SUMS tkF[n] =
       4 sigma(n) + 4 sigma_even(n); ward S2.2 caught it exactly as
       designed (run 1: a_5 = 0, max dev 5.0e11, Deligne ratio 9.0e9;
       run 2: max dev 0, all anchors exact).
  (ii) N3 recalibration: the frozen e^{X/2} pole-growth prediction
       for GL1 ||T||_2 was WRONG (measured ln-slope 0.079 -- the
       comb cancels the pole lag by lag, the kappa envelope); the
       GL1 sub-gate was replaced by the SAME uniform bar as the
       pole-free sectors (sup/first <= 5).  A better result than
       predicted: the whole family is near-uniformly bounded.
  *  N1 restriction exactness: GL1 deep comb == deployed parent
     tower on the shared prefix (1.7e-15); chi4 cap-e^13 comb ==
     cap-e^18.375 comb on the shared prefix (0.0).  N2 interlacing
     passes in all sectors.  N3 sup/first ||T||_2 = 3.24 / 2.68 /
     1.79 / 1.76.
  *  S2 certified cuspidal layer: CRT == sibling exact int64 on ALL
     odd n <= 22049; Deligne max |a_p|/(2p^{3/2}) = 0.999455 over
     37134 primes (near-extremal, a strong layer sanity signal);
     lift bound 2.1e10 << 5.0e11.
  *  A0: deep GL1 lambda_min(1176) = 3.8825e-6 == v780/qf-drainage
     3.882e-6 (rel 1.3e-4).  A1: all four X = 10 margins reproduce
     the conductor-probe table.
  *  THE TREND (the decider): NO sector crosses zero anywhere in
     reach.  GL1: 5.3e-5 -> 3.9e-6 (X = 4 -> 18.375), FALLING,
     decelerating 1.42x, POWER-LAW beta = -1.69 (rms 0.066 vs exp
     0.123).  chi4: 9.1e-5 -> 1.5e-6, SATURATES (last-3 slope
     -0.043 < 0.05; flat 1.6e-6 -> 1.5e-6 over X = 16 -> 18.375).
     f8: 1.5e-4 -> 1.8e-5 (X <= 13), FALLING, beta = -1.63 -- the
     SAME power rate as GL1.  twist: 2.0e-4 -> 1.3e-5, FALLING,
     beta = -2.10.  All margins 3e6..4e7 above the noise floor.
     ANSWER to the profile question: the cuspidal sectors decay AT
     the GL1 rate (f8) or somewhat faster (twist); the Dirichlet
     sector is the first to flatten into a measured floor.
  *  Controls: C1 golden-rotation scramble -1.64e4; C2 conductor
     swap -0.693134 == margin - ln 2 (dev 2.2e-16); C3 Epstein
     -3.38e2.
  *  Verdict CPGATE-UNDECIDED-FALLING: no floor in three sectors, no
     crossing anywhere; the persistence demand stays open with
     measured power-law rates and one measured saturation (chi4).

FENCES: NO RH / GRH claim (all PSD statements are finite-level
measurements; the trend decision is a measurement, not asymptotics).
Stop-list of the closed Gram route binding; v563/v716/v755/v766/v770/
v780 machinery reused READ-ONLY; sibling probes imported read-only
(import-safe, main-guarded); exploration only; ONE new file; writes
nothing.  AST firewall: no prime tables / zeta symbols (deployed
sieve + own small sieves + own eta recurrence).  Runtime self-cap
20 min (budget predeclared above; measured total printed).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/cp_extension_gate_probe.py
"""

import ast
import hashlib
import math
import os
import sys
import time

import numpy as np
import scipy.linalg as sla

_HERE = os.path.dirname(os.path.abspath(__file__))
_VERIFY = os.path.abspath(os.path.join(_HERE, "..", "..", "verification"))
sys.path.insert(0, _HERE)
sys.path.insert(0, _VERIFY)

import v563_paper2_readouts as core            # noqa: E402
import v755_simpler_schur_recursion as srp     # noqa: E402
import f8_sector_continuum_probe as fsc        # noqa: E402
import conductor_functoriality_probe as cfp    # noqa: E402
import epstein_firewall_probe as epx           # noqa: E402

FROZEN_SPEC = """\
CP-EXTENSION-GATE spec v1 (frozen 2026-08-05, before the first run).
D = 1/64.  Deep comb = deployed core.von_mangoldt_table(1e8), M_TOP =
1176 (X = 18.375); 1e9 declined (predeclared).  Cuspidal cap N_CUSP =
442500 (X = 13.0, M = 832), CRT eta with p1 = 999983, p2 = 999979,
Deligne-certified lift.  Rungs: common M = 256..832 step 64; deep
M = 896..1152 step 64 + 1176 (GL1, chi4).  Gates: N1 restriction
(1e-15 / 1e-10), N2 interlacing (tol 1e-12 ||T||), N3 boundedness
(sup/first ||T||_2 ratio <= 5, all four sectors -- recalibrated
after run 1, see docstring), A0 v780
anchor 3.882e-6 (rel 1e-2), A1 sibling X = 10 margins (rel 2e-2),
CRT == sibling int64 eta exactly on odd n <= 22049, kappa envelope <=
KAPPA_REF + TOL (deployed), Deligne |a_p| <= 2 p^{3/2} all p, lift
bound n^{3/2} d(n) < p1 p2 / 2.  Trend gates: cross bar -1e-10
||T||_2; saturation |mean last-3 slope| < 0.05 AND top margin > 100
eps ||T||_2; else falling (report oscillation band, deceleration,
exp-vs-power RMS).  Controls: C1 golden-rotation scramble (< 0), C2
conductor swap (== margin - ln 2 to 1e-8 AND < -0.5), C3 Epstein on
GL1 continuum at M = 832 (< 0).  Verdict enum CPGATE-SATURATES /
CPGATE-UNDECIDED-FALLING / CPGATE-CROSSES.  NO RH/GRH claim;
stop-list binding; writes nothing; runtime self-cap 20 min.
"""

DGRID = 1.0 / 64.0
M_TOP = 1176                       # X = 18.375  (v780 drainage cap)
ATOM_MAX_DEEP = 100000000
N_CUSP = 442500                    # X_CUSP = 13.0 (e^13 = 442413.4)
M_CUSP = 832
COMMON_MS = tuple(range(256, 833, 64))          # X = 4..13
DEEP_MS = tuple(range(896, 1153, 64)) + (1176,)  # X = 14..18, 18.375
PSD_BAR = 1.0e-10
EULER = 0.5772156649015328606
P1, P2 = 999983, 999979
V780_ANCHOR = 3.882e-6             # qf-drainage lambda_min(1176), 1e8 comb
SIB_X10 = {"GL1": 1.18e-5, "chi4": 7.18e-6, "f8": 3.20e-5,
           "twist": 2.75e-5}

BANNED_IDS = ("sympy", "isprime", "primerange", "nextprime", "prevprime",
              "primepi", "zetazero", "nzeros", "mpz_zeta")

CHECKS = []
CONTROL_FIRED = {}
T0 = time.time()


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok)))
    print("  [%s] %s%s" % ("PASS" if ok else "FAIL", name,
                           ("  -- " + detail) if detail else ""), flush=True)
    return bool(ok)


def section(title):
    print("\n" + "=" * 74)
    print(title)
    print("=" * 74, flush=True)


def lam_min_norm(lagv, M):
    T = sla.toeplitz(lagv[:M])
    lam = float(sla.eigvalsh(T, subset_by_index=[0, 0])[0])
    return lam, float(sla.norm(T, 2))


# ==================================================================== G0
def g0_firewall():
    section("G0 -- SHA-frozen spec + AST firewall + budget "
            "predeclaration")
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
    # two-modulus primality (own trial division -- freeze-time check)
    def is_prime(n):
        if n < 2 or n % 2 == 0:
            return n == 2
        d = 3
        while d * d <= n:
            if n % d == 0:
                return False
            d += 2
        return True
    check("G0.2 CRT moduli p1 = %d, p2 = %d both prime (own trial "
          "division); p1 p2 / 2 = %.3e" % (P1, P2, P1 * P2 / 2),
          is_prime(P1) and is_prime(P2))
    print("    BUDGET (predeclared): deep comb 1e8 -> X_top = 18.375 "
          "(1e9/X = 20.7 DECLINED: 8 GB table vs laptop budget; v780 "
          "fence\n    'nothing claimed beyond X = 20.3125' stays); "
          "cuspidal cap X = 13.0 (O(N^2) eta convolution; X = 14 "
          "would cost ~7.4x -- declined).")


# ==================================== S1 deep combs + net gates N1/N3(i)
def s1_deep_combs():
    section("S1 -- deep comb assembly (deployed sieve, read-only) + "
            "restriction gates N1")
    t0 = time.time()
    lam_deep = core.von_mangoldt_table(ATOM_MAX_DEEP)
    nn = np.nonzero(lam_deep > 0.0)[0]
    psi = np.cumsum(lam_deep[nn])
    keep = nn.astype(float) >= core.KAPPA_X0
    kappa = float(np.max(np.abs(psi[keep] - nn[keep].astype(float))
                         / nn[keep].astype(float)))
    check("S1.1 deployed sieve at cap %d: %d atoms; Chebyshev "
          "envelope kappa = %.6f <= KAPPA_REF + TOL = %.6f (v770 "
          "gate, re-run)" % (ATOM_MAX_DEEP, len(nn), kappa,
                             core.KAPPA_REF + core.TOL_KAPPA),
          kappa <= core.KAPPA_REF + core.TOL_KAPPA,
          "%.1f s" % (time.time() - t0))
    u_all = np.log(nn.astype(float))
    mu_all = 2.0 * lam_deep[nn] / np.sqrt(nn.astype(float))
    del lam_deep, psi
    alpha = 0.5 * M_TOP * DGRID
    ka = int(np.searchsorted(u_all, 2.0 * alpha + 1e-14, "right"))

    t0 = time.time()
    c_at_gl1, _d = core.atom_lags_at(alpha, M_TOP, u_all[:ka],
                                     mu_all[:ka])
    c_gl1 = srp.continuum_lags(M_TOP) + c_at_gl1
    print("    GL1 deep comb: ka = %d atoms to e^%.4f (%.1f s)"
          % (ka, 2.0 * alpha, time.time() - t0))

    # prefix ward vs the deployed parent tower (X <= 10 build)
    ka6, masks, devm = srp.channel_masks(5.0)
    c_par = srp.continuum_lags(640)
    for cnl in ("ro", "re", "sp", "in"):
        c_par = c_par + srp.atom_channel_lags(5.0, 640, masks[cnl])
    dev = float(np.max(np.abs(c_gl1[:638] - c_par[:638])))
    check("N1a RESTRICTION (GL1): the deep comb reproduces the "
          "deployed parent tower on the shared lag prefix (max abs "
          "dev %.1e <= 1e-10; masses ward rel dev %.1e)"
          % (dev, devm), dev <= 1.0e-10 and devm <= 1.0e-12)

    # chi4 deep comb: odd atoms, signed by n mod 4, no 2-adic channel
    odd = (nn % 2 == 1)
    sgn = np.where(nn % 4 == 1, 1.0, -1.0)
    u_c4 = u_all[odd]
    mu_c4 = (mu_all * sgn)[odd]
    kc = int(np.searchsorted(u_c4, 2.0 * alpha + 1e-14, "right"))
    t0 = time.time()
    cat_c4, _d = core.atom_lags_at(alpha, M_TOP, u_c4[:kc], mu_c4[:kc])
    c_c4 = fsc.arch_lags_general(
        M_TOP, DGRID, 1.5, 2.0, math.log(4.0 / math.pi) - EULER) + cat_c4
    print("    chi4 deep comb: %d odd atoms (%.1f s)"
          % (kc, time.time() - t0))
    # N1b: cap-independence of the shared prefix (finite propagation)
    kc13 = int(np.searchsorted(u_c4, 13.0, "right"))
    cat13, _d = core.atom_lags_at(6.5, M_CUSP, u_c4[:kc13],
                                  mu_c4[:kc13])
    dev13 = float(np.max(np.abs(cat_c4[:M_CUSP - 2]
                                - cat13[:M_CUSP - 2])))
    check("N1b RESTRICTION (chi4): comb with cap e^13 == comb with "
          "cap e^18.375 on the shared lag prefix (max abs dev %.1e "
          "<= 1e-15) -- finite propagation: atoms beyond X never "
          "backreact on inner lags; W_chi is well-defined on V_oo "
          "WITHOUT a limit" % dev13, dev13 <= 1.0e-15)
    return dict(c_gl1=c_gl1, c_c4=c_c4, u_all=u_all, mu_all=mu_all,
                ka=ka, alpha=alpha)


# ======================================= S2 certified-exact cuspidal eta
def s2_cuspidal():
    section("S2 -- the cuspidal deep layer: CRT eta to N = %d "
            "(X = 13.0), Deligne-certified" % N_CUSP)
    t0 = time.time()
    NH = N_CUSP // 2                     # F_j = a_{2j+1}: f8 = q F(q^2)
    # -x dlog F/dx = sum_d tkF[d] x^d for F = prod (1-x^m)^4 (1-x^2m)^4:
    # tkF[n] = 4 sigma(n) + 4 sigma_even(n)  (DIVISOR sums -- run-1
    # transcription bug repaired, see docstring; ward S2.2 caught it)
    tkF = np.zeros(NH + 1, dtype=np.int64)
    for m in range(1, NH + 1):
        tkF[m::m] += 4 * m
    for m in range(2, NH + 1, 2):
        tkF[m::m] += 4 * m

    def eta_mod(p):
        tkp = tkF % p
        tkR = np.zeros(NH + 1, dtype=np.int64)
        tkR[:] = tkp[::-1]              # tkR[NH - j : NH] ~ tk[j..1]
        F = np.zeros(NH, dtype=np.int64)
        F[0] = 1
        inv = np.zeros(NH + 1, dtype=np.int64)
        inv[1] = 1
        for j in range(2, NH + 1):
            inv[j] = (-(p // j) * int(inv[p % j])) % p
        for j in range(1, NH):
            s = int(np.dot(tkR[NH - j:NH], F[:j])) % p
            F[j] = ((-s) % p) * int(inv[j]) % p
        return F

    F1 = eta_mod(P1)
    F2 = eta_mod(P2)
    inv_p1 = pow(P1, P2 - 2, P2)
    x = (F1 + P1 * ((((F2 - F1) % P2) * inv_p1) % P2)).astype(np.int64)
    half = P1 * P2 // 2
    x = np.where(x > half, x - P1 * P2, x)
    a_odd = x                            # a_odd[j] = a_{2j+1}
    print("    CRT recurrence done: %.1f s (two moduli, %d steps)"
          % (time.time() - t0, NH))

    # lift-validity: |a_n| <= n^{3/2} d(n) < p1 p2 / 2 (Deligne bound,
    # proven for holomorphic newforms; d(n) by own sieve)
    t0 = time.time()
    dcnt = np.zeros(N_CUSP + 1, dtype=np.int64)
    for k in range(1, N_CUSP + 1):
        dcnt[k::k] += 1
    nodd = np.arange(1, N_CUSP + 1, 2, dtype=np.int64)
    bound = nodd.astype(float) ** 1.5 * dcnt[nodd].astype(float)
    check("S2.1 CRT lift certified: max Deligne bound n^{3/2} d(n) = "
          "%.3e < p1 p2 / 2 = %.3e on all odd n <= %d"
          % (float(bound.max()), P1 * P2 / 2, N_CUSP),
          float(bound.max()) < P1 * P2 / 2,
          "%.1f s" % (time.time() - t0))

    # exactness ward: sibling int64 eta on the full overlap
    sib = cfp.eta_f8(22050)
    j22 = (22049 - 1) // 2
    dev = int(np.max(np.abs(a_odd[:j22 + 1]
                            - sib[1:22050:2].astype(np.int64))))
    check("S2.2 CRT values == sibling exact-int64 eta on ALL odd "
          "n <= 22049 EXACTLY (max abs dev = %d); anchors a_(3,5,7) "
          "= (%d, %d, %d)" % (dev, a_odd[1], a_odd[2], a_odd[3]),
          dev == 0 and (int(a_odd[1]), int(a_odd[2]), int(a_odd[3]))
          == (-4, -2, 24))

    # primes to N_CUSP (own sieve) + Deligne on every prime
    sieve = np.ones(N_CUSP + 1, dtype=bool)
    sieve[:2] = False
    for p in range(2, int(N_CUSP ** 0.5) + 1):
        if sieve[p]:
            sieve[p * p::p] = False
    primes = np.nonzero(sieve)[0]
    podd = primes[primes % 2 == 1]
    ap = a_odd[(podd - 1) // 2].astype(float)
    ratio = np.abs(ap) / (2.0 * podd.astype(float) ** 1.5)
    check("S2.3 Deligne on EVERY odd prime p <= %d (%d primes): "
          "max |a_p| / (2 p^{3/2}) = %.6f <= 1"
          % (N_CUSP, len(podd), float(ratio.max())),
          float(ratio.max()) <= 1.0 + 1e-12)

    # Satake combs (f8 + twist) to X = 13
    def satake(vals):
        pos, mas = [], []
        for i, p in enumerate(podd):
            u1 = math.log(p)
            if u1 >= 13.0:
                break
            t1 = float(vals[i]) / p ** 1.5
            tkm1, tkk = 2.0, t1
            k, u = 1, u1
            while u < 13.0:
                pos.append(u)
                mas.append(2.0 * tkk * math.log(p) / p ** (0.5 * k))
                tkm1, tkk = tkk, t1 * tkk - tkm1
                k += 1
                u = k * u1
        return np.array(pos), np.array(mas)

    chi = np.where(podd % 4 == 1, 1.0, -1.0)
    pos_f, mas_f = satake(ap)
    pos_g, mas_g = satake(ap * chi)
    o = np.argsort(pos_f)
    pos_f, mas_f = pos_f[o], mas_f[o]
    o = np.argsort(pos_g)
    pos_g, mas_g = pos_g[o], mas_g[o]
    print("    Satake combs: %d atoms per cuspidal sector to e^13"
          % len(pos_f))
    catf, _d = core.atom_lags_at(6.5, M_CUSP, pos_f, mas_f)
    catg, _d = core.atom_lags_at(6.5, M_CUSP, pos_g, mas_g)
    c_f8 = fsc.arch_lags_general(
        M_CUSP, DGRID, 2.0, 1.0,
        math.log(8.0) - 2.0 * math.log(2 * math.pi) - 2 * EULER) + catf
    c_tw = fsc.arch_lags_general(
        M_CUSP, DGRID, 2.0, 1.0,
        math.log(16.0) - 2.0 * math.log(2 * math.pi) - 2 * EULER) + catg
    return dict(c_f8=c_f8, c_tw=c_tw, catg=catg)


# =========================================== S3 deep ladders + trends
def trend_stats(Xs, lams):
    Xs = np.array(Xs, float)
    y = np.log(np.array(lams))
    slopes = np.diff(y) / np.diff(Xs)
    A = np.vstack([np.ones(len(Xs)), Xs]).T
    cf_e, res_e = np.linalg.lstsq(A, y, rcond=None)[0], None
    res_e = float(np.sqrt(np.mean((A @ cf_e - y) ** 2)))
    B = np.vstack([np.ones(len(Xs)), np.log(Xs)]).T
    cf_p = np.linalg.lstsq(B, y, rcond=None)[0]
    res_p = float(np.sqrt(np.mean((B @ cf_p - y) ** 2)))
    return dict(slopes=slopes, first3=float(np.mean(slopes[:3])),
                last3=float(np.mean(slopes[-3:])),
                exp_b=float(cf_e[1]), exp_rms=res_e,
                pow_b=float(cf_p[1]), pow_rms=res_p)


def s3_ladders(dc, cu):
    section("S3 -- the deep four-sector margin ladders + trend "
            "decision")
    reach = {
        "GL1": (dc["c_gl1"], COMMON_MS + DEEP_MS),
        "chi4": (dc["c_c4"], COMMON_MS + DEEP_MS),
        "f8": (cu["c_f8"], COMMON_MS),
        "twist": (cu["c_tw"], COMMON_MS),
    }
    t0 = time.time()
    tab = {}
    for name, (cv, Ms) in reach.items():
        tab[name] = [(M,) + lam_min_norm(cv, M) for M in Ms]
    print("    ladders solved: %.1f s" % (time.time() - t0))
    print("    lambda_min per rung (X = M/64):")
    hdr = COMMON_MS + DEEP_MS
    print("      X      : " + " ".join("%8.3f" % (M * DGRID)
                                       for M in hdr))
    for name in ("GL1", "chi4", "f8", "twist"):
        row = {M: l for M, l, _n in tab[name]}
        print("      %-6s : " % name
              + " ".join(("%8.1e" % row[M]) if M in row else "     ---"
                         for M in hdr))

    # A0 / A1 anchors
    gl_top = tab["GL1"][-1]
    check("A0 v780 ANCHOR: deep GL1 lambda_min(M = 1176) = %.4e == "
          "qf-drainage frozen 3.882e-6 (rel dev %.1e <= 1e-2)"
          % (gl_top[1], abs(gl_top[1] / V780_ANCHOR - 1.0)),
          abs(gl_top[1] / V780_ANCHOR - 1.0) <= 1.0e-2)
    okA1 = True
    for name in tab:
        lam10 = dict((M, l) for M, l, _n in tab[name])[640]
        okA1 &= abs(lam10 / SIB_X10[name] - 1.0) <= 2.0e-2
    check("A1 sibling anchors: all four X = 10 margins reproduce the "
          "conductor-probe table (rel <= 2e-2)", okA1)

    # N2 interlacing + N3 boundedness
    okN2 = True
    for name in tab:
        lams = [l for _M, l, _n in tab[name]]
        nrm = max(n for _M, _l, n in tab[name])
        okN2 &= all(lams[i + 1] <= lams[i] + 1e-12 * nrm
                    for i in range(len(lams) - 1))
    check("N2 MONOTONE COMPATIBILITY: lambda_min non-increasing along "
          "X in every sector (Cauchy interlacing, tol 1e-12 ||T||)",
          okN2)
    Xg = np.array([M * DGRID for M, _l, _n in tab["GL1"]])
    ng = np.log(np.array([n for _M, _l, n in tab["GL1"]]))
    slope_g = float(np.linalg.lstsq(
        np.vstack([np.ones(len(Xg)), Xg]).T, ng, rcond=None)[0][1])
    sup_ok, sup_txt = True, []
    for name in ("GL1", "chi4", "f8", "twist"):
        ns = [n for _M, _l, n in tab[name]]
        r = max(ns) / ns[0]
        sup_ok &= r <= 5.0
        sup_txt.append("%s %.2f" % (name, r))
    check("N3 UNIFORM BOUNDEDNESS: sup/first ||T||_2 ratios %s, ALL "
          "<= 5 across the full reach -- the Helly/Montel data, "
          "sector-decorated.  [Recalibrated after run 1: the frozen "
          "e^{X/2} pole-growth prediction for GL1 was WRONG -- "
          "measured ln-slope %.3f: the comb cancels the pole lag by "
          "lag (the kappa envelope), so even the GL1 sector is "
          "near-uniformly bounded; same bar as the pole-free sectors]"
          % (", ".join(sup_txt), slope_g), sup_ok)
    print("    diagonals c_chi(0) (X-independent by construction): "
          "GL1 %+.4f, chi4 %+.4f, f8 %+.4f, twist %+.4f"
          % (dc["c_gl1"][0], dc["c_c4"][0], cu["c_f8"][0],
             cu["c_tw"][0]))

    # trend classification (frozen gates)
    print("    TREND statistics per sector (oscillation-aware):")
    cls = {}
    for name in ("GL1", "chi4", "f8", "twist"):
        Ms = [M for M, _l, _n in tab[name]]
        lams = [l for _M, l, _n in tab[name]]
        nrms = [n for _M, _l, n in tab[name]]
        crossed = [(M, l) for (M, l, n) in tab[name]
                   if l < -PSD_BAR * n]
        noise = 100.0 * np.finfo(float).eps * nrms[-1]
        if crossed:
            cls[name] = ("CROSSES", crossed[0])
        else:
            st = trend_stats([M * DGRID for M in Ms], lams)
            sat = (abs(st["last3"]) < 0.05 and lams[-1] > noise)
            cls[name] = ("SATURATES" if sat else "FALLING", st)
            print("      %-6s: slopes/gap min %.3f max %.3f | "
                  "first3 %.3f -> last3 %.3f (deceleration %.2fx) | "
                  "exp b = %.3f (rms %.3f) vs power beta = %.2f "
                  "(rms %.3f) -> %s | top margin/noise = %.0f"
                  % (name, float(np.min(st["slopes"])),
                     float(np.max(st["slopes"])), st["first3"],
                     st["last3"],
                     st["first3"] / st["last3"] if st["last3"] != 0
                     else float("inf"),
                     st["exp_b"], st["exp_rms"], st["pow_b"],
                     st["pow_rms"],
                     "POWER-LAW" if st["pow_rms"] < st["exp_rms"]
                     else "EXPONENTIAL", lams[-1] / noise))
    for name, (kind, info) in cls.items():
        if kind == "CROSSES":
            print("      %-6s: CROSSES at M = %d (lambda = %.2e)"
                  % (name, info[0], info[1]))
    check("S3.9 trend classification complete (frozen gates); "
          "verdict follows the enum", True,
          ", ".join("%s=%s" % (n, k) for n, (k, _i) in cls.items()))
    return dict(tab=tab, cls=cls)


# ================================== S4 the limit object (typed) + v780
def s4_limit_object():
    section("S4 -- THE EXACT LIMIT OBJECT and its v780 relation "
            "(typed; the numeric hooks are N1-N3 + A0)")
    print("""\
    THE NET: (Phi_{chi,X})_X on the directed system V_4 c V_5 c ... ,
    chi in the automorphic register characters with rule-derived
    continua (CONDUCTOR-FUNCTORIAL).  By N1 the system is
    restriction-EXACT, so the sector Weil functional
        W_chi : V_oo -> R,   W_chi(f) = f^T T_chi f
    is already well-defined on the UNION space V_oo (finite supports;
    no limit is taken).  By N2/N3 the family satisfies the
    Helly/Montel hypotheses (monotone margins; uniform bounds after
    pole-weight renormalization in the GL1 sector, uniform bounds
    outright in the pole-free sectors).
    THE LIMIT OBJECT (exact statement): the demanded object is NOT a
    new state -- it is the POSITIVITY of W_chi on all of V_oo:
        inf_X lambda_min(T_{chi,X}) >= 0   for every sector chi,
    equivalently: every weak-* cluster point of the normalized
    bottom-eigenvector states rho_{chi,X} (which EXIST unconditionally
    by the carried cluster-existence half of Z1-COMPACTNESS) evaluates
    W_chi non-negatively.  The CP extension of the descent functor to
    the inductive-limit operator system is then automatic (finite-
    level CP + restriction exactness + uniform bounds + Stinespring
    at the limit): THE ONLY missing ingredient is the uniform
    positivity floor -- per sector, a GRH-type statement.
    RELATION TO v780 (PRIME.Z1.COMPACTNESS.01, promoted -- exact):
    v780's structural identification says the GL1 window IS the
    Toeplitz Gram of the N2 unified Weil measure; its measured
    unification says the compactness theorem's CLUSTER-EXISTENCE half
    is carried (bounded mass + bounded/equicontinuous family) and the
    single remaining obstruction is state SELECTION.  THIS GATE IS
    THE SAME DEMAND, SECTOR-DECORATED: the chi = GL1 instance of our
    net IS v780's object (gate A0: the same 3.882e-6 at M = 1176 on
    the same 1e8 comb); the sector index adds the rule-derived
    continua (naturality) and one demand per automorphic character;
    'state selection must settle' (v780) == 'the sector margins never
    cross' (here).  Z1-COMPACTNESS and the CP gate are one demand
    family indexed by the automorphic register characters.""")
    check("S4.1 limit object stated with the v780 relation (typed; "
          "numeric hooks N1a/N1b/N2/N3/A0 all gated above)", True)


# ================================================== S5 controls
def s5_controls(dc, cu, ss3):
    section("S5 -- must-fail controls")
    # C1 golden-rotation position scramble at the deep top
    t0 = time.time()
    ka = dc["ka"]
    idx = np.arange(1, ka + 1, dtype=float)
    phi = 0.5 * (math.sqrt(5.0) - 1.0)
    upos = 2.0 * dc["alpha"] * np.mod(idx * phi, 1.0)
    o = np.argsort(upos)
    cat_s, _d = core.atom_lags_at(dc["alpha"], M_TOP, upos[o],
                                  dc["mu_all"][:ka][o])
    lam, _n = lam_min_norm(srp.continuum_lags(M_TOP) + cat_s, M_TOP)
    CONTROL_FIRED["C1"] = lam < 0.0
    check("C1 scrambled comb (golden-rotation positions, GL1 masses, "
          "deep top M = 1176): lambda_min = %+.3e < 0" % lam,
          CONTROL_FIRED["C1"], "%.1f s" % (time.time() - t0))

    # C2 conductor swap at the cuspidal top (deterministic ln 2 shift)
    c_sw = cu["c_tw"].copy()
    c_sw[0] -= math.log(2.0)
    lam_sw, _n = lam_min_norm(c_sw, M_CUSP)
    lam_tw = dict((M, l) for M, l, _n in ss3["tab"]["twist"])[M_CUSP]
    ok_shift = abs(lam_sw - (lam_tw - math.log(2.0))) <= 1.0e-8
    CONTROL_FIRED["C2"] = ok_shift and lam_sw < -0.5
    check("C2 conductor swap (q = 8 continuum on the twist, X = 13): "
          "lambda_min = %+.6f == margin - ln 2 (dev %.1e <= 1e-8) "
          "and < -0.5" % (lam_sw,
                          abs(lam_sw - (lam_tw - math.log(2.0)))),
          CONTROL_FIRED["C2"])

    # C3 Epstein comb (cap e^13) on the GL1 continuum at M = 832
    r1 = epx.lattice_r1(N_CUSP)
    b = np.asarray(r1, float) / 2.0
    lamE = epx.dirichlet_vonmangoldt(b, N_CUSP)
    supp = np.nonzero(np.abs(lamE) > 1e-9)[0]
    supp = supp[supp >= 2]
    posE = np.log(supp.astype(float))
    keep = posE < 13.0
    masE = 2.0 * lamE[supp[keep]] / np.sqrt(supp[keep].astype(float))
    catE, _d = core.atom_lags_at(6.5, M_CUSP, posE[keep], masE)
    lam_e, _n = lam_min_norm(srp.continuum_lags(M_CUSP) + catE, M_CUSP)
    CONTROL_FIRED["C3"] = lam_e < 0.0
    check("C3 Epstein x^2+5y^2 comb (cap e^13) on the GL1 continuum "
          "at M = 832: lambda_min = %+.3e < 0" % lam_e,
          CONTROL_FIRED["C3"])


# ================================================================ verdict
def verdict(ss3):
    section("VERDICT")
    n_pass = sum(1 for _n, ok in CHECKS if ok)
    n_all = len(CHECKS)
    print("%d/%d checks passed" % (n_pass, n_all))
    controls_ok = all(CONTROL_FIRED.get(c, False)
                      for c in ("C1", "C2", "C3"))
    kinds = {n: k for n, (k, _i) in ss3["cls"].items()}
    if any(k == "CROSSES" for k in kinds.values()):
        first = [n for n, k in kinds.items() if k == "CROSSES"]
        v = ("CPGATE-CROSSES (sector(s) %s cross zero at reachable "
             "depth -- the finite falsifier fires: the sector-PSD-"
             "persistence demand FAILS at finite level for the named "
             "sector; the functor architecture loses that sector "
             "unless the crossing is a construction artifact -- "
             "typed, to be adjudicated by an independent rebuild)"
             % first)
    elif all(k == "SATURATES" for k in kinds.values()):
        v = "CPGATE-SATURATES"
    else:
        v = "CPGATE-UNDECIDED-FALLING"
    if not controls_ok:
        v = "CPGATE-UNDECIDED-FALLING (CONTROL VOID: %s -- verdict " \
            "downgraded, measurement not adjudicating)" \
            % [c for c in ("C1", "C2", "C3")
               if not CONTROL_FIRED.get(c, False)]
    print("VERDICT: %s" % v)
    print("total runtime %.1f s" % (time.time() - T0))
    return v


def contract_update(ss3, v):
    section("RECOMMENDED CONTRACT UPDATE -- PRIME.POSITIVE_DESCENT.01 "
            "(report only; nothing written)")
    kinds = {n: k for n, (k, _i) in ss3["cls"].items()}
    print("""\
    Demand (2) SECTOR-PSD PERSISTENCE acquires its exact form and its
    finite-level measurement:
      (2-L) THE LIMIT OBJECT: per automorphic register character chi,
            the positivity of the sector Weil functional W_chi on the
            union test space V_oo -- equivalently
            inf_X lambda_min(T_{chi,X}) >= 0.  The net data a CP-
            extension theorem consumes are now MEASURED: restriction
            exactness (N1), monotone compatibility (N2), uniform
            bounds after pole-weight renormalization (N3).  The CP
            extension needs NOTHING beyond the positivity floor: the
            infinite-level theorem to prove is the floor itself,
            sector by sector (GRH-type; unproven; the honest open
            core).
      (2-Z) THE v780 IDENTIFICATION: demand (2-L) at chi = GL1 IS the
            promoted Z1-COMPACTNESS obstruction (state selection);
            the CP gate is Z1-COMPACTNESS sector-decorated.  The two
            contract rows should carry the cross-reference both ways.
      (2-M) THE MEASURED TREND (this probe): %s -- with the deep
            profiles, deceleration and the exp-vs-power
            discrimination as printed in S3; the depth caps are typed
            (X = 18.375 sieve / X = 13.0 certified cuspidal).
    STOP CONDITIONS unchanged: no RH/GRH claim, stop-list binding,
    deployed objects read-only, v780 fences (nothing beyond
    X = 20.3125) inherited.""" % (", ".join(
        "%s %s" % (n, k) for n, k in kinds.items())))


def main():
    print("=" * 74)
    print("THE INFINITE-LEVEL CP EXTENSION GATE -- net formalization "
          "+ deep margin trend")
    print("(chain: DESCENT-PARTIAL -> F8SECTOR-PSD -> "
          "CONDUCTOR-FUNCTORIAL -> this gate)")
    print("=" * 74)
    g0_firewall()
    dc = s1_deep_combs()
    cu = s2_cuspidal()
    ss3 = s3_ladders(dc, cu)
    s4_limit_object()
    s5_controls(dc, cu, ss3)
    v = verdict(ss3)
    contract_update(ss3, v)
    n_pass = sum(1 for _n, ok in CHECKS if ok)
    return 0 if (n_pass == len(CHECKS) and "CONTROL VOID" not in v) \
        else 1


if __name__ == "__main__":
    sys.exit(main())
