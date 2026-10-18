#!/usr/bin/env python3
"""v636 -- PRIME.PCONSTRUCT.01: P as an explicit operator construction.

Goal: upgrade the v624 congruence matrix P = [[3,0,0],[3,0,2],[-1,1,-1]]
(P^T J_det P = J_fix exactly, det P = -6) from "found matrix" to
"constructed map".

Established context (READ-ONLY: predecessor sandbox probe
p_canonicity_hodge_fine_probe.py, and verification/ v600/v604/v624/v627):
  * J_det = [[0,1,0],[1,0,0],[0,0,-2]] is the polarization of det on
    Sym^2 (y = (S11,S22,S12), y^T J_det y = 2 det S);
  * J_fix = [[16,2,4],[2,-2,2],[4,2,-2]] is the cover polarization on
    the saturated R-fixed lattice in the v604 basis (det 72);
  * (C_U, C_V) are the integer restrictions of the compiler pair to the
    fixed lattice (v600 J3, copied-matrix guarded below);
  * predecessor results: P is NOT in the Q-span of the 7-word algebra of
    (C_U, C_V); P is the unique minimal-Frobenius / operator-compatible
    class in the [-4,4] census (40 solutions) modulo the order-8
    prime-side symmetry group G8.  The deck (omega-multiplication) does
    NOT restrict to the fixed lattice (it is omega-semilinear w.r.t. R),
    so the literal word-algebra form of the task's candidate (1) stays
    negative -- this probe executes the eigenframe variant instead.

Construction route executed here (task candidates (1)+(2) merged):
  A2  the eigenframe of C_V (eigenvalues 0,1,2) is canonical operator
      data on the cover side;
  A3  null-cone census: the primitive isotropic rays of J_fix of the two
      lowest heights are EXACTLY (ker C_V, fix C_V) -- the operator
      characterization of the minimal null data;
  A4  P transports this frame to canonical rank-one (isotropic) rays of
      the prime-side det form, grading-preservingly on the two lowest
      height classes;
  A5  the transported operators P C_V P^-1, P C_U P^-1 are integer;
      the gl2-derivation ansatz for P C_V P^-1 FAILS (documented
      must-fail: the missing structure is named); P C_U P^-1 has the
      closed rank-one read form S |-> S11 * N, N = [[3,-2],[-2,3]];
  A6  THE CONSTRUCTION: the full solution set of {congruence + the two
      canonical ray conditions} is an explicit 1-parameter boost family
      (proved exactly by hyperbolic-basis normal form); INTEGRALITY
      leaves a FINITE set of exactly 16 members (m in {+-1, +-2, +-1/3,
      +-2/3}, eps = +-1; irrational Pell-type members excluded by an
      entrywise Galois argument: for integral Q the matrix B = Q P^-1
      is rational with eigenvalues (m, 1/m, eps); irrational m forces
      every entry coefficient pair a_ij = b_ij in
      Q_ij = a_ij m + b_ij/m + c_ij, which is measured to fail, so m is
      rational and m in (1/D1)Z, 1/m in (1/D2)Z give a finite candidate
      list); within the 16, EITHER the trace-ray condition OR
      Frobenius-minimality selects EXACTLY {+P, -P}; operator
      compatibility (integral transport of BOTH C_U and C_V) alone
      leaves 8 (honest partial: C_V-transport is integral for ALL 16 --
      automatic in the family -- and C_U-transport halves it).
  A6.4/A6.5 census cross-check: the exact ray conditions select the 4
      family members inside the [-4,4] box ({+-P, +-Q'} with
      Q' = Q(2/3,+1), the scale-swapped partner), and the class-level
      conditions reproduce exactly the two G8-orbits G8.P u G8.Q'.

Honest typing: the residual non-canonical input is the CHOICE of the
prime-side target pair inside its G8-orbit (swap X11<->X22, X12-sign,
global sign) -- exactly the symmetry residue the predecessor census
left; everything else is operator/null-cone data.

Verdict enums (frozen): P-OPERATOR-CONSTRUCTED-MOD-SIGN (core checks
pass), P-CONSTRUCTION-OPEN.

FIREWALL: no marker changes; no positivity claim, no RH statement; the
gl2-derivation ansatz stays a documented must-fail (typed negative); the
G8 orientation choice of the target pair is the named residual input.

PROVENANCE: discovery probe p_operator_construction_probe.py (2026-08-02,
25/25, verdict P-OPERATOR-CONSTRUCTED-MOD-SIGN).

Python-only (sympy exact), counted per GATE.WOLFRAM.02.
"""
import itertools
import math
import time

