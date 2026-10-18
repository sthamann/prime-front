#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""port_sflow_toda_probe -- PRIME.PORT.SFLOW.01
(EXPLORATION ONLY, experiments/; round 44, the continuation of
PRIME.PORT.HIROTA.01: derive and verify the EXACT s-direction
flow equations of the port tau minors from the IIKS/resolvent
structure and measure the positive-cone invariance from s = 0
(trivial, tau = 1) to s = 1 (the wall), 2026-08-09.)

THE EXACT MATH (frozen).  For the s-family M(s) = I - s C on
the fixed 12-window (C = C_J(h), the Schur-compressed window of
PRIME.PORT.COCYCLE.01) with nested leading principal minors
tau^{(k)}(s) := det(M(s)[:k, :k]) = det(I_k - s C_k):

 (i)  JACOBI, PER SECTION, EXACT:
          d/ds tau^{(k)}(s)
              = -tau^{(k)}(s) * tr[(M_k(s))^{-1} C_k],
      equivalently d/ds log tau^{(k)} = -tr[M_k^{-1} C_k]
      =: L_k(s), and d^2/ds^2 log tau^{(k)}
      = -tr[(M_k^{-1} C_k)^2] =: L'_k(s).  In the spectral
      form (lambda_i the eigenvalues of the SYMMETRIC C_k):
      log tau^{(k)} = sum_i log(1 - s lambda_i),
      L_k = -sum_i lambda_i / (1 - s lambda_i),
      L'_k = -sum_i lambda_i^2 / (1 - s lambda_i)^2.

 (ii) THE CLASSICAL TODA CONNECTION: the ratios
          r_k(s) := tau^{(k+1)} tau^{(k-1)} / (tau^{(k)})^2
      (tau^{(0)} := 1) are the standard tau-function variables;
      IF the section family follows a Toda-lattice flow in a
      time t(s), then the Toda bilinear identity holds:
          d^2/dt^2 log tau^{(k)} = a_k * r_k(s) + b_k
      with CONSTANT a_k, b_k along the flow.  Time candidates
      (frozen): t = s; t = log(1/(1-s)); t = log s, with the
      exact chain rule d^2/dt^2 f = (ds/dt)^2 f'' +
      (d^2 s/dt^2) f', i.e.
          t = s:            D2 = f''
          t = log(1/(1-s)): D2 = (1-s)^2 f'' - (1-s) f'
          t = log s:        D2 = s^2 f'' + s f''*0 + s f'
                               = s^2 f'' + s f'   (s > 0 only).

 (iii) THE POLE IDENTITY (elementary but organizing): by Cauchy
      interlacing lam_max(C_k) <= lam_max(C_12) = lam_max(C),
      so the FIRST zero of ANY section minor on s > 0 is the
      zero of tau^{(12)}:  s*_h = 1 / lam_max(C_h) EXACTLY
      (when lam_max > 0).  Hence s*_h - 1 = tau_h/(1 - tau_h)
      with the wall margin tau_h := 1 - lam_max(C_h): the wall
      margin IS the pole distance of the s-flow.  RH on the
      ladder = the pole of the s-flow stays outside [0, 1]
      uniformly.  NO RH claim follows from any finite window.

MACHINERY (reused VERBATIM, declared): the Schur-compressed
fixed-window 12 x 12 matrices C_J(h) on J = {2, 4, ..., 24}
(PRIME.PORT.COCYCLE.01 / feshbach_hessian_probe pipeline); the
Jacobi variational identity was established scalar-globally in
port_tau_determinant_probe (PRIME.PORT.TAU.01) -- here it is
verified PER SECTION.  Known input (port_tau_hirota_probe):
MINORS-POSITIVE at s = 1 on all 37 full-window rungs; DJ exact
in the s-family; the bilinear cancellation ratio in s improves
with depth (0.010 -> 0.000) -- the Toda compatibility lives in
the s-direction.  v563 READ-ONLY.

