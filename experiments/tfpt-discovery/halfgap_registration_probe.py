#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""halfgap_registration_probe -- PRIME.PORT.HALFGAP.01
(EXPLORATION ONLY, experiments/; round 63, theorem-engineering on
the RH-side wall: the REGISTRATION -- not the celebration -- of
the frozen target inequality
    n_h - q_h >= (1/2) mu1(h)   for all h,
mu1(h) = 4 sin^2(pi/(2h+1)) the deployed KMS/Dirichlet parity gap.
On the deployed surface the pair (n_h, q_h) collapses along the
critical direction (K v = m v => q = 0, n = m; CXLIII ward), so
the inequality reads  shat_h = m_h/mu1(h) >= 1/2.  2026-08-11.)

THE FROZEN NO-ADJUSTMENT CLAUSE (recorded verbatim, first): the
constant is FROZEN at EXACTLY 1/2, now, before any future data.
A later miss on any rung -- holdout or otherwise -- is a FAIL of
the registered inequality, full stop; it must NOT be repaired by
adjusting the constant to 0.49, 0.501, or any other value, by
reweighting, or by excluding rungs.  A failed registration is a
first-class result and gets reported as such.  This clause is
part of the registered object.

TAU-SCREEN FORMALITY, DECLARED OPENLY (spec item (f)): the
inequality is the WALL MARGIN REPARAMETRIZED -- m_h divided by a
source-only geometric gap, with a frozen constant.  Its value is
FALSIFIABILITY (a sharp, non-adjustable, per-rung pass/fail
target for deeper data), NOT novelty: nothing here is a new
floor, a new theorem, or evidence.  CXLIII measured inf shat =
0.502 on this surface; registering 1/2 converts that measurement
into a hostage.

FROZEN PROTOCOL:

 W   LADDER + REPRODUCTION (kill -> PIPELINE-BROKEN /
     WARD-BROKEN; machinery verbatim from
     moving_node_second_order_probe = CXLIII): faithful rungs
     (KZMAX 150); W1 >= MIN_RUNGS = 40; W2 WARD m_h > 0
     everywhere; W3 WARD mu1 closed form == core.parity_mu(h)[0]
     to MU_WARD relative on the SUBSET; W4 WARD pivot collapse
     |K v - m v|/scale <= RES_WARD on the SUBSET (=> n - q = m
     along v: the registered inequality is evaluated as shat >=
     1/2 on this surface); W5 REPRODUCTION margin exponent p in
     [-2.5, -1.5]; W6 REPRODUCTION CXLIII band: shat min/med/max
     == 0.502/1.027/2.185 (rtol 2e-2).

 R   THE REGISTRATION (typed, never kill):
     R1 the frozen clause printed verbatim (constant exactly
        1/2, no adjustment, no exclusion, miss = FAIL);
     R2 surface evaluation: count of rungs with shat_h >= 1/2;
        margin ladder margin_h = shat_h - 1/2 (min/med/max);
        typed SURFACE-PASS(n/N, min margin) iff all rungs pass,
        else SURFACE-FAIL(list) -- a fail here is a first-class
        result, reported, not repaired;
     R3 the THREE tightest rungs: (kz, h, alpha, m_h, mu1,
        shat_h, margin_h) at full precision;
     R4 the registered-surface hash: SHA-256 over the lines
        "kz:h:shat(%.12e)" of the ladder -- the frozen registry
        a future holdout test diffs against.

 H   BLIND-HOLDOUT PROTOCOL (declared, typed): any faithful rung
     (kz, h) NOT in the registered R4 surface -- rungs that
     become reachable through deeper windows or extensions of
     KZMAX / HCAP / ATOM_MAX -- is a BLIND HOLDOUT.  Evaluation
     rule, frozen now: compute shat_h = m_h/mu1(h) with THIS
     pipeline verbatim; the holdout rung PASSES iff shat_h >=
     1/2; each rung is scored individually; no refits, no
     constant adjustment, no exclusions; failures are reported
     per rung.  The holdout verdict never edits the
     registration.

 O   DEMAND-OF-ORIGIN (typed OPEN, never kill): the four
     candidate algebraic origins of the 1/2 are recorded as OPEN
     hypotheses; the registration REQUIRES an algebraic
     derivation of the constant from one of them (or a
     successor) before any claim upgrade anywhere:
     O1 MEASURED-FLOOR: inf shat = 0.502 (CXLIII INF-FLAT, c0 =
        0.502) -- is 1/2 the true infimum of which 0.502 is the
        surface trace?  OPEN: needs a lower-bound derivation,
        not a measurement.
     O2 PG-HALF: the canonical s = 1/2 in the certified
        dominance B >= 1/2 P_G + c_dom I (CXLIV V4, 39/39) --
        same 1/2 or coincidence?  OPEN.
     O3 SCHUR-WARD-SECOND-VARIATION: the 1/2 of the second-order
        coefficient in the Schur-Ward envelope expansion (CXL
        exact within-rung transition).  OPEN.
     O4 MATCHED-ASYMPTOTICS-REST: C_h = m_h h^2 in [4.95, 21.5]
        (round 59) gives shat ~ C_h/pi^2 in [0.502, 2.18]: is
        1/2 = C_min/pi^2 an integrated second-order rest with an
        algebraic C_min = pi^2/2?  OPEN.

 C   CONTROLS (spec item (e)): wards (kill -> WARD-BROKEN if
     silent): C1 smooth world lam_sm < 0 on EVERY rung (v883
     regression); C2 Epstein x^2+5y^2 comb + scramble (seed 1)
     at kz 9 fire (lam_min < 0).  DISCRIMINATION (typed, never
     kill -- a control SATISFYING the inequality means the
     target is not discriminating, and that is a first-class
     finding): the three control worlds (smooth per rung;
     Epstein and scramble at kz 9) must VIOLATE shat >= 1/2;
     typed CONTROLS-DISCRIMINATE(k/3) /
     CONTROLS-NON-DISCRIMINATING(names).

 F   SCREENS (documentation, NOT a floor): OLS slope of
     log(margin) vs log(m) on the positive-margin subset, and vs
     log h, both with R^2 -- the reparametrization statement
     printed next to the formality declaration.

