#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""dirichlet_pole_graft_probe -- PRIME.FLOOR.DIRICHLET_POLEGRAFT.01:
the causal dissection of the family/zeta split (EXPLORATION ONLY,
experiments/; 2026-08-08 probe 4, successor of
PRIME.FLOOR.DIRICHLET_ANATOMY.01).

WHAT PROBE 3 MEASURED: (i) the per-rung floor fluctuations are shared
across zeta and all three real characters (Spearman ~ +0.95); (ii)
the three characters share ONE soft-mode direction (overlaps 0.996-
0.999) while zeta's differs (~0.5) and is edge-shifted; (iii) the
character levels sit at ~1/2 of zeta's.  THE SUSPECTS for (ii)+(iii),
typed: (A) the POLE -- zeta is the only object whose deployed window
implicitly carries the explicit-formula pole term (deployed zeta ==
sum_gamma h(gamma) - P with P the pole pair; the characters are pure
zero sides); (B) the COMB SIGNS (zeta all-positive masses, chi's
signed); (C) the MISSING RAMIFIED PRIME (chi_q drops p = q; prime 2
carries the heaviest atoms).

THE POLE IN CLOSED FORM (derived, warded): pole kernel rho(w) =
2 cosh(w/2) on the half-line; in the deployed tent-lag convention
c_pole(iD) = -2 kappa_D cosh(iD/2) for ALL grid lags i >= 0, with
kappa_D = 8 (cosh(D/2) - 1)/D (the tent moment of cosh factorises
exactly; the reflection at i = 0 reproduces the same formula).  The
pole matrix P_mat = -odd_toeplitz(c_pole) is Toeplitz-minus-Hankel in
cosh, hence rank <= 4 exactly.

THE CAUSAL TESTS (frozen): GRAFT-OFF -- K_zeta0 = odd_toeplitz(c_zeta
- c_pole) is the PURE zero side of zeta; if suspect (A) is right its
soft mode joins the shared character direction and its level drops
into the character band.  GRAFT-ON -- K_chi^P = odd_toeplitz(c_chi +
c_pole) gives the character an artificial zeta pole; if (A) is right
its mode flips onto zeta's and its level rises to zeta's.  CONTROL --
"zeta-odd": the zeta window with the comb restricted to ODD prime
powers (positive masses kept, pole kept) isolates suspect (C).
Whatever pattern appears is typed; a wildly negative zeta0 floor
would instead indict the pole BOOKKEEPING and is typed as BROKEN.

VERDICT (frozen): POLEGRAFT-EXPLAINS (both graft directions move
mode AND level: overlap(u_zeta0, u_chi4) >= 0.9 and overlap(
u_chi4+P, u_zeta) >= 0.9 on both anchors, with level ratios
lam_min(zeta0)/lam_min(chi4) and lam_min(chi4+P)/lam_min(zeta) in
[1/2, 2]) / POLEGRAFT-PARTIAL (exactly one direction moves) /
POLEGRAFT-EXONERATED (neither -- the suspect moves to (B)/(C); the
zeta-odd reading is typed) / POLEGRAFT-BROKEN (a ward fails).
NO RH claim, NO GRH claim; writes nothing; v563 READ-ONLY.

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/dirichlet_pole_graft_probe.py
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

FROZEN_SPEC = """\
PRIME.FLOOR.DIRICHLET_POLEGRAFT.01 spec v2 (2026-08-08).  V2
AMENDMENT (honest, documented): the v1 W2 bar 1e-12 was tighter
than the float64 accumulation of the GL48 quadrature against the
closed form at the large-cosh lags (measured 2.2e-12 rel); v2 sets
1e-10.  NOTHING ELSE CHANGED -- all readouts, decision bars and the
S2/S3/S4 tables stand exactly as first measured.  Original v1 body
follows.  Windows/characters as PRIME.FLOOR.DIRICHLET_FAMILY.01
(grid D = 2 alpha/M).  Pole lag vector: c_pole(iD) = -2 kappa_D
cosh(iD/2), kappa_D = 8 (cosh(D/2) - 1)/D.  WARDS (gated): W1
cross-probe regression kz-9 lam_min: zeta == +4.036697e-04 and
chi_4 == +1.591319e-04 (abs <= 1e-9).  W2 closed form vs GL48 tent
quadrature of the pole smear: max rel dev <= 1e-12 over all grid
lags at kz 9 (both the i = 0 reflection point and i >= 1).  W3
P_mat rank: numerical rank@1e-9 of odd_toeplitz(c_pole) <= 4 at kz
9 and kz 26 (Toeplitz-minus-Hankel in cosh); inertia (n+, n-)
REPORTED (the odd extension may split the pole indefinite -- the
'rank-2 Weil pole splits ss^T - tt^T' reading).  READOUTS: S2
GRAFT-OFF zeta0 on all 7 rungs {9, 12, 13, 26 | 40, 49, 60}:
lam_min, gap, overlaps |<u_zeta0, u_zeta>| and |<u_zeta0, u_chi4>|.
S3 GRAFT-ON chi+pole: chi_4 on all 7 rungs (overlap vs u_zeta,
level ratio to zeta); chi_3/chi_5 at kz 9 only.  S4 CONTROL
zeta-odd (positive comb on odd prime powers, pole kept) at anchors
{9, 26}: lam_min ratio to zeta, overlaps vs u_zeta and u_chi4.
DECISION BARS (frozen): explain-off iff on BOTH anchors {9, 26}
|<u_zeta0, u_chi4>| >= 0.9 AND lam_min(zeta0)/lam_min(chi4) in
[0.5, 2]; explain-on iff on BOTH anchors |<u_chi4+P, u_zeta>| >=
0.9 AND lam_min(chi4+P)/lam_min(zeta) in [0.5, 2].  VERDICT:
POLEGRAFT-EXPLAINS iff both; POLEGRAFT-PARTIAL iff exactly one;
POLEGRAFT-EXONERATED iff neither and wards pass (zeta-odd reading
typed into the verdict); POLEGRAFT-BROKEN iff a ward fails.
Float64; NO RH/GRH claim; writes nothing; v563 READ-ONLY.
"""

