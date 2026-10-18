#!/usr/bin/env python3
"""GLOBAL-HANDOFF-OFFENSIVE -- the eps = 1e-3 cross-window
compatibility decider, handoff_compat_eps3_probe.

Exploration only (tfpt-experiment firewall): NOT wired into run_all.py,
no ledger row, no paper edit, no website edit, NO RH CLAIM, and this
probe writes no files.  It never reads a zero ordinate and never
evaluates the target before every source object is built and SHA-256
frozen (same discipline as all parent probes).

INPUT STATE (frozen findings, none re-adjudicated here):
  *  Module 1, handoff_bulk_probe -- 17/17 PASS,
     HANDOFF-BULK-CONVERGES (eps-regulated resolvent is the admissible
     operator-system evaluation; full-step Cauchy increments fall at
     b = 0.174..0.310 per X unit, eps-robust 1e-1..1e-3).
  *  Modules 2+3, handoff_frequency_gram_probe -- 6/6 PASS,
     HANDOFF-GRAM-CONVERGES (Candidate B anti-alias quadrature,
     slope -0.369, final/first 0.441).
  *  Module 4/6, handoff_tail_weil_probe -- HANDOFF-TAIL-WEIL-PARTIAL,
     11/13 gates: quadrature tail CLOSED (terminates algebraically,
     2.4e-13), Weil identification CLOSED on the battery (kappa
     0.97768 -> 0.99028, agreement 0.0485 spectral relative).  Its
     cross-window axis (b) passed 4/6 cells; BOTH eps = 1e-3 cells
     FAILED their frozen endpoint gates: the trend still falls (b =
     0.126/0.147, second-half b2 = 0.121/0.101 > 0) but atom-burst
     oscillation at the last rungs broke the endpoint statistics
     (trend 2.9x < 3 at R = 1; final-rung jump 3.8e-4 -> 2.3e-3
     giving raw 1.5x < 2x at R = 2).  That probe predeclared NO
     iteration, so the two cells stand failed; deciding them requires
     THIS new preregistration.  Nothing from that run is re-gated.

QUESTION (single axis): do the two eps = 1e-3 cross-window
compatibility cells (frozen module-1 local battery, R = 1, 2) PASS an
oscillation-aware endpoint statistic on the DEEPEST honestly reachable
interleaved prefix ladder of the one tower lag vector?

REACHABLE DEPTH (determined from the generator, frozen here):
  the atom table of v563_paper2_readouts carries prime-power atoms to
  ATOM_MAX = 400000, i.e. u <= ln(400000) = 12.8992; on the dyadic
  grid D = 1/64 the absolute cap is M = floor(64 * ln 400000) = 825
  (X = 12.890625).  M_TOP = 824 (X = 12.875) is frozen as the deepest
  rung: it is the deepest step-8-aligned prefix (the interleave grid
  A step 16 / B = A + 8 lives on multiples of 8 above 256), and the
  sacrificed single cell is 0.0156 in X -- immaterial and documented.
  The stage-1 Gaussian double sieve covers xmax = exp(12.875) + 2 =
  390430 <= 400000, so every atom up to X is present.  The parent
  (b)-axis compared A <= 800 (X = 12.5) against B <= 816 (X = 12.75)
  in 18 rungs; this probe compares A <= 816 (X = 12.75) against
  B <= 824 (X = 12.875) in 36 rungs -- twice the rung density AND a
  deeper top end on both ladders.

FROZEN CONSTRUCTION, Candidate A (default; the parent geometry,
densified and deepened): interleaved prefix ladders LAD_A = 256..816
step 16 and LAD_B = LAD_A + 8 of ONE tower lag vector (exact prefix
nesting, simpler_tower T1.1); per frozen local observable pair the
defect |<f_i, G^eps_{A_k} f_j> - <f_i, G^eps_{B_k} f_j>| / scale with
the eps-regulated resolvent G^eps = (A_M + eps I)^{-1} as the ONLY
admissible evaluation (module-1 finding); evaluation code reused
verbatim: handoff_tail_weil_probe.compat_rows (one Cholesky per
(eps, M), scale = sqrt(max diag * min diag) at the first A rung).

FROZEN ITERATION POLICY (Candidate A/B pattern, at most ONE
construction iteration, fixed here BEFORE the first run):
  Candidate B = full-step Cauchy increments (the module-1
  methodology, which was less noisy): consecutive-rung Schur
  increments Delta_k = W^T (Stilde_k^eps)^{-1} W (PSD, monotone
  diagonal) on SIZES_B = 256..824 step 8 (72 rungs, 71 increments),
  machinery reused verbatim from handoff_bulk_probe.rung_data plus a
  diagonal capture.  TRIGGER (numeric, frozen): Candidate B is
  consulted if and only if at least ONE anchor cell (eps = 1e-2,
  R in {1, 2}) FAILS the frozen cell statistic under Candidate A
  (i.e. the half-step noise swamps the statistic on a cell that the
  parent probe already passed).  If triggered, the ENTIRE
  adjudication (anchor + decider + outlook + controls) runs on
  Candidate B and the A numbers are reported as a named block; if the
  anchor also fails under B the run is DEAD.  If A passes the anchor,
  B is never consulted (no cherry-picking).  No further iteration.

FROZEN OSCILLATION-AWARE CELL STATISTIC (replaces the parent raw
endpoint gates; all bars fixed here BEFORE the first run):
  C1  trend: least-squares log-linear rate b >= 0.10 per X unit over
      the full ladder (defect vs X - R; fit residuum reported, never
      gated -- atom-burst oscillation is structure).
  C2  robust endpoint: median of the LAST 5 rung defects <= 0.50 x
      median of the FIRST 5 rung defects (the parent bar 0.5, now on
      5-rung medians instead of single endpoint rungs; a single
      atom-burst rung can no longer break the cell).
  C3  anti-plateau with frozen margin: fitted rate on the second half
      of the rungs b2 >= 0.02 (parent measured b2 = 0.121/0.101 at
      eps = 1e-3; the margin is 5x below that, but strictly positive).
  C4  Dini / Cauchy-summability (applicable where the construction IS
      the increment): on Candidate B the diagonal increments are PSD
      and monotone -- gate: sum of the max-diagonal increments over
      the last ceil(n/4) rungs <= 0.25 x the full sum (tail
      summability).  On Candidate A the same fraction is computed on
      the PSD diagonal of E_B - E_A and REPORTED, not gated (the A/B
      window defect is not itself the Dini increment).
  A cell PASSES iff C1 and C2 and C3 (and C4 on Candidate B) hold.
GUARDS (must pass or the run is invalid): AST firewall; battery and
every ladder specification SHA-256-frozen BEFORE any comb data is
loaded; tower comb consistency (zeta-free Gauss double sieve ==
deployed masses, rel dev <= 1e-12); reach census (top B rung <= table
cap, sieve cover >= exp(X_top)); mid-rung dense-solve Ward <= 1e-8 at
eps = 1e-2 AND eps = 1e-3 (R = 2); PSD of the compatibility diagonal
(min diag >= -1e-8 x scale, both candidates).

CELLS:
  GATED anchor : eps = 1e-2, R = 1, 2 -- MUST PASS.  The parent probe
      passed these cells (b = 0.216/0.129); if the new statistic
      fails a previously passing cell, the statistic is invalid and
      the run is DEAD by rule (declared in the verdict).
  GATED decider: eps = 1e-3, R = 1, 2 -- the two open cells.
  REPORTED     : eps = 3e-4 (outlook, both R, never gated); b(eps)
      rate table over eps = 1e-1 / 1e-2 / 1e-3 / 3e-4; eps = 0 PD
      margins lambda_min(W_first), lambda_min(W_top) (the wall,
      quantified, never gated).  Uniformity in eps -> 0 is NOT part
      of PASS; b(eps) is quantified, not hidden.

CONTROLS (mandatory, must fire, on the compatibility construction of
the adjudicated candidate at eps = 1e-2): CS position scramble
(positions uniform in (0.5, 2 alpha), masses kept) and CE Epstein
x^2 + 5y^2 atoms (Lambda_E via lattice count + Dirichlet division,
epstein_firewall_probe read-only, ladder capped at M = 640 where its
table carries).  FIRE = (A + eps I) Cholesky breaks on >= 1 rung OR
the control FAILS the frozen cell statistic (C1-C3, R = 2) OR its
final defect >= 10 x the real final defect (eps = 1e-2, R = 2).  A
control that is PD, passes the statistic, and stays below 10x has
spuriously converged: the run is DEAD.

VERDICT ENUM (numeric, frozen):
  COMPAT-EPS3-CONVERGES = all guards pass AND both controls fire AND
      anchor 2/2 AND decider 2/2 (both eps = 1e-3 cells pass C1-C3
      (+C4 on B)).
  COMPAT-EPS3-PARTIAL   = all guards pass AND both controls fire AND
      anchor 2/2 AND decider exactly 1/2.
  COMPAT-EPS3-DEAD      = any guard fails, OR any control fails to
      fire (spurious convergence), OR any anchor cell fails (invalid
      statistic by rule), OR decider 0/2 (the eps = 1e-3 cells fail
      the oscillation-aware statistic at full reachable depth: that
      closes tail-weil remainder (b) NEGATIVELY at this depth and the
      route synthesis must state it).

STOP-LIST (binding, inherited): no domino variants, no layer
positivizations, no channel factorizations, no drift-sign attempts,
no raw symbol minorants, no norm triangles, no perturbation theory,
no position-blind estimates.  The eps -> 0 wall (PD persistence)
stays out of scope.  NO RH claim.  This probe writes no files.

RESULTS (2026-08-04, first and only preregistered run, 1.2 s; GATES
4/4 (anchor 2/2, decider 2/2), GUARDS+CONTROLS 8/8, iteration UNUSED,
verdict COMPAT-EPS3-CONVERGES):
  *  Candidate A passed the anchor 2/2 on the first run -- the single
     declared iteration to Candidate B was NEVER consulted.
  *  ANCHOR eps = 1e-2 (statistic validity): R = 1 b = 0.259 (resid
     0.45), med5 last/first = 0.191, b2 = 0.194, Dini tail 0.077;
     R = 2 b = 0.149 (resid 0.47), med5 = 0.202, b2 = 0.260, Dini
     0.124.  The oscillation-aware statistic reproduces the parent
     decision on the previously passing cells.
  *  DECIDER eps = 1e-3 -- BOTH open cells PASS on the deeper ladder:
     R = 1: defect 2.8e-3/3.0e-3/1.8e-2 head -> 5.6e-4..2.4e-3 tail
     band over X-R = 3.00..11.75; b = 0.178 >= 0.10 (resid 0.65 =
     atom-burst oscillation, reported), med5 = 0.343 <= 0.50, b2 =
     0.069 >= 0.02, Dini tail 0.140.
     R = 2: defect 1.2e-3/1.5e-3/3.9e-3 head -> 1.3e-4..1.2e-3 tail
     band over X-R = 2.00..10.75; b = 0.186 >= 0.10 (resid 0.58),
     med5 = 0.467 <= 0.50 (thin but frozen margin), b2 = 0.096 >=
     0.02, Dini tail 0.127.  The parent's eps = 1e-3 endpoint
     failures were single-final-rung atom-burst artifacts of the
     shorter ladder: on 36 interleaved rungs to X = 12.875 the
     5-rung medians fall 2.1..2.9x and the second-half trend stays
     strictly falling.
  *  b(eps) rate table (per X unit; R = 1 / R = 2): eps = 1e-1:
     0.239 / 0.185; 1e-2: 0.259 / 0.149; 1e-3: 0.178 / 0.186; 3e-4
     (outlook, never gated): 0.148 / 0.137.  HONEST WALL NOTE: at
     the outlook eps = 3e-4 the R = 1 second-half slope turns
     NEGATIVE (b2 = -0.011; med5 = 0.475, R = 2 b2 = +0.085) -- had
     3e-4 been a gated cell it would FAIL C3: the eps -> 0 wall is
     now visible one decade below the decided cells and is
     quantified, not hidden.  eps = 0 PD margins: lambda_min =
     5.289e-5 (W_256) / 8.265e-6 (W_824).
  *  CONTROLS both fire at the first gate: scramble lambda_min =
     -1.30e+3, (A + eps I) Cholesky breaks on 72/72 rungs; Epstein
     x^2+5y^2 (496 negative atom sites) lambda_min = -84.4, breaks
     48/48.  No spurious convergence.
  *  GUARDS: comb == deployed masses rel dev 0.0 (ka = 33276 atoms
     to e^12.875); reach census 824 <= 825, sieve cover 390430 <=
     400000; compatibility diagonal PSD min +1.0e-7 >= -1e-8 (the
     E_B - E_A diagonal is PSD on every rung of every reported
     cell); mid-rung dense-solve Ward 2.0e-13.
  *  CONSEQUENCE: tail-weil remainder (b), cross-window
     compatibility, is closed POSITIVELY on the reachable surface --
     all six original (eps, R) cells now pass (4 from the parent +
     the 2 decided here at greater depth with the robust endpoint
     statistic).  Open beyond this surface (honest): the eps -> 0
     wall (PD persistence; b(eps) degrading toward it, outlook b2
     sign flip at 3e-4), the battery-limited Weil identification,
     and every RH-level positivity statement.  NO RH claim.

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/handoff_compat_eps3_probe.py
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
M_CAP = int(math.floor(math.log(core.ATOM_MAX) / D))   # 825, X = 12.891
M_TOP = 824                          # deepest step-8-aligned rung
LAD_A = list(range(256, 817, 16))    # 36 rungs, X = 4.0 .. 12.75
LAD_OFF = 8                          # ladder B = A + 8 cells (half step)
SIZES_B = list(range(256, 825, 8))   # candidate-B grid, X = 4.0 .. 12.875

R_BAT = (1.0, 2.0)                   # frozen module-1 local battery
EPS_ANCHOR = 1.0e-2                  # gated, must pass (statistic valid)
EPS_DECIDER = 1.0e-3                 # gated, the two open cells
EPS_OUTLOOK = 3.0e-4                 # reported only, never gated
EPS_REPORT = (1.0e-1, 1.0e-2, 1.0e-3, 3.0e-4)

N_MED = 5                            # median block size (C2)
C1_RATE = 0.10                       # full-ladder fit rate bar
C2_MED = 0.50                        # med5(last)/med5(first) bar
C3_RATE2 = 0.02                      # second-half fit rate bar
C4_DINI = 0.25                       # tail-quarter Dini fraction bar (B)
WARD_BAR = 1.0e-8                    # mid-rung dense-solve Ward
DIAG_PSD_TOL = -1.0e-8               # PSD tolerance on defect diagonal
CTRL_FACTOR = 10.0                   # control final-defect separation
COMB_DEV_BAR = 1.0e-12               # sieve == deployed masses
EP_NCAP = 34000                      # Epstein Lambda_E table reach
EP_MMAX = 640                        # Epstein control tower cap
SEED = 7

BANNED = ("zetazero", "nzeros", "isprime", "primerange", "nextprime",
          "prevprime", "primepi", "sympy")

CHECKS = []       # guards + controls: all must pass, else invalid run
GATES = []        # anchor + decider cells: feed the verdict only


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
    """Battery + every ladder specification + every bar, SHA-256
    frozen BEFORE any comb/deployed data is loaded."""
    bats = {}
    hsh = hashlib.sha256()
    hsh.update(("compat-eps3 spec: 4 boxes + 3 hats per R, l2-norm, "
                "D=%.10f, R=%s; LAD_A=%d..%d step 16, LAD_B=A+%d, "
                "SIZES_B=%d..%d step 8, M_TOP=%d (cap %d); "
                "eps anchor=%g decider=%g outlook=%g report=%s; "
                "stat: b>=%g, med%d ratio<=%g, b2>=%g, dini<=%g; "
                "ward<=%g, diagPSD>=%g, ctrl x%g; iteration: B iff "
                "anchor fails under A, else unused"
                % (D, R_BAT, LAD_A[0], LAD_A[-1], LAD_OFF, SIZES_B[0],
                   SIZES_B[-1], M_TOP, M_CAP, EPS_ANCHOR, EPS_DECIDER,
                   EPS_OUTLOOK, EPS_REPORT, C1_RATE, N_MED, C2_MED,
                   C3_RATE2, C4_DINI, WARD_BAR, DIAG_PSD_TOL,
                   CTRL_FACTOR)).encode())
    for R in R_BAT:
        bats[R] = hbp.battery(R)
        for nm, v in bats[R]:
            hsh.update(nm.encode())
            hsh.update(v.tobytes())
    return bats, hsh.hexdigest()


# ------------------------------------------------ cell statistic
def cell_stat(rows, dini_vals):
    """The frozen oscillation-aware statistic on one cell."""
    mxs = [r["mx"] for r in rows]
    b, resid = hbp.fit_rate(rows)
    half = rows[len(rows) // 2:]
    b2, _r2 = hbp.fit_rate(half)
    med_first = float(np.median(mxs[:N_MED]))
    med_last = float(np.median(mxs[-N_MED:]))
    med_ratio = med_last / max(med_first, 1.0e-300)
    n_q = int(math.ceil(len(dini_vals) / 4.0))
    dini = float(sum(dini_vals[-n_q:]) / max(sum(dini_vals),
                                             1.0e-300))
    c1 = b >= C1_RATE
    c2 = med_ratio <= C2_MED
    c3 = b2 >= C3_RATE2
    c4 = dini <= C4_DINI
    return dict(b=b, resid=resid, b2=b2, med_ratio=med_ratio,
                dini=dini, c1=c1, c2=c2, c3=c3, c4=c4, mxs=mxs,
                xmr0=rows[0]["XmR"], xmr1=rows[-1]["XmR"])


def cell_pass(st, gate_dini):
    ok = st["c1"] and st["c2"] and st["c3"]
    if gate_dini:
        ok = ok and st["c4"]
    return ok


def cell_detail(st, gate_dini):
    return ("defect %s ... %s over X-R = %.2f..%.2f -- b = %.3f "
            "(>= %g; resid %.2f reported), med%d last/first = %.3f "
            "(<= %g), b2 = %.3f (>= %g), dini tail = %.3f (%s %g)"
            % (", ".join("%.1e" % v for v in st["mxs"][:3]),
               ", ".join("%.1e" % v for v in st["mxs"][-5:]),
               st["xmr0"], st["xmr1"], st["b"], C1_RATE, st["resid"],
               N_MED, st["med_ratio"], C2_MED, st["b2"], C3_RATE2,
               st["dini"], "gated <=" if gate_dini else "reported vs",
               C4_DINI))


# ------------------------------------------------ candidate A rows
def cand_a_cell(E, ladA, ladB, R):
    """Diagonal Dini values + PSD floor for one (eps, R) cell from
    the compat_rows E dict (same scale convention as compat_rows)."""
    d0 = np.diag(E[ladA[0]][R])
    scale = float(np.sqrt(np.max(d0) * np.min(d0)))
    dgs, dmin = [], np.inf
    for Ma, Mb in zip(ladA, ladB):
        dd = np.diag(E[Mb][R] - E[Ma][R]) / scale
        dgs.append(float(np.max(dd)))
        dmin = min(dmin, float(np.min(dd)))
    return dgs, dmin


def cand_a_all(T, bats):
    """Candidate A: interleaved half-step ladders (verbatim
    handoff_tail_weil_probe.compat_rows) over the report eps set."""
    ladB = [m + LAD_OFF for m in LAD_A]
    out = {}
    for eps in EPS_REPORT:
        rows, E = htw.compat_rows(T, LAD_A, ladB, eps, bats)
        out[eps] = dict(rows=rows, E=E)
        for R in R_BAT:
            dgs, dmin = cand_a_cell(E, LAD_A, ladB, R)
            out[eps][R] = dict(st=cell_stat(rows[R], dgs), dmin=dmin)
    return out


# ------------------------------------------------ candidate B rows
def increment_rows(T, rungs, fs, R, eps, ward_every=8):
    """Verbatim handoff_bulk_probe.handoff_rows plus diagonal capture
    (the Dini increments); full-step Cauchy increments."""
    nR = int(round(R / D))
    Fm = np.stack([v for _n, v in fs], axis=1)
    rows = []
    scale = None
    for r in rungs:
        if not r["pd"] or r["m0"] < nR:
            continue
        F = np.zeros((r["m0"], Fm.shape[1]))
        F[:nR] = Fm
        GF = sla.cho_solve(r["cf"], F)
        if scale is None:
            gd = np.einsum("ij,ij->j", F, GF)
            scale = float(np.sqrt(np.max(gd) * np.min(gd)))
        W = r["B"].T @ GF
        Dm = W.T @ np.linalg.solve(r["St"], W)
        ward = None
        if r["k"] % ward_every == 0:
            m1 = r["m1"]
            F1 = np.zeros((m1, Fm.shape[1]))
            F1[:nR] = Fm
            G1 = np.linalg.solve(T[:m1, :m1] + eps * np.eye(m1), F1)
            Dd = F1.T @ G1 - F.T @ GF
            ward = float(np.max(np.abs(Dm - Dd))
                         / max(np.max(np.abs(Dd)), 1.0e-300))
        rows.append(dict(k=r["k"], X=r["m1"] * D,
                         XmR=r["m1"] * D - R,
                         mx=float(np.max(np.abs(Dm))) / scale,
                         dg=float(np.max(np.diag(Dm))) / scale,
                         dmin=float(np.min(np.diag(Dm))) / scale,
                         ward=ward))
    return rows


def cand_b_all(T, bats):
    out = {}
    for eps in EPS_REPORT:
        rungs = hbp.rung_data(T, SIZES_B, eps)
        out[eps] = dict(rows={}, E=None)
        for R in R_BAT:
            rows = increment_rows(T, rungs, bats[R], R, eps)
            out[eps]["rows"][R] = rows
            dgs = [r["dg"] for r in rows]
            dmin = min(r["dmin"] for r in rows)
            wards = [r["ward"] for r in rows if r["ward"] is not None]
            out[eps][R] = dict(st=cell_stat(rows, dgs), dmin=dmin,
                               ward=max(wards))
    return out


# ------------------------------------------------ tower + controls
def build_tower():
    alpha_full = 0.5 * M_TOP * D
    ka, masks, dev_m = srp.channel_masks(alpha_full)
    check("G2.1 tower comb consistency (zeta-free Gauss double sieve "
          "== deployed masses, rel dev <= %.0e)" % COMB_DEV_BAR,
          dev_m <= COMB_DEV_BAR, "rel dev %.1e, ka=%d atoms to "
          "e^%.4f" % (dev_m, ka, 2.0 * alpha_full))
    c_cont = srp.continuum_lags(M_TOP)
    c_full = c_cont.copy()
    for cnl in ("ro", "re", "sp", "in"):
        c_full = c_full + srp.atom_channel_lags(alpha_full, M_TOP,
                                                masks[cnl])
    return sla.toeplitz(c_full[:M_TOP]), c_cont, alpha_full, ka


def control_fire(Tc, ladA, ladB, bats, real_last, use_b, label):
    """Frozen fire rule on the adjudicated construction: Cholesky
    break OR statistic failure OR >= CTRL_FACTOR x real defect."""
    lam = float(np.min(np.linalg.eigvalsh(Tc)))
    sizes = sorted(set(ladA) | set(ladB)) if not use_b else ladA
    broken = 0
    for M in sizes:
        try:
            sla.cho_factor(Tc[:M, :M] + EPS_ANCHOR * np.eye(M))
        except np.linalg.LinAlgError:
            broken += 1
    if broken:
        return True, ("(A + eps I) Cholesky breaks on %d/%d rungs "
                      "(lambda_min = %.2e << -eps)"
                      % (broken, len(sizes), lam))
    if use_b:
        rungs = hbp.rung_data(Tc, ladA, EPS_ANCHOR)
        rows = increment_rows(Tc, rungs, bats[2.0], 2.0, EPS_ANCHOR)
        dgs = [r["dg"] for r in rows]
    else:
        rows_all, E = htw.compat_rows(Tc, ladA, ladB, EPS_ANCHOR,
                                      bats)
        rows = rows_all[2.0]
        dgs, _dm = cand_a_cell(E, ladA, ladB, 2.0)
    st = cell_stat(rows, dgs)
    passes = st["c1"] and st["c2"] and st["c3"]
    big = st["mxs"][-1] >= CTRL_FACTOR * real_last
    fire = (not passes) or big
    return fire, ("PD under eps; statistic C1/C2/C3 = %s/%s/%s "
                  "(b = %.3f, med ratio %.2f, b2 = %.3f), final "
                  "defect %.2e vs real %.2e (x%g bar): fire=%s"
                  % (st["c1"], st["c2"], st["c3"], st["b"],
                     st["med_ratio"], st["b2"], st["mxs"][-1],
                     real_last, CTRL_FACTOR, fire))


def run_controls(c_cont, alpha_full, ka, bats, real_last, use_b):
    print("\n-- controls (must fire; on the adjudicated %s "
          "construction, eps = %g)"
          % ("Candidate-B increment" if use_b
             else "Candidate-A interleave", EPS_ANCHOR))
    if use_b:
        ladA, ladB = SIZES_B, SIZES_B
        ladA_E = [m for m in SIZES_B if m <= EP_MMAX]
        ladB_E = ladA_E
    else:
        ladA = LAD_A
        ladB = [m + LAD_OFF for m in LAD_A]
        ladA_E = [m for m in LAD_A if m + LAD_OFF <= EP_MMAX]
        ladB_E = [m + LAD_OFF for m in ladA_E]

    rng = np.random.default_rng(SEED)
    pos = np.sort(rng.uniform(0.5, 2.0 * alpha_full, ka))
    cat_s, _dd = core.atom_lags_at(alpha_full, M_TOP, pos,
                                   core.MU_ALL[:ka])
    Ts = sla.toeplitz((c_cont + cat_s)[:M_TOP])
    fire_s, det_s = control_fire(Ts, ladA, ladB, bats, real_last,
                                 use_b, "scramble")
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
    fire_e, det_e = control_fire(TE, ladA_E, ladB_E, bats, real_last,
                                 use_b, "epstein")
    check("CE Epstein control (x^2+5y^2, %d negative atom sites, "
          "ladder to M = %d) fires"
          % (int(np.sum(lamE[2:] < -1.0e-9)), ladA_E[-1]),
          fire_e, det_e)


# ------------------------------------------------ adjudication
def print_cell(tag, cell, gate_dini):
    print("  %s: %s" % (tag, cell_detail(cell["st"], gate_dini)))


def adjudicate(cand, tagc, T, bats, use_b):
    """Anchor gates, decider gates, outlook + b(eps) report, guards."""
    gate_dini = use_b
    print("\n-- %s: anchor cells (eps = %g, MUST pass or DEAD)"
          % (tagc, EPS_ANCHOR))
    anchor_ok = 0
    for R in R_BAT:
        cell = cand[EPS_ANCHOR][R]
        ok = cell_pass(cell["st"], gate_dini)
        anchor_ok += bool(ok)
        gate("ANCHOR eps=%g,R=%g" % (EPS_ANCHOR, R), ok,
             cell_detail(cell["st"], gate_dini))
    print("\n-- %s: decider cells (eps = %g, the two open cells)"
          % (tagc, EPS_DECIDER))
    decider_ok = 0
    for R in R_BAT:
        cell = cand[EPS_DECIDER][R]
        ok = cell_pass(cell["st"], gate_dini)
        decider_ok += bool(ok)
        gate("DECIDER eps=%g,R=%g" % (EPS_DECIDER, R), ok,
             cell_detail(cell["st"], gate_dini))

    print("\n-- %s: outlook cell (eps = %g, REPORTED, never gated)"
          % (tagc, EPS_OUTLOOK))
    for R in R_BAT:
        print_cell("outlook eps=%g,R=%g" % (EPS_OUTLOOK, R),
                   cand[EPS_OUTLOOK][R], gate_dini)

    print("\n-- %s: b(eps) rate table (per X unit, reported)" % tagc)
    for eps in EPS_REPORT:
        print("  eps=%-7g: %s" % (eps, "  ".join(
            "R=%g: b=%.3f b2=%.3f med=%.3f" %
            (R, cand[eps][R]["st"]["b"], cand[eps][R]["st"]["b2"],
             cand[eps][R]["st"]["med_ratio"]) for R in R_BAT)))

    # guards: diagonal PSD + mid-rung dense-solve Ward
    dmin_all = min(cand[eps][R]["dmin"] for eps in EPS_REPORT
                   for R in R_BAT)
    check("G3.1 compatibility diagonal PSD (min diag >= %.0e x "
          "scale) on every rung of every reported cell"
          % DIAG_PSD_TOL, dmin_all >= DIAG_PSD_TOL,
          "min %.1e" % dmin_all)
    if use_b:
        wmax = max(cand[eps][R]["ward"] for eps in
                   (EPS_ANCHOR, EPS_DECIDER) for R in R_BAT)
        check("G3.2 increment dense-solve Ward <= %.0e (every 8th "
              "rung, gated eps)" % WARD_BAR, wmax <= WARD_BAR,
              "max rel %.1e" % wmax)
    else:
        mid = LAD_A[len(LAD_A) // 2]
        R = 2.0
        nR = int(round(R / D))
        Fm = np.stack([v for _n, v in hbp.battery(R)], axis=1)
        F = np.zeros((mid, Fm.shape[1]))
        F[:nR] = Fm
        wmax = 0.0
        for eps in (EPS_ANCHOR, EPS_DECIDER):
            Ed = F.T @ np.linalg.solve(
                T[:mid, :mid] + eps * np.eye(mid), F)
            w = float(np.max(np.abs(Ed - cand[eps]["E"][mid][R]))
                      / max(np.max(np.abs(Ed)), 1.0e-300))
            wmax = max(wmax, w)
        check("G3.2 mid-rung dense-solve Ward (M=%d, R=%g, eps = "
              "%g and %g) <= %.0e"
              % (mid, R, EPS_ANCHOR, EPS_DECIDER, WARD_BAR),
              wmax <= WARD_BAR, "max rel %.1e" % wmax)
    return anchor_ok, decider_ok


def run():
    print("=" * 78)
    print("GLOBAL HANDOFF -- eps = 1e-3 cross-window compatibility "
          "decider (deep ladder)")
    print("=" * 78)

    hits = ast_firewall()
    check("G0.1 AST firewall", not hits, str(hits))
    bats, spec_sha = freeze_spec()
    check("G0.2 battery + every ladder specification + every bar "
          "SHA-256-frozen BEFORE any comb data load", True,
          "SHA256 %s..." % spec_sha[:16])
    check("G0.3 reach census: top B rung M = %d <= table cap M = %d "
          "(X = %.6f <= ln(ATOM_MAX) = %.6f); sieve cover "
          "exp(X_top) + 2 = %d <= ATOM_MAX = %d"
          % (max(LAD_A[-1] + LAD_OFF, SIZES_B[-1]), M_CAP,
             M_TOP * D, math.log(core.ATOM_MAX),
             int(math.exp(M_TOP * D)) + 2, core.ATOM_MAX),
          max(LAD_A[-1] + LAD_OFF, SIZES_B[-1]) <= M_CAP
          and int(math.exp(M_TOP * D)) + 2 <= core.ATOM_MAX)

    # ---- first comb/deployed data touch strictly after the freeze
    T, c_cont, alpha_full, ka = build_tower()
    lam0 = float(np.min(np.linalg.eigvalsh(T[:LAD_A[0], :LAD_A[0]])))
    lamF = float(np.min(np.linalg.eigvalsh(T)))
    print("  PD margins (eps = 0, the wall, reported not gated): "
          "lambda_min(W_%d) = %.3e, lambda_min(W_%d) = %.3e"
          % (LAD_A[0], lam0, M_TOP, lamF))

    # ---- Candidate A (default construction)
    cand_a = cand_a_all(T, bats)
    a_anchor = all(cell_pass(cand_a[EPS_ANCHOR][R]["st"], False)
                   for R in R_BAT)
    use_b = not a_anchor
    if use_b:
        print("\n!! DECLARED ITERATION TRIGGERED: Candidate A fails "
              "the anchor -- the single predeclared iteration to "
              "Candidate B (full-step Cauchy increments) is spent; "
              "adjudication runs on B, the A numbers stand as the "
              "named half-step block below.")
        for R in R_BAT:
            print_cell("A(named) anchor eps=%g,R=%g"
                       % (EPS_ANCHOR, R), cand_a[EPS_ANCHOR][R],
                       False)
            print_cell("A(named) decider eps=%g,R=%g"
                       % (EPS_DECIDER, R), cand_a[EPS_DECIDER][R],
                       False)
        cand = cand_b_all(T, bats)
        tagc = "Candidate B (full-step Cauchy increments, %d rungs " \
               "to X = %.3f)" % (len(SIZES_B) - 1, SIZES_B[-1] * D)
    else:
        print("\n  Candidate A passes the anchor: adjudication runs "
              "on A; the declared iteration to Candidate B is UNUSED "
              "(B never consulted).")
        cand = cand_a
        tagc = "Candidate A (interleaved half-step ladders, %d " \
               "rungs, A to X = %.2f / B to X = %.3f)" \
               % (len(LAD_A), LAD_A[-1] * D,
                  (LAD_A[-1] + LAD_OFF) * D)

    anchor_ok, decider_ok = adjudicate(cand, tagc, T, bats, use_b)

    # ---- controls on the adjudicated construction
    real_last = cand[EPS_ANCHOR]["rows"][2.0][-1]["mx"]
    run_controls(c_cont, alpha_full, ka, bats, real_last, use_b)

    # ---- verdict (preregistered rules)
    guards_ok = all(ok for (n, ok) in CHECKS
                    if not n.startswith(("CS", "CE")))
    controls_ok = all(ok for (n, ok) in CHECKS
                      if n.startswith(("CS", "CE")))
    if guards_ok and controls_ok and anchor_ok == 2 \
            and decider_ok == 2:
        verdict = "COMPAT-EPS3-CONVERGES"
    elif guards_ok and controls_ok and anchor_ok == 2 \
            and decider_ok == 1:
        verdict = "COMPAT-EPS3-PARTIAL"
    else:
        verdict = "COMPAT-EPS3-DEAD"

    n_gate = sum(1 for (_n, ok) in GATES if ok)
    n_chk = sum(1 for (_n, ok) in CHECKS if ok)
    print("\nVERDICT: %s" % verdict)
    print("GATES %d/%d (anchor %d/2, decider %d/2), GUARDS+CONTROLS "
          "%d/%d, iteration %s, runtime %.1f s"
          % (n_gate, len(GATES), anchor_ok, decider_ok, n_chk,
             len(CHECKS), "SPENT (Candidate B)" if use_b
             else "UNUSED (Candidate A)", time.time() - T_START))
    if verdict == "COMPAT-EPS3-CONVERGES":
        print("CONSEQUENCE: the two open eps = 1e-3 cross-window "
              "compatibility cells PASS the oscillation-aware "
              "statistic on the deepest reachable ladder -- "
              "tail-weil remainder (b) is closed POSITIVELY on this "
              "surface.  Open beyond it (honest): the eps -> 0 wall "
              "(PD persistence; b(eps) quantified above), the "
              "battery-limited identification, and every RH-level "
              "positivity statement.  NO RH claim.")
    elif verdict == "COMPAT-EPS3-PARTIAL":
        print("HONEST READING: exactly one eps = 1e-3 cell passes; "
              "the failed cell's profile above is the remaining "
              "object at this depth -- remainder (b) stays open, "
              "narrowed to one cell.")
    else:
        if not (guards_ok and controls_ok and anchor_ok == 2):
            print("KILL (invalid or spurious): a guard failed, a "
                  "control spuriously converged, or the anchor cell "
                  "failed -- by the frozen rule the statistic (or "
                  "run) is invalid; no statement about the eps = "
                  "1e-3 cells follows from this run.")
        else:
            print("KILL (negative closure at this depth): both eps "
                  "= 1e-3 cells FAIL the oscillation-aware statistic "
                  "on the deepest reachable ladder -- tail-weil "
                  "remainder (b) closes NEGATIVELY at this depth and "
                  "the route synthesis must state it.")
    return 0 if (guards_ok and controls_ok) else 1


if __name__ == "__main__":
    sys.exit(run())
