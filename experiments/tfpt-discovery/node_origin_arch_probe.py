#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""node_origin_arch_probe -- E8.WALL.NODEORIGIN.01: where does the
soft mode's stable interior node at u*/alpha ~ 0.35 come from?
Answer measured here: the node is CLASSICAL (the prime-free smooth
model reproduces it on 66 of 67 rungs, median offset 0.038) and it is
a BALANCE property -- the pure arch mode is NODELESS and the pure
comb mode's node sits at the origin; only their competition puts a
node at ~1/3 of the window.  Within the smooth model the node is NOT
a constant: it drifts linearly with depth (-0.0116 alpha + 0.373,
R2 0.97 over the accessible range), so no closed constant (1/3, 1/e)
is selected; the true node scatters arithmetically (+-0.04) around
the classical value.

EXPLORATION ONLY (experiments/): no ledger row, no paper edit, no
.md, nothing outside experiments/.  NO RH CLAIM in either direction.
Read-only import of the deployed v563 tables (the v881/v882 pattern).
Frozen (spec + sha256) before the frozen run; the smoke measurements
that shaped the wards are declared below.

THE QUESTION (continuation of E8.WALL.CRITDIR.01, the named object
(b) of note CII, user-approved): CII found the soft mode has a
genuine interior node at u*/alpha median 0.353 on every faithful
rung, stable along the ladder -- unexplained.  This probe tests
where it comes from: is it arithmetic or classical, arch or comb or
their balance, constant or drifting?

SMOKE-RUN DISCLOSURE (2026-08-10, before freezing): the smoke run
fixed three things that are frozen as found.  (i) The naive
"first sign change" node detector is edge-fragile for the smooth
modes; the frozen detector takes the interpolated zero between the
two dominant lobes (negative lobe must reach 2% of the peak).
(ii) On exactly one rung (kz = 97) the smooth model's two lowest
branches cross: its bottom eigenvector is a head-localized object
(overlap 1e-4 with the true mode, center of mass 0.16 alpha) while
its SECOND eigenvector carries the classical soft mode (overlap
0.972, node 0.302) -- frozen as a recorded branch crossing.
(iii) The smooth node's drift is clean only after masking that one
crossing (R2 0.16 raw -> 0.97 masked); smoke values: smooth node
0.334..0.297 falling with alpha, true node median 0.355, response to
a +-10% density rescale +0.009..+0.087, pure-comb bottom mode node
0.0008..0.0072, pure-arch bottom mode nodeless on all subset rungs,
grid-resolution stability 1e-4.

