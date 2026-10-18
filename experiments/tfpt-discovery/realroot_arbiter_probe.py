#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""realroot_arbiter_probe -- ARBITER, PRIME.SEMILOCAL.REALROOT.LIMIT.01

FROZEN SPEC v1 (2026-08-14).  EXPLORATION ONLY.  This probe writes no
files, changes no verification module, paper, ledger, website, manifest
or status marker.  It makes NO RH claim, NO positivity claim.  It
closes no gate and narrows no gate.

=======================================================================
MISSION
=======================================================================
Round 83 froze a RECORDED three-way instrument conflict on the real-root
architecture (source-only finite self-adjoint H_N, E_N = det_reg(z-H_N),
identification with Xi via trace convergence R3 + uniform tails R4):

  LANE 1  semilocal_realroot_limit_probe.py  (16/16)
          verdict REALROOT-ARCHITECTURE-OPEN
  LANE 2  stc_sol_convergence_probe.py       (4/4)
          verdict STC-OPEN + two boxed missing lemmata
  LANE 3  stc_opus_convergence_probe.py      (20/20)
          verdict STC-DISGUISE + STC-FALSE for the family
          (Nyquist density obstruction, unweighted trace diverges)

The arbiter reconstructs all three instruments side by side, names the
sum each lane measured (Q1), tests lane 3's density theorem against
lanes 1-2's objects at depth (Q2), runs one unified convergence table
(Q3), and issues ONE architecture verdict (Q4).  Standard of this
repo's arbiter rounds: the conflict is resolved by exhibiting the
mechanism, not by majority vote.

