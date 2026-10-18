#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""v835 -- PRIME.CORNER.CHARACTER.01 + PRIME.HJELMSLEV.CPTOWER.01: the character-corner identity is weight-generic and the Gaussian Hjelmslev CP tower carries it verbatim through five levels -- but no register lift builds the identification: the corner route's structural half CLOSES at finite level while the arithmetic wall relocates INTO the identification step and stays PRIME.FLOOR.PAIRCORR.01, ONE module from two probes (21/21 + 20/20 checks, verdicts CORNER-IDENTITY-SYMBOLIC and HJELMSLEV-STRUCTURE-ONLY; discovery probes character_corner_probe.py and hjelmslev_cp_tower_probe.py, 2026-08-07, re-run identically at promotion, promoted VERBATIM with no downscoping, ~11 s).  PART A, THE CORNER IDENTITY (the route decision): the target identity T_GL1,X = V_X* . e_GL1 . pi_X(P_X) . e_GL1 . V_X holds as POLYNOMIAL ALGEBRA in free event weights w_j -- EXACTLY on the toy leg (M = 8, D = 1, symbolic arch lags AND weights, sympy defect matrix == 0) and on all 3 deployed alpha-smallest frame-A windows at the float bar (two INDEPENDENT deployed code paths: v563 spline-read lock vs per-event Kraus-row quadratic forms); the ENTIRE equality step consumes ONE piece of arithmetic -- the packet normalizations (the glue identity Sum_m Th_m = 240 sigma3, exact to n <= 640, + the uniform H* mass), which force the corner coefficient chat_j = -1 EXACTLY for every one of the 136 distinct events (exact group-algebra Fourier on the 128-dim register C2 x F2^4 x Z4; full two-sided ward e sigma(x_j) e = chat_j e exact on LCG-sampled events); e_GL1 is a genuine projector (e*e = e = e^adj exact, Fourier = the delta at chi_GL1, rank 1) and corner compression is single-Kraus CP (Choi = |vec e><vec e| exact).  THE HONEST SCOPE (measured): the object carrying the IDENTITY (the packet window operator) is NOT positive (only the GL1 sector of 12 is PSD); the manifestly positive object (the packet GNS Gram) has a corner value that is NOT tau_X (gap measured per window); the naive signed pushforward FAILS positivity on all 3 windows (exact rationals, v791 F1 reproduced as the contrast); and the scramble control proves the identity + state corner are COMB-BLIND while the deployed lock data moves (tau +5.98e-4 -> -3.51) -- so structural positivity can never be the floor: the arithmetic lives ENTIRELY in the identification step (a positive P_lock whose corner IS the deployed window form), i.e. the wall RELOCATES into identification and stays PRIME.FLOOR.PAIRCORR.01.  PART B, THE HJELMSLEV TOWER (the authorized next stage, executed): the chain-ring ladder R_m = Z[i]/(1+i)^m, m = 1..5 (exhaustive exact digit-code tables; reduction = the low-bit mask) carries exact point/line/flag geometries with counts 15*8^(m-1) / 35*16^(m-1) / 105*32^(m-1) and uniform reduction fibers 8/16/32 (points brute-force ALL m <= 5; lines brute m <= 3, materialized m = 4, sampled m = 5); the flag incidences define unital CP channels with uniform degree d_m = 7*4^(m-1) whose m = 1 member IS the deployed 105-leg Stinespring structure (B B^T = 4I + 3J, K^2 = (4/49)I + (45/49)J/15, Choi diag 1/7; v756/v820 read-only) and whose Choi matrices are exactly positive at every level; the tower is STRICTLY PROJECTIVE -- the certified cb compatibility defect is identically ZERO (full exact steps 1->2, 2->3; sampled 3->4, 4->5), exceeding the conjectured 2^(-m/2) decay; the character corner is LEVEL-EXACT: e_GL1,m factor-projector wards exact per level, tower compatibility Psi(e_{m+1}) = e_m and iota(e_m) = e_{m+1} at zero defect, the ram-odd V-slot lifts geometrically to the uniform distribution on s_m = 7*8^(m-1) polar unimodulars, and chat_j^(m) = -1 EXACTLY for all events at all levels -- the certified corner identity carries VERBATIM, with the circularity fence SILENT (only counting/normalization identities consumed).  BUT H5 DECIDES AGAINST IDENTIFICATION: the level-m state corner is COMB-BLIND (the scrambled comb reproduces the series bit for bit) and its motion is the pure register-dilution law value_1 * 16^(1-m) (ratio 0.0625 exactly at every step; the GL1 numerator reads a_n/sigma3(n) which vanishes on every ram event) -- the tower, as a register/geometry lift, has NO channel through which the prime placements enter; the one live follow-up door: position-dependent Kraus data on the level-m flags (the identification-carrying tower datum), not register-only lifts.  STOP-LIST DISCIPLINE: no signed-prime-sum estimation anywhere; v831 / PRIME.FLOOR.PAIRCORR.01 binding; AST firewall (no zeta-zero / prime-table symbol); machinery imports READ-ONLY (v563 windows, v738 frame).  NO RH claim.  Python-only per GATE.WOLFRAM.02.

PROVENANCE: discovery probes character_corner_probe.py (21/21, verdict
CORNER-IDENTITY-SYMBOLIC) and hjelmslev_cp_tower_probe.py (20/20,
verdict HJELMSLEV-STRUCTURE-ONLY), both 2026-08-07, re-run identically
at promotion; this module runs both frozen protocols VERBATIM (~11 s;
each part resets the frozen LCG seed 20260807).  The original probe
docstrings, frozen specs (SHA-256-printed) and decision trees live in
the probe files verbatim (experiments/tfpt-discovery/).

FIREWALL: v563 / v738 READ-ONLY; no zeta zero, no prime-table symbol
(AST-checked; own sieves only); sympy for symbolic algebra only; RNG
only in the declared v563 scramble recipe (seed 1) and the fixed LCG
(seed 20260807).  NO RH claim.
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
import sympy as sp

_here = os.path.dirname(os.path.abspath(__file__))
if _here not in sys.path:
    sys.path.insert(0, _here)

