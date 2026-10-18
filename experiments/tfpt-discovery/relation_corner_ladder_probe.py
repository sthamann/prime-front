#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""relation_corner_ladder_probe -- PRIME.RELATION.LADDER.01
(EXPLORATION ONLY, experiments/; follow-up to RELATION-CARRIER-EXISTS:
close the two typed limits, then run the identified corner along the
deployed ladder, 2026-08-07).

STAGE 1 -- AMPLITUDE-GRADE CORNER WIRING (the first typed limit):
the comb datum now CARRIES COEFFICIENTS: a config is (masses m_j,
positions u_j, coefficient function a on [1, X_c], a(1) = 1).  The
routing scalar becomes
    rho_j = min(1, rho_amp(j) + rho_pos(j)),
    rho_amp(j) = min(1, ||Lambda_F(m_j)||_1 / log 2)  if m_j is NOT
                 a prime power, else 0,
where Lambda_F is the EXACT log-derivative reconstruction from the
comb's OWN coefficients (a(n) log n = sum_{d|n} Lambda_F(d) a(n/d),
Fractions on the log-p basis).  rho_pos is the position-relational
mu*log defect (unchanged; already L-safe).  The support-grade
closure reading of the previous probe is RETIRED.  The exact corner-
carried reading R_corner = sum_j ||Lambda_F(m_j)||_1 [m_j not pp]
(Fraction) plus its coverage of the total off-pp defect.

STAGE 2 -- L-FUNCTION SAFETY: the old closure defect flagged
zeta_{Q(i)}-type supports (9 present, 3 absent -- inert primes at
even powers).  rho_amp cannot: a genuine Euler product has Lambda_F
supported on prime powers REGARDLESS of its support gaps, so the
amplitude wiring fixes L-safety automatically -- measured by the
redone four-comb table THROUGH THE CORNER on the anchor rungs:
TRUE (a = 1)              -> R_corner = 0 exact, delta = 0;
s2s / zeta_Q(i) (a = r2/4) -> R_corner = 0 exact, delta = 0
                             (Selberg-correct blindness; the old
                             support-grade flag is typed SUPERSEDED);
EPSTEIN x^2+5y^2 (a = rQ/2, h = 2) -> R_corner > 0 exact, delta != 0
                             (separated PURELY by the Euler-product
                             datum -- this null is also self-
                             consistent, rho_pos ~ 0);
chi4 L-FAKE (true masses, a = chi4) -> R_corner = 0 exact, delta = 0;
SCRAMBLE (a = 1, positions scrambled) -> delta != 0 via rho_pos
                             (different fingerprint).

STAGE 3 -- THE LADDER RUN (the sharpened PRIME.FLOOR.PAIRCORR.01):
tier A = ALL deployed frame-A rungs passing the deployed filter
(exp(2 alpha) <= ATOM_MAX + 0.5 and h != 1292): 67 rungs, kz = 9 ..
121, masses up to 3.0e5 (predeclared from the measured inventory:
window builds <= 0.1 s each; per-event reads Xn and the arch block B
ship with the window, so tier A is afforded WITHOUT per-event
Toeplitz rebuilds).  Per rung: (a) IDENTITY ward: lambda_min(B -
sum_j lam_j Xn_j) == tau_X = lambda_min(Ah) (the corner reduction,
rel 1e-6; Xn == -q3 cross-checked against an independent reads_pair
on the primary rung); (b) THE EXCESS (frozen definition):
    EXC(rung) = tau_X - lambda_min(S),   S = the comb-blind
    structural block (the arch-only 2x2, rr['B']),
i.e. the difference between the identified corner's value at the
true comb and the pure-structural corner value -- the comb events'
contribution to the floor in corner coordinates; its sign, size and
trend along the ladder are THE measurement; (c) wards per rung:
support == all prime powers in range (divisor-closed by
arithmetic), max |u_j - log m_j| == 0, rho(true) == 0 => the
carrier at truth IS the deployed carrier (state property inherited
structurally; re-measured explicitly on the anchor rungs).
Tier B (anchors kz = 9, 12, 13): the full four-comb amplitude-wired
corner + scramble-excess control (EXC_scr must differ from EXC).

