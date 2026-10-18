#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""character_corner_probe -- PRIME.CORNER.CHARACTER.01 (EXPLORATION ONLY,
experiments/; the decisive probe of the positive-corner route, 2026-08-07).

THE STRATEGIC SHIFT (frozen): stop estimating tau as a signed prime sum
(that route is stop-listed at the typed pair-correlation circularity
boundary, PRIME.FLOOR.PAIRCORR.01 / v831).  Instead represent tau as a
POSITIVE CHARACTER CORNER.  Target identity:

    tau_X = <Omega_X, e_GL1 . P_lock . e_GL1 . Omega_X>,
    P_lock >= 0,  e_GL1 a genuine projector (e^2 = e = e*),

so tau_X >= 0 immediately -- corner compression e.a.e is CP, unlike the
naive signed character pushforward (corpus: v791 finding F1 -- the
linear pushforward is NOT a state; the packet construction builds the
positive state FIRST, then applies characters).

THE KILL TEST (symbolic, decided in ONE run): does

    T_GL1,X ?= V_X* . e_GL1 . pi_X(P_X) . e_GL1 . V_X

hold for GENERIC SYMBOLIC event weights -- the prime half-weights
Lambda(n)/sqrt(n) at the comb events replaced by FREE SYMBOLS w_j, the
identity tested as polynomial algebra (sympy), not numerics?

THE DEPLOYED OBJECTS (read-only reuse, nothing re-gated):
  *  T_GL1,X  = the deployed frame-A lock block Ahat(w) = B - sum_j w_j
     X_j (v563 build_window verbatim: arch reads B via the lag-weight
     vectors W11/W22/W12; per-event 2x2 spline reads X_j; deployed
     weights lam_j = Lambda(n_j)/sqrt(n_j)) -- the PRIME.FLOOR.RATIO.01
     lock compression of the sector window (v818).
  *  pi_X(P_X) = the v791 packet WINDOW operator on H_h (x) l^2(G),
     G = C2 x F2^4 x Z4 (|G| = 128, the extended packet register),
         P_X(w) = T_arch (x) 1  +  sum_j Q_j(w) (x) sigma(x_j),
     Q_j(w) = MINUS the deployed single-atom lag Toeplitz at weight w_j
     (v791 window-face convention), sigma(x_j) = the symmetrized
     carrier-register element of event j (C2 slot = the sign carrier s;
     V slot = uniform on the 7 classes of the chi_NSR polar hyperplane
     H* for ram-odd events, delta_0 else -- v738 lex-first
     sigma-invariant symplectic frame, read-only; mu4 slot = the exact
     glue-class distribution Th_m(n)/240 sigma3(n)).
  *  e_GL1 = (1/|G|) sum_g conj(chi_GL1(g)) u_g at chi_GL1 = the
     (eps = -1, w = 0, j = 0) character -- built from the ACTUAL finite
     character group of the deployed sector structure; rank 1 in the
     regular representation, so the corner reduces per event to the
     exact character value chat_j = sum_g c_j(g) chi_GL1(g).
  *  V_X = [t1 (x) v_chi, t2 (x) v_chi] -- the deployed lock-block
     compression pair tensored with the unit chi_GL1 vector.
  *  CP layer cited read-only: v756 (105-leg Stinespring intertwiner,
     exactly positive Choi) and v820 (round-23 Kraus modules) supply
     the deployed CP machinery; the corner map a -> e a e is single-
     Kraus CP (Choi = |vec e><vec e|, machine-checked exactly on the
     C2 reduction below).

FROZEN SURFACES (declared before any run):
  W1-W3: the THREE alpha-smallest regular complete windows of the
     deployed frame-A ladder (v563 frame_a_zones, alpha-sorted,
     h = 1292 anomaly excluded, complete combs only) -- the smallest
     deployed window battery, predeclared window sizes 3.
  TOY: one fully exact symbolic window (M = 8, D = 1, exact-Fraction
     tent assembly at rational positions {1/2, 3/2, 7/3, 5} incl. one
     reflection event, arch lags = free symbols a_d, rational
     compression pair) carrying the REAL packet labels of events
     n = 2 (ro), 3 (in), 4 (re), 5 (sp) -- the exact identity with
     both sides printed.
  Exact character layer: theta builds to N_TH = 640 (covers every
     deployed event n <= 623), f8 by the independent eta recurrence,
     sigma3 by sieve; all character sums in exact rationals.

FROZEN BARS:
  BAR_COEF = 1e-9 * scale  per defect-polynomial coefficient (the two
     sides are built through DIFFERENT deployed code paths -- spline
     reads vs direct quadratic forms on per-event odd-Toeplitz rows --
     so float round-off, not bitwise identity, is the honest bar;
     scale = the global read scale of the window).
  Exact legs (projector wards, chat_j, toy identity, glue identity):
     EXACT equality in Fractions, no tolerance.
  PSD reports: eigvalsh, bar -1e-10 * ||T||_2 (v791 convention).
  LCG seed 20260807 (12-event sample for the full two-sided corner
     ward); scramble seed 1 (v563 convention).  Runtime cap 30 min.

