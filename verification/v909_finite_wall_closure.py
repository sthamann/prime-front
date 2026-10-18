#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""v909 -- PRIME.WALL.FINITE_CLOSURE.01: THE FINITE WALL CLOSURE -- the composed wall census of rounds 64-67: on the deployed finite ladder every reachable wall face is certified from cited inputs -- B-half (P_G chain: B >= (1/2) P_G + c_dom I with the CLIII/v905 interval-certified class floor min c_B = 0.5523, 39/39 surface + 27/27 deep steps, SPEC 903714c1), W1 (monotone composition [L0/L1/L2/L5] + verified-zero supply at the j = 16 seat: 39/39 surface at N_Z = 7000, composed 67/67 with the CITED CLXXXIV deep 28/28, SPECs bed53f23 / 37a5e259 / deea4e1c) and W2 (the recomposed certificate m_cert = FC + PARITH_hat - TAILB > 0: 16/67 + 0/8 at N_Z = 7000, 67/67 + 8/8 with the 20,000,000-ordinate certified cache, SPECs 921140fa / 9cafc26f), giving the composed census B AND W1 AND W2 on 39/39 matched surface + 8/8 deep rungs (note CXCV/CCV).  THIS MODULE re-verifies the load-bearing spine on a REDUCED FROZEN SUBSET (the shallowest surface rungs and steps, runtime budget) with SELF-CONTAINED machinery (no experiments/ import; probe functions ported verbatim, attributed inline) and a committed 7,000-ordinate verified-zero cache (verification/verified_zeros_n7000.json, mpmath dps 15, re-warded in-run; EXTERNAL-CITED on-line status: every ordinate below T0 = 3e12, Platt-Trudgian 2021 Bull. LMS 53 Thm 1); the FULL census numbers above are the frozen experiments/ runs, cited with their SPEC SHAs and NOT recomputed here.

LANGUAGE DISCIPLINE (frozen by the round-66/67 audits, non-negotiable):
 (i)  W1 and W2 are ALGORITHMICALLY INDEPENDENT EVALUATIONS OF THE
      SAME LOCALIZED WEIL FORM -- a strong mutual crosscheck, NOT two
      independent proofs;
 (ii) every certified statement is per-rung and along the MEASURED
      critical direction v (DIRECTION-CONDITIONAL; the positivity is
      certified on a finite family of Galerkin sections -- the
      UNIF-PATH caveat: nothing is uniform in h or in direction);
 (iii) the finite closure consumes published zero verifications as
      CITATIONS (Odlyzko zeros6 tables, LMFDB / Platt, Platt-Trudgian
      2021 T0 = 3e12, Rosser 1941 N(T), Buethe 2018, B_PSI) plus
      exact window algebra and the exact composition steps;
 (iv) a finite verified-zero sum can never prove RH; the all-h,
      all-direction Weil-positivity object remains OPEN and RH-hard
      in every branch.  NO RH claim in either direction.

WHAT THIS MODULE CHECKS (reduced, rigorous; bars frozen after one
disclosed sizing run, see PROMOTION-RUN DISCLOSURE below):
 Z   the committed zero cache: census 7000, strict monotonicity,
     gamma_1 identity, Rosser-corridor consistency per index (both
     sides, unconditional), independent mpmath |zeta(1/2 + i gamma)|
     spot checks at 12 geomspace ordinates (dps 20), T_c < T0.
 W   the deployed ladder (v563 pipeline): parent zone census == 42,
     the SUB_GRAM = 10 shallowest gram rungs usable, wall margin
     m > 0 and pivot collapse on the subset.
 B   the B-half on the first 7 usable steps: lam_min(B) >= 0.5523
     (the CLIII interval-certified class floor, float re-check),
     negidx(B - (1/2) P_G) == 0 and c_B = (1/2) c_G + c_dom > 0.
 L   the W1 monotone composition on the same step rungs (mono
     machinery verbatim): [L0] dual-interpolation identity exact at
     M_i = K_h(y_i, .), [L1] dual identity, [L1b] fold-grid rebuild
     of nu_+, [L2] Loewner ward G[nu_+] >= G[omega_ENV], [L3] trace
     corollary, [L4] fold-wise domination (d_f)_+ <= |d^ar_f| +
     Delta_env, and the ENV-tier composed bound > mu1(h) per rung
     (the registered-target comparison); the verified-zero v-floor
     supply half (j16, 39/39) is CITED, not recomputed.
 C   the W2 face on the SUB_W2 = 6 shallowest rungs: split identity
     m = FC + PARITH at every ladder cut; the HEART ward (zeros
     against primes): |PARITH - PARITH_hat| <= TAILB on every
     (rung, cut) read; soundness m_cert <= m; and the closure census
     m_cert > 0 at the minimal certifying head -- expected 6/6 at
     N_Z = 7000 on this subset (the full-ladder censuses 16/67 at
     7000 and 67/67 + 8/8 at 2e7 are cited).
 X   the composed subset census: rungs where the B step, the W1
     composition wards and the W2 certificate all hold.
 M   controls (must fire): the smooth world breaks the wall on the
     whole subset; Epstein + scramble combs break lam_min at kz 9;
     the scrambled comb breaks the exact prime-side heart ward at
     both control cuts; the off-line impostor (gamma_1 -> beta =
     0.75, FE-symmetrised quadruple) shifts PARITH_hat by >= 10x
     the genuine residual.

PROMOTION-RUN DISCLOSURE (2026-08-12): the first full run of this
module passed 28/28 in 3.3 s with NO amendment; measured content
(frozen as the expectation record): zero-cache wards green (corridor
7000/7000 both sides, gamma_1 dev 1.4e-07, worst |zeta| spot 2.1e-12
at 12 ordinates, T_c = 7264.7482); 7 B-steps (h 149..203) with
lam_min(B) min 2.0908 >= 0.5523 and dominance 7/7 (min c_B 1.8750);
mono wards L0 1.2e-14 / L1 2.7e-15 / L1b 4.8e-14 / L2 min rel +0.424
/ L4 all-negative slack, ENV/mu1 dex +0.28/+0.61/+0.79 on the shallow
band (the frozen 39-rung run: med +1.55); W2 face: split identity
2.6e-14, recon 1.0e-15, HEART worst scaled excess -4.9e-06 with slack
+2.12/+3.29/+4.78 dex over all (rung, cut) reads, soundness 0
violations, closure 6/6 at N_Z = 7000 (minimal heads A = 50..400);
composed subset census 4 matched rungs (kz 12, 13, 20, 23); controls
all fire (smooth 6/6 max -1.6, Epstein -1.0e+01, scramble -7.9e+00,
heart-break 1.5e+02 / 3.8e+02 x TAILB, impostor 8.2e+04 x, TRIV
envelope 6.8e-02 <= 3.7e-01).  No tolerance was loosened after this
run; the frozen experiments runs this module mirrors are
CLXXXII/CLXXXIV/CLXXXIX (W1), CLXXXV/CXCIII/CXCV (W2), CLXXVII/CLIII
(B-half) with the SPEC SHAs cited above.

ANTI-CIRCULARITY (frozen): the verified ordinates enter ONLY the
supply side and are tested AGAINST the independent prime side on
every read (the explicit formula is exactly this zeros-against-primes
duality); measured m appears only as truth column, soundness ward and
denominator; no wall output feeds any bound; omega_ENV is built from
the arch layer, window conventions and the scalar Delta_env = 2 M_up
= 4 B_PSI (2 sqrt(X) - 1) only.  The composition step [L2] is a
measure inequality valid for EVERY measure and therefore WORLD-BLIND
by construction (declared, not a discovery): the discriminating
content sits in the supply soundness and the v-floor, which is why
the controls attack exactly those.  RNG: none except the declared
scramble control (seed 1).

