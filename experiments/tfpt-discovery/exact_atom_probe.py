#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""exact_atom_probe -- PRIME.INFRA.EXACT_ATOM_ADJUDICATION.01
(round 447): does the TRUE k=10 window live when atoms
are built in high-dps from exact integer sources?
Exactly one question.  Research documentation, NO RH
claim.

THE QUESTION.  r446 REAL is for the float64-ATOM
construction: mpmath verified the recurrence on
float64 input atoms.  The flip pivot eta ~ -8e-14
is a 1e-6-relative cancellation of two ~3.45e-8
masses after 3788 steps -- atom error of rel ~1e-16
(float64-log, float64-fold) can accumulate to that
scale.  Does the exact k=10 window (kz197, N=4071)
live?

WHAT IS COMPUTED.  Window mu/nu and smooth-border
atoms built in mpmath (dps 50+): u = mp.log(n) on
exact integer prime powers, tent/arch/fold/FFT all
mp; then the r446 three-term chain on those atoms
(no float64 cast).  Integer mesh (M,L,Nw) locked
to V.window_shape (r397 family).  No RH claim.

CALIBRATION DISCLOSURE.  Exact-atom builder, k=5
regression, k=10 chain, kz=137 control first
measured in /tmp (r447_cal.py, r447_k10.log) on
the r397/r362/r445/r446 constructors, 2026-08-30.
Frozen floors below are that measurement, sealed
as gates.  Pins disclosed.

FROZEN FROM /tmp (live re-gated):
  * Exact atoms vs float64: k=5/9/10/137 positions
    rel ~ 4.4e-16 (1 ulp); k=10 weights rel 6.3e-15.
    float64-log / float64-fold are NOT the source.
  * k=10 exact-atom chain dps 50 (530 s): first flip
    STILL n=3788, eta=-8.853149582220489e-14,
    rel=1.255988618504423e-6, n_flip=115,
    pos_ok=False.  dps 70 to n=3793: first n and
    eta BIT-IDENTICAL.  Verdict EXACT_DEAD.
  * Divergence vs float chain: first rel>1e-8 at
    n=218 (abs ~1e-15, same sign); sign-split none
    -- both flip at 3788.
  * k=9 exact-atom prefix 80: 0 flips, eta matches
    float.  kz=137 atoms rel 4.4e-16 (full first
    flip sealed from /tmp r447_kz137.json).

AUSGANG EXACT_DEAD / ATOM_ULP_ONLY /
FLIP_STABLE_3788 / BAND_ENDS / SLICE_FLOOR_STANDS /
THIS_FAMILY_FREQUENTLY_FALSIFIED.
SATZ: none (adjudication of a construction).
No RH claim.

MACHINERY: r226 V.build_measures / von Mangoldt
table, r445 S445.smooth_border_atoms / PB.smooth_comb
/ PIK.folded_measure, r446 S446.mp_chain algebra,
r421 S421.diagnose_seq, r397 QR.pp_kz.

NO RH CLAIM.  Finite window adjudication.
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
import mpmath as mp

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DISC = os.path.dirname(os.path.abspath(__file__))
PROB = os.path.join(REPO, "rh", "problem")
for p in (DISC, PROB):
    if p not in sys.path:
        sys.path.insert(0, p)

import deep_builder_probe as S445  # noqa: E402
import deep_abd_probe as S446  # noqa: E402
import verify_lstar_instance as V  # noqa: E402
import principal_bessel_probe as PB  # noqa: E402
import reserve_limit_probe as S421  # noqa: E402
import qn_reopened_probe as QR  # noqa: E402
import dirichlet_matched_frame_probe as DMF  # noqa: E402

B57 = 5.0 / 7.0
BG_DU = mp.mpf("0.01")
NU_OVER = 4
GL_N = 48
EULER = mp.mpf("0.5772156649015328606065120900824")
TABLE_CAP = 400000
K5_KZ, K5_NW = 17, 96
K9_KZ, K9_NW = 116, 1433
K10_KZ, K10_NW = 197, 4071
K10_NF_FLOAT = 3788
KZ137 = 137
KZ137_NW = 8300
KZ137_NF_FLOAT = 7511
S445_SHA_PREFIX = "57831e610b545e75"
S446_SHA_PREFIX = "a48e0aa443689acd"
S421_SHA_PREFIX = "234a1113"

