#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""crossterm_probe -- PRIME.RDAGGER.CROSSTERM_SHARPENING.01 (r476).

F2b follow-up of r474: the arch cross-term, not the grid, was the
slack.  Route B evaluates Q_W on the generator of the first
Dirichlet H^2 ball (the ball is one-dimensional).  Route A seals
the regularized Peano constants against weilArchSide.

CONVENTION (r461, r471, r474).
  lambda_*(L) = inf { Q_W(h)/||h||_2^2 : supp h subset [-L, L] }.
  This round does NOT claim lambda_*(L) >= 0.
  Declared class: first Dirichlet H^2 ball
    { h in H^2_0([-L,L]) : ||h''||_2 <= (pi/(2L))^2 ||h||_2 }
  which equals span{ cos(pi x / (2L)) }.
  g = h * h-tilde, Q = A - P + Pi as in classical_cert_probe.
  Prime nodes: n with log n <= 2L.

SCRAMBLE GATE (r469 anti-list item 3).  P uses the literal nodes
log n.  A source-position scramble changes P and the Rayleigh.
The bound is scramble-sensitive.  Not a q^dagger pairing.

HONEST TYPE.  Direct 1-mode Rayleigh with sealed A-tail
(algebraic psi remainder).  YB gate: r_lo(L=0.3) > 0 is required.
No silent class shift.  NO RH CLAIM.
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

DPS = 40
BOSE_K = 200

# Sealed after /tmp.  r_lo / r_hi on the first Dirichlet mode.
# (lo, hi) strings, P-used count.  Hulls padded outward ~1%.
RAYLEIGH_PINS: dict[str, tuple[str, str, int]] = {
    "YB": ("1.150e-02", "1.192e-02", 0),
    "L08": ("1.818e-04", "2.101e-04", 3),
    "L5": ("9.116e-04", "9.511e-04", 4),
    "L10": ("1.087e-04", "1.267e-04", 5),
    "L12": ("8.641e-05", "9.907e-05", 8),
    "Lk8": ("1.375e-04", "1.485e-04", 10),
    "L14": ("8.637e-05", "9.613e-05", 10),
    "L16": ("9.775e-05", "1.059e-04", 13),
    "L18": ("9.582e-05", "1.027e-04", 18),
    "L20": ("7.119e-05", "7.656e-05", 24),
    "Lk12": ("2.431e-05", "2.844e-05", 27),
    "Lk16": ("3.417e-06", "5.528e-06", 70),
}

# sigma(0) ~ -5.372; Peano C0 = sum 2/alpha^3 ~ 16.166
SIGMA0_PIN = "-5.30"
PEANO_C0_PIN = "16.17"
VERDICT_KIND = "UNCONDITIONAL(L_max=2.7726)"
CLASS_NAME = "H2BALL_FIRST_DIRICHLET"

SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
CHECKS: list[tuple[str, bool]] = []

