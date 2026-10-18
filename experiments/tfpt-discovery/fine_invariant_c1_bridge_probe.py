#!/usr/bin/env python3
"""SLICE B sandbox probe -- fine Hodge-ray invariants vs the C = 1 margin.

Question (the first quantitative geometry <-> arithmetic bridge test):
do the fine Hodge-chamber ray invariants of the transported window
vectors z = P^-1 y (projective spacelike angle phi, cone distance
q/|z|^2, timelike angle theta) correlate WINDOW-WISE with the v618
uniform-constant load eps_h * h (equivalently the C = 1 margin
1 - eps_h * h) BEYOND the trivial h-dependence?

Machinery: v563_paper2_readouts READ-ONLY (zones, windows, spline
reads); the v618 model matrix + closed v591 lock direction REBUILT
verbatim (no import of v618 to avoid re-running its checks); the fine
invariants exactly as the predecessor probe
p_canonicity_hodge_fine_probe.py defines them (J_fix eigenbasis,
ascending eigenvalues, sign-normalized columns).

Preregistered decisions (declared BEFORE looking at the numbers):
  * primary invariants: phi (projective spacelike angle) and q/|z|^2;
    secondary (reported, not verdict-driving): theta, c1/c2;
  * sample: complete windows (2 alpha <= u_max) with the LOCK SIGN
    (q_real q_model > 0), h != 1292 -- the v627 x v618 intersection;
  * target variable: eps_h * h = |q_real/q_model| * h (the C = 1 load;
    the margin is 1 - eps_h * h, a monotone flip -- same rank tests);
  * controls: h via rank-linear AND rank-cubic residualization
    (rank-based control absorbs ANY monotone h-trend up to the
    rank-polynomial order), plus (h, alpha) jointly;
  * verdict-driving test: partial Spearman after the rank-cubic
    h-control, permutation p (20000 perms, seed 20260802, residual
    permutation a la Freedman-Lane);
  * PASS (BRIDGE-CORRELATED) iff |rho_partial| >= 0.30 AND p < 0.01
    for phi or q/|z|^2; 0.01 <= p < 0.05 -> BRIDGE-PARTIAL; else
    NO-INDEPENDENT-INFORMATION.  An honest negative is a result.

Verdict enums (frozen): BRIDGE-CORRELATED, BRIDGE-PARTIAL,
NO-INDEPENDENT-INFORMATION, MIXED (guards failed).

Sandbox probe: reads verification/ READ-ONLY, writes nothing.
"""
import math
import os
import sys
import time

import numpy as np
import sympy as sp

_here = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(_here, "..", "..",
                                                "verification")))

T0 = time.time()
CHECKS = []


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok)))
    print("[%s] %s%s" % ("PASS" if ok else "FAIL", name,
                         (" -- " + detail) if detail else ""))


import v563_paper2_readouts as core  # noqa: E402  (READ-ONLY import)
from mpmath import mp, zeta, diff    # noqa: E402

# ---------------------------------------------------------------- v618 verbatim
GRID_PER_D = 4.0
N_PERM = 20000
SEED = 20260802

mp.dps = 30
C_TH = float(-2 * diff(lambda s: zeta(s), 0.5) / zeta(0.5))
U0 = 2.0 * math.log(-C_TH / 4.0)


def model_matrix(r):
    """v618 model_matrix, verbatim (zeta constant hoisted)."""
    alpha, Mz, D = r["alpha"], r["M"], r["D"]
    delta = D / GRID_PER_D
    n_cells = int(math.ceil((2.0 * alpha - U0) / delta))
    edges = U0 + delta * np.arange(n_cells + 1)
    lam = 0.5 * 4.0 * (np.exp(edges[1:] / 2) - np.exp(edges[:-1] / 2))
    centers = 0.5 * (edges[:-1] + edges[1:])
    X = np.empty((n_cells, 3))
    for k, u_j in enumerate(centers):
        X[k, 0] = core.spline_project(r["W11"], u_j, D, Mz)
        X[k, 1] = core.spline_project(r["W22"], u_j, D, Mz)
        X[k, 2] = core.spline_project(r["W12"], u_j, D, Mz)
    s = (lam[:, None] * X).sum(axis=0)
    return np.array([[s[0], s[2]], [s[2], s[1]]])


def lock_dir(alpha):
    """The closed v591 lock direction (parameter-free)."""
    v2v1 = -(alpha ** 2 + 16 * math.pi ** 2) / (2 * (alpha ** 2
                                                     + 4 * math.pi ** 2))
    v = np.array([1.0, v2v1])
    return v / np.linalg.norm(v)