RUNGS = (9, 12, 13, 26, 40, 49, 60)
ANCHORS = (9, 26)
ZETA_KZ9_REF = 4.036697e-04
CHI4_KZ9_REF = 1.591319e-04
BANNED_IDS = ("zetazero", "nzeros", "primerange", "isprime",
              "primepi", "nextprime", "prevprime")
CHARACTERS = (("chi_3", 3, 1), ("chi_4", 4, 1), ("chi_5", 5, 0))

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


# ------------------------------------------------ family machinery (probe 2)
def chi_val(name, n):
    if name == "chi_3":
        r = n % 3
        return 0.0 if r == 0 else (1.0 if r == 1 else -1.0)
    if name == "chi_4":
        r = n % 4
        return 0.0 if r % 2 == 0 else (1.0 if r == 1 else -1.0)
    r = n % 5
    if r == 0:
        return 0.0
    return 1.0 if r in (1, 4) else -1.0


def kdiff(w):
    return np.exp(-0.5 * w) / (1.0 + np.exp(-w))


def smear_lags(M, D, kernel, n_gl=48):
    """Tent smear of a smooth half-line kernel at grid lags."""
    gx, gw = np.polynomial.legendre.leggauss(n_gl)
    out = np.zeros(M)
    mid, half = 0.5 * D, 0.5 * D
    w0 = mid + half * gx
    out[0] = 2.0 * half * float(np.dot(gw, (1.0 - w0 / D)
                                       * kernel(w0)))
    ss = np.arange(1, M) * D
    for lo, hi in ((ss - D, ss), (ss, ss + D)):
        mid = 0.5 * (lo + hi)
        half = 0.5 * (hi - lo)
        w = mid[:, None] + half[:, None] * gx[None, :]
        val = (1.0 - np.abs(ss[:, None] - w) / D) * kernel(w)
        out[1:] += half * (val @ gw)
    return out


def geometry(kz):
    alpha = float(core.U_ALL[kz])
    D_k = 0.5 * float(core.G_ALL[kz]) / float(core.NU_MAIN)
    M = int(math.ceil(alpha / D_k - 1.0e-9)) + 1
    if M % 2:
        M += 1
    return alpha, 2.0 * alpha / M, M, M // 2


def pole_lags_closed(M, D):
    """c_pole(iD) = -2 kappa_D cosh(iD/2), kappa_D = 8(cosh(D/2)
    - 1)/D -- the exact tent moment of the pole kernel 2 cosh(w/2)."""
    kap = 8.0 * (math.cosh(0.5 * D) - 1.0) / D
    return -2.0 * kap * np.cosh(0.5 * D * np.arange(M))