KILLS: K1 (W1) -> PIPELINE-BROKEN; K2 (W2-W6, C1-C2) ->
WARD-BROKEN.  R/H/O/F and the discrimination census are typed
measurements, never kills.

VERDICT (frozen enum): HALFGAP-REGISTERED with typed sublabels
REG-FROZEN(c = 1/2 exact, NO-ADJUST), SURFACE-PASS(n/N, min
margin)/SURFACE-FAIL(k), TIGHTEST(three rungs),
HOLDOUT-DECLARED(registry sha8), ORIGIN-OPEN(4),
CONTROLS-DISCRIMINATE(k/3)/CONTROLS-NON-DISCRIMINATING(...),
REPARAM-DECLARED; else PIPELINE-BROKEN / WARD-BROKEN.

FROZEN BARS: REG_C = 1/2 EXACT (Fraction(1, 2); the
no-adjustment clause above); KZMAX = 150; MIN_RUNGS = 40; SUBSET
= (9, 13, 26, 40, 60, 90, 121) intersected with the faithful
ladder; MU_WARD = 1e-12; RES_WARD = 1e-9; EXPO_BAND = [-2.5,
-1.5]; SHAT_REF = (0.502, 1.027, 2.185) (rtol 2e-2); CTRL_KZ =
9; scramble seed 1; NG_SMOOTH = 6000.  Runtime cap declared: 8
min.

ANTI-CIRCULARITY (frozen): no sigma_h, no defect eigenvector, no
pivot sign as input, no factorization of the target matrix; mu1
is pure geometry; m_h and v_h are measured outcomes of the
deployed wall, used as measurements only; the constant 1/2 is
frozen BEFORE any holdout data and is not fit to anything.

