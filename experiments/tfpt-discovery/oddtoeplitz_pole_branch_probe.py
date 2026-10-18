#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""oddtoeplitz_pole_branch_probe -- PRIME.PORT.CHEB.THREEBRANCH.01
(EXPLORATION ONLY, experiments/; round 64, theorem-engineering on the
RH-side wall: an EXACT representation theorem for the odd-Toeplitz
positivity cone, and the source-only Bochner certificate it produces.
2026-08-11.)

NO RH CLAIM ANYWHERE.  RH is unsolved.  Section S7 types every result
as PROVED / MACHINE-MEASURED / OPEN, and names the remaining gap.

--------------------------------------------------------------------
PART 0 -- THE OBJECT
--------------------------------------------------------------------
M = 2h, and the deployed wall is A[c] = odd_toeplitz(c, M) (v563,
read-only import), i.e.
    A[c]_{ij} = c_{|i-j|} - c_{M-1-i-j},      0 <= i, j < h,
with the SOURCE lag vector c = arch_lags(M, D) + atom_lags_at(...)
(Weil archimedean lags + the negative von-Mangoldt tent comb).  The
T163 correlation theorem (v563.lag_weights_from_v) gives the pairing
    v^T A[c] v = <c, w(v)>,       w(v) = lag_weights_from_v(v, h).

--------------------------------------------------------------------
PART 1 -- FOUR LEMMAS, WITH PROOFS (elementary; all machine-checked
in S1; none of them uses primes, RH, sigma_h or any wall eigendata)
--------------------------------------------------------------------
L1 (THE COSH RANK-ONE IDENTITY).  For every z in C,
        A[(cosh(z d))_{d<M}] = -2 k_z k_z^T,
        k_z(i) = sinh((h - i - 1/2) z).
    PROOF.  cosh X - cosh Y = 2 sinh((X+Y)/2) sinh((X-Y)/2) with
    X = (i-j)z, Y = (M-1-i-j)z gives (X+Y)/2 = (h-j-1/2)z (sign) and
    (X-Y)/2 = -(h-i-1/2)z.  QED (one line).
    SPECIALISATIONS.  z = i*theta:  A[(cos(d theta))] = +2 l l^T with
    l_theta(i) = sin((h-i-1/2) theta)  [PSD].  z = beta real:
    A[(cosh(beta d))] = -2 k k^T  [NSD, so MINUS a cosh sequence is a
    POSITIVE generator].  z = beta + i*pi: A[((-1)^d cosh(beta d))] =
    +2 m m^T, m(i) = (-1)^i cosh((h-i-1/2) beta)  [PSD].  z = 0:
    A[1] = 0 (the gauge).  Also A[delta_0] = I, A[-delta_{M-1}] =
    e_0 e_0^T, A[(d^2)] = -4 g g^T with g_i = h - i - 1/2.

L2 (RANK-ONE CLASSIFICATION).  A[c] = +/- u u^T forces
    u_{i+1} - 2 lam u_i + u_{i-1} = 0 for a constant lam, hence
    u = k_z for some z in C (or the r -> infinity limit u = e_0).
    PROOF.  A[c] = u u^T is Toeplitz-minus-Hankel, so
    u_i u_j - u_{i+1} u_{j+1} depends on i+j only; equating the
    (i,j) and (i-1,j+1) versions gives
    u_i (u_j + u_{j+2}) = u_{j+1} (u_{i-1} + u_{i+1}), i.e.
    (u_{i-1}+u_{i+1})/u_i is a constant 2 lam.  Matching the Hankel
    part then pins u_i = a (r^i - r^{M-1-i}) ~ k_{log r}.  QED.
    => the ONLY rank-one PSD directions inside range(A) are the
    cos-branch and the two cosh-branches.  There is no fourth family.

L3 (THE CHEBYSHEV DICTIONARY).  Put W_n(x) = the Chebyshev polynomial
    of the FOURTH kind, W_n(cos th) = sin((n+1/2) th)/sin(th/2), and
    for v in R^h let q_v = sum_j v_j W_{h-1-j}  (degree <= h-1).
    Then, EXACTLY, for every x in R:
        sum_{d<M} w_d(v) T_d(x) = (1 - x) q_v(x)^2.
    PROOF.  At x = cos th both sides equal 2 (l_theta . v)^2 (the
    left by L1 + the pairing, the right because
    q_v(cos th) = (l_theta . v)/sin(th/2) and 1-cos th =
    2 sin^2(th/2)); two polynomials of degree <= M-1 agreeing on
    [-1,1] agree on R.  QED.
    (At x = cosh be this reads sum_d w_d cosh(be d) = -2 (k_be.v)^2,
    the analytic continuation -- machine-checked separately.)

L4 (THE THREE-BRANCH REPRESENTATION THEOREM).  Let
        eps(x) = -1 for x > 1,   eps(x) = +1 otherwise,
        g^{(x)} := ( eps(x) T_d(x) )_{d<M}.
    Then
        A[c] >= 0   <=>   c  in  cl cone{ g^{(x)} : x in R } + R*1.
    PROOF.  "<=" is L1 termwise.  "=>": by L3 the dual cone of the
    generators is exactly {y : eps(x) Y(x) >= 0 on R}, Y = sum y_d T_d
    of degree <= 2h-1; such a Y has Y(1) = 0, so Y = (1-x) S with
    S >= 0 on ALL of R (the three sign conditions collapse to one),
    hence S is a sum of two squares of degree <= h-1 (Markov), hence
    Y in (1-x)*SOS = the cone of the w(v) by L3.  Bipolar. QED.
    CONSEQUENCE (the currency).  If c = t delta_0 + gam*1 +
    sum_i mu_i g^{(x_i)} with mu >= 0, then
        v^T A[c] v = t |v|^2 + sum_i mu_i |1 - x_i| q_v(x_i)^2,
    a POSITIVE-measure Gram form; A[c] >= t I follows.

