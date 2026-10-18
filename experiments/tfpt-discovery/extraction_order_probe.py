#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""extraction_order_probe -- PRIME.EXTRACTION.ORDER_REPAIR_FORK.01
(round 325): THE EXTRACTION-REPAIR FORK -- the measurable halves of
the three reviewer variants for repairing the RH connection seam
found by R319 (the rh/ cofinality runs in the ANCHOR direction;
the carrier hypothesis H_cof demands the MESH-refinement direction;
the window direction is MEASURED inadmissible there -- false floors
-2.114e-03 at D0 = 1/32 / -2.128e-04 at D0 = 1/128,
hcof_dodging_audit_probe S6.8).  This probe measures ONLY the
machine-checkable parts; the quantifier architecture itself is the
round's analytic deliverable (fork table, next.txt note).

THE THREE VARIANTS (reviewer, verbatim; measured halves per leg):
  A  ELEMENTWISE (per-test-function) STABILIZATION: for each f of a
     dense class a window sequence w_j(f) PREDEFINED FROM f with
     Q_{w_j(f)}(f) -> Q_Weil(f), ideally finite stabilization
     (exists j0(f): equality for all j >= j0(f)) -- the R310 form
     finite_forms_converge_to_weil generalized beyond the comb
     channel.  MEASURED HERE (S1): on the NATIVE dense class (dyadic
     step-function autocorrelations F = D0 * autocorr(x), the v749
     "Weil form of step functions" class, elements sealed by seed
     BEFORE any sign is read) the per-channel reads of the canonical
     tower windows (comb = atom tent lags, arch = Weil-kernel tent
     lags, pole) stabilize EXACTLY at the predicted finite onset
     alpha*(f) = (n_g + 1) D0 / 2 in the ANCHOR direction, and are
     CONSTANT under dyadic mesh refinement (no hidden mesh limit:
     the value at the element's native mesh IS the limit value).
  B  CANONICAL MESH REBUILD (no transport): the family
     w(a, h) = buildPrimeWindow(a, h) is built DIRECTLY at every
     mesh stage.  MEASURED HERE (S3): the v749 bridge reproduced --
     every deployed frame-A window IS a tower member at deviation
     0.0 (T1.4b class); the direct rebuild ladder at fixed anchor is
     PD at every dyadic stage (Levinson), with the honest falling
     relative margins; the dyadic lag-transport identity holds but
     is NOT consumed (variant B's point: no transport step).
  C  EXPLICIT QUADRATURE CORRECTION: Q_{a,h}(f) = Q_Weil(f) + E_h(f)
     with E controlled ON ITS OWN (hard rule: never divided through
     the shrinking wall margin -- no margin appears anywhere in this
     probe).  MEASURED HERE (S2): on a SEALED non-native test class
     (F1 tent with off-grid kink C^0, F2 quartic bump C^1, F3 Hann
     C^1; widths 1.7 / 2.3 / 2.9, fixed before any run) the
     per-channel defect E_ch(D, F) = L^D_ch(F) - R_ch(F) against
     mesh-independent references (comb: exact atom sum; arch/pole:
     Richardson-gated fine-mesh reads), its SIGN census, its dyadic
     decay ratios, and the RIGOROUS interpolation envelope
     |E_ch| <= (D^2/8) ||F''||_inf K_ch (K_comb = atom mass on the
     support, K_arch/pole = read-weighted absolute kernel mass) --
     an inequality gate consuming NO wall margin.  Plus the
     ANCHOR-ONLY FLOOR: at fixed mesh the anchor ladder stabilizes
     at a NONZERO E (the R319 false-floor mechanism on this probe's
     own elements).

THE OBJECT (v563/v716/v718/v749 machinery imported verbatim, zero
new constructors): U_ALL/MU_ALL (prime-power log nodes, von-Mangoldt
comb masses 2 Lambda(n)/sqrt(n)), atom_lags_at (T115 tent assembly),
arch_lags (exact Weil arch kernel vs tents, GL-48), pole_lags_closed
(v716), family_ext (v718 deployed frame-A family), the v749 tower
constructor c(D, X) = arch + atoms + pole at M = 2 alpha / D.  The
probe's single derived identity, used as the comb reference (proved
in-line by the tent algebra, gated at S1.3): the even lag read
L_cat(F) = F(0) c_0 + 2 sum_{d>=1} F(dD) c_d of the atom channel
equals -sum_n mu_n (I_D F)(u_n) EXACTLY, I_D = the piecewise-linear
interpolant on the D-grid -- so E_comb = -sum_n mu_n (I_D F - F)(u_n)
and E_comb == 0 identically on the native class (I_D F = F).

SEALED ADJUDICATION (frozen BEFORE the first full run; exactly one
primary letter; co-letters recorded independently):
  GATE_A: S1 all three channels stabilize exactly at the predicted
          onset on every sealed grid element (rel dev <= BAR_EXACT
          comb / BAR_GL arch+pole above onset, > ONSET_MIN below),
          AND mesh-constancy across two dyadic refinements
          (<= BAR_EXACT comb, <= BAR_GL arch/pole),
          AND the comb read identity vs the exact atom sum
          (<= BAR_EXACT).
  GATE_B: S3 deployed-window tower membership rel dev <= BAR_MEMBER
          on all three picked windows AND the direct rebuild ladder
          PD (Levinson, no breakdown, min E > 0) at every stage.
  GATE_C: S2 on every C^2 element (F2, F3), every mesh stage and
          every channel: |E_ch| <= envelope_ch + ABS_GL,
          AND every dyadic PER-CHANNEL defect ratio >= RATIO_DOWN
          (denominators below 1e-13 scale: stage skipped, disclosed;
          the TOTAL ratio is reported, not gated -- the smoke run
          measured comb/arch sign opposition that cancels in the
          total, an honest structural record).
          Subtype SIGN iff each channel's E carries ONE sign across
          all C^2 elements and stages, else subtype RATE.
  FLOOR:  at fixed D = 1/32 the anchor sweep stabilizes
          (|E(a_last) - E(a_prev)| <= 0.01 |E(a_last)|) at
          |E| > FLOOR_MIN on every smooth element.
  Primary: ELEMENTWISE_STABILIZATION_GO iff GATE_A; else
  CANONICAL_MESH_REBUILD_GO iff GATE_B; else
  SIGNED_DEFECT_CORRECTION_GO iff GATE_C; else
  ANCHOR_ONLY_INSUFFICIENT iff FLOOR; else
  NO_EXTRACTION_ARCHITECTURE.
  Co-letters: CANONICAL_MESH_REBUILD_GO iff GATE_B;
  SIGNED_DEFECT_CORRECTION_GO(SIGN|RATE) iff GATE_C;
  ANCHOR_ONLY_INSUFFICIENT iff FLOOR.
  The "comb exactly 0" reviewer parenthesis is adjudicated as a
  two-prong gate (S2.3): E_comb == 0 on the native class AND
  E_comb != 0 on the smooth class (the parenthesis holds exactly on
  the native class and FAILS off it -- whichever way it measures).

SEALED BARS: BAR_EXACT = 1e-12 (relative; float-exact identities),
BAR_GL = 5e-9 (the v749 BAR_REFINE GL-48 tolerance), BAR_MEMBER =
1e-13 (v749 T1.4b class), ONSET_MIN = 1e-6 (a truncated read must
differ), BAR_RICH = 1e-6 (Richardson reference gap), RATIO_DOWN = 1.8
(strict per-channel dyadic fall; the D^2 class value 4 is the
reported reference), FLOOR_MIN = 1e-9, ABS_GL = 1e-7 (additive GL
slack on the envelope gate).

MUST-FAILS (>= 3; all sealed with the tree):
  m1 ANCHOR-ONLY ADVERSARY: the claim "the fixed-mesh anchor ladder
     reaches Q_Weil" (|E_tot| <= 1e-9 scale at the deepest anchor,
     D = 1/32, on a smooth element) must FAIL -- the false-floor
     guard fires.
  m2 BROKEN TENT EXACTNESS: a nearest-neighbour read (instead of the
     linear-interpolation read) on a native grid element must
     violate the comb exactness bar.
  m3 CORRUPTED TRANSPORT: the dyadic lag identity with full (not
     half) neighbour weights must violate BAR_GL.
  m4 MEMBERSHIP CORRUPTION: a 1e-6 perturbation of one deployed lag
     must violate BAR_MEMBER.

