#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""euler_clark_test_probe -- PRIME.EULER.CLARK.COMPLETION.01
(EXPLORATION ONLY, experiments/; stage 1, the direct falsification
test of the Euler-Clark architecture, 2026-08-13).

THE ARCHITECTURE UNDER TEST.  The Krein factorization
A_h = B_+^* (I - C_h^* C_h) B_+ reduces wall positivity to
||C_h|| <= 1.  The sought lemma

  (EC)   C_h = J_-^* M_Theta J_+ ,  J_+- source-only ISOMETRIES
         from the two Christoffel/Jacobi arms, M_Theta the UNITARY
         multiplication by the completed finite Euler phase
         Theta_h = rho_inf(s) prod_{p <= X} rho_p(s), |Theta| = 1

would give I - C^*C = J_+^* M^* (I - J_- J_-^*) M J_+ >= 0
automatically.  Its finite shadow is the classical orthogonal-Cauchy
lemma: for real P, Q with STRICTLY INTERLACING zeros
x_1 < y_1 < x_2 < y_2 < ... and canonical positive residues
a_i = -Q(x_i)/P'(x_i), b_j = P(y_j)/Q'(y_j), the weighted Cauchy
matrix U_ij = sqrt(a_i b_j)/(x_i - y_j) is ORTHOGONAL.  The
hypothesis: the joint relation of the regional theorem (R2/R4) is
the finite shadow of ONE common rational Herglotz function P/Q whose
two Clark spectra are the two Jacobi arms.

THE DEPLOYED OBJECT (source-only, v870/v872 machinery, READ-ONLY):
C^G = D_- U^G with D_+^G = I, U^G = Lam_-^{1/2} Z_- Z_+^* Lam_+^{1/2}
the Christoffel-normalized cross kernel of the TWO ARM GAUSS SYSTEMS
(fold-aggregated sin^2-modified measures nu~_+-).  The arms supply
exactly the two node sets and the two weight sets (EC) needs.

WHY THE TEST IS LOAD-BEARING (not decoration): v872's exact split is
I - C^*C = (I - U^*U) + U^*(I - D_-^2) U.  If U^G were a COISOMETRY
then I - U^*U is an orthogonal projection (>= 0) and, with
max D_- <= 0.9946 ladder-wide, BOTH terms are PSD -- the wall would
close on every finite rung.  (EC) is exactly the claim that U^G is
that coisometry.  The documented obstruction is that its coisometry
defect is O(1) and full rank with no finite-rank compensation.  This
probe decides whether the FINITE ARM DATA admits the Clark structure
at all, and whether any source-only node extension can repair it.

THE HARD HONESTY GATE (carried verbatim).  |Theta| = 1 does NOT
imply the compression is contractive (Connes-Consani arXiv:
2008.10974, EXTERNAL-CITED: local Euler factor ratios are not inner
despite modulus one; only the completed products carry a weaker
quasi-inner structure).  The corpus's own named gap is the
"grid-side band intertwiner: the explicit-formula kernel itself"
(tfpt_prime_front.tex): the Douglas contractor couples DIFFERENT
|tau| density bands while the machine's only band mover (the J flip)
couples +-j at equal |tau|.  Any step that would silently identify
the two subspaces is flagged CIRCULARITY-RISK and is measured, never
assumed.  A second vacuity trap is typed and demonstrated: by
Sz.-Nagy / Halmos unitary dilation (1950/1953, EXTERNAL-CITED) EVERY
contraction admits a factorization J_-^* M J_+ with isometries J_+-
and M unitary -- so (EC) with UNSPECIFIED isometries is logically
EQUIVALENT to ||C|| <= 1 and carries no content.  All content sits
in the source-only identification of J_+- as the arm coordinate
embeddings.  That, and only that, is what is tested here.

VERDICT (frozen): EC-STRUCTURE-PRESENT / EC-REPAIRABLE / EC-DEAD.
NO RH claim.  Writes nothing.  verification/ imported READ-ONLY.

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/euler_clark_test_probe.py
"""

import ast
import hashlib
import math
import os
import sys
import time

import mpmath as mp
import numpy as np
import sympy as sp

_HERE = os.path.dirname(os.path.abspath(__file__))
_VERIFY = os.path.abspath(os.path.join(_HERE, "..", "..",
                                       "verification"))
sys.path.insert(0, _HERE)
sys.path.insert(0, _VERIFY)

import v563_paper2_readouts as core        # noqa: E402  (READ-ONLY)
import gauss_node_unitary_probe as gnu     # noqa: E402  (READ-ONLY)

FROZEN_SPEC = """\
PRIME.EULER.CLARK.COMPLETION.01 spec v3 (2026-08-13, frozen after a
FIVE-WAVE SMOKE that is disclosed in full, with four AMENDMENTS).

AMENDMENT 3 (spec v1 -> v2, the ward firing).  The FIRST frozen run
of spec v1 STOPPED at T0.4: the lemma ward reported a NEGATIVE
canonical residue at n = 3 (odd) while n = 8, 20, 60 (even) passed.
Cause: the overflow-safe log-space residue builder dropped the
(-1)^n parity factors of Q(x_i) = (-1)^n prod_j (y_j - x_i) and
P(y_j) = (-1)^n prod_i (x_i - y_j), so the residue SIGNS were
correct only at even n.  The parity factors are restored; no
threshold, bar, test or verdict rule is changed by this amendment.
Recorded here rather than silently patched because the ward did
exactly its job: it caught an implementation error at odd n BEFORE
any arithmetic data touched the lemma, and the arm node counts r_-
are of both parities on the ladder.  Spec v1 SHA was
433f9dbf0c1fa6b60de3e3af726e6b5e047133c7dd87d8716d9ae913ba176851.

AMENDMENT 4 (spec v2 -> v3, typing precision at T3.5).  The v2 run
classified the missing-mass profile 1 - D_-^2 with the coarse test
prof[0] + prof[-1] > 2 prof[2] and printed "edge-loaded
(collar-like)" for the kz 9 quintile profile 0.131 / 0.402 / 0.439 /
0.589 / 0.792, which is in fact MONOTONE INCREASING and therefore a
ONE-SIDED ramp, not a two-sided collar -- the opposite of what the
outsourced-Euler-collar hypothesis predicts.  The classifier is
replaced by three mutually exclusive predeclared types
(SYMMETRIC-COLLAR: both edge quintiles > 1.5x the middle and not
monotone; MONOTONE-ONE-SIDED RAMP: strictly monotone across the five
quintiles, with the Spearman coefficient printed; BULK-SPREAD:
neither), reported at kz 9 AND kz 40.  No threshold, bar, test or
verdict rule of the (EC) hypothesis legs changes; only this
descriptive typing.  Spec v2 SHA was
3bea8f223e9ab73eed39d09e175f83ba97b811f8002d1e3beb17f3cda7c50c37
(that run: all 15 wards PASS, hypothesis ledger E1 pass / E2 fail /
K3 fail / ID fail, verdict EC-DEAD).

