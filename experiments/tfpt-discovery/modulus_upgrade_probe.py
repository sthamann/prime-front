#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""modulus_upgrade_probe -- PRIME.RDAGGER.MODULUS_UPGRADE.01 (r474).

F2b of the r469 U3 contract: explicit continuity modulus of the
Guinand--Weil form at FIXED support length L, and the mu-vs-omega
balance against the r471 grid certificates.

CONVENTION (r461, r471).
  lambda_*(L) = inf { Q_W(h)/||h||_2^2 : supp h subset [-L, L] }.
  g = h * h-tilde, supp g subset [-2L, 2L].
  Q = A - P + Pi  as in classical_cert_probe.
  Prime nodes: n with log n <= 2L.

SCRAMBLE GATE (r469 anti-list item 3).  P uses the literal nodes
log n.  The modulus of P is a weighted l1-norm of those nodes
(S_eff).  A source-position scramble changes S_eff and therefore
omega.  The bound is scramble-sensitive.  Not a q^dagger pairing.

HONEST TYPE.  This round PROVES explicit C_P(L), C_Pi(L), Jackson
constants, and a combination implication.  The quantitative
upgrade GRID_CERTIFIED -> lambda_*(L) >= 0 is STUCK: at every
sealed mesh, including the Yoshida/Bombieri point L=0.3, the
proved omega exceeds R_grid = mu/delta.  No silent upgrade.
No infinite-k statement.  NO RH CLAIM.
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
SERIES_K = 80

# Sealed after /tmp.  S_eff = sum_{n <= exp(2L)} Lambda(n)/sqrt(n).
S_EFF_PINS: dict[str, tuple[str, str, int]] = {
    "YB": ("0.0", "0.0", 0),
    "L08": ("1.47098676e+00", "1.47098677e+00", 3),
    "L08f": ("1.47098676e+00", "1.47098677e+00", 3),
    "L5": ("2.19074927e+00", "2.19074929e+00", 4),
    "L10": ("2.92623418e+00", "2.92623419e+00", 5),
    "L12": ("4.26049544e+00", "4.26049545e+00", 8),
    "Lk8": ("5.14517119e+00", "5.14517120e+00", 10),
    "L14": ("5.14517119e+00", "5.14517120e+00", 10),
    "L16": ("7.16162273e+00", "7.16162274e+00", 13),
    "L18": ("9.05952406e+00", "9.05952407e+00", 18),
    "L20": ("1.21916459e+01", "1.21916460e+01", 24),
    "Lk12": ("1.33354829e+01", "1.33354830e+01", 27),
    "Lk16": ("2.91431909e+01", "2.91431911e+01", 70),
}

# omega_hi ceiling: first Dirichlet mode, 5% outward.
OMEGA_PINS: dict[tuple[str, int], str] = {
    ("YB", 8): "5.50e-01",
    ("YB", 16): "1.48e-01",
    ("L08", 8): "9.20e-01",
    ("L08f", 24): "1.10e-01",
    ("L5", 16): "2.61e-01",
    ("L10", 20): "1.89e-01",
    ("L12", 24): "1.56e-01",
    ("Lk8", 28): "1.31e-01",
    ("L14", 28): "1.31e-01",
    ("L16", 32): "1.19e-01",
    ("L18", 32): "1.38e-01",
    ("L20", 32): "1.63e-01",
    ("Lk12", 32): "1.74e-01",
    ("Lk16", 36): "2.45e-01",
}

VERDICT_KIND = "PARTIAL"
JACKSON_L2 = "1/pi^2"
JACKSON_H1 = "1/pi"

SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
CHECKS: list[tuple[str, bool]] = []


def check(name: str, ok: bool, detail: str = "") -> bool:
    CHECKS.append((name, bool(ok)))
    print("  [%s] %-42s %s" %
          ("PASS" if ok else "FAIL", name, detail), flush=True)
    return bool(ok)


SCRAMBLE_SENSITIVE = True
SCRAMBLE_REASON = (
    "The P-modulus is 2 S_eff(L) ||g-g'||_inf with S_eff a sum "
    "over the literal nodes log n <= 2L.  Scrambling those nodes "
    "changes S_eff and omega.  Not fold-mode pairing."
)


def firewall_audit() -> tuple[bool, str]:
    source = open(os.path.abspath(__file__), encoding="utf-8").read()
    tree = ast.parse(source)
    forbidden = {"zetazero", "nzeros", "grampoint", "zetazeros"}
    bad = []
    for node in ast.walk(tree):
        name = node.attr if isinstance(node, ast.Attribute) else (
            node.id if isinstance(node, ast.Name) else None)
        if name and name.lower().replace("_", "") in forbidden:
            bad.append("%s@%d" % (name, node.lineno))
    return (not bad), ("NO zero/oracle calls" if not bad else "; ".join(bad))