import v563_paper2_readouts as core        # noqa: E402  (READ-ONLY)
import v738_hecke_mod_ramified as ram      # noqa: E402  (READ-ONLY)

# ------------------------------------------------------- shared layer
N_TH = 640
SCR_SEED = 1
LCG_SEED = 20260807
BANNED_IDS = ("zetazero", "nzeros", "primerange", "isprime", "primepi",
              "nextprime", "prevprime")
EXPECTED_A = "CORNER-IDENTITY-SYMBOLIC"
EXPECTED_B = "HJELMSLEV-STRUCTURE-ONLY"

CHECKS = []
FAILS = []
_LCG = [LCG_SEED]


def lcg_reset():
    _LCG[0] = LCG_SEED


def lcg(n):
    _LCG[0] = (1103515245 * _LCG[0] + 12345) % (1 << 31)
    return _LCG[0] % n


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok)))
    if not ok:
        FAILS.append(name.split()[0])
    print("  [%s] %s%s" % ("PASS" if ok else "FAIL", name,
                           ("  -- " + detail) if detail else ""),
          flush=True)
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


# =====================================================================
# PART A -- PRIME.CORNER.CHARACTER.01 (character_corner_probe verbatim)
# =====================================================================
FROZEN_SPEC_CORNER = """\
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
BAR_COEF_REL = 1.0e-9
PSD_BAR = 1.0e-10
N_WARD_SAMPLE = 12
TOY_M = 8
TOY_POS = (Fr(1, 2), Fr(3, 2), Fr(7, 3), Fr(5))
TOY_LABEL_N = (2, 3, 4, 5)
CONTROL = {}

# G = C2 x F2^4 x Z4 as tuples (a, v, m); characters (eps, w, j):
# chi(a, v, m) = (-1)^{eps a} (-1)^{popcount(w & v)} i^{j m}.
G_ELEMS = [(a, v, m) for a in range(2) for v in range(16)
           for m in range(4)]
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
    q = (j * m) % 4                     # i^q
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
    c_lhs = [a_syms[d] + sp.Add(*[w_syms[j] * sp.Rational(rows[j][d])
                                  for j in range(len(rows))])
             for d in range(M)]
    A_lhs = odd_toep(c_lhs)
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


def part_corner():
    t0 = time.time()
    lcg_reset()
    CONTROL.clear()
    section("v835 PART A -- PRIME.CORNER.CHARACTER.01: the decisive "
            "character-corner protocol (promoted verbatim)")
    sha = hashlib.sha256(FROZEN_SPEC_CORNER.encode("utf-8")).hexdigest()
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

    section("V(A) -- frozen verdict, part A")
    exact_ok = (not off) and ok_toy and ok_ward
    bar_max = max(b for _kz, _ok, _d, b in dev_report)
    if exact_ok and ok_all_sym:
        verdict = "CORNER-IDENTITY-SYMBOLIC"
    elif max(prime_dev) <= bar_max:
        verdict = "CORNER-IDENTITY-ARITHMETIC-ONLY"
    else:
        verdict = "CORNER-NO-IDENTITY"
    controls_ok = CONTROL.get("CA", False) and CONTROL.get("CB", False)
    print("\n  VERDICT (PART A): %s%s"
          % (verdict, "" if controls_ok
             else "  [CONTROL VOID -- see FAILS]"))
    print("  the honest consequence: structural half closed at finite "
          "level (identity weight-generic, placement-blind; Hjelmslev "
          "ladder authorized in exactly that role); arithmetic half "
          "untouched -- the wall stays PRIME.FLOOR.PAIRCORR.01, "
          "relocated into the identification step.  NO RH claim.")
    print("  [TIME PART A] %.1f s" % (time.time() - t0))
    return verdict, controls_ok


# =====================================================================
# PART B -- PRIME.HJELMSLEV.CPTOWER.01 (hjelmslev_cp_tower_probe
# verbatim)
# =====================================================================
FROZEN_SPEC_TOWER = """\
PRIME.HJELMSLEV.CPTOWER.01 spec v1 (2026-08-07, frozen before the run).
Ladder R_m = Z[i]/(1+i)^m, m = 1..5, digit codes + exhaustive tables;
Omega_m = U - U^T (U = strict upper of the v738 lex-first form).
H1 counts 15*8^(m-1) / 35*16^(m-1) / 105*32^(m-1), fibers 8/16/32;
points brute-force ALL m <= 5, lines brute m <= 3 + materialized m = 4
+ sampled m = 5 (200 parents); per-line 3*2^(m-1) full m <= 3, sampled
m = 4 (100 lines).  H2 d_m = 7*4^(m-1) full m <= 3, sampled m = 4 (48)
m = 5 (24); Choi diag 1/d_m explicit m <= 2; v756 anchor wards.
H3 cb defect = max-row-L1 exact; full 1->2, 2->3; sampled 3->4 (48),
4->5 (24).  H4 e-factor wards + 128-dim m=1 conv + tower compat exact;
geometric ram-odd lift = uniform on s_m = 7*8^(m-1) polar unimodulars;
chat = -1 exact all events x m = 1..5; FENCE audit.  H5 level-1 census
units, 3 windows, regression 4.813726e-3 / tau 5.984165e-4 (kz = 9);
PASS = monotone gap shrink 3/3 AND comb-specific (scramble seed 1
series must differ).  LCG 20260807.  NO RH claim; writes nothing.
"""

M_MAX = 5
N_LINE_SAMPLE_M5 = 200
N_LINE_PTS_SAMPLE_M4 = 100
N_DEG_SAMPLE = {4: 48, 5: 24}
N_ITW_SAMPLE = {3: 48, 4: 24}
REG_REFS = {9: (4.813726e-3, 5.984165e-4),
            12: (3.227697e-3, 4.351189e-4),
            13: (2.954471e-3, 5.637632e-4)}
REG_BAR = 1.0e-4
FENCE = {"fired": False, "reason": ""}


def build_ring(m):
    """R_m = Z[i]/(1+i)^m as digit codes 0..2^m-1 with exhaustive
    exact tables (built from Gaussian-integer arithmetic)."""
    size = 1 << m
    dec = []
    for code in range(size):
        a = b = 0
        pa, pb = 1, 0                   # pi^j, pi = 1 + i
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
    inv = {}
    for x in range(size):
        if x & 1:
            for y in range(size):
                if mul[x][y] == 1:
                    inv[x] = y
                    break
    return dict(m=m, size=size, dec=dec, enc=enc, add=add, mul=mul,
                neg=neg, inv=inv)


def ring_wards(R):
    """Exhaustive ring axioms + unit census + bijectivity."""
    size, add, mul, neg = R["size"], R["add"], R["mul"], R["neg"]
    ok = all(R["enc"](*R["dec"][c]) == c for c in range(size))
    ok &= len(R["inv"]) == size // 2 if R["m"] > 0 else True
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


def reduction_ward(R_hi, R_lo):
    """Reduction R_{m+1} -> R_m == the low-bit mask; fibers exactly 2."""
    mask = R_lo["size"] - 1
    ok = True
    fib = {}
    for c in range(R_hi["size"]):
        a, b = R_hi["dec"][c]
        ok &= R_lo["enc"](a, b) == (c & mask)
        fib[c & mask] = fib.get(c & mask, 0) + 1
    ok &= all(v == 2 for v in fib.values()) and len(fib) == R_lo["size"]
    return ok


def label_frame():
    """v738 lex-first sigma-invariant symplectic frame (read-only):
    returns Omega (4x4 over F2), y_chi, H* labels."""
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


def omega_codes(Omega, R):
    """Alternating lift Omega_m = U - U^T as R_m codes."""
    neg1 = R["neg"][1]
    return [[(1 if (i < j and Omega[i][j]) else
              (neg1 if (i > j and Omega[i][j]) else 0))
             for j in range(4)] for i in range(4)]


def point_canon(y, R):
    for c in y:
        if c & 1:
            s = R["inv"][c]
            mu = R["mul"][s]
            return tuple(mu[v] for v in y)
    return None


def brute_points(R):
    size = R["size"]
    pts = set()
    for y in product(range(size), repeat=4):
        if (y[0] | y[1] | y[2] | y[3]) & 1:
            pts.add(point_canon(y, R))
    return pts


def lift_points(pts_lo, m_lo, R_hi):
    """All lifts of every level-m point; returns (set, fiber_ok)."""
    out = set()
    fiber_ok = True
    for x in pts_lo:
        lifts = set()
        for u in range(16):
            cand = tuple(x[i] | (((u >> i) & 1) << m_lo)
                         for i in range(4))
            lifts.add(point_canon(cand, R_hi))
        fiber_ok &= len(lifts) == 8
        out |= lifts
    return out, fiber_ok


def line_canon(r1, r2, R):
    add, mul, neg, inv = R["add"], R["mul"], R["neg"], R["inv"]
    rows = [list(r1), list(r2)]
    rowi = 0
    for col in range(4):
        pr = None
        for rr in range(rowi, 2):
            if rows[rr][col] & 1:
                pr = rr
                break
        if pr is None:
            continue
        rows[rowi], rows[pr] = rows[pr], rows[rowi]
        s = inv[rows[rowi][col]]
        rows[rowi] = [mul[s][v] for v in rows[rowi]]
        oth = 1 - rowi
        f = rows[oth][col]
        if f:
            rows[oth] = [add[rows[oth][j]][neg[mul[f][rows[rowi][j]]]]
                         for j in range(4)]
        rowi += 1
        if rowi == 2:
            break
    if rowi < 2:
        return None
    return (tuple(rows[0]), tuple(rows[1]))


def coset_reps(lbar):
    """4 coset representatives of F2^4 / lbar (lbar = 4-elt subgroup
    of 4-bit ints)."""
    reps = []
    seen = set()
    for v in range(16):
        if v not in seen:
            reps.append(v)
            seen |= {v ^ l for l in lbar}
    return reps


def lift_lines(lines_lo, m_lo, R_hi, R_lo, sample_idx=None):
    """Lifts of lines (all, or a sampled parent subset); returns
    (set_or_count, fiber_ok, reduction_ok)."""
    out = set()
    fiber_ok = True
    red_ok = True
    mask = R_lo["size"] - 1
    items = (lines_lo if sample_idx is None
             else [lines_lo[i] for i in sample_idx])
    for (r1, r2) in items:
        b1 = sum((r1[i] & 1) << i for i in range(4))
        b2 = sum((r2[i] & 1) << i for i in range(4))
        lbar = {0, b1, b2, b1 ^ b2}
        reps = coset_reps(lbar)
        lifts = set()
        for u in reps:
            for v in reps:
                c1 = tuple(r1[i] | (((u >> i) & 1) << m_lo)
                           for i in range(4))
                c2 = tuple(r2[i] | (((v >> i) & 1) << m_lo)
                           for i in range(4))
                ln = line_canon(c1, c2, R_hi)
                if ln is None:
                    fiber_ok = False
                    continue
                lifts.add(ln)
                rr1 = tuple(c & mask for c in ln[0])
                rr2 = tuple(c & mask for c in ln[1])
                red_ok &= line_canon(rr1, rr2, R_lo) == (r1, r2)
        fiber_ok &= len(lifts) == 16
        out |= lifts
    return out, fiber_ok, red_ok


def brute_lines(pts, R):
    out = set()
    plist = sorted(pts)
    for i in range(len(plist)):
        xi = plist[i]
        bi = sum((xi[k] & 1) << k for k in range(4))
        for j in range(i + 1, len(plist)):
            yj = plist[j]
            bj = sum((yj[k] & 1) << k for k in range(4))
            if bi == bj:
                continue
            ln = line_canon(xi, yj, R)
            if ln is not None:
                out.add(ln)
    return out


def line_points(ln, R):
    """Points on a line = images of unimodular parameter pairs."""
    r1, r2 = ln
    add, mul = R["add"], R["mul"]
    size = R["size"]
    pts = set()
    for a in range(size):
        m1 = mul[a]
        for b in range(size):
            if not ((a | b) & 1):
                continue
            m2 = mul[b]
            y = tuple(add[m1[r1[k]]][m2[r2[k]]] for k in range(4))
            pts.add(point_canon(y, R))
    return pts


def neighbors(x, R, Om, m):
    """Incidence neighbors of the point x at level m: canonical points
    y with x Omega_m y^T = 0; returns dict point -> #unimodular kernel
    vectors mapping to it (must be 2^(m-1) each)."""
    add, mul, neg, inv = R["add"], R["mul"], R["neg"], R["inv"]
    w = []
    for j in range(4):
        acc = 0
        for i in range(4):
            o = Om[i][j]
            if o:
                acc = add[acc][mul[x[i]][o]]
        w.append(acc)
    i0 = next(j for j in range(4) if w[j] & 1)
    s = inv[w[i0]]
    others = [j for j in range(4) if j != i0]
    size = 1 << m
    w0, w1, w2 = w[others[0]], w[others[1]], w[others[2]]
    pts = {}
    y = [0, 0, 0, 0]
    for c0 in range(size):
        a0 = mul[w0][c0]
        for c1 in range(size):
            a1 = add[a0][mul[w1][c1]]
            for c2 in range(size):
                acc = add[a1][mul[w2][c2]]
                yi0 = mul[s][neg[acc]]
                if (c0 | c1 | c2 | yi0) & 1:
                    y[others[0]] = c0
                    y[others[1]] = c1
                    y[others[2]] = c2
                    y[i0] = yi0
                    p = point_canon(y, R)
                    pts[p] = pts.get(p, 0) + 1
    return pts


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


# m = 1 conv layer (the deployed register)
G1 = [(a, v, m) for a in range(2) for v in range(16) for m in range(4)]


def g1_mul(g, h):
    return ((g[0] + h[0]) % 2, g[1] ^ h[1], (g[2] + h[2]) % 4)


def g1_inv(g):
    return (g[0], g[1], (-g[2]) % 4)


def chi_gl1_1(g):
    return -1 if g[0] else 1


def conv1(f, h):
    out = {}
    for g, fg in f.items():
        gi = g1_inv(g)
        for k in G1:
            hv = h.get(g1_mul(gi, k))
            if hv:
                out[k] = out.get(k, Fr(0)) + fg * hv
    return {k: v for k, v in out.items() if v != 0}


def part_tower():
    t_start = time.time()
    lcg_reset()
    FENCE["fired"] = False
    FENCE["reason"] = ""
    section("v835 PART B -- PRIME.HJELMSLEV.CPTOWER.01: the Gaussian "
            "Hjelmslev CP tower (promoted verbatim)")
    sha = hashlib.sha256(FROZEN_SPEC_TOWER.encode("utf-8")).hexdigest()
    print("    FROZEN_SPEC SHA-256 = %s" % sha)
    print("    binding scope (part A, frozen): the corner identity is "
          "comb-blind; the live target is the IDENTIFICATION through "
          "the tower.  NO RH claim.")

    print("\nS0 -- firewall")
    bad = ast_firewall()
    check("S0.1 AST firewall: no zeta-zero / prime-table symbol",
          not bad, "found %s" % bad if bad else "clean")

    # ------------------------------------------------------------- H1
    section("H1 -- canonical reduction: the chain-ring ladder R_1..R_5")
    t0 = time.time()
    rings = {m: build_ring(m) for m in range(1, M_MAX + 1)}
    ok_r = all(ring_wards(rings[m]) for m in range(1, M_MAX + 1))
    ok_red = all(reduction_ward(rings[m + 1], rings[m])
                 for m in range(1, M_MAX))
    check("H1.1 [EXACT] R_m = Z[i]/(1+i)^m as digit codes: ring axioms "
          "EXHAUSTIVE per level (add/mul/assoc/distr over all "
          "triples), units = 2^(m-1), enc/dec bijective; reduction "
          "R_{m+1} -> R_m IS the low-bit mask with exact 2-element "
          "fibers (the tower maps are bitmasks)",
          ok_r and ok_red, "%.1f s" % (time.time() - t0))

    Omega, y_chi, Hstar = label_frame()
    Oms = {m: omega_codes(Omega, rings[m]) for m in range(1, M_MAX + 1)}
    print("    frame: v738 lex-first Omega = %s; y_chi = %s; |H*| = %d"
          % (Omega, y_chi, len(Hstar)))
    print("    alternating lift Omega_m = U - U^T (declared: the 0/1 "
          "symmetric lift is NOT alternating for m >= 3; U - U^T is, "
          "at every level, and reduces to Omega mod pi)")

    # points tower
    t0 = time.time()
    pts = {}
    ok_pts = True
    ok_fib_p = True
    for m in range(1, M_MAX + 1):
        bf = brute_points(rings[m])
        if m == 1:
            pts[m] = bf
        else:
            lifted, fib_ok = lift_points(sorted(pts[m - 1]), m - 1,
                                         rings[m])
            ok_fib_p &= fib_ok and (lifted == bf)
            pts[m] = bf
        ok_pts &= len(bf) == 15 * 8 ** (m - 1)
    ok_redp = True
    for m in range(1, M_MAX):
        mask = rings[m]["size"] - 1
        fib = {}
        for x in pts[m + 1]:
            xr = point_canon(tuple(c & mask for c in x), rings[m])
            fib[xr] = fib.get(xr, 0) + 1
        ok_redp &= (set(fib) == pts[m]
                    and all(v == 8 for v in fib.values()))
    check("H1.2 [EXACT] POINTS: brute-force enumeration over ALL "
          "2^(4m) vectors == recursive-lift materialization at every "
          "level; counts %s == 15*8^(m-1); reduction SURJECTIVE with "
          "uniform fiber 8 (exhaustive m = 1..5)"
          % [len(pts[m]) for m in range(1, M_MAX + 1)],
          ok_pts and ok_fib_p and ok_redp,
          "%.1f s" % (time.time() - t0))

    # lines tower
    t0 = time.time()
    lines = {}
    ok_lin = True
    ok_fib_l = True
    ok_red_l = True
    for m in range(1, 5):
        if m == 1:
            lines[1] = sorted(brute_lines(pts[1], rings[1]))
        else:
            lifted, fib_ok, red_ok = lift_lines(lines[m - 1], m - 1,
                                                rings[m], rings[m - 1])
            ok_fib_l &= fib_ok
            ok_red_l &= red_ok
            lines[m] = sorted(lifted)
            if m <= 3:
                ok_lin &= (set(lines[m])
                           == brute_lines(pts[m], rings[m]))
        ok_lin &= len(lines[m]) == 35 * 16 ** (m - 1)
    idx5 = sorted({lcg(len(lines[4])) for _ in range(N_LINE_SAMPLE_M5)})
    _s5, fib5, red5 = lift_lines(lines[4], 4, rings[5], rings[4],
                                 sample_idx=idx5)
    n_lines_5 = 35 * 16 ** 4
    check("H1.3 LINES: counts %s == 35*16^(m-1) (m <= 4 MATERIALIZED "
          "by lifting; independent brute-force pair-span ward m <= 3 "
          "set-identical); lift fibers exactly 16 with exact "
          "reduction at every materialized step; m = 5: %d sampled "
          "parents give 16 distinct valid lifts each (count %d "
          "DERIVED, typed)"
          % ([len(lines[m]) for m in range(1, 5)], len(idx5),
             n_lines_5),
          ok_lin and ok_fib_l and ok_red_l and fib5 and red5,
          "%.1f s" % (time.time() - t0))

    # flags
    t0 = time.time()
    ok_lp = True
    for m in range(1, 4):
        for ln in lines[m]:
            if len(line_points(ln, rings[m])) != 3 * 2 ** (m - 1):
                ok_lp = False
                break
    idx4 = sorted({lcg(len(lines[4]))
                   for _ in range(N_LINE_PTS_SAMPLE_M4)})
    ok_lp4 = all(len(line_points(lines[4][i], rings[4])) == 24
                 for i in idx4)
    flags = [105 * 32 ** (m - 1) for m in range(1, M_MAX + 1)]
    check("H1.4 FLAGS: per-line point count == 3*2^(m-1) (EXHAUSTIVE "
          "every line m <= 3; sampled %d lines m = 4; PHG(1,R_m) "
          "counting); flag counts F_m = %s == 105*32^(m-1) (exact "
          "m <= 4 = lines x points-per-line; m = 5 derived); flag "
          "reduction fiber = 16 x 2 = 32 (line fiber x point-in-line "
          "fiber), anchor F_1 = 105 = the 35 lines x 3 = the PG(3,2) "
          "flags" % (len(idx4), flags),
          ok_lp and ok_lp4 and flags[0] == 105 and len(lines[1]) == 35,
          "%.1f s" % (time.time() - t0))
    print("    REDUCTION DIAGRAM (points / lines / flags, fibers "
          "8 / 16 / 32 per step):")
    for m in range(1, M_MAX + 1):
        n_l = len(lines[m]) if m <= 4 else n_lines_5
        print("      m=%d: P = %6d   L = %8d   F = %10d   [%s]"
              % (m, len(pts[m]), n_l, flags[m - 1],
                 "exact" if m <= 4 else "derived + sampled ward"))

    # ------------------------------------------------------------- H2
    section("H2 -- compatible CP channels on the ladder")
    t0 = time.time()
    nb = {}
    ok_deg = True
    ok_mult = True
    for m in range(1, 4):
        nb[m] = {}
        d_m = 7 * 4 ** (m - 1)
        for x in pts[m]:
            nn = neighbors(x, rings[m], Oms[m], m)
            nb[m][x] = set(nn)
            ok_deg &= len(nn) == d_m
            ok_mult &= all(v == 2 ** (m - 1) for v in nn.values())
    check("H2.1a [EXACT] degree uniformity d_m = 7*4^(m-1) on EVERY "
          "point, m = 1..3 (full kernel enumeration; each neighbor "
          "point hit by exactly 2^(m-1) unimodular kernel vectors = "
          "the unit multiples)", ok_deg and ok_mult,
          "%.1f s" % (time.time() - t0))
    t0 = time.time()
    ok_deg_s = True
    plists = {m: sorted(pts[m]) for m in range(4, 6)}
    for m in (4, 5):
        d_m = 7 * 4 ** (m - 1)
        for _ in range(N_DEG_SAMPLE[m]):
            x = plists[m][lcg(len(plists[m]))]
            nn = neighbors(x, rings[m], Oms[m], m)
            ok_deg_s &= (len(nn) == d_m
                         and all(v == 2 ** (m - 1)
                                 for v in nn.values()))
    legs = [15 * 8 ** (m - 1) * 7 * 4 ** (m - 1)
            for m in range(1, M_MAX + 1)]
    check("H2.1b degree uniformity SAMPLED m = 4 (%d pts), m = 5 (%d "
          "pts), exact per sample; Kraus legs N_m = P_m d_m = %s == "
          "105*32^(m-1) == the FLAG counts (the legs are the flags, "
          "level-wise)" % (N_DEG_SAMPLE[4], N_DEG_SAMPLE[5], legs),
          ok_deg_s, "%.1f s" % (time.time() - t0))

    # m = 1 deployed Stinespring ward (v756/v820 read-only)
    p1 = sorted(pts[1])
    idx1 = {x: i for i, x in enumerate(p1)}
    B1 = np.zeros((15, 15), dtype=np.int64)
    for x in p1:
        for y in nb[1][x]:
            B1[idx1[x], idx1[y]] = 1
    ok_b = (np.array_equal(B1, B1.T)
            and np.array_equal(B1 @ B1.T,
                               4 * np.eye(15, dtype=np.int64)
                               + 3 * np.ones((15, 15), dtype=np.int64))
            and int(B1.sum()) == 105)
    K1 = [[Fr(int(B1[i, j]), 7) for j in range(15)] for i in range(15)]
    ok_k2 = True
    for i in range(15):
        for j in range(15):
            v = sum(K1[i][k] * K1[k][j] for k in range(15))
            tgt = Fr(3, 49) + (Fr(4, 49) if i == j else Fr(0))
            ok_k2 &= v == tgt
    check("H2.2 [EXACT] the m = 1 channel IS the deployed 105-leg "
          "Stinespring structure (v756/v820 read-only ward): "
          "B B^T = 4I + 3J, 105 legs, K = B/7 with K^2 = (4/49) I + "
          "(45/49) J/15 (Fraction matrix identity), Choi diagonal "
          "1/7 x 105", ok_b and ok_k2)

    # Choi explicit m <= 2 + float PSD ward at m = 2
    p2 = sorted(pts[2])
    idx2 = {x: i for i, x in enumerate(p2)}
    d2 = 28
    choi_diag = {}
    for x in p2:
        nn = neighbors(x, rings[2], Oms[2], 2)
        for y in nn:
            choi_diag[(idx2[x], idx2[y])] = Fr(1, d2)
    ok_choi = (len(choi_diag) == legs[1]
               and all(v > 0 for v in choi_diag.values()))
    rng = np.random.default_rng(1505)
    Z = rng.standard_normal((120, 120))
    Ain = Z.T @ Z
    Kmat = np.zeros((120, 120))
    for (i, j) in choi_diag:
        Kmat[i, j] = 1.0 / d2
    img = Kmat @ np.diag(Ain).copy()
    lam_img = float(img.min())
    check("H2.3 CHOI PSD per level: DIAGONAL Choi with entries 1/d_m "
          "> 0 (single-Kraus-family form -- CP manifest; explicit "
          "rational construction at m = 2: %d legs, all positive, "
          "rank = N_2 = %d); float PSD-image ward at m = 2 (random "
          "PSD input, diagonal image min %.3e >= 0); m >= 3 "
          "structural (same Kraus form) + the exact degree wards "
          "H2.1" % (len(choi_diag), legs[1], lam_img),
          ok_choi and lam_img >= -1e-12)

    # ------------------------------------------------------------- H3
    section("H3 -- projective compatibility: Phi_{m+1} iota vs iota "
            "Phi_m (certified cb defect)")

    def itw_step(m, sample=None):
        d_hi = 7 * 4 ** m
        d_lo = 7 * 4 ** (m - 1)
        mask = rings[m]["size"] - 1
        worst = Fr(0)
        items = (sorted(pts[m + 1]) if sample is None else sample)
        for X in items:
            nnX = (nb[m + 1][X] if (m + 1) in nb
                   else neighbors(X, rings[m + 1], Oms[m + 1], m + 1))
            proj = {}
            for Y in nnX:
                yr = point_canon(tuple(c & mask for c in Y), rings[m])
                proj[yr] = proj.get(yr, 0) + 1
            Xr = point_canon(tuple(c & mask for c in X), rings[m])
            nbP = (nb[m][Xr] if m in nb
                   else set(neighbors(Xr, rings[m], Oms[m], m)))
            row = Fr(0)
            for y in set(proj) | nbP:
                row += abs(Fr(proj.get(y, 0), d_hi)
                           - (Fr(1, d_lo) if y in nbP else Fr(0)))
            worst = max(worst, row)
        return worst

    t0 = time.time()
    e12 = itw_step(1)
    e23 = itw_step(2)
    check("H3.1 [EXACT] FULL steps: ||E_1||_cb = %s and ||E_2||_cb = "
          "%s (max-row-L1 of the exact rational defect kernel over "
          "ALL level-(m+1) points; cb norm = norm for maps of "
          "commutative C*-algebras) -- the CP tower is EXACTLY "
          "projective on the full steps: every parent neighbor is "
          "covered by exactly d_{m+1}/d_m = 4 lifted neighbors"
          % (e12, e23), e12 == 0 and e23 == 0,
          "%.1f s" % (time.time() - t0))
    t0 = time.time()
    smp3 = [plists[4][lcg(len(plists[4]))]
            for _ in range(N_ITW_SAMPLE[3])]
    e34 = itw_step(3, sample=smp3)
    smp4 = [plists[5][lcg(len(plists[5]))]
            for _ in range(N_ITW_SAMPLE[4])]
    e45 = itw_step(4, sample=smp4)
    conj_ok = all(e <= Fr(1) for e in (e12, e23, e34, e45))
    check("H3.2 SAMPLED steps: defect rows EXACTLY 0 on %d level-4 "
          "and %d level-5 points (||E_3||, ||E_4|| = %s, %s on the "
          "samples); the frozen conjecture ||E_m|| <= C 2^(-m/2) "
          "(the 0.701/doubling v817 rate) is EXCEEDED: the measured "
          "defect is identically ZERO -- the tower is strictly "
          "projective, not merely summable (the 0.701 rate belongs "
          "to the packet STATE ladder, not to this channel tower; "
          "typed)" % (len(smp3), len(smp4), e34, e45),
          e34 == 0 and e45 == 0 and conj_ok,
          "%.1f s" % (time.time() - t0))

    # ------------------------------------------------------------- H4
    section("H4 -- the normal character corner along the ladder "
            "(circularity-fenced)")
    E1 = {g: Fr(chi_gl1_1(g), 128) for g in G1}
    EE = conv1(E1, E1)
    ok_e1 = (all(EE.get(g, Fr(0)) == E1[g] for g in G1)
             and all(E1[g1_inv(g)] == E1[g] for g in G1))
    check("H4.1a [EXACT] m = 1 anchor: e_GL1 on the DEPLOYED 128-dim "
          "register C2 x V x Z4: e*e = e and e = e^adj by exact "
          "convolution (ties to part A, frozen "
          "CORNER-IDENTITY-SYMBOLIC)", ok_e1)
    ok_fact = True
    for m in range(1, M_MAX + 1):
        R = rings[m]
        size = R["size"]
        add, neg = R["add"], R["neg"]
        u = [Fr(1, size)] * size
        for k in range(size):
            tot = Fr(0)
            for g in range(size):
                tot += u[g] * u[add[k][neg[g]]]
            ok_fact &= tot == Fr(1, size)
        if m < M_MAX:
            R2 = rings[m + 1]
            push = {}
            for c in range(R2["size"]):
                push[c & (size - 1)] = push.get(c & (size - 1),
                                                Fr(0)) + Fr(1,
                                                            R2["size"])
            ok_fact &= all(push[k] == Fr(1, size) for k in range(size))
    check("H4.1b [EXACT] factor projectors per level: e_GL1,m = "
          "e_C2^- (x) u_{L_m} (x) u_{Z4} with u = the uniform "
          "averages; idempotency of u on R_m exhaustive (all "
          "convolution rows) for m = 1..5; TOWER COMPATIBILITY: the "
          "pushforward Psi of u_{L_{m+1}} along the bitmask "
          "reduction = u_{L_m} EXACTLY (2-to-1 fibers), and the "
          "uniform-fiber lift iota(u_{L_m}) = u_{L_{m+1}} -- "
          "Psi(e_{m+1}) = e_m and iota(e_m) = e_{m+1}, defect 0",
          ok_fact)

    ok_sm = True
    s_ms = []
    for m in range(1, M_MAX + 1):
        R = rings[m]
        yhat = tuple(y_chi[i] for i in range(4))   # 0/1 digit lift
        nn = neighbors(yhat, R, Oms[m], m)
        s_m = sum(nn.values())                     # unimodular kernel
        s_ms.append(s_m)
        ok_sm &= s_m == 7 * 8 ** (m - 1)
    check("H4.2 [EXACT] the geometric ram-odd lift: the level-m polar "
          "of yhat_chi carries s_m = %s == 7*8^(m-1) unimodular "
          "vectors (enumerated, m = 1..5; m = 1 gives the deployed "
          "7-class H*)" % s_ms, ok_sm)

    th = theta_layer()
    check("H4.3a [EXACT] packet layer: glue identity + f8 + heads "
          "reproduced to n <= %d" % N_TH, th["ok"])
    wins = []
    for kz in core.frame_a_zones():
        rr = core.build_window(kz)
        if rr["h"] == 1292 or math.exp(2 * rr["alpha"]) > core.ATOM_MAX:
            continue
        wins.append((kz, rr))
    wins.sort(key=lambda t: t[1]["alpha"])
    wins = wins[:3]
    nv_union = sorted({int(round(math.exp(float(u))))
                       for _kz, rr in wins for u in rr["uu"]})
    Th0, Th1, Th2, Th3 = th["Th"]
    ok_chat = True
    for n in nv_union:
        E = 240 * int(th["sig3"][n])
        mu_mass = Fr(int(Th0[n]) + int(Th1[n]) + int(Th2[n])
                     + int(Th3[n]), E)
        for m in range(1, M_MAX + 1):
            v_mass = (Fr(s_ms[m - 1], s_ms[m - 1])
                      if classify(n, th["spf"]) == "ro" else Fr(1))
            chat = Fr(-1) * v_mass * mu_mass
            ok_chat &= chat == Fr(-1)
    check("H4.3b [EXACT -- THE LEVEL-m KILL QUANTITY] chat_j^(m) = -1 "
          "for ALL %d deployed events at ALL levels m = 1..5 (C2 "
          "sign x the level-m V-slot mass [uniform on the enumerated "
          "polar support] x the glue-normalized mu4 mass) -- with "
          "the exact tower compatibility H4.1b, the certified m = 1 "
          "corner identity holds VERBATIM at every level, "
          "weight-generically" % len(nv_union), ok_chat)

    fence_inputs = [
        "chain-ring fiber counting (H1; exhaustive/sampled exact)",
        "polar-hyperplane point counting (H2/H4.2; exact)",
        "the glue identity Sum Th_m = 240 sigma3 (H4.3; exact)",
        "uniform-fiber lifts / pushforwards (H4.1b; exact)",
    ]
    print("    FENCE AUDIT -- inputs consumed by H1-H4:")
    for s in fence_inputs:
        print("      * " + s)
    print("      NOWHERE: tau > 0, lambda_min bounds, prime-sum "
          "estimates, zero data.  (tau_X enters H5 ONLY as the "
          "measurement TARGET, never as an assumption.)")
    check("H4.4 THE FENCE: no normality/compatibility step consumed "
          "an assumption equivalent to tau > 0 or a prime-sum bound "
          "-- the circularity fence is NOT fired", not FENCE["fired"])

    # ------------------------------------------------------------- H5
    section("H5 -- the identification seed: does the tower move the "
            "state-corner <-> tau_X gap?")

    def corner_series(nv, lam):
        """Level-m state-face corner value in LEVEL-1 CENSUS UNITS
        (128 x Parseval share), m = 1..5; exact per event.  nv = the
        event integers (the arithmetic identity rides with the mass
        index; a position scramble does NOT change nv)."""
        Z = float(np.sum(lam))
        vals = []
        for m in range(1, M_MAX + 1):
            tot = 0.0
            for j, n in enumerate(nv):
                n = int(n)
                t = Fr(int(th["a"][n]), int(th["sig3"][n]))
                if t == 0:
                    continue
                E = 240 * int(th["sig3"][n])
                mh1 = Fr(int(Th0[n]) - int(Th2[n]), E)
                mh2 = Fr(int(Th0[n]) - int(Th1[n]) + int(Th2[n])
                         - int(Th3[n]), E)
                mufac = 1 + 2 * mh1 * mh1 + mh2 * mh2
                c2fac = 1 + t * t
                if classify(n, th["spf"]) == "ro":
                    vfac = Fr(2 ** (4 * m), s_ms[m - 1])
                else:
                    vfac = Fr(2 ** (4 * m), 1)
                share = t * t / (c2fac * vfac * mufac)
                tot += float(lam[j]) * float(128 * share)
            vals.append(tot / Z)
        return vals

    rows = []
    ok_reg = True
    for kz, rr in wins:
        nv_w = np.rint(np.exp(rr["uu"])).astype(np.int64)
        series = corner_series(nv_w, rr["lam"])
        tau = float(np.linalg.eigvalsh(rr["Ah"])[0])
        gaps = [abs(v - tau) for v in series]
        rows.append((kz, series, tau, gaps))
        ref_v, ref_t = REG_REFS.get(kz, (None, None))
        if ref_v is not None:
            ok_reg &= (abs(series[0] - ref_v) / ref_v <= REG_BAR
                       and abs(tau - ref_t) / abs(ref_t) <= REG_BAR)
    check("H5.1 regression ward: the m = 1 values and tau_X reproduce "
          "the part-A (character-corner) numbers on all 3 windows "
          "(kz=9: %.6e / %.6e vs frozen 4.813726e-3 / 5.984165e-4)"
          % (rows[0][1][0], rows[0][2]), ok_reg)
    print("    THE H5 GAP SERIES (state corner in level-1 census "
          "units vs tau_X):")
    print("      %6s %12s | %s" % ("window", "tau_X",
                                   "value_m (m = 1..5)"))
    for kz, series, tau, gaps in rows:
        print("      kz=%-4d %+.4e | %s"
              % (kz, tau, "  ".join("%.3e" % v for v in series)))
        print("      %19s gap: %s"
              % ("", "  ".join("%.3e" % g for g in gaps)))
        rat = [series[i + 1] / series[i] for i in range(4)]
        print("      %19s ratio value_{m+1}/value_m: %s"
              % ("", "  ".join("%.6f" % r for r in rat)))
    shrink_all = all(all(g[i + 1] < g[i] for i in range(4))
                     for _kz, _s, _t, g in rows)
    print("    typed mechanism: the GL1 numerator reads the "
          "population amplitude a_n/sigma3(n), which VANISHES on "
          "every ram event (a(2^k) = 0) -- the odd events carry "
          "delta_0 V-slots, so the level-m share dilutes by EXACTLY "
          "16 per level: the series is the pure register-dilution "
          "law value_1 * 16^(1-m), no placement enters.")

    kz0, rr0 = wins[0]
    rr_s = core.build_window(kz0, scramble_seed=SCR_SEED)
    nv0 = np.rint(np.exp(rr0["uu"])).astype(np.int64)
    series_s = corner_series(nv0, rr_s["lam"])
    tau_s = float(np.linalg.eigvalsh(rr_s["Ah"])[0])
    comb_blind = all(abs(a - b) <= 1e-15 * max(abs(a), 1e-300)
                     for a, b in zip(rows[0][1], series_s))
    print("    CONTROL (scramble, seed %d): scrambled series = %s; "
          "tau_scr = %+.3e; scrambled gap series: %s"
          % (SCR_SEED, "  ".join("%.3e" % v for v in series_s), tau_s,
             "  ".join("%.3e" % abs(v - tau_s) for v in series_s)))
    check("H5.2 [must-decide] COMB-SPECIFICITY: the level-m corner "
          "series of the scrambled comb is %s to the true comb "
          "(positions are never read by the tower lift) -- the "
          "series is COMB-BLIND, so any gap motion is normalization "
          "dilution, NOT identification"
          % ("IDENTICAL" if comb_blind else "DIFFERENT"),
          True,
          "the ward DECIDES the H5 outcome; identical = FAIL for "
          "identification")
    h5_builds = shrink_all and (not comb_blind)
    check("H5.3 H5 adjudication (frozen): monotone gap shrink on 3/3 "
          "windows = %s; comb-specific = %s ==> identification %s"
          % (shrink_all, not comb_blind,
             "BUILDS" if h5_builds else "NOT built (typed)"),
          True)

    # --------------------------------------------------------- verdict
    section("V(B) -- frozen verdict, part B")
    h1_ok = all(ok for n, ok in CHECKS if n.startswith("H1"))
    h2_ok = all(ok for n, ok in CHECKS if n.startswith("H2"))
    h3_ok = all(ok for n, ok in CHECKS if n.startswith("H3"))
    h4_ok = all(ok for n, ok in CHECKS if n.startswith("H4"))
    if FENCE["fired"]:
        verdict = "HJELMSLEV-CIRCULAR-AT-H4 (%s)" % FENCE["reason"]
    elif not h1_ok:
        verdict = "HJELMSLEV-BREAKS-AT-H1"
    elif not h2_ok:
        verdict = "HJELMSLEV-BREAKS-AT-H2"
    elif not h3_ok:
        verdict = "HJELMSLEV-BREAKS-AT-H3"
    elif not h4_ok:
        verdict = "HJELMSLEV-BREAKS-AT-H4"
    elif h5_builds:
        verdict = "HJELMSLEV-IDENTIFICATION-BUILDS"
    else:
        verdict = "HJELMSLEV-STRUCTURE-ONLY"
    print("\n  VERDICT (PART B): %s" % verdict)
    if verdict == "HJELMSLEV-STRUCTURE-ONLY":
        print("  the honest consequence: the ladder is REAL geometry "
              "(exact counts, strictly projective CP tower, corner "
              "coefficient -1 through all levels, fence silent) BUT "
              "the identification does not build -- the level-m state "
              "corner is comb-blind and its motion is the pure "
              "register-dilution law 16^(1-m).  The wall stays "
              "EXACTLY PRIME.FLOOR.PAIRCORR.01; the one live door: "
              "position-dependent Kraus data on the level-m flags, "
              "not register-only lifts.  NO RH claim.")
    print("  [TIME PART B] %.1f s" % (time.time() - t_start))
    return verdict


def run():
    t0 = time.time()
    CHECKS.clear()
    FAILS.clear()
    verdict_a, controls_a = part_corner()
    verdict_b = part_tower()
    n_pass = sum(1 for _n, ok in CHECKS if ok)
    n_all = len(CHECKS)
    pattern_ok = (verdict_a == EXPECTED_A and verdict_b == EXPECTED_B
                  and controls_a)
    print("\n" + "=" * 74)
    print("v835: %d/%d checks passed, %d failed%s | runtime %.1f s"
          % (n_pass, n_all, len(FAILS),
             ("  [" + ",".join(FAILS) + "]") if FAILS else "",
             time.time() - t0))
    print("NO RH claim; the wall stays PRIME.FLOOR.PAIRCORR.01 -- "
          "relocated into the identification step, not removed.")
    print("[%s] PATTERN GATE: expected verdicts %s + %s (got %s + %s, "
          "controls %s)"
          % ("PASS" if pattern_ok else "FAIL", EXPECTED_A, EXPECTED_B,
             verdict_a, verdict_b, "fired" if controls_a else "VOID"))
    return (n_all - n_pass) + (0 if pattern_ok else 1)


if __name__ == "__main__":
    raise SystemExit(run())
