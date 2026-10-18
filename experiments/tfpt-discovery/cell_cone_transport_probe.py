#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""cell_cone_transport_probe -- PRIME.CELLCONE.TRANSPORT.01
(EXPLORATION ONLY, experiments/; work package D of the 2026-08-07
v5.4 strategy: the cell-wise Lorentz cone transport).

THE CORPUS NEGATIVES THIS BUILDS ON (cited, not re-adjudicated):
  * v758 keystone: the assembled certificate [continuum root (+)
    Kraus] is NOT mountable -- arch+pole PSD at no stage, the rescue
    is strictly CELL-ORDERED; additive continuum+atoms is the wrong
    granularity; the corrected target shape is the cell-wise cascade
    factorization (PRIME.PD.PERSISTENCE.01).
  * v773 (COCYCLE-DOMAIN-ONLY): the exact Moebius/Redheffer cell
    cocycle preserves the Nevanlinna/Stieltjes domain (zero breaches,
    PD cell blocks, monotone Loewner flow) but its renormalized
    objects do not converge -- structure without limit.
  * simpler_schur_recursion / layer kills: single prime layers are
    provably not positive; positivity is not additive over layers.
  * v807 (LORENTZ-COORDS-REVEAL + NULLSELECTOR-ALGEBRAIC): the
    signature-(1,2) determinant form q(t,x,y) = t^2 - x^2 - y^2 =
    4 det on the 2x2 lock blocks; the compiler vector (5,-3,4) =
    (g_car, -N_fam, |mu4|) is EXACTLY null, M(5,-3,4) =
    2 (1,2)^T (1,2); the deployed locking slope r is strictly
    monotone in alpha toward 2 (the ray edge hint).
  * v818/v829 + margin_law_probe (2026-08-07): Ah = B - S with
    margin tau = lambda_min(Ah) > 0 on all deployed rungs; tau_pnt =
    lambda_min(B - S_pnt) with the explicit zero-free density model
    (v583 convention U0 = 2 ln(-C_TH/4), GRID_PER_D = 4); certified
    envelope e1 = (tau/tau_pnt) h^{3/2} >= 4.335 on all rungs.

THE CONSTRUCTION (frozen): COMPLETED CELLS.  cell_n = (the prime-
power atom kick at n) + (its associated continuum-and-pole
increment).  In the deployed 2x2 lock coordinates the atom kick is
-lam_n Xhat_n (shipped reads) and the continuum/pole increment is
Chat_n = the S_pnt increment over the interval I_n assigned to atom
n (the growing e^{u/2} channel IS the pole channel in this frame --
the atom_pole_abel identification, cited).  TWO PREDECLARED GROUPING
RULES decide the intervals (the relational assignment):
  G1 (Abel/Stieltjes pairing, tail strand): atom j owns the
     continuum interval (u_{j-1}, u_j] ending AT its own position
     (u_0 := U0); the last atom additionally absorbs the tail
     (u_{K-1}, 2 alpha] -- the left Stieltjes pairing of dpsi with
     dx, cell = one increment of dE.
  G2 (relational mu*log mass matching): atom j owns the interval
     (v_{j-1}, v_j] where the cumulative continuum mass equals the
     cumulative atom mass, e^{v_j/2} = e^{U0/2} +
     (1/2) sum_{i<=j} Lambda(n_i)/sqrt(n_i), capped at 2 alpha; the
     remaining tail goes to the last cell.  Each prime power absorbs
     EXACTLY its own mass of smooth density (psi-inverse pairing --
     the multiplicative weight decides the continuum share).
Both rules PARTITION [U0, 2 alpha], so the completed flow
     A_k = Ah_pnt + sum_{j<=k} (Chat_j - lam_j Xhat_j)
telescopes EXACTLY from A_0 = Ah_pnt = B - S_pnt (the continuum
transversal) to A_K = B - S = Ah (the certified margin object) --
gated per rung (WARD_REL).  At stage k the state is exactly the
HYBRID window: arithmetic atoms below the moving horizon, smooth
density above it -- the completed window at every stage.

THE CELL MAP (frozen): each completed cell acts as the canonical
congruence update A_{k+1} = M_k^T A_k M_k with
     M_k = A_k^{-1/2} (I + Atil_k)^{1/2} A_k^{1/2},
     Atil_k = A_k^{-1/2} (Chat_k - lam_k Xhat_k) A_k^{-1/2},
which EXISTS iff I + Atil_k > 0 iff A_{k+1} > 0 (cone preservation
== admissibility of the Moebius/Redheffer square root).  Its induced
3x3 Lorentz action Phi_k on u = L(A) = (a11+a22, a11-a22, 2 a12)
satisfies the EXACT identity
     Phi_k^T J Phi_k = c_k J,   c_k = det(M_k)^2
                              = det(A_{k+1}) / det(A_k),
(J = diag(1,-1,-1); q(L(A)) = 4 det A) -- spot-gated numerically
(PHI_REL).  HONESTY, stated up front: because J is indefinite, the
literal matrix inequality Phi^T J Phi <= J holds ONLY at c = 1
(lambda_max(Phi^T J Phi - J) = max(c-1, 1-c) >= 0 for any c != 1);
the frozen operational J-CONTRACTIVITY reading is therefore the
ON-CONE one -- q(Phi v) <= q(v) for all v in the future cone L+,
which for the congruence map is EXACTLY c_k <= 1.  The frozen
per-cell J-DEFECT is jdef_k = c_k - 1 = det(A_{k+1})/det(A_k) - 1;
the literal lambda_max(Phi^T J Phi - J) is REPORTED alongside on the
spot-check cells with the identity named.

THE TEST (frozen; bars in FROZEN_SPEC below, sha256-hashed and
printed before any measurement):
  (a) per-cell: CONE PRESERVATION lambda_min(A_k) > 0 at every cell
      (incl. the base) and the J-defect census jdef_k <= JDEF_TOL;
  (b) the CASCADE: the composed flow stays in the future cone per
      rung; the distance to the null direction (dnull =
      q/(t^2+x^2+y^2)) and the angle to the compiler ray (5,-3,4)
      along the path and across the alpha-ordered ladder (does the
      ray appear as the asymptotic edge -- the locking-slope-2
      hint); the ray clause is the named sub-verdict
      RAY-EDGE-CONFIRMED / RAY-EDGE-OPEN and does NOT move the cone
      enum;
  (c) the INCOMPLETE contrast: the SAME flow with naive cells
      (atom kick alone, no continuum piece, same base Ah_pnt) must
      FAIL (cone exit) -- the corpus's additive-granularity negative
      reproduced as a flow; the ward that completion is load-bearing
      (its firing is mass-forced -- stated, not hidden: the
      information of this probe lives in the completed flow's path,
      the contrast is the bookkeeping ward).