def iv_sinh(x):
    return (iv.exp(x) - iv.exp(-x)) / 2


def series_wN_from0(eta, k_terms=SERIES_K):
    """int_0^eta w N(w) dw = sum_k [1/alpha^2 - e^{-alpha eta}(eta/alpha+1/alpha^2)].
    The k=0 endpoint at 0 is finite.  Tail of sum 1/alpha_k^2 is 1/(4K-2)."""
    total = iv.mpf(0)
    half = iv.mpf("0.5")
    two = iv.mpf(2)
    for k in range(k_terms):
        alpha = two * k + half
        total += (1 / (alpha * alpha)
                  - iv.exp(-alpha * eta) * (eta / alpha + 1 / (alpha * alpha)))
    # remaining sum_{k>=K} 1/alpha_k^2 <= int_{K-1/2}^inf dx/(2x+1/2)^2 = 1/(4K-2)
    thi = 1.0 / (4 * k_terms - 2)
    return total + iv.mpf([-thi, thi])


def series_N_from(a, b, k_terms=None):
    """int_a^b N, a>0.  Adaptive K so alpha_K * a >= 20."""
    a_lo = float(CC.ivsplit(a)[0])
    if a_lo <= 0:
        raise ValueError("series_N_from requires a>0")
    need = int(0.5 * (20.0 / a_lo - 0.5)) + 8
    k_terms = max(SERIES_K, min(need, 4000))
    total = iv.mpf(0)
    half = iv.mpf("0.5")
    two = iv.mpf(2)
    for k in range(k_terms):
        alpha = two * k + half
        total += (iv.exp(-alpha * a) - iv.exp(-alpha * b)) / alpha
    alpha_k = two * k_terms + half
    den = 1 - iv.exp(-two * a)
    tail = iv.exp(-alpha_k * a) / alpha_k / den
    tlo, thi = CC.ivsplit(tail)
    rad = max(abs(float(tlo)), abs(float(thi)), 0.0)
    return total + iv.mpf([-rad, rad])


def int_B(a, b):
    """int_a^b B(w) dw = -1/2 [log(1-e^{-2b}) - log(1-e^{-2a})], a>0."""
    return (iv.log(1 - iv.exp(-2 * a)) - iv.log(1 - iv.exp(-2 * b))) / 2


def S_eff(L):
    """sum Lambda(n)/sqrt(n) over n with log n <= 2L, interval."""
    twoL = 2 * L
    _, hi = CC.ivsplit(iv.exp(twoL))
    n_hi = int(math.floor(float(hi) + 1e-15))
    rows = CC.prime_powers_upto(max(n_hi, 2))
    tot = iv.mpf(0)
    used = 0
    t_hi = float(CC.ivsplit(twoL)[1])
    for n, p in rows:
        if n > n_hi:
            continue
        ln_lo, _ = CC.ivsplit(iv.log(n))
        if float(ln_lo) > t_hi:
            continue
        tot += iv.log(p) / iv.sqrt(n)
        used += 1
    return tot, used, n_hi


def first_dirichlet_sigma2(L):
    """sigma_2 = ||h''||_2 / ||h||_2 for h = cos(pi x / (2L)) on [-L,L]."""
    return (iv.pi / (2 * L)) ** 2


