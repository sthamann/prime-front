#!/usr/bin/env python3
"""QF-OFFENSIVE strand 3 follow-up -- the drainage decider: does the
frame-independent band weight q_f^T(X) = ||P_X^(6) f||^2 drain to
ZERO on a deeper comb (kernel pairing asymptotically vanishing -- the
wall dissolves) or settle at a positive per-function level (the wall
is a true constant -- Feshbach / boundary-triple treatment becomes
mandatory)?  qf_drainage_probe.

Exploration only (tfpt-experiment firewall): NOT wired into
run_all.py, no ledger row, no paper edit, no website edit, NO RH
CLAIM, and this probe writes no files.  It never reads a zero
ordinate and never evaluates the target before every source object
is built and SHA-256 frozen.  The band weight is built exclusively
from the source window operator -- never from target data.

INPUT STATE (frozen findings, none re-adjudicated here):
  *  qf_spectral_bundle_probe -- QF-BUNDLE-PARTIAL (GATES 4/5,
     GUARDS+CONTROLS 19/19): the Kato transport is WELL-DEFINED
     (rank 6 on all 22 rungs 888..972, rel gap 6/7 = 0.3441..0.5592,
     angles <= 2.72 deg, TV flattening) and repairs the rigid frame
     for 14/14 functions (median med5 ratio 26.7 -> 1.004), but the
     decider failed 0/14: the residual increments are dominated
     (radial share median ~0.64) by the frame-independent drainage
     of the band weight, e.g. R1:box[0,R] 0.1906 -> 0.0811,
     R2:box[0,R] 0.6140 -> 0.4403 over X = 13.875..15.1875.  Its
     two named next surfaces are exactly this probe: (1) the
     drainage limit on a deeper comb, (2) O(step^2) Kato-holonomy
     scaling on a step-1 sub-ladder.
  *  Same probe, honest outlook inside the pass: the 6/7 gap erodes
     monotonically from M = 916 (0.5592) to M = 972 (0.3441) --
     lam7 descending toward the frozen threshold 1e-4; a 7th-mode
     THRESHOLD crossing on the extension is expected and is handled
     by the predeclared band rule below, typed, never hidden.
  *  yosida_qf_convergence_probe -- the near-kernel is a stable
     object (alignment >= 0.9996); the battery class is essentially
     subordinate to it (89..99.9% of battery mass).

COMPUTE-BUDGET BENCHMARK (declared; run BEFORE this spec was frozen;
timing/memory only -- no spectra, no battery pairing, no q levels
were consulted): sieve at 1e8 = 1.2 s / 800 MB table / peak RSS
1.17 GB; tent assembly over 5.52e6 atoms at M = 1176 = 6.5 s; dense
eigh at M ~ 1176 ~ 0.13 s.  On this budget the DEEPER COMB CAP is
frozen at ATOM_MAX_DEEP = 100,000,000 (1e8) -- one cap, chosen
before the first run, never adjusted after.

FROZEN CONSTRUCTION (reused machinery verbatim, none invented):
  deeper comb = deployed von Mangoldt generator
      (core.von_mangoldt_table) at cap ATOM_MAX_DEEP = 1e8;
      M_CAP_DEEP = floor(64 ln 1e8) = 1178; M_TOP_DEEP = 1176
      (X = 18.375; step-4 aligned with the parent top 972 = 1176 -
      51*4; sieve cover exp(18.375) + 2 = 95,534,693 <= 1e8).
  battery = module-1 handoff_bulk battery verbatim (14 functions,
      support <= NPAD = 128 cells); dyadic grid D = 1/64.
  spectral ladder SLAD = 956..1176 step 4 (56 rungs; the leading 5
      rungs 956..972 are the bundle probe's LAST5 window, reused as
      the parent-top block for exact continuity).
  band rule (parent rule verbatim, predeclared): the drainage object
      is the BAND weight q_f(X) = ||P_X^(6) f||^2 with P^(6) = span
      of the 6 LOWEST eigenmodes, ALWAYS; the threshold count
      #{lam <= THR_NULL = 1e-4} is reported on every rung and a
      threshold crossing (count 6 -> 7 while the band stays
      separated) is TYPED with its crossing rung -- it does NOT by
      itself change the object.
  depth blocks (med5, fit-free level statistics; N_MED = 5):
      PARENT5 = M in {956, 960, 964, 968, 972}   (X ~ 14.94..15.19)
      MID5    = M in {1056, 1060, 1064, 1068, 1072} (X ~ 16.50..16.75)
      TOP5    = M in {1160, 1164, 1168, 1172, 1176} (X ~ 18.13..18.38)
      second-half slope block = M in 1072..1176 step 4 (27 rungs);
      slope = hbp.fit_rate verbatim on (X, q): log q = a - b X,
      b > 0 = draining, per X unit.
DRAINAGE GATES (per function, all frozen BEFORE the first run):
  DRAINS-TO-ZERO type Z:  Z1 level: med5(TOP5) <= Z_FRAC = 0.5 x
      med5(PARENT5); Z2 monotone trend: med5(PARENT5) > med5(MID5)
      > med5(TOP5); Z3 no plateau: second-half falling rate
      b >= Z_SLOPE = 0.10 per X unit.
  SETTLES-POSITIVE type P:  P1 flattening: |b| <= P_SLOPE = 0.05
      per X unit; P2 positive level: med5(TOP5) >= P_FLOOR = 1e-3;
      P3 oscillation-aware spread: rel spread (max-min)/max of q
      over TOP5 <= P_SPREAD = 0.15.
  neither -> type U (undecided); for U and P functions the
      decision-depth extrapolation X* with q(X*) = Z_FRAC x
      med5(PARENT5) at the measured rate b (if b > 0) is REPORTED
      with the implied ATOM_MAX ~ exp(X*).
STRUCTURE GATES on the extension (frozen; take PRECEDENCE):
  S1 gap collapse: rel gap (lam7 - lam6)/lam7 < GAP_BAR = 0.10 on
      any SLAD rung (the 6-band ceases to be separated); the gap
      profile AND the linear second-half trend with its projected
      GAP_BAR crossing X are reported either way.
  S2 deep-structure change: deep count #{lam <= THR_DEEP = 1e-5}
      != 1 on any SLAD rung (the single persistent deep mode is a
      frozen parent finding).
  S3 band instability: consecutive 6-band alignment (parent formula
      ||V_new^T pad(V_old)||_F^2 / 6) < ALIGN_BAR = 0.80 on any
      SLAD pair.
  A THRESHOLD crossing (count 6 -> 7 at thr 1e-4 with S1-S3 intact)
      is typed and reported, NOT a structure change (the band rule
      is the predeclared instrument for exactly this).
HOLONOMY CHECK (secondary, REPORTED never gated): step-1 sub-ladder
  HOLO_LAD = 1160..1176 step 1 (17 rungs).  For step s in {1, 2, 4}
  the same one-step Kato transport (polar of the 6x6 overlap) is run
  on the sub-chain 1160, 1160+s, ..., 1176; per pair and function
  the increment ||Q^T a_next - a|| splits into radial | ||a_next||
  - ||a|| | and angular remainder sqrt(max(delta^2 - radial^2, 0)).
  Kato-holonomy expectation: per-step ANGULAR medians scale
  ~ O(s^2) (exponent log2(m(2s)/m(s)) ~ 2) while RADIAL medians
  scale ~ O(s) (exponent ~ 1) -- the level slide is first-order,
  the frame error second-order.  Measured exponents reported.
GUARDS (must pass or the run is invalid):
  G0.1 AST firewall (banned: zetazero/nzeros/isprime/primerange/
       nextprime/prevprime/primepi/sympy); G0.2 SHA-256 freeze of
       battery bytes + ladders + blocks + every bar + the deep-comb
       spec BEFORE any comb data is built here; G0.3 reach census +
       runtime cap 900 s predeclared;
  G1.1 deep-table overlap: extended von Mangoldt table == deployed
       core table on [0, 400000] EXACTLY; G1.2 extended Chebyshev
       envelope kappa <= KAPPA_REF + 1e-6 over [100, 1e8];
  G1.3 parent tower comb consistency (rel dev <= 1e-12); G1.4
       prefix Ward: deep tower leading 824 x 824 block == parent
       tower (<= 1e-12);
  G1.5 bundle-probe reproduction Ward: max band q_f(M = 972) =
       0.4403 +- 2e-3 AND rel gap(972) = 0.3441 +- 2e-3 AND
       threshold count(972) = 6 AND deep count(972) = 1 (the frozen
       first-run numbers of qf_spectral_bundle_probe);
  G1.6 measured PD: lambda_min > -1e-9 on every SLAD rung (measured
       output; NO gate uses a PD margin or 1/eps);
  G1.7 boundedness: every q_f in [-1e-12, 1 + 1e-9], every overlap
       singular value <= 1 + 1e-12;
  G2.1 holonomy isometry Ward: max | ||Q^T a|| - ||a|| | <= 1e-10
       on the step-1 chain.
CONTROLS (mandatory, must fire; fire rule = qf_spectral_bundle_probe.
  control_bundle VERBATIM, imported read-only): CS position scramble
  (positions uniform in (0.5, 2 alpha_deep), masses kept, seed 7, on
  the DEEP comb, rungs 496..512 step 4) and CE Epstein x^2 + 5y^2
  (epstein_firewall_probe read-only, cap M = 640, rungs 624..640
  step 4).  FIRE = rank instability OR gap collapse OR angle
  saturation.  A control whose bundle construction stays intact has
  spuriously converged: the run is INVALID.
VERDICT ENUM (frozen; decision order as listed):
  0. any guard fails or a control spuriously converges -> the run is
     INVALID: printed as QF-DRAINAGE-UNDECIDED (invalid run), exit 1,
     no drainage statement follows.
  1. QF-STRUCTURE-CHANGES = S1 or S2 or S3 fires: the rank/gap
     structure changes qualitatively on the deeper comb (typed
     exactly: which clause, which rung); this reopens the object
     question and takes precedence over the drainage typing.
  2. QF-DRAINS-TO-ZERO   = ALL 14 functions type Z: the kernel
     pairing is asymptotically vanishing with measured rates -- the
     wall dissolves at depth; for Gate 3 this means the diagonal
     route's transported coordinates become Cauchy-to-zero (the
     Feshbach 6x6 block would converge to 0 -- the reduction becomes
     unnecessary rather than impossible).
  3. QF-SETTLES-POSITIVE = ALL 14 functions type P: the wall is a
     true per-function positive constant; the settled levels are the
     new named objects and the Feshbach / boundary-triple treatment
     becomes mandatory.
  4. otherwise QF-DRAINAGE-UNDECIDED: the bars are not reached
     either way at this depth (the Z/P/U split is named per function
     and the decision depth is extrapolated honestly).
STOP-LIST (binding, inherited): no target decomposition / Cholesky /
zeros anywhere; no bare A^{-1}; no PD-margin or 1/eps in any gate;
no fits inside gates beyond the declared bounded-statistic slopes;
no Riemann zeros; NO RH claim.  This probe writes no files.  Runtime
cap 900 s predeclared.

RESULTS (2026-08-05, first and only preregistered run, 22.0 s; GATES
4/5 -- S1, S2, S3 and P pass, Z fails 0/14; GUARDS+CONTROLS 14/14;
types PPPPPPPPPPPPPP; verdict QF-SETTLES-POSITIVE):
  *  THE DRAINAGE WAS A TRANSIENT.  The steep fall measured by the
     bundle probe on 888..972 does NOT continue: from the parent-top
     block (X ~ 15.1) to MID5 (X ~ 16.6) levels drop only 6..25%,
     and from MID5 to TOP5 (X ~ 18.3) they are FLAT to slightly
     RISING (med5 top >= med5 mid for 12/14).  Second-half falling
     rates b = -0.040..+0.002 per X unit -- every |b| <= 0.05
     (plateau bar); TOP5 rel spreads 0.008..0.025 <= 0.15; every
     settled level >= 7.4e-3 >= floor 1e-3.  All 14 functions type
     P; type Z fires for none (worst-case decision depth if the
     residual +0.002 rate were trusted: X* ~ 227, ATOM_MAX ~ 5e98
     -- i.e. never, on any reachable surface).
  *  THE SETTLED LEVELS (the new named objects; med5 over TOP5):
     R2:box[0,R] 0.3583, R2:box[R/2,R] 0.3370, R2:hat(R/2,R/2)
     0.3127, R2:hat(3R/4,R/4) 0.2590, R2:box[R/4,3R/4] 0.2249;
     R1 family 0.0082..0.0793 (R1:box[R/2,R] 0.0793, R1:box[0,R]
     0.0741, R1:hat(R/4,R/4) 0.0082); R2:box[0,R/2] == R1:box[0,R]
     (same function, 0.0741).
  *  STRUCTURE HOLDS -- with two typed, honest observations: (i)
     7th-mode THRESHOLD crossing at M = 992 (X = 15.5, lam7 =
     9.94e-5), count reaches 8 from M ~ 1108; the band rule (6
     lowest) carries the object as predeclared -- at this depth
     "6" is a band-rule choice, no longer a threshold fact.  (ii)
     the 6/7 gap erosion BOTTOMS OUT instead of collapsing: min rel
     gap 0.1008 at M ~ 1100 -- 8e-4 above the bar, the thinnest
     pass in this strand -- then RECOVERS to 0.1397 at M = 1176;
     second-half trend +0.0179/X, no projected crossing.  S2: the
     single deep mode (lam <= 1e-5) persists 1 on all 56 rungs.
     S3: consecutive 6-band alignment >= 0.999597.  PD margins
     6.459e-6 (972) -> 3.882e-6 (1176), measured never gated.
  *  HOLONOMY CHECK -- the O(step^2) expectation is CORRECTED by
     measurement: per-step ANGULAR medians 2.39e-4 / 4.88e-4 /
     9.06e-4 for s = 1/2/4, exponents 1.03 and 0.89 (NOT ~2);
     RADIAL exponents 1.01 / 1.02 (~1 as expected).  Honest
     reading: O(s^2) applies to the frame-transport ERROR, not to
     the coordinate increments of a moving section -- the measured
     O(s) scaling says the transported coordinates c(X) trace a
     SMOOTH curve with O(1) velocity in X (a genuine connection-
     speed term; the step-4 ladder was already resolving it).
     Cauchy-ness of c(X) is therefore a question of velocity decay
     in X, not of step refinement -- consistent with the settled-
     positive verdict.
  *  CONTROLS both fire (rank + gap clauses): CS scramble (deep
     comb, 5,520,266 atoms) threshold counts 243..252 vs 6,
     252/512 negative eigenvalues, min rel gap 1e-4; CE Epstein
     counts 251..263 vs 6, min rel gap 0.065.
  *  GUARDS 14/14: deep-table overlap exact (dev 0.0), kappa =
     0.038821 unchanged on [100, 1e8], prefix Ward 2.0e-14, bundle
     reproduction Ward q(972) dev 1.0e-5 / gap(972) dev 3.7e-5,
     boundedness q in [7.4e-3, 0.4679], holonomy isometry Ward
     4.4e-16, runtime 22.0 s <= 900 s.
  *  CONSEQUENCE FOR THE OFFENSIVE (stated plainly): the wall is a
     TRUE positive per-function constant -- the kernel pairing does
     not vanish at depth, so the diagonal route can NOT wait it
     out: the Feshbach 6x6 / boundary-triple treatment of the
     near-kernel block becomes MANDATORY.  What this run OPENS: the
     Feshbach 6x6 module now has everything it needs -- a
     well-defined transported frame (bundle probe), SETTLED
     coupling levels (this probe: the draining diagonal objection
     was a transient of the 888..972 window), and a smooth O(1)
     connection velocity (holonomy check); the hierarchical-basis
     module inherits a stable kernel-band/complement split with
     converged pairing weights.  What it CLOSES: the "wall
     dissolves by itself" hope (Z fired 0/14) and the step-
     refinement route to Cauchy coordinates (exponent ~1, not ~2).
     The cell-cocycle module is neither opened nor closed: the
     connection is smooth and nontrivial, its cocycle data remains
     unprobed.  Typed caution carried forward: the 6/7 gap min
     0.1008 and the threshold counts 7..8 mean the Feshbach block
     dimension at deeper X may need the band rule re-examined
     (6 vs 7/8) -- a predeclared question for that module, not a
     defect of this run.  NO RH claim, no X -> infinity claim.

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/qf_drainage_probe.py
"""

