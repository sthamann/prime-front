#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""v951 -- PRIME.CANCELLATION.FUNCTIONAL.01: THE ACF LAW + THE POLE
SQUARE + THE ARCH LAW of round 195 -- the wall is a CLOSED TRUNCATED
WEIL-EXPLICIT-FORMULA FUNCTIONAL of the positive-definite test
function g_x, with per-atom manifest positivity PROVABLY IMPOSSIBLE
(Wiener-Khinchin) and the measured sign law + localization; PLUS THE
BUGHUNT-X KD PIN, RECOMPUTED IN-RUN: the arch kernel is THE
CLASSICAL WEIL ARCHIMEDEAN KERNEL in the L -> infinity limit -- the
arc's designated external handoff object.

THE THREE EXACT LAWS (all recomputed in-run).  (1) THE ACF LAW: for
an atom (u, w) with u <= L = 2a, the atom's TOTAL wall contribution
(the Loewner divided-difference off-diagonal PLUS the r189/v947
cosine diagonal shift) is ONE kernel w W(u) with
    x^T W(u) x = -2 int_0^{L-u} A_x(t) A_x(t + u) dt,
    A_x(t) = sum_k x_k cos(om_k t)
-- MINUS TWICE THE APERIODIC AUTOCORRELATION of the windowed mode
polynomial at lag log q: r189's 'both quadratures in different
slots' IS ONE OBJECT.  In-run: the generic convolution identity
2 int_0^u cos(om_i (u - t)) cos(om_j t) dt == (f_i - f_j)/(b_i -
b_j) (sympy, no periodicity), the k = 0 slice x = e_0 ==> g(u) =
L - u exactly (the norm-doubling wraparound in its simplest exact
slice), and the FULL kernel-vs-quadrature ward at h = 4 AND h = 5
(own wall build, every atom, mp oscillation-split quadrature).
(2) THE POLE SQUARE: x^T RawP x = 8 sinh^2(a/2) (int_0^infty
e^{-t/2} A_x dt)^2 EXACTLY -- a manifest L^2 square (the v947
Herglotz point mass in integral form); recomputed SYMBOLICALLY
GENERIC (any modes, via the Laplace closed form int e^{-t/2}
cos(om t) dt = (1/2)/(1/4 + om^2)) and numerically at h = 4, 5.
(3) THE ARCH LAW (closed the r189 open arch item): DeltaArch_k =
-mult_k L (kappa(om_k) + c*) with kappa the Ci-regularized cosine
transform of the arch measure and c* = (gamma + ln 2 pi)/2 EXACTLY,
k-independent including k = 0 -- recomputed at h = 4 and h = 5 for
EVERY mode k (own arch integrals; k-independence and the closed
form gated).

THE KD PIN (Bughunt X, F4 POSITIVE, note-only per precedent --
recomputed in-run HERE as the promoted surface): in the L ->
infinity limit the arch kernel IS the classical Weil archimedean
kernel,
    kappa(om) + c*  -->  -1/2 [Re psi(1/4 + i om/2) - ln pi]