import sympy as sp

T0 = time.time()
CHECKS = []


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok)))
    print("[%s] %s%s" % ("PASS" if ok else "FAIL", name,
                         (" -- " + detail) if detail else ""))


x = sp.symbols("x")
Jdet = sp.Matrix([[0, 1, 0], [1, 0, 0], [0, 0, -2]])
Jfix = sp.Matrix([[16, 2, 4], [2, -2, 2], [4, 2, -2]])
P = sp.Matrix([[3, 0, 0], [3, 0, 2], [-1, 1, -1]])
CU = sp.Matrix([[3, 0, 0], [-3, 0, 0], [0, 0, 0]])
CV = sp.Matrix([[2, 1, -1], [-2, -1, 2], [-2, -1, 2]])
Pinv = P.inv()


def qform(J, v):
    v = sp.Matrix(v)
    return sp.expand((v.T * J * v)[0, 0])


def pairing(J, u, v):
    return sp.expand((sp.Matrix(u).T * J * sp.Matrix(v))[0, 0])


def ray(vec):
    """Primitive sign-normalized integer representative of a ray."""
    vec = [sp.Rational(c) for c in vec]
    L = sp.ilcm(*[sp.fraction(c)[1] for c in vec])
    w = [int(c * L) for c in vec]
    g = 0
    for c in w:
        g = math.gcd(g, abs(c))
    w = [c // g for c in w]
    for c in w:
        if c != 0:
            if c < 0:
                w = [-a for a in w]
            break
    return tuple(w)


def height(z):
    return sum(c * c for c in z)


# ================================================================== A0
print("=" * 78)
print("A0: guards (copied matrices)")
print("=" * 78)

check("A0.1 congruence guard: P^T J_det P = J_fix, det P = -6, "
      "det J_det = 2, det J_fix = 72",
      sp.simplify(P.T * Jdet * P - Jfix) == sp.zeros(3, 3)
      and P.det() == -6 and Jdet.det() == 2 and Jfix.det() == 72)

char_ok = (CU.charpoly(x).as_expr() == sp.expand(x ** 2 * (x - 3))
           and CV.charpoly(x).as_expr() == sp.expand(x * (x - 1) * (x - 2))
           and sp.trace(CU * CV) == 3)
u_cu = sp.Matrix([1, -1, 0])
w_cu = sp.Matrix([1, 0, 0])
check("A0.2 (C_U, C_V) copied-matrix guard: char C_U = x^2(x-3), "
      "char C_V = x(x-1)(x-2), tr(C_U C_V) = 3; and C_U = 3 u w^T with "
      "u = (1,-1,0), w = e1 (rank one)",
      char_ok and sp.simplify(CU - 3 * u_cu * w_cu.T) == sp.zeros(3, 3))

# ================================================================== A1
print("=" * 78)
print("A1: the spectral structure of P")
print("=" * 78)

charP = P.charpoly(x).as_expr()
check("A1.1 char P = (x-3)(x-1)(x+2) exactly (spectrum {3, 1, -2}, "
      "product -6 = det P)",
      sp.expand(charP - (x - 3) * (x - 1) * (x + 2)) == 0,
      "char P = %s" % sp.factor(charP))

tau = sp.Matrix([1, 1, 0])          # the trace ray (S = identity direction)
check("A1.2 exact eigenrays: P(1,1,0) = 3(1,1,0) [the prime-side TRACE "
      "ray is P-fixed], P(0,2,1) = (0,2,1), P(0,1,-1) = -2(0,1,-1)",
      P * tau == 3 * tau
      and P * sp.Matrix([0, 2, 1]) == sp.Matrix([0, 2, 1])
      and P * sp.Matrix([0, 1, -1]) == -2 * sp.Matrix([0, 1, -1]))

# ================================================================== A2
print("=" * 78)
print("A2: the C_V eigenframe on the fixed lattice (canonical operator data)")
print("=" * 78)

v0 = sp.Matrix([1, -2, 0])    # ker C_V
v1 = sp.Matrix([0, 1, 1])     # fix C_V
v2 = sp.Matrix([1, -2, -2])   # 2-eigenvector
check("A2.1 C_V eigenframe exact: ker C_V = ray(1,-2,0), fix C_V = "
      "ray(0,1,1), 2-eigenray = (1,-2,-2) (eigenvalues 0,1,2 simple)",
      CV * v0 == sp.zeros(3, 1) and CV * v1 == v1 and CV * v2 == 2 * v2
      and CV.eigenvals() == {0: 1, 1: 1, 2: 1})

q0, q1, q2 = qform(Jfix, v0), qform(Jfix, v1), qform(Jfix, v2)
p01 = pairing(Jfix, v0, v1)
p02 = pairing(Jfix, v0, v2)
p12 = pairing(Jfix, v1, v2)
check("A2.2 J_fix data of the frame: q(v0) = %s, q(v1) = %s (BOTH "
      "ISOTROPIC), q(v2) = %s; pairings <v0,v1> = %s, <v0,v2> = %s, "
      "<v1,v2> = %s" % (q0, q1, q2, p01, p02, p12),
      (q0, q1, q2) == (0, 0, -8) and (p01, p02, p12) == (6, 0, 6))

eps_v = sp.Matrix([0, 0, 1])   # off-diagonal unit E = e1 e2^T + e2 e1^T
iota2 = sp.Matrix([0, 1, 0])   # e2 (x) e2 (minimal isotropic)
check("A2.3 bookkeeping (task candidate (1)): the P columns in "
      "prime-side atoms: col1 = 3 tau - eps, col2 = eps, col3 = "
      "2 iota2 - eps with tau = trace ray, eps = off-diagonal unit, "
      "iota2 = e2(x)e2",
      P.col(0) == 3 * tau - eps_v and P.col(1) == eps_v
      and P.col(2) == 2 * iota2 - eps_v)

# ================================================================== A3
print("=" * 78)
print("A3: the null-cone census (primitive isotropic rays by height)")
print("=" * 78)

BOUND = 12


def primitive_isotropic_rays(J, bound):
    out = []
    J = [[int(J[i, j]) for j in range(3)] for i in range(3)]
    for z in itertools.product(range(-bound, bound + 1), repeat=3):
        if z == (0, 0, 0):
            continue
        first = next(c for c in z if c != 0)
        if first < 0:
            continue
        if math.gcd(math.gcd(abs(z[0]), abs(z[1])), abs(z[2])) != 1:
            continue
        qv = (J[0][0] * z[0] * z[0] + J[1][1] * z[1] * z[1]
              + J[2][2] * z[2] * z[2]
              + 2 * (J[0][1] * z[0] * z[1] + J[0][2] * z[0] * z[2]
                     + J[1][2] * z[1] * z[2]))
        if qv == 0:
            out.append((height(z), z))
    return sorted(out)


iso_fix = primitive_isotropic_rays(Jfix, BOUND)
iso_det = primitive_isotropic_rays(Jdet, BOUND)
print("    J_fix isotropic rays (height, ray), first 8: %s"
      % iso_fix[:8])
print("    J_det isotropic rays (height, ray), first 8: %s"
      % iso_det[:8])

h_fix = [h for h, _ in iso_fix]
min_fix = [z for h, z in iso_fix if h == h_fix[0]]
second_h = min(h for h in h_fix if h > h_fix[0])
second_fix = [z for h, z in iso_fix if h == second_h]
check("A3.1 J_fix minimal isotropic ray UNIQUE: height %d ray %s; "
      "second-minimal UNIQUE: height %d ray %s"
      % (h_fix[0], min_fix, second_h, second_fix),
      h_fix[0] == 2 and min_fix == [(0, 1, 1)]
      and second_h == 5 and second_fix == [(1, -2, 0)])

check("A3.2 THE OPERATOR CHARACTERIZATION: {minimal, second-minimal} "
      "isotropic rays of J_fix = {fix C_V, ker C_V} = {(0,1,1), "
      "(1,-2,0)} EXACTLY",
      set(min_fix + second_fix) == {ray(v1), ray(v0)})

h_det = [h for h, _ in iso_det]
first_det = [z for h, z in iso_det if h == 1]
second_det = [z for h, z in iso_det if h == 3]
rank1_ok = all(z[0] * z[1] - z[2] * z[2] == 0 for _, z in iso_det)
check("A3.3 J_det minimal isotropic rays: height 1 = {(1,0,0), (0,1,0)} "
      "(the two coordinate rank-one directions; Klein-swap ambiguous "
      "PAIR), height 3 = {(1,1,1), (1,1,-1)}; every J_det-isotropic y "
      "is a rank-one symmetric matrix (det = 0)",
      sorted(first_det) == [(0, 1, 0), (1, 0, 0)]
      and sorted(second_det) == [(1, 1, -1), (1, 1, 1)] and rank1_ok)

# ================================================================== A4
print("=" * 78)
print("A4: P on the null cones (ray transport)")
print("=" * 78)

img1 = ray(P * v1)
img0 = ray(P * v0)
img2 = ray(P * v2)
check("A4.1 [CENTRAL] P transports the operator frame to canonical "
      "rank-one rays: P(fix C_V) = %s (height %d: THE minimal J_det "
      "class), scale 2; P(ker C_V) = %s (height %d: the second class), "
      "scale 3; P(2-eigenray) = %s (q = -8)"
      % (img1, height(img1), img0, height(img0), img2),
      img1 == (0, 1, 0) and P * v1 == 2 * sp.Matrix([0, 1, 0])
      and img0 == (1, 1, -1) and P * v0 == 3 * sp.Matrix([1, 1, -1])
      and img2 == (3, -1, -1))

pull_100 = ray(Pinv * sp.Matrix([1, 0, 0]))
pull_111 = ray(Pinv * sp.Matrix([1, 1, 1]))
check("A4.2 [honest asymmetry] the minimal J_det rays do NOT all pull "
      "back to minimal J_fix rays: P^-1(1,0,0) ~ %s (height %d), "
      "P^-1(1,1,1) ~ %s (height %d); the grading match is the FORWARD "
      "transport of the operator frame (A4.1)"
      % (pull_100, height(pull_100), pull_111, height(pull_111)),
      pull_100 == (2, -1, -3) and pull_111 == (1, 4, 0))

print("    transport table (J_fix ray -> P image, heights):")
for h, z in iso_fix[:6]:
    im = ray(P * sp.Matrix(z))
    print("      %s (h=%d)  ->  %s (h=%d)" % (z, h, im, height(im)))

# ================================================================== A5
print("=" * 78)
print("A5: the transported operators on the prime side")
print("=" * 78)

CVp = sp.simplify(P * CV * Pinv)
CUp = sp.simplify(P * CU * Pinv)
CVp_target = sp.Matrix([[3, 0, 3], [0, 1, 1], [-1, 0, -1]])
CUp_target = sp.Matrix([[3, 0, 0], [3, 0, 0], [-2, 0, 0]])
check("A5.1 P C_V P^-1 and P C_U P^-1 are INTEGER: C_V' = %s, C_U' = %s"
      % (CVp.tolist(), CUp.tolist()),
      CVp == CVp_target and CUp == CUp_target)

y1s, y2s, y3s = sp.symbols("y1 y2 y3")
yv = sp.Matrix([y1s, y2s, y3s])
read_form = sp.expand(CUp * yv - y1s * sp.Matrix([3, 3, -2]))
Nmat = sp.Matrix([[3, -2], [-2, 3]])
check("A5.2 C_U' has the closed rank-one READ form: C_U'(S) = S11 * N "
      "with N = [[3,-2],[-2,3]] (det N = 5, tr N = 6) -- exact symbolic "
      "identity", read_form == sp.zeros(3, 1)
      and Nmat.det() == 5 and sp.trace(Nmat) == 6,
      "(measured numerology, no claim: det N = 5 = g_car, tr N = 6 = "
      "p_2 = |det P|)")

a_, b_, c_, d_ = sp.symbols("a b c d")
DA = sp.Matrix([[2 * a_, 0, 2 * b_], [0, 2 * d_, 2 * c_],
                [c_, b_, a_ + d_]])   # S |-> A S + S A^T in y-coords
solV = sp.solve([sp.expand(e) for e in (DA - CVp)],
                [a_, b_, c_, d_], dict=True)
solU = sp.solve([sp.expand(e) for e in (DA - CUp)],
                [a_, b_, c_, d_], dict=True)
DA_ok_example = sp.Matrix([[0, 0, 0], [0, 2, 0], [0, 0, 1]])
example_hits = (DA.subs({a_: 0, b_: 0, c_: 0, d_: 1}) == DA_ok_example
                and DA_ok_example.charpoly(x).as_expr()
                == sp.expand(x * (x - 1) * (x - 2)))
check("A5.3 [must-fail, honest] the gl2-DERIVATION ansatz "
      "C'(S) = A S + S A^T has NO solution for C_V' (nor for C_U'), "
      "although the ansatz CAN realize the eigenvalue set {0,1,2} "
      "(A = diag(0,1) does): the obstruction is the EIGENVECTOR "
      "configuration, i.e. C_V' is not gl2-equivariant -- the named "
      "missing structure for a fully intrinsic prime-side reading of "
      "C_V'", solV == [] and solU == [] and example_hits)

check("A5.4 C_V' is pinned by its eigen data: ker C_V' = ray(1,1,-1) "
      "= (e1-e2)(x)(e1-e2), fix C_V' = ray(0,1,0) = e2(x)e2 (both "
      "canonical rank-one null rays), 2-eigenray = (3,-1,-1)",
      CVp * sp.Matrix([1, 1, -1]) == sp.zeros(3, 1)
      and CVp * sp.Matrix([0, 1, 0]) == sp.Matrix([0, 1, 0])
      and CVp * sp.Matrix([3, -1, -1]) == 2 * sp.Matrix([3, -1, -1]))

# ================================================================== A6
print("=" * 78)
print("A6: the construction -- congruence + ray conditions + integrality")
print("=" * 78)

y0t = sp.Matrix([1, 1, -1])   # target of ker C_V
y1t = sp.Matrix([0, 1, 0])    # target of fix C_V
ortho = sp.Matrix.vstack((Jdet * y0t).T, (Jdet * y1t).T)
wv = sp.Matrix(ray(ortho.nullspace()[0]))
W = sp.Matrix.hstack(y0t, y1t, wv)
G = sp.expand(W.T * Jdet * W)
check("A6.0 hyperbolic normal form: W = [(1,1,-1) | (0,1,0) | %s] is "
      "UNIMODULAR (det %s) with Gram W^T J_det W = %s (hyperbolic pair "
      "+ anisotropic line, q(w) = -2)"
      % (tuple(wv), W.det(), G.tolist()),
      abs(W.det()) == 1
      and G == sp.Matrix([[0, 1, 0], [1, 0, 0], [0, 0, -2]]))

s0_, s1_, aa_, bb_, cc_ = sp.symbols("s0 s1 a3 b3 c3")
Bw = sp.Matrix([[s0_, 0, aa_], [0, s1_, bb_], [0, 0, cc_]])
eqs = [sp.expand(e) for e in (Bw.T * G * Bw - G)]
fam = sp.solve(eqs, [s1_, aa_, bb_, cc_], dict=True)
fam_ok = (len(fam) == 2
          and all(sol[s1_] == 1 / s0_ and sol[aa_] == 0 and sol[bb_] == 0
                  and sol[cc_] ** 2 == 1 for sol in fam))
check("A6.1 the FULL two-ray solution set is the 1-parameter boost "
      "family: every Q with Q^T J_det Q = J_fix, Q(ker C_V) || (1,1,-1), "
      "Q(fix C_V) || (0,1,0) equals Q(m,eps) = W diag(m, 1/m, eps) "
      "W^-1 P with eps = +-1 (B := Q P^-1 fixes both rays, hence the "
      "J_det-orthocomplement line w, hence is W-triangular; the "
      "congruence forces exactly s0 s1 = 1, off-terms 0, eps^2 = 1)",
      fam_ok, "solve -> %s" % fam)

mm = sp.symbols("m", nonzero=True)


def Qfam(m_, e_):
    m_ = sp.sympify(m_)
    return sp.expand(W * sp.diag(m_, sp.Integer(1) / m_, sp.sympify(e_))
                     * W.inv() * P)


check("A6.G family guard: Q(1,+1) = P exactly", Qfam(1, 1) == P)

# ---- A6.2: pinning by the trace ray (symbolic, both eps branches)
pin = []
for e_ in (1, -1):
    Qm = Qfam(mm, e_)
    img = Qm * tau
    conds = [sp.expand(sp.together(img[0] * tau[1] - img[1] * tau[0])),
             sp.expand(sp.together(img[1] * tau[2] - img[2] * tau[1])),
             sp.expand(sp.together(img[0] * tau[2] - img[2] * tau[0]))]
    for sol in sp.solve(conds, mm, dict=True):
        pin.append((sol[mm], e_))
pin_ok = sorted(pin, key=str) == sorted([(sp.Integer(1), 1),
                                         (sp.Integer(-1), -1)], key=str)
check("A6.2 pinning (i), trace ray: within the WHOLE family (any real "
      "m), Q(1,1,0) || (1,1,0) holds ONLY for (m,eps) = (1,+1) -> "
      "Q = +P and (m,eps) = (-1,-1) -> Q = -P  [honest: the source ray "
      "(1,1,0)_z = b1+b2 is v604-basis data, not yet operator-derived]",
      pin_ok, "solutions (m, eps) = %s" % pin)

# ---- A6.3: pinning by INTEGRALITY (exact, finite)
rat_forced = {}
for e_ in (1, -1):
    Qm = Qfam(mm, e_)
    diffs = []
    for i in range(3):
        for j in range(3):
            pol = sp.Poly(sp.expand(Qm[i, j] * mm), mm)
            diffs.append(sp.expand(pol.nth(2) - pol.nth(0)))
    rat_forced[e_] = any(d != 0 for d in diffs)
check("A6.3a Galois exclusion of irrational (Pell) members: in BOTH eps "
      "branches some entry has m-coefficient != (1/m)-coefficient, so "
      "an integral Q P^-1 (rational, eigenvalues m, 1/m conjugate if "
      "irrational) forces m RATIONAL",
      rat_forced[1] and rat_forced[-1])

qsyms = sp.symbols("q0:9")
Qs = sp.Matrix(3, 3, qsyms)
Bdiag = sp.expand(W.inv() * Qs * Pinv * W)


def denom_lcm(e):
    d = sp.Integer(1)
    for s in qsyms:
        d = sp.ilcm(d, sp.fraction(sp.nsimplify(e.coeff(s)))[1])
    c0 = e.subs({s: 0 for s in qsyms})
    d = sp.ilcm(d, sp.fraction(sp.nsimplify(c0))[1])
    return int(d)


D1 = denom_lcm(Bdiag[0, 0])
D2 = denom_lcm(Bdiag[1, 1])
cands = set()
for k in sp.divisors(D1 * D2):
    cands.add(sp.Rational(k, D1))
    cands.add(sp.Rational(-k, D1))
found = []
for m_ in sorted(cands):
    for e_ in (1, -1):
        Qc = Qfam(m_, e_)
        if all(entry.is_integer for entry in Qc):
            found.append((m_, e_, Qc))
found_ms = sorted({m_ for m_, _, _ in found}, key=str)
target_ms = sorted({sp.Rational(s) for s in
                    ("1", "-1", "2", "-2", "1/3", "-1/3", "2/3", "-2/3")},
                   key=str)
check("A6.3b INTEGRALITY leaves a FINITE set: for integral Q, "
      "m in (1/%d)Z and 1/m in (1/%d)Z (denominator functionals of "
      "B = Q P^-1 in the W-basis), so m = k/%d with k | %d -- exact "
      "enumeration finds EXACTLY 16 integral members: m in {+-1, +-2, "
      "+-1/3, +-2/3} x eps = +-1 (NO Pell tower; the two-ray condition "
      "is integrally 16-fold, not unique)"
      % (D1, D2, D1, D1 * D2),
      len(found) == 16 and found_ms == target_ms,
      "m values %s" % [str(m_) for m_ in found_ms])

# ---- A6.3c: selectors within the 16 integral members
frobs = {}
tr_sel, op_sel = [], []
for m_, e_, Qc in found:
    frobs[(m_, e_)] = sum(int(en) ** 2 for en in Qc)
    img = Qc * tau
    if img[0] * tau[1] - img[1] * tau[0] == 0 and img[2] == 0:
        tr_sel.append((m_, e_, Qc))
    Qi = Qc.inv()
    if (all(en.is_integer for en in sp.expand(Qc * CV * Qi))
            and all(en.is_integer for en in sp.expand(Qc * CU * Qi))):
        op_sel.append((m_, e_, Qc))
fmin = min(frobs.values())
fmin_set = [Qc for m_, e_, Qc in found if frobs[(m_, e_)] == fmin]
fsecond = min(v for v in frobs.values() if v > fmin)
opV_all = all(all(en.is_integer for en in sp.expand(Qc * CV * Qc.inv()))
              for _, _, Qc in found)
check("A6.3c [CENTRAL] selectors inside the 16: (i) Frobenius-minimal "
      "= {+P, -P} EXACTLY (norm^2 %d, next %d); (ii) trace-ray "
      "= {+P, -P} EXACTLY; (iii) honest partial: operator "
      "compatibility alone leaves %d of 16 (C_V-transport is integral "
      "for ALL 16 -- automatic in the family: %s -- C_U-transport "
      "halves it)"
      % (fmin, fsecond, len(op_sel), opV_all),
      fmin == 25 and fsecond == 27
      and sorted(map(str, fmin_set)) == sorted(map(str, [P, -P]))
      and len(tr_sel) == 2
      and sorted(str(Qc) for _, _, Qc in tr_sel)
      == sorted(map(str, [P, -P]))
      and opV_all and len(op_sel) == 8,
      "op-compatible (m,eps): %s"
      % sorted((str(m_), e_) for m_, e_, _ in op_sel))
Qprime = Qfam(sp.Rational(2, 3), 1)
print("    the scale-swapped partner Q' = Q(2/3,+1) = %s (frob^2 27, "
      "frame scales (2,3) vs P's (3,2))" % Qprime.tolist())

# ---- A6.4/A6.5: the census cross-check
rng4 = range(-4, 5)
cols16 = [c for c in itertools.product(rng4, repeat=3)
          if c[0] * c[1] - c[2] * c[2] == 8]
colsm2 = [c for c in itertools.product(rng4, repeat=3)
          if c[0] * c[1] - c[2] * c[2] == -1]


def bil(u, v):
    return u[0] * v[1] + u[1] * v[0] - 2 * u[2] * v[2]


sols = []
for c1 in cols16:
    c2s = [c for c in colsm2 if bil(c1, c) == 2]
    c3s = [c for c in colsm2 if bil(c1, c) == 4]
    for c2 in c2s:
        for c3 in c3s:
            if bil(c2, c3) == 2:
                sols.append(tuple(tuple(int(v) for v in (c1[i], c2[i],
                                                         c3[i]))
                                  for i in range(3)))
P_rows = tuple(tuple(int(P[i, j]) for j in range(3)) for i in range(3))


def mat_ray(Q, z):
    y = [sum(Q[i][j] * z[j] for j in range(3)) for i in range(3)]
    g = 0
    for c in y:
        g = math.gcd(g, abs(c))
    y = [c // g for c in y]
    for c in y:
        if c != 0:
            if c < 0:
                y = [-a for a in y]
            break
    return tuple(y)


v0t, v1t = (1, -2, 0), (0, 1, 1)
imgs = {Q: (mat_ray(Q, v1t), mat_ray(Q, v0t)) for Q in sols}
exact_sols = [Q for Q, (i1, i0) in imgs.items()
              if i1 == (0, 1, 0) and i0 == (1, 1, -1)]
n_min1 = sum(1 for i1, _ in imgs.values() if i1 in {(0, 1, 0), (1, 0, 0)})
n_min0 = sum(1 for _, i0 in imgs.values() if i0 in {(1, 1, 1), (1, 1, -1)})
both_class = [Q for Q, (i1, i0) in imgs.items()
              if i1 in {(0, 1, 0), (1, 0, 0)}
              and i0 in {(1, 1, 1), (1, 1, -1)}]
fam_in_box = sorted(str(Qc.tolist()) for _, _, Qc in found
                    if all(abs(int(en)) <= 4 for en in Qc))
check("A6.4 census consistency: %d solutions in the [-4,4] box "
      "(predecessor: 40); the EXACT ray conditions select %d of them "
      "= {+-P, +-Q'} = precisely the family members inside the box; "
      "class-level (any minimal target): fix->height-1 for %d, "
      "ker->height-3 for %d, BOTH for %d"
      % (len(sols), len(exact_sols), n_min1, n_min0, len(both_class)),
      len(sols) == 40 and len(exact_sols) == 4
      and sorted(str(sp.Matrix(3, 3, lambda i, j: Q[i][j]).tolist())
                 for Q in exact_sols) == fam_in_box)

T_swap = sp.Matrix([[0, 1, 0], [1, 0, 0], [0, 0, 1]])
T_sgn = sp.Matrix([[1, 0, 0], [0, 1, 0], [0, 0, -1]])
G8 = [sp.eye(3)]
frontier = [sp.eye(3)]
while frontier:
    g = frontier.pop()
    for tmat in (T_swap, T_sgn, -sp.eye(3)):
        hmat = tmat * g
        if hmat not in G8:
            G8.append(hmat)
            frontier.append(hmat)


def orbit_of(M):
    return {tuple(tuple(int((g * M)[i, j]) for j in range(3))
                  for i in range(3)) for g in G8}


orbitP = orbit_of(P)
orbitQp = orbit_of(Qprime)
check("A6.5 the class-level ray conditions on the census select "
      "EXACTLY the two G8-orbits G8.P u G8.Q' (%d + %d = %d matrices; "
      "order-8 group: global sign, X11<->X22 swap, X12 sign); P's "
      "orbit is separated from Q's by Frobenius 25 vs 27"
      % (len(orbitP), len(orbitQp), len(both_class)),
      len(G8) == 8 and len(orbitP) == 8 and len(orbitQp) == 8
      and set(both_class) == (orbitP | orbitQp)
      and orbitP.isdisjoint(orbitQp))

# ================================================================== summary
print("=" * 78)
n_pass = sum(1 for _, ok in CHECKS if ok)
print("%d/%d checks passed" % (n_pass, len(CHECKS)))

core_ids = ("A3.2", "A4.1", "A6.1", "A6.3b", "A6.3c", "A6.5")
core_ok = all(ok for name, ok in CHECKS
              if any(name.startswith(cid) for cid in core_ids))
if core_ok:
    verdict_A = ("P-OPERATOR-CONSTRUCTED-MOD-SIGN -- P is, up to global "
                 "sign, the Frobenius-MINIMAL (equivalently: the "
                 "trace-ray-preserving) INTEGER congruence "
                 "J_fix -> J_det mapping the C_V-operator null frame "
                 "(ker C_V, fix C_V) = the two minimal isotropic rays "
                 "of J_fix onto the canonical rank-one rays "
                 "((e1-e2)^(x)2, e2^(x)2); the two-ray integral family "
                 "is finite (16 members, one scale-swapped partner "
                 "orbit Q' at Frobenius 27); residual non-canonical "
                 "input: the G8 orientation choice of the target pair; "
                 "the gl2-derivation reading of C_V' stays a typed "
                 "negative")
else:
    verdict_A = "P-CONSTRUCTION-OPEN (core checks failed; see FAILs)"
print("VERDICT A: %s" % verdict_A)
print("elapsed: %.1f s" % (time.time() - T0))
if n_pass == len(CHECKS):
    print("ALL CHECKS PASSED")
else:
    print("SOME CHECKS FAILED")


def run():
    """run_all.py entry point; the checks execute at import time above."""
    return len([1 for _, ok in CHECKS if not ok])


if __name__ == "__main__":
    raise SystemExit(1 if run() else 0)
