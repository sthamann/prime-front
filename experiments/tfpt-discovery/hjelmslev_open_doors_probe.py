#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""hjelmslev_open_doors_probe -- PRIME.CORNER.OPENDOORS.01 (EXPLORATION
ONLY, experiments/; the class-map completion of the character-corner
channel class: the two typed open doors of POSITION-KRAUS-TRADEOFF,
2026-08-07).

THE INPUT FINDINGS (frozen, read-only):
  * CORNER-IDENTITY-SYMBOLIC (character_corner_probe): the corner
    identity T_GL1,X = V* e_GL1 pi(P(w)) e_GL1 V holds weight-
    generically; chat_j = -1 EXACT for every deployed event; the
    structural positivity is comb-blind -- the arithmetic lives in the
    IDENTIFICATION step.
  * POSITION-KRAUS-TRADEOFF (hjelmslev_position_kraus_probe): within
    register-side leg dressings the GL1 corner reads ONLY the total
    carrier mass; dressings are either identity-preserving-but-corner-
    invisible (unital) or placement-sensitive-but-identity-breaking
    (raw); the m = 1 carrier supports exactly ONE placement scalar.
    OPEN DOORS TYPED THERE: (1) dressings acting on the lag/window
    tensor FACTOR itself; (2) corners at characters NON-trivial on V.

THE TASK (frozen): test both doors and deliver THE COMPLETE CLASS MAP
(dressing side x character class) -> {identity, visibility, placement-
sensitivity}.  A cell carrying ALL THREE is a named identification
carrier (the route reopens; report prominently).  An EMPTY map is the
structural closure candidate: no corner of the group algebra of
G = C2 x F2^4 x Z4 simultaneously carries the deployed-form identity
and the identification -- exact quantifier typed; stop-list entry
candidate.