FROZEN PROTOCOL (2026-08-09; ladder h <= 900; the 37 full-
window rungs exactly as in feshbach_hessian_probe F2.0; frozen
+ SHA-hashed before first run):

 S1  EXACT VARIATIONAL WARD (kill KW): on the frozen heavy
     rungs kz {12, 20, 26, 40, 52} PLUS the 3 deepest full-
     window rungs by h (dedup), per section k = 1..12 and per
     s in {0.3, 0.6, 0.9}: the analytic derivative
     L_k = -tr[M_k^{-1} C_k] (trace route) against a 4th-order
     central finite difference of log tau^{(k)} (slogdet route,
     step 1e-3): rel = |L - FD| / max(|L|, 1e-30) <= 1e-8.
     Ward W2 (kill KW): the spectral route for L_k agrees with
     the trace route, rel <= 1e-9 (guards the S2 machinery).
     This is algebra; the ward guards the bookkeeping.

 S2  THE TODA TEST (the substance): on the frozen fine s-grid
     s_j = 0.999 * (1 - (1 - u_j)^2), u_j = j/199, j = 0..199
     (200 points, denser near 1), compute log tau^{(k)}(s) for
     k = 1..12 on the S1 rung set; per rung, per time candidate
     and per k = 1..11 (k = 12 has no right neighbor) fit
     D2_t log tau^{(k)} = a_k r_k + b_k by least squares over
     the grid (t = log s: s > 0 points only).  Residual per
     point: |y - a x - b| / (|y| + |a x| + |b| + 1e-300).
     Candidate score = median residual over (rungs, k, points);
     best candidate t* = argmin.  CROSS-RUNG STABILITY
     (frozen): per k the spread of a_k across rungs,
     (max - min) / max(|median|, 1e-30); STABLE iff the median
     over k <= 0.5.  TYPE: TODA-CLOSED(t*) iff best median
     residual <= 0.05 AND STABLE; TODA-VARYING(t*) iff best
     median residual <= 0.05 but coefficients drift across
     rungs; TODA-OPEN otherwise (all honest; a fitted closure
     is only the existence signal).

 S3  POLE-FREE CORRIDOR (the positivity reading): per full-
     window rung (all 37) track min_k tau^{(k)}(s) on the
     frozen grid UNION {1.0}: NO section minor may cross zero
     on [0, 1] (the s-deformation statement of the wall: the
     corridor from the trivial point to the wall is pole-free/
     sign-stable).  Print the closest approach min_{k,s}
     tau^{(k)} and where.  TYPE: CORRIDOR-CLEAR iff positive
     throughout on every tested rung; else CORRIDOR-CROSSED
     (census printed).  THEN the decisive structural readout:
     the same corridor for the EPSTEIN and SCRAMBLE controls
     (kz 9) -- the controls MUST cross before (or at) s = 1
     since their walls are violated; print s* per control
     (the 'pole position' that distinguishes truth from
     controls: the truth keeps the pole beyond s = 1, the
     controls pull it inside).

 S4  THE POLE-DISTANCE LAW (report only): per truth rung the
     EXACT pole s*_h = 1/lam_max(C_h) (symmetric eig; identity
     (iii)), the wall margin tau_h = 1 - lam_max, the exact
     relation s*_h - 1 = tau_h/(1 - tau_h), and the h-trend
     (LS slope of log(s*_h - 1) against log h).  The identity
     is elementary but organizing; stated honestly, no bar.

 C   CONTROLS (kz 9, must fire; kill KC): Epstein and scramble
     combs, covered structurally in S3 -- fires iff the fixed
     12-window is UNAVAILABLE (frame death) OR the control pole
     s* <= 1 (corridor crossed).  Pipeline persistence printed.

KILLS: KP pipeline (full-window census != 37 / Lanczos
breakdown) -> PIPELINE-BROKEN; KW wards (S1 variational /
spectral-trace agreement) -> WARD-BROKEN; KC controls silent ->
CONTROL-DEAD.  S2/S3 types and S4 are TYPED / reported, never
kill.

VERDICT (frozen enum): SFLOW-MEASURED (+ typed sublabels
TODA-CLOSED(t*) / TODA-VARYING(t*) / TODA-OPEN and
CORRIDOR-CLEAR / CORRIDOR-CROSSED) / PIPELINE-BROKEN /
WARD-BROKEN / CONTROL-DEAD.

HONEST FRAME: S1 and the pole identity are exact algebra --
their wards protect the bookkeeping, they prove nothing about
the wall.  The value content is (a) whether a Toda time
EXISTS in which the section flow closes bilinearly (measured,
not derived -- derivation from the IIKS generators remains
PRIME.PORT.PAINLEVE.01), and (b) the pole-free corridor with
the control pole positions.  NO RH claim.  No marker moves.

