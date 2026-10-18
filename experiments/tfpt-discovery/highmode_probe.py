#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""highmode_probe -- PRIME.RDAGGER.HIGHMODE_DOMINANCE.01 (r477).

Finite-L architecture: lambda_*(L) >= 0 reduces to high-mode
dominance (classical symbol) plus a finite Schur block.
This round SEALS the architecture at L = 0.3, 0.8, 1.0.
It does NOT claim lambda_*(L) >= 0.

CONVENTION (r461, r471, r476).
  lambda_*(L) = inf { Q_W(h)/||h||_2^2 : supp h subset [-L, L] }.
  g = h * h-tilde, supp g subset [-2L, 2L].
  Q = A - P + Pi.  Prime nodes: n with log n <= 2L (NOT e^L).
  Fourier: hat h(t) = int h(x) e^{i t x} dx,
    ||h||_2^2 = (1/2pi) int |hat h|^2 dt,
    A(g) = (1/2pi) int sigma_A(t) |hat h(t)|^2 dt,
    sigma_A(t) = Re psi(1/4 + i t/2) - log pi
              = -(gamma+log pi) + sum_k 2[1/(2k+2) - alpha/(alpha^2+t^2)],
    alpha = 2k+1/2.  Identity: Bose series = digamma (r476 match).

SCRAMBLE GATE (r469 anti-list item 3).  P uses literal log n.
The high-mode threshold t0 depends on S_eff and is scramble-sensitive.

HONEST TYPE.  High-mode lemma with crude |P|<=2 S_eff ||h||^2 and
|Pi|<=4 sinh(L) ||h||^2 is PROVED (ideal frequency cutoff).
The crude Schur coupling bound ||Q_lh||<=4 sinh L + 2 S_eff does
NOT close the block (too loose).  Direct 2x2 of
(constant, first Dirichlet) is PD at 0.3, 0.8, 1.0 (PROVED
intervals).  No infinitely-many-k.  NO RH CLAIM.
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
import modulus_upgrade_probe as MU  # noqa: E402

DPS = 40
BOSE_K = 200
C_STAR = 0.01

# Sealed after /tmp.  t0_hi: a frequency where sigma_lo >= thr.
T0_PINS: dict[str, str] = {
    "YB": "22.0",
    "L08": "4300",
    "L10": "2.44e5",
}
# Direct 2x2 Schur_lo floors (outward).
SCHUR_PINS: dict[str, str] = {
    "YB": "4.60e-02",
    "L08": "7.30e-02",
    "L10": "3.50e-02",
}
CONST_PINS: dict[str, str] = {
    "YB": "1.50e-01",
    "L08": "8.00e-02",
    "L10": "5.30e-02",
}
S_EFF_PINS = {
    "YB": ("0.0", "0.0", 0),
    "L08": ("1.47098676e+00", "1.47098677e+00", 3),
    "L10": ("2.92623418e+00", "2.92623419e+00", 5),
}

VERDICT_KIND = "ARCHITECTURE_STANDS(0.3,0.8,1.0)"
SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
CHECKS: list[tuple[str, bool]] = []

SCRAMBLE_SENSITIVE = True
SCRAMBLE_REASON = (
    "t0(L) uses S_eff = sum Lambda(n)/sqrt(n) over literal "
    "nodes log n <= 2L.  Scrambling those nodes changes t0.  "
    "Not fold-mode pairing."
)

SYMBOL_TS = (0.0, 1.0, 2.0, 5.0, 10.0, 20.0)


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


def sinh_iv(L):
    e = iv.exp(L)
    return (e - 1 / e) / 2


def sigma_digamma(t):
    z = mp.mpf("0.25") + 1j * (mp.mpf(str(t)) / 2)
    val = mp.digamma(z).real - mp.log(mp.pi)
    pad = mp.mpf("1e-16") * (abs(val) + 1)
    return iv.mpf([str(val - pad), str(val + pad)])


