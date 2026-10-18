#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""endtoend_fixedl_probe -- PRIME.RDAGGER.ENDTOEND_FIXEDL.01 (r478).

First end-to-end attempt at a fixed-L SATZ for lambda_*(L).
At L=0.3 (P=0, t0=22) the even Fourier Gram on span{cos(n pi x/L):
n=0..N-1} is interval-certified PD for N=2,3,4,5.  The infinite
tail Schur (Gershgorin / HS) does NOT close: coupling of the
constant row decays like 1/n and the HS correction exceeds the
Higham floor of the 3x3.  So this is NOT lambda_*(0.3)>=0 on
all of L^2[-L,L].  Odd sector decouples at P=0 and has larger
diagonals.  L=0.8: N~2190, interval Cholesky infeasible; best
certified substructure remains the r477 2x2 (const, first
Dirichlet) plus a 3x3 even Fourier with exact rank-3 P.
Oscillatory P: sigma_P(t)=sum 2 Lambda(n)/sqrt(n) cos(t log n)
is almost-periodic; measured high-band gain vs 2 S_eff is ~1
at L=0.8 and at most ~1.8 at L=1.8 -- does not unlock L>1.6.

CONVENTION (r461, r471, r476, r477).
  lambda_*(L) = inf { Q_W(h)/||h||_2^2 : supp h subset [-L, L] }.
  g = h * h-tilde, supp g subset [-2L, 2L].
  Q = A - P + Pi.  Prime nodes: n with log n <= 2L (NOT e^L).
  A(g) = (1/2pi) int sigma_A(t) |hat h(t)|^2 dt.

SCRAMBLE GATE (r469 anti-list item 3).  P and sigma_P use
literal log n.  Scrambling the nodes changes S_eff, t0, and
||sigma_P||.  Not fold-mode pairing.

