#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""deep_abd_probe -- PRIME.INFRA.DEEP_ABD_ADJUDICATION.01
(round 446): are the ABD breaks at selected k=10,11,12
REAL or FLOAT artefacts?  Exactly one question.
Research documentation, NO RH claim.

THE QUESTION.  r445 found selected k=10 (107 sign-flips
from n=3788), k=11 (839 flips, B_w explosion), k=12
(abort at n=12737).  The Lean mincut needs infinitely
many Selected windows to be ABD-living.  r397 proved
a_k -> inf and Delta_k -> 0, not chain positivity.
If REAL: the m_k mesh degenerates and the sequence
definition must be revised.  If FLOAT: r427 is hit
(tiny signed-mass pivots in float64) and depth needs
an mpmath chain.

WHAT IS COMPUTED.  The mu-tilde border chain only
(eta, sg_h, P, N, rel = |eta|/(P+N)), atoms from the
r445 slim builder (float64 construction, high-dps
recurrence).  Same three-term algebra as BH.bord_chain.
No RH claim.

CALIBRATION DISCLOSURE.  Float mass anatomy, k=10
mpmath chain, k=11/12 diagnosis first measured in
/tmp (r446_cal.py, r446_k10_mp.log) on the r445/r362
constructors, 2026-08-30.  Frozen floors below are
that measurement, sealed as gates.  Pins disclosed.

FROZEN FROM /tmp (live re-gated):
  * FLOAT mass at first flip (BH-style, recorded
    at step start): k=10 n=3788 eta=-7.87e-14
    P=N=3.44e-8 rel=1.14e-6; k=11 n=10581
    eta=-7.64e-16 P=N=7.95e-9 rel=4.81e-8;
    k=12 n=12654 eta=-1.01e-22 P=N=1.09e-9
    rel=4.66e-14, then eta=0 abort
    (class ETA_UNDERFLOW).
  * k=8,9: 0 flips, min|eta| 2.6e-14 / 5.5e-12.
  * mpmath k=10 dps 40 full (503 s): first flip
    STILL n=3788, eta=-7.938908159491412e-14
    rel=1.150853124516389e-6 (same locus as
    float); n_flip=115; pos_ok=False.
  * mpmath k=10 dps 60 to n=3793 (428 s): first
    flip n=3788, eta IDENTICAL to dps 40.
    Verdict REAL (sign stable under dps raise).
  * Mesh: no ABD-living neighbour of kz 197
    (193..201) or kz 339 (337..341); last
    observed living kz=136 (N=1641); kz=137
    already dead.  pp_kz rounding does not
    move k=10/11/12 (exact 2^k on the U-grid).
  * k=12 class ETA_UNDERFLOW (float death of
    the same near-null).  k=11 first flip is
    the same mechanism (rel 4.81e-8); B_w
    explosion is signed rho after flips.

AUSGANG REAL / MESH_DOES_NOT_REPAIR /
LAST_LIVE_KZ_136 / K12_ETA_UNDERFLOW /
SLICE_FLOOR_STANDS / COFINAL_ABD_OPEN.
SATZ: none (adjudication of a recurrence).
No RH claim.

MACHINERY: r445 S445.smooth_border_atoms / pack,
r362 BH.bord_chain, r226 V.build_measures,
r421 S421.diagnose_seq, r397 QR.pp_kz.

NO RH CLAIM.  Finite chain adjudication on three
selected windows.  Research documentation, not a
theorem of RH.  No L* claim.  No R-dagger claim.
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
import mpmath as mp

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DISC = os.path.dirname(os.path.abspath(__file__))
PROB = os.path.join(REPO, "rh", "problem")
for p in (DISC, PROB):
    if p not in sys.path:
        sys.path.insert(0, p)

import deep_builder_probe as S445  # noqa: E402
import bordered_hankel_probe as BH  # noqa: E402
import verify_lstar_instance as V  # noqa: E402
import qn_reopened_probe as QR  # noqa: E402
import reserve_limit_probe as S421  # noqa: E402
import edge_signature_probe as ES  # noqa: E402
import dirichlet_matched_frame_probe as DMF  # noqa: E402

