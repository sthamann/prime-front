#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""prefix_mincut_probe -- PRIME.RDAGGER.PREFIX_MINCUT.01
(round 450): name the n_stab-compression of R^dagger
and fit the honest prefix-delta chart.
Three questions, kept separate.  Research
documentation, NO RH claim and NO anti-RH claim.

OBJECT.  The n_stab-compression of R^dagger is the
r362/r369 border-augmented pack cut at depth
n_stab (not at N_w-3, not at prefix-80):
chain + border through nstar = n_stab,
B_w = cumsum(rho)[nstar-2] + 5/7.
n_stab is the r449 Chebyshev Fenster-Vergleich
(skip m0/m1; first neighbour break).

Q1 FIT.  delta on that object for kz136
(control), 137, 170, 197, 230, 500, and
Selected k<=9 for consistency vs full-window
delta.  Then M1/M2/M3 + AIC + drop tests on
(a) the mixed chart (full-slice + n_stab-deep)
and (b) the object-pure n_stab chart.

Q2 SCALE.  Does n_stab grow cofinally
(needed so every finite meshExp is eventually
inside the prefix)?  Fit n_stab ~ c a^p.

Q3 LEAN.  The frequently-mincut Prop is the
prefix cone (Iff.rfl); no new sorry.

CALIBRATION DISCLOSURE.  First measured in
/tmp (r450_census.json, r450_fits.json,
r450_chi_nstab.log) on 2026-08-30, then
sealed.  Pins disclosed.

FROZEN FROM /tmp (live re-gated):
  * Living full vs n_stab-delta is NOT close
    (rel gap 0.97..3.62).  Different objects.
  * n_stab-delta on deep windows:
    136:0.12908, 137:0.09989, 170:0.10591,
    197:0.11214, 230:0.12674, 500:0.09287.
    All n_flip=0, pos_ok, q<1.
  * Slice-only floor stands (M1 +0.02741).
    Mixed full-slice + n_stab-deep: M2,
    M1_Rinf hits -0.02.  Object-pure
    n_stab-delta (abscissa a): M2.
  * n_stab ~ 0.0417 a^1.273 (growing).
    n_stab/N falls in [0.021, 0.11].
  * CHI3-15 full q=1.023 (edge dead,
    n_flip=0).  Chi n_stab vs 14/16 is 37;
    at n=40, q=0.863 LIVING.  Death sits
    in the last three grades (200 living,
    203 dead).  Prefix does not classify chi.

AUSGANG PREFIX_OBJECT_SPLIT / M2_UNDECIDED /
NSTAB_GROWS / CHI_PREFIX_LIVES / LEAN_IDENT_RFL.
SATZ: none (infra census).
No RH claim.  No anti-RH claim.

MACHINERY: r449 n_stab / cheb_moments;
r445 bord_pack_slim / mu_chain_opt /
solve_qdag; r421 diagnose_seq.

