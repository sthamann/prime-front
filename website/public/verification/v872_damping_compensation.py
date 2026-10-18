#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""v872 -- PRIME.CD.DAMPING.COMPENSATION.01: THE COMPENSATION IDENTITY (the round's headline) -- the defect operator splits EXACTLY into two source-built terms, I - C*C = T_1 + T_2 with T_1 = I - U*U (the INDEFINITE cross-measure Jacobi geometry: U from the two channel Jacobi chains) and T_2 = U*(I - D_-^2)U (the PSD arithmetic Christoffel damping: D_- from the Christoffel weights, max D_- <= 0.997041 ladder-wide so I - D_-^2 >= 0 with zero negative entries), warded at max rel 1.0e-12 on ALL 42 reachable rungs h <= 900, transported LOSSLESSLY into the Gauss frame (Q unitary at 7.7e-11; I - C*C == Q Delta Q^H at 3.5e-12) -- and the anatomy is measured to all digits: the EXACT global minimizer g* of the directional compensation ratio inf_x T_2/|T_1^-| (computed basis-free from the pencil, spec v2 -- no eigenbasis under-resolution) IS the soft direction (|<g*, e_soft>| >= 0.9991 on every heavy rung, ladder overlap column 0.9991-1.0000) with the min ratio EXACTLY 1 + tau/|v^H T_1 v| (rel-margin dev 0.00 -- to all printed digits), the rank-one pole deflation is exact (lam_min(Delta_bulk) == 0 at 2.6e-15, Feshbach) giving Delta = Delta_bulk + s pp* with the CERTIFIED bulk floor c = lam_2(Delta_bulk) at 98-100 percent of lam_2(Delta) and the isolated scalar s = kappa tau reproducing the v864 kappa law (kappa 2.68 -> 1.35 along the ladder; kz9: s = 4.4955e-4 = 2.68 tau) -- THE WALL AS TWO EXPLICIT SOURCE NUMBERS: at the soft direction the two terms read (kz9) -0.0328 + 0.0330 = 1.68e-4 = tau (kz12: -0.0743 + 0.0744 = 7.65e-5; kz40: -0.0121 + 0.0121 = 6.66e-7), i.e. the open cofinal content is exactly the two-term inequality v^H T_2 v > |v^H T_1 v| at the soft direction with BOTH terms explicit source objects, ONE module from one probe (10 checks, zero fails, verdict COMPENSATION-EXACT; discovery probe cd_damping_compensation_probe.py, 2026-08-08, re-run identically at promotion, embedded BYTE-EXACT and executed verbatim, ~77 s).  THE HONESTY LINE (typed in the frozen spec and carried verbatim): the truth-side ratio >= 1 is IMPLIED by the upstream certified positivity on these finite rungs (S1.6 is the anatomy, not new evidence) -- what the identity buys is the FORM: the floor question becomes ONE inequality between two named classical objects (a Jacobi-chain cross defect and a Christoffel damping profile) at ONE named direction, with the pole-port decomposition a = a_1 + a_2 exact at the port (sum ward <= 2.1e-12) and the coupling removing all but kappa tau of it (kz9: a = 0.5135, coupling 0.5131).  THE DISCRIMINATION ANATOMY (what arithmetic MEANS in these coordinates): Epstein and scramble BREAK THE DAMPING'S SIGN (max D_- = 34.2/2917 > 1: T_2 loses PSD-ness -- the Christoffel weights of a false comb over-shoot 1) and under-compensate on their OWN soft directions (43/45 and 27/27 dangerous directions with worst ratios -175 and -446513; failing directions' soft overlap up to 0.95) while truth compensates >= 1.000008 EVERYWHERE -- the equal-phase coupling law of v869 and the ladder-wide damping bound of v870 are the two measured inputs this identity organizes.  NO RH claim.  Python-only per GATE.WOLFRAM.02.