SMOKE-RUN DISCLOSURE (2026-08-11, before freezing): one smoke
run of this script (17/17 with the identical bars; NO bar, band,
count, rule or enum was moved after it) measured: 67 faithful
rungs (h 142..1433), wards exact (mu1 tie 0.0, pivot collapse
4.3e-16, margin exponent -1.934), CXLIII band reproduced
exactly (shat min/med/max 0.502/1.027/2.185).  R2: SURFACE-PASS
67/67, margin min/med/max +0.0025/+0.5273/+1.6845.  R3 the three
tightest rungs: kz 98 h 997 alpha 6.014 shat 0.5024791578
(margin +2.479e-03); kz 22 h 199 alpha 3.892 shat 0.5257694654
(margin +2.577e-02); kz 71 h 989 alpha 5.572 shat 0.5278921411
(margin +2.789e-02) -- two of the three tightest rungs sit in
the deepest reachable regime (h ~ 1000), the registration bites
near where the ladder ends, but the second-tightest is a SHALLOW
rung (h 199): the tightness is arithmetic scatter, not a depth
trend (consistent with CXLIII INF-FLAT).  R4 registry sha256
ae292e55... over 67 lines.  Controls: smooth world violates the
wall on 67/67 (max shat_sm -2.3e+03 < 1/2), Epstein shat_ctrl
-3.5e+04, scramble -2.7e+04 -> DISCRIMINATE 3/3.  F screens: log
margin vs log m slope +0.099 (R^2 0.018), vs log h +0.098 (R^2
0.005) -- decorrelated flatness, the reparametrization
statement.  Runtime 16.6 s (cap holds).  Fail-first preserved:
nothing was weakened; the clause, bars and enums are exactly as
frozen above.

SPEC v1 (2026-08-11, frozen + SHA-hashed before the frozen run):
everything above.  Mechanical concretizations frozen with v1:
(i) ladder + robust-node-free rung build verbatim from CXLIII
(ONE eigh per rung); (ii) mu1 closed form 4 sin^2(pi/(2h+1)),
parity tie via core.parity_mu(h)[0] on the subset; (iii) OLS
population statistics + leave-one-out jackknife as CXLIII; (iv)
registry hash over "%d:%d:%.12e" % (kz, h, shat) lines joined
by newlines.

NO RH claim: the registration is a falsifiability device on the
measured surface; shat >= 1/2 on 67 rungs proves nothing about
deeper h, the ideal objects, or any tail statement; the constant
awaits an algebraic origin (O1-O4) before any upgrade.  No
marker moves.

FIREWALL: no zeros, no prime oracles (AST scan; banned ids
zetazero / nzeros / primerange / isprime / primepi / nextprime /
prevprime); v563 READ-ONLY; RNG only inside the declared
scramble control; stdout only.