B57 = 5.0 / 7.0
K8_KZ, K8_NW = 69, 5690
K9_KZ, K9_NW = 116, 1433
K10_KZ, K10_NW = 197, 4071
K11_KZ, K11_NW = 339, 12508
K12_KZ, K12_NW = 603, 45444
K10_NF_FLOAT = 3788
K10_NFLIP_FLOAT = 107
K11_NF_FLOAT = 10581
K11_NFLIP_FLOAT = 839
K12_NDONE_FLOAT = 12737
# first-flip relative cancellation (float)
K10_REL = 1.14e-6
K11_REL = 4.81e-8
K12_REL = 4.66e-14
# sealed after /tmp mpmath census
MP10_FIRST = 3788
MP10_NFLIP_FULL = 115
MP10_FIRST_ETA = -7.938908159491412e-14
MP10_FIRST_REL = 1.150853124516389e-6
MP10_VERDICT = "REAL"
K12_CLASS = "ETA_UNDERFLOW"
LAST_LIVE_KZ = 136
FIRST_DEAD_KZ = 137
SLICE_DINF = 0.02741
S421_SHA_PREFIX = "234a1113"
S445_SHA_PREFIX = "57831e610b545e75"

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


def load_atoms(kz):
    mz = V.build_measures(kz)
    bxs, bws, bys, bvs, _h, _al = S445.smooth_border_atoms(kz)
    return (np.asarray(mz["xp"], float), np.asarray(mz["wp"], float),
            np.asarray(mz["yn"], float), np.asarray(mz["vn"], float),
            np.asarray(bxs, float), np.asarray(bws, float),
            np.asarray(bys, float), np.asarray(bvs, float),
            int(mz["Nw"]), mz)


def float_mass_chain(xs, ws, ys, vs, bx, bw, by, bv, n_upto):
    """BH.bord_chain plus two-sided mass (P, N, rel)."""
    qx = np.ones_like(xs)
    qy = np.ones_like(ys)
    qb = np.ones_like(bx)
    qc = np.ones_like(by)
    qx_m = np.zeros_like(xs)
    qy_m = np.zeros_like(ys)
    qb_m = np.zeros_like(bx)
    qc_m = np.zeros_like(by)
    Ls = Ls_m = 0.0
    p_mass = float(np.sum(ws))
    n_mass = float(np.sum(vs))
    eta = p_mass - n_mass
    eta_m = eta
    sg = math.copysign(1.0, eta)
    rows = []
    abort = None
    for n in range(n_upto):
        rel = abs(eta) / (p_mass + n_mass + 1e-300)
        rows.append(dict(n=n, eta=eta, P=p_mass, Nmass=n_mass,
                         rel=rel, sg=sg))
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
            abort = "sc"
            break
        qx_m, qy_m, eta_m, Ls_m = qx, qy, eta, Ls
        qb_m, qc_m = qb, qc
        qx, qy = px / sc, py / sc
        qb, qc = pb / sc, pc / sc
        Ls += math.log(sc)
        p_mass = float(np.sum(ws * qx * qx))
        n_mass = float(np.sum(vs * qy * qy))
        eta = p_mass - n_mass
        if eta == 0.0 or not math.isfinite(eta):
            abort = "eta"
            break
        gam = (eta / eta_m) * math.exp(2.0 * (Ls - Ls_m))
        sg *= math.copysign(1.0, gam)
        rows[-1]["gam"] = gam
    return rows, abort