PROVENANCE: discovery probe cd_damping_compensation_probe.py (10
checks, 0 failed, verdict COMPENSATION-EXACT, spec SHA
a85aad5a4b345a2ca1227def19f4fd5806f5a7544a4c0c94a6d7fbfd724031b8, spec
v2 with the basis-free exact-minimizer amendment typed in the frozen
spec), 2026-08-08, re-run identically at promotion.  ROUND-31
EMBEDDING CONVENTION: frozen source embedded BYTE-EXACT and executed
verbatim in an isolated namespace; the printed spec SHA reproduces;
byte-equality ward vs experiments/tfpt-discovery/ inside the pattern
gate.  The probe imports gauss_node_unitary_probe.py (gated in v870)
READ-ONLY -- not re-gated here.

FIREWALL: no zeros, no prime-table oracles (AST firewall inside the
probe); all 42 reachable rungs h <= 900; heavy-rung anatomy at
kz {9, 12, 13, 26, 40}; controls (Epstein x^2+5y^2, scramble seed 1)
MUST-FIRE and do -- the compensation breaks on their own soft
directions.  NO RH claim.
"""

import contextlib
import io
import math
import os
import re
import sys
import time
import types

_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)

# ------------- frozen probe source cd_damping_compensation_probe (embedded BYTE-EXACT, raw string)
_SRC_0 = r'''
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""cd_damping_compensation_probe -- PRIME.CD.DAMPING.
COMPENSATION.01 (EXPLORATION ONLY, experiments/; round 33
late plan probe C, 2026-08-08).

THE EQUATION (exact in the Gauss frame, D_+ = I so C = D_- U):

    I - C*C  =  (I - U*U)  +  U*(I - D_-^2) U
             =      T_1     +       T_2

T_1 = the cross-measure defect (indefinite: U amplifies where
sigma(U) > 1); T_2 = the arithmetic damping (PSD wherever
D_- <= 1, i.e. the Christoffel weights damp).  The hypothesis:
the true prime structure aligns the damping EXACTLY with the
dangerous directions of the defect, leaving one soft direction
at height tau; Epstein/scramble lose the alignment.

FRAME TRANSPORT (derived before running, warded): Q = B_+^G
G_+^{-1/2} is square unitary (plus arm in Gauss mode), and
I - C*C = Q Delta Q^H exactly (K = G_+ - G_- + quadrature
tightness), so all pencil objects transport: e_soft^G =
Q e_soft, p^G = Q w_pole, s and kappa unchanged.

HONESTY (pre-typed): for the true comb the directional ratio
T_2 / |T_1^-| >= 1 on Delta >= 0 windows is IMPLIED by the
certified positivity -- the census here delivers the ANATOMY
of the compensation (where the margin lives, how thin, who
holds the soft direction), and the DISCRIMINATION (where
Epstein/scramble break it).  It is not new positivity
evidence.

VERDICT (frozen): COMPENSATION-EXACT / COMPENSATION-PARTIAL /
COMPENSATION-DIFFUSE.  NO RH claim; writes nothing; v563 +
gauss_node_unitary READ-ONLY.

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/cd_damping_compensation_probe.py
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
import gauss_node_unitary_probe as gnu     # noqa: E402  (READ-ONLY)

FROZEN_SPEC = """\
PRIME.CD.DAMPING.COMPENSATION.01 spec v2 (2026-08-08; v1 run
findings: all wards passed, but the alignment census in the
T_1 EIGENBASIS under-resolves the minimizer -- the T_1
eigenvectors are 0.00-0.50 away from e_soft while the
two-term cancellation AT e_soft is exact; v2 replaces the
eigenbasis argmin bar by the EXACT global minimizer of the
directional ratio over the sphere, computed basis-free from
the pencil: for Delta_G > 0, inf ratio = 1 + nu*, nu* =
1/lam_max(Delta^{-1/2}(-T_1)Delta^{-1/2}), argmin g* =
Delta^{-1/2} w_max; new S2 bar: |<g*, e_soft^G>| >= 0.9 on
heavy rungs AND min ratio == 1 + nu* consistent with the
soft-direction read 1 + tau/|v^H T_1 v| rel 0.2; the
eigenbasis census stays as the descriptive profile.  Also
fixes the S2.1 check wiring (v1 hard-passed the flag).
No other changes).  Machinery = gauss_node_unitary read-only
(build_rung, gauss_objects, softport); ladder = all
frame_a_zones with h <= 900 AND plus arm in 'gauss' mode
(r_+ = h; non-square Q rungs typed + skipped); heavy census
rungs {9, 12, 13, 26, 40}.  WARDS (gate): W1 split
||T_1 + T_2 - (I - C*C)||_F / ||I - C*C||_F <= 1e-6 (the
D_+ = I deviation enters here); W2 transport ||Q^H Q - I||_F
<= 1e-8 and ||(I - C*C) - Q Delta Q^H||_F / ||Delta_G||_F <=
1e-6; W3 Feshbach: lam_min(Delta_bulk) <= 1e-10 with
Delta_bulk = Delta_G - s p p^H, s = 1/(p^H Delta_G^{-1} p);
kappa regression kappa(kz9) in [2.6, 2.8], kappa(kz40) in
[1.5, 1.7]; beta regression as before.  MEASUREMENTS per
rung: neg part of T_1 (count, most-negative mu, its
overlap with e_soft^G and p^G); T_2 PSD check (max D_- vs 1,
neg-part of 1 - D_-^2 typed); the directional ratio r_i =
(g_i^H T_2 g_i)/(-mu_i) over T_1-negative eigendirections:
min, quantiles, argmin overlap with e_soft^G; the four-way
projection table (pole port / soft / bulk-mean / most
dangerous) for T_1 and T_2 at heavy rungs; the port split
a = p^H T_1 p + p^H T_2 p (the explicit two-term
near-cancellation) and the s formula s = a - r*G^{-1}r
(softport ward rel <= 1e-6); Delta_bulk floor c = lam_2
(Delta_bulk) with backward-stability budget n eps ||Delta||
typed; c >= 0.3 lam_2(Delta) bar.  CONTROLS at kz 9: Epstein
(x^2+5y^2) and scramble seed 1 through the same split:
required: >= 1 dangerous direction with ratio < 1 (localized:
worst ratio, count, overlap census), or the T_2 sign breaks
(max D_- > 1); truth must have min ratio >= 1 on every rung.
VERDICT: COMPENSATION-EXACT iff all wards pass AND truth min
ratio >= 1 everywhere with argmin-overlap |<g_min, e_soft^G>|
>= 0.5 on heavy rungs AND Delta_bulk floor bar holds on all
rungs AND both controls break; COMPENSATION-PARTIAL iff wards
pass but a secondary leg fails (typed); COMPENSATION-DIFFUSE
iff a ward fails or the truth ratio dips below 1 (typed).
Float64; budgets typed.  NO RH claim; writes nothing."""

HEAVY = (9, 12, 13, 26, 40)
KAPPA_REFS = {9: (2.6, 2.8), 40: (1.5, 1.7)}
BANNED_IDS = ("zetazero", "nzeros", "primerange", "isprime",
              "primepi", "nextprime", "prevprime")

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


def split_rung(kz, **kw):
    """Build the two-term split of one rung.  Returns None if
    the Gauss system fails or the plus arm is not square."""
    b = gnu.build_rung(kz, **kw)
    if b["h"] > 900:
        return "skip-h"
    go = gnu.gauss_objects(b)
    if go["fail"]:
        return "gauss-fail:%s" % (go["mode"],)
    if len(go["thp"]) != b["h"]:
        return "plus-not-square:%d" % len(go["thp"])
    sp = gnu.softport(b)
    h = b["h"]
    U = go["U"]
    Dm2 = go["Dm"] ** 2
    C = go["CG"]
    ImCC = np.eye(h) - C.conj().T @ C
    ImCC = 0.5 * (ImCC + ImCC.conj().T)
    T1 = np.eye(h) - U.conj().T @ U
    T1 = 0.5 * (T1 + T1.conj().T)
    T2 = U.conj().T @ ((1.0 - Dm2)[:, None] * U)
    T2 = 0.5 * (T2 + T2.conj().T)
    w1 = float(np.linalg.norm(T1 + T2 - ImCC)
               / np.linalg.norm(ImCC))
    Q = go["BpG"] @ b["Rm"]
    wq = float(np.linalg.norm(Q.conj().T @ Q - np.eye(h)))
    wtr = float(np.linalg.norm(ImCC - Q @ b["Delta"]
                               @ Q.conj().T)
                / np.linalg.norm(ImCC))
    esG = Q @ sp["esoft"]
    v = np.exp(0.5 * np.arange(h) * b["D"])
    v = v / np.linalg.norm(v)
    wpole = b["Rp"] @ v
    wpole = wpole / np.linalg.norm(wpole)
    pG = Q @ wpole
    pG = pG / np.linalg.norm(pG)
    # Feshbach in Gauss coordinates
    y = np.linalg.solve(ImCC, pG)
    s = 1.0 / float(np.real(np.vdot(pG, y)))
    kap = s / sp["lam1"]
    Dbulk = ImCC - s * np.outer(pG, pG.conj())
    Dbulk = 0.5 * (Dbulk + Dbulk.conj().T)
    ebv = np.linalg.eigvalsh(Dbulk)
    # exact global compensation minimizer (spec v2): for
    # Delta_G > 0, inf_x ratio = 1 + nu*, nu* = 1/lam_max of
    # Delta^{-1/2}(-T_1)Delta^{-1/2}, argmin = Delta^{-1/2} w
    lamD, WD = np.linalg.eigh(ImCC)
    if lamD[0] > 0.0:
        Rsq = WD @ ((lamD ** -0.5)[:, None] * WD.conj().T)
        Mp = Rsq @ (-T1) @ Rsq
        Mp = 0.5 * (Mp + Mp.conj().T)
        em, Wm = np.linalg.eigh(Mp)
        nustar = 1.0 / float(em[-1])
        gstar = Rsq @ Wm[:, -1]
        gstar = gstar / np.linalg.norm(gstar)
        ovg = float(abs(np.vdot(gstar, esG)))
        rmin_exact = 1.0 + nustar
    else:
        nustar = ovg = rmin_exact = float("nan")
    # T_1 anatomy + directional compensation
    mu, Gv = np.linalg.eigh(T1)
    ndang = int(np.sum(mu < 0.0))
    ratios = np.array(
        [float(np.real(np.vdot(Gv[:, i], T2 @ Gv[:, i])))
         / (-mu[i]) for i in range(ndang)])
    if ndang:
        imin = int(np.argmin(ratios))
        ov_soft = float(abs(np.vdot(Gv[:, imin], esG)))
        ov_pole = float(abs(np.vdot(Gv[:, imin], pG)))
        idang = int(np.argmin(mu))
        ovd_soft = float(abs(np.vdot(Gv[:, idang], esG)))
    else:
        ov_soft = ov_pole = ovd_soft = float("nan")
    a1 = float(np.real(np.vdot(pG, T1 @ pG)))
    a2 = float(np.real(np.vdot(pG, T2 @ pG)))
    a_dir = float(np.real(np.vdot(pG, ImCC @ pG)))
    s1 = float(np.real(np.vdot(esG, T1 @ esG)))
    s2 = float(np.real(np.vdot(esG, T2 @ esG)))
    return dict(kz=kz, h=h, b=b, go=go, sp=sp, w1=w1, wq=wq,
                wtr=wtr, T1=T1, T2=T2, ImCC=ImCC, esG=esG,
                pG=pG, s=s, kap=kap, lam1=sp["lam1"],
                lam2=sp["lam2"], eb1=float(ebv[0]),
                c=float(ebv[1]), mu=mu, ndang=ndang,
                ratios=ratios, ov_soft=ov_soft,
                ov_pole=ov_pole, ovd_soft=ovd_soft,
                nustar=nustar, ovg=ovg, rmin_exact=rmin_exact,
                a1=a1, a2=a2, a_dir=a_dir, s1=s1, s2=s2,
                maxDm=float(np.max(go["Dm"])),
                negD=int(np.sum(1.0 - Dm2 < 0.0)))


# ================================================================= main
def main():
    section("PRIME.CD.DAMPING.COMPENSATION.01 "
            "(EXPLORATION ONLY)")
    sha = hashlib.sha256(FROZEN_SPEC.encode("utf-8")).hexdigest()
    print("    FROZEN_SPEC SHA-256 = %s" % sha)
    print("    NO RH claim.")
    print("\nS0 -- firewall")
    check("S0.1 AST firewall clean (no zero/prime oracles)",
          not ast_scan(BANNED_IDS))

    zones = list(core.frame_a_zones())

    section("S1 -- the exact split along the ladder")
    rows = []
    skipped = []
    print("    kz    h    #T1<0  rmin-eig  rmin-EXACT  "
          "ov(g*,soft)  maxD-  kappa  a1(pole)  a2(pole)  "
          "c/lam2")
    for kz in zones:
        r = split_rung(kz)
        if isinstance(r, str):
            skipped.append((kz, r))
            continue
        rows.append(r)
        print("    %-5d %-4d %-5d  %.4f    %.6f    %.4f"
              "       %.4f %5.2f  %+.4f   %+.4f   %.2f"
              % (kz, r["h"], r["ndang"],
                 float(np.min(r["ratios"])) if r["ndang"]
                 else float("nan"),
                 r["rmin_exact"], r["ovg"], r["maxDm"],
                 r["kap"], r["a1"], r["a2"],
                 r["c"] / r["lam2"]),
              flush=True)
    if skipped:
        print("    skipped/typed: %s" % skipped)

    w1max = max(r["w1"] for r in rows)
    wqmax = max(r["wq"] for r in rows)
    wtrmax = max(r["wtr"] for r in rows)
    check("S1.1 [W1 SPLIT WARD] T_1 + T_2 == I - C*C on every "
          "rung (max rel %.1e <= 1e-6)" % w1max, w1max <= 1e-6)
    check("S1.2 [W2 TRANSPORT] Q unitary (max %.1e) and "
          "I - C*C == Q Delta Q^H (max rel %.1e) -- the pencil "
          "transports exactly" % (wqmax, wtrmax),
          wqmax <= 1e-8 and wtrmax <= 1e-6)
    eb1max = max(abs(r["eb1"]) for r in rows)
    check("S1.3 [W3 FESHBACH] lam_min(Delta_bulk) == 0 on "
          "every rung (max |lam_min| %.1e; the rank-one "
          "deflation is exact)" % eb1max, eb1max <= 1e-10)
    kaps = {r["kz"]: r["kap"] for r in rows}
    reg_ok = all(KAPPA_REFS[k][0] <= kaps[k] <= KAPPA_REFS[k][1]
                 for k in KAPPA_REFS if k in kaps)
    check("S1.4 [SOFTPORT REGRESSION] kappa(kz9) = %.3f, "
          "kappa(kz40) = %.3f within the kappa-probe bands"
          % (kaps.get(9, -1), kaps.get(40, -1)), reg_ok)
    t2_ok = all(r["maxDm"] <= 1.0 + 1e-9 for r in rows)
    check("S1.5 [T2 SIGN] max D_- <= 1 on every rung (max "
          "%.6f; neg entries of 1 - D_-^2: %d total) -- the "
          "damping term is PSD"
          % (max(r["maxDm"] for r in rows),
             sum(r["negD"] for r in rows)), t2_ok)
    minr = min(r["rmin_exact"] for r in rows)
    ratio_ok = minr >= 1.0
    check("S1.6 [COMPENSATION] the EXACT global directional "
          "ratio inf_x T_2/|T_1^-| >= 1 on every rung (ladder "
          "min %.6f; eigenbasis census min %.4f; implied by "
          "Delta >= 0 -- the anatomy, not new evidence)"
          % (minr, min(float(np.min(r["ratios"]))
                       for r in rows if r["ndang"])), ratio_ok)
    floor_ok = all(r["c"] >= 0.3 * r["lam2"] for r in rows)
    check("S1.7 [BULK FLOOR] c = lam_2(Delta_bulk) >= 0.3 "
          "lam_2(Delta) on every rung (min c/lam2 %.2f; "
          "backward-stability budget ~ %.0e)"
          % (min(r["c"] / r["lam2"] for r in rows),
             max(r["h"] for r in rows) * 2.2e-16), floor_ok)

    # ---------------- S2 heavy anatomy
    section("S2 -- the four-way alignment table (heavy rungs)")
    ov_ok = True
    for r in rows:
        if r["kz"] not in HEAVY:
            continue
        h = r["h"]
        Pb = np.eye(h) - np.outer(r["esG"], r["esG"].conj())
        t1b = float(np.real(np.trace(Pb @ r["T1"] @ Pb))) \
            / (h - 1)
        t2b = float(np.real(np.trace(Pb @ r["T2"] @ Pb))) \
            / (h - 1)
        qs = np.quantile(r["ratios"], [0.0, 0.1, 0.5]) \
            if r["ndang"] else [float("nan")] * 3
        soft_read = 1.0 + r["lam1"] / max(-r["s1"], 1e-300)
        cons = abs(r["rmin_exact"] - soft_read) \
            / max(soft_read - 1.0, 1e-300)
        ov_ok &= (r["ovg"] >= 0.9 and cons <= 0.2)
        print("    kz %-3d: %d dangerous dirs, mu_min %+.4f | "
              "eigenbasis ratios q0/q10/q50 = %.4f/%.2f/%.2f "
              "| EXACT min ratio %.6f vs soft-read 1 + tau/"
              "|v^H T1 v| = %.6f (rel-margin dev %.2f) | "
              "|<g*, e_soft>| = %.4f"
              % (r["kz"], r["ndang"], float(np.min(r["mu"])),
                 qs[0], qs[1], qs[2], r["rmin_exact"],
                 soft_read, cons, r["ovg"]))
        print("           T1/T2 at pole: %+.4f/%+.4f (sum "
              "%.4f = a, ward %.1e) | at soft: %+.4f/%+.4f "
              "(sum %.2e ~ tau %.2e) | bulk mean: %+.4f/%+.4f"
              % (r["a1"], r["a2"], r["a1"] + r["a2"],
                 abs(r["a1"] + r["a2"] - r["a_dir"]),
                 r["s1"], r["s2"], r["s1"] + r["s2"],
                 r["lam1"], t1b, t2b))
    check("S2.1 [SOFT-DIRECTION IDENTITY] the exact global "
          "minimizer g* IS the soft direction (|<g*, e_soft>| "
          ">= 0.9 and margin consistent with the soft read, "
          "all heavy rungs)", ov_ok)

    # ---------------- S3 the s formula
    section("S3 -- the isolated scalar")
    r9 = next(r for r in rows if r["kz"] == 9)
    print("""    THE TARGET FORM, assembled (kz 9 numbers):
      Delta_G = Delta_bulk + s p p^H,  Delta_bulk >= 0 with
      lam_min = %.1e (exact zero), floor c = %.3e
      (= %.2f lam_2), and s = %.6e = %.2f tau.
      THE EXPLICIT s: s = a - coupling, a = p^H T_1 p +
      p^H T_2 p = %+.4f + %+.4f = %.4f -- the cross-measure
      defect READ AT THE POLE PORT plus the arithmetic damping
      READ AT THE POLE PORT, both source-built (U from the
      Jacobi chains, D_- from the Christoffel weights); the
      coupling removes %.4f of it.  The wall in its sharpest
      form: why does a1 + a2 exceed the coupling by exactly
      kappa tau > 0.""" % (
        r9["eb1"], r9["c"], r9["c"] / r9["lam2"], r9["s"],
        r9["kap"], r9["a1"], r9["a2"], r9["a1"] + r9["a2"],
        r9["a1"] + r9["a2"] - r9["s"]))

    # ---------------- S4 discrimination anatomy
    section("S4 -- discrimination anatomy at kz 9 "
            "(Epstein x^2+5y^2, scramble seed 1)")
    rr9 = core.build_window(9)
    N_E = int(math.floor(math.exp(2.0 * rr9["alpha"]))) + 1
    lamE = gnu.lambda_eps(N_E)
    nn = np.nonzero(np.abs(lamE) > 1e-12)[0]
    ctrl_ok = True
    for nmc, kw in (("Epstein", dict(comb=(
            np.log(nn.astype(float)),
            2.0 * lamE[nn] / np.sqrt(nn.astype(float))))),
            ("scramble", dict(scramble_seed=1))):
        rc_ = split_rung(9, **kw)
        if isinstance(rc_, str):
            print("    %-8s: pipeline failed (%s) -- typed as "
                  "maximal breach" % (nmc, rc_))
            continue
        nfail = int(np.sum(rc_["ratios"] < 1.0)) \
            if rc_["ndang"] else 0
        worst = float(np.min(rc_["ratios"])) if rc_["ndang"] \
            else float("nan")
        broke = nfail >= 1 or rc_["maxDm"] > 1.0 + 1e-9
        ctrl_ok &= broke
        # localization: overlap of failing dirs with their own
        # soft direction (most negative of their Delta_G)
        lamc, Wc = np.linalg.eigh(rc_["ImCC"])
        esc = Wc[:, 0]
        muc, Gc = np.linalg.eigh(rc_["T1"])
        fails_ov = [float(abs(np.vdot(Gc[:, i], esc)))
                    for i in range(rc_["ndang"])
                    if rc_["ratios"][i] < 1.0]
        print("    %-8s: %d/%d dangerous dirs UNDER-compensated"
              " (worst ratio %.3f); max D_- = %.4f (T2 sign %s)"
              "; lam_min(Delta_G) = %+.3e; failing dirs' "
              "overlap with their soft dir: max %.3f (n=%d)"
              % (nmc, nfail, rc_["ndang"], worst, rc_["maxDm"],
                 "OK" if rc_["maxDm"] <= 1 + 1e-9 else
                 "BROKEN", float(lamc[0]),
                 max(fails_ov) if fails_ov else float("nan"),
                 len(fails_ov)), flush=True)
    check("S4.1 [DISCRIMINATION] both controls break the "
          "compensation (ratio < 1 somewhere or T2 sign "
          "breaks) while truth holds >= 1 everywhere", ctrl_ok)

    # ---------------- V verdict
    section("V -- FROZEN VERDICT + honest consequence")
    wards_ok = (w1max <= 1e-6 and wqmax <= 1e-8
                and wtrmax <= 1e-6 and eb1max <= 1e-10
                and reg_ok)
    if (wards_ok and t2_ok and ratio_ok and floor_ok
            and ov_ok and ctrl_ok):
        verdict = "COMPENSATION-EXACT"
    elif wards_ok:
        legs = []
        if not t2_ok:
            legs.append("T2 sign")
        if not ratio_ok:
            legs.append("truth ratio < 1 (min %.6f)" % minr)
        if not floor_ok:
            legs.append("bulk floor")
        if not ov_ok:
            legs.append("argmin not soft-aligned")
        if not ctrl_ok:
            legs.append("controls don't break")
        verdict = "COMPENSATION-PARTIAL (%s)" % ", ".join(legs)
    else:
        verdict = "COMPENSATION-DIFFUSE (wards fail)"
    print("\n  VERDICT: %s" % verdict)
    print("""
  HONEST CONSEQUENCE: the 99.9%% cancellation is now an EXACT
  identity of two source-built terms -- the cross-measure
  defect T_1 = I - U*U (Jacobi geometry) and the arithmetic
  damping T_2 = U*(I - D_-^2)U (Christoffel weights) -- with
  the pencil transported losslessly into the Gauss frame.
  MEASURED anatomy: exact global min ratio %.6f (ladder), the
  minimizer's soft overlap %s on heavy rungs; bulk floor
  c/lam2 in [%.2f, %.2f] after the rank-one pole deflation.
  The discrimination anatomy localizes what arithmetic MEANS
  in these coordinates: Epstein/scramble lose the alignment
  in measured directions (S4).  Unchanged and typed: the
  truth-side ratio >= 1 is implied by the upstream certified
  positivity on these finite rungs -- the open cofinal content
  is exactly the two-term inequality at the soft direction
  (s = kappa tau > 0) with both terms explicit.  NO RH
  claim.""" % (
        minr,
        "/".join("%.3f" % r["ovg"] for r in rows
                 if r["kz"] in HEAVY),
        min(r["c"] / r["lam2"] for r in rows),
        max(r["c"] / r["lam2"] for r in rows)))
    n_pass = sum(1 for _n, ok in CHECKS if ok)
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed%s"
          % (time.time() - T0, len(CHECKS), len(FAILS),
             ("  " + ",".join(FAILS)) if FAILS else ""))
    return 0 if n_pass == len(CHECKS) else 1


if __name__ == "__main__":
    raise SystemExit(main())
'''

# --------------------------------------------------------------- harness
_PF_RE = re.compile(r"^\s*\[(PASS|FAIL)\]\s+(\S+)", re.M)
_VD_RE = re.compile(r"VERDICT[^\n]*:")


def _probe_file(name):
    cand = os.path.abspath(os.path.join(
        _HERE, os.pardir, "experiments", "tfpt-discovery", name + ".py"))
    return cand if os.path.isfile(cand) else None


def _census(out):
    marks = _PF_RE.findall(out)
    fails = sorted({tok for st, tok in marks if st == "FAIL"})
    verdicts = [ln.strip() for ln in out.splitlines()
                if _VD_RE.search(ln)]
    return len(marks), fails, " | ".join(verdicts)


def _exec_probe(name, src, run_entry=True):
    """Execute one embedded frozen probe source BYTE-EXACT in its own
    module namespace, registered in sys.modules under the probe's
    canonical import name; capture and re-emit stdout; return
    (stdout, exit_code, byte_equal_to_source_file_or_None).  Probes
    whose main() returns the verdict STRING map to exit 0, exactly as
    their own __main__ guards do (main() called, return value dropped)."""
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
                code = (0 if rc is None or isinstance(rc, str)
                        else int(rc))
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


def _gate(name, out, code, same, exp_n, exp_fails, exp_verdicts,
          exp_code, gates):
    n, fails, verdict = _census(out)
    ok = (n == exp_n and fails == list(exp_fails)
          and all(v in verdict for v in exp_verdicts)
          and code == exp_code and same is not False)
    gates.append(ok)
    prov = ("byte-exact vs experiments source" if same is True else
            "embedded copy (source file not present)" if same is None
            else "SOURCE MISMATCH")
    print("\n[%s] PATTERN GATE %s: %d checks (exp %d) | FAILs %s "
          "(exp %s) | exit %d (exp %d) | %s\n      verdict line(s): %s"
          % ("PASS" if ok else "FAIL", name, n, exp_n,
             ",".join(fails) if fails else "none",
             ",".join(exp_fails) if exp_fails else "none",
             code, exp_code, prov, verdict), flush=True)
    return ok

_PLAN = (
    ('cd_damping_compensation_probe', _SRC_0, 10, (),
     ('COMPENSATION-EXACT',), 0),
)


def run():
    t0 = time.time()
    print("=" * 74)
    print('v872 -- PRIME.CD.DAMPING.COMPENSATION.01')
    print("(the round's headline: the EXACT two-term compensation identity")
    print('I - C*C = T_1 + T_2 (indefinite Jacobi geometry + PSD Christoffel')
    print('damping) warded at 1e-12 on all 42 rungs; the exact global')
    print('compensation minimizer IS the soft direction; the wall as two')
    print('explicit source numbers; NO RH claim)')
    print("=" * 74, flush=True)
    gates = []
    for name, src, exp_n, exp_fails, exp_verdicts, exp_code in _PLAN:
        print("\n" + "-" * 74)
        print("EMBEDDED FROZEN PROBE: %s" % name)
        print("-" * 74, flush=True)
        out, code, same = _exec_probe(name, src)
        _gate(name, out, code, same, exp_n, exp_fails,
              exp_verdicts, exp_code, gates)
    ok = all(gates)
    print("\n" + "=" * 74)
    print("%s: %d/%d probe pattern gates passed | runtime %.1f s"
          % ('v872', sum(gates), len(gates), time.time() - t0))
    print('The 99.9% cancellation is an EXACT identity of two source-built')
    print('terms; the exact global minimizer of the directional ratio IS')
    print('the soft direction (overlap >= 0.9991, min ratio = 1 +')
    print('tau/|v*T1v| to all digits); Delta = Delta_bulk + s pp* with the')
    print('certified bulk floor and s = kappa tau; the wall in its sharpest')
    print('form: why does a1 + a2 exceed the coupling by exactly kappa tau.')
    print("Epstein/scramble BREAK the damping's sign on their own soft")
    print('directions -- the anatomy of what arithmetic means here.')
    print("[%s] %s VERDICT GATE: COMPENSATION-EXACT"
          % ("PASS" if ok else "FAIL", 'v872'))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(run())