# ------------------------------------------------------- fine invariants (pred.)
P = sp.Matrix([[3, 0, 0], [3, 0, 2], [-1, 1, -1]])
Jfix = sp.Matrix([[16, 2, 4], [2, -2, 2], [4, 2, -2]])
Jdet = sp.Matrix([[0, 1, 0], [1, 0, 0], [0, 0, -2]])
assert sp.simplify(P.T * Jdet * P - Jfix) == sp.zeros(3, 3)
PinvN = np.array(P.inv().evalf(20).tolist(), dtype=float)
JfixN = np.array(Jfix.tolist(), dtype=float)
w_, V_ = np.linalg.eigh(JfixN)
for j in range(3):
    k = int(np.argmax(np.abs(V_[:, j])))
    if V_[k, j] < 0:
        V_[:, j] *= -1.0


def invariants(S):
    """theta, q/|z|^2, c1/c2, phi -- predecessor conventions verbatim."""
    y = np.array([S[0, 0], S[1, 1], S[0, 1]], dtype=float)
    z = PinvN @ y
    nz = float(np.linalg.norm(z))
    c = V_.T @ z
    theta = math.degrees(math.acos(min(1.0, abs(float(c[2])) / nz)))
    qn = float(z @ (JfixN @ z)) / nz ** 2
    ratio = float(c[0] / c[1]) if c[1] != 0 else float("inf")
    phi = math.degrees(math.atan2(float(c[1]), float(c[0]))) % 180.0
    return theta, qn, ratio, phi, abs(float(z @ (JfixN @ z))
                                      - 2.0 * float(np.linalg.det(S)))


# ---------------------------------------------------------------- statistics
def rankdata(a):
    a = np.asarray(a, float)
    order = np.argsort(a, kind="mergesort")
    r = np.empty(len(a))
    i = 0
    while i < len(a):
        j = i
        while j + 1 < len(a) and a[order[j + 1]] == a[order[i]]:
            j += 1
        r[order[i:j + 1]] = 0.5 * (i + j) + 1.0
        i = j + 1
    return r


def pearson(xx, yy):
    xx = np.asarray(xx, float) - np.mean(xx)
    yy = np.asarray(yy, float) - np.mean(yy)
    return float(xx @ yy / math.sqrt((xx @ xx) * (yy @ yy)))


def spearman(xx, yy):
    return pearson(rankdata(xx), rankdata(yy))


def perm_p(xx, yy, rng, nperm=N_PERM):
    """Two-sided permutation p for pearson(xx, yy) permuting xx."""
    obs = pearson(xx, yy)
    cnt = 0
    for _ in range(nperm):
        if abs(pearson(rng.permutation(xx), yy)) >= abs(obs) - 1e-12:
            cnt += 1
    return obs, (cnt + 1.0) / (nperm + 1.0)


def control_cols(controls, poly):
    cols = []
    for cvec in controls:
        rc = rankdata(cvec)
        rc = (rc - rc.mean()) / rc.std()
        for p_ in range(1, poly + 1):
            cols.append(rc ** p_)
    return cols


def residualize(vec, cols):
    C = np.column_stack([np.ones(len(vec))] + cols)
    beta, _, _, _ = np.linalg.lstsq(C, vec, rcond=None)
    return vec - C @ beta


def partial_spearman(xx, yy, controls, rng, poly=1, nperm=N_PERM):
    """Rank-based partial correlation, permutation p on the residuals."""
    cols = control_cols(controls, poly)
    ex = residualize(rankdata(xx), cols)
    ey = residualize(rankdata(yy), cols)
    return perm_p(ex, ey, rng, nperm)


def tertile_medians(key, val):
    order = np.argsort(np.asarray(key, float), kind="mergesort")
    parts = np.array_split(order, 3)
    val = np.asarray(val, float)
    return [float(np.median(val[ix])) for ix in parts]


def tertile_spread_p(key, val, rng, nperm=N_PERM):
    meds = tertile_medians(key, val)
    obs = max(meds) - min(meds)
    val = np.asarray(val, float)
    cnt = 0
    for _ in range(nperm):
        m = tertile_medians(key, rng.permutation(val))
        if (max(m) - min(m)) >= obs - 1e-15:
            cnt += 1
    return meds, obs, (cnt + 1.0) / (nperm + 1.0)


# ---------------------------------------------------------------- build surface
print("=" * 78)
print("B: fine Hodge invariants vs the C = 1 load eps_h * h")
print("=" * 78)