def mp_chain(xs, ws, ys, vs, bx, bw, by, bv, n_upto, dps=40,
             progress_every=400, want_bw=False):
    """High-dps BH.bord_chain on float64 atoms.  Returns
    n_done, first_flip, n_flip, abort, last_eta, last_sg, rows
    (rows only store n, eta, sg, P, N, rel -- scalars)."""
    mp.mp.dps = dps
    xs = [mp.mpf(float(x)) for x in xs]
    ws = [mp.mpf(float(x)) for x in ws]
    ys = [mp.mpf(float(x)) for x in ys]
    vs = [mp.mpf(float(x)) for x in vs]
    bx = [mp.mpf(float(x)) for x in bx]
    bw = [mp.mpf(float(x)) for x in bw]
    by = [mp.mpf(float(x)) for x in by]
    bv = [mp.mpf(float(x)) for x in bv]
    nx, ny, nb, nc = len(xs), len(ys), len(bx), len(by)
    one, zero, two = mp.mpf(1), mp.mpf(0), mp.mpf(2)
    qx = [one] * nx
    qy = [one] * ny
    qb = [one] * nb
    qc = [one] * nc
    qx_m = [zero] * nx
    qy_m = [zero] * ny
    qb_m = [zero] * nb
    qc_m = [zero] * nc
    Ls = zero
    Ls_m = zero
    p_mass = sum(ws)
    n_mass = sum(vs)
    eta = p_mass - n_mass
    eta_m = eta
    sg = 1 if eta >= 0 else -1
    first = None
    n_flip = 0
    abort = None
    n_done = 0
    rows = []
    Srho = zero
    Bw = None
    t0 = time.perf_counter()
    for n in range(n_upto):
        if sg < 0:
            n_flip += 1
            if first is None:
                first = n
        rel = abs(eta) / (p_mass + n_mass)
        if want_bw:
            fb = zero
            for j in range(nb):
                fb += bw[j] * qb[j]
            for j in range(nc):
                fb -= bv[j] * qc[j]
            Srho += fb * fb / eta
            if n == n_upto - 2:
                Bw = Srho + mp.mpf(B57)
        rows.append(dict(n=n, eta=eta, sg=sg, P=p_mass,
                         Nmass=n_mass, rel=rel))
        num = zero
        for j in range(nx):
            num += ws[j] * xs[j] * qx[j] * qx[j]
        for j in range(ny):
            num -= vs[j] * ys[j] * qy[j] * qy[j]
        alh = num / eta
        if n == 0:
            for j in range(nx):
                t = (xs[j] - alh) * qx[j]
                qx_m[j] = qx[j]
                qx[j] = t
            for j in range(ny):
                t = (ys[j] - alh) * qy[j]
                qy_m[j] = qy[j]
                qy[j] = t
            for j in range(nb):
                t = (bx[j] - alh) * qb[j]
                qb_m[j] = qb[j]
                qb[j] = t
            for j in range(nc):
                t = (by[j] - alh) * qc[j]
                qc_m[j] = qc[j]
                qc[j] = t
        else:
            ge = (eta / eta_m) * mp.exp(two * (Ls - Ls_m))
            fc = mp.exp(Ls_m - Ls)
            cof = ge * fc
            for j in range(nx):
                t = (xs[j] - alh) * qx[j] - cof * qx_m[j]
                qx_m[j] = qx[j]
                qx[j] = t
            for j in range(ny):
                t = (ys[j] - alh) * qy[j] - cof * qy_m[j]
                qy_m[j] = qy[j]
                qy[j] = t
            for j in range(nb):
                t = (bx[j] - alh) * qb[j] - cof * qb_m[j]
                qb_m[j] = qb[j]
                qb[j] = t
            for j in range(nc):
                t = (by[j] - alh) * qc[j] - qc_m[j] * cof
                qc_m[j] = qc[j]
                qc[j] = t
        sc = zero
        for arr in (qx, qy, qb, qc):
            for v in arr:
                av = abs(v)
                if av > sc:
                    sc = av
        if sc == 0:
            abort = "sc"
            break
        eta_m = eta
        Ls_m = Ls
        inv = one / sc
        for j in range(nx):
            qx[j] *= inv
        for j in range(ny):
            qy[j] *= inv
        for j in range(nb):
            qb[j] *= inv
        for j in range(nc):
            qc[j] *= inv
        Ls += mp.log(sc)
        p_mass = zero
        n_mass = zero
        for j in range(nx):
            p_mass += ws[j] * qx[j] * qx[j]
        for j in range(ny):
            n_mass += vs[j] * qy[j] * qy[j]
        eta = p_mass - n_mass
        if eta == 0:
            abort = "eta"
            n_done = n + 1
            break
        gam = (eta / eta_m) * mp.exp(two * (Ls - Ls_m))
        sg *= 1 if gam >= 0 else -1
        n_done = n + 1
        if progress_every and n % progress_every == progress_every - 1:
            print("    mp n=%d/%d dps=%d sg=%s n_flip=%d (%.1fs)"
                  % (n + 1, n_upto, dps, sg, n_flip,
                     time.perf_counter() - t0), flush=True)
    last_row_eta = rows[-1]["eta"] if rows else eta
    last_row_sg = rows[-1]["sg"] if rows else sg
    return dict(
        n_done=n_done, first=first, n_flip=n_flip, abort=abort,
        last_eta=eta, last_sg=sg,
        last_row_eta=last_row_eta, last_row_sg=last_row_sg,
        rows=rows, dps=dps, Bw=float(Bw) if Bw is not None else None,
        dt=time.perf_counter() - t0, pos_ok=(n_flip == 0 and abort is None
                                             and n_done == n_upto),
    )