import ast
import hashlib
import math
import os
import sys
import time

import numpy as np
import scipy.linalg as sla

_HERE = os.path.dirname(os.path.abspath(__file__))
_VERIFY = os.path.abspath(os.path.join(_HERE, "..", "..",
                                       "verification"))
sys.path.insert(0, _HERE)
sys.path.insert(0, _VERIFY)

import v563_paper2_readouts as core  # noqa: E402
import simpler_schur_recursion_probe as srp  # noqa: E402
import handoff_bulk_probe as hbp  # noqa: E402
import epstein_firewall_probe as epx  # noqa: E402
import qf_spectral_bundle_probe as qsb  # noqa: E402  (read-only)

T_START = time.time()

# ------------------------------------------------ frozen specification
D = srp.DGRID                        # 1/64, dyadic float-exact
ATOM_MAX_DEEP = 100000000            # deep comb cap (frozen, 1e8)
M_CAP_DEEP = int(math.floor(math.log(ATOM_MAX_DEEP) / D))   # 1178
M_TOP_DEEP = 1176                    # deepest rung (step-4 aligned)
M_TOP_PAR = 824                      # first-parent cap (prefix Ward)
M_TOP_BUN = 972                      # bundle-probe top (continuity)

SLAD = list(range(956, 1177, 4))     # 56 rungs, X = 14.9375..18.375
PARENT5 = list(range(956, 973, 4))   # bundle probe's LAST5 window
MID5 = list(range(1056, 1073, 4))
TOP5 = list(range(1160, 1177, 4))
HALF2 = list(range(1072, 1177, 4))   # 27 rungs, second-half slope
HOLO_LAD = list(range(1160, 1177))   # 17 rungs step 1 (holonomy)
HOLO_STEPS = (1, 2, 4)

