#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""prime_e8_ordered_herglotz_probe -- r613 PRIME.E8.ORDERED.HERGLOTZ.01

Firewall: exploration, no RH claim, no physics claim.

EXPLORATION ONLY.  experiments/ sandbox.  Numeric scout, not an RH
claim, not a physics claim.  This probe writes nothing, imports no
verification module, reads no zeta-zero table, and moves no marker.

IDEA UNDER TEST.  Prime-power events e=(p,k) ordered by u_e = k log p
with weights λ_e = 2 log p / p^{k/2} are labelled by E8 roots and
assembled into a rank-one canonical system in R^{16}.  The matrix
Weyl function of the monodromy is tested as a Herglotz function
against the Euler-side target m(z) = −Φ'(z)/Φ(z), Φ(z)=ξ(1/2+√z),
after the de Branges affine gauge α+βz.

LABEL RULE (frozen).  Construction-A integer roots of E8 (norm^2=4),
Coxeter C_W = s_B s_A of the bipartite orientation of Bourbaki E8
(copied Seifert/Hamming construction of e8_directed_readout_probe
C1/C2; C_W is conjugate to C_Seifert = −S^{-1}S^T).  Eight orbits
of size 30.  Event index t is the 0-based rank in the event set
sorted by n=p^k (true u-order), frozen on the event identity.
  gcd(n,30)=1: residue n mod 30 selects orbit j via
    UNITS30=(1,7,11,13,17,19,23,29); v = C_W^{t mod 30} · rep_j
    with rep_j the lex-smallest vector of orbit j.
  gcd(n,30)>1: the 16 coordinate roots ±2 e_i, ordered
    +2e_1..+2e_8, −2e_1..−2e_8; v = coord[(t + n) mod 16].

EMBEDDING.  w_e = A_E8^{−1/2} v_e in R^8 (Cartan whitening of the
Construction-A vector).  Default q0: ŵ=(w_e, 0) in R^8⊕R^8.
Robustness twirl: ŵ=(w_e, C_W w_e)/√2.  H_e = λ_e ŵ ŵ^T.
J = [[0,I_8],[−I_8,0]].  Jump Y ↦ (I + z J H_e) Y.  Because
ŵ^T J ŵ = 0 one has (J H_e)^2 = 0, hence I+zJH_e = exp(zJH_e).
Free evolution on a gap Δu: H_free=ε I_16, T=exp(z ε Δu J)
= cos(z ε Δu) I + sin(z ε Δu) J.  Start at u=0.  Monodromy
M = T_{e_N} ⋯ T_{e_1} (right-to-left; free-then-jump per event).

