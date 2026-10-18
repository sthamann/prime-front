"""v666 -- PRIME.TURINGCERT.01: SLICE B of the RH-criteria scan -- the
COMPLETENESS CERTIFICATE of the loaded zero comb via the Riemann-von
Mangoldt counting formula and Turing's integral refinement.  This
certifies the shared data premise of ALL comb-reading modules (v589
convention, v665 routes): the loaded list is complete below
gamma_max -- no zero is missing from the comb.

THE CERTIFICATE.  With the Riemann-Siegel theta function (mpmath
siegeltheta) the exact counting formula reads

    N(T) = theta(T)/pi + 1 + S(T),

with the cited band |S(T)| <= S_BOUND = 2.5 at these heights
(empirically |S| < 1.1 below t ~ 3e3; 2.5 is the conservative band
the task prescribes).  If the comb (first N_ZEROS zeros, gamma_max ~
2.5e3, shared cache with keiper_li_probe) is COMPLETE, then at every
midpoint m_k between consecutive comb zeros

    dev_k := k - (theta(m_k)/pi + 1)  =  S(m_k),   |dev_k| <= S_BOUND,

whereas a MISSING or DOUBLED zero shifts dev_k by -+1 PERSISTENTLY for
all k beyond it.  The probe checks (i) the full midpoint ladder (every
gap, N_ZEROS - 1 rungs) plus a display T-ladder up to gamma_max,
(ii) pairwise separation (no doubles), (iii) TURING'S REFINEMENT: the
integral criterion on three sample intervals [t1, t2] with
t1 > 168 pi,

    |int_{t1}^{t2} S(t) dt| <= LEHMAN_A + LEHMAN_B log(t2/(2 pi))
                              (Turing 1953 / Lehman 1970),

where int S is computed EXACTLY from the comb (N piecewise constant:
int N dt = sum_k k (gamma_{k+1} - gamma_k); int theta by quadrature).
A persistent unit offset over an interval of length L contributes ~L
to the integral and violates the O(log) bound LOUDLY -- this is what
makes the certificate sharp where the pointwise 2.5-band is not.

MUST-FAIL controls: (a) drop one interior zero, (b) duplicate one
zero: both move the mean midpoint deviation by ~1 and blow the Turing
integral by two orders of magnitude above the Lehman bound.

FIREWALL: no verification/ imports; NO RH statement (the certificate
says "the loaded list is exactly the first N_ZEROS zeros up to the
cited S-band and Turing bound", nothing more); the zero-side data
are DIAGNOSTIC per the declared exception of the zero-comb line.
Zero data: mpmath zetazero (dps 15) via the shared committed cache
experiments/tfpt-discovery/zero_comb_cache_n2000.json.  Verdict
enums (frozen): TURING-COMPLETE-BAND (all rungs inside the band, all
Turing integrals inside the Lehman bound, controls break loudly),
TURING-DISCREPANCY (a band or integral check fails), MIXED (only a
control fails to break).  Python-only, counted per GATE.WOLFRAM.02.

PROVENANCE: discovery probe turing_cert_probe.py (2026-08-02, 6/6,
verdict TURING-COMPLETE-BAND).
"""
import json
import math
import os
import time

from mpmath import mp, mpf, zetazero, siegeltheta

T0 = time.time()
FAILS = []
N_CHK = 0

HERE = os.path.dirname(os.path.abspath(__file__))
# shared zero-comb cache: committed in experiments/tfpt-discovery/
# (repo tree); fall back to a local copy next to this module, else
# rebuild locally (~1 h of zetazero calls).
_REPO_CACHE = os.path.join(os.path.dirname(HERE), "experiments",
                           "tfpt-discovery",
                           "zero_comb_cache_n2000.json")
_LOCAL_CACHE = os.path.join(HERE, "zero_comb_cache_n2000.json")
CACHE = _REPO_CACHE if os.path.exists(_REPO_CACHE) else _LOCAL_CACHE