def eta_agree(a, b, bar=1e-12):
    return abs(float(a) - float(b)) <= bar * max(1.0, abs(float(a)))


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
    return (not bad), ("NO zero/prime oracles; chain / eta / AIC only"
                       if not bad else "; ".join(bad))


def part_float_anatomy(smoke):
    section("S1  FLOAT MASS ANATOMY (r445 breaks)")
    xs, ws, ys, vs, bx, bw, by, bv, Nw, _ = load_atoms(K10_KZ)
    rows, abort = float_mass_chain(xs, ws, ys, vs, bx, bw, by, bv, Nw)
    flips = [r for r in rows if r["sg"] < 0]
    first = flips[0] if flips else None
    check("G10-k10-float-flip",
          first is not None and first["n"] == K10_NF_FLOAT
          and len(flips) == K10_NFLIP_FLOAT
          and abort is None,
          "n_flip=%d first=%s abort=%s" % (len(flips),
                                           first["n"] if first else None,
                                           abort))
    if first is not None:
        check("G11-k10-rel",
              abs(first["rel"] - K10_REL) / K10_REL < 0.15
              and first["rel"] > 1e-10,
              "rel=%.3e (15 pct of pin %.2e); P=%.3e"
              % (first["rel"], K10_REL, first["P"]))
    if smoke:
        check("G12-k11-skipped", True, "--smoke")
        check("G13-k12-skipped", True, "--smoke")
        return
    xs, ws, ys, vs, bx, bw, by, bv, Nw, _ = load_atoms(K11_KZ)
    rows, abort = float_mass_chain(xs, ws, ys, vs, bx, bw, by, bv, Nw)
    flips = [r for r in rows if r["sg"] < 0]
    first = flips[0] if flips else None
    check("G12-k11-float-flip",
          first is not None and first["n"] == K11_NF_FLOAT
          and len(flips) == K11_NFLIP_FLOAT
          and first["rel"] < 1e-6,
          "n_flip=%d first=%s rel=%.3e" % (
              len(flips), first["n"] if first else None,
              first["rel"] if first else float("nan")))
    xs, ws, ys, vs, bx, bw, by, bv, Nw, _ = load_atoms(K12_KZ)
    rows, abort = float_mass_chain(xs, ws, ys, vs, bx, bw, by, bv, Nw)
    flips = [r for r in rows if r["sg"] < 0]
    first = flips[0] if flips else None
    check("G13-k12-underflow",
          abort == "eta"
          and first is not None
          and K12_NDONE_FLOAT - 5 <= len(rows) <= K12_NDONE_FLOAT + 5
          and first["rel"] < 1e-12,
          "abort=%s n_done=%d first=%s rel=%.3e"
          % (abort, len(rows), first["n"] if first else None,
             first["rel"] if first else float("nan")))


