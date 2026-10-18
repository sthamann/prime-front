#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""schur_envelope_identity_probe -- PRIME.PORT.SCHUR.ENVELOPE.01
(EXPLORATION ONLY, experiments/; round 61, theorem-engineering on the
RH-side wall: the ALPHA-level lift-race pair (hub, demand along the
critical direction) versus the envelope split s_+ = s + H - R of the
round-59 Schur-Ward identity -- the exact bookkeeping bridge between
the two frames, constructed and verified to machine precision.
2026-08-10.)

THE TWO PREDECESSOR LEVELS (declared inputs).  (i) TRANSITION level
(schur_ward_identity_probe, round 59): for any symmetric pair M, M_+
with PD co-blocks, EXACTLY s_+ - s = H - R with H = Delta n -
2<x, Delta b> + <x, Delta B x> and R = |Delta b - Delta B x|^2 in
the (B + Delta B)^{-1} metric; on the tangent-surface ladder the
identity is exact (5.4e-20 raw) but the transition-level hub is NOT
the linear term (R^2 0.181) and there is no structural cancellation
(med rho 0.781).  (ii) ALPHA level (arithmetic_lift_race_probe):
lift = 0.0769 alpha + 0.809 and demand = 0.0770 alpha + 0.809 along
the critical direction, residual = lam_min exactly.  THE QUESTION
FROZEN HERE: does the alpha-level pair correspond exactly to the
envelope terms H and R -- at the right level?

THE EXACT BRIDGE (derived a priori; the construction is the claim).
The dimension-consistent transition at ALPHA level is NOT rung ->
rung (the wall dimension h changes) but WITHIN each rung: M = K_sm
(prime-free smooth wall) -> M_+ = K_t (true wall), same h x h odd
Toeplitz frame, in the FROZEN frame of the smooth bottom eigenvector
v_sm (K_sm v_sm = lam_sm v_sm).  In that frame the Schur-Ward data
collapse EXACTLY (no approximation):
    b = P K_sm v_sm = 0,  hence  x = B^{-1} b = 0,      [X-VANISH]
    s   = n = lam_sm = -demand(v_sm),                   [S-IS-DEMAND]
    H   = Delta n = v_sm.(K_t - K_sm).v_sm = lift(v_sm),[H-IS-HUB]
    R   = |b_+|^2_{B_+^{-1}},  b_+ = P K_t v_sm = P dK v_sm,
          dK = K_t - K_sm = odd_toeplitz(c_at - c_sm)   [R-IS-FLUCT]
(P = I - v_sm v_sm^T; B_+ = P K_t P on the complement; dK is the
ARITHMETIC FLUCTUATION operator, a pure comb-difference object).
The envelope identity s_+ = s + H - R then reads
    pivot_t(v_sm) = -demand(v_sm) + lift(v_sm) - R,
with pivot_t(v_sm) = 1/(v_sm . K_t^{-1} v_sm) the frame-free Schur
pivot of the TRUE wall along the smooth direction, and the exact
sandwich m_h <= s_+ <= n_+ = v_sm.K_t.v_sm (harmonic <= Rayleigh;
s_+ >= m_h because sum ov_j^2/lam_j <= 1/m_h).  SO THE FROZEN ANSWER
SHAPE to the four sharp questions:
 (1) CORRESPONDENCE: hub <-> H is EXACT and demand <-> (-s) is EXACT
     (both machine-warded); the accumulated-R reading of the demand
     is measured against this: R is expected MARGIN-SCALE (the
     Kantorovich/adaptation defect n_+ - s_+), NOT the O(1) demand
     -- the mismatch term demand - R is measured exactly per rung.
     A cross-rung telescope is DIMENSION-OBSTRUCTED (M_h varies) --
     declared; the alpha-level accumulation lives within the rung.
 (2) SYMBOLIC COMMON TERM: lift(g) = E_t(g) - E_s(g) and demand(g)
     = -E_ar(g) - E_s(g) share the SAME functional -E_s (the smooth
     atom energy) evaluated on the SAME object g; it cancels
     IDENTICALLY in lift - demand = E_t + E_ar = g.K_t.g -- decided
     by identity (two-route matrix-vs-lag wards), not fit.  The
     alpha-growth attribution (which leg carries 0.077 alpha) is
     the measured shadow: affine fits of E_s, E_t, E_ar along v
     with jackknife bars, typed.
 (3) REMAINING DIFFERENCE: H - R + s = s_+ EXACTLY.  Natural
     candidates tested: (a) R itself IS a norm square of source
     data (the fluctuation field dK v_sm) in the target metric
     B_+^{-1} -- warded exactly; (b) s_+ is a positive determinant
     ratio det(K_t)/det(B_+) -- warded on the two shallowest rungs
     (slogdet route); (c) whether s_+ carries any NEW source-only
     positivity is decided by the tau-screen: s_+ vs m_h log-log
     slope ~ +1 = relocation (the margin restated), ~ 0 = new
     floor.  HONEST EXPECTATION: RELOC (declared a priori).
 (4) CONTROLS: Epstein / scramble / smooth must break exactly the
     residual positivity (B_+ indefinite -> R stops being an
     energy; s_+ <= 0) while the completion-of-square ALGEBRA
     survives wherever the solves exist -- the round-59 ENERGY-WALL
     pattern on this surface.
 (5) NO WALL POSITIVITY ENTERS THE CONSTRUCTION: frames and
     functionals use only the prime-free smooth world (v_sm,
     lam_sm) and comb linear algebra; PD of B_+ and positivity of
     s_+, R are MEASURED OUTCOMES on the target, never assumptions
     (the same code path executes on the controls).

