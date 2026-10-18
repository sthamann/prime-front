#!/usr/bin/env python3
"""QF-OFFENSIVE strand 3, module 3 follow-up -- the deep-comb
edge-separation decider: does the 7/8 slow-band edge SEPARATE again
at greater depth (so that d = 7 owns a uniformly separated band on a
frozen tail of the new range AND passes the parent Cauchy bars -- the
fixed-d Feshbach limit exists after all), or does the edge KEEP
MOVING (new modes descending at a measurable cadence -- fixed-d is
closed on every reachable surface and the cell-cocycle formulation is
mandatory)?  qf_edge_separation_probe.

Exploration only (tfpt-experiment firewall): NOT wired into
run_all.py, no ledger row, no paper edit, no website edit, NO RH
CLAIM, and this probe writes no files.  It never reads a zero
ordinate and never evaluates the target before every source object is
built and SHA-256 frozen.  Band, transport, effective block and
census are built exclusively from the source window operator -- never
from target data.

INPUT STATE (frozen findings, none re-adjudicated here):
  *  qf_feshbach_effective_probe -- FESHBACH-PARTIAL on the 1e8 comb
     (X <= 18.375): the reduction is well-defined for d = 6 and ONLY
     d = 6 (GAP+HERG+REC), but CAUCHY-6 fails on the slope clause
     (b2 = +0.006 < 0.02) exactly where the 7th mode brushes the
     band; d = 7 passes CAUCHY strongly (med5 0.207, b2 = +0.502/X)
     but loses separation exactly at the top rung (gap 7/8 = 0.0613
     at M = 1176 < bar 0.10, lam8 descending); d = 8 has an internal
     8/9 crossing at M = 976 (transport angle 87.2 deg).  Its named
     next surface is exactly this probe: a deeper comb to see whether
     the 7/8 edge separates again (letting d = 7 pass both), vs a
     depth-dependent band dimension d(X) (the cocycle module).
  *  qf_drainage_probe -- QF-SETTLES-POSITIVE 14/14 on the 1e8 comb:
     settled per-function band weights (R2 family 0.225..0.358, R1
     family 0.008..0.079); 7th-mode threshold entry at M = 992,
     count 8 from M ~ 1108; 6/7 gap bottoms at 0.1008 (M ~ 1096..
     1100) then recovers to 0.1397 at 1176; single deep mode
     persists; lambda_min(1176) = 3.882e-6.
  *  Mode-entry record so far (X = M/64): 6th at M = 888
     (X = 13.875), 7th at M = 992 (X = 15.5), 8th at M ~ 1108
     (X ~ 17.3125) -- inter-entry gaps DX ~ 1.625, ~1.8125.  If this
     cadence is REGULAR, a new mode reaches every fixed band edge at
     bounded intervals and no fixed d separates permanently.

COMPUTE-BUDGET BENCHMARK (declared; run BEFORE this spec was frozen;
timing/memory only -- no spectra, no battery pairing, no gap or
census value was consulted): deployed sieve at 1e8 = 1.2 s / peak RSS
0.99 GB (reproduces the drainage declaration); 4e8 = 4.9 s / 4.5 GB;
1e9 = 12.3 s / 13.5 GB on a 512-GB machine; tent assembly rate
8.0e5 atoms/s -> ~62 s for the ~4.94e7 atoms in reach of X = 20.6875;
dense eigh at M ~ 1324 well under 0.5 s.  On this budget the deeper
cap is frozen at ATOM_MAX_XD = 1,000,000,000 (1e9) -- one cap, chosen
before the first run, never adjusted after.  M_CAP_XD =
floor(64 ln 1e9) = 1326; M_TOP_XD = 1324 (X = 20.6875; step-4 aligned
with the parent top: 1324 = 1176 + 37 x 4; sieve cover exp(20.6875)
+ 2 = 964,900,015 <= 1e9).  No rung thinning needed at this budget:
the full step-4 ladder 888..1324 (110 rungs) is kept.

FROZEN CONSTRUCTION (reused machinery verbatim, none invented):
  deep comb = deployed von Mangoldt generator (core.
      von_mangoldt_table) at cap ATOM_MAX_XD = 1e9; tower = continuum
      lags + atom tents on the dyadic grid D = 1/64
      (simpler_schur_recursion machinery verbatim).
  full ladder FLAD = 888..1324 step 4 (110 rungs, 109 increments;
      the leading 73 rungs 888..1176 are the Feshbach probe's GLAD,
      reused for exact continuity); census ladder CENS = [884] +
      FLAD (884 carries the entry-rung reproduction Ward);
      extension XLAD = 1180..1324 step 4 (37 rungs, X = 18.4375..
      20.6875); frozen tail block TAIL = last ceil(37/4) = 10
      extension rungs = 1288..1324 (X = 20.125..20.6875).
  band rule (parent rule verbatim): d LOWEST eigenmodes, always;
      threshold census #{lam <= THR_NULL = 1e-4} and deep census
      #{lam <= THR_DEEP = 1e-5} reported on every rung; q_f band
      weight uses the 6 LOWEST modes (drainage object, verbatim).
  d = 7 transported effective block (Feshbach machinery verbatim):
      sign-fixed 7 lowest eigenvectors, overlap S_k = V_{k+1}^T
      pad(V_k), polar factor of the SVD (floor sigma_min >= 1e-8
      else transport undefined = kill), chained R; F~_k(z) = R_k^T
      [Lambda_7(X_k) - z - C_7(z)] R_k with the MEASURED Schur
      correction C_7(z) = E_c^T diag(1/(lam_c - z)) E_c (machine
      scale, P A Q = 0 -- coupling Ward, never assumed); reference
      cell Z_REF = -1e-2 (the parent z-shift identity binds all
      other z cells to it -- redundant cells not re-evaluated);
      Herglotz certificates at ZC = (i h, -1e-3 + i h), h = 1e-2,
      on every FLAD rung (exact structural identity, checked as a
      guard-level Ward, not sold as evidence).
EDGE GATES (all frozen BEFORE the first run):
  EDGE-A  7/8 TAIL SEPARATION: rel gap g78 = (lam8 - lam7)/lam8 >=
      GAP_BAR = 0.10 on EVERY rung of the frozen TAIL block
      (recover above the bar and STAY there); the full g78 profile
      on FLAD, the first recovery rung on the extension, and the
      extension second-half linear trend are reported either way.
  EDGE-B  CAUCHY-7 DEEP (parent bars verbatim): increments delta_k
      = max-entry |F~_{k+1}(Z_REF) - F~_k(Z_REF)| over the 109
      FLAD increments; med5(LAST5)/med5(FIRST5) <= C_MED = 0.5 AND
      second-half falling rate b2 >= C_SLOPE = 0.02 per X unit
      (hbp.fit_rate verbatim); blocks FIRST5 = increments 1..5,
      LAST5 = 105..109, second half = 55..109.
  EDGE-C  MODE-DESCENT CADENCE (fit-free, reported AND gated as the
      keeps-moving clause): entry rung of mode n = first CENS rung
      with threshold count >= n; inter-entry gaps DX_n in X; frozen
      regularity statistic rel spread (max DX - min DX)/max DX <=
      CAD_BAR = 0.25 over all measured consecutive gaps; the
      keeps-moving clause KM2 FIRES iff a NEW entry (count >= 9)
      occurs on the extension AND the cadence is regular.  No fit
      enters any gate; the predicted next-entry depth X_last +
      mean(DX) is REPORTED only.
  Also reported, never gated: gap 6/7 and 8/9 profiles on the
      extension (does the d = 6 grazing resolve? where does the 9th
      mode press?); settled q_f levels med5 over the new TOP5 =
      1308..1324 vs the drainage TOP5 = 1160..1176 (drainage
      confirmation for free); PD margins.
GUARDS (must pass or the run is invalid):
  G0.1 AST firewall (banned: zetazero/nzeros/isprime/primerange/
       nextprime/prevprime/primepi/sympy); G0.2 SHA-256 freeze of
       battery bytes + cap + ladders + blocks + every bar + anchors
       BEFORE any comb data is built here; G0.3 reach census +
       runtime cap 1800 s predeclared;
  G1.1 deep-table overlap: extended von Mangoldt table == deployed
       core table on [0, 400000] EXACTLY; G1.2 extended Chebyshev
       envelope kappa <= KAPPA_REF + 1e-6 over [100, 1e9];
  G1.3 parent tower comb consistency (rel dev <= 1e-12); G1.4
       prefix Ward: deep tower leading 824 x 824 block == parent
       tower (<= 1e-12);
  G1.5 Feshbach/drainage anchor reproduction: (a) 6/7 gap(1096) =
       0.1008, 6/7 gap(1176) = 0.1397, 7/8 gap(1176) = 0.0613, all
       +- 2e-4 (4 digits); thr count(1176) = 8, deep count(1176) =
       1, lambda_min(1176) = 3.882e-6 +- 2e-8; (b) entry-rung
       reproduction: count 5 at M = 884, 6 at M = 888, 7th entry
       exactly at M = 992; (c) drainage settled levels: med5 over
       1160..1176 of the band-6 weight reproduces the nine frozen
       drainage values (0.3583/0.3370/0.3127/0.2590/0.2249/0.0793/
       0.0741/0.0741/0.0082) +- 2e-3;
  G1.6 measured PD: lambda_min > -1e-9 on every rung (measured
       output; NO gate uses a PD margin or 1/eps); G1.7 coupling
       Ward max |E| <= 1e-8 (P A Q = 0 measured); G1.8 transport
       orthogonality Ward <= 1e-10; K4 sigma_min >= 1e-8; HERG-7
       Ward: max eig Im F~ <= 1e-10 AND min eig Im F~^{-1} >=
       -1e-10 at both ZC points on every FLAD rung; G1.9
       boundedness: every band q_f in [-1e-12, 1 + 1e-9], every
       overlap singular value <= 1 + 1e-12, every |F~| entry <=
       lam_max(band) + |z|_max + 1e-9.
CONTROLS (mandatory, must fire; fire rule = qf_spectral_bundle_probe.
  control_bundle VERBATIM, imported read-only): CS position scramble
  (positions uniform in (0.5, 2 alpha_xd), masses kept, seed 7, on
  the 1e9 comb, rungs 496..512 step 4) and CE Epstein x^2 + 5y^2
  (epstein_firewall_probe read-only, cap M = 640, rungs 624..640
  step 4).  FIRE = rank instability OR gap collapse OR angle
  saturation.  A control whose bundle construction stays intact has
  spuriously converged: the run is INVALID.
VERDICT ENUM (frozen; decision order as listed):
  0. any guard fails or a control spuriously converges -> the run is
     INVALID: printed as EDGE-UNDECIDED (invalid run), exit 1, no
     edge statement follows.
  1. EDGE-SEPARATES-D7 = EDGE-A passes AND EDGE-B passes: the 7/8
     edge separates again at depth and the transported d = 7 block
     is Cauchy at the parent bars -- the fixed-d Feshbach limit
     exists after all; the boundary-triple module reopens with
     d = 7.
  2. EDGE-KEEPS-MOVING = (EDGE-A fails) OR (KM2 fires: a new mode
     entry on the extension at regular cadence): the band edge is
     chased by descending modes at the measured cadence -- fixed-d
     is closed on every reachable surface and the cell-cocycle
     formulation is the remaining path; the cadence (mean DX, rel
     spread) is stated as the new named structural constant.
  3. otherwise EDGE-UNDECIDED: the bars are not reached either way
     (e.g. tail separates but the Cauchy tail is too short, and no
     new entry adjudicates the cadence); the deciding depth is
     stated honestly.
STOP-LIST (binding, inherited): no target decomposition / Cholesky /
zeros anywhere; no bare A^{-1} (resolvents only at the frozen z with
|z| >= 1e-3 or Im z = h); no PD-margin or 1/eps in any gate; no fits
inside gates beyond the declared bounded-statistic slope (b2, parent
CAUCHY clause verbatim; the cadence gate is fit-free); no Riemann
zeros; NO RH claim.  This probe writes no files.  Runtime cap 1800 s
predeclared.

RESULTS (2026-08-05, first and only preregistered run, 160.3 s;
GATES: EDGE-A FAIL, EDGE-B PASS, KM2 quiet; GUARDS+CONTROLS 20/20;
verdict EDGE-KEEPS-MOVING, carried by the EDGE-A failure alone):
  *  THE 7/8 EDGE DOES NOT SEPARATE -- IT CLOSES INTO A NEAR-
     CROSSING.  On the extension the 7/8 gap NEVER reaches the bar
     again (extension max 0.0568, right after the parent top): from
     0.0613 at M = 1176 it falls through 0.0209 (M = 1208) to
     0.0039 at M = 1240 (printed profile; an avoided crossing --
     lam8 descends THROUGH the 7-band edge), relaxes to ~0.011,
     and decays again to 0.0074 at the top rung 1324.  At the top
     the pair is nearly degenerate: lam7 = 7.9351e-5, lam8 =
     7.9946e-5 (and lam9 = 9.1935e-5 -- modes 7/8/9 now form a
     CLUSTER below thr 1e-4).  The transport sees the crossing:
     min sigma_min = 0.0271 (max angle 88.45 deg, still above the
     1e-8 kill floor -- the same violent band rotation the parent
     measured for d = 8 at M = 976, now one level down).  EDGE-A
     min tail gap 0.0074 < 0.10: FAIL, unambiguous.
  *  EDGE-B PASSES CLEANLY EVEN THROUGH THE CROSSING: the
     transported 7x7 block stays Cauchy on all 109 increments --
     2.72e-6 -> 3.94e-7, med5 last/first = 0.181 <= 0.5, b2 =
     +0.061/X >= 0.02 (parent 1e8 numbers were 0.207 / +0.502).
     The moving-edge picture is now measured at two consecutive
     levels: every d gets a CONVERGENT transported block and then
     loses its edge to the next descending mode.  Convergence was
     never the problem; band ownership is.
  *  MODE-DESCENT CADENCE (the fit-free record): entries at
     M = 888 / 992 / 1108 / 1276 (X = 13.8750 / 15.5000 / 17.3125
     / 19.9375) -- the 9th mode enters INSIDE the extension.
     Inter-entry gaps DX = 1.6250 / 1.8125 / 2.6250, mean 2.0208,
     rel spread 0.381 > CAD_BAR 0.25: the frozen KM2 clause does
     NOT fire -- the cadence is real but NOT regular at the frozen
     bar; the spacing WIDENS with depth (third gap 1.6x the
     first).  That widening is the honest surprise of this run and
     the number the cocycle module must carry.  Predicted next
     entry at the measured mean cadence (REPORTED only): X ~ 21.96
     (M ~ 1405, ATOM_MAX ~ 3.4e9).  Deep count (lam <= 1e-5)
     stays exactly 1 on all 111 census rungs.
  *  THE d = 6 GRAZING RESOLVES (reported): the 6/7 gap recovers
     from the parent's 0.1008 bottom to 0.4333 at the top rung
     (extension min 0.1444 at M = 1180) -- at X = 20.6875 the
     separated object is the 6-band again, sitting under a 7/8/9
     cluster.  gap 8/9 extension min 0.1304 (at the top, falling).
     Together with EDGE-A this is the moving-edge picture in full:
     the band boundary d(X) is 6 -> 7 -> 8 -> 9 by threshold count
     but the SEPARATED dimension oscillates (6 separated here,
     7/8/9 clustered) -- no fixed d owns the tail.
  *  q_f DRAINAGE CONFIRMATION FOR FREE: the settled levels hold
     to 0.87..1.09x over 2.3 more X units -- med5(1308..1324) vs
     med5(1160..1176): R2 family 0.3245/0.2948/0.2809/0.2247/
     0.2015 vs 0.3583/0.3370/0.3127/0.2590/0.2249; R1 family
     0.0735/0.0761/0.0599/0.0089.  Typed honestly: extension fall
     rates b = +0.050..+0.083/X sit slightly ABOVE the drainage
     plateau bar 0.05 (reported here, never gated) -- a mild
     renewed decline worth one line in any future drainage rerun,
     far from the Z-type collapse (levels >= 0.0089).  PD margins
     (measured, never gated): lambda_min 3.882e-6 (1176) ->
     2.455e-6 (1324).
  *  CONTROLS both fire (rank + gap clauses): CS scramble (1e9
     comb, 49,154,321 atoms) threshold counts 242..253 vs 6,
     253/512 negative, min rel gap 0.0006; CE Epstein counts
     251..263 vs 6, min rel gap 0.0650.  GUARDS 20/20: deep-table
     overlap exact (dev 0.0), kappa = 0.038821 unchanged on
     [100, 1e9], prefix Ward 2.0e-14, ALL anchors reproduced --
     gaps 0.1008/0.1397/0.0613 to 4 digits, lambda_min(1176) dev
     5e-10, entry rungs 884:5 / 888:6 / 992:7th exact, all nine
     drainage levels dev <= 4.9e-5; coupling Ward 4.1e-15,
     transport orthogonality 9.6e-14, HERG-7 Ward exact (-1.000e-2
     / +98.57), boundedness clean; runtime 160.3 s <= 1800 s.
  *  CONSEQUENCE FOR THE OFFENSIVE (stated plainly): FIXED-d IS
     CLOSED on every reachable surface -- not by non-convergence
     (CAUCHY-7 passes at 1e8 and again at 1e9, straight through an
     avoided crossing) but by band ownership: d = 7 never regains
     a separated edge (tail gap 0.0074 vs bar 0.10) because lam8
     crosses INTO the 7-band on the extension, exactly as lam7 had
     grazed the 6-band one window earlier.  The boundary-triple
     module does NOT reopen with d = 7.  The CELL-COCYCLE
     formulation -- depth-dependent band dimension d(X) with
     transition maps at the mode-entry rungs -- is the only
     remaining path of the diagonal route; its cell boundaries are
     the measured entry rungs 888 / 992 / 1108 / 1276, its
     per-cell blocks are convergent objects (EDGE-B), and its
     structural constant is the measured, WIDENING entry cadence
     DX = 1.625 / 1.8125 / 2.625 (mean 2.02, spread 0.381 -- NOT
     regular at the frozen 0.25 bar; whether DX grows like a
     deterministic law is a question for that module, stated not
     fitted).  Additional cocycle input from this run: the
     separated dimension at the top is 6 again under a 7/8/9
     cluster -- cells may carry CLUSTERS, not single modes.  NOT
     claimed: any statement beyond X = 20.6875, eps-uniformity,
     RH.

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/qf_edge_separation_probe.py
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
ATOM_MAX_XD = 1000000000             # deeper comb cap (frozen, 1e9)
M_CAP_XD = int(math.floor(math.log(ATOM_MAX_XD) / D))       # 1326
M_TOP_XD = 1324                      # deepest rung (X = 20.6875)
M_TOP_PAR = 824                      # first-parent cap (prefix Ward)
M_TOP_FES = 1176                     # Feshbach-probe top (anchors)

FLAD = list(range(888, 1325, 4))     # 110 rungs, X = 13.875..20.6875
CENS = [884] + FLAD                  # census ladder (entry Ward)
XLAD = list(range(1180, 1325, 4))    # 37 extension rungs
N_TAIL = int(math.ceil(len(XLAD) / 4.0))          # 10 tail rungs
TAIL = XLAD[-N_TAIL:]                # 1288..1324, X = 20.125..20.6875
TOP5_NEW = list(range(1308, 1325, 4))
TOP5_DRAIN = list(range(1160, 1177, 4))

K_QF = 6                             # q_f band rank (drainage rule)
D_EDGE = 7                           # the adjudicated band dimension
D_STORE = 9                          # stored eigenmodes (gaps to 8/9)
THR_NULL = 1.0e-4                    # threshold census (entry rule)
THR_DEEP = 1.0e-5                    # deep census (reported)
NPAD = 128                           # max battery support in cells
R_BAT = (1.0, 2.0)                   # frozen module-1 local battery
N_MED = 5                            # median block size

Z_REF = -1.0e-2                      # frozen Cauchy reference cell
H_IM = 1.0e-2                        # Herglotz imaginary offset
ZC = (complex(0.0, H_IM), complex(-1.0e-3, H_IM))

GAP_BAR = 0.10                       # EDGE-A tail separation bar
C_MED = 0.50                         # EDGE-B med5 ratio bar
C_SLOPE = 0.02                       # EDGE-B second-half rate bar
INC_FIRST5 = slice(0, 5)             # increment blocks (109 pairs)
INC_LAST5 = slice(104, 109)
INC_HALF2 = slice(54, 109)
CAD_BAR = 0.25                       # EDGE-C rel spread regularity

SVD_FLOOR = 1.0e-8                   # K4 polar/90-degree floor
COUP_WARD = 1.0e-8                   # G1.7 coupling |E| Ward
WARD_ORTH = 1.0e-10                  # G1.8 R orthogonality
HERG_FLOOR = 1.0e-10                 # HERG-7 Ward floor
PD_TOL = 1.0e-9                      # G1.6 measured-PD slack
BOUND_TOL = 1.0e-9                   # G1.9 boundedness slack
QF_FLOOR = 1.0e-12                   # denominator floor
COMB_DEV_BAR = 1.0e-12               # G1.3 sieve == deployed masses
PREFIX_WARD = 1.0e-12                # G1.4 prefix max abs dev
RUNTIME_CAP = 1800.0                 # seconds, predeclared

REPRO_G67_1096 = 0.1008              # Feshbach frozen 6/7 gap (1096)
REPRO_G67_1176 = 0.1397              # Feshbach frozen 6/7 gap (1176)
REPRO_G78_1176 = 0.0613              # Feshbach frozen 7/8 gap (1176)
REPRO_TOLG = 2.0e-4                  # anchor gaps to 4 digits
REPRO_NN1176 = 8                     # frozen thr count (1176)
REPRO_LMIN1176 = 3.882e-6            # frozen lambda_min (1176)
REPRO_LTOL = 2.0e-8
ENTRY7_RUNG = 992                    # frozen 7th-mode entry rung
DRAIN_LEVELS = {                     # drainage med5(TOP5) frozen
    "R2:box[0,R]": 0.3583, "R2:box[R/2,R]": 0.3370,
    "R2:hat(R/2,R/2)": 0.3127, "R2:hat(3R/4,R/4)": 0.2590,
    "R2:box[R/4,3R/4]": 0.2249, "R1:box[R/2,R]": 0.0793,
    "R1:box[0,R]": 0.0741, "R2:box[0,R/2]": 0.0741,
    "R1:hat(R/4,R/4)": 0.0082}
REPRO_QTOL = 2.0e-3

EP_NCAP = 34000                      # Epstein Lambda_E table reach
EP_MMAX = 640                        # Epstein control tower cap
SEED = 7

BANNED = ("zetazero", "nzeros", "isprime", "primerange", "nextprime",
          "prevprime", "primepi", "sympy")

CHECKS = []       # guards + controls: all must pass, else invalid run
GATES = []        # edge gates: feed the verdict only


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
    """Battery bytes + cap + ladders + blocks + bars + anchors,
    SHA-256 frozen BEFORE any comb data is built in this probe."""
    bats = {}
    hsh = hashlib.sha256()
    hsh.update(("qf-edge-separation spec: 4 boxes + 3 hats per R, "
                "l2-norm, D=%.10f, R=%s; deeper comb = deployed "
                "von_mangoldt_table sieve at cap %d (benchmarked "
                "12.3 s / 13.5 GB before freeze), M_CAP=%d, M_TOP=%d"
                "; FLAD=%s; CENS=[884]+FLAD; XLAD=%s; TAIL=%s; "
                "TOP5_NEW=%s TOP5_DRAIN=%s; band rule = d lowest "
                "always, qf rank %d, d_edge = %d, thr=%g deep=%g; "
                "z: zref=%g h=%g zc=%s; EDGE-A: g78 >= %g on every "
                "TAIL rung; EDGE-B: med5 last/first <= %g AND b2 >= "
                "%g, blocks [0:5][104:109][54:109] Nmed=%d; EDGE-C: "
                "entry rung = first CENS rung with count >= n, rel "
                "spread (max-min)/max of DX <= %g = regular, KM2 = "
                "new entry (>= 9) on extension AND regular; kills: "
                "svd>=%g coup<=%g; wards: orth<=%g herg<=%g "
                "pd>=-%g bound<=%g; anchors: g67(1096)=%g "
                "g67(1176)=%g g78(1176)=%g tolg=%g nn1176=%d "
                "deep1176=1 lmin1176=%g toll=%g entry7=%d "
                "entry884=5 entry888=6; drain levels %s tol=%g; "
                "guards: comb<=%g prefix<=%g runtime<=%g; controls "
                "verbatim qsb.control_bundle, lads=%s/%s epcap=%d "
                "epM=%d seed=%d; verdict order: invalid -> "
                "SEPARATES-D7 (A and B) -> KEEPS-MOVING (not A or "
                "KM2) -> UNDECIDED"
                % (D, R_BAT, ATOM_MAX_XD, M_CAP_XD, M_TOP_XD, FLAD,
                   XLAD, TAIL, TOP5_NEW, TOP5_DRAIN, K_QF, D_EDGE,
                   THR_NULL, THR_DEEP, Z_REF, H_IM, ZC, GAP_BAR,
                   C_MED, C_SLOPE, N_MED, CAD_BAR, SVD_FLOOR,
                   COUP_WARD, WARD_ORTH, HERG_FLOOR, PD_TOL,
                   BOUND_TOL, REPRO_G67_1096, REPRO_G67_1176,
                   REPRO_G78_1176, REPRO_TOLG, REPRO_NN1176,
                   REPRO_LMIN1176, REPRO_LTOL, ENTRY7_RUNG,
                   sorted(DRAIN_LEVELS.items()), REPRO_QTOL,
                   COMB_DEV_BAR, PREFIX_WARD, RUNTIME_CAP,
                   qsb.CTRL_LAD_S, qsb.CTRL_LAD_E, EP_NCAP, EP_MMAX,
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
    lam_deep = core.von_mangoldt_table(ATOM_MAX_XD)
    dev = float(np.max(np.abs(lam_deep[:core.ATOM_MAX + 1]
                              - core.LAM_TAB)))
    check("G1.1 deep-table overlap: 1e9 von Mangoldt table == "
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
          "%.0e = %.6f" % (kappa, core.KAPPA_X0, ATOM_MAX_XD,
                           core.TOL_KAPPA,
                           core.KAPPA_REF + core.TOL_KAPPA),
          kappa <= core.KAPPA_REF + core.TOL_KAPPA)
    return u_deep, mu_deep


def build_deep_tower(u_deep, mu_deep, T_par):
    alpha = 0.5 * M_TOP_XD * D
    ka = int(np.searchsorted(u_deep, 2.0 * alpha + 1.0e-14,
                             side="right"))
    c_cont = srp.continuum_lags(M_TOP_XD)
    c_at, _dd = core.atom_lags_at(alpha, M_TOP_XD, u_deep[:ka],
                                  mu_deep[:ka])
    T = sla.toeplitz((c_cont + c_at)[:M_TOP_XD])
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
    """Per rung: full spectrum, sign-fixed 9-mode head basis,
    coupling rows E = V^T A V9 (commutation Ward rows), census."""
    out = {}
    for M in sizes:
        A = T[:M, :M]
        lam, V = np.linalg.eigh(A)
        V9 = qsb.sign_fix(V[:, :D_STORE])
        out[M] = dict(M=M, lam=lam, V9=V9, E=V.T @ (A @ V9),
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


def rel_gap(blk, d):
    """(lam_{d+1} - lam_d)/lam_{d+1}, 1-based (parent formula)."""
    return float((blk["lam"][d] - blk["lam"][d - 1]) / blk["lam"][d])


# ------------------------------------------------ anchors (G1.5)
def anchor_guards(spec):
    g67a = rel_gap(spec[1096], 6)
    g67b = rel_gap(spec[M_TOP_FES], 6)
    g78b = rel_gap(spec[M_TOP_FES], 7)
    check("G1.5a Feshbach anchor reproduction: 6/7 gap(1096) = "
          "%.4f vs frozen %.4f, 6/7 gap(1176) = %.4f vs frozen "
          "%.4f, 7/8 gap(1176) = %.4f vs frozen %.4f (all dev <= "
          "%.0e); thr count(1176) = %d (== %d), deep count = %d "
          "(== 1); lambda_min(1176) = %.4e vs frozen %.4e (tol "
          "%.0e)"
          % (g67a, REPRO_G67_1096, g67b, REPRO_G67_1176, g78b,
             REPRO_G78_1176, REPRO_TOLG, spec[M_TOP_FES]["nn"],
             REPRO_NN1176, spec[M_TOP_FES]["nn_deep"],
             spec[M_TOP_FES]["lam"][0], REPRO_LMIN1176, REPRO_LTOL),
          abs(g67a - REPRO_G67_1096) <= REPRO_TOLG
          and abs(g67b - REPRO_G67_1176) <= REPRO_TOLG
          and abs(g78b - REPRO_G78_1176) <= REPRO_TOLG
          and spec[M_TOP_FES]["nn"] == REPRO_NN1176
          and spec[M_TOP_FES]["nn_deep"] == 1
          and abs(spec[M_TOP_FES]["lam"][0] - REPRO_LMIN1176)
          <= REPRO_LTOL)
    entry7 = min((M for M in FLAD if spec[M]["nn"] >= 7),
                 default=-1)
    check("G1.5b entry-rung reproduction: count %d at M = 884, %d "
          "at M = 888 (6th entry frozen), 7th entry at M = %d "
          "(frozen %d)" % (spec[884]["nn"], spec[888]["nn"], entry7,
                           ENTRY7_RUNG),
          spec[884]["nn"] == 5 and spec[888]["nn"] == 6
          and entry7 == ENTRY7_RUNG)


# ------------------------------------------------ EDGE-A + reports
def edge_gap_analysis(spec):
    print("\n-- EDGE-A: the 7/8 edge on the extension (bar %g; "
          "frozen tail block M = %d..%d)" % (GAP_BAR, TAIL[0],
                                             TAIL[-1]))
    g78 = {M: rel_gap(spec[M], 7) for M in FLAD}
    print("  gap 7/8 profile on FLAD (every 8th rung): %s"
          % "  ".join("M=%d:%.4f" % (M, g78[M]) for M in FLAD[::8]))
    print("  gap 7/8 on the tail block: %s"
          % "  ".join("M=%d:%.4f" % (M, g78[M]) for M in TAIL))
    rec = [M for M in XLAD if g78[M] >= GAP_BAR]
    if rec:
        stays = all(g78[M] >= GAP_BAR for M in XLAD
                    if M >= rec[0])
        print("  first recovery rung on the extension: M = %d "
              "(g78 = %.4f); stays above bar from there to top: %s"
              % (rec[0], g78[rec[0]], stays))
    else:
        print("  no extension rung reaches the bar (max %.4f)"
              % max(g78[M] for M in XLAD))
    xs_x = np.array([M * D for M in XLAD])
    gx = np.array([g78[M] for M in XLAD])
    n2 = len(XLAD) // 2
    print("  extension second-half linear trend: %+.4f/X "
          "(reported)" % lin_slope(xs_x[n2:], gx[n2:]))
    tail_min = min(g78[M] for M in TAIL)
    a_ok = gate("EDGE-A 7/8 TAIL SEPARATION: min rel gap on the "
                "frozen tail block = %.4f (top rung %.4f) >= %g"
                % (tail_min, g78[M_TOP_XD], GAP_BAR),
                tail_min >= GAP_BAR)

    # reported, never gated: 6/7 and 8/9 on the extension
    g67 = {M: rel_gap(spec[M], 6) for M in XLAD}
    g89 = {M: rel_gap(spec[M], 8) for M in XLAD}
    m67 = min(g67, key=g67.get)
    m89 = min(g89, key=g89.get)
    print("  gap 6/7 on the extension (reported): min %.4f at "
          "M = %d, top rung %.4f -- the d = 6 grazing %s"
          % (g67[m67], m67, g67[M_TOP_XD],
             "resolves" if min(g67.values()) >= GAP_BAR
             else "does NOT resolve"))
    print("  gap 8/9 on the extension (reported): min %.4f at "
          "M = %d, top rung %.4f" % (g89[m89], m89,
                                     g89[M_TOP_XD]))
    print("  lam7/8/9 at the top rung: %.4e / %.4e / %.4e"
          % (spec[M_TOP_XD]["lam"][6], spec[M_TOP_XD]["lam"][7],
             spec[M_TOP_XD]["lam"][8]))
    return a_ok


# ------------------------------------------------ EDGE-C cadence
def cadence(spec):
    print("\n-- EDGE-C: mode-descent cadence (fit-free; entry rung "
          "= first census rung with count >= n, thr %g)" % THR_NULL)
    nns = [spec[M]["nn"] for M in CENS]
    print("  threshold count profile along CENS (every 8th rung): "
          "%s" % "/".join("%d:%d" % (M, spec[M]["nn"])
                          for M in CENS[::8]))
    deeps = sorted(set(spec[M]["nn_deep"] for M in CENS))
    print("  deep count (lam <= %g) values seen: %s"
          % (THR_DEEP, deeps))
    entries = {}
    for M in CENS:
        for n in range(6, spec[M]["nn"] + 1):
            entries.setdefault(n, M)
    ns = sorted(n for n in entries if n >= 6)
    print("  mode-entry table:")
    for n in ns:
        print("    mode %2d: entry M = %d (X = %.4f)"
              % (n, entries[n], entries[n] * D))
    dxs = [(entries[b] - entries[a]) * D
           for a, b in zip(ns, ns[1:])]
    if dxs:
        spread = (max(dxs) - min(dxs)) / max(dxs)
        print("  inter-entry gaps DX = %s; mean %.4f; rel spread "
              "(max-min)/max = %.3f (regularity bar <= %g)"
              % ("/".join("%.4f" % v for v in dxs),
                 float(np.mean(dxs)), spread, CAD_BAR))
        print("  predicted next entry at the measured cadence "
              "(REPORTED only): X ~ %.2f (M ~ %d, ATOM_MAX ~ %.1e)"
              % (entries[ns[-1]] * D + float(np.mean(dxs)),
                 int((entries[ns[-1]] * D + float(np.mean(dxs)))
                     / D),
                 math.exp(entries[ns[-1]] * D + float(np.mean(dxs)))))
    else:
        spread = float("inf")
    new_entry = max(ns) >= 9 and entries[max(ns)] > M_TOP_FES
    regular = bool(dxs) and spread <= CAD_BAR
    km2 = gate("EDGE-C KM2 keeps-moving clause (fires = pass): new "
               "mode entry (count >= 9) on the extension = %s AND "
               "cadence regular (spread %.3f <= %g) = %s"
               % (new_entry, spread, CAD_BAR, regular),
               new_entry and regular)
    _ = nns
    return km2


# ------------------------------------------------ EDGE-B: d=7 Cauchy
def f_frame(blk, d, z):
    """Effective block in the rung band frame: Lambda_d - z - C_d(z)
    with the MEASURED Schur correction (machine scale, P A Q = 0)."""
    lam = blk["lam"]
    Ec = blk["E"][d:, :d]
    corr = Ec.T @ (Ec / (lam[d:, None] - z))
    return np.diag(lam[:d]) - z * np.eye(d) - corr


def feshbach_d7(spec):
    print("\n-- EDGE-B: transported d = %d effective block on the "
          "deep range (parent bars verbatim; Z_REF = %g)"
          % (D_EDGE, Z_REF))
    d = D_EDGE
    xs = np.array([M * D for M in FLAD])

    Rs, sig_min = [np.eye(d)], []
    ward_orth = 0.0
    sig_max = 0.0
    for Ma, Mb in zip(FLAD, FLAD[1:]):
        Va = spec[Ma]["V9"][:, :d]
        Vb = spec[Mb]["V9"][:, :d]
        S = Vb[:Ma, :].T @ Va
        U, s, Wt = np.linalg.svd(S)
        sig_min.append(float(s[-1]))
        sig_max = max(sig_max, float(s[0]))
        Rs.append(U @ Wt @ Rs[-1])
        ward_orth = max(ward_orth, float(np.max(np.abs(
            Rs[-1].T @ Rs[-1] - np.eye(d)))))
    check("K4 kill audit (d=%d): min sigma_min = %.6f >= %.0e "
          "(transport well-defined; max angle %.2f deg)"
          % (d, min(sig_min), SVD_FLOOR,
             math.degrees(math.acos(min(min(sig_min), 1.0)))),
          min(sig_min) >= SVD_FLOOR)
    check("G1.8 transport orthogonality Ward (d=%d): max "
          "||R^T R - I|| = %.1e <= %.0e" % (d, ward_orth,
                                            WARD_ORTH),
          ward_orth <= WARD_ORTH)
    coup = max(float(np.max(np.abs(spec[M]["E"][d:, :d])))
               for M in FLAD)
    check("G1.7 coupling/commutation Ward (d=%d): max |E| = %.1e "
          "<= %.0e on every FLAD rung (P A Q = 0 measured, not "
          "assumed)" % (d, coup, COUP_WARD), coup <= COUP_WARD)

    Ft = [Rs[i].T @ f_frame(spec[M], d, complex(Z_REF, 0.0)) @ Rs[i]
          for i, M in enumerate(FLAD)]
    dref = np.array([float(np.max(np.abs(Ft[i + 1] - Ft[i])))
                     for i in range(len(FLAD) - 1)])
    med_f = float(np.median(dref[INC_FIRST5]))
    med_l = float(np.median(dref[INC_LAST5]))
    ratio = med_l / max(med_f, QF_FLOOR)
    b2 = fall_rate(xs[1:][INC_HALF2], dref[INC_HALF2])
    print("  increment profile (first 3 / last 3): %s ... %s"
          % (", ".join("%.2e" % v for v in dref[:3]),
             ", ".join("%.2e" % v for v in dref[-3:])))
    b_ok = gate("EDGE-B CAUCHY-%d DEEP: med%d last/first = %.3f <= "
                "%g AND second-half falling rate b2 = %+.3f/X >= "
                "%g (%d increments, oscillation-aware, parent bars "
                "verbatim)" % (d, N_MED, ratio, C_MED, b2, C_SLOPE,
                               len(dref)),
                ratio <= C_MED and b2 >= C_SLOPE)

    # HERG-7 Ward (exact structural identity, guard level)
    herg_f, herg_m = -np.inf, np.inf
    for z in ZC:
        for i, M in enumerate(FLAD):
            Fz = Rs[i].T @ f_frame(spec[M], d, z) @ Rs[i]
            imF = (Fz - Fz.conj().T) / 2.0j
            herg_f = max(herg_f, float(np.max(
                np.linalg.eigvalsh(imF))))
            Minv = np.linalg.inv(Fz)
            imM = (Minv - Minv.conj().T) / 2.0j
            herg_m = min(herg_m, float(np.min(
                np.linalg.eigvalsh(imM))))
    check("HERG-%d Ward (every FLAD rung, both complex z): max eig "
          "Im F~ = %+.3e <= %.0e AND min eig Im F~^{-1} = %+.3e >= "
          "-%.0e" % (d, herg_f, HERG_FLOOR, herg_m, HERG_FLOOR),
          herg_f <= HERG_FLOOR and herg_m >= -HERG_FLOOR)

    fmax = max(float(np.max(np.abs(F))) for F in Ft)
    lmax_band = max(float(spec[M]["lam"][d - 1]) for M in FLAD)
    check("G1.9a boundedness (d=%d): max |F~| entry = %.3e <= "
          "lam_max(band) + |z|_max + %.0e = %.3e; max overlap "
          "sigma = %.6f <= 1 + 1e-12"
          % (d, fmax, BOUND_TOL,
             lmax_band + abs(Z_REF) + BOUND_TOL, sig_max),
          fmax <= lmax_band + abs(Z_REF) + BOUND_TOL
          and sig_max <= 1.0 + 1.0e-12)
    return b_ok


# ------------------------------------------------ q_f levels (report)
def qf_levels(spec, F, names):
    print("\n-- settled q_f levels (band rule = %d lowest, "
          "drainage object verbatim; med%d over M %d..%d NEW vs "
          "%d..%d DRAIN; reported, never gated)"
          % (K_QF, N_MED, TOP5_NEW[0], TOP5_NEW[-1], TOP5_DRAIN[0],
             TOP5_DRAIN[-1]))
    qmap = {M: np.sum((spec[M]["V9"][:NPAD, :K_QF].T @ F) ** 2,
                      axis=0) for M in FLAD}
    med_dr = np.median(np.stack([qmap[M] for M in TOP5_DRAIN]),
                       axis=0)
    med_nw = np.median(np.stack([qmap[M] for M in TOP5_NEW]),
                       axis=0)
    xs_x = np.array([M * D for M in XLAD])
    q_x = np.stack([qmap[M] for M in XLAD])
    print("  %-18s %-8s %-8s %-8s %s"
          % ("function", "drain", "new", "ratio", "ext rate b/X"))
    dev_worst = 0.0
    for j, nm in enumerate(names):
        b = fall_rate(xs_x, q_x[:, j])
        print("  %-18s %.4f   %.4f   %5.3f   %+6.3f"
              % (nm, med_dr[j], med_nw[j],
                 med_nw[j] / max(med_dr[j], QF_FLOOR), b))
        if nm in DRAIN_LEVELS:
            dev_worst = max(dev_worst,
                            abs(med_dr[j] - DRAIN_LEVELS[nm]))
    check("G1.5c drainage settled-level reproduction: med%d over "
          "%d..%d matches the nine frozen drainage values, worst "
          "dev %.1e <= %.0e" % (N_MED, TOP5_DRAIN[0], TOP5_DRAIN[-1],
                                dev_worst, REPRO_QTOL),
          dev_worst <= REPRO_QTOL)
    qall = np.stack([qmap[M] for M in FLAD])
    check("G1.9b boundedness: every band q_f in [%.1e, %.4f] "
          "inside [-1e-12, 1 + %.0e]"
          % (float(np.min(qall)), float(np.max(qall)), BOUND_TOL),
          float(np.min(qall)) >= -1.0e-12
          and float(np.max(qall)) <= 1.0 + BOUND_TOL)


# ------------------------------------------------ controls
def run_controls(c_cont, alpha_xd, ka_xd, mu_deep):
    print("\n-- controls (must fire; fire rule = "
          "qf_spectral_bundle_probe.control_bundle verbatim)")
    rng = np.random.default_rng(SEED)
    pos = np.sort(rng.uniform(0.5, 2.0 * alpha_xd, ka_xd))
    cat_s, _dd = core.atom_lags_at(alpha_xd, M_TOP_XD, pos,
                                   mu_deep[:ka_xd])
    Ts = sla.toeplitz((c_cont + cat_s)[:M_TOP_XD])
    fire_s, det_s = qsb.control_bundle(Ts, qsb.CTRL_LAD_S,
                                       "scramble")
    check("CS position-scramble control (1e9 comb, %d atoms) "
          "fires" % ka_xd, fire_s, det_s)

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
    print("QF OFFENSIVE strand 3, module 3 follow-up -- edge "
          "separation: the 7/8 edge on the 1e9 comb (X <= %.4f)"
          % (M_TOP_XD * D))
    print("=" * 78)

    hits = ast_firewall()
    check("G0.1 AST firewall (band rule is an eigenvalue-order "
          "rule of the source operator; no target information)",
          not hits, str(hits))
    bats, spec_sha = freeze_spec()
    check("G0.2 battery + cap + ladders + blocks + bars + anchors "
          "SHA-256-frozen BEFORE any comb data is built here", True,
          "SHA256 %s..." % spec_sha[:16])
    check("G0.3 reach census: M_TOP = %d <= floor(64 ln %d) = %d "
          "(X = %.6f <= %.6f); sieve cover exp(X_top) + 2 = %d <= "
          "%d; runtime cap %.0f s predeclared"
          % (M_TOP_XD, ATOM_MAX_XD, M_CAP_XD, M_TOP_XD * D,
             math.log(ATOM_MAX_XD),
             int(math.exp(M_TOP_XD * D)) + 2, ATOM_MAX_XD,
             RUNTIME_CAP),
          M_TOP_XD <= M_CAP_XD
          and int(math.exp(M_TOP_XD * D)) + 2 <= ATOM_MAX_XD)

    # ---- comb + towers strictly after the freeze
    u_deep, mu_deep = build_deep_comb()
    T_par = build_parent_tower()
    T, c_cont, alpha_xd, ka_xd = build_deep_tower(u_deep, mu_deep,
                                                  T_par)

    # ---- spectra on the census ladder
    spec = spectral_pass(T, CENS)
    F, names = battery_matrix(bats)
    pd_min = min(float(spec[M]["lam"][0]) for M in CENS)
    print("  PD margins (measured, never gated): lambda_min = "
          "%.3e (M %d) -> %.3e (M %d)"
          % (spec[M_TOP_FES]["lam"][0], M_TOP_FES,
             spec[M_TOP_XD]["lam"][0], M_TOP_XD))
    check("G1.6 measured PD: lambda_min = %.3e > -%.0e on every "
          "rung (measured output; no gate uses a PD margin or "
          "1/eps)" % (pd_min, PD_TOL), pd_min > -PD_TOL)

    # ---- anchors, gates, reports
    anchor_guards(spec)
    a_ok = edge_gap_analysis(spec)
    km2 = cadence(spec)
    b_ok = feshbach_d7(spec)
    qf_levels(spec, F, names)

    # ---- controls
    run_controls(c_cont, alpha_xd, ka_xd, mu_deep)

    # ---- runtime guard (predeclared)
    dt = time.time() - T_START
    check("G0.4 runtime %.1f s <= predeclared cap %.0f s"
          % (dt, RUNTIME_CAP), dt <= RUNTIME_CAP)

    # ---- verdict (preregistered decision order)
    guards_ok = all(ok for (n, ok) in CHECKS
                    if not n.startswith(("CS", "CE")))
    controls_ok = all(ok for (n, ok) in CHECKS
                      if n.startswith(("CS", "CE")))
    if not (guards_ok and controls_ok):
        verdict = "EDGE-UNDECIDED (invalid run)"
    elif a_ok and b_ok:
        verdict = "EDGE-SEPARATES-D7"
    elif (not a_ok) or km2:
        verdict = "EDGE-KEEPS-MOVING"
    else:
        verdict = "EDGE-UNDECIDED"

    n_gate = sum(1 for (_n, ok) in GATES if ok)
    n_chk = sum(1 for (_n, ok) in CHECKS if ok)
    print("\nVERDICT: %s" % verdict)
    print("GATES %d/%d (A=%s B=%s KM2=%s), GUARDS+CONTROLS %d/%d, "
          "runtime %.1f s"
          % (n_gate, len(GATES), "P" if a_ok else "F",
             "P" if b_ok else "F", "fires" if km2 else "quiet",
             n_chk, len(CHECKS), time.time() - T_START))
    if verdict == "EDGE-SEPARATES-D7":
        print("CONSEQUENCE (stated plainly): the 7/8 edge separates "
              "again at depth and the transported d = 7 block is "
              "Cauchy at the parent bars -- the fixed-d Feshbach "
              "limit EXISTS after all: the boundary-triple module "
              "reopens with d = 7 (the z -> 0 transition of "
              "M~(z) = F~(z)^{-1} on the d = 7 limit block is its "
              "remaining task).  NOT claimed: X -> infinity, "
              "eps-uniformity, RH.")
    elif verdict == "EDGE-KEEPS-MOVING":
        print("CONSEQUENCE (stated plainly): the band edge KEEPS "
              "MOVING -- descending modes overrun every fixed band "
              "dimension at the measured entry positions above; "
              "fixed-d Feshbach is CLOSED on every reachable "
              "surface, and the cell-cocycle formulation (depth-"
              "dependent d(X) with transition maps at the mode-"
              "entry rungs) is the only remaining path of the "
              "diagonal route.  The measured cadence is the new "
              "named structural constant of that module.  NO RH "
              "claim, no X -> infinity claim.")
    else:
        print("CONSEQUENCE (stated plainly): the edge bars are not "
              "reached either way at X = %.4f -- the gap tail, "
              "Cauchy numbers and cadence table above say exactly "
              "what a deeper comb must decide (next predicted "
              "entry depth printed in the cadence block).  NO RH "
              "claim." % (M_TOP_XD * D))
    return 0 if (guards_ok and controls_ok) else 1


if __name__ == "__main__":
    sys.exit(run())
