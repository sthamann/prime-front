#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""positive_descent_probe -- PRIME.POSITIVE_DESCENT.01 (positive-protocol
round, strand E): the first finite-level version of the completely
positive functor from the extended packet register to the GL1/Weil
state, and the decision of what carries.

THE STRATEGIC IDEA (frozen; the user's Section 19 with the positive
algebra concrete): do NOT control the signed sequence directly.  Work
in the positive algebra N[C2] (x) N[F2^4] (x) N[mu4] (the extended
packet register), build the positive correspondence operator / state
THERE, run GNS, and apply the sign characters ONLY AFTER.  The
candidate RH-relevant statement becomes: "the GL1 descent is a
completely positive functor of the extended packet state" -- the
sign-carrier lives BEFORE character evaluation; signedness is observer
projection.

THE REGISTER (frozen): the abelian group
    G = C2 x F2^4 x Z4,   |G| = 128,
group semiring N[G] inside the *-algebra C[G] (natural involution
g -> g^{-1} with complex conjugation; events are symmetrized through
sigma(g) = (rho(g) + rho(g^{-1}))/2 in the regular representation).
Because G is abelian, EVERY positivity question splits over the 128
characters chi = (eps, w, j):
    chi(s^a, v, m) = eps^a * (-1)^{w.v} * i^{j m},
and character evaluation on a commutative *-algebra is automatically a
*-character, hence completely positive AS A MAP.  The finite-level
CONTENT decided here is therefore: (i) is the packet-side object
(state / correspondence operator) inside the positive cone at every
finite depth, and (ii) does its positivity SURVIVE into every
character sector -- in particular into the GL1 sign sector, which is
verified below to be EXACTLY the deployed Weil window of the closed
diagonal-Gram route (read-only reuse; stop-list respected, nothing
re-gated).

THE TWO FACES OF THE REGISTER (frozen, declared honestly):
  *  STATE face (Schroedinger): per event n the C2 slot carries the
     PARITY POPULATIONS (A_n, B_n) = ((sigma3(n) + a_n)/2,
     (sigma3(n) - a_n)/2) from the theta decomposition (a_n = a_n(f8),
     f8 = eta(2t)^4 eta(4t)^4; independently recomputed here from the
     D5/A3 class thetas: Th0 - Th2 = -8 f8, Sum_j Th_j = 240 sigma3).
     chi_+ readout = the sigma3 channel; chi_- readout = the f8
     channel.  The mu4 slot carries the exact glue-class distribution
     (Th_j(n)/240 sigma3(n))_j; the V slot carries delta_0 for odd
     places (v742 V-scalarity), the uniform distribution on the 7
     nonzero classes of the chi_NSR polar hyperplane for ram-odd
     events, delta_0 for ram-even (v738/v752 label frame, machinery
     read-only).
  *  WINDOW face (Heisenberg / the correspondence operator): per atom
     event the C2 slot carries the sign CARRIER s (the deck-parity
     bit: this event is prime data, the continuum sits at e).  The
     packet window operator at rung M is
       W_pack(M) = T_cont(M) (x) 1 + Sum_n Q_n(M) (x) sigma(x_n),
     Q_n = MINUS the deployed single-atom lag Toeplitz (v563 tent
     assembly, masses 2 Lambda(n)/sqrt(n), read-only).  Character
     sectors: W_chi = T_cont + Sum_n Re chi(x_n) Q_n.  The sector
     chi = (-, 0, 0) is bit-identical to the deployed Weil window
     (gated); the sector (+, 0, 0) is the mirror envelope; the other
     126 sectors are the genuinely NEW measured objects (V-twist,
     spinor-balance j = 2, f8-twist j = 1).
     The population-register window operator (packet-faithful face) is
     measured alongside: there the C2/mu4 slots damp every atom by the
     normalized Hecke ratios, and positivity is expected MANIFEST
     (fat, depth-flat margins) -- the honest comparison of step 4.

THE DESCENT (frozen): D = (evaluate chi_- on C2) o (forget V) o
(forget mu4) -- i.e. the character (eps, w, j) = (-, 0, 0).  On the
window face it lands EXACTLY on the von-Mangoldt-weighted prime data
the deployed Weil functional consumes (gate D0 below: lag-vector
identity with the v755/v563 build, machine precision).  On the state
face it reads out the signed Hecke channel a_n realized as the
DIFFERENCE of positive populations A_n - B_n.

THE PACKET STATE (v2, ONE definition; the v1 linear candidate is kept
as a NAMED run-1 readout -- see CALIBRATION below): the KMS/half-weight
GNS mixture of event vector states,
    omega_N(a) = (1/Z) Sum_{events n <= N} w_n <x_n, a x_n> / ||x_n||^2,
    w_n = Lambda(n)/sqrt(n)   (the v756 half-weight / the deployed
                               atom mass over 2),
x_n in N[G] the population register element, the inner product in
l^2(G).  Its 128 character values are |x_n-hat(chi)|^2-weighted, hence
positivity is MANIFEST -- exactly the Section-19 claim, and the census
verifies it in exact rationals (Bochner/Herglotz on the finite abelian
group: the Gram of the generating family {delta_g} is the G-circulant
with the 128 Fourier values as eigenvalues).  Census: 12 distinct
sector classes at 7 nested depths (the rung reaches), float with a
forward error bound, plus a fully exact Fraction leg at depth n <= 300
with unit weights.

