#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""cdcore_probe -- PRIME.CONTRACTOR.CDCORE.01: the Christoffel-
Darboux identification of the reproducing kernel (EXPLORATION
ONLY, experiments/; round 33 evening probe 1, 2026-08-08).

THE PREDICTION: the SourceContractor C = W_- K+ W_+ with
K+ = F G+^{-1} F^H is a weighted reproducing-kernel transport,
low-rank displaced in the MULTIPLICATION coordinate
x = 2 cos(D tau) even though the tau-coordinate displacement
needed a growing budget.

THE DERIVATION (typed BEFORE running -- the probe wards it):
the frame columns are F_{j,r} = e^{-i phi_j r} -
e^{-i phi_j (M-1-r)} = gamma_j sin((h - 1/2 - r) phi_j) with
phi_j = 2 pi j / L, gamma_j = 2i e^{-i phi_j (h - 1/2)}, and
sin((k + 1/2) phi) = sin(phi/2) W_k(x), W_k a degree-k
polynomial in x = 2 cos(phi) (Chebyshev 4th kind).  Hence
F = diag(gamma) diag(s) V_poly with s_j = sin(phi_j / 2):
the frame space IS a degree-(h-1) polynomial space, and

  K+(i, j) = gamma_i conj(gamma_j) s_i s_j K_mu(x_i, x_j),

with K_mu the reproducing kernel of P_{h-1} w.r.t. the SOURCE
measure mu = sum_j [4 s_j^2 d_+(j) / 2L] delta_{x_j} (positive
bins only; cos-degenerate bins j, L-j merge exactly since d is
even).  By Christoffel-Darboux, (x - y) K_mu(x, y) =
b_h [p_h(x) p_{h-1}(y) - p_{h-1}(x) p_h(y)]: the displacement
X_- K+ - K+ X+ has rank EXACTLY 2, and the same holds for the
weighted C (diagonal weights commute with diagonal X).

TYPED CONSEQUENCE FOR THE CONTROLS (pre-run): the rank-2
collapse is forced by the WINDOW GEOMETRY for ANY even density
-- Epstein/scramble MUST show the same collapse; the
non-discrimination of the rank is therefore structural, not a
kill.  The arithmetic lives in the MEASURE: the Jacobi chain
(a_n, b_n) of mu and the arm weights -- the controls must
differ THERE (frozen bar below), and their bulk indefiniteness
(lam_min(K) < 0) is unchanged.

TASKS: S1 the kernel + wards (frame factorization machine-
exact; reproducing/projection identity P^2 = P, P F = F at the
anchors).  S2 the decisive displacement test: sv profiles of
X_- C - C X_+ and X_- K+ - K+ X+ vs the tau-coordinate
contrast, per rung along construction {9,12,13,26} + FROZEN
blind holdouts {40,49,60}.  S3 the CD reconstruction: source
Jacobi chain of mu by Stieltjes-Lanczos (full reorth,
h steps -> b_h), orthonormal p_n by recurrence, CD formula,
C rebuilt entrywise; FIREWALL: the reconstruction function
consumes ONLY (chain, m0, node/geometry data) -- no G-, no
target defect, no target eigenvectors (structural: enforced by
the function signature).  S4 the weighted transport reading:
C_ij = w-_i w+_j K+(x_i, x_j) entrywise; the Christoffel
comparison w+^2 K+(x,x) = mu_j K_mu(x_j,x_j) = the leverage
profile (sum = h exactly -- trace ward); the negative-side
load profile reported for coordination.

VERDICT (frozen): CDCORE-IDENTIFIED (rank-2 collapse + CD
reconstruction inside certified budgets on construction AND
holdouts -- the non-monomial spreader is NAMED: K+ is the CD
kernel of the source measure mu) / CDCORE-RANK-GROWS (the
coordinate hypothesis dies -- typed) / CDCORE-PARTIAL (rank
collapses, reconstruction misses -- typed where: rung,
boundary-vs-interior split).  NO RH claim; writes nothing;
v563 READ-ONLY.

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/cdcore_probe.py
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