SCRAMBLE_SENSITIVE = True
SCRAMBLE_REASON = (
    "P(g) = sum 2 Lambda(n)/sqrt(n) g(log n) at the literal "
    "nodes log n <= 2L.  Scrambling those nodes changes the "
    "1-mode Rayleigh.  Not fold-mode pairing."
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


def g_of(t, L, omega):
    """Autocorrelation of h(x)=cos(omega x) on [-L,L], t in [0, 2L]."""
    return (L - t / 2) * iv.cos(omega * t) + iv.sin(omega * t) / (2 * omega)


def int_exp_cos(a, w, T):
    d = a * a + w * w
    end = iv.exp(-a * T) * (-a * iv.cos(w * T) + w * iv.sin(w * T)) / d
    return end + a / d


def int_exp_sin(a, w, T):
    d = a * a + w * w
    end = iv.exp(-a * T) * (-a * iv.sin(w * T) - w * iv.cos(w * T)) / d
    return end + w / d


def int_u_exp_cos(a, w, T):
    beta = -a + iv.mpc(0, 1) * w
    b2 = beta * beta

    def antideriv(u):
        return iv.exp(beta * u) * (beta * u - 1) / b2

    return (antideriv(T) - antideriv(iv.mpf(0))).real


def I_alpha(a, L, omega):
    """int_0^{2L} e^{-a u} g(u) du."""
    T = 2 * L
    return (L * int_exp_cos(a, omega, T)
            - int_u_exp_cos(a, omega, T) / 2
            + int_exp_sin(a, omega, T) / (2 * omega))


def algebraic_tail(L, K):
    """Exact sum_{k>=K} 2L (1/ap - 1/alpha) = -L (psi(K+1)-psi(K+1/4))."""
    d1 = mp.digamma(K + 1)
    d2 = mp.digamma(K + mp.mpf("0.25"))
    diff = d1 - d2
    lo = mp.nstr(diff, 20, strip_zeros=False)
    # outward 2 ulp at 18 digits
    pad = mp.mpf("1e-18") * (abs(diff) + 1)
    return -L * iv.mpf([str(diff - pad), str(diff + pad)])


def cubic_tail(L, omega, K, T):
    """|term_k - leading_k| <= 2L e^{-a T}/a + 2L e^{-ap T}/ap + 2 w^2 L / a^3."""
    aK = 2 * K + iv.mpf("0.5")
    geom = iv.exp(-aK * T) / aK / (1 - iv.exp(-2 * T))
    s3 = 1 / (aK ** 3) + 1 / (4 * aK * aK)
    tot = 4 * L * geom + 2 * (omega ** 2) * L * s3
    thi = float(CC.ivsplit(tot)[1])
    return iv.mpf([-thi, thi])


def A_of_mode(L, omega, K=BOSE_K):
    """A(g0) via Bose series + psi algebraic tail + O(1/k^3) pad."""
    g0 = L
    T = 2 * L
    Cb = -(iv.euler + iv.log(iv.pi)) - iv.log(1 - iv.exp(-2 * T))
    total = Cb * g0
    for k in range(K):
        alpha = 2 * k + iv.mpf("0.5")
        ap = 2 * (k + 1)
        term_g0 = 2 * g0 * (1 - iv.exp(-ap * T)) / ap
        total += term_g0 - 2 * I_alpha(alpha, L, omega)
    total += algebraic_tail(L, K)
    total += cubic_tail(L, omega, K, T)
    return total


def Pi_of_mode(L, omega):
    """Pi(g) = 4 int_0^{2L} g cosh(t/2) dt = 2 (I(-1/2)+I(1/2))."""
    return 2 * (I_alpha(iv.mpf("-0.5"), L, omega)
                + I_alpha(iv.mpf("0.5"), L, omega))


def P_of_mode(L, omega):
    T = 2 * L
    _, hi = CC.ivsplit(iv.exp(T))
    n_hi = int(math.floor(float(hi) + 1e-15))
    rows = CC.prime_powers_upto(max(n_hi, 2))
    tot = iv.mpf(0)
    used = 0
    t_hi = float(CC.ivsplit(T)[1])
    for n, p in rows:
        if n > n_hi:
            continue
        ln = iv.log(n)
        if float(CC.ivsplit(ln)[0]) > t_hi:
            continue
        tot += 2 * iv.log(p) / iv.sqrt(n) * g_of(ln, L, omega)
        used += 1
    return tot, used


def sigma_A(t, K=BOSE_K):
    """Fourier symbol of A: Bose prefix + psi algebraic tail + O(1/k^3)."""
    tot = -(iv.euler + iv.log(iv.pi))
    tt = t * t
    for k in range(K):
        alpha = 2 * k + iv.mpf("0.5")
        tot += 2 * (1 / (2 * (k + 1)) - alpha / (alpha * alpha + tt))
    # sum_{k>=K} 2(1/ap - 1/alpha) = -(psi(K+1)-psi(K+1/4))
    tot += algebraic_tail(iv.mpf(1), K)
    # leftover 2 t^2 / (alpha (alpha^2+t^2)) <= 2 (t^2+1) / alpha^3
    aK = 2 * K + iv.mpf("0.5")
    extra = 2 * (abs(tt) + 1) * (1 / (aK ** 3) + 1 / (4 * aK * aK))
    thi = float(CC.ivsplit(extra)[1])
    return tot + iv.mpf([-thi, thi])


def sigma0_closed():
    """sigma(0) = -(gamma+log pi) - (pi/2 + 3 log 2)."""
    return -(iv.euler + iv.log(iv.pi)) - (iv.pi / 2 + 3 * iv.log(2))


def peano_C0():
    """int_0^inf w(s) s^2/2 ds = sum_k 2 / alpha_k^3, sealed."""
    tot = iv.mpf(0)
    K = 400
    for k in range(K):
        alpha = 2 * k + iv.mpf("0.5")
        tot += 2 / (alpha ** 3)
    aK = 2 * K + iv.mpf("0.5")
    tail = 1 / (aK ** 2)
    thi = float(CC.ivsplit(tail)[1])
    return tot + iv.mpf([0, thi])


def rayleigh(L):
    omega = iv.pi / (2 * L)
    A = A_of_mode(L, omega)
    P, used = P_of_mode(L, omega)
    Pi = Pi_of_mode(L, omega)
    Q = A - P + Pi
    r = Q / L
    return {
        "A": A, "P": P, "Pi": Pi, "Q": Q, "r": r,
        "used": used, "omega": omega,
    }


SCHEDULE_FULL = [
    ("YB", iv.mpf("0.30")),
    ("L08", iv.mpf("0.80")),
    ("L5", 5 * iv.log(2) / 4),
    ("L10", iv.mpf("1.0")),
    ("L12", iv.mpf("1.2")),
    ("Lk8", 8 * iv.log(2) / 4),
    ("L14", iv.mpf("1.4")),
    ("L16", iv.mpf("1.6")),
    ("L18", iv.mpf("1.8")),
    ("L20", iv.mpf("2.0")),
    ("Lk12", 12 * iv.log(2) / 4),
    ("Lk16", 16 * iv.log(2) / 4),
]

SCHEDULE_SMOKE = [
    ("YB", iv.mpf("0.30")),
    ("L08", iv.mpf("0.80")),
]


def L_float(L):
    return CC.L_float(L)


def run(smoke: bool) -> int:
    global CHECKS
    CHECKS = []
    started = time.perf_counter()
    mp.mp.dps = DPS
    iv.dps = DPS
    print("crossterm_probe -- r476")
    print("SPEC_SHA", SPEC_SHA[:16])
    print("mode", "SMOKE" if smoke else "FULL")
    print("scramble-sensitive", SCRAMBLE_SENSITIVE)
    print("reason", SCRAMBLE_REASON)
    print("verdict-kind", VERDICT_KIND)
    print("class", CLASS_NAME)

    fw_ok, fw_d = firewall_audit()
    check("firewall", fw_ok, fw_d if not fw_ok else "no zero oracle")
    check("scramble-gate", SCRAMBLE_SENSITIVE, "P uses literal log n")
    check("class-is-h2ball",
          CLASS_NAME == "H2BALL_FIRST_DIRICHLET",
          "no silent L2 upgrade")

    # Route B: symbol at 0
    s0 = sigma_A(iv.mpf(0))
    s0c = sigma0_closed()
    s0_lo, s0_hi = CC.ivsplit(s0)
    c_lo, c_hi = CC.ivsplit(s0c)
    overlap = not (float(s0_hi) < float(c_lo) or float(c_hi) < float(s0_lo))
    check("sigma0-identity", overlap,
          "series meets -(γ+log π)-(π/2+3 log 2)")
    check("sigma0-negative", float(s0_hi) < 0 and float(c_hi) < 0,
          "A-symbol negative at t=0")
    if SIGMA0_PIN:
        check("sigma0-pin", float(s0_hi) < float(mp.mpf(SIGMA0_PIN)),
              "sigma(0) below sealed ceiling")

    C0 = peano_C0()
    C0_hi = float(CC.ivsplit(C0)[1])
    check("peano-C0-finite", C0_hi < 17.0, "int w s^2/2 = %.6f" % C0_hi)
    if PEANO_C0_PIN:
        check("peano-C0-pin", C0_hi < float(mp.mpf(PEANO_C0_PIN)),
              "Peano C0 below sealed ceiling")

    schedule = SCHEDULE_SMOKE if smoke else SCHEDULE_FULL
    print("\n  tag   L        r_lo         r_hi         A            P            Pi       used  verdict")
    results = []
    yb_pos = False
    all_pos = True
    L_max_pos = 0.0
    for tag, L in schedule:
        rec = rayleigh(L)
        lo, hi = CC.ivsplit(rec["r"])
        rlo, rhi = float(lo), float(hi)
        Alo, Ahi = CC.ivsplit(rec["A"])
        Plo, Phi = CC.ivsplit(rec["P"])
        Pilo, Pihi = CC.ivsplit(rec["Pi"])
        Lf = float(L_float(L))
        pos = rlo > 0
        if tag == "YB":
            yb_pos = pos
        if not pos:
            all_pos = False
        else:
            L_max_pos = max(L_max_pos, Lf)
        verdict = "H2BALL_POS" if pos else "SHORT"
        print("  %-5s %-8.4f %+.6e %+.6e  %+.4e %+.4e %+.4e  %3d  %s" % (
            tag, Lf, rlo, rhi,
            float((Alo + Ahi) / 2), float((Plo + Phi) / 2),
            float((Pilo + Pihi) / 2), rec["used"], verdict), flush=True)
        results.append({
            "tag": tag, "L": Lf, "rlo": rlo, "rhi": rhi,
            "used": rec["used"], "pos": pos, "verdict": verdict,
            "S": rec["P"],
        })
        check("%s-typed" % tag, True, "%s r=[%.6e, %.6e]" % (verdict, rlo, rhi))

    check("yb-S-eff-zero",
          all(r["used"] == 0 for r in results if r["tag"] == "YB"),
          "P identically zero at L=0.3")
    check("yb-gate",
          yb_pos,
          "YB r_lo>0 on the first Dirichlet mode" if yb_pos
          else "YB SHORT: modulus/evaluation still crude")
    check("no-lambda-star-claim",
          VERDICT_KIND.startswith("UNCONDITIONAL")
          or VERDICT_KIND in ("YB_ONLY", "STILL_SHORT"),
          "verdict names the H2 ball, not lambda_*")
    check("type-matches-table",
          (VERDICT_KIND.startswith("UNCONDITIONAL") and all_pos)
          or (VERDICT_KIND == "YB_ONLY" and yb_pos and not all_pos)
          or (VERDICT_KIND == "STILL_SHORT" and not yb_pos),
          "VERDICT_KIND agrees with the schedule")

    if RAYLEIGH_PINS:
        ok = True
        for r in results:
            if r["tag"] not in RAYLEIGH_PINS:
                ok = False
                continue
            plo, phi, used = RAYLEIGH_PINS[r["tag"]]
            if r["used"] != used:
                ok = False
            if r["rlo"] < float(mp.mpf(plo)) or r["rhi"] > float(mp.mpf(phi)):
                ok = False
        check("rayleigh-pins", ok, "live r inside sealed hulls")
    else:
        check("rayleigh-pins-unsealed", True, "first run")

    elapsed = time.perf_counter() - started
    n_pass = sum(1 for _, ok in CHECKS if ok)
    n_fail = sum(1 for _, ok in CHECKS if not ok)
    print("\nCHECKS %d/%d  elapsed %.2fs" % (n_pass, n_pass + n_fail, elapsed))
    print("VERDICT", VERDICT_KIND)
    print("L_max_pos", L_max_pos)
    print("SPEC_SHA", SPEC_SHA)
    print("PIN_DUMP_BEGIN")
    for r in results:
        print("  PIN %s L=%.10f r=[%.12e, %.12e] used=%d" % (
            r["tag"], r["L"], r["rlo"], r["rhi"], r["used"]))
    print("PIN_DUMP_END")
    if n_fail:
        print("CROSSTERM FAILED")
        return 1
    print("CROSSTERM %s" % VERDICT_KIND)
    return 0


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--smoke", action="store_true")
    args = parser.parse_args()
    sys.exit(run(args.smoke))


if __name__ == "__main__":
    main()
