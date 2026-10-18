#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""cross_chain_gamma_probe -- PRIME.RDAGGER.CROSS_CHAIN_GAMMA.01
(round 425): is ||b||^2 < B_w a cross-chain
theorem (mu-Parseval of sigma vs tilde S+5/7)?

THE OBJECT.
  Both energies are RKHS pairings of the SAME
  signed border sigma:
    ||b||^2 = w^T K_N^mu w     (mu-ONB of P_<N)
    S       = w^T K_N^{mu-nu} w (tilde-ONB)
  On P_<N, <p,p>_mu = int p^2 dmu >= int p^2 d(mu-nu)
  = <p,p>_{mu-nu} whenever nu is a positive
  measure and the tilde form is positive
  (chain ok).  Reproducing kernels then satisfy
  K^{mu-nu} ≽ K^mu, hence ||b||^2 <= S.
  B_w = S_{N-2}+5/7 equals S iff q_N=1, and
  S < B_w iff q_N < 1.  So ||b||^2 < B_w
  is ||b||^2 <= S plus q_N < 1 (or slack).

CALIBRATION DISCLOSURE.  Kernel comparison,
||G||_op on col(Psi), q_N vs B_w, random
borders, one-atom, dead q_N>1, unnorm, core-42
first measured in /tmp (r425_cal.py,
r425_cal2.py, r425_cal3.py) on the r424
constructors, 2026-08-29.  Frozen floors
below are that measurement, sealed as gates.
Pins disclosed.  Builder fallback TAKEN for
k=8: r421 pin gamma=0.6386, not re-gated live.

FROZEN FROM /tmp (live re-gated except k=8):
  * SATZ ||b||^2 <= S: Q-toy constants, mu
    weights (2,1), nu (1) on the second atom,
    K_mu=1/3 <= K_t=1/2, Dirac-at-0 ratio 2/3.
    Machine: f^2 = S (1e-15); ray = b2/S <= 1
    on 42/42 + EXT + dead.  Parallel-subspace
    ||G||_op^2 = 1.0000 (w9, k=5).
  * q_N < 1 on core-42 ([0.0015, 0.9805]) =>
    S < B_w => gamma<1 as a COMPOSED theorem
    on that census.  k=5 tightest ray=0.799
    (q_N=0.023 -- slack is kernel, not budget).
  * DEAD chi: q_N=1.21, 1.33 > 1, so S > B_w;
    ||b||^2 <= S does NOT imply ||b||^2 <= B_w.
    They still have gamma<1 by kernel slack
    (ray 0.62).  Random borders: ray ~ 0.02
    (this sigma is special, not the maximizer).
  * Unnorm mu-frame: gamma=2.51>1 (not an ONB,
    SATZ does not apply).
  * k=8 pin gamma=0.6386.

AUSGANG B2_LE_S_SATZ / QN_BRIDGES_BW /
DEAD_NEEDS_SLACK / COFINAL_OPEN.
SATZ: ||b||^2 <= S (kernel Loewner).
Posted ||b||^2 < B_w REDUZIERT to q_N<1.
On the v960 42-rung q_N<1 census it composes
to gamma<1.  Cofinal q_N remains open.
Does not move the mincut.  No RH claim.

MACHINERY: S424.chain_pack / ABD / BH.