Sources (read-only): v563_paper2_readouts (incl. parity_mu);
ladder machinery verbatim from moving_node_second_order_probe.py
(CXLIII); C_h band from wall_matched_asymptotics_probe (declared
input); s = 1/2 dominance from bfloor_pg_dominance_probe (CXLIV,
declared input).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/halfgap_registration_probe.py
"""

import ast
import hashlib
import math
import os
import sys
import time
from fractions import Fraction

import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
_VERIFY = os.path.abspath(os.path.join(_HERE, "..", "..",
                                       "verification"))
sys.path.insert(0, _HERE)
sys.path.insert(0, _VERIFY)

import v563_paper2_readouts as core        # noqa: E402  (READ-ONLY)

REG_C = Fraction(1, 2)
KZMAX = 150
MIN_RUNGS = 40
SUBSET = (9, 13, 26, 40, 60, 90, 121)
MU_WARD = 1e-12
RES_WARD = 1e-9
EXPO_BAND = (-2.5, -1.5)
SHAT_REF = (0.502, 1.027, 2.185)
SHAT_RTOL = 2e-2
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
    bb = []
    for i in range(n):
        m = np.ones(n, bool)
        m[i] = False
        _ai, bi, _ = ols_line(x[m], y[m])
        bb.append(bi)
    bb = np.array(bb)
    se_b = math.sqrt((n - 1) / n * float(np.sum((bb - bb.mean())
                                                ** 2)))
    return a, b, r2, se_b


def smooth_comb(alpha, ng=NG_SMOOTH):
    ug = (np.arange(ng) + 0.5) * (2.0 * alpha / ng)
    mg = 2.0 * np.exp(ug / 2.0) * (2.0 * alpha / ng)
    return ug, mg


def lambda_eps(N):
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


def mu1_of(h):
    return 4.0 * math.sin(math.pi / (2.0 * h + 1.0)) ** 2


def main():
    section("PRIME.PORT.HALFGAP.01 -- REGISTRATION of the frozen "
            "target n_h - q_h >= (1/2) mu1(h) (shat >= 1/2 on the "
            "deployed surface; EXPLORATION ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s"
          % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
    print("    NO RH claim; no marker moves.  REPARAM-DECLARED: "
          "the registered inequality is the wall margin "
          "reparametrized; its value is falsifiability, not "
          "novelty.")
    print("\nS0 -- firewall")
    check("S0.1 AST firewall clean", not ast_scan(BANNED_IDS))

    # ------------------------------------------------------------ W
    section("W -- the faithful ladder + wards (CXLIII verbatim)")
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
        Kt = core.odd_toeplitz(c_ar + c_at, M)
        w, V = np.linalg.eigh(Kt)
        v = V[:, 0]
        row = dict(kz=kz, alpha=float(alpha), h=h, m=float(w[0]),
                   mu1=mu1_of(h))
        if kz in SUBSET:
            res = float(np.linalg.norm(Kt @ v - w[0] * v)) \
                / max(float(np.max(np.abs(w))), 1.0)
            row["pivres"] = res
            row["mu1_tie"] = abs(row["mu1"]
                                 - float(core.parity_mu(h)[0])) \
                / row["mu1"]
        ug, mg = smooth_comb(alpha)
        c_sm = np.asarray(core.atom_lags_at(alpha, M, ug, mg)[0],
                          float)
        row["lam_sm"] = float(np.linalg.eigvalsh(
            core.odd_toeplitz(c_ar + c_sm, M))[0])
        rungs.append(row)
        del Kt, V
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
    sub = [r for r in rungs if "pivres" in r]
    tie = max(r["mu1_tie"] for r in sub)
    check("W3 WARD mu1 closed form == core.parity_mu(h)[0] on the "
          "subset: max rel dev %.2e <= %.0e" % (tie, MU_WARD),
          tie <= MU_WARD, kill="K2")
    pres = max(r["pivres"] for r in sub)
    check("W4 WARD pivot collapse |K v - m v|/scale %.2e <= %.0e "
          "on the subset => n - q = m along v: the registered "
          "inequality reads shat >= 1/2 on this surface"
          % (pres, RES_WARD), pres <= RES_WARD, kill="K2")
    hh = np.array([float(r["h"]) for r in rungs])
    _a, p_exp, _r2, _se = jack_fit(np.log(hh), np.log(ms))
    check("W5 REPRODUCTION margin exponent p = %+.3f in [%.1f, "
          "%.1f]" % (p_exp, EXPO_BAND[0], EXPO_BAND[1]),
          EXPO_BAND[0] <= p_exp <= EXPO_BAND[1], kill="K2")
    shat = ms / np.array([r["mu1"] for r in rungs])
    trio = (float(shat.min()), float(np.median(shat)),
            float(shat.max()))
    ok_band = all(abs(a / b - 1.0) <= SHAT_RTOL
                  for a, b in zip(trio, SHAT_REF))
    check("W6 REPRODUCTION CXLIII band: shat min/med/max "
          "%.3f/%.3f/%.3f == %.3f/%.3f/%.3f (rtol %.0e)"
          % (trio + SHAT_REF + (SHAT_RTOL,)), ok_band, kill="K2")
    if KILLS:
        return finish({})

    # ------------------------------------------------------------ R
    section("R -- the registration")
    print("    R1 THE FROZEN CLAUSE (verbatim, part of the "
          "registered object):")
    print("       the constant is EXACTLY %s, frozen now; a "
          "later miss on any rung is a FAIL of the registered"
          % REG_C)
    print("       inequality, full stop -- it must NOT be "
          "repaired by adjusting the constant (0.49, 0.501, "
          "...),")
    print("       by reweighting, or by excluding rungs; a "
          "failed registration is a first-class result.")
    check("R1 typed: REG-FROZEN(c = 1/2 exact, NO-ADJUST)", True)
    c_half = float(REG_C)
    margins = shat - c_half
    n_pass_r = int(np.sum(shat >= c_half))
    fails = [r for r, s in zip(rungs, shat) if s < c_half]
    print("    R2 margins shat - 1/2: min/med/max %+.4f/%+.4f/"
          "%+.4f on %d rungs" % (float(margins.min()),
                                 float(np.median(margins)),
                                 float(margins.max()),
                                 len(rungs)))
    if fails:
        for r in fails:
            print("    R2 FAIL kz %d h %d: shat %.6f < 1/2"
                  % (r["kz"], r["h"], r["m"] / r["mu1"]))
        r2lab = "SURFACE-FAIL(%d)" % len(fails)
    else:
        r2lab = ("SURFACE-PASS(%d/%d, min margin %+.2e)"
                 % (n_pass_r, len(rungs), float(margins.min())))
    check("R2 typed: %s" % r2lab, True)
    order = np.argsort(margins)
    tight = []
    print("    R3 the three tightest rungs (full precision):")
    for i in order[:3]:
        r = rungs[i]
        s = float(shat[i])
        tight.append("kz%d/h%d" % (r["kz"], r["h"]))
        print("       kz %4d  h %5d  alpha %.6f  m %.12e  mu1 "
              "%.12e  shat %.10f  margin %+.6e"
              % (r["kz"], r["h"], r["alpha"], r["m"], r["mu1"],
                 s, s - c_half))
    check("R3 typed: TIGHTEST(%s)" % ", ".join(tight), True)
    reg_lines = "\n".join("%d:%d:%.12e" % (r["kz"], r["h"], s)
                          for r, s in zip(rungs, shat))
    reg_sha = hashlib.sha256(reg_lines.encode("utf-8")).hexdigest()
    print("    R4 registered-surface sha256 = %s (%d lines)"
          % (reg_sha, len(rungs)))
    check("R4 typed: registry frozen (sha8 %s)" % reg_sha[:8],
          True)

    # ------------------------------------------------------------ H
    section("H -- the blind-holdout protocol (declared)")
    print("    any faithful rung (kz, h) NOT in the R4 registry "
          "-- reachable later through deeper windows or")
    print("    KZMAX/HCAP/ATOM_MAX extensions -- is a BLIND "
          "HOLDOUT: evaluate shat_h = m_h/mu1(h) with THIS")
    print("    pipeline verbatim; PASS iff shat_h >= 1/2, scored "
          "per rung; no refits, no constant adjustment,")
    print("    no exclusions; failures reported individually; "
          "the holdout verdict never edits the registration.")
    check("H1 typed: HOLDOUT-DECLARED(%s)" % reg_sha[:8], True)

    # ------------------------------------------------------------ O
    section("O -- demand-of-origin: the four OPEN candidates for "
            "the 1/2")
    print("    O1 MEASURED-FLOOR: inf shat = 0.502 (CXLIII "
          "INF-FLAT) -- needs a lower-bound derivation.  OPEN")
    print("    O2 PG-HALF: the canonical s = 1/2 in B >= 1/2 P_G "
          "+ c_dom I (CXLIV V4, 39/39).  OPEN")
    print("    O3 SCHUR-WARD-SECOND-VARIATION: the 1/2 of the "
          "second-order envelope coefficient (CXL).  OPEN")
    print("    O4 MATCHED-ASYMPTOTICS-REST: shat ~ C_h/pi^2, "
          "C_h in [4.95, 21.5] -- is C_min = pi^2/2?  OPEN")
    print("    the registration REQUIRES an algebraic derivation "
          "of the constant before any claim upgrade.")
    check("O typed: ORIGIN-OPEN(4)", True)

    # ------------------------------------------------------------ C
    section("C -- controls + discrimination")
    lam_sm = np.array([r["lam_sm"] for r in rungs])
    check("C1 WARD smooth world violates the wall: lam_sm < 0 on "
          "%d/%d rungs (min %.1e)"
          % (int(np.sum(lam_sm < 0)), len(rungs),
             float(lam_sm.min())),
          bool(np.all(lam_sm < 0)), kill="K2")
    rr9 = core.build_window(CTRL_KZ)
    alpha9, M9, D9, h9 = rr9["alpha"], rr9["M"], rr9["D"], rr9["h"]
    c_ar9 = np.asarray(core.arch_lags(M9, D9), float)
    N_E = int(math.floor(math.exp(2.0 * alpha9))) + 1
    lamE_ = lambda_eps(N_E)
    nn = np.nonzero(np.abs(lamE_) > 1e-12)[0]
    c_E = np.asarray(core.atom_lags_at(
        alpha9, M9, np.log(nn.astype(float)),
        2.0 * lamE_[nn] / np.sqrt(nn.astype(float)))[0], float)
    rr_s = core.build_window(CTRL_KZ, scramble_seed=1)
    c_s = np.asarray(core.atom_lags_at(
        rr_s["alpha"], rr_s["M"], np.asarray(rr_s["uu"], float),
        2.0 * np.asarray(rr_s["lam"], float))[0], float)
    fired = True
    ctrl_shat = {}
    for name, c_c in (("Epstein", c_E), ("scramble", c_s)):
        lam_c = float(np.linalg.eigvalsh(core.odd_toeplitz(
            c_ar9 + c_c, M9))[0])
        fired &= lam_c < 0
        ctrl_shat[name] = lam_c / mu1_of(h9)
        print("    %-9s: lam_min %+.3e  shat_ctrl %+.3e -> %s"
              % (name, lam_c, ctrl_shat[name],
                 "FIRES" if lam_c < 0 else "SILENT"))
    check("C2 WARD both controls fire (lam_min < 0)", fired,
          kill="K2")
    shat_sm = lam_sm / np.array([r["mu1"] for r in rungs])
    disc = []
    if bool(np.all(shat_sm < c_half)):
        disc.append("smooth")
    for name in ("Epstein", "scramble"):
        if ctrl_shat[name] < c_half:
            disc.append(name)
    if len(disc) == 3:
        clab = "CONTROLS-DISCRIMINATE(3/3)"
    else:
        bad = [n for n in ("smooth", "Epstein", "scramble")
               if n not in disc]
        clab = ("CONTROLS-NON-DISCRIMINATING(%s) -- FIRST-CLASS "
                "FINDING: the target does not separate the "
                "worlds" % ",".join(bad))
    print("    discrimination census: smooth max shat_sm %+.1e; "
          "Epstein %+.1e; scramble %+.1e (all must be < 1/2)"
          % (float(shat_sm.max()), ctrl_shat["Epstein"],
             ctrl_shat["scramble"]))
    check("C3 typed: %s" % clab, True)

    # ------------------------------------------------------------ F
    section("F -- the tau-screen formality + screens")
    pos = margins > 0
    if int(np.sum(pos)) >= 3:
        _a1, sl_m, r2_m = ols_line(np.log(ms[pos]),
                                   np.log(margins[pos]))
        _a2, sl_h, r2_h = ols_line(np.log(hh[pos]),
                                   np.log(margins[pos]))
    else:
        sl_m = sl_h = r2_m = r2_h = float("nan")
    print("    log(margin) vs log m slope %+.3f (R^2 %.3f); vs "
          "log h slope %+.3f (R^2 %.3f)" % (sl_m, r2_m, sl_h,
                                            r2_h))
    print("    DECLARED: shat >= 1/2 is a reparametrized wall "
          "statement; the registration's value is")
    print("    FALSIFIABILITY (a frozen, non-adjustable, per-rung "
          "target for deeper data), not novelty.")
    check("F1 typed: REPARAM-DECLARED(vs-m %+.3f, vs-h %+.3f)"
          % (sl_m, sl_h), True)

    return finish(dict(r2=r2lab,
                       tight="TIGHTEST(%s)" % ", ".join(tight),
                       hold="HOLDOUT-DECLARED(%s)" % reg_sha[:8],
                       ctrl=clab))


def finish(labels):
    section("V -- FROZEN VERDICT")
    n_pass = sum(1 for _n, okk in CHECKS if okk)
    n_tot = len(CHECKS)
    if KILLS:
        VERDICT = {"K1": "PIPELINE-BROKEN",
                   "K2": "WARD-BROKEN"}[KILLS[0]]
        print("\n  VERDICT: %s" % VERDICT)
    else:
        VERDICT = ("HALFGAP-REGISTERED / REG-FROZEN(1/2, "
                   "NO-ADJUST) / %s / %s / %s / ORIGIN-OPEN(4) / "
                   "%s / REPARAM-DECLARED"
                   % (labels.get("r2", "-"),
                      labels.get("tight", "-"),
                      labels.get("hold", "-"),
                      labels.get("ctrl", "-")))
        print("\n  VERDICT: %s" % VERDICT)
    print("""
  HONEST FRAME (as frozen): this is a REGISTRATION, not a result:
  the inequality n - q >= (1/2) mu1 is the wall margin
  reparametrized, its constant frozen at exactly 1/2 with an
  explicit no-adjustment clause, its future evaluation protocol
  declared blind; the algebraic origin of the 1/2 (O1-O4) is OPEN
  and required before any upgrade.  NO RH claim.  No marker
  moves.""")
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed"
          % (time.time() - T0, n_tot, n_tot - n_pass))
    return 0 if n_pass == n_tot else 1


if __name__ == "__main__":
    raise SystemExit(main())