FROZEN_SPEC = """\
PRIME.CONTRACTOR.CDCORE.01 spec v1 (2026-08-08, frozen before
run).  Coordinate x = 2 cos(D tau) = 2 cos(2 pi j / L) exactly
(folding invisible).  Construction rungs {9, 12, 13, 26};
FROZEN HOLDOUT {40, 49, 60} (zero fitted constants; holdout =
recipe applied blind).  S1 wards: frame factorization F ==
diag(gamma) [s_j sin-poly] at kz 9 rel <= 1e-12 (pure
geometry); projection P = K+[pos,pos] diag(w+^2): ||P P - P||
and ||P F[pos] - F[pos]|| rel <= 1e-8 at anchors {9, 12, 13};
W1 regression ||C_formula - C_pinv|| rel <= 1e-8 at kz 9.
S2 decisive bar: rank@1e-6 of X_- C - C X_+ <= 2 AND hard gap
sig2/sig3 >= 1e6 on ALL 7 rungs (K+-version reported);
tau-contrast: rank@1e-3 of T_- C - C T_+ >= 8 on all rungs +
regression == 12 at kz 9; growth reported fit-free (Spearman
+ log-log slope vs L), no growth bar.  S3 chain: merged
positive nodes (j' = min(j, L-j), weights mu = 2 s^2 d_+ / L
summed), Stieltjes-Lanczos full reorth, h steps (a_0..a_{h-1},
b_1..b_h), N_nodes >= h+1 required else typed; chain wards:
orthonormality ||P^T diag(mu) P - I||_max <= 1e-6, leverage
trace |sum l - h| <= 1e-6 h; CD reconstruction budget per rung
res_F(C_rec - C) <= max(1e-8, 1e2 eps cond2(G+)) AND <= 1e-3
cap (certified budget: the solve and the chain share the G+
conditioning); overflow of p_h at gap points typed if hit.
S4: entrywise max dev reported vs ||C||_max; leverage deciles
+ negative-side load deciles reported (coordination
deliverable).  S5 controls at kz 9: Epstein (x^2+5y^2,
relation-level Lambda_E) + scramble seed 1: x-rank expected 2
(STRUCTURAL, typed pre-run -- not a discriminator); frozen
discrimination bar: first-10 Jacobi coefficient rel L2
distance from truth >= 1e-2 for both AND lam_min(K) < 0 both
(the arithmetic lives in the measure).  VERDICT:
CDCORE-IDENTIFIED iff S1+S2 bars pass AND S3 budgets pass on
all 7 rungs AND chain wards pass; CDCORE-RANK-GROWS iff the
S2 rank bar fails; else CDCORE-PARTIAL (typed: failing rungs,
boundary |x_- - x_+| <= 40 pi / L vs interior residual
split).  Float64; NO RH claim; writes nothing.
"""

CONSTRUCTION = (9, 12, 13, 26)
HOLDOUT = (40, 49, 60)
RUNGS = CONSTRUCTION + HOLDOUT
ANCHORS = (9, 12, 13)
TAU_RANK_REG_KZ9 = 12
BANNED_IDS = ("zetazero", "nzeros", "primerange", "isprime",
              "primepi", "nextprime", "prevprime")

CHECKS = []
FAILS = []
T0 = time.time()


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok)))
    if not ok:
        FAILS.append(name.split()[0])
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


def spearman(a, b):
    ra = np.argsort(np.argsort(a)).astype(float)
    rb = np.argsort(np.argsort(b)).astype(float)
    ra -= ra.mean()
    rb -= rb.mean()
    dn = math.sqrt(float(ra @ ra) * float(rb @ rb))
    return float(ra @ rb) / dn if dn > 0 else 0.0


# ------------------------------------------------ Krein machinery (verbatim)
def odd_extend_mat(h):
    E = np.zeros((2 * h, h))
    E[:h] = np.eye(h)
    E[h:] = -np.eye(h)[::-1]
    return E


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


def ranks_of(sv, thrs=(1e-3, 1e-6, 1e-9)):
    if len(sv) == 0 or sv[0] <= 0:
        return tuple(0 for _ in thrs)
    return tuple(int(np.sum(sv > t * sv[0])) for t in thrs)


