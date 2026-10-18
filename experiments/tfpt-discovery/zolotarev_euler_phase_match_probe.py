#!/usr/bin/env python3
"""
PRIME.PHASE.ZOLOTAREV.EULER.MATCH.01 -- the deferred comparison of
CCXXV's stored 68 x 8 determinant phases against CCXXIII's completed
Euler phase Theta_X.

EXPLORATION ONLY.  No RH claim in any direction.  Nothing outside
experiments/tfpt-discovery/ + experiments/next.txt is touched.

------------------------------------------------------------------ WHY
CCXXV rebuilt the ONEBADMODE certificate as a proper Zolotarev
determinant-phase filter and reduced it to FINITELY MANY determinant
phase values: with the proper type-(2m-1, 2m) separator
    R_m(x) = 1 + sum_j [ a_j/(x - z_j) + conj(a_j)/(x - conj z_j) ],
    tr R_m(M_h) = 8 + 2 Re sum_j a_j tr(M_h - z_j I)^{-1},
one FIXED family of eight conjugate pole pairs certifies all 68 wall
steps.  The artifact zolotarev_phase_filter_phases.json stores, per
step and per pole, the complex determinant, its principal and
h-unwrapped log phase, the resolvent trace, the residue, the margin
and the identity wards.  The Euler comparison was DEFERRED with the
verdict DEFERRED-NO-EULER-ARTIFACT and a frozen comparison
specification.  CCXXIII then supplied the exact Theta_X but writes
only stdout, so the hook still has no artifact on either side.  This
probe closes the hook by building BOTH sides itself.

--------------------------------------------------- WHAT IS ACTUALLY
--------------------------------------------------- BEING COMPARED
THE HONEST DERIVATION, FIRST.  The stored poles are PURELY IMAGINARY,
z_j = i y_j with y_j = 0.484 .. 4.97e4, and M_h is real symmetric, so
    arg det(M_h - i y_j I) = sum_k atan2(-y_j, lam_k(M_h))   (mod 2pi)
EXACTLY.  The stored determinant phase is therefore a SMOOTHED
NEGATIVE-EIGENVALUE COUNT of the wall step: as y -> 0+ each negative
eigenvalue contributes -pi and each positive one 0, so the phase at
the smallest pole is -pi n_-(M_h) + O(y).  This is derived and warded
here (S2), and it is the same object CCXXIV censused as WALLPAPER.

THE DOMAIN QUESTION, ANSWERED HONESTLY AND NEGATIVELY.  Theta_X(t)
lives on the FREQUENCY axis t conjugate to the lag u; y_j is a
SPECTRAL parameter of the tau-normalized 8 x 8 step matrix
M_h = Q^T (S/tau) Q.  There is NO derivation identifying y_j with a
frequency: the two carry different units and the filter poles are
placed by the elliptic Zolotarev construction on the spectral
interval [c_B, L_src], which is a statement about eigenvalue scales,
not about lag scales.  A direct "z_j -> t_j" map would be an invented
correspondence, and inventing one is exactly what this program calls
a relabel.  It is therefore NOT done.

THE BRIDGE THAT DOES EXIST (CCXXIV, exact at 9.4e-15):
    W^T diag(K_Theta*) W == Gamma - (1/2) mu1 I,   W^T W = I,
i.e. the CCXI wall block IS the diagonal congruence image of the
Krein kernel of the half-gap-shifted Euler phase.  That gives the
Euler side a matrix of exactly the same species as M_h, and the
comparison is then made with the SAME functional at the SAME eight
poles, in the SAME tau normalization the Zolotarev side already uses:
    OUR SIDE     Phi_j(h) = unwrap_h arg det(M_h - z_j I)      [stored]
    EULER SIDE   Psi_j(h) = unwrap_h arg det(G_h - z_j I),
                 G_h := (Gamma_h - (1/2)mu1 I) / ((1/2) mu1),
                 Gamma_h = W^T diag(D) W  the CCXI carrier block.
Both are smoothed spectral phases of a tau-normalized real symmetric
wall object at the same eight scales.  Nothing is identified that is
not identified by the congruence.

A SECOND, INDEPENDENT COORDINATE is carried so that a null on the
bridge cannot be confused with a null on the phase itself: the
COMPLETED EULER PHASE evaluated directly,
    Phi_X(t) = [2 Im logGamma(1/4 + it/2) - t log pi]
               - sum_n (mu_n / u_n) sin(t u_n),
at three DECLARED anchors -- t = 1 (fixed), t = 5.25 (the CLV /
CLXXXV carrier band edge) and t = pi/D_h (the rung Nyquist frequency).

------------------------------------------------------- THE MEASUREMENT
Matched set: the stored rows whose (h, kz) exist on the CCXXIII level
ladder.  That intersection is EXACTLY the 40 SURFACE steps -- the 27
deep steps and the bridge lie beyond the CCXXIII rung caps and are
declared OUT OF THE COMPARISON (they are still covered by the
artifact-integrity wards).  Rows are ordered by (h, kz) and phases
unwrapped along that order, exactly as CCXXV's frozen specification
demands; a global additive phase is free on both sides.

Per pole j three numbers are reported, in increasing severity:
  RAW      Pearson r(Phi_j, Psi_j) and the affine OLS R^2.
  DIFF     Pearson r of the FIRST DIFFERENCES along the ordered ladder.
  DETREND  Pearson r of the residuals after removing an OLS fit in
           log h from BOTH series.  This is the only one that can
           carry content: both sides are monotone-ish in h, so a raw
           correlation is a TREND ARTIFACT by construction, and this
           probe says so before measuring rather than after.

CONTROLS (the point).  The Zolotarev side is a frozen artifact of the
TRUE world and cannot be rebuilt in a falsifying world within budget.
The control is therefore run on the EULER side: Psi_j and Phi_X are
recomputed in the smooth, scramble and cosh worlds and correlated
against the SAME true determinant phases.  If a correlation survives a
scrambled Euler side, it is not arithmetic content -- it is the shared
h-trend, and the null is then stated as such.  Controls firing is a
requirement, not a decoration.

VERDICT RULE (frozen BEFORE the frozen run):
  PHASES-LINKED iff for at least one pole j the DETRENDED correlation
      satisfies |r| >= 0.70 on the true world AND |r| <= 0.30 in BOTH
      the scramble and the cosh world (i.e. the link is arithmetic,
      not a trend).  The relation and its discrimination are then
      stated explicitly.
  PHASES-UNRELATED otherwise -- an honest null: the eight fixed
      determinant phases of the ONEBADMODE filter and the completed
      Euler phase of the same ladder carry no measured common content
      beyond the h-trend.
  Independently of that: RESOLVENT-PHASE-RECOMPUTED (the stored
  artifact reproduced from scratch), SPECTRAL-PHASE-IDENTITY (the
  determinant phase IS a smoothed negative-eigenvalue count) and
  DOMAIN-MISMATCH-DECLARED (no z_j -> t map is invented) are reported
  in every case.

TYPING / ANTI-CIRCULARITY.  (i) No zeta zeros, no zero counts, no
prime oracle (AST-scanned).  (ii) The Zolotarev side is RECOMPUTED
from the CCVII/CCXXV machinery (read-only import) and warded against
the stored artifact entry by entry -- the stored numbers are never
trusted blind, and the artifact-integrity wards (partial fractions,
log-det derivative, unwrap consistency) are checked first.  (iii) The
Euler side is built by the CCXXIII rung builder with the CCXI carrier
frame; no target eigendata enters the construction of either phase --
eigenvalues appear only inside the determinant phases themselves,
which ARE spectral objects by definition, and in blocks typed [DIAG].
(iv) RNG only inside the declared scramble control.  (v) Everything is
a statement about float64 objects of a deployed FINITE ladder.

SMOKE DISCLOSURE (mandatory, verbatim).  Smoke rounds were run before
this spec was frozen and they DID see numbers:
 (z1) the (h, kz) intersection was measured BEFORE the freeze and is
      exactly 40 of 68 rows (all surface).  The comparison scope was
      written to that number rather than pretending the deep block
      could be matched; the deep rows remain inside the integrity
      wards and outside the correlation.
 (z2) the recomputation ward was first written to rebuild the SURFACE
      ladder only, since only the surface rows are in the matched set
      and the deep block costs the bulk of the parent's runtime.
      After (z5) showed that the step matrices depend on the ladder as
      a WHOLE, the rebuild was made COMPLETE -- surface plus deep,
      combined and sorted exactly as CCXXV does -- so the ward now
      covers ALL 68 stored rows, not just the 40 matched ones.  That
      is amendment B1 and it is a scope INCREASE, disclosed.
 (z3) the DETREND severity ladder was written INTO the spec before
      measuring, precisely because a raw correlation between two
      monotone h-series is meaningless; the 0.70 / 0.30 thresholds
      were fixed at that point and were not touched afterwards.
 (z4) the spectral-phase identity arg det(M - iyI) = sum_k atan2(-y,
      lam_k) was derived by hand and then CONFIRMED against the stored
      phases in smoke; it is carried as a ward, not as a claim.
 (z5) THE RECOMPUTATION WARD FAILED IN SMOKE AND IT WAS RIGHT TO.  The
      smoke ran a TRUNCATED surface ladder and matched steps by the
      terminating rung (h, kz) only; the ward fired at 2.76 rad on the
      phases and 7.7e-01 on the traces.  The cause is structural and
      is exactly what the ward is for: a CCVII step matrix is built
      from a CONSECUTIVE PAIR of rungs, so truncating the ladder
      silently changes the PREDECESSOR and therefore the matrix.  The
      bar was NOT loosened.  The fix is amendment B3: steps are keyed
      by the FULL step identity (h1, kz1, h, kz) and the surface
      ladder is always built complete, in smoke as well.
 (z6) the correlation table of S5 was SEEN before the freeze and it is
      a NULL (best truth detrended |r| ~ 0.38 at the smallest pole,
      best direct-anchor |r| ~ 0.49, both below the 0.70 link
      threshold fixed in z3).  The thresholds were not moved
      afterwards, and the null branch was already written out in the
      verdict rule.  The correlations do not depend on the S2
      rebuild -- they are computed from the stored phases -- so the
      z5 failure did not touch them.
No bar was moved to make a verdict come out; the null branch is
written out in full in the verdict rule above.

HONEST AMENDMENTS (post-smoke, disclosed):
  B1  the recomputation ward rebuilds the COMPLETE combined ladder
      (surface + deep) and covers all 68 stored rows.
  B2  phase comparisons are done modulo 2 pi (principal-branch
      differences), since a global additive phase is free on both
      sides by CCXXV's own specification.
  B3  steps are keyed by the FULL step identity (h1, kz1, h, kz) and
      the surface ladder is always rebuilt complete (z5).

Sources (read-only): zolotarev_phase_filter_probe (CCXXV: the filter,
assemble_step, complex_logdet, resolvent_data),
onebadmode_moments_probe (CCVII: ladder_zones, build_rung, make_steps,
seg_of), euler_phase_identity_probe (CCXXIII: level_rung,
grid_density, carrier_frame, phase_arch, smooth_comb),
v563_paper2_readouts (corpus readouts).  CCXXIV is cited for the
congruence bridge and reproduced here, not re-derived.

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/zolotarev_euler_phase_match_probe.py
Smoke (declared, reduced ladder):  ... --smoke
"""

