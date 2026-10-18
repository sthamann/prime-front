#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""arithmetic_lift_race_probe -- E8.WALL.LIFTRACE.01: the arithmetic
lift written explicitly as a weighted prime(-power) sum, and raced
against the h^-2 margin demand.  Answer measured here: THE RACE HAS
NO WINNER -- along the true critical direction the lift and the
demand are two O(1) legs that grow at the SAME rate (~0.077 per unit
depth alpha, slope difference ~1e-4), and the wall margin is their
ever-sharpening difference, falling like h^-1.9 while both legs grow.

EXPLORATION ONLY (experiments/): no ledger row, no paper edit, no
.md, nothing outside experiments/.  NO RH CLAIM in either direction.
Read-only import of the deployed v563 tables (the v881/v882 pattern).
Frozen (spec + sha256) before the frozen run; the smoke measurements
that shaped the wards are declared below, including one refuted naive
expectation -- recording dead guesses is part of the method.

THE QUESTION (continuation of E8.WALL.CRITDIR.01, the named object
(a) of note CII, user-approved): CII measured that the critical
direction is CLASSICAL (computable from the prime-free smooth model,
overlap 0.88..0.99) and only its VALUE is arithmetic.  This probe
writes that value down explicitly.  Along a FIXED direction g the
atom energy of the deployed wall is EXACTLY a weighted prime(-power)
sum, E_at(g) = sum_n mu_n q_g(u_n) with mu_n = 2 Lambda(n)/sqrt(n)
and an explicit per-unit-mass weight q_g(u) (the energy of a single
unit atom at position u, closed two-point read of the T163 lag
weights).  The ARITHMETIC LIFT is that sum minus its PNT-continuum
counterpart -- a smoothed Chebyshev-psi-vs-PNT comparison in the
window -- and the MARGIN DEMAND is what the smooth world leaves
uncovered along g.  Exactly: lam-along-g = lift - demand.  The frozen
race question: does the h^-2 margin decay come from the demand
growing faster, the lift growing slower, or both tracking each other
with a shrinking residual?

SMOKE-RUN DISCLOSURE (2026-08-10, before freezing): a smoke run on
the full 67-rung ladder shaped every ward below.  Two smoke findings
are frozen as such: (i) a naive expectation is REFUTED -- q_g is a
LAG (autocorrelation) read, NOT a position read, so an atom placed at
the mode's interior NODE u* does NOT contribute ~0 (measured
|q_g(u*)| = 0.08..0.44 of max|q_g| on the subset); the zero-weight
control is therefore placed at a zero of q_g itself, where the
DIRECT single-atom matrix energy must vanish; (ii) on exactly one
rung (kz = 97) the smooth model's two lowest branches CROSS: its
bottom eigenvector is a head-localized object (overlap 1e-4 with the
true mode) while its SECOND eigenvector carries the classical
direction (overlap 0.972) -- recorded as a branch crossing, wards on
the smooth-direction leg formulated accordingly.  Smoke numbers:
lift = 0.0769 alpha + 0.809 (R2 0.888), demand = 0.0770 alpha + 0.809
(R2 0.888), residual = lam_min in 4.0e-6..4.3e-4 ~ h^-1.93,
lift/sigma_fluct 0.31..0.53, half of the lift accumulated below
u/(2 alpha) = 0.04, identities at 4e-13 or better.