K_RANK = 6                           # band rank (frozen)
THR_NULL = 1.0e-4                    # threshold policy (reported)
THR_DEEP = 1.0e-5                    # deep census (S2 gate)
NPAD = 128                           # max battery support in cells
R_BAT = (1.0, 2.0)                   # frozen module-1 local battery
N_MED = 5                            # median block size

Z_FRAC = 0.5                         # Z1: top med5 <= 0.5 x parent
Z_SLOPE = 0.10                       # Z3: falling rate >= 0.10/X
P_SLOPE = 0.05                       # P1: |rate| <= 0.05/X plateau
P_FLOOR = 1.0e-3                     # P2: settled level floor
P_SPREAD = 0.15                      # P3: TOP5 rel spread bar
QF_FLOOR = 1.0e-12                   # denominator floor

GAP_BAR = 0.10                       # S1: rel gap (lam7-lam6)/lam7
ALIGN_BAR = 0.80                     # S3: consecutive band alignment

REPRO_Q972 = 0.4403                  # bundle frozen max band q(972)
REPRO_GAP972 = 0.3441                # bundle frozen rel gap(972)
REPRO_TOL = 2.0e-3                   # G1.5 reproduction tolerance
COMB_DEV_BAR = 1.0e-12               # G1.3 sieve == deployed masses
PREFIX_WARD = 1.0e-12                # G1.4 prefix max abs dev
PD_TOL = 1.0e-9                      # G1.6 measured-PD slack
BOUND_TOL = 1.0e-9                   # G1.7 boundedness slack
WARD_ISO = 1.0e-10                   # G2.1 holonomy isometry Ward
RUNTIME_CAP = 900.0                  # seconds, predeclared

