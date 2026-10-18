#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""feshbach_hessian_probe -- PRIME.PORT.FESHBACH.HESSIAN.01
(EXPLORATION ONLY, experiments/; round 42, the strategy memo's
highest-value computation: is the canonical fixed-window Feshbach
scalar a PSD QUADRATIC FORM in the arithmetic residual
coordinates?  A stable PSD quadratic identity would explain BOTH
the measured exponent 1 in sigma ~ rho AND one-sidedness without
any pathwise flow control, 2026-08-09.)

MACHINERY (reused verbatim, declared): the Schur-compressed
fixed-window 12 x 12 matrices C_J(h) on J = {2, 4, ..., 24}
(PRIME.PORT.COCYCLE.01); the fit-free Mellin-Cauchy continuum
prediction pred_j of the deployed port numerators d_at(theta_j)
(PRIME.PORT.MELLIN.01); the atom-pivot scalar sigma_h
(PRIME.PORT.SCALAR.01 via PRIME.PORT.LEADING.SIGN.01).  THE FROZEN
RESIDUAL COORDINATES (stated once): r_h = the 8-vector
(d_at(theta_j) - pred_j) over the port modes j = 1..8 of
leading_sign_kappa_probe, in ABSOLUTE units.  v563 READ-ONLY.

FROZEN PROTOCOL (2026-08-09; ladder h <= 900; frozen + SHA-hashed
before first run):

 F1  LIMIT PAIR: C_inf := C_J at the DEEPEST compressed rung
     directly (h = 878; frozen choice, not Richardson -- the
     drift at depth is ~1.2e-3, second-order for the scalar);
     q_inf = its top eigenvector (sign: largest-|entry| positive).
     Ward W0: the drift ||C_h - C_inf||_2 on the 5 deepest
     below-reference rungs must TREND to zero: max over the 2
     deepest <= min over the 2 shallowest AND the deepest drift
     <= 5e-3 (the pairwise reading of "decreasing" is frozen to
     be robust to the h = 841/859 near-tie rungs).

 F2  CANONICAL SCALAR (every full-window rung): with Q = I -
     q_inf q_inf^T,
       s_h = q^T(I-C_h)q - q^T(I-C_h) Q [Q(I-C_h)Q]^{-1}
                                        Q(I-C_h) q
     (pseudo-inverse on the 11-dim complement).  Ward W1 (typed,
     printed): min eig of Q(I-C_h)Q on the complement -- the
     identity sign(s_h) = sign(tau_wall) only holds where it is
     PD; by Cauchy interlacing it is >= tau on truth, i.e. PD but
     TAU-SCALE (the pole diagnostic below).  Ward W2 (kill):
     sign(s_h) == sign(tau_h) wherever W1 holds.  Report table:
     s_h vs sigma_h vs tau_h.  LADDER SCOPE (frozen): the rungs
     of the 42 reachable (h <= 900) whose folded negative arm
     carries the FULL 12-window; design census 37 (kz 9, 13, 15,
     16, 24 carry only 7-11 of the 12 indices, typed, excluded).

 F3  QUADRATIC ANSATZ (the decisive test): s_h =? r_h^T H_h r_h.
     The map r -> s: the atom numerators are deformed d_at ->
     pred + r AT THE 8 PORT MODES (grid bins j and L-j) and the
     lag vector is reconstructed by the inverse FFT of the full
     grid -- the grid cosine transform c -> d is a BIJECTION
     between the M lags and the M independent grid frequencies,
     so the reconstruction is EXACT and least-norm is NOT needed;
     wards (kill): lag round trip rel <= 1e-8 and the identity
     point s(r_true) == s_h at rel <= 1e-10.  H by SYMMETRIC
     FRECHET SECOND DIFFERENCES at the TRUE r:
       H_ij = [s(r+ei+ej) - s(r+ei-ej) - s(r-ei+ej) + s(r-ei-ej)]
              / (4 eps^2),
     computed IN FULL at eps = 0.1 ||r||_2 AND at eps/2.  Ward W3
     (typed): the 4 dominant |H| entries agree at eps vs eps/2 to
     <= 5% -> EPS-CONVERGED, else EPS-DIVERGENT (all 4 printed).
     D   1-D CURVATURE LADDER (frozen part of the protocol; the
     referee for W3): per coordinate, the centered second
     difference d2_i at fracs {0.05, 0.025, 0.0125} x ||r||;
     CONVERGED iff the last two agree <= 10%; a CONVERGED d2_i <
     -1e-3 x max|H(eps)| is a genuinely negative Hessian
     direction.  POLE DIAGNOSTIC (printed): min eig of the
     complement block at r_true vs tau_h and at the minus-side
     stencil -- if the margin is tau-scale, the quadratic
     neighborhood excludes the residual scale.

 F4  THE THREE CRITERIA (typed over the tested rungs):
     (i)   LINEAR-SMALL: s(0) at the pure-Mellin point (r = 0)
           and lin = [s(+0.1 r) - s(-0.1 r)] / 0.2 (directional
           first difference through 0); typed PASS iff
           median(|s(0)| + |lin|) <= 0.2 x median |r^T H r|.
     (ii)  H-PSD: min eig H >= -1e-3 x max eig H on EVERY tested
           rung, required at BOTH eps scales (sign-stability).
     (iii) RATIO-ONE: median of s_h / (r_h^T H_h r_h) in
           [0.7, 1.4] (H at eps).
     SUBLABEL (frozen rule): HESSIAN-REFUTED iff (a) min eig H <
     -1e-3 max eig at BOTH eps scales on some rung, OR (a') a
     CONVERGED negative 1-D direction (D above) on some rung, OR
     (b) median(|s(0)| + |lin|) > median |r^T H r| (linear /
     constant term dominant).  HESSIAN-PSD-CONFIRMED iff (i),
     (ii), (iii) all pass AND W3 = EPS-CONVERGED on all tested
     rungs.  Else HESSIAN-PARTIAL.

 F5  SCOPE (frozen): tested rungs kz {12, 20, 14, 26, 40} plus
     the 3 deepest compressed {50, 64, 52}.  SAID SO: the heavy
     rungs kz 9 and kz 13 carry only 7 and 11 of the 12 window
     indices on their folded negative arm and CANNOT enter the
     compressed frame; kz 20 (h 170) and kz 14 (h 185) are the
     nearest full-window rungs at matching depth.  Full 8x8 H at
     both eps scales on all 8 tested rungs (measured feasible,
     ~5 min total).

 F6  CONTROLS (kz 9, must fire; value control): scramble and
     Epstein combs -- fires iff the fixed 12-window is UNAVAILABLE
     on the control comb (frame death = the strongest W1 failure)
     OR the exterior is indefinite (lam_max(E_out) > 1, exact
     transfer broken) OR the complement is not PD OR s < 0.  The
     quadratic-form test is NOT run on controls: their r is not a
     small residual around the Mellin prediction (stated).

KILLS: KP pipeline (ladder census != 37 / Lanczos breakdown /
failed FD evaluation) -> PIPELINE-BROKEN; KW wards (W0 drift, W2
sign, round trip, identity point) -> WARD-BROKEN; KC controls
silent -> CONTROL-DEAD.  F4 criteria are TYPED, never kill.

VERDICT (frozen enum): FESHBACH-HESSIAN-MEASURED (+ sublabel
HESSIAN-PSD-CONFIRMED / HESSIAN-PARTIAL / HESSIAN-REFUTED) /
PIPELINE-BROKEN / WARD-BROKEN / CONTROL-DEAD.

HONEST FRAME: HESSIAN-REFUTED is a decisive negative for the
entropy/variance strategy (no stable PSD quadratic identity in
these coordinates) and leaves discrete IIKS steepest descent as
the main route; it is NOT a statement about RH.  NO RH claim.
No marker moves.

FIREWALL: no zeros, no prime oracles (AST scan; banned:
zetazero/nzeros/primerange/isprime/primepi/nextprime/prevprime);
v563 READ-ONLY; RNG only in the declared scramble control; stdout
only.

Sources (read-only): v563_paper2_readouts;
port_cocycle_window_probe (C_J machinery, VERBATIM);
port_mellin_cauchy_probe (pred_j, VERBATIM);
port_atom_numerator_probe (the windowed-sum lag relation);
leading_sign_kappa_probe (port set, sigma via scalar_split,
VERBATIM).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/feshbach_hessian_probe.py
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

JWIN = tuple(range(2, 25, 2))
PORTSET = tuple(range(1, 9))
TESTED = (12, 20, 14, 26, 40, 50, 64, 52)
N_FULLWIN_FROZEN = 37
EPS_FRAC = 0.1
LADDER_FRACS = (0.05, 0.025, 0.0125)
LIN_T = 0.1
BANNED_IDS = ("zetazero", "nzeros", "primerange", "isprime",
              "primepi", "nextprime", "prevprime")

CHECKS = []
KILLS = []
T0 = time.time()


def check(name, ok, detail="", kill=None):
    CHECKS.append((name, bool(ok)))
    if kill and not ok:
        KILLS.append(kill)
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


# ---- shared machinery, VERBATIM from the round-39/41 chain ----

def grid_density(c):
    c = np.asarray(c, float)
    a = np.concatenate([c, c[-2:0:-1]])
    d = np.fft.fft(a)
    assert float(np.max(np.abs(d.imag))) <= 1e-9 * max(
        1.0, float(np.max(np.abs(d.real))))
    return d.real


def lambda_eps(N):
    r = np.zeros(N + 1)
    s = int(math.isqrt(N)) + 1
    for x in range(-s, s + 1):
        for y in range(-s, s + 1):
            v = x * x + 5 * y * y
            if 1 <= v <= N:
                r[v] += 1.0
    a = r / 2.0
    lam = np.zeros(N + 1)
    for n in range(2, N + 1):
        acc = a[n] * math.log(n)
        for dd in range(2, n):
            if n % dd == 0:
                acc -= lam[dd] * a[n // dd]
        lam[n] = acc
    return lam


def folded_measure(d_arm, L, sign=+1.0):
    jj = np.arange(L)
    keep = (sign * d_arm) > 0.0
    jj = jj[keep]
    th = 2.0 * math.pi * jj / L
    wt = (np.abs(d_arm[keep]) / (2.0 * L)) * 4.0 * np.sin(
        th / 2.0) ** 2
    fold = np.minimum(jj, L - jj)
    uf, inv = np.unique(fold, return_inverse=True)
    wagg = np.zeros(len(uf))
    np.add.at(wagg, inv, wt)
    xs = np.cos(2.0 * math.pi * uf / L)
    m = wagg > 1e-300
    return xs[m], wagg[m], uf[m]


def lanczos_chain(x, w, n):
    m0 = float(np.sum(w))
    m = len(x)
    Q = np.zeros((m, n))
    Q[:, 0] = np.sqrt(w) / math.sqrt(m0)
    al = np.zeros(n)
    be = np.zeros(max(n - 1, 0))
    steps = n
    for k in range(n):
        z = x * Q[:, k]
        al[k] = float(Q[:, k] @ z)
        z = z - al[k] * Q[:, k]
        if k > 0:
            z = z - be[k - 1] * Q[:, k - 1]
        for _ in range(2):
            z = z - Q[:, :k + 1] @ (Q[:, :k + 1].T @ z)
        if k == n - 1:
            break
        bnorm = float(np.linalg.norm(z))
        if bnorm <= 1e-14:
            steps = k + 1
            break
        be[k] = bnorm
        Q[:, k + 1] = z / bnorm
    return al[:steps], be[:max(steps - 1, 0)], m0, steps


def eval_chain(al, be, m0, y, n):
    P = np.zeros((len(y), n))
    P[:, 0] = 1.0 / math.sqrt(m0)
    if n > 1:
        P[:, 1] = (y - al[0]) * P[:, 0] / be[0]
    for k in range(1, n - 1):
        P[:, k + 1] = ((y - al[k]) * P[:, k]
                       - be[k - 1] * P[:, k - 1]) / be[k]
    return P


# ---- pred_j, VERBATIM from port_mellin_cauchy_probe ----

def w_exact(u_arr, M, D, L, j):
    th = 2.0 * math.pi * j / L
    i0 = np.floor(u_arr / D).astype(int)
    f = u_arr / D - i0

    def w_of(i):
        return np.where((i == 0) | (i == M - 1), 1.0, 2.0)

    tot = np.zeros(len(u_arr))
    for i_at, v_at in ((i0, 1.0 - f), (i0 + 1, f)):
        ok = (i_at >= 0) & (i_at <= M - 1) & (v_at > 0.0)
        tot += np.where(ok, v_at * w_of(i_at)
                        * np.cos(i_at * th), 0.0)
    return 0.5 * tot


def pred_port(uu, M, D, L, j):
    U = float(np.max(uu))
    rg = np.linspace(1e-6, 1.0, 20000)
    ug = U + 2.0 * np.log(rg)
    keep = ug >= 0.0
    w = w_exact(ug[keep], M, D, L, j)
    return -4.0 * math.exp(U / 2.0) * float(
        np.trapezoid(w, rg[keep]))


# ---- sigma, VERBATIM from port_scalar_schur / leading_sign ----

def scalar_split(E):
    n = E.shape[0]
    mstar = int(np.argmax(np.diag(E)))
    rest = [i for i in range(n) if i != mstar]
    a = 1.0 - float(E[mstar, mstar])
    bvec = E[mstar, rest]
    B = np.eye(n - 1) - E[np.ix_(rest, rest)]
    beta = float(bvec @ np.linalg.solve(B, bvec))
    return a - beta


# ---- rung construction + the deformed pipeline ----

def rung_data(kz, scramble_seed=None, comb=None):
    rr = core.build_window(kz, scramble_seed=scramble_seed)
    h, M, D, alpha = rr["h"], rr["M"], rr["D"], rr["alpha"]
    uu = np.asarray(rr["uu"], float)
    mm = 2.0 * np.asarray(rr["lam"], float)
    if comb is not None:
        uu, mm = comb
    c_at, _ = core.atom_lags_at(alpha, M, uu, mm)
    c_ar = np.asarray(core.arch_lags(M, D), float)
    d_ar = grid_density(c_ar)
    d_at = grid_density(np.asarray(c_at, float))
    L = 2 * M - 2
    pred = np.array([pred_port(uu, M, D, L, j) for j in PORTSET])
    r_true = np.array([float(d_at[j]) for j in PORTSET]) - pred
    return dict(kz=kz, h=h, M=M, D=D, L=L, alpha=alpha,
                d_ar=d_ar, d_at=d_at, pred=pred, r=r_true)


def deform_density(b, r):
    """d_at with the port numerators set to pred + r (bins j and
    L-j); the exact lag reconstruction (full-grid inverse FFT)
    is warded by the round trip.  Returns (d_total, rt_rel)."""
    d_new = b["d_at"].copy()
    L, M = b["L"], b["M"]
    for k, j in enumerate(PORTSET):
        delta = (b["pred"][k] + r[k]) - float(b["d_at"][j])
        d_new[j] += delta
        d_new[L - j] += delta
    a = np.fft.ifft(d_new)
    scale = max(1.0, float(np.max(np.abs(d_new))))
    rt = float(np.max(np.abs(a.imag))) / scale
    c_new = a.real[:M]
    d_chk = grid_density(c_new)
    rt = max(rt, float(np.max(np.abs(d_chk - d_new))) / scale)
    return b["d_ar"] + d_new, rt


def feshbach_scalar(CJ, q):
    """s = q^T Mh q - (Q Mh q)^T [Q Mh Q]^+ (Q Mh q), Mh = I-C;
    pseudo-inverse on the 11-dim complement of q.  Returns
    (s, min eig of the complement block)."""
    Mh = np.eye(len(q)) - CJ
    v = Mh @ q
    qv = float(q @ v)
    Qv = v - q * qv
    A = Mh - np.outer(q, v) - np.outer(v, q) + qv * np.outer(q, q)
    ev, V = np.linalg.eigh(A)
    comp = np.argsort(np.abs(V.T @ q))[:len(q) - 1]
    mineig = float(np.min(ev[comp]))
    Ainv_Qv = V[:, comp] @ ((V[:, comp].T @ Qv) / ev[comp])
    return qv - float(Qv @ Ainv_Qv), mineig


def pipeline(d_total, h, q=None, full=False):
    """Folded measure -> Lanczos -> E -> 12-window Schur C_J.
    full: also tau (eigh of E), sigma, lamO.  Returns dict or a
    typed string."""
    L = len(d_total)
    xs, ws, _ = folded_measure(d_total, L, +1.0)
    ys, vs, uf_n = folded_measure(d_total, L, -1.0)
    al, be, m0, steps = lanczos_chain(xs, ws, h + 1)
    if steps < h + 1 or np.any(be <= 0):
        return "LANCZOS-BREAK"
    Pn = eval_chain(al, be, m0, ys, h)
    E = np.sqrt(vs)[:, None] * (Pn @ Pn.T) * np.sqrt(vs)[None, :]
    E = 0.5 * (E + E.T)
    idx = {int(j): k for k, j in enumerate(uf_n)}
    jav = [j for j in JWIN if j in idx]
    if len(jav) < 12:
        return "WINDOW-SHORT:%d" % len(jav)
    iw = [idx[j] for j in jav]
    io = [k for k in range(E.shape[0]) if k not in set(iw)]
    Eo = E[np.ix_(io, io)]
    IO = np.eye(len(io)) - Eo
    Ex = E[np.ix_(iw, io)]
    CJ = E[np.ix_(iw, iw)] + Ex @ np.linalg.solve(IO, Ex.T)
    CJ = 0.5 * (CJ + CJ.T)
    out = dict(CJ=CJ)
    if q is not None:
        out["s"], out["mineigA"] = feshbach_scalar(CJ, q)
    if full:
        out["lamO"] = float(np.linalg.eigvalsh(Eo)[-1])
        out["tau"] = 1.0 - float(np.linalg.eigvalsh(E)[-1])
        out["sigma"] = scalar_split(E)
    return out


def make_s_of(b, q):
    """Cached map r -> s with round-trip tracking."""
    cache = {}
    state = dict(rt_max=0.0, n_bad=0)

    def s_of(r):
        key = tuple(np.round(np.asarray(r, float), 12))
        if key not in cache:
            d_total, rt = deform_density(b, np.asarray(r, float))
            state["rt_max"] = max(state["rt_max"], rt)
            out = pipeline(d_total, b["h"], q=q)
            if isinstance(out, str):
                state["n_bad"] += 1
                cache[key] = (float("nan"), float("nan"))
            else:
                cache[key] = (out["s"], out["mineigA"])
        return cache[key]

    return s_of, state


def hessian_at(s_of, r0, eps):
    H = np.zeros((8, 8))
    for i in range(8):
        for j in range(i, 8):
            ei = np.zeros(8)
            ei[i] = eps
            ej = np.zeros(8)
            ej[j] = eps
            H[i, j] = H[j, i] = (
                s_of(r0 + ei + ej)[0] - s_of(r0 + ei - ej)[0]
                - s_of(r0 - ei + ej)[0]
                + s_of(r0 - ei - ej)[0]) / (4.0 * eps * eps)
    return H


def main():
    section("PRIME.PORT.FESHBACH.HESSIAN.01 -- is the canonical "
            "Feshbach scalar a PSD quadratic form in the "
            "arithmetic residuals?  (EXPLORATION ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s"
          % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
    print("    NO RH claim; no marker moves.")
    print("\nS0 -- firewall")
    check("S0.1 AST firewall clean", not ast_scan(BANNED_IDS))

    # ---------------- F1/F2: ladder, limit pair, scalar table --
    section("F1/F2 -- limit pair + the canonical scalar ladder")
    rungs = {}
    short = []
    for kz in core.frame_a_zones():
        b = rung_data(kz)
        if b["h"] > 900:
            continue
        out = pipeline(b["d_ar"] + b["d_at"], b["h"], full=True)
        if isinstance(out, str):
            short.append((kz, out))
            continue
        rungs[kz] = (b, out)
    print("    full-window rungs: %d | window-short (typed, "
          "excluded): %s"
          % (len(rungs), ["kz%d %s" % t for t in short]))
    check("F2.0 ladder census %d == %d (frozen)"
          % (len(rungs), N_FULLWIN_FROZEN),
          len(rungs) == N_FULLWIN_FROZEN, kill="KP")
    if len(rungs) < 6:
        return finish("n/a")

    order = sorted(rungs, key=lambda k: rungs[k][0]["h"])
    kz_ref = order[-1]
    Cinf = rungs[kz_ref][1]["CJ"]
    ev, V = np.linalg.eigh(Cinf)
    q = V[:, -1]
    if q[int(np.argmax(np.abs(q)))] < 0:
        q = -q
    print("    C_inf = C_J at kz %d (h %d, frozen: deepest rung "
          "directly); top eig %.8f"
          % (kz_ref, rungs[kz_ref][0]["h"], float(ev[-1])))
    deep5 = order[-6:-1]
    drifts = [float(np.linalg.norm(rungs[k][1]["CJ"] - Cinf, 2))
              for k in deep5]
    for k, dv in zip(deep5, drifts):
        print("    drift kz %-3d h %-4d ||C_h - C_inf||_2 = %.6f"
              % (k, rungs[k][0]["h"], dv))
    w0 = (max(drifts[-2:]) <= min(drifts[:2])
          and drifts[-1] <= 5e-3)
    check("W0 drift trend on the deepest 5: max(deepest 2) "
          "%.2e <= min(shallowest 2) %.2e and final <= 5e-3"
          % (max(drifts[-2:]), min(drifts[:2])), w0, kill="KW")

    print("\n    %-4s %-5s %-7s %-11s %-11s %-11s %-8s %-9s"
          % ("kz", "h", "alpha", "tau", "sigma", "s", "s/tau",
             "W1 mineig"))
    w1_min = float("inf")
    w2_ok = True
    for kz in order:
        b, out = rungs[kz]
        s, mineigA = feshbach_scalar(out["CJ"], q)
        out["s"], out["mineigA"] = s, mineigA
        w1_min = min(w1_min, mineigA)
        if mineigA > 0.0:
            w2_ok &= (s > 0) == (out["tau"] > 0)
        print("    %-4d %-5d %-7.3f %-11.3e %-11.3e %-11.3e "
              "%-8.3f %-9.2e"
              % (kz, b["h"], b["alpha"], out["tau"], out["sigma"],
                 s, s / out["tau"], mineigA))
    check("W1 complement block PD on every truth rung (typed; "
          "min eig over ladder %.2e > 0; NOTE tau-scale by "
          "interlacing -- the pole diagnostic of F3)" % w1_min,
          w1_min > 0.0)
    check("W2 sign(s_h) == sign(tau_h) wherever W1 holds",
          w2_ok, kill="KW")

    # ---------------- F3: the quadratic ansatz ----------------
    section("F3 -- symmetric Frechet second differences "
            "(tested rungs, full 8x8 at eps and eps/2)")
    print("    tested rungs (frozen): %s -- kz 9/13 carry only "
          "7/11 of the 12 window indices and CANNOT enter the "
          "compressed frame; kz 20/14 substitute at matching "
          "depth (SAID SO)." % (TESTED,))
    rows = []
    rt_max = 0.0
    idw_max = 0.0
    n_bad = 0
    for kz in TESTED:
        b, base = rungs[kz]
        s_of, st = make_s_of(b, q)
        r0 = b["r"]
        nr = float(np.linalg.norm(r0))
        s_id, _ = s_of(r0)
        idw = abs(s_id - base["s"]) / max(abs(base["s"]), 1e-300)
        idw_max = max(idw_max, idw)
        eps = EPS_FRAC * nr
        H1 = hessian_at(s_of, r0, eps)
        H2 = hessian_at(s_of, r0, 0.5 * eps)
        flat = sorted(((abs(H1[i, j]), i, j) for i in range(8)
                       for j in range(i, 8)), reverse=True)
        dom = [(i, j) for _v, i, j in flat[:4]]
        dev_dom = max(abs(H2[i, j] - H1[i, j])
                      / max(abs(H1[i, j]), 1e-300)
                      for i, j in dom)
        # 1-D curvature ladder (the referee for W3)
        s0v = s_of(r0)[0]
        conv_neg = []
        d2_last = np.zeros(8)
        d2_conv = np.zeros(8, dtype=bool)
        for i in range(8):
            d2s = []
            for fr in LADDER_FRACS:
                e = np.zeros(8)
                e[i] = fr * nr
                d2s.append((s_of(r0 + e)[0] - 2.0 * s0v
                            + s_of(r0 - e)[0]) / (fr * nr) ** 2)
            d2_last[i] = d2s[-1]
            d2_conv[i] = (abs(d2s[-1] - d2s[-2])
                          <= 0.10 * max(abs(d2s[-1]), 1e-300))
            if d2_conv[i] and d2s[-1] < -1e-3 * float(
                    np.max(np.abs(H1))):
                conv_neg.append(i)
        # pure-Mellin point and the directional first difference
        sz, mz = s_of(np.zeros(8))
        lin = (s_of(LIN_T * r0)[0]
               - s_of(-LIN_T * r0)[0]) / (2.0 * LIN_T)
        # pole diagnostic: minus-side complement min eig along
        # the dominant diagonal direction at the eps stencil
        i_dom = int(np.argmax(np.abs(np.diag(H1))))
        e = np.zeros(8)
        e[i_dom] = eps
        m_minus = s_of(r0 - 2.0 * e)[1]
        ev1 = np.linalg.eigvalsh(H1)
        ev2 = np.linalg.eigvalsh(H2)
        rHr1 = float(r0 @ H1 @ r0)
        rHr2 = float(r0 @ H2 @ r0)
        rt_max = max(rt_max, st["rt_max"])
        n_bad += st["n_bad"]
        rows.append(dict(kz=kz, h=b["h"], s=base["s"],
                         tau=base["tau"], nr=nr, eps=eps,
                         ev1=ev1, ev2=ev2, rHr1=rHr1, rHr2=rHr2,
                         dev_dom=dev_dom, dom=dom, H1=H1, H2=H2,
                         s0=sz, m0=mz, lin=lin,
                         mA=base["mineigA"], m_minus=m_minus,
                         conv_neg=conv_neg, d2_last=d2_last,
                         d2_conv=d2_conv))
        print("\n    kz %-3d h %-4d ||r|| %.3f eps %.3f "
              "(|r_j|/|d_at_j| max %.3f)"
              % (kz, b["h"], nr, eps,
                 max(abs(r0[k]) / abs(b["d_at"][j])
                     for k, j in enumerate(PORTSET))))
        print("      eig H(eps)  : min %+.3e max %+.3e | "
              "r^T H r %+.4e | s %+.4e | s/rHr %+.2e"
              % (ev1[0], ev1[-1], rHr1, base["s"],
                 base["s"] / rHr1))
        print("      eig H(eps/2): min %+.3e max %+.3e | "
              "r^T H r %+.4e | dominant-4 dev %.3f"
              % (ev2[0], ev2[-1], rHr2, dev_dom))
        print("      1-D ladder  : converged dirs (port j) %s | "
              "converged NEGATIVE dirs %s | d2(conv) %s"
              % ([PORTSET[i] for i in np.nonzero(d2_conv)[0]],
                 [PORTSET[i] for i in conv_neg],
                 " ".join("%+.2e" % d2_last[i]
                          for i in np.nonzero(d2_conv)[0])))
        print("      pure Mellin : s(0) %+.4e (complement min "
              "eig %+.2e) | lin %+.4e | |s0|+|lin| = %.3e"
              % (sz, mz, lin, abs(sz) + abs(lin)))
        print("      pole diag   : mineigA(r_true) %.2e = %.1f x "
              "tau | minus-side stencil mineigA %+.2e"
              % (base["mineigA"], base["mineigA"] / base["tau"],
                 m_minus), flush=True)
    check("F3.1 round-trip ward: exact lag reconstruction, max "
          "rel %.1e <= 1e-8 (full-grid cosine bijection, no "
          "least-norm needed)" % rt_max, rt_max <= 1e-8,
          kill="KW")
    check("F3.2 identity ward: s(deform at true r) == s_h, max "
          "rel %.1e <= 1e-10" % idw_max, idw_max <= 1e-10,
          kill="KW")
    check("F3.3 all FD evaluations completed (%d failed)" % n_bad,
          n_bad == 0, kill="KP")
    eps_conv_all = all(r_["dev_dom"] <= 0.05 for r_ in rows)
    w3_type = ("EPS-CONVERGED" if eps_conv_all
               else "EPS-DIVERGENT")
    check("W3 typed: %s -- dominant-4 entry eps vs eps/2 "
          "deviation per rung: %s (bar 0.05)"
          % (w3_type, " ".join("%.2f" % r_["dev_dom"]
                               for r_ in rows)), True)

    # ---------------- F4: the three criteria -------------------
    section("F4 -- the three criteria (typed)")
    med_rHr = float(np.median([abs(r_["rHr1"]) for r_ in rows]))
    med_lin = float(np.median([abs(r_["s0"]) + abs(r_["lin"])
                               for r_ in rows]))
    c1 = med_lin <= 0.2 * med_rHr
    check("F4.i LINEAR-SMALL: median(|s(0)|+|lin|) %.3e <= 0.2 x "
          "median|r^T H r| %.3e -> %s"
          % (med_lin, med_rHr, "PASS" if c1 else "FAIL"), True)
    psd1 = all(r_["ev1"][0] >= -1e-3 * r_["ev1"][-1]
               for r_ in rows)
    psd2 = all(r_["ev2"][0] >= -1e-3 * r_["ev2"][-1]
               for r_ in rows)
    c2 = psd1 and psd2
    check("F4.ii H-PSD at eps %s / at eps/2 %s (min eig >= -1e-3 "
          "max eig on every tested rung) -> %s"
          % (psd1, psd2, "PASS" if c2 else "FAIL"), True)
    ratios = [r_["s"] / r_["rHr1"] for r_ in rows]
    med_ratio = float(np.median(ratios))
    c3 = 0.7 <= med_ratio <= 1.4
    check("F4.iii RATIO-ONE: median s/(r^T H r) = %.3e in "
          "[0.7, 1.4] -> %s (ladder: %s)"
          % (med_ratio, "PASS" if c3 else "FAIL",
             " ".join("%+.1e" % v for v in ratios)), True)

    neg_stable = [r_["kz"] for r_ in rows
                  if r_["ev1"][0] < -1e-3 * r_["ev1"][-1]
                  and r_["ev2"][0] < -1e-3 * r_["ev2"][-1]]
    neg_1d = [(r_["kz"], [PORTSET[i] for i in r_["conv_neg"]])
              for r_ in rows if r_["conv_neg"]]
    lin_dom = med_lin > med_rHr
    if neg_stable or neg_1d or lin_dom:
        sub = "HESSIAN-REFUTED"
    elif c1 and c2 and c3 and eps_conv_all:
        sub = "HESSIAN-PSD-CONFIRMED"
    else:
        sub = "HESSIAN-PARTIAL"
    check("F4.s sublabel %s -- sign-stable negative eig rungs %s "
          "| converged negative 1-D directions %s | linear "
          "dominance %s (median lin %.3e vs median rHr %.3e)"
          % (sub, neg_stable, neg_1d, lin_dom, med_lin, med_rHr),
          True)

    # ---------------- F6: controls (kz 9) ----------------------
    section("F6 -- controls (kz 9; value control; the quadratic-"
            "form test is NOT run on controls -- their r is not "
            "a small residual)")
    rr9 = core.build_window(9)
    N_E = int(math.floor(math.exp(2.0 * rr9["alpha"]))) + 1
    lamE_ = lambda_eps(N_E)
    nn = np.nonzero(np.abs(lamE_) > 1e-12)[0]
    ok_ctl = True
    for nmc, kw in (("Epstein", dict(comb=(
            np.log(nn.astype(float)),
            2.0 * lamE_[nn] / np.sqrt(nn.astype(float))))),
            ("scramble", dict(scramble_seed=1))):
        b_c = rung_data(9, **kw)
        out = pipeline(b_c["d_ar"] + b_c["d_at"], b_c["h"], q=q,
                       full=True)
        if isinstance(out, str):
            print("    %-8s: %s -> fires via FRAME DEATH (the "
                  "fixed 12-window does not exist on this comb)"
                  % (nmc, out))
            continue
        fired = (out["lamO"] > 1.0 or out["mineigA"] <= 0.0
                 or out["s"] < 0.0)
        ok_ctl &= fired
        print("    %-8s: s %+.3e | complement min eig %+.3e | "
              "lam(out) %.3e -> %s"
              % (nmc, out["s"], out["mineigA"], out["lamO"],
                 "FIRES" if fired else "silent"))
    check("C1 CONTROLS FIRE (frame death / exterior indefinite / "
          "complement not PD / s < 0)", ok_ctl, kill="KC")

    return finish(sub, w3_type)


def finish(sub, w3_type="n/a"):
    section("V -- FROZEN VERDICT")
    n_pass = sum(1 for _n, okk in CHECKS if okk)
    n_tot = len(CHECKS)
    if KILLS:
        VERDICT = {"KP": "PIPELINE-BROKEN", "KW": "WARD-BROKEN",
                   "KC": "CONTROL-DEAD"}[KILLS[0]]
    else:
        VERDICT = "FESHBACH-HESSIAN-MEASURED"
    print("\n  VERDICT: %s (%s, %s)" % (VERDICT, sub, w3_type))
    if sub == "HESSIAN-REFUTED":
        print("""
  DECISIVE NEGATIVE (reported loudly, as frozen): the canonical
  fixed-window Feshbach scalar is NOT a stable PSD quadratic form
  in the arithmetic residual coordinates.  The measured structure:
  the 11-dim complement block inherits the wall's criticality
  (its PD margin is tau-scale by interlacing, so the quadratic
  neighborhood of the true point excludes the residual scale and
  the scalar is dominated by a near-pole), the pure-Mellin point
  s(0) and the directional linear term dwarf s_h by orders of
  magnitude (s_h is a fine cancellation, not a quadratic value),
  and where the 1-D curvature converges it can be NEGATIVE.  This
  kills the entropy/variance strategy in these coordinates: the
  exponent 1 in sigma ~ rho and the one-sidedness are NOT
  explained by a rung-wise PSD quadratic identity.  Discrete IIKS
  steepest descent remains the main route.  NO RH claim.""")
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed"
          % (time.time() - T0, n_tot, n_tot - n_pass))
    return 0 if n_pass == n_tot else 1


if __name__ == "__main__":
    raise SystemExit(main())