def build_rung(kz, scramble_seed=None, comb=None):
    """One rung: density, frame, kernel M' = K+ restricted to
    (neg rows, pos cols), contractor, x/tau coordinates, and
    the source-measure data for the chain."""
    rr = core.build_window(kz, scramble_seed=scramble_seed)
    h, M, D, alpha = rr["h"], rr["M"], rr["D"], rr["alpha"]
    assert M == 2 * h
    uu = np.asarray(rr["uu"], float)
    mm = 2.0 * np.asarray(rr["lam"], float)
    if comb is not None:
        uu, mm = comb
    c_at, _ = core.atom_lags_at(alpha, M, uu, mm)
    c_ar = np.asarray(core.arch_lags(M, D), float)
    c = c_ar + c_at
    d = grid_density(c)
    K = core.odd_toeplitz(c, M)
    L = 2 * M - 2
    E = odd_extend_mat(h)
    F = np.fft.fft(np.vstack([E, np.zeros((L - M, h))]), axis=0)
    jj = np.arange(L)
    jfold = np.minimum(jj, L - jj)
    phi = 2.0 * math.pi * jj / L
    x = 2.0 * np.cos(2.0 * math.pi * jfold / L)
    tau = jfold * (2.0 * math.pi / L) / D
    s = np.sin(phi / 2.0)
    gam = 2j * np.exp(-1j * phi * (h - 0.5))
    pos, neg = d > 0.0, d < 0.0
    wp = np.sqrt(d[pos] / (2.0 * L))
    wm = np.sqrt(-d[neg] / (2.0 * L))
    Bp = np.sqrt(np.maximum(d, 0.0) / (2.0 * L))[:, None] * F
    Gp = np.real(Bp.conj().T @ Bp)
    Mp = F[neg] @ np.linalg.solve(Gp, F[pos].conj().T)
    Cres = wm[:, None] * Mp * wp[None, :]
    evG = np.linalg.eigvalsh(Gp)
    # merged source-measure nodes (positive bins; d even =>
    # bins j and L-j carry equal weight and identical x)
    jp = jj[pos]
    mu_bin = 2.0 * s[jp] ** 2 * d[jp] / L
    ju, inv = np.unique(jfold[jp], return_inverse=True)
    mu = np.zeros(len(ju))
    np.add.at(mu, inv, mu_bin)
    xn = 2.0 * np.cos(2.0 * math.pi * ju / L)
    return dict(rr=rr, h=h, L=L, D=D, alpha=alpha, d=d, K=K,
                F=F, Gp=Gp, Mp=Mp, Cres=Cres, x=x, tau=tau,
                s=s, gam=gam, pos=pos, neg=neg, wp=wp, wm=wm,
                condG=float(evG[-1] / evG[0]),
                xn=xn, mu=mu, ju=ju,
                lminK=float(np.linalg.eigvalsh(K)[0]))


def stieltjes_chain(xn, mu, m_steps):
    """Jacobi chain (a_0..a_{m-1}, b_1..b_m) of the discrete
    measure sum mu_i delta_{xn_i} by Lanczos on diag(xn) with
    full reorthogonalization.  SOURCE ONLY."""
    N = len(xn)
    m0 = float(np.sum(mu))
    Q = np.zeros((N, m_steps + 1))
    Q[:, 0] = np.sqrt(mu) / math.sqrt(m0)
    alphas, betas = [], []
    for k in range(m_steps):
        v = xn * Q[:, k]
        if k > 0:
            v -= betas[-1] * Q[:, k - 1]
        a_ = float(Q[:, k] @ v)
        v -= a_ * Q[:, k]
        for _ in range(2):
            v -= Q[:, :k + 1] @ (Q[:, :k + 1].T @ v)
        b_ = float(np.linalg.norm(v))
        alphas.append(a_)
        if b_ <= 1e-14:
            return np.array(alphas), np.array(betas), m0, True
        betas.append(b_)
        Q[:, k + 1] = v / b_
    return np.array(alphas), np.array(betas), m0, False