FIREWALL: no zeros, no prime oracles (AST scan; banned:
zetazero/nzeros/primerange/isprime/primepi/nextprime/prevprime);
v563 READ-ONLY; RNG only in the declared scramble control;
stdout only.

Sources (read-only): v563_paper2_readouts;
port_cocycle_window_probe (C_J machinery, VERBATIM);
feshbach_hessian_probe (pipeline + ladder scope, VERBATIM);
port_tau_determinant_probe (scalar variational ward, declared
input); port_tau_hirota_probe (minor ladder + s-family seed,
VERBATIM machinery).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/port_sflow_toda_probe.py
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
N_FULLWIN_FROZEN = 37
NW = 12
HEAVY_RUNGS = (12, 20, 26, 40, 52)
N_DEEPEST = 3
S_WARD = (0.3, 0.6, 0.9)
FD_H = 1e-3
WARD_BAR = 1e-8
SPEC_BAR = 1e-9
NGRID = 200
S_MAX = 0.999
TODA_RES_BAR = 0.05
TODA_STAB_BAR = 0.5
BANNED_IDS = ("zetazero", "nzeros", "primerange", "isprime",
              "primepi", "nextprime", "prevprime")

CHECKS = []
KILLS = []
AMENDMENTS = []
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


# ---- shared machinery, VERBATIM from the round-39/44 chain ----

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


def rung_data(kz, scramble_seed=None, comb=None):
    rr = core.build_window(kz, scramble_seed=scramble_seed)
    h, M, D, alpha = rr["h"], rr["M"], rr["D"], rr["alpha"]
    uu = np.asarray(rr["uu"], float)
    mm = 2.0 * np.asarray(rr["lam"], float)
    if comb is not None:
        uu, mm = comb
    c_at, _ = core.atom_lags_at(alpha, M, uu, mm)
    c_ar = np.asarray(core.arch_lags(M, D), float)
    d = grid_density(c_ar + np.asarray(c_at, float))
    return dict(d=d, L=2 * M - 2, h=h, alpha=alpha)


def pipeline(d_total, h):
    """Folded measure -> Lanczos -> E -> 12-window Schur C_J.
    Returns C_J or a typed string (VERBATIM structure of the
    feshbach_hessian_probe pipeline, C_J only)."""
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
    if len(jav) < NW:
        return "WINDOW-SHORT:%d" % len(jav)
    iw = [idx[j] for j in jav]
    io = [k for k in range(E.shape[0]) if k not in set(iw)]
    Eo = E[np.ix_(io, io)]
    IO = np.eye(len(io)) - Eo
    Ex = E[np.ix_(iw, io)]
    CJ = E[np.ix_(iw, iw)] + Ex @ np.linalg.solve(IO, Ex.T)
    return 0.5 * (CJ + CJ.T)


# ---- s-flow machinery -----------------------------------------

def s_grid():
    """Frozen fine grid on [0, S_MAX], denser near 1."""
    u = np.linspace(0.0, 1.0, NGRID)
    return S_MAX * (1.0 - (1.0 - u) ** 2)


def section_eigs(CJ):
    """Eigenvalues of every leading section C_k, k = 1..NW."""
    return [np.linalg.eigvalsh(CJ[:k, :k]) for k in range(1, NW + 1)]


def spectral_flow(evs, ss):
    """Exact spectral route on the grid ss:
    logtau[k-1, j] = log tau^{(k)}(s_j),
    L[k-1, j]      = d/ds log tau^{(k)},
    Lp[k-1, j]     = d^2/ds^2 log tau^{(k)}.
    Returns (logtau, L, Lp, pos) -- pos = all 1 - s lam > 0."""
    G = len(ss)
    logtau = np.full((NW, G), np.nan)
    L = np.full((NW, G), np.nan)
    Lp = np.full((NW, G), np.nan)
    pos = True
    for k in range(NW):
        ev = np.asarray(evs[k], float)[:, None]
        q = 1.0 - ss[None, :] * ev
        if np.any(q <= 0.0):
            pos = False
            continue
        logtau[k] = np.sum(np.log(q), axis=0)
        L[k] = np.sum(-ev / q, axis=0)
        Lp[k] = np.sum(-(ev ** 2) / q ** 2, axis=0)
    return logtau, L, Lp, pos