# ---------------- declared constants (before any number) ----------------
N_ZEROS = 2000            # the loaded comb (shared with keiper_li_probe)
DPS_ZEROS = 15            # zero precision of the cache (declared)
DPS_WORK = 30             # working precision (theta, quadrature)
S_BOUND = 2.5             # cited |S(T)| band at these heights (task)
LEHMAN_A = 2.30           # |int_{t1}^{t2} S dt| <= A + B log(t2/2pi)
LEHMAN_B = 0.128          # (Turing 1953, constants Lehman 1970)
T1_MIN = 168 * math.pi    # validity floor t1 > 168 pi ~ 527.8
TURING_IVALS = ((350, 900), (900, 1450), (1450, 2000))  # index pairs
LADDER_RUNGS = 12         # display T-ladder size
DROP_IDX = 1000           # must-fail (a): drop this zero (1-based)
DUP_IDX = 1500            # must-fail (b): duplicate this zero
BAR_MUT_OFFSET = 0.9      # controls must move the mean deviation >= this
BAR_MUT_TURING = 50.0     # controls must exceed the Lehman bound by >=


def check(name, ok, detail=""):
    global N_CHK
    N_CHK += 1
    if not ok:
        FAILS.append(name.split()[0])
    print("[%s] %s%s" % ("PASS" if ok else "FAIL", name,
                         (": " + detail) if detail else ""))


def load_or_build_comb():
    if os.path.exists(CACHE):
        with open(CACHE, "r", encoding="utf-8") as fh:
            data = json.load(fh)
        if data["n_zeros"] == N_ZEROS and data["dps"] == DPS_ZEROS:
            return [mpf(g) for g in data["gammas"]], data
    mp.dps = DPS_ZEROS
    t0 = time.time()
    gam = []
    for k in range(1, N_ZEROS + 1):
        gam.append(zetazero(k).imag)
        if k % 200 == 0:
            print("   ... zetazero %d/%d (%.0f s)"
                  % (k, N_ZEROS, time.time() - t0))
    data = dict(n_zeros=N_ZEROS, dps=DPS_ZEROS,
                generator="mpmath.zetazero",
                gammas=[mp.nstr(g, DPS_ZEROS) for g in gam])
    with open(CACHE, "w", encoding="utf-8") as fh:
        json.dump(data, fh)
    return [mpf(mp.nstr(g, DPS_ZEROS)) for g in gam], data


def nbar(t):
    """The smooth Riemann-von Mangoldt count theta(t)/pi + 1."""
    return siegeltheta(t) / mp.pi + 1


def midpoint_devs(gammas):
    """dev_k = k - Nbar(m_k) at every midpoint of consecutive zeros;
    equals S(m_k) iff the list is the complete initial zero list."""
    out = []
    for k in range(len(gammas) - 1):
        m = (gammas[k] + gammas[k + 1]) / 2
        out.append(float((k + 1) - nbar(m)))
    return out


def turing_integral(gammas, i_lo, i_hi):
    """Exact int_{gamma_{i_lo}}^{gamma_{i_hi}} S(t) dt for the comb
    (1-based indices): int N dt piecewise minus int Nbar dt."""
    t1, t2 = gammas[i_lo - 1], gammas[i_hi - 1]
    int_N = mp.fsum((k + 1) * (gammas[k + 1] - gammas[k])
                    for k in range(i_lo - 1, i_hi - 1))
    int_Nbar = mp.quad(nbar, [t1, (t1 + t2) / 2, t2])
    return float(int_N - int_Nbar), float(t1), float(t2)


def lehman_bound(t2):
    return LEHMAN_A + LEHMAN_B * math.log(t2 / (2 * math.pi))


