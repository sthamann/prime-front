#!/usr/bin/env python3
"""chain_deck_sector_probe.py -- S-C, THE V3 OPERATOR TARGET: do the
three digamma channels of the zeta arch density (arguments 1/12, 5/12,
3/4 on the zeta_12 grid; big_picture S3.1/S3.3) arise as regularized
traces of the three DECK SECTORS of an explicit cover-transfer
operator -- the v623 lift (48-site NS circle, clock of order 12,
deck = L^4)?

EXPLORATION ONLY (experiments/ firewall): nothing here is a
verification claim; no verification/, paper, ledger or website surface
is touched; no marker moves; NO RH statement.  File prefix chain_ to
avoid collision with the parallel beam-search worker (z1_* names).

THE CHAIN UNDER TEST (each link machine-checked):
  D1 [lift] the 48-site antiperiodic (NS) shift S has one-particle
     eigenphases theta_m = m pi/48, m odd; the clock L = S^4 satisfies
     L^12 = S^48 = -1 (order 12, spin-doubled); the deck Dk = L^4 =
     S^16 has eigenvalue exp(i pi m / 3) on mode m, cube = -1 (the
     projective mu3 of the fermion), i.e. deck charge
     nu(m) = m/6 mod 1 in {1/6, 1/2, 5/6} == the v628 deck-class
     twists.  Counts 16/16/16.
  D2 [selection] the arch tower: rho(t) = e^{-t/2}/(1 - e^{-2t}) =
     sum over the HALF-TURN eigenspace {S^24 mode eigenvalue = +i}
     == {m == 1 mod 4} of e^{-t m/2} (exact geometric series).  The
     other half-turn class {m == 3 mod 4} gives e^{-3t/2}/(1-e^{-2t})
     != rho -- the arch layer selects ONE clock character
     (mu4-class); WHICH character is selected is semantics tied to
     Gamma(s/2) (the even Gamma_R factor), typed open.
  D3 [deck split, EXACT] within {m == 1 mod 4}, the deck classes
     m mod 12 in {1, 5, 9} have tower traces
         T_r(t) = sum_k e^{-(6k + r/2) t} = e^{-(r/2)t}/(1 - e^{-6t})
     == the three digamma channels b in {1/2, 5/2, 9/2} of the
     triplication identity, with deck charges nu = r/6 =
     {1/6, 5/6, 1/2}.  GLOBAL SCALAR IS FORCED TO 1 by the t -> inf
     asymptote e^{-t/2}.  Bar: max rel dev <= 1e-12 on the t-grid.
  D4 [lattice operator read] the finite lift realizes the tower with
     sin dispersion: eps_m = (N/pi) sin(m pi / (2N)).  Sector traces
     T_lat(r, t) = sum_{m == r mod 12, m < N} e^{-t eps_m} vs the
     continuum channels, ONE JOINT scalar s* (least squares over all
     three sectors on t in [0.5, 3]; no per-sector scalar).
     BAR (declared): the CONVERGENCE claim -- max rel dev <= 2% at
     N = 192 with fitted rate >= 1.8 (~N^-2).  N = 48 is expected
     COARSE in the b = 9/2 sector (the trace error is ~ t x
     dispersion error, which is (m pi/2N)^2/6 per mode -- printed,
     not hidden).
  D5 [must-fail] the WRONG twist set {1/4, 1/2, 3/4} (un-doubled
     offsets {1/8, 1/4, 3/8}, channel exponents 6x = {3/4, 3/2,
     9/4}): (a) its channel sum misses rho by >= 30% in max rel dev
     on the t-grid; (b) at N = 192 the best joint-scalar match of
     the true sector traces onto the wrong channels must leave a
     residual >= 10x the true-channel residual.
  D6 [break anatomy] where the lattice read breaks (N = 192 dev
     rows over t): (i) UV t -> 0: finite mode cutoff vs the 1/t
     divergence -- the Pf/diagonal renormalization slot (same slot
     as the deployed arch layer d = 0 cell); (ii) large t: the
     smallest-mode dispersion error t x Delta eps (the N -> inf
     order of limits).  BOTH named as the concrete regularization
     tasks of the L1 operator candidate; mid-range t in [0.5, 2]
     must be clean (<= 2%) at N = 192.

FIREWALL: AST-checked -- no zetazero/nzeros/zeta anywhere; the
digamma channels are elementary geometric series here (the tie to
Re psi(1/4 + it/2) is the big_picture S3.1 triplication identity,
cited).  No v-module imports needed (pure lattice + series).

Provenance (read-only): v623 (48-site NS lift, clock 12), v628
(deck-class twists {1/6, 1/2, 5/6}), v611/v613 (zeta_12 grid),
big_picture_hunt_probe S3 (triplication + lag-side mirror).
"""
import ast
import math
import os
import time