EP_NCAP = 34000                      # Epstein Lambda_E table reach
EP_MMAX = 640                        # Epstein control tower cap
SEED = 7

BANNED = ("zetazero", "nzeros", "isprime", "primerange", "nextprime",
          "prevprime", "primepi", "sympy")

CHECKS = []       # guards + controls: all must pass, else invalid run
GATES = []        # structure + drainage gates: feed the verdict only


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok)))
    print("[%s] %s%s" % ("PASS" if ok else "FAIL", name,
                         (": " + detail) if detail else ""))
    return bool(ok)


def gate(name, ok, detail=""):
    GATES.append((name, bool(ok)))
    print("[GATE %s] %s%s" % ("PASS" if ok else "FAIL", name,
                              (": " + detail) if detail else ""))
    return bool(ok)


def ast_firewall():
    with open(os.path.abspath(__file__), "r", encoding="utf-8") as fh:
        tree = ast.parse(fh.read())
    hits = set()
    for node in ast.walk(tree):
        name = ""
        if isinstance(node, ast.Name):
            name = node.id
        elif isinstance(node, ast.Attribute):
            name = node.attr
        elif isinstance(node, (ast.Import, ast.ImportFrom)):
            for alias in node.names:
                token = alias.name.split(".")[0]
                if any(b in token.lower() for b in BANNED):
                    hits.add(token)
        if name and any(b in name.lower() for b in BANNED):
            hits.add(name)
    return sorted(hits)


def freeze_spec():
    """Battery bytes + ladders + blocks + bars + deep-comb spec,
    SHA-256 frozen BEFORE any comb data is built in this probe."""
    bats = {}
    hsh = hashlib.sha256()
    hsh.update(("qf-drainage spec: 4 boxes + 3 hats per R, l2-norm, "
                "D=%.10f, R=%s; deep comb = deployed "
                "von_mangoldt_table sieve at cap %d, M_CAP=%d, "
                "M_TOP=%d; SLAD=%s; PARENT5=%s MID5=%s TOP5=%s "
                "HALF2=%s; HOLO=%s steps=%s; band rule = 6 LOWEST "
                "modes always, thr=%g reported, crossing typed not "
                "structural; K=%d Nmed=%d; Z: frac<=%g mono slope>=%g"
                "; P: |slope|<=%g floor>=%g spread<=%g; S1 gap>=%g "
                "S2 deep==1 (thr %g) S3 align>=%g; repro q972=%g "
                "gap972=%g tol=%g; guards: comb<=%g prefix<=%g "
                "pd>=-%g bound<=%g iso<=%g runtime<=%g; controls "
                "verbatim qsb.control_bundle, lads=%s/%s epcap=%d "
                "epM=%d seed=%d; verdict order: invalid -> "
                "STRUCTURE -> DRAINS(all Z) -> SETTLES(all P) -> "
                "UNDECIDED"
                % (D, R_BAT, ATOM_MAX_DEEP, M_CAP_DEEP, M_TOP_DEEP,
                   SLAD, PARENT5, MID5, TOP5, HALF2, HOLO_LAD,
                   HOLO_STEPS, THR_NULL, K_RANK, N_MED, Z_FRAC,
                   Z_SLOPE, P_SLOPE, P_FLOOR, P_SPREAD, GAP_BAR,
                   THR_DEEP, ALIGN_BAR, REPRO_Q972, REPRO_GAP972,
                   REPRO_TOL, COMB_DEV_BAR, PREFIX_WARD, PD_TOL,
                   BOUND_TOL, WARD_ISO, RUNTIME_CAP, qsb.CTRL_LAD_S,
                   qsb.CTRL_LAD_E, EP_NCAP, EP_MMAX, SEED)).encode())
    for R in R_BAT:
        bats[R] = hbp.battery(R)
        for nm, v in bats[R]:
            hsh.update(nm.encode())
            hsh.update(v.tobytes())
    return bats, hsh.hexdigest()


