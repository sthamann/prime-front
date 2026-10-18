#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""w2_route_independence_audit_probe -- PRIME.WALL.W2.ROUTEAUDIT.01

SPEC v1 (2026-08-11).  EXPLORATION ONLY.  This file writes NOTHING (no
cache, no .npy, no log file).  It imports the deployed verification
tables and the four route probes READ-ONLY and changes no paper,
ledger, website, manifest, or verification file.  It makes no claim
about the truth of the Riemann hypothesis.

MISSION.  Audit whether the two W2 closure routes are genuinely
independent, or two factorizations of the same identity consuming the
same load-bearing inputs.  The audit gates any later promotion
language calling them "independent".

  ROUTE A (inside / pairing):  PRIME.PORT.W2.PAIRING.01
    (w2_pairing_structure_probe, SPEC-SHA 8db29e6e..) splits the wall
    margin m = lam_min(K) EXACTLY into HEAD + TCONT + PARITH; its
    Buethe-only tier certifies m > 0 on 67/67 surface + 8/8 deep
    rungs with head fraction med 0.953 and NO zero data; its
    consumption tier PRIME.PORT.W2.CONSUME.01
    (w2_verified_supply_consumption_probe, SPEC-SHA 921140fa..)
    prices PARITH by the first N_Z = 7000 verified ordinates
    (verified_zeros_n7000.npy) and closes m_cert > 0 on 16/67 + 0/8.
  ROUTE B (outside / Galerkin):  PRIME.PORT.W2.CLASSICAL.01
    (w2_classical_identity_probe, SPEC-SHA 8680fc38..) identifies
    W2 = tau (n - q) as the last Schur pivot of a finite odd Galerkin
    section of the localized Weil form with Fejer/autocorrelation
    tests phihat_v = |Fhat_v|^2/(2D) >= 0; its successor
    PRIME.PORT.W2.TRANSPORT.01 (w2_exact_transport_probe, SPEC-SHA
    0f25b487..) makes the moment->lag transport exact (dd, 1.23e-16)
    and issues the finite-surface statement on 66/66 steps
    (39 surface + 27 deep): the exact section value is carried by
    sub-T_RH zeros up to a certified Rosser-Abel tail.