PROTOCOL: deterministic (seeded elements, no data downloads);
run1/run2 identical up to WALL; --smoke = reduced config (one grid
element, F2 only, two meshes, coarser references), same gates.
Record tables are inserted AFTER the first full run (r316/r317
protocol; the insertion is the only post-freeze change).
SMOKE-HARNESS FIXES (disclosed, all BEFORE the first full run =
the freeze; r318 class): (1) the grid-element constructor omitted
the closing zero knot -- np.interp created a jump at the last knot
and the kernel-channel midpoint reads across that cell were wrong
by ~1e-6 (the dyadic lag identity itself measured machine-exact,
arch 1.1e-16 / pole 0.0); (2) the decay gate retyped from the
total defect to PER-CHANNEL ratios after the smoke run measured
comb/arch sign opposition cancelling in the total (recorded as a
finding, not gated away); (3) a smoke-config index bug in S2.3.

RECORD (2026-08-27, inserted after the first full run per the
r316/r317 protocol -- this insertion is the only post-freeze
change; freeze-run SPEC_SHA 57e50d366a62f2a6, all numbers below
byte-identical on run1/run2 after insertion):
  S1 anchor-onset (comb rel dev to the deep reference):
    g1 (seed 11, n_g 48, D0 1/32, a* 0.766):
       a=0.35: 2.65e-02 | 0.55: 6.10e-03 | 1.0/2.0/3.0: 3.3e-18
    g2 (seed 12, n_g 40, D0 1/32, a* 0.641):
       a=0.35: 5.34e-02 | 0.55: 4.92e-02 | 1.0/2.0/3.0: 0.0
    g3 (seed 13, n_g 96, D0 1/64, a* 0.758):
       a=0.35: 1.76e-02 | 0.55: 2.04e-02 | 1.0/2.0/3.0: 1.7e-18
    mesh constancy D0 -> D0/2 -> D0/4 (worst): comb 3.3e-18,
    arch 1.5e-15, pole 2.0e-17 -- the native mesh IS the limit
  S2 defect E_ch(D, F) at alpha 2.5 (sign carried):
    F1_tent (C^0, L=1.7; report only): comb +2.2e-16 EXACTLY 0 --
       the off-grid kink cells contain NO prime-power atom (honest
       fluke, recorded); arch -6.09e-05 -> -1.02e-05 -> -3.81e-06;
       pole +3.82e-04 -> +6.35e-05 -> +2.38e-05
    F2_quartic (C^2, L=2.3): comb -3.00e-04 -> -4.97e-05 ->
       -5.52e-06 (ratios 6.05, 9.01); arch +3.67e-04 -> +1.02e-04
       -> +2.82e-05 (3.58, 3.63); pole +1.11e-04 -> +2.71e-05 ->
       +6.82e-06 (4.10, 3.97); total ratios 2.22, 2.70 (reported)
    F3_hann (C^2, L=2.9): comb -2.69e-04 -> -6.67e-05 -> -1.15e-05
       (4.03, 5.81); arch +2.91e-04 -> +8.11e-05 -> +2.23e-05
       (3.59, 3.63); pole +1.36e-04 -> +3.39e-05 -> +8.42e-06
       (4.03, 4.02); total ratios 3.29, 2.51 (reported)
    sign census (C^2, all stages): comb NEGATIVE, arch POSITIVE,
       pole POSITIVE, total POSITIVE -> subtype SIGN; the comb/arch
       opposition cancels in the total (the reported-only ratios)
    anchor floor (D=1/32, a = 2.0/2.5/3.0/3.5): E_tot CONSTANT at
       +1.77e-04 (F2) / +1.59e-04 (F3) -- stable and nonzero
    comb two-prong: native 6.9e-18 (exactly 0) vs smooth 3.00e-04
  S3: membership rel dev 0.0 / 0.0 / 0.0 (deployed picks 0/mid/
    last); rebuild ladder alpha 2.5, D = 1/64 -> 1/128 -> 1/256:
    PD 3/3, lambda_min/c_0 = 1.33e-05 -> 3.34e-06 -> 6.92e-07
    (falling, reported not consumed); transport identity 8.0e-17
  VERDICT: primary ELEMENTWISE_STABILIZATION_GO; co-letters
    CANONICAL_MESH_REBUILD_GO + SIGNED_DEFECT_CORRECTION_GO(SIGN)
    + ANCHOR_ONLY_INSUFFICIENT; must-fails m1-m4 all CAUGHT
    (6.5e-02 / 1.5e-01 / 4.4e-07 against their bars).
    18/18 gates PASS, 0.4 s full / 0.2 s smoke.