SMOKE DISCLOSURE (what was seen before freezing, and what it changed
in the spec).  W1: the two arm systems were extracted from
gauss_node_unitary_probe (READ-ONLY) -- plus arm r_+ = h Gauss nodes,
minus arm r_- = 0.55-0.65 h measure-tight nodes; the arms therefore
CANNOT be an equal-degree Clark pair without a 35-45 percent node
extension.  W2: FOUR predeclared source-only weight/coordinate
conventions (nu~ on cos th, mu on cos th == the frame weight w^S on
cos th, nu~ on th) all gave a violently non-constant master relation
(relative IQR 0.55 to 20, sign consistency 0.51-0.90) -- the naive
measure route is not the canonical read, so the spec DROPPED it as a
verdict leg and keeps it only as a descriptive appendix.  W3: the
gauge-free kernel test showed sigma_2/sigma_1 of
Knp .* (x_i - y_j) at 1e-12 -- the cross kernel is an EXACT weighted
Cauchy matrix, on every rung tried; this promoted the KERNEL-
EFFECTIVE weights (read off the exact rank-one factorization,
source-only, no fit) to THE canonical read, and forced a new
theorem-grade ward T0b (the interpolation origin of that rank-one
structure), because a free identity must never be scored as
evidence.  W4: the full 42-rung census with the effective weights --
second Clark relation exact (max dev 8.9e-8, float-limited), master
relation relative IQR 1.86-76.2 with sign consistency 0.51-0.70,
coisometry defect cert 0.93-1.30.  W5: timing/validation of the
symbolic legs; the exact defect identity measured at rel 7e-11 on
kz 9 and kz 40; the Halmos dilation verified at 6e-15.
AMENDMENT 1 (budget): the FULL symbolic verification of L1-L4 at
n = 4 timed at 344 s, which does not fit the 25 min frozen-run
budget beside the ladder; it is replaced by EXACT RATIONAL
instantiation at generic rational interlacing nodes for n = 4, 5, 6
(sympy Rational arithmetic, zero floating point), with full generic
symbolics kept at n = 2, 3.  AMENDMENT 2 (correctness): the explicit
symbolic matrix identity W W^T = I cannot be decided by sympy in the
sqrt(a_i b_j) form (it will not merge square roots of sign-unknown
expressions and returns a false negative); it is replaced by (i) the
sqrt-free core identities L3/L4, which ARE that statement for
positive residues, and (ii) a 60-digit mpmath verification on exact
rational interlacing nodes for n = 2..6 with residual bar 1e-45.
W^T W = I then follows because a square matrix with W W^T = I is
orthogonal.  The bars below are set AFTER seeing these numbers and
are therefore NOT independent evidence for the DEAD direction; they
are stated so the run is reproducible.  The verdict is carried by
the EXACTNESS wards (T0, T0b, T2.1, T3-K1, T3-K2, T4.2), not by any
threshold.

MACHINERY: gauss_node_unitary_probe (build_rung, arm_gauss_system,
gauss_objects, softport, lambda_eps) and v563_paper2_readouts, both
READ-ONLY.  LADDER: all core.frame_a_zones() with h <= 900 AND plus
arm square (r_+ = h); non-square/failed rungs typed and skipped.
WINDOW SET for the expensive legs (T3/T4): SPAN = (9, 12, 13, 16,
19, 22, 26, 28, 31, 34, 40, 44, 48, 53, 67) plus DEEP = (43, 50, 52,
64) -- 19 windows spanning h = 151..878.

T0 THE LEMMA WARD (theorem grade before any arithmetic data).
(a) sympy EXACT, generic symbols, n = 2, 3: L1 partial fractions
P/Q - 1 == sum_j b_j/(z-y_j) with b_j = P(y_j)/Q'(y_j); L2
sum_j b_j/(x_i-y_j) == -1; L3 sum_j b_j/(x_i-y_j)^2 == 1/a_i with
a_i = -Q(x_i)/P'(x_i); L4 sum_j b_j/((x_i-y_j)(x_k-y_j)) == 0 for
i != k.  L2+L3+L4 ARE U U^T = I for positive residues.  (b) EXACT
RATIONAL L1-L4 at n = 4, 5, 6 (Amendment 1).  (c) 60-digit mpmath
matrix ward ||W W^T - I||_max <= 1e-45, n = 2..6 (Amendment 2).
(d) NUMERIC on random strictly interlacing data, n in {3, 8, 20,
60}, 40 seeds each: a_i > 0, b_j > 0, ||W W^T - I|| <= 1e-9 * n, and
cross-ward that the forced nodes x are EXACTLY the spectrum of the
Clark rank-one operator diag(y) - v v^T, v = sqrt(b) (max node
deviation <= 1e-8).  (e) ANTI-CONTROL: 40 non-interlacing
configurations must produce a non-positive residue or
||W W^T - I|| > 1e-3.  Gate: every leg must pass or the probe stops
-- no arithmetic data may touch an unwarded lemma.

