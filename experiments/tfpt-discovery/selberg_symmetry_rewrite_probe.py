#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""selberg_symmetry_rewrite_probe -- PRIME.CORE.FLUCTUATION.ENERGY.02
(EXPLORATION ONLY, experiments/; TESTS B and C of the lead's campaign on
the FINAL LOCALIZED OBJECT of CCCXXV.  After CCCXXV the entire RH-side
burden is ONE scalar anti-cancellation inequality

        v_-^T X_h v_-  >=  -lam_min(G0_h),

left side a prime-only form at the geometry-only negative direction,
right side a geometry-only number, relative margin O(1e-4), the sign
carried by ALIGNMENT.  The frozen GATE RULE says only an INDEPENDENT
source for the sign counts.  Selberg's symmetry formula is a classical
UNCONDITIONAL identity connecting the linear and the quadratic von
Mangoldt terms -- this probe asks, exactly and on the ladder, whether it
is that source.  2026-08-13.)

NO RH claim.  No marker moves.  Writes nothing.  verification/ is
imported READ-ONLY.
"""

import ast
import hashlib
import math
import os
import sys
import time
from fractions import Fraction as Fr

import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
_VERIFY = os.path.abspath(os.path.join(_HERE, "..", "..",
                                       "verification"))
sys.path.insert(0, _HERE)
sys.path.insert(0, _VERIFY)

import v563_paper2_readouts as core                     # noqa: E402 RO
import exterior_square_factorization_probe as esq       # noqa: E402 RO
import core_fluctuation_normalform_probe as nf          # noqa: E402 RO

FROZEN_SPEC = """\
PRIME.CORE.FLUCTUATION.ENERGY.02 -- frozen spec v1 (2026-08-13).

THE OBJECT, inherited verbatim from CCCXXV and re-derived here, not
re-invented.  The CCXI representation is reused by import:
  [B-FREQ] K_h - (1/2)mu1 I = Gram_{rho*}(S), rho*_j = (2/L)(D_j
  - (1/2)mu1), S_j(v) = sum_p v_p sin(theta_j (p - (M-1)/2)), L = 2M-2;
  the seat is the 2 x 2 block in the CCXI carrier (t1, t2),
  Gam_2 - (1/2)mu1 I = G0 + X, G0 GEOMETRY ONLY (arch + smooth comb +
  window shift), X the PURE windowed prime fluctuation.  G0 carries
  exactly ONE negative direction v_- (geometry only), need :=
  -lam_min(G0), and the CCCXXV burden is v_-^T X v_- >= need.

TEST B.1 -- THE eq.-4 REPRESENTATION, DERIVED AND WARDED.  Two exact
reductions are chained, both registered:
  (i) T163 correlation theorem (core.lag_weights_from_v, verbatim):
      every seat entry is ONE linear functional of the lag vector,
      v^T A_h v = sum_d c_d w_d(v); by bilinearity the direction weight
      is W_v = v1^2 W11 + 2 v1 v2 W12 + v2^2 W22, so
      v_-^T X_h v_- = c_osc . W_v with c_osc = c_at - c_sm EXACTLY.
  (ii) T115/T170 tent-spline duality (core.atom_lags_at vs
      core.spline_project, verbatim): the tent deposit at position u
      dotted against any lag-weight vector W is the closed two-point
      read Phi_W(u) := spline_project(W, u, D, M), D = 2 alpha / M.
Chaining them gives the EXACT representation (eq. 4a), LINEAR in the
von Mangoldt data:
  (eq. 4a)  v_-^T X_h v_-  =  sum_g w^sm_g Phi_v(u_g)
                              -  sum_n (Lambda(n)/sqrt n) Phi_v(log n),
w^sm the smooth-comb (PNT main mass) quadrature weights, Phi_v the
GEOMETRY-ONLY window read of W_v.  AMENDMENT A1, disclosed: the lead's
eq. 4 was specified as a DOUBLE sum sum_{m,n} Lambda(m)Lambda(n)/
sqrt(mn) W_h(log m, log n).  That form does NOT exist for this object:
X is linear in the comb, hence v_-^T X v_- is a SINGLE sum and no
quadratic-in-Lambda kernel represents it.  The honest reading is kept
and the genuine double sum is delivered where it does exist (B.2).
Ward: |(eq. 4a) - v_-^T X v_-| / |v_-^T X v_-| <= 1e-10 per rung.

TEST B.2 -- WHERE THE DOUBLE SUM DOES LIVE, AND ITS EXACT STRUCTURE.
The CCCXXV quadratic supply Q2 = det X IS quadratic in Lambda, and the
same duality gives it in closed kernel form:
  X = sum_i w_i Theta(u_i), Theta(u) = [[Phi_11, Phi_12],
                                        [Phi_12, Phi_22]](u),
  (eq. 4b)  det X = (1/2) sum_{i,j} w_i w_j W_h(u_i, u_j),
            W_h(u, u') = phi(u)^T A phi(u'),
            phi = (Phi_11, Phi_22, Phi_12),
            A = [[0, 1, 0], [1, 0, 0], [0, 0, -2]],
whose prime-prime block is literally sum_{m,n} Lambda(m)Lambda(n)/
sqrt(mn) W_h(log m, log n).  W_h is EXACTLY RANK 3 and LORENTZIAN: the
rational congruence T^T A T = diag(2, -2, -2) over Q is verified in
Fractions -> inertia (1, 2, 0), the atom-coordinate transport of the
CCCXXV wedge kernel.  The SELBERG-DIRECTION question is then answered
by measurement, not assumption: on a uniform u-grid the exact variance
fractions explained by an anti-diagonal function g(u + u') (the Selberg
direction log(mn)) and by a diagonal function g(u - u') (the difference
direction log(m/n)) are computed; a finite mixture is reported as such.

TEST B.3 -- THE SELBERG REWRITE, EXECUTED EXACTLY ON THE LADDER.  The
identity (EXTERNAL-CITED: Selberg 1949, elementary PNT machinery)
  Lambda(n) log n + sum_{d|n} Lambda(d) Lambda(n/d)
      = sum_{d|n} mu(d) log^2(n/d)  =: L(n)
is warded TWICE: (a) EXACTLY, in integer arithmetic, by representing
all three terms as integer-coefficient quadratic forms in the log-primes
and comparing the coefficient tables for every n <= N_EXACT; (b)
numerically for every n <= N_max of the ladder.  With the geometry-only
kernel G_h(n) := Phi_v(log n) / (sqrt n log n) the prime sum of eq. 4a
is P_h = sum_n Lambda(n) log n G_h(n), and the identity rewrites it
EXACTLY as
  (eq. 5)  P_h = A_h - B_h,
  A_h := sum_{n <= N} L(n) G_h(n)                  (mu * log^2 side),
  B_h := sum_{m k <= N} Lambda(m) Lambda(k) G_h(mk) (prime-PAIR side),
so that v_-^T X v_- = Q_h - A_h + B_h.  B_h is a genuine double sum
whose kernel depends on (m, k) ONLY through the product mk, i.e. ONLY
through log m + log n: 100 percent Selberg direction, 0 percent
difference direction -- warded by the exact collision test (all pairs
with equal product carry a bit-identical kernel value).  THE DECISIVE
CENSUS is then per rung: demand need, Selberg-supplied Q_h - A_h,
residual B_h, and the total margin; plus the CANCELLATION DEPTH
(margin divided by the total absolute mass of the terms) BEFORE and
AFTER the rewrite -- the only honest measure of whether the identity
extracted the cancellation or deepened it.

TEST C -- ONLY AFTER THE IDENTITY.  The lead's order is strict: no
absolute estimate before the exact rewrite.  Three unconditional
readings are then priced, all EXTERNAL-CITED and none fitted:
  C1 POINTWISE NONNEGATIVITY.  L(n) = Lambda(n) log n + (Lambda*Lambda)
     (n) with both summands >= 0 gives 0 <= Lambda(n) log n <= L(n)
     pointwise, hence the alignment-free two-sided bound
     sum_{G>0} L G  >=  P  >=  sum_{G<0} L G, needing NO error term and
     NO prime alignment.  Is Q - P_ub >= need?
  C2 THE SELBERG ASYMPTOTIC.  sum_{n<=x} L(n) = 2 x log x + O(x) and
     (with sum_{n<=x} Lambda(n) log n = x log x + O(x), Chebyshev/
     Mertens) sum_{mk<=x} Lambda(m)Lambda(k) = x log x + O(x).  Exact
     DISCRETE Abel summation splits A_h = A_main + A_err and B_h =
     B_main + B_err with A_main, B_main computable from the main terms
     alone; |A_err| <= C_A V_h, |B_err| <= C_B V_h with V_h the exact
     weighted discrete total variation of G_h.  The constants C are
     MEASURED on the built range as max |remainder| / t, which is a
     LOWER bound on any true absolute constant -- so the priced
     envelope is OPTIMISTIC and its failure is conclusive.  Census:
     is (Q - A_main + B_main) - need > ENV?
  C3 THE NEUTRALITY WARD.  A_main - B_main == B_main identically (2 t
     log t minus t log t), hence A_err - B_err == P - P_main EXACTLY:
     the post-Selberg residual is bit-identical to the pre-Selberg one.
     Warded numerically; it is the sharpest statement of what the
     identity does and does not do to the burden.
No Vaughan / large-sieve / Hilbert bound is quoted as a number: each is
an absolute estimate of the SAME residual whose size is measured here
directly, and the measurement decides whether any absolute estimate can
close the inequality at all.