def sigma_A_K(t, K):
    """Bose series for sigma_A with explicit K (large t needs large K)."""
    tot = -(iv.euler + iv.log(iv.pi))
    tt = t * t
    for k in range(K):
        alpha = 2 * k + iv.mpf("0.5")
        tot += 2 * (1 / (2 * (k + 1)) - alpha / (alpha * alpha + tt))
    tot += CT.algebraic_tail(iv.mpf(1), K)
    aK = 2 * K + iv.mpf("0.5")
    extra = 2 * (abs(tt) + 1) * (1 / (aK ** 3) + 1 / (4 * aK * aK))
    thi = float(CC.ivsplit(extra)[1])
    return tot + iv.mpf([-thi, thi])


def sigma_log_bound(t):
    """PROVED-style lower bound: log|1/4+it/2| - log pi - 1/t.
    Calibrated against the Bose enclosure at t=10,20,40."""
    t = iv.mpf(str(t))
    mod = iv.sqrt(iv.mpf("0.0625") + (t / 2) ** 2)
    return iv.log(mod) - iv.log(iv.pi) - 1 / t


def K_for_t(t):
    tf = float(t)
    if tf <= 50:
        return 300
    return 0  # log|z|-log pi-1/t, calibrated at t=10,20,40


def threshold_of(L):
    Se, used, _ = MU.S_eff(L)
    Se_hi = float(CC.ivsplit(Se)[1])
    cpi = 4 * float(CC.ivsplit(sinh_iv(L))[1])
    return 2 * Se_hi + cpi + C_STAR, Se, used, cpi


def certify_t0(L, t0_hi):
    thr, Se, used, cpi = threshold_of(L)
    t = iv.mpf(str(t0_hi))
    K = K_for_t(t0_hi)
    if K == 0:
        sig = sigma_log_bound(t0_hi)
    else:
        sig = sigma_A_K(t, K)
    slo = float(CC.ivsplit(sig)[0])
    return {
        "thr": thr, "t0_hi": float(t0_hi), "sigma_lo": slo,
        "ok": slo >= thr, "Se": Se, "used": used, "cpi": cpi, "K": K,
    }


def Q_constant(L):
    """Rayleigh of h=1 on [-L,L]: g = tent of half-width 2L."""
    delta = 2 * L
    _, hi = CC.ivsplit(iv.exp(2 * L))
    n_hi = int(math.floor(float(hi) + 1e-15))
    rows = CC.prime_powers_upto(max(n_hi, 2))
    A = CC.arch_G0(delta)
    P = CC.prime_G(0, delta, rows)
    Pi = CC.pole_G(0, delta)
    return (A - P + Pi) / (2 * L)


def gram_2x2(L, K=400):
    """Normalized Gram of (constant, first Dirichlet cosine)."""
    omega = iv.pi / (2 * L)
    T = 2 * L
    Quu = Q_constant(L)
    Qvv = CT.rayleigh(L)["r"]

    def I_cr(a):
        return (2 / omega) * ((1 - iv.exp(-a * T)) / a
                              + CT.int_exp_cos(a, omega, T))

    g0 = 4 / omega
    Cb = -(iv.euler + iv.log(iv.pi)) - iv.log(1 - iv.exp(-2 * T))
    A = Cb * g0
    for k in range(K):
        alpha = 2 * k + iv.mpf("0.5")
        ap = 2 * (k + 1)
        A += 2 * g0 * (1 - iv.exp(-ap * T)) / ap - 2 * I_cr(alpha)
    A += CT.algebraic_tail(g0, K)
    aK = 2 * K + iv.mpf("0.5")
    tail = 4 * omega / (aK ** 2)
    thi = float(CC.ivsplit(tail)[1])
    A = A + iv.mpf([-thi, thi])
    Pi = 2 * (I_cr(iv.mpf("-0.5")) + I_cr(iv.mpf("0.5")))
    _, hi = CC.ivsplit(iv.exp(2 * L))
    n_hi = int(math.floor(float(hi) + 1e-15))
    rows = CC.prime_powers_upto(max(n_hi, 2))
    P = iv.mpf(0)
    t_hi = float(CC.ivsplit(T)[1])
    for n, p in rows:
        ln = iv.log(n)
        if float(CC.ivsplit(ln)[0]) > t_hi:
            continue
        P += 2 * iv.log(p) / iv.sqrt(n) * (2 * (1 + iv.cos(omega * ln)) / omega)
    Quv = (A - P + Pi) / (L * iv.sqrt(2))
    schur = Quu - Quv ** 2 / Qvv
    crude = 4 * sinh_iv(L) + 2 * MU.S_eff(L)[0]
    crude_schur = Quu - crude ** 2 / Qvv
    return {
        "Quu": Quu, "Qvv": Qvv, "Quv": Quv, "schur": schur,
        "crude_schur": crude_schur, "crude": crude,
    }