FROZEN CLAIMS (2026-08-10, frozen + SHA-hashed before the frozen
run):

 S1  CLASSICAL REDUCTION (the attribution).  Build the prime-free
     smooth model on every faithful rung (same arch lags, atoms
     replaced by the PNT continuum comb on a 6000-cell grid).
     (a) the smooth bottom eigenvector carries the true direction
         (overlap >= 0.8) on at least 60 of the faithful rungs
         (smoke: 66/67); every exception must be a BRANCH CROSSING
         -- one of the four lowest smooth eigenvectors carries
         overlap >= 0.8 (smoke: kz = 97, second branch, 0.972);
     (b) on the classical-branch rungs the smooth mode's node agrees
         with the true node: median |node_sm - node_true| < 0.06 in
         u*/alpha units (smoke: 0.038) and at least 55% of rungs
         within 0.05 (smoke: 46/66 = 70%).
     READING: the node is a property of the PRIME-FREE operator;
     the question reduces to smooth geometry.  Fail =>
     REDUCTION-BROKEN.

 S2  WHAT SETS IT (within the smooth model).
     (a) DENSITY BALANCE: rescaling the continuum density by 0.9 /
         1.1 moves the node UP with the comb weight on every subset
         rung: node(1.1) - node(0.9) > 0 (smoke: +0.009 shallow to
         +0.087 deep; response grows with depth).  The node position
         is a live arch-vs-comb balance point, not a rigid feature
         of either part;
     (b) THE DRIFT LAW: on the classical-branch rungs the smooth
         node follows node_sm/alpha = s * alpha + c with s < -0.005
         and R2 > 0.9 (smoke: -0.0116 alpha + 0.3727, R2 0.973);
         the true node's fit is RECORDED but not warded (smoke: R2
         0.17 -- arithmetic scatter dominates);
     (c) NEITHER HALF ALONE: the pure arch bottom mode is NODELESS
         (negative lobe < 2% of peak) on every subset rung, and the
         pure comb bottom mode's node sits at u*/alpha <= 0.05
         (smoke: 0.0008..0.0072).  The ~1/3 node exists only in the
         BALANCE.
     Fail => MECHANISM-BROKEN.

 S3  CANDIDATE VALUES, honestly (typed; recorded measurements only,
     NO numerology flag).  Deep-30% asymptotes (classical-branch
     rungs): true node and smooth node reported with error bars and
     compared, as plain distances, against 1/3 and 1/e = 0.3679.
     The smooth model's own answer is that the node is NOT constant
     in the accessible range (it crosses 1/3 on the way down), so no
     closed constant is selected; the true node's scatter covers
     both candidates.  A closed zero condition from the digamma
     structure of the arch kernel was NOT derived here -- said
     honestly; the deliverable is the measured attribution
     (classical + balance + drift law), not a matched constant.
     Always-true typed check; no kill.

 C   CONTROLS (must fire):
     C1 energy identity v.K.v = lam_min to 1e-8 relative on the
        subset rungs (true wall);
     C2 the smooth model FAILS ON VALUE while serving on direction:
        lam_min(K_smooth) < -0.5 on every subset rung (regression of
        v883 FLUCTUATIONS-REQUIRED; full-ladder range recorded);
     C3 RESOLUTION: the smooth node moves < 2e-3 between 3000- and
        12000-cell continuum grids on every subset rung (smoke:
        ~1e-4) -- the node is not a discretization artifact;
     C4 SCRAMBLE (seeded, rungs 13/40): randomized atom positions
        break the wall (lam_min < 0, regression) and the scrambled
        ground mode's node is RECORDED (no ward on its value) --
        the true node rides on a positive wall, the classical node
        does not need one;
     C5 FIREWALL: AST scan of this file for the deployed banned
        identifiers (zetazero, nzeros, primerange, isprime, primepi,
        nextprime, prevprime); none may appear as a call;
     C6 NO-RH-CLAIM: the verdict asserts nothing about RH's truth.

VERDICT (frozen precedence): REDUCTION-BROKEN / MECHANISM-BROKEN /
CONTROL-DEAD on kill; else NODEORIGIN-MEASURED with the measured
classical share, node offsets, drift law and asymptotes.