def tau_grid(evs, ss):
    """tau^{(k)}(s_j) exactly (spectral product), (NW, G)."""
    T = np.empty((NW, len(ss)))
    for k in range(NW):
        ev = np.asarray(evs[k], float)[:, None]
        T[k] = np.prod(1.0 - ss[None, :] * ev, axis=0)
    return T


def d2_of_candidate(name, ss, L, Lp):
    """Exact chain rule: D2_t log tau from f' = L, f'' = Lp."""
    if name == "t=s":
        return Lp, np.ones(len(ss), bool)
    if name == "t=log(1/(1-s))":
        w = 1.0 - ss
        return (w ** 2)[None, :] * Lp - w[None, :] * L, \
            np.ones(len(ss), bool)
    if name == "t=log s":
        m = ss > 0.0
        return (ss ** 2)[None, :] * Lp + ss[None, :] * L, m
    raise ValueError(name)


def fit_affine(y, x):
    """LS fit y = a x + b; per-point relative residuals."""
    G = np.column_stack([x, np.ones(len(x))])
    coef, *_ = np.linalg.lstsq(G, y, rcond=None)
    a, b = float(coef[0]), float(coef[1])
    res = np.abs(y - G @ coef) / (np.abs(y) + np.abs(a * x)
                                  + abs(b) + 1e-300)
    return a, b, res


TIME_CANDIDATES = ("t=s", "t=log(1/(1-s))", "t=log s")


