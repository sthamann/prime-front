#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""tau_mobius_factor_probe -- PRIME.PORT.TAU.MOEBIUS.01
(EXPLORATION ONLY, experiments/; round 48, reviewer probe 5 --
THE KEY RUN: does the tau quotient factor through the Moebius/
transfer step as tau_{h+1}/tau_h = F(step data) with F > 0
following ALGEBRAICALLY from a contractivity condition?
2026-08-09.)

THE QUESTION (frozen): port_schur_cocycle_probe warded the exact
quotient identity det(W_{h+1})/det(W_h) = det(I + W_h^{-1} Delta C)
on the 12x12 window W = I - C_J, but the naive low-rank alpha
reduction FAILS because W is near-singular at the soft mode -- the
sv tail of the increment is determinant-relevant.  The reviewer's
target shape: tau_{h+1} = q_h (1 - |alpha_h|^2) tau_h with q_h > 0
source-positive, or any equivalent positive factorization where
sign(tau_{h+1}) = sign(tau_h) follows from the step algebra.
Without such an identity there is no positivity inheritance.

THE LADDER (frozen, port_schur_cocycle verbatim): all frame-A
zones (core.frame_a_zones()) with h <= 900, sorted by (h, kz);
consecutive rung pairs.  T1/T2 run on FULL-WINDOW pairs (both
rungs carry all 12 indices of J = {2, 4, ..., 24}; typed skips
counted); the fitted-step reproduction (T3/T4) runs on pairs with
>= 8 common port alias indices.

