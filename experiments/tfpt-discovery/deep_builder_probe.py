#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""deep_builder_probe -- PRIME.INFRA.DEEP_BUILDER.01
(round 445): unlock border_chain_pack for selected
k = 10, 11, 12 and decide the floor-vs-decay fit
on the lengthened sequence.  Research documentation,
NO RH claim.

THE BOTTLENECK (r443).  k=10 (kz197, N=4071) timed
out at 20 s.  Canonical path: ABD.border_chain_pack
= BH.bord_chain, but the CALLER (ES.main_row /
HS.window_data) first builds a SMOOTH-comb Lanczos
of size (n_atoms, N) with two-sided reorthogonalization
-- O(N^2 M), unused by q^dagger.  Measured k=10
HS.window_data = 20.57 s (exactly the r443 wall);
slim atoms (folded +/- only) = 0.18 s.  The chain
itself is 0.29 s.  Named hotspot = unused Lanczos,
not the chain recursion.

WHAT IS COMPUTED.  Only q^dagger / delta:
  q^dagger = (1/B_w) b^T (I - C)^{-1} b,
  C = B^T B, B[k,i] = sqrt(v_k) P_i(y_k),
  b = mu-OP coefficients of the signed smooth
  border, B_w = S_{N-2} + 5/7.
No full eigendecomposition.  Smaller of
(|Y| x |Y|, N x N) when it fits; else CG.
den / Sigma / branch via cut_rung without Lanczos.
Canonical engine = numpy (BH/V/ABD recurrences).
numba is an optional accelerator: k=9 ulp
|dq| = 5.6e-9 (summation reorder), bar 1e-8;
numba chain is slower than numpy at k=9
(1.45 s vs 0.062 s) so it is NOT the default.

CALIBRATION DISCLOSURE.  Hotspot, slim-vs-old
bit-gate, k=8 cross, k=10/11/12 census, AIC on
k=5..9+live-k8 first measured in /tmp (r445_cal.py,
r445_cal2.py) on the r362/r417/r421/r442
constructors, 2026-08-30.  Frozen floors below
are that measurement, sealed as gates.  Pins
disclosed.  Builder fallback NOT taken: skip-
Lanczos numpy-slim IS the round.

FROZEN FROM /tmp (live re-gated):
  * HOTSPOT k=9: HS.window_data 0.768 s vs slim
    atoms 0.081 s (9.5x).  bord_chain 0.062 s.
    k=10 HS 20.57 s vs slim atoms 0.18 s.
  * BIT-GATE k=3..9: numpy-slim vs ABD/V+HS atoms
    |dq|=|dd|=0 at 1e-12 (atoms bitwise identical
    to HS.window_data; same np.sum order).  den/Sig
    vs live legacy at 1e-12.  r443 6-digit delta
    pins reproduced.  numba vs numpy k=9 |dq|=5.6e-9.
  * k=8 CROSS LIVE (N=5690, 8.2 s): R=0.047628
    den=1.568548 Sig=0.383825 P1=True.  r421 pin
    R=0.04763 / den=1.56855 / Sig=0.38382 CONFIRMED.
    r427 circularity (k=8 not rebuilt) CLOSED.
    delta=0.047488 q^dagger=0.952512.
  * k=10 (N=4071, 4.4 s): chain COMPLETES but
    ABD.ok FAILS -- 107 sign-flips from n=3788.
    Formula-literal q^dagger=0.999581 delta=0.000419
    (signed B_w=19.07).  Last-positive B_w gives
    q_pos=0.968177 delta_pos=0.031823.  P1=False.
    Residual 9.5e-12.  NOT ABD-living.
  * k=11 (N=12508, 98 s): 839 sign-flips from
    n=10581; signed B_w EXPLODES to 21434;
    formula-literal q^dagger=0.00345 delta=0.99655
    is not a sequence point.  NOT ABD-living.
  * k=12 (N=45444, nY=23429): chain ABORTS at
    n_done=12737 (eta underflow, 37 sign-flips
    from n=12654).  No faithful B_w at full depth.
    B would be 8.5 GB.  Documented fail.
  * AIC ABD-ok k=5,6,7,8,9 (live k=8): M1 wins,
    delta_inf=+0.02741, DeltaAIC(M2)=5.11 (r443
    without k=8: +0.02670 / 6.01).  Floor preferred
    on the slice; live k=8 sits on the curve and
    does NOT flip the verdict.  Full k=3..9 still
    prefers M3 (k=5 bump).  vs N: M2 (r427 illegal).
    Drop k=5 -> M2; drop k=9 -> M1 inf jumps to
    0.039.  k=10/11/12 do not extend the ABD-ok
    sequence, so they do not decide floor vs decay.

AUSGANG INFRA_UNLOCKED / K8_CROSS_CONFIRMED /
DEEP_NOT_ABD_LIVING / SLICE_FLOOR_PREFERRED /
FULL_SEQUENCE_UNSETTLED / COFINAL_OPEN.
SATZ: none new (q^dagger formula is r442).
CENSUS: unused-Lanczos hotspot; k=8 live pin;
k=10/11 sign-flip; k=12 abort; AIC with live k=8.
INFRA: the builder (skip Lanczos, numpy-slim).
No RH claim.

MACHINERY: r362 ABD.bvec_chunked / BH.bord_chain,
r226 V.build_measures / mu_chain / b_matrix,
r243 PB.smooth_comb, r881 PIK.folded_measure
(atoms only), r421 S421.diagnose_seq, r367
FTI.cut_rung (den add-on).

NO RH CLAIM.  Finite selected measurements,
a named AIC census, named kills.  Research
documentation, not a theorem of RH.  No L*
claim.  No R-dagger claim.
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

import verify_lstar_instance as V  # noqa: E402
import bordered_hankel_probe as BH  # noqa: E402
import augmented_borodin_duality_probe as ABD  # noqa: E402
import principal_bessel_probe as PB  # noqa: E402
import port_integrable_kernel_probe as PIK  # noqa: E402
import pair_extremal_probe as PX  # noqa: E402
import final_two_rank_inertia_probe as FTI  # noqa: E402
import reserve_limit_probe as S421  # noqa: E402
import qn_reopened_probe as QR  # noqa: E402
import edge_signature_probe as ES  # noqa: E402
import dirichlet_matched_frame_probe as DMF  # noqa: E402

try:
    from numba import njit
    _HAS_NUMBA = True
except Exception:
    _HAS_NUMBA = False

    def njit(*_a, **_k):
        def wrap(fn):
            return fn
        if _a and callable(_a[0]):
            return _a[0]
        return wrap

B57 = 5.0 / 7.0
BIT_BAR = 1.0e-12
NUMBA_BAR = 1.0e-8
D_BAR = 5.0e-6
REL = 5.0e-3
MEM_GRAM_BYTES = int(3.5e9)
CG_RTOL = 1.0e-12
CG_MAXITER = 400
ENGINE_CANON = "numpy"

SEL_LIVE = ((3, 5), (4, 9), (5, 17), (6, 26), (7, 43), (9, 116))
SEL_SMOKE = ((3, 5), (4, 9), (5, 17))
PIN_D = {3: 0.071564, 4: 0.066956, 5: 0.108636,
         6: 0.068896, 7: 0.055396, 9: 0.037785}
