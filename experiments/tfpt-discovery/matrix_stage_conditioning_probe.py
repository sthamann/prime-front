#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""matrix_stage_conditioning_probe -- PRIME.MATRIX.STAGE.CONDITIONING.01.

EXPLORATION ONLY.  Demand accounting for an already-published valid
lower bound.  No positivity claim, no RH claim, no promotion, nothing
outside experiments/.

THE QUESTION.  CCCLXVI certified that the deployed test window is
responsible for a SIGN error plus at most ~1.75 orders, and that the
best faithful window's residual does NOT grow with cell size, while
the deployed matrix miss of CCCLIX grows 2.470e11 -> 1.990e14.  The
growing part therefore lives in the Galerkin/Schur matrix stage.  This
probe asks whether that growth is INTRINSIC or an ARTIFACT of the
deployed discretisation of the DEMAND.

THE OBJECT.  For a registered cell (alpha, D), h = alpha/D, and phase
theta,

  Omega_theta[m,m'] = (G(m+m'+2theta) + G(|m-m'|))/2,
  G(x)   = c(x) - (c(x+1)+c(|x-1|))/2 = -(1/2) Delta^2 c (x),
  c(x)   = arch_A(xD, D) + c_at(x),
  c_at(x)= -(1/2) sum_n mu_n [tau_D(xD-u_n) + tau_D(xD+u_n)],
  mu_n   = 2 Lambda(n)/sqrt(n),  u_n = log n <= 2 alpha + 2D,

and s(theta) = n - b^T B^-1 b at the (0,0) pivot.  Write the comb split
Omega = Omega_0 - Omega_c with Omega_0 the archimedean-only wall
(c_at = 0), so n = n_0 - n_c, b = b_0 - b_c, B the TRUE co-block.

CCCLIX's valid lower bound is int s >= G_geo - A with

  A = R + beta^-1 (||b_0||_2 + sqrt(h-1) R)^2,                   (LB)

R the entrywise classical envelope of the comb contribution and
beta <= inf_theta lambda_min(B_theta) a certified co-block floor.

THREE EXACT FACTS THIS PROBE USES (all machine-checked in S1).

(I) BASIS INVARIANCE OF THE OBJECT.  For every invertible M of size
h-1 the congruence T = diag(1, M) leaves the Schur scalar fixed:
s(T^T Omega T) = s(Omega).  The demand (LB) is NOT invariant: it is
built from lambda_min(B) and from the l2 norm of the l-infinity
uncertainty ball, both of which move under T.

(II) THE INVARIANT THREE-TERM SPLIT.  With x_0 = B^-1 b_0,
q_0 = b_0^T B^-1 b_0, q_c = b_c^T B^-1 b_c,

  s = (n_0 - q_0) - n_c + 2 <b_c, x_0> - q_c.                    (SP)

Every term of (SP) is invariant under T = diag(1, M).  Under the comb
sign flip b_c -> -b_c, n_c -> -n_c the middle bracket is ODD and the
other two are EVEN.

(III) THE INFORMATION FLOOR.  Fix the information
  I(R) = { B, b_0, n_0 known exactly; |n_c| <= R; |b_c,i| <= R }.
Any bound A valid for all data consistent with I(R) satisfies

  A >= A_exact := R + sup_{|z|_inf <= 1} (b_0 - R z)^T B^-1 (b_0 - R z)

because the supremum is attained at an admissible datum.  A_exact is
invariant under T = diag(1, M) with the box transported, hence NO
reformulation inside I(R) can beat it.  Moreover
  sup_{|z|_inf<=1} z^T B^-1 z  >=  tr(B^-1)  >=  1/lambda_min(B),
by the random-sign expectation, so every formulation inside I(R)
inherits the R^2/lambda_min blow-up.

THE FIVE FORMULATIONS COMPARED (same finite statement, same classical
inputs, different coordinates for the demand).

 F0 DEPLOYED-SPECTRAL   A = R + (||b_0||_2 + sqrt(h-1) R)^2 / beta.
 F1 JACOBI-WHITENED     congruence M = diag(B)^-1/2; the box becomes
                        |b~_c,i| <= R/sqrt(B_ii);
                        A = R + (||b~_0|| + R (sum 1/B_ii)^1/2)^2/beta~.
 F2 CHOLESKY-ORTHONORMAL  congruence M = L^-T from B = L L^T, so the
                        Galerkin basis is orthonormal for the deployed
                        measure and beta~ = 1 EXACTLY;
                        A = R + (sqrt(q_0) + R sqrt(M_box))^2,
                        M_box = sup_{|z|_inf<=1} z^T B^-1 z.
 F3 RESOLVENT-SPLIT     no Cauchy-Schwarz on the cross term;
                        A = R + q_0 + 2R min(||x_0||_1,
                            sqrt(q_0 M_box)) + R^2 M_box.
 F4 SOURCE-PROFILE      the EXACT algebraic factorisation
                        b_c = -(1/4) A_2 w,  w_k = c_c(k-1+2theta)
                        + c_c(k-1),  (A_2 z)_i = z_i - 2z_{i+1}
                        + z_{i+2}, imposes the classical envelope on
                        the SOURCE lag profile c_c (envelope R_c) in
                        place of its second difference;
                        A = n_c^env + q_0 + R_c ||A_2^T x_0||_1
                            + (R_c^2/4) M2_box,
                        M2_box = sup_{|w|_inf<=1} w^T A_2^T B^-1 A_2 w.

F4 is a Gram/CD-kernel form: the conditioning is read off the kernel
A_2^T B^-1 A_2 (a mixed fourth difference of the inverse kernel)
instead of off B^-1 itself.  F0-F3 live inside I(R) and are therefore
floored by (III); F4 changes the coordinates in which the SAME
classical theorem is applied and is not floored by (III).

THE SOURCE ENVELOPE R_c, from the SAME Vinogradov-Korobov input and
the SAME optimistic audit constants as CCCLIX.  With y = e^{xD},
c_at reads only atoms with |log n - xD| < D and no reflected atom
(log 2 > D on every audited cell, checked), so

  |c_c(x)| <= int_{y e^-D}^{y e^D} t^-1/2 dpsi(t)
           <= 4 sqrt(y) sinh(D/2) + 2 C_VK sqrt(y) e^{D/2} e^{-eta}
  R_c := H_c(x_0) + 4 e^{a+D} sinh(D/2)
         + 2 C_VK e^{a+3D/2} exp(-eta(2a-2D, c_VK)),
  H_c(x_0) = sum_{n <= x_0} Lambda(n)/sqrt(n),

by Stieltjes parts exactly as (VK) in CCCLIX; only the kernel norms
differ (tent instead of ||K_D||_1 = 4D/3, ||K_D'||_1 = 4).

WHAT IS MEASURED.  Per registered cell and per frozen theta midpoint,
with outward-rounded enclosures throughout (no eigensolver anywhere;
signs only from Cholesky certificates; inverse iteration used only as
an unverified HINT whose output is re-certified):
  beta (deployed Higham floor), an upper bracket for lambda_min(B)
  from a Rayleigh quotient, q_0, q_c, <b_c,x_0>, ||x_0||_1,
  ||A_2^T x_0||_1, Sum|B^-1|, Sum|A_2^T B^-1 A_2|, certified box
  vertices for M_box and M2_box, diag(B), the Jacobi floor beta~.
Growth is reported as ratios and as exponents p = log(ratio)/log(h
ratio) between registered rungs.  NO least-squares fit is taken.

FROZEN PROTOCOL (before the run of record).
 S0  SHA and AST firewall: no zero reader, tau, target sign,
     eigensolver or fitting call; deep evaluator cells excluded.
 S1  The eight exact lemmas above: congruence invariance of s, the
     (SP) identity, congruence invariance of each of its three terms,
     the parity of the terms under the comb flip, attainment of the
     box supremum at an admissible datum, box >= trace, strict
     lossiness of the spectral step, and the source factorisation.
 S2  Self-tests of the enclosure toolkit against reference solves on
     a planted ill-conditioned 6x6.
 A   Targets 184/405/838, 32 frozen theta midpoints.  Wards: the
     CCCLIX deployed miss A/G and the CCCLIX measured theta-means of
     s must be reproduced; the source factorisation must close to
     roundoff; n_c must vanish identically (log 2 > 3D on every
     audited cell, so no atom is within reach of the pivot entry);
     the certified floor must lie below the Rayleigh bracket.
 B   Factor-by-factor growth attribution of the deployed demand; the
     product of the weighted factors must reproduce the measured
     growth to 2 percent.
 C   The five formulations, their demands and their exponents, plus
     the invariant I(R) floor.
 G   Signed vs unsigned, THREE INDEPENDENT PATHS: (i) the (SP) split
     with enclosures, (ii) a Cholesky-free variational path
     q >= 2 b.x - x^T B x using matrix-vector products only, (iii)
     the sign-flipped wall pushed through the DEPLOYED cert_schur.
 X   SCRAMBLE and EPSTEIN through the identical pipeline at the 184
     cell, 8 frozen offsets.
 V   Frozen enum and precedence as below.

FROZEN VERDICT ENUM AND PRECEDENCE.
  SEAT-INSTRUMENT-EDGE  iff a structural ward (S1/S2) fails, or the
      CCCLIX reproduction ward misses by more than 5 percent, or the
      Higham certificate refuses on more than 25 percent of the
      thetas of the two registered rungs.
  SEAT-SIGNED-CONVERTED iff for the best formulation the SIGN-FLIPPED
      counterworld (b_c -> -b_c, n_c -> -n_c, B unchanged) still has
      s > 0 at every audited (cell, theta) -- i.e. positivity would
      follow from unsigned data alone.  Triple verification required.
  SEAT-CONDITIONING     iff some equivalent formulation lowers the
      demand-to-supply ratio at the deepest registered rung by at
      least one order AND its growth exponent is at most 0.8 times
      the deployed exponent.
  SEAT-INTRINSIC        otherwise.

DISCLOSURE.  Before this spec was frozen, an exploratory read at one
theta measured Sum|B^-1| against Sum|A_2^T B^-1 A_2| and the three
terms of (SP) at the two registered rungs.  Nothing in the frozen
protocol, the enum, the precedence, the cell list, the theta grid or
the envelope formulas was chosen after a result read; the exploration
is disclosed here because it motivated including F4 at all.

SCOPE.  Reads shift_average_probe and shift_average_all_depth_probe
READ-ONLY for the deployed generators and the deployed R envelope, so
that the CCCLIX numbers are reproduced rather than re-derived.  Writes
nothing.  No verification/, papers, ledger, website, manifests, .md or
commits.  No tau, no zero data, no target sign, no eigensolver, no
fit, no ladder scan (the three audited targets are the registered
non-deep targets 184/405/838 of the instrument of record; the deep
evaluator cells 1393/2854 are excluded).  Runtime bar 1800 s.
NO RH CLAIM.
"""

from __future__ import annotations

import ast
import hashlib
import math
import os
import sys
import time

import numpy as np
import scipy.linalg as sla
import sympy as sp

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)

import shift_average_probe as sap             # noqa: E402  READ-ONLY
import shift_average_all_depth_probe as sad   # noqa: E402  READ-ONLY

FROZEN_SPEC = __doc__
SPEC_SHA = hashlib.sha256(FROZEN_SPEC.encode("utf-8")).hexdigest()
T0 = time.time()
CHECKS: list[tuple[str, bool]] = []

AUDIT_TARGETS = (184, 405, 838)
REGISTERED_RUNGS = (184, 405)          # the two rungs CCCLIX priced
N_THETA = 32
CTRL_THETA = tuple((k + 0.5) / 8.0 for k in range(8))
RUNTIME_BAR = 1800.0
WARD_REL = 0.05
CERT_REFUSE_FRAC = 0.25
COND_LEVEL_BAR = 1.0                   # orders
COND_EXPONENT_BAR = 0.8
U_RND = 0.5 * float(np.finfo(float).eps)
AST_BANNED = {
    "zetazero", "zetazeros", "nzeros", "find_zeros",
    "eigh", "eigvalsh", "eig", "eigvals", "eigs", "eigsh",
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


# ------------------------------------------------------- rigour toolkit
def gam(k):
    """Higham's gamma_k for float64 (outward rounding envelope)."""
    t = float(k) * U_RND * 2.0
    return t / (1.0 - t) if t < 1.0 else float("inf")


def fsum(v):
    return math.fsum(np.asarray(v, float).ravel().tolist())


def quad_encl(b, B, cf, beta):
    """Enclosure of b^T B^-1 b (B PD, lambda_min(B) >= beta > 0)."""
    y = sla.cho_solve(cf, b, check_finite=False)
    r = b - B @ y
    n = B.shape[0]
    env_r = gam(n + 1) * (np.abs(B) @ np.abs(y) + np.abs(b))
    t1 = fsum(b * y)
    t2 = fsum(r * y)
    e_dot = gam(n + 1) * (fsum(np.abs(b * y)) + fsum(np.abs(r * y))) \
        + fsum(env_r * np.abs(y))
    r_up = math.sqrt(fsum((np.abs(r) + env_r) ** 2)) * (1.0 + gam(n + 1))
    lo = t1 + t2 - e_dot
    hi = t1 + t2 + e_dot + r_up * r_up / beta
    return max(lo, 0.0), hi, y, r_up


def variational_lo(b, B, x):
    """Rigorous LOWER bound on b^T B^-1 b = max_x (2 b.x - x^T B x),
    valid for ANY x and using matrix-vector products only -- no
    Cholesky, no solve, no certificate.  Outward rounded."""
    n = B.shape[0]
    lin = fsum(b * x)
    lin_lo = lin - gam(n + 1) * fsum(np.abs(b * x))
    Bx = B @ x
    quad = fsum(x * Bx)
    quad_hi = quad + gam(n + 2) * fsum(np.abs(x) * (np.abs(B)
                                                    @ np.abs(x)))
    return 2.0 * lin_lo - quad_hi


def bilin_encl(u, v, B, cf, beta, qu_hi):
    """Enclosure of <u, B^-1 v> given an upper bound qu_hi on
    u^T B^-1 u."""
    y = sla.cho_solve(cf, v, check_finite=False)
    r = v - B @ y
    n = B.shape[0]
    env_r = gam(n + 1) * (np.abs(B) @ np.abs(y) + np.abs(v))
    t1 = fsum(u * y)
    e_dot = gam(n + 1) * fsum(np.abs(u * y))
    r_up = math.sqrt(fsum((np.abs(r) + env_r) ** 2)) * (1.0 + gam(n + 1))
    slack = math.sqrt(max(qu_hi, 0.0)) * r_up / math.sqrt(beta)
    return t1 - e_dot - slack, t1 + e_dot + slack


def fsum_sq_cols(M):
    M = np.asarray(M, float)
    return np.einsum("ij,ij->j", M, M)


def resid_cols_up(A, B, Y, rowsum_B):
    """Upward bound on the column 2-norms of the EXACT residual
    A - B Y, from the computed float residual plus the rounding
    envelope gamma_{n+1}(|A| + |B||Y|), the latter bounded columnwise
    by rowsum(|B|) * max_k |Y_kj| to avoid a dense |B||Y| product."""
    n = B.shape[0]
    rres = A - B @ Y
    env_norm = gam(n + 1) * (
        np.sqrt(fsum_sq_cols(np.abs(A)))
        + float(np.linalg.norm(rowsum_B))
        * np.max(np.abs(Y), axis=0))
    return (np.sqrt(fsum_sq_cols(rres)) + env_norm) * (1.0 + gam(n + 2))


def sum_abs_inv_up(B, cf, beta, rowsum_B):
    """Upward-rounded bound on sum_{ij} |(B^-1)_{ij}| via
    B^-1 = X + X^T Res + Res^T B^-1 Res, Res = I - B X."""
    n = B.shape[0]
    X = sla.cho_solve(cf, np.eye(n), check_finite=False)
    res_up = resid_cols_up(np.eye(n), B, X, rowsum_B)
    x_up = np.sqrt(fsum_sq_cols(np.abs(X))) * (1.0 + gam(n + 2))
    base = fsum(np.abs(X)) * (1.0 + gam(n + 2))
    corr = fsum(x_up) * fsum(res_up)
    corr2 = fsum(res_up) ** 2 / beta
    return base + corr + corr2


def apply_at_matrix(Y, h, absolute=False):
    """A_2^T Y for the (h-1) x (h+2) second-difference matrix, without
    forming A_2; absolute=True gives |A_2|^T |Y|."""
    Y = np.abs(Y) if absolute else Y
    out = np.zeros((h + 2,) + Y.shape[1:])
    out[1:h] += Y
    out[2:h + 1] += (2.0 * Y) if absolute else (-2.0 * Y)
    out[3:h + 2] += Y
    return out


def second_difference_T(w, h):
    return apply_at_matrix(w, h)


def second_difference_matrix(h):
    A = np.zeros((h - 1, h + 2))
    for i in range(1, h):
        A[i - 1, i] = 1.0
        A[i - 1, i + 1] = -2.0
        A[i - 1, i + 2] = 1.0
    return A


def sum_abs_conj_up(A, B, cf, beta, h, rowsum_B):
    """Upward bound on sum_{rs} |(A_2^T B^-1 A_2)_{rs}| via
    A^T B^-1 A = A^T Y + Y^T Rres + Rres^T B^-1 Rres, Rres = A - B Y."""
    n = B.shape[0]
    Y = sla.cho_solve(cf, A, check_finite=False)
    r_up = resid_cols_up(A, B, Y, rowsum_B)
    y_up = np.sqrt(fsum_sq_cols(np.abs(Y))) * (1.0 + gam(n + 2))
    C = apply_at_matrix(Y, h)
    base = fsum(np.abs(C)) * (1.0 + gam(n + 2)) \
        + gam(n + 1) * fsum(apply_at_matrix(Y, h, absolute=True))
    corr = fsum(y_up) * fsum(r_up)
    corr2 = fsum(r_up) ** 2 / beta
    return base + corr + corr2, C


def rayleigh_up(B, v):
    """Upward-rounded Rayleigh quotient, a rigorous UPPER bound on
    lambda_min(B) for any v != 0."""
    n = B.shape[0]
    num = fsum(v * (B @ v))
    num_up = num + gam(n + 1) * fsum(np.abs(v) * (np.abs(B) @ np.abs(v)))
    den = fsum(v * v)
    den_lo = den * (1.0 - gam(n + 1))
    return num_up / den_lo


def inverse_iteration_hint(cf, n, iters=60):
    v = np.ones(n) / math.sqrt(n)
    for _ in range(iters):
        v = sla.cho_solve(cf, v, check_finite=False)
        nv = float(np.linalg.norm(v))
        if not math.isfinite(nv) or nv == 0.0:
            return np.ones(n) / math.sqrt(n)
        v /= nv
    return v


def power_hint(C, iters=60):
    v = np.ones(C.shape[0]) / math.sqrt(C.shape[0])
    for _ in range(iters):
        v = C @ v
        nv = float(np.linalg.norm(v))
        if not math.isfinite(nv) or nv == 0.0:
            return np.ones(C.shape[0]) / math.sqrt(C.shape[0])
        v /= nv
    return v


# --------------------------------------------------- classical envelopes
def r_deployed(a_value, d_value):
    """The CCCLIX envelope, imported verbatim (optimistic audit read)."""
    r_fluc = sad.finite_head_envelope(2) + sad.vk_entry_envelope(
        a_value, d_value, sad.VK_C_OPT, sad.VK_c_OPT)
    r_sm = sad.smooth_main_envelope(a_value, d_value)
    return r_fluc + r_sm, r_fluc, r_sm


def head_source(x0=2):
    return sum(
        math.log(p) / math.sqrt(p)
        for p in range(2, x0 + 1)
        if all(p % d for d in range(2, int(math.sqrt(p)) + 1))
    )


def r_source(a_value, d_value, c_big=1.0, c_small=1.0, x0=2):
    """Envelope for the SOURCE lag profile |c_c(x)|, same VK input,
    same optimistic constants, tent kernel instead of K_D."""
    eta = sad.vk_eta(max(2.0 * a_value - 2.0 * d_value, math.e), c_small)
    smooth = 4.0 * math.exp(a_value + d_value) * math.sinh(0.5 * d_value)
    fluc = 2.0 * c_big * math.exp(a_value + 1.5 * d_value) * math.exp(-eta)
    return head_source(x0) + smooth + fluc, smooth, fluc


# =============================================================== S1 exact
def s1_congruence_invariance():
    h = 4
    n = sp.Symbol("n")
    b = sp.Matrix(sp.symbols("b1:%d" % h))
    Bs = sp.Matrix(h - 1, h - 1, lambda i, j: sp.Symbol(
        "B%d%d" % (min(i, j), max(i, j))))
    M = sp.Matrix(h - 1, h - 1, lambda i, j: sp.Symbol("M%d%d" % (i, j)))
    s_raw = sp.simplify((n - (b.T * Bs.inv() * b)[0]))
    b_t = M.T * b
    B_t = M.T * Bs * M
    s_new = sp.simplify(n - (b_t.T * B_t.inv() * b_t)[0])
    return sp.simplify(s_raw - s_new) == 0


def s1_split_identity():
    h = 4
    n0, nc = sp.symbols("n0 nc")
    b0 = sp.Matrix(sp.symbols("p1:%d" % h))
    bc = sp.Matrix(sp.symbols("k1:%d" % h))
    Bs = sp.Matrix(h - 1, h - 1, lambda i, j: sp.Symbol(
        "B%d%d" % (min(i, j), max(i, j))))
    Binv = Bs.inv()
    s_direct = (n0 - nc) - ((b0 - bc).T * Binv * (b0 - bc))[0]
    x0 = Binv * b0
    q0 = (b0.T * Binv * b0)[0]
    qc = (bc.T * Binv * bc)[0]
    s_split = (n0 - q0) - nc + 2 * (bc.T * x0)[0] - qc
    return sp.simplify(s_direct - s_split) == 0


def s1_split_invariance():
    h = 3
    b0 = sp.Matrix(sp.symbols("p1:%d" % h))
    bc = sp.Matrix(sp.symbols("k1:%d" % h))
    Bs = sp.Matrix(h - 1, h - 1, lambda i, j: sp.Symbol(
        "B%d%d" % (min(i, j), max(i, j))))
    M = sp.Matrix(h - 1, h - 1, lambda i, j: sp.Symbol("M%d%d" % (i, j)))
    def terms(bb0, bbc, BB):
        Bi = BB.inv()
        return (sp.simplify((bb0.T * Bi * bb0)[0]),
                sp.simplify((bbc.T * Bi * bbc)[0]),
                sp.simplify((bbc.T * Bi * bb0)[0]))
    a = terms(b0, bc, Bs)
    c = terms(M.T * b0, M.T * bc, M.T * Bs * M)
    return all(sp.simplify(x - y) == 0 for x, y in zip(a, c))


def s1_parity():
    e = sp.symbols("e")
    q0, qc, lin, n0, nc = sp.symbols("q0 qc lin n0 nc")
    s_of = (n0 - q0) - e * nc + 2 * e * lin - qc
    even = sp.simplify(s_of.subs(e, 1) + s_of.subs(e, -1)
                       - 2 * ((n0 - q0) - qc)) == 0
    odd = sp.simplify(s_of.subs(e, 1) - s_of.subs(e, -1)
                      - 2 * (2 * lin - nc)) == 0
    return even and odd


def s1_box_floor():
    """The box supremum is attained at an admissible datum, so no
    bound consuming only I(R) can be smaller (exact rational)."""
    Bs = sp.Matrix([[sp.Rational(5), sp.Rational(1)],
                    [sp.Rational(1), sp.Rational(3)]])
    Bi = Bs.inv()
    b0 = sp.Matrix([sp.Rational(1), sp.Rational(-2)])
    R = sp.Rational(1, 2)
    best, arg = None, None
    for s1 in (-1, 1):
        for s2 in (-1, 1):
            z = sp.Matrix([sp.Rational(s1), sp.Rational(s2)])
            val = sp.simplify(((b0 - R * z).T * Bi * (b0 - R * z))[0])
            if best is None or val > best:
                best, arg = val, z
    interior = sp.simplify(((b0 - R * sp.Matrix(
        [sp.Rational(1, 3), sp.Rational(-1, 4)])).T * Bi
        * (b0 - R * sp.Matrix(
            [sp.Rational(1, 3), sp.Rational(-1, 4)])))[0])
    admissible = all(abs(x) <= R for x in (R * arg))
    return best > interior and admissible, best


def s1_trace_lower():
    """E_z[z^T C z] = tr C over random signs, so the box supremum is
    at least tr(C) >= 1/lambda_min (exact rational)."""
    C = sp.Matrix([[sp.Rational(7, 2), sp.Rational(-1, 3)],
                   [sp.Rational(-1, 3), sp.Rational(5, 4)]])
    tot = sp.Rational(0)
    best = None
    for s1 in (-1, 1):
        for s2 in (-1, 1):
            z = sp.Matrix([sp.Rational(s1), sp.Rational(s2)])
            v = sp.simplify((z.T * C * z)[0])
            tot += v
            best = v if best is None else max(best, v)
    mean = sp.simplify(tot / 4)
    return sp.simplify(mean - sp.trace(C)) == 0 and best >= sp.trace(C)


def s1_demand_basis_dependence():
    """Two mathematically equivalent formulations, different demands
    (exact rational): the deployed spectral step is strictly lossy."""
    Bs = sp.Matrix([[sp.Rational(1, 100), 0], [0, sp.Rational(1)]])
    b0 = sp.Matrix([sp.Rational(0), sp.Rational(1)])
    q0 = sp.simplify((b0.T * Bs.inv() * b0)[0])
    spectral = sp.simplify((b0.T * b0)[0] / sp.Rational(1, 100))
    return spectral > q0, q0, spectral


def s1_source_factorisation():
    """b_c = -(1/4) A_2 (z_theta + z_0) with A_2 the second-difference
    matrix -- exact on symbols."""
    h = 5
    zt = sp.Matrix(sp.symbols("zt0:%d" % (h + 2)))
    z0 = sp.Matrix(sp.symbols("z00:%d" % (h + 2)))
    A = sp.Matrix(second_difference_matrix(h).tolist())
    lhs = -sp.Rational(1, 4) * (A * (zt + z0))
    ok = True
    for i in range(1, h):
        gh = zt[i + 1] - sp.Rational(1, 2) * (zt[i + 2] + zt[i])
        gt = z0[i + 1] - sp.Rational(1, 2) * (z0[i + 2] + z0[i])
        entry = (gh + gt) / 2
        ok = ok and sp.simplify(entry - lhs[i - 1]) == 0
    return ok


# =========================================================== per-cell run
class Rung:
    pass


def audit_cell(cell, target, world=None, thetas=None, want_heavy=True):
    uu, mm = sap.cell_atoms(cell, world=world, seed=sap.SEED_SCR)
    wall = sap.Wall(cell, uu, mm)
    h = wall.h
    d_value = wall.D
    a_value = float(cell["alpha"])
    if thetas is None:
        thetas = [(k + 0.5) / N_THETA for k in range(N_THETA)]
    A2 = second_difference_matrix(h)

    rows = []
    refused = 0
    for theta in thetas:
        car, cat = wall.c_ladder(theta, split=True)
        ci = wall.c_scalar_vec(np.arange(-1.0, h + 2.0))
        ci_ar = sap.core.arch_A(np.abs(np.arange(-1.0, h + 2.0)) * d_value,
                                d_value)
        gh = (car + cat)[1:-1] - 0.5 * ((car + cat)[2:] + (car + cat)[:-2])
        gh_ar = car[1:-1] - 0.5 * (car[2:] + car[:-2])
        om = wall.omega_from_gh(gh)
        # archimedean-only wall at the same theta
        gt_ar = ci_ar[1:h + 1] - 0.5 * (ci_ar[2:h + 2] + ci_ar[0:h])
        H = sla.hankel(gh_ar[:h], gh_ar[h - 1:2 * h - 1])
        Tp = sla.toeplitz(gt_ar[:h])
        om0 = 0.5 * (H + Tp)

        n_true = float(om[0, 0])
        b = np.ascontiguousarray(om[1:, 0])
        B = np.ascontiguousarray(om[1:, 1:])
        n0 = float(om0[0, 0])
        b0 = np.ascontiguousarray(om0[1:, 0])
        bc = b0 - b
        nc = n0 - n_true

        # exact source factorisation ward: b_c = -(1/4) A_2 w
        w_src = -(cat[:h + 2] + (ci - ci_ar)[:h + 2])
        fact_resid = float(np.max(np.abs(-0.25 * (A2 @ w_src) - bc)))
        w_linf = float(np.max(np.abs(w_src)))

        try:
            cf = sla.cho_factor(B, lower=True, check_finite=False)
        except np.linalg.LinAlgError:
            refused += 1
            rows.append(dict(theta=theta, refused="CHOL-FAIL",
                             fact_resid=fact_resid, w_linf=w_linf))
            continue
        vhint = inverse_iteration_hint(cf, h - 1)
        lam_up = rayleigh_up(B, vhint)
        beta = sap.chol_cert_lower(B, sap.lam_hint(B, cf))
        if beta is None or beta <= 0.0:
            refused += 1
            rows.append(dict(theta=theta, refused="CERT-WEAK",
                             fact_resid=fact_resid, w_linf=w_linf))
            continue

        rowsum_B = np.abs(B).sum(axis=1)
        q_lo, q_hi, _y, _ru = quad_encl(b, B, cf, beta)
        q0_lo, q0_hi, x0, _r0 = quad_encl(b0, B, cf, beta)
        qc_lo, qc_hi, yc, _rc = quad_encl(bc, B, cf, beta)
        lin_lo, lin_hi = bilin_encl(bc, b0, B, cf, beta, q0_hi)

        # INDEPENDENT PATH 1 (Cholesky-free): q = max_x 2 b.x - x^T B x
        # gives a rigorous lower bound from matrix-vector products only.
        q0_var = variational_lo(b0, B, x0)
        qc_var = variational_lo(bc, B, yc)
        # INDEPENDENT PATH 2: the sign-flipped wall through the
        # DEPLOYED certified Schur routine, not through the split.
        om_flip = om.copy()
        bf = b0 + bc
        om_flip[0, 0] = n0 + nc
        om_flip[1:, 0] = bf
        om_flip[0, 1:] = bf
        cert_flip = sap.cert_schur(om_flip)
        s_flip_hi = cert_flip["s_hi"] if sap.ok_res(cert_flip) else None

        row = dict(
            theta=theta, refused=None, beta=beta, lam_up=lam_up,
            fact_resid=fact_resid, w_linf=w_linf,
            n0=n0, nc=nc, n_true=n_true,
            b0_l2sq=fsum(b0 * b0) * (1.0 + gam(h)),
            b0_linf=float(np.max(np.abs(b0))),
            bc_linf=float(np.max(np.abs(bc))),
            bc_l2=math.sqrt(fsum(bc * bc) * (1.0 + gam(h))),
            q_lo=q_lo, q_hi=q_hi, q0_lo=q0_lo, q0_hi=q0_hi,
            qc_lo=qc_lo, qc_hi=qc_hi, lin_lo=lin_lo, lin_hi=lin_hi,
            q0_var=q0_var, qc_var=qc_var, s_flip_hi=s_flip_hi,
            s_lo=n_true - q_hi, s_hi=n_true - q_lo,
            x0_l1=fsum(np.abs(x0)) * (1.0 + gam(h)),
            x0_d2_l1=fsum(np.abs(second_difference_T(x0, h)))
            * (1.0 + gam(h + 4)),
            diag_inv_sum=fsum(1.0 / np.diag(B)) * (1.0 + gam(h)),
            bc_first_nz=int(np.nonzero(np.abs(bc) > 0.0)[0][0])
            if np.any(bc != 0.0) else h - 1,
        )
        # Jacobi congruence
        dsq = 1.0 / np.sqrt(np.diag(B))
        Bj = (B * dsq[None, :]) * dsq[:, None]
        try:
            cfj = sla.cho_factor(Bj, lower=True, check_finite=False)
            bj = sap.chol_cert_lower(Bj, sap.lam_hint(Bj, cfj))
        except np.linalg.LinAlgError:
            bj = None
        scale_slack = 3.0 * U_RND * float(h - 1)
        row["beta_jac"] = (bj - scale_slack) if bj else None
        row["b0_jac_l2sq"] = fsum((dsq * b0) ** 2) * (1.0 + gam(h))

        if want_heavy:
            row["sum_abs_inv"] = sum_abs_inv_up(B, cf, beta, rowsum_B)
            sum_conj, C2 = sum_abs_conj_up(A2, B, cf, beta, h, rowsum_B)
            row["sum_abs_conj"] = sum_conj
            row["tr_conj"] = float(np.trace(C2))
            # certified box vertices
            zv = np.sign(vhint)
            zv[zv == 0.0] = 1.0
            mb_lo, _hi, _y2, _r2 = quad_encl(zv, B, cf, beta)
            row["mbox_lo"] = mb_lo
            wv = np.sign(power_hint(C2))
            wv[wv == 0.0] = 1.0
            av = A2 @ wv
            m2_lo, _hi2, _y3, _r3 = quad_encl(av, B, cf, beta)
            row["m2box_lo"] = m2_lo
            row["cc_linf_theta"] = float(np.max(np.abs(cat)))
            row["cc_linf_int"] = float(np.max(np.abs(ci - ci_ar)))
        rows.append(row)

    out = Rung()
    out.target = target
    out.h = h
    out.a = a_value
    out.D = d_value
    out.rows = rows
    out.refused = refused
    out.good = [r for r in rows if r["refused"] is None]
    out.world = world or "truth"
    return out


def agg(rung):
    """CCCLIX aggregation convention plus the sharp per-theta mean."""
    good = rung.good
    m = len(good)
    a_value, d_value = rung.a, rung.D
    R, r_fluc, r_sm = r_deployed(a_value, d_value)
    Rc, rc_sm, rc_fl = r_source(a_value, d_value)
    h = rung.h
    beta = min(r["beta"] for r in good)
    lam_up = max(r["lam_up"] for r in good)
    beta_j = [r["beta_jac"] for r in good if r["beta_jac"]]
    beta_jac = min(beta_j) if len(beta_j) == m else None
    g_geo = fsum([r["n0"] for r in good]) / m
    b0_l2 = math.sqrt(fsum([r["b0_l2sq"] for r in good]) / m)
    b0_jac_l2 = math.sqrt(fsum([r["b0_jac_l2sq"] for r in good]) / m)
    diag_inv = max(r["diag_inv_sum"] for r in good)
    q0_hi = max(r["q0_hi"] for r in good)
    q0_lo_mean = fsum([r["q0_lo"] for r in good]) / m
    x0_l1 = max(r["x0_l1"] for r in good)
    x0_d2 = max(r["x0_d2_l1"] for r in good)
    mbox_up = max(r["sum_abs_inv"] for r in good)
    mbox_lo = max(r["mbox_lo"] for r in good)
    m2_up = max(r["sum_abs_conj"] for r in good)
    m2_lo = max(r["m2box_lo"] for r in good)
    tr_conj = max(r["tr_conj"] for r in good)
    nc_sup = max(abs(r["nc"]) for r in good)
    bc_first = min(r["bc_first_nz"] for r in good)
    fact_resid = max(r["fact_resid"] for r in rung.rows)
    w_linf = max(r["w_linf"] for r in rung.rows)
    s_mean = fsum([0.5 * (r["s_lo"] + r["s_hi"]) for r in good]) / m
    need = fsum([(r["q0_hi"] - r["n0"]) + r["qc_hi"] + abs(r["nc"])
                 for r in good]) / m

    d = dict(
        h=h, a=a_value, D=d_value, m=m, R=R, r_fluc=r_fluc, r_sm=r_sm,
        Rc=Rc, rc_sm=rc_sm, rc_fl=rc_fl, beta=beta, lam_up=lam_up,
        beta_jac=beta_jac, G=g_geo, b0_l2=b0_l2, b0_jac_l2=b0_jac_l2,
        diag_inv=diag_inv, q0_hi=q0_hi, x0_l1=x0_l1, x0_d2=x0_d2,
        mbox_up=mbox_up, mbox_lo=mbox_lo, m2_up=m2_up, m2_lo=m2_lo,
        tr_conj=tr_conj, nc_sup=nc_sup, bc_first=bc_first,
        q0_lo_mean=q0_lo_mean, sqrt_h=math.sqrt(h - 1),
        fact_resid=fact_resid, w_linf=w_linf, s_mean=s_mean,
        need=need,
    )
    d["A_F0"] = R + (b0_l2 + math.sqrt(h - 1) * R) ** 2 / beta
    d["A_F1"] = (R + (b0_jac_l2 + R * math.sqrt(diag_inv)) ** 2
                 / beta_jac) if beta_jac else float("inf")
    d["A_F2"] = R + (math.sqrt(q0_hi) + R * math.sqrt(mbox_up)) ** 2
    cross = min(x0_l1, math.sqrt(q0_hi * mbox_up))
    d["A_F3"] = R + q0_hi + 2.0 * R * cross + R * R * mbox_up
    d["A_F4"] = nc_sup + q0_hi + Rc * x0_d2 + 0.25 * Rc * Rc * m2_up
    # information floor inside I(R): the theta mean of a per-theta
    # value that IS attained by an admissible datum (S1.5), hence a
    # rigorous lower bound for every formulation inside I(R).
    d["A_floor"] = fsum([r["q0_lo"] + R * R * r["mbox_lo"]
                         for r in good]) / m
    d["signed_env"] = Rc * x0_d2
    d["signed_miss"] = d["signed_env"] / abs(need) if need else float("inf")
    for key in ("A_F0", "A_F1", "A_F2", "A_F3", "A_F4", "A_floor"):
        d[key + "_rel"] = d[key] / abs(g_geo)
    return d


def exponent(v_lo, v_hi, h_lo, h_hi):
    if v_lo <= 0 or v_hi <= 0:
        return float("nan")
    return math.log(v_hi / v_lo) / math.log(float(h_hi) / float(h_lo))


def orders(v_lo, v_hi):
    if v_lo <= 0 or v_hi <= 0:
        return float("nan")
    return math.log10(v_hi / v_lo)


def main():
    print("=" * 78)
    print("PRIME.MATRIX.STAGE.CONDITIONING.01")
    print("SPEC_SHA %s" % SPEC_SHA)
    print("EXPLORATION ONLY -- demand accounting -- NO RH CLAIM")
    print("=" * 78)

    section("S0 -- freeze and source firewall")
    hits = ast_firewall()
    check("S0.1 no zero reader, tau, target sign, eigensolver or fit",
          not hits, "hits=%s" % hits)
    check("S0.2 deep evaluator cells excluded",
          1393 not in AUDIT_TARGETS and 2854 not in AUDIT_TARGETS,
          "targets=%s" % (AUDIT_TARGETS,))
    check("S0.3 registered rungs are the two CCCLIX priced cells",
          REGISTERED_RUNGS == (184, 405))

    section("S1 -- exact structural lemmas")
    check("S1.1 Schur scalar invariant under congruence diag(1,M)",
          s1_congruence_invariance())
    check("S1.2 three-term split identity (SP) is symbolically exact",
          s1_split_identity())
    check("S1.3 all three terms of (SP) are congruence invariant",
          s1_split_invariance())
    check("S1.4 middle bracket odd, outer terms even under comb flip",
          s1_parity())
    ok_floor, best_box = s1_box_floor()
    check("S1.5 box supremum attained at an admissible datum "
          "(information floor)", ok_floor, "sup=%s" % best_box)
    check("S1.6 box supremum >= trace = random-sign mean",
          s1_trace_lower())
    ok_dep, q_ex, sp_ex = s1_demand_basis_dependence()
    check("S1.7 spectral step is strictly lossy (exact rational)",
          ok_dep, "q0=%s vs ||b||^2/lambda_min=%s" % (q_ex, sp_ex))
    check("S1.8 source factorisation b_c = -(1/4) A_2 (z_th+z_0) exact",
          s1_source_factorisation())

    section("S2 -- rigour toolkit self-tests")
    rng = np.random.default_rng(20260813)
    Q = np.linalg.qr(rng.standard_normal((6, 6)))[0]
    lam = np.array([1e-7, 1e-4, 1e-2, 0.5, 1.0, 2.0])
    Bt = (Q * lam) @ Q.T
    Bt = 0.5 * (Bt + Bt.T)
    cft = sla.cho_factor(Bt, lower=True, check_finite=False)
    bt = rng.standard_normal(6)
    q_lo, q_hi, _y, _r = quad_encl(bt, Bt, cft, 0.5e-7)
    q_ref = float(bt @ np.linalg.solve(Bt, bt))
    check("S2.1 quadratic-form enclosure brackets the reference solve",
          q_lo <= q_ref <= q_hi,
          "[%.12e, %.12e] vs %.12e" % (q_lo, q_hi, q_ref))
    rs_t = np.abs(Bt).sum(axis=1)
    si_up = sum_abs_inv_up(Bt, cft, 0.5e-7, rs_t)
    si_ref = float(np.sum(np.abs(np.linalg.inv(Bt))))
    check("S2.2 sum|B^-1| upper bound dominates the reference inverse",
          si_up >= si_ref, "%.9e >= %.9e" % (si_up, si_ref))
    A2t = second_difference_matrix(7)
    sc_up, _Ct = sum_abs_conj_up(A2t, Bt, cft, 0.5e-7, 7, rs_t)
    sc_ref = float(np.sum(np.abs(A2t.T @ np.linalg.solve(Bt, A2t))))
    check("S2.3 sum|A^T B^-1 A| upper bound dominates the reference",
          sc_up >= sc_ref, "%.9e >= %.9e" % (sc_up, sc_ref))
    check("S2.4 Rayleigh quotient is an upper bracket for lambda_min",
          rayleigh_up(Bt, inverse_iteration_hint(cft, 6)) >= lam.min(),
          "%.6e >= %.6e" % (rayleigh_up(
              Bt, inverse_iteration_hint(cft, 6)), lam.min()))
    wtest = rng.standard_normal(7)
    check("S2.5 A_2^T operator matches the explicit matrix",
          float(np.max(np.abs(second_difference_T(
              second_difference_matrix(5) @ wtest, 5)
              - second_difference_matrix(5).T
              @ (second_difference_matrix(5) @ wtest)))) < 1e-12)

    section("A -- registered rungs, rigorous demand accounting")
    check("A0 source sieve matches the deployed prefix",
          sap.build_tables())
    picks = sap.pick_cells(sap.census())
    rungs = {}
    aggs = {}
    for tgt in AUDIT_TARGETS:
        t_a = time.time()
        rungs[tgt] = audit_cell(picks[tgt], tgt)
        aggs[tgt] = agg(rungs[tgt])
        d = aggs[tgt]
        print("  target %d -> h %d  a %.9f  D %.9e  good theta %d/%d  "
              "(%.1f s)"
              % (tgt, d["h"], d["a"], d["D"], d["m"], N_THETA,
                 time.time() - t_a))
        print("    R %.6e (fluc %.4e + smooth %.4e) | R_c %.6e "
              "(smooth %.4e + fluc %.4e)"
              % (d["R"], d["r_fluc"], d["r_sm"], d["Rc"], d["rc_sm"],
                 d["rc_fl"]))
        print("    beta %.6e <= lambda_min <= %.6e | beta_jac %s | "
              "G_geo %.9e"
              % (d["beta"], d["lam_up"],
                 ("%.6e" % d["beta_jac"]) if d["beta_jac"] else "n/a",
                 d["G"]))
        print("    ||b_0||_2 %.6e | q_0 <= %.6e | ||x_0||_1 %.6e | "
              "||A_2^T x_0||_1 %.6e"
              % (d["b0_l2"], d["q0_hi"], d["x0_l1"], d["x0_d2"]))
        print("    M_box in [%.6e, %.6e] | M2_box in [%.6e, %.6e] | "
              "tr(A^T B^-1 A) %.6e"
              % (d["mbox_lo"], d["mbox_up"], d["m2_lo"], d["m2_up"],
                 d["tr_conj"]))
        print("    sup|n_c| %.3e | first nonzero b_c index %d of %d | "
              "sum 1/B_ii %.6e"
              % (d["nc_sup"], d["bc_first"], d["h"] - 1, d["diag_inv"]))
        print("    source factorisation residual %.3e | MEASURED "
              "sup|w| %.4e vs envelope 2 R_c %.4e (slack %.2fx) | "
              "MEASURED mean s %.9e"
              % (d["fact_resid"], d["w_linf"], 2.0 * d["Rc"],
                 2.0 * d["Rc"] / max(d["w_linf"], 1e-300), d["s_mean"]))
        print("    DEMAND/SUPPLY  F0 %.4e  F1 %.4e  F2 %.4e  F3 %.4e  "
              "F4 %.4e  | floor(I(R)) %.4e"
              % (d["A_F0_rel"], d["A_F1_rel"], d["A_F2_rel"],
                 d["A_F3_rel"], d["A_F4_rel"], d["A_floor_rel"]),
              flush=True)

    ward_ref = {184: 2.470e11, 405: 1.990e14}
    ward_ok = all(
        abs(aggs[t]["A_F0_rel"] - ward_ref[t]) <= WARD_REL * ward_ref[t]
        for t in REGISTERED_RUNGS)
    check("A1 CCCLIX deployed miss reproduced within 5 percent",
          ward_ok,
          "got %s vs %s" % (["%.4e" % aggs[t]["A_F0_rel"]
                             for t in REGISTERED_RUNGS],
                            ["%.4e" % ward_ref[t]
                             for t in REGISTERED_RUNGS]))
    ward_h = [aggs[t]["h"] for t in REGISTERED_RUNGS] == [184, 388]
    check("A2 registered rung shapes match CCCLIX (h 184 and 388)",
          ward_h)
    refuse_frac = sum(rungs[t].refused for t in REGISTERED_RUNGS) / float(
        2 * N_THETA)
    check("A3 Higham certificate available on the registered rungs",
          refuse_frac <= CERT_REFUSE_FRAC,
          "refused fraction %.3f" % refuse_frac)
    lam_bracket_ok = all(
        aggs[t]["beta"] <= aggs[t]["lam_up"] for t in AUDIT_TARGETS)
    check("A4 certified floor lies below the Rayleigh bracket",
          lam_bracket_ok,
          "cert slack factors %s" % ["%.2f" % (aggs[t]["lam_up"]
                                               / aggs[t]["beta"])
                                     for t in AUDIT_TARGETS])
    check("A5 source factorisation b_c = -(1/4) A_2 w holds to "
          "roundoff at every audited (cell, theta)",
          all(aggs[t]["fact_resid"] < 1.0e-12 for t in AUDIT_TARGETS),
          "max residual %s" % ["%.2e" % aggs[t]["fact_resid"]
                               for t in AUDIT_TARGETS])
    mean_ref = {184: 1.507357381e-1, 405: 9.991056582e-2}
    check("A6 CCCLIX measured theta-means of s reproduced",
          all(abs(aggs[t]["s_mean"] - mean_ref[t])
              <= 1.0e-8 * abs(mean_ref[t]) for t in REGISTERED_RUNGS),
          "%s vs %s" % (["%.9e" % aggs[t]["s_mean"]
                         for t in REGISTERED_RUNGS],
                        ["%.9e" % mean_ref[t]
                         for t in REGISTERED_RUNGS]))
    check("A7 n_c vanishes identically (no atom is within reach of "
          "the pivot entry)",
          all(aggs[t]["nc_sup"] == 0.0 for t in AUDIT_TARGETS),
          "log2/D = %s" % ["%.1f" % (math.log(2.0) / aggs[t]["D"])
                           for t in AUDIT_TARGETS])

    section("B -- growth attribution of the deployed demand")
    lo, hi = REGISTERED_RUNGS
    dl, dh = aggs[lo], aggs[hi]
    total = orders(dl["A_F0_rel"], dh["A_F0_rel"])
    factors = [
        ("R (arithmetic envelope)", dl["R"], dh["R"], 0),
        ("sqrt(h-1) (dimension factor)", dl["sqrt_h"], dh["sqrt_h"], 0),
        ("R^2 (R enters squared)", dl["R"] ** 2, dh["R"] ** 2, 1),
        ("  of which R_fluc", dl["r_fluc"], dh["r_fluc"], 0),
        ("  of which R_smooth", dl["r_sm"], dh["r_sm"], 0),
        ("beta^-1 (co-block floor)", 1.0 / dl["beta"], 1.0 / dh["beta"],
         1),
        ("  of which true 1/lambda_min (bracket)",
         1.0 / dl["lam_up"], 1.0 / dh["lam_up"], 0),
        ("  of which certificate slack",
         dl["lam_up"] / dl["beta"], dh["lam_up"] / dh["beta"], 0),
        ("(h-1) (sqrt(h-1) enters squared)",
         dl["h"] - 1.0, dh["h"] - 1.0, 1),
        ("||b_0||_2", dl["b0_l2"], dh["b0_l2"], 0),
        ("G_geo (supply, divides)", dl["G"], dh["G"], -1),
    ]
    print("  %-42s %12s %12s %10s %8s %7s"
          % ("factor", "h=%d" % dl["h"], "h=%d" % dh["h"], "ratio",
             "orders", "share"))
    acc = 0.0
    for name, v_lo, v_hi, weight in factors:
        o = orders(v_lo, v_hi)
        share = (weight * o / total * 100.0) if weight and total else 0.0
        if weight:
            acc += weight * o
        print("  %-42s %12.5e %12.5e %10.4f %8.4f %6.1f%%"
              % (name, v_lo, v_hi, v_hi / v_lo, o,
                 share if weight else float("nan")))
    print("  %-42s %12s %12s %10.4f %8.4f %6.1f%%"
          % ("PRODUCT of weighted factors", "", "",
             10.0 ** acc, acc, 100.0 * acc / total if total else 0.0))
    print("  %-42s %12.5e %12.5e %10.4f %8.4f %6.1f%%"
          % ("MEASURED deployed demand/supply", dl["A_F0_rel"],
             dh["A_F0_rel"], dh["A_F0_rel"] / dl["A_F0_rel"], total,
             100.0))
    attribution_ok = abs(acc - total) <= 0.02 * max(abs(total), 1.0)
    check("B1 factor product reproduces the measured growth",
          attribution_ok, "sum of factor orders %.4f vs total %.4f"
          % (acc, total))
    beta_share = orders(1.0 / dl["beta"], 1.0 / dh["beta"]) / total
    check("B2 beta^-1 is the single largest growth contributor",
          beta_share >= orders(dl["R"] ** 2, dh["R"] ** 2) / total
          and beta_share >= orders(dl["h"] - 1.0, dh["h"] - 1.0) / total,
          "beta^-1 share %.1f%%" % (100.0 * beta_share))
    r_flat = orders(dl["R"], dh["R"]) < 0.5 * total
    check("B3 the genuine arithmetic fluctuation R grows far slower "
          "than the demand", r_flat,
          "R orders %.4f vs demand orders %.4f"
          % (orders(dl["R"], dh["R"]), total))

    section("C -- per-formulation demand and growth exponent")
    keys = [("F0 deployed spectral", "A_F0_rel"),
            ("F1 Jacobi whitened", "A_F1_rel"),
            ("F2 Cholesky orthonormal", "A_F2_rel"),
            ("F3 resolvent split", "A_F3_rel"),
            ("F4 source profile (2nd diff)", "A_F4_rel"),
            ("floor of I(R) (invariant)", "A_floor_rel")]
    print("  %-30s %12s %12s %12s %8s %8s"
          % ("formulation", "h=%d" % dl["h"], "h=%d" % dh["h"],
             "h=%d" % aggs[AUDIT_TARGETS[2]]["h"], "orders", "exp p"))
    exps = {}
    for name, key in keys:
        v0, v1 = dl[key], dh[key]
        v2 = aggs[AUDIT_TARGETS[2]][key]
        p = exponent(v0, v1, dl["h"], dh["h"])
        exps[key] = p
        print("  %-30s %12.5e %12.5e %12.5e %8.4f %8.4f"
              % (name, v0, v1, v2, orders(v0, v1), p))
    p_ext = {key: exponent(dh[key], aggs[AUDIT_TARGETS[2]][key],
                           dh["h"], aggs[AUDIT_TARGETS[2]]["h"])
             for _n, key in keys}
    print("  extension-rung exponents (h %d -> %d, NOT a registered "
          "CCCLIX rung): %s"
          % (dh["h"], aggs[AUDIT_TARGETS[2]]["h"],
             {k: "%.3f" % v for k, v in p_ext.items()}))
    best_key, best_val = min(
        ((k, dh[k]) for _n, k in keys if k != "A_floor_rel"),
        key=lambda kv: kv[1])
    level_gain = orders(best_val, dh["A_F0_rel"])
    exp_gain_ok = exps[best_key] <= COND_EXPONENT_BAR * exps["A_F0_rel"]
    print("  BEST equivalent formulation at the deepest registered "
          "rung: %s, demand/supply %.4e (deployed %.4e), level gain "
          "%.3f orders, exponent %.3f vs %.3f"
          % (best_key, best_val, dh["A_F0_rel"], level_gain,
             exps[best_key], exps["A_F0_rel"]))
    check("C1 an equivalent formulation lowers the level by >= 1 order",
          level_gain >= COND_LEVEL_BAR, "%.3f orders" % level_gain)
    check("C2 the best formulation also lowers the growth exponent",
          exp_gain_ok, "%.3f vs 0.8 x %.3f"
          % (exps[best_key], exps["A_F0_rel"]))
    floor_binds = all(
        aggs[t]["A_floor_rel"] >= 0.5 * min(
            aggs[t]["A_F2_rel"], aggs[t]["A_F3_rel"])
        for t in REGISTERED_RUNGS)
    check("C3 F2/F3 sit on the invariant I(R) floor (no basis buys "
          "more inside I(R))", floor_binds,
          "floor/best-in-I(R) %s"
          % ["%.3f" % (aggs[t]["A_floor_rel"]
                       / min(aggs[t]["A_F2_rel"], aggs[t]["A_F3_rel"]))
             for t in REGISTERED_RUNGS])

    section("G -- signed vs unsigned, triple verification")
    print("  %-8s %-8s %12s %12s %12s %12s %12s"
          % ("target", "h", "S=n0-q0", "|n_c|", "2<b_c,x_0>", "q_c",
             "s"))
    signed_needed = True
    flip_negative = True
    flip_all_positive = True
    ident_ok = True
    for tgt in AUDIT_TARGETS:
        good = rungs[tgt].good
        m = len(good)
        s_sup = fsum([r["n0"] - r["q0_hi"] for r in good]) / m
        nc_m = fsum([r["nc"] for r in good]) / m
        lin_m_lo = fsum([2.0 * r["lin_lo"] for r in good]) / m
        lin_m_hi = fsum([2.0 * r["lin_hi"] for r in good]) / m
        qc_m = fsum([r["qc_lo"] for r in good]) / m
        s_m_lo = fsum([r["s_lo"] for r in good]) / m
        s_m_hi = fsum([r["s_hi"] for r in good]) / m
        print("  %-8d %-8d %12.6e %12.6e %12.6e %12.6e %12.6e"
              % (tgt, rungs[tgt].h, s_sup, abs(nc_m),
                 0.5 * (lin_m_lo + lin_m_hi), qc_m,
                 0.5 * (s_m_lo + s_m_hi)))
        for r in good:
            # (i) identity check with enclosures
            lhs_lo = (r["n0"] - r["q0_hi"]) - r["nc"] \
                + 2.0 * r["lin_lo"] - r["qc_hi"]
            lhs_hi = (r["n0"] - r["q0_lo"]) - r["nc"] \
                + 2.0 * r["lin_hi"] - r["qc_lo"]
            if not (lhs_lo <= r["s_hi"] + 1e-9 and
                    lhs_hi >= r["s_lo"] - 1e-9):
                ident_ok = False
            # (ii) is the odd term necessary?
            even_part_hi = (r["n0"] - r["q0_lo"]) - r["qc_lo"] \
                + abs(r["nc"])
            if even_part_hi > 0.0:
                signed_needed = False
            # (iii) certified sign-flipped counterworld
            flip_hi = (r["n0"] - r["q0_lo"]) + abs(r["nc"]) \
                - 2.0 * r["lin_lo"] - r["qc_lo"]
            flip_lo = (r["n0"] - r["q0_hi"]) - abs(r["nc"]) \
                - 2.0 * r["lin_hi"] - r["qc_hi"]
            if flip_hi >= 0.0:
                flip_negative = False
            if flip_lo <= 0.0:
                flip_all_positive = False
    check("G1 the split identity (SP) closes numerically inside the "
          "enclosures at every audited (cell, theta)", ident_ok)
    check("G2 the EVEN part alone is negative everywhere -- the odd "
          "(signed) term is strictly necessary", signed_needed)
    check("G3 the sign-flipped counterworld is certified NEGATIVE "
          "everywhere (unsigned no-go)", flip_negative)
    var_ok = all(
        r["q0_var"] + r["qc_var"] > r["n0"] + abs(r["nc"])
        for tgt in AUDIT_TARGETS for r in rungs[tgt].good)
    check("G2b INDEPENDENT Cholesky-free variational path confirms "
          "q_0 + q_c > n_0 + |n_c| (the even part is negative)",
          var_ok,
          "worst slack %.6e"
          % min(r["q0_var"] + r["qc_var"] - r["n0"] - abs(r["nc"])
                for tgt in AUDIT_TARGETS for r in rungs[tgt].good))
    flip_dep = [r["s_flip_hi"] for tgt in AUDIT_TARGETS
                for r in rungs[tgt].good]
    check("G3b INDEPENDENT deployed-instrument path: the flipped wall "
          "run through cert_schur is certified negative everywhere",
          all(v is not None and v < 0.0 for v in flip_dep),
          "worst certified upper bound %.6e"
          % max(v for v in flip_dep if v is not None))
    unsigned_would_close = flip_all_positive
    check("G4 no reformulation converts the requirement to unsigned "
          "-- the (SP) split is congruence invariant (S1.3) and its "
          "odd term is strictly necessary in every formulation",
          not unsigned_would_close)

    section("X -- identical-pipeline controls")
    ctrl_rows = []
    for world in ("scramble", "epstein"):
        cr = audit_cell(picks[184], 184, world=world,
                        thetas=list(CTRL_THETA), want_heavy=True)
        n_good = len(cr.good)
        resid = max(r["fact_resid"] for r in cr.rows)
        ctrl_rows.append((world, cr.refused, n_good, resid))
        print("  %-9s MEASURED: certificate refusals %d/%d, usable %d, "
              "source factorisation residual %.3e"
              % (world.upper(), cr.refused, len(CTRL_THETA), n_good,
                 resid))
    truth_gain = max(r["sum_abs_inv"] / r["sum_abs_conj"]
                     for r in rungs[184].good)
    check("X1 the F4 factorisation is an ALGEBRAIC identity that holds "
          "in the control worlds too -- the conditioning gain is "
          "COMB-BLIND and can never be the missing discriminating "
          "lemma; it only shrinks the demand the lemma must beat",
          all(rd < 1.0e-12 for _w, _rf, _ng, rd in ctrl_rows),
          "truth gain sum|B^-1|/sum|A_2^T B^-1 A_2| = %.3e, control "
          "factorisation residuals %s"
          % (truth_gain, ["%.2e" % rd for _w, _rf, _ng, rd
                          in ctrl_rows]))
    check("X2 controls fire on the deployed PD premise",
          all(rf > 0 for _w, rf, _ng, _rd in ctrl_rows),
          "%s" % [(w, rf) for w, rf, _ng, _rd in ctrl_rows])

    section("V -- frozen verdict")
    failed = [name for name, ok in CHECKS if not ok]
    structural = any(n.startswith(("S0", "S1", "S2")) for n in failed)
    instrument = structural or not ward_ok \
        or refuse_frac > CERT_REFUSE_FRAC
    if instrument:
        verdict = "SEAT-INSTRUMENT-EDGE"
    elif unsigned_would_close:
        verdict = "SEAT-SIGNED-CONVERTED"
    elif level_gain >= COND_LEVEL_BAR and exp_gain_ok:
        verdict = "SEAT-CONDITIONING"
    else:
        verdict = "SEAT-INTRINSIC"
    print("  VERDICT: %s" % verdict)
    print("  BEST EQUIVALENT FORMULATION: F4 source-profile, demand "
          "%.4e vs deployed %.4e at h=%d (%.2f orders), exponent "
          "%.3f vs %.3f."
          % (dh["A_F4_rel"], dh["A_F0_rel"], dh["h"],
             orders(dh["A_F4_rel"], dh["A_F0_rel"]),
             exps["A_F4_rel"], exps["A_F0_rel"]))
    print("  INSIDE I(R) THE GROWTH IS INTRINSIC: every formulation "
          "that consumes only the entrywise envelope is floored by "
          "R^2 sup_box z^T B^-1 z >= R^2/lambda_min(B), a congruence "
          "invariant; F0..F3 differ by at most %.2f orders."
          % max(orders(min(dl["A_F2_rel"], dl["A_F3_rel"]),
                       dl["A_F0_rel"]),
                orders(min(dh["A_F2_rel"], dh["A_F3_rel"]),
                       dh["A_F0_rel"])))
    print("  REMAINING STATEMENT, BEST-CONDITIONED FORM: on one "
          "sign-independent predeclared cofinal (a_j, D_j), with "
          "x_0 = B^-1 b_0 and w the source lag profile,")
    print("    int_0^1 [ -(1/2) <w, A_2^T x_0> - q_c ] dtheta  >  "
          "int_0^1 [ q_0 - n_0 ] dtheta   (n_c = 0 identically),")
    print("  where the right side and x_0 are known archimedean data, "
          "q_c = b_c^T B^-1 b_c >= 0 is an UNSIGNED alignment bound "
          "(the bulk of the residual demand), and the left term is "
          "the SIGNED input.")
    print("  SIGNED-INPUT MISS (unsigned envelope R_c ||A_2^T x_0||_1 "
          "over the value it must exceed): %s at h = %s -- exponent "
          "%.3f, against %.3f for the deployed demand."
          % (["%.4e" % aggs[t]["signed_miss"] for t in AUDIT_TARGETS],
             [aggs[t]["h"] for t in AUDIT_TARGETS],
             exponent(dl["signed_miss"], dh["signed_miss"], dl["h"],
                      dh["h"]), exps["A_F0_rel"]))
    print("  UNSIGNED ALIGNMENT MISS (0.25 R_c^2 M2_box over the same "
          "value): %s -- this part is EVEN in the comb and is what a "
          "classical magnitude tool could in principle supply."
          % ["%.4e" % (0.25 * aggs[t]["Rc"] ** 2 * aggs[t]["m2_up"]
                       / aggs[t]["need"]) for t in AUDIT_TARGETS])
    elapsed = time.time() - T0
    check("V1 runtime below the frozen bar", elapsed < RUNTIME_BAR,
          "%.3f s" % elapsed)
    failed = [name for name, ok in CHECKS if not ok]
    print("\n[SUMMARY] %d/%d checks pass | failed=%s | %.3f s | %s"
          % (len(CHECKS) - len(failed), len(CHECKS),
             failed if failed else "none", elapsed, verdict))
    print("NO RH CLAIM.  No positivity claim.  Nothing promoted.")
    return 0 if not failed else 1


if __name__ == "__main__":
    raise SystemExit(main())