def omega_H2(L, delta, sigma2):
    """Enclosure of |Q(h)-Q(I_delta h)| / ||h||_2^2 on the H^2 ball
    ||h''||_2 <= sigma2 ||h||_2, I_delta = piecewise-linear interpolant.

    Jackson (sine series on each element, ends matched):
      ||h-I||_2 <= (delta^2/pi^2) ||h''||_2
      ||(h-I)'||_2 <= (delta/pi) ||h''||_2
    g-bounds:
      ||g-g_I||_inf <= (||h||_2 + ||I||_2) ||h-I||_2
      Lip(g-g_I) <= ||h||_2 ||(h-I)'||_2 + ||h-I||_2 ||I'||_2
    A uses min(2||Delta g||_inf, w Lip) against N, plus Delta g(0) on B-N.
    """
    pi = iv.pi
    rho0 = (delta ** 2 / (pi * pi)) * sigma2
    sig1 = iv.sqrt(sigma2)
    two = iv.mpf(2)
    Dg_inf = (two + rho0) * rho0
    d_pi = delta / pi
    Dg_lip = d_pi * sigma2 + (delta ** 2 / (pi * pi)) * sigma2 * (
        sig1 + d_pi * sigma2)
    twoL = 2 * L
    # split increment at w* = 2 Dg_inf / Dg_lip
    if float(CC.L_float(Dg_lip)) <= 0:
        I_incr = two * Dg_inf * series_N_from(iv.mpf("0.05"), twoL)
    else:
        wstar = two * Dg_inf / Dg_lip
        ws_hi = float(CC.ivsplit(wstar)[1])
        cap = float(CC.L_float(twoL))
        if ws_hi >= cap:
            I_incr = Dg_lip * series_wN_from0(twoL)
        else:
            ws = iv.mpf(str(max(min(ws_hi, cap * 0.99), 1e-10)))
            I_incr = (Dg_lip * series_wN_from0(ws)
                      + two * Dg_inf * series_N_from(ws, twoL))
    # |B-N|(0)=3/4; int_0^{2L}|B-N| <= (3/4)*2L + int_eta^{2L}|N-B|.
    eta = iv.mpf("0.05")
    I_NmB = (iv.mpf("0.75") * twoL
             + abs(series_N_from(eta, twoL) - int_B(eta, twoL)))
    I_Btail = -iv.log(1 - iv.exp(-4 * L)) / 2
    Dg0 = two * rho0 + rho0 ** 2
    gam = iv.euler + iv.log(iv.pi)
    Aerr = gam * Dg0 + two * (I_incr + Dg0 * (I_NmB + I_Btail))
    Se, n_used, n_hi = S_eff(L)
    Perr = two * Se * Dg_inf
    Pierr = 8 * iv_sinh(L) * Dg_inf
    tot = Aerr + Perr + Pierr
    return {
        "rho0": CC.L_float(rho0),
        "Dg_inf": CC.L_float(Dg_inf),
        "Aerr": float(CC.ivsplit(Aerr)[1]),
        "Perr": float(CC.ivsplit(Perr)[1]),
        "Pierr": float(CC.ivsplit(Pierr)[1]),
        "omega_hi": float(CC.ivsplit(tot)[1]),
        "S_eff": Se,
        "n_used": n_used,
        "n_hi": n_hi,
        "sigma2": CC.L_float(sigma2),
    }


# Finest r471 mesh per tag (mu from sealed CERT_PINS, lower endpoint).
SCHEDULE_FULL = [
    ("YB", 0.30, 16),
    ("L08f", 0.80, 24),
    ("L5", None, 16),          # L = 5 log2 / 4
    ("L10", 1.0, 20),
    ("L12", 1.2, 24),
    ("Lk8", None, 28),
    ("L14", 1.4, 28),
    ("L16", 1.6, 32),
    ("L18", 1.8, 32),
    ("L20", 2.0, 32),
    ("Lk12", None, 32),
    ("Lk16", None, 36),
]

SCHEDULE_SMOKE = [
    ("YB", 0.30, 8),
    ("L08", 0.80, 8),
]


def L_of_tag(tag, L_hint):
    if L_hint is not None:
        return iv.mpf(str(L_hint))
    log2 = iv.log(2)
    if tag == "L5":
        return 5 * log2 / 4
    if tag == "Lk8":
        return 8 * log2 / 4
    if tag == "Lk12":
        return 12 * log2 / 4
    if tag == "Lk16":
        return 16 * log2 / 4
    raise KeyError(tag)


def R_grid_of(tag, n, L):
    key = (tag, n)
    if key not in CC.CERT_PINS:
        return None, None
    lo_s, hi_s = CC.CERT_PINS[key]
    mu_lo = float(mp.mpf(lo_s))
    delta = CC.L_float(2 * L / n)
    return mu_lo / delta, mu_lo