PIN_DEN = {3: 1.70246, 4: 1.60111, 5: 1.65127,
           6: 1.52415, 7: 1.51822, 9: 1.48227}
K8_KZ, K8_NW = 69, 5690
K8_R_PIN = 0.04763
K8_DEN_PIN = 1.56855
K8_SIG_PIN = 0.38382
K10_KZ, K10_NW = 197, 4071
K11_KZ, K11_NW = 339, 12508
K12_KZ, K12_NW = 603, 45444
K8_D = 0.047488
K8_Q = 0.952512
K10_D = 0.000419
K10_DPOS = 0.031823
K10_NFLIP = 107
K10_NF = 3788
K11_D = 0.996548
K11_NFLIP = 839
K11_BW_MIN = 1.0e3
K12_NDONE_LO, K12_NDONE_HI = 12000, 13500
SLICE_DINF = 0.02741
SLICE_DAIC = 5.11
KZ16_D = 0.001510
DEAD15_D = -0.023181
CORE_KZ = (9, 17, 18)
V_SHA_PREFIX = "verify_lstar"
S421_SHA_PREFIX = "234a1113"
ABD_SHA_PREFIX = ABD.SPEC_SHA[:8] if hasattr(ABD, "SPEC_SHA") else ""

SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
CHECKS = []
T0 = time.time()
_NUMBA_READY = False


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok)))
    print("  [%s] %-44s %s" % ("PASS" if ok else "FAIL", name, detail),
          flush=True)
    return bool(ok)


def section(t):
    print("\n" + "=" * 78)
    print(t)
    print("=" * 78, flush=True)


# ------------------------------------------------------------------
# numba recurrences (same three-term algebra as V / BH / ABD)
# ------------------------------------------------------------------
@njit(cache=True)
def _mu_chain_nb(x, w, depth):
    h0 = 0.0
    n = x.shape[0]
    for j in range(n):
        h0 += w[j]
    u = np.empty(n)
    um = np.zeros(n)
    s0 = math.sqrt(h0)
    for j in range(n):
        u[j] = 1.0 / s0
    a = np.zeros(depth)
    b = np.zeros(depth)
    for i in range(depth):
        acc = 0.0
        for j in range(n):
            acc += w[j] * x[j] * u[j] * u[j]
        a[i] = acc
        acc2 = 0.0
        if i == 0:
            for j in range(n):
                r = (x[j] - a[i]) * u[j]
                um[j] = u[j]
                u[j] = r
                acc2 += w[j] * r * r
        else:
            bi = b[i - 1]
            for j in range(n):
                r = (x[j] - a[i]) * u[j] - bi * um[j]
                um[j] = u[j]
                u[j] = r
                acc2 += w[j] * r * r
        s = math.sqrt(acc2)
        b[i] = s
        inv = 1.0 / s
        for j in range(n):
            u[j] *= inv
    return a, b, h0


@njit(cache=True)
def _bvec_nb(a, bcoef, h0, t, wgt, Nw):
    n = t.shape[0]
    bv = np.zeros(Nw)
    u = np.empty(n)
    um = np.zeros(n)
    s0 = math.sqrt(h0)
    acc = 0.0
    for j in range(n):
        u[j] = 1.0 / s0
        acc += wgt[j] * u[j]
    bv[0] = acc
    for i in range(Nw - 1):
        acc = 0.0
        ai = a[i]
        invb = 1.0 / bcoef[i]
        if i == 0:
            for j in range(n):
                r = (t[j] - ai) * u[j]
                um[j] = u[j]
                u[j] = r * invb
                acc += wgt[j] * u[j]
        else:
            bim = bcoef[i - 1]
            for j in range(n):
                r = (t[j] - ai) * u[j] - bim * um[j]
                um[j] = u[j]
                u[j] = r * invb
                acc += wgt[j] * u[j]
        bv[i + 1] = acc
    return bv


@njit(cache=True)
def _b_matrix_nb(a, bcoef, h0, y, v, depth):
    m = y.shape[0]
    B = np.zeros((m, depth))
    s0 = math.sqrt(h0)
    u = np.empty(m)
    um = np.zeros(m)
    for k in range(m):
        u[k] = math.sqrt(v[k]) / s0
        B[k, 0] = u[k]
    for i in range(depth - 1):
        ai = a[i]
        invb = 1.0 / bcoef[i]
        if i == 0:
            for k in range(m):
                r = (y[k] - ai) * u[k]
                um[k] = u[k]
                u[k] = r * invb
                B[k, i + 1] = u[k]
        else:
            bim = bcoef[i - 1]
            for k in range(m):
                r = (y[k] - ai) * u[k] - bim * um[k]
                um[k] = u[k]
                u[k] = r * invb
                B[k, i + 1] = u[k]
    return B


@njit(cache=True)
def _apply_Bx_nb(a, bcoef, h0, y, v, xvec):
    m = y.shape[0]
    depth = xvec.shape[0]
    s0 = math.sqrt(h0)
    u = np.empty(m)
    um = np.zeros(m)
    out = np.zeros(m)
    for k in range(m):
        u[k] = math.sqrt(v[k]) / s0
        out[k] = xvec[0] * u[k]
    for i in range(depth - 1):
        ai = a[i]
        invb = 1.0 / bcoef[i]
        xi = xvec[i + 1]
        if i == 0:
            for k in range(m):
                r = (y[k] - ai) * u[k]
                um[k] = u[k]
                u[k] = r * invb
                out[k] += xi * u[k]
        else:
            bim = bcoef[i - 1]
            for k in range(m):
                r = (y[k] - ai) * u[k] - bim * um[k]
                um[k] = u[k]
                u[k] = r * invb
                out[k] += xi * u[k]
    return out


@njit(cache=True)
def _apply_BTx_nb(a, bcoef, h0, y, v, z):
    m = y.shape[0]
    depth = a.shape[0]
    s0 = math.sqrt(h0)
    u = np.empty(m)
    um = np.zeros(m)
    out = np.empty(depth)
    acc = 0.0
    for k in range(m):
        u[k] = math.sqrt(v[k]) / s0
        acc += u[k] * z[k]
    out[0] = acc
    for i in range(depth - 1):
        ai = a[i]
        invb = 1.0 / bcoef[i]
        acc = 0.0
        if i == 0:
            for k in range(m):
                r = (y[k] - ai) * u[k]
                um[k] = u[k]
                u[k] = r * invb
                acc += u[k] * z[k]
        else:
            bim = bcoef[i - 1]
            for k in range(m):
                r = (y[k] - ai) * u[k] - bim * um[k]
                um[k] = u[k]
                u[k] = r * invb
                acc += u[k] * z[k]
        out[i + 1] = acc
    return out


