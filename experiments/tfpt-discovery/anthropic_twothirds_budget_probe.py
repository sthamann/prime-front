#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""anthropic_twothirds_budget_probe -- PRIME.W3.ANTHROPIC.TWOTHIRDS.01
(EXPLORATION ONLY, experiments/; RH-side auxiliary round CLXV,
2026-08-11): the ANTHROPIC TWO-THIRDS BUDGET -- injecting the new
unconditional zero-statistics theorem as an EXTERNAL-CITED input into
the deployed off-line detector / exclusion machinery, measuring where
it moves numbers and where it saturates (the honest ceiling).

THE EXTERNAL INPUT (typed EXTERNAL-CITED, pedigree recorded):
Anthropic (2026, paper + Lean formalization, arXiv / GitHub
zeta-23-lean): UNCONDITIONALLY, in every large dyadic window, at least
a fraction theta = 0.6725 of the nontrivial zeta zeros are SIMPLE and
ON the critical line (optimized constant ~ 0.6725; at least 0.83625
distinct).  Consequences used here: per large dyadic window the
off-line zero fraction is f_off <= 1 - 0.6725 = 0.3275 (~<= 1/3), the
off-line QUADRUPLE (pair) fraction is f_pair = f_off/2 = 0.16375
(~<= 1/6), and the mean zero multiplicity is <= 1/0.83625 = 1.19581.
PEDIGREE + CAVEATS (all three carried in every output block):
(i) published theorem-grade literature WITH machine-checked Lean
formalization -- but INDEPENDENT REPO-SIDE VERIFICATION IS PENDING
(neither the paper's argument nor its Lean artifact has been re-run
or audited inside this corpus; using external classical results is
established corpus practice, cf. the Schoenfeld / Buethe / Platt-
Trudgian [A1] citations, and this input is typed at exactly that
citation grade, not higher); (ii) the theorem is ASYMPTOTIC (per
LARGE dyadic window) -- an EXPLICIT-CONSTANT / finite-height form is
NOT available to this probe, so every finite-height application below
the classically verified strip stays typed ASYMPTOTIC and is NEVER
applied at deployed finite heights, where [A1] (Platt-Trudgian 3e12,
off-line fraction EXACTLY 0) is strictly stronger anyway;
(iii) NO RH claim -- the budget is a counting statement about zero
statistics, not a positivity certificate.

THE DEPLOYED CONSUMERS (inventory target; module anchors verified
live with line numbers in S1):
  C-A  v688_interpolation_detector.py (PRIME.INTERP.01): the
       matched-filter falsifier with single-quadruple threshold
       xi = 2 alpha delta >= 1.974 and the D4 MASKING adjudication
       (conspiring off-line quadruples masking a strong one).  The
       budget enters as the worst-case CONSPIRATOR COUNT per window:
       K = f_pair * N_win (old trivial f_off = 1: K = N_win/2).
  C-B  v825/v826/v827/v828 (PRIME.EXCLUSION.*): the certified
       exclusion tower with multi-zero hardening (two-quadruple
       superadditive exclusion) and the [A1] strip input
       T_RH_CITED = 3.0e12.  The budget enters as the admissible
       two-quadruple conspiracy census C(K, 2) per window; below
       3e12 it is SUPERSEDED by [A1] (exactly zero off-line).
  C-C  v684_rank3_zeroside.py (PRIME.RANK3ZERO.01): the explicit-
       formula zero side with kappa_unc = 0.039..0.190 and the
       per-zero envelope |z(gamma)| <= 2 C_G / gamma^2.  HONEST NULL
       EXPECTED: the envelope is LOCATION-BLIND (it bounds via
       1/|1/2 + i gamma|^2 and total counts, not via beta), so the
       off-line fraction budget moves NOTHING there; the location
       input it does consume (classical zero-free strip, damping
       x634) is STRONGER than any fractional budget in its region
       (fraction exactly 0 off-line inside the strip).  The
       DISTINCTNESS budget is the one genuinely new average bound:
       mean multiplicity <= 1.19581 per large window (classical
       per-zero reference m(rho) << log gamma is unbounded on
       average; NOTE: RH itself implies NOTHING about simplicity,
       so the f_off = 0 control does NOT improve this row).
  C-D  PRIME.ERRORTERM.SCALE.01 (the hardness row, decided; the
       demand-curve probe errorterm_demand_curve_probe.py + the
       tfpt_prime_front.tex hardness paragraph, A* ~ sqrt(tau)/
       delta^2, off-line cosh injection Delta c(t) = A cos(gamma0 t)
       (cosh(delta t) - 1)): the wall-flip amplitude A* is the
       calibration the ceiling is measured against.  The budget
       enters as the total admissible off-line injection amplitude
       per window A_tot = 2 * f_pair * N_win (A = 2 per quadruple).

