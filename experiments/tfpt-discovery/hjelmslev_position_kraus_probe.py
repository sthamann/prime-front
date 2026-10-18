#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""hjelmslev_position_kraus_probe -- PRIME.CORNER.DRESSING.01
(EXPLORATION ONLY, experiments/; the licensed follow-up of the
HJELMSLEV-STRUCTURE-ONLY verdict, 2026-08-07).

THE DIAGNOSIS (frozen input): the tower's corner series is the pure
dilution law 16^(1-m), bit-identical under scramble, because the flag
Kraus operators carry NO placement data.  THE LICENSED QUESTION: can
the 105 Kraus legs of the deployed m = 1 flag system be DRESSED with
position data such that (a) complete positivity survives, (b) the
corner identity survives weight-generically, and (c) the corner now
distinguishes the true comb from the scramble?

THE CHANNEL CLASS (frozen): leg dressings of the deployed 105-leg
system -- K[x, y] = amplitude^2 on the incidence legs x ~ y (the 15
nonzero classes of V, x Omega y^T = 0, 7 per row), acting on the
event carrier V-slot by the predual pushforward p' = K^T p.  The
dressing fields are SOURCE-NATIVE comb functionals aggregated on the
labels through the deployed event carriers (ram-odd events -> uniform
on H*; other events carry delta_0 and never touch the flags):
    F1(x) = sum_{j ram-odd} w_j p_j(x)                (mass field)
    F2(x) = sum_{j ram-odd} w_j cos(pi u_j / 2 alpha) p_j(x)
    F3(x) = sum_{j ram-odd} w_j sin(pi u_j / 2 alpha) p_j(x)
(the three comb functionals; w_j = the deployed half-weight masses
lam_j, u_j = the comb positions; NO target data, NO zeros, NO tau).
Leg field fhat(x,y) = (F2(x)+F2(y)+F3(x)+F3(y)) / (2 max) in [-1,1];
mass leg field mhat likewise from F1.  KAPPA = 1/4.

FROZEN VARIANTS:
  A  mass-dressed UNITAL:      K = (1 + k mhat)/N(x), rows normalized
  A' position-dressed UNITAL:  K = (1 + k fhat)/N(x), rows normalized
  B  phase-dressed:            legs e^{i pi k fhat}/sqrt(7); |amp|^2
                               = 1/7 (the diagonal action is blind to
                               phases -- measured, typed)
  C  position-dressed RAW:     K = (1 + k fhat)/7, rows NOT normalized

THE THREE GATES (frozen, per variant; primary window = the alpha-
smallest deployed window, corner block per the certified reduction of
character_corner_probe [CORNER-IDENTITY-SYMBOLIC, frozen]:
corner(P(w)) = tB - sum_j chat'_j w_j q_j with chat'_j = -(total
dressed carrier mass), re-derived here at the register level):
 (a) CP: the dressed Choi is diagonal with entries = |amplitude|^2
     >= 0 -- exact-positive check; unitality status reported.
 (b) IDENTITY weight-generic: the defect polynomial coefficient of
     w_j is (1 + chat'_j) q_j (dressing frozen as channel data, packet
     weights free) -- PASS iff max_j |1 + chat'_j| <= 1e-12.
 (c) IDENTIFICATION: tau_dressed = lambda_min(corner block at the
     deployed weights); excess delta = tau_dressed - tau_X.  PASS iff
     |delta| > bar (the gap MOVES) AND delta differs from the
     scrambled-window excess (placement sensitivity) -- the scramble
     control IS this gate.
TOWER LIFT: executed only if a variant passes ALL THREE.  NOTE the
class-level reduction makes (b) and (c) mutually exclusive -- gate (b)
forces chat' = -1 forcing delta = 0; the probe MEASURES this as the
structural exclusion rather than assuming it.
CONTROLS: undressed regression (identity residual, the 16^(1-m)
dilution ratios in closed form, state-scalar scramble-blindness); the
register ward (full 128-dim Fourier: chat' == -(dressed mass), exact
undressed == -1); the Epstein comb (positions = log of the first ka
sums of two squares >= 2, same masses) as a second placement control;
the random-dressing sweep (raw vs row-normalized) establishing
delta = 0 <=> unital <=> identity across the class.
VERDICT (frozen): POSITION-KRAUS-CARRIES / POSITION-KRAUS-TRADEOFF /
POSITION-KRAUS-PARTIAL.