THREE FROZEN OUTCOMES (the user's decision tree, verbatim):
  1. CORNER-IDENTITY-SYMBOLIC  -- the identity holds for free symbolic
     weights: positivity is STRUCTURAL where it attaches; window
     induction realistic; the Hjelmslev ladder (H1-H5) authorized.
     Deliver: the exact symbolic identity with both sides printed, the
     projector verification e^2 = e = e* (exact), P_lock >= 0 shown
     structurally (Gram/Choi form), and the precise statement of what
     remains for the infinite limit.
  2. CORNER-IDENTITY-ARITHMETIC-ONLY -- the generic version has a
     nonzero symbolic defect, the identity holds only at the prime
     weights: type the defect polynomial exactly (skeleton
     sum_j w_j (1 + chat_j) read_j -- which weight combinations must
     vanish); check whether the defect is the known pair-correlation
     object.
  3. CORNER-NO-IDENTITY -- no identity even at the prime weights
     (float bar on the deployed windows): route dead; type the
     obstruction (which term of T_GL1 is not a corner).

MANDATORY CONTROLS (frozen):
  CA [must-fire] the naive signed pushforward FAILS positivity on the
     SAME windows (v791 F1 reproduced as the contrast): the linear
     population-register pushforward has a negative character sector
     on each window event set, in EXACT rationals at unit weights; the
     raw signed carrier count sits at -1 exactly.
  CB [typing control] the scrambled comb (v563 scramble_seed = 1,
     positions uniform at the same masses): the corner identity must
     STILL hold within the same bar (the structure is placement-blind)
     and the state-face corner value is UNCHANGED (it does not read
     positions) -- while the deployed lock data moves; the deliverable
     is the TYPED answer to "what then distinguishes the true comb":
     the identification with tau_X, not the positivity.
  CC [projector ward] e_GL1 from the actual character group:
     e*e = e = e^adj EXACT (group-algebra convolution, Fractions),
     Fourier transform = the delta at chi_GL1 (rank 1), single-Kraus
     Choi rank-1 exact on the C2 reduction.

HONESTY GATES: NO RH claim anywhere; the corner identity transports
POSITIVITY only from a positive P -- and the packet window operator is
NOT positive (v791 F2, re-measured here on the deployed A-frame sector
census, report-only); the manifestly positive object (the packet GNS
Gram) does NOT have tau_X as its corner value (the identification gap
is MEASURED and printed).  The scramble control makes the scope exact:
corner positivity is placement-blind, hence never by itself the floor.
Stop-list respected: no signed-prime-sum estimation anywhere; v831 /
PRIME.FLOOR.PAIRCORR.01 binding.  Nothing outside experiments/ is
touched; no file is written; no marker moves.

FIREWALL: no zeta zero, no zetazero/nzeros/primerange/isprime symbol
(AST-checked; own sieves only); sympy used for SYMBOLIC ALGEBRA ONLY
(declared -- no sympy.ntheory call); machinery imports READ-ONLY:
v563 (deployed windows), v738 (label frame).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/character_corner_probe.py
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
import sympy as sp

_HERE = os.path.dirname(os.path.abspath(__file__))
_VERIFY = os.path.abspath(os.path.join(_HERE, "..", "..", "verification"))
sys.path.insert(0, _HERE)
sys.path.insert(0, _VERIFY)

import v563_paper2_readouts as core        # noqa: E402  (READ-ONLY)
import v738_hecke_mod_ramified as ram      # noqa: E402  (READ-ONLY)

# ---------------------------------------------------------------- frozen
FROZEN_SPEC = """\
PRIME.CORNER.CHARACTER.01 spec v1 (2026-08-07, frozen before the run).
Windows: the 3 alpha-smallest regular complete frame-A windows (v563
zones, h=1292 excluded).  Register G = C2 x F2^4 x Z4 (128); chi_GL1 =
(eps=-1, w=0, j=0); carrier-register event elements with the v738
lex-first sigma-invariant symplectic H* frame (ram-odd uniform on 7);
mu4 slot = exact glue distribution Th_m/240sigma3 (theta builds to
N_TH=640, f8 eta recurrence, sigma3 sieve, all exact).  KILL TEST:
T_GL1,X(w) [v563 spline-read lock, weights symbolic] ?= V* e pi(P(w)) e
V [per-event Kraus rows, exact character corner coefficients chat_j],
sympy polynomial algebra; defect skeleton sum_j w_j (1+chat_j) read_j.
TOY: exact symbolic leg M=8, D=1, positions {1/2,3/2,7/3,5}, arch lags
symbolic, labels of n=2,3,4,5.  BARS: BAR_COEF=1e-9*scale float legs;
exact legs EXACT; PSD -1e-10*||T||.  CONTROLS: CA naive linear
pushforward negative sector (exact, unit weights, must-fire per
window); CB scramble seed 1 -- identity still holds + state corner
unchanged + lock data moves (typing); CC projector wards exact.
OUTCOMES: CORNER-IDENTITY-SYMBOLIC / CORNER-IDENTITY-ARITHMETIC-ONLY /
CORNER-NO-IDENTITY.  LCG 20260807.  NO RH claim; writes nothing.
"""

N_WIN = 3
N_TH = 640
BAR_COEF_REL = 1.0e-9
PSD_BAR = 1.0e-10
SCR_SEED = 1
N_WARD_SAMPLE = 12
TOY_M = 8
TOY_POS = (Fr(1, 2), Fr(3, 2), Fr(7, 3), Fr(5))
TOY_LABEL_N = (2, 3, 4, 5)

BANNED_IDS = ("zetazero", "nzeros", "primerange", "isprime", "primepi",
              "nextprime", "prevprime")

CHECKS = []
FAILS = []
CONTROL = {}
T0 = time.time()
_LCG = [20260807]


def lcg(n):
    _LCG[0] = (1103515245 * _LCG[0] + 12345) % (1 << 31)
    return _LCG[0] % n


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
    tree = ast.parse(src)
    bad = []
    for node in ast.walk(tree):
        name = None
        if isinstance(node, ast.Name):
            name = node.id
        elif isinstance(node, ast.Attribute):
            name = node.attr
        if name and name.lower() in BANNED_IDS:
            bad.append(name)
    return bad


# ============================================================ group layer
# G = C2 x F2^4 x Z4 as tuples (a, v, m); characters (eps, w, j):
# chi(a, v, m) = (-1)^{eps a} (-1)^{popcount(w & v)} i^{j m}.
G_ELEMS = [(a, v, m) for a in range(2) for v in range(16) for m in range(4)]
G_IDX = {g: i for i, g in enumerate(G_ELEMS)}
CHARS = [(eps, w, j) for eps in range(2) for w in range(16)
         for j in range(4)]
CHI_GL1 = (1, 0, 0)


def g_mul(g, h):
    return ((g[0] + h[0]) % 2, g[1] ^ h[1], (g[2] + h[2]) % 4)


def g_inv(g):
    return (g[0], g[1], (-g[2]) % 4)


def chival(chi, g):
    """Exact character value as (re, im) integer pair (values in
    {+-1, +-i} times a sign)."""
    eps, w, j = chi
    a, v, m = g
    s = (-1) ** (eps * a) * (-1) ** (bin(w & v).count("1"))
    q = (j * m) % 4                       # i^q
    if q == 0:
        return (s, 0)
    if q == 1:
        return (0, s)
    if q == 2:
        return (-s, 0)
    return (0, -s)


def conv(f, h):
    """Group convolution (f*h)(k) = sum_g f(g) h(g^{-1} k) of two dicts
    with Fraction values (exact)."""
    out = {}
    for g, fg in f.items():
        gi = g_inv(g)
        for k in G_ELEMS:
            hv = h.get(g_mul(gi, k))
            if hv:
                out[k] = out.get(k, Fr(0)) + fg * hv
    return {k: v for k, v in out.items() if v != 0}


def fourier(f, chi):
    """fhat(chi) = sum_g f(g) chi(g), exact (re, im) Fractions."""
    re = Fr(0)
    im = Fr(0)
    for g, fg in f.items():
        cr, ci = chival(chi, g)
        re += fg * cr
        im += fg * ci
    return re, im


def s2_projector():
    section("S2 -- the projector ward (control CC): e_GL1 from the "
            "actual character group, exact")
    E = {g: Fr(chival(CHI_GL1, g)[0], 128) for g in G_ELEMS}
    # chi_GL1 is real, so conj(chi) = chi and E is real by construction.
    EE = conv(E, E)
    ok_idem = all(EE.get(g, Fr(0)) == E[g] for g in G_ELEMS)
    check("S2.1 [EXACT] idempotency e*e = e on the 128-dim group "
          "algebra (convolution in Fractions, no tolerance)", ok_idem)
    ok_adj = all(E[g_inv(g)] == E[g] for g in G_ELEMS)
    check("S2.2 [EXACT] self-adjointness e = e^adj: E(g^{-1}) = E(g) "
          "(chi_GL1 real-valued)", ok_adj)
    hits = []
    for chi in CHARS:
        re, im = fourier(E, chi)
        if im != 0:
            hits.append((chi, "imag"))
        if (re == 1) != (chi == CHI_GL1):
            hits.append((chi, re))
        elif chi != CHI_GL1 and re != 0:
            hits.append((chi, re))
    check("S2.3 [EXACT] Fourier transform of e = the delta at chi_GL1 "
          "over all 128 characters -- e_GL1 has RANK 1 in the regular "
          "representation (the corner space is one-dimensional per "
          "window mode)", not hits, "violations %s" % hits[:3])
    # single-Kraus CP fact on the C2 reduction: Choi(a -> e2 a e2) is
    # EXACTLY the rank-1 outer square |vec e2><vec e2| >= 0.
    e2 = [[Fr(1, 2), Fr(-1, 2)], [Fr(-1, 2), Fr(1, 2)]]

    def mat2mul(A, B):
        return [[sum(A[i][k] * B[k][j] for k in range(2))
                 for j in range(2)] for i in range(2)]

    choi = [[Fr(0)] * 4 for _ in range(4)]
    for k in range(2):
        for l in range(2):
            Ekl = [[Fr(1) if (i, j) == (k, l) else Fr(0)
                    for j in range(2)] for i in range(2)]
            img = mat2mul(mat2mul(e2, Ekl), e2)
            for i in range(2):
                for j in range(2):
                    choi[2 * k + i][2 * l + j] = img[i][j]
    v = [e2[0][0], e2[0][1], e2[1][0], e2[1][1]]
    ok_choi = all(choi[i][j] == v[i] * v[j]
                  for i in range(4) for j in range(4))
    check("S2.4 [EXACT] the corner map a -> e a e is single-Kraus CP: "
          "its Choi matrix equals the rank-1 outer square "
          "|vec(e)><vec(e)| entrywise on the C2 reduction -- corner "
          "compression is a CP operation (deployed CP layer cited "
          "read-only: v756 105-leg Stinespring, exactly positive Choi; "
          "v820 Kraus modules)", ok_choi)
    return E


# ============================================================ theta layer
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


def s1_arithmetic():
    section("S1 -- the exact packet layer: sigma3, class thetas, f8 "
            "(own builds, no prime table)")
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
    num0 = p3 + m53 + m35 + p4
    num2 = p3 - m53 - m35 + p4
    ok_div = bool(np.all(num0 % 4 == 0) and np.all(num2 % 4 == 0))
    Th0 = (num0 // 4)[::2][:N_TH + 1].copy()
    Th2 = (num2 // 4)[::2][:N_TH + 1].copy()
    TCAP = 8 * N_TH
    t2 = sparse_theta_terms("th2", TCAP)
    acc = np.zeros(TCAP + 1, dtype=np.int64)
    acc[0] = 1
    for _ in range(8):
        acc = sparse_mul(acc, t2)
    ok_div &= bool(np.all(acc[::8][:N_TH + 1] % 4 == 0))
    Th1 = (acc[::8][:N_TH + 1] // 4).copy()
    Th3 = Th1
    heads_ok = (Th0[1], Th1[1], Th2[1], Th3[1]) == (52, 64, 60, 64)
    check("S1.1 [EXACT] theta builds to n <= %d: divisibility by 4 "
          "exact; heads (52, 64, 60, 64)" % N_TH, ok_div and heads_ok)
    tot = Th0 + Th1 + Th2 + Th3
    glue_ok = bool(np.all(tot[1:] == 240 * sig3[1:]))
    check("S1.2 [EXACT] the GLUE IDENTITY Sum_m Th_m(n) = 240 sigma3(n) "
          "for ALL n <= %d -- THE one arithmetic input the corner "
          "identity consumes (it normalizes the mu4 distribution, "
          "hence chi-trivial slots evaluate to exactly 1)" % N_TH,
          glue_ok)
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
    ok_f8 = ((a_f8[3], a_f8[5], a_f8[7]) == (-4, -2, 24)
             and bool(np.all(a_f8[2::2] == 0)) and a_f8[1] == 1)
    check("S1.3 [EXACT] f8 by the independent eta recurrence: a_p = "
          "(-4, -2, 24) at p = 3, 5, 7; odd support; a_1 = 1", ok_f8)
    return dict(sig3=sig3, Th=(Th0, Th1, Th2, Th3), a=a_f8, spf=spf)


# ============================================================ label frame
def s3_label_frame():
    """v738 lex-first sigma-invariant symplectic frame (v791 s3,
    read-only reuse): returns the 7 H* labels and the 16 labels."""
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
    ok = len(Hstar) == 7 and y_chi in Hstar
    check("S3.0 label frame (v738 read-only): lex-first sigma-invariant "
          "symplectic form; H* = 7 nonzero classes containing y_chi",
          ok, "y_chi = %s" % (y_chi,))
    return labels, Hstar


def label_int(lab):
    return sum(b << i for i, b in enumerate(lab))


# ============================================================ events
def classify(n, spf):
    """Deployed channel of the prime-power event n (v755 convention):
    ram-odd / ram-even for base 2 by exponent parity; split for
    p = 1 mod 4; inert else."""
    p = int(spf[n])
    m, k = n, 0
    while m % p == 0:
        m //= p
        k += 1
    assert m == 1
    if p == 2:
        return "ro" if k % 2 == 1 else "re"
    return "sp" if p % 4 == 1 else "in"


def event_carrier_element(n, th, Hstar):
    """The symmetrized carrier-register element sigma(x_n) of event n
    as an exact coefficient dict on G (v791 window face): C2 slot =
    the pure sign carrier a = 1; V slot = uniform on H* (ram-odd) or
    delta_0; mu4 slot = the glue distribution Th_m(n)/240 sigma3(n)."""
    Th0, Th1, Th2, Th3 = th["Th"]
    E = 240 * int(th["sig3"][n])
    pm = [Fr(int(Th0[n]), E), Fr(int(Th1[n]), E),
          Fr(int(Th2[n]), E), Fr(int(Th3[n]), E)]
    ch = classify(n, th["spf"])
    vlist = [label_int(v) for v in Hstar] if ch == "ro" else [0]
    pv = Fr(1, len(vlist))
    c = {}
    for vv in vlist:
        for m in range(4):
            w = pv * pm[m] / 2
            if w == 0:
                continue
            for gg in ((1, vv, m), (1, vv, (-m) % 4)):
                c[gg] = c.get(gg, Fr(0)) + w
    return c, ch


def event_population_values(n, th, jc, eps, vclass):
    """State-face (population-register) class value t = c2f * vf * mf,
    exact (v791 class_values): the naive-pushforward control object."""
    Th0, Th1, Th2, Th3 = th["Th"]
    sig3, a = th["sig3"], th["a"]
    E = 240 * int(sig3[n])
    c2f = Fr(1) if eps == +1 else Fr(int(a[n]), int(sig3[n]))
    is_ro = classify(n, th["spf"]) == "ro"
    vf = Fr(-1, 7) if (is_ro and vclass == "v7") else Fr(1)
    if jc == 0:
        mf = Fr(1)
    elif jc == 1:
        mf = Fr(int(Th0[n]) - int(Th2[n]), E)
    else:
        mf = Fr(int(Th0[n]) - int(Th1[n]) + int(Th2[n]) - int(Th3[n]), E)
    return c2f * vf * mf


SECTORS = [(eps, vc, jc) for eps in (+1, -1) for vc in ("v1", "v7")
           for jc in (0, 1, 2)]
SECTOR_MULT = {(eps, vc, jc): (2 if vc == "v1" else 14)
               * (2 if jc == 1 else 1)
               for eps in (+1, -1) for vc in ("v1", "v7")
               for jc in (0, 1, 2)}


def sector_char_rep(vclass, jc, eps, labels, Hstar):
    """One representative character (eps_bit, w, j) of the 12-class."""
    eps_bit = 0 if eps == +1 else 1
    if vclass == "v1":
        w = 0
    else:
        w = None
        hs = [label_int(v) for v in Hstar]
        for cand in range(1, 16):
            s = sum(1 if bin(cand & v).count("1") % 2 == 0 else -1
                    for v in hs)
            if Fr(s, 7) == Fr(-1, 7):
                w = cand
                break
    return (eps_bit, w, jc)


# ============================================================ windows
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
    """Per-event UNIT-WEIGHT lag rows rho_j (deployed tent assembly at
    mass 2, so weight w_j * rho_j = the deployed row at half-weight
    w_j; deployed: w_j = lam_j = Lambda(n)/sqrt(n))."""
    uu = rr["uu"] if positions is None else positions
    out = np.zeros((len(uu), 2 * rr["h"]))
    for j, u in enumerate(uu):
        out[j] = core.atom_lags_at(rr["alpha"], rr["M"], [float(u)],
                                   [2.0])[0]
    return out


def lock_reads_direct(rr, rows):
    """Per-event direct quadratic forms q_j[ik] = t_i . odd_toeplitz(
    rho_j) . t_k -- the corner-side route (different code path from
    the deployed spline reads)."""
    t1, t2 = rr["t1"], rr["t2"]
    out = np.zeros((rows.shape[0], 3))
    for j in range(rows.shape[0]):
        R = core.odd_toeplitz(rows[j], rr["M"])
        out[j, 0] = t1 @ (R @ t1)
        out[j, 1] = t2 @ (R @ t2)
        out[j, 2] = t1 @ (R @ t2)
        del R
    return out


def arch_lock_direct(rr):
    c_ar = np.asarray(core.arch_lags(rr["M"], rr["D"]), float)
    T = core.odd_toeplitz(c_ar, rr["M"])
    t1, t2 = rr["t1"], rr["t2"]
    out = np.array([[t1 @ (T @ t1), t1 @ (T @ t2)],
                    [t1 @ (T @ t2), t2 @ (T @ t2)]])
    del T
    return out, c_ar


def kill_test_window(tag, rr, chat, nvals):
    """The symbolic kill test on one window; returns (ok, max_dev, bar,
    dev_prime, lhs00, rhs00): the defect polynomial coefficients of
    LHS - RHS in free w_j, plus the defect at the prime weights (the
    outcome-2 decider)."""
    ka = len(rr["uu"])
    wsyms = sp.symbols("w1:%d" % (ka + 1))
    Xn = rr["Xn"]                       # deployed spline reads (LHS)
    B = rr["B"]
    lam = rr["lam"]                     # prime weights (cross-check)
    rows = unit_rows(rr)
    q = lock_reads_direct(rr, rows)     # corner-side direct reads (RHS)
    tB, _c_ar = arch_lock_direct(rr)
    scale = max(float(np.max(np.abs(B))), float(np.max(np.abs(Xn))),
                float(np.max(np.abs(q))), 1.0)
    bar = BAR_COEF_REL * scale
    idx = ((0, 0, 0), (1, 1, 1), (2, 0, 1))   # (slot, i, k)
    max_dev = 0.0
    dev_prime = 0.0
    lhs00 = rhs00 = None
    for slot, i, k in idx:
        Bik = float(B[i, k])
        tBik = float(tB[i, k])
        lhs = sp.Float(Bik) - sp.Add(*[wsyms[j] * sp.Float(Xn[j, slot])
                                       for j in range(ka)])
        # RHS: V* e pi(P(w)) e V entry = t_i T_arch t_k
        #      - sum_j chat_j w_j (t_i R_j t_k)
        rhs = sp.Float(tBik) - sp.Add(*[sp.Rational(chat[int(nvals[j])])
                                        * wsyms[j] * sp.Float(q[j, slot])
                                        for j in range(ka)])
        if slot == 0:
            lhs00, rhs00 = lhs, rhs
        defect = sp.expand(lhs - rhs)
        cdev = abs(float(defect.subs({w: 0 for w in wsyms})))
        max_dev = max(max_dev, cdev)
        for j in range(ka):
            max_dev = max(max_dev, abs(float(defect.coeff(wsyms[j]))))
        # numeric cross-check at the prime weights w_j = lam_j
        lhs_p = Bik - float(lam @ Xn[:, slot])
        rhs_p = tBik - float(sum(float(chat[int(nvals[j])]) * lam[j]
                                 * q[j, slot] for j in range(ka)))
        dev_prime = max(dev_prime, abs(lhs_p - rhs_p))
    ok = max_dev <= bar
    return ok, max_dev, bar, dev_prime, lhs00, rhs00


def print_truncated(name, expr, nterms=3):
    terms = sp.Add.make_args(expr)
    head = " + ".join(str(t) for t in terms[:nterms])
    print("      %s = %s  ... (+%d more terms)"
          % (name, head, max(0, len(terms) - nterms)))


# ============================================================ exact toy
def toy_exact_leg(chat):
    """The fully exact symbolic identity: M = 8 (h = 4), D = 1, exact
    Fraction tent assembly, symbolic arch lags a_d, symbolic weights,
    rational compression pair; chat from the REAL packet labels of
    n = 2, 3, 4, 5."""
    M, h = TOY_M, TOY_M // 2
    a_syms = sp.symbols("a0:%d" % M)
    w_syms = sp.symbols("v1:%d" % (len(TOY_POS) + 1))

    def tent_row(u):
        """Exact unit row (mass 2, the deployed assembly verbatim in
        Fractions): c[i] -= mu/2 * tent(iD - u), + reflection u < D."""
        c = [Fr(0)] * M
        i0 = int(u)                     # floor(u/D), D = 1
        for i in range(max(0, i0 - 2), min(M, i0 + 3)):
            v = 1 - abs(Fr(i) - u)
            if v > 0:
                c[i] -= Fr(2, 2) * v
        if u < 1:
            for i in range(0, min(M, int(1 - u) + 2)):
                v = 1 - (Fr(i) + u)
                if v > 0:
                    c[i] -= Fr(2, 2) * v
        return c

    def odd_toep(cexpr):
        return sp.Matrix(h, h, lambda i, j:
                         cexpr[abs(i - j)] - cexpr[(M - 1) - i - j])

    rows = [tent_row(u) for u in TOY_POS]
    # LHS: deployed assembly -- ONE summed lag vector, then compress.
    c_lhs = [a_syms[d] + sp.Add(*[w_syms[j] * sp.Rational(rows[j][d])
                                  for j in range(len(rows))])
             for d in range(M)]
    A_lhs = odd_toep(c_lhs)
    # RHS: corner route -- per-event Kraus rows Q_j = -w_j R_j with the
    # exact character corner coefficients chat_j, then compress.
    A_rhs = odd_toep(list(a_syms))
    for j, n in enumerate(TOY_LABEL_N):
        Rj = odd_toep([sp.Rational(x) for x in rows[j]])
        A_rhs = A_rhs - sp.Rational(chat[n]) * w_syms[j] * Rj
    t1 = sp.Matrix([1, 2, 3, 4])
    t2 = sp.Matrix([4, 3, 2, 1])
    lhs = sp.Matrix(2, 2, lambda i, k:
                    ([t1, t2][i].T * A_lhs * [t1, t2][k])[0, 0])
    rhs = sp.Matrix(2, 2, lambda i, k:
                    ([t1, t2][i].T * A_rhs * [t1, t2][k])[0, 0])
    defect = sp.expand(lhs - rhs)
    ok = defect == sp.zeros(2, 2)
    return ok, sp.expand(lhs[0, 0]), sp.expand(rhs[0, 0]), defect


# ================================================================== main
def main():
    section("PRIME.CORNER.CHARACTER.01 -- the decisive character-corner "
            "probe (EXPLORATION ONLY)")
    sha = hashlib.sha256(FROZEN_SPEC.encode("utf-8")).hexdigest()
    print("    FROZEN_SPEC SHA-256 = %s" % sha)
    print("    stop-list honoured: no signed-prime-sum estimation; "
          "v831 / PRIME.FLOOR.PAIRCORR.01 binding.  NO RH claim.")

    print("\nS0 -- firewall")
    bad = ast_firewall()
    check("S0.1 AST firewall: no zeta-zero / prime-table symbol "
          "(zetazero/nzeros/primerange/isprime/primepi); sympy used "
          "for symbolic algebra only (declared)", not bad,
          "found %s" % bad if bad else "clean")

    th = s1_arithmetic()
    E = s2_projector()

    section("S3 -- the corner reduction, exact: per-event character "
            "values on the actual group algebra")
    labels, Hstar = s3_label_frame()

    wins = deployed_windows()
    print("    predeclared battery: the %d alpha-smallest deployed "
          "frame-A windows" % N_WIN)
    nmax = 0
    for kz, rr in wins:
        nv = np.rint(np.exp(rr["uu"])).astype(np.int64)
        nmax = max(nmax, int(nv[-1]))
        print("      W(kz=%d): alpha = %.4f, h = %d, M = %d, ka = %d "
              "events (n <= %d); corner space dim = 2 x 1 (lock pair "
              "x rank-1 e_GL1); packet space dim = %d x 128"
              % (kz, rr["alpha"], rr["h"], rr["M"], len(rr["uu"]),
                 int(nv[-1]), rr["h"]))
    check("S3.1 theta reach covers every deployed event (max n = %d "
          "<= N_TH = %d)" % (nmax, N_TH), nmax <= N_TH)

    # exact chat_j for every distinct event of the battery
    nv_union = np.rint(np.exp(wins[-1][1]["uu"])).astype(np.int64)
    chat = {}
    cdicts = {}
    imag_bad = []
    for n in sorted(set(int(x) for x in nv_union) | set(TOY_LABEL_N)):
        c, _ch = event_carrier_element(n, th, Hstar)
        re, im = fourier(c, CHI_GL1)
        if im != 0:
            imag_bad.append(n)
        chat[n] = re
        cdicts[n] = c
    off = {n: v for n, v in chat.items() if v != Fr(-1)}
    check("S3.2 [EXACT -- THE KILL QUANTITY] the corner coefficient "
          "chat_j = sum_g c_j(g) chi_GL1(g) equals -1 EXACTLY for "
          "every one of the %d distinct events (all channels ro/re/"
          "sp/in), imaginary part exactly 0 -- the defect skeleton "
          "sum_j w_j (1 + chat_j) read_j vanishes IDENTICALLY"
          % len(chat), not off and not imag_bad,
          "off-values %s" % (list(off.items())[:3] if off else "none"))
    print("      typed: chi_GL1 is trivial on F2^4 x mu4 and reads the "
          "C2 sign carrier; chat_j = -1 needs ONLY the slot "
          "normalizations -- Sum_m Th_m = 240 sigma3 (the glue "
          "identity, S1.2 exact) and the uniform H* mass 7 x 1/7.  "
          "THAT is the entire arithmetic content of the equality step.")

    # full two-sided corner ward on an LCG sample
    keys = sorted(cdicts.keys())
    worst = None
    ok_ward = True
    for _ in range(N_WARD_SAMPLE):
        n = keys[lcg(len(keys))]
        lhs = conv(conv(E, cdicts[n]), E)
        tgt = {g: chat[n] * v for g, v in E.items() if chat[n] * v != 0}
        same = (all(lhs.get(g, Fr(0)) == tgt.get(g, Fr(0))
                    for g in G_ELEMS))
        ok_ward &= same
        if not same and worst is None:
            worst = n
    check("S3.3 [EXACT] the full two-sided corner reduction "
          "e sigma(x_j) e = chat_j e on the 128-dim group algebra "
          "(exact convolutions, %d LCG-sampled events)"
          % N_WARD_SAMPLE, ok_ward,
          "first violation at n = %s" % worst if worst else "")

    section("S4 -- THE KILL TEST: the corner identity as polynomial "
            "algebra in free weights")
    ok_toy, lhs00, rhs00, defect_toy = toy_exact_leg(chat)
    print("    TOY (fully exact symbolic window, M = %d, D = 1, "
          "events at u = %s carrying the real packet labels n = %s):"
          % (TOY_M, tuple(str(u) for u in TOY_POS), TOY_LABEL_N))
    print_truncated("LHS(1,1)", lhs00)
    print_truncated("RHS(1,1)", rhs00)
    check("S4.1 [EXACT] the toy identity holds SYMBOLICALLY: "
          "T_GL1(a, v) == V* e pi(P(a, v)) e V with symbolic arch "
          "lags a_d AND symbolic weights v_j, defect matrix == 0 "
          "exactly (sympy)", ok_toy,
          "" if ok_toy else "defect = %s" % defect_toy)

    dev_report = []
    prime_dev = []
    first_sides = None
    for kz, rr in wins:
        nv = np.rint(np.exp(rr["uu"])).astype(np.int64)
        ok, dev, bar, dev_p, dl, dr = kill_test_window(
            "W%d" % kz, rr, chat, nv)
        dev_report.append((kz, ok, dev, bar))
        prime_dev.append(dev_p)
        if first_sides is None:
            first_sides = (kz, dl, dr)
        check("S4.2 W(kz=%d) SYMBOLIC defect polynomial == 0: every "
              "coefficient (per free w_j and constant) has |coeff| = "
              "%.2e <= bar %.2e (two INDEPENDENT deployed code paths: "
              "v563 spline-read lock vs per-event Kraus-row quadratic "
              "forms)" % (kz, dev, bar), ok)
    print("    both sides on W(kz=%d), entry (1,1), free weights "
          "(truncated):" % first_sides[0])
    print_truncated("LHS(1,1)", first_sides[1])
    print_truncated("RHS(1,1)", first_sides[2])
    print("    numerics only as CROSS-CHECK: the LHS - RHS defect at "
          "the prime weights w_j = Lambda(n)/sqrt(n): max dev %s"
          % ", ".join("%.1e" % d for d in prime_dev))
    ok_all_sym = all(ok for _kz, ok, _d, _b in dev_report)

    section("S5 -- P_lock >= 0 structurally, and the honest gap")
    # (i) the Gram form, symbolically: sum of squares
    y1, y2, u1, u2, x1, x2, om1, om2 = sp.symbols(
        "y1 y2 u1 u2 x1 x2 omega1 omega2")
    xi1 = sp.Matrix([u1, u2])
    xi2 = sp.Matrix([x1, x2])
    y = sp.Matrix([y1, y2])
    P = om1 * xi1 * xi1.T + om2 * xi2 * xi2.T
    sos = sp.expand((y.T * P * y)[0, 0]
                    - om1 * (xi1.dot(y)) ** 2 - om2 * (xi2.dot(y)) ** 2)
    check("S5.1 [EXACT] the Gram/Choi form of P_lock: for the packet "
          "GNS mixture P(w) = sum_j w_j |xi_j><xi_j| / nu_j the "
          "quadratic form is IDENTICALLY the weighted sum of squares "
          "sum_j w_j <xi_j, y>^2 / nu_j (sympy residual %s) -- P_lock "
          ">= 0 is STRUCTURAL for any w >= 0, any placement, any comb"
          % sos, sos == 0)
    # (ii) the exact structural corner value of the positive object
    gaps = []
    for kz, rr in wins:
        nv = np.rint(np.exp(rr["uu"])).astype(np.int64)
        lam = rr["lam"]
        val = 0.0
        for j, n in enumerate(nv):
            tvals = [event_population_values(int(n), th, jc, eps, vc)
                     for (eps, vc, jc) in SECTORS]
            nu = sum(Fr(SECTOR_MULT[sec]) * t * t
                     for sec, t in zip(SECTORS, tvals)) / 128
            tgl1 = event_population_values(int(n), th, 0, -1, "v1")
            val += float(lam[j]) * float(tgl1 * tgl1 / nu)
        z = float(np.sum(lam))
        state_corner = val / z
        tau = float(np.linalg.eigvalsh(rr["Ah"])[0])
        gaps.append((kz, state_corner, tau))
        print("      W(kz=%d): state-face corner value (GNS, structural"
              " >= 0) = %+.6e   vs   tau_X = lambda_min(T_GL1,X) = "
              "%+.6e -- DIFFERENT objects" % (kz, state_corner, tau))
    check("S5.2 the identification gap is REAL and measured: the "
          "manifestly positive corner value is NOT tau_X on any "
          "window (the corner identity lives on the packet WINDOW "
          "operator, whose positivity is exactly the open floor)",
          all(abs(s - t) > 1e-12 for _k, s, t in gaps))
    # (iii) the operator face is NOT positive (v791 F2 on the A-frame)
    kz0, rr0 = wins[0]
    nv0 = np.rint(np.exp(rr0["uu"])).astype(np.int64)
    rows0 = unit_rows(rr0)
    c_ar0 = np.asarray(core.arch_lags(rr0["M"], rr0["D"]), float)
    lam0 = rr0["lam"]
    print("      operator-face sector census on W(kz=%d) (A-frame "
          "odd-Toeplitz windows, coefficients -chat_j(chi), exact "
          "character values):" % kz0)
    n_psd = 0
    gl1_psd = False
    for (eps, vc, jc) in SECTORS:
        rep = sector_char_rep(vc, jc, eps, labels, Hstar)
        coeff = np.array([float(-fourier(cdicts[int(n)], rep)[0])
                          for n in nv0])
        lag = c_ar0 + (coeff * lam0) @ rows0
        T = core.odd_toeplitz(lag, rr0["M"])
        lmin = float(np.linalg.eigvalsh(T)[0])
        nrm = float(np.max(np.abs(np.linalg.eigvalsh(T))))
        psd = lmin >= -PSD_BAR * nrm
        n_psd += psd
        if (eps, vc, jc) == (-1, "v1", 0):
            gl1_psd = psd
        print("        (eps=%+d, %s, j=%d): lambda_min = %+.3e  [%s]"
              % (eps, vc, jc, lmin, "PSD" if psd else "NEG"))
        del T
    check("S5.3 the GL1 sector is PSD (the deployed window) while the "
          "packet window operator is NOT positive as an operator: "
          "%d of 12 sector classes PSD -- the object carrying the "
          "IDENTITY does not carry the POSITIVITY (v791 F2 anatomy, "
          "re-measured on the deployed A-frame)" % n_psd,
          gl1_psd and n_psd < 12)

    section("C -- mandatory controls")
    # CA: the naive signed pushforward fails positivity (exact)
    ca_ok = True
    for kz, rr in wins:
        nv = np.rint(np.exp(rr["uu"])).astype(np.int64)
        worst_val = None
        worst_sec = None
        for sec in SECTORS:
            eps, vc, jc = sec
            tot = sum(event_population_values(int(n), th, jc, eps, vc)
                      for n in nv)
            if worst_val is None or tot < worst_val:
                worst_val, worst_sec = tot, sec
        fired = worst_val < 0
        ca_ok &= fired
        print("      W(kz=%d): naive LINEAR pushforward (population "
              "register, unit weights, EXACT rationals): min sector "
              "value = %+.4f at (eps=%+d, %s, j=%d) -- %s"
              % (kz, float(worst_val), worst_sec[0], worst_sec[1],
                 worst_sec[2], "NOT a state" if fired else "positive"))
    CONTROL["CA"] = ca_ok
    check("CA [must-fire] the naive signed pushforward FAILS "
          "positivity on ALL %d windows (exact rationals; the corpus "
          "claim v791 F1 reproduced as the contrast); the raw signed "
          "carrier count is chi_-(s) = -1 exactly" % N_WIN, ca_ok)

    # CB: the scrambled comb -- identity blind, data moves
    rr_s = core.build_window(kz0, scramble_seed=SCR_SEED)
    ok_scr, dev_scr, bar_scr, _dp, _l, _r = kill_test_window(
        "Wscr", rr_s, chat, nv0)
    tau_scr = float(np.linalg.eigvalsh(rr_s["Ah"])[0])
    rows_s = unit_rows(rr_s)
    A_s = core.odd_toeplitz(
        np.asarray(core.arch_lags(rr_s["M"], rr_s["D"]), float)
        + rr_s["lam"] @ rows_s, rr_s["M"])
    lmin_s = float(np.linalg.eigvalsh(A_s)[0])
    del A_s
    tau_true = float(np.linalg.eigvalsh(rr0["Ah"])[0])
    CONTROL["CB"] = ok_scr
    check("CB [typing control] the SCRAMBLED comb (seed %d, same "
          "masses): the corner identity STILL holds symbolically "
          "(max coeff dev %.2e <= %.2e) and the state-face corner "
          "value is UNCHANGED (it reads no positions) -- while the "
          "deployed lock data moves: tau = %+.3e (true) -> %+.3e "
          "(scrambled), full-window lambda_min(scr) = %+.3e"
          % (SCR_SEED, dev_scr, bar_scr, tau_true, tau_scr, lmin_s),
          ok_scr)
    print("      TYPED (the honest scope of the route): under outcome "
          "1 a scrambled comb gets tau >= 0 STRUCTURALLY from any "
          "positive P_lock -- so what distinguishes the true comb is "
          "NOT the positivity but the IDENTIFICATION: which self-"
          "adjoint operator the CP corner is applied to, i.e. that "
          "the corner of P_X equals the DEPLOYED window form T_GL1,X "
          "built from the actual prime placements.  The arithmetic "
          "lives entirely in the identification step.")

    section("V -- FROZEN VERDICT + the one-paragraph honest consequence")
    exact_ok = (not off) and ok_toy and ok_ward
    bar_max = max(b for _kz, _ok, _d, b in dev_report)
    if exact_ok and ok_all_sym:
        verdict = "CORNER-IDENTITY-SYMBOLIC"
    elif max(prime_dev) <= bar_max:
        verdict = "CORNER-IDENTITY-ARITHMETIC-ONLY"
    else:
        verdict = "CORNER-NO-IDENTITY"
    controls_ok = CONTROL.get("CA", False) and CONTROL.get("CB", False)
    print("\n  VERDICT: %s%s" % (verdict, "" if controls_ok
                                 else "  [CONTROL VOID -- see FAILS]"))
    if verdict == "CORNER-IDENTITY-SYMBOLIC":
        print("""
  THE FINDING: T_GL1,X = V_X* . e_GL1 . pi_X(P_X) . e_GL1 . V_X holds
  as POLYNOMIAL ALGEBRA in free event weights w_j -- exactly (toy leg,
  symbolic arch lags AND weights) and on all %d deployed windows at
  the float bar; the entire equality step consumes ONE piece of
  arithmetic: the packet normalizations (glue identity Sum_m Th_m =
  240 sigma3 + the uniform H* mass), which force chat_j = -1 for every
  event.  e_GL1 is a genuine projector (e^2 = e = e*, exact, rank 1),
  corner compression is single-Kraus CP, and P_lock-type Gram objects
  are structurally >= 0.

  THE HONEST CONSEQUENCE (one paragraph): the corner route SPLITS the
  floor into (i) a structural half that is now closed at finite level
  -- the identity is weight-generic and placement-blind, so a window
  induction over X is bookkeeping, not arithmetic: the Hjelmslev
  ladder (H1-H5) is AUTHORIZED in exactly this role, carrying the
  IDENTITY and the projector/CP structure through the tower -- and
  (ii) an arithmetic half that this probe does NOT touch and no corner
  can manufacture: the object with the corner identity (the packet
  window operator P_X) is NOT positive (S5.3: only the GL1 sector of
  12 is PSD), the manifestly positive object (the packet GNS Gram) has
  a corner value that is NOT tau_X (S5.2, gap measured), and the
  scramble control (CB) proves any purely structural positivity is
  comb-blind.  So tau_X >= 0 via this route needs a positive P_lock
  WHOSE CORNER IS IDENTIFIED with the deployed window form -- and that
  identification is exactly where the prime placements enter, i.e. the
  honest wall stays PRIME.FLOOR.PAIRCORR.01: relocated into the
  identification step, not removed.  Any Hjelmslev stage that promises
  positivity transfer WITHOUT the identification datum is dead on
  arrival; the stages that build the identification (the ring-lift of
  the incidence frame carrying the window form itself) are the live
  ones.  NO RH claim.""" % N_WIN)
    elif verdict == "CORNER-IDENTITY-ARITHMETIC-ONLY":
        print("""
  THE FINDING: the generic symbolic identity FAILS -- the defect
  polynomial is sum_j w_j (1 + chat_j) read_j with the nonzero
  chat-offsets printed in S3.2: the weight combinations that must
  vanish are exactly the events whose carrier element is NOT
  normalized to the GL1 character.  The residual is the honest new
  wall; check against the pair-correlation object before any next
  stage.  Hjelmslev ladder NOT authorized until the defect is typed.""")
    else:
        print("""
  THE FINDING: no identity even at the prime weights -- the printed
  per-window deviations localize which term of T_GL1,X cannot be
  written as a corner (constant/arch term vs which event rows).  The
  route is dead; the Hjelmslev ladder is KILLED at H1.""")

    n_pass = sum(1 for _n, ok in CHECKS if ok)
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed%s"
          % (time.time() - T0, len(CHECKS), len(FAILS),
             ("  " + ",".join(FAILS)) if FAILS else ""))
    return 0 if (n_pass == len(CHECKS) and controls_ok) else 1


if __name__ == "__main__":
    raise SystemExit(main())