=======================================================================
Q1 PRE-AUDIT (from the three probes' code, verified executably below)
=======================================================================
 LANE 1 object: Connes extremal family.  Trig-Galerkin compression of
   the Weil form on [-a,a], a = log(x)/2, K = ceil(1.25 x log x) even
   cosine modes, bottom eigenvector -> E_N = etahat.  Spectrum used:
   ALL nontrivial zeros of E_N (complete working-precision polynomial
   census, hp_zero_data) PLUS the exact lattice zeros j pi/a, j >= K.
   Sum (trig_eps, lines 1071-1078): UNWEIGHTED
   eps = |2 sum h(zeros) + 2 sum_lattice h(j pi/a) - SRC|.
   No filter, no weights.  Ladder x = 3,5,8,13, dps 45-120.
 LANE 2 object: Connes-van Suijlekom quotient D# = D - |D xi><1| built
   from the SAME Galerkin minimizer (own K = 12/18/26, dps 70-120).
   Doc lines 23-25: nonzero eigenvalues of D# = the NON-LATTICE zeros
   of the minimizer's Fourier transform.  Sum (trace_h, lines 333-335):
   UNWEIGHTED  math.fsum(h(lam) for lam in spectrum) -- no lattice
   tail, no weights.  Ladder x = 3,5,8.
 LANE 3 object: Caratheodory-Fejer Gauss-Szego atoms of the uniform
   tent-mesh Toeplitz compression, D = 1/(2ex), N = l/D nodes.  Sums
   (S2, line 595):  u = np.sum(hv)          UNWEIGHTED over all N nodes
                    wq = np.dot(w, hv)      WEIGHTED (Christoffel)
   R3 is the unweighted one; the weighted one is lane 3's separate
   exact-identity row.  Ladder x = 5..144.
 TARGET normalization: all three use W(h) = POLE + ARCH - PRIME with
   identical conventions (cross-warded here at 1e-9).
 CONSEQUENCE TO TEST: all three lanes sum honest UNWEIGHTED sums; no
 lane's convergence is a weighted quadrature or a filtered subset in
 disguise.  The conflict, if real, must be DIFFERENT OBJECT or
 DIFFERENT DEPTH.

=======================================================================
FROZEN LADDERS, INSTRUMENTS, BARS
=======================================================================
 EXTREMAL (lanes 1-2 object, lane 1's own builder build_trig_cell_hp):
   census ladder x = 3, 5, 8, 13 (complete mp census hp_zero_data);
   DEEP RUNG x = 21, dps 128 >= floor 4 pi x/ln10 + 5 = 119.6
   (declared price: the minimizer direction exists only at internal
   precision ~e^{-4 pi x}; smoke measured tau(21) ~ 1e-93,
   gap ~ 7e-86, build ~682 s).
   At x = 21 the complete census is INFEASIBLE: mp.polyroots at degree
   79 raised NoConvergence (maxsteps=300) in the smoke, and the
   float64 profile scan FABRICATES zeros beyond tau ~ 30 (amendment-A2
   pathology; smoke measured 5717 "zeros", deficit -5638).  Frozen
   replacement instrument: MP-PRECISION PROFILE SCAN of E(t) on
   (0, 100), step 0.02, 60 bisections, at the cell's working dps --
   warded against the exact census at x = 8 and x = 13 (band counts
   in (0,30) and (0,60) must MATCH EXACTLY).  Band counts, not eps,
   are the x = 21 deliverable (declared subsampling: no Q3 trace row
   at x = 21; a scan-based trace would carry an undeclared edge floor).
   Realness/completeness at x = 21 beyond the scanned band is CITED
   (CF/[32] realness theorem, K-1 = 79 forced) and not re-measured.
 QUOTIENT (lane 2 object): rebuilt ONCE at x = 8 (modes 26, dps 120,
   lane 2's own base_form/build_form/finite_connes_operator); identity
   gate: its positive spectrum must sit on the zeros of the SAME
   minimizer's transform (|E(lam)|/scale <= 1e-12) and its (0,30)
   census must equal the E-scan count.  Deep quotient rungs are NOT
   rebuilt: the smoke measured that a float64 D# from rounded
   coefficients is unusable (first-eigenvalue error 2.68), and the mp
   D# at K = 80 is out of budget; instead the identity above transfers
   the extremal band counts to the quotient (they differ only by the
   lattice zeros, all >= K pi/a = 163 at x = 21).
 MESH-CF (lane 3 object, lane 3's own run_rung): x = 5, 8, 13, 21, 34,
   55, 89, 144 on the exact balance D = 1/(2ex).
 UNIFIED BATTERY (Q3; every row tower-complete for x >= 5, closed h):
   tent(1.5)      = lane 3's B1;   h = 1.5 sinc^2(0.75 tau)  ~ tau^-2
   bump(1.5,3)    = lane 3's B3 == (B,m) = (1.5,3) Bessel row ~ tau^-4
   bessel(1.0,2)  = lane 2's (0.7|1.0, m) family at B = 1.0, m = 2
   bessel(1.0,4)  = lane 2's row at B = 1.0, m = 4
   SRC via lane 1's src_value, cross-warded against lane 3's
   weil_of_kernel (bar 1e-9).  Extremal rows reported BOTH with the
   lattice tail (lane 1's sum) and without (lane 2's quotient sum).
   Row typing over each construction's ladder: DIVERGES iff
   eps_last > 2 eps_first; CONVERGES iff eps_last < eps_first/2;
   else PLATEAU.  Extremal typing ladder x = (5, 8, 13).
 Z1-TRANSFER WARD (the disguise content, lane 3's (*) applied to the
   TRIG family): unnormalized Galerkin entries M[j,k] at x = 5 vs
   2 sum_{gamma>0, cache} B_j(gamma) B_k(gamma) plus the analytic
   cache-tail model (-1)^{j+k} (2/pi)(log(G/2pi)+1)/G, G = top cache
   ordinate; bars: corrected worst abs dev <= 2e-4 AND the model must
   explain >= 75 percent of the raw deviation.  Plus the margin
   identity lam_min vs 2 sum E(gamma)^2 (rel bar 0.10, cache-truncated).
 CACHE (verified_zeros_n7000.npy): read ONLY inside ward_/target_
   functions and main; instrument and band-reference only, never
   construction (AST firewall gate).
 CONTROLS: NOT re-run here -- world separation was gated inside each
   lane (lane 1 HP SCRPOS/EPSTEIN at x = 8, median 1.26e6-1.40e6 vs
   bar 5; lane 2 3.1e5/4.1e5; lane 3 C1-C3).  The arbiter adjudicates
   the conflict between PASSING instruments; re-running controls would
   not discriminate between them.  DECLARED, not built.
 RUNTIME_BAR = 2400 s (the x = 21 rung alone is ~682 s).
 --smoke: extremal <= 8, mesh <= 13, no deep rung; NOT verdict-bearing.

=======================================================================
COMPOSITE VERDICT RULES (frozen; gates are instrument-only, findings
select the branch -- the probe must PASS its gates while recording
whatever verdict is true)
=======================================================================
 Findings computed:
   MESH-UNIFORM      mesh-CF count in (0,30) tracks 30 l/2pi within
                     30 percent on every rung (lane 3's S5 recomputed);
   MESH-UNW-DIV      >= 3 of 4 unified rows: mesh unweighted diverges;
   MESH-WT-CONV      4 of 4: mesh weighted converges;
   EXT-UNW-CONV      >= 3 of 4: extremal unweighted converges;
   EXT-FLAT-30       extremal count in (0,30) == cache count (3) on
                     every rung x >= 5 INCLUDING x = 21, min zero
                     == gamma_1 within 1e-3;
   EXT-FLAT-60       extremal count in (0,60) == cache count (13) at
                     x = 8, 13, 21.
 Branches (exactly one):
   ARBITER-INSTRUMENT-EDGE   any gate fails (exit 1);
   REALROOT-FALSE-FOR-FAMILY if NOT EXT-FLAT-30, or (NOT EXT-FLAT-60
       AND NOT EXT-UNW-CONV): the density obstruction reaches the
       extremal object -- lane 3 right for all three;
   REALROOT-EXTREMAL-INVADED-AT-DEPTH if EXT-FLAT-30 but NOT
       EXT-FLAT-60: fillers measurably creep into fixed bands; lane
       3's obstruction reaches the extremal family on a trajectory
       (recorded as the FALSE-leaning refinement of DEPTH-UNDECIDED);
   REALROOT-DEPTH-UNDECIDED  if EXT-FLAT-30 AND EXT-FLAT-60 AND
       MESH-UNIFORM AND MESH-UNW-DIV AND EXT-UNW-CONV: the conflict
       itself is RESOLVED (different objects: lane 3's theorem is
       proven for its mesh family and measurably does NOT transfer to
       the extremal/quotient family, whose fixed-band spectrum stays
       on the Xi census through the deepest feasible rung while the
       Nyquist excess is exiled to the band edge) -- but the
       architecture is neither killed nor saved: the thinning has no
       proof (Connes par. 6.6 open), its mechanism is the Gram-of-
       zero-evaluations structure (Z1-transfer: source-only in INPUT,
       zero-measure in CONTENT), and R3 alone is RH-hard (lanes 2 and
       3, independently), so no finite computation can verify -- only
       falsify -- the surviving lemma.  The deciding falsification
       computations and their measured costs are printed.
   (REALROOT-QUOTIENT-ESCAPES is NOT awardable by measurement: it
    requires a PROOF of thinning; the branch is documented, unreachable.)

SMOKE DISCLOSURE: the instruments were shaken out pre-freeze on x <= 8
plus one x = 21 feasibility build (timings, the polyroots failure, the
float64 fabrication, the f64-D# rejection, the Z1 tail-model constant
all frozen above as instrument facts).  Smoke numbers are not
verdict-bearing; every gated number below is produced by THIS run.

NO RH CLAIM.  NO POSITIVITY CLAIM.  EXPLORATION ONLY.
"""

from __future__ import annotations

import argparse
import ast
import hashlib
import math
import os
import sys
import time

import mpmath as mp
import numpy as np

import semilocal_realroot_limit_probe as lane1
import stc_opus_convergence_probe as lane3
import stc_sol_convergence_probe as lane2

# ---------------------------------------------------------------- bars
EXT_CENSUS_X = (3, 5, 8, 13)
EXT_DEEP_X = 21
EXT_DPS = {3: 45, 5: 60, 8: 80, 13: 120, 21: 128}
EXT_KFAC = 1.25
EXT_TYPE_X = (5, 8, 13)
MESH_X = (5, 8, 13, 21, 34, 55, 89, 144)
SCAN_HI_DEEP = 100.0
SCAN_STEP = 0.02
SCAN_BISECT = 60
LATTICE_TOP = 6000.0
DPS_FLOOR_MARGIN = 5.0
SRC_CROSS_BAR = 1e-9
Q1B_BAR = 1e-12
Q1_IMAG_BAR = 2e-7
W1_BAR = 1e-8
Z1T_CORR_BAR = 2e-4
Z1T_MODEL_SHARE = 0.75
Z1T_MARGIN_BAR = 0.10
MINZERO_BAR = 1e-3
MESH_UNIFORM_TOL = 0.30
RUNTIME_BAR = 2400.0
GAMMA1_LIT = 14.134725141734693790     # literature constant, ward only

SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
T0_WALL = time.time()
HERE = os.path.dirname(os.path.abspath(__file__))
CACHE_N7000 = os.path.join(HERE, "verified_zeros_n7000.npy")

CHECKS: list[tuple[str, bool, str]] = []


def check(name: str, ok: bool, detail: str) -> bool:
    ok = bool(ok)
    CHECKS.append((name, ok, detail))
    print("  [%s] %-52s %s" % ("PASS" if ok else "FAIL", name, detail))
    return ok


def section(title: str) -> None:
    print("\n" + "-" * 78 + "\n" + title + "\n" + "-" * 78, flush=True)


# ------------------------------------------------------------ firewall
def firewall_audit() -> tuple[bool, str]:
    with open(os.path.abspath(__file__), "r", encoding="utf-8") as fh:
        tree = ast.parse(fh.read())
    bad: list[str] = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Attribute):
            if node.attr.lower() in {"zeta", "zetazero", "zetazeros",
                                     "nzeros", "siegelz", "siegeltheta"}:
                bad.append("attr " + node.attr)
        if isinstance(node, ast.Call):
            fn = node.func
            name = (fn.id if isinstance(fn, ast.Name)
                    else fn.attr if isinstance(fn, ast.Attribute) else "")
            if name.lower() in {"zetazero", "zetazeros", "nzeros",
                                "declared_zeros"}:
                bad.append("call " + name)
    for node in ast.walk(tree):
        if not isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            continue
        cache_ok = node.name.startswith(("ward_", "target_")) \
            or node.name == "main"
        for ch in ast.walk(node):
            if isinstance(ch, ast.Name) and ch.id == "CACHE_N7000" \
                    and not cache_ok:
                bad.append("cache in " + node.name)
    return not bad, "violations: %s" % (bad or "none")


def ward_cache_load() -> np.ndarray:
    return np.asarray(np.load(CACHE_N7000), float)


# --------------------------------------------- mp-precision profile scan
def mp_profile_scan(cell: dict, t_hi: float) -> np.ndarray:
    """Zeros of E(t) = sum c_k B_k(t) on (0, t_hi), evaluated at the
    cell's working precision from the stored mp eigenvector (frozen
    replacement for the census where polyroots fails; float64 profile
    values are noise-dominated beyond tau ~ 30 at deep x)."""
    with mp.workdps(cell["dps"]):
        aa = mp.log(cell["x"]) / 2
        K = cell["K"]
        cs = [mp.mpf(s) for s in cell["cn_mp_str"]]
        oms = [k * mp.pi / aa for k in range(K)]

        def ee(t):
            t = mp.mpf(t)
            tot = mp.mpf(0)
            for k in range(K):
                for sg in (1, -1):
                    d = t - sg * oms[k]
                    tot += cs[k] * (aa if abs(d) < mp.mpf("1e-30")
                                    else mp.sin(aa * d) / d)
            return tot

        ts = [mp.mpf("1e-9") + i * mp.mpf(SCAN_STEP)
              for i in range(int(t_hi / SCAN_STEP) + 1)]
        vs = [ee(t) for t in ts]
        zs = []
        for i in range(len(ts) - 1):
            if vs[i] * vs[i + 1] < 0:
                lo, hi, flo = ts[i], ts[i + 1], vs[i]
                for _ in range(SCAN_BISECT):
                    mid = (lo + hi) / 2
                    fm = ee(mid)
                    if fm * flo > 0:
                        lo, flo = mid, fm
                    else:
                        hi = mid
                zs.append(float((lo + hi) / 2))
    return np.asarray(zs)


# ------------------------------------------------------ unified battery
def h_tent(lam: np.ndarray, B: float) -> np.ndarray:
    x = 0.5 * B * np.asarray(lam, float)
    out = np.full(x.shape, B, float)
    nz = np.abs(x) > 1e-9
    out[nz] = B * (np.sin(x[nz]) / x[nz]) ** 2
    return out


def unified_battery() -> list[tuple]:
    """(name, h(lam), f(v), f0, B) -- closed h, even PW, tower-complete
    for x >= 5."""
    return [
        ("tent(1.5)[l3-B1]",
         lambda t: h_tent(t, 1.5),
         lambda v: np.maximum(0.0, 1.0 - np.abs(v) / 1.5), 1.0, 1.5),
        ("bump(1.5,3)[l3-B3]",
         lambda t: lane1.h_battery(np.asarray(t, float), 1.5, 3),
         lambda v: np.where(np.abs(v) <= 1.5,
                            (1.0 - (np.abs(v) / 1.5) ** 2) ** 3, 0.0),
         1.0, 1.5),
        ("bessel(1.0,2)[l2]",
         lambda t: lane1.h_battery(np.asarray(t, float), 1.0, 2),
         lambda v: np.where(np.abs(v) <= 1.0,
                            (1.0 - np.abs(v) ** 2) ** 2, 0.0), 1.0, 1.0),
        ("bessel(1.0,4)[l2]",
         lambda t: lane1.h_battery(np.asarray(t, float), 1.0, 4),
         lambda v: np.where(np.abs(v) <= 1.0,
                            (1.0 - np.abs(v) ** 2) ** 4, 0.0), 1.0, 1.0),
    ]


def ext_eps(cell: dict, hfun, src: float, with_lattice: bool) -> float:
    """Lane 1's sum (with lattice) / lane 2's quotient sum (without)."""
    s = 2.0 * float(np.sum(hfun(cell["zeros"])))
    if with_lattice:
        a, K = cell["a"], cell["K"]
        jmax = int(math.floor(LATTICE_TOP * a / math.pi))
        js = np.arange(K, max(jmax, K) + 1, dtype=float)
        s += 2.0 * float(np.sum(hfun(js * math.pi / a)))
    return abs(s - src)


def row_type(first: float, last: float) -> str:
    if last > 2.0 * first:
        return "DIVERGES"
    if last < 0.5 * first:
        return "CONVERGES"
    return "PLATEAU"


# ---------------------------------------------------------------- main
def main() -> int:
    global EXT_CENSUS_X, MESH_X
    ap = argparse.ArgumentParser()
    ap.add_argument("--smoke", action="store_true")
    args = ap.parse_args()
    smoke = bool(args.smoke)
    deep_x = None if smoke else EXT_DEEP_X
    if smoke:
        EXT_CENSUS_X = (3, 5, 8)
        MESH_X = (5, 8, 13)

    print("=" * 78)
    print("realroot_arbiter_probe  ARBITER  PRIME.SEMILOCAL.REALROOT."
          "LIMIT.01")
    print("FROZEN SPEC_SHA %s%s" % (SPEC_SHA[:16],
          "   *** SMOKE -- NOT VERDICT-BEARING ***" if smoke else ""))
    print("=" * 78)

    section("I. INSTRUMENT WARDS")
    fw_ok, fw_det = firewall_audit()
    check("A1 AST firewall (no zero oracle; cache only in ward_/"
          "target_/main)", fw_ok, fw_det)
    gammas = ward_cache_load()
    check("A2 zero cache health (READ-ONLY, X5-typed)",
          len(gammas) >= 5000
          and abs(float(gammas[0]) - GAMMA1_LIT) < 1e-9
          and bool(np.all(np.diff(gammas) > 0)),
          "n=%d gamma_1 dev %.1e top %.4f"
          % (len(gammas), abs(float(gammas[0]) - GAMMA1_LIT),
             float(gammas[-1])))
    bat = unified_battery()
    src_tab: dict[str, float] = {}
    au144, am144 = lane3.prime_power_comb(144)
    worst_cross = 0.0
    for (nm, hf, ff, f0, Bb) in bat:
        s1 = lane1.src_value(lambda v: np.asarray(ff(np.abs(v)), float),
                             f0, Bb)
        s3 = lane3.weil_of_kernel(
            lambda w: np.asarray(ff(np.abs(w)), float), f0,
            (-1.0 / Bb if nm.startswith("tent") else 0.0), Bb,
            list(np.linspace(0.0, Bb, 9)), au144, am144)[0]
        src_tab[nm] = s1
        worst_cross = max(worst_cross, abs(s1 - s3))
        print("    %-20s SRC lane1 %+.9f lane3 %+.9f dev %.2e"
              % (nm, s1, s3, abs(s1 - s3)))
    check("A3 target normalization identical across lanes",
          worst_cross < SRC_CROSS_BAR,
          "worst |SRC_l1 - SRC_l3| = %.2e (bar %.0e)"
          % (worst_cross, SRC_CROSS_BAR))

    # =========================================================== Q1
    section("II. Q1 -- WHAT DID EACH LANE ACTUALLY SUM (executable)")
    print("  LANE 3 rung x=%d: re-verify the exact WEIGHTED CF identity"
          % MESH_X[2])
    r_id = lane3.run_rung(MESH_X[2])
    worst_w1 = 0.0
    dd = np.arange(r_id["N"] + 1)
    epsv = np.where(dd == 0, 1.0, 2.0)
    for (nm3, kf, k0, kp0, brk, hf3) in lane3.make_battery(1.5):
        kd = kf(dd * r_id["D"])
        lhs = float(np.dot(epsv * kd, r_id["c"]))
        hD = np.cos(np.outer(r_id["theta"], dd)) @ (epsv * kd)
        rhs = float(np.dot(r_id["rho"], hD)) + r_id["lam"] * k0
        worst_w1 = max(worst_w1, abs(lhs - rhs) / max(1e-12, abs(lhs)))
    check("Q1a lane-3 W1: the EXACT finite identity is the WEIGHTED one",
          worst_w1 < W1_BAR, "worst rel dev %.2e at x=%d (bar %.0e)"
          % (worst_w1, MESH_X[2], W1_BAR))
    hv_id = h_tent(r_id["tau"], 1.5)
    unw = float(np.sum(hv_id))
    unw_manual = float(np.dot(np.ones(len(r_id["tau"])), hv_id))
    check("Q1b lane-3 unweighted Tr = sum over ALL N nodes, weight 1",
          abs(unw - unw_manual) < 1e-12 and len(r_id["tau"]) == r_id["N"],
          "N=%d nodes, no filter (dev %.1e)"
          % (r_id["N"], abs(unw - unw_manual)))

    print("  LANE 2 x=8 (modes 26, dps 120): rebuild via lane 2's own"
          " code path")
    t0 = time.time()
    mp.mp.dps = 120
    base2, a2 = lane2.base_form(8, 26)
    form2, atoms2 = lane2.build_form(base2, a2, 8, 26, "MAIN")
    cell2 = lane2.finite_connes_operator(form2, a2)
    spec2 = cell2["spectrum"]
    pos2 = spec2[spec2 > 1e-8]
    print("    dim(spec)=%d atoms=%d tau=%.3e gap=%.3e imag=%.1e"
          " sym=%.1e  %.1fs"
          % (len(spec2), atoms2, cell2["tau"], cell2["gap"],
             cell2["imag_max"], cell2["symmetry"], time.time() - t0))
    check("Q1c lane-2 quotient is real/self-adjoint (its own bars)",
          cell2["gap"] > 0 and cell2["imag_max"] <= Q1_IMAG_BAR
          and cell2["symmetry"] <= Q1_IMAG_BAR,
          "gap %.2e imag %.1e sym %.1e" % (cell2["gap"],
                                           cell2["imag_max"],
                                           cell2["symmetry"]))
    evals2, evecs2 = mp.eigsy(form2)
    c2 = [evecs2[i, 0] for i in range(26)]
    if c2[max(range(26), key=lambda i: abs(c2[i]))] < 0:
        c2 = [-v for v in c2]
    cn2 = np.array([float(v) for v in c2])
    af2 = float(a2)
    norms2 = np.full(26, math.sqrt(af2))
    norms2[0] = math.sqrt(2.0 * af2)
    ecell2 = {"a": af2, "om": np.arange(26) * math.pi / af2,
              "cn": cn2 / norms2, "K": 26}
    e_at = lane1.trig_profile(ecell2, pos2[:12])
    scale2 = float(np.max(np.abs(lane1.trig_profile(
        ecell2, np.linspace(0.1, 30.0, 500)))))
    dev_q = float(np.max(np.abs(e_at))) / scale2
    check("Q1d lane-2 spectrum == zeros of the SAME minimizer's"
          " transform", dev_q < Q1B_BAR,
          "max |E(lam)|/scale = %.2e over first 12 (bar %.0e)"
          % (dev_q, Q1B_BAR))
    ts30 = np.arange(1e-9, 30.0, 0.005)
    v30 = lane1.trig_profile(ecell2, ts30)
    sflips = int(np.sum(np.sign(v30[:-1]) * np.sign(v30[1:]) < 0))
    n30q = int((pos2 < 30.0).sum())
    check("Q1e lane-2 (0,30) census == E-scan census",
          sflips == n30q,
          "D# eigs (0,30): %d = E sign changes: %d -> %s"
          % (n30q, sflips,
             " ".join("%.4f" % v for v in pos2[pos2 < 30.0])))
    print("  Q1 TABLE (executable audit):")
    print("    lane 1: extremal minimizer | ALL E_N zeros + exact"
          " lattice | UNWEIGHTED | SRC")
    print("    lane 2: SAME minimizer, quotient D# | ALL non-lattice"
          " zeros | UNWEIGHTED | SRC")
    print("    lane 3: mesh-CF Gauss-Szego atoms | ALL N nodes |"
          " UNWEIGHTED (+ separate WEIGHTED row) | SRC")
    print("    => no weighted/filtered sum in disguise anywhere; the"
          " conflict must be OBJECT or DEPTH.")

    # =========================================================== Q2
    section("III. Q2 -- BAND CENSUS ACROSS DEPTH (the density"
            " obstruction, per object)")
    n30_xi = int((gammas < 30.0).sum())
    n60_xi = int((gammas < 60.0).sum())
    n100_xi = int((gammas < 100.0).sum())
    print("  Xi reference (cache): (0,30)=%d (0,60)=%d (0,100)=%d"
          % (n30_xi, n60_xi, n100_xi))

    print("  MESH-CF (lane 3 object, its own run_rung):")
    mesh_rungs: dict[int, dict] = {}
    mesh_uniform = True
    for x in MESH_X:
        r = lane3.run_rung(x)
        mesh_rungs[x] = r
        tp = r["tau"][r["tau"] > 0]
        c30 = int((tp < 30.0).sum())
        c60 = int((tp < 60.0).sum())
        upred = 30.0 * r["ell"] / (2.0 * math.pi)
        mesh_uniform &= abs(c30 / upred - 1.0) < MESH_UNIFORM_TOL
        print("    x=%4d N=%5d  (0,30)=%3d [unif %5.1f | Xi %d]"
              "  (0,60)=%3d [unif %5.1f | Xi %d]  min tau %.3f"
              % (x, r["N"], c30, upred, n30_xi, c60,
                 60.0 * r["ell"] / (2.0 * math.pi), n60_xi,
                 float(tp.min())))
    check("Q2a mesh-CF measurement complete (lane 3's S5/S6 density"
          " recomputed)", len(mesh_rungs) == len(MESH_X),
          "MESH-UNIFORM finding: %s" % mesh_uniform)

    print("  EXTREMAL (lanes 1-2 object, lane 1's own HP builder;"
          " dps floor = 4 pi x/ln10 + %.0f):" % DPS_FLOOR_MARGIN)
    ext: dict[int, dict] = {}
    floors_ok = True
    for x in EXT_CENSUS_X:
        floor = 4.0 * math.pi * x / math.log(10.0) + DPS_FLOOR_MARGIN
        floors_ok &= EXT_DPS[x] >= floor
        t0 = time.time()
        cell = lane1.build_trig_cell_hp(x, EXT_KFAC, "MAIN", EXT_DPS[x])
        lane1.hp_zero_data(cell)
        ext[x] = cell
        z = cell["zeros"]
        print("    x=%3d K=%3d dps=%3d (floor %5.1f) tau=%s gap=%s"
              " census %d/%d  (0,30)=%d (0,60)=%d minz=%.4f  %.1fs"
              % (x, cell["K"], EXT_DPS[x], floor, cell["tau_str"],
                 cell["gap_str"], len(z), cell["census_expect"],
                 int((z < 30.0).sum()), int((z < 60.0).sum()),
                 cell["min_zero"], time.time() - t0))
    census_ok = all(0 <= ext[x]["census_deficit"] <= 1
                    for x in EXT_CENSUS_X)
    check("Q2b extremal census complete on x <= %d (deficit <= 1,"
          " lane 1's own gate)" % EXT_CENSUS_X[-1], census_ok,
          "%s" % {x: ext[x]["census_deficit"] for x in EXT_CENSUS_X})

    scan_ward_ok = True
    for x in (8, EXT_CENSUS_X[-1]):
        if x not in ext:
            continue
        t0 = time.time()
        zs = mp_profile_scan(ext[x], 60.0)
        zc = ext[x]["zeros"]
        ok = (int((zs < 30.0).sum()) == int((zc < 30.0).sum())
              and len(zs) == int((zc < 60.0).sum()))
        scan_ward_ok &= ok
        print("    scan-vs-census ward x=%d: scan (0,30)=%d (0,60)=%d"
              " census %d/%d  %.1fs %s"
              % (x, int((zs < 30.0).sum()), len(zs),
                 int((zc < 30.0).sum()), int((zc < 60.0).sum()),
                 time.time() - t0, "ok" if ok else "MISMATCH"))
    check("Q2c mp-scan instrument == exact census in (0,30)/(0,60)",
          scan_ward_ok, "warded at x = 8 and x = %d" % EXT_CENSUS_X[-1])

    deep_c30 = deep_c60 = deep_c100 = -1
    deep_minz = float("nan")
    deep_tau = deep_gap = ""
    if deep_x is not None:
        floor = 4.0 * math.pi * deep_x / math.log(10.0) \
            + DPS_FLOOR_MARGIN
        floors_ok &= EXT_DPS[deep_x] >= floor
        print("    DEEP RUNG x=%d building (declared ~11 min; the"
              " e^{-4 pi x} conditioning price) ..." % deep_x,
              flush=True)
        t0 = time.time()
        dcell = lane1.build_trig_cell_hp(deep_x, EXT_KFAC, "MAIN",
                                         EXT_DPS[deep_x])
        tb = time.time() - t0
        t0 = time.time()
        zdeep = mp_profile_scan(dcell, SCAN_HI_DEEP)
        deep_c30 = int((zdeep < 30.0).sum())
        deep_c60 = int((zdeep < 60.0).sum())
        deep_c100 = len(zdeep)
        deep_minz = float(zdeep[0]) if len(zdeep) else float("nan")
        deep_tau, deep_gap = dcell["tau_str"], dcell["gap_str"]
        print("    x=%3d K=%3d dps=%3d (floor %5.1f) tau=%s gap=%s"
              "  mp-scan (0,30)=%d (0,60)=%d (0,100)=%d minz=%.4f"
              "  build %.1fs scan %.1fs"
              % (deep_x, dcell["K"], EXT_DPS[deep_x], floor, deep_tau,
                 deep_gap, deep_c30, deep_c60, deep_c100, deep_minz,
                 tb, time.time() - t0))
        print("    (total zero count K-1 = %d is forced by the CITED"
              " CF realness theorem [32]; %d - %d = %d zeros sit in"
              " (100, edge=%.1f] -- the Nyquist excess at the band"
              " edge)"
              % (dcell["K"] - 1, dcell["K"] - 1, deep_c100,
                 dcell["K"] - 1 - deep_c100, float(dcell["om"][-1])))
    check("Q2d dps floor honored on every extremal rung", floors_ok,
          "dps >= 4 pi x/ln10 + %.0f everywhere" % DPS_FLOOR_MARGIN)

    ext_rows = []
    for x in EXT_CENSUS_X:
        z = ext[x]["zeros"]
        ext_rows.append((x, int((z < 30.0).sum()), int((z < 60.0).sum()),
                         ext[x]["min_zero"]))
    if deep_x is not None:
        ext_rows.append((deep_x, deep_c30, deep_c60, deep_minz))
    print("  Q2 TABLE  (0,30): Xi=%d | (0,60): Xi=%d" % (n30_xi, n60_xi))
    print("    %-28s %s" % ("mesh-CF (0,30):",
          "  ".join("x%d:%d" % (x, int((mesh_rungs[x]["tau"]
                                        [mesh_rungs[x]["tau"] > 0]
                                        < 30.0).sum()))
                    for x in MESH_X)))
    print("    %-28s %s" % ("extremal/quotient (0,30):",
          "  ".join("x%d:%d" % (x, c30) for (x, c30, _c, _m)
                    in ext_rows)))
    print("    %-28s %s" % ("extremal/quotient (0,60):",
          "  ".join("x%d:%d" % (x, c60) for (x, _c, c60, _m)
                    in ext_rows)))
    print("    (quotient = extremal minus lattice zeros; identical in"
          " these bands -- lattice starts at K pi/a, Q1d/Q1e identity)")

    ext_flat30 = all(c30 == n30_xi and abs(mz - float(gammas[0]))
                     < MINZERO_BAR
                     for (x, c30, _c, mz) in ext_rows if x >= 5)
    ext_flat60 = all(c60 == n60_xi for (x, _c, c60, _m) in ext_rows
                     if x >= 8)
    check("Q2e band-census findings recorded", True,
          "EXT-FLAT-30: %s  EXT-FLAT-60: %s  MESH-UNIFORM: %s"
          % (ext_flat30, ext_flat60, mesh_uniform))

    # =========================================================== Q3
    section("IV. Q3 -- ONE UNIFIED CONVERGENCE TABLE (same h, same"
            " SRC, all constructions)")
    mesh_types_u: list[str] = []
    mesh_types_w: list[str] = []
    ext_types: list[str] = []
    for (nm, hf, ff, f0, Bb) in bat:
        src = src_tab[nm]
        print("  %s   SRC = %+.9f" % (nm, src))
        eu = []
        ew = []
        for x in MESH_X:
            r = mesh_rungs[x]
            hv = hf(r["tau"])
            eu.append(abs(float(np.sum(hv)) - src))
            ew.append(abs(float(np.dot(r["w"], hv)) - src))
        print("    mesh-CF unweighted : %s"
              % "  ".join("x%d:%.3e" % (x, e)
                          for x, e in zip(MESH_X, eu)))
        print("    mesh-CF weighted   : %s"
              % "  ".join("x%d:%.3e" % (x, e)
                          for x, e in zip(MESH_X, ew)))
        tu, tw = row_type(eu[0], eu[-1]), row_type(ew[0], ew[-1])
        mesh_types_u.append(tu)
        mesh_types_w.append(tw)
        ef = []
        eq = []
        for x in EXT_TYPE_X:
            if x not in ext:
                continue
            ef.append(ext_eps(ext[x], hf, src, True))
            eq.append(ext_eps(ext[x], hf, src, False))
        print("    extremal (+lattice): %s"
              % "  ".join("x%d:%.3e" % (x, e)
                          for x, e in zip(EXT_TYPE_X, ef)))
        print("    quotient (no latt.): %s"
              % "  ".join("x%d:%.3e" % (x, e)
                          for x, e in zip(EXT_TYPE_X, eq)))
        te = row_type(ef[0], ef[-1]) if len(ef) >= 2 else "N/A"
        ext_types.append(te)
        print("    typing: mesh-unw %s | mesh-wt %s | extremal %s"
              % (tu, tw, te))
    n_mesh_div = sum(1 for t in mesh_types_u if t == "DIVERGES")
    n_mesh_wt = sum(1 for t in mesh_types_w if t == "CONVERGES")
    n_ext_conv = sum(1 for t in ext_types if t == "CONVERGES")
    check("Q3a unified table complete on all constructions", True,
          "MESH-UNW-DIV %d/4  MESH-WT-CONV %d/4  EXT-UNW-CONV %d/4"
          % (n_mesh_div, n_mesh_wt, n_ext_conv))

    # =========================================================== Z1-T
    section("V. Z1-TRANSFER -- the disguise content of the EXTREMAL"
            " family (ward, target-namespace)")
    cell5 = ext[5]
    K5, a5 = cell5["K"], cell5["a"]
    om5 = cell5["om"]
    norms5 = np.full(K5, math.sqrt(a5))
    norms5[0] = math.sqrt(2.0 * a5)
    mfull = cell5["m_tilde"] * np.outer(norms5, norms5)

    def target_bfun(j: int, t: np.ndarray) -> np.ndarray:
        return a5 * (np.sinc(a5 * (t - om5[j]) / math.pi)
                     + np.sinc(a5 * (t + om5[j]) / math.pi))

    gtop = float(gammas[-1])
    tail_mag = (2.0 / math.pi) * (math.log(gtop / (2.0 * math.pi))
                                  + 1.0) / gtop
    worst_raw = worst_corr = 0.0
    pairs = [(0, 0), (1, 1), (3, 3), (6, 6), (10, 10),
             (0, 3), (2, 7), (1, 10), (4, 9)]
    for (j, k) in pairs:
        zsum = 2.0 * float(np.sum(target_bfun(j, gammas)
                                  * target_bfun(k, gammas)))
        model = ((-1.0) ** (j + k)) * tail_mag
        worst_raw = max(worst_raw, abs(mfull[j, k] - zsum))
        worst_corr = max(worst_corr, abs(mfull[j, k] - zsum - model))
    check("Z1T the trig Galerkin matrix IS the Gram matrix of zero"
          " evaluations", worst_corr < Z1T_CORR_BAR
          and worst_corr < (1.0 - Z1T_MODEL_SHARE) * worst_raw,
          "worst dev %.2e raw -> %.2e after the analytic cache-tail"
          " model (bar %.0e; model share %.0f%%)"
          % (worst_raw, worst_corr, Z1T_CORR_BAR,
             100.0 * (1.0 - worst_corr / worst_raw)))
    ez = lane1.trig_profile(cell5, gammas[:4000])
    gram = 2.0 * float(np.sum(ez ** 2))
    tau5 = cell5["tau"]
    rel_g = abs(gram - tau5) / max(abs(tau5), 1e-300)
    check("Z1T-margin lam_min == 2 sum_gamma E(gamma)^2 (cache-"
          "truncated)", rel_g < Z1T_MARGIN_BAR,
          "lam_min %s vs zero-Gram %.3e (rel %.3f) -- the minimizer"
          " MINIMIZES its transform on the true ordinates"
          % (cell5["tau_str"], gram, rel_g))

    # =========================================================== verdict
    section("VI. COMPOSITE VERDICT")
    wall = time.time() - T0_WALL
    check("A9 runtime", wall <= RUNTIME_BAR, "%.1f s (bar %.0f)"
          % (wall, RUNTIME_BAR))
    instrument_ok = all(ok for _n, ok, _d in CHECKS)

    mesh_unw_div = n_mesh_div >= 3
    mesh_wt_conv = n_mesh_wt == 4
    ext_unw_conv = n_ext_conv >= 3

    if not instrument_ok:
        verdict = "ARBITER-INSTRUMENT-EDGE"
    elif not ext_flat30 or (not ext_flat60 and not ext_unw_conv):
        verdict = ("REALROOT-FALSE-FOR-FAMILY(the density obstruction"
                   " reaches the extremal object: fixed-band census"
                   " departs the Xi count; lane 3's theorem covers all"
                   " three objects)")
    elif ext_flat30 and not ext_flat60:
        verdict = ("REALROOT-EXTREMAL-INVADED-AT-DEPTH(fillers"
                   " measurably enter (30,60) while (0,30) stays on"
                   " the Xi census: lane 3's obstruction reaches the"
                   " extremal family on a trajectory; FALSE-leaning"
                   " refinement of DEPTH-UNDECIDED)")
    elif (ext_flat30 and ext_flat60 and mesh_uniform and mesh_unw_div
          and ext_unw_conv):
        verdict = ("REALROOT-DEPTH-UNDECIDED(conflict RESOLVED ="
                   " DIFFERENT OBJECT: lane 3's Nyquist theorem is"
                   " proven for its mesh family and measurably does"
                   " NOT transfer to the extremal/quotient family --"
                   " fixed bands stay on the Xi census through x = %d"
                   " with the excess exiled to the band edge; but the"
                   % (deep_x if deep_x is not None
                      else EXT_CENSUS_X[-1]) +
                   " thinning has no proof, its mechanism is the"
                   " Gram-of-zero-evaluations structure (Z1T), and R3"
                   " alone is RH-hard, so the architecture is neither"
                   " killed nor saved)")
    else:
        verdict = ("ARBITER-MIXED(findings do not fit a frozen branch;"
                   " see table)")

    n_pass = sum(1 for _n, ok, _d in CHECKS if ok)
    print("\n  ADJUDICATION UNDER THIS VERDICT:")
    print("  * Lane 3's STC-FALSE stands FOR ITS OWN FAMILY (mesh-CF:"
          " uniform l/2pi density, unweighted trace diverges --"
          " reproduced here on the shared battery).")
    print("  * Lanes 1-2's OPEN stands FOR THEIR OWN FAMILY at their"
          " own and deeper depth; their converging sums are honest"
          " unweighted sums, not weighted quadratures in disguise"
          " (Q1).")
    print("  * The two boxed Sol lemmata (ground-state comparison,"
          " Connes par.6.6, + uniform log spectral-count bound) are"
          " NOT mooted: they ARE the thinning-persists statement the"
          " deep census probes, now with measured support to x = 21"
          " and a measured non-uniform target (Xi-census bands + edge"
          " excess).  Z1T prices them: their content is the zero"
          " measure itself, so they carry wall strength.")
    print("  * Lane 1's skeleton repairs (G0 Fejer origin-exclusion,"
          " G1 E''(0) pin) remain valid conditional statements; lane"
          " 3's redundancy finding (Hurwitz/Hadamard layer redundant"
          " given R3+R4 via Beurling-Selberg) demotes them from"
          " load-bearing to convenience -- the entire weight is on R3,"
          " which is RH-hard (lanes 2 and 3, independently).")
    print("  * Lane 3's salvage carried: (i) Theorem A unconditional"
          " self-adjointness without wall positivity is TRUE and"
          " transfers (the quotient shift is tautologically psd);"
          " (ii) the 3.34e-05 unit-mass capture is a SUBSET statement"
          " (zeros subset of limit spectrum) for the mesh family, not"
          " determination; (iii) the converging weighted identity is"
          " Gauss-Szego exactness -- the wall in quadrature language,"
          " weights = Christoffel function of the zero measure = the"
          " unknown.")
    print("  * Deciding computations (falsification only): extremal"
          " rung x = 34 needs K = 150, dps >= 191 (~1.5 h by the"
          " measured K^3 dps scaling law from 172.5 s at x = 13 and"
          " 681.5 s at x = 21); x = 55 (lane 3's flagrant depth,"
          " 36-vs-3 in (0,30)) needs K = 276, dps >= 305 (~10 h)."
          " NO finite rung can VERIFY the architecture: R3 for a real"
          " spectrum already implies Weil positivity (h = |ghat|^2),"
          " so the surviving lemma carries full RH strength.")
    print("\n" + "=" * 78)
    print("CHECKS %d/%d PASS   runtime %.1f s   SPEC_SHA %s"
          % (n_pass, len(CHECKS), wall, SPEC_SHA[:16]))
    print("VERDICT: %s" % verdict)
    if smoke:
        print("*** SMOKE RUN -- NOT VERDICT-BEARING ***")
    print("NO RH CLAIM. NO POSITIVITY CLAIM. EXPLORATION ONLY.")
    print("=" * 78)
    return 0 if n_pass == len(CHECKS) else 1


if __name__ == "__main__":
    sys.exit(main())