FROZEN PROTOCOL (2026-08-09; all bars frozen before the run):

 T1  THE EXACT FACTORIZATION LEDGER: per full-window step compute
     the exact quotient Q_h = det(W_{h+1})/det(W_h) (slogdet) and
     decompose it EXACTLY along the eigen structure:
       Q_h = prod_i (1 + mu_i),
       mu_i = eigenvalues of W_h^{-1} Delta C,
       Delta C = C_J(h) - C_J(h+1)  (so W_{h+1} = W_h + Delta C).
     On truth W_h is PD (minors-positive, re-warded), so the mu_i
     are computed EXACTLY REAL via the symmetric similarity
     W^{-1/2} Delta C W^{-1/2} (eigh); WARD (kill -> WARD-BROKEN):
     |prod(1 + mu_i) - Q_h| <= 1e-10 relative on every step.
     THE MU-SPECTRUM ANATOMY per step: number of factors with
     mu_i < -1 (negative factor = sign flip), number with
     |1 + mu_i| < 0.1 (near-crossing, frozen NEAR_BAR), the census
     min_i (1 + mu_i), and the soft-mode projection: the soft mode
     s_h = eigenvector of W_h at its SMALLEST eigenvalue (= top
     eigenvector of C_J); per eigenvalue mu_i the overlap
     |<v_i, s_h>| of its (W^{-1/2}-transported, normalized)
     eigenvector; reported for the dangerous factor
     (argmin |1 + mu_i|) -- is the dangerous direction always the
     soft mode?  MEASURED FACT to establish: Q_h > 0 on every
     truth step (tau never flips; census reported, not killed --
     a flip would be a discovery, not a breakage).

 T2  THE ONE-DANGEROUS-FACTOR REDUCTION (the candidate bridge):
     typed test -- define mu_soft = the eigenvalue whose
     eigenvector has the LARGEST soft-mode overlap (frozen
     selector).  Q_h = (bulk product over i != soft) x
     (1 + mu_soft) holds exactly by T1; the BRIDGE question is
     whether the bulk is uniformly harmless: typed BRIDGE-SCALAR
     iff min over the ladder of min_{i != soft} (1 + mu_i) >=
     BULK_MARGIN = 0.5 (then sign(Q_h) = sign(1 + mu_soft) and
     the determinant bridge reduces to ONE scalar per step);
     BRIDGE-DIFFUSE otherwise.  Reported: the mu_soft ladder, its
     sign census, its size law (corr(log|mu_soft|, log tau_h) and
     corr(log|mu_soft|, log ||Delta C||_F)), the census of
     soft == dangerous coincidences, and -- if BRIDGE-SCALAR --
     the new contract candidate stated plainly: the induction
     demand becomes the SINGLE explicit inequality
     1 + mu_soft(h) > 0 for all h.

 T3  THE CONTRACTION LINK (the reviewer's demanded coupling):
     reproduce the fitted per-step Moebius maps of
     port_schur_cocycle S2 (machinery verbatim; REPRODUCTION WARD
     kill -> WARD-BROKEN: 41 steps, per-step residual table match
     within the print rounding 5.001e-5, |alpha| < 1 on 100% --
     moebius_source_step_probe precedent).  On steps that are BOTH
     full-window AND fitted, compute (fit NOTHING new):
       J_h := (1 + mu_soft) / (1 - |alpha_h|^2)
     and examine: (a) J_h > 0 on all steps; (b) lawful vs h: the
     sign of (J_h - 1) constant on >= 0.90 of steps; (c) source-
     interpretable: corr(log|J_h - 1|, log ||Delta C||_F) >= 0.8.
     TYPED: LINK-LAWFUL iff (a)+(b)+(c); LINK-POSITIVE iff (a)
     only; LINK-OPEN otherwise (honest -- if J_h is wild the link
     is not this simple).  KNOWN CONTEXT, declared: round 46
     measured the fitted steps INSIDE the identity noise
     (CARRIER-INVARIANT, |alpha_h| ~ 0.002), so 1 - |alpha_h|^2 =
     1 - O(1e-5) and J_h ~ 1 + mu_soft is the expected outcome;
     the probe measures whether the Moebius datum carries ANY of
     the determinant load, and reports plainly if it does not.

 T4  J-CONTRACTIVITY IN THE CANONICAL GAUGE (report only): frozen
     det-normalized convention (own; coordinated with, but not
     dependent on, the parallel iiks_gauge_firewall_probe): the
     step transfer A_h = T_h / |det T_h|^{1/2} from the fitted
     anchored map T_h (three-anchor (0,1,inf) gauge), Cayley disk
     conjugation U_h = K A_h K^{-1}, K = [[1, -i], [1, i]];
     compute the eigenvalues of J - U_h^* J U_h with J =
     diag(1, -1); census of J-contractive steps (min eig >=
     -1e-9 ||U||_F^2) on truth AND on the SMOOTH-MASS world.
     ALGEBRA, declared up front: a real A_h with det = +1 gives
     U_h in SU(1,1), i.e. an EXACT J-isometry -- the census
     therefore separates orientation (det sign) and quantifies
     the numerical deviation; contractivity in this gauge lives
     in the Cayley datum |alpha_h| < 1, not in the matrix
     quadratic form, and the probe says so plainly.

 C   CONTROLS: (C1, kz 9, must fire, kill -> CONTROL-DEAD)
     Epstein (lambda_eps recursion comb) + scramble (seed 1): the
     compressed frame must die (I - E_out indefinite OR
     lam(C_J) > 1 OR window unavailable); channel reported.
     (C2, the arithmetic detector, kill -> CONTROL-DEAD if
     silent) THE SMOOTH-MASS WORLD: the full ladder rebuilt with
     the actual atom positions u_n carrying the SMOOTH masses
     m_n = 2 e^{u_n/2} du_n (midpoint cells; lattice_parametrix
     B1 LATTICE-SMOOTH verbatim -- the FLUCTUATIONS-REQUIRED
     world whose floor is violated).  Its Q_h ladder MUST show
     the violation: typed SMOOTH-FLIP-DETECTED iff some smooth
     rung has det(W) <= 0 or min eig(W) < 0, or some smooth step
     has Q_h < 0 or a real factor 1 + mu < 0 (first crossing
     LOCATED and printed); SMOOTH-FRAME-DIES iff the smooth frame
     itself dies (exterior supercritical / window unavailable /
     chain death -- detection via frame, reported against the
     'frame survives' premise); SMOOTH-UNDETECTED (control
     silent) -> CONTROL-DEAD.  The smooth factor anatomy uses the
     general (complex-capable) eigensolver since W need not stay
     PD there; its factorization ward is 1e-8 (reported).

 W   PIPELINE WARDS (kill -> PIPELINE-BROKEN): W1 >= 30 truth
     rungs; W2 [Y, D_P] rank 2 on every truth rung (s3/s1 <=
     1e-10); W3 >= 20 full-window T1 pairs AND det(W_h) > 0 on
     every truth full-window rung; W4 >= 30 fitted steps.

KILLS: K1 pipeline ward breaks -> PIPELINE-BROKEN; KW the T1
factorization ward or the T3 reproduction ward breaks ->
WARD-BROKEN; K3 controls silent (C1 or C2) -> CONTROL-DEAD.

VERDICT (frozen enum): TAUMOEBIUS-MEASURED with typed sublabels
BRIDGE-SCALAR / BRIDGE-DIFFUSE (T2), LINK-LAWFUL / LINK-POSITIVE
/ LINK-OPEN (T3), and SMOOTH-FLIP-DETECTED / SMOOTH-FRAME-DIES
(C2); else PIPELINE-BROKEN / WARD-BROKEN / CONTROL-DEAD.

SPEC v1 BOOKKEEPING NOTE (documented before the first run;
physics verbatim): core.build_window(kz) is called ONCE per zone
and its output dict is passed to both the truth rung and the
smooth-mass rung (the comb substitution happens after the build
exactly as in the predecessors); this is bookkeeping only -- the
per-world lag assembly, fold, chain and compressions are the
predecessor code paths bit for bit.

SPEC v2 (2026-08-09, after run 1; fail-first preserved -- run 1
passed S0/W/T1-T4/C1 and crashed on a SHAPE slip in the C2
bookkeeping BEFORE any C2 typing: smooth-mass rungs may carry a
PARTIAL window (>= 8 but < 12 of the J indices; the truth ladder
always carries all 12), and the per-rung wall diagnostic sized
W = I - C_J by the full 12.  v2 sizes W by the available window
(mechanical), reports the partial-window count, and restricts the
per-rung wall census to the available indices.  Every T1-T4
number of run 1 is unchanged by construction (the truth-side code
path is untouched).

NO RH claim -- an exact factorization of window-determinant
quotients on compressed truncations is a numerical measurement,
not a theorem about zeros.

FIREWALL: no zeros, no prime oracles (AST scan; banned ids
zetazero / nzeros / primerange / isprime / primepi / nextprime /
prevprime); v563 READ-ONLY; RNG only inside the declared scramble
control; stdout only.  No marker moves.

Sources (read-only): v563_paper2_readouts; window compression +
exact quotient identity + fitted-step machinery verbatim from
port_schur_cocycle_probe.py (PRIME.PORT.SCHURSTEP.01) via
moebius_source_step_probe.py (PRIME.PORT.MOEBIUS.SOURCE.01,
reproduction table); smooth-mass world verbatim from
lattice_parametrix_probe.py (PRIME.PORT.LATTICE.PARAMETRIX.01,
B1); port_kyp_storage_probe.py (KYP storage: wall-blind,
context).  IIKS = Its-Izergin-Korepin-Slavnov.

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/tau_mobius_factor_probe.py
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

H_DEEP_MAX = 900
JWIN = tuple(range(2, 25, 2))
HEAVY = (9, 12, 13, 26, 40)
MIN_RUNGS = 30
MIN_PAIRS_T1 = 20
MIN_PAIRS_FIT = 30
MIN_COMMON_J = 8
RANK_BAR = 1e-10
FACT_WARD = 1e-10           # T1 truth factorization ward (kill)
FACT_WARD_SMOOTH = 1e-8     # C2 smooth factorization ward (report)
NEAR_BAR = 0.1              # |1 + mu| < NEAR_BAR = near-crossing
BULK_MARGIN = 0.5           # T2 BRIDGE-SCALAR bar
LINK_SIGN_FRAC = 0.90       # T3 (b)
LINK_CORR_BAR = 0.8         # T3 (c)
JCON_TOL = 1e-9             # T4 relative tolerance
REF_SEP_MIN = 1e-6
CTRL_KZ = 9
BANNED_IDS = ("zetazero", "nzeros", "primerange", "isprime",
              "primepi", "nextprime", "prevprime")

# T3 reproduction ward: the predecessor's printed per-step residual
# table (41 steps, print precision 1e-4) and headline stats
# (moebius_source_step_probe precedent, verbatim).
REF_RES = (0.0011, 0.0024, 0.0150, 0.0035, 0.0097, 0.0102, 0.0015,
           0.0028, 0.0022, 0.0012, 0.0008, 0.0007, 0.0011, 0.0016,
           0.0006, 0.0005, 0.0003, 0.0001, 0.0013, 0.0005, 0.0002,
           0.0036, 0.0122, 0.0010, 0.0002, 0.0001, 0.0012, 0.0005,
           0.0017, 0.0032, 0.0019, 0.0005, 0.0077, 0.0015, 0.0024,
           0.0215, 0.0118, 0.0063, 0.0011, 0.0043, 0.0005)
REF_N_STEPS = 41
REF_MED_RES = 0.0015
ROUND_TOL = 5.001e-5

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


# --------- pipeline, verbatim from port_schur_cocycle_probe
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


def build_rung(kz, scramble_seed=None, comb=None, rr_cache=None):
    rr = (rr_cache if rr_cache is not None
          else core.build_window(kz, scramble_seed=scramble_seed))
    h, M, D, alpha = rr["h"], rr["M"], rr["D"], rr["alpha"]
    uu = np.asarray(rr["uu"], float)
    mm = 2.0 * np.asarray(rr["lam"], float)
    if comb is not None:
        uu, mm = comb
    c_at, _ = core.atom_lags_at(alpha, M, uu, mm)
    c_ar = np.asarray(core.arch_lags(M, D), float)
    d = grid_density(c_ar + c_at)
    return dict(d=d, L=2 * M - 2, D=D, alpha=alpha, h=h)


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


def antisym_generators(C):
    """Canonical (f, g) with C = f g^T - g f^T (SPEC v2 extraction,
    verbatim)."""
    U, sv, _Vh = np.linalg.svd(C)
    s1 = sv[0]
    f = math.sqrt(s1) * U[:, 0]
    g = math.sqrt(s1) * U[:, 1]
    Ct = np.outer(f, g) - np.outer(g, f)
    if np.linalg.norm(Ct + C) < np.linalg.norm(Ct - C):
        g = -g
    return f, g, sv


def gauge_fix(f, g, jp):
    """FROZEN GAUGE (lax2 verbatim; the anchored normalization
    quotients it out exactly)."""
    m0 = int(np.argmin(jp))
    r = math.hypot(f[m0], g[m0])
    c, s = f[m0] / r, g[m0] / r
    return c * f + s * g, -s * f + c * g


def rung_all(kz, scramble_seed=None, comb=None, rr_cache=None):
    """One heavy build per rung (port_schur_cocycle verbatim): the
    negative-arm Gram E feeds BOTH the 12-index window compression
    and the dressed-port IIKS generators."""
    b = build_rung(kz, scramble_seed=scramble_seed, comb=comb,
                   rr_cache=rr_cache)
    h, L, D = b["h"], b["L"], b["D"]
    if h > H_DEEP_MAX:
        return "TOO-DEEP"
    xs, ws, _ = folded_measure(b["d"], L, +1.0)
    ys, vs, uf_n = folded_measure(b["d"], L, -1.0)
    al, be, m0, steps = lanczos_chain(xs, ws, h + 1)
    if steps < h + 1 or np.any(be <= 0):
        return None
    Pn = eval_chain(al, be, m0, ys, h)
    E = np.sqrt(vs)[:, None] * (Pn @ Pn.T) * np.sqrt(vs)[None, :]
    E = 0.5 * (E + E.T)
    out = dict(kz=kz, h=h, alpha=b["alpha"],
               lamE=float(np.linalg.eigvalsh(E)[-1]))
    # ---- window compression (port_cocycle_window verbatim)
    idx = {int(j): k for k, j in enumerate(uf_n)}
    jav = [j for j in JWIN if j in idx]
    out["full"] = (len(jav) == len(JWIN))
    if len(jav) >= MIN_COMMON_J:
        iw = [idx[j] for j in jav]
        io = [k for k in range(E.shape[0]) if k not in set(iw)]
        Eo = E[np.ix_(io, io)]
        IO = np.eye(len(io)) - Eo
        CJ = (E[np.ix_(iw, iw)]
              + E[np.ix_(iw, io)] @ np.linalg.solve(
                  IO, E[np.ix_(io, iw)]))
        CJ = 0.5 * (CJ + CJ.T)
        out["CJ"] = CJ
        out["jav"] = jav
        out["lamO"] = float(np.linalg.eigvalsh(Eo)[-1])
        out["lamC"] = float(np.linalg.eigvalsh(CJ)[-1])
    # ---- dressed port + IIKS generators (lax2 verbatim)
    tau_m = (2.0 * math.pi * uf_n / L) / D
    port = tau_m <= float(np.max(tau_m)) / 10.0
    ip, ib = np.where(port)[0], np.where(~port)[0]
    if len(ip) >= 4 and len(ib) >= 1:
        P = E[np.ix_(ip, ip)]
        X = E[np.ix_(ip, ib)]
        R = E[np.ix_(ib, ib)]
        IR = np.eye(len(ib)) - R
        DP = P + X @ np.linalg.solve(IR, X.T)
        DP = 0.5 * (DP + DP.T)
        Y = np.diag(ys[ip])
        C = Y @ DP - DP @ Y
        f, g, sv = antisym_generators(C)
        f, g = gauge_fix(f, g, uf_n[ip])
        out["f"], out["g"] = f, g
        out["jp"], out["yp"] = uf_n[ip], ys[ip]
        out["rk"] = float(sv[2] / sv[0]) if len(sv) > 2 else 0.0
    return out


# ------------------------------------------- homogeneous RP^1 machinery
def unit_pairs(g, f):
    P = np.stack([np.asarray(g, float), np.asarray(f, float)],
                 axis=1)
    return P / np.linalg.norm(P, axis=1)[:, None]


def chordal(P, Q):
    """Chordal distance on RP^1 between unit pair rows."""
    return np.abs(P[:, 0] * Q[:, 1] - P[:, 1] * Q[:, 0])


def norm_map(p0, p1, p2):
    """The unique PSL(2, R) map sending p0 -> 0, p1 -> 1,
    p2 -> infinity (homogeneous); None if degenerate (verbatim)."""
    M = np.stack([p2, p0], axis=1)
    if abs(float(np.linalg.det(M))) < 1e-12:
        return None
    T0 = np.linalg.inv(M)
    s, t = T0 @ p1
    if abs(s) < 1e-10 or abs(t) < 1e-10:
        return None
    return np.diag([1.0 / s, 1.0 / t]) @ T0


def apply_hom(T, P):
    Q = (T @ P.T).T
    n = np.linalg.norm(Q, axis=1)
    n[n < 1e-300] = 1.0
    return Q / n[:, None]


def moebius_fit(P, Q):
    """TLS Moebius fit (verbatim)."""
    rows = np.stack([P[:, 0] * Q[:, 1], P[:, 1] * Q[:, 1],
                     -P[:, 0] * Q[:, 0], -P[:, 1] * Q[:, 0]],
                    axis=1)
    _u, _s, Vh = np.linalg.svd(rows)
    a, b, c, d = Vh[-1]
    T = np.array([[a, b], [c, d]])
    return T, chordal(apply_hom(T, P), Q)


def cayley_alpha(T):
    den = T[1, 0] * 1j + T[1, 1]
    if abs(den) < 1e-300:
        return float("inf")
    z = (T[0, 0] * 1j + T[0, 1]) / den
    return abs((z - 1j) / (z + 1j))


def quart(v):
    q = np.percentile(np.asarray(v, float), [25, 50, 75])
    return "q25 %.4f  med %.4f  q75 %.4f" % tuple(q)


def eps_comb(kz):
    rr = core.build_window(kz)
    N_E = int(math.floor(math.exp(2.0 * rr["alpha"]))) + 1
    lamE_ = lambda_eps(N_E)
    nn = np.nonzero(np.abs(lamE_) > 1e-12)[0]
    return (np.log(nn.astype(float)),
            2.0 * lamE_[nn] / np.sqrt(nn.astype(float)))


# ------------------------------------------- smooth-mass world (B1)
def cell_widths(uu):
    """Midpoint cell widths (lattice_parametrix verbatim)."""
    du = np.zeros(len(uu))
    du[1:-1] = 0.5 * (uu[2:] - uu[:-2])
    du[0] = uu[1] - uu[0]
    du[-1] = uu[-1] - uu[-2]
    return du


def smooth_masses(uu):
    """B1 LATTICE-SMOOTH masses m_n = 2 e^{u_n/2} du_n (verbatim)."""
    return 2.0 * np.exp(np.asarray(uu, float) / 2.0) \
        * cell_widths(np.asarray(uu, float))


# ------------------------------------------- factorization machinery
def logdet_sgn(W):
    sgn, ld = np.linalg.slogdet(W)
    return float(sgn), float(ld)


def factor_step_pd(Wa, DC):
    """Truth branch: Wa symmetric PD.  Exact real mu spectrum of
    Wa^{-1} DC via the symmetric similarity, plus transported
    normalized eigenvectors and the soft mode of Wa."""
    ew, Vw = np.linalg.eigh(Wa)
    if ew[0] <= 0.0:
        return None
    Wisq = Vw @ np.diag(ew ** -0.5) @ Vw.T
    Msym = Wisq @ DC @ Wisq
    mu, Us = np.linalg.eigh(0.5 * (Msym + Msym.T))
    vecs = Wisq @ Us
    vecs = vecs / np.linalg.norm(vecs, axis=0)[None, :]
    soft = Vw[:, 0]
    return dict(mu=mu, vecs=vecs, soft=soft, tau=float(ew[0]))


def factor_step_general(Wa, DC):
    """Smooth-world branch: W need not be PD; general (complex-
    capable) eigen decomposition of Wa^{-1} DC."""
    try:
        M = np.linalg.solve(Wa, DC)
    except np.linalg.LinAlgError:
        return None
    mu, V = np.linalg.eig(M)
    ews, Vw = np.linalg.eigh(0.5 * (Wa + Wa.T))
    isoft = int(np.argmin(ews))
    return dict(mu=mu, vecs=V, soft=Vw[:, isoft],
                tau=float(ews[isoft]))


def corr_or_nan(x, y):
    x = np.asarray(x, float)
    y = np.asarray(y, float)
    m = np.isfinite(x) & np.isfinite(y)
    if int(np.sum(m)) < 3 or np.std(x[m]) == 0 or np.std(y[m]) == 0:
        return float("nan")
    return float(np.corrcoef(x[m], y[m])[0, 1])


K_HD = np.array([[1.0, -1j], [1.0, 1j]], dtype=complex)   # H -> D
K_DH = np.linalg.inv(K_HD)
J2 = np.diag([1.0, -1.0]).astype(complex)


def j_contract_eigs(T):
    """T4: det-normalized disk conjugation; eigenvalues of
    J - U^* J U (2, ascending) plus det sign and ||U||_F^2."""
    dt = float(np.linalg.det(T))
    if abs(dt) < 1e-300:
        return None
    A = T / math.sqrt(abs(dt))
    U = K_HD @ A.astype(complex) @ K_DH
    Mj = J2 - U.conj().T @ J2 @ U
    ev = np.linalg.eigvalsh(0.5 * (Mj + Mj.conj().T))
    return dict(ev=ev, sgn=(1.0 if dt > 0 else -1.0),
                n2=float(np.linalg.norm(U) ** 2))


def fit_steps(rungs):
    """The port_schur_cocycle S2 fitted steps (verbatim), indexed by
    the consecutive-pair position k.  Returns (steps, skips)."""
    steps = []
    n_skip_j = n_skip_ref = 0
    for k, (ra, rb) in enumerate(zip(rungs[:-1], rungs[1:])):
        com, ia, ib = np.intersect1d(ra.get("jp", []),
                                     rb.get("jp", []),
                                     return_indices=True)
        if len(com) < MIN_COMMON_J:
            n_skip_j += 1
            continue
        Pa = unit_pairs(ra["g"][ia], ra["f"][ia])
        Pb = unit_pairs(rb["g"][ib], rb["f"][ib])
        order = np.argsort(com)
        i0, i1, i2 = order[0], order[1], order[2]
        seps = [chordal(Pa[[u]], Pa[[v]])[0]
                for u, v in ((i0, i1), (i0, i2), (i1, i2))] \
            + [chordal(Pb[[u]], Pb[[v]])[0]
               for u, v in ((i0, i1), (i0, i2), (i1, i2))]
        Ta = norm_map(Pa[i0], Pa[i1], Pa[i2])
        Tb = norm_map(Pb[i0], Pb[i1], Pb[i2])
        if min(seps) <= REF_SEP_MIN or Ta is None or Tb is None:
            n_skip_ref += 1
            continue
        Na, Nb = apply_hom(Ta, Pa), apply_hom(Tb, Pb)
        T, res = moebius_fit(Na, Nb)
        keep = np.ones(len(com), dtype=bool)
        keep[[i0, i1, i2]] = False
        steps.append(dict(k=k, ra=ra, rb=rb, T=T,
                          res=float(np.median(res[keep])),
                          alpha=cayley_alpha(T)))
    return steps, n_skip_j, n_skip_ref


def factor_pairs(rungs, general=False):
    """T1 ledger rows on the full-window consecutive pairs of a
    rung list.  Truth: PD branch (real mu); general=True: smooth
    branch."""
    rows = []
    n_skip = 0
    for k, (ra, rb) in enumerate(zip(rungs[:-1], rungs[1:])):
        if not (ra.get("full") and rb.get("full")):
            n_skip += 1
            continue
        n = len(JWIN)
        Wa = np.eye(n) - ra["CJ"]
        Wb = np.eye(n) - rb["CJ"]
        sga, lda = logdet_sgn(Wa)
        sgb, ldb = logdet_sgn(Wb)
        Q = sga * sgb * math.exp(ldb - lda)
        DC = ra["CJ"] - rb["CJ"]         # W_b = W_a + DC
        fs = (factor_step_general(Wa, DC) if general
              else factor_step_pd(Wa, DC))
        if fs is None:
            fs = factor_step_general(Wa, DC)
            if fs is None:
                n_skip += 1
                continue
            fs["forced_general"] = True
        mu = fs["mu"]
        prod = complex(np.prod(1.0 + mu.astype(complex)))
        dev = abs(prod - Q) / max(abs(Q), 1e-300)
        real_m = np.abs(np.imag(mu.astype(complex))) \
            <= 1e-9 * (1.0 + np.abs(mu))
        mur = np.real(mu.astype(complex))
        fac_r = 1.0 + mur[real_m]
        ovl = np.abs(np.real(
            fs["vecs"].astype(complex)).T @ fs["soft"])
        nv = np.linalg.norm(np.real(fs["vecs"].astype(complex)),
                            axis=0)
        ovl = ovl / np.maximum(nv, 1e-300)
        i_soft = int(np.argmax(ovl))
        i_dang = int(np.argmin(np.abs(1.0 + mu.astype(complex))))
        mu_soft = complex(mu[i_soft])
        bulk = np.abs(1.0 + np.delete(mu.astype(complex), i_soft))
        bulk_signed = np.delete(1.0 + mur, i_soft) \
            if np.all(real_m) else None
        rows.append(dict(
            k=k, ha=ra["h"], hb=rb["h"], kza=ra["kz"], Q=Q,
            dev=dev, mu=mu, n_real=int(np.sum(real_m)),
            n_neg=int(np.sum(fac_r < 0.0)),
            n_near=int(np.sum(np.abs(fac_r) < NEAR_BAR)),
            min_fac=(float(np.min(fac_r)) if len(fac_r)
                     else float("nan")),
            i_soft=i_soft, i_dang=i_dang,
            mu_soft=mu_soft, ovl_soft=float(ovl[i_soft]),
            ovl_dang=float(ovl[i_dang]),
            bulk_min=(float(np.min(bulk_signed))
                      if bulk_signed is not None
                      else float(np.min(bulk))),
            all_real=bool(np.all(real_m)),
            tau=fs["tau"], dmass=float(np.linalg.norm(DC)),
            sga=sga, sgb=sgb))
    return rows, n_skip


def main():
    section("PRIME.PORT.TAU.MOEBIUS.01 -- the exact determinant "
            "bridge of the tau quotient (EXPLORATION ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s"
          % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
    print("    NO RH claim; no marker moves.")
    print("\nS0 -- firewall")
    check("S0.1 AST firewall clean", not ast_scan(BANNED_IDS))

    # ------------------------------------------------------------ W
    section("W -- build the truth + smooth-mass ladders (all "
            "frame-A zones, h <= %d)" % H_DEEP_MAX)
    rungs, srungs = [], []
    rk_max = 0.0
    n_smooth_dead = 0
    for kz in core.frame_a_zones():
        rr = core.build_window(kz)
        r = rung_all(kz, rr_cache=rr)
        if not isinstance(r, dict):
            continue
        rk_max = max(rk_max, r.get("rk", 1.0))
        rungs.append(r)
        uu = np.asarray(rr["uu"], float)
        rs = rung_all(kz, comb=(uu, smooth_masses(uu)),
                      rr_cache=rr)
        if isinstance(rs, dict):
            srungs.append(rs)
        else:
            n_smooth_dead += 1
        if kz in HEAVY and "lamC" in r:
            print("    kz %-3d h %4d truth lam(C_J) %.6f | smooth "
                  "%s"
                  % (kz, r["h"], r["lamC"],
                     ("lam(C_J) %.6f lam(out) %.3f"
                      % (rs["lamC"], rs["lamO"]))
                     if isinstance(rs, dict) and "lamC" in rs
                     else "window unavailable / chain dead"))
    rungs.sort(key=lambda r: (r["h"], r["kz"]))
    srungs.sort(key=lambda r: (r["h"], r["kz"]))
    print("    truth: %d rungs, h %d .. %d; worst [Y,D_P] s3/s1 "
          "%.1e" % (len(rungs), rungs[0]["h"], rungs[-1]["h"],
                    rk_max))
    print("    smooth-mass: %d rungs built, %d chain/window "
          "deaths" % (len(srungs), n_smooth_dead))
    check("W1 >= %d truth rungs built" % MIN_RUNGS,
          len(rungs) >= MIN_RUNGS, "%d rungs" % len(rungs),
          kill="K1")
    check("W2 rank-2 exact on every truth rung (max s3/s1 %.1e "
          "<= %.0e)" % (rk_max, RANK_BAR), rk_max <= RANK_BAR,
          kill="K1")

    # ------------------------------------------------------------ T1
    trows, n_skip_full = factor_pairs(rungs, general=False)
    section("T1 -- THE EXACT FACTORIZATION LEDGER (%d full-window "
            "pairs; %d typed skips)" % (len(trows), n_skip_full))
    print("    Q_h = det(W_{h+1})/det(W_h) = prod_i (1 + mu_i), "
          "mu_i = eig(W_h^{-1} Delta C)  [ward %.0e]" % FACT_WARD)
    print("    step         Q        min(1+mu)  n<-1 near  "
          "mu_soft    1+mu_soft  ovl(soft) s==d ovl(dang) "
          "bulk_min")
    pd_ok = all(r["sga"] > 0 and r["sgb"] > 0 for r in trows)
    for r in trows:
        print("    h %3d->%3d %+.4e  %+.4f     %d    %d   "
              "%+.2e  %+.6f  %.3f     %-5s %.3f     %+.4f"
              % (r["ha"], r["hb"], r["Q"], r["min_fac"],
                 r["n_neg"], r["n_near"], r["mu_soft"].real,
                 1.0 + r["mu_soft"].real, r["ovl_soft"],
                 str(r["i_soft"] == r["i_dang"]), r["ovl_dang"],
                 r["bulk_min"]))
    check("W3 >= %d full-window pairs and det(W) > 0 on every "
          "truth full-window rung" % MIN_PAIRS_T1,
          len(trows) >= MIN_PAIRS_T1 and pd_ok,
          "%d pairs, PD %s" % (len(trows), pd_ok), kill="K1")
    dev_max = (float(np.max([r["dev"] for r in trows]))
               if trows else float("inf"))
    check("T1.1 FACTORIZATION WARD: max rel dev %.2e <= %.0e "
          "(exact algebra)" % (dev_max, FACT_WARD),
          dev_max <= FACT_WARD, kill="KW")
    all_real = all(r["all_real"] for r in trows)
    check("T1.2 truth mu-spectra all real (PD symmetric "
          "similarity)", all_real)
    n_qpos = sum(1 for r in trows if r["Q"] > 0)
    n_flip = sum(1 for r in trows if r["n_neg"] > 0)
    n_near_any = sum(1 for r in trows if r["n_near"] > 0)
    n_coin = sum(1 for r in trows if r["i_soft"] == r["i_dang"])
    print("\n    MEASURED FACTS: Q_h > 0 on %d/%d steps; steps "
          "with a negative factor: %d; steps with a"
          % (n_qpos, len(trows), n_flip))
    print("    near-crossing factor (|1+mu| < %.1f): %d; "
          "dangerous == soft-mode factor on %d/%d steps"
          % (NEAR_BAR, n_near_any, n_coin, len(trows)))
    print("    min(1+mu) ladder: %s"
          % quart([r["min_fac"] for r in trows]))
    print("    soft-mode overlap of the dangerous eigenvector: %s"
          % quart([r["ovl_dang"] for r in trows]))
    check("T1.3 census reported (Q > 0 on %d/%d, %d negative-"
          "factor steps)" % (n_qpos, len(trows), n_flip), True)

    # ------------------------------------------------------------ T2
    section("T2 -- THE ONE-DANGEROUS-FACTOR REDUCTION (the "
            "candidate bridge)")
    bulk_lad = [r["bulk_min"] for r in trows]
    bulk_min_all = float(np.min(bulk_lad)) if bulk_lad else -1.0
    bridge = ("BRIDGE-SCALAR" if bulk_min_all >= BULK_MARGIN
              else "BRIDGE-DIFFUSE")
    musoft = np.array([r["mu_soft"].real for r in trows])
    n_soft_pos = int(np.sum(1.0 + musoft > 0.0))
    taus = np.array([r["tau"] for r in trows])
    dms = np.array([r["dmass"] for r in trows])
    c_tau = corr_or_nan(np.log(np.abs(musoft) + 1e-300),
                        np.log(taus))
    c_dm = corr_or_nan(np.log(np.abs(musoft) + 1e-300),
                       np.log(dms))
    print("    bulk-min ladder (min over i != soft of (1+mu_i)): "
          "%s" % quart(bulk_lad))
    print("    ladder-wide bulk margin: min %.4f vs frozen bar "
          "%.2f" % (bulk_min_all, BULK_MARGIN))
    print("    mu_soft ladder: %s" % quart(musoft))
    print("    sign census: 1 + mu_soft > 0 on %d/%d steps"
          % (n_soft_pos, len(trows)))
    print("    size law: corr(log|mu_soft|, log tau_h) = %s | "
          "corr(log|mu_soft|, log||Delta C||_F) = %s"
          % ("%.3f" % c_tau if np.isfinite(c_tau) else "n/a",
             "%.3f" % c_dm if np.isfinite(c_dm) else "n/a"))
    check("T2.1 typed: %s (bulk margin %.4f vs %.2f)"
          % (bridge, bulk_min_all, BULK_MARGIN), True)
    if bridge == "BRIDGE-SCALAR":
        print("    CONTRACT CANDIDATE (stated, not claimed): "
              "sign(Q_h) = sign(1 + mu_soft) on the whole")
        print("    ladder -- the induction demand is the SINGLE "
              "inequality  1 + mu_soft(h) > 0  per step,")
        print("    mu_soft = the soft-mode eigenvalue of "
              "W_h^{-1}(C_J(h) - C_J(h+1)).")

    # ------------------------------------------------------------ T3
    steps, n_skip_j, n_skip_ref = fit_steps(rungs)
    section("T3 -- THE CONTRACTION LINK (fitted steps reproduced: "
            "%d; skips %d common-j, %d reference)"
            % (len(steps), n_skip_j, n_skip_ref))
    check("W4 >= %d fitted steps" % MIN_PAIRS_FIT,
          len(steps) >= MIN_PAIRS_FIT, "%d steps" % len(steps),
          kill="K1")
    res_v = np.array([s["res"] for s in steps])
    al_v = np.array([s["alpha"] for s in steps])
    med_res = float(np.median(res_v)) if len(res_v) else 1.0
    frac_al = float(np.mean(al_v < 1.0)) if len(al_v) else 0.0
    tab_dev = (float(np.max(np.abs(res_v - np.array(REF_RES))))
               if len(res_v) == REF_N_STEPS else float("inf"))
    check("T3.0 REPRODUCTION WARD: %d steps == %d; residual "
          "table max dev %.1e <= %.1e; |median - %.4f| <= "
          "%.1e; |alpha| < 1 on %.2f == 1.00"
          % (len(steps), REF_N_STEPS, tab_dev, ROUND_TOL,
             REF_MED_RES, ROUND_TOL, frac_al),
          len(steps) == REF_N_STEPS and tab_dev <= ROUND_TOL
          and abs(med_res - REF_MED_RES) <= ROUND_TOL
          and frac_al == 1.0, kill="KW")
    by_k = {s["k"]: s for s in steps}
    link = [(r, by_k[r["k"]]) for r in trows if r["k"] in by_k]
    print("\n    J_h := (1 + mu_soft)/(1 - |alpha_h|^2)  "
          "(NOTHING fitted here; %d joint steps)" % len(link))
    print("    step        1+mu_soft   |alpha|   1-|a|^2    "
          "J_h        J_h - 1")
    jvals, jm1, ldm = [], [], []
    for r, s in link:
        one_m = 1.0 - s["alpha"] ** 2
        Jh = (1.0 + r["mu_soft"].real) / one_m
        jvals.append(Jh)
        jm1.append(Jh - 1.0)
        ldm.append(math.log(max(r["dmass"], 1e-300)))
        print("    h %3d->%3d  %+.6f   %.4f    %.6f   %+.6f  "
              "%+.2e"
              % (r["ha"], r["hb"], 1.0 + r["mu_soft"].real,
                 s["alpha"], one_m, Jh, Jh - 1.0))
    jvals = np.array(jvals)
    jm1 = np.array(jm1)
    all_pos = bool(len(jvals)) and bool(np.all(jvals > 0.0))
    sgn_frac = (max(float(np.mean(jm1 > 0.0)),
                    float(np.mean(jm1 < 0.0)))
                if len(jm1) else 0.0)
    c_link = corr_or_nan(np.log(np.abs(jm1) + 1e-300),
                         np.array(ldm))
    lawful = (all_pos and sgn_frac >= LINK_SIGN_FRAC
              and np.isfinite(c_link) and c_link >= LINK_CORR_BAR)
    link_label = ("LINK-LAWFUL" if lawful else
                  "LINK-POSITIVE" if all_pos else "LINK-OPEN")
    print("    J_h ladder: %s" % quart(jvals))
    print("    (a) J_h > 0 on %s steps; (b) sign(J_h - 1) "
          "constant on %.2f (bar %.2f); (c) corr(log|J_h-1|,"
          % ("all" if all_pos else "NOT all", sgn_frac,
             LINK_SIGN_FRAC))
    print("        log||Delta C||_F) = %s (bar %.2f)"
          % ("%.3f" % c_link if np.isfinite(c_link) else "n/a",
             LINK_CORR_BAR))
    print("    PLAIN STATEMENT: |alpha_h| ~ %.0e (round-46 "
          "identity noise), so 1 - |alpha_h|^2 deviates"
          % float(np.median(al_v)))
    print("    from 1 by O(1e-5) -- the Moebius datum carries "
          "essentially NONE of the determinant load;")
    print("    J_h is 1 + mu_soft up to that correction, and the "
          "link content is (b)+(c) alone.")
    check("T3.1 typed: %s" % link_label, True)

    # ------------------------------------------------------------ T4
    section("T4 -- J-contractivity census in the det-normalized "
            "disk gauge (report only)")
    ssteps, sn_j, sn_ref = fit_steps(srungs)

    def jcensus(name, stps):
        n_iso = n_con = n_ind = n_neg_det = 0
        evmax = 0.0
        for s in stps:
            jc = j_contract_eigs(s["T"])
            if jc is None:
                continue
            tol = JCON_TOL * max(jc["n2"], 1.0)
            if jc["sgn"] < 0:
                n_neg_det += 1
            evmax = max(evmax, float(np.max(np.abs(jc["ev"]))))
            if float(np.max(np.abs(jc["ev"]))) <= tol:
                n_iso += 1
            elif float(jc["ev"][0]) >= -tol:
                n_con += 1
            else:
                n_ind += 1
        print("    %-12s: %d steps | J-isometric %d | strictly "
              "J-contractive %d | indefinite %d | det<0 %d | "
              "max|eig| %.1e"
              % (name, len(stps), n_iso, n_con, n_ind,
                 n_neg_det, evmax))
        return n_iso, n_con, n_ind

    tj = jcensus("truth", steps)
    sj = jcensus("smooth-mass", ssteps)
    sal = np.array([s["alpha"] for s in ssteps])
    print("    smooth-mass fitted |alpha| < 1 on %s of %d steps "
          "(skips %d common-j, %d reference)"
          % ("%.2f" % float(np.mean(sal < 1.0)) if len(sal)
             else "n/a", len(ssteps), sn_j, sn_ref))
    print("    ALGEBRA, stated plainly: det-normalized real "
          "steps with det > 0 are EXACT J-isometries")
    print("    (SL(2,R) ~ SU(1,1)); the census above measures "
          "orientation + numerical deviation only --")
    print("    in this gauge the contraction lives in the "
          "Cayley datum |alpha_h| < 1, not in J - A*JA.")
    check("T4.1 census reported (truth iso/con/ind = %d/%d/%d; "
          "smooth = %d/%d/%d)" % (tj + sj), True)

    # ------------------------------------------------------------ C
    section("C -- controls")
    print("  C1 -- Epstein/scramble (kz %d, frame must die):"
          % CTRL_KZ)
    ok1 = True
    for nmc, kw in (("Epstein", dict(comb=eps_comb(CTRL_KZ))),
                    ("scramble", dict(scramble_seed=1))):
        try:
            rc = rung_all(CTRL_KZ, **kw)
        except (np.linalg.LinAlgError, AssertionError):
            rc = None
        if not isinstance(rc, dict):
            print("    %-8s: rung not built (%r) -> FRAME DIES"
                  % (nmc, rc))
            continue
        if "lamC" not in rc:
            print("    %-8s: window unavailable -> FRAME DIES"
                  % nmc)
            continue
        fired = (rc["lamO"] > 1.0) or (rc["lamC"] > 1.0)
        ok1 &= fired
        print("    %-8s: lam(out) %.3e | lam(C_J) %.3e -> fires "
              "via %s"
              % (nmc, rc["lamO"], rc["lamC"],
                 "EXTERIOR" if rc["lamO"] > 1.0 else
                 "WINDOW" if rc["lamC"] > 1.0 else "NOTHING"))
    check("C1 CONTROLS FIRE (frame death or supercriticality)",
          ok1, kill="K3")

    print("\n  C2 -- the SMOOTH-MASS world (arithmetic detector):")
    sfull = [r for r in srungs if r.get("full")]
    first_rung_viol = None
    n_partial = sum(1 for r in srungs
                    if "CJ" in r and not r.get("full"))
    for r in srungs:
        if "CJ" not in r:
            continue
        W = np.eye(r["CJ"].shape[0]) - r["CJ"]
        ew = np.linalg.eigvalsh(W)
        r["minW"] = float(ew[0])
        r["detW_sgn"] = float(np.prod(np.sign(ew)))
        if r["minW"] < 0.0 and first_rung_viol is None:
            first_rung_viol = r
    srows, sn_skip = factor_pairs(srungs, general=True)
    print("    %d smooth rungs with window (%d full, %d partial "
          "< 12 indices); %d full-window pairs (%d skips); %d "
          "chain deaths"
          % (sum(1 for r in srungs if "CJ" in r), len(sfull),
             n_partial, len(srows), sn_skip, n_smooth_dead))
    first_pair_viol = None
    sdev_max = 0.0
    for r in srows:
        sdev_max = max(sdev_max, r["dev"])
        flag = (r["Q"] < 0.0
                or (np.isfinite(r["min_fac"])
                    and r["min_fac"] < 0.0))
        if flag and first_pair_viol is None:
            first_pair_viol = r
        print("    h %3d->%3d kz %-3d  Q %+.4e  min(1+mu) %s  "
              "n<-1 %d  near %d  ovl(dang) %.3f%s"
              % (r["ha"], r["hb"], r["kza"], r["Q"],
                 ("%+.4f" % r["min_fac"])
                 if np.isfinite(r["min_fac"]) else "  n/a ",
                 r["n_neg"], r["n_near"], r["ovl_dang"],
                 "  <-- CROSSING" if flag else ""))
    print("    smooth factorization ward (general eig): max rel "
          "dev %.2e vs %.0e (%s)"
          % (sdev_max, FACT_WARD_SMOOTH,
             "ok" if sdev_max <= FACT_WARD_SMOOTH else
             "EXCEEDED -- reported"))
    if sfull:
        deep = max(sfull, key=lambda r: r["h"])
        print("    ENDPOINT: deepest full-window smooth rung "
              "h %d kz %d: min eig(W) %+.4e, det sign %+.0f "
              "(wall %s)"
              % (deep["h"], deep["kz"], deep["minW"],
                 deep["detW_sgn"],
                 "VIOLATED" if deep["minW"] < 0 else "holds"))
    if first_rung_viol is not None:
        print("    FIRST WALL VIOLATION on the rung ladder: "
              "h %d kz %d (min eig(W) %+.4e)"
              % (first_rung_viol["h"], first_rung_viol["kz"],
                 first_rung_viol["minW"]))
    if first_pair_viol is not None:
        print("    FIRST FACTOR CROSSING on the step ladder: "
              "h %d -> %d (Q %+.3e, min(1+mu) %+.4f)"
              % (first_pair_viol["ha"], first_pair_viol["hb"],
                 first_pair_viol["Q"], first_pair_viol["min_fac"]))
    detected = (first_rung_viol is not None
                or first_pair_viol is not None
                or any(r["Q"] < 0 for r in srows))
    frame_died = (n_smooth_dead > 0
                  or any("CJ" not in r for r in srungs)
                  or any(r.get("lamO", 0.0) > 1.0
                         for r in srungs))
    if detected:
        smooth_label = "SMOOTH-FLIP-DETECTED"
    elif frame_died:
        smooth_label = "SMOOTH-FRAME-DIES"
        print("    NOTE: the smooth frame itself dies (against "
              "the 'frame survives' premise) -- detection")
        print("    fires via the frame channel; reported "
              "honestly.")
    else:
        smooth_label = "SMOOTH-UNDETECTED"
    check("C2 SMOOTH-MASS DETECTION: %s" % smooth_label,
          smooth_label != "SMOOTH-UNDETECTED", kill="K3")

    # ------------------------------------------------------------ V
    section("V -- FROZEN VERDICT")
    n_pass = sum(1 for _n, okk in CHECKS if okk)
    n_tot = len(CHECKS)
    if KILLS:
        VERDICT = {"K1": "PIPELINE-BROKEN",
                   "KW": "WARD-BROKEN",
                   "K3": "CONTROL-DEAD"}[KILLS[0]]
        print("\n  VERDICT: %s" % VERDICT)
    else:
        VERDICT = ("TAUMOEBIUS-MEASURED / %s / %s / %s"
                   % (bridge, link_label, smooth_label))
        print("\n  VERDICT: %s" % VERDICT)
        print("  (Q > 0 on %d/%d truth steps; bulk margin %.4f; "
              "1 + mu_soft > 0 on %d/%d; J_h census"
              % (n_qpos, len(trows), bulk_min_all, n_soft_pos,
                 len(trows)))
        print("   (a) %s (b) %.2f (c) %s; smooth detection: %s)"
              % (all_pos, sgn_frac,
                 "%.3f" % c_link if np.isfinite(c_link)
                 else "n/a", smooth_label))
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed"
          % (time.time() - T0, n_tot, n_tot - n_pass))
    return 0 if n_pass == n_tot else 1


if __name__ == "__main__":
    raise SystemExit(main())