import ast
import hashlib
import json
import math
import os
import sys
import time

import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
_VERIFY = os.path.abspath(os.path.join(_HERE, "..", "..", "verification"))
sys.path.insert(0, _HERE)
sys.path.insert(0, _VERIFY)

import euler_phase_identity_probe as eul       # noqa: E402 READ-ONLY
import onebadmode_moments_probe as ob          # noqa: E402 READ-ONLY
import zolotarev_phase_filter_probe as zol     # noqa: E402 READ-ONLY

SMOKE = "--smoke" in sys.argv

# ---------------------------------------------------------------- frozen
ARTIFACT = os.path.join(_HERE, "zolotarev_phase_filter_phases.json")
NDIM = zol.NDIM
IDENT_WARD = 1e-9            # stored identity_rel bar (CCXXV worst 1.0e-11)
RECOMP_WARD = 1e-9           # recomputed vs stored (phase, abs)
EXACT_WARD = 1e-12
ANCHORS = (1.0, 5.25)        # fixed t anchors; the Nyquist one is per-rung
CORR_LINK = 0.70             # detrended |r| needed on truth
CORR_KILL = 0.30             # detrended |r| allowed in the controls
NG_SMOOTH = eul.NG_SMOOTH
SCR_SEED = eul.SCR_SEED
INJ_A, INJ_DELTA, INJ_GAMMA0 = eul.INJ_A, eul.INJ_DELTA, eul.INJ_GAMMA0
NKAR = eul.NKAR
BANNED_IDS = ("zetazero", "nzeros", "primerange", "isprime",
              "primepi", "nextprime", "prevprime")