def battery_matrix(bats):
    cols, names = [], []
    for R in R_BAT:
        nR = int(round(R / D))
        for nm, v in bats[R]:
            f = np.zeros(NPAD)
            f[:nR] = v
            cols.append(f)
            names.append("R%g:%s" % (R, nm))
    return np.stack(cols, axis=1), names


# ------------------------------------------------ towers (verbatim)
def build_parent_tower():
    alpha = 0.5 * M_TOP_PAR * D
    ka, masks, dev_m = srp.channel_masks(alpha)
    check("G1.3 parent tower comb consistency (zeta-free Gauss "
          "double sieve == deployed masses, rel dev <= %.0e)"
          % COMB_DEV_BAR, dev_m <= COMB_DEV_BAR,
          "rel dev %.1e, ka=%d atoms to e^%.4f"
          % (dev_m, ka, 2.0 * alpha))
    c = srp.continuum_lags(M_TOP_PAR)
    for cnl in ("ro", "re", "sp", "in"):
        c = c + srp.atom_channel_lags(alpha, M_TOP_PAR, masks[cnl])
    return sla.toeplitz(c[:M_TOP_PAR])


def build_deep_comb():
    lam_deep = core.von_mangoldt_table(ATOM_MAX_DEEP)
    dev = float(np.max(np.abs(lam_deep[:core.ATOM_MAX + 1]
                              - core.LAM_TAB)))
    check("G1.1 deep-table overlap: deep von Mangoldt table == "
          "deployed core table on [0, %d] EXACTLY"
          % core.ATOM_MAX, dev == 0.0, "max abs dev %.1e" % dev)
    nn = np.nonzero(lam_deep > 0.0)[0]
    u_deep = np.log(nn.astype(float))
    mu_deep = 2.0 * lam_deep[nn] / np.sqrt(nn.astype(float))
    psi = np.cumsum(lam_deep[nn])
    keep = nn.astype(float) >= core.KAPPA_X0
    kappa = float(np.max(np.abs(psi[keep] - nn[keep].astype(float))
                         / nn[keep].astype(float)))
    check("G1.2 deep-range Chebyshev envelope: kappa = %.6f over "
          "all jump points of psi(x)/x in [%.0f, %d] <= KAPPA_REF + "
          "%.0e = %.6f" % (kappa, core.KAPPA_X0, ATOM_MAX_DEEP,
                           core.TOL_KAPPA,
                           core.KAPPA_REF + core.TOL_KAPPA),
          kappa <= core.KAPPA_REF + core.TOL_KAPPA)
    return u_deep, mu_deep


def build_deep_tower(u_deep, mu_deep, T_par):
    alpha = 0.5 * M_TOP_DEEP * D
    ka = int(np.searchsorted(u_deep, 2.0 * alpha + 1.0e-14,
                             side="right"))
    c_cont = srp.continuum_lags(M_TOP_DEEP)
    c_at, _dd = core.atom_lags_at(alpha, M_TOP_DEEP, u_deep[:ka],
                                  mu_deep[:ka])
    T = sla.toeplitz((c_cont + c_at)[:M_TOP_DEEP])
    dev = float(np.max(np.abs(T[:M_TOP_PAR, :M_TOP_PAR] - T_par)))
    check("G1.4 prefix Ward: deep tower leading %d x %d block == "
          "parent tower, max abs dev %.1e <= %.0e"
          % (M_TOP_PAR, M_TOP_PAR, dev, PREFIX_WARD),
          dev <= PREFIX_WARD)
    print("  deep census: ka = %d atoms to e^%.4f" % (ka,
                                                      2.0 * alpha))
    return T, c_cont, alpha, ka


# ------------------------------------------------ spectral ladder
def spectral_pass(T, sizes):
    """One dense eigendecomposition per rung; store spectrum head,
    sign-fixed 6-band basis, census numbers."""
    out = {}
    for M in sizes:
        lam, V = np.linalg.eigh(T[:M, :M])
        out[M] = dict(M=M, lam_min=float(lam[0]),
                      lam6=float(lam[K_RANK - 1]),
                      lam7=float(lam[K_RANK]),
                      Vb=qsb.sign_fix(V[:, :K_RANK]),
                      nn=int(np.sum(lam <= THR_NULL)),
                      nn_deep=int(np.sum(lam <= THR_DEEP)))
    return out


def lin_slope(xs, ys):
    A = np.vstack([np.ones_like(xs), xs]).T
    coef, *_ = np.linalg.lstsq(A, ys, rcond=None)
    return float(coef[1])


def fall_rate(xs, vals):
    """hbp.fit_rate verbatim: log val = a - b x, b > 0 = falling."""
    rows = [dict(XmR=float(x), mx=float(v)) for x, v in zip(xs, vals)]
    b, _resid = hbp.fit_rate(rows)
    return b