THE DECISION (frozen): with tol = 1e-12 + 1e-9 max(|tau_X|,
|lambda_min(S)|) per rung: EXCESS-NONNEGATIVE iff EXC >= -tol on
ALL tier-A rungs (margin trend reported); EXCESS-VANISHES iff
|EXC| <= tol on all rungs; otherwise EXCESS-CHANGES-SIGN /
NEGATIVE with the exact sign census typed (uniform negativity is
reported under this branch with its own typing -- positivity NOT
automatic, the hardness located inside the new construction).

CONTROLS: GL1 anchor (exact, anchor-union events); tau_X frozen
refs on kz = 9/12/13; the mu*log and Moebius-inversion wards exact
to X_ANCHOR; Xn == -q3 ward; state wards per anchor config; exact
Fractions in the relational layer, float corner numerics with bars
typed.  HONESTY: NO RH claim; nothing outside experiments/; no
file written; the excess is a corner-coordinate measurement at
deployed scale, not an asymptotic statement.

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/relation_corner_ladder_probe.py
"""

import ast
import hashlib
import math
import os
import sys
import time
from fractions import Fraction as Fr

import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
_VERIFY = os.path.abspath(os.path.join(_HERE, "..", "..",
                                       "verification"))
sys.path.insert(0, _HERE)
sys.path.insert(0, _VERIFY)

import v563_paper2_readouts as core        # noqa: E402  (READ-ONLY)

FROZEN_SPEC = """\
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
mu*log + Moebius inversion exact to 2048.  N_TH = 2048.  LCG
20260807.  NO RH claim; writes nothing.
"""

N_TH = 2048
X_ANCHOR = 2048
ANCHORS = (9, 12, 13)
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
    sig3 = np.zeros(N_TH + 1, dtype=object)
    for d in range(1, N_TH + 1):
        for m in range(d, N_TH + 1, d):
            sig3[m] = (sig3[m] or 0) + d ** 3
    SCAP = 2 * N_TH
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
    Th0 = ((p3 + m53 + m35 + p4) // 4)[::2][:N_TH + 1].copy()
    Th2 = ((p3 - m53 - m35 + p4) // 4)[::2][:N_TH + 1].copy()
    TCAP = 8 * N_TH
    t2 = sparse_theta_terms("th2", TCAP)
    acc = np.zeros(TCAP + 1, dtype=object)
    acc[0] = 1
    for _ in range(8):
        acc = sparse_mul(acc, t2)
    Th1 = (acc[::8][:N_TH + 1] // 4).copy()
    spf = np.zeros(N_TH + 1, dtype=np.int64)
    for p in range(2, N_TH + 1):
        if spf[p] == 0:
            spf[p::p] = np.where(spf[p::p] == 0, p, spf[p::p])
    glue_ok = all(int(Th0[n] + 2 * Th1[n] + Th2[n])
                  == 240 * int(sig3[n]) for n in range(1, N_TH + 1))
    heads_ok = (int(Th0[1]), int(Th1[1]), int(Th2[1])) == (52, 64, 60)
    return dict(sig3=sig3, Th=(Th0, Th1, Th2, Th1), spf=spf,
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


# ================================================= v738 label frame
def label_frame():
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


# =============================================== the relational layer
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


# ================================================================= main
def main():
    section("PRIME.RELATION.LADDER.01 -- amplitude wiring + the "
            "identified corner along the ladder (EXPLORATION ONLY)")
    sha = hashlib.sha256(FROZEN_SPEC.encode("utf-8")).hexdigest()
    print("    FROZEN_SPEC SHA-256 = %s" % sha)
    print("    NO RH claim; the excess is a deployed-scale corner "
          "measurement, not an asymptotic statement.")

    print("\nS0 -- firewall")
    bad = ast_firewall()
    check("S0.1 AST firewall: no zeta-zero / prime-table symbol "
          "(divisor/mu arithmetic admissible)", not bad,
          "found %s" % bad if bad else "clean")

    # ---------------------------------------------------------- layer
    section("S1 -- packet layer, frame, anchors, Xn cross-ward")
    th = theta_layer()
    spf = th["spf"]
    check("S1.1 [EXACT] packet layer to n <= %d: glue identity "
          "Th0 + 2 Th1 + Th2 = 240 sigma3 + heads" % N_TH, th["ok"])
    Hs = label_frame()
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
    return 0 if n_pass == len(CHECKS) else 1


if __name__ == "__main__":
    raise SystemExit(main())
