#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""jensen_compiler_rigidity_probe -- r618 PRIME.JENSEN.E8COMPILER.RIGIDITY.01

FROZEN SPEC v1 (2026-09-02).  EXPLORATION ONLY, experiments/ only.
Nothing here is load-bearing, nothing is promoted, no marker moves,
no scorecard row is written by this probe.  This probe writes no files.
KILL probe: pre-registered matrix rules, NO fitting of matrices to
Jensen coefficients (that would be circular).  Every matrix rule is
fixed before any Jensen coefficient is read.

Firewall: "Both compilers are generic real-rootedness certificates
(A-unitary monodromy; MSS interlacing); their existence for all (n,d)
is equivalent to RH; the E8 data are RH-neutral. No RH claim."

=======================================================================
MANDATE
=======================================================================
Two proposed "stability compilers" for the Jensen polynomials of the
Riemann Ξ function are tested for STRUCTURAL feasibility.  Both are
rigid/trivial; this probe seals the two lemmas as exact gates and
provides the Jensen data.

DATA.  Titchmarsh Φ(u) = Σ_{n≥1} (2π² n⁴ e^{9u/2} − 3π n² e^{5u/2})
exp(−π n² e^{2u}).  Edwards/Titchmarsh: Ξ(t) = ξ(1/2+it) =
4 ∫_0^∞ Φ(u) cos(tu) du.  (The cosine-even reading "2∫" undercounts
this Φ by exactly 2; the prefactor is locked by a_0 = ξ(1/2) against
the closed form of ξ and against GORZ γ(0).)  Then
Ξ(t) = Σ_n (−1)^n a_n t^{2n} with a_n = 4 ∫_0^∞ Φ(u) u^{2n} du/(2n)! > 0.
G(z) = Σ_n a_n z^n (= Ξ at t² = −z).  c_n = n! a_n, so
G(z) = Σ c_n z^n/n!.  Jensen J_{n,d}(X) = Σ_{k=0}^d C(d,k) c_{n+k} X^k.
mpmath dps ≥ 40; Φ n-sum until terms < 1e-60.  a_n for n ≤ 14 to ≥ 30
significant digits.  GORZ PNAS 116 (2019) 11103: γ(n) = ξ^{(n)}(1/2),
γ(2k) = (2k)! a_k, γ(odd) = 0.  Classical d = 2 Turán
c_n² ≥ c_{n−1} c_{n+1} (Csordas–Norfolk–Varga 1986).

  D1  Turán inequalities for n ≤ 12; a_0 = ξ(1/2).
  D2  J_{n,d} hyperbolic numerically for d ≤ 8, n ≤ 4 (polyroots;
      all imaginary parts < 1e-20 relative).  Report roots of (0,8)
      and (4,8).  Cayley 𝒞_{n,d}(z) = (1−z)^d J_{n,d}(i(1+z)/(1−z));
      roots on |z| = 1 to 1e-20, and their arguments.

