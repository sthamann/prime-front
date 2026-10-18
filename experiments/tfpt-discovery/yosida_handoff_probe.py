#!/usr/bin/env python3
"""GLOBAL-HANDOFF-OFFENSIVE -- the kernel-safe eps -> 0 decider via the
bounded Yosida transform, yosida_handoff_probe (strand: kernel-safe
epsilon limit; intended promotion target v763_yosida_handoff).

Exploration only (tfpt-experiment firewall): NOT wired into run_all.py,
no ledger row, no paper edit, no website edit, NO RH CLAIM, and this
probe writes no files.  It never reads a zero ordinate and never
evaluates the target before every source object is built and SHA-256
frozen (same discipline as all parent probes).

INPUT STATE (frozen findings, none re-adjudicated here):
  *  handoff_bulk_probe -- HANDOFF-BULK-CONVERGES: the eps-regulated
     resolvent G^eps = (A_X + eps I)^{-1} is the admissible
     operator-system evaluation; the bare A^{-1} does NOT stabilize
     (named negative block) and stays FORBIDDEN here.
  *  handoff_tail_weil_probe -- HANDOFF-TAIL-WEIL-PARTIAL: b values
     eps 1e-1: 0.179/0.181, 1e-2: 0.216/0.129 (R = 1/2, 18-rung
     interleave); the two eps = 1e-3 cells failed its endpoint gates.
  *  handoff_compat_eps3_probe -- COMPAT-EPS3-CONVERGES on the SAME
     geometry reused here (LAD_A = 256..816 step 16, B = A + 8,
     M_TOP = 824): b(eps) table 1e-1: 0.239/0.185, 1e-2: 0.259/0.149,
     1e-3: 0.178/0.186; outlook eps = 3e-4: R = 1 second-half slope
     turns NEGATIVE (b2 = -0.011) -- the first concrete sign of the
     eps -> 0 wall; eps = 0 PD margins fall 5.289e-5 (W_256) ->
     8.265e-6 (W_824).

OBJECT (the kernel-safe route): the eps -> 0 wall of the resolvent
formulation sits in the INSTRUMENT, not necessarily in the object: the
resolvent bound ||G^eps|| <= 1/eps forces a positive-margin assumption
at the limit.  The bounded YOSIDA TRANSFORM

    Y_eps = A (A + eps I)^{-1} = I - eps (A + eps I)^{-1}

needs no margin: for PSD A it satisfies the SANDWICH 0 <= Y_eps <= I,
and as eps decreases Y_eps increases MONOTONELY (spectral map
g_eps(l) = l/(l + eps), pointwise increasing in decreasing eps for
l >= 0) with strong limit = the orthogonal projection onto the closure
of range(A).  Exact zero modes are ALLOWED -- the Ihara lesson already
typed in the repo: true RH analogues can carry exact null modes after
rank saturation; a uniform positive eigenvalue margin is stronger than
needed and the wrong instrument.  Everything below uses ONLY A >= 0
(measured, never assumed as a margin) and bounded spectral functions
of A; the bare A^{-1} is never formed.

PREDECLARED ALGEBRA (honesty, stated BEFORE the run): on nested
window prefixes the battery Gram <f_i, f_j> is window-independent, so
the Y-form cross-window defect is EXACTLY eps times the resolvent
defect: E_Y = Gram - eps E_G  =>  E_Y(B) - E_Y(A) = -eps (E_G(B) -
E_G(A)).  The measured content of Q1 is therefore NOT a new rate but
(i) that the identical falling rates are carried by an observable
BOUNDED BY 1 on an O(1) scale (no 1/eps normalization anywhere),
(ii) that the defect AMPLITUDE shrinks linearly in eps on that fixed
scale (the eps- and X-limits lose their fight on the reachable
surface), and (iii) the sandwich + double monotonicity certificates
(increasing in decreasing eps, decreasing in growing X via PSD Schur
increments).  This equality is declared here so it cannot be sold as
an independent discovery.

FINITE-M HONESTY (declared): at every finite window A_M is PD, so
Y_eps -> I strongly and every fixed-f limit exists trivially.  The
non-trivial measured content is (a) the QUANTIFIED Cauchy/contraction
profiles per fixed f on the frozen eps ladder, (b) their stability
along the X ladder, and (c) the near-null spectral structure that
would become the kernel of the limit object.  No X -> infinity claim
is made; the diagonal strategy (fixed f, then X, then eps) is
assessed, not proven.

FROZEN CONSTRUCTION (all reused verbatim, none invented): tower lag
vector and channels from simpler_schur_recursion_probe (DGRID = 1/64,
channel_masks, continuum_lags, atom_channel_lags) exactly as in
handoff_compat_eps3_probe.build_tower; local battery = module-1
handoff_bulk_probe.battery (4 boxes + 3 hats per R, l2-normalized),
R in {1, 2}; interleaved prefix ladders LAD_A = 256..816 step 16,
LAD_B = LAD_A + 8, M_TOP = 824 (deepest step-8-aligned rung under the
table cap 825); rate fit = handoff_bulk_probe.fit_rate verbatim;
resolvent rows Ward-checked against handoff_tail_weil_probe.
compat_rows verbatim; Epstein atoms from epstein_firewall_probe
(read-only); scramble via v563_paper2_readouts.atom_lags_at.

FROZEN GRIDS AND BARS (all fixed here BEFORE the first run):
  eps ladder (decadic)  EPS_LADDER = 1e-1, 1e-2, 1e-3, 1e-4, 1e-5.
  gated eps for Q1      EPS_GATED  = 1e-1, 1e-2, 1e-3 (the documented
                        cells); 1e-4 and 1e-5 are REPORTED outlook
                        cells, never gated (the wall side).
  spectral rung set     QLAD = 256..800 step 32, plus 824 (19 rungs).
  near-null threshold   THR_NULL = 1e-4 (between the top-rung PD
                        margin 8.3e-6 and the first eps decade);
                        THR_DEEP = 1e-5 reported.
  Q1 bars: rate b_Y >= 0.10 per X unit; |b_Y - b_G(same run)| <= 1e-3
      (the predeclared algebra, allowed float-cancellation slack);
      X-monotonicity certificate max diag increment of E_Y <= 1e-8;
      sandwich guard -1e-9 <= diag(E_Y) <= 1 + 1e-9 on every rung of
      every eps; med5 / b2 reported per cell (not gated).
  Q2 bars (branch (i) OR (ii), realized branch reported):
      (i)  stable object: near-null count spread over the last 5 QLAD
           rungs <= 3 AND mean consecutive subspace alignment over the
           last 4 rung pairs >= 0.80 (alignment = ||V_new^T
           pad(V_old)||_F^2 / dim_old in [0, 1]);
      (ii) stable battery weight: total near-null battery weight
           rel spread (max-min)/max over the last 5 QLAD rungs <= 0.5.
  Q3 bars (branch (i) OR (ii), realized branch reported):
      (i)  vanishing: max over the 14 battery functions of the
           near-null weight q_f = sum_{l <= THR_NULL} <v, f>^2 at
           M_TOP <= 1e-3;
      (ii) admissible stable null pairing: every f with q_f > 1e-3
           has rel spread of q_f over the last 5 QLAD rungs <= 0.5.
      The full 14-function pairing table is printed either way.
  Q4 bars (per fixed f at M_TOP; uniformity across f NOT required):
      monotone certificate min eps-increment of <f, Y_eps f> >=
      -1e-12 on EVERY QLAD rung; deficit contraction
      (1 - y(1e-5)) / (1 - y(1e-1)) <= 0.25 at M_TOP; the full
      increment/ratio profiles and their X-stability (M = 800 vs 824)
      are REPORTED, not gated.
  Guards: AST firewall; SHA-256 freeze of battery bytes + every
      ladder + eps grid + threshold + bar BEFORE any comb data load;
      reach census (824 <= floor(64 ln ATOM_MAX) = 825, sieve cover);
      comb consistency rel dev <= 1e-12; resolvent-identity Ward
      max |A_M G^eps F - (F - eps G^eps F)| / max|F| <= 1e-8
      (verifies Y f = A (A+eps)^{-1} f = f - eps G^eps f in floats);
      verbatim-machinery Ward my E_G == handoff_tail_weil_probe.
      compat_rows at eps = 1e-2 rel <= 1e-10; spectral-vs-Cholesky
      Ward on diag(E_Y) at M_TOP rel <= 1e-8; scale audit: every
      Y-defect scale in [1e-3, 1.5] (an O(1) scale -- the numeric
      form of "no 1/eps normalization entered any gate"); real-data
      operator sandwich at M = 512: all Yosida eigenvalues in
      [-1e-9, 1 + 1e-9] for every eps.
KILL (frozen): if any gate had to be normalized by ||(A + eps I)^{-1}||
(a 1/eps-sized bound) or needed a positive lower eigenvalue bound on
A, the wall sits in the assumption again -- verdict DEAD.  Structural
audit: every gated quantity above is a bounded quadratic form of
Y_eps (|.| <= 1 by the sandwich), a ratio of two such, or a rate fit
on their logs with an O(1) scale; the scale-audit guard measures this.

CONTROLS (mandatory, must fire; spectral map at M_CTRL = 512, frozen):
  CS position scramble (positions uniform in (0.5, 2 alpha), masses
  kept, seed 7) and CE Epstein x^2 + 5y^2 atoms (Lambda_E via lattice
  count + Dirichlet division, epstein_firewall_probe read-only, tower
  cap M = 640, control prefix 512).  For indefinite A the spectral map
  g_eps(l) = l/(l + eps) leaves [0, 1]: FIRE = [exists eps in
  EPS_LADDER with min g < -0.01 or max g > 1.01 (sandwich break)] OR
  [battery eps-monotonicity violation: some increment < -1e-6] OR
  [|l + eps| < 1e-12 for some eigenvalue (singular Yosida)].  A
  control that keeps the sandwich, stays monotone, and is nonsingular
  has spuriously converged: the run is DEAD.

VERDICT ENUM (frozen): YOSIDA-KERNEL-SAFE = all guards pass AND both
controls fire AND Q1 (all 6 gated cells + mono + sandwich) AND Q2 AND
Q3 AND Q4 all decided positively.  YOSIDA-PARTIAL = guards + controls
ok AND >= 2 of the four questions pass (the open ones are named with
their exact failing numbers).  YOSIDA-DEAD = any guard fails, any
control spuriously converges, <= 1 question passes, or the KILL
trigger (a 1/eps bound or positive-margin assumption inside a gate).

STOP-LIST (binding, inherited): no bare A^{-1}; no positive-margin
assumptions; no fits inside proof-grade statements (measured rates
reported as measured); no Riemann zeros; no domino variants, no layer
positivizations, no norm triangles, no perturbation theory.  NO RH
claim.  This probe writes no files.  Runtime minutes.

RESULTS (2026-08-04, first and only preregistered run, 1.7 s; GATES
9/10, GUARDS+CONTROLS 12/12, verdict YOSIDA-PARTIAL -- Q1, Q2, Q4
decided positively, Q3 OPEN as preregistered):
  *  Q1 PASS 6/6 + mono -- the handoff observable IS formulable
     entirely through Y_eps: b_Y = 0.239/0.185 (eps 1e-1),
     0.259/0.149 (1e-2), 0.178/0.186 (1e-3) for R = 1/2, reproducing
     the resolvent rates on the same geometry to |b_Y - b_G| <=
     1.0e-13 (the predeclared algebra, verified in floats, not
     assumed); SANDWICH 0.0028 <= diag(E_Y) <= 1 - 6.8e-3 over all
     360 (eps, rung) evaluations; X-MONOTONE certificate: max diag
     increment -8.3e-8 (strictly decreasing); defect scales
     0.012..0.983, all O(1).  OUTLOOK (reported, never gated): the
     wall reappears as RATE COLLAPSE two decades below the gated
     cells -- eps = 1e-4: b_Y = 0.127/0.058 (R = 2 under the 0.10
     bar, b2 = -0.026); eps = 1e-5: b_Y = 0.094/0.008 with med5 =
     1.52/1.08 (the ladder no longer falls).
  *  MEASURED CORRECTION of a predeclared expectation (honesty): the
     Y-defect amplitude does NOT shrink linearly in eps.  Final-rung
     Y-defect: R = 1: 3.9e-3 -> 4.4e-5 (~ eps^0.49 over 4 decades);
     R = 2: 5.0e-3 -> 5.9e-4 (~ eps^0.23).  The resolvent defect
     grows toward the spectral edge and eats most of the eps factor;
     the amplitude still falls monotonely in eps on the fixed O(1)
     scale, but sublinearly -- the wall is weakened, not erased, and
     its carrier is exactly the Q3 weight below.
  *  Q2 PASS branch (i) AND (ii) -- the kernel part IS explicitly
     identifiable as a stable object: near-null count (lam <= 1e-4)
     = 1 -> 5 over QLAD with last-5 spread 1 <= 3; consecutive
     subspace alignment 0.961..0.998, mean of last 4 = 0.988 >=
     0.80; a SINGLE deep mode (lam <= 1e-5) appears at M = 736 and
     persists to the top.  Branch (ii) is thin: total near-null
     battery weight 1.67..3.17 on the last 5 rungs, rel spread 0.473
     vs bar 0.5.  PD margins (reported, never gated): 5.289e-5
     (M 256) -> 8.265e-6 (M 824).
  *  Q3 FAIL both branches -- THE central honest finding: the
     near-null pairing neither vanishes nor is stable on the
     reachable surface.  ALL 14 battery functions pair above 1e-3;
     max q_f = 4.46e-1 (R2:box[0,R]; the battery parks up to ~45% of
     its mass on the near-null subspace), per-f rel spreads
     0.309..0.711 (worst R1:hat(R/4,R/4) = 0.711 > 0.5).  This
     growing/fluctuating weight is precisely what stalls the
     small-eps handoff rate in the Q1 outlook cells: the two
     failures are one phenomenon seen from two sides.
  *  Q4 PASS 14/14 -- for every fixed battery f the eps -> 0 limit
     goes through with measured certificates: monotone on every QLAD
     rung (min eps-increment +2.2e-2 >= -1e-12), deficit contraction
     0.0106..0.1079 <= 0.25 over four decades; median Cauchy-ratio
     profile 3.08/1.43/0.46 (increments PEAK at the middle decades
     -- the spectral mass of the battery sits at lam ~ 1e-3..1e-4 --
     and contract only on the last step).  HONEST LIMIT: the
     last-step contraction leans on the finite-M spectral floor
     (lambda_min = 8.3e-6 < 1e-5); the increment profile is X-stable
     to 1.5e-3 (M 800 vs 824, reported), but no X -> infinity claim
     follows.
  *  CONTROLS both fire: CS scramble lambda_min = -1.10e+3, 206/512
     negative eigenvalues, sandwich break max g = 5.1, 4 battery
     monotonicity violations (worst -8.1e-3); CE Epstein (496
     negative atom sites) lambda_min = -3.32e+1, 189/512 negative,
     min g = -2.5, max g = 23, 56 violations (worst -5.1e-2).
     Indefinite data destroys exactly the sandwich/monotonicity
     certificates the real tower satisfies.
  *  KILL audit PASS: no gate was normalized by ||(A + eps I)^{-1}||
     or a PD margin; every gated quantity is a bounded Y-form
     statistic on an O(1) scale (audit band held: 0.012..0.983);
     the PD of the real tower is measured output (G1.2 sandwich),
     never an assumption inside a gate.
  *  HONEST STATEMENT (does the kernel-safe route carry the diagonal
     strategy fixed f -> X -> eps?): PARTIALLY.  (fixed f) Every
     battery function has a monotone, contraction-certified
     eps-limit at every reachable window -- Q4.  (then X) The
     Y-observable is monotone decreasing in X and carries the
     documented falling handoff rates at the documented eps -- Q1;
     the near-null subspace converges to a stable identified object
     -- Q2.  (then eps) The joint corner (small eps AND deep X) is
     carried ONLY IF the battery null-pairing q_f(X) converges along
     the tower -- and it does NOT yet (Q3): the route BREAKS exactly
     there.  What the Yosida transform achieves: the wall is
     relocated from a forbidden instrument (a 1/eps resolvent bound
     / positive-margin assumption) into a bounded, well-posed object
     (q_f in [0, 1], the pairing of the frozen battery with the
     identified near-kernel), whose X-convergence is now THE
     remaining question.  Exact zero modes stay admissible (Ihara
     lesson); nothing here needs A > 0.  NO RH claim, no X ->
     infinity claim; deeper towers or a battery orthogonalized
     against the identified near-kernel are the two named next
     probes.

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/yosida_handoff_probe.py
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
import handoff_tail_weil_probe as htw  # noqa: E402
import epstein_firewall_probe as epx  # noqa: E402

T_START = time.time()

# ------------------------------------------------ frozen specification
D = srp.DGRID                        # 1/64, dyadic float-exact
M_CAP = int(math.floor(math.log(core.ATOM_MAX) / D))   # 825
M_TOP = 824                          # deepest step-8-aligned rung
LAD_A = list(range(256, 817, 16))    # 36 rungs, X = 4.0 .. 12.75
LAD_OFF = 8                          # ladder B = A + 8 cells
QLAD = list(range(256, 801, 32)) + [824]   # 19 spectral rungs

R_BAT = (1.0, 2.0)                   # frozen module-1 local battery
EPS_LADDER = (1.0e-1, 1.0e-2, 1.0e-3, 1.0e-4, 1.0e-5)  # decadic
EPS_GATED = (1.0e-1, 1.0e-2, 1.0e-3)  # documented cells (gated)
EPS_WREF = 1.0e-2                    # verbatim-machinery Ward eps

THR_NULL = 1.0e-4                    # near-null threshold (Q2/Q3)
THR_DEEP = 1.0e-5                    # reported deep threshold
N_MED = 5                            # median block (reported)

Q1_RATE = 0.10                       # b_Y bar per X unit
Q1_MATCH = 1.0e-3                    # |b_Y - b_G| same-run bar
Q1_XMONO = 1.0e-8                    # X-monotone diag certificate
SANDWICH_TOL = 1.0e-9                # 0 <= diag(E_Y) <= 1 slack
SCALE_LO, SCALE_HI = 1.0e-3, 1.5     # O(1) scale audit band (KILL)
Q2_NSPREAD = 3                       # near-null count spread, last 5
Q2_ALIGN = 0.80                      # mean subspace alignment, last 4
Q2_WSPREAD = 0.5                     # battery weight rel spread
Q3_VANISH = 1.0e-3                   # vanishing-pairing bar
Q3_STAB = 0.5                        # stable-pairing rel spread bar
Q4_MONO = -1.0e-12                   # eps-monotone certificate floor
Q4_CONTRACT = 0.25                   # deficit contraction bar
WARD_RES = 1.0e-8                    # resolvent-identity Ward
WARD_REF = 1.0e-10                   # verbatim compat_rows Ward
WARD_SPEC = 1.0e-8                   # spectral vs Cholesky Ward

SBRK = 0.01                          # control sandwich break bar
CTRL_MONO = 1.0e-6                   # control monotonicity break bar
POLE_TOL = 1.0e-12                   # singular Yosida detection
M_CTRL = 512                         # control spectral rung
EP_NCAP = 34000                      # Epstein Lambda_E table reach
EP_MMAX = 640                        # Epstein control tower cap
SEED = 7
COMB_DEV_BAR = 1.0e-12

# documented parent rates for the REPORTED comparison (same geometry:
# handoff_compat_eps3_probe; task-quoted mixed-source values in
# parentheses in the printout)
PARENT_B = {1.0e-1: (0.239, 0.185), 1.0e-2: (0.259, 0.149),
            1.0e-3: (0.178, 0.186)}

BANNED = ("zetazero", "nzeros", "isprime", "primerange", "nextprime",
          "prevprime", "primepi", "sympy")

CHECKS = []       # guards + controls: all must pass, else invalid run
GATES = []        # Q1..Q4 gates: feed the verdict only


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
    """Battery bytes + every ladder + eps grid + threshold + bar,
    SHA-256 frozen BEFORE any comb/deployed data is loaded."""
    bats = {}
    hsh = hashlib.sha256()
    hsh.update(("yosida-handoff spec: 4 boxes + 3 hats per R, "
                "l2-norm, D=%.10f, R=%s; LAD_A=%d..%d step 16, "
                "LAD_B=A+%d, M_TOP=%d (cap %d); QLAD=%s; "
                "eps ladder=%s gated=%s; thr null=%g deep=%g; "
                "Q1: b>=%g match<=%g xmono<=%g sandwich<=%g "
                "scale=[%g,%g]; Q2: nspread<=%d align>=%g wspread<=%g;"
                " Q3: vanish<=%g stab<=%g; Q4: mono>=%g contract<=%g;"
                " wards res<=%g ref<=%g spec<=%g; controls: sbrk=%g "
                "mono=%g pole=%g M=%d seed=%d"
                % (D, R_BAT, LAD_A[0], LAD_A[-1], LAD_OFF, M_TOP,
                   M_CAP, QLAD, EPS_LADDER, EPS_GATED, THR_NULL,
                   THR_DEEP, Q1_RATE, Q1_MATCH, Q1_XMONO,
                   SANDWICH_TOL, SCALE_LO, SCALE_HI, Q2_NSPREAD,
                   Q2_ALIGN, Q2_WSPREAD, Q3_VANISH, Q3_STAB, Q4_MONO,
                   Q4_CONTRACT, WARD_RES, WARD_REF, WARD_SPEC, SBRK,
                   CTRL_MONO, POLE_TOL, M_CTRL, SEED)).encode())
    for R in R_BAT:
        bats[R] = hbp.battery(R)
        for nm, v in bats[R]:
            hsh.update(nm.encode())
            hsh.update(v.tobytes())
    return bats, hsh.hexdigest()


def battery_all(bats, M):
    """All 14 battery functions zero-padded to window size M."""
    cols, names = [], []
    for R in R_BAT:
        nR = int(round(R / D))
        for nm, v in bats[R]:
            f = np.zeros(M)
            f[:nR] = v
            cols.append(f)
            names.append("R%g:%s" % (R, nm))
    return np.stack(cols, axis=1), names


# ------------------------------------------------ tower (verbatim)
def build_tower():
    alpha_full = 0.5 * M_TOP * D
    ka, masks, dev_m = srp.channel_masks(alpha_full)
    check("G1.1 tower comb consistency (zeta-free Gauss double sieve "
          "== deployed masses, rel dev <= %.0e)" % COMB_DEV_BAR,
          dev_m <= COMB_DEV_BAR,
          "rel dev %.1e, ka=%d atoms to e^%.4f"
          % (dev_m, ka, 2.0 * alpha_full))
    c_cont = srp.continuum_lags(M_TOP)
    c_full = c_cont.copy()
    for cnl in ("ro", "re", "sp", "in"):
        c_full = c_full + srp.atom_channel_lags(alpha_full, M_TOP,
                                                masks[cnl])
    return sla.toeplitz(c_full[:M_TOP]), c_cont, alpha_full, ka


# ================================================== Q1: Y-form handoff
def yosida_pass(T, bats):
    """One Cholesky per (eps, M); from the SAME solve both the
    resolvent Gram E_G and the Yosida Gram E_Y = F^T (F - eps G F)
    are assembled -- Y f is computed as f - eps G^eps f and the
    resolvent identity A (G F) = F - eps G F is Ward-checked."""
    ladB = [m + LAD_OFF for m in LAD_A]
    sizes = sorted(set(LAD_A) | set(ladB))
    Fms = {R: np.stack([v for _n, v in bats[R]], axis=1)
           for R in R_BAT}
    res = {}
    for eps in EPS_LADDER:
        EG, EY = {}, {}
        ward = 0.0
        mid = sizes[len(sizes) // 2]
        for M in sizes:
            cf = sla.cho_factor(T[:M, :M] + eps * np.eye(M))
            perG, perY = {}, {}
            for R in R_BAT:
                nR = int(round(R / D))
                F = np.zeros((M, Fms[R].shape[1]))
                F[:nR] = Fms[R]
                GF = sla.cho_solve(cf, F)
                YF = F - eps * GF
                perG[R] = F.T @ GF
                EYm = F.T @ YF
                perY[R] = 0.5 * (EYm + EYm.T)
                if M == mid:
                    r = float(np.max(np.abs(T[:M, :M] @ GF - YF))
                              / max(np.max(np.abs(F)), 1.0e-300))
                    ward = max(ward, r)
            EG[M], EY[M] = perG, perY
        res[eps] = dict(EG=EG, EY=EY, ward=ward)
    return res, sizes, ladB


def defect_rows(E, ladB, R):
    d0 = np.diag(E[LAD_A[0]][R])
    scale = float(np.sqrt(np.max(d0) * np.min(d0)))
    rows = [dict(X=Ma * D, XmR=Ma * D - R,
                 mx=float(np.max(np.abs(E[Mb][R] - E[Ma][R])))
                 / scale)
            for Ma, Mb in zip(LAD_A, ladB)]
    return rows, scale


def stat_of(rows):
    mxs = [r["mx"] for r in rows]
    b, resid = hbp.fit_rate(rows)
    b2, _r2 = hbp.fit_rate(rows[len(rows) // 2:])
    med = float(np.median(mxs[-N_MED:])
                / max(np.median(mxs[:N_MED]), 1.0e-300))
    return b, resid, b2, med, mxs


def q1_block(T, bats):
    print("\n-- Q1: the handoff observable through Y_eps alone "
          "(bounded, O(1) scale)")
    res, sizes, ladB = yosida_pass(T, bats)

    # guards on the pass
    wmax = max(res[eps]["ward"] for eps in EPS_LADDER)
    check("G2.1 resolvent-identity Ward A(G^eps F) = F - eps G^eps F "
          "(mid rung, every eps) <= %.0e" % WARD_RES, wmax <= WARD_RES,
          "max rel %.1e" % wmax)
    rows_ref, E_ref = htw.compat_rows(T, LAD_A, ladB, EPS_WREF, bats)
    dref = 0.0
    for M in sorted(set(LAD_A) | set(ladB)):
        for R in R_BAT:
            num = float(np.max(np.abs(E_ref[M][R]
                                      - res[EPS_WREF]["EG"][M][R])))
            dref = max(dref, num / max(
                float(np.max(np.abs(E_ref[M][R]))), 1.0e-300))
    check("G2.2 verbatim-machinery Ward: E_G(this probe) == "
          "handoff_tail_weil_probe.compat_rows at eps = %g, rel <= "
          "%.0e" % (EPS_WREF, WARD_REF), dref <= WARD_REF,
          "max rel %.1e" % dref)

    # sandwich + X-monotone certificates over every eps and rung
    dmin, dmax, xmono = np.inf, -np.inf, -np.inf
    for eps in EPS_LADDER:
        for R in R_BAT:
            prev = None
            for M in sizes:
                dg = np.diag(res[eps]["EY"][M][R])
                dmin = min(dmin, float(np.min(dg)))
                dmax = max(dmax, float(np.max(dg)))
                if prev is not None:
                    xmono = max(xmono, float(np.max(dg - prev)))
                prev = dg
    check("G2.3 SANDWICH on real data: %.4f <= diag(E_Y) <= 1 - "
          "%.1e over all %d (eps, rung) evaluations (bars -%.0e / "
          "1+%.0e)" % (dmin, 1.0 - dmax, len(EPS_LADDER) * len(sizes),
                       SANDWICH_TOL, SANDWICH_TOL),
          dmin >= -SANDWICH_TOL and dmax <= 1.0 + SANDWICH_TOL)
    ok_xm = gate("Q1.mono X-MONOTONE certificate: diag(E_Y) is "
                 "non-increasing along the window ladder (PSD Schur "
                 "increments of E_G); max positive increment %.1e <= "
                 "%.0e, over every eps" % (xmono, Q1_XMONO),
                 xmono <= Q1_XMONO)

    # gated cells + reported outlook cells
    cells_ok = ok_xm
    scale_lo, scale_hi = np.inf, -np.inf
    for eps in EPS_LADDER:
        gated = eps in EPS_GATED
        for R in R_BAT:
            rowsY, scY = defect_rows(res[eps]["EY"], ladB, R)
            rowsG, _scG = defect_rows(res[eps]["EG"], ladB, R)
            scale_lo, scale_hi = min(scale_lo, scY), max(scale_hi,
                                                         scY)
            bY, resid, b2, med, mxs = stat_of(rowsY)
            bG, _rg, _b2g, _mg, _mxg = stat_of(rowsG)
            det = ("b_Y = %.3f (>= %g; resid %.2f reported), "
                   "|b_Y - b_G| = %.1e (<= %g), b2 = %.3f, med%d = "
                   "%.3f, Y-defect %s ... %s over X-R = %.2f..%.2f, "
                   "scale %.3f"
                   % (bY, Q1_RATE, resid, abs(bY - bG), Q1_MATCH, b2,
                      N_MED, med,
                      ", ".join("%.1e" % v for v in mxs[:2]),
                      ", ".join("%.1e" % v for v in mxs[-2:]),
                      rowsY[0]["XmR"], rowsY[-1]["XmR"], scY))
            if gated:
                ok = bY >= Q1_RATE and abs(bY - bG) <= Q1_MATCH
                cells_ok &= gate("Q1.eps=%g,R=%g (parent b_G = %.3f)"
                                 % (eps, R, PARENT_B[eps][
                                     0 if R == 1.0 else 1]), ok, det)
            else:
                print("  Q1 OUTLOOK eps=%g,R=%g (reported, never "
                      "gated): %s" % (eps, R, det))
    check("K1 KILL/scale audit: every Y-defect scale in [%g, %g] "
          "(O(1), bounded by the sandwich -- no 1/eps normalization "
          "entered any gate)" % (SCALE_LO, SCALE_HI),
          scale_lo >= SCALE_LO and scale_hi <= SCALE_HI,
          "scales %.3f .. %.3f" % (scale_lo, scale_hi))

    # eps-scaling of the final-rung Y defect (reported)
    print("  Q1 report -- final-rung Y-defect vs eps (the amplitude "
          "side of the kernel-safe claim):")
    for R in R_BAT:
        line = []
        for eps in EPS_LADDER:
            rowsY, _s = defect_rows(res[eps]["EY"], ladB, R)
            line.append("eps=%g: %.1e" % (eps, rowsY[-1]["mx"]))
        print("    R=%g: %s" % (R, "  ".join(line)))
    return cells_ok, res


# ================================================== Q2/Q3: spectral
def spectral_block(T, bats):
    out = []
    for M in QLAD:
        lam, V = np.linalg.eigh(T[:M, :M])
        Fall, names = battery_all(bats, M)
        wt = (V.T @ Fall) ** 2
        idx = np.nonzero(lam <= THR_NULL)[0]
        out.append(dict(M=M, lam=lam, wt=wt, Vn=V[:, idx],
                        nn=len(idx),
                        nn_deep=int(np.sum(lam <= THR_DEEP)),
                        qf=wt[idx].sum(axis=0)))
    return out, names


def y_profile(blk, eps_set):
    return np.stack([blk["wt"].T @ (blk["lam"] / (blk["lam"] + e))
                     for e in eps_set])   # (n_eps, 14)


def q2_block(spec):
    print("\n-- Q2: is the kernel part explicitly identifiable?")
    print("  PD margins (eps = 0, reported not gated): lambda_min = "
          "%.3e (M %d) -> %.3e (M %d)"
          % (spec[0]["lam"][0], spec[0]["M"], spec[-1]["lam"][0],
             spec[-1]["M"]))
    nns = [b["nn"] for b in spec]
    print("  near-null count (lam <= %g) along QLAD: %s"
          % (THR_NULL, "/".join(str(n) for n in nns)))
    print("  deep count (lam <= %g): %s"
          % (THR_DEEP, "/".join(str(b["nn_deep"]) for b in spec)))
    aligns = []
    for a, b in zip(spec, spec[1:]):
        if a["nn"] == 0 or b["nn"] == 0:
            aligns.append(None)
            continue
        Vp = np.zeros((b["M"], a["nn"]))
        Vp[:a["M"]] = a["Vn"]
        pr = b["Vn"].T @ Vp
        aligns.append(float(np.sum(pr ** 2) / a["nn"]))
    astr = "/".join("%.3f" % a if a is not None else "-"
                    for a in aligns)
    last5 = nns[-5:]
    spread = max(last5) - min(last5)
    a4 = [a for a in aligns[-4:] if a is not None]
    br1 = (spread <= Q2_NSPREAD and len(a4) == 4
           and float(np.mean(a4)) >= Q2_ALIGN)
    Qw = [float(np.sum(b["qf"])) for b in spec]
    w5 = Qw[-5:]
    wspread = (max(w5) - min(w5)) / max(max(w5), 1.0e-300)
    br2 = wspread <= Q2_WSPREAD
    return gate("Q2 kernel identifiability: branch(i) STABLE OBJECT "
                "%s (count spread last 5 = %d <= %d; consecutive "
                "subspace alignment %s, mean last 4 = %.3f >= %g) / "
                "branch(ii) STABLE BATTERY WEIGHT %s (total near-null"
                " weight last 5 = %s, rel spread %.3f <= %g)"
                % (br1, spread, Q2_NSPREAD, astr,
                   float(np.mean(a4)) if len(a4) == 4 else -1.0,
                   Q2_ALIGN, br2,
                   "/".join("%.2e" % w for w in w5), wspread,
                   Q2_WSPREAD), br1 or br2)


def q3_block(spec, names):
    print("\n-- Q3: does the kernel contribution vanish on the "
          "battery, or is it an admissible stable null pairing?")
    qtop = spec[-1]["qf"]
    qhist = np.stack([b["qf"] for b in spec[-5:]])
    spread_f = (qhist.max(axis=0) - qhist.min(axis=0)) \
        / np.maximum(qhist.max(axis=0), 1.0e-300)
    dfc = 1.0 - y_profile(spec[-1], (EPS_LADDER[-1],))[0]
    print("  pairing with EVERY battery function (M = %d): "
          "q_f = near-null weight (lam <= %g), spread = rel spread "
          "last 5 rungs, deficit = 1 - <f, Y_(1e-5) f>:"
          % (spec[-1]["M"], THR_NULL))
    for i, nm in enumerate(names):
        print("    %-18s q_f = %.2e  spread = %.3f  deficit = %.2e"
              % (nm, qtop[i], spread_f[i], dfc[i]))
    br1 = float(np.max(qtop)) <= Q3_VANISH
    big = [i for i in range(len(names)) if qtop[i] > Q3_VANISH]
    br2 = all(spread_f[i] <= Q3_STAB for i in big)
    return gate("Q3 battery pairing: branch(i) VANISHING %s (max q_f "
                "= %.2e vs %g) / branch(ii) ADMISSIBLE STABLE NULL "
                "PAIRING %s (%d funcs above %g, worst spread %.3f <= "
                "%g)" % (br1, float(np.max(qtop)), Q3_VANISH, br2,
                         len(big), Q3_VANISH,
                         max((spread_f[i] for i in big), default=0.0),
                         Q3_STAB), br1 or br2)


# ================================================== Q4: fixed-f limit
def q4_block(spec, names, res):
    print("\n-- Q4: fixed-f eps -> 0 limit via the spectral theorem "
          "(monotone + measured Cauchy rate)")
    mono_worst = np.inf
    for blk in spec:
        Y = y_profile(blk, EPS_LADDER)
        mono_worst = min(mono_worst, float(np.min(np.diff(Y,
                                                          axis=0))))
    top, prev = spec[-1], spec[-2]
    Yt = y_profile(top, EPS_LADDER)
    Yp = y_profile(prev, EPS_LADDER)
    dt, dp = np.diff(Yt, axis=0), np.diff(Yp, axis=0)
    contract = (1.0 - Yt[-1]) / np.maximum(1.0 - Yt[0], 1.0e-300)
    xstab = float(np.max(np.abs(dt - dp)))
    med_ratio = [float(np.median(dt[j + 1] / np.maximum(dt[j],
                                                        1.0e-300)))
                 for j in range(dt.shape[0] - 1)]
    print("  per-f profiles at M = %d (y = <f, Y_eps f> over eps = "
          "%s):" % (top["M"], "/".join("%g" % e for e in EPS_LADDER)))
    for i, nm in enumerate(names):
        rat = "/".join("%.2f" % (dt[j + 1, i]
                                 / max(dt[j, i], 1.0e-300))
                       for j in range(dt.shape[0] - 1))
        print("    %-18s y = %s  incr = %s  ratios = %s  "
              "contraction = %.4f"
              % (nm, "/".join("%.4f" % v for v in Yt[:, i]),
                 "/".join("%.1e" % v for v in dt[:, i]), rat,
                 contract[i]))
    print("  median Cauchy-ratio profile over the battery: %s; "
          "X-stability of the increments |d(M=%d) - d(M=%d)| <= %.1e "
          "(reported)" % ("/".join("%.2f" % r for r in med_ratio),
                          top["M"], prev["M"], xstab))
    # spectral-vs-Cholesky Ward on diag(E_Y) at the top rung
    wspec = 0.0
    for j, eps in enumerate(EPS_LADDER):
        ycho = np.concatenate([np.diag(res[eps]["EY"][M_TOP][R])
                               for R in R_BAT])
        wspec = max(wspec, float(np.max(np.abs(ycho - Yt[j]))))
    check("G3.1 spectral-vs-Cholesky Ward on diag(E_Y) at M = %d, "
          "every eps <= %.0e" % (M_TOP, WARD_SPEC),
          wspec <= WARD_SPEC, "max abs %.1e" % wspec)
    ok = (mono_worst >= Q4_MONO
          and float(np.max(contract)) <= Q4_CONTRACT)
    return gate("Q4 fixed-f limit: MONOTONE certificate min "
                "eps-increment = %+.1e >= %.0e on every QLAD rung; "
                "deficit contraction (1-y(1e-5))/(1-y(1e-1)) = "
                "%.4f..%.4f <= %g for all 14 f (uniformity across f "
                "NOT required and not claimed)"
                % (mono_worst, Q4_MONO, float(np.min(contract)),
                   float(np.max(contract)), Q4_CONTRACT), ok)


# ================================================== controls
def control_yosida(Tc, bats, label):
    A = Tc[:M_CTRL, :M_CTRL]
    lam, V = np.linalg.eigh(A)
    Fall, _names = battery_all(bats, M_CTRL)
    wt = (V.T @ Fall) ** 2
    nneg = int(np.sum(lam < 0.0))
    pole = min(float(np.min(np.abs(lam + e))) for e in EPS_LADDER)
    if pole < POLE_TOL:
        return True, ("SINGULAR Yosida: |lam + eps| = %.1e < %.0e "
                      "(lambda_min = %.2e, %d negative eigenvalues)"
                      % (pole, POLE_TOL, lam[0], nneg))
    gmin, gmax = np.inf, -np.inf
    Yb = []
    for e in EPS_LADDER:
        g = lam / (lam + e)
        gmin, gmax = min(gmin, float(np.min(g))), \
            max(gmax, float(np.max(g)))
        Yb.append(wt.T @ g)
    difs = np.diff(np.stack(Yb), axis=0)
    viol = float(np.min(difs))
    nviol = int(np.sum(difs < -CTRL_MONO))
    fire = (gmin < -SBRK) or (gmax > 1.0 + SBRK) \
        or (viol < -CTRL_MONO)
    return fire, ("lambda_min(A) = %.2e, %d/%d negative eigenvalues; "
                  "SANDWICH: min g = %.1e, max g = %.1e (bars "
                  "-%g / 1+%g); MONOTONICITY: %d battery violations, "
                  "worst increment %.1e (bar -%.0e): fire=%s"
                  % (lam[0], nneg, M_CTRL, gmin, gmax, SBRK, SBRK,
                     nviol, viol, CTRL_MONO, fire))


def run_controls(c_cont, alpha_full, ka, bats):
    print("\n-- controls (must fire: indefinite A destroys the "
          "sandwich / monotonicity of the Yosida map)")
    rng = np.random.default_rng(SEED)
    pos = np.sort(rng.uniform(0.5, 2.0 * alpha_full, ka))
    cat_s, _dd = core.atom_lags_at(alpha_full, M_TOP, pos,
                                   core.MU_ALL[:ka])
    Ts = sla.toeplitz((c_cont + cat_s)[:M_TOP])
    fire_s, det_s = control_yosida(Ts, bats, "scramble")
    check("CS position-scramble control fires", fire_s, det_s)

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
    fire_e, det_e = control_yosida(TE, bats, "epstein")
    check("CE Epstein control (x^2+5y^2, %d negative atom sites) "
          "fires" % int(np.sum(lamE[2:] < -1.0e-9)), fire_e, det_e)


# ================================================== run
def run():
    print("=" * 78)
    print("GLOBAL HANDOFF -- kernel-safe eps -> 0 decider (bounded "
          "Yosida transform)")
    print("=" * 78)

    hits = ast_firewall()
    check("G0.1 AST firewall", not hits, str(hits))
    bats, spec_sha = freeze_spec()
    check("G0.2 battery + ladders + eps grids + thresholds + bars "
          "SHA-256-frozen BEFORE any comb data load", True,
          "SHA256 %s..." % spec_sha[:16])
    check("G0.3 reach census: M_TOP = %d <= table cap %d (X = %.6f "
          "<= ln(ATOM_MAX) = %.6f); sieve cover exp(X_top) + 2 = %d "
          "<= ATOM_MAX = %d"
          % (M_TOP, M_CAP, M_TOP * D, math.log(core.ATOM_MAX),
             int(math.exp(M_TOP * D)) + 2, core.ATOM_MAX),
          M_TOP <= M_CAP
          and int(math.exp(M_TOP * D)) + 2 <= core.ATOM_MAX)

    # ---- first comb/deployed data touch strictly after the freeze
    T, c_cont, alpha_full, ka = build_tower()

    # ---- real-data operator sandwich at the control rung
    lamR = np.linalg.eigvalsh(T[:M_CTRL, :M_CTRL])
    gmin = min(float(np.min(lamR / (lamR + e))) for e in EPS_LADDER)
    gmax = max(float(np.max(lamR / (lamR + e))) for e in EPS_LADDER)
    check("G1.2 real-data operator sandwich at M = %d: all Yosida "
          "eigenvalues in [%.1e, 1 - %.1e] for every eps (bars "
          "-%.0e / 1+%.0e) -- PD is MEASURED output, never a gate "
          "assumption" % (M_CTRL, gmin, 1.0 - gmax, SANDWICH_TOL,
                          SANDWICH_TOL),
          gmin >= -SANDWICH_TOL and gmax <= 1.0 + SANDWICH_TOL)

    # ---- Q1
    q1_ok, res = q1_block(T, bats)

    # ---- Q2 / Q3 / Q4 (spectral)
    spec, names = spectral_block(T, bats)
    q2_ok = q2_block(spec)
    q3_ok = q3_block(spec, names)
    q4_ok = q4_block(spec, names, res)

    # ---- controls
    run_controls(c_cont, alpha_full, ka, bats)

    # ---- verdict (preregistered rules)
    guards_ok = all(ok for (n, ok) in CHECKS
                    if not n.startswith(("CS", "CE")))
    controls_ok = all(ok for (n, ok) in CHECKS
                      if n.startswith(("CS", "CE")))
    qs = dict(Q1=q1_ok, Q2=q2_ok, Q3=q3_ok, Q4=q4_ok)
    n_q = sum(1 for v in qs.values() if v)
    if guards_ok and controls_ok and n_q == 4:
        verdict = "YOSIDA-KERNEL-SAFE"
    elif guards_ok and controls_ok and n_q >= 2:
        verdict = "YOSIDA-PARTIAL"
    else:
        verdict = "YOSIDA-DEAD"

    n_gate = sum(1 for (_n, ok) in GATES if ok)
    n_chk = sum(1 for (_n, ok) in CHECKS if ok)
    print("\nVERDICT: %s" % verdict)
    print("GATES %d/%d, GUARDS+CONTROLS %d/%d, questions %s, "
          "runtime %.1f s"
          % (n_gate, len(GATES), n_chk, len(CHECKS),
             " ".join("%s=%s" % (k, "PASS" if v else "FAIL")
                      for k, v in qs.items()), time.time() - T_START))
    if verdict == "YOSIDA-KERNEL-SAFE":
        print("CONSEQUENCE: the eps -> 0 limit is treated WITHOUT a "
              "positive eigenvalue margin -- the handoff observable "
              "lives on the bounded Yosida transform (sandwich + "
              "double monotonicity certificates), the near-null part "
              "is an identified stable object with a quantified, "
              "admissible battery pairing (Ihara lesson: exact null "
              "modes allowed), and every fixed test function has a "
              "monotone, contraction-certified eps-limit.  The "
              "resolvent wall is BYPASSED, not solved: no statement "
              "beyond the reachable surface, no X -> infinity claim, "
              "NO RH claim.")
    elif verdict == "YOSIDA-PARTIAL":
        print("HONEST READING: the open questions are %s -- their "
              "exact failing numbers are printed above; the "
              "kernel-safe route carries only the decided part."
              % ", ".join(k for k, v in qs.items() if not v))
    else:
        print("KILL: a guard failed, a control spuriously converged, "
              "or the route needs the forbidden 1/eps bound -- the "
              "kernel-safe formulation closes honestly at this "
              "surface.")
    return 0 if (guards_ok and controls_ok) else 1


if __name__ == "__main__":
    sys.exit(run())