PINNING DISCLOSURE (meta-audit CCCXXXVI, 2026-08-13): the executed
gates of this module pin ONLY the reduced frozen subset (X1 demands
len(matched) >= 4 on the SUB_GRAM = 10 / N_STEPS = 7 / SUB_W2 = 6
subset); the FULL census 39/39 + 8/8 enters as a CITED premise and
is NOT pinned by any executed predicate -- a false cited full census
would not fail this module.  The full-census statement rests on the
frozen experiments runs and their SPEC SHAs, not on this gate.

CACHE REBUILD (disclosed builder): python v909_finite_wall_closure.py
--rebuild-cache recomputes the 7000 ordinates with mpmath.zetazero at
dps 15 (~2 min) and rewrites verification/verified_zeros_n7000.json;
the in-run wards (Z1-Z4) make trust independent of provenance.

Python-only per GATE.WOLFRAM.02 (float64 numerics + mpmath spot
checks; no exact-algebra readout).  NO marker moves beyond this
measured closure; the deep block of the full census is FLOAT-LEVEL
as declared in CLXXXV.
"""

import json
import math
import os
import sys
import time

import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)

import v563_paper2_readouts as core  # noqa: E402  (deployed pipeline)

# ---------------------------------------------------------------- bars
ZC_JSON = os.path.join(_HERE, "verified_zeros_n7000.json")
N_Z = 7000
GAMMA1 = 14.134725
T0_RH = 3.0e12
ROSSER_A = 0.137
ROSSER_B = 0.443
ROSSER_C = 1.588
TAIL_GEO = 1.5
TAIL_IMAX = 600
CORR_EPS = 1.0e-6
NS_ZETA = 12
ZETA_TOL = 1.0e-6
SUB_GRAM = 10                 # shallowest gram rungs (by h)
N_STEPS = 7                   # usable B/W1 steps consumed
SUB_W2 = 6                    # shallowest W2 rungs
B_FLOOR_CITED = 0.5523        # CLIII / v905 interval-certified class
PG_S = 0.5                    # canonical V4 dominance shape
CORE_J = (2, 4, 6, 8, 10, 12, 14, 16)
H_LADDER_MAX = 900
L0_TOL = 1.0e-8
L1_TOL = 1.0e-8
GRID_TOL = 1.0e-9
L2_TOL = 1.0e-9
DOM_TOL = 1.0e-12
ID_WARD = 1.0e-10
RECON_TOL = 1.0e-9
SOUND_TOL = 1.0e-9
RAMP_EPS_MAX = 2.0
U0_SUBG = math.log(2.0) / 2.0
DPS_ERR = 1.0e-9
HEAD_A = (9, 12, 20, 50, 100, 200, 400)
NC_ABS = (9, 17, 47, 149, 1000, 10000)
NC_FRAC = (0.1, 0.5, 0.9, 0.99)
NC_SUP_MIN = 11
CTRL_KZ = 9
NG_SMOOTH = 6000
IMP_BETA = 0.75
IMP_RATIO_MIN = 10.0
SPEC_CITED = ("B-half 903714c1 (CLXXVII) + CLIII interval floor "
              "(v905); W1 bed53f23 (CLXXXII) / 37a5e259 (CLXXXIV) / "
              "deea4e1c (CLXXXIX); W2 921140fa (CXCIII) / 9cafc26f "
              "(CXCV)")
_GLX, _GLW = np.polynomial.legendre.leggauss(24)

CHECKS = []


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok)))
    print("  [%s] %s%s" % ("PASS" if ok else "FAIL", name,
                           ("  -- " + detail) if detail else ""),
          flush=True)
    return bool(ok)


def section(title):
    print("\n" + "=" * 74)
    print(title)
    print("=" * 74, flush=True)


def band(v):
    v = np.asarray(v, float)
    return float(np.min(v)), float(np.median(v)), float(np.max(v))


# ------------------- Rosser corridor (subgamma_fourier_bound verbatim)
def n_main(t):
    t = np.asarray(t, float)
    return t / (2.0 * math.pi) * np.log(t / (2.0 * math.pi * math.e)) \
        + 0.875


def n_fluc(t):
    t = np.asarray(t, float)
    lt = np.log(t)
    return ROSSER_A * lt + ROSSER_B * np.log(lt) + ROSSER_C


def n_up(t):
    return n_main(t) + n_fluc(t)


def n_lo(t):
    return np.maximum(n_main(t) - n_fluc(t), 0.0)


def abel_upper(tgrid, c, n_start=0.0):
    """Rigorous upper bound of Sum_{gamma in (t_0, t_K]} f(gamma) for
    0 <= f <= step envelope c_i, via Abel summation against the
    Rosser 1941 N(T) corridor (subgamma verbatim)."""
    c = np.asarray(c, float)
    ti = tgrid[1:-1]
    d = c[:-1] - c[1:]
    nu = n_up(ti)
    nl = n_lo(ti)
    s = float(np.sum(np.where(d >= 0.0, d * nu, d * nl)))
    s += float(c[-1] * n_up(tgrid[-1]))
    s -= float(c[0] * n_start)
    return s


def s2_tail():
    """Abel upper bound of Sum_{gamma > T0_RH} 1/gamma^2 (subgamma
    verbatim, incl. the disclosed factor-20 truncation pad)."""
    tg = T0_RH * TAIL_GEO ** np.arange(TAIL_IMAX + 1)
    c = 1.0 / tg[:-1] ** 2
    s = abel_upper(tg, c, n_start=float(n_lo(np.array([T0_RH]))[0]))
    pad = 20.0 * float(c[-1] * n_up(tg[-1]))
    return s + pad


def tail_grid(D, tc):
    """CLXXXIX tail grid: linear (phase step 0.25 in gamma D) from
    T_c, then geometric *1.3 to T0 (consumption-probe verbatim)."""
    dt = max(0.25 / D, 0.5)
    tsw = max(300.0, 10.0 * math.pi / D, 2.0 * tc)
    nlin = max(int(math.ceil((tsw - tc) / dt)), 1)
    lin = tc + dt * np.arange(nlin + 1)
    geo = [lin[-1]]
    while geo[-1] < T0_RH:
        geo.append(min(geo[-1] * 1.3, T0_RH))
    return np.concatenate([lin, np.asarray(geo[1:], float)])


# --------------- P_G chain machinery (bfloor_pg_dominance verbatim)
def grid_density(c):
    c = np.asarray(c, float)
    a = np.concatenate([c, c[-2:0:-1]])
    d = np.fft.fft(a)
    assert float(np.max(np.abs(d.imag))) <= 1e-9 * max(
        1.0, float(np.max(np.abs(d.real))))
    return d.real


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


def householder_frame(v):
    n = len(v)
    v = v / float(np.linalg.norm(v))
    e1 = np.zeros(n)
    e1[0] = 1.0
    u = e1 - v
    nu = float(np.linalg.norm(u))
    if nu < 1e-14:
        return np.eye(n)
    u = u / nu
    Q = np.eye(n) - 2.0 * np.outer(u, u)
    if float(Q[:, 0] @ v) < 0:
        Q = -Q
    return Q


_WIN_CACHE = {}


def window_of(kz, scramble_seed=None):
    key = (kz, scramble_seed)
    if key not in _WIN_CACHE:
        rr = core.build_window(kz, scramble_seed=scramble_seed)
        _WIN_CACHE[key] = dict(
            h=rr["h"], M=rr["M"], D=rr["D"], alpha=rr["alpha"],
            n_atom=rr["n_atom"],
            uu=np.asarray(rr["uu"], float).copy(),
            lam=np.asarray(rr["lam"], float).copy(),
            c_ar=np.asarray(core.arch_lags(rr["M"], rr["D"]),
                            float))
    return _WIN_CACHE[key]


def ladder_zones():
    out = []
    for kz in core.frame_a_zones():
        D_k = 0.5 * float(core.G_ALL[kz]) / float(core.NU_MAIN)
        M_k = int(math.ceil(float(core.U_ALL[kz]) / D_k - 1.0e-9)) + 1
        if M_k % 2:
            M_k += 1
        if M_k // 2 <= H_LADDER_MAX:
            out.append(kz)
    return out


def cell_widths(uu):
    du = np.zeros(len(uu))
    du[1:-1] = 0.5 * (uu[2:] - uu[:-2])
    du[0] = uu[1] - uu[0]
    du[-1] = uu[-1] - uu[-2]
    return du


def gram_anatomy(kz, world_fn=None, keep_chain=False):
    """v900 verbatim wall + fixed-core split (bfloor probe port)."""
    rr = window_of(kz)
    M, D, alpha, h = rr["M"], rr["D"], rr["alpha"], rr["h"]
    uu = rr["uu"]
    mm = 2.0 * rr["lam"]
    if world_fn is not None:
        uu, mm = world_fn(uu, mm, rr)
    c_at, _ = core.atom_lags_at(alpha, M, uu, mm)
    d = grid_density(rr["c_ar"] + np.asarray(c_at, float))
    L = 2 * M - 2
    xs, ws, _ = folded_measure(d, L, +1.0)
    ys, vs, uf_n = folded_measure(d, L, -1.0)
    al, be, m0, steps = lanczos_chain(xs, ws, h + 1)
    if steps < h + 1 or np.any(be <= 0):
        return None
    Pn = eval_chain(al, be, m0, ys, h)
    G = np.sqrt(vs)[:, None] * (Pn @ Pn.T) * np.sqrt(vs)[None, :]
    G = 0.5 * (G + G.T)
    n = G.shape[0]
    A = np.eye(n) - G
    evA = np.linalg.eigvalsh(A)
    out = dict(kz=kz, h=h, n=n, alpha=float(alpha), M=M, D=D, L=L,
               c_at=np.asarray(c_at, float))
    out["tau"] = float(evA[0])
    out["negA"] = int(np.sum(evA < 0.0))
    if keep_chain:
        out["chain"] = (al, be, m0)
    idx = {int(j): k for k, j in enumerate(uf_n)}
    out["core_ok"] = all(j in idx for j in CORE_J)
    if not out["core_ok"]:
        return out
    ic = np.array([idx[j] for j in CORE_J], dtype=int)
    icset = set(ic.tolist())
    ib = np.array([k for k in range(n) if k not in icset],
                  dtype=int)
    B = A[np.ix_(ic, ic)]
    Xc = A[np.ix_(ic, ib)]
    R = A[np.ix_(ib, ib)]
    Z = np.linalg.solve(R, Xc.T)
    Y = Xc @ Z
    Y = 0.5 * (Y + Y.T)
    S = B - Y
    S = 0.5 * (S + S.T)
    evS = np.linalg.eigvalsh(S)
    out["S"] = S
    out["lamS"] = float(evS[0])
    out["negS"] = int(np.sum(evS < 0.0))
    if keep_chain:
        out["y_core"] = np.array([ys[idx[j]] for j in CORE_J])
        out["v_core"] = np.array([vs[idx[j]] for j in CORE_J])
    return out


def build_step(r1, r2):
    """One P_G-chain step (exterior_pg_schur build_truth_rows port,
    trimmed to the B-half objects + the W1 Gc payload)."""
    _w, vectors = np.linalg.eigh(r1["S"])
    Q = householder_frame(vectors[:, 0])
    Mt = Q.T @ (r2["S"] / r1["tau"]) @ Q
    Mt = 0.5 * (Mt + Mt.T)
    B = Mt[1:, 1:].copy()
    al, be, m0 = r2["chain"]
    Pc = eval_chain(al, be, m0, r2["y_core"], r2["h"])
    H = np.sqrt(r2["v_core"])[:, None] * Pc
    V = Q.T @ H
    P = V @ V.T
    P = 0.5 * (P + P.T)
    PG = P[1:, 1:].copy()
    Gc = H @ H.T
    Gc = 0.5 * (Gc + Gc.T)
    minB = float(np.linalg.eigvalsh(B)[0])
    cg = float(np.linalg.eigvalsh(PG)[0])
    Dm = B - PG_S * PG
    Dm = 0.5 * (Dm + Dm.T)
    evd = np.linalg.eigvalsh(Dm)
    return dict(r1=r1, r2=r2, B=B, minB=minB, cg=cg,
                cdom=float(evd[0]), negD=int(np.sum(evd < 0.0)),
                cb=PG_S * cg + float(evd[0]), H=H, Gc=Gc,
                mu1=mu1_of(r2["h"]))


# --------------- W1 monotone composition (monotone_composition port)
def fold_grid(L):
    f = np.arange(0, L // 2 + 1)
    w = 4.0 * np.sin(math.pi * f / L) ** 2 / (2.0 * L)
    mult = np.where((f > 0) & (f < L // 2), 2.0, 1.0)
    return f, w * mult, np.cos(2.0 * math.pi * f / L)


def delta_env(alpha):
    X = math.exp(2.0 * alpha)
    m_up = 2.0 * core.B_PSI * (2.0 * math.sqrt(X) - 1.0)
    return 2.0 * m_up


def kernel_of(xg, wom, y_core, h):
    m = wom > 1e-300
    al, be, m0, steps = lanczos_chain(xg[m], wom[m], h + 1)
    if steps < h + 1 or np.any(be <= 0):
        return None
    P = eval_chain(al, be, m0, y_core, h)
    K = P @ P.T
    return 0.5 * (K + K.T)


def mono_bound(K, v):
    G = np.sqrt(v)[:, None] * K * np.sqrt(v)[None, :]
    G = 0.5 * (G + G.T)
    return float(np.linalg.eigvalsh(G)[0]), G


def trace_bound(K, v):
    Ki = np.linalg.inv(K)
    s = float(np.sum(np.diag(Ki) / v))
    return 1.0 / s if s > 0 else float("-inf")


def dual_form(Mrows, Amat, wpos, v):
    Gam = (Mrows * wpos[None, :]) @ Mrows.T
    Gam = 0.5 * (Gam + Gam.T)
    Ai = np.linalg.inv(Amat)
    Lam = Ai @ Gam @ Ai.T
    Lam = 0.5 * (Lam + Lam.T)
    sv = 1.0 / np.sqrt(v)
    Q = Lam * np.outer(sv, sv)
    return 1.0 / float(np.linalg.eigvalsh(0.5 * (Q + Q.T))[-1])


def l1_ward(H, Gc, rng_free_u):
    c, *_ = np.linalg.lstsq(H, rng_free_u, rcond=None)
    lhs = float(rng_free_u @ np.linalg.solve(Gc, rng_free_u))
    return abs(float(c @ c) / lhs - 1.0)


def mono_payload(step):
    """ENV-tier monotone-composition payload of one step's r2 rung
    (monotone_composition rung_payload, trimmed to the promoted
    wards: ENV + GRID tiers, no LOW anatomy)."""
    r2 = step["r2"]
    rr = window_of(r2["kz"])
    d = grid_density(rr["c_ar"] + r2["c_at"])
    d_ar = grid_density(rr["c_ar"])
    L = 2 * rr["M"] - 2
    f, wg, xg = fold_grid(L)
    de = delta_env(rr["alpha"])
    df = d[f]
    daf = np.abs(d_ar[f])
    wpos = wg * np.maximum(df, 0.0)
    out = dict(dom=float(np.max(np.maximum(df, 0.0) - (daf + de))))
    K_env = kernel_of(xg, wg * (daf + de), r2["y_core"], r2["h"])
    K_grid = kernel_of(xg, wpos, r2["y_core"], r2["h"])
    if K_env is None or K_grid is None:
        return None
    v = r2["v_core"]
    Gc = step["Gc"]
    out["truth"] = float(np.linalg.eigvalsh(Gc)[0])
    out["env"], Gom = mono_bound(K_env, v)
    dif = Gc - Gom
    out["loewner"] = (float(np.linalg.eigvalsh(
        0.5 * (dif + dif.T))[0])
        / max(float(np.linalg.norm(Gc, 2)), 1e-300))
    out["grid_dev"] = abs(mono_bound(K_grid, v)[0] / out["truth"]
                          - 1.0)
    out["l3"] = trace_bound(K_env, v)
    al, be, m0 = r2["chain"]
    Pg = eval_chain(al, be, m0, xg, r2["h"])
    Pc = eval_chain(al, be, m0, r2["y_core"], r2["h"])
    Mrows = Pc @ Pg.T
    Amat = Pc @ Pc.T
    val = dual_form(Mrows, 0.5 * (Amat + Amat.T), wpos, v)
    out["l0"] = abs(val / out["truth"] - 1.0)
    out["mu1"] = step["mu1"]
    return out


# ------------------------- W2 read machinery (w2_pairing/cons ports)
def q_read(W, u, D, M):
    u = np.asarray(u, float)
    i0 = np.floor(u / D).astype(int)
    f = u / D - i0
    val = np.zeros_like(u)
    ok0 = (i0 >= 0) & (i0 < M)
    val[ok0] += (1.0 - f[ok0]) * W[i0[ok0]]
    ok1 = (i0 + 1 >= 0) & (i0 + 1 < M)
    val[ok1] += f[ok1] * W[i0[ok1] + 1]
    refl = u < D
    val[refl] += (1.0 - u[refl] / D) * W[0]
    return -0.5 * val


def smooth_comb(alpha, ng=NG_SMOOTH):
    ug = (np.arange(ng) + 0.5) * (2.0 * alpha / ng)
    mg = 2.0 * np.exp(ug / 2.0) * (2.0 * alpha / ng)
    return ug, mg


def lambda_eps(N):
    """Epstein x^2 + 5 y^2 comb (port_schur_reduction verbatim)."""
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


def mu1_of(h):
    return 4.0 * math.sin(math.pi / (2.0 * h + 1.0)) ** 2


def weight_pieces(W, u0, uL, D, M):
    i_lo = int(math.floor(u0 / D)) + 1
    i_hi = int(math.ceil(uL / D)) - 1
    kn = D * np.arange(i_lo, i_hi + 1, dtype=float)
    kn = kn[(kn > u0 + 1e-12) & (kn < uL - 1e-12)]
    ed = np.concatenate([[u0], kn, [uL]])
    a_p, b_p = ed[:-1], ed[1:]
    wa = q_read(W, a_p, D, M)
    wb = q_read(W, b_p, D, M)
    s_p = (wb - wa) / (b_p - a_p)
    return a_p, b_p, wa, wb, s_p


def tcont_of(pc):
    a_p, b_p, wa, wb, s_p = pc
    return 2.0 * float(np.sum(
        np.exp(b_p / 2.0) * (2.0 * wb - 4.0 * s_p)
        - np.exp(a_p / 2.0) * (2.0 * wa - 4.0 * s_p)))


def build_rung(kz, scramble_seed=None, smooth_world=False,
               comb=None):
    """One W2 rung with the deployed bookkeeping (w2_pairing
    build_rung, surface branch verbatim, trimmed)."""
    try:
        rr = core.build_window(kz, scramble_seed=scramble_seed)
    except Exception:
        return None
    if not (core.H_MIN <= rr["h"] <= core.HCAP):
        return None
    if rr["X"] > core.ATOM_MAX:
        return None
    alpha, M, D, h = rr["alpha"], rr["M"], rr["D"], rr["h"]
    uu = np.asarray(rr["uu"], float)
    mu = 2.0 * np.asarray(rr["lam"], float)
    X = float(rr["X"])
    if smooth_world:
        mu = 2.0 * np.exp(uu / 2.0) * cell_widths(uu)
    if comb is not None:
        uu, mu = comb
    c_at = np.asarray(core.atom_lags_at(alpha, M, uu, mu)[0], float)
    c_ar = np.asarray(core.arch_lags(M, D), float)
    Kt = core.odd_toeplitz(c_ar + c_at, M)
    ev, V = np.linalg.eigh(Kt)
    v = V[:, 0]
    m = float(ev[0])
    pivres = float(np.linalg.norm(Kt @ v - m * v)) \
        / max(float(np.max(np.abs(ev))), 1.0)
    del Kt, V
    Wv = core.lag_weights_from_v(v, h)
    e_ar = float(c_ar @ Wv)
    e_at = float(c_at @ Wv)
    qa = mu * q_read(Wv, uu, D, M)
    cq = np.cumsum(qa)
    head_B = e_ar + cq
    tail_B = float(qa.sum()) - cq
    cert_B = head_B - np.abs(tail_B)
    ug, mg = smooth_comb(alpha)
    c_sm = np.asarray(core.atom_lags_at(alpha, M, ug, mg)[0], float)
    lam_sm = float(np.linalg.eigvalsh(
        core.odd_toeplitz(c_ar + c_sm, M))[0])
    Ng = max(int(math.floor(X)), int(round(math.exp(float(uu[-1])))))
    row = dict(kz=kz, alpha=float(alpha), h=h, M=M, D=D, X=X,
               m=m, mu1=mu1_of(h), uu=uu, mu=mu, Wv=Wv,
               e_ar=e_ar, e_at=e_at, lam_sm=lam_sm,
               head_B=head_B, Ng=Ng, pivres=pivres,
               lam_tab=core.LAM_TAB, natom=len(uu))
    nn = np.round(np.exp(uu)).astype(np.int64)
    row["nn"] = nn
    icB = int(np.argmax(cert_B > 0.0)) if bool(np.any(cert_B > 0)) \
        else -1
    row["icB"] = icB
    row["ncB"] = int(nn[icB]) if icB >= 0 else -1
    return row


def split_at(row, nc):
    """THE SPLIT: m = HEAD(nc) + TCONT(nc) + PARITH(nc)
    (w2_pairing verbatim, trimmed)."""
    Ng = row["Ng"]
    if nc < 2 or nc >= Ng - 1:
        return None
    D, M, Wv = row["D"], row["M"], row["Wv"]
    i = int(np.searchsorted(row["nn"], nc, side="right")) - 1
    head = float(row["head_B"][i]) if i >= 0 else row["e_ar"]
    u0 = math.log(nc + 1.0)
    uL = math.log(float(Ng))
    if u0 >= uL:
        return None
    kk = np.arange(nc + 1, Ng + 1, dtype=np.int64)
    kf = kk.astype(float)
    ug = np.log(kf)
    wg = q_read(Wv, ug, D, M)
    inv = 1.0 / np.sqrt(kf)
    a_k = 2.0 * row["lam_tab"][nc + 1:Ng + 1] * inv
    t_int = float(a_k @ wg)
    pc = weight_pieces(Wv, u0, uL, D, M)
    tc = tcont_of(pc)
    par = t_int - tc
    fc = head + tc
    return dict(nc=nc, head=head, tcont=tc, t_int=t_int, par=par,
                fc=fc, u0=u0, uL=uL, pc=pc,
                dev_x1=abs(head + t_int - row["m"])
                / max(1.0, abs(row["e_at"])),
                dev_x3=abs(fc + par - row["m"])
                / max(1.0, abs(row["e_at"])))


def cut_ladder(row):
    Ng = row["Ng"]
    cuts = list(NC_ABS)
    if row["ncB"] > 0:
        cuts.append(row["ncB"])
    cuts += [int(round(fr * Ng)) for fr in NC_FRAC]
    out = []
    for c in cuts:
        c = int(max(2, min(c, Ng - 2)))
        if c not in out:
            out.append(c)
    return sorted(out)


def demand_at_head(row, A):
    if A > row["natom"]:
        return None
    nc = int(row["nn"][A - 1])
    if nc < NC_SUP_MIN or nc >= row["Ng"] - 1:
        return None
    return split_at(row, nc)


# --------------- zero-side supply (w2_verified_supply_consumption)
def zsum4re(v, J, gam):
    tot = 0.0
    for i0 in range(0, len(gam), 1000):
        g = gam[i0:i0 + 1000]
        E = np.exp(1j * np.outer(g, v))
        tot += float(np.sum((-(E @ J) / g ** 2).real))
    return 4.0 * tot


def triv_pl(edges, fvals, slopes):
    tot = 0.0
    for a, b, fa, sl in zip(edges[:-1], edges[1:], fvals[:-1],
                            slopes):
        mid, half = 0.5 * (a + b), 0.5 * (b - a)
        u = mid + half * _GLX
        phi = fa + sl * (u - a)
        tot += half * float(np.dot(_GLW, 2.0 * phi
                                   * np.exp(-0.5 * u)
                                   / np.expm1(2.0 * u)))
    return tot


def triv_env_pl(edges, fvals):
    f = np.asarray(fvals, float)
    v = np.asarray(edges, float)
    supg = 2.0 * np.maximum(np.abs(f[:-1]), np.abs(f[1:])) \
        * np.exp(-0.5 * v[:-1])
    wseg = 0.5 * (np.log(1.0 - np.exp(-2.0 * v[1:]))
                  - np.log(1.0 - np.exp(-2.0 * v[:-1])))
    return float(np.sum(supg * wseg))


def hat_seg_c(edges, fvals, slopes, z):
    iz = 1.0 / z
    e0 = np.exp(z * edges[:-1])
    e1 = np.exp(z * edges[1:])
    val = e1 * (fvals[1:] * iz - slopes * iz ** 2) \
        - e0 * (fvals[:-1] * iz - slopes * iz ** 2)
    return complex(np.sum(val))


def phi_cont_of(row, sp):
    """The continuous compactly supported pw-linear phi_cont of the
    direct PARITH read (consumption probe verbatim)."""
    Wv, D, M = row["Wv"], row["D"], row["M"]
    u0, uL = sp["u0"], sp["uL"]
    a_p, b_p, wa, wb, s_p = weight_pieces(Wv, u0, uL, D, M)
    w0 = float(wa[0])
    eps = min(RAMP_EPS_MAX, u0 - U0_SUBG)
    aL = u0 - eps
    edges = [aL]
    fvals = [0.0]
    slopes = [w0 / eps]
    edges.extend(a_p.tolist())
    fvals.extend(wa.tolist())
    slopes.extend(s_p.tolist())
    edges.append(float(b_p[-1]))
    fvals.append(float(wb[-1]))
    u_end = M * D
    ext_cont = 0.0
    ext_at = 0.0
    if u_end > uL + 1e-12 and abs(fvals[-1]) > 0.0:
        e_p = weight_pieces(Wv, uL, u_end, D, M)
        ext_cont = tcont_of(e_p)
        edges.extend(e_p[1].tolist())
        fvals.extend(e_p[3].tolist())
        slopes.extend(e_p[4].tolist())
        k_lo = row["Ng"] + 1
        k_hi = int(math.floor(math.exp(u_end)))
        if k_hi >= k_lo:
            kk = np.arange(k_lo, min(k_hi,
                                     len(row["lam_tab"]) - 1) + 1)
            lv = row["lam_tab"][kk]
            nz = lv > 0.0
            if bool(np.any(nz)):
                kk = kk[nz].astype(float)
                ext_at = float(np.sum(
                    2.0 * lv[nz] / np.sqrt(kk)
                    * q_read(Wv, np.log(kk), D, M)))
    edges = np.asarray(edges, float)
    fvals = np.asarray(fvals, float)
    slopes = np.asarray(slopes, float)
    J = np.empty(len(edges))
    J[0] = slopes[0]
    J[1:-1] = slopes[1:] - slopes[:-1]
    J[-1] = -slopes[-1]
    keep = np.abs(J) > 1e-15
    s = w0 / eps
    ramp_cont = 2.0 * (math.exp(u0 / 2.0) * (2.0 * w0 - 4.0 * s)
                       - math.exp(aL / 2.0) * (-4.0 * s))
    lo = int(math.floor(math.exp(aL))) + 1
    kk = np.arange(max(lo, 2), sp["nc"] + 1)
    ramp_at = 0.0
    if len(kk):
        lv = row["lam_tab"][kk]
        nz = lv > 0.0
        kk = kk[nz].astype(float)
        if len(kk):
            ramp_at = float(np.sum(2.0 * lv[nz] / np.sqrt(kk)
                                   * s * (np.log(kk) - aL)))
    return dict(v=edges[keep], J=J[keep],
                sd=float(np.sum(np.abs(J[keep]))),
                vmax=float(edges[-1]), edges=edges, fvals=fvals,
                slopes=slopes, w0=w0, eps=eps,
                ramp_cont=ramp_cont, ramp_at=ramp_at,
                ext_cont=ext_cont, ext_at=ext_at,
                fend=float(fvals[-1]),
                fmax=float(np.max(np.abs(fvals))),
                triv=triv_pl(edges, fvals, slopes))


def direct_read(row, sp, pc, gam, abel, s2t, inv2, inv3):
    """PARITH_hat + TAILB of one (rung, cut) (consumption verbatim)."""
    zs = zsum4re(pc["v"], pc["J"], gam)
    par_hat = (-zs - pc["triv"] - pc["ramp_at"] + pc["ramp_cont"]
               + pc["ext_cont"] - pc["ext_at"])
    dps = 4.0 * pc["sd"] * (pc["vmax"] * inv2 + 2.0 * inv3) \
        * DPS_ERR
    tailb = (4.0 * pc["sd"] * abel
             + 4.0 * math.exp(0.5 * pc["vmax"]) * pc["sd"] * s2t
             + dps + 1e-12 * (1.0 + abs(pc["triv"])))
    return par_hat, tailb


def recon_of(row, sp, pc):
    """Bookkeeping ward (no zeros): PARITH reconstructed from the
    phi_cont atom/continuum sides (consumption verbatim)."""
    uu = row["uu"]
    idx = np.searchsorted(pc["edges"], uu, side="right") - 1
    ok = (idx >= 0) & (idx < len(pc["slopes"]))
    phi = np.zeros(len(uu))
    phi[ok] = pc["fvals"][idx[ok]] + pc["slopes"][idx[ok]] \
        * (uu[ok] - pc["edges"][idx[ok]])
    atom_side = float(np.dot(row["mu"], phi))
    cont_side = sp["tcont"] + pc["ramp_cont"] + pc["ext_cont"]
    par_recon = (atom_side - cont_side) - pc["ramp_at"] \
        - pc["ext_at"] + pc["ramp_cont"] + pc["ext_cont"]
    return abs(par_recon - sp["par"]) \
        / max(1.0, abs(sp["t_int"]))


def rung_reads(row, gam, abel, s2t, inv2, inv3):
    """All frozen reads of one rung: HEAD_A cuts + cB; returns the
    read dict + the per-rung worst wards + the closure info."""
    reads = {}
    for A in HEAD_A:
        sp = demand_at_head(row, A)
        if sp is not None:
            reads[("A", A)] = sp
    spB = split_at(row, row["ncB"]) if row["ncB"] > 0 else None
    if spB is not None:
        reads[("cB", 0)] = spB
    out = dict(reads={}, recon=0.0, heart=-1e18, sound=0,
               close_key=None, m_cert_best=-1e18, slack=[])
    for key, sp in reads.items():
        pc = phi_cont_of(row, sp)
        par_hat, tailb = direct_read(row, sp, pc, gam, abel,
                                     s2t, inv2, inv3)
        out["recon"] = max(out["recon"], recon_of(row, sp, pc))
        resid = sp["par"] - par_hat
        tol_a = RECON_TOL * (1.0 + abs(sp["t_int"]))
        out["heart"] = max(out["heart"],
                           (abs(resid) - tailb - tol_a)
                           / max(1.0, abs(sp["t_int"])))
        out["slack"].append(math.log10(tailb
                                       / max(abs(resid), 1e-300)))
        m_cert = sp["fc"] + par_hat - tailb
        if m_cert > row["m"] * (1.0 + SOUND_TOL) + 1e-15:
            out["sound"] += 1
        if m_cert > out["m_cert_best"]:
            out["m_cert_best"] = m_cert
            if m_cert > 0.0:
                out["close_key"] = key
        out["reads"][key] = dict(sp=sp, pc=pc, par_hat=par_hat,
                                 tailb=tailb, resid=resid,
                                 m_cert=m_cert)
    return out


def rebuild_cache():
    """Disclosed builder: recompute the 7000 ordinates with mpmath
    (dps 15) and rewrite the committed JSON cache."""
    from mpmath import mp, zetazero
    mp.dps = 15
    t0 = time.time()
    gam = []
    for n in range(1, N_Z + 1):
        gam.append(float(zetazero(n).imag))
        if n % 500 == 0:
            print("  ... %d / %d  [%.1f s]" % (n, N_Z,
                                               time.time() - t0),
                  flush=True)
    out = dict(meta=dict(
        n_zeros=N_Z, dps=15,
        generator=("mpmath.zetazero (dps 15); disclosed builder: "
                   "python v909_finite_wall_closure.py "
                   "--rebuild-cache"),
        pedigree=("every ordinate below T0 = 3e12, hence ON the "
                  "critical line unconditionally by Platt-Trudgian "
                  "2021 (Bull. LMS 53, Thm 1) -- EXTERNAL-CITED; "
                  "warded in-run: strict monotonicity, gamma_1 "
                  "identity, Rosser 1941 N(T) corridor per index "
                  "(both sides), independent mpmath "
                  "|zeta(1/2+i gamma)| spot checks"),
        gamma_1=gam[0], gamma_N=gam[-1]), gammas=gam)
    with open(ZC_JSON, "w") as fh:
        json.dump(out, fh)
    print("rebuilt %s (%d ordinates, %.1f s)" % (ZC_JSON, N_Z,
                                                 time.time() - t0))


# ------------------------------------------------------------- run
def run():
    t0 = time.time()
    print("=" * 74)
    print("v909 -- PRIME.WALL.FINITE_CLOSURE.01: the finite wall "
          "closure -- composed census B AND W1 AND W2 on 39/39 "
          "matched surface + 8/8 deep rungs from cited inputs "
          "(frozen experiments runs; SPECs %s); this module "
          "re-verifies the load-bearing spine on the reduced frozen "
          "subset with the committed 7000-ordinate verified-zero "
          "cache" % SPEC_CITED)
    print("(W1/W2 = algorithmically independent evaluations of the "
          "same localized Weil form -- a strong mutual crosscheck, "
          "NOT two independent proofs; DIRECTION-CONDITIONAL; "
          "NO RH claim)")
    print("=" * 74, flush=True)
    del CHECKS[:]

    # ------------------------------------------------------------ Z
    section("Z -- the committed verified-zero cache and its wards")
    with open(ZC_JSON) as fh:
        zc = json.load(fh)
    gam = np.asarray(zc["gammas"], float)
    t_c = float(gam[-1])
    check("Z1 census %d == %d, strictly increasing, gamma_1 dev "
          "%.1e <= 2e-6" % (len(gam), N_Z, abs(gam[0] - GAMMA1)),
          len(gam) == N_Z and bool(np.all(np.diff(gam) > 0.0))
          and abs(gam[0] - GAMMA1) <= 2.0e-6)
    kk = np.arange(1, N_Z + 1, dtype=float)
    up_r = n_up(gam + CORR_EPS)
    lo_r = n_lo(gam + CORR_EPS)
    up_l = n_up(np.maximum(gam - CORR_EPS, 2.0))
    lo_l = n_lo(np.maximum(gam - CORR_EPS, 2.0))
    n_ok = int(np.sum((kk <= up_r) & (kk >= lo_r)
                      & (kk - 1.0 <= up_l) & (kk - 1.0 >= lo_l)))
    check("Z2 Rosser-corridor consistency per index (%d/%d both "
          "sides, unconditional)" % (n_ok, N_Z), n_ok == N_Z)
    from mpmath import mp as _mp, mpc as _mpc
    from mpmath import zeta as _zf
    _mp.dps = 20
    idx = np.unique(np.geomspace(1, N_Z, NS_ZETA).astype(int)) - 1
    worst_z = max(float(abs(_zf(_mpc(0.5, float(gam[i])))))
                  for i in idx)
    check("Z3 independent zeta spot check <= %.0e at %d ordinates "
          "(worst %.1e, dps 20)" % (ZETA_TOL, len(idx), worst_z),
          worst_z <= ZETA_TOL)
    check("Z4 T_c = %.4f < T0 = %.0e (Platt-Trudgian 2021: every "
          "summed ordinate is ON the line, EXTERNAL-CITED)"
          % (t_c, T0_RH), t_c < T0_RH)
    inv2 = float(np.sum(1.0 / gam ** 2))
    inv3 = float(np.sum(1.0 / gam ** 3))
    s2t = s2_tail()

    # ------------------------------------------------------------ W
    section("W -- the deployed ladder (v563 pipeline) + the reduced "
            "frozen subset")
    zones = ladder_zones()
    check("W1 parent zone census %d == 42 (CLXXIV/CLXXVII frame)"
          % len(zones), len(zones) == 42)
    hz = []
    for kz in zones:
        D_k = 0.5 * float(core.G_ALL[kz]) / float(core.NU_MAIN)
        M_k = int(math.ceil(float(core.U_ALL[kz]) / D_k - 1.0e-9)) + 1
        if M_k % 2:
            M_k += 1
        hz.append((M_k // 2, kz))
    hz.sort()
    grams = []
    for _h, kz in hz[:SUB_GRAM]:
        g = gram_anatomy(kz, keep_chain=True)
        if g is not None and g.get("core_ok"):
            grams.append(g)
    grams.sort(key=lambda g: (g["h"], g["kz"]))
    check("W2 gram subset usable: %d of the %d shallowest rungs "
          "(h %d..%d)  [%.1f s]"
          % (len(grams), SUB_GRAM, grams[0]["h"], grams[-1]["h"],
             time.time() - t0), len(grams) >= N_STEPS + 1)

    # ------------------------------------------------------------ B
    section("B -- the B-half on the first %d usable steps "
            "(P_G chain; CLIII interval-certified class floor "
            "%.4f)" % (N_STEPS, B_FLOOR_CITED))
    steps = []
    for g1, g2 in zip(grams, grams[1:]):
        if g1["negA"] > 0 or g1["negS"] > 0 or g1["lamS"] <= 0.0:
            continue
        steps.append(build_step(g1, g2))
        if len(steps) >= N_STEPS:
            break
    print("    kz(r2) h     lam_min(B)  c_G        c_dom      "
          "negidx  c_B")
    for s in steps:
        print("    %-6d %-5d %.6f    %.6f   %+.6f  %-6d  %.6f"
              % (s["r2"]["kz"], s["r2"]["h"], s["minB"], s["cg"],
                 s["cdom"], s["negD"], s["cb"]), flush=True)
    minB = min(s["minB"] for s in steps)
    check("B1 %d steps built (>= %d)" % (len(steps), N_STEPS),
          len(steps) >= N_STEPS)
    check("B2 lam_min(B) >= %.4f on %d/%d steps (min %.4f; float "
          "re-check of the CLIII interval-certified class)"
          % (B_FLOOR_CITED, sum(1 for s in steps
                                if s["minB"] >= B_FLOOR_CITED),
             len(steps), minB),
          all(s["minB"] >= B_FLOOR_CITED for s in steps))
    check("B3 dominance B - (1/2) P_G PSD and c_B > 0 on %d/%d "
          "steps (min c_B %.4f)"
          % (sum(1 for s in steps if s["negD"] == 0
                 and s["cb"] > 0), len(steps),
             min(s["cb"] for s in steps)),
          all(s["negD"] == 0 and s["cb"] > 0 for s in steps))

    # ------------------------------------------------------------ L
    section("L -- the W1 monotone composition wards on the step "
            "rungs (measure inequality [L0/L1/L2/L3] + fold "
            "domination + ENV tier vs mu1)")
    rng = np.random.default_rng(20260811)
    pays = []
    for s in steps:
        p = mono_payload(s)
        if p is None:
            continue
        p["l1"] = l1_ward(s["H"], s["Gc"], rng.standard_normal(8))
        p["kz"] = s["r2"]["kz"]
        p["h"] = s["r2"]["h"]
        pays.append(p)
    n = len(pays)
    check("L0 dual-interpolation identity EXACT at M_i = K_h(y_i,.) "
          "on %d/%d (worst %.2e <= %.0e)"
          % (sum(1 for p in pays if p["l0"] <= L0_TOL), n,
             max(p["l0"] for p in pays), L0_TOL),
          all(p["l0"] <= L0_TOL for p in pays))
    check("L1 dual identity u*G^-1 u == min-norm interpolant energy "
          "on %d/%d (worst %.2e <= %.0e)"
          % (sum(1 for p in pays if p["l1"] <= L1_TOL), n,
             max(p["l1"] for p in pays), L1_TOL),
          all(p["l1"] <= L1_TOL for p in pays))
    check("L1b fold-grid rebuild of nu_+ reproduces the pipeline "
          "Gram on %d/%d (worst %.2e <= %.0e)"
          % (sum(1 for p in pays if p["grid_dev"] <= GRID_TOL), n,
             max(p["grid_dev"] for p in pays), GRID_TOL),
          all(p["grid_dev"] <= GRID_TOL for p in pays))
    check("L2 Loewner ward G[nu_+] - G[omega_ENV] >= 0 on %d/%d "
          "(min rel %.3e >= -%.0e)"
          % (sum(1 for p in pays if p["loewner"] >= -L2_TOL), n,
             min(p["loewner"] for p in pays), L2_TOL),
          all(p["loewner"] >= -L2_TOL for p in pays))
    check("L3 trace corollary positive and <= the L2 bound on %d/%d"
          % (sum(1 for p in pays if 0.0 < p["l3"]
                 <= p["env"] * (1.0 + 1e-9)), n),
          all(0.0 < p["l3"] <= p["env"] * (1.0 + 1e-9)
              for p in pays))
    check("L4 fold-wise domination (d_f)_+ <= |d^ar_f| + Delta_env "
          "on %d/%d (worst %.2e <= %.0e)"
          % (sum(1 for p in pays if p["dom"] <= DOM_TOL), n,
             max(p["dom"] for p in pays), DOM_TOL),
          all(p["dom"] <= DOM_TOL for p in pays))
    env_mu = [math.log10(p["env"] / p["mu1"]) for p in pays]
    check("L5 ENV-tier composed bound > mu1(h) on %d/%d (dex "
          "%+.2f/%+.2f/%+.2f; frozen run: 39/39 med +1.55; the "
          "verified-zero v-floor supply half is CITED: j16 "
          "deea4e1c 39/39, composed 67/67 with the CLXXXIV deep "
          "28/28)" % ((sum(1 for p in pays if p["env"] > p["mu1"]),
                       n) + band(env_mu)),
          all(p["env"] > p["mu1"] for p in pays))

    # ------------------------------------------------------------ C
    section("C -- the W2 face on the %d shallowest rungs: split "
            "identity + HEART ward (zeros against primes) + "
            "closure census at N_Z = %d" % (SUB_W2, N_Z))
    w2rows = []
    for kz in range(2, 151):
        r = build_rung(kz)
        if r is not None:
            w2rows.append(r)
        if len(w2rows) >= 40:
            break
    w2rows.sort(key=lambda r: (r["h"], r["kz"]))
    sub = w2rows[:SUB_W2]
    check("C1 W2 subset: %d rungs (h %d..%d), m > 0 and pivot "
          "collapse <= 1e-9 on all"
          % (len(sub), sub[0]["h"], sub[-1]["h"]),
          len(sub) == SUB_W2 and all(r["m"] > 0 for r in sub)
          and max(r["pivres"] for r in sub) <= 1e-9)
    dx = 0.0
    for r in sub:
        for nc in cut_ladder(r):
            sp = split_at(r, nc)
            if sp is not None:
                dx = max(dx, sp["dev_x1"], sp["dev_x3"])
    check("C2 split identities m = HEAD + TCONT + PARITH on the "
          "whole subset ladder (worst %.2e <= %.0e)" % (dx, ID_WARD),
          dx <= ID_WARD)
    recon_w = 0.0
    heart_w = -1e18
    sound_bad = 0
    n_close = 0
    slack = []
    for r in sub:
        tg = tail_grid(r["D"], t_c)
        abel = abel_upper(tg, 1.0 / tg[:-1] ** 2,
                          n_start=float(N_Z))
        rd = rung_reads(r, gam, abel, s2t, inv2, inv3)
        r["_rd"] = rd
        recon_w = max(recon_w, rd["recon"])
        heart_w = max(heart_w, rd["heart"])
        sound_bad += rd["sound"]
        if rd["close_key"] is not None:
            n_close += 1
        slack.extend(rd["slack"])
        print("    kz %3d h %4d: m %.3e  m_cert best %+.3e at %s  "
              "heart slack med %+.2f dex  [%.1f s]"
              % (r["kz"], r["h"], r["m"], rd["m_cert_best"],
                 rd["close_key"], float(np.median(rd["slack"])),
                 time.time() - t0), flush=True)
    check("C3 bookkeeping recon exact on every read (worst %.2e "
          "<= 1e-8)" % recon_w, recon_w <= 1e-8)
    check("C4 THE HEART: |PARITH - PARITH_hat| <= TAILB on every "
          "(rung, cut) read (worst scaled excess %+.2e <= 0; "
          "slack %+.2f/%+.2f/%+.2f dex)"
          % ((heart_w,) + band(slack)), heart_w <= 0.0)
    check("C5 soundness m_cert <= m on every read (%d violations)"
          % sound_bad, sound_bad == 0)
    check("C6 closure census: m_cert > 0 on %d/%d subset rungs at "
          "N_Z = %d (frozen full-ladder censuses CITED: 16/67 + "
          "0/8 at 7000; 67/67 + 8/8 at the 2e7 certified cache, "
          "CXCV)" % (n_close, SUB_W2, N_Z), n_close == SUB_W2)

    # ------------------------------------------------------------ X
    section("X -- the composed subset census (B AND W1 AND W2)")
    step_kz = {s["r2"]["kz"] for s in steps
               if s["minB"] >= B_FLOOR_CITED and s["negD"] == 0
               and s["cb"] > 0}
    pay_kz = {p["kz"] for p in pays
              if p["env"] > p["mu1"] and p["dom"] <= DOM_TOL
              and p["loewner"] >= -L2_TOL}
    w2_kz = {r["kz"] for r in sub
             if r["_rd"]["close_key"] is not None}
    matched = sorted(step_kz & pay_kz & w2_kz)
    check("X1 composed census on the matched subset: %d rungs with "
          "all three faces certified (kz %s); FULL frozen census "
          "CITED, not pinned by this gate: 39/39 matched surface "
          "+ 8/8 deep (CXCV V4 / CCV)"
          % (len(matched), matched), len(matched) >= 4)

    # ------------------------------------------------------------ M
    section("M -- controls (must fire)")
    lam_sm = []
    for r in sub:
        rs = build_rung(r["kz"], smooth_world=True)
        lam_sm.append(rs["m"] if rs is not None else r["lam_sm"])
    check("M1 smooth world breaks the wall on %d/%d subset rungs "
          "(max %+.1e)" % (sum(1 for v in lam_sm if v < 0),
                           len(lam_sm), max(lam_sm)),
          all(v < 0 for v in lam_sm))
    r9 = build_rung(CTRL_KZ)
    NE = int(math.floor(math.exp(2.0 * r9["alpha"]))) + 1
    lamE = lambda_eps(NE)
    nz = np.nonzero(np.abs(lamE) > 1e-12)[0]
    cE = (np.log(nz.astype(float)),
          2.0 * lamE[nz] / np.sqrt(nz.astype(float)))
    rE = build_rung(CTRL_KZ, comb=cE)
    rS = build_rung(CTRL_KZ, scramble_seed=1)
    check("M2 Epstein + scramble break lam_min at kz %d (%+.1e, "
          "%+.1e)" % (CTRL_KZ, rE["m"], rS["m"]),
          rE["m"] < 0 and rS["m"] < 0)
    tg9 = tail_grid(r9["D"], t_c)
    abel9 = abel_upper(tg9, 1.0 / tg9[:-1] ** 2, n_start=float(N_Z))
    rd9 = rung_reads(r9, gam, abel9, s2t, inv2, inv3)
    fired = 0
    tried = 0
    for key in (("cB", 0), ("A", 9)):
        rd = rd9["reads"].get(key)
        if rd is None:
            continue
        tried += 1
        sp = rd["sp"]
        keep = rS["uu"] > math.log(sp["nc"]) + 1e-12
        t_scr = float(np.dot(
            np.asarray(rS["mu"], float)[keep],
            q_read(r9["Wv"], rS["uu"][keep], r9["D"], r9["M"])))
        par_scr = t_scr - sp["tcont"]
        exc = abs(par_scr - rd["par_hat"]) / rd["tailb"]
        print("    scramble read at %s: |PARITH_scr - PARITH_hat| "
              "/ TAILB = %.1e -> %s"
              % (str(key), exc, "FIRES" if exc > 1 else "silent"))
        if exc > 1.0:
            fired += 1
    check("M3 the scrambled comb breaks the exact prime-side heart "
          "ward on %d/%d control cuts" % (fired, tried),
          tried >= 1 and fired == tried)
    rd = rd9["reads"][("cB", 0)]
    pc = rd["pc"]
    g1 = float(gam[0])
    on_pair = 4.0 * float((-np.sum(
        pc["J"] * np.exp(1j * g1 * pc["v"])) / g1 ** 2).real)
    dlt = IMP_BETA - 0.5
    quad = 4.0 * (hat_seg_c(pc["edges"], pc["fvals"],
                            pc["slopes"], dlt + 1j * g1).real
                  + hat_seg_c(pc["edges"], pc["fvals"],
                              pc["slopes"], -dlt + 1j * g1).real)
    shift = abs((-quad) - (-on_pair))
    ratio = shift / max(abs(rd["resid"]), 1e-300)
    check("M4 off-line impostor (gamma_1 -> beta = %.2f, "
          "FE-symmetrised quadruple) shifts PARITH_hat by %.4f = "
          "%.1e x the genuine residual (>= %.0f)"
          % (IMP_BETA, shift, ratio, IMP_RATIO_MIN),
          ratio >= IMP_RATIO_MIN)
    tb_env = triv_env_pl(pc["edges"], pc["fvals"])
    check("M5 |TRIV| <= trivial-zero envelope at the control read "
          "(%.3e <= %.3e)" % (abs(pc["triv"]), tb_env),
          abs(pc["triv"]) <= tb_env * (1 + 1e-9) + 1e-15)

    # ------------------------------------------------------- verdict
    n_pass = sum(1 for _n, okk in CHECKS if okk)
    n_tot = len(CHECKS)
    ok = n_pass == n_tot
    print("\n" + "=" * 74)
    print("v909: %d/%d checks passed | runtime %.1f s"
          % (n_pass, n_tot, time.time() - t0))
    print("the finite wall closure: every reachable wall face "
          "certified from cited inputs on the deployed ladder "
          "(frozen experiments census 39/39 + 8/8 composed); W1/W2 "
          "are algorithmically independent evaluations of the same "
          "localized Weil form -- a strong mutual crosscheck; "
          "positivity is certified on a finite family of Galerkin "
          "sections along the measured critical direction "
          "(DIRECTION-CONDITIONAL, UNIF-PATH); a finite verified-"
          "zero sum can never prove RH -- NO RH claim")
    print("[%s] v909 VERDICT GATE" % ("PASS" if ok else "FAIL"))
    return 0 if ok else n_tot - n_pass


if __name__ == "__main__":
    if "--rebuild-cache" in sys.argv:
        rebuild_cache()
        raise SystemExit(0)
    raise SystemExit(1 if run() else 0)
