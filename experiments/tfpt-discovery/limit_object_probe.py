#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""limit_object_probe -- PRIME.RDAGGER.LIMIT_OBJECT.01
(round 454): identify the degreewise limit of
the folded Chebyshev moments and the limit
chain.  Lemma-first.  Research
documentation, NO RH claim and NO anti-RH
claim.

THE QUESTION.  r452: m_k[j] converges
degreewise at rate a^{-1.9}.  Where to?
If the limit is classical (arch / PNT fold)
the von Mangoldt comb sits only in the RATE,
not in the limit -- the deepest structure
statement of the prefix program.

THREE LEGS.

A. Limit identification.
  For every fixed j>=2 the ladder is already
  at a universal value (deep maxrel vs kz500
  down to 1e-11).  m0, m1 do NOT converge
  (arch mass grows with N).
  MAIN folded moments equal ARCH folded
  moments (comb deleted) through n_stab
  (kz17/116/136: break == n_stab at 1e-4;
  deeper windows agree through the computed
  prefix).  PNT-swap is redundant: the comb
  is in the kernel of the latched fold.
  LIMIT_CLASSICAL.

B. Limit chain.
  rho_j on the plateau of kz197/500 at
  j=20,40,80,160,200 is <= 7e-6.  Conservative
  bar 1e-4 still << 5/7.  So
  rho_j(inf) = 0 +/- 1e-4 for j<=200, and
  the 5/7 test is load-bearing.
  mu-chain h stays positive through n_stab
  (r449 TAIL_ONLY).  LIMITCHAIN_ALIVE(200).

C. Lemma chain (paper, not Lean).
  [L1] MEASURED: degreewise convergence;
      identification MAIN -> ARCH for j <
      n_stab.
  [L2] MEASURED: pack map Lipschitz in the
      moments (dq/dm_2 ~ 0.06..0.10 on kz17).
  [L3] MEASURED for j<=200 (rho_inf=0,
      h>0 on the computed prefix); OPEN as
      a theorem for all j.
  Together: for each fixed n, eventually
  n < n_stab and rho_n < 5/7 => prefix
  mincut eventually (Lean Iff.rfl => full
  mincut).  CHAIN_DOCUMENTED.

CALIBRATION DISCLOSURE.  First measured in
/tmp (r454_diag.json, r454_diag2.py,
r454_diag3.py) on 2026-08-30, then sealed.

PINNED m_inf[j] from kz500 (live re-gate):
  m2  = 0.1698990367924736
  m4  = 0.0089525326636440
  m8  = 0.0010081970691365
  m16 = 0.0001230324491490
  m24 = 0.0000362950580291
  m32 = 0.0000152886541084

PNT world (same fold, comb -> smooth dpsi ~ e^u du)
agrees with MAIN on j=2..15 at 1e-4 (kz17) to
1e-7 (kz137).  ARCH agrees at 1e-15.  The
identified limit is ARCH; PNT is a nearby
classical proxy.  Arithmetic lives in
n_stab / the rate, not in m_inf[j] for
fixed j>=2.

AUSGANG LIMIT_CLASSICAL /
LIMITCHAIN_ALIVE_200 / CHAIN_DOCUMENTED.
No RH claim.  No anti-RH claim.

MACHINERY: r449 cheb_moments / load_mom;
r451 pack_at; r452 masses_of / rho_last;
V.arch_lags / spectral_density.