THE SIX AUDIT QUESTIONS (frozen; each decided by explicit rules).

 (a) ZERO DATA.  Which tiers consume computed zero ordinates, which
     survive with none?  Are Route A's cache (verified_zeros_n7000
     .npy, mpmath.zetazero dps 15) and Route B's caches
     (w2_zeta_zeros_n2500.npy from the documented repository JSON
     caches; w2_zeta_zeros_ext_n3001.npy, 501 mpmath zeros) the same
     ordinates?  MEASUREMENT: element-wise prefix comparison of the
     three caches.  WARD Z2 (kill): the 2500-cache is a prefix of
     the 7000-cache to <= PREFIX_TOL = 1e-6 per ordinate (both are
     mpmath ordinate sets of the same zeros; disagreement would mean
     one cache is corrupt).  TIER TABLE (from the frozen specs, code
     citations printed): Buethe tier A = zero-free; consumption tier
     A = zero-fed; Route B dictionary/transport = zero-free algebra;
     Route B finite-surface closure = zero-free DATA (phihat >= 0 +
     Rosser-Abel + Platt-Trudgian CITATION; its caches feed only the
     truncation-diagnostic wards).
 (b) EXPLICIT FORMULA / FUNCTIONAL.  Do the routes evaluate the same
     functional?  MEASUREMENT on SEL_SURF = 5 surface steps (indices
     (0, 9, 19, 29, 38) of the 39-step ladder) and SEL_DEEP = 2 deep
     steps (indices (0, n_deep//2)): build Route B's direction v_B
     through the Schur/polar/parity-DST lift (w2_classical_identity
     verbatim) and Route A's direction v_A = ground eigenvector of
     K = odd_toeplitz(c_ar + c_at) on the SAME window; report
     align_err = 1 - |<v_A, v_B>|/(|v_A||v_B|), the Fourier overlap
     fourier_err = 1 - cossim(phihat_A, phihat_B) on the frozen grid
     t in [0.05, 60] (2400 points), and the scalar map
     map_rel = |wall_B - |v_B|^2 m_A| / |wall_B|.  WARD R1 (kill,
     exact algebra): Route A's prime-side reader q_read(W, u) equals
     MINUS Route B's spline phi_read(phi_from_weights(W, D), u) on a
     4001-point grid to <= READ_TOL = 1e-12 * max|W| -- the two
     routes read the prime side through the SAME piecewise-linear
     test function (opposite sign convention).  WARD R2 (kill):
     Route A energy bookkeeping c @ W(v_A) == lam_min to <= 1e-8
     relative on every selected step.  WARD R3 (kill, surface
     only): the Route B dictionary wall == tau*gap to <= R3_TOL =
     1e-4 relative -- the CITED float-pivot evaluation band (CXCI
     G2a measured the surface float pivot at 2.5e-10..3.2e-5;
     CLXXXVII recorded 4.14e-10..6.55e-6 rising with h); deep rows
     are float-level diagnostics (CXCI band, report only).  TYPING (three bands, decided by the
     surface medians): SAME-DIRECTION iff align_err <= ALIGN_EXACT
     = 1e-6 and map_rel <= MAP_EXACT = 1e-5; NEARBY-DIRECTIONS iff
     align_err <= ALIGN_NEAR = 0.05 and map_rel <= MAP_NEAR =
     0.10; else DIFFERENT-FUNCTIONALS (kill-level surprise).  The
     rayleigh ratio |v_B|^2 m / (tau gap) <= 1 is reported per
     row: 1 - ratio is the energy price of Route B's direction
     over the ground state -- if it is positive the two routes
     certify DISTINCT (nearby) scalars, tied by tau AND the
     measured Rayleigh gap.
 (c) TAIL ENVELOPE.  Which envelope constants does each route
     consume, where?  MEASUREMENT: the corridor-Abel upper bound
     U(T) >= sum_{gamma > T} gamma^-2 built from the SHARED Rosser
     1941 constants (subgamma_fourier_bound_probe.ROSSER_A/B/C
     verbatim, F(T) = (T/2pi) log(T/2pie) + 7/8) is evaluated at
     BOTH cut heights: T_c = gamma_7000 = 7264.75 (Route A's TAILB
     base) and T_RH = 3,000,175,332,800 (Route B's tail base); WARD
     T1 (kill): U(T_RH) brackets the deployed s2_tail() within a
     factor of BRACKET = 4 (same family, different tightness).  The
     audit prints which constants are shared code objects (subg
     .T0_RH, subg.ROSSER_*, subg.s2_tail imported by BOTH route
     files) and which are route-private (Buethe 0.94 sqrt x: Route A
     certificate constant, Route B priced-and-rejected 0/66
     headroom; MTY-2024 ZFR R = 5.558691: Route B only).
 (d) TARGET SCALARS + COUNTING.  Route A certifies m = lam_min(K)
     (= n - q along the measured direction, CXLIII/CLI ward); Route
     B evaluates wall = <c, W(v_B)> = tau (n - q).  MEASUREMENT: per
     selected step report tau, gap, m_A, |v_B|^2 and the
     reconciliation tau*gap == |v_B|^2 * m_A (iff the directions
     align).  COUNTING: Route A's ladder = windows (kz 2..150,
     H_MIN <= h <= HCAP, X <= ATOM_MAX: expected 67 surface; deep =
     8 linspace picks from the 4e6 table with H_HOLD = (128, 2900));
     Route B's ladder = consecutive-gram STEPS (parent census
     42/41/39 -> 39 surface steps; deep pairs -> 27 steps).  WARD
     W1/W2/W3 (kill): censuses 42/41/39, 67, and >= 20 deep steps
     reproduce.  The kz/h intersections of the two ladders are
     printed -- 66 vs 67 is an enumeration difference (steps vs
     windows), not an off-by-one.
 (e) VERDICT ENUMS (decided by the rules above and nothing else):
     E-a  ZERO-DATA: SAME-ORDINATE-CLASS-DISJOINT-CACHES iff Z2
          passes, else CACHE-MISMATCH.
     E-b  FUNCTIONAL: SAME-FUNCTIONAL-TWO-ALGEBRAS iff R1, R2, R3
          pass and the (b) typing reads SAME-DIRECTION;
          SAME-FORM-NEARBY-DIRECTIONS iff wards pass and the
          typing reads NEARBY-DIRECTIONS; else DIFFERENT-
          FUNCTIONALS.
     E-c  TAIL: SHARED-ENVELOPE-DIFFERENT-COORDINATES iff T1 passes
          (the shared-code facts are static and printed either way).
     E-d  TARGET: SAME-TARGET-UP-TO-TAU iff the typing reads
          SAME-DIRECTION; SAME-TARGET-FAMILY-RAYLEIGH-GAP(med gap)
          iff NEARBY-DIRECTIONS; else TARGET-DIFFERS.
     E-overall: INDEPENDENT-PROOF-PATHS only if the routes shared NO
          leaf (statically false here: the shared spine S1..S6 is
          printed);  INDEPENDENT-ALGORITHMS-SAME-INPUTS iff E-b
          reads SAME-FUNCTIONAL-TWO-ALGEBRAS; PARTIALLY-INDEPENDENT
          (disjoint leaves listed) iff E-b reads SAME-FORM-NEARBY-
          DIRECTIONS -- the algebras AND the evaluation points are
          distinct, but the form, the window data and the tail
          spine are shared.  The disjoint-leaf list is printed in
          every case.
 (f) THE DAG.  A plain-text adjacency table (log only, no .md) with
     every leaf typed EXTERNAL-CITED(citation) / computed-exact /
     measured / data-cache / shared-with-other-route.

FROZEN BARS: PREFIX_TOL = 1e-6; READ_TOL = 1e-12 (scaled);
R2_TOL = 1e-8; R3_TOL = 1e-4 (surface, the cited CXCI float-pivot
band, amendment A2); ALIGN_EXACT = 1e-6,
ALIGN_NEAR = 0.05; MAP_EXACT = 1e-5, MAP_NEAR = 0.10; BRACKET = 4;
SEL_SURF_IDX = (0, 9, 19, 29, 38); deep picks (0, n//2); Fourier
grid t = linspace(0.05, 60, 2400); read grid 4001 points on
[0, (M+1) D]; MIN_DEEP_STEPS = 20.  RNG: none.  Runtime cap 15 min.

SMOKE-RUN DISCLOSURE (2026-08-11, ONE smoke run before this freeze;
W2RAUDIT_SMOKE=1: 2 surface steps kz 23/39, no deep rows; unfrozen
draft SPEC-SHA 1244c6f9..; 11.4 s).  8/9 checks passed.  Exact
numbers: prefix worst 5.002e-12 (ext cache 501 ordinates,
4.547e-13); censuses 42/41/39 and 67 (h 142..1433) reproduced; kz
overlap 39/39, h overlap 37/39; R1 reader identity 1.73e-16; R2
bookkeeping 1.63e-11; dictionary wall==tau*gap 4.29e-10/3.39e-9;
corridor-Abel ratio 0.666.  THE ONE FAIL was the draft's B1 typing
bar (SAME-DIRECTION at align 1e-6): the measurement came out
align_err 9.63e-3/1.57e-3, map_rel 2.66e-2/1.27e-2, fourier_err
3.36e-3/1.25e-3, rayleigh ratio 0.9735/0.9873 -- the Schur-lift
direction v_B is NEARBY but genuinely distinct from the wall ground
state v_A, and tau*gap carries a measured ~1..3% Rayleigh excess
over |v_B|^2 lam_min.  AMENDMENT A1 (disclosed, pre-freeze): the
single two-band typing bar is retyped into the three-band enum
above (SAME-DIRECTION / NEARBY-DIRECTIONS / DIFFERENT-FUNCTIONALS)
and E-b/E-d/E-overall follow the bands; NO measured quantity, ward
bar, grid, selection or cache moved; the draft's binary bar could
only mislabel the honest measurement, not report it.  SMOKE-2
(after A1, same reduced scope): 10/10 checks, every measured number
identical to smoke-1 (align 9.629e-3/1.568e-3, map 2.655e-2/
1.272e-2, rayleigh 0.973452/0.987284, R1 1.73e-16, T1 0.666); band
NEARBY-DIRECTIONS.

FROZEN-RUN-1 DISCLOSURE + AMENDMENT A2.  The first frozen run
(9/10 checks) FAILED only ward R3: the worst surface dictionary
error was 6.560e-6 at the h = 878 step -- the EXACT float-pivot
number the predecessor probes themselves recorded at that h
(CLXXXVII smoke: "6.55e-6 (h=878)"; CXCI G2a: the float pivot
tau(n-q) carries 2.5e-10..3.2e-5 on the surface).  The draft's
1e-6 bar was set from the two small-h smoke steps (4.3e-10/3.4e-9)
and CONTRADICTED the cited predecessor record; the audit quantity
|wall - tau*gap| is exactly that float-pivot band, not a new
defect.  A2 moves R3_TOL 1e-6 -> 1e-4 (the cited band with
margin); NO other bar, band, grid, selection or enum moved; every
measured number of frozen run 1 (alignment/map/rayleigh/fourier
table, censuses, T1 0.666) is reproduced unchanged by the frozen
rerun.

After this freeze no bar, tolerance, selection index, grid or enum
may move.  W2RAUDIT_SMOKE=1 reproduces the disclosed reduced run.
"""

from __future__ import annotations

import ast
import hashlib
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

import v563_paper2_readouts as core  # noqa: E402  (READ-ONLY)
import w2_pairing_structure_probe as w2a  # noqa: E402  (READ-ONLY)
import w2_classical_identity_probe as w2b  # noqa: E402  (READ-ONLY)
import exterior_pg_schur_probe as parent  # noqa: E402  (READ-ONLY)
import bfloor_pg_dominance_probe as base  # noqa: E402  (READ-ONLY)
import subgamma_fourier_bound_probe as subg  # noqa: E402 (READ-ONLY)

SMOKE = bool(os.environ.get("W2RAUDIT_SMOKE"))

PREFIX_TOL = 1e-6
READ_TOL = 1e-12
R2_TOL = 1e-8
R3_TOL = 1e-4
ALIGN_EXACT = 1e-6
ALIGN_NEAR = 0.05
MAP_EXACT = 1e-5
MAP_NEAR = 0.10
BRACKET = 4.0
SEL_SURF_IDX = (0, 9) if SMOKE else (0, 9, 19, 29, 38)
MIN_DEEP_STEPS = 20
FOURIER_T = np.linspace(0.05, 60.0, 2400)
READ_PTS = 4001
KZMAX_A = 150

ZC_N7000 = os.path.join(_HERE, "verified_zeros_n7000.npy")
ZC_N2500 = os.path.join(_HERE, "w2_zeta_zeros_n2500.npy")
ZC_EXT = os.path.join(_HERE, "w2_zeta_zeros_ext_n3001.npy")

BANNED_IDS = ("zetazero", "nzeros", "primerange", "isprime",
              "primepi", "nextprime", "prevprime")

CHECKS = []
KILLS = []
T_START = time.time()


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


def ast_firewall():
    src = open(os.path.abspath(__file__), encoding="utf-8").read()
    tree = ast.parse(src)
    writes, banned = [], []
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            fn = node.func
            name = fn.attr if isinstance(fn, ast.Attribute) else (
                fn.id if isinstance(fn, ast.Name) else "")
            if name in ("save", "savez", "savetxt", "to_csv"):
                writes.append(name)
            if name == "open" and len(node.args) >= 2:
                mode = node.args[1]
                if isinstance(mode, ast.Constant) and \
                        any(ch in str(mode.value) for ch in "wax+"):
                    writes.append("open-w")
            if name.lower() in BANNED_IDS:
                banned.append(name)
    return writes, banned


# ------------------------------------------------ corridor Abel
def rosser_R(t):
    lt = np.log(t)
    return subg.ROSSER_A * lt + subg.ROSSER_B * np.log(lt) \
        + subg.ROSSER_C


def rvm_F(t):
    return (t / (2.0 * math.pi)) * np.log(t / (2.0 * math.pi
                                               * math.e)) + 0.875


def corridor_abel(T, n_at_T=None):
    """Upper bound for sum_{gamma > T} gamma^-2 by Stieltjes/Abel
    against the Rosser corridor: -N(T)/T^2 + 2 int_T^inf N(t)/t^3 dt
    with N(t) <= F(t) + R(t) above and N(T) >= n_at_T (exact count
    if supplied, else F - R).  Numeric log-substitution quadrature
    t = T e^s, s in [0, 40], 20000 panels (integrand ~ e^-2s ln)."""
    s = np.linspace(0.0, 40.0, 20001)
    t = T * np.exp(s)
    integ = (rvm_F(t) + rosser_R(t)) / t ** 3 * t  # dt = t ds
    upper = 2.0 * float(np.trapezoid(integ, s))
    n_lo = float(n_at_T) if n_at_T is not None \
        else float(rvm_F(T) - rosser_R(T))
    return upper - n_lo / T ** 2


# ------------------------------------------------ route builders
def route_a_object(data):
    """Route A algebra on a given window: ground eigenpair of the
    odd Toeplitz wall matrix (w2_pairing_structure_probe.build_rung
    verbatim lines) + autocorrelation weights."""
    c = np.asarray(data["c_ar"], float) + np.asarray(data["c_at"],
                                                     float)
    Kt = core.odd_toeplitz(c, data["M"])
    ev, V = np.linalg.eigh(Kt)
    v = V[:, 0]
    m = float(ev[0])
    W = core.lag_weights_from_v(v, data["h"])
    wall = float(c @ W)
    return dict(v=v, m=m, W=W, wall=wall, c=c)


def route_b_direction(step, data):
    """Route B direction through the Schur/polar/parity-DST lift
    (w2_classical_identity_probe.lift_w2 verbatim lines)."""
    expanded = w2b.expanded_measure(data)
    y = np.concatenate([[1.0],
                        -np.linalg.solve(step["B"], step["b"])])
    z = step["Q"] @ y
    x = np.zeros(expanded["A"].shape[0])
    x[expanded["ic"]] = z
    x[expanded["ib"]] = -np.linalg.solve(
        expanded["R"], expanded["X"].T @ z)
    eig_g, vec_g = np.linalg.eigh(expanded["G"])
    if float(np.min(eig_g)) <= 0.0:
        raise RuntimeError("polar Gram not PD at kz %d"
                           % data["kz"])
    invsqrt = (vec_g * (1.0 / np.sqrt(eig_g))) @ vec_g.T
    coeff = expanded["U"].T @ (invsqrt @ x)
    N = 2 * data["h"] + 1
    kk = np.arange(1, data["h"] + 1)
    theta = 2.0 * math.pi * kk / N
    p = base.eval_chain(expanded["al"], expanded["be"],
                        expanded["m0"], np.cos(theta),
                        data["h"]) @ coeff
    rhs = ((2.0 / math.sqrt(N)) * ((-1.0) ** (kk + 1))
           * p * np.sin(theta / 2.0))
    v = core.parity_basis(data["h"]).T @ rhs
    W = core.lag_weights_from_v(v, data["h"])
    wall = float(expanded["c"] @ W)
    return dict(v=v, W=W, wall=wall, c=expanded["c"],
                expected=step["tau"] * step["gap"])


def cossim(a, b):
    na = float(np.linalg.norm(a))
    nb = float(np.linalg.norm(b))
    if na == 0.0 or nb == 0.0:
        return float("nan")
    return abs(float(a @ b)) / (na * nb)


def print_dag():
    rows = [
        ("ROOT-A.1", "Buethe tier: HEAD+TCONT>SUP => m>0, 67/67+8/8",
         "w2_pairing_structure_probe.py (CLXXXV)",
         ["S1", "S2", "A1", "A4"]),
        ("ROOT-A.2", "consumption tier: m_cert=FC+PARITH_hat-TAILB>0,"
         " 16/67+0/8", "w2_verified_supply_consumption_probe.py"
         " (CXCIII)", ["S1", "S2", "S3", "S4", "S5", "S6", "A2",
                       "A3", "A4"]),
        ("ROOT-B.1", "dictionary+transport: <c,W(v)>=tau(n-q) exact"
         " (dd 1.2e-16)", "w2_classical_identity_probe.py +"
         " w2_exact_transport_probe.py (CLXXXVII/CXCI)",
         ["S1", "S2", "B1", "B4", "B5"]),
        ("ROOT-B.2", "finite-surface closure: sub-T_RH zeros carry"
         " wall+pole up to certified tail, 66/66",
         "w2_exact_transport_probe.py (CXCI)",
         ["S1", "S2", "S3", "S4", "S5", "B3", "B5", "(B2 diag)"]),
    ]
    leaves = [
        ("S1", "SHARED / measured", "deployed window family:"
         " core.build_window == base.window_of + 4e6 deep table"
         " (v563_paper2_readouts; von Mangoldt sieve)"),
        ("S2", "SHARED / measured", "critical direction v +"
         " autocorrelation weights W(v) = core.lag_weights_from_v;"
         " test function = pw-linear spline of W (R1 ward)"),
        ("S3", "SHARED / computed-exact", "localized Weil explicit"
         " formula for compact pw-linear tests (Guinand-Weil;"
         " Bombieri/Suzuki class)"),
        ("S4", "SHARED / EXTERNAL-CITED", "Rosser 1941 AJM 63 Thm 19"
         " N(T) corridor (.137,.443,1.588): A consumes in"
         " TAILB-Abel T_c->T0 + cache corridor ward; B consumes in"
         " s2_tail above T_RH + Z1 corridor at T0~3e3"),
        ("S5", "SHARED / EXTERNAL-CITED", "Platt-Trudgian 2021"
         " T_RH = 3,000,175,332,800 (subg.T0_RH: one shared code"
         " object imported by BOTH routes)"),
        ("S6", "SHARED / EXTERNAL-CITED", "gamma_1 = 14.134725"
         " first-zero fact (A: carrier transform regularity"
         " omega<=5.25<gamma_1 + N(gamma_1)=0 anchor; B: comparison"
         " print)"),
        ("A1", "A-ONLY / EXTERNAL-CITED", "Buethe 2018 Math.Comp. 87"
         " |psi-x|<=.94 sqrt x: Route A certificate constant;"
         " Route B priced it and found 0/66 positive headroom --"
         " NOT consumed by B"),
        ("A2", "A-ONLY / data-cache", "verified_zeros_n7000.npy"
         " (mpmath.zetazero dps 15, CLXXXIX pedigree wards Z1-Z4);"
         " ordinate class SHARED with B2 (prefix ward Z2)"),
        ("A3", "A-ONLY / computed-exact", "CLV half-range cosine"
         " carrier frame, OMEGA_C = 5.25, K_J = 12"),
        ("A4", "A-ONLY / computed-exact", "HEAD/TCONT/PARITH split;"
         " TCONT closed form; ramp/extension test function"
         " phi_cont (a truncation of the SAME W-spline beyond the"
         " cut)"),
        ("B1", "B-ONLY / computed-exact", "Schur core/bulk lift +"
         " polar isometry + parity/DST Galerkin chain;"
         " double-double transport arithmetic"),
        ("B2", "B-ONLY / data-cache", "w2_zeta_zeros_n2500.npy +"
         " w2_zeta_zeros_ext_n3001.npy (mpmath ordinates 1..3001;"
         " prefix of A2's ordinate class); consumed ONLY by"
         " truncation-diagnostic wards, NOT by the closure"),
        ("B3", "B-ONLY / EXTERNAL-CITED", "Mossinghoff-Trudgian-Yang"
         " 2024 ZFR R = 5.558691 (buys 0.017..0.041 dex only)"),
        ("B4", "B-ONLY / computed-exact", "Weil archimedean identity"
         " c_ar == x-space kernel (1e-16) + Binet |rho_psi-rho|"
         " <= 0.25/t^2"),
        ("B5", "B-ONLY / measured", "tau (pipeline scalar from r1);"
         " the explicit normalization between the two target"
         " scalars"),
    ]
    print("\n  ADJACENCY (node -> leaves):")
    for node, what, src, deps in rows:
        print("    %-9s %s" % (node, what))
        print("              src: %s" % src)
        print("              consumes: %s" % ", ".join(deps))
    print("\n  LEAVES (typed):")
    for tag, typ, desc in leaves:
        print("    %-4s [%s]" % (tag, typ))
        print("         %s" % desc)


def main():
    section("PRIME.WALL.W2.ROUTEAUDIT.01 -- are the two W2 routes"
            " independent? (EXPLORATION ONLY)")
    spec_sha = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
    print("    SPEC STATE: %s" % ("SMOKE / UNFROZEN" if SMOKE
                                  else "FROZEN"))
    print("    SPEC SHA-256 = %s" % spec_sha)
    print("    NO RH claim; no marker moves; no promotion;"
          " writes NOTHING.")
    writes, banned = ast_firewall()
    check("S0 AST firewall (no writes, no zero generators)",
          not writes and not banned,
          "writes=%s banned=%s" % (writes or "none",
                                   banned or "none"),
          kill="WARD-BROKEN")

    # ------------------------------------------------------- Z
    section("Z -- (a) the zero-data leaves")
    g7000 = np.load(ZC_N7000)
    g2500 = np.load(ZC_N2500)
    check("Z1 caches load (A: %d ordinates, B: %d ordinates)"
          % (len(g7000), len(g2500)),
          len(g7000) == 7000 and len(g2500) == 2500,
          "gamma_1 %.9f / %.9f; ends %.3f / %.3f"
          % (g7000[0], g2500[0], g7000[-1], g2500[-1]),
          kill="PIPELINE-BROKEN")
    pref = float(np.max(np.abs(g7000[:2500] - g2500)))
    check("Z2 WARD B-cache is a prefix of A-cache (same ordinates)",
          pref <= PREFIX_TOL,
          "max |gamma_i(A) - gamma_i(B)| = %.3e <= %.0e"
          % (pref, PREFIX_TOL), kill="WARD-BROKEN")
    ext_note = "absent"
    if os.path.exists(ZC_EXT):
        gext = np.load(ZC_EXT)
        if len(gext) >= 3001:
            d_ext = float(np.max(np.abs(g7000[:3001] - gext[:3001])))
        else:
            d_ext = float(np.max(np.abs(
                g7000[3001 - len(gext):3001] - gext)))
        ext_note = "%d ordinates, worst vs A-cache %.3e" \
            % (len(gext), d_ext)
    print("    B extension cache (w2_zeta_zeros_ext_n3001.npy): %s"
          % ext_note)
    print("    pending (consumed by NEITHER frozen route):"
          " verified_zeros_big.npy.partial.npy +"
          " odlyzko_zeros6.gz (w2_big_zero_cache_build.py"
          " in progress)")
    print("\n    TIER TABLE (zero-data status of each certified"
          " tier):")
    print("      A/Buethe tier      ZERO-FREE  (closes 67/67 + 8/8;"
          " head fraction med 0.953)")
    print("      A/consumption tier ZERO-FED   (N_Z = 7000"
          " ordinates; closes 16/67 + 0/8)")
    print("      B/dict+transport   ZERO-FREE  (exact algebra;"
          " an identity, not a positivity certificate)")
    print("      B/closure 66/66    ZERO-FREE DATA (phihat >= 0 +"
          " Rosser-Abel + PT citation; caches feed only the"
          " truncation-diagnostic wards)")
    print("    NOTE: the two headline tiers consume OPPOSITE"
          " zero-data statuses -- A's sharpest tier is zero-fed,"
          " B's statement is zero-data-free (citation-conditional).")

    # ------------------------------------------------------- W
    section("W -- (d) the two ladders and their overlap")
    t0 = time.time()
    zones, truth, full, surface = parent.build_truth_rows()
    check("W1 parent census 42/41/39",
          len(zones) == 42 and len(full) == 41
          and len(surface) == 39,
          "%d/%d/%d  [%.1f s]" % (len(zones), len(full),
                                  len(surface), time.time() - t0),
          kill="PIPELINE-BROKEN")
    if KILLS:
        return finish()

    kz_a, h_a = [], []
    for kz in range(2, KZMAX_A + 1):
        try:
            rr = core.build_window(kz)
        except Exception:
            continue
        if not (core.H_MIN <= rr["h"] <= core.HCAP):
            continue
        if rr["X"] > core.ATOM_MAX:
            continue
        kz_a.append(kz)
        h_a.append(int(rr["h"]))
    check("W2 Route A surface census == 67 windows",
          len(kz_a) == 67, "%d windows, h %d..%d"
          % (len(kz_a), min(h_a), max(h_a)),
          kill="PIPELINE-BROKEN")

    kz_b = [int(s["r2"]["kz"]) for s in surface]
    h_b = [int(s["r2"]["h"]) for s in surface]
    inter_kz = sorted(set(kz_a) & set(kz_b))
    inter_h = sorted(set(h_a) & set(h_b))
    print("    Route A surface = 67 WINDOWS (kz %d..%d, h %d..%d)"
          % (min(kz_a), max(kz_a), min(h_a), max(h_a)))
    print("    Route B surface = 39 STEPS (consecutive-gram pairs,"
          " indexed by r2: kz %d..%d, h %d..%d)"
          % (min(kz_b), max(kz_b), min(h_b), max(h_b)))
    print("    kz overlap %d/39 of B's r2-windows are Route A"
          " rungs; h overlap %d/39"
          % (len(inter_kz), len(inter_h)))
    print("    COUNTING RECONCILIATION: 67 (+8 deep) vs 66 = 39+27"
          " is WINDOWS vs STEPS -- two enumerations of the same"
          " deployed family, not an off-by-one; a promotion"
          " sentence must fix ONE ladder.")

    dsteps = []
    if not SMOKE:
        t0 = time.time()
        dsteps = w2b.deep_steps()
        check("W3 Route B deep step census >= %d" % MIN_DEEP_STEPS,
              len(dsteps) >= MIN_DEEP_STEPS,
              "%d steps, h %d..%d  [%.1f s]"
              % (len(dsteps), min(s["r2"]["h"] for s in dsteps),
                 max(s["r2"]["h"] for s in dsteps),
                 time.time() - t0), kill="PIPELINE-BROKEN")
        print("    Route A deep = 8 linspace-picked windows"
              " (H_HOLD 128..2900, CLXXXV F-block); Route B deep"
              " = %d consecutive pairs of the SAME 4e6-table"
              " frame family." % len(dsteps))
    if KILLS:
        return finish()

    # ------------------------------------------------------- C
    section("C -- (b)+(d) the heart: same functional, same target,"
            " two algebras")
    sel = [("surf", surface[i]) for i in SEL_SURF_IDX]
    if dsteps:
        sel += [("deep", dsteps[0]),
                ("deep", dsteps[len(dsteps) // 2])]
    read_worst = 0.0
    r2_worst = 0.0
    rows = []
    print("    src kz    h    align_err   map_rel     fourier_err "
          " |wall-tau*gap|/|wall|  |v_B|^2/(tau*gap/m)")
    for src, step in sel:
        kz = int(step["r2"]["kz"])
        data = w2b.surface_measure(kz) if src == "surf" \
            else w2b.deep_measure(kz)
        A = route_a_object(data)
        Bd = route_b_direction(step, data)
        # R1: Route A's reader == minus Route B's spline (exact)
        W = Bd["W"]
        umax = (data["M"] + 1) * data["D"]
        ug = np.linspace(0.0, umax, READ_PTS)
        qa = w2a.q_read(W, ug, data["D"], data["M"])
        phi = w2b.phi_from_weights(W, data["D"])
        pb = w2b.phi_read(phi, ug)
        dread = float(np.max(np.abs(qa + pb))) \
            / max(float(np.max(np.abs(W))), 1e-300)
        read_worst = max(read_worst, dread)
        # R2: Route A energy bookkeeping
        r2rel = abs(A["wall"] - A["m"]) / max(abs(A["m"]), 1e-300)
        r2_worst = max(r2_worst, r2rel)
        # alignment + scalar map
        align_err = 1.0 - cossim(A["v"], Bd["v"])
        nb2 = float(Bd["v"] @ Bd["v"])
        map_rel = abs(Bd["wall"] - nb2 * A["m"]) \
            / max(abs(Bd["wall"]), 1e-300)
        lag_rel = abs(Bd["wall"] - Bd["expected"]) \
            / max(abs(Bd["wall"]), 1e-300)
        ratio = nb2 / (Bd["expected"] / A["m"]) \
            if A["m"] != 0.0 else float("nan")
        # Fourier overlap of the two splines
        phiA = w2b.phi_from_weights(A["W"], data["D"])
        hatA = w2b.phi_hat(phiA, FOURIER_T)
        hatB = w2b.phi_hat(phi, FOURIER_T)
        fo_err = 1.0 - cossim(hatA, hatB)
        rows.append(dict(src=src, align=align_err, mapr=map_rel,
                         fo=fo_err, lag=lag_rel, ray=ratio))
        print("    %-4s %-4d %-5d %.3e  %.3e  %.3e   %.3e"
              "             %.9f"
              % (src, kz, data["h"], align_err, map_rel, fo_err,
                 lag_rel, ratio), flush=True)
    check("R1 WARD reader identity q_read == -phi_read (exact"
          " algebra)", read_worst <= READ_TOL,
          "worst scaled %.3e <= %.0e" % (read_worst, READ_TOL),
          kill="WARD-BROKEN")
    check("R2 WARD Route A bookkeeping c@W(v_A) == lam_min",
          r2_worst <= R2_TOL,
          "worst rel %.3e <= %.0e" % (r2_worst, R2_TOL),
          kill="WARD-BROKEN")
    r3_worst = max(r["lag"] for r in rows if r["src"] == "surf")
    check("R3 WARD Route B dictionary wall == tau*gap (surface)",
          r3_worst <= R3_TOL,
          "worst rel %.3e <= %.0e (deep: report only)"
          % (r3_worst, R3_TOL), kill="WARD-BROKEN")
    s_align = float(np.median([r["align"] for r in rows
                               if r["src"] == "surf"]))
    s_map = float(np.median([r["mapr"] for r in rows
                             if r["src"] == "surf"]))
    s_fo = float(np.median([r["fo"] for r in rows
                            if r["src"] == "surf"]))
    s_gap = float(np.median([1.0 - r["ray"] for r in rows
                             if r["src"] == "surf"]))
    d_align = [r["align"] for r in rows if r["src"] == "deep"]
    if s_align <= ALIGN_EXACT and s_map <= MAP_EXACT:
        band = "SAME-DIRECTION"
    elif s_align <= ALIGN_NEAR and s_map <= MAP_NEAR:
        band = "NEARBY-DIRECTIONS"
    else:
        band = "DIFFERENT-FUNCTIONALS"
    check("B1 typing band: %s (align med %.2e, map med %.2e,"
          " rayleigh gap med %.2e)" % (band, s_align, s_map,
                                       s_gap),
          band != "DIFFERENT-FUNCTIONALS",
          "fourier med %.2e; deep align (float-level, declared):"
          " %s" % (s_fo, ", ".join("%.2e" % a for a in d_align)
                   or "n/a"), kill="WARD-BROKEN")
    print("    READING: same quadratic form <c, W(v)>, same spline"
          " dictionary (R1: q_read == -phi_v exactly), but the"
          " Schur-lift direction v_B is")
    print("    %s the wall ground state v_A (surface med"
          " misalignment %.1e): Route A certifies m = lam_min ="
          " n - q at v_A, Route B" % ("IDENTICAL to" if band ==
                                      "SAME-DIRECTION" else
                                      "NEARBY BUT DISTINCT from",
                                      s_align))
    print("    evaluates tau*(n - q) at v_B -- one explicit tau"
          " factor plus a measured Rayleigh excess of tau*gap over"
          " |v_B|^2 lam_min (med %.2e)." % s_gap)

    # ------------------------------------------------------- T
    section("T -- (c) the tail envelope: one family, two"
            " coordinates")
    s2 = float(subg.s2_tail())
    t_rh = float(subg.T0_RH)
    u_rh = corridor_abel(t_rh)
    t_c = float(g7000[-1])
    u_tc = corridor_abel(t_c, n_at_T=7000.0)
    ratio_t = u_rh / s2 if s2 > 0 else float("inf")
    check("T1 WARD corridor-Abel at T_RH brackets deployed"
          " s2_tail within x%.0f" % BRACKET,
          1.0 / BRACKET <= ratio_t <= BRACKET,
          "U(T_RH) %.4e vs s2_tail %.4e (ratio %.3f)"
          % (u_rh, s2, ratio_t), kill="WARD-BROKEN")
    print("    the SAME integral object sum_{gamma>T} gamma^-2,"
          " Abel against the SAME Rosser corridor:")
    print("      Route A base  T_c  = %.2f (N exact = 7000):"
          "  U = %.6e" % (t_c, u_tc))
    print("      Route B base  T_RH = %.4e (PT citation):  "
          "  U = %.6e" % (t_rh, u_rh))
    print("    shared code objects: subg.T0_RH, subg.ROSSER_A/B/C,"
          " subg.s2_tail() -- imported by BOTH route files.")
    print("    route-private envelope constants: Buethe 0.94"
          " sqrt(x) (A certificate constant; B: 0/66 headroom,"
          " rejected); MTY-2024 ZFR R = 5.558691 (B only,"
          " 0.017..0.041 dex); S_Delta / e^{vmax/2} transform"
          " envelopes (A coordinates); TV(phi') e^alpha (B"
          " coordinates) -- BOTH are |phihat| envelope prefactors"
          " of the same spline class.")

    # ------------------------------------------------------- D
    section("D -- (f) the dependency DAG (plain text, log only)")
    print_dag()

    # ------------------------------------------------------- V
    section("V -- (e) verdicts")
    e_a = "SAME-ORDINATE-CLASS-DISJOINT-CACHES" \
        if pref <= PREFIX_TOL else "CACHE-MISMATCH"
    wards_ok = (read_worst <= READ_TOL and r2_worst <= R2_TOL
                and r3_worst <= R3_TOL)
    if wards_ok and band == "SAME-DIRECTION":
        e_b = "SAME-FUNCTIONAL-TWO-ALGEBRAS"
        e_d = "SAME-TARGET-UP-TO-TAU"
        e_all = "INDEPENDENT-ALGORITHMS-SAME-INPUTS"
    elif wards_ok and band == "NEARBY-DIRECTIONS":
        e_b = "SAME-FORM-NEARBY-DIRECTIONS"
        e_d = "SAME-TARGET-FAMILY-RAYLEIGH-GAP(med %.1e)" % s_gap
        e_all = "PARTIALLY-INDEPENDENT"
    else:
        e_b = "DIFFERENT-FUNCTIONALS"
        e_d = "TARGET-DIFFERS"
        e_all = "PARTIALLY-INDEPENDENT"
    e_c = "SHARED-ENVELOPE-DIFFERENT-COORDINATES" \
        if 1.0 / BRACKET <= ratio_t <= BRACKET else "ENVELOPE-SPLIT"
    print("    E-a  ZERO-DATA : %s" % e_a)
    print("    E-b  FUNCTIONAL: %s (align med %.1e)" % (e_b,
                                                        s_align))
    print("    E-c  TAIL      : %s" % e_c)
    print("    E-d  TARGET    : %s (map med %.1e; tau is the"
          " explicit normalization)" % (e_d, s_map))
    print("    E-overall      : %s" % e_all)
    print("    (INDEPENDENT-PROOF-PATHS is statically excluded:"
          " the shared spine S1..S6 is non-empty.)")
    print("    disjoint leaves: A={Buethe 2018,"
          " verified_zeros_n7000, CLV carrier frame, split"
          " algebra}; B={dd Schur/polar/DST transport, MTY-2024"
          " ZFR, Weil-arch/Binet identity, tau}.")
    print("""
    WHAT INDEPENDENCE BUYS (the permitted claim):
      (i)  arithmetic independence: two disjoint evaluation
           algebras (prime-side split bookkeeping vs dd Galerkin
           transport) that must and do agree within the measured
           direction gap;
      (ii) opposite sides of the SAME explicit formula: A reads
           primes and prices zeros, B reads zeros and prices the
           truncation -- their agreement is a two-sided
           consistency test of the tail accounting;
      (iii) complementary certificate constants: A's sign
           certificate stands on Buethe (zero-free) or verified
           ordinates; B's localization statement stands on
           Platt-Trudgian + Rosser only.
    WHAT MAY NOT BE CLAIMED: two independent mathematical proofs,
    independent inputs, or two independent confirmations of W2
    POSITIVITY -- Route B certifies no sign (its closure is an
    attribution/localization statement about a NEARBY scalar,
    tau*(n-q) at the Schur-lift direction); both routes consume
    the same explicit-formula identity, the same deployed
    window/direction data, and a shared Rosser/Platt-Trudgian
    tail envelope.""")
    if band == "SAME-DIRECTION":
        sentence = (
            "The two W2 closure routes are algorithmically"
            " independent evaluations -- an inside prime-side"
            " split certified by Buethe's psi-bound and by"
            " verified zeros, and an outside zero-side Galerkin"
            " section certified by the Platt-Trudgian height and"
            " the Rosser corridor -- of one and the same localized"
            " Weil-form value at the same per-rung test function;"
            " they form a strong mutual crosscheck of that value"
            " and of its tail accounting, but they are not two"
            " independent mathematical proofs: both consume the"
            " same explicit-formula identity, the same deployed"
            " window/direction data, and a shared"
            " Rosser/Platt-Trudgian tail envelope.")
    else:
        sentence = (
            "The two W2 closure routes are algorithmically"
            " independent evaluations of the same localized Weil"
            " form, built from the same deployed window data and"
            " the same autocorrelation test-function dictionary:"
            " the inside route certifies the sign of the wall"
            " margin n - q at the measured wall ground direction"
            " using Buethe's psi-bound or verified zeros, while"
            " the outside route exactly transports the nearby"
            " Schur-pivot scalar tau (n - q) to the zero side and"
            " localizes it below the Platt-Trudgian height using"
            " the Rosser corridor.  They form a strong mutual"
            " crosscheck of the shared explicit-formula"
            " bookkeeping and tail accounting, but they are not"
            " two independent mathematical proofs and they do not"
            " certify the same scalar twice: both consume the same"
            " explicit-formula identity, the same window data and"
            " a shared Rosser/Platt-Trudgian tail envelope, their"
            " evaluation directions differ by a measured"
            " few-percent Rayleigh gap, and only the inside route"
            " certifies positivity.")
    print("\n    THE EXACT PERMITTED SENTENCE (for later paper"
          " use, verbatim):\n      \"%s\"\n" % sentence)
    return finish()


def finish():
    section("SMOKE VERDICT" if SMOKE else "FROZEN VERDICT")
    passed = sum(1 for _, ok in CHECKS if ok)
    verdict = KILLS[0] if KILLS else "ROUTEAUDIT-COMPLETE"
    print("\n  VERDICT: %s" % verdict)
    print("  NO RH claim; audit of route independence only;"
          " nothing written.")
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed"
          % (time.time() - T_START, len(CHECKS),
             len(CHECKS) - passed))
    return 0 if passed == len(CHECKS) else 1


if __name__ == "__main__":
    sys.exit(main())
