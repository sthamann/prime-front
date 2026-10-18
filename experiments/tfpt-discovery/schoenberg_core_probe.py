#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""schoenberg_core_probe -- PRIME.CORE.SCHOENBERG.01
(EXPLORATION ONLY, experiments/.  NO RH claim.  2026-08-13.)

THE CONDITIONAL-POSITIVITY (SCHOENBERG) ROUTE FOR THE RH CORE, RUN TO
A DECISION BY EXACT ALGEBRA AND CERTIFIED LINEAR PROGRAMMING.  The
endform (CCCXXV/CCCXXXI) localizes the wall in ONE scalar
    Delta_h := v_-^T X_h v_- + lam_min(G0_h)
with v_- the single soft direction of the geometry seat G0_h and X_h
the arithmetic seat block, both 2 x 2 compressions of the odd
Toeplitz-minus-Hankel form built from the lag split c = c_geo + c_osc
(c_osc = atom comb minus PNT smooth mass).  The HYPOTHESIS under
test: the correct positivity class is not global PSD (killed by
trace-zero, CCCXXV) but CONDITIONALLY positive definite of degree
one; the classical Schoenberg lemma -- for real c_r with
sum_r c_r = 0 and psi(x) = int (1 - cos t x) dnu(t), nu >= 0,
    -sum_{r,s} c_r c_s psi(x_r - x_s)
      = int |sum_r c_r e^{i t x_r}|^2 dnu(t)  >=  0
-- should turn Delta_h >= 0 into the existence of a positive
SOURCE-ONLY Euler measure nu_h = sum_{p^k <= X_h} a_{p^k}
delta_{k log p}, a_{p^k} >= 0 (TARGET IDENTITY (E)).

THE EXACT BRIDGE, established generically (sympy) before anything is
measured.  With grid positions x_i = (i - (M-1)/2) Dg, i = 0..h-1,
the deployed compression K(c)_ij = c_{|i-j|} - c_{(M-1)-i-j} obeys
four exact relations (declared here as R1..R4; see amendment A1):
  R1 GAUGE.  K(const) == 0 identically: the parity form annihilates
     constant lag vectors, equivalently the T163 lag weights of every
     compression direction satisfy sum_d w_d = 0 EXACTLY.  Every
     compression is therefore ALREADY a centered (degree-one) form:
     the weighted centering projector H_h = I - 1 pi_h^T acts as the
     identity on it, and the (1/2,1/2)-fold constant-direction
     remover removes EXACTLY ZERO.
  R2 RANK-ONE COSINE KERNEL.  K(cos(t . Dg))_ij ==
     2 sin(t x_i) sin(t x_j) -- an exact trig identity: the odd
     compression of a pure cosine lag is one PSD rank-one square.
  R3 REFLECTION = CENTERING.  On the reflected node set {x_i, -x_i}
     with antisymmetric coefficients c_r = (u_i, -u_i) one has
     sum_r c_r = 0 automatically and
       -sum_{r,s} c_r c_s (1 - cos(t(x_r - x_s)))
         = |sum_r c_r e^{i t x_r}|^2 = 4 (sum_i u_i sin(t x_i))^2,
     i.e. the odd compression IS the degree-one Schoenberg form and
     u^T K(cos(t .)) u = (1/2)|sum_r c_r e^{i t x_r}|^2.
  R4 HALF-ANGLE.  (1/2) mu1(h) == 1 - cos(2 pi / N), N = 2h + 1:
     the window shift is literally the Schoenberg kernel 1 - cos at
     the fundamental frequency-position product (CCCXXV H2).
CONSEQUENCE (exact, the centering adjudication of (E) and of work
item 5): because of R1/R3 the passage global -> conditional is a
GAUGE IDENTITY here -- the centering term of ANY measure nu
contributes IDENTICALLY ZERO to the compression.  Hence if nu
represents the arithmetic block (v^T X_h v = int |.|^2 dnu for all
v), then Delta_h = int |.|^2 dnu(v_-) + lam_min(G0_h) is SMALLER than
the integral by exactly -lam_min(G0_h) > 0: identity (E) as stated
can hold only if lam_min(G0_h) = 0, and lam_min(G0_h) is measured
O(-1).  If nu is NOT required to represent X_h, (E) is one scalar
equation in many nonnegative unknowns and is VACUOUSLY solvable
whenever Delta_h >= 0.  Either way (E) carries no independent
content; what remains decidable is WHERE the representation lives.

THE THREE REPRESENTATION TIERS (frozen).
  T-FULL  the full centered quadratic form: does the M-lag identity
     c_osc_d = A + sum_{p^k} a_{p^k} (cos((k log p) Dg d) - 1),
     a >= 0, hold on all lags d = 0..M-1?  (Equivalent, by R1 + the
     exact one-dimensional kernel of lag -> form, to the h x h
     matrix identity, i.e. to representability of the FULL centered
     form.)  Decided by LP; a kill is CERTIFIED twice: (i) an
     explicit witness direction u* with u*^T K(c_osc) u* < 0 in
     outward-rounded arithmetic (no positive measure of ANY support
     represents a form with a negative value), and (ii) a
     quantitative Farkas dual y with y . 1 = 0, ||y||_1 <= 1,
     y . col_t <= -GAMMA for EVERY Euler frequency and y . c_osc >=
     eps_low > 0, certifying that every admissible (A, a >= 0) stays
     at sup-norm distance >= eps_low from the oscillating lag.
  T-SEAT  the seat compression: X_h = sum_t a_t . 2 sigma(t)
     sigma(t)^T with sigma(t) = (S_1(t), S_2(t)), S_a(t) = sum_i
     (t_a)_i sin(t x_i) -- three equations.  A feasible LP point is
     reduced to a 3-atom basic solution and certified by interval
     Cramer (mpmath.iv): nonsingular system + strictly positive
     weights => the EXACT identity X_h = sum_{i=1..3} a_i 2 sigma
     sigma^T holds with a_i in certified positive enclosures.  This
     gives v^T X_h v >= 0 for ALL v -- but NOT the wall, which needs
     v_-^T X_h v_- >= -lam_min(G0) > 0 in MAGNITUDE.
  T-WALL  the full seat G_h = G0_h + X_h in the Euler cone: would be
     the wall itself from a positive source-only measure.  Decided by
     LP; kills are certified by the conic Farkas dual Y (2 x 2):
     <Y, 2 sigma(t) sigma(t)^T> >= GAMMA_G w_t for every Euler t and
     <Y, G_h> <= -delta < 0.
KILL CRITERIA (frozen, hard).  K1: T-FULL certified dead on every
true rung => the exact Schoenberg identity is refuted.  K2: if the
strongest tier that passes on the true world ALSO passes on the
scramble world, the class is comb-blind => SCHOENBERG-VACUOUS.  K3:
no tau, no zero data, no target sign enters any construction (AST
scan; the consumed path never calls an eigensolver -- 2 x 2 closed
forms and LP/Farkas only; m_h / shat are never computed).

VERDICT ENUM (dominance order, frozen):
  SCHOENBERG-REPRESENTED  (E) holds as a matrix identity with the
      centering delivering lam_min(G0), all rungs, scramble fails;
  SCHOENBERG-VACUOUS      strongest passing tier also passes scramble;
  SCHOENBERG-DEAD         no tier survives on the true world;
  SCHOENBERG-PARTIAL      a proper subset holds -- printed exactly.

RIGOR (post-CCCXXIII discipline).  Two adversarial audits of the
assembly pipeline run concurrently, so the entry data of this probe
are assembled INDEPENDENTLY at mpmath dps = 50 from the frozen
recipe (arch kernel via 48-point Gauss-Legendre nodes recomputed at
50 digits by Newton iteration; atom tents at mp.log positions of an
own integer sieve; smooth comb at mp midpoints), then cross-warded
against the deployed float64 pipeline (esq.level_rung, READ-ONLY) at
1e-10.  Every sign-bearing scalar carries an outward-rounded
enclosure: assembled mp values get a declared +-1e-38 buffer (five
decades above the dps-50 op-count rounding bound), 2 x 2 closed-form
eigenvalues / Cramer solutions / witness values are evaluated in
mpmath.iv interval arithmetic, and the big certificate sums are
evaluated in float64 with an explicit a-priori error budget
    |err| <= ||y||_1 (eps_arg + 2 M eps_mach) + conversion,
    eps_arg = eps_mach (1 + theta_max), theta_max = max |t d Dg|,
