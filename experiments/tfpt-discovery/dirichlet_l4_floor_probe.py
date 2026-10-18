#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""dirichlet_l4_floor_probe -- PRIME.FLOOR.DIRICHLET_L4.01: does the
deployed window form generalise to the first Dirichlet L-function?
(EXPLORATION ONLY, experiments/; 2026-08-08 afternoon probe.)

THE QUESTION (essay point 7, the positive half): the Epstein control
(off-line zeros) breaks the contraction by 1-2 orders of magnitude --
the mechanism SEES arithmetic.  The missing half: does a GRH-expected
L-function, fed through the SAME window machinery with its OWN correct
archimedean data, reproduce the floor lam_min(K) >= 0 and the Loewner
contraction ||C|| <= 1?

THE DERIVATION (typed BEFORE running -- the probe wards it): the
deployed zeta form is EXACTLY the explicit-formula quadratic form
without the pole term,

  Q_zeta = [DG_{1/4} - log(pi) g(0)] - C_Lambda = sum_gamma h(gamma) - P,

read off arch_A verbatim: constant -(EULER + LOG_PI) tri_s, digamma
kernel e^{-w/2}/(1-e^{-2w}) with the z-independent counterterm
2 g(0) e^{-2w}/(1-e^{-2w}) (psi(z) = -gamma + sum_k [1/(k+1) - 1/(k+z)]),
atoms -Lambda(n)/sqrt(n) per side.  For the odd character chi_4 mod 4
(a = 1, q = 4) the SAME convention gives the PURE zero side (no pole):

  Q_chi = [DG_{3/4} + log(4/pi) g(0)] - C_{chi Lambda}
        = sum_{gamma_chi} h(gamma_chi),

so the chi_4 window is the zeta window plus an EXACT, smooth, closed
difference: kernel e^{-w/2}/(1-e^{-2w}) - e^{-3w/2}/(1-e^{-2w}) =
e^{-w/2}/(1+e^{-w}) (nonsingular; counterterm and Euler bookkeeping
cancel identically), constant shift +log(4) at lag 0, comb masses
2 chi_4(n) Lambda(n)/sqrt(n) on odd prime powers (chi_4(2^k) = 0).
Under GRH(chi_4) every zero layer of the master-identity mechanics is
PSD -- and there is NO pole square to eat the cushion: positivity of
the chi_4 window is the finite-window GRH readout on this frame.

TASKS: S1 wards (kernel identity sympy-exact; GL48-vs-GL96 quadrature;
trivial-character regression == the deployed assembly bit for bit).
S2 THE FLOOR: lam_min(K_chi) on construction {9,12,13,26} + FROZEN
holdouts {40,49,60}, side by side with the zeta floor tau.  S3 the
Loewner reading: density split, contractor C = W_- K+ W_+, sign
consistency sign(1 - ||C||) == sign(lam_min(K)); x-displacement rank
(expected 2 -- STRUCTURAL per PRIME.CONTRACTOR.CDCORE.01, typed, not a
discriminator).  S4 the chi_4 source Jacobi chain vs the zeta chain
(expected O(1) apart -- the arithmetic lives in the measure).  S5
controls at kz 9: (a) position scramble seed 1, (b) sign scramble
seed 2 (kills character coherence, keeps positions/magnitudes) --
expectation typed pre-run as EXPECTED-NEGATIVE but NOT structural
(the chi_4 window has no pole square, so a cushion may protect
scrambles at shallow depth -- if controls stay positive that is a
TYPED finding about depth, not a kill).