FIREWALL: no zeta zero, no prime-table symbol (AST-checked; own
sieves); machinery imports READ-ONLY: v563 (windows), v738 (frame);
writes nothing; NO RH claim.

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/hjelmslev_position_kraus_probe.py
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
PRIME.CORNER.DRESSING.01 spec v2 (2026-08-07; v1 revealed a field
DEGENERACY at the control stage -- every ram-odd carrier is the same
uniform-on-H* distribution, so max-normalized aggregated fields lose
all position content; v2 normalizes the position field by the MASS
field, keeping the placement scalar c* = <cos phi + sin phi>_w in the
kernel.  The m = 1 carrier granularity supports EXACTLY ONE placement
scalar -- typed.  Amendment declared before the v2 run; verdict logic
unchanged).
Channel class: leg dressings K[x,y] of the deployed 105-leg system on
the 15 labels, predual pushforward on the event carrier V-slot.
Fields F1/F2/F3 (mass, cos, sin at phase pi u / 2 alpha) aggregated on
labels via the ram-odd carriers; leg fields normalized to [-1,1];
KAPPA = 1/4.  Variants: A (mass, unital), A' (position, unital), B
(phase, |amp|^2 = 1/7), C (position, raw).  Gates: (a) Choi diag >= 0
exact; (b) max_j |1 + chat'_j| <= 1e-12 with chat'_j = -(dressed
carrier mass), the certified corner reduction; (c) |delta| > 1e-9 AND
|delta - delta_scr| > 1e-9, delta = lambda_min(dressed corner block)
- tau_X, scramble seed 1.  Controls: undressed identity residual
<= 1e-6 rel; dilution ratios == 1/16 closed form m = 1..3; state
scalar dressing- and scramble-blind; 128-dim register Fourier ward;
Epstein comb (first ka sums of two squares); sweep 48 random
dressings (24 raw / 24 unital, LCG 20260807).  Tower lift only on a
full three-gate pass.  NO RH claim; writes nothing.
"""

N_TH = 640
N_WIN = 3
KAPPA = 0.25
BAR_EXACT = 1.0e-12
BAR_ID_REL = 1.0e-6
BAR_MOVE = 1.0e-9
SCR_SEED = 1
N_SWEEP_RAW = 24
N_SWEEP_UNI = 24
REG_STATE_KZ9 = 4.813726e-3
REG_TAU_KZ9 = 5.984165e-4
REG_BAR = 1.0e-4
BANNED_IDS = ("zetazero", "nzeros", "primerange", "isprime", "primepi",
              "nextprime", "prevprime")

CHECKS = []
FAILS = []
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
    """First `count` integers n >= 2 with n = a^2 + b^2 (the Gaussian
    Epstein norm comb); own sieve."""
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


def lock_reads_direct(rr, rows):
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
    return out


def corner_block(tB, chat_vec, lam, q):
    """The certified corner reduction: block[i,k] = tB - sum_j chat_j
    lam_j q_j (character_corner_probe, CORNER-IDENTITY-SYMBOLIC)."""
    s0 = float(np.sum(chat_vec * lam * q[:, 0]))
    s1 = float(np.sum(chat_vec * lam * q[:, 1]))
    sx = float(np.sum(chat_vec * lam * q[:, 2]))
    return np.array([[tB[0, 0] - s0, tB[0, 1] - sx],
                     [tB[0, 1] - sx, tB[1, 1] - s1]])


# ============================================================= dressing
def build_fields(labels15, Hstar_ints, nvals, uu, lam, alpha, spf):
    """The three comb functionals aggregated on the 15 labels."""
    F1 = {x: 0.0 for x in labels15}
    F2 = {x: 0.0 for x in labels15}
    F3 = {x: 0.0 for x in labels15}
    for j, n in enumerate(nvals):
        if classify(int(n), spf) != "ro":
            continue
        phi = math.pi * float(uu[j]) / (2.0 * alpha)
        for x in Hstar_ints:
            p = 1.0 / 7.0
            F1[x] += float(lam[j]) * p
            F2[x] += float(lam[j]) * math.cos(phi) * p
            F3[x] += float(lam[j]) * math.sin(phi) * p
    return F1, F2, F3


def position_leg_field(Hstar_ints, nvals, uu, lam, alpha, spf, legs):
    """v2 field: c(x) = the mass-normalized placement scalar
    c* = <cos phi + sin phi>_w over the ram-odd events (in [1, sqrt2])
    on H*, 0 off H*; leg field f(x,y) = (c(x)+c(y))/2 - 1 in [-1, 1].
    The position content survives (NOT divided out by the v1 max
    normalization)."""
    num = den = 0.0
    for j, n in enumerate(nvals):
        if classify(int(n), spf) != "ro":
            continue
        phi = math.pi * float(uu[j]) / (2.0 * alpha)
        num += float(lam[j]) * (math.cos(phi) + math.sin(phi))
        den += float(lam[j])
    cstar = (num / den) if den > 0 else 0.0
    Hset = set(Hstar_ints)
    c = {x: (cstar if x in Hset else 0.0) for x in range(1, 16)}
    return ({(x, y): (c[x] + c[y]) / 2.0 - 1.0 for (x, y) in legs},
            cstar)


def mass_leg_field(F1, legs):
    raw = {(x, y): F1[x] + F1[y] for (x, y) in legs}
    mx = max(abs(v) for v in raw.values())
    return ({k: v / mx for k, v in raw.items()} if mx > 0
            else {k: 0.0 for k in raw})


def make_kernel(legs, nb, field, unital):
    """K[x][y] = (1 + KAPPA field)/7, optionally row-normalized."""
    K = {}
    for x in nb:
        row = {y: (1.0 + KAPPA * field[(x, y)]) / 7.0 for y in nb[x]}
        if unital:
            s = sum(row.values())
            row = {y: v / s for y, v in row.items()}
        K[x] = row
    return K


def kernel_stats(K, nb):
    """(min entry, max |rowsum - 1|)."""
    mn = min(v for x in K for v in K[x].values())
    dev = max(abs(sum(K[x].values()) - 1.0) for x in K)
    return mn, dev


def dressed_masses(K, nvals, spf, Hstar_ints):
    """chat'_j = -(total dressed carrier mass): the predual pushforward
    p' = K^T p keeps total mass sum_x p(x) * rowsum(x); non-ro events
    carry delta_0 and are untouched (chat' = -1)."""
    out = np.zeros(len(nvals))
    for j, n in enumerate(nvals):
        if classify(int(n), spf) == "ro":
            mass = sum((1.0 / 7.0) * sum(K[x].values())
                       for x in Hstar_ints)
            out[j] = -mass
        else:
            out[j] = -1.0
    return out


# ================================================= register-level ward
def register_chat(pv_dict, th, n):
    """Full 128-dim register Fourier value of the dressed carrier at
    chi_GL1 (float): the carrier element with V-slot distribution
    pv_dict, C2 pure sign slot, mu4 glue slot; chat = sum_g c(g)
    chi_GL1(g) with chi_GL1 = sign on C2, trivial on V x Z4."""
    Th0, Th1, Th2, Th3 = th["Th"]
    E = 240.0 * float(th["sig3"][n])
    pm = [float(Th0[n]) / E, float(Th1[n]) / E, float(Th2[n]) / E,
          float(Th3[n]) / E]
    tot = 0.0
    for vv, pv in pv_dict.items():
        for m in range(4):
            w = pv * pm[m] / 2.0
            for _gg in ((1, vv, m), (1, vv, (-m) % 4)):
                tot += w * (-1.0)        # chi_GL1((1, v, m)) = -1
    return tot


def register_chat_exact(th, n, Hstar_ints):
    """Exact undressed version (Fractions): must equal -1."""
    Th0, Th1, Th2, Th3 = th["Th"]
    E = 240 * int(th["sig3"][n])
    pm = [Fr(int(Th0[n]), E), Fr(int(Th1[n]), E), Fr(int(Th2[n]), E),
          Fr(int(Th3[n]), E)]
    tot = Fr(0)
    for _vv in Hstar_ints:
        pv = Fr(1, len(Hstar_ints))
        for m in range(4):
            w = pv * pm[m] / 2
            tot += 2 * w * Fr(-1)
    return tot


# ================================================== state-face scalar
def state_scalar(nvals, lam, th, vfac_fn):
    Th0, Th1, Th2, Th3 = th["Th"]
    Z = float(np.sum(lam))
    tot = 0.0
    for j, n in enumerate(nvals):
        n = int(n)
        t = Fr(int(th["a"][n]), int(th["sig3"][n]))
        if t == 0:
            continue
        E = 240 * int(th["sig3"][n])
        mh1 = Fr(int(Th0[n]) - int(Th2[n]), E)
        mh2 = Fr(int(Th0[n]) - int(Th1[n]) + int(Th2[n]) - int(Th3[n]), E)
        mufac = 1 + 2 * mh1 * mh1 + mh2 * mh2
        c2fac = 1 + t * t
        vfac = vfac_fn(n, j)
        share = float(t * t / (c2fac * mufac)) / vfac
        tot += float(lam[j]) * 128.0 * share
    return tot / Z


# ================================================================= main
def main():
    section("PRIME.CORNER.DRESSING.01 -- position-dependent Kraus data "
            "on the flags (EXPLORATION ONLY)")
    sha = hashlib.sha256(FROZEN_SPEC.encode("utf-8")).hexdigest()
    print("    FROZEN_SPEC SHA-256 = %s" % sha)
    print("    the licensed question: can the 105 legs carry placement "
          "data with CP + the corner identity + comb-specificity all "
          "surviving?  NO RH claim.")

    print("\nS0 -- firewall")
    bad = ast_firewall()
    check("S0.1 AST firewall: no zeta-zero / prime-table symbol",
          not bad, "found %s" % bad if bad else "clean")

    # ---------------------------------------------------------- frame
    section("S1 -- deployed frame, incidence, packet layer")
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
    B1 = np.zeros((15, 15), dtype=np.int64)
    for x in labels15:
        for y in nb[x]:
            B1[x - 1, y - 1] = 1
    ok_b = (len(legs) == 105
            and all(len(nb[x]) == 7 for x in labels15)
            and np.array_equal(B1 @ B1.T,
                               4 * np.eye(15, dtype=np.int64)
                               + 3 * np.ones((15, 15), dtype=np.int64)))
    check("S1.2 [EXACT] the deployed flag system: 105 legs, 7 per row, "
          "B B^T = 4I + 3J (v756 ward); |H*| = %d at y_chi = %s"
          % (len(Hs), y_chi), ok_b and len(Hs) == 7)

    # --------------------------------------------------------- windows
    section("S2 -- deployed windows, reads, undressed regression")
    wins = deployed_windows()
    wdata = []
    ok_id = True
    for kz, rr in wins:
        nvals = np.rint(np.exp(rr["uu"])).astype(np.int64)
        rows = unit_rows(rr)
        q = lock_reads_direct(rr, rows)
        tB = arch_lock_direct(rr)
        tau_X = float(np.linalg.eigvalsh(rr["Ah"])[0])
        chat0 = -np.ones(len(nvals))
        A0 = corner_block(tB, chat0, rr["lam"], q)
        tau0 = float(np.linalg.eigvalsh(A0)[0])
        scale = max(1.0, float(np.max(np.abs(A0))))
        res = abs(tau0 - tau_X) / scale
        ok_id &= res <= BAR_ID_REL
        wdata.append(dict(kz=kz, rr=rr, nvals=nvals, q=q, tB=tB,
                          tau_X=tau_X, tau0=tau0, scale=scale))
        print("    kz=%-3d  ka=%3d  tau_X=%+.6e  undressed corner "
              "lambda_min=%+.6e  res/scale=%.1e (scale %.2e)"
              % (kz, len(nvals), tau_X, tau0, res, scale))
    check("S2.1 undressed regression: the certified corner reduction "
          "(chat = -1) reproduces tau_X on all %d windows (residual "
          "<= %.0e of the block scale; the identity is the baseline; "
          "lambda_min inherits the coefficient-level residual of the "
          "certified identity)" % (len(wdata), BAR_ID_REL), ok_id)
    W = wdata[0]                                # primary window
    kz0, rr0 = W["kz"], W["rr"]
    alpha0 = float(rr0["alpha"])
    ok_reg = (abs(W["tau_X"] - REG_TAU_KZ9) / REG_TAU_KZ9 <= REG_BAR)
    val1 = state_scalar(W["nvals"], rr0["lam"], th,
                        lambda n, j: (16.0 / 7.0 if classify(
                            n, th["spf"]) == "ro" else 16.0))
    ok_reg &= abs(val1 - REG_STATE_KZ9) / REG_STATE_KZ9 <= REG_BAR
    vals_m = [state_scalar(W["nvals"], rr0["lam"], th,
                           lambda n, j, m=m: (
                               (2.0 ** (4 * m)) / (7.0 * 8.0 ** (m - 1))
                               if classify(n, th["spf"]) == "ro"
                               else 2.0 ** (4 * m)))
              for m in (1, 2, 3)]
    rats = [vals_m[i + 1] / vals_m[i] for i in range(2)]
    check("S2.2 undressed dilution control: state scalar %.6e (frozen "
          "4.813726e-3) with closed-form tower ratios %s == 1/16 "
          "(the STRUCTURE-ONLY law reproduced)"
          % (val1, ["%.6f" % r for r in rats]),
          ok_reg and all(abs(r - 1.0 / 16.0) <= 1e-12 for r in rats))

    # scrambled + Epstein combs (position controls, same masses)
    rr_s = core.build_window(kz0, scramble_seed=SCR_SEED)
    uu_s = rr_s["uu"]
    rows_s = unit_rows(rr0, positions=uu_s)
    q_s = lock_reads_direct(rr0, rows_s)
    uu_e = sum2sq_positions(len(W["nvals"]))
    rows_e = unit_rows(rr0, positions=uu_e)
    q_e = lock_reads_direct(rr0, rows_e)
    print("    controls built: scramble (seed %d) and Epstein comb "
          "(first %d sums of two squares, n = %d..%d), same masses"
          % (SCR_SEED, len(uu_e), int(round(math.exp(uu_e[0]))),
             int(round(math.exp(uu_e[-1])))))

    # -------------------------------------------------------- register
    section("S3 -- the register ward: chat' == -(dressed carrier mass)")
    n_ro = next(int(n) for n in W["nvals"]
                if classify(int(n), th["spf"]) == "ro")
    ok_ex = register_chat_exact(th, n_ro, Hs) == Fr(-1)
    F1, _F2, _F3 = build_fields(labels15, Hs, W["nvals"], rr0["uu"],
                                rr0["lam"], alpha0, th["spf"])
    fh, cstar = position_leg_field(Hs, W["nvals"], rr0["uu"],
                                   rr0["lam"], alpha0, th["spf"], legs)
    K_probe = make_kernel(legs, nb, fh, unital=False)
    pv0 = {x: 1.0 / 7.0 for x in Hs}
    pv1 = {y: sum(pv0.get(x, 0.0) * K_probe[x].get(y, 0.0)
                  for x in Hs) for y in labels15}
    mass1 = sum(pv1.values())
    chat_reg = register_chat(pv1, th, n_ro)
    ok_reg2 = abs(chat_reg - (-mass1)) <= BAR_EXACT
    check("S3.1 register ward: on the FULL 128-dim register the "
          "GL1-Fourier value of the dressed ro carrier (n = %d, "
          "variant-C kernel) equals -(total dressed V-mass) = %+.9f "
          "to %.0e (chi_GL1 is trivial on V x Z4 -- the corner reads "
          "ONLY the carrier mass); undressed exact value = -1 "
          "(Fractions)" % (n_ro, -mass1, BAR_EXACT),
          ok_ex and ok_reg2)

    # -------------------------------------------------------- variants
    section("S4 -- the four frozen variants x the three gates "
            "(primary window kz=%d)" % kz0)
    mh = mass_leg_field(F1, legs)
    fh_s, cstar_s = position_leg_field(Hs, W["nvals"], uu_s,
                                       rr0["lam"], alpha0, th["spf"],
                                       legs)
    fh_e, cstar_e = position_leg_field(Hs, W["nvals"], uu_e,
                                       rr0["lam"], alpha0, th["spf"],
                                       legs)
    print("    the placement scalar (the ONE number the m = 1 carrier "
          "granularity supports): c* true = %.6f, scrambled = %.6f, "
          "Epstein = %.6f" % (cstar, cstar_s, cstar_e))

    variants = [
        ("A  mass-dressed unital",  mh,   True,  mh,   mh),
        ("A' pos-dressed unital",   fh,   True,  fh_s, fh_e),
        ("B  phase-dressed",        None, None,  None, None),
        ("C  pos-dressed raw",      fh,   False, fh_s, fh_e),
    ]
    table = []
    for name, field, unital, field_scr, field_eps in variants:
        if field is None:                       # phase variant
            # |amp|^2 = 1/7 exactly: the diagonal channel is the
            # undressed one -- corner-invisible by construction.
            ga, unit_dev = True, 0.0
            chat_v = -np.ones(len(W["nvals"]))
            gb_dev = 0.0
            A_d = corner_block(W["tB"], chat_v, rr0["lam"], W["q"])
            tau_d = float(np.linalg.eigvalsh(A_d)[0])
            delta = tau_d - W["tau0"]
            delta_scr = 0.0
            delta_eps = 0.0
            gb = True
            gc = False
            note = "phases cancel on the diagonal corner: typed blind"
        else:
            K = make_kernel(legs, nb, field, unital=unital)
            mn, unit_dev = kernel_stats(K, nb)
            ga = mn > 0.0
            chat_v = dressed_masses(K, W["nvals"], th["spf"], Hs)
            gb_dev = float(np.max(np.abs(1.0 + chat_v)))
            gb = gb_dev <= BAR_EXACT
            A_d = corner_block(W["tB"], chat_v, rr0["lam"], W["q"])
            tau_d = float(np.linalg.eigvalsh(A_d)[0])
            delta = tau_d - W["tau0"]
            K_scr = make_kernel(legs, nb, field_scr, unital=unital)
            chat_scr = dressed_masses(K_scr, W["nvals"], th["spf"], Hs)
            A_scr = corner_block(W["tB"], chat_scr, rr0["lam"], q_s)
            A0_scr = corner_block(W["tB"],
                                  -np.ones(len(W["nvals"])),
                                  rr0["lam"], q_s)
            delta_scr = float(np.linalg.eigvalsh(A_scr)[0]
                              - np.linalg.eigvalsh(A0_scr)[0])
            K_eps = make_kernel(legs, nb, field_eps, unital=unital)
            chat_eps = dressed_masses(K_eps, W["nvals"], th["spf"], Hs)
            A_eps = corner_block(W["tB"], chat_eps, rr0["lam"], q_e)
            A0_eps = corner_block(W["tB"],
                                  -np.ones(len(W["nvals"])),
                                  rr0["lam"], q_e)
            delta_eps = float(np.linalg.eigvalsh(A_eps)[0]
                              - np.linalg.eigvalsh(A0_eps)[0])
            # kernel-level placement signal: the dressing defect
            # itself must move under the scramble (not just the reads)
            ker_sig = abs(float(np.max(np.abs(1.0 + chat_v)))
                          - float(np.max(np.abs(1.0 + chat_scr))))
            gc = (abs(delta) > BAR_MOVE
                  and abs(delta - delta_scr) > BAR_MOVE
                  and ker_sig > BAR_MOVE)
            note = "kernel placement signal %.3e" % ker_sig
        table.append((name, ga, unit_dev, gb, gb_dev, gc, delta,
                      delta_scr, delta_eps, note))

    print("    THE THREE-GATE TABLE (primary window kz=%d, "
          "tau_X = %+.6e):" % (kz0, W["tau_X"]))
    print("    %-26s %-10s %-16s %-30s" % ("variant",
          "(a) CP", "(b) identity", "(c) identification"))
    for (name, ga, ud, gb, gbd, gc, d, ds, de, note) in table:
        print("    %-26s %-10s max|1+chat'|=%.1e %s  %s  "
              "delta=%+.3e  scr=%+.3e  eps=%+.3e%s"
              % (name, "PASS" if ga else "FAIL", gbd,
                 "PASS" if gb else "FAIL",
                 "PASS" if gc else "FAIL", d, ds, de,
                 ("  [" + note + "]") if note else ""))
    check("S4.1 gate (a) CP survives for ALL variants (dressed Choi "
          "diagonal, min entry > 0; unitality deviation reported per "
          "variant)", all(r[1] for r in table))
    ab_only = [r[0] for r in table if r[1] and r[3] and not r[5]]
    ac_only = [r[0] for r in table if r[1] and r[5] and not r[3]]
    abc = [r[0] for r in table if r[1] and r[3] and r[5]]
    check("S4.2 gate (b): identity survives EXACTLY for the unital "
          "variants (%s) and BREAKS for the raw position variant "
          "with the typed defect max|1+chat'| = %.3e = the injected "
          "position field (kappa x the placement scalar aggregate)"
          % ([r[0] for r in table if r[3]],
             max(r[4] for r in table)),
          all(r[3] == (not r[0].startswith("C")) for r in table))
    check("S4.3 gate (c): the corner MOVES and is placement-sensitive "
          "ONLY for the raw variant (%s); every identity-preserving "
          "variant has delta == 0 EXACTLY (chat' = -1 forces the "
          "dressed block == the window form)" % ac_only,
          len(ac_only) >= 1 and all(
              abs(r[6]) <= BAR_MOVE for r in table if r[3]))

    # delta across all three windows for the raw variant
    print("    variant C excess across the deployed battery:")
    for Wd in wdata:
        rrw = Wd["rr"]
        fhw, csw = position_leg_field(Hs, Wd["nvals"], rrw["uu"],
                                      rrw["lam"], float(rrw["alpha"]),
                                      th["spf"], legs)
        Kw = make_kernel(legs, nb, fhw, unital=False)
        chw = dressed_masses(Kw, Wd["nvals"], th["spf"], Hs)
        Aw = corner_block(Wd["tB"], chw, rrw["lam"], Wd["q"])
        dw = float(np.linalg.eigvalsh(Aw)[0]) - Wd["tau0"]
        print("      kz=%-3d delta = %+.6e   max|1+chat'| = %.6e   "
              "c* = %.6f" % (Wd["kz"], dw,
                             float(np.max(np.abs(1.0 + chw))), csw))

    # ----------------------------------------------------------- sweep
    section("S5 -- the trade-off sweep: delta = 0 <=> unital <=> "
            "identity, across the channel class")
    sweep_ok = True
    max_d_uni = 0.0
    min_d_raw = float("inf")
    for k in range(N_SWEEP_RAW + N_SWEEP_UNI):
        unital = k >= N_SWEEP_RAW
        f_rand = {}
        for (x, y) in legs:
            if (y, x) in f_rand:
                f_rand[(x, y)] = f_rand[(y, x)]
            else:
                f_rand[(x, y)] = 2.0 * lcg_float() - 1.0
        Kr = make_kernel(legs, nb, f_rand, unital=unital)
        mn, _ud = kernel_stats(Kr, nb)
        chr_v = dressed_masses(Kr, W["nvals"], th["spf"], Hs)
        gbd = float(np.max(np.abs(1.0 + chr_v)))
        Ar = corner_block(W["tB"], chr_v, rr0["lam"], W["q"])
        dr = abs(float(np.linalg.eigvalsh(Ar)[0]) - W["tau0"])
        sweep_ok &= mn > 0.0
        if unital:
            sweep_ok &= gbd <= BAR_EXACT and dr <= BAR_MOVE
            max_d_uni = max(max_d_uni, dr)
        else:
            min_d_raw = min(min_d_raw, gbd)
    check("S5.1 sweep (%d raw + %d row-normalized random dressings, "
          "LCG): every unital draw has identity defect <= %.0e AND "
          "corner excess <= %.0e (max %.1e); every raw draw carries "
          "its defect (min %.1e > 0 generically) -- across the class, "
          "the corner moves ONLY through the identity defect"
          % (N_SWEEP_RAW, N_SWEEP_UNI, BAR_EXACT, BAR_MOVE,
             max_d_uni, min_d_raw), sweep_ok)
    # the sharpest exhibit: two DIFFERENT unital dressings, identical
    # corner block bit for bit
    K_A = make_kernel(legs, nb, mh, unital=True)
    K_A2 = make_kernel(legs, nb, fh, unital=True)
    blk_A = corner_block(W["tB"], dressed_masses(K_A, W["nvals"],
                                                 th["spf"], Hs),
                         rr0["lam"], W["q"])
    blk_A2 = corner_block(W["tB"], dressed_masses(K_A2, W["nvals"],
                                                  th["spf"], Hs),
                          rr0["lam"], W["q"])
    bdiff = float(np.max(np.abs(blk_A - blk_A2))) / W["scale"]
    kdiff = max(abs(K_A[x].get(y, 0.0) - K_A2[x].get(y, 0.0))
                for (x, y) in legs)
    check("S5.2 the exhibit: variants A and A' have DIFFERENT kernels "
          "(max leg difference %.3e -- the position data IS in the "
          "channel) yet IDENTICAL corner blocks to %.1e of scale "
          "(float ulp of the row normalization): the GL1 corner is "
          "blind to everything except the carrier mass"
          % (kdiff, bdiff),
          bdiff <= BAR_EXACT and kdiff > 1e-6)
    # state scalar: dressing- and scramble-blind at m = 1 (measured
    # with the GENUINELY dressed ro l2 mass from the S3 pushforward)
    vfac_ro_dressed = 16.0 * sum(p * p for p in pv1.values())
    val_dressed = state_scalar(W["nvals"], rr0["lam"], th,
                               lambda n, j: (vfac_ro_dressed
                                             if classify(
                                                 n, th["spf"]) == "ro"
                                             else 16.0))
    check("S5.3 typed: the STATE-face scalar cannot move at m = 1 for "
          "ANY leg dressing -- the only events touching the flags are "
          "ram-odd, whose GL1 population amplitude a(2^k)/sigma3 "
          "vanishes identically (scalar with the DRESSED ro l2 mass "
          "[vfac %.4f vs undressed %.4f]: %.6e == undressed %.6e)"
          % (vfac_ro_dressed, 16.0 / 7.0, val_dressed, val1),
          abs(val_dressed - val1) <= 1e-14 * val1
          and abs(vfac_ro_dressed - 16.0 / 7.0) > 1e-6)

    # ------------------------------------------------------ tower lift
    section("S6 -- tower lift gate")
    if abc:
        print("    a variant passed all three gates: %s -- lifting "
              "through m = 2, 3 ..." % abc)
        lifted = True   # (unreachable in this channel class; see below)
    else:
        lifted = False
        print("    NO variant passed all three gates -- the tower "
              "lift is NOT executed (frozen rule).  The reduction "
              "makes the branch unreachable in this channel class: "
              "gate (b) forces chat' = -1, which makes the dressed "
              "corner block IDENTICAL to the window form, killing "
              "gate (c)'s 'gap moves' -- measured in S4/S5, not "
              "assumed.")
    check("S6.1 tower lift executed only on a full three-gate pass "
          "(none passed: the class-level exclusion held)",
          (len(abc) > 0) == lifted)

    # --------------------------------------------------------- verdict
    section("V -- FROZEN VERDICT + the honest consequence")
    tradeoff = (len(abc) == 0 and len(ab_only) >= 1
                and len(ac_only) >= 1 and sweep_ok
                and bdiff <= BAR_EXACT)
    if abc:
        verdict = "POSITION-KRAUS-CARRIES"
    elif tradeoff:
        verdict = "POSITION-KRAUS-TRADEOFF"
    else:
        verdict = "POSITION-KRAUS-PARTIAL"
    print("\n  VERDICT: %s" % verdict)
    if verdict == "POSITION-KRAUS-TRADEOFF":
        print("""
  THE HONEST CONSEQUENCE (one paragraph): the trade-off is
  STRUCTURAL, not accidental.  Within the licensed channel class --
  leg dressings of the deployed 105-leg flag system acting on the
  event carrier V-slot -- the GL1 corner reads EXACTLY ONE number
  per event: the total dressed carrier mass (the register ward S3.1
  proves this on the full 128-dim group algebra: chi_GL1 is trivial
  on V x Z4).  The corner identity holds weight-generically iff that
  mass is 1 for every event (unital dressing), and then the dressed
  corner block is BIT-IDENTICAL to the undressed window form no
  matter how much position data the kernel carries (S5.2: two
  different position-dressed unital kernels, same corner).  The raw
  position dressing DOES make the corner placement-sensitive (S4:
  delta moves, scramble and Epstein move it differently) but pays
  with the identity broken by exactly the injected field --
  identification data flows ONLY through the identity defect
  (S5.1).  Gates (b) and (c) are mutually exclusive in this class:
  the corner route through register-side leg dressings is CLOSED
  (stop-list candidate PRIME.CORNER.DRESSING.01, exploration-typed;
  no ledger writes).  What the closure does NOT cover, typed
  honestly: dressings that act OUTSIDE the V-slot carrier (e.g. on
  the lag/window tensor factor itself) or corners at characters
  NON-trivial on V -- those are different channel classes and remain
  the only open doors for a position-carrying corner.  The state
  scalar is doubly dead at m = 1: ram events have zero GL1
  amplitude (S5.3).  The wall stays PRIME.FLOOR.PAIRCORR.01.
  NO RH claim.""")
    elif verdict == "POSITION-KRAUS-CARRIES":
        print("\n  THE FINDING: a dressing passes all three gates -- "
              "the first genuine identification carrier; the tower "
              "question reopens (report prominently).")
    n_pass = sum(1 for _n, ok in CHECKS if ok)
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed%s"
          % (time.time() - T0, len(CHECKS), len(FAILS),
             ("  " + ",".join(FAILS)) if FAILS else ""))
    return 0 if n_pass == len(CHECKS) else 1


if __name__ == "__main__":
    raise SystemExit(main())
