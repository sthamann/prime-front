#!/usr/bin/env python3
"""
PRIME.PHASE.LOCALFACTOR.NOGO.01 -- the permanent no-go typing of the
local Euler-phase route: four identities, established symbolically
exactly, connected to the measured night results (CCXI / CCXIX /
CCXXIII / CCXXIV), and frozen as the replacement of the Potapov
successor route.

EXPLORATION ONLY.  No RH claim in any direction.  Nothing outside
experiments/tfpt-discovery/ + experiments/next.txt is touched.

------------------------------------------------------------------ WHY
CCXXIII proved the wall read is exactly the derivative of a completed
unitary phase (coordinate change; the Euler GROUPING is the measurable
content).  CCXXIV computed the Krein index of that phase and buried the
route: the negative index is INDEX-PROPORTIONAL (+0.997 in the channel
cap), the halfgap shift removes not one negative direction, and the
signature is world-blind (WALLPAPER).  What was still missing is the
STRUCTURAL REASON, established at the level of exact identities: WHY
must every local-factor route carry negativity, and WHY is the fully
completed Euler phase arithmetically empty?  This probe verifies the
program lead's four hand-derived identities (verify, do not trust) and
freezes the resulting no-go as a permanent typing result.

------------------------------------------------- THE FOUR IDENTITIES
With s = 1/2 + it, a_p = p^{-1/2}, z = e^{it log p}, the local Euler
phase U_p(t) = (1 - p^{-1/2-it})/(1 - p^{-1/2+it}), the Blaschke
factor B_a(z) = (z-a)/(1-az), the Poisson kernel
P_a(theta) = (1-a^2)/(1-2a cos theta + a^2):

(I1)  U_p(z) = B_{a_p}(z)/z on |z| = 1 -- the local factor is a
      QUOTIENT of inner functions (numerator inner, denominator
      inner-in-denominator): a generalized (quotiented) Schur factor,
      not a Schur function.  [sympy exact]
(I2)  d/dt arg U_p(t) = log p * (P_{a_p}(t log p) - 1) -- each prime
      contributes a POSITIVE Poisson peak MINUS a UNIFORM background.
      Cross-checked exactly against the CCXXIII prime-power comb form
      2 sum_k (log p / p^{k/2}) cos(k t log p).  [sympy exact + wards]
(I3)  The Pick kernel K_{U_p}(z,w) = (1 - U_p(z) conj(U_p(w)))
      / (1 - z conj(w)) decomposes EXACTLY as K_+ - K_- with BOTH
      rank one positive:
        K_+ = (1-a^2) f(z) conj(f(w)),  f(z) = 1/(z(1-az)),
        K_- = h(z) conj(h(w)),          h(z) = 1/z.
      Every local factor carries EXACTLY ONE negative square
      (Krein-Langer class S_1), and the negative square is exactly the
      1/z block (the denominator inner factor).  [sympy exact +
      numeric census, products: kappa(prod_{p in S} U_p) = |S|]
(I4)  THE TRIVIALITY: after analytic continuation the completed Euler
      phase carries no arithmetic --
        prod_p U_p(t) = zeta(1/2-it)/zeta(1/2+it)
                      = pi^{-it} Gamma(1/4+it/2)/Gamma(1/4-it/2)
                      = G_inf(t)   (functional equation, Riemann 1859),
      hence G_inf(t)^{-1} prod_p U_p(t) = 1, and
        xi(1/2-it)/xi(1/2+it) = 1 EXACTLY.
      Numerically: (a) mpmath 50-digit verification of both equalities
      (1e-30); (b) in the absolutely convergent regime sigma = 2 / 1.2
      the finite-X product converges to the continued zeta ratio with
      the measured tail law; (c) ON the critical line the SHARP
      finite-X product does NOT converge (wrapped distance O(1) at all
      X) -- the classical zeta-POLE block, computed in closed form as
      P(L,t) = int_0^L (2/u) e^{u/2} sin(tu) (1-u/L) du (log-triangular
      smoothing w_p = 1 - log p/log X), grows like X^{1/2} and must be
      carried explicitly; after subtracting it the corrected phase
      converges to the analytic target
        A(t) = arg G_inf(t) - 2 arg(-1/2 + it)   (mod 2pi)
      (the -2 arg(s-1) offset is the Frullani/pole boundary term,
      derived, not fitted) with the MEASURED law ~ (log X)^{-0.94}:
      the residual after the pole block is exactly the ZERO factor of
      the hybrid Euler-Hadamard decomposition (EXTERNAL-CITED:
      Gonek-Hughes-Keating, Duke Math. J. 136 (2007) 507-549) -- the
      completed boundary phase carries NO new arithmetic information;
      the nontrivial remainder IS the Hadamard/zero factor.

--------------------------------- CONNECTIONS TO THE MEASURED RESULTS
CCXXIV (Krein index WALLPAPER, index-proportional +0.997): I3 is the
mechanism -- every local factor contributes exactly one negative
square, Krein-Langer additivity gives kappa(prod over S) = |S|
(measured here exactly for |S| = 1..6), so a deployment resolving ~n
local factors carries ~n negative squares: the index MUST grow with
the cap and can never be finite for the full Euler grouping.
CCXI (negative channels never empty, h-stable): same mechanism -- the
signed representing measure inherits one negative direction per
resolved local factor.
CCXIX (LEVEL-DECAY-IN-SOURCE-CANCELLATION, the wall margin is a 1e-7
residual of two O(1) blocks): I2 makes the cancellation structural --
the prime side is a sum of POSITIVE Poisson masses sum_p b_p P (each
term strictly positive) minus the uniform background sum_p b_p
(Chebyshev-theta size, warded here on 3 corpus rungs at the deployed
prime-power depth with the exact k-cutoff correction), and the
archimedean block renormalizes the summed backgrounds: the wall is the
small difference.  Measured on the rungs: background/halfgap ratios of
order 1e6..1e7.
Suzuki anchoring (corpus): the atom layer of the window form IS
Suzuki's prime measure, literally (suzuki_contact_probe S1.1, exact;
Suzuki arXiv:2606.09096 eq. 1.3 screw function; Suzuki 2021 JFA 281:
GRH == positivity of the canonical family) -- the zero-negative-
squares property of the residual zero factor is RH itself in the
screw-function dictionary.

------------------------------------------------------------ CONTROLS
IMPOSTOR WEIGHT (w = 0.6 instead of 1/2): the zero-parameter weight
law mu_n = 2 b e^{-k b/2} of the corpus atom table must hold exactly
for w = 1/2 (<= 1e-12) and BREAK at measured O(1) for the impostor;
the impostor's I4 pipeline distances are reported (no hard gate,
disclosed s4).  BLASCHKE CONTROL: B_a alone (numerator only, no 1/z)
must have ZERO negative squares -- the one negative square of U_p is
exactly the denominator block.

VERDICT RULE (frozen BEFORE the frozen run):
  NOGO-TYPED iff all four identities verify (sympy residuals exactly
      zero; float wards <= bars), the Krein census gives kappa = |S|
      exactly for |S| = 1..6 with the Blaschke control at 0, the I4
      triviality holds at 1e-30 with the corrected on-line convergence
      measured (median strictly decreasing, final <= bar), and the
      impostor breaks the weight law at measured O(1).
  IDENTITY-FAILS iff any symbolic residual is nonzero or a ward fails.
  CONTROL-BLIND iff a control passes its break gate.

TYPING / ANTI-CIRCULARITY: no zeta zeros, no zero counts, no prime
oracles (AST-scanned; primes from an in-file sieve are the OBJECT of
study, not an oracle for zeros); mpmath.zeta is evaluated at POINTS ON
the critical line only (values by analytic continuation --
EXTERNAL-CITED classical continuation, never zero locations); the
corpus atom tables come from v563_paper2_readouts READ-ONLY; the rung
Euler ladder is DETECTED from positions (CCXXIII's detector,
re-implemented verbatim); no target eigendata enters anything.
Nothing here proves or disproves RH; the no-go is a statement about
the ROUTE TYPE (local Euler-factor positivity), not about zeta.

SMOKE DISCLOSURE (mandatory, verbatim).  FOUR prototype rounds were
run before this spec was frozen and they DID see numbers:
 (s1) the sympy identities I1/I2/I3 were seen to close exactly in
      prototype; the I2 comb form needed expand_complex on re() --
      a code path, no definition change.
 (s2) the SHARP on-line partial product was measured NOT to converge
      (wrapped distances O(1), median 1.32 at X = 1e6) and the raw
      sums wander (pole term ~X^{1/2}/log X).  The pole block P(L,t)
      and the corrected target A(t) were introduced AFTER seeing this:
      the -2 arg(s-1) offset was first OBSERVED as a stable constant
      and then DERIVED analytically (Frullani boundary term of the
      pole density e^u/u du); it is a derived closed form, not a fit.
      Disclosed: the I4 on-line measurement definition was fixed after
      prototype data; the derivation is in the spec, and the
      convergence bars below were then chosen from the prototype
      values WITH margins: corrected final median 0.0969 -> bar 0.15;
      slope -0.94 vs loglogX -> bar <= -0.5; sharp final median 1.32
      -> non-convergence gate >= 0.3; sigma = 2 final 1.44e-8 -> bar
      1e-6; sigma = 1.2 final 8.99e-4 (non-monotone, oscillatory
      tail) -> bar 1e-2 on the final value only.
 (s3) the Pick census prototype saw n_- = 1 per factor, kappa = m for
      m = 1..6 and the Blaschke control at 0 before freeze; those
      gates are exact integer equalities, nothing tunable.
 (s4) the impostor's I4 distances were seen to fluctuate (0.07..0.74
      uncorrected) -- too unstable for an honest hard gate; the
      impostor is therefore gated on the WEIGHT LAW (deterministic
      O(1) break) and its I4 distances are reported ungated.
No bar was tightened after being met; no census definition was changed
after seeing its result except the I4 pole-block correction disclosed
in (s2), which was added because the uncorrected measurement was
measuring the classical pole, not the arithmetic.

--------------------------------------------- THE FROZEN NO-GO (verbatim)
THE LOCAL-FACTOR NO-GO: the local prime phase explains the comb but
not its positivity -- every local Euler factor U_p is a generalized
Schur function with EXACTLY ONE negative square (I3, Krein-Langer), so
any resolution deploying n local factors carries ~n negative squares
(CCXXIV: index-proportional, measured +0.997; CCXI: negative channels
never empty) and no product of local factors can have finite negative
index, let alone zero.  The fully completed Euler phase is TRIVIAL by
the functional equation: G_inf^{-1} prod_p U_p = 1 after analytic
continuation and xi(1/2-it)/xi(1/2+it) = 1 exactly (I4) -- the
completed boundary phase carries NO new arithmetic information.  The
nontrivial residual phase IS the Hadamard/zero factor (hybrid
Euler-Hadamard: Gonek-Hughes-Keating 2007, EXTERNAL-CITED), whose
zero-negative-squares property is RH itself (Suzuki screw-function
dictionary: the corpus atom layer is literally Suzuki's prime measure,
suzuki_contact_probe / arXiv:2606.09096 / Suzuki 2021 JFA 281).
THEREFORE local Euler-factor positivity routes -- Potapov read as
LOCAL positivity, factor by factor -- are PERMANENTLY CLOSED, and the
successor route PRIME.PHASE.POTAPOV.01 (the Potapov product CCXXIV
deliberately did not attempt) is REPLACED by this no-go.  NO RH claim
in any direction.

Sources (read-only): v563_paper2_readouts (build_window, U_ALL/MU_ALL
atom table); euler_phase_identity_probe (CCXXIII) base detector
re-implemented verbatim; krein_index_census_probe (CCXXIV) inertia
zero-tolerance convention; suzuki_contact_probe (Suzuki dictionary).
CLASSICAL, EXTERNAL-CITED: Euler product + functional equation of the
completed zeta (Riemann 1859; Titchmarsh, Theory of the Riemann
Zeta-function, ch. 2); Blaschke/Poisson boundary derivative and
Pick/Nevanlinna kernels (Garnett, Bounded Analytic Functions);
Krein-Langer generalized Schur classes S_kappa (Krein-Langer 1977);
hybrid Euler-Hadamard product (Gonek-Hughes-Keating, Duke Math. J. 136
(2007) 507-549); Gamma/digamma (Abramowitz-Stegun 6.3;
scipy.special.loggamma/digamma); Frullani integral (classical).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/local_factor_nogo_probe.py
Smoke (declared, reduced sieve/checkpoints):  ... --smoke
"""