u_max = float(core.U_ALL[-1])
recs = []
for kz in core.frame_a_zones():
    r = core.build_window(kz)
    if r["h"] == 1292:
        continue
    Sm = model_matrix(r)
    v = lock_dir(r["alpha"])
    q_r = float(v @ ((r["B"] - r["S"]) @ v))
    q_m = float(v @ ((r["B"] - Sm) @ v))
    theta, qn, ratio, phi, qresid = invariants(r["S"])
    recs.append(dict(h=int(r["h"]), alpha=float(r["alpha"]),
                     complete=(2.0 * r["alpha"] <= u_max),
                     lock=(q_r * q_m > 0.0),
                     eh=abs(q_r / q_m) * float(r["h"]),
                     theta=theta, qn=qn, ratio=ratio, phi=phi,
                     qresid=qresid))

n_all = len(recs)
lock_recs = [rec for rec in recs if rec["lock"]]
flip_hs = sorted(rec["h"] for rec in recs if not rec["lock"])
eh_lock = np.array([rec["eh"] for rec in lock_recs])
h_lock = np.array([rec["h"] for rec in lock_recs], float)
mx = float(eh_lock.max())
h_at_mx = int(h_lock[int(np.argmax(eh_lock))])
n_complete = sum(1 for rec in recs if rec["complete"])
incomplete_hs = sorted(rec["h"] for rec in recs if not rec["complete"])

check("G0.1 v618 surface reproduces: %d floor-passed windows, %d "
      "lock-sign, flips at h = %s, max eps*h = %.3f at h = %d; "
      "%d complete windows (incomplete: h = %s)"
      % (n_all, len(lock_recs), flip_hs, mx, h_at_mx,
         n_complete, incomplete_hs),
      n_all == 69 and len(lock_recs) == 67 and flip_hs == [1219, 1445]
      and 0.95 < mx <= 1.0 and h_at_mx == 184 and n_complete == 67)

meds618 = tertile_medians(h_lock, eh_lock)
check("G0.2 v618 tertile medians of eps*h over the lock-sign h-ladder "
      "reproduce: %.3f / %.3f / %.3f (v618: ~0.61/0.44/0.39, "
      "non-increasing)" % tuple(meds618),
      abs(meds618[0] - 0.61) < 0.03 and abs(meds618[1] - 0.44) < 0.03
      and abs(meds618[2] - 0.39) < 0.03
      and meds618[0] >= meds618[1] >= meds618[2])

sample = [rec for rec in recs if rec["complete"] and rec["lock"]]
n_s = len(sample)
qres_max = max(rec["qresid"] for rec in sample)
check("G0.3 analysis sample = complete x lock-sign: n = %d windows; "
      "transport bookkeeping exact (max |q(z) - 2 det S| = %.1e)"
      % (n_s, qres_max), n_s >= 60 and qres_max < 1e-9)

hs = np.array([rec["h"] for rec in sample], float)
al = np.array([rec["alpha"] for rec in sample], float)
eh = np.array([rec["eh"] for rec in sample], float)
inv_vals = {"phi": np.array([rec["phi"] for rec in sample]),
            "qn": np.array([rec["qn"] for rec in sample]),
            "theta": np.array([rec["theta"] for rec in sample]),
            "ratio": np.array([rec["ratio"] for rec in sample])}

print("    per-window table (h | phi_deg | q/|z|^2 | theta_deg | eps*h):")
for rec in sorted(sample, key=lambda rr: rr["h"]):
    print("      h=%-5d phi=%9.5f  qn=%8.5f  theta=%8.5f  eh=%7.4f"
          % (rec["h"], rec["phi"], rec["qn"], rec["theta"], rec["eh"]))

# ---------------------------------------------------------------- correlations
rng = np.random.default_rng(SEED)

print("-" * 78)
sp_h, p_h = perm_p(rankdata(hs), rankdata(eh), rng)
sp_a, p_a = perm_p(rankdata(al), rankdata(eh), rng)
check("B1.1 [baseline, structureless controls] Spearman(h, eps*h) = "
      "%.4f (perm p = %.5f); Spearman(alpha, eps*h) = %.4f (p = %.5f) "
      "-- the trivial depth trend the invariants must beat"
      % (sp_h, p_h, sp_a, p_a), True)

print("    invariant <-> h redundancy (Spearman): "
      + ", ".join("%s: %.4f" % (n_, spearman(inv_vals[n_], hs))
                  for n_ in ("phi", "qn", "theta", "ratio"))
      + "; phi<->qn: %.4f" % spearman(inv_vals["phi"], inv_vals["qn"]))