# ------------------------------------------------ structure gates
def structure_gates(spec, F):
    blks = [spec[M] for M in SLAD]
    xs = np.array([b["M"] * D for b in blks])

    nns = [b["nn"] for b in blks]
    print("\n-- structure on the extension (band rule = 6 lowest "
          "always; threshold count thr = %g reported)" % THR_NULL)
    print("  threshold count profile along SLAD: %s"
          % "/".join(str(n) for n in nns))
    cross = [b["M"] for b in blks if b["nn"] > K_RANK]
    if cross:
        print("  TYPED: 7th-mode THRESHOLD crossing (count > 6) "
              "first at M = %d (X = %.4f); lam7 there = %.4e <= "
              "thr %g.  Band rule keeps the object = 6 lowest "
              "modes; NOT a structure change while S1-S3 hold."
              % (cross[0], cross[0] * D,
                 spec[cross[0]]["lam7"], THR_NULL))
    else:
        print("  no threshold crossing on SLAD (count stays <= 6)")

    gaps = [(b["lam7"] - b["lam6"]) / b["lam7"] for b in blks]
    print("  gap profile (every 4th rung shown): %s"
          % "  ".join("M=%d:%.4f" % (b["M"], g)
                      for b, g in list(zip(blks, gaps))[::4]))
    n2 = len(gaps) // 2
    gslope = lin_slope(xs[n2:], np.array(gaps[n2:]))
    if gslope < 0.0:
        x_cross = xs[-1] + (gaps[-1] - GAP_BAR) / (-gslope)
        proj = ("second-half gap trend %.4f/X; projected GAP_BAR "
                "crossing at X ~ %.2f (M ~ %d, ATOM_MAX ~ %.1e)"
                % (gslope, x_cross, int(x_cross / D),
                   math.exp(x_cross)))
    else:
        proj = ("second-half gap trend %.4f/X (non-decreasing; no "
                "projected crossing)" % gslope)
    print("  " + proj)
    s1 = gate("S1 band separation on the extension: min rel gap "
              "(lam7-lam6)/lam7 = %.4f >= %g (max %.4f, at top "
              "rung %.4f)" % (min(gaps), GAP_BAR, max(gaps),
                              gaps[-1]), min(gaps) >= GAP_BAR)

    deeps = [b["nn_deep"] for b in blks]
    s2 = gate("S2 deep structure: deep count (lam <= %g) == 1 on "
              "every SLAD rung (profile %s..%s)"
              % (THR_DEEP, deeps[0], deeps[-1]),
              all(d == 1 for d in deeps))

    aligns = []
    for a, b in zip(blks, blks[1:]):
        Vp = np.zeros((b["M"], K_RANK))
        Vp[:a["M"], :] = a["Vb"]
        pr = b["Vb"].T @ Vp
        aligns.append(float(np.sum(pr ** 2) / K_RANK))
    s3 = gate("S3 band stability: min consecutive 6-band alignment "
              "= %.6f >= %g (mean %.6f)"
              % (min(aligns), ALIGN_BAR, float(np.mean(aligns))),
              min(aligns) >= ALIGN_BAR)
    return s1, s2, s3, cross


# ------------------------------------------------ drainage decider
def drainage(spec, F, names):
    blks = [spec[M] for M in SLAD]
    q = np.stack([(blk["Vb"][:NPAD, :].T @ F) ** 2 for blk in blks]
                 ).sum(axis=1)                     # (56, 14)
    qmap = {M: q[i] for i, M in enumerate(SLAD)}

    med_par = np.median(np.stack([qmap[M] for M in PARENT5]), axis=0)
    med_mid = np.median(np.stack([qmap[M] for M in MID5]), axis=0)
    med_top = np.median(np.stack([qmap[M] for M in TOP5]), axis=0)
    q_top5 = np.stack([qmap[M] for M in TOP5])
    spread_top = (q_top5.max(axis=0) - q_top5.min(axis=0)) \
        / np.maximum(q_top5.max(axis=0), QF_FLOOR)
    xs_h = np.array([M * D for M in HALF2])
    q_h = np.stack([qmap[M] for M in HALF2])
    b = np.array([fall_rate(xs_h, q_h[:, j])
                  for j in range(q.shape[1])])

    print("\n-- drainage decider: per-function band-weight levels "
          "(med5 at three depths; slope = second-half falling rate "
          "b per X unit over M %d..%d; Z bars: top <= %g x parent, "
          "monotone, b >= %g; P bars: |b| <= %g, level >= %g, "
          "TOP5 spread <= %g)"
          % (HALF2[0], HALF2[-1], Z_FRAC, Z_SLOPE, P_SLOPE, P_FLOOR,
             P_SPREAD))
    print("  %-18s %-8s %-8s %-8s %6s %7s %7s  %s"
          % ("function", "parent", "mid", "top", "ratio", "b/X",
             "spread", "type"))
    types = []
    for j, nm in enumerate(names):
        ratio = med_top[j] / max(med_par[j], QF_FLOOR)
        z = (ratio <= Z_FRAC
             and med_par[j] > med_mid[j] > med_top[j]
             and b[j] >= Z_SLOPE)
        p = (abs(b[j]) <= P_SLOPE and med_top[j] >= P_FLOOR
             and spread_top[j] <= P_SPREAD)
        ty = "Z" if z else ("P" if p else "U")
        types.append(ty)
        print("  %-18s %.4f   %.4f   %.4f   %5.3f  %+6.3f  %6.3f  %s"
              % (nm, med_par[j], med_mid[j], med_top[j], ratio,
                 b[j], spread_top[j], ty))
        if ty != "Z" and b[j] > 0.0:
            x_star = TOP5[-1] * D + math.log(
                max(med_top[j], QF_FLOOR)
                / max(Z_FRAC * med_par[j], QF_FLOOR)) / b[j]
            if x_star > TOP5[-1] * D:
                print("    %-16s decision depth at measured rate: "
                      "X* ~ %.2f (M ~ %d, ATOM_MAX ~ %.1e)"
                      % ("", x_star, int(x_star / D),
                         math.exp(x_star)))

    n_z = types.count("Z")
    n_p = types.count("P")
    n_u = types.count("U")
    gz = gate("Z DRAINS-TO-ZERO: all 14 functions type Z -- %d Z / "
              "%d P / %d U" % (n_z, n_p, n_u), n_z == 14)
    gp = gate("P SETTLES-POSITIVE: all 14 functions type P -- %d Z "
              "/ %d P / %d U" % (n_z, n_p, n_u), n_p == 14)

    qmin, qmax = float(np.min(q)), float(np.max(q))
    check("G1.7 boundedness audit: every band q_f in [%.1e, %.4f] "
          "inside [-1e-12, 1 + %.0e] -- bounded quadratic forms of "
          "unit vectors; no 1/eps, no PD margin in any gate"
          % (qmin, qmax, BOUND_TOL),
          qmin >= -1.0e-12 and qmax <= 1.0 + BOUND_TOL)
    return gz, gp, types, qmap