Sources (read-only): v563_paper2_readouts (deployed tables, arch
kernel with digamma structure, tent assembly, odd Toeplitz),
critical_direction_classical_probe / note CII (node invariant 0.353,
classical direction, named object (b)), wall_margin_mechanism_probe /
note CI (cancellation law), rh_leverage_probe / note C (67 faithful
rungs), v883 (FLUCTUATIONS-REQUIRED), tfpt_prime_front.tex (I5
equivalence typing).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/node_origin_arch_probe.py
"""

import ast
import hashlib
import math
import os
import sys
import time

import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
_VERIFY = os.path.abspath(os.path.join(_HERE, "..", "..", "verification"))
sys.path.insert(0, _HERE)
sys.path.insert(0, _VERIFY)

import v563_paper2_readouts as core        # noqa: E402  (READ-ONLY)

T0 = time.time()
CHECKS = []
KILLS = []
SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()

KZMAX = int(os.environ.get("NODEORIGIN_KZMAX", 150))
SUBSET = (9, 13, 26, 40, 60, 90, 121)
AUDIT = (13, 40)
SEED = 20260810
NG_SMOOTH = 6000
BANNED_IDS = ("zetazero", "nzeros", "primerange", "isprime",
              "primepi", "nextprime", "prevprime")


def check(name, ok, detail="", kill=None):
    CHECKS.append((name, bool(ok)))
    if kill and not ok:
        KILLS.append(kill)
    print("  [%s] %s%s" % ("PASS" if ok else "FAIL", name,
                           ("  -- " + detail) if detail else ""),
          flush=True)
    return bool(ok)


def section(title):
    print("\n" + "=" * 70)
    print(title)
    print("=" * 70)


def robust_node(vec, D, alpha):
    """interior node between the two dominant lobes: sign-normalize
    so the global peak is positive, take the interpolated zero
    between the most negative point and the positive peak; nan if
    the negative lobe stays below 2% of the peak."""
    v = vec * np.sign(vec[int(np.argmax(np.abs(vec)))])
    ip = int(np.argmax(v))
    im = int(np.argmin(v))
    if v[im] >= -0.02 * v[ip]:
        return float("nan")
    lo, hi = (im, ip) if im < ip else (ip, im)
    seg = v[lo:hi + 1]
    idx = np.where(np.diff(np.sign(seg)) != 0)[0]
    if len(idx) == 0:
        return float("nan")
    i = lo + (int(idx[0]) if im < ip else int(idx[-1]))
    t = v[i] / (v[i] - v[i + 1])
    return (i + t) * D / alpha


def smooth_comb(alpha, ng=NG_SMOOTH):
    ug = (np.arange(ng) + 0.5) * (2.0 * alpha / ng)
    mg = 2.0 * np.exp(ug / 2.0) * (2.0 * alpha / ng)
    return ug, mg


# ======================================================================
section("S0: setup -- ladder, smooth companions, nodes")
# ======================================================================
print("spec sha256 = %s" % SPEC_SHA)

RUNGS = {}
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
    c_at = core.atom_lags_at(alpha, M, uu, mu)[0]
    c_ar = np.asarray(core.arch_lags(M, D), float)
    w, V = np.linalg.eigh(core.odd_toeplitz(c_ar + c_at, M))
    v = V[:, 0]
    ug, mg = smooth_comb(alpha)
    c_sm = core.atom_lags_at(alpha, M, ug, mg)[0]
    ws, Vs = np.linalg.eigh(core.odd_toeplitz(c_ar + c_sm, M))
    ov4 = [abs(float(v @ Vs[:, j])) for j in range(4)]
    jbest = int(np.argmax(ov4))
    RUNGS[kz] = dict(alpha=alpha, M=M, D=D, h=h, uu=uu, mu=mu,
                     c_at=c_at, c_ar=c_ar, c_sm=c_sm,
                     lmin=float(w[0]), v=v, lam_sm=float(ws[0]),
                     ov4=ov4, jbest=jbest,
                     node_t=robust_node(v, D, alpha),
                     node_s=robust_node(Vs[:, 0], D, alpha),
                     node_best=robust_node(Vs[:, jbest], D, alpha))
print("  %d faithful rungs rebuilt (alpha = %.3f..%.3f), %.1f s"
      % (len(RUNGS), min(R["alpha"] for R in RUNGS.values()),
         max(R["alpha"] for R in RUNGS.values()), time.time() - T0))

# ======================================================================
section("S1: classical reduction")
# ======================================================================
kzs = sorted(RUNGS)
ov0 = np.array([RUNGS[k]["ov4"][0] for k in kzs])
n_ok = int(np.sum(ov0 >= 0.8))
exc = [k for k in kzs if RUNGS[k]["ov4"][0] < 0.8]
exc_ok = all(max(RUNGS[k]["ov4"]) >= 0.8 for k in exc)
for k in exc:
    R = RUNGS[k]
    print("    exception kz %d: bottom-branch overlap %.4f, best "
          "branch j = %d with overlap %.4f, node %.4f (true %.4f)"
          % (k, R["ov4"][0], R["jbest"], max(R["ov4"]),
             R["node_best"], R["node_t"]))
check("S1.a THE DIRECTION SURVIVES LADDER-WIDE: the smooth bottom "
      "eigenvector carries the true direction (overlap >= 0.8) on "
      "%d/%d rungs (ward >= 60); the %d exception(s) are BRANCH "
      "CROSSINGS -- a higher smooth branch carries overlap %s"
      % (n_ok, len(kzs), len(exc),
         "/".join("%.3f" % max(RUNGS[k]["ov4"]) for k in exc)
         or "-"),
      n_ok >= 60 and exc_ok, kill="REDUCTION-BROKEN")

mask = [k for k in kzs if RUNGS[k]["ov4"][0] >= 0.8]
nt = np.array([RUNGS[k]["node_t"] for k in mask])
ns = np.array([RUNGS[k]["node_s"] for k in mask])
al = np.array([RUNGS[k]["alpha"] for k in mask])
d = np.abs(ns - nt)
frac05 = float(np.mean(d < 0.05))
print("    true node u*/alpha: median %.4f range %.4f..%.4f"
      % (float(np.median(nt)), nt.min(), nt.max()))
print("    smooth node u*/alpha: median %.4f range %.4f..%.4f"
      % (float(np.median(ns)), ns.min(), ns.max()))
check("S1.b THE NODE IS CLASSICAL: on the %d classical-branch rungs "
      "the smooth mode's node sits at the true node -- median "
      "|node_sm - node_true| = %.4f (ward < 0.06), %.0f%% within "
      "0.05 (ward >= 55%%), max offset %.4f.  The prime-free "
      "operator already puts the node at ~1/3 of the window; the "
      "question reduces to smooth geometry"
      % (len(mask), float(np.median(d)), 100 * frac05, d.max()),
      float(np.median(d)) < 0.06 and frac05 >= 0.55,
      kill="REDUCTION-BROKEN")

# ======================================================================
section("S2: what sets it (inside the smooth model)")
# ======================================================================
resp_rows = []
for kz in SUBSET:
    R = RUNGS[kz]
    nd = {}
    for sc in (0.9, 1.1):
        wsc, Vsc = np.linalg.eigh(
            core.odd_toeplitz(R["c_ar"] + sc * R["c_sm"], R["M"]))
        nd[sc] = robust_node(Vsc[:, 0], R["D"], R["alpha"])
    resp_rows.append((kz, nd[0.9], nd[1.1], nd[1.1] - nd[0.9]))
    print("    kz %3d: node at density x0.9 = %.4f, x1.1 = %.4f, "
          "response %+.4f (d node / d ln rho ~ %+.3f)"
          % (kz, nd[0.9], nd[1.1], nd[1.1] - nd[0.9],
             (nd[1.1] - nd[0.9]) / (math.log(1.1) - math.log(0.9))))
check("S2.a DENSITY BALANCE: +-10%% of continuum density moves the "
      "node UP with the comb weight on every subset rung -- "
      "node(1.1) - node(0.9) = %+.4f..%+.4f (ward > 0), response "
      "growing with depth.  The node is a live arch-vs-comb balance "
      "point"
      % (min(r[3] for r in resp_rows), max(r[3] for r in resp_rows)),
      all(r[3] > 0 for r in resp_rows), kill="MECHANISM-BROKEN")

sl_s, ic_s = np.polyfit(al, ns, 1)
r2_s = 1.0 - float(np.var(ns - (sl_s * al + ic_s)) / np.var(ns))
sl_t, ic_t = np.polyfit(al, nt, 1)
r2_t = 1.0 - float(np.var(nt - (sl_t * al + ic_t)) / np.var(nt))
check("S2.b THE DRIFT LAW: the smooth node is NOT a constant -- "
      "node_sm/alpha = %.5f alpha %+.4f with R2 = %.3f (wards s < "
      "-0.005, R2 > 0.9) over alpha = %.2f..%.2f; the true node's "
      "fit %.5f alpha %+.4f has R2 = %.3f (RECORDED, not warded: "
      "arithmetic scatter dominates the classical drift)"
      % (sl_s, ic_s, r2_s, al.min(), al.max(), sl_t, ic_t, r2_t),
      sl_s < -0.005 and r2_s > 0.9, kill="MECHANISM-BROKEN")

part_rows = []
for kz in SUBSET:
    R = RUNGS[kz]
    wa, Va = np.linalg.eigh(core.odd_toeplitz(R["c_ar"], R["M"]))
    wc, Vc = np.linalg.eigh(core.odd_toeplitz(R["c_sm"], R["M"]))
    va = Va[:, 0] * np.sign(Va[:, 0][int(np.argmax(np.abs(Va[:, 0])))])
    neg_a = -float(va.min()) / float(va.max())
    nd_a = robust_node(Va[:, 0], R["D"], R["alpha"])
    nd_c = robust_node(Vc[:, 0], R["D"], R["alpha"])
    part_rows.append((kz, neg_a, nd_a, nd_c, float(wa[0]),
                      float(wc[0])))
    print("    kz %3d: ARCH-only ground mode neg lobe %.4f of peak "
          "(node %s, lam %+.2e); COMB-only node %.4f (lam %+.2e)"
          % (kz, neg_a, "%.3f" % nd_a if np.isfinite(nd_a)
             else "none", wa[0], nd_c, wc[0]))
check("S2.c NEITHER HALF ALONE: the pure ARCH bottom mode is "
      "NODELESS on every subset rung (negative lobe %.4f..%.4f of "
      "peak, ward < 0.02 => no robust node), and the pure COMB "
      "bottom mode's node sits at the ORIGIN (u*/alpha = "
      "%.4f..%.4f, ward <= 0.05).  The ~1/3 node exists only in "
      "the arch-vs-comb BALANCE"
      % (min(r[1] for r in part_rows), max(r[1] for r in part_rows),
         min(r[3] for r in part_rows), max(r[3] for r in part_rows)),
      all((not np.isfinite(r[2])) and r[3] <= 0.05
          for r in part_rows), kill="MECHANISM-BROKEN")

# ======================================================================
section("S3: candidate values, honestly (typed)")
# ======================================================================
deep = al >= np.percentile(al, 70)
mt, st = float(np.mean(nt[deep])), float(np.std(nt[deep]))
ms, ss = float(np.mean(ns[deep])), float(np.std(ns[deep]))
a_third = (ic_s - 1.0 / 3.0) / (-sl_s)
print("    deep-30%% asymptotes: true %.4f +- %.4f, smooth %.4f +- "
      "%.4f" % (mt, st, ms, ss))
print("    candidates: 1/3 = %.4f (true offset %.2f sigma), 1/e = "
      "%.4f (true offset %.2f sigma)"
      % (1.0 / 3.0, abs(mt - 1.0 / 3.0) / st, 1.0 / math.e,
         abs(mt - 1.0 / math.e) / st))
print("    the smooth drift law crosses 1/3 at alpha ~ %.2f (inside "
      "the accessible range %.2f..%.2f)" % (a_third, al.min(),
                                            al.max()))
check("S3 NO CONSTANT SELECTED (typed, recorded only): the smooth "
      "model's node is not constant (it crosses 1/3 at alpha ~ %.1f "
      "and keeps falling, reaching %.4f +- %.4f on the deep third), "
      "while the true node sits at %.4f +- %.4f -- within %.2f "
      "sigma of 1/3 AND %.2f sigma of 1/e, discriminating neither.  "
      "A closed zero condition from the arch kernel's digamma "
      "structure was NOT derived here; the deliverable is the "
      "measured attribution: CLASSICAL origin, BALANCE mechanism, "
      "LINEAR drift in the smooth model, arithmetic scatter on top.  "
      "NO numerology flag is planted"
      % (a_third, ms, ss, mt, st, abs(mt - 1.0 / 3.0) / st,
         abs(mt - 1.0 / math.e) / st), True, kill=None)

# ======================================================================
section("C: controls")
# ======================================================================
cons = 0.0
for kz in SUBSET:
    R = RUNGS[kz]
    K = core.odd_toeplitz(R["c_ar"] + R["c_at"], R["M"])
    cons = max(cons, abs(float(R["v"] @ K @ R["v"]) - R["lmin"])
               / max(abs(R["lmin"]), 1e-30))
    del K
check("C1 energy identity v.K.v = lam_min holds to %.1e relative on "
      "the subset (ward 1e-8)" % cons, cons <= 1e-8,
      kill="CONTROL-DEAD")

lam_sub = [RUNGS[kz]["lam_sm"] for kz in SUBSET]
lam_all = [R["lam_sm"] for R in RUNGS.values()]
check("C2 the smooth model FAILS ON VALUE while carrying node and "
      "direction: lam_min(K_smooth) = %+.2f..%+.2f on the subset "
      "(ward < -0.5, regression of v883); full-ladder range "
      "%+.2f..%+.2f (recorded)"
      % (min(lam_sub), max(lam_sub), min(lam_all), max(lam_all)),
      all(x < -0.5 for x in lam_sub), kill="CONTROL-DEAD")

res_rows = []
for kz in SUBSET:
    R = RUNGS[kz]
    nd = {}
    for ng in (3000, 12000):
        ug, mg = smooth_comb(R["alpha"], ng)
        c2 = core.atom_lags_at(R["alpha"], R["M"], ug, mg)[0]
        w2, V2 = np.linalg.eigh(core.odd_toeplitz(R["c_ar"] + c2,
                                                  R["M"]))
        nd[ng] = robust_node(V2[:, 0], R["D"], R["alpha"])
    res_rows.append((kz, abs(nd[12000] - nd[3000])))
check("C3 RESOLUTION: the smooth node moves at most %.1e between "
      "3000- and 12000-cell continuum grids (ward < 2e-3 on every "
      "subset rung) -- not a discretization artifact"
      % max(r[1] for r in res_rows),
      all(r[1] < 2e-3 for r in res_rows), kill="CONTROL-DEAD")

rng = np.random.default_rng(SEED)
scr_rows = []
for kz in AUDIT:
    R = RUNGS[kz]
    uus = np.sort(rng.uniform(0.0, 2.0 * R["alpha"],
                              size=len(R["uu"])))
    c2 = core.atom_lags_at(R["alpha"], R["M"], uus, R["mu"])[0]
    w2, V2 = np.linalg.eigh(core.odd_toeplitz(R["c_ar"] + c2,
                                              R["M"]))
    scr_rows.append((kz, float(w2[0]),
                     robust_node(V2[:, 0], R["D"], R["alpha"])))
    print("    kz %3d scrambled: lam_min %+.3f, ground-mode node "
          "%.4f (true %.4f) -- recorded"
          % (kz, w2[0], scr_rows[-1][2], R["node_t"]))
check("C4 SCRAMBLE fires: randomized positions break the wall "
      "(lam_min = %s < 0, regression) while the scrambled node is "
      "recorded without a ward -- the classical node does not need "
      "a positive wall, the true wall needs the primes"
      % "/".join("%+.2f" % r[1] for r in scr_rows),
      all(r[1] < 0.0 for r in scr_rows), kill="CONTROL-DEAD")

_tree = ast.parse(open(__file__, encoding="utf-8").read())
_called = {n.func.id for n in ast.walk(_tree)
           if isinstance(n, ast.Call) and isinstance(n.func, ast.Name)}
_called |= {n.func.attr for n in ast.walk(_tree)
            if isinstance(n, ast.Call)
            and isinstance(n.func, ast.Attribute)}
hits = sorted(_called & set(BANNED_IDS))
check("C5 FIREWALL: none of the deployed banned identifiers %s is "
      "called (hits: %s); no zero ordinate appears anywhere in this "
      "probe" % (list(BANNED_IDS), hits or "none"), not hits,
      kill="CONTROL-DEAD")

# ======================================================================
section("VERDICT")
# ======================================================================
if KILLS:
    verdict = KILLS[0]
else:
    verdict = ("NODEORIGIN-MEASURED (NODE-CLASSICAL-%d/%d + "
               "BRANCH-CROSS-%s + BALANCE-SET (ARCH-NODELESS + "
               "COMB-NODE-AT-ZERO) + DRIFT-%.4fA-R2-%.2f + "
               "TRUE-%.3f+-%.3f + NO-CONSTANT-SELECTED)"
               % (n_ok, len(kzs),
                  ",".join("KZ%d" % k for k in exc) or "NONE",
                  sl_s, r2_s, mt, st))
check("C6 NO-RH-CLAIM: the verdict reports an attribution and a "
      "drift law -- no truth value for RH in either direction",
      "RH-TRUE" not in verdict and "RH-FALSE" not in verdict,
      kill="CONTROL-DEAD")

n_pass = sum(1 for _, ok in CHECKS if ok)
print("\nCHECKS: %d/%d passed" % (n_pass, len(CHECKS)))
if n_pass != len(CHECKS):
    print("FAILED: %s" % [nm for nm, ok in CHECKS if not ok])
print("VERDICT: %s" % verdict)
print("""
WHAT THIS MEASURES (exploration only):
 * THE NODE IS CLASSICAL: the prime-free smooth model puts the soft
   mode's interior node where the true wall puts it, on 66 of 67
   rungs (median offset 0.038 in u*/alpha); the one exception is a
   branch crossing in the smooth spectrum, not a failure of the
   classical picture.  The primes add scatter (+-0.04), not the
   node.
 * THE NODE IS A BALANCE: the pure arch mode is nodeless, the pure
   comb mode's node sits at the origin, and a +-10% density rescale
   moves the node -- only the arch-vs-comb competition puts it near
   one third of the window.
 * THE NODE IS NOT A CONSTANT: inside the smooth model it falls
   linearly with depth (-0.012 per unit alpha, R2 0.97) and crosses
   1/3 inside the accessible range; the true node's scatter covers
   both 1/3 and 1/e.  No closed constant is selected, and no zero
   condition was derived from the digamma structure -- the honest
   deliverable is attribution + drift law, not a matched number.
NO ledger/paper/website claim; NO RH claim in either direction; NO
physics claim beyond the recorded identities and measurements.
""")
print("runtime: %.1f s" % (time.time() - T0))
sys.exit(0 if n_pass == len(CHECKS) else 1)