CONTROLS (frozen fire rules in FROZEN_SPEC):
  C1 order swap (cells applied in decreasing u; endpoint identical
     by additivity -- checked): MEASURED, not gated (does order
     matter for the path?).
  C2 equal-weight scramble (same positions, every atom mass replaced
     by the ladder-mean mass, total matched; G1 pairing): must
     break.
  C3 Epstein x^2 + 5 y^2 comb (mass-matched, same completion, G1):
     must break; the u-positions of the breaks are censused (the
     Euler-product-sensitive cells).
  C4 removal of the continuum piece == (c).
  C5 wrong pole normalization (continuum density x WRONG_FAC = 2,
     self-consistent base B - 2 S_pnt; endpoint still telescopes to
     Ah): must break.
VERDICT ENUM (frozen, decision order):
  INVALID            -- any ward fails (no structural claim, exit 1).
  CELLS-PRESERVE-CONE -- BOTH groupings: cone preserved at EVERY
     cell on EVERY tested rung AND zero J-defect violations
     (jdef <= JDEF_TOL everywhere) AND the incomplete contrast
     breaks at >= MB_FRAC of rungs AND all must-break controls fire.
     The universal-cell-theorem candidate; the verdict then states
     exactly what the infinite statement would need.
  CONE-BROKEN        -- for BOTH groupings the completed flow exits
     the cone on >= 0.5 of the tested rungs (the completion rules do
     not produce admissible cells) -- typed which grouping failed
     where.
  CONE-PARTIAL       -- everything in between: some cells violate
     (typed census: p = 2?, prime powers k >= 2?, p mod 4,
     u-position decile), or a must-break control did not fire
     (control surprise, typed).
NO RH claim anywhere.  Cone preservation of a finite flow on 67
rungs is a FINITE measurement; nothing here bounds the infinite
ladder.  This probe writes no files; nothing outside experiments/
is touched; no ledger row, no paper edit.

FIREWALL: v563 imported READ-ONLY; mpmath used for the zero-free
constant C_TH = -2 zeta'(1/2)/zeta(1/2) ONLY; no zeta zero is read
anywhere (AST-checked); own spf sieve for the census typing (no
sympy.ntheory); NO RNG anywhere (all controls deterministic);
runtime cap 1800 s predeclared.