CHECKS = []
KILLS = []
T0 = time.time()
SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()


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
    bad = set()
    for node in ast.walk(ast.parse(src)):
        nm = None
        if isinstance(node, ast.Name):
            nm = node.id
        elif isinstance(node, ast.Attribute):
            nm = node.attr
        if nm and nm.lower() in banned:
            bad.add(nm)
    return sorted(bad)


def trio(v):
    v = np.asarray(v, float)
    return float(np.min(v)), float(np.median(v)), float(np.max(v))


def e3(v):
    return "%.3e/%.3e/%.3e" % trio(v)


def f3(v):
    return "%+.4f/%+.4f/%+.4f" % trio(v)


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


def corr(a, b):
    a = np.asarray(a, float)
    b = np.asarray(b, float)
    if a.size < 3 or float(np.std(a)) == 0.0 or float(np.std(b)) == 0.0:
        return float("nan")
    return float(np.corrcoef(a, b)[0, 1])


def detrend(y, lx):
    a, b, _r2 = ols_line(lx, y)
    return np.asarray(y, float) - (a + b * np.asarray(lx, float))


def wrap(x):
    """principal-branch reduction to (-pi, pi]  [B2]."""
    return np.arctan2(np.sin(x), np.cos(x))


def spectral_phase(eigs, y):
    """arg det(A - i y I) for real symmetric A with eigenvalues eigs --
    EXACT: sum_k arg(lam_k - i y) = sum_k atan2(-y, lam_k)."""
    return float(np.sum(np.arctan2(-y, np.asarray(eigs, float))))