def main():
    section("PRIME.PORT.SFLOW.01 -- the exact s-direction flow "
            "of the port tau minors: variational ward, Toda "
            "time test, pole-free corridor (EXPLORATION ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s"
          % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
    print("    NO RH claim; no marker moves.")
    print("\nS0 -- firewall")
    check("S0.1 AST firewall clean", not ast_scan(BANNED_IDS))

    # ---------------- P0: build the ladder ---------------------
    section("P0 -- the fixed-window ladder (all full-window "
            "rungs, h <= 900; pipeline VERBATIM)")
    rungs = {}
    short = []
    for kz in core.frame_a_zones():
        b = rung_data(kz)
        if b["h"] > 900:
            continue
        CJ = pipeline(b["d"], b["h"])
        if isinstance(CJ, str):
            short.append((kz, CJ))
            continue
        rungs[kz] = dict(b=b, CJ=CJ, evs=section_eigs(CJ))
    print("    full-window rungs: %d | window-short (typed, "
          "excluded): %s"
          % (len(rungs), ["kz%d %s" % t for t in short]))
    check("P0.1 ladder census %d == %d (frozen)"
          % (len(rungs), N_FULLWIN_FROZEN),
          len(rungs) == N_FULLWIN_FROZEN, kill="KP")
    if len(rungs) < 6:
        return finish("n/a", "n/a")
    order = sorted(rungs, key=lambda k: rungs[k]["b"]["h"])
    deepest = list(order[-N_DEEPEST:])
    s1_set = sorted(set(HEAVY_RUNGS) | set(deepest),
                    key=lambda k: rungs[k]["b"]["h"])
    print("    S1/S2 rung set (frozen rule: heavy %s + %d "
          "deepest by h, dedup): %s"
          % (list(HEAVY_RUNGS), N_DEEPEST,
             ["kz%d(h%d)" % (kz, rungs[kz]["b"]["h"])
              for kz in s1_set]))

    # ---------------- S1: exact variational ward ---------------
    section("S1 -- EXACT VARIATIONAL WARD: d/ds log tau^(k) = "
            "-tr[M_k(s)^{-1} C_k] per section, trace route vs "
            "4th-order FD of slogdet, at s in %s" % (S_WARD,))
    worst_fd = 0.0
    worst_sp = 0.0
    print("\n    %-4s %-5s %-11s %-11s" % (
        "kz", "h", "max|L-FD|/L", "max|L-spec|/L"))
    for kz in s1_set:
        r = rungs[kz]
        CJ = r["CJ"]
        w_fd = 0.0
        w_sp = 0.0
        for s0 in S_WARD:
            for k in range(1, NW + 1):
                Ck = CJ[:k, :k]
                Mk = np.eye(k) - s0 * Ck
                Lan = -float(np.trace(np.linalg.solve(Mk, Ck)))

                def f(s, Ck=Ck, k=k):
                    sg, ld = np.linalg.slogdet(np.eye(k) - s * Ck)
                    assert sg > 0.0
                    return ld

                fd = (-f(s0 + 2 * FD_H) + 8.0 * f(s0 + FD_H)
                      - 8.0 * f(s0 - FD_H) + f(s0 - 2 * FD_H)) \
                    / (12.0 * FD_H)
                sc = max(abs(Lan), 1e-30)
                w_fd = max(w_fd, abs(Lan - fd) / sc)
                ev = r["evs"][k - 1]
                Lsp = -float(np.sum(ev / (1.0 - s0 * ev)))
                w_sp = max(w_sp, abs(Lan - Lsp) / sc)
        worst_fd = max(worst_fd, w_fd)
        worst_sp = max(worst_sp, w_sp)
        print("    %-4d %-5d %-11.1e %-11.1e"
              % (kz, r["b"]["h"], w_fd, w_sp))
    check("W1 JACOBI PER SECTION: analytic vs FD4, worst rel "
          "%.1e <= %.0e (k = 1..12, s in %s, %d rungs)"
          % (worst_fd, WARD_BAR, S_WARD, len(s1_set)),
          worst_fd <= WARD_BAR, kill="KW")
    check("W2 SPECTRAL = TRACE route, worst rel %.1e <= %.0e "
          "(guards the S2 machinery)" % (worst_sp, SPEC_BAR),
          worst_sp <= SPEC_BAR, kill="KW")

    # ---------------- S2: the Toda test -------------------------
    section("S2 -- THE TODA TEST: D2_t log tau^(k) = a_k r_k + "
            "b_k with constant a_k, b_k?  (frozen grid, %d "
            "points on [0, %.3f], denser near 1; candidates %s)"
            % (NGRID, S_MAX, list(TIME_CANDIDATES)))
    ss = s_grid()
    flows = {}
    for kz in s1_set:
        lt, L, Lp, pos = spectral_flow(rungs[kz]["evs"], ss)
        flows[kz] = dict(lt=lt, L=L, Lp=Lp, pos=pos)
        if not pos:
            print("    NOTE kz %d: nonpositive section minor on "
                  "the grid -- excluded from the fit (corridor "
                  "census in S3)" % kz)
    fit_rungs = [kz for kz in s1_set if flows[kz]["pos"]]
    cand_stats = {}
    for cname in TIME_CANDIDATES:
        res_all = []
        a_by_k = {k: [] for k in range(1, NW)}
        med_by_rung = []
        for kz in fit_rungs:
            fl = flows[kz]
            D2, m = d2_of_candidate(cname, ss, fl["L"], fl["Lp"])
            # log tau^(0) := 0 row prepended for r_k, k = 1..11
            LT = np.vstack([np.zeros(len(ss)), fl["lt"]])
            res_rung = []
            for k in range(1, NW):        # tau^(k), k = 1..11
                x = np.exp(LT[k + 1, m] + LT[k - 1, m]
                           - 2.0 * LT[k, m])
                y = D2[k - 1, m]
                a, b, res = fit_affine(y, x)
                a_by_k[k].append(a)
                res_all.extend(res.tolist())
                res_rung.extend(res.tolist())
            med_by_rung.append(float(np.median(res_rung)))
        spreads = []
        for k in range(1, NW):
            av = np.asarray(a_by_k[k], float)
            spreads.append(
                float(av.max() - av.min())
                / max(abs(float(np.median(av))), 1e-30))
        cand_stats[cname] = dict(
            med=float(np.median(res_all)),
            mx=float(np.max(res_all)),
            med_rung=med_by_rung,
            spread=float(np.median(spreads)),
            a_by_k=a_by_k)
    print("\n    %-16s %-9s %-9s %-11s %s" % (
        "candidate", "med res", "max res", "a_k spread",
        "per-rung median residuals"))
    for cname in TIME_CANDIDATES:
        st = cand_stats[cname]
        print("    %-16s %-9.3f %-9.3f %-11.3f %s"
              % (cname, st["med"], st["mx"], st["spread"],
                 " ".join("%.3f" % v for v in st["med_rung"])))
    best = min(TIME_CANDIDATES, key=lambda c: cand_stats[c]["med"])
    bst = cand_stats[best]
    stable = bst["spread"] <= TODA_STAB_BAR
    print("\n    best candidate: %s (median residual %.3f; "
          "cross-rung a_k spread %.3f, bar %.1f)"
          % (best, bst["med"], bst["spread"], TODA_STAB_BAR))
    print("    %-3s %-13s %-11s" % ("k", "median a_k", "spread"))
    for k in range(1, NW):
        av = np.asarray(bst["a_by_k"][k], float)
        print("    %-3d %+.6e %-11.3f"
              % (k, float(np.median(av)),
                 float(av.max() - av.min())
                 / max(abs(float(np.median(av))), 1e-30)))
    if bst["med"] <= TODA_RES_BAR and stable:
        sub_toda = "TODA-CLOSED(%s)" % best
    elif bst["med"] <= TODA_RES_BAR:
        sub_toda = "TODA-VARYING(%s)" % best
    else:
        sub_toda = "TODA-OPEN"
    check("S2.s Toda bilinear form typed %s (best median "
          "residual %.3f vs bar %.2f; a fitted closure is only "
          "the existence signal -- derivation from the IIKS "
          "generators is PRIME.PORT.PAINLEVE.01)"
          % (sub_toda, bst["med"], TODA_RES_BAR), True)

    # ---------------- S3: the pole-free corridor ----------------
    section("S3 -- POLE-FREE CORRIDOR: min_k tau^(k)(s) on "
            "[0, 1] (grid + s = 1.0 exactly) on ALL %d rungs; "
            "then the control corridors + crossing points s*"
            % len(rungs))
    ss1 = np.append(ss, 1.0)
    crossed = []
    closest = (float("inf"), None, None, None)  # val, kz, k, s
    for kz in order:
        T = tau_grid(rungs[kz]["evs"], ss1)
        i_min = int(np.argmin(T))
        kmin, jmin = divmod(i_min, len(ss1))
        vmin = float(T[kmin, jmin])
        if vmin < closest[0]:
            closest = (vmin, kz, kmin + 1, float(ss1[jmin]))
        if np.any(T <= 0.0):
            kk, jj = np.nonzero(T <= 0.0)
            crossed.append((kz, int(kk[0]) + 1,
                            float(ss1[jj[0]])))
    corridor_clear = len(crossed) == 0
    sub_corr = ("CORRIDOR-CLEAR" if corridor_clear
                else "CORRIDOR-CROSSED")
    check("S3.s truth corridor typed %s -- crossings (kz, k, "
          "s): %s" % (sub_corr, crossed if crossed else "none"),
          True)
    print("    closest approach: min_{k,s} tau^(k) = %.6e at "
          "kz %d, k = %d, s = %.4f"
          % (closest[0], closest[1], closest[2], closest[3]))
    print("    (the corridor from tau = 1 at s = 0 to the wall "
          "at s = 1 is %s on every tested rung)"
          % ("pole-free/sign-stable"
             if corridor_clear else "NOT pole-free"))

    # controls: the decisive structural readout
    print("\n    CONTROLS (kz 9): the control walls are "
          "violated, so their corridors MUST cross before "
          "(or at) s = 1 -- the pole position s* separates "
          "truth from controls.")
    rr9 = core.build_window(9)
    N_E = int(math.floor(math.exp(2.0 * rr9["alpha"]))) + 1
    lamE_ = lambda_eps(N_E)
    nn = np.nonzero(np.abs(lamE_) > 1e-12)[0]
    ok_ctl = True
    ctl_report = []
    for nmc, kw in (("Epstein", dict(comb=(
            np.log(nn.astype(float)),
            2.0 * lamE_[nn] / np.sqrt(nn.astype(float))))),
            ("scramble", dict(scramble_seed=1))):
        b_c = rung_data(9, **kw)
        CJ = pipeline(b_c["d"], b_c["h"])
        if isinstance(CJ, str):
            print("    %-8s: %s -> fires via FRAME DEATH (the "
                  "fixed 12-window does not exist on this comb)"
                  % (nmc, CJ))
            ctl_report.append((nmc, "frame-death"))
            continue
        evc = section_eigs(CJ)
        lam_mx = float(np.max(evc[-1]))
        s_star = (1.0 / lam_mx) if lam_mx > 0 else float("inf")
        # grid confirmation of the first crossing
        sg = np.linspace(0.0, 1.2, 1201)
        Tc = tau_grid(evc, sg)
        neg = np.nonzero(np.any(Tc <= 0.0, axis=0))[0]
        s_grid_cross = float(sg[neg[0]]) if len(neg) else None
        fired = s_star <= 1.0
        ok_ctl &= fired
        ctl_report.append((nmc, s_star))
        print("    %-8s: lam_max(C) = %.6f -> pole s* = %.6f "
              "(exact 1/lam_max; grid-confirmed first crossing "
              "at s = %s) -> %s"
              % (nmc, lam_mx, s_star,
                 ("%.3f" % s_grid_cross)
                 if s_grid_cross is not None else ">1.2",
                 "FIRES (pole inside [0,1])" if fired
                 else "silent"))
    check("C1 CONTROLS FIRE (frame death / pole s* <= 1): %s"
          % (["%s: %s" % (n, v if isinstance(v, str)
                          else "%.4f" % v)
              for n, v in ctl_report]), ok_ctl, kill="KC")

    # ---------------- S4: the pole-distance law -----------------
    section("S4 -- THE POLE-DISTANCE LAW (report only): s*_h = "
            "1/lam_max(C_h) EXACTLY; s*_h - 1 = tau_h/(1 - "
            "tau_h) with the wall margin tau_h = 1 - lam_max")
    print("\n    %-4s %-5s %-10s %-11s %-11s %-11s" % (
        "kz", "h", "lam_max", "tau_h", "s*_h", "s*_h - 1"))
    hs, margins = [], []
    all_out = True
    for kz in order:
        r = rungs[kz]
        lam_mx = float(np.max(r["evs"][-1]))
        tau_h = 1.0 - lam_mx
        s_star = 1.0 / lam_mx if lam_mx > 0 else float("inf")
        all_out &= s_star > 1.0
        print("    %-4d %-5d %-10.6f %-11.4e %-11.6f %-11.4e"
              % (kz, r["b"]["h"], lam_mx, tau_h, s_star,
                 s_star - 1.0))
        if s_star > 1.0 and math.isfinite(s_star):
            hs.append(float(r["b"]["h"]))
            margins.append(s_star - 1.0)
    if len(margins) >= 3:
        slope = float(np.polyfit(np.log(hs),
                                 np.log(margins), 1)[0])
        print("\n    h-trend: LS slope of log(s*_h - 1) vs "
              "log h = %+.3f  (s*_h - 1 = tau_h/(1 - tau_h) "
              "~ tau_h for small tau_h: the wall margin IS "
              "the pole distance)" % slope)
    print("""
    HONEST STATEMENT (elementary but organizing): tau^{(12)}(s)
    = prod_i (1 - s lam_i(C_h)) has its first positive zero at
    s*_h = 1/lam_max(C_h) exactly, and by Cauchy interlacing no
    section minor crosses earlier.  So the wall margin tau_h =
    1 - lam_max and the pole distance s*_h - 1 carry the SAME
    information: RH on the ladder = the pole of the s-flow
    stays outside [0, 1] uniformly in h.  The truth keeps the
    pole beyond s = 1 on every tested rung%s; the controls pull
    it inside (S3).  This is a finite-window measurement, NOT
    an RH claim.""" % ("" if all_out else
                       " -- EXCEPT the crossings censused in S3"))

    return finish(sub_toda, sub_corr)


def finish(sub_toda, sub_corr):
    section("V -- FROZEN VERDICT")
    n_pass = sum(1 for _n, okk in CHECKS if okk)
    n_tot = len(CHECKS)
    if KILLS:
        VERDICT = {"KP": "PIPELINE-BROKEN", "KW": "WARD-BROKEN",
                   "KC": "CONTROL-DEAD"}[KILLS[0]]
    else:
        VERDICT = "SFLOW-MEASURED"
    print("\n  VERDICT: %s (%s, %s)" % (VERDICT, sub_toda,
                                        sub_corr))
    print("\n  SPEC v2 amendments (fail-first preserved): %s"
          % ("; ".join(AMENDMENTS) if AMENDMENTS else "none"))
    print("""
  HONEST FRAME (as frozen): the per-section Jacobi identity and
  the pole identity s* = 1/lam_max are exact algebra -- their
  wards protect the bookkeeping.  The value content is (a) the
  measured Toda time (if any) in which the section flow closes
  bilinearly with constant coefficients, and (b) the pole-free
  corridor [0, 1] on the truth against the control poles pulled
  inside.  The flow equations must FOLLOW from the IIKS
  generators (PRIME.PORT.PAINLEVE.01) before anything is
  claimed.  NO RH claim.  No marker moves.""")
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed"
          % (time.time() - T0, n_tot, n_tot - n_pass))
    return 0 if n_pass == n_tot else 1


if __name__ == "__main__":
    raise SystemExit(main())