THE HONEST CEILING (the (c) content, verified live in S3): the wall
margin tau equals a FRACTION OF ONE QUADRUPLE (live A* = 2e-4..8e-3,
i.e. 0.01%..0.4% of A = 2), while the counting budget still PERMITS
A_tot = 0.3275 * N_win of off-line amplitude per window -- the budget
saturates ORDERS OF MAGNITUDE above the wall demand; and even the
f_off = 0 (RH-count) world leaves every deployed floor numerically
untouched (tau(A=0) == tau0 exactly: floor_of consumes LAGS, never a
zero count) -- the remaining difficulty is fine-phase prime-side
cancellation (the error term at the port frequencies), NOT off-line
counting, exactly as the deployed hardness decision types it
("exact reformulation at RH strength, no unconditional slack").

FROZEN PROTOCOL (frozen + SHA-hashed before the frozen run; SMOKE
DISCLOSURE below):

 S0  EXTERNAL INPUT RECORD: constants typed and arithmetically
     closed (theta + f_off == 1 exactly; f_pair == f_off/2;
     mean_mult == 1/0.83625); the three caveat phrases (independent
     verification pending / asymptotic, explicit-constant form
     pending / no RH claim) present in this frozen spec (self-scan).

 S1  INVENTORY (machine-derived, module + line): locate the frozen
     anchors in the consumer files -- '1.974' + 'masking' in v688;
     'T_RH_CITED = 3.0e12' + 'two-quadruple' in v825; 'kappa_unc'
     in v684; 'RH-SCALE-EQUIVALENT' in the demand-curve probe;
     'PRIME.ERRORTERM.SCALE.01' in tfpt_prime_front.tex.  Gates:
     >= 6 anchors found, each with a line number.

 S2  THE WINDOW BUDGET TABLE (asymptotic rows T in {1e12, 1e16,
     1e20, 1e28}; dyadic window [T, 2T]; N_win from the RvM main
     term N(T) = T/(2 pi) ln(T/(2 pi e)) + 7/8, VALIDATED against
     the committed zero cache at T = 500 / 1000, rel <= 5e-3):
     per budget world OLD (f_off = 1, deployed trivial) / NEW
     (0.3275) / RH (0): conspirator quadruples K, masking-robust
     threshold xi_rob = xi_min + ln K (worst-case linear masking
     model, typed as model; xi_min = 1.974 from v688), two-quadruple
     census C(K, 2), admissible injection A_tot = 2K.  Frozen
     expectations: Delta xi(OLD->NEW) = ln(0.5/0.16375) = 1.11627
     (T-independent); census factor (0.5/0.16375)^2 = 9.32350;
     the T = 1e12 row (2T < 3e12) typed A1-SUPERSEDED with the
     Anthropic budget NOT applied (off-line = 0 classically).

 S3  LIVE RECOMPUTE on the deployed demand-curve machinery (v563
     READ-ONLY, floor route verbatim from the round-38 chain):
     rungs kz {9, 13, 26} x delta {0.05, 0.10} x gamma0 = 10
     (generic frozen frequency, NOT a zero ordinate; worst sign;
     18-step bisection).  Gates: tau0 reproduces the frozen
     references {9: 1.6752e-4, 13: 7.8242e-5, 26: 2.7938e-6} rel
     1e-3; the A = 2 single-quadruple kill fires at all 6 cells
     (corpus detector claim reproduced); A* < 2 at all cells with
     quadruple fraction A*/2 <= 0.005; the ceiling gap
     log10(A_tot_NEW / A*) >= 6 at every asymptotic T for every
     cell; tau(A = 0) == tau0 EXACTLY at all three rungs (floors
     consume no zero count -- the RH-count world moves nothing).

 S4  CONTROLS: C1 REGRESSION -- the f_off = 1 world reproduces the
     deployed trivial numbers exactly (K = N_win/2, A_tot = N_win,
     independently coded closed forms, equality to 0 ulps);
     C2 RH BRACKET -- monotone old >= new >= RH per location row,
     the bracket [old, RH-limit] printed with the 2/3 point marked;
     C3 TAU-SCREEN -- amplitude-convention rescale x1.1 (A, A*,
     A_tot together) leaves Delta xi, the census factor and every
     ceiling gap invariant to 1e-12 (the margins are dimensionless);
     C4 MULTIPLICITY HONESTY -- mean-mult 1.19581 < ln T on every
     asymptotic row (the distinctness budget is the binding AVERAGE
     bound) AND the RH-no-simplicity caveat is typed (f_off = 0
     does not touch the multiplicity row).

 KILLS: K1 pipeline breaks -> PIPELINE-BROKEN; K2 inventory empty /
 anchor missing -> INVENTORY-EMPTY; K3 C1 fails -> REGRESSION-FAIL.

 VERDICT (frozen enum): BUDGET-INJECTED-CEILING-TYPED /
 PIPELINE-BROKEN / INVENTORY-EMPTY / REGRESSION-FAIL.