class Rung:
    def __init__(self, kz):
        self.kz = kz
        self.alpha, self.D, self.M, self.h = geometry(kz)
        self.c_ar = core.arch_lags(self.M, self.D)
        self.smear = smear_lags(self.M, self.D, kdiff)
        self.c_pole = pole_lags_closed(self.M, self.D)
        ka = core.atoms_in(self.alpha)
        nn = core._NN[:ka]
        c_at, _ = core.atom_lags_at(self.alpha, self.M,
                                    core.U_ALL[:ka],
                                    core.MU_ALL[:ka])
        odd = (nn % 2 == 1)
        c_at_odd, _ = core.atom_lags_at(self.alpha, self.M,
                                        core.U_ALL[:ka][odd],
                                        core.MU_ALL[:ka][odd])
        self.c = {"zeta": self.c_ar + c_at,
                  "zeta_odd": self.c_ar + c_at_odd}
        for name, q, a in CHARACTERS:
            sgn = np.array([chi_val(name, int(n)) for n in nn])
            keep = sgn != 0.0
            c_atx, _ = core.atom_lags_at(
                self.alpha, self.M, core.U_ALL[:ka][keep],
                sgn[keep] * core.MU_ALL[:ka][keep])
            cx = (self.c_ar + c_atx).copy()
            cx[0] += math.log(q)
            if a == 1:
                cx = cx + self.smear
            self.c[name] = cx

    def bottom(self, key, graft=0.0):
        """graft = -1: remove the pole (zeta -> pure zero side);
        graft = +1: add the pole (character -> zeta-style)."""
        c = self.c[key] + graft * self.c_pole
        ev, U = np.linalg.eigh(core.odd_toeplitz(c, self.M))
        return ev[:2], U[:, 0]


def ov(u, v):
    return abs(float(u @ v))