FROZEN PROTOCOL (race machinery verbatim from
arithmetic_lift_race_probe / wall_matched_asymptotics_probe):

 W   LADDER + REPRODUCTION (kill -> PIPELINE-BROKEN / WARD-BROKEN):
     faithful rungs = kz in 2..KZMAX with H_MIN <= h <= HCAP and X
     <= ATOM_MAX; W1 >= MIN_RUNGS = 40; W2 WARD m_h > 0 everywhere;
     W3 WARD exact bookkeeping lift(v) - demand(v) = m_h; W4
     REPRODUCTION race ledger (slopes 0.077 rtol 20%, |dslope| <=
     0.005, exponent in [-2.5, -1.5]); W5 WARD demand(v_sm) =
     -lam_sm on EVERY rung (the S-IS-DEMAND identity).

 E1  THE BRIDGE, EXACT (kill -> WARD-BROKEN): E1.a X-VANISH
     |K_sm v_sm - lam_sm v_sm| <= RES_WARD x spectral scale; E1.b
     H-IS-HUB |H - lift(v_sm)| <= ID_WARD x max(1, |E_t|); E1.c
     R two routes on SUBSET_R: explicit |b_+|^2_{B_+^{-1}} (PD
     solve of P K_t P + v_sm v_sm^T) == n_+ - s_+ to R2_WARD
     relative on (|R| + |s_+|); E1.d FLUCT |b_+ - P dK v_sm| <=
     RES_WARD x scale (subset); E1.e DET-RATIO s_+ ==
     exp(slogdet K_t - slogdet(P K_t P + v_sm v_sm^T)) on the
     DET_N shallowest rungs (signs +1); E1.f SANDWICH m_h - tol <=
     s_+ <= n_+ + tol on every rung; E1.g R >= -RTOL_NEG on every
     rung (truth side).

 E2  THE CORRESPONDENCE ANSWER (typed, never kills): hub = H and
     demand = -s exact (from E1); the accumulated-R reading:
     med/range of R, R/m_h, and the exact mismatch demand - R per
     rung.  TYPED: CORRESPONDENCE-SPLIT(medR, medR/m) -- the
     envelope pair at alpha level is (H, -s) = (hub, demand)
     EXACTLY and R is a THIRD, margin-scale object; would be
     CORRESPONDENCE-FULL only if R tracked the demand (|R -
     demand|/demand <= 0.1 in median -- not expected).

 E3  THE SYMBOLIC COMMON TERM (typed): two-route wards (subset):
     n_+ == E_ar + E_t and n == E_ar + E_s (matrix vs lag read) to
     ID_WARD; the identity lift - demand = E_t + E_ar holds by
     construction on every rung (printed dev); affine fits of
     E_s/E_t/E_ar along v vs alpha (jackknife): TYPED
     GROWTH-SEAT(sE_s, sE_t, sE_ar) -- which functional carries the
     common 0.077 alpha growth; the common-term statement itself is
     an identity, typed SYMBOLIC-COMMON-TERM-EXACT.

 E4  RESIDUAL ANATOMY + TAU-SCREENS (typed): ladder of s_+/m_h and
     n_+/m_h and R/m_h; smooth-direction overlap ov = <v_sm, v>^2
     printed (branch crossings recorded, race S2.d); TAU-SCREENS
     (log-log OLS on positive subsets, counts printed): s_+ vs m_h,
     R vs m_h, n_+ vs m_h; bands PASS |s| <= 0.30 / RELOC >= 0.70 /
     else AMBIG.  TYPED: SPLUS-SCREEN-<PASS|RELOC|AMBIG>(slope),
     R-SCREEN-<...>, and NO-NEW-SOURCE-ONLY-POSITIVITY declared
     unless a screen PASSES with an O(1) floor (not expected).

 C   CONTROLS (kill -> WARD-BROKEN if silent): C1 smooth world
     lam_sm < 0 on EVERY rung (v883 regression); C2 Epstein
     x^2+5y^2 comb + scramble (seed 1) at kz 9 fire (lam_min < 0)
     on this surface; C3 ENERGY-WALL typed: on both controls the
     complement compression P K_ctrl P is INDEFINITE (min
     complement eig < 0: R stops being an energy) and/or s_+ <= 0,
     while the algebra survives (two-route R identity holds
     wherever the solves exist; deviation printed) ->
     ENERGY-WALL-SEEN(channels) / ENERGY-WALL-BLIND; C4 AST
     firewall; C5 NO-RH-CLAIM.

KILLS: K1 pipeline (W1) -> PIPELINE-BROKEN; K2 wards (W2-W5, E1,
C1/C2/C4) -> WARD-BROKEN.  E2/E3/E4/C3 typed outcomes are
measurements, never kills.

VERDICT (frozen enum): ENVELOPE-MEASURED with typed sublabels
BRIDGE-EXACT(maxdev), CORRESPONDENCE-SPLIT/-FULL,
SYMBOLIC-COMMON-TERM-EXACT + GROWTH-SEAT(...),
SPLUS-SCREEN-<...> + R-SCREEN-<...>, ENERGY-WALL-SEEN/BLIND; else
PIPELINE-BROKEN / WARD-BROKEN.

