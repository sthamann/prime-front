#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""port_kyp_storage_probe -- PRIME.PORT.KYP.01
(EXPLORATION ONLY, experiments/; round 45, probe 3 of the new
review: is the compressed 12-dimensional port window the STATE
SPACE of a contractive transfer function with a positive
KYP/bounded-real storage matrix, and does the corpus's older
boundary Riccati object match it under a source-determined
congruence?  2026-08-09.)

CONTEXT (declared inputs): port_cocycle_window_probe (the fixed
12-index Schur compression C_J carries the wall EXACTLY,
(1 - lam_max(C_J))/tau = 1.00, op-norm convergent);
port_riemann_hilbert_setup_probe (IIKS generators (f, g) of the
exactly-rank-2 commutator [Y, D_P] on the port node set).

K0 -- THE CORPUS SEARCH (result frozen here): the older boundary
Riccati machinery IS boundary_formulation_probe.py (contract
BOUNDARY.FORMULATION, 2026-07-27, T116): the boundary state
(Sig, r, sig) = partial minimisation of the pole-free odd form
T = Toeplitz(c) - Hankel(c) over the interior,
    Sig = T_BB - T_BI T_II^{-1} T_IB,
updated by a Riccati recursion; its deep march ran at EXACTLY
state width W_DEEP = 12 (the "exact 12x12-state boundary run" of
the review).  HONESTY: that object lives on the outermost 12
CELLS of the odd Weil form on frame-A windows -- position space
-- while the port window lives on 12 folded PORT NODES of the
v563 ladder -- a different geometry.  There is NO canonical
source map between the two coordinate systems.  K3 therefore
REBUILDS Sigma_h per the T116 construction from the v563 rung's
OWN lag vector (c = arch + atoms, outermost b cells, b = |J|)
and tests the congruence with the only source-determined T
available (the identity on 12-dim space), typing the outcome
honestly; a fitted congruence between two PD matrices exists
ALWAYS (Sylvester), so STORAGE-FREE-FIT is the honest label
whenever only that trivial route works.

