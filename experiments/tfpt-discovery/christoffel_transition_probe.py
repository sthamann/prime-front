#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""christoffel_transition_probe -- PRIME.CONTRACTOR.
CHRISTOFFEL.01 (EXPLORATION ONLY, experiments/; round 33
evening, probe 3, after SYLVESTER12-SOURCE-EXACT +
KAPPA-LAW + WELD-WITHOUT-CONTRACTOR, 2026-08-08).

THE QUESTION: does the SourceContractor factor as
C = D_- . U . D_+ with U the Christoffel-normalized CD-kernel
transition between the two node sets and D_+- stable diagonal
attenuations -- so that contractivity = unitarity of U +
||D_+-|| <= 1 + one scalar pole-port condition?

THE ALGEBRA, DERIVED BEFORE RUNNING (frozen predictions):
with K = F G+^{-1} F^H the reproducing kernel of the h-dim
space S = span(F) in ell^2(mu_+), mu_j = d_j^+/2L, and the
Christoffel weights lam_j = 1/K_jj:

  (P1) C = W_- K[neg,pos] W_+ EXACTLY (Sylvester12 W1), hence
       with D_+- := diag(w_i^{+-} sqrt(K_ii)) and
       U := Lam_-^{1/2} K[neg,pos] Lam_+^{1/2} the assembly
       C = D_- U D_+ is an IDENTITY (diagonal rescaling; null
       kernel bins masked and typed).  The ward is numerical
       conditioning; the CONTENT is the factor profiles.
  (P2) VARIATIONAL THEOREM: lam_j >= mu_j on the positive
       support (Christoffel >= point mass), hence
       ||D_+|| <= 1 ALWAYS, and the trace identity
       sum_pos mu_j K_jj = h  (= ||D_+||_F^2).
  (P3) OVERSAMPLING THEOREM: lam_j >= mu_j pointwise gives
       F_+^H Lam_+ F_+ >= G_+ (Loewner), hence EVERY non-null
       row of U has ell^2 norm >= 1 and sigma_max(U) >= 1:
       at oversampled node sets the Christoffel-normalized
       transition CANNOT be a strict contraction -- the
       classical unitary statement is exclusive to
       Gauss-tight nodes.  Frozen expectation: the U factor
       breaches the partial-isometry bar; measure by how
       much, where, and whether D_- compensates.
  (P4) POLYNOMIAL BRIDGE (exact): f_k(th) = e^{-i th k} -
       e^{-i th(2h-1-k)} = e^{-i th(2h-1)/2} * 2i *
       sin((h-k-1/2)th), so S = phase . sin(th/2) .
       P_{h-1}(cos th).  Therefore the kernel Christoffel
       function of S equals the POLYNOMIAL Christoffel
       function of the sin^2-modified source measure
       nu~ = sum mu_j 4 sin^2(th_j/2) delta_{cos th_j}:
       lam_j^S = lam^{poly,nu~}(x_j) / (4 sin^2(th_j/2)).
       The "source Jacobi chain" is the Lanczos chain of nu~;
       the Christoffel-Gauss identity check is machine-grade.
  (P5) SOFTPORT TRANSFER (exact): the top right-singular
       vector of C is u_C = B+[pos] G+^{-1/2} e_soft and
       |<u_C, p_C>| = beta with p_C = B+[pos] v / ||.||
       (frame isometry Y^H Y = G+) -- the kappa-probe pole
       regression transfers verbatim to bin space.

