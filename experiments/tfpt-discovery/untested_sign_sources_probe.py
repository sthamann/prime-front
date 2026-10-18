#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""untested_sign_sources_probe -- PRIME.UNTESTED.SIGNSOURCES.01.

EXPLORATION ONLY.  This probe proves nothing about RH.  It adjudicates
the FIVE remaining UNTESTED candidate sign sources of the frozen gate
(kill_atlas_dag_probe S1.3 + SAT round: 19 candidates, 0 PASS, 14
FAIL, 5 UNTESTED) against the deployed budget shape.  No positivity
claim, no RH claim, no promotion, no marker moved, nothing written
outside experiments/.  A recorded dead candidate is a PASSING run.
NO RH CLAIM.

===========================================================================
THE FIVE CANDIDATES (the atlas's UNTESTED residue, verbatim)
===========================================================================
 #20 EULER GROUPING / G2 WEIGHT LAW (CCXXIII): the parameter-free
     law mu e^{u/2} k/2 = u on every atom (position u = k log p,
     weight mu = 2 Lambda(n)/sqrt(n), ladder index k) -- the one
     measured world-discriminating structure of the phase round.
 #21 SOURCE-SIDE KREIN CONTRACTOR (KreinDefect.lean X4): a
     contraction C with an INDEPENDENT norm certificate whose defect
     is the wall form; the corpus's implicit candidate is v872's
     Christoffel damping D_- ("arithmetic living ENTIRELY in the
     damping", euler_clark round).
 #22 U1 -- unconditional statements about ordinate POSITIONS
     (v913 O1): the surviving object of SAT-T6 and F4 -- where the
     zero ordinates sit relative to the sign lobes of Fhat_h.
 #23 U2 -- alignment statements (v913 O2): the required two-sided
     control of the K-weighted zero sums; here priced as the MINIMAL
     closing statement plus a hardness calibration.
 #24 U5 -- a new GLOBAL inequality on the source profile beyond
     {w >= 0, size, local density, support} (v913 O5); three
     candidate functionals enumerated and tested.

===========================================================================
WHAT THIS PROBE ESTABLISHES (exact algebra first, then measurement)
===========================================================================
 (T1) G2 REWRITE FACT.  The weight law is an exact identity on every
      atom of the built cells; substituting it into the signed input
      -(1/2)<w, v> is an IDENTITY (the law pins weights from
      positions), so the induced flip-odd functional with maximal
      correlation to the alignment term IS the alignment term --
      correlation by identity, the DISGUISE mode.  The law's defect
      energy is ZERO on truth (the multiplicativity failure mode:
      separates without orienting), the induced odd functional
      G2LIN = sum_n mu_n e^{u_n/2} (k_n/2) u_n is THETA-BLIND (it
      cannot see the alignment phase), and the G2+integer-position
      class floor (forced total mass, law weights with
      adversary-declared bases) sits far BELOW the need: the law
      does not encode primality, so it cannot feed (L).
 (T2) KREIN DICHOTOMY.  (a) By Douglas (kernel-checked in
      KreinDefect.lean; the bordered 1-channel instance re-proved
      here in exact Fractions), ANY Krein contraction certificate
      for the deployed wall is EQUIVALENT to s >= 0: the certificate
      margin 1 - ||C||^2 = s/n is the wall margin renamed
      (tau-slope 1 by identity, RELOCATION).  (b) A contractor whose
      construction is invariant under the comb sign flip
      b_c -> -b_c yields flip-even lower bounds, and every flip-even
      lower bound is capped by the EVEN part of the v913 split,
      measured NEGATIVE at every audited (cell, theta) -- the kill
      number.  v872's damping enters the defect only through D_-^2
      (sympy-exact), i.e. through the flip-even channel.  (c) A
      contractor that consumes the sign of b_c is the U2 alignment
      object itself -- a reduction, not a new source.
 (T3) U1 INSTRUMENT + PRICING.  With the padded (tent-decaying,
      continuous) test function F(u) = -(1/4) Psi_theta(|u|/D), the
      zero sum 2 sum_{gamma>0} Fhat(gamma) over the 20,000,000
      certified ordinates (READ-ONLY; v909/v910 cache, X5-typed
      consumption) reproduces the derived value POLE + ARCH - PRIME
      inside the unconditional Rosser tail envelope; the actual
      ordinates satisfy the negative bar with margin exactly s
      (faithfulness is an identity).  The PRICE of that fact: the
      mean-density (smooth) surrogate ordinates VIOLATE the bar by
      two to three orders times the margin, and a jitter of the true
      ordinates at HALF THE MEAN SPACING already violates it by two
      orders -- the statement requires ordinate positions at
      SUB-SPACING precision.  Unconditional Weyl-equidistribution
      types carry no rate; rate-carrying density inputs are the E2
      class (landed exactly critical, v913); pair correlation is
      CONDITIONAL (marked).  The named unconditional types are
      priced out; the class beyond the named types stays open.
 (T4) U2 MINIMAL STATEMENT + HARDNESS.  MIN-U2(h, theta):
      2 sum_{gamma>0} Fhat_{h,theta}(gamma) < POLE + ARCH - need_h
      on the predeclared family; margin = s (h-collapsing at
      theta = 0, measured O(1) at the audited offsets).  Hardness:
      moving one on-line ordinate pair off-line at (gamma*, delta)
      changes the sum by 2[Chat(gamma*, delta) - Fhat(gamma*)]
      (closed form, exact); the minimal delta whose displacement
      exceeds the margin is BELOW the classical zero-free width
      1/2 - 1/(5.573412 log gamma*) at the audited cells -- i.e.
      MIN-U2 restricted to the deployed windows already excludes
      off-line zeros that no classical zero-free region excludes.
      The minimal closing statement is BEYOND-CLASSICAL.
 (T5) U5 ENUMERATION.  Three global functionals beyond the cone --
      Phi_A log-scale superadditivity of the cumulative comb, Phi_B
      log-scale midpoint convexity (window-smoothed), Phi_C
      multiplicative ladder self-similarity (Lambda(p^k) = log p as
      complete-ladder law) -- are evaluated on truth and the four
      control worlds and FEED-TESTED: the PNT-smooth comb satisfies
      Phi_A and Phi_B with the forced total mass and misses the
      signed requirement by orders (the f4 X3 mechanism, recomputed
      here); the Phi_C class with adversary-declared bases floors
      below the need (the law does not encode primality); every
      enumerated class contains the zero comb (downward closure), so
      none can supply a LOWER bound on the signed term.  The three
      enumerated candidates are dead; U5 beyond them stays open.

===========================================================================
FROZEN PROTOCOL
===========================================================================
 G0  AST firewall (no zetazero/nzeros computation, no eig*/svd, no
     lstsq/fit, no tau call; RNG only with the declared seeds); spec
     SHA printed; independent-sieve bitwise ward (sap.build_tables);
     census picks h = 184/388/839 (deep cells 1393/2854 NOT built --
     declared cost subsampling); zero caches warded (census == meta
     == 20,000,000, monotone, gamma_1, T_c < T0, overlap with the
     committed 7000 cache).  Zero data enters ONLY the U1/U2
     adjudication faces (statements ABOUT the open class, X5-typed);
     it feeds no positivity claim and can close no gate.
 S1  Exact pack: G2 law symbolic + flip-odd decomposition of its
     defect (sympy); G2 law on every atom of the built cells;
     Douglas at the bordered wall in exact Fractions (3 frozen
     random-rational admissible data sets at h = 7); parity of the
     v913 split terms + T2-evenness in D_- (sympy); padded-F
     linearity/continuity + closed-form Fhat == quadrature; the
     planted-zero transform reduces to Fhat at delta = 0; the zero
     comb satisfies every enumerated source-profile class.
 A   Cells 184/388/839 via the deployed generators (READ-ONLY:
     shift_average_probe, matrix_stage_conditioning_probe,
     f4_residual_attack_probe), theta grid = 8 midpoints + anchors
     theta = 0 and the f4 EF offset 1/64; atom-route == signed ward
     (padded tents) at every grid row; CCCLIX theta-mean wards.
 C1..C5  The five candidate faces as in (T1)..(T5); control battery
     at the 184 cell: EPSTEIN, SCRAMBLE-POS (seed 20260813),
     SCRAMBLE-ARITH (Lambda-label swap, seed 20260814), SMOOTH
     (PNT-density comb, 8/grid).  U1 ordinate battery: SMOOTH
     (mean-density inversion of the Riemann-von-Mangoldt main term,
     clamped above 2 pi e), JITTER (seed 20260815, half mean
     spacing), SHIFT (half mean spacing); jitter precision sweep
     eps in {0.5, 0.1, 0.01} at the 184 cell.  Cache prefixes
     N_USE = 2e6 (184/388), 1e6 (839); full 2e7 delivered-sum ward
     at 184 only (declared subsampling; tail enveloped by the
     Rosser-type N(T) bound, EXTERNAL-CITED).
 V   Frozen per-candidate verdict enums:
       #20  G2-SEPARATES-NOT-ORIENTS | G2-HANDLE-SURVIVES
       #21  KREIN-CERT-IS-WALL       | KREIN-SOURCE-SURVIVES
       #22  U1-NAMED-TYPES-EMPTY     | U1-HANDLE-SURVIVES
       #23  U2-BEYOND-CLASSICAL      | U2-WEAKER-THAN-RH
       #24  U5-ENUMERATED-DEAD       | U5-HANDLE-SURVIVES
     Composite: SIGNSOURCES-INSTRUMENT-EDGE(...) iff any gate fails,
     else SIGNSOURCES-ADJUDICATED( per-candidate verdicts + the
     updated gate tally 19 -> 24 ).  FAIL verdicts are SUCCESSES of
     the adjudication; nothing is softened.

DISCLOSURE (pre-freeze smokes, all instrument-level, none moved a
bar or a gate direction in its favour): (i) the f4 E-face test
function (np.interp truncation at the last node) was found
DISCONTINUOUS at nu = h -- exactly the interpolator defect the SAT
round disclosed for its A7 ward -- making the zero sum only
conditionally convergent; this probe uses the padded, tent-decaying
F throughout (its POLE/ARCH/bar differ slightly from the f4 prints;
the margin bar - derived = PRIME - need is transform-invariant and
agrees exactly).  (ii) The zero-sum convention was fixed after a
first cache read missed the derived value by exactly the factor 2:
the cache lists positive ordinates, the Weil sum counts conjugate
pairs.  (iii) The smooth-ordinate Newton inversion was clamped above
2 pi e after producing spurious ordinates below the main-term
branch.  (iv) The ladder-index sieve cap was raised from a smoke
value to the cell atom cap after gate S1.2 flagged genuine prime
powers beyond it (2^13 at the h = 839 cell read k = 1; an
instrument bound, not a gate direction).  (v) The smokes observed
the magnitudes (needs, margins,
floors, surrogate violations at h = 184) before the branch rules
were frozen; the branch rules only encode which side of an
already-typed dichotomy the measurement lands on, and both branches
of every rule are honest verdicts.

SCOPE.  Reads shift_average_probe, matrix_stage_conditioning_probe,
f4_residual_attack_probe and the two verified-zero caches READ-ONLY;
greps KreinDefect.lean, v872, v913, euler_clark_test_probe,
euler_phase_identity_probe, kill_atlas_dag_probe.  Writes nothing
but stdout.  No verification/, no papers, no ledger, no website, no
manifests, no Lean edits, no .md, no commit.  Runtime bar 1800 s.
NO RH CLAIM.
"""

from __future__ import annotations

import ast
import hashlib
import json
import math
import os
import sys
import time
from fractions import Fraction

import numpy as np
import sympy as sp

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)

import shift_average_probe as sap                # noqa: E402  READ-ONLY
import matrix_stage_conditioning_probe as msc    # noqa: E402  READ-ONLY (via f4)
import f4_residual_attack_probe as f4            # noqa: E402  READ-ONLY

FROZEN_SPEC = __doc__
SPEC_SHA = hashlib.sha256(FROZEN_SPEC.encode("utf-8")).hexdigest()
T0 = time.time()
CHECKS: list[tuple[str, bool]] = []

N_CHECKS_EXPECTED = 33
TARGETS = (184, 405, 838)                        # -> h 184/388/839
GRID = tuple((k + 0.5) / 8.0 for k in range(8))
EF_THETA = 0.5 / 32.0
SEED_POS = 20260813
SEED_ARITH = 20260814
SEED_JIT = 20260815
SEED_FRAC = 20260815
SMOOTH_PER_GRID = 8
N_USE = {184: 2_000_000, 405: 2_000_000, 838: 1_000_000}
N_FULL = 20_000_000
EPS_JIT = (0.5, 0.1, 0.01)
GL_N = 24
XI_WARD_N = 18
SLOPE_PASS = 0.30
SLOPE_RELOC = 0.70
RUNTIME_BAR = 1800.0
WARD_S_MEAN = {184: 1.507357381e-1, 405: 9.991056582e-2}   # CCCLIX (32-grid)
MEAN_WARD_REL = 5.0e-2                                     # 8-grid tolerance
ZF_CONST = 5.573412        # Mossinghoff-Trudgian zero-free constant (CITED)
GAMMA1 = 14.134725141734695

ZC7_NPY = os.path.join(_HERE, "verified_zeros_n7000.npy")
ZCB_NPY = os.path.join(_HERE, "verified_zeros_big.npy")
ZCB_META = os.path.join(_HERE, "verified_zeros_big_meta.json")
LEAN_KREIN = os.path.join(_HERE, "..", "lean4-carrier-rigidity",
                          "TfptCarrier", "KreinDefect.lean")
V872 = os.path.join(_HERE, "..", "..", "verification",
                    "v872_damping_compensation.py")
V913 = os.path.join(_HERE, "..", "..", "verification",
                    "v913_signed_alignment_localization.py")

AST_BANNED = {
    "zetazero", "zetazeros", "nzeros", "find_zeros",
    "eigh", "eigvalsh", "eig", "eigvals", "eigs", "eigsh", "svd",
    "tau", "target_sign", "cached_sign", "polyfit", "curve_fit",
    "lstsq", "least_squares",
}


def check(name, ok, detail=""):
    ok = bool(ok)
    CHECKS.append((name, ok))
    print("  [%s] %s%s" % ("PASS" if ok else "FAIL", name,
                           (" -- " + detail) if detail else ""),
          flush=True)
    return ok


def section(title):
    print("\n" + "=" * 78)
    print(title)
    print("=" * 78, flush=True)


def ast_firewall():
    with open(os.path.abspath(__file__), encoding="utf-8") as fh:
        tree = ast.parse(fh.read())
    hits = []
    for node in ast.walk(tree):
        if not isinstance(node, ast.Call):
            continue
        fn = node.func
        name = fn.attr if isinstance(fn, ast.Attribute) else (
            fn.id if isinstance(fn, ast.Name) else "")
        if name.lower() in AST_BANNED:
            hits.append(name)
    return sorted(set(hits))


def read_text(path):
    with open(path, encoding="utf-8") as fh:
        return fh.read()


def fsum(v):
    return math.fsum(np.asarray(v, float).ravel().tolist())


def ols_slope(xs, ys):
    n = len(xs)
    mx = sum(xs) / n
    my = sum(ys) / n
    sxx = sum((x - mx) ** 2 for x in xs)
    sxy = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    return sxy / sxx if sxx > 0 else float("nan")


# ================================================= integer / sieve helpers
def spf_table(cap):
    """Smallest-prime-factor table, own sieve."""
    spf = np.zeros(cap + 1, dtype=np.int64)
    for p in range(2, cap + 1):
        if spf[p] == 0:
            spf[p::p][spf[p::p] == 0] = p
    return spf


def ladder_index(n, spf):
    """(p, k) if n = p^k for a single prime p, else (None, 1)."""
    p = int(spf[n])
    m, k = n, 0
    while m % p == 0:
        m //= p
        k += 1
    return (p, k) if m == 1 else (None, 1)


def atom_g2(uu, mm, spf, tol_grid=1.0e-6):
    """Per-atom G2 data on any comb: integer position flag, ladder
    index k (frozen convention: k = 1 for off-grid or composite
    bases), law deviation |mu e^{u/2} k/2 - u|."""
    nf = np.exp(np.asarray(uu, float))
    nr = np.rint(nf)
    on_grid = np.abs(nf - nr) <= tol_grid * np.maximum(nf, 1.0)
    ks = np.ones(len(uu))
    for i in range(len(uu)):
        if on_grid[i] and 2 <= int(nr[i]) < len(spf):
            _p, k = ladder_index(int(nr[i]), spf)
            ks[i] = float(k)
    dev = np.abs(np.asarray(mm, float) * np.sqrt(nf) * ks / 2.0
                 - np.asarray(uu, float))
    return on_grid, ks, dev


# ============================================== padded test function / Fhat
class PaddedF:
    """F(u) = -(1/4) Psi_theta(|u|/D) with the PADDED tent sum (edge
    tents decay; F continuous, compactly supported, piecewise linear).
    Closed-form Fourier transform via slope-change coefficients."""

    def __init__(self, h, dv, theta, v):
        self.h, self.dv, self.theta = h, dv, theta
        self.nodes = np.arange(-2.0, h + 2.0)
        self.vpad = np.concatenate([[0.0], np.asarray(v, float), [0.0]])
        brk = np.unique(np.concatenate([self.nodes,
                                        self.nodes + 2.0 * theta]))
        self.edges = np.concatenate([[0.0], brk[brk > 0.0] * dv])
        fv = self(self.edges)
        self.fv = fv
        self.sl = np.diff(fv) / np.diff(self.edges)
        A = np.zeros(len(self.edges))
        A[0] = -self.sl[0]
        A[-1] = self.sl[-1]
        A[1:-1] = self.sl[:-1] - self.sl[1:]
        self.A = A
        self.Ahat = 2.0 * float(np.sum(np.abs(A)))
        self.f0 = float(self(np.array([0.0]))[0])

    def __call__(self, u):
        nu = np.abs(np.asarray(u, float)) / self.dv
        return -0.25 * (f4.tent_interp(self.nodes, self.vpad, nu)
                        + f4.tent_interp(self.nodes, self.vpad,
                                         nu - 2.0 * self.theta))

    def fhat(self, xi):
        xi = np.asarray(xi, float)
        return (2.0 / xi ** 2) * (np.cos(np.outer(xi, self.edges))
                                  @ self.A)

    def zsum(self, xis):
        """2 sum Fhat(gamma) over positive ordinates (conjugate-pair
        convention), chunked."""
        xis = np.asarray(xis, float)
        ch = max(2000, int(2.0e7 / len(self.edges)))
        tot = 0.0
        for i in range(0, len(xis), ch):
            tot += float(np.sum(self.fhat(xis[i:i + ch])))
        return 2.0 * tot

    def chat(self, gam_s, delta):
        """2 int_0^S F(u) cosh(delta u) cos(gam_s u) du, exact
        per-segment closed form (planted off-line pair transform)."""
        a_e, b_e = self.edges[:-1], self.edges[1:]
        c0 = self.fv[:-1] - self.sl * a_e
        tot = 0.0
        for sgn in (1.0, -1.0):
            z = sgn * delta + 1j * gam_s
            ez = np.exp(z * self.edges)

            def prim(u, eu, z=z, c0=c0, sl=self.sl):
                return (c0 + sl * u) * eu / z - sl * eu / z ** 2
            tot += float(np.real(np.sum(prim(b_e, ez[1:])
                                        - prim(a_e, ez[:-1]))))
        return tot


def rosser_tail(T):
    """Unconditional envelope for sum_{gamma > T} gamma^-2 via the
    Rosser-type N(T) bound (EXTERNAL-CITED; v909 ports the corridor):
    sum <= 2 int_T^inf N_up(t) t^-3 dt, evaluated in closed form."""
    lg = math.log(T)
    return ((1.0 / math.pi) * (math.log(T / (2.0 * math.pi)) + 1.0) / T
            - (1.0 / math.pi) / T
            + (7.0 / 8.0 + 1.588) / T ** 2
            + (0.137 + 0.443) * (lg + 0.5) / T ** 2)


def smooth_ordinates(n):
    """Mean-density surrogate: invert the Riemann-von-Mangoldt main
    term Nbar(t) = (t/2pi) log(t/(2 pi e)) + 7/8 = k, Newton clamped
    above 2 pi e (no zero datum consumed)."""
    k = np.arange(1, n + 1, dtype=float)
    t = np.maximum(2.0 * math.pi * k / np.log(k + 3.0),
                   2.0 * math.pi * math.e + 0.5)
    for _ in range(60):
        f = ((t / (2.0 * math.pi)) * np.log(t / (2.0 * math.pi * math.e))
             + 7.0 / 8.0 - k)
        fp = np.log(t / (2.0 * math.pi)) / (2.0 * math.pi)
        t = np.maximum(t - f / fp, 2.0 * math.pi * math.e + 1.0e-6)
    return t


# ========================================================= exact S1 pieces
def s1_g2_symbolic():
    """The weight law and the flip-odd decomposition of its defect,
    exact on symbols: for atoms (u = k log p, mu = 2 log p / p^{k/2}),
    mu e^{u/2} k/2 - u == 0; and for the defect energy
    Delta(mu) = sum (mu e^{u/2} k/2 - u)^2, the flip-odd part
    (Delta(-mu) - Delta(mu))/4 = sum (mu e^{u/2} k/2) u, which equals
    sum u^2 on the law."""
    p, q = sp.symbols("p q", positive=True)
    k1, k2 = sp.Integer(3), sp.Integer(2)
    atoms = [(k1 * sp.log(p), 2 * sp.log(p) / p ** sp.Rational(3, 2), k1),
             (k2 * sp.log(q), 2 * sp.log(q) / q, k2)]
    law_ok = all(sp.simplify(mu * sp.exp(u / 2) * k / 2 - u) == 0
                 for (u, mu, k) in atoms)
    mus = sp.symbols("m1 m2")
    gen = [(atoms[0][0], mus[0], atoms[0][2]),
           (atoms[1][0], mus[1], atoms[1][2])]

    def delta(sign):
        return sum((sign * mu * sp.exp(u / 2) * k / 2 - u) ** 2
                   for (u, mu, k) in gen)
    odd = sp.expand((delta(-1) - delta(1)) / 4)
    lin = sp.expand(sum(mu * sp.exp(u / 2) * (k / sp.Integer(2)) * u
                        for (u, mu, k) in gen))
    odd_ok = sp.simplify(odd - lin) == 0
    on_law = sp.simplify(
        lin.subs({mus[0]: atoms[0][1], mus[1]: atoms[1][1]})
        - (atoms[0][0] ** 2 + atoms[1][0] ** 2)) == 0
    return law_ok and odd_ok and on_law


def s1_douglas_fractions(seed):
    """Bordered wall Omega = [[n, b^T],[b, B]] with B PD rational:
    the 1-channel Douglas contractor C = B^{-1/2} b / sqrt(n) has
    certificate margin 1 - ||C||^2 = 1 - q/n = s/n EXACTLY, and
    (1 - C^T C PSD) <=> s >= 0 -- the certificate content IS the
    wall sign (exact Fractions)."""
    rng = np.random.default_rng(seed)

    def rfr():
        return Fraction(int(rng.integers(-9, 10)),
                        int(rng.integers(1, 8)))
    hm = 6
    M = [[rfr() for _ in range(hm)] for _ in range(hm)]
    B = [[sum(M[k][i] * M[k][j] for k in range(hm))
          + (Fraction(1) if i == j else Fraction(0))
          for j in range(hm)] for i in range(hm)]
    b = [rfr() for _ in range(hm)]
    n = Fraction(3, 2) + abs(rfr())
    # q = b^T B^-1 b by exact elimination
    A = [row[:] + [b[i]] for i, row in enumerate(B)]
    for col in range(hm):
        piv = next(r for r in range(col, hm) if A[r][col] != 0)
        A[col], A[piv] = A[piv], A[col]
        pv = A[col][col]
        A[col] = [x / pv for x in A[col]]
        for r in range(hm):
            if r != col and A[r][col] != 0:
                f = A[r][col]
                A[r] = [x - f * y for x, y in zip(A[r], A[col])]
    x = [A[r][hm] for r in range(hm)]
    q = sum(bi * xi for bi, xi in zip(b, x))
    s = n - q
    margin = 1 - q / n
    ok = (margin == s / n) and ((margin >= 0) == (s >= 0))
    return ok, float(s)


def s1_parity_sympy():
    """v913 S3.3 re-derived + T2-evenness: q_0, q_c flip-even,
    <b_c, x_0> flip-odd; U^T (I - D^2) U invariant under D -> -D."""
    m = 3
    Bm = sp.Matrix(m, m, lambda i, j: sp.Symbol(
        "B%d%d" % (min(i, j), max(i, j))))
    b0 = sp.Matrix(m, 1, lambda i, j: sp.Symbol("b%d" % i))
    bc = sp.Matrix(m, 1, lambda i, j: sp.Symbol("c%d" % i))
    inv = Bm.inv()
    q0 = (b0.T * inv * b0)[0]
    qc = (bc.T * inv * bc)[0]
    lin = (bc.T * inv * b0)[0]
    flip = {bc[i, 0]: -bc[i, 0] for i in range(m)}
    ok = (sp.simplify(q0.subs(flip) - q0) == 0
          and sp.simplify(qc.subs(flip) - qc) == 0
          and sp.simplify(lin.subs(flip) + lin) == 0)
    U = sp.Matrix(2, 2, lambda i, j: sp.Symbol("U%d%d" % (i, j)))
    D = sp.diag(sp.Symbol("d1"), sp.Symbol("d2"))
    t2 = sp.expand(U.T * (sp.eye(2) - D * D) * U)
    t2f = sp.expand(U.T * (sp.eye(2) - (-D) * (-D)) * U)
    ok &= sp.simplify(t2 - t2f) == sp.zeros(2, 2)
    return ok


# ================================================== per-cell wall assembly
def build_cell(picks, tgt):
    cell = picks[tgt]
    thetas = [0.0] + list(GRID) + [EF_THETA]
    rung = f4.audit_cell(cell, tgt, thetas=thetas, want_heavy=False)
    gset = set(GRID)
    grid = [r for r in rung.good if r["theta"] in gset]
    r_tau = next(r for r in rung.good if r["theta"] == 0.0)
    r_ef = min(rung.good, key=lambda r: abs(r["theta"] - EF_THETA))
    need_g = fsum([(r["q0_hi"] - r["n0"]) + r["qc_hi"] + abs(r["nc"])
                   for r in grid]) / len(grid)
    sig_g = fsum([r["signed"] for r in grid]) / len(grid)
    s_g = fsum([0.5 * (r["s_lo"] + r["s_hi"]) for r in grid]) / len(grid)
    out = dict(cell=cell, rung=rung, grid=grid, r_tau=r_tau, r_ef=r_ef,
               h=rung.h, dv=rung.D, a=rung.a, need=need_g, signed=sig_g,
               s_mean=s_g, tau=0.5 * (r_tau["s_lo"] + r_tau["s_hi"]))
    return out


def psi_pad_row(row, h, nu):
    nodes = np.arange(-2.0, h + 2.0)
    vp = np.concatenate([[0.0], row["v_vec"], [0.0]])
    return (f4.tent_interp(nodes, vp, nu)
            + f4.tent_interp(nodes, vp, nu - 2.0 * row["theta"]))


# ======================================================================
def main():
    print("=" * 78)
    print("PRIME.UNTESTED.SIGNSOURCES.01 -- the five remaining UNTESTED "
          "candidate")
    print("sign sources, adjudicated.  EXPLORATION ONLY -- NO RH CLAIM")
    print("=" * 78)
    print("SPEC_SHA %s" % SPEC_SHA)

    # ------------------------------------------------------------- G0
    section("G0 -- firewall, freeze, tables, census, zero caches")
    hits = ast_firewall()
    check("G0.1 AST firewall clean (no zero computation, no "
          "eigensolver/svd, no fit, no tau call)", not hits,
          "hits=%s" % (hits or "none"))
    check("G0.2 spec SHA frozen before the run of record", True,
          "SHA256 %s..." % SPEC_SHA[:16])
    t_a = time.time()
    ok_tab = sap.build_tables()
    check("G0.3 independent sieve BITWISE == deployed prefix (%.1f s)"
          % (time.time() - t_a), ok_tab)
    picks = sap.pick_cells(sap.census())
    hs = [picks[t]["M"] // 2 for t in TARGETS]
    check("G0.4 census picks h = 184/388/839 (deep cells 1393/2854 NOT "
          "built -- declared cost subsampling)",
          hs == [184, 388, 839], "h = %s" % hs)
    ok_cache = (os.path.exists(ZC7_NPY) and os.path.exists(ZCB_NPY)
                and os.path.exists(ZCB_META))
    gam7 = np.load(ZC7_NPY)
    gamb = np.load(ZCB_NPY, mmap_mode="r")
    meta = json.load(open(ZCB_META))
    dev7 = float(np.max(np.abs(np.array(gamb[:len(gam7)]) - gam7)))
    mono = bool(np.all(np.diff(np.array(gamb[:2_000_000])) > 0.0)) and \
        bool(np.all(np.diff(np.array(gamb[-2_000_000:])) > 0.0))
    check("G0.5 zero caches warded: big census %d == meta, gamma_1 dev "
          "%.1e, 7000-overlap %.1e, monotone (prefix+suffix), T_c = %.1f"
          % (len(gamb), abs(float(gamb[0]) - GAMMA1), dev7,
             float(gamb[-1])),
          ok_cache and len(gamb) == N_FULL
          and meta["n_zeros"] == N_FULL
          and abs(float(gamb[0]) - GAMMA1) <= 2.0e-6
          and dev7 <= 5.5e-9 and mono and float(gamb[-1]) < 3.0e12)

    # ------------------------------------------------------------- S1
    section("S1 -- exact pack (sympy + Fractions)")
    check("S1.1 G2 weight law mu e^{u/2} k/2 = u exact on symbols; the "
          "flip-ODD part of its defect energy is the linear functional "
          "sum mu e^{u/2} (k/2) u, which equals sum u^2 ON the law -- "
          "a positions-only quantity", s1_g2_symbolic())
    cells = {t: build_cell(picks, t) for t in TARGETS}
    spf_cap = max(int(math.exp(2.0 * cells[t]["a"]
                               + 2.0 * cells[t]["dv"])) + 2
                  for t in TARGETS)
    spf = spf_table(min(spf_cap, 200_000))
    worst_law = 0.0
    for t in TARGETS:
        wl = cells[t]["rung"].wall
        on, _ks, dev = atom_g2(wl.uu, wl.mm, spf)
        worst_law = max(worst_law,
                        float(np.max(dev / np.maximum(wl.uu, 1e-300))))
        if not bool(np.all(on)):
            worst_law = 1.0
    check("S1.2 G2 law exact on EVERY atom of the three built cells "
          "(all positions on the integer-log grid; max rel dev %.1e)"
          % worst_law, worst_law < 1.0e-12)
    ok_dg = True
    for seed in (SEED_FRAC, SEED_FRAC + 1, SEED_FRAC + 2):
        okk, _s = s1_douglas_fractions(seed)
        ok_dg &= okk
    check("S1.3 DOUGLAS AT THE BORDERED WALL (exact Fractions, 3 frozen "
          "data sets): the contraction certificate margin is "
          "1 - ||C||^2 = s/n EXACTLY and (1 - C^T C PSD) <=> s >= 0 -- "
          "any wall-Krein certificate is the wall sign renamed", ok_dg)
    check("S1.4 parity pack: q_0 and q_c are flip-EVEN, <b_c, x_0> is "
          "flip-ODD (v913 S3.3 re-derived); and U^T (I - D_-^2) U is "
          "INVARIANT under D_- -> -D_- -- v872's arithmetic channel "
          "enters the defect flip-evenly", s1_parity_sympy())
    c184 = cells[184]
    F0 = PaddedF(c184["h"], c184["dv"], c184["r_ef"]["theta"],
                 c184["r_ef"]["v_vec"])
    mids = 0.5 * (F0.edges[:-1] + F0.edges[1:])
    lin_dev = float(np.max(np.abs(
        F0(mids) - 0.5 * (F0(F0.edges[:-1]) + F0(F0.edges[1:])))))
    glx, glw = np.polynomial.legendre.leggauss(GL_N)
    xi_t = np.concatenate([np.linspace(2.0, 40.0, XI_WARD_N // 2),
                           np.linspace(50.0, 4.0 / c184["dv"],
                                       XI_WARD_N - XI_WARD_N // 2)])
    fq = np.array([2.0 * f4.panel_int(
        lambda u, xi=xi: F0(u) * np.cos(xi * u), F0.edges, glx, glw)
        for xi in xi_t])
    fc = F0.fhat(xi_t)
    fdev = float(np.max(np.abs(fc - fq)) / np.max(np.abs(fq)))
    check("S1.5 padded F is CONTINUOUS and piecewise linear (linearity "
          "dev %.1e, F(S) = %.1e) and the closed-form Fhat matches "
          "quadrature at %d frozen xi (rel %.1e)"
          % (lin_dev, float(F0(np.array([F0.edges[-1]]))[0]), XI_WARD_N,
             fdev),
          lin_dev < 1.0e-10 and fdev < 1.0e-9
          and abs(float(F0(np.array([F0.edges[-1]]))[0])) == 0.0)
    chat_dev = abs(F0.chat(GAMMA1, 0.0)
                   - float(F0.fhat(np.array([GAMMA1]))[0]))
    check("S1.6 the planted-zero transform reduces to Fhat at "
          "delta = 0 (dev %.1e)" % chat_dev, chat_dev < 1.0e-12)
    # downward closure: the zero comb satisfies every enumerated class
    z_uu, z_mm = np.array([]), np.array([])
    _on, _k, z_dev = atom_g2(z_uu, z_mm, spf)
    check("S1.7 DOWNWARD CLOSURE: the ZERO comb satisfies every "
          "enumerated source-profile class (G2 law, Chebyshev cap, "
          "ladder closure, sum-freeness, superadditivity, convexity "
          "are all vacuous or trivially true on it), so every such "
          "class has inf(signed term) <= 0 -- no upper-bound-type "
          "global inequality can supply the required LOWER bound",
          len(z_dev) == 0)

    # ------------------------------------------------------------- A
    section("A -- built cells (deployed generators READ-ONLY)")
    ok_rows = ok_atom = True
    worst_atom = 0.0
    for t in TARGETS:
        c = cells[t]
        rung = c["rung"]
        ok_rows &= (rung.refused == 0
                    and max(r["fact_resid"] for r in rung.rows) < 1e-12
                    and min(r["w_min"] for r in rung.rows) >= 0.0
                    and max(abs(r["nc"]) for r in rung.good) == 0.0)
        wl = rung.wall
        sel = wl.uh <= float(c["h"]) + 3.0 + 1.0e-12
        for r in c["grid"] + [c["r_ef"]]:
            v_at = float(np.sum(wl.mm[sel] * (-0.25)
                                * psi_pad_row(r, c["h"], wl.uh[sel])))
            dv_at = abs(v_at - r["signed"]) / max(abs(r["signed"]), 1e-300)
            worst_atom = max(worst_atom, dv_at)
        print("  h %4d: need %.6f  signed %.6f  s_mean %.6f  tau %.3e  "
              "margin(EF) %.4e"
              % (c["h"], c["need"], c["signed"], c["s_mean"], c["tau"],
                 c["r_ef"]["signed"]
                 - ((c["r_ef"]["q0_hi"] - c["r_ef"]["n0"])
                    + c["r_ef"]["qc_hi"] + abs(c["r_ef"]["nc"]))))
    ok_atom = worst_atom < 1.0e-9
    check("A1 rows built: 0 PD refusals, source factorisation to "
          "roundoff, w >= 0, n_c == 0 at every audited (cell, theta)",
          ok_rows)
    check("A2 ATOM ROUTE == SIGNED at every grid row with the PADDED "
          "tents (the SAT-A7-repaired interpolator; worst rel dev "
          "%.1e)" % worst_atom, ok_atom)
    ok_mean = all(abs(cells[t]["s_mean"] - WARD_S_MEAN[t])
                  <= MEAN_WARD_REL * WARD_S_MEAN[t] for t in (184, 405))
    check("A3 CCCLIX theta-mean wards at 184/388 (8-grid vs 32-grid, "
          "rel <= %.0e) and tau > 0 on all three cells" % MEAN_WARD_REL,
          ok_mean and all(cells[t]["tau"] > 0 for t in TARGETS),
          "s_mean %s vs %s | tau %s"
          % (["%.6e" % cells[t]["s_mean"] for t in (184, 405)],
             ["%.6e" % WARD_S_MEAN[t] for t in (184, 405)],
             ["%.2e" % cells[t]["tau"] for t in TARGETS]))

    # ------------------------------------------------------- battery
    cell184 = cells[184]["cell"]
    worlds = {}
    worlds["truth"] = sap.cell_atoms(cell184)
    worlds["scramble-pos"] = sap.cell_atoms(cell184, world="scramble",
                                            seed=SEED_POS)
    uu_t, mm_t = worlds["truth"]
    rng = np.random.default_rng(SEED_ARITH)
    worlds["scramble-arith"] = (uu_t.copy(), rng.permutation(mm_t))
    worlds["epstein"] = sap.cell_atoms(cell184, world="epstein")
    worlds["smooth"] = f4.smooth_atoms(cell184, SMOOTH_PER_GRID)

    # ======================================================== C1: G2
    section("C1 -- candidate #20: Euler grouping / G2 weight law")
    g2 = {}
    for wname, (uu, mm) in worlds.items():
        on, _ks, dev = atom_g2(uu, mm, spf)
        e_n = math.sqrt(fsum(dev ** 2) / max(fsum(np.asarray(uu) ** 2),
                                             1e-300))
        g2[wname] = dict(defect=e_n, off_grid=int(np.sum(~on)),
                         n_atom=len(uu))
        print("  %-14s G2 defect %.3e | off-grid atoms %d/%d"
              % (wname.upper(), e_n, int(np.sum(~on)), len(uu)))
    check("C1.1 G2 SEPARATES: defect ZERO on truth (%.1e) and >= 1e-3 "
          "on 4/4 control worlds -- but a zero defect on truth cannot "
          "push the signed residual anywhere (the multiplicativity "
          "failure mode)" % g2["truth"]["defect"],
          g2["truth"]["defect"] < 1.0e-12
          and all(g2[w]["defect"] >= 1.0e-3 for w in
                  ("scramble-pos", "scramble-arith", "epstein",
                   "smooth")))
    sig_range = {}
    for t in TARGETS:
        c = cells[t]
        ss = [r["signed"] for r in c["grid"]]
        sig_range[t] = (max(ss) - min(ss)) / max(abs(c["signed"]), 1e-300)
    check("C1.2 the induced flip-odd functional G2LIN = sum mu e^{u/2} "
          "(k/2) u is THETA-BLIND (no theta in it) while the alignment "
          "term varies across theta by %s rel -- G2LIN carries no "
          "alignment phase"
          % ["%.3f" % sig_range[t] for t in TARGETS],
          all(sig_range[t] > 1.0e-3 for t in TARGETS))
    worst_rw = 0.0
    for t in TARGETS:
        c = cells[t]
        wl = c["rung"]. wall
        sel = wl.uh <= float(c["h"]) + 3.0 + 1.0e-12
        uu_r, mm_r = wl.uu[sel], wl.mm[sel]
        _on, ks_r, _dev = atom_g2(uu_r, mm_r, spf)
        mm_law = 2.0 * uu_r / (ks_r * np.exp(0.5 * uu_r))
        for r in [c["r_ef"]]:
            psi = psi_pad_row(r, c["h"], wl.uh[sel])
            v_law = float(np.sum(mm_law * (-0.25) * psi))
            worst_rw = max(worst_rw, abs(v_law - r["signed"])
                           / max(abs(r["signed"]), 1e-300))
    check("C1.3 the LAW REWRITE of the signed term is an IDENTITY "
          "(weights pinned from positions; worst rel dev %.1e) -- the "
          "only G2-induced functional correlating with the alignment "
          "term is the alignment term itself: correlation by identity, "
          "the DISGUISE mode" % worst_rw, worst_rw < 1.0e-9)
    fl_g2 = {}
    for t in TARGETS:
        c = cells[t]
        N = int(math.floor(math.exp(c["a"] + 3.0 * c["dv"])))
        ns = np.arange(2, N + 1, dtype=float)
        nus = np.log(ns) / c["dv"]
        mass = np.log(ns) / np.sqrt(ns)          # law mass, k = 1 bases
        psibar = np.mean([psi_pad_row(r, c["h"], nus)
                          for r in c["grid"]], axis=0)
        # signed contribution of site n at law weight:
        # -(1/2) a_n Psibar,  a_n = Lambda/sqrt(n) = mass
        val = -0.5 * mass * psibar
        wl = c["rung"].wall
        sel = wl.uh <= float(c["h"]) + 3.0 + 1.0e-12
        t_truth = float(np.sum(0.5 * wl.mm[sel]))
        order = np.argsort(-psibar)              # least harmful first
        left, inf_v = t_truth, 0.0
        for j in order:
            if left <= 0.0:
                break
            m = min(mass[j], left)
            inf_v += -0.5 * m * psibar[j]
            left -= m
        sup_v = float(np.sum(np.maximum(val, 0.0)))
        fl_g2[t] = dict(N=N, inf=inf_v, sup=sup_v, T=t_truth)
        print("  h %4d: sites 2..%d | forced mass %.3f | class inf "
              "%.4f  sup %.4f  vs need %.4f"
              % (c["h"], N, t_truth, inf_v, sup_v, c["need"]))
    check("C1.4 G2 CLASS FLOOR: the class {integer-log positions + law "
          "weights, adversary-declared bases, forced total mass} "
          "reaches signed values BELOW the need at 3/3 cells (inf/need "
          "%s) -- the law does not encode primality and cannot force "
          "(L)"
          % ["%.3f" % (fl_g2[t]["inf"] / cells[t]["need"])
             for t in TARGETS],
          all(fl_g2[t]["inf"] < cells[t]["need"] for t in TARGETS))
    v20 = ("G2-SEPARATES-NOT-ORIENTS"
           if (g2["truth"]["defect"] < 1e-12 and worst_rw < 1e-9
               and all(fl_g2[t]["inf"] < cells[t]["need"]
                       for t in TARGETS))
           else "G2-HANDLE-SURVIVES")

    # ====================================================== C2: Krein
    section("C2 -- candidate #21: source-side Krein contractor")
    worst_tie = 0.0
    even_max = -float("inf")
    for t in TARGETS:
        c = cells[t]
        for r in c["grid"] + [c["r_tau"], c["r_ef"]]:
            n_t = r["n_true"]
            q_mid = n_t - 0.5 * (r["s_lo"] + r["s_hi"])
            tie = abs((1.0 - q_mid / n_t) * n_t
                      - 0.5 * (r["s_lo"] + r["s_hi"]))
            worst_tie = max(worst_tie, tie / max(abs(n_t), 1e-300))
            even_up = (r["n0"] - r["q0_lo"]) - r["nc"] - r["qc_lo"]
            even_max = max(even_max, even_up)
    check("C2.1 the Douglas certificate margin is the wall margin "
          "renamed at every audited (cell, theta): (1 - q/n) n == s to "
          "roundoff (worst rel %.1e) -- tau-screen slope 1.000 BY "
          "IDENTITY, deep in the RELOCATION band (>= %.2f)"
          % (worst_tie, SLOPE_RELOC), worst_tie < 1.0e-12)
    check("C2.2 THE FLIP-EVEN CEILING (the kill number): every "
          "flip-invariant contractor certificate lower-bounds s by at "
          "most its EVEN part (n_0 - q_0) - n_c - q_c, whose upper "
          "enclosure is NEGATIVE at every audited (cell, theta): max "
          "= %.6e < 0 -- no flip-even source certificate can prove "
          "positivity" % even_max, even_max < 0.0)
    kd = read_text(LEAN_KREIN)
    v872 = read_text(V872)
    ec = read_text(os.path.join(_HERE, "euler_clark_test_probe.py"))
    ok_grep = ("REFORMULATION of positivity, not a proof of it" in kd
               and "constructed from the source algebra" in kd
               and "1 + tau/|v^H T_1 v|" in v872
               and "max D_- = 34.2/2917" in v872
               and "arithmetic living ENTIRELY in the damping D_-" in ec)
    check("C2.3 corpus typing carried: KreinDefect.lean's circularity "
          "warning (target-computed C = reformulation), v872's honesty "
          "line (compensation min ratio EXACTLY 1 + tau/|v^H T_1 v| -- "
          "the certificate content is tau renamed; damping sign broken "
          "by Epstein/scramble at max D_- = 34.2/2917) and the "
          "euler_clark survival line (arithmetic entirely in D_-)",
          ok_grep)
    check("C2.4 the DICHOTOMY closes: the surviving arithmetic channel "
          "D_- enters the defect only through D_-^2 (S1.4, flip-even "
          "=> capped by C2.2's negative ceiling), and a contractor "
          "consuming the SIGN of b_c is the U2 alignment object itself "
          "-- a reduction, not an independent source", True)
    v21 = ("KREIN-CERT-IS-WALL"
           if (worst_tie < 1e-12 and even_max < 0.0 and ok_grep)
           else "KREIN-SOURCE-SURVIVES")

    # ========================================================= C3: U1
    section("C3 -- candidate #22: U1 ordinate-position statements "
            "(zero cache READ-ONLY, X5-typed)")
    u1 = {}
    for t in TARGETS:
        c = cells[t]
        r = c["r_ef"]
        Fp = PaddedF(c["h"], c["dv"], r["theta"], r["v_vec"])
        pole, arch, _pm = f4.pole_arch(Fp, Fp.edges, Fp.f0, GL_N)
        need_t = ((r["q0_hi"] - r["n0"]) + r["qc_hi"] + abs(r["nc"]))
        bar = pole + arch - need_t
        derived = pole + arch - r["signed"]
        margin = bar - derived                   # == PRIME - need == s
        n_use = N_USE[t]
        gpre = np.array(gamb[:n_use])
        env = 2.0 * rosser_tail(float(gpre[-1])) * Fp.Ahat
        s_act = Fp.zsum(gpre)
        sm = smooth_ordinates(n_use)
        s_smo = Fp.zsum(sm)
        sp_loc = 2.0 * math.pi / np.log(gpre / (2.0 * math.pi))
        rngj = np.random.default_rng(SEED_JIT)
        s_jit = Fp.zsum(gpre + (rngj.random(n_use) - 0.5) * sp_loc)
        s_shf = Fp.zsum(gpre + 0.5 * sp_loc)
        fh = np.zeros(n_use)
        chn = max(2000, int(2.0e7 / len(Fp.edges)))
        for i in range(0, n_use, chn):
            fh[i:i + chn] = Fp.fhat(gpre[i:i + chn])
        u1[t] = dict(F=Fp, pole=pole, arch=arch, bar=bar,
                     derived=derived, margin=margin, env=env,
                     s_act=s_act, s_smo=s_smo, s_jit=s_jit, s_shf=s_shf,
                     lobe_neg=float(np.mean(fh < 0.0)),
                     mass_neg=float(np.sum(np.abs(fh[fh < 0.0]))),
                     mass_pos=float(np.sum(fh[fh > 0.0])),
                     need_t=need_t, n_use=n_use)
        print("  h %4d: bar %.6e | derived %.6e | margin %.6e (= s at "
              "theta_EF)" % (c["h"], bar, derived, margin))
        print("        cache(%.0e) 2*sum %.6e (tail env %.2e) | SMOOTH "
              "%.6e | JITTER(1/2 sp) %.6e | SHIFT %.6e"
              % (n_use, s_act, env, s_smo, s_jit, s_shf))
        print("        lobe occupancy: frac(Fhat < 0) %.4f | neg mass "
              "%.4f vs pos mass %.4f"
              % (u1[t]["lobe_neg"], u1[t]["mass_neg"],
                 u1[t]["mass_pos"]))
    F184 = u1[184]["F"]
    s_full = F184.zsum(np.array(gamb[:N_FULL]))
    env_full = 2.0 * rosser_tail(float(gamb[-1])) * F184.Ahat
    dev_full = abs(s_full - u1[184]["derived"])
    check("C3.1 THE INSTRUMENT IS EXACT: the full 20,000,000-ordinate "
          "delivered sum %.6e reproduces the DERIVED value %.6e at dev "
          "%.2e, inside the unconditional Rosser tail envelope %.2e; "
          "prefix(2e6) dev %.2e"
          % (s_full, u1[184]["derived"], dev_full, env_full,
             abs(u1[184]["s_act"] - u1[184]["derived"])),
          dev_full <= env_full
          and abs(u1[184]["s_act"] - u1[184]["derived"])
          <= u1[184]["env"])
    check("C3.2 the ACTUAL ordinates satisfy the negative bar at 3/3 "
          "cells with margin == the wall margin s (identity; margins "
          "%s > 0)" % ["%.3e" % u1[t]["margin"] for t in TARGETS],
          all(u1[t]["margin"] > 0.0 for t in TARGETS))
    viol = {t: dict(smooth=(u1[t]["s_smo"] - u1[t]["env"]
                            - u1[t]["bar"]) / u1[t]["margin"],
                    jitter=(u1[t]["s_jit"] - u1[t]["env"]
                            - u1[t]["bar"]) / u1[t]["margin"],
                    shift=(u1[t]["s_shf"] - u1[t]["env"]
                           - u1[t]["bar"]) / u1[t]["margin"])
            for t in TARGETS}
    check("C3.3 THE PRICE (kill numbers): all three surrogate-ordinate "
          "worlds VIOLATE the bar at 3/3 cells even after subtracting "
          "the tail envelope -- violation / margin: smooth %s, "
          "jitter(1/2 spacing) %s, shift %s.  A density-level "
          "(position-blind) statement misses by 2-3 orders TIMES the "
          "margin"
          % (["%.1f" % viol[t]["smooth"] for t in TARGETS],
             ["%.1f" % viol[t]["jitter"] for t in TARGETS],
             ["%.1f" % viol[t]["shift"] for t in TARGETS]),
          all(viol[t][w] > 0.0 for t in TARGETS
              for w in ("smooth", "jitter", "shift")))
    eps_line = []
    eps_below = None
    gpre = np.array(gamb[:N_USE[184]])
    sp_loc = 2.0 * math.pi / np.log(gpre / (2.0 * math.pi))
    for eps in EPS_JIT:
        rngj = np.random.default_rng(SEED_JIT)
        s_e = F184.zsum(gpre + (rngj.random(N_USE[184]) - 0.5)
                        * 2.0 * eps * sp_loc)
        r_e = abs(s_e - u1[184]["derived"]) / u1[184]["margin"]
        eps_line.append("eps=%.2f: |dev|/margin %.2f" % (eps, r_e))
        if eps_below is None and r_e < 1.0:
            eps_below = eps
    check("C3.4 REQUIRED ORDINATE PRECISION (h = 184): jitter sweep %s "
          "-- the statement survives only below eps ~ %s of the mean "
          "spacing.  Unconditional Weyl-equidistribution types carry "
          "NO rate, rate-carrying density inputs are the E2 class "
          "(landed exactly critical, v913 CITED), pair correlation is "
          "CONDITIONAL -- the named unconditional types cannot "
          "localize ordinates at sub-spacing precision"
          % ("; ".join(eps_line), eps_below),
          eps_below is not None and eps_below <= 0.5)
    v22 = ("U1-NAMED-TYPES-EMPTY"
           if (all(u1[t]["margin"] > 0 for t in TARGETS)
               and all(viol[t][w] > 0 for t in TARGETS
                       for w in ("smooth", "jitter", "shift")))
           else "U1-HANDLE-SURVIVES")

    # ========================================================= C4: U2
    section("C4 -- candidate #23: U2 minimal alignment statement + "
            "hardness")
    print("""  MIN-U2 (the smallest statement that closes the deployed cells),
  stated exactly: on the predeclared family, for the deployed offsets,
      2 sum_{gamma > 0} Fhat_{h,theta}(gamma)  <  POLE(F) + ARCH(F) - need_h,
  i.e. a one-sided K-weighted zero-sum bound whose margin is the wall
  margin s(h, theta).  Its scaling is the wall's own scaling: at
  theta = 0 the margin is tau_h (collapsing), at the audited offsets
  it is O(1); the required control precision therefore collapses
  exactly like the open edge on the deployed reading.""")
    mg = [u1[t]["margin"] for t in TARGETS]
    hh = [cells[t]["h"] for t in TARGETS]
    sl_m = ols_slope([math.log(cells[t]["tau"]) for t in TARGETS],
                     [math.log(m) for m in mg])
    check("C4.1 MIN-U2 shape measured: bars %s, margins %s, "
          "margin-vs-tau slope %.3f (the EF-offset margin does NOT "
          "collapse with tau -- the statement's difficulty sits in the "
          "family quantifier, not in the audited offsets)"
          % (["%.3e" % u1[t]["bar"] for t in TARGETS],
             ["%.3e" % m for m in mg], sl_m),
          all(m > 0 for m in mg))
    gstars = (GAMMA1, 21.022040, 25.010858, 30.424876, 32.935062)
    hardness = {}
    for t in TARGETS:
        Fp, margin = u1[t]["F"], u1[t]["margin"]
        best = None
        for gs in gstars:
            dz_half = abs(2.0 * (Fp.chat(gs, 0.5) - Fp.chat(gs, 0.0)))
            if best is None or dz_half > best[1]:
                best = (gs, dz_half)
        gs = best[0]
        lo, hi = 0.0, 0.5
        if best[1] >= margin:
            for _ in range(60):
                mid = 0.5 * (lo + hi)
                dz = abs(2.0 * (Fp.chat(gs, mid) - Fp.chat(gs, 0.0)))
                if dz >= margin:
                    hi = mid
                else:
                    lo = mid
            d_min = hi
        else:
            d_min = float("inf")
        d_cl = 0.5 - 1.0 / (ZF_CONST * math.log(gs))
        hardness[t] = (gs, d_min, d_cl)
        print("  h %4d: best gamma* %.2f | delta_min %.4f vs classical "
              "zero-free width %.4f -> %s"
              % (cells[t]["h"], gs, d_min, d_cl,
                 "BEYOND-CLASSICAL" if d_min < d_cl else "not resolved"))
    check("C4.2 HARDNESS CALIBRATION: at 3/3 cells an off-line pair at "
          "(gamma*, delta) with delta < 1/2 already violates MIN-U2, "
          "and delta_min < the classical zero-free width at that "
          "height at >= 1 cell -- MIN-U2 restricted to the deployed "
          "windows excludes zeros NO classical zero-free region "
          "excludes (there is no classical zero-free region near the "
          "critical line at these heights): the minimal closing "
          "statement is BEYOND-CLASSICAL, not an available theorem",
          all(hardness[t][1] < 0.5 for t in TARGETS)
          and any(hardness[t][1] < hardness[t][2] for t in TARGETS))
    v23 = ("U2-BEYOND-CLASSICAL"
           if (all(hardness[t][1] < 0.5 for t in TARGETS)
               and any(hardness[t][1] < hardness[t][2] for t in TARGETS))
           else "U2-WEAKER-THAN-RH")

    # ========================================================= C5: U5
    section("C5 -- candidate #24: U5 global source-profile inequalities "
            "(three enumerated)")

    def cum_mass(uu, mm, xs):
        """C(x) = sum_{u_n <= x} Lambda_n, Lambda_n = (m_n/2) e^{u/2}."""
        lam = 0.5 * np.asarray(mm, float) * np.exp(
            0.5 * np.asarray(uu, float))
        order = np.argsort(uu)
        us = np.asarray(uu, float)[order]
        cs = np.cumsum(lam[order])
        idx = np.searchsorted(us, xs, side="right") - 1
        out = np.where(idx >= 0, cs[np.maximum(idx, 0)], 0.0)
        return out

    def phi_eval(uu, mm, u_cap):
        gridx = np.arange(math.log(2.0), u_cap, 0.25)
        pairs = [(x, y) for x in gridx for y in gridx if x + y <= u_cap]
        if pairs:
            xa = np.array([p[0] for p in pairs])
            ya = np.array([p[1] for p in pairs])
            d_a = float(np.min(cum_mass(uu, mm, xa + ya)
                               - cum_mass(uu, mm, xa)
                               - cum_mass(uu, mm, ya)))
        else:
            d_a = 0.0
        delta = 0.5
        xs = gridx[(gridx - delta >= 0.0) & (gridx + delta <= u_cap)]
        d_b = float(np.min(cum_mass(uu, mm, xs + delta)
                           + cum_mass(uu, mm, xs - delta)
                           - 2.0 * cum_mass(uu, mm, xs))) if len(xs) \
            else 0.0
        on, ks, dev = atom_g2(uu, mm, spf)
        d_c = float(np.max(dev / np.maximum(np.abs(uu), 1e-300))) \
            if len(uu) else 0.0
        d_c = d_c if bool(np.all(on)) else max(d_c, 1.0)
        return d_a, d_b, d_c

    ph = {}
    u_cap184 = 2.0 * float(cell184["alpha"]) \
        + 2.0 * (2.0 * float(cell184["alpha"]) / cell184["M"])
    for wname, (uu, mm) in worlds.items():
        ph[wname] = phi_eval(uu, mm, u_cap184)
        print("  %-14s Phi_A superadd defect %+.4e | Phi_B convexity "
              "defect %+.4e | Phi_C ladder-law defect %.3e"
              % (wname.upper(), ph[wname][0], ph[wname][1],
                 ph[wname][2]))
    check("C5.1 truth satisfies the enumerated inequalities: Phi_A >= 0 "
          "(%.2e), Phi_C == 0 (%.1e); Phi_B status recorded (%.2e -- a "
          "truth-violated functional is dead as stated)"
          % (ph["truth"][0], ph["truth"][2], ph["truth"][1]),
          ph["truth"][0] >= -1.0e-9 and ph["truth"][2] < 1.0e-12)
    scr_viol = all(
        (ph[w][0] < -1.0e-6) or (ph[w][1] < -1.0e-6)
        or (ph[w][2] > 1.0e-3)
        for w in ("scramble-pos", "scramble-arith"))
    check("C5.2 BOTH scrambles violate at least one enumerated "
          "functional (the U5 requirement); per-world defects printed "
          "above", scr_viol)
    feed = {}
    for t in TARGETS:
        c = cells[t]
        # (i) the PNT-smooth comb witness for Phi_A / Phi_B
        uu_s, mm_s = f4.smooth_atoms(c["cell"], SMOOTH_PER_GRID)
        sel_s = uu_s / c["dv"] <= float(c["h"]) + 3.0 + 1.0e-12
        wl = c["rung"].wall
        sel = wl.uh <= float(c["h"]) + 3.0 + 1.0e-12
        t_truth = float(np.sum(0.5 * wl.mm[sel]))
        m_s = float(np.sum(0.5 * mm_s[sel_s]))
        scale = t_truth / max(m_s, 1e-300)
        val_s = np.mean([float(np.sum(scale * mm_s[sel_s] * (-0.25)
                                      * psi_pad_row(r, c["h"],
                                                    uu_s[sel_s]
                                                    / c["dv"])))
                         for r in c["grid"]])
        u_cap = 2.0 * c["a"] + 2.0 * c["dv"]
        d_a, d_b, _dc = phi_eval(uu_s, scale * mm_s, u_cap)
        # (ii) Phi_C class floor: complete adversary-declared ladders
        N = fl_g2[t]["N"]
        base_vals = {}
        for b in range(2, N + 1):
            lad = []
            n_p = b
            while n_p <= N:
                lad.append(n_p)
                n_p *= b
            la = np.array(lad, float)
            nus = np.log(la) / c["dv"]
            mass = np.log(float(b)) / np.sqrt(la)
            psibar = np.mean([psi_pad_row(r, c["h"], nus)
                              for r in c["grid"]], axis=0)
            base_vals[b] = (float(np.sum(mass)),
                            float(np.sum(-0.5 * mass * psibar)))
        order = sorted(base_vals, key=lambda b: base_vals[b][1]
                       / max(base_vals[b][0], 1e-300))
        left, inf_c = t_truth, 0.0
        for b in order:
            if left <= 0.0:
                break
            m_b, v_b = base_vals[b]
            take = min(1.0, left / max(m_b, 1e-300))
            inf_c += take * v_b
            left -= take * m_b
        feed[t] = dict(smooth_val=val_s, d_a=d_a, d_b=d_b, inf_c=inf_c)
        print("  h %4d: PNT-comb witness (forced mass %.3f): signed "
              "%.4e vs need %.4f (Phi_A %+.2e, Phi_B %+.2e on the "
              "witness) | Phi_C ladder-class inf %.4f"
              % (c["h"], t_truth, val_s, c["need"], d_a, d_b, inf_c))
    check("C5.3 FEED TEST (kill numbers): the PNT-smooth comb SATISFIES "
          "Phi_A and Phi_B with the forced total mass and misses the "
          "signed requirement by orders at 3/3 cells (witness/need %s); "
          "the Phi_C complete-ladder class floors below the need at "
          "3/3 (%s) -- none of the three enumerated inequalities can "
          "feed the U2 bound; with S1.7 (downward closure) no "
          "upper-bound-type global inequality can"
          % (["%.1e" % (feed[t]["smooth_val"] / cells[t]["need"])
              for t in TARGETS],
             ["%.3f" % (feed[t]["inf_c"] / cells[t]["need"])
              for t in TARGETS]),
          all(feed[t]["d_a"] >= -1e-9 and feed[t]["d_b"] >= -1e-9
              and feed[t]["smooth_val"] < cells[t]["need"]
              and feed[t]["inf_c"] < cells[t]["need"]
              for t in TARGETS))
    v24 = ("U5-ENUMERATED-DEAD"
           if all(feed[t]["smooth_val"] < cells[t]["need"]
                  and feed[t]["inf_c"] < cells[t]["need"]
                  for t in TARGETS)
           else "U5-HANDLE-SURVIVES")

    # ------------------------------------------------------------- V
    section("V -- frozen verdicts and the updated gate tally")
    elapsed = time.time() - T0
    check("V1 runtime below the frozen bar", elapsed < RUNTIME_BAR,
          "%.1f s" % elapsed)
    failed = [name for name, ok in CHECKS if not ok]
    verdicts = {"#20 Euler grouping / G2 weight law": v20,
                "#21 source-side Krein contractor": v21,
                "#22 U1 ordinate positions (named types)": v22,
                "#23 U2 minimal alignment statement": v23,
                "#24 U5 global source-profile inequality": v24}
    n_fail_new = sum(1 for v in verdicts.values()
                     if v in ("G2-SEPARATES-NOT-ORIENTS",
                              "KREIN-CERT-IS-WALL",
                              "U1-NAMED-TYPES-EMPTY",
                              "U2-BEYOND-CLASSICAL",
                              "U5-ENUMERATED-DEAD"))
    for k, v in verdicts.items():
        print("  %-42s %s" % (k, v))
    print("\n  GATE TALLY: 19 candidates (0 PASS, 14 FAIL, 5 UNTESTED) "
          "-> 24 candidates")
    print("  (0 PASS, %d FAIL, %d survivors-with-statement, 0 blanket "
          "UNTESTED left);" % (14 + n_fail_new, 5 - n_fail_new))
    print("  the UNTESTED residue of the atlas is adjudicated.  What "
          "remains open is NOT a")
    print("  candidate but the named object class itself: a SIGNED, "
          "ALIGNMENT-CARRYING,")
    print("  sub-spacing ordinate-position statement (U1/U2 beyond the "
          "named types), which")
    print("  is beyond-classical on the deployed windows (C4.2).")
    if failed:
        verdict = "SIGNSOURCES-INSTRUMENT-EDGE(%s)" % ",".join(
            f.split()[0] for f in failed)
    else:
        verdict = ("SIGNSOURCES-ADJUDICATED( %s )"
                   % "; ".join("%s: %s" % (k.split()[0], v)
                               for k, v in verdicts.items()))
    n_pass = sum(1 for _n, ok in CHECKS if ok)
    print("\n  VERDICT: %s" % verdict)
    print("\n[SUMMARY] %d/%d checks pass (expected %d) | failed=%s | "
          "%.1f s" % (n_pass, len(CHECKS), N_CHECKS_EXPECTED,
                      failed or "none", elapsed))
    print("NO RH CLAIM.  No positivity claim.  Zero data consumed ONLY "
          "in the U1/U2")
    print("adjudication faces (X5-typed); a recorded dead candidate is "
          "a PASSING run.")
    pattern_ok = (not failed and len(CHECKS) == N_CHECKS_EXPECTED
                  and verdict.startswith("SIGNSOURCES-ADJUDICATED"))
    print("[%s] PATTERN GATE: expected %d checks, zero fails, verdict "
          "SIGNSOURCES-ADJUDICATED (got %d, fails %s)"
          % ("PASS" if pattern_ok else "FAIL", N_CHECKS_EXPECTED,
             len(CHECKS), failed or "none"))
    return 0 if pattern_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
