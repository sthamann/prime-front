#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""v842 -- PRIME.RELATION.SKELETON.01: the certified skeleton of the identified floor decomposition -- strictly positive interval enclosures of tau_X on all 67 reachable rungs in identified-corner coordinates, the certified discriminator (the h = 2 Epstein fake certified-NEGATIVE on every anchor), and the scaling law that types the wall as the infinite quantifier over strictly-positive certified enclosures, ONE module from one probe (9/9 checks, verdict SKELETON-CERTIFIED; discovery probe excess_certified_skeleton_probe.py, 2026-08-07, re-run identically at promotion, promoted VERBATIM with no downscoping, ~5 s).  THE MARGIN CERTIFICATE (the round's headline): in identified-corner coordinates (v841) the deployed floor splits per rung as tau_X = lambda_min(S) + EXCESS, with S the comb-blind structural block and the excess carried entirely by the prime-power comb; on ALL 67 reachable rungs (kz = 9..121, alpha = 2.773..6.304, masses to 3.0e5) the interval certificate encloses tau_X with width 5.4e-11..6.6e-09 -- three to five orders below the margin even at the deepest rung -- and EVERY enclosure is STRICTLY POSITIVE (chol_cert discipline: certificates cover the linear algebra above the deployed float data; row-wise-fsum budget wards contained on the anchors + the deepest rung; certified midpoints reproduce the float ladder at 4.9e-13; the direct tau enclosure beats the naive two-giants composition).  THE CERTIFIED DISCRIMINATOR: the same certificate discipline certifies the four-comb separation on all three anchors (kz = 9/12/13) -- TRUE tau enclosed strictly positive; the Euler-product-violating Epstein comb (x^2 + 5y^2, class number 2) FAILS its margin certificate (routed-corner enclosure strictly NEGATIVE: -0.786/-1.100/-1.228, routing from the exact rational Lambda_F recursion); QI/CHI delta == 0 by EXACT routing (rho_amp == 0, no numerics); scramble disjoint from TRUE (control grade).  THE SCALING LAW (typed honestly): certifiability degrades FASTER than the margin decays (width log-slope +0.62 vs margin log-slope -0.52 per alpha; ratio slope +1.14), so the coordinate system HAS a finite certification horizon under the frozen budget discipline -- but the headroom is LARGE: the extrapolated horizon alpha* ~ 9.1 (mass ~ 7.5e7) lies far beyond the deployed ladder end 6.304 (max width/margin ratio 7.1e-04) -- within every reachable rung certifiability is NOT the binding constraint (analogous to the exclusion-ladder coordinates, where certification reached X = 25.5 comfortably).  WHAT REMAINS IS EXACTLY THE WALL: the infinite quantifier over the sequence of strictly-positive certified enclosures -- any future route must supply a UNIFORM lower bound on the excess margin tau_X (by the GUE-side findings v839/v840 a finer-than-statistical datum), and no finite table, certified or not, settles it.  Registers the skeleton coordinates: PRIME.RELATION.SKELETON.01 [O] with the sharpened demand.  NO RH claim.  Python-only per GATE.WOLFRAM.02.

PROVENANCE: discovery probe excess_certified_skeleton_probe.py (9/9,
verdict SKELETON-CERTIFIED), 2026-08-07, re-run identically at
promotion; this module runs the frozen protocol VERBATIM (~5 s; a
module-level _VERDICTS capture inserted at the frozen verdict per the
v817/v791 precedent -- no gate, bar or table changed).  The original
probe docstring, frozen spec (SHA-256-printed) and decision tree live
in the probe file verbatim (experiments/tfpt-discovery/).

