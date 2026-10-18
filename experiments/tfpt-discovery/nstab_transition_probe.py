#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""nstab_transition_probe -- PRIME.RDAGGER.NSTAB_TRANSITION.01
(round 451): what changes at n_stab?
Exactly the transition anatomy.  Research
documentation, NO RH claim and NO anti-RH claim.

THE QUESTION.  The Prefix Stability Theorem
candidate needs a property that is stable on
the early chain and MAY be lost later.
r449 located n_stab (Chebyshev Fenster-
Vergleich).  This round asks which of three
single-window objects kinks there:
  (1) OP conditioning / Christoffel regime,
  (2) fold-atom resolution n_res,
  (3) Schur/Redheffer energy q^dagger_n.

DEFINITIONS (source-pure, no fit dof).
  n_stab: r449 method, skip m0/m1, first
    neighbour break, eps-robust.
  n_res: folded mu-atoms x_i in [-1,1];
    theta_i = arccos(x_i); n_res = pi / min
    consecutive Delta theta.  On the cosine
    grid of the fold this equals L/2.
  q^dagger_n: r362/r369 pack cut at depth n
    (chain + border; B_w = cumsum(rho)[n-2]
    + 5/7).
  n_qbreak: first n > n_ref with
    |q_n - q_ref| > 1e-4.

CALIBRATION DISCLOSURE.  First measured in
/tmp (r451_diag.json, r451_diag2.json,
r451_diag3.json, r451_diag4.json,
r451_diag5.json) on 2026-08-30, then sealed.
Pins disclosed.

FROZEN FROM /tmp (live re-gated):
  * n_stab reproduced (r449 pins):
    kz17:18; 136:175; 137:175; 170:194;
    197:406; 230:194; 500:1525.  Selected
    5:13, 9:13, 26:46, 43:60, 69:119,
    116:158.  eps-cuts identical 1e-6..1e-2.
  * n_res = L/2 (regular Chebyshev grid).
    n_stab/n_res in [0.010, 0.094] on every
    measured window.  RES_MISMATCH.
  * Conditioning: beta_n stays ~1/2 through
    n_stab; n*lambda_n(0) O(1); no slope-
    cliff at n_stab (smooth Chebyshev
    regime; discrete near-singularity only
    near n_mu >> n_stab).
  * q^dagger_n is CONSTANT on n <= n_stab
    (plateau std < 1e-4) on EVERY window,
    including kz137/170/500.  PREFIX_Q_
    PLATEAU.  Exit is NOT universal:
    CLIFF at n_stab+1 on {17,116,136,197,
    230,500}; DELAYED on {5,9,26,43};
    CONTINUES past 2 n_stab on {69,137,170}.
  * SCRAMBLE (theta-jitter, seed 451, kz17):
    n_stab -> 2, n_res blows up, q plateau
    dies (std ~ 0.1, q exceeds 1).  The
    plateau is construction-specific; n_res
    is support geometry.
  * dps: Gram residuals 1e-16..1e-14 on
    the q-solve through n_stab (kz500 float
    residual 1.5e-15 at n=1525).  Jump is
    not an ill-conditioned artefact.

AUSGANG TRANSITION_SMOOTH / RES_MISMATCH /
PREFIX_Q_PLATEAU.
n_stab is a sufficient operational cut for
the Schur plateau, not a universal mechanical
cliff of the three single-window objects.
SATZ: none (infra census).
No RH claim.  No anti-RH claim.

MACHINERY: r449 n_stab / cheb_moments;
r445 bord_pack_slim / mu_chain_opt /
solve_qdag; r446 load_atoms.