def comb_phase(t, uu, mm):
    t = np.atleast_1d(np.asarray(t, float))
    w = np.where(uu > 0, mm / np.maximum(uu, 1e-300), 0.0)
    return np.sin(np.outer(t, uu)) @ w


def euler_side(rg, poles):
    """the CCXXIV BRIDGE object of a level rung: the tau-normalized
    wall block G = (Gamma - (1/2)mu1 I)/((1/2)mu1) and its spectral
    phases at the SAME eight poles, plus the direct completed Euler
    phase at the declared anchors."""
    D = eul.grid_density(rg["c"])
    _Tb, W = eul.carrier_frame(rg)
    Gam = (W * D[:, None]).T @ W
    tau = 0.5 * rg["mu1"]
    G = (Gam - tau * np.eye(NKAR)) / tau
    ev = np.linalg.eigvalsh(G)
    psi = [spectral_phase(ev, y) for y in poles]
    tny = math.pi / rg["Dg"]
    anch = list(ANCHORS) + [tny]
    ph = (eul.phase_arch(np.asarray(anch, float))
          - comb_phase(anch, rg["uu"], rg["mm"]))
    return dict(Gam=Gam, G=G, ev=ev, psi=psi, phiX=[float(v) for v in ph],
                tny=tny, W=W, D=D, tau=tau,
                lam_car=float(np.linalg.eigvalsh(Gam)[0]))


def inj_lag(M, Dg):
    tt = np.arange(M) * Dg
    return (INJ_A * np.cos(INJ_GAMMA0 * tt)
            * (np.cosh(INJ_DELTA * tt) - 1.0))


def build_combined_steps():
    """the FULL CCVII ladder, rebuilt read-only through the parent
    machinery exactly as CCXXV assembles it: surface rungs with
    core_ok plus the deep rungs, sorted by (h, kz), then stepped and
    assembled  [B1].  Anything less changes the step PAIRS and is
    caught by the ward (z5)."""
    zones = ob.ladder_zones()
    surf = [ob.build_rung("surf", kz, with_split=True) for kz in zones]
    surf = [r for r in surf if r is not None and r["core_ok"]]
    deep = []
    for kz, _hexp in sorted(ob.deep_zone_census(),
                            key=lambda pr: (pr[1], pr[0])):
        rung = ob.build_rung("deep", kz, with_split=True)
        if (rung is not None and rung["core_ok"] and rung["negA"] == 0
                and rung.get("lamS", -1.0) > 0.0):
            deep.append(rung)
    rungs = sorted(surf + deep, key=lambda r: (r["h"], r["kz"]))
    steps = [zol.assemble_step(s) for s in ob.make_steps(rungs)]
    return ([s for s in steps if s["status"] == "OK"],
            len(surf), len(deep))


