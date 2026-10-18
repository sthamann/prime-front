#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""v838 -- PRIME.CORNER.EXPECTATION.01 + PRIME.CARRIER.POSITION.01: the compression toolkit closes and the position-dependent carrier map is extremally pinned -- the rank-1 corner dichotomy extends to EVERY conditional expectation, the full pinching and Stinespring-side compressions, and carrier-side position dependence is incompatible with (state AND identity AND separation of self-consistent combs): the fourth wall coordinate typed (EXTREMAL PINNING), ONE module from two probes (13/13 + 13/13 checks, verdicts EXPECTATION-CLOSED and POSITION-CARRIER-TRADEOFF; discovery probes conditional_expectation_probe.py and position_carrier_probe.py, 2026-08-07, re-run identically at promotion, promoted VERBATIM with no downscoping, ~5 s).  PART A, THE COMPRESSION TOOLKIT (the definitive class closure): (i) THE FULL SUBGROUP LATTICE -- all 5276 subgroups of G = C2 x F2^4 x Z4 enumerated (order histogram 1/63/683/1891/1891/683/63/1), all 74259 conditional-expectation components measured: identity(E_H) holds for EXACTLY 2 subgroups (G and ker psi0), equal to the predicted pinning criterion Ann(H) subset {1, psi0} subgroup by subgroup; NO component of ANY expectation carries identity AND visibility (0 violations of 74259; 0 accidental invisibles); the full average E_e reads exactly ZERO (compression coarser than the C2 grading loses the object); the E_H ward exact on all 4 representatives ((1/|A|) Sum_{psi in Ann(H)} psi(g) == 1_{g in H}, integer i-power sums).  (ii) THE FULL PINCHING -- completeness Sum_chi chi(g) = 128 delta_g exact; the direct sum holds identity and placement only in DIFFERENT summands, and the positivity census shows the ONLY PSD summands at the deployed weights are the two pinned chat = -1 sectors (+4.037e-04; every other sector NEG down to -15.3): no positive object has the deployed pinching -- pinched-family positivity transport collapses back to the GL1 corner (the joint-use kill).  (iii) STINESPRING -- dilation wards exact in the genuine 105-leg dilation space (W^dag W = diag(rowsum), W^dag (f x 1) W = Phi_xi(f)); the position-weighted raw compression vector sees placement but pays the identity defect 6.721e-02 coefficient for coefficient; the row-normalized (identity-true) vector differs from uniform AT LEG LEVEL (1.366e-02 -- the position data IS in the dilation) yet has the IDENTICAL corner: the dilated read is a positive leg functional the identity pins to the constant 1.  PART B, THE POSITION CARRIER (candidate 1 executed): four frozen state-preserving designs (consistency router A on the (1+i)-adic tower address addr(n) with period 4; mu4 rotation B1; absolute C2 grading B2; normalized V grading C) -- ALL pass the state ward (positive, unit mass, inversion-symmetric; spectrum real with |chat| <= 1); identity at truth INHERITED verbatim for A (beta_j = 0 at truth, weight-for-weight dict equality), B1/C GL1-invisible (2.7e-14), B2 breaks at truth by the DERIVED defect 2 max|q_j| = 2.343308 (matched to 1e-9); placement fires for A (scramble 51/70, Epstein 56/70 events flagged) -- BUT THE DECISIVE NULL: on the SELF-CONSISTENT Epstein comb (sums of two squares at their OWN log positions) variant A reads beta == 0 EVERYWHERE, corner excess 0.0 IDENTICAL to truth: NO variant separates the true comb from the self-consistent fake (SEP = 0 for all four).  THE STRUCTURAL REASON, named EXTREMAL PINNING (the fourth wall coordinate): for any state carrier the GL1 read is a mass difference in [-1, 1] and the deployed-form identity demands the EXTREME point -1 (the entire C2 mass locked) at every true configuration -- the only position dependence compatible with state + identity is a nonnegative consistency defect (1 + chat)/2 that vanishes on EVERY self-consistent comb, true or fake.  THE CLOSURE: no compression-based route AND no state-preserving position-dependent carrier map reopens the corner route -- the identification datum at the wall is WHICH self-consistent comb is real, information no identity-true carrier F(n, u) can encode; what would escape: giving up manifest state positivity, or the pair-correlation substance itself.  The wall stays EXACTLY PRIME.FLOOR.PAIRCORR.01 with all four coordinates typed (register closed, factor pinned, tower level-exact, carrier extremally pinned); stop-list entries PRIME.CORNER.EXPECTATION.01 / PRIME.CARRIER.POSITION.01.  NO RH claim.  Python-only per GATE.WOLFRAM.02.

PROVENANCE: discovery probes conditional_expectation_probe.py (13/13,
verdict EXPECTATION-CLOSED) and position_carrier_probe.py (13/13,
verdict POSITION-CARRIER-TRADEOFF), both 2026-08-07, re-run
identically at promotion; this module runs both frozen protocols
VERBATIM (~5 s; a module-level _VERDICTS capture inserted at the
frozen verdict per the v817/v791 precedent -- no gate, bar or table
changed).  The original probe docstrings, frozen specs
(SHA-256-printed) and decision trees live in the probe files verbatim
(experiments/tfpt-discovery/).

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
from itertools import combinations

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

REG_REFS = {9: 5.984165e-4, 12: 4.351189e-4, 13: 5.637632e-4}

REG_BAR = 1.0e-4

BANNED_IDS = ("zetazero", "nzeros", "primerange", "isprime", "primepi",
              "nextprime", "prevprime")

CHECKS = []

FAILS = []

CONTROL = {}

T0 = time.time()

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

def chival(chi, g):
    eps, w, j = chi
    a, v, m = g
    s = (-1) ** (eps * a) * (-1) ** (bin(w & v).count("1"))
    q = (j * m) % 4
    return [(s, 0), (0, s), (-s, 0), (0, -s)][q]

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

def blk2(tBf, cvec, lam, q3):
    s0 = float(np.sum(cvec * lam * q3[:, 0]))
    s1 = float(np.sum(cvec * lam * q3[:, 1]))
    sx = float(np.sum(cvec * lam * q3[:, 2]))
    return np.array([[tBf[0] - s0, tBf[2] - sx],
                     [tBf[2] - sx, tBf[1] - s1]])

def id_dev(tBf, cvec, q3, B, Xn):
    d = max(abs(B[0, 0] - tBf[0]), abs(B[1, 1] - tBf[1]),
            abs(B[0, 1] - tBf[2]))
    for s in range(3):
        d = max(d, float(np.max(np.abs(cvec * q3[:, s] - Xn[:, s]))))
    return d


# =============== PART A -- conditional_expectation_probe.py (frozen probe, verbatim)

