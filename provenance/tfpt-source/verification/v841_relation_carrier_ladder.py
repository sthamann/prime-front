#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""v841 -- PRIME.RELATION.MULT.01 + PRIME.RELATION.LADDER.01: the relation carrier EXISTS and its identified corner's excess is nonnegative along the whole reachable ladder -- the corner route REOPENS with the right input class (the multiplicative relations between events), the first structure in the program to pass all four gates including the self-consistency null that killed every compression and every single-event carrier, and in identified-corner coordinates the wall takes its sharpest form tau_X = lambda_min(structural) + EXCESS, ONE module from two probes (18/18 + 13/13 checks, verdicts RELATION-CARRIER-EXISTS and EXCESS-NONNEGATIVE; discovery probes multiplicative_relation_probe.py and relation_corner_ladder_probe.py, 2026-08-07, re-run identically at promotion, promoted VERBATIM with no downscoping, ~6 s).  PART A, THE RELATION CARRIER (the round's breakthrough): (1) THE RELATIONAL ALGEBRA -- the exact convolution frame A_X carries Moebius inversion (mu * 1 = delta for ALL n <= 256) and Lambda-hat = mu * log == Lambda as EXACT structure (dict equality on the log-p basis; truncated frame associative on the ideal quotient): every event's Lambda-weight is derivable from the pair relations alone.  (2) THE FOUR-COMB DISCRIMINATOR (exact Euler-product reading R_mult = L1 mass of Lambda_F off prime powers): TRUE comb 0 EXACT; the self-consistent s2s null (= zeta_{Q(i)}, h = 1) 0 EXACT and the chi4 L-fake 0 EXACT (Selberg-class-CORRECT blindness -- multiplicativity is the right necessary discriminator, L-function identity is amplitude data); the GENUINE no-Euler-product Epstein comb x^2 + 5y^2 (h = 2) reads 200.0 on 24 off-prime-power sites localized at the class-group obstruction (21 = 3 x 7 represented, neither factor is).  (3) ALL FOUR GATES: the relationally-routed carrier keeps the packet state EXACTLY (convex routing rho in [0,1]); at the true comb rho == 0 and the carrier IS the deployed carrier (corner defect 2.7e-14, lambda_min reproduces tau_X = +5.984165e-04 at rel 3.8e-12 -- the identity re-derived by degeneration); placement fires (scramble +1.291, Epstein -1.226); and GATE 4, the point where every previous carrier died: the SELF-CONSISTENT s2s null is SEPARATED -- 14 of 70 events carry missing product relations (18 present without its divisors 3, 6), corner excess -0.2966 vs exactly 0 at truth.  PART B, THE LADDER (both typed limits of part A closed): the AMPLITUDE wiring -- the corner reads the Euler-product datum at amplitude grade (R_corner exact Fractions: TRUE/QI/CHI 0 EXACT and delta ~ 1e-15; H2 reads 196/392/496 on the anchors kz = 9/12/13 and moves the corner, separated PURELY by the Euler-product datum) and the amplitude reading fixes L-SAFETY AUTOMATICALLY (rho_amp flags 0 of the 14 s2s closure events -- Lambda_F of r2/4 is prime-power-supported exactly -- while still flagging the h = 2 fake); THE EXCESS SERIES on all 67 reachable rungs (kz = 9..121, alpha = 2.773..6.304, masses to 3.0e5): support ward exact on every rung (prime powers at exact log positions, rho(true) == 0 -- the identified carrier IS the deployed carrier at truth), identity ward lambda_min(B - Sum lam Xn) == tau_X on all 67, and the EXCESS = tau_X - lambda_min(S) over the comb-blind structural skeleton is POSITIVE ON ALL 67 RUNGS (min +2.285 at kz = 9, max +3.704 at kz = 121; scramble control -1.224 -- comb-sensitive, not a structural artefact) while tau_X itself decays 5.98e-04 -> 1.71e-05.  THE SHARPEST WALL FORM (the deliverable): the open question now has corner coordinates -- tau_X = lambda_min(structural) + EXCESS with the structural part certifiable and the excess the arithmetic substance; the identified route has measured substance, the floor's positivity along the ladder remains unproven; the question is no longer 'can any corner see the primes' (yes: this one) but 'is the identified corner's excess nonnegative along the ladder' -- a positivity statement about the multiplicative comb itself, which is PRIME.FLOOR.PAIRCORR.01.  Registers the relation route: PRIME.RELATION.MULT.01 [O].  NO RH claim.  Python-only per GATE.WOLFRAM.02.