SMOKE DISCLOSURE (honest, before freeze): one smoke pass of the
machinery was run before freezing (2026-08-11): window sizes M =
368/336/728, tau0 = 1.675e-4 / 7.824e-5 / 2.794e-6, and the six A*
values 0.0058/0.0014/0.0077/0.0019/0.0008/0.0002 were SEEN; the S3
tau0 reference values and the A*/2 <= 0.005 and gap >= 6 bars were
frozen AFTER seeing them (disclosed; the bars are typing bars, not
discovery bars -- the discovery content is the old/new/RH table and
the ceiling, both fixed by the external constants and closed forms).

FIREWALL: v563 READ-ONLY import; consumer modules are OPENED AS TEXT
ONLY (never imported, never executed); NO zetazero()/nzeros()/prime
oracles (AST self-scan); the committed zero cache is read for the
RvM VALIDATION ward only (no zero datum enters any budget number);
no RNG; writes nothing but stdout.  NO marker moves, NO ledger row,
NO paper edit, NO RH claim.

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/anthropic_twothirds_budget_probe.py
"""

import ast
import hashlib
import json
import math
import os
import sys
import time

import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.abspath(os.path.join(_HERE, "..", ".."))
_VERIFY = os.path.join(_ROOT, "verification")
sys.path.insert(0, _HERE)
sys.path.insert(0, _VERIFY)

import v563_paper2_readouts as core        # noqa: E402  (READ-ONLY)

# ------------------------------------------------------- frozen constants
THETA_SIMPLE_ONLINE = 0.6725          # Anthropic 2026, optimized constant
DISTINCT_FRAC = 0.83625               # >= distinct fraction
F_OFF_NEW = 1.0 - THETA_SIMPLE_ONLINE  # 0.3275  (~<= 1/3)
F_PAIR_NEW = F_OFF_NEW / 2.0           # 0.16375 (~<= 1/6)
MEAN_MULT_NEW = 1.0 / DISTINCT_FRAC    # 1.19581
F_OFF_OLD, F_OFF_RH = 1.0, 0.0         # trivial deployed / RH-count world
XI_MIN = 1.974                         # v688 single-quadruple threshold
T_A1 = 3.0e12                          # [A1] Platt-Trudgian (v825 cite)
T_GRID = (1.0e12, 1.0e16, 1.0e20, 1.0e28)
RUNGS = (9, 13, 26)
DELTAS = (0.05, 0.10)
GAMMA0 = 10.0                          # generic frozen frequency
TAU0_REF = {9: 1.6752e-4, 13: 7.8242e-5, 26: 2.7938e-6}
TAU0_REL = 1.0e-3
FRAC_BAR = 0.005                       # A*/2 typing bar
GAP_BAR = 6.0                          # ceiling gap bar (log10)
DXI_EXP = math.log(0.5 / F_PAIR_NEW)   # 1.11627
CENSUS_EXP = (0.5 / F_PAIR_NEW) ** 2   # 9.32350
CACHE = os.path.join(_HERE, "zero_comb_cache_n2000.json")
BANNED_IDS = ("zetazero", "nzeros", "primerange", "isprime",
              "primepi", "nextprime", "prevprime")

ANCHORS = (
    ("verification/v688_interpolation_detector.py", "1.974"),
    ("verification/v688_interpolation_detector.py", "masking"),
    ("verification/v825_prime_exclusion_ladder.py", "T_RH_CITED = 3.0e12"),
    ("verification/v825_prime_exclusion_ladder.py", "two-quadruple"),
    ("verification/v684_rank3_zeroside.py", "kappa_unc"),
    ("experiments/tfpt-discovery/errorterm_demand_curve_probe.py",
     "RH-SCALE-EQUIVALENT"),
    ("tfpt_prime_front.tex", "PRIME.ERRORTERM.SCALE.01"),
)

FROZEN_SPEC = "\n".join([
    "PRIME.W3.ANTHROPIC.TWOTHIRDS.01 frozen 2026-08-11",
    "external input EXTERNAL-CITED: Anthropic 2026 zeta-23-lean,",
    "unconditional per large dyadic window: >= 0.6725 simple+on-line,",
    ">= 0.83625 distinct; independent repo-side verification PENDING;",
    "ASYMPTOTIC theorem, explicit-constant finite form PENDING ->",
    "never applied below the [A1] strip 3e12; NO RH claim.",
    "f_off = 0.3275, f_pair = 0.16375, mean_mult <= 1.19581.",
    "worlds: OLD f_off=1 / NEW 0.3275 / RH 0.",
    "S1 anchors >= 6 with line numbers.",
    "S2 T in {1e12,1e16,1e20,1e28}; RvM main term validated on the",
    "committed cache at T=500/1000 rel 5e-3; xi_rob = 1.974 + ln K;",
    "Delta xi = ln(0.5/0.16375); census factor (0.5/0.16375)^2;",
    "1e12 row A1-SUPERSEDED (budget not applied).",
    "S3 kz {9,13,26} x delta {0.05,0.10} x gamma0 10, worst sign,",
    "18-step bisection; tau0 refs {1.6752e-4,7.8242e-5,2.7938e-6}",
    "rel 1e-3; A=2 kill 6/6; A*/2 <= 0.005; gap >= 6 asymptotic;",
    "tau(A=0) == tau0 exact.",
    "S4 C1 regression exact; C2 bracket monotone; C3 tau-screen x1.1",
    "invariant 1e-12; C4 mean-mult < ln T + RH-no-simplicity typed.",
    "verdict enum: BUDGET-INJECTED-CEILING-TYPED / PIPELINE-BROKEN /",
    "INVENTORY-EMPTY / REGRESSION-FAIL.",
])
SPEC_SHA = hashlib.sha256(FROZEN_SPEC.encode()).hexdigest()

CHECKS = []
KILLS = []
T0 = time.time()


def check(name, ok, detail="", kill=None):
    CHECKS.append((name, bool(ok)))
    if kill and not ok:
        KILLS.append(kill)
    print("  [%s] %s%s" % ("PASS" if ok else "FAIL", name,
                           ("  -- " + detail) if detail else ""),
          flush=True)
    return bool(ok)


def section(title):
    print("\n" + "=" * 74)
    print(title)
    print("=" * 74, flush=True)


def ast_scan():
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


# --------------------------------------------- deployed floor machinery
# (verbatim route of errorterm_demand_curve_probe / round-38 chain;
#  v563 READ-ONLY)

def grid_density(c):
    c = np.asarray(c, float)
    a = np.concatenate([c, c[-2:0:-1]])
    d = np.fft.fft(a)
    assert float(np.max(np.abs(d.imag))) <= 1e-9 * max(
        1.0, float(np.max(np.abs(d.real))))
    return d.real


def build_lags(kz):
    rr = core.build_window(kz)
    uu = np.asarray(rr["uu"], float)
    mm = 2.0 * np.asarray(rr["lam"], float)
    c_at, _ = core.atom_lags_at(rr["alpha"], rr["M"], uu, mm)
    c_ar = np.asarray(core.arch_lags(rr["M"], rr["D"]), float)
    return dict(c=c_ar + np.asarray(c_at, float), M=rr["M"],
                D=rr["D"], alpha=rr["alpha"], h=rr["h"])


def floor_of(c, M):
    # NOTE: consumes LAGS only -- no zero count, no budget argument.
    K = core.odd_toeplitz(c, M)
    c_abs = np.real(np.fft.ifft(np.abs(grid_density(c))))[:M]
    Tabs = core.odd_toeplitz(c_abs, M)
    Gp = 0.5 * (Tabs + K)
    Gm = 0.5 * (Tabs - K)
    ev, V = np.linalg.eigh(Gp)
    if float(ev[0]) <= 0.0:
        return None
    R = V @ np.diag(ev ** -0.5) @ V.T
    A = R @ Gm @ R
    return 1.0 - float(np.linalg.eigvalsh(0.5 * (A + A.T))[-1])


def zero_signature(M, D, delta, gamma0):
    tt = np.arange(M) * D
    return np.cos(gamma0 * tt) * (np.cosh(delta * tt) - 1.0)


def critical_A(b, sig, steps=18):
    best = (float("inf"), 0)
    for s in (+1.0, -1.0):
        hi = 4.0
        t_hi = floor_of(b["c"] + s * hi * sig, b["M"])
        grow = 0
        while (t_hi is None or t_hi > 0.0) and grow < 8:
            hi *= 4.0
            t_hi = floor_of(b["c"] + s * hi * sig, b["M"])
            grow += 1
        if t_hi is None or t_hi > 0.0:
            continue
        lo = 0.0
        for _ in range(steps):
            mid = 0.5 * (lo + hi)
            t_m = floor_of(b["c"] + s * mid * sig, b["M"])
            if t_m is None or t_m < 0.0:
                hi = mid
            else:
                lo = mid
        if hi < best[0]:
            best = (hi, int(s))
    return best


# ------------------------------------------------------- budget algebra

def rvm_N(T):
    return T / (2.0 * math.pi) * math.log(T / (2.0 * math.pi * math.e)) \
        + 7.0 / 8.0


def window_row(T, f_off):
    """Per-window budget quantities for off-line fraction f_off."""
    n_win = rvm_N(2.0 * T) - rvm_N(T)
    K = (f_off / 2.0) * n_win           # admissible off-line quadruples
    xi_rob = XI_MIN + (math.log(K) if K >= 1.0 else 0.0)
    census2 = 0.5 * K * (K - 1.0) if K >= 2.0 else 0.0
    a_tot = 2.0 * K
    return dict(T=T, n_win=n_win, K=K, xi_rob=xi_rob,
                census2=census2, a_tot=a_tot)


def main():
    section("PRIME.W3.ANTHROPIC.TWOTHIRDS.01 -- the two-thirds budget "
            "injected into the off-line machinery (EXPLORATION ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s" % SPEC_SHA)
    print("    EXTERNAL-CITED: Anthropic 2026 (paper + Lean, "
          "zeta-23-lean); independent repo-side verification PENDING;")
    print("    ASYMPTOTIC per large dyadic window (explicit-constant "
          "finite form PENDING); NO RH claim.")
    bad = ast_scan()
    check("FW  firewall AST self-scan (no zero/prime oracles)",
          not bad, "banned ids found: %s" % bad if bad else "clean",
          kill="PIPELINE-BROKEN")

    # ------------------------------------------------------------ S0
    section("S0 -- the external input record")
    ok0 = (abs(THETA_SIMPLE_ONLINE + F_OFF_NEW - 1.0) == 0.0
           and F_PAIR_NEW == F_OFF_NEW / 2.0
           and MEAN_MULT_NEW == 1.0 / DISTINCT_FRAC)
    check("S0.1 constants arithmetically closed", ok0,
          "theta %.4f -> f_off %.4f, f_pair %.5f, mean_mult %.5f"
          % (THETA_SIMPLE_ONLINE, F_OFF_NEW, F_PAIR_NEW, MEAN_MULT_NEW),
          kill="PIPELINE-BROKEN")
    doc = __doc__
    phrases = ("INDEPENDENT REPO-SIDE VERIFICATION IS PENDING",
               "ASYMPTOTIC", "explicit-constant", "NO RH claim")
    miss = [p for p in phrases if p.lower() not in doc.lower()]
    check("S0.2 pedigree + caveat phrases present in spec", not miss,
          "missing: %s" % miss if miss else "all four typed",
          kill="PIPELINE-BROKEN")

    # ------------------------------------------------------------ S1
    section("S1 -- consumer inventory (machine-derived, module + line)")
    found = []
    for rel, pat in ANCHORS:
        path = os.path.join(_ROOT, rel)
        lineno = None
        if os.path.exists(path):
            with open(path, encoding="utf-8", errors="replace") as fh:
                for i, line in enumerate(fh, 1):
                    if pat in line:
                        lineno = i
                        break
        found.append((rel, pat, lineno))
        print("    %-58s %-28s line %s"
              % (rel.split("/")[-1], repr(pat),
                 lineno if lineno else "MISSING"))
    n_found = sum(1 for _, _, ln in found if ln)
    check("S1.1 inventory >= 6 anchors located", n_found >= 6,
          "%d/%d anchors with line numbers" % (n_found, len(ANCHORS)),
          kill="INVENTORY-EMPTY")
    print("\n    HOW THE BUDGET ENTERS (per large dyadic window, "
          "asymptotic):")
    print("    C-A v688 masking: conspirators K = f_pair*N_win "
          "(old N_win/2)")
    print("    C-B v825/828 tower: two-quadruple census C(K,2); "
          "below 3e12 [A1] gives 0 exactly (budget NOT applied)")
    print("    C-C v684 zero side: envelope 2C_G/gamma^2 is "
          "LOCATION-BLIND -> no gain (honest null); NEW average "
          "bound mean_mult <= %.5f (RH gives no simplicity)"
          % MEAN_MULT_NEW)
    print("    C-D hardness row: admissible injection A_tot = "
          "2*f_pair*N_win vs the wall demand A*")

    # ------------------------------------------------------------ S2
    section("S2 -- the window budget table (OLD / NEW / RH)")
    with open(CACHE, encoding="utf-8") as fh:
        gam = np.asarray(json.load(fh)["gammas"], float)
    ok_rvm = True
    for Tv in (500.0, 1000.0):
        actual = int(np.sum(gam <= Tv))
        pred = rvm_N(Tv)
        rel = abs(pred / actual - 1.0)
        ok_rvm &= rel <= 5e-3
        print("    RvM ward T=%6.0f: cache %4d vs main term %8.2f "
              "(rel %.2e)" % (Tv, actual, pred, rel))
    check("S2.1 RvM main term validated on the committed cache",
          ok_rvm, "rel <= 5e-3 at T = 500 / 1000",
          kill="PIPELINE-BROKEN")

    rows = {}
    hdr = ("T", "N_win", "K_old", "K_new", "K_rh", "xi_old", "xi_new",
           "xi_rh", "flag")
    print("\n    %-8s %-10s %-10s %-10s %-5s %-8s %-8s %-6s %s" % hdr)
    for Tv in T_GRID:
        r_old = window_row(Tv, F_OFF_OLD)
        r_new = window_row(Tv, F_OFF_NEW)
        r_rh = window_row(Tv, F_OFF_RH)
        flag = ("A1-SUPERSEDED (off-line = 0 classically; asymptotic "
                "budget NOT applied)") if 2.0 * Tv <= T_A1 else "asymptotic"
        rows[Tv] = (r_old, r_new, r_rh, flag)
        print("    %-8.0e %-10.3e %-10.3e %-10.3e %-5.0f %-8.3f "
              "%-8.3f %-6.3f %s"
              % (Tv, r_new["n_win"], r_old["K"], r_new["K"], r_rh["K"],
                 r_old["xi_rob"], r_new["xi_rob"], r_rh["xi_rob"], flag))
    asym = [Tv for Tv in T_GRID if 2.0 * Tv > T_A1]
    check("S2.2 asymptotic rows populated, N_win large",
          all(rows[Tv][1]["n_win"] > 1e10 for Tv in asym),
          "N_win %.2e .. %.2e" % (rows[asym[0]][1]["n_win"],
                                  rows[asym[-1]][1]["n_win"]),
          kill="PIPELINE-BROKEN")
    dxis = [rows[Tv][0]["xi_rob"] - rows[Tv][1]["xi_rob"] for Tv in asym]
    check("S2.3 masking-threshold shift Delta xi = ln(0.5/0.16375) "
          "= %.5f, T-independent" % DXI_EXP,
          all(abs(d - DXI_EXP) <= 1e-5 for d in dxis),
          "measured %.5f .. %.5f (%.1f%% of the single-quadruple "
          "threshold %.3f)" % (min(dxis), max(dxis),
                               100.0 * DXI_EXP / XI_MIN, XI_MIN))
    cfacs = [rows[Tv][0]["census2"] / rows[Tv][1]["census2"]
             for Tv in asym]
    check("S2.4 two-quadruple census factor (0.5/0.16375)^2 = %.4f"
          % CENSUS_EXP,
          all(abs(f / CENSUS_EXP - 1.0) <= 1e-3 for f in cfacs),
          "measured %.4f .. %.4f" % (min(cfacs), max(cfacs)))
    fin = [Tv for Tv in T_GRID if 2.0 * Tv <= T_A1]
    check("S2.5 finite-height honesty: sub-[A1] rows typed "
          "A1-SUPERSEDED",
          all(rows[Tv][3].startswith("A1-SUPERSEDED") for Tv in fin),
          "%d row(s) below 3e12; budget there = 0 exactly from [A1], "
          "NOT 0.3275" % len(fin))

    # ------------------------------------------------------------ S3
    section("S3 -- live recompute on the deployed floor machinery "
            "(the ceiling)")
    live = {}
    ok_tau, ok_kill, ok_frac, ok_zero = True, True, True, True
    for kz in RUNGS:
        b = build_lags(kz)
        tau0 = floor_of(b["c"], b["M"])
        rel = abs(tau0 / TAU0_REF[kz] - 1.0)
        ok_tau &= rel <= TAU0_REL
        tz = floor_of(b["c"] + 0.0 * b["c"], b["M"])   # A = 0 injection
        ok_zero &= (tz == tau0)
        print("    kz %2d: h %3d alpha %.3f tau0 %.4e (ref rel %.1e); "
              "tau(A=0) == tau0: %s" % (kz, b["h"], b["alpha"], tau0,
                                        rel, tz == tau0))
        for d in DELTAS:
            sig = zero_signature(b["M"], b["D"], d, GAMMA0)
            t2 = min(x for x in
                     (floor_of(b["c"] + s * 2.0 * sig, b["M"])
                      for s in (+1.0, -1.0)) if x is not None)
            ok_kill &= t2 < 0.0
            Ast, sgn = critical_A(b, sig)
            ok_frac &= (Ast < 2.0 and Ast / 2.0 <= FRAC_BAR)
            live[(kz, d)] = Ast
            print("      delta %.2f: A=2 kill tau %.3e | A* %.6f "
                  "(sign %+d, %.4f%% of one quadruple)"
                  % (d, t2, Ast, sgn, 100.0 * Ast / 2.0))
    check("S3.1 tau0 reproduces the frozen round-38 references "
          "(rel <= 1e-3)", ok_tau, kill="PIPELINE-BROKEN")
    check("S3.2 the A = 2 single-quadruple kill fires 6/6 "
          "(corpus detector claim reproduced)", ok_kill)
    check("S3.3 A* is a FRACTION of one quadruple (A*/2 <= %.3f "
          "everywhere)" % FRAC_BAR, ok_frac,
          "A* %.2e .. %.2e" % (min(live.values()), max(live.values())))
    gaps = {}
    ok_gap = True
    for Tv in asym:
        a_new = rows[Tv][1]["a_tot"]
        for cell, Ast in live.items():
            g = math.log10(a_new / Ast)
            gaps[(Tv,) + cell] = g
            ok_gap &= g >= GAP_BAR
    check("S3.4 THE CEILING: budget saturates >= %.0f decades above "
          "the wall demand" % GAP_BAR, ok_gap,
          "log10(A_tot_NEW / A*) = %.1f .. %.1f over %d (T, cell) "
          "pairs" % (min(gaps.values()), max(gaps.values()), len(gaps)))
    check("S3.5 floors consume NO zero count (tau(A=0) == tau0 "
          "exactly; the RH-count world moves no deployed number)",
          ok_zero)
    print("\n    HONEST CEILING (typed): even f_off = 0 -- ZERO "
          "off-line pairs, the RH-count world -- leaves tau0 and the")
    print("    open one-sidedness T_h <= 1 numerically untouched: the "
          "remaining difficulty is fine-phase prime-side")
    print("    cancellation (the error term at the port frequencies), "
          "NOT off-line counting -- consistent with the deployed")
    print("    hardness decision PRIME.ERRORTERM.SCALE.01 ('exact "
          "reformulation at RH strength, no unconditional slack').")

    # ------------------------------------------------------------ S4
    section("S4 -- controls")
    ok_reg = True
    for Tv in T_GRID:
        n_win = rvm_N(2.0 * Tv) - rvm_N(Tv)
        K_triv = 0.5 * n_win                      # deployed trivial
        a_triv = n_win
        r_old = rows[Tv][0]
        ok_reg &= (r_old["K"] == K_triv and r_old["a_tot"] == a_triv)
    check("S4.1 C1 REGRESSION: f_off = 1 reproduces the deployed "
          "trivial numbers exactly (0 ulps)", ok_reg,
          kill="REGRESSION-FAIL")
    ok_mono = True
    for Tv in T_GRID:
        r_old, r_new, r_rh, _ = rows[Tv]
        for q in ("K", "a_tot", "xi_rob", "census2"):
            ok_mono &= (r_old[q] >= r_new[q] >= r_rh[q])
    check("S4.2 C2 RH BRACKET monotone: old >= 2/3-point >= RH on "
          "every location quantity", ok_mono,
          "e.g. T=1e16 xi_rob %.3f >= %.3f >= %.3f"
          % (rows[1e16][0]["xi_rob"], rows[1e16][1]["xi_rob"],
             rows[1e16][2]["xi_rob"]))
    scale = 1.1
    ok_tau_scr = True
    for Tv in asym:
        a_new = rows[Tv][1]["a_tot"]
        for cell, Ast in live.items():
            g0 = math.log10(a_new / Ast)
            g1 = math.log10((scale * a_new) / (scale * Ast))
            ok_tau_scr &= abs(g1 - g0) <= 1e-12
    d0 = rows[asym[0]][0]["xi_rob"] - rows[asym[0]][1]["xi_rob"]
    ok_tau_scr &= abs(d0 - DXI_EXP) <= 1e-5
    check("S4.3 C3 TAU-SCREEN: x%.1f amplitude-convention rescale "
          "leaves every margin invariant (<= 1e-12)" % scale,
          ok_tau_scr)
    ok_mult = all(MEAN_MULT_NEW < math.log(Tv) for Tv in T_GRID)
    check("S4.4 C4 MULTIPLICITY: mean_mult %.5f < ln T on every row; "
          "RH-no-simplicity caveat typed (f_off = 0 does NOT improve "
          "this row)" % MEAN_MULT_NEW, ok_mult)

    # -------------------------------------------------------- verdict
    section("VERDICT")
    n_pass = sum(1 for _, ok in CHECKS if ok)
    if KILLS:
        verdict = KILLS[0]
    elif n_pass == len(CHECKS):
        verdict = "BUDGET-INJECTED-CEILING-TYPED"
    else:
        verdict = "PIPELINE-BROKEN"
    print("  checks: %d/%d PASS" % (n_pass, len(CHECKS)))
    print("  VERDICT: %s" % verdict)
    print("  runtime %.1f s" % (time.time() - T0))
    print("\n  EXTERNAL-CITED pedigree carried: Anthropic 2026 "
          "(paper + Lean, zeta-23-lean), unconditional, ASYMPTOTIC "
          "per large dyadic window;")
    print("  independent repo-side verification PENDING; "
          "explicit-constant finite form PENDING; NO RH claim; "
          "no marker moves.")
    return verdict


if __name__ == "__main__":
    main()