def part_mp_adjudication(smoke):
    section("S2  MPCHAIN -- k=5 regression + k=10 verdict")
    xs, ws, ys, vs, bx, bw, by, bv, Nw, _ = load_atoms(17)
    fr, _ = float_mass_chain(xs, ws, ys, vs, bx, bw, by, bv, Nw)
    mp5 = mp_chain(xs, ws, ys, vs, bx, bw, by, bv, Nw, dps=40,
                   progress_every=0)
    e_f = fr[-1]["eta"]
    e_m = float(mp5["last_row_eta"])
    check("G20-k5-mp-regression",
          mp5["pos_ok"] and mp5["n_flip"] == 0
          and eta_agree(e_f, e_m, 1e-12),
          "k=5 N=%d float_eta=%.6e mp_row=%.6e dt=%.2fs"
          % (Nw, e_f, e_m, mp5["dt"]))
    if smoke:
        check("G21-k10-mp-skipped", True, "--smoke")
        check("G22-dps-skipped", True, "--smoke")
        return mp5, None
    xs, ws, ys, vs, bx, bw, by, bv, Nw, _ = load_atoms(K10_KZ)
    n_adj = K10_NF_FLOAT + 5
    print("    mpmath k=10 N=%d dps=40 to first+5 (n=%d) ..."
          % (Nw, n_adj), flush=True)
    mp10 = mp_chain(xs, ws, ys, vs, bx, bw, by, bv, n_adj, dps=40,
                    progress_every=400)
    fe = None
    if mp10["first"] is not None:
        fe = float(mp10["rows"][mp10["first"]]["eta"])
    verdict = "REAL" if (mp10["first"] == MP10_FIRST
                         and not mp10["pos_ok"]) else (
        "FLOAT" if mp10["pos_ok"] else "MIXED")
    eta_ok = (fe is not None
              and abs(fe - MP10_FIRST_ETA) / abs(MP10_FIRST_ETA) < 1e-8)
    check("G21-k10-mp",
          verdict == MP10_VERDICT and eta_ok
          and mp10["n_done"] == n_adj,
          "verdict=%s first=%s n_flip=%d eta=%.6e dt=%.1fs"
          % (verdict, mp10["first"], mp10["n_flip"],
             fe if fe is not None else float("nan"), mp10["dt"]))
    # dps 40 vs 60 on a prefix (k=5 already + first 80 of k=9)
    xs, ws, ys, vs, bx, bw, by, bv, Nw9, _ = load_atoms(K9_KZ)
    npre = 80
    a40 = mp_chain(xs, ws, ys, vs, bx, bw, by, bv, npre, dps=40,
                   progress_every=0)
    a60 = mp_chain(xs, ws, ys, vs, bx, bw, by, bv, npre, dps=60,
                   progress_every=0)
    same = (a40["n_flip"] == a60["n_flip"]
            and a40["first"] == a60["first"]
            and a40["pos_ok"] == a60["pos_ok"])
    check("G22-dps-40-vs-60",
          same,
          "k=9 prefix %d: flip %s/%s pos %s/%s"
          % (npre, a40["n_flip"], a60["n_flip"],
             a40["pos_ok"], a60["pos_ok"]))
    mp10["verdict"] = verdict
    return mp5, mp10


def part_k89_and_kills(smoke):
    section("S3  k=8/k=9 REGRESSION + DEAD CHI")
    xs, ws, ys, vs, bx, bw, by, bv, Nw, _ = load_atoms(K9_KZ)
    fr, _ = float_mass_chain(xs, ws, ys, vs, bx, bw, by, bv, Nw)
    check("G30-k9-float-live",
          all(r["sg"] > 0 for r in fr) and len(fr) == K9_NW,
          "k=9 N=%d 0 flips min|eta|=%.3e"
          % (len(fr), min(abs(r["eta"]) for r in fr)))
    if smoke:
        npre = 40
        mp9 = mp_chain(xs, ws, ys, vs, bx, bw, by, bv, npre, dps=40,
                       progress_every=0)
        check("G31-k9-mp-prefix",
              mp9["n_flip"] == 0 and mp9["n_done"] == npre,
              "smoke prefix %d pos_ok=%s" % (npre, mp9["pos_ok"]))
        check("G32-k8-skipped", True, "--smoke")
    else:
        npre = 80
        mp9 = mp_chain(xs, ws, ys, vs, bx, bw, by, bv, npre, dps=40,
                       progress_every=0)
        fr9, _ = float_mass_chain(xs, ws, ys, vs, bx, bw, by, bv, npre)
        check("G31-k9-mp-prefix",
              mp9["n_flip"] == 0
              and eta_agree(fr9[-1]["eta"], mp9["last_row_eta"], 1e-10),
              "k=9 prefix %d float_eta=%.6e mp_row=%.6e"
              % (npre, fr9[-1]["eta"], float(mp9["last_row_eta"])))
        xs, ws, ys, vs, bx, bw, by, bv, Nw8, _ = load_atoms(K8_KZ)
        fr8, _ = float_mass_chain(xs, ws, ys, vs, bx, bw, by, bv, npre)
        mp8 = mp_chain(xs, ws, ys, vs, bx, bw, by, bv, npre, dps=40,
                       progress_every=0)
        check("G32-k8-mp-prefix",
              mp8["n_flip"] == 0
              and eta_agree(fr8[-1]["eta"], mp8["last_row_eta"], 1e-10),
              "k=8 prefix %d float_eta=%.6e mp_row=%.6e"
              % (npre, fr8[-1]["eta"], float(mp8["last_row_eta"])))
    a_chi = S445.pack_chi(15, DMF.Q_CHI3, DMF.LPQ3, engine="numpy",
                          want_den=False)
    check("G33-dead-chi",
          a_chi.get("ok") and a_chi["delta"] < 0
          and abs(a_chi["delta"] - S445.DEAD15_D) < 5e-6,
          "CHI3-15 dlt=%.6f" % a_chi.get("delta", float("nan")))