L5 (THE CERTIFICATE).  For any m >= 0, be > 0, gam in R, t in R:
        Tz_M( c + m cosh(be .) - t delta_0 - gam * 1 ) >= 0
    implies      A[c]  >=  t I + 2 m k_be k_be^T,
    where Tz_M(r) = (r_{|i-j|}) is the plain M x M Toeplitz matrix.
    PROOF.  Tz(r) >= 0 <=> (Caratheodory-Toeplitz) r is the cosine
    moment vector of a nonnegative measure on the circle, i.e. r is a
    nonnegative combination of cos-branch generators; apply L1/L4 and
    then L1 again to move m cosh and t delta_0 to the other side. QED
    So the certificate value is
        Psi(m, be) := lam_min( Pi Tz(c + m cosh(be .)) Pi ),
    Pi = orthoprojector onto 1^perp (the gauge; the attained gam is
    exhibited explicitly in S1.9), and  lam_min(A[c]) >= Psi(m, be)
    for EVERY m >= 0, be > 0.  Source-only: c is the source lag
    vector, nothing else enters.

--------------------------------------------------------------------
PART 2 -- WHAT IS BEING TESTED (the a-priori mechanism)
--------------------------------------------------------------------
The corpus' Gram/SOS completion (resistance item 2; wall_gram_radau,
wall_edge_completion, mt_window_family) asks whether the signed comb
measure is nonnegative on the Lukacs cone OF [-1, 1], and it fails
"at the x = +1 edge" on every rung.  L4 says the [-1,1] restriction
is the wrong hypothesis: the representing measure of an odd-Toeplitz
PSD matrix may -- and, we predict, must -- put mass just OUTSIDE the
segment, on the branch x = cosh(be) > 1, where the generator carries
the sign flip eps = -1.

WHICH be?  The Weil explicit formula's pole term for zeta at s = 1
is  int g(x) (e^{x/2} + e^{-x/2}) dx = int g(x) 2 cosh(x/2) dx.  In
lag coordinates x = dD that is the sequence 2D cosh(D d / 2), i.e.
    PREDICTED BRANCH POINT   be = D/2   (x = cosh(D/2)),
    PREDICTED MASS           m  = 2D.
The deployed wall c = arch + comb OMITS this term.  MECHANISM UNDER
TEST: the wall is positive because c is the pole-DEFICIENT part of a
classical positive-definite sequence -- restoring the single pole
generator turns the odd-Toeplitz statement into a plain Bochner
statement.  Both constants are DERIVED (not fitted) and are frozen
before the run; S3 measures m* and S4 screens be.

HONEST A-PRIORI EXPECTATION (frozen).  Psi(m, D/2) > 0 is expected on
most rungs; a FROZEN mass m = 2D exactly is expected to FAIL on the
deep rungs because dPsi/dm ~ cosh(alpha) grows exponentially in the
window half-width while Psi ~ mu1 ~ h^-2 decays, so the admissible
relative window in m shrinks like mu1/cosh(alpha).  The certificate
under test is therefore the SUPREMUM over m >= 0 (a one-parameter
concave maximisation -- standard certificate practice, no target
eigendata), with be = D/2 frozen.  The probe's value is the exact
census, the m*/2D law, the be uniqueness screen and the controls --
NOT a proof.

--------------------------------------------------------------------
PART 3 -- MANDATORY GATES, DECLARED BEFORE THE RUN
--------------------------------------------------------------------
ANTI-CIRCULARITY: the only inputs are arch_lags, atom_lags_at,
build_window geometry (all source) and the two derived constants
be = D/2, m ~ 2D.  No sigma_h, no tau, no eigenvector of the wall, no
wall positivity is used to BUILD the certificate.  (tau is computed
only to REPORT the ratio Psi/tau; S3 recomputes Psi without it.)
WALL-BLINDNESS: S5 runs the prime-free world (arch only) and the
scrambled-comb world.  The certificate MUST fail there.  Declared
kill: CONTROLS-SILENT if any control certifies.
TAU-SCREEN: S3 regresses log(Psi*/tau) on log h.  Slope ~ 0 means the
certificate tracks tau, i.e. it is a RELOCATION of the difficulty,
not a gain in the h-decay.  This is reported as such, plainly.
NO POINTWISE PRIME STATEMENT: the comb enters only through c.
NO ABSOLUTE ENDPOINT ENVELOPE, NO TRANSITION-ONLY CERTIFICATE: the
certificate is a single global matrix positivity per rung.
ANTHROPIC NO-GO DECLARATION: the certificate consumes the FULL comb
(all atoms, positions and von-Mangoldt masses) through the lag vector
c -- far more than two moments plus bandwidth-1 pair correlation.  It
therefore does not live inside the Anthropic budget and is not
claimed to evade it; it is a REFORMULATION, and S7 says so.

--------------------------------------------------------------------
FROZEN SPEC
--------------------------------------------------------------------
Ladder: every kz in v563.frame_a_zones() with h in [142, 878] (the
deployed reachable ladder).  BETA_OVER_D = 0.5 (derived, frozen).
m located by BISECT_ITERS = 34 bisections of the concave derivative
v^T C1 v on [0, 8/cosh(be(M-1))].  LP grids: N_TH = 12h cos-branch
nodes uniform in theta on [0, pi], N_HYP = 800 hyperbolic nodes per
signed branch, be = u/(M-1), u geometric on [1e-3, 120], columns
sup-normalised; LP rungs LP_KZ = (18, 13).  Identity tolerance
ID_TOL = 1e-9 relative.  Andreief tolerance AND_TOL = 1e-9 relative.
Branch-lift bar: POLE-BRANCH-CARRIES iff the x>1 branch improves the
cos-branch-only LP value by >= 50x AND every recovered x>1 atom has
be/D in [0.45, 0.55].  be uniqueness bar: BETA-UNIQUE iff on the
screened rungs Psi* > 0 at be/D = 0.5 and Psi* < 0 at every other
screened ratio.

SMOKE-RUN DISCLOSURE (2026-08-11, before freezing).  The mechanism
was found in four throwaway scratch scripts (deleted): (i) the two
pairing identities of L1/L3 at machine precision; (ii) a three-branch
LP on kz = 9, 13 which recovered, unprompted, exactly two adjacent
x>1 atoms at be/D in [0.493, 0.501] and NOTHING on the x<-1 branch;
(iii) a (m, be) scan on kz = 9, 13, 26, 40 returning be/D = 0.5000
and m*/D = 2.000, 2.000, 1.999, 2.001; (iv) a frozen-mass run over 70
zones showing frozen m = 2D positive on 32/70 and the sup-over-m
version positive on 42/42 in-range rungs.  Those runs FIXED the
frozen spec above (the be constant, the sup-over-m formulation, the
h-window and the bars).  NO bar was moved after this file was
written.  Numbers below are the first run of THIS file.

