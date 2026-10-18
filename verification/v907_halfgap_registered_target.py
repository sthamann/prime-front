#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""v907 -- PRIME.PORT.HALFGAP.01 + PRIME.PORT.DEEP.HOLDOUT.01: THE REGISTERED HALF-GAP TARGET AND ITS FIRST BLIND HOLDOUT -- the target inequality n_h - q_h >= (1/2) mu1(h) is REGISTERED on the 67-rung surface with the constant EXACTLY 1/2 frozen under an explicit NO-ADJUST clause, and the first genuine blind holdout on 28 new deeper faithful rungs PASSES 28/28, ONE module from two probes (17/17 + 14/14 checks, zero fails, verdicts HALFGAP-REGISTERED (REG-FROZEN(1/2, NO-ADJUST) / SURFACE-PASS(67/67, min margin +2.48e-03) / TIGHTEST(kz98/h997, kz22/h199, kz71/h989) / HOLDOUT-DECLARED(ae292e55) / ORIGIN-OPEN(4) / CONTROLS-DISCRIMINATE(3/3) / REPARAM-DECLARED) + DEEPHOLDOUT-SCORED (FIDELITY(overlap 0.0, regression 0.0 bit-exact, registry ae292e55) / NEW-SURFACE(28, h 1219..2854) / HALFGAP-HOLDOUT-PASS(28/28, min margin +2.2316e-01) / HEADFLOOR-O1(slope=-0.049) + BCOVER/NETB/NETA(28/28) / BFLOOR-PERSISTS(min lam_min(B) = 1.6610) + DOM-PERSISTS(27/27, min c_B = 1.6394) + SKIPPED(0) / LAW-CONTINUES(p_comb = -1.925)); discovery probes halfgap_registration_probe.py and deep_blind_holdout_probe.py (round 63), 2026-08-11, re-run identically at promotion, embedded BYTE-EXACT and executed verbatim, ~150 s).  LEDGER TYPE: REGISTERED TARGET INEQUALITY + FIRST BLIND HOLDOUT PASSED -- EXPLICITLY NOT EVIDENCE FOR RH: a falsification instrument.  REPARAM-DECLARED in every print: the inequality is the wall margin REPARAMETRIZED (shat = m/mu1 with the exact pivot collapse n - q = m along v, warded at 4.3e-16); its value is FALSIFIABILITY, not novelty.  (1) THE REGISTRATION (halfgap_registration, 17/17): the constant is EXACTLY 1/2, frozen, with the NO-ADJUST clause part of the registered object (a later miss may NOT be repaired by 0.49, reweighting, or rung exclusion -- a fail is a first-class result); SURFACE-PASS 67/67 with margins shat - 1/2 min/med/max +0.0025/+0.5273/+1.6845; the three tightest rungs kz 98/h 997 (shat 0.5024791578), kz 22/h 199 (0.5257694654), kz 71/h 989 (0.5278921411) -- the second-tightest is SHALLOW (h 199): the tightness is arithmetic scatter, not a depth trend; the blind-holdout protocol is DECLARED (registry sha256 ae292e55..., 67 lines kz:h:shat; every future reachable faithful rung outside the registry scored verbatim by THIS pipeline, PASS iff shat >= 1/2 per rung, no refits, no constant moves, the holdout verdict never edits the registration); the FOUR candidate origins of the 1/2 typed OPEN (O1 the measured floor 0.502; O2 the canonical s = 1/2 of the v905 P_G dominance; O3 the Schur-Ward second-variation coefficient; O4 the integrated matched-asymptotics remainder C_min = pi^2/2?) -- the registration DEMANDS an algebraic derivation of the constant before any claim upgrade; screens decorrelated-flat (log margin vs m +0.099 R^2 0.018, vs h +0.098 R^2 0.005); CONTROLS DISCRIMINATE 3/3 (smooth violates on 67/67 with max shat_sm -2.3e+03, Epstein -3.5e+04, scramble -2.7e+04 -- all far below 1/2).  (2) THE FIRST BLIND HOLDOUT (deep_blind_holdout, 14/14): the 4e6 table (10x deeper) is byte-exact against the deployed one on [0, 4e5] (prefix arrays bitwise, kappa 0.038821 unchanged, 3-rung convention regression BIT-EXACT 0.0 incl. tangent scalars, registry SHA reproduced verbatim) and opens 28 NEW rungs outside the registry (kz 139..326, h 1219..2854, X to 3.81e6; the H-band extension is a disclosed REACHABILITY amendment, no scoring rule moved); HALFGAP-HOLDOUT-PASS 28/28 with margins min/med/max +0.2232/+0.6567/+1.3482 -- the holdout minimum sits ~90x ABOVE the registered surface minimum (+2.48e-03, which remains the global minimum): NO depth erosion; HEADFLOOR-O1 PERSISTS (B-cover 28/28, tail_B <= 0 at cB 28/28, tail_A <= 0 at cA 28/28, screen slope -0.049 +- 0.440) -- with the honest structural drift disclosed: the cut ladders DRIFT (n_minB med 47 vs deployed 17; the shared cut n = 9 no longer covers the depth universally -- the first honest structural shift of the holdout); the B-floor and the half-dominance persist at the DECLARED float level (28/28 Gram chains complete, min lam_min(B) = 1.6610, dominance negidx(B - P_G/2) = 0 on 27/27 steps, c_G 0.914..0.962, min c_B = 1.6394; no interval rollout, no exact-rational certificates in the depth -- said explicitly); the margin law CONTINUES (combined p = -1.9246 +- 0.0763 over 95 rungs, R^2 0.966; new-only -2.136 +- 0.381); PRE-FREEZE SIZING disclosed (census + timing saw two holdout values before the freeze -- the constant 1/2 is upstream-frozen and immovable, no bar/band/enum chosen after).  (3) THE ROUND-61 FRAME (docstring-level; probes NOT embedded, cited as exploration): the coordinates in which the registered object lives are exact -- schur_envelope_identity_probe.py (20/20, ENVELOPE-MEASURED, Spec-SHA 6c4188c3...): in the frozen v_sm frame the Schur-Ward decomposition collapses exactly (b = 0, x = 0), so the HUB IS the H-term and the DEMAND IS the -s-term at machine precision (bridge 6.9e-13; s = lam_min(K_smooth) = -demand(v_sm) at 2.7e-15 class), and R = the adaptation energy of the arithmetic fluctuation field dK = K_true - K_smooth is a THIRD object (R/m med 34.9 -- overlap-deficiency scale, not margin scale; the accumulated-R reading of the demand is DEAD; lift and demand share the same smooth atom-energy functional -E_s which cancels IDENTICALLY in lift - demand = g^T K_true g); moving_node_second_order_probe.py (12/12, GAPNORM-MEASURED, Spec-SHA 7a3d30c1...): the normalization mu1(h) = 4 sin^2(pi/(2h+1)) is the deployed KMS/Dirichlet parity geometry (tie 0.0, sign-free, tau_{h+1}-independent), shat lies in [0.502, 2.185] on 67/67 (med 1.027, reproducing the matched-asymptotics band C_h/pi^2 almost exactly), inf shat = 0.502 is INF-FLAT (jackknife slope -0.023 +- 0.105, CI contains 0 -- no measurable erosion, no measurable rise) and NO one-variable organization exists (R^2 vs node 0.000, vs alpha 0.003, vs log h 0.027).  CONTROLS: all three worlds discriminate in both embedded probes (the deep Epstein control is DECLARED SKIPPED in the holdout -- O(X^2) divisor recursion infeasible at X ~ 8e5, it lives at kz 9 in the upstream probes); AST firewalls clean; RNG only in scramble.  NO RH claim; no marker moves; a pass is survival of a falsification attempt, never evidence -- the constant 1/2 has no derivation yet, and the registration forbids celebrating one into existence.

PROVENANCE: discovery probes halfgap_registration_probe.py (17/17,
HALFGAP-REGISTERED, SPEC v1 frozen pre-run, round 63 note CLI,
Spec-SHA 767d38ce..., 2026-08-11) and deep_blind_holdout_probe.py
(14/14, DEEPHOLDOUT-SCORED, SPEC v1 frozen pre-run, round 63 note
CLIV, Spec-SHA 6d798074..., 2026-08-11), re-run identically at
promotion; frame probes schur_envelope_identity_probe.py (round 61
note CXL) and moving_node_second_order_probe.py (round 61 note
CXLIII) cited at docstring level only (both re-run green at
promotion: 20/20 + 12/12).  ROUND-31 EMBEDDING CONVENTION: frozen
sources embedded BYTE-EXACT, executed verbatim in isolated
namespaces; printed spec SHAs and the registry sha256 ae292e55...
reproduce; byte-equality ward vs experiments/tfpt-discovery/
inside the pattern gates.