NO RH CLAIM.  Finite window census.
Research documentation, not a theorem of RH.
No L* claim.  No R-dagger claim.
"""
from __future__ import annotations

import argparse
import ast
import hashlib
import math
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
import verify_lstar_instance as V  # noqa: E402

S445_SHA_PREFIX = "57831e610b545e75"
S449_SHA_PREFIX = "84ba4e6a83a627b9"

VERDICT = "TRANSITION_SMOOTH"
VERDICT_RES = "RES_MISMATCH"
VERDICT_Q = "PREFIX_Q_PLATEAU"

# r449 n_stab pins + selected (same method)
NSTAB = {
    5: 13, 9: 13, 17: 18, 26: 46, 43: 60, 69: 119,
    116: 158, 136: 175, 137: 175, 170: 194,
    197: 406, 230: 194, 500: 1525,
}
NEIGH = {
    5: (6, 7), 9: (10, 11), 17: (18, 26), 26: (27, 28),
    43: (44, 45), 69: (70, 71), 116: (117, 118),
    136: (137, 138), 137: (138, 136), 170: (169, 171),
    197: (198, 199), 230: (229, 231), 500: (499, 501),
}
# n_res = pi / min Delta theta  (equals L/2 on the grid)
NRES = {
    5: 143.0, 9: 367.0, 17: 191.0, 26: 727.0, 43: 1677.0,
    69: 11379.0, 116: 2865.0, 136: 3281.0, 137: 16599.0,
    170: 11541.0, 197: 8141.0, 230: 4023.0, 500: 35693.0,
}
# q at n_stab (plateau value)
Q_NS = {
    5: 0.79918396, 9: 0.82997764, 17: 0.78567551,
    26: 0.84062889, 43: 0.86132830, 69: 0.89686989,
    116: 0.86847768, 136: 0.87092043, 137: 0.90010658,
    170: 0.89408582, 197: 0.88786234, 230: 0.87325960,
    500: 0.90713008,
}
# n_qbreak; 0 means continues past the scanned range
QBREAK = {
    5: 24, 9: 46, 17: 19, 26: 60, 43: 119, 69: 0,
    116: 159, 136: 176, 137: 0, 170: 0,
    197: 407, 230: 195, 500: 1526,
}
CLIFF = (17, 116, 136, 197, 230, 500)
DELAYED = (5, 9, 26, 43)
CONTINUES = (69, 137, 170)
Q_BAR = 1e-4
SCRAMBLE_SEED = 451

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
    return (not bad), ("NO zero/oracles; n_stab / OP / pack only"
                       if not bad else "; ".join(bad))


def n_res_th(xp):
    """Nyquist of folded mu-atoms in Chebyshev angle.
    Source-pure: pi / min consecutive Delta theta."""
    th = np.sort(np.arccos(np.clip(np.unique(np.asarray(xp, float)),
                                   -1.0, 1.0)))
    if len(th) < 2:
        return float("nan")
    d = np.diff(th)
    dmin = float(d.min())
    if dmin <= 0.0:
        return float("inf")
    return math.pi / dmin


def n_res_of(kz):
    mz = dict(V.build_measures(kz))
    nr = n_res_th(mz["xp"])
    return nr, int(mz["L"]) / 2.0, int(mz["Nw"]), mz


def pack_at(mz, nstar, border):
    bxs, bws, bys, bvs = border
    nstar = min(int(nstar), int(mz["Nw"]))
    if nstar < 4:
        return dict(ok=False, nstar=nstar, qdag=float("nan"),
                    delta=float("nan"), residual=float("inf"))
    bp = S445.bord_pack_slim(
        mz["xp"], mz["wp"], mz["yn"], mz["vn"],
        bxs, bws, bys, bvs, nstar, engine="numpy", require_pos=False)
    if bp.get("rho") is None:
        return dict(ok=False, nstar=nstar, qdag=float("nan"),
                    delta=float("nan"), residual=float("inf"),
                    n_flip=bp.get("n_flip"))
    a, b, h0 = S445.mu_chain_opt(mz["xp"], mz["wp"], nstar, engine="numpy")
    bxa = np.concatenate([np.asarray(bxs, float), np.asarray(bys, float)])
    bwa = np.concatenate([np.asarray(bws, float), -np.asarray(bvs, float)])
    bvec = S445.bvec_opt(a, b, h0, bxa, bwa, nstar, engine="numpy")
    rho = np.asarray(bp["rho"], float)
    Bw = float(np.cumsum(rho)[nstar - 2]) + S445.B57
    sol = S445.solve_qdag(a, b, h0, mz["yn"], mz["vn"], bvec, Bw,
                          engine="numpy")
    return dict(ok=True, nstar=int(nstar), qdag=float(sol["qdag"]),
                delta=float(sol["delta"]),
                residual=float(sol["residual"]),
                n_flip=bp.get("n_flip") or 0,
                pos_ok=bool(bp.get("pos_ok", True)),
                form=sol.get("form"))


def christoffel_at(a, b, h0, x, n):
    s0 = math.sqrt(h0)
    p = 1.0 / s0
    pm = 0.0
    acc = p * p
    for i in range(n - 1):
        if i == 0:
            r = (x - a[i]) * p
        else:
            r = (x - a[i]) * p - b[i - 1] * pm
        pm, p = p, r / b[i]
        acc += p * p
    return 1.0 / acc if acc > 0 else float("nan")


def cond_kink_at(mz, ns, n_hi=None):
    """Does |beta-1/2| or n*lambda_n(0) cliff at n_stab?
    Sharp := second-diff peak within 15% of n_stab AND
    |slope_post/slope_pre| > 4."""
    Nw = int(mz["Nw"])
    if n_hi is None:
        n_hi = min(Nw - 3, max(int(ns * 1.4) + 20, ns + 40), 900)
    n_hi = max(n_hi, min(Nw - 3, ns + 20))
    a, b, h0 = S445.mu_chain_opt(mz["xp"], mz["wp"], n_hi, engine="numpy")
    nn = np.arange(8, n_hi)
    if len(nn) < 8:
        return dict(sharp=False, rel_peak=float("nan"), ratio=float("nan"),
                    n_hi=n_hi, beta_ns=float("nan"), nlam_ns=float("nan"))
    y = np.log(np.maximum(np.abs(np.asarray(b[8:n_hi], float) - 0.5),
                          1e-16))
    pre = nn < 0.85 * ns
    post = nn > 1.15 * ns
    def sl(m):
        if int(m.sum()) < 4:
            return float("nan")
        return float(np.polyfit(nn[m], y[m], 1)[0])
    sp, so = sl(pre), sl(post)
    ratio = (abs(so / sp)
             if (sp == sp and so == so and abs(sp) > 1e-18)
             else float("nan"))
    d2 = np.abs(np.diff(y, 2))
    ipeak = int(np.nanargmax(d2)) + 1 if len(d2) else 0
    npeak = float(nn[ipeak]) if len(nn) else float("nan")
    rel = abs(npeak - ns) / ns if ns else float("nan")
    lam = christoffel_at(a, b, h0, 0.0, min(ns, n_hi))
    sharp = (rel == rel and rel < 0.15
             and ratio == ratio and ratio > 4.0)
    return dict(sharp=bool(sharp), rel_peak=rel, ratio=ratio,
                n_hi=n_hi, beta_ns=float(b[min(ns, n_hi) - 1]),
                nlam_ns=float(ns * lam) if lam == lam else float("nan"))


def scramble_mz(mz, seed=SCRAMBLE_SEED):
    rng = np.random.RandomState(seed)
    out = dict(mz)
    th = np.arccos(np.clip(mz["xp"], -1.0, 1.0))
    thy = np.arccos(np.clip(mz["yn"], -1.0, 1.0))
    out["xp"] = np.cos(np.mod(th + rng.uniform(0.3, 1.2, size=th.shape),
                              math.pi))
    out["yn"] = np.cos(np.mod(thy + rng.uniform(0.3, 1.2, size=thy.shape),
                              math.pi))
    return out


def cheb_moments_xy(xs, ws, ys, vs, nmax):
    xs, ws, ys, vs = (np.asarray(a, float) for a in (xs, ws, ys, vs))
    t0x, t1x = np.ones_like(xs), xs.copy()
    t0y, t1y = np.ones_like(ys), ys.copy()
    out = [float(ws.sum() - vs.sum()),
           float((ws * xs).sum() - (vs * ys).sum())]
    for _n in range(2, nmax):
        t2x = 2.0 * xs * t1x - t0x
        t2y = 2.0 * ys * t1y - t0y
        out.append(float((ws * t2x).sum() - (vs * t2y).sum()))
        t0x, t1x = t1x, t2x
        t0y, t1y = t1y, t2y
    return np.asarray(out, float)


def n_stab_scrambled(mz_s, k2, nmax=80, eps=1e-4):
    m_s = cheb_moments_xy(mz_s["xp"], mz_s["wp"], mz_s["yn"], mz_s["vn"],
                          nmax)
    m2, _ = S449.load_mom(k2, nmax)
    return S449.agree_from2(m_s, m2, eps)


def q_on_grid(mz, border, depths):
    rows = []
    for n in depths:
        p = pack_at(mz, int(n), border)
        rows.append(p)
    return rows


def part_nstab(smoke):
    section("S1  n_stab REPRODUCED (r449 method)")
    ns17, nw17 = S449.n_stab(17, NEIGH[17], 80)
    check("G10-k5-nstab",
          ns17 == NSTAB[17] and nw17 == 96,
          "kz17 n_stab=%d pin=%d N=%d" % (ns17, NSTAB[17], nw17))
    m17, _ = S449.load_mom(17, 80)
    m18, _ = S449.load_mom(18, 80)
    cuts = [S449.agree_from2(m17, m18, e)
            for e in (1e-6, 1e-5, 1e-4, 1e-3, 1e-2)]
    check("G11-eps-robust",
          len(set(cuts)) == 1 and cuts[0] == NSTAB[17],
          "kz17-18 cut=%s identical 1e-6..1e-2" % cuts[0])
    keys = (17,) if smoke else (
        5, 9, 17, 26, 43, 69, 116, 136, 137, 170, 197, 230, 500)
    for kz in keys:
        nmax = 80 if (smoke or kz < 40) else 2200
        ns, Nw = S449.n_stab(kz, NEIGH[kz], nmax)
        pin = NSTAB[kz]
        ok = ns == pin if nmax >= pin else (ns >= nmax or ns == pin)
        check("G12-nstab-kz%d" % kz, ok,
              "n_stab=%d pin=%d N=%d" % (ns, pin, Nw))


def part_nres(smoke):
    section("S2  SUPPORT RESOLUTION  n_res vs n_stab")
    keys = (17, 136) if smoke else (
        5, 9, 17, 26, 43, 69, 116, 136, 137, 170, 197, 230, 500)
    ratios = []
    for kz in keys:
        nr, ngrid, Nw, _mz = n_res_of(kz)
        pin = NRES[kz]
        ns = NSTAB[kz]
        ratio = ns / nr if nr else float("nan")
        ratios.append(ratio)
        check("G20-nres-kz%d" % kz,
              abs(nr - pin) < 0.6 and abs(nr - ngrid) < 0.6
              and ratio < 0.12 and ratio > 0.005,
              "n_res=%.1f pin=%.1f grid=%.1f n_stab=%d ratio=%.4f N=%d"
              % (nr, pin, ngrid, ns, ratio, Nw))
    check("G21-res-mismatch",
          VERDICT_RES == "RES_MISMATCH"
          and max(ratios) < 0.12 and min(ratios) > 0.005,
          "n_stab/n_res in [%.4f, %.4f] -- never ~1"
          % (min(ratios), max(ratios)))


def part_cond(smoke):
    section("S3  CONDITIONING / CHRISTOFFEL (no cliff)")
    keys = (17,) if smoke else (17, 136, 137, 197)
    any_sharp = False
    for kz in keys:
        mz = dict(V.build_measures(kz))
        mz["kz"] = kz
        ck = cond_kink_at(mz, NSTAB[kz])
        any_sharp = any_sharp or ck["sharp"]
        check("G30-cond-smooth-kz%d" % kz,
              (not ck["sharp"])
              and ck["nlam_ns"] == ck["nlam_ns"]
              and 0.5 < ck["nlam_ns"] < 20.0
              and 0.3 < ck["beta_ns"] < 0.7,
              "sharp=%s rel_peak=%.3f ratio=%.3g beta=%.4f n*lam=%.3f"
              % (ck["sharp"], ck["rel_peak"], ck["ratio"],
                 ck["beta_ns"], ck["nlam_ns"]))
    check("G31-no-cond-cliff",
          not any_sharp,
          "OP stays Chebyshev through n_stab; no near-singularity")


def part_schur(smoke):
    section("S4  SCHUR q^dagger_n  (plateau; exit not universal)")
    keys = (17,) if smoke else (
        5, 9, 17, 26, 43, 69, 116, 136, 137, 170, 197, 230, 500)
    plateau_ok = True
    for kz in keys:
        mz = dict(V.build_measures(kz))
        mz["kz"] = kz
        border = S445.smooth_border_atoms(kz)[:4]
        ns = NSTAB[kz]
        nref = max(8, min(ns, 20 if smoke else 40))
        depths = sorted(set([
            nref, max(8, ns // 2), max(8, ns - 1), ns,
            min(int(mz["Nw"]) - 3, ns + 1),
        ]))
        rows = q_on_grid(mz, border, depths)
        byn = {r["nstar"]: r for r in rows if r.get("ok")}
        qns = byn.get(ns, {}).get("qdag", float("nan"))
        qref = byn.get(nref, {}).get("qdag", qns)
        pre = [r["qdag"] for r in rows
               if r.get("ok") and r["nstar"] <= ns]
        std = float(np.std(pre)) if len(pre) >= 2 else 0.0
        pinq = Q_NS[kz]
        live = (abs(qns - pinq) < 1e-6
                and std < Q_BAR
                and qns < 1.0
                and byn.get(ns, {}).get("residual", 1.0) < 1e-10)
        plateau_ok = plateau_ok and live
        qp1 = byn.get(ns + 1, {}).get("qdag")
        dq1 = (abs(qp1 - qref) if qp1 is not None else float("nan"))
        nb_pin = QBREAK[kz]
        if kz in CLIFF:
            cliff_ok = dq1 > Q_BAR and (nb_pin in (ns + 1, ns + 2))
        elif kz in DELAYED:
            cliff_ok = (nb_pin > ns + 5)
            # smoke: only check plateau, not the delayed exit
            if smoke:
                cliff_ok = True
        else:
            # CONTINUES: no break at n_stab+1
            cliff_ok = (not (dq1 == dq1 and dq1 > Q_BAR)) or smoke
            if not smoke:
                cliff_ok = dq1 == dq1 and dq1 <= Q_BAR and nb_pin == 0
        check("G40-q-kz%d" % kz,
              live and cliff_ok,
              "q*=%.8f std=%.2e dq+1=%.3e class=%s res=%.1e"
              % (qns, std, dq1,
                 ("CLIFF" if kz in CLIFF else
                  "DELAYED" if kz in DELAYED else "CONTINUES"),
                 byn.get(ns, {}).get("residual", float("nan"))))
    check("G41-prefix-plateau",
          plateau_ok and VERDICT_Q == "PREFIX_Q_PLATEAU",
          "q^dagger_n constant on n<=n_stab of every measured window")
    if smoke:
        # kz17 is the CLIFF prototype
        mz = dict(V.build_measures(17))
        mz["kz"] = 17
        border = S445.smooth_border_atoms(17)[:4]
        p19 = pack_at(mz, 19, border)
        check("G42-kz17-cliff",
              abs(p19["qdag"] - 0.83731872) < 1e-6
              and QBREAK[17] == 19,
              "n=19 q=%.8f (jump off the 0.785675 plateau)"
              % p19["qdag"])
    else:
        check("G42-subset-cliff",
              all(QBREAK[kz] in (NSTAB[kz] + 1, NSTAB[kz] + 2)
                  for kz in CLIFF),
              "CLIFF subset {17,116,136,197,230,500} at n_stab+1/+2")


def part_scramble(smoke):
    section("S5  SCRAMBLE (theta-jitter, seed 451)")
    mz = dict(V.build_measures(17))
    mz["kz"] = 17
    mz_s = scramble_mz(mz)
    br = n_stab_scrambled(mz_s, 18, 80)
    nr_s = n_res_th(mz_s["xp"])
    nr_live = NRES[17]
    check("G50-scr-nstab-collapses",
          br <= 3,
          "scramble n_stab=%d (live 18)" % br)
    check("G50b-scr-nres-not-nstab",
          nr_s > 10 * max(br, 1) and nr_s != nr_live,
          "scramble n_res=%.1f (live %.1f); still RES_MISMATCH"
          % (nr_s, nr_live))
    border = S445.smooth_border_atoms(17)[:4]
    depths = list(range(8, 19)) if not smoke else [8, 12, 16, 18]
    qs = [pack_at(mz_s, n, border)["qdag"] for n in depths]
    std = float(np.std(qs))
    qmax = float(np.max(qs))
    check("G51-scr-q-not-plateau",
          std > 0.01 and qmax > 0.95,
          "scramble q std=%.3f max=%.3f (live std 6e-6, q=0.786)"
          % (std, qmax))
    check("G52-scr-kills-construction",
          br <= 3 and std > 0.01,
          "plateau is fold-arithmetic, not generic OP of 138 atoms")


def main():
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke
    print("=" * 78)
    print("nstab_transition_probe -- PRIME.RDAGGER.NSTAB_TRANSITION.01 "
          "(round 451)")
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
    part_nstab(smoke)
    part_nres(smoke)
    part_cond(smoke)
    part_schur(smoke)
    part_scramble(smoke)
    r1 = S445.pack(17, engine="numpy", want_den=False)
    r2 = S445.pack(17, engine="numpy", want_den=False)
    check("G60-determinism",
          r1["qdag"] == r2["qdag"],
          "k=5 run1=run2 q=%.16f" % r1["qdag"])
    section("S6  VERDICT")
    prev = all(ok for _n, ok in CHECKS)
    check("G70-verdict",
          prev and VERDICT == "TRANSITION_SMOOTH"
          and VERDICT_RES == "RES_MISMATCH"
          and VERDICT_Q == "PREFIX_Q_PLATEAU",
          "TRANSITION_SMOOTH / RES_MISMATCH / PREFIX_Q_PLATEAU; "
          "no RH / no anti-RH / no L* / no R-dagger")
    n_fail = sum(1 for _n, ok in CHECKS if not ok)
    n_ok = len(CHECKS) - n_fail
    print("\nRESULT: %d/%d gates PASS   SPEC_SHA %s   (%.1fs)" % (
        n_ok, len(CHECKS), SPEC_SHA[:16], time.time() - T0))
    if n_fail == 0:
        print("NSTAB TRANSITION %sVERIFIED" % ("SMOKE " if smoke else ""))
        return 0
    print("NSTAB TRANSITION FAILED %d" % n_fail)
    return 1


if __name__ == "__main__":
    sys.exit(main())