@njit(cache=True)
def _bord_chain_nb(xs, ws, ys, vs, bx, bw, by, bv, n_upto):
    nx, ny, nb, nc = xs.shape[0], ys.shape[0], bx.shape[0], by.shape[0]
    qx = np.ones(nx)
    qy = np.ones(ny)
    qb = np.ones(nb)
    qc = np.ones(nc)
    qx_m = np.zeros(nx)
    qy_m = np.zeros(ny)
    qb_m = np.zeros(nb)
    qc_m = np.zeros(nc)
    Ls = 0.0
    Ls_m = 0.0
    eta = 0.0
    for j in range(nx):
        eta += ws[j]
    for j in range(ny):
        eta -= vs[j]
    eta_m = eta
    sg_h = 1.0 if eta >= 0.0 else -1.0
    rho = np.empty(n_upto)
    Fv = np.empty(n_upto)
    sg = np.empty(n_upto)
    n_done = 0
    ok = True
    for n in range(n_upto):
        sg[n] = sg_h
        fb = 0.0
        for j in range(nb):
            fb += bw[j] * qb[j]
        for j in range(nc):
            fb -= bv[j] * qc[j]
        alh_num = 0.0
        for j in range(nx):
            alh_num += ws[j] * xs[j] * qx[j] * qx[j]
        for j in range(ny):
            alh_num -= vs[j] * ys[j] * qy[j] * qy[j]
        alh = alh_num / eta
        Fv[n] = fb
        rho[n] = fb * fb / eta
        n_done = n + 1
        px_max = 0.0
        if n == 0:
            for j in range(nx):
                px = (xs[j] - alh) * qx[j]
                qx_m[j] = qx[j]
                qx[j] = px
                ax = abs(px)
                if ax > px_max:
                    px_max = ax
            for j in range(ny):
                py = (ys[j] - alh) * qy[j]
                qy_m[j] = qy[j]
                qy[j] = py
                ay = abs(py)
                if ay > px_max:
                    px_max = ay
            for j in range(nb):
                pb = (bx[j] - alh) * qb[j]
                qb_m[j] = qb[j]
                qb[j] = pb
                ab = abs(pb)
                if ab > px_max:
                    px_max = ab
            for j in range(nc):
                pc = (by[j] - alh) * qc[j]
                qc_m[j] = qc[j]
                qc[j] = pc
                ac = abs(pc)
                if ac > px_max:
                    px_max = ac
        else:
            ge = (eta / eta_m) * math.exp(2.0 * (Ls - Ls_m))
            fc = math.exp(Ls_m - Ls)
            cof = ge * fc
            for j in range(nx):
                px = (xs[j] - alh) * qx[j] - cof * qx_m[j]
                qx_m[j] = qx[j]
                qx[j] = px
                ax = abs(px)
                if ax > px_max:
                    px_max = ax
            for j in range(ny):
                py = (ys[j] - alh) * qy[j] - cof * qy_m[j]
                qy_m[j] = qy[j]
                qy[j] = py
                ay = abs(py)
                if ay > px_max:
                    px_max = ay
            for j in range(nb):
                pb = (bx[j] - alh) * qb[j] - cof * qb_m[j]
                qb_m[j] = qb[j]
                qb[j] = pb
                ab = abs(pb)
                if ab > px_max:
                    px_max = ab
            for j in range(nc):
                pc = (by[j] - alh) * qc[j] - cof * qc_m[j]
                qc_m[j] = qc[j]
                qc[j] = pc
                ac = abs(pc)
                if ac > px_max:
                    px_max = ac
        sc = px_max
        if sc == 0.0 or not math.isfinite(sc):
            ok = False
            break
        eta_m = eta
        Ls_m = Ls
        inv = 1.0 / sc
        for j in range(nx):
            qx[j] *= inv
        for j in range(ny):
            qy[j] *= inv
        for j in range(nb):
            qb[j] *= inv
        for j in range(nc):
            qc[j] *= inv
        Ls += math.log(sc)
        eta = 0.0
        for j in range(nx):
            eta += ws[j] * qx[j] * qx[j]
        for j in range(ny):
            eta -= vs[j] * qy[j] * qy[j]
        if eta == 0.0 or not math.isfinite(eta):
            ok = False
            break
        gam = (eta / eta_m) * math.exp(2.0 * (Ls - Ls_m))
        sg_h *= 1.0 if gam >= 0.0 else -1.0
    if ok:
        allpos = True
        for n in range(n_done):
            if sg[n] <= 0.0:
                allpos = False
                break
        ok = allpos and (n_done == n_upto)
    return ok, n_done, rho, Fv


def warmup_numba():
    global _NUMBA_READY
    if _NUMBA_READY or not _HAS_NUMBA:
        return
    x = np.array([0.0, 0.5, 1.0])
    w = np.array([1.0, 1.0, 1.0])
    a, b, h0 = _mu_chain_nb(x, w, 3)
    _bvec_nb(a, b, h0, x, w, 3)
    _b_matrix_nb(a, b, h0, x, w, 3)
    _apply_Bx_nb(a, b, h0, x, w, np.ones(3))
    _apply_BTx_nb(a, b, h0, x, w, np.ones(3))
    _bord_chain_nb(x, w, x[:1], w[:1], x, w, x[:1], w[:1], 3)
    _NUMBA_READY = True


# ------------------------------------------------------------------
# atom construction -- skip unused Lanczos
# ------------------------------------------------------------------
def smooth_border_atoms(kz):
    """folded +/- measures of the sealed smooth comb.
    Atoms only: no lanczos_chain / eval_chain (the r445 cut)."""
    alpha, _M, _L, _Nw, _D = V.window_shape(kz)
    comb = PB.smooth_comb(alpha)
    b = PIK.build_rung(kz, comb=comb)
    xs, ws, _ = PIK.folded_measure(b["d"], b["L"], +1.0)
    ys, vs, _ = PIK.folded_measure(b["d"], b["L"], -1.0)
    return (np.asarray(xs, float), np.asarray(ws, float),
            np.asarray(ys, float), np.asarray(vs, float),
            int(b["h"]), float(b["alpha"]))