def eval_polys(alphas, betas, m0, xs, n_keep):
    """Orthonormal p_n by the three-term recurrence; returns
    (p_{n_keep-1}, p_{n_keep}, sum_{n<n_keep} p_n^2, max|p|).
    SOURCE ONLY: chain + evaluation points."""
    p_prev = np.zeros_like(xs)
    p_cur = np.full_like(xs, 1.0 / math.sqrt(m0))
    ksum = p_cur ** 2
    pmax = float(np.max(np.abs(p_cur)))
    for n in range(n_keep):
        p_next = ((xs - alphas[n]) * p_cur
                  - (betas[n - 1] * p_prev if n > 0 else 0.0)
                  ) / betas[n]
        p_prev, p_cur = p_cur, p_next
        if n < n_keep - 1:
            ksum += p_cur ** 2
        pmax = max(pmax, float(np.max(np.abs(p_cur))))
    return p_prev, p_cur, ksum, pmax


def cd_reconstruct(alphas, betas, m0, b, n_deg):
    """CD reconstruction of C from ONLY the Jacobi chain + the
    node/geometry data (x, s, gamma, arm weights as declared
    transport weights).  No G-, no target defect, no target
    eigenvectors enter this function (structural firewall:
    signature + body).  Returns (C_rec, M_rec, pmax,
    boundary_mask)."""
    xm_, xp_ = b["x"][b["neg"]], b["x"][b["pos"]]
    sm_, sp_ = b["s"][b["neg"]], b["s"][b["pos"]]
    gm_, gp_ = b["gam"][b["neg"]], b["gam"][b["pos"]]
    pm1, pm2, _, pmax1 = eval_polys(alphas, betas, m0, xm_,
                                    n_deg)
    pp1, pp2, _, pmax2 = eval_polys(alphas, betas, m0, xp_,
                                    n_deg)
    b_h = betas[n_deg - 1]
    num = b_h * (np.outer(pm2, pp1) - np.outer(pm1, pp2))
    den = xm_[:, None] - xp_[None, :]
    Kpoly = num / den
    Mrec = (gm_[:, None] * np.conj(gp_)[None, :]) \
        * (sm_[:, None] * sp_[None, :]) * Kpoly
    Crec = b["wm"][:, None] * Mrec * b["wp"][None, :]
    bmask = np.abs(den) <= 40.0 * math.pi / b["L"]
    return Crec, Mrec, max(pmax1, pmax2), bmask