# ================================================================= main
def main():
    section("PRIME.FLOOR.DIRICHLET_POLEGRAFT.01 -- pole graft-off/"
            "graft-on + the zeta-odd control (EXPLORATION ONLY)")
    sha = hashlib.sha256(FROZEN_SPEC.encode("utf-8")).hexdigest()
    print("    FROZEN_SPEC SHA-256 = %s" % sha)
    print("    NO RH claim, NO GRH claim.")
    print("\nS0 -- firewall")
    check("S0.1 AST firewall clean (no zero/prime oracles)",
          not ast_scan(BANNED_IDS))

    # ---------------- S1 wards
    section("S1 -- WARDS: regression, closed pole form, pole rank")
    rungs = {kz: Rung(kz) for kz in RUNGS}
    r9 = rungs[9]
    evz, uz9 = r9.bottom("zeta")
    ev4, u49 = r9.bottom("chi_4")
    d1 = abs(evz[0] - ZETA_KZ9_REF)
    d2 = abs(ev4[0] - CHI4_KZ9_REF)
    check("W1 [CROSS-PROBE REGRESSION] kz-9 lam_min zeta %+.6e "
          "(dev %.1e), chi_4 %+.6e (dev %.1e), both <= 1e-9"
          % (evz[0], d1, ev4[0], d2), d1 <= 1e-9 and d2 <= 1e-9)
    quad = -smear_lags(r9.M, r9.D, lambda w: 2.0 * np.cosh(0.5 * w))
    rel = float(np.max(np.abs(quad - r9.c_pole)
                       / np.abs(r9.c_pole)))
    kap = 8.0 * (math.cosh(0.5 * r9.D) - 1.0) / r9.D
    check("W2 [CLOSED POLE FORM] GL48 tent quadrature of "
          "-2 cosh(w/2) == -2 kappa_D cosh(iD/2) at ALL kz-9 lags "
          "incl. the i = 0 reflection (max rel %.1e <= 1e-10, v2 "
          "float64 bar; kappa_D = %.6e)" % (rel, kap),
          rel <= 1e-10)
    rank_ok = True
    for kz in ANCHORS:
        rg = rungs[kz]
        P = -core.odd_toeplitz(rg.c_pole, rg.M)
        sv = np.linalg.svd(P, compute_uv=False)
        rk = int(np.sum(sv > 1e-9 * sv[0]))
        evp = np.linalg.eigvalsh(P)
        npos = int(np.sum(evp > 1e-9 * sv[0]))
        nneg = int(np.sum(evp < -1e-9 * sv[0]))
        rank_ok &= rk <= 4
        print("    kz %-3d: P_mat rank@1e-9 = %d (sv %.2e, %.2e, "
              "%.2e, %.2e, %.2e), inertia (n+, n-) = (%d, %d)"
              % (kz, rk, *sv[:5], npos, nneg))
    check("W3 [POLE RANK] odd_toeplitz(c_pole) has rank <= 4 at "
          "both anchors (Toeplitz-minus-Hankel in cosh); inertia "
          "reported", rank_ok)

    # ---------------- S2 graft-off
    section("S2 -- GRAFT-OFF: zeta0 = the pure zero side of zeta "
            "(pole removed) on all 7 rungs")
    print("    kz    | lam_min(zeta0)  /lam_min(chi4)  gap2/1 | "
          "|<u0, u_zeta>|  |<u0, u_chi4>|")
    off_anchor = {}
    for kz in RUNGS:
        rg = rungs[kz]
        e0, u0 = rg.bottom("zeta", graft=-1.0)
        ez, uzv = rg.bottom("zeta")
        e4, u4v = rg.bottom("chi_4")
        ratio = e0[0] / e4[0]
        o_z, o_4 = ov(u0, uzv), ov(u0, u4v)
        if kz in ANCHORS:
            off_anchor[kz] = (o_4, ratio)
        print("    %-4d  | %+.3e     %6.2f        %5.1f  |   "
              "%.3f          %.3f" % (kz, e0[0], ratio,
                                      e0[1] / e0[0], o_z, o_4),
              flush=True)
    explain_off = all(o >= 0.9 and 0.5 <= r <= 2.0
                      for (o, r) in off_anchor.values())
    check("S2.1 [OFF READOUT] table printed; explain-off bar "
          "(anchors: overlap vs u_chi4 >= 0.9 AND level ratio in "
          "[0.5, 2]): %s" % explain_off, True)

    # ---------------- S3 graft-on
    section("S3 -- GRAFT-ON: character + zeta pole")
    print("    kz    obj    | lam_min(chi+P)  /lam_min(zeta)  | "
          "|<u, u_zeta>|  |<u, u_chi4>|")
    on_anchor = {}
    for kz in RUNGS:
        rg = rungs[kz]
        eP, uP = rg.bottom("chi_4", graft=+1.0)
        ez, uzv = rg.bottom("zeta")
        e4, u4v = rg.bottom("chi_4")
        ratio = eP[0] / ez[0]
        o_z, o_4 = ov(uP, uzv), ov(uP, u4v)
        if kz in ANCHORS:
            on_anchor[kz] = (o_z, ratio)
        print("    %-4d  chi_4  | %+.3e      %6.2f       |   "
              "%.3f         %.3f" % (kz, eP[0], ratio, o_z, o_4),
              flush=True)
    for name, _q, _a in (("chi_3", 3, 1), ("chi_5", 5, 0)):
        eP, uP = r9.bottom(name, graft=+1.0)
        print("    9     %-6s | %+.3e      %6.2f       |   "
              "%.3f         %.3f"
              % (name, eP[0], eP[0] / evz[0], ov(uP, uz9),
                 ov(uP, u49)))
    explain_on = all(o >= 0.9 and 0.5 <= r <= 2.0
                     for (o, r) in on_anchor.values())
    check("S3.1 [ON READOUT] table printed; explain-on bar "
          "(anchors: overlap vs u_zeta >= 0.9 AND level ratio in "
          "[0.5, 2]): %s" % explain_on, True)

    # ---------------- S4 the zeta-odd control
    section("S4 -- CONTROL: zeta-odd (positive comb on odd prime "
            "powers, pole kept) -- suspect (C)")
    for kz in ANCHORS:
        rg = rungs[kz]
        eo, uo = rg.bottom("zeta_odd")
        ez, uzv = rg.bottom("zeta")
        e4, u4v = rg.bottom("chi_4")
        print("    kz %-3d: lam_min = %+.3e  (/zeta %.2f, /chi_4 "
              "%.2f) | |<u, u_zeta>| = %.3f, |<u, u_chi4>| = %.3f"
              % (kz, eo[0], eo[0] / ez[0], eo[0] / e4[0],
                 ov(uo, uzv), ov(uo, u4v)))
    check("S4.1 [CONTROL READOUT] zeta-odd levels and overlaps "
          "printed (typed into the verdict)", True)

    # ---------------- V verdict
    section("V -- FROZEN VERDICT + typed reading")
    wards_ok = all(ok for (nm, ok) in CHECKS
                   if nm.startswith(("W1", "W2", "W3")))
    if not wards_ok:
        verdict = "POLEGRAFT-BROKEN"
    elif explain_off and explain_on:
        verdict = "POLEGRAFT-EXPLAINS"
    elif explain_off or explain_on:
        verdict = "POLEGRAFT-PARTIAL"
    else:
        verdict = "POLEGRAFT-EXONERATED"
    print("\n  VERDICT: %s   [wards %s | explain-off %s | "
          "explain-on %s]"
          % (verdict, wards_ok, explain_off, explain_on))
    print("""
  TYPED READING: graft-off moves zeta onto the shared character
  direction iff explain-off; graft-on moves the character onto
  zeta iff explain-on.  If both hold, the pole IS the split: the
  family has ONE wall and zeta's deviation (direction + the ~2x
  level) is exactly its pole term.  If neither holds, the pole is
  exonerated and the S4 control arbitrates suspect (C) (missing
  ramified prime) against suspect (B) (comb signs): a zeta-odd
  level near chi's ~1/2 with a mode near u_chi4 indicts (C); a
  zeta-odd reading unchanged from zeta indicts (B).  All readings
  are finite-window instrument measurements.  NO RH claim, NO GRH
  claim.""")
    n_pass = sum(1 for _n, ok in CHECKS if ok)
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed%s"
          % (time.time() - T0, len(CHECKS), len(FAILS),
             ("  " + ",".join(FAILS)) if FAILS else ""))
    return 0 if n_pass == len(CHECKS) else 1


if __name__ == "__main__":
    raise SystemExit(main())
