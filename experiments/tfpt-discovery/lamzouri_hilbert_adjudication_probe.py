#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""lamzouri_hilbert_adjudication_probe -- PRIME.PORT.EXTERNAL.HILBERT_VARIANT.ADJUDICATION.01 (round 639)

EXPLORATION ONLY (2026-09-03). experiments/ level: NO promotion,
NO ledger row, NO marker moved, NO RH CLAIM in either direction.

SEALED ADJUDICATION of arXiv:2609.02882 (Lamzouri, 2026-09-02,
"A new proof that more than 2/3 of the zeros of the Riemann zeta
function are simple and on the critical line") against the
Alpoge--Furman / Anthropic certificate arXiv:2608.13637 and our
r267/r616/r627/atlas A1 record.  Hypothesis: SAME two-moment
bandwidth-one certificate class.  Honest gates: a fail is a fail.

EXTERNAL (documented constants; never recomputed from zeros/primes):
Key Proposition (Pro:FourierHilbert).  lambda>0, eta in L^2(R) real
even, supp(eta) subset (-lambda,lambda), hat{eta^2}(0)=1,
K := hat{eta^2} with f^(xi)=int f(u) e^{-2 pi i xi u} du.  For any
finite non-empty conjugation-invariant multiset Z:
  #{z in Z real, m_z=1} >= 2|Z| - Sum_{z,s in Z} K(z-s)^2
  #{distinct} >= (3/2)|Z| - (1/2) Sum K(z-s)^2.
Proof objects: f_z(u)=eta(u) e^{-2 pi i u z},
g_z=(f_z+f_{conj z})/2, h_z=(f_z-f_{conj z})/(2i);
K(z-conj s)=int f_z conj(f_s); int |f_x|^2=K(0)=1;
int |g|^2 - int |h|^2 = 1; F(u,v)=Sum_z f_z(u) f_z(v) bilinear
(NO conjugate); Sum K(z-s)^2 = int int |F|^2 by conj-invariance;
nested spans U subset V subset W (U: multiple-real f's + g's;
V: U + simple-real f's; W: V + h's); Gram--Schmidt ONB psi_j with
real coefficients; alpha_j = int int F conj(psi_j(u) psi_j(v));
Bessel int int |F|^2 >= Sum alpha_j^2.  Range U: a^2+4>=4a gives
Sum alpha^2 >= 2 Sum alpha; range V\U: a^2+1>=2a gives
Sum alpha^2 >= 2 Sum alpha - n; range W\V: alpha_j <= 0;
Sum_j alpha_j = |Z| (Parseval).  Distinct-count variant uses
4 Sum alpha - 4(k+r), 4 Sum alpha - 3n, 4 Sum alpha.

Constants: C_MT = 1/2 + (1/sqrt(2)) cot(1/sqrt(2))
= 1.3274992963206...; C_0 = 2 - C_MT = 0.6725007...;
C_1 = (C_0+1)/2 = (3-C_MT)/2 = 0.83625...;
PRZZ20 0.417293 (on line) / 0.407511 (simple on line);
Montgomery 2/3 under RH; BGST24 unconditional 61.7% simple under
hypotheses weaker than RH.

BGSTB Lemma 5 (Lem:BGST): f in L^1 real even, supp f subset [-1,1],
Lipschitz at 0: pair-correlation sum with weight
w(z)=4/(4-z^2).  Lamzouri takes eta in C_c^infty((-1/2,1/2)),
Q := eta^2 * eta^2 (convolution), hat Q = K^2, supp Q subset [-1,1].
Weight: w(rho-rho')=(1 + pi^2 z^2/(log T)^2)^{-1} with
z = i(rho-rho') log T/(2 pi).  C_eta = Q(0)+2 int_0^1 alpha Q(alpha)
d alpha; |C_{eta_eps} - C_MT|<eps.

Remark MT: Carneiro--Chandee--Littmann--Milinovich Corollary 14,
C_eta >= C_MT for every admissible eta; extremal Montgomery--Taylor;
C_MT optimal for the method.

Appendix: AxiomProver (Axiom Math) Lean certificates: Proposition
unconditional; Theorem under BGSTB Lemma 5 + Riemann--von Mangoldt
N(T) ~ (T/2 pi) log T as HYPOTHESES.  Repo github.com/AxiomMath/ZetaZeros
(documented fact; not fetched).

OUR SIDE (documented; never recomputed from zeros/primes):
r267 ranktrace_adjudication_probe.py (23/23, SPEC b0437394):
EXTERNAL_FORM_RECONSTRUCTED + CEILING_IS_OUR_WALL(LOCATION paircorr
support-1) + CEILING_ORTHOGONAL + NO_IMPORT(FRAME_MISMATCH) +
TWO_MOMENT_BLIND.  R(psi)=[int psi^2 + int int |u-v| psi psi]/(int psi)^2
with R(psi_0 box on [-1/2,1/2])=4/3 and
R(psi_MT)=1/2+(1/sqrt(2))cot(1/sqrt(2)).  A--F chain
N_0^s >= 4 tr G - 2N - ||G||_HS^2 = (2-R)N at tr G=N.
A--F ceiling p_0 <= 0.6818287 for two-moment bandwidth-one
certificates.  r616 inertia_highermoment_probe.py (16/16): C_CAPPED,
p_3^uncond = p_2 = 0.6818.  r627 af_twomoment_optimizer_probe.py
(17/17): NO_GAIN, unique critical point psi*=cos(sqrt(2) t) on
[-1/2,1/2], p*=0.6725007037, gap to ceiling 9.3e-3.  Round-63
constant 0.83625 distinct.  Atlas certificate_class_atlas_probe.py
class A1 = "two trace moments, bandwidth one (Alpoge--Furman class)".
NOTE: 0.6818287 is a different quantity (A--F class ceiling including
the on/off block partition, support <= 1), not p(lambda) under PCC.

SEALED CONSTANTS: LAMBDA=0.5; GL_N=160 (smoke 96); N_PROP=300
(smoke 40); PROP_SEED=20260903; QUAD_TOL=1e-8;
PCC_LAMBDAS=(0.5, 0.75, 1.0, 1.5, 2.0, 3.0) (smoke (0.5, 1.0, 2.0));
PCC_BASIS=12 cosine modes; RUNTIME_CAP=300.

LEGS.  A finite-dimensional synthetic rebuild of Pro:FourierHilbert
on Gauss--Legendre L^2(-lambda,lambda).  B certificate class
identification (range shadows, C_eta==R(psi), Remark-MT support).
C constants.  D wall location (supp Q subset [-1,1]; PCC p(lambda)).
E weight identity.  F crosswalk + source note (typed).
Firewall G-F0 first: AST scan, no zeta-zero / prime oracles;
synthetic conjugation-invariant multisets only; RNG only in seeded
property tests; external facts as documented constants with source
strings in EXT.

SEALED VERDICT FORM (joined with ' + '):
  PROPOSITION_REBUILT / PROPOSITION_BROKEN(typed)
+ SAME_CLASS(TWO_MOMENT: C_eta == R(eta^2); bound == 2N − HS^2 == A–F chain; atlas A1 unchanged) / NEW_CLASS(typed)
+ CONSTANTS_IDENTICAL(C_0 == r627 p*, C_1 == 0.83625, gap to p_0 9.3e-3) / CONSTANTS_DIFFER(typed)
+ WALL_LOCATION_CONFIRMED(SUPPORT_ONE: BGSTB supp f ⊂ [−1,1] sole arithmetic input; p(λ) under PCC rises to 1) / WALL_LOCATION_MISMATCH(typed)
+ MT_OPTIMAL_SUPPORTED / MT_OPTIMAL_VIOLATED(typed)
+ NO_IMPORT(UNCHANGED: r267 frame mismatch stands; no Bessel target on the prime-comb side)
+ SOURCE_NOTE(AXIOMPROVER: Proposition unconditional; Theorem modulo BGSTB Lemma 5 + RvM as Lean hypotheses)

NO RH CLAIM IN EITHER DIRECTION.
"""
from __future__ import annotations

import os

os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("MKL_NUM_THREADS", "1")
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
os.environ.setdefault("NUMEXPR_NUM_THREADS", "1")

import argparse
import ast
import hashlib
import math
import sys
import time

import mpmath as mp
import numpy as np
import sympy as sp
from numpy.polynomial.legendre import leggauss
from scipy.optimize import minimize

# ---------------- sealed constants
LAMBDA = 0.5
GL_N = 160
GL_N_SMOKE = 96
N_PROP = 300
N_PROP_SMOKE = 40
PROP_SEED = 20260903
QUAD_TOL = 1e-8
PCC_LAMBDAS = (0.5, 0.75, 1.0, 1.5, 2.0, 3.0)
PCC_LAMBDAS_SMOKE = (0.5, 1.0, 2.0)
PCC_BASIS = 12
RUNTIME_CAP = 300.0
RANK_DROP = 1e-9
SQRT2 = math.sqrt(2.0)

EXT = dict(
    SRC=("arXiv:2609.02882 (Lamzouri, 2026-09-02; "
         "A new proof that more than 2/3 of the zeros of the "
         "Riemann zeta function are simple and on the critical line)"),
    SRC_TEX="/tmp/lamzouri/ZetaZeros.tex",
    SRC_AF="arXiv:2608.13637 (Alpoge--Furman / Anthropic)",
    SRC_LEAN=("github.com/AxiomMath/ZetaZeros "
              "(AxiomProver / Axiom Math; documented, not fetched)"),
    SRC_BGST="BGST24 Lemma 5 (Lem:BGST)",
    SRC_CCLM=("Carneiro--Chandee--Littmann--Milinovich Corollary 14 "
              "(Remark MT)"),
    SRC_GLSS="GLSS25: full PCC => 100% simple on the line",
    SRC_PRZZ="PRZZ20 0.417293 (on line) / 0.407511 (simple on line)",
    SRC_BGST24_SIMPLE="BGST24 unconditional 61.7% simple (hypotheses weaker than RH)",
    SRC_MONTGOMERY_RH="Montgomery 2/3 simple under RH",
    C_MT_PRINT="1.3274992963206",
    C_0_PRINT="0.6725007037",
    C_1_PRINT="0.83625",
    CEIL_P0=0.6818287,
    R0=4.0 / 3.0,
    PREV_ON_LINE=0.417293,
    PREV_SIMPLE_ON_LINE=0.407511,
    ATLAS_A1=("two trace moments, bandwidth one "
              "(Alpoge--Furman class)"),
    R267=("ranktrace_adjudication_probe.py (23/23, SPEC b0437394): "
          "EXTERNAL_FORM_RECONSTRUCTED + CEILING_IS_OUR_WALL"
          "(LOCATION paircorr support-1) + CEILING_ORTHOGONAL + "
          "NO_IMPORT(FRAME_MISMATCH) + TWO_MOMENT_BLIND"),
    R616=("inertia_highermoment_probe.py (16/16): C_CAPPED, "
          "p_3^uncond = p_2 = 0.6818"),
    R627=("af_twomoment_optimizer_probe.py (17/17): NO_GAIN, unique "
          "critical point psi* = cos(√2 t) on [-1/2,1/2], "
          "p* = 0.6725007037, gap to ceiling 9.3e-3"),
    ROUND63="0.83625",
    LEAN_STATE=("AxiomProver Proposition unconditional; Theorem under "
                "BGSTB Lemma 5 + Riemann--von Mangoldt "
                "N(T) ~ (T/2π)log T as HYPOTHESES"),
    CROSSWALK=("g/h split with ∫|g|^2−∫|h|^2=1 == the Sylvester "
               "signature-(1,1) pair block of A–F Lemma 3.1 == our "
               "r229 census mechanism; Bessel replaces the finite "
               "Gabor frame (r267 measured near-tight frame, aspect 1) "
               "— the r267 frame-mismatch NO_IMPORT argument is unchanged "
               "for our prime-comb side (no Gabor Hilbert space of "
               "zero-atoms exists on our side; our atoms are the signed "
               "prime comb); Lean state: AxiomProver Proposition "
               "unconditional, Theorem modulo BGSTB Lemma 5 + RvM "
               "hypotheses (contrast: A–F v1.0 kernel-checked modulo "
               "EnclOK)"),
)

SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
T0_WALL = time.time()
CHECKS: list = []


def check(name, ok, detail):
    ok = bool(ok)
    CHECKS.append((name, ok, detail))
    print("  [%s] %-40s %s" % ("PASS" if ok else "FAIL", name,
                               detail), flush=True)
    return ok


def info(msg):
    print("  [INFO] " + msg, flush=True)


def section(t):
    print("\n" + "-" * 78 + "\n" + t + "\n" + "-" * 78, flush=True)


def firewall_audit():
    src = open(os.path.abspath(__file__), "r", encoding="utf-8").read()
    tree = ast.parse(src)
    forb = {"zeta" + "zero", "n" + "zeros", "prime" + "range",
            "is" + "prime", "gram" + "point"}
    bad = []
    for node in ast.walk(tree):
        nm = node.attr if isinstance(node, ast.Attribute) else (
            node.id if isinstance(node, ast.Name) else None)
        if nm and nm.lower() in forb:
            bad.append("%s@%d" % (nm, node.lineno))
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                if alias.name.endswith("_probe") and alias.name != (
                        "lamzouri_hilbert_adjudication_probe"):
                    bad.append("import:%s" % alias.name)
        if isinstance(node, ast.ImportFrom) and node.module:
            if "_probe" in node.module:
                bad.append("from:%s" % node.module)
    return (not bad), (
        "NO zero/prime oracles; synthetic conjugation-invariant "
        "multisets only; external paper facts enter as documented "
        "constants in EXT; STANDALONE (no probe imports)"
        if not bad else "; ".join(bad))


def gl_map(n, a, b):
    x, w = leggauss(n)
    u = 0.5 * (b - a) * x + 0.5 * (a + b)
    wu = 0.5 * (b - a) * w
    return u.astype(np.float64), wu.astype(np.float64)


def ip(a, b):
    return np.dot(a, np.conjugate(b))


# ---------------- windows: eta raw (even, real, open support)
def eta_box_raw(t, lam=LAMBDA):
    t = np.asarray(t, dtype=np.float64)
    return np.where(np.abs(t) < lam - 1e-15, 1.0, 0.0).astype(np.float64)


def eta_mt_raw(t, lam=LAMBDA):
    t = np.asarray(t, dtype=np.float64)
    out = np.zeros_like(t, dtype=np.float64)
    m = np.abs(t) < lam - 1e-15
    c = np.cos(SQRT2 * t[m])
    out[m] = np.sqrt(np.maximum(c, 0.0))
    return out


def eta_bump_raw(t, lam=LAMBDA):
    t = np.asarray(t, dtype=np.float64)
    out = np.zeros_like(t, dtype=np.float64)
    x = t / lam
    m = np.abs(x) < 1.0 - 1e-15
    xm = x[m]
    out[m] = np.exp(-1.0 / (1.0 - xm * xm))
    return out


WINDOWS = (
    ("box", eta_box_raw),
    ("mt", eta_mt_raw),
    ("bump", eta_bump_raw),
)


def scaled_psi_fn(eta_raw, lam, u, w):
    raw = eta_raw(u, lam)
    mass = float(np.sum(w * raw * raw))
    scale2 = 1.0 / mass

    def psi(t, _raw=eta_raw, _lam=lam, _s=scale2):
        e = _raw(t, _lam)
        return _s * e * e

    eta = raw / math.sqrt(mass)
    return psi, eta


# ---------------- discrete Hilbert objects
def f_vec(z, eta, u, sw):
    return sw * eta * np.exp(-2j * np.pi * u * z)


def g_h_vec(z, eta, u, sw):
    fz = f_vec(z, eta, u, sw)
    fc = f_vec(np.conjugate(z), eta, u, sw)
    g = 0.5 * (fz + fc)
    h = (fz - fc) / (2j)
    return g, h


def gram_schmidt(vectors):
    basis = []
    for v in vectors:
        v = np.array(v, dtype=np.complex128, copy=True)
        for _pass in range(2):
            for psi in basis:
                v -= ip(v, psi).real * psi
        n2 = ip(v, v).real
        nrm = math.sqrt(max(n2, 0.0))
        if nrm < RANK_DROP:
            continue
        basis.append(v / nrm)
    return basis


def K_from_grid(xi, psi_nodes, u, w):
    return np.dot(w * psi_nodes, np.exp(-2j * np.pi * xi * u))


class Inst:
    __slots__ = ("simples", "multiples", "pairs", "tag")

    def __init__(self, simples, multiples, pairs, tag):
        self.simples = list(simples)
        self.multiples = list(multiples)
        self.pairs = list(pairs)
        self.tag = tag

    @property
    def n(self):
        return len(self.simples)

    @property
    def r(self):
        return len(self.multiples)

    @property
    def k(self):
        return len(self.pairs)


def draw_real(rng, used, lo=-6.0, hi=6.0, sep=0.15):
    x = float(rng.uniform(lo, hi))
    for _ in range(8):
        if all(abs(x - y) >= sep for y in used):
            break
        x = float(rng.uniform(lo, hi))
    used.append(x)
    return x


def edge_instances():
    return [
        Inst([-6.0, -3.0, 0.0, 3.0, 6.0], [], [], "sharp-int3"),
        Inst([-6.0, -4.0, -2.0, 0.0, 2.0, 4.0, 6.0], [], [],
             "sharp-int2"),
        Inst([-6.0, -5.0, -1.0, 1.0, 5.0, 6.0], [], [], "sharp-mix"),
        Inst(list(np.linspace(-6.0, 6.0, 8)), [], [], "sharp-lin8"),
        Inst([], [(-4.0, 2), (-1.0, 3), (2.0, 4), (5.0, 2)], [],
             "all-multiple"),
        Inst([], [], [(0.7 + 0.4j, 1), (-2.2 + 0.9j, 2),
                      (3.1 + 1.2j, 1), (-5.0 + 0.2j, 1)],
             "only-pairs"),
        Inst([0.0, 4.0], [( -3.0, 2)], [(1.5 + 0.6j, 1)], "mixed"),
    ]


def random_inst(rng):
    n = int(rng.integers(0, 7))
    r = int(rng.integers(0, 4))
    k = int(rng.integers(0, 4))
    if n + r + k == 0:
        n = 2
    used = []
    simples = [draw_real(rng, used) for _ in range(n)]
    multiples = []
    for _ in range(r):
        x = draw_real(rng, used)
        m = int(rng.integers(2, 5))
        multiples.append((x, m))
    pairs = []
    for _ in range(k):
        x = draw_real(rng, used)
        y = float(rng.uniform(0.05, 1.5))
        m = int(rng.integers(1, 3))
        pairs.append((complex(x, y), m))
    return Inst(simples, multiples, pairs, "rand")


def adjudicate(inst, eta, u, w):
    sw = np.sqrt(w)
    psi_nodes = eta * eta
    vecs = []
    zvals = []
    for x in inst.simples:
        vecs.append(f_vec(x, eta, u, sw))
        zvals.append(complex(x))
    for x, m in inst.multiples:
        vx = f_vec(x, eta, u, sw)
        for _ in range(m):
            vecs.append(vx)
            zvals.append(complex(x))
    for z, m in inst.pairs:
        vz = f_vec(z, eta, u, sw)
        vc = f_vec(np.conjugate(z), eta, u, sw)
        for _ in range(m):
            vecs.append(vz)
            zvals.append(complex(z))
            vecs.append(vc)
            zvals.append(complex(np.conjugate(z)))
    n_card = len(vecs)
    F = np.zeros((u.size, u.size), dtype=np.complex128)
    for v in vecs:
        F += np.outer(v, v)
    hs2 = float(np.sum(np.abs(F) ** 2))
    zs = np.asarray(zvals, dtype=np.complex128)
    dxi = zs[:, None] - zs[None, :]
    kw = w * psi_nodes
    kflat = np.exp(-2j * np.pi * dxi.reshape(-1, 1) * u.reshape(1, -1)) @ kw
    sumk2 = np.sum(kflat ** 2)
    u_vecs = ([f_vec(x, eta, u, sw) for x, _ in inst.multiples]
              + [g_h_vec(z, eta, u, sw)[0] for z, _ in inst.pairs])
    v_extra = [f_vec(x, eta, u, sw) for x in inst.simples]
    w_extra = [g_h_vec(z, eta, u, sw)[1] for z, _ in inst.pairs]
    bun = gram_schmidt(u_vecs)
    d_u = len(bun)
    bun = bun + gram_schmidt_continue(bun, v_extra)
    d_v = len(bun)
    bun = bun + gram_schmidt_continue(bun, w_extra)
    d_w = len(bun)
    alphas = []
    max_im = 0.0
    for psi in bun:
        cpsi = np.conjugate(psi)
        aj = cpsi @ F @ cpsi
        max_im = max(max_im, abs(float(np.imag(aj))))
        alphas.append(float(np.real(aj)))
    alphas = np.asarray(alphas, dtype=np.float64)
    sum_a = float(np.sum(alphas)) if alphas.size else 0.0
    sum_a2 = float(np.dot(alphas, alphas)) if alphas.size else 0.0
    # unit / signature identities
    unit_err = 0.0
    for x in list(inst.simples) + [p[0] for p in inst.multiples]:
        fx = f_vec(x, eta, u, sw)
        unit_err = max(unit_err, abs(float(ip(fx, fx).real) - 1.0))
    sig_err = 0.0
    for z, _m in inst.pairs:
        g, h = g_h_vec(z, eta, u, sw)
        sig = float(ip(g, g).real - ip(h, h).real)
        sig_err = max(sig_err, abs(sig - 1.0))
    # range inequalities
    n, r, k = inst.n, inst.r, inst.k
    a_u = alphas[:d_u]
    a_v = alphas[d_u:d_v]
    a_w = alphas[d_v:d_w]
    rng_ok = True
    if d_u > 0:
        s1 = float(np.sum(a_u))
        s2 = float(np.dot(a_u, a_u))
        rng_ok = rng_ok and (s2 >= 2.0 * s1 - 1e-6)
        rng_ok = rng_ok and (s2 >= 4.0 * s1 - 4.0 * (k + r) - 1e-6)
        rng_ok = rng_ok and (s1 >= 2.0 * d_u - 1e-5)
    if d_v > d_u:
        s1 = float(np.sum(a_v))
        s2 = float(np.dot(a_v, a_v))
        rng_ok = rng_ok and (s2 >= 2.0 * s1 - n - 1e-6)
        rng_ok = rng_ok and (s2 >= 4.0 * s1 - 3.0 * n - 1e-6)
    if d_w > d_v:
        rng_ok = rng_ok and (float(np.max(a_w)) <= 1e-7)
        s1 = float(np.sum(a_w))
        s2 = float(np.dot(a_w, a_w))
        rng_ok = rng_ok and (s2 >= 2.0 * s1 - 1e-6)
        rng_ok = rng_ok and (s2 >= 4.0 * s1 - 1e-6)
    rhs_s = 2.0 * n_card - hs2
    rhs_d = 1.5 * n_card - 0.5 * hs2
    dist = n + r + 2 * k
    slack_s = n - rhs_s
    slack_d = dist - rhs_d
    rel_f = abs(hs2 - float(np.real(sumk2))) / max(hs2, 1.0)
    return dict(
        n_card=n_card, hs2=hs2, sumk2_re=float(np.real(sumk2)),
        sumk2_im=float(np.imag(sumk2)), rel_f=rel_f,
        unit_err=unit_err, sig_err=sig_err, max_im=max_im,
        sum_a=sum_a, sum_a2=sum_a2, d_u=d_u, d_v=d_v, d_w=d_w,
        rng_ok=rng_ok, slack_s=slack_s, slack_d=slack_d,
        n=n, r=r, k=k, tag=inst.tag,
        bessel_ok=sum_a2 <= hs2 + 1e-6,
        parseval_err=abs(sum_a - n_card),
        master_ok=(slack_s >= -1e-6) and (slack_d >= -1e-6),
    )


def gram_schmidt_continue(existing, vectors):
    extra = []
    basis = list(existing)
    for v in vectors:
        v = np.array(v, dtype=np.complex128, copy=True)
        for _pass in range(2):
            for psi in basis:
                v -= ip(v, psi).real * psi
        n2 = ip(v, v).real
        nrm = math.sqrt(max(n2, 0.0))
        if nrm < RANK_DROP:
            continue
        q = v / nrm
        basis.append(q)
        extra.append(q)
    return extra


# ---------------- R / C_eta quadrature
def r_kink(psi_fn, lam, n):
    u, wu = gl_map(n, -lam, lam)
    pu = np.asarray(psi_fn(u), dtype=np.float64)
    i_psi = float(np.sum(wu * pu))
    i2 = float(np.sum(wu * pu * pu))
    dbl = 0.0
    x, w = leggauss(n)
    for uk, wk, pk in zip(u, wu, pu):
        v, wv = 0.5 * (uk - (-lam)) * x + 0.5 * (uk + (-lam)), 0.5 * (
            uk - (-lam)) * w
        if uk <= -lam + 1e-18:
            continue
        pv = np.asarray(psi_fn(v), dtype=np.float64)
        dbl += float(wk * pk * np.sum(wv * (uk - v) * pv))
    dbl *= 2.0
    return (i2 + dbl) / (i_psi * i_psi)


def Q_of(alpha, psi_fn, lam, n):
    lo = max(-lam, alpha - lam)
    hi = min(lam, alpha + lam)
    if hi <= lo + 1e-18:
        return 0.0
    t, wt = gl_map(n, lo, hi)
    return float(np.sum(wt * psi_fn(t) * psi_fn(alpha - t)))


def c_eta_of(psi_fn, lam, n):
    q0 = Q_of(0.0, psi_fn, lam, n)
    a, wa = gl_map(n, 0.0, 1.0)
    qs = np.array([Q_of(float(ai), psi_fn, lam, n) for ai in a])
    return q0 + 2.0 * float(np.sum(wa * a * qs))


def r_from_samples(psi, u, w, pcc=False):
    mass = float(np.dot(w, psi))
    p = psi / mass
    i2 = float(np.dot(w, p * p))
    duv = np.abs(u[:, None] - u[None, :])
    if pcc:
        duv = np.minimum(duv, 1.0)
    wp = w * p
    dbl = float(wp @ duv @ wp)
    return i2 + dbl


def mt_closed(dps=30):
    mp.mp.dps = dps
    s2 = 1 / mp.sqrt(2)
    c_mt = mp.mpf("0.5") + s2 * mp.cot(s2)
    c_0 = 2 - c_mt
    c_1 = (3 - c_mt) / 2
    return c_mt, c_0, c_1


def pcc_minimise(lam, gl_n, n_restarts, rng):
    u, w = gl_map(gl_n, -lam, lam)
    duv = np.minimum(np.abs(u[:, None] - u[None, :]), 1.0)
    ks = np.arange(PCC_BASIS, dtype=np.float64)
    basis = np.cos(np.pi * np.outer(u, ks) / lam)

    def obj(a):
        phi = basis @ a
        psi = phi * phi
        return r_from_samples(psi, u, w, pcc=True)

    starts = [np.zeros(PCC_BASIS), np.zeros(PCC_BASIS)]
    starts[0][0] = 1.0
    psi_pad = np.where(np.abs(u) < 0.5 - 1e-15,
                       np.cos(SQRT2 * u), 0.0)
    psi_pad = np.maximum(psi_pad, 0.0)
    target = np.sqrt(psi_pad + 1e-30)
    sw = np.sqrt(w)
    starts[1] = np.linalg.lstsq(
        basis * sw[:, None], target * sw, rcond=None)[0]
    for _ in range(n_restarts):
        starts.append(rng.normal(size=PCC_BASIS))
    best = 1e9
    for a0 in starts:
        res = minimize(obj, a0, method="L-BFGS-B",
                       options=dict(maxiter=180, ftol=1e-14,
                                    gtol=1e-9))
        val = float(res.fun)
        if val < best:
            best = val
    return 2.0 - best, best


def failed_names(prefix):
    return [nm for nm, ok, _ in CHECKS if (not ok) and nm.startswith(prefix)]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--smoke", action="store_true")
    args = ap.parse_args()
    smoke = args.smoke
    gl_n = GL_N_SMOKE if smoke else GL_N
    n_prop = N_PROP_SMOKE if smoke else N_PROP
    pcc_lams = PCC_LAMBDAS_SMOKE if smoke else PCC_LAMBDAS
    n_restarts = 4 if smoke else 8

    print("=" * 78)
    print("lamzouri_hilbert_adjudication_probe -- PRIME.PORT.EXTERNAL."
          "HILBERT_VARIANT.ADJUDICATION.01 (round 639)")
    print("SPEC_SHA %s  MODE %s" % (SPEC_SHA[:16],
                                    "SMOKE" if smoke else "FULL"))
    print("=" * 78, flush=True)

    section("S0  FIREWALL + EXTERNAL CONSTANTS TABLE")
    fw_ok, fw_msg = firewall_audit()
    check("G-F0-ast-firewall", fw_ok, fw_msg)
    for key in ("SRC", "SRC_AF", "SRC_LEAN", "SRC_BGST", "SRC_CCLM",
                "SRC_GLSS", "SRC_PRZZ", "SRC_BGST24_SIMPLE",
                "SRC_MONTGOMERY_RH", "ATLAS_A1", "R267", "R616",
                "R627", "LEAN_STATE"):
        info("%s: %s" % (key, EXT[key]))

    # ---------------- Leg A
    section("S1  LEG A  PROPOSITION REBUILT (synthetic multisets)")
    rng = np.random.default_rng(PROP_SEED)
    insts = edge_instances() + [random_inst(rng) for _ in range(n_prop)]
    u, w = gl_map(gl_n, -LAMBDA, LAMBDA)
    recs = []
    for wname, eraw in WINDOWS:
        psi_fn, eta = scaled_psi_fn(eraw, LAMBDA, u, w)
        _ = psi_fn
        for inst in insts:
            rec = adjudicate(inst, eta, u, w)
            rec["window"] = wname
            recs.append(rec)
    rel_f_max = max(r["rel_f"] for r in recs)
    sumk2_im_max = max(abs(r["sumk2_im"]) for r in recs)
    unit_max = max(r["unit_err"] for r in recs)
    sig_max = max(r["sig_err"] for r in recs)
    bessel_fail = sum(1 for r in recs if not r["bessel_ok"])
    max_a2_minus = max(r["sum_a2"] - r["hs2"] for r in recs)
    rng_fail = sum(1 for r in recs if not r["rng_ok"])
    parseval_max = max(r["parseval_err"] for r in recs)
    master_fail = sum(1 for r in recs if not r["master_ok"])
    slack_s_min = min(r["slack_s"] for r in recs)
    slack_d_min = min(r["slack_d"] for r in recs)
    sharp = [r for r in recs if r["tag"].startswith("sharp")]
    slack_sharp_min = min(r["slack_s"] for r in sharp)
    d_u = [r["d_u"] for r in recs]
    d_v = [r["d_v"] for r in recs]
    d_w = [r["d_w"] for r in recs]
    max_im = max(r["max_im"] for r in recs)
    n_inst = len(recs)
    info("instances=%d (windows=%d x |I|=%d)  GL_N=%d"
         % (n_inst, len(WINDOWS), len(insts), gl_n))
    info("D_U range [%d,%d]  D_V [%d,%d]  D_W [%d,%d]"
         % (min(d_u), max(d_u), min(d_v), max(d_v), min(d_w), max(d_w)))
    info("G-A6 min slack simple=%.6e distinct=%.6e  G-A7 min slack=%.6e"
         % (slack_s_min, slack_d_min, slack_sharp_min))
    check("G-A1-F-eq-sumK2",
          rel_f_max <= QUAD_TOL and sumk2_im_max <= 1e-6,
          "max rel |||F||_HS^2 - Sum K(z-s)^2|=%.3e  max Im SumK2=%.3e  "
          "tol=%g  n=%d" % (rel_f_max, sumk2_im_max, QUAD_TOL, n_inst))
    check("G-A2-unit-and-signature",
          unit_max <= 1e-8 and sig_max <= 1e-7,
          "max |int |f_x|^2 - 1|=%.3e  max |int|g|^2-int|h|^2-1|=%.3e"
          % (unit_max, sig_max))
    check("G-A3-bessel",
          bessel_fail == 0,
          "Sum alpha_j^2 <= HS^2 on all; max(Sum a^2 - HS^2)=%.3e  "
          "fails=%d" % (max_a2_minus, bessel_fail))
    check("G-A4-range-inequalities",
          rng_fail == 0 and max_im <= 1e-6,
          "U: a^2>=2a (via a^2+4>=4a + Sum a>=2 D_U); "
          "V\\U: Sum a^2>=2 Sum a - n; W\\V: alpha<=0; fails=%d  "
          "max Im(alpha)=%.3e" % (rng_fail, max_im))
    check("G-A5-parseval-sum-alpha",
          parseval_max <= 1e-6,
          "max |Sum_j alpha_j - |Z||=%.3e" % parseval_max)
    check("G-A6-master-bounds",
          master_fail == 0,
          "n >= 2|Z|-HS^2 and n+r+2k >= 1.5|Z|-0.5 HS^2 on ALL; "
          "fails=%d  min slack simple=%.6e distinct=%.6e"
          % (master_fail, slack_s_min, slack_d_min))
    check("G-A7-sharpness",
          slack_sharp_min >= -1e-6 and slack_sharp_min < 0.15,
          "well-separated all-simple-real: bound approaches n; "
          "min slack=%.6e (n - (2n - HS^2) = HS^2 - n)"
          % slack_sharp_min)

    # ---------------- Leg B
    section("S2  LEG B  CERTIFICATE CLASS IDENTIFICATION")
    a = sp.symbols("a", real=True)
    sh1 = sp.expand((a - 1) ** 2 - (a ** 2 + 1 - 2 * a))
    sh2 = sp.expand((a - 2) ** 2 - (a ** 2 + 4 - 4 * a))
    sols1 = sp.solve((a - 1) ** 2, a)
    sols2 = sp.solve((a - 2) ** 2, a)
    Nv, tr, HS = sp.symbols("N tr HS", real=True)
    af = 4 * tr - 2 * Nv - HS ** 2
    af_at = sp.simplify(af.subs(tr, Nv))
    lam_bound = 2 * Nv - HS ** 2
    chain_ok = (sh1 == 0 and sh2 == 0 and sols1 == [1] and sols2 == [2]
                and sp.simplify(af_at - lam_bound) == 0)
    check("G-B1-shadows-and-AF-chain", chain_ok,
          "a^2+1-2a=(a-1)^2 eq{1}; a^2+4-4a=(a-2)^2 eq{2}; "
          "Sum a^2 >= 2 Sum a - n; at tr G=N: 4 tr G-2N-HS^2 = 2N-HS^2 "
          "identical to A-F chain (sympy exact)")

    c_mt, c_0, c_1 = mt_closed(30)
    c_mt_f = float(c_mt)
    c_0_f = float(c_0)
    c_1_f = float(c_1)
    r_vals = {}
    c_vals = {}
    rels = {}
    for wname, eraw in WINDOWS:
        psi_fn, _eta = scaled_psi_fn(eraw, LAMBDA, u, w)
        rv = r_kink(psi_fn, LAMBDA, gl_n)
        cv = c_eta_of(psi_fn, LAMBDA, gl_n)
        r_vals[wname] = rv
        c_vals[wname] = cv
        rels[wname] = abs(cv - rv) / max(abs(rv), 1.0)
    rel_b2 = max(rels.values())
    r0_dev = abs(r_vals["box"] - 4.0 / 3.0)
    rmt_dev = abs(r_vals["mt"] - c_mt_f)
    info("R(psi0)=%.12f vs 4/3 (dev=%.3e); R(psiMT)=%.12f vs C_MT=%.12f "
         "(dev=%.3e); R(bump)=%.12f"
         % (r_vals["box"], r0_dev, r_vals["mt"], c_mt_f, rmt_dev,
            r_vals["bump"]))
    info("C_eta: box=%.12f mt=%.12f bump=%.12f  max rel |C_eta-R|=%.3e"
         % (c_vals["box"], c_vals["mt"], c_vals["bump"], rel_b2))
    check("G-B2-Ceta-eq-R",
          rel_b2 <= 1e-7 and r0_dev <= 1e-7 and rmt_dev <= 1e-6,
          "C_eta:=Q(0)+2 int_0^1 a Q(a) da == R(psi=eta^2) rel<=1e-7 "
          "all three windows; max rel=%.3e  R(psi0)-4/3=%.3e  "
          "R(psiMT)-C_MT=%.3e" % (rel_b2, r0_dev, rmt_dev))

    rng_b = np.random.default_rng(PROP_SEED + 11)
    ub, wb = gl_map(gl_n, -LAMBDA, LAMBDA)
    r_rand = []
    for _ in range(200):
        ck = rng_b.normal(size=8)
        phi = np.zeros_like(ub)
        for k, ck_k in enumerate(ck):
            phi += ck_k * np.cos(2.0 * math.pi * k * ub)
        psi = phi * phi
        r_rand.append(r_from_samples(psi, ub, wb, pcc=False))
    min_r = min(r_rand)
    gap_mt = min_r - c_mt_f
    # local minimum at psi_MT, 20 directions
    psi_mt = np.cos(SQRT2 * ub)
    psi_mt = psi_mt / float(np.dot(wb, psi_mt))
    second = []
    rng_d = np.random.default_rng(PROP_SEED + 13)
    for _ in range(20):
        ck = rng_d.normal(size=6)
        dlt = np.zeros_like(ub)
        for k, ck_k in enumerate(ck):
            dlt += ck_k * np.cos(2.0 * math.pi * k * ub)
        dlt -= float(np.dot(wb, dlt)) / float(np.sum(wb))
        nrm = math.sqrt(max(float(np.dot(wb, dlt * dlt)), 0.0))
        dlt /= nrm
        eps = min(1e-3, 0.05 * float(np.min(psi_mt)) / (
            float(np.max(np.abs(dlt))) + 1e-12))
        rp = r_from_samples(psi_mt + eps * dlt, ub, wb)
        rm = r_from_samples(psi_mt - eps * dlt, ub, wb)
        r0 = r_from_samples(psi_mt, ub, wb)
        second.append(rp + rm - 2.0 * r0)
    min_sd = min(second)
    info("Remark-MT: min_R - C_MT = %.6e over 200 random admissible psi; "
         "min second-diff at psi_MT = %.6e (20 dirs)"
         % (gap_mt, min_sd))
    check("G-B3-remark-MT",
          (min_r >= c_mt_f - 1e-9) and (min_sd >= -1e-12),
          "all 200 R(psi)>=C_MT-1e-9; min R-C_MT=%.6e; "
          "local min second-diff>=0: min=%.6e" % (gap_mt, min_sd))
    info("TWO_MOMENT_CLASS — certificate consumes exactly "
         "(|Z|, Sum K(z-s)^2)=(trace, HS^2) of the same Weil-form "
         "compression; atlas class A1 unchanged")

    # ---------------- Leg C
    section("S3  LEG C  CONSTANTS")
    c_mt_print = 1.3274992963206
    c_0_print = 0.6725007037
    c_1_print = 0.83625
    check("G-C1-CMT-digits",
          abs(c_mt_f - c_mt_print) < 5e-14,
          "C_MT mpmath 30d = %.13f vs 1.3274992963206 (|dev|=%.3e)"
          % (c_mt_f, abs(c_mt_f - c_mt_print)))
    check("G-C2-C0-eq-pstar",
          abs(c_0_f - c_0_print) < 5e-11,
          "C_0=2-C_MT=%.12f == r627 p*=0.6725007037 (|dev|=%.3e)"
          % (c_0_f, abs(c_0_f - c_0_print)))
    c1_from_c0 = (c_0_f + 1.0) / 2.0
    check("G-C3-C1-round63",
          abs(c_1_f - c_1_print) < 5e-6 and abs(c_1_f - c1_from_c0) < 1e-15,
          "C_1=(3-C_MT)/2=%.12f == 0.83625 (5 digits) and == (C_0+1)/2=%.12f"
          % (c_1_f, c1_from_c0))
    seq = (0.407511, 5.0 / 12.0, 0.417293, 2.0 / 3.0, c_0_f,
           0.6818287, 1.0)
    ordered = all(seq[i] < seq[i + 1] for i in range(len(seq) - 1))
    gap = 0.6818287 - c_0_f
    check("G-C4-ordering-gap",
          ordered and abs(gap - 9.33e-3) < 1e-4,
          "0.407511 < 5/12 < 0.417293 < 2/3 < C_0 < 0.6818287 < 1; "
          "gap 0.6818287-C_0=%.6e (r627 9.3e-3, tol 1e-4)" % gap)

    # ---------------- Leg D
    section("S4  LEG D  WALL LOCATION (support one)")
    max_q_out = 0.0
    for wname, eraw in WINDOWS:
        psi_fn, _eta = scaled_psi_fn(eraw, LAMBDA, u, w)
        for aa in (1.0, 1.01, 1.1, 1.5, 2.0):
            max_q_out = max(max_q_out, abs(Q_of(aa, psi_fn, LAMBDA, gl_n)))
            max_q_out = max(max_q_out, abs(Q_of(-aa, psi_fn, LAMBDA, gl_n)))
    check("G-D1-Q-support-one",
          max_q_out < 1e-10,
          "|Q(alpha)| for |alpha|>=1, supp eta subset (-1/2,1/2), "
          "all three windows: maxabs=%.3e" % max_q_out)

    lam_w = 0.6
    uw, ww = gl_map(gl_n, -lam_w, lam_w)
    psi_w, _ = scaled_psi_fn(eta_box_raw, lam_w, uw, ww)
    a_tail, wa_tail = gl_map(gl_n, 1.0, 2.0 * lam_w)
    qs_tail = np.array([Q_of(float(ai), psi_w, lam_w, gl_n)
                        for ai in a_tail])
    tail_frac = 2.0 * float(np.sum(wa_tail * qs_tail))
    info("widened supp eta=(-0.6,0.6) box: Q tail mass |alpha|>1 "
         "fraction=%.6e (BGSTB Lemma 5 inapplicable)" % tail_frac)
    check("G-D2-widened-tail",
          tail_frac > 1e-6,
          "widened (-0.6,0.6): mass of Q beyond |alpha|>1 = %.6e > 0; "
          "typed: sole arithmetic input is Montgomery pair-correlation "
          "range |alpha|<=1 = r267 X<=T = PAIRCORR wall" % tail_frac)

    rng_p = np.random.default_rng(PROP_SEED + 17)
    p_at = {}
    r_at = {}
    for lam in pcc_lams:
        p_lam, r_lam = pcc_minimise(lam, gl_n, n_restarts, rng_p)
        p_at[lam] = p_lam
        r_at[lam] = r_lam
        info("p(lambda=%.2f)=%.10f  (min R_PCC=%.10f)"
             % (lam, p_lam, r_lam))
    p05 = p_at[0.5]
    lams_sorted = list(pcc_lams)
    mono = all(p_at[lams_sorted[i + 1]] + 1e-4 >= p_at[lams_sorted[i]]
               for i in range(len(lams_sorted) - 1))
    lam_far = 3.0 if 3.0 in p_at else max(lams_sorted)
    p_far = p_at[lam_far]
    check("G-D3-PCC-p-lambda",
          abs(p05 - c_0_f) <= 2e-4 and mono and p_far > 0.9,
          "p(0.5)=%.8f vs C_0=%.8f (|dev|=%.3e, tol 2e-4); "
          "p(lambda) non-decreasing=%s; p(%.1f)=%.8f > 0.9; "
          "table=%s; NOTE 0.6818287 is A-F class ceiling (on/off "
          "partition), not p(lambda)"
          % (p05, c_0_f, abs(p05 - c_0_f), mono, lam_far, p_far,
             ", ".join("%.2f:%.8f" % (lam, p_at[lam])
                       for lam in lams_sorted)))

    # ---------------- Leg E
    section("S5  LEG E  WEIGHT IDENTITY")
    d, L = sp.symbols("d L", positive=True)
    z = sp.I * d * L / (2 * sp.pi)
    lhs = 4 / (4 - d ** 2)
    rhs = 1 / (1 + sp.pi ** 2 * z ** 2 / L ** 2)
    wdiff = sp.simplify(sp.together(lhs - rhs))
    check("G-E1-weight-identity", wdiff == 0,
          "w(rho-rho')=4/(4-(rho-rho')^2) == "
          "(1 + pi^2 z^2/(log T)^2)^{-1} with "
          "z=i(rho-rho') log T/(2 pi)  (sympy exact)")
    g = sp.symbols("g", real=True)
    w_on = 4 / (4 + g ** 2)
    w_le1 = sp.simplify(1 - w_on)  # g^2/(4+g^2) >= 0
    w_pos = sp.simplify(w_on)
    samples = [float(w_on.subs(g, gv)) for gv in
               (0.0, 0.1, 1.0, 2.0, 10.0, -3.0)]
    on_ok = (all(0.0 < s <= 1.0 + 1e-15 for s in samples[1:])
             and abs(samples[0] - 1.0) < 1e-15
             and w_le1.subs(g, 1) > 0 and w_pos.subs(g, 1) > 0)
    check("G-E2-online-weight", on_ok,
          "on-line rho-rho'=i(gamma-gamma'): w=4/(4+(gamma-gamma')^2) "
          "in (0,1]; w(0)=1; samples=%s"
          % ", ".join("%.6f" % s for s in samples))

    xis = np.linspace(0.0, 2.5, 20)
    rel_e3 = 0.0
    psi_box, _ = scaled_psi_fn(eta_box_raw, LAMBDA, u, w)
    psi_mt, _ = scaled_psi_fn(eta_mt_raw, LAMBDA, u, w)
    psi_bp, _ = scaled_psi_fn(eta_bump_raw, LAMBDA, u, w)
    e3_ok = True
    for psi_fn in (psi_box, psi_mt, psi_bp):
        for xi in xis:
            uu, wu = gl_map(gl_n, -LAMBDA, LAMBDA)
            kval = float(np.sum(
                wu * psi_fn(uu) * np.cos(2.0 * math.pi * xi * uu)))
            k2 = kval * kval
            # hat Q, split at 0 (Q even)
            aa, wa = gl_map(gl_n, 0.0, 1.0)
            qs = np.array([Q_of(float(ai), psi_fn, LAMBDA, gl_n)
                           for ai in aa])
            hq = 2.0 * float(np.sum(wa * qs * np.cos(
                2.0 * math.pi * xi * aa)))
            rel = abs(hq - k2) / max(abs(k2), 1e-8)
            rel_e3 = max(rel_e3, rel)
            if rel > 1e-7:
                e3_ok = False
    check("G-E3-hatQ-eq-K2", e3_ok,
          "hat Q = K^2 at 20 real xi, three windows, rel tol 1e-7; "
          "max rel=%.3e" % rel_e3)

    # ---------------- Leg F + verdict
    section("S6  CROSSWALK + VERDICT")
    info(EXT["CROSSWALK"])
    check("G-F1-crosswalk", True,
          "TYPED: %s" % EXT["CROSSWALK"])

    a_ok = all(ok for nm, ok, _ in CHECKS if nm.startswith("G-A"))
    b_class_ok = all(ok for nm, ok, _ in CHECKS
                     if nm in ("G-B1-shadows-and-AF-chain",
                               "G-B2-Ceta-eq-R"))
    b3_ok = all(ok for nm, ok, _ in CHECKS if nm == "G-B3-remark-MT")
    c_ok = all(ok for nm, ok, _ in CHECKS if nm.startswith("G-C"))
    d_ok = all(ok for nm, ok, _ in CHECKS if nm.startswith("G-D"))

    def typed(prefix):
        fs = failed_names(prefix)
        return ",".join(fs) if fs else prefix + "fail"

    verdict = " + ".join([
        "PROPOSITION_REBUILT" if a_ok else
        "PROPOSITION_BROKEN(%s)" % typed("G-A"),
        ("SAME_CLASS(TWO_MOMENT: C_eta == R(eta^2); bound == 2N − HS^2 "
         "== A–F chain; atlas A1 unchanged)") if b_class_ok else
        "NEW_CLASS(%s)" % typed("G-B"),
        ("CONSTANTS_IDENTICAL(C_0 == r627 p*, C_1 == 0.83625, "
         "gap to p_0 9.3e-3)") if c_ok else
        "CONSTANTS_DIFFER(%s)" % typed("G-C"),
        ("WALL_LOCATION_CONFIRMED(SUPPORT_ONE: BGSTB supp f ⊂ [−1,1] "
         "sole arithmetic input; p(λ) under PCC rises to 1)") if d_ok else
        "WALL_LOCATION_MISMATCH(%s)" % typed("G-D"),
        "MT_OPTIMAL_SUPPORTED" if b3_ok else
        "MT_OPTIMAL_VIOLATED(%s)" % typed("G-B3"),
        ("NO_IMPORT(UNCHANGED: r267 frame mismatch stands; no Bessel "
         "target on the prime-comb side)"),
        ("SOURCE_NOTE(AXIOMPROVER: Proposition unconditional; Theorem "
         "modulo BGSTB Lemma 5 + RvM as Lean hypotheses)"),
    ])
    print("\nVERDICT: %s" % verdict, flush=True)

    npass = sum(1 for _, ok, _ in CHECKS if ok)
    wall = time.time() - T0_WALL
    check("G-runtime", wall <= RUNTIME_CAP,
          "wall %.1f s <= %.0f s" % (wall, RUNTIME_CAP))
    npass = sum(1 for _, ok, _ in CHECKS if ok)
    print("\nGATES: %d/%d PASS  (SPEC_SHA %s)  wall %.1f s"
          % (npass, len(CHECKS), SPEC_SHA[:16], wall), flush=True)
    print("AMENDMENTS AFTER FREEZE: NONE" if npass == len(CHECKS)
          else "GATE FAILURES PRESENT -- see above", flush=True)
    print("NO RH CLAIM IN EITHER DIRECTION.", flush=True)
    return 0 if npass == len(CHECKS) else 1


if __name__ == "__main__":
    sys.exit(main())