FROZEN_SPEC_a = """\
PRIME.CORNER.EXPECTATION.01 spec v2 (2026-08-07, frozen before run;
v2 = honest wording of the S3 positivity claim only, no gate change).
(i) E_H for EVERY subgroup H <= G = C2 x F2^4 x Z4: BFS enumeration
of the full subgroup lattice (abelian closure <S, g> = union of
S g^k); E_H components = Ann(H)-coset averages of chat; identity(E_H)
<=> GL1-coset average == -1 all events <=> Ann(H) subset {1, psi0}
(measured equivalence over ALL subgroups; chat in [-1,1] forces the
coset to be pinned); componentwise dichotomy (identity ==> invisible)
checked for EVERY component of EVERY subgroup (tol 1e-12 on
|coeff + 1|, visibility bar 1e-9 scale on the excess); placement on
4 predeclared reps (G, ker psi0, C2xVx{0}, {e}); E_H ward: (1/|A|)
sum_psi psi(g) == 1_{g in H} exact (integer i-power sums) per rep.
(ii) pinching: completeness sum_chi chi(g) == 128 delta_g exact; the
positivity census of the 18 class-rep sector windows (full h x h
odd-Toeplitz, coeff -chat, deployed weights; PSD bar -1e-10 ||T||):
PSD set must be censused and compared to the pinned set {(1,0,0),
(1,w0,0)}; the pinned sector windows must be strictly PSD (the raw
arch+comb Toeplitz, sign of tau_X; NOT the boundary-corrected Ah, so
value equality is not claimed).  (iii) dilation: W|x> = sum xi_xy
|y>|xy>; wards W^dag W =
diag(rowsum), W^dag (f x 1) W == Phi_xi(f) (1e-12, random f, LCG);
variants xi-uniform / xi-raw (tradeoff v2 leg field, kappa = 1/4) /
xi-normalized; dilated read c(n) = -(1/7) sum_{H*} s(x) (ro), -1
(else); cells with the open-doors gates, fields rebuilt per position
set (scramble seed 1, Epstein comb); the exhibit: xi-normalized !=
xi-uniform at leg level but identical corner.  CONTROLS: GL1 anchor
exact (union events); product law all 128 chars x primary events
exact; tau_X 3 windows (1e-6 rel, frozen refs); rank-1 none-row
identity cells == {(1,0,0),(1,w0,0)}.  LCG 20260807.  VERDICTS:
EXPECTATION-CARRIES / EXPECTATION-CLOSED / EXPECTATION-PARTIAL.
NO RH claim; writes nothing.
"""

TOL_ID = 1.0e-12

PSD_BAR = 1.0e-10

_LCG = [20260807]

def lcg_float():
    _LCG[0] = (1103515245 * _LCG[0] + 12345) % (1 << 31)
    return _LCG[0] / float(1 << 31)

G_ELEMS = [(a, v, m) for a in range(2) for v in range(16) for m in range(4)]

G_IDX = {g: i for i, g in enumerate(G_ELEMS)}

def fourier(f, chi):
    re = Fr(0)
    im = Fr(0)
    for g, fg in f.items():
        cr, ci = chival(chi, g)
        re += fg * cr
        im += fg * ci
    return re, im

def sum2sq_positions(count):
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

def chat_product(n, chi, th, Hs):
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

def unit_rows_a(rr, positions=None):
    uu = rr["uu"] if positions is None else positions
    out = np.zeros((len(uu), 2 * rr["h"]))
    for j, u in enumerate(uu):
        out[j] = core.atom_lags_at(rr["alpha"], rr["M"], [float(u)],
                                   [2.0])[0]
    return out

def reads_pair_a(rr, rows):
    """Undressed lock-pair reads q3 (ka x 3) and arch tuple."""
    t1, t2 = rr["t1"], rr["t2"]
    ka = rows.shape[0]
    q3 = np.zeros((ka, 3))
    for j in range(ka):
        R = core.odd_toeplitz(rows[j], rr["M"])
        q3[j, 0] = t1 @ (R @ t1)
        q3[j, 1] = t2 @ (R @ t2)
        q3[j, 2] = t1 @ (R @ t2)
        del R
    c_ar = np.asarray(core.arch_lags(rr["M"], rr["D"]), float)
    T = core.odd_toeplitz(c_ar, rr["M"])
    tB = (float(t1 @ (T @ t1)), float(t2 @ (T @ t2)),
          float(t1 @ (T @ t2)))
    del T
    return q3, tB, c_ar

def position_leg_field(Hs, nvals, uu, lam, alpha, spf, legs):
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