import ast
import hashlib
import math
import os
import sys
import time

import numpy as np
import scipy.special as sps
from scipy.integrate import quad

_HERE = os.path.dirname(os.path.abspath(__file__))
_VERIFY = os.path.abspath(os.path.join(_HERE, "..", "..", "verification"))
sys.path.insert(0, _HERE)
sys.path.insert(0, _VERIFY)

import v563_paper2_readouts as core            # noqa: E402 READ-ONLY

SMOKE = "--smoke" in sys.argv

# ---------------------------------------------------------------- frozen
EXACT_WARD = 1e-12           # closed-form vs direct-sum bar
ID_WARD = 1e-10              # identity bar (relative)
UNIT_WARD = 1e-13            # |U| = 1 bar
XI_DPS = 50                  # mpmath working precision (digits)
XI_WARD = 1e-30              # xi / functional-equation bar
SYM_PRIMES = (2, 3, 5, 7, 11, 13, 97, 1009)
PICK_RADII = (0.35, 0.6, 0.85)
PICK_NANG = 16
PICK_SINGLE = (2, 3, 13, 97)
PRIMES6 = (2, 3, 5, 7, 11, 13)
T_XI = (0.7, 1.7, 3.3, 6.4, 9.8, 12.6)
T_LIST = (1.7, 3.3, 6.4, 9.8, 12.6)   # declared, all below gamma_1 = 14.13
SIEVE_N = 10**5 if SMOKE else 10**6
XCK = ((1000, 10000, 100000) if SMOKE else
       (1000, 3162, 10000, 31623, 100000, 316228, 1000000))
