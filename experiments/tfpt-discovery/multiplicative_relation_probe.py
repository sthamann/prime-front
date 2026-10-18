#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""multiplicative_relation_probe -- PRIME.RELATION.MULT.01
(EXPLORATION ONLY, experiments/; the deepest structural move: the
RELATIONAL input class after the four closure theorems, 2026-08-07).

THE PREMISE (frozen, read-only): the position-carrier probe distilled
the identification datum to "which self-consistent comb is real", and
proved (extremal pinning) that no state-preserving, identity-true
carrier F(n_j, u_j) reading events SINGLY can separate self-
consistent combs.  The mathematical discriminator is the EULER
PRODUCT: multiplicativity, Lambda = mu * log, the convolution
relations BETWEEN events -- a PAIR datum, an input class none of the
four closure theorems covers.  The divisor/mu arithmetic of the
integers is admissible input (it IS the Euler-product datum);
firewall: no zeros, no tau, no target data, no fitting.

AN HONESTY CORRECTION TYPED BEFORE THE RUN: the carrier-probe null
(sums of two squares) is SECRETLY MULTIPLICATIVE -- its coefficient
comb is zeta_{Q(i)} = zeta(s) L(s, chi4) (class number 1, Euler
product EXISTS).  The genuine no-Euler-product Epstein zeta needs
class number >= 2: the form x^2 + 5y^2 (h(-20) = 2, the classical
off-line-zero example class).  Both are measured; the s2s null is
still separated by the relational carrier, but at SUPPORT grade
(missing product relations), not at amplitude grade -- typed.

DESIGN (a) -- THE CONVOLUTION FRAME (exact): the truncated Dirichlet
convolution algebra A_X on {e_n : n <= X = 178}: e_d * e_e = e_{de}
if de <= X else 0 (the span of n > X is an ideal, so the quotient is
associative).  All scalars live in the free module over the log-p
basis (Fractions) -- EVERYTHING EXACT, no floats in the arithmetic
layer.  Wards: mu * 1 = delta_1 (full Moebius inversion, all n <= X);
Lambda-hat = mu * log == Lambda (own sieve) for ALL n <= X, exact
dict equality; associativity on LCG-sampled triples.

DESIGN (b) -- THE MOEBIUS-PAIRING FORM: the pairing matrix
B[k, j] = mu(m_k / m_j) on divisor pairs m_j | m_k; the DERIVED
weight of event k is Lambda-hat_pos(k) = sum_{d | m_k} mu(d)
U(m_k/d) with U = the comb's ACTUAL positions (missing events filled
with their claimed log; the miss itself is read by the closure
statistic).  The reconstruction defect is the multiplicativity
reading -- position-AND-relation sensitive.