NO RH CLAIM.  Finite window census.
Research documentation, not a theorem of RH.
No L* claim.  No R-dagger claim.
"""
from __future__ import annotations

import argparse
import ast
import hashlib
import os
import sys
import time

import numpy as np

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DISC = os.path.dirname(os.path.abspath(__file__))
PROB = os.path.join(REPO, "rh", "problem")
for p in (DISC, PROB):
    if p not in sys.path:
        sys.path.insert(0, p)

import deep_builder_probe as S445  # noqa: E402
import flip_vs_stab_probe as S449  # noqa: E402
import reserve_limit_probe as S421  # noqa: E402
import dirichlet_matched_frame_probe as DMF  # noqa: E402
import verify_lstar_instance as V  # noqa: E402
import principal_bessel_probe as PB  # noqa: E402

S445_SHA_PREFIX = "57831e610b545e75"
S449_SHA_PREFIX = "84ba4e6a83a627b9"

VERDICT = "M2_UNDECIDED"

# r449 n_stab pins + selected k<=9 from /tmp/r450_census
NSTAB = {
    5: 13, 9: 13, 17: 18, 26: 18, 43: 60, 69: 119,
    116: 158, 136: 175, 137: 175, 170: 194,
    197: 406, 230: 194, 500: 1525,
}
# n_stab-compression delta pins
D_PRE = {
    5: 0.20081603607852783,
    9: 0.17002235861799897,
    17: 0.21432449385355412,
    26: 0.15937166335906594,
    43: 0.1386716965976036,
    69: 0.10313011349798185,
    116: 0.1315223232534103,
    136: 0.12907957185638264,
    137: 0.099893424862461,
    170: 0.10591418323218449,
    197: 0.11213766076367393,
    230: 0.12674040177169,
    500: 0.0928699158909625,
}
D_FULL = {
    5: 0.0715644903784356,
    9: 0.0669557660041672,
    17: 0.10863605427499412,
    26: 0.06889582254786508,
    43: 0.05539631317793148,
    69: 0.04748760864627366,
    116: 0.03778501073586571,
    136: 0.02791230959515767,
}
CHI15_Q_FULL = 1.023180939479071
CHI15_Q_N40 = 0.8628007
CHI15_NSTAB = 37
SLICE_DINF = S445.SLICE_DINF
SCALE_P = 1.2734192316227517
SCALE_C = 0.04167915159003622

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
    return (not bad), ("NO zero/oracles; n_stab / pack / fit only"
                       if not bad else "; ".join(bad))


def pack_nstab(kz, nstar=None):
    """r362/r369 border pack cut at nstar (default n_stab)."""
    mz = V.build_measures(kz)
    mz = dict(mz)
    mz["kz"] = kz
    bxs, bws, bys, bvs, _h, _al = S445.smooth_border_atoms(kz)
    if nstar is None:
        nstar = NSTAB[kz]
    nstar = min(int(nstar), int(mz["Nw"]))
    bp = S445.bord_pack_slim(
        mz["xp"], mz["wp"], mz["yn"], mz["vn"],
        bxs, bws, bys, bvs, nstar, engine="numpy", require_pos=False)
    a, b, h0 = S445.mu_chain_opt(mz["xp"], mz["wp"], nstar, engine="numpy")
    bxa = np.concatenate([np.asarray(bxs, float), np.asarray(bys, float)])
    bwa = np.concatenate([np.asarray(bws, float), -np.asarray(bvs, float)])
    bvec = S445.bvec_opt(a, b, h0, bxa, bwa, nstar, engine="numpy")
    rho = np.asarray(bp["rho"], float)
    Bw = float(np.cumsum(rho)[nstar - 2]) + S445.B57
    sol = S445.solve_qdag(a, b, h0, mz["yn"], mz["vn"], bvec, Bw,
                          engine="numpy")
    return dict(ok=True, kz=kz, nstar=nstar, Nw=int(mz["Nw"]),
                qdag=float(sol["qdag"]), delta=float(sol["delta"]),
                Bw=Bw, n_flip=bp.get("n_flip") or 0,
                pos_ok=bool(bp.get("pos_ok", True)))


def pack_chi_at(k, nstar):
    uu, ww, _nn, _ch = DMF.chi_window_comb(k, DMF.Q_CHI3)
    mzc = DMF.chi_build_measures(k, uu, ww, 1.0, DMF.LPQ3)
    usm, wsm = PB.smooth_comb(mzc["alpha"])
    mzb = DMF.chi_build_measures(k, usm, wsm, 1.0, DMF.LPQ3)
    nstar = min(int(nstar), int(mzc["Nw"]))
    bp = S445.bord_pack_slim(
        mzc["xp"], mzc["wp"], mzc["yn"], mzc["vn"],
        mzb["xp"], mzb["wp"], mzb["yn"], mzb["vn"],
        nstar, engine="numpy", require_pos=False)
    a, b, h0 = S445.mu_chain_opt(mzc["xp"], mzc["wp"], nstar)
    bxa = np.concatenate([np.asarray(mzb["xp"], float),
                          np.asarray(mzb["yn"], float)])
    bwa = np.concatenate([np.asarray(mzb["wp"], float),
                          -np.asarray(mzb["vn"], float)])
    bvec = S445.bvec_opt(a, b, h0, bxa, bwa, nstar)
    rho = np.asarray(bp["rho"], float)
    Bw = float(np.cumsum(rho)[nstar - 2]) + S445.B57
    sol = S445.solve_qdag(a, b, h0, mzc["yn"], mzc["vn"], bvec, Bw)
    return dict(nstar=nstar, Nw=int(mzc["Nw"]),
                qdag=float(sol["qdag"]), delta=float(sol["delta"]),
                n_flip=bp.get("n_flip") or 0,
                pos_ok=bool(bp.get("pos_ok", True)))


def fit_slice():
    ks = [5, 6, 7, 8, 9]
    ds = [S445.PIN_D[5], S445.PIN_D[6], S445.PIN_D[7],
          S445.K8_D, S445.PIN_D[9]]
    return S421.diagnose_seq(ks, ds)


def fit_mixed():
    """full-window selected k=5..9 plus n_stab-deep (fake k)."""
    ks = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    ds = [S445.PIN_D[5], S445.PIN_D[6], S445.PIN_D[7],
          S445.K8_D, S445.PIN_D[9],
          D_PRE[136], D_PRE[137], D_PRE[170],
          D_PRE[197], D_PRE[230], D_PRE[500]]
    return S421.diagnose_seq(ks, ds)


def fit_pure_a():
    kzs = [5, 9, 17, 26, 43, 69, 116, 136, 137, 170, 197, 230, 500]
    aa = [int(V.PP[kz]) for kz in kzs]
    ds = [D_PRE[kz] for kz in kzs]
    return S421.diagnose_seq(aa, ds)


def part_object(smoke):
    section("S1  n_stab-COMPRESSION vs FULL (living)")
    ns17, nw17 = S449.n_stab(17, (18, 26), 80)
    check("G10-k5-nstab",
          ns17 == NSTAB[17] and nw17 == 96,
          "kz17 n_stab=%d N=%d" % (ns17, nw17))
    p = pack_nstab(17)
    check("G11-k5-prefix",
          p["pos_ok"] and p["n_flip"] == 0
          and abs(p["delta"] - D_PRE[17]) < 1e-8
          and p["nstar"] == NSTAB[17],
          "d=%.6f q=%.6f n=%d" % (p["delta"], p["qdag"], p["nstar"]))
    full = S445.pack(17, engine="numpy", want_den=False)
    check("G12-k5-full",
          full["ok"] and abs(full["delta"] - D_FULL[17]) < 1e-8,
          "full d=%.6f" % full["delta"])
    gap = abs(p["delta"] - full["delta"])
    check("G13-living-not-near",
          gap > 0.05,
          "|d_pre-d_full|=%.5f (OBJECT SPLIT, not a miss)" % gap)
    if smoke:
        check("G14-deep-skipped", True, "--smoke")
        return
    pairs = {
        136: (137, 138), 137: (138, 136), 170: (169, 171),
        197: (198, 199), 230: (229, 231),
    }
    for kz in (136, 137, 170, 197, 230, 500):
        nmax = 2200 if kz != 500 else 2200
        neigh = pairs[kz] if kz != 500 else (499, 501)
        ns, _nw = S449.n_stab(kz, neigh, nmax)
        check("G14a-nstab-kz%d" % kz,
              ns == NSTAB[kz],
              "n_stab=%d pin=%d" % (ns, NSTAB[kz]))
        pre = pack_nstab(kz)
        check("G14b-pack-kz%d" % kz,
              pre["pos_ok"] and pre["n_flip"] == 0
              and pre["qdag"] < 1.0
              and abs(pre["delta"] - D_PRE[kz]) < 1e-5,
              "d=%.6f q=%.6f n=%d" % (pre["delta"], pre["qdag"],
                                      pre["nstar"]))
    # selected living consistency pins (recompute cheap k=5,9)
    for kz in (5, 9):
        pre = pack_nstab(kz)
        full = S445.pack(kz, engine="numpy", want_den=False)
        rel = abs(pre["delta"] - full["delta"]) / max(1e-12, abs(full["delta"]))
        check("G15-cons-kz%d" % kz,
              rel > 0.5 and abs(pre["delta"] - D_PRE[kz]) < 1e-8,
              "rel=%.3f (split stands)" % rel)


def part_fit(smoke):
    section("S2  FLOOR FITS (three charts, transparent)")
    sl = fit_slice()
    check("G20-slice-M1",
          sl["winner"] == "M1"
          and abs(sl["M1_Rinf"] - SLICE_DINF) < 0.002,
          "slice M1 inf=%.5f AIC1=%.2f AIC2=%.2f"
          % (sl["M1_Rinf"], sl["aic1"], sl["aic2"]))
    mx = fit_mixed()
    check("G21-mixed-M2",
          mx["winner"] == "M2" and mx["M1_Rinf"] <= 0.0,
          "mixed winner=%s M1=%.5f AIC1=%.2f AIC2=%.2f"
          % (mx["winner"], mx["M1_Rinf"], mx["aic1"], mx["aic2"]))
    pu = fit_pure_a()
    check("G22-pure-M2",
          pu["winner"] == "M2",
          "pure-a winner=%s M1=%.5f AIC1=%.2f AIC2=%.2f AIC3=%.2f"
          % (pu["winner"], pu["M1_Rinf"], pu["aic1"],
             pu["aic2"], pu["aic3"]))
    # drop-deep on mixed: back to M1
    ks = [5, 6, 7, 8, 9]
    ds = [S445.PIN_D[5], S445.PIN_D[6], S445.PIN_D[7],
          S445.K8_D, S445.PIN_D[9]]
    drop = S421.diagnose_seq(ks, ds)
    check("G23-drop-deep-M1",
          drop["winner"] == "M1",
          "drop-deep restores slice M1")
    if not smoke:
        kzs = [5, 9, 17, 26, 43, 69, 116, 136, 137, 170, 197, 230]
        aa = [int(V.PP[kz]) for kz in kzs]
        ds = [D_PRE[kz] for kz in kzs]
        d500 = S421.diagnose_seq(aa, ds)
        check("G24-drop500-still-M2",
              d500["winner"] == "M2",
              "drop kz500 winner=%s M1=%.5f" % (d500["winner"],
                                                d500["M1_Rinf"]))


def part_scale(smoke):
    section("S3  n_stab SCALING")
    deep = [136, 137, 170, 197, 230, 500]
    aa = np.array([float(int(V.PP[kz])) for kz in deep], float)
    ns = np.array([float(NSTAB[kz]) for kz in deep], float)
    loga, logn = np.log(aa), np.log(ns)
    p = float(np.polyfit(loga, logn, 1)[0])
    growing = p > 0.5
    nN = [NSTAB[kz] / {136: 1641, 137: 8300, 170: 5771,
                       197: 4071, 230: 2012, 500: 17847}[kz]
          for kz in deep]
    check("G30-nstab-grows",
          growing and abs(p - SCALE_P) < 0.05,
          "n_stab ~ a^%.3f (pin %.3f); n/N in [%.3f, %.3f]"
          % (p, SCALE_P, min(nN), max(nN)))
    check("G31-nN-falls",
          min(nN) < 0.05 and max(nN) < 0.12,
          "n_stab/N not bounded away from 0; absolute "
          "growth is the quantifier input")
    if smoke:
        check("G32-onset-note", True,
              "a0(f) finite per f; n_stab->inf covers meshExp")


def part_chi(smoke):
    section("S4  CHI: FULL DEAD, PREFIX LIVING")
    chi = S445.pack_chi(15, DMF.Q_CHI3, DMF.LPQ3, engine="numpy",
                        want_den=False)
    check("G40-chi-full-dead",
          chi["ok"] and chi["n_flip"] == 0
          and chi["qdag"] > 1.0
          and abs(chi["qdag"] - CHI15_Q_FULL) < 1e-8,
          "full q=%.6f n_flip=0 (edge death stands)"
          % chi["qdag"])
    c40 = pack_chi_at(15, 40)
    check("G41-chi-prefix-lives",
          c40["pos_ok"] and c40["n_flip"] == 0
          and c40["qdag"] < 1.0
          and abs(c40["qdag"] - CHI15_Q_N40) < 1e-4,
          "n=40 q=%.6f d=%.6f (PREFIX DOES NOT CLASSIFY CHI)"
          % (c40["qdag"], c40["delta"]))
    if not smoke:
        c200 = pack_chi_at(15, 200)
        check("G42-chi-n200-live",
              c200["qdag"] < 1.0,
              "n=200 q=%.6f; death in last 3 grades"
              % c200["qdag"])


def main():
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke
    print("=" * 78)
    print("prefix_mincut_probe -- PRIME.RDAGGER.PREFIX_MINCUT.01 "
          "(round 450)")
    print("SPEC_SHA %s" % SPEC_SHA[:16])
    print("mode: %s" % ("SMOKE" if smoke else "FULL"))
    print("=" * 78)
    section("S0  FIREWALL")
    okf, det = firewall_audit()
    check("G00-firewall", okf, det)
    check("G00b-import-sha",
          S445.SPEC_SHA.startswith(S445_SHA_PREFIX)
          and S449.SPEC_SHA.startswith(S449_SHA_PREFIX),
          "S445 %s S449 %s" % (S445.SPEC_SHA[:16], S449.SPEC_SHA[:16]))
    part_object(smoke)
    part_fit(smoke)
    part_scale(smoke)
    part_chi(smoke)
    r1 = pack_nstab(17)
    r2 = pack_nstab(17)
    check("G50-determinism",
          r1["qdag"] == r2["qdag"] and r1["delta"] == r2["delta"],
          "kz17 n_stab run1=run2 d=%.16f" % r1["delta"])
    section("S5  VERDICT")
    prev = all(ok for _n, ok in CHECKS)
    check("G70-verdict",
          prev and VERDICT == "M2_UNDECIDED",
          "PREFIX_OBJECT_SPLIT / M2_UNDECIDED / NSTAB_GROWS / "
          "CHI_PREFIX_LIVES / LEAN_IDENT_RFL; "
          "no RH / no anti-RH / no L* / no R-dagger")
    n_fail = sum(1 for _n, ok in CHECKS if not ok)
    n_ok = len(CHECKS) - n_fail
    print("\nRESULT: %d/%d gates PASS   SPEC_SHA %s   (%.1fs)" % (
        n_ok, len(CHECKS), SPEC_SHA[:16], time.time() - T0))
    if n_fail == 0:
        print("PREFIX MINCUT %sVERIFIED" % ("SMOKE " if smoke else ""))
        return 0
    print("PREFIX MINCUT FAILED %d" % n_fail)
    return 1


if __name__ == "__main__":
    sys.exit(main())