SIGMAS = (2.0, 1.2)
SIG2_BAR = 1e-6              # sigma = 2 final ward (s2 disclosed)
SIG12_BAR = 1e-2             # sigma = 1.2 final ward (s2 disclosed)
CORR_FINAL_BAR = 0.15        # corrected on-line final median (s2)
CORR_SLOPE_BAR = -0.5        # corrected law vs loglogX (s2)
SHARP_MIN_MED = 0.3          # sharp NON-convergence gate (s2)
IMP_W = 0.6                  # impostor weight exponent
IMP_LAW_MIN = 0.05           # impostor weight-law break gate
N_RUNGS = 2 if SMOKE else 3
RUNG_TG = np.linspace(0.3, 20.0, 60 if SMOKE else 160)
BX_RATIO_MIN = 1e3           # background/halfgap floor (CCXIX connection)
LADDER_TOL = 1e-11           # integer-multiple detection (CCXXIII verbatim)
BANNED_IDS = ("zetazero", "nzeros", "primerange", "isprime",
              "primepi", "nextprime", "prevprime")

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


def ast_scan(banned):
    src = open(os.path.abspath(__file__), encoding="utf-8").read()
    bad = []
    for node in ast.walk(ast.parse(src)):
        nm = None
        if isinstance(node, ast.Name):
            nm = node.id
        elif isinstance(node, ast.Attribute):
            nm = node.attr
        if nm and nm.lower() in banned:
            bad.append(nm)
    return bad


def sieve(n):
    """in-file Eratosthenes -- the primes are the OBJECT of study here
    (local Euler factors), not an oracle for anything about zeros."""
    sv = np.ones(n + 1, bool)
    sv[:2] = False
    for i in range(2, int(math.isqrt(n)) + 1):
        if sv[i]:
            sv[i * i::i] = False
    return np.nonzero(sv)[0].astype(float)


def phase_arch(t):
    """arg G_inf(t) = 2 Im logGamma(1/4+it/2) - t log pi (EXTERNAL-CITED)."""
    return 2.0 * float(np.imag(sps.loggamma(0.25 + 0.5j * t))) - t * LOG_PI


def dens_arch(t):
    """(1/i) dlog G_inf = Re psi(1/4+it/2) - log pi (EXTERNAL-CITED)."""
    return np.real(sps.digamma(0.25 + 0.5j * np.asarray(t))) - LOG_PI


def wrap(d):
    return abs(float(np.angle(np.exp(1j * d))))


def pole_block(L, t):
    """P(L,t) = int_0^L (2/u) e^{u/2} sin(tu) (1 - u/L) du -- the
    classical zeta-pole block of the log-triangular-smoothed prime
    phase sum (density e^u/u du of Lambda(n)/log n; Frullani boundary
    term gives the -2 arg(s-1) target offset).  Closed numeric form,
    EXTERNAL-CITED classical."""
    f = lambda u: 2.0 / u * math.exp(0.5 * u) * math.sin(t * u) \
        * (1.0 - u / L)                                       # noqa: E731
    v, _err = quad(f, 0.0, L, limit=800)
    return v