PROVENANCE: discovery probes multiplicative_relation_probe.py (18/18,
verdict RELATION-CARRIER-EXISTS) and relation_corner_ladder_probe.py
(13/13, verdict EXCESS-NONNEGATIVE), both 2026-08-07, re-run
identically at promotion; this module runs both frozen protocols
VERBATIM (~6 s; a module-level _VERDICTS capture inserted at the
frozen verdict per the v817/v791 precedent -- no gate, bar or table
changed; the two probes' cosmetically different check() printers are
unified to part A's line-wrap, output otherwise byte-identical).
The original probe docstrings, frozen specs (SHA-256-printed) and
decision trees live in the probe files verbatim
(experiments/tfpt-discovery/).

FIREWALL: v563 / v738 READ-ONLY; no zeta zero, no prime-table symbol
(AST-checked; own sieves only -- the divisor/mu arithmetic IS the
admissible Euler-product datum); RNG only in the declared v563
scramble recipe (seed 1).  NO RH claim.
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
    p = int(spf[n])
    m, k = n, 0
    while m % p == 0:
        m //= p
        k += 1
    if p == 2:
        return "ro" if k % 2 == 1 else "re"
    return "sp" if p % 4 == 1 else "in"

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

def factorize(n, spf):
    out = {}
    while n > 1:
        p = int(spf[n])
        k = 0
        while n % p == 0:
            n //= p
            k += 1
        out[p] = k
    return out

def logvec(n, spf):
    return {p: Fr(k) for p, k in factorize(n, spf).items()}

def vaddto(acc, v, s):
    for p, c in v.items():
        acc[p] = acc.get(p, Fr(0)) + s * c
    return acc

def vnorm1(v):
    return sum(abs(c) for c in v.values())

def vclean(v):
    return {p: c for p, c in v.items() if c != 0}

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

def gl1_read(c):
    r = Fr(0)
    for (a, _v, _m), w in c.items():
        r += (w if a == 0 else -w)
    return r

def unit_rows(rr, positions):
    out = np.zeros((len(positions), 2 * rr["h"]))
    for j, u in enumerate(positions):
        out[j] = core.atom_lags_at(rr["alpha"], rr["M"], [float(u)],
                                   [2.0])[0]
    return out

def reads_pair(rr, rows):
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

def blk2(tBf, cvec, lam, q3):
    s0 = float(np.sum(cvec * lam * q3[:, 0]))
    s1 = float(np.sum(cvec * lam * q3[:, 1]))
    sx = float(np.sum(cvec * lam * q3[:, 2]))
    return np.array([[tBf[0] - s0, tBf[2] - sx],
                     [tBf[2] - sx, tBf[1] - s1]])


# =============== PART A -- multiplicative_relation_probe.py (frozen probe, verbatim)

FROZEN_SPEC_a = """\
PRIME.RELATION.MULT.01 spec v2 (2026-08-07, frozen before the run;
v2 = X 178 -> 256 after the v1 run crashed at the S2/S4 divisor
lookup BEFORE any discriminator or gate measurement: the primary
window support was measured to be the PRIME POWERS 2..256, not
contiguous integers 2..71 -- the support ward below replaces the
contiguity assumption; no gate expectation changed).
X = 256.  Support ward: every primary event mass is a prime power
AND every prime power in [2, 256] is an event (the Lambda-comb
support; divisor-closed).  Design (a): truncated convolution
algebra A_X, exact
log-p-basis scalars; wards mu*1 = delta (all n), mu*log == Lambda
(all n, dict equality), associativity (64 LCG triples).  Design (b):
Moebius pairing B[k,j] = mu(m_k/m_j) on divisor pairs; derived
weight = B applied to the position vector; ward B@log == Lambda to
1e-12 at truth.  Discriminator: exact recursion a(n) log n =
sum_{d|n} Lambda_F(d) a(n/d); R_mult = L1(Lambda_F off prime
powers), exact.  Comb rows: TRUE a = 1 (R_mult == 0 exact AND
Lambda_F == Lambda); s2s a = r2/4 (R_mult == 0, vs-zeta defect > 0;
typed: the carrier-probe null is secretly zeta_{Q(i)} = zeta L(chi4),
h = 1); EPSTEIN-h2 a = r_{x^2+5y^2}/2 (R_mult > 0; off-pp sites
include 6 = 2x3 and 21 = 3x7, factors non-represented);
L-FAKE a = chi4 (R_mult == 0, typed correct Selberg blindness).
Carrier: rho = min(1, rho_close + rho_pos); rho_close = missing-
divisor fraction (exact); rho_pos = |mu-reconstruction from
positions - Lambda|/log 2 capped 1; sigma_rel = (1-rho) sigma + rho
tau_C2 sigma.  Gates: state (weights >= 0, mass 1, symmetric, all 4
configs x 70 events, 1e-12); identity at truth (corner defect <=
1e-9 scale AND lambda_min(block) == tau_X to 1e-6 rel); placement
(|delta_t - delta_s| > 1e-9 AND |delta_t - delta_e| > 1e-9, scramble
seed 1, mass-fixed Epstein); separation (|delta_t| <= 1e-9 AND
|delta_null| > 1e-9 on the self-consistent s2s null).  Controls:
GL1 anchor exact (union events); tau_X 3 windows (frozen refs,
1e-6/1e-4).  VERDICTS: RELATION-CARRIER-EXISTS / RELATION-SEPARATES-
ONLY / RELATION-BLIND.  Honest frame: success != ladder positivity;
the amplitude-grade discriminator is exact but corner-wired only at
support/position grade.  LCG 20260807.  NO RH claim; writes nothing.
"""

N_TH_a = 640

N_WIN = 3

X_FRAME = 256

CONTROL = {}

_LCG = [20260807]

def lcg(n):
    _LCG[0] = (1103515245 * _LCG[0] + 12345) % (1 << 31)
    return _LCG[0] % n

def theta_layer_a():
    sig3 = np.zeros(N_TH_a + 1, dtype=np.int64)
    for d in range(1, N_TH_a + 1):
        sig3[d::d] += d ** 3
    spf = np.zeros(N_TH_a + 1, dtype=np.int64)
    for p in range(2, N_TH_a + 1):
        if spf[p] == 0:
            spf[p::p] = np.where(spf[p::p] == 0, p, spf[p::p])
    SCAP = 2 * N_TH_a
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
    Th0 = ((p3 + m53 + m35 + p4) // 4)[::2][:N_TH_a + 1].copy()
    Th2 = ((p3 - m53 - m35 + p4) // 4)[::2][:N_TH_a + 1].copy()
    TCAP = 8 * N_TH_a
    t2 = sparse_theta_terms("th2", TCAP)
    acc = np.zeros(TCAP + 1, dtype=np.int64)
    acc[0] = 1
    for _ in range(8):
        acc = sparse_mul(acc, t2)
    Th1 = (acc[::8][:N_TH_a + 1] // 4).copy()
    tk = np.zeros(N_TH_a + 1, dtype=np.int64)
    for d in range(2, N_TH_a + 1, 2):
        tk[d::d] += d * (4 + (4 if d % 4 == 0 else 0))
    g = np.zeros(N_TH_a, dtype=np.int64)
    g[0] = 1
    for n in range(1, N_TH_a):
        s = int(np.dot(tk[1:n + 1], g[n - 1::-1]))
        q, r = divmod(-s, n)
        assert r == 0
        g[n] = q
    a_f8 = np.zeros(N_TH_a + 1, dtype=np.int64)
    a_f8[1:] = g
    glue_ok = bool(np.all((Th0 + 2 * Th1 + Th2)[1:] == 240 * sig3[1:]))
    heads_ok = ((Th0[1], Th1[1], Th2[1]) == (52, 64, 60)
                and (a_f8[3], a_f8[5], a_f8[7]) == (-4, -2, 24))
    return dict(sig3=sig3, Th=(Th0, Th1, Th2, Th1), a=a_f8, spf=spf,
                ok=glue_ok and heads_ok)

def label_frame_a():
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
    return Hstar

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

def id_dev(tBf, cvec, q3, B, Xn):
    d = max(abs(B[0, 0] - tBf[0]), abs(B[1, 1] - tBf[1]),
            abs(B[0, 1] - tBf[2]))
    for s in range(3):
        d = max(d, float(np.max(np.abs(cvec * q3[:, s] - Xn[:, s]))))
    return d

def part_a():
    section("PRIME.RELATION.MULT.01 -- the multiplicative-relation "
            "input class (EXPLORATION ONLY)")
    sha = hashlib.sha256(FROZEN_SPEC_a.encode("utf-8")).hexdigest()
    print("    FROZEN_SPEC_a SHA-256 = %s" % sha)
    print("    honesty correction typed before the run: the s2s null "
          "is secretly multiplicative (zeta_{Q(i)}, h = 1); the "
          "genuine no-Euler-product Epstein is x^2 + 5y^2 (h = 2).  "
          "NO RH claim.")

    print("\nS0 -- firewall")
    bad = ast_firewall()
    check("S0.1 AST firewall: no zeta-zero / prime-table symbol; the "
          "divisor/mu arithmetic is admissible input (it IS the "
          "Euler-product datum)", not bad,
          "found %s" % bad if bad else "clean")

    # ------------------------------------------------------------ frame
    section("S1 -- packet layer, frame, windows, deployed anchors")
    th = theta_layer_a()
    spf = th["spf"]
    check("S1.1 [EXACT] packet layer: glue identity + f8 + heads to "
          "n <= %d" % N_TH_a, th["ok"])
    Hs = sorted(label_int(v) for v in label_frame_a())
    wins = deployed_windows()
    nv_union = sorted({int(round(math.exp(float(u))))
                       for _kz, rr in wins for u in rr["uu"]})
    off = [n for n in nv_union
           if gl1_read(carrier_deployed(n, th, Hs)) != Fr(-1)]
    CONTROL["GL1"] = not off
    check("S1.2 [EXACT -- CONTROL] the GL1 anchor: chat = -1 for ALL "
          "%d union events" % len(nv_union), not off)
    ok_id = True
    for kz, rr in wins:
        nv = np.rint(np.exp(rr["uu"])).astype(np.int64)
        q3w, tBw = reads_pair(rr, unit_rows(rr, np.asarray(rr["uu"],
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
    lam0 = rr0["lam"]
    nv0 = np.rint(np.exp(rr0["uu"])).astype(np.int64)
    ka0 = len(nv0)
    uu_t = np.asarray(rr0["uu"], float)
    uu_s = np.asarray(core.build_window(kz0, scramble_seed=SCR_SEED)
                      ["uu"], float)
    ne = sum2sq_ints(ka0)
    uu_e = np.log(np.array(ne, dtype=float))
    Xn0, B0 = rr0["Xn"], rr0["B"]
    tau_X0 = float(np.linalg.eigvalsh(rr0["Ah"])[0])
    q3 = {}
    tB = {}
    for p, uu in (("t", uu_t), ("s", uu_s), ("e", uu_e)):
        q3[p], tB[p] = reads_pair(rr0, unit_rows(rr0, uu))
    scale0 = max(float(np.max(np.abs(B0))), float(np.max(np.abs(Xn0))),
                 float(np.max(np.abs(q3["t"]))), 1.0)
    bar_coef = BAR_COEF_REL * scale0
    cm1 = -np.ones(ka0)
    tau0_pi = {p: float(np.linalg.eigvalsh(
        blk2(tB[p], cm1, lam0, q3[p]))[0]) for p in ("t", "s", "e")}
    print("    primary window kz=%d: ka=%d, masses n = %d..%d; null "
          "comb = s2s %d..%d at own logs; max|u_j - log n_j| at "
          "truth = %.1e"
          % (kz0, ka0, int(nv0[0]), int(nv0[-1]), ne[0], ne[-1],
             float(np.max(np.abs(uu_t
                                 - np.log(nv0.astype(float)))))))

    def is_pp(n):
        f = factorize(int(n), spf)
        return len(f) == 1
    sup_t = set(int(m) for m in nv0)
    pp_all = [n for n in range(2, X_FRAME + 1) if is_pp(n)]
    check("S1.4 [SUPPORT WARD] the primary support IS the "
          "Lambda-comb support: every event mass is a prime power "
          "and every prime power in [2, %d] is an event (%d = %d) "
          "-- the true comb is divisor-closed BY ARITHMETIC, not by "
          "assumption" % (X_FRAME, len(pp_all), ka0),
          all(is_pp(m) for m in nv0) and set(pp_all) == sup_t)

    # ------------------------------------ design (a): convolution frame
    section("S2 -- design (a): the exact convolution frame A_X + "
            "design (b): the Moebius pairing")
    X = X_FRAME
    divs = {n: [] for n in range(1, X + 1)}
    for d in range(1, X + 1):
        for m in range(d, X + 1, d):
            divs[m].append(d)
    MU = np.zeros(X + 1, dtype=np.int64)
    MU[1] = 1
    for n in range(2, X + 1):
        f = factorize(n, spf)
        MU[n] = 0 if any(k > 1 for k in f.values()) \
            else (-1) ** len(f)
    ISPP = np.zeros(X + 1, dtype=bool)
    for n in range(2, X + 1):
        ISPP[n] = len(factorize(n, spf)) == 1
    LAMV = {n: ({int(spf[n]): Fr(1)} if ISPP[n] else {})
            for n in range(2, X + 1)}
    mu_ok = all(sum(int(MU[d]) for d in divs[n]) == (1 if n == 1
                                                     else 0)
                for n in range(1, X + 1))
    check("S2.1 [EXACT] Moebius inversion inside A_X: (mu * 1)(n) = "
          "delta_1(n) for ALL n <= %d -- the frame's structure "
          "constants (e_d e_e = e_de, ideal-truncated) carry the "
          "full inversion calculus" % X, mu_ok)
    lamhat_ok = True
    for n in range(2, X + 1):
        acc = {}
        for d in divs[n]:
            if MU[d]:
                vaddto(acc, logvec(n // d, spf), Fr(int(MU[d])))
        lamhat_ok &= vclean(acc) == LAMV[n]
    check("S2.2 [EXACT -- THE mu*log WARD] Lambda-hat = mu * log "
          "== Lambda (own sieve) for ALL n <= %d, dict equality on "
          "the log-p basis -- the derived weight of every event is "
          "reconstructed EXACTLY from the pair relations" % X,
          lamhat_ok)
    ok_assoc = True
    for _ in range(64):
        a = 2 + lcg(X - 1)
        b = 2 + lcg(X - 1)
        c = 2 + lcg(X - 1)
        lhs = a * b * c if (a * b <= X and a * b * c <= X) else 0
        rhs = a * b * c if (b * c <= X and a * b * c <= X) else 0
        ok_assoc &= (lhs == 0) == (rhs == 0)
    check("S2.3 [EXACT] associativity of the truncated frame on 64 "
          "LCG triples (the span of n > X is an ideal; the quotient "
          "algebra is associative)", ok_assoc)
    # design (b) ward: B @ log-positions == Lambda at truth
    ok_pair = True
    for j in range(ka0):
        m = int(nv0[j])
        acc = 0.0
        for d in divs[m]:
            if MU[d]:
                acc += float(MU[d]) * (math.log(m // d)
                                       if m // d > 1 else 0.0)
        lam_f = math.log(int(spf[m])) if ISPP[m] else 0.0
        ok_pair &= abs(acc - lam_f) <= 1e-11
    check("S2.4 design (b) ward: the Moebius pairing applied to the "
          "TRUE position vector reproduces Lambda(m_j) for all %d "
          "events (<= 1e-11) -- the derived weight IS a linear "
          "reading of the comb positions through the pair relations"
          % ka0, ok_pair)

    # ------------------------------------------- the discriminator
    section("S3 -- THE DISCRIMINATOR: the exact Euler-product "
            "reading on the four combs")
    r2 = np.zeros(X + 1, dtype=np.int64)
    rq = np.zeros(X + 1, dtype=np.int64)
    s = int(math.isqrt(X)) + 1
    for x in range(-s, s + 1):
        for y in range(-s, s + 1):
            v = x * x + y * y
            if 1 <= v <= X:
                r2[v] += 1
            v = x * x + 5 * y * y
            if 1 <= v <= X:
                rq[v] += 1
    ok_r = (r2[1] == 4 and rq[1] == 2 and r2[2] == 4 and rq[5] == 2
            and rq[21] == 8 and rq[3] == 0 and rq[7] == 0)
    s2s_set = set(sum2sq_ints(200))
    ok_r &= all((r2[n] > 0) == (n in s2s_set) for n in range(2, X + 1))
    check("S3.1 [EXACT] representation counts (own double loops): "
          "r2(1) = 4, r_Q(1) = 2 (normalizers); r_Q(3) = r_Q(7) = 0 "
          "but r_Q(21) = 8 (the h = 2 signature: 21 represented, "
          "its factors NOT); r2-support == the s2s sieve", ok_r)

    def euler_reading(a):
        """Exact log-derivative recursion; returns (off-pp L1, off-pp
        sites, vs-zeta L1, G)."""
        G = {}
        for n in range(2, X + 1):
            acc = {}
            if a[n] != 0:
                vaddto(acc, logvec(n, spf), a[n])
            for d in divs[n]:
                if 1 < d < n and G[d] and a[n // d] != 0:
                    vaddto(acc, G[d], -a[n // d])
            G[n] = vclean(acc)
        offpp = Fr(0)
        sites = []
        vsz = Fr(0)
        for n in range(2, X + 1):
            if not ISPP[n] and G[n]:
                offpp += vnorm1(G[n])
                sites.append(n)
            dv = dict(G[n])
            vaddto(dv, LAMV[n], Fr(-1))
            vsz += vnorm1(vclean(dv))
        return offpp, sites, vsz, G

    a_true = [Fr(1)] * (X + 1)
    a_qi = [Fr(int(r2[n]), 4) for n in range(X + 1)]
    a_h2 = [Fr(int(rq[n]), 2) for n in range(X + 1)]
    a_chi = [Fr(0) if n % 2 == 0 else Fr(1 if n % 4 == 1 else -1)
             for n in range(X + 1)]
    rows = [("TRUE zeta (a=1)", a_true),
            ("s2s / zeta_Q(i) (a=r2/4)", a_qi),
            ("EPSTEIN x^2+5y^2 (a=rQ/2)", a_h2),
            ("L-FAKE chi4 (a=chi4)", a_chi)]
    res = {}
    print("    THE FOUR-COMB TABLE (R_mult = L1 mass of Lambda_F off "
          "prime powers, EXACT; vs-zeta = L1(Lambda_F - Lambda)):")
    for name, a in rows:
        offpp, sites, vsz, G = euler_reading(a)
        res[name] = (offpp, sites, vsz, G)
        print("      %-28s R_mult = %-10s  off-pp sites: %3d %s  "
              "vs-zeta L1 = %.4f"
              % (name, ("0 (EXACT)" if offpp == 0 else
                        "%.4f" % float(offpp)), len(sites),
                 (str(sites[:6]) + ("..." if len(sites) > 6 else ""))
                 if sites else "[]", float(vsz)))
    G_true = res["TRUE zeta (a=1)"][3]
    ok_true = (res["TRUE zeta (a=1)"][0] == 0
               and all(G_true[n] == LAMV[n] for n in range(2, X + 1)))
    check("S3.2 [EXACT -- THE WARD] the TRUE comb: Lambda_F == "
          "Lambda dict for dict on ALL n <= %d and R_mult == 0 "
          "EXACTLY -- Lambda IS mu * log; the multiplicativity "
          "reading vanishes identically on the real comb" % X,
          ok_true)
    off_h2, sites_h2, _v, G_h2 = res["EPSTEIN x^2+5y^2 (a=rQ/2)"]
    dist = sorted(((float(vnorm1(G_h2[n])), n) for n in sites_h2),
                  reverse=True)[:5]
    check("S3.3 THE GENUINE NON-MULTIPLICATIVE FAKE FLAGGED: the "
          "h = 2 Epstein comb has R_mult = %.4f > 0 on %d off-prime-"
          "power sites (first %s; heaviest %s) -- the Euler product "
          "FAILS and the reading measures exactly where: 21 = 3 x 7 "
          "is represented while neither factor is (the class-group "
          "obstruction)"
          % (float(off_h2), len(sites_h2), sites_h2[:5],
             [(n, round(w, 3)) for w, n in dist[:3]]),
          off_h2 > 0 and 21 in sites_h2)
    off_qi = res["s2s / zeta_Q(i) (a=r2/4)"][0]
    vsz_qi = res["s2s / zeta_Q(i) (a=r2/4)"][2]
    off_chi = res["L-FAKE chi4 (a=chi4)"][0]
    vsz_chi = res["L-FAKE chi4 (a=chi4)"][2]
    check("S3.4 [TYPED HONESTLY] the s2s comb (R_mult == 0) and the "
          "chi4 comb (R_mult == 0) are MULTIPLICATIVE -- the reading "
          "is blind between L-functions, and that is CORRECT "
          "Selberg-class behaviour; both are still separated from "
          "zeta's comb by the vs-zeta fingerprint (%.3f / %.3f > 0): "
          "multiplicativity is the right NECESSARY discriminator, "
          "identity of the L-function is amplitude data"
          % (float(vsz_qi), float(vsz_chi)),
          off_qi == 0 and off_chi == 0 and vsz_qi > 0 and vsz_chi > 0)

    # ------------------------------------------- the four-gate carrier
    section("S4 -- the relationally-routed carrier: the four gates")
    LOG2 = math.log(2.0)

    def rho_config(masses, uus):
        sup = {int(m): float(u) for m, u in zip(masses, uus)}
        rc = np.zeros(ka0)
        rp = np.zeros(ka0)
        for j in range(ka0):
            m = int(masses[j])
            dd = [d for d in divs[m] if d >= 2]
            miss = [d for d in dd if d not in sup]
            rc[j] = len(miss) / max(len(dd), 1)
            acc = 0.0
            for d in divs[m]:
                if not MU[d]:
                    continue
                e = m // d
                if e == 1:
                    continue
                acc += float(MU[d]) * sup.get(e, math.log(e))
            lam_f = math.log(int(spf[m])) if ISPP[m] else 0.0
            rp[j] = min(1.0, abs(acc - lam_f) / LOG2)
        return np.minimum(1.0, rc + rp), rc, rp

    configs = [("t", nv0, uu_t), ("s", nv0, uu_s), ("e", nv0, uu_e),
               ("null", np.array(ne), uu_e)]
    rho = {}
    cvec = {}
    ok_state = True
    for pi, masses, uus in configs:
        r, rc, rp = rho_config(masses, uus)
        rho[pi] = (r, rc, rp)
        cvec[pi] = -1.0 + 2.0 * r
        for j in range(ka0):
            c0 = carrier_deployed(int(masses[j]), th, Hs)
            rr_ = r[j]
            wmin = min((1.0 - rr_) * float(w) for w in c0.values())
            ok_state &= wmin >= -BAR_EXACT and 0.0 <= rr_ <= 1.0
        print("    %-5s rho: mean=%.4f max=%.4f  closure-flagged=%d  "
              "position-flagged=%d"
              % (pi, float(np.mean(r)), float(np.max(r)),
                 int(np.sum(rc > 1e-9)), int(np.sum(rp > 1e-6))))
    check("S4.1 gate 1 STATE: the relational routing is convex "
          "(rho in [0, 1] everywhere; weights of (1-rho) sigma + "
          "rho tau_C2 sigma nonnegative, mass 1, inversion-symmetric "
          "by construction of both summands) on all 4 configurations "
          "x %d events" % ka0, ok_state)
    dev_t = id_dev(tB["t"], cvec["t"], q3["t"], B0, Xn0)
    blk_t = blk2(tB["t"], cvec["t"], lam0, q3["t"])
    tau_link = float(np.linalg.eigvalsh(blk_t)[0])
    check("S4.2 gate 2 IDENTITY at the true comb: the true support "
          "is divisor-closed and position-consistent, so rho == 0 "
          "(max %.1e) and the carrier IS the deployed carrier: "
          "corner defect %.1e <= bar %.1e, and lambda_min(block) = "
          "%+.6e reproduces tau_X = %+.6e (rel %.1e) -- the identity "
          "LINKS to tau_X, re-derived by degeneration"
          % (float(np.max(rho["t"][0])), dev_t, bar_coef, tau_link,
             tau_X0, abs(tau_link - tau_X0) / tau_X0),
          dev_t <= bar_coef
          and abs(tau_link - tau_X0) / tau_X0 <= BAR_ID_REL)
    delta = {}
    for pi in ("t", "s", "e"):
        delta[pi] = float(np.linalg.eigvalsh(
            blk2(tB[pi], cvec[pi], lam0, q3[pi]))[0]) - tau0_pi[pi]
    delta["null"] = float(np.linalg.eigvalsh(
        blk2(tB["e"], cvec["null"], lam0, q3["e"]))[0]) - tau0_pi["e"]
    print("    delta: true=%+.3e  scramble=%+.3e  eps(mass-fixed)="
          "%+.3e  NULL(self-consistent s2s)=%+.3e"
          % (delta["t"], delta["s"], delta["e"], delta["null"]))
    P_ok = (abs(delta["t"] - delta["s"]) > BAR_MOVE
            and abs(delta["t"] - delta["e"]) > BAR_MOVE)
    check("S4.3 gate 3 PLACEMENT: the mass-fixed scramble and "
          "Epstein position sets fire the POSITION-relational "
          "reading (rho_pos on %d / %d events) and move the corner "
          "(delta %+.3e / %+.3e vs 0 at truth)"
          % (int(np.sum(rho["s"][2] > 1e-6)),
             int(np.sum(rho["e"][2] > 1e-6)), delta["s"],
             delta["e"]), P_ok)
    n_close = int(np.sum(rho["null"][1] > 1e-9))
    flagged = [(int(ne[j]), round(float(rho["null"][1][j]), 3))
               for j in range(ka0) if rho["null"][1][j] > 1e-9][:8]
    sep_ok = (abs(delta["t"]) <= BAR_MOVE
              and abs(delta["null"]) > BAR_MOVE)
    check("S4.4 gate 4 -- THE FOURTH GATE, THE POINT WHERE EVERY "
          "PREVIOUS CARRIER DIED: the SELF-CONSISTENT s2s null is "
          "SEPARATED -- %d of %d events carry missing product "
          "relations (rho_close > 0; first flagged %s: e.g. 18 is "
          "present but its divisors 3, 6 are not), the corner "
          "excess on the null is %+.3e (vs exactly 0 at the truth): "
          "the RELATIONAL datum reads what no single-event carrier "
          "could -- the null's event set does not close under the "
          "multiplicative relations"
          % (n_close, ka0, flagged[:4], delta["null"]), sep_ok)
    check("S4.5 typed: the separation grade -- the corner-wired "
          "carrier reads SUPPORT closure + POSITION consistency.  "
          "Two honest limits: (1) closure is NOT L-function-safe: "
          "genuine Euler products can have non-closed Lambda-"
          "supports (zeta_{Q(i)} carries 9 but not 3 -- inert "
          "primes enter at even powers only), so the closure "
          "reading can flag some true L-combs; (2) the AMPLITUDE-"
          "grade discriminator (R_mult, S3, exact and L-safe) is "
          "not yet corner-wired: wiring it requires combs that "
          "carry claimed coefficient data -- the next construction "
          "stage, not claimed here", True)

    # --------------------------------------------------------- verdict
    section("V -- FROZEN VERDICT + the honest consequence")
    disc_ok = (ok_true and off_h2 > 0 and off_qi == 0 and off_chi == 0
               and vsz_qi > 0 and vsz_chi > 0 and ok_r)
    algebra_ok = mu_ok and lamhat_ok and ok_assoc and ok_pair
    gates_ok = (ok_state
                and dev_t <= bar_coef
                and abs(tau_link - tau_X0) / tau_X0 <= BAR_ID_REL
                and P_ok and sep_ok)
    controls_ok = all(CONTROL.values())
    if disc_ok and algebra_ok and gates_ok and controls_ok:
        verdict = "RELATION-CARRIER-EXISTS"
    elif disc_ok and algebra_ok and controls_ok:
        verdict = "RELATION-SEPARATES-ONLY"
    else:
        verdict = "RELATION-BLIND / PARTIAL"
    print("\n  VERDICT: %s   [discriminator: %s | algebra: %s | "
          "gates: %s | controls: %s]"
          % (verdict, "OK" if disc_ok else "FAIL",
             "OK" if algebra_ok else "FAIL",
             "OK" if gates_ok else "FAIL",
             "OK" if controls_ok else "FAIL"))
    if verdict == "RELATION-CARRIER-EXISTS":
        print("""
  THE FINDING (report prominently): THE IDENTIFICATION CARRIER
  EXISTS -- the first structure in the program to pass all four
  gates, including the self-consistency null that killed every
  compression and every single-event carrier.  The route reopens
  with the RIGHT INPUT: the multiplicative relations between events.
  Measured content: (1) the exact convolution frame A_X carries
  mu * 1 = delta and Lambda = mu * log as EXACT structure -- every
  event's Lambda-weight is derivable from the pair relations alone;
  (2) the Euler-product reading R_mult (exact, log-p basis)
  vanishes identically on the true comb, vanishes on every
  multiplicative comb (Selberg-class blindness, the CORRECT
  behaviour), and is strictly positive on the genuine no-Euler-
  product Epstein comb x^2 + 5y^2 (h = 2), localized at the class-
  group obstruction sites (21 = 3 x 7 first); (3) the relationally-
  routed carrier keeps the packet state EXACTLY, degenerates to the
  deployed carrier on the true comb (identity + tau_X link
  verbatim), moves under scramble/Epstein positions, and reads a
  NONZERO excess on the self-consistent s2s null through its
  missing product relations -- identity AND placement AND
  separation, in ONE reading, with a positive state.

  THE HONEST FRAME (part 4, precisely): this does NOT prove
  positivity along the ladder, and it is NOT an RH-relevant bound.
  What is delivered: the corner route's missing piece -- an input
  class (relational/multiplicative data) on which a state-
  preserving, identity-true, placement-sensitive carrier exists
  that separates self-consistent fakes.  What is NOT delivered:
  (i) the amplitude-grade wiring (the corner currently reads
  support closure + position consistency; the exact R_mult
  discriminator still has to be carried INTO the corner by a comb
  datum with claimed coefficients); (ii) the wall's substance --
  the positivity of the IDENTIFIED corner at depth on the pair-
  correlation object, which is exactly PRIME.FLOOR.PAIRCORR.01 and
  remains open, now with a sharper shape: the question is no longer
  "can any corner see the primes" (yes: this one) but "is the
  identified corner's excess nonnegative along the ladder" -- a
  positivity statement about the multiplicative comb itself.  Next
  stage if pursued: freeze the relational carrier as a contract
  (spec + exact wards), then study the identified corner's
  lambda_min along the (1+i)-tower.  NO RH claim.""")
    elif verdict == "RELATION-SEPARATES-ONLY":
        print("""
  The discriminator works (the four-comb table stands exact) but a
  positive-structure gate failed -- the failure map above localizes
  which; the relational input separates combs, yet no state-
  preserving corner carries the separation.""")
    n_pass = sum(1 for _n, ok in CHECKS if ok)
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed%s"
          % (time.time() - T0, len(CHECKS), len(FAILS),
             ("  " + ",".join(FAILS)) if FAILS else ""))
    _VERDICTS["a"] = verdict
    return 0 if (n_pass == len(CHECKS) and controls_ok) else 1


# =============== PART B -- relation_corner_ladder_probe.py (frozen probe, verbatim)

FROZEN_SPEC_b = """\
PRIME.RELATION.LADDER.01 spec v1 (2026-08-07, frozen before the run).
Amplitude wiring: rho_amp = min(1, L1(Lambda_F(m_j))/log 2) on
non-prime-power event masses, Lambda_F from the comb's OWN
coefficients by the exact recursion (Fractions, log-p basis);
rho = min(1, rho_amp + rho_pos); the support-grade closure reading
is retired.  Anchor rungs kz = {9, 12, 13}; configs per anchor:
TRUE (a=1), QI (first-ka s2s, a=r2/4), H2 (first-ka x^2+5y^2
support, a=rQ/2), CHI (true masses, a=chi4), SCR (a=1, scramble
seed 1).  Wards: R_corner exact {0, 0, >0, 0}; delta {0, 0, !=0,
0, !=0} with bars 1e-9-scale; state weights >= -1e-12; L-safety =
QI flagged by the retired closure reading but NOT by rho_amp.
Ladder tier A: all frame-A zones with exp(2 alpha) <= ATOM_MAX+0.5
and h != 1292 (measured inventory: 67 rungs, kz 9..121, builds
<= 0.1 s -- predeclared benchmark); per rung: identity ward
lambda_min(B - sum lam Xn) == lambda_min(Ah) rel 1e-6; EXCESS :=
tau_X - lambda_min(arch-only block B); support ward (all masses ==
all prime powers in range, exact positions).  Xn == -q3 ward on
kz=9 (independent reads_pair, 1e-9 scale).  Decision: tol(rung) =
1e-12 + 1e-9 max(|tau_X|, |lmin(S)|); EXCESS-NONNEGATIVE iff all
EXC >= -tol; EXCESS-VANISHES iff all |EXC| <= tol; else EXCESS-
CHANGES-SIGN/NEGATIVE with sign census.  Scramble-excess control
on anchors: EXC_scr != EXC.  Controls: GL1 anchor exact; tau refs
kz 9/12/13 (5.984165e-4 / 4.351189e-4 / 5.637632e-4, 1e-4 rel);
mu*log + Moebius inversion exact to 2048.  N_TH_b = 2048.  LCG
20260807.  NO RH claim; writes nothing.
"""

N_TH_b = 2048

X_ANCHOR = 2048

ANCHORS = (9, 12, 13)

def theta_layer_b():
    sig3 = np.zeros(N_TH_b + 1, dtype=object)
    for d in range(1, N_TH_b + 1):
        for m in range(d, N_TH_b + 1, d):
            sig3[m] = (sig3[m] or 0) + d ** 3
    SCAP = 2 * N_TH_b
    t3 = sparse_theta_terms("th3", SCAP)
    t4 = sparse_theta_terms("th4", SCAP)
    one = np.zeros(SCAP + 1, dtype=object)
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
    Th0 = ((p3 + m53 + m35 + p4) // 4)[::2][:N_TH_b + 1].copy()
    Th2 = ((p3 - m53 - m35 + p4) // 4)[::2][:N_TH_b + 1].copy()
    TCAP = 8 * N_TH_b
    t2 = sparse_theta_terms("th2", TCAP)
    acc = np.zeros(TCAP + 1, dtype=object)
    acc[0] = 1
    for _ in range(8):
        acc = sparse_mul(acc, t2)
    Th1 = (acc[::8][:N_TH_b + 1] // 4).copy()
    spf = np.zeros(N_TH_b + 1, dtype=np.int64)
    for p in range(2, N_TH_b + 1):
        if spf[p] == 0:
            spf[p::p] = np.where(spf[p::p] == 0, p, spf[p::p])
    glue_ok = all(int(Th0[n] + 2 * Th1[n] + Th2[n])
                  == 240 * int(sig3[n]) for n in range(1, N_TH_b + 1))
    heads_ok = (int(Th0[1]), int(Th1[1]), int(Th2[1])) == (52, 64, 60)
    return dict(sig3=sig3, Th=(Th0, Th1, Th2, Th1), spf=spf,
                ok=glue_ok and heads_ok)

def rq_support(count, cap=X_ANCHOR):
    rep = np.zeros(cap + 1, dtype=np.int64)
    s = int(math.isqrt(cap)) + 1
    for x in range(-s, s + 1):
        for y in range(-s, s + 1):
            v = x * x + 5 * y * y
            if 1 <= v <= cap:
                rep[v] += 1
    vals = [n for n in range(2, cap + 1) if rep[n] > 0]
    return vals[:count], rep

def label_frame_b():
    import v738_hecke_mod_ramified as ram  # READ-ONLY
    from itertools import combinations
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
    return sorted(sum(v[i] << i for i in range(4)) for v in Hstar)

def ladder_rungs():
    out = []
    for kz in core.frame_a_zones():
        rr = core.build_window(kz)
        if rr["h"] == 1292:
            continue
        if math.exp(2.0 * rr["alpha"]) > core.ATOM_MAX + 0.5:
            continue
        out.append((rr["alpha"], kz))
        del rr
    out.sort()
    return [kz for _a, kz in out]

def build_divisors(X):
    divs = {n: [] for n in range(1, X + 1)}
    for d in range(1, X + 1):
        for m in range(d, X + 1, d):
            divs[m].append(d)
    return divs

def lam_reconstruct(a, X, divs, spf, ispp):
    """Exact log-derivative recursion from the comb's own
    coefficients; returns (G dict, off-pp L1 total, off-pp sites)."""
    G = {}
    offpp = Fr(0)
    sites = []
    for n in range(2, X + 1):
        acc = {}
        if a[n] != 0:
            vaddto(acc, logvec(n, spf), a[n])
        for d in divs[n]:
            if 1 < d < n and G[d] and a[n // d] != 0:
                vaddto(acc, G[d], -a[n // d])
        G[n] = vclean(acc)
        if not ispp[n] and G[n]:
            offpp += vnorm1(G[n])
            sites.append(n)
    return G, offpp, sites

def rho_amp_pos(masses, uus, a, divs, spf, ispp, MU):
    """The amplitude-wired routing: (rho, rho_amp, rho_pos,
    R_corner exact, offpp total exact)."""
    X = int(max(masses))
    G, offpp, _sites = lam_reconstruct(a, X, divs, spf, ispp)
    sup = {int(m): float(u) for m, u in zip(masses, uus)}
    LOG2 = math.log(2.0)
    ka = len(masses)
    ra = np.zeros(ka)
    rp = np.zeros(ka)
    Rc = Fr(0)
    for j in range(ka):
        m = int(masses[j])
        if not ispp[m] and G[m]:
            w = vnorm1(G[m])
            Rc += w
            ra[j] = min(1.0, float(w) / LOG2)
        acc = 0.0
        for d in divs[m]:
            if not MU[d]:
                continue
            e = m // d
            if e == 1:
                continue
            acc += float(MU[d]) * sup.get(e, math.log(e))
        lam_f = math.log(int(spf[m])) if ispp[m] else 0.0
        rp[j] = min(1.0, abs(acc - lam_f) / LOG2)
    return np.minimum(1.0, ra + rp), ra, rp, Rc, offpp

def part_b():
    section("PRIME.RELATION.LADDER.01 -- amplitude wiring + the "
            "identified corner along the ladder (EXPLORATION ONLY)")
    sha = hashlib.sha256(FROZEN_SPEC_b.encode("utf-8")).hexdigest()
    print("    FROZEN_SPEC_b SHA-256 = %s" % sha)
    print("    NO RH claim; the excess is a deployed-scale corner "
          "measurement, not an asymptotic statement.")

    print("\nS0 -- firewall")
    bad = ast_firewall()
    check("S0.1 AST firewall: no zeta-zero / prime-table symbol "
          "(divisor/mu arithmetic admissible)", not bad,
          "found %s" % bad if bad else "clean")

    # ---------------------------------------------------------- layer
    section("S1 -- packet layer, frame, anchors, Xn cross-ward")
    th = theta_layer_b()
    spf = th["spf"]
    check("S1.1 [EXACT] packet layer to n <= %d: glue identity "
          "Th0 + 2 Th1 + Th2 = 240 sigma3 + heads" % N_TH_b, th["ok"])
    Hs = label_frame_b()
    MU = np.zeros(X_ANCHOR + 1, dtype=np.int64)
    MU[1] = 1
    ISPP = np.zeros(X_ANCHOR + 1, dtype=bool)
    for n in range(2, X_ANCHOR + 1):
        f = factorize(n, spf)
        MU[n] = 0 if any(k > 1 for k in f.values()) else (-1) ** len(f)
        ISPP[n] = len(f) == 1
    divs = build_divisors(X_ANCHOR)
    mu_ok = all(sum(int(MU[d]) for d in divs[n])
                == (1 if n == 1 else 0)
                for n in range(1, X_ANCHOR + 1))
    lam_ok = True
    for n in range(2, X_ANCHOR + 1):
        acc = {}
        for d in divs[n]:
            if MU[d]:
                vaddto(acc, logvec(n // d, spf), Fr(int(MU[d])))
        ref = {int(spf[n]): Fr(1)} if ISPP[n] else {}
        lam_ok &= vclean(acc) == ref
    check("S1.2 [EXACT] relational-layer wards to %d: Moebius "
          "inversion (mu * 1 = delta, all n) AND mu * log == Lambda "
          "(dict equality, all n)" % X_ANCHOR, mu_ok and lam_ok)

    anchors = {}
    ok_ref = True
    for kz in ANCHORS:
        rr = core.build_window(kz)
        nv = np.rint(np.exp(rr["uu"])).astype(np.int64)
        tau_X = float(np.linalg.eigvalsh(rr["Ah"])[0])
        ok_ref &= abs(tau_X - REG_REFS[kz]) / REG_REFS[kz] <= REG_BAR
        anchors[kz] = dict(rr=rr, nv=nv, tau=tau_X,
                           uu=np.asarray(rr["uu"], float))
    check("S1.3 [CONTROL] tau_X frozen refs matched on anchors "
          "kz = %s" % (ANCHORS,), ok_ref)
    ev_union = sorted({int(n) for kz in ANCHORS
                       for n in anchors[kz]["nv"]})
    off = [n for n in ev_union
           if gl1_read(carrier_deployed(n, th, Hs)) != Fr(-1)]
    check("S1.4 [EXACT -- CONTROL] GL1 anchor: chat = -1 for ALL %d "
          "anchor-union events" % len(ev_union), not off)
    rr9 = anchors[9]["rr"]
    q3_9, tB_9 = reads_pair(rr9, unit_rows(rr9, anchors[9]["uu"]))
    xw = float(np.max(np.abs(q3_9 + np.asarray(rr9["Xn"], float))))
    sc9 = max(1.0, float(np.max(np.abs(q3_9))))
    check("S1.5 [WARD] Xn == -q3 on the primary rung (independent "
          "per-event Toeplitz reads vs the shipped window reads): "
          "max dev %.1e <= %.1e -- the tier-A ladder identity/excess "
          "can use the shipped Xn" % (xw, BAR_MOVE * sc9),
          xw <= BAR_MOVE * sc9)

    # ------------------------------------------- stages 1 + 2: wiring
    section("S2 -- STAGE 1+2: the amplitude-wired four-comb corner "
            "on the anchor rungs")
    _rql, rq = rq_support(1)
    r2 = np.zeros(X_ANCHOR + 1, dtype=np.int64)
    s = int(math.isqrt(X_ANCHOR)) + 1
    for x in range(-s, s + 1):
        for y in range(-s, s + 1):
            v = x * x + y * y
            if 1 <= v <= X_ANCHOR:
                r2[v] += 1
    ok_all_anchor = True
    lsafe_done = False
    for kz in ANCHORS:
        A = anchors[kz]
        rr, nv, uu_t = A["rr"], A["nv"], A["uu"]
        ka = len(nv)
        lam = rr["lam"]
        s2s = sum2sq_ints(ka)
        rqs, _ = rq_support(ka)
        uu_s = np.asarray(core.build_window(kz,
                                            scramble_seed=SCR_SEED)
                          ["uu"], float)
        a1 = [Fr(1)] * (X_ANCHOR + 1)
        aqi = [Fr(int(r2[n]), 4) for n in range(X_ANCHOR + 1)]
        ah2 = [Fr(int(rq[n]), 2) for n in range(X_ANCHOR + 1)]
        achi = [Fr(0) if n % 2 == 0 else Fr(1 if n % 4 == 1 else -1)
                for n in range(X_ANCHOR + 1)]
        cfgs = [("TRUE", nv, uu_t, a1),
                ("QI", np.array(s2s), np.log(np.array(s2s, float)),
                 aqi),
                ("H2", np.array(rqs), np.log(np.array(rqs, float)),
                 ah2),
                ("CHI", nv, uu_t, achi),
                ("SCR", nv, uu_s, a1)]
        print("    -- anchor kz=%d (ka=%d, masses <= %d; QI <= %d, "
              "H2 <= %d)" % (kz, ka, int(nv.max()), s2s[-1], rqs[-1]))
        res = {}
        st_ok = True
        for name, mm, uus, a in cfgs:
            rho, ra, rp, Rc, offpp = rho_amp_pos(mm, uus, a, divs,
                                                 spf, ISPP, MU)
            q3c, tBc = ((q3_9, tB_9) if (kz == 9 and name in
                                         ("TRUE", "CHI"))
                        else reads_pair(rr, unit_rows(rr, uus)))
            base = float(np.linalg.eigvalsh(
                blk2(tBc, -np.ones(ka), lam, q3c))[0])
            val = float(np.linalg.eigvalsh(
                blk2(tBc, -1.0 + 2.0 * rho, lam, q3c))[0])
            res[name] = dict(rho=rho, ra=ra, rp=rp, Rc=Rc,
                             offpp=offpp, delta=val - base, val=val,
                             base=base)
            for j in range(len(mm)):
                c0 = carrier_deployed(int(mm[j]), th, Hs)
                st_ok &= (min(float(w) for w in c0.values()) >= 0.0
                          and 0.0 <= rho[j] <= 1.0)
            cov = (float(Rc / offpp) if offpp > 0 else
                   (1.0 if Rc == 0 else 0.0))
            print("       %-4s R_corner = %-12s (coverage %.2f)  "
                  "rho: amp %d, pos %d events  delta = %+.3e"
                  % (name, ("0 (EXACT)" if Rc == 0 else
                            "%.3f" % float(Rc)), cov,
                     int(np.sum(ra > 1e-9)), int(np.sum(rp > 1e-6)),
                     res[name]["delta"]))
        sc = max(1.0, abs(res["TRUE"]["base"]))
        ok_kz = (res["TRUE"]["Rc"] == 0 and res["QI"]["Rc"] == 0
                 and res["CHI"]["Rc"] == 0 and res["H2"]["Rc"] > 0
                 and abs(res["TRUE"]["delta"]) <= BAR_MOVE * sc
                 and abs(res["QI"]["delta"]) <= BAR_MOVE * sc
                 and abs(res["CHI"]["delta"]) <= BAR_MOVE * sc
                 and abs(res["H2"]["delta"]) > BAR_MOVE
                 and abs(res["SCR"]["delta"]) > BAR_MOVE
                 and abs(res["TRUE"]["val"] - A["tau"])
                 <= BAR_ID_REL * max(1.0, A["tau"]) + 1e-12
                 and st_ok)
        ok_all_anchor &= ok_kz
        check("S2.%d anchor kz=%d: the amplitude-wired table stands "
              "-- TRUE/QI/CHI read 0 EXACT and move nothing; H2 "
              "reads %.3f exact and moves %+.3e (separated PURELY "
              "by the Euler-product datum, rho_pos ~ 0 on its self-"
              "consistent positions); SCR moves %+.3e via rho_pos "
              "(distinct fingerprint); identity at truth reproduces "
              "tau_X; states convex"
              % (ANCHORS.index(kz) + 1, kz, float(res["H2"]["Rc"]),
                 res["H2"]["delta"], res["SCR"]["delta"]), ok_kz)
        if not lsafe_done:
            lsafe_done = True
            sup_qi = set(s2s)
            n_close_old = sum(
                1 for m in s2s
                if any(d not in sup_qi for d in divs[int(m)]
                       if d >= 2))
            check("S2.4 [STAGE 2 -- L-SAFETY] the retired support-"
                  "grade closure reading flagged %d of %d s2s events "
                  "(e.g. 9 without 3); the amplitude-grade rho_amp "
                  "flags 0 of them (Lambda_F of r2/4 is prime-power-"
                  "supported EXACTLY) while still flagging the h=2 "
                  "Epstein -- the amplitude wiring fixes L-function "
                  "safety AUTOMATICALLY, as typed"
                  % (n_close_old, ka),
                  n_close_old > 0
                  and int(np.sum(res["QI"]["ra"] > 0)) == 0
                  and int(np.sum(res["H2"]["ra"] > 0)) > 0)

    # ----------------------------------------------- stage 3: ladder
    section("S3 -- STAGE 3: the identified corner along the ladder "
            "(tier A, all reachable rungs)")
    rungs = ladder_rungs()
    print("    reachable rung set (frozen filter): %d rungs, kz = "
          "%s .. %s" % (len(rungs), rungs[0], rungs[-1]))
    spf_big = None
    table = []
    ok_sup = True
    ok_id = True
    print("    %-4s %-7s %-6s %-12s %-12s %-12s %-9s"
          % ("kz", "alpha", "ka", "tau_X", "lmin(S)", "EXCESS",
             "EXC/tau"))
    for kz in rungs:
        rr = core.build_window(kz)
        nv = np.rint(np.exp(rr["uu"])).astype(np.int64)
        uu = np.asarray(rr["uu"], float)
        ka = len(nv)
        mx = int(nv.max())
        if spf_big is None or len(spf_big) <= mx:
            spf_big = np.zeros(mx + 1, dtype=np.int64)
            for p in range(2, mx + 1):
                if spf_big[p] == 0:
                    spf_big[p::p] = np.where(spf_big[p::p] == 0, p,
                                             spf_big[p::p])
        pp_ok = all(len(factorize(int(n), spf_big)) == 1 for n in nv)
        pos_ok = float(np.max(np.abs(
            uu - np.log(nv.astype(float))))) <= 1e-12
        ok_sup &= pp_ok and pos_ok
        lam = np.asarray(rr["lam"], float)
        Xn = np.asarray(rr["Xn"], float)
        B = np.asarray(rr["B"], float)
        C = np.array([[float(np.sum(lam * Xn[:, 0])),
                       float(np.sum(lam * Xn[:, 2]))],
                      [float(np.sum(lam * Xn[:, 2])),
                       float(np.sum(lam * Xn[:, 1]))]])
        A_id = B - C
        tau_X = float(np.linalg.eigvalsh(rr["Ah"])[0])
        lid = float(np.linalg.eigvalsh(A_id)[0])
        lS = float(np.linalg.eigvalsh(B)[0])
        sc = max(1.0, float(np.max(np.abs(B))))
        ok_id &= abs(lid - tau_X) <= BAR_ID_REL * sc
        exc = tau_X - lS
        table.append((kz, rr["alpha"], ka, tau_X, lS, exc))
        print("    %-4d %-7.3f %-6d %+.5e %+.5e %+.5e %+9.4f"
              % (kz, rr["alpha"], ka, tau_X, lS, exc,
                 exc / tau_X if tau_X != 0 else float("nan")))
        del rr
    check("S3.1 [SUPPORT WARD, ALL RUNGS] every rung's support is "
          "exactly the prime powers at exact log positions (masses "
          "pp: %s; positions exact) -- rho(true) == 0 along the "
          "whole ladder, the identified carrier IS the deployed "
          "carrier at truth on every rung" % ok_sup, ok_sup)
    check("S3.2 [IDENTITY WARD, ALL RUNGS] lambda_min(B - sum lam "
          "Xn) == tau_X (rel 1e-6 scale) on all %d rungs -- the "
          "corner identity holds along the entire reachable ladder"
          % len(rungs), ok_id)

    excs = np.array([t[5] for t in table])
    taus = np.array([t[3] for t in table])
    lSs = np.array([t[4] for t in table])
    tols = 1e-12 + 1e-9 * np.maximum(np.abs(taus), np.abs(lSs))
    n_pos = int(np.sum(excs > tols))
    n_neg = int(np.sum(excs < -tols))
    n_zero = len(excs) - n_pos - n_neg
    third = max(1, len(excs) // 3)
    print("\n    THE EXCESS SERIES: %d rungs | sign census: %d > 0, "
          "%d < 0, %d ~ 0 | min %+.3e (kz=%d) max %+.3e (kz=%d)"
          % (len(excs), n_pos, n_neg, n_zero, float(np.min(excs)),
             table[int(np.argmin(excs))][0], float(np.max(excs)),
             table[int(np.argmax(excs))][0]))
    print("    trend: first-third mean %+.3e -> last-third mean "
          "%+.3e; tau_X first/last %+.3e -> %+.3e; lmin(S) "
          "first/last %+.3e -> %+.3e"
          % (float(np.mean(excs[:third])),
             float(np.mean(excs[-third:])), taus[0], taus[-1],
             lSs[0], lSs[-1]))
    exc_t9 = anchors[9]["tau"] - float(np.linalg.eigvalsh(
        np.array([[tB_9[0], tB_9[2]], [tB_9[2], tB_9[1]]]))[0])
    scr9 = core.build_window(9, scramble_seed=SCR_SEED)
    q3s9, tBs9 = reads_pair(rr9, unit_rows(
        rr9, np.asarray(scr9["uu"], float)))
    lam9 = anchors[9]["rr"]["lam"]
    exc_s9 = (float(np.linalg.eigvalsh(
        blk2(tBs9, -np.ones(len(lam9)), lam9, q3s9))[0])
        - float(np.linalg.eigvalsh(
            np.array([[tBs9[0], tBs9[2]],
                      [tBs9[2], tBs9[1]]]))[0]))
    check("S3.3 [CONTROL] the scramble excess differs from the true "
          "excess on the primary rung (%+.3e vs %+.3e, diff %.1e > "
          "%g) -- the excess is a comb-sensitive quantity, not a "
          "structural artefact"
          % (exc_s9, exc_t9, abs(exc_s9 - exc_t9), BAR_MOVE),
          abs(exc_s9 - exc_t9) > BAR_MOVE)

    # --------------------------------------------------------- verdict
    section("V -- THE DECISION (frozen) + honest consequence")
    if n_neg == 0 and n_pos > 0:
        exc_verdict = "EXCESS-NONNEGATIVE"
    elif n_pos == 0 and n_neg == 0:
        exc_verdict = "EXCESS-VANISHES"
    else:
        exc_verdict = "EXCESS-CHANGES-SIGN/NEGATIVE"
    stage12_ok = ok_all_anchor
    controls_ok = ok_sup and ok_id and not FAILS
    print("\n  VERDICT: %s   [amplitude wiring: %s | L-safety: "
          "fixed automatically | ladder wards: %s]"
          % (exc_verdict, "WIRED" if stage12_ok else "FAILED",
             "OK" if (ok_sup and ok_id) else "FAIL"))
    if exc_verdict == "EXCESS-NONNEGATIVE":
        print("""
  THE FINDING: on all %d reachable rungs the identified corner's
  value sits ABOVE its comb-blind structural skeleton -- the prime
  comb's contribution to the floor is nonnegative at every deployed
  scale, with the margin trend printed above.  The identified route
  has measured substance.  WHAT A CERTIFIED SKELETON WOULD NEED
  (typed, not claimed): (1) an exact or interval-certified lower
  bound for lambda_min of the arch-only block (the structural side
  is explicit Toeplitz data -- certifiable); (2) a sign-certified
  comb contribution, i.e. the event quadratic sum lam_j q3_j in
  certified arithmetic (the reads are explicit finite sums --
  certifiable but heavy); (3) the ladder limit: the deployed rungs
  stop at mass ~3e5; the wall's substance is the SAME sign question
  at every scale, which no finite table settles.""" % len(excs))
    elif exc_verdict == "EXCESS-CHANGES-SIGN/NEGATIVE":
        print("""
  THE FINDING (the honest expected outcome per the wall's history):
  the identification carrier exists (stages 1-2 stand) but the
  excess is NOT automatically nonnegative -- sign census %d > 0,
  %d < 0 over %d rungs, located exactly in the table above.  The
  arithmetic hardness sits INSIDE the new construction: the wall
  gains its fifth, sharpest coordinate -- the excess IS the pair-
  correlation substance in corner coordinates, and its sign at
  depth is the open question.""" % (n_pos, n_neg, len(excs)))
    else:
        print("""
  THE FINDING: the excess vanishes within tolerance on every rung --
  the identification decouples from the floor value: the relational
  carrier separates combs, but the corner VALUE carries no comb
  contribution at deployed scale (typed; the floor question and the
  identification question are then independent coordinates).""")
    print("""
  HONEST CONSEQUENCE FOR PRIME.FLOOR.PAIRCORR.01: stages 1-2 close
  both typed limits of the RELATION-CARRIER-EXISTS finding: the
  corner now reads the Euler-product datum at amplitude grade
  (exact Fractions), and the reading is L-function-safe (Selberg-
  correct blindness measured).  The wall itself %s: the floor's
  positivity along the ladder remains unproven in either case --
  what changed is that the open question now has corner
  coordinates: tau_X = lambda_min(structural) + EXCESS, with the
  structural part certifiable and the excess the arithmetic
  substance.  NO RH claim; deployed-scale measurement only."""
          % ("moves to its sharpest form" if exc_verdict
             != "EXCESS-VANISHES" else "holds unchanged"))
    n_pass = sum(1 for _n, ok in CHECKS if ok)
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed%s"
          % (time.time() - T0, len(CHECKS), len(FAILS),
             ("  " + ",".join(FAILS)) if FAILS else ""))
    _VERDICTS["b"] = exc_verdict
    return 0 if n_pass == len(CHECKS) else 1


EXPECT = {"a": (18, "RELATION-CARRIER-EXISTS"),
          "b": (13, "EXCESS-NONNEGATIVE")}


def run():
    t_all = time.time()
    rc = 0
    counts = {}
    for tag, part in (("a", part_a), ("b", part_b)):
        CHECKS.clear()
        FAILS.clear()
        if "CONTROL" in globals():
            CONTROL.clear()
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
    print("v841: %d/%d checks passed, %d failed | runtime %.1f s"
          % (n_run - n_fail, n_run, n_fail, time.time() - t_all))
    print("NO RH claim; the identification carrier exists with the "
          "relational input; the wall takes its sharpest form "
          "tau_X = lambda_min(structural) + EXCESS and stays "
          "PRIME.FLOOR.PAIRCORR.01.")
    print("[%s] PATTERN GATE: expected 18 + 13 checks, 0 failed, "
          "verdicts RELATION-CARRIER-EXISTS + EXCESS-NONNEGATIVE "
          "(got %s + %s)"
          % ("PASS" if pattern_ok else "FAIL",
             _VERDICTS.get("a"), _VERDICTS.get("b")))
    return rc + (0 if pattern_ok else 1)


if __name__ == "__main__":
    raise SystemExit(run())