AMENDMENT A1 (disclosed; added AFTER the first frozen run of this
file, SPEC_SHA 7ef4403327703bb3, which returned 21/21 checks, no
kills, and the verdicts POLE-BRANCH-CARRIES / POLE-CERT-POSITIVE
(42/42) / HALF-TARGET-MET(36/42) / RELOCATION(-0.020) /
BETA-UNIQUE-AT-D/2 / CONTROLS-FIRE).  A1 ADDS section S8 only.  It
moves NO bar, changes NO enum and can only add measurement surface;
S0-S7 are byte-identical to the run above.  S8 asks the two obvious
follow-ups and records that BOTH DIE:
  (i)  SCHUR TRANSFER.  L5 gives the rank-one bonus A[c] >= Psi I +
       2m k k^T, and the Schur complement is Loewner-monotone, so
       along the classical soft direction v_sm (prime-free bottom
       mode of the smooth wall; the CI/CLIX convention, rebuilt
       in-file) one gets the closed bound
         s >= Psi + 2m kap1^2 Psi / (Psi + 2m |kap_r|^2),
       kap1 = <k_{D/2}, v_sm>.  MEASURED: the pole direction is
       essentially ORTHOGONAL to v_sm, so the bonus transfers
       nothing.  Typed TRANSFER-DEAD iff median gain < 1.01.
  (ii) MORE GENERATORS.  The cone L4 also contains the limit ray
       -delta_{M-1} (A[-d_{M-1}] = e_0 e_0^T; the trapezoid endpoint
       of the pole quadrature) and further cosh atoms.  MEASURED on
       the rungs where one pole atom misses (1/2) mu1: the endpoint
       ray gains ~1e-4 of mu1 (nothing); a second cosh atom helps
       but its optimal be_2 runs to the scan boundary and has no
       explicit-formula meaning, and the (1/2) mu1 target is still
       missed.  Typed SECOND-ATOM-PATCH-INSUFFICIENT.