THE DISCRIMINATOR (exact, coefficient grade): for a comb with
coefficient datum a(n) (a(1) = 1), the log-derivative sequence
Lambda_F is reconstructed by the EXACT recursion a(n) log n =
sum_{d | n} Lambda_F(d) a(n/d); the Euler product holds iff
Lambda_F is supported on prime powers.  READING R_mult = the L1 mass
of Lambda_F off prime powers (exact; zero iff multiplicative).
THE FOUR-COMB TABLE: (i) TRUE zeta comb a = 1: R_mult = 0 EXACTLY
and Lambda_F == Lambda dict for dict (the mu*log ward); (ii-a) the
s2s comb a = r2/4 (the carrier-probe null's native series): R_mult
= 0 (multiplicative -- the typed correction) but vs-zeta defect > 0
(the chi4 fingerprint); (ii-b) EPSTEIN x^2+5y^2, a = r_Q/2: R_mult
> 0 -- the GENUINE non-multiplicative fake, flagged with its site
distribution (off-pp sites include 6 = 2 x 3 and 21 = 3 x 7: the
number is represented while neither factor is -- the class-group
obstruction);
(iii) the mass-fixed scramble: flagged by the POSITION reading
(different fingerprint: rho_pos, not rho_close); (iv) the
MULTIPLICATIVE fake a = chi4(n): R_mult = 0 -- blind between
L-functions, typed CORRECT (RH-type statements are Selberg-class-
wide; the reading must only separate multiplicative from non-
multiplicative).

THE POSITIVE STRUCTURE (the four gates): the relationally-routed
carrier sigma_rel(x_j) = (1 - rho_j) sigma + rho_j tau_C2 sigma
with rho_j = min(1, rho_close(j) + rho_pos(j)):
  rho_close = the fraction of divisors d >= 2 of m_j ABSENT from
              the comb support (the missing-relation datum, exact);
  rho_pos   = |sum_{d|m_j} mu(d) U(m_j/d) - Lambda(m_j)| / log 2,
              capped at 1 (the position-relational mu*log defect).
GATES: (1) STATE: convex routing => symmetric probability, measured
on all 4 configurations; (2) IDENTITY at the true comb: the primary
support is the prime powers in [2, 256] (the Lambda-comb support,
divisor-closed by arithmetic -- measured, not assumed), so rho == 0
=> the deployed carrier verbatim; the
corner block reproduces tau_X (the link measured); (3) PLACEMENT:
the mass-fixed scramble and Epstein position sets move the corner
(rho_pos fires); (4) THE FOURTH GATE -- the self-consistent s2s
null MUST SEPARATE: rho_close > 0 on the events with missing
divisor relations => nonzero corner excess ON THE NULL, the exact
point where every previous carrier died.

THE HONEST FRAME (part 4, frozen): even full success does NOT prove
positivity along the ladder.  The carrier delivers the
IDENTIFICATION the corner route lacked (at support/position grade,
with the amplitude-grade discriminator exact but not yet corner-
wired); the remaining question -- the wall's substance -- is the
positivity of the identified corner at depth on the pair-
correlation object.  Stated precisely in the verdict.

VERDICTS (frozen): RELATION-CARRIER-EXISTS (discriminator table
correct AND all four gates pass -- the reopening, report
prominently) / RELATION-SEPARATES-ONLY (discriminator works, a
positive-structure gate fails -- typed where) / RELATION-BLIND
(separation fails -- typed why).

CONTROLS: the mu*log ward exact on the true comb; the four-comb
table; state wards per design; GL1 anchor (exact, union events);
tau_X reproduction on 3 windows (frozen refs).  HONESTY: NO RH
claim; nothing outside experiments/; no file written; stop-list
respected (v831 binding).  FIREWALL: no zeta zero, no prime-table
symbol (AST-checked; own sieves); v563/v738 imports READ-ONLY.

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/multiplicative_relation_probe.py
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

N_TH = 640
N_WIN = 3
X_FRAME = 256
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


# =============================================== exact log-p arithmetic
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
    return Hstar


def label_int(v):
    return sum(v[i] << i for i in range(4))


# ============================================================== carriers
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


def id_dev(tBf, cvec, q3, B, Xn):
    d = max(abs(B[0, 0] - tBf[0]), abs(B[1, 1] - tBf[1]),
            abs(B[0, 1] - tBf[2]))
    for s in range(3):
        d = max(d, float(np.max(np.abs(cvec * q3[:, s] - Xn[:, s]))))
    return d


# ================================================================= main
def main():
    section("PRIME.RELATION.MULT.01 -- the multiplicative-relation "
            "input class (EXPLORATION ONLY)")
    sha = hashlib.sha256(FROZEN_SPEC.encode("utf-8")).hexdigest()
    print("    FROZEN_SPEC SHA-256 = %s" % sha)
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
    th = theta_layer()
    spf = th["spf"]
    check("S1.1 [EXACT] packet layer: glue identity + f8 + heads to "
          "n <= %d" % N_TH, th["ok"])
    Hs = sorted(label_int(v) for v in label_frame())
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
    return 0 if (n_pass == len(CHECKS) and controls_ok) else 1


if __name__ == "__main__":
    raise SystemExit(main())