# ------------------------------------------------ holonomy (report)
def holonomy(T, F):
    print("\n-- holonomy check (secondary, REPORTED never gated): "
          "step scaling of transported increments on M = %d..%d"
          % (HOLO_LAD[0], HOLO_LAD[-1]))
    spec_h = {}
    for M in HOLO_LAD:
        lam, V = np.linalg.eigh(T[:M, :M])
        spec_h[M] = qsb.sign_fix(V[:, :K_RANK])
    ward_iso = 0.0
    med_ang, med_rad, med_tot = {}, {}, {}
    sig_max = 0.0
    for s in HOLO_STEPS:
        chain = list(range(HOLO_LAD[0], HOLO_LAD[-1] + 1, s))
        angs, rads, tots = [], [], []
        for Ma, Mb in zip(chain, chain[1:]):
            Va, Vb = spec_h[Ma], spec_h[Mb]
            a0 = Va[:NPAD, :].T @ F
            a1 = Vb[:NPAD, :].T @ F
            S = Vb[:Ma, :].T @ Va
            U, sv, Wt = np.linalg.svd(S)
            sig_max = max(sig_max, float(sv[0]))
            Q = U @ Wt
            Qa1 = Q.T @ a1
            ward_iso = max(ward_iso, float(np.max(np.abs(
                np.linalg.norm(Qa1, axis=0)
                - np.linalg.norm(a1, axis=0)))))
            dlt = np.linalg.norm(Qa1 - a0, axis=0)
            rad = np.abs(np.linalg.norm(a1, axis=0)
                         - np.linalg.norm(a0, axis=0))
            ang = np.sqrt(np.maximum(dlt ** 2 - rad ** 2, 0.0))
            tots.append(dlt)
            rads.append(rad)
            angs.append(ang)
        med_ang[s] = float(np.median(np.stack(angs)))
        med_rad[s] = float(np.median(np.stack(rads)))
        med_tot[s] = float(np.median(np.stack(tots)))
        print("  step s=%d (%d pairs): median per-step increment = "
              "%.3e (radial %.3e, angular %.3e)"
              % (s, len(chain) - 1, med_tot[s], med_rad[s],
                 med_ang[s]))
    e_ang_12 = math.log2(med_ang[2] / max(med_ang[1], QF_FLOOR))
    e_ang_24 = math.log2(med_ang[4] / max(med_ang[2], QF_FLOOR))
    e_rad_12 = math.log2(med_rad[2] / max(med_rad[1], QF_FLOOR))
    e_rad_24 = math.log2(med_rad[4] / max(med_rad[2], QF_FLOOR))
    print("  measured step-scaling exponents log2(m(2s)/m(s)): "
          "ANGULAR %.2f (1->2), %.2f (2->4) [Kato-holonomy "
          "expectation ~ 2]; RADIAL %.2f, %.2f [level slide "
          "expectation ~ 1]"
          % (e_ang_12, e_ang_24, e_rad_12, e_rad_24))
    check("G2.1 holonomy isometry Ward: max | ||Q^T a|| - ||a|| | "
          "= %.1e <= %.0e; max overlap singular value = %.6f <= "
          "1 + 1e-12" % (ward_iso, WARD_ISO, sig_max),
          ward_iso <= WARD_ISO and sig_max <= 1.0 + 1.0e-12)


# ------------------------------------------------ controls
def run_controls(c_cont, alpha_deep, ka_deep, mu_deep):
    print("\n-- controls (must fire; fire rule = "
          "qf_spectral_bundle_probe.control_bundle verbatim)")
    rng = np.random.default_rng(SEED)
    pos = np.sort(rng.uniform(0.5, 2.0 * alpha_deep, ka_deep))
    cat_s, _dd = core.atom_lags_at(alpha_deep, M_TOP_DEEP, pos,
                                   mu_deep[:ka_deep])
    Ts = sla.toeplitz((c_cont + cat_s)[:M_TOP_DEEP])
    fire_s, det_s = qsb.control_bundle(Ts, qsb.CTRL_LAD_S,
                                       "scramble")
    check("CS position-scramble control (deep comb, %d atoms) "
          "fires" % ka_deep, fire_s, det_s)

    r1 = epx.lattice_r1(EP_NCAP)
    bb = np.asarray(r1, float) / 2.0
    lamE = epx.dirichlet_vonmangoldt(bb, EP_NCAP)
    supp = np.nonzero(np.abs(lamE) > 1.0e-9)[0]
    supp = supp[supp >= 2]
    posE = np.log(supp.astype(float))
    masE = 2.0 * lamE[supp] / np.sqrt(supp.astype(float))
    catE, _dd = core.atom_lags_at(0.5 * EP_MMAX * D, EP_MMAX, posE,
                                  masE)
    cont = srp.continuum_lags(EP_MMAX)
    TE = sla.toeplitz((cont + catE)[:EP_MMAX])
    fire_e, det_e = qsb.control_bundle(TE, qsb.CTRL_LAD_E, "epstein")
    check("CE Epstein control (x^2+5y^2, %d negative atom sites) "
          "fires" % int(np.sum(lamE[2:] < -1.0e-9)), fire_e, det_e)