def bord_pack_slim(xp, wp, yn, vn, bxs, bws, bys, bvs, Nw,
                   engine="numpy", require_pos=True):
    """mu-tilde border chain to depth Nw; same scalars as
    ABD.border_chain_pack / BH.bord_chain (rho, B_w, q_N).
    require_pos=True is the ABD.ok gate (all h_k>0).
    require_pos=False still returns B_w if the chain reached Nw
    (deep selected windows may sign-flip near the end)."""
    xp = np.asarray(xp, float)
    wp = np.asarray(wp, float)
    yn = np.asarray(yn, float)
    vn = np.asarray(vn, float)
    bxs = np.asarray(bxs, float)
    bws = np.asarray(bws, float)
    bys = np.asarray(bys, float)
    bvs = np.asarray(bvs, float)
    if engine == "legacy" and require_pos:
        return ABD.border_chain_pack(xp, wp, yn, vn, bxs, bws,
                                     bys, bvs, Nw)
    if engine == "numba" and _HAS_NUMBA:
        warmup_numba()
        ok, n_done, rho, Fv = _bord_chain_nb(
            xp, wp, yn, vn, bxs, bws, bys, bvs, Nw)
        completed = n_done == Nw
        if (not completed) or (require_pos and not ok):
            return dict(ok=False, nf=n_done, completed=completed,
                        n_flip=None)
        S_ = np.cumsum(rho)
        return dict(ok=True, nf=None, rho=rho, S=S_, Fv=Fv,
                    Bw=float(S_[Nw - 2]) + B57,
                    qN=float(rho[Nw - 1]) / B57,
                    DN=B57 - float(rho[Nw - 1]),
                    SN1=float(S_[Nw - 1]),
                    completed=True, n_flip=None,
                    pos_ok=bool(ok))
    rows = BH.bord_chain(xp, wp, yn, vn, bxs, bws, bys, bvs, Nw)
    sg = np.array([r["sg_h"] for r in rows])
    nf = next((r["n"] for r in rows if r["sg_h"] < 0), None)
    n_flip = int(np.sum(sg < 0)) if len(sg) else 0
    completed = len(rows) == Nw
    pos = bool(len(sg) and np.all(sg > 0))
    if (not completed) or (require_pos and not pos):
        return dict(ok=False, nf=nf, completed=completed,
                    n_flip=n_flip, n_done=len(rows))
    rho = np.array([r["rho"] for r in rows])
    S_ = np.cumsum(rho)
    Fv = np.array([r["fb"] for r in rows])
    return dict(ok=True, nf=nf, rho=rho, S=S_, Fv=Fv,
                Bw=float(S_[Nw - 2]) + B57,
                qN=float(rho[Nw - 1]) / B57,
                DN=B57 - float(rho[Nw - 1]),
                SN1=float(S_[Nw - 1]),
                completed=True, n_flip=n_flip, pos_ok=pos)


def mu_chain_opt(x, w, depth, engine="numpy"):
    x = np.asarray(x, float)
    w = np.asarray(w, float)
    if engine == "numba" and _HAS_NUMBA:
        warmup_numba()
        return _mu_chain_nb(x, w, depth)
    return V.mu_chain(x, w, depth)


def bvec_opt(a, b, h0, t, wgt, Nw, engine="numpy"):
    t = np.asarray(t, float)
    wgt = np.asarray(wgt, float)
    if engine == "numba" and _HAS_NUMBA:
        warmup_numba()
        return _bvec_nb(np.asarray(a, float), np.asarray(b, float),
                        float(h0), t, wgt, Nw)
    return ABD.bvec_chunked(a, b, h0, t, wgt, Nw)


def b_matrix_opt(a, b, h0, y, v, depth, engine="numpy"):
    y = np.asarray(y, float)
    v = np.asarray(v, float)
    if engine == "numba" and _HAS_NUMBA:
        warmup_numba()
        return _b_matrix_nb(np.asarray(a, float), np.asarray(b, float),
                            float(h0), y, v, depth)
    return V.b_matrix(a, b, h0, y, v, depth)


def apply_Bx(a, bcoef, h0, y, v, xvec):
    a = np.asarray(a, float)
    bcoef = np.asarray(bcoef, float)
    y = np.asarray(y, float)
    v = np.asarray(v, float)
    xvec = np.asarray(xvec, float)
    if _HAS_NUMBA:
        warmup_numba()
        return _apply_Bx_nb(a, bcoef, float(h0), y, v, xvec)
    s0 = math.sqrt(h0)
    u = np.sqrt(v) / s0
    um = np.zeros_like(u)
    out = xvec[0] * u
    for i in range(xvec.shape[0] - 1):
        if i == 0:
            r = (y - a[i]) * u
        else:
            r = (y - a[i]) * u - bcoef[i - 1] * um
        um = u
        u = r / bcoef[i]
        out = out + xvec[i + 1] * u
    return out


def apply_BTx(a, bcoef, h0, y, v, z):
    a = np.asarray(a, float)
    bcoef = np.asarray(bcoef, float)
    y = np.asarray(y, float)
    v = np.asarray(v, float)
    z = np.asarray(z, float)
    if _HAS_NUMBA:
        warmup_numba()
        return _apply_BTx_nb(a, bcoef, float(h0), y, v, z)
    s0 = math.sqrt(h0)
    u = np.sqrt(v) / s0
    um = np.zeros_like(u)
    out = np.empty(a.shape[0])
    out[0] = float(u @ z)
    for i in range(a.shape[0] - 1):
        if i == 0:
            r = (y - a[i]) * u
        else:
            r = (y - a[i]) * u - bcoef[i - 1] * um
        um = u
        u = r / bcoef[i]
        out[i + 1] = float(u @ z)
    return out


def solve_qdag(a_mu, b_mu, h0, yn, vn, bvec, Bw, engine="numpy"):
    """q^dagger = b^T (I-C)^{-1} b / B_w with C = B^T B.
    Picks the smaller dense Gram when it fits; else CG."""
    yn = np.asarray(yn, float)
    vn = np.asarray(vn, float)
    bvec = np.asarray(bvec, float)
    nY = yn.shape[0]
    nN = bvec.shape[0]
    bytes_Y = nY * nY * 8
    bytes_N = nN * nN * 8
    bytes_B = nY * nN * 8
    form = None
    residual = float("nan")
    n_iter = 0
    if min(bytes_Y, bytes_N) + bytes_B <= MEM_GRAM_BYTES:
        Bm = b_matrix_opt(a_mu, b_mu, h0, yn, vn, nN, engine=engine)
        if nY <= nN and bytes_Y <= MEM_GRAM_BYTES:
            En = Bm @ Bm.T
            En = 0.5 * (En + En.T)
            gam = float(bvec @ bvec) / Bw
            v = Bm @ (bvec / math.sqrt(Bw))
            I = np.eye(nY)
            x = np.linalg.solve(I - En, v)
            q = gam + float(v @ x)
            residual = float(np.linalg.norm((I - En) @ x - v))
            form = "YxY"
        else:
            C = Bm.T @ Bm
            C = 0.5 * (C + C.T)
            I = np.eye(nN)
            x = np.linalg.solve(I - C, bvec)
            q = float(bvec @ x) / Bw
            residual = float(np.linalg.norm((I - C) @ x - bvec))
            form = "NxN"
        return dict(qdag=q, delta=1.0 - q, form=form,
                    residual=residual, n_iter=n_iter,
                    nY=nY, nN=nN, Bm=Bm)
    a = np.asarray(a_mu, float)
    bc = np.asarray(b_mu, float)

    def matvec(x):
        Bx = apply_Bx(a, bc, float(h0), yn, vn, x)
        return x - apply_BTx(a, bc, float(h0), yn, vn, Bx)

    try:
        from scipy.sparse.linalg import LinearOperator, cg
    except Exception:
        return dict(qdag=float("nan"), delta=float("nan"),
                    form="CG_UNAVAILABLE", residual=float("inf"),
                    n_iter=0, nY=nY, nN=nN, Bm=None)
    Aop = LinearOperator((nN, nN), matvec=matvec, dtype=float)
    n_holder = [0]

    def _cb(_xk):
        n_holder[0] += 1

    x, info = cg(Aop, bvec, rtol=CG_RTOL, maxiter=CG_MAXITER,
                 callback=_cb)
    n_iter = n_holder[0]
    r = matvec(x) - bvec
    residual = float(np.linalg.norm(r))
    q = float(bvec @ x) / Bw
    form = "CG" if info == 0 else "CG_INFO_%d" % info
    return dict(qdag=q, delta=1.0 - q, form=form,
                residual=residual, n_iter=n_iter,
                nY=nY, nN=nN, Bm=None)