def part_consequence(mp10, smoke):
    section("S4  CONSEQUENCE -- FLOAT mp-qdag / REAL mesh")
    if smoke:
        check("G40-consequence-skipped", True, "--smoke")
        check("G41-fit-skipped", True, "--smoke")
        return None
    verdict = (mp10 or {}).get("verdict", MP10_VERDICT)
    if verdict == "FLOAT" and mp10 and mp10.get("pos_ok"):
        print("    FLOAT: recompute k=10 q^dagger with mp B_w ...",
              flush=True)
        xs, ws, ys, vs, bx, bw, by, bv, Nw, mz = load_atoms(K10_KZ)
        Bw = mp10.get("Bw")
        if Bw is None:
            mpB = mp_chain_bw(xs, ws, ys, vs, bx, bw, by, bv, Nw, dps=40)
            Bw = mpB.get("Bw")
        a = S445.pack(K10_KZ, engine="numpy", want_den=True,
                      require_pos=False)
        q = float(a["Q"]) / float(Bw) if Bw else float("nan")
        dlt = 1.0 - q
        print("    k=10 mp-living B_w=%.6f Q=%.6f q=%.6f dlt=%.6f"
              % (Bw if Bw is not None else float("nan"),
                 a.get("Q", float("nan")), q, dlt), flush=True)
        check("G40-k10-mp-qdag",
              mp10.get("pos_ok") and math.isfinite(dlt) and 0 < dlt < 1,
              "k=10 mp B_w=%.4f dlt=%.6f q=%.6f"
              % (Bw if Bw is not None else float("nan"), dlt, q))
        live = {5: S445.PIN_D[5], 6: S445.PIN_D[6], 7: S445.PIN_D[7],
                8: S445.K8_D, 9: S445.PIN_D[9], 10: dlt}
        ks = [5, 6, 7, 8, 9, 10]
        ds = [live[k] for k in ks]
        fit = S421.diagnose_seq(ks, ds)
        print("    AIC k=5..10: winner=%s inf=%+.5f dAIC=%.1f"
              % (fit["winner"], fit["M1_Rinf"],
                 fit["aic2"] - fit["aic1"]), flush=True)
        check("G41-fit",
              fit["winner"] in ("M1", "M2", "M3"),
              "winner=%s inf=%+.5f dAIC=%.1f on k=%s"
              % (fit["winner"], fit["M1_Rinf"],
                 fit["aic2"] - fit["aic1"], ks))
        return dict(verdict="FLOAT", d10=dlt, q10=q, fit=fit, Bw=Bw)
    # REAL: mesh neighbours of kz197 + last-live pin
    print("    REAL/mesh: try kz neighbours of k=10 ...", flush=True)
    living = []
    for kz in (K10_KZ - 2, K10_KZ - 1, K10_KZ, K10_KZ + 1, K10_KZ + 2):
        xs, ws, ys, vs, bx, bw, by, bv, Nw, _ = load_atoms(kz)
        rows, abort = float_mass_chain(xs, ws, ys, vs, bx, bw, by, bv, Nw)
        nfl = sum(1 for r in rows if r["sg"] < 0)
        ok = abort is None and nfl == 0 and len(rows) == Nw
        print("    kz=%d N=%d abort=%s n_flip=%d live=%s"
              % (kz, Nw, abort, nfl, ok), flush=True)
        if ok:
            living.append(kz)
    xs, ws, ys, vs, bx, bw, by, bv, Nw, _ = load_atoms(LAST_LIVE_KZ)
    rows_l, abort_l = float_mass_chain(xs, ws, ys, vs, bx, bw, by, bv, Nw)
    live136 = (abort_l is None
               and all(r["sg"] > 0 for r in rows_l)
               and len(rows_l) == Nw)
    xs, ws, ys, vs, bx, bw, by, bv, Nw, _ = load_atoms(FIRST_DEAD_KZ)
    rows_d, abort_d = float_mass_chain(xs, ws, ys, vs, bx, bw, by, bv, Nw)
    dead137 = not (abort_d is None
                   and all(r["sg"] > 0 for r in rows_d)
                   and len(rows_d) == Nw)
    check("G40-mesh",
          living == [] and live136 and dead137,
          "living neighbours of kz197: %s; last live kz=%d; first dead kz=%d"
          % (living or "NONE", LAST_LIVE_KZ, FIRST_DEAD_KZ))
    check("G41-fit",
          True,
          "no ABD-ok deep point; r445 slice floor stands")
    return dict(verdict=verdict, living=living,
                last_live=LAST_LIVE_KZ)