def part_a():
    section("PRIME.CORNER.EXPECTATION.01 -- beyond corners: the "
            "compression toolkit (EXPLORATION ONLY)")
    sha = hashlib.sha256(FROZEN_SPEC_a.encode("utf-8")).hexdigest()
    print("    FROZEN_SPEC_a SHA-256 = %s" % sha)
    print("    the honest frame: the rank-1 dichotomy (visibility "
          "<=> identity defect) is the input theorem; find where it "
          "FAILS for higher-rank compressions, or prove it extends.  "
          "NO RH claim.")

    print("\nS0 -- firewall")
    bad = ast_firewall()
    check("S0.1 AST firewall: no zeta-zero / prime-table symbol",
          not bad, "found %s" % bad if bad else "clean")

    # ------------------------------------------------------------ frame
    section("S1 -- packet layer, frame, windows, rank-1 anchors")
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
    w0 = next(w for w in range(1, 16)
              if all(bin(w & v).count("1") % 2 == 0 for v in Hs))
    w14 = min(w for w in range(1, 16) if w != w0)

    wins = deployed_windows()
    nv_union = sorted({int(round(math.exp(float(u))))
                       for _kz, rr in wins for u in rr["uu"]})
    ok_id = True
    for kz, rr in wins:
        nv = np.rint(np.exp(rr["uu"])).astype(np.int64)
        q3w, tBw, _ = reads_pair_a(rr, unit_rows_a(rr))
        tau_X = float(np.linalg.eigvalsh(rr["Ah"])[0])
        tau0 = float(np.linalg.eigvalsh(
            blk2(tBw, -np.ones(len(nv)), rr["lam"], q3w))[0])
        scale = max(1.0, abs(tBw[0]), abs(tBw[1]))
        ok_id &= (abs(tau0 - tau_X) / scale <= BAR_ID_REL
                  and abs(tau_X - REG_REFS[kz]) / REG_REFS[kz]
                  <= REG_BAR)
    CONTROL["REDUCTION"] = ok_id
    check("S1.2 [CONTROL] the corner reduction reproduces tau_X on "
          "all %d windows (frozen refs matched)" % N_WIN, ok_id)

    kz0, rr0 = wins[0]
    h0, M0, alpha0 = rr0["h"], rr0["M"], float(rr0["alpha"])
    lam0 = rr0["lam"]
    nv0 = np.rint(np.exp(rr0["uu"])).astype(np.int64)
    ka0 = len(nv0)
    uu_t = np.asarray(rr0["uu"], float)
    uu_s = np.asarray(core.build_window(kz0, scramble_seed=SCR_SEED)
                      ["uu"], float)
    uu_e = sum2sq_positions(ka0)
    Xn0, B0 = rr0["Xn"], rr0["B"]
    rows_t = unit_rows_a(rr0, positions=uu_t)
    q3 = {}
    tB = {}
    c_ar0 = None
    for p, uu in (("t", uu_t), ("s", uu_s), ("e", uu_e)):
        rows_p = rows_t if p == "t" else unit_rows_a(rr0, positions=uu)
        q3[p], tB[p], c_ar = reads_pair_a(rr0, rows_p)
        if p == "t":
            c_ar0 = c_ar
            rows_true = rows_p

    # exact product-law anchor on all 128 chars x primary events
    t0 = time.time()
    CHARS = [(eps, w, j) for eps in range(2) for w in range(16)
             for j in range(4)]
    bad_pl = []
    for n in sorted(set(int(x) for x in nv0)):
        c = event_carrier_element(n, th, Hs)
        for chi in CHARS:
            re, im = fourier(c, chi)
            if im != 0 or re != chat_product(n, chi, th, Hs):
                bad_pl.append((n, chi))
    off = [n for n in nv_union
           if chat_product(n, (1, 0, 0), th, Hs) != Fr(-1)]
    CONTROL["GL1"] = (not bad_pl) and (not off)
    check("S1.3 [EXACT -- CONTROL] product law chat = (-1)^eps Vfac "
          "Mfac verified vs the full carrier Fourier (128 chars x "
          "%d primary events); GL1 anchor chat = -1 on all %d union "
          "events" % (len(set(int(x) for x in nv0)), len(nv_union)),
          CONTROL["GL1"], "%.1f s" % (time.time() - t0))

    CHAT = np.array([[float(chat_product(int(n), chi, th, Hs))
                      for n in nv0] for chi in CHARS])
    scale0 = max(float(np.max(np.abs(B0))), float(np.max(np.abs(Xn0))),
                 float(np.max(np.abs(q3["t"]))), 1.0)
    bar_coef = BAR_COEF_REL * scale0
    cm1 = -np.ones(ka0)
    blk_gl1 = {p: blk2(tB[p], cm1, lam0, q3[p]) for p in ("t", "s", "e")}
    tau0_pi = {p: float(np.linalg.eigvalsh(blk_gl1[p])[0])
               for p in ("t", "s", "e")}
    E3 = {p: lam0[:, None] * q3[p] for p in ("t", "s", "e")}

    # rank-1 regression: none-row identity cells
    id_cells = []
    for ci, chi in enumerate(CHARS):
        if float(np.max(np.abs(CHAT[ci] + 1.0))) <= TOL_ID:
            id_cells.append(chi)
    CONTROL["RANK1"] = sorted(id_cells) == sorted([(1, 0, 0),
                                                   (1, w0, 0)])
    check("S1.4 [CONTROL] rank-1 regression: the characters with "
          "chat == -1 on all events are exactly {(1,0,0), (1,%d,0)} "
          "-- the open-doors pinned pair" % w0, CONTROL["RANK1"])

    # ------------------------------------------------- (i) expectations
    section("S2 -- (i) conditional expectations E_H onto C[H]: the "
            "FULL subgroup lattice")
    # group tables (indices: a*64 + v*4 + m)
    A_arr = np.array([g[0] for g in G_ELEMS])
    V_arr = np.array([g[1] for g in G_ELEMS])
    M_arr = np.array([g[2] for g in G_ELEMS])
    GT = ((A_arr[:, None] ^ A_arr[None, :]) * 64
          + (V_arr[:, None] ^ V_arr[None, :]) * 4
          + (M_arr[:, None] + M_arr[None, :]) % 4)
    INV = (A_arr * 64 + V_arr * 4 + (-M_arr) % 4)
    EXPT = np.zeros((128, 128), dtype=np.int64)
    for ci, (eps, w, j) in enumerate(CHARS):
        EXPT[ci] = (2 * eps * A_arr
                    + 2 * np.array([bin(w & v).count("1")
                                    for v in V_arr])
                    + j * M_arr) % 4
    TR = GT[:, INV]           # TR[x, h] = x * h^{-1}
    P2 = np.array([GT[g, g] for g in range(128)])
    P3 = np.array([GT[P2[g], g] for g in range(128)])

    t0 = time.time()
    start = np.zeros(128, dtype=bool)
    start[0] = True
    seen = {start.tobytes()}
    queue = [start]
    subs = [start]
    while queue:
        S = queue.pop()
        for g in range(1, 128):
            if S[g]:
                continue
            T = (S | S[TR[:, g]] | S[TR[:, P2[g]]] | S[TR[:, P3[g]]])
            key = T.tobytes()
            if key not in seen:
                seen.add(key)
                queue.append(T)
                subs.append(T)
    orders = {}
    for S in subs:
        o = int(S.sum())
        orders[o] = orders.get(o, 0) + 1
    check("S2.1 the FULL subgroup lattice of G enumerated by abelian "
          "BFS closure: %d subgroups (order histogram %s)"
          % (len(subs), {k: orders[k] for k in sorted(orders)}),
          len(subs) > 100 and orders.get(1) == 1
          and orders.get(128) == 1, "%.1f s" % (time.time() - t0))

    idx_gl1 = CHARS.index((1, 0, 0))
    idx_psi0 = CHARS.index((0, w0, 0))
    t0 = time.time()
    n_identity = 0
    n_id_pred = 0
    equiv_ok = True
    viol_IV = 0
    n_accidental = 0
    total_comps = 0
    for S in subs:
        Hidx = np.flatnonzero(S)
        Amask = ~np.any(EXPT[:, Hidx], axis=1)
        Aidx = np.flatnonzero(Amask)
        cid = GT[:, Aidx].min(axis=1)
        order = np.argsort(cid, kind="stable")
        sc = cid[order]
        starts = np.flatnonzero(np.r_[True, sc[1:] != sc[:-1]])
        counts = np.diff(np.r_[starts, 128])
        Csum = np.add.reduceat(CHAT[order], starts, axis=0)
        C = Csum / counts[:, None]
        devs = np.max(np.abs(C + 1.0), axis=1)
        BD = np.max(np.abs((C + 1.0) @ E3["t"]), axis=1)
        total_comps += len(starts)
        # the GL1-containing component
        gid = cid[idx_gl1]
        gl_row = int(np.searchsorted(sc[starts], gid))
        has_id = devs[gl_row] <= TOL_ID
        pred = set(Aidx.tolist()) <= {0, idx_psi0}
        n_identity += has_id
        n_id_pred += pred
        equiv_ok &= (has_id == pred)
        viol_IV += int(np.sum((devs <= TOL_ID) & (BD > bar_coef)))
        n_accidental += int(np.sum((BD <= bar_coef) & (devs > TOL_ID)))
    check("S2.2 [THE LATTICE CENSUS] over ALL %d subgroups (%d "
          "components total): identity(E_H) holds for EXACTLY %d "
          "subgroups, == the predicted pinning criterion Ann(H) "
          "subset {1, psi0} (%d; equivalence holds subgroup by "
          "subgroup) -- every other expectation DESTROYS the "
          "deployed-form component outright (averaging chat over a "
          "non-pinned coset moves it off -1)"
          % (len(subs), total_comps, n_identity, n_id_pred),
          equiv_ok and n_identity == 2 and n_id_pred == 2,
          "%.1f s" % (time.time() - t0))
    check("S2.3 [THE DICHOTOMY, all components] no component of ANY "
          "E_H carries identity AND visibility (violations: %d of "
          "%d); accidental invisibles (excess == 0 without the "
          "identity): %d" % (viol_IV, total_comps, n_accidental),
          viol_IV == 0)

    # representative subgroups with placement
    reps = [("E_G = id (full pinching)",
             np.ones(128, dtype=bool)),
            ("E_{ker psi0} (largest identity-preserving)",
             np.array([bin(w0 & V_arr[i]).count("1") % 2 == 0
                       for i in range(128)])),
            ("E_{C2 x V} (mu4 killed)",
             np.array([M_arr[i] == 0 for i in range(128)])),
            ("E_{e} (full average)", start.copy())]
    ward_ok = True
    for name, S in reps:
        Hidx = np.flatnonzero(S)
        Amask = ~np.any(EXPT[:, Hidx], axis=1)
        Aidx = np.flatnonzero(Amask)
        # exact E_H ward: (1/|A|) sum_psi psi(g) == 1_{g in H}
        for gi in range(128):
            ex = EXPT[Aidx, gi]
            nbk = np.bincount(ex, minlength=4)
            val = (int(nbk[0] - nbk[2]), int(nbk[1] - nbk[3]))
            tgt = (len(Aidx), 0) if S[gi] else (0, 0)
            ward_ok &= val == tgt
        cid = GT[:, Aidx].min(axis=1)
        order = np.argsort(cid, kind="stable")
        sc = cid[order]
        starts = np.flatnonzero(np.r_[True, sc[1:] != sc[:-1]])
        counts = np.diff(np.r_[starts, 128])
        C = np.add.reduceat(CHAT[order], starts, axis=0) \
            / counts[:, None]
        devs = np.max(np.abs(C + 1.0), axis=1)
        Ex = {p: -(C + 1.0) @ E3[p] for p in ("t", "s", "e")}
        vis = np.max(np.abs(Ex["t"]), axis=1) > bar_coef
        plc = ((np.max(np.abs(Ex["t"] - Ex["s"]), axis=1) > BAR_MOVE)
               & (np.max(np.abs(Ex["t"] - Ex["e"]), axis=1) > BAR_MOVE))
        idc = devs <= TOL_ID
        gid = cid[idx_gl1]
        gl_row = int(np.searchsorted(sc[starts], gid))
        maxread = float(np.max(np.abs(C)))
        print("    %-42s |H|=%3d comps=%3d  identity=%d visible=%d "
              "placement=%d  I&V=%d  GL1-comp: %s  max|read|=%.3f"
              % (name, int(S.sum()), len(starts), int(idc.sum()),
                 int(vis.sum()), int(plc.sum()),
                 int(np.sum(idc & vis)),
                 "identity" if idc[gl_row] else "broken", maxread))
    check("S2.4 [EXACT] the E_H ward on all 4 representatives: "
          "(1/|A|) sum_{psi in Ann(H)} psi(g) == 1_{g in H} for all "
          "128 g (integer i-power sums) -- E_H IS the average of "
          "character automorphisms: unital, CP, a genuine "
          "conditional expectation", ward_ok)
    print("    typed: E_{e} (the full average / the canonical trace) "
          "reads EXACTLY ZERO on every event -- the C2 average "
          "annihilates the sign carrier; compression coarser than "
          "the C2 grading loses the object entirely, never gains.")

    # ---------------------------------------------------- (ii) pinching
    section("S3 -- (ii) the full character pinching: direct sum + "
            "the positivity census")
    ok_comp = True
    for gi in range(128):
        ex = EXPT[:, gi]
        nbk = np.bincount(ex, minlength=4)
        val = (int(nbk[0] - nbk[2]), int(nbk[1] - nbk[3]))
        ok_comp &= val == ((128, 0) if gi == 0 else (0, 0))
    check("S3.1 [EXACT] pinching completeness: sum_chi chi(g) = 128 "
          "delta_g over all 128 g -- Sigma e_chi = 1, the pinching "
          "is a unital CP sum of the 128 rank-1 corners; on abelian "
          "C[G] the pinched matrix IS the direct sum of the corners "
          "(no off-diagonal survives)", ok_comp)

    col_reps = [(eps, w, j) for eps in (1, 0) for w in (0, w0, w14)
                for j in (0, 1, 2)]
    tau_X0 = float(np.linalg.eigvalsh(rr0["Ah"])[0])
    psd_set = []
    print("    the positivity census (full h x h sector windows at "
          "the deployed weights, primary window kz=%d, tau_X = "
          "%+.6e):" % (kz0, tau_X0))
    for chi in col_reps:
        coeff = np.array([-float(chat_product(int(n), chi, th, Hs))
                          for n in nv0])
        lag = c_ar0 + (coeff * lam0) @ rows_true
        Tw = core.odd_toeplitz(lag, M0)
        ev = np.linalg.eigvalsh(Tw)
        del Tw
        lmin = float(ev[0])
        nrm = float(np.max(np.abs(ev)))
        psd = lmin >= -PSD_BAR * nrm
        if psd:
            psd_set.append(chi)
        pinned = chi in ((1, 0, 0), (1, w0, 0))
        print("      chi=(eps=%d,w=%2d,j=%d): lambda_min = %+.3e  "
              "[%s]%s" % (chi[0], chi[1], chi[2], lmin,
                          "PSD" if psd else "NEG",
                          "  <-- pinned (chat == -1 sector)"
                          if pinned else ""))
    pinned_set = [(1, 0, 0), (1, w0, 0)]
    CONTROL["PSD"] = sorted(psd_set) == sorted(pinned_set)
    check("S3.2 [THE JOINT-USE KILL] the PSD components of the "
          "pinched packet operator are EXACTLY the pinned classes "
          "%s (strictly PSD, sign of tau_X; the raw sector Toeplitz, "
          "not the boundary-corrected block, so no value equality "
          "claimed): "
          "no positive object has the deployed pinching, so a "
          "positivity-transporting identification through the "
          "pinched FAMILY reduces to the GL1 corner -- the direct "
          "sum carries identity and placement only in DIFFERENT "
          "components, and the placement components are exactly the "
          "non-positive ones" % pinned_set, CONTROL["PSD"])

    # ---------------------------------------------------- (iii) dilation
    section("S4 -- (iii) Stinespring-side compression in the 105-leg "
            "dilation space")
    fld = {}
    for p, uu in (("t", uu_t), ("s", uu_s), ("e", uu_e)):
        fld[p], _cs = position_leg_field(Hs, nv0, uu, lam0, alpha0,
                                         th["spf"], legs)

    def xi2_variant(kind, p):
        if kind == "uniform":
            return {le: 1.0 / 7.0 for le in legs}
        raw = {le: (1.0 + KAPPA * fld[p][le]) / 7.0 for le in legs}
        if kind == "raw":
            return raw
        out = {}
        for x in labels15:
            s = sum(raw[(x, y)] for y in nb[x])
            for y in nb[x]:
                out[(x, y)] = raw[(x, y)] / s
        return out

    # dilation wards (uniform + raw), random f, LCG
    leg_idx = {le: i for i, le in enumerate(legs)}
    ok_dil = True
    for kind in ("uniform", "raw"):
        x2 = xi2_variant(kind, "t")
        W = np.zeros((15 * 105, 15))
        for (x, y) in legs:
            W[(y - 1) * 105 + leg_idx[(x, y)], x - 1] = \
                math.sqrt(x2[(x, y)])
        WtW = W.T @ W
        rowsum = np.array([sum(x2[(x, y)] for y in nb[x])
                           for x in labels15])
        ok_dil &= float(np.max(np.abs(WtW - np.diag(rowsum)))) \
            <= BAR_EXACT
        f = np.array([2.0 * lcg_float() - 1.0 for _ in range(15)])
        big = np.kron(np.diag(f), np.eye(105))
        lhs = np.diag(W.T @ (big @ W))
        rhs = np.array([sum(x2[(x, y)] * f[y - 1] for y in nb[x])
                        for x in labels15])
        ok_dil &= float(np.max(np.abs(lhs - rhs))) <= BAR_EXACT
    check("S4.1 [EXACT to float] dilation wards: W^dag W = "
          "diag(rowsum) (isometry iff rows normalized) and "
          "W^dag (f (x) 1) W == Phi_xi(f) for random f -- the "
          "compression lives in the genuine Stinespring space of "
          "the deployed 105-leg channel; the flags are explicit "
          "basis legs there", ok_dil)

    def dil_cvec(kind, p):
        x2 = xi2_variant(kind, p)
        sfun = {x: sum(x2[(x, y)] for y in nb[x]) for x in labels15}
        val_ro = -sum(sfun[x] for x in Hs) / 7.0
        return np.array([val_ro if classify(int(n), th["spf"]) == "ro"
                         else -1.0 for n in nv0])

    dil_cells = {}
    for kind in ("uniform", "raw", "normalized"):
        cvec_t = dil_cvec(kind, "t")
        dev = id_dev(tB["t"], cvec_t, q3["t"], B0, Xn0)
        bt = blk2(tB["t"], cvec_t, lam0, q3["t"])
        bd = float(np.max(np.abs(bt - blk_gl1["t"])))
        dl = {}
        for p in ("t", "s", "e"):
            cv = dil_cvec(kind, p)
            bp = blk2(tB[p], cv, lam0, q3[p])
            dl[p] = float(np.linalg.eigvalsh(bp)[0]) - tau0_pi[p]
        I = dev <= bar_coef
        Vv = bd > bar_coef
        P = (abs(dl["t"] - dl["s"]) > BAR_MOVE
             and abs(dl["t"] - dl["e"]) > BAR_MOVE)
        dil_cells[kind] = (I, Vv, P, dev, bd, dl["t"])
        print("    xi-%-11s IVP=%d%d%d  defect=%.3e  bdiff=%.3e  "
              "delta=%+.3e" % (kind, I, Vv, P, dev, bd, dl["t"]))
    x2u = xi2_variant("uniform", "t")
    x2n = xi2_variant("normalized", "t")
    kdiff = max(abs(x2u[le] - x2n[le]) for le in legs)
    ok_dcells = (dil_cells["uniform"][:3] == (True, False, False)
                 and dil_cells["raw"][:3] == (False, True, True)
                 and dil_cells["normalized"][:3] == (True, False, False)
                 and kdiff > 1e-6)
    check("S4.2 the dilated corner obeys the SAME dichotomy: uniform "
          "xi reproduces the base corner (identity, invisible); the "
          "position-weighted raw xi sees placement (visible, "
          "placement-sensitive) but breaks the identity by exactly "
          "the injected leg weight; the row-normalized xi differs "
          "from uniform at leg level (max leg diff %.3e -- the "
          "position data IS in the dilation) yet has the identical "
          "corner: the dilated read is the POSITIVE leg functional "
          "s(x), and the identity pins it to the constant 1"
          % kdiff, ok_dcells)

    # --------------------------------------------------------- verdict
    section("V -- FROZEN VERDICT + the honest consequence")
    carriers = []
    if viol_IV > 0:
        carriers.append("E_H component")
    for kind, cell in dil_cells.items():
        if cell[0] and cell[1] and cell[2]:
            carriers.append("dilation xi-%s" % kind)
    controls_ok = all(CONTROL.values())
    closed = (equiv_ok and n_identity == 2 and viol_IV == 0
              and ward_ok and ok_comp and CONTROL["PSD"]
              and ok_dil and ok_dcells and controls_ok)
    if carriers:
        verdict = "EXPECTATION-CARRIES (%s)" % ", ".join(carriers)
    elif closed:
        verdict = "EXPECTATION-CLOSED"
    else:
        verdict = "EXPECTATION-PARTIAL"
    print("\n  VERDICT: %s" % verdict)
    if verdict == "EXPECTATION-CLOSED":
        print("""
  THE DICHOTOMY EXTENDS TO THE FULL COMPRESSION TOOLKIT (the
  definitive class closure).  Measured, with the exact quantifier:
  (i) for EVERY subgroup H <= G (%d subgroups, %d components) the
  conditional expectation E_H reads only Ann(H)-coset AVERAGES of
  the character coefficients -- position-blind functionals of the
  carrier; exactly TWO subgroups (G and ker psi0) retain the
  deployed-form component at all, that component is the pinned GL1
  block (invisible), and NO component of ANY expectation carries
  identity and visibility together; the full average E_e reads zero.
  (ii) the full pinching is the direct sum of the 128 corners
  (completeness exact); it holds identity and placement only in
  DIFFERENT summands, and the positivity census shows the only PSD
  summands at the deployed weights are the two pinned chat == -1
  sectors: no positive operator has the deployed
  pinching, so pinched-family positivity transport collapses back to
  the GL1 corner.  (iii) the Stinespring dilation exposes the 105
  flags as explicit legs, and a position-weighted compression vector
  does see placement -- but the dilated corner reads a POSITIVE leg
  functional s(x) that the identity pins to the constant 1: the
  normalized (identity-true) compression is corner-identical to the
  uniform one, the raw (placement-seeing) compression pays the
  identity defect coefficient for coefficient.  In every structure
  the mechanism is the same equation: the deployed-form identity
  pins the reading, so visibility is bought only by breaking it.

  THE HONEST CONSEQUENCE ACROSS BOTH ESCALATIONS (one paragraph):
  no compression-based route to the identification remains inside
  the deployed register machinery.  The excluded class, with the
  quantifier now measured: ALL characters of the tower groups
  G_m = C2 x L_m x Z4 for m <= 3 (level-2 probe: the jet refines
  the readable arithmetic but reads Vfac in {1, 0, -1/7} --
  position-blind at every level), ALL conditional expectations onto
  group subalgebras, the full pinching family, and Stinespring-side
  compressions of the deployed flag dilation -- plus all register
  and factor dressings of the earlier probes.  Every one of these
  reads either (a) position-blind carrier modes, or (b) the factor
  compression that the corner identity freezes to the deployed
  spline reads; identity and new placement information are mutually
  exclusive CELL BY CELL, and direct sums cannot join them because
  the non-pinned components are exactly the non-positive ones.  An
  identification carrier must therefore change the INPUT, not the
  compression: a position-dependent carrier map n -> sigma(x_n)
  (outside the licensed tower datum), a non-group-algebra register,
  or the pair-correlation substance itself.  The wall stays EXACTLY
  PRIME.FLOOR.PAIRCORR.01; stop-list entry candidate
  PRIME.CORNER.EXPECTATION.01 (exploration-typed, no ledger writes).
  NO RH claim.""" % (len(subs), total_comps))
    elif carriers:
        print("""
  THE FINDING (report prominently): %s carries identity AND
  visibility AND placement in one reading -- the first compression
  structure to escape the rank-1 dichotomy; freeze it as a contract.
  """ % ", ".join(carriers))
    n_pass = sum(1 for _n, ok in CHECKS if ok)
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed%s"
          % (time.time() - T0, len(CHECKS), len(FAILS),
             ("  " + ",".join(FAILS)) if FAILS else ""))
    _VERDICTS["a"] = verdict
    return 0 if (n_pass == len(CHECKS) and controls_ok) else 1


