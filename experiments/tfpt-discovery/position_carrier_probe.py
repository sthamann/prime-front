#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""position_carrier_probe -- PRIME.CARRIER.POSITION.01 (EXPLORATION
ONLY, experiments/; the first typed INPUT-CHANGE candidate after
LEVEL2-CLOSED / EXPECTATION-CLOSED: the position-dependent carrier
map, 2026-08-07).

THE INPUT (frozen, read-only): the closure theorems say no compression
of the deployed register machinery carries identity AND placement --
the deployed carrier map n -> sigma(x_n) is position-blind and the
corner identity pins every reading.  CANDIDATE 1: build the positions
into the CARRIER CONSTRUCTION itself: sigma' = F(n_j, u_j), reading
both the mass index n_j and the actual position u_j (at the true
configuration u_j = log n_j; scramble/Epstein move u_j with the mass
list held fixed -- the convention of all previous probes).

THE CONSTRUCTION SPACE (frozen design rules, source-native; no target
data, no zeros, no tau, no fitting):
  A  ADDRESS-ROUTED (tower-consistency routing): the position's
     claimed integer ntilde_j = round(exp(u_j)) is reduced in the
     (1+i)-tower R_3 = Z[i]/(1+i)^3 (the level-3 address, 3 dyadic
     digits); beta_j = Hamming(addr(n_j), addr(ntilde_j))/3 in
     {0, 1/3, 2/3, 1}; the carrier routes beta_j of its mass to the
     C2-shifted copy: sigma_A = (1 - beta) sigma + beta tau_C2 sigma.
     Positions enter ONLY through the arithmetic of ntilde mod the
     tower.  At the true configuration ntilde = n, beta = 0: the
     construction DEGENERATES to the deployed carrier exactly.
  B1 LAG-GRADED, mu4 slot (symmetrized): bin_j = floor(u_j /
     (alpha/8)) mod 4; sigma_B1 = (tau_mu4^{+bin} + tau_mu4^{-bin})
     sigma / 2 (self-adjoint by symmetrization).
  B2 LAG-GRADED, C2 slot: flip_j = bin_j mod 2; sigma_B2 =
     tau_C2^{flip} sigma -- the ABSOLUTE position grading in the
     sign slot.
  C  FREE SLOT (predeclared best design): the V-AMPLITUDE-GRADED
     carrier: for ram-odd events the H* spread is tilted by the
     window's own fundamental position read s_j = cos(pi u_j /
     (2 alpha)): p_v(v) = (1 + kappa s_j eps(v)) / Z_j on H*,
     eps(v) = (-1)^{popcount(v)}, kappa = 1/4, Z_j the normalizer
     (mass preserved EXACTLY -- the state-safe way to grade the
     V slot).

THE THREE GATES per variant (frozen, the standing bars):
  (a) STATE: the carrier stays a genuine positive state datum -- a
      symmetric PROBABILITY distribution on G (weights >= 0, mass 1,
      inversion-symmetric; note the deployed carrier is exactly this,
      and its convolution operator is a self-adjoint CONTRACTION, not
      PSD -- chat(GL1) = -1 is an eigenvalue; the positivity that
      matters is the state/probability structure).  Measured exactly
      (Fractions) where the design is rational; spectrum ward
      (all-128 Fourier: real, |chat| <= 1) on representatives.
  (b) IDENTITY at the true configuration, weight-generic: the corner
      identity of the deployed form (defect <= 1e-9 scale) -- with
      the DERIVATION per variant, not just the test: A degenerates
      to the deployed carrier at truth (identity inherited
      verbatim); B1 is GL1-invisible because the mu4 rotation leaves
      the C2-mass read unchanged; C is GL1-invisible because the
      GL1 corner reads only the (normalized) V-mass; B2 has NO
      identity: the typed defect = 2 |q_j| on odd-bin events
      (formula matched to the measured defect).
  (c) PLACEMENT: scramble (seed 1) / Epstein (positions moved, mass
      list fixed) must move the corner excess.

THE DECISIVE FOURTH MEASUREMENT (frozen with the spec): THE
SELF-CONSISTENCY NULL.  A carrier map F(n, u) that keeps the state
and the identity at ALL true configurations must read position only
through the consistency defect (n vs u), which VANISHES on every
self-consistent comb.  The null: the Epstein comb made self-
consistent (masses = the sums-of-two-squares integers, positions =
their own logs).  An identification carrier must SEPARATE: excess
signal ~ 0 at the truth AND > bar at the self-consistent fake.
VERDICT RULE (frozen): POSITION-CARRIER-CARRIES requires gates
(a) + (b) + (c) AND the null separation; gates without separation =
the consistency channel only (typed, no reopening).

THE STRUCTURAL PATTERN UNDER TEST (the fourth-wall candidate):
EXTREMAL PINNING.  For ANY state carrier, chat_GL1 = mass(a=0) -
mass(a=1) lies in [-1, 1]; the identity pins it to the EXTREME point
-1, i.e. the ENTIRE C2 mass is locked.  Hence a state-preserving,
identity-true carrier has zero first-order position freedom at every
configuration where the identity is required; what remains is a
NONNEGATIVE consistency defect that vanishes identically on self-
consistent combs -- position-dependence in the carrier is
incompatible with (state + identity + separation).  Measured, not
assumed.

CONTROLS: deployed-carrier regression (position-blind, chat_j = -1
exact on all union events; identity holds; tau_X reproduced on 3
windows, frozen refs); variant A degenerates to the deployed carrier
at truth EXACTLY (weight-level dict equality); state wards per
variant x position set; scramble/Epstein per gate; the GL1 anchor.

FROZEN VERDICTS: POSITION-CARRIER-CARRIES (variant + all three gates
+ null separation -- the reopening; report prominently) /
POSITION-CARRIER-TRADEOFF (the failure map typed, structural pattern
named) / POSITION-CARRIER-PARTIAL.

HONESTY GATES: NO RH claim; nothing outside experiments/ touched; no
file written; stop-list respected (v831 / PRIME.FLOOR.PAIRCORR.01
binding).  FIREWALL: no zeta zero, no prime-table symbol
(AST-checked; own sieves); v563/v738 imports READ-ONLY.

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/position_carrier_probe.py
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


# ============================================================ ring layer
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
def chival(chi, g):
    eps, w, j = chi
    a, v, m = g
    s = (-1) ** (eps * a) * (-1) ** (bin(w & v).count("1"))
    q = (j * m) % 4
    return [(s, 0), (0, s), (-s, 0), (0, -s)][q]


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
    section("PRIME.CARRIER.POSITION.01 -- the position-dependent "
            "carrier map (EXPLORATION ONLY)")
    sha = hashlib.sha256(FROZEN_SPEC.encode("utf-8")).hexdigest()
    print("    FROZEN_SPEC SHA-256 = %s" % sha)
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
        q3[p], tB[p] = reads_pair(rr0, unit_rows(rr0, uu))
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
    return 0 if (n_pass == len(CHECKS) and controls_ok) else 1


if __name__ == "__main__":
    raise SystemExit(main())