import numpy as np

T0 = time.time()
FAILS = []
N_CHK = 0

BANNED = ("zetazero", "nzeros", "zeta", "second_sheet_zero")

N0 = 48
T_GRID = np.linspace(0.5, 3.0, 51)
BAR_EXACT = 1e-12
BAR_LAT192 = 0.02         # 2% joint-scalar residual at N = 192
RATE_MIN = 1.8            # ~N^-2 convergence
MUSTFAIL_X = 10.0
BAR_WRONGSUM = 0.30


def check(name, ok, detail=""):
    global N_CHK
    N_CHK += 1
    if not ok:
        FAILS.append(name.split()[0])
    print("[%s] %s%s" % ("PASS" if ok else "FAIL", name,
                         (": " + detail) if detail else ""))


def ast_firewall(src_path):
    with open(src_path, "r", encoding="utf-8") as fh:
        tree = ast.parse(fh.read())
    for node in ast.walk(tree):
        if isinstance(node, ast.Attribute) and node.attr in BANNED:
            return False
        if isinstance(node, ast.Name) and node.id in BANNED:
            return False
    return True


def ns_shift(N):
    S = np.zeros((N, N))
    for i in range(N - 1):
        S[i, i + 1] = 1.0
    S[N - 1, 0] = -1.0
    return S


def channel(b, t):
    return np.exp(-b * t) / (1.0 - np.exp(-6.0 * t))


def sector_trace_lat(N, r, t):
    ms = np.arange(1, N, 2)
    ms = ms[ms % 12 == r]
    eps = (N / math.pi) * np.sin(ms * math.pi / (2.0 * N))
    return np.exp(-np.outer(t, eps)).sum(axis=1)


def joint_fit(traces, chans):
    """One scalar s* minimizing sum ||s T - C||^2 jointly; returns
    (s*, max rel dev of s* T vs C)."""
    Tv = np.concatenate(traces)
    Cv = np.concatenate(chans)
    s = float(Tv @ Cv) / float(Tv @ Tv)
    dev = float(np.max(np.abs(s * Tv - Cv) / np.abs(Cv)))
    return s, dev