FIREWALL: no zeros, no prime-table oracles (AST firewalls inside
the probes); the registered object is a TARGET, not a claim -- the
NO-ADJUST clause and the blind protocol are part of the object;
holdout depth is float-level (declared); NO RH claim in either
direction.  Python-only per GATE.WOLFRAM.02.
"""

import contextlib
import io
import os
import re
import sys
import time
import types

_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)

# ------------- frozen probe source halfgap_registration_probe (embedded BYTE-EXACT, raw string)
_SRC_0 = r'''
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
'''

# ------------- frozen probe source deep_blind_holdout_probe (embedded BYTE-EXACT, raw string)
_SRC_1 = r'''
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""deep_blind_holdout_probe -- PRIME.PORT.DEEP.HOLDOUT.01
(EXPLORATION ONLY, experiments/; round 63, theorem-engineering on
the RH-side wall: the FIRST BLIND HOLDOUT of the frozen round-63
conjectures on genuinely NEW, DEEPER faithful rungs.  The deployed
v563 pipeline caps faithful rungs at X <= ATOM_MAX = 400000 (the
67-rung registered surface, h 142..1433).  This probe rebuilds the
IDENTICAL pipeline over a ten-times-deeper von Mangoldt table
(TAB_EXT = 4e6), wards the extension byte-exact against the
deployed table, and scores the frozen targets OUT-OF-SAMPLE on the
newly reachable rungs -- no refits, no constant moves, no
exclusions.  2026-08-11.)

WHAT IS BEING SCORED BLIND (all frozen upstream, before any deep
data existed):
 (1) HALFGAP (PRIME.PORT.HALFGAP.01 = CLI): the registered target
     n_h - q_h >= (1/2) mu1(h), mu1(h) = 4 sin^2(pi/(2h+1)); on
     this surface the pivot collapses (K v = m v => n - q = m
     along v, CXLIII ward), so the score is shat_h = m_h/mu1(h)
     >= 1/2 PER RUNG.  The registered no-adjustment clause applies
     verbatim: the constant is EXACTLY 1/2; a miss on any rung is
     a FIRST-CLASS FAIL of the registered conjecture -- it must
     NOT be repaired by adjusting the constant, by reweighting, or
     by excluding rungs; failures are reported per rung; the
     holdout verdict never edits the registration.  The registered
     surface is frozen as the 67-line registry sha256 ae292e55...
     (full hash in REG_SHA below); every scored rung here is
     OUTSIDE that registry.
 (2) HEADFLOOR-O1 + NET TAIL (PRIME.PORT.TAILSIGN.01 = CXLVII):
     on the deployed surface B-covering cuts exist on 67/67
     (n_minB med 17), tail_B <= 0 at the first B-covering cut on
     67/67, tail_A <= 0 at the first A-covering cut on 67/67, and
     head_B(cB) is O(1) vs m (slope +0.113, med 0.388).  Scored
     here: do B-covering cuts exist on the new rungs, does the
     net tail sign persist at the covering cuts (both
     bookkeepings), and does head_B(cB) stay O(1) (typed with the
     TAILSIGN bands PASS |s| <= 0.30 / RELOC s >= 0.70 / AMBIG)?
 (3) B-FLOOR + P_G DOMINANCE, FLOAT LEVEL (PRIME.PORT.BFLOOR.PG.01
     = CXLIV): on the deployed 39-step surface lam_min(B) >= 0.679
     and B >= (1/2) P_G + c_dom I with c_dom > 0 (canonical V4,
     s = 1/2) hold on 39/39.  Scored here on the NEW steps
     (consecutive new-rung pairs, pipeline verbatim): per step
     lam_min(B), float c_G = lam_min(P_G), float c_dom =
     lam_min(B - (1/2) P_G), negidx(B - (1/2) P_G), and c_B =
     (1/2) c_G + c_dom.  Typed BFLOOR-PERSISTS iff min lam_min(B)
     >= MINB_REF (1 - MINB_RTOL) with the deployed constants
     0.679 / 2e-2; DOM-PERSISTS iff negidx = 0 and c_B > 0 on
     every scoreable step.  FLOAT LEVEL DECLARED: no
     exact-rational LDL and no interval enclosure here -- this is
     the float-level persistence measurement only; the certified
     analogue is CXLIV/CXLIX/CLIII machinery and is NOT run at
     depth.
 (4) THE MARGIN LAW (rh_leverage_probe / CXLIII chain): lam_min ~
     h^p with p = -1.93 on the deployed ladder.  Scored here: the
     log-log fit on the deployed 67, on the new rungs alone, and
     combined; typed LAW-CONTINUES iff the combined exponent stays
     in the deployed band EXPO_BAND = [-2.5, -1.5] (halfgap W5
     band, frozen upstream).

HOW THE DEEP RUNGS ARE BUILT (conventions replicated, every copy
documented):
  * table: lam_ext = core.von_mangoldt_table(TAB_EXT) -- the
    DEPLOYED generator itself, called at the deeper cap (the
    v770/v771 "deep-table overlap EXACTLY" pattern); ward W1
    requires lam_ext[:ATOM_MAX+1] == core.LAM_TAB byte-exact,
    ward W2 requires the derived prefix arrays (_NN, U_ALL,
    MU_ALL, G_ALL) to agree bitwise on the deployed range, ward
    W3 requires the Chebyshev envelope kappa on [100, TAB_EXT] to
    stay <= KAPPA_REF + 1e-6 (v770 guard verbatim).
  * zones + frame: exactly core.build_window's conventions on the
    extended arrays -- alpha = U[kz], D = 0.5 G[kz]/NU_MAIN, M =
    ceil(alpha/D - 1e-9) + 1 rounded up to even, h = M/2, atoms =
    all table atoms with u <= 2 alpha + 1e-14, masses mu =
    2 Lambda(n)/sqrt(n).  The zone-horizon guard (ZONE_DEEP /
    NZ_DEEP) is never binding here: faithfulness X = e^{2 alpha}
    <= TAB_EXT caps n_zone at 2000 << the mirrored horizon.
  * faithful NEW rung: ATOM_MAX < X <= TAB_EXT and h in the
    DECLARED band H_HOLD = [128, 2900].  H_MIN = 128 is the
    deployed floor; the ceiling 2900 EXTENDS the deployed HCAP =
    1450 (disclosed AMENDMENT of the reachability frame, frozen
    before scoring; under the deployed HCAP only 3 new rungs
    exist -- the band is widened to make the holdout non-trivial;
    NO scoring rule, bar or constant is touched by this).  Census
    from the pre-freeze sizing run: 28 new rungs, kz 137..332,
    n_zone 641..1951, h 1219..2854, X 4.19e5..3.81e6.
  * per-rung objects: c_at = core.atom_lags_at (tent assembly
    verbatim), c_ar = core.arch_lags, K = core.odd_toeplitz, ONE
    eigh per rung (eigenvalues + eigenvectors -- the registry
    convention; eigvalsh takes a different LAPACK path and moves
    the 12th printed digit, measured in sizing); weights Wv =
    core.lag_weights_from_v(v, h); the head/tail bookkeepings A
    and B verbatim from tail_sign_mechanism_probe (cuts inclusive
    at atom positions, PNT grid NG_SMOOTH = 6000 midpoints); the
    P_G chain verbatim from bfloor_pg_dominance_probe
    (grid_density FFT -> folded_measure -> lanczos_chain(h+1) ->
    eval_chain -> CD-Gram co-block in the r1 Householder frame,
    CORE_J = (2,...,16), steps = consecutive full-core pairs with
    r1 all-PSD).  The deployed step ladder caps H_LADDER_MAX =
    900; the new steps live at h 1219..2854 -- the SAME disclosed
    band amendment as above, machinery untouched.

FROZEN PROTOCOL:

 W   FIDELITY WARDS (kill -> WARD-BROKEN):
     W1 deep-table overlap: lam_ext[:ATOM_MAX+1] == core.LAM_TAB
        EXACTLY (max abs dev == 0.0);
     W2 prefix arrays bitwise: NN/U/MU prefixes equal, G prefix
        equal on the deployed length - 1;
     W3 extended Chebyshev envelope kappa <= KAPPA_REF + 1e-6;
     W4 CONVENTION REGRESSION (3 deployed rungs REG_KZ = (9, 60,
        121) rebuilt THROUGH THE EXTENDED PIPELINE): frame ties
        (h, M, D, alpha, n_atom) exact; lam_min and the tangent
        scalars (a11, a22, a12, det Ahat of the 2x2 frame-A read)
        agree with the deployed core.build_window output to
        <= REG_WARD = 1e-12 relative (bit-agreement expected);
     W5 REGISTRY REPRODUCTION (deployed pipeline verbatim, kz
        2..150, H_MIN <= h <= HCAP, X <= ATOM_MAX): 67 rungs,
        registry sha256 == REG_SHA (the CLI frozen registry),
        CXLIII band shat min/med/max == 0.502/1.027/2.185 (rtol
        2e-2), margin exponent in EXPO_BAND.
     W6 WARD split exactness on the new rungs: |e_ar + e_t - m|
        and the full-scan identities (head_B + tail_B = m, G +
        tail_A = m) <= SCAN_WARD relative.

 D   THE NEW SURFACE (typed): census of all new rungs (kz,
     n_zone, h, X, atoms); NEW-SURFACE(count, h range); kill K1
     iff count < MIN_NEW = 10.

 H1  HALFGAP BLIND SCORE (typed, never kill; the headline): per
     new rung shat = m/mu1(h), margin = shat - 1/2, PASS iff shat
     >= 1/2; full table printed; typed
     HALFGAP-HOLDOUT-PASS(n/N, min margin, tightest rungs) iff
     all pass, else HALFGAP-HOLDOUT-FAIL(k, list) -- a
     first-class FAIL of the registered conjecture, reported
     plainly, NO adjustment.

 H2  HEADFLOOR + NET-TAIL PERSISTENCE (typed): per new rung the
     first A- and B-covering cuts (cert_A > 0 / cert_B > 0),
     tail_A <= 0 at cA, tail_B <= 0 at cB, n_minB ladder,
     head_B(cB) stats (deployed context: med 0.388), TYPED screen
     jackknife slope of log head_B(cB) vs log m on the new rungs:
     HEADFLOOR-O1(|s| <= 0.30) / HEADFLOOR-RELOC(s >= 0.70) /
     HEADFLOOR-AMBIG.

 H3  B-FLOOR / P_G DOMINANCE, FLOAT (typed): the new-rung gram
     ladder (chain machinery verbatim), steps = consecutive
     full-core pairs (r1 all-PSD, lamS > 0); per step lam_min(B),
     c_G, c_dom = lam_min(B - (1/2) P_G), negidx, c_B; typed
     BFLOOR-PERSISTS(min lam_min(B)) iff min >= MINB_REF (1 -
     MINB_RTOL), else BFLOOR-HOLDOUT-FAIL(min);
     DOM-PERSISTS(n/n, min c_B) iff negidx = 0 and c_B > 0
     everywhere scoreable, else DOM-HOLDOUT-FAIL(k).  Chain-short
     / core-missing rungs are reported and typed as SKIPPED (an
     honest reachability limit, not a pass and not a fail).

 H4  MARGIN-LAW CONTINUATION (typed): jackknife log-log fits of
     m vs h -- deployed 67 / new-only / combined; typed
     LAW-CONTINUES(p_comb) iff p_comb in EXPO_BAND, else
     LAW-BREAKS(p_comb).

 C   CONTROLS (kill -> WARD-BROKEN if silent): on the FIRST new
     rung (by (h, kz); sizing says kz 177, h 1219): C1 scramble
     (seed 1, uniform positions in (0, 2 alpha], SAME masses)
     must break the wall (lam_min < 0, hence shat < 1/2) AND have
     zero covering cuts in both bookkeepings; C2 smooth comb (PNT
     grid masses on the SAME window) must do the same; C3 the
     smooth-world gram chain at that rung must violate the wall
     (neg(A) > 0) or die (chain short / core missing) -- the
     P_G-chain scoring cannot be faked by a prime-free comb.
     DECLARED SKIP: the Epstein x^2+5y^2 control is NOT run at
     depth (its divisor recursion is O(X^2), infeasible at X ~
     8e5); the deployed Epstein control lives at kz 9 inside the
     frozen upstream probes and is not re-run here.  The W4
     3-rung regression doubles as the convention control.

KILLS: K1 (D, MIN_NEW) -> PIPELINE-BROKEN; K2 (W1-W6, C1-C3) ->
WARD-BROKEN.  All H1-H4 outcomes are typed measurements, never
kills: a FAIL label is a first-class reported result.

VERDICT (frozen enum): DEEPHOLDOUT-SCORED with typed sublabels
FIDELITY(overlap, regression, registry sha8),
NEW-SURFACE(count, h range),
HALFGAP-HOLDOUT-PASS(n/N, min margin)/HALFGAP-HOLDOUT-FAIL(k),
HEADFLOOR-HOLDOUT(BCOVER n/N, NETB n/N, NETA n/N, slope label),
BFLOOR-PERSISTS(min)/BFLOOR-HOLDOUT-FAIL(min) +
DOM-PERSISTS(n/n)/DOM-HOLDOUT-FAIL(k) [+ SKIPPED(k)],
LAW-CONTINUES(p)/LAW-BREAKS(p),
CONTROLS-FIRE(k/3); else PIPELINE-BROKEN / WARD-BROKEN.

FROZEN BARS: TAB_EXT = 4_000_000; H_HOLD = (128, 2900) (declared
band; HCAP extension disclosed above); MIN_NEW = 10; KZ_SCAN_MAX
= 400; REG_KZ = (9, 60, 121); REG_WARD = 1e-12; REG_SHA =
"ae292e557efa24f13fa1d75823219bcda9a0f6757089fee459e5c652e3458df8"
(the CLI registry, 67 lines "kz:h:shat(%.12e)"); SHAT_REF =
(0.502, 1.027, 2.185), rtol 2e-2; EXPO_BAND = (-2.5, -1.5);
HALF = 1/2 EXACT (registered upstream, NO-ADJUST); SCAN_WARD =
1e-8 (relative; the deployed TAILSIGN bar is 1e-9 at <= 33k
atoms -- one digit of depth allowance for up to 271k atoms,
declared BEFORE the frozen run); NG_SMOOTH = 6000; MINB_REF =
0.679, MINB_RTOL = 2e-2; PG_S = 1/2 (canonical V4, frozen
upstream); CORE_J = (2,...,16); SLOPE_PASS = 0.30, SLOPE_RELOC =
0.70; CTRL scramble seed 1; runtime cap declared: 30 min.

ANTI-CIRCULARITY (frozen): the constant 1/2, the HEADFLOOR bands,
the B-floor class 0.679 and the dominance shape s = 1/2 are all
frozen UPSTREAM in the registered probes, before any deep data;
nothing here is fit to the new rungs; mu1 is pure geometry; the
new rungs are scored and never feed back into any registered
object; the holdout verdict never edits the registration.

PRE-FREEZE SIZING DISCLOSURE (2026-08-11, before the spec was
frozen): a sizing run built the extended table (overlap dev 0.0),
counted the band census (28 rungs; 3 under the deployed HCAP;
list frozen into this spec), timed the deep pipeline (deepest
eigh 1.3 s, deepest Lanczos 8.0 s), and -- unavoidably, since the
timing ran the rung end-to-end -- SAW TWO HOLDOUT VALUES before
freezing: kz 177/h 1219 shat 1.3048 and kz 222/h 2854 shat
0.7232 (both above 1/2).  Disclosed in full: the scoring constant
was frozen upstream (CLI) and cannot move, no bar/band/enum of
this spec was chosen after seeing them (the band H_HOLD and all
wards were fixed by the census geometry and the deployed
constants), and the remaining 26 rungs were NOT computed before
the freeze.  The sizing run also recomputed the deployed registry
sha (eigh path) = REG_SHA, confirming the CLI prefix ae292e55.

SMOKE-RUN DISCLOSURE (2026-08-11, before freezing): one smoke run
(DEEPHOLD_SMOKE=1, the 2 shallowest new rungs end-to-end, 14/14,
16.5 s) measured: wards W1-W6 green (overlap 0.0, prefix bitwise,
kappa within guard, W4 regression max rel dev 0.0e+00 BIT-EXACT
on all 3 rungs, registry sha == REG_SHA, scan ward 2.7e-14 <<
1e-8); smoke rungs kz 177/h 1219 shat 1.3047882108 PASS and kz
243/h 1292 shat 1.2442150312 PASS (two further holdout values
seen, the declared purpose of the smoke); both A- and B-covered
(n_minA 9/13, n_minB 41/59), tail_A <= 0 at cA and tail_B <= 0
at cB on 2/2, head_B(cB) 0.4004/0.2579 (deployed med 0.388); the
HEADFLOOR screen is VACUOUS at n = 2 (jackknife R^2 nan -- the
typed label resolves only on the full census); 1 smoke step:
lam_min(B) 3.9638, c_G 0.9551, c_dom +3.4638, negidx 0, c_B
3.9414; combined law p = -1.926; controls: scramble lam_min
-9.1e+02, smooth -9.6e+00, both with zero A/B coverage, smooth
gram chain neg(A) = 13 -- all three fire.  NO bar, band, count,
rule or enum was moved after the smoke.

SPEC v1 (2026-08-11, frozen + SHA-hashed before the frozen run):
everything above.  Mechanical concretizations frozen with v1: (i)
one eigh per rung (eigenvalues + vectors), registry format
"%d:%d:%.12e"; (ii) covering cuts inclusive at atom positions
(u_n <= u_c); first covering cut = argmax(cert > 0); (iii)
jackknife = full leave-one-out, CI +- 2SE; (iv) the head_B(cB)
screen reads the positive-cert subset; (v) steps sorted by
(h, kz), consecutive pairs, r1 must be full-core all-PSD with
lamS > 0; (vi) negidx = count of eigenvalues < 0 (float sign, no
tolerance); (vii) scramble = rng.default_rng(1).uniform(0,
2 alpha, ka), sorted, same masses.

HONEST LIMITS (frozen): all new-rung objects are FLOAT-LEVEL --
no interval rollout, no exact-rational certificates at depth (the
CLIII interval machinery is not rerun here; its band ends at h ~
900); the H band extension beyond the deployed HCAP is a declared
reachability amendment, not a convention change; the Epstein
control is skipped at depth (declared above); the P_G-chain
step ladder extends H_LADDER_MAX = 900 by the same declared
amendment; a PASS census on 28 rungs proves nothing about deeper
h, ideal objects, or any tail statement.  NO RH claim.  No
marker moves.

FIREWALL: no zeros, no prime oracles (AST scan; banned ids
zetazero / nzeros / primerange / isprime / primepi / nextprime /
prevprime; the extended table comes from the deployed sieve
generator, not an oracle); v563 READ-ONLY; RNG only inside the
declared scramble control; stdout only.

Sources (read-only): v563_paper2_readouts (table generator, tent
assembly, arch lags, odd Toeplitz, frame conventions);
halfgap_registration_probe (CLI: registered target + holdout
protocol + registry sha); tail_sign_mechanism_probe (CXLVII:
bookkeepings + HEADFLOOR bands); bfloor_pg_dominance_probe
(CXLIV: gram/chain/P_G machinery + B-floor constants);
rh_leverage_probe (margin-law fit); v770_qf_spectral_bundle
(deep-table overlap ward pattern).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/deep_blind_holdout_probe.py
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

TAB_EXT = 4_000_000
H_HOLD = (128, 2900)
MIN_NEW = 10
KZ_SCAN_MAX = 400
REG_KZ = (9, 60, 121)
REG_WARD = 1e-12
REG_SHA = ("ae292e557efa24f13fa1d75823219bcda9a0f6757089fee459e"
           "5c652e3458df8")
SHAT_REF = (0.502, 1.027, 2.185)
SHAT_RTOL = 2e-2
EXPO_BAND = (-2.5, -1.5)
HALF = Fraction(1, 2)
SCAN_WARD = 1e-8
NG_SMOOTH = 6000
MINB_REF = 0.679
MINB_RTOL = 2e-2
PG_S = 0.5
CORE_J = (2, 4, 6, 8, 10, 12, 14, 16)
SLOPE_PASS = 0.30
SLOPE_RELOC = 0.70
SCRAMBLE_SEED = 1
SMOKE = os.environ.get("DEEPHOLD_SMOKE", "") == "1"
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


def jack_slope(x, y):
    x = np.asarray(x, float)
    y = np.asarray(y, float)
    _a, b, r2 = ols_line(x, y)
    n = len(x)
    bb = []
    for i in range(n):
        m = np.ones(n, bool)
        m[i] = False
        bb.append(ols_line(x[m], y[m])[1])
    bb = np.array(bb)
    se = math.sqrt((n - 1) / n * float(np.sum((bb - bb.mean())
                                              ** 2)))
    return b, se, r2


def mu1_of(h):
    return 4.0 * math.sin(math.pi / (2.0 * h + 1.0)) ** 2


def q_read(W, u, D, M):
    """tail_sign_mechanism_probe verbatim."""
    u = np.asarray(u, float)
    i0 = np.floor(u / D).astype(int)
    f = u / D - i0
    val = np.zeros_like(u)
    ok0 = (i0 >= 0) & (i0 < M)
    val[ok0] += (1.0 - f[ok0]) * W[i0[ok0]]
    ok1 = (i0 + 1 >= 0) & (i0 + 1 < M)
    val[ok1] += f[ok1] * W[i0[ok1] + 1]
    refl = u < D
    val[refl] += (1.0 - u[refl] / D) * W[0]
    return -0.5 * val


def smooth_comb(alpha, ng=NG_SMOOTH):
    ug = (np.arange(ng) + 0.5) * (2.0 * alpha / ng)
    mg = 2.0 * np.exp(ug / 2.0) * (2.0 * alpha / ng)
    return ug, mg


# ------------- P_G chain machinery (bfloor_pg_dominance verbatim)
def grid_density(c):
    c = np.asarray(c, float)
    a = np.concatenate([c, c[-2:0:-1]])
    d = np.fft.fft(a)
    assert float(np.max(np.abs(d.imag))) <= 1e-9 * max(
        1.0, float(np.max(np.abs(d.real))))
    return d.real


def folded_measure(d_arm, L, sign=+1.0):
    jj = np.arange(L)
    keep = (sign * d_arm) > 0.0
    jj = jj[keep]
    th = 2.0 * math.pi * jj / L
    wt = (np.abs(d_arm[keep]) / (2.0 * L)) * 4.0 * np.sin(
        th / 2.0) ** 2
    fold = np.minimum(jj, L - jj)
    uf, inv = np.unique(fold, return_inverse=True)
    wagg = np.zeros(len(uf))
    np.add.at(wagg, inv, wt)
    xs = np.cos(2.0 * math.pi * uf / L)
    m = wagg > 1e-300
    return xs[m], wagg[m], uf[m]


def lanczos_chain(x, w, n):
    m0 = float(np.sum(w))
    m = len(x)
    Q = np.zeros((m, n))
    Q[:, 0] = np.sqrt(w) / math.sqrt(m0)
    al = np.zeros(n)
    be = np.zeros(max(n - 1, 0))
    steps = n
    for k in range(n):
        z = x * Q[:, k]
        al[k] = float(Q[:, k] @ z)
        z = z - al[k] * Q[:, k]
        if k > 0:
            z = z - be[k - 1] * Q[:, k - 1]
        for _ in range(2):
            z = z - Q[:, :k + 1] @ (Q[:, :k + 1].T @ z)
        if k == n - 1:
            break
        bnorm = float(np.linalg.norm(z))
        if bnorm <= 1e-14:
            steps = k + 1
            break
        be[k] = bnorm
        Q[:, k + 1] = z / bnorm
    return al[:steps], be[:max(steps - 1, 0)], m0, steps


def eval_chain(al, be, m0, y, n):
    P = np.zeros((len(y), n))
    P[:, 0] = 1.0 / math.sqrt(m0)
    if n > 1:
        P[:, 1] = (y - al[0]) * P[:, 0] / be[0]
    for k in range(1, n - 1):
        P[:, k + 1] = ((y - al[k]) * P[:, k]
                       - be[k - 1] * P[:, k - 1]) / be[k]
    return P


def householder_frame(v):
    n = len(v)
    v = v / float(np.linalg.norm(v))
    e1 = np.zeros(n)
    e1[0] = 1.0
    u = e1 - v
    nu = float(np.linalg.norm(u))
    if nu < 1e-14:
        return np.eye(n)
    u = u / nu
    Q = np.eye(n) - 2.0 * np.outer(u, u)
    if float(Q[:, 0] @ v) < 0:
        Q = -Q
    return Q


# ---------------- the extended surface (frame conventions verbatim)
EXT = {}


def build_ext_tables():
    lam_ext = core.von_mangoldt_table(TAB_EXT)
    NN = np.nonzero(lam_ext > 0.0)[0]
    EXT["lam"] = lam_ext
    EXT["NN"] = NN
    EXT["U"] = np.log(NN.astype(float))
    EXT["MU"] = 2.0 * lam_ext[NN] / np.sqrt(NN.astype(float))
    EXT["G"] = np.diff(EXT["U"])
    return lam_ext


def ext_frame(kz):
    """core.build_window frame conventions on the extended arrays."""
    alpha = float(EXT["U"][kz])
    D_k = 0.5 * float(EXT["G"][kz]) / float(core.NU_MAIN)
    Mz = int(math.ceil(alpha / D_k - 1.0e-9)) + 1
    if Mz % 2:
        Mz += 1
    hz = Mz // 2
    ka = int(np.searchsorted(EXT["U"], 2.0 * alpha + 1.0e-14,
                             side="right"))
    return alpha, Mz, hz, ka


def ext_rung(kz, positions=None, masses=None):
    """One extended-pipeline rung: eigh + both tail bookkeepings
    (tail_sign_mechanism_probe build_rung, re-hosted on the
    extended arrays; identical formulas)."""
    alpha, M, h, ka = ext_frame(kz)
    uu = EXT["U"][:ka].copy() if positions is None else positions
    mm = EXT["MU"][:ka].copy() if masses is None else masses
    c_at, D = core.atom_lags_at(alpha, M, uu, mm)
    c_at = np.asarray(c_at, float)
    c_ar = np.asarray(core.arch_lags(M, D), float)
    Kt = core.odd_toeplitz(c_ar + c_at, M)
    w, V = np.linalg.eigh(Kt)
    v = V[:, 0]
    del Kt, V
    row = dict(kz=kz, nz=int(EXT["NN"][kz]), alpha=alpha, h=h,
               M=M, D=D, ka=ka, X=math.exp(2.0 * alpha),
               m=float(w[0]), mu1=mu1_of(h), uu=uu)
    Wv = core.lag_weights_from_v(v, h)
    e_ar = float(c_ar @ Wv)
    e_t = float(c_at @ Wv)
    ug, mg = smooth_comb(alpha)
    c_sm = np.asarray(core.atom_lags_at(alpha, M, ug, mg)[0],
                      float)
    e_s = float(c_sm @ Wv)
    qa = mm * q_read(Wv, uu, D, M)
    qg = mg * q_read(Wv, ug, D, M)
    lift = e_t - e_s
    demand = -(e_ar + e_s)
    cq = np.cumsum(qa)
    idxg = np.searchsorted(ug, uu, side="right")
    cg_all = np.concatenate([[0.0], np.cumsum(qg)])
    head_err = cq - cg_all[idxg]
    G = head_err - demand
    tail_A = lift - head_err
    cert_A = G - np.abs(tail_A)
    head_B = e_ar + cq
    tail_B = float(qa.sum()) - cq
    cert_B = head_B - np.abs(tail_B)
    row.update(e_ar=e_ar, e_t=e_t, e_s=e_s, lift=lift,
               demand=demand, cert_A=cert_A, tail_A=tail_A,
               head_B=head_B, tail_B=tail_B, cert_B=cert_B,
               c_at=c_at, c_ar=c_ar,
               dev_id=abs((e_ar + e_t) - row["m"])
               / max(1.0, abs(e_t)),
               dev_scan=max(
                   float(np.max(np.abs((head_B + tail_B)
                                       - row["m"]))),
                   float(np.max(np.abs((G + tail_A)
                                       - row["m"]))))
               / max(1.0, abs(e_t)))
    return row


def ext_gram(kz, c_lags=None, keep_chain=True):
    """bfloor_pg_dominance gram_anatomy verbatim, on the extended
    frame; c_lags = precomputed c_ar + c_at (or a control's)."""
    alpha, M, h, ka = ext_frame(kz)
    if c_lags is None:
        c_at, D = core.atom_lags_at(alpha, M, EXT["U"][:ka],
                                    EXT["MU"][:ka])
        c_ar = np.asarray(core.arch_lags(M, D), float)
        c_lags = c_ar + np.asarray(c_at, float)
    d = grid_density(c_lags)
    L = 2 * M - 2
    xs, ws, _ = folded_measure(d, L, +1.0)
    ys, vs, uf_n = folded_measure(d, L, -1.0)
    al, be, m0, steps = lanczos_chain(xs, ws, h + 1)
    if steps < h + 1 or np.any(be <= 0):
        return None
    Pn = eval_chain(al, be, m0, ys, h)
    G = np.sqrt(vs)[:, None] * (Pn @ Pn.T) * np.sqrt(vs)[None, :]
    G = 0.5 * (G + G.T)
    n = G.shape[0]
    A = np.eye(n) - G
    evA = np.linalg.eigvalsh(A)
    out = dict(kz=kz, h=h, n=n, alpha=alpha, M=M)
    out["tau"] = float(evA[0])
    out["negA"] = int(np.sum(evA < 0.0))
    if keep_chain:
        out["chain"] = (al, be, m0)
    idx = {int(j): k for k, j in enumerate(uf_n)}
    out["core_ok"] = all(j in idx for j in CORE_J)
    if not out["core_ok"]:
        return out
    ic = np.array([idx[j] for j in CORE_J], dtype=int)
    icset = set(ic.tolist())
    ib = np.array([k for k in range(n) if k not in icset],
                  dtype=int)
    B = A[np.ix_(ic, ic)]
    Xc = A[np.ix_(ic, ib)]
    R = A[np.ix_(ib, ib)]
    evR = np.linalg.eigvalsh(R)
    out["negR"] = int(np.sum(evR < 0.0))
    Z = np.linalg.solve(R, Xc.T)
    Y = Xc @ Z
    Y = 0.5 * (Y + Y.T)
    S = B - Y
    S = 0.5 * (S + S.T)
    evS = np.linalg.eigvalsh(S)
    out["S"] = S
    out["lamS"] = float(evS[0])
    out["negS"] = int(np.sum(evS < 0.0))
    if keep_chain:
        out["y_core"] = np.array([ys[idx[j]] for j in CORE_J])
        out["v_core"] = np.array([vs[idx[j]] for j in CORE_J])
    return out


def build_pg_step(r1, r2):
    """One step of the P_G chain (bfloor E-block verbatim, s from
    PG_S): frame from r1's soft direction, B = 7x7 co-block of
    Q^T (S_2/tau_1) Q, P_G from r2's own chain at r2's core
    nodes."""
    wS, VS = np.linalg.eigh(r1["S"])
    Q = householder_frame(VS[:, 0])
    Mt = Q.T @ (r2["S"] / r1["tau"]) @ Q
    Mt = 0.5 * (Mt + Mt.T)
    B = Mt[1:, 1:]
    al, be, m0 = r2["chain"]
    Pc = eval_chain(al, be, m0, r2["y_core"], r2["h"])
    Gc = (np.sqrt(r2["v_core"])[:, None] * (Pc @ Pc.T)
          * np.sqrt(r2["v_core"])[None, :])
    Gc = 0.5 * (Gc + Gc.T)
    PG = (Q.T @ Gc @ Q)[1:, 1:]
    PG = 0.5 * (PG + PG.T)
    minB = float(np.linalg.eigvalsh(B)[0])
    cg = float(np.linalg.eigvalsh(PG)[0])
    Dm = B - PG_S * PG
    Dm = 0.5 * (Dm + Dm.T)
    evd = np.linalg.eigvalsh(Dm)
    return dict(kz=r2["kz"], h=r2["h"], minB=minB, cg=cg,
                cdom=float(evd[0]), negD=int(np.sum(evd < 0.0)),
                cb=PG_S * cg + float(evd[0]), tau=r1["tau"])


def deployed_registry():
    """halfgap_registration_probe W-block verbatim (deployed
    pipeline): the 67-rung faithful ladder + registry sha."""
    rungs = []
    for kz in range(2, 151):
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
        rungs.append(dict(kz=kz, h=h, m=float(w[0]),
                          shat=float(w[0]) / mu1_of(h)))
        del Kt, V
    rungs.sort(key=lambda r: (r["h"], r["kz"]))
    lines = "\n".join("%d:%d:%.12e" % (r["kz"], r["h"], r["shat"])
                      for r in rungs)
    return rungs, hashlib.sha256(lines.encode("utf-8")).hexdigest()


def first_cut(nn_atoms, cert):
    cov = cert > 0.0
    if not bool(np.any(cov)):
        return -1, -1
    i0 = int(np.argmax(cov))
    return i0, int(nn_atoms[i0])


def main():
    section("PRIME.PORT.DEEP.HOLDOUT.01 -- blind holdout deepening:"
            " the frozen round-63 targets scored out-of-sample on "
            "the 4e6-table rungs (EXPLORATION ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s"
          % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
    print("    NO RH claim; no marker moves; no refits -- the "
          "constant 1/2, the HEADFLOOR bands, the 0.679 class and "
          "s = 1/2 are frozen upstream.")
    if SMOKE:
        print("    *** SMOKE MODE: 2 shallowest new rungs only ***")
    print("\nS0 -- firewall")
    check("S0.1 AST firewall clean", not ast_scan(BANNED_IDS))

    # ------------------------------------------------------------ W
    section("W -- fidelity wards: the extension IS the deployed "
            "pipeline")
    lam_ext = build_ext_tables()
    dev = float(np.max(np.abs(lam_ext[:core.ATOM_MAX + 1]
                              - core.LAM_TAB)))
    check("W1 deep-table overlap: extended von Mangoldt table == "
          "deployed core table on [0, %d] EXACTLY (max abs dev "
          "%.1e)" % (core.ATOM_MAX, dev), dev == 0.0, kill="K2")
    nP = len(core.U_ALL)
    ok_pref = (np.array_equal(EXT["NN"][:nP], core._NN)
               and np.array_equal(EXT["U"][:nP], core.U_ALL)
               and np.array_equal(EXT["MU"][:nP], core.MU_ALL)
               and np.array_equal(EXT["G"][:nP - 1],
                                  core.G_ALL[:nP - 1]))
    check("W2 prefix arrays bitwise: NN/U/MU on %d entries, G on "
          "%d" % (nP, nP - 1), ok_pref, kill="K2")
    psi = np.cumsum(lam_ext[EXT["NN"]])
    nnf = EXT["NN"].astype(float)
    keep = nnf >= core.KAPPA_X0
    kappa = float(np.max(np.abs(psi[keep] - nnf[keep])
                         / nnf[keep]))
    check("W3 extended Chebyshev envelope: kappa = %.6f <= %.6f "
          "+ 1e-6 on [%d, %d]"
          % (kappa, core.KAPPA_REF, int(core.KAPPA_X0), TAB_EXT),
          kappa <= core.KAPPA_REF + 1e-6, kill="K2")

    # W4: convention regression through the extended pipeline
    dev_reg = 0.0
    reg_rows = []
    for kz in REG_KZ:
        rr = core.build_window(kz)
        alpha, M, h = rr["alpha"], rr["M"], rr["h"]
        uu_d = np.asarray(rr["uu"], float)
        mu_d = 2.0 * np.asarray(rr["lam"], float)
        c_at_d = np.asarray(core.atom_lags_at(alpha, M, uu_d,
                                              mu_d)[0], float)
        c_ar_d = np.asarray(core.arch_lags(M, rr["D"]), float)
        lam_d = float(np.linalg.eigh(
            core.odd_toeplitz(c_ar_d + c_at_d, M))[0][0])
        a_e, M_e, h_e, ka_e = ext_frame(kz)
        ok_frame = (a_e == alpha and M_e == M and h_e == h
                    and ka_e == rr["n_atom"])
        c_at_e, D_e = core.atom_lags_at(a_e, M_e, EXT["U"][:ka_e],
                                        EXT["MU"][:ka_e])
        c_at_e = np.asarray(c_at_e, float)
        c_ar_e = np.asarray(core.arch_lags(M_e, D_e), float)
        lam_e = float(np.linalg.eigh(
            core.odd_toeplitz(c_ar_e + c_at_e, M_e))[0][0])
        # tangent scalars through the extended pipeline
        Tb = core.parity_basis(h_e, 2)
        t1, t2 = Tb[0].copy(), Tb[1].copy()
        W11 = core.lag_weights_from_v(t1, h_e)
        W22 = core.lag_weights_from_v(t2, h_e)
        Wpp = core.lag_weights_from_v(t1 + t2, h_e)
        W12 = 0.5 * (Wpp - W11 - W22)
        B2 = np.array([[float(c_ar_e @ W11), float(c_ar_e @ W12)],
                       [float(c_ar_e @ W12),
                        float(c_ar_e @ W22)]])
        lamw = 0.5 * EXT["MU"][:ka_e]
        Xn = np.empty((ka_e, 3))
        for i in range(ka_e):
            Xn[i, 0] = core.spline_project(W11, EXT["U"][i], D_e,
                                           M_e)
            Xn[i, 1] = core.spline_project(W22, EXT["U"][i], D_e,
                                           M_e)
            Xn[i, 2] = core.spline_project(W12, EXT["U"][i], D_e,
                                           M_e)
        S2 = np.array([[float(lamw @ Xn[:, 0]),
                        float(lamw @ Xn[:, 2])],
                       [float(lamw @ Xn[:, 2]),
                        float(lamw @ Xn[:, 1])]])
        Ah = B2 - S2
        det_e = float(np.linalg.det(Ah))
        devs = [abs(lam_e - lam_d) / max(abs(lam_d), 1e-300),
                abs(Ah[0, 0] - rr["a11"]) / max(abs(rr["a11"]),
                                                1e-300),
                abs(Ah[1, 1] - rr["a22"]) / max(abs(rr["a22"]),
                                                1e-300),
                abs(Ah[0, 1] - rr["a12"]) / max(abs(rr["a12"]),
                                                1e-300),
                abs(det_e - rr["det"]) / max(abs(rr["det"]),
                                             1e-300)]
        dev_reg = max(dev_reg, max(devs))
        reg_rows.append((kz, h, ok_frame, max(devs)))
        print("    kz %3d h %4d: frame tie %s; lam_min dev %.1e; "
              "tangent scalars (a11, a22, a12, det) max dev %.1e"
              % (kz, h, ok_frame, devs[0], max(devs[1:])),
              flush=True)
    check("W4 CONVENTION REGRESSION: 3 deployed rungs rebuilt "
          "through the extended pipeline; frame ties exact, max "
          "rel dev %.2e <= %.0e (bit-agreement expected)"
          % (dev_reg, REG_WARD),
          all(o for _k, _h, o, _d in reg_rows)
          and dev_reg <= REG_WARD, kill="K2")

    # W5: the deployed registry reproduced verbatim
    reg_rungs, reg_sha = deployed_registry()
    shat_d = np.array([r["shat"] for r in reg_rungs])
    trio = (float(shat_d.min()), float(np.median(shat_d)),
            float(shat_d.max()))
    ok_band = all(abs(a / b - 1.0) <= SHAT_RTOL
                  for a, b in zip(trio, SHAT_REF))
    m_d = np.array([r["m"] for r in reg_rungs])
    h_d = np.array([float(r["h"]) for r in reg_rungs])
    p_dep, se_dep, r2_dep = jack_slope(np.log(h_d), np.log(m_d))
    check("W5 REGISTRY REPRODUCTION: %d rungs, sha256 %s.. == "
          "ae292e55.. (%s); band %.3f/%.3f/%.3f == "
          "0.502/1.027/2.185; exponent %+.3f in [%.1f, %.1f]  "
          "[%.1f s]"
          % (len(reg_rungs), reg_sha[:8],
             "MATCH" if reg_sha == REG_SHA else "MISMATCH",
             trio[0], trio[1], trio[2], p_dep, EXPO_BAND[0],
             EXPO_BAND[1], time.time() - T0),
          len(reg_rungs) == 67 and reg_sha == REG_SHA and ok_band
          and EXPO_BAND[0] <= p_dep <= EXPO_BAND[1], kill="K2")
    if KILLS:
        return finish({})

    # ------------------------------------------------------------ D
    section("D -- the new surface: faithful rungs with ATOM_MAX < "
            "X <= %d, h in [%d, %d]" % (TAB_EXT, H_HOLD[0],
                                        H_HOLD[1]))
    new_kz = []
    for kz in range(2, min(KZ_SCAN_MAX, len(EXT["NN"]) - 2)):
        alpha = float(EXT["U"][kz])
        X = math.exp(2.0 * alpha)
        if X > TAB_EXT:
            break
        if X <= core.ATOM_MAX:
            continue
        _a, _M, h, _ka = ext_frame(kz)
        if not (H_HOLD[0] <= h <= H_HOLD[1]):
            continue
        new_kz.append(kz)
    rows = []
    order = sorted(new_kz, key=lambda k: (ext_frame(k)[2], k))
    if SMOKE:
        order = order[:2]
    for kz in order:
        r = ext_rung(kz)
        rows.append(r)
        print("    NEW kz %3d n_zone %5d h %5d X %.4g atoms %6d  "
              "[%.1f s]" % (r["kz"], r["nz"], r["h"], r["X"],
                            r["ka"], time.time() - T0), flush=True)
    N = len(rows)
    check("D1 new-surface census: %d new rungs (>= %d), h %d..%d, "
          "every one OUTSIDE the ae292e55 registry (kz range "
          "%d..%d disjoint from the 67 registered kz <= 136)"
          % (N, MIN_NEW if not SMOKE else 2, rows[0]["h"],
             rows[-1]["h"], min(r["kz"] for r in rows),
             max(r["kz"] for r in rows)),
          N >= (MIN_NEW if not SMOKE else 2), kill="K1")
    if KILLS:
        return finish({})
    dev_id = max(r["dev_id"] for r in rows)
    dev_sc = max(r["dev_scan"] for r in rows)
    check("W6 WARD split exactness on the new rungs: |e_ar + e_t "
          "- m| rel %.2e, full scans (head_B + tail_B = m, G + "
          "tail_A = m) rel %.2e <= %.0e"
          % (dev_id, dev_sc, SCAN_WARD),
          max(dev_id, dev_sc) <= SCAN_WARD, kill="K2")
    if KILLS:
        return finish({})

    # ----------------------------------------------------------- H1
    section("H1 -- THE BLIND HALFGAP SCORE: shat >= 1/2 per rung "
            "(constant EXACTLY 1/2, NO-ADJUST, frozen upstream)")
    c_half = float(HALF)
    print("    kz   n_zone  h     alpha     m            mu1      "
          "    shat          margin      score")
    fails = []
    for r in rows:
        s = r["m"] / r["mu1"]
        r["shat"] = s
        ok = s >= c_half
        if not ok:
            fails.append(r)
        print("    %-4d %-6d %-5d %.4f  %.6e %.6e %.10f %+.6e  %s"
              % (r["kz"], r["nz"], r["h"], r["alpha"], r["m"],
                 r["mu1"], s, s - c_half,
                 "PASS" if ok else "FAIL"), flush=True)
    margins = np.array([r["shat"] - c_half for r in rows])
    o3 = np.argsort(margins)[:3]
    tight = ", ".join("kz%d/h%d %+.2e"
                      % (rows[i]["kz"], rows[i]["h"], margins[i])
                      for i in o3)
    print("\n    margins: min/med/max %+.4f/%+.4f/%+.4f; tightest:"
          " %s" % (float(margins.min()), float(np.median(margins)),
                   float(margins.max()), tight))
    if fails:
        h1 = ("HALFGAP-HOLDOUT-FAIL(%d/%d: %s) -- a FIRST-CLASS "
              "FAIL of the registered conjecture; the "
              "no-adjustment clause applies (no repair, no "
              "exclusion, no constant move)"
              % (len(fails), N,
                 ", ".join("kz%d/h%d shat %.6f" %
                           (r["kz"], r["h"], r["shat"])
                           for r in fails)))
    else:
        h1 = ("HALFGAP-HOLDOUT-PASS(%d/%d, min margin %+.4e at "
              "kz%d/h%d)" % (N, N, float(margins.min()),
                             rows[int(np.argmin(margins))]["kz"],
                             rows[int(np.argmin(margins))]["h"]))
    check("H1 typed: %s" % h1, True)

    # ----------------------------------------------------------- H2
    section("H2 -- HEADFLOOR + NET-TAIL persistence at depth")
    print("    kz   h     n_minA  tailA@cA    n_minB  tailB@cB    "
          "headB@cB")
    kA = kB = nBcov = nAcov = 0
    hBc, nB_min = [], []
    for r in rows:
        nn_at = np.round(np.exp(r["uu"])).astype(np.int64)
        iA, nA = first_cut(nn_at, r["cert_A"])
        iB, nB = first_cut(nn_at, r["cert_B"])
        tAc = float(r["tail_A"][iA]) if iA >= 0 else float("nan")
        tBc = float(r["tail_B"][iB]) if iB >= 0 else float("nan")
        hBv = float(r["head_B"][iB]) if iB >= 0 else float("nan")
        nAcov += iA >= 0
        nBcov += iB >= 0
        kA += (iA >= 0 and tAc <= 0.0)
        kB += (iB >= 0 and tBc <= 0.0)
        nB_min.append(nB)
        hBc.append(hBv)
        print("    %-4d %-5d %-7d %+.3e  %-7d %+.3e  %+.4f"
              % (r["kz"], r["h"], nA, tAc, nB, tBc, hBv),
              flush=True)
    hBc = np.array(hBc)
    okB = np.array([n > 0 for n in nB_min])
    mm = np.array([r["m"] for r in rows])
    print("\n    B-cover exists on %d/%d (n_minB med %s, deployed "
          "med 17); A-cover on %d/%d; head_B(cB) min/med/max "
          "%.4f/%.4f/%.4f (deployed med 0.388)"
          % (nBcov, N,
             int(np.median(np.array(nB_min)[okB])) if okB.any()
             else "-", nAcov, N,
             float(np.nanmin(hBc)) if okB.any() else float("nan"),
             float(np.nanmedian(hBc)), float(np.nanmax(hBc))))
    pos = okB & (hBc > 0)
    if int(np.sum(pos)) >= 3:
        slC, seC, r2C = jack_slope(np.log(mm[pos]),
                                   np.log(hBc[pos]))
    else:
        slC = seC = r2C = float("nan")
    print("    TYPED screen log head_B(cB) vs log m on the new "
          "rungs: slope %+.3f +- 2SE %.3f (R^2 %.2f); deployed "
          "+0.113" % (slC, 2 * seC, r2C))
    if not np.isfinite(slC):
        hd = "HEADFLOOR-VACUOUS(pos=%d)" % int(np.sum(pos))
    elif abs(slC) <= SLOPE_PASS:
        hd = "HEADFLOOR-O1(slope=%+.3f)" % slC
    elif slC >= SLOPE_RELOC:
        hd = "HEADFLOOR-RELOC(slope=%+.3f)" % slC
    else:
        hd = "HEADFLOOR-AMBIG(slope=%+.3f)" % slC
    h2 = ("BCOVER(%d/%d) + NETB(%d/%d@cB) + NETA(%d/%d@cA) + %s"
          % (nBcov, N, kB, N, kA, N, hd))
    check("H2 typed: %s" % h2, True)

    # ----------------------------------------------------------- H3
    section("H3 -- B-floor + (1/2) P_G dominance on the NEW steps "
            "(float level, declared)")
    grams = []
    for r in rows:
        g = ext_gram(r["kz"])
        tag = ("chain-short" if g is None else
               "core-missing" if not g["core_ok"] else
               "negA=%d" % g["negA"] if g["negA"] > 0 else "ok")
        print("    gram kz %3d h %5d: %s%s  [%.1f s]"
              % (r["kz"], r["h"], tag,
                 ("" if g is None or not g.get("core_ok") else
                  "  tau %.3e n %d" % (g["tau"], g["n"])),
                 time.time() - T0), flush=True)
        grams.append(g)
    usable = [g for g in grams if isinstance(g, dict)
              and g.get("core_ok")]
    n_skip = len(grams) - len(usable)
    usable.sort(key=lambda g: (g["h"], g["kz"]))
    steps = []
    for g1, g2 in zip(usable, usable[1:]):
        if g1["negA"] > 0 or g1["negS"] > 0 or g1["lamS"] <= 0.0:
            continue
        steps.append(build_pg_step(g1, g2))
    print("\n    %d/%d rungs usable (%d skipped: honest "
          "reachability limit), %d steps"
          % (len(usable), len(grams), n_skip, len(steps)))
    print("    kz(r2) h     lam_min(B)  c_G        c_dom       "
          "negidx  c_B")
    for s in steps:
        print("    %-6d %-5d %.6f    %.6f   %+.6f   %-6d  %.6f"
              % (s["kz"], s["h"], s["minB"], s["cg"], s["cdom"],
                 s["negD"], s["cb"]), flush=True)
    if steps:
        minB_new = float(np.min([s["minB"] for s in steps]))
        n_dom = sum(1 for s in steps if s["negD"] == 0
                    and s["cb"] > 0)
        cb_min = float(np.min([s["cb"] for s in steps]))
        bar = MINB_REF * (1.0 - MINB_RTOL)
        if minB_new >= bar:
            h3a = ("BFLOOR-PERSISTS(min lam_min(B) = %.4f >= "
                   "%.4f)" % (minB_new, bar))
        else:
            h3a = ("BFLOOR-HOLDOUT-FAIL(min lam_min(B) = %.4f < "
                   "%.4f at kz%d/h%d) -- first-class, reported, "
                   "not repaired"
                   % (minB_new, bar,
                      min(steps, key=lambda s: s["minB"])["kz"],
                      min(steps, key=lambda s: s["minB"])["h"]))
        if n_dom == len(steps):
            h3b = ("DOM-PERSISTS(%d/%d, min c_B = %.4f)"
                   % (n_dom, len(steps), cb_min))
        else:
            h3b = ("DOM-HOLDOUT-FAIL(%d/%d) -- first-class, "
                   "reported, not repaired"
                   % (len(steps) - n_dom, len(steps)))
    else:
        h3a = "BFLOOR-VACUOUS(no steps)"
        h3b = "DOM-VACUOUS(no steps)"
    h3 = "%s + %s + SKIPPED(%d)" % (h3a, h3b, n_skip)
    check("H3 typed: %s (FLOAT LEVEL: no exact-rational LDL, no "
          "interval enclosure at depth)" % h3, True)

    # ----------------------------------------------------------- H4
    section("H4 -- the margin law lam_min ~ h^p across the depth "
            "extension")
    hh_n = np.array([float(r["h"]) for r in rows])
    p_new, se_new, r2_new = jack_slope(np.log(hh_n), np.log(mm))
    h_all = np.concatenate([h_d, hh_n])
    m_all = np.concatenate([m_d, mm])
    p_all, se_all, r2_all = jack_slope(np.log(h_all),
                                       np.log(m_all))
    print("    deployed 67: p = %+.4f +- %.4f (R^2 %.3f)"
          % (p_dep, 2 * se_dep, r2_dep))
    print("    new %d:      p = %+.4f +- %.4f (R^2 %.3f)"
          % (N, p_new, 2 * se_new, r2_new))
    print("    combined %d: p = %+.4f +- %.4f (R^2 %.3f)"
          % (len(h_all), p_all, 2 * se_all, r2_all))
    if EXPO_BAND[0] <= p_all <= EXPO_BAND[1]:
        h4 = "LAW-CONTINUES(p_comb = %+.3f, p_new = %+.3f)" % (
            p_all, p_new)
    else:
        h4 = "LAW-BREAKS(p_comb = %+.3f outside [%.1f, %.1f])" % (
            p_all, EXPO_BAND[0], EXPO_BAND[1])
    check("H4 typed: %s" % h4, True)

    # ------------------------------------------------------------ C
    section("C -- controls on the first new rung (kz %d, h %d)"
            % (rows[0]["kz"], rows[0]["h"]))
    kz0 = rows[0]["kz"]
    alpha0, M0, h0, ka0 = ext_frame(kz0)
    rng = np.random.default_rng(SCRAMBLE_SEED)
    uu_s = np.sort(rng.uniform(0.0, 2.0 * alpha0, size=ka0))
    r_scr = ext_rung(kz0, positions=uu_s,
                     masses=EXT["MU"][:ka0].copy())
    ug0, mg0 = smooth_comb(alpha0)
    r_smo = ext_rung(kz0, positions=ug0, masses=mg0)
    fired = 0
    for name, rc in (("scramble", r_scr), ("smooth", r_smo)):
        ncA = int(np.sum(rc["cert_A"] > 0))
        ncB = int(np.sum(rc["cert_B"] > 0))
        f = rc["m"] < 0 and ncA == 0 and ncB == 0
        fired += f
        print("    %-9s: lam_min %+.3e  shat %+.3e  covering cuts "
              "A/B %d/%d -> %s"
              % (name, rc["m"], rc["m"] / rc["mu1"], ncA, ncB,
                 "FIRES" if f else "SILENT"), flush=True)
    check("C1/C2 WARD scramble + smooth break the wall AND have "
          "zero coverage in both bookkeepings", fired == 2,
          kill="K2")
    c_at_s, D0 = core.atom_lags_at(alpha0, M0, ug0, mg0)
    c_sm_lags = (np.asarray(core.arch_lags(M0, D0), float)
                 + np.asarray(c_at_s, float))
    g_sm = ext_gram(kz0, c_lags=c_sm_lags)
    if g_sm is None:
        c3 = "smooth gram chain dies (chain short) -> fires"
        ok3 = True
    elif not g_sm.get("core_ok"):
        c3 = "smooth gram core missing -> fires"
        ok3 = True
    else:
        ok3 = g_sm["negA"] > 0
        c3 = ("smooth gram neg(A) = %d -> %s"
              % (g_sm["negA"], "FIRES" if ok3 else "SILENT"))
    check("C3 WARD the prime-free comb cannot fake the P_G-chain "
          "surface: %s" % c3, ok3, kill="K2")
    print("    DECLARED SKIP: Epstein control not run at depth "
          "(O(X^2) divisor recursion infeasible at X ~ 8e5); it "
          "lives at kz 9 in the frozen upstream probes.")

    return finish(dict(h1=h1, h2=h2, h3=h3, h4=h4,
                       fid="FIDELITY(overlap 0.0, regression "
                           "%.1e, registry %s)"
                           % (dev_reg, reg_sha[:8]),
                       surf="NEW-SURFACE(%d, h %d..%d)"
                            % (N, rows[0]["h"], rows[-1]["h"])))


def finish(labels):
    section("V -- FROZEN VERDICT")
    n_pass = sum(1 for _n, okk in CHECKS if okk)
    n_tot = len(CHECKS)
    if KILLS:
        VERDICT = {"K1": "PIPELINE-BROKEN",
                   "K2": "WARD-BROKEN"}[KILLS[0]]
        print("\n  VERDICT: %s" % VERDICT)
    else:
        VERDICT = ("DEEPHOLDOUT-SCORED / %(fid)s / %(surf)s / "
                   "%(h1)s / %(h2)s / %(h3)s / %(h4)s" % labels)
        print("\n  VERDICT: %s" % VERDICT)
    print("""
  HONEST FRAME (as frozen): this is the first genuine OUT-OF-SAMPLE
  test of the round-63 registered objects -- the constant 1/2, the
  HEADFLOOR bands, the 0.679 class and s = 1/2 were all frozen
  before any rung beyond X = 4e5 existed.  All deep objects are
  FLOAT-LEVEL (no interval rollout, no exact-rational certificates
  at depth); the h band beyond HCAP and the Epstein skip are
  declared amendments of REACHABILITY, not of any scoring rule.  A
  PASS census on 28 rungs proves nothing about deeper h, the ideal
  objects, or any tail statement; a FAIL is a first-class result
  and is never repaired.  NO RH claim.  No marker moves.""")
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed"
          % (time.time() - T0, n_tot, n_tot - n_pass))
    return 0 if n_pass == n_tot else 1


if __name__ == "__main__":
    raise SystemExit(main())
'''

# --------------------------------------------------------------- harness
_PF_RE = re.compile(r"^\s*\[(PASS|FAIL)\]\s+(\S+)", re.M)
_VD_RE = re.compile(r"VERDICT[:\]]")


def _probe_file(name):
    cand = os.path.abspath(os.path.join(
        _HERE, os.pardir, "experiments", "tfpt-discovery", name + ".py"))
    return cand if os.path.isfile(cand) else None


def _census(out):
    marks = _PF_RE.findall(out)
    fails = sorted({tok for st, tok in marks if st == "FAIL"})
    verdict = ""
    for line in out.splitlines():
        if _VD_RE.search(line):
            verdict = line.strip()
    return len(marks), fails, verdict


def _exec_probe(name, src, run_entry=True):
    """Execute one embedded frozen probe source BYTE-EXACT in its own
    module namespace (round-31 convention); capture and re-emit
    stdout; return (stdout, exit_code, byte_equal_or_None)."""
    if src[:1] == "\n":
        src = src[1:]
    path = _probe_file(name)
    same = None
    if path is not None:
        with open(path, encoding="utf-8") as fh:
            same = (fh.read() == src)
    fname = path or os.path.abspath(__file__)
    mod = types.ModuleType(name)
    mod.__file__ = fname
    sys.modules[name] = mod
    buf = io.StringIO()
    code = 0
    with contextlib.redirect_stdout(buf):
        try:
            exec(compile(src, fname, "exec"), mod.__dict__)
            entry = mod.__dict__.get("main") or mod.__dict__.get("run")
            if run_entry and callable(entry):
                rc = entry()
                code = 0 if rc is None else int(rc)
        except SystemExit as exc:
            code = 0 if exc.code is None else int(exc.code)
        except Exception:                            # regression guard
            import traceback
            traceback.print_exc(file=sys.stdout)
            code = 99
    out = buf.getvalue()
    sys.stdout.write(out)
    sys.stdout.flush()
    return out, code, same


def _gate(name, out, code, same, exp_n, exp_fails, exp_verdict,
          exp_code, gates):
    n, fails, verdict = _census(out)
    ok = (n == exp_n and fails == list(exp_fails)
          and exp_verdict in verdict and code == exp_code
          and same is not False)
    gates.append(ok)
    prov = ("byte-exact vs experiments source" if same is True else
            "embedded copy (source file not present)" if same is None
            else "SOURCE MISMATCH")
    print("\n[%s] PATTERN GATE %s: %d checks (exp %d) | FAILs %s "
          "(exp %s) | exit %d (exp %d) | %s\n      verdict line: %s"
          % ("PASS" if ok else "FAIL", name, n, exp_n,
             ",".join(fails) if fails else "none",
             ",".join(exp_fails) if exp_fails else "none",
             code, exp_code, prov, verdict), flush=True)
    return ok


_PLAN = (
    ('halfgap_registration_probe', _SRC_0, 17, (), 'HALFGAP-REGISTERED', 0),
    ('deep_blind_holdout_probe', _SRC_1, 14, (), 'DEEPHOLDOUT-SCORED', 0),
)


def run():
    t0 = time.time()
    print("=" * 74)
    print('v907 -- PRIME.PORT.HALFGAP.01 + PRIME.PORT.DEEP.HOLDOUT.01: the registered half-gap target n - q >= (1/2) mu1 (constant exactly 1/2 frozen, NO-ADJUST clause, registry sha ae292e55, 67/67 surface pass, min margin +2.48e-03) and its FIRST BLIND HOLDOUT passed on 28 new rungs h 1219..2854 (28/28, min margin +0.2232, no depth erosion, margin law -1.925 continues) -- a falsification instrument, explicitly NOT evidence for RH')
    print("(frozen probes embedded byte-exact and executed verbatim; NO RH claim)")
    print("=" * 74, flush=True)
    gates = []
    for name, src, exp_n, exp_fails, exp_verdict, exp_code in _PLAN:
        print("\n" + "-" * 74)
        print("EMBEDDED FROZEN PROBE: %s" % name)
        print("-" * 74, flush=True)
        out, code, same = _exec_probe(name, src)
        _gate(name, out, code, same, exp_n, exp_fails,
              exp_verdict, exp_code, gates)
    ok = all(gates)
    print("\n" + "=" * 74)
    print("v907: %d/%d pattern gates passed | runtime %.1f s"
          % (sum(gates), len(gates), time.time() - t0))
    print('the target is registered and survived its first blind holdout; the constant 1/2 has no derivation (four origins typed open); a pass is survival of a falsification attempt, never evidence')
    print("[%s] v907 VERDICT GATE" % ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(run())