raw_stats = {}
for n_ in ("phi", "qn", "theta", "ratio"):
    rho_s, p_s = perm_p(rankdata(inv_vals[n_]), rankdata(eh), rng)
    r_p = pearson(inv_vals[n_], eh)
    raw_stats[n_] = (rho_s, p_s, r_p)
check("B1.2 [raw] Spearman(invariant, eps*h) with perm p, plus "
      "Pearson: %s"
      % "; ".join("%s: rho=%.4f (p=%.5f), r=%.4f" % (n_, *raw_stats[n_])
                  for n_ in ("phi", "qn", "theta", "ratio")), True)

# ---------------------------------------------------------------- partial
part = {}
for n_ in ("phi", "qn", "theta", "ratio"):
    rho1, p1 = partial_spearman(inv_vals[n_], eh, [hs], rng, poly=1)
    rho3, p3 = partial_spearman(inv_vals[n_], eh, [hs], rng, poly=3)
    rhoha, pha = partial_spearman(inv_vals[n_], eh, [hs, al], rng, poly=1)
    part[n_] = (rho1, p1, rho3, p3, rhoha, pha)
    print("    partial %-6s | h rank-lin: rho=%.4f p=%.5f | h rank-cubic: "
          "rho=%.4f p=%.5f | (h,alpha): rho=%.4f p=%.5f"
          % (n_, rho1, p1, rho3, p3, rhoha, pha))

check("B2.1 [verdict-driving] h-controlled partial Spearman "
      "(rank-cubic): phi: rho=%.4f (p=%.5f); q/|z|^2: rho=%.4f "
      "(p=%.5f) -- preregistered gate |rho| >= 0.30 AND p < 0.01"
      % (part["phi"][2], part["phi"][3], part["qn"][2], part["qn"][3]),
      True)

# ---------------------------------------------------------------- tertiles
meds_phi, spread_phi, p_t_phi = tertile_spread_p(inv_vals["phi"], eh, rng)
meds_qn, spread_qn, p_t_qn = tertile_spread_p(inv_vals["qn"], eh, rng)
check("B3.1 tertile structure BY INVARIANT (medians of eps*h): "
      "phi-tertiles %.3f/%.3f/%.3f (spread %.3f, perm p = %.5f); "
      "qn-tertiles %.3f/%.3f/%.3f (spread %.3f, p = %.5f); compare "
      "h-tertiles %.3f/%.3f/%.3f"
      % (*meds_phi, spread_phi, p_t_phi, *meds_qn, spread_qn, p_t_qn,
         *meds618), True)

cols3 = control_cols([hs], 3)
eh_res = residualize(rankdata(eh), cols3)
meds_phi_r, spread_phi_r, p_tr_phi = tertile_spread_p(
    inv_vals["phi"], eh_res, rng)
meds_qn_r, spread_qn_r, p_tr_qn = tertile_spread_p(
    inv_vals["qn"], eh_res, rng)
check("B3.2 tertile structure on the h-DETRENDED load (rank-cubic "
      "residuals): phi-tertiles %.2f/%.2f/%.2f (p = %.5f); qn-tertiles "
      "%.2f/%.2f/%.2f (p = %.5f)"
      % (*meds_phi_r, p_tr_phi, *meds_qn_r, p_tr_qn), True)

# ---------------------------------------------------------------- verdict
guards_ok = all(ok for name, ok in CHECKS if name.startswith("G0"))
best = {n_: (part[n_][2], part[n_][3]) for n_ in ("phi", "qn")}
hit = any(abs(rho) >= 0.30 and p < 0.01 for rho, p in best.values())
near = any(p < 0.05 for _, p in best.values())
if not guards_ok:
    VERDICT = "MIXED (guards failed)"
elif hit:
    VERDICT = "BRIDGE-CORRELATED"
elif near:
    VERDICT = "BRIDGE-PARTIAL"
else:
    VERDICT = ("NO-INDEPENDENT-INFORMATION (the fine invariants do not "
               "explain the C = 1 margin beyond the h-trend on this "
               "surface)")

print("=" * 78)
n_pass = sum(1 for _, ok in CHECKS if ok)
print("%d/%d checks passed" % (n_pass, len(CHECKS)))
print("VERDICT B: %s -- primary h-controlled (rank-cubic) partials: "
      "phi rho=%.4f p=%.5f; qn rho=%.4f p=%.5f"
      % (VERDICT, part["phi"][2], part["phi"][3],
         part["qn"][2], part["qn"][3]))
print("elapsed: %.1f s" % (time.time() - T0))
if n_pass == len(CHECKS):
    print("ALL CHECKS PASSED")
else:
    print("SOME CHECKS FAILED")