CONTROLS (must fire).  smooth world (comb -> 2 e^{u/2} du, no primes):
X == 0 identically, so eq. 4a degenerates to P == Q and the arithmetic
objects A_h, B_h -- which depend only on geometry and on the arithmetic
tables, NOT on the comb -- stay UNCHANGED; the identity A - B = P then
fails there by exactly the true alignment supply, which is precisely
WHERE the smooth world loses.  arithmetic scramble (a seeded
permutation of Lambda over the prime powers, positions kept): the
Selberg identity is arithmetic and must BREAK -- measured pointwise and
in the weighted rewrite.  position scramble (CCCXXV seed 1): the
alignment inequality must fail and the rewrite must mismatch.  Epstein
(x^2 + 5y^2) comb: a DIFFERENT arithmetic whose von Mangoldt analogue
does not satisfy the identity -- must break the rewrite.
SCREENS.  TAU_REP := shat - 1/2 is inherited from CCCXXV; every new
margin is screened log-log against tau_rep and against c_h with the
CCXI bar (|slope| <= 0.30 PASS, >= 0.70 RELOC).
ANTI-CIRCULARITY.  The kernel builders (W_v, Phi_v, the wedge kernel,
the geometry seat and the negative direction) are AST-scanned and may
see NO prime-side name; v_- is geometry-only by construction (it is the
bottom eigenvector of G0, which CCCXXV builds under its own AST scan)
and the reproduction of CCCXXV's need / v_-^T X v_- / margin is warded
against the imported module on a subset and against the PUBLISHED
CCCXXV trios on the full ladder.

VERDICT ENUM.  eq. 4: REPRESENTATION-EXACT / PARTIAL / REFUSED (with
the A1 typing of the double-sum form).  Rewrite: SELBERG-EXACT (the
identity holds and the rewrite wards) plus the direction typing.
GATE RULE: SELBERG-INDEPENDENT-SOURCE (the rewritten part carries the
sign by a smooth/unconditional statement) / SELBERG-PARTIAL /
SELBERG-INSUFFICIENT (the sign stays in the residual) -- decided by the
measured census and printed last with the measured seat.