# ------------------------------------------------ run
def run():
    print("=" * 78)
    print("QF OFFENSIVE strand 3 follow-up -- drainage decider: "
          "band weight q_f^T(X) on the 1e8 comb (X <= 18.375)")
    print("=" * 78)

    hits = ast_firewall()
    check("G0.1 AST firewall (drainage object uses no target "
          "information)", not hits, str(hits))
    bats, spec_sha = freeze_spec()
    check("G0.2 battery + ladders + blocks + bars + deep-comb spec "
          "SHA-256-frozen BEFORE any comb data is built here", True,
          "SHA256 %s..." % spec_sha[:16])
    check("G0.3 reach census: M_TOP = %d <= floor(64 ln %d) = %d "
          "(X = %.6f <= %.6f); sieve cover exp(X_top) + 2 = %d <= "
          "%d; runtime cap %.0f s predeclared"
          % (M_TOP_DEEP, ATOM_MAX_DEEP, M_CAP_DEEP, M_TOP_DEEP * D,
             math.log(ATOM_MAX_DEEP),
             int(math.exp(M_TOP_DEEP * D)) + 2, ATOM_MAX_DEEP,
             RUNTIME_CAP),
          M_TOP_DEEP <= M_CAP_DEEP
          and int(math.exp(M_TOP_DEEP * D)) + 2 <= ATOM_MAX_DEEP)

    # ---- comb + towers strictly after the freeze
    u_deep, mu_deep = build_deep_comb()
    T_par = build_parent_tower()
    T, c_cont, alpha_deep, ka_deep = build_deep_tower(
        u_deep, mu_deep, T_par)

    # ---- spectra on SLAD
    spec = spectral_pass(T, SLAD)
    F, names = battery_matrix(bats)
    pd_min = min(spec[M]["lam_min"] for M in SLAD)
    print("  PD margins (measured, never gated): lambda_min = "
          "%.3e (M %d) -> %.3e (M %d)"
          % (spec[M_TOP_BUN]["lam_min"], M_TOP_BUN,
             spec[M_TOP_DEEP]["lam_min"], M_TOP_DEEP))
    check("G1.6 measured PD: lambda_min = %.3e > -%.0e on every "
          "SLAD rung (measured output; no gate uses a PD margin or "
          "1/eps)" % (pd_min, PD_TOL), pd_min > -PD_TOL)

    # G1.5 bundle-probe reproduction Ward at M = 972
    q972 = float(np.max(np.sum((spec[M_TOP_BUN]["Vb"][:NPAD, :].T
                                @ F) ** 2, axis=0)))
    gap972 = (spec[M_TOP_BUN]["lam7"] - spec[M_TOP_BUN]["lam6"]) \
        / spec[M_TOP_BUN]["lam7"]
    check("G1.5 bundle reproduction Ward at M = %d: max band q_f = "
          "%.4f vs frozen %.4f (dev %.1e), rel gap = %.4f vs frozen "
          "%.4f (dev %.1e), both <= %.0e; thr count = %d (== 6), "
          "deep count = %d (== 1)"
          % (M_TOP_BUN, q972, REPRO_Q972, abs(q972 - REPRO_Q972),
             gap972, REPRO_GAP972, abs(gap972 - REPRO_GAP972),
             REPRO_TOL, spec[M_TOP_BUN]["nn"],
             spec[M_TOP_BUN]["nn_deep"]),
          abs(q972 - REPRO_Q972) <= REPRO_TOL
          and abs(gap972 - REPRO_GAP972) <= REPRO_TOL
          and spec[M_TOP_BUN]["nn"] == K_RANK
          and spec[M_TOP_BUN]["nn_deep"] == 1)

    # ---- structure gates + drainage decider + holonomy
    s1, s2, s3, cross = structure_gates(spec, F)
    gz, gp, types, _qmap = drainage(spec, F, names)
    holonomy(T, F)

    # ---- controls
    run_controls(c_cont, alpha_deep, ka_deep, mu_deep)

    # ---- runtime guard (predeclared)
    dt = time.time() - T_START
    check("G0.4 runtime %.1f s <= predeclared cap %.0f s"
          % (dt, RUNTIME_CAP), dt <= RUNTIME_CAP)

    # ---- verdict (preregistered decision order)
    guards_ok = all(ok for (n, ok) in CHECKS
                    if not n.startswith(("CS", "CE")))
    controls_ok = all(ok for (n, ok) in CHECKS
                      if n.startswith(("CS", "CE")))
    structure_broke = not (s1 and s2 and s3)
    if not (guards_ok and controls_ok):
        verdict = "QF-DRAINAGE-UNDECIDED (invalid run)"
    elif structure_broke:
        verdict = "QF-STRUCTURE-CHANGES"
    elif gz:
        verdict = "QF-DRAINS-TO-ZERO"
    elif gp:
        verdict = "QF-SETTLES-POSITIVE"
    else:
        verdict = "QF-DRAINAGE-UNDECIDED"

    n_gate = sum(1 for (_n, ok) in GATES if ok)
    n_chk = sum(1 for (_n, ok) in CHECKS if ok)
    print("\nVERDICT: %s" % verdict)
    print("GATES %d/%d, GUARDS+CONTROLS %d/%d, types %s, runtime "
          "%.1f s" % (n_gate, len(GATES), n_chk, len(CHECKS),
                      "".join(types), time.time() - T_START))
    if verdict == "QF-DRAINS-TO-ZERO":
        print("CONSEQUENCE (stated plainly): the kernel pairing is "
              "asymptotically VANISHING with the measured rates "
              "above -- the diagonal-gram wall dissolves at depth: "
              "the transported coordinates of the bundle frame "
              "become Cauchy-to-zero and Gate 3's remaining "
              "obstruction empties out.  The Feshbach 6x6 block "
              "would converge to 0 (the reduction becomes "
              "unnecessary rather than impossible); the hierarchical"
              "-basis module inherits a vanishing target.  NOT "
              "claimed: X -> infinity, eps-uniformity, RH.")
    elif verdict == "QF-SETTLES-POSITIVE":
        print("CONSEQUENCE (stated plainly): the wall is a TRUE "
              "positive per-function constant -- the settled levels "
              "above are the new named objects, and the Feshbach "
              "6x6 / boundary-triple treatment of the near-kernel "
              "block becomes MANDATORY for the diagonal route.  "
              "NO RH claim.")
    elif verdict == "QF-STRUCTURE-CHANGES":
        print("CONSEQUENCE (stated plainly): the rank/gap structure "
              "changes qualitatively on the deeper comb (typed "
              "above: S1 gap / S2 deep count / S3 alignment) -- the "
              "6-band bundle object of the parent probes is not the "
              "right invariant at this depth and the object "
              "question REOPENS before any drainage statement can "
              "be made.  NO RH claim.")
    else:
        print("CONSEQUENCE (stated plainly): the drainage bars are "
              "not reached either way at X = %.4f -- the Z/P/U "
              "split and the per-function decision depths are "
              "printed above; no module of the offensive is opened "
              "or closed by this run.  NO RH claim."
              % (M_TOP_DEEP * D))
    return 0 if (guards_ok and controls_ok) else 1


if __name__ == "__main__":
    sys.exit(run())