FROZEN BARS: KZMAX = 150; MIN_RUNGS = 40; SUBSET_R = (13, 40, 90);
DET_N = 2; RQ_WARD = 1e-10; ID_WARD = 1e-10; RES_WARD = 1e-9;
R2_WARD = 1e-6; RTOL_NEG = 1e-10; SAND_TOL = 1e-10; SLOPE_REF =
0.077 (rtol 0.20); DSLOPE_BAR = 0.005; EXPO_BAND = [-2.5, -1.5];
CORR_FULL_BAR = 0.1; SLOPE_PASS = 0.30; SLOPE_RELOC = 0.70;
CTRL_KZ = 9; scramble seed 1; jackknife = leave-one-out.

ANTI-CIRCULARITY (frozen): no sigma_h, no defect eigenvector, no
pivot sign as input, no factorization of the target matrix as a
certificate -- eigh/solve/slogdet of K_t appear ONLY as measured
outcomes and two-route identity wards, never as a positivity
certificate; all frames and functionals are prime-free or comb
linear algebra.  NO wall positivity is assumed anywhere in the
construction (Q5 above).

SMOKE-RUN DISCLOSURE (2026-08-10, before freezing): one smoke run of
this script (20/20 with the identical bars; NO bar, band, count,
rule or enum was moved after it) measured, recorded as the honest
context the frozen run must confirm -- INCLUDING two refuted a
priori expectations, frozen as such: 67 faithful rungs (h 142..
1433, 20.1 s); bridge exact -- X-VANISH <= 1e-9 scale, H-IS-HUB max
dev ~6e-14 class, S-IS-DEMAND (W5) exact, two-route R dev <= 7e-13,
FLUCT ward 6.9e-13, det-ratio 6.5e-13, sandwich slacks >= +4.8e-08
/ +4.1e-04 on 67/67, R >= +4.1e-04 on 67/67.  (i) REFUTED
EXPECTATION 1: R is NOT bare margin-scale -- it is OVERLAP-
DEFICIENCY scale: R med 9.5e-04 = 34.9 x m_h in median (range
[5.1, 3.2e+05], the extreme at the kz 97 branch crossing where
ov^2 = 0.0000), while s_+ hugs the margin (s_+/m med 1.027).  The
correspondence still SPLITS exactly as derived: mismatch |R -
demand|/demand med 0.9992, demand - R med 1.218 -- the
accumulated-R reading of the demand is DEAD; hub = H and demand =
-s are the exact envelope readings.  (ii) REFUTED EXPECTATION 2:
the common 0.077-alpha growth is NOT carried by -E_s alone -- the
seat is SPLIT: slope(E_s) = +0.2973 +- 2SE 0.0158, slope(E_t) =
+0.3742 +- 0.0181, slope(E_ar) = -0.3743 +- 0.0181 (E_t and -E_ar
mirror each other EXACTLY as the identity E_t + E_ar = m_h forces;
each leg's 0.077 = 0.3742 - 0.2973 is the difference of the
atom-read growth and the smooth-energy growth).  Screens: SPLUS
slope +0.825 (R^2 0.368) -> RELOC; R slope +0.203 (R^2 0.071) ->
PASS but tau-DEcorrelated (R^2 0.07 -- the same decorrelation
pattern as the round-59 Radau weight; R >= 0 is automatic on the
truth side, so this PASS carries NO new wall content -- said
plainly); NPLUS slope +0.220 (R^2 0.073), same reading; n_+/m med
35.9.  ENERGY-WALL-SEEN on 2/2 controls (Epstein: complement min
eig -1.0e+01; scramble: -7.9e+00 -- R stops being an energy on
both; algebra survives at 4.8e-15/0.0).  Fail-first preserved:
nothing was weakened; all four answers live in typed measurements.

SPEC v1 (2026-08-10, frozen + SHA-hashed before the frozen run):
everything above.  Mechanical concretizations frozen with v1: (i)
per-rung eigh of K_t and K_sm (values + bottom vectors), sign of
v_sm aligned to v; (ii) lag reads through core.lag_weights_from_v
exactly as the race probe; (iii) explicit-R solve via the PD
operator P K_t P + v_sm v_sm^T (subset only, matrices freed after
use); (iv) OLS population statistics + leave-one-out jackknife as
the matched-asymptotics probe; screens read positive subsets with
excluded counts printed.

NO RH claim: every identity here is exact finite linear algebra for
the deployed window family; the measured relocation of s_+ and R
proves nothing about tau_h > 0 for all h.  No marker moves.

FIREWALL: no zeros, no prime oracles (AST scan; banned ids zetazero
/ nzeros / primerange / isprime / primepi / nextprime / prevprime);
v563 READ-ONLY; RNG only inside the declared scramble control;
stdout only.