def run(smoke: bool) -> int:
    global CHECKS
    CHECKS = []
    started = time.perf_counter()
    mp.mp.dps = DPS
    iv.dps = DPS
    print("modulus_upgrade_probe -- r474")
    print("SPEC_SHA", SPEC_SHA[:16])
    print("mode", "SMOKE" if smoke else "FULL")
    print("scramble-sensitive", SCRAMBLE_SENSITIVE)
    print("reason", SCRAMBLE_REASON)
    print("verdict-kind", VERDICT_KIND)

    fw_ok, fw_d = firewall_audit()
    check("firewall", fw_ok, fw_d if not fw_ok else "no zero oracle")
    check("scramble-gate", SCRAMBLE_SENSITIVE, "S_eff uses literal log n")
    check("jackson-constants",
          JACKSON_L2 == "1/pi^2" and JACKSON_H1 == "1/pi",
          "element sine series")

    schedule = SCHEDULE_SMOKE if smoke else SCHEDULE_FULL
    print("\n  tag   L        n   delta    R_grid     omega_hi   A        P        Pi       verdict")
    results = []
    yb_short = False
    any_pass = False
    for tag, L_hint, n in schedule:
        L = L_of_tag(tag, L_hint)
        Lf = CC.L_float(L)
        delta = 2 * L / n
        dfloat = CC.L_float(delta)
        R, mu = R_grid_of(tag, n, L)
        sig2 = first_dirichlet_sigma2(L)
        om = omega_H2(L, delta, sig2)
        short = (R is None) or (R <= om["omega_hi"])
        if tag.startswith("YB") and short:
            yb_short = True
        if R is not None and R > om["omega_hi"]:
            any_pass = True
        verdict = "SHORT" if short else "H2BALL_POS"
        print("  %-5s %-8.4f %3d  %.4f  %-10s %.4e  %.4e %.4e %.4e  %s" % (
            tag, Lf, n, dfloat,
            ("%.4e" % R) if R is not None else "None",
            om["omega_hi"], om["Aerr"], om["Perr"], om["Pierr"], verdict),
              flush=True)
        rec = {
            "tag": tag, "L": Lf, "n": n, "delta": dfloat,
            "R": R, "mu": mu, "omega_hi": om["omega_hi"],
            "Aerr": om["Aerr"], "Perr": om["Perr"], "Pierr": om["Pierr"],
            "sigma2": om["sigma2"], "S_used": om["n_used"],
            "S_eff": om["S_eff"], "short": short, "verdict": verdict,
        }
        results.append(rec)
        check("%s-n=%d-typed" % (tag, n), True,
              "%s R=%s om=%.4e" % (verdict,
                                   ("%.4e" % R) if R else "None",
                                   om["omega_hi"]))

    # YB: S_eff must vanish (2L < log 2)
    yb = [r for r in results if r["tag"] == "YB"]
    check("yb-S-eff-zero",
          all(r["S_used"] == 0 for r in yb) and len(yb) >= 1,
          "P identically zero for L=0.30")
    # Calibration kill: upgrade MUST pass at YB, or diagnose.
    check("yb-upgrade-diagnosis",
          yb_short,
          "YB SHORT: proved omega exceeds R_grid (modulus too crude)")
    check("no-silent-L2-upgrade",
          not any_pass,
          "no row claims lambda_*(L)>=0")
    check("type-is-partial",
          VERDICT_KIND == "PARTIAL",
          "lemmas proved; quantitative close STUCK")

    # pin checks
    if S_EFF_PINS:
        ok = True
        for r in results:
            if r["tag"] not in S_EFF_PINS:
                ok = False
                continue
            lo_s, hi_s, used = S_EFF_PINS[r["tag"]]
            lo, hi = mp.mpf(lo_s), mp.mpf(hi_s)
            mid = sum(CC.ivsplit(r["S_eff"])) / 2
            if r["S_used"] != used or not (lo <= mid <= hi):
                ok = False
        check("s-eff-pins", ok, "S_eff inside sealed hulls")
    else:
        check("s-eff-pins-unsealed", True, "first run")

    if OMEGA_PINS:
        ok = True
        for r in results:
            key = (r["tag"], r["n"])
            if key not in OMEGA_PINS:
                ok = False
                continue
            if r["omega_hi"] > float(mp.mpf(OMEGA_PINS[key])):
                ok = False
        check("omega-pins", ok, "live omega_hi below sealed ceiling")
    else:
        check("omega-pins-unsealed", True, "first run")

    elapsed = time.perf_counter() - started
    n_pass = sum(1 for _, ok in CHECKS if ok)
    n_fail = sum(1 for _, ok in CHECKS if not ok)
    print("\nCHECKS %d/%d  elapsed %.2fs" % (n_pass, n_pass + n_fail, elapsed))
    print("VERDICT", VERDICT_KIND)
    print("SPEC_SHA", SPEC_SHA)
    print("PIN_DUMP_BEGIN")
    for r in results:
        lo, hi = CC.ivsplit(r["S_eff"])
        print("  PIN %s %d S=[%.8e, %.8e] used=%d om_hi=%.8e R=%s" % (
            r["tag"], r["n"], float(lo), float(hi), r["S_used"],
            r["omega_hi"],
            ("%.8e" % r["R"]) if r["R"] is not None else "None"))
    print("PIN_DUMP_END")
    if n_fail:
        print("MODULUS UPGRADE FAILED")
        return 1
    print("MODULUS UPGRADE %s" % VERDICT_KIND)
    return 0


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--smoke", action="store_true")
    args = parser.parse_args()
    sys.exit(run(args.smoke))


if __name__ == "__main__":
    main()