NO RH CLAIM.  Finite RKHS comparison plus a
named q_N bridge.  Research documentation,
not a theorem of RH.  No L* claim.
No R-dagger claim.
"""
from __future__ import annotations

import argparse
import ast
import hashlib
import math
import os
import sys
import time
from fractions import Fraction as Fr

import numpy as np

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DISC = os.path.dirname(os.path.abspath(__file__))
PROB = os.path.join(REPO, "rh", "problem")
for p in (DISC, PROB):
    if p not in sys.path:
        sys.path.insert(0, p)

import gamma_chain_probe as S424  # noqa: E402
import cj_sigma_probe as S420  # noqa: E402
import den_limit_probe as S423  # noqa: E402
import edge_signature_probe as ES  # noqa: E402
import source_sch_sign_probe as S417  # noqa: E402
import phi_bb_sign_probe as S418  # noqa: E402
import pair_extremal_probe as PX  # noqa: E402
import hirota_sign_probe as HS  # noqa: E402
import principal_bessel_probe as PB  # noqa: E402
import augmented_borodin_duality_probe as ABD  # noqa: E402
import verify_lstar_instance as V  # noqa: E402
import dirichlet_matched_frame_probe as DMF  # noqa: E402
import high_moment_inertia_probe as HM  # noqa: E402
import final_two_rank_inertia_probe as FTI  # noqa: E402

ES_SHA_PREFIX = "395673f2"
S417_SHA_PREFIX = "f2905f2a"
S418_SHA_PREFIX = "6ef3a327"
S420_SHA_PREFIX = "46409e2f"
S423_SHA_PREFIX = "15693316"
S424_SHA_PREFIX = "0c85977b"
HM_SHA_PREFIX = "bb1dcf6a"
FTI_SHA_PREFIX = "e0d79840"
DMF_SHA_PREFIX = "4bf1a94b"

FLOOR = ES.FLOOR
SCR_NNEG = ES.SCR_NNEG
SEL_LIVE = ((4, 9), (5, 17), (6, 26), (7, 43), (9, 116))
K8_PIN = dict(k=8, kz=69, gam=0.6386)
W9_GAMS, W9_QN, W9_GAM = 0.7264, 0.2143, 0.6778
K5_GAMS, K5_QN = 0.7992, 0.0228
CORE_N = 42
QBAR = 0.80
DEAD_QN_LO = 1.0

SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
CHECKS = []
T0 = time.time()


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok)))
    print("  [%s] %-44s %s" % ("PASS" if ok else "FAIL", name, detail),
          flush=True)
    return bool(ok)


def section(t):
    print("\n" + "=" * 78)
    print(t)
    print("=" * 78, flush=True)


def firewall_audit():
    src = open(os.path.abspath(__file__), "r", encoding="utf-8").read()
    tree = ast.parse(src)
    forb = {"zeta" + "zero", "n" + "zeros", "prime" + "range",
            "is" + "prime", "gram" + "point"}
    bad = []
    for node in ast.walk(tree):
        nm = node.attr if isinstance(node, ast.Attribute) else (
            node.id if isinstance(node, ast.Name) else None)
        if nm and nm.lower() in forb:
            bad.append("%s@%d" % (nm, node.lineno))
    return (not bad), ("NO zero/prime oracles; RKHS / "
                       "border chain only"
                       if not bad else "; ".join(bad))


def antigate_fragment_audit():
    frags = ("poly" + "fit", "curve_" + "fit", "lst" + "sq",
             "mini" + "mize", "Line" + "arRegression")
    src = open(os.path.abspath(__file__), "r", encoding="utf-8").read()
    tree = ast.parse(src)
    hits = []
    for node in ast.walk(tree):
        nm = None
        if isinstance(node, ast.Attribute):
            nm = node.attr
        elif isinstance(node, ast.Name):
            nm = node.id
        elif isinstance(node, ast.FunctionDef):
            nm = node.name
        if nm and any(f in nm for f in frags):
            hits.append("%s@%d" % (nm, node.lineno))
    return hits


def kernel_Q():
    """constants on mu=(2,1) at (0,1), nu=(1,) at 1."""
    h_mu, h_t = Fr(3), Fr(2)
    K_mu, K_t = Fr(1, 3), Fr(1, 2)
    ray = K_mu / K_t
    n_mu, n_t = h_mu, h_t
    return dict(K_mu=K_mu, K_t=K_t, ray=ray,
                n_mu=n_mu, n_t=n_t,
                leq=K_mu <= K_t,
                norm_mu_ge=n_mu >= n_t)


def mu_onb_at(a, b, h0, z, depth):
    z = np.asarray(z, float)
    u = np.full_like(z, 1.0 / math.sqrt(h0))
    um = np.zeros_like(z)
    P = np.zeros((len(z), depth))
    P[:, 0] = u
    for i in range(depth - 1):
        r = (z - a[i]) * u - (b[i - 1] * um if i > 0 else 0.0)
        um, u = u, r / b[i]
        P[:, i + 1] = u
    return P


def tilde_onb_border(xs, ws, ys, vs, bx, by, n_upto):
    xs, ws = np.asarray(xs, float), np.asarray(ws, float)
    ys, vs = np.asarray(ys, float), np.asarray(vs, float)
    bx, by = np.asarray(bx, float), np.asarray(by, float)
    qx = np.ones_like(xs)
    qy = np.ones_like(ys)
    qb = np.ones_like(bx)
    qc = np.ones_like(by)
    qx_m = np.zeros_like(xs)
    qy_m = np.zeros_like(ys)
    qb_m = np.zeros_like(bx)
    qc_m = np.zeros_like(by)
    Ls = Ls_m = 0.0
    eta = float(np.sum(ws) - np.sum(vs))
    eta_m = eta
    nB = len(bx) + len(by)
    Q = np.zeros((nB, n_upto))
    for n in range(n_upto):
        if eta <= 0.0 or not math.isfinite(eta):
            return Q
        Q[:, n] = np.concatenate([qb, qc]) / math.sqrt(eta)
        alh = (float(np.sum(ws * xs * qx * qx)
                     - np.sum(vs * ys * qy * qy))) / eta
        if n == 0:
            px = (xs - alh) * qx
            py = (ys - alh) * qy
            pb = (bx - alh) * qb
            pc = (by - alh) * qc
        else:
            ge = (eta / eta_m) * math.exp(2.0 * (Ls - Ls_m))
            fc = math.exp(Ls_m - Ls)
            px = (xs - alh) * qx - ge * fc * qx_m
            py = (ys - alh) * qy - ge * fc * qy_m
            pb = (bx - alh) * qb - ge * fc * qb_m
            pc = (by - alh) * qc - ge * fc * qc_m
        sc = max(float(np.max(np.abs(px))), float(np.max(np.abs(py))),
                 float(np.max(np.abs(pb))), float(np.max(np.abs(pc))))
        if sc == 0.0 or not math.isfinite(sc):
            return Q
        qx_m, qy_m, qb_m, qc_m = qx, qy, qb, qc
        eta_m, Ls_m = eta, Ls
        qx, qy, qb, qc = px / sc, py / sc, pb / sc, pc / sc
        Ls += math.log(sc)
        eta = float(np.sum(ws * qx * qx) - np.sum(vs * qy * qy))
    return Q


def w9_opnorm():
    """||G||_op^2 on col(Psi) at kz9; expect 1."""
    R = PX.build_rung(9)
    mz = R["mz"]
    Nw = int(R["Nw"])
    alk = float(V.window_shape(9)[0])
    dsm = HS.window_data(9, comb=PB.smooth_comb(alk))
    xp, wp = np.asarray(mz["xp"], float), np.asarray(mz["wp"], float)
    yn, vn = np.asarray(mz["yn"], float), np.asarray(mz["vn"], float)
    bxs, bys = np.asarray(dsm["xs"], float), np.asarray(dsm["ys"], float)
    a_mu, b_mu, h0 = V.mu_chain(xp, wp, Nw)
    t = np.concatenate([bxs, bys])
    Phi = mu_onb_at(a_mu, b_mu, h0, t, Nw)
    Psi = tilde_onb_border(xp, wp, yn, vn, bxs, bys, Nw)
    Gp = Psi.T @ Psi
    M = Phi.T @ Psi
    W = np.linalg.solve(Gp, M.T)
    ev = np.linalg.eigvalsh(W.T @ W)
    return float(ev[-1])


def part_satz():
    section("S1  LEG A -- KERNEL LOEWNER OVER Q")
    t = kernel_Q()
    check("G01-kernel-Q",
          t["K_mu"] == Fr(1, 3) and t["K_t"] == Fr(1, 2)
          and t["leq"] and t["ray"] == Fr(2, 3)
          and t["norm_mu_ge"],
          "K_mu=1/3 <= K_t=1/2; ||1||_mu^2=3>=2; ray=2/3")
    check("G02-b2-le-S-Q",
          t["ray"] < Fr(1),
          "Dirac-0: ||b||^2/S=2/3<1")
    check("G03-qn-bridge-Q",
          Fr(1) + Fr(2, 3) < Fr(2),
          "if q_N<=1 then S<=B_w => gamma<=1")


def part_pins():
    section("S2  w9 / k=5 -- SATZ + q_N + op-norm")
    w = S424.chain_pack(9)
    check("G10-w9-b2-le-S",
          w["ok"] and w["gam_S"] < 1
          and abs(w["gam_S"] - W9_GAMS) <= 0.003
          and abs(w["qN"] - W9_QN) <= 0.003
          and w["qN"] < 1 and w["gam"] < 1,
          "ray=%.4f qN=%.4f gam=%.4f (S<B_w)"
          % (w["gam_S"], w["qN"], w["gam"]))
    g2sq = w9_opnorm()
    check("G11-w9-op-one",
          abs(g2sq - 1.0) <= 1e-4,
          "||G||_op^2=%.6f on col(Psi)" % g2sq)
    k5 = S424.chain_pack(17)
    check("G12-k5-tight",
          k5["ok"] and abs(k5["gam_S"] - K5_GAMS) <= 0.003
          and k5["gam_S"] <= QBAR and k5["gam_S"] >= 0.79
          and abs(k5["qN"] - K5_QN) <= 0.005
          and k5["qN"] < 0.05,
          "k=5 ray=%.4f (tight kernel); qN=%.4f (budget slack)"
          % (k5["gam_S"], k5["qN"]))
    return w, k5


def part_kills():
    section("S3  LEG D -- DEAD q_N>1 / UNNORM / SCRAMBLE")
    uu, ww, _n, _c = DMF.chi_window_comb(23, DMF.Q_CHI3)
    mz = DMF.chi_build_measures(23, uu, ww, 1.0, DMF.LPQ3)
    d23 = S424.chain_pack(23, mz=mz, chi=True, lpq=DMF.LPQ3)
    check("G20-dead-qn",
          d23["ok"] and d23["qN"] > DEAD_QN_LO
          and d23["gam_S"] < 1 and d23["gam"] < 1,
          "DEAD C3-23 qN=%.3f>1 so S>B_w; ray=%.4f "
          "still saves gamma=%.4f"
          % (d23["qN"], d23["gam_S"], d23["gam"]))
    uu4, ww4, _n4, _c4 = DMF.chi_window_comb(20, DMF.Q_CHI4)
    mz4 = DMF.chi_build_measures(20, uu4, ww4, 1.0, DMF.LPQ4)
    d20 = S424.chain_pack(20, mz=mz4, chi=True, lpq=DMF.LPQ4)
    check("G21-dead-chi4-qn",
          d20["ok"] and d20["qN"] > DEAD_QN_LO
          and d20["gam"] < 1,
          "C4-20 qN=%.3f>1 gam=%.4f" % (d20["qN"], d20["gam"]))
    w = S424.chain_pack(9)
    check("G22-unnorm",
          w["bun_gam"] >= S424.UNNORM_GAM_LO,
          "unnorm gam=%.3f>1 (SATZ needs the ONB)"
          % w["bun_gam"])
    mz_s = HM.scramble_mz()
    j1, j2 = PX.pair_select(mz_s["yn"])
    oS = FTI.cut_rung(mz_s["xu"], mz_s["wu"], mz_s["yn"], mz_s["vn"],
                       mz_s["Nw"], mz_s["S"], mz_s["L"], j1, j2)
    scr = S424.chain_pack(0, mz=mz_s)
    check("G23-scramble",
          oS["nneg"] == SCR_NNEG and (not scr.get("ok")),
          "tilde form not positive (SATZ hyp fails)")


def part_census(smoke):
    section("S4  LEG C -- CORE / SELECTED / EXT")
    if smoke:
        section("S4b  core/EXT skipped (--smoke)")
        return None
    rows = []
    for kz in V.admissible_indices():
        r = S424.chain_pack(kz)
        rows.append(r)
    check("G30-core-composed",
          len(rows) == CORE_N
          and all(r["ok"] and r["gam_S"] < 1 and r["qN"] < 1
                  and r["gam"] < 1 for r in rows)
          and max(r["gam_S"] for r in rows) <= QBAR
          and max(r["qN"] for r in rows) < 1.0,
          "42/42 b2<S and qN<1 => gamma<1 SATZ; "
          "qN[%.4f,%.4f] ray[%.3f,%.3f]"
          % (min(r["qN"] for r in rows),
             max(r["qN"] for r in rows),
             min(r["gam_S"] for r in rows),
             max(r["gam_S"] for r in rows)))
    sel = []
    for k, kz in SEL_LIVE:
        r = S424.chain_pack(kz)
        r["k"] = k
        sel.append(r)
        print("    k=%d kz%d ray=%.4f qN=%.4f gam=%.4f"
              % (k, kz, r["gam_S"], r["qN"], r["gam"]), flush=True)
    check("G31-selected",
          all(r["ok"] and r["gam_S"] <= QBAR and r["qN"] < 1
              for r in sel),
          "selected ray<=0.80 qN<1; k=8 pin gam=%.4f"
          % K8_PIN["gam"])
    ext = [S424.chain_pack(kz) for kz in ES.SAMPLE_EXT]
    check("G32-EXT",
          all(r["ok"] and r["gam_S"] < 1 and r["qN"] < 1
              and r["gam"] < 1 for r in ext),
          "EXT 6/6 composed gamma<1")
    return rows


def main():
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke

    print("=" * 78)
    print("cross_chain_gamma_probe -- "
          "PRIME.RDAGGER.CROSS_CHAIN_GAMMA.01 (round 425)")
    print("SPEC_SHA %s   (S424 %s)"
          % (SPEC_SHA[:16], S424.SPEC_SHA[:16]))
    print("mode: %s" % ("SMOKE" if smoke else
                        "FULL (core-42 + selected + EXT; k=8 pinned)"))
    print("=" * 78)

    section("S0  FIREWALL + IMPORT SHA")
    okf, det = firewall_audit()
    check("G00-firewall", okf, det)
    sha_ok = (ES.SPEC_SHA.startswith(ES_SHA_PREFIX)
              and S417.SPEC_SHA.startswith(S417_SHA_PREFIX)
              and S418.SPEC_SHA.startswith(S418_SHA_PREFIX)
              and S420.SPEC_SHA.startswith(S420_SHA_PREFIX)
              and S423.SPEC_SHA.startswith(S423_SHA_PREFIX)
              and S424.SPEC_SHA.startswith(S424_SHA_PREFIX)
              and HM.SPEC_SHA.startswith(HM_SHA_PREFIX)
              and FTI.SPEC_SHA.startswith(FTI_SHA_PREFIX)
              and DMF.SPEC_SHA.startswith(DMF_SHA_PREFIX))
    check("G00b-import-sha", sha_ok,
          "S424 %s" % S424.SPEC_SHA[:8])
    ag = antigate_fragment_audit()
    check("G00c-no-fit", not ag,
          "no fit primitives" if not ag else "; ".join(ag))

    part_satz()
    part_pins()
    part_kills()
    part_census(smoke)

    section("S5  VERDICT")
    prev_ok = all(ok for _n, ok in CHECKS)
    check("G50-verdict",
          prev_ok,
          "B2_LE_S_SATZ / QN_BRIDGES_BW / "
          "DEAD_NEEDS_SLACK / COFINAL_OPEN.  "
          "no RH / L* / R-dagger")

    n_fail = sum(1 for _n, ok in CHECKS if not ok)
    n_ok = len(CHECKS) - n_fail
    verd = ("B2_LE_S_SATZ / QN_BRIDGES_BW / "
            "DEAD_NEEDS_SLACK / COFINAL_OPEN")
    print("\nRESULT: %d/%d gates PASS   SPEC_SHA %s   (%.1fs)  %s" % (
        n_ok, len(CHECKS), SPEC_SHA[:16], time.time() - T0, verd))
    if n_fail == 0:
        print("CROSS CHAIN %sVERIFIED" % ("SMOKE " if smoke else ""))
        return 0
    print("CROSS CHAIN FAILED %d" % n_fail)
    return 1


if __name__ == "__main__":
    sys.exit(main())