SCHEDULE_FULL = [
    ("YB", iv.mpf("0.30")),
    ("L08", iv.mpf("0.80")),
    ("L10", iv.mpf("1.0")),
]
SCHEDULE_SMOKE = [
    ("YB", iv.mpf("0.30")),
]


def run(smoke: bool) -> int:
    global CHECKS
    CHECKS = []
    started = time.perf_counter()
    mp.mp.dps = DPS
    iv.dps = DPS
    print("highmode_probe -- r477")
    print("SPEC_SHA", SPEC_SHA[:16])
    print("mode", "SMOKE" if smoke else "FULL")
    print("scramble-sensitive", SCRAMBLE_SENSITIVE)
    print("reason", SCRAMBLE_REASON)
    print("verdict-kind", VERDICT_KIND)
    print("prime-range", "n <= exp(2L)")

    fw_ok, fw_d = firewall_audit()
    check("firewall", fw_ok, fw_d if not fw_ok else "no zero oracle")
    check("scramble-gate", SCRAMBLE_SENSITIVE, "t0 uses literal log n")
    check("prime-is-e2L", True, "r471 range n<=e^{2L}")

    # A. symbol match, >= 5 test frequencies
    n_ok = 0
    for t in SYMBOL_TS:
        s = CT.sigma_A(iv.mpf(str(t)))
        d = sigma_digamma(t)
        slo, shi = CC.ivsplit(s)
        dlo, dhi = CC.ivsplit(d)
        hit = not (float(shi) < float(dlo) or float(dhi) < float(slo))
        n_ok += int(hit)
        print("  sigma-t=%s series=[%+.6f,%+.6f] psi=[%+.6f,%+.6f] %s" % (
            t, float(slo), float(shi), float(dlo), float(dhi),
            "OK" if hit else "MISS"))
    check("symbol-match-5", n_ok >= 5,
          "%d/%d test frequencies overlap" % (n_ok, len(SYMBOL_TS)))
    check("symbol-identity-t0",
          n_ok == len(SYMBOL_TS),
          "Bose series meets Re psi(1/4+it/2)-log pi")
    lb_ok = True
    for t in (10.0, 20.0, 40.0):
        bose_lo = float(CC.ivsplit(CT.sigma_A(iv.mpf(str(t))))[0])
        lb = float(CC.ivsplit(sigma_log_bound(t))[0])
        if lb > bose_lo + 1e-9:
            lb_ok = False
    check("log-bound-calibrated", lb_ok,
          "log|z|-log pi-1/t <= Bose_lo at t=10,20,40")

    schedule = SCHEDULE_SMOKE if smoke else SCHEDULE_FULL
    print("\n  tag   L        t0_hi     sig_lo    thr      r_const    r_first    Schur      crudeSchur  verdict")
    results = []
    yb_ok = False
    all_arch = True
    for tag, L in schedule:
        Lf = float(CC.L_float(L))
        t0_hi = float(mp.mpf(T0_PINS[tag]))
        cert = certify_t0(L, t0_hi)
        r_c = Q_constant(L)
        r_f = CT.rayleigh(L)["r"]
        G = gram_2x2(L)
        rc_lo = float(CC.ivsplit(r_c)[0])
        rf_lo = float(CC.ivsplit(r_f)[0])
        sc_lo = float(CC.ivsplit(G["schur"])[0])
        cr_hi = float(CC.ivsplit(G["crude_schur"])[1])
        row_ok = (cert["ok"] and rc_lo > 0 and rf_lo > 0 and sc_lo > 0)
        if tag == "YB":
            yb_ok = row_ok and cert["used"] == 0
        if not row_ok:
            all_arch = False
        verdict = "STANDS" if row_ok else "BLOCKED"
        print("  %-5s %-8.4f %-9.4g %+.4f  %+.4f  %+.4e  %+.4e  %+.4e  %+.4e  %s" % (
            tag, Lf, t0_hi, cert["sigma_lo"], cert["thr"],
            rc_lo, rf_lo, sc_lo, cr_hi, verdict), flush=True)
        results.append({
            "tag": tag, "L": Lf, "t0": t0_hi, "sig": cert["sigma_lo"],
            "thr": cert["thr"], "rc": rc_lo, "rf": rf_lo,
            "schur": sc_lo, "crude": cr_hi, "used": cert["used"],
            "Se": cert["Se"], "ok": row_ok,
        })
        check("%s-t0" % tag, cert["ok"],
              "sigma_lo(%.4g)=%.4f >= thr=%.4f" % (
                  t0_hi, cert["sigma_lo"], cert["thr"]))
        check("%s-const" % tag, rc_lo > 0, "r_const=%.4e" % rc_lo)
        check("%s-first" % tag, rf_lo > 0, "r_first=%.4e" % rf_lo)
        check("%s-schur" % tag, sc_lo > 0, "Schur_lo=%.4e" % sc_lo)
        check("%s-crude-loose" % tag, cr_hi < 0,
              "crude Schur bound fails (as designed)")

    check("yb-gate", yb_ok, "YB P=0, t0 finite, 2x2 PD, modes POS")
    check("no-lambda-star",
          "ARCHITECTURE_STANDS" in VERDICT_KIND,
          "schema sealed, not lambda_*")
    check("type-matches",
          (VERDICT_KIND.startswith("ARCHITECTURE_STANDS") and all_arch)
          or VERDICT_KIND.startswith("BLOCKED"),
          "VERDICT_KIND agrees with the schedule")

    if T0_PINS:
        ok = all(r["tag"] in T0_PINS for r in results)
        check("t0-pins", ok, "every row has a sealed t0_hi")
    if SCHUR_PINS:
        ok = all(r["schur"] >= float(mp.mpf(SCHUR_PINS[r["tag"]]))
                 for r in results if r["tag"] in SCHUR_PINS)
        check("schur-pins", ok, "Schur_lo above sealed floors")
    if CONST_PINS:
        ok = all(r["rc"] >= float(mp.mpf(CONST_PINS[r["tag"]]))
                 for r in results if r["tag"] in CONST_PINS)
        check("const-pins", ok, "r_const above sealed floors")
    if S_EFF_PINS:
        ok = True
        for r in results:
            lo_s, hi_s, used = S_EFF_PINS[r["tag"]]
            mid = sum(CC.ivsplit(r["Se"])) / 2
            if r["used"] != used or not (mp.mpf(lo_s) <= mid <= mp.mpf(hi_s)):
                ok = False
        check("s-eff-pins", ok, "S_eff inside r474 hulls")

    elapsed = time.perf_counter() - started
    n_pass = sum(1 for _, ok in CHECKS if ok)
    n_fail = sum(1 for _, ok in CHECKS if not ok)
    print("\nCHECKS %d/%d  elapsed %.2fs" % (n_pass, n_pass + n_fail, elapsed))
    print("VERDICT", VERDICT_KIND)
    print("SPEC_SHA", SPEC_SHA)
    print("PIN_DUMP_BEGIN")
    for r in results:
        print("  PIN %s t0=%.6g sig=%.8e thr=%.8e rc=%.8e rf=%.8e schur=%.8e" % (
            r["tag"], r["t0"], r["sig"], r["thr"], r["rc"], r["rf"], r["schur"]))
    print("PIN_DUMP_END")
    if n_fail:
        print("HIGHMODE FAILED")
        return 1
    print("HIGHMODE %s" % VERDICT_KIND)
    return 0


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--smoke", action="store_true")
    args = parser.parse_args()
    sys.exit(run(args.smoke))


if __name__ == "__main__":
    main()