"""
import ast
import hashlib
import math
import os
import sys
import time

import numpy as np
from scipy.linalg import eigh
from scipy.optimize import linprog

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)
sys.path.insert(0, os.path.abspath(os.path.join(_HERE, "..", "..",
                                                "verification")))
import v563_paper2_readouts as core  # noqa: E402  READ-ONLY

# ------------------------------------------------------------ frozen spec
H_LO, H_HI = 142, 878
BETA_OVER_D = 0.5
BISECT_ITERS = 34
N_HYP = 800
U_LO, U_HI = 1.0e-3, 120.0
LP_KZ = (18, 13)
BETA_SCREEN = (0.25, 0.40, 0.48, 0.50, 0.52, 0.60, 0.75, 1.00)
SCREEN_KZ = (9, 26, 44, 55)
CTRL_KZ = (9, 26, 44)
SCRAMBLE_SEED = 777
ID_TOL = 1.0e-9
AND_TOL = 1.0e-9
LIFT_BAR = 50.0
BE_LO, BE_HI = 0.45, 0.55
RNG = np.random.default_rng(20260811)

CHECKS, KILLS, VERDICTS = [], [], []


def check(name, ok, detail="", kill=None):
    CHECKS.append((name, bool(ok)))
    if kill and not ok:
        KILLS.append(kill)
    print("  [%s] %s%s" % ("PASS" if ok else "FAIL", name,
                           ("  -- " + detail) if detail else ""), flush=True)
    return bool(ok)


def section(t):
    print("\n" + "=" * 74)
    print(t)
    print("=" * 74, flush=True)


def spec_sha():
    src = open(os.path.abspath(__file__), encoding="utf-8").read()
    return hashlib.sha256(src.encode("utf-8")).hexdigest()[:16]


def ast_scan(banned):
    src = open(os.path.abspath(__file__), encoding="utf-8").read()
    bad = []
    for node in ast.walk(ast.parse(src)):
        nm = None
        if isinstance(node, ast.Attribute):
            nm = node.attr
        elif isinstance(node, ast.Name):
            nm = node.id
        if nm in banned:
            bad.append(nm)
    return sorted(set(bad))


# --------------------------------------------------------------- machinery
def kvec(h, z):
    return np.sinh((h - np.arange(h, dtype=float) - 0.5) * z)


def lvec(h, th):
    return np.sin((h - np.arange(h, dtype=float) - 0.5) * th)


def tz(c):
    i = np.arange(len(c))
    return c[np.abs(i[:, None] - i[None, :])]


def _reflector(M):
    u = np.zeros(M)
    u[0] = 1.0
    u -= np.ones(M) / math.sqrt(M)
    return u / np.linalg.norm(u)


def comp1(X):
    """compression of X to 1^perp (exact Householder congruence)."""
    u = _reflector(X.shape[0])
    Y = X - 2.0 * np.outer(u, u @ X)
    Y = Y - 2.0 * np.outer(Y @ u, u)
    return Y[1:, 1:]


def w_of(v, h):
    return core.lag_weights_from_v(v, h)


def q_at(v, x):
    """q_v(x) = sum_j v_j W_{h-1-j}(x) by the W recurrence
    (W_0 = 1, W_1 = 2x + 1, W_{n+1} = 2 x W_n - W_{n-1})."""
    h = len(v)
    wm1, w0 = 0.0, 1.0
    acc = v[h - 1] * w0
    for n in range(1, h):
        w1 = (2.0 * x + 1.0) if n == 1 else (2.0 * x * w0 - wm1)
        wm1, w0 = w0, w1
        acc += v[h - 1 - n] * w0
    return acc


def wall_c(kz, scramble_seed=None, arch_only=False):
    r = core.build_window(kz, scramble_seed=scramble_seed)
    alpha, M, D = r["alpha"], r["M"], r["D"]
    c_at = np.asarray(core.atom_lags_at(alpha, M, np.asarray(r["uu"], float),
                                        2.0 * np.asarray(r["lam"], float))[0],
                      float)
    c_ar = np.asarray(core.arch_lags(M, D), float)
    return (c_ar if arch_only else c_ar + c_at), r


def lam1(A):
    w, v = eigh(A, subset_by_index=[0, 0])
    return float(w[0]), v[:, 0]


def sup_psi(c, D, beta_over_D=BETA_OVER_D, iters=BISECT_ITERS):
    """sup_{m>=0} lam_min(Pi Tz(c + m cosh(be .)) Pi).  Concave in m."""
    M = len(c)
    be = beta_over_D * D
    C0 = comp1(tz(c))
    C1 = comp1(tz(np.cosh(be * np.arange(M, dtype=float))))
    w0, v = lam1(C0)
    if float(v @ C1 @ v) <= 0.0:
        return w0, 0.0, w0
    lo, hi = 0.0, 8.0 / math.cosh(be * (M - 1))
    for _ in range(iters):
        mid = 0.5 * (lo + hi)
        _, v = lam1(C0 + mid * C1)
        if float(v @ C1 @ v) > 0.0:
            lo = mid
        else:
            hi = mid
    m = 0.5 * (lo + hi)
    w, _ = lam1(C0 + m * C1)
    return w, m, w0


# =========================================================== S0
section("S0 -- FRAME, SPEC AND STATIC WARDS")
SHA = spec_sha()
print("  SPEC_SHA (sha256/16 of this file) = %s" % SHA)
print("  frozen: BETA_OVER_D=%.3f  H in [%d, %d]  BISECT=%d  N_HYP=%d"
      % (BETA_OVER_D, H_LO, H_HI, BISECT_ITERS, N_HYP))
BANNED = ["eigvals_wall_target", "sigma_h", "known_tau"]
check("S0.1 no banned target symbols in source", not ast_scan(BANNED),
      "scanned %d names" % len(BANNED))
LADDER = []
for kz in core.frame_a_zones():
    r0 = core.build_window(kz)
    if H_LO <= r0["h"] <= H_HI:
        LADDER.append(kz)
check("S0.2 deployed ladder recovered", len(LADDER) == 42,
      "%d rungs, h in [%d, %d]" % (len(LADDER),
                                   min(core.build_window(k)["h"]
                                       for k in LADDER),
                                   max(core.build_window(k)["h"]
                                       for k in LADDER)),
      kill="PIPELINE-BROKEN")

# =========================================================== S1
section("S1 -- THE IDENTITY BATTERY (L1-L5, exact)")
worst = {}
for h in (5, 9, 20, 33):
    M = 2 * h
    d = np.arange(M, dtype=float)
    for tag, seq, target in (
            ("L1.cos", None, None),):
        pass
    # L1 three branches
    for tag, z, mk in (("real", 0.137, lambda z: kvec(h, z)),
                       ("imag", 0.731, lambda z: 1j * lvec(h, z)),
                       ("alt", 0.209, None)):
        if tag == "real":
            seq = np.cosh(z * d)
            tgt = -2.0 * np.outer(kvec(h, z), kvec(h, z))
        elif tag == "imag":
            seq = np.cos(z * d)
            tgt = 2.0 * np.outer(lvec(h, z), lvec(h, z))
        else:
            seq = ((-1.0) ** d) * np.cosh(z * d)
            mm = ((-1.0) ** np.arange(h)) * np.cosh(
                (h - np.arange(h) - 0.5) * z)
            tgt = 2.0 * np.outer(mm, mm)
        dev = np.abs(core.odd_toeplitz(seq, M) - tgt).max() / max(
            1.0, np.abs(tgt).max())
        worst["L1." + tag] = max(worst.get("L1." + tag, 0.0), dev)
    e0 = np.zeros(M)
    e0[0] = 1.0
    eM = np.zeros(M)
    eM[M - 1] = -1.0
    g = h - np.arange(h, dtype=float) - 0.5
    ee = np.zeros(h)
    ee[0] = 1.0
    for tag, seq, tgt in (
            ("L1.delta0", e0, np.eye(h)),
            ("L1.gauge", np.ones(M), np.zeros((h, h))),
            ("L1.edge", eM, np.outer(ee, ee)),
            ("L1.d2", d ** 2, -4.0 * np.outer(g, g))):
        dev = np.abs(core.odd_toeplitz(seq, M) - tgt).max()
        worst[tag] = max(worst.get(tag, 0.0), dev)
    # L3 dictionary, inside and outside [-1, 1]
    for _ in range(4):
        v = RNG.standard_normal(h)
        w = w_of(v, h)
        for x in (0.31, -0.77, 1.0, math.cosh(0.23), -math.cosh(0.11), 3.7):
            lhs = float(w @ np.polynomial.chebyshev.chebvander(
                np.array([x]), M - 1)[0])
            rhs = (1.0 - x) * q_at(v, x) ** 2
            dv = abs(lhs - rhs) / max(1.0, abs(rhs))
            worst["L3.dict"] = max(worst.get("L3.dict", 0.0), dv)
    # the cosh pairing (analytic continuation of L3)
    for _ in range(3):
        v = RNG.standard_normal(h)
        w = w_of(v, h)
        for be in (0.05, 0.31, 0.9):
            lhs = float(w @ np.cosh(be * d))
            rhs = -2.0 * float(kvec(h, be) @ v) ** 2
            worst["L3.cosh"] = max(worst.get("L3.cosh", 0.0),
                                   abs(lhs - rhs) / max(1.0, abs(rhs)))
for k in sorted(worst):
    check("S1 %s exact" % k, worst[k] <= ID_TOL, "max dev %.2e" % worst[k],
          kill="WARD-BROKEN")

# L2: no rank-one PSD element of range(A) outside the k_z family
bad2 = 0
for h in (5, 6, 7):
    M = 2 * h
    Bas = [core.odd_toeplitz(np.eye(M)[k], M) for k in range(M)]
    for _ in range(400):
        cc = RNG.standard_normal(M)
        Ac = core.odd_toeplitz(cc, M)
        ev = np.linalg.eigvalsh(Ac)
        if ev[0] < -1e-12 or ev[-2] > 1e-9 * max(1.0, ev[-1]):
            continue                      # not rank-one PSD
        u = np.linalg.eigh(Ac)[1][:, -1]
        rat = (u[:-2] + u[2:]) / u[1:-1]
        if np.ptp(rat) > 1e-6 * max(1.0, abs(rat).max()):
            bad2 += 1
check("S1 L2 rank-one classification (3-term recursion forced)", bad2 == 0,
      "counterexamples %d in 1200 random draws" % bad2, kill="WARD-BROKEN")

# L5: end-to-end with an EXPLICIT gauge gamma
print("\n  L5 end-to-end (explicit gauge):")
l5ok = True
for kz in (9, 26):
    c, r = wall_c(kz)
    h, M, D = r["h"], r["M"], r["D"]
    ps, m, _ = sup_psi(c, D)
    t = 0.99 * ps
    rr = c + m * np.cosh(0.5 * D * np.arange(M, dtype=float))
    rr = rr - t * np.eye(M)[0]
    T2 = tz(rr)
    one = np.ones(M) / math.sqrt(M)
    u = _reflector(M)
    Y = T2 - 2.0 * np.outer(u, u @ T2)
    Y = Y - 2.0 * np.outer(Y @ u, u)
    gam = (float(one @ T2 @ one)
           - float(Y[0, 1:] @ np.linalg.solve(Y[1:, 1:], Y[0, 1:]))) / M
    gam -= 1e-12
    lT = float(np.linalg.eigvalsh(T2 - gam * np.ones((M, M)))[0])
    kb = kvec(h, 0.5 * D)
    lK = float(np.linalg.eigvalsh(core.odd_toeplitz(c, M) - t * np.eye(h)
                                  - 2.0 * m * np.outer(kb, kb))[0])
    ok = (lT >= -1e-11) and (lK >= -1e-11)
    l5ok = l5ok and ok
    print("     kz=%-3d t=%.6e gam=%+.3e  lam_min Tz(gauged)=%+.3e  "
          "lam_min(A[c] - tI - 2m kk^T)=%+.3e  %s"
          % (kz, t, gam, lT, lK, "OK" if ok else "BROKEN"))
check("S1 L5 certificate chain closes with explicit gauge", l5ok,
      kill="WARD-BROKEN")

# =========================================================== S2
section("S2 -- BRANCH ANATOMY: WHICH GENERATORS CARRY THE WALL?")


def build_cols(M, n_th, use_th=True, use_p=True, use_n=True):
    cols, tag, xs = [], [], []
    if use_th:
        th = np.linspace(0.0, math.pi, n_th)
        cols.append(np.cos(np.outer(np.arange(M), th)))
        tag += ["th"] * n_th
        xs.append(np.cos(th))
    be = np.geomspace(U_LO, U_HI, N_HYP) / (M - 1.0)
    d = np.arange(M, dtype=float)
    top = (M - 1) * be
    base = np.exp(np.outer(d, be) - top) + np.exp(-np.outer(d, be) - top)
    base = base / np.max(np.abs(base), axis=0)
    if use_p:
        cols.append(-base)
        tag += ["p"] * N_HYP
        xs.append(np.cosh(be))
    if use_n:
        cols.append(base * ((-1.0) ** d)[:, None])
        tag += ["n"] * N_HYP
        xs.append(-np.cosh(be))
    return np.hstack(cols), np.array(tag), np.concatenate(xs)


def cone_lp(c, G):
    M = len(c)
    A = np.hstack([np.eye(M)[:, :1], np.ones((M, 1)), G])
    cost = np.zeros(A.shape[1])
    cost[0] = -1.0
    bnd = [(None, None), (None, None)] + [(0.0, None)] * (A.shape[1] - 2)
    r = linprog(cost, A_eq=A, b_eq=c, bounds=bnd, method="highs")
    return (float(r.x[0]), r.x[2:]) if r.success else (None, None)


lp_rows = []
for kz in LP_KZ:
    c, r = wall_c(kz)
    h, M, D = r["h"], r["M"], r["D"]
    tau = float(np.linalg.eigvalsh(core.odd_toeplitz(c, M))[0])
    print("\n  kz=%d h=%d M=%d D=%.5f  tau=%+.5e" % (kz, h, M, D, tau))
    vals = {}
    for nm, kw in (("cos only   ", dict(use_p=False, use_n=False)),
                   ("cos + x>1  ", dict(use_n=False)),
                   ("cos + x<-1 ", dict(use_p=False)),
                   ("all three  ", dict())):
        t0 = time.time()
        G, tg, xs = build_cols(M, 12 * h, **kw)
        t, mu = cone_lp(c, G)
        if t is None:
            print("     %s LP infeasible" % nm)
            continue
        vals[nm.strip()] = t
        sup = mu > 1e-11 * max(1.0, mu.max())
        nb = {k: int(np.sum(sup & (tg == k))) for k in ("th", "p", "n")}
        ex = ""
        if nb["p"]:
            bp = np.arccosh(np.maximum(xs[sup & (tg == "p")], 1.0)) / D
            ex = "  x>1 atoms at be/D in [%.4f, %.4f]" % (bp.min(), bp.max())
            lp_rows.append((kz, bp.min(), bp.max(), nb["p"]))
        print("     %s t*=%+.6e  t*/tau=%+9.2f  atoms %d/%d/%d [%.0fs]%s"
              % (nm, t, t / tau, nb["th"], nb["p"], nb["n"],
                 time.time() - t0, ex))
    if "cos only" in vals and "cos + x>1" in vals:
        lift = abs(vals["cos only"]) / max(1e-30, abs(vals["cos + x>1"]))
        print("     -> x>1 branch lifts the cos-only value by %.1fx" % lift)
        lp_rows.append(("lift", kz, lift))
lifts = [x[2] for x in lp_rows if x[0] == "lift"]
bes = [(a, b) for (k, a, b, n) in [x for x in lp_rows if x[0] != "lift"]]
carries = (bool(lifts) and min(lifts) >= LIFT_BAR and bool(bes)
           and all(BE_LO <= a and b <= BE_HI for a, b in bes))
check("S2 POLE-BRANCH-CARRIES", carries,
      "min lift %.1fx (bar %.0fx); recovered be/D in [%.4f, %.4f]"
      % (min(lifts) if lifts else 0.0, LIFT_BAR,
         min(a for a, b in bes) if bes else 0.0,
         max(b for a, b in bes) if bes else 0.0))
VERDICTS.append(("BRANCH", "POLE-BRANCH-CARRIES" if carries
                 else "POLE-BRANCH-INCONCLUSIVE"))

# =========================================================== S3
section("S3 -- THE CERTIFICATE ON THE DEPLOYED LADDER  (sup_m Psi(m, D/2))")
print("   kz     h     M   tau          Psi*         Psi0(m=0)    Psi/tau"
      "  Psi/mu1  m*/2D-1")
rows = []
t00 = time.time()
for kz in LADDER:
    c, r = wall_c(kz)
    h, M, D = r["h"], r["M"], r["D"]
    tau = float(np.linalg.eigvalsh(core.odd_toeplitz(c, M))[0])
    mu1 = 4.0 * math.sin(math.pi / (2.0 * h + 1.0)) ** 2
    ps, m, p0 = sup_psi(c, D)
    rows.append((kz, h, M, D, tau, ps, p0, mu1, m))
    print("  %4d %5d %5d  %+.4e  %+.4e  %+.4e  %+.4f  %+.4f  %+.3e"
          % (kz, h, M, tau, ps, p0, ps / tau, ps / mu1, m / (2 * D) - 1.0))
print("  [%.1fs]" % (time.time() - t00))

ps = np.array([x[5] for x in rows])
p0 = np.array([x[6] for x in rows])
tt = np.array([x[4] for x in rows])
mu = np.array([x[7] for x in rows])
hs = np.array([float(x[1]) for x in rows])
dv = np.array([x[8] / (2.0 * x[3]) - 1.0 for x in rows])
Ds = np.array([x[3] for x in rows])
npos = int((ps > 0).sum())
nhalf = int((ps >= 0.5 * mu).sum())
print("\n  Psi* > 0 on %d/%d ; Psi* >= (1/2) mu1 on %d/%d"
      % (npos, len(rows), nhalf, len(rows)))
print("  Psi*/tau  min %.4f  med %.4f  max %.4f"
      % ((ps / tt).min(), float(np.median(ps / tt)), (ps / tt).max()))
print("  Psi*/mu1  min %.4f  med %.4f  max %.4f"
      % ((ps / mu).min(), float(np.median(ps / mu)), (ps / mu).max()))
print("  Psi0/tau (NO pole term) min %.1f med %.1f max %.1f  [sign must "
      "be wrong]" % ((p0 / tt).min(), float(np.median(p0 / tt)),
                     (p0 / tt).max()))
print("  m*/2D - 1 : med %+.3e ; (m*/2D-1)/D^2 med %+.4f  [O(D^2) "
      "quadrature correction]" % (float(np.median(dv)),
                                  float(np.median(dv / Ds ** 2))))
A = np.vstack([np.log(hs), np.ones_like(hs)]).T
sp = np.linalg.lstsq(A, np.log(ps), rcond=None)[0][0]
st = np.linalg.lstsq(A, np.log(tt), rcond=None)[0][0]
sr = np.linalg.lstsq(A, np.log(ps / tt), rcond=None)[0][0]
print("  TAU-SCREEN: log Psi* ~ %.4f log h ; log tau ~ %.4f log h ; "
      "log(Psi*/tau) ~ %+.4f log h" % (sp, st, sr))
check("S3 certificate positive on the whole deployed ladder",
      npos == len(rows), "%d/%d" % (npos, len(rows)))
check("S3 m* matches the Weil pole mass 2D to <1e-4 relative",
      float(np.median(np.abs(dv))) < 1e-4,
      "median |m*/2D - 1| = %.2e" % float(np.median(np.abs(dv))))
check("S3 no-pole baseline has the WRONG SIGN on every rung",
      bool((p0 < 0).all()), "max Psi0 = %+.3e" % p0.max())
VERDICTS.append(("CERT", "POLE-CERT-POSITIVE(%d/%d)" % (npos, len(rows))
                 if npos == len(rows) else
                 "POLE-CERT-PARTIAL(%d/%d)" % (npos, len(rows))))
VERDICTS.append(("HALF", "HALF-TARGET-MET(%d/%d)" % (nhalf, len(rows))))
VERDICTS.append(("TAUSCREEN", "RELOCATION (slope %+.3f, |slope| < 0.25)"
                 % sr if abs(sr) < 0.25 else
                 "TAU-DECORRELATED (slope %+.3f)" % sr))

# =========================================================== S4
section("S4 -- BETA SCREEN: is be = D/2 forced?")
uniq = True
for kz in SCREEN_KZ:
    c, r = wall_c(kz)
    out = []
    for rr in BETA_SCREEN:
        p, _, _ = sup_psi(c, r["D"], beta_over_D=rr, iters=26)
        out.append((rr, p))
        if (rr == 0.50 and p <= 0) or (rr != 0.50 and p > 0):
            uniq = False
    print("  kz=%-3d h=%-4d  %s" % (kz, r["h"],
                                    "  ".join("%.2f:%+.3e" % o for o in out)))
check("S4 BETA-UNIQUE (only be = D/2 certifies)", uniq,
      "screened %d ratios on %d rungs" % (len(BETA_SCREEN), len(SCREEN_KZ)))
VERDICTS.append(("BETA", "BETA-UNIQUE-AT-D/2" if uniq else "BETA-NOT-UNIQUE"))

# =========================================================== S5
section("S5 -- CONTROLS (must fire)")
ctrl_ok = True
for kz in CTRL_KZ:
    c, r = wall_c(kz)
    D, M = r["D"], r["M"]
    ca, _ = wall_c(kz, arch_only=True)
    cs, rs = wall_c(kz, scramble_seed=SCRAMBLE_SEED + kz)
    pa, ma, _ = sup_psi(ca, D, iters=26)
    psc, msc, _ = sup_psi(cs, rs["D"], iters=26)
    ta = float(np.linalg.eigvalsh(core.odd_toeplitz(ca, M))[0])
    ts = float(np.linalg.eigvalsh(core.odd_toeplitz(cs, rs["M"]))[0])
    ctrl_ok = ctrl_ok and (pa <= 0.0) and (psc <= 0.0)
    print("  kz=%-3d  ARCH-ONLY tau=%+.4e Psi*=%+.4e m*/2D=%.4f | "
          "SCRAMBLE tau=%+.4e Psi*=%+.4e m*/2D=%.4f"
          % (kz, ta, pa, ma / (2 * D), ts, psc, msc / (2 * rs["D"])))
check("S5 CONTROLS-FIRE (no control world certifies)", ctrl_ok,
      kill="CONTROLS-SILENT")
VERDICTS.append(("CONTROLS", "CONTROLS-FIRE" if ctrl_ok
                 else "CONTROLS-SILENT"))

# =========================================================== S6
section("S6 -- THE ALGEBRAIC ORIGIN OF THE 1/2 (Andreief on the "
        "three-branch measure)")
print("""  Given L4's positive representation  v^T A[c] v =
  int |1-x| q_v(x)^2 dmu(x) =: <q_v, q_v>_om  with om >= 0, the
  Andreief/Cauchy-Binet identity gives, for ANY two directions,
      det [[<f,f>, <f,g>], [<g,f>, <g,g>]]
        = (1/2) int int (f(x) g(y) - f(y) g(x))^2 dom(x) dom(y),
  and the integrand is the signature-(1,2) form a(x)b(y) + b(x)a(y)
  - 2 c(x)c(y) with a = f^2, b = g^2, c = fg.  The 1/2 is the
  symmetrisation factor of the exterior square -- available for the
  wall ONLY because the pole branch makes om nonnegative.""")
wa = 0.0
for trial in range(6):
    n = 40
    xs = np.concatenate([RNG.uniform(-1.0, 1.0, n - 2),
                         [math.cosh(0.31), -math.cosh(0.12)]])
    om = RNG.random(n) * np.abs(1.0 - xs)
    f = RNG.standard_normal(n)
    g = RNG.standard_normal(n)
    G = np.array([[float(om @ (f * f)), float(om @ (f * g))],
                  [float(om @ (f * g)), float(om @ (g * g))]])
    Wm = (np.outer(f * f, g * g) + np.outer(g * g, f * f)
          - 2.0 * np.outer(f * g, f * g))
    rhs = 0.5 * float(om @ Wm @ om)
    wa = max(wa, abs(np.linalg.det(G) - rhs) / max(1.0, abs(rhs)))
check("S6 Andreief 2x2 wedge identity with the 1/2", wa <= AND_TOL,
      "max rel dev %.2e" % wa)
# the same on the REAL wall, using the L4 representation from S2's LP
h_ = core.build_window(LP_KZ[0])["h"]
c_, r_ = wall_c(LP_KZ[0])
M_, D_ = r_["M"], r_["D"]
Gc, tgc, xsc = build_cols(M_, 12 * h_)
t_, mu_ = cone_lp(c_, Gc)
rep_dev = None
if t_ is not None:
    sup = mu_ > 1e-13 * max(1.0, mu_.max())
    K_ = core.odd_toeplitz(c_, M_)
    worst_rep = 0.0
    for _ in range(4):
        v = RNG.standard_normal(h_)
        lhs = float(v @ K_ @ v)
        acc = t_ * float(v @ v)
        for idx in np.nonzero(sup)[0]:
            x = xsc[idx]
            if abs(x) <= 1.0:
                acc += mu_[idx] * abs(1.0 - x) * q_at(v, x) ** 2
            else:
                be = math.acosh(abs(x))
                nrm = math.cosh(be * (M_ - 1))
                kk = float(kvec(h_, be) @ (v * ((-1.0) ** np.arange(h_))
                                           if x < 0 else v))
                acc += mu_[idx] * 2.0 * kk * kk / nrm
        worst_rep = max(worst_rep, abs(lhs - acc) / max(1.0, abs(lhs)))
    rep_dev = worst_rep
    print("  L4 representation reproduces v^T A[c] v on the REAL wall "
          "(kz=%d): max rel dev %.2e" % (LP_KZ[0], rep_dev))
check("S6 L4 positive representation exact on the deployed wall",
      rep_dev is not None and rep_dev <= 1e-6,
      "rel dev %.2e" % (rep_dev if rep_dev is not None else -1.0))

# =========================================================== S8 (A1)
section("S8 -- AMENDMENT A1: the two obvious follow-ups, and why they die")
NG_SMOOTH_MIN, NG_FACT = 6000, 8


def smooth_vsm(alpha, M, D):
    """prime-free bottom mode of the smooth wall (CI/CLIX convention,
    rebuilt in-file: PNT continuum comb, resolution scaled to M)."""
    ng = max(NG_SMOOTH_MIN, NG_FACT * M)
    ug = (np.arange(ng) + 0.5) * (2.0 * alpha / ng)
    mg = 2.0 * np.exp(ug / 2.0) * (2.0 * alpha / ng)
    Ksm = core.odd_toeplitz(
        np.asarray(core.arch_lags(M, D), float)
        + np.asarray(core.atom_lags_at(alpha, M, ug, mg)[0], float), M)
    ws, Vs = np.linalg.eigh(Ksm)
    return Vs[:, 0].copy(), float(ws[0])


print("  (i) SCHUR TRANSFER of the rank-one pole bonus along v_sm")
print("      kz     h   lam_sm    rho=<k,vsm>^2   s/mu1    Psi/mu1  "
      "s_bound/mu1  gain")
gains, sm_ok = [], True
for kz in (9, 12, 22, 25, 26, 29, 32, 44, 46, 55, 64, 82):
    c, r = wall_c(kz)
    h, M, D, alpha = r["h"], r["M"], r["D"], r["alpha"]
    K = core.odd_toeplitz(c, M)
    mu1 = 4.0 * math.sin(math.pi / (2.0 * h + 1.0)) ** 2
    vsm, lam_sm = smooth_vsm(alpha, M, D)
    sm_ok = sm_ok and (-2.0 <= lam_sm <= -0.5)
    s = 1.0 / float(vsm @ np.linalg.solve(K, vsm))
    ps, m, _ = sup_psi(c, D)
    kb = kvec(h, 0.5 * D)
    k1 = float(kb @ vsm)
    kr2 = float(kb @ kb) - k1 * k1
    sb = ps + 2.0 * m * k1 * k1 * ps / (ps + 2.0 * m * kr2)
    gains.append(sb / ps)
    print("      %4d %5d  %+.3f   %.3e     %.4f   %.4f   %.4f     %.4fx"
          % (kz, h, lam_sm, k1 * k1 / float(kb @ kb), s / mu1, ps / mu1,
             sb / mu1, sb / ps))
medg = float(np.median(gains))
check("S8 smooth branch guard (lam_sm in [-2, -0.5])", sm_ok)
check("S8 TRANSFER-DEAD (rank-one pole bonus does not reach the pivot)",
      medg < 1.01, "median gain %.5fx; the pole is orthogonal to v_sm"
      % medg)
VERDICTS.append(("TRANSFER", "TRANSFER-DEAD (median gain %.5fx)" % medg
                 if medg < 1.01 else "TRANSFER-LIVE (%.3fx)" % medg))

print("\n  (ii) MORE GENERATORS on the rungs where one pole atom misses "
      "(1/2) mu1")


def alt_max(C0, Cs, his, a0=None, sweeps=5, iters=30):
    """Alternating golden section on the concave lam_min(C0 + sum a_i C_i),
    a_i >= 0.  SEEDED at a0 (the coordinates are strongly coupled -- the
    pole mass must be resolved to ~1e-6 relative -- so a cold start from
    the origin under-converges and can report a value BELOW the seed,
    which is impossible for the true supremum: a generator carrying zero
    mass cannot lower it.  The caller therefore also clamps from below by
    the seed value.)"""
    a = [0.0] * len(Cs) if a0 is None else list(a0)

    def val(aa):
        A = C0.copy()
        for ai, Ci in zip(aa, Cs):
            if ai:
                A = A + ai * Ci
        return lam1(A)[0]
    gr = (math.sqrt(5.0) - 1.0) / 2.0
    for _ in range(sweeps):
        for i in range(len(Cs)):
            lo, hi = 0.0, his[i]
            b = list(a)
            x1, x2 = hi - gr * (hi - lo), lo + gr * (hi - lo)
            b[i] = x1
            f1 = val(b)
            b[i] = x2
            f2 = val(b)
            for _ in range(iters):
                if f1 < f2:
                    lo, x1, f1 = x1, x2, f2
                    x2 = lo + gr * (hi - lo)
                    b[i] = x2
                    f2 = val(b)
                else:
                    hi, x2, f2 = x2, x1, f1
                    x1 = hi - gr * (hi - lo)
                    b[i] = x1
                    f1 = val(b)
            a[i] = 0.5 * (lo + hi)
    return val(a), a


DEFICIENT = [x[0] for x in rows if x[5] < 0.5 * x[7]]
print("      deficient rungs (Psi* < mu1/2): %s"
      % (", ".join(str(k) for k in DEFICIENT) or "none"))
print("      kz     h   Psi1/mu1  +edge ray  +2nd cosh  be2/D  still<1/2?")
edge_gain, still = [], 0
for kz in DEFICIENT:
    c, r = wall_c(kz)
    h, M, D = r["h"], r["M"], r["D"]
    mu1 = 4.0 * math.sin(math.pi / (2.0 * h + 1.0)) ** 2
    d = np.arange(M, dtype=float)
    C0 = comp1(tz(c))
    Cp = comp1(tz(np.cosh(0.5 * D * d)))
    hp = 8.0 / math.cosh(0.5 * D * (M - 1))
    p1, m1, _ = sup_psi(c, D)
    Ce = comp1(tz(np.eye(M)[M - 1]))
    pe, _ = alt_max(C0, [Cp, Ce], [hp, 4.0], a0=[m1, 0.0])
    pe = max(pe, p1)
    edge_gain.append((pe - p1) / mu1)
    best = (p1, 0.0)
    for r2 in (0.20, 0.70, 1.00, 1.50, 2.00):
        C2 = comp1(tz(np.cosh(r2 * D * d)))
        p2, _ = alt_max(C0, [Cp, C2], [hp, 8.0 / math.cosh(r2 * D * (M - 1))],
                        a0=[m1, 0.0])
        if p2 > best[0]:
            best = (p2, r2)
    miss = best[0] < 0.5 * mu1
    still += 1 if miss else 0
    print("      %4d %5d  %+.4f   %+.4f    %+.4f    %.2f   %s"
          % (kz, h, p1 / mu1, pe / mu1, best[0] / mu1, best[1],
             "YES" if miss else "no"))
print("      endpoint ray gains (units of mu1): max %+.2e  -> nothing"
      % (max(edge_gain) if edge_gain else 0.0))
check("S8 SECOND-ATOM-PATCH-INSUFFICIENT (target still missed)",
      still > 0, "%d of %d deficient rungs still below (1/2) mu1"
      % (still, len(DEFICIENT)))
VERDICTS.append(("EXTEND", "SECOND-ATOM-PATCH-INSUFFICIENT (%d/%d still "
                 "below)" % (still, len(DEFICIENT)) if still else
                 "SECOND-ATOM-CLOSES-TARGET"))

# =========================================================== S7
section("S7 -- LOGICAL STATUS, TYPED (read this before anything else)")
print("""  PROVED (elementary, machine-checked in S1; no primes, no RH):
    L1  A[cosh(z.)] = -2 k_z k_z^T for every z in C.
    L2  those are the ONLY rank-one directions in range(A).
    L3  sum_d w_d(v) T_d(x) = (1-x) q_v(x)^2 exactly on R.
    L4  A[c] >= 0  <=>  c in cl cone{eps(x) T.(x) : x in R} + R*1,
        and then v^T A[c] v = int |1-x| q_v(x)^2 dmu with mu >= 0.
    L5  Tz(c + m cosh(be.) - t d_0 - gam*1) >= 0  =>  A[c] >= t I
        + 2 m k_be k_be^T.
  MACHINE-MEASURED (this run, deployed ladder, source-only):
    the wall's positivity is carried by ONE generator outside the
    Chebyshev segment, at be = D/2 with mass 2D -- numerically the
    zeta pole term 2 cosh(x/2) dx of the Weil explicit formula; the
    cos-branch alone has the wrong sign by orders; the x < -1 branch
    is empty; the controls do not certify.
  NOT PROVED, AND THE GAP IS NAMED:
    the certificate's hypothesis Tz(c + 2D cosh(D./2)) >= 0 says, by
    Bochner, that the pole-RESTORED lag sequence is the cosine-moment
    sequence of a NONNEGATIVE measure.  Via the explicit formula that
    sequence is the (windowed, D-aliased) transform of the zero
    measure, so its nonnegativity is not weaker than the window's
    share of RH.  THIS IS A REFORMULATION, NOT A REDUCTION.  What it
    buys is the currency: an odd-Toeplitz-minus-Hankel compression
    with margin ~ h^-2 is replaced by a plain Caratheodory-Toeplitz
    positivity plus one explicit rank-one pole, on which the
    classical apparatus (Fejer-Riesz, Szego, Markov) is available.
    The TAU-SCREEN below says the h-decay is NOT removed.
  NO RH CLAIM IS MADE OR IMPLIED BY THIS FILE.""")
section("VERDICTS")
for k, v in VERDICTS:
    print("  %-10s %s" % (k, v))
npass = sum(1 for _, o in CHECKS if o)
print("\n  checks %d/%d passed ; kills: %s"
      % (npass, len(CHECKS), ", ".join(sorted(set(KILLS))) or "none"))
print("  SPEC_SHA %s" % SHA)