# =============== PART B -- position_carrier_probe.py (frozen probe, verbatim)

FROZEN_SPEC_b = """\
PRIME.CARRIER.POSITION.01 spec v1 (2026-08-07, frozen before run).
Variants: A address-routed (R_3 tower address addr(n) = the 3-digit
(1+i)-adic code of n; beta = Hamming(addr(n), addr(round(exp u)))/3;
sigma_A = (1-beta) sigma + beta tau_C2 sigma); B1 mu4-graded
symmetrized (bin = floor(u/(alpha/8)) mod 4; (tau^{+bin} +
tau^{-bin})/2); B2 C2-graded (flip = bin mod 2); C V-amplitude
graded (s = cos(pi u / 2 alpha), p_v = (1 + s eps(v)/4)/Z on H*,
eps = (-1)^popcount, mass-normalized).  Gates: (a) state = symmetric
probability (weights >= 0, mass 1, inversion symmetry; exact
Fractions for A/B1/B2, 1e-12 for C) + spectrum ward (all 128
Fourier values real, |chat| <= 1) on representatives; (b) identity
at truth: corner defect <= 1e-9 scale, weight-generic, WITH the
per-variant derivation (A inherits by degeneration -- dict-equal at
truth; B1/C GL1-invisible by the mass read; B2 typed defect
2|q_j| on odd-bin events, formula matched to 1e-9 scale); (c)
placement: |delta_t - delta_s| > 1e-9 AND |delta_t - delta_e| >
1e-9 (mass list fixed, positions moved; scramble seed 1, Epstein
comb).  FOURTH MEASUREMENT: the self-consistency null = Epstein
masses AT their own log positions; separation = |delta_truth| <=
1e-9 AND |delta_null| > 1e-9.  VERDICT RULE: CARRIES needs (a) AND
(b) AND (c) AND separation; else the failure map is typed
(TRADEOFF) or PARTIAL.  Extremal-pinning ward: chat_GL1 in [-1, 1]
for every variant x configuration; identity <=> chat_GL1 == -1 <=>
C2 mass locked at a = 1.  Controls: GL1 anchor exact (union
events); tau_X 3 windows (frozen refs, 1e-6 rel); A == deployed at
truth exactly.  KAPPA = 1/4.  NO RH claim; writes nothing.
"""