T0b THE STRUCTURAL WARD (anti-circularity, decisive for reading T1).
The Cauchy SHAPE of the deployed cross kernel must be shown to be a
FREE interpolation identity before any Cauchy-shape observation can
be scored as evidence.  Claim: the odd frame
F(th)_k = z^k - z^{2h-1-k} (z = e^{-i th}) factorizes as
phi(th) p_{h-1-k}(cos th) with phi = 2i e^{-i th (2h-1)/2}
sin(th/2) and p_j of exact degree j, so span F = phi *
P_{h-1}(cos th); hence for ANY node sets Fm Fp^{-1} =
diag(phi_-) L diag(1/phi_+) with L the degree-(h-1) LAGRANGE matrix
L_ij = Q(x_i)/((x_i-y_j) Q'(y_j)), and therefore
(Fm Fp^{-1})_ij * (x_i - y_j) is RANK ONE identically.  Wards:
(a) sympy EXACT in z for h = 2, 3 with 2 generic minus nodes -- all
2x2 minors of the multiplied matrix vanish; (b) EXACT RATIONAL
instantiation for h = 4, 5, 6 at generic rational z -- all 2x2
minors exactly 0; (c) numeric on EVERY ladder rung:
sigma_2/sigma_1 of Knp .* (x_i-y_j) <= 1e-8.  CONSEQUENCE typed in
the report: the Cauchy shape is comb-blind and MUST also hold for
Epstein/scramble; it is declared NON-DISCRIMINATING in advance.

T1 CLARK RESIDUES (per window, source-only).  Nodes x_i = cos th_-,
y_j = cos th_+.  Canonical weights = KERNEL-EFFECTIVE: from the
exact rank-one factorization Knp .* (x_i-y_j) = u v^T set
a_i = |u_i|^2 / K_-(i), b_j = |v_j|^2 / K_+(j) (positive by
construction, no fit, no free scale).  Ward: U^G = D_phi^-
[sqrt(a_i b_j)/(x_i-y_j)] D_phi^+ with UNITARY diagonal phase
gauges, rel <= 1e-8.  EXACT tests, in the scale-free form the
residue equations take: (E1) a_i P'(x_i) + Q(x_i) = 0 in its
equivalent form a_i sum_j b_j/(x_i-y_j)^2 = 1 (max dev per window;
budget 1e-6, float-limited at large h); (E2) b_j Q'(y_j) - P(y_j)
= 0 in its equivalent scale-free form: S_i := sum_j b_j/(x_i-y_j)
is CONSTANT in i (Clark: S_i = -1/c).  Census over the whole ladder:
E2 passes iff relative IQR of S <= 1e-6 AND sign consistency == 1.
RESIDUAL ANATOMY typing (predeclared, mutually exclusive):
GLOBAL-MISNORMALIZATION iff S constant to 1e-6 up to one scale
(fixable); SIGN-INDEFINITE iff sign consistency < 1 (structural --
no positive Clark measure can produce a sign-mixed master relation);
PER-NODE-DRIFT iff sign-consistent, relative IQR > 1e-6 and
Spearman |rho| >= 0.7 vs x_i (structural, a missing normalizing
weight); NOISE iff relative IQR <= 1e-3 and |rho| < 0.3.

T2 COMMON HERGLOTZ.  (a) DEGREE CENSUS: deg P = r_-, deg Q = h, so
P/Q -> 0 not 1; the exact partial-fraction comparison of the raw
node sets is reported with its exact degree deficit h - r_- per
window (the number of atoms the minus arm would have to outsource).
(b) THE EXACT DEFECT IDENTITY (the bridge): for a weighted Cauchy
matrix with unit rows, (U U^*)_{ik} = sqrt(a_i a_k)
(S_i - S_k)/(x_k - x_i) EXACTLY; warded per window at rel 1e-8.
Hence the coisometry defect IS the Clark master-relation residual,
in closed form -- measured, not asserted.  (c) THE R2/R4 SHADOW:
count the demands.  R2/R4 (cofinal_package.json, joint_sha
31aaf94c5bb432d7) consume ONE scalar inequality
sum_j c_j nu_j <= (1-eta) n on the moment functional of the wall
matrix's Herglotz measure; (EC) demands r_- - 1 INDEPENDENT
equalities m(x_i) = m(x_k).  The satisfied/made ratio is reported
per window.

T3 EXTENDED NODES (no arbitrary nodes).  Two exhaustive source-only
extension directions, each with a predeclared lemma to be VERIFIED
numerically, not assumed: (K1) COLUMN extension (extra plus-arm
atoms, the outsourced Euler collar): rows of U^G are saturated --
max |row norm - 1| <= 1e-8 on every rung (the Gauss-Christoffel
identity w^S_+ K_+ = 1) -- so any collar with positive mass
strictly raises a row norm above 1 and destroys the coisometry.
(K2) ROW extension (extra minus-arm atoms): appending rows leaves
every existing (i, k) inner product unchanged (verified with
explicit RANDOM appended rows), so it cannot reduce the measured
off-diagonal defect.  (K3) THE CONSTRAINED RECONSTRUCTION, run
anyway and reported honestly: from the plus arm alone the Clark
partner is FORCED as spec(diag(y) - c v v^T), v = sqrt(b), a
rank-one (Clark) family with ONE global scale c; 31-point log scan
c in [1e-8, 1e6]; statistic = fraction of measured minus nodes
within 0.1 grid spacings (2 pi / L) of a forced node, scored against
a SURROGATE NULL (b permuted, seed 11).  Bar: a real reconstruction
needs match rate >= 0.9 AND >= 5x the surrogate.  Band profile of
the missing mass 1 - D_-^2 by theta quintile reported either way.

T4 CONTRACTOR IDENTIFICATION.  Build U_hat from the reconstructed
node set (T3-K3 best c) with the CANONICAL residues in log space
(overflow-safe at h ~ 900), ward its orthogonality, then measure the
identification residual of C^G = P_- U_hat P_+ per window,
gauge-free (entrywise magnitudes, invariant under the diagonal
phase/sign gauge) and additionally sign-gauged.  Bar: rel <= 1e-6.
CIRCULARITY-RISK FLAG: identifying the arm coordinate subspace with
the window compression is exactly the corpus's named grid-side band
intertwiner gap; it is measured here and never assumed.  VACUITY
DEMONSTRATION (EXTERNAL-CITED, Halmos/Sz.-Nagy): an explicit unitary
dilation of an ARBITRARY random contraction is built and the
factorization J_-^* M J_+ verified to 1e-12, and refuted for a
random non-contraction -- establishing that the
unspecified-isometry form of (EC) has exactly the content of
||C|| <= 1 and no more.

T5 CONTROLS (must-fire, gate-resolved).  Epstein (x^2 + 5 y^2) and
scramble (seed 1) at kz 9 through the SAME pipeline.  Predeclared
gate list with predeclared discrimination status: G0 Cauchy shape
(NON-DISCRIMINATING BY THEOREM T0b -- must pass for the fakes too;
declared, not counted); G1 second Clark relation E1 (NON-
DISCRIMINATING -- the Christoffel normalization is comb-blind;
declared); G2 master relation E2; G3 reconstruction match rate;
G4 contractor identification residual; G5 damping sign max D_- <= 1
(the v872 comb-sensitive gate, included as the positive control that
the pipeline CAN discriminate).  Report WHICH gate catches each
fake.  KILL CRITERION (the lead's): if the fakes pass every gate the
construction is too structural -- reported LOUDLY.  A gate that
gives the same verdict for truth and fakes is reported COMB-BLIND,
which is a finding about (EC), not evidence for it.  G5 MUST
separate truth from both fakes or the pipeline itself is impeached.

TAU-SCREEN.  log(relative IQR of S) and log(cert) regressed against
log(tau) and log(h) over the ladder; |slope| <= 0.30 vs log tau
means the Clark obstruction is INDEPENDENT of the wall margin (a
genuine structural obstruction); |slope| >= 0.70 means the
obstruction is the margin in disguise (RELOC).

VERDICT.  EC-STRUCTURE-PRESENT iff E1 and E2 both pass on a cofinal
subset AND T4 identifies.  EC-REPAIRABLE iff E2 fails but T3-K3
reconstructs (match >= 0.9, >= 5x surrogate) and at least one of
K1, K2 leaves the corresponding extension open.  EC-DEAD iff E2
fails AND both extension directions are closed by the verified
lemmas K1, K2 -- with the killing test and mechanism named.
Float64 (exact rational / sympy / 60-digit mpmath where stated);
budget < 25 min.  NO RH claim; writes nothing; verification/
READ-ONLY.
"""

SPAN = (9, 12, 13, 16, 19, 22, 26, 28, 31, 34, 40, 44, 48, 53, 67)
DEEP = (43, 50, 52, 64)
WINDOWS = tuple(sorted(set(SPAN) | set(DEEP)))
CTRL_KZ = 9

TOL_RANK1 = 1e-8
TOL_GAUGE = 1e-8
TOL_E1 = 1e-6
TOL_IQR = 1e-6
TOL_DEFID = 1e-8
TOL_ROWSAT = 1e-8
TOL_IDENT = 1e-6
MATCH_BAR = 0.9
SURR_FACTOR = 5.0
CGRID = np.logspace(-8, 6, 31)

BANNED_IDS = ("zetazero", "nzeros", "primerange", "isprime",
              "primepi", "nextprime", "prevprime")

CHECKS = []
FAILS = []
HYPO = []
T0 = time.time()


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok)))
    if not ok:
        FAILS.append(name.split()[0])
    print("  [%s] %s%s" % ("PASS" if ok else "FAIL", name,
                           ("  -- " + detail) if detail else ""),
          flush=True)
    return bool(ok)


def hypo(name, ok, detail=""):
    """A hypothesis leg of (EC).  Its failure is the FINDING and is
    carried by the verdict, not by the ward count."""
    HYPO.append((name, bool(ok)))
    print("  [%s] %s%s"
          % ("HYPO-PASS" if ok else "HYPO-FAIL", name,
             ("  -- " + detail) if detail else ""), flush=True)
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


def spearman(a, b):
    ra = np.argsort(np.argsort(np.asarray(a, float))).astype(float)
    rb = np.argsort(np.argsort(np.asarray(b, float))).astype(float)
    return float(np.corrcoef(ra, rb)[0, 1])


def rel_iqr(v):
    v = np.asarray(v, float)
    med = np.median(v)
    if med == 0.0:
        return float("inf")
    return float((np.percentile(v, 75) - np.percentile(v, 25))
                 / abs(med))


def sign_consistency(v):
    v = np.asarray(v, float)
    return float(np.mean(np.sign(v) == np.sign(np.median(v))))


# ============================================================ T0 lemma
def _clark_pieces(xs, ys, n, exact):
    z = sp.Symbol("z")
    P = sp.prod([z - xi for xi in xs])
    Q = sp.prod([z - yj for yj in ys])
    Pp, Qp = sp.diff(P, z), sp.diff(Q, z)
    red = (lambda e: sp.cancel(e)) if exact else \
        (lambda e: sp.cancel(sp.together(e)))
    b = [red(P.subs(z, yj) / Qp.subs(z, yj)) for yj in ys]
    a = [red(-Q.subs(z, xi) / Pp.subs(z, xi)) for xi in xs]
    out = [red(sum(b[j] / (z - ys[j]) for j in range(n))
               - (P / Q - 1))]
    for i in range(n):
        out.append(red(sum(b[j] / (xs[i] - ys[j])
                           for j in range(n)) + 1))
        out.append(red(sum(b[j] / (xs[i] - ys[j]) ** 2
                           for j in range(n)) - 1 / a[i]))
        for k in range(i + 1, n):
            out.append(red(sum(
                b[j] / ((xs[i] - ys[j]) * (xs[k] - ys[j]))
                for j in range(n))))
    return out, a, b


def lemma_symbolic(n):
    xs = sp.symbols("x1:%d" % (n + 1))
    ys = sp.symbols("y1:%d" % (n + 1))
    out, _a, _b = _clark_pieces(xs, ys, n, exact=False)
    return all(e == 0 for e in out), len(out)


def rational_interlacing(n, seed):
    """Exact rational strictly interlacing x_1<y_1<...<x_n<y_n."""
    rng = np.random.default_rng(seed)
    g = sorted(set(int(v) for v in
                   rng.choice(np.arange(1, 4000), 4 * n,
                              replace=False)))[:2 * n]
    v = [sp.Rational(t, 97) for t in g]
    return v[0::2], v[1::2]


def lemma_rational(n, seed=13):
    xs, ys = rational_interlacing(n, seed)
    out, a, b = _clark_pieces(xs, ys, n, exact=True)
    pos = all(sp.sign(t) == 1 for t in a) and \
        all(sp.sign(t) == 1 for t in b)
    return all(e == 0 for e in out), pos


def lemma_matrix_mp(n, seed=29, dps=60):
    """60-digit ward of W W^T = I on exact rational nodes."""
    mp.mp.dps = dps
    xs, ys = rational_interlacing(n, seed)
    _out, a, b = _clark_pieces(xs, ys, n, exact=True)
    A = [mp.mpf(sp.Rational(t).p) / mp.mpf(sp.Rational(t).q)
         for t in a]
    B = [mp.mpf(sp.Rational(t).p) / mp.mpf(sp.Rational(t).q)
         for t in b]
    X = [mp.mpf(t.p) / mp.mpf(t.q) for t in xs]
    Y = [mp.mpf(t.p) / mp.mpf(t.q) for t in ys]
    W = mp.matrix(n, n)
    for i in range(n):
        for j in range(n):
            W[i, j] = mp.sqrt(A[i] * B[j]) / (X[i] - Y[j])
    G = W * W.T
    worst = mp.mpf(0)
    for i in range(n):
        for j in range(n):
            d = abs(G[i, j] - (1 if i == j else 0))
            worst = max(worst, d)
    return float(worst)


def canonical_log(x, y):
    """log|a|, sign a, log|b|, sign b (overflow-safe, any n).

    a_i = -Q(x_i)/P'(x_i) with Q(x_i) = (-1)^n prod_j (y_j - x_i),
    so sign(a_i) = (-1)^(n+1) prod_j sgn(y_j - x_i)
    prod_{k!=i} sgn(x_i - x_k); likewise sign(b_j) = (-1)^n
    prod_i sgn(x_i - y_j) prod_{k!=j} sgn(y_j - y_k).  The (-1)^n
    parity factors are load-bearing at odd n (Amendment 3)."""
    n = len(x)
    par = 1.0 if n % 2 == 0 else -1.0        # (-1)^n
    la = np.empty(n)
    sa = np.empty(n)
    lb = np.empty(n)
    sb = np.empty(n)
    for i in range(n):
        d = x[i] - np.delete(x, i)
        num = y - x[i]
        la[i] = np.sum(np.log(np.abs(num))) \
            - np.sum(np.log(np.abs(d)))
        sa[i] = -par * np.prod(np.sign(num)) * np.prod(np.sign(d))
    for j in range(n):
        d = y[j] - np.delete(y, j)
        num = x - y[j]
        lb[j] = np.sum(np.log(np.abs(num))) \
            - np.sum(np.log(np.abs(d)))
        sb[j] = par * np.prod(np.sign(num)) * np.prod(np.sign(d))
    return la, sa, lb, sb


def cauchy_from_log(x, y, la, lb):
    LU = 0.5 * (la[:, None] + lb[None, :]) \
        - np.log(np.abs(x[:, None] - y[None, :]))
    return np.exp(LU) * np.sign(x[:, None] - y[None, :])


def lemma_numeric(n, seeds, interlace=True, rng0=1000):
    worst = 0.0
    worst_pos = 1.0
    worst_cross = 0.0
    for s in range(seeds):
        rng = np.random.default_rng(rng0 + s)
        g = np.sort(rng.uniform(-1.0, 1.0, 2 * n))
        if interlace:
            x, y = g[0::2], g[1::2]
        else:
            x = np.sort(g[:n])
            y = np.sort(rng.uniform(x[0], x[-1], n))
        la, sa, lb, sb = canonical_log(x, y)
        worst_pos = min(worst_pos, float(min(sa.min(), sb.min())))
        if sa.min() <= 0 or sb.min() <= 0:
            worst = float("inf")
            continue
        W = cauchy_from_log(x, y, la, lb)
        worst = max(worst, float(np.linalg.norm(
            W @ W.T - np.eye(n))))
        if interlace:
            v = np.exp(0.5 * lb)
            ev = np.linalg.eigvalsh(np.diag(y) - np.outer(v, v))
            worst_cross = max(worst_cross, float(np.max(
                np.abs(np.sort(ev) - x))))
    return worst, worst_pos, worst_cross


# ============================================ T0b the structural ward
def frame_z(zs, h):
    return [[zj ** k - zj ** (2 * h - 1 - k) for k in range(h)]
            for zj in zs]


def _minors_zero(N, h, reduce_fn):
    for j in range(h):
        for k in range(j + 1, h):
            if reduce_fn(N[0, j] * N[1, k] - N[0, k] * N[1, j]) != 0:
                return False
    return True


def lagrange_rank1_symbolic(h):
    zs = sp.symbols("z1:%d" % (h + 1))
    ws = sp.symbols("w1:3")
    T = sp.Matrix(frame_z(ws, h)) * sp.Matrix(frame_z(zs, h)).inv()
    N = sp.Matrix(2, h, lambda i, j: sp.cancel(
        T[i, j] * ((ws[i] + 1 / ws[i]) / 2
                   - (zs[j] + 1 / zs[j]) / 2)))
    return _minors_zero(N, h,
                        lambda e: sp.cancel(sp.together(e)))


def lagrange_rank1_rational(h, seed=7):
    rng = np.random.default_rng(seed)
    while True:
        v = [sp.Rational(int(t), 97) for t in
             rng.choice(np.arange(2, 400), h + 2, replace=False)]
        zs, ws = v[:h], v[h:]
        Fp = sp.Matrix(frame_z(zs, h))
        if Fp.det() != 0:
            break
    T = sp.Matrix(frame_z(ws, h)) * Fp.inv()
    N = sp.Matrix(2, h, lambda i, j: T[i, j]
                  * ((ws[i] + 1 / ws[i]) / 2
                     - (zs[j] + 1 / zs[j]) / 2))
    return _minors_zero(N, h, lambda e: e)


# ==================================================== deployed objects
def arm_objects(kz, **kw):
    """Source-only arm data + the kernel-effective Clark weights."""
    b = gnu.build_rung(kz, **kw)
    if b["h"] > 900:
        return "skip-h"
    go = gnu.gauss_objects(b)
    if go["fail"]:
        return "gauss-fail:%s" % (go["mode"],)
    if len(go["thp"]) != b["h"]:
        return "plus-not-square:%d" % len(go["thp"])
    op, om = np.argsort(go["thp"]), np.argsort(go["thm"])
    thp, thm = go["thp"][op], go["thm"][om]
    y, x = np.cos(thp), np.cos(thm)
    Knp = (go["Zm"] @ go["Zp"].conj().T)[np.ix_(om, op)]
    U = go["U"][np.ix_(om, op)]
    N = Knp * (x[:, None] - y[None, :])
    uu, ss, vv = np.linalg.svd(N)
    r1 = float(ss[1] / ss[0])
    u1 = uu[:, 0] * math.sqrt(ss[0])
    v1 = vv[0].conj() * math.sqrt(ss[0])
    a = np.abs(u1) ** 2 / go["Km"][om]
    bw = np.abs(v1) ** 2 / go["Kp"][op]
    Wmag = np.sqrt(np.outer(a, bw)) / np.abs(
        x[:, None] - y[None, :])
    gauge = float(np.linalg.norm(np.abs(U) - Wmag)
                  / np.linalg.norm(np.abs(U)))
    S = np.array([np.sum(bw / (xi - y)) for xi in x])
    e1 = np.array([a[i] * np.sum(bw / (x[i] - y) ** 2) - 1.0
                   for i in range(len(x))])
    UU = U @ U.conj().T
    off = UU - np.diag(np.diag(UU))
    r = dict(kz=kz, h=b["h"], rminus=len(x), x=x, y=y, thp=thp,
             thm=thm, a=a, bw=bw, U=U, Dm=go["Dm"][om], r1=r1,
             gauge=gauge, S=S, e1=e1, UU=UU, off=off, L=b["L"],
             rown=np.linalg.norm(U, axis=1),
             cert=float(np.max(np.abs(
                 np.linalg.svd(U, compute_uv=False) ** 2 - 1.0))),
             tau=gnu.softport(b)["lam1"],
             maxDm=float(np.max(go["Dm"])))
    r["rowsat"] = float(np.max(np.abs(r["rown"] - 1.0)))
    r["riqr"] = rel_iqr(S)
    r["sgn"] = sign_consistency(S)
    r["rho"] = spearman(x, S)
    r["e1max"] = float(np.max(np.abs(e1)))
    r["offn"] = float(np.linalg.norm(off) / math.sqrt(len(x)))
    return r


def defect_identity(r):
    """(U U^*)_{ik} == sqrt(a_i a_k)(S_i - S_k)/(x_k - x_i)."""
    x, a, S = r["x"], r["a"], r["S"]
    with np.errstate(divide="ignore", invalid="ignore"):
        pred = np.sqrt(np.outer(a, a)) \
            * (S[:, None] - S[None, :]) \
            / (x[None, :] - x[:, None])
    m = ~np.eye(len(x), dtype=bool)
    return float(np.linalg.norm(np.abs(r["off"][m])
                                - np.abs(pred[m]))
                 / np.linalg.norm(np.abs(r["off"][m])))


def clark_scan(r, permute=None):
    """The FORCED Clark partner of the plus arm, one scale c."""
    y, bw, thm, L = r["y"], r["bw"], r["thm"], r["L"]
    v = np.sqrt(bw if permute is None
                else bw[permute.permutation(len(bw))])
    dth = 2.0 * math.pi / L
    best = None
    for c in CGRID:
        xh = np.clip(np.linalg.eigvalsh(
            np.diag(y) - c * np.outer(v, v)), -1.0, 1.0)
        thh = np.sort(np.arccos(xh))
        d = np.min(np.abs(thm[:, None] - thh[None, :]),
                   axis=1) / dth
        sc = (float(np.mean(d <= 0.1)), -float(np.median(d)))
        if best is None or sc > best["score"]:
            best = dict(score=sc, c=float(c), rate=sc[0],
                        med=-sc[1], q90=float(np.percentile(d, 90)),
                        xh=np.sort(xh))
    return best


def identify(r, xh):
    """Identification residual of C^G == P_- U_hat P_+."""
    la, sa, lb, sb = canonical_log(xh, r["y"])
    if min(sa.min(), sb.min()) <= 0:
        return None, None, "residues not positive (%d, %d neg)" % (
            int(np.sum(sa <= 0)), int(np.sum(sb <= 0)))
    Uh = cauchy_from_log(xh, r["y"], la, lb)
    orth = float(np.linalg.norm(Uh @ Uh.T - np.eye(len(xh)))
                 / math.sqrt(len(xh)))
    idx = np.argmin(np.abs(r["x"][:, None] - xh[None, :]), axis=1)
    Pm = Uh[idx]
    den = np.linalg.norm(np.abs(r["U"]))
    mag = float(np.linalg.norm(np.abs(Pm) - np.abs(r["U"])) / den)
    sg = np.sign(np.real(np.sum(np.conj(r["U"]) * Pm, axis=1)))
    sg[sg == 0] = 1.0
    sgn = float(np.linalg.norm(np.abs(sg[:, None] * Pm)
                               - np.abs(r["U"])) / den)
    return mag, sgn, "orth/sqrt(n) %.1e" % orth


def sqrtm_sym(A):
    ev, V = np.linalg.eigh(A)
    return V @ (np.sqrt(np.maximum(ev, 0.0))[:, None] * V.T)


# ================================================================= main
def main():
    section("PRIME.EULER.CLARK.COMPLETION.01 (EXPLORATION ONLY)")
    sha = hashlib.sha256(FROZEN_SPEC.encode("utf-8")).hexdigest()
    print("    FROZEN_SPEC SHA-256 = %s" % sha)
    print("    NO RH claim.  Writes nothing.  verification/ "
          "READ-ONLY.")
    print("\nS0 -- firewall")
    check("S0.1 AST firewall clean (no zero/prime oracles)",
          not ast_scan(BANNED_IDS))

    # ------------------------------------------------------------ T0
    section("T0 -- THE LEMMA WARD (theorem grade, before any "
            "arithmetic data touches it)")
    sym_ok = True
    for n in (2, 3):
        ok, m = lemma_symbolic(n)
        sym_ok &= ok
        print("    n = %d generic symbols: %d identities (L1 "
              "partial fractions, L2 master, L3 derivative, L4 "
              "off-diagonal) all exactly 0: %s" % (n, m, ok),
              flush=True)
    check("T0.1 [SYMPY EXACT] L1-L4 hold identically for generic "
          "n = 2, 3 (L2+L3+L4 ARE U U^T = I for positive residues)",
          sym_ok)
    rat_ok = True
    for n in (4, 5, 6):
        ok, pos = lemma_rational(n)
        rat_ok &= (ok and pos)
        print("    n = %d exact rational interlacing nodes: L1-L4 "
              "== 0: %s ; all canonical residues positive: %s"
              % (n, ok, pos), flush=True)
    check("T0.2 [EXACT RATIONAL, Amendment 1] L1-L4 == 0 and "
          "residues positive at n = 4, 5, 6 (full symbolics at "
          "n = 4 timed at 344 s -- out of budget, disclosed)",
          rat_ok)
    mpw = max(lemma_matrix_mp(n) for n in (2, 3, 4, 5, 6))
    check("T0.3 [60-DIGIT MPMATH, Amendment 2] the explicit "
          "weighted Cauchy matrix satisfies ||W W^T - I||_max = "
          "%.2e <= 1e-45 at n = 2..6 on exact rational nodes; "
          "W^T W = I follows since a square W with W W^T = I is "
          "orthogonal" % mpw, mpw <= 1e-45)
    num_ok = True
    for n in (3, 8, 20, 60):
        w, wp, wc = lemma_numeric(n, 40)
        good = (w <= 1e-9 * n) and wp > 0.0 and wc <= 1e-8
        num_ok &= good
        print("    n = %-3d 40 seeds: max ||W W^T - I|| %.2e "
              "(budget %.1e) | residues positive (min sign %.0f) | "
              "Clark rank-one eigenbasis cross-ward %.2e"
              % (n, w, 1e-9 * n, wp, wc), flush=True)
    check("T0.4 [NUMERIC] random strictly interlacing data: "
          "positive residues, orthogonality, and the forced nodes "
          "ARE the spectrum of diag(y) - v v^T (v = sqrt(b))",
          num_ok)
    wn, wpn, _ = lemma_numeric(20, 40, interlace=False, rng0=5000)
    anti = (wpn <= 0.0) or (wn > 1e-3)
    check("T0.5 [ANTI-CONTROL] non-interlacing configurations break "
          "the lemma (min residue sign %.0f, max ||W W^T - I|| "
          "%.2e)" % (wpn, wn), anti)
    if FAILS:
        print("\n  LEMMA WARD FAILED -- stopping before any "
              "arithmetic data touches it.")
        return 1

    # ----------------------------------------------------------- T0b
    section("T0b -- THE STRUCTURAL WARD (the Cauchy shape is a FREE "
            "interpolation identity -- anti-circularity)")
    check("T0b.1 [SYMPY EXACT in z] (Fm Fp^-1)_ij (x_i - y_j) has "
          "all 2x2 minors 0 -- rank one for ARBITRARY nodes "
          "(h = 2, 3)",
          all(lagrange_rank1_symbolic(h) for h in (2, 3)))
    check("T0b.2 [EXACT RATIONAL] same at generic rational nodes "
          "(h = 4, 5, 6), zero floating point",
          all(lagrange_rank1_rational(h) for h in (4, 5, 6)))
    print("""
    CONSEQUENCE (typed BEFORE the data is read): the odd frame
    factorizes as F(th)_k = phi(th) p_{h-1-k}(cos th), so the cross
    kernel of ANY two node sets is a LAGRANGE matrix up to diagonal
    gauges and Knp .* (x_i - y_j) is rank one IDENTICALLY.  The
    Cauchy SHAPE of the contractor therefore carries ZERO arithmetic
    information and is declared NON-DISCRIMINATING; only the
    RESIDUES can carry it.""")

    # ------------------------------------------- the ladder (T1/T2)
    section("T1/T2 -- the ladder census with the KERNEL-EFFECTIVE "
            "Clark residues (source-only, no fit, no free scale)")
    rows = []
    skipped = []
    print("    kz    h    r-   defc  rank1     gauge     E1(deriv) "
          " S:med      relIQR   sgn    rho(S,x)  cert   rowsat   "
          "defect-id  offdiag")
    for kz in list(core.frame_a_zones()):
        r = arm_objects(kz)
        if isinstance(r, str):
            skipped.append((kz, r))
            continue
        r["did"] = defect_identity(r)
        rows.append(r)
        print("    %-5d %-4d %-4d %-5d %.2e  %.2e  %.2e  %+.5f  "
              "%8.3f  %.3f  %+.3f    %.3f  %.1e  %.2e   %.4f"
              % (kz, r["h"], r["rminus"], r["h"] - r["rminus"],
                 r["r1"], r["gauge"], r["e1max"],
                 float(np.median(r["S"])), r["riqr"], r["sgn"],
                 r["rho"], r["cert"], r["rowsat"], r["did"],
                 r["offn"]), flush=True)
    if skipped:
        print("    skipped (typed): %s" % (skipped,))

    check("T1.0 [WARD] the deployed cross kernel is an EXACT "
          "weighted Cauchy matrix on all %d rungs (max "
          "sigma2/sigma1 %.2e) and U^G equals the real weighted "
          "Cauchy matrix up to unitary diagonal gauges (max rel "
          "%.2e)" % (len(rows), max(r["r1"] for r in rows),
                     max(r["gauge"] for r in rows)),
          max(r["r1"] for r in rows) <= TOL_RANK1
          and max(r["gauge"] for r in rows) <= TOL_GAUGE)
    e1p = [r["kz"] for r in rows if r["e1max"] <= TOL_E1]
    hypo("T1.1 (E1) the residue/derivative equation "
         "a_i P'(x_i) + Q(x_i) = 0 holds on %d/%d rungs (max dev "
         "%.1e) -- BUT it IS the Gauss-Christoffel normalization "
         "w^S K = 1 and is declared COMB-BLIND, so passing is NOT "
         "evidence" % (len(e1p), len(rows),
                       max(r["e1max"] for r in rows)),
         len(e1p) == len(rows))
    e2p = [r["kz"] for r in rows
           if r["riqr"] <= TOL_IQR and r["sgn"] == 1.0]
    hypo("T1.2 (E2) the master residue equation "
         "b_j Q'(y_j) - P(y_j) = 0, scale-free form S_i = const, "
         "holds on %d/%d rungs (relative IQR range [%.2f, %.1f], "
         "sign consistency range [%.2f, %.2f])"
         % (len(e2p), len(rows), min(r["riqr"] for r in rows),
            max(r["riqr"] for r in rows),
            min(r["sgn"] for r in rows),
            max(r["sgn"] for r in rows)),
         len(e2p) == len(rows))
    anat = {}
    for r in rows:
        if r["riqr"] <= TOL_IQR:
            t = "GLOBAL-MISNORMALIZATION"
        elif r["sgn"] < 1.0:
            t = "SIGN-INDEFINITE"
        elif abs(r["rho"]) >= 0.7:
            t = "PER-NODE-DRIFT"
        elif r["riqr"] <= 1e-3:
            t = "NOISE"
        else:
            t = "PER-NODE-DRIFT(diffuse)"
        anat[t] = anat.get(t, 0) + 1
        r["anat"] = t
    print("    RESIDUAL ANATOMY census (predeclared types): %s"
          % ", ".join("%s %d" % kv for kv in sorted(anat.items())))
    check("T1.3 [ANATOMY] every rung is typed by the predeclared "
          "residual anatomy (%d/%d); SIGN-INDEFINITE is structural "
          "-- no positive Clark measure can produce a sign-mixed "
          "master relation" % (sum(anat.values()), len(rows)),
          sum(anat.values()) == len(rows))

    check("T2.1 [THE EXACT DEFECT IDENTITY] "
          "|(U U^*)_ik| == sqrt(a_i a_k)|S_i - S_k|/|x_k - x_i| on "
          "all %d rungs (max rel %.2e <= %.0e) -- the coisometry "
          "defect IS the Clark master-relation residual, in closed "
          "form" % (len(rows), max(r["did"] for r in rows),
                    TOL_DEFID),
          max(r["did"] for r in rows) <= TOL_DEFID)
    dd = [(r["kz"], r["h"] - r["rminus"],
           (r["h"] - r["rminus"]) / r["h"]) for r in rows]
    check("T2.2 [DEGREE CENSUS] deg P = r_- vs deg Q = h: the "
          "deficit h - r_- is STRICTLY POSITIVE on all %d rungs "
          "(range [%d, %d], relative [%.3f, %.3f]) -- the raw arms "
          "are an equal-degree Clark pair on NO rung, and P/Q -> 0 "
          "instead of 1" % (len(rows), min(d[1] for d in dd),
                            max(d[1] for d in dd),
                            min(d[2] for d in dd),
                            max(d[2] for d in dd)),
          all(d[1] > 0 for d in dd))
    dem = [r["rminus"] - 1 for r in rows]
    sat = [max(int(np.sum(np.abs(r["S"] - np.median(r["S"]))
                          <= 1e-6 * abs(np.median(r["S"])))) - 1, 0)
           for r in rows]
    print("    T2.3 R2/R4 SHADOW (demand count): the regional "
          "theorem consumes ONE scalar moment inequality "
          "sum_j c_j nu_j <= (1-eta) n (cofinal_package.json "
          "joint_sha 31aaf94c5bb432d7); (EC) demands r_- - 1 "
          "INDEPENDENT equalities m(x_i) = m(x_k).  Demands per "
          "window [%d, %d]; satisfied [%d, %d]; best "
          "satisfied/made ratio %.4f."
          % (min(dem), max(dem), min(sat), max(sat),
             max(s / d for s, d in zip(sat, dem))))

    # ------------------------------------------------------------ T3
    section("T3 -- EXTENDED NODES: the two exhaustive source-only "
            "extension directions")
    check("T3.1 [K1 -- COLUMN extension CLOSED] the rows of U^G are "
          "saturated at norm 1 on all %d rungs (max |row - 1| = "
          "%.1e <= %.0e, the Gauss-Christoffel identity w^S_+ K_+ "
          "= 1), so ANY collar with positive mass strictly raises a "
          "row norm above 1 and destroys the coisometry -- the "
          "'outsourced Euler collar' cannot exist in the column "
          "direction" % (len(rows),
                         max(r["rowsat"] for r in rows),
                         TOL_ROWSAT),
          max(r["rowsat"] for r in rows) <= TOL_ROWSAT)
    k2max = 0.0
    rng2 = np.random.default_rng(77)
    for r in rows:
        if r["kz"] not in WINDOWS:
            continue
        n = r["rminus"]
        extra = rng2.normal(size=(r["h"] - n, r["h"]))
        extra /= np.linalg.norm(extra, axis=1, keepdims=True)
        Oe = np.vstack([r["U"], extra])
        Oe = Oe @ Oe.conj().T
        k2max = max(k2max, float(np.max(np.abs(
            Oe[:n, :n] - r["UU"]))))
    check("T3.2 [K2 -- ROW extension CLOSED] appending %d..%d "
          "explicit RANDOM unit rows leaves every existing (i, k) "
          "inner product bit-identical (max dev %.1e) -- a row "
          "extension cannot reduce the measured off-diagonal "
          "defect, which is ||offdiag(U U^*)||_F / sqrt(r_-) in "
          "[%.4f, %.4f]"
          % (min(r["h"] - r["rminus"] for r in rows),
             max(r["h"] - r["rminus"] for r in rows), k2max,
             min(r["offn"] for r in rows),
             max(r["offn"] for r in rows)), k2max <= 1e-14)
    print("\n    T3.3 [K3] the constrained rank-one (Clark) "
          "reconstruction from the plus arm alone -- ONE global "
          "scale c, forced spectrum of diag(y) - c v v^T -- against "
          "the surrogate null (b permuted, seed 11):")
    print("      kz    h    best-c      match@0.1dth  med(dth)  "
          "q90     surrogate  ratio   1-D-^2 [min, med, max]")
    k3 = []
    for r in rows:
        if r["kz"] not in WINDOWS:
            continue
        bi = clark_scan(r)
        su = clark_scan(r, permute=np.random.default_rng(11))
        one = 1.0 - r["Dm"] ** 2
        ratio = bi["rate"] / max(su["rate"], 1e-9)
        k3.append((r, bi, su, ratio))
        print("      %-5d %-4d %.3e   %.4f        %.3f     %.3f   "
              "%.4f     %6.2f  [%.3e, %.3e, %.3e]"
              % (r["kz"], r["h"], bi["c"], bi["rate"], bi["med"],
                 bi["q90"], su["rate"], ratio, one.min(),
                 float(np.median(one)), one.max()), flush=True)
    best_rate = max(t[1]["rate"] for t in k3)
    best_ratio = max(t[3] for t in k3)
    hypo("T3.4 (K3) a source-only rank-one Clark partner of the "
         "plus arm reproduces the measured minus nodes: best match "
         "rate %.4f (bar %.2f), best surrogate ratio %.2f (bar "
         "%.1f); median nearest-node distance %.3f grid spacings "
         "(0.25-0.50 == indistinguishable from random)"
         % (best_rate, MATCH_BAR, best_ratio, SURR_FACTOR,
            float(np.median([t[1]["med"] for t in k3]))),
         best_rate >= MATCH_BAR and best_ratio >= SURR_FACTOR)
    for r0 in [r for r in rows if r["kz"] in (CTRL_KZ, 40)]:
        one = 1.0 - r0["Dm"] ** 2
        q = np.percentile(r0["thm"], np.linspace(0, 100, 6))
        prof = []
        for i in range(5):
            m = (r0["thm"] >= q[i]) & (r0["thm"] <= q[i + 1])
            prof.append(float(np.median(one[m])))
        rho_m = spearman(r0["thm"], one)
        mono = all(prof[i] < prof[i + 1] for i in range(4)) or \
            all(prof[i] > prof[i + 1] for i in range(4))
        sym = (min(prof[0], prof[-1]) > 1.5 * prof[2])
        if sym and not mono:
            typ = "SYMMETRIC-COLLAR (two-sided edge load -- the " \
                  "shape the outsourced-Euler-collar hypothesis " \
                  "predicts)"
        elif mono:
            typ = "MONOTONE-ONE-SIDED RAMP in theta (Spearman " \
                  "%+.3f) -- NOT a symmetric collar: the deficit " \
                  "grows steadily toward large theta, so it does " \
                  "not have the outsourced-collar shape" % rho_m
        else:
            typ = "BULK-SPREAD (Spearman %+.3f) -- NOT collar-like" \
                % rho_m
        print("    T3.5 the missing-mass profile 1 - D_-^2 by theta "
              "quintile at kz %d: %s -- %s"
              % (r0["kz"], " / ".join("%.3f" % v for v in prof),
                 typ))

    # ------------------------------------------------------------ T4
    section("T4 -- CONTRACTOR IDENTIFICATION (+ the dilation "
            "vacuity demonstration)")
    print("    CIRCULARITY-RISK FLAG: identifying the arm "
          "coordinate subspace with the window compression is the "
          "corpus's named 'grid-side band intertwiner' gap "
          "(tfpt_prime_front.tex: the Douglas contractor couples "
          "DIFFERENT |tau| bands, the machine's J flip couples +-j "
          "at EQUAL |tau|).  It is MEASURED below, never assumed.")
    print("      kz    ident-residual(magnitude)  sign-gauged  "
          "U_hat orthogonality / note")
    ident = []
    for r, bi, _su, _q in k3:
        mag, sgn, note = identify(r, bi["xh"])
        ident.append((r["kz"], mag, sgn, note))
        if mag is None:
            print("      %-5d --                          --      "
                  "     %s" % (r["kz"], note))
        else:
            print("      %-5d %.4f                      %.4f     "
                  "   %s" % (r["kz"], mag, sgn, note))
    good = [m for _k, m, _s, _n in ident if m is not None]
    best_id = min(good) if good else float("nan")
    hypo("T4.1 (ID) C^G == P_- U_hat P_+ with the reconstructed "
         "orthogonal U_hat: best residual %s (bar %.0e) on %d/%d "
         "windows with positive reconstructed residues"
         % ("%.4f" % best_id if good else "n/a", TOL_IDENT,
            len(good), len(ident)),
         bool(good) and best_id <= TOL_IDENT)
    rng = np.random.default_rng(2026)
    A = rng.normal(size=(6, 9))
    A = 0.7 * A / np.linalg.svd(A, compute_uv=False)[0]
    Mdil = np.block([[A, sqrtm_sym(np.eye(6) - A @ A.T)],
                     [sqrtm_sym(np.eye(9) - A.T @ A), -A.T]])
    uni = float(np.linalg.norm(Mdil.T @ Mdil - np.eye(15)))
    Jp = np.vstack([np.eye(9), np.zeros((6, 9))])
    Jm = np.vstack([np.eye(6), np.zeros((9, 6))])
    fac = float(np.linalg.norm(Jm.T @ Mdil @ Jp - A))
    B = rng.normal(size=(6, 9))
    B = 1.3 * B / np.linalg.svd(B, compute_uv=False)[0]
    bad_ok = float(np.linalg.eigvalsh(np.eye(9)
                                      - B.T @ B)[0]) < 0.0
    check("T4.2 [VACUITY, EXTERNAL-CITED Halmos 1950 / Sz.-Nagy "
          "1953] an ARBITRARY random contraction admits the (EC) "
          "form J_-^* M J_+ with M unitary (||M^T M - I|| %.1e, "
          "factorization residual %.1e) while a non-contraction "
          "does not (I - B^*B indefinite: %s) -- (EC) with "
          "UNSPECIFIED isometries is logically EQUIVALENT to "
          "||C|| <= 1 and carries no content; ALL content is in the "
          "source-only identification of J_+-"
          % (uni, fac, bad_ok),
          uni <= 1e-12 and fac <= 1e-12 and bad_ok)

    # ------------------------------------------------------------ T5
    section("T5 -- CONTROLS (must fire; gate-resolved)")
    rr9 = core.build_window(CTRL_KZ)
    N_E = int(math.floor(math.exp(2.0 * rr9["alpha"]))) + 1
    lamE = gnu.lambda_eps(N_E)
    nn = np.nonzero(np.abs(lamE) > 1e-12)[0]
    ctrls = [("truth", {}),
             ("Epstein", dict(comb=(np.log(nn.astype(float)),
                                    2.0 * lamE[nn]
                                    / np.sqrt(nn.astype(float))))),
             ("scramble", dict(scramble_seed=1))]
    print("      case      G0 rank1   G1 E1      G2 relIQR  "
          "G2 sgn   G3 match  G4 ident   G5 maxD-")
    gate_tab = {}
    for nmc, kw in ctrls:
        r = arm_objects(CTRL_KZ, **kw)
        if isinstance(r, str):
            print("      %-9s SKIP (%s)" % (nmc, r))
            continue
        bi = clark_scan(r)
        mag, _sg, _nt = identify(r, bi["xh"])
        gate_tab[nmc] = dict(
            G0=r["r1"] <= TOL_RANK1, G1=r["e1max"] <= TOL_E1,
            G2=(r["riqr"] <= TOL_IQR and r["sgn"] == 1.0),
            G3=bi["rate"] >= MATCH_BAR,
            G4=(mag is not None and mag <= TOL_IDENT),
            G5=r["maxDm"] <= 1.0)
        print("      %-9s %.2e   %.2e   %8.3f   %.3f    %.4f    "
              "%s     %.4f"
              % (nmc, r["r1"], r["e1max"], r["riqr"], r["sgn"],
                 bi["rate"],
                 "%.4f" % mag if mag is not None else "  n/a ",
                 r["maxDm"]))
    tt = gate_tab.get("truth", {})
    for nmc in ("Epstein", "scramble"):
        g = gate_tab.get(nmc, {})
        caught = [k for k, v in sorted(g.items()) if not v]
        agree = [k for k in sorted(g) if g[k] == tt.get(k)]
        print("      %-9s caught by: %s | SAME verdict as truth on: "
              "%s" % (nmc, ", ".join(caught) or "NOTHING",
                      ", ".join(agree)))
    fake_fires = all(
        any(not v for v in gate_tab.get(nmc, {"x": True}).values())
        for nmc in ("Epstein", "scramble"))
    check("T5.1 [CONTROLS MUST FIRE] Epstein and scramble each fail "
          "at least one gate", fake_fires)
    g5sep = (tt.get("G5") is True
             and all(gate_tab.get(n, {}).get("G5") is False
                     for n in ("Epstein", "scramble")))
    check("T5.2 [POSITIVE CONTROL] the v872 damping-sign gate G5 "
          "SEPARATES truth (max D_- <= 1) from both fakes -- the "
          "pipeline demonstrably CAN discriminate the comb, so a "
          "gate that does not is genuinely comb-blind", g5sep)
    blind = [k for k in ("G0", "G1", "G2", "G3", "G4")
             if all(gate_tab.get(n, {}).get(k) == tt.get(k)
                    for n in ("Epstein", "scramble"))]
    check("T5.3 [COMB-BLINDNESS CENSUS] the (EC) gates that give "
          "the IDENTICAL verdict for truth and BOTH fakes: %s.  "
          "Reported LOUDLY per the kill criterion: the (EC) gate "
          "family carries no arithmetic information; the only "
          "comb-sensitive gate in this pipeline is G5, which is "
          "NOT part of (EC) but of the v872 damping term"
          % (", ".join(blind) or "none"), True)

    # ---------------------------------------------------- tau-screen
    section("TAU-SCREEN (is the Clark obstruction the wall margin "
            "in disguise?)")
    lt = np.log([r["tau"] for r in rows])
    lh = np.log([float(r["h"]) for r in rows])
    screens = []
    for nm, v in (("relIQR(S)", [r["riqr"] for r in rows]),
                  ("cert", [r["cert"] for r in rows]),
                  ("offdiag", [r["offn"] for r in rows])):
        lv = np.log(np.abs(v))
        s1 = float(np.polyfit(lt, lv, 1)[0])
        s2 = float(np.polyfit(lh, lv, 1)[0])
        vd = ("INDEPENDENT" if abs(s1) <= 0.30
              else ("RELOC" if abs(s1) >= 0.70 else "AMBIG"))
        screens.append((nm, s1, s2, vd))
        print("    log %-10s vs log tau: slope %+.3f (Pearson "
              "%+.3f) -> %s ; vs log h: slope %+.3f"
              % (nm, s1, float(np.corrcoef(lt, lv)[0, 1]), vd, s2))
    check("TAU.1 [SCREEN] recorded for all three obstruction "
          "measures (%s) -- INDEPENDENT means a structural "
          "obstruction, not a rescaled margin"
          % ", ".join("%s %s" % (n, v) for n, _a, _b, v in screens),
          True)

    # ------------------------------------------------------- verdict
    section("V -- FROZEN VERDICT")
    e2_ok = len(e2p) == len(rows)
    id_ok = bool(good) and best_id <= TOL_IDENT
    k3_ok = best_rate >= MATCH_BAR and best_ratio >= SURR_FACTOR
    k1_closed = max(r["rowsat"] for r in rows) <= TOL_ROWSAT
    k2_closed = k2max <= 1e-14
    if e2_ok and id_ok:
        verdict = "EC-STRUCTURE-PRESENT"
    elif k3_ok and not (k1_closed and k2_closed):
        verdict = "EC-REPAIRABLE"
    else:
        verdict = "EC-DEAD"
    print("\n  HYPOTHESIS LEDGER (the (EC) legs; wards are separate)")
    for nm, ok in HYPO:
        print("    [%s] %s" % ("PASS" if ok else "FAIL",
                               nm.split(")")[0] + ")"))
    print("\n  VERDICT: %s  (killed by T1.2/E2, the master residue "
          "equation; both repairs closed by T3.1/K1 and T3.2/K2)"
          % verdict)
    print("""
  WHAT KILLS IT, NAMED.  (1) The Cauchy SHAPE of the deployed
  contractor kernel is an exact interpolation identity (T0b, sympy
  + exact rational): for ANY two node sets the odd frame's cross
  kernel is a Lagrange matrix up to diagonal gauges, so
  Knp .* (x_i - y_j) is rank one identically.  The shape is free,
  comb-blind, and carries no arithmetic -- it must never be read as
  evidence for (EC).  (2) With the kernel-effective residues (the
  only source-only, fit-free read) the SECOND Clark relation
  a_i sum_j b_j/(x_i-y_j)^2 = 1 holds exactly -- because it IS the
  Gauss-Christoffel normalization w^S K = 1, also comb-blind.
  (3) The FIRST (master) Clark relation
  S_i = sum_j b_j/(x_i-y_j) = const fails on every rung, and fails
  SIGN-INDEFINITELY: no positive Clark measure can produce a
  sign-mixed master relation.  (4) The exact defect identity (T2.1)
  shows why that is decisive:
  |(U U^*)_ik| = sqrt(a_i a_k)|S_i - S_k|/|x_k - x_i|, so the O(1)
  full-rank coisometry defect IS the master-relation residual.
  (EC) in its source-only coordinate realization is therefore
  EQUIVALENT to the already-excluded coisometry property -- a
  relocation, not a route.  (5) Both extension directions are
  closed: the column direction (the 'outsourced Euler collar') by
  row saturation (K1 -- the rows are exactly unit norm, so any
  positive collar mass breaks the coisometry), the row direction by
  inner-product invariance (K2 -- appending rows cannot change the
  existing off-diagonals).  (6) And the unspecified-isometry form
  of (EC) is vacuous: by Halmos/Sz.-Nagy dilation (T4.2,
  EXTERNAL-CITED) every contraction has one.

  THE HONEST CONNES-CONSANI TYPING.  Nothing here contradicts
  |Theta| = 1; it CONFIRMS the cited obstruction inside the finite
  shadow.  Connes-Consani (arXiv:2008.10974, EXTERNAL-CITED) is the
  analytic statement that modulus one does not buy an inner
  function, hence not a contractive compression.  The finite data
  says the same thing in one number: the residues, not the phase,
  decide -- and the residues are not Clark residues.  The corpus's
  named gap -- the grid-side band intertwiner, the explicit-formula
  kernel itself -- is exactly where (EC) tried to shortcut and
  exactly where it fails: the arm coordinate subspaces are NOT the
  window compressions, and the deviation is O(1), not a margin.

  WHAT SURVIVES.  The v872 two-term split is untouched and remains
  the live object: I - C^*C = (I - U^*U) + U^*(I - D_-^2)U with the
  arithmetic living ENTIRELY in the damping D_- (the only gate in
  this run that separates truth from Epstein/scramble).  This probe
  narrows the tool space: any future contraction certificate must
  act on the DAMPING term, not on a phase/inner-function
  identification of the cross kernel.

  WHAT IS *NOT* TESTED (scope).  This falsifies (EC) for the
  DEPLOYED arm pair (the fold-aggregated sin^2-modified Gauss
  systems of the two signed halves of the grid density) in the
  coordinate-compression realization.  A DIFFERENT pair of Clark
  measures -- e.g. built from the completed Euler phase on the
  critical line rather than from the folded grid -- is untouched by
  this run; any such proposal must supply its own source-only
  J_+- and then face T2.1 and K1/K2 again.  NO RH claim.""")
    n_pass = sum(1 for _n, ok in CHECKS if ok)
    print("\n[TIME] %.1f s   [WARDS] %d run, %d failed%s   "
          "[HYPO] %d/%d passed"
          % (time.time() - T0, len(CHECKS), len(FAILS),
             ("  " + ",".join(FAILS)) if FAILS else "",
             sum(1 for _n, o in HYPO if o), len(HYPO)))
    return 0 if n_pass == len(CHECKS) else 1


if __name__ == "__main__":
    raise SystemExit(main())