def euler_blocks(uu, mm):
    """CCXXIII's ladder detector, verbatim: bases from POSITIONS ONLY
    (no factorization oracle)."""
    order = np.argsort(uu)
    u = np.asarray(uu, float)[order]
    m = np.asarray(mm, float)[order]
    n = u.shape[0]
    kidx = np.ones(n, dtype=int)
    base_of = np.arange(n)
    umax = u[-1] if n else 0.0
    for i in range(n):
        if kidx[i] != 1 or u[i] <= 0.0:
            continue
        k = 2
        while k * u[i] <= umax * (1.0 + 1e-14):
            tgt = k * u[i]
            j = int(np.searchsorted(u, tgt))
            best = -1
            bres = np.inf
            for jj in (j - 1, j, j + 1):
                if 0 <= jj < n:
                    r = abs(u[jj] - tgt) / max(tgt, 1e-300)
                    if r < bres:
                        bres, best = r, jj
            if best >= 0 and bres <= LADDER_TOL and kidx[best] == 1:
                kidx[best] = k
                base_of[best] = i
            k += 1
    return u, m, kidx, base_of


def pick_points():
    pts = []
    for r in PICK_RADII:
        for j in range(PICK_NANG):
            pts.append(r * np.exp(1j * 2.0 * math.pi
                                  * (j + 0.31) / PICK_NANG))
    return np.array(pts)


def u_product(z, alphas):
    out = np.ones_like(z)
    for a in alphas:
        out = out * (z - a) / (z * (1.0 - a * z))
    return out


def pick_census(z, U):
    """inertia of the Pick matrix with the CCXXIV zero-tolerance
    convention ZTOL = 1e3 n eps max|eig|."""
    Z = z[:, None] * np.conj(z[None, :])
    K = (1.0 - U[:, None] * np.conj(U[None, :])) / (1.0 - Z)
    K = 0.5 * (K + K.conj().T)
    ev = np.linalg.eigvalsh(K)
    zt = 1e3 * len(z) * np.finfo(float).eps * max(abs(ev[0]), abs(ev[-1]))
    return int(np.sum(ev < -zt)), int(np.sum(ev > zt)), K