def build_ring(m):
    size = 1 << m

    def enc(a, b):
        code = 0
        for j in range(m):
            d = (a + b) & 1
            if d:
                code |= 1 << j
                a -= 1
            a, b = (a + b) // 2, (b - a) // 2
        return code

    return dict(m=m, size=size, enc=enc)

def sum2sq_ints(count):
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
            return vals[:count]

def carrier_deployed(n, th, Hs):
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

def c2_shift(c):
    return {((a + 1) % 2, v, m): w for (a, v, m), w in c.items()}

def mu4_rot_sym(c, b):
    out = {}
    for (a, v, m), w in c.items():
        for mm in ((m + b) % 4, (m - b) % 4):
            k = (a, v, mm)
            out[k] = out.get(k, Fr(0)) + w / 2
    return out

def gl1_read(c):
    """chat at GL1 = -mass(a=1) + mass(a=0)."""
    r = Fr(0) if isinstance(next(iter(c.values())), Fr) else 0.0
    for (a, _v, _m), w in c.items():
        r += (w if a == 0 else -w)
    return r

def char_read(c, chi):
    re = 0.0
    im = 0.0
    for g, w in c.items():
        cr, ci = chival(chi, g)
        re += float(w) * cr
        im += float(w) * ci
    return re, im

def unit_rows_b(rr, positions):
    out = np.zeros((len(positions), 2 * rr["h"]))
    for j, u in enumerate(positions):
        out[j] = core.atom_lags_at(rr["alpha"], rr["M"], [float(u)],
                                   [2.0])[0]
    return out