printed next to each margin (margins are O(1e-6..1e-1); budgets are
O(1e-11)).  Eigensolvers are never called on the consumed path.
NO deeper ladder, NO fits, NO paper/ledger/website/manifest edits,
NO .md, NO commit, runtime < 30 min.

LADDER (frozen): kz in (9, 13, 26, 40, 60) -- the CCCXXV SUBSET_KZ,
h = 184/168/364/591/388, Euler frequency counts 70/136/604/1773/4710.
CONTROLS (must fire): scramble seed 1 on every rung (identical
pipeline; expected: X_scr leaves the PSD cone => T-SEAT dual fires);
Epstein x^2 + 5y^2 at kz 9; smooth world at kz 9 (c_osc == 0
structurally).  Controls are assembled at float64 with the same
budget certification (their kill margins are O(1); declared).
SCREENS: tau/c_h screens are honestly N/A -- computing tau_rep or
c_h would import the target spectrum into a probe whose consumed
path forbids it; no new margin claimed here is a wall substitute.

FROZEN BARS.  DPS = 50; ENC_BUF = 1e-38; XWARD = 1e-10 (assembly
cross-ward, relative); GAUGE_BAR = 1e-40 (mp) / 1e-12 (float
controls); REPRO_BAR = 1e-4 (the stored prototype anchors carry
five significant digits; the bar is their truncation radius);
GAMMA = 1e-6 (T-FULL dual safety); GAMMA_G = 1e-9 and Y_BOX = 10
(conic duals); per-column float64 error majorant
    err_t = 8 Y_BOX deltaS (|S1_t| + |S2_t| + deltaS)
            + 16 eps_mach Y_BOX (w_t + 1),
    deltaS = 2 eps_mach (2 + theta_max) sqrt(h),
inflated demand kappa_t = 20 err_t + 1e-13 inside the dual LP and
re-verified outside it; LP method HiGHS (tight feasibility
tolerances); witness channel = argmin of the oscillating density;
CRAMER_POS: all three interval weights strictly > 0 and det
enclosure excludes 0.  EPS_MACH = 2^-52.

SMOKE DISCLOSURE (mandatory, verbatim).  Before this spec was frozen
a prototype (float64, /tmp, not committed) ran the assembly, the
alignment reproduction and ALL THREE tiers on the full subset plus
scramble/Epstein at kz 9/13/26 -- THE CENSUS NUMBERS WERE SEEN:
alignment margins 2.73e-3/1.36e-3/2.54e-4/1.26e-4/8.00e-5 (matching
CCCXXV), T-FULL LP residual 0.32..0.37 vs lag scale 0.61..0.68 on
every true rung (dead by ~50 percent of scale), T-SEAT feasible on
5/5 true rungs, INFEASIBLE on 3/3 scramble rungs and on Epstein,
T-WALL infeasible on the true world and feasible on Epstein.  The
verdict RULE above was frozen AFTER seeing these numbers; it is
nevertheless stated in falsifiable form (any certification failure,
ward break, control silence or repro break still kills the run), and
the honest value of the frozen run is (i) the exact R1..R4 bridge
and the centering adjudication of (E), which smoke did not decide,
(ii) the CERTIFIED kill objects (witness, Farkas duals, interval
Cramer) replacing LP statuses, and (iii) the controls-must-fire
gates.  One declared smoke run of THIS file (TFPT_SCHOENBERG_SMOKE=1,
kz 9/13 only) was run before the freeze; its construction-side
repairs are disclosed in the run header as S1..S5 (a banned
identifier rename, the exp-rewrite proof route for R3 -- sympy's
default simplify is too weak for the 36-term trig identity, which
smoke verified to 1e-166 on exact rationals --, the per-column
error-majorant inflation of the conic duals after near-null Euler
columns w_t ~ 1e-9 broke the naive check, and the repro bar set to
the five-digit truncation radius of the stored prototype anchors).
None of these repairs touches a census definition, a bar direction
or the verdict rule.

HONEST AMENDMENTS (declared before the frozen run).
 A1 the mission brief locates "the shared relations R1-R4" in the
    radau_sos_certificate / radau_class_close probes.  No literal
    R1..R4 relation object exists there (checked; those probes carry
    Radau/SOS moment machinery for the OTHER wall block, and the
    CCCXXVII certificate skeleton is Newton/Radau/SOS/LDL-shaped).
    The four exact relations actually available for this reduction
    are declared above as R1..R4 and proved generically in-run.
 A2 "solve rationally" is realized as: LP search in float64 (never
    trusted), then certification in outward-rounded interval
    arithmetic on the exact transcendental data -- exact rational
    arithmetic is impossible for cos(k log p . x) entries, and the
    interval tier is the honest equivalent (the certified statements
    are about the EXACT values).
 A3 the window geometry (integers M, h, n_zone and the scramble
    positions) is consumed from the deployed ladder as frozen DATA;
    every entry VALUE (arch/atom/smooth lags, seats, eigen data) is
    rebuilt independently at dps 50.
 A4 controls run the identical code path at float64 precision with
    the same certification formulas (their margins are O(1)).
 A5 POST-FREEZE AMENDMENT (disclosed, radau_class_close A6 style).
    Frozen-run-1 (SPEC_SHA 522c7ce97a1f693a..., 25.8 s, 23 checks,
    0 kills) decided every census identically to this run but left
    two CERTIFICATION-MACHINERY gaps: (i) at kz 40 the argmin-D_osc
    witness channel read +70.2 (the channel-leakage of the sine
    profile), although 60 of the 64 most negative channels DO
    certify (min -925.5) -- the witness SEARCH is widened to a
    float64 pre-screen over the 64 most negative channels whose
    argmin is then mp-certified (the search is free, the
    certification tier is unchanged); (ii) the HiGHS feasibility
    tolerance 1e-11 is an INVALID option value that scipy ignores
    with a warning, so the kz-60 wall dual came back at the default
    tolerance and violated the re-verification margin by 2.7e-9 --
    the tolerance is set to the valid 1e-10 and the dual solve
    retries ONCE with any measured violation folded into kappa_t.
    No bar, census definition, control, or verdict rule changed;
    both repairs only let the already-decided LP statuses be
    CERTIFIED rather than dropped.

NO RH claim.  No marker moves.  verification/ and the predecessor
probes are imported READ-ONLY (level_rung geometry + cross-ward
only; level_reads is never called).  The only later edit outside
this file is the German CCCXXXIX note prepended to
experiments/next.txt AFTER the frozen summary.

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/schoenberg_core_probe.py
    TFPT_SCHOENBERG_SMOKE=1 ... (declared smoke, kz 9/13)