def main():
    section("PRIME.PHASE.LOCALFACTOR.NOGO.01 -- the permanent no-go "
            "typing of the local Euler-phase route: four identities, "
            "symbolically exact, connected to CCXI/CCXIX/CCXXIII/"
            "CCXXIV, frozen.  (EXPLORATION ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s"
          % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
    print("    NO RH claim; no marker moves; experiments/ only.  "
          "Smoke disclosure in the spec, verbatim.%s"
          % ("  [SMOKE MODE]" if SMOKE else ""))

    print("\nS0 -- firewall")
    bad = ast_scan(BANNED_IDS)
    check("S0.1 AST firewall clean (no prime/zero oracles)", not bad,
          ",".join(sorted(set(bad))) if bad else "", kill="K0")
    check("S0.2 DECLARED: primes from an in-file sieve (the OBJECT of "
          "study, not an oracle); mpmath.zeta evaluated at points on "
          "the line ONLY (classical continuation, EXTERNAL-CITED, "
          "never zero locations); atom tables read-only; ladder "
          "detected from positions; no target eigendata", True)

    import sympy as sp

    # ================================================================ S1
    section("S1 -- IDENTITY I1 (sympy exact): U_p(z) = B_{a_p}(z)/z on "
            "|z| = 1 -- a QUOTIENT of inner functions")
    a, zc = sp.symbols("a", real=True, positive=True), sp.Symbol("z")
    t_s, b_s = sp.symbols("t b", real=True, positive=True)
    r11 = sp.simplify((1 - a / zc) / (1 - a * zc)
                      - ((zc - a) / (1 - a * zc)) / zc)
    check("S1.1 [SYMBOLIC-EXACT] U_p = B_a(z)/z as a rational identity "
          "(z = e^{it log p}, a = p^{-1/2}): residual %s" % r11,
          r11 == 0, kill="K1")
    r12 = sp.simplify(((zc - a) / (1 - a * zc))
                      * ((1 / zc - a) / (1 - a / zc)) - 1)
    check("S1.2 [SYMBOLIC-EXACT] B_a is inner on |z| = 1: "
          "B_a(z) B_a(1/z) == 1 (conj z = 1/z on the circle): "
          "residual %s" % r12, r12 == 0, kill="K1")
    Ut = (1 - a * sp.exp(-sp.I * t_s * b_s)) \
        / (1 - a * sp.exp(sp.I * t_s * b_s))
    r13 = sp.simplify(sp.expand_complex(Ut * sp.conjugate(Ut)) - 1)
    check("S1.3 [SYMBOLIC-EXACT] |U_p(t)| == 1 on the critical axis: "
          "U conj(U) - 1 = %s" % r13, r13 == 0, kill="K1")
    check("S1.4 typed: the local factor is numerator-inner over "
          "denominator-inner (B_a over z) -- a GENERALIZED (quotiented) "
          "Schur factor, NOT a Schur function; the denominator z is "
          "the block that will carry the negative square (S3)",
          r11 == 0 and r12 == 0 and r13 == 0)

    # ================================================================ S2
    section("S2 -- IDENTITY I2 (sympy exact + wards): d/dt arg U_p = "
            "log p (P_{a_p}(t log p) - 1) -- Poisson peak MINUS "
            "uniform background; == the CCXXIII prime-power comb")
    P_s = (1 - a**2) / (1 - 2 * a * sp.cos(b_s * t_s) + a**2)
    dens_s = sp.diff(sp.log(Ut), t_s) / sp.I
    r21 = sp.simplify(sp.expand_trig(sp.together(
        sp.expand(dens_s - b_s * (P_s - 1)).rewrite(sp.cos))))
    check("S2.1 [SYMBOLIC-EXACT] (1/i) d/dt log U_p == "
          "b (P_a(bt) - 1), b = log p: residual %s" % r21,
          r21 == 0, kill="K1")
    zz_s = a * sp.exp(sp.I * b_s * t_s)
    r22 = sp.simplify(sp.expand_trig(sp.together(
        2 * b_s * sp.re(sp.expand_complex(zz_s / (1 - zz_s)))
        - b_s * (P_s - 1))))
    check("S2.2 [SYMBOLIC-EXACT] the CCXXIII comb closed form agrees "
          "EXACTLY: 2b Re[z/(1-z)] == b (P_a - 1): residual %s" % r22,
          r22 == 0, kill="K1")
    k_s, x_s = sp.Symbol("k", integer=True, positive=True), sp.Symbol("x")
    s_geo = sp.Sum(x_s**k_s, (k_s, 1, sp.oo)).doit()
    s_log = sp.Sum(x_s**k_s / k_s, (k_s, 1, sp.oo)).doit()
    g_ok = (sp.simplify(s_geo.args[0][0] - x_s / (1 - x_s)) == 0
            and s_geo.args[0][1] == (sp.Abs(x_s) < 1))
    l_ok = (sp.simplify(s_log.args[0][0] + sp.log(1 - x_s)) == 0)
    check("S2.3 [SYMBOLIC-EXACT] the resummations: sum_k x^k = x/(1-x) "
          "and sum_k x^k/k = -log(1-x) on |x| < 1 (sympy piecewise "
          "branches) => the prime-power comb 2 sum_k b a^k cos(ktb) IS "
          "the Poisson form and arg U_p = -2 arg(1 - a e^{itb})",
          g_ok and l_ok, kill="K1")
    tg = np.linspace(0.3, 30.0, 240)
    worst = 0.0
    pmin_glob = np.inf
    for p in SYM_PRIMES:
        b = math.log(p)
        ap = p ** -0.5
        z = ap * np.exp(1j * tg * b)
        dser = np.zeros_like(tg)
        aser = np.zeros_like(tg)
        for k in range(1, 400):
            c = ap ** k
            if c < 1e-18:
                break
            dser += 2.0 * b * c * np.cos(k * tg * b)
            aser += 2.0 * (c / k) * np.sin(k * tg * b)
        pois = b * ((1.0 - ap * ap)
                    / (1.0 - 2.0 * ap * np.cos(tg * b) + ap * ap) - 1.0)
        sc = max(float(np.max(np.abs(dser))), 1e-300)
        worst = max(worst, float(np.max(np.abs(dser - pois))) / sc)
        sc2 = max(float(np.max(np.abs(aser))), 1e-300)
        worst = max(worst, float(np.max(np.abs(
            aser + 2.0 * np.angle(1.0 - z)))) / sc2)
        pmin_glob = min(pmin_glob, float(np.min(pois / b + 1.0)))
    check("S2.4 numeric ward on %d primes x %d t: truncated k-comb == "
          "Poisson-minus-background AND arg series == -2 arg(1-z): max "
          "rel dev %.2e <= %.0e; the Poisson part P_a is STRICTLY "
          "POSITIVE (min %.3e > 0)"
          % (len(SYM_PRIMES), len(tg), worst, EXACT_WARD, pmin_glob),
          worst <= EXACT_WARD and pmin_glob > 0.0, kill="K2")
    check("S2.5 typed: PEAK-MINUS-BACKGROUND -- each prime contributes "
          "a strictly positive Poisson peak log p * P_a (mass "
          "concentrated at t log p = 0 mod 2pi) MINUS the uniform "
          "background log p; positivity of the comb read is a fight "
          "between summed peaks and summed backgrounds (S5 measures "
          "it on corpus rungs)", r21 == 0 and worst <= EXACT_WARD)

    # ================================================================ S3
    section("S3 -- IDENTITY I3 (sympy exact + census): the Pick kernel "
            "of U_p splits EXACTLY as K_+ - K_-, both rank one "
            "positive => EXACTLY ONE negative square per local factor")
    w_c = sp.Symbol("w")
    Uz = (zc - a) / (zc * (1 - a * zc))
    Uw = (w_c - a) / (w_c * (1 - a * w_c))
    Kk = (1 - Uz * Uw) / (1 - zc * w_c)
    Kp = (1 - a**2) / (zc * (1 - a * zc) * w_c * (1 - a * w_c))
    Km = 1 / (zc * w_c)
    r31 = sp.simplify(sp.together(Kk - (Kp - Km)))
    check("S3.1 [SYMBOLIC-EXACT] K_{U_p}(z,w) == (1-a^2) f(z) f(w~) - "
          "h(z) h(w~) with f = 1/(z(1-az)), h = 1/z (w~ the conjugate "
          "coordinate): residual %s" % r31, r31 == 0, kill="K1")
    z_pts = pick_points()
    dmax = 0.0
    cen_ok = True
    for p in PICK_SINGLE:
        ap = p ** -0.5
        U = u_product(z_pts, [ap])
        nn, npos, K = pick_census(z_pts, U)
        f = 1.0 / (z_pts * (1.0 - ap * z_pts))
        h = 1.0 / z_pts
        K2 = (1.0 - ap * ap) * f[:, None] * np.conj(f[None, :]) \
            - h[:, None] * np.conj(h[None, :])
        dmax = max(dmax, float(np.max(np.abs(K - K2)))
                   / max(float(np.max(np.abs(K))), 1e-300))
        cen_ok = cen_ok and (nn == 1) and (npos == 1)
        print("    p=%4d  n_- = %d  n_+ = %d (rank-2 kernel)"
              % (p, nn, npos))
    check("S3.2 the two rank-one vectors EXHIBITED and warded on %d "
          "disk points x %d primes: K == (1-a^2) f f* - h h*: max rel "
          "dev %.2e <= %.0e" % (len(z_pts), len(PICK_SINGLE), dmax,
                                EXACT_WARD),
          dmax <= EXACT_WARD, kill="K2")
    check("S3.3 census: every single local factor has EXACTLY ONE "
          "negative square (n_- = 1, n_+ = 1, kernel rank 2) -- "
          "Krein-Langer class S_1", cen_ok, kill="K2")
    Ub = (z_pts - 2.0 ** -0.5) / (1.0 - 2.0 ** -0.5 * z_pts)
    nnb, nposb, _ = pick_census(z_pts, Ub)
    check("S3.4 BLASCHKE CONTROL: B_a alone (numerator only, no 1/z) "
          "has ZERO negative squares (n_- = %d) -- the one negative "
          "square of U_p is EXACTLY the denominator inner factor z"
          % nnb, nnb == 0, kill="K3")
    prod_ok = True
    kap = []
    for m in range(1, 7):
        alphas = [p ** -0.5 for p in PRIMES6[:m]]
        U = u_product(z_pts, alphas)
        nn, npos, _ = pick_census(z_pts, U)
        kap.append(nn)
        prod_ok = prod_ok and (nn == m)
    print("    kappa(prod_{p in S} U_p) over |S| = 1..6: %s"
          % kap)
    check("S3.5 KREIN-LANGER ADDITIVITY, measured EXACTLY: "
          "kappa(prod) == |S| for |S| = 1..6 -- every resolved local "
          "factor adds one negative square; THIS is CCXXIV's "
          "index-proportional law (+0.997 in the cap) and CCXI's "
          "never-empty negative channels, now with the structural "
          "mechanism", prod_ok, kill="K2")
    check("S3.6 typed: LOCAL-NEGATIVITY-STRUCTURAL -- no product of "
          "local Euler factors can be a Schur function (kappa = 0); "
          "the negative index of any local-factor deployment grows "
          "with the number of resolved factors, unconditionally",
          r31 == 0 and cen_ok and prod_ok)

    # ================================================================ S4
    section("S4 -- IDENTITY I4 (mpmath 50 digits + measured "
            "convergence): the completed Euler phase is TRIVIAL -- "
            "G_inf^{-1} prod_p U_p = 1 after continuation; "
            "xi(1/2-it)/xi(1/2+it) = 1 exactly")
    import mpmath as mp
    mp.mp.dps = XI_DPS
    dxi = 0.0
    dfe = 0.0
    for t in T_XI:
        s = mp.mpf("0.5") + 1j * mp.mpf(str(t))
        xi_s = mp.mpf("0.5") * s * (s - 1) * mp.pi ** (-s / 2) \
            * mp.gamma(s / 2) * mp.zeta(s)
        xi_1s = mp.mpf("0.5") * (1 - s) * (-s) * mp.pi ** (-(1 - s) / 2) \
            * mp.gamma((1 - s) / 2) * mp.zeta(1 - s)
        dxi = max(dxi, float(abs(xi_1s / xi_s - 1)))
        lhs = mp.zeta(1 - s) / mp.zeta(s)
        rhs = mp.pi ** (-1j * mp.mpf(str(t))) \
            * mp.gamma(mp.mpf("0.25") + 0.5j * mp.mpf(str(t))) \
            / mp.gamma(mp.mpf("0.25") - 0.5j * mp.mpf(str(t)))
        dfe = max(dfe, float(abs(lhs / rhs - 1)))
    check("S4.1 [EXTERNAL-CITED, Riemann 1859] "
          "xi(1/2-it)/xi(1/2+it) == 1 EXACTLY (mpmath %d digits, %d "
          "t): max |ratio-1| %.2e <= %.0e"
          % (XI_DPS, len(T_XI), dxi, XI_WARD), dxi <= XI_WARD,
          kill="K1")
    check("S4.2 [EXTERNAL-CITED] the functional equation: "
          "zeta(1/2-it)/zeta(1/2+it) == pi^{-it} Gamma(1/4+it/2)/"
          "Gamma(1/4-it/2) = G_inf(t) at %.0e (max dev %.2e) -- "
          "G_inf^{-1} prod_p U_p = 1 AFTER ANALYTIC CONTINUATION, the "
          "continuation carried by zeta itself"
          % (XI_WARD, dfe), dfe <= XI_WARD, kill="K1")

    primes = sieve(SIEVE_N)
    lp = np.log(primes)
    print("    sieve: %d primes <= %d  [%.1f s]"
          % (len(primes), SIEVE_N, time.time() - T0))
    # -- S4.3/S4.4 the absolutely convergent regime
    for sig, bar in zip(SIGMAS, (SIG2_BAR, SIG12_BAR)):
        asig = primes ** -sig
        errs = []
        for t in (3.3, 9.8):
            argu = -2.0 * np.angle(1.0 - asig * np.exp(1j * t * lp))
            A = np.cumsum(argu)
            zr = mp.zeta(mp.mpf(str(sig)) - 1j * mp.mpf(str(t))) \
                / mp.zeta(mp.mpf(str(sig)) + 1j * mp.mpf(str(t)))
            tgt = float(mp.arg(zr))
            row = [wrap(A[int(np.searchsorted(primes, X, side="right"))
                          - 1] - tgt) for X in XCK]
            errs.append(row)
            print("    sigma=%.1f t=%4.1f  err(X): %s"
                  % (sig, t, " ".join("%.2e" % v for v in row)))
        fin = max(e[-1] for e in errs)
        sl = np.polyfit(np.log(np.array(XCK, float)),
                        np.log(np.maximum(
                            np.median(np.array(errs), axis=0), 1e-300)),
                        1)[0]
        check("S4.%d CONVERGENT REGIME sigma = %.1f: the finite-X "
              "product converges to the continued zeta ratio: final "
              "err %.2e <= %.0e; measured tail law slope %+.2f "
              "(classical expectation ~ %+.1f)"
              % (3 if sig == SIGMAS[0] else 4, sig, fin, bar, sl,
                 1.0 - sig), fin <= bar, kill="K2")
    # -- S4.5/S4.6 the on-line measurement
    sharp_fin = []
    corr_med = None
    corr_tab = []
    for t in T_LIST:
        argu = -2.0 * np.angle(1.0 - primes ** -0.5
                               * np.exp(1j * t * lp))
        A = np.cumsum(argu)
        B = np.cumsum(argu * lp)
        tgt_sharp = phase_arch(t)
        tgtA = phase_arch(t) - 2.0 * math.atan2(t, -0.5)
        rs = []
        rc = []
        for X in XCK:
            L = math.log(X)
            i = int(np.searchsorted(primes, X, side="right")) - 1
            rs.append(wrap(A[i] - tgt_sharp))
            rc.append(wrap((A[i] - B[i] / L) - pole_block(L, t) - tgtA))
        sharp_fin.append(rs[-1])
        corr_tab.append(rc)
        print("    t=%5.1f sharp: %s" % (t, " ".join("%.3f" % v
                                                     for v in rs)))
        print("           corr : %s" % " ".join("%.4f" % v for v in rc))
    med_sharp = float(np.median(sharp_fin))
    check("S4.5 THE HONEST FINDING: the SHARP on-line partial product "
          "does NOT converge to the archimedean phase -- median "
          "wrapped distance %.2f >= %.2f at X = %d (the classical "
          "zeta-POLE block ~X^{1/2}/log X dominates; convergence to "
          "the trivial completed phase REQUIRES carrying the pole and "
          "zero bookkeeping)" % (med_sharp, SHARP_MIN_MED, XCK[-1]),
          med_sharp >= SHARP_MIN_MED, kill="K2")
    corr_med = np.median(np.array(corr_tab), axis=0)
    mono = bool(np.all(np.diff(corr_med) < 0.0))
    slope = float(np.polyfit(np.log(np.log(np.array(XCK, float))),
                             np.log(np.maximum(corr_med, 1e-300)), 1)[0])
    print("    corrected median over t: %s"
          % " ".join("%.4f" % v for v in corr_med))
    check("S4.6 POLE-BLOCK-CORRECTED convergence (log-triangular "
          "smoothing + closed P(L,t), target A(t) = arg G_inf - "
          "2 arg(-1/2+it), derived): median strictly decreasing (%s), "
          "final %.4f <= %.2f, law slope %+.2f <= %+.1f vs log log X "
          "-- the residual is the ZERO factor of the hybrid "
          "Euler-Hadamard decomposition (Gonek-Hughes-Keating 2007, "
          "EXTERNAL-CITED): ALL remaining arithmetic lives there"
          % (mono, float(corr_med[-1]), CORR_FINAL_BAR, slope,
             CORR_SLOPE_BAR),
          mono and float(corr_med[-1]) <= CORR_FINAL_BAR
          and slope <= CORR_SLOPE_BAR, kill="K2")
    imp_fin = []
    for t in T_LIST:
        argu = -2.0 * np.angle(1.0 - primes ** -IMP_W
                               * np.exp(1j * t * lp))
        A = np.cumsum(argu)
        B = np.cumsum(argu * lp)
        L = math.log(XCK[-1])
        i = int(np.searchsorted(primes, XCK[-1], side="right")) - 1
        tgtA = phase_arch(t) - 2.0 * math.atan2(t, -0.5)
        imp_fin.append(wrap((A[i] - B[i] / L) - pole_block(L, t) - tgtA))
    print("    IMPOSTOR (a_p = p^{-%.1f}) corrected final distances: "
          "%s  (median %.3f vs truth %.4f) -- REPORTED, not gated "
          "(disclosed s4)"
          % (IMP_W, " ".join("%.3f" % v for v in imp_fin),
             float(np.median(imp_fin)), float(corr_med[-1])))

    # ================================================================ S5
    section("S5 -- THE RETRO-EXPLANATION ON CORPUS RUNGS: I2's "
            "peak-minus-background at the deployed prime-power depth "
            "(exact k-cutoff), the weight law, and the CCXIX "
            "cancellation scale")
    rungs = []
    for kz in range(2, 40):
        try:
            rr = core.build_window(kz)
        except Exception:
            continue
        if not (core.H_MIN <= rr["h"] <= core.HCAP):
            continue
        if rr["X"] > core.ATOM_MAX:
            continue
        rungs.append(rr)
        if len(rungs) >= N_RUNGS:
            break
    check("S5.1 corpus rung ladder: %d declared rungs (h %s)"
          % (len(rungs), "/".join(str(r["h"]) for r in rungs)),
          len(rungs) >= N_RUNGS, kill="K2")
    d_law = 0.0
    d_imp = np.inf
    d_dec = 0.0
    rows = []
    for rr in rungs:
        alpha, h = float(rr["alpha"]), rr["h"]
        uu = np.asarray(rr["uu"], float)
        mm = 2.0 * np.asarray(rr["lam"], float)
        u, m_srt, kidx, base_of = euler_blocks(uu, mm)
        b_of = u[base_of]
        pred = 2.0 * b_of * np.exp(-0.5 * u)
        pred_imp = 2.0 * b_of * np.exp(-IMP_W * u)
        scl = np.maximum(np.abs(m_srt), np.abs(pred))
        d_law = max(d_law, float(np.max(np.abs(m_srt - pred) / scl)))
        d_imp = min(d_imp, float(np.max(
            np.abs(m_srt - pred_imp)
            / np.maximum(np.abs(m_srt), np.abs(pred_imp)))))
        # peak-minus-background at deployed depth, two code paths
        direct = np.zeros_like(RUNG_TG)
        for a0 in range(0, len(RUNG_TG), 64):
            b0 = min(len(RUNG_TG), a0 + 64)
            direct[a0:b0] = np.cos(np.outer(RUNG_TG[a0:b0], u)) @ m_srt
        bases = sorted({int(base_of[i]) for i in range(u.shape[0])})
        pois = np.zeros_like(RUNG_TG)
        posp = np.zeros_like(RUNG_TG)
        BX = 0.0
        for i in bases:
            b = u[i]
            if b <= 0:
                continue
            ap = m_srt[i] / (2.0 * b)
            K = int(math.floor(2.0 * alpha / b + 1e-12))
            z = ap * np.exp(1j * RUNG_TG * b)
            Pk = (1.0 - ap * ap) / (1.0 - 2.0 * ap * np.cos(RUNG_TG * b)
                                    + ap * ap)
            pois += b * (Pk - 1.0) - 2.0 * b * np.real(
                z ** (K + 1) / (1.0 - z))
            posp += b * Pk
            BX += b
        sc = max(float(np.max(np.abs(direct))), 1e-300)
        d_dec = max(d_dec, float(np.max(np.abs(direct - pois))) / sc)
        mu1 = 4.0 * math.sin(math.pi / (2.0 * h + 1.0)) ** 2
        rows.append((h, len(u), len(bases), BX,
                     float(np.min(posp)),
                     float(np.max(np.abs(dens_arch(RUNG_TG)))),
                     BX / (0.5 * mu1)))
    check("S5.2 THE ZERO-PARAMETER WEIGHT LAW on the corpus atom "
          "tables (%d rungs): mu_n == 2 b e^{-k b/2} (i.e. a_p = "
          "p^{-1/2} EXACTLY): max rel dev %.2e <= %.0e"
          % (len(rungs), d_law, EXACT_WARD), d_law <= EXACT_WARD,
          kill="K2")
    check("S5.3 IMPOSTOR CONTROL: the wrong weight a_p = p^{-%.1f} "
          "BREAKS the weight law at measured O(1): min-over-rungs max "
          "rel dev %.3f >= %.2f -- I2's Poisson form with the "
          "corpus-derived generator is EXCLUSIVE to the critical "
          "weight 1/2" % (IMP_W, d_imp, IMP_LAW_MIN),
          d_imp >= IMP_LAW_MIN, kill="K3")
    check("S5.4 PEAK-MINUS-BACKGROUND AT DEPLOYED DEPTH, warded by two "
          "code paths on %d t x %d rungs: direct atom comb == "
          "sum_p [b(P_a - 1) - 2b Re(z^{K+1}/(1-z))] (exact k-cutoff, "
          "bases detected from positions): max rel dev %.2e <= %.0e"
          % (len(RUNG_TG), len(rungs), d_dec, ID_WARD),
          d_dec <= ID_WARD, kill="K2")
    print("    %-5s %7s %7s %12s %12s %10s %12s"
          % ("h", "n_atom", "n_base", "background",
             "min sum bP", "max|arch|", "bg/halfgap"))
    for r in rows:
        print("    %-5d %7d %7d %12.4f %12.4f %10.4f %12.3e" % r)
    ok_pos = all(r[4] > 0.0 for r in rows)
    ok_ratio = all(r[6] >= BX_RATIO_MIN for r in rows)
    check("S5.5 THE CCXIX CONNECTION, measured: the Poisson part "
          "sum_p b P is STRICTLY POSITIVE on every rung (min %s > 0) "
          "while the uniform background sum_p log p is %s -- both "
          "O(1)-in-t blocks are >= %.0e times the half-gap: the wall "
          "margin is the SMALL DIFFERENCE of huge renormalized blocks "
          "(CCXIX's LEVEL-DECAY-IN-SOURCE-CANCELLATION), exactly I2's "
          "peak-minus-background made quantitative"
          % ("/".join("%.2f" % r[4] for r in rows),
             "/".join("%.1f" % r[3] for r in rows), BX_RATIO_MIN),
          ok_pos and ok_ratio, kill="K2")

    # ================================================================ S6
    section("S6 -- THE FROZEN NO-GO (verbatim from the spec)")
    nogo = __doc__.split(
        "--------------------------------------------- "
        "THE FROZEN NO-GO (verbatim)")[1].split("Sources (read-only)")[0]
    print(nogo.rstrip())
    all_ok = all(o for _n, o in CHECKS)
    check("S6.1 the no-go statement is FROZEN (covered by the spec "
          "SHA), printed verbatim, and every load-bearing input to it "
          "passed above", all_ok, kill="K3")

    # ============================================================ verdict
    section("VERDICT")
    v = []
    if all(o for _n, o in CHECKS):
        v.append("NOGO-TYPED")
    elif KILLS and any(k in ("K1", "K2") for k in KILLS):
        v.append("IDENTITY-FAILS")
    else:
        v.append("CONTROL-BLIND")
    v.append("I1-QUOTIENT-INNER-EXACT(sympy 0)")
    v.append("I2-POISSON-PEAK-MINUS-BACKGROUND-EXACT(sympy 0; ward "
             "%.1e)" % worst)
    v.append("I3-ONE-NEGATIVE-SQUARE-PER-FACTOR(sympy 0; kappa == |S| "
             "for 1..6; Blaschke control 0)")
    v.append("I4-COMPLETED-PHASE-TRIVIAL(xi ratio %.1e; FE %.1e; "
             "sharp NON-convergent %.2f; pole-corrected final %.4f, "
             "slope %+.2f)"
             % (dxi, dfe, med_sharp, float(corr_med[-1]), slope))
    v.append("RESIDUAL-IS-HADAMARD-ZERO-FACTOR(GHK 2007, "
             "EXTERNAL-CITED)")
    v.append("POTAPOV-LOCAL-POSITIVITY-PERMANENTLY-CLOSED")
    for s in v:
        print("  " + s)
    return finish()


def finish():
    section("SUMMARY")
    npass = sum(1 for _n, o in CHECKS if o)
    print("  checks: %d/%d PASS" % (npass, len(CHECKS)))
    for n, o in CHECKS:
        if not o:
            print("    FAIL: %s" % n)
    print("  kills: %s" % (",".join(sorted(set(KILLS))) or "none"))
    print("  wall clock: %.1f s" % (time.time() - T0))
    print("  FROZEN_SPEC SHA-256 = %s"
          % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
    print("  EXPLORATION ONLY -- no ledger row, no paper edit, no "
          "marker move, NO RH claim.")
    return 0 if npass == len(CHECKS) else 1


if __name__ == "__main__":
    sys.exit(main())