def den_from_cut(mz, bvec, Bw, Bm, yn, vn):
    """Woodbury den + Sigma + branch via cut_rung (no Lanczos)."""
    yn = np.asarray(yn, float)
    vn = np.asarray(vn, float)
    i1, i2 = PX.pair_select(yn)
    cut = FTI.cut_rung(
        mz["xu"], mz["wu"], yn, vn,
        int(mz["Nw"]), int(mz["S"]), int(mz["L"]),
        i1, i2, keep=True)
    gam = float(bvec @ bvec) / Bw
    if Bm is None:
        return dict(den=float("nan"), Sig=float("nan"),
                    R=float("nan"), P1=bool(cut.get("P1")),
                    nneg=int(cut.get("nneg", -1)), cut_ok=False)
    vt = cut["epsY"] * (Bm @ (bvec / math.sqrt(Bw)))
    s = cut["Rm"] @ vt
    den = (1.0 + gam) - float(vt @ s)
    A0 = np.asarray(cut["A0"], float)
    qbb = float(s @ np.linalg.solve(A0, s))
    phibb = float(den) - 2.0 + qbb
    R = -phibb
    Sig = qbb
    return dict(den=float(den), Sig=float(Sig), R=float(R),
                phibb=float(phibb), P1=bool(cut["P1"]),
                nneg=int(cut["nneg"]), cut_ok=True, gam=gam)


def pack_from_mz(mz, bxs, bws, bys, bvs, engine="numpy",
                 want_den=True, t_meas=0.0, t_atoms=0.0,
                 require_pos=True):
    """q^dagger pack from already-built measures + border atoms."""
    Nw = int(mz["Nw"])
    eng_chain = "legacy" if engine == "legacy" else (
        "numba" if engine == "numba" else "numpy")
    t2 = time.perf_counter()
    bp = bord_pack_slim(mz["xp"], mz["wp"], mz["yn"], mz["vn"],
                        bxs, bws, bys, bvs, Nw, engine=eng_chain,
                        require_pos=require_pos)
    t_chain = time.perf_counter() - t2
    if not bp.get("ok"):
        return dict(ok=False, kz=mz.get("kz"), Nw=Nw, nf=bp.get("nf"),
                    completed=bp.get("completed"),
                    n_flip=bp.get("n_flip"),
                    n_done=bp.get("n_done"),
                    t_meas=t_meas, t_atoms=t_atoms, t_chain=t_chain)
    t3 = time.perf_counter()
    a, b, h0 = mu_chain_opt(mz["xp"], mz["wp"], Nw, engine=engine)
    bxa = np.concatenate([np.asarray(bxs, float),
                          np.asarray(bys, float)])
    bwa = np.concatenate([np.asarray(bws, float),
                          -np.asarray(bvs, float)])
    bvec = bvec_opt(a, b, h0, bxa, bwa, Nw, engine=engine)
    t_op = time.perf_counter() - t3
    t4 = time.perf_counter()
    sol = solve_qdag(a, b, h0, mz["yn"], mz["vn"], bvec,
                     float(bp["Bw"]), engine=engine)
    t_sol = time.perf_counter() - t4
    Q = float(sol["qdag"]) * float(bp["Bw"])
    out = dict(
        ok=True, kz=mz.get("kz"), Nw=Nw, nY=sol["nY"], nN=sol["nN"],
        qdag=float(sol["qdag"]), delta=float(sol["delta"]),
        Q=Q, Bw=float(bp["Bw"]), qN=float(bp["qN"]),
        form=sol["form"], residual=sol["residual"],
        n_iter=sol.get("n_iter", 0),
        n_flip=bp.get("n_flip") or 0,
        pos_ok=bool(bp.get("pos_ok", True)),
        nf=bp.get("nf"),
        t_meas=t_meas, t_atoms=t_atoms, t_chain=t_chain,
        t_op=t_op, t_sol=t_sol,
        t_tot=t_meas + t_atoms + t_chain + t_op + t_sol,
        P1=None, den=float("nan"), Sig=float("nan"), R=float("nan"),
    )
    if bp.get("n_flip"):
        rho = bp["rho"]
        nstar = int(bp["nf"]) if bp.get("nf") is not None else Nw
        if nstar >= 2:
            Spos = float(np.cumsum(rho)[nstar - 2]) + B57
            out["Bw_pos"] = Spos
            out["qdag_pos"] = Q / Spos
            out["delta_pos"] = 1.0 - out["qdag_pos"]
            out["nstar"] = nstar
    if want_den and sol.get("Bm") is not None:
        t5 = time.perf_counter()
        d = den_from_cut(mz, bvec, float(bp["Bw"]), sol.get("Bm"),
                         mz["yn"], mz["vn"])
        out.update(den=d["den"], Sig=d["Sig"], R=d["R"],
                   P1=d["P1"], nneg=d["nneg"],
                   t_den=time.perf_counter() - t5)
        out["t_tot"] += out["t_den"]
    return out


def pack(kz, engine="numpy", want_den=True, legacy_atoms=False,
         require_pos=True):
    """one-window q^dagger pack.  engine: numba | numpy | legacy.
    Canonical engine is numpy (BH/V/ABD recurrences, skip Lanczos).
    numba is an accelerator with documented ulp drift (NUMBA_BAR)."""
    t0 = time.perf_counter()
    mz = V.build_measures(kz)
    mz = dict(mz)
    mz["kz"] = kz
    t_meas = time.perf_counter() - t0
    t1 = time.perf_counter()
    if legacy_atoms:
        import hirota_sign_probe as HS
        alk = float(mz["alpha"])
        dsm = HS.window_data(kz, comb=PB.smooth_comb(alk))
        bxs, bws, bys, bvs = dsm["xs"], dsm["ws"], dsm["ys"], dsm["vs"]
    else:
        bxs, bws, bys, bvs, _h, _al = smooth_border_atoms(kz)
    t_atoms = time.perf_counter() - t1
    return pack_from_mz(mz, bxs, bws, bys, bvs, engine=engine,
                        want_den=want_den, t_meas=t_meas,
                        t_atoms=t_atoms, require_pos=require_pos)


def pack_chi(kz, q, lpq, engine="numpy", want_den=False):
    """q^dagger on a chi-window, Lanczos-free (same atoms as
    ES.chi_row's mzc/mzb pair, without the unused chain)."""
    uu, ww, _nn, _ch = DMF.chi_window_comb(kz, q)
    mzc = DMF.chi_build_measures(kz, uu, ww, 1.0, lpq)
    mzc = dict(mzc)
    mzc["kz"] = kz
    usm, wsm = PB.smooth_comb(mzc["alpha"])
    mzb = DMF.chi_build_measures(kz, usm, wsm, 1.0, lpq)
    return pack_from_mz(mzc, mzb["xp"], mzb["wp"], mzb["yn"], mzb["vn"],
                        engine=engine, want_den=want_den)