LEMMA A (Seifert compiler rigidity), exact.  Euler/Seifert S of the
bipartite E8 quiver (copied from e8_directed_readout_probe:
cartan_e8, euler_S, bipartite_arrows, coxeter_from_arrows; copy, do
not import).  For invertible complex M, S' = M S M* has Hermitian
part M A_{E8} M* ≻ 0 and monodromy U' = −S'^{−*} S' similar to
C = −S^{−1} S^T, hence charpoly Φ_30, independent of M.

  A1  12 random Gaussian-integer M (entries in {−2..2}+i{−2..2},
      det ≠ 0, seed 618): charpoly(U') = Φ_30 exactly (sympy).
  A2  arguments of roots of 𝒞_{n,8}, n = 0..4, are NOT of the form
      2πk/30 (min distance to that set > 1e-3); the 𝒞_{n,8} differ
      from each other (coeff L∞ > 1e-6 after L∞-normalisation).
  A3  leading principal d×d blocks S_d of S (d = 2..7) have monodromy
      charpolys that are products of cyclotomic polynomials (n-
      independent), while 𝒞_{n,d} varies with n.

Print: "the Coxeter monodromy spectrum is a congruence invariant of
the Seifert form; producing (n,d)-dependent 𝒞_{n,d} requires injecting
the a_n into S, at which point the E8 datum is decoration."

LEMMA B (rank-one mixed characteristic polynomials are ordinary
characteristic polynomials), exact.  MSS: μ[A_1..A_m](x) =
Π_e (1−∂_{z_e}) det(xI + Σ_e z_e A_e)|_{z=0}.  For PSD rank-one
A_e = w_e v_e v_e* the random vectors are deterministic up to a
phase, so μ(x) = det(xI − Σ_e A_e).

  B1  exact sympy, differential-operator definition literally, vs
      det(xI − Σ w_e v_e v_e*), for (d,m) = (3,5) and (4,6), two
      instances each, random Gaussian-rational v_e and rational
      w_e > 0, seed 618.
  B2  (data, not a gate) required Tr M_{n,d}/d = c_{n+1}/c_n for
      n = 0..6 and required det M_{n,d} · c_n / c_{n+d}.  These
      ratios are nonlinear functions of the zero power sums
      σ_k = Σ_γ γ^{−2k} (Newton from the Hadamard product) while any
      fixed-test-function prime sum is LINEAR in zero data by the
      explicit formula — so no rule v_e = F(p,k,E8) independent of
      the zeros can produce them for all n.

VERDICT.
  COMPILERS_STRUCTURALLY_RIGID  iff D1, D2, A1, A2, A3, B1 all pass.
  INCONCLUSIVE(<gate>)          otherwise.

--smoke: n ≤ 8 moments, d ≤ 4, A2 on 𝒞_{n,4}; no full verdict.
Deterministic.  No Jensen coefficient is read before A1/A3/B1 matrix
rules are sealed.
"""
from __future__ import annotations

import argparse
import hashlib
import os
import random
import sys
import time

os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("MKL_NUM_THREADS", "1")
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
os.environ.setdefault("NUMEXPR_NUM_THREADS", "1")

import mpmath as mp  # noqa: E402
import sympy as sp  # noqa: E402

FROZEN_SPEC = __doc__
SPEC_SHA = hashlib.sha256(FROZEN_SPEC.encode("utf-8")).hexdigest()

EDGES_E8 = ((1, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (2, 4))
PHI30_COEFFS = (1, 1, 0, -1, -1, -1, 0, 1, 1)  # x^8+x^7-x^5-x^4-x^3+x+1
SEED = 618
N_M = 12
MP_DPS = 50
ROOT_DPS = 80
PHI_TERM_CUT = mp.mpf("1e-60")
UMAX = 4
PREF = 4  # Edwards: Xi(t) = 4 int Phi(u) cos(tu) du
REL_IMAG = mp.mpf("1e-20")
CAYLEY_UNIT = mp.mpf("1e-20")
A2_MIN_DIST = mp.mpf("1e-3")
A2_LINF = mp.mpf("1e-6")
FENCE = (
    "Both compilers are generic real-rootedness certificates "
    "(A-unitary monodromy; MSS interlacing); their existence for all "
    "(n,d) is equivalent to RH; the E8 data are RH-neutral. No RH claim."
)
LEMMA_A = (
    "the Coxeter monodromy spectrum is a congruence invariant of the "
    "Seifert form; producing (n,d)-dependent 𝒞_{n,d} requires injecting "
    "the a_n into S, at which point the E8 datum is decoration."
)

CHECKS: list[tuple[str, bool, str]] = []
PARENT: dict[str, list[bool]] = {k: [] for k in ("D1", "D2", "A1", "A2", "A3", "B1")}


def file_sha256() -> str:
    return hashlib.sha256(open(os.path.abspath(__file__), "rb").read()).hexdigest()


def section(title: str) -> None:
    print("\n" + "=" * 74)
    print(title)
    print("=" * 74, flush=True)


def check(name: str, ok: bool, detail: str = "", parent: str | None = None) -> bool:
    flag = bool(ok)
    CHECKS.append((name, flag, detail))
    if parent is not None:
        PARENT[parent].append(flag)
    print(
        "  [%s] %s%s"
        % ("PASS" if flag else "FAIL", name, ("  " + detail) if detail else ""),
        flush=True,
    )
    return flag


def fmt_mp(x, digits: int = 12) -> str:
    return mp.nstr(x, digits, strip_zeros=False)


# ---------------------------------------------------------------------------
# E8 Seifert construction -- copied from e8_directed_readout_probe.py
# (do not import that module).
# ---------------------------------------------------------------------------
def cartan_e8() -> sp.Matrix:
    a = sp.eye(8) * 2
    for i, j in EDGES_E8:
        a[i - 1, j - 1] = -1
        a[j - 1, i - 1] = -1
    return a


def euler_S(arrows: list[tuple[int, int]]) -> sp.Matrix:
    """Euler matrix: S_ii=1, S_ij=-1 on arrow i->j (1-based).  S+S^T = Cartan."""
    s = sp.eye(8)
    for i, j in arrows:
        s[i - 1, j - 1] = -1
    return s


def bipartite_arrows() -> list[tuple[int, int]]:
    # colour: {1,4,6,8} vs {2,3,5,7}; all arrows colour-A -> colour-B
    a_set = {1, 4, 6, 8}
    arrows = []
    for i, j in EDGES_E8:
        if i in a_set:
            arrows.append((i, j))
        else:
            arrows.append((j, i))
    return arrows


def coxeter_from_arrows(arrows: list[tuple[int, int]]) -> sp.Matrix:
    s = euler_S(arrows)
    return -s.inv() * s.T


def to_zi(mat: sp.Matrix) -> sp.Matrix:
    return mat.applyfunc(lambda e: sp.expand(e))


def charpoly_U_via_det(Sp: sp.Matrix, x: sp.Symbol) -> sp.Expr:
    """charpoly(U') with U' = -S'^{-*} S' equals det(x S'* + S') / det(S'*)."""
    ys = [sp.expand((k * Sp.H + Sp).det()) for k in range(9)]
    return sp.expand(sp.interpolate(list(zip(range(9), ys)), x))


def cyclotomic_parts(poly: sp.Expr, x: sp.Symbol) -> tuple[list[int], sp.Expr]:
    rem = sp.Poly(sp.expand(poly), x, domain=sp.QQ)
    parts: list[int] = []
    for k in range(1, 60):
        ck = sp.Poly(sp.cyclotomic_poly(k, x), x, domain=sp.QQ)
        if ck.degree() <= 0:
            continue
        while rem.degree() >= ck.degree():
            q, r = rem.div(ck)
            if r == 0:
                parts.append(k)
                rem = q
            else:
                break
    return parts, rem.as_expr()


def fmt_phi_product(parts: list[int]) -> str:
    if not parts:
        return "1"
    counts: dict[int, int] = {}
    for k in parts:
        counts[k] = counts.get(k, 0) + 1
    bits = []
    for k in sorted(counts):
        e = counts[k]
        bits.append("Phi_%d%s" % (k, "^%d" % e if e > 1 else ""))
    return " ".join(bits)


def random_gi_matrix(rng: random.Random, n: int = 8) -> sp.Matrix:
    while True:
        entries = [
            rng.randint(-2, 2) + sp.I * rng.randint(-2, 2) for _ in range(n * n)
        ]
        m = sp.Matrix(n, n, entries)
        if m.det() != 0:
            return m


def gq_entry(rng: random.Random) -> sp.Expr:
    den = rng.choice((1, 2, 3))
    return sp.Rational(rng.randint(-3, 3), den) + sp.I * sp.Rational(
        rng.randint(-3, 3), den
    )


def random_gq_vector(rng: random.Random, d: int) -> sp.Matrix:
    while True:
        v = sp.Matrix([gq_entry(rng) for _ in range(d)])
        if v.H * v != 0:
            return v


def mixed_charpoly_literal(As: list[sp.Matrix], x: sp.Symbol) -> sp.Expr:
    """Π_e (1 − ∂_{z_e}) det(xI + Σ z_e A_e) evaluated at z = 0."""
    m = len(As)
    zs = sp.symbols("z0:%d" % m)
    d = As[0].rows
    mtx = x * sp.eye(d)
    for z, a in zip(zs, As):
        mtx = mtx + z * a
    p = mtx.det()
    for z in zs:
        p = p - sp.diff(p, z)
    p = p.subs({z: 0 for z in zs})
    return sp.expand(p)


# ---------------------------------------------------------------------------
# Φ / a_n
# ---------------------------------------------------------------------------
def phi_titchmarsh(u: mp.mpf) -> mp.mpf:
    total = mp.mpf(0)
    pi = mp.pi
    n = 1
    while n <= 120:
        n2 = mp.mpf(n) * n
        e2u = mp.exp(2 * u)
        e5 = mp.exp(mp.mpf("2.5") * u)
        e9 = mp.exp(mp.mpf("4.5") * u)
        term = (2 * pi ** 2 * n2 * n2 * e9 - 3 * pi * n2 * e5) * mp.exp(
            -pi * n2 * e2u
        )
        total += term
        if n >= 2 and abs(term) < PHI_TERM_CUT:
            break
        n += 1
    return total


def moment_I(n: int) -> mp.mpf:
    return mp.quad(lambda u: phi_titchmarsh(u) * u ** (2 * n), [0, UMAX])


def xi_half() -> mp.mpf:
    s = mp.mpf("0.5")
    return (
        mp.mpf("0.5")
        * s
        * (s - 1)
        * mp.power(mp.pi, -s / 2)
        * mp.gamma(s / 2)
        * mp.zeta(s)
    )


def compute_a(nmax: int) -> list[mp.mpf]:
    out = []
    for n in range(nmax + 1):
        i_n = moment_I(n)
        a_n = PREF * i_n / mp.factorial(2 * n)
        out.append(a_n)
        print(
            "  a_%d = %s" % (n, mp.nstr(a_n, 32, strip_zeros=False)),
            flush=True,
        )
    return out


def c_from_a(a: list[mp.mpf]) -> list[mp.mpf]:
    return [mp.factorial(n) * a[n] for n in range(len(a))]


# ---------------------------------------------------------------------------
# Jensen / Cayley
# ---------------------------------------------------------------------------
def polymul(p: list[mp.mpc], q: list[mp.mpc]) -> list[mp.mpc]:
    r = [mp.mpc(0)] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            r[i + j] += a * b
    return r


def jensen_coeffs(c: list[mp.mpf], n: int, d: int) -> list[mp.mpf]:
    return [mp.binomial(d, k) * c[n + k] for k in range(d + 1)]


def jensen_roots(c: list[mp.mpf], n: int, d: int) -> list[mp.mpc]:
    coeff = jensen_coeffs(c, n, d)
    sig = mp.power(abs(coeff[0] / coeff[-1]), mp.mpf(1) / d)
    scaled = [coeff[k] * sig ** k for k in range(d + 1)]
    pc = list(reversed(scaled))
    with mp.workdps(ROOT_DPS):
        rts_y = mp.polyroots(pc, maxsteps=400, extraprec=50)
    return [r * sig for r in rts_y]


def max_rel_imag(roots: list[mp.mpc]) -> mp.mpf:
    worst = mp.mpf(0)
    for r in roots:
        rel = abs(mp.im(r)) / max(mp.mpf(1), abs(r))
        if rel > worst:
            worst = rel
    return worst


def cayley_z_from_t(t: mp.mpc) -> mp.mpc:
    return (t - mp.j) / (t + mp.j)


def cayley_poly_coeffs(c: list[mp.mpf], n: int, d: int) -> list[mp.mpc]:
    acc = [mp.mpc(0)] * (d + 1)
    one_p = [mp.mpc(1), mp.mpc(1)]
    one_m = [mp.mpc(1), mp.mpc(-1)]
    for k in range(d + 1):
        amp = mp.binomial(d, k) * c[n + k] * (mp.j ** k)
        p = [mp.mpc(1)]
        for _ in range(k):
            p = polymul(p, one_p)
        for _ in range(d - k):
            p = polymul(p, one_m)
        for i, a in enumerate(p):
            acc[i] += amp * a
    return acc


def normalize_linf(coeffs: list[mp.mpc]) -> list[mp.mpc]:
    m = max(abs(a) for a in coeffs)
    return [a / m for a in coeffs]


def angdist(a: mp.mpf, b: mp.mpf) -> mp.mpf:
    d = abs(a - b) % (2 * mp.pi)
    return min(d, 2 * mp.pi - d)


def min_dist_thirtieth(args: list[mp.mpf]) -> mp.mpf:
    grid = [2 * mp.pi * k / 30 for k in range(30)]
    best = mp.pi
    for th in args:
        d = min(angdist(th, g) for g in grid)
        if d < best:
            best = d
    return best


# ---------------------------------------------------------------------------
# sections
# ---------------------------------------------------------------------------
def run_a1(S: sp.Matrix, x: sp.Symbol) -> None:
    section("A1  Seifert monodromy is a congruence invariant (exact)")
    phi30 = sp.Poly(sp.cyclotomic_poly(30, x), x)
    C = coxeter_from_arrows(bipartite_arrows())
    c_coeffs = [int(cf) for cf in sp.Poly(C.charpoly(x).as_expr(), x).all_coeffs()]
    check(
        "A1.C_charpoly_Phi30",
        tuple(c_coeffs) == PHI30_COEFFS,
        "C = -S^{-1} S^T  coeffs=%s" % (c_coeffs,),
        "A1",
    )
    U = -S.T.inv() * S
    u_coeffs = [int(cf) for cf in sp.Poly(U.charpoly(x).as_expr(), x).all_coeffs()]
    check(
        "A1.U_charpoly_Phi30",
        tuple(u_coeffs) == PHI30_COEFFS,
        "U = -S^{-*} S  same as C (transpose-similar)",
        "A1",
    )
    rng = random.Random(SEED)
    n_ok = 0
    dets = []
    for i in range(N_M):
        M = random_gi_matrix(rng)
        Sp = to_zi(M * S * M.H)
        p = charpoly_U_via_det(Sp, x)
        dlt = sp.expand(Sp.H.det())
        diff = sp.expand(p - dlt * phi30.as_expr())
        ok = diff == 0
        n_ok += int(ok)
        dets.append(dlt)
        check(
            "A1.M%d_charpoly" % (i + 1),
            ok,
            "det(M)=%s  det(S'*)=%s" % (sp.expand(M.det()), dlt),
            "A1",
        )
    check(
        "A1.all_12",
        n_ok == N_M,
        "%d/%d matrices  seed=%d" % (n_ok, N_M, SEED),
        "A1",
    )


def run_a3_blocks(S: sp.Matrix, x: sp.Symbol) -> dict[int, str]:
    section("A3  leading-principal-block monodromy (exact, n-independent)")
    report: dict[int, str] = {}
    all_ok = True
    for d in range(2, 8):
        sd = S[:d, :d]
        detd = sd.det()
        if detd == 0:
            all_ok = False
            check("A3.d%d_invertible" % d, False, "det=0", "A3")
            report[d] = "SINGULAR"
            continue
        ud = -sd.T.inv() * sd
        cp = sp.expand(ud.charpoly(x).as_expr())
        parts, rem = cyclotomic_parts(cp, x)
        label = fmt_phi_product(parts)
        ok = rem == 1 and parts != []
        all_ok = all_ok and ok
        report[d] = label
        check(
            "A3.d%d_cyclotomic" % d,
            ok,
            "charpoly=%s  = %s" % (cp, label),
            "A3",
        )
    check("A3.blocks_all", all_ok, "d=2..7 n-independent (S fixed)", "A3")
    return report


def run_b1() -> None:
    section("B1  rank-one MSS mixed charpoly = ordinary charpoly (exact)")
    rng = random.Random(SEED)
    x = sp.symbols("x")
    specs = [(3, 5), (3, 5), (4, 6), (4, 6)]
    n_ok = 0
    for idx, (d, m) in enumerate(specs, start=1):
        As = []
        for _ in range(m):
            v = random_gq_vector(rng, d)
            w = sp.Rational(rng.randint(1, 5), rng.randint(1, 3))
            As.append(w * (v * v.H))
        mu = mixed_charpoly_literal(As, x)
        suma = sum(As, sp.zeros(d))
        ordinary = sp.expand((x * sp.eye(d) - suma).det())
        ok = sp.expand(mu - ordinary) == 0
        n_ok += int(ok)
        check(
            "B1.d%dm%d_i%d" % (d, m, idx),
            ok,
            "mu=%s" % mu,
            "B1",
        )
    check("B1.all_four", n_ok == 4, "%d/4 instances" % n_ok, "B1")
    print(
        "  consequence: with rank-one prime-event matrices the target "
        "identity mu_{n,d}(x) = c·J_{n,d}(-x) would say that J_{n,d}(-x) "
        "is the characteristic polynomial of the PSD matrix "
        "M_{n,d} = Σ_e w_e v_e v_e*; coefficient identities "
        "e_k(M_{n,d}) = C(d,k) c_{n+k}/c_n  (normalisation 1), in "
        "particular Tr M_{n,d} = d·c_{n+1}/c_n.",
        flush=True,
    )


def run_d1(a: list[mp.mpf], c: list[mp.mpf], n_turan: int) -> None:
    section("D1  Jensen data / Turán / GORZ γ(n)")
    xih = xi_half()
    rel = abs(a[0] - xih) / abs(xih)
    check(
        "D1.a0_eq_xi_half",
        rel < mp.mpf("1e-25"),
        "a_0=%s  xi(1/2)=%s  rel=%s" % (fmt_mp(a[0], 20), fmt_mp(xih, 20), fmt_mp(rel, 6)),
        "D1",
    )
    h = mp.mpf("1e-8")
    s0 = mp.mpf("0.5")

    def xi_at(s: mp.mpf) -> mp.mpf:
        return (
            mp.mpf("0.5")
            * s
            * (s - 1)
            * mp.power(mp.pi, -s / 2)
            * mp.gamma(s / 2)
            * mp.zeta(s)
        )

    d2 = (xi_at(s0 + h) + xi_at(s0 - h) - 2 * xi_at(s0)) / h ** 2
    # GORZ γ(2) = ξ''(1/2) = 2! a_1
    g2 = 2 * a[1]
    rel2 = abs(g2 - d2) / abs(d2)
    check(
        "D1.GORZ_gamma2",
        rel2 < mp.mpf("1e-8"),
        "gamma(2)=(2)! a_1=%s  xi''(1/2)~%s  rel=%s"
        % (fmt_mp(g2, 16), fmt_mp(d2, 16), fmt_mp(rel2, 6)),
        "D1",
    )
    print("  GORZ dictionary: gamma(n)=xi^{(n)}(1/2); gamma(odd)=0; "
          "gamma(2k)=(2k)! a_k.", flush=True)
    for k in range(min(7, len(a))):
        g = mp.factorial(2 * k) * a[k]
        print("    gamma(%d)=%s" % (2 * k, fmt_mp(g, 16)), flush=True)
    pos = all(an > 0 for an in a)
    check("D1.a_n_positive", pos, "n=0..%d" % (len(a) - 1), "D1")
    turan_ok = True
    ratios = []
    for n in range(1, n_turan + 1):
        lhs = c[n] ** 2
        rhs = c[n - 1] * c[n + 1]
        ok = lhs >= rhs
        turan_ok = turan_ok and ok
        ratios.append(float(lhs / rhs))
        if not ok:
            print("    Turán FAIL n=%d  lhs/rhs=%s" % (n, fmt_mp(lhs / rhs, 8)),
                  flush=True)
    check(
        "D1.Turan_n_le_%d" % n_turan,
        turan_ok,
        "min ratio=%s  max ratio=%s" % (min(ratios), max(ratios)),
        "D1",
    )


def run_d2_a2(
    c: list[mp.mpf], d_max: int, full: bool
) -> tuple[list[mp.mpc], list[mp.mpc], mp.mpf, mp.mpf]:
    section("D2  Jensen hyperbolicity / Cayley unit circle")
    n_max = 4
    worst_im = mp.mpf(0)
    all_hyp = True
    roots_08: list[mp.mpc] = []
    roots_48: list[mp.mpc] = []
    cayley_unit_ok = True
    worst_unit = mp.mpf(0)
    args_by_n: dict[int, list[mp.mpf]] = {}
    cayley_norm: dict[int, list[mp.mpc]] = {}
    d_cayley = 8 if (full and d_max >= 8) else d_max
    for n in range(0, n_max + 1):
        for d in range(1, d_max + 1):
            if n + d >= len(c):
                continue
            rts = jensen_roots(c, n, d)
            rel = max_rel_imag(rts)
            if rel > worst_im:
                worst_im = rel
            hyp = rel < REL_IMAG
            all_hyp = all_hyp and hyp
            if d == 8 and n == 0:
                roots_08 = rts
            if d == 8 and n == 4:
                roots_48 = rts
            if d == d_cayley:
                zs = [cayley_z_from_t(t) for t in rts]
                args_by_n[n] = [mp.arg(z) for z in zs]
                for z in zs:
                    du = abs(abs(z) - 1)
                    if du > worst_unit:
                        worst_unit = du
                    if du >= CAYLEY_UNIT:
                        cayley_unit_ok = False
                cayley_norm[n] = normalize_linf(cayley_poly_coeffs(c, n, d))
    check(
        "D2.hyperbolic_d_le_%d_n_le_4" % d_max,
        all_hyp,
        "max rel Im=%s  thresh=%s" % (fmt_mp(worst_im, 6), REL_IMAG),
        "D2",
    )
    check(
        "D2.cayley_on_circle_d%d" % d_cayley,
        cayley_unit_ok,
        "max ||z|-1|=%s" % fmt_mp(worst_unit, 6),
        "D2",
    )
    if roots_08:
        print("  J_{0,8} roots:", flush=True)
        for r in sorted(roots_08, key=lambda z: float(mp.re(z))):
            print("    %s" % fmt_mp(mp.re(r), 16), flush=True)
    if roots_48:
        print("  J_{4,8} roots:", flush=True)
        for r in sorted(roots_48, key=lambda z: float(mp.re(z))):
            print("    %s" % fmt_mp(mp.re(r), 16), flush=True)
    if 0 in args_by_n:
        print("  𝒞_{0,%d} arguments (rad):" % d_cayley, flush=True)
        for th in sorted(args_by_n[0], key=lambda t: float(t)):
            print("    %s  (= %s * pi)" % (fmt_mp(th, 12), fmt_mp(th / mp.pi, 12)),
                  flush=True)
    if 4 in args_by_n:
        print("  𝒞_{4,%d} arguments (rad):" % d_cayley, flush=True)
        for th in sorted(args_by_n[4], key=lambda t: float(t)):
            print("    %s  (= %s * pi)" % (fmt_mp(th, 12), fmt_mp(th / mp.pi, 12)),
                  flush=True)

    section("A2  Cayley arguments vs 30th roots / n-dependence")
    all_args = []
    for n, ths in args_by_n.items():
        all_args.extend(ths)
    mind = min_dist_thirtieth(all_args) if all_args else mp.mpf(0)
    check(
        "A2.min_dist_30th_d%d" % d_cayley,
        mind > A2_MIN_DIST,
        "min dist=%s  (need > %s)" % (fmt_mp(mind, 10), A2_MIN_DIST),
        "A2",
    )
    ns = sorted(cayley_norm)
    max_linf = mp.mpf(0)
    for i, n1 in enumerate(ns):
        for n2 in ns[i + 1 :]:
            dist = max(abs(u - v) for u, v in zip(cayley_norm[n1], cayley_norm[n2]))
            if dist > max_linf:
                max_linf = dist
    check(
        "A2.cayley_n_distinct_d%d" % d_cayley,
        max_linf > A2_LINF,
        "max Linf after Linf-norm=%s  (need > %s)"
        % (fmt_mp(max_linf, 8), A2_LINF),
        "A2",
    )
    print(
        "  no congruence class of the E8 Seifert form realises these "
        "𝒞_{n,%d}." % d_cayley,
        flush=True,
    )
    return roots_08, roots_48, mind, max_linf


def run_a3_variation(c: list[mp.mpf], d_max: int) -> None:
    section("A3  𝒞_{n,d} varies with n (blocks n-independent, Cayley is not)")
    all_var = True
    details = []
    for d in range(2, min(d_max, 7) + 1):
        if 0 + d >= len(c) or 1 + d >= len(c):
            continue
        p0 = normalize_linf(cayley_poly_coeffs(c, 0, d))
        p1 = normalize_linf(cayley_poly_coeffs(c, 1, d))
        dist = max(abs(u - v) for u, v in zip(p0, p1))
        ok = dist > A2_LINF
        all_var = all_var and ok
        details.append("d=%d Linf=%s" % (d, fmt_mp(dist, 6)))
        check("A3.Cayley_varies_d%d" % d, ok, "n=0 vs n=1  Linf=%s" % fmt_mp(dist, 8), "A3")
    check("A3.Cayley_varies_all", all_var, "; ".join(details), "A3")
    print("  LEMMA A: %s" % LEMMA_A, flush=True)


def run_b2(c: list[mp.mpf], d_list: list[int]) -> None:
    section("B2  required traces / dets (data; not a gate)")
    print(
        "  required Tr M_{n,d}/d = c_{n+1}/c_n  (independent of d); "
        "required det M_{n,d} = c_{n+d}/c_n, hence "
        "det M_{n,d} · c_n / c_{n+d} = 1.",
        flush=True,
    )
    print(
        "  n   c_{n+1}/c_n              "
        + "  ".join("det(d=%d)" % d for d in d_list)
        + "   det*c_n/c_{n+d}",
        flush=True,
    )
    n_top = min(6, len(c) - 2)
    for n in range(0, n_top + 1):
        tr = c[n + 1] / c[n]
        dets = []
        products = []
        for d in d_list:
            if n + d >= len(c):
                dets.append("    n/a    ")
                products.append(" n/a")
                continue
            det_req = c[n + d] / c[n]
            prod = det_req * c[n] / c[n + d]
            dets.append("%s" % fmt_mp(det_req, 10))
            products.append(fmt_mp(prod, 6))
        print(
            "  %d  %s  %s  %s"
            % (n, fmt_mp(tr, 16), "  ".join(dets), " ".join(products)),
            flush=True,
        )
    print(
        "  reasoning note: these ratios are nonlinear functions of the "
        "zero power sums σ_k = Σ_γ γ^{-2k} (Newton identities from the "
        "Hadamard product G(z) = a_0 Π (1 + z/γ²)) while any "
        "fixed-test-function prime sum is LINEAR in zero data by the "
        "explicit formula — so no rule v_e = F(p,k,E8) that is "
        "independent of the zeros can produce them for all n.",
        flush=True,
    )


def parent_pass(name: str) -> bool:
    bits = PARENT[name]
    return bool(bits) and all(bits)


def main() -> int:
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke
    full = not smoke
    t0 = time.time()

    global CHECKS, PARENT
    CHECKS = []
    PARENT = {k: [] for k in ("D1", "D2", "A1", "A2", "A3", "B1")}

    n_a = 8 if smoke else 14
    d_max = 4 if smoke else 8
    n_turan = 6 if smoke else 12
    d_b2 = [2, 4] if smoke else [2, 4, 8]

    mp.mp.dps = MP_DPS

    print("=" * 74)
    print("jensen_compiler_rigidity_probe -- r618 "
          "PRIME.JENSEN.E8COMPILER.RIGIDITY.01")
    print("mode: %s" % ("SMOKE (n_a=%d, d_max=%d)" % (n_a, d_max) if smoke
                        else "FULL"))
    print("SPEC_SHA %s" % SPEC_SHA)
    print("FILE     %s" % file_sha256())
    print("FENCE    %s" % FENCE)
    print("=" * 74, flush=True)

    x = sp.symbols("x")
    arrows = bipartite_arrows()
    S = euler_S(arrows)
    A = cartan_e8()
    section("S0  Seifert / Cartan (matrix rules; no Jensen yet)")
    check(
        "S0.S_plus_ST_Cartan",
        S + S.T == A,
        "bipartite orientation, det(S)=%s" % S.det(),
        "A1",
    )
    print("  S =\n%s" % S, flush=True)

    # Matrix rules BEFORE any Jensen coefficient is read.
    run_a1(S, x)
    block_report = run_a3_blocks(S, x)
    run_b1()

    section("D0  Φ-moments a_n (Jensen data)")
    print(
        "  prefactor %d, dps=%d, Umax=%s, Phi n-sum cut %s"
        % (PREF, MP_DPS, UMAX, PHI_TERM_CUT),
        flush=True,
    )
    a = compute_a(n_a)
    cc = c_from_a(a)
    run_d1(a, cc, n_turan)
    roots_08, roots_48, mind, max_linf = run_d2_a2(cc, d_max, full)
    run_a3_variation(cc, d_max)
    run_b2(cc, d_b2)

    section("VERDICT")
    print("FENCE  %s" % FENCE, flush=True)
    failed_parents = []
    for name in ("D1", "D2", "A1", "A2", "A3", "B1"):
        ok = parent_pass(name)
        print("  parent %s  %s  (%d subchecks)"
              % (name, "PASS" if ok else "FAIL", len(PARENT[name])),
              flush=True)
        if not ok:
            failed_parents.append(name)
    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    ntot = len(CHECKS)
    print("checks %d/%d PASS" % (npass, ntot), flush=True)
    print("A3 block charpolys: %s"
          % ({d: block_report[d] for d in sorted(block_report)},),
          flush=True)
    print("a_0..a_6: %s" % [fmt_mp(a[i], 12) for i in range(min(7, len(a)))],
          flush=True)
    if roots_08:
        print("J(0,8) roots: %s"
              % [fmt_mp(mp.re(r), 12) for r in sorted(roots_08, key=lambda z: float(mp.re(z)))],
              flush=True)
    if roots_48:
        print("J(4,8) roots: %s"
              % [fmt_mp(mp.re(r), 12) for r in sorted(roots_48, key=lambda z: float(mp.re(z)))],
              flush=True)
    print("A2 min dist to 2πk/30: %s" % fmt_mp(mind, 12), flush=True)
    print("A2 max Cayley Linf:    %s" % fmt_mp(max_linf, 8), flush=True)
    if smoke:
        verdict = "SMOKE_PASS" if not failed_parents else (
            "SMOKE_FAIL(%s)" % ",".join(failed_parents)
        )
    else:
        verdict = (
            "COMPILERS_STRUCTURALLY_RIGID"
            if not failed_parents
            else "INCONCLUSIVE(%s)" % ",".join(failed_parents)
        )
    dt = time.time() - t0
    print("VERDICT: %s" % verdict, flush=True)
    print("SPEC_SHA %s" % SPEC_SHA, flush=True)
    print("FILE     %s" % file_sha256(), flush=True)
    print("runtime  %.1f s" % dt, flush=True)
    print("gates    %d/%d" % (npass, ntot), flush=True)
    return 0 if not failed_parents else 1


if __name__ == "__main__":
    sys.exit(main())