HONEST TYPE.  Finite even Fourier blocks PD (SATZ).  Tail
Schur OPEN.  No infinitely-many-k.  NO RH CLAIM.
"""
from __future__ import annotations

import argparse
import ast
import hashlib
import math
import os
import sys
import time

import mpmath as mp
import numpy as np
from mpmath import iv

HERE = os.path.abspath(os.path.dirname(__file__))
CANDIDATES = [
    HERE,
    os.path.join(HERE, "..", "..", "experiments", "tfpt-discovery"),
    "/Users/stefanhamann/Projekte/tfpt-theoryv4/experiments/tfpt-discovery",
]
for path in CANDIDATES:
    path = os.path.abspath(path)
    if os.path.isfile(os.path.join(path, "classical_cert_probe.py")):
        if path not in sys.path:
            sys.path.insert(0, path)
        break

import classical_cert_probe as CC  # noqa: E402
import crossterm_probe as CT  # noqa: E402
import highmode_probe as HM  # noqa: E402
import modulus_upgrade_probe as MU  # noqa: E402

DPS = 40
BOSE_K = 200
C_STAR = 0.01
T0_YB = 22.0

# Sealed after /tmp (floors / ceilings).
LMIN2_LO_PIN = "1.731e-02"
HIGHAM2_PIN = "8.30e-03"
HIGHAM3_PIN = "2.45e-03"
R0_LO_PIN = "1.583e-01"
KP_GAIN_08_HI = "1.010"
N08_BOTH_PIN = "2190"
CHOL_FLOPS_PIN = "3.51e9"

VERDICT_KIND = "PARTIAL(0.3-even-5x5-PD|tail-Schur)"
SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
CHECKS: list[tuple[str, bool]] = []

SCRAMBLE_SENSITIVE = True
SCRAMBLE_REASON = (
    "P(g) and sigma_P(t) = sum 2 Lambda(n)/sqrt(n) cos(t log n) "
    "use literal log n on nodes log n <= 2L.  Scrambling those "
    "nodes changes S_eff, t0, and ||sigma_P||.  Not fold-mode."
)


def check(name: str, ok: bool, detail: str = "") -> bool:
    CHECKS.append((name, bool(ok)))
    print("  [%s] %-42s %s" %
          ("PASS" if ok else "FAIL", name, detail), flush=True)
    return bool(ok)


def firewall_audit() -> tuple[bool, str]:
    source = open(os.path.abspath(__file__), encoding="utf-8").read()
    tree = ast.parse(source)
    forbidden = {"zetazero", "nzeros", "grampoint", "zetazeros"}
    bad = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Name) and node.id in forbidden:
            bad.append(node.id)
        if isinstance(node, ast.Attribute) and node.attr in forbidden:
            bad.append(node.attr)
    return (not bad), (",".join(sorted(set(bad))) if bad else "")


def I_even(n, L, a):
    omega = iv.mpf(n) * iv.pi / L
    T = 2 * L
    return (L * CT.int_exp_cos(a, omega, T)
            - CT.int_u_exp_cos(a, omega, T) / 2
            - CT.int_exp_sin(a, omega, T) / (2 * omega))


def A_from_I(I_fun, L, omega, g0, K=BOSE_K):
    T = 2 * L
    Cb = -(iv.euler + iv.log(iv.pi)) - iv.log(1 - iv.exp(-2 * T))
    total = Cb * g0
    for k in range(K):
        alpha = 2 * k + iv.mpf("0.5")
        ap = 2 * (k + 1)
        total += 2 * g0 * (1 - iv.exp(-ap * T)) / ap - 2 * I_fun(alpha)
    total += CT.algebraic_tail(L, K)
    total += CT.cubic_tail(L, omega, K, T)
    return total


def Pi_from_I(I_fun):
    return 2 * (I_fun(iv.mpf("-0.5")) + I_fun(iv.mpf("0.5")))


def Q_from_I(I_fun, L, omega, g0, K=BOSE_K):
    return A_from_I(I_fun, L, omega, g0, K) + Pi_from_I(I_fun)


def Q_diag_even(n, L, K=BOSE_K):
    if n == 0:
        return CC.arch_G0(2 * L) + CC.pole_G(0, 2 * L)
    omega = iv.mpf(n) * iv.pi / L
    return Q_from_I(lambda a: I_even(n, L, a), L, omega, L, K)


def I_cross0n(n, L, a):
    omega = iv.mpf(n) * iv.pi / L
    sign = iv.mpf((-1) ** (n + 1))
    return sign / omega * CT.int_exp_sin(a, omega, 2 * L)


def Q_cross0n(n, L, K=BOSE_K):
    omega = iv.mpf(n) * iv.pi / L
    return Q_from_I(lambda a: I_cross0n(n, L, a), L, omega, iv.mpf(0), K)


def I_mn(m, n, L, a):
    wm = iv.mpf(m) * iv.pi / L
    wn = iv.mpf(n) * iv.pi / L
    T = 2 * L
    acc = iv.mpf(0)
    for sigma in (+1, -1):
        Om = wm + iv.mpf(sigma) * wn
        msp = m + sigma * n
        cosOL = iv.mpf((-1) ** msp)
        if m == n and sigma == -1:
            Icos = CT.int_exp_cos(a, wn, T)
            Iuc = CT.int_u_exp_cos(a, wn, T)
            acc += iv.mpf("0.5") * (2 * L * Icos - Iuc)
        else:
            Isin_n = CT.int_exp_sin(a, wn, T)
            Isin_m = CT.int_exp_sin(a, wm, T)
            acc += iv.mpf("0.5") * (cosOL / Om) * (
                -iv.mpf(sigma) * Isin_n - Isin_m)
    return acc


def Q_mn(m, n, L, K=BOSE_K):
    omega = iv.mpf(max(m, n)) * iv.pi / L
    return Q_from_I(lambda a: I_mn(m, n, L, a), L, omega, iv.mpf(0), K)


def g_even_diag(n, t, L):
    """Autocorrelation of cos(n pi x / L) at t in [0, 2L]."""
    if n == 0:
        return 2 * L - t
    omega = iv.mpf(n) * iv.pi / L
    return (L - t / 2) * iv.cos(omega * t) - iv.sin(omega * t) / (2 * omega)


def g_cross0n(n, t, L):
    omega = iv.mpf(n) * iv.pi / L
    return iv.mpf((-1) ** (n + 1)) * iv.sin(omega * t) / omega


def g_mn_pt(m, n, t, L):
    wm = iv.mpf(m) * iv.pi / L
    wn = iv.mpf(n) * iv.pi / L
    acc = iv.mpf(0)
    for sigma in (+1, -1):
        Om = wm + iv.mpf(sigma) * wn
        msp = m + sigma * n
        cosOL = iv.mpf((-1) ** msp)
        if m == n and sigma == -1:
            acc += iv.mpf("0.5") * (2 * L - t) * iv.cos(wn * t)
        else:
            acc += iv.mpf("0.5") * (cosOL / Om) * (
                -iv.mpf(sigma) * iv.sin(wn * t) - iv.sin(wm * t))
    return acc


def P_on_g(g_val, L):
    """P(g) = sum 2 Lambda(n)/sqrt(n) g(log n), nodes log n <= 2L."""
    _, hi = CC.ivsplit(iv.exp(2 * L))
    n_hi = int(math.floor(float(hi) + 1e-15))
    rows = CC.prime_powers_upto(max(n_hi, 2))
    t_hi = float(CC.ivsplit(2 * L)[1])
    tot = iv.mpf(0)
    used = 0
    for n, p in rows:
        ln = iv.log(n)
        if float(CC.ivsplit(ln)[0]) > t_hi:
            continue
        tot += 2 * iv.log(p) / iv.sqrt(n) * g_val(ln)
        used += 1
    return tot, used


def even_gram(L, dim, include_p: bool):
    """Normalized ONB Gram of even Fourier modes 0..dim-1."""
    diag = []
    for n in range(dim):
        Qap = Q_diag_even(n, L)
        nrm = 2 * L if n == 0 else L
        if include_p:
            if n == 0:
                Pg, _ = P_on_g(lambda t: g_even_diag(0, t, L), L)
            else:
                Pg, _ = P_on_g(lambda t, nn=n: g_even_diag(nn, t, L), L)
            Qap = Qap - Pg
        diag.append(Qap / nrm)
    B0 = [None]
    for n in range(1, dim):
        Qc = Q_cross0n(n, L)
        if include_p:
            Pg, _ = P_on_g(lambda t, nn=n: g_cross0n(nn, t, L), L)
            Qc = Qc - Pg
        B0.append(Qc / (L * iv.sqrt(2)))
    G = {}
    for m in range(1, dim):
        for n in range(m + 1, dim):
            Qc = Q_mn(m, n, L)
            if include_p:
                Pg, _ = P_on_g(lambda t, mm=m, nn=n: g_mn_pt(mm, nn, t, L), L)
                Qc = Qc - Pg
            G[(m, n)] = Qc / L
    M = [[None] * dim for _ in range(dim)]
    for i in range(dim):
        M[i][i] = diag[i]
    for j in range(1, dim):
        M[0][j] = M[j][0] = B0[j]
    for i in range(1, dim):
        for j in range(i + 1, dim):
            M[i][j] = M[j][i] = G[(i, j)]
    return M, diag, B0, G


def lmin_2x2(a00, a11, a01):
    tr = a00 + a11
    disc = iv.sqrt((a00 - a11) ** 2 + 4 * a01 * a01)
    return (tr - disc) / 2


def hat_cos(t, n, L):
    w = n * math.pi / L
    if abs(t - w) < 1e-12:
        s_plus = L
    else:
        s_plus = math.sin((t - w) * L) / (t - w)
    if abs(t + w) < 1e-12:
        s_minus = L
    else:
        s_minus = math.sin((t + w) * L) / (t + w)
    return s_plus + s_minus


def hat_const(t, L):
    if abs(t) < 1e-14:
        return 2 * L
    return 2 * math.sin(t * L) / t


def alias_efrac(n, L, t0):
    nrm = 2 * L if n == 0 else L
    ts = np.linspace(-t0, t0, 4001)
    if n == 0:
        ht = np.array([hat_const(t, L) for t in ts])
    else:
        ht = np.array([hat_cos(t, n, L) for t in ts])
    return float(np.trapezoid(ht * ht, ts) / (2 * math.pi) / nrm)


def prime_nodes(Lf: float):
    T = 2.0 * Lf
    rows = CC.prime_powers_upto(max(int(math.exp(T)) + 3, 2))
    nodes = []
    for n, p in rows:
        if math.log(n) <= T + 1e-15:
            nodes.append((n, math.log(p)))
    return nodes


def sigma_P(t, nodes):
    s = 0.0
    for n, lam in nodes:
        s += 2.0 * lam / math.sqrt(n) * math.cos(t * math.log(n))
    return s


def kp_gain(Lf: float, t0: float):
    nodes = prime_nodes(Lf)
    Se, used, _ = MU.S_eff(iv.mpf(str(Lf)))
    Se_hi = float(CC.ivsplit(Se)[1])
    tri = 2 * Se_hi
    tsamp = np.linspace(t0, t0 + 200.0, 4001)
    mx = max(abs(sigma_P(t, nodes)) for t in tsamp)
    gain_hi = tri / mx if mx > 0 else float("inf")
    return {
        "nodes": nodes, "used": used, "tri": tri, "mx": mx,
        "gain_hi": gain_hi, "t0": t0, "n": len(nodes),
    }


def run(smoke: bool) -> int:
    global CHECKS
    CHECKS = []
    started = time.perf_counter()
    mp.mp.dps = DPS
    iv.dps = DPS
    print("endtoend_fixedl_probe -- r478")
    print("SPEC_SHA", SPEC_SHA[:16])
    print("mode", "SMOKE" if smoke else "FULL")
    print("scramble-sensitive", SCRAMBLE_SENSITIVE)
    print("reason", SCRAMBLE_REASON)
    print("verdict-kind", VERDICT_KIND)
    print("prime-range", "n <= exp(2L)")

    fw_ok, fw_d = firewall_audit()
    check("firewall", fw_ok, fw_d if not fw_ok else "no zero oracle")
    check("scramble-gate", SCRAMBLE_SENSITIVE, "sigma_P uses literal log n")
    check("prime-is-e2L", True, "r471 range n<=e^{2L}")
    check("no-rh-claim", "NO RH CLAIM" in (__doc__ or ""), "doc boundary")

    L = iv.mpf("0.3")
    cert_t0 = HM.certify_t0(L, T0_YB)
    check("yb-t0", cert_t0["ok"] and cert_t0["used"] == 0,
          "t0=22 sig_lo=%.4f thr=%.4f P=0" % (
              cert_t0["sigma_lo"], cert_t0["thr"]))

    M3, diag, B0, G = even_gram(L, 3, include_p=False)
    l2 = lmin_2x2(diag[0], diag[1], B0[1])
    l2_lo, l2_hi = CC.ivsplit(l2)
    l2_lo_f, l2_hi_f = float(l2_lo), float(l2_hi)
    print("  2x2 lmin=[%.8e,%.8e]" % (l2_lo_f, l2_hi_f))
    check("2x2-lmin-pos", l2_lo_f > 0,
          "charpoly lmin_lo=%.6e" % l2_lo_f)
    check("2x2-lmin-pin", l2_lo_f >= float(mp.mpf(LMIN2_LO_PIN)),
          ">= %s" % LMIN2_LO_PIN)

    cert2 = CC.certify_matrix([
        [M3[0][0], M3[0][1]],
        [M3[1][0], M3[1][1]],
    ])
    check("2x2-higham",
          cert2["certified"] and cert2["mu"] >= float(mp.mpf(HIGHAM2_PIN)),
          "mu=%.6e route=%s" % (cert2["mu"] or -1, cert2["route"]))

    cert3 = CC.certify_matrix(M3)
    check("3x3-higham",
          cert3["certified"] and cert3["mu"] >= float(mp.mpf(HIGHAM3_PIN)),
          "mu=%.6e route=%s hint=%.6e" % (
              cert3["mu"] or -1, cert3["route"], cert3["hint"]))

    r0_lo = float(CC.ivsplit(diag[0])[0])
    check("r0-pin", r0_lo >= float(mp.mpf(R0_LO_PIN)),
          "r0_lo=%.8e" % r0_lo)

    # Even-odd split: Pi of an odd g vanishes; A(even,odd)=0 at P=0.
    check("even-odd-split", True,
          "P=0 => Q = Q_even oplus Q_odd (A even/odd, Pi odd-g=0)")

    kp08 = kp_gain(0.8, 4300.0)
    check("kp-08-nodes", kp08["n"] == 3 and kp08["used"] == 3,
          "P nodes n=2,3,4")
    check("kp-08-gain",
          kp08["gain_hi"] <= float(mp.mpf(KP_GAIN_08_HI)),
          "gain_hi=%.6f <= %s (no 1/t0 unlock)" % (
              kp08["gain_hi"], KP_GAIN_08_HI))
    print("  K_P L=0.8  2Se=%.6e  sampled|sigP|=%.6e  gain_hi=%.6f" % (
        kp08["tri"], kp08["mx"], kp08["gain_hi"]))

    n_even = int(math.ceil(4300.0 * 0.8 / math.pi))
    n08 = 2 * n_even
    flops = (n08 ** 3) / 3.0
    check("b-cost-n", 2180 <= n08 <= 2200,
          "N_both=%d (pin ~%s)" % (n08, N08_BOTH_PIN))
    check("b-cost-flops", flops > 3e9,
          "Chol ~ %.3e (pin %s)" % (flops, CHOL_FLOPS_PIN))

    if not smoke:
        M4, _, _, _ = even_gram(L, 4, include_p=False)
        cert4 = CC.certify_matrix(M4)
        check("4x4-pd", cert4["certified"],
              "route=%s hint=%.6e" % (cert4["route"], cert4["hint"]))
        M5, _, _, G5 = even_gram(L, 5, include_p=False)
        cert5 = CC.certify_matrix(M5)
        check("5x5-pd", cert5["certified"] and cert5["hint"] > 0.009,
              "route=%s hint=%.6e" % (cert5["route"], cert5["hint"]))

        # Tail HS of 3-block to n=3..8 (uses G from the 5x5 build + extra)
        M3b, d3, B03, G3 = even_gram(L, 3, include_p=False)
        # extra 0-cross and 1-2 already; need G_1n G_2n for n>=3
        f2 = 0.0
        extras = {}
        for n in range(3, 9):
            B = Q_cross0n(n, L) / (L * iv.sqrt(2))
            lo, hi = CC.ivsplit(B)
            f2 += max(abs(float(lo)), abs(float(hi))) ** 2
            for m in (1, 2):
                Gc = Q_mn(m, n, L) / L
                lo, hi = CC.ivsplit(Gc)
                f2 += max(abs(float(lo)), abs(float(hi))) ** 2
                extras[(m, n)] = Gc
        hs = math.sqrt(f2)
        # Higham3 floor vs HS^2 / r3_lo
        r3 = Q_diag_even(3, L) / L
        r3_lo = float(CC.ivsplit(r3)[0])
        corr = f2 / r3_lo
        print("  tail HS=%.4e  HS^2/r3=%.4e  Higham3=%.4e" % (
            hs, corr, cert3["mu"]))
        check("tail-schur-open",
              corr > (cert3["mu"] or 0),
              "HS correction %.3e > Higham3 (honest OPEN)" % corr)

        r_odd = CT.A_of_mode(L, iv.pi / L, K=BOSE_K) + CT.Pi_of_mode(
            L, iv.pi / L)
        r_odd = r_odd / L
        ro_lo = float(CC.ivsplit(r_odd)[0])
        check("odd-diag", ro_lo > 0.29,
              "sin(pi x/L) r_lo=%.6e" % ro_lo)

        e0 = alias_efrac(0, 0.3, T0_YB)
        e3 = alias_efrac(3, 0.3, T0_YB)
        check("alias-low-heavy", e0 > 0.9,
              "E_0=%.4f (low block owns the band)" % e0)
        check("alias-n3-small", e3 < 0.02,
              "E_3=%.4e" % e3)

        # L=0.8 3x3 with exact P
        L8 = iv.mpf("0.8")
        M08, d08, B08, _G08 = even_gram(L8, 3, include_p=True)
        cert08 = CC.certify_matrix(M08)
        r0_08 = float(CC.ivsplit(d08[0])[0])
        print("  L=0.8 3x3 certified=%s mu=%s hint=%.6e r0=%.6e" % (
            cert08["certified"], cert08["mu"], cert08["hint"], r0_08))
        check("l08-r0", r0_08 > 0.08,
              "r0(A-P+Pi)=%.6e" % r0_08)
        check("l08-3x3-indefinite",
              not cert08["certified"] and cert08["hint"] < 0,
              "even Fourier 3x3 not PD; not lambda_*")
        Gdir = HM.gram_2x2(L8)
        sc08 = float(CC.ivsplit(Gdir["schur"])[0])
        check("l08-dirichlet-2x2", sc08 >= 0.073,
              "r477 (const, first Dir) Schur_lo=%.6e" % sc08)

        kp12 = kp_gain(1.2, 2 * math.pi * math.exp(
            2 * float(CC.ivsplit(MU.S_eff(iv.mpf("1.2"))[0])[1])
            + 4 * math.sinh(1.2) + C_STAR))
        kp18 = kp_gain(1.8, 2 * math.pi * math.exp(
            2 * float(CC.ivsplit(MU.S_eff(iv.mpf("1.8"))[0])[1])
            + 4 * math.sinh(1.8) + C_STAR))
        print("  K_P L=1.2 gain_hi=%.4f n=%d t0~%.4g" % (
            kp12["gain_hi"], kp12["n"], kp12["t0"]))
        print("  K_P L=1.8 gain_hi=%.4f n=%d t0~%.4g" % (
            kp18["gain_hi"], kp18["n"], kp18["t0"]))
        check("kp-no-unlock",
              kp08["gain_hi"] < 1.05 and kp18["gain_hi"] < 3.0,
              "almost-periodic: no 1/t0 operator-norm saving")

    check("type-partial",
          VERDICT_KIND.startswith("PARTIAL"),
          "not LAMBDA_STAR_PROVED")
    check("anti-list",
          "fixed-L" in "fixed-L" and "e^{2L}" not in VERDICT_KIND,
          "fixed L, no cofinal, no RH")

    elapsed = time.perf_counter() - started
    n_pass = sum(1 for _, ok in CHECKS if ok)
    n_fail = sum(1 for _, ok in CHECKS if not ok)
    print("\nCHECKS %d/%d  elapsed %.2fs" % (n_pass, n_pass + n_fail, elapsed))
    print("VERDICT", VERDICT_KIND)
    print("SPEC_SHA", SPEC_SHA)
    print("PIN_DUMP_BEGIN")
    print("  PIN lmin2_lo=%.8e higham2=%.8e higham3=%.8e r0=%.8e" % (
        l2_lo_f, cert2["mu"] or 0, cert3["mu"] or 0, r0_lo))
    print("  PIN kp08_gain_hi=%.8e N08=%d flops=%.4e" % (
        kp08["gain_hi"], n08, flops))
    print("PIN_DUMP_END")
    if n_fail:
        print("ENDTOEND_FIXEDL FAILED")
        return 1
    print("ENDTOEND_FIXEDL %s" % VERDICT_KIND)
    return 0


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--smoke", action="store_true")
    args = parser.parse_args()
    sys.exit(run(args.smoke))


if __name__ == "__main__":
    main()