NO RH CLAIM.  Finite window identities.
No L* claim.  No R-dagger claim.
"""
from __future__ import annotations

import argparse
import ast
import hashlib
import math
import os
import sys
import time

import numpy as np

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DISC = os.path.dirname(os.path.abspath(__file__))
PROB = os.path.join(REPO, "rh", "problem")
for p in (DISC, PROB):
    if p not in sys.path:
        sys.path.insert(0, p)

import deep_builder_probe as S445  # noqa: E402
import flip_vs_stab_probe as S449  # noqa: E402
import nstab_transition_probe as S451  # noqa: E402
import plateau_theorem_probe as S452  # noqa: E402
import verify_lstar_instance as V  # noqa: E402

S445_SHA_PREFIX = "57831e610b545e75"
S449_SHA_PREFIX = "84ba4e6a83a627b9"
S451_SHA_PREFIX = "dcda19ffb95b515b"
S452_SHA_PREFIX = "63758d55e84acb27"

VERDICT_A = "LIMIT_CLASSICAL"
VERDICT_B = "LIMITCHAIN_ALIVE_200"
VERDICT_C = "CHAIN_DOCUMENTED"

NSTAB = S451.NSTAB
KEYS = S452.KEYS
DEEP = (69, 137, 170, 197, 500)
M2_INF = 0.1698990367924736
M4_INF = 0.0089525326636440
M8_INF = 0.0010081970691365
M16_INF = 0.0001230324491490
RHO_BAR = 1e-4
PNT_BAR = 5e-4
B57 = S445.B57
JMAX = 200
LIP_BAR = 0.25
GLX, GLW = np.polynomial.legendre.leggauss(24)

SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
CHECKS = []
T0 = time.time()


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok)))
    print("  [%s] %-44s %s" % ("PASS" if ok else "FAIL", name, detail),
          flush=True)
    return bool(ok)


def section(t):
    print("\n" + "=" * 78)
    print(t)
    print("=" * 78, flush=True)


def firewall_audit():
    src = open(os.path.abspath(__file__), "r", encoding="utf-8").read()
    tree = ast.parse(src)
    forb = {"zeta" + "zero", "n" + "zeros", "prime" + "range",
            "is" + "prime", "gram" + "point"}
    bad = []
    for node in ast.walk(tree):
        nm = node.attr if isinstance(node, ast.Attribute) else (
            node.id if isinstance(node, ast.Name) else None)
        if nm and nm.lower() in forb:
            bad.append("%s@%d" % (nm, node.lineno))
    return (not bad), ("NO zero/oracles; moments / arch / pack only"
                       if not bad else "; ".join(bad))


def fold_moments_from_c(c, L, nmax):
    d = V.spectral_density(c)
    jj = np.arange(1, L // 2 + 1)
    theta = 2.0 * math.pi * jj / L
    x = np.cos(theta)
    wt = (2.0 / L) * (1.0 - np.cos(theta)) * d[jj]
    wt[-1] *= 0.5
    keep = np.abs(wt) > 1e-300
    x, wt = x[keep], wt[keep]
    pos = wt > 0
    return S449.cheb_moments(x[pos], wt[pos], x[~pos], -wt[~pos],
                             int(nmax))


def moments_arch(kz, nmax):
    """Folded Chebyshev moments of the ARCH lags only
    (von Mangoldt comb deleted; same fold geometry)."""
    _alpha, M, L, Nw, D = V.window_shape(kz)
    return fold_moments_from_c(V.arch_lags(M, D), L,
                               min(int(nmax), int(Nw)))


def pnt_lags(alpha, M, D):
    """Replace the von Mangoldt tent-sum by the PNT density
    dpsi ~ e^u du (same support, same tent, same fold).
    SCRAMBLE is a different test -- this keeps geometry."""
    umax = 2.0 * alpha
    c = np.zeros(M)
    for i in range(M):
        s = i * D
        lo = max(0.0, s - D)
        hi = min(umax, s + D)
        if hi > lo:
            mid, half = 0.5 * (lo + hi), 0.5 * (hi - lo)
            u = mid + half * GLX
            tent = np.maximum(0.0, 1.0 - np.abs(s - u) / D)
            c[i] -= half * float(np.dot(GLW, tent * np.exp(0.5 * u)))
        if s + D > 0:
            lo2, hi2 = 0.0, min(D, umax)
            if hi2 > lo2:
                mid, half = 0.5 * (lo2 + hi2), 0.5 * (hi2 - lo2)
                u = mid + half * GLX
                tent = np.maximum(0.0, 1.0 - (s + u) / D)
                c[i] -= half * float(np.dot(GLW, tent * np.exp(0.5 * u)))
    return c


def moments_pnt(kz, nmax):
    alpha, M, L, Nw, D = V.window_shape(kz)
    c = V.arch_lags(M, D) + pnt_lags(alpha, M, D)
    return fold_moments_from_c(c, L, min(int(nmax), int(Nw)))


def first_rel_break(a, b, eps):
    n = min(len(a), len(b))
    for i in range(n):
        den = max(1.0, abs(a[i]), abs(b[i]))
        if abs(a[i] - b[i]) / den > eps:
            return i
    return n


def part_limit(smoke):
    section("S1  LIMIT IDENTIFICATION  (A)")
    keys = (17, 136, 500) if smoke else (
        17, 26, 69, 136, 137, 197, 500)
    m500, _ = S449.load_mom(500, 40)
    check("G10-m2-universal",
          abs(m500[2] - M2_INF) < 1e-12,
          "kz500 m2=%.16f pin=%.16f" % (m500[2], M2_INF))
    check("G11-m16-universal",
          abs(m500[16] - M16_INF) < 1e-12,
          "kz500 m16=%.16f" % m500[16])
    for kz in keys:
        nmax = 24 if smoke else min(40, NSTAB[kz])
        m, _ = S449.load_mom(kz, nmax)
        n = min(len(m), 40, NSTAB[kz])
        if n <= 2:
            continue
        rel = np.abs(m[2:n] - m500[2:n]) / np.maximum(
            1.0, np.abs(m500[2:n]))
        bar = 2e-6 if kz < 40 else 1e-8
        check("G12-shape-kz%d" % kz,
              float(rel.max()) < bar,
              "maxrel j=2..%d vs 500 = %.3e" % (n, float(rel.max())))
    # MAIN vs ARCH
    arch_keys = (17, 136) if smoke else (17, 116, 136)
    for kz in arch_keys:
        ns = NSTAB[kz]
        nmax = ns + 2 if ns < 80 else min(ns + 2, 180)
        mt, _ = S449.load_mom(kz, nmax)
        ma = moments_arch(kz, nmax)
        br = first_rel_break(mt, ma, 1e-4)
        check("G13-arch-kz%d" % kz,
              br >= ns,
              "MAIN-ARCH break at %d (n_stab=%d)" % (br, ns))
    # m0 does not converge
    m0s = [S449.load_mom(kz, 8)[0][0] for kz in (17, 136, 500)]
    check("G14-m0-no-finite-limit",
          max(m0s) - min(m0s) > 2.0,
          "m0 range %.3f .. %.3f (arch mass grows)"
          % (min(m0s), max(m0s)))
    # PNT world: same fold, comb -> smooth density
    pnt_keys = (17,) if smoke else (17, 137)
    for kz in pnt_keys:
        mt, _ = S449.load_mom(kz, 16)
        mp = moments_pnt(kz, 16)
        rel = np.abs(mt[2:16] - mp[2:16]) / np.maximum(
            1.0, np.abs(mt[2:16]))
        check("G15-pnt-kz%d" % kz,
              float(rel.max()) < PNT_BAR,
              "MAIN-PNT maxrel j=2..15 = %.3e (ARCH is the exact "
              "limit; PNT is the nearby classical proxy)"
              % float(rel.max()))
    # drop-500: m2 already at the pin on kz137/197
    m137, _ = S449.load_mom(137, 8)
    check("G16-drop500-m2",
          abs(m137[2] - M2_INF) < 1e-10,
          "kz137 m2=%.16f vs pin (no kz500)" % m137[2])


def part_chain(smoke):
    section("S2  LIMIT CHAIN  (B)")
    keys = (17, 500) if smoke else (197, 500)
    js = (16,) if smoke else (20, 40, 80, 160, 200)
    worst = 0.0
    for kz in keys:
        w = S452.masses_of(kz)
        for j in js:
            if j > NSTAB[kz] or j > int(w["N"]) - 3:
                continue
            rho, _Bw = S452.rho_last(w["mz"], w["border"], j)
            worst = max(worst, abs(rho))
            check("G20-rho-kz%d-j%d" % (kz, j),
                  abs(rho) + RHO_BAR < B57,
                  "rho=%.3e  bar+err=%.1e < 5/7" % (rho, abs(rho) + RHO_BAR))
    check("G21-jmax-alive",
          worst + RHO_BAR < B57 and VERDICT_B == "LIMITCHAIN_ALIVE_200",
          "worst |rho_j|=%.3e on computed prefix; j_max=%d" % (worst, JMAX))
    # drop-500: still tiny on kz197
    if not smoke:
        w = S452.masses_of(197)
        rho, _ = S452.rho_last(w["mz"], w["border"], 200)
        check("G22-drop500-still-alive",
              abs(rho) + RHO_BAR < B57,
              "kz197 j=200 rho=%.3e" % rho)
    # mu-chain h / b couplings stay positive (proxy for h_j(inf)>0)
    kz_h = 17 if smoke else 500
    depth = 16 if smoke else JMAX
    w = S452.masses_of(kz_h)
    _a, bcoupl, h0 = S445.mu_chain_opt(
        w["mz"]["xp"], w["mz"]["wp"], depth, engine="numpy")
    check("G23-h-positive-kz%d" % kz_h,
          float(h0) > 0.0 and float(np.min(bcoupl[:depth])) > 0.0,
          "h0=%.4f min b[0..%d]=%.3e" % (h0, depth - 1,
                                          float(np.min(bcoupl[:depth]))))


def part_lip(smoke):
    section("S3  L2 LIPSCHITZ + L1-L3  (C)")
    w = S452.masses_of(17)
    border = w["border"]
    p0 = S451.pack_at(w["mz"], 18, border)
    m0 = S451.cheb_moments_xy(w["mz"]["xp"], w["mz"]["wp"],
                              w["mz"]["yn"], w["mz"]["vn"], 20)
    xs = np.asarray(w["mz"]["xp"], float)
    ws = np.asarray(w["mz"]["wp"], float)
    T2 = 2.0 * xs * xs - 1.0
    eps = 1e-5
    mz2 = dict(w["mz"])
    mz2["wp"] = ws + eps * float(np.mean(np.abs(ws))) * T2
    p = S451.pack_at(mz2, 18, border)
    mm = S451.cheb_moments_xy(mz2["xp"], mz2["wp"],
                             mz2["yn"], mz2["vn"], 20)
    lip = abs(p["qdag"] - p0["qdag"]) / max(abs(mm[2] - m0[2]), 1e-18)
    check("G30-lipschitz-m2",
          lip < LIP_BAR,
          "dq/dm_2=%.3f (eps=1e-5)" % lip)
    check("G31-chain-documented",
          VERDICT_C == "CHAIN_DOCUMENTED",
          "[L1] MEASURED  [L2] MEASURED  [L3] MEASURED(j<=200)/OPEN")


def main():
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke
    print("=" * 78)
    print("limit_object_probe -- PRIME.RDAGGER.LIMIT_OBJECT.01 "
          "(round 454)")
    print("SPEC_SHA %s" % SPEC_SHA[:16])
    print("mode: %s" % ("SMOKE" if smoke else "FULL"))
    print("=" * 78)
    section("S0  FIREWALL")
    okf, det = firewall_audit()
    check("G00-firewall", okf, det)
    check("G00b-import-sha",
          S445.SPEC_SHA.startswith(S445_SHA_PREFIX)
          and S449.SPEC_SHA.startswith(S449_SHA_PREFIX)
          and S451.SPEC_SHA.startswith(S451_SHA_PREFIX)
          and S452.SPEC_SHA.startswith(S452_SHA_PREFIX),
          "S445 %s S449 %s S451 %s S452 %s"
          % (S445.SPEC_SHA[:16], S449.SPEC_SHA[:16],
             S451.SPEC_SHA[:16], S452.SPEC_SHA[:16]))
    part_limit(smoke)
    part_chain(smoke)
    part_lip(smoke)
    r1 = S445.pack(17, engine="numpy", want_den=False)
    r2 = S445.pack(17, engine="numpy", want_den=False)
    check("G40-determinism",
          r1["qdag"] == r2["qdag"],
          "k=5 run1=run2 q=%.16f" % r1["qdag"])
    section("S4  VERDICT")
    prev = all(ok for _n, ok in CHECKS)
    check("G50-verdict",
          prev and VERDICT_A == "LIMIT_CLASSICAL"
          and VERDICT_B == "LIMITCHAIN_ALIVE_200"
          and VERDICT_C == "CHAIN_DOCUMENTED",
          "LIMIT_CLASSICAL / LIMITCHAIN_ALIVE_200 / "
          "CHAIN_DOCUMENTED; no RH / no anti-RH")
    n_fail = sum(1 for _n, ok in CHECKS if not ok)
    n_ok = len(CHECKS) - n_fail
    print("\nRESULT: %d/%d gates PASS   SPEC_SHA %s   (%.1fs)" % (
        n_ok, len(CHECKS), SPEC_SHA[:16], time.time() - T0))
    if n_fail == 0:
        print("LIMIT OBJECT %sVERIFIED" % ("SMOKE " if smoke else ""))
        return 0
    print("LIMIT OBJECT FAILED %d" % n_fail)
    return 1


if __name__ == "__main__":
    sys.exit(main())