EXPLORATION ONLY (2026-08-27).  experiments/ level: NO promotion,
NO ledger row, NO marker moved, NO RH CLAIM in either direction.
Coexistence: the wave-12 worker (v969) and R324 (QMAX x M_2) run in
parallel; this probe touches nothing outside its own file and the
strictly additive rh-sync.
"""

import argparse
import ast
import hashlib
import math
import os
import sys
import time

import numpy as np
import scipy.linalg as sla

_here = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _here)
sys.path.insert(0, os.path.abspath(os.path.join(_here, "..", "..",
                                                "verification")))

import v563_paper2_readouts as core            # noqa: E402
import v716_moonshot_arch_glue as stage2       # noqa: E402
import v718_moonshot_spectral as stage4        # noqa: E402
import v696_z1_jacobi as jac                   # noqa: E402

SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
T0_WALL = time.time()
CHECKS: list = []

# ---------------------------------------------------------- sealed bars
BAR_EXACT = 1.0e-12     # float-exact identities (relative)
BAR_GL = 5.0e-9         # GL-48 arch tolerance (v749 BAR_REFINE)
BAR_MEMBER = 1.0e-13    # tower membership (v749 T1.4b class)
ONSET_MIN = 1.0e-6      # below-onset reads must genuinely differ
BAR_RICH = 1.0e-6       # Richardson reference gap (relative)
RATIO_DOWN = 1.8        # strict per-channel dyadic fall (4 = D^2 ref)
FLOOR_MIN = 1.0e-9      # anchor floor must be genuinely nonzero
ABS_GL = 1.0e-7         # additive GL slack on the envelope gate

# ------------------------------------------------------- sealed configs
# S1 native grid elements: (seed, n_g, D0); support n_g * D0,
# predicted onset alpha* = (n_g + 1) * D0 / 2.
GRID_ELEMENTS = ((11, 48, 1.0 / 32.0),
                 (12, 40, 1.0 / 32.0),
                 (13, 96, 1.0 / 64.0))
ALPHA_SWEEP = (0.35, 0.55, 1.0, 2.0, 3.0)
ALPHA_MESHCONST = 2.0

# S2 non-native sealed class: (name, kind, half-width L, ||F''||_inf
# or None for C^0).  Widths chosen off-grid on every dyadic mesh.
SMOOTH_ELEMENTS = (("F1_tent", "tent", 1.7, None),
                   ("F2_quartic", "quartic", 2.3, 8.0 / 2.3 ** 2),
                   ("F3_hann", "hann", 2.9, math.pi ** 2 / (2 * 2.9 ** 2)))
ALPHA_C = 2.5
MESHES_C = (1.0 / 32.0, 1.0 / 64.0, 1.0 / 128.0)
ALPHA_FLOOR = (2.0, 2.5, 3.0, 3.5)

# S3 rebuild ladder
ALPHA_B = 2.5
MESHES_B = (1.0 / 64.0, 1.0 / 128.0, 1.0 / 256.0)


def check(name, ok, detail=""):
    ok = bool(ok)
    CHECKS.append((name, ok, detail))
    print("  [%s] %-46s %s" % ("PASS" if ok else "FAIL", name, detail),
          flush=True)
    return ok


def info(msg):
    print("  [INFO] " + msg, flush=True)


def section(t):
    print("\n" + "-" * 78 + "\n" + t + "\n" + "-" * 78, flush=True)


# ---------------------------------------------------------- constructors
def channel_lags(D, alpha):
    """The v749 tower member at (D, X = e^{2 alpha}), per channel:
    M = 2 alpha / D lags; comb = T115 tent assembly of the atoms
    n <= e^{2 al}; arch = exact Weil-kernel tent integrals (GL-48);
    pole = v716 closed form.  Verbatim constructor chain."""
    M = int(round(2.0 * alpha / D))
    al = 0.5 * M * D
    ka = core.atoms_in(al)
    cat, _dd = core.atom_lags_at(al, M, core.U_ALL[:ka], core.MU_ALL[:ka])
    car = core.arch_lags(M, D)
    cp = stage2.pole_lags_closed(M, D)
    return dict(M=M, al=al, ka=ka, cat=cat, car=car, cp=cp)


def read_lags(c, D, F, Lsup):
    """The even lag read L_c(F) = F(0) c_0 + 2 sum_{d>=1} F(dD) c_d,
    truncated at the support (F == 0 beyond Lsup)."""
    dmax = min(len(c), int(math.floor(Lsup / D)) + 3)
    dd = np.arange(dmax, dtype=float) * D
    vals = F(dd)
    return float(vals[0] * c[0] + 2.0 * float(vals[1:] @ c[1:dmax]))


def grid_element(seed, ng, D0):
    """A native element: F = D0 * autocorr(x) of a seeded step
    function on the D0-grid -- piecewise linear with knots on the
    grid, support [-(ng) D0, ng D0].  Sealed BEFORE any sign read."""
    rng = np.random.default_rng(seed)
    x = rng.standard_normal(ng)
    a = np.append(np.correlate(x, x, "full")[ng - 1:] * D0, 0.0)
    knots = np.arange(ng + 1, dtype=float) * D0   # closing zero knot

    def F(u):
        return np.interp(np.abs(np.asarray(u, dtype=float)), knots, a,
                         right=0.0)
    return F, float(ng * D0)


def smooth_element(kind, L):
    """The sealed non-native class: even, compactly supported on
    [-L, L], evaluated exactly (closed forms)."""
    if kind == "tent":
        def F(u):
            t = np.abs(np.asarray(u, dtype=float)) / L
            return np.maximum(0.0, 1.0 - t)
    elif kind == "quartic":
        def F(u):
            t = np.abs(np.asarray(u, dtype=float)) / L
            v = np.maximum(0.0, 1.0 - t * t)
            return v * v
    elif kind == "hann":
        def F(u):
            t = np.abs(np.asarray(u, dtype=float)) / L
            return np.where(t < 1.0,
                            0.5 * (1.0 + np.cos(math.pi
                                                * np.minimum(t, 1.0))), 0.0)
    else:
        raise ValueError(kind)
    return F


def comb_ref(F, alpha_eff):
    """The exact comb reference -sum_n mu_n F(u_n) over the window
    atom set n <= e^{2 al} (mesh-free; the derived tent identity
    makes L_cat(F) = -sum_n mu_n (I_D F)(u_n))."""
    ka = core.atoms_in(alpha_eff)
    return -float(core.MU_ALL[:ka] @ F(core.U_ALL[:ka]))


def kernel_ref_lags(D_ref, Lsup, builder):
    """Fine-mesh kernel lags over the support only (reference)."""
    M = int(math.floor(Lsup / D_ref)) + 4
    return builder(M, D_ref)


# ------------------------------------------------------------ G0 firewall
def g0_firewall():
    section("G0  FIREWALL")
    src = open(os.path.abspath(__file__), "r", encoding="utf-8").read()
    tree = ast.parse(src)
    forb = {"zeta" + "zero", "n" + "zeros", "prime" + "range",
            "is" + "prime", "gram" + "point", "prime" + "pi"}
    bad = []
    for node in ast.walk(tree):
        nm = node.attr if isinstance(node, ast.Attribute) else (
            node.id if isinstance(node, ast.Name) else None)
        if nm and nm.lower() in forb:
            bad.append("%s@%d" % (nm, node.lineno))
    check("G0.1 zero/prime-oracle-free", not bad,
          "constructors = v563 sieve + v563/v716 kernels only"
          if not bad else "; ".join(bad))
    fitfrags = ("poly" + "fit", "curve_" + "fit", "lst" + "sq",
                "mini" + "mize")
    hits = []
    for node in ast.walk(tree):
        nm = None
        if isinstance(node, ast.Attribute):
            nm = node.attr
        elif isinstance(node, ast.Name):
            nm = node.id
        if nm and any(f in nm for f in fitfrags):
            hits.append("%s@%d" % (nm, node.lineno))
    check("G0.2 no fitting anywhere", not hits,
          "decay ratios are raw quotients, envelopes closed-form"
          if not hits else "; ".join(hits))


# ================================================================== S1
def s1_elementwise(cfg):
    """VARIANT A measured half: per-channel finite stabilization on
    the native class, in the anchor direction, at the PREDICTED
    onset; plus mesh-constancy (no hidden refinement)."""
    section("S1  VARIANT A -- ELEMENTWISE STABILIZATION (native class)")
    ok_onset = True
    ok_below = True
    ok_exact = True
    rows = []
    for (seed, ng, D0) in cfg["grid_elements"]:
        F, Lsup = grid_element(seed, ng, D0)
        astar = (ng + 1) * D0 / 2.0
        # reference: exact atom sum at the deepest sweep anchor
        ch_deep = channel_lags(D0, cfg["alpha_sweep"][-1])
        ref_comb = comb_ref(F, ch_deep["al"])
        ref_arch = read_lags(ch_deep["car"], D0, F, Lsup)
        ref_pole = read_lags(ch_deep["cp"], D0, F, Lsup)
        sc = max(abs(ref_comb), abs(ref_arch), abs(ref_pole), 1.0e-6)
        # comb tent-exactness at the deep anchor (the derived identity)
        dev_id = abs(read_lags(ch_deep["cat"], D0, F, Lsup)
                     - ref_comb) / sc
        ok_exact &= dev_id <= BAR_EXACT
        devs = []
        for a in cfg["alpha_sweep"]:
            ch = channel_lags(D0, a)
            dc = abs(read_lags(ch["cat"], D0, F, Lsup) - ref_comb) / sc
            da = abs(read_lags(ch["car"], D0, F, Lsup) - ref_arch) / sc
            dp = abs(read_lags(ch["cp"], D0, F, Lsup) - ref_pole) / sc
            devs.append((a, dc, da, dp))
            if a >= astar + D0:
                ok_onset &= max(dc, da, dp) <= max(BAR_EXACT, BAR_GL)
            elif 2.0 * ch["al"] < Lsup - D0:
                ok_below &= max(dc, da, dp) > ONSET_MIN
        rows.append("g(seed %d, n_g %d, D0 1/%d, a* %.3f): comb %s "
                    "| tent-id %.1e"
                    % (seed, ng, int(round(1.0 / D0)),
                       astar,
                       ", ".join("a=%g: %.2e" % (a, dc)
                                 for (a, dc, _da, _dp) in devs), dev_id))
    for r in rows:
        info(r)
    check("S1.1 finite anchor stabilization EXACT", ok_onset,
          "all channels, every element, every anchor >= alpha* + D0: "
          "rel dev <= %.0e (comb) / %.0e (arch,pole) -- the R310 "
          "finite_forms_converge_to_weil shape holds for ALL channels "
          "on the native class" % (BAR_EXACT, BAR_GL))
    check("S1.2 below-onset reads genuinely differ", ok_below,
          "truncated windows (2 al < support) deviate > %.0e -- the "
          "onset is real, not vacuous" % ONSET_MIN)
    check("S1.3 comb tent-read identity", ok_exact,
          "L_cat(F) == -sum_n mu_n (I_D F)(u_n) == -sum_n mu_n F(u_n) "
          "on the native class (I_D F = F), rel dev <= %.0e" % BAR_EXACT)

    # mesh constancy: refining the mesh does not move the value
    ok_mc_comb = True
    ok_mc_kern = True
    worst = dict(comb=0.0, arch=0.0, pole=0.0)
    for (seed, ng, D0) in cfg["grid_elements"]:
        F, Lsup = grid_element(seed, ng, D0)
        base = channel_lags(D0, cfg["alpha_meshconst"])
        v0 = dict(comb=read_lags(base["cat"], D0, F, Lsup),
                  arch=read_lags(base["car"], D0, F, Lsup),
                  pole=read_lags(base["cp"], D0, F, Lsup))
        sc = max(*[abs(v) for v in v0.values()], 1.0e-6)
        for k in (2, 4):
            ch = channel_lags(D0 / k, cfg["alpha_meshconst"])
            dc = abs(read_lags(ch["cat"], D0 / k, F, Lsup)
                     - v0["comb"]) / sc
            da = abs(read_lags(ch["car"], D0 / k, F, Lsup)
                     - v0["arch"]) / sc
            dp = abs(read_lags(ch["cp"], D0 / k, F, Lsup)
                     - v0["pole"]) / sc
            worst["comb"] = max(worst["comb"], dc)
            worst["arch"] = max(worst["arch"], da)
            worst["pole"] = max(worst["pole"], dp)
            ok_mc_comb &= dc <= BAR_EXACT
            ok_mc_kern &= max(da, dp) <= BAR_GL
    check("S1.4 mesh constancy (no hidden refinement)", 
          ok_mc_comb and ok_mc_kern,
          "native value CONSTANT under D0 -> D0/2 -> D0/4: comb %.1e "
          "(exact), arch %.1e, pole %.1e (GL) -- the element's native "
          "mesh already carries the limit value"
          % (worst["comb"], worst["arch"], worst["pole"]))
    return dict(ok=(ok_onset and ok_below and ok_exact
                    and ok_mc_comb and ok_mc_kern))


# ================================================================== S2
def s2_defect(cfg):
    """VARIANT C measured half: the per-channel quadrature defect
    E_ch(D, F) on the sealed non-native class, its sign census, its
    dyadic decay, the rigorous interpolation envelope, and the
    anchor-only floor."""
    section("S2  VARIANT C -- QUADRATURE DEFECT (non-native class)")
    D_fine = min(cfg["meshes_c"])
    Lmax = max(t[2] for t in cfg["smooth_elements"])
    # Richardson-gated kernel references over the support
    dref1, dref2 = D_fine / cfg["ref_div"], D_fine / (2 * cfg["ref_div"])
    car1 = kernel_ref_lags(dref1, Lmax, core.arch_lags)
    car2 = kernel_ref_lags(dref2, Lmax, core.arch_lags)
    cp1 = kernel_ref_lags(dref1, Lmax, stage2.pole_lags_closed)
    cp2 = kernel_ref_lags(dref2, Lmax, stage2.pole_lags_closed)
    ok_rich = True
    for (_name, kind, L, _f2) in cfg["smooth_elements"]:
        F = smooth_element(kind, L)
        for (ca, cb, dpa, dpb) in ((car1, car2, dref1, dref2),
                                   (cp1, cp2, dref1, dref2)):
            r1 = read_lags(ca, dpa, F, L)
            r2 = read_lags(cb, dpb, F, L)
            ok_rich &= abs(r1 - r2) <= BAR_RICH * max(1.0, abs(r2))
    check("S2.0 Richardson reference gate", ok_rich,
          "arch/pole references at D_ref = %.1e vs %.1e agree to "
          "<= %.0e rel on every element" % (dref1, dref2, BAR_RICH))

    # read-weighted absolute kernel masses for the envelopes
    def abs_mass(c, D_ref, L):
        dmax = min(len(c), int(math.floor(L / D_ref)) + 3)
        return float(abs(c[0]) + 2.0 * np.sum(np.abs(c[1:dmax])))

    ok_env = True
    ok_ratio = True
    sign_tab = dict(comb=set(), arch=set(), pole=set(), tot=set())
    e_records = {}
    for (name, kind, L, f2max) in cfg["smooth_elements"]:
        F = smooth_element(kind, L)
        r_arch = read_lags(car2, dref2, F, L)
        r_pole = read_lags(cp2, dref2, F, L)
        e_by_mesh = []
        for D in cfg["meshes_c"]:
            ch = channel_lags(D, cfg["alpha_c"])
            r_comb = comb_ref(F, ch["al"])
            ec = read_lags(ch["cat"], D, F, L) - r_comb
            ea = read_lags(ch["car"], D, F, L) - r_arch
            ep = read_lags(ch["cp"], D, F, L) - r_pole
            e_by_mesh.append((D, ec, ea, ep, ec + ea + ep))
            if f2max is not None:
                ka = core.atoms_in(ch["al"])
                inside = core.U_ALL[:ka] <= L + D
                k_comb = float(np.sum(core.MU_ALL[:ka][inside]))
                env = (D * D / 8.0) * f2max
                ok_env &= abs(ec) <= env * k_comb + ABS_GL
                ok_env &= abs(ea) <= env * abs_mass(car2, dref2, L) + ABS_GL
                ok_env &= abs(ep) <= env * abs_mass(cp2, dref2, L) + ABS_GL
                for key, val in (("comb", ec), ("arch", ea),
                                 ("pole", ep), ("tot", ec + ea + ep)):
                    sign_tab[key].add(1 if val > 0 else -1)
        e_records[name] = e_by_mesh
        info("%s (L=%.1f): %s" % (name, L, " | ".join(
            "D=1/%d: comb %+.2e arch %+.2e pole %+.2e"
            % (int(round(1.0 / D)), ec, ea, ep)
            for (D, ec, ea, ep, _et) in e_by_mesh)))
        if f2max is not None:
            sc = max(abs(r_arch), abs(r_pole), 1.0e-6)
            for i in range(len(e_by_mesh) - 1):
                rr = []
                for j, chn in ((1, "comb"), (2, "arch"), (3, "pole")):
                    num = abs(e_by_mesh[i][j])
                    den = abs(e_by_mesh[i + 1][j])
                    if den > 1.0e-13 * sc:
                        ratio = num / den
                        ok_ratio &= ratio >= RATIO_DOWN
                        rr.append("%s %.2f" % (chn, ratio))
                    else:
                        rr.append("%s skipped" % chn)
                tot_r = (abs(e_by_mesh[i][4]) / abs(e_by_mesh[i + 1][4])
                         if abs(e_by_mesh[i + 1][4]) > 1.0e-13 * sc
                         else float("nan"))
                info("  %s dyadic ratios D=1/%d -> 1/%d: %s "
                     "(total %.2f, reported only)"
                     % (name, int(round(1.0 / e_by_mesh[i][0])),
                        int(round(1.0 / e_by_mesh[i + 1][0])),
                        ", ".join(rr), tot_r))
    check("S2.1 rigorous envelope holds (C^2 elements)", ok_env,
          "|E_ch| <= (D^2/8) ||F''|| K_ch + %.0e on every channel/"
          "stage -- the defect is controlled ON ITS OWN (closed-form "
          "interpolation bound; no wall margin anywhere)" % ABS_GL)
    check("S2.2 per-channel dyadic fall >= %.1f (C^2)" % RATIO_DOWN,
          ok_ratio, "every channel's defect falls strictly at every "
          "dyadic step (D^2 reference value 4; the TOTAL ratio is "
          "reported only -- comb/arch sign opposition cancels there)")
    one_signed = all(len(sign_tab[k]) == 1
                     for k in ("comb", "arch", "pole"))
    subtype = "SIGN" if one_signed else "RATE"
    info("sign census (C^2): comb %s arch %s pole %s tot %s -> "
         "subtype %s"
         % tuple([sorted(sign_tab[k]) for k in
                  ("comb", "arch", "pole", "tot")] + [subtype]))

    # the comb two-prong ("comb exactly 0" adjudication)
    (seed, ng, D0) = cfg["grid_elements"][0]
    Fg, Lg = grid_element(seed, ng, D0)
    chg = channel_lags(D0, cfg["alpha_c"])
    e_native = abs(read_lags(chg["cat"], D0, Fg, Lg)
                   - comb_ref(Fg, chg["al"]))
    name2, kind2, L2, _ = cfg["smooth_elements"][min(
        1, len(cfg["smooth_elements"]) - 1)]
    F2 = smooth_element(kind2, L2)
    ch2 = channel_lags(cfg["meshes_c"][0], cfg["alpha_c"])
    e_smooth = abs(read_lags(ch2["cat"], cfg["meshes_c"][0], F2, L2)
                   - comb_ref(F2, ch2["al"]))
    check("S2.3 comb two-prong", 
          e_native <= BAR_EXACT and e_smooth > 1.0e-6,
          "E_comb native %.1e (exactly 0) vs smooth %.2e (NOT 0) -- "
          "the reviewer parenthesis 'comb exactly 0' holds ONLY on "
          "the native class" % (e_native, e_smooth))

    # anchor-only floor
    ok_floor = True
    for (name, kind, L, f2max) in cfg["smooth_elements"]:
        if f2max is None:
            continue
        F = smooth_element(kind, L)
        r_arch = read_lags(car2, dref2, F, L)
        r_pole = read_lags(cp2, dref2, F, L)
        es = []
        for a in cfg["alpha_floor"]:
            ch = channel_lags(cfg["meshes_c"][0], a)
            et = (read_lags(ch["cat"], cfg["meshes_c"][0], F, L)
                  - comb_ref(F, ch["al"])
                  + read_lags(ch["car"], cfg["meshes_c"][0], F, L)
                  - r_arch
                  + read_lags(ch["cp"], cfg["meshes_c"][0], F, L)
                  - r_pole)
            es.append(et)
        stab = abs(es[-1] - es[-2]) <= 0.01 * abs(es[-1])
        ok_floor &= stab and abs(es[-1]) > FLOOR_MIN
        info("%s anchor sweep (D=1/%d): E_tot %s -> floor %s"
             % (name, int(round(1.0 / cfg["meshes_c"][0])),
                ", ".join("%+.2e" % e for e in es),
                "STABLE-NONZERO" if stab and abs(es[-1]) > FLOOR_MIN
                else "?"))
    check("S2.4 anchor-only floor reproduced", ok_floor,
          "at fixed mesh the anchor ladder stabilizes at a NONZERO "
          "defect (> %.0e) -- the R319 false-floor mechanism on this "
          "probe's own elements: the anchor direction cannot repair "
          "the mesh defect" % FLOOR_MIN)
    return dict(ok_env=ok_env, ok_ratio=ok_ratio, ok_rich=ok_rich,
                subtype=subtype, ok_floor=ok_floor,
                gate_c=(ok_rich and ok_env and ok_ratio),
                records=e_records)


# ================================================================== S3
def s3_rebuild(cfg):
    """VARIANT B measured half: tower membership of the deployed
    windows (v749 T1.4b class), direct-rebuild ladder PD, and the
    (unconsumed) dyadic transport identity."""
    section("S3  VARIANT B -- CANONICAL MESH REBUILD")
    wins = stage4.family_ext()
    picks = ([wins[0]] if cfg["smoke"]
             else [wins[0], wins[len(wins) // 2], wins[-1]])
    ok_mem = True
    devs = []
    for w in picks:
        ch = channel_lags(w["D"], w["alpha"])
        c_tw = ch["car"] + ch["cat"] + ch["cp"]
        sc = float(np.max(np.abs(w["p"])))
        dev = float(np.max(np.abs(c_tw[:w["M"]] - w["p"]))) / sc
        devs.append(dev)
        ok_mem &= dev <= BAR_MEMBER
    check("S3.1 deployed windows ARE rebuilt members", ok_mem,
          "lag vector == direct constructor at (D_w, alpha_w), rel "
          "dev %s (v749 T1.4b reproduced: NO transport is needed to "
          "reach any deployed window)"
          % ", ".join("%.1e" % d for d in devs))

    ok_pd = True
    margins = []
    for D in cfg["meshes_b"]:
        ch = channel_lags(D, cfg["alpha_b"])
        c = ch["car"] + ch["cat"] + ch["cp"]
        ks, Es, bd = jac.levinson(c, len(c) - 1)
        pd = (bd is None) and float(np.min(Es)) > 0.0
        ok_pd &= pd
        lam = float(np.min(np.linalg.eigvalsh(sla.toeplitz(c))))
        margins.append("D=1/%d: PD %s, lambda_min/c_0 %.2e"
                       % (int(round(1.0 / D)), pd, lam / c[0]))
    check("S3.2 direct rebuild ladder PD per stage", ok_pd,
          "%s -- every stage carries its own PSD certificate (the "
          "variant-B premise measured; the falling relative margin "
          "is the honest price, reported not consumed" 
          % "; ".join(margins))

    # transport identity: exists, measured, NOT consumed by B
    dev_lag = 0.0
    Dc, Df = cfg["meshes_b"][0], cfg["meshes_b"][1]
    cc = channel_lags(Dc, cfg["alpha_b"])
    cf = channel_lags(Df, cfg["alpha_b"])
    c = cc["car"] + cc["cat"] + cc["cp"]
    c2 = cf["car"] + cf["cat"] + cf["cp"]
    M = len(c)
    d = np.arange(1, M - 1)
    pred = c2[2 * d] + 0.5 * (c2[2 * d - 1] + c2[2 * d + 1])
    sc = float(np.max(np.abs(c)))
    dev_lag = float(np.max(np.abs(c[1:M - 1] - pred))) / sc
    check("S3.3 dyadic transport identity (unconsumed)", 
          dev_lag <= BAR_GL,
          "c^(D)_d == c^(D/2)_2d + (c'_2d-1 + c'_2d+1)/2, rel dev "
          "%.1e -- transport EXISTS (v749 T1.2a) but variant B never "
          "uses it: each stage is built from source" % dev_lag)
    return dict(ok=(ok_mem and ok_pd), ok_mem=ok_mem, ok_pd=ok_pd)


# ============================================================ must-fails
def s4_mustfails(cfg):
    section("S4  MUST-FAILS (sealed mutants)")
    # m1 anchor-only adversary
    name2, kind2, L2, _ = cfg["smooth_elements"][min(
        1, len(cfg["smooth_elements"]) - 1)]
    F2 = smooth_element(kind2, L2)
    D = cfg["meshes_c"][0]
    dref = min(cfg["meshes_c"]) / (2 * cfg["ref_div"])
    car = kernel_ref_lags(dref, L2, core.arch_lags)
    cp = kernel_ref_lags(dref, L2, stage2.pole_lags_closed)
    ch = channel_lags(D, cfg["alpha_floor"][-1])
    e_tot = (read_lags(ch["cat"], D, F2, L2) - comb_ref(F2, ch["al"])
             + read_lags(ch["car"], D, F2, L2)
             - read_lags(car, dref, F2, L2)
             + read_lags(ch["cp"], D, F2, L2)
             - read_lags(cp, dref, F2, L2))
    adversary_claim = abs(e_tot) <= 1.0e-9 * max(1.0, abs(e_tot))
    check("m1 anchor-only adversary CAUGHT", not adversary_claim,
          "'deepest anchor at fixed mesh reaches Q_Weil' is FALSE: "
          "|E_tot| = %.2e stays" % abs(e_tot))

    # m2 broken tent exactness: a nearest-neighbour ATOM PLACEMENT
    # in the reference (the sloppy assembly: each atom snapped to its
    # closest grid node instead of the exact tent split)
    (seed, ng, D0) = cfg["grid_elements"][0]
    Fg, Lg = grid_element(seed, ng, D0)
    chg = channel_lags(D0, cfg["alpha_meshconst"])
    ka = core.atoms_in(chg["al"])
    u_snap = np.round(core.U_ALL[:ka] / D0) * D0
    ref_nn = -float(core.MU_ALL[:ka] @ Fg(u_snap))
    dev_nn = abs(read_lags(chg["cat"], D0, Fg, Lg) - ref_nn)
    sc = max(abs(comb_ref(Fg, chg["al"])), 1.0e-6)
    check("m2 broken tent read CAUGHT", dev_nn / sc > BAR_EXACT,
          "nearest-neighbour atom placement violates the exactness "
          "bar: rel dev %.2e >> %.0e" % (dev_nn / sc, BAR_EXACT))

    # m3 corrupted transport weights
    Dc, Df = cfg["meshes_b"][0], cfg["meshes_b"][1]
    cc = channel_lags(Dc, cfg["alpha_b"])
    cf = channel_lags(Df, cfg["alpha_b"])
    c = cc["car"] + cc["cat"] + cc["cp"]
    c2 = cf["car"] + cf["cat"] + cf["cp"]
    M = len(c)
    d = np.arange(1, M - 1)
    pred_bad = c2[2 * d] + (c2[2 * d - 1] + c2[2 * d + 1])   # full weight
    dev_bad = float(np.max(np.abs(c[1:M - 1] - pred_bad))) \
        / float(np.max(np.abs(c)))
    check("m3 corrupted transport CAUGHT", dev_bad > BAR_GL,
          "full-weight neighbour rule violates the identity: rel dev "
          "%.2e >> %.0e" % (dev_bad, BAR_GL))

    # m4 membership corruption
    wins = stage4.family_ext()
    w = wins[0]
    ch = channel_lags(w["D"], w["alpha"])
    c_tw = ch["car"] + ch["cat"] + ch["cp"]
    p_bad = w["p"].copy()
    p_bad[len(p_bad) // 2] += 1.0e-6
    dev_mem = float(np.max(np.abs(c_tw[:w["M"]] - p_bad))) \
        / float(np.max(np.abs(p_bad)))
    check("m4 membership corruption CAUGHT", dev_mem > BAR_MEMBER,
          "a 1e-6 lag perturbation violates the membership bar: rel "
          "dev %.2e >> %.0e" % (dev_mem, BAR_MEMBER))


# ================================================================== S5
def s5_verdict(r1, r2, r3):
    section("S5  SEALED VERDICT")
    gate_a = r1["ok"]
    gate_b = r3["ok"]
    gate_c = r2["gate_c"]
    floor = r2["ok_floor"]
    if gate_a:
        primary = "ELEMENTWISE_STABILIZATION_GO"
    elif gate_b:
        primary = "CANONICAL_MESH_REBUILD_GO"
    elif gate_c:
        primary = "SIGNED_DEFECT_CORRECTION_GO"
    elif floor:
        primary = "ANCHOR_ONLY_INSUFFICIENT"
    else:
        primary = "NO_EXTRACTION_ARCHITECTURE"
    co = []
    if gate_b:
        co.append("CANONICAL_MESH_REBUILD_GO")
    if gate_c:
        co.append("SIGNED_DEFECT_CORRECTION_GO(%s)" % r2["subtype"])
    if floor:
        co.append("ANCHOR_ONLY_INSUFFICIENT")
    print("""
  THE MEASURED FORK (honest scope):
  A  the native class stabilizes FINITELY in the anchor direction,
     per channel, at the predicted onset, and its value is CONSTANT
     under mesh refinement -- the elementwise architecture consumes
     NO mesh-cofinal ladder and NO transport.  The mesh limit
     reappears ONLY off the native class, where it is a rate-
     controlled quadrature defect (leg C), i.e. the classical
     density/continuity step -- not a positivity ladder.
  B  every deployed window is a directly rebuilt canonical member
     (dev 0 class); the rebuild ladder carries per-stage PSD
     certificates with honestly falling margins; the transport
     identity exists but is never consumed.
  C  the defect is one-sided per channel on the C^2 class and sits
     inside the closed-form interpolation envelope -- controlled on
     its own, no wall margin; the anchor-only floor is real.
  NOTHING here proves any window positivity, any local lemma, or
  any statement about zeta zeros.  NO RH CLAIM.""")
    print("\n  PRIMARY: %s" % primary)
    if co:
        print("  CO-LETTERS: %s" % " + ".join(co))
    return primary


def main():
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = bool(args.smoke)

    cfg = dict(
        smoke=smoke,
        grid_elements=GRID_ELEMENTS[:1] if smoke else GRID_ELEMENTS,
        alpha_sweep=(0.55, 1.0, 2.0) if smoke else ALPHA_SWEEP,
        alpha_meshconst=ALPHA_MESHCONST,
        smooth_elements=(SMOOTH_ELEMENTS[1],) if smoke
        else SMOOTH_ELEMENTS,
        alpha_c=ALPHA_C,
        meshes_c=MESHES_C[:2] if smoke else MESHES_C,
        alpha_floor=ALPHA_FLOOR[-2:] if smoke else ALPHA_FLOOR,
        alpha_b=ALPHA_B,
        meshes_b=MESHES_B[:2] if smoke else MESHES_B,
        ref_div=8 if smoke else 16,
    )

    print("PRIME.EXTRACTION.ORDER_REPAIR_FORK.01 -- round 325%s"
          % ("  [SMOKE]" if smoke else ""))
    print("SPEC_SHA %s" % SPEC_SHA[:16])
    g0_firewall()
    r1 = s1_elementwise(cfg)
    r2 = s2_defect(cfg)
    r3 = s3_rebuild(cfg)
    s4_mustfails(cfg)
    primary = s5_verdict(r1, r2, r3)

    n_ok = sum(1 for _n, ok, _d in CHECKS if ok)
    print("\nRESULT: %d/%d gates PASS   VERDICT %s   SPEC_SHA %s"
          % (n_ok, len(CHECKS), primary, SPEC_SHA[:16]))
    print("wall %.1f s" % (time.time() - T0_WALL))
    return 0 if n_ok == len(CHECKS) else 1


if __name__ == "__main__":
    sys.exit(main())