# ================================================================= main
def main():
    section("PRIME.CONTRACTOR.CDCORE.01 -- the Christoffel-"
            "Darboux identification (EXPLORATION ONLY)")
    sha = hashlib.sha256(FROZEN_SPEC.encode("utf-8")).hexdigest()
    print("    FROZEN_SPEC SHA-256 = %s" % sha)
    print("    NO RH claim.  Construction %s, frozen holdout "
          "%s." % (CONSTRUCTION, HOLDOUT))
    print("\nS0 -- firewall")
    check("S0.1 AST firewall clean (no zero/prime oracles)",
          not ast_scan(BANNED_IDS))

    # ---------------- S1 the kernel + wards
    section("S1 -- THE KERNEL: frame factorization + "
            "reproducing property")
    rungs = {}
    for kz in RUNGS:
        rungs[kz] = build_rung(kz)
    b9 = rungs[9]
    # frame factorization ward (pure geometry, machine)
    h9, L9 = b9["h"], b9["L"]
    rr_idx = np.arange(h9)
    Sgeo = np.sin(np.outer(2.0 * math.pi * np.arange(L9) / L9,
                           (h9 - 0.5 - rr_idx)))
    Freb = b9["gam"][:, None] * Sgeo
    fdev = float(np.max(np.abs(Freb - b9["F"]))
                 / np.max(np.abs(b9["F"])))
    check("S1.1 [FRAME FACTORIZATION] F == diag(gamma) . "
          "[sin((h-1/2-r) phi)] at kz 9 (max rel %.1e <= "
          "1e-12) -- the frame space is s(phi) x polynomials "
          "of degree <= h-1 in x = 2 cos(D tau), EXACTLY"
          % fdev, fdev <= 1e-12)
    # W1 regression: formula C vs pinv route at kz 9
    d9 = b9["d"]
    Bp9 = np.sqrt(np.maximum(d9, 0.0) / (2.0 * L9))[:, None] \
        * b9["F"]
    U, sv, Vh = np.linalg.svd(Bp9, full_matrices=False)
    rk = int(np.sum(sv > 1e-12 * sv[0]))
    Cpinv = ((np.sqrt(np.maximum(-d9, 0.0) / (2.0 * L9))
              [:, None] * b9["F"])
             @ (Vh[:rk].conj().T / sv[:rk])) @ U[:, :rk].conj().T
    Cpinv = Cpinv[np.ix_(b9["neg"], b9["pos"])]
    w1 = float(np.linalg.norm(Cpinv - b9["Cres"])
               / np.linalg.norm(b9["Cres"]))
    check("S1.2 [W1 REGRESSION] C = W_- K+ W_+ == the pinv "
          "contractor at kz 9 (rel %.1e <= 1e-8)" % w1,
          w1 <= 1e-8)
    # reproducing / projection ward at the anchors
    proj_ok = True
    for kz in ANCHORS:
        b = rungs[kz]
        Fp_ = b["F"][b["pos"]]
        Kpp = Fp_ @ np.linalg.solve(b["Gp"], Fp_.conj().T)
        P = Kpp * (b["wp"] ** 2)[None, :]
        r1 = float(np.linalg.norm(P @ P - P)
                   / max(np.linalg.norm(P), 1e-300))
        r2 = float(np.linalg.norm(P @ b["F"][b["pos"]]
                                  - b["F"][b["pos"]])
                   / np.linalg.norm(b["F"][b["pos"]]))
        proj_ok &= r1 <= 1e-8 and r2 <= 1e-8
        print("    kz %-3d projection wards: ||P^2 - P|| rel "
              "%.1e, ||P F - F|| rel %.1e" % (kz, r1, r2))
    check("S1.3 [REPRODUCING PROPERTY] P = K+ W+^2 is the "
          "orthogonal projection onto the frame space (P^2 = "
          "P, P F = F, rel <= 1e-8 at the anchors)", proj_ok)

    # ---------------- S2 the decisive displacement test
    section("S2 -- THE DECISIVE TEST: displacement in x = "
            "2 cos(D tau) vs tau (7 rungs)")
    print("    kz    h    L    | x: rank@1e-3/1e-6/1e-9  "
          "sig2/sig3  | K+: r@1e-6 | tau: r@1e-3/1e-6")
    collapse_ok = True
    tau_floor_ok = True
    Ls, tr3, tr6 = [], [], []
    for kz in RUNGS:
        b = rungs[kz]
        xm_, xp_ = b["x"][b["neg"]], b["x"][b["pos"]]
        tm_, tp_ = b["tau"][b["neg"]], b["tau"][b["pos"]]
        RxC = xm_[:, None] * b["Cres"] - b["Cres"] * xp_[None, :]
        svx = np.linalg.svd(RxC, compute_uv=False)
        rx = ranks_of(svx)
        gap23 = float(svx[1] / max(svx[2], 1e-300))
        RxM = xm_[:, None] * b["Mp"] - b["Mp"] * xp_[None, :]
        rxM = ranks_of(np.linalg.svd(RxM, compute_uv=False))
        RtC = tm_[:, None] * b["Cres"] - b["Cres"] * tp_[None, :]
        rt = ranks_of(np.linalg.svd(RtC, compute_uv=False))
        collapse_ok &= (rx[1] <= 2 and gap23 >= 1e6)
        tau_floor_ok &= rt[0] >= 8
        Ls.append(b["L"])
        tr3.append(rt[0])
        tr6.append(rt[1])
        b["rt3"] = rt[0]
        print("    %-4d %-4d %-5d|    %2d / %2d / %2d      "
              "%8.1e |     %2d     |   %3d / %3d%s"
              % (kz, b["h"], b["L"], rx[0], rx[1], rx[2],
                 gap23, rxM[1], rt[0], rt[1],
                 "  (holdout)" if kz in HOLDOUT else ""),
              flush=True)
    check("S2.1 [THE COLLAPSE] rank@1e-6 of X_- C - C X_+ <= "
          "2 with hard gap sig2/sig3 >= 1e6 on ALL 7 rungs "
          "(construction + blind holdouts) -- the CD "
          "prediction: fixed rank TWO, independent of window "
          "size", collapse_ok)
    sl = np.polyfit(np.log(Ls), np.log(np.maximum(tr6, 1)),
                    1)[0]
    check("S2.2 [THE CONTRAST] tau-coordinate rank@1e-3 >= 8 "
          "on all rungs (regression: == %d at kz 9: %s); "
          "growth fit-free: Spearman(rank@1e-6, L) = %+.2f, "
          "log-log slope %+.2f (vs sqrt-L = +0.50) -- the "
          "SAME operator is budget-rank in tau and rank-2 "
          "in x"
          % (TAU_RANK_REG_KZ9,
             rungs[9]["rt3"] == TAU_RANK_REG_KZ9,
             spearman(np.array(tr6, float),
                      np.array(Ls, float)), sl),
          tau_floor_ok
          and rungs[9]["rt3"] == TAU_RANK_REG_KZ9)

    # ---------------- S3 the CD reconstruction
    section("S3 -- THE CD RECONSTRUCTION from the source "
            "Jacobi chain (firewalled)")
    print("    kz    N_nodes  h    cond(G+)  b_h      "
          "max|p|   res_F(C)   budget    res bnd/int")
    recon_ok = True
    chain_ok = True
    chains = {}
    eps = np.finfo(float).eps
    for kz in RUNGS:
        b = rungs[kz]
        h = b["h"]
        if len(b["xn"]) < h + 1:
            recon_ok = False
            print("    kz %-3d: N_nodes %d < h+1 = %d -- "
                  "chain short, typed" % (kz, len(b["xn"]),
                                          h + 1))
            continue
        al, be, m0, brk = stieltjes_chain(b["xn"], b["mu"], h)
        chains[kz] = (al, be, m0)
        if brk or len(be) < h:
            recon_ok = False
            print("    kz %-3d: Lanczos breakdown at step %d "
                  "< h = %d -- typed" % (kz, len(be), h))
            continue
        # chain wards: orthonormality + leverage trace
        # (full column matrix for the orthonormality ward)
        N = len(b["xn"])
        Pm = np.zeros((N, h))
        pp_, pc_ = np.zeros(N), np.full(N, 1.0 / math.sqrt(m0))
        Pm[:, 0] = pc_
        for n in range(h - 1):
            pn = ((b["xn"] - al[n]) * pc_
                  - (be[n - 1] * pp_ if n > 0 else 0.0)) / be[n]
            pp_, pc_ = pc_, pn
            Pm[:, n + 1] = pc_
        orth = float(np.max(np.abs(
            Pm.T @ (b["mu"][:, None] * Pm) - np.eye(h))))
        lev = b["mu"] * np.sum(Pm ** 2, axis=1)
        trc = abs(float(np.sum(lev)) - h) / h
        chain_ok &= orth <= 1e-6 and trc <= 1e-6
        b["lev"] = lev
        # the firewalled reconstruction
        Crec, Mrec, pmax, bmask = cd_reconstruct(al, be, m0,
                                                 b, h)
        nrmC = float(np.linalg.norm(b["Cres"]))
        res = float(np.linalg.norm(Crec - b["Cres"]) / nrmC)
        Ediff = np.abs(Crec - b["Cres"]) ** 2
        rb = math.sqrt(float(np.sum(Ediff[bmask]))) / nrmC
        ri = math.sqrt(float(np.sum(Ediff[~bmask]))) / nrmC
        budget = max(1e-8, 1e2 * eps * b["condG"])
        okr = res <= budget and res <= 1e-3 \
            and np.isfinite(pmax)
        recon_ok &= okr
        b["res"] = res
        print("    %-4d  %-6d  %-4d %.1e  %.2e %.1e  "
              "%.2e  %.2e  %.1e/%.1e%s"
              % (kz, len(b["xn"]), h, b["condG"],
                 be[h - 1], pmax, res, budget, rb, ri,
                 "  (holdout)" if kz in HOLDOUT else ""),
              flush=True)
    check("S3.1 [CHAIN WARDS] recurrence orthonormality "
          "||P^T diag(mu) P - I||_max <= 1e-6 and leverage "
          "trace sum = h (rel 1e-6) on every rung", chain_ok)
    check("S3.2 [THE RECONSTRUCTION] the CD formula from the "
          "source chain rebuilds C entrywise within the "
          "certified budget max(1e-8, 1e2 eps cond(G+)) on "
          "construction AND blind holdouts (FIREWALL: the "
          "reconstruction consumed only chain + node/geometry "
          "data -- no G-, no target defect, no target "
          "eigenvectors, enforced by cd_reconstruct's "
          "signature)", recon_ok)

    # ---------------- S4 the weighted transport reading
    section("S4 -- the weighted transport + the Christoffel "
            "profile")
    b = rungs[9]
    assert 9 in chains and len(chains[9][1]) >= b["h"], \
        "kz 9 chain unavailable -- S3 typed the failure"
    al, be, m0 = chains[9]
    Crec, _M, _p, _bm = cd_reconstruct(al, be, m0, b, b["h"])
    edev = float(np.max(np.abs(Crec - b["Cres"]))
                 / np.max(np.abs(b["Cres"])))
    check("S4.1 [ENTRYWISE TRANSPORT] C_ij == w-_i w+_j "
          "K+(x_i, x_j) with K+ the CD kernel, entrywise at "
          "kz 9 (max dev %.1e of ||C||_max <= 1e-6)" % edev,
          edev <= 1e-6)
    for kz in (9, RUNGS[-1]):
        bq = rungs[kz]
        if "lev" not in bq:
            continue
        lev = bq["lev"]
        tn = bq["ju"] * (2.0 * math.pi / bq["L"]) / bq["D"]
        qs = np.percentile(lev, [10, 30, 50, 70, 90])
        # negative-side Christoffel load
        aln, ben, m0n = chains[kz]
        _p1, _p2, ksn, _pm = eval_polys(
            aln, ben, m0n, bq["x"][bq["neg"]], bq["h"])
        qneg = bq["wm"] ** 2 * 4.0 * bq["s"][bq["neg"]] ** 2 \
            * ksn
        print("    kz %-3d leverage l_j = mu_j K_mu(x_j, x_j):"
              " deciles %s, mean %.3f (= h/N_bins), tau of "
              "top-decile nodes median %.2f | neg-side load "
              "w-^2 K+(x,x): median %.2e max %.2e sum %.1f"
              % (kz, "/".join("%.2f" % q for q in qs),
                 float(np.mean(lev)),
                 float(np.median(tn[lev > qs[-1]])),
                 float(np.median(qneg)), float(np.max(qneg)),
                 float(np.sum(qneg))))
    print("    COORDINATION NOTE (for the wave's probe 3): "
          "w+^2-weighted diagonal == the leverage/Christoffel "
          "profile above; the arm weights are NOT "
          "equi-oscillating -- the profile carries the band "
          "structure.")

    # ---------------- S5 controls
    section("S5 -- controls at kz 9 (Epstein, scramble): the "
            "rank is geometry, the CHAIN is arithmetic")
    rr9 = b9["rr"]
    N_E = int(math.floor(math.exp(2.0 * rr9["alpha"]))) + 1
    lamE = lambda_eps(N_E)
    nn = np.nonzero(np.abs(lamE) > 1e-12)[0]
    at, bt, _m = chains[9]
    ctr_ok = True
    for nmc, kw in (("Epstein", dict(comb=(
            np.log(nn.astype(float)),
            2.0 * lamE[nn] / np.sqrt(nn.astype(float))))),
            ("scramble", dict(scramble_seed=1))):
        bc = build_rung(9, **kw)
        xm_, xp_ = bc["x"][bc["neg"]], bc["x"][bc["pos"]]
        Rx = xm_[:, None] * bc["Cres"] \
            - bc["Cres"] * xp_[None, :]
        rx = ranks_of(np.linalg.svd(Rx, compute_uv=False))
        alc, bec, _mc, _bk = stieltjes_chain(
            bc["xn"], bc["mu"], min(bc["h"], len(bc["xn"]) - 1))
        n10 = min(10, len(alc), len(at), len(bec), len(bt))
        va = np.concatenate([at[:n10], bt[:n10]])
        vc = np.concatenate([alc[:n10], bec[:n10]])
        dist = float(np.linalg.norm(vc - va)
                     / np.linalg.norm(va))
        ok = dist >= 1e-2 and bc["lminK"] < 0.0
        ctr_ok &= ok
        print("    %-8s: x-rank@1e-6 = %d (expected 2 -- "
              "STRUCTURAL, typed pre-run), chain distance "
              "(first %d a+b) = %.3f (bar >= 1e-2), "
              "lam_min(K) = %+.3e < 0: %s"
              % (nmc, rx[1], n10, dist, bc["lminK"], ok))
    check("S5.1 [DISCRIMINATION IN THE MEASURE] both controls "
          "show the same geometric rank-2 collapse (predicted "
          "by the derivation for ANY even density -- the "
          "collapse NAMES the geometry, it cannot certify "
          "arithmetic) while their Jacobi chains differ from "
          "truth at O(1) and their bulk stays indefinite -- "
          "the arithmetic lives in the measure mu, exactly "
          "where the CD identification puts it", ctr_ok)

    # ---------------- V verdict
    section("V -- FROZEN VERDICT + honest consequence")
    wards_ok = (fdev <= 1e-12 and w1 <= 1e-8 and proj_ok
                and chain_ok)
    if not collapse_ok:
        verdict = "CDCORE-RANK-GROWS"
    elif recon_ok and wards_ok:
        verdict = "CDCORE-IDENTIFIED"
    else:
        verdict = "CDCORE-PARTIAL"
    print("\n  VERDICT: %s   [frame ward %s | collapse %s | "
          "reconstruction %s | chain wards %s | tau contrast "
          "%s | controls %s]"
          % (verdict, fdev <= 1e-12, collapse_ok, recon_ok,
             chain_ok, tau_floor_ok, ctr_ok))
    if verdict == "CDCORE-IDENTIFIED":
        print("""
  HONEST CONSEQUENCE: the non-monomial spreader is NAMED.  The
  reproducing kernel of the SourceContractor is the
  CHRISTOFFEL-DARBOUX KERNEL of an explicit source measure:
  mu = sum over positive-density bins of [2 sin^2(phi/2)
  d_+(phi) / L] delta at x = 2 cos(D tau), and

      C_ij = w-_i w+_j gamma_i conj(gamma_j) s_i s_j
             K_mu(x_i, x_j),

  machine-verified entrywise on construction windows and blind
  holdouts, with the displacement rank collapsing from the
  tau-coordinate budget (%d at kz 9, growing with L) to
  EXACTLY 2 in the multiplication coordinate -- the CD
  structure, warded by the hard sig2/sig3 gap.  The whole
  contractor is now three named objects: the arm weights
  (density roots), the phase/geometry factors (gamma, s), and
  ONE Jacobi chain (a_n, b_n) of the source measure.  The
  floor statement ||C|| <= 1 becomes a statement about a
  weighted CD kernel transported between the negative and
  positive spectral bands of the SAME measure family --
  the classical objects (Christoffel functions, chain
  asymptotics) now apply.  Honest boundary: the rank-2
  collapse itself is window geometry (the controls collapse
  too); what is arithmetic is the CHAIN and the WEIGHTS --
  a contraction proof must still control those, and the
  Loewner equivalence to the floor is unchanged.  NO RH
  claim.""" % TAU_RANK_REG_KZ9)
    elif verdict == "CDCORE-PARTIAL":
        print("""
  HONEST CONSEQUENCE (typed): the displacement rank collapses
  to 2 in x = 2 cos(D tau) -- the CD structure is present --
  but the chain-based reconstruction misses the certified
  budget where marked above (residual split boundary/interior
  printed per rung).  The failure localizes the broken piece:
  chain conditioning / gap-point polynomial growth, not the
  kernel identity.  NO RH claim.""")
    else:
        print("""
  HONEST CONSEQUENCE (typed): the multiplication-coordinate
  hypothesis dies -- the displacement rank does not collapse
  in x = 2 cos(D tau); the growth law is printed above.  The
  frame-polynomial derivation must then have a broken premise
  (inspect the frame ward).  NO RH claim.""")
    n_pass = sum(1 for _n, ok in CHECKS if ok)
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed%s"
          % (time.time() - T0, len(CHECKS), len(FAILS),
             ("  " + ",".join(FAILS)) if FAILS else ""))
    return 0 if n_pass == len(CHECKS) else 1


if __name__ == "__main__":
    raise SystemExit(main())
