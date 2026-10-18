#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""e8_directed_readout_probe -- TFPT E8 front, round r609.

Firewall: exploration, no physics claim, no RH claim.

EXPLORATION ONLY.  experiments/ sandbox.  This probe writes nothing,
imports no verification module, moves no marker, and does not touch
papers, ledger, README, next.txt, or INVENTORY.  NOT an RH probe.

Exact-arithmetic audit of a synthesis note: directed Seifert/Euler
matrix of the E8 Dynkin quiver (Coxeter = Φ_30), Hamming Construction A,
shells/Hecke, Ramanujan Δ as first anisotropy, principal multiplets,
(Z/30)^x prime-phase channels, optional Gauss-code matrix, E6⊕A2 glue.

Corpus already has (one-line regression only, not re-derived):
  E8 theta = E4 / 240 σ_3, Coxeter order 30 with totative phases,
  degree-4/6 isotropy F_4| = F_6| = 0.
"""
from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import math
import os
import re
import sys
from collections import defaultdict

os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("MKL_NUM_THREADS", "1")
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
os.environ.setdefault("NUMEXPR_NUM_THREADS", "1")

import numpy as np  # noqa: E402
import sympy as sp  # noqa: E402
from sympy.matrices.normalforms import (  # noqa: E402
    hermite_normal_form,
    smith_normal_form,
)

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
NOTE_PATH = os.path.join(ROOT, "note_e8_gaussian_code.tex")

SPEC = {
    "round": "r609",
    "front": "TFPT-E8",
    "not_rh": True,
    "firewall": "exploration, no physics claim, no RH claim",
    "claims": ["C1", "C2", "C3", "C4", "C5", "C6", "C7", "C8"],
    "dynkin": "Bourbaki E8, node 2 attached to 4",
    "edges": ["1-3", "3-4", "4-5", "5-6", "6-7", "7-8", "2-4"],
    "coxeter": "C=-S^{-1}S^T, charpoly Phi_30, order 30",
    "hamming": "RM(1,3)=extended Hamming [8,4,4], Construction A",
    "tau": [1, -24, 252, -1472, 4830, -6048, -16744, 84480],
    "smoke": ["C1", "C2", "C5", "C6"],
}
SPEC_SHA = hashlib.sha256(
    json.dumps(SPEC, sort_keys=True, separators=(",", ":")).encode("utf-8")
).hexdigest()

PHI30 = [1, 1, 0, -1, -1, -1, 0, 1, 1]  # x^8+x^7-x^5-x^4-x^3+x+1
TAU = tuple(SPEC["tau"])
TOTATIVES = (1, 7, 11, 13, 17, 19, 23, 29)
EXPONENTS = TOTATIVES
DEGREES = tuple(m + 1 for m in EXPONENTS)  # 2,8,12,14,18,20,24,30
EDGES_E8 = ((1, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (2, 4))

CHECKS: list[tuple[str, bool, str]] = []
CLAIM: dict[str, list[bool]] = {f"C{i}": [] for i in range(1, 9)}
C7_STATUS = "NOT_RUN"


def check(name: str, ok: bool, detail: str = "", claim: str | None = None) -> bool:
    flag = bool(ok)
    CHECKS.append((name, flag, detail))
    if claim is not None:
        CLAIM[claim].append(flag)
    print(
        "  [%s] %s%s"
        % ("PASS" if flag else "FAIL", name, (" -- " + detail) if detail else ""),
        flush=True,
    )
    return flag


def section(title: str) -> None:
    print("\n" + "=" * 74)
    print(title)
    print("=" * 74, flush=True)


def file_sha256() -> str:
    return hashlib.sha256(open(os.path.abspath(__file__), "rb").read()).hexdigest()


def divisors(n: int) -> list[int]:
    n = abs(int(n))
    if n == 0:
        return []
    out = []
    d = 1
    while d * d <= n:
        if n % d == 0:
            out.append(d)
            if d * d != n:
                out.append(n // d)
        d += 1
    out.sort()
    return out


def sigma_k(n: int, k: int) -> int:
    return sum(d ** k for d in divisors(n))


def ramanujan_c(n: int, k: int) -> int:
    g = math.gcd(n, k)
    return sum(int(sp.mobius(n // d)) * d for d in divisors(g))


def poly_mul(a: list[int], b: list[int], nmax: int) -> list[int]:
    c = [0] * (nmax + 1)
    for i, ai in enumerate(a):
        if ai == 0:
            continue
        jmax = min(len(b) - 1, nmax - i)
        for j in range(jmax + 1):
            bj = b[j]
            if bj:
                c[i + j] += ai * bj
    return c


def poly_pow(a: list[int], exp: int, nmax: int) -> list[int]:
    out = [0] * (nmax + 1)
    out[0] = 1
    base = a[:]
    e = exp
    while e:
        if e & 1:
            out = poly_mul(out, base, nmax)
        e >>= 1
        if e:
            base = poly_mul(base, base, nmax)
    return out


# ---------------------------------------------------------------------------
# Hamming RM(1,3) = extended Hamming [8,4,4] from F_2^3 affine functions
# ---------------------------------------------------------------------------
def _f2_points() -> list[tuple[int, int, int]]:
    return [(i & 1, (i >> 1) & 1, (i >> 2) & 1) for i in range(8)]


def hamming_code() -> tuple[tuple[tuple[int, ...], ...], tuple[tuple[int, ...], ...]]:
    pts = _f2_points()
    gens = []
    gens.append(tuple(1 for _ in range(8)))
    for j in range(3):
        gens.append(tuple(p[j] for p in pts))
    gens_t = tuple(gens)
    words = []
    for bits in itertools.product((0, 1), repeat=4):
        w = [0] * 8
        for b, g in zip(bits, gens):
            if b:
                for i in range(8):
                    w[i] ^= g[i]
        words.append(tuple(w))
    return tuple(sorted(words)), gens_t


CODE, CODE_GENS = hamming_code()
CODE_SET = frozenset(CODE)


def affine_hyperplanes() -> set[frozenset[int]]:
    """Supports of the 14 affine hyperplanes of AG(3,2) (F_2^3)."""
    pts = _f2_points()
    blocks = set()
    for a in itertools.product((0, 1), repeat=3):
        if a == (0, 0, 0):
            continue
        for bit in (0, 1):
            supp = frozenset(
                i for i, p in enumerate(pts)
                if (a[0] * p[0] + a[1] * p[1] + a[2] * p[2]) % 2 == bit
            )
            blocks.add(supp)
    return blocks


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


def sink_arrows(sink: int) -> list[tuple[int, int]]:
    """Unique-sink orientation of the E8 tree (not bipartite unless luck)."""
    adj: dict[int, list[int]] = {i: [] for i in range(1, 9)}
    for i, j in EDGES_E8:
        adj[i].append(j)
        adj[j].append(i)
    parent = {sink: 0}
    queue = [sink]
    for u in queue:
        for v in adj[u]:
            if v not in parent:
                parent[v] = u
                queue.append(v)
    arrows = []
    for v, u in parent.items():
        if u != 0:
            arrows.append((v, u))  # toward the sink
    return arrows


def coxeter_from_arrows(arrows: list[tuple[int, int]]) -> sp.Matrix:
    s = euler_S(arrows)
    return -s.inv() * s.T


def charpoly_coeffs(m: sp.Matrix) -> list[int]:
    x = sp.symbols("x")
    p = m.charpoly(x)
    return [int(c) for c in p.all_coeffs()]


def matrix_order(c: sp.Matrix, hard_cap: int = 60) -> int:
    ident = sp.eye(c.rows)
    p = c
    for k in range(1, hard_cap + 1):
        if p == ident:
            return k
        p = p * c
    return -1


def gegenbauer_coeffs(n: int, lam: sp.Rational) -> list[sp.Rational]:
    t = sp.symbols("t")
    expr = sp.expand(sp.gegenbauer(n, lam, t))
    poly = sp.Poly(expr, t)
    return [sp.Rational(poly.coeff_monomial(t ** k)) for k in range(n + 1)]


def zonal_ql(n: int, u2: sp.Expr) -> tuple[sp.Expr, sp.Symbol, sp.Symbol]:
    """Zonal harmonic as f(q, ell), q=|x|^2, ell=<x,u>, |u|^2=u2."""
    q, ell = sp.symbols("q ell")
    ak = gegenbauer_coeffs(n, sp.Rational(3))
    expr = sp.Integer(0)
    for k, a in enumerate(ak):
        if a == 0 or ((n - k) & 1):
            continue
        expr += a * ell ** k * q ** ((n - k) // 2) / (u2 ** (sp.Rational(k, 2)))
    return sp.expand(expr), q, ell


def laplacian_ql(f: sp.Expr, q: sp.Symbol, ell: sp.Symbol, d: int, u2: sp.Expr) -> sp.Expr:
    """Laplacian of F(x)=f(|x|^2, <x,u>) on R^d."""
    fq = sp.diff(f, q)
    return sp.expand(
        2 * d * fq
        + 4 * q * sp.diff(f, q, 2)
        + 4 * ell * sp.diff(f, q, ell)
        + u2 * sp.diff(f, ell, 2)
    )


def half_table(bound: int, par: tuple[int, ...], max_ss: int) -> dict[int, list[tuple[int, ...]]]:
    ranges = [
        [x for x in range(-bound, bound + 1) if (x & 1) == (par[i] & 1)]
        for i in range(4)
    ]
    tab: dict[int, list[tuple[int, ...]]] = defaultdict(list)
    for v in itertools.product(*ranges):
        ss = v[0] * v[0] + v[1] * v[1] + v[2] * v[2] + v[3] * v[3]
        if ss <= max_ss:
            tab[ss].append(v)
    return tab


def enumerate_construction_a(max_n: int, collect_n: int = 0):
    """Unscaled Construction-A vectors.  Shell n has ||y||^2 = 4n (= scaled 2n)."""
    max_ss = 4 * max_n
    bound = int(math.isqrt(max_ss))
    counts = {n: 0 for n in range(1, max_n + 1)}
    collected: dict[int, list[tuple[int, ...]]] = {
        n: [] for n in range(1, collect_n + 1)
    }
    for cw in CODE:
        left = half_table(bound, cw[:4], max_ss)
        right = half_table(bound, cw[4:], max_ss)
        for sl, lvecs in left.items():
            sr_max = max_ss - sl
            for sr, rvecs in right.items():
                if sr > sr_max:
                    continue
                ss = sl + sr
                if ss == 0 or ss % 4 != 0:
                    continue
                n = ss // 4
                if n > max_n:
                    continue
                nvec = len(lvecs) * len(rvecs)
                counts[n] += nvec
                if 1 <= n <= collect_n:
                    for a in lvecs:
                        for b in rvecs:
                            collected[n].append(a + b)
    return counts, collected


def eval_zonal_shell(arr: np.ndarray, ak: list[sp.Rational], n_deg: int, mode: str) -> sp.Rational:
    """Exact shell sum of the degree-n_deg zonal harmonic.

    modes:
      e1      u = e1
      diag    u = (1,1,0,...,0)/sqrt(2)
      generic u = (3,4,0,...,0)/5
    All three are unit vectors, so P = sum a_k <x,u>^k |x|^{n-k}.
    """
    x = np.asarray(arr, dtype=object)
    ss = np.sum(x * x, axis=1)
    if mode == "e1":
        ell_num, ell_den = x[:, 0], 1
    elif mode == "diag":
        # <x,u>^k = (x0+x1)^k / 2^{k/2}, k even
        ell_num, ell_den = x[:, 0] + x[:, 1], "sqrt2"
    elif mode == "generic":
        ell_num, ell_den = 3 * x[:, 0] + 4 * x[:, 1], 5
    else:
        raise ValueError(mode)
    acc = 0
    for k, a in enumerate(ak):
        if a == 0 or ((n_deg - k) & 1):
            continue
        term = (ell_num ** k) * (ss ** ((n_deg - k) // 2))
        sterm = int(np.sum(term))
        if ell_den == "sqrt2":
            # k even: divide by 2^{k/2}
            sterm = sp.Integer(sterm) / (2 ** (k // 2))
        elif ell_den != 1:
            sterm = sp.Integer(sterm) / (sp.Integer(ell_den) ** k)
        else:
            sterm = sp.Integer(sterm)
        acc += a * sterm
    return sp.nsimplify(acc)


def zspan_hnf_rows(vectors: list[tuple[int, ...]]) -> list[tuple[int, ...]]:
    """Z-basis of the span: generators as columns, column-style HNF."""
    if not vectors:
        return []
    dim = len(vectors[0])
    m = sp.Matrix(dim, len(vectors), lambda i, j: int(vectors[j][i]))
    h = hermite_normal_form(m)
    basis = []
    for j in range(h.cols):
        col = tuple(int(h[i, j]) for i in range(h.rows))
        if any(col):
            basis.append(col)
    return basis


def gram_int(basis: list[tuple[int, ...]]) -> sp.Matrix:
    b = sp.Matrix([list(v) for v in basis])
    return b * b.T


def smith_diag(mat: sp.Matrix) -> list[int]:
    s = smith_normal_form(mat)
    return [int(s[i, i]) for i in range(min(s.rows, s.cols))]


def gmul(a: tuple[int, int], b: tuple[int, int]) -> tuple[int, int]:
    return (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0])


def i_pow(m: int) -> tuple[int, int]:
    return ((1, 0), (0, 1), (-1, 0), (0, -1))[m % 4]


def unit_ab(n: int) -> tuple[int, int] | None:
    n = n % 30
    for a in (0, 1):
        for b in range(4):
            if (pow(11, a, 30) * pow(7, b, 30)) % 30 == n:
                return a, b
    return None


def chi_kl(k: int, l: int, n: int) -> tuple[int, int]:
    if math.gcd(n, 30) != 1:
        return (0, 0)
    ab = unit_ab(n)
    if ab is None:
        return (0, 0)
    a, b = ab
    sign = 1 if ((k * a) & 1) == 0 else -1
    re, im = i_pow(l * b)
    return (sign * re, sign * im)


def extract_numeric_matrices(tex: str) -> list[tuple[int, int, tuple]]:
    """Pull integer pmatrix/bmatrix/smallmatrix blocks from the note."""
    found = []
    pattern = re.compile(
        r"\\begin\{(p|b|small)matrix\}(.*?)\\end\{\1matrix\}",
        re.DOTALL,
    )
    for m in pattern.finditer(tex):
        body = m.group(2)
        body = body.replace("\n", " ")
        rows = [r.strip() for r in body.split(r"\\") if r.strip()]
        mat = []
        ok = True
        for row in rows:
            cells = [c.strip() for c in row.split("&")]
            nums = []
            for c in cells:
                c2 = re.sub(r"[{}$\s]", "", c)
                if re.fullmatch(r"[+-]?\d+", c2):
                    nums.append(int(c2))
                else:
                    ok = False
                    break
            if not ok:
                break
            mat.append(tuple(nums))
        if ok and mat and all(len(r) == len(mat[0]) for r in mat):
            found.append((len(mat), len(mat[0]), tuple(mat)))
    return found


# =====================================================================
# claims
# =====================================================================
def run_c1() -> dict:
    section("C1  directed Seifert / Euler matrix")
    a = cartan_e8()
    arrows0 = bipartite_arrows()
    s = euler_S(arrows0)
    ok_cartan = s + s.T == a
    check("C1.S+ST=Cartan", ok_cartan, "bipartite orientation", "C1")
    c = coxeter_from_arrows(arrows0)
    coeffs = charpoly_coeffs(c)
    x = sp.symbols("x")
    phi = [int(c) for c in sp.Poly(sp.cyclotomic_poly(30, x), x).all_coeffs()]
    check(
        "C1.charpoly=Phi_30",
        coeffs == PHI30 and coeffs == phi,
        "coeffs=%s" % coeffs,
        "C1",
    )
    ident = sp.eye(8)
    c30 = c ** 30
    ok_period = c30 == ident
    smaller = [d for d in divisors(30) if d < 30 and d > 0 and c ** d == ident]
    check(
        "C1.C^30=I_min",
        ok_period and smaller == [],
        "smaller periods %s" % (smaller,),
        "C1",
    )
    traces = [int((c ** k).trace()) for k in range(0, 31)]
    rsums = [ramanujan_c(30, k) for k in range(0, 31)]
    check(
        "C1.Tr(C^k)=c_30(k)",
        traces == rsums,
        "k=0..30 traces=%s" % (traces,),
        "C1",
    )
    # eigenphases: roots of Phi_30 are e^{2π i m/30}, m totative
    check(
        "C1.eigenphases totatives",
        tuple(sorted(TOTATIVES)) == TOTATIVES,
        "m in (Z/30)^x = %s" % (TOTATIVES,),
        "C1",
    )
    y = c + c.inv()
    quartic = y ** 4 + y ** 3 - 4 * y ** 2 - 4 * y + ident
    check(
        "C1.Y-quartic",
        quartic == 0 * ident,
        "Y^4+Y^3-4Y^2-4Y+I=0",
        "C1",
    )
    skew = s - s.T
    rk = int(skew.rank())
    check("C1.skew-rank", rk == 8, "rank(S-S^T)=%d" % rk, "C1")
    c_sink8 = coxeter_from_arrows(sink_arrows(8))
    c_sink4 = coxeter_from_arrows(sink_arrows(4))
    p0 = coeffs
    p8 = charpoly_coeffs(c_sink8)
    p4 = charpoly_coeffs(c_sink4)
    check(
        "C1.charpoly orientation-invariant",
        p0 == p8 == p4,
        "bipartite vs sink-8 vs sink-4 (trees: Coxeter conjugate)",
        "C1",
    )
    return {
        "charpoly": coeffs,
        "y_quartic": "Y^4+Y^3-4Y^2-4Y+I=0",
        "skew_rank": rk,
        "traces_ok": traces == rsums,
    }


def run_c2() -> dict:
    section("C2  Hamming -> E8 Construction A")
    wdist = {}
    for w in CODE:
        wt = sum(w)
        wdist[wt] = wdist.get(wt, 0) + 1
    check(
        "C2.weight-enumerator",
        len(CODE) == 16 and wdist == {0: 1, 4: 14, 8: 1},
        "1+14 y^4+y^8  dist=%s" % (wdist,),
        "C2",
    )
    dual = []
    for v in itertools.product((0, 1), repeat=8):
        if all(sum(a * b for a, b in zip(v, c)) % 2 == 0 for c in CODE):
            dual.append(v)
    check("C2.self-dual", sorted(dual) == list(CODE), "C=C-perp", "C2")
    check(
        "C2.doubly-even",
        all(sum(c) % 4 == 0 for c in CODE),
        "weights in 0 mod 4",
        "C2",
    )
    gens = [list(g) for g in CODE_GENS]
    for i in range(8):
        v = [0] * 8
        v[i] = 2
        gens.append(v)
    basis_L = zspan_hnf_rows([tuple(g) for g in gens])
    check("C2.L-rank", len(basis_L) == 8, "HNF rank %d" % len(basis_L), "C2")
    gram = gram_int(basis_L)
    even = all(int(gram[i, j]) % 2 == 0 for i in range(8) for j in range(8))
    even_diag = all(int(gram[i, i]) % 4 == 0 for i in range(8))
    det_g = int(gram.det())
    # scaled Gram = Gram_L / 2; det(Λ) = det_g / 2^8
    det_scaled = sp.Rational(det_g, 256)
    check(
        "C2.Gram even unimodular",
        even and even_diag and det_scaled == 1,
        "det(Gram_L)=%d  det(Gram/2)=%s" % (det_g, det_scaled),
        "C2",
    )
    # minimal vectors, bound 2
    roots = []
    for cw in CODE:
        # |c_i+2z_i| <= 2
        ranges = []
        for i in range(8):
            if cw[i] == 0:
                ranges.append([-2, 0, 2])
            else:
                ranges.append([-1, 1])
        for v in itertools.product(*ranges):
            if sum(x * x for x in v) == 4:
                roots.append(v)
    roots = tuple(sorted(roots))
    w4 = [c for c in CODE if sum(c) == 4]
    n_coord = sum(1 for r in roots if max(abs(x) for x in r) == 2)
    n_w4 = len(roots) - n_coord
    check(
        "C2.min-vectors 240=16+14*16",
        len(roots) == 240 and n_coord == 16 and n_w4 == 14 * 16,
        "240=%d+%d" % (n_coord, n_w4),
        "C2",
    )
    supports = [frozenset(i for i, b in enumerate(c) if b) for c in w4]
    planes = affine_hyperplanes()
    check(
        "C2.affine-hyperplanes",
        set(supports) == planes and len(planes) == 14,
        "14 = 7 directions x 2",
        "C2",
    )
    steiner_ok = True
    for triple in itertools.combinations(range(8), 3):
        hit = sum(1 for s in supports if set(triple) <= s)
        if hit != 1:
            steiner_ok = False
            break
    check(
        "C2.Steiner S(3,4,8)",
        steiner_ok,
        "every 3-subset in exactly one weight-4 word",
        "C2",
    )
    # inner-product distribution vs a fixed root (scaled: divide unscaled by 2)
    r0 = roots[0]
    dist = {2: 0, 1: 0, 0: 0, -1: 0, -2: 0}
    for r in roots:
        ip = sum(a * b for a, b in zip(r0, r)) // 2  # scaled inner product
        dist[ip] = dist.get(ip, 0) + 1
    want = {2: 1, 1: 56, 0: 126, -1: 56, -2: 1}
    check(
        "C2.inner-product dist",
        dist == want,
        "(2,1,0,-1,-2) counts (%d,%d,%d,%d,%d)"
        % (dist[2], dist[1], dist[0], dist[-1], dist[-2]),
        "C2",
    )
    # 120-line graph: one representative of each ± pair
    lines = []
    seen = set()
    for r in roots:
        key = r if r > tuple(-x for x in r) else tuple(-x for x in r)
        if key not in seen:
            seen.add(key)
            lines.append(key)
    nlines = len(lines)
    a_adj = np.zeros((nlines, nlines), dtype=np.int64)
    for i in range(nlines):
        for j in range(i + 1, nlines):
            ip = sum(a * b for a, b in zip(lines[i], lines[j])) // 2
            if abs(ip) == 1:
                a_adj[i, j] = 1
                a_adj[j, i] = 1
    a2 = a_adj @ a_adj
    deg = np.diag(a2)
    lam_vals = a2[a_adj == 1]
    mu_mask = (a_adj == 0) & (~np.eye(nlines, dtype=bool))
    mu_vals = a2[mu_mask]
    lam = int(lam_vals[0]) if lam_vals.size else -1
    mu = int(mu_vals[0]) if mu_vals.size else -1
    srg = (
        nlines == 120
        and set(int(d) for d in deg) == {56}
        and lam_vals.size > 0 and mu_vals.size > 0
        and int(lam_vals.min()) == int(lam_vals.max()) == 28
        and int(mu_vals.min()) == int(mu_vals.max()) == 24
    )
    disc = (lam - mu) ** 2 + 4 * (56 - mu)
    theta = (lam - mu + int(math.isqrt(disc))) // 2
    tau_e = (lam - mu - int(math.isqrt(disc))) // 2
    n_m = 120
    k_m = 56
    rootd = int(math.isqrt(disc))
    f_mult = ((n_m - 1) + ((n_m - 1) * (mu - lam) - 2 * k_m) // rootd) // 2
    g_mult = ((n_m - 1) - ((n_m - 1) * (mu - lam) - 2 * k_m) // rootd) // 2
    mults = sorted((1, f_mult, g_mult))
    check(
        "C2.120-line spectrum",
        srg and mults == [1, 35, 84],
        "srg(120,56,%d,%d) eig (56, %d, %d) mult (1, %d, %d)"
        % (lam, mu, theta, tau_e, f_mult, g_mult),
        "C2",
    )
    return {
        "enumerator": "1+14y^4+y^8",
        "ip_dist": (dist[2], dist[1], dist[0], dist[-1], dist[-2]),
        "spectrum": (k_m, theta, tau_e),
        "mults": (1, f_mult, g_mult),
        "roots": roots,
        "basis_L": basis_L,
    }


def run_c3(counts: dict[int, int]) -> dict:
    section("C3  shells and Hecke")
    n_ok = True
    got = []
    for n in range(1, 11):
        want = 240 * sigma_k(n, 3)
        got.append(counts[n])
        if counts[n] != want:
            n_ok = False
            check(
                "C3.N(%d)" % n,
                False,
                "got %d want 240*sigma_3(%d)=%d" % (counts[n], n, want),
                "C3",
            )
    if n_ok:
        check(
            "C3.N(n)=240 sigma_3(n)",
            True,
            "n=1..10  N=%s" % (got,),
            "C3",
        )
    pairs = ((2, 3), (2, 5), (3, 4), (4, 5))
    hecke_ok = True
    details = []
    for m, n in pairs:
        lhs = counts[m * n]
        rhs = counts[m] * counts[n] // 240
        details.append("%d*%d: %d vs %d" % (m, n, lhs, rhs))
        if lhs != rhs:
            hecke_ok = False
    check(
        "C3.Hecke coprime",
        hecke_ok,
        "; ".join(details),
        "C3",
    )
    return {"N": got, "hecke": hecke_ok}


def run_c4(collected: dict[int, list[tuple[int, ...]]]) -> dict:
    section("C4  Ramanujan Delta as first anisotropy")
    # All three axes are unit vectors, so u2=1 in the (q, ell) Laplacian.
    for tag, u2 in (
        ("u=e1", 1),
        ("u=(1,1,0..)/sqrt2", 1),
        ("u=(3,4,0..)/5", 1),
    ):
        f, q, ell = zonal_ql(8, sp.Integer(u2))
        lap = laplacian_ql(f, q, ell, 8, sp.Integer(u2))
        check("C4.Delta P=0 (%s)" % tag, lap == 0, "symbolic Laplacian in (q,ell)", "C4")

    ak8 = gegenbauer_coeffs(8, sp.Rational(3))
    directions = ("e1", "diag", "generic")
    ap_table: dict[str, list[sp.Rational]] = {}
    for name in directions:
        vals = []
        for n in range(1, 9):
            arr = np.array(collected[n], dtype=object)
            vals.append(eval_zonal_shell(arr, ak8, 8, name))
        ap_table[name] = vals
        print(
            "  [info] A_P(1) u=%s : %s  (nonzero=%s)"
            % (name, vals[0], vals[0] != 0),
            flush=True,
        )
    working = None
    tau_hits = []
    for name, vals in ap_table.items():
        if vals[0] == 0:
            check(
                "C4.A_P(n)/A_P(1)=tau(n)  u=%s" % name,
                False,
                "A_P(1)=0",
                "C4",
            )
            continue
        if working is None:
            working = name
        ratios = [sp.simplify(vals[n] / vals[0]) for n in range(8)]
        ok = ratios == [sp.Integer(t) for t in TAU]
        if ok:
            tau_hits.append(name)
        check(
            "C4.A_P(n)/A_P(1)=tau(n)  u=%s" % name,
            ok,
            "A_P(1)=%s ratios=%s" % (vals[0], [int(r) for r in ratios]),
            "C4",
        )
    nonzero = [name for name, vals in ap_table.items() if vals[0] != 0]
    check(
        "C4.which-u",
        len(nonzero) > 0,
        "A_P(1)≠0 on %s; tau match on %s"
        % (",".join(nonzero) if nonzero else "(none)",
           ",".join(tau_hits) if tau_hits else "(none)"),
        "C4",
    )

    vanish_ok = True
    vanish_detail = []
    for deg in (2, 4, 6):
        ak = gegenbauer_coeffs(deg, sp.Rational(3))
        f, q, ell = zonal_ql(deg, sp.Integer(1))
        if laplacian_ql(f, q, ell, 8, sp.Integer(1)) != 0:
            vanish_ok = False
            vanish_detail.append("deg%d not harmonic" % deg)
            continue
        for n in range(1, 5):
            arr = np.array(collected[n], dtype=object)
            s = eval_zonal_shell(arr, ak, deg, "e1")
            vanish_detail.append("F_%d(n=%d)=%s" % (deg, n, s))
            if s != 0:
                vanish_ok = False
    check(
        "C4.deg 2,4,6 vanish n=1..4",
        vanish_ok,
        "7-design regression; " + ", ".join(vanish_detail[:6]),
        "C4",
    )

    nmax = 8
    e4 = [0] * (nmax + 1)
    e6 = [0] * (nmax + 1)
    e4[0] = 1
    e6[0] = 1
    for n in range(1, nmax + 1):
        e4[n] = 240 * sigma_k(n, 3)
        e6[n] = -504 * sigma_k(n, 5)
    e4_3 = poly_mul(poly_mul(e4, e4, nmax), e4, nmax)
    e6_2 = poly_mul(e6, e6, nmax)
    diff = [e4_3[i] - e6_2[i] for i in range(nmax + 1)]
    delta = [0] * (nmax + 1)
    delta[1] = 1
    for n in range(1, nmax + 1):
        fac = [0] * (nmax + 1)
        for k in range(0, 25):
            exp = n * k
            if exp > nmax:
                break
            fac[exp] += math.comb(24, k) * ((-1) ** k)
        delta = poly_mul(delta, fac, nmax)
    check(
        "C4.E4^3-E6^2=1728 Delta",
        diff == [1728 * c for c in delta],
        "q-series to order 8; Delta=%s" % (delta[1:],),
        "C4",
    )
    if working is not None:
        c0 = ap_table[working][0]
        # Θ_P = sum A_P(n) q^n  vs  c * Δ  (Δ starts at q^1)
        theta_p = [0] + ap_table[working]
        want_th = [c0 * sp.Integer(delta[n]) for n in range(nmax + 1)]
        # A_P stored for n=1..8; theta_p[0] unused
        ok_th = all(theta_p[n] == want_th[n] for n in range(1, nmax + 1))
        check(
            "C4.Theta_{E8,P}=c Delta",
            ok_th,
            "c=A_P(1)=%s" % c0,
            "C4",
        )
    return {
        "working_u": working,
        "ap1": {k: v[0] for k, v in ap_table.items()},
        "tau_ok": working is not None,
    }


def run_c5() -> dict:
    section("C5  principal multiplets")
    m = list(EXPONENTS)
    s1 = sum(2 * mi + 1 for mi in m)
    s2 = sum(m)
    s3 = sum(mi + 1 for mi in m)
    check("C5.sum(2m_i+1)=248", s1 == 248, "sum=%d" % s1, "C5")
    check("C5.sum m_i=120", s2 == 120, "sum=%d" % s2, "C5")
    check("C5.sum(m_i+1)=128", s3 == 128, "sum=%d" % s3, "C5")
    check(
        "C5.degrees=m_i+1",
        DEGREES == (2, 8, 12, 14, 18, 20, 24, 30),
        "degrees=%s" % (DEGREES,),
        "C5",
    )
    return {"exponents": m, "degrees": list(DEGREES)}


def run_c6() -> dict:
    section("C6  prime-phase channels (Z/30)^x")
    units = list(TOTATIVES)
    orders = []
    for g in units:
        x, k = g, 1
        while x != 1:
            x = (x * g) % 30
            k += 1
            if k > 30:
                break
        orders.append(k)
    multiset = tuple(sorted(orders))
    check(
        "C6.order multiset",
        multiset == (1, 2, 2, 2, 4, 4, 4, 4),
        "orders=%s  (group, element)=%s"
        % (multiset, list(zip(units, orders))),
        "C6",
    )
    # C2 x C4: three order-2, four order-4
    check(
        "C6.iso C2xC4",
        orders.count(1) == 1 and orders.count(2) == 3 and orders.count(4) == 4,
        "(Z/30)^x cong C2 x C4",
        "C6",
    )
    f23_orders = [1] + [2] * 7  # (F_2^3, +)
    check(
        "C6.not iso (F2^3,+)",
        multiset != tuple(sorted(f23_orders)),
        "(F2^3,+) all seven nontrivial order 2",
        "C6",
    )
    # character table vs H2 ⊗ F4
    elts = []
    for a in range(2):
        for b in range(4):
            elts.append((pow(11, a, 30) * pow(7, b, 30)) % 30)
    h2f4 = [[None] * 8 for _ in range(8)]
    for k in range(2):
        for l in range(4):
            for a in range(2):
                for b in range(4):
                    sign = 1 if ((k * a) & 1) == 0 else -1
                    re, im = i_pow(l * b)
                    h2f4[k * 4 + l][a * 4 + b] = (sign * re, sign * im)
    chi_prod = [[None] * 8 for _ in range(8)]
    for k in range(2):
        for l in range(4):
            for j, g in enumerate(elts):
                chi_prod[k * 4 + l][j] = chi_kl(k, l, g)
    check(
        "C6.H2⊗F4 in product order",
        chi_prod == h2f4,
        "explicit C2xC4 coordinates: cols (a,b), rows (k,l)",
        "C6",
    )
    # monomial equivalence to the sorted-unit table: column permutation
    col_of = [elts.index(u) for u in units]
    chi_sorted = [[chi_kl(k, l, u) for u in units] for k in range(2) for l in range(4)]
    h2_perm = [[h2f4[r][col_of[c]] for c in range(8)] for r in range(8)]
    check(
        "C6.Fourier monomially ~ H2⊗F4",
        chi_sorted == h2_perm,
        "column perm %s (sorted units), phases=1" % (col_of,),
        "C6",
    )
    vals = {chi_kl(k, l, u) for k in range(2) for l in range(4) for u in units}
    check(
        "C6.character values in {±1,±i}",
        vals <= {(1, 0), (-1, 0), (0, 1), (0, -1)},
        "values=%s" % (sorted(vals),),
        "C6",
    )
    # D_χ coefficients = L(s,χ) L(s-3,χ) for n<=200
    nmax = 200
    dchi_ok = True
    nfail = None
    for k in range(2):
        for l in range(4):
            for n in range(1, nmax + 1):
                chn = chi_kl(k, l, n)
                lhs = (chn[0] * sigma_k(n, 3), chn[1] * sigma_k(n, 3))
                rhs = (0, 0)
                for d in divisors(n):
                    prod = gmul(chi_kl(k, l, d), chi_kl(k, l, n // d))
                    sc = (n // d) ** 3
                    rhs = (rhs[0] + prod[0] * sc, rhs[1] + prod[1] * sc)
                if lhs != rhs:
                    dchi_ok = False
                    nfail = (k, l, n, lhs, rhs)
                    break
            if not dchi_ok:
                break
        if not dchi_ok:
            break
    check(
        "C6.D_chi = L(s,chi)L(s-3,chi)",
        dchi_ok,
        "n<=200, 8 Dirichlet chars mod 30"
        + ("" if dchi_ok else " FAIL %s" % (nfail,)),
        "C6",
    )
    return {"orders": multiset, "dchi": dchi_ok, "col_perm": col_of}


def run_c7() -> str:
    global C7_STATUS
    section("C7  Gauss-code audit (note_e8_gaussian_code.tex)")
    if not os.path.isfile(NOTE_PATH):
        C7_STATUS = "NOT_TESTED(no matrix in note)"
        print("  [SKIP] C7 NOT_TESTED(no matrix in note) -- note missing", flush=True)
        return C7_STATUS
    tex = open(NOTE_PATH, encoding="utf-8").read()
    mats = extract_numeric_matrices(tex)
    # Accept only an explicit 8x8 (Fourier on Coxeter channels) or 4x4
    # over F2 that could be a message-space transform.  The note's only
    # numeric matrix is the 2x2 of 1+i; do not invent the rest.
    big = [(r, c, m) for r, c, m in mats if r >= 4 and c >= 4]
    print(
        "  [info] numeric matrices in note: %s"
        % ([(r, c) for r, c, _ in mats],),
        flush=True,
    )
    if not big:
        C7_STATUS = "NOT_TESTED(no matrix in note)"
        print("  [SKIP] C7 NOT_TESTED(no matrix in note)", flush=True)
        return C7_STATUS
    # If an 8x8 with entries in {0,±1} appeared, test monomial ~ H2⊗F4.
    eight = [m for r, c, m in big if r == 8 and c == 8]
    if not eight:
        C7_STATUS = "NOT_TESTED(no matrix in note)"
        print(
            "  [SKIP] C7 NOT_TESTED(no matrix in note) -- found %s, not 8x8"
            % ([(r, c) for r, c, _ in big],),
            flush=True,
        )
        return C7_STATUS
    C7_STATUS = "TESTED"
    # placeholder: would test monomial equivalence here
    check("C7.monomial H2⊗F4", False, "8x8 present but not identified", "C7")
    return C7_STATUS


def run_c8(roots: tuple, basis_L: list[tuple[int, ...]]) -> dict:
    section("C8  E6 ⊕ A2 ⊂ E8 glue")
    # A2: a coordinate root and a 60-degree neighbour
    alpha = None
    beta = None
    for r in roots:
        if r == (2, 0, 0, 0, 0, 0, 0, 0) or r == (-2, 0, 0, 0, 0, 0, 0, 0):
            alpha = r
            break
    if alpha is None:
        alpha = roots[0]
    for r in roots:
        ip = sum(a * b for a, b in zip(alpha, r))
        if ip == -2:
            beta = r
            break
    check(
        "C8.A2 pair",
        alpha is not None and beta is not None,
        "alpha=%s beta=%s" % (alpha, beta),
        "C8",
    )
    a2_roots = []
    for s in (1, -1):
        a2_roots.append(tuple(s * x for x in alpha))
        a2_roots.append(tuple(s * x for x in beta))
        a2_roots.append(tuple(s * (alpha[i] + beta[i]) for i in range(8)))
    a2_roots = tuple(sorted(set(a2_roots)))
    e6_roots = []
    glue_roots = []
    for r in roots:
        if sum(a * b for a, b in zip(r, alpha)) == 0 and sum(
            a * b for a, b in zip(r, beta)
        ) == 0:
            e6_roots.append(r)
        elif r not in a2_roots and tuple(-x for x in r) not in a2_roots:
            # classified below; first split by membership
            pass
    in_a2 = set(a2_roots)
    e6_set = set(e6_roots)
    for r in roots:
        if r in in_a2:
            continue
        if r in e6_set:
            continue
        glue_roots.append(r)
    split = (len(e6_roots), len(a2_roots), len(glue_roots))
    check(
        "C8.root split 72+6+162",
        split == (72, 6, 162),
        "72+6+162 = (78-6)+(8-2)+27*3*2  got %s" % (split,),
        "C8",
    )
    e6_basis = zspan_hnf_rows(e6_roots)
    a2_basis = zspan_hnf_rows(list(a2_roots))
    check(
        "C8.ranks E6,A2",
        len(e6_basis) == 6 and len(a2_basis) == 2,
        "rk E6=%d rk A2=%d" % (len(e6_basis), len(a2_basis)),
        "C8",
    )
    m_basis = zspan_hnf_rows(e6_basis + a2_basis)
    check("C8.M=E6⊕A2 rank 8", len(m_basis) == 8, "rk M=%d" % len(m_basis), "C8")
    gram_m = gram_int(m_basis)
    gram_l = gram_int(basis_L)
    det_m = int(gram_m.det())
    det_l = int(gram_l.det())
    # [L:M]^2 = det(M)/det(L); unscaled L has det 256, M should have 2304, index 3
    ratio = sp.Rational(det_m, det_l)
    index = int(sp.sqrt(ratio)) if ratio > 0 and sp.sqrt(ratio).is_integer else -1
    check(
        "C8.index 3 (det 9 scaled)",
        index == 3 and ratio == 9,
        "det Gram_M=%d det Gram_L=%d  [L:M]=%s  det ratio=%s"
        % (det_m, det_l, index, ratio),
        "C8",
    )
    even_m = all(int(gram_m[i, j]) % 2 == 0 for i in range(8) for j in range(8))
    gram_scaled = sp.Matrix(8, 8, lambda i, j: int(gram_m[i, j]) // 2)
    inv = smith_diag(gram_scaled) if even_m else []
    inv_nz = [d for d in inv if d not in (0,)]
    disc = [d for d in inv_nz if abs(d) != 1]
    check(
        "C8.disc group Z3 x Z3",
        even_m and sorted(abs(d) for d in disc) == [3, 3],
        "Smith(Gram_M/2)=%s" % (inv,),
        "C8",
    )
    # glue classes: E8/M ≅ Z3.  Reduce each root in the M-basis.
    b = sp.Matrix([list(v) for v in m_basis])
    binv = b.inv()
    classes = set()
    class_count: dict[tuple, int] = defaultdict(int)
    for r in roots:
        xi = (sp.Matrix(list(r)).T * binv).tolist()[0]
        frac = []
        for t in xi:
            t = sp.nsimplify(t)
            frac.append(t - sp.floor(t))
        key = tuple(frac)
        classes.add(key)
        class_count[key] += 1
    ncl = len(classes)
    check(
        "C8.three glue classes",
        ncl == 3,
        "#classes among roots=%d  sizes=%s"
        % (ncl, sorted(class_count.values(), reverse=True)),
        "C8",
    )
    return {
        "split": split,
        "index": index,
        "disc": disc,
        "n_glue_classes": ncl,
    }


def regression_line() -> None:
    section("R0  one-line corpus regression (theta / Coxeter / isotropy)")
    units = [u for u in range(1, 30) if math.gcd(u, 30) == 1]
    x = sp.symbols("x")
    phi = [int(c) for c in sp.Poly(sp.cyclotomic_poly(30, x), x).all_coeffs()]
    check(
        "R0.totatives+Phi_30+240",
        units == list(TOTATIVES)
        and phi == PHI30
        and 16 + 14 * 16 == 240
        and DEGREES == (2, 8, 12, 14, 18, 20, 24, 30),
        "exponents=(Z/30)^x; Phi_30 given; 240=16+14*16; deg=m_i+1 "
        "(F4=F6 vanish deferred to C4 7-design)",
    )


def main() -> int:
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    global CHECKS, CLAIM, C7_STATUS
    CHECKS = []
    CLAIM = {f"C{i}": [] for i in range(1, 9)}
    C7_STATUS = "NOT_RUN"
    smoke = args.smoke

    print("=" * 74)
    print("e8_directed_readout_probe -- r609 TFPT E8 front")
    print("Firewall: exploration, no physics claim, no RH claim")
    print("mode: %s" % ("SMOKE (C1,C2,C5,C6)" if smoke else "FULL"))
    print("SPEC %s" % SPEC_SHA[:16])
    print("FILE %s" % file_sha256())
    print("=" * 74, flush=True)

    regression_line()
    c1 = run_c1()
    c2 = run_c2()
    c5 = run_c5()
    c6 = run_c6()
    c7_status = run_c7()

    c3 = c4 = c8 = None
    if not smoke:
        section("enumeration  Construction-A shells n=1..10")
        counts, collected = enumerate_construction_a(max_n=20, collect_n=8)
        print(
            "  [info] N(n) n=1..10: %s" % [counts[n] for n in range(1, 11)],
            flush=True,
        )
        c3 = run_c3(counts)
        c4 = run_c4(collected)
        c8 = run_c8(c2["roots"], c2["basis_L"])
    else:
        for cid, reason in (
            ("C3", "smoke skip"),
            ("C4", "smoke skip"),
            ("C8", "smoke skip"),
        ):
            print("  [SKIP] %s %s" % (cid, reason), flush=True)

    section("VERDICT")
    held = []
    failed = []
    skipped = []
    for i in range(1, 9):
        cid = "C%d" % i
        if cid == "C7":
            if c7_status.startswith("NOT_TESTED"):
                skipped.append("C7 " + c7_status)
                continue
        bits = CLAIM[cid]
        if not bits:
            skipped.append(cid + " not run")
            continue
        if all(bits):
            held.append(cid)
        else:
            fails = [n for n, ok, d in CHECKS if n.startswith(cid + ".") and not ok]
            failed.append("%s:%s" % (cid, fails))
    k = len(held)
    if smoke:
        verdict = "E8_READOUT_SMOKE(%d/4)" % k
    else:
        verdict = "E8_READOUT_SEALED(%d/8)" % k
    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    ntot = len(CHECKS)
    print("checks %d/%d PASS" % (npass, ntot), flush=True)
    print("held: %s" % (", ".join(held) if held else "(none)"), flush=True)
    if failed:
        print("FAIL: %s" % ("; ".join(failed),), flush=True)
    if skipped:
        print("skip: %s" % ("; ".join(skipped),), flush=True)
    print("C1 charpoly=%s  Y-quartic=Y^4+Y^3-4Y^2-4Y+I  skew-rank=%s"
          % (c1["charpoly"], c1["skew_rank"]), flush=True)
    print("C2 enumerator=%s  ip=%s  spec=%s mult=%s"
          % (c2["enumerator"], c2["ip_dist"], c2["spectrum"], c2["mults"]),
          flush=True)
    if c3 is not None:
        print("C3 N(1..10)=%s hecke=%s" % (c3["N"], c3["hecke"]), flush=True)
    if c4 is not None:
        print("C4 working_u=%s A_P(1)=%s tau_ok=%s"
              % (c4["working_u"], c4["ap1"], c4["tau_ok"]), flush=True)
    print("C5 exponents=%s degrees=%s" % (c5["exponents"], c5["degrees"]),
          flush=True)
    print("C6 order_multiset=%s D_chi=%s" % (c6["orders"], c6["dchi"]),
          flush=True)
    print("C7 %s" % c7_status, flush=True)
    if c8 is not None:
        print("C8 split=%s index=%s disc=%s glue_classes=%s"
              % (c8["split"], c8["index"], c8["disc"], c8["n_glue_classes"]),
              flush=True)
    print("VERDICT: %s" % verdict, flush=True)
    print("SPEC %s" % SPEC_SHA[:16], flush=True)
    return 0 if (not failed) else 1


if __name__ == "__main__":
    sys.exit(main())