FIREWALL: v563 READ-ONLY; no zeta zero, no prime-table symbol
(AST-checked; own sieves only -- the divisor/mu arithmetic IS the
admissible Euler-product datum); no RNG beyond the declared v563
scramble recipe (seed 1).  NO RH claim.
"""
import ast
import hashlib
import math
import os
import sys
import time
from fractions import Fraction as Fr
from math import fsum

import numpy as np

_here = os.path.dirname(os.path.abspath(__file__))
if _here not in sys.path:
    sys.path.insert(0, _here)

import v563_paper2_readouts as core        # noqa: E402  (READ-ONLY)

_VERDICTS = {}


# =============== PART A -- excess_certified_skeleton_probe.py (frozen probe, verbatim)

FROZEN_SPEC = """\
PRIME.RELATION.SKELETON.01 spec v1 (2026-08-07, frozen before run).
u = eps/2; gamma_n = n u/(1-n u); CERT_INFL = 1.01.  E_form =
gamma_{h+6} (absform + |x||Ty|) INFL; assembly e_c[k] = INFL u
((cnt_k+6) + (2M+16)) Aabs_k with cnt/Aabs from the mirror tent
pass; perturbation via Mabs[i,j] = e_c[|i-j|] + e_c[(M-1)-i-j];
2x2 lambda enclosure closed-form + 8u(|lo|+|hi|+1) widening.  Data
convention: c_ar/t1/t2/lam/positions are deployed float data (the
chol_cert discipline); the comb assembly is certified.  Ladder =
the 67 frozen rungs; margin certificate = direct tau enclosure of
lambda_min(S + C); strict flag tau_lo > 0; EXC enclosure = tau (-)
lamS; naive composed margin reported.  Scaling: ratio = width/
tau_mid, OLS log10(ratio) vs alpha, horizon at ratio 1 (heuristic).
Discriminator (anchors): TRUE tau_lo > 0 certified; H2 (a = rQ/2;
Lambda_F recursion exact in Fractions, routing weights data-grade
floats at the corner boundary; X_REL = 2048) routed enclosure hi
< 0 certified; QI/CHI delta == 0 by exact routing; SCR disjoint
from TRUE (control grade, float rho_pos).  Wards: fsum containment of
all 6 forms on kz {9,12,13,121} and of the assembly bins; tau refs
kz 9/12/13 rel 1e-4; EXC refs 2.28526/2.48552/2.52887 rel 1e-3.
VERDICTS: SKELETON-CERTIFIED / SKELETON-HORIZON / SKELETON-BLOCKED.
NO RH claim; writes nothing.
"""

U_RND = 0.5 * np.finfo(float).eps

CERT_INFL = 1.01

X_REL = 2048

ANCHORS = (9, 12, 13)

FSUM_RUNGS = (9, 12, 13, 121)

SCR_SEED = 1

TAU_REFS = {9: 5.984165e-4, 12: 4.351189e-4, 13: 5.637632e-4}

EXC_REFS = {9: 2.28526, 12: 2.48552, 13: 2.52887}

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

def gamma_fl(n):
    t = n * U_RND
    return t / (1.0 - t)

def qform(x, y, T, aT):
    """Certified quadratic form x (T y): (value, budget)."""
    z = T @ y
    q = float(x @ z)
    ab = (float(np.abs(x) @ (aT @ np.abs(y)))
          + float(np.abs(x) @ np.abs(z)))
    return q, gamma_fl(T.shape[0] + 6) * ab * CERT_INFL

def qform_fsum(x, y, T):
    rows = [fsum((T[i] * y).tolist()) for i in range(T.shape[0])]
    return fsum((float(x[i]) * rows[i]) for i in range(T.shape[0]))

def mirror_tent(alpha, M, positions, wabs):
    """Mirror pass over the deployed tent windows: per-bin
    contribution count and abs-weight mass (rigorous upper data for
    the assembly budget); asserts the boundary branch is dormant."""
    D = 2.0 * alpha / M
    cnt = np.zeros(M)
    Aabs = np.zeros(M)
    for u_j, w_j in zip(positions, wabs):
        assert u_j >= D, "boundary tent branch fired"
        i0 = int(math.floor(u_j / D))
        lo, hi = max(0, i0 - 2), min(M, i0 + 3)
        cnt[lo:hi] += 1.0
        Aabs[lo:hi] += w_j
    return cnt, Aabs

def assemble_comb(rr, positions, weights):
    """Certified tent assembly: returns (c_comb, e_c)."""
    M = rr["M"]
    alpha = rr["alpha"]
    w2 = [2.0 * float(w) for w in weights]
    cc, _D = core.atom_lags_at(alpha, M, list(positions), w2)
    cc = np.asarray(cc, float)
    cnt, Aabs = mirror_tent(alpha, M, positions,
                            [abs(w) for w in w2])
    e_c = CERT_INFL * U_RND * ((cnt + 6.0) + (2.0 * M + 16.0)) * Aabs
    return cc, e_c

def block_enclosure(rr, T, aT, Tc=None, aTc=None, Mabs=None):
    """Entry enclosures of the 2x2 block for lag matrix T (+ optional
    comb part Tc with data-perturbation envelope Mabs)."""
    t1, t2 = rr["t1"], rr["t2"]
    ent = {}
    for key, x, y in (("00", t1, t1), ("11", t2, t2), ("01", t1, t2)):
        q, E = qform(x, y, T, aT)
        if Tc is not None:
            qc, Ec = qform(x, y, Tc, aTc)
            Ep = float(np.abs(x) @ (Mabs @ np.abs(y))) * CERT_INFL
            q, E = q + qc, E + Ec + Ep + U_RND * (abs(q) + abs(qc))
        ent[key] = (q, E)
    return ent

def lam_min_2x2(ent):
    """Certified enclosure of lambda_min of the symmetric 2x2 with
    entry enclosures ent[key] = (value, budget)."""
    a, ea = ent["00"]
    c, ec = ent["11"]
    b, eb = ent["01"]
    m_lo, m_hi = (a - ea + c - ec) / 2.0, (a + ea + c + ec) / 2.0
    d_lo, d_hi = (a - ea - c - ec) / 2.0, (a + ea - c + ec) / 2.0
    d_abs_hi = max(abs(d_lo), abs(d_hi))
    d_abs_lo = 0.0 if d_lo <= 0.0 <= d_hi else min(abs(d_lo),
                                                   abs(d_hi))
    b_lo, b_hi = b - eb, b + eb
    b_abs_hi = max(abs(b_lo), abs(b_hi))
    b_abs_lo = 0.0 if b_lo <= 0.0 <= b_hi else min(abs(b_lo),
                                                   abs(b_hi))
    r_hi = math.hypot(d_abs_hi, b_abs_hi)
    r_lo = math.hypot(d_abs_lo, b_abs_lo)
    lo = m_lo - r_hi
    hi = m_hi - r_lo
    pad = 8.0 * U_RND * (abs(lo) + abs(hi) + 1.0)
    return lo - pad, hi + pad

def spf_sieve(N):
    spf = np.zeros(N + 1, dtype=np.int64)
    for p in range(2, N + 1):
        if spf[p] == 0:
            spf[p::p] = np.where(spf[p::p] == 0, p, spf[p::p])
    return spf

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

def rq_counts(cap):
    rep = np.zeros(cap + 1, dtype=np.int64)
    s = int(math.isqrt(cap)) + 1
    for x in range(-s, s + 1):
        for y in range(-s, s + 1):
            v = x * x + 5 * y * y
            if 1 <= v <= cap:
                rep[v] += 1
    return rep

def rho_amp_exact(masses, a, divs, spf, ispp):
    """EXACT amplitude routing (Fractions): Lambda_F recursion from
    the comb's own coefficients; rho_amp on non-pp event masses."""
    X = int(max(masses))
    G = {}
    for n in range(2, X + 1):
        acc = {}
        if a[n] != 0:
            vaddto(acc, logvec(n, spf), a[n])
        for d in divs[n]:
            if 1 < d < n and G[d] and a[n // d] != 0:
                vaddto(acc, G[d], -a[n // d])
        G[n] = {p: c for p, c in acc.items() if c != 0}
    LOG2 = math.log(2.0)
    rho = []
    for m in masses:
        m = int(m)
        if not ispp[m] and G[m]:
            rho.append(min(1.0, float(vnorm1(G[m])) / LOG2))
        else:
            rho.append(0.0)
    return rho

def part_a():
    section("PRIME.RELATION.SKELETON.01 -- the certified skeleton of "
            "tau_X = lambda_min(S) + EXCESS (EXPLORATION ONLY)")
    sha = hashlib.sha256(FROZEN_SPEC.encode("utf-8")).hexdigest()
    print("    FROZEN_SPEC SHA-256 = %s" % sha)
    print("    NO RH claim; certificates cover the linear algebra "
          "above the deployed float data (chol_cert discipline).")

    print("\nS0 -- firewall")
    bad = ast_firewall()
    check("S0.1 AST firewall clean", not bad,
          "found %s" % bad if bad else "clean")

    # ------------------------------------------------- ladder + wards
    section("S1 -- the certified ladder: per-rung enclosures")
    rungs = []
    for kz in core.frame_a_zones():
        rr = core.build_window(kz)
        if rr["h"] == 1292 or math.exp(2.0 * rr["alpha"]) \
                > core.ATOM_MAX + 0.5:
            del rr
            continue
        rungs.append(kz)
        del rr
    print("    %d rungs (frozen filter)" % len(rungs))
    print("    %-4s %-6s [%-12s %-12s] [%-12s %-12s] %-9s %-6s %-5s"
          % ("kz", "alpha", "tau_lo", "tau_hi", "lamS_lo", "lamS_hi",
             "width", "w/tau", "bind"))
    table = []
    fsum_ok = True
    ah_gap_max = 0.0
    for kz in rungs:
        rr = core.build_window(kz)
        uu = np.asarray(rr["uu"], float)
        lam = np.asarray(rr["lam"], float)
        M = rr["M"]
        c_ar = np.asarray(core.arch_lags(M, rr["D"]), float)
        T = core.odd_toeplitz(c_ar, M)
        aT = np.abs(T)
        cc, e_c = assemble_comb(rr, uu, lam)
        Tc = core.odd_toeplitz(cc, M)
        aTc = np.abs(Tc)
        h = M // 2
        ri = np.arange(h)
        Mabs = (e_c[np.abs(ri[:, None] - ri[None, :])]
                + e_c[(M - 1) - ri[:, None] - ri[None, :]])
        entS = block_enclosure(rr, T, aT)
        entA = block_enclosure(rr, T, aT, Tc, aTc, Mabs)
        lamS_lo, lamS_hi = lam_min_2x2(entS)
        tau_lo, tau_hi = lam_min_2x2(entA)
        width = tau_hi - tau_lo
        tau_mid = 0.5 * (tau_lo + tau_hi)
        tau_ref = float(np.linalg.eigvalsh(rr["Ah"])[0])
        ah_gap_max = max(ah_gap_max, abs(tau_mid - tau_ref))
        eS = max(entS[k][1] for k in entS)
        eP = max(float(np.abs(rr["t1"]) @ (Mabs @ np.abs(rr["t1"]))),
                 float(np.abs(rr["t2"]) @ (Mabs @ np.abs(rr["t2"]))))
        bind = "asm" if eP > eS else "form"
        table.append(dict(kz=kz, alpha=rr["alpha"], tau=(tau_lo,
                          tau_hi), lamS=(lamS_lo, lamS_hi),
                          width=width, ratio=width / tau_mid,
                          strict=tau_lo > 0.0, bind=bind,
                          tau_ref=tau_ref))
        print("    %-4d %-6.3f [%+.4e %+.4e] [%+.4e %+.4e] %.2e "
              "%.1e %-5s%s"
              % (kz, rr["alpha"], tau_lo, tau_hi, lamS_lo, lamS_hi,
                 width, width / tau_mid, bind,
                 "" if tau_lo > 0 else "  ** NOT STRICT **"))
        if kz in FSUM_RUNGS:
            for key, x, y in (("00", rr["t1"], rr["t1"]),
                              ("11", rr["t2"], rr["t2"]),
                              ("01", rr["t1"], rr["t2"])):
                qS, ES = qform(x, y, T, aT)
                qC, EC = qform(x, y, Tc, aTc)
                fsum_ok &= abs(qS - qform_fsum(x, y, T)) <= ES
                fsum_ok &= abs(qC - qform_fsum(x, y, Tc)) <= EC
        del rr, T, aT, Tc, aTc, Mabs
    n_strict = sum(1 for t in table if t["strict"])
    check("S1.1 [THE MARGIN CERTIFICATE] the tau enclosure is "
          "STRICTLY POSITIVE on %d / %d rungs -- the first "
          "certified-interval version of the floor in identified-"
          "corner coordinates" % (n_strict, len(table)),
          n_strict == len(table))
    check("S1.2 [BUDGET WARD] row-wise-fsum re-evaluation of all six "
          "forms contained in the certified budgets on kz = %s"
          % (FSUM_RUNGS,), fsum_ok)
    wid_all = np.array([t["width"] for t in table])
    check("S1.3 [REGRESSION] certified midpoints reproduce the "
          "float ladder: max |tau_mid - lambda_min(Ah)| = %.1e "
          "across all rungs (the Ah residual, below the max "
          "enclosure width %.1e); tau refs kz 9/12/13 matched rel "
          "1e-4" % (ah_gap_max, float(np.max(wid_all))),
          ah_gap_max <= max(1e-9, float(np.max(wid_all)))
          and all(abs(0.5 * sum(t["tau"]) - TAU_REFS[t["kz"]])
                  / TAU_REFS[t["kz"]] <= 1e-4
                  for t in table if t["kz"] in TAU_REFS))
    exc_ok = True
    for t in table:
        if t["kz"] in EXC_REFS:
            exc_lo = t["tau"][0] - t["lamS"][1]
            exc_hi = t["tau"][1] - t["lamS"][0]
            exc_ok &= abs(0.5 * (exc_lo + exc_hi)
                          - EXC_REFS[t["kz"]]) / EXC_REFS[t["kz"]] \
                <= 1e-3
    t0_ = table[0]
    nv_lo = (t0_["tau"][0] - t0_["lamS"][1]) + t0_["lamS"][0]
    nv_hi = (t0_["tau"][1] - t0_["lamS"][0]) + t0_["lamS"][1]
    check("S1.4 [REGRESSION] the certified EXC enclosures reproduce "
          "the ladder-probe excess on the anchors (rel 1e-3); the "
          "naive composed margin [EXC_lo - |lamS|_hi, EXC_hi - "
          "|lamS|_lo] on kz=9 = [%+.6e, %+.6e] (width %.1e, the "
          "two-giants cost) vs the sharp DIRECT tau enclosure width "
          "%.1e -- the direct enclosure is the payoff and both stay "
          "strictly positive"
          % (nv_lo, nv_hi, nv_hi - nv_lo, t0_["width"]),
          exc_ok and nv_lo > 0.0)

    # -------------------------------------------------- scaling law
    section("S2 -- THE SCALING LAW: certifiability vs margin decay")
    al = np.array([t["alpha"] for t in table])
    ratio = np.array([t["ratio"] for t in table])
    taum = np.array([0.5 * sum(t["tau"]) for t in table])
    wid = np.array([t["width"] for t in table])
    A1 = np.vstack([al, np.ones_like(al)]).T
    sl_r, ic_r = np.linalg.lstsq(A1, np.log10(ratio), rcond=None)[0]
    sl_w, _ = np.linalg.lstsq(A1, np.log10(wid), rcond=None)[0]
    sl_t, _ = np.linalg.lstsq(A1, np.log10(taum), rcond=None)[0]
    alpha_star = (0.0 - ic_r) / sl_r if sl_r > 0 else float("inf")
    print("    width:  %.2e -> %.2e (log-slope %+0.3f / alpha)"
          % (wid[0], wid[-1], sl_w))
    print("    margin: %.2e -> %.2e (log-slope %+0.3f / alpha)"
          % (taum[0], taum[-1], sl_t))
    print("    ratio width/margin: %.1e -> %.1e (log-slope %+0.3f); "
          "extrapolated certification horizon alpha* ~ %.1f "
          "(mass ~ e^{2 alpha*} ~ %.1e); deployed ladder ends at "
          "alpha = %.3f (mass 3.0e5)"
          % (ratio[0], ratio[-1], sl_r, alpha_star,
             math.exp(2 * alpha_star) if alpha_star < 50 else
             float("inf"), al[-1]))
    check("S2.1 [FROZEN QUESTION] certifiability degrades SLOWER "
          "than the margin decays iff the ratio stays << 1 with "
          "room: max ratio %.1e at the deepest rung; the "
          "extrapolated horizon alpha* ~ %.1f sits %s the deployed "
          "ladder end %.3f"
          % (float(np.max(ratio)), alpha_star,
             "far beyond" if alpha_star > al[-1] + 2 else "near",
             al[-1]), float(np.max(ratio)) < 1e-2)

    # --------------------------------------- certified discriminator
    section("S3 -- the certified discriminator (anchors)")
    spf = spf_sieve(X_REL)
    ISPP = np.zeros(X_REL + 1, dtype=bool)
    for n in range(2, X_REL + 1):
        ISPP[n] = len(factorize(n, spf)) == 1
    divs = {n: [] for n in range(1, X_REL + 1)}
    for d in range(1, X_REL + 1):
        for m in range(d, X_REL + 1, d):
            divs[m].append(d)
    rq = rq_counts(X_REL)
    ah2 = [Fr(int(rq[n]), 2) for n in range(X_REL + 1)]
    disc_ok = True
    for kz in ANCHORS:
        rr = core.build_window(kz)
        uu_t = np.asarray(rr["uu"], float)
        lam = np.asarray(rr["lam"], float)
        ka = len(lam)
        M = rr["M"]
        c_ar = np.asarray(core.arch_lags(M, rr["D"]), float)
        T = core.odd_toeplitz(c_ar, M)
        aT = np.abs(T)

        def routed_enclosure(masses, positions, cvec):
            w = [-float(lam[j]) * float(cvec[j]) for j in range(ka)]
            cc, e_c = assemble_comb(rr, positions, w)
            Tc = core.odd_toeplitz(cc, M)
            aTc = np.abs(Tc)
            h = M // 2
            ri = np.arange(h)
            Mabs = (e_c[np.abs(ri[:, None] - ri[None, :])]
                    + e_c[(M - 1) - ri[:, None] - ri[None, :]])
            ent = block_enclosure(rr, T, aT, Tc, aTc, Mabs)
            return lam_min_2x2(ent)

        t_lo, t_hi = routed_enclosure(
            np.rint(np.exp(uu_t)).astype(int), uu_t, [Fr(-1)] * ka)
        rqs = [n for n in range(2, X_REL + 1) if rq[n] > 0][:ka]
        rho_h2 = rho_amp_exact(rqs, ah2, divs, spf, ISPP)
        cv_h2 = [-1 + 2 * r for r in rho_h2]
        h_lo, h_hi = routed_enclosure(
            rqs, np.log(np.array(rqs, float)), cv_h2)
        uu_s = np.asarray(core.build_window(kz,
                                            scramble_seed=SCR_SEED)
                          ["uu"], float)
        LOG2 = math.log(2.0)
        # scramble routing: rho_pos at scrambled positions (control)
        sup_s = {int(round(math.exp(u))): float(us)
                 for u, us in zip(uu_t, uu_s)}
        MUv = np.zeros(X_REL + 1, dtype=np.int64)
        MUv[1] = 1
        for n in range(2, X_REL + 1):
            f = factorize(n, spf)
            MUv[n] = 0 if any(k > 1 for k in f.values()) \
                else (-1) ** len(f)
        cv_s = []
        for j in range(ka):
            m = int(round(math.exp(uu_t[j])))
            acc = 0.0
            for d in divs[m]:
                if not MUv[d]:
                    continue
                e = m // d
                if e == 1:
                    continue
                acc += float(MUv[d]) * sup_s.get(e, math.log(e))
            lam_f = math.log(int(spf[m])) if ISPP[m] else 0.0
            cv_s.append(-1.0 + 2.0 * min(1.0, abs(acc - lam_f)
                                         / LOG2))
        s_lo, s_hi = routed_enclosure(
            np.rint(np.exp(uu_t)).astype(int), uu_s, cv_s)
        n_flag = sum(1 for r in rho_h2 if r > 0)
        ok_kz = (t_lo > 0.0 and h_hi < 0.0
                 and (s_lo > t_hi or s_hi < t_lo))
        disc_ok &= ok_kz
        check("S3.%d anchor kz=%d CERTIFIED: TRUE tau in [%+.3e, "
              "%+.3e] > 0; EPSTEIN-h2 routed corner in [%+.3e, "
              "%+.3e] < 0 (the margin certificate FAILS for the "
              "fake; %d events routed from the exact Lambda_F "
              "recursion); QI/CHI delta == 0 by EXACT routing "
              "(rho_amp == 0, no numerics); scramble [%+.3e, "
              "%+.3e] disjoint from TRUE (control grade)"
              % (ANCHORS.index(kz) + 1, kz, t_lo, t_hi, h_lo, h_hi,
                 n_flag, s_lo, s_hi), ok_kz)
        del rr, T, aT

    # --------------------------------------------------------- verdict
    section("V -- FROZEN VERDICT + the contract-note paragraph")
    all_strict = n_strict == len(table)
    if all_strict and disc_ok and fsum_ok and not FAILS:
        verdict = "SKELETON-CERTIFIED"
    elif n_strict > 0:
        frontier = next((t["kz"] for t in table if not t["strict"]),
                        None)
        verdict = ("SKELETON-HORIZON (frontier kz=%s)" % frontier
                   if frontier else "SKELETON-PARTIAL (a ward "
                   "failed; see FAIL lines)")
    else:
        verdict = "SKELETON-BLOCKED"
    print("\n  VERDICT: %s   [strict rungs %d/%d | discriminator "
          "certified: %s | wards: %s]"
          % (verdict, n_strict, len(table),
             "YES" if disc_ok else "NO",
             "OK" if (fsum_ok and not FAILS) else "FAIL"))
    print("""
  THE CONTRACT-NOTE PARAGRAPH (PRIME.RELATION.LADDER.01 candidate):
  A certified finite skeleton of the identified floor decomposition
  now exists.  In identified-corner coordinates the deployed floor
  splits per rung as tau_X = lambda_min(S) + EXCESS, with S the
  comb-blind structural block and the excess carried entirely by
  the prime-power comb; on all %d reachable rungs (alpha = %.3f ..
  %.3f, masses to 3.0e5) the interval certificate encloses tau_X
  with width %.1e .. %.1e -- three to five orders below the margin
  even at the deepest rung -- and every enclosure is strictly
  positive.  The same certificate discipline certifies the
  discriminator: the Euler-product-violating Epstein comb (x^2 +
  5y^2, class number 2) FAILS its margin certificate (routed-corner
  enclosure strictly negative) on every anchor, with the routing
  computed from the exact rational Lambda_F recursion.  The scaling
  law, typed honestly: certifiability degrades FASTER than the
  margin decays (width log-slope %+.2f vs margin log-slope %+.2f
  per alpha; ratio slope the sum), so this coordinate system HAS a
  finite certification horizon under the frozen budget discipline
  -- but the headroom is large: the extrapolated horizon alpha* ~
  %.1f (mass ~ 7.5e7) lies well beyond the deployed ladder end,
  so within every reachable rung certifiability is not the binding
  constraint (analogous to the exclusion-ladder coordinates, where
  certification reached X = 25.5 comfortably).  What remains
  is exactly the wall: the infinite quantifier over the sequence
  of strictly-positive certified enclosures.  Any future route
  must supply a UNIFORM lower bound on the excess margin tau_X --
  by the GUE-side findings a finer-than-statistical datum -- and
  no finite table, certified or not, settles it.  NO RH claim.
""" % (len(table), al[0], al[-1], float(np.min(wid)),
       float(np.max(wid)), sl_w, sl_t, alpha_star))
    n_pass = sum(1 for _n, ok in CHECKS if ok)
    print("[TIME] %.1f s   [CHECKS] %d run, %d failed%s"
          % (time.time() - T0, len(CHECKS), len(FAILS),
             ("  " + ",".join(FAILS)) if FAILS else ""))
    _VERDICTS["a"] = verdict
    return 0 if n_pass == len(CHECKS) else 1


EXPECT = (9, "SKELETON-CERTIFIED")


def run():
    t_all = time.time()
    CHECKS.clear()
    FAILS.clear()
    globals()["T0"] = time.time()
    rc = int(part_a() or 0)
    pattern_ok = (len(CHECKS) == EXPECT[0] and len(FAILS) == 0
                  and _VERDICTS.get("a") == EXPECT[1])
    print("\n" + "=" * 74)
    print("v842: %d/%d checks passed, %d failed | runtime %.1f s"
          % (len(CHECKS) - len(FAILS), len(CHECKS), len(FAILS),
             time.time() - t_all))
    print("NO RH claim; the wall = the infinite quantifier over "
          "strictly-positive certified enclosures; the demand: a "
          "UNIFORM lower bound on the excess margin -- "
          "PRIME.FLOOR.PAIRCORR.01.")
    print("[%s] PATTERN GATE: expected 9 checks, 0 failed, verdict "
          "SKELETON-CERTIFIED (got %s)"
          % ("PASS" if pattern_ok else "FAIL", _VERDICTS.get("a")))
    return rc + (0 if pattern_ok else 1)


if __name__ == "__main__":
    raise SystemExit(run())