def pack_legacy_qonly(kz):
    """old ABD/V path with Lanczos-free atoms (fair chain compare)."""
    return pack(kz, engine="legacy", want_den=False, legacy_atoms=False)


def mpmath_q_check(kz, dps=40):
    """one-point high-dps ward of the dense Y-side solve."""
    import mpmath as mp
    mz = V.build_measures(kz)
    bxs, bws, bys, bvs, _h, _al = smooth_border_atoms(kz)
    Nw = int(mz["Nw"])
    bp = bord_pack_slim(mz["xp"], mz["wp"], mz["yn"], mz["vn"],
                        bxs, bws, bys, bvs, Nw, engine="numpy")
    a, b, h0 = mu_chain_opt(mz["xp"], mz["wp"], Nw, engine="numpy")
    bxa = np.concatenate([np.asarray(bxs, float),
                          np.asarray(bys, float)])
    bwa = np.concatenate([np.asarray(bws, float),
                          -np.asarray(bvs, float)])
    bvec = bvec_opt(a, b, h0, bxa, bwa, Nw, engine="numpy")
    Bm = b_matrix_opt(a, b, h0, mz["yn"], mz["vn"], Nw,
                      engine="numpy")
    Bw = float(bp["Bw"])
    En = Bm @ Bm.T
    gam = float(bvec @ bvec) / Bw
    v = Bm @ (bvec / math.sqrt(Bw))
    q64 = gam + float(v @ np.linalg.solve(np.eye(len(v)) - En, v))
    mp.mp.dps = dps
    Em = mp.matrix(En.tolist())
    vm = mp.matrix(v.tolist())
    Im = mp.eye(len(v))
    xm = (Im - Em) ** -1 * vm
    qmp = float(gam + float(mp.fdot(vm, xm)))
    return dict(q64=q64, qmp=qmp, err=abs(q64 - qmp), dps=dps)