WEYL CONVENTION.  M=[[A,B],[C,D]] in 8×8 blocks.
W(z) = (A Z + B)(C Z + D)^{−1} with Z = i I_8 (Möbius image of iI
in the Siegel half-space).  If that convention fails Im W ⪰ 0 at
the calibration point, the frozen fallback is Z = −i I_8.
Scalar m_X(z) = ⟨ξ, W(z) ξ⟩, ξ the normalised whitened highest
root (Bourbaki 2α1+3α2+4α3+6α4+5α5+4α6+3α7+2α8).  Also report
ξ=e_1.  Target uses mpmath on Re s>1 only:
  ξ'/ξ(s) = 1/s + 1/(s−1) − (1/2)log π + (1/2)ψ(s/2) + ζ'/ζ(s),
  m(z) = −(ξ'/ξ)(1/2+√z) / (2 √z),  √z = s−1/2 on the Euler list.

GATES (preregistered).
  G1 ORDER: 20 time-permutations of E_full, primary (q0, ε=0.05).
     ORDER_DECORATIVE if max relative |Δm| at the 8 Euler points
     is < 1e-10.  (The abelian corner q0,ε=0 is reported separately:
     jumps [[I,0],[−z H,I]] commute, so order is a theorem there.)
  G2 LABELS: 20 root-assignment permutations, same primary;
     LABELS_DECORATIVE if max < 1e-10.
  G3 IDENTIFICATION: res(E_full)<res(E7)<res(E3) on TRUE, and
     res(E_full,TRUE) at least 3× smaller than the median res of
     (a) SCRAMBLE (b) WPERM, for BOTH embeddings and BOTH ε.
     Fit (α,β)∈R^2 on s=1.1 and s=2.0; res = max relative error
     on the remaining six Euler points.
  G4 FIREWALL: no Weil matrix, Weil eigenvalue, zeta zero, or
     Gabor object enters H_e or the ordering.

VERDICT.
  ORDERED_IDENTIFIES   if G1 and G2 non-decorative AND G3 fully holds
  ORDER_DECORATIVE     if G1 max < 1e-10
  LABELS_DECORATIVE    if G1 passes and G2 max < 1e-10
  NO_IDENTIFICATION    if G1,G2 pass but G3 fails (named sub-condition)
  INCONCLUSIVE         otherwise

CAVEAT (mandatory).  de Branges: every Herglotz function is the Weyl
function of some canonical system; existence of a canonical system
with Weyl function −Φ'/Φ is therefore equivalent to RH.  This probe
tests a specific rigid E8 ansatz for falsifiability only.
"""
from __future__ import annotations

import argparse
import ast
import hashlib
import itertools
import json
import math
import os
import sys

os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("MKL_NUM_THREADS", "1")
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
os.environ.setdefault("NUMEXPR_NUM_THREADS", "1")

import mpmath as mp  # noqa: E402
import numpy as np  # noqa: E402
import sympy as sp  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
mp.mp.dps = 25

# ---------------------------------------------------------------------------
# Frozen design.  SPEC_SHA is sha256 of the canonical JSON of SPEC.
# ---------------------------------------------------------------------------
UNITS30 = (1, 7, 11, 13, 17, 19, 23, 29)
EDGES_E8 = ((1, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (2, 4))
PHI30 = (1, 1, 0, -1, -1, -1, 0, 1, 1)
HIGHEST_COEF = (2, 3, 4, 6, 5, 4, 3, 2)
E3 = (2, 3, 4)
E7 = (2, 3, 4, 5, 7, 8, 9)
CAP = 50
S_EULER = (
    1.1 + 0.0j, 1.2 + 0.0j, 1.4 + 0.0j, 2.0 + 0.0j,
    1.1 + 0.5j, 1.2 + 1.0j, 1.5 + 2.0j, 3.0 + 1.0j,
)
FIT_S = (1.1 + 0.0j, 2.0 + 0.0j)
EMBEDS = ("q0", "twirl")
EPS_LIST = (0.0, 0.05)
PRIMARY_EMBED = "q0"
PRIMARY_EPS = 0.05
N_PERM = 20
N_HERGLOTZ = 20
N_NULL = 20
DECO_BAR = 1.0e-10
ID_FACTOR = 3.0
SEED_ORDER = 20261301
SEED_LABELS = 20261302
SEED_SCRAMBLE = 20261303
SEED_WPERM = 20261304
SEED_HERGLOTZ = 20261305
HERGLOTZ_TOL = 1.0e-8
NIL_TOL = 1.0e-10
CAVEAT = (
    "de Branges: every Herglotz function is the Weyl function of some "
    "canonical system; existence of a canonical system with Weyl function "
    "-Phi'/Phi is therefore equivalent to RH. This probe tests a specific "
    "rigid E8 ansatz for falsifiability only."
)
BANNED_CALLS = frozenset(
    {"zetazero", "zetazeros", "nzeros", "grampoint", "siegelz", "gabor"}
)

SPEC = {
    "round": "r613",
    "id": "PRIME.E8.ORDERED.HERGLOTZ.01",
    "firewall": "exploration, no RH claim, no physics claim",
    "cap": CAP,
    "E3": list(E3),
    "E7": list(E7),
    "s_euler": [str(s) for s in S_EULER],
    "fit_s": ["1.1", "2.0"],
    "eps": list(EPS_LIST),
    "embeds": list(EMBEDS),
    "primary_embed": PRIMARY_EMBED,
    "primary_eps": PRIMARY_EPS,
    "n_perm": N_PERM,
    "n_herglotz": N_HERGLOTZ,
    "n_null": N_NULL,
    "deco_bar": DECO_BAR,
    "id_factor": ID_FACTOR,
    "seeds": {
        "order": SEED_ORDER,
        "labels": SEED_LABELS,
        "scramble": SEED_SCRAMBLE,
        "wperm": SEED_WPERM,
        "herglotz": SEED_HERGLOTZ,
    },
    "label_rule": "totative:orbit[UNITS30][t%30]; gcd>1:pm2e_i[(t+n)%16]",
    "weyl": "W=(A Z+B)(C Z+D)^{-1}, Z=iI (fallback Z=-iI)",
    "xi": "whitened highest root; also e1",
    "caveat": CAVEAT,
}
SPEC_SHA = hashlib.sha256(
    json.dumps(SPEC, sort_keys=True, separators=(",", ":")).encode("utf-8")
).hexdigest()

CHECKS: list[tuple[str, bool, str]] = []
I8 = np.eye(8, dtype=np.float64)
I16 = np.eye(16, dtype=np.float64)
J16 = np.zeros((16, 16), dtype=np.float64)
J16[:8, 8:] = I8
J16[8:, :8] = -I8


def check(name: str, ok: bool, detail: str = "") -> bool:
    flag = bool(ok)
    CHECKS.append((name, flag, detail))
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


def fmtc(z: complex) -> str:
    z = complex(z)
    if not (math.isfinite(z.real) and math.isfinite(z.imag)):
        return "nan"
    return "%+.10e%+.10ej" % (z.real, z.imag)


def fmtf(x: float) -> str:
    x = float(x)
    if not math.isfinite(x):
        return "nan"
    return "%+.10e" % x


# ---------------------------------------------------------------------------
# C1/C2 fragments copied from e8_directed_readout_probe.py (no import).
# ---------------------------------------------------------------------------
def cartan_e8() -> sp.Matrix:
    a = sp.eye(8) * 2
    for i, j in EDGES_E8:
        a[i - 1, j - 1] = -1
        a[j - 1, i - 1] = -1
    return a


def euler_S(arrows: list[tuple[int, int]]) -> sp.Matrix:
    s = sp.eye(8)
    for i, j in arrows:
        s[i - 1, j - 1] = -1
    return s


def bipartite_arrows() -> list[tuple[int, int]]:
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


def _f2_points() -> list[tuple[int, int, int]]:
    return [(i & 1, (i >> 1) & 1, (i >> 2) & 1) for i in range(8)]


def hamming_code() -> tuple[tuple[int, ...], ...]:
    pts = _f2_points()
    gens = [tuple(1 for _ in range(8))]
    for j in range(3):
        gens.append(tuple(p[j] for p in pts))
    words = []
    for bits in itertools.product((0, 1), repeat=4):
        w = [0] * 8
        for b, g in zip(bits, gens):
            if b:
                for i in range(8):
                    w[i] ^= g[i]
        words.append(tuple(w))
    return tuple(sorted(words))


def construction_a_roots(code: tuple[tuple[int, ...], ...]) -> tuple[tuple[int, ...], ...]:
    roots = []
    for cw in code:
        ranges = []
        for i in range(8):
            if cw[i] == 0:
                ranges.append((-2, 0, 2))
            else:
                ranges.append((-1, 1))
        for v in itertools.product(*ranges):
            if sum(x * x for x in v) == 4:
                roots.append(v)
    return tuple(sorted(roots))


def bourbaki_perm(gram: np.ndarray) -> list[int] | None:
    adj = np.array(gram, dtype=int) == -1
    deg = adj.sum(axis=1)
    if sorted(int(d) for d in deg) != [1, 1, 1, 2, 2, 2, 2, 3]:
        return None
    branch = int(np.flatnonzero(deg == 3)[0])
    nbrs = [int(x) for x in np.flatnonzero(adj[branch])]

    def walk(start: int, prev: int) -> list[int]:
        path = [start]
        cur, pr = start, prev
        while True:
            nxt = [int(x) for x in np.flatnonzero(adj[cur]) if x != pr]
            if len(nxt) != 1:
                return path
            pr, cur = cur, nxt[0]
            path.append(cur)

    arms = sorted((walk(nb, branch) for nb in nbrs), key=len)
    if [len(a) for a in arms] != [1, 2, 4]:
        return None
    p = [0] * 8
    p[3] = branch
    p[1] = arms[0][0]
    p[2] = arms[1][0]
    p[0] = arms[1][1]
    p[4], p[5], p[6], p[7] = arms[2]
    return p


def simple_system(int_roots: tuple[tuple[int, ...], ...]) -> list[tuple[int, ...]]:
    wfun = np.array(
        [1.0, math.e, math.pi, math.sqrt(2.0), math.sqrt(3.0),
         math.sqrt(5.0), math.sqrt(7.0), math.sqrt(11.0)]
    )
    dots = np.array([float(np.dot(v, wfun)) for v in int_roots])
    pos = [v for v, d in zip(int_roots, dots) if d > 0.0]
    pos_set = set(pos)
    simple = []
    for a in pos:
        dec = False
        for b in pos:
            if b is a:
                continue
            ip = sum(x * y for x, y in zip(a, b))
            if ip == 2:
                diff = tuple(x - y for x, y in zip(a, b))
                if diff in pos_set:
                    dec = True
                    break
        if not dec:
            simple.append(a)
    return simple


def s_apply(alpha: tuple[int, ...], v: tuple[int, ...]) -> tuple[int, ...]:
    ip = sum(a * b for a, b in zip(alpha, v))
    k = ip // 2
    return tuple(x - k * a for x, a in zip(v, alpha))


def refl_mat(alpha: tuple[int, ...]) -> np.ndarray:
    a = np.asarray(alpha, dtype=np.float64)
    return np.eye(8, dtype=np.float64) - np.outer(a, a) / 2.0


def make_coxeter(simple_b: list[tuple[int, ...]], a_then_b: bool
                 ) -> tuple[object, np.ndarray]:
    idx_a, idx_b = (0, 3, 5, 7), (1, 2, 4, 6)
    seq_a = [simple_b[i] for i in idx_a]
    seq_b = [simple_b[i] for i in idx_b]
    seq = seq_a + seq_b if a_then_b else seq_b + seq_a

    def c_apply(v: tuple[int, ...]) -> tuple[int, ...]:
        for al in seq:
            v = s_apply(al, v)
        return v

    mat = np.eye(8, dtype=np.float64)
    for al in seq:
        mat = refl_mat(al) @ mat
    return c_apply, mat


def cartan_invsqrt(a_np: np.ndarray) -> np.ndarray:
    evals, evecs = np.linalg.eigh(a_np)
    if np.any(evals <= 1.0e-14):
        raise RuntimeError("Cartan not SPD")
    return (evecs * (1.0 / np.sqrt(evals))) @ evecs.T


def coord_roots() -> tuple[tuple[int, ...], ...]:
    out = []
    for sgn in (1, -1):
        for i in range(8):
            v = [0] * 8
            v[i] = 2 * sgn
            out.append(tuple(v))
    return tuple(out)


def build_orbits(int_roots: tuple[tuple[int, ...], ...], c_apply
                 ) -> list[tuple[tuple[int, ...], ...]]:
    used: set[tuple[int, ...]] = set()
    orbits: list[tuple[tuple[int, ...], ...]] = []
    for seed in int_roots:
        if seed in used:
            continue
        orb: list[tuple[int, ...]] = []
        v = seed
        for _ in range(30):
            orb.append(v)
            used.add(v)
            v = c_apply(v)
        orbits.append(tuple(orb))
    orbits.sort(key=lambda o: o[0])
    return orbits


# ---------------------------------------------------------------------------
# Arithmetic events.  Independent sieve; no primerange / zero table.
# ---------------------------------------------------------------------------
def prime_powers(cap: int) -> list[tuple[int, int, int]]:
    sieve = np.zeros(cap + 1, dtype=bool)
    out: list[tuple[int, int, int]] = []
    for p in range(2, cap + 1):
        if not sieve[p]:
            sieve[p * p::p] = True
            n, k = p, 1
            while n <= cap:
                out.append((n, p, k))
                n *= p
                k += 1
    out.sort(key=lambda t: t[0])
    return out


def assign_root(n: int, t: int, orbits, coords) -> tuple[int, ...]:
    if math.gcd(n, 30) == 1:
        j = UNITS30.index(n % 30)
        return orbits[j][t % 30]
    return coords[(t + n) % 16]


def make_events(ns: tuple[int, ...] | list[int], pp_map, orbits, coords
                ) -> list[dict]:
    ordered = sorted(int(n) for n in ns)
    ev = []
    for t, n in enumerate(ordered):
        p, k = pp_map[n]
        u = k * math.log(p)
        lam = 2.0 * math.log(p) / (p ** (0.5 * k))
        v = np.array(assign_root(n, t, orbits, coords), dtype=np.float64)
        ev.append(dict(n=n, p=p, k=k, t=t, u=u, lam=lam, v=v))
    return ev


def embed_w16(w: np.ndarray, c_w: np.ndarray, kind: str) -> np.ndarray:
    w16 = np.zeros(16, dtype=np.float64)
    if kind == "q0":
        w16[:8] = w
    elif kind == "twirl":
        cw = c_w @ w
        s = math.sqrt(2.0)
        w16[:8] = w / s
        w16[8:] = cw / s
    else:
        raise ValueError(kind)
    return w16


def hamiltonians(events: list[dict], embed: str, c_w: np.ndarray,
                 ainv: np.ndarray) -> list[np.ndarray]:
    out = []
    for e in events:
        w = ainv @ e["v"]
        w16 = embed_w16(w, c_w, embed)
        out.append(e["lam"] * np.outer(w16, w16))
    return out


def free_matrix(z: complex, eps: float, du: float) -> np.ndarray:
    if eps == 0.0 or du == 0.0:
        return np.eye(16, dtype=np.complex128)
    th = z * eps * du
    return np.cos(th) * I16 + np.sin(th) * J16


def jump_matrix(z: complex, h: np.ndarray) -> np.ndarray:
    return np.eye(16, dtype=np.complex128) + z * (J16 @ h)


def monodromy(z: complex, events: list[dict], hs: list[np.ndarray],
              eps: float) -> np.ndarray:
    m = np.eye(16, dtype=np.complex128)
    u_prev = 0.0
    for e, h in zip(events, hs):
        du = float(e["u"]) - u_prev
        m = jump_matrix(z, h) @ (free_matrix(z, eps, du) @ m)
        u_prev = float(e["u"])
    return m


def mobius(m: np.ndarray, zmat: np.ndarray) -> np.ndarray | None:
    a, b = m[:8, :8], m[:8, 8:]
    c, d = m[8:, :8], m[8:, 8:]
    lhs = a @ zmat + b
    rhs = c @ zmat + d
    try:
        wt = np.linalg.solve(rhs.T, lhs.T)
    except np.linalg.LinAlgError:
        return None
    return wt.T


def im_min(w: np.ndarray) -> float:
    h = (w - w.conj().T) / (2.0j)
    h = 0.5 * (h + h.conj().T)
    ev = np.linalg.eigvalsh(h.real)
    return float(np.min(ev))


def scalar_m(w: np.ndarray, xi: np.ndarray) -> complex:
    return complex(xi.conj() @ (w @ xi))


def weyl_scalar(z: complex, events: list[dict], hs: list[np.ndarray],
                eps: float, xi: np.ndarray, zsig: complex) -> complex:
    m = monodromy(z, events, hs, eps)
    zmat = zsig * np.eye(8, dtype=np.complex128)
    w = mobius(m, zmat)
    if w is None:
        return complex(float("nan"), float("nan"))
    return scalar_m(w, xi)


def system_ms(zs: list[complex], events: list[dict], embed: str, eps: float,
              c_w: np.ndarray, ainv: np.ndarray, xi: np.ndarray,
              zsig: complex) -> np.ndarray:
    hs = hamiltonians(events, embed, c_w, ainv)
    out = np.empty(len(zs), dtype=np.complex128)
    for i, z in enumerate(zs):
        out[i] = weyl_scalar(z, events, hs, eps, xi, zsig)
    return out


# ---------------------------------------------------------------------------
# Euler-side target (Re s > 1).  No zeros.
# ---------------------------------------------------------------------------
def xi_logderiv(s: complex):
    s = mp.mpc(s)
    return (
        1 / s + 1 / (s - 1)
        - mp.mpf("0.5") * mp.log(mp.pi)
        + mp.mpf("0.5") * mp.digamma(s / 2)
        + mp.zeta(s, derivative=1) / mp.zeta(s)
    )


def mpc_to_py(z) -> complex:
    z = mp.mpc(z)
    return complex(float(z.real), float(z.imag))


def target_m(s: complex) -> complex:
    half = s - 0.5
    return mpc_to_py(-xi_logderiv(s) / (2 * mp.mpc(half)))


def z_from_s(s: complex) -> complex:
    h = s - 0.5
    return h * h


def fit_alpha_beta(z1: complex, z2: complex, mx1: complex, mx2: complex,
                   m1: complex, m2: complex) -> tuple[float, float]:
    d1 = (m1 - mx1).real
    d2 = (m2 - mx2).real
    denom = (z2 - z1).real
    beta = (d2 - d1) / denom
    alpha = d1 - beta * z1.real
    return float(alpha), float(beta)


def residual(mx: np.ndarray, mt: np.ndarray, zs: list[complex],
             fit_idx: tuple[int, int], test_idx: list[int]
             ) -> tuple[float, float, float]:
    i1, i2 = fit_idx
    alpha, beta = fit_alpha_beta(zs[i1], zs[i2], mx[i1], mx[i2], mt[i1], mt[i2])
    worst = 0.0
    for k in test_idx:
        pred = mx[k] + alpha + beta * zs[k]
        den = abs(mt[k])
        if den < 1.0e-30 or not math.isfinite(pred.real):
            return float("inf"), alpha, beta
        worst = max(worst, abs(pred - mt[k]) / den)
    return float(worst), alpha, beta


def rel_pool(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    out = np.empty(a.size, dtype=np.float64)
    for i in range(a.size):
        den = abs(b[i])
        if den < 1.0e-30 or not math.isfinite(a[i].real):
            out[i] = float("inf")
        else:
            out[i] = abs(a[i] - b[i]) / den
    return out


def permute_times(events: list[dict], rng: np.random.Generator) -> list[dict]:
    us = np.array([e["u"] for e in events], dtype=np.float64)
    us = rng.permutation(us)
    out = []
    for e, u in zip(events, us):
        row = dict(e)
        row["u"] = float(u)
        out.append(row)
    out.sort(key=lambda r: (r["u"], r["n"]))
    return out


def permute_labels(events: list[dict], rng: np.random.Generator) -> list[dict]:
    vs = [e["v"].copy() for e in events]
    order = rng.permutation(len(vs))
    out = []
    for e, k in zip(events, order):
        row = dict(e)
        row["v"] = vs[int(k)]
        out.append(row)
    return out


def scramble_events(events: list[dict], rng: np.random.Generator) -> list[dict]:
    n = len(events)
    u = np.sort(np.array([e["u"] for e in events], dtype=np.float64))
    qs = np.sort(rng.uniform(0.0, 1.0, size=n))
    pos = np.interp(qs, np.linspace(0.0, 1.0, n), u)
    perm = rng.permutation(n)
    out = []
    for i in range(n):
        src = events[int(perm[i])]
        row = dict(src)
        row["u"] = float(pos[i])
        row["lam"] = float(src["lam"])
        row["v"] = src["v"].copy()
        out.append(row)
    out.sort(key=lambda r: (r["u"], r["n"]))
    return out


def wperm_events(events: list[dict], rng: np.random.Generator) -> list[dict]:
    lams = np.array([e["lam"] for e in events], dtype=np.float64)
    rng.shuffle(lams)
    out = []
    for e, lam in zip(events, lams):
        row = dict(e)
        row["lam"] = float(lam)
        out.append(row)
    return out


def ast_firewall(src: str) -> list[str]:
    tree = ast.parse(src)
    hits = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            fn = node.func
            name = fn.attr if isinstance(fn, ast.Attribute) else (
                fn.id if isinstance(fn, ast.Name) else "")
            if name.lower() in BANNED_CALLS:
                hits.append(name)
        if isinstance(node, ast.ImportFrom):
            mod = node.module or ""
            if mod.startswith("rh") or "verification" in mod.split("."):
                hits.append("import " + mod)
        if isinstance(node, ast.Import):
            for alias in node.names:
                if alias.name.startswith("rh") or "verification" in alias.name:
                    hits.append("import " + alias.name)
    return sorted(set(hits))


def choose_zsig(events: list[dict], c_w: np.ndarray, ainv: np.ndarray,
                xi: np.ndarray) -> complex:
    hs = hamiltonians(events, "q0", c_w, ainv)
    z_cal = 1.0j
    m = monodromy(z_cal, events, hs, 0.0)
    best_sig, best_im = 1.0j, -1.0e9
    for sig in (1.0j, -1.0j):
        w = mobius(m, sig * np.eye(8, dtype=np.complex128))
        if w is None:
            continue
        imv = im_min(w)
        if imv > best_im:
            best_im, best_sig = imv, sig
    return complex(best_sig)


def g1g2_stats(true_ev: list[dict], zs: list[complex], mx_true: np.ndarray,
               embed: str, eps: float, c_w: np.ndarray, ainv: np.ndarray,
               xi: np.ndarray, zsig: complex, n_perm: int, seed: int,
               kind: str) -> tuple[float, float]:
    rels: list[float] = []
    for k in range(n_perm):
        rng = np.random.default_rng(seed + k)
        if kind == "order":
            ev = permute_times(true_ev, rng)
        else:
            ev = permute_labels(true_ev, rng)
        mx = system_ms(zs, ev, embed, eps, c_w, ainv, xi, zsig)
        rels.extend(float(x) for x in rel_pool(mx, mx_true))
    arr = np.array(rels, dtype=np.float64)
    return float(np.max(arr)), float(np.median(arr))


def median_res(events: list[dict], kind: str, n_null: int, seed: int,
               zs: list[complex], mt: np.ndarray, fit_idx, test_idx,
               embed: str, eps: float, c_w, ainv, xi, zsig) -> float:
    vals = []
    for k in range(n_null):
        rng = np.random.default_rng(seed + 1000 * (0 if kind == "SCRAMBLE" else 1) + k)
        if kind == "SCRAMBLE":
            ev = scramble_events(events, rng)
        else:
            ev = wperm_events(events, rng)
        mx = system_ms(zs, ev, embed, eps, c_w, ainv, xi, zsig)
        r, _, _ = residual(mx, mt, zs, fit_idx, test_idx)
        vals.append(r)
    return float(np.median(np.array(vals, dtype=np.float64)))


def run(smoke: bool) -> int:
    n_perm = 3 if smoke else N_PERM
    n_herg = 5 if smoke else N_HERGLOTZ
    n_null = 3 if smoke else N_NULL

    print("=" * 74)
    print("prime_e8_ordered_herglotz_probe -- r613 PRIME.E8.ORDERED.HERGLOTZ.01")
    print("Firewall: exploration, no RH claim, no physics claim")
    print("mode: %s" % ("SMOKE" if smoke else "FULL"))
    print("SPEC %s" % SPEC_SHA[:16])
    print("FILE %s" % file_sha256())
    print("=" * 74, flush=True)

    src = open(os.path.abspath(__file__), encoding="utf-8").read()
    hits = ast_firewall(src)
    section("G4  firewall")
    check("G4.AST_no_zero_gabor_rh", not hits, str(hits) if hits else "clean")
    check(
        "G4.construction_uses_primes_E8_Euler",
        True,
        "H_e and ordering: primes + E8 roots only; target xi/zeta on Re s>1",
    )
    print(
        "  FIREWALL: no Weil matrix, Weil eigenvalue, zeta zero, or Gabor "
        "object enters H_e or the ordering.",
        flush=True,
    )

    section("C0  E8 Seifert / Construction A / Coxeter orbits")
    a_sym = cartan_e8()
    arrows = bipartite_arrows()
    c_sei = coxeter_from_arrows(arrows)
    x = sp.symbols("x")
    cp = [int(c) for c in sp.Poly(c_sei.charpoly(x).as_expr(), x).all_coeffs()]
    c30 = sp.simplify(c_sei ** 30)
    check("C0.Seifert_charpoly_Phi30", tuple(cp) == PHI30, str(cp))
    check("C0.Seifert_C^30=I", c30 == sp.eye(8), "order 30")
    a_np = np.array(a_sym, dtype=np.float64)
    ainv = cartan_invsqrt(a_np)
    check("C0.Cartan_SPD_det1", abs(float(np.linalg.det(a_np)) - 1.0) < 1.0e-8)

    code = hamming_code()
    int_roots = construction_a_roots(code)
    n_coord = sum(1 for r in int_roots if max(abs(x) for x in r) == 2)
    check(
        "C0.ConstructionA_240=16+224",
        len(int_roots) == 240 and n_coord == 16,
        "N=%d coord=%d" % (len(int_roots), n_coord),
    )
    simple = simple_system(int_roots)
    check("C0.simple_system_8", len(simple) == 8, "n=%d" % len(simple))
    gram = np.array(
        [[sum(a * b for a, b in zip(simple[i], simple[j])) / 2.0
          for j in range(8)] for i in range(8)]
    )
    p = bourbaki_perm(np.rint(gram).astype(int))
    check("C0.bourbaki_perm", p is not None, str(p))
    simple_b = [simple[p[k]] for k in range(8)]
    gram_b = np.array(
        [[sum(a * b for a, b in zip(simple_b[i], simple_b[j])) / 2.0
          for j in range(8)] for i in range(8)]
    )
    check(
        "C0.Gram=Cartan",
        np.allclose(gram_b, a_np, atol=1.0e-10),
        "max|Δ|=%.3e" % float(np.max(np.abs(gram_b - a_np))),
    )

    c_apply, c_w = make_coxeter(simple_b, a_then_b=True)
    probe = int_roots[0]
    v = probe
    for _ in range(30):
        v = c_apply(v)
    if v != probe:
        c_apply, c_w = make_coxeter(simple_b, a_then_b=False)
        v = probe
        for _ in range(30):
            v = c_apply(v)
    check("C0.C_W^30_fixes_a_root", v == probe, "closed")
    check(
        "C0.C_W_float_order30",
        float(np.linalg.norm(np.linalg.matrix_power(c_w, 30) - I8)) < 1.0e-8
        and float(np.linalg.norm(np.linalg.matrix_power(c_w, 15) + I8)) < 1.0e-6,
        "||C^30-I||, ||C^15+I||",
    )
    orbits = build_orbits(int_roots, c_apply)
    sizes = sorted(len(o) for o in orbits)
    closed = all(c_apply(o[-1]) == o[0] for o in orbits)
    check(
        "C0.orbits_8x30",
        len(orbits) == 8 and sizes == [30] * 8 and closed,
        "n_orb=%d sizes=%s" % (len(orbits), sizes[:8]),
    )
    coords = coord_roots()
    check("C0.coord_roots_16", len(coords) == 16 and all(r in int_roots for r in coords))

    alpha = np.array(simple_b, dtype=np.float64)
    v_hr = alpha.T @ np.array(HIGHEST_COEF, dtype=np.float64)
    v_hr_int = tuple(int(round(x)) for x in v_hr)
    check("C0.highest_root_in_Phi", v_hr_int in set(int_roots), str(v_hr_int))
    w_hr = ainv @ np.array(v_hr_int, dtype=np.float64)
    nrm = float(np.linalg.norm(w_hr))
    xi_hr = w_hr / nrm
    xi_e1 = np.zeros(8, dtype=np.float64)
    xi_e1[0] = 1.0
    check("C0.xi_unit", abs(float(np.linalg.norm(xi_hr)) - 1.0) < 1.0e-12)

    pp = prime_powers(CAP)
    pp_map = {n: (p, k) for n, p, k in pp}
    n_full = tuple(n for n, _p, _k in pp)
    check("C0.E_full_N", len(n_full) >= 20, "N=%d cap=%d" % (len(n_full), CAP))
    print("  E_full N=%d  n=%s" % (len(n_full), ",".join(str(n) for n in n_full)))
    print("  label: totative n mod 30 -> orbit j in UNITS30; gcd>1 -> pm2e_i[(t+n) mod 16]")
    print("  Coxeter: bipartite s_B s_A (or s_A s_B if needed) of Bourbaki simple system")
    print("  embedding q0=(w,0); twirl=(w, C_W w)/sqrt(2); w=A^{-1/2} v", flush=True)

    sets = {
        "E3": make_events(E3, pp_map, orbits, coords),
        "E7": make_events(E7, pp_map, orbits, coords),
        "E_full": make_events(n_full, pp_map, orbits, coords),
    }
    check("C0.E3", [e["n"] for e in sets["E3"]] == list(E3))
    check("C0.E7", [e["n"] for e in sets["E7"]] == list(E7))

    section("C0  nilpotency / symplectic / Herglotz")
    ev0 = sets["E3"]
    for embed in EMBEDS:
        hs = hamiltonians(ev0, embed, c_w, ainv)
        h0 = hs[0]
        jh = J16 @ h0
        nil = float(np.linalg.norm(jh @ jh))
        w16 = embed_w16(ainv @ ev0[0]["v"], c_w, embed)
        wjw = float(w16 @ (J16 @ w16))
        ztest = 0.3 + 0.7j
        x = ztest * jh
        expm = I16.astype(np.complex128) + x  # (JH)^2=0 => Taylor exact
        jump = jump_matrix(ztest, h0)
        check(
            "C0.nilpotency_%s" % embed,
            nil < NIL_TOL and abs(wjw) < NIL_TOL,
            "||(JH)^2||=%.3e  wJw=%.3e" % (nil, wjw),
        )
        check(
            "C0.exp_identity_%s" % embed,
            float(np.linalg.norm(jump - expm)) < NIL_TOL,
            "||(I+zJH)-expm||",
        )
    m_real = monodromy(0.5 + 0.0j, ev0, hamiltonians(ev0, "q0", c_w, ainv), 0.0)
    symp = m_real.T.real @ J16 @ m_real.real
    check(
        "C0.symplectic_real_z",
        float(np.linalg.norm(symp - J16)) < 1.0e-8,
        "||M^T J M - J||",
    )

    zsig = choose_zsig(ev0, c_w, ainv, xi_hr)
    print("  Weyl Z = %s I  (Möbius image of this marker)" % ("+i" if zsig.imag > 0 else "-i"))
    rng_h = np.random.default_rng(SEED_HERGLOTZ)
    hs_full_p = hamiltonians(sets["E_full"], PRIMARY_EMBED, c_w, ainv)
    ims = []
    for _ in range(n_herg):
        zr = float(rng_h.normal())
        zi = float(rng_h.uniform(0.15, 1.8))
        w = mobius(
            monodromy(zr + 1j * zi, sets["E_full"], hs_full_p, PRIMARY_EPS),
            zsig * np.eye(8, dtype=np.complex128),
        )
        ims.append(-1.0 if w is None else im_min(w))
    herg_ok = all(v >= -HERGLOTZ_TOL for v in ims)
    check(
        "C0.Herglotz_ImW_succeq_0",
        herg_ok,
        "n=%d min_eig=%.3e zsig=%s" % (n_herg, min(ims) if ims else float("nan"),
                                       "+i" if zsig.imag > 0 else "-i"),
    )

    section("T  Euler target m(z)=-Phi'/Phi")
    zs = [z_from_s(s) for s in S_EULER]
    mt = np.array([target_m(s) for s in S_EULER], dtype=np.complex128)
    in_h = []
    for s, z in zip(S_EULER, zs):
        flag = z.imag > 1.0e-14
        in_h.append(flag)
        print(
            "  s=%s  z=%s  in_H=%s  m=%s"
            % (fmtc(s), fmtc(z), "Y" if flag else "N", fmtc(target_m(s))),
            flush=True,
        )
    check(
        "T.in_H_pattern",
        in_h == [False, False, False, False, True, True, True, True],
        "real s => z real; four complex s => z in H",
    )
    fit_idx = (0, 3)  # s=1.1 and s=2.0
    test_idx = [i for i in range(8) if i not in fit_idx]
    check("T.fit_points", S_EULER[0] == 1.1 + 0.0j and S_EULER[3] == 2.0 + 0.0j)
    check("T.zeta_Re_gt_1", all(s.real >= 1.1 for s in S_EULER))

    section("G1/G2  order and labels (primary q0, eps=0.05)")
    primary = (PRIMARY_EMBED, PRIMARY_EPS)
    g1 = {}
    g2 = {}
    mx_cache: dict[tuple, np.ndarray] = {}
    for embed, eps in itertools.product(EMBEDS, EPS_LIST):
        mx = system_ms(zs, sets["E_full"], embed, eps, c_w, ainv, xi_hr, zsig)
        mx_cache[("E_full", embed, eps, "TRUE")] = mx
        g1[embed, eps] = g1g2_stats(
            sets["E_full"], zs, mx, embed, eps, c_w, ainv, xi_hr, zsig,
            n_perm, SEED_ORDER, "order",
        )
        g2[embed, eps] = g1g2_stats(
            sets["E_full"], zs, mx, embed, eps, c_w, ainv, xi_hr, zsig,
            n_perm, SEED_LABELS, "labels",
        )
        print(
            "  G1 ORDER  embed=%-5s eps=%.2f  max=%s  median=%s"
            % (embed, eps, fmtf(g1[embed, eps][0]), fmtf(g1[embed, eps][1])),
            flush=True,
        )
        print(
            "  G2 LABELS embed=%-5s eps=%.2f  max=%s  median=%s"
            % (embed, eps, fmtf(g2[embed, eps][0]), fmtf(g2[embed, eps][1])),
            flush=True,
        )
    g1_max, g1_med = g1[primary]
    g2_max, g2_med = g2[primary]
    g1_deco = g1_max < DECO_BAR
    g2_deco = g2_max < DECO_BAR
    q0_eps0_deco = g1[("q0", 0.0)][0] < DECO_BAR
    check(
        "G1.q0_eps0_commuting_jumps",
        q0_eps0_deco,
        "max=%s (expected decorative)" % fmtf(g1[("q0", 0.0)][0]),
    )
    check(
        "G1.primary_non_decorative",
        not g1_deco,
        "embed=%s eps=%s max=%s median=%s" % (PRIMARY_EMBED, PRIMARY_EPS,
                                              fmtf(g1_max), fmtf(g1_med)),
    )
    check(
        "G2.primary_non_decorative",
        not g2_deco,
        "max=%s median=%s" % (fmtf(g2_max), fmtf(g2_med)),
    )

    section("G3  identification residual table")
    print(
        "  %-6s %-8s %-6s %6s %14s %14s %14s"
        % ("set", "world", "embed", "eps", "res", "alpha", "beta"),
        flush=True,
    )
    table: dict[tuple, tuple[float, float, float]] = {}
    # TRUE for all sets × embed × eps
    for sname, embed, eps in itertools.product(("E3", "E7", "E_full"), EMBEDS, EPS_LIST):
        key = (sname, embed, eps, "TRUE")
        if key not in mx_cache:
            mx_cache[key] = system_ms(
                zs, sets[sname], embed, eps, c_w, ainv, xi_hr, zsig
            )
        mx = mx_cache[key]
        res, alpha, beta = residual(mx, mt, zs, fit_idx, test_idx)
        table[key] = (res, alpha, beta)
        print(
            "  %-6s %-8s %-6s %6.2f %14s %14s %14s"
            % (sname, "TRUE", embed, eps, fmtf(res), fmtf(alpha), fmtf(beta)),
            flush=True,
        )
    # SCRAMBLE / WPERM medians
    for sname, embed, eps, world in itertools.product(
        ("E3", "E7", "E_full"), EMBEDS, EPS_LIST, ("SCRAMBLE", "WPERM")
    ):
        med = median_res(
            sets[sname], world, n_null,
            SEED_SCRAMBLE if world == "SCRAMBLE" else SEED_WPERM,
            zs, mt, fit_idx, test_idx, embed, eps, c_w, ainv, xi_hr, zsig,
        )
        table[(sname, embed, eps, world)] = (med, float("nan"), float("nan"))
        print(
            "  %-6s %-8s %-6s %6.2f %14s %14s %14s"
            % (sname, world, embed, eps, fmtf(med), "n/a", "n/a"),
            flush=True,
        )

    ab_pri = table[("E_full", PRIMARY_EMBED, PRIMARY_EPS, "TRUE")]
    print(
        "  fitted (alpha,beta) primary E_full TRUE: (%s, %s)"
        % (fmtf(ab_pri[1]), fmtf(ab_pri[2])),
        flush=True,
    )

    # xi = e1, E_full TRUE only
    print("  xi=e1  E_full TRUE residuals:")
    e1_res = {}
    for embed, eps in itertools.product(EMBEDS, EPS_LIST):
        mx = system_ms(zs, sets["E_full"], embed, eps, c_w, ainv, xi_e1, zsig)
        r, a, b = residual(mx, mt, zs, fit_idx, test_idx)
        e1_res[embed, eps] = r
        print(
            "    embed=%-5s eps=%.2f  res=%s  alpha=%s  beta=%s"
            % (embed, eps, fmtf(r), fmtf(a), fmtf(b)),
            flush=True,
        )

    chain_ok = {}
    scramble_ok = {}
    wperm_ok = {}
    for embed, eps in itertools.product(EMBEDS, EPS_LIST):
        r3 = table[("E3", embed, eps, "TRUE")][0]
        r7 = table[("E7", embed, eps, "TRUE")][0]
        rf = table[("E_full", embed, eps, "TRUE")][0]
        rs = table[("E_full", embed, eps, "SCRAMBLE")][0]
        rw = table[("E_full", embed, eps, "WPERM")][0]
        chain_ok[embed, eps] = (rf < r7 < r3) and all(math.isfinite(x) for x in (rf, r7, r3))
        scramble_ok[embed, eps] = math.isfinite(rf) and math.isfinite(rs) and (rf * ID_FACTOR <= rs)
        wperm_ok[embed, eps] = math.isfinite(rf) and math.isfinite(rw) and (rf * ID_FACTOR <= rw)
        print(
            "  G3 %s ε=%.2f  chain %s  vsSCR %s (TRUE %s / med %s)  vsWPERM %s"
            % (embed, eps,
               "Y" if chain_ok[embed, eps] else "N",
               "Y" if scramble_ok[embed, eps] else "N",
               fmtf(rf), fmtf(rs),
               "Y" if wperm_ok[embed, eps] else "N"),
            flush=True,
        )

    g3_chain_all = all(chain_ok.values())
    g3_scr_all = all(scramble_ok.values())
    g3_wperm_all = all(wperm_ok.values())
    g3_ok = g3_chain_all and g3_scr_all and g3_wperm_all
    fails = []
    if not g3_chain_all:
        bad = [k for k, v in chain_ok.items() if not v]
        fails.append("CHAIN_FAIL%s" % (bad,))
    if not g3_scr_all:
        bad = [k for k, v in scramble_ok.items() if not v]
        fails.append("SCRAMBLE_3x_FAIL%s" % (bad,))
    if not g3_wperm_all:
        bad = [k for k, v in wperm_ok.items() if not v]
        fails.append("WPERM_3x_FAIL%s" % (bad,))
    check("G3.chain_all_embed_eps", g3_chain_all, str(chain_ok))
    check("G3.scramble_3x_all", g3_scr_all)
    check("G3.wperm_3x_all", g3_wperm_all)

    section("VERDICT")
    print(CAVEAT, flush=True)
    n_fail = sum(1 for _n, ok, _d in CHECKS if not ok)
    if not herg_ok:
        verdict = "INCONCLUSIVE"
        why = "Herglotz check failed"
    elif g1_deco:
        verdict = "ORDER_DECORATIVE"
        why = "G1 max=%s < %s on primary (q0, eps=0.05)" % (fmtf(g1_max), DECO_BAR)
    elif g2_deco:
        verdict = "LABELS_DECORATIVE"
        why = "G2 max=%s < %s on primary" % (fmtf(g2_max), DECO_BAR)
    elif g3_ok:
        verdict = "ORDERED_IDENTIFIES"
        why = "G1,G2 non-decorative and G3 holds for all embed x eps"
    elif (not g1_deco) and (not g2_deco):
        verdict = "NO_IDENTIFICATION"
        why = "; ".join(fails) if fails else "G3 failed"
    else:
        verdict = "INCONCLUSIVE"
        why = "unclassified (n_fail=%d)" % n_fail

    print("  G1 primary max=%s median=%s decorative=%s" % (
        fmtf(g1_max), fmtf(g1_med), "Y" if g1_deco else "N"))
    print("  G2 primary max=%s median=%s decorative=%s" % (
        fmtf(g2_max), fmtf(g2_med), "Y" if g2_deco else "N"))
    print("  G3 fully_holds=%s  %s" % ("Y" if g3_ok else "N", why))
    print("  N_E_full=%d  zsig=%s  xi=highest_root" % (
        len(n_full), "+i" if zsig.imag > 0 else "-i"))
    print("  label_rule: totative orbit UNITS30[n mod 30], phase t=index mod 30;")
    print("              gcd>1 uses pm2e_i[(t+n) mod 16]")
    print("VERDICT: %s" % verdict, flush=True)
    print("SPEC %s" % SPEC_SHA[:16], flush=True)
    print("why: %s" % why, flush=True)
    return 0


def main() -> int:
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    return run(bool(args.smoke))


if __name__ == "__main__":
    sys.exit(main())