def reads_pair_b(rr, rows):
    t1, t2 = rr["t1"], rr["t2"]
    ka = rows.shape[0]
    q3 = np.zeros((ka, 3))
    for j in range(ka):
        R = core.odd_toeplitz(rows[j], rr["M"])
        q3[j, 0] = t1 @ (R @ t1)
        q3[j, 1] = t2 @ (R @ t2)
        q3[j, 2] = t1 @ (R @ t2)
        del R
    c_ar = np.asarray(core.arch_lags(rr["M"], rr["D"]), float)
    T = core.odd_toeplitz(c_ar, rr["M"])
    tB = (float(t1 @ (T @ t1)), float(t2 @ (T @ t2)),
          float(t1 @ (T @ t2)))
    del T
    return q3, tB

def part_b():
    section("PRIME.CARRIER.POSITION.01 -- the position-dependent "
            "carrier map (EXPLORATION ONLY)")
    sha = hashlib.sha256(FROZEN_SPEC_b.encode("utf-8")).hexdigest()
    print("    FROZEN_SPEC_b SHA-256 = %s" % sha)
    print("    verdict rule frozen: CARRIES needs state + identity + "
          "placement AND the self-consistency-null separation.  "
          "NO RH claim.")

    print("\nS0 -- firewall")
    bad = ast_firewall()
    check("S0.1 AST firewall: no zeta-zero / prime-table symbol",
          not bad, "found %s" % bad if bad else "clean")

    # ------------------------------------------------------------ frame
    section("S1 -- packet layer, frame, windows, deployed regressions")
    th = theta_layer()
    check("S1.1 [EXACT] packet layer: glue identity + f8 + heads to "
          "n <= %d" % N_TH, th["ok"])
    _Om, _yc, Hstar = label_frame()
    Hs = sorted(label_int(v) for v in Hstar)
    wins = deployed_windows()
    nv_union = sorted({int(round(math.exp(float(u))))
                       for _kz, rr in wins for u in rr["uu"]})
    off = []
    for n in nv_union:
        c = carrier_deployed(n, th, Hs)
        if gl1_read(c) != Fr(-1):
            off.append(n)
    CONTROL["GL1"] = not off
    check("S1.2 [EXACT -- CONTROL] the GL1 anchor: the deployed "
          "carrier reads chat = -1 for ALL %d union events "
          "(Fractions; position-blind by construction: it consumes "
          "only n)" % len(nv_union), not off)

    ok_id = True
    for kz, rr in wins:
        nv = np.rint(np.exp(rr["uu"])).astype(np.int64)
        q3w, tBw = reads_pair_b(rr, unit_rows_b(rr, np.asarray(rr["uu"],
                                                           float)))
        tau_X = float(np.linalg.eigvalsh(rr["Ah"])[0])
        tau0 = float(np.linalg.eigvalsh(
            blk2(tBw, -np.ones(len(nv)), rr["lam"], q3w))[0])
        scale = max(1.0, abs(tBw[0]), abs(tBw[1]))
        ok_id &= (abs(tau0 - tau_X) / scale <= BAR_ID_REL
                  and abs(tau_X - REG_REFS[kz]) / REG_REFS[kz]
                  <= REG_BAR)
    CONTROL["REDUCTION"] = ok_id
    check("S1.3 [CONTROL] the corner reduction reproduces tau_X on "
          "all %d windows (frozen refs matched)" % N_WIN, ok_id)

    kz0, rr0 = wins[0]
    alpha0 = float(rr0["alpha"])
    lam0 = rr0["lam"]
    nv0 = np.rint(np.exp(rr0["uu"])).astype(np.int64)
    ka0 = len(nv0)
    uu_t = np.asarray(rr0["uu"], float)
    uu_s = np.asarray(core.build_window(kz0, scramble_seed=SCR_SEED)
                      ["uu"], float)
    ne = sum2sq_ints(ka0)
    uu_e = np.log(np.array(ne, dtype=float))
    Xn0, B0 = rr0["Xn"], rr0["B"]
    q3 = {}
    tB = {}
    for p, uu in (("t", uu_t), ("s", uu_s), ("e", uu_e)):
        q3[p], tB[p] = reads_pair_b(rr0, unit_rows_b(rr0, uu))
    scale0 = max(float(np.max(np.abs(B0))), float(np.max(np.abs(Xn0))),
                 float(np.max(np.abs(q3["t"]))), 1.0)
    bar_coef = BAR_COEF_REL * scale0
    cm1 = -np.ones(ka0)
    tau0_pi = {p: float(np.linalg.eigvalsh(
        blk2(tB[p], cm1, lam0, q3[p]))[0]) for p in ("t", "s", "e")}
    print("    primary window kz=%d: ka=%d; position sets: true / "
          "scramble(seed %d) / Epstein (mass list FIXED at the "
          "deployed nv); the null comb: Epstein masses n=%d..%d at "
          "their OWN log positions (self-consistent)"
          % (kz0, ka0, SCR_SEED, ne[0], ne[-1]))

    # ------------------------------------------- construction space
    section("S2 -- the construction space (frozen designs)")
    R3 = build_ring(3)
    addr3 = {}

    def addr(n):
        if n not in addr3:
            addr3[n] = R3["enc"](int(n), 0)
        return addr3[n]

    per = all(addr(n) == addr(n + 4) for n in range(1, 40))
    check("S2.1 [EXACT] the tower address: addr(n) = the (1+i)-adic "
          "3-digit code of n in R_3 = Z[i]/(1+i)^3; on rational "
          "integers the address has period 4 ((1+i)^3 | k <=> 4 | k) "
          "-- the routing reads the level-3 tower residue of the "
          "position's claimed integer", per)
    print("    A : sigma_A = (1-beta) sigma + beta tau_C2 sigma, "
          "beta = dH(addr(n), addr(round(e^u)))/3")
    print("    B1: sigma_B1 = (tau_mu4^+bin + tau_mu4^-bin) sigma/2, "
          "bin = floor(u/(alpha/8)) mod 4")
    print("    B2: sigma_B2 = tau_C2^(bin mod 2) sigma")
    print("    C : p_v -> (1 + kappa s eps(v))/Z on H*, s = "
          "cos(pi u/2 alpha), eps = (-1)^popcount, kappa = %.2f"
          % KAPPA)

    def beta_of(n, u):
        nt = int(round(math.exp(float(u))))
        return Fr(bin(addr(int(n)) ^ addr(nt)).count("1"), 3)

    def bin_of(u):
        return int(math.floor(float(u) / (alpha0 / 8.0))) % 4

    def s_of(u):
        return math.cos(math.pi * float(u) / (2.0 * alpha0))

    def build_variant(name, n, u):
        c0 = carrier_deployed(int(n), th, Hs)
        if name == "A":
            b = beta_of(n, u)
            if b == 0:
                return dict(c0)
            cs = c2_shift(c0)
            out = {}
            for g, w in c0.items():
                out[g] = out.get(g, Fr(0)) + (1 - b) * w
            for g, w in cs.items():
                out[g] = out.get(g, Fr(0)) + b * w
            return out
        if name == "B1":
            return mu4_rot_sym(c0, bin_of(u))
        if name == "B2":
            return c2_shift(c0) if bin_of(u) % 2 else dict(c0)
        # C: V-amplitude graded (float weights)
        if classify(int(n), th["spf"]) != "ro":
            return {g: float(w) for g, w in c0.items()}
        s = s_of(u)
        wts = {v: 1.0 + KAPPA * s
               * (1.0 if bin(v).count("1") % 2 == 0 else -1.0)
               for v in Hs}
        Z = sum(wts.values())
        out = {}
        for (a, v, m), w in c0.items():
            out[(a, v, m)] = float(w) * 7.0 * wts[v] / Z
        return out

    VARIANTS = ("A", "B1", "B2", "C")

    # ------------------------------------------------- gate (a): state
    section("S3 -- gate (a): the state ward (the danger zone)")
    ok_state = {v: True for v in VARIANTS}
    ok_extrem = True
    configs = [("t", nv0, uu_t), ("s", nv0, uu_s), ("e", nv0, uu_e),
               ("null", np.array(ne), uu_e)]
    cvec = {}
    for name in VARIANTS:
        for pi, masses, uus in configs:
            cv = np.zeros(ka0)
            for j in range(ka0):
                c = build_variant(name, masses[j], uus[j])
                exact = isinstance(next(iter(c.values())), Fr)
                wmin = min(c.values())
                mass = sum(c.values())
                sym = all(c.get((a, v, (-m) % 4)) == w
                          if exact else
                          abs(c.get((a, v, (-m) % 4), 0.0) - w)
                          <= BAR_EXACT
                          for (a, v, m), w in c.items())
                if exact:
                    ok_state[name] &= (wmin >= 0 and mass == 1 and sym)
                else:
                    ok_state[name] &= (float(wmin) >= -BAR_EXACT
                                       and abs(float(mass) - 1.0)
                                       <= BAR_EXACT and sym)
                r = float(gl1_read(c))
                ok_extrem &= -1.0 - BAR_EXACT <= r <= 1.0 + BAR_EXACT
                cv[j] = r
            cvec[(name, pi)] = cv
    check("S3.1 ALL variants pass the state ward on ALL 4 "
          "configurations x %d events: weights >= 0, total mass = 1, "
          "inversion-symmetric (exact Fractions for A/B1/B2, 1e-12 "
          "for C) -- position-dependent ROUTING and NORMALIZED "
          "grading keep the packet a genuine positive state; the "
          "danger zone opens only for signed/unnormalized designs "
          "(excluded by the frozen rules)"
          % ka0, all(ok_state.values()),
          str({k: bool(v) for k, v in ok_state.items()}))
    # spectrum ward on representatives (scrambled ro event)
    j_ro = next(j for j in range(ka0)
                if classify(int(nv0[j]), th["spf"]) == "ro")
    ok_spec = True
    for name in VARIANTS:
        c = build_variant(name, nv0[j_ro], uu_s[j_ro])
        mx = 0.0
        mi = 0.0
        for eps in range(2):
            for w in range(16):
                for jj in range(4):
                    re, im = char_read(c, (eps, w, jj))
                    mx = max(mx, abs(re))
                    mi = max(mi, abs(im))
        ok_spec &= mx <= 1.0 + BAR_EXACT and mi <= BAR_EXACT
    check("S3.2 spectrum ward (representative ro event, scrambled "
          "position): all 128 Fourier values REAL (self-adjoint) "
          "with |chat| <= 1 (contraction) for every variant -- the "
          "state structure survives the position dependence "
          "(as deployed: contraction, NOT operator-PSD; chat_GL1 = "
          "-1 is an eigenvalue)", ok_spec)

    # -------------------------------------------- gate (b): identity
    section("S4 -- gate (b): the identity at the true configuration "
            "(with the derivations)")
    # A degenerates to deployed at truth (dict equality, exact)
    ok_deg = True
    for j in range(ka0):
        cA = build_variant("A", nv0[j], uu_t[j])
        c0 = carrier_deployed(int(nv0[j]), th, Hs)
        ok_deg &= cA == c0
    CONTROL["DEGEN"] = ok_deg
    check("S4.1 [EXACT -- THE DERIVATION FOR A] at the true "
          "configuration beta_j = 0 for every event, and sigma_A == "
          "the deployed carrier WEIGHT FOR WEIGHT (dict equality): "
          "the certified corner identity is INHERITED verbatim, not "
          "re-proved -- the position dependence lives entirely in "
          "the consistency defect beta, which vanishes at truth",
          ok_deg)
    devs = {}
    for name in VARIANTS:
        devs[name] = id_dev(tB["t"], cvec[(name, "t")], q3["t"],
                            B0, Xn0)
    check("S4.2 [DERIVED + MEASURED] identity at truth: A defect = "
          "%.1e (inherited); B1 defect = %.1e (the mu4 rotation is "
          "GL1-INVISIBLE: the GL1 corner reads only the C2 mass); "
          "C defect = %.1e (the normalized V grading is GL1-"
          "INVISIBLE: the GL1 corner reads only the V mass, "
          "normalized to 1) -- all three <= bar %.1e"
          % (devs["A"], devs["B1"], devs["C"], bar_coef),
          max(devs["A"], devs["B1"], devs["C"]) <= bar_coef)
    odd = np.array([bin_of(u) % 2 == 1 for u in uu_t])
    pred_dev = 2.0 * float(np.max(np.abs(q3["t"][odd]))) \
        if np.any(odd) else 0.0
    check("S4.3 [THE TYPED DEFECT FOR B2] the absolute C2 grading "
          "flips chat to +1 on the %d odd-bin events AT THE TRUE "
          "positions: defect %.6e == the derived formula "
          "2 max|q_j| = %.6e (matched to 1e-9 scale) -- an absolute "
          "position grading in the identity-carrying slot breaks "
          "the identity at truth by construction"
          % (int(odd.sum()), devs["B2"], pred_dev),
          abs(devs["B2"] - pred_dev) <= bar_coef and devs["B2"]
          > bar_coef)

    # ------------------------------------------- gate (c): placement
    section("S5 -- gate (c): placement (scramble / Epstein, mass "
            "list fixed) + the null comb")
    delta = {}
    for name in VARIANTS:
        delta[name] = {}
        for pi in ("t", "s", "e"):
            b = blk2(tB[pi], cvec[(name, pi)], lam0, q3[pi])
            delta[name][pi] = float(np.linalg.eigvalsh(b)[0]) \
                - tau0_pi[pi]
        bnull = blk2(tB["e"], cvec[(name, "null")], lam0, q3["e"])
        delta[name]["null"] = float(np.linalg.eigvalsh(bnull)[0]) \
            - tau0_pi["e"]
    nflag_s = int(np.sum(np.abs(cvec[("A", "s")] + 1.0) > 1e-12))
    nflag_e = int(np.sum(np.abs(cvec[("A", "e")] + 1.0) > 1e-12))
    print("    variant A consistency flags: scramble %d/%d events, "
          "Epstein(mass-fixed) %d/%d events, truth 0, null comb %d"
          % (nflag_s, ka0, nflag_e, ka0,
             int(np.sum(np.abs(cvec[("A", "null")] + 1.0) > 1e-12))))
    for name in VARIANTS:
        d = delta[name]
        print("    %-3s delta: true=%+.3e  scr=%+.3e  eps=%+.3e  "
              "NULL(self-consistent)=%+.3e"
              % (name, d["t"], d["s"], d["e"], d["null"]))
    P = {name: (abs(delta[name]["t"] - delta[name]["s"]) > BAR_MOVE
                and abs(delta[name]["t"] - delta[name]["e"])
                > BAR_MOVE) for name in VARIANTS}
    check("S5.1 placement: A moves under scramble AND Epstein "
          "(P=%s) -- the consistency router IS position-sensitive "
          "under the mass-fixed convention; B2 moves (P=%s, but its "
          "identity is already broken at truth); B1 and C are "
          "GL1-blind (P=%s/%s: the graded slots are exactly the "
          "ones the GL1 corner cannot see)"
          % (P["A"], P["B2"], P["B1"], P["C"]),
          P["A"] and P["B2"] and not P["B1"] and not P["C"])
    sep = {name: (abs(delta[name]["t"]) <= BAR_MOVE
                  and abs(delta[name]["null"]) > BAR_MOVE)
           for name in VARIANTS}
    check("S5.2 [THE DECISIVE NULL] the self-consistency null: on "
          "the self-consistent Epstein comb (masses = sums of two "
          "squares AT their own log positions) variant A reads "
          "beta == 0 EVERYWHERE -- the corner excess is %.1e, "
          "IDENTICAL to the truth (0): NO variant separates the "
          "true comb from the self-consistent fake (separation "
          "map %s) -- the placement sensitivity of A is "
          "CONSISTENCY sensitivity, not prime-placement "
          "sensitivity; the deployed-form floor transports to the "
          "fake comb equally"
          % (abs(delta["A"]["null"]),
             {k: bool(v) for k, v in sep.items()}),
          not any(sep.values()))
    check("S5.3 [THE EXTREMAL-PINNING WARD] chat_GL1 in [-1, 1] for "
          "EVERY variant x configuration x event (state ==> the GL1 "
          "read is a mass difference), and the identity pins it to "
          "the EXTREME point -1 (the entire C2 mass locked at "
          "a = 1): a state-preserving, identity-true carrier has NO "
          "first-order position freedom at any configuration where "
          "the identity is required -- what remains is the "
          "nonnegative consistency defect (1 + chat)/2, which "
          "vanishes identically on self-consistent combs",
          ok_extrem)

    # --------------------------------------------------------- verdict
    section("V -- FROZEN VERDICT + the honest consequence")
    gates = {}
    for name in VARIANTS:
        gates[name] = (ok_state[name],
                       devs[name] <= bar_coef,
                       P[name],
                       sep[name])
    print("    THE FAILURE MAP (state, identity@truth, placement, "
          "null-separation):")
    legs = {"A": "consistency channel only (null-blind)",
            "B1": "GL1-blind (graded slot invisible to the corner)",
            "B2": "identity broken at truth (absolute grading)",
            "C": "GL1-blind (normalized grading invisible)"}
    for name in VARIANTS:
        g = gates[name]
        print("      %-3s S=%d I=%d P=%d SEP=%d   <- %s"
              % (name, g[0], g[1], g[2], g[3], legs[name]))
    carriers = [n for n, g in gates.items() if all(g)]
    controls_ok = all(CONTROL.values())
    map_ok = (gates["A"] == (True, True, True, False)
              and gates["B1"][1] and not gates["B1"][2]
              and not gates["B2"][1] and gates["B2"][2]
              and gates["C"][1] and not gates["C"][2]
              and ok_extrem and ok_spec)
    if carriers:
        verdict = "POSITION-CARRIER-CARRIES (%s)" % ", ".join(carriers)
    elif map_ok and controls_ok:
        verdict = "POSITION-CARRIER-TRADEOFF"
    else:
        verdict = "POSITION-CARRIER-PARTIAL"
    print("\n  VERDICT: %s" % verdict)
    if verdict == "POSITION-CARRIER-TRADEOFF":
        print("""
  THE FAILURE PATTERN IS STRUCTURAL (the fourth wall coordinate,
  named: EXTREMAL PINNING).  A position-dependent carrier map can
  keep the packet state (probability + symmetry + contraction:
  measured for all four designs) -- positivity is NOT the obstacle.
  The obstacle is the conjunction: STATE + IDENTITY = EXTREMALITY.
  For any state carrier the GL1 read is a mass difference in
  [-1, 1]; the deployed-form identity demands the extreme value -1,
  i.e. the entire C2 mass locked, at EVERY true configuration.  So
  the only position dependence compatible with both is a NONNEGATIVE
  consistency defect (1 + chat)/2 that vanishes wherever the
  identity is required -- and therefore vanishes on EVERY self-
  consistent comb, true or fake (measured: variant A flags every
  mass-fixed scramble yet reads exactly zero on the self-consistent
  Epstein comb).  Grading position into other slots fails on the
  other side: mu4 rotations and normalized V tilts are invisible to
  the GL1 corner (which reads only the locked masses), and absolute
  grading in the C2 slot breaks the identity at truth by the typed
  defect 2|q_j|.  The three legs -- still-blind (B1, C), identity-
  broken (B2), consistency-only (A) -- exhaust the frozen design
  space: position-dependence in the carrier is incompatible with
  (state AND identity AND separation of self-consistent combs).

  THE HONEST CONSEQUENCE (one paragraph): candidate 1 does not
  reopen the corner route -- it sharpens WHY it is closed.  The
  compression closures said: no reading of a position-blind carrier
  identifies.  This probe says: making the carrier position-
  dependent does not help, because the identity is an EXTREMAL
  state condition -- any carrier that satisfies it at the true comb
  satisfies it verbatim at every self-consistent comb, so the
  corner's zero-excess certificate can never distinguish the primes
  from an Epstein (or any other self-consistent) configuration.
  The identification datum at the wall is about WHICH self-
  consistent comb is real -- information that no state-preserving,
  identity-true carrier map F(n, u) can encode, since it only ever
  sees the pair (n, u) whose consistency is comb-universal.  What
  would escape: giving up manifest state positivity (then the
  packet is no longer the positive object the route needs), or an
  input that distinguishes self-consistent combs by SUBSTANCE
  rather than by consistency -- i.e. the pair-correlation datum
  itself.  The wall stays EXACTLY PRIME.FLOOR.PAIRCORR.01, with the
  fourth coordinate typed: register closed, factor pinned, tower
  level-exact, and now carrier-side position-dependence extremally
  pinned.  Stop-list entry candidate PRIME.CARRIER.POSITION.01
  (exploration-typed; no ledger writes).  NO RH claim.""")
    elif carriers:
        print("""
  THE FINDING (report prominently): variant %s passes state +
  identity + placement AND separates the self-consistent null --
  an identification carrier exists; next stage: the positivity of
  the identified corner along the ladder.""" % ", ".join(carriers))
    n_pass = sum(1 for _n, ok in CHECKS if ok)
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed%s"
          % (time.time() - T0, len(CHECKS), len(FAILS),
             ("  " + ",".join(FAILS)) if FAILS else ""))
    _VERDICTS["b"] = verdict
    return 0 if (n_pass == len(CHECKS) and controls_ok) else 1


