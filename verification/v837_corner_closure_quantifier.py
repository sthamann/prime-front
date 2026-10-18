#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""v837 -- PRIME.CORNER.OPENDOORS.01 + PRIME.CORNER.LEVEL2.01: the corner-closure quantifier -- the two open doors of the character-corner channel class close by opposite mechanisms, and the closure quantifier extends level-exactly through the Hjelmslev tower to m <= 3: position data has NO corner-compatible channel into the register group algebra, at any level, ONE module from two probes plus the kernel-checked Lean mirror (19/19 + 17/17 + 3 mirror checks, verdicts DOORS-CLOSED and LEVEL2-CLOSED; discovery probes hjelmslev_open_doors_probe.py and hjelmslev_level2_corner_probe.py, 2026-08-07, re-run identically at promotion, promoted VERBATIM with no downscoping, ~8 s; Lean core TfptCarrier/SectorPositiveDescent.lean, lake build green, kernel axioms clean).  PART A, THE TWO DOORS (the class map): DOOR 1 (lag-factor dressings) -- the GL1 corner does NOT trace out the factor: it reads the full (t1, t2) COMPRESSION, so factor dressings are generically visible AND placement-sensitive -- but the deployed-form identity pins the compressed reads to the spline reads X_j, so EVERY visible dressing breaks the identity by exactly its action on span(t1, t2) (mass multiplier defect 1.215e-01, unital phase 5.849e-02; typed mutually exclusive), and the identity-preserving factor dressings are EXACTLY the corner-invisible ones (12 commutant draws at 2.7e-14; sweep dichotomy on all 24 draws: defect <= bar <=> corner unmoved) -- Door 1 CLOSED: visibility <=> identity defect.  DOOR 2 (characters nontrivial on V) -- the product law chat(chi) = (-1)^eps Vfac(w) Mfac(j; n) verified against the full 128-dim carrier Fourier for ALL 128 characters x ALL 136 events (exact Fractions): the 128 characters COLLAPSE to 18 classes; the mass ward GENERALIZED: the chi-corner reads exactly ONE V-mode and ONE mu4-mode of the carrier per event -- every coefficient is a functional of the mass index n, NEVER of the position u_j (position-blind; scrambling positions leaves every chat_j(chi) bit-identical).  THE COMPLETE CLASS MAP (90 cells = 18 character classes x 5 dressing columns): identity ==> NOT visible in EVERY cell; the identity cells are exactly the pinning classes (the undressed GL1 corner, the polar-mode duplicate (eps=1, w=w0, j=0), the unital register dressing at GL1); cells with identity AND visibility AND placement: NONE -- the class is complete and empty.  PART B, THE TOWER LEVELS (the quantifier extends): rings R_m = Z[i]/(1+i)^m for m = 1..3 with complete duals (16/256/4096 characters); polar supports |S_m| = 7*8^(m-1) generating the full polar submodule 2^(3m); the exact Vfac spectra read ONLY {1, 0, -1/7} at every level -- the identity characters are EXACTLY Ann(<S_m>) with count 2^m (every one reproducing the GL1 block bit for bit), and EVERY jet-new character refines POSITION-BLIND data only (the level-2 mass ward: the level-m corner reads one phi-mode of the carrier per event, factorization to 1e-12); the class map at m = 2, 3 (18 columns x 3 dressing rows each) carries the same census {identity column: 1, visible-broken: 17} -- cells with all three: NONE at any level.  THE CLOSURE STATEMENT (measured, the round's structural deliverable): the corner program on C[C2 x F2^4 x Z4] and its Hjelmslev tower is CLOSED as an identification device -- the register side is INFORMATION-STARVED (position-blind carrier modes), the factor side is INFORMATION-RICH but PINNED (the identity freezes the one position-reading slot); an identification carrier would need a POSITION-DEPENDENT carrier map or a corner OUTSIDE this group algebra -- the wall stays EXACTLY PRIME.FLOOR.PAIRCORR.01, with the corner route's perimeter fully surveyed and typed; stop-list entries PRIME.CORNER.OPENDOORS.01 / PRIME.CORNER.LEVEL2.01.  PART C, THE LEAN MIRROR: the structural half of the closure is kernel-checked in TfptCarrier/SectorPositiveDescent.lean (no sorry, no native_decide; imported in TfptCarrier.lean, carried in the shipped Lean manifest): corner compression by a hermitian idempotent is linear/idempotent/CP with the corner-trace split (corner_posSemidef, corner_trace_le), descent towers with the measured-zero compatibility defect transport compatible positive families (DescentTower, tower_proj_descent, cornerFamily_*), entrywise limits of corner states are PSD (corner_limit_posSemidef via GramCompactness), and the final theorem sector_floor passes IdentificationPositivity through as the SINGLE NAMED HYPOTHESIS -- the kernel-checked logical geography of exactly this module's finding: structural positivity proven, the identification datum deliberately NOT a theorem; the three checks here are the numeric witness mirror (v817 precedent).  NO RH claim.  Python-only per GATE.WOLFRAM.02.

PROVENANCE: discovery probes hjelmslev_open_doors_probe.py (19/19,
verdict DOORS-CLOSED) and hjelmslev_level2_corner_probe.py (17/17,
verdict LEVEL2-CLOSED), both 2026-08-07, re-run identically at
promotion; this module runs both frozen protocols VERBATIM (~8 s;
each part resets the frozen LCG seed 20260807; a module-level
_VERDICTS capture inserted at the frozen verdict per the v817/v791
precedent -- no gate, bar or table changed).  PART C is the
promotion-time numeric witness mirror of
experiments/lean4-carrier-rigidity/TfptCarrier/SectorPositiveDescent.lean
(lake build green at promotion, 3409 jobs, no sorry / native_decide;
import wired in TfptCarrier.lean; lean_manifest.sha256 regenerated
with this round) -- the kernel-checked statements are cited, not
re-proved (positive_descent_master v817 precedent).  The original
probe docstrings, frozen specs (SHA-256-printed) and decision trees
live in the probe files verbatim (experiments/tfpt-discovery/).