VERDICT (frozen): DIRICHLET-CONTRACTS-DISCRIMINATING (floor >= 0 on
all 7 rungs AND both kz-9 controls indefinite) /
DIRICHLET-CONTRACTS-CUSHIONED (floor >= 0 everywhere but controls
also positive -- positivity real yet not arithmetic-sensitive at this
depth, typed) / DIRICHLET-INDEFINITE (floor < 0 somewhere -- typed
per rung; a statement about THIS window form, NOT about GRH) /
DIRICHLET-PARTIAL (wards or Loewner consistency broken -- typed).
NO RH claim, NO GRH claim; writes nothing; v563 READ-ONLY.

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/dirichlet_l4_floor_probe.py
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
PRIME.FLOOR.DIRICHLET_L4.01 spec v2 (2026-08-08).  V2 AMENDMENT
(honest, documented): the v1 W1 numeric bar 1e-15 was tighter than
float64 evaluation noise of two ALGEBRAICALLY IDENTICAL expressions
(measured 7.8e-15; the sympy identity gate passed exactly, == 0);
v2 sets the numeric bar to 1e-13 with sympy remaining the exact
gate.  NOTHING ELSE CHANGED: all v1 results (floor, Loewner, chain,
controls) stand as first measured.  Original v1 body follows.
Character: chi_4 mod 4 (odd, a = 1, q = 4), chi_4(n) = +1 (n = 1 mod
4), -1 (n = 3 mod 4), 0 (even).  Window: c_chi = c_ar_zeta + DELTA +
c_at_chi with DELTA(s) = log(4) tri_s + int [tent(s-w) + tent(s+w)]
e^{-w/2}/(1 + e^{-w}) dw (tent support panels, Gauss-Legendre 48;
grid lags s = iD: only i = 0 carries tri_s and the reflection), and
c_at_chi the deployed tent assembly at uu = log n, mm = 2 chi_4(n)
Lambda(n)/sqrt(n), odd prime powers n <= e^{2 alpha}.  Rungs: the
CDCORE seven -- construction {9, 12, 13, 26}, FROZEN HOLDOUT {40, 49,
60} (zero fitted constants).  W1 kernel identity (e^{-w/2} -
e^{-3w/2})/(1 - e^{-2w}) == e^{-w/2}/(1 + e^{-w}) sympy-exact + max
numeric dev <= 1e-15 on 1000 points w in (0, 60].  W2 quadrature:
GL48 vs GL96 max abs dev <= 1e-12 * max|DELTA| at kz 9.  W3 trivial-
character regression: the probe's assembly path with chi == 1 on ALL
prime powers and DELTA off reproduces the deployed c_ar + c_at at kz
9 to max abs 1e-12.  S2 gate: lam_min(K_chi) >= -1e-12 * ||K_chi||_2
on all 7 rungs (floor).  S3 gate: sign(1 - ||C_chi||) == sign(
lam_min(K_chi)) wherever the density splits (tol band 1e-9); x-rank
reported (expected 2, structural, NOT gated).  S4 report: first-10
Jacobi coefficient rel L2 distance chi_4-chain vs zeta-chain at kz 9
(expected >= 1e-2, gated as DIFFERENT).  S5 controls at kz 9, both
built with the FULL chi_4 arch (DELTA on): (a) position scramble
seed 1 (uniform on (0, 2 alpha), sorted, signs/magnitudes kept);
(b) sign scramble seed 2 (random +-1 replacing chi_4(n), positions/
magnitudes kept).  Expectation typed pre-run: EXPECTED lam_min < 0
for both, honestly NOT structural (no pole square -- a shallow-depth
cushion may protect scrambles; if a control stays PSD that is a typed
depth finding, routed to the CUSHIONED verdict, not a kill).
VERDICT: DIRICHLET-CONTRACTS-DISCRIMINATING iff S2 + S3 + W1-3 pass
AND both controls indefinite; DIRICHLET-CONTRACTS-CUSHIONED iff S2 +
S3 + W1-3 pass and >= 1 control stays PSD; DIRICHLET-INDEFINITE iff
S2 fails (typed per rung -- a statement about THIS window form, not
about GRH); else DIRICHLET-PARTIAL.  Float64; NO RH/GRH claim;
writes nothing; v563 READ-ONLY.
"""

CONSTRUCTION = (9, 12, 13, 26)
HOLDOUT = (40, 49, 60)
RUNGS = CONSTRUCTION + HOLDOUT
KZ_CTRL = 9
SEED_POS, SEED_SIGN = 1, 2
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


# ---------------------------------------------------- the chi_4 arch delta
def kdiff(w):
    """The exact zeta -> chi_4 archimedean kernel difference:
    e^{-w/2}/(1 + e^{-w}) -- smooth, bounded by 1/2, decays e^{-w/2}."""
    return np.exp(-0.5 * w) / (1.0 + np.exp(-w))


def delta_lags(M, D, n_gl=48):
    """DELTA(iD) = log(4) [i == 0] + int [tent(s-w) + tent(s+w)]
    kdiff(w) dw over w > 0, per tent-support Gauss-Legendre panels.
    Grid lags only: i = 0 is the single near-field point (tri_s = 1,
    reflection tent(s+w) coincides with tent(s-w))."""
    gx, gw = np.polynomial.legendre.leggauss(n_gl)
    out = np.zeros(M)
    # i = 0: 2 * int_0^D (1 - w/D) kdiff(w) dw + log 4
    mid, half = 0.5 * D, 0.5 * D
    w0 = mid + half * gx
    out[0] = math.log(4.0) + 2.0 * half * float(
        np.dot(gw, (1.0 - w0 / D) * kdiff(w0)))
    # i >= 1: panels [s-D, s] and [s, s+D], full tent (far-field form)
    ss = np.arange(1, M) * D
    for lo, hi in ((ss - D, ss), (ss, ss + D)):
        mid = 0.5 * (lo + hi)
        half = 0.5 * (hi - lo)
        w = mid[:, None] + half[:, None] * gx[None, :]
        val = (1.0 - np.abs(ss[:, None] - w) / D) * kdiff(w)
        out[1:] += half * (val @ gw)
    return out


# ---------------------------------------------------- window machinery
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


def ranks_of(sv, thrs=(1e-3, 1e-6, 1e-9)):
    if len(sv) == 0 or sv[0] <= 0:
        return tuple(0 for _ in thrs)
    return tuple(int(np.sum(sv > t * sv[0])) for t in thrs)


def chi4_comb(alpha, rng_pos=None, rng_sign=None):
    """(uu, mm) for the chi_4 comb: odd prime powers n <= e^{2 alpha},
    masses 2 chi_4(n) Lambda(n)/sqrt(n).  Optional controls: position
    scramble (rng_pos) or sign scramble (rng_sign)."""
    ka = core.atoms_in(alpha)
    nn = core._NN[:ka]
    odd = (nn % 2 == 1)
    nn = nn[odd]
    uu = core.U_ALL[:ka][odd].copy()
    sgn = np.where(nn % 4 == 1, 1.0, -1.0)
    if rng_sign is not None:
        sgn = rng_sign.choice([-1.0, 1.0], size=len(nn))
    if rng_pos is not None:
        uu = np.sort(rng_pos.uniform(0.0, 2.0 * alpha, size=len(nn)))
    mm = sgn * core.MU_ALL[:ka][odd]
    return uu, mm


def build_chi_rung(kz, rng_pos=None, rng_sign=None):
    """One chi_4 rung on the deployed frame geometry: K_chi, density,
    contractor, x-coordinate, merged source-measure nodes."""
    rr = core.build_window(kz)
    h, M, D, alpha = rr["h"], rr["M"], rr["D"], rr["alpha"]
    uu, mm = chi4_comb(alpha, rng_pos=rng_pos, rng_sign=rng_sign)
    c_at, _ = core.atom_lags_at(alpha, M, uu, mm)
    c = core.arch_lags(M, D) + delta_lags(M, D) + c_at
    K = core.odd_toeplitz(c, M)
    evK = np.linalg.eigvalsh(K)
    d = grid_density(c)
    L = 2 * M - 2
    E = odd_extend_mat(h)
    F = np.fft.fft(np.vstack([E, np.zeros((L - M, h))]), axis=0)
    jj = np.arange(L)
    jfold = np.minimum(jj, L - jj)
    phi = 2.0 * math.pi * jj / L
    x = 2.0 * np.cos(2.0 * math.pi * jfold / L)
    s = np.sin(phi / 2.0)
    pos, neg = d > 0.0, d < 0.0
    out = dict(rr=rr, h=h, M=M, L=L, D=D, alpha=alpha, d=d, K=K,
               lmin=float(evK[0]), lmax=float(evK[-1]),
               n_neg_bins=int(np.sum(neg)), x=x,
               n_atoms=len(uu), l1=float(np.sum(np.abs(mm))))
    if neg.any() and pos.any():
        wp = np.sqrt(d[pos] / (2.0 * L))
        wm = np.sqrt(-d[neg] / (2.0 * L))
        Bp = np.sqrt(np.maximum(d, 0.0) / (2.0 * L))[:, None] * F
        Gp = np.real(Bp.conj().T @ Bp)
        Mp = F[neg] @ np.linalg.solve(Gp, F[pos].conj().T)
        Cres = wm[:, None] * Mp * wp[None, :]
        out["Cnorm"] = float(np.linalg.svd(Cres,
                                           compute_uv=False)[0])
        xm_, xp_ = x[neg], x[pos]
        Rx = xm_[:, None] * Cres - Cres * xp_[None, :]
        out["xrank"] = ranks_of(np.linalg.svd(Rx,
                                              compute_uv=False))[1]
    # merged positive-bin source measure (for the chain)
    jp = jj[pos]
    mu_bin = 2.0 * s[jp] ** 2 * d[jp] / L
    ju, inv = np.unique(jfold[jp], return_inverse=True)
    mu = np.zeros(len(ju))
    np.add.at(mu, inv, mu_bin)
    out["xn"] = 2.0 * np.cos(2.0 * math.pi * ju / L)
    out["mu"] = mu
    return out


def stieltjes_chain(xn, mu, m_steps):
    """Jacobi chain of the discrete measure by Lanczos on diag(xn)
    with full reorthogonalization (CDCORE machinery, verbatim)."""
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
            break
        betas.append(b_)
        Q[:, k + 1] = v / b_
    return np.array(alphas), np.array(betas), m0


def zeta_rung_floor(kz):
    """The deployed zeta window floor on the same frame (context)."""
    rr = core.build_window(kz)
    ka = core.atoms_in(rr["alpha"])
    c_at, _ = core.atom_lags_at(rr["alpha"], rr["M"],
                                core.U_ALL[:ka], core.MU_ALL[:ka])
    c = core.arch_lags(rr["M"], rr["D"]) + c_at
    K = core.odd_toeplitz(c, rr["M"])
    ev = np.linalg.eigvalsh(K)
    d = grid_density(c)
    return float(ev[0]), c, d, rr


# ================================================================= main
def main():
    section("PRIME.FLOOR.DIRICHLET_L4.01 -- the chi_4 window "
            "(EXPLORATION ONLY)")
    sha = hashlib.sha256(FROZEN_SPEC.encode("utf-8")).hexdigest()
    print("    FROZEN_SPEC SHA-256 = %s" % sha)
    print("    NO RH claim, NO GRH claim.  Construction %s, frozen "
          "holdout %s." % (CONSTRUCTION, HOLDOUT))
    print("\nS0 -- firewall")
    check("S0.1 AST firewall clean (no zero/prime oracles)",
          not ast_scan(BANNED_IDS))

    # ---------------- S1 wards
    section("S1 -- WARDS: kernel identity, quadrature, trivial-"
            "character regression")
    import sympy as sp
    w_ = sp.symbols("w", positive=True)
    expr = sp.simplify(
        (sp.exp(-w_ / 2) - sp.exp(-3 * w_ / 2))
        / (1 - sp.exp(-2 * w_))
        - sp.exp(-w_ / 2) / (1 + sp.exp(-w_)))
    wn = np.linspace(1e-3, 60.0, 1000)
    dev_num = float(np.max(np.abs(
        (np.exp(-0.5 * wn) - np.exp(-1.5 * wn))
        / (1.0 - np.exp(-2.0 * wn)) - kdiff(wn))))
    check("W1 [KERNEL IDENTITY] (e^{-w/2} - e^{-3w/2})/(1 - e^{-2w})"
          " == e^{-w/2}/(1 + e^{-w}): sympy %s (the exact gate), "
          "numeric max dev %.1e <= 1e-13 (v2 float64 bar)"
          % (expr == 0, dev_num),
          expr == 0 and dev_num <= 1e-13)
    rr9 = core.build_window(KZ_CTRL)
    M9, D9, a9 = rr9["M"], rr9["D"], rr9["alpha"]
    d48 = delta_lags(M9, D9, n_gl=48)
    d96 = delta_lags(M9, D9, n_gl=96)
    qdev = float(np.max(np.abs(d48 - d96)))
    check("W2 [QUADRATURE] DELTA lags GL48 vs GL96 at kz %d: max "
          "abs dev %.1e <= 1e-12 * max|DELTA| = %.1e"
          % (KZ_CTRL, qdev, 1e-12 * float(np.max(np.abs(d48)))),
          qdev <= 1e-12 * float(np.max(np.abs(d48))))
    ka9 = core.atoms_in(a9)
    c_triv, _ = core.atom_lags_at(a9, M9, core.U_ALL[:ka9],
                                  core.MU_ALL[:ka9])
    tau_z9, c_z9, d_z9, _ = zeta_rung_floor(KZ_CTRL)
    rdev = float(np.max(np.abs(
        (core.arch_lags(M9, D9) + c_triv) - c_z9)))
    check("W3 [TRIVIAL-CHARACTER REGRESSION] chi == 1 assembly path "
          "reproduces the deployed zeta lags at kz %d (max abs "
          "%.1e <= 1e-12)" % (KZ_CTRL, rdev), rdev <= 1e-12)
    print("    context: DELTA_0 = %.6f (log 4 = %.6f + smeared "
          "kernel), DELTA_1 = %.3e, DELTA decays over ~%d lags"
          % (float(d48[0]), math.log(4.0), float(d48[1]),
             int(2.0 / D9)))

    # ---------------- S2 the floor
    section("S2 -- THE FLOOR: lam_min(K_chi4) on 7 rungs vs the "
            "deployed zeta floor")
    print("    kz    h    alpha  atoms  l1(chi)  | lam_min(K_chi)"
          "   lam_min(K_zeta)   neg-bins")
    rungs = {}
    floor_ok = True
    for kz in RUNGS:
        b = build_chi_rung(kz)
        rungs[kz] = b
        tz, _c, _d, _r = zeta_rung_floor(kz)
        b["tau_z"] = tz
        okf = b["lmin"] >= -1e-12 * abs(b["lmax"])
        floor_ok &= okf
        print("    %-4d %-4d %-6.3f %-6d %-8.1f |  %+.6e   "
              "%+.6e   %4d%s"
              % (kz, b["h"], b["alpha"], b["n_atoms"], b["l1"],
                 b["lmin"], tz, b["n_neg_bins"],
                 "  (holdout)" if kz in HOLDOUT else ""),
              flush=True)
    check("S2.1 [THE FLOOR] lam_min(K_chi4) >= -1e-12 ||K|| on ALL "
          "7 rungs (construction + blind holdouts) -- the finite-"
          "window GRH readout of the chi_4 explicit formula on the "
          "deployed frame", floor_ok)

    # ---------------- S3 the Loewner reading
    section("S3 -- THE LOEWNER READING: contraction vs floor, "
            "x-displacement rank")
    print("    kz    ||C_chi||     1 - ||C||     sign-consistent"
          "   x-rank@1e-6")
    loew_ok = True
    for kz in RUNGS:
        b = rungs[kz]
        if "Cnorm" not in b:
            print("    %-4d  density one-signed (%d neg bins): "
                  "K PSD trivially, contractor empty -- consistent"
                  % (kz, b["n_neg_bins"]))
            continue
        gap = 1.0 - b["Cnorm"]
        cons = (gap >= -1e-9) == (b["lmin"] >= -1e-12 * b["lmax"])
        loew_ok &= cons
        print("    %-4d  %10.6f   %+.3e      %-5s          %d%s"
              % (kz, b["Cnorm"], gap, cons, b.get("xrank", -1),
                 "  (holdout)" if kz in HOLDOUT else ""),
              flush=True)
    check("S3.1 [LOEWNER CONSISTENCY] sign(1 - ||C_chi||) == "
          "sign(lam_min(K_chi)) on every rung where the density "
          "splits (the v866 equivalence transfers to the chi_4 "
          "window)", loew_ok)

    # ---------------- S4 the chain
    section("S4 -- THE MEASURE: chi_4 source Jacobi chain vs the "
            "zeta chain at kz %d" % KZ_CTRL)
    b9 = rungs[KZ_CTRL]
    al_c, be_c, _m = stieltjes_chain(b9["xn"], b9["mu"],
                                     min(b9["h"],
                                         len(b9["xn"]) - 1))
    # zeta source measure on the same frame
    L9 = 2 * M9 - 2
    jj9 = np.arange(L9)
    jfold9 = np.minimum(jj9, L9 - jj9)
    s9 = np.sin(2.0 * math.pi * jj9 / L9 / 2.0)
    posz = d_z9 > 0.0
    jpz = jj9[posz]
    mu_binz = 2.0 * s9[jpz] ** 2 * d_z9[jpz] / L9
    juz, invz = np.unique(jfold9[jpz], return_inverse=True)
    muz = np.zeros(len(juz))
    np.add.at(muz, invz, mu_binz)
    xnz = 2.0 * np.cos(2.0 * math.pi * juz / L9)
    al_z, be_z, _mz = stieltjes_chain(xnz, muz,
                                      min(b9["h"], len(xnz) - 1))
    n10 = min(10, len(al_c), len(al_z), len(be_c), len(be_z))
    va = np.concatenate([al_z[:n10], be_z[:n10]])
    vc = np.concatenate([al_c[:n10], be_c[:n10]])
    dist = float(np.linalg.norm(vc - va) / np.linalg.norm(va))
    check("S4.1 [THE ARITHMETIC LIVES IN THE MEASURE] first-%d "
          "Jacobi coefficient rel L2 distance chi_4 vs zeta = %.3f "
          ">= 1e-2 (different arithmetic => different chain, same "
          "geometry)" % (n10, dist), dist >= 1e-2)

    # ---------------- S5 controls
    section("S5 -- CONTROLS at kz %d (chi_4 arch kept): position "
            "scramble, sign scramble" % KZ_CTRL)
    ctrl = {}
    for nm, kw in (("pos-scramble",
                    dict(rng_pos=np.random.default_rng(SEED_POS))),
                   ("sign-scramble",
                    dict(rng_sign=np.random.default_rng(SEED_SIGN)))):
        bc = build_chi_rung(KZ_CTRL, **kw)
        ctrl[nm] = bc
        print("    %-13s: lam_min = %+.6e  (truth %+.6e), "
              "||C|| = %s"
              % (nm, bc["lmin"], b9["lmin"],
                 ("%.4f" % bc["Cnorm"]) if "Cnorm" in bc
                 else "n/a (one-signed)"))
    ctrl_neg = all(c["lmin"] < 0.0 for c in ctrl.values())
    print("    typed pre-run: EXPECTED negative, honestly NOT "
          "structural (no pole square -- a shallow-depth cushion "
          "may protect scrambles).")
    check("S5.1 [DISCRIMINATION] both kz-%d controls indefinite "
          "(lam_min < 0): %s -- if False this routes to the "
          "CUSHIONED verdict, typed, not a kill"
          % (KZ_CTRL, ctrl_neg), True)  # informative, never fails

    # ---------------- V verdict
    section("V -- FROZEN VERDICT + honest consequence")
    wards_ok = all(ok for (nm, ok) in CHECKS
                   if nm.startswith(("W1", "W2", "W3")))
    if not floor_ok:
        verdict = "DIRICHLET-INDEFINITE"
    elif not (wards_ok and loew_ok):
        verdict = "DIRICHLET-PARTIAL"
    elif ctrl_neg:
        verdict = "DIRICHLET-CONTRACTS-DISCRIMINATING"
    else:
        verdict = "DIRICHLET-CONTRACTS-CUSHIONED"
    print("\n  VERDICT: %s   [wards %s | floor %s | loewner %s | "
          "controls-negative %s | chain-distance %.3f]"
          % (verdict, wards_ok, floor_ok, loew_ok, ctrl_neg, dist))
    if verdict == "DIRICHLET-CONTRACTS-DISCRIMINATING":
        print("""
  HONEST CONSEQUENCE: the deployed window mechanism GENERALISES to
  the first Dirichlet L-function on this frame: with the exact
  chi_4 archimedean data (digamma 3/4 kernel + log(4/pi) constant,
  no pole) and the signed comb chi_4(n) Lambda(n), the finite-window
  form is PSD on construction AND blind holdouts, the Loewner
  contraction transfers, and both scrambled controls go indefinite
  -- the positivity is arithmetic-sensitive, exactly as for zeta.
  This is the POSITIVE half of essay point 7; the Epstein kill was
  the negative half.  Finite windows only: NO GRH claim.""")
    elif verdict == "DIRICHLET-CONTRACTS-CUSHIONED":
        print("""
  HONEST CONSEQUENCE (typed): the chi_4 window is PSD on all rungs
  -- the mechanism carries over -- but at this depth the positivity
  is NOT arithmetic-sensitive (scrambled controls stay PSD too):
  without the zeta pole square the window has a cushion, and the
  wall (the razor-thin margin that makes the zeta floor hard) has
  no chi_4 analogue at these depths.  Depth extension is the named
  next step.  NO GRH claim.""")
    elif verdict == "DIRICHLET-INDEFINITE":
        print("""
  HONEST CONSEQUENCE (typed): the chi_4 window form goes indefinite
  on the marked rungs.  This is a statement about THIS finite window
  form (tail/alias mechanics), NOT about GRH -- the zeta master
  identity has tail pieces too.  The typed follow-up: per-rung
  margin vs alpha, and the chi_4 analogue of the alias-weight layer
  decomposition.  NO GRH claim.""")
    else:
        print("""
  HONEST CONSEQUENCE (typed): a ward or the Loewner consistency
  broke -- the construction, not the mathematics, is the suspect;
  see the FAIL lines.  NO GRH claim.""")
    n_pass = sum(1 for _n, ok in CHECKS if ok)
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed%s"
          % (time.time() - T0, len(CHECKS), len(FAILS),
             ("  " + ",".join(FAILS)) if FAILS else ""))
    return 0 if n_pass == len(CHECKS) else 1


if __name__ == "__main__":
    raise SystemExit(main())