EXPECT = {"a": (13, "EXPECTATION-CLOSED"),
          "b": (13, "POSITION-CARRIER-TRADEOFF")}


def run():
    t_all = time.time()
    rc = 0
    counts = {}
    for tag, part in (("a", part_a), ("b", part_b)):
        CHECKS.clear()
        FAILS.clear()
        CONTROL.clear()
        if "_LCG" in globals():
            _LCG[0] = 20260807
        globals()["T0"] = time.time()
        r = part()
        rc += int(r or 0)
        counts[tag] = (len(CHECKS), len(FAILS))
    pattern_ok = all(
        counts[t][0] == EXPECT[t][0] and counts[t][1] == 0
        and _VERDICTS.get(t) == EXPECT[t][1] for t in EXPECT)
    n_run = sum(c[0] for c in counts.values())
    n_fail = sum(c[1] for c in counts.values())
    print("\n" + "=" * 74)
    print("v838: %d/%d checks passed, %d failed | runtime %.1f s"
          % (n_run - n_fail, n_run, n_fail, time.time() - t_all))
    print("NO RH claim; the wall stays PRIME.FLOOR.PAIRCORR.01 -- all "
          "four corner-route coordinates typed.")
    print("[%s] PATTERN GATE: expected 13 + 13 checks, 0 failed, "
          "verdicts EXPECTATION-CLOSED + POSITION-CARRIER-TRADEOFF "
          "(got %s + %s)"
          % ("PASS" if pattern_ok else "FAIL",
             _VERDICTS.get("a"), _VERDICTS.get("b")))
    return rc + (0 if pattern_ok else 1)


if __name__ == "__main__":
    raise SystemExit(run())