FIREWALL: v563 / v738 READ-ONLY; no zeta zero, no prime-table symbol
(AST-checked; own sieves only); RNG only in the declared v563
scramble recipe (seed 1) and the fixed LCG (seed 20260807).
NO RH claim.
"""
import ast
import hashlib
import math
import os
import sys
import time
from fractions import Fraction as Fr
from itertools import combinations, product

import numpy as np

_here = os.path.dirname(os.path.abspath(__file__))
if _here not in sys.path:
    sys.path.insert(0, _here)

import v563_paper2_readouts as core        # noqa: E402  (READ-ONLY)
import v738_hecke_mod_ramified as ram      # noqa: E402  (READ-ONLY)

_VERDICTS = {}

# ------------------- shared layer (identical in both frozen probes; emitted once)

N_TH = 640

N_WIN = 3

KAPPA = 0.25

BAR_COEF_REL = 1.0e-9

BAR_ID_REL = 1.0e-6

BAR_MOVE = 1.0e-9

BAR_EXACT = 1.0e-12

SCR_SEED = 1

REG_BAR = 1.0e-4

BANNED_IDS = ("zetazero", "nzeros", "primerange", "isprime", "primepi",
              "nextprime", "prevprime")

CHECKS = []

FAILS = []

CONTROL = {}

T0 = time.time()

_LCG = [20260807]

def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok)))
    if not ok:
        FAILS.append(name.split()[0])
    print("  [%s] %s%s" % ("PASS" if ok else "FAIL", name,
                           ("  -- " + detail) if detail else ""), flush=True)
    return bool(ok)

def section(title):
    print("\n" + "=" * 74)
    print(title)
    print("=" * 74, flush=True)

def ast_firewall():
    src = open(os.path.abspath(__file__), encoding="utf-8").read()
    bad = []
    for node in ast.walk(ast.parse(src)):
        name = None
        if isinstance(node, ast.Name):
            name = node.id
        elif isinstance(node, ast.Attribute):
            name = node.attr
        if name and name.lower() in BANNED_IDS:
            bad.append(name)
    return bad

def sparse_theta_terms(kind, cap):
    out = []
    if kind in ("th3", "th4"):
        out.append((0, 1))
        n = 1
        while n * n <= cap:
            out.append((n * n, 2 if kind == "th3" else 2 * ((-1) ** n)))
            n += 1
    else:
        o = 1
        while o * o <= cap:
            out.append((o * o, 2))
            o += 2
    return out

def sparse_mul(dense, terms):
    out = np.zeros_like(dense)
    for e, c in terms:
        if e == 0:
            out += c * dense
        else:
            out[e:] += c * dense[:-e]
    return out

def theta_layer():
    sig3 = np.zeros(N_TH + 1, dtype=np.int64)
    for d in range(1, N_TH + 1):
        sig3[d::d] += d ** 3
    spf = np.zeros(N_TH + 1, dtype=np.int64)
    for p in range(2, N_TH + 1):
        if spf[p] == 0:
            spf[p::p] = np.where(spf[p::p] == 0, p, spf[p::p])
    SCAP = 2 * N_TH
    t3 = sparse_theta_terms("th3", SCAP)
    t4 = sparse_theta_terms("th4", SCAP)
    one = np.zeros(SCAP + 1, dtype=np.int64)
    one[0] = 1
    p3 = one
    p4 = one
    for _ in range(8):
        p3 = sparse_mul(p3, t3)
        p4 = sparse_mul(p4, t4)
    m53 = one
    for _ in range(5):
        m53 = sparse_mul(m53, t3)
    for _ in range(3):
        m53 = sparse_mul(m53, t4)
    m35 = one
    for _ in range(5):
        m35 = sparse_mul(m35, t4)
    for _ in range(3):
        m35 = sparse_mul(m35, t3)
    Th0 = ((p3 + m53 + m35 + p4) // 4)[::2][:N_TH + 1].copy()
    Th2 = ((p3 - m53 - m35 + p4) // 4)[::2][:N_TH + 1].copy()
    TCAP = 8 * N_TH
    t2 = sparse_theta_terms("th2", TCAP)
    acc = np.zeros(TCAP + 1, dtype=np.int64)
    acc[0] = 1
    for _ in range(8):
        acc = sparse_mul(acc, t2)
    Th1 = (acc[::8][:N_TH + 1] // 4).copy()
    tk = np.zeros(N_TH + 1, dtype=np.int64)
    for d in range(2, N_TH + 1, 2):
        tk[d::d] += d * (4 + (4 if d % 4 == 0 else 0))
    g = np.zeros(N_TH, dtype=np.int64)
    g[0] = 1
    for n in range(1, N_TH):
        s = int(np.dot(tk[1:n + 1], g[n - 1::-1]))
        q, r = divmod(-s, n)
        assert r == 0
        g[n] = q
    a_f8 = np.zeros(N_TH + 1, dtype=np.int64)
    a_f8[1:] = g
    glue_ok = bool(np.all((Th0 + 2 * Th1 + Th2)[1:] == 240 * sig3[1:]))
    heads_ok = ((Th0[1], Th1[1], Th2[1]) == (52, 64, 60)
                and (a_f8[3], a_f8[5], a_f8[7]) == (-4, -2, 24))
    return dict(sig3=sig3, Th=(Th0, Th1, Th2, Th1), a=a_f8, spf=spf,
                ok=glue_ok and heads_ok)

def classify(n, spf):
    p = int(spf[n])
    m, k = n, 0
    while m % p == 0:
        m //= p
        k += 1
    if p == 2:
        return "ro" if k % 2 == 1 else "re"
    return "sp" if p % 4 == 1 else "in"

def label_frame():
    L = ram.Lmodule()
    E4 = [tuple((1 if j == k else 0, 0) for j in range(4))
          for k in range(4)]
    S = [L.coords(ram.pack(ram.sig8(ram.unpack(L.to_ambient(E4[k])))))
         for k in range(4)]
    S2 = [[ram.par(S[k][j]) for j in range(4)] for k in range(4)]

    def sigbar(v):
        return tuple((sum(v[k] * S2[k][j] for k in range(4))) & 1
                     for j in range(4))

    labels = [tuple((z >> b) & 1 for b in range(4)) for z in range(16)]
    pairs = list(combinations(range(4), 2))
    Omega = None
    for mask in range(1, 1 << 6):
        M = [[0] * 4 for _ in range(4)]
        for bi, (i, j) in enumerate(pairs):
            if (mask >> bi) & 1:
                M[i][j] = M[j][i] = 1
        cols = [tuple(M[i][j] for i in range(4)) for j in range(4)]
        rk, _k, _i = ram.f2_rank_ker_inv(cols)
        if rk != 4:
            continue
        inv_ok = all(
            (sum(sigbar(v)[k] * M[k][l] * sigbar(w)[l]
                 for k in range(4) for l in range(4))) & 1
            == (sum(v[k] * M[k][l] * w[l]
                    for k in range(4) for l in range(4))) & 1
            for v in labels for w in labels)
        if inv_ok:
            Omega = M
            break
    cols_o = [tuple(Omega[i][j] for i in range(4)) for j in range(4)]
    _rk, _ker, inv_o = ram.f2_rank_ker_inv(cols_o)
    a_par = tuple(ram.unpack(L.to_ambient(E4[k]))[0] % 2
                  for k in range(4))
    y_chi = ram.f2_matvec(inv_o, a_par)
    Hstar = [v for v in labels if any(v)
             and (sum(v[k] * Omega[k][l] * y_chi[l]
                      for k in range(4) for l in range(4))) & 1 == 0]
    return Omega, y_chi, Hstar

def label_int(v):
    return sum(v[i] << i for i in range(4))

def deployed_windows():
    rows = []
    for kz in core.frame_a_zones():
        rr = core.build_window(kz)
        if rr["h"] == 1292:
            continue
        if math.exp(2.0 * rr["alpha"]) > core.ATOM_MAX + 0.5:
            continue
        rows.append((rr["alpha"], kz, rr))
    rows.sort(key=lambda t: t[0])
    return [(kz, rr) for _a, kz, rr in rows[:N_WIN]]

def unit_rows(rr, positions=None):
    uu = rr["uu"] if positions is None else positions
    out = np.zeros((len(uu), 2 * rr["h"]))
    for j, u in enumerate(uu):
        out[j] = core.atom_lags_at(rr["alpha"], rr["M"], [float(u)],
                                   [2.0])[0]
    return out


# =============== PART A -- hjelmslev_open_doors_probe.py (frozen probe, verbatim)

FROZEN_SPEC_a = """\
PRIME.CORNER.OPENDOORS.01 spec v1 (2026-08-07, frozen before the run).
DOOR 1: cheap check = trace-out test on the GL1 corner functional
(traceless factor operator with nonzero corner read ==> compression,
not trace); variants D1a (tent-read mass multiplier, diag(1 + fhat/4),
fhat = normalized -sum_j lam_j diag(R_j)) and D1b (lag-phase unitary,
diag(exp(i pi ghat/4)), g_i = sum_j lam_j sin((i+1) pi u_j / 2 alpha),
normalized); gates (a) single-Kraus Choi entrywise on the 2x2 leading
reduction + D1a min entry > 0 + D1b unitarity <= 1e-12, (b) defect
coeffs (const + per-w_j) <= 1e-9 scale else typed, (c) |delta| > 1e-9
AND |delta - delta_scr| > 1e-9 AND |delta - delta_eps| > 1e-9, fields
rebuilt per position set; controls: D_perp = 1 + P_perp F P_perp / 4
(identity + invisible), sweep 12 generic + 12 perp draws (LCG
20260807): defect <= bar <=> block unmoved.  DOOR 2: all 128
characters verified EXACTLY against the product law chat = (-1)^eps *
Vfac(w) * Mfac(j; n) (full carrier Fourier, Fractions, all union
events); collapse to 18 classes (Vfac in {1, -1/7} via the H* mode,
w0 = the unique nonzero w with w.H* = 0); per class rep: e_chi ward
(idempotent + self-adjoint + Fourier delta, exact complex Fractions),
chat spectrum (zeros = non-surviving events), identity <=> chat = -1
all j (measured), the generalized mass ward (register-dressed chat'
= (-1)^eps Fw(p') Mfac on the full 128-dim register, <= 1e-12), and
placement of delta_chi.  MAP: 5 dressing rows x 18 character columns,
cells (I, V, P); I = max defect <= 1e-9 scale, V = max|block -
GL1-undressed block| > 1e-9 scale, P = excess moves under scramble
seed 1 AND Epstein (first ka sums of two squares).  VERDICTS:
DOORS-CARRY / DOORS-CLOSED / DOORS-PARTIAL (typed per door).
Controls: GL1 chat = -1 exact; corner reduction reproduces tau_X on
3 windows (<= 1e-6 rel of block scale); tradeoff regression (A'
identity + |delta| <= 1e-9; C defect > 0 + placement).  KAPPA = 1/4.
NO RH claim; writes nothing.
"""

N_SWEEP_GEN = 12

N_SWEEP_PERP = 12

REG_REFS_a = {9: (4.813726e-3, 5.984165e-4),
            12: (3.227697e-3, 4.351189e-4),
            13: (2.954471e-3, 5.637632e-4)}

def lcg_float():
    _LCG[0] = (1103515245 * _LCG[0] + 12345) % (1 << 31)
    return _LCG[0] / float(1 << 31)

G_ELEMS = [(a, v, m) for a in range(2) for v in range(16) for m in range(4)]

def g_mul(g, h):
    return ((g[0] + h[0]) % 2, g[1] ^ h[1], (g[2] + h[2]) % 4)

def g_inv(g):
    return (g[0], g[1], (-g[2]) % 4)

def chival(chi, g):
    """Exact character value as (re, im) integer pair."""
    eps, w, j = chi
    a, v, m = g
    s = (-1) ** (eps * a) * (-1) ** (bin(w & v).count("1"))
    q = (j * m) % 4
    if q == 0:
        return (s, 0)
    if q == 1:
        return (0, s)
    if q == 2:
        return (-s, 0)
    return (0, -s)

def fourier(f, chi):
    """fhat(chi) = sum_g f(g) chi(g), exact (re, im) Fractions."""
    re = Fr(0)
    im = Fr(0)
    for g, fg in f.items():
        cr, ci = chival(chi, g)
        re += fg * cr
        im += fg * ci
    return re, im

def conv_c(f, h):
    """Complex group convolution, values = (re, im) Fraction pairs."""
    out = {}
    for g, (fr_, fi_) in f.items():
        gi = g_inv(g)
        for k in G_ELEMS:
            hv = h.get(g_mul(gi, k))
            if hv:
                hr, hi = hv
                orr, oii = out.get(k, (Fr(0), Fr(0)))
                out[k] = (orr + fr_ * hr - fi_ * hi,
                          oii + fr_ * hi + fi_ * hr)
    return out

def e_chi_element(chi):
    """e_chi(g) = conj(chi(g)) / |G|, exact complex Fractions."""
    out = {}
    for g in G_ELEMS:
        cr, ci = chival(chi, g)
        out[g] = (Fr(cr, 128), Fr(-ci, 128))
    return out

def sum2sq_positions_a(count):
    """First `count` integers n >= 2 with n = a^2 + b^2 (own sieve)."""
    cap = 16
    while True:
        cap *= 4
        rep = np.zeros(cap + 1, dtype=bool)
        a = 0
        while a * a <= cap:
            b = a
            while a * a + b * b <= cap:
                rep[a * a + b * b] = True
                b += 1
            a += 1
        vals = [n for n in range(2, cap + 1) if rep[n]]
        if len(vals) >= count:
            return np.log(np.array(vals[:count], dtype=float))

def event_carrier_element(n, th, Hs):
    """Symmetrized carrier element sigma(x_n), exact dict on G (v791
    window face, read-only reuse)."""
    Th0, Th1, Th2, Th3 = th["Th"]
    E = 240 * int(th["sig3"][n])
    pm = [Fr(int(Th0[n]), E), Fr(int(Th1[n]), E),
          Fr(int(Th2[n]), E), Fr(int(Th3[n]), E)]
    ch = classify(n, th["spf"])
    vlist = Hs if ch == "ro" else [0]
    pv = Fr(1, len(vlist))
    c = {}
    for vv in vlist:
        for m in range(4):
            w = pv * pm[m] / 2
            if w == 0:
                continue
            for gg in ((1, vv, m), (1, vv, (-m) % 4)):
                c[gg] = c.get(gg, Fr(0)) + w
    return c

def chat_product(n, chi, th, Hs):
    """The typed product law chat(chi) = (-1)^eps Vfac(w) Mfac(j; n),
    exact Fraction."""
    eps, w, j = chi
    epsf = Fr(-1) if eps else Fr(1)
    if classify(n, th["spf"]) == "ro":
        s = sum(1 if bin(w & v).count("1") % 2 == 0 else -1 for v in Hs)
        vf = Fr(s, 7)
    else:
        vf = Fr(1)
    Th0, Th1, Th2, Th3 = th["Th"]
    E = 240 * int(th["sig3"][n])
    if j == 0:
        mf = Fr(1)
    elif j in (1, 3):
        mf = Fr(int(Th0[n]) - int(Th2[n]), E)
    else:
        mf = Fr(int(Th0[n]) - int(Th1[n]) + int(Th2[n]) - int(Th3[n]), E)
    return epsf * vf * mf

def reads_multi_a(rr, rows, V):
    """Per-event Gram reads for a bank of compression vectors: returns
    q[j] = V^dagger odd_toeplitz(rows[j]) V (K x K complex per event)
    plus the arch Gram (K x K)."""
    ka = rows.shape[0]
    K = V.shape[1]
    q = np.zeros((ka, K, K), dtype=np.complex128)
    for j in range(ka):
        R = core.odd_toeplitz(rows[j], rr["M"])
        W = R @ V
        q[j] = V.conj().T @ W
        del R, W
    c_ar = np.asarray(core.arch_lags(rr["M"], rr["D"]), float)
    T = core.odd_toeplitz(c_ar, rr["M"])
    Ga = V.conj().T @ (T @ V)
    del T
    return q, Ga

def fam3_a(G2, i, k):
    """(00, 11, 01) slots of the (i, k) vector family from a Gram."""
    return np.array([G2[i, i].real, G2[k, k].real, G2[i, k]],
                    dtype=np.complex128)

def blk2_a(tBf, cvec, lam, q3):
    """2x2 hermitian corner block: tB - sum_j c_j lam_j q_j."""
    s0 = float(np.sum(cvec * lam * q3[:, 0].real))
    s1 = float(np.sum(cvec * lam * q3[:, 1].real))
    sx = complex(np.sum(cvec * lam * q3[:, 2]))
    b01 = tBf[2] - sx
    return np.array([[tBf[0] - s0, b01],
                     [np.conj(b01), tBf[1] - s1]])

def id_dev_a(tBf, cvec, q3, B, Xn):
    """Max defect coefficient of (deployed form) - (cell corner) in
    free weights: constant slots + per-w_j slots."""
    d = max(abs(B[0, 0] - tBf[0]), abs(B[1, 1] - tBf[1]),
            abs(B[0, 1] - tBf[2]))
    for s in range(3):
        d = max(d, float(np.max(np.abs(cvec * q3[:, s]
                                       - Xn[:, s]))))
    return d

def position_leg_field(Hs, nvals, uu, lam, alpha, spf, legs):
    """v2 field of the tradeoff probe (read-only reuse): the mass-
    normalized placement scalar c* on H*, leg field in [-1, 1]."""
    num = den = 0.0
    for j, n in enumerate(nvals):
        if classify(int(n), spf) != "ro":
            continue
        phi = math.pi * float(uu[j]) / (2.0 * alpha)
        num += float(lam[j]) * (math.cos(phi) + math.sin(phi))
        den += float(lam[j])
    cstar = (num / den) if den > 0 else 0.0
    Hset = set(Hs)
    c = {x: (cstar if x in Hset else 0.0) for x in range(1, 16)}
    return ({(x, y): (c[x] + c[y]) / 2.0 - 1.0 for (x, y) in legs},
            cstar)

def make_kernel(legs, nb, field, unital):
    K = {}
    for x in nb:
        row = {y: (1.0 + KAPPA * field[(x, y)]) / 7.0 for y in nb[x]}
        if unital:
            s = sum(row.values())
            row = {y: v / s for y, v in row.items()}
        K[x] = row
    return K

def pushforward(K, Hs):
    """p' = K^T (uniform on H*) over the 15 labels."""
    p1 = {}
    for x in Hs:
        for y, v in K[x].items():
            p1[y] = p1.get(y, 0.0) + v / 7.0
    return p1

def fw_mode(p1, w):
    """The w-Fourier mode of a V-slot distribution."""
    return sum(v * (1.0 if bin(w & y).count("1") % 2 == 0 else -1.0)
               for y, v in p1.items())

def part_a():
    section("PRIME.CORNER.OPENDOORS.01 -- the two open doors of the "
            "character-corner channel class (EXPLORATION ONLY)")
    sha = hashlib.sha256(FROZEN_SPEC_a.encode("utf-8")).hexdigest()
    print("    FROZEN_SPEC_a SHA-256 = %s" % sha)
    print("    stop-list honoured: no signed-prime-sum estimation; "
          "v831 / PRIME.FLOOR.PAIRCORR.01 binding.  NO RH claim.")

    print("\nS0 -- firewall")
    bad = ast_firewall()
    check("S0.1 AST firewall: no zeta-zero / prime-table symbol; own "
          "sieves; v563/v738 imports read-only", not bad,
          "found %s" % bad if bad else "clean")

    # ------------------------------------------------------------ frame
    section("S1 -- packet layer, frame, windows, baseline controls")
    th = theta_layer()
    check("S1.1 [EXACT] packet layer: glue identity + f8 + heads to "
          "n <= %d" % N_TH, th["ok"])
    Omega, y_chi, Hstar = label_frame()
    Hs = sorted(label_int(v) for v in Hstar)
    labels15 = list(range(1, 16))

    def omega_pair(x, y):
        vx = [(x >> i) & 1 for i in range(4)]
        vy = [(y >> i) & 1 for i in range(4)]
        return (sum(vx[i] * Omega[i][j] * vy[j]
                    for i in range(4) for j in range(4))) & 1

    nb = {x: [y for y in labels15 if omega_pair(x, y) == 0]
          for x in labels15}
    legs = [(x, y) for x in labels15 for y in nb[x]]
    w0_cands = [w for w in range(1, 16)
                if all(bin(w & v).count("1") % 2 == 0 for v in Hs)]
    ok_w0 = len(w0_cands) == 1
    w0 = w0_cands[0]
    w14 = min(w for w in range(1, 16) if w != w0)
    check("S1.2 [EXACT] frame: v738 lex-first Omega; |H*| = %d; 105 "
          "legs, 7 per row; w0 = %d is the UNIQUE nonzero V-character "
          "trivial on H* (the polar-defining mode); 14-class rep w = "
          "%d" % (len(Hs), w0, w14),
          len(Hs) == 7 and len(legs) == 105 and ok_w0
          and all(len(nb[x]) == 7 for x in labels15))

    wins = deployed_windows()
    nv_union = sorted({int(round(math.exp(float(u))))
                       for _kz, rr in wins for u in rr["uu"]})
    print("    battery: the %d alpha-smallest deployed frame-A windows;"
          " %d distinct events (n <= %d)"
          % (N_WIN, len(nv_union), nv_union[-1]))

    # GL1 exact control (chat = -1 on all union events, Fractions)
    chi_gl1 = (1, 0, 0)
    off = []
    cdicts = {}
    for n in nv_union:
        c = event_carrier_element(n, th, Hs)
        cdicts[n] = c
        re, im = fourier(c, chi_gl1)
        if re != Fr(-1) or im != 0:
            off.append(n)
    CONTROL["GL1"] = not off
    check("S1.3 [EXACT -- CONTROL] the GL1 column reproduces chat_j = "
          "-1 for ALL %d union events (full carrier Fourier, "
          "Fractions, imaginary part 0)" % len(nv_union), not off,
          "off at %s" % off[:3] if off else "")

    # undressed corner-reduction regression on all 3 windows
    ok_id = True
    wreg = []
    for kz, rr in wins:
        nv = np.rint(np.exp(rr["uu"])).astype(np.int64)
        V0 = np.stack([rr["t1"], rr["t2"]], axis=1).astype(np.complex128)
        rows = unit_rows(rr)
        q, Ga = reads_multi_a(rr, rows, V0)
        q3 = np.stack([fam3_a(q[j], 0, 1) for j in range(len(nv))])
        tBf = (Ga[0, 0].real, Ga[1, 1].real, Ga[0, 1])
        tau_X = float(np.linalg.eigvalsh(rr["Ah"])[0])
        A0 = blk2_a(tBf, -np.ones(len(nv)), rr["lam"], q3)
        tau0 = float(np.linalg.eigvalsh(A0)[0])
        scale = max(1.0, float(np.max(np.abs(A0))))
        ok_id &= abs(tau0 - tau_X) / scale <= BAR_ID_REL
        ref = REG_REFS_a.get(kz)
        if ref is not None:
            ok_id &= abs(tau_X - ref[1]) / abs(ref[1]) <= REG_BAR
        wreg.append((kz, tau_X, tau0))
        print("    kz=%-3d ka=%3d  tau_X=%+.6e  undressed corner "
              "lambda_min=%+.6e" % (kz, len(nv), tau_X, tau0))
    CONTROL["REDUCTION"] = ok_id
    check("S1.4 [CONTROL] the certified corner reduction (chat = -1) "
          "reproduces tau_X on all %d windows (<= %.0e rel of block "
          "scale; frozen kz-refs matched)" % (N_WIN, BAR_ID_REL), ok_id)

    # primary window data + position sets
    kz0, rr0 = wins[0]
    h0, M0, alpha0 = rr0["h"], rr0["M"], float(rr0["alpha"])
    lam0 = rr0["lam"]
    nv0 = np.rint(np.exp(rr0["uu"])).astype(np.int64)
    ka0 = len(nv0)
    uu_t = np.asarray(rr0["uu"], float)
    rr_s = core.build_window(kz0, scramble_seed=SCR_SEED)
    uu_s = np.asarray(rr_s["uu"], float)
    uu_e = sum2sq_positions_a(ka0)
    Xn0, B0 = rr0["Xn"], rr0["B"]
    print("    primary window kz=%d: h=%d, M=%d, ka=%d; position sets: "
          "true / scramble(seed %d) / Epstein (n = %d..%d)"
          % (kz0, h0, M0, ka0, SCR_SEED,
             int(round(math.exp(uu_e[0]))),
             int(round(math.exp(uu_e[-1])))))

    # ----------------------------------------------------------- DOOR 1
    section("S2 -- DOOR 1: lag-factor dressings (the cheap decisive "
            "check first)")
    t1, t2 = rr0["t1"], rr0["t2"]
    rows_t = unit_rows(rr0, positions=uu_t)
    R0 = core.odd_toeplitz(rows_t[0], M0)
    trR = float(np.trace(R0))
    read_R = float(t1 @ (R0 @ t1))
    read_tr = trR / h0 * float(t1 @ t1)
    traceless_read = read_R - read_tr
    del R0
    not_traced = abs(traceless_read) > 1e-6 * max(abs(read_R), 1.0)
    check("S2.1 [THE CHEAP DECISIVE CHECK] the GL1 corner does NOT "
          "trace out the factor: the corner functional on the factor "
          "is the (t1, t2) COMPRESSION, not a trace -- the traceless "
          "part of the first event operator has corner read %+.6e "
          "(raw read %+.6e vs trace surrogate %+.6e); factor "
          "dressings are GENERICALLY VISIBLE, Door 1 stays open and "
          "the gates run" % (traceless_read, read_R, read_tr),
          not_traced)

    # factor fields per position set (predeclared)
    def factor_fields(uu, rows):
        dg = rows[:, 0][:, None] - rows[:, M0 - 1 - 2 * np.arange(h0)]
        f_mass = -(lam0 @ dg)
        fm = f_mass / max(float(np.max(np.abs(f_mass))), 1e-300)
        g = np.zeros(h0)
        for j in range(ka0):
            g += float(lam0[j]) * np.sin(
                (np.arange(1, h0 + 1)) * math.pi * float(uu[j])
                / (2.0 * alpha0))
        gh = g / max(float(np.max(np.abs(g))), 1e-300)
        Da = 1.0 + KAPPA * fm                     # D1a multiplier
        Ub = np.exp(1j * math.pi * KAPPA * gh)    # D1b unitary diag
        return Da, Ub

    rows_s = unit_rows(rr0, positions=uu_s)
    rows_e = unit_rows(rr0, positions=uu_e)
    Da_t, Ub_t = factor_fields(uu_t, rows_t)
    Da_s, Ub_s = factor_fields(uu_s, rows_s)
    Da_e, Ub_e = factor_fields(uu_e, rows_e)

    # CP gates
    ok_pos = float(np.min(Da_t)) > 0.0
    ok_uni = float(np.max(np.abs(np.abs(Ub_t) ** 2 - 1.0))) <= BAR_EXACT
    D2 = np.diag(Da_t[:2])
    choi = np.zeros((4, 4))
    for k in range(2):
        for l in range(2):
            Ekl = np.zeros((2, 2))
            Ekl[k, l] = 1.0
            img = D2 @ Ekl @ D2
            choi[2 * k:2 * k + 2, 2 * l:2 * l + 2] = img
    vD = D2.reshape(-1)
    ok_choi = float(np.max(np.abs(choi - np.outer(vD, vD)))) <= BAR_EXACT
    check("S2.2 gate (a) CP: both dressings are single-Kraus "
          "conjugations -- Choi == |vec D><vec D| entrywise on the "
          "leading 2x2 reduction (max dev %.1e); D1a strictly "
          "positive multiplier (min %.4f, NOT unital: max|D^2 - 1| = "
          "%.4f typed); D1b exactly unitary (max||u|^2 - 1| = %.1e, "
          "unital)" % (float(np.max(np.abs(choi - np.outer(vD, vD)))),
                       float(np.min(Da_t)),
                       float(np.max(np.abs(Da_t ** 2 - 1.0))), ok_uni
                       and float(np.max(np.abs(np.abs(Ub_t) ** 2
                                               - 1.0)))),
          ok_pos and ok_uni and ok_choi)

    # vector banks per position set
    def perp_apply(f, v):
        """(1 + KAPPA P_perp diag(f) P_perp) v for real v."""
        u = v - Q_lock @ (Q_lock.T @ v)
        w = f * u
        w = w - Q_lock @ (Q_lock.T @ w)
        return v + KAPPA * w

    Q_lock, _ = np.linalg.qr(np.stack([t1, t2], axis=1))
    sweep_gen = []
    sweep_perp = []
    for _ in range(N_SWEEP_GEN):
        sweep_gen.append(np.array([2.0 * lcg_float() - 1.0
                                   for _ in range(h0)]))
    for _ in range(N_SWEEP_PERP):
        sweep_perp.append(np.array([2.0 * lcg_float() - 1.0
                                    for _ in range(h0)]))

    def bank(Da, Ub, with_sweep):
        cols = [t1, t2, Da * t1, Da * t2,
                np.conj(Ub) * t1, np.conj(Ub) * t2]
        if with_sweep:
            for f in sweep_gen:
                D = 1.0 + KAPPA * f
                cols += [D * t1, D * t2]
            for f in sweep_perp:
                cols += [perp_apply(f, t1), perp_apply(f, t2)]
        return np.stack(cols, axis=1).astype(np.complex128)

    V_t = bank(Da_t, Ub_t, with_sweep=True)
    V_s = bank(Da_s, Ub_s, with_sweep=False)
    V_e = bank(Da_e, Ub_e, with_sweep=False)
    print("    computing Gram reads (true bank %d vectors, scr/eps "
          "banks 6) ..." % V_t.shape[1], flush=True)
    qG_t, Ga_t = reads_multi_a(rr0, rows_t, V_t)
    qG_s, Ga_s = reads_multi_a(rr0, rows_s, V_s)
    qG_e, Ga_e = reads_multi_a(rr0, rows_e, V_e)

    def fam_data(qG, Ga, i, k):
        q3 = np.stack([fam3_a(qG[j], i, k) for j in range(ka0)])
        return q3, (Ga[i, i].real, Ga[k, k].real, Ga[i, k])

    q3_t, tB_t = fam_data(qG_t, Ga_t, 0, 1)       # undressed
    q3a_t, tBa_t = fam_data(qG_t, Ga_t, 2, 3)     # D1a
    q3b_t, tBb_t = fam_data(qG_t, Ga_t, 4, 5)     # D1b
    q3_s, tB_s = fam_data(qG_s, Ga_s, 0, 1)
    q3a_s, tBa_s = fam_data(qG_s, Ga_s, 2, 3)
    q3b_s, tBb_s = fam_data(qG_s, Ga_s, 4, 5)
    q3_e, tB_e = fam_data(qG_e, Ga_e, 0, 1)
    q3a_e, tBa_e = fam_data(qG_e, Ga_e, 2, 3)
    q3b_e, tBb_e = fam_data(qG_e, Ga_e, 4, 5)

    scale0 = max(float(np.max(np.abs(B0))), float(np.max(np.abs(Xn0))),
                 float(np.max(np.abs(q3_t))), 1.0)
    bar_coef = BAR_COEF_REL * scale0
    cm1 = -np.ones(ka0)
    blk_gl1 = {"t": blk2_a(tB_t, cm1, lam0, q3_t),
               "s": blk2_a(tB_s, cm1, lam0, q3_s),
               "e": blk2_a(tB_e, cm1, lam0, q3_e)}
    tau0_pi = {p: float(np.linalg.eigvalsh(blk_gl1[p])[0])
               for p in ("t", "s", "e")}

    def cell_measure(tB3, q33, cvec3):
        """(identity dev, visibility bdiff, delta triple) for a cell
        given per-position-set (tB, q3) dicts and cvec dict."""
        dev = id_dev_a(tB3["t"], cvec3["t"], q33["t"], B0, Xn0)
        bt = blk2_a(tB3["t"], cvec3["t"], lam0, q33["t"])
        bd = float(np.max(np.abs(bt - blk_gl1["t"])))
        deltas = {}
        for p in ("t", "s", "e"):
            bp = blk2_a(tB3[p], cvec3[p], lam0, q33[p])
            deltas[p] = float(np.linalg.eigvalsh(bp)[0]) - tau0_pi[p]
        return dev, bd, deltas

    def ivp(dev, bd, dl):
        I = dev <= bar_coef
        Vv = bd > bar_coef
        P = (abs(dl["t"] - dl["s"]) > BAR_MOVE
             and abs(dl["t"] - dl["e"]) > BAR_MOVE)
        return I, Vv, P

    # Door-1 variants at the GL1 column
    cm1_3 = {"t": cm1, "s": cm1, "e": cm1}
    devA, bdA, dlA = cell_measure(
        {"t": tBa_t, "s": tBa_s, "e": tBa_e},
        {"t": q3a_t, "s": q3a_s, "e": q3a_e}, cm1_3)
    devB, bdB, dlB = cell_measure(
        {"t": tBb_t, "s": tBb_s, "e": tBb_e},
        {"t": q3b_t, "s": q3b_s, "e": q3b_e}, cm1_3)
    IA, VA, PA = ivp(devA, bdA, dlA)
    IB, VB, PB = ivp(devB, bdB, dlB)
    print("    D1a mass-multiplier: defect=%.3e (bar %.1e)  "
          "bdiff=%.3e  delta t/s/e = %+.3e / %+.3e / %+.3e"
          % (devA, bar_coef, bdA, dlA["t"], dlA["s"], dlA["e"]))
    print("    D1b phase-unitary:   defect=%.3e (bar %.1e)  "
          "bdiff=%.3e  delta t/s/e = %+.3e / %+.3e / %+.3e"
          % (devB, bar_coef, bdB, dlB["t"], dlB["s"], dlB["e"]))
    check("S2.3 gate (b)+(c) D1a: the mass dressing is VISIBLE and "
          "placement-sensitive (V=%s, P=%s) but BREAKS the deployed-"
          "form identity with the typed defect %.3e = the injected "
          "multiplier acting inside the lock pair -- (b) and (c) "
          "mutually exclusive, measured" % (VA, PA, devA),
          (not IA) and VA and PA)
    check("S2.4 gate (b)+(c) D1b: the UNITAL phase dressing (CP + "
          "unital, the sharp candidate) is VISIBLE and placement-"
          "sensitive (V=%s, P=%s) yet STILL breaks the identity "
          "(defect %.3e): unitality does NOT rescue the factor side "
          "-- the corner sees every dressing that touches span(t1, "
          "t2), and any such dressing moves the block off the "
          "deployed form" % (VB, PB, devB),
          (not IB) and VB and PB)

    # perp control + sweep dichotomy
    sweep_rows = []
    for d in range(N_SWEEP_GEN + N_SWEEP_PERP):
        i0 = 6 + 2 * d
        q3d, tBd = fam_data(qG_t, Ga_t, i0, i0 + 1)
        dev = id_dev_a(tBd, cm1, q3d, B0, Xn0)
        bd = float(np.max(np.abs(blk2_a(tBd, cm1, lam0, q3d)
                                 - blk_gl1["t"])))
        sweep_rows.append((d < N_SWEEP_GEN, dev, bd))
    perp_ok = all(dev <= bar_coef and bd <= bar_coef
                  for gen, dev, bd in sweep_rows if not gen)
    gen_ok = all(dev > bar_coef for gen, dev, bd in sweep_rows if gen)
    dichot_ok = all((dev <= bar_coef) == (bd <= bar_coef)
                    for _gen, dev, bd in sweep_rows)
    min_gen = min(dev for gen, dev, _bd in sweep_rows if gen)
    max_perp = max(dev for gen, dev, _bd in sweep_rows if not gen)
    CONTROL["PERP"] = perp_ok
    check("S2.5 [CONTROL] the commutant dressing D_perp = 1 + kappa "
          "P_perp F P_perp: all %d perp draws preserve the identity "
          "AND are corner-invisible (max defect %.1e <= bar) -- the "
          "identity-preserving factor dressings are EXACTLY the "
          "corner-invisible ones" % (N_SWEEP_PERP, max_perp), perp_ok)
    check("S2.6 sweep dichotomy (%d generic + %d perp draws, LCG): "
          "defect <= bar <=> corner block unmoved, for EVERY draw; "
          "every generic draw carries its defect (min %.3e > bar) -- "
          "across the factor class, visibility is paid for by the "
          "identity defect, coefficient for coefficient"
          % (N_SWEEP_GEN, N_SWEEP_PERP, min_gen),
          gen_ok and dichot_ok)
    print("    DOOR 1 TYPED: the corner compresses the factor through "
          "the deployed lock pair -- NOT a trace -- so factor "
          "dressings are generically visible AND placement-sensitive; "
          "but the deployed-form identity pins the compressed reads "
          "to the spline reads X_j, so every visible dressing breaks "
          "it by exactly its action on span(t1, t2); the invisible "
          "ones (commutant of the compression) change nothing.  "
          "Door 1 CLOSED: visibility <=> identity defect.")

    # ----------------------------------------------------------- DOOR 2
    section("S3 -- DOOR 2: corners at characters nontrivial on V")
    # exact verification of the product law on ALL 128 characters
    t0 = time.time()
    CHARS = [(eps, w, j) for eps in range(2) for w in range(16)
             for j in range(4)]
    bad_pl = []
    for n in nv_union:
        c = cdicts[n]
        for chi in CHARS:
            re, im = fourier(c, chi)
            if im != 0 or re != chat_product(n, chi, th, Hs):
                bad_pl.append((n, chi))
    check("S3.1 [EXACT] the product law chat(chi) = (-1)^eps Vfac(w) "
          "Mfac(j; n) verified against the full carrier Fourier for "
          "ALL 128 characters x ALL %d union events (Fractions, "
          "imaginary parts 0) -- the 128 characters COLLAPSE to 18 "
          "classes: eps x {w = 0, w = w0, 14 others} x {j = 0, "
          "j in {1,3}, j = 2}; Vfac in {1 (w in {0, w0}), -1/7} on "
          "ram-odd events" % len(nv_union), not bad_pl,
          "%.1f s%s" % (time.time() - t0,
                        "; first %s" % bad_pl[:2] if bad_pl else ""))

    # projector wards on the 18 class reps
    t0 = time.time()
    col_reps = [(eps, w, j) for eps in (1, 0) for w in (0, w0, w14)
                for j in (0, 1, 2)]
    ok_proj = True
    for chi in col_reps:
        E = e_chi_element(chi)
        EE = conv_c(E, E)
        ok_proj &= all(EE.get(g, (Fr(0), Fr(0))) == E[g] for g in G_ELEMS)
        ok_proj &= all(E[g_inv(g)] == (E[g][0], -E[g][1])
                       for g in G_ELEMS)
        for chi2 in CHARS:
            fr_ = Fr(0)
            fi_ = Fr(0)
            for g, (er, ei) in E.items():
                cr, ci = chival(chi2, g)
                fr_ += er * cr - ei * ci
                fi_ += er * ci + ei * cr
            tgt = (Fr(1), Fr(0)) if chi2 == chi else (Fr(0), Fr(0))
            ok_proj &= (fr_, fi_) == tgt
    check("S3.2 [EXACT -- CONTROL] projector wards for all 18 class "
          "reps: e_chi * e_chi = e_chi, e_chi self-adjoint, Fourier "
          "transform = the delta at chi (rank 1) -- exact complex-"
          "Fraction convolutions on the 128-dim group algebra",
          ok_proj, "%.1f s" % (time.time() - t0))
    CONTROL["PROJ"] = ok_proj

    # chat spectra per class
    chat_ex = {}
    for chi in col_reps:
        chat_ex[chi] = {n: chat_product(n, chi, th, Hs)
                        for n in nv_union}
    print("    chat_j SPECTRA per character class (all %d union "
          "events; 'survive' = chat != 0):" % len(nv_union))
    for chi in col_reps:
        vals = chat_ex[chi]
        fl = [float(v) for v in vals.values()]
        nz = sum(1 for v in vals.values() if v == 0)
        dis = len(set(vals.values()))
        by_ch = {}
        for n, v in vals.items():
            by_ch.setdefault(classify(n, th["spf"]), set()).add(v)
        chs = " ".join("%s:%d" % (c, len(s))
                       for c, s in sorted(by_ch.items()))
        print("      chi=(eps=%d,w=%2d,j=%d): distinct=%3d  min=%+.4f "
              " max=%+.4f  zeros=%d/%d  survive=%d  [values/channel "
              "%s]" % (chi[0], chi[1], chi[2], dis, min(fl), max(fl),
                       nz, len(fl), len(fl) - nz, chs))

    # the generalized mass ward (register-dressed chat' at chi)
    fh_t, cst_t = position_leg_field(Hs, nv0, uu_t, lam0, alpha0,
                                     th["spf"], legs)
    fh_s, cst_s = position_leg_field(Hs, nv0, uu_s, lam0, alpha0,
                                     th["spf"], legs)
    fh_e, cst_e = position_leg_field(Hs, nv0, uu_e, lam0, alpha0,
                                     th["spf"], legs)
    K_C = make_kernel(legs, nb, fh_t, unital=False)
    p1_C = pushforward(K_C, Hs)
    n_ro = next(int(n) for n in nv0
                if classify(int(n), th["spf"]) == "ro")
    chi_ward = (0, w14, 1)
    Th0_, Th1_, Th2_, Th3_ = th["Th"]
    E_n = 240.0 * float(th["sig3"][n_ro])
    pmf = [float(Th0_[n_ro]) / E_n, float(Th1_[n_ro]) / E_n,
           float(Th2_[n_ro]) / E_n, float(Th3_[n_ro]) / E_n]
    tot = 0.0j
    for vv, pv in p1_C.items():
        for m in range(4):
            wgt = pv * pmf[m] / 2.0
            for gg in ((1, vv, m), (1, vv, (-m) % 4)):
                cr, ci = chival(chi_ward, gg)
                tot += wgt * (cr + 1j * ci)
    mf1 = (float(Th0_[n_ro]) - float(Th2_[n_ro])) / E_n
    pred = fw_mode(p1_C, w14) * mf1        # eps = 0 => +1
    ok_ward = (abs(tot.real - pred) <= BAR_EXACT
               and abs(tot.imag) <= BAR_EXACT)
    check("S3.3 [CONTROL] the mass ward GENERALIZED: on the full "
          "128-dim register the chi-Fourier value of the register-"
          "dressed ro carrier (n = %d, raw kernel, chi = (0, %d, 1)) "
          "equals (-1)^eps x the w-FOURIER MODE of the dressed V-slot "
          "x the j-mode of the glue slot: %.9f vs predicted %.9f -- "
          "the chi-corner reads exactly ONE V-mode and ONE mu4-mode "
          "per event; every coefficient is a functional of the "
          "carrier (n only), NEVER of the position u_j"
          % (n_ro, w14, tot.real, pred), ok_ward)
    # position-blindness of the coefficients, typed
    ok_blind = all(chat_product(int(n), chi, th, Hs)
                   == chat_ex[chi][int(n)]
                   for chi in col_reps for n in nv0)
    check("S3.4 typed: the chat coefficients are POSITION-BLIND -- "
          "the carrier map n -> sigma(x_n) consumes only the mass "
          "index, so scrambling positions leaves every chat_j(chi) "
          "bit-identical (position data can enter a corner cell ONLY "
          "through the reads q_j, which the identity pins to the "
          "deployed spline reads)", ok_blind)

    # ------------------------------------------------------- CLASS MAP
    section("S4 -- THE CLASS MAP: dressing side x character class -> "
            "(identity, visibility, placement)")
    # register-dressed carrier modes per position set
    K_Ap = {"t": make_kernel(legs, nb, fh_t, unital=True),
            "s": make_kernel(legs, nb, fh_s, unital=True),
            "e": make_kernel(legs, nb, fh_e, unital=True)}
    K_Cp = {"t": K_C,
            "s": make_kernel(legs, nb, fh_s, unital=False),
            "e": make_kernel(legs, nb, fh_e, unital=False)}
    print("    placement scalar c* (the one register scalar): true = "
          "%.6f, scrambled = %.6f, Epstein = %.6f"
          % (cst_t, cst_s, cst_e))

    def reg_cvec(Kd, chi, pi):
        eps, w, j = chi
        p1 = pushforward(Kd[pi], Hs)
        fwv = fw_mode(p1, w)
        out = np.zeros(ka0)
        for jj, n in enumerate(nv0):
            n = int(n)
            base = float(chat_product(n, (0, 0, j), th, Hs))  # Mfac
            if classify(n, th["spf"]) == "ro":
                vf = fwv
            else:
                vf = (1.0 if bin(w & 0).count("1") % 2 == 0 else -1.0)
            out[jj] = ((-1.0) ** eps) * vf * base
        return out

    def char_cvec(chi):
        return np.array([float(chat_ex[chi][int(n)]) for n in nv0])

    row_names = ["none", "regA'u", "regC-r", "facD1a", "facD1b"]
    tB_none = {"t": tB_t, "s": tB_s, "e": tB_e}
    q3_none = {"t": q3_t, "s": q3_s, "e": q3_e}
    tB_fa = {"t": tBa_t, "s": tBa_s, "e": tBa_e}
    q3_fa = {"t": q3a_t, "s": q3a_s, "e": q3a_e}
    tB_fb = {"t": tBb_t, "s": tBb_s, "e": tBb_e}
    q3_fb = {"t": q3b_t, "s": q3b_s, "e": q3b_e}

    cells = {}
    for chi in col_reps:
        cv_none = char_cvec(chi)
        cfg = [
            ("none", tB_none, q3_none,
             {p: cv_none for p in ("t", "s", "e")}),
            ("regA'u", tB_none, q3_none,
             {p: reg_cvec(K_Ap, chi, p) for p in ("t", "s", "e")}),
            ("regC-r", tB_none, q3_none,
             {p: reg_cvec(K_Cp, chi, p) for p in ("t", "s", "e")}),
            ("facD1a", tB_fa, q3_fa,
             {p: cv_none for p in ("t", "s", "e")}),
            ("facD1b", tB_fb, q3_fb,
             {p: cv_none for p in ("t", "s", "e")}),
        ]
        for name, tB3, q33, cv3 in cfg:
            dev, bd, dl = cell_measure(tB3, q33, cv3)
            cells[(name, chi)] = (ivp(dev, bd, dl), dev, bd, dl)

    print("    THE COMPLETE TABLE (I = deployed-form identity, V = "
          "visible vs the undressed GL1 block, P = placement-"
          "sensitive; primary window kz=%d, bar %.1e):" % (kz0,
                                                           bar_coef))
    hdr = "    %-18s" + "  %-9s" * len(row_names)
    print(hdr % tuple(["chi class \\ dress"] + row_names))
    for chi in col_reps:
        rowtxt = []
        for name in row_names:
            (I, Vv, P), dev, bd, dl = cells[(name, chi)]
            rowtxt.append("%d%d%d" % (I, Vv, P))
        tag = " <-- GL1" if chi == chi_gl1 else ""
        print(("    (eps=%d,w=%2d,j=%d)  " % chi)
              + "  ".join("IVP=%s " % s for s in rowtxt) + tag)
    carriers = [(name, chi) for (name, chi), (b, _d, _bd, _dl)
                in cells.items() if all(b[0:3])]
    id_cells = [(name, chi) for (name, chi), (b, _d, _bd, _dl)
                in cells.items() if b[0]]
    quant_ok = all((not b[0]) or (not b[1])
                   for (b, _d, _bd, _dl) in cells.values())
    id_expect = {("none", (1, 0, 0)), ("none", (1, w0, 0)),
                 ("regA'u", (1, 0, 0))}
    check("S4.1 THE QUANTIFIER (measured cell by cell): identity ==> "
          "NOT visible, for EVERY one of the %d cells -- the "
          "deployed-form identity pins the corner block to T_GL1(w), "
          "so an identity cell has zero excess by the same equation "
          "that grants the identity" % len(cells), quant_ok)
    check("S4.2 the identity cells are exactly the PINNING classes: "
          "%s -- the undressed corner at chi_GL1, the undressed "
          "corner at the polar-mode character (eps=1, w=w0, j=0) "
          "whose chat = -1 duplicates the GL1 block bit for bit, and "
          "the unital register dressing at GL1 (the tradeoff "
          "regression); every OTHER cell pays the typed defect"
          % sorted(id_cells), set(id_cells) == id_expect)
    # tradeoff regression as a named control
    (bA_, dA_, bdA_, dlA_) = cells[("regA'u", chi_gl1)]
    (bC_, dC_, bdC_, dlC_) = cells[("regC-r", chi_gl1)]
    CONTROL["TRADEOFF"] = (bA_[0] and not bA_[1]
                           and (not bC_[0]) and bC_[1] and bC_[2])
    check("S4.3 [CONTROL] the register-side tradeoff reproduced: "
          "unital A' keeps the identity with zero excess (defect "
          "%.1e, delta %+.1e); raw C breaks it (defect %.3e) and is "
          "placement-sensitive (delta t/s = %+.3e / %+.3e)"
          % (dA_, dlA_["t"], dC_, dlC_["t"], dlC_["s"]),
          CONTROL["TRADEOFF"])
    check("S4.4 THE CARRIER SCAN: cells carrying all three "
          "(identity AND visibility AND placement) = %s"
          % (sorted(carriers) if carriers else "NONE"),
          True, "empty map = structural closure candidate"
          if not carriers else "CARRIER FOUND -- report prominently")

    # --------------------------------------------------------- verdict
    section("V -- FROZEN VERDICT + the honest consequence")
    door1_closed = ((not IA) and VA and PA and (not IB) and VB and PB
                    and perp_ok and gen_ok and dichot_ok and not_traced)
    door2_closed = ((not bad_pl) and ok_proj and ok_ward and ok_blind
                    and set(id_cells) == id_expect and quant_ok)
    controls_ok = all(CONTROL.values())
    if carriers:
        verdict = "DOORS-CARRY"
    elif door1_closed and door2_closed and controls_ok:
        verdict = "DOORS-CLOSED"
    else:
        verdict = "DOORS-PARTIAL"
    print("\n  VERDICT: %s   [door 1: %s | door 2: %s | controls: %s]"
          % (verdict,
             "CLOSED (visibility <=> identity defect; commutant "
             "invisible)" if door1_closed else "PARTIAL/OPEN",
             "CLOSED (18-class collapse exact; identity only on the "
             "pinning classes, zero excess)" if door2_closed
             else "PARTIAL/OPEN",
             "OK" if controls_ok else "VOID"))
    if verdict == "DOORS-CLOSED":
        print("""
  THE CLASS IS COMPLETE AND EMPTY (the structural closure candidate).
  The exact quantifier, measured: for EVERY corner e_chi of the group
  algebra C[C2 x F2^4 x Z4] (all 128 characters, collapsed exactly to
  18 classes) and EVERY dressing side of the deployed channel class
  (register leg kernels -- unital or raw -- and factor conjugations
  by comb-built multipliers, phases, or random fields), the cell map
  (identity, visibility, placement-sensitivity) contains NO cell with
  all three: the deployed-form corner identity is an EQUATION pinning
  the corner block to the window form T_GL1(w), so any cell that
  carries the identity has zero excess (invisible), and any cell that
  moves the corner has broken the identity by exactly the amount it
  moved.  The two doors close by opposite mechanisms: the register
  side is INFORMATION-STARVED (the chi-corner reads one position-
  blind Fourier mode of the carrier per event -- the mass ward
  generalized), while the factor side is INFORMATION-RICH but PINNED
  (the corner reads the full (t1, t2) compression, which the identity
  locks to the deployed spline reads; only commutant dressings
  survive, and they are invisible).  Position data therefore has no
  corner-compatible channel into this group algebra beyond what the
  deployed window form already carries.

  THE HONEST CONSEQUENCE for PRIME.FLOOR.PAIRCORR.01 (one paragraph):
  the corner program on C[C2 x F2^4 x Z4] is now closed as an
  identification device -- stop-list entry candidate
  PRIME.CORNER.OPENDOORS.01 (exploration-typed; no ledger writes
  here).  The certified corner identity remains true and useful as
  STRUCTURE (positivity transport where a positive P_lock exists),
  but the identification datum -- that the positive object's corner
  IS the deployed window form built from the true prime placements --
  cannot be manufactured by ANY dressing of this register or ANY
  character corner: the carrier map n -> sigma(x_n) is position-
  blind, and the only position-reading slot (the factor compression)
  is exactly the slot the identity freezes.  An identification
  carrier would need a POSITION-DEPENDENT carrier map or a corner
  OUTSIDE this group algebra (a different register, a non-group
  corner, or the pair-correlation substance itself) -- i.e. the wall
  stays EXACTLY PRIME.FLOOR.PAIRCORR.01, now with the corner route's
  perimeter fully surveyed and typed.  NO RH claim.""")
    elif verdict == "DOORS-CARRY":
        print("""
  THE FINDING (report prominently): a cell of the class map carries
  identity AND visibility AND placement -- a named identification
  carrier inside the group-algebra corner class; the route REOPENS at
  that cell; next stage = freeze the carrier as a contract and lift
  it through the Hjelmslev tower.""")
    else:
        print("""
  DOORS-PARTIAL: at least one gate or control failed -- the per-door
  typing above localizes which; no closure claim is made.""")

    n_pass = sum(1 for _n, ok in CHECKS if ok)
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed%s"
          % (time.time() - T0, len(CHECKS), len(FAILS),
             ("  " + ",".join(FAILS)) if FAILS else ""))
    _VERDICTS["a"] = verdict
    return 0 if (n_pass == len(CHECKS) and controls_ok) else 1


# =============== PART B -- hjelmslev_level2_corner_probe.py (frozen probe, verbatim)

FROZEN_SPEC_b = """\
PRIME.CORNER.LEVEL2.01 spec v1 (2026-08-07, frozen before the run).
Tower group G_m = C2 x L_m x Z4, L_m = (Z[i]/(1+i)^m)^4, m = 2, 3
(the H4 lift of the cp_tower probe: address slot lifts, C2/mu4 level-
constant).  Carriers: V-slot uniform on the s_m = 7*8^(m-1) polar
unimodulars S_m (ro), delta_0 else; mu4 glue; C2 sign.  Dual of R_m by
exhaustive cyclic decomposition (additivity + completeness warded);
Vfac(phi) = (1/s_m) sum_{S_m} phi(y) exact by i-power counting (imag
must vanish); identity chars = Ann(<S_m>), count must equal 2^m.  Jet
split: characters nontrivial on pi^{m-1} L_m = level-new.  Carrier
wards: m = 2 all 2048 chars x 2 events (first ro + first non-ro of
the primary window), m = 3 64 LCG chars x 2 events, exact.  Level-2
mass ward: synthetic p' on L_2, full G_2 Fourier == (-1)^eps
F_phi(p') Mfac to 1e-12.  Class map per level: columns (eps in {1,0})
x (distinct Vfac values) x (j in {0,1,2}); rows none / facD1a /
facD1b (open-doors fields verbatim, KAPPA = 1/4); gates I: defect <=
1e-9 scale, V: block-diff > 1e-9 scale, P: |delta_t - delta_s| > 1e-9
AND |delta_t - delta_e| > 1e-9 (scramble seed 1, Epstein comb).
Controls: m = 1 regression (S_1 == H*, spectrum {1:2, -1/7:14},
identity count 2), GL1 anchor exact all union events, tau_X
reproduction 3 windows (1e-6 rel), D1a/D1b frozen refs 1.215e-1 /
5.849e-2 (rel 2e-3).  LCG 20260807.  VERDICTS: LEVEL2-CARRIES /
LEVEL2-CLOSED / LEVEL2-PARTIAL.  NO RH claim; writes nothing.
"""

N_M3_CHAR_SAMPLE = 64

REG_REFS_b = {9: 5.984165e-4, 12: 4.351189e-4, 13: 5.637632e-4}

REG_D1A_DEV = 1.215e-1

REG_D1B_DEV = 5.849e-2

REG_FAC_BAR = 2.0e-3

def lcg(n):
    _LCG[0] = (1103515245 * _LCG[0] + 12345) % (1 << 31)
    return _LCG[0] % n

def build_ring(m):
    """R_m = Z[i]/(1+i)^m as digit codes (cp_tower machinery,
    read-only reuse)."""
    size = 1 << m
    dec = []
    for code in range(size):
        a = b = 0
        pa, pb = 1, 0
        for j in range(m):
            if (code >> j) & 1:
                a += pa
                b += pb
            pa, pb = pa - pb, pa + pb
        dec.append((a, b))

    def enc(a, b):
        code = 0
        for j in range(m):
            d = (a + b) & 1
            if d:
                code |= 1 << j
                a -= 1
            a, b = (a + b) // 2, (b - a) // 2
        return code

    add = [[enc(dec[x][0] + dec[y][0], dec[x][1] + dec[y][1])
            for y in range(size)] for x in range(size)]
    mul = [[enc(dec[x][0] * dec[y][0] - dec[x][1] * dec[y][1],
                dec[x][0] * dec[y][1] + dec[x][1] * dec[y][0])
            for y in range(size)] for x in range(size)]
    neg = [enc(-dec[x][0], -dec[x][1]) for x in range(size)]
    return dict(m=m, size=size, enc=enc, add=add, mul=mul, neg=neg)

def ring_wards(R):
    size, add, mul, neg = R["size"], R["add"], R["mul"], R["neg"]
    ok = True
    for x in range(size):
        ok &= add[x][neg[x]] == 0 and add[x][0] == x and mul[x][1] == x
        for y in range(size):
            ok &= add[x][y] == add[y][x] and mul[x][y] == mul[y][x]
            for z in range(size):
                ok &= add[add[x][y]][z] == add[x][add[y][z]]
                ok &= mul[mul[x][y]][z] == mul[x][mul[y][z]]
                ok &= mul[x][add[y][z]] == add[mul[x][y]][mul[x][z]]
        if not ok:
            return False
    return ok

def ring_dual(R):
    """Characters of the ADDITIVE group of R_m: exhaustive cyclic
    decomposition R = <g1> (+) <g2>; returns the exponent table
    DEXP[w][x] in Z4 (value = i^t), plus (o1, o2)."""
    size, add = R["size"], R["add"]

    def aord(x):
        if x == 0:
            return 1
        k, acc = 1, x
        while acc != 0:
            acc = add[acc][x]
            k += 1
        return k

    orders = [aord(x) for x in range(size)]
    g1 = int(np.argmax(orders))
    o1 = orders[g1]
    C1 = set()
    acc = 0
    for _ in range(o1):
        C1.add(acc)
        acc = add[acc][g1]
    o2 = size // o1
    g2 = 0
    if o2 > 1:
        for x in range(size):
            if orders[x] == o2:
                cyc = set()
                acc = 0
                for _ in range(o2):
                    cyc.add(acc)
                    acc = add[acc][x]
                if cyc & C1 == {0}:
                    g2 = x
                    break
    coords = {}
    a = 0
    for c1 in range(o1):
        b = a
        for c2 in range(o2):
            coords[b] = (c1, c2)
            b = add[b][g2] if o2 > 1 else b
        a = add[a][g1]
    ok = len(coords) == size
    st1, st2 = 4 // o1, (4 // o2 if o2 > 1 else 0)
    DEXP = np.zeros((size, size), dtype=np.int64)
    for w in range(size):
        aa, bb = (w // o2, w % o2) if o2 > 1 else (w, 0)
        for x in range(size):
            c1, c2 = coords[x]
            DEXP[w, x] = (aa * c1 * st1 + bb * c2 * st2) % 4
    # wards: additivity + completeness (distinct rows)
    for w in range(size):
        for x in range(size):
            for y in range(size):
                if DEXP[w, add[x][y]] != (DEXP[w, x] + DEXP[w, y]) % 4:
                    ok = False
    ok &= len({tuple(DEXP[w]) for w in range(size)}) == size
    return DEXP, (o1, o2), ok

def omega_codes(Omega, R):
    neg1 = R["neg"][1]
    return [[(1 if (i < j and Omega[i][j]) else
              (neg1 if (i > j and Omega[i][j]) else 0))
             for j in range(4)] for i in range(4)]

def sum2sq_positions_b(count):
    cap = 16
    while True:
        cap *= 4
        rep = np.zeros(cap + 1, dtype=bool)
        a = 0
        while a * a <= cap:
            b = a
            while a * a + b * b <= cap:
                rep[a * a + b * b] = True
                b += 1
            a += 1
        vals = [n for n in range(2, cap + 1) if rep[n]]
        if len(vals) >= count:
            return np.log(np.array(vals[:count], dtype=float))

def chival1(chi, g):
    eps, w, j = chi
    a, v, m = g
    s = (-1) ** (eps * a) * (-1) ** (bin(w & v).count("1"))
    q = (j * m) % 4
    return [(s, 0), (0, s), (-s, 0), (0, -s)][q]

def event_carrier_m1(n, th, Hs):
    Th0, Th1, Th2, Th3 = th["Th"]
    E = 240 * int(th["sig3"][n])
    pm = [Fr(int(Th0[n]), E), Fr(int(Th1[n]), E),
          Fr(int(Th2[n]), E), Fr(int(Th3[n]), E)]
    vlist = Hs if classify(n, th["spf"]) == "ro" else [0]
    pv = Fr(1, len(vlist))
    c = {}
    for vv in vlist:
        for m in range(4):
            w = pv * pm[m] / 2
            if w == 0:
                continue
            for gg in ((1, vv, m), (1, vv, (-m) % 4)):
                c[gg] = c.get(gg, Fr(0)) + w
    return c

def mfac_frac(n, j, th):
    Th0, Th1, Th2, Th3 = th["Th"]
    E = 240 * int(th["sig3"][n])
    if j == 0:
        return Fr(1)
    if j in (1, 3):
        return Fr(int(Th0[n]) - int(Th2[n]), E)
    return Fr(int(Th0[n]) - int(Th1[n]) + int(Th2[n]) - int(Th3[n]), E)

def reads_multi_b(rr, rows, V):
    ka = rows.shape[0]
    q = np.zeros((ka, V.shape[1], V.shape[1]), dtype=np.complex128)
    for j in range(ka):
        R = core.odd_toeplitz(rows[j], rr["M"])
        q[j] = V.conj().T @ (R @ V)
        del R
    c_ar = np.asarray(core.arch_lags(rr["M"], rr["D"]), float)
    T = core.odd_toeplitz(c_ar, rr["M"])
    Ga = V.conj().T @ (T @ V)
    del T
    return q, Ga

def fam3_b(G2, i, k):
    return np.array([G2[i, i].real, G2[k, k].real, G2[i, k]],
                    dtype=np.complex128)

def blk2_b(tBf, cvec, lam, q3):
    s0 = float(np.sum(cvec * lam * q3[:, 0].real))
    s1 = float(np.sum(cvec * lam * q3[:, 1].real))
    sx = complex(np.sum(cvec * lam * q3[:, 2]))
    b01 = tBf[2] - sx
    return np.array([[tBf[0] - s0, b01],
                     [np.conj(b01), tBf[1] - s1]])

def id_dev_b(tBf, cvec, q3, B, Xn):
    d = max(abs(B[0, 0] - tBf[0]), abs(B[1, 1] - tBf[1]),
            abs(B[0, 1] - tBf[2]))
    for s in range(3):
        d = max(d, float(np.max(np.abs(cvec * q3[:, s] - Xn[:, s]))))
    return d

def part_b():
    section("PRIME.CORNER.LEVEL2.01 -- the closure quantifier at "
            "ladder levels m = 2, 3 (EXPLORATION ONLY)")
    sha = hashlib.sha256(FROZEN_SPEC_b.encode("utf-8")).hexdigest()
    print("    FROZEN_SPEC_b SHA-256 = %s" % sha)
    print("    honest expectation typed: dilution suggests more of "
          "the same; the non-split jet at m = 2 is the one genuinely "
          "new structure -- measured, not assumed.  NO RH claim.")

    print("\nS0 -- firewall")
    bad = ast_firewall()
    check("S0.1 AST firewall: no zeta-zero / prime-table symbol",
          not bad, "found %s" % bad if bad else "clean")

    # ------------------------------------------------------------ frame
    section("S1 -- packet layer, frame, windows, m = 1 anchors")
    th = theta_layer()
    check("S1.1 [EXACT] packet layer: glue identity + f8 + heads to "
          "n <= %d" % N_TH, th["ok"])
    Omega, y_chi, Hstar = label_frame()
    Hs = sorted(label_int(v) for v in Hstar)
    wins = deployed_windows()
    nv_union = sorted({int(round(math.exp(float(u))))
                       for _kz, rr in wins for u in rr["uu"]})
    chi_gl1 = (1, 0, 0)
    off = []
    for n in nv_union:
        c = event_carrier_m1(n, th, Hs)
        re = Fr(0)
        im = Fr(0)
        for g, fg in c.items():
            cr, ci = chival1(chi_gl1, g)
            re += fg * cr
            im += fg * ci
        if re != Fr(-1) or im != 0:
            off.append(n)
    CONTROL["GL1"] = not off
    check("S1.2 [EXACT -- CONTROL] the GL1 anchor: chat_j = -1 for "
          "ALL %d union events (m = 1 carrier Fourier, Fractions)"
          % len(nv_union), not off)

    ok_id = True
    for kz, rr in wins:
        nv = np.rint(np.exp(rr["uu"])).astype(np.int64)
        V0 = np.stack([rr["t1"], rr["t2"]], axis=1).astype(np.complex128)
        q, Ga = reads_multi_b(rr, unit_rows(rr), V0)
        q3 = np.stack([fam3_b(q[j], 0, 1) for j in range(len(nv))])
        tBf = (Ga[0, 0].real, Ga[1, 1].real, Ga[0, 1])
        tau_X = float(np.linalg.eigvalsh(rr["Ah"])[0])
        A0 = blk2_b(tBf, -np.ones(len(nv)), rr["lam"], q3)
        tau0 = float(np.linalg.eigvalsh(A0)[0])
        scale = max(1.0, float(np.max(np.abs(A0))))
        ok_id &= (abs(tau0 - tau_X) / scale <= BAR_ID_REL
                  and abs(tau_X - REG_REFS_b[kz]) / REG_REFS_b[kz]
                  <= REG_BAR)
    CONTROL["REDUCTION"] = ok_id
    check("S1.3 [CONTROL] the corner reduction reproduces tau_X on "
          "all %d windows (frozen refs matched)" % N_WIN, ok_id)

    kz0, rr0 = wins[0]
    h0, M0, alpha0 = rr0["h"], rr0["M"], float(rr0["alpha"])
    lam0 = rr0["lam"]
    nv0 = np.rint(np.exp(rr0["uu"])).astype(np.int64)
    ka0 = len(nv0)
    uu_t = np.asarray(rr0["uu"], float)
    uu_s = np.asarray(core.build_window(kz0, scramble_seed=SCR_SEED)
                      ["uu"], float)
    uu_e = sum2sq_positions_b(ka0)
    Xn0, B0 = rr0["Xn"], rr0["B"]
    t1, t2 = rr0["t1"], rr0["t2"]
    ro_mask = np.array([classify(int(n), th["spf"]) == "ro"
                        for n in nv0])
    n_ro = int(nv0[np.argmax(ro_mask)])
    n_oth = int(nv0[np.argmax(~ro_mask)])
    print("    primary window kz=%d: h=%d, ka=%d; ward events: ro "
          "n=%d, non-ro n=%d" % (kz0, h0, ka0, n_ro, n_oth))

    # ----------------------------------------------------- ring ladder
    section("S2 -- the ring ladder, duals, polar supports")
    rings = {m: build_ring(m) for m in (1, 2, 3)}
    ok_r = all(ring_wards(rings[m]) for m in (1, 2, 3))
    duals = {}
    ok_d = True
    for m in (1, 2, 3):
        DEXP, (o1, o2), okm = ring_dual(rings[m])
        duals[m] = DEXP
        ok_d &= okm
        print("    R_%d: additive group Z/%d x Z/%d; dual complete "
              "(%d characters, additivity exhaustive)"
              % (m, o1, o2, rings[m]["size"]))
    check("S2.1 [EXACT] rings R_1..R_3 (axioms exhaustive) and their "
          "additive duals (cyclic decomposition, additivity + "
          "completeness warded)", ok_r and ok_d)

    Oms = {m: omega_codes(Omega, rings[m]) for m in (1, 2, 3)}
    yhat = tuple(int(y_chi[i]) for i in range(4))
    Smv = {}
    Sgen = {}
    Kred = {}
    ok_s = True
    for m in (1, 2, 3):
        R = rings[m]
        add, mul = R["add"], R["mul"]
        wrow = []
        for j in range(4):
            acc = 0
            for i in range(4):
                o = Oms[m][i][j]
                if o:
                    acc = add[acc][mul[yhat[i]][o]]
            wrow.append(acc)
        S = []
        for y in product(range(R["size"]), repeat=4):
            if not ((y[0] | y[1] | y[2] | y[3]) & 1):
                continue
            acc = 0
            for j in range(4):
                acc = add[acc][mul[wrow[j]][y[j]]]
            if acc == 0:
                S.append(y)
        Smv[m] = S
        ok_s &= len(S) == 7 * 8 ** (m - 1)
        # generated subgroup <S_m>
        zero = (0, 0, 0, 0)
        known = {zero}
        queue = list(S)
        for y in S:
            known.add(y)
        while queue:
            a = queue.pop()
            for b in S:
                c = tuple(add[a[i]][b[i]] for i in range(4))
                if c not in known:
                    known.add(c)
                    queue.append(c)
        Sgen[m] = known
        ok_s &= len(known) == 2 ** (3 * m)
        # reduction kernel pi^{m-1} L_m
        pi_code = R["enc"](1, 1)
        pw = 1
        for _ in range(m - 1):
            pw = mul[pw][pi_code]
        Kred[m] = {tuple(mul[pw][z[i]] for i in range(4))
                   for z in product(range(R["size"]), repeat=4)}
    check("S2.2 [EXACT] polar supports: |S_m| = %s == 7*8^(m-1) "
          "(cp_tower H4.2 reproduced); generated subgroups |<S_m>| = "
          "%s == 2^(3m) (the full polar submodule)"
          % ([len(Smv[m]) for m in (1, 2, 3)],
             [len(Sgen[m]) for m in (1, 2, 3)]), ok_s)
    s1_ints = sorted(sum(b << i for i, b in enumerate(y))
                     for y in Smv[1])
    CONTROL["S1FRAME"] = s1_ints == Hs
    check("S2.3 [CONTROL] the m = 1 ring frame ties to the deployed "
          "v738 frame: S_1 as bit-labels == H* = %s" % Hs,
          CONTROL["S1FRAME"])

    # -------------------------------------------------- Vfac spectra
    section("S3 -- the exact Vfac spectra of the full duals; "
            "identity characters; the jet split")
    spectra = {}
    id_chars = {}
    jet_info = {}
    ok_imag = True
    for m in (1, 2, 3):
        size = rings[m]["size"]
        DE = duals[m]
        Ys = np.array(Smv[m], dtype=np.int64)
        Kr = np.array(sorted(Kred[m]), dtype=np.int64)
        s_m = len(Smv[m])
        spec = {}
        ids = []
        jet_ids = 0
        n_jet = 0
        for wflat in range(size ** 4):
            w = ((wflat // size ** 3) % size, (wflat // size ** 2)
                 % size, (wflat // size) % size, wflat % size)
            ex = (DE[w[0]][Ys[:, 0]] + DE[w[1]][Ys[:, 1]]
                  + DE[w[2]][Ys[:, 2]] + DE[w[3]][Ys[:, 3]]) % 4
            nb = np.bincount(ex, minlength=4)
            re = int(nb[0] - nb[2])
            im = int(nb[1] - nb[3])
            if im != 0:
                ok_imag = False
            v = Fr(re, s_m)
            if v not in spec:
                spec[v] = [0, w]
            spec[v][0] += 1
            exk = (DE[w[0]][Kr[:, 0]] + DE[w[1]][Kr[:, 1]]
                   + DE[w[2]][Kr[:, 2]] + DE[w[3]][Kr[:, 3]]) % 4
            is_jet = bool(np.any(exk != 0))
            n_jet += is_jet
            if v == 1:
                ids.append(w)
                jet_ids += is_jet
        spectra[m] = spec
        id_chars[m] = ids
        jet_info[m] = (n_jet, jet_ids)
        vals = sorted(spec.keys(), reverse=True)
        print("    m=%d: |dual| = %5d, %2d distinct Vfac values; "
              "identity (Vfac = 1) count = %d; level-new (jet) "
              "characters = %d, of which identity = %d"
              % (m, size ** 4, len(vals), len(ids), n_jet, jet_ids))
        print("        spectrum: %s"
              % ", ".join("%s x%d" % (v, spec[v][0])
                          for v in vals[:12])
              + (" ..." if len(vals) > 12 else ""))
    check("S3.1 [EXACT] all Vfac values REAL (S_m symmetric) and the "
          "identity characters are EXACTLY Ann(<S_m>) with count "
          "2^m: %s (m = 1, 2, 3) -- every identity character is "
          "trivial on the full polar submodule"
          % [len(id_chars[m]) for m in (1, 2, 3)],
          ok_imag and all(len(id_chars[m]) == 2 ** m
                          for m in (1, 2, 3)))
    CONTROL["M1SPEC"] = (spectra[1].get(Fr(1), [0])[0] == 2
                         and spectra[1].get(Fr(-1, 7), [0])[0] == 14)
    check("S3.2 [CONTROL] the m = 1 regression: Vfac spectrum "
          "{1 x 2, -1/7 x 14} == the open-doors 18-class structure",
          CONTROL["M1SPEC"])
    ok_ann = True
    for m in (2, 3):
        DE = duals[m]
        Gm = np.array(sorted(Sgen[m]), dtype=np.int64)
        for w in id_chars[m]:
            ex = (DE[w[0]][Gm[:, 0]] + DE[w[1]][Gm[:, 1]]
                  + DE[w[2]][Gm[:, 2]] + DE[w[3]][Gm[:, 3]]) % 4
            ok_ann &= not np.any(ex)
    check("S3.3 [EXACT] annihilator ward: every identity character "
          "is trivial on ALL of <S_m> (m = 2, 3) -- Vfac = 1 forces "
          "phi == 1 on the polar submodule (|phi| = 1 and average 1)",
          ok_ann)
    print("    THE JET SPLIT TYPED: at m = 2 the %d level-new "
          "characters refine the Vfac spectrum (new values beyond "
          "{1, -1/7}), i.e. the jet DOES open new arithmetic modes; "
          "whether any of them escapes the pinning is decided by the "
          "class map (S5), and their identity members (%d) are "
          "pinned by construction (Vfac = 1 ==> chat = -1)."
          % (jet_info[2][0], jet_info[2][1]))

    # ------------------------------------------------- carrier wards
    section("S4 -- carrier wards on G_2 / G_3 + the level-2 mass ward")
    t0 = time.time()

    def carrier_fourier_exact(m, n, eps, w, j):
        """Full G_m-Fourier of the exact level-m carrier at
        chi = (eps, phi_w, j), exact (re, im) Fractions."""
        R = rings[m]
        DE = duals[m]
        Th0, Th1, Th2, Th3 = th["Th"]
        E = 240 * int(th["sig3"][n])
        pm = [Fr(int(Th0[n]), E), Fr(int(Th1[n]), E),
              Fr(int(Th2[n]), E), Fr(int(Th3[n]), E)]
        ys = Smv[m] if classify(n, th["spf"]) == "ro" else [(0, 0, 0, 0)]
        pv = Fr(1, len(ys))
        re = Fr(0)
        im = Fr(0)
        for y in ys:
            ty = int((DE[w[0]][y[0]] + DE[w[1]][y[1]] + DE[w[2]][y[2]]
                      + DE[w[3]][y[3]]) % 4)
            for mm in range(4):
                wgt = pv * pm[mm] / 2
                if wgt == 0:
                    continue
                for mmm in (mm, (-mm) % 4):
                    tt = (ty + j * mmm + 2 * eps) % 4
                    if tt == 0:
                        re += wgt
                    elif tt == 1:
                        im += wgt
                    elif tt == 2:
                        re -= wgt
                    else:
                        im -= wgt
        return re, im

    def vfac_frac(m, w):
        DE = duals[m]
        Ys = np.array(Smv[m], dtype=np.int64)
        ex = (DE[w[0]][Ys[:, 0]] + DE[w[1]][Ys[:, 1]]
              + DE[w[2]][Ys[:, 2]] + DE[w[3]][Ys[:, 3]]) % 4
        nb = np.bincount(ex, minlength=4)
        return Fr(int(nb[0] - nb[2]), len(Smv[m]))

    bad_w = []
    size2 = rings[2]["size"]
    for n in (n_ro, n_oth):
        for eps in (0, 1):
            for j in range(4):
                for wflat in range(size2 ** 4):
                    w = ((wflat // size2 ** 3) % size2,
                         (wflat // size2 ** 2) % size2,
                         (wflat // size2) % size2, wflat % size2)
                    re, im = carrier_fourier_exact(2, n, eps, w, j)
                    vf = (vfac_frac(2, w)
                          if classify(n, th["spf"]) == "ro" else Fr(1))
                    tgt = (Fr(-1) if eps else Fr(1)) * vf \
                        * mfac_frac(n, j, th)
                    if re != tgt or im != 0:
                        bad_w.append((n, eps, w, j))
    check("S4.1 [EXACT] the m = 2 product law chat = (-1)^eps "
          "Vfac(phi) Mfac(j; n) verified against the FULL G_2 "
          "carrier Fourier for ALL 2048 characters x 2 events "
          "(ro n=%d, non-ro n=%d)" % (n_ro, n_oth), not bad_w,
          "%.1f s%s" % (time.time() - t0,
                        "; first %s" % bad_w[:1] if bad_w else ""))
    t0 = time.time()
    size3 = rings[3]["size"]
    bad3 = []
    for _ in range(N_M3_CHAR_SAMPLE):
        w = tuple(lcg(size3) for _ in range(4))
        eps = lcg(2)
        j = lcg(4)
        for n in (n_ro, n_oth):
            re, im = carrier_fourier_exact(3, n, eps, w, j)
            vf = (vfac_frac(3, w)
                  if classify(n, th["spf"]) == "ro" else Fr(1))
            tgt = (Fr(-1) if eps else Fr(1)) * vf * mfac_frac(n, j, th)
            if re != tgt or im != 0:
                bad3.append((n, eps, w, j))
    check("S4.2 [EXACT] the m = 3 product law on %d LCG-sampled "
          "characters x 2 events (full G_3 carrier Fourier, exact)"
          % N_M3_CHAR_SAMPLE, not bad3,
          "%.1f s" % (time.time() - t0))

    # level-2 mass ward: synthetic dressed V-slot
    DE2 = duals[2]
    pprime = {}
    tot = 0.0
    for y in Smv[2]:
        wgt = 1.0 + 0.25 * (1.0 if (y[0] & 1) else -1.0)
        pprime[y] = wgt
        tot += wgt
    pprime = {y: v / tot for y, v in pprime.items()}
    w_test = id_chars[2][0]
    w_test2 = None
    for v, (_cnt, wrep) in spectra[2].items():
        if v != 1:
            w_test2 = wrep
            break
    ok_mw = True
    for (eps, w, j) in ((0, w_test2, 1), (1, w_test2, 0),
                        (1, w_test, 0)):
        Th0_, Th1_, Th2_, Th3_ = th["Th"]
        E = 240.0 * float(th["sig3"][n_ro])
        pmf = [float(Th0_[n_ro]) / E, float(Th1_[n_ro]) / E,
               float(Th2_[n_ro]) / E, float(Th3_[n_ro]) / E]
        acc = 0.0j
        for y, pv in pprime.items():
            ty = int((DE2[w[0]][y[0]] + DE2[w[1]][y[1]]
                      + DE2[w[2]][y[2]] + DE2[w[3]][y[3]]) % 4)
            for mm in range(4):
                wgt = pv * pmf[mm] / 2.0
                for mmm in (mm, (-mm) % 4):
                    tt = (ty + j * mmm + 2 * eps) % 4
                    acc += wgt * (1j ** tt)
        fmode = sum(pv * (1j ** int((DE2[w[0]][y[0]] + DE2[w[1]][y[1]]
                                     + DE2[w[2]][y[2]]
                                     + DE2[w[3]][y[3]]) % 4))
                    for y, pv in pprime.items())
        mfv = 1.0 if j == 0 else (pmf[0] - pmf[2] if j in (1, 3) else
                                  pmf[0] - pmf[1] + pmf[2] - pmf[3])
        pred = ((-1.0) ** eps) * fmode * mfv
        ok_mw &= abs(acc - pred) <= BAR_EXACT
    check("S4.3 [CONTROL] THE LEVEL-2 MASS WARD: for a synthetic "
          "dressed V-slot p' on L_2 the full G_2 Fourier factorizes "
          "as (-1)^eps x (the phi-mode of p') x Mfac to %.0e -- the "
          "level-m corner reads exactly ONE phi-mode of the carrier "
          "per event; the carrier map n -> sigma_m(x_n) consumes "
          "only n and the frame (position-blind), so the m = 1 "
          "register closure transfers verbatim" % BAR_EXACT, ok_mw)

    # ------------------------------------------------------ class map
    section("S5 -- the class map at m = 2, 3 (rows: none / facD1a / "
            "facD1b)")

    def factor_fields(uu, rows):
        dg = rows[:, 0][:, None] - rows[:, M0 - 1 - 2 * np.arange(h0)]
        f_mass = -(lam0 @ dg)
        fm = f_mass / max(float(np.max(np.abs(f_mass))), 1e-300)
        g = np.zeros(h0)
        for j in range(ka0):
            g += float(lam0[j]) * np.sin(
                (np.arange(1, h0 + 1)) * math.pi * float(uu[j])
                / (2.0 * alpha0))
        gh = g / max(float(np.max(np.abs(g))), 1e-300)
        return 1.0 + KAPPA * fm, np.exp(1j * math.pi * KAPPA * gh)

    rows_pi = {"t": unit_rows(rr0, positions=uu_t),
               "s": unit_rows(rr0, positions=uu_s),
               "e": unit_rows(rr0, positions=uu_e)}
    uu_pi = {"t": uu_t, "s": uu_s, "e": uu_e}
    q3d = {}
    tBd = {}
    for p in ("t", "s", "e"):
        Da, Ub = factor_fields(uu_pi[p], rows_pi[p])
        V = np.stack([t1, t2, Da * t1, Da * t2,
                      np.conj(Ub) * t1, np.conj(Ub) * t2],
                     axis=1).astype(np.complex128)
        qG, Ga = reads_multi_b(rr0, rows_pi[p], V)
        for name, (i, k) in (("none", (0, 1)), ("facD1a", (2, 3)),
                             ("facD1b", (4, 5))):
            q3d[(name, p)] = np.stack([fam3_b(qG[j], i, k)
                                       for j in range(ka0)])
            tBd[(name, p)] = (Ga[i, i].real, Ga[k, k].real, Ga[i, k])

    scale0 = max(float(np.max(np.abs(B0))), float(np.max(np.abs(Xn0))),
                 float(np.max(np.abs(q3d[("none", "t")]))), 1.0)
    bar_coef = BAR_COEF_REL * scale0
    cm1 = -np.ones(ka0)
    blk_gl1 = {p: blk2_b(tBd[("none", p)], cm1, lam0, q3d[("none", p)])
               for p in ("t", "s", "e")}
    tau0_pi = {p: float(np.linalg.eigvalsh(blk_gl1[p])[0])
               for p in ("t", "s", "e")}

    def cell(name, cvec):
        dev = id_dev_b(tBd[(name, "t")], cvec, q3d[(name, "t")], B0, Xn0)
        bt = blk2_b(tBd[(name, "t")], cvec, lam0, q3d[(name, "t")])
        bd = float(np.max(np.abs(bt - blk_gl1["t"])))
        dl = {}
        for p in ("t", "s", "e"):
            bp = blk2_b(tBd[(name, p)], cvec, lam0, q3d[(name, p)])
            dl[p] = float(np.linalg.eigvalsh(bp)[0]) - tau0_pi[p]
        I = dev <= bar_coef
        Vv = bd > bar_coef
        P = (abs(dl["t"] - dl["s"]) > BAR_MOVE
             and abs(dl["t"] - dl["e"]) > BAR_MOVE)
        return (I, Vv, P), dev, bd, dl

    # factor regression at the GL1 column
    _ivpA, devA, _bdA, dlA = cell("facD1a", cm1)
    _ivpB, devB, _bdB, dlB = cell("facD1b", cm1)
    CONTROL["FACREG"] = (abs(devA - REG_D1A_DEV) / REG_D1A_DEV
                         <= REG_FAC_BAR
                         and abs(devB - REG_D1B_DEV) / REG_D1B_DEV
                         <= REG_FAC_BAR)
    check("S5.1 [CONTROL] the factor-dressing regression: D1a/D1b "
          "identity defects %.4e / %.4e reproduce the frozen open-"
          "doors values %.3e / %.3e (rel %.0e)"
          % (devA, devB, REG_D1A_DEV, REG_D1B_DEV, REG_FAC_BAR),
          CONTROL["FACREG"])

    mfacf = {j: np.array([float(mfac_frac(int(n), j, th))
                          for n in nv0]) for j in (0, 1, 2)}
    carriers = []
    closed_lv = {}
    for m in (2, 3):
        vals = sorted(spectra[m].keys(), reverse=True)
        cols = [(eps, v, j) for eps in (1, 0) for v in vals
                for j in (0, 1, 2)]
        print("\n    LEVEL m = %d: %d columns (2 eps x %d Vfac "
              "classes x 3 j-classes); character multiplicities per "
              "Vfac class as in S3" % (m, len(cols), len(vals)))
        pat = {}
        id_ok = True
        quant_ok = True
        table_lines = []
        for (eps, v, j) in cols:
            vf = float(v)
            base = np.where(ro_mask, vf, 1.0) * mfacf[j]
            # eps bit convention: eps = 1 is the sign character
            cvec = (-1.0 if eps == 1 else 1.0) * base
            rowres = []
            for name in ("none", "facD1a", "facD1b"):
                (I, Vv, P), dev, bd, dl = cell(name, cvec)
                rowres.append((name, I, Vv, P))
                quant_ok &= (not I) or (not Vv)
                if I and Vv and P:
                    carriers.append((m, name, (eps, str(v), j)))
            key = tuple("%d%d%d" % (r[1], r[2], r[3]) for r in rowres)
            pat[key] = pat.get(key, 0) + 1
            is_id_col = (eps == 1 and v == 1 and j == 0)
            if is_id_col:
                id_ok &= rowres[0][1] and not rowres[0][2] \
                    and not rowres[0][3]
                table_lines.append((eps, v, j, key, "<-- identity "
                                    "column (x%d characters)"
                                    % len(id_chars[m])))
            elif len(table_lines) < 14:
                table_lines.append((eps, v, j, key, ""))
        for (eps, v, j, key, tag) in table_lines:
            print("      (eps=%d, Vfac=%-6s, j=%d): none/facA/facB "
                  "IVP = %s %s %s  %s"
                  % (eps, v, j, key[0], key[1], key[2], tag))
        print("      IVP pattern census over all %d columns: %s"
              % (len(cols), {" ".join(k): c for k, c in pat.items()}))
        closed_lv[m] = id_ok and quant_ok
        check("S5.%d level m = %d: the identity column (eps=1, "
              "Vfac=1, j=0; %d characters = Ann(<S_m>), including "
              "%d jet-new) is INVISIBLE and placement-dead (IVP = "
              "100); EVERY other column is visible with the identity "
              "broken (the quantifier identity ==> not-visible holds "
              "on all %d x 3 cells)"
              % (m, m, len(id_chars[m]), jet_info[m][1], len(cols)),
              closed_lv[m])

    check("S5.4 THE CARRIER SCAN at m = 2, 3: cells with identity "
          "AND visibility AND placement = %s"
          % (carriers if carriers else "NONE"), True,
          "empty = the class theorem extends" if not carriers
          else "CARRIER FOUND -- report prominently")

    # --------------------------------------------------------- verdict
    section("V -- FROZEN VERDICT + the honest consequence")
    controls_ok = all(CONTROL.values())
    struct_ok = (ok_r and ok_d and ok_s and ok_imag and ok_ann
                 and not bad_w and not bad3 and ok_mw
                 and all(len(id_chars[m]) == 2 ** m for m in (1, 2, 3)))
    if carriers:
        verdict = "LEVEL2-CARRIES"
    elif struct_ok and closed_lv[2] and closed_lv[3] and controls_ok:
        verdict = "LEVEL2-CLOSED"
    else:
        verdict = "LEVEL2-PARTIAL"
    print("\n  VERDICT: %s" % verdict)
    if verdict == "LEVEL2-CLOSED":
        print("""
  THE QUANTIFIER EXTENDS TO m <= 3 (the class theorem strengthens).
  For every character of G_m = C2 x L_m x Z4 (all 2048 at m = 2, all
  32768 at m = 3, collapsed exactly by the product law verified on
  the full G_m carrier Fourier), the corner coefficient is chat =
  (-1)^eps Vfac(phi) Mfac(j; n) with Vfac the phi-average over the
  polar support S_m.  The identity characters are EXACTLY the
  annihilator of the polar submodule <S_m> (2^m of them -- including
  jet-new ones at m >= 2), and each of them reproduces the GL1 block
  bit for bit: invisible, placement-dead.  Every other character is
  visible and placement-sensitive but pays the typed identity defect
  -- including EVERY jet-new character: the non-split jet at m = 2
  does refine the readable arithmetic (the Vfac spectrum grows beyond
  {1, -1/7}), but it refines POSITION-BLIND data only, because the
  tower's licensed carrier map n -> sigma_m(x_n) (the H4 geometric
  lift) consumes the mass index and the frame, never a position.
  The hoped-for position-graded epsilon-component does not exist in
  the corner's input at any level m <= 3; a position-graded carrier
  would be a NEW carrier map -- the dressing class already closed by
  the tradeoff/open-doors probes, whose mass ward transfers verbatim
  to level m (S4.3).  The wall stays PRIME.FLOOR.PAIRCORR.01.
  NO RH claim.""")
    elif verdict == "LEVEL2-CARRIES":
        print("""
  THE FINDING (report prominently): a level-m character cell carries
  identity AND visibility AND placement -- the jet structure DOES
  open an identification channel invisible at m = 1; freeze the
  carrier cell as a contract and lift it through the tower.""")
    n_pass = sum(1 for _n, ok in CHECKS if ok)
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed%s"
          % (time.time() - T0, len(CHECKS), len(FAILS),
             ("  " + ",".join(FAILS)) if FAILS else ""))
    _VERDICTS["b"] = verdict
    return 0 if (n_pass == len(CHECKS) and controls_ok) else 1


# =============== PART C -- the Lean mirror (SectorPositiveDescent.lean;
# kernel-checked statements cited, numeric witnesses only -- v817
# precedent)

def _min_eig(M):
    return float(np.linalg.eigvalsh((M + M.T) / 2.0).min())


def part_c():
    section("v837 PART C -- the Lean mirror: TfptCarrier/"
            "SectorPositiveDescent.lean (kernel-checked; numeric "
            "witnesses here)")
    rng = np.random.default_rng(20260807)
    n = 6
    Q, _ = np.linalg.qr(rng.normal(size=(n, n)))
    e = Q[:, :3] @ Q[:, :3].T
    A = rng.normal(size=(n, n))
    rho = A @ A.T
    corner = e @ rho @ e
    comp = (np.eye(n) - e) @ rho @ (np.eye(n) - e)
    ok1 = (_min_eig(corner) >= -1e-10
           and abs(np.trace(corner) + np.trace(comp)
                   - np.trace(rho)) < 1e-9
           and np.trace(corner) <= np.trace(rho) + 1e-9
           and float(np.abs(e @ corner @ e - corner).max()) < 1e-9)
    check("C1 corner compression is CP at the matrix level with the "
          "corner-trace split tr(e rho e) + tr((1-e) rho (1-e)) = "
          "tr rho and idempotent compression (min eig %.1e >= -1e-10) "
          "-- corner_posSemidef / corner_trace_le / corner_corner, "
          "kernel-checked" % _min_eig(corner), ok1)

    V = np.zeros((2 * n, n))
    for j in range(n):
        V[2 * j, j] = V[2 * j + 1, j] = 1.0 / math.sqrt(2.0)

    def phi(a):
        return V.T @ a @ V

    e_up = V @ e @ V.T
    B = rng.normal(size=(2 * n, 2 * n))
    rho_up = B @ B.T
    dev = float(np.abs(phi(e_up @ rho_up @ e_up)
                       - e @ phi(rho_up) @ e).max())
    ok2 = (dev < 1e-9
           and float(np.abs(phi(e_up) - e).max()) < 1e-9
           and float(np.abs(phi(np.eye(2 * n)) - np.eye(n)).max()) < 1e-9
           and _min_eig(phi(rho_up)) >= -1e-10)
    check("C2 descent tower: phi(e' a e') = e phi(a) e (dev %.1e), "
          "phi(e') = e, phi unital positive -- the Hjelmslev "
          "compatibility whose defect part B measures as identically "
          "zero (DescentTower / tower_proj_descent / "
          "cornerFamily_compatible, kernel-checked)" % dev, ok2)

    G = None
    for k in range(1, 25):
        Gk = corner * (1.0 + 2.0 ** (-k))
        G = Gk
    x = rng.normal(size=n)
    identified = float(np.trace(G))
    ok3 = (_min_eig(G) >= -1e-10
           and float(x @ (G @ x)) >= -1e-9
           and identified >= 0.0)
    check("C3 the sector floor: the entrywise limit of corner states "
          "is PSD with every quadratic direction nonnegative "
          "(corner_limit_posSemidef via GramCompactness), and the "
          "identified functional enters ONLY as the named hypothesis "
          "IdentificationPositivity (here a nonnegative witness "
          "%.3f) -- the kernel-checked honest boundary: structural "
          "positivity is comb-blind (parts A/B), the identification "
          "datum is deliberately NOT a theorem" % identified, ok3)
    print("  (kernel-checked statements: experiments/"
          "lean4-carrier-rigidity/TfptCarrier/SectorPositiveDescent"
          ".lean -- lake build green, no sorry, no native_decide)")


EXPECT = {"a": (19, "DOORS-CLOSED"), "b": (17, "LEVEL2-CLOSED"),
          "c": (3, None)}


def run():
    t_all = time.time()
    rc = 0
    counts = {}
    for tag, part in (("a", part_a), ("b", part_b), ("c", part_c)):
        CHECKS.clear()
        FAILS.clear()
        CONTROL.clear()
        _LCG[0] = 20260807
        globals()["T0"] = time.time()
        r = part()
        rc += int(r or 0)
        counts[tag] = (len(CHECKS), len(FAILS))
    pattern_ok = all(
        counts[t][0] == EXPECT[t][0] and counts[t][1] == 0
        and (EXPECT[t][1] is None or _VERDICTS.get(t) == EXPECT[t][1])
        for t in EXPECT)
    n_run = sum(c[0] for c in counts.values())
    n_fail = sum(c[1] for c in counts.values())
    print("\n" + "=" * 74)
    print("v837: %d/%d checks passed, %d failed | runtime %.1f s"
          % (n_run - n_fail, n_run, n_fail, time.time() - t_all))
    print("NO RH claim; the wall stays PRIME.FLOOR.PAIRCORR.01 -- the "
          "corner route's perimeter fully surveyed and typed.")
    print("[%s] PATTERN GATE: expected 19 + 17 + 3 checks, 0 failed, "
          "verdicts DOORS-CLOSED + LEVEL2-CLOSED (got %s + %s)"
          % ("PASS" if pattern_ok else "FAIL",
             _VERDICTS.get("a"), _VERDICTS.get("b")))
    return rc + (0 if pattern_ok else 1)


if __name__ == "__main__":
    raise SystemExit(run())