VERDICT (frozen): CHRISTOFFEL-ASSEMBLES /
CHRISTOFFEL-PARTIAL (typed factor) / CHRISTOFFEL-DEAD.
NO RH claim; writes nothing; v563 READ-ONLY.

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/christoffel_transition_probe.py
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
PRIME.CONTRACTOR.CHRISTOFFEL.01 spec v1 (2026-08-08, frozen
before run).  Machinery = displacement_sylvester12 build_rung
verbatim; ladder = ALL frame_a_zones with h <= 900; heavy
rungs {9, 12, 13, 26, 40}; anchors {9, 12, 13}.  Objects per
rung: K = F G+^{-1} F^H via Z = F G+^{-1/2} (eigh route),
Kdiag = row norms^2 of Z, Christoffel lam = 1/Kdiag (null if
Kdiag <= 1e-12 max, count typed), U = Lam_-^{1/2} K[neg,pos]
Lam_+^{1/2}, D_+- = diag(w^{+-} sqrt(Kdiag)).  S1 CLASSICAL
WARDS (gate): W1 trace sum_pos mu K = h rel <= 1e-8 every
rung; W2 variational mu_j K_jj <= 1 + 1e-8 every pos bin,
every rung (== ||D_+|| <= 1); W3 Gauss-Golub-Welsch at
anchors: 40-step Lanczos chain of nu~ (the sin^2(th/2)-
modified source measure, folded pairs aggregated), Gauss
nodes/weights from the tridiagonal, identity w_g *
sum_{m<40} p_m(x_g)^2 = 1 rel <= 1e-8 max over g; W4
POLYNOMIAL BRIDGE at anchors: full h-step chain, lam_j^S *
4 sin^2(th_j/2) * ||Q_row||^2 / w~ = 1 rel <= 1e-6 max over
pos bins with sin^2 > 1e-12 (Lanczos full reorth; early
breakdown typed).  S2 U ANALYSIS: row-norm theorem ward (P3)
min non-null row >= 1 - 1e-8 every rung (gate); per heavy
rung the full sigma(U) census (compute_uv=False): sigma_max,
#sigma > 1+1e-3, #|sigma-1| <= 1e-3, #sigma in (1e-3,
1-1e-3), quantiles; defect locus: Pearson corr(rownorm^2 - 1,
1/(1/4+tau_-^2)) + argmax tau (descriptive); tight-frame
defect Theta = spec(G+^{-1/2} F+^H Lam_+ F+ G+^{-1/2} - I)
at heavy rungs (lam_min >= -1e-8 ward = P3 core).  Ladder
sigma_max lower bound = max(power-iter Rayleigh 120 its seed
0, max row norm); anchors cross-ward power vs SVD rel <=
1e-4.  S3 D PROFILES: ||D_+||, ||D_-|| per rung (ladder
series + heavy tau-profiles); margins typed; the payoff
product ||D_-|| sigma_max(U) ||D_+|| vs ||C|| =
sqrt(1 - lam1(Delta)) vs 1 (census).  S4 ASSEMBLY + SOFT
PORT: W5 assembly ||C_douglas - D_- U D_+||_F/||C||_F <=
1e-8 heavy rungs (gate; = Sylvester12 W1 recoordinatized);
softport: beta per rung from eigh(Delta) + pole w = G+^{1/2}
v/||.||; regressions (gate): beta(kz9) in [0.59, 0.63],
ladder max beta in [0.80, 0.88]; W6 frame transfer at
anchors: |<u_C, p_C>| == beta rel <= 1e-6 with u_C =
B+[pos] G+^{-1/2} e_soft (norm ward 1e-8), p_C = B+[pos]v
normalized; SHARPENING (the 84%->100% question, measured
ladder-wide, both predeclared ports): o1 = |<D+ u_C, D+
p_C>|/norms, o2 = |<D+ u_C, Lam_+^{1/2} F+ v>|/norms; report
beta vs o1, o2 (max over rungs; answered honestly, no gate).
S5 KILLS/CONTROLS at kz 9: Epstein (x^2+5y^2, N =
floor(e^{2 alpha9})+1) and scramble seed 1 through the same
pipeline; bars: lam1(Delta) < 0 (||C|| > 1) for both AND the
triple (||D_-||, sigma_max lb(U), max row(U)) differs from
truth by >= 5 percent relative in >= 1 component for each
control; classical wards W1/W2 must PASS for controls too
(measure-independent algebra; discrimination lives in the
profiles).  VERDICT: DEAD iff any gate ward (W1-W6, row
theorem, beta regression, controls) fails;
CHRISTOFFEL-ASSEMBLES iff all gates pass AND max||D_+|| <=
1+1e-9 AND max||D_-|| <= 1+1e-9 AND sigma_max(U) <= 1+1e-6
on all rungs; CHRISTOFFEL-PARTIAL otherwise (breaching
factors typed with magnitudes; expected: U by P3).  Float64;
budget ~20 min.  NO RH claim; writes nothing.
"""

HEAVY = (9, 12, 13, 26, 40)
ANCHORS = (9, 12, 13)
BETA_KZ9 = (0.59, 0.63)
BETA_MAX = (0.80, 0.88)
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


def build_rung(kz, scramble_seed=None, comb=None):
    """Source data of one rung (displacement_sylvester12
    verbatim + the h-space Delta of the kappa probe)."""
    rr = core.build_window(kz, scramble_seed=scramble_seed)
    h, M, D, alpha = rr["h"], rr["M"], rr["D"], rr["alpha"]
    uu = np.asarray(rr["uu"], float)
    mm = 2.0 * np.asarray(rr["lam"], float)
    if comb is not None:
        uu, mm = comb
    c_at, _ = core.atom_lags_at(alpha, M, uu, mm)
    c_ar = np.asarray(core.arch_lags(M, D), float)
    d = grid_density(c_ar + c_at)
    Ktoe = core.odd_toeplitz(c_ar + c_at, M)
    L = 2 * (2 * h) - 2
    E = odd_extend_mat(h)
    F = np.fft.fft(np.vstack([E, np.zeros((L - M, h))]), axis=0)
    dp = np.sqrt(np.maximum(d, 0.0) / (2.0 * L))
    dm = np.sqrt(np.maximum(-d, 0.0) / (2.0 * L))
    Bp = dp[:, None] * F
    Bm = dm[:, None] * F
    # Douglas contractor via SVD (the reference object)
    U, s, Vh = np.linalg.svd(Bp, full_matrices=False)
    rk = int(np.sum(s > 1e-12 * s[0]))
    Cf = (Bm @ (Vh[:rk].conj().T / s[:rk])) @ U[:, :rk].conj().T
    pos, neg = d > 0.0, d < 0.0
    Cres = Cf[np.ix_(neg, pos)]
    Gp = np.real(Bp.conj().T @ Bp)
    ev, Vp = np.linalg.eigh(Gp)
    Rm = Vp @ np.diag(ev ** -0.5) @ Vp.T
    Rp = Vp @ np.diag(ev ** 0.5) @ Vp.T
    Delta = Rm @ Ktoe @ Rm
    Delta = 0.5 * (Delta + Delta.T)
    jj = np.arange(L)
    tau = np.where(jj <= L // 2, jj, L - jj) * (
        2.0 * math.pi / L) / D
    return dict(rr=rr, d=d, L=L, h=h, D=D, alpha=alpha, F=F,
                Bp=Bp, tau=tau, pos=pos, neg=neg, Cres=Cres,
                wm=dm[neg], wp=dp[pos], tm=tau[neg],
                tp=tau[pos], Gp=Gp, Rm=Rm, Rp=Rp, Delta=Delta,
                evmin=float(ev[0]), evmax=float(ev[-1]))


# ------------------------------------------------ Christoffel machinery
def christoffel_objects(b):
    """Kdiag, Christoffel weights, U, D_+- from one rung."""
    Z = b["F"] @ b["Rm"]                       # L x h, K = Z Z^H
    Kdiag = np.sum(np.abs(Z) ** 2, axis=1)
    tol = 1e-12 * float(np.max(Kdiag))
    null = Kdiag <= tol
    g = np.where(null, 0.0, 1.0 / np.sqrt(
        np.where(null, 1.0, Kdiag)))           # lam^{1/2} = K_jj^{-1/2}
    Knp = Z[b["neg"]] @ Z[b["pos"]].conj().T   # K[neg,pos]
    U = g[b["neg"]][:, None] * Knp * g[b["pos"]][None, :]
    Dm = b["wm"] * np.sqrt(Kdiag[b["neg"]])
    Dp = b["wp"] * np.sqrt(Kdiag[b["pos"]])
    return dict(Z=Z, Kdiag=Kdiag, null=null, U=U, Dm=Dm, Dp=Dp,
                nnull=int(np.sum(null & (b["pos"] | b["neg"]))))


def sigmax_power(A, iters=120, seed=0):
    """Rayleigh lower-bound estimate of sigma_max(A)."""
    rng = np.random.default_rng(seed)
    x = (rng.standard_normal(A.shape[1])
         + 1j * rng.standard_normal(A.shape[1]))
    x /= np.linalg.norm(x)
    for _ in range(iters):
        y = A @ x
        x = A.conj().T @ y
        nx = np.linalg.norm(x)
        if nx == 0.0:
            return 0.0
        x /= nx
    return float(np.linalg.norm(A @ x))        # certified lower bound


def lanczos_chain(x, w, n):
    """Lanczos chain (full reorth, twice) of the discrete
    measure sum_i w_i delta_{x_i}.  Returns (alphas, betas, Q,
    m0, steps)."""
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
    return al[:steps], be[:max(steps - 1, 0)], Q[:, :steps], \
        m0, steps


def folded_measure(b):
    """The sin^2-modified source measure nu~ on x = cos th,
    folded pairs aggregated (pos support)."""
    L, pos = b["L"], b["pos"]
    jj = np.arange(L)[pos]
    th = 2.0 * math.pi * jj / L
    mu = b["d"][pos] / (2.0 * L)
    wt = mu * 4.0 * np.sin(th / 2.0) ** 2
    fold = np.minimum(jj, L - jj)
    uf, inv = np.unique(fold, return_inverse=True)
    wagg = np.zeros(len(uf))
    np.add.at(wagg, inv, wt)
    xs = np.cos(2.0 * math.pi * uf / L)
    # zero-weight folds (theta = 0) kept: harmless in Lanczos,
    # excluded downstream by the sin^2 mask
    return xs, wagg, inv


def gauss_golub_welsch(al, be, m0):
    """Nodes and weights of the Gauss rule of the chain."""
    n = len(al)
    T = np.diag(al)
    if n > 1:
        T += np.diag(be, 1) + np.diag(be, -1)
    evs, V = np.linalg.eigh(T)
    return evs, m0 * V[0] ** 2


def ortho_poly_eval(al, be, m0, xg):
    """p_m(xg) via the three-term recurrence; returns
    sum_{m<n} p_m^2 at each node."""
    n = len(al)
    P = np.zeros((n, len(xg)))
    P[0] = 1.0 / math.sqrt(m0)
    if n > 1:
        P[1] = (xg - al[0]) * P[0] / be[0]
    for k in range(2, n):
        P[k] = ((xg - al[k - 1]) * P[k - 1]
                - be[k - 2] * P[k - 2]) / be[k - 1]
    return np.sum(P ** 2, axis=0)


def softport(b):
    """Pole-port quantities (kappa-probe conventions)."""
    h = b["h"]
    v = np.exp(0.5 * np.arange(h) * b["D"])
    v = v / np.linalg.norm(v)
    w = b["Rp"] @ v
    w = w / np.linalg.norm(w)
    lam, W = np.linalg.eigh(b["Delta"])
    esoft = W[:, 0]
    beta = float(abs(w @ esoft))
    uC = b["Bp"][b["pos"]] @ (b["Rm"] @ esoft)
    pC = b["Bp"][b["pos"]] @ v
    pC = pC / np.linalg.norm(pC)
    return dict(v=v, beta=beta, lam1=float(lam[0]),
                lam2=float(lam[1]), esoft=esoft, uC=uC, pC=pC,
                normC=math.sqrt(max(0.0, 1.0 - float(lam[0]))))


def pearson(a, bvec):
    a = np.asarray(a, float)
    bvec = np.asarray(bvec, float)
    a = a - a.mean()
    bvec = bvec - bvec.mean()
    den = np.linalg.norm(a) * np.linalg.norm(bvec)
    return float(a @ bvec / den) if den > 0 else 0.0


def rung_scalars(b, co, sp):
    """All ladder scalars for one rung."""
    U, Dm, Dp = co["U"], co["Dm"], co["Dp"]
    rown = np.sqrt(np.sum(np.abs(U) ** 2, axis=1))
    nz = rown > 0.0
    mu_pos = b["d"][b["pos"]] / (2.0 * b["L"])
    Kp = co["Kdiag"][b["pos"]]
    trace_rel = abs(float(np.sum(mu_pos * Kp)) - b["h"]) / b["h"]
    var_max = float(np.max(mu_pos * Kp))       # = max D_+^2
    sig_pi = sigmax_power(U)
    sig_lb = max(sig_pi, float(np.max(rown[nz])) if nz.any()
                 else 0.0)
    # sharpening overlaps (P5 exact u_C, no SVD needed)
    uC, pC = sp["uC"], sp["pC"]
    a1, b1 = Dp * uC, Dp * pC
    o1 = (abs(np.vdot(a1, b1))
          / (np.linalg.norm(a1) * np.linalg.norm(b1)))
    gpos = np.where(Kp > 0, 1.0 / np.sqrt(np.where(Kp > 0, Kp,
                                                   1.0)), 0.0)
    pU = gpos * (b["F"][b["pos"]] @ sp["v"])
    o2 = (abs(np.vdot(a1, pU))
          / (np.linalg.norm(a1) * np.linalg.norm(pU)))
    return dict(kz=None, h=b["h"], alpha=b["alpha"],
                normC=sp["normC"], lam1=sp["lam1"],
                maxDp=float(np.max(Dp)), maxDm=float(np.max(Dm)),
                sig=sig_lb, sig_pi=sig_pi,
                rowmin=float(np.min(rown[nz])) if nz.any()
                else float("nan"),
                rowmax=float(np.max(rown[nz])) if nz.any()
                else float("nan"),
                trace_rel=trace_rel, var_max=var_max,
                beta=sp["beta"], o1=float(o1), o2=float(o2),
                nnull=co["nnull"],
                prod=float(np.max(Dm)) * sig_lb
                * float(np.max(Dp)))


# ================================================================= main
def main():
    section("PRIME.CONTRACTOR.CHRISTOFFEL.01 (EXPLORATION ONLY)")
    sha = hashlib.sha256(FROZEN_SPEC.encode("utf-8")).hexdigest()
    print("    FROZEN_SPEC SHA-256 = %s" % sha)
    print("    NO RH claim.")
    print("\nS0 -- firewall")
    check("S0.1 AST firewall clean (no zero/prime oracles)",
          not ast_scan(BANNED_IDS))

    zones = list(core.frame_a_zones())

    # ---------------- single ladder pass
    section("S1-S4 ladder pass (all frame_a_zones, h <= 900)")
    rows = []
    heavy_data = {}
    skipped = []
    print("    kz    h   ||C||   maxD+   maxD-   sig(U)lb "
          "rowmin  rowmax  beta   o1     o2     nnul")
    for kz in zones:
        b = build_rung(kz)
        if b["h"] > 900:
            skipped.append(kz)
            continue
        co = christoffel_objects(b)
        sp = softport(b)
        r = rung_scalars(b, co, sp)
        r["kz"] = kz
        rows.append(r)
        if kz in HEAVY:
            heavy_data[kz] = (b, co, sp)
        print("    %-5d %-4d %.4f  %.4f  %.4f  %.4f   "
              "%.4f  %.4f  %.3f  %.3f  %.3f  %d"
              % (kz, r["h"], r["normC"], r["maxDp"], r["maxDm"],
                 r["sig"], r["rowmin"], r["rowmax"], r["beta"],
                 r["o1"], r["o2"], r["nnull"]), flush=True)
    if skipped:
        print("    skipped (h > 900): %s" % skipped)

    # ---------------- S1 classical wards
    section("S1 -- Christoffel weights: the classical wards")
    tr_max = max(r["trace_rel"] for r in rows)
    check("S1.1 [W1 TRACE] sum_pos mu_j K_jj = h on every rung "
          "(max rel err %.2e)" % tr_max, tr_max <= 1e-8)
    vm = max(r["var_max"] for r in rows)
    check("S1.2 [W2 VARIATIONAL] mu_j K_jj <= 1 everywhere "
          "(max %.12f; == ||D_+||^2 <= 1, theorem P2)" % vm,
          vm <= 1.0 + 1e-8)

    gauss_ok = True
    bridge_ok = True
    for kz in ANCHORS:
        b, co, sp = heavy_data[kz]
        xs, ws, inv = folded_measure(b)
        # W3: 40-step chain, Golub-Welsch identity
        n40 = min(40, int(np.sum(ws > 0.0)) - 1)
        al, be, Q, m0, st = lanczos_chain(xs, ws, n40)
        xg, wg = gauss_golub_welsch(al, be, m0)
        s2 = ortho_poly_eval(al, be, m0, xg)
        gerr = float(np.max(np.abs(wg * s2 - 1.0)))
        gauss_ok &= gerr <= 1e-8
        print("    kz %-3d: chain n=%d (steps %d), Gauss nodes "
              "in [%.4f, %.4f], max|w_g sum p^2 - 1| = %.2e"
              % (kz, n40, st, xg[0], xg[-1], gerr))
        # W4: polynomial bridge, full h-step chain
        h = b["h"]
        nfull = min(h, len(xs))
        alf, bef, Qf, m0f, stf = lanczos_chain(xs, ws, nfull)
        if stf < h:
            print("    kz %-3d: BRIDGE typed -- Lanczos "
                  "breakdown at step %d < h=%d" % (kz, stf, h))
        # chain Christoffel at support points via Q row norms
        wsafe = np.where(ws > 0.0, ws, 1.0)
        rowq = np.sum(Qf ** 2, axis=1)
        lam_poly = np.where(rowq > 0.0, wsafe / np.where(
            rowq > 0.0, rowq, 1.0), np.inf)      # 1/sum p_m^2
        # transport to pos bins
        L, pos = b["L"], b["pos"]
        jj = np.arange(L)[pos]
        th = 2.0 * math.pi * jj / L
        s2th = 4.0 * np.sin(th / 2.0) ** 2
        Kp = co["Kdiag"][pos]
        okm = (s2th > 1e-12) & (Kp > 0)
        # lam_S = 1/Kp must equal lam_poly[inv]/s2th
        rel = np.abs(Kp[okm] * lam_poly[inv][okm]
                     / s2th[okm] - 1.0)
        brerr = float(np.max(rel))
        bridge_ok &= brerr <= 1e-6 and stf == nfull
        print("    kz %-3d: bridge (S = sin(th/2) x P_{h-1}) "
              "max rel err = %.2e over %d bins"
              % (kz, brerr, int(np.sum(okm))))
    check("S1.3 [W3 GAUSS] Golub-Welsch identity w_g = "
          "1/sum p_m(x_g)^2 at the 40-step source Jacobi "
          "chain, anchors", gauss_ok)
    check("S1.4 [W4 BRIDGE] kernel Christoffel == polynomial "
          "Christoffel of nu~ / 4sin^2(th/2), full h-chain, "
          "anchors", bridge_ok)

    # ---------------- S2 the U analysis
    section("S2 -- the normalized transition U")
    rowmin_all = min(r["rowmin"] for r in rows)
    check("S2.1 [P3 ROW THEOREM] every non-null row of U has "
          "norm >= 1 on every rung (min %.9f)" % rowmin_all,
          rowmin_all >= 1.0 - 1e-8)
    sig_cross_ok = True
    print("    heavy sigma(U) census:")
    print("    kz    sigmax  #>1+1e-3  #|s-1|<=1e-3  "
          "#mid  q50     q90     rank")
    for kz in HEAVY:
        b, co, sp = heavy_data[kz]
        sv = np.linalg.svd(co["U"], compute_uv=False)
        r = next(rr for rr in rows if rr["kz"] == kz)
        if kz in ANCHORS:
            sig_cross_ok &= abs(r["sig_pi"] - sv[0]) \
                <= 1e-4 * sv[0]
        rk = int(np.sum(sv > 1e-12 * sv[0]))
        nab = int(np.sum(sv > 1.0 + 1e-3))
        nat = int(np.sum(np.abs(sv - 1.0) <= 1e-3))
        nmid = int(np.sum((sv > 1e-3) & (sv < 1.0 - 1e-3)))
        svr = sv[:rk]
        print("    %-5d %.4f  %-8d  %-12d  %-4d %.4f  %.4f"
              "  %d" % (kz, sv[0], nab, nat, nmid,
                        float(np.quantile(svr, 0.50)),
                        float(np.quantile(svr, 0.90)), rk))
        r["sig"] = max(r["sig"], float(sv[0]))
        r["svcensus"] = (nab, nat, nmid, rk)
        # defect locus
        rown2 = np.sum(np.abs(co["U"]) ** 2, axis=1)
        nzm = rown2 > 0
        cau = 1.0 / (0.25 + b["tm"] ** 2)
        cr = pearson(rown2[nzm] - 1.0, cau[nzm])
        imx = int(np.argmax(rown2))
        # tight-frame defect Theta (P3 core)
        mu_pos = b["d"][b["pos"]] / (2.0 * b["L"])
        Kp = co["Kdiag"][b["pos"]]
        lamp = np.where(Kp > 0, 1.0 / np.where(Kp > 0, Kp, 1.0),
                        0.0)
        Fp = b["F"][b["pos"]]
        Gl = Fp.conj().T @ (lamp[:, None] * Fp)
        Th = b["Rm"] @ np.real(Gl) @ b["Rm"] - np.eye(b["h"])
        tev = np.linalg.eigvalsh(0.5 * (Th + Th.T))
        print("          defect locus: corr(row^2-1, Cauchy) = "
              "%+.3f, argmax at tau = %.3f (row %.4f); "
              "Theta spec [%+.2e, %.3f]"
              % (cr, b["tm"][imx], math.sqrt(rown2[imx]),
                 float(tev[0]), float(tev[-1])))
        check("S2.h kz %d tight-frame defect Theta >= 0 "
              "(lam_min %.2e, P3 Loewner)" % (kz, tev[0]),
              tev[0] >= -1e-8)
    check("S2.2 power-iteration sigma_max cross-ward vs SVD at "
          "anchors (rel <= 1e-4)", sig_cross_ok)
    sig_all = max(r["sig"] for r in rows)
    u_ok = sig_all <= 1.0 + 1e-6
    print("    ladder: sigma_max(U) lower bounds in [%.4f, "
          "%.4f]; partial-unitarity bar (<= 1+1e-6): %s"
          % (min(r["sig"] for r in rows), sig_all,
             "MET" if u_ok else "BREACHED"))

    # ---------------- S3 the D profiles + payoff product
    section("S3 -- the diagonal attenuations D_+-")
    dp_all = max(r["maxDp"] for r in rows)
    dm_all = max(r["maxDm"] for r in rows)
    dplus_ok = dp_all <= 1.0 + 1e-9
    dminus_ok = dm_all <= 1.0 + 1e-9
    print("    ||D_+|| over ladder: max %.6f (theorem: <= 1); "
          "margin min %.4f" % (dp_all, 1.0 - dp_all))
    print("    ||D_-|| over ladder: max %.6f (measured); "
          "%s" % (dm_all,
                  "CONTRACTIVE with margin %.4f" % (1.0 - dm_all)
                  if dminus_ok else
                  "EXCEEDS 1 by %.2e" % (dm_all - 1.0)))
    for kz in HEAVY:
        b, co, sp = heavy_data[kz]
        idm = int(np.argmax(co["Dm"]))
        idp = int(np.argmax(co["Dp"]))
        print("    kz %-3d: max D_- = %.4f at tau = %.3f; "
              "max D_+ = %.4f at tau = %.3f"
              % (kz, co["Dm"][idm], b["tm"][idm],
                 co["Dp"][idp], b["tp"][idp]))
    ncert = sum(1 for r in rows if r["maxDm"] * r["sig"]
                * r["maxDp"] <= 1.0)
    worst = max(rows, key=lambda r: r["prod"])
    print("    payoff product ||D_-|| sig(U) ||D_+|| <= 1 on "
          "%d/%d rungs (max product %.4f at kz %d; ||C|| there "
          "%.4f)" % (ncert, len(rows), worst["prod"],
                     worst["kz"], worst["normC"]))

    # ---------------- S4 assembly + soft port
    section("S4 -- assembly C = D_- U D_+ and the soft port")
    asm_max = 0.0
    for kz in HEAVY:
        b, co, sp = heavy_data[kz]
        Casm = co["Dm"][:, None] * co["U"] * co["Dp"][None, :]
        rel = float(np.linalg.norm(Casm - b["Cres"])
                    / np.linalg.norm(b["Cres"]))
        asm_max = max(asm_max, rel)
        print("    kz %-3d: ||C - D_- U D_+||_F/||C||_F = %.2e"
              % (kz, rel))
    assembly_ok = check(
        "S4.1 [W5 ASSEMBLY] rel residual <= 1e-8 on heavy "
        "rungs (max %.2e; identity P1, ward = conditioning)"
        % asm_max, asm_max <= 1e-8)

    transfer_ok = True
    for kz in ANCHORS:
        b, co, sp = heavy_data[kz]
        nrm = float(np.linalg.norm(sp["uC"]))
        sv, svec = np.linalg.svd(b["Cres"], compute_uv=True)[1:]
        # frame prediction: |<u_C, p_C>| == beta
        ov = float(abs(np.vdot(sp["uC"], sp["pC"]))) / nrm
        rel = abs(ov - sp["beta"]) / max(sp["beta"], 1e-12)
        # SVD cross-ward: sigma_max(C) vs sqrt(1 - lam1)
        svrel = abs(sv[0] - sp["normC"]) / sp["normC"]
        vtop = svec[0].conj()
        ovv = float(abs(np.vdot(vtop, sp["uC"] / nrm)))
        transfer_ok &= (abs(nrm - 1.0) <= 1e-8 and rel <= 1e-6
                        and svrel <= 1e-8)
        print("    kz %-3d: ||u_C|| = %.10f, |<u_C,p_C>| = "
              "%.6f vs beta = %.6f (rel %.1e); sigmax(C) rel "
              "%.1e; |<v_svd, u_C>| = %.6f (gap lam2-lam1 = "
              "%.2e)" % (kz, nrm, ov, sp["beta"], rel, svrel,
                         ovv, sp["lam2"] - sp["lam1"]))
    check("S4.2 [W6 FRAME TRANSFER] |<u_C, p_C>| == beta and "
          "sigma_max(C) == sqrt(1-lam1) at anchors (P5 exact)",
          transfer_ok)

    b9 = next(r for r in rows if r["kz"] == 9)
    bmax = max(rows, key=lambda r: r["beta"])
    beta_ok = (BETA_KZ9[0] <= b9["beta"] <= BETA_KZ9[1]
               and BETA_MAX[0] <= bmax["beta"] <= BETA_MAX[1])
    check("S4.3 [SOFTPORT 84%% REGRESSION] beta(kz9) = %.4f in "
          "[%.2f, %.2f]; ladder max = %.4f at kz %d in "
          "[%.2f, %.2f]" % (b9["beta"], *BETA_KZ9,
                            bmax["beta"], bmax["kz"], *BETA_MAX),
          beta_ok)
    o1max = max(rows, key=lambda r: r["o1"])
    o2max = max(rows, key=lambda r: r["o2"])
    print("    SHARPENING (84%% -> 100%%?): pole share of the "
          "soft mode, ladder max:")
    print("      beta (raw C coords)      : %.4f (kz %d)"
          % (bmax["beta"], bmax["kz"]))
    print("      o1 (D_+-transported)     : %.4f (kz %d)"
          % (o1max["o1"], o1max["kz"]))
    print("      o2 (kernel-normalized)   : %.4f (kz %d)"
          % (o2max["o2"], o2max["kz"]))
    print("      mean over ladder: beta %.4f, o1 %.4f, o2 %.4f"
          % (float(np.mean([r["beta"] for r in rows])),
             float(np.mean([r["o1"] for r in rows])),
             float(np.mean([r["o2"] for r in rows]))))

    # ---------------- S5 kills / controls
    section("S5 -- kills and controls at kz 9 "
            "(Epstein x^2+5y^2, scramble seed 1)")
    rtruth = next(r for r in rows if r["kz"] == 9)
    triple_t = np.array([rtruth["maxDm"], rtruth["sig"],
                         rtruth["rowmax"]])
    rr9 = core.build_window(9)
    N_E = int(math.floor(math.exp(2.0 * rr9["alpha"]))) + 1
    lamE = lambda_eps(N_E)
    nn = np.nonzero(np.abs(lamE) > 1e-12)[0]
    ctrl_ok = True
    ctrl_classical_ok = True
    for nmc, kw in (("Epstein", dict(comb=(
            np.log(nn.astype(float)),
            2.0 * lamE[nn] / np.sqrt(nn.astype(float))))),
            ("scramble", dict(scramble_seed=1))):
        bc = build_rung(9, **kw)
        cc = christoffel_objects(bc)
        sc = softport(bc)
        rc = rung_scalars(bc, cc, sc)
        svc = np.linalg.svd(cc["U"], compute_uv=False)
        sigc = float(svc[0])
        triple_c = np.array([rc["maxDm"], sigc, rc["rowmax"]])
        reldiff = np.abs(triple_c - triple_t) / triple_t
        sign_break = sc["lam1"] < 0.0
        ctrl_ok &= sign_break and bool(np.max(reldiff) >= 0.05)
        ctrl_classical_ok &= (rc["trace_rel"] <= 1e-8
                              and rc["var_max"] <= 1.0 + 1e-8
                              and rc["rowmin"] >= 1.0 - 1e-8)
        print("    %-8s: lam1(Delta) = %+.4e (||C|| = %.4f), "
              "triple (maxD-, sig U, maxrow) = (%.4f, %.4f, "
              "%.4f) vs truth (%.4f, %.4f, %.4f), max rel "
              "diff %.1f%%"
              % (nmc, sc["lam1"],
                 math.sqrt(max(0.0, 1.0 - sc["lam1"])),
                 *triple_c, *triple_t,
                 100.0 * float(np.max(reldiff))))
    check("S5.1 [KILL GUARD] both controls break the sign "
          "(lam1 < 0, ||C|| > 1) AND their (D_-, sigma, "
          "rowmax) profile differs from truth by >= 5%",
          ctrl_ok)
    check("S5.2 [CONTROL ALGEBRA] W1/W2/row-theorem hold for "
          "the controls too (measure-independent identities; "
          "discrimination lives in the profiles)",
          ctrl_classical_ok)

    # ---------------- verdict
    section("V -- FROZEN VERDICT + honest consequence")
    gates_ok = (tr_max <= 1e-8 and vm <= 1.0 + 1e-8
                and gauss_ok and bridge_ok
                and rowmin_all >= 1.0 - 1e-8 and sig_cross_ok
                and assembly_ok and transfer_ok and beta_ok
                and ctrl_ok and ctrl_classical_ok)
    if not gates_ok:
        verdict = "CHRISTOFFEL-DEAD"
        typed = "gate wards failed: %s" % sorted(set(FAILS))
    elif dplus_ok and dminus_ok and u_ok:
        verdict = "CHRISTOFFEL-ASSEMBLES"
        typed = ("contractivity = unitarity defect of U + "
                 "||D_+-|| <= 1 + the scalar pole port")
    else:
        verdict = "CHRISTOFFEL-PARTIAL"
        bad = []
        if not u_ok:
            bad.append("U: sigma_max = %.4f > 1 (theorem P3: "
                       "rows >= 1 at oversampled nodes; max row "
                       "%.4f)" % (sig_all,
                                  max(r["rowmax"] for r in rows)))
        if not dminus_ok:
            bad.append("D_-: max %.6f > 1" % dm_all)
        if not dplus_ok:
            bad.append("D_+: max %.6f > 1 (!! theorem breach)"
                       % dp_all)
        typed = "; ".join(bad)
    print("\n  VERDICT: %s" % verdict)
    print("  typed: %s" % typed)
    npass = sum(1 for _, ok in CHECKS if ok)
    print("\n  checks: %d/%d passed; elapsed %.1f s"
          % (npass, len(CHECKS), time.time() - T0))
    print("""
HONEST CONSEQUENCE (no RH claim):
  the assembly C = D_- U D_+ is an exact identity (P1) -- the
  factorization RELOCATES the contraction question, it does
  not decide it.  What the run decides: whether the three
  factors carry the load as the architecture hoped (U
  partially unitary, D_+- contractive, defect at the pole
  port).  The variational theorem P2 gives ||D_+|| <= 1 for
  free; the oversampling theorem P3 forces U's rows >= 1, so
  the classical unitary transition is exclusive to
  Gauss-tight node sets -- the measured question is the SIZE
  of the breach and whether D_- absorbs it.  EXPLORATION
  ONLY; nothing here enters verification/ or the papers.""")
    return verdict


if __name__ == "__main__":
    main()