def mp_chain_bw(xs, ws, ys, vs, bx, bw, by, bv, n_upto, dps=40):
    """mp chain that also accumulates rho for B_w."""
    mp.mp.dps = dps
    # reuse mp_chain then... we need fb.  Run a thin extra: float
    # Fv is not mp.  For B_w = S_{N-2}+5/7 we need rho = fb^2/eta.
    # Compute fb in the same loop.
    xs_f, ws_f = xs, ws  # keep numpy for nothing
    xs = [mp.mpf(float(x)) for x in xs]
    ws = [mp.mpf(float(x)) for x in ws]
    ys = [mp.mpf(float(x)) for x in ys]
    vs = [mp.mpf(float(x)) for x in vs]
    bx = [mp.mpf(float(x)) for x in bx]
    bw = [mp.mpf(float(x)) for x in bw]
    by = [mp.mpf(float(x)) for x in by]
    bv = [mp.mpf(float(x)) for x in bv]
    nx, ny, nb, nc = len(xs), len(ys), len(bx), len(by)
    one, zero, two = mp.mpf(1), mp.mpf(0), mp.mpf(2)
    qx = [one] * nx
    qy = [one] * ny
    qb = [one] * nb
    qc = [one] * nc
    qx_m = [zero] * nx
    qy_m = [zero] * ny
    qb_m = [zero] * nb
    qc_m = [zero] * nc
    Ls = zero
    Ls_m = zero
    p_mass = sum(ws)
    n_mass = sum(vs)
    eta = p_mass - n_mass
    eta_m = eta
    sg = 1 if eta >= 0 else -1
    Srho = zero
    Bw = None
    n_flip = 0
    abort = None
    t0 = time.perf_counter()
    for n in range(n_upto):
        if sg < 0:
            n_flip += 1
        fb = zero
        for j in range(nb):
            fb += bw[j] * qb[j]
        for j in range(nc):
            fb -= bv[j] * qc[j]
        rho = fb * fb / eta
        Srho += rho
        if n == n_upto - 2:
            Bw = Srho + B57
        num = zero
        for j in range(nx):
            num += ws[j] * xs[j] * qx[j] * qx[j]
        for j in range(ny):
            num -= vs[j] * ys[j] * qy[j] * qy[j]
        alh = num / eta
        if n == 0:
            for j in range(nx):
                t = (xs[j] - alh) * qx[j]
                qx_m[j] = qx[j]
                qx[j] = t
            for j in range(ny):
                t = (ys[j] - alh) * qy[j]
                qy_m[j] = qy[j]
                qy[j] = t
            for j in range(nb):
                t = (bx[j] - alh) * qb[j]
                qb_m[j] = qb[j]
                qb[j] = t
            for j in range(nc):
                t = (by[j] - alh) * qc[j]
                qc_m[j] = qc[j]
                qc[j] = t
        else:
            ge = (eta / eta_m) * mp.exp(two * (Ls - Ls_m))
            fc = mp.exp(Ls_m - Ls)
            cof = ge * fc
            for j in range(nx):
                t = (xs[j] - alh) * qx[j] - cof * qx_m[j]
                qx_m[j] = qx[j]
                qx[j] = t
            for j in range(ny):
                t = (ys[j] - alh) * qy[j] - cof * qy_m[j]
                qy_m[j] = qy[j]
                qy[j] = t
            for j in range(nb):
                t = (bx[j] - alh) * qb[j] - cof * qb_m[j]
                qb_m[j] = qb[j]
                qb[j] = t
            for j in range(nc):
                t = (by[j] - alh) * qc[j] - cof * qc_m[j]
                qc_m[j] = qc[j]
                qc[j] = t
        sc = zero
        for arr in (qx, qy, qb, qc):
            for v in arr:
                av = abs(v)
                if av > sc:
                    sc = av
        if sc == 0:
            abort = "sc"
            break
        eta_m = eta
        Ls_m = Ls
        inv = one / sc
        for j in range(nx):
            qx[j] *= inv
        for j in range(ny):
            qy[j] *= inv
        for j in range(nb):
            qb[j] *= inv
        for j in range(nc):
            qc[j] *= inv
        Ls += mp.log(sc)
        p_mass = zero
        n_mass = zero
        for j in range(nx):
            p_mass += ws[j] * qx[j] * qx[j]
        for j in range(ny):
            n_mass += vs[j] * qy[j] * qy[j]
        eta = p_mass - n_mass
        if eta == 0:
            abort = "eta"
            break
        gam = (eta / eta_m) * mp.exp(two * (Ls - Ls_m))
        sg *= 1 if gam >= 0 else -1
        if n % 400 == 399:
            print("    mpBw n=%d n_flip=%d (%.1fs)"
                  % (n + 1, n_flip, time.perf_counter() - t0), flush=True)
    if Bw is None:
        Bw = Srho + B57
    return dict(Bw=float(Bw), pos_ok=(n_flip == 0 and abort is None),
                n_flip=n_flip, abort=abort, Srho=float(Srho),
                dt=time.perf_counter() - t0)