DOOR 1 -- LAG-FACTOR DRESSING.  The packet operator lives on
H_h (x) l^2(G); the corner compresses the register side to the rank-1
e_chi and the FACTOR side through the deployed lock pair (t1, t2).
THE CHEAP DECISIVE CHECK FIRST: does the GL1 corner trace out the
factor completely (corner functional = a multiple of tr)?  If yes,
factor dressings are invisible and Door 1 closes in one paragraph.
If not (expected: the corner reads t_i^T A t_k, a 2x2 COMPRESSION,
not a trace), dress the factor with comb lag data -- TWO PREDECLARED
VARIANTS, both single-Kraus conjugations a -> (D (x) 1) a (D (x) 1)*:
  D1a  tent-read masses as factor multipliers: D = diag(1 + k fhat),
       fhat = the per-coordinate tent-read mass profile of the comb,
       f_i = -sum_j lam_j diag_i(R_j), normalized to [-1, 1]; k = 1/4.
  D1b  lag phases as factor unitaries: U = diag(exp(i pi k ghat)),
       g_i = sum_j lam_j sin((i+1) pi u_j / (2 alpha)) (the sine reads
       of the comb at the window's internal frequencies), ghat
       normalized to [-1, 1]; k = 1/4.
GATES per variant: (a) CP survives (single-Kraus Choi = |vec D><vec D|
>= 0, verified entrywise on the leading 2x2 reduction; D1a min entry
> 0; D1b unitarity exact to float); (b) corner identity of the
deployed form weight-generic: defect coefficients (constant:
|B - tB_dressed|; per free weight w_j: |chat_j q'_j - X_j|) <= 1e-9 *
scale, else the defect TYPED; (c) placement sensitivity: delta =
lambda_min(dressed block) - tau0 moves AND differs under the scramble
(seed 1) and the Epstein comb (first ka sums of two squares), fields
rebuilt per position set.  CONTROLS: the commutant dressing D_perp =
1 + k P_perp F P_perp (P_perp = the orthocomplement of span(t1, t2)):
identity-preserving AND corner-invisible exactly; the 24-draw sweep
(12 generic diagonal fields, 12 perp-compressed; LCG 20260807):
identity defect <= bar <=> corner block unmoved (the dichotomy across
the class).

DOOR 2 -- V-NONTRIVIAL CHARACTERS.  All 128 characters chi =
(eps, w, j) of G enumerated; the 120 with w != 0 are the door.  THE
TYPED SYMMETRY REDUCTION (verified EXACTLY, all 128 characters x all
union events, full carrier Fourier in Fractions): chat_j(chi) =
(-1)^eps * Vfac(w; channel) * Mfac(j; n) with Vfac = (1/7) sum_{v in
H*} (-1)^{w.v} in {1 (w in Hperp = {0, w0}), -1/7 (the other 14)} for
ram-odd events and 1 otherwise; Mfac(0) = 1, Mfac(1) = Mfac(3) =
(Th0 - Th2)/(240 sigma3), Mfac(2) = (Th0 - Th1 + Th2 - Th3)/(240
sigma3).  Hence 128 characters collapse to 18 classes (eps x wclass in
{0, w0, other} x jclass in {0, {1,3}, 2}); the class-rep table is the
predeclared symmetry-reduced set.  Per class rep: e_chi projector ward
(exact complex-Fraction convolution: idempotent, self-adjoint, rank 1
= Fourier delta); the chat_j spectrum over all union events (which
events survive, zeros counted); gate (a) identity of the deployed
form at chi (<=> chat_j = -1 for all j -- measured, not assumed);
gate (b) WHAT the chi-corner reads (the mass ward generalized): the
w-Fourier mode of the carrier V-slot times the j-mode of the glue
distribution times the C2 sign -- linear functionals of the event
weights with POSITION-BLIND coefficients (the carrier map n ->
sigma(x_n) never reads u_j; verified: the register-dressed
generalized ward on the full 128-dim register, and chat bit-identical
under the scramble); gate (c) placement sensitivity of the chi-excess
delta_chi = lambda_min(T_chi) - tau0 under scramble/Epstein.

THE CLASS MAP (frozen): rows = dressing side in {none, register-
unital (A' of the tradeoff probe, rebuilt), register-raw (C, rebuilt),
factor-mass D1a, factor-phase D1b}; columns = the 18 character
classes; cells = (identity, visibility, placement) with identity =
max defect coeff <= 1e-9 scale, visibility = max entry |block_cell -
block_GL1,undressed| > 1e-9 scale, placement = |delta - delta_scr| >
1e-9 AND |delta - delta_eps| > 1e-9.  Register rows at chi use the
dressed carrier Fourier chat'_j = (-1)^eps Fw(p'_pi) Mfac (kernels
rebuilt per position set, v2 mass-normalized placement-scalar field).

FROZEN VERDICTS: DOORS-CARRY (a cell carries all three) /
DOORS-CLOSED (both doors typed closed: every identity cell is
invisible, every visible cell pays the identity defect; the exact
quantifier: for every cell of the map, identity ==> the corner block
== the deployed window form ==> zero excess) / DOORS-PARTIAL (typed
per door).  MANDATORY CONTROLS: the GL1 column reproduces chat_j = -1
exactly (Fractions, all union events); the undressed corner reduction
reproduces tau_X on all 3 windows; the register-side tradeoff
regression (A' identity + zero excess; C defect + moving excess);
projector wards per class rep; scramble/Epstein per cell as designed.

HONESTY GATES: NO RH claim anywhere; nothing outside experiments/
touched; no file written; no marker moves; stop-list respected (no
signed-prime-sum estimation; v831 / PRIME.FLOOR.PAIRCORR.01 binding).
FIREWALL: no zeta zero, no prime-table symbol (AST-checked; own
sieves); machinery imports READ-ONLY: v563 (windows), v738 (frame).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/hjelmslev_open_doors_probe.py
"""

import ast
import hashlib
import math
import os
import sys
import time
from fractions import Fraction as Fr
from itertools import combinations

import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
_VERIFY = os.path.abspath(os.path.join(_HERE, "..", "..", "verification"))
sys.path.insert(0, _HERE)
sys.path.insert(0, _VERIFY)

import v563_paper2_readouts as core        # noqa: E402  (READ-ONLY)
import v738_hecke_mod_ramified as ram      # noqa: E402  (READ-ONLY)

FROZEN_SPEC = """\
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

N_TH = 640
N_WIN = 3
KAPPA = 0.25
BAR_COEF_REL = 1.0e-9
BAR_ID_REL = 1.0e-6
BAR_MOVE = 1.0e-9
BAR_EXACT = 1.0e-12
SCR_SEED = 1
N_SWEEP_GEN = 12
N_SWEEP_PERP = 12
REG_REFS = {9: (4.813726e-3, 5.984165e-4),
            12: (3.227697e-3, 4.351189e-4),
            13: (2.954471e-3, 5.637632e-4)}
REG_BAR = 1.0e-4
BANNED_IDS = ("zetazero", "nzeros", "primerange", "isprime", "primepi",
              "nextprime", "prevprime")

CHECKS = []
FAILS = []
CONTROL = {}
T0 = time.time()
_LCG = [20260807]


def lcg_float():
    _LCG[0] = (1103515245 * _LCG[0] + 12345) % (1 << 31)
    return _LCG[0] / float(1 << 31)


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


# ============================================================ group layer
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


# ===================================================== arithmetic layer
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


def sum2sq_positions(count):
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


# ========================================================== label frame
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


# ============================================================== carriers
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


# ============================================================== windows
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


def reads_multi(rr, rows, V):
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


def fam3(G2, i, k):
    """(00, 11, 01) slots of the (i, k) vector family from a Gram."""
    return np.array([G2[i, i].real, G2[k, k].real, G2[i, k]],
                    dtype=np.complex128)


def blk2(tBf, cvec, lam, q3):
    """2x2 hermitian corner block: tB - sum_j c_j lam_j q_j."""
    s0 = float(np.sum(cvec * lam * q3[:, 0].real))
    s1 = float(np.sum(cvec * lam * q3[:, 1].real))
    sx = complex(np.sum(cvec * lam * q3[:, 2]))
    b01 = tBf[2] - sx
    return np.array([[tBf[0] - s0, b01],
                     [np.conj(b01), tBf[1] - s1]])


def id_dev(tBf, cvec, q3, B, Xn):
    """Max defect coefficient of (deployed form) - (cell corner) in
    free weights: constant slots + per-w_j slots."""
    d = max(abs(B[0, 0] - tBf[0]), abs(B[1, 1] - tBf[1]),
            abs(B[0, 1] - tBf[2]))
    for s in range(3):
        d = max(d, float(np.max(np.abs(cvec * q3[:, s]
                                       - Xn[:, s]))))
    return d


# ============================================== register-dressing layer
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


# ================================================================= main
def main():
    section("PRIME.CORNER.OPENDOORS.01 -- the two open doors of the "
            "character-corner channel class (EXPLORATION ONLY)")
    sha = hashlib.sha256(FROZEN_SPEC.encode("utf-8")).hexdigest()
    print("    FROZEN_SPEC SHA-256 = %s" % sha)
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
        q, Ga = reads_multi(rr, rows, V0)
        q3 = np.stack([fam3(q[j], 0, 1) for j in range(len(nv))])
        tBf = (Ga[0, 0].real, Ga[1, 1].real, Ga[0, 1])
        tau_X = float(np.linalg.eigvalsh(rr["Ah"])[0])
        A0 = blk2(tBf, -np.ones(len(nv)), rr["lam"], q3)
        tau0 = float(np.linalg.eigvalsh(A0)[0])
        scale = max(1.0, float(np.max(np.abs(A0))))
        ok_id &= abs(tau0 - tau_X) / scale <= BAR_ID_REL
        ref = REG_REFS.get(kz)
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
    uu_e = sum2sq_positions(ka0)
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
    qG_t, Ga_t = reads_multi(rr0, rows_t, V_t)
    qG_s, Ga_s = reads_multi(rr0, rows_s, V_s)
    qG_e, Ga_e = reads_multi(rr0, rows_e, V_e)

    def fam_data(qG, Ga, i, k):
        q3 = np.stack([fam3(qG[j], i, k) for j in range(ka0)])
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
    blk_gl1 = {"t": blk2(tB_t, cm1, lam0, q3_t),
               "s": blk2(tB_s, cm1, lam0, q3_s),
               "e": blk2(tB_e, cm1, lam0, q3_e)}
    tau0_pi = {p: float(np.linalg.eigvalsh(blk_gl1[p])[0])
               for p in ("t", "s", "e")}

    def cell_measure(tB3, q33, cvec3):
        """(identity dev, visibility bdiff, delta triple) for a cell
        given per-position-set (tB, q3) dicts and cvec dict."""
        dev = id_dev(tB3["t"], cvec3["t"], q33["t"], B0, Xn0)
        bt = blk2(tB3["t"], cvec3["t"], lam0, q33["t"])
        bd = float(np.max(np.abs(bt - blk_gl1["t"])))
        deltas = {}
        for p in ("t", "s", "e"):
            bp = blk2(tB3[p], cvec3[p], lam0, q33[p])
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
        dev = id_dev(tBd, cm1, q3d, B0, Xn0)
        bd = float(np.max(np.abs(blk2(tBd, cm1, lam0, q3d)
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
    return 0 if (n_pass == len(CHECKS) and controls_ok) else 1


if __name__ == "__main__":
    raise SystemExit(main())