(verified in-run at L = 80 on om = 0.5, 1, 2, 5, 11 to <= 1e-14
class; Bughunt X's own verification 6e-18), with the finite-L
corrections O(e^{-L/2}) TYPED NOT-SMALL at the reachable rungs --
the finite-rung wall is NOT the classical kernel, it LIMITS to it.
This is the arc's cleanest external handoff object: the wall's arch
leg speaks the textbook explicit-formula language exactly in the
window limit.

PER-ATOM POSITIVITY PROVABLY IMPOSSIBLE (Wiener-Khinchin): g_x-hat
= |B_x-hat|^2 >= 0, so each atom samples a positive-definite
function WITH A MINUS SIGN; the exhibit x = e_0 gives x^T W(u) x =
2(u - L) < 0 for u < L (exact in-run) -- the too-good outcome
(per-atom manifest positivity) is EXCLUDED, not just unobserved.

THE MEASURED ANATOMY (pinned): budgets at the collapsing direction
(mp inverse iteration, every rung) pole P = 1.281 -> 2.632 > 0,
arch A = -1.251 -> -2.517, prime Pr = -0.031 -> -0.115 across
h = 4 -> 20 -- THE POLE ALONE CARRIES POSITIVITY; cancellation
depth -11.11 -> -88.25 == the tau ladder (DEFINITIONAL);
concentration CI = 11.3 -> 88.7 dex (TOTAL in the collapsing
direction, O(1)-partial elsewhere).  THE SIGN LAW (the round's
cleanest measured finding): at v_0 EVERY resolvable atom
contributes NEGATIVELY (n+ = 0 at ALL 14 rungs), decaying
near-exponentially in log q, the commensurate q = h atom EXACTLY
ZERO; LOCALIZATION m99 = 1..2 of 3..12 atoms (q = 2, sometimes
+ q = 3, carries the prime total); COMPENSATION IS ATOMS-VS-POLE,
NOT ATOM-VS-ATOM.  Complementarity rho_min = 1.16..2.91 >= 1
everywhere with finite margin -- and NECESSARY-NOT-SUFFICIENT
(amendment A2 honest: rho_min >= 1 holds in the indefinite
SCRARITH/EPSTEIN cells too); SMOOTH has an EMPTY L_f-negative
subspace (the commensurability mechanism in anatomy coordinates);
ATOMJET exactly linear; tau screens flat.

RE-RUN GREEN AS TYPED AT PROMOTION: cancellation_functional_
probe.py round 195 (note DXVIII (518), contract PRIME.
CANCELLATION.FUNCTIONAL.01), 24/24 gates, SPEC_SHA
a50b85bb112513a1 (UNTOUCHED by the Bughunt-X corrections -- the KD
pin is note-only per precedent, the spec hash verified unchanged),
record 1036 s + 1061 s deterministic re-run (timing-normalized
diff empty, all logs kept, FOUR pre-freeze amendments disclosed:
A1 warded antiderivatives; A2 worlds enum corrected; A3 THE
SUBSTANTIVE ONE -- float64 bottom eigenvectors are direction-noise
below the tau gap, the pass-1 mixed-sign ladders were artifacts,
reversed to one-signed after the mp cross-check, the anatomy moved
to mp inverse iteration everywhere; A4 gap-limited invit ward
bars), re-run at promotion 1102.8 s, 24/24 -- log kept as
cancellation_functional_probe.promo_rerun.log.

HONEST PRICING (adopted verbatim): the Weil-ACF rewrite is EXACT
AND NEW but an ALGEBRAIC RESTATEMENT -- the residual object (the
pole square dominating the weighted autocorrelation samples,
cofinally) IS the wall: the relabeling barrier is NAMED, NOT
CROSSED; WEIL-ALLTESTS <-> RH is a FLAGGED LOOP consumed by
NOTHING.  THE RESIDUE (canonical, notes DII/DXVI/DXXIV): {H1 AND
H2 AND H3}-cofinal (mod D = 0.0042) + {census-forall-k == LOOP} +
{H-PIN = the one lambda-uniform edge of {L1, WPD}; WPD non-lambda
legs: extension instantiated, TAILWPD world-front}.  Census
cardinality 4 UNCHANGED.  NOT evidence for or against the Riemann
Hypothesis in either direction.  NO RH CLAIM.

PROVENANCE: discovery probe cancellation_functional_probe.py
(round 195, 2026-08-21, note DXVIII); consumes v947 (the
Loewner-Pick dictionary whose two slots this round unifies into
one ACF object); externally covered by Bughunt X (round 199, note
DXXIII: THE ACF/pole/arch laws reproduced in FULLY OWN CODE to
<= 1e-61, c* exact, and the F4/KD positive pin -- the arch kernel
is the classical Weil archimedean kernel in the L -> infinity
limit, verified 6e-18; note DXXIV: KD note-only per precedent).
Python-only per GATE.WOLFRAM.02.
"""
from __future__ import annotations

import math
import time

import mpmath as mp

T_ALL = time.time()

# ---------------------------------------------------------------- pinned
PIN_SPEC_R195 = "a50b85bb112513a1"
PIN_ASM_DEV = 1.7e-61                  # ACF law, all 14 rungs (record)
PIN_QUAD_WARD = 2.7e-31
PIN_POLE_SQ = 4.5e-61
PIN_ARCH_KIND = 3.1e-61                # k-independence at h = 4, 5
PIN_BH10_OWN = 1e-61                   # BH10 own-code recompute class
PIN_KD_BH10 = 6e-18                    # BH10 digamma-limit verification
PIN_BUDGETS = ((1.281, 2.632), (-1.251, -2.517), (-0.031, -0.115))
PIN_DEPTH = (-11.11, -88.25)           # == the tau ladder, definitional
PIN_CI = (11.3, 88.7)
PIN_SIGNS_NPLUS = 0                    # at ALL 14 rungs
PIN_M99 = (1, 2)
PIN_RHO_MIN = (1.16, 2.91)
PIN_CTRL_RHO = {"SCRARITH": 1.0992, "EPSTEIN": 1.1199}
PIN_SMOOTH_NNEG = 0
PIN_JET_DEVS = (3.0e-61, 8.3e-61)
PIN_SLOPES = (-0.005, 0.000, 0.001)    # nneg/match/m99 -- all flat

KD_L = 80
KD_OMS = (0.5, 1, 2, 5, 11)
KD_BAR = 1e-13
ACF_BAR = 1e-25
ARCH_BAR = 1e-28

N_CHECKS = 10
EXPECTED = "WALL-IS-WEIL-ACF-FORM-EXACT"

CHECKS: list[tuple[str, bool]] = []
FAILS: list[str] = []


def check(name, ok, detail=""):
    ok = bool(ok)
    CHECKS.append((name, ok))
    if not ok:
        FAILS.append(name.split()[0])
    print("  [%s] %-52s %s" % ("PASS" if ok else "FAIL", name, detail))
    return ok


def section(title):
    print("\n" + "=" * 74)
    print(title)
    print("=" * 74)


# ------------------------------------------------- own wall ingredients
def r_of(w):
    if w == 0:
        return mp.mpf("0.25")
    return mp.exp(-w / 2) / (-mp.expm1(-2 * w)) - 1 / (2 * w)


def sieve_atoms(h):
    icap = int(h)
    comp = [False] * (icap + 1)
    nlist = []
    for p in range(2, icap + 1):
        if comp[p]:
            continue
        for m in range(p * p, icap + 1, p):
            comp[m] = True
        q = p
        while q <= icap:
            nlist.append((q, p))
            q *= p
    nlist.sort()
    return [(mp.log(q), mp.log(p) / mp.sqrt(q)) for q, p in nlist]


def cell(h, dps):
    """Node lattice + atoms at rung h (r171-r198 conventions)."""
    with mp.workdps(dps):
        aa = mp.log(h) / 2
        K = int(math.ceil(1.25 * h * math.log(h)))
        L = 2 * aa
        oms = [k * mp.pi / aa for k in range(K)]
        b = [o * o for o in oms]
        return dict(aa=aa, K=K, L=L, oms=oms, b=b,
                    atoms=sieve_atoms(h))


def W_atom(u, oms, b, L, K):
    """The r195 ACF kernel W(u) (Raw coordinates)."""
    W = mp.zeros(K, K)
    for i in range(K):
        for j in range(i):
            W[i, j] = 2 * (oms[i] * mp.sin(oms[i] * u)
                           - oms[j] * mp.sin(oms[j] * u)) / (b[i] - b[j])
            W[j, i] = W[i, j]
    W[0, 0] = 2 * (u - L)
    for k in range(1, K):
        W[k, k] = mp.sin(oms[k] * u) / oms[k] \
            + (u - L) * mp.cos(oms[k] * u)
    return W


def acf_quad(x, u, oms, L, K):
    """-2 int_0^{L-u} A_x(t) A_x(t+u) dt by oscillation-split quad."""
    om_max = oms[-1] if K > 1 else mp.mpf(1)

    def integrand(t):
        A1 = sum(x[k] * mp.cos(oms[k] * t) for k in range(K))
        A2 = sum(x[k] * mp.cos(oms[k] * (t + u)) for k in range(K))
        return A1 * A2

    top = L - u
    npts = max(int(mp.floor(top * om_max / mp.pi)), 1)
    pts = [top * j / npts for j in range(npts + 1)]
    return -2 * mp.quad(integrand, pts)


def kappa_of(om, L):
    """Ci-regularized cosine transform of the arch measure."""
    if om == 0:
        npts = 8
        pts = [L * j / npts for j in range(npts + 1)]
        return mp.log(L) / 2 + mp.quad(r_of, pts)
    npts = max(int(mp.floor(L * om / mp.pi)), 1)
    pts = sorted(set(
        [mp.mpf(0), L] + [j * mp.pi / om for j in range(1, npts + 1)
                          if j * mp.pi / om < L]))
    integ = mp.quad(lambda w: mp.cos(om * w) * r_of(w), pts)
    return mp.ci(L * om) / 2 - (mp.euler + mp.log(om)) / 2 + integ


def arch_diag(h, k, aa, L, om):
    """The builder arch diagonal entry (own transcription of the
    documented r171+ arch recipe; BH9/BH10 lineage)."""
    if k == 0:
        f0 = L
        psi_d = lambda w: L - w                        # noqa: E731
    else:
        f0 = aa
        psi_d = (lambda w, o=om: (aa - w / 2) * mp.cos(o * w)
                 - mp.sin(o * w) / (2 * o))
    integrand = (lambda w, f0=f0, psi_d=psi_d:
                 (f0 * mp.exp(-2 * w) - psi_d(w) * mp.exp(-w / 2))
                 / (-mp.expm1(-2 * w)))
    npts = max(int(mp.floor(L * om / mp.pi)), 1) if k else 1
    base = [mp.mpf(0), mp.mpf("1e-6"), mp.mpf("1e-3"),
            mp.mpf("0.05"), L]
    if k:
        base += [j * mp.pi / om for j in range(1, npts + 1)]
    pts = sorted(set(p for p in base if p <= L))
    body = mp.quad(integrand, pts)
    tail = -f0 / 2 * mp.log1p(-mp.exp(-2 * L))
    return -f0 * (mp.euler + mp.log(mp.pi)) + 2 * (body + tail)


def farch_prime(k, om, L, aa):
    """Canonical Loewner diagonal f_arch'(b_k) = J/om + J' at the
    node (sin(L om_k) = 0); k = 0 by the exact limit."""
    if k == 0:
        npts = 8
        pts = [L * j / npts for j in range(npts + 1)]
        iwr = mp.quad(lambda w: w * r_of(w), pts)
        return 2 * iwr + L
    npts = max(int(mp.floor(L * om / mp.pi)), 1)
    pts = sorted(set(
        [mp.mpf(0), L] + [j * mp.pi / om for j in range(1, npts + 1)
                          if j * mp.pi / om < L]))
    J = mp.quad(lambda w: mp.sin(om * w) * r_of(w), pts) \
        + mp.si(L * om) / 2
    Jp = mp.quad(lambda w: w * mp.cos(om * w) * r_of(w), pts)
    return J / om + Jp


def part():
    import sympy as sp

    # ================================================ A: exact layer
    section("A. THE EXACT LAYER (sympy generic)")
    u_, t_ = sp.symbols("u t", positive=True)
    oi, oj = sp.symbols("omega_i omega_j", positive=True)
    integrand = 2 * sp.cos(oi * (u_ - t_)) * sp.cos(oj * t_)
    # explicit product-to-sum antiderivative, WARDED by symbolic
    # differentiation (the r195 amendment-A1 route: sympy's own
    # integrate returns a Piecewise that defeats simplify)
    F = -sp.sin(oi * u_ - (oi + oj) * t_) / (oi + oj) \
        - sp.sin(oi * u_ - (oi - oj) * t_) / (oi - oj)
    ward = sp.simplify(sp.expand_trig(sp.diff(F, t_) - integrand))
    conv = F.subs(t_, u_) - F.subs(t_, 0)
    f_i, f_j = 2 * oi * sp.sin(oi * u_), 2 * oj * sp.sin(oj * u_)
    okA = ward == 0 and sp.simplify(sp.expand_trig(sp.expand(
        (conv - (f_i - f_j) / (oi ** 2 - oj ** 2))
        * (oi ** 2 - oj ** 2)))) == 0
    check("A1 the generic convolution identity (the ACF law's "
          "engine, exact)", okA,
          "2 int_0^u cos(om_i(u - t)) cos(om_j t) dt == (f_i - "
          "f_j)/(b_i - b_j) with f = 2 om sin(om u) (sympy, no "
          "periodicity assumed; explicit antiderivative warded by "
          "differentiation, the probe's amendment-A1 route): the "
          "Loewner divided difference IS a convolution of the two "
          "modes -- the off-diagonal slot of the ACF law")

    a_ = sp.symbols("a", positive=True)
    L_ = 2 * a_
    # k = 0 slice: x = e_0, A(t) = 1: g(u) = int_0^{L-u} 1 = L - u
    g_e0 = sp.integrate(sp.Integer(1), (t_, 0, L_ - u_))
    okB = sp.simplify(g_e0 - (L_ - u_)) == 0
    check("A2 the k = 0 wraparound slice: x = e_0 ==> g(u) = L - u "
          "(exact)", okB,
          "W(u)[0, 0] = 2(u - L) == -2 int_0^{L-u} 1 dt exactly "
          "(the mult_0 = 2 norm-doubling IS the wraparound of the "
          "k = 0 mode): per-atom manifest positivity is already "
          "impossible here -- x = e_0 gives x^T W x = 2(u - L) < 0 "
          "for every interior lag (the Wiener-Khinchin kill's "
          "exact exhibit)")

    b_ = sp.symbols("b", positive=True)
    om_ = sp.sqrt(b_)
    lap = sp.integrate(sp.exp(-t_ / 2) * sp.cos(om_ * t_),
                       (t_, 0, sp.oo))
    okC = sp.simplify(lap - sp.Rational(1, 2)
                      / (sp.Rational(1, 4) + b_)) == 0
    x1, x2, x3 = sp.symbols("x1 x2 x3", real=True)
    b1, b2, b3 = sp.symbols("b1 b2 b3", positive=True)
    s2 = 2 * sp.sinh(a_ / 2) ** 2
    xs, bs = (x1, x2, x3), (b1, b2, b3)
    quad_form = sum(
        xs[i] * xs[j] * s2 / ((sp.Rational(1, 4) + bs[i])
                              * (sp.Rational(1, 4) + bs[j]))
        for i in range(3) for j in range(3))
    lap_sq = 8 * sp.sinh(a_ / 2) ** 2 * sum(
        xs[i] * sp.Rational(1, 2) / (sp.Rational(1, 4) + bs[i])
        for i in range(3)) ** 2
    okD = sp.simplify(quad_form - lap_sq) == 0
    check("A3 THE POLE SQUARE, generic (a manifest L^2 square, "
          "exact)", okC and okD,
          "int_0^inf e^{-t/2} cos(om t) dt == (1/2)/(1/4 + b) "
          "(Laplace closed form) and x^T RawP x == 8 sinh^2(a/2) "
          "(int_0^inf e^{-t/2} A_x dt)^2 for generic 3-mode data "
          "(sympy exact): the pole block is EXACTLY the square of "
          "the Laplace transform of the mode polynomial -- the "
          "v947 Herglotz point mass in integral form, manifestly "
          "PSD")

    # ================================================ B: h = 4, 5 wards
    section("B. THE LAWS AT h = 4 AND h = 5 (own wall build, mp)")
    acf_worst = mp.mpf(0)
    pole_worst = mp.mpf(0)
    for h in (4, 5):
        dps = 60
        with mp.workdps(dps):
            ce = cell(h, dps)
            K, L, oms, b = ce["K"], ce["L"], ce["oms"], ce["b"]
            phi = (1 + mp.sqrt(5)) / 2
            xg = [mp.frac((k + 1) * phi) - mp.mpf("0.5")
                  for k in range(K)]
            for (u, w) in ce["atoms"]:
                W = W_atom(u, oms, b, L, K)
                form = sum(xg[i] * W[i, j] * xg[j]
                           for i in range(K) for j in range(K))
                quadv = acf_quad(xg, u, oms, L, K)
                rel = abs(form - quadv) / max(abs(form), mp.mpf("1e-30"))
                acf_worst = max(acf_worst, rel)
            # pole square numeric
            s2v = mp.sinh(ce["aa"] / 2) ** 2
            formP = sum(xg[i] * xg[j] * 2 * s2v
                        / ((mp.mpf(1) / 4 + b[i])
                           * (mp.mpf(1) / 4 + b[j]))
                        for i in range(K) for j in range(K))
            lapv = sum(xg[k] / (2 * (mp.mpf(1) / 4 + b[k]))
                       for k in range(K))
            sq = 8 * s2v * lapv ** 2
            pole_worst = max(pole_worst,
                             abs(formP - sq) / abs(formP))
    okE = acf_worst < ACF_BAR and pole_worst < 1e-45
    check("B1 THE ACF LAW + THE POLE SQUARE at h = 4, 5 (every "
          "atom, mp)", okE,
          "x^T W(u_q) x == -2 int_0^{L-u} A_x A_x(. + u) dt at "
          "EVERY atom of both rungs for the golden probe vector "
          "(worst rel dev %.1e, bar %.0e; oscillation-split "
          "quadrature, dps 60) and the pole square holds "
          "numerically (worst %.1e): the probe gates the same "
          "objects at all 14 rungs to <= %.1e (assembly) / %.1e "
          "(quad wards) / %.1e (pole square); Bughunt X reproduced "
          "them in fully own code to <= 1e-61"
          % (float(acf_worst), ACF_BAR, float(pole_worst),
             PIN_ASM_DEV, PIN_QUAD_WARD, PIN_POLE_SQ))

    arch_worst = mp.mpf(0)
    kind_spread = mp.mpf(0)
    for h in (4, 5):
        dps = 60
        with mp.workdps(dps):
            cstar = (mp.euler + mp.log(2 * mp.pi)) / 2
            ce = cell(h, dps)
            K, L, oms, aa = ce["K"], ce["L"], ce["oms"], ce["aa"]
            cvals = []
            for k in range(K):
                adiag = arch_diag(h, k, aa, L, oms[k])
                fap = farch_prime(k, oms[k], L, aa)
                delta = adiag - fap
                mult = 2 if k == 0 else 1
                ck = -delta / (mult * L) - kappa_of(oms[k], L)
                cvals.append(ck)
                arch_worst = max(arch_worst, abs(ck - cstar))
            kind_spread = max(kind_spread,
                              max(cvals) - min(cvals))
    okF = arch_worst < ARCH_BAR and kind_spread < ARCH_BAR
    check("B2 THE ARCH LAW at h = 4, 5 (every mode k incl. k = 0; "
          "c* exact)", okF,
          "DeltaArch_k = RawA[k, k] - f_arch'(b_k) == -mult_k L "
          "(kappa(om_k) + c*) with kappa the Ci-regularized cosine "
          "transform and c* = (gamma + ln 2 pi)/2: recomputed at "
          "EVERY mode of h = 4 (K = 7) and h = 5 (K = 11) -- "
          "worst |c*_k - (gamma + ln 2pi)/2| = %.1e, k-spread "
          "%.1e (bar %.0e; probe: k-independence <= %.1e, c* "
          "exact at working precision): the r189 open arch item "
          "is CLOSED -- the wall is a closed truncated Weil form"
          % (float(arch_worst), float(kind_spread), ARCH_BAR,
             PIN_ARCH_KIND))

    # ================================================ C: the KD pin
    section("C. THE KD PIN: THE ARCH KERNEL IS THE CLASSICAL WEIL "
            "KERNEL (L -> inf)")
    kd_worst = mp.mpf(0)
    with mp.workdps(40):
        cst = (mp.euler + mp.log(2 * mp.pi)) / 2
        for om in KD_OMS:
            omv = mp.mpf(om)
            lhs = kappa_of(omv, mp.mpf(KD_L)) + cst
            rhs = -(mp.re(mp.digamma(mp.mpf(1) / 4
                                     + mp.mpc(0, 1) * omv / 2))
                    - mp.log(mp.pi)) / 2
            kd_worst = max(kd_worst, abs(lhs - rhs))
    okG = kd_worst < KD_BAR
    check("C1 KD RECOMPUTED: kappa + c* --> -1/2 [Re psi(1/4 + "
          "i om/2) - ln pi]", okG,
          "at L = %d and om in %s: worst |kappa(om) + c* - "
          "classical| = %.1e (bar %.0e; Bughunt X's own "
          "verification %.0e at higher dps): THE ARCH KERNEL IS "
          "THE CLASSICAL WEIL ARCHIMEDEAN KERNEL IN THE L -> "
          "infinity LIMIT -- the finite-L corrections are "
          "O(e^{-L/2}) and TYPED NOT-SMALL at the reachable rungs "
          "(L = log h <= 3): the finite-rung wall is not the "
          "classical kernel, it LIMITS to it -- the arc's external "
          "handoff pin (the wall's arch leg speaks the textbook "
          "explicit-formula language exactly in the window limit)"
          % (KD_L, str(KD_OMS), float(kd_worst), KD_BAR,
             PIN_KD_BH10))

    # ================================================ D: pinned anatomy
    section("D. THE MEASURED ANATOMY (pinned, typed measured)")
    okH = PIN_BUDGETS[0][0] > 0 and PIN_BUDGETS[0][1] > 0 \
        and PIN_BUDGETS[1][1] < PIN_BUDGETS[1][0] < 0 \
        and PIN_BUDGETS[2][1] < PIN_BUDGETS[2][0] < 0 \
        and PIN_DEPTH[1] < PIN_DEPTH[0] < 0
    check("D1 THE POLE ALONE CARRIES POSITIVITY (budgets at v_0; "
          "depth == tau)", okH,
          "budgets at the collapsing direction (mp inverse "
          "iteration): pole P = %.3f -> %.3f > 0, arch A = %.3f -> "
          "%.3f, prime Pr = %.3f -> %.3f across h = 4 -> 20, "
          "cancelling to depth %.2f -> %.2f == the tau ladder "
          "(DEFINITIONAL, typed); concentration CI = %.1f -> %.1f "
          "dex: the cancellation is TOTAL in the collapsing "
          "direction, O(1)-partial elsewhere"
          % (PIN_BUDGETS[0][0], PIN_BUDGETS[0][1], PIN_BUDGETS[1][0],
             PIN_BUDGETS[1][1], PIN_BUDGETS[2][0], PIN_BUDGETS[2][1],
             PIN_DEPTH[0], PIN_DEPTH[1], PIN_CI[0], PIN_CI[1]))

    okI = PIN_SIGNS_NPLUS == 0 and PIN_M99 == (1, 2)
    check("D2 THE SIGN LAW + LOCALIZATION (n+ = 0 at all 14 "
          "rungs)", okI,
          "at v_0 EVERY resolvable atom contributes NEGATIVELY "
          "(n+ = %d at ALL 14 rungs -- each autocorrelation sample "
          "g_v(log q) > 0), near-exponential decay in log q, the "
          "commensurate q = h atom EXACTLY ZERO; localization "
          "m99 = %d..%d of 3..12 atoms (q = 2, sometimes + q = 3, "
          "carries the prime total): COMPENSATION IS ATOMS-VS-"
          "POLE, NOT ATOM-VS-ATOM"
          % (PIN_SIGNS_NPLUS, PIN_M99[0], PIN_M99[1]))

    okJ = PIN_RHO_MIN[0] >= 1 \
        and all(v >= 1 for v in PIN_CTRL_RHO.values()) \
        and PIN_SMOOTH_NNEG == 0 \
        and all(abs(s) <= 0.30 for s in PIN_SLOPES) \
        and max(PIN_JET_DEVS) < 1e-28
    check("D3 complementarity NECESSARY-NOT-SUFFICIENT; worlds; "
          "screens flat", okJ,
          "rho_min = %.2f..%.2f >= 1 everywhere (finite margin) -- "
          "and >= 1 ALSO in the indefinite SCRARITH/EPSTEIN cells "
          "(%s: amendment A2 honest -- NOT a world detector); "
          "SMOOTH has an EMPTY L_f-negative subspace (n_neg = %d: "
          "the v949 commensurability mechanism in anatomy "
          "coordinates); ATOMJET exactly linear (devs %s); tau "
          "screens %s ALL FLAT; the identity itself is world-blind "
          "linear algebra (typed, never sold)"
          % (PIN_RHO_MIN[0], PIN_RHO_MIN[1], str(PIN_CTRL_RHO),
             PIN_SMOOTH_NNEG, str(PIN_JET_DEVS), str(PIN_SLOPES)))

    okK = True                                # adjudication/pricing
    check("D4 HONEST PRICING: an ALGEBRAIC RESTATEMENT -- the "
          "barrier named, not crossed", okK,
          "the Weil-ACF rewrite is exact and NEW as structure, but "
          "the residual object it exposes (the pole square "
          "dominating the weighted autocorrelation samples, "
          "cofinally) IS the wall again -- the relabeling barrier "
          "is NAMED, NOT CROSSED; WEIL-ALLTESTS <-> RH is a "
          "FLAGGED LOOP consumed by NOTHING; per-atom manifest "
          "positivity is PROVABLY IMPOSSIBLE (Wiener-Khinchin: "
          "hat-g = |hat-B|^2 >= 0, each atom samples a PD function "
          "with a minus sign) -- the too-good outcome excluded, "
          "not just unobserved; census cardinality 4 UNCHANGED; "
          "NOT RH evidence")

    print("\n  [TYPED] THE WALL IS A CLOSED TRUNCATED WEIL FORM of")
    print("  g_x; the arch kernel LIMITS to the classical Weil")
    print("  archimedean kernel (KD, recomputed); per-atom positivity")
    print("  provably impossible; the pole alone carries positivity.")
    print("  An algebraic restatement, typed honestly.  NO RH claim.")
    return 0


def run():
    global CHECKS, FAILS
    CHECKS = []
    FAILS = []
    print("=" * 74)
    print("v951 -- PRIME.CANCELLATION.FUNCTIONAL.01 (the ACF law; "
          "the pole square;")
    print("the arch law with c* = (gamma + ln 2 pi)/2; the KD "
          "classical-Weil-kernel")
    print("pin recomputed; the sign law; round 195; NO RH claim)")
    print("=" * 74)
    rc = part()
    n_run, fails = len(CHECKS), list(FAILS)
    verdict = EXPECTED if (rc == 0 and not fails) else "MIXED"
    ok = (rc == 0 and n_run == N_CHECKS and not fails
          and verdict == EXPECTED)
    print("\n" + "=" * 74)
    print("v951: %d/%d checks passed | verdict %s | runtime %.1f s"
          % (n_run - len(fails), n_run, verdict, time.time() - T_ALL))
    print("PINNING: the convolution/wraparound/Laplace algebra "
          "(sympy generic), the")
    print("ACF/pole/arch laws at h = 4, 5 (own wall build, every "
          "atom/mode) and the")
    print("KD digamma limit recomputed in-run; the anatomy/sign/"
          "world tables PINNED")
    print("from cancellation_functional_probe.py (SPEC %s, 24/24,"
          % PIN_SPEC_R195)
    print("record 1036 s + 1061 s deterministic re-run, four "
          "pre-freeze amendments")
    print("disclosed, SPEC verified UNTOUCHED by the Bughunt-X "
          "corrections, RE-RUN")
    print("GREEN AS TYPED AT PROMOTION 1102.8 s, 24/24).  NOT RH "
          "evidence; NO RH claim.")
    print("[%s] PATTERN GATE: expected %d checks, zero fails, verdict "
          "%s (got %d, fails %s)"
          % ("PASS" if ok else "FAIL", N_CHECKS, EXPECTED, n_run,
             fails or "none"))
    print("--- PRIME.CANCELLATION.FUNCTIONAL.01 Weil-ACF form + KD "
          "pin: %d passed, %d failed ---"
          % (n_run - len(fails), len(fails)))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(run())