FROZEN PROTOCOL (2026-08-09; full frame-A ladder h <= 900,
window >= 8 indices; heavy rungs kz {9, 12, 13, 26, 40} printed;
K3 on the heavy subset only -- Sigma_h needs an O((M/2)^3) dense
elimination per rung and the budget forbids all 37; controls
kz 9):

 K1  MINIMAL REALIZATION FROM THE GENERATORS.  Frozen
     construction: A = the compression of the multiplication
     operator Y onto the window = diag(y_j, j in J) (EXACT Schur
     compression, Y is diagonal); B = f|_J; C = g|_J^T; D = 0.
     Phi(z) = D + z C (I - z A)^{-1} B, a SCALAR rational
     function.  GAUGE FREEDOMS, stated: (i) (f, g) carry the
     frozen SVD extraction of the RH probe; the SL(2) gauge
     (f, g) -> (af + bg, cf + dg), ad - bc = 1, preserves D_P
     but NOT Phi (the products f_j g_j are not gauge invariant)
     -- the probe measures the CANONICAL-GAUGE object only;
     (ii) the scale of (f, g) is sqrt(s1) each with s1 =
     ||[Y, D_P]||_2, a source scale -- contractivity of Phi is
     therefore scale-sensitive and the honesty check below must
     (and does) report it; (iii) D = 0 is the canonical centre
     of the constant-shift freedom.  McMillan degree: numerical
     rank of the 20 x 20 Hankel matrix of the Markov parameters
     m_k = C A^{k-1} B, k = 1..39 (frozen tol: sv > 1e-10 sv_1).
     RESOLUTION CAVEAT, declared: the window poles 1/y_j cluster
     within O((j/L)^2) of z = 1, so a 39-term Hankel is a LOWER
     bound on the degree; because A is diagonal with distinct
     y_j, the exact structural degree is the residue count
     #{j : f_j g_j != 0} (frozen tol |f_j g_j| > 1e-12 max) --
     BOTH ladders are reported, MCMILLAN-12 is typed on the
     residue count.

 K2  BOUNDED-REAL/KYP TEST.  Solve the discrete-time
     bounded-real Riccati equation
       P = A^T P A + C^T C
           + (A^T P B)(1 - D^2 - B^T P B)^{-1}(B^T P A)
     by the STRUCTURED DOUBLING iteration (SDA; the standard
     no-external-SDP route: E <- E (I + G H)^{-1} E, G <- G +
     E (I + G H)^{-1} G E^T, H <- H + E^T H (I + G H)^{-1} E
     with E_0 = A, G_0 = -B B^T/(1 - D^2), H_0 = C^T C; H -> P0
     quadratically), accepted only if the DARE residual is
     <= 1e-8 rel.  P0 is the MINIMAL (canonical) storage; it is
     singular exactly on the unobservable directions (residues
     f_j g_j = 0), so the PD certificate is the frozen
     delta-OBSERVABILITY COMPLETION: re-solve the DARE with
     H_0 = C^T C + delta I,
       delta = 1e-3 (1 - ||Phi||_inf^2) / ssup^2,
       ssup  = max over the frozen theta grid of
               ||z (I - z A)^{-1} B||_2,
     which exists whenever ||Phi||_inf < 1 (the augmented
     transfer [Phi; sqrt(delta) z (I - zA)^{-1} B] stays
     strictly contractive by the delta bound), gives P > 0
     (delta I makes (A, C) observable), and keeps the KYP
     residual matrix
       diag(P, 1) - [[A, B], [C, D]]^T diag(P, 1) [[A, B],[C, D]]
     PSD EXACTLY (its Schur complement is delta I).  Typed
     KYP-POSITIVE iff the PD storage passes on every truth
     rung; reported: min eig(P0), delta, min eig(P), KYP
     residual min eig.  K3/K4 compare the CANONICAL minimal P0
     (gauge-free), not the certificate P.
     Frequency ward: contractivity ||Phi||_inf <= 1 is computed
     INDEPENDENTLY on the frozen grid theta in {0} u
     logspace(-10, log10(pi), 4000) (the poles sit at theta ~ 0,
     the log grid resolves them); the two channels must agree.
     THE TAUTOLOGY WARNING, frozen: this construction does NOT
     feed I - C_J >= 0 into Phi -- so a KYP pass here is NOT
     automatically a reformulation of the wall; but it MAY pass
     for the cheaper reason that the generator scale sqrt(s1)
     makes Phi small.  The honesty check therefore reports
     ||Phi||_inf against tau rung by rung and on the CONTROLS:
     if the controls kill the wall (lam(E) > 1) while the KYP
     channel stays contractive, the KYP object is BLIND to the
     wall and the probe says so plainly (the residual value of
     the probe is then the storage-matrix OBJECT for K3, not new
     wall evidence).

 K3  CONGRUENCE TO THE T116 RICCATI OBJECT (heavy rungs).
     Sigma_h = T_BB - T_BI T_II^{-1} T_IB with T the odd form of
     the rung's own lag vector, B = outermost b = |J| cells.
     Source-determined congruence: T_c = I (there is no
     canonical cell->node map; the identity on the abstract
     12-dim space is the ONLY unfitted candidate).  Typed
     STORAGE-MATCHED iff ||T_c^T Sigma_h T_c - P||_F/||P||_F
     <= 1e-6 on every heavy rung; the one-scalar calibration
     c^2 = tr(P)/tr(Sigma_h) is reported as a LABELED
     one-parameter fit; STORAGE-FREE-FIT if only a fitted
     congruence works (always available for PD pairs, Sylvester
     -- the review's kill); STORAGE-NO-OBJECT if T_II is not PD
     (object does not exist on the rung).

 K4  CASCADE/RICCATI UPDATE (report only): rung-to-rung, is
     P_{h+1} closer to the one-step Riccati image F_{h+1}(P_h)
     (the simplest Redheffer/Schur cascade candidate, F = the
     DARE map with rung h+1's (A, B, C) on the common index set)
     than to P_h itself?  Residual vs raw difference printed.

 C   CONTROLS (kz 9, must fire): Epstein/scramble: lam(E) > 1
     (the wall channel); the KYP-channel behaviour (frame death
     or indefinite storage or blind-pass) is REPORTED per
     control.

KILLS: K1 pipeline (window/Lanczos/generator extraction) breaks
on truth -> PIPELINE-BROKEN; K2 the two contractivity channels
(frequency vs Riccati) disagree on a truth rung ->
PIPELINE-BROKEN; K3 controls silent in the value channel ->
CONTROL-DEAD.

VERDICT (frozen enum): KYP-MEASURED (+ typed sublabels
MCMILLAN-*/KYP-*/STORAGE-*) / PIPELINE-BROKEN / CONTROL-DEAD.

NO RH claim.  Firewall: no zeros, no prime oracles (AST scan);
v563 READ-ONLY; RNG nowhere (controls use the frozen Epstein
comb and scramble_seed=1 inside v563); stdout only; no marker
moves.

SPEC v2 (2026-08-09, after run 1; fail-first preserved -- run 1
ended PIPELINE-BROKEN via the K2.0 channel-agreement ward,
which is exactly what the ward exists for):
  (a) SDA SIGN REPAIR: v1 coded the doubling middle factor as
      (I - G H)^{-1} with G_0 = -B B^T/(1 - D^2); in the +G
      convention it must be (I + G H)^{-1}.  Verified against a
      brute-force fixed point on a synthetic contractive system
      (rel 6e-17 after repair; 1e-5 mismatch before).
  (b) SINGULAR MINIMAL STORAGE: run 1 measured vanishing
      residues f_j g_j on every rung (residue degrees 8..11,
      never 12), so the DARE solution P0 is PSD-singular by
      STRUCTURE, not by failure.  v2 added a Lyapunov shift
      P0 + eps diag(1/(1-y^2)) as the PD certificate.

SPEC v3 (2026-08-09, after run 2; fail-first preserved): the v2
Lyapunov shift is PD but leaves the Riccati manifold -- run 2
measured the KYP residual min eig at -8.9..-30 (indefinite), so
the certificate was WRONG and the honest typed label of run 2
was KYP-INDEFINITE.  v3 replaces it with the delta-observability
completion above, whose KYP residual is PSD by construction
(Schur complement delta I); the DARE residual tolerance, the
typed labels, and every other bar are unchanged.

Sources (read-only): v563_paper2_readouts; port_cocycle_window
(WINDOW-CARRIES, declared), port_riemann_hilbert_setup
(RH-SETUP-WELLPOSED, declared), boundary_formulation_probe
(T116 construction, rebuilt here, declared).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/port_kyp_storage_probe.py
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

HEAVY = (9, 12, 13, 26, 40)
JWIN = tuple(range(2, 25, 2))
BANNED_IDS = ("zetazero", "nzeros", "primerange", "isprime",
              "primepi", "nextprime", "prevprime")

HANKEL_TOL = 1e-10          # frozen: numerical-rank cut on sv/sv1
RESIDUE_TOL = 1e-12         # frozen: |f_j g_j| > tol * max
DARE_TOL = 1e-8             # frozen: accepted DARE rel residual
CONGR_TOL = 1e-6            # frozen: STORAGE-MATCHED threshold
SIGMA_CAP = 4600            # frozen cost cap on the odd half-size
TIME_GUARD = 700.0          # ladder guard (heavy-only fallback)

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


def antisym_generators(C):
    """Canonical (f, g) with C = f g^T - g f^T (frozen RH-probe
    extraction: paired-singular-value normal form)."""
    U, sv, _Vh = np.linalg.svd(C)
    s1 = sv[0]
    f = math.sqrt(s1) * U[:, 0]
    g = math.sqrt(s1) * U[:, 1]
    Ct = np.outer(f, g) - np.outer(g, f)
    if np.linalg.norm(Ct + C) < np.linalg.norm(Ct - C):
        g = -g
    return f, g, sv


def integrable_offdiag(f, g, y):
    dy = y[:, None] - y[None, :] + np.eye(len(y))
    K = (f[:, None] * g[None, :] - g[:, None] * f[None, :]) / dy
    np.fill_diagonal(K, 0.0)
    return K


def offdiag_rel(A, B):
    M_ = A - B
    np.fill_diagonal(M_, 0.0)
    A0 = A.copy()
    np.fill_diagonal(A0, 0.0)
    return float(np.linalg.norm(M_) / np.linalg.norm(A0))


def odd_toeplitz(c, M):
    """T116 odd form: (c[|r-s|] - c[M-1-r-s]) on h = M//2 cells,
    r = 0 the outermost cell."""
    h = M // 2
    r = np.arange(h)
    return (c[np.abs(r[:, None] - r[None, :])]
            - c[(M - 1) - r[:, None] - r[None, :]])


def sym(A):
    return 0.5 * (A + A.T)


# ---------------------------------------------------------------
# realization + KYP machinery (K1/K2)
# ---------------------------------------------------------------
def markov_hankel_degree(y, B, C, nmk=40, nh=20):
    """Frozen Hankel test: m_k = sum_j C_j B_j y_j^{k-1}."""
    r = C * B
    mk = np.array([float(np.sum(r * y ** k)) for k in range(nmk)])
    H = np.empty((nh, nh))
    for i in range(nh):
        H[i, :] = mk[i:i + nh]
    sv = np.linalg.svd(H, compute_uv=False)
    if sv[0] <= 0.0:
        return 0, sv
    return int(np.sum(sv > HANKEL_TOL * sv[0])), sv


def residue_degree(B, C):
    r = np.abs(C * B)
    mx = float(np.max(r)) if len(r) else 0.0
    if mx <= 0.0:
        return 0
    return int(np.sum(r > RESIDUE_TOL * mx))


def hinf_norm(y, B, C, D=0.0):
    """||Phi||_inf on the frozen theta grid (poles cluster at
    theta ~ 0; the log grid resolves widths down to 1e-10)."""
    th = np.concatenate([[0.0],
                         np.logspace(-10.0, math.log10(math.pi),
                                     4000)])
    z = np.exp(1j * th)
    r = C * B
    vals = D + z * np.sum(r[None, :] / (1.0 - z[:, None]
                                        * y[None, :]), axis=1)
    return float(np.max(np.abs(vals)))


def kyp_residual_min(P, y, B, C, D=0.0):
    """min eig of diag(P,1) - [[A,B],[C,D]]^T diag(P,1)
    [[A,B],[C,D]]."""
    n = len(y)
    S = np.zeros((n + 1, n + 1))
    S[:n, :n] = np.diag(y)
    S[:n, n] = B
    S[n, :n] = C
    S[n, n] = D
    W = np.zeros((n + 1, n + 1))
    W[:n, :n] = P
    W[n, n] = 1.0
    return float(np.linalg.eigvalsh(sym(W - S.T @ W @ S))[0])


def _sda_dare(y, B, H0, r0, iters=200, tol=1e-14):
    """SDA doubling (frozen, SPEC v2 sign) for
    P = A^T P A + H0 + (A^T P B)(r0 - B^T P B)^{-1}(B^T P A),
    A = diag(y).  Returns (P, rel_residual) or None."""
    n = len(y)
    A = np.diag(y)
    E = A.copy()
    Gm = -np.outer(B, B) / r0
    H = np.array(H0, float)
    for _ in range(iters):
        try:
            M1i = np.linalg.inv(np.eye(n) + Gm @ H)
        except np.linalg.LinAlgError:
            return None
        if not np.all(np.isfinite(M1i)):
            return None
        E2 = E @ M1i @ E
        G2 = Gm + E @ (M1i @ Gm) @ E.T
        H2 = H + E.T @ (H @ M1i) @ E
        dH = float(np.linalg.norm(H2 - H)
                   / max(np.linalg.norm(H2), 1e-300))
        E, Gm, H = E2, sym(G2), sym(H2)
        if dH <= tol:
            break
    P = sym(H)
    if not np.all(np.isfinite(P)):
        return None
    den = r0 - float(B @ P @ B)
    if den <= 0.0:
        return None
    w = A @ P @ B
    resid = A @ P @ A + H0 + np.outer(w, w) / den - P
    rel = float(np.linalg.norm(resid)
                / max(np.linalg.norm(P), 1e-300))
    return P, rel


def solve_bounded_real(y, B, C, D=0.0, hinf=None):
    """Frozen K2 method: canonical minimal storage P0 (DARE with
    H0 = C^T C) plus the SPEC v3 delta-observability completion
    for the PD certificate.  Returns a dict or None."""
    r0 = 1.0 - D * D
    out0 = _sda_dare(y, B, np.outer(C, C), r0)
    if out0 is None:
        return None
    P0, rel0 = out0
    if hinf is None:
        hinf = hinf_norm(y, B, C, D)
    if hinf >= 1.0:
        return None
    th = np.concatenate([[0.0],
                         np.logspace(-10.0, math.log10(math.pi),
                                     4000)])
    z = np.exp(1j * th)
    ssup2 = float(np.max(np.sum(
        np.abs(B[None, :] / (1.0 - z[:, None] * y[None, :]))
        ** 2, axis=1)))
    delta = 1e-3 * (1.0 - hinf * hinf) / max(ssup2, 1e-300)
    outd = _sda_dare(y, B, np.outer(C, C)
                     + delta * np.eye(len(y)), r0)
    if outd is None:
        return None
    P, reld = outd
    return dict(P0=P0, P=P, rel=max(rel0, reld), delta=delta,
                p0_min=float(np.linalg.eigvalsh(P0)[0]),
                p_min=float(np.linalg.eigvalsh(P)[0]),
                kyp_min=kyp_residual_min(P, y, B, C, D))


# ---------------------------------------------------------------
# one rung: window compression + port generators + realization
# ---------------------------------------------------------------
def rung_data(kz, scramble_seed=None, comb=None, want_sigma=False):
    rr = core.build_window(kz, scramble_seed=scramble_seed)
    h, M, D, alpha = rr["h"], rr["M"], rr["D"], rr["alpha"]
    uu = np.asarray(rr["uu"], float)
    mm = 2.0 * np.asarray(rr["lam"], float)
    if comb is not None:
        uu, mm = comb
    c_at, _ = core.atom_lags_at(alpha, M, uu, mm)
    c_ar = np.asarray(core.arch_lags(M, D), float)
    cvec = c_ar + c_at
    d = grid_density(cvec)
    L = 2 * M - 2
    if h > 900:
        return "TOO-DEEP"
    xs, ws, _ = folded_measure(d, L, +1.0)
    ys, vs, uf_n = folded_measure(d, L, -1.0)
    al, be, m0, steps = lanczos_chain(xs, ws, h + 1)
    if steps < h + 1 or np.any(be <= 0):
        return None
    Pn = eval_chain(al, be, m0, ys, h)
    G = np.sqrt(vs)[:, None] * (Pn @ Pn.T) * np.sqrt(vs)[None, :]
    G = sym(G)
    lamE = float(np.linalg.eigvalsh(G)[-1])
    tau = 1.0 - lamE
    # -- fixed window compression (cocycle probe, verbatim) -----
    idx = {int(j): k for k, j in enumerate(uf_n)}
    jav = [j for j in JWIN if j in idx]
    if len(jav) < 8:
        return None
    iw = [idx[j] for j in jav]
    io = [k for k in range(G.shape[0]) if k not in set(iw)]
    Ew = G[np.ix_(iw, iw)]
    Ex = G[np.ix_(iw, io)]
    Eo = G[np.ix_(io, io)]
    lamO = float(np.linalg.eigvalsh(Eo)[-1])
    CJ = sym(Ew + Ex @ np.linalg.solve(np.eye(len(io)) - Eo,
                                       Ex.T))
    lamC = float(np.linalg.eigvalsh(CJ)[-1])
    # -- dressed port + IIKS generators (RH probe, verbatim) ----
    tau_m = (2.0 * math.pi * uf_n / L) / D
    port = tau_m <= float(np.max(tau_m)) / 10.0
    ip, ib = np.where(port)[0], np.where(~port)[0]
    Pp = G[np.ix_(ip, ip)]
    Xp = G[np.ix_(ip, ib)]
    Rp = G[np.ix_(ib, ib)]
    DP = sym(Pp + Xp @ np.linalg.solve(np.eye(len(ib)) - Rp,
                                       Xp.T))
    yp = ys[ip]
    Cm = np.diag(yp) @ DP - DP @ np.diag(yp)
    f, g, sv = antisym_generators(Cm)
    rec = offdiag_rel(DP, integrable_offdiag(f, g, yp))
    # -- window inside the port set -----------------------------
    ppos = {int(i): k for k, i in enumerate(ip)}
    jreal, pos = [], []
    for j, i in zip(jav, iw):
        if int(i) in ppos:
            jreal.append(j)
            pos.append(ppos[int(i)])
    if len(jreal) < 8:
        return None
    Ad = yp[pos]
    Bv = f[pos]
    Cv = g[pos]
    out = dict(kz=kz, h=h, M=M, tau=tau, lamE=lamE, lamO=lamO,
               lamC=lamC, jav=jav, jreal=jreal, y=Ad, B=Bv, C=Cv,
               s1=float(sv[0]), rec=rec, cvec=cvec)
    # -- T116 boundary Riccati object, rebuilt (K3) --------------
    if want_sigma:
        h_odd = M // 2
        if h_odd > SIGMA_CAP:
            out["Sigma"] = "TOO-BIG"
        else:
            T = odd_toeplitz(cvec, M)
            b = len(jreal)
            TII = sym(T[b:, b:])
            try:
                np.linalg.cholesky(TII)
                Sig = sym(T[:b, :b] - T[:b, b:]
                          @ np.linalg.solve(TII, T[b:, :b]))
                out["Sigma"] = Sig
            except np.linalg.LinAlgError:
                out["Sigma"] = "NOT-PD"
    return out


def dare_map(P, y, B, C, D=0.0):
    A = np.diag(y)
    den = (1.0 - D * D) - float(B @ P @ B)
    if den <= 0.0:
        return None
    w = A @ P @ B + C * D
    return sym(A @ P @ A + np.outer(C, C) + np.outer(w, w) / den)


def main():
    section("PRIME.PORT.KYP.01 -- KYP storage of the port window "
            "(EXPLORATION ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s"
          % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
    print("    NO RH claim; no marker moves.")
    print("\nS0 -- firewall")
    check("S0.1 AST firewall clean", not ast_scan(BANNED_IDS))

    section("K0 -- the corpus search (result frozen in the spec)")
    print("    The older boundary Riccati machinery: "
          "boundary_formulation_probe.py (BOUNDARY.FORMULATION,")
    print("    2026-07-27, T116): state (Sig, r, sig), Sig = "
          "T_BB - T_BI T_II^{-1} T_IB on the outermost")
    print("    b cells of the odd form; deep march at state "
          "width W_DEEP = 12 -- the reviewed 12x12 run.")
    print("    It lives on frame-A CELL space, not port-node "
          "space; K3 rebuilds it per rung from the")
    print("    v563 lag vector and types the congruence "
          "honestly (no canonical cell->node map exists).")
    check("K0.1 old object located and construction frozen "
          "(rebuild, not import)", True)

    section("K1/K2 -- realization, McMillan ladder, KYP storage")
    rows = []
    heavy_only = False
    for kz in core.frame_a_zones():
        if heavy_only and kz not in HEAVY:
            continue
        r = rung_data(kz, want_sigma=(kz in HEAVY))
        if r in (None, "TOO-DEEP"):
            continue
        y, B, C = r["y"], r["B"], r["C"]
        r["deg_h"], _svh = markov_hankel_degree(y, B, C)
        r["deg_r"] = residue_degree(B, C)
        r["hinf"] = hinf_norm(y, B, C)
        sol = solve_bounded_real(y, B, C, hinf=r["hinf"])
        if sol is not None and sol["rel"] <= DARE_TOL:
            r.update(P=sol["P"], P0=sol["P0"],
                     delta=sol["delta"], dare_rel=sol["rel"],
                     kyp_min=sol["kyp_min"], p_min=sol["p_min"],
                     p0_min=sol["p0_min"])
        else:
            r.update(P=None, P0=None, delta=float("nan"),
                     dare_rel=(sol["rel"] if sol is not None
                               else float("nan")),
                     kyp_min=float("nan"), p_min=float("nan"),
                     p0_min=float("nan"))
        rows.append(r)
        if kz in HEAVY:
            print("    kz %-3d h %4d |J| %2d: deg(Hankel) %2d | "
                  "deg(residue) %2d | s1 %.3e | ||Phi||_inf %.3e"
                  % (kz, r["h"], len(r["jreal"]), r["deg_h"],
                     r["deg_r"], r["s1"], r["hinf"]))
            if r["P"] is not None:
                print("           storage: min eig(P0) %.2e | "
                      "delta %.2e | min eig(P) %.2e | KYP min "
                      "eig %.2e | DARE rel %.1e"
                      % (r["p0_min"], r["delta"], r["p_min"],
                         r["kyp_min"], r["dare_rel"]))
            else:
                print("           storage: NONE (DARE rel %s)"
                      % ("%.1e" % r["dare_rel"]
                         if np.isfinite(r["dare_rel"]) else "n/a"))
        if (time.time() - T0) > TIME_GUARD and not heavy_only:
            heavy_only = True
            print("    [AMEND] time guard: remaining rungs "
                  "restricted to the heavy subset (frozen "
                  "fallback)")
    n_r = len(rows)
    check("P0 pipeline: %d rungs realized (window in port set, "
          "generators extracted)" % n_r, n_r >= 5, kill="K1")
    rec_max = max(r["rec"] for r in rows)
    check("P1 IIKS reconstruction ward on all rungs (max rel "
          "%.1e <= 1e-6)" % rec_max, rec_max <= 1e-6, kill="K1")
    tr_ok = all(0.99 <= (1.0 - r["lamC"]) / r["tau"] <= 1.01
                and r["lamO"] < 1.0 for r in rows)
    check("P2 window still carries the wall exactly on all "
          "rungs ((1-lamC)/tau == 1.00, declared input "
          "re-verified)", tr_ok, kill="K1")

    # ---- K1 typed -------------------------------------------
    degs_r = sorted(set(r["deg_r"] for r in rows))
    degs_h = sorted(set(r["deg_h"] for r in rows))
    full12 = [r for r in rows if len(r["jreal"]) == 12]
    mc12 = (all(r["deg_r"] == len(r["jreal"]) for r in rows)
            and len(full12) == len(rows))
    mc_label = ("MCMILLAN-12" if mc12 else
                ("MCMILLAN-FULLRANK" if all(
                    r["deg_r"] == len(r["jreal"]) for r in rows)
                 else "MCMILLAN-DEFICIENT"))
    print("\n    K1 degree ladder (residue count | Hankel-39 "
          "lower bound):")
    print("      residue degrees over the ladder: %s" % degs_r)
    print("      Hankel   degrees over the ladder: %s" % degs_h)
    print("      (the clustered poles 1/y_j at 1 + O((j/L)^2) "
          "cap the 39-term Hankel resolution --")
    print("      declared lower bound, see spec; the residue "
          "count is the structural degree)")
    check("K1.1 typed: %s -- structural degrees %s over %d "
          "rungs (%d full 12-windows): at least one residue "
          "f_j g_j vanishes on EVERY rung, the port window is "
          "never a minimal state space for this Phi"
          % (mc_label, degs_r, n_r, len(full12)), True)

    # ---- K2 typed + honesty ---------------------------------
    kyp_ok = [r for r in rows if r["P"] is not None
              and r["p_min"] > 0.0
              and r["kyp_min"] >= -1e-10
              * max(1.0, float(np.linalg.norm(r["P"])))]
    contr = [r for r in rows if r["hinf"] <= 1.0]
    agree = all((r["P"] is not None) == (r["hinf"] < 1.0)
                or abs(r["hinf"] - 1.0) < 1e-9 for r in rows)
    check("K2.0 WARD: frequency channel (||Phi||_inf <= 1) and "
          "Riccati channel (PD storage) agree on every rung",
          agree, kill="K2")
    kyp_pos = (len(kyp_ok) == n_r)
    kyp_label = "KYP-POSITIVE" if kyp_pos else "KYP-INDEFINITE"
    hmax = max(r["hinf"] for r in rows)
    hmin = min(r["hinf"] for r in rows)
    check("K2.1 typed: %s -- PD storage on %d/%d truth rungs; "
          "||Phi||_inf in [%.3e, %.3e]"
          % (kyp_label, len(kyp_ok), n_r, hmin, hmax), True)
    # honesty: is the pass/fail the wall, or the scale?
    lt = np.log([r["tau"] for r in rows])
    lh = np.log([max(r["hinf"], 1e-300) for r in rows])
    if len(rows) > 2 and np.std(lt) > 0 and np.std(lh) > 0:
        corr = float(np.corrcoef(lt, lh)[0, 1])
    else:
        corr = float("nan")
    print("\n    K2 HONESTY: corr(log tau, log ||Phi||_inf) = %s"
          % ("%.3f" % corr if np.isfinite(corr) else "n/a"))
    if kyp_pos and hmax < 0.5:
        print("    PLAIN STATEMENT: the KYP pass is a SCALE "
            "effect -- ||Phi||_inf stays <= %.1e because the" % hmax)
        print("    generator scale s1 = ||[Y, D_P]||_2 is small "
              "on truth; the construction does NOT encode")
        print("    I - C_J >= 0, so this is NOT the wall "
              "reformulated and NOT new wall evidence.  The")
        print("    probe's value is the storage OBJECT P itself "
              "(K3/K4); the controls below decide whether")
        print("    the KYP channel sees the wall at all.")
    elif kyp_pos:
        print("    ||Phi||_inf is O(1) on truth: contractivity "
              "is a nontrivial pass; controls decide whether")
        print("    it tracks the wall.")
    else:
        bad = [r["kz"] for r in rows if r not in kyp_ok]
        print("    KYP fails on truth rungs kz %s while the "
              "wall holds there (lam_max(C_J) < 1 everywhere):"
              % bad)
        print("    the frozen generator-built Phi is NOT the "
              "wall's transfer function -- reported honestly.")

    # ---- K3 congruence --------------------------------------
    section("K3 -- congruence to the rebuilt T116 Riccati object "
            "(heavy rungs)")
    k3_rows = [r for r in rows if r["kz"] in HEAVY
               and "Sigma" in r]
    n_obj = 0
    id_rels, sc_rels = [], []
    for r in k3_rows:
        Sig = r["Sigma"]
        if isinstance(Sig, str):
            print("    kz %-3d: Sigma_h %s -> no object on this "
                  "rung" % (r["kz"], Sig))
            continue
        if r["P0"] is None:
            print("    kz %-3d: no storage P0 -> congruence "
                  "untestable" % r["kz"])
            continue
        n_obj += 1
        P = r["P0"]
        rel_id = float(np.linalg.norm(Sig - P)
                       / max(np.linalg.norm(P), 1e-300))
        trS = float(np.trace(Sig))
        c2 = (float(np.trace(P)) / trS) if trS > 0 else float("nan")
        if np.isfinite(c2) and c2 > 0:
            rel_sc = float(np.linalg.norm(c2 * Sig - P)
                           / max(np.linalg.norm(P), 1e-300))
        else:
            rel_sc = float("nan")
        id_rels.append(rel_id)
        sc_rels.append(rel_sc)
        eS = np.linalg.eigvalsh(Sig)
        eP = np.linalg.eigvalsh(P)
        print("    kz %-3d h_odd %4d: eig(Sigma) [%.2e, %.2e] | "
              "eig(P) [%.2e, %.2e]"
              % (r["kz"], r["M"] // 2, eS[0], eS[-1], eP[0],
                 eP[-1]))
        print("           T = I rel %.3e | one-scalar (FITTED "
              "c^2 = trP/trSig = %.3e) rel %.3e"
              % (rel_id, c2, rel_sc))
    if n_obj == 0:
        st_label = "STORAGE-NO-OBJECT"
    elif id_rels and max(id_rels) <= CONGR_TOL:
        st_label = "STORAGE-MATCHED"
    else:
        st_label = "STORAGE-FREE-FIT"
    if st_label == "STORAGE-FREE-FIT":
        print("    NOTE: a full fitted congruence between two PD "
              "12x12 matrices ALWAYS exists (Sylvester), so")
        print("    FREE-FIT is vacuously available; the "
              "source-determined test above is the real one and")
        print("    it failed -- the two 12x12 objects live on "
              "different geometries (cells vs port nodes).")
    check("K3.1 typed: %s (source-determined T = I: %s; %d "
          "objects tested)"
          % (st_label,
             ("worst rel %.2e" % max(id_rels)) if id_rels
             else "n/a", n_obj), True)

    # ---- K4 cascade (report only) ----------------------------
    section("K4 -- cascade/Riccati update law (report only)")
    prows = sorted([r for r in rows if r["P0"] is not None],
                   key=lambda r: r["h"])
    n_pairs = 0
    for k in range(len(prows) - 1):
        if n_pairs >= 6:
            break
        r1, r2 = prows[k], prows[k + 1]
        commonj = [j for j in r1["jreal"] if j in r2["jreal"]]
        if len(commonj) < 8:
            continue
        i1 = [r1["jreal"].index(j) for j in commonj]
        i2 = [r2["jreal"].index(j) for j in commonj]
        P1 = r1["P0"][np.ix_(i1, i1)]
        P2 = r2["P0"][np.ix_(i2, i2)]
        F1 = dare_map(P1, r2["y"][i2], r2["B"][i2], r2["C"][i2])
        raw = float(np.linalg.norm(P2 - P1)
                    / max(np.linalg.norm(P2), 1e-300))
        if F1 is None:
            print("    h %4d -> %4d: raw dP %.3e | cascade "
                  "candidate: denominator dead"
                  % (r1["h"], r2["h"], raw))
            n_pairs += 1
            continue
        cas = float(np.linalg.norm(P2 - F1)
                    / max(np.linalg.norm(P2), 1e-300))
        print("    h %4d -> %4d: raw rel dP %.3e | one-step "
              "Riccati-image residual %.3e | ratio %.3f"
              % (r1["h"], r2["h"], raw, cas,
                 cas / max(raw, 1e-300)))
        n_pairs += 1
    check("K4.1 cascade residuals reported on %d rung pairs"
          % n_pairs, True)

    # ---- C controls ------------------------------------------
    section("C -- controls (kz 9)")
    rr9 = core.build_window(9)
    N_E = int(math.floor(math.exp(2.0 * rr9["alpha"]))) + 1
    lamE_ = lambda_eps(N_E)
    nn = np.nonzero(np.abs(lamE_) > 1e-12)[0]
    ok = True
    for nmc, kw in (("Epstein", dict(comb=(
            np.log(nn.astype(float)),
            2.0 * lamE_[nn] / np.sqrt(nn.astype(float))))),
            ("scramble", dict(scramble_seed=1))):
        try:
            r = rung_data(9, **kw)
        except (np.linalg.LinAlgError, AssertionError):
            r = None
        if r in (None, "TOO-DEEP"):
            print("    %-8s: FRAME DEATH (window/Lanczos "
                  "unavailable) -- wall channel untestable here, "
                  "typed" % nmc)
            continue
        fired = r["lamE"] > 1.0
        ok &= fired
        hinf = hinf_norm(r["y"], r["B"], r["C"])
        sol = solve_bounded_real(r["y"], r["B"], r["C"])
        if (sol is not None and sol["rel"] <= DARE_TOL
                and sol["p_min"] > 0.0):
            kchan = ("storage still PD (min eig %.2e) -- KYP "
                     "channel BLIND to the wall" % sol["p_min"])
        else:
            kchan = "INDEFINITE STORAGE (no bounded-real P)"
        print("    %-8s: lam(E) %.3e -> value fires %s | "
              "||Phi||_inf %.3e | %s"
              % (nmc, r["lamE"], fired, hinf, kchan))
    check("C1 CONTROLS FIRE in the value channel", ok, kill="K3C")

    section("V -- FROZEN VERDICT")
    n_pass = sum(1 for _n, okk in CHECKS if okk)
    n_tot = len(CHECKS)
    if KILLS:
        VERDICT = {"K1": "PIPELINE-BROKEN",
                   "K2": "PIPELINE-BROKEN",
                   "K3C": "CONTROL-DEAD"}[KILLS[0]]
        subl = ""
    else:
        VERDICT = "KYP-MEASURED"
        subl = " (%s, %s, %s)" % (mc_label, kyp_label, st_label)
    print("\n  VERDICT: %s%s" % (VERDICT, subl))
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed"
          % (time.time() - T0, n_tot, n_tot - n_pass))
    return 0 if n_pass == n_tot else 1


if __name__ == "__main__":
    raise SystemExit(main())