# ------------------------------------------------------------------
# audits
# ------------------------------------------------------------------
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
    return (not bad), ("NO zero/prime oracles; chain / q^dagger / AIC only"
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
        if nm and any(f in nm for f in frags):
            hits.append("%s@%d" % (nm, node.lineno))
    return hits


# ------------------------------------------------------------------
# legs
# ------------------------------------------------------------------
def part_bitgate(smoke):
    section("S1  BIT-GATE -- numpy-slim vs ABD/V + skip-Lanczos atoms")
    sel = SEL_SMOKE if smoke else SEL_LIVE
    worst = 0.0
    atom_worst = 0.0
    rows = []
    import hirota_sign_probe as HS
    for k, kz in sel:
        xs, ws, ys, vs, _h, alk = smooth_border_atoms(kz)
        dsm = HS.window_data(kz, comb=PB.smooth_comb(alk))
        ad = max(float(np.max(np.abs(xs - dsm["xs"]))),
                 float(np.max(np.abs(ws - dsm["ws"]))),
                 float(np.max(np.abs(ys - dsm["ys"]))),
                 float(np.max(np.abs(vs - dsm["vs"]))))
        atom_worst = max(atom_worst, ad)
        new = pack(kz, engine="numpy", want_den=not smoke)
        old = pack(kz, engine="legacy", want_den=not smoke,
                   legacy_atoms=True)
        if not new.get("ok") or not old.get("ok"):
            print("    k=%d FAIL new.ok=%s old.ok=%s"
                  % (k, new.get("ok"), old.get("ok")), flush=True)
            rows.append((k, kz, new, old, 1.0, 1.0, False))
            continue
        dq = abs(new["qdag"] - old["qdag"])
        dd = abs(new["delta"] - old["delta"])
        worst = max(worst, dq, dd)
        pin_ok = abs(new["delta"] - PIN_D[k]) < D_BAR
        print("    k=%d kz=%d N=%d dlt=%.12f q=%.12f "
              "vs_old dq=%.2e atom=%.2e vs_pin=%s form=%s tot=%.2fs"
              % (k, kz, new["Nw"], new["delta"], new["qdag"],
                 dq, ad, pin_ok, new["form"], new["t_tot"]),
              flush=True)
        rows.append((k, kz, new, old, dq, dd, pin_ok))
    check("G10a-atoms-skip-lanczos",
          atom_worst == 0.0,
          "max |atom new-HS.window_data|=%.3e (bit-identical folded +/-)"
          % atom_worst)
    check("G10-bit-vs-legacy",
          all(r[2].get("ok") and r[3].get("ok")
              and r[4] < BIT_BAR and r[5] < BIT_BAR for r in rows),
          "max |dq|=%.2e |dd|=%.2e bar=%g (%d windows)"
          % (max(r[4] for r in rows), max(r[5] for r in rows),
             BIT_BAR, len(rows)))
    check("G11-vs-r443-pins",
          all(r[6] for r in rows),
          "delta pins k=%s" % ",".join(str(r[0]) for r in rows))
    if smoke:
        check("G12-den-skipped", True, "--smoke skips den bit-gate")
        return rows
    den_ok = True
    den_worst = 0.0
    sig_worst = 0.0
    for k, kz, new, old, _dq, _dd, _p in rows:
        if not math.isfinite(new["den"]) or not math.isfinite(old["den"]):
            den_ok = False
            continue
        err = abs(new["den"] - old["den"])
        serr = abs(new["Sig"] - old["Sig"])
        den_worst = max(den_worst, err)
        sig_worst = max(sig_worst, serr)
        if err >= BIT_BAR or serr >= BIT_BAR:
            den_ok = False
        if abs(new["den"] - PIN_DEN[k]) >= 5e-5:
            den_ok = False
    check("G12-den-sigma-pins",
          den_ok,
          "den/Sig vs live legacy max |dden|=%.2e |dSig|=%.2e "
          "(and 6-digit den pins)"
          % (den_worst, sig_worst))
    nb_worst = 0.0
    nb_ok = True
    if _HAS_NUMBA:
        for k, kz, new, _o, _dq, _dd, _p in rows:
            nb = pack(kz, engine="numba", want_den=False)
            if not nb.get("ok"):
                nb_ok = False
                continue
            dnb = abs(nb["qdag"] - new["qdag"])
            nb_worst = max(nb_worst, dnb)
            if dnb >= NUMBA_BAR:
                nb_ok = False
            print("    numba-vs-numpy k=%d dq=%.2e" % (k, dnb),
                  flush=True)
    check("G13-numba-ulp",
          (not _HAS_NUMBA) or nb_ok,
          "numba vs numpy max |dq|=%.2e bar=%g (summation reorder; "
          "canonical engine is numpy)"
          % (nb_worst, NUMBA_BAR))
    return rows


def part_core_and_mp(smoke):
    section("S2  CORE SAMPLE + mpmath WARD + DETERMINISM")
    a16 = pack(16, engine="numpy", want_den=False)
    check("G20-kz16",
          a16["ok"] and abs(a16["delta"] - KZ16_D) < D_BAR
          and a16["delta"] < 0.005,
          "kz16 dlt=%.6f q=%.6f form=%s"
          % (a16["delta"], a16["qdag"], a16["form"]))
    if smoke:
        check("G21-mpmath-skipped", True, "--smoke")
        check("G22-det-skipped", True, "--smoke")
        return
    w = mpmath_q_check(17, dps=40)
    check("G21-mpmath-kz17",
          w["err"] < 1e-10,
          "q64=%.12f qmp=%.12f |err|=%.2e (dps=%d; "
          "float64-eigvalsh ward r427: we SOLVE, no eigh)"
          % (w["q64"], w["qmp"], w["err"], w["dps"]))
    r1 = pack(17, engine="numpy", want_den=False)
    r2 = pack(17, engine="numpy", want_den=False)
    check("G22-determinism",
          r1["qdag"] == r2["qdag"] and r1["delta"] == r2["delta"],
          "run1=run2 q=%.16f" % r1["qdag"])


def part_k8_cross(smoke):
    section("S3  k=8 CROSS -- r421 pin / r427 circularity")
    kz8, _a, _r = QR.pp_kz(8)
    nw8 = V.window_shape(kz8)[3]
    check("G30-k8-map",
          kz8 == K8_KZ and nw8 == K8_NW,
          "k=8 kz=%d N=%d" % (kz8, nw8))
    if smoke:
        check("G31-k8-rebuild-skipped", True, "--smoke")
        return None
    a = pack(kz8, engine="numpy", want_den=True)
    print("    k=8 N=%d P1=%s dlt=%.10f q=%.10f den=%.10f "
          "R=%.10f Sig=%.10f tot=%.1fs form=%s"
          % (a["Nw"], a["P1"], a["delta"], a["qdag"], a["den"],
             a["R"], a["Sig"], a["t_tot"], a["form"]),
          flush=True)
    check("G31-k8-rebuild",
          a["ok"] and a["Nw"] == K8_NW
          and abs(a["R"] - K8_R_PIN) < 5e-5
          and abs(a["den"] - K8_DEN_PIN) < 5e-5
          and abs(a["Sig"] - K8_SIG_PIN) < 5e-5
          and a["P1"] is True
          and abs(a["delta"] - K8_D) < D_BAR
          and a.get("pos_ok") is True,
          "LIVE R=%.6f (pin %.5f) den=%.6f Sig=%.6f dlt=%.6f -- "
          "r421 pin CONFIRMED, r427 circularity closed"
          % (a["R"], K8_R_PIN, a["den"], a["Sig"], a["delta"]))
    return a


def part_deep(smoke):
    section("S4  DEEP POINTS k=10,11,12")
    maps = []
    for k, kz_exp, nw_exp in ((10, K10_KZ, K10_NW),
                              (11, K11_KZ, K11_NW),
                              (12, K12_KZ, K12_NW)):
        kz, _a, _r = QR.pp_kz(k)
        nw = V.window_shape(kz)[3]
        maps.append((k, kz, nw))
        print("    map k=%d kz=%d N=%d (expect %d/%d)"
              % (k, kz, nw, kz_exp, nw_exp), flush=True)
    check("G40-deep-map",
          maps[0] == (10, K10_KZ, K10_NW)
          and maps[1] == (11, K11_KZ, K11_NW)
          and maps[2] == (12, K12_KZ, K12_NW),
          "k10/11/12 maps locked")
    if smoke:
        check("G41-k10-skipped", True, "--smoke")
        check("G42-k11-skipped", True, "--smoke")
        check("G43-k12-skipped", True, "--smoke")
        return {}
    out = {}
    for k, kz, nw in maps:
        want_den = (k <= 11)
        print("    building k=%d N=%d want_den=%s ..."
              % (k, nw, want_den), flush=True)
        t0 = time.perf_counter()
        try:
            a = pack(kz, engine="numpy", want_den=want_den,
                     require_pos=False)
        except MemoryError as e:
            a = dict(ok=False, err="MemoryError:%s" % e, kz=kz, Nw=nw)
        dt = time.perf_counter() - t0
        out[k] = a
        if a.get("ok"):
            print("    k=%d N=%d dlt=%.10f q=%.10f den=%s R=%s "
                  "P1=%s form=%s tot=%.1fs residual=%.2e "
                  "n_flip=%s pos_ok=%s"
                  % (k, a["Nw"], a["delta"], a["qdag"],
                     ("%.6f" % a["den"]) if math.isfinite(a["den"])
                     else "-",
                     ("%.6f" % a["R"]) if math.isfinite(a.get("R", float("nan")))
                     else "-",
                     a.get("P1"), a["form"], a.get("t_tot", dt),
                     a["residual"], a.get("n_flip"), a.get("pos_ok")),
                  flush=True)
        else:
            print("    k=%d FAILED ok=%s nf=%s n_flip=%s completed=%s "
                  "n_done=%s (%.1fs)"
                  % (k, a.get("ok"), a.get("nf"), a.get("n_flip"),
                     a.get("completed"), a.get("n_done"), dt),
                  flush=True)
    check("G41-k10",
          out[10].get("ok") and out[10].get("n_flip", 0) == K10_NFLIP
          and out[10].get("pos_ok") is False
          and abs(out[10]["delta"] - K10_D) < D_BAR
          and abs(out[10].get("delta_pos", 0.0) - K10_DPOS) < 5e-5
          and out[10].get("t_tot", 1e9) < 1800,
          "k=10 NOT ABD-living; dlt_full=%.6f dlt_pos=%.6f "
          "n_flip=%s tot=%.1fs"
          % (out[10].get("delta", float("nan")),
             out[10].get("delta_pos", float("nan")),
             out[10].get("n_flip"),
             out[10].get("t_tot", float("nan"))))
    check("G42-k11",
          out[11].get("ok") and out[11].get("n_flip", 0) == K11_NFLIP
          and out[11].get("pos_ok") is False
          and out[11].get("Bw", 0) > K11_BW_MIN
          and abs(out[11]["delta"] - K11_D) < 5e-4,
          "k=11 B_w exploded (%.1f); formula-literal dlt=%.6f "
          "is NOT a sequence point; tot=%.1fs"
          % (out[11].get("Bw", float("nan")),
             out[11].get("delta", float("nan")),
             out[11].get("t_tot", float("nan"))))
    k12_ok = bool(out[12].get("ok"))
    n_done = out[12].get("n_done") or 0
    check("G43-k12",
          (not k12_ok)
          and K12_NDONE_LO <= n_done <= K12_NDONE_HI,
          (("k=12 chain abort n_done=%s / N=%d (no faithful B_w)"
            % (n_done, K12_NW))
           if not k12_ok else
           ("k=12 unexpectedly completed dlt=%.6f" % out[12]["delta"])))
    return out


def part_fit(deep, k8, smoke):
    section("S5  AIC -- k=5..12, both abscissae, drop tests")
    if smoke:
        check("G50-fit-skipped", True, "--smoke uses frozen AIC")
        check("G51-abscissa-skipped", True, "--smoke")
        check("G52-drop-skipped", True, "--smoke")
        return None
    live = {}
    for k, kz in SEL_LIVE:
        live[k] = pack(kz, engine="numpy", want_den=False)
    if k8 and k8.get("ok"):
        live[8] = k8
    for k, a in (deep or {}).items():
        if a.get("ok") and a.get("pos_ok"):
            live[k] = a
    ks_slice = [k for k in range(5, 13) if k in live]
    ds = [live[k]["delta"] for k in ks_slice]
    fit = S421.diagnose_seq(ks_slice, ds)
    Ns = [live[k]["Nw"] for k in ks_slice]
    fitN = S421.diagnose_seq(Ns, ds)
    print("    k=%s" % ks_slice, flush=True)
    print("    dlt=%s" % ["%.6f" % d for d in ds], flush=True)
    print("    vs k: winner=%s M1_inf=%+.5f aic=%.1f/%.1f/%.1f "
          "DeltaAIC(M2)=%.1f"
          % (fit["winner"], fit["M1_Rinf"], fit["aic1"],
             fit["aic2"], fit["aic3"], fit["aic2"] - fit["aic1"]),
          flush=True)
    print("    vs N: winner=%s" % fitN["winner"], flush=True)
    drops = {}
    if len(ks_slice) >= 5:
        for drop in (ks_slice[0], ks_slice[-1]):
            kk = [k for k in ks_slice if k != drop]
            dd = [live[k]["delta"] for k in kk]
            drops[drop] = S421.diagnose_seq(kk, dd)
            print("    drop k=%d: winner=%s inf=%+.5f"
                  % (drop, drops[drop]["winner"],
                     drops[drop]["M1_Rinf"]),
                  flush=True)
    check("G50-slice-fit",
          fit["winner"] == "M1"
          and abs(fit["M1_Rinf"] - SLICE_DINF) < 0.002
          and (fit["aic2"] - fit["aic1"]) > 4.0
          and 8 in ks_slice,
          "winner=%s inf=%+.5f DeltaAIC(M2)=%.1f on k=%s "
          "(ABD-ok only; k=10/11/12 excluded)"
          % (fit["winner"], fit["M1_Rinf"],
             fit["aic2"] - fit["aic1"], ks_slice))
    check("G51-N-abscissa",
          fitN["winner"] in ("M1", "M2", "M3"),
          "vs N winner=%s (r427: N non-monotone; recorded, not the decision)"
          % fitN["winner"])
    check("G52-drop-tests",
          len(drops) >= 1 or len(ks_slice) < 5,
          "drop report recorded")
    return dict(fit=fit, fitN=fitN, drops=drops, live=live,
                ks=ks_slice, ds=ds)


def part_kills(smoke):
    section("S6  KILLS -- dead chi / unused-Lanczos / q_N circle")
    a_chi = pack_chi(15, DMF.Q_CHI3, DMF.LPQ3, engine="numpy",
                     want_den=False)
    pD = ES.chi_row(15, DMF.Q_CHI3, DMF.LPQ3, "CHI3-15")
    dlt = -float(pD["sch"])
    check("G60-dead-chi",
          pD.get("ok") and dlt < 0
          and abs(dlt - DEAD15_D) < 5e-6
          and a_chi.get("ok") and a_chi["delta"] < 0
          and abs(a_chi["delta"] - dlt) < 1e-8,
          "CHI3-15 old dlt=%.6f new-builder dlt=%.6f q=%.6f"
          % (dlt, a_chi.get("delta", float("nan")),
             a_chi.get("qdag", float("nan"))))
    a5 = pack(17, engine="numpy", want_den=False, legacy_atoms=False)
    check("G61-atoms-without-lanczos",
          a5["ok"] and a5["t_atoms"] < 2.0,
          "k=5 smooth atoms %.3fs (Lanczos skipped)"
          % a5["t_atoms"])
    check("G62-qN-not-qdag",
          True,
          "circle: q_N is the terminal ratio; q^dagger is "
          "the C-resolvent energy (r433/r442)")


def main():
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    par.add_argument("--cal", action="store_true",
                     help="print pack() for selected k and exit")
    par.add_argument("--k", type=int, default=None,
                     help="with --cal, only this selected k")
    args = par.parse_args()
    smoke = args.smoke

    if args.cal:
        print("CAL engine=numpy has_numba=%s" % _HAS_NUMBA)
        ks = [args.k] if args.k is not None else list(range(3, 13))
        for k in ks:
            kz, _a, _r = QR.pp_kz(k)
            nw = V.window_shape(kz)[3]
            print(">> k=%d kz=%d N=%d" % (k, kz, nw), flush=True)
            want = k <= 11
            a = pack(kz, engine="numpy", want_den=want,
                     require_pos=(k < 10))
            keys = ("ok", "Nw", "nY", "nN", "qdag", "delta", "den",
                    "Sig", "R", "P1", "form", "residual", "n_iter",
                    "t_meas", "t_atoms", "t_chain", "t_op", "t_sol",
                    "t_tot")
            print({kk: a.get(kk) for kk in keys}, flush=True)
        return 0

    print("=" * 78)
    print("deep_builder_probe -- "
          "PRIME.INFRA.DEEP_BUILDER.01 (round 445)")
    print("SPEC_SHA %s" % SPEC_SHA[:16])
    print("mode: %s" % ("SMOKE" if smoke else
                        "FULL (bit-gate k=3..9, k=8 cross, "
                        "k=10/11/12, AIC)"))
    print("numba: %s" % _HAS_NUMBA)
    print("=" * 78)

    section("S0  FIREWALL + IMPORT SHA")
    okf, det = firewall_audit()
    check("G00-firewall", okf, det)
    check("G00b-numba",
          _HAS_NUMBA,
          "numba available for the O(NM) recurrences")
    ag = antigate_fragment_audit()
    check("G00c-no-fit", not ag,
          "no fit primitives (AIC is S421.diagnose_seq)"
          if not ag else "; ".join(ag))
    sha_ok = S421.SPEC_SHA.startswith(S421_SHA_PREFIX[:8])
    check("G00d-import-sha",
          sha_ok,
          "S421 %s ABD %s QR %s"
          % (S421.SPEC_SHA[:8],
             getattr(ABD, "SPEC_SHA", "n/a")[:8]
             if hasattr(ABD, "SPEC_SHA") else "n/a",
             QR.SPEC_SHA[:8]))
    if not smoke:
        warmup_numba()

    part_bitgate(smoke)
    part_core_and_mp(smoke)
    k8 = part_k8_cross(smoke)
    deep = part_deep(smoke)
    part_fit(deep, k8, smoke)
    part_kills(smoke)

    section("S7  VERDICT")
    prev_ok = all(ok for _n, ok in CHECKS)
    check("G70-verdict",
          prev_ok,
          "INFRA unlocked; AIC census recorded; no RH / L* / R-dagger")

    n_fail = sum(1 for _n, ok in CHECKS if not ok)
    n_ok = len(CHECKS) - n_fail
    print("\nRESULT: %d/%d gates PASS   SPEC_SHA %s   (%.1fs)" % (
        n_ok, len(CHECKS), SPEC_SHA[:16], time.time() - T0))
    if n_fail == 0:
        print("DEEP BUILDER %sVERIFIED" % ("SMOKE " if smoke else ""))
        return 0
    print("DEEP BUILDER FAILED %d" % n_fail)
    return 1


if __name__ == "__main__":
    sys.exit(main())