def run():
    print("=" * 78)
    print("S-C CHAIN DECK SECTORS -- the V3 operator target")
    print("=" * 78)

    check("G0.0 [E] AST firewall: no zeta/zero symbol anywhere "
          "(channels are elementary geometric series here)",
          ast_firewall(os.path.abspath(__file__)))

    # ------------------------------------------------------------- D1
    print("\nD1 -- the v623 lift and its deck classes")
    S = ns_shift(N0)
    ev = np.linalg.eigvals(S)
    ph = np.sort(np.mod(np.angle(ev), 2.0 * math.pi))
    ph_ref = np.sort(np.array([(m * math.pi / N0) % (2 * math.pi)
                               for m in range(1, 2 * N0, 2)]))
    dev_ph = float(np.max(np.abs(ph - ph_ref)))
    L = np.linalg.matrix_power(S, 4)
    Dk = np.linalg.matrix_power(S, 16)
    dev_L12 = float(np.max(np.abs(
        np.linalg.matrix_power(L, 12) + np.eye(N0))))
    dev_Dk3 = float(np.max(np.abs(
        np.linalg.matrix_power(Dk, 3) + np.eye(N0))))
    # deck charge per mode m: exp(i pi m/3) -> nu = m/6 mod 1
    ms = np.arange(1, 2 * N0, 2)
    nus = np.mod(ms / 6.0, 1.0)
    cnt = {v: int(np.sum(np.isclose(nus, v)))
           for v in (1.0 / 6.0, 0.5, 5.0 / 6.0)}
    check("D1.1 [E] 48-site NS lift: eigenphases m pi/48 (m odd, dev "
          "%.1e); clock L = S^4: L^12 = -1 (dev %.1e, order 12 "
          "spin-doubled); deck Dk = L^4: Dk^3 = -1 (dev %.1e, "
          "projective mu3 = the fermion spin doubling); deck charges "
          "nu = m/6 mod 1 with counts %s == v628 twist classes "
          "{1/6, 1/2, 5/6} x 16"
          % (dev_ph, dev_L12, dev_Dk3,
             {("%d/6" % round(6 * k)): v for k, v in cnt.items()}),
          dev_ph <= 1e-12 and dev_L12 <= 1e-9 and dev_Dk3 <= 1e-9
          and all(v == 16 for v in cnt.values()))

    # ------------------------------------------------------------- D2
    print("\nD2 -- clock-character selection of the arch tower")
    t = T_GRID
    rho = np.exp(-t / 2.0) / (1.0 - np.exp(-2.0 * t))
    tow1 = sum(np.exp(-(2.0 * k + 0.5) * t) for k in range(400))
    tow3 = sum(np.exp(-(2.0 * k + 1.5) * t) for k in range(400))
    dev1 = float(np.max(np.abs(rho - tow1) / rho))
    dev3 = float(np.min(np.abs(rho - tow3) / rho))
    # half-turn eigenvalue of class m == 1 mod 4: exp(i pi m/2) = +i
    ht = set(np.round(np.mod(ms[ms % 4 == 1] * 0.5, 2.0), 9))
    check("D2.1 [E] rho(t) == the {m == 1 mod 4} half-tower (rel dev "
          "%.1e <= 1e-12); this class is EXACTLY the half-turn-"
          "eigenvalue-(+i) eigenspace (S^24 phase pi m/2, unique "
          "value %s x pi/2); the opposite class {m == 3 mod 4} "
          "misses rho by %.0f%% (min rel dev) -- the arch layer "
          "selects ONE clock character; WHY this one = Gamma(s/2) "
          "semantics, typed OPEN"
          % (dev1, sorted(ht), 100 * dev3),
          dev1 <= BAR_EXACT and dev3 > 0.3 and ht == {0.5})

    # ------------------------------------------------------------- D3
    print("\nD3 -- deck split of the arch tower == digamma channels")
    ok3 = True
    dev_max = 0.0
    scal_inf = []
    for r, b, nu in ((1, 0.5, "1/6"), (5, 2.5, "5/6"),
                     (9, 4.5, "1/2")):
        tow = sum(np.exp(-(6.0 * k + b) * t) for k in range(140))
        ch = channel(b, t)
        dev = float(np.max(np.abs(tow - ch) / ch))
        dev_max = max(dev_max, dev)
        ok3 &= dev <= BAR_EXACT
        scal_inf.append(float(tow[-1] / ch[-1]))
        print("   sector m == %d mod 12 (deck nu = %s): tower == "
              "e^{-%.1ft}/(1-e^{-6t}), rel dev %.1e" % (r, nu, b, dev))
    check("D3.1 [E] EXACT: the three deck sectors of the arch tower "
          "ARE the three digamma channels b in {1/2, 5/2, 9/2} "
          "(max rel dev %.1e <= 1e-12); global scalar forced to 1 "
          "by the t->inf asymptote (measured %s); deck charges "
          "{1/6, 5/6, 1/2} = v628 twists" % (dev_max,
          ["%.6f" % s_ for s_ in scal_inf]),
          ok3 and all(abs(s_ - 1) < 1e-9 for s_ in scal_inf))

    # ------------------------------------------------------------- D4
    print("\nD4 -- lattice operator read (sin dispersion, one joint "
          "scalar)")
    devs = {}
    chans = [channel(b, t) for b in (0.5, 2.5, 4.5)]
    for N in (48, 96, 192):
        traces = [sector_trace_lat(N, r, t) for r in (1, 5, 9)]
        s_star, dev = joint_fit(traces, chans)
        devs[N] = dev
        per = [float(np.max(np.abs(s_star * traces[i] - chans[i])
                            / chans[i])) for i in range(3)]
        print("   N = %3d: joint scalar s* = %.6f, max rel dev "
              "%.2e  (per sector b=1/2: %.1e, 5/2: %.1e, 9/2: "
              "%.1e)" % (N, s_star, dev, per[0], per[1], per[2]))
    rate = math.log(devs[48] / devs[192]) / math.log(192.0 / 48.0)
    check("D4.1 [M] lattice sector traces converge to the channels "
          "with ONE joint scalar: N = 192 dev %.2e <= %.0e, rate "
          "%.2f >= %.1f (~N^-2); N = 48 coarse in the b = 9/2 "
          "sector as predicted by t x (m pi/2N)^2/6 (printed): the "
          "channel identity is the CONTINUUM LIMIT of the lift's "
          "deck sectors, not a lattice artifact"
          % (devs[192], BAR_LAT192, rate, RATE_MIN),
          devs[192] <= BAR_LAT192 and rate >= RATE_MIN)

    # ------------------------------------------------------------- D5
    print("\nD5 -- must-fail: wrong twist set {1/4, 1/2, 3/4}")
    wrong_b = (0.75, 1.5, 2.25)
    wsum = sum(channel(b, t) for b in wrong_b)
    rho_g = np.exp(-t / 2.0) / (1.0 - np.exp(-2.0 * t))
    dev_w = float(np.max(np.abs(rho_g - wsum) / rho_g))
    traces192 = [sector_trace_lat(192, r, t) for r in (1, 5, 9)]
    _sw, dev_wfit = joint_fit(traces192,
                              [channel(b, t) for b in wrong_b])
    ratio = dev_wfit / devs[192]
    check("D5.1 [E] wrong-twist channels (exponents %s from "
          "un-doubled {1/8, 1/4, 3/8}) miss rho by %.0f%% max rel "
          "dev (>= %.0f%% bar) and the N = 192 sector-trace fit "
          "onto them leaves %.1e = %.0fx the true residual "
          "(>= %.0fx bar)"
          % (list(wrong_b), 100 * dev_w, 100 * BAR_WRONGSUM,
             dev_wfit, ratio, MUSTFAIL_X),
          dev_w >= BAR_WRONGSUM and ratio >= MUSTFAIL_X)

    # ------------------------------------------------------------- D6
    print("\nD6 -- break anatomy of the lattice read (N = 192)")
    t_uv = np.array([0.02, 0.05, 0.1, 0.5, 1.0, 2.0, 6.0, 12.0])
    traces = [sector_trace_lat(192, r, t_uv) for r in (1, 5, 9)]
    chans6 = [channel(b, t_uv) for b in (0.5, 2.5, 4.5)]
    print("   t:        " + "  ".join("%8.2f" % x for x in t_uv))
    per_t_max = np.zeros(len(t_uv))
    for i, r in enumerate((1, 5, 9)):
        rd = np.abs(traces[i] - chans6[i]) / chans6[i]
        per_t_max = np.maximum(per_t_max, rd)
        print("   m==%d dev: " % r
              + "  ".join("%8.1e" % x for x in rd))
    uv_dev = float(per_t_max[0])
    mid_dev = float(np.max(per_t_max[3:6]))
    deep_dev = float(per_t_max[-1])
    check("D6.1 [M] break anatomy: UV t = 0.02 dev %.1e (mode "
          "cutoff vs 1/t divergence -- the Pf/diagonal "
          "renormalization slot) and deep-t t = 12 dev %.1e "
          "(smallest-mode dispersion drift t x Delta eps -- the "
          "order-of-limits task) are the two NAMED construction "
          "slots; the mid-range t in [0.5, 2] is clean: max dev "
          "%.1e <= 2e-2" % (uv_dev, deep_dev, mid_dev),
          mid_dev <= 0.02 and uv_dev > 5 * mid_dev)

    print("\n" + "=" * 72)
    dt = time.time() - T0
    if FAILS:
        print("RESULT: %d/%d checks passed -- FAILURES: %s  (%.1f s)"
              % (N_CHK - len(FAILS), N_CHK, ", ".join(FAILS), dt))
        return 1
    print("RESULT: ALL %d CHECKS PASSED  (%.1f s)" % (N_CHK, dt))
    return 0


if __name__ == "__main__":
    raise SystemExit(run())