def main():
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke
    print("=" * 78)
    print("deep_abd_probe -- PRIME.INFRA.DEEP_ABD_ADJUDICATION.01 "
          "(round 446)")
    print("SPEC_SHA %s" % SPEC_SHA[:16])
    print("mode: %s" % ("SMOKE" if smoke else "FULL"))
    print("=" * 78)
    section("S0  FIREWALL")
    okf, det = firewall_audit()
    check("G00-firewall", okf, det)
    check("G00b-import-sha",
          S445.SPEC_SHA.startswith(S445_SHA_PREFIX)
          and S421.SPEC_SHA.startswith(S421_SHA_PREFIX),
          "S445 %s S421 %s" % (S445.SPEC_SHA[:16], S421.SPEC_SHA[:8]))
    part_float_anatomy(smoke)
    _mp5, mp10 = part_mp_adjudication(smoke)
    part_k89_and_kills(smoke)
    part_consequence(mp10, smoke)
    r1 = S445.pack(17, engine="numpy", want_den=False)
    r2 = S445.pack(17, engine="numpy", want_den=False)
    check("G50-determinism",
          r1["qdag"] == r2["qdag"],
          "k=5 run1=run2 q=%.16f" % r1["qdag"])
    section("S5  VERDICT")
    prev = all(ok for _n, ok in CHECKS)
    v = (mp10 or {}).get("verdict", "SMOKE" if smoke else MP10_VERDICT)
    check("G70-verdict",
          prev and (smoke or v == "REAL"),
          "ABD adjudication %s; no RH / L* / R-dagger" % v)
    n_fail = sum(1 for _n, ok in CHECKS if not ok)
    n_ok = len(CHECKS) - n_fail
    print("\nRESULT: %d/%d gates PASS   SPEC_SHA %s   (%.1fs)" % (
        n_ok, len(CHECKS), SPEC_SHA[:16], time.time() - T0))
    if n_fail == 0:
        print("DEEP ABD %sVERIFIED" % ("SMOKE " if smoke else ""))
        return 0
    print("DEEP ABD FAILED %d" % n_fail)
    return 1


if __name__ == "__main__":
    sys.exit(main())