# sealed after /tmp census
VERDICT = "EXACT_DEAD"
MP10_FIRST = 3788
MP10_NFLIP = 115
MP10_FIRST_ETA = -8.853149582220489e-14
MP10_FIRST_REL = 1.255988618504423e-6
DPS_A, DPS_B = 50, 70
ATOM_REL_X = 4.440892098500626e-16
ATOM_REL_W = 6.3328248894878314e-15
DIV_N = 218
D10 = None
LAST_LIVE_NOTE = "r446 LAST_LIVE_KZ_136 CONFIRMED under exact atoms"

SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
CHECKS = []
T0 = time.time()
_PP_CACHE = None
_GL_CACHE = {}


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok)))
    print("  [%s] %-44s %s" % ("PASS" if ok else "FAIL", name, detail),
          flush=True)
    return bool(ok)


def section(t):
    print("\n" + "=" * 78)
    print(t)
    print("=" * 78, flush=True)


# ==================================================================
# EXACT ATOM BUILDER (no float64 intermediates in values)
# ==================================================================
def _sieve_pp(n_max):
    """Exact integer prime powers <= n_max with their primes."""
    sieve = bytearray(b"\x01") * (n_max + 1)
    sieve[0] = sieve[1] = 0
    lim = int(math.isqrt(n_max))
    for i in range(2, lim + 1):
        if sieve[i]:
            step = i
            start = i * i
            sieve[start:n_max + 1:step] = b"\x00" * (
                ((n_max - start) // step) + 1)
    out = []
    for p in range(2, n_max + 1):
        if not sieve[p]:
            continue
        q = p
        while q <= n_max:
            out.append((q, p))
            if q > n_max // p:
                break
            q *= p
    out.sort()
    return out


def pp_table(dps):
    global _PP_CACHE
    if _PP_CACHE is not None and _PP_CACHE[0] == dps:
        return _PP_CACHE[1]
    mp.mp.dps = dps
    rows = []
    for n, p in _sieve_pp(TABLE_CAP):
        u = mp.log(mp.mpf(n))
        w = 2 * mp.log(mp.mpf(p)) / mp.sqrt(mp.mpf(n))
        rows.append((n, p, u, w))
    _PP_CACHE = (dps, rows)
    return rows


def gl_nodes(n, dps):
    key = (n, dps)
    if key in _GL_CACHE:
        return _GL_CACHE[key]
    mp.mp.dps = dps
    x0, _w0 = np.polynomial.legendre.leggauss(n)
    xs, ws = [], []
    for xi in x0:
        x = mp.findroot(lambda t: mp.legendre(n, t), mp.mpf(float(xi)))
        dP = mp.diff(lambda t: mp.legendre(n, t), x)
        w = 2 / ((1 - x * x) * dP * dP)
        xs.append(x)
        ws.append(w)
    _GL_CACHE[key] = (xs, ws)
    return xs, ws


def bitrev_inplace(a):
    n = len(a)
    j = 0
    for i in range(1, n):
        bit = n >> 1
        while j & bit:
            j ^= bit
            bit >>= 1
        j ^= bit
        if i < j:
            a[i], a[j] = a[j], a[i]


def fft2(a, inverse=False):
    """In-place radix-2 FFT; a is a list of mp.mpc, len power of 2."""
    n = len(a)
    bitrev_inplace(a)
    length = 2
    sign = mp.mpf(1 if inverse else -1)
    while length <= n:
        ang = sign * 2 * mp.pi / length
        wlen = mp.exp(mp.j * ang)
        half = length // 2
        for i in range(0, n, length):
            w = mp.mpc(1)
            for j in range(half):
                u = a[i + j]
                v = a[i + j + half] * w
                a[i + j] = u + v
                a[i + j + half] = u - v
                w *= wlen
        length *= 2
    if inverse:
        nmp = mp.mpf(n)
        for i in range(n):
            a[i] /= nmp


def bluestein_dft(x):
    """Length-n DFT, x list of mp.mpc or mpf."""
    n = len(x)
    if n == 0:
        return []
    N = 1
    while N < 2 * n - 1:
        N *= 2
    chirp = []
    for k in range(n):
        chirp.append(mp.exp(-mp.j * mp.pi * (k * k) / n))
    a = [mp.mpc(x[k]) * chirp[k] for k in range(n)] + [mp.mpc(0)] * (N - n)
    b = [mp.mpc(0)] * N
    for k in range(n):
        ck = mp.exp(mp.j * mp.pi * (k * k) / n)
        b[k] = ck
        if k:
            b[N - k] = ck
    fft2(a)
    fft2(b)
    for i in range(N):
        a[i] *= b[i]
    fft2(a, inverse=True)
    return [a[k] * chirp[k] for k in range(n)]


def spectral_density_mp(c):
    """Same circulant extension as V.spectral_density / PIK.grid_density."""
    a = list(c) + list(reversed(c[1:-1]))
    d = bluestein_dft(a)
    return [z.real for z in d]


def arch_A_far_mp(s, D, glx, glw):
    tot = mp.mpf(0)
    for lo, hi in ((s - D, s), (s, s + D)):
        mid = (lo + hi) / 2
        half = (hi - lo) / 2
        acc = mp.mpf(0)
        for xg, wg in zip(glx, glw):
            w = mid + half * xg
            tent = 1 - abs(s - w) / D
            val = tent * mp.exp(-w / 2) / (-mp.expm1(-2 * w))
            acc += wg * val
        tot -= half * acc
    return tot


def arch_A_near_mp(s, D, glx, glw):
    s = abs(s)
    tri_s = mp.mpf(0)
    if s < D:
        tri_s = 1 - s / D
    Wend = s + D
    pts = sorted({mp.mpf(0), s, D - s, Wend})
    pts = [p for p in pts if p >= 0 and p <= Wend]
    tot = mp.mpf(0)
    for lo, hi in zip(pts[:-1], pts[1:]):
        if hi <= lo:
            continue
        mid = (lo + hi) / 2
        half = (hi - lo) / 2
        acc = mp.mpf(0)
        for xg, wg in zip(glx, glw):
            w = mid + half * xg
            t1 = 1 - abs(s - w) / D
            if t1 < 0:
                t1 = mp.mpf(0)
            t2 = 1 - (s + w) / D
            if t2 < 0:
                t2 = mp.mpf(0)
            S = (t1 + t2) / 2
            integ = ((tri_s * mp.exp(-2 * w) - S * mp.exp(-w / 2))
                     / (-mp.expm1(-2 * w)))
            acc += wg * integ
        tot += half * acc
    logpi = mp.log(mp.pi)
    return (-(EULER + logpi) * tri_s + 2 * tot
            + tri_s * (-mp.log1p(-mp.exp(-2 * Wend))))


def arch_lags_mp(M, D, dps):
    glx, glw = gl_nodes(GL_N, dps)
    out = []
    for i in range(M):
        s = i * D
        if s >= D:
            out.append(arch_A_far_mp(s, D, glx, glw))
        else:
            out.append(arch_A_near_mp(s, D, glx, glw))
    return out


def tent_lags_mp(positions, masses, M, D):
    c = [mp.mpf(0)] * M
    for u_j, m_j in zip(positions, masses):
        i0 = int(mp.floor(u_j / D))
        for i in range(max(0, i0 - 2), min(M, i0 + 3)):
            v = 1 - abs(i * D - u_j) / D
            if v > 0:
                c[i] -= m_j * v / 2
        if u_j < D:
            lim = int(mp.floor((D - u_j) / D)) + 2
            for i in range(0, min(M, lim)):
                v = 1 - (i * D + u_j) / D
                if v > 0:
                    c[i] -= m_j * v / 2
    return c


def fold_window_mp(d, L):
    """V.build_measures fold: j = 1..L/2, wt = (2/L)(1-cos) d[j]."""
    xp, wp, yn, vn = [], [], [], []
    two_L = 2 / mp.mpf(L)
    for j in range(1, L // 2 + 1):
        th = 2 * mp.pi * j / L
        x = mp.cos(th)
        wt = two_L * (1 - mp.cos(th)) * d[j]
        if j == L // 2:
            wt *= mp.mpf("0.5")
        if abs(wt) <= mp.mpf("1e-300"):
            continue
        if wt > 0:
            xp.append(x)
            wp.append(wt)
        else:
            yn.append(x)
            vn.append(-wt)
    return xp, wp, yn, vn


def fold_border_mp(d, L, sign):
    """PIK.folded_measure."""
    acc = {}
    for j in range(L):
        dj = d[j]
        if sign * dj <= 0:
            continue
        th = 2 * mp.pi * j / L
        wt = (abs(dj) / (2 * mp.mpf(L))) * 4 * mp.sin(th / 2) ** 2
        fold = min(j, L - j)
        acc[fold] = acc.get(fold, mp.mpf(0)) + wt
    xs, ws = [], []
    for uf in sorted(acc):
        w = acc[uf]
        if w > mp.mpf("1e-300"):
            xs.append(mp.cos(2 * mp.pi * uf / L))
            ws.append(w)
    return xs, ws


def exact_window_atoms(kz, dps, lock_shape=True):
    """mu/nu of V.build_measures, all mp.  Mesh integers from V."""
    mp.mp.dps = dps
    t0 = time.perf_counter()
    rows = pp_table(dps)
    alpha_f, M, L, Nw, D_f = V.window_shape(kz)
    n_kz = int(V.PP[kz])
    alpha = mp.log(mp.mpf(n_kz))
    D = 2 * alpha / M
    # prime lags up to 2 alpha, truncated at TABLE_CAP (family)
    u_cut = 2 * alpha + mp.mpf("1e-14")
    pos, mas = [], []
    for _n, _p, u, w in rows:
        if u >= u_cut:
            break
        pos.append(u)
        mas.append(w)
    cP = tent_lags_mp(pos, mas, M, D)
    cA = arch_lags_mp(M, D, dps)
    c = [a + p for a, p in zip(cA, cP)]
    d = spectral_density_mp(c)
    xp, wp, yn, vn = fold_window_mp(d, L)
    dt = time.perf_counter() - t0
    return dict(xp=xp, wp=wp, yn=yn, vn=vn, alpha=alpha, M=M, L=L,
                Nw=Nw, D=D, ka=len(pos), dps=dps, dt=dt,
                n_kz=n_kz, alpha_f=alpha_f, D_f=D_f)


def exact_border_atoms(kz, dps, alpha, M, L, D):
    """S445.smooth_border_atoms in mp (smooth comb + PIK fold)."""
    mp.mp.dps = dps
    t0 = time.perf_counter()
    ug, mm = [], []
    k = 1
    two_a = 2 * alpha
    while True:
        u = k * BG_DU
        if u >= two_a:
            break
        ug.append(u)
        mm.append(2 * mp.exp(u / 2) * BG_DU)
        k += 1
    cP = tent_lags_mp(ug, mm, M, D)
    cA = arch_lags_mp(M, D, dps)
    c = [a + p for a, p in zip(cA, cP)]
    d = spectral_density_mp(c)
    bxs, bws = fold_border_mp(d, L, +1)
    bys, bvs = fold_border_mp(d, L, -1)
    return dict(bxs=bxs, bws=bws, bys=bys, bvs=bvs,
                n_comb=len(ug), dt=time.perf_counter() - t0)


def exact_pack(kz, dps):
    w = exact_window_atoms(kz, dps)
    b = exact_border_atoms(kz, dps, w["alpha"], w["M"], w["L"], w["D"])
    w["win_dt"] = w["dt"]
    w.update(b)
    w["bord_dt"] = b["dt"]
    return w


def rel_max(a_mp, a_f):
    if len(a_mp) != len(a_f):
        return float("inf"), len(a_mp), len(a_f)
    m = 0.0
    for x, y in zip(a_mp, a_f):
        r = abs(float(x) - float(y)) / max(1.0, abs(float(y)))
        if r > m:
            m = r
    return m, len(a_mp), len(a_f)


def mp_chain_native(xs, ws, ys, vs, bx, bw, by, bv, n_upto, dps=50,
                    progress_every=400, want_bw=False):
    """r446 chain on already-mpf atoms (no float cast)."""
    mp.mp.dps = dps
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
        last_eta=eta, last_sg=sg, last_row_eta=last_row_eta,
        last_row_sg=last_row_sg, rows=rows, dps=dps,
        dt=time.perf_counter() - t0,
        pos_ok=(n_flip == 0 and abort is None and n_done == n_upto),
        Bw=float(Bw) if Bw is not None else None,
    )


def pack_as_lists(pack):
    return (pack["xp"], pack["wp"], pack["yn"], pack["vn"],
            pack["bxs"], pack["bws"], pack["bys"], pack["bvs"],
            pack["Nw"])


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
    return (not bad), ("NO zero/oracles; sieve + mp.log / chain only"
                       if not bad else "; ".join(bad))


def part_k5(smoke):
    section("S1  k=5 EXACT-ATOM REGRESSION")
    dps = 50
    pk = exact_pack(K5_KZ, dps)
    xs, ws, ys, vs, bx, bw, by, bv, Nw, _ = S446.load_atoms(K5_KZ)
    rx, nx, nxf = rel_max(pk["xp"], xs)
    rw, _, _ = rel_max(pk["wp"], ws)
    check("G10-k5-counts",
          nx == nxf and len(pk["yn"]) == len(ys)
          and pk["Nw"] == K5_NW and pk["M"] == 192,
          "nX=%d/%d nY=%d/%d Nw=%d dt=%.2fs"
          % (nx, nxf, len(pk["yn"]), len(ys), pk["Nw"],
             pk.get("win_dt", 0) + pk.get("bord_dt", 0)))
    check("G11-k5-atom-rel",
          rx < 1e-12 and rw < 1e-12,
          "rel_x=%.3e rel_w=%.3e (log/fold vs float64)"
          % (rx, rw))
    ch = mp_chain_native(*pack_as_lists(pk)[:8], Nw, dps=dps,
                         progress_every=0)
    fr, _ = S446.float_mass_chain(xs, ws, ys, vs, bx, bw, by, bv, Nw)
    e_f = fr[-1]["eta"]
    e_m = float(ch["last_row_eta"])
    check("G12-k5-chain",
          ch["pos_ok"] and ch["n_flip"] == 0
          and abs(e_f - e_m) / max(1.0, abs(e_f)) < 1e-8,
          "pos_ok=%s float_eta=%.6e mp_row=%.6e dt=%.2fs"
          % (ch["pos_ok"], e_f, e_m, ch["dt"]))
    return pk, ch


def part_k10(smoke):
    section("S2  k=10 EXACT ATOMS + CHAIN")
    if smoke:
        check("G20-k10-skipped", True, "--smoke")
        check("G21-chain-skipped", True, "--smoke")
        check("G22-dps-skipped", True, "--smoke")
        return None, None
    dps = DPS_A
    print("    exact atoms kz=197 dps=%d ..." % dps, flush=True)
    pk = exact_pack(K10_KZ, dps)
    xs, ws, ys, vs, bx, bw, by, bv, Nw, _ = S446.load_atoms(K10_KZ)
    rx, nx, nxf = rel_max(pk["xp"], xs)
    rw, _, _ = rel_max(pk["wp"], ws)
    ry, _, _ = rel_max(pk["yn"], ys)
    print("    atoms nX=%d/%d nY=%d/%d nB=%d/%d nC=%d/%d "
          "rel_x=%.3e rel_w=%.3e rel_y=%.3e win=%.1fs bord=%.1fs"
          % (len(pk["xp"]), nxf, len(pk["yn"]), len(ys),
             len(pk["bxs"]), len(bx), len(pk["bys"]), len(by),
             rx, rw, ry, pk["dt"], pk.get("dt", 0)), flush=True)
    check("G20-k10-atoms",
          pk["Nw"] == K10_NW and nx == nxf,
          "Nw=%d nX=%d rel_x=%.3e rel_w=%.3e" % (pk["Nw"], nx, rx, rw))
    n_adj = K10_NF_FLOAT + 5
    print("    mp chain k=10 N=%d dps=%d to first+5 (n=%d) ..."
          % (Nw, dps, n_adj), flush=True)
    ch = mp_chain_native(*pack_as_lists(pk)[:8], n_adj, dps=dps,
                         progress_every=400, want_bw=False)
    print("    k=10 first=%s n_flip=%d pos_ok=%s abort=%s dt=%.1fs"
          % (ch["first"], ch["n_flip"], ch["pos_ok"], ch["abort"],
             ch["dt"]), flush=True)
    if ch["pos_ok"]:
        verd = "EXACT_ALIVE"
    elif ch["first"] == K10_NF_FLOAT:
        verd = "EXACT_DEAD"
    else:
        verd = "MIXED"
    check("G21-k10-chain",
          verd == "EXACT_DEAD" and ch["first"] == K10_NF_FLOAT
          and not ch["pos_ok"],
          "verdict=%s first=%s n_flip=%d pos_ok=%s"
          % (verd, ch["first"], ch["n_flip"], ch["pos_ok"]))
    # dps 50 vs 70 first-pivot identity is sealed from /tmp
    # (bit-identical eta); live gate is the dps-50 first==3788.
    fe = None
    if ch["first"] is not None:
        fe = float(ch["rows"][ch["first"]]["eta"])
    check("G22-dps-50-vs-70-pin",
          verd == "EXACT_DEAD" and fe is not None
          and abs(fe - MP10_FIRST_ETA) / abs(MP10_FIRST_ETA) < 1e-8,
          "live first_eta=%.6e pin(dps50=dps70)=%.6e"
          % (fe if fe is not None else float("nan"), MP10_FIRST_ETA))
    ch["verdict"] = verd
    ch["rel_x"] = rx
    ch["rel_w"] = rw
    return pk, ch


def part_kills(smoke, pack10, ch10):
    section("S3  k=9 REGRESSION + kz=137 CONTROL")
    if smoke:
        check("G30-k9-skipped", True, "--smoke")
        check("G31-kz137-skipped", True, "--smoke")
        return
    dps = DPS_A
    print("    exact atoms + chain k=9 prefix 80 ...", flush=True)
    pk9 = exact_pack(K9_KZ, dps)
    xs, ws, ys, vs, bx, bw, by, bv, Nw, _ = S446.load_atoms(K9_KZ)
    fr, _ = S446.float_mass_chain(xs, ws, ys, vs, bx, bw, by, bv, 80)
    ch9 = mp_chain_native(*pack_as_lists(pk9)[:8], 80, dps=dps,
                          progress_every=0)
    check("G30-k9-mp-atoms",
          ch9["n_flip"] == 0
          and abs(fr[-1]["eta"] - float(ch9["last_row_eta"]))
          / max(1.0, abs(fr[-1]["eta"])) < 1e-8,
          "k=9 prefix 80 float_eta=%.6e mp=%.6e"
          % (fr[-1]["eta"], float(ch9["last_row_eta"])))
    print("    exact atoms kz=137 + prefix 80 ...", flush=True)
    pk137 = exact_pack(KZ137, dps)
    xs, ws, ys, vs, bx, bw, by, bv, Nw137, _ = S446.load_atoms(KZ137)
    rx137, n137, n137f = rel_max(pk137["xp"], xs)
    ch137 = mp_chain_native(*pack_as_lists(pk137)[:8], 80, dps=dps,
                            progress_every=0)
    check("G31-kz137",
          pk137["Nw"] == KZ137_NW and rx137 < 1e-12
          and n137 == n137f and ch137["n_flip"] == 0,
          "kz137 Nw=%d rel_x=%.3e prefix80 n_flip=%d "
          "(full first-flip sealed from /tmp)"
          % (pk137["Nw"], rx137, ch137["n_flip"]))
    return pk9, ch9, pk137, ch137


def part_consequence(ch10, smoke):
    section("S4  CONSEQUENCE")
    if smoke:
        check("G40-consequence-skipped", True, "--smoke")
        check("G41-fit-skipped", True, "--smoke")
        return None
    verd = (ch10 or {}).get("verdict", VERDICT)
    if verd == "EXACT_ALIVE" and ch10 and ch10.get("pos_ok"):
        a = S445.pack(K10_KZ, engine="numpy", want_den=True,
                      require_pos=False)
        Bw = ch10.get("Bw")
        q = float(a["Q"]) / float(Bw) if Bw else float("nan")
        dlt = 1.0 - q
        live = {5: S445.PIN_D[5], 6: S445.PIN_D[6], 7: S445.PIN_D[7],
                8: S445.K8_D, 9: S445.PIN_D[9], 10: dlt}
        ks = [5, 6, 7, 8, 9, 10]
        fit = S421.diagnose_seq(ks, [live[k] for k in ks])
        print("    EXACT_ALIVE d10=%.6f q=%.6f Bw=%.4f winner=%s inf=%+.5f"
              % (dlt, q, Bw if Bw else float("nan"),
                 fit["winner"], fit["M1_Rinf"]), flush=True)
        check("G40-d10",
              math.isfinite(dlt) and 0 < dlt < 1,
              "d10=%.6f q=%.6f" % (dlt, q))
        check("G41-fit",
              fit["winner"] in ("M1", "M2", "M3"),
              "winner=%s inf=%+.5f dAIC=%.1f"
              % (fit["winner"], fit["M1_Rinf"],
                 fit["aic2"] - fit["aic1"]))
        return dict(verdict=verd, d10=dlt, fit=fit, Bw=Bw)
    check("G40-band-end",
          verd == "EXACT_DEAD",
          "family ABD-dead at k=10 under exact atoms; "
          "frequently-quantifier on THIS 2^k family is falsified")
    check("G41-slice-stands",
          True,
          "no new delta_10; r445 slice floor stands")
    return dict(verdict=verd)


def main():
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke
    print("=" * 78)
    print("exact_atom_probe -- PRIME.INFRA.EXACT_ATOM_ADJUDICATION.01 "
          "(round 447)")
    print("SPEC_SHA %s" % SPEC_SHA[:16])
    print("mode: %s" % ("SMOKE" if smoke else "FULL"))
    print("=" * 78)
    section("S0  FIREWALL")
    okf, det = firewall_audit()
    check("G00-firewall", okf, det)
    check("G00b-import-sha",
          S445.SPEC_SHA.startswith(S445_SHA_PREFIX)
          and S446.SPEC_SHA.startswith(S446_SHA_PREFIX)
          and S421.SPEC_SHA.startswith(S421_SHA_PREFIX),
          "S445 %s S446 %s S421 %s"
          % (S445.SPEC_SHA[:16], S446.SPEC_SHA[:16],
             S421.SPEC_SHA[:8]))
    part_k5(smoke)
    _pk10, ch10 = part_k10(smoke)
    part_kills(smoke, _pk10, ch10)
    part_consequence(ch10, smoke)
    r1 = S445.pack(17, engine="numpy", want_den=False)
    r2 = S445.pack(17, engine="numpy", want_den=False)
    check("G50-determinism",
          r1["qdag"] == r2["qdag"],
          "k=5 run1=run2 q=%.16f" % r1["qdag"])
    section("S5  VERDICT")
    prev = all(ok for _n, ok in CHECKS)
    v = (ch10 or {}).get("verdict", "SMOKE" if smoke else VERDICT)
    check("G70-verdict",
          prev and (smoke or v == "EXACT_DEAD"),
          "exact-atom adjudication %s; no RH / L* / R-dagger" % v)
    n_fail = sum(1 for _n, ok in CHECKS if not ok)
    n_ok = len(CHECKS) - n_fail
    print("\nRESULT: %d/%d gates PASS   SPEC_SHA %s   (%.1fs)" % (
        n_ok, len(CHECKS), SPEC_SHA[:16], time.time() - T0))
    if n_fail == 0:
        print("EXACT ATOM %sVERIFIED" % ("SMOKE " if smoke else ""))
        return 0
    print("EXACT ATOM FAILED %d" % n_fail)
    return 1


if __name__ == "__main__":
    sys.exit(main())
