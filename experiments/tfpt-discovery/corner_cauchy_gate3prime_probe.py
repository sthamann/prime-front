#!/usr/bin/env python3
"""QF-OFFENSIVE strand 1, follow-up -- THE CORNER-NATIVE GATE 3'
DECIDER (direct precondition test for v764):
corner_cauchy_gate3prime_probe.

Exploration only (tfpt-experiment firewall): NOT wired into run_all.py,
no ledger row, no paper edit, no website edit, NO RH CLAIM, and this
probe writes no files.  It never reads a zero ordinate and never
evaluates the target before every source object is built and SHA-256
frozen (same discipline as all parent probes).

INPUT STATE (frozen findings, none re-adjudicated here):
  *  qf_contract_necessity_probe -- QF-GAUGE (5/5 gates, 14/14
     guards+controls): Gate 3's full-ladder Cauchy demand on q_f was
     STRONGER than the diagonal contract needs.  A single epsilon-net
     subsequence (density 0.144) makes all 14 q_f profiles Cauchy at
     the parent bars; the corner objects are BLIND to q_f motion
     (corr_adj = +0.038; the dq = 0.3369 mode-entry jump at M = 888
     leaves corner increments at routine level; 370 cross-cluster
     pairs, median rho = 1.13).  MEASURED CAVEATS carried in: (i)
     the EXT corner-increment envelope OSCILLATES (eps 1e-3 head ->
     tail med5: 8.8e-4 -> 1.8e-3 on 824..972) -- raw endpoint gates
     are the wrong instrument (the compat-eps3 lesson); (ii) the
     controls discriminate via POSITIVITY (sandwich/monotonicity),
     not corner size (for lam << -eps the Yosida symbol is ~ 1, so
     corner entries of indefinite matrices stay bounded off the
     poles); (iii) Q4: the eps/X limits do not commute uniformly --
     the ORDER X-before-eps is enforced (every gate below lives at
     FIXED eps along the X ladder; no eps -> 0 claim).
  *  handoff_compat_eps3_probe / v768 -- the oscillation-aware cell
     statistic pattern reused here verbatim in spirit: 5-rung
     medians, second-half fitted slope, Dini/summability tail share.
  *  Contract PRIME.KMS.INDUCTIVE_STATE.02 + GramCompactness.lean:
     the objects the diagonal contract actually consumes are the
     ENTRYWISE corner values <f_i, Y_eps f_j> on fixed battery
     corners -- Gate 3' therefore gates on corner-increment Cauchy
     smallness directly; q_f is bounded gauge (report only).

SINGLE QUESTION (preregistered): are the E_Y Gram corner entries
entrywise Cauchy along the deepest honestly reachable window ladder,
at each gated eps, under the oscillation-aware statistic -- i.e. is
Gate 3' (the weakened, contract-native form frozen by the parent
audit) DECIDED POSITIVELY on the objects themselves?

DEEPER-LADDER LEVER (predeclared by OWN compute budget; this probe
does NOT depend on any other worker's comb extension): deep comb cap
ATOM_MAX_DEEP = 16,000,000 (ln = 16.5881, M_CAP_DEEP =
floor(64 ln 1.6e7) = 1061); M_TOP_DEEP = 1060 is frozen as the
deepest step-4-aligned rung (X = 16.5625); sieve cover
exp(16.5625) + 2 = 15,595,611 <= 16,000,000.  The extension is the
deployed generator (core.von_mangoldt_table) at a larger cap -- no
new information class; guards tie it to the deployed table (exact
overlap on [0, 400000]), to the parent tower (float-exact 824
prefix), to the Chebyshev envelope on [100, 1.6e7], and to the
parent-audit anchors (q_f(824), EXT drift, nn(888), the 824..972
corner-envelope numbers reproduced).  This adds 1.375 X units and 22
rungs beyond the 972 surface where the envelope oscillation was
seen: the deep rungs decide whether it was a shallow-window artifact.

FROZEN CONSTRUCTION: full ladder FULL_LAD = 256..1060 step 4 (202
rungs, 201 increments); frozen module-1 battery (4 boxes + 3 hats
per R, R in {1, 2}, l2-normalized, NPAD = 128); one dense eigh per
rung; corner objects E_Y^eps[i,j] = <f_i, Y_eps f_j> =
C^T diag(lam/(lam+eps)) C (bounded by the sandwich, no 1/eps
anywhere) at the gated eps set EPS_GATED = (1e-1, 1e-2, 1e-3);
CORNER-CELL SET (predeclared): ALL entry pairs (i <= j) WITHIN each
R-group -- 28 cells per group (7 diagonal + 21 off-diagonal), 56
cells total, x 3 eps = 168 gated cells (the contract needs entrywise
corners, not just diagonals; cross-R pairs are excluded by
declaration: the contract's corners live per local observable
algebra).  Per-eps scale (parent convention) scale_eps =
sqrt(max diag * min diag) of E_Y at the first rung; scaling is
constant per eps and cancels from every ratio/slope/share gate.

GATES (all frozen numerically BEFORE the first run; slope statistics
are declared gate statistics on bounded quantities, not proof-grade
claims).  Per corner cell (entry, eps), on the increment profile
inc(k) = |E_Y(M_{k+1}) - E_Y(M_k)|[i,j] / scale_eps over the 201
ladder steps (X of the upper rung as abscissa):
  S1 med5 ratio:   median(inc last 5) / max(median(inc first 5),
                   1e-12) <= RATIO_BAR = 0.5   (the compat-eps3 C2
                   pattern: single atom-burst rungs cannot break a
                   cell);
  S2 second-half slope: least-squares slope of log(inc) vs X over
                   the last 101 increments <= SLOPE_TOL = +0.02 per
                   X unit (falling, or at worst marginally rising
                   within the declared oscillation tolerance);
  S3 summability proxy: tail-quarter share of total variation,
                   sum(inc last 51) / sum(inc all) <= TV_BAR = 0.25
                   (a flat profile gives 51/201 = 0.254: the gate
                   demands strictly better than flat).
  A cell PASSES iff S1 and S2 and S3.
VERDICT COUNTS (frozen; n_e = passing cells of 56 at eps e):
  GATE3PRIME-CONVERGES = guards ok AND both controls fire AND
      n(1e-1) = 56 AND n(1e-2) = 56 AND n(1e-3) >= 51 (>= 90%);
  GATE3PRIME-PARTIAL   = guards ok AND both controls fire AND
      n(1e-1) >= 51 AND n(1e-2) >= 51 AND n(1e-3) >= 28, not
      CONVERGES (every failing cell is NAMED);
  GATE3PRIME-DEAD      = anything else: majority corner failures
      (the corner increments do not fall -- the gauge reading of
      q_f was a false hope and the wall returns at the corner
      level), OR a control spuriously converges, OR a guard fails
      (invalid run, stated as such).

SUBSEQUENCE REPORT (never gated): the parent's greedy epsilon-net
rule (ETA = 0.03, sup-norm, ladder order, first-center membership)
recomputed on this deeper ladder for BOTH profiles: (a) q_f-native
(14-dim, THR_NULL = 1e-4) and (b) corner-native (168-dim: the
UNSCALED E_Y entries of all 56 cells at the 3 gated eps -- bounded
by 1, same footing).  Reported: cluster counts, largest-cluster
densities, and the comparison the parent asked for (does the corner
picture need subsequences at all, or is it full-ladder Cauchy
already -- the gates above answer the Cauchy half; the net density
is the honesty metric).  q_f boundedness in [0, 1] is REPORTED
(KILL audit) -- q_f appears in NO gate.

GUARDS (must pass or the run is invalid):
  G0.1 AST firewall; G0.2 SHA-256 freeze of battery bytes + ladder +
  cell set + eps set + every bar + net rule + deep-comb spec + the
  control fire rule BEFORE any comb data is built here; G0.3 reach
  census (1060 <= 1061, sieve cover) + runtime cap 900 s
  predeclared; G1.1 deep-table overlap == deployed core table on
  [0, 400000] EXACTLY; G1.2 Chebyshev envelope kappa on [100, 1.6e7]
  <= KAPPA_REF + 1e-6; G1.3 parent tower comb consistency (zeta-free
  Gauss double sieve == deployed masses, <= 1e-12); G1.4 prefix
  Ward: deep tower's leading 824 block == parent tower <= 1e-12;
  G1.5 parent-audit anchor reproduction: max q_f(824) = 0.446 +-
  2e-3, worst 824..972 drift (MID5/LAST5 verbatim) = 0.5636 +- 2e-3,
  near-null count at M = 888 = 6, AND the parent audit's corner
  envelope numbers at eps = 1e-3 (max-entry increments, 824..972
  window): head med5 = 8.8e-4 +- 1e-5, tail med5 = 1.8e-3 +- 1e-4;
  G1.6 real-data operator sandwich at M = 512 and 1060 (Yosida
  eigenvalues in [-1e-9, 1 + 1e-9] at every gated eps); G1.7
  boundedness/KILL audit: every corner entry in [-1-1e-9, 1+1e-9],
  every scale in [1e-3, 1.5], every q_f and every increment >= 0 and
  bounded -- bounded forms only, no 1/eps, no PD assumption, no
  target data in any gate; G2.1 spectral-vs-dense-solve Ward on E_Y
  at M = 900, eps = 1e-3, <= 1e-8; G0.4 runtime.

CONTROLS (mandatory, must fire; fire rule stated plainly): the
parent audit MEASURED that corner-increment size does NOT
discriminate corrupted combs (indefinite spectra keep the Yosida
symbol ~ 1 away from the poles), so the frozen fire rule is the
POSITIVITY rule verbatim (yosida_handoff_probe.control_yosida at
M_CTRL = 512): FIRE = sandwich break (g outside [-0.01, 1.01]) OR
battery eps-monotonicity violation (< -1e-6) OR singular Yosida
(|lam + eps| < 1e-12).  CS position scramble (positions uniform in
(0.5, 2 alpha_deep), masses kept, seed 7, on the DEEP comb, tower
M_TOP_DEEP) and CE Epstein x^2 + 5y^2 atoms (epstein_firewall_probe
read-only, tower cap M = 640).  The control-side corner increments
on the mini-ladder 480..512 step 4 at eps = 1e-2 are PRINTED as
context (report only, per the measured lesson).  A control that
keeps sandwich + monotonicity + regularity has spuriously
converged: verdict DEAD.

STOP-LIST (binding, inherited): no target decomposition / Cholesky /
zeros; no bare A^{-1}; no 1/eps bounds in gates; no fits beyond the
declared slope gate statistics; no q_f in any gate; SHA-freeze
before comb data; NO RH claim; probe writes no files; runtime cap
900 s.  X-before-eps order enforced: all gates live at fixed eps
along the X ladder; nothing here claims eps -> 0 closure or
eps-uniformity.

RESULTS (2026-08-05, first and only preregistered run, 10.4 s;
CELLS 34/168 (n(1e-1) = 31/56, n(1e-2) = 3/56, n(1e-3) = 0/56),
GUARDS+CONTROLS 14/14, verdict GATE3PRIME-DEAD, majority corner
failures -- the deeper-ladder lever decided it, and it decided it
NEGATIVELY):
  *  DEEP EXTENSION VALID: ka = 1,007,385 atoms to e^16.5625 (3.6x
     the 4e6 comb); overlap with the deployed table exact (0.0);
     kappa = 0.038821 unchanged on [100, 1.6e7]; prefix Ward vs the
     parent tower 2.0e-14; parent-audit anchors reproduced: max
     q_f(824) = 0.4459 (dev 1.3e-4), worst 824..972 drift 0.5636
     (dev 1.4e-5), nn(888) = 6, corner envelope head/tail med5 at
     eps 1e-3 = 8.7873e-4 / 1.7906e-3 (dev 1.3e-6 / 9.4e-6).  PD
     margins (measured, never gated): 5.289e-5 (256) -> 6.459e-6
     (972) -> 5.383e-6 (1060); sandwich at 512 + 1060 holds with
     Yosida eigenvalues in [5.4e-5, 1 - 5.8e-5]; dense-solve Ward
     5.3e-13; runtime 10.4 s <= 900 s.
  *  THE CENTRAL MEASUREMENT (max-entry envelope, med5, scaled):
     the corner increments FALL from the ladder head to X ~ 12.9
     (eps = 1e-3: ~1.4e-3 at M = 256 -> 8.79e-4 at the 824 window
     -- exactly the falling regime every parent probe certified on
     rungs <= 824) and then RISE on the deep rungs: 824-head ->
     972-tail -> deep-tail (1044..1060) med5 = 3.05e-3 -> 6.44e-3
     -> 5.60e-3 (eps 1e-1), 1.16e-3 -> 1.25e-3 -> 3.49e-3 (1e-2),
     8.79e-4 -> 1.79e-3 -> 3.67e-3 (1e-3).  The parent audit's
     "envelope oscillation" was the ONSET of this rise, not a
     shallow-window artifact: 22 additional rungs to X = 16.5625
     confirm sustained growth (second-half slopes at 1e-3:
     +0.10..+0.34 per X unit, fitted over 101 increments).
  *  CELL TABLE (frozen bars 0.5 / +0.02 / 0.25): eps = 1e-1:
     31/56 pass; the 25 failures are mostly S2 slope marginals
     (+0.001..+0.116) and R1 deep-edge ratios (box[R/2,R] rows up
     to 1.91).  eps = 1e-2: 3/56 pass (R1:box[0,R]*box[0,R/2],
     R2:box[0,R]*box[0,R], R2:box[0,R]*box[R/2,R]); typical
     failures ratio 0.6..14.9 with positive second-half slopes.
     eps = 1e-3: 0/56 pass -- every cell fails at least S2 (slopes
     +0.101..+0.344/X) and mostly S3 too (TV tail shares
     0.24..0.44 vs flat = 0.254); worst med5 ratio 29.25
     (R1:box[R/2,R]*box[R/2,R]).  The failure is broad-spectrum
     across boxes, hats, diagonal and off-diagonal, both R-groups:
     NOT a single bad channel.
  *  SUBSEQUENCE COMPARISON (report): corner-native net (168-dim
     unscaled entries, ETA 0.03): 4 clusters, largest density
     0.431 (87/202) -- vs q_f-native on the same deep ladder: 20
     clusters, largest density 0.134.  The corner LEVELS are far
     more coherent than q_f (3.2x denser, 4 vs 20 clusters), but
     level coherence is not increment summability: the levels move
     slowly yet persistently.  q_f boundedness report: all q in
     [1.8e-3, 0.6601] within [0, 1]; q_f appears in no gate.
  *  CONTROLS both fire via the positivity rule as frozen: CS
     scramble (deep comb, 1,007,385 atoms) lambda_min = -6.41e+3,
     252/512 negative eigenvalues, sandwich max g = 5.4, 31
     monotonicity violations; CE Epstein lambda_min = -3.32e+1,
     189/512 negative, min g = -2.5, max g = 23, 56 violations.
     Context report reconfirms the measured lesson: control corner
     med increments stay ORDINARY (4.5e-4 / 4.1e-4 vs real 3.3e-3)
     -- positivity, not corner size, separates.  KILL audit PASS:
     corners bounded by 0.7031 (sandwich), scales 0.017 / 0.087 /
     0.359, all increments >= 0, no 1/eps, no fits beyond the
     declared slope statistics, no target data.
  *  CONSEQUENCE FOR v764 (stated plainly): the v764 precondition
     is NOT met.  At fixed eps <= 1e-2 the X-ladder Cauchy
     increments of the very objects the diagonal contract consumes
     rise beyond X ~ 13 on the deepest honestly reachable surface
     -- the reachable X-limit of the corner entries is not
     certified, and no assembly of v760 (anti-alias) + v761
     (atom-pole Abel) on top of this can proceed.  Precisely
     stated: the parent audit's RELATIVE finding stands (corners
     are blind to q_f gauge jumps; nothing here re-couples q_f to
     the value), but its optimistic extension -- that the corner
     envelope keeps falling -- is REFUTED: the wall returns at the
     corner level as a depth-driven rise, visible from X ~ 13.5 at
     every gated eps below 1e-1.  The rise coincides with the
     regime where the per-cell comb fluctuation amplitude (~
     2(psi(e^u) - e^u)/e^{u/2}) grows through the battery scale;
     whether a fluctuation-normalized corner increment still falls
     there is a DIFFERENT, not-yet-frozen question -- named next
     surfaces (not probed here, no verdict implied): (i) a
     fluctuation-normalized restatement of Gate 3' (preregister
     the normalization first, on parent rungs only), (ii) the
     eps = 1e-1 decade, where 31/56 cells still pass -- locate the
     eps detachment point on a refined eps ladder, (iii) deeper
     combs (4e7-class) to test whether the rise saturates.  NO RH
     claim, no X -> infinity claim, no eps -> 0 claim.

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/corner_cauchy_gate3prime_probe.py
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
import yosida_handoff_probe as yhp  # noqa: E402
import epstein_firewall_probe as epx  # noqa: E402

T_START = time.time()

# ------------------------------------------------ frozen specification
D = srp.DGRID                        # 1/64, dyadic float-exact
ATOM_MAX_DEEP = 16000000             # own predeclared deep comb cap
M_CAP_DEEP = int(math.floor(math.log(ATOM_MAX_DEEP) / D))  # 1061
M_TOP_DEEP = 1060                    # deepest step-4-aligned rung
M_TOP_PAR = 824                      # parent cap
FULL_LAD = list(range(256, 1061, 4))         # 202 rungs
I824 = FULL_LAD.index(824)                   # 142
I972 = FULL_LAD.index(972)                   # 179
MID5 = slice(17, 22)                 # on the 824..972 sub-ladder
LAST5 = slice(33, 38)                # (parent-audit anchor verbatim)

R_BAT = (1.0, 2.0)                   # frozen module-1 local battery
NPAD = 128                           # max battery support in cells
EPS_GATED = (1.0e-1, 1.0e-2, 1.0e-3)                # gated eps set
THR_NULL = 1.0e-4                    # q_f threshold (report only)

RATIO_BAR = 0.5                      # S1 med5(last)/med5(first)
SLOPE_TOL = 0.02                     # S2 second-half slope cap (/X)
TV_BAR = 0.25                        # S3 tail-quarter TV share
N_MED = 5                            # median block size
QF_FLOOR = 1.0e-12                   # denominator floor
N3_CONV = 51                         # CONVERGES: eps=1e-3 pass floor
N_PART = 51                          # PARTIAL: upper-eps pass floor
N3_PART = 28                         # PARTIAL: eps=1e-3 pass floor

ETA_NET = 0.03                       # subsequence net radius (report)
PARENT_QF_MAX = 0.446                # G1.5 anchor (parent probes)
PARENT_DRIFT_WORST = 0.5636          # G1.5 anchor (qf probe, EXT)
PARENT_NN_888 = 6                    # G1.5 anchor (qf probe)
ENV_HEAD_REF = 8.8e-4                # G1.5 anchor (parent audit)
ENV_TAIL_REF = 1.8e-3                # G1.5 anchor (parent audit)
ENV_HEAD_TOL = 1.0e-5                # (refs printed to 2 sig digits)
ENV_TAIL_TOL = 1.0e-4
REPRO_TOL = 2.0e-3                   # q/drift anchor tolerance
COMB_DEV_BAR = 1.0e-12               # G1.3 sieve == deployed masses
PREFIX_WARD = 1.0e-12                # G1.4 prefix max abs dev
SANDWICH_TOL = 1.0e-9                # G1.6 sandwich slack
BOUND_TOL = 1.0e-9                   # G1.7 boundedness slack
SCALE_LO, SCALE_HI = 1.0e-3, 1.5     # G1.7 corner scale audit band
WARD_SPEC = 1.0e-8                   # G2.1 dense-solve Ward
M_WARD, EPS_WARD = 900, 1.0e-3       # G2.1 Ward rung and eps
RUNTIME_CAP = 900.0                  # seconds, predeclared (15 min)

M_CTRL = 512                         # control spectral rung (parent)
CTRL_LAD = list(range(480, 513, 4))  # control corner context ladder
CTRL_EPS = 1.0e-2                    # control corner context eps
EP_NCAP = 34000                      # Epstein Lambda_E table reach
EP_MMAX = 640                        # Epstein control tower cap
SEED = 7

BANNED = ("zetazero", "nzeros", "isprime", "primerange", "nextprime",
          "prevprime", "primepi", "sympy")

CHECKS = []       # guards + controls: all must pass, else invalid run
CELLS = []        # per (entry, eps) cell results: feed the verdict


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok)))
    print("[%s] %s%s" % ("PASS" if ok else "FAIL", name,
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
    """Battery bytes + ladder + cell set + eps set + bars + net rule
    + deep-comb spec + control fire rule, SHA-256 frozen BEFORE any
    comb data is built in this probe."""
    bats = {}
    hsh = hashlib.sha256()
    hsh.update(("corner-cauchy-gate3prime spec: 4 boxes + 3 hats per "
                "R, l2-norm, D=%.10f, R=%s; deep comb = deployed "
                "von_mangoldt_table sieve at cap %d, M_CAP=%d, "
                "M_TOP_DEEP=%d (parent %d); FULL_LAD=%s; anchors "
                "I824=%d I972=%d MID5=[17:22] LAST5=[33:38]; corners "
                "= E_Y entries, cells = all pairs i<=j within each "
                "R-group (56), eps gated=%s, scale = sqrt(maxdiag*"
                "mindiag) at first rung; stats on 201 step-4 "
                "increments, X of upper rung: S1 med%d ratio<=%g, "
                "S2 second-half log-slope<=%+g/X over last 101, S3 "
                "TV tail quarter (51) share<=%g; verdict: CONVERGES "
                "n1=n2=56 & n3>=%d, PARTIAL n1,n2>=%d & n3>=%d, else "
                "DEAD; subsequence report: greedy net ladder-order "
                "first-center ETA=%g on (a) q_f 14-dim thr=%g (b) "
                "unscaled corner entries 168-dim; anchors qfmax=%g "
                "drift=%g nn888=%d envhead=%g+-%g envtail=%g+-%g "
                "tol=%g; guards comb<=%g prefix<=%g sandwich<=%g "
                "bound<=%g scale=[%g,%g] ward<=%g (M=%d,eps=%g) "
                "runtime<=%g; controls: POSITIVITY fire rule "
                "verbatim (control_yosida, M=%d), corner context "
                "minilad=%s eps=%g REPORT ONLY, epcap=%d epM=%d "
                "seed=%d; X-before-eps enforced, no eps->0 claim"
                % (D, R_BAT, ATOM_MAX_DEEP, M_CAP_DEEP, M_TOP_DEEP,
                   M_TOP_PAR, FULL_LAD, I824, I972, EPS_GATED, N_MED,
                   RATIO_BAR, SLOPE_TOL, TV_BAR, N3_CONV, N_PART,
                   N3_PART, ETA_NET, THR_NULL, PARENT_QF_MAX,
                   PARENT_DRIFT_WORST, PARENT_NN_888, ENV_HEAD_REF,
                   ENV_HEAD_TOL, ENV_TAIL_REF, ENV_TAIL_TOL,
                   REPRO_TOL, COMB_DEV_BAR, PREFIX_WARD,
                   SANDWICH_TOL, BOUND_TOL, SCALE_LO, SCALE_HI,
                   WARD_SPEC, M_WARD, EPS_WARD, RUNTIME_CAP, M_CTRL,
                   CTRL_LAD, CTRL_EPS, EP_NCAP, EP_MMAX,
                   SEED)).encode())
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


def corner_cells(names):
    """All entry pairs (i <= j) within each R-group: 56 cells."""
    cells = []
    for lo, hi in ((0, 7), (7, 14)):
        for i in range(lo, hi):
            for j in range(i, hi):
                cells.append((i, j))
    labels = ["%s*%s" % (names[i], names[j].split(":", 1)[1])
              for (i, j) in cells]
    return cells, labels


def lin_slope(xs, ys):
    A = np.vstack([np.ones_like(xs), xs]).T
    coef, *_ = np.linalg.lstsq(A, ys, rcond=None)
    return float(coef[1])


# ------------------------------------------------ towers
def build_parent_tower():
    alpha = 0.5 * M_TOP_PAR * D
    ka, masks, dev_m = srp.channel_masks(alpha)
    check("G1.3 parent tower comb consistency (zeta-free Gauss double "
          "sieve == deployed masses, rel dev <= %.0e)" % COMB_DEV_BAR,
          dev_m <= COMB_DEV_BAR,
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
          "deployed core table on [0, %d] EXACTLY" % core.ATOM_MAX,
          dev == 0.0, "max abs dev %.1e" % dev)
    nn = np.nonzero(lam_deep > 0.0)[0]
    u_deep = np.log(nn.astype(float))
    mu_deep = 2.0 * lam_deep[nn] / np.sqrt(nn.astype(float))
    psi = np.cumsum(lam_deep[nn])
    keep = nn.astype(float) >= core.KAPPA_X0
    kappa = float(np.max(np.abs(psi[keep] - nn[keep].astype(float))
                         / nn[keep].astype(float)))
    check("G1.2 deep-range Chebyshev envelope: kappa = %.6f over all "
          "jump points of psi(x)/x in [%.0f, %d] <= %.6f"
          % (kappa, core.KAPPA_X0, ATOM_MAX_DEEP,
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
    print("  deep extension census: ka = %d atoms to e^%.4f"
          % (ka, 2.0 * alpha))
    return T, c_cont, alpha, ka


# ------------------------------------------------ spectral machinery
def spectral_pass(T, F):
    out = []
    for M in FULL_LAD:
        lam, V = np.linalg.eigh(T[:M, :M])
        C = V[:NPAD, :].T @ F
        out.append(dict(M=M, lam=lam, C=C,
                        nn=int(np.sum(lam <= THR_NULL))))
    return out


def qf_of(blk):
    idx = blk["lam"] <= THR_NULL
    return (blk["C"][idx] ** 2).sum(axis=0)


def corner_of(blk, eps):
    g = blk["lam"] / (blk["lam"] + eps)
    E = blk["C"].T @ (blk["C"] * g[:, None])
    return 0.5 * (E + E.T)


def greedy_net(vmat):
    centers, assign = [], []
    for r in range(vmat.shape[0]):
        hit = -1
        for ci, c in enumerate(centers):
            if float(np.max(np.abs(vmat[r] - c))) <= ETA_NET:
                hit = ci
                break
        if hit < 0:
            centers.append(vmat[r].copy())
            hit = len(centers) - 1
        assign.append(hit)
    return np.array(assign, int), centers


# ------------------------------------------------ cell adjudication
def cell_stats(inc_cell, xs_up):
    """Frozen oscillation-aware statistic on one (entry, eps) cell."""
    n = len(inc_cell)
    med_first = float(np.median(inc_cell[:N_MED]))
    med_last = float(np.median(inc_cell[-N_MED:]))
    ratio = med_last / max(med_first, QF_FLOOR)
    half = n // 2
    slope = lin_slope(xs_up[half:],
                      np.log(np.maximum(inc_cell[half:], 1.0e-300)))
    n_q = int(math.ceil(n / 4.0))
    tv = float(np.sum(inc_cell[-n_q:]) / max(np.sum(inc_cell),
                                             QF_FLOOR))
    ok = ratio <= RATIO_BAR and slope <= SLOPE_TOL and tv <= TV_BAR
    return ok, ratio, slope, tv


def corner_gate_block(spec, cells, labels):
    print("\n-- Gate 3'(a): corner-increment Cauchy per (entry, eps) "
          "cell (S1 med5 ratio <= %g, S2 second-half slope <= %+g/X, "
          "S3 TV tail share <= %g)" % (RATIO_BAR, SLOPE_TOL, TV_BAR))
    n = len(FULL_LAD)
    xs_up = np.array([FULL_LAD[k + 1] * D for k in range(n - 1)])
    EY = {eps: np.stack([corner_of(b, eps) for b in spec])
          for eps in EPS_GATED}                   # (202, 14, 14)
    scales = {}
    for eps in EPS_GATED:
        dg = np.diag(EY[eps][0])
        scales[eps] = float(np.sqrt(np.max(dg) * np.min(dg)))
    print("  corner scales (first rung): %s"
          % "  ".join("eps=%g: %.3f" % (e, scales[e])
                      for e in EPS_GATED))
    dif = {eps: np.abs(np.diff(EY[eps], axis=0)) / scales[eps]
           for eps in EPS_GATED}                  # (201, 14, 14)
    # max-entry envelope (parent-audit anchor material + report)
    incmax = {eps: dif[eps].max(axis=(1, 2)) for eps in EPS_GATED}
    for eps in EPS_GATED:
        h_par = float(np.median(incmax[eps][I824:I824 + 5]))
        t_par = float(np.median(incmax[eps][I972 - 5:I972]))
        t_deep = float(np.median(incmax[eps][-5:]))
        print("  max-entry envelope eps=%g: 824-window head med5 = "
              "%.4e, 972-window tail med5 = %.4e, DEEP tail med5 "
              "(1044..1060) = %.4e" % (eps, h_par, t_par, t_deep))
    env_head = float(np.median(incmax[1.0e-3][I824:I824 + 5]))
    env_tail = float(np.median(incmax[1.0e-3][I972 - 5:I972]))

    counts = {eps: 0 for eps in EPS_GATED}
    fails = {eps: [] for eps in EPS_GATED}
    print("  per-cell table (ratio / slope / tv per eps; bars %g / "
          "%+g / %g):" % (RATIO_BAR, SLOPE_TOL, TV_BAR))
    for c_i, (i, j) in enumerate(cells):
        parts = []
        for eps in EPS_GATED:
            ok, ratio, slope, tv = cell_stats(dif[eps][:, i, j],
                                              xs_up)
            CELLS.append((labels[c_i], eps, ok, ratio, slope, tv))
            counts[eps] += bool(ok)
            if not ok:
                fails[eps].append((labels[c_i], ratio, slope, tv))
            parts.append("e%g: %.2f/%+.3f/%.2f %s"
                         % (eps, ratio, slope, tv,
                            "ok" if ok else "FAIL"))
        print("    %-42s %s" % (labels[c_i], "  ".join(parts)))
    for eps in EPS_GATED:
        print("  eps = %-6g: %d/56 cells pass" % (eps, counts[eps]))
        for nm, ratio, slope, tv in fails[eps]:
            print("      FAIL %-42s ratio=%.3f slope=%+.3f tv=%.3f"
                  % (nm, ratio, slope, tv))
    # boundedness material
    cmax = max(float(np.max(np.abs(EY[eps]))) for eps in EPS_GATED)
    inc_min = min(float(np.min(dif[eps])) for eps in EPS_GATED)
    med_real = float(np.median(dif[CTRL_EPS].max(axis=(1, 2))))
    return counts, EY, scales, dict(cmax=cmax, inc_min=inc_min,
                                    env_head=env_head,
                                    env_tail=env_tail,
                                    med_real=med_real)


# ------------------------------------------------ subsequence report
def subsequence_report(spec, EY, cells, qmat):
    print("\n-- subsequence report (never gated; greedy net ETA = "
          "%g, parent rule verbatim)" % ETA_NET)
    n = len(FULL_LAD)
    corner_vec = np.zeros((n, len(cells) * len(EPS_GATED)))
    for k in range(n):
        cols = []
        for eps in EPS_GATED:
            cols.extend(EY[eps][k][i, j] for (i, j) in cells)
        corner_vec[k] = cols
    a_q, c_q = greedy_net(qmat)
    a_c, c_c = greedy_net(corner_vec)
    s_q = np.bincount(a_q)
    s_c = np.bincount(a_c)
    d_q = float(np.max(s_q)) / n
    d_c = float(np.max(s_c)) / n
    print("  q_f-native (14-dim): %d clusters, largest density %.3f "
          "(%d/%d rungs)" % (len(c_q), d_q, int(np.max(s_q)), n))
    print("  corner-native (unscaled E_Y entries, %d-dim): %d "
          "clusters, largest density %.3f (%d/%d rungs)"
          % (corner_vec.shape[1], len(c_c), d_c, int(np.max(s_c)), n))
    print("  comparison: the corner profile needs %s subsequence "
          "thinning than q_f (density ratio %.1fx, cluster count "
          "%d vs %d); the Cauchy half is decided by the gates above."
          % ("far less" if d_c > d_q else "no less",
             d_c / max(d_q, QF_FLOOR), len(c_c), len(c_q)))
    print("  q_f boundedness (report only, q_f in NO gate): all q "
          "in [%.1e, %.4f] within [0, 1]"
          % (float(np.min(qmat)), float(np.max(qmat))))
    return d_q, d_c


# ------------------------------------------------ controls
def control_corner_context(Tc, F):
    """REPORT ONLY: corner increments on the control mini-ladder
    (the parent audit measured these do NOT discriminate)."""
    EYs = []
    for M in CTRL_LAD:
        lam, V = np.linalg.eigh(Tc[:M, :M])
        C = V[:NPAD, :].T @ F
        g = lam / (lam + CTRL_EPS)
        E = C.T @ (C * g[:, None])
        EYs.append(0.5 * (E + E.T))
    incs = [float(np.max(np.abs(EYs[k + 1] - EYs[k])))
            for k in range(len(EYs) - 1)]
    return float(np.median(incs)), max(float(np.max(np.abs(E)))
                                       for E in EYs)


def run_controls(c_cont, alpha_deep, ka_deep, mu_deep, bats, F,
                 med_real):
    print("\n-- controls (must fire via the POSITIVITY rule -- the "
          "measured lesson: corner size does not discriminate)")
    rng = np.random.default_rng(SEED)
    pos = np.sort(rng.uniform(0.5, 2.0 * alpha_deep, ka_deep))
    cat_s, _dd = core.atom_lags_at(alpha_deep, M_TOP_DEEP, pos,
                                   mu_deep[:ka_deep])
    Ts = sla.toeplitz((c_cont + cat_s)[:M_TOP_DEEP])
    lam_s = np.linalg.eigvalsh(Ts[:M_CTRL, :M_CTRL])
    print("  CS census: %d/%d eigenvalues below -THR_NULL = -%g"
          % (int(np.sum(lam_s < -THR_NULL)), M_CTRL, THR_NULL))
    fire_s, det_s = yhp.control_yosida(Ts, bats, "scramble")
    med_c, cmax_c = control_corner_context(Ts, F)
    check("CS position-scramble control fires (positivity rule, "
          "deep comb, %d atoms)" % ka_deep, fire_s, det_s)
    print("    corner context (report only): control corner med "
          "increment %.1e vs real %.1e, max |E_Y| %.1e"
          % (med_c, med_real, cmax_c))

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
    lam_e = np.linalg.eigvalsh(TE[:M_CTRL, :M_CTRL])
    print("  CE census: %d/%d eigenvalues below -THR_NULL = -%g"
          % (int(np.sum(lam_e < -THR_NULL)), M_CTRL, THR_NULL))
    fire_e, det_e = yhp.control_yosida(TE, bats, "epstein")
    med_c, cmax_c = control_corner_context(TE, F)
    check("CE Epstein control (x^2+5y^2, %d negative atom sites) "
          "fires (positivity rule)"
          % int(np.sum(lamE[2:] < -1.0e-9)), fire_e, det_e)
    print("    corner context (report only): control corner med "
          "increment %.1e vs real %.1e, max |E_Y| %.1e"
          % (med_c, med_real, cmax_c))


# ------------------------------------------------ run
def run():
    print("=" * 78)
    print("QF OFFENSIVE strand 1, follow-up -- corner-native Gate 3' "
          "decider (v764 precondition)")
    print("=" * 78)

    hits = ast_firewall()
    check("G0.1 AST firewall", not hits, str(hits))
    bats, spec_sha = freeze_spec()
    check("G0.2 battery + ladder + cell set + eps set + bars + net "
          "rule + deep-comb spec + control rule SHA-256-frozen "
          "BEFORE any comb data is built here", True,
          "SHA256 %s..." % spec_sha[:16])
    check("G0.3 reach census: M_TOP_DEEP = %d <= floor(64 ln %d) = "
          "%d; sieve cover exp(X_top) + 2 = %d <= %d; runtime cap "
          "%.0f s" % (M_TOP_DEEP, ATOM_MAX_DEEP, M_CAP_DEEP,
                      int(math.exp(M_TOP_DEEP * D)) + 2,
                      ATOM_MAX_DEEP, RUNTIME_CAP),
          M_TOP_DEEP <= M_CAP_DEEP
          and int(math.exp(M_TOP_DEEP * D)) + 2 <= ATOM_MAX_DEEP)

    # ---- comb + towers strictly after the freeze
    u_deep, mu_deep = build_deep_comb()
    T_par = build_parent_tower()
    T, c_cont, alpha_deep, ka_deep = build_deep_tower(u_deep, mu_deep,
                                                      T_par)

    # ---- spectral ladder
    F, names = battery_matrix(bats)
    cells, labels = corner_cells(names)
    spec = spectral_pass(T, F)
    print("  PD margins (eps = 0, measured, never gated): lambda_min "
          "= %.3e (M %d) -> %.3e (M %d) -> %.3e (M %d)"
          % (spec[0]["lam"][0], FULL_LAD[0],
             spec[I972]["lam"][0], 972, spec[-1]["lam"][0],
             M_TOP_DEEP))
    gmin, gmax = np.inf, -np.inf
    for idx in (FULL_LAD.index(M_CTRL), len(FULL_LAD) - 1):
        lam = spec[idx]["lam"]
        for e in EPS_GATED:
            g = lam / (lam + e)
            gmin = min(gmin, float(np.min(g)))
            gmax = max(gmax, float(np.max(g)))
    check("G1.6 real-data operator sandwich at M = %d and %d: Yosida "
          "eigenvalues in [%.1e, 1 - %.1e] at every gated eps (bars "
          "-%.0e / 1+%.0e)" % (M_CTRL, M_TOP_DEEP, gmin, 1.0 - gmax,
                               SANDWICH_TOL, SANDWICH_TOL),
          gmin >= -SANDWICH_TOL and gmax <= 1.0 + SANDWICH_TOL)

    # ---- dense-solve Ward on the corner
    iw = FULL_LAD.index(M_WARD)
    Fp = np.zeros((M_WARD, F.shape[1]))
    Fp[:NPAD] = F
    GF = np.linalg.solve(T[:M_WARD, :M_WARD]
                         + EPS_WARD * np.eye(M_WARD), Fp)
    EYd = Fp.T @ (Fp - EPS_WARD * GF)
    EYd = 0.5 * (EYd + EYd.T)
    wdev = float(np.max(np.abs(EYd - corner_of(spec[iw], EPS_WARD))))
    check("G2.1 spectral-vs-dense-solve Ward on E_Y (M = %d, eps = "
          "%g) <= %.0e" % (M_WARD, EPS_WARD, WARD_SPEC),
          wdev <= WARD_SPEC, "max abs %.1e" % wdev)

    # ---- corner gates (needs EY for anchors too)
    counts, EY, scales, aud = corner_gate_block(spec, cells, labels)

    # ---- parent-audit anchor reproduction
    qmat = np.stack([qf_of(b) for b in spec])
    q824 = qmat[I824]
    q_ext = qmat[I824:I972 + 1]
    med_mid = np.median(q_ext[MID5], axis=0)
    med_last = np.median(q_ext[LAST5], axis=0)
    drift = np.abs(med_last - med_mid) \
        / np.maximum(np.maximum(med_last, med_mid), QF_FLOOR)
    nn888 = spec[FULL_LAD.index(888)]["nn"]
    dev_q = abs(float(np.max(q824)) - PARENT_QF_MAX)
    dev_d = abs(float(np.max(drift)) - PARENT_DRIFT_WORST)
    dev_h = abs(aud["env_head"] - ENV_HEAD_REF)
    dev_t = abs(aud["env_tail"] - ENV_TAIL_REF)
    check("G1.5 parent-audit anchor reproduction: max q_f(824) = "
          "%.4f (dev %.1e <= %.0e), worst 824..972 drift = %.4f "
          "(dev %.1e), nn(888) = %d (frozen %d), corner envelope "
          "eps=1e-3 head/tail med5 = %.4e / %.4e (dev %.1e <= %.0e "
          "/ %.1e <= %.0e)"
          % (float(np.max(q824)), dev_q, REPRO_TOL,
             float(np.max(drift)), dev_d, nn888, PARENT_NN_888,
             aud["env_head"], aud["env_tail"], dev_h, ENV_HEAD_TOL,
             dev_t, ENV_TAIL_TOL),
          dev_q <= REPRO_TOL and dev_d <= REPRO_TOL
          and nn888 == PARENT_NN_888 and dev_h <= ENV_HEAD_TOL
          and dev_t <= ENV_TAIL_TOL)

    # ---- subsequence report
    d_q, d_c = subsequence_report(spec, EY, cells, qmat)

    # ---- boundedness / KILL audit
    smin, smax = min(scales.values()), max(scales.values())
    check("G1.7 boundedness/KILL audit: corner entries bounded by "
          "%.4f (sandwich, band 1+%.0e), increments >= %.1e, corner "
          "scales %.3f..%.3f in [%g, %g], q_f in [%.1e, %.4f] "
          "within [0, 1] -- bounded forms only, no 1/eps, no PD "
          "assumption, no target data, no q_f in any gate"
          % (aud["cmax"], BOUND_TOL, aud["inc_min"], smin, smax,
             SCALE_LO, SCALE_HI, float(np.min(qmat)),
             float(np.max(qmat))),
          aud["cmax"] <= 1.0 + BOUND_TOL and aud["inc_min"] >= 0.0
          and smin >= SCALE_LO and smax <= SCALE_HI
          and float(np.min(qmat)) >= -1.0e-12
          and float(np.max(qmat)) <= 1.0 + BOUND_TOL)

    # ---- controls
    run_controls(c_cont, alpha_deep, ka_deep, mu_deep, bats, F,
                 aud["med_real"])

    # ---- runtime guard
    dt = time.time() - T_START
    check("G0.4 runtime %.1f s <= predeclared cap %.0f s"
          % (dt, RUNTIME_CAP), dt <= RUNTIME_CAP)

    # ---- verdict (preregistered rules)
    guards_ok = all(ok for (n, ok) in CHECKS
                    if not n.startswith(("CS", "CE")))
    controls_ok = all(ok for (n, ok) in CHECKS
                      if n.startswith(("CS", "CE")))
    n1, n2, n3 = (counts[e] for e in EPS_GATED)
    if not (guards_ok and controls_ok):
        verdict = "GATE3PRIME-DEAD"
        reason = "invalid run: a guard failed or a control " \
                 "spuriously converged -- no measured statement " \
                 "about the corners follows"
    elif n1 == 56 and n2 == 56 and n3 >= N3_CONV:
        verdict = "GATE3PRIME-CONVERGES"
        reason = ""
    elif n1 >= N_PART and n2 >= N_PART and n3 >= N3_PART:
        verdict = "GATE3PRIME-PARTIAL"
        reason = ""
    else:
        verdict = "GATE3PRIME-DEAD"
        reason = "majority corner failures"

    n_chk = sum(1 for (_n, ok) in CHECKS if ok)
    n_cell = sum(1 for c in CELLS if c[2])
    print("\nVERDICT: %s%s" % (verdict,
                               (" (%s)" % reason) if reason else ""))
    print("CELLS %d/%d (eps 1e-1: %d/56, 1e-2: %d/56, 1e-3: %d/56), "
          "GUARDS+CONTROLS %d/%d, subsequence density corner %.3f "
          "vs q_f %.3f, runtime %.1f s"
          % (n_cell, len(CELLS), n1, n2, n3, n_chk, len(CHECKS),
             d_c, d_q, time.time() - T_START))
    if verdict == "GATE3PRIME-CONVERGES":
        print("CONSEQUENCE FOR v764 (stated plainly): the corner "
              "entries are entrywise Cauchy at the frozen "
              "oscillation-aware bars on every gated eps -- Gate 3' "
              "is decided POSITIVELY in the weakened, contract-"
              "native form (QF-GAUGE upstream).  What remains for "
              "v764: assemble the a-priori bound from v760 (anti-"
              "alias exactness) + v761 (atom-pole Abel control) "
              "with this corner-Cauchy statement into the promoted "
              "Gate 3' module; the q_f Cauchy demand is dropped "
              "(bounded gauge, reported).  NOT claimed: eps -> 0 "
              "closure, X -> infinity, RH.")
    elif verdict == "GATE3PRIME-PARTIAL":
        print("CONSEQUENCE FOR v764 (stated plainly): the corner "
              "Cauchy statement holds on the named majority and "
              "FAILS on the named minority cells above -- the v764 "
              "precondition is met only in the reduced form; every "
              "failing (entry, eps) cell is listed and must be "
              "carried as an open named block.  NOT claimed: eps -> "
              "0 closure, X -> infinity, RH.")
    else:
        print("CONSEQUENCE (stated plainly): %s -- the corner "
              "increments do not fall at the frozen bars: the gauge "
              "reading of q_f was a false hope at this depth and "
              "the wall returns at the corner level (or the run is "
              "invalid as stated).  NO RH claim." % (reason or
                                                     "DEAD"))
    return 0 if (guards_ok and controls_ok) else 1


if __name__ == "__main__":
    sys.exit(run())