def run():
    global N_CHK, FAILS
    N_CHK = 0
    FAILS = []
    print("=" * 78)
    print("TURING CERTIFICATE -- completeness of the zero comb via "
          "N(T) = theta(T)/pi + 1 + S(T)")
    print("=" * 78)

    # ============================================================== T0
    print("\nT0 -- the loaded comb, pairwise separation")
    gam, meta = load_or_build_comb()
    mp.dps = DPS_WORK
    gam = [mpf(g) for g in gam]
    gmax = float(gam[-1])
    gaps = [float(gam[k + 1] - gam[k]) for k in range(N_ZEROS - 1)]
    min_gap = min(gaps)
    check("T0.1 comb: %d zeros from %s (dps %d), gamma_1 = %s, "
          "gamma_max = %.6f, strictly increasing with min gap %.6f > 0"
          " (no doubles at cache resolution ~1e-13)"
          % (N_ZEROS, meta["generator"], DPS_ZEROS,
             mp.nstr(gam[0], 12), gmax, min_gap),
          len(gam) == N_ZEROS and min_gap > 1e-6
          and abs(float(gam[0]) - 14.134725141734693) < 1e-9)

    # ============================================================== T1
    print("\nT1 -- the N(T) band certificate (every gap + display "
          "ladder)")
    devs = midpoint_devs(gam)
    max_dev = max(abs(d) for d in devs)
    mean_dev = sum(devs) / len(devs)
    k_worst = max(range(len(devs)), key=lambda k: abs(devs[k]))
    print("   display ladder (T, N_comb(T), theta/pi + 1, S_est):")
    for j in range(LADDER_RUNGS):
        T = 20.0 * (gmax / 20.0) ** (j / (LADDER_RUNGS - 1.0))
        n_comb = sum(1 for g in gam if float(g) <= T)
        nb = float(nbar(T))
        print("     T = %9.2f   N = %4d   Nbar = %9.3f   S_est = %+ .3f"
              % (T, n_comb, nb, n_comb - nb))
    check("T1.1 [CERTIFICATE] every one of the %d midpoint rungs sits "
          "inside the cited S-band: max |k - theta(m_k)/pi - 1| = "
          "%.4f < %.1f (worst at k = %d, m ~ %.1f), mean deviation "
          "%+.4f ~ 0 -- no missing and no doubled zero anywhere below "
          "gamma_max = %.1f at band resolution"
          % (len(devs), max_dev, S_BOUND, k_worst + 1,
             float((gam[k_worst] + gam[k_worst + 1]) / 2), mean_dev,
             gmax),
          max_dev < S_BOUND and abs(mean_dev) < 0.5)
    n_end = sum(1 for g in gam if float(g) <= gmax)
    s_end = n_end - float(nbar(gmax))
    check("T1.2 endpoint: N_comb(gamma_max) = %d vs theta/pi + 1 = "
          "%.3f (S_est = %+.3f inside the band): the comb is the "
          "COMPLETE initial segment up to its declared end"
          % (n_end, float(nbar(gmax)), s_end), abs(s_end) < S_BOUND)

    # ============================================================== T2
    print("\nT2 -- Turing's refinement: the integral criterion")
    tur_rows = []
    ok_t2 = True
    for i_lo, i_hi in TURING_IVALS:
        val, t1, t2 = turing_integral(gam, i_lo, i_hi)
        bd = lehman_bound(t2)
        ok = (t1 > T1_MIN) and abs(val) <= bd
        ok_t2 = ok_t2 and ok
        tur_rows.append((i_lo, i_hi, t1, t2, val, bd))
        print("     [gamma_%d, gamma_%d] = [%8.2f, %8.2f]: "
              "int S dt = %+.4f   bound %.3f   %s"
              % (i_lo, i_hi, t1, t2, val, bd,
                 "OK" if ok else "VIOLATED"))
    check("T2.1 [Turing] |int S dt| <= %.2f + %.3f log(t2/2pi) on all "
          "%d sample intervals (t1 > 168 pi = %.1f; worst usage "
          "%.3f of the bound): the band certificate is REFINED -- a "
          "persistent unit offset (one missing/extra zero) would "
          "contribute ~interval length >> bound"
          % (LEHMAN_A, LEHMAN_B, len(TURING_IVALS), T1_MIN,
             max(abs(v) / b for *_, v, b in tur_rows)),
          ok_t2)

    # ============================================================== T3
    print("\nT3 -- MUST-FAIL controls (the certificate has teeth)")
    # (a) drop one interior zero
    gam_drop = gam[:DROP_IDX - 1] + gam[DROP_IDX:]
    devs_d = midpoint_devs(gam_drop)
    mean_tail_d = (sum(devs_d[DROP_IDX - 1:])
                   / len(devs_d[DROP_IDX - 1:]))
    iv = next((a, b) for a, b in TURING_IVALS if a <= DROP_IDX <= b)
    val_d, t1_d, t2_d = turing_integral(
        gam_drop, iv[0], iv[1] - 1)
    bd_d = lehman_bound(t2_d)
    # (b) duplicate one zero
    gam_dup = (gam[:DUP_IDX] + [gam[DUP_IDX - 1] + mpf("1e-9")]
               + gam[DUP_IDX:])
    devs_u = midpoint_devs(gam_dup)
    mean_tail_u = (sum(devs_u[DUP_IDX:]) / len(devs_u[DUP_IDX:]))
    iv2 = next((a, b) for a, b in TURING_IVALS if a <= DUP_IDX <= b)
    val_u, t1_u, t2_u = turing_integral(gam_dup, iv2[0], iv2[1] + 1)
    bd_u = lehman_bound(t2_u)
    check("T3.1 [must-break, drop] removing zero #%d shifts the mean "
          "midpoint deviation beyond it to %+.4f (>= %.1f in "
          "magnitude) and blows the Turing integral on [%.0f, %.0f] "
          "to %+.1f = %.0f x the Lehman bound %.2f"
          % (DROP_IDX, mean_tail_d, BAR_MUT_OFFSET, t1_d, t2_d,
             val_d, abs(val_d) / bd_d, bd_d),
          abs(mean_tail_d) >= BAR_MUT_OFFSET
          and abs(val_d) >= BAR_MUT_TURING * bd_d)
    check("T3.2 [must-break, double] duplicating zero #%d shifts the "
          "mean midpoint deviation to %+.4f and blows the Turing "
          "integral on [%.0f, %.0f] to %+.1f = %.0f x the bound %.2f "
          "-- missing AND doubled zeros are both loud"
          % (DUP_IDX, mean_tail_u, t1_u, t2_u, val_u,
             abs(val_u) / bd_u, bd_u),
          abs(mean_tail_u) >= BAR_MUT_OFFSET
          and abs(val_u) >= BAR_MUT_TURING * bd_u)

    # ============================================================== verdict
    if not FAILS:
        VERDICT = "TURING-COMPLETE-BAND"
    elif any(f.startswith("T1") or f.startswith("T2") for f in FAILS):
        VERDICT = "TURING-DISCREPANCY"
    else:
        VERDICT = "MIXED"
    print("\nVERDICT: %s -- %d zeros certified complete up to "
          "gamma_max = %.1f: max midpoint |S_est| = %.4f < %.1f, all "
          "%d Turing integrals inside the Lehman bound, controls "
          "break by > %.0f x" % (VERDICT, N_ZEROS, gmax, max_dev,
                                 S_BOUND, len(TURING_IVALS),
                                 BAR_MUT_TURING))
    print("checks: %d, failures: %d %s" % (N_CHK, len(FAILS),
                                           FAILS or ""))
    print("elapsed: %.1f s" % (time.time() - T0))
    print("FIREWALL: shared zetazero cache (dps %d, diagnostic zero-"
          "side line); certificate = completeness of the loaded "
          "list, NO RH statement" % DPS_ZEROS)
    print("--- v666_turing_cert: %d passed, %d failed ---"
          % (N_CHK - len(FAILS), len(FAILS)))
    return len(FAILS)


if __name__ == "__main__":
    raise SystemExit(1 if run() else 0)