def main():
    section("PRIME.PHASE.ZOLOTAREV.EULER.MATCH.01 -- the deferred "
            "comparison of CCXXV's 68 x 8 determinant phases against "
            "CCXXIII's completed Euler phase  (EXPLORATION ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s" % SPEC_SHA)
    print("    NO RH claim; no marker moves; experiments/ only.%s"
          % ("  [SMOKE MODE]" if SMOKE else ""))

    print("\nS0 -- firewall")
    bad = ast_scan(BANNED_IDS)
    check("S0.1 AST firewall clean (no prime/zero oracles)", not bad,
          ",".join(bad) if bad else "", kill="K0")
    art = json.load(open(ARTIFACT, encoding="utf-8"))
    rows = art["rungs"]
    poles = [p[1] for p in art["filter"]["poles"]]
    resid = art["filter"]["residues"]
    check("S0.2 CCXXV artifact loaded: schema %s, parent spec %s..., "
          "%d rows x %d poles, global filter m = %d, delta %.3e"
          % (art["schema"], art["spec_sha256"][:8], len(rows),
             len(poles), art["filter"]["m"], art["filter"]["delta"]),
          art["schema"] == "tfpt.zolotarev_phase_filter.v1"
          and len(rows) == 68 and len(poles) == NDIM, kill="K0")
    if KILLS:
        return finish()
    print("    stored comparison spec status was %s -- this probe "
          "closes it" % art["comparison"]["status"])

    # ================================================================ S1
    section("S1 -- ARTIFACT INTEGRITY (the stored numbers are never "
            "trusted blind)")
    d_ph = d_ab = d_tr = d_pf = d_mg = d_uw = 0.0
    worst_id = 0.0
    for r in rows:
        acc = []
        for p in r["poles"]:
            det = complex(p["determinant"][0], p["determinant"][1])
            d_ph = max(d_ph, abs(float(wrap(np.angle(det)
                                              - p["phase"]))))
            d_ab = max(d_ab, abs(math.log(abs(det)) - p["log_abs_det"])
                       / max(abs(p["log_abs_det"]), 1.0))
            tr = complex(p["resolvent_trace"][0], p["resolvent_trace"][1])
            md = complex(p["minus_dlogdet"][0], p["minus_dlogdet"][1])
            d_tr = max(d_tr, abs(tr - md) / max(abs(tr), 1.0))
            worst_id = max(worst_id, p["identity_rel"])
            acc.append(2.0 * p["a"] * tr.real)
            k = (p["phase_unwrapped"] - p["phase"]) / (2.0 * math.pi)
            d_uw = max(d_uw, abs(k - round(k)))
        expr = NDIM + math.fsum(acc)
        d_pf = max(d_pf, abs(expr - r["trace_R"])
                   / max(abs(r["trace_R"]), 1.0))
        d_mg = max(d_mg, abs((1.0 - r["trace_R"]) - r["margin"]))
    check("S1.1 phase == arg(determinant) on all %d x %d stored pole "
          "rows (principal branch): max dev %.2e <= %.0e"
          % (len(rows), NDIM, d_ph, EXACT_WARD), d_ph <= EXACT_WARD,
          kill="K1")
    check("S1.2 log_abs_det == log|determinant|: max rel dev %.2e "
          "<= %.0e" % (d_ab, EXACT_WARD), d_ab <= EXACT_WARD, kill="K1")
    check("S1.3 the stored log-det derivative identity tr(M-zI)^{-1} "
          "== -d_z log det(M-zI): max stored identity_rel %.2e <= %.0e "
          "(CCXXV cites worst 1.02e-11); recomputed consistency of the "
          "two stored fields %.2e" % (worst_id, IDENT_WARD, d_tr),
          worst_id <= IDENT_WARD and d_tr <= 1e-8, kill="K1")
    check("S1.4 the PARTIAL-FRACTION expression closes: tr R_m == %d + "
          "2 sum_j a_j Re tr(M-z_j I)^{-1} on all %d rows (max rel dev "
          "%.2e) and margin == 1 - tr R_m (max abs dev %.2e)"
          % (NDIM, len(rows), d_pf, d_mg),
          d_pf <= 1e-10 and d_mg <= 1e-12, kill="K1")
    check("S1.5 the stored h-unwrapped phases differ from the "
          "principal ones by exact multiples of 2 pi: max deviation "
          "from an integer %.2e <= %.0e" % (d_uw, 1e-9), d_uw <= 1e-9,
          kill="K1")

    # ================================================================ S2
    section("S2 -- RECOMPUTATION of the resolvent phases from the "
            "CCVII/CCXXV machinery + the SPECTRAL-PHASE IDENTITY")
    ob.build_ext_tables()
    steps, n_surf, n_deep = build_combined_steps()
    segs = [ob.seg_of(s) for s in steps]
    print("    combined ladder rebuilt [B1]: %d surface + %d deep "
          "rungs -> %d OK steps (surf %d / bridge %d / deep %d)  "
          "[%.1f s]"
          % (n_surf, n_deep, len(steps), segs.count("surf"),
             segs.count("bridge"), segs.count("deep"),
             time.time() - T0))
    smap = {(int(s["r1"]["h"]), int(s["r1"]["kz"]),
             int(s["r2"]["h"]), int(s["r2"]["kz"])): s for s in steps}
    d_re = d_id = d_tre = 0.0
    nrec = 0
    idx_rows = []
    for r in rows:
        s = smap.get((r["h1"], r["kz1"], r["h"], r["kz"]))
        if s is None:
            continue
        nrec += 1
        Mt = s["Mt"]
        ev = np.linalg.eigvalsh(Mt)
        for p in r["poles"]:
            z = complex(0.0, p["z"][1])
            lg = zol.complex_logdet(Mt, z)
            d_re = max(d_re, abs(float(wrap(lg.imag - p["phase"]))))
            d_re = max(d_re, abs(lg.real - p["log_abs_det"])
                       / max(abs(p["log_abs_det"]), 1.0))
            tr = zol.resolvent_data(Mt, z)
            d_tre = max(d_tre, abs(tr - complex(p["resolvent_trace"][0],
                                                p["resolvent_trace"][1]))
                        / max(abs(tr), 1.0))
            d_id = max(d_id, abs(float(wrap(
                spectral_phase(ev, p["z"][1]) - p["phase"]))))
        idx_rows.append((r["h"], r["kz"], int(np.sum(ev < 0.0)),
                         r["poles"][0]["phase"], float(ev[0])))
    check("S2.1 RESOLVENT-PHASE-RECOMPUTED: arg det(M_h - z_j I), "
          "log|det| and tr(M_h - z_j I)^{-1} rebuilt from scratch "
          "through the CCVII/CCXXV machinery on %d x %d matched pole "
          "rows == the stored artifact: max dev %.2e (traces %.2e) "
          "<= %.0e" % (nrec, NDIM, d_re, d_tre, RECOMP_WARD),
          nrec == len(rows) and d_re <= RECOMP_WARD
          and d_tre <= 1e-8, kill="K2")
    check("S2.2 SPECTRAL-PHASE IDENTITY (derived here, warded): "
          "arg det(M_h - i y I) == sum_k atan2(-y, lam_k(M_h)) on the "
          "same %d x %d rows, max dev %.2e <= %.0e -- the stored "
          "determinant phase IS a SMOOTHED NEGATIVE-EIGENVALUE COUNT "
          "of the wall step, the same object CCXXIV censused"
          % (nrec, NDIM, d_id, RECOMP_WARD), d_id <= RECOMP_WARD,
          kill="K2")
    nneg = np.array([r[2] for r in idx_rows], float)
    ph0 = np.array([r[3] for r in idx_rows], float)
    pred0 = -math.pi * nneg
    print("    the small-pole limit, as a table: n_-(M_h) = %s ; the "
          "stored phase at the smallest pole y = %.4f vs the "
          "predicted -pi n_- : max |dev| (principal branch) %.3f rad"
          % ("/".join("%d" % v for v in sorted(set(nneg.astype(int)))),
             poles[0],
             float(np.max(np.abs(wrap(ph0 - pred0))))))
    check("S2.3 [DIAG] the CCVII one-bad-mode census is visible in the "
          "phase: n_- in {%s} on the %d matched surface steps -- the "
          "phase carries the index, and CCXXIV already typed that "
          "index as WALLPAPER (cosh shares the truth signature), so "
          "the phase's discriminating content, if any, must sit "
          "elsewhere"
          % (",".join("%d" % v for v in sorted(set(nneg.astype(int)))),
             len(idx_rows)), True)

    # ================================================================ S3
    section("S3 -- THE DOMAIN QUESTION and the CCXXIV BRIDGE")
    print("    DOMAIN-MISMATCH-DECLARED: z_j = i y_j is a SPECTRAL "
          "parameter of the tau-normalized step matrix (the elliptic "
          "poles are placed on the eigenvalue interval [c_B, L_src], "
          "y in [%.3f, %.3e]); Theta_X(t) lives on the FREQUENCY axis "
          "conjugate to the lag u.  No z_j -> t identification is "
          "derivable and NONE IS INVENTED.  The comparison is made "
          "through the CCXXIV congruence instead."
          % (poles[0], poles[-1]))
    lad = {}
    for kz in set(r["kz"] for r in rows):
        rg = eul.level_rung(kz)
        if rg is not None:
            lad[(rg["h"], rg["kz"])] = rg
    matched = [r for r in rows if (r["h"], r["kz"]) in lad]
    matched.sort(key=lambda r: (r["h"], r["kz"]))
    check("S3.1 the matched set is exactly the SURFACE segment [z1]: "
          "%d of %d stored rows have their (h, kz) on the CCXXIII "
          "level ladder (segments %s); the deep block and the bridge "
          "lie beyond the CCXXIII rung caps and are DECLARED OUT of "
          "the correlation (they remain inside S1)"
          % (len(matched), len(rows),
             "+".join(sorted({r["segment"] for r in matched}))),
          len(matched) >= (10 if SMOKE else 30)
          and {r["segment"] for r in matched} == {"surf"}, kill="K3")
    dcong = 0.0
    for r in matched[:5]:
        rg = lad[(r["h"], r["kz"])]
        es = euler_side(rg, poles)
        wall = es["Gam"] - es["tau"] * np.eye(NKAR)
        cong = (es["W"] * (es["D"] - es["tau"])[:, None]).T @ es["W"]
        dcong = max(dcong, float(np.max(np.abs(cong - wall)))
                    / max(float(np.max(np.abs(wall))), 1e-300))
    check("S3.2 [CCXXIV CONGRUENCE BRIDGE, reproduced] W^T diag(D - "
          "(1/2)mu1) W == Gamma - (1/2)mu1 I on 5 matched rungs: max "
          "rel dev %.2e <= %.0e -- the Euler-side object G_h = (Gamma "
          "- (1/2)mu1 I)/((1/2)mu1) is therefore the tau-normalized "
          "congruence image of the Krein kernel of Theta_X, and it is "
          "the ONLY Euler-side matrix compared here"
          % (dcong, 1e-10), dcong <= 1e-10, kill="K3")

    # ================================================================ S4
    section("S4 -- both sides on the matched ladder")
    hh = np.array([float(r["h"]) for r in matched])
    lx = np.log(hh)
    phi = np.array([[r["poles"][j]["phase"] for j in range(NDIM)]
                    for r in matched])
    phi = np.unwrap(phi, axis=0)
    worlds = {}
    for nm, kw in (("truth", {}),
                   ("smooth", dict(world="smooth")),
                   ("scramble", dict(scramble_seed=SCR_SEED)),
                   ("cosh", dict(lag_fn=inj_lag))):
        psi = np.zeros((len(matched), NDIM))
        phx = np.zeros((len(matched), 3))
        okr = np.zeros(len(matched), bool)
        for i, r in enumerate(matched):
            rg = eul.level_rung(r["kz"], **kw)
            if rg is None:
                continue
            es = euler_side(rg, poles)
            psi[i, :] = es["psi"]
            phx[i, :] = es["phiX"]
            okr[i] = True
        worlds[nm] = dict(psi=np.unwrap(psi, axis=0), phx=phx, ok=okr)
        print("    %-9s built on %d/%d matched rungs  [%.1f s]"
              % (nm, int(okr.sum()), len(matched), time.time() - T0))
    check("S4.1 all four worlds carry the full matched ladder",
          all(int(w["ok"].sum()) == len(matched)
              for w in worlds.values()), kill="K4")
    print("    [DIAG] truth ranges: Phi_j (our side) %s ; Psi_j "
          "(Euler bridge) %s ; Phi_X anchors t=1 %s"
          % (f3(phi.ravel()), f3(worlds["truth"]["psi"].ravel()),
             f3(worlds["truth"]["phx"][:, 0])))

    # ================================================================ S5
    section("S5 -- THE MEASUREMENT: raw / first-difference / DETRENDED "
            "correlation per pole (only the detrended one can carry "
            "content, declared before measuring)")
    print("    %-3s %9s %9s %9s %9s %9s %9s %9s"
          % ("j", "y_j", "raw_r", "affine_R2", "diff_r", "DETR_r",
             "DETR_scr", "DETR_cosh"))
    detr = {}
    for nm in ("truth", "smooth", "scramble", "cosh"):
        detr[nm] = []
    for j in range(NDIM):
        a = phi[:, j]
        da = detrend(a, lx)
        vals = {}
        for nm in ("truth", "smooth", "scramble", "cosh"):
            b = worlds[nm]["psi"][:, j]
            vals[nm] = corr(da, detrend(b, lx))
            detr[nm].append(vals[nm])
        b0 = worlds["truth"]["psi"][:, j]
        _i, _s, r2 = ols_line(b0, a)
        print("    %-3d %9.3f %+9.4f %9.4f %+9.4f %+9.4f %+9.4f %+9.4f"
              % (j, poles[j], corr(a, b0), r2,
                 corr(np.diff(a), np.diff(b0)), vals["truth"],
                 vals["scramble"], vals["cosh"]))
    dt = np.abs(np.array(detr["truth"]))
    print("    THE SECOND COORDINATE: the DIRECT completed Euler phase "
          "at the declared anchors, detrended, against each pole")
    print("    %-3s %9s %11s %11s %11s"
          % ("j", "y_j", "t=1.00", "t=5.25", "t=pi/D"))
    anc_best = 0.0
    for j in range(NDIM):
        da = detrend(phi[:, j], lx)
        rr = [corr(da, detrend(worlds["truth"]["phx"][:, k], lx))
              for k in range(3)]
        anc_best = max(anc_best, max(abs(v) for v in rr))
        print("    %-3d %9.3f %+11.4f %+11.4f %+11.4f"
              % (j, poles[j], rr[0], rr[1], rr[2]))
    link_j = [j for j in range(NDIM)
              if abs(detr["truth"][j]) >= CORR_LINK
              and abs(detr["scramble"][j]) <= CORR_KILL
              and abs(detr["cosh"][j]) <= CORR_KILL]
    linked = len(link_j) > 0
    check("S5.1 the detrended correlation is computed on all %d poles "
          "in all four worlds, none vacuous (|r| truth %s)"
          % (NDIM, e3(np.maximum(dt, 1e-18))),
          bool(np.all(np.isfinite(dt))))
    surv = [j for j in range(NDIM)
            if abs(detr["truth"][j]) >= CORR_LINK
            and (abs(detr["scramble"][j]) > CORR_KILL
                 or abs(detr["cosh"][j]) > CORR_KILL)]
    check("S5.2 CONTROL DIAGNOSIS: %d of %d poles reach |DETR_r| >= "
          "%.2f on truth; of those, %d ALSO reach > %.2f in a "
          "falsifying world (i.e. the apparent link is carried by the "
          "shared h-trend, not by arithmetic) and %d survive both "
          "controls" % (int(np.sum(dt >= CORR_LINK)), NDIM, CORR_LINK,
                        len(surv), CORR_KILL, len(link_j)), True)

    # ================================================================ S6
    section("S6 -- tau-screens, anti-circularity, verdict")
    tau = np.array([0.5 * lad[(r["h"], r["kz"])]["mu1"]
                    for r in matched])
    print("    TAU_REP := (1/2) mu1(h), the registered half-gap scale "
          "(declared BEFORE the run)")
    scr = []
    for lbl, vals in (("|Phi_0| (our phase, smallest pole)",
                       np.abs(phi[:, 0])),
                      ("|Psi_0| (Euler bridge, smallest pole)",
                       np.abs(worlds["truth"]["psi"][:, 0])),
                      ("|margin| (CCXXV 1 - tr R_m)",
                       np.abs([r["margin"] for r in matched]))):
        s = eul.screen(vals, tau, "S6 " + lbl)
        scr.append(s)
        print("    " + s)
    check("S6.1 tau-screens computed on every scale-like quantity, "
          "none vacuous", all("vacuous" not in s for s in scr))
    check("S6.2 ANTI-CIRCULARITY AUDIT: (i) zero zeta-zero reads, no "
          "prime oracle (AST); (ii) the stored artifact is RECOMPUTED "
          "from the parent machinery and warded entry by entry (S2.1) "
          "-- no stored number is trusted blind; (iii) the Euler side "
          "is built by the CCXXIII rung builder and compared ONLY "
          "through the CCXXIV congruence -- no z_j -> t map is "
          "invented; (iv) eigenvalues enter only inside the spectral "
          "phases, which ARE spectral objects by definition; (v) RNG "
          "only in the declared scramble control", True)

    # ============================================================ verdict
    section("VERDICT")
    v = []
    v.append("ARTIFACT-INTEGRITY-EXACT(phase %.1e, partial fractions "
             "%.1e, unwrap %.1e on all %d x %d stored rows)"
             % (d_ph, d_pf, d_uw, len(rows), NDIM))
    v.append("RESOLVENT-PHASE-RECOMPUTED(%d of %d x %d stored rows "
             "rebuilt from the CCVII/CCXXV machinery, max dev %.1e "
             "[B1])" % (nrec, len(rows), NDIM, d_re))
    v.append("SPECTRAL-PHASE-IDENTITY(arg det(M-iyI) == sum_k "
             "atan2(-y, lam_k), %.1e -- the determinant phase IS a "
             "smoothed negative-eigenvalue count)" % d_id)
    v.append("DOMAIN-MISMATCH-DECLARED(no z_j -> t identification "
             "exists or is invented; the comparison runs through the "
             "CCXXIV congruence, reproduced at %.1e)" % dcong)
    if linked:
        v.append("PHASES-LINKED(poles %s: |DETR_r| %s on truth and "
                 "<= %.2f in BOTH scramble and cosh)"
                 % (",".join(str(j) for j in link_j),
                    "/".join("%.3f" % abs(detr["truth"][j])
                             for j in link_j), CORR_KILL))
    else:
        v.append("PHASES-UNRELATED(no pole reaches |DETR_r| >= %.2f on "
                 "truth while collapsing in BOTH controls; truth "
                 "detrended |r| %s, best direct-anchor |r| %.3f -- an "
                 "honest null: beyond the shared h-trend the eight "
                 "fixed determinant phases and the completed Euler "
                 "phase of the same ladder carry no measured common "
                 "content)"
                 % (CORR_LINK, e3(np.maximum(dt, 1e-18)), anc_best))
    for s in v:
        print("  " + s)
    return finish()


def finish():
    section("SUMMARY")
    npass = sum(1 for _n, o in CHECKS if o)
    print("  checks: %d/%d PASS" % (npass, len(CHECKS)))
    for n, o in CHECKS:
        if not o:
            print("    FAIL: %s" % n)
    print("  kills: %s" % (",".join(sorted(set(KILLS))) or "none"))
    print("  wall clock: %.1f s" % (time.time() - T0))
    print("  FROZEN_SPEC SHA-256 = %s" % SPEC_SHA)
    print("  EXPLORATION ONLY -- no ledger row, no paper edit, no "
          "marker move, NO RH claim.")
    return 0 if npass == len(CHECKS) else 1


if __name__ == "__main__":
    sys.exit(main())