CALIBRATION (declared, run 1 -> run 2; v755 precedent, run-1 numbers
documented, nothing hidden):
  (a) STATE FACE.  The v1-frozen state was the LINEAR pushforward
      omega(g) = (1/Z) Sum w_n x_n(g).  Run 1 (2026-08-05) FALSIFIED
      it: nonnegative coefficients do not give a positive-definite
      function on G; the census failed at binding sector
      (eps = +1, v7, j = 2) with value -6.6e-2, depth-FLAT (exact leg
      -4.50 at unit weights) -- a structural, not numerical, failure.
      FINDING F1 (typed): even the pre-character linear aggregation of
      positive packet elements is NOT a state; positivity requires the
      squared/GNS form.  The v2 state above is the GNS-correct
      construction the strategy actually prescribes ("build the state,
      run GNS"); the linear candidate stays as a named readout.
  (b) OPERATOR-FACE EXPECTATION.  v1 expected all 24 sector windows
      PSD ("manifest positivity" at operator level).  Run 1 FALSIFIED
      the expectation: the GL1 sector (bit-identical to the deployed
      Weil window, Ward 6e-16) is PSD on the full ladder with EXACTLY
      the corpus PD margins (+5.3e-5 at X = 4 -> +1.2e-5 at X = 10),
      and it is the UNIQUE PSD sector: every damped/twisted sector
      breaks at O(1)-O(100) scale.  FINDING F2 (typed): under a
      register-TRIVIAL continuum, any character that damps or flips
      the atom leg exposes the pole--atom cancellation (the v755 S4 /
      v767 A3 balance anatomy); the breaking tensor factor is the
      CONTINUUM (e-slot) leg, not C2 / F2^4 / mu4.  The v2 gates type
      this honestly: the descent-target gate (GL1 sector PSD) is
      gated; the operator-face census is adjudicated as the
      PARTIAL-trigger with the breaking factor NAMED, plus an
      arch-only vs arch+pole localization diagnostic.  No sector
      construction was altered; no re-gating of closed-route objects.
  (c) C3 CONTROL CONSTANT.  v1 wrote sigma3(7) = 400 (a transcription
      error); the correct value is 344.  Fixed; the control logic is
      unchanged.

GATES (frozen before the run):
  P1  the packet layer is exact: class thetas nonneg with
      Sum_j Th_j = 240 sigma3 (ALL n <= N_THETA); Th1 = Th3;
      Th0 - Th2 = -8 f8 with f8 from the independent eta-product
      recurrence (cross-checked on n <= 2000) and odd support;
      a_p = (-4, -2, 24) at p = 3, 5, 7; populations (A_n, B_n)
      nonneg INTEGERS for all odd n; packet matrices
      M_n = [[A, B], [B, A]] multiplicative on ALL coprime odd pairs
      (m <= 45, mn <= N_THETA) and satisfying the p^3-corrected Hecke
      recursion M_{p^{k+1}} = M_p M_{p^k} - p^3 M_{p^{k-1}} on ALL
      reachable odd prime powers.
  P2  the packet GNS state is positive at every depth: exact leg (n <=
      300, Fractions, unit weights) all 128 values >= 0 EXACTLY;
      half-weight leg all 12 sector classes >= -1e-9 at all 7 depths
      (forward float error bound reported); the v1 LINEAR candidate is
      re-measured and its failure REPORTED (finding F1), not gated.
  P3  the descent is constructed and its target decided at finite
      level: D0 sector (-, 0, 0) lag == deployed c_full (rel <=
      1e-12); D1 sigma(x)-character diagonalization Ward (3 sampled
      events, dev <= 1e-10) + C2-reduced Kron Ward at M_TOP;
      D2 the DESCENDED (GL1) sector PSD at ALL 7 rungs (lambda_min >=
      -1e-10 * ||T||); battery Grams (v766 battery R = 1, read-only)
      PSD through the descent.
  P4  the operator-face census (the PARTIAL trigger): all 24 sector
      ladders (carrier + population registers) measured; if any sector
      other than GL1 breaks PSD, the verdict is DESCENT-PARTIAL with
      the breaking tensor factor NAMED, supported by the localization
      diagnostic (arch-only vs arch+pole continuum ladders).  The
      honest comparison (measurement): per-sector lambda_min ladders,
      log-slopes, state-census margins per depth (flat vs falling).
CONTROLS (must fire):
  C1  position scramble (rng seed 7, positions uniform in
      (0.5, 2 alpha), masses kept): the descended (Weil) sector must
      lose PSD.
  C2  Epstein x^2 + 5y^2 swap (epstein_firewall_probe read-only,
      Lambda_E has negative sites): the event stream leaves the
      positive cone (negative weights counted) AND the window sectors
      break.
  C3  wrong character (chi_+ where chi_- belongs): the readout is the
      sigma3 channel EXACTLY (240-normalized glue identity), NOT the
      f8 channel (a_p pattern absent), and the (+,0,0) window differs
      from the deployed window macroscopically.
  C4  random parities (LCG split of sigma3(n) into A' + B'):
      multiplicativity and the p^3 recursion must break.
  C5  scrambled glue labels ((0123) -> (1230) on the mu4 slot): the
      Th0 - Th2 = -8 f8 identity must break at p = 3, 5, 7.

VERDICT ENUM (frozen): DESCENT-CP-CARRIES (P1-P4 all pass, controls
fire -- the finite-level functor is CP into every sector including the
GL1 sign sector; the packet side is manifestly positive where the
signed side struggles) / DESCENT-PARTIAL (P1-P3 pass but the operator
face breaks: name the breaking sector / tensor factor / character) /
DESCENT-DEAD (the packet GNS state fails positivity, or the descended
GL1 sector breaks PSD at reachable depth, or a control is void).

RESULTS (2026-08-05, run 2 = the declared calibration run, 30/30
checks, all 5 controls fire, 4.2 s; verdict DESCENT-PARTIAL):
  *  P1 EXACT: heads (52, 64, 60, 64); Sum Th_j = 240 sigma3 on ALL
     n <= 22050; Th0 - Th2 = -8 f8 on ALL odd n (even-n remainder =
     typed Eisenstein object, head 1, 16, -144); f8 eta-recurrence
     primary, a_p = (-4, -2, 24); populations integral nonneg
     (A_3, B_3) = (12, 16); multiplicativity 13225/13225 pairs,
     p^3 recursion 53/53 steps.
  *  P2 STATE CARRIES: GNS census positive at all 7 depths (min
     sector value 2.0e-7 -> 8.3e-9, binding sector (eps=-1, v1, j=1)
     = the f8^2 sector -- dilution, not sign approach; trivial sector
     exactly 1; GNS rank 128/128 at X = 10); EXACT leg min = +4e-6
     >= 0 exactly (79 events, Fractions, Parseval ward exact).
     F1 (typed): the v1 LINEAR counting candidate FAILS at
     (+1, v7, j2) = -6.6e-2 (depth-flat failure; exact leg -4.50) --
     nonneg coefficients do not make a positive-definite function;
     only the squared/GNS aggregation is a state.  The naive
     sign-carrier count fails at -1 (the honesty point, quantified).
  *  P3 DESCENT CARRIES: D0 identity rel 6.0e-16 (the GL1 sector IS
     the deployed Weil window); character-diagonalization ward
     1.7e-16; Kron ward exact; GL1 sector PSD on all 7 rungs with
     margins +5.29e-5 (X=4) -> +1.18e-5 (X=10), log-slope -0.239 per
     X unit (the corpus PD margins / moving edge, reproduced
     read-only); descended battery Grams PSD.
  *  P4 OPERATOR FACE BREAKS (the named finding F2): 1 of 24 sector
     ladders PSD -- the GL1 sector is the UNIQUE positive sector.
     Mirror (+,0,0) = -282 at X = 10; f8-twisted and spinor-balance
     sectors -132..-151; the V-twisted GL1 neighbour (eps=-1, v7,
     j=0) = -1.85.  LOCALIZATION: lambda_min(arch only) = -3.6..-4.7
     (flat) vs lambda_min(arch+pole) = -5.0 -> -141 (falling): the
     negativity is carried by the POLE layer; only the exact deployed
     atom leg (the GL1 character) cancels it.  The breaking tensor
     factor is the CONTINUUM (e-slot) leg, not C2 / F2^4 / mu4.
  *  CONTROLS: C1 scramble lambda_min = -271; C2 Epstein 333 events
     leave the cone, window -84.4; C3 chi_+ reads sigma3 (28/126/344)
     not f8, window rel diff 1.79; C4 random parities break 5/5 + 3/3;
     C5 glue scramble breaks 3/3.
  *  CONSEQUENCE: the functorial-positivity route has finite-level
     substance on the STATE face and lands exactly on the deployed
     GL1 evaluation, but the operator face needs sector-adapted
     continua (twisted-channel explicit formulas) as the missing CP
     data -- contract PRIME.POSITIVE_DESCENT.01 text in the report.

FENCES: NO RH claim.  The stop-list of the closed diagonal-Gram route
stays binding: no fixed-d variants, no re-gating of v759-v773 objects,
windows/batteries reused READ-ONLY.  [C neu] semantics: everything
here is exploration-typed, no marker move, no ledger row.  Writes
nothing.  ONE new file.  AST firewall: no prime tables / zeta symbols
(own sieve only); machinery imports read-only from v563 / v716 / v738 /
v755 / v766 and epstein_firewall_probe.

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/positive_descent_probe.py
"""

import ast
import hashlib
import math
import os
import sys
import time
from fractions import Fraction as Fr

import numpy as np
import scipy.linalg as sla

_HERE = os.path.dirname(os.path.abspath(__file__))
_VERIFY = os.path.abspath(os.path.join(_HERE, "..", "..", "verification"))
sys.path.insert(0, _HERE)
sys.path.insert(0, _VERIFY)

import v563_paper2_readouts as core          # noqa: E402  (deployed atoms)
import v755_simpler_schur_recursion as srp   # noqa: E402  (tower channels)
import v766_handoff_bulk as hbp              # noqa: E402  (frozen battery)
import v738_hecke_mod_ramified as ram        # noqa: E402  (label frame)
import epstein_firewall_probe as epx         # noqa: E402  (control comb)

# ------------------------------------------------------------- frozen spec
FROZEN_SPEC = """\
PRIME.POSITIVE_DESCENT.01 finite-level spec v2 (2026-08-05; v1 frozen
before the first run, v2 = the declared run-1 -> run-2 calibration with
the v1 run-1 numbers documented in the module docstring: F1 the linear
counting candidate fails positivity at (+1, v7, j2) = -6.6e-2 and is
replaced by the GNS vector-state mixture; F2 the operator-face
all-sector-PSD expectation is falsified -- GL1 is the unique PSD sector
-- and is re-typed as the PARTIAL trigger with the breaking factor
named; C3 constant sigma3(7) corrected 400 -> 344).
Register G = C2 x F2^4 x Z4 (order 128); characters (eps, w, j).
Events: all deployed atoms with u <= 10 (n <= e^10, v563 table read-only);
  channels ro/re/sp/in from the zeta-free Gauss double sieve (v755).
State face: c2 populations ((sigma3 + a)/2, (sigma3 - a)/2)/sigma3 with
  a = a(f8) via the independent eta recurrence, linked to the class
  thetas by Th0 - Th2 = -8 f8 on odd n (N_THETA = 22050); mu4 slot =
  (Th_j / 240 sigma3)_j; V slot = delta_0 (odd, ram-even), uniform on
  H*(y_chi) (ram-odd, 7 classes, v738 frame lex-first sigma-invariant
  symplectic form).  Frozen state = half-weight GNS mixture of event
  vector states, w_n = Lambda(n)/sqrt(n); reported alternatives: unit
  weights (exact leg, depth n <= 300), the v1 linear candidate (named
  readout F1), the naive sign-carrier readout.
Window face: carrier register (c2 = delta_s); W_chi(M) = T_cont +
  Sum Re chi(x_n) Q_n on rungs M = 256, 320, 384, 448, 512, 576, 640
  (X = 4..10, DGRID = 1/64, alpha_top = 5); population-register sectors
  measured alongside; battery = v766 battery(R = 1) read-only;
  localization diagnostic: arch-only vs arch+pole continuum ladders.
Gates P1-P4, controls C1-C5, verdict enum DESCENT-CP-CARRIES /
DESCENT-PARTIAL / DESCENT-DEAD as in the module docstring.  PSD bars:
sectors lambda_min >= -1e-10 * ||T||_2; census float >= -1e-9; exact leg
>= 0 exactly; D0 ward <= 1e-12, D1 ward <= 1e-10.  LCG seed 20260805;
numpy rng seed 7 (scramble control only).  Runtime cap ~30 min.  NO RH
claim; stop-list of the closed Gram route binding; writes nothing.
"""

N_THETA = 22050
M_TOP = 640
DGRID = 1.0 / 64.0
ALPHA_TOP = 0.5 * M_TOP * DGRID          # = 5.0, reach n <= e^10
RUNGS = (256, 320, 384, 448, 512, 576, 640)
EXACT_DEPTH = 300
PSD_BAR = 1.0e-10                        # x ||T||_2 per sector/rung
CENSUS_BAR = -1.0e-9
WARD_BAR = 1.0e-12
EP_NCAP = 34000
SEED_NP = 7

BANNED_IDS = ("sympy", "isprime", "primerange", "nextprime", "prevprime",
              "primepi", "zetazero", "nzeros", "mpz_zeta")

CHECKS = []
P_FLAGS = {}
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


# =============================================== S1 theta / packet layer
def sparse_theta_terms(kind, cap):
    """(exponent, coefficient) list on the given grid cap."""
    out = []
    if kind in ("th3", "th4"):
        out.append((0, 1))
        n = 1
        while n * n <= cap:
            c = 2 if kind == "th3" else 2 * ((-1) ** n)
            out.append((n * n, c))
            n += 1
    else:                                   # th2-type: odd squares, coeff 2
        o = 1
        while o * o <= cap:
            out.append((o * o, 2))
            o += 2
    return out


def sparse_mul(dense, terms):
    """exact int64 product of a dense series with a sparse one."""
    out = np.zeros_like(dense)
    for e, c in terms:
        if e == 0:
            out += c * dense
        else:
            out[e:] += c * dense[:-e]
    return out


def s1_theta_layer():
    section("S1 -- independent packet layer: class thetas, f8, sigma3")
    t0 = time.time()
    # sigma3 (python ints via int64 sieve; max ~1.3e13 << 2^62)
    sig3 = np.zeros(N_THETA + 1, dtype=np.int64)
    for d in range(1, N_THETA + 1):
        sig3[d::d] += d ** 3
    # von Mangoldt via own smallest-factor sieve (channel/control use)
    spf = np.zeros(EP_NCAP + 1, dtype=np.int64)
    for p in range(2, EP_NCAP + 1):
        if spf[p] == 0:
            spf[p::p] = np.where(spf[p::p] == 0, p, spf[p::p])

    def is_ppow(n):
        p = int(spf[n])
        m = n
        while m % p == 0:
            m //= p
        return p if m == 1 else 0

    # class thetas on the s-grid (q^{1/2}): th3/th4 sparse at n^2
    SCAP = 2 * N_THETA
    t3 = sparse_theta_terms("th3", SCAP)
    t4 = sparse_theta_terms("th4", SCAP)
    one = np.zeros(SCAP + 1, dtype=np.int64)
    one[0] = 1
    p3 = [one]
    p4 = [one]
    for k in range(8):
        p3.append(sparse_mul(p3[-1], t3))
        p4.append(sparse_mul(p4[-1], t4))
    # exact: Th0 = (th3^8 + th3^5 th4^3 + th4^5 th3^3 + th4^8)/4
    m53 = p3[5].copy()
    for _ in range(3):
        m53 = sparse_mul(m53, t4)            # th3^5 * th4^3
    m35 = p4[5].copy()
    for _ in range(3):
        m35 = sparse_mul(m35, t3)            # th4^5 * th3^3
    num0 = p3[8] + m53 + m35 + p4[8]
    num2 = p3[8] - m53 - m35 + p4[8]
    ok_div = (np.all(num0 % 4 == 0) and np.all(num2 % 4 == 0))
    Th0 = (num0 // 4)[::2][:N_THETA + 1].copy()   # s = 2n -> q^n
    Th2 = (num2 // 4)[::2][:N_THETA + 1].copy()
    # Th1 = Th3 = th2^8 / 4 on the t-grid (q^{1/8}), t = 8n -> q^n
    TCAP = 8 * N_THETA
    t2 = sparse_theta_terms("th2", TCAP)
    acc = np.zeros(TCAP + 1, dtype=np.int64)
    acc[0] = 1
    for k in range(8):
        acc = sparse_mul(acc, t2)
    ok_div &= bool(np.all(acc[::8][:N_THETA + 1] % 4 == 0))
    Th1 = (acc[::8][:N_THETA + 1] // 4).copy()
    Th3 = Th1
    check("S1.1 theta builds exact (int64, divisibility by 4 exact); "
          "heads (Th0,Th1,Th2,Th3)(1) = (%d,%d,%d,%d) == (52,64,60,64)"
          % (Th0[1], Th1[1], Th2[1], Th3[1]),
          ok_div and (Th0[1], Th1[1], Th2[1], Th3[1]) == (52, 64, 60, 64),
          "%.1f s" % (time.time() - t0))
    tot = Th0 + Th1 + Th2 + Th3
    ok_tot = bool(np.all(tot[1:] == 240 * sig3[1:])) and tot[0] == 1
    ok_pos = bool(np.all(Th0 >= 0) and np.all(Th1 >= 0)
                  and np.all(Th2 >= 0))
    check("S1.2 glue identity Sum_j Th_j(n) = 240 sigma3(n) for ALL "
          "n = 1..%d (overflow ward included); Th_j >= 0 everywhere; "
          "Th1 == Th3" % N_THETA, ok_tot and ok_pos)

    # f8 PRIMARY build: eta-product recurrence (independent of thetas)
    # f8 = q prod (1-q^{2m})^4 (1-q^{4m})^4;  n g_n = -sum t_k g_{n-k}
    t0f = time.time()
    tk = np.zeros(N_THETA + 1, dtype=np.int64)
    for d in range(2, N_THETA + 1, 2):
        e_d = 4 + (4 if d % 4 == 0 else 0)
        tk[d::d] += d * e_d
    g = np.zeros(N_THETA, dtype=np.int64)
    g[0] = 1
    for n in range(1, N_THETA):
        s = int(np.dot(tk[1:n + 1], g[n - 1::-1]))
        q, r = divmod(-s, n)
        assert r == 0
        g[n] = q
    a_f8 = np.zeros(N_THETA + 1, dtype=np.int64)
    a_f8[1:] = g
    # python-int Ward on 20 LCG-sampled steps (int64 overflow guard)
    ok_ward = True
    for _ in range(20):
        n = 1 + lcg(N_THETA - 1)
        s = sum(int(tk[k]) * int(g[n - k]) for k in range(1, n + 1)
                if tk[k])
        ok_ward &= (-s == n * int(g[n]))
    ok_odd = bool(np.all(a_f8[2::2] == 0)) and a_f8[1] == 1
    ok_ap = (a_f8[3], a_f8[5], a_f8[7]) == (-4, -2, 24)
    ok_bound = bool(np.all(np.abs(a_f8[1::2]) <= sig3[1::2]))
    check("S1.3 f8 primary (eta recurrence, exact int64 + python-int "
          "Ward on 20 sampled steps): odd-supported, f8(1) = 1; a_p = "
          "(%d, %d, %d) == (-4, -2, 24); |a_n| <= sigma3(n) on odd n"
          % (a_f8[3], a_f8[5], a_f8[7]),
          ok_ward and ok_odd and ok_ap and ok_bound,
          "%.1f s" % (time.time() - t0f))

    # the C2/mu4 link: odd-support identity of the glue register
    diff = Th0 - Th2
    odd = np.arange(1, N_THETA + 1, 2)
    ok_link = bool(np.all(diff[odd] == -8 * a_f8[odd]))
    check("S1.4 C2/mu4 link: Th0(n) - Th2(n) = -8 f8(n) for ALL odd "
          "n <= %d (the sign channel of the glue register IS the f8 "
          "channel on the odd places); even-n remainder is a typed "
          "Eisenstein object (head n = 0, 2, 4: %d, %d, %d -- "
          "REPORTED, not the f8 channel)"
          % (N_THETA, diff[0], diff[2], diff[4]), ok_link)

    return dict(sig3=sig3, Th=(Th0, Th1, Th2, Th3), a=a_f8, spf=spf,
                is_ppow=is_ppow)


def s2_packet(th):
    section("S2 -- the C2 packet: populations, composition, p^3 recursion")
    sig3, a = th["sig3"], th["a"]
    odd = np.arange(1, N_THETA + 1, 2)
    ok_int = bool(np.all((sig3[odd] + a[odd]) % 2 == 0))
    ok_pos = bool(np.all(np.abs(a[odd]) <= sig3[odd]))
    A = (sig3 + a) // 2
    B = (sig3 - a) // 2
    check("S2.1 populations A_n = (sigma3 + a)/2, B_n = (sigma3 - a)/2 "
          "are nonneg INTEGERS for ALL odd n <= %d (E_odd = A + B, "
          "f8 = A - B realized)" % N_THETA, ok_int and ok_pos,
          "A(3),B(3) = %d,%d; A(9),B(9) = %d,%d"
          % (A[3], B[3], A[9], B[9]))
    # even layer: a = 0 exactly -> symmetric populations
    ok_ram = bool(np.all(a[2::2] == 0))
    check("S2.2 ramified layer C2-symmetric: a(2^k) = 0 (all even n), "
          "packet (e + s)/2 after normalization (integrality not "
          "claimed on the ram layer, typed)", ok_ram)

    # multiplicativity of M_n = [[A,B],[B,A]] on coprime odd pairs
    viol = 0
    npairs = 0
    for m in range(3, 46, 2):
        for n in range(3, N_THETA // m + 1, 2):
            if math.gcd(m, n) != 1:
                continue
            npairs += 1
            Am, Bm = int(A[m]), int(B[m])
            An, Bn = int(A[n]), int(B[n])
            if (Am * An + Bm * Bn != int(A[m * n])
                    or Am * Bn + Bm * An != int(B[m * n])):
                viol += 1
    check("S2.3 packet matrices multiplicative: M_m M_n = M_{mn} on ALL "
          "%d coprime odd pairs (m <= 45, mn <= %d); violations = %d"
          % (npairs, N_THETA, viol), viol == 0)

    # p^3-corrected Hecke recursion on all reachable odd prime powers
    viol_r = 0
    ntrip = 0
    p = 3
    while p * p <= N_THETA:
        if th["is_ppow"](p) == p and p % 2 == 1 and int(th["spf"][p]) == p:
            pk = p
            k = 1
            while pk * p <= N_THETA:
                nxt, cur, prv = pk * p, pk, pk // p
                ntrip += 1
                Ap, Bp = int(A[p]), int(B[p])
                Ak, Bk = int(A[cur]), int(B[cur])
                Aprev, Bprev = int(A[prv]), int(B[prv])
                c = p ** 3
                if (Ap * Ak + Bp * Bk - c * Aprev != int(A[nxt])
                        or Ap * Bk + Bp * Ak - c * Bprev != int(B[nxt])):
                    viol_r += 1
                pk *= p
                k += 1
        p += 2
    check("S2.4 p^3-corrected recursion M_{p^{k+1}} = M_p M_{p^k} - "
          "p^3 M_{p^{k-1}} EXACT on all %d reachable odd prime-power "
          "steps; violations = %d" % (ntrip, viol_r), viol_r == 0)
    return dict(A=A, B=B)


# =============================================== S3 label frame (V slot)
def s3_label_frame():
    section("S3 -- the V-label frame (v738 read-only): y_chi + hyperplane")
    L = ram.Lmodule()
    E = [tuple((1 if j == k else 0, 0) for j in range(4)) for k in range(4)]
    S = [L.coords(ram.pack(ram.sig8(ram.unpack(L.to_ambient(E[k])))))
         for k in range(4)]
    S2 = [[ram.par(S[k][j]) for j in range(4)] for k in range(4)]

    def sigbar(v):
        return tuple((sum(v[k] * S2[k][j] for k in range(4))) & 1
                     for j in range(4))

    labels = [tuple((z >> b) & 1 for b in range(4)) for z in range(16)]
    # lex-first sigma-invariant nondegenerate alternating form (v756)
    from itertools import combinations
    pairs = list(combinations(range(4), 2))
    Omega = None
    n_inv = 0
    for mask in range(1, 1 << 6):
        M = [[0] * 4 for _ in range(4)]
        for bi, (i, j) in enumerate(pairs):
            if (mask >> bi) & 1:
                M[i][j] = M[j][i] = 1
        cols = [tuple(M[i][j] for i in range(4)) for j in range(4)]
        rk, _k, _i = ram.f2_rank_ker_inv(cols)
        if rk != 4:
            continue
        inv_ok = all(
            (sum(sigbar(v)[k] * M[k][l] * sigbar(w)[l]
                 for k in range(4) for l in range(4))) & 1
            == (sum(v[k] * M[k][l] * w[l]
                    for k in range(4) for l in range(4))) & 1
            for v in labels for w in labels)
        if inv_ok:
            n_inv += 1
            if Omega is None:
                Omega = M
    cols_o = [tuple(Omega[i][j] for i in range(4)) for j in range(4)]
    _rk, _ker, inv_o = ram.f2_rank_ker_inv(cols_o)
    a_par = tuple(ram.unpack(L.to_ambient(E[k]))[0] % 2 for k in range(4))
    y_chi = ram.f2_matvec(inv_o, a_par)
    Hstar = [v for v in labels if any(v)
             and (sum(v[k] * Omega[k][l] * y_chi[l]
                      for k in range(4) for l in range(4))) & 1 == 0]
    n_ns = sum(1 for v in labels if any(v)
               and (sum(x * y for x, y in zip(a_par, v))) & 1 == 0)
    ok = (Omega is not None and any(y_chi)
          and sigbar(y_chi) == y_chi and len(Hstar) == 7
          and y_chi in Hstar and n_ns == 7)
    check("S3.1 frame: lex-first sigma-invariant symplectic form "
          "(%d invariant choices); y_chi = %s sigma-fixed; polar "
          "hyperplane H* has 7 nonzero classes containing y_chi; "
          "chi_NSR census 7 NS + 8 R" % (n_inv, (y_chi,)), ok)

    # vhat values for the ram-odd uniform distribution on H*
    vhat = {}
    for w in labels:
        s = sum(1 if (sum(w[k] * v[k] for k in range(4))) & 1 == 0 else -1
                for v in Hstar)
        vhat[w] = Fr(s, 7)
    vals = sorted(set(vhat.values()))
    n_one = sum(1 for w in labels if vhat[w] == 1)
    check("S3.2 V-slot Fourier values on the uniform H* distribution: "
          "exactly {%s}; %d characters see +1 (the annihilator of H), "
          "14 see -1/7" % (", ".join(str(v) for v in vals), n_one),
          vals == [Fr(-1, 7), Fr(1, 1)] and n_one == 2)
    return dict(vhat=vhat, y_chi=y_chi, Hstar=Hstar, labels=labels)


# =============================================== S4 events + state census
def s4_events(th, frame):
    section("S4 -- the event stream + the packet state positivity census")
    t0 = time.time()
    ka, masks, dev = srp.channel_masks(ALPHA_TOP)
    check("S4.1 tower comb consistency (zeta-free Gauss double sieve == "
          "deployed masses)", dev <= 1.0e-12,
          "rel dev %.1e, ka = %d atoms to e^%.0f" % (dev, ka,
                                                     2 * ALPHA_TOP))
    chan = np.empty(ka, dtype="U2")
    for c, idx in masks.items():
        chan[idx] = c
    nvals = np.array([int(round(math.exp(float(core.U_ALL[i]))))
                      for i in range(ka)], dtype=np.int64)
    ok_reach = bool(np.all(nvals <= N_THETA))
    check("S4.2 every event n <= N_THETA = %d (theta data covers the "
          "reach); channel census ro/re/sp/in = %d/%d/%d/%d"
          % (N_THETA, len(masks["ro"]), len(masks["re"]),
             len(masks["sp"]), len(masks["in"])), ok_reach)

    sig3, a = th["sig3"], th["a"]
    Th0, Th1, Th2, Th3 = th["Th"]

    # per-event exact slot data
    ev = []
    for i in range(ka):
        n = int(nvals[i])
        E = 240 * int(sig3[n])
        c2m = Fr(int(a[n]), int(sig3[n]))          # chi_- population readout
        mh1 = Fr(int(Th0[n]) - int(Th2[n]), E)     # Re mhat(1) = -8 f8 / E
        mh2 = Fr(int(Th0[n]) - int(Th1[n]) + int(Th2[n]) - int(Th3[n]), E)
        is_ro = (chan[i] == "ro")
        ev.append(dict(i=i, n=n, ch=str(chan[i]), is_ro=is_ro,
                       w=float(core.MU_ALL[i]) / 2.0,
                       c2m=c2m, mh=(Fr(1), mh1, mh2)))
    # 12 sector classes: eps x {v1, v7} x {j0, j1, j2}
    sectors = [(eps, vc, jc) for eps in (+1, -1)
               for vc in ("v1", "v7") for jc in (0, 1, 2)]
    mult = {}
    for eps, vc, jc in sectors:
        mult[(eps, vc, jc)] = (2 if vc == "v1" else 14) * \
            (2 if jc == 1 else 1)
    ok_mult = sum(mult.values()) == 128
    check("S4.3 sector classes: 12 distinct (eps, V-class, mu4-class) "
          "covering all 128 characters (multiplicities sum = %d)"
          % sum(mult.values()), ok_mult)

    # per-event sector class values t = c2hat * vhat * mhat (exact)
    def class_values(e, eps, vc, jc, exact=False):
        if eps == +1:
            c2f = Fr(1) if exact else 1.0
        else:
            c2f = e["c2m"] if exact else float(e["c2m"])
        if e["is_ro"] and vc == "v7":
            vf = Fr(-1, 7) if exact else -1.0 / 7.0
        else:
            vf = Fr(1) if exact else 1.0
        mf = e["mh"][jc] if exact else float(e["mh"][jc])
        return c2f * vf * mf

    # GNS vector-state census (v2 frozen state): value per sector =
    # (1/Z) sum_n w_n |xhat_n(chi)|^2 / nu_n, nu_n = (1/128) sum mult t^2
    W = [e["w"] for e in ev]
    depths = [(X, sum(1 for e in ev if e["n"] <= math.exp(X) + 1e-9))
              for X in range(4, 11)]
    tvals = np.array([[class_values(e, *sec) for sec in sectors]
                      for e in ev])                       # (ka, 12)
    mvec = np.array([mult[sec] for sec in sectors], float)
    nu = (tvals ** 2 @ mvec) / 128.0
    ok_nu = bool(np.all(nu > 0))
    check("S4.4a GNS normalizers nu_n > 0 for every event (the packet "
          "element never vanishes in l^2(G))", ok_nu,
          "min nu = %.3e" % float(np.min(nu)))
    gns = (tvals ** 2) / nu[:, None]                      # (ka, 12)
    Wv = np.array(W)
    print("    GNS packet-state census (value, all 12 sectors, "
          "half-weight):")
    census_rows = []
    min_all = np.inf
    worst = None
    for X, cnt in depths:
        z = float(Wv[:cnt].sum())
        row_v = (Wv[:cnt] @ gns[:cnt]) / z
        row = {sec: float(row_v[k]) for k, sec in enumerate(sectors)}
        census_rows.append((X, cnt, row))
        mn = min(row.values())
        amn = min(row, key=row.get)
        if mn < min_all:
            min_all, worst = mn, (X, amn)
        norm_ward = float(abs(row_v @ mvec / 128.0 - 1.0))
        print("      X = %2d (%4d events): min = %+.6e at (eps=%+d, "
              "%s, j=%d); GL1-adjacent (-1,v1,j0) = %.4e; unit ward "
              "%.1e" % (X, cnt, mn, amn[0], amn[1], amn[2],
                        row[(-1, "v1", 0)], norm_ward))
    ok_census = min_all >= CENSUS_BAR
    check("S4.4 packet GNS state positive at ALL depths (manifest, "
          "verified): min sector value = %+.3e >= %.0e; binding "
          "sector %s" % (min_all, CENSUS_BAR, worst), ok_census)

    # exact-rational leg: unit weights, depth n <= 300, Fractions
    subx = [e for e in ev if e["n"] <= EXACT_DEPTH]
    exact_min = None
    exact_worst = None
    ward_exact = Fr(0)
    for e in subx:
        tx = {sec: class_values(e, *sec, exact=True) for sec in sectors}
        nux = sum(Fr(mult[sec]) * tx[sec] ** 2
                  for sec in sectors) / 128
        assert nux > 0
        e["_gns_exact"] = {sec: tx[sec] ** 2 / nux for sec in sectors}
    for sec in sectors:
        tot = sum(e["_gns_exact"][sec] for e in subx)
        ward_exact += Fr(mult[sec]) * tot
        if exact_min is None or tot < exact_min:
            exact_min, exact_worst = tot, sec
    ok_exact = (exact_min >= 0
                and ward_exact == 128 * len(subx))
    check("S4.5 EXACT leg (Fractions, unit weights, %d events n <= "
          "%d): min sector value = %.6f >= 0 EXACTLY (binding sector "
          "%s); Parseval ward exact" % (len(subx), EXACT_DEPTH,
                                        float(exact_min), exact_worst),
          ok_exact)
    # GNS rank at top depth
    top_row = census_rows[-1][2]
    gns_rank = sum(mult[k] for k, v in top_row.items() if v > 1e-15)
    print("    GNS data at X = 10: rank of the 128 x 128 state Gram = %d "
          "of 128 (positive Fourier sectors, counted with multiplicity)"
          % gns_rank)

    # NAMED READOUTS (not gated): the v1 linear candidate (finding F1)
    # and the naive sign-carrier count
    lin = {}
    z = float(Wv.sum())
    for k, sec in enumerate(sectors):
        lin[sec] = float(Wv @ tvals[:, k]) / z
    mn_lin = min(lin.values())
    amn_lin = min(lin, key=lin.get)
    print("    F1 NAMED READOUT: the v1 LINEAR counting candidate has "
          "min sector value %+.4e at (eps=%+d, %s, j=%d) < 0 at X = 10 "
          "-- the linear pushforward of positive elements is NOT a "
          "state; the GNS (squared) form is (run-1 finding, typed)"
          % (mn_lin, amn_lin[0], amn_lin[1], amn_lin[2]))
    mn_car = -1.0     # chi_-(s) = -1: the raw signed count, exact
    print("    NAMED READOUT: naive sign-carrier counting state has "
          "min sector value %+.1f (the raw signed count is NOT a "
          "state; the population lift is -- the honesty point)"
          % mn_car)
    ok_named = mn_lin < 0
    check("S4.6 sign-vs-population separation at state level: the GNS "
          "population state passes; the linear and sign-carrier "
          "candidates fail (observer projection quantified)",
          ok_named and ok_census)

    return dict(ev=ev, ka=ka, masks=masks, depths=depths,
                census_rows=census_rows, sectors=sectors, mult=mult,
                mn_car=mn_car, mn_lin=mn_lin)


# =============================================== S5 windows + descent
def build_atom_rows(ev, positions=None, masses=None):
    """per-event deployed lag rows (v563 tent assembly, read-only)."""
    ka = len(ev)
    C = np.zeros((ka, M_TOP))
    for k, e in enumerate(ev):
        u = (positions[k] if positions is not None
             else float(core.U_ALL[e["i"]]))
        mu = (masses[k] if masses is not None
              else float(core.MU_ALL[e["i"]]))
        C[k] = core.atom_lags_at(ALPHA_TOP, M_TOP, [u], [mu])[0]
    return C


def sector_coeffs(ev, frame, sectors, register):
    """s_chi(n): multiplier on the DEPLOYED atom lag row per sector.
    Convention: W_chi = T_cont + sum Re chi(x_n) Q_n with Q_n = minus
    the deployed row; hence s_chi(n) = -Re chi(x_n)."""
    out = {}
    for eps, vc, jc in sectors:
        s = np.empty(len(ev))
        for k, e in enumerate(ev):
            if eps == +1:
                c2f = 1.0
            elif register == "carrier":
                c2f = -1.0                    # chi_-(s), the sign carrier
            else:
                c2f = float(e["c2m"])         # population readout a/sigma3
            vf = 1.0 if (not e["is_ro"] or vc == "v1") else -1.0 / 7.0
            mf = float(e["mh"][jc])
            s[k] = -(c2f * vf * mf)
        out[(eps, vc, jc)] = s
    return out


def s5_descent(th, frame, ss4):
    section("S5 -- the descent: sector windows on the frozen rung ladder")
    ev = ss4["ev"]
    sectors = ss4["sectors"]
    t0 = time.time()
    c_cont = srp.continuum_lags(M_TOP)
    C_at = build_atom_rows(ev)
    # deployed reference build (v755 verbatim)
    c_full = c_cont.copy()
    for cnl in ("ro", "re", "sp", "in"):
        c_full = c_full + srp.atom_channel_lags(ALPHA_TOP, M_TOP,
                                                ss4["masks"][cnl])
    ward0 = float(np.max(np.abs((c_cont + C_at.sum(axis=0)) - c_full))
                  / np.max(np.abs(c_full)))
    check("S5.1 per-event row assembly == deployed channel build "
          "(rel %.1e <= %.0e)" % (ward0, WARD_BAR), ward0 <= WARD_BAR,
          "%d rows, %.1f s" % (len(ev), time.time() - t0))

    co_car = sector_coeffs(ev, frame, sectors, "carrier")
    co_pop = sector_coeffs(ev, frame, sectors, "population")
    # D0: the GL1 descent sector is EXACTLY the deployed Weil window
    lag_gl1 = c_cont + co_car[(-1, "v1", 0)] @ C_at
    wardD0 = float(np.max(np.abs(lag_gl1 - c_full))
                   / np.max(np.abs(c_full)))
    check("S5.2 D0 DESCENT IDENTITY: carrier sector (eps=-1, v1, j=0) "
          "lag vector == deployed Weil window c_full (rel %.1e)"
          % wardD0, wardD0 <= WARD_BAR)

    # D1a: character diagonalization ward on sigma(x_n), 3 LCG events
    G = [(aa, vv, mm) for aa in range(2) for vv in range(16)
         for mm in range(4)]
    gidx = {g: i for i, g in enumerate(G)}
    chars = [(eps, w, j) for eps in range(2) for w in range(16)
             for j in range(4)]

    def chival(chi, g):
        eps, w, j = chi
        aa, vv, mm = g
        pc = bin(w & vv).count("1")
        return ((-1) ** (eps * aa)) * ((-1) ** pc) * (1j ** (j * mm))

    U = np.array([[chival(chi, g) for chi in chars] for g in G],
                 dtype=complex) / math.sqrt(128.0)
    labels16 = frame["labels"]
    lab_idx = {v: i for i, v in enumerate(labels16)}
    hidx = [lab_idx[v] for v in frame["Hstar"]]
    dev1 = 0.0
    for _ in range(3):
        e = ev[lcg(len(ev))]
        sig = np.zeros((128, 128))
        # reconstruct the full mu4 distribution
        n = e["n"]
        Th0, Th1, Th2, Th3 = th["Th"]
        E = 240.0 * float(th["sig3"][n])
        pmm = [float(Th0[n]) / E, float(Th1[n]) / E,
               float(Th2[n]) / E, float(Th3[n]) / E]
        vlist = (hidx if e["is_ro"] else [0])
        pv = 1.0 / len(vlist)
        for vv in vlist:
            for mm in range(4):
                ccoef = pv * pmm[mm]
                g = (1, vv, mm)
                ginv = (1, vv, (-mm) % 4)
                for gg, cc in ((g, ccoef / 2.0), (ginv, ccoef / 2.0)):
                    # sigma(x) acting by left translation
                    for hsrc, hg in enumerate(G):
                        tg = ((hg[0] + gg[0]) % 2, hg[1] ^ gg[1],
                              (hg[2] + gg[2]) % 4)
                        sig[gidx[tg], hsrc] += cc
        Dm = U.conj().T @ sig @ U
        off = float(np.max(np.abs(Dm - np.diag(np.diag(Dm)))))
        # expected diagonal: Re chi(x)
        exp_d = []
        for chi in chars:
            eps, w, j = chi
            vfv = np.mean([1.0 if (sum(((w >> b) & 1) * labels16[vv][b]
                                       for b in range(4)) % 2 == 0)
                           else -1.0 for vv in vlist])
            mfv = float(np.real(sum(pmm[mm] * (1j ** (j * mm))
                                    for mm in range(4))))
            exp_d.append(((-1) ** eps) * vfv * mfv)
        dev1 = max(dev1, off,
                   float(np.max(np.abs(np.real(np.diag(Dm))
                                       - np.array(exp_d)))))
    check("S5.3 D1 sigma(x)-character diagonalization Ward (3 sampled "
          "events): max off-diagonal / diagonal deviation %.1e <= 1e-10"
          % dev1, dev1 <= 1.0e-10)

    # D1b: C2-reduced Kron ward at M_TOP
    rowsum = C_at.sum(axis=0)
    Tc = sla.toeplitz(c_cont[:M_TOP])
    Ta = sla.toeplitz(rowsum[:M_TOP])
    K = np.block([[Tc, Ta], [Ta, Tc]])
    lam_k = float(sla.eigvalsh(K, subset_by_index=[0, 0])[0])
    lam_dep = float(sla.eigvalsh(Tc + Ta, subset_by_index=[0, 0])[0])
    lam_mir = float(sla.eigvalsh(Tc - Ta, subset_by_index=[0, 0])[0])
    ok_kron = abs(lam_k - min(lam_dep, lam_mir)) <= 1.0e-8 * max(
        1.0, abs(lam_k))
    check("S5.4 D1 C2-reduced Kron Ward at M = %d: lambda_min(kron) = "
          "%+.6e == min(deployed %+.6e, mirror %+.6e)"
          % (M_TOP, lam_k, lam_dep, lam_mir), ok_kron)

    # sector ladders
    def ladder(coeffs):
        lag = c_cont + coeffs @ C_at
        out = []
        for M in RUNGS:
            T = sla.toeplitz(lag[:M])
            lam = float(sla.eigvalsh(T, subset_by_index=[0, 0])[0])
            nrm = float(sla.norm(T, 2))
            out.append((M, lam, nrm))
        return out

    print("    carrier-register sectors (the descent side; measurement):")
    lads_car = {}
    psd_car = {}
    for sec in sectors:
        lads_car[sec] = ladder(co_car[sec])
        psd_car[sec] = all(lam >= -PSD_BAR * nrm
                           for _M, lam, nrm in lads_car[sec])
        print("      (eps=%+d, %s, j=%d): lambda_min = %s  [%s]"
              % (sec[0], sec[1], sec[2],
                 " / ".join("%+.2e" % l for _m, l, _n in lads_car[sec]),
                 "PSD" if psd_car[sec] else "NEG"))
    gl1_ok = psd_car[(-1, "v1", 0)]
    check("S5.5 D2 the DESCENDED (GL1) sector PSD on ALL %d rungs "
          "(lambda_min >= -%.0e ||T||): margins %+.3e (X=4) -> %+.3e "
          "(X=10) -- the deployed Weil PD margins, reproduced through "
          "the descent" % (len(RUNGS), PSD_BAR,
                           lads_car[(-1, "v1", 0)][0][1],
                           lads_car[(-1, "v1", 0)][-1][1]), gl1_ok)

    print("    population-register sectors (the packet-faithful side; "
          "measurement):")
    lads_pop = {}
    psd_pop = {}
    for sec in sectors:
        lads_pop[sec] = ladder(co_pop[sec])
        psd_pop[sec] = all(lam >= -PSD_BAR * nrm
                           for _M, lam, nrm in lads_pop[sec])
        print("      (eps=%+d, %s, j=%d): lambda_min = %s  [%s]"
              % (sec[0], sec[1], sec[2],
                 " / ".join("%+.2e" % l for _m, l, _n in lads_pop[sec]),
                 "PSD" if psd_pop[sec] else "NEG"))
    ok_car = all(psd_car.values())
    ok_pop = all(psd_pop.values())
    n_psd = sum(psd_car.values()) + sum(psd_pop.values())
    print("    OPERATOR-FACE CENSUS (P4): %d of 24 sector ladders PSD"
          % n_psd)

    # localization diagnostic: WHICH leg breaks the damped sectors?
    arch = core.arch_lags(M_TOP, DGRID)
    lam_arch = []
    lam_cont = []
    for M in RUNGS:
        lam_arch.append(float(sla.eigvalsh(sla.toeplitz(arch[:M]),
                                           subset_by_index=[0, 0])[0]))
        lam_cont.append(float(sla.eigvalsh(sla.toeplitz(c_cont[:M]),
                                           subset_by_index=[0, 0])[0]))
    print("    LOCALIZATION (named): lambda_min(arch only)   = %s"
          % " / ".join("%+.2e" % v for v in lam_arch))
    print("                          lambda_min(arch + pole) = %s"
          % " / ".join("%+.2e" % v for v in lam_cont))
    culprit = ("the POLE layer (arch alone stays near-PSD)"
               if lam_arch[-1] > 10.0 * lam_cont[-1]
               else "the arch+pole continuum jointly")
    print("      -> the register-trivial continuum is exposed by any "
          "atom damping; the negativity is carried by %s.  ONLY the "
          "exact deployed atom leg (coefficient +1 on every event = "
          "the GL1 character) restores PSD: the breaking tensor "
          "factor of every damped sector is the CONTINUUM (e-slot) "
          "leg -- the pole--atom cancellation (v755 S4 / v767 A3 "
          "anatomy) -- not C2 / F2^4 / mu4." % culprit)

    # battery grams through the descent (v766 battery R = 1, read-only)
    bat = hbp.battery(1.0)
    Fm = np.stack([v for _n, v in bat], axis=1)
    nR = Fm.shape[0]
    lag_gl1 = c_cont + co_car[(-1, "v1", 0)] @ C_at
    gmins = []
    for M in RUNGS:
        F = np.zeros((M, Fm.shape[1]))
        F[:nR] = Fm
        T = sla.toeplitz(lag_gl1[:M])
        Gm = F.T @ T @ F
        gmins.append(float(np.linalg.eigvalsh(0.5 * (Gm + Gm.T))[0]))
    ok_bat = all(g >= -1.0e-12 for g in gmins)
    check("S5.7 descended battery Grams (v766 battery R = 1) PSD on all "
          "rungs: min eig = %s" % " / ".join("%.2e" % g for g in gmins),
          ok_bat)

    return dict(c_cont=c_cont, C_at=C_at, c_full=c_full,
                co_car=co_car, co_pop=co_pop, lads_car=lads_car,
                lads_pop=lads_pop, ok_car=ok_car, ok_pop=ok_pop,
                gl1_ok=gl1_ok, psd_car=psd_car, psd_pop=psd_pop,
                lam_arch=lam_arch, lam_cont=lam_cont)


# =============================================== S6 honest comparison
def s6_comparison(ss4, ss5):
    section("S6 -- honest comparison: packet-side vs descended margins "
            "along the ladder (the moving-edge question)")
    Xs = [M * DGRID for M in RUNGS]
    gl1 = [l for _m, l, _n in ss5["lads_car"][(-1, "v1", 0)]]
    mir = [l for _m, l, _n in ss5["lads_car"][(+1, "v1", 0)]]
    pop_min = [min(ss5["lads_pop"][sec][k][1]
                   for sec in ss4["sectors"]) for k in range(len(RUNGS))]
    car_min = [min(ss5["lads_car"][sec][k][1]
                   for sec in ss4["sectors"]) for k in range(len(RUNGS))]
    car_arg = [min(ss4["sectors"],
                   key=lambda s: ss5["lads_car"][s][k][1])
               for k in range(len(RUNGS))]

    def slope(vals):
        if any(v <= 0 for v in vals):
            return None
        y = np.log(np.array(vals))
        A = np.vstack([np.ones(len(Xs)), np.array(Xs)]).T
        cf, *_ = np.linalg.lstsq(A, y, rcond=None)
        return float(cf[1])

    print("    rung ladder (X = M/64):")
    print("      X    | GL1 descended  | mirror (+)     | worst carrier"
          " sector                 | packet(pop) worst")
    for k, X in enumerate(Xs):
        print("      %4.1f | %+.6e | %+.6e | %+.6e (eps=%+d,%s,j=%d) | "
              "%+.6e"
              % (X, gl1[k], mir[k], car_min[k], car_arg[k][0],
                 car_arg[k][1], car_arg[k][2], pop_min[k]))
    s_gl1 = slope(gl1)
    state_min = [min(r.values()) for _X, _c, r in ss4["census_rows"]]
    s_state = slope(state_min)
    print("    the three margin ladders, compared honestly:")
    print("      DESCENDED (GL1 window)  : falls %+.6e -> %+.6e "
          "(factor %.1f, log-slope %.3f per X unit) -- the closed "
          "route's moving edge, REPRODUCED read-only, not re-gated"
          % (gl1[0], gl1[-1], gl1[0] / gl1[-1], s_gl1))
    print("      PACKET STATE (GNS)      : min sector %+.6e -> %+.6e "
          "(factor %.2f, log-slope %s) -- positive at EVERY depth BY "
          "CONSTRUCTION (each event contributes a square): the fall "
          "is weight DILUTION of the f8^2 sector, structurally unable "
          "to cross zero; the trivial sector stays exactly 1"
          % (state_min[0], state_min[-1],
             state_min[0] / state_min[-1],
             "%.3f" % s_state if s_state is not None else "n/a"))
    print("      PACKET OPERATOR (naive) : worst sector %+.3e -> "
          "%+.3e -- NOT positive in any non-GL1 sector at ANY depth "
          "(no depth-driven rise: it is dead on arrival, the "
          "register-trivial continuum cannot follow the damped atom "
          "legs)" % (pop_min[0], pop_min[-1]))
    ok = (s_gl1 is not None) and math.isfinite(s_gl1)
    check("S6.1 comparison well-formed (GL1 ladder positive with "
          "finite slope; measurement, not a gate on signs)", ok)
    return dict(s_gl1=s_gl1, s_state=s_state, gl1=gl1,
                pop_min=pop_min, car_min=car_min, state_min=state_min)


# =============================================== S7 controls
def s7_controls(th, frame, ss4, ss5):
    section("S7 -- must-fail controls")
    ev = ss4["ev"]
    c_cont = ss5["c_cont"]
    sectors = ss4["sectors"]

    # C1 position scramble
    rng = np.random.default_rng(SEED_NP)
    pos = np.sort(rng.uniform(0.5, 2.0 * ALPHA_TOP, len(ev)))
    mas = [float(core.MU_ALL[e["i"]]) for e in ev]
    C_s = build_atom_rows(ev, positions=pos, masses=mas)
    lag = c_cont + ss5["co_car"][(-1, "v1", 0)] @ C_s
    lam = float(sla.eigvalsh(sla.toeplitz(lag[:M_TOP]),
                             subset_by_index=[0, 0])[0])
    fired = lam < 0.0
    CONTROL_FIRED["C1"] = fired
    check("C1 position scramble: descended (GL1) sector loses PSD at "
          "top rung (lambda_min = %+.3e < 0)" % lam, fired)

    # C2 Epstein swap
    r1 = epx.lattice_r1(EP_NCAP)
    b = np.asarray(r1, float) / 2.0
    lamE = epx.dirichlet_vonmangoldt(b, EP_NCAP)
    supp = np.nonzero(np.abs(lamE) > 1.0e-9)[0]
    supp = supp[(supp >= 2) & (supp <= N_THETA)]
    n_neg = int(np.sum(lamE[supp] < -1.0e-9))
    posE = np.log(supp.astype(float))
    keep = posE <= 2.0 * ALPHA_TOP
    posE = posE[keep]
    suppE = supp[keep]
    masE = 2.0 * lamE[suppE] / np.sqrt(suppE.astype(float))
    # cone breach: negative event weights
    n_out = int(np.sum(masE < 0))
    # window breach on the deployed sector (all coefficients +1)
    CE = np.zeros((len(suppE), M_TOP))
    for k in range(len(suppE)):
        CE[k] = core.atom_lags_at(ALPHA_TOP, M_TOP, [float(posE[k])],
                                  [float(masE[k])])[0]
    lagE = c_cont + CE.sum(axis=0)
    lamE_min = float(sla.eigvalsh(sla.toeplitz(lagE[:M_TOP]),
                                  subset_by_index=[0, 0])[0])
    fired = (n_out > 0) and (lamE_min < 0.0)
    CONTROL_FIRED["C2"] = fired
    check("C2 Epstein x^2+5y^2 swap: %d events leave the positive cone "
          "(negative masses; %d negative Lambda_E sites <= %d) AND the "
          "descended window breaks (lambda_min = %+.3e < 0)"
          % (n_out, n_neg, EP_NCAP, lamE_min), fired)

    # C3 wrong character: chi_+ where chi_- belongs
    sig3, a = th["sig3"], th["a"]
    okp = all(int((sig3[n] + a[n]) // 2 + (sig3[n] - a[n]) // 2)
              == int(sig3[n]) for n in range(3, 200, 2))
    ap_plus = [int(sig3[p]) for p in (3, 5, 7)]
    ap_minus = [int(a[p]) for p in (3, 5, 7)]
    sigma_channel = (ap_plus == [28, 126, 344]
                     and ap_minus == [-4, -2, 24])
    lag_plus = c_cont + ss5["co_car"][(+1, "v1", 0)] @ ss5["C_at"]
    dmax = float(np.max(np.abs(lag_plus - ss5["c_full"]))
                 / np.max(np.abs(ss5["c_full"])))
    fired = okp and sigma_channel and dmax > 0.1
    CONTROL_FIRED["C3"] = fired
    check("C3 wrong character: chi_+ readout is the SIGMA3 channel "
          "(28/126/344 at p = 3/5/7), not f8 (-4/-2/24); the (+,0,0) "
          "window differs from the deployed one by rel %.2f (macro)"
          % dmax, fired)

    # C4 random parities break composition
    viol = 0
    for p, q in ((3, 5), (3, 7), (5, 7), (3, 11), (5, 11)):
        Ap = lcg(int(sig3[p]) + 1)
        Bp = int(sig3[p]) - Ap
        Aq = lcg(int(sig3[q]) + 1)
        Bq = int(sig3[q]) - Aq
        Apq = lcg(int(sig3[p * q]) + 1)
        Bpq = int(sig3[p * q]) - Apq
        if Ap * Aq + Bp * Bq != Apq or Ap * Bq + Bp * Aq != Bpq:
            viol += 1
    rec_viol = 0
    for p in (3, 5, 7):
        A1 = lcg(int(sig3[p]) + 1)
        B1 = int(sig3[p]) - A1
        A2 = lcg(int(sig3[p * p]) + 1)
        B2 = int(sig3[p * p]) - A2
        if (A1 * A1 + B1 * B1 - p ** 3 * 1 != A2
                or 2 * A1 * B1 - p ** 3 * 0 != B2):
            rec_viol += 1
    fired = viol > 0 and rec_viol > 0
    CONTROL_FIRED["C4"] = fired
    check("C4 random parities (LCG splits of sigma3): multiplicativity "
          "breaks on %d/5 pairs, p^3 recursion breaks on %d/3 primes"
          % (viol, rec_viol), fired)

    # C5 scrambled glue labels: (0123) -> (1230)
    Th0, Th1, Th2, Th3 = th["Th"]
    broken = 0
    for p in (3, 5, 7):
        newdiff = int(Th1[p]) - int(Th3[p])   # permuted Th'0 - Th'2
        if newdiff != -8 * int(a[p]):
            broken += 1
    fired = broken == 3
    CONTROL_FIRED["C5"] = fired
    check("C5 scrambled glue labels (0123)->(1230): the Th0 - Th2 = "
          "-8 f8 identity breaks at all of p = 3, 5, 7 (%d/3)" % broken,
          fired)


# ================================================================ verdict
def verdict(ss4, ss5, cmp_):
    section("VERDICT")
    n_pass = sum(1 for _n, ok in CHECKS if ok)
    n_all = len(CHECKS)
    print("%d/%d checks passed" % (n_pass, n_all))
    controls_ok = all(CONTROL_FIRED.get(c, False)
                      for c in ("C1", "C2", "C3", "C4", "C5"))
    p123 = all(P_FLAGS.get(k, False) for k in ("P1", "P2", "P3"))
    op_face = ss5["ok_car"] and ss5["ok_pop"]
    if not P_FLAGS.get("P2", True):
        v = "DESCENT-DEAD (the packet GNS state fails positivity)"
    elif not ss5["gl1_ok"]:
        v = "DESCENT-DEAD (the descended GL1 sector breaks PSD at " \
            "reachable depth)"
    elif not controls_ok:
        v = "DESCENT-DEAD (control void: %s)" % [
            c for c in ("C1", "C2", "C3", "C4", "C5")
            if not CONTROL_FIRED.get(c, False)]
    elif p123 and op_face and n_pass == n_all:
        v = "DESCENT-CP-CARRIES"
    elif p123:
        n_neg = sum(1 for sec in ss4["sectors"]
                    if not ss5["psd_car"][sec]) + \
            sum(1 for sec in ss4["sectors"] if not ss5["psd_pop"][sec])
        v = ("DESCENT-PARTIAL (breaking tensor factor: the CONTINUUM "
             "(e-slot) leg -- %d of 24 operator-face sectors "
             "non-PSD; the GL1 sector is the UNIQUE PSD carrier "
             "sector)" % n_neg)
    else:
        fails = [n for n, ok in CHECKS if not ok]
        v = "DESCENT-PARTIAL (%s)" % ("; ".join(fails[:3])
                                      if fails else "non-gate check")
    print("VERDICT: %s" % v)
    if v.startswith("DESCENT-PARTIAL (breaking tensor factor"):
        print("""
PRIME.POSITIVE_DESCENT.01 -- DESCENT-PARTIAL, adjudicated honestly.
What CARRIES at finite level:
  * P1 the packet layer is exact: integral nonneg populations
    A_n = (sigma3 + a_n)/2, B_n = (sigma3 - a_n)/2 with exact
    multiplicative composition and the p^3-corrected Hecke recursion;
    the glue register ties C2 to mu4 exactly (Th0 - Th2 = -8 f8 on
    odd n; Sum Th_j = 240 sigma3 everywhere).
  * P2 the packet GNS state (half-weight mixture of event vector
    states) IS a state at every depth -- positivity manifest (each
    event contributes a square, structurally unable to cross zero)
    and verified in exact rationals; the falling minimal sector is
    f8^2-weight dilution, not an approach to a sign change.  The v1
    linear candidate and the naive signed count FAIL positivity
    (findings F1 and the carrier readout): "signedness as observer
    projection" is now a quantified state-level statement.
  * P3 the descent lands EXACTLY on the deployed Weil evaluation
    (lag-vector identity at machine precision) and the descended (GL1)
    sector stays PSD on the whole frozen ladder with the corpus PD
    margins; the descended battery Grams stay PSD.
What BREAKS (the named factor):
  * P4 the naive packet correspondence OPERATOR (register-trivial
    continuum, atoms carrying the register) is positive ONLY in the
    GL1 sector: all 23 other sector windows are non-PSD at O(1)-O(100)
    because damping/twisting the atom leg exposes the pole--atom
    cancellation.  The breaking tensor factor is the CONTINUUM (e-slot)
    leg, not C2 / F2^4 / mu4: a CP functor at operator level must
    transport the arch+pole layer WITH the character (sector-adapted
    continua = the twisted-channel explicit formulas).
  * NO RH claim; the moving-edge fall of the GL1 margin is reproduced
    read-only, not re-gated.  Contract text below.""")
    print("total runtime %.1f s" % (time.time() - T0))
    return v


def contract_text(ss4, ss5, cmp_):
    section("RECOMMENDED CONTRACT TEXT -- PRIME.POSITIVE_DESCENT.01 "
            "(report only; nothing written)")
    print("""\
    PRIME.POSITIVE_DESCENT.01 (proposed, [C neu] semantics):
    FINITE-LEVEL FACTS (this probe): (i) the packet GNS state on
    N[C2] (x) N[F2^4] (x) N[mu4] is positive at every depth BY
    CONSTRUCTION -- sum of event squares, verified in exact rationals;
    the falling minimal sector is f8^2-weight dilution, structurally
    unable to cross zero (linear and signed-count candidates fail --
    the squared/GNS form is the ONLY positive aggregation found);
    (ii) the GL1 character sector of the packet
    correspondence operator is bit-identical to the deployed Weil
    window and is its UNIQUE PSD sector (margins +5.3e-5 -> +1.2e-5
    over X = 4 -> 10); (iii) every damped/twisted sector breaks
    because the register-trivial continuum cannot follow the atom leg
    (the pole--atom cancellation is exposed).
    THE CONTRACT MUST THEREFORE DEMAND THREE OBJECTS:
      (1) SECTOR-ADAPTED CONTINUA (the missing CP-functor data): for
          each character sector chi, the arch/pole layer of the
          TWISTED channel (the explicit-formula continuum of the
          chi-twisted L-data; for the f8 sector: weight-4 arch factor,
          NO pole), such that the sector window
          T_cont^chi + Sum Re chi(x_n) Q_n is PSD at finite level.
          Finite-level falsifier: exhibiting the f8-sector continuum
          and finding its window non-PSD kills the operator face for
          good; constructing it PSD promotes the functor from
          state-level to operator-level.
      (2) SECTOR-PSD PERSISTENCE (the GL1 limit): the weak-* limit
          (Z1-COMPACTNESS frame, v780) of the GL1 sector functional
          stays in the cone as X -> infinity.  This IS Weil
          positivity, now typed as: "the sign sector of a manifestly
          positive packet object stays PSD" -- the sign is never
          controlled directly, only the sector compression.
      (3) THE CARRIER INTERTWINER: a positive identification, in the
          GNS limit, of the population register (chi_- readout =
          damped Hecke ratio a_n/sigma3(n)) with the carrier register
          (chi_- readout = the unit-modulus sign).  At finite level
          this step is NOT CP-trivial (the signed count fails
          positivity); the contract must name the renormalization /
          amplification limit as the single non-automatic step.
    STOP CONDITIONS: no fixed-d variants, no re-gating of the closed
    diagonal-Gram objects, no RH claim; (2) failing at any finite
    depth = DESCENT-DEAD for the route; (1) and (3) without (2) are
    decorative.
    FALSIFIER AT FINITE LEVEL (inherited): any rung where a non-GL1
    carrier sector becomes PSD-binding while GL1 stays positive would
    break the 'GL1 is the unique carrier edge' reading measured
    here.""")


def main():
    print("=" * 74)
    print("PRIME.POSITIVE_DESCENT.01 -- the finite-level completely "
          "positive")
    print("descent from the extended packet register to the GL1/Weil "
          "state")
    print("=" * 74)
    g0_firewall()
    th = s1_theta_layer()
    pk = s2_packet(th)
    P_FLAGS["P1"] = all(ok for n, ok in CHECKS if n.startswith(("S1",
                                                                "S2")))
    frame = s3_label_frame()
    ss4 = s4_events(th, frame)
    P_FLAGS["P2"] = all(ok for n, ok in CHECKS if n.startswith("S4"))
    ss5 = s5_descent(th, frame, ss4)
    P_FLAGS["P3"] = all(ok for n, ok in CHECKS
                        if n.startswith(("S3", "S5")))
    cmp_ = s6_comparison(ss4, ss5)
    s7_controls(th, frame, ss4, ss5)
    v = verdict(ss4, ss5, cmp_)
    contract_text(ss4, ss5, cmp_)
    n_pass = sum(1 for _n, ok in CHECKS if ok)
    return 0 if (n_pass == len(CHECKS)
                 and not v.startswith("DESCENT-DEAD")) else 1


if __name__ == "__main__":
    sys.exit(main())