FROZEN CLAIMS (2026-08-10, frozen + SHA-hashed before the frozen
run):

 S1  THE EXACT WEIGHT IDENTITY.  For g in {v (true soft mode),
     v_sm (smooth-model bottom mode)} on every faithful rung:
     (a) matrix = lag read: g.K_at.g equals c_at.W_g (T163 weights)
         to 1e-12 relative on the subset rungs, and the fast
         two-point read q_g(u) equals the DIRECT single-atom matrix
         energy g.K_{atom(u,1)}.g to 1e-10 relative on five sample
         atoms of kz = 13;
     (b) the weighted-sum identity sum_n mu_n q_g(u_n) = E_at(g)
         holds to 1e-10 relative on ALL faithful rungs and BOTH
         directions, and the same identity with the PNT continuum
         grid (6000 cells, masses 2 e^{u/2} du) reproduces
         E_at_smooth(g) to 1e-10;
     (c) THE WEIGHT PROFILE (direction v, subset): q_g(0+) =
         -||g||^2 = -1 exactly (ward |q(0+) + 1| < 0.01); the
         profile has 1..6 interior sign changes (smoke: 3 on all
         seven); its 5%-support covers 0.5..0.9 of the window
         (smoke: 0.68..0.78); its largest magnitude sits at the
         u -> 0 lag end where NO atom lives (first atom at log 2) --
         the largest weight an actual atom can collect is recorded;
     (d) FROZEN REFUTATION of the position reading: an atom at the
         mode's interior node u* does NOT get zero weight --
         |q_g(u*)|/max|q_g| >= 0.03 on every subset rung (smoke:
         0.08..0.44).  q_g reads the folded autocorrelation of g at
         lag u, not g(u)^2.
     Fail => IDENTITY-BROKEN.

 S2  THE LIFT, THE DEMAND, AND THE RACE.  Per rung and direction g:
     demand = -(E_ar(g) + E_at_smooth(g)) (what the smooth world
     leaves uncovered along g), lift = E_at_true(g) - E_at_smooth(g)
     (what the actual prime placement adds over the PNT continuum).
     (a) EXACT BOOKKEEPING on all faithful rungs: lift - demand =
         lam_min for g = v (1e-10 relative to the E_at scale);
         lift - demand = RQ(v_sm) for g = v_sm (same ward); and
         demand(v_sm) = -lam_min(K_smooth) EXACTLY (v_sm is the
         smooth model's own ground direction);
     (b) both legs are POSITIVE on every rung and both directions:
         lift > 0 and demand > 0 everywhere (smoke: lift 0.95..4.6,
         demand 0.94..1.49);
     (c) THE RACE (direction v, frozen answer BOTH-TRACK): linear
         fits over the ladder give slope(lift) and slope(demand)
         both in [0.02, 0.2] per unit alpha with R2 >= 0.7 each
         (smoke: 0.0769/0.0770, R2 0.888), slope difference
         |d slope| <= 0.005 (smoke ~1e-4), max residual <= 1e-3, and
         residual ~ h^p with p in [-2.5, -1.5] (smoke -1.93).  The
         h^-2 margin decay is NOT "demand outruns lift" and NOT
         "lift stalls" -- both legs grow together and the margin is
         their ever-sharpening difference;
     (d) the smooth-direction leg is recorded honestly: fits along
         v_sm are contaminated by the kz = 97 branch crossing (at
         most 2 rungs may have bottom-branch overlap < 0.8, and on
         each such rung one of the four lowest smooth eigenvectors
         must carry overlap >= 0.8 with the true mode).
     Fail => RACE-BROKEN.

 S3  THE PSI-ERROR READING.  lift = sum_n mu_n q_g(u_n) - integral
     2 e^{u/2} q_g(u) du is a smoothed psi-vs-PNT comparison against
     the compactly supported weight q_g.
     (a) WHERE IT ACCUMULATES (audit rungs kz = 13, 40, direction
         v): the cumulative lift profile reaches half its final
         value below u/(2 alpha) = 0.15 (smoke: 0.039/0.029), and
         the head n <= 100 carries a fraction in [0.5, 1.5] of the
         total lift (smoke: 1.06/0.88) -- the lift is HEAD-CARRIED,
         the same small-prime seat as note CI's sensitivity audit;
     (b) THE SCALE TYPE (all faithful rungs, direction v): in units
         of the naive sqrt-size fluctuation scale sigma_g =
         (sum_n mu_n^2 q_g(u_n)^2)^{1/2}, the lift sits at
         lift/sigma_g in [0.15, 0.9] (smoke: 0.31..0.53, median
         0.38) -- the actual prime placement delivers a
         SUB-GENERIC-SCALE lift, not a conspiratorial many-sigma
         alignment.
     Fail => PSI-BROKEN.

 C   CONTROLS (must fire):
     C1 SCRAMBLE (seeded, rungs 13/40): with atom positions
        randomized in (0, 2 alpha], the weighted-sum identity STILL
        holds to 1e-10 (it is linear algebra, not arithmetic), but
        the lift flips: lift_scrambled < 0 and lift_scrambled -
        demand < 0 -- positivity is destroyed, the lift is a
        property of the actual prime placement;
     C2 ZERO-WEIGHT PLACEMENT (kz = 13): a unit atom placed at the
        first interior zero u0 of q_g (piecewise-linear read, exact
        cell solve) has DIRECT single-atom matrix energy
        |g.K_{atom(u0,1)}.g| <= 1e-9 -- the weight profile is the
        true influence function of the wall along g;
     C3 FIREWALL: AST scan of this file for the deployed banned
        identifiers (zetazero, nzeros, primerange, isprime, primepi,
        nextprime, prevprime); none may appear as a call;
     C4 NO-RH-CLAIM: the verdict asserts nothing about RH's truth.

VERDICT (frozen precedence): IDENTITY-BROKEN / RACE-BROKEN /
PSI-BROKEN / CONTROL-DEAD on kill; else LIFTRACE-MEASURED with the
measured slopes, tracking gap, residual exponent, half-lift point and
fluctuation type.

Sources (read-only): v563_paper2_readouts (deployed tables, T163 lag
weights, T170 two-point read, tent assembly, odd Toeplitz),
critical_direction_classical_probe / note CII (classical direction,
named object (a)), wall_margin_mechanism_probe / note CI
(cancellation law, head-carried sensitivity), rh_leverage_probe /
note C (margin law h^-1.93, 67 faithful rungs), v883
(FLUCTUATIONS-REQUIRED), v884 (certified floors),
tfpt_prime_front.tex (I5 equivalence typing).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/arithmetic_lift_race_probe.py
"""

import ast
import hashlib
import math
import os
import sys
import time

import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
_VERIFY = os.path.abspath(os.path.join(_HERE, "..", "..", "verification"))
sys.path.insert(0, _HERE)
sys.path.insert(0, _VERIFY)

import v563_paper2_readouts as core        # noqa: E402  (READ-ONLY)

T0 = time.time()
CHECKS = []
KILLS = []
SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()

KZMAX = int(os.environ.get("LIFTRACE_KZMAX", 150))
SUBSET = (9, 13, 26, 40, 60, 90, 121)
AUDIT = (13, 40)
SEED = 20260810
NG_SMOOTH = 6000
BANNED_IDS = ("zetazero", "nzeros", "primerange", "isprime",
              "primepi", "nextprime", "prevprime")


def check(name, ok, detail="", kill=None):
    CHECKS.append((name, bool(ok)))
    if kill and not ok:
        KILLS.append(kill)
    print("  [%s] %s%s" % ("PASS" if ok else "FAIL", name,
                           ("  -- " + detail) if detail else ""),
          flush=True)
    return bool(ok)


def section(title):
    print("\n" + "=" * 70)
    print(title)
    print("=" * 70)


def q_read(W, u, D, M):
    """per-unit-mass atom energy along the direction with T163 lag
    weights W: q_g(u) = -0.5 x closed two-point read of W at u (the
    T170 spline_project, vectorized, incl. the u < D reflection)."""
    u = np.asarray(u, float)
    i0 = np.floor(u / D).astype(int)
    f = u / D - i0
    val = np.zeros_like(u)
    ok0 = (i0 >= 0) & (i0 < M)
    val[ok0] += (1.0 - f[ok0]) * W[i0[ok0]]
    ok1 = (i0 + 1 >= 0) & (i0 + 1 < M)
    val[ok1] += f[ok1] * W[i0[ok1] + 1]
    refl = u < D
    val[refl] += (1.0 - u[refl] / D) * W[0]
    return -0.5 * val


def robust_node(vec, D, alpha):
    """interior node between the two dominant lobes, interpolated."""
    v = vec * np.sign(vec[int(np.argmax(np.abs(vec)))])
    ip = int(np.argmax(v))
    im = int(np.argmin(v))
    if v[im] >= -0.02 * v[ip]:
        return float("nan")
    lo, hi = (im, ip) if im < ip else (ip, im)
    seg = v[lo:hi + 1]
    idx = np.where(np.diff(np.sign(seg)) != 0)[0]
    if len(idx) == 0:
        return float("nan")
    i = lo + (int(idx[0]) if im < ip else int(idx[-1]))
    t = v[i] / (v[i] - v[i + 1])
    return (i + t) * D / alpha


def smooth_comb(alpha, ng=NG_SMOOTH):
    ug = (np.arange(ng) + 0.5) * (2.0 * alpha / ng)
    mg = 2.0 * np.exp(ug / 2.0) * (2.0 * alpha / ng)
    return ug, mg


# ======================================================================
section("S0: setup -- rebuild the faithful ladder + smooth companions")
# ======================================================================
print("spec sha256 = %s" % SPEC_SHA)

RUNGS = {}
for kz in range(2, KZMAX + 1):
    try:
        rr = core.build_window(kz)
    except Exception:
        continue
    if not (core.H_MIN <= rr["h"] <= core.HCAP):
        continue
    if rr["X"] > core.ATOM_MAX:
        continue
    alpha, M, D, h = rr["alpha"], rr["M"], rr["D"], rr["h"]
    uu = np.asarray(rr["uu"], float)
    mu = 2.0 * np.asarray(rr["lam"], float)
    c_at = core.atom_lags_at(alpha, M, uu, mu)[0]
    c_ar = np.asarray(core.arch_lags(M, D), float)
    w, V = np.linalg.eigh(core.odd_toeplitz(c_ar + c_at, M))
    v = V[:, 0]
    ug, mg = smooth_comb(alpha)
    c_sm = core.atom_lags_at(alpha, M, ug, mg)[0]
    ws, Vs = np.linalg.eigh(core.odd_toeplitz(c_ar + c_sm, M))
    vsm = Vs[:, 0]
    if float(v @ vsm) < 0:
        vsm = -vsm
    ov4 = [abs(float(v @ Vs[:, j])) for j in range(4)]
    RUNGS[kz] = dict(alpha=alpha, M=M, D=D, h=h, X=rr["X"],
                     n_atom=rr["n_atom"], uu=uu, mu=mu, c_at=c_at,
                     c_ar=c_ar, c_sm=c_sm, lmin=float(w[0]), v=v,
                     lam_sm=float(ws[0]), vsm=vsm, ov4=ov4)
print("  %d faithful rungs rebuilt (h = %d..%d, alpha = %.3f..%.3f), "
      "%.1f s"
      % (len(RUNGS), min(R["h"] for R in RUNGS.values()),
         max(R["h"] for R in RUNGS.values()),
         min(R["alpha"] for R in RUNGS.values()),
         max(R["alpha"] for R in RUNGS.values()), time.time() - T0))

# per-rung, per-direction energy bookkeeping via the T163 lag weights
for kz, R in RUNGS.items():
    R["dir"] = {}
    for tag, g in (("v", R["v"]), ("vsm", R["vsm"])):
        W = core.lag_weights_from_v(g, R["h"])
        e_ar = float(R["c_ar"] @ W)
        e_t = float(R["c_at"] @ W)
        e_s = float(R["c_sm"] @ W)
        qa = R["mu"] * q_read(W, R["uu"], R["D"], R["M"])
        ug, mg = smooth_comb(R["alpha"])
        qg = mg * q_read(W, ug, R["D"], R["M"])
        R["dir"][tag] = dict(
            W=W, e_ar=e_ar, e_t=e_t, e_s=e_s,
            lift=e_t - e_s, demand=-(e_ar + e_s),
            id_atom=abs(float(qa.sum()) - e_t) / max(abs(e_t), 1e-30),
            id_grid=abs(float(qg.sum()) - e_s) / max(abs(e_s), 1e-30),
            sig=float(np.sqrt(np.sum(qa ** 2))))

# ======================================================================
section("S1: the exact weight identity")
# ======================================================================
mat_dev = 0.0
for kz in SUBSET:
    R = RUNGS[kz]
    K_at = core.odd_toeplitz(R["c_at"], R["M"])
    for tag, g in (("v", R["v"]), ("vsm", R["vsm"])):
        mat = float(g @ K_at @ g)
        lag = R["dir"][tag]["e_t"]
        mat_dev = max(mat_dev, abs(mat - lag) / max(abs(mat), 1e-30))
    del K_at

R13 = RUNGS[13]
W13 = R13["dir"]["v"]["W"]
samp_dev = 0.0
samp_rows = []
for j in (0, 5, 50, 100, 130):
    cj = core.atom_lags_at(R13["alpha"], R13["M"],
                           R13["uu"][j:j + 1], [1.0])[0]
    qd = float(R13["v"] @ core.odd_toeplitz(cj, R13["M"]) @ R13["v"])
    qf = float(q_read(W13, R13["uu"][j:j + 1], R13["D"], R13["M"])[0])
    samp_dev = max(samp_dev, abs(qd - qf) / max(abs(qd), 1e-30))
    samp_rows.append((int(round(math.exp(R13["uu"][j]))), qd))
print("    kz = 13 sample atoms (n, per-unit-mass weight q): %s"
      % ", ".join("n=%d: %+.4e" % r for r in samp_rows))
check("S1.a MATRIX = LAG READ: g.K_at.g equals the T163 lag read "
      "c_at.W_g to %.1e relative on the subset (ward 1e-12, both "
      "directions), and the fast two-point q_g(u) equals the DIRECT "
      "single-atom matrix energy to %.1e relative on five kz = 13 "
      "sample atoms (ward 1e-10)" % (mat_dev, samp_dev),
      mat_dev <= 1e-12 and samp_dev <= 1e-10, kill="IDENTITY-BROKEN")

id_at = max(R["dir"][t]["id_atom"] for R in RUNGS.values()
            for t in ("v", "vsm"))
id_gr = max(R["dir"][t]["id_grid"] for R in RUNGS.values()
            for t in ("v", "vsm"))
check("S1.b THE WEIGHTED-SUM IDENTITY on all %d rungs x 2 directions: "
      "sum_n mu_n q_g(u_n) = E_at(g) to %.1e relative (ward 1e-10) "
      "with mu_n = 2 Lambda(n)/sqrt(n); the PNT-grid version "
      "reproduces E_at_smooth(g) to %.1e (ward 1e-10).  THE ATOM "
      "ENERGY IS EXACTLY A WEIGHTED PRIME(-POWER) SUM"
      % (len(RUNGS), id_at, id_gr),
      id_at <= 1e-10 and id_gr <= 1e-10, kill="IDENTITY-BROKEN")

prof_rows = []
for kz in SUBSET:
    R = RUNGS[kz]
    alpha, D, M = R["alpha"], R["D"], R["M"]
    W = R["dir"]["v"]["W"]
    ugrid = np.linspace(1e-6, 2 * alpha - 1e-6, 3000)
    q = q_read(W, ugrid, D, M)
    qmax = float(np.max(np.abs(q)))
    live = np.abs(q) > 1e-4 * qmax
    nchg = int(np.sum(np.diff(np.sign(q[live])) != 0))
    supp = float(np.mean(np.abs(q) > 0.05 * qmax))
    q0 = float(q_read(W, np.array([1e-6]), D, M)[0])
    sel = ugrid >= math.log(2.0)
    jbig = int(np.argmax(np.abs(q[sel])))
    prof_rows.append((kz, q0, nchg, supp,
                      float(ugrid[sel][jbig] / alpha),
                      float(q[sel][jbig])))
    print("    kz %3d: q(0+) = %+.4f, sign changes %d, 5%%-support "
          "%.2f, largest reachable weight %+0.3f at u/alpha = %.3f"
          % (kz, q0, nchg, supp, prof_rows[-1][5], prof_rows[-1][4]))
check("S1.c THE WEIGHT PROFILE: q_g(0+) = -||g||^2 = -1 exactly "
      "(measured %+.4f..%+.4f, ward |q+1| < 0.01); 1..6 interior "
      "sign changes (measured %d..%d); 5%%-support %.2f..%.2f of the "
      "window (ward [0.5, 0.9]).  The largest magnitude sits at the "
      "u -> 0 lag end where NO atom lives (first atom at log 2 = "
      "%.3f)"
      % (min(r[1] for r in prof_rows), max(r[1] for r in prof_rows),
         min(r[2] for r in prof_rows), max(r[2] for r in prof_rows),
         min(r[3] for r in prof_rows), max(r[3] for r in prof_rows),
         math.log(2.0)),
      all(abs(r[1] + 1.0) < 0.01 and 1 <= r[2] <= 6
          and 0.5 <= r[3] <= 0.9 for r in prof_rows),
      kill="IDENTITY-BROKEN")

node_rows = []
for kz in SUBSET:
    R = RUNGS[kz]
    W = R["dir"]["v"]["W"]
    nd = robust_node(R["v"], R["D"], R["alpha"])
    qn = float(q_read(W, np.array([nd * R["alpha"]]), R["D"],
                      R["M"])[0])
    ugrid = np.linspace(1e-6, 2 * R["alpha"] - 1e-6, 3000)
    qmax = float(np.max(np.abs(q_read(W, ugrid, R["D"], R["M"]))))
    node_rows.append((kz, nd, abs(qn) / qmax))
check("S1.d FROZEN REFUTATION of the position reading: an atom at "
      "the mode's interior node u*/alpha = %.3f..%.3f still collects "
      "|q_g(u*)|/max|q_g| = %.3f..%.3f (ward >= 0.03 on every subset "
      "rung) -- q_g reads the FOLDED AUTOCORRELATION of g at lag u, "
      "not g(u)^2; the naive 'node atoms are free' picture is dead"
      % (min(r[1] for r in node_rows), max(r[1] for r in node_rows),
         min(r[2] for r in node_rows), max(r[2] for r in node_rows)),
      all(r[2] >= 0.03 for r in node_rows), kill="IDENTITY-BROKEN")

# ======================================================================
section("S2: the lift, the demand, and the race")
# ======================================================================
rows_v, rows_sm = [], []
for kz, R in RUNGS.items():
    dv, ds = R["dir"]["v"], R["dir"]["vsm"]
    rows_v.append((kz, R["alpha"], R["h"], dv["lift"], dv["demand"],
                   dv["lift"] - dv["demand"], R["lmin"], dv["sig"],
                   dv["e_t"]))
    rows_sm.append((kz, R["alpha"], R["h"], ds["lift"], ds["demand"],
                    ds["lift"] - ds["demand"], R["lam_sm"],
                    R["ov4"][0]))

print("      kz  alpha     h      lift      demand    lift-demand"
      "   lam_min")
for r in rows_v[:4] + rows_v[-4:]:
    print("    %4d %6.3f %5d  %8.4f  %8.4f   %+.4e  %+.4e"
          % (r[0], r[1], r[2], r[3], r[4], r[5], r[6]))

dev_v = max(abs(r[5] - r[6]) / max(abs(r[8]), 1.0) for r in rows_v)
dev_sm = 0.0
dev_dem = 0.0
for kz, R in RUNGS.items():
    ds = R["dir"]["vsm"]
    rq = ds["e_ar"] + ds["e_t"]
    dev_sm = max(dev_sm, abs((ds["lift"] - ds["demand"]) - rq)
                 / max(abs(ds["e_t"]), 1.0))
    dev_dem = max(dev_dem, abs(ds["demand"] + R["lam_sm"])
                  / max(abs(R["lam_sm"]), 1e-30))
check("S2.a EXACT BOOKKEEPING on all %d rungs: lift - demand = "
      "lam_min along v to %.1e (ward 1e-10 on the E_at scale); "
      "lift - demand = RQ(v_sm) along v_sm to %.1e; and demand(v_sm) "
      "= -lam_min(K_smooth) exactly (%.1e relative) -- the smooth "
      "model's own ground level IS the demand along its direction"
      % (len(RUNGS), dev_v, dev_sm, dev_dem),
      dev_v <= 1e-10 and dev_sm <= 1e-10 and dev_dem <= 1e-10,
      kill="RACE-BROKEN")

pos_ok = (all(r[3] > 0 and r[4] > 0 for r in rows_v)
          and all(r[3] > 0 and r[4] > 0 for r in rows_sm))
check("S2.b BOTH LEGS POSITIVE everywhere: lift %.4f..%.4f and "
      "demand %.4f..%.4f along v; lift %.4f..%.4f and demand "
      "%.4f..%.4f along v_sm -- the smooth world always leaves an "
      "O(1) hole, and the actual primes always over-fill it"
      % (min(r[3] for r in rows_v), max(r[3] for r in rows_v),
         min(r[4] for r in rows_v), max(r[4] for r in rows_v),
         min(r[3] for r in rows_sm), max(r[3] for r in rows_sm),
         min(r[4] for r in rows_sm), max(r[4] for r in rows_sm)),
      pos_ok, kill="RACE-BROKEN")

al = np.array([r[1] for r in rows_v])
hh = np.array([float(r[2]) for r in rows_v])
lf = np.array([r[3] for r in rows_v])
dm = np.array([r[4] for r in rows_v])
rs = np.array([r[5] for r in rows_v])
sl_l, ic_l = np.polyfit(al, lf, 1)
sl_d, ic_d = np.polyfit(al, dm, 1)
r2_l = 1.0 - float(np.var(lf - (sl_l * al + ic_l)) / np.var(lf))
r2_d = 1.0 - float(np.var(dm - (sl_d * al + ic_d)) / np.var(dm))
p_res = float(np.polyfit(np.log(hh), np.log(rs), 1)[0])
dsl = abs(sl_l - sl_d)
check("S2.c THE RACE HAS NO WINNER (frozen answer BOTH-TRACK): "
      "lift = %.4f alpha %+.4f (R2 %.3f), demand = %.4f alpha %+.4f "
      "(R2 %.3f), slope difference %.2e (ward <= 0.005), max "
      "residual %.2e (ward <= 1e-3), residual ~ h^%.3f (ward p in "
      "[-2.5, -1.5]).  The h^-2 margin decay is NOT demand outrunning "
      "lift and NOT lift stalling: both legs grow at the same rate "
      "and the margin is their ever-sharpening difference -- the "
      "six-digit cancellation of note CI, now written as a race of "
      "two explicit psi-type functionals"
      % (sl_l, ic_l, r2_l, sl_d, ic_d, r2_d, dsl, float(rs.max()),
         p_res),
      0.02 <= sl_l <= 0.2 and 0.02 <= sl_d <= 0.2 and r2_l >= 0.7
      and r2_d >= 0.7 and dsl <= 0.005 and float(rs.max()) <= 1e-3
      and -2.5 <= p_res <= -1.5, kill="RACE-BROKEN")

out_kz = [kz for kz, R in RUNGS.items() if R["ov4"][0] < 0.8]
out_ok = all(max(RUNGS[kz]["ov4"]) >= 0.8 for kz in out_kz)
a2 = np.array([r[1] for r in rows_sm])
lf2 = np.array([r[3] for r in rows_sm])
sl2, ic2 = np.polyfit(a2, lf2, 1)
r22 = 1.0 - float(np.var(lf2 - (sl2 * a2 + ic2)) / np.var(lf2))
check("S2.d THE SMOOTH-DIRECTION LEG, recorded honestly: %d rung(s) "
      "with bottom-branch overlap < 0.8 (%s; ward <= 2), and on each "
      "the classical direction is carried by a HIGHER smooth branch "
      "with overlap %s >= 0.8 -- a branch crossing, not a direction "
      "failure.  The v_sm lift fit %.4f alpha %+.4f has R2 = %.3f "
      "(recorded): the crossing rung contaminates the smooth-leg "
      "fit, which is exactly why the race ward lives on the true "
      "mode"
      % (len(out_kz),
         ", ".join("kz%d ov %.4f" % (k, RUNGS[k]["ov4"][0])
                   for k in out_kz) or "none",
         "/".join("%.3f" % max(RUNGS[k]["ov4"]) for k in out_kz)
         or "-", sl2, ic2, r22),
      len(out_kz) <= 2 and out_ok, kill="RACE-BROKEN")

# ======================================================================
section("S3: the psi-error reading")
# ======================================================================
cum_rows = []
for kz in AUDIT:
    R = RUNGS[kz]
    alpha, D, M = R["alpha"], R["D"], R["M"]
    W = R["dir"]["v"]["W"]
    qa = R["mu"] * q_read(W, R["uu"], D, M)
    ug, mg = smooth_comb(alpha)
    qg = mg * q_read(W, ug, D, M)
    lift = float(qa.sum() - qg.sum())
    ca = np.cumsum(qg)
    idx = np.searchsorted(R["uu"], ug, side="right")
    cq = np.concatenate(([0.0], np.cumsum(qa)))
    cum = cq[idx] - ca
    ihalf = int(np.argmax(np.abs(cum) >= 0.5 * abs(lift)))
    uhalf = float(ug[ihalf] / (2.0 * alpha))
    uh = math.log(100.0)
    head = float(qa[R["uu"] <= uh].sum() - qg[ug <= uh].sum())
    cum_rows.append((kz, lift, uhalf, head / lift))
    print("    kz %3d: lift %+0.4f; |cum| >= 50%% first at u/(2a) = "
          "%.3f; head n <= 100 carries %.2f of the lift; cum at "
          "u/(2a) = 0.25/0.50/0.75: %s"
          % (kz, lift, uhalf, head / lift,
             "/".join("%+.3f" % cum[int(f * (len(ug) - 1))]
                      for f in (0.25, 0.50, 0.75))))
check("S3.a HEAD-CARRIED: half of the lift is in place below "
      "u/(2 alpha) = %.3f/%.3f (ward <= 0.15) and the head n <= 100 "
      "carries %.2f/%.2f of the total (ward [0.5, 1.5]) on kz = "
      "13/40 -- the same small-prime seat that carries note CI's "
      "sensitivity carries the lift; the mid-window contributes "
      "oscillation, not level"
      % (cum_rows[0][2], cum_rows[1][2], cum_rows[0][3],
         cum_rows[1][3]),
      all(r[2] <= 0.15 and 0.5 <= r[3] <= 1.5 for r in cum_rows),
      kill="PSI-BROKEN")

ratio = np.array([r[3] / r[7] for r in rows_v])
check("S3.b THE SCALE TYPE: lift/sigma_fluct = %.3f..%.3f (median "
      "%.3f, ward [0.15, 0.9] on all %d rungs) with sigma_fluct = "
      "(sum mu_n^2 q^2)^{1/2} -- the arithmetic lift is a "
      "SUB-GENERIC-SCALE object, about 0.4 of the naive sqrt "
      "fluctuation scale, NOT a many-sigma conspiracy; the wall "
      "lives on a prime-sum displacement that generic placement "
      "noise could produce, pointed in exactly the right direction"
      % (float(ratio.min()), float(ratio.max()),
         float(np.median(ratio)), len(ratio)),
      bool(np.all((ratio >= 0.15) & (ratio <= 0.9))),
      kill="PSI-BROKEN")

# ======================================================================
section("C: controls")
# ======================================================================
rng = np.random.default_rng(SEED)
scr_rows = []
for kz in AUDIT:
    R = RUNGS[kz]
    alpha, D, M = R["alpha"], R["D"], R["M"]
    W = R["dir"]["v"]["W"]
    uus = np.sort(rng.uniform(0.0, 2.0 * alpha, size=len(R["uu"])))
    c_scr = core.atom_lags_at(alpha, M, uus, R["mu"])[0]
    e_scr = float(c_scr @ W)
    qs = float(np.sum(R["mu"] * q_read(W, uus, D, M)))
    id_scr = abs(qs - e_scr) / max(abs(e_scr), 1e-30)
    lift_scr = e_scr - R["dir"]["v"]["e_s"]
    scr_rows.append((kz, id_scr, lift_scr,
                     lift_scr - R["dir"]["v"]["demand"]))
    print("    kz %3d: scrambled identity %.1e; lift_scr %+0.3f "
          "(true %+0.3f); lift_scr - demand = %+0.3f"
          % (kz, id_scr, lift_scr, R["dir"]["v"]["lift"],
             scr_rows[-1][3]))
check("C1 SCRAMBLE fires: with randomized positions the identity "
      "still holds (%.1e, ward 1e-10 -- it is linear algebra) but "
      "the lift flips to %s and lift - demand to %s (wards < 0): "
      "the LIFT is a property of the actual prime placement, not of "
      "the mass budget"
      % (max(r[1] for r in scr_rows),
         "/".join("%+.2f" % r[2] for r in scr_rows),
         "/".join("%+.2f" % r[3] for r in scr_rows)),
      all(r[1] <= 1e-10 and r[2] < 0 and r[3] < 0 for r in scr_rows),
      kill="CONTROL-DEAD")

R = RUNGS[13]
W = R["dir"]["v"]["W"]
D, M, alpha = R["D"], R["M"], R["alpha"]
i0 = int(math.floor(math.log(2.0) / D)) + 1
u0 = None
while i0 + 1 < M:
    if W[i0] * W[i0 + 1] < 0.0:
        f0 = W[i0] / (W[i0] - W[i0 + 1])
        u0 = (i0 + f0) * D
        break
    i0 += 1
c0 = core.atom_lags_at(alpha, M, [u0], [1.0])[0]
e0 = float(R["v"] @ core.odd_toeplitz(c0, M) @ R["v"])
check("C2 ZERO-WEIGHT PLACEMENT: a unit atom at the first interior "
      "zero of q_g (u0 = %.4f = %.3f alpha, exact cell solve) has "
      "DIRECT matrix energy %+.1e (ward |E| <= 1e-9) -- the matrix, "
      "which never sees q_g, confirms the weight profile as the "
      "true influence function" % (u0, u0 / alpha, e0),
      abs(e0) <= 1e-9, kill="CONTROL-DEAD")

_tree = ast.parse(open(__file__, encoding="utf-8").read())
_called = {n.func.id for n in ast.walk(_tree)
           if isinstance(n, ast.Call) and isinstance(n.func, ast.Name)}
_called |= {n.func.attr for n in ast.walk(_tree)
            if isinstance(n, ast.Call)
            and isinstance(n.func, ast.Attribute)}
hits = sorted(_called & set(BANNED_IDS))
check("C3 FIREWALL: none of the deployed banned identifiers %s is "
      "called (hits: %s); no zero ordinate appears anywhere in this "
      "probe" % (list(BANNED_IDS), hits or "none"), not hits,
      kill="CONTROL-DEAD")

# ======================================================================
section("VERDICT")
# ======================================================================
if KILLS:
    verdict = KILLS[0]
else:
    verdict = ("LIFTRACE-MEASURED (LIFT-%.3fA%+.2f + "
               "TRACK-DSLOPE-%.0e + RESID-h^%.2f + HEAD-HALF-%.3f + "
               "SUBGENERIC-%.2fSIG + LAGREAD-NOT-POSITIONREAD)"
               % (sl_l, ic_l, dsl, p_res,
                  max(r[2] for r in cum_rows),
                  float(np.median(ratio))))
check("C4 NO-RH-CLAIM: the verdict reports an identity, two fitted "
      "growth laws and a scale type -- no truth value for RH in "
      "either direction",
      "RH-TRUE" not in verdict and "RH-FALSE" not in verdict,
      kill="CONTROL-DEAD")

n_pass = sum(1 for _, ok in CHECKS if ok)
print("\nCHECKS: %d/%d passed" % (n_pass, len(CHECKS)))
if n_pass != len(CHECKS):
    print("FAILED: %s" % [nm for nm, ok in CHECKS if not ok])
print("VERDICT: %s" % verdict)
print("""
WHAT THIS MEASURES (exploration only):
 * THE LIFT IS NOW EXPLICIT: along any fixed direction g the wall's
   atom energy is exactly sum_n 2 Lambda(n)/sqrt(n) q_g(log n) with
   a computable, compactly supported weight q_g -- verified against
   the matrix to 4e-13.  The open positivity statement per depth is
   a one-dimensional inequality between this prime sum and its PNT
   integral: a smoothed psi-error statement, nothing more exotic.
 * THE RACE HAS NO WINNER: demand (the smooth world's hole) and lift
   (the primes' surplus) both grow like 0.077 alpha and track each
   other to a few parts in 1e4 of their slopes; the h^-2 margin is
   their difference.  Neither leg misbehaves -- the difficulty is
   that the POSITIVE difference of two O(1) growing quantities must
   stay positive forever.
 * WHERE AND HOW BIG: the lift is head-carried (half in place below
   4% of the window; n <= 100 carries ~all of it) and SUB-GENERIC in
   size (~0.4 of the naive sqrt fluctuation scale).  The wall does
   not need a conspiracy-sized prime signal; it needs an ordinary-
   sized one with the right sign at every depth.
 * ONE DEAD PICTURE: q_g is a lag read, not a position read -- atoms
   at the mode's node are NOT free; the zero-weight points of the
   true influence function sit elsewhere and are confirmed by the
   raw matrix.
NO ledger/paper/website claim; NO RH claim in either direction; NO
physics claim beyond the recorded identities and measurements.
""")
print("runtime: %.1f s" % (time.time() - T0))
sys.exit(0 if n_pass == len(CHECKS) else 1)