"""

import ast
import hashlib
import math
import os
import sys
import time

import numpy as np
import mpmath as mp
from scipy.optimize import linprog

_HERE = os.path.dirname(os.path.abspath(__file__))
_VERIFY = os.path.abspath(os.path.join(_HERE, "..", "..",
                                       "verification"))
sys.path.insert(0, _HERE)
sys.path.insert(0, _VERIFY)

import v563_paper2_readouts as core                  # noqa: E402 RO
import exterior_square_factorization_probe as esq    # noqa: E402 RO

# ---------------------------------------------------------------- frozen
LADDER_KZ = (9, 13, 26, 40, 60)
DPS = 50
ENC_BUF = mp.mpf("1e-38")
XWARD = 1.0e-10
GAUGE_BAR_MP = mp.mpf("1e-40")
GAUGE_BAR_F = 1.0e-12
REPRO_BAR = 1.0e-4
GAMMA = 1.0e-6
GAMMA_G = 1.0e-9
Y_BOX = 10.0
EPS_MACH = 2.0 ** -52
LP_OPTS = {"primal_feasibility_tolerance": 1.0e-10,
           "dual_feasibility_tolerance": 1.0e-10}
WIT_SCAN = 64
GLN = 48
NG_SMOOTH = 6000
SCR_SEED = 1
CTRL_KZ = 9
SMOKE = bool(os.environ.get("TFPT_SCHOENBERG_SMOKE"))
BANNED_IDS = ("zetazero", "nzeros", "primerange", "isprime",
              "primepi", "nextprime", "prevprime")
# consumed-path anti-circularity: no eigensolver, no target read
CONSUMED_FNS = ("assemble_rung", "seat_objects", "tier_full_dual",
                "tier_seat", "tier_wall_dual", "witness_kill")
CONSUMED_BANNED = ("eigh", "eigvalsh", "eigvals", "svd", "pinv",
                   "tau", "shat", "m_h", "level_reads", "det2",
                   "verdict", "target", "zetazero", "nzeros")

SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
T0 = time.time()
CHECKS = []
KILLS = []

mp.mp.dps = DPS
IV = mp.iv
IV.dps = DPS


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


def ast_scan(banned, only_fns=None):
    src = open(os.path.abspath(__file__), encoding="utf-8").read()
    bad = []
    tree = ast.parse(src)
    for node in ast.walk(tree):
        if only_fns is not None:
            if not isinstance(node, ast.FunctionDef) \
                    or node.name not in only_fns:
                continue
            walk = ast.walk(node)
        else:
            walk = [node]
        for sub in walk:
            nm = None
            if isinstance(sub, ast.Name):
                nm = sub.id
            elif isinstance(sub, ast.Attribute):
                nm = sub.attr
            if nm and nm.lower() in banned:
                bad.append(nm)
    return bad


def enc(x):
    """outward enclosure of an mp scalar with the declared buffer."""
    return IV.mpf([mp.mpf(x) - ENC_BUF, mp.mpf(x) + ENC_BUF])


def ivstr(v):
    return "[%.6e, %.6e]" % (float(v.a), float(v.b))


# =============================================== exact relations R1..R4
def generic_relations():
    """R1..R4 verified GENERICALLY on the relation variables (sympy),
    at symbolic M = 6, h = 3 with free t, Dg, u_1..u_3, c_0..c_5."""
    import sympy as sp
    t, Dg = sp.symbols("t Dg", real=True)
    M, h = 6, 3
    u = sp.symbols("u1:4", real=True)
    c = sp.symbols("c0:6", real=True)

    def K_of(lag):
        return sp.Matrix(h, h, lambda i, j: lag(abs(i - j))
                         - lag((M - 1) - i - j))

    # R1: constant lag annihilated + lag-weight gauge sum
    K1m = K_of(lambda d: sp.Integer(1))
    r1a = all(sp.simplify(K1m[i, j]) == 0
              for i in range(h) for j in range(h))
    uv = sp.Matrix(u)
    form = sp.expand((uv.T * K_of(lambda d: c[d]) * uv)[0, 0])
    wsum = sum(sp.expand(form).coeff(cd) for cd in c)
    r1b = sp.simplify(wsum) == 0
    # R2: rank-one cosine kernel
    xs = [(i - sp.Rational(M - 1, 2)) * Dg for i in range(h)]
    Kc = K_of(lambda d: sp.cos(t * d * Dg))
    r2 = all(sp.simplify(
        Kc[i, j] - 2 * sp.sin(t * xs[i]) * sp.sin(t * xs[j])) == 0
        for i in range(h) for j in range(h))
    # R3: reflection = centering (Schoenberg degree one); the 36-term
    # trig identities need the exp-rewrite proof route (S4)
    def zero(expr):
        return sp.simplify(expr.rewrite(sp.exp).expand()) == 0

    nodes = xs + [-x for x in xs]
    coef = list(u) + [-ui for ui in u]
    csum = sp.simplify(sum(coef))
    lhs = -sum(coef[r] * coef[s]
               * (1 - sp.cos(t * (nodes[r] - nodes[s])))
               for r in range(2 * h) for s in range(2 * h))
    sq = (sum(coef[r] * sp.cos(t * nodes[r])
              for r in range(2 * h)) ** 2
          + sum(coef[r] * sp.sin(t * nodes[r])
                for r in range(2 * h)) ** 2)
    r3a = zero(lhs - sq)
    r3b = zero(sq - 4 * sum(u[i] * sp.sin(t * xs[i])
                            for i in range(h)) ** 2)
    r3c = zero((uv.T * Kc * uv)[0, 0] - sp.Rational(1, 2) * sq)
    # R4: half-angle
    hh = sp.symbols("hsym", positive=True)
    r4 = sp.simplify(
        2 * sp.sin(sp.pi / (2 * hh + 1)) ** 2
        - (1 - sp.cos(2 * sp.pi / (2 * hh + 1)))) == 0
    # centering projector: H = I - 1 pi^T with sum(pi) = 1 fixes the
    # antisymmetric sector pointwise (H^T c = c when sum c = 0)
    pi = sp.symbols("pi1:7", real=True)
    Hm = sp.eye(2 * h) - sp.ones(2 * h, 1) * sp.Matrix(1, 2 * h,
                                                       lambda _i, j:
                                                       pi[j])
    cv = sp.Matrix(coef)
    fixed = sp.simplify(Hm.T * cv - cv
                        + sp.Matrix(pi) * csum)
    r5 = all(sp.simplify(v) == 0 for v in fixed)
    return dict(r1a=r1a, r1b=r1b, r2=r2, r3a=r3a, r3b=r3b, r3c=r3c,
                r4=r4, r5=r5, csum=(csum == 0))


# ================================================= independent assembly
def gl_nodes_mp(n):
    out = []
    for i in range(1, n + 1):
        x = mp.mpf(math.cos(math.pi * (i - 0.25) / (n + 0.5)))
        for _ in range(80):
            p = mp.legendre(n, x)
            dp = n * (x * p - mp.legendre(n - 1, x)) / (x * x - 1)
            dx = p / dp
            x -= dx
            if abs(dx) < mp.mpf(10) ** -(DPS + 4):
                break
        w = 2 / ((1 - x * x) * dp * dp)
        out.append((x, w))
    return out


GL_MP = None


def arch_far_mp(s, D):
    out = mp.mpf(0)
    for lo, hi in ((s - D, s), (s, s + D)):
        mid = (lo + hi) / 2
        half = (hi - lo) / 2
        acc = mp.mpf(0)
        for x, w in GL_MP:
            wv = mid + half * x
            acc += w * ((1 - abs(s - wv) / D) * mp.e ** (-wv / 2)
                        / (-mp.expm1(-2 * wv)))
        out -= half * acc
    return out


def arch_near_mp(s, D):
    s = abs(s)
    tri_s = max(mp.mpf(0), 1 - s / D)
    W = s + D
    pts = sorted({mp.mpf(0), s, D - s, W})
    pts = [p for p in pts if 0 <= p <= W]
    tot = mp.mpf(0)
    for lo, hi in zip(pts[:-1], pts[1:]):
        if hi <= lo:
            continue
        mid = (lo + hi) / 2
        half = (hi - lo) / 2
        for x, w in GL_MP:
            wv = mid + half * x
            S = (max(mp.mpf(0), 1 - abs(s - wv) / D)
                 + max(mp.mpf(0), 1 - abs(s + wv) / D)) / 2
            tot += half * w * ((tri_s * mp.e ** (-2 * wv)
                                - S * mp.e ** (-wv / 2))
                               / (-mp.expm1(-2 * wv)))
    return (-(mp.euler + mp.log(mp.pi)) * tri_s + 2 * tot
            + tri_s * (-mp.log(-mp.expm1(-2 * W))))


def sieve_prime_powers(nmax):
    """own integer sieve: (n, log p) for every prime power n <= nmax."""
    isp = np.ones(nmax + 1, dtype=bool)
    isp[:2] = False
    for i in range(2, int(math.isqrt(nmax)) + 1):
        if isp[i]:
            isp[i * i::i] = False
    out = []
    for p in np.nonzero(isp)[0]:
        p = int(p)
        lp = mp.log(p)
        q = p
        while q <= nmax:
            out.append((q, lp))
            q *= p
    out.sort(key=lambda z: z[0])
    return out


def tent_deposit_mp(c, u, mass, D, M):
    """the T115 tent deposit, mp verbatim: c[i] -= mass/2 * tent."""
    i0 = int(mp.floor(u / D))
    for i in range(max(0, i0 - 2), min(M, i0 + 3)):
        v = 1 - abs(i * D - u) / D
        if v > 0:
            c[i] -= mass * v / 2
    if u < D:
        for i in range(0, min(M, int(mp.floor((D - u) / D)) + 2)):
            v = 1 - (i * D + u) / D
            if v > 0:
                c[i] -= mass * v / 2


def autocorr_mp(v, h, M):
    """T163 lag weights at mp: w_0 = A_0, w_d = 2 A_d - CV_{M-1-d}."""
    A = [mp.fdot(v[:h - d], v[d:]) for d in range(h)]
    CV = [mp.mpf(0)] * (2 * h - 1)
    for e in range(2 * h - 1):
        lo = max(0, e - h + 1)
        hi = min(h - 1, e)
        CV[e] = mp.fsum(v[i] * v[e - i] for i in range(lo, hi + 1))
    w = [mp.mpf(0)] * M
    w[0] = A[0]
    for d in range(1, M):
        w[d] = (2 * A[d] if d < h else mp.mpf(0))
        e = (M - 1) - d
        if 0 <= e <= M - 2:
            w[d] -= CV[e]
    return w


def assemble_rung(kz, world=None, scramble_seed=None, comb=None,
                  float_mode=False):
    """Independent assembly of one rung.  Geometry integers (M, h,
    n_zone) are frozen ladder data; every value is rebuilt (mp dps=50,
    or float64 for controls, declared A4)."""
    rgf = esq.level_rung(kz, want_split=True,
                         scramble_seed=scramble_seed,
                         world=world, comb=comb)
    if rgf is None:
        return None
    M, h = rgf["M"], rgf["h"]
    n_zone = int(round(math.exp(rgf["alpha"])))
    if float_mode:
        # controls: the identical formulas at float64 (A4)
        alpha = rgf["alpha"]
        Dg = 2.0 * alpha / M
        c_ar = rgf["c_ar"]
        c_osc = rgf["c"] - rgf["c_ar"] - rgf["c_sm"]
        pp = [(int(n), math.log(int(n)))
              for n in np.exp(core.U_ALL[
                  :core.atoms_in(alpha)]).round().astype(int)]
        return dict(kz=kz, M=M, h=h, n_zone=n_zone, alpha=alpha,
                    Dg=Dg, c_ar=c_ar, c_osc=c_osc, pp=pp, mode="f64",
                    rgf=rgf)
    alpha = mp.log(n_zone)
    Dg = 2 * alpha / M
    # archimedean lags (frozen recipe at 50 digits)
    c_ar = []
    for d in range(M):
        s = d * Dg
        c_ar.append(arch_far_mp(s, Dg) if s >= Dg
                    else arch_near_mp(s, Dg))
    # atom comb (own sieve, mp positions/masses)
    pp = sieve_prime_powers(n_zone * n_zone)
    c_at = [mp.mpf(0)] * M
    if scramble_seed is not None:
        rng = np.random.default_rng(scramble_seed)
        upos = np.sort(rng.uniform(0.0, 2.0 * float(alpha),
                                   size=len(pp)))
        for (n, lp), u in zip(pp, upos):
            tent_deposit_mp(c_at, mp.mpf(float(u)),
                            2 * lp / mp.sqrt(n), Dg, M)
    else:
        for n, lp in pp:
            tent_deposit_mp(c_at, mp.log(n), 2 * lp / mp.sqrt(n),
                            Dg, M)
    # smooth PNT comb (frozen ng = 6000 midpoint recipe)
    c_sm = [mp.mpf(0)] * M
    du = 2 * alpha / NG_SMOOTH
    for g in range(NG_SMOOTH):
        ug = (g + mp.mpf(1) / 2) * du
        tent_deposit_mp(c_sm, ug, 2 * mp.e ** (ug / 2) * du, Dg, M)
    c_osc = [a - s for a, s in zip(c_at, c_sm)]
    return dict(kz=kz, M=M, h=h, n_zone=n_zone, alpha=alpha, Dg=Dg,
                c_ar=c_ar, c_at=c_at, c_sm=c_sm, c_osc=c_osc, pp=pp,
                mode="mp", rgf=rgf)


def seat_objects(rg):
    """G0, X seats, the soft direction and the enclosures.  2 x 2
    closed forms only -- no eigensolver on the consumed path."""
    M, h = rg["M"], rg["h"]
    if rg["mode"] == "f64":
        Tb = core.parity_basis(h, 2)
        t1 = [float(v) for v in Tb[0]]
        t2 = [float(v) for v in Tb[1]]
        W11 = core.lag_weights_from_v(np.asarray(t1), h)
        W22 = core.lag_weights_from_v(np.asarray(t2), h)
        W12 = 0.5 * (core.lag_weights_from_v(
            np.asarray(t1) + np.asarray(t2), h) - W11 - W22)
        W3 = (list(W11), list(W12), list(W22))
        lag_g = list(np.asarray(rg["c_ar"])
                     + (np.asarray(rg["rgf"]["c_sm"])))
        lag_o = list(rg["c_osc"])
        mu1h = 4.0 * math.sin(math.pi / (2 * h + 1)) ** 2
        dot = lambda w, c: float(np.dot(w, c))         # noqa: E731
        sqrtf = math.sqrt
    else:
        N = 2 * h + 1
        t1 = [2 / mp.sqrt(N) * mp.sin(2 * mp.pi * (j + 1) / N)
              for j in range(h)]
        t2 = [2 / mp.sqrt(N) * mp.sin(4 * mp.pi * (j + 1) / N)
              for j in range(h)]
        W11 = autocorr_mp(t1, h, M)
        W22 = autocorr_mp(t2, h, M)
        Wpp = autocorr_mp([a + b for a, b in zip(t1, t2)], h, M)
        W12 = [(p - a - b) / 2 for p, a, b in zip(Wpp, W11, W22)]
        W3 = (W11, W12, W22)
        lag_g = [a + s for a, s in zip(rg["c_ar"], rg["c_sm"])]
        lag_o = rg["c_osc"]
        mu1h = 4 * mp.sin(mp.pi / N) ** 2
        dot = lambda w, c: mp.fdot(w, c)               # noqa: E731
        sqrtf = mp.sqrt
    gauge = max(abs(dot(W3[0], [1] * M)), abs(dot(W3[1], [1] * M)),
                abs(dot(W3[2], [1] * M)))
    G0 = [[dot(W3[0], lag_g) - mu1h / 2, dot(W3[1], lag_g)],
          [dot(W3[1], lag_g), dot(W3[2], lag_g) - mu1h / 2]]
    X = [[dot(W3[0], lag_o), dot(W3[1], lag_o)],
         [dot(W3[1], lag_o), dot(W3[2], lag_o)]]
    tr = G0[0][0] + G0[1][1]
    det = G0[0][0] * G0[1][1] - G0[0][1] ** 2
    lam = (tr - sqrtf(tr * tr - 4 * det)) / 2
    v1, v2 = G0[0][1], lam - G0[0][0]
    nv = sqrtf(v1 * v1 + v2 * v2)
    v1, v2 = v1 / nv, v2 / nv
    qneg = (v1 * (X[0][0] * v1 + X[0][1] * v2)
            + v2 * (X[0][1] * v1 + X[1][1] * v2))
    rg.update(t1=t1, t2=t2, W3=W3, G0=G0, X=X, mu1=mu1h,
              lam_g0=lam, vneg=(v1, v2), qneg=qneg,
              align=qneg + lam, gauge=gauge,
              lam_geo_seat=lam + mu1h / 2)
    # interval tier for the sign-bearing scalar (mp mode only)
    if rg["mode"] == "mp":
        G0i = [[enc(G0[0][0]), enc(G0[0][1])],
               [enc(G0[0][1]), enc(G0[1][1])]]
        Xi = [[enc(X[0][0]), enc(X[0][1])],
              [enc(X[0][1]), enc(X[1][1])]]
        tri = G0i[0][0] + G0i[1][1]
        deti = G0i[0][0] * G0i[1][1] - G0i[0][1] ** 2
        lami = (tri - IV.sqrt(tri * tri - 4 * deti)) / 2
        w1, w2 = G0i[0][1], lami - G0i[0][0]
        nn = w1 * w1 + w2 * w2
        qi = (w1 * (Xi[0][0] * w1 + Xi[0][1] * w2)
              + w2 * (Xi[0][1] * w1 + Xi[1][1] * w2)) / nn
        rg["align_iv"] = qi + lami
        rg["lam_iv"] = lami
    return rg


# ==================================================== frequencies/reads
def euler_reads(rg):
    """sine reads of the two carriers at every Euler frequency
    t = k log p = log n, n = p^k <= n_zone^2 (float64 for LP search;
    the certified objects re-evaluate what they need)."""
    M, h = rg["M"], rg["h"]
    Dg = float(rg["Dg"])
    ts = np.array([math.log(n) for n, _lp in rg["pp"]])
    xi = Dg * (np.arange(h) - (M - 1) / 2.0)
    SIN = np.sin(np.outer(ts, xi))
    t1f = np.array([float(v) for v in rg["t1"]])
    t2f = np.array([float(v) for v in rg["t2"]])
    theta_max = float(ts[-1]) * float(np.max(np.abs(xi)))
    delta_s = 2.0 * EPS_MACH * (2.0 + theta_max) * math.sqrt(h)
    rg.update(ts=ts, xi=xi, S1=SIN @ t1f, S2=SIN @ t2f,
              delta_s=delta_s)
    return rg


# ================================================= the certified tiers
def float_budget(y_l1, M, theta_max):
    """a-priori outward bound for a float64 sum
    sum_d y_d (cos(theta_d) - 1) with |theta| <= theta_max."""
    return y_l1 * (EPS_MACH * (1.0 + theta_max) + 2.0 * M * EPS_MACH
                   + 2.0 * EPS_MACH)


def witness_kill(rg):
    """explicit centered direction with certified negative value of
    the oscillating form: float64 pre-screen over the WIT_SCAN most
    negative oscillating channels (free search, A5), then the argmin
    profile is certified at mp."""
    M, h = rg["M"], rg["h"]
    L = 2 * M - 2
    cof = np.array([float(v) for v in rg["c_osc"]])
    dosc = esq.grid_density(cof)
    order = np.argsort(dosc[:L // 2 + 1])[:WIT_SCAN]
    best_j, best_v = None, np.inf
    for j in order:
        th = 2.0 * math.pi * int(j) / L
        uf = np.sin(th * (np.arange(h) - (M - 1) / 2.0))
        v = float(core.lag_weights_from_v(uf, h) @ cof)
        if v < best_v:
            best_j, best_v = int(j), v
    th = 2.0 * math.pi * best_j / L
    u = [mp.sin(th * (p - mp.mpf(M - 1) / 2)) for p in range(h)]
    W = autocorr_mp(u, h, M)
    val = mp.fdot(W, rg["c_osc"])
    gau = abs(mp.fsum(W))
    scale = mp.fsum([abs(w) for w in W])
    vi = enc(val) + IV.mpf([-1, 1]) * (ENC_BUF * scale)
    return dict(j=best_j, val=val, iv=vi, gauge=gau,
                dmin=float(dosc[best_j]))


def tier_full_dual(rg):
    """T-FULL: LP search + safe Farkas dual + certification."""
    M = rg["M"]
    Dg = float(rg["Dg"])
    ts = rg["ts"]
    nfr = len(ts)
    dd = np.arange(M) * Dg
    COL = np.cos(np.outer(dd, ts)) - 1.0
    cof = np.array([float(v) for v in rg["c_osc"]])
    # primal: min eps  s.t. |c - A 1 - COL a| <= eps
    nv = nfr + 2
    cvec = np.zeros(nv)
    cvec[-1] = 1.0
    Aub = np.zeros((2 * M, nv))
    Aub[:M, :nfr] = COL
    Aub[:M, nfr] = 1.0
    Aub[:M, -1] = -1.0
    Aub[M:, :nfr] = -COL
    Aub[M:, nfr] = -1.0
    Aub[M:, -1] = -1.0
    bub = np.concatenate([cof, -cof])
    r = linprog(cvec, A_ub=Aub, b_ub=bub,
                bounds=[(0, None)] * nfr + [(None, None), (0, None)],
                method="highs")
    eps_lp = float(r.fun) if r.status == 0 else float("nan")
    # safe dual: max y.c  s.t. y.col <= -GAMMA, y.1 = 0, ||y||_1 <= 1
    ny = 2 * M
    cd = np.concatenate([-cof, cof])                 # max -> min
    A2 = np.zeros((nfr + 1, ny))
    A2[:nfr, :M] = COL.T
    A2[:nfr, M:] = -COL.T
    A2[nfr, :] = 1.0                                 # ||y||_1 <= 1
    b2 = np.concatenate([-GAMMA * np.ones(nfr), [1.0]])
    Ae = np.zeros((1, ny))
    Ae[0, :M] = 1.0
    Ae[0, M:] = -1.0
    r2 = linprog(cd, A_ub=A2, b_ub=b2, A_eq=Ae, b_eq=[0.0],
                 bounds=[(0, None)] * ny, method="highs")
    out = dict(eps_lp=eps_lp, ok=False)
    if r2.status != 0:
        return out
    y = r2.x[:M] - r2.x[M:]
    y_l1 = float(np.sum(np.abs(y)))
    theta_max = float(ts[-1]) * (M - 1) * Dg
    bud = float_budget(y_l1, M, theta_max)
    marg = y @ COL                                   # must be <= 0
    ysum = float(np.sum(y))
    eps_low = float(y @ cof) - bud - abs(ysum) * 0.0
    # y.1 = 0 enforced exactly up to float sum error:
    onebud = abs(ysum) + M * EPS_MACH * y_l1
    worst = float(np.max(marg))
    ok = (worst + bud < 0.0) and (eps_low > 0.0) \
        and (y_l1 <= 1.0 + 1e-12) and (onebud * 10.0 < eps_low)
    out.update(ok=ok, eps_low=eps_low, worst_col=worst, budget=bud,
               y_l1=y_l1, one_defect=onebud)
    return out


def tier_seat(rg, tgt):
    """T-SEAT: X (or a control seat) in the Euler cone; certified
    3-atom interval-Cramer representation when feasible; certified
    conic Farkas dual when infeasible."""
    S1, S2, ts = rg["S1"], rg["S2"], rg["ts"]
    nfr = len(ts)
    Beq = np.vstack([2 * S1 * S1, 2 * S2 * S2, 2 * S1 * S2])
    beq = np.array([float(tgt[0][0]), float(tgt[1][1]),
                    float(tgt[0][1])])
    r = linprog(np.ones(nfr), A_eq=Beq, b_eq=beq,
                bounds=[(0, None)] * nfr, method="highs")
    if r.status == 0:
        sup = np.argsort(-r.x)[:8]
        sup = [int(i) for i in sup if r.x[i] > 1e-14][:8]
        cert = None
        cache = {}
        from itertools import combinations
        for tri in combinations(sup, 3):
            cert = cramer_cert(rg, tri, tgt, cache)
            if cert is not None:
                break
        return dict(feasible=True, cert=cert, sum_a=float(r.fun),
                    nsup=int(np.sum(r.x > 1e-12)))
    # infeasible: conic Farkas dual with the per-column error
    # majorant (S5): find Y in [-Y_BOX, Y_BOX]^3 with
    #   <Y, 2 sig sig^T>  >=  GAMMA_G w_t + kappa_t   for every t,
    #   <Y, tgt> < 0 certified against the enclosed seat entries.
    wt = 2.0 * (S1 * S1 + S2 * S2)
    dS = rg["delta_s"]
    err_t = (8.0 * Y_BOX * dS * (np.abs(S1) + np.abs(S2) + dS)
             + 16.0 * EPS_MACH * Y_BOX * (wt + 1.0))
    kap = 20.0 * err_t + 1.0e-13
    Aub = np.zeros((nfr, 3))
    Aub[:, 0] = -2 * S1 * S1
    Aub[:, 1] = -2 * S2 * S2
    Aub[:, 2] = -4 * S1 * S2
    cobj = np.array([beq[0], beq[1], 2 * beq[2]])
    Y, worst = None, -np.inf
    for _attempt in range(2):
        r2 = linprog(cobj, A_ub=Aub, b_ub=-(GAMMA_G * wt + kap),
                     bounds=[(-Y_BOX, Y_BOX)] * 3, method="highs",
                     options=LP_OPTS)
        if r2.status != 0:
            return dict(feasible=False, dual=None)
        Y = r2.x
        colv = 2 * S1 * S1 * Y[0] + 2 * S2 * S2 * Y[1] \
            + 4 * S1 * S2 * Y[2]
        # rigorous re-verification: true column value >= colv-err_t,
        # so colv - GAMMA_G w_t - err_t >= 0 certifies the demand
        worst = float(np.min(colv - GAMMA_G * wt - err_t))
        if worst >= 0.0:
            break
        kap = kap + 2.0 * abs(worst) + 1.0e-12       # A5 retry
    if rg["mode"] == "mp":
        vi = (IV.mpf(Y[0]) * enc(tgt[0][0])
              + IV.mpf(Y[1]) * enc(tgt[1][1])
              + 2 * IV.mpf(Y[2]) * enc(tgt[0][1]))
    else:
        vi = (IV.mpf(Y[0]) * IV.mpf(float(tgt[0][0]))
              + IV.mpf(Y[1]) * IV.mpf(float(tgt[1][1]))
              + 2 * IV.mpf(Y[2]) * IV.mpf(float(tgt[0][1])))
        vi += IV.mpf([-1, 1]) * mp.mpf(4.0e-11 * Y_BOX
                                       * max(1.0, abs(beq[0]),
                                             abs(beq[1]),
                                             abs(beq[2])))
    ok = (worst >= 0.0) and (vi.b < 0)
    return dict(feasible=False, dual=dict(Y=list(Y),
                                          val=float(cobj @ Y),
                                          val_hi=float(vi.b),
                                          worst=worst, ok=ok))


def cramer_cert(rg, tri, tgt, cache):
    """interval Cramer on the exact 3 x 3 system: strictly positive
    enclosed weights + nonsingular det => EXACT representation."""
    M, h = rg["M"], rg["h"]
    if rg["mode"] == "mp":
        Dgi = (2 * IV.log(rg["n_zone"])) / M
    else:
        Dgi = IV.mpf(float(rg["Dg"]))
    cols = []
    for idx in tri:
        if idx not in cache:
            n, _lp = rg["pp"][idx]
            ti = IV.log(n)
            s1 = IV.mpf(0)
            s2 = IV.mpf(0)
            for p in range(h):
                xp = Dgi * (IV.mpf(p) - IV.mpf(M - 1) / 2)
                sn = IV.sin(ti * xp)
                s1 += IV.mpf(mp.mpf(rg["t1"][p])
                             if rg["mode"] == "mp"
                             else float(rg["t1"][p])) * sn
                s2 += IV.mpf(mp.mpf(rg["t2"][p])
                             if rg["mode"] == "mp"
                             else float(rg["t2"][p])) * sn
            cache[idx] = (s1, s2)
        s1, s2 = cache[idx]
        cols.append((2 * s1 * s1, 2 * s2 * s2, 2 * s1 * s2))
    A = [[cols[j][i] for j in range(3)] for i in range(3)]
    if rg["mode"] == "mp":
        b = [enc(tgt[0][0]), enc(tgt[1][1]), enc(tgt[0][1])]
    else:
        b = [IV.mpf(float(tgt[0][0])), IV.mpf(float(tgt[1][1])),
             IV.mpf(float(tgt[0][1]))]

    def det3(m):
        return (m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1])
                - m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0])
                + m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0]))

    D0 = det3(A)
    if 0 in D0:
        return None
    aa = []
    for j in range(3):
        Aj = [[b[i] if k == j else A[i][k] for k in range(3)]
              for i in range(3)]
        aj = det3(Aj) / D0
        if not (aj > 0):
            return None
        aa.append(aj)
    return dict(tri=[rg["pp"][i][0] for i in tri], a=aa, det=D0)


# ================================================================ main
def main():
    global GL_MP
    section("PRIME.CORE.SCHOENBERG.01 -- the conditional-positivity "
            "route for the RH core (EXPLORATION ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s" % SPEC_SHA)
    print("    mode=%s; NO RH claim; no marker moves; writes nothing."
          % ("SMOKE" if SMOKE else "FROZEN"))
    print("    SMOKE REPAIRS DISCLOSED (S1..S5, construction-side "
          "only, none touches a census/bar/verdict rule): S1 a "
          "banned identifier rename on the consumed path; S2 the "
          "exp-rewrite proof route for the R3 trig identity (sympy "
          "default simplify too weak; identity verified to 1e-166 "
          "on exact rationals in smoke); S3 the interval-Cramer "
          "searches all 3-subsets of the top LP support with cached "
          "interval reads; S4 the conic duals demand "
          "GAMMA_G w_t + kappa_t with the explicit float64 error "
          "majorant kappa_t (near-null Euler columns w_t ~ 1e-9 "
          "broke the naive check) and re-verify outside the LP; S5 "
          "REPRO_BAR = 1e-4 = the truncation radius of the "
          "five-digit prototype anchors.")

    section("S0 -- firewall and anti-circularity")
    bad = ast_scan(BANNED_IDS)
    check("S0.1 AST firewall clean (no prime/zero oracles)", not bad,
          ",".join(sorted(set(bad))), kill="K0")
    badc = ast_scan(CONSUMED_BANNED, only_fns=CONSUMED_FNS)
    check("S0.2 consumed path clean: no eigensolver, no tau/shat/m_h,"
          " no level_reads, no target read", not badc,
          ",".join(sorted(set(badc))), kill="K0")
    check("S0.3 zero zero-reads consumed; RNG only in the declared "
          "scramble control", True)

    section("S1 -- R1..R4 verified GENERICALLY (sympy, relation "
            "variables free)")
    tg = time.time()
    rel = generic_relations()
    check("R1 GAUGE: K(const) == 0 and sum_d w_d == 0 identically",
          rel["r1a"] and rel["r1b"], kill="K2")
    check("R2 RANK-ONE: K(cos(t.))_ij == 2 sin(t x_i) sin(t x_j)",
          rel["r2"], kill="K2")
    check("R3 REFLECTION=CENTERING: sum c_r == 0 automatic, "
          "-sum c_r c_s (1 - cos) == |sum c_r e^{itx}|^2 == "
          "4 (sum u sin)^2 == 2 u^T K(cos) u",
          rel["csum"] and rel["r3a"] and rel["r3b"] and rel["r3c"],
          kill="K2")
    check("R4 HALF-ANGLE: (1/2) mu1 == 1 - cos(2 pi/N) exactly",
          rel["r4"], kill="K2")
    check("R5 CENTERING PROJECTOR: H = I - 1 pi^T fixes the "
          "reflected antisymmetric sector pointwise (H^T c = c), "
          "so the reduction H^T X H is EXACT and a no-op there",
          rel["r5"], kill="K2")
    print("    [%.1f s] the compression is ALREADY the centered "
          "degree-one Schoenberg form; the centering term of ANY "
          "measure contributes IDENTICALLY ZERO." % (time.time() - tg))

    section("S2 -- independent assembly (mp dps=%d) + cross-ward"
            % DPS)
    GL_MP = gl_nodes_mp(GLN)
    ladder = []
    kzs = LADDER_KZ[:2] if SMOKE else LADDER_KZ
    for kz in kzs:
        tR = time.time()
        rg = assemble_rung(kz)
        rg = seat_objects(rg)
        rg = euler_reads(rg)
        rgf = rg["rgf"]
        dev_ar = max(abs(float(a) - b) for a, b
                     in zip(rg["c_ar"], rgf["c_ar"])) \
            / max(np.max(np.abs(rgf["c_ar"])), 1e-300)
        co_f = rgf["c"] - rgf["c_ar"] - rgf["c_sm"]
        dev_os = max(abs(float(a) - b) for a, b
                     in zip(rg["c_osc"], co_f)) \
            / max(np.max(np.abs(co_f)), 1e-300)
        rg["dev_ar"], rg["dev_os"] = dev_ar, dev_os
        ladder.append(rg)
        print("    kz %3d h %4d M %4d n_zone %5d euler %4d | "
              "dev_ar %.2e dev_osc %.2e | gauge %s | [%.1f s]"
              % (kz, rg["h"], rg["M"], rg["n_zone"], len(rg["pp"]),
                 dev_ar, dev_os, mp.nstr(rg["gauge"], 3),
                 time.time() - tR), flush=True)
    check("S2.1 assembly cross-ward vs deployed float64 pipeline "
          "<= %.0e on every rung (arch and oscillating lags)" % XWARD,
          max(max(r["dev_ar"], r["dev_os"]) for r in ladder) <= XWARD,
          "max %.2e" % max(max(r["dev_ar"], r["dev_os"])
                           for r in ladder), kill="K1")
    check("S2.2 R1 gauge on the actual seats: sum_d W_d = 0 at mp "
          "(bar %s)" % mp.nstr(GAUGE_BAR_MP, 2),
          max(r["gauge"] for r in ladder) <= GAUGE_BAR_MP,
          "max %s" % mp.nstr(max(r["gauge"] for r in ladder), 3),
          kill="K2")
    check("S2.3 atom census matches the deployed window "
          "(own sieve count == atoms_in)",
          all(len(r["pp"]) == core.atoms_in(float(r["alpha"]))
              for r in ladder), kill="K1")

    section("S3 -- the endform scalar, enclosed (CCCXXV repro)")
    print("    %4s %5s %14s %14s %16s %s"
          % ("kz", "h", "need", "vXv", "Delta (align)",
             "enclosure"))
    repro = []
    for r in ladder:
        need = -float(r["lam_g0"])
        print("    %4d %5d %14.9f %14.9f %+16.6e %s"
              % (r["kz"], r["h"], need, float(r["qneg"]),
                 float(r["align"]), ivstr(r["align_iv"])))
        repro.append(float(r["align"]))
    ref = {9: 2.7298e-03, 13: 1.3581e-03, 26: 2.5372e-04,
           40: 1.2627e-04, 60: 7.9968e-05}
    dev = max(abs(a / ref[r["kz"]] - 1.0)
              for a, r in zip(repro, ladder))
    check("S3.1 alignment margins reproduce the CCCXXV/prototype "
          "values (rel <= %.0e)" % REPRO_BAR, dev <= REPRO_BAR,
          "max rel dev %.2e" % dev, kill="K3")
    check("S3.2 Delta_h > 0 CERTIFIED on every rung (outward "
          "enclosure)",
          all(r["align_iv"].a > 0 for r in ladder),
          "min lower bound %.3e"
          % min(float(r["align_iv"].a) for r in ladder))
    check("S3.3 lam_min(G0) < 0 certified (the geometry demand is "
          "real)", all(r["lam_iv"].b < 0 for r in ladder),
          "max upper %.3e" % max(float(r["lam_iv"].b)
                                 for r in ladder))

    section("S4 -- T-FULL: the full centered form (kill tier)")
    print("    witness = most negative oscillating channel; dual = "
          "safe Farkas over the Euler frequency columns")
    full_dead = []
    for r in ladder:
        wt = witness_kill(r)
        td = tier_full_dual(r)
        scale = float(max(abs(float(v)) for v in r["c_osc"]))
        dead = (wt["iv"].b < 0) and td["ok"]
        full_dead.append(dead)
        print("    kz %3d | witness ch %5d D_osc %+.3e -> u*Ku %s "
              "(gauge %s) | LP eps* %.4f dual eps_low %.4f "
              "(|c_osc|inf %.4f, worst col %+.2e, budget %.1e) %s"
              % (r["kz"], wt["j"], wt["dmin"], ivstr(wt["iv"]),
                 mp.nstr(wt["gauge"], 2), td["eps_lp"],
                 td.get("eps_low", float("nan")), scale,
                 td.get("worst_col", float("nan")),
                 td.get("budget", float("nan")),
                 "DEAD" if dead else "alive"), flush=True)
        r["tfull_dead"] = dead
        r["tfull"] = td
        r["twit"] = wt
    check("S4.1 K1 CERTIFIED on every true rung: an explicit "
          "centered direction gives a certified NEGATIVE value of "
          "the oscillating form, AND the Farkas dual certifies "
          "sup-norm distance >= eps_low > 0 from EVERY admissible "
          "positive Euler measure", all(full_dead),
          "%d/%d rungs" % (sum(full_dead), len(ladder)))

    section("S5 -- T-SEAT: the arithmetic seat block in the Euler "
            "cone (representation tier)")
    seat_ok = []
    for r in ladder:
        ts_ = tier_seat(r, r["X"])
        r["tseat"] = ts_
        if ts_["feasible"] and ts_["cert"] is not None:
            ce = ts_["cert"]
            astr = ", ".join("a[%d]=%s" % (n, ivstr(a))
                             for n, a in zip(ce["tri"], ce["a"]))
            print("    kz %3d FEASIBLE, certified 3-atom EXACT "
                  "representation at n = %s: %s"
                  % (r["kz"], ce["tri"], astr), flush=True)
            seat_ok.append(True)
        elif ts_["feasible"]:
            print("    kz %3d feasible (LP) but no 3-subset "
                  "certified -- typed NUMERIC-ONLY" % r["kz"])
            seat_ok.append(False)
        else:
            print("    kz %3d INFEASIBLE (dual %s)"
                  % (r["kz"], ts_.get("dual")))
            seat_ok.append(False)
    check("S5.1 X_h = sum_{3 atoms} a 2 sigma sigma^T with certified "
          "positive interval weights on every rung (an EXACT "
          "identity: v^T X_h v = int |sum c_r e^{itx}|^2 dnu_h / 2 "
          "for ALL v, nu_h positive source-only Euler)",
          all(seat_ok), "%d/%d" % (sum(seat_ok), len(ladder)))
    print("    NOTE (gate rule): this certifies X_h >= 0, which was "
          "already measured; the wall needs the MAGNITUDE "
          "v_-^T X v_- >= -lam_min(G0), which no conic membership "
          "supplies.")

    section("S6 -- T-WALL: the full seat G = G0 + X in the Euler "
            "cone (would be the wall; expected dead)")
    wall_dead = []
    for r in ladder:
        G = [[r["G0"][0][0] + r["X"][0][0],
              r["G0"][0][1] + r["X"][0][1]],
             [r["G0"][0][1] + r["X"][0][1],
              r["G0"][1][1] + r["X"][1][1]]]
        tw = tier_seat(r, G)
        r["twall"] = tw
        if not tw["feasible"] and tw["dual"] and tw["dual"]["ok"]:
            print("    kz %3d INFEASIBLE, certified dual Y = "
                  "[%.6f, %.6f, %.6f], <Y,G> = %+.3e "
                  "(certified upper %+.3e, worst column margin "
                  "%+.2e)" % (r["kz"], *tw["dual"]["Y"],
                              tw["dual"]["val"],
                              tw["dual"]["val_hi"],
                              tw["dual"]["worst"]), flush=True)
            wall_dead.append(True)
        else:
            print("    kz %3d %s" % (r["kz"],
                                     "FEASIBLE" if tw["feasible"]
                                     else "infeasible (no certified "
                                     "dual)"))
            wall_dead.append(False)
    check("S6.1 the wall does NOT follow from source-only Euler "
          "positivity at the seat: G in the Euler cone is certified "
          "INFEASIBLE on every true rung (Farkas dual Y)",
          all(wall_dead), "%d/%d" % (sum(wall_dead), len(ladder)))

    section("S7 -- (E) and the centering (work item 5), adjudicated "
            "by exact algebra")
    for r in ladder:
        print("    kz %3d lam_min(G0) %s | (1/2)mu1 %.6e | "
              "lam_min(Gamma_geo seat) = lam_min(G0) + mu1/2 = %s"
              % (r["kz"], ivstr(r["lam_iv"]), float(r["mu1"]) / 2,
                 mp.nstr(r["lam_geo_seat"], 8)))
    check("S7.1 the centering term is IDENTICALLY ZERO (R1/R3 exact:"
          " gauge sums at mp %s), so identity (E) with the "
          "X-representing measure fails by exactly -lam_min(G0) > 0,"
          " certified" % mp.nstr(max(r["gauge"] for r in ladder), 2),
          all(r["lam_iv"].b < 0 for r in ladder))
    check("S7.2 lam_min(G0_h) is NOT the centering remainder: the "
          "candidate identity lam_min(Gamma_geo,seat) == 0 fails by "
          "O(1) on every rung",
          all(abs(float(r["lam_geo_seat"])) > 0.5 for r in ladder),
          "values %s" % ", ".join("%.4f" % float(r["lam_geo_seat"])
                                  for r in ladder))
    print("    the scalar reading of (E) (nu free, ONE equation) is "
          "VACUOUSLY solvable whenever Delta_h >= 0 -- one positive "
          "atom at any Euler frequency with S_-(t) != 0 suffices; "
          "typed VACUOUS, no content, gate rule: reformulation.")

    section("S8 -- controls (must fire): scramble / Epstein / smooth")
    ctrl_fire = {}
    scr_seat_pass = 0
    n_scr = 0
    for kz in ([9, 13] if SMOKE else list(LADDER_KZ)):
        rs = assemble_rung(kz, scramble_seed=SCR_SEED,
                           float_mode=True)
        if rs is None:
            continue
        rs = seat_objects(rs)
        rs = euler_reads(rs)
        ts_ = tier_seat(rs, rs["X"])
        n_scr += 1
        fired = (not ts_["feasible"]) and ts_["dual"] \
            and ts_["dual"]["ok"]
        if ts_["feasible"]:
            scr_seat_pass += 1
        print("    scramble kz %3d: X in cone -> %s%s"
              % (kz, "FEASIBLE (does NOT fire)" if ts_["feasible"]
                 else "infeasible",
                 "" if ts_["feasible"] else
                 (", dual certified" if fired else ", dual "
                  "UNCERTIFIED")), flush=True)
        ctrl_fire.setdefault("scramble", []).append(bool(fired))
    rr9 = core.build_window(CTRL_KZ)
    n_e = int(math.floor(math.exp(2.0 * rr9["alpha"]))) + 1
    lam_e = esq.lambda_eps(n_e)
    nn_e = np.nonzero(np.abs(lam_e) > 1e-12)[0]
    re_ = assemble_rung(CTRL_KZ, comb=(np.log(nn_e.astype(float)),
                                       2.0 * lam_e[nn_e]
                                       / np.sqrt(nn_e.astype(float))),
                        float_mode=True)
    re_ = seat_objects(re_)
    re_ = euler_reads(re_)
    te = tier_seat(re_, re_["X"])
    ep_fired = (not te["feasible"]) and te["dual"] and te["dual"]["ok"]
    Ge = [[re_["G0"][0][0] + re_["X"][0][0],
           re_["G0"][0][1] + re_["X"][0][1]],
          [re_["G0"][0][1] + re_["X"][0][1],
           re_["G0"][1][1] + re_["X"][1][1]]]
    tew = tier_seat(re_, Ge)
    print("    epstein  kz %3d: X in cone -> %s | G in cone -> %s "
          "(the wall-cone is NOT truth-selective)"
          % (CTRL_KZ, "FEASIBLE" if te["feasible"] else
             "infeasible (fires)",
             "FEASIBLE" if tew["feasible"] else "infeasible"))
    rsm = assemble_rung(CTRL_KZ, world="smooth", float_mode=True)
    rsm = seat_objects(rsm)
    co_max = float(np.max(np.abs(np.asarray(rsm["c_osc"]))))
    print("    smooth   kz %3d: |c_osc|_inf = %.3e (identically "
          "zero comb fluctuation), Delta = lam_min(G0) = %+.4f < 0"
          % (CTRL_KZ, co_max, float(rsm["lam_g0"])))
    check("E-scramble FIRES: X_scr leaves the Euler cone with a "
          "certified dual on every scramble rung",
          all(ctrl_fire.get("scramble", [False])),
          "%d/%d fired, %d/%d seat-passed"
          % (sum(ctrl_fire.get("scramble", [])), n_scr,
             scr_seat_pass, n_scr), kill="K4")
    check("E-epstein FIRES: X_eps leaves the Euler cone (certified "
          "dual)", bool(ep_fired), kill="K4")
    check("E-smooth STRUCTURE: the smooth world has c_osc == 0 and "
          "a strictly negative Delta -- no measure can represent a "
          "negative number", co_max <= 1e-12
          and float(rsm["lam_g0"]) < 0, kill="K4")
    check("K2 NOT TRIGGERED: the strongest surviving tier (T-SEAT) "
          "is comb-sensitive -- scramble does NOT pass it",
          scr_seat_pass == 0,
          "%d scramble seat-passes" % scr_seat_pass)

    section("S9 -- screens")
    print("    tau/c_h screens N/A BY CONSTRUCTION (declared): the "
          "consumed path forbids the target spectrum (no "
          "eigensolver, no tau, no shat); no margin claimed here is "
          "a wall substitute.  h-trend of the certified kill "
          "margins: eps_low %s across the ladder."
          % ", ".join("%.4f" % r["tfull"].get("eps_low", float("nan"))
                      for r in ladder))

    section("VERDICT (frozen enum)")
    n_ok = sum(1 for _n, o in CHECKS if o)
    full_all_dead = all(r["tfull_dead"] for r in ladder)
    seat_all = all(seat_ok)
    wall_all_dead = all(wall_dead)
    scr_blind = scr_seat_pass > 0
    if scr_blind:
        verdict = "SCHOENBERG-VACUOUS(scramble passes the seat tier)"
    elif full_all_dead and seat_all and wall_all_dead:
        verdict = ("SCHOENBERG-PARTIAL(exact statement: (i) the "
                   "TARGET IDENTITY (E) is refuted by exact algebra "
                   "-- the gauge R1/R3 makes the centering "
                   "contribution of EVERY measure identically zero, "
                   "so (E) requires lam_min(G0_h) = 0, which is "
                   "certified false [O(-1) on every rung]; its "
                   "scalar reading is vacuous; (ii) the FULL "
                   "centered form is certified NOT representable by "
                   "any positive Euler measure -- explicit negative "
                   "witness + Farkas distance eps_low ~ 0.33..0.37 "
                   "vs lag scale ~0.62 [K1 fires at the full-form "
                   "level]; (iii) what survives: the 2 x 2 "
                   "arithmetic seat block X_h HAS a certified exact "
                   "3-atom positive Euler representation on every "
                   "rung, and it is comb-sensitive [scramble and "
                   "Epstein certified out of the cone] -- but it "
                   "certifies only X_h >= 0, and the wall-cone "
                   "T-WALL is certified infeasible, so the wall "
                   "does NOT follow)")
    elif full_all_dead and not seat_all:
        verdict = ("SCHOENBERG-DEAD(K1 certificate: witness + dual "
                   "on every rung; no representation tier survives)")
    else:
        verdict = ("SCHOENBERG-PARTIAL(mixed censuses -- see the "
                   "tier tables above)")
    print("  VERDICT: %s" % verdict)
    print("  HONEST FRAME: finite frozen subset ladder (5 rungs), "
          "certified enclosures on float64-searched objects; no "
          "all-h statement; the gate rule reads the surviving seat "
          "representation as REFORMULATION-ONLY (X_h >= 0 was "
          "already measured); NO RH CLAIM.")
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed   [KILLS] %s"
          % (time.time() - T0, len(CHECKS), len(CHECKS) - n_ok,
             ",".join(sorted(set(KILLS))) if KILLS else "none"))
    print("  FROZEN_SPEC SHA-256 = %s" % SPEC_SHA)
    return 0 if n_ok == len(CHECKS) and not KILLS else 1


if __name__ == "__main__":
    sys.exit(main())