Sources (read-only): v563_paper2_readouts; race machinery verbatim
from arithmetic_lift_race_probe.py / wall_matched_asymptotics_
probe.py; the Schur-Ward identity from schur_ward_identity_probe.py
(round 59, declared input).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/schur_envelope_identity_probe.py
"""

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

import v563_paper2_readouts as core        # noqa: E402  (READ-ONLY)

KZMAX = 150
MIN_RUNGS = 40
SUBSET_R = (13, 40, 90)
DET_N = 2
RQ_WARD = 1e-10
ID_WARD = 1e-10
RES_WARD = 1e-9
R2_WARD = 1e-6
RTOL_NEG = 1e-10
SAND_TOL = 1e-10
SLOPE_REF = 0.077
SLOPE_RTOL = 0.20
DSLOPE_BAR = 0.005
EXPO_BAND = (-2.5, -1.5)
CORR_FULL_BAR = 0.1
SLOPE_PASS = 0.30
SLOPE_RELOC = 0.70
CTRL_KZ = 9
NG_SMOOTH = 6000
BANNED_IDS = ("zetazero", "nzeros", "primerange", "isprime",
              "primepi", "nextprime", "prevprime")

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


def ast_scan(banned):
    src = open(os.path.abspath(__file__), encoding="utf-8").read()
    bad = []
    for node in ast.walk(ast.parse(src)):
        name = None
        if isinstance(node, ast.Name):
            name = node.id
        elif isinstance(node, ast.Attribute):
            name = node.attr
        if name and name.lower() in banned:
            bad.append(name)
    return bad


def ols_line(x, y):
    x = np.asarray(x, float)
    y = np.asarray(y, float)
    vx = float(np.var(x))
    if vx == 0.0:
        return float(np.mean(y)), 0.0, float("nan")
    b = float(np.cov(x, y, bias=True)[0, 1] / vx)
    a = float(np.mean(y) - b * np.mean(x))
    ss = float(np.sum((y - a - b * x) ** 2))
    st = float(np.sum((y - np.mean(y)) ** 2))
    return a, b, (1.0 - ss / st if st > 0 else float("nan"))


def jack_fit(x, y):
    x = np.asarray(x, float)
    y = np.asarray(y, float)
    a, b, r2 = ols_line(x, y)
    n = len(x)
    aa, bb = [], []
    for i in range(n):
        m = np.ones(n, bool)
        m[i] = False
        ai, bi, _ = ols_line(x[m], y[m])
        aa.append(ai)
        bb.append(bi)
    aa = np.array(aa)
    bb = np.array(bb)
    se_a = math.sqrt((n - 1) / n * float(np.sum((aa - aa.mean())
                                                ** 2)))
    se_b = math.sqrt((n - 1) / n * float(np.sum((bb - bb.mean())
                                                ** 2)))
    return a, b, r2, se_a, se_b


def smooth_comb(alpha, ng=NG_SMOOTH):
    ug = (np.arange(ng) + 0.5) * (2.0 * alpha / ng)
    mg = 2.0 * np.exp(ug / 2.0) * (2.0 * alpha / ng)
    return ug, mg


def lambda_eps(N):
    """Epstein x^2+5y^2 comb (port_schur_reduction verbatim)."""
    r = np.zeros(N + 1)
    s = int(math.isqrt(N)) + 1
    for x in range(-s, s + 1):
        for y in range(-s, s + 1):
            v = x * x + 5 * y * y
            if 1 <= v <= N:
                r[v] += 1.0
    a = r / 2.0
    lam = np.zeros(N + 1)
    for n in range(2, N + 1):
        acc = a[n] * math.log(n)
        for dd in range(2, n):
            if n % dd == 0:
                acc -= lam[dd] * a[n // dd]
        lam[n] = acc
    return lam


def explicit_R(Kt, vsm):
    """Route 2: R = |b_+|^2_{B_+^{-1}} via the PD full-space
    operator P Kt P + vsm vsm^T (b_+ perp vsm)."""
    npl = Kt @ vsm
    n_plus = float(vsm @ npl)
    b_plus = npl - n_plus * vsm
    KP = Kt - np.outer(Kt @ vsm, vsm)
    PKP = KP - np.outer(vsm, vsm @ KP)
    PKP = 0.5 * (PKP + PKP.T)
    Aop = PKP + np.outer(vsm, vsm)
    z = np.linalg.solve(Aop, b_plus)
    return float(b_plus @ z), b_plus, PKP, Aop


def bridge_terms(Kt, vsm, lam_sm):
    """The exact envelope terms in the frozen v_sm frame."""
    n_plus = float(vsm @ (Kt @ vsm))
    x = np.linalg.solve(Kt, vsm)
    s_plus = 1.0 / float(vsm @ x)
    H = n_plus - lam_sm
    R1 = n_plus - s_plus
    return n_plus, s_plus, H, R1


def main():
    section("PRIME.PORT.SCHUR.ENVELOPE.01 -- the alpha-level "
            "lift-race pair vs the envelope split s_+ = s + H - R "
            "(EXPLORATION ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s"
          % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
    print("    NO RH claim; no marker moves.")
    print("\nS0 -- firewall")
    check("S0.1 AST firewall clean (C4)", not ast_scan(BANNED_IDS))

    # ------------------------------------------------------------ W
    section("W -- the faithful ladder (race surface) + bridge data")
    rungs = []
    for kz in range(2, KZMAX + 1):
        try:
            rr = core.build_window(kz)
        except Exception:
            continue
        if not (core.H_MIN <= rr["h"] <= core.HCAP):
            continue
        if rr["X"] > core.ATOM_MAX:
            continue
        alpha, M, D, h = rr["alpha"], rr["M"], rr["D"], rr["h"]
        uu = np.asarray(rr["uu"], float)
        mu = 2.0 * np.asarray(rr["lam"], float)
        c_at = np.asarray(core.atom_lags_at(alpha, M, uu, mu)[0],
                          float)
        c_ar = np.asarray(core.arch_lags(M, D), float)
        ug, mg = smooth_comb(alpha)
        c_sm = np.asarray(core.atom_lags_at(alpha, M, ug, mg)[0],
                          float)
        Kt = core.odd_toeplitz(c_ar + c_at, M)
        Ks = core.odd_toeplitz(c_ar + c_sm, M)
        w, V = np.linalg.eigh(Kt)
        v = V[:, 0]
        ws, Vs = np.linalg.eigh(Ks)
        vsm = Vs[:, 0]
        if float(v @ vsm) < 0:
            vsm = -vsm
        # lag reads (both directions)
        row = dict(kz=kz, alpha=float(alpha), M=M, D=float(D), h=h,
                   m=float(w[0]), lam_sm=float(ws[0]),
                   ov2=float(v @ vsm) ** 2,
                   wmax_s=float(np.max(np.abs(ws))))
        for tag, g in (("v", v), ("vsm", vsm)):
            Wg = core.lag_weights_from_v(g, h)
            row["Ear_" + tag] = float(c_ar @ Wg)
            row["Et_" + tag] = float(c_at @ Wg)
            row["Es_" + tag] = float(c_sm @ Wg)
        # bridge terms (frozen v_sm frame; smooth -> true)
        res = Ks @ vsm - row["lam_sm"] * vsm
        row["xvan"] = float(np.linalg.norm(res)) \
            / max(row["wmax_s"], 1.0)
        n_plus, s_plus, H, R1 = bridge_terms(Kt, vsm, row["lam_sm"])
        row.update(n_plus=n_plus, s_plus=s_plus, H=H, R1=R1)
        # subset: explicit R route 2 + fluctuation ward
        if kz in SUBSET_R:
            R2, b_plus, PKP, _A = explicit_R(Kt, vsm)
            dK = core.odd_toeplitz(c_at - c_sm, M)
            f = dK @ vsm
            f = f - float(vsm @ f) * vsm
            row["R2"] = R2
            row["fluct_dev"] = float(np.linalg.norm(b_plus - f)) \
                / max(float(np.linalg.norm(b_plus)), 1e-300)
            del PKP
        rungs.append(row)
        del Kt, Ks, V, Vs
    rungs.sort(key=lambda r: (r["h"], r["kz"]))
    check("W1 faithful ladder >= %d rungs" % MIN_RUNGS,
          len(rungs) >= MIN_RUNGS,
          "%d rungs, h %d..%d  [%.1f s]"
          % (len(rungs), rungs[0]["h"], rungs[-1]["h"],
             time.time() - T0), kill="K1")
    if KILLS:
        return finish({})
    ms = np.array([r["m"] for r in rungs])
    check("W2 WARD truth margin m_h > 0 everywhere (min %.3e)"
          % float(ms.min()), bool(np.all(ms > 0)), kill="K2")
    lifts_v = np.array([r["Et_v"] - r["Es_v"] for r in rungs])
    dems_v = np.array([-(r["Ear_v"] + r["Es_v"]) for r in rungs])
    dev_bk = float(np.max(np.abs((lifts_v - dems_v) - ms)
                          / np.maximum(1.0, np.abs(ms))))
    check("W3 WARD exact bookkeeping lift(v) - demand(v) = m_h: "
          "max dev %.2e <= %.0e" % (dev_bk, RQ_WARD),
          dev_bk <= RQ_WARD, kill="K2")
    als = np.array([r["alpha"] for r in rungs])
    hh = np.array([float(r["h"]) for r in rungs])
    aL, bL, r2L, _sa, sebL = jack_fit(als, lifts_v)
    aD, bD, r2D, _sa2, sebD = jack_fit(als, dems_v)
    _ae, p_exp, _r2e, _se, se_p = jack_fit(np.log(hh), np.log(ms))
    ok_w4 = (abs(bL / SLOPE_REF - 1.0) <= SLOPE_RTOL
             and abs(bD / SLOPE_REF - 1.0) <= SLOPE_RTOL
             and abs(bL - bD) <= DSLOPE_BAR
             and EXPO_BAND[0] <= p_exp <= EXPO_BAND[1])
    check("W4 REPRODUCTION race ledger: lift = %.4f a %+.3f (R^2 "
          "%.3f), demand = %.4f a %+.3f (R^2 %.3f), |dslope| %.1e, "
          "exponent %+.3f" % (bL, aL, r2L, bD, aD, r2D,
                              abs(bL - bD), p_exp),
          ok_w4, kill="K2")
    dems_sm = np.array([-(r["Ear_vsm"] + r["Es_vsm"])
                        for r in rungs])
    lam_sms = np.array([r["lam_sm"] for r in rungs])
    dev_w5 = float(np.max(np.abs(dems_sm + lam_sms)
                          / np.maximum(1.0, np.abs(lam_sms))))
    check("W5 WARD S-IS-DEMAND: demand(v_sm) = -lam_sm on every "
          "rung, max dev %.2e <= %.0e" % (dev_w5, RQ_WARD),
          dev_w5 <= RQ_WARD, kill="K2")

    # ------------------------------------------------------------ E1
    section("E1 -- the bridge, exact")
    xv = float(np.max([r["xvan"] for r in rungs]))
    check("E1.a WARD X-VANISH: |K_sm v_sm - lam_sm v_sm| / "
          "spectral scale <= %.0e (max %.2e) -> b = 0, x = 0 in "
          "the frozen frame" % (RES_WARD, xv), xv <= RES_WARD,
          kill="K2")
    Hs = np.array([r["H"] for r in rungs])
    lifts_sm = np.array([r["Et_vsm"] - r["Es_vsm"] for r in rungs])
    dev_h = float(np.max(np.abs(Hs - lifts_sm)
                         / np.maximum(1.0, np.abs(
                             [r["Et_vsm"] for r in rungs]))))
    check("E1.b WARD H-IS-HUB: H = Delta n = lift(v_sm), max dev "
          "%.2e <= %.0e -- the alpha-level hub IS the envelope "
          "linear term at this level" % (dev_h, ID_WARD),
          dev_h <= ID_WARD, kill="K2")
    sub = [r for r in rungs if r["kz"] in SUBSET_R]
    dev_r2 = max(abs(r["R1"] - r["R2"])
                 / max(abs(r["R1"]) + abs(r["s_plus"]), 1e-300)
                 for r in sub)
    check("E1.c WARD R two routes on subset %s: explicit "
          "|b_+|^2_{B_+^{-1}} == n_+ - s_+, max rel dev %.2e <= "
          "%.0e" % (list(SUBSET_R), dev_r2, R2_WARD),
          dev_r2 <= R2_WARD and len(sub) == len(SUBSET_R),
          kill="K2")
    dev_fl = max(r["fluct_dev"] for r in sub)
    check("E1.d WARD R-IS-FLUCT: b_+ = P dK v_sm (dK = the comb "
          "fluctuation operator), max rel dev %.2e <= %.0e"
          % (dev_fl, RES_WARD), dev_fl <= RES_WARD, kill="K2")
    # det-ratio on the DET_N shallowest rungs
    dev_det = 0.0
    sgn_ok = True
    for r in rungs[:DET_N]:
        rr = core.build_window(r["kz"])
        uu = np.asarray(rr["uu"], float)
        mu = 2.0 * np.asarray(rr["lam"], float)
        c_at = np.asarray(core.atom_lags_at(
            r["alpha"], r["M"], uu, mu)[0], float)
        c_ar = np.asarray(core.arch_lags(r["M"], r["D"]), float)
        ug, mg = smooth_comb(r["alpha"])
        c_sm = np.asarray(core.atom_lags_at(
            r["alpha"], r["M"], ug, mg)[0], float)
        Kt = core.odd_toeplitz(c_ar + c_at, r["M"])
        Ks = core.odd_toeplitz(c_ar + c_sm, r["M"])
        vsm = np.linalg.eigh(Ks)[1][:, 0]
        _n, s_plus, _H, _R = bridge_terms(Kt, vsm,
                                          float(np.linalg.eigh(
                                              Ks)[0][0]))
        _R2, _b, PKP, Aop = explicit_R(Kt, vsm)
        s1, ld1 = np.linalg.slogdet(Kt)
        s2, ld2 = np.linalg.slogdet(Aop)
        sgn_ok &= (s1 > 0 and s2 > 0)
        dev_det = max(dev_det, abs(s_plus - math.exp(ld1 - ld2))
                      / max(abs(s_plus), 1e-300))
        del Kt, Ks, PKP, Aop
    check("E1.e WARD DET-RATIO on %d shallowest rungs: s_+ = "
          "det(K_t)/det(B_+) (slogdet signs +1), max rel dev %.2e "
          "<= 1e-8 -- the positive-determinant shape of the "
          "residual, target-derived (declared, not a source-only "
          "certificate)" % (DET_N, dev_det),
          sgn_ok and dev_det <= 1e-8, kill="K2")
    spl = np.array([r["s_plus"] for r in rungs])
    npl = np.array([r["n_plus"] for r in rungs])
    sand_lo = float(np.min(spl - ms))
    sand_hi = float(np.min(npl - spl))
    check("E1.f WARD SANDWICH m_h <= s_+ <= n_+ on every rung "
          "(slacks min %.2e / %.2e >= -%.0e)"
          % (sand_lo, sand_hi, SAND_TOL),
          sand_lo >= -SAND_TOL and sand_hi >= -SAND_TOL,
          kill="K2")
    Rs = np.array([r["R1"] for r in rungs])
    check("E1.g WARD R >= 0 on the truth side (min %.2e >= -%.0e)"
          % (float(Rs.min()), RTOL_NEG),
          float(Rs.min()) >= -RTOL_NEG, kill="K2")

    # ------------------------------------------------------------ E2
    section("E2 -- the correspondence answer (typed)")
    print("      kz    h    alpha    m_h        s_+        R      "
          "   demand     R/m    ov^2")
    for r in rungs[:4] + rungs[-4:]:
        print("    %4d %5d  %6.3f  %.3e  %.3e  %.3e  %8.4f  "
              "%6.3f  %.4f"
              % (r["kz"], r["h"], r["alpha"], r["m"], r["s_plus"],
                 r["R1"], -(r["Ear_vsm"] + r["Es_vsm"]),
                 r["R1"] / r["m"], r["ov2"]))
    Rm = Rs / ms
    dems_pos = -lam_sms
    mism = np.abs(Rs - dems_pos) / np.abs(dems_pos)
    print("    R: med %.2e, R/m med %.3f (range [%.3f, %.3f]); "
          "mismatch |R - demand|/demand med %.4f; demand - R med "
          "%.4f" % (float(np.median(Rs)), float(np.median(Rm)),
                    float(np.min(Rm)), float(np.max(Rm)),
                    float(np.median(mism)),
                    float(np.median(dems_pos - Rs))))
    if float(np.median(mism)) <= CORR_FULL_BAR:
        e2 = "CORRESPONDENCE-FULL(med-mismatch=%.3f)" % float(
            np.median(mism))
    else:
        e2 = ("CORRESPONDENCE-SPLIT(medR=%.1e, medR/m=%.2f)"
              % (float(np.median(Rs)), float(np.median(Rm))))
    check("E2.1 typed: %s -- hub = H exact (E1.b), demand = -s "
          "exact (W5); the accumulated-R reading of the demand is "
          "%s: R is the margin-scale adaptation defect, a THIRD "
          "object" % (e2, "ALIVE" if "FULL" in e2 else "DEAD"),
          True)

    # ------------------------------------------------------------ E3
    section("E3 -- the symbolic common term (identity + growth "
            "seat)")
    dev_2r = 0.0
    for r in sub:
        dev_2r = max(dev_2r, abs(r["n_plus"]
                                 - (r["Ear_vsm"] + r["Et_vsm"]))
                     / max(1.0, abs(r["n_plus"])))
        dev_2r = max(dev_2r, abs(r["lam_sm"]
                                 - (r["Ear_vsm"] + r["Es_vsm"]))
                     / max(1.0, abs(r["lam_sm"])))
    check("E3.1 WARD two-route (matrix vs lag read) on subset: "
          "n_+ == E_ar + E_t and n == E_ar + E_s, max dev %.2e <= "
          "%.0e -- the decomposition into the three explicit "
          "functionals is an identity, so the common term -E_s of "
          "hub and demand cancels IDENTICALLY (not by fit)"
          % (dev_2r, ID_WARD), dev_2r <= ID_WARD, kill="K2")
    Es_v = np.array([r["Es_v"] for r in rungs])
    Et_v = np.array([r["Et_v"] for r in rungs])
    Ear_v = np.array([r["Ear_v"] for r in rungs])
    _a1, sE_s, _r1, _q1, se_s = jack_fit(als, Es_v)
    _a2, sE_t, _r2, _q2, se_t = jack_fit(als, Et_v)
    _a3, sE_a, _r3, _q3, se_a = jack_fit(als, Ear_v)
    print("    along v: slope(E_s) = %+.4f +- 2SE %.4f; slope(E_t)"
          " = %+.4f +- %.4f; slope(E_ar) = %+.4f +- %.4f; "
          "slope(lift) = %+.4f, slope(demand) = %+.4f"
          % (sE_s, 2 * se_s, sE_t, 2 * se_t, sE_a, 2 * se_a,
             bL, bD))
    e3 = ("GROWTH-SEAT(sEs=%+.4f, sEt=%+.4f, sEar=%+.4f)"
          % (sE_s, sE_t, sE_a))
    check("E3.2 typed: SYMBOLIC-COMMON-TERM-EXACT(-E_s) + %s -- "
          "which functional carries the common 0.077-alpha growth "
          "of both legs" % e3, True)

    # ------------------------------------------------------------ E4
    section("E4 -- residual anatomy + tau-screens")
    print("    s_+/m: med %.3f range [%.3f, %.3f]; n_+/m: med "
          "%.3f range [%.3f, %.3f]; overlap ov^2 med %.4f min "
          "%.4f (branch crossings recorded)"
          % (float(np.median(spl / ms)), float(np.min(spl / ms)),
             float(np.max(spl / ms)), float(np.median(npl / ms)),
             float(np.min(npl / ms)), float(np.max(npl / ms)),
             float(np.median([r["ov2"] for r in rungs])),
             float(np.min([r["ov2"] for r in rungs]))))
    scr = {}
    for nm, arr in (("SPLUS", spl), ("R", Rs), ("NPLUS", npl)):
        pos = arr > 0
        if int(np.sum(pos)) >= 3:
            _a, sl, r2f = ols_line(np.log(ms[pos]),
                                   np.log(arr[pos]))
        else:
            sl, r2f = float("nan"), float("nan")
        if abs(sl) <= SLOPE_PASS:
            lab = "PASS"
        elif sl >= SLOPE_RELOC:
            lab = "RELOC"
        else:
            lab = "AMBIG"
        scr[nm] = "%s-SCREEN-%s(slope=%+.3f)" % (nm, lab, sl)
        print("    tau-screen %s vs m_h: slope %+.4f (R^2 %.3f, "
              "%d excluded) -> %s"
              % (nm, sl, r2f, int(np.sum(~pos)), lab))
    check("E4.1 typed: %s / %s / %s -- RELOC = the residual is "
          "the wall margin relocated; NO new source-only "
          "positivity is claimed unless a screen PASSES with an "
          "O(1) floor" % (scr["SPLUS"], scr["R"], scr["NPLUS"]),
          True)

    # ------------------------------------------------------------ C
    section("C -- controls (smooth / Epstein / scramble; "
            "ENERGY-WALL)")
    check("C1 WARD smooth world violates at rung level: lam_sm < "
          "0 on %d/%d rungs (v883 regression)"
          % (int(np.sum(lam_sms < 0)), len(rungs)),
          bool(np.all(lam_sms < 0)), kill="K2")
    rr9 = core.build_window(CTRL_KZ)
    alpha9, M9, D9 = rr9["alpha"], rr9["M"], rr9["D"]
    c_ar9 = np.asarray(core.arch_lags(M9, D9), float)
    ug9, mg9 = smooth_comb(alpha9)
    c_sm9 = np.asarray(core.atom_lags_at(alpha9, M9, ug9,
                                         mg9)[0], float)
    Ks9 = core.odd_toeplitz(c_ar9 + c_sm9, M9)
    ws9, Vs9 = np.linalg.eigh(Ks9)
    vsm9 = Vs9[:, 0]
    lam9 = float(ws9[0])
    N_E = int(math.floor(math.exp(2.0 * alpha9))) + 1
    lamE_ = lambda_eps(N_E)
    nn = np.nonzero(np.abs(lamE_) > 1e-12)[0]
    c_E = np.asarray(core.atom_lags_at(
        alpha9, M9, np.log(nn.astype(float)),
        2.0 * lamE_[nn] / np.sqrt(nn.astype(float)))[0], float)
    rr_s = core.build_window(CTRL_KZ, scramble_seed=1)
    c_scr = np.asarray(core.atom_lags_at(
        rr_s["alpha"], rr_s["M"], np.asarray(rr_s["uu"], float),
        2.0 * np.asarray(rr_s["lam"], float))[0], float)
    fired = True
    ew_chan = []
    for name, c_c in (("Epstein", c_E), ("scramble", c_scr)):
        Kc = core.odd_toeplitz(c_ar9 + c_c, M9)
        lam_c = float(np.linalg.eigvalsh(Kc)[0])
        fired &= lam_c < 0
        # same bridge algebra on the control world
        n_p = float(vsm9 @ (Kc @ vsm9))
        try:
            xk = np.linalg.solve(Kc, vsm9)
            s_p = 1.0 / float(vsm9 @ xk)
        except np.linalg.LinAlgError:
            s_p = float("nan")
        R2c, b_p, PKPc, Aopc = explicit_R(Kc, vsm9)
        evP = np.linalg.eigvalsh(PKPc)
        # complement min eig: drop the (single) ~0 eigenvalue of
        # the v_sm direction
        i0 = int(np.argmin(np.abs(evP)))
        comp = np.delete(evP, i0)
        cmin = float(np.min(comp))
        dev_alg = (abs((n_p - s_p) - R2c)
                   / max(abs(n_p - s_p) + abs(s_p), 1e-300)
                   if np.isfinite(s_p) else float("nan"))
        seen = (cmin < 0) or (np.isfinite(s_p) and s_p <= 0)
        if seen:
            ew_chan.append("%s(compmin=%.1e, s_+=%.1e)"
                           % (name, cmin, s_p))
        print("    %-9s: lam_min %+.3e -> %s; complement min eig "
              "%+.3e; s_+ %+.3e; two-route algebra dev %.1e"
              % (name, lam_c, "FIRES" if lam_c < 0 else "SILENT",
                 cmin, s_p, dev_alg), flush=True)
        del Kc, PKPc, Aopc
    check("C2 WARD both controls fire on this surface (lam_min < "
          "0)", fired, kill="K2")
    ew = ("ENERGY-WALL-SEEN(%s)" % "; ".join(ew_chan) if ew_chan
          else "ENERGY-WALL-BLIND")
    check("C3 typed: %s -- R stops being an energy / s_+ loses "
          "positivity exactly where the wall is violated, while "
          "the completion-of-square algebra survives" % ew, True)

    return finish(dict(dev=max(xv, dev_h, dev_r2, dev_fl),
                       e2=e2, e3=e3, scr=scr, ew=ew))


def finish(labels):
    section("V -- FROZEN VERDICT")
    n_pass = sum(1 for _n, okk in CHECKS if okk)
    n_tot = len(CHECKS)
    if KILLS:
        VERDICT = {"K1": "PIPELINE-BROKEN",
                   "K2": "WARD-BROKEN"}[KILLS[0]]
        print("\n  VERDICT: %s" % VERDICT)
    else:
        VERDICT = ("ENVELOPE-MEASURED / BRIDGE-EXACT(%.1e) / %s / "
                   "SYMBOLIC-COMMON-TERM-EXACT + %s / %s / %s / %s"
                   % (labels["dev"], labels["e2"], labels["e3"],
                      labels["scr"]["SPLUS"], labels["scr"]["R"],
                      labels["ew"]))
        print("\n  VERDICT: %s" % VERDICT)
    print("""
  HONEST FRAME (as frozen): every identity here is exact finite
  linear algebra on the deployed window family -- the bridge maps
  the alpha-level lift-race pair onto the envelope terms (hub = H,
  demand = -s) exactly, and the third term R is measured, not
  conjectured.  RELOC screens mean the residual objects are the
  wall margin relocated -- no new positivity.  NO RH claim.  No
  marker moves.""")
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed"
          % (time.time() - T0, n_tot, n_tot - n_pass))
    return 0 if n_pass == n_tot else 1


if __name__ == "__main__":
    raise SystemExit(main())