DECLARED IMPLEMENTATION CORRECTIONS (run 1 -> final run, 2026-08-07;
house disclosure precedent -- no bar, tolerance, grouping rule or
verdict enum changed; the FROZEN_SPEC hash is unchanged):
  (1) phi_spot PD guard: run 1 crashed at the spot gate because the
      completed flow's state at a spot cell is NOT PD (exactly the
      cone-exit event the census measures); the helper now returns
      None for non-PD states instead of inverting a singular root.
  (2) verdict validity logic: run 1's code wrongly folded the
      control-fire checks into the INVALID clause; the frozen spec
      text says INVALID only on WARD failure (S0.AST, S1.REF,
      S1.ENV, S1.TEL, S1.PHI) or runtime -- implemented as frozen.
      Controls/contrast remain gates for CELLS-PRESERVE-CONE only.
  (3) report-only additions: per-rung out-of-cone path census
      (number of out-of-cone states, first/last exit position,
      longest out-run) to type WHERE the completion fails, and the
      Epstein control surprise named in the verdict.
  Run-1 numbers carried honestly: wards all green (tau refs rel
  <= 6e-8, min e1 4.8546, telescoping 3.4e-15); BOTH groupings exit
  the cone on 67/67 rungs (first exit at cell 0 = the n = 2 atom);
  J-census G1 49.6% / G2 12.1% expanding cells; contrast fires
  67/67; equal-weight and wrong-norm fire 14/14; Epstein does NOT
  fire (0/14 exits, dnull 3.5x < 10x bar) -- the control surprise.

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/cell_cone_transport_probe.py
"""

import ast
import hashlib
import inspect
import math
import os
import sys
import time

import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
_VERIFY = os.path.abspath(os.path.join(_HERE, "..", "..",
                                       "verification"))
sys.path.insert(0, _HERE)
sys.path.insert(0, _VERIFY)

import v563_paper2_readouts as core        # noqa: E402  (READ-ONLY)
from mpmath import mp, zeta, diff as mpdiff  # noqa: E402 (VALUES only)

FROZEN_SPEC = """\
PRIME.CELLCONE.TRANSPORT.01 spec v1 (2026-08-07, frozen before the
run).  Ladder: frame_a_zones minus h = 1292 (anomalous, v586) minus
incomplete combs (e^{2 alpha} > ATOM_MAX); full per-cell detail on
the 3 smallest-h rungs; controls on the stride-5 subset.  Objects:
Ah = B - S (shipped), tau = eig2_min(Ah); continuum model = v818
convention (U0 = 2 ln(-C_TH/4), C_TH = -2 zeta'(1/2)/zeta(1/2),
GRID_PER_D = 4, grid umax = 2 alpha + 1e-9, cumulative evaluated at
2 alpha); tau_pnt = eig2_min(B - S_pnt).  Completed flow: A_0 =
B - S_pnt; A_k = A_0 + sum_{j<=k} (Chat_j - lam_j Xhat_j); grouping
G1 = left Stieltjes intervals (U0, u_1], (u_1, u_2], ..., last cell
absorbs (u_{K-1}, 2 alpha]; G2 = mass-matched intervals e^{v_j/2} =
e^{U0/2} + 0.5 cumsum(mm)_j capped at 2 alpha, tail to last cell.
WARDS (all must pass; else INVALID): tau refs kz 9/12/13 =
5.984165e-4 / 4.351189e-4 / 5.637632e-4 rel <= 1e-4; envelope
e1 = (tau/tau_pnt) h^{3/2} >= 4.335*0.999 on ALL rungs; telescoping
|A_K - Ah|_max <= 1e-9 ||Ah||_max and |sum Chat - S_pnt|_max <=
1e-9 ||S_pnt||_max per rung per grouping; Phi spot identity
||Phi^T J Phi - c J||_max <= 1e-8 * max(c,1) and ||Phi L(A_k) -
L(A_{k+1})||max <= 1e-8 ||L(A_{k+1})|| on the spot cells (smallest
rung: cells 0, K/2, K-1, every 500th).  BARS: cone = lambda_min > 0
strictly at every cell incl. base; J-defect jdef_k =
det(A_{k+1})/det(A_k) - 1, violation iff jdef_k > JDEF_TOL = 1e-9;
MB_FRAC = 0.9 (incomplete contrast: fraction of rungs with cone
exit); CTRL_FRAC = 0.5 (controls, stride-5 subset); control fire =
[cone exit on >= CTRL_FRAC of subset rungs] OR [median over subset
of the path max |dnull| >= DNULL_FAC = 10 x the real completed
flow's]; RAY clause: RAY-EDGE-CONFIRMED iff Kendall(alpha, r_end)
>= 0.8 AND Kendall(alpha, angle_end to (5,-3,4)) <= -0.8 across the
ladder (sub-verdict only).  VERDICT (order): INVALID if any ward
fails or runtime > 1800 s; CELLS-PRESERVE-CONE iff both groupings
have zero cone exits and zero J-violations on all rungs AND
contrast >= MB_FRAC AND all must-break controls (C2, C3, C5) fire;
CONE-BROKEN iff both groupings exit the cone on >= 0.5 of rungs;
else CONE-PARTIAL (census typed: p = 2, k >= 2, p mod 4, u/2alpha
decile; control surprises named).  No prediction is frozen for the
per-cell J-census (measured as it falls); the incomplete contrast
is predicted to fire (mass-forced).  NO RH claim; writes nothing.
"""

GRID_PER_D = 4.0
STRIDE = 5
ANOMALOUS_H = 1292
TAU_REFS = {9: 5.984165e-4, 12: 4.351189e-4, 13: 5.637632e-4}
TAU_REF_REL = 1.0e-4
ENV_C = 4.335
ENV_GUARD = 0.999
WARD_REL = 1.0e-9
PHI_REL = 1.0e-8
JDEF_TOL = 1.0e-9
MB_FRAC = 0.9
CTRL_FRAC = 0.5
DNULL_FAC = 10.0
KEN_BAR = 0.8
WRONG_FAC = 2.0
N_DETAIL = 3
RUNTIME_CAP = 1800.0
RAY = np.array([5.0, -3.0, 4.0])
J3 = np.diag([1.0, -1.0, -1.0])
BANNED_IDS = ("zetazero", "nzeros", "primerange", "isprime", "primepi",
              "nextprime", "prevprime", "find_zeros",
              "second_sheet_zero")

mp.dps = 30
C_TH = float(-2 * mpdiff(lambda s: zeta(s), 0.5) / zeta(0.5))
U0 = 2.0 * math.log(-C_TH / 4.0)

CHECKS = []
FAILS = []
T0 = time.time()


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok)))
    if not ok:
        FAILS.append(name.split()[0])
    print("  [%s] %s%s" % ("PASS" if ok else "FAIL", name,
                           ("  -- " + detail) if detail else ""),
          flush=True)


def ast_zero_firewall(src_path):
    with open(src_path, "r", encoding="utf-8") as fh:
        tree = ast.parse(fh.read())
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            f = node.func
            nm = f.attr if isinstance(f, ast.Attribute) else (
                f.id if isinstance(f, ast.Name) else "")
            if nm in BANNED_IDS:
                return False
    return True


def kendall_tau(x, y):
    n = len(x)
    conc = disc = 0
    for i in range(n):
        for j in range(i + 1, n):
            s = (x[j] - x[i]) * (y[j] - y[i])
            if s > 0:
                conc += 1
            elif s < 0:
                disc += 1
    return (conc - disc) / max(n * (n - 1) // 2, 1)


def spf_sieve(nmax):
    """Own smallest-prime-factor sieve (census typing only)."""
    s = np.zeros(nmax + 1, dtype=np.int64)
    for p in range(2, int(math.isqrt(nmax)) + 1):
        if s[p] == 0:
            s[p * p::p] = np.where(s[p * p::p] == 0, p, s[p * p::p])
    for n in range(2, nmax + 1):
        if s[n] == 0:
            s[n] = n
    return s


# ------------------------------------------------- continuum machinery
def pnt_grid(rr):
    """The v818 pnt cell grid: edges + 2x2 spline reads per cell."""
    Mz, D, alpha = rr["M"], rr["D"], rr["alpha"]
    delta = D / GRID_PER_D
    umax = 2.0 * alpha + 1e-9
    n_cells = int(math.ceil((umax - U0) / delta))
    edges = U0 + delta * np.arange(n_cells + 1)
    reads = np.empty((n_cells, 3))
    for j in range(n_cells):
        u_j = 0.5 * (edges[j] + edges[j + 1])
        reads[j, 0] = core.spline_project(rr["W11"], u_j, D, Mz)
        reads[j, 1] = core.spline_project(rr["W22"], u_j, D, Mz)
        reads[j, 2] = core.spline_project(rr["W12"], u_j, D, Mz)
    return edges, reads


def cum_reads(edges, reads, bpts):
    """Exact cumulative continuum 2x2 read (as (n,3) triples) up to
    each breakpoint: full cells by prefix sum, boundary cell by the
    exact clipped mass 2(e^{u/2} - e^{edge/2})."""
    e_half = np.exp(edges / 2.0)
    m_full = 2.0 * (e_half[1:] - e_half[:-1])
    pref = np.vstack([np.zeros(3),
                      np.cumsum(m_full[:, None] * reads, axis=0)])
    b = np.asarray(bpts, float)
    idx = np.clip(np.searchsorted(edges, b, side="right") - 1,
                  0, len(reads) - 1)
    part = 2.0 * (np.exp(b / 2.0) - e_half[idx])
    return pref[idx] + part[:, None] * reads[idx]


def breaks_G1(uu, alpha):
    """Left Stieltjes pairing: cell j ends at u_j; last cell absorbs
    the tail to 2 alpha."""
    b = np.array(uu, float)
    b[-1] = 2.0 * alpha
    return b


def breaks_G2(mm, alpha):
    """Mass-matched (mu*log relational) pairing: e^{v_j/2} = e^{U0/2}
    + 0.5 cumsum(mm)_j, capped at 2 alpha; tail to last cell."""
    v = 2.0 * np.log(math.exp(U0 / 2.0) + 0.5 * np.cumsum(mm))
    v = np.minimum(v, 2.0 * alpha)
    v[-1] = 2.0 * alpha
    return v


def cell_increments(edges, reads, bpts):
    """Chat_j triples for a partition given by breakpoints (b_0 = U0
    implicit): exact, telescoping to the full S_pnt."""
    cum = cum_reads(edges, reads, bpts)
    out = np.empty_like(cum)
    out[0] = cum[0]
    out[1:] = np.diff(cum, axis=0)
    return out


# ------------------------------------------------- the flow engine
def path_stats(A0_tri, deltas):
    """Vectorized path of A_k = A0 + cumsum(deltas); returns per-state
    arrays (K+1 incl. base) of the Lorentz/cone quantities and the
    per-cell J-defects (K)."""
    a11 = A0_tri[0] + np.concatenate([[0.0], np.cumsum(deltas[:, 0])])
    a22 = A0_tri[1] + np.concatenate([[0.0], np.cumsum(deltas[:, 1])])
    a12 = A0_tri[2] + np.concatenate([[0.0], np.cumsum(deltas[:, 2])])
    t = a11 + a22
    x = a11 - a22
    y = 2.0 * a12
    det = a11 * a22 - a12 ** 2
    R = np.hypot(0.5 * x, a12)
    lmin = 0.5 * t - R
    lmax = 0.5 * t + R
    q = t * t - x * x - y * y
    nrm2 = t * t + x * x + y * y
    dnull = q / np.maximum(nrm2, 1e-300)
    uvec = np.stack([t, x, y], axis=1)
    cosr = (uvec @ RAY) / np.maximum(
        np.linalg.norm(uvec, axis=1) * np.linalg.norm(RAY), 1e-300)
    ang = np.degrees(np.arccos(np.clip(cosr, -1.0, 1.0)))
    with np.errstate(divide="ignore", invalid="ignore"):
        jdef = det[1:] / np.where(det[:-1] != 0.0, det[:-1], np.nan) - 1.0
    r_dom = np.where(np.abs(a12) > 1e-300,
                     (lmax - a11) / np.where(a12 != 0.0, a12, 1.0),
                     np.where(a11 >= a22, 0.0, np.inf))
    return dict(a11=a11, a22=a22, a12=a12, t=t, det=det, lmin=lmin,
                lmax=lmax, dnull=dnull, ang=ang, jdef=jdef, r=r_dom)


def flow_summary(ps):
    lmin = ps["lmin"]
    cone_ok = bool(np.all(lmin > 0.0))
    first_exit = int(np.argmax(lmin <= 0.0)) if not cone_ok else -1
    out = lmin <= 0.0
    n_out = int(out.sum())
    last_out = int(len(out) - 1 - np.argmax(out[::-1])) if n_out else -1
    runs = 0
    if n_out:
        d = np.diff(out.astype(int))
        starts = np.where(d == 1)[0]
        runs = len(starts) + (1 if out[0] else 0)
    jd = ps["jdef"]
    valid = np.isfinite(jd)
    nviol = int(np.sum(jd[valid] > JDEF_TOL))
    return dict(cone_ok=cone_ok, first_exit=first_exit,
                n_out=n_out, frac_out=n_out / max(len(out), 1),
                last_out=last_out, n_out_runs=runs,
                min_lmin=float(np.min(lmin)),
                min_rel=float(np.min(lmin / np.maximum(ps["lmax"],
                                                       1e-300))),
                nviol=nviol, ncell=int(len(jd)),
                frac_viol=nviol / max(len(jd), 1),
                worst_jdef=float(np.nanmax(jd)) if len(jd) else 0.0,
                max_dnull=float(np.max(np.abs(ps["dnull"]))),
                dnull_end=float(ps["dnull"][-1]),
                r_end=float(ps["r"][-1]), ang_end=float(ps["ang"][-1]),
                ang_min=float(np.min(ps["ang"])),
                ang_argmin=float(np.argmin(ps["ang"]) /
                                 max(len(ps["ang"]) - 1, 1)))


# ------------------------------------------------- the Phi spot gate
def sqrt2(A):
    w, V = np.linalg.eigh(A)
    return V @ np.diag(np.sqrt(np.maximum(w, 0.0))) @ V.T


def tri_mat(tri):
    return np.array([[tri[0], tri[2]], [tri[2], tri[1]]])


def lorentz_of(M):
    """The 3x3 Lorentz action of the congruence X -> M^T X M in the
    (t, x, y) coordinates."""
    basis = (0.5 * np.eye(2), 0.5 * np.diag([1.0, -1.0]),
             np.array([[0.0, 0.5], [0.5, 0.0]]))
    Phi = np.empty((3, 3))
    for i, E in enumerate(basis):
        Y = M.T @ E @ M
        Phi[:, i] = (Y[0, 0] + Y[1, 1], Y[0, 0] - Y[1, 1],
                     2.0 * Y[0, 1])
    return Phi


def phi_spot(Aprev, Anext):
    """M_k, Phi_k and the exact-identity residuals for one cell.
    Returns None when the map does not exist (state not PD -- exactly
    the cone-exit event the census measures; declared robustness
    guard, no bar changed)."""
    if float(np.linalg.eigvalsh(Aprev)[0]) <= 0.0 \
            or float(np.linalg.eigvalsh(Anext)[0]) <= 0.0:
        return None
    S = sqrt2(Aprev)
    Sinv = np.linalg.inv(S)
    IA = np.eye(2) + Sinv @ (Anext - Aprev) @ Sinv
    wmin = float(np.linalg.eigvalsh(IA)[0])
    if wmin <= 0.0:
        return None
    M = Sinv @ sqrt2(IA) @ S
    Phi = lorentz_of(M)
    c = float(np.linalg.det(M)) ** 2
    res_id = float(np.max(np.abs(Phi.T @ J3 @ Phi - c * J3)))
    uP = np.array([Aprev[0, 0] + Aprev[1, 1], Aprev[0, 0] - Aprev[1, 1],
                   2.0 * Aprev[0, 1]])
    uN = np.array([Anext[0, 0] + Anext[1, 1], Anext[0, 0] - Anext[1, 1],
                   2.0 * Anext[0, 1]])
    res_map = float(np.max(np.abs(Phi @ uP - uN))) \
        / max(float(np.max(np.abs(uN))), 1e-300)
    lam_lit = float(np.max(np.linalg.eigvalsh(Phi.T @ J3 @ Phi - J3)))
    return dict(c=c, res_id=res_id, res_map=res_map, lam_lit=lam_lit)


# ------------------------------------------------- controls: Epstein
def epstein_atoms(alpha):
    """Atoms of the x^2 + 5 y^2 comb (n >= 2 represented): positions
    log n, raw masses r_Q(n)/sqrt(n) (v818 recipe, verbatim)."""
    Nmax = int(math.floor(math.exp(2.0 * alpha)))
    cnt = np.zeros(Nmax + 1)
    for xx in range(0, int(math.isqrt(Nmax)) + 1):
        rem = Nmax - xx * xx
        if rem < 0:
            break
        yy = np.arange(0, int(math.isqrt(rem // 5)) + 1)
        n = xx * xx + 5 * yy * yy
        mult = (2.0 if xx > 0 else 1.0) * np.where(yy > 0, 2.0, 1.0)
        np.add.at(cnt, n, mult)
    nn = np.nonzero(cnt[2:])[0] + 2
    return np.log(nn.astype(float)), cnt[nn] / np.sqrt(nn.astype(float))


def atom_reads(rr, uuX):
    """Per-atom 2x2 spline reads at custom positions (the build_window
    Xn recipe at explicit u)."""
    Mz, D = rr["M"], rr["D"]
    out = np.empty((len(uuX), 3))
    for i, u in enumerate(uuX):
        out[i, 0] = core.spline_project(rr["W11"], u, D, Mz)
        out[i, 1] = core.spline_project(rr["W22"], u, D, Mz)
        out[i, 2] = core.spline_project(rr["W12"], u, D, Mz)
    return out


def eig2_min(A):
    return float(np.linalg.eigvalsh(A)[0])


def main():
    spec_hash = hashlib.sha256(FROZEN_SPEC.encode()).hexdigest()
    g1_hash = hashlib.sha256(
        inspect.getsource(breaks_G1).encode()).hexdigest()
    g2_hash = hashlib.sha256(
        inspect.getsource(breaks_G2).encode()).hexdigest()
    print("=" * 78)
    print("PRIME.CELLCONE.TRANSPORT.01 -- completed cells as Lorentz "
          "cone transport")
    print("=" * 78)
    print(FROZEN_SPEC)
    print("SPEC sha256   : %s" % spec_hash)
    print("G1 rule sha256: %s" % g1_hash)
    print("G2 rule sha256: %s" % g2_hash)
    print("U0 = %.6f (C_TH = %.6f)" % (U0, C_TH))

    # ============================================================== S0
    print("\nS0 -- firewall")
    check("S0.AST no zero/prime-table loader (banned ids absent); "
          "mpmath = the zero-free constant C_TH only; no RNG anywhere",
          ast_zero_firewall(__file__))

    # ============================================================== S1
    print("\nS1 -- ladder + wards")
    rows = []
    for kz in core.frame_a_zones():
        rr = core.build_window(kz)
        if rr["h"] == ANOMALOUS_H:
            continue
        if math.exp(2.0 * rr["alpha"]) > core.ATOM_MAX + 0.5:
            continue
        rows.append(dict(rr=rr, kz=kz, h=rr["h"], alpha=rr["alpha"],
                         tau=eig2_min(rr["Ah"])))
    rows.sort(key=lambda w: w["alpha"])
    print("    %d regular complete rungs, alpha %.3f..%.3f, h %d..%d"
          % (len(rows), rows[0]["alpha"], rows[-1]["alpha"],
             min(w["h"] for w in rows), max(w["h"] for w in rows)))

    ref_ok = True
    ref_txt = []
    for kz, tref in TAU_REFS.items():
        tk = eig2_min(core.build_window(kz)["Ah"])
        rel = abs(tk - tref) / tref
        ref_ok = ref_ok and rel <= TAU_REF_REL
        ref_txt.append("kz%d %.6e (rel %.1e)" % (kz, tk, rel))
    check("S1.REF tau references reproduce margin_law: %s (bar %.0e)"
          % ("; ".join(ref_txt), TAU_REF_REL), ref_ok)

    # continuum grids + envelope ward + telescoping wards per rung
    env_min = float("inf")
    tel_worst = 0.0
    cw_worst = 0.0
    for w in rows:
        rr = w["rr"]
        edges, reads = pnt_grid(rr)
        w["edges"], w["reads"] = edges, reads
        S_pnt = tri_mat(cum_reads(edges, reads,
                                  [2.0 * rr["alpha"]])[0])
        w["S_pnt"] = S_pnt
        A0 = rr["B"] - S_pnt
        w["A0"] = A0
        w["tau_pnt"] = eig2_min(A0)
        e1 = (w["tau"] / w["tau_pnt"]) * w["h"] ** 1.5
        w["e1"] = e1
        env_min = min(env_min, e1)
        uu, lam, Xn = rr["uu"], rr["lam"], rr["Xn"]
        w["mm"] = 2.0 * lam
        for gname in ("G1", "G2"):
            b = (breaks_G1(uu, rr["alpha"]) if gname == "G1"
                 else breaks_G2(w["mm"], rr["alpha"]))
            Chat = cell_increments(edges, reads, b)
            csum = Chat.sum(axis=0)
            cw = float(np.max(np.abs(tri_mat(csum) - S_pnt))) \
                / max(float(np.max(np.abs(S_pnt))), 1e-300)
            cw_worst = max(cw_worst, cw)
            deltas = Chat - lam[:, None] * Xn
            A0t = (A0[0, 0], A0[1, 1], A0[0, 1])
            ps = path_stats(A0t, deltas)
            Aend = tri_mat((ps["a11"][-1], ps["a22"][-1],
                            ps["a12"][-1]))
            tel = float(np.max(np.abs(Aend - rr["Ah"]))) \
                / max(float(np.max(np.abs(rr["Ah"]))), 1e-300)
            tel_worst = max(tel_worst, tel)
            w[gname] = dict(breaks=b, deltas=deltas, ps=ps,
                            summ=flow_summary(ps))
    check("S1.ENV the certified envelope reproduces: min e1 = %.4f >= "
          "%.4f (= %.3f x %.3f) on all %d rungs"
          % (env_min, ENV_C * ENV_GUARD, ENV_C, ENV_GUARD, len(rows)),
          env_min >= ENV_C * ENV_GUARD)
    check("S1.TEL the completed flow TELESCOPES exactly per rung per "
          "grouping: worst |A_K - Ah| rel %.2e and worst "
          "|sum Chat - S_pnt| rel %.2e (bar %.0e) -- the completed "
          "cells are a PARTITION of the certified objects"
          % (tel_worst, cw_worst, WARD_REL),
          tel_worst <= WARD_REL and cw_worst <= WARD_REL)

    # Phi spot identity gate (smallest rung, G1)
    w0 = rows[0]
    ps0 = w0["G1"]["ps"]
    K0 = len(w0["G1"]["deltas"])
    spots = sorted(set([0, K0 // 2, K0 - 1]
                       + list(range(0, K0, 500))))
    worst_id = worst_map = 0.0
    lit_lines = []
    n_spot = 0
    for k in spots:
        Ap = tri_mat((ps0["a11"][k], ps0["a22"][k], ps0["a12"][k]))
        An = tri_mat((ps0["a11"][k + 1], ps0["a22"][k + 1],
                      ps0["a12"][k + 1]))
        sp = phi_spot(Ap, An)
        if sp is None:
            continue
        n_spot += 1
        worst_id = max(worst_id, sp["res_id"] / max(sp["c"], 1.0))
        worst_map = max(worst_map, sp["res_map"])
        if len(lit_lines) < 4:
            lit_lines.append("cell %d: c = %.6f, lam_max(Phi^TJPhi-J) "
                             "= %+.2e (= max(c-1,1-c) as derived)"
                             % (k, sp["c"], sp["lam_lit"]))
    check("S1.PHI the congruence/Lorentz identity holds on %d spot "
          "cells (smallest rung): worst ||Phi^TJPhi - cJ|| rel %.1e, "
          "worst |Phi L(A_k) - L(A_{k+1})| rel %.1e (bar %.0e)"
          % (n_spot, worst_id, worst_map, PHI_REL),
          worst_id <= PHI_REL and worst_map <= PHI_REL)
    print("    HONESTY (the literal J-inequality): "
          + "; ".join(lit_lines))
    print("    -> the frozen J-contractivity reading is ON-CONE: "
          "jdef = det-ratio - 1 <= 0.")

    # ============================================================== S2
    print("\nS2 -- the completed flow, per-rung census (both groupings)")
    spf = spf_sieve(int(core.ATOM_MAX) + 1)
    for gname in ("G1", "G2"):
        print("\n  grouping %s:" % gname)
        print("    %5s %7s %6s | %5s %10s %8s | %5s %6s %5s | %6s "
              "%8s | %7s %7s"
              % ("h", "alpha", "K", "cone", "min_lmin", "min_rel",
                 "n_out", "f_out", "1st", "nJvio", "fracJ",
                 "r_end", "ang_end"))
        for w in rows:
            s = w[gname]["summ"]
            print("    %5d %7.3f %6d | %5s %10.2e %8.1e | %5d %6.3f "
                  "%5d | %6d %8.4f | %7.4f %7.3f"
                  % (w["h"], w["alpha"], s["ncell"],
                     "IN" if s["cone_ok"] else "EXIT",
                     s["min_lmin"], s["min_rel"], s["n_out"],
                     s["frac_out"], s["first_exit"], s["nviol"],
                     s["frac_viol"], s["r_end"], s["ang_end"]))
    # per-cell detail on the smallest rungs (G1)
    print("\n  per-cell detail, %d smallest rungs (G1): first 12 cells "
          "+ 5 worst-jdef cells" % N_DETAIL)
    for w in sorted(rows, key=lambda v: v["h"])[:N_DETAIL]:
        ps = w["G1"]["ps"]
        jd = w["G1"]["ps"]["jdef"]
        uu = w["rr"]["uu"]
        nn = np.rint(np.exp(uu)).astype(np.int64)
        print("    rung h = %d (alpha %.3f, K = %d):"
              % (w["h"], w["alpha"], len(jd)))
        print("      %5s %8s %6s | %10s %10s %10s | %8s"
              % ("cell", "n", "u/2a", "lmin_k+1", "jdef", "dnull",
                 "r_k+1"))
        order = list(range(min(12, len(jd))))
        worst = list(np.argsort(-np.nan_to_num(jd, nan=-1e30))[:5])
        for k in order + [k for k in worst if k not in order]:
            print("      %5d %8d %6.3f | %10.2e %+10.2e %10.2e | %8.4f"
                  % (k, nn[k], uu[k] / (2 * w["alpha"]),
                     ps["lmin"][k + 1], jd[k], ps["dnull"][k + 1],
                     ps["r"][k + 1]))

    # census typing of J-violating cells (both groupings, all rungs)
    print("\n  J-defect census typing (jdef > %.0e), all rungs:"
          % JDEF_TOL)
    census = {}
    for gname in ("G1", "G2"):
        cls = dict(total=0, viol=0, p2=0, kge2=0, p1m4=0, p3m4=0,
                   dec=np.zeros(10))
        vd = np.zeros(10)
        td = np.zeros(10)
        for w in rows:
            jd = w[gname]["ps"]["jdef"]
            uu = w["rr"]["uu"]
            nn = np.rint(np.exp(uu)).astype(np.int64)
            frac = uu / (2.0 * w["alpha"])
            deci = np.clip((frac * 10).astype(int), 0, 9)
            viol = np.nan_to_num(jd, nan=-1e30) > JDEF_TOL
            cls["total"] += len(jd)
            cls["viol"] += int(viol.sum())
            np.add.at(td, deci, 1)
            np.add.at(vd, deci[viol], 1)
            for n in nn[viol]:
                p = int(spf[n])
                k = 0
                m = int(n)
                while m > 1:
                    m //= p
                    k += 1
                if p == 2:
                    cls["p2"] += 1
                elif p % 4 == 1:
                    cls["p1m4"] += 1
                else:
                    cls["p3m4"] += 1
                if k >= 2:
                    cls["kge2"] += 1
        with np.errstate(divide="ignore", invalid="ignore"):
            decf = np.where(td > 0, vd / np.maximum(td, 1), 0.0)
        census[gname] = cls
        print("    %s: %d/%d cells J-expand (%.1f%%); of the "
              "violators: p=2 %d, p=1(4) %d, p=3(4) %d, k>=2 %d; "
              "violation fraction by u/2alpha decile: %s"
              % (gname, cls["viol"], cls["total"],
                 100.0 * cls["viol"] / max(cls["total"], 1),
                 cls["p2"], cls["p1m4"], cls["p3m4"], cls["kge2"],
                 np.array2string(decf, precision=2)))

    # ============================================================== S3
    print("\nS3 -- the cascade / boundary-ray analysis")
    aas = [w["alpha"] for w in rows]
    ray_sub = {}
    for gname in ("G1", "G2"):
        r_end = [w[gname]["summ"]["r_end"] for w in rows]
        a_end = [w[gname]["summ"]["ang_end"] for w in rows]
        kt_r = kendall_tau(aas, r_end)
        kt_a = kendall_tau(aas, a_end)
        ok = kt_r >= KEN_BAR and kt_a <= -KEN_BAR
        ray_sub[gname] = ok
        argmins = [w[gname]["summ"]["ang_argmin"] for w in rows]
        print("    %s: r_end %.4f -> %.4f (Kendall vs alpha %+.3f), "
              "angle to (5,-3,4) %.3f -> %.3f deg (Kendall %+.3f); "
              "closest path approach to the ray at relative cell "
              "position median %.3f -- %s"
              % (gname, r_end[0], r_end[-1], kt_r, a_end[0],
                 a_end[-1], kt_a, float(np.median(argmins)),
                 "RAY-EDGE-CONFIRMED" if ok else "RAY-EDGE-OPEN"))
    print("    (sub-verdict only; the compiler ray (5,-3,4) is the "
          "exact null direction q = 0, v807)")

    # ============================================================== S4
    print("\nS4 -- the incomplete-cell contrast (must break; "
          "mass-forced, stated)")
    n_exit = 0
    exit_pos = []
    for w in rows:
        rr = w["rr"]
        deltas = -(rr["lam"][:, None] * rr["Xn"])
        ps = path_stats((w["A0"][0, 0], w["A0"][1, 1], w["A0"][0, 1]),
                        deltas)
        s = flow_summary(ps)
        if not s["cone_ok"]:
            n_exit += 1
            fe = s["first_exit"]
            exit_pos.append(rr["uu"][min(fe, len(rr["uu"]) - 1)]
                            / (2.0 * rr["alpha"]) if fe > 0 else 0.0)
    frac = n_exit / len(rows)
    check("S4.INC naive cells (atom kick alone, no continuum piece, "
          "same base Ah_pnt) EXIT the cone on %d/%d rungs (%.2f >= "
          "%.2f); first-exit u/2alpha median %.3f -- the corpus's "
          "additive-granularity negative reproduced: the completion "
          "is load-bearing"
          % (n_exit, len(rows), frac, MB_FRAC,
             float(np.median(exit_pos)) if exit_pos else float("nan")),
          frac >= MB_FRAC)

    # ============================================================== S5
    print("\nS5 -- controls (stride-%d subset, G1 pairing unless "
          "stated)" % STRIDE)
    sub = rows[::STRIDE]
    real_dnull_med = float(np.median(
        [w["G1"]["summ"]["max_dnull"] for w in sub]))

    # C1 order swap (measured, both groupings)
    print("  C1 order swap (cells applied in decreasing u; endpoint "
          "identical by additivity):")
    for gname in ("G1", "G2"):
        n_exit_sw = 0
        end_dev = 0.0
        for w in sub:
            deltas = w[gname]["deltas"][::-1]
            ps = path_stats((w["A0"][0, 0], w["A0"][1, 1],
                             w["A0"][0, 1]), deltas)
            s = flow_summary(ps)
            if not s["cone_ok"]:
                n_exit_sw += 1
            Aend = tri_mat((ps["a11"][-1], ps["a22"][-1],
                            ps["a12"][-1]))
            end_dev = max(end_dev,
                          float(np.max(np.abs(Aend - w["rr"]["Ah"])))
                          / float(np.max(np.abs(w["rr"]["Ah"]))))
        fwd_exits = sum(0 if w[gname]["summ"]["cone_ok"] else 1
                        for w in sub)
        print("    %s reversed: cone exits %d/%d (forward: %d/%d); "
              "endpoint dev %.1e -- ORDER %s for the path"
              % (gname, n_exit_sw, len(sub), fwd_exits, len(sub),
                 end_dev,
                 "MATTERS" if n_exit_sw != fwd_exits else
                 "does not decide cone membership"))

    def control_flow(w, uuX, lamX, XnX, cont_fac=1.0,
                     base_fac=1.0):
        """One control flow on rung w: custom atoms + G1 pairing;
        continuum scaled by cont_fac; base B - base_fac*S_pnt."""
        rr = w["rr"]
        b = breaks_G1(uuX, rr["alpha"])
        Chat = cont_fac * cell_increments(w["edges"], w["reads"], b)
        deltas = Chat - lamX[:, None] * XnX
        A0 = rr["B"] - base_fac * w["S_pnt"]
        ps = path_stats((A0[0, 0], A0[1, 1], A0[0, 1]), deltas)
        return flow_summary(ps)

    # C2 equal-weight scramble
    n_exit_eq = 0
    dn_eq = []
    for w in sub:
        rr = w["rr"]
        mm_eq = np.full(len(rr["uu"]),
                        float(np.sum(w["mm"])) / len(rr["uu"]))
        s = control_flow(w, rr["uu"], 0.5 * mm_eq, rr["Xn"])
        if not s["cone_ok"]:
            n_exit_eq += 1
        dn_eq.append(s["max_dnull"])
    eq_fire = (n_exit_eq / len(sub) >= CTRL_FRAC
               or float(np.median(dn_eq)) >= DNULL_FAC * real_dnull_med)
    check("S5.C2 [must-break] equal-weight scramble (positions kept, "
          "masses -> ladder mean, total matched): cone exits %d/%d, "
          "median path max|dnull| %.2e vs real %.2e (fire iff exits "
          ">= %.1f or dnull >= %.0fx) -- %s"
          % (n_exit_eq, len(sub), float(np.median(dn_eq)),
             real_dnull_med, CTRL_FRAC, DNULL_FAC,
             "fires" if eq_fire else "does NOT fire"), eq_fire)

    # C3 Epstein comb
    n_exit_ep = 0
    dn_ep = []
    ep_exit_pos = []
    for w in sub:
        rr = w["rr"]
        uuE, mE_raw = epstein_atoms(rr["alpha"])
        kap = float(np.sum(w["mm"])) / float(np.sum(mE_raw))
        XnE = atom_reads(rr, uuE)
        s = control_flow(w, uuE, 0.5 * kap * mE_raw, XnE)
        if not s["cone_ok"]:
            n_exit_ep += 1
            fe = s["first_exit"]
            ep_exit_pos.append(uuE[min(max(fe - 1, 0), len(uuE) - 1)]
                               / (2.0 * rr["alpha"]))
        dn_ep.append(s["max_dnull"])
    ep_fire = (n_exit_ep / len(sub) >= CTRL_FRAC
               or float(np.median(dn_ep)) >= DNULL_FAC * real_dnull_med)
    check("S5.C3 [must-break] Epstein x^2+5y^2 comb (mass-matched, "
          "same completion): cone exits %d/%d, median path "
          "max|dnull| %.2e; first-exit u/2alpha %s -- %s"
          % (n_exit_ep, len(sub), float(np.median(dn_ep)),
             ("median %.3f" % float(np.median(ep_exit_pos)))
             if ep_exit_pos else "n/a",
             "fires" if ep_fire else "does NOT fire"), ep_fire)

    # C5 wrong pole normalization
    n_exit_wr = 0
    for w in sub:
        rr = w["rr"]
        s = control_flow(w, rr["uu"], rr["lam"], rr["Xn"],
                         cont_fac=WRONG_FAC, base_fac=WRONG_FAC)
        if not s["cone_ok"]:
            n_exit_wr += 1
    wr_fire = n_exit_wr / len(sub) >= CTRL_FRAC
    check("S5.C5 [must-break] wrong pole normalization (continuum "
          "density x %.1f, self-consistent base B - %.1f S_pnt; "
          "endpoint still telescopes to Ah): cone exits %d/%d -- %s"
          % (WRONG_FAC, WRONG_FAC, n_exit_wr, len(sub),
             "fires" if wr_fire else "does NOT fire"), wr_fire)

    # ============================================================== S6
    print("\n" + "=" * 78)
    print("S6 -- VERDICT")
    print("=" * 78)
    runtime = time.time() - T0
    WARD_IDS = ("S0.AST", "S1.REF", "S1.ENV", "S1.TEL", "S1.PHI")
    ward_fails = [f for f in FAILS if f in WARD_IDS]
    valid = not ward_fails and runtime <= RUNTIME_CAP
    cone_all = {g: all(w[g]["summ"]["cone_ok"] for w in rows)
                for g in ("G1", "G2")}
    jzero = {g: census[g]["viol"] == 0 for g in ("G1", "G2")}
    exit_frac = {g: sum(0 if w[g]["summ"]["cone_ok"] else 1
                        for w in rows) / len(rows)
                 for g in ("G1", "G2")}
    contrast_ok = frac >= MB_FRAC
    controls_ok = eq_fire and ep_fire and wr_fire
    if not valid:
        verdict = "INVALID"
    elif (cone_all["G1"] and cone_all["G2"] and jzero["G1"]
          and jzero["G2"] and contrast_ok and controls_ok):
        verdict = "CELLS-PRESERVE-CONE"
    elif exit_frac["G1"] >= 0.5 and exit_frac["G2"] >= 0.5:
        verdict = "CONE-BROKEN"
    else:
        verdict = "CONE-PARTIAL"
    print("""
  VERDICT: %s
    cone preserved at every cell:  G1 %s (exit fraction %.2f), G2 %s
      (exit fraction %.2f)
    per-cell J-contraction (jdef <= %.0e): G1 %d/%d violations
      (%.1f%%), G2 %d/%d (%.1f%%)
    incomplete contrast fires: %s (%.2f of rungs)
    must-break controls: equal-weight %s, Epstein %s, wrong-norm %s
    ray sub-verdict: G1 %s, G2 %s
""" % (verdict,
       "YES" if cone_all["G1"] else "no", exit_frac["G1"],
       "YES" if cone_all["G2"] else "no", exit_frac["G2"],
       JDEF_TOL,
       census["G1"]["viol"], census["G1"]["total"],
       100.0 * census["G1"]["viol"] / max(census["G1"]["total"], 1),
       census["G2"]["viol"], census["G2"]["total"],
       100.0 * census["G2"]["viol"] / max(census["G2"]["total"], 1),
       "YES" if contrast_ok else "NO", frac,
       "fires" if eq_fire else "NO", "fires" if ep_fire else "NO",
       "fires" if wr_fire else "NO",
       "RAY-EDGE-CONFIRMED" if ray_sub["G1"] else "RAY-EDGE-OPEN",
       "RAY-EDGE-CONFIRMED" if ray_sub["G2"] else "RAY-EDGE-OPEN"))
    if verdict == "CONE-BROKEN":
        for g in ("G1", "G2"):
            fe = [w[g]["summ"]["first_exit"] for w in rows]
            fo = [w[g]["summ"]["frac_out"] for w in rows]
            nr = [w[g]["summ"]["n_out_runs"] for w in rows]
            lo = [w[g]["summ"]["last_out"]
                  / max(w[g]["summ"]["ncell"], 1) for w in rows]
            end_in = sum(1 for w in rows
                         if w[g]["ps"]["lmin"][-1] > 0.0)
            print("  TYPED (%s): first exit at cell index median %d "
                  "(the n = 2 cell if 0); fraction of path states "
                  "out of cone median %.3f; out-runs per rung median "
                  "%d; last out-of-cone state at relative position "
                  "median %.3f; endpoint back inside the cone on "
                  "%d/%d rungs (= the certified tau > 0)"
                  % (g, int(np.median(fe)), float(np.median(fo)),
                     int(np.median(nr)), float(np.median(lo)),
                     end_in, len(rows)))
    if not ep_fire:
        print("  CONTROL SURPRISE (typed, kept as frozen with its "
              "FAIL): the mass-matched Epstein comb does NOT break "
              "the cone transport while the TRUE von Mangoldt comb "
              "does -- the cone dips are driven by the true comb's "
              "own small-x fluctuation E(x) = psi(x) - x (the n = 2 "
              "cell), which the smoother Epstein representation "
              "numbers do not reproduce; the frozen must-break "
              "prediction pointed the wrong way.")
    if verdict == "CELLS-PRESERVE-CONE":
        print("""  WHAT THE INFINITE STATEMENT WOULD NEED (named exactly):
    (i)   the UNCONDITIONAL completed-cell inequality: for every
          prime power n, the completed increment Chat_n - lam_n
          Xhat_n keeps A > 0 and det non-increasing FROM THE
          CONSTRUCTION (an explicit inequality between the local
          von Mangoldt mass and its Stieltjes continuum share on the
          deployed reads) -- replacing this probe's measured census;
    (ii)  a uniform Birkhoff/Wojtkowski contraction modulus for the
          composed congruence flow in the Lorentz cone metric
          (the v773 missing piece, now on the 2x2 lock surface);
    (iii) the boundary transition: the composed flow's limit
          direction is the null ray (5,-3,4) with the transversal
          reserve tau > 0 at every finite stage -- the v818 amplifier
          floor rho > 0 restated as cone non-degeneracy.""")
    print("""
  HONESTY: this is a FINITE transport measurement on %d deployed
  rungs (2-mode lock compression).  Cone preservation of the
  completed flow is a statement about the hybrid window (atoms below
  the horizon, density above) -- it does NOT bound the infinite
  ladder, does NOT provide the uniform capture constant, and the
  per-cell J-census is measured, not derived.  The incomplete
  contrast is mass-forced (its firing confirms the bookkeeping, not
  arithmetic).  NO RH claim.""" % len(rows))
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed%s"
          % (runtime, len(CHECKS), len(FAILS),
             ("  " + ",".join(FAILS)) if FAILS else ""))
    print("[VERDICT] %s" % verdict)
    return 0 if valid else 1


if __name__ == "__main__":
    raise SystemExit(main())