SMOKE DISCLOSURE (mandatory).  Smoke rounds were run on four sample
rungs (kz 9, 40, 71, 121) before the SPEC_SHA was frozen: the eq.-4
duality, the sieve sizes, the identity ward, the A/B census and the
Abel envelope were checked there.  Construction-side amendments made in
smoke are listed as A1..A6 in the run header.  No gate, band or verdict
rule was changed after seeing a frozen number.
"""

# ---------------------------------------------------------------- frozen
KZMAX = 150
MIN_RUNGS = 40
REP_WARD = 1.0e-10        # eq. 4a representation ward (relative)
ID_WARD = 1.0e-10         # identity / rewrite wards (relative)
N_EXACT = 3000            # exact integer ward range for the identity
SUBSET_KZ = (9, 40, 71, 105, 121)
CTRL_KZ = 9
SCR_SEED = 1
SCR_RUNGS = 12
GRID_DIR = 192            # u-grid for the direction decomposition
SLOPE_PASS = 0.30
SLOPE_RELOC = 0.70
REG_C = 0.5
# CCCXXV published trios (CITED, never recomputed as a gate substitute)
PUB_NEED = (0.9429, 1.2050, 1.2690)
PUB_ALIGN = (1.500e-05, 9.207e-05, 2.730e-03)
PUB_QNEG = (0.9457, 1.2051, 1.2690)
BANNED_IDS = ("zetazero", "nzeros", "primerange", "isprime",
              "primepi", "nextprime", "prevprime")
# the kernel builders may see NO prime-side and NO observed-spectral
# object -- this is the AST-enforced anti-circularity
KER_BANNED = ("lam_tab", "u_all", "mu_all", "lam", "mangoldt", "prime",
              "comb", "atom", "mobius", "selberg", "shat", "tau",
              "margin", "need", "align", "verdict", "demand")
KER_FNS = ("w_lag_dir", "phi_read", "wedge_kernel_atom",
           "geo_seat", "geo_negdir")

SMOKE = bool(os.environ.get("TFPT_SEL_SMOKE"))

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


def ker_path_scan():
    """Anti-circularity: the kernel builders may not mention any
    prime-side or observed-spectral object."""
    src = open(os.path.abspath(__file__), encoding="utf-8").read()
    bad = []
    for node in ast.walk(ast.parse(src)):
        if not isinstance(node, ast.FunctionDef):
            continue
        if node.name not in KER_FNS:
            continue
        for sub in ast.walk(node):
            nm = None
            if isinstance(sub, ast.Name):
                nm = sub.id
            elif isinstance(sub, ast.Attribute):
                nm = sub.attr
            if nm and nm.lower() in KER_BANNED:
                bad.append("%s:%s" % (node.name, nm))
    return bad


# ------------------------------------------------------------ formatting
def trio(v):
    v = np.asarray(v, float)
    return float(np.min(v)), float(np.median(v)), float(np.max(v))


def f3(v):
    return "%.4f/%.4f/%.4f" % trio(v)


def e3(v):
    return "%.3e/%.3e/%.3e" % trio(v)


def d3(v):
    return "%+.3e/%+.3e/%+.3e" % trio(v)


def spearman(a, b):
    a, b = np.asarray(a, float), np.asarray(b, float)
    if len(a) < 3:
        return float("nan")
    ra = np.argsort(np.argsort(a)).astype(float)
    rb = np.argsort(np.argsort(b)).astype(float)
    ra -= ra.mean()
    rb -= rb.mean()
    dn = math.sqrt(float(ra @ ra) * float(rb @ rb))
    return float(ra @ rb) / dn if dn > 0 else float("nan")


def rel(a, b):
    return abs(a - b) / max(abs(a), abs(b), 1e-300)


# ============================================== the anti-circular builders
def w_lag_dir(w3, vv):
    """GEOMETRY + DIRECTION ONLY.  The T163 lag-weight vector of the
    quadratic form at the seat direction vv: W_v = v1^2 W11
    + 2 v1 v2 W12 + v2^2 W22, so that (any lag) . W_v is the value of
    the seat form at vv."""
    w11, w12, w22 = w3
    return (vv[0] * vv[0] * w11 + 2.0 * vv[0] * vv[1] * w12
            + vv[1] * vv[1] * w22)


def phi_read(ww, uu, dd, mm):
    """GEOMETRY ONLY.  The T170 closed two-point window read of a
    lag-weight vector at positions uu (vectorised core.spline_project,
    bit for bit)."""
    uu = np.asarray(uu, float)
    xx = uu / dd
    i0 = np.floor(xx).astype(np.int64)
    ff = xx - i0
    out = np.zeros_like(uu)
    k0 = (i0 >= 0) & (i0 < mm)
    out[k0] += (1.0 - ff[k0]) * ww[i0[k0]]
    i1 = i0 + 1
    k1 = (i1 >= 0) & (i1 < mm)
    out[k1] += ff[k1] * ww[i1[k1]]
    k2 = uu < dd
    out[k2] += (1.0 - uu[k2] / dd) * ww[0]
    return out


def wedge_kernel_atom(p11, p22, p12):
    """GEOMETRY ONLY.  W(u, u') = phi(u)^T A phi(u') with
    phi = (Phi_11, Phi_22, Phi_12) and A = [[0,1,0],[1,0,0],[0,0,-2]]:
    the atom-coordinate transport of the CCXI/CCCXXV wedge kernel."""
    return (np.outer(p11, p22) + np.outer(p22, p11)
            - 2.0 * np.outer(p12, p12))


def geo_seat(reads, dgeo, ll, mu):
    """GEOMETRY + GAMMA FACTOR + WINDOW ONLY.  The seat matrix of the
    prime-free world."""
    wgt = (2.0 / ll) * (dgeo - 0.5 * mu)
    return (reads * wgt[:, None]).T @ reads


def geo_negdir(g0):
    """GEOMETRY ONLY.  The single negative direction of the prime-free
    seat matrix and its depth."""
    ev, vc = np.linalg.eigh(g0)
    return vc[:, 0].copy(), -float(ev[0]), (float(ev[0]), float(ev[1]))


# ===================================================== arithmetic tables
def mobius_table(nmax):
    mu = np.ones(nmax + 1, dtype=np.int8)
    prime = np.ones(nmax + 1, dtype=bool)
    prime[:2] = False
    rt = int(math.isqrt(nmax))
    for p in range(2, rt + 1):
        if prime[p]:
            prime[p * p::p] = False
            mu[p::p] *= -1
            mu[p * p::p * p] = 0
    for p in range(rt + 1, nmax + 1):
        if prime[p]:
            mu[p::p] *= -1
    mu[0] = 0
    return mu


def spf_table(nmax):
    spf = np.zeros(nmax + 1, dtype=np.int64)
    for p in range(2, nmax + 1):
        if spf[p] == 0:
            spf[p::p] = np.where(spf[p::p] == 0, p, spf[p::p])
    return spf


def factor_map(n, spf):
    out = {}
    while n > 1:
        p = int(spf[n])
        e = 0
        while n % p == 0:
            n //= p
            e += 1
        out[p] = e
    return out


def _add(dct, i, j, c):
    key = (i, j) if i <= j else (j, i)
    dct[key] = dct.get(key, 0) + c
    if dct[key] == 0:
        del dct[key]


def selberg_exact_ward(nmax, spf):
    """EXACT INTEGER ward of Lambda(n) log n + (Lambda*Lambda)(n)
    == sum_{d|n} mu(d) log^2(n/d): all three terms are integer-coefficient
    quadratic forms in the log-primes; the coefficient tables are
    compared exactly.  Returns (n_checked, n_mismatch, first_bad)."""
    bad = None
    nbad = 0
    for n in range(2, nmax + 1):
        fac = factor_map(n, spf)
        ps = sorted(fac)
        lhs = {}
        if len(ps) == 1:                       # n = p^k
            p, k = ps[0], fac[ps[0]]
            _add(lhs, p, p, k)                 # Lambda(n) log n
            _add(lhs, p, p, k - 1)             # (Lambda * Lambda)(n)
        elif len(ps) == 2:                     # n = p^a q^b
            _add(lhs, ps[0], ps[1], 2)
        rhs = {}
        nsf = len(ps)
        for msk in range(1 << nsf):            # squarefree divisors d
            sgn = 1
            ex = dict(fac)
            for i in range(nsf):
                if msk >> i & 1:
                    sgn = -sgn
                    ex[ps[i]] -= 1
            for a in ps:                       # log^2(n/d)
                if ex[a] == 0:
                    continue
                for b in ps:
                    if ex[b] == 0 or b < a:
                        continue
                    cf = ex[a] * ex[a] if a == b else 2 * ex[a] * ex[b]
                    _add(rhs, a, b, sgn * cf)
        if lhs != rhs:
            nbad += 1
            if bad is None:
                bad = (n, dict(lhs), dict(rhs))
    return nmax - 1, nbad, bad


def congruence_rank3():
    """T^T A T = diag(2, -2, -2) over Q for the atom wedge form
    A = [[0,1,0],[1,0,0],[0,0,-2]] -> inertia (1, 2, 0)."""
    A = [[Fr(0), Fr(1), Fr(0)],
         [Fr(1), Fr(0), Fr(0)],
         [Fr(0), Fr(0), Fr(-2)]]
    T = [[Fr(1), Fr(1), Fr(0)],
         [Fr(1), Fr(-1), Fr(0)],
         [Fr(0), Fr(0), Fr(1)]]
    out = [[sum(T[k][i] * A[k][m] * T[m][j] for k in range(3)
                for m in range(3)) for j in range(3)] for i in range(3)]
    tgt = [[Fr(2), Fr(0), Fr(0)],
           [Fr(0), Fr(-2), Fr(0)],
           [Fr(0), Fr(0), Fr(-2)]]
    ok = all(out[i][j] == tgt[i][j] for i in range(3)
             for j in range(3))
    return ok, esq.ldl_inertia_fr(out)


class Arith(object):
    """The frozen arithmetic tables: von Mangoldt (reused from the
    verification module, READ-ONLY), mu * log^2, the prime-power pair
    table and the cumulative sums with their MEASURED remainders."""

    def __init__(self, nmax):
        self.N = nmax
        tt = np.arange(nmax + 1, dtype=float)
        self.t = tt
        lg = np.zeros(nmax + 1)
        lg[1:] = np.log(tt[1:])
        self.lg = lg
        self.tlog = np.zeros(nmax + 1)
        self.tlog[2:] = tt[2:] * lg[2:]
        self.inv = np.zeros(nmax + 1)
        self.inv[2:] = 1.0 / (np.sqrt(tt[2:]) * lg[2:])
        self.lam = np.asarray(core.LAM_TAB[:nmax + 1], float).copy()
        self.lamlog = self.lam * lg
        mu = mobius_table(nmax)
        lg2 = lg * lg
        LL = np.zeros(nmax + 1)
        for d in range(1, nmax + 1):
            m = int(mu[d])
            if m == 0:
                continue
            q = nmax // d
            LL[d::d] += m * lg2[1:q + 1]
        self.L = LL
        pp = np.nonzero(self.lam > 0.0)[0]
        self.pp = pp
        pr, wt, lf = [], [], []
        for m in pp:
            if 2 * int(m) > nmax:
                break
            kk = pp[pp <= nmax // int(m)]
            pr.append(int(m) * kk)
            wt.append(self.lam[m] * self.lam[kk])
            lf.append(np.full(len(kk), int(m), dtype=np.int64))
        self.prod = np.concatenate(pr).astype(np.int64)
        self.pwt = np.concatenate(wt)
        self.pfac = np.concatenate(lf)
        self.conv = np.bincount(self.prod, weights=self.pwt,
                                minlength=nmax + 1)
        self.dev_id = float(np.max(np.abs(
            self.lamlog + self.conv - self.L)))
        self.TL = np.cumsum(self.L)
        self.T2 = np.cumsum(self.conv)
        self.T1 = np.cumsum(self.lamlog)
        self.RA, self.CA = self._rem(self.TL, 2.0 * self.tlog)
        self.RB, self.CB = self._rem(self.T2, self.tlog)
        self.RP, self.CP = self._rem(self.T1, self.tlog)

    def _rem(self, cum, main):
        r = cum - main
        r = r - r[1]
        return r, float(np.max(np.abs(r[2:] / self.t[2:])))


def abel_main(gg, main, nn):
    """EXACT discrete Abel summation of a main term against the weight:
    sum_{n<=N} dMain(n) G(n) = Main(N) G(N) + sum_{n<N} Main(n)
    (G(n) - G(n+1))."""
    dg = gg[1:nn] - gg[2:nn + 1]
    return float(main[nn] * gg[nn] + np.dot(main[1:nn], dg))


def abel_var(gg, tt, nn):
    """The exact weighted discrete total variation that prices the
    remainder: sum_{n<N} n |G(n) - G(n+1)| + N |G(N)|."""
    dg = np.abs(gg[1:nn] - gg[2:nn + 1])
    return float(np.dot(tt[1:nn], dg) + tt[nn] * abs(gg[nn]))


# ============================================================ rung packing
def sel_rung(ar, kz, with_ops=True, **kw):
    """One ladder rung: the CCXI reads (reused), the CCCXXV alignment
    objects (re-derived), the eq.-4a representation and the exact
    Selberg rewrite census."""
    rg = esq.level_rung(kz, want_split=True, **kw)
    if rg is None:
        return None
    esq.level_reads(rg, with_ops=with_ops)
    mm, hh, ll, mu1, al = (rg["M"], rg["h"], rg["L"], rg["mu1"],
                           rg["alpha"])
    dd = 2.0 * al / mm
    c_geo = rg["c_ar"] + rg["c_sm"]
    c_osc = rg["c"] - c_geo
    d_geo = esq.grid_density(c_geo)
    d_flu = esq.grid_density(c_osc)
    reads = esq.sine_reads(core.parity_basis(hh, 2).T, mm)
    g0 = geo_seat(reads, d_geo, ll, mu1)
    xx = (reads * ((2.0 / ll) * d_flu)[:, None]).T @ reads
    vneg, need, g0ev = geo_negdir(g0)
    qneg = float(vneg @ (xx @ vneg))
    rg["need"], rg["q_neg"], rg["align"] = need, qneg, qneg - need
    rg["G0_ev"] = g0ev
    rg["D_lag"] = dd
    rg["detX"] = float(xx[0, 0] * xx[1, 1] - xx[0, 1] ** 2)
    # ---- eq. 4a: the T163 direction weight and its window read
    w_v = w_lag_dir(rg["W3"], vneg)
    rg["dev_t163"] = rel(float(c_osc @ w_v), qneg)
    ka = core.atoms_in(al)
    uu = np.asarray(core.U_ALL[:ka], float)
    rho = 0.5 * np.asarray(core.MU_ALL[:ka], float)
    if kw.get("comb") is not None:
        uu, rho = kw["comb"][0], 0.5 * np.asarray(kw["comb"][1], float)
    if kw.get("scramble_seed") is not None:
        rng = np.random.default_rng(kw["scramble_seed"])
        uu = np.sort(rng.uniform(0.0, 2.0 * al, size=ka))
    if kw.get("world") == "smooth":
        uu, msm = esq.smooth_comb(al)
        rho = 0.5 * msm
    phi_at = phi_read(w_v, uu, dd, mm)
    p_sum = float(rho @ phi_at)
    ug, mg = esq.smooth_comb(al)
    q_sum = float((0.5 * mg) @ phi_read(w_v, ug, dd, mm))
    rg["P"], rg["Q"] = p_sum, q_sum
    rg["dev_eq4"] = abs((q_sum - p_sum) - qneg) / max(abs(qneg), 1e-300)
    # ---- the exact Selberg rewrite in the geometry-only kernel
    nn = min(int(math.floor(math.exp(2.0 * al))), ar.N)
    gg = np.zeros(ar.N + 1)
    gg[2:] = phi_read(w_v, ar.lg[2:], dd, mm) * ar.inv[2:]
    gg[nn + 1:] = 0.0
    rg["Nsel"] = nn
    aa = float(np.dot(ar.L[:nn + 1], gg[:nn + 1]))
    msk = ar.prod <= nn
    bb = float(np.dot(ar.pwt[msk], gg[ar.prod[msk]]))
    pl = float(np.dot(ar.lamlog[:nn + 1], gg[:nn + 1]))
    rg["A"], rg["B"], rg["P_lin"] = aa, bb, pl
    rg["dev_plin"] = rel(pl, p_sum)
    # the pure identity ward under the geometry kernel (world-blind)
    rg["dev_ident"] = abs((aa - bb) - pl) / max(abs(pl), 1e-300)
    # the rewrite of THIS world's own prime sum (the control-sensitive
    # one: the identity is arithmetic, so a wrong arithmetic breaks it)
    rg["dev_rewrite"] = abs((aa - bb) - p_sum) / max(abs(p_sum),
                                                     1e-300)
    rg["sup_sel"] = q_sum - aa
    rg["mar_sel"] = (q_sum - aa) - need
    rg["mass_pre"] = abs(q_sum) + abs(p_sum)
    rg["mass_post"] = abs(q_sum) + abs(aa) + abs(bb)
    rg["depth_pre"] = abs(rg["align"]) / rg["mass_pre"]
    rg["depth_post"] = abs(rg["align"]) / rg["mass_post"]
    # ---- C1 pointwise nonnegativity (alignment-free, no error term)
    gp = np.where(gg > 0.0, gg, 0.0)
    gm = np.where(gg < 0.0, gg, 0.0)
    rg["P_ub"] = float(np.dot(ar.L[:nn + 1], gp[:nn + 1]))
    rg["P_lb"] = float(np.dot(ar.L[:nn + 1], gm[:nn + 1]))
    rg["c1_margin"] = (q_sum - rg["P_ub"]) - need
    rg["n_Gpos"] = int(np.sum(gg[2:nn + 1] > 0.0))
    rg["n_Gsup"] = int(np.sum(gg[2:nn + 1] != 0.0))
    # ---- C2 the unconditional Abel split with MEASURED constants
    adm = abel_main(gg, 2.0 * ar.tlog, nn)
    bdm = abel_main(gg, ar.tlog, nn)
    pdm = abel_main(gg, ar.tlog, nn)
    vh = abel_var(gg, ar.t, nn)
    rg["A_main"], rg["B_main"], rg["P_main"] = adm, bdm, pdm
    rg["A_err"], rg["B_err"] = aa - adm, bb - bdm
    rg["P_err"] = pl - pdm
    rg["TV"] = vh
    rg["ENV"] = (ar.CA + ar.CB) * vh
    rg["mar_main"] = (q_sum - adm + bdm) - need
    rg["dev_neutral"] = abs((rg["A_err"] - rg["B_err"]) - rg["P_err"]) \
        / max(abs(rg["P_err"]), 1e-300)
    # ---- the measured seat: dyadic profile of the running margin
    prof = []
    for r in range(0, 20):
        lo, hi = math.log(2.0 ** r), math.log(2.0 ** (r + 1))
        if lo >= 2.0 * al:
            break
        sel_a = (uu > lo) & (uu <= hi)
        sel_g = (ug > lo) & (ug <= hi)
        prof.append((r,
                     float((0.5 * mg[sel_g])
                           @ phi_read(w_v, ug[sel_g], dd, mm))
                     - float(rho[sel_a] @ phi_at[sel_a])))
    rg["dyad"] = prof
    rg["tau_rep"] = rg["shat"] - REG_C
    del reads, gg, gp, gm
    return rg


# ================================================================== main
def main():
    section("PRIME.CORE.FLUCTUATION.ENERGY.02 -- TEST B (Selberg "
            "symmetry rewrite of the final localized object) and TEST C "
            "(the residual after the identity)  (EXPLORATION ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s"
          % hashlib.sha256(FROZEN_SPEC.encode("utf-8")).hexdigest())
    print("    CODE_SHA = %s"
          % hashlib.sha256(open(os.path.abspath(__file__), "rb")
                           .read()).hexdigest()[:8])
    print("    NO RH claim; no marker moves; experiments/ only; "
          "writes nothing.")
    if SMOKE:
        print("    *** SMOKE MODE (reduced ladder, NOT a frozen run) ***")
    print("    AMENDMENTS (construction-side, disclosed pre-freeze): "
          "A1 the lead's eq. 4 DOUBLE-SUM form does not exist for the "
          "alignment object -- X is LINEAR in the comb, so "
          "v_-^T X v_- is a SINGLE sum; the exact linear form (eq. 4a) "
          "is the primary reading and the genuine double sum is "
          "delivered for det X (eq. 4b), where it does exist; A2 the "
          "Selberg-induced double sum (eq. 5) is the SECOND place a "
          "genuine kernel appears, and it is the one the identity "
          "creates; A3 the unconditional constants of the O(x) terms "
          "are MEASURED on the built range (max |remainder|/t), which "
          "is a LOWER bound on any true absolute constant -- the "
          "priced envelope is therefore OPTIMISTIC and only its "
          "FAILURE is conclusive; A4 the low end of every Abel "
          "remainder is anchored at n = 1 so the boundary term "
          "vanishes, which fixes the additive constant inside the O(x) "
          "class; A5 the arm objects of CCCXXV are not rebuilt -- the "
          "CCCXXV reproduction is warded against the IMPORTED module "
          "on SUBSET_KZ and against the PUBLISHED trios on the full "
          "ladder; A6 no Vaughan / large-sieve / Hilbert constant is "
          "quoted as a number: each bounds the SAME residual whose "
          "size is measured here directly.")
    print("    SMOKE REPAIRS (disclosed, all made BEFORE the frozen "
          "run, none in the direction of a nicer result): R1 the "
          "rewrite ward was first written against the geometry-kernel "
          "prime sum, where it is world-blind and no control could "
          "fire; it now wards A - B against THIS world's own prime "
          "sum, and the pure identity ward is printed separately.  "
          "R2 the cancellation-depth comparison needed a float "
          "tolerance: on the shallowest rung A < 0 < B, so "
          "|A| + |B| == |P| exactly and the depth is unchanged there "
          "rather than deeper.  R3 the published-CCCXXV-trio gate "
          "applies to the frozen ladder only -- a truncated smoke "
          "ladder cannot reproduce the trios of the full one.  R4 the "
          "product-direction claim was first asserted by "
          "construction; it is now MEASURED, by evaluating the "
          "induced kernel from the SEPARATE logs log m + log k and "
          "comparing it both to its value at the product and across "
          "all pairs sharing a product.")

    section("S0 -- firewall and anti-circularity")
    bad = ast_scan(BANNED_IDS)
    check("S0.1 AST firewall clean (no prime/zero oracles)", not bad,
          ",".join(sorted(set(bad))) if bad else "", kill="K0")
    kbad = ker_path_scan()
    check("S0.2 KERNEL-path anti-circularity clean (W_v, Phi_v, the "
          "wedge kernel, the geometry seat and v_- see no prime-side "
          "and no observed-spectral name)", not kbad,
          ",".join(sorted(set(kbad))) if kbad else "", kill="K0")
    check("S0.3 IMPOSTOR N/A DECLARED: zero zero-reads consumed; the "
          "probe never touches an off-line-zero seat", True)
    print("    TAU_REP INHERITED from CCCXXV: tau_rep := shat - 1/2 = "
          "(m_h - mu1/2)/mu1.  Every new margin is screened against it "
          "and against c_h.")
    print("    EXTERNAL-CITED, source-only, never recomputed as a "
          "gate: Selberg 1949 symmetry formula (the identity AND the "
          "asymptotic sum_{n<=x} L(n) = 2 x log x + O(x)); Chebyshev / "
          "Mertens for sum_{n<=x} Lambda(n) log n = x log x + O(x); "
          "Vaughan identity, Hilbert inequality, large sieve are named "
          "as the absolute-estimate toolkit of TEST C and are NOT "
          "consumed as numbers.")

    section("S1 -- the ladder (CCXI level rungs, CCCXXV objects "
            "re-derived)")
    kzs = range(2, (30 if SMOKE else KZMAX) + 1)
    pre = []
    for kz in kzs:
        rg = esq.level_rung(kz, want_split=False)
        if rg is not None:
            pre.append((kz, rg["alpha"]))
    nmax = min(core.ATOM_MAX,
               int(math.floor(math.exp(2.0 * max(a for _k, a in pre))))
               + 8)
    print("    admissible rungs %d, alpha %.4f..%.4f, "
          "N_max = e^{2 alpha} = %d  [%.1f s]"
          % (len(pre), pre[0][1], pre[-1][1], nmax, time.time() - T0))
    ar = Arith(nmax)
    print("    arithmetic tables built: mu * log^2 to %d, prime-power "
          "pairs %d, C_A(L) %.4f  C_B(pair) %.4f  C_P(linear) %.4f  "
          "[%.1f s]" % (nmax, len(ar.prod), ar.CA, ar.CB, ar.CP,
                        time.time() - T0))
    lad = []
    for kz, _a in pre:
        rg = sel_rung(ar, kz)
        if rg is not None:
            lad.append(rg)
    print("    rungs %d, h %d..%d  [%.1f s]"
          % (len(lad), lad[0]["h"], lad[-1]["h"], time.time() - T0))
    check("S1.1 ladder depth >= %d rungs" % (3 if SMOKE else MIN_RUNGS),
          len(lad) >= (3 if SMOKE else MIN_RUNGS),
          "%d rungs" % len(lad), kill="K1")
    shat = np.array([r["shat"] for r in lad])
    n_reg = int(np.sum(shat >= REG_C))
    check("S1.2 registered half-gap reproduced (shat >= 1/2 on the "
          "ladder)", n_reg == len(lad),
          "shat %s, %d/%d" % (f3(shat), n_reg, len(lad)))
    need = np.array([r["need"] for r in lad])
    qneg = np.array([r["q_neg"] for r in lad])
    algn = np.array([r["align"] for r in lad])
    print("    S1-CCCXXV  the inherited object, reproduced")
    print("      need = -lam_min(G0)   %s   (published %.4f/%.4f/%.4f)"
          % (f3(need), PUB_NEED[0], PUB_NEED[1], PUB_NEED[2]))
    print("      v_-^T X v_-           %s   (published %.4f/%.4f/%.4f)"
          % (f3(qneg), PUB_QNEG[0], PUB_QNEG[1], PUB_QNEG[2]))
    print("      alignment margin      %s   (published %.3e/%.3e/%.3e)"
          % (e3(algn), PUB_ALIGN[0], PUB_ALIGN[1], PUB_ALIGN[2]))
    pub_ok = (max(abs(trio(need)[i] - PUB_NEED[i]) for i in range(3))
              <= 1e-3
              and max(abs(trio(algn)[i] - PUB_ALIGN[i])
                      / PUB_ALIGN[i] for i in range(3)) <= 2e-3)
    check("S1.3 the CCCXXV trios are reproduced against the PUBLISHED "
          "numbers (cited, not recomputed as a gate substitute)",
          (SMOKE or pub_ok) and bool(np.all(algn > 0)),
          "align > 0 on %d/%d%s"
          % (int(np.sum(algn > 0)), len(lad),
             "; SMOKE ladder is truncated, the trio gate applies to "
             "the frozen run only" if SMOKE else ""))
    sub = [kz for kz in (SUBSET_KZ[:2] if SMOKE else SUBSET_KZ)
           if kz in [r["kz"] for r in lad]]
    devs = []
    for kz in sub:
        rr = nf.rung_pack(kz)
        mine = [r for r in lad if r["kz"] == kz][0]
        devs.append(max(rel(rr["need"], mine["need"]),
                        rel(rr["q_neg"], mine["q_neg"]),
                        rel(rr["align"], mine["align"])))
        del rr
    check("S1.4 CCCXXV module cross-check on %d subset rungs: need, "
          "v_-^T X v_- and the margin agree with the IMPORTED "
          "core_fluctuation_normalform_probe" % len(sub),
          bool(devs) and max(devs) <= 1e-10,
          "max rel %.2e on kz %s" % (max(devs) if devs else 1.0, sub))

    # ------------------------------------------------------------ TEST B1
    section("S2 -- TEST B.1: the eq.-4 representation, derived and "
            "warded")
    print("    (eq. 4a)  v_-^T X_h v_- = sum_g w^sm_g Phi_v(u_g) "
          "- sum_n (Lambda(n)/sqrt n) Phi_v(log n),  Phi_v the "
          "GEOMETRY-ONLY window read of W_v = v1^2 W11 + 2 v1 v2 W12 "
          "+ v2^2 W22")
    print("      T163 ward   c_osc . W_v == v_-^T X v_-      : %s"
          % e3([r["dev_t163"] for r in lad]))
    print("      eq. 4a ward (Q - P) == v_-^T X v_-          : %s"
          % e3([r["dev_eq4"] for r in lad]))
    print("      kernel-form ward  P == sum_n Lambda(n) log n G_h(n)  "
          ": %s" % e3([r["dev_plin"] for r in lad]))
    print("      prime sum P %s | smooth sum Q %s"
          % (d3([r["P"] for r in lad]), d3([r["Q"] for r in lad])))
    check("S2.1 THE eq.-4 REPRESENTATION IS EXACT: the T163 "
          "correlation theorem and the T115/T170 tent-spline duality "
          "chain to a closed single sum over prime powers, warded "
          "<= %.0e on every rung" % REP_WARD,
          max(r["dev_eq4"] for r in lad) <= REP_WARD,
          "max %.2e" % max(r["dev_eq4"] for r in lad), kill="K3")
    check("S2.2 the geometry-only kernel G_h(n) = Phi_v(log n) / "
          "(sqrt n log n) reproduces the prime sum exactly (the form "
          "the identity acts on)",
          max(r["dev_plin"] for r in lad) <= ID_WARD,
          "max %.2e" % max(r["dev_plin"] for r in lad))
    check("S2.3 AMENDMENT A1 TYPED, NOT HIDDEN: the object is LINEAR "
          "in Lambda, so NO quadratic-in-Lambda kernel W_h(log m, "
          "log n) represents it; the specified double-sum form of "
          "eq. 4 does not exist here", True,
          "single-sum representation exact to %.2e"
          % max(r["dev_eq4"] for r in lad))

    # ------------------------------------------------------------ TEST B2
    section("S3 -- TEST B.2: where a genuine double sum DOES live, and "
            "its exact structural decomposition")
    r0 = lad[len(lad) // 2]
    mm0, al0, dd0 = r0["M"], r0["alpha"], r0["D_lag"]
    w11, w12, w22 = r0["W3"]
    ug0 = np.linspace(0.0, 2.0 * al0, GRID_DIR)
    p11 = phi_read(w11, ug0, dd0, mm0)
    p22 = phi_read(w22, ug0, dd0, mm0)
    p12 = phi_read(w12, ug0, dd0, mm0)
    wk = wedge_kernel_atom(p11, p22, p12)
    ssum = np.add.outer(np.arange(GRID_DIR), np.arange(GRID_DIR))
    sdif = np.subtract.outer(np.arange(GRID_DIR), np.arange(GRID_DIR))
    tot = float(np.sum((wk - wk.mean()) ** 2))

    def explained(lab):
        key = lab.ravel()
        key = key - key.min()
        sm = np.bincount(key, weights=wk.ravel())
        ct = np.bincount(key)
        pred = (sm / np.maximum(ct, 1))[key].reshape(wk.shape)
        return 1.0 - float(np.sum((wk - pred) ** 2)) / max(tot, 1e-300)

    r_sum, r_dif = explained(ssum), explained(sdif)
    print("    (eq. 4b)  det X_h = (1/2) sum_{i,j} w_i w_j W_h(u_i, "
          "u_j),  W_h(u, u') = phi(u)^T A phi(u'),  phi = (Phi_11, "
          "Phi_22, Phi_12),  A = [[0,1,0],[1,0,0],[0,0,-2]]")
    print("      the prime-prime block is literally sum_{m,n} "
          "Lambda(m)Lambda(n)/sqrt(mn) W_h(log m, log n) -- the lead's "
          "eq. 4, for the QUADRATIC supply")
    ok_c, inert = congruence_rank3()
    check("S3.1 W_h is EXACTLY RANK 3 and LORENTZIAN: the rational "
          "congruence T^T A T = diag(2, -2, -2) over Q gives inertia "
          "(1, 2, 0) -- the atom-coordinate transport of the CCCXXV "
          "wedge kernel", ok_c and inert == (1, 2, 0),
          "congruence %s, LDL inertia %s"
          % ("exact" if ok_c else "MISMATCH", inert))
    devq = []
    for r in lad:
        ka = core.atoms_in(r["alpha"])
        uu = np.asarray(core.U_ALL[:ka], float)
        rho = 0.5 * np.asarray(core.MU_ALL[:ka], float)
        ug, mg = esq.smooth_comb(r["alpha"])
        pos = np.concatenate([uu, ug])
        wgt = np.concatenate([-rho, 0.5 * mg])
        a11 = float(wgt @ phi_read(r["W3"][0], pos, r["D_lag"],
                                   r["M"]))
        a12 = float(wgt @ phi_read(r["W3"][1], pos, r["D_lag"],
                                   r["M"]))
        a22 = float(wgt @ phi_read(r["W3"][2], pos, r["D_lag"],
                                   r["M"]))
        dq = a11 * a22 - a12 * a12
        devq.append(rel(dq, r["detX"]))
        r["detX_atom"] = dq
    print("      det X in the ATOM coordinates (eq. 4b assembled from "
          "the three window reads) vs the frequency route: ward %s, "
          "det X %s" % (e3(devq), d3([r["detX"] for r in lad])))
    check("S3.2 eq. 4b IS EXACT: det X_h assembled as the double sum "
          "(1/2) sum_{i,j} w_i w_j W_h(u_i, u_j) over prime atoms AND "
          "smooth grid reproduces the frequency-route determinant on "
          "every rung", max(devq) <= 1e-8, "max rel %.2e" % max(devq))
    print("    S3-DIR    THE DIRECTION DECOMPOSITION of W_h on a "
          "uniform u-grid (%d x %d), exact variance fractions"
          % (GRID_DIR, GRID_DIR))
    print("      explained by an anti-diagonal function g(u + u') "
          "[the SELBERG direction log(mn)]     : %.6f" % r_sum)
    print("      explained by a  diagonal      function g(u - u') "
          "[the DIFFERENCE direction log(m/n)] : %.6f" % r_dif)
    check("S3.3 W_h is a FINITE MIXTURE, not a pure Selberg kernel: "
          "the anti-diagonal (log mn) direction explains %.1f%% and "
          "the diagonal (log m/n) direction %.1f%% of its variance, "
          "and neither is 1 -- the genuine prime-PAIR kernel is NOT a "
          "function of the product alone"
          % (100.0 * r_sum, 100.0 * r_dif),
          r_sum < 1.0 - 1e-6 and r_dif < 1.0 - 1e-6,
          "rank 3, signature (1, 2)")

    # ------------------------------------------------------------ TEST B3
    section("S4 -- TEST B.3a: the Selberg symmetry identity, warded "
            "exactly")
    spf = spf_table(N_EXACT)
    nchk, nbad, first = selberg_exact_ward(N_EXACT, spf)
    check("S4.1 EXACT INTEGER WARD of Lambda(n) log n + "
          "(Lambda*Lambda)(n) == sum_{d|n} mu(d) log^2(n/d): all three "
          "terms are integer-coefficient quadratic forms in the "
          "log-primes and the coefficient tables agree for every "
          "n <= %d" % N_EXACT, nbad == 0,
          "%d checked, %d mismatches%s"
          % (nchk, nbad, "" if first is None else " first %d" % first[0]),
          kill="K5")
    check("S4.2 NUMERIC WARD of the same identity for every n <= %d "
          "(the full ladder range)" % ar.N,
          ar.dev_id <= 1e-11 * max(float(np.max(np.abs(ar.L))), 1.0),
          "max abs dev %.3e vs max |L| %.3e"
          % (ar.dev_id, float(np.max(np.abs(ar.L)))))
    print("    S4-CUM    the CITED unconditional asymptotics and their "
          "MEASURED remainders on the built range (A3)")
    print("      sum_{n<=x} L(n)              = 2 x log x + R_A,  "
          "max |R_A|/x = %.4f" % ar.CA)
    print("      sum_{mk<=x} Lam(m)Lam(k)     =   x log x + R_B,  "
          "max |R_B|/x = %.4f" % ar.CB)
    print("      sum_{n<=x} Lam(n) log n      =   x log x + R_P,  "
          "max |R_P|/x = %.4f" % ar.CP)

    section("S5 -- TEST B.3b: THE DECISIVE CENSUS -- demand vs "
            "Selberg-supplied vs residual, per rung")
    aa = np.array([r["A"] for r in lad])
    bb = np.array([r["B"] for r in lad])
    qq = np.array([r["Q"] for r in lad])
    pp = np.array([r["P"] for r in lad])
    msel = np.array([r["mar_sel"] for r in lad])
    print("    (eq. 5)  P_h = A_h - B_h,  A_h = sum_n L(n) G_h(n),  "
          "B_h = sum_{mk<=N} Lambda(m)Lambda(k) G_h(mk)")
    print("      identity ward |A - B - P_lin|/|P_lin|      : %s"
          % e3([r["dev_ident"] for r in lad]))
    print("      rewrite ward  |A - B - P|/|P|  (this world) : %s"
          % e3([r["dev_rewrite"] for r in lad]))
    print("      Selberg range N = e^{2 alpha}              : %d..%d"
          % (min(r["Nsel"] for r in lad), max(r["Nsel"] for r in lad)))
    check("S5.1 THE REWRITE IS EXACT ON THE LADDER: P_h = A_h - B_h "
          "wards <= %.0e on every rung" % ID_WARD,
          max(r["dev_rewrite"] for r in lad) <= ID_WARD,
          "max %.2e (pure identity ward %.2e)"
          % (max(r["dev_rewrite"] for r in lad),
             max(r["dev_ident"] for r in lad)), kill="K6")
    # the collision ward, MEASURED (not asserted): the induced kernel
    # evaluated from the SEPARATE logs log m + log k must agree with
    # its value at the product, and pairs sharing a product must carry
    # the same value -- i.e. no log(m/n) dependence at all
    rc = lad[len(lad) // 2]
    nn0 = rc["Nsel"]
    sel = ar.prod <= nn0
    pd_ = ar.prod[sel]
    pf_ = ar.pfac[sel]
    ssep = ar.lg[pf_] + ar.lg[pd_ // pf_]
    w_vc = w_lag_dir(rc["W3"], geo_negdir(
        geo_seat(esq.sine_reads(core.parity_basis(rc["h"], 2).T,
                                rc["M"]),
                 esq.grid_density(rc["c_ar"] + rc["c_sm"]),
                 rc["L"], rc["mu1"]))[0])
    gsep = (phi_read(w_vc, ssep, rc["D_lag"], rc["M"])
            / (np.sqrt(pd_.astype(float)) * ssep))
    gprod = np.zeros(ar.N + 1)
    gprod[2:] = (phi_read(w_vc, ar.lg[2:], rc["D_lag"], rc["M"])
                 * ar.inv[2:])
    sc_g = max(float(np.max(np.abs(gsep))), 1e-300)
    dev_sep = float(np.max(np.abs(gsep - gprod[pd_]))) / sc_g
    gmx = np.full(nn0 + 1, -np.inf)
    gmn = np.full(nn0 + 1, np.inf)
    np.maximum.at(gmx, pd_, gsep)
    np.minimum.at(gmn, pd_, gsep)
    cnts = np.bincount(pd_, minlength=nn0 + 1)
    coll = cnts > 1
    ncoll = int(np.sum(coll))
    spread = float(np.max(gmx[coll] - gmn[coll])) / sc_g
    print("      kernel-of-the-product ward at kz %d: G_h evaluated "
          "from the SEPARATE logs log m + log k vs at the product mk "
          "-- rel dev %.3e; over %d products carrying more than one "
          "prime-power pair the value spread is %.3e"
          % (rc["kz"], dev_sep, ncoll, spread))
    check("S5.2 THE SELBERG-INDUCED DOUBLE SUM IS 100%% SELBERG "
          "DIRECTION, MEASURED: its kernel is G_h(mk), a function of "
          "log m + log n ALONE -- the log(m/n) dependence is not "
          "small, it is absent (spread %.1e over %d colliding "
          "products)" % (spread, ncoll),
          ncoll > 0 and spread <= 1e-12 and dev_sep <= 1e-12,
          "rel dev %.2e, spread %.2e" % (dev_sep, spread))
    del gprod, gsep
    print("    S5-CENSUS  the anti-cancellation inequality after the "
          "exact rewrite:  v_-^T X v_- = Q_h - A_h + B_h  >=  need")
    print("      %5s %6s %10s %11s %11s %11s %12s %12s"
          % ("kz", "h", "need", "Q", "A(mu log^2)", "B(pair)",
             "supplied Q-A", "margin"))
    for r in (lad[::max(1, len(lad) // 10)] + [lad[-1]]):
        print("      %5d %6d %10.6f %11.6f %11.6f %11.6f %12.6f %+12.3e"
              % (r["kz"], r["h"], r["need"], r["Q"], r["A"], r["B"],
                 r["Q"] - r["A"], r["align"]))
    print("      demand need           %s" % f3(need))
    print("      Selberg-supplied Q-A  %s" % f3(qq - aa))
    print("      residual B            %s" % d3(bb))
    print("      supplied margin (Q-A)-need %s   (>= 0 on %d/%d)"
          % (d3(msel), int(np.sum(msel >= 0)), len(lad)))
    print("      |B| / alignment margin     %s"
          % e3(np.abs(bb) / np.maximum(algn, 1e-300)))
    print("      |(Q-A)-need| / |B|         %s   (the supplied part "
          "OVERSHOOTS and the residual takes back exactly the "
          "overshoot)" % f3(np.abs(msel) / np.maximum(np.abs(bb),
                                                      1e-300)))
    check("S5.3 THE RESIDUAL IS NOT SMALL -- IT IS THE WHOLE FIGHT: "
          "the prime-PAIR double sum created by the identity exceeds "
          "the alignment margin by a median factor %.3g, and its sign "
          "is negative on %d/%d rungs, so it can NOT be dropped by a "
          "nonnegativity argument"
          % (float(np.median(np.abs(bb) / np.maximum(algn, 1e-300))),
             int(np.sum(bb < 0)), len(lad)),
          bool(np.all(np.abs(bb) > algn)),
          "min |B|/margin %.3e"
          % float(np.min(np.abs(bb) / np.maximum(algn, 1e-300))))
    dpre = np.array([r["depth_pre"] for r in lad])
    dpost = np.array([r["depth_post"] for r in lad])
    print("    S5-DEPTH  DID THE IDENTITY EXTRACT THE CANCELLATION?  "
          "the cancellation depth = |margin| / (total absolute mass of "
          "the terms)")
    print("      BEFORE  |Q| + |P|            mass %s  depth %s"
          % (f3([r["mass_pre"] for r in lad]), e3(dpre)))
    print("      AFTER   |Q| + |A| + |B|      mass %s  depth %s"
          % (f3([r["mass_post"] for r in lad]), e3(dpost)))
    print("      depth ratio after/before     %s"
          % f3(dpost / np.maximum(dpre, 1e-300)))
    check("S5.4 THE IDENTITY DEEPENS THE CANCELLATION INSTEAD OF "
          "EXTRACTING IT: the required relative cancellation gets "
          "%.2fx SMALLER (median), i.e. the same sign must now be "
          "produced by a deeper cancellation among MORE and LARGER "
          "terms" % float(np.median(dpre / np.maximum(dpost, 1e-300))),
          bool(np.all(dpost <= dpre * (1.0 + 1e-12))),
          "depth before %s -> after %s; ratio after/before %s"
          % (e3(dpre), e3(dpost),
             f3(dpost / np.maximum(dpre, 1e-300))))

    # ------------------------------------------------------------- TEST C
    section("S6 -- TEST C: what the classical toolkit can do with the "
            "residual, priced only AFTER the exact identity")
    c1 = np.array([r["c1_margin"] for r in lad])
    pub = np.array([r["P_ub"] for r in lad])
    print("    C1  POINTWISE NONNEGATIVITY (alignment-free, NO error "
          "term): 0 <= Lambda(n) log n <= L(n) pointwise gives "
          "P <= sum_{G>0} L G")
    print("      P %s  vs  unconditional upper bound P_ub %s"
          % (f3(pp), f3(pub)))
    print("      the inequality needs P <= Q - need = %s"
          % f3(qq - need))
    print("      C1 margin (Q - P_ub) - need %s   (>= 0 on %d/%d)"
          % (d3(c1), int(np.sum(c1 >= 0)), len(lad)))
    print("      G_h sign census: positive on %s of %s support points"
          % (e3([float(r["n_Gpos"]) for r in lad]),
             e3([float(r["n_Gsup"]) for r in lad])))
    check("C1 THE ALIGNMENT-FREE POINTWISE ROUTE FAILS BY O(1), NOT BY "
          "EPSILON: the identity plus nonnegativity of BOTH von "
          "Mangoldt terms bounds P only by %s, while the seat needs "
          "%s -- a gap of %s, so the sign genuinely needs the "
          "CANCELLATION inside sum Lambda(n) log n G(n)"
          % (f3(pub), f3(qq - need), f3(pub - (qq - need))),
          bool(np.all(c1 < 0)),
          "C1 margin < 0 on %d/%d" % (int(np.sum(c1 < 0)), len(lad)))
    amn = np.array([r["A_main"] for r in lad])
    bmn = np.array([r["B_main"] for r in lad])
    aer = np.array([r["A_err"] for r in lad])
    ber = np.array([r["B_err"] for r in lad])
    env = np.array([r["ENV"] for r in lad])
    mmn = np.array([r["mar_main"] for r in lad])
    print("    C2  THE SELBERG ASYMPTOTIC, priced by exact discrete "
          "Abel summation with the MEASURED constants (A3: optimistic)")
    print("      A = A_main + A_err : A_main %s  A_err %s"
          % (f3(amn), d3(aer)))
    print("      B = B_main + B_err : B_main %s  B_err %s"
          % (f3(bmn), d3(ber)))
    print("      UNCONDITIONAL MAIN margin (Q - A_main + B_main) - "
          "need %s   (>= 0 on %d/%d)"
          % (d3(mmn), int(np.sum(mmn >= 0)), len(lad)))
    print("      the error that must be controlled  B_err - A_err %s"
          % d3(ber - aer))
    print("      weighted total variation V_h %s | envelope "
          "(C_A + C_B) V_h %s" % (e3([r["TV"] for r in lad]), e3(env)))
    print("      envelope / alignment margin  %s"
          % e3(env / np.maximum(algn, 1e-300)))
    print("      ORACLE error |A_err| / alignment margin  %s   (even "
          "EXACT knowledge of the main term leaves this)"
          % e3(np.abs(aer) / np.maximum(algn, 1e-300)))
    check("C2 THE UNCONDITIONAL ENVELOPE MISSES BY 5 TO 7 ORDERS: the "
          "Selberg main term leaves a surplus %s over the demand, but "
          "the unconditional error envelope is %s -- a median %.3g "
          "times the alignment margin, and even the ORACLE error "
          "(exact main term, no constant) is a median %.3g times it"
          % (d3(mmn), e3(env),
             float(np.median(env / np.maximum(algn, 1e-300))),
             float(np.median(np.abs(aer) / np.maximum(algn, 1e-300)))),
          bool(np.all(env > algn)),
          "min envelope/margin %.3e"
          % float(np.min(env / np.maximum(algn, 1e-300))))
    print("    C3  THE NEUTRALITY WARD: A_main - B_main == B_main "
          "identically, hence A_err - B_err == P - P_main EXACTLY -- "
          "the post-Selberg residual IS the pre-Selberg residual")
    print("      ward |(A_err - B_err) - P_err| / |P_err| : %s"
          % e3([r["dev_neutral"] for r in lad]))
    print("      P_err (the pre-Selberg residual) %s | its ratio to "
          "the alignment margin %s"
          % (d3([r["P_err"] for r in lad]),
             e3(np.abs([r["P_err"] for r in lad])
                / np.maximum(algn, 1e-300))))
    check("C3 THE IDENTITY IS EXACTLY NEUTRAL ON THE BURDEN: the "
          "residual after the Selberg rewrite is bit-identical to the "
          "residual before it, so no absolute estimate of the "
          "rewritten pieces can be better than an absolute estimate of "
          "the original one",
          max(r["dev_neutral"] for r in lad) <= 1e-8,
          "max %.2e" % max(r["dev_neutral"] for r in lad))
    print("    C-SEAT   THE MEASURED SEAT: dyadic profile of the "
          "running supply Q - P by block n in (2^r, 2^{r+1}] at the "
          "deepest rung (kz %d, h %d, need %.6f)"
          % (lad[-1]["kz"], lad[-1]["h"], lad[-1]["need"]))
    rl = lad[-1]
    dy = rl["dyad"]
    tots = sum(abs(x[1]) for x in dy)
    tails = []
    for i in range(len(dy)):
        tails.append(sum(v for _r, v in dy[i + 1:]))
    print("      %5s %14s %12s %12s %14s" % ("r", "block supply",
                                             "share", "running",
                                             "|tail| / margin"))
    run = 0.0
    for i, (r_, v_) in enumerate(dy):
        run += v_
        print("      %5d %+14.6f %11.4f%% %12.6f %14.3e"
              % (r_, v_, 100.0 * abs(v_) / max(tots, 1e-300), run,
                 abs(tails[i]) / max(rl["align"], 1e-300)))
    r_star = next((dy[i][0] for i in range(len(dy))
                   if abs(tails[i]) < rl["align"]), None)
    n_big = sum(1 for _r, v in dy if abs(v) > rl["align"])
    rg_star = "> %d (never)" % dy[-1][0] if r_star is None else str(
        r_star)
    print("      SEAT: %d of %d dyadic blocks move the supply by MORE "
          "than the final margin %.3e, and the tail beyond block r "
          "first falls under that margin at r = %s -- the sum must be "
          "resolved to n ~ 2^%s = %s, i.e. essentially the whole "
          "window, before its sign is decided"
          % (n_big, len(dy), rl["align"], rg_star, rg_star,
             "%d" % (2 ** r_star) if r_star is not None else
             "the full range"))

    # ---------------------------------------------------------- controls
    section("S7 -- controls (must fire) and screens")
    ctl = {}
    ctl["smooth"] = [sel_rung(ar, r["kz"], with_ops=False,
                              world="smooth") for r in lad]
    ctl["scramble"] = [sel_rung(ar, r["kz"], with_ops=False,
                                scramble_seed=SCR_SEED)
                       for r in lad[:(2 if SMOKE else SCR_RUNGS)]]
    rr9 = core.build_window(CTRL_KZ)
    n_e = int(math.floor(math.exp(2.0 * rr9["alpha"]))) + 1
    lam_e = esq.lambda_eps(n_e)
    nn_e = np.nonzero(np.abs(lam_e) > 1e-12)[0]
    ctl["epstein"] = [sel_rung(
        ar, CTRL_KZ, with_ops=False,
        comb=(np.log(nn_e.astype(float)),
              2.0 * lam_e[nn_e] / np.sqrt(nn_e.astype(float))))]
    print("    E-TABLE   control census -- each world must BREAK the "
          "alignment inequality or the rewrite")
    print("    %-10s %5s %-21s %-21s %-12s %-12s"
          % ("world", "rungs", "alignment margin", "rewrite ward",
             "align>=0", "rewrite ok"))
    print("    %-10s %5d %-21s %-21s %-12s %-12s"
          % ("TRUE", len(lad), d3(algn),
             e3([r["dev_rewrite"] for r in lad]),
             "%d/%d" % (int(np.sum(algn >= 0)), len(lad)),
             "%d/%d" % (len(lad), len(lad))))
    fired = {}
    for nm in ("smooth", "scramble", "epstein"):
        good = [r for r in ctl[nm] if r is not None]
        if not good:
            fired[nm] = True
            print("    %-10s %5d chain death" % (nm, 0))
            continue
        al_ = np.array([r["align"] for r in good])
        dv_ = np.array([r["dev_rewrite"] for r in good])
        n_a = int(np.sum(al_ >= 0))
        n_r = int(np.sum(dv_ <= ID_WARD))
        fired[nm] = (n_a < len(good)) or (n_r < len(good))
        print("    %-10s %5d %-21s %-21s %-12s %-12s"
              % (nm, len(good), d3(al_), e3(dv_),
                 "%d/%d" % (n_a, len(good)),
                 "%d/%d" % (n_r, len(good))))
    # the arithmetic scramble: the identity itself must break.  The
    # SUPPORT is kept (the same prime powers carry mass) and only the
    # values are permuted, so the break is purely multiplicative.
    rng = np.random.default_rng(SCR_SEED)
    lam_s = np.zeros(ar.N + 1)
    lam_s[ar.pp] = ar.lam[rng.permutation(ar.pp)]
    wt_s = []
    for m in ar.pp:
        if 2 * int(m) > ar.N:
            break
        kk = ar.pp[ar.pp <= ar.N // int(m)]
        wt_s.append(lam_s[m] * lam_s[kk])
    conv_s = np.bincount(ar.prod, weights=np.concatenate(wt_s),
                         minlength=ar.N + 1)
    dev_arith = float(np.max(np.abs(lam_s * ar.lg + conv_s - ar.L))) \
        / max(float(np.max(np.abs(ar.L))), 1e-300)
    check("E-arith-scramble control FIRES: a seeded permutation of "
          "Lambda over the prime powers BREAKS the Selberg identity "
          "structurally (the identity is arithmetic, not analytic)",
          dev_arith > 1e-3,
          "max |Lam' log + Lam'*Lam' - L| / max|L| = %.3e (true world "
          "%.3e)" % (dev_arith, ar.dev_id
                     / max(float(np.max(np.abs(ar.L))), 1e-300)),
          kill="K2")
    for nm in ("smooth", "scramble", "epstein"):
        check("E-%s control FIRES" % nm, fired.get(nm, False), "",
              kill="K2")
    pair_sm = [(t, c) for t, c in zip(lad, ctl["smooth"])
               if c is not None]
    if pair_sm:
        sm_x = np.array([abs(c["q_neg"]) for _t, c in pair_sm])
        sm_d = np.array([abs((c["A"] - c["B"]) - c["P"])
                         for _t, c in pair_sm])
        sm_t = np.array([t["q_neg"] for t, _c in pair_sm])
        check("E-smooth STRUCTURE: WHERE the smooth world loses the "
              "supply, exactly.  X == 0 there, so eq. 4a degenerates "
              "to P == Q; the arithmetic objects A and B are "
              "UNCHANGED (they are geometry x arithmetic tables, not "
              "comb data), and the identity A - B = P then fails by "
              "exactly the true alignment supply v_-^T X v_-",
              bool(np.max(sm_x) <= 1e-10
                   and np.max(np.abs(sm_d - np.abs(sm_t))
                              / np.maximum(np.abs(sm_t), 1e-300))
                   <= 1e-8),
              "max |v_-^T X v_-|_smooth %.2e ; |A - B - P| == "
              "|v_-^T X v_-|_true to %.2e"
              % (float(np.max(sm_x)),
                 float(np.max(np.abs(sm_d - np.abs(sm_t))
                              / np.maximum(np.abs(sm_t), 1e-300)))))
    sc_ok = [r for r in ctl["scramble"] if r is not None]
    if sc_ok:
        sc_a = np.array([r["align"] for r in sc_ok])
        sc_d = np.array([r["dev_rewrite"] for r in sc_ok])
        check("E-scramble STRUCTURE: with scrambled atom POSITIONS the "
              "eq.-4a bookkeeping still holds (it is geometry) but the "
              "Selberg rewrite mismatches, and the alignment "
              "inequality fails",
              bool(np.any(sc_a < 0) and np.max(sc_d) > ID_WARD),
              "alignment %s, rewrite ward %s" % (d3(sc_a), e3(sc_d)))
    ep_ok = [r for r in ctl["epstein"] if r is not None]
    if ep_ok:
        check("E-epstein STRUCTURE: a DIFFERENT arithmetic (the "
              "x^2 + 5y^2 comb) does not satisfy the identity, so the "
              "rewrite breaks",
              bool(max(r["dev_rewrite"] for r in ep_ok) > ID_WARD),
              "rewrite ward %s, alignment %s"
              % (e3([r["dev_rewrite"] for r in ep_ok]),
                 d3([r["align"] for r in ep_ok])))
    taus = np.array([r["tau_rep"] for r in lad])
    chs = np.array([r["c_h"] for r in lad])
    hh = np.array([r["h"] for r in lad], float)
    print("    S-SCREEN  every NEW margin against TAU_REP (shat - 1/2) "
          "and against c_h [|slope| <= %.2f PASS, >= %.2f RELOC]"
          % (SLOPE_PASS, SLOPE_RELOC))
    for nm, vals in (("|A|", np.abs(aa)), ("|B|", np.abs(bb)),
                     ("|Q|", np.abs(qq)), ("Q-A", qq - aa),
                     ("|A_err|", np.abs(aer)),
                     ("envelope", env), ("TV", np.array(
                         [r["TV"] for r in lad])),
                     ("main margin", mmn),
                     ("align margin", algn)):
        print("      %-12s %s" % (nm, esq.screen(vals, taus, "vs tau")))
        print("      %-12s %s" % ("", esq.screen(vals, chs, "vs c_h")))
    print("      h-trend  Spearman(h, .)  |A| %+.3f | |B| %+.3f | "
          "Q-A %+.3f | main margin %+.3f | envelope %+.3f | "
          "align margin %+.3f | depth_post %+.3f"
          % (spearman(hh, np.abs(aa)), spearman(hh, np.abs(bb)),
             spearman(hh, qq - aa), spearman(hh, mmn),
             spearman(hh, env), spearman(hh, algn),
             spearman(hh, dpost)))

    # ----------------------------------------------------------- verdict
    section("VERDICT")
    n_ok = sum(1 for _n, o in CHECKS if o)
    print("    TEST B.1: REPRESENTATION-EXACT.  The final localized "
          "object has a closed arithmetic form, chained from two "
          "registered theorems (T163 correlation, T115/T170 "
          "tent-spline duality) and warded to %.1e on %d/%d rungs: "
          "v_-^T X_h v_- = Q_h - P_h with P_h = sum_n (Lambda(n)/"
          "sqrt n) Phi_v(log n) and Phi_v a GEOMETRY-ONLY window read. "
          " AMENDMENT A1 stands: the object is LINEAR in Lambda, so "
          "the specified double-sum eq. 4 does NOT exist for it."
          % (max(r["dev_eq4"] for r in lad), len(lad), len(lad)))
    print("    TEST B.2: the genuine double sum lives in det X, with "
          "the EXACT rank-3 Lorentzian kernel W_h(u, u') = phi(u)^T A "
          "phi(u'), inertia (1, 2, 0) by rational congruence.  Its "
          "direction census is a FINITE MIXTURE: the Selberg "
          "direction log(mn) explains %.3f and the difference "
          "direction log(m/n) explains %.3f of the kernel variance -- "
          "neither is complete." % (r_sum, r_dif))
    print("    TEST B.3: SELBERG-EXACT.  The identity is warded in "
          "EXACT INTEGER arithmetic for n <= %d and numerically to "
          "%.1e for n <= %d; the rewrite P_h = A_h - B_h holds to "
          "%.1e on the whole ladder, and the induced double sum is "
          "100%% Selberg direction (its kernel is G_h(mk), a function "
          "of log m + log n alone).  So the identity FITS the object "
          "perfectly -- and still does not decide it."
          % (N_EXACT, ar.dev_id, ar.N,
             max(r["dev_rewrite"] for r in lad)))
    print("    THE CENSUS, the number that decides: the "
          "Selberg-supplied part Q - A OVERSHOOTS the demand by %s "
          "while the residual prime-PAIR sum B takes back exactly "
          "that overshoot (|B| is a median %.3g times the alignment "
          "margin).  The cancellation depth gets %.2fx DEEPER after "
          "the rewrite (%s -> %s), i.e. the identity RELOCATES the "
          "cancellation and does not extract it."
          % (d3(msel),
             float(np.median(np.abs(bb) / np.maximum(algn, 1e-300))),
             float(np.median(dpre / np.maximum(dpost, 1e-300))),
             e3(dpre), e3(dpost)))
    print("    TEST C: the classical toolkit cannot reach the margin, "
          "and the reason is measured, not asserted.  C1 (pointwise "
          "0 <= Lambda log <= L, alignment-free, NO error term) misses "
          "by O(1): it bounds P by %s where %s is needed.  C2 (the "
          "unconditional Selberg asymptotic, priced by exact discrete "
          "Abel summation with MEASURED -- hence optimistic -- "
          "constants) leaves a main-term surplus %s against an error "
          "envelope %s, a median %.3g times the margin; even the "
          "ORACLE error with an exact main term is a median %.3g "
          "times it.  C3 is the reason: A_err - B_err == P_err "
          "EXACTLY (warded to %.1e), so the post-identity residual IS "
          "the pre-identity residual and no absolute estimate of the "
          "rewritten pieces can beat one of the original."
          % (f3(pub), f3(qq - need), d3(mmn), e3(env),
             float(np.median(env / np.maximum(algn, 1e-300))),
             float(np.median(np.abs(aer) / np.maximum(algn, 1e-300))),
             max(r["dev_neutral"] for r in lad)))
    print("    THE GATE RULE: SELBERG-INSUFFICIENT.  The Selberg "
          "symmetry formula IS an independent, unconditional, "
          "classical source, and it IS structurally matched to the "
          "object (pure product direction, exact rewrite) -- but the "
          "supply it delivers is 4 to 5 orders of magnitude COARSER "
          "than the burden it has to cover.  The measured seat: the "
          "sign is decided by the top dyadic blocks of the windowed "
          "prime sum, and %d of %d dyadic blocks move the supply by "
          "more than the final margin (the largest by a factor "
          "%.1e), so no coarse unconditional estimate localizes it."
          % (n_big, len(dy),
             float(max(abs(v) for _r, v in dy)
                   / max(rl["align"], 1e-300))))
    print("\n    KILLS: %s" % (", ".join(sorted(set(KILLS)))
                               if KILLS else "none"))
    print("    checks %d/%d passed   [%.1f s]"
          % (n_ok, len(CHECKS), time.time() - T0))
    print("    EXPLORATION ONLY -- no ledger row, no paper edit, no "
          "marker move, NO RH claim.")
    return 0 if n_ok == len(CHECKS) else 1


if __name__ == "__main__":
    sys.exit(main())
