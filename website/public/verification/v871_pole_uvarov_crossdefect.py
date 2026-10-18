#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""v871 -- PRIME.JACOBI.POLE.UVAROV.01 + PRIME.GAUSS.CROSSDEFECT.01: the measure-relation closure (two honest kills with typed residues) -- NONE of the three classical spectral transformations (Uvarov mass insertion, Christoffel multiplication, Geronimus division) relates the two channel measures mu_-, mu_+ exactly or at fixed small rank at the source pole x_pole = 2 cosh(D/2) (the machinery itself warded exact at 9.2e-16 on the synthetic example: the kills are findings, not bugs; Sherman-Morrison == direct wherever lambda >= 0 at <= 8e-15), with the TYPED RESIDUE registered: Geronimus with SMALL NEGATIVE MASS (lambda in [-0.140, -0.017], per-rung source formula, never tuned) is uniformly closest -- Weyl residual 3.5-8.1 percent across construction AND blind holdouts kz 40/49/60, NON-GROWING (holdout/construction ratio 0.97) and DISCRIMINATING (Epstein residual ratio 2.58, scramble lambda rel dev 2.14: the transformation carries arithmetic, not window geometry) -- but it misses the frozen 5-percent bar and no lambda(D) law exists (Spearman +0.61, log-log slope -1.28) -- and the companion audit closes the OPERATOR-side escape: the Gauss-frame co-isometry defect is DIFFUSE -- full-rank (residual rank@1e-2 up to 530 = ALL of r_-), growing LINEARLY with h (first/last-third means 119.6 -> 405.1, x3.39, Pearson +0.996), pole removal changes NOTHING (top-mode pole overlap mostly 0.002-0.1), and the closest-co-isometry split U_0 + R assembles exactly (U_0 U_0^H = I at 1.5e-13; base term I - U_0^H D_-^2 U_0 PSD BY THEOREM, lam_min >= +0.011) with the bracket O(1) at near-full rank (0.72-0.89, rank ~= r_-): NO finite-matrix compensation exists at this ingredient list, ONE module from two probes (7 + 11 checks, zero fails, verdicts POLE-TRANSFORM-DEAD + CROSSDEFECT-DIFFUSE; discovery probes jacobi_pole_uvarov_probe.py and gauss_crossdefect_probe.py, 2026-08-08, re-run identically at promotion, embedded BYTE-EXACT and executed verbatim, ~21 s).  PART A, THE POLE TRANSFORMATIONS: the two channel measures in x are built and warded (nu_+ merge reproduces the cdcore measure at machine precision; 40-column recurrence orthonormality <= 1e-6 for BOTH channel chains on every rung; mass ratios mu_-/mu_+ = 0.06-0.10), the pole point x_pole - 2 ~ D^2/4 is typed, and the census is decisive: Uvarov chain/Weyl/Gauss/kernel residuals 0.13-0.99, Christoffel 0.11-245, Geronimus Weyl 0.035-0.081 -- FULL and PARTIAL verdicts False for all three; the suspiciously-well-fitting hypothesis (v864's rank-2 Cauchy exclusion extended to ALL classical one-pole transformations) dies at the functional level.  PART B, THE DEFECT ANATOMY: the sign structure is exact (E_L traceless at 1.0e-13 -- over-normalization == loss in trace; the two-route kernel column ward at x_pole 2.9e-13; tau preserved every rung), the eigenvalue split is measured (n_+/n_- ~ r_-/3 vs 2r_-/3; |eig|_max 0.93-1.30), the top modes are NOT edge artifacts (edge-node mass 13-32 percent) and are STABLE (std(o_pole) = 0.123 over the last 10 rungs -- the wild-rotation kill does not fire), and the bracket census closes the finite-rank hope: lam_min(Delta_pos) == tau on the heavy rungs (the Feshbach consistency 1.675e-4/7.6e-5/7.8e-5/2.8e-6/6.7e-7 == tau to all digits).  The controls break sign AND structure on both legs (defect triples differ 907/2434 percent).  HONEST CONSEQUENCE: with the classical measure relations and the finite-matrix compensations both closed, the named plan B is the Pruefer/Cotlar phase route -- registered as the FROZEN preregistration PRIME.PRUEFER.COMPENSATION.01 (committed with this round, NOT run).  NO RH claim.  Python-only per GATE.WOLFRAM.02.

PROVENANCE: discovery probes jacobi_pole_uvarov_probe.py (7 checks, 0
failed, verdict POLE-TRANSFORM-DEAD, spec SHA
295792a85e2ddaaa39df96a5c500f2e0f88b8f8f6e176e8aeffa603ba5f35b56) and
gauss_crossdefect_probe.py (11/11, verdict CROSSDEFECT-DIFFUSE, spec
SHA 6b523ef5913a720e3ffb1a78e8b6c25a6686883834649b55b96998ce9d27965c),
2026-08-08, re-run identically at promotion.  ROUND-31 EMBEDDING
CONVENTION: frozen sources embedded BYTE-EXACT and executed verbatim in
isolated namespaces; printed spec SHAs reproduce; byte-equality ward vs
experiments/tfpt-discovery/ inside the pattern gates.  The uvarov probe
imports cdcore_probe.py (gated in v869) READ-ONLY -- not re-gated here.

FIREWALL: no zeros, no prime-table oracles (AST firewalls inside the
probes); construction rungs {9, 12, 13, 26} with FROZEN blind holdouts
{40, 49, 60} (uvarov) / all 42 reachable rungs h <= 900 (crossdefect);
the transformation machinery warded on synthetics BEFORE deployment;
controls MUST-FIRE and do.  NO RH claim.
"""

import contextlib
import io
import math
import os
import re
import sys
import time
import types

_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)

# ------------- frozen probe source jacobi_pole_uvarov_probe (embedded BYTE-EXACT, raw string)
_SRC_0 = r'''
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""jacobi_pole_uvarov_probe -- PRIME.JACOBI.POLE.UVAROV.01: is
mu_- a classical spectral transformation of mu_+ at the source
pole?  (EXPLORATION ONLY, experiments/; round 33 evening probe
A, after CDCORE-IDENTIFIED, 2026-08-08.)

THE HYPOTHESIS: the two channel measures of the CD
identification -- mu_+- = sum over sign-split density bins of
[2 sin^2(phi/2) |d(phi)| / L] delta at x = 2 cos(D tau) --
differ by a rank-one/small-rank spectral transformation at the
EXTERIOR pole x_pole = 2 cosh(D/2) (the explicit-formula pole
tau = +-i/2 through x = 2 cos(D tau), OUTSIDE the band [-2,2]).
Candidates: UVAROV (add lambda delta_{x_p}), CHRISTOFFEL
(multiply by (x_p - x)), GERONIMUS (divide by (x_p - x) +
compensating mass).

TYPED BEFORE RUNNING (the honest frame): the two atomic
supports are DISJOINT interleaved band sets, so a literal
measure identity is impossible; the meaningful (and frozen)
sense of "equal" is the FUNCTIONAL battery -- normalized
moments, Jacobi chains (mass-invariant), Weyl functions on a
predeclared exterior grid, Gauss-12 nodes + Christoffel
weights, and the degree-12 kernels (Sherman-Morrison update
for Uvarov, warded internally where lambda >= 0).  All
lambdas are SOURCE-DETERMINED by first-moment matching (the
formulas typed below); zero fitted constants, so the frozen
holdouts are the recipe applied blind.

  lambda_UVAROV    = (m1- - m1+) / (x_p - m1-),
  CHRISTOFFEL      : no parameter (normalization x_p - m1+),
  lambda_GERONIMUS = (m1- I0 - I1) / (x_p - m1-),
      I0 = int dnu+/(x_p - x),  I1 = int x dnu+/(x_p - x),

with nu_+- the mass-normalized measures and m1 their first
moments (all source data: the signed window density).

VERDICT (frozen): UVAROV-EXACT / CHRISTOFFEL-EXACT /
GERONIMUS-EXACT (machine battery + discrimination) /
POLE-TRANSFORM-PARTIAL (window-independent small residual +
fixed small correction rank, typed) / POLE-TRANSFORM-DEAD
(growing correction, typed -- the Pruefer/Cotlar plan B
activates).  NO RH claim; writes nothing; v563 + cdcore
READ-ONLY.

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/jacobi_pole_uvarov_probe.py
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
import cdcore_probe as cd                  # noqa: E402  (READ-ONLY)

FROZEN_SPEC = """\
PRIME.JACOBI.POLE.UVAROV.01 spec v1 (2026-08-08, frozen before
run).  Construction {9, 12, 13, 26}; FROZEN HOLDOUT
{40, 49, 60} (lambda formulas are per-rung source expressions,
zero tuned constants).  x_pole = 2 cosh(D/2).  Measures:
mass-normalized nu_+- from the sign-split density (cdcore
merge).  S0 machinery ward (synthetic, deterministic 50-atom
measure, pole 2.5, lambda 0.3): Uvarov/Christoffel/Geronimus
Weyl identities and the Sherman-Morrison degree-8 kernel
update all rel <= 1e-10.  S1 wards: nu_+ merge == cdcore mu
(machine); chain orthonormality (40 cols) <= 1e-6 both sides;
cdcore regression x-rank@1e-6 == 2 at kz 9.  Battery (per
transformation, per rung): normalized moments k <= 16 (dev_k
= |mT_k - m-_k|/(1 + |m-_k|), max); Jacobi chain depth 20
(max abs dev, skipped + typed if the transformed weights are
signed); Weyl on frozen grid Z = {2.5i, 1+1.5i, -1+1.5i,
3+0.5i, -3+0.5i, 4i} (max rel dev -- THE ranking scalar);
Gauss-12 nodes (max abs) + weights (max abs); degree-12
kernel on 25 Chebyshev points (rel Frobenius) with
Sherman-Morrison for Uvarov (internal SM-vs-direct ward <=
1e-8 where lambda >= 0); correction rank = #sv(K- - K_T) >
1e-2 sigma1(K-).  Classification: FULL = every battery
component <= 1e-8 on all 7 rungs; PARTIAL = weyl_res <= 0.05
on all 7 rungs AND max(holdout res)/max(construction res) <=
1.5 AND correction rank <= 3 everywhere; else the
transformation is dead.  Best = smallest mean construction
weyl_res.  Discrimination at kz 9 (best transformation):
Epstein (x^2+5y^2) + scramble seed 1 must have weyl_res >=
2x truth OR |lambda - lambda_truth| rel >= 0.5; if
non-discriminating, *-EXACT is demoted to PARTIAL with the
relation typed GEOMETRIC.  lambda(D) law reported fit-free
(Spearman, log-log slope vs D).  VERDICT enum as header.
Float64; certified budgets = the stated wards.  NO RH claim;
writes nothing.
"""

CONSTRUCTION = (9, 12, 13, 26)
HOLDOUT = (40, 49, 60)
RUNGS = CONSTRUCTION + HOLDOUT
Z_GRID = np.array([2.5j, 1 + 1.5j, -1 + 1.5j, 3 + 0.5j,
                   -3 + 0.5j, 4j])
K_MOM = 16
K_CHAIN = 20
K_GAUSS = 12
K_KER = 12
X_EVAL = 2.0 * np.cos(math.pi * (2 * np.arange(25) + 1) / 50.0)
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


# ------------------------------------------------ measure utilities
def merge_side(b, sign):
    """Merged x-measure of one channel side (cdcore merge,
    source data only)."""
    L, s, d = b["L"], b["s"], b["d"]
    jj = np.arange(L)
    jfold = np.minimum(jj, L - jj)
    sel = d > 0.0 if sign > 0 else d < 0.0
    jn = jj[sel]
    mu_bin = 2.0 * s[jn] ** 2 * np.abs(d[jn]) / L
    ju, inv = np.unique(jfold[jn], return_inverse=True)
    mu = np.zeros(len(ju))
    np.add.at(mu, inv, mu_bin)
    xn = 2.0 * np.cos(2.0 * math.pi * ju / L)
    return xn, mu


def weyl(xs, ws, z):
    """m(z) = int dmu / (x - z) for a discrete (possibly
    signed) measure."""
    return np.array([np.sum(ws / (xs - zz)) for zz in z])


def moments(xs, ws, kmax):
    out = [float(np.sum(ws))]
    p = ws.copy()
    for _k in range(kmax):
        p = p * xs
        out.append(float(np.sum(p)))
    return np.array(out)


def poly_mat(al, be, m0, xs, n):
    """Orthonormal p_0..p_{n-1} at xs (chain from
    cd.stieltjes_chain conventions)."""
    P = np.zeros((len(xs), n))
    P[:, 0] = 1.0 / math.sqrt(m0)
    if n > 1:
        P[:, 1] = (xs - al[0]) * P[:, 0] / be[0]
    for k in range(1, n - 1):
        P[:, k + 1] = ((xs - al[k]) * P[:, k]
                       - be[k - 1] * P[:, k - 1]) / be[k]
    return P


def gauss12(al, be, m0):
    J = np.diag(al[:K_GAUSS]) \
        + np.diag(be[:K_GAUSS - 1], 1) \
        + np.diag(be[:K_GAUSS - 1], -1)
    ev, V = np.linalg.eigh(J)
    return ev, m0 * V[0] ** 2


def kernel_grid(al, be, m0, xs):
    P = poly_mat(al, be, m0, xs, K_KER)
    return P @ P.T, P


def transformed_atoms(name, xs, ws, xp, lam):
    """Transformed measure as atoms (possibly signed), already
    mass-normalized.  Source-only."""
    if name == "uvarov":
        xa = np.concatenate([xs, [xp]])
        wa = np.concatenate([ws, [lam]]) / (1.0 + lam)
        return xa, wa
    if name == "christoffel":
        wa = (xp - xs) * ws
        return xs, wa / np.sum(wa)
    # geronimus
    xa = np.concatenate([xs, [xp]])
    wa = np.concatenate([ws / (xp - xs), [lam]])
    return xa, wa / np.sum(wa)


def battery(name, xs_p, ws_p, xs_m, ws_m, chain_m, xp, lam,
            Kmin_grid):
    """The frozen functional battery: transformed nu_+ vs
    nu_-.  Returns component dict + internal SM ward."""
    xa, wa = transformed_atoms(name, xs_p, ws_p, xp, lam)
    signed = bool(np.min(wa) < 0.0)
    out = dict(signed=signed, sm_ward=None)
    # moments
    mT = moments(xa, wa, K_MOM)
    mM = moments(xs_m, ws_m, K_MOM)
    out["mom"] = float(np.max(np.abs(mT - mM)
                              / (1.0 + np.abs(mM))))
    # Weyl (THE ranking scalar)
    wT = weyl(xa, wa, Z_GRID)
    wM = weyl(xs_m, ws_m, Z_GRID)
    out["weyl"] = float(np.max(np.abs(wT - wM)
                               / np.abs(wM)))
    alm, bem, m0m = chain_m
    if not signed:
        alt, bet, m0t, brk = cd.stieltjes_chain(
            xa, wa, min(K_CHAIN + 2, len(xa) - 1))
        nn = min(K_CHAIN, len(alt) - 1, len(alm) - 1,
                 len(bet), len(bem))
        out["chain"] = float(max(
            np.max(np.abs(alt[:nn] - alm[:nn])),
            np.max(np.abs(bet[:nn] - bem[:nn]))))
        nT, wgT = gauss12(alt, bet, m0t)
        nM, wgM = gauss12(alm, bem, m0m)
        out["gauss_n"] = float(np.max(np.abs(nT - nM)))
        out["gauss_w"] = float(np.max(np.abs(wgT - wgM)))
        KT, _P = kernel_grid(alt, bet, m0t, X_EVAL)
    else:
        out["chain"] = out["gauss_n"] = out["gauss_w"] = None
        KT = None
    if name == "uvarov":
        # Sherman-Morrison update of the nu_+ kernel (valid
        # for signed lambda as long as 1 + lam K(p,p) != 0);
        # note: SM updates the UNnormalized mu_+ + lam delta
        # kernel; nu_T kernel = same up to p_0 scale, and the
        # reproducing kernel is scale-covariant: K_nu = (1 +
        # lam) K_mu for mass-normalization by (1 + lam).
        xg = np.concatenate([X_EVAL, [xp]])
        Kp, _ = kernel_grid(*chain_pack_p, xg)
        kp = Kp[:-1, -1]
        kpp = Kp[-1, -1]
        Ksm = Kp[:-1, :-1] - lam * np.outer(kp, kp) \
            / (1.0 + lam * kpp)
        Ksm = Ksm * (1.0 + lam)
        if KT is not None:
            out["sm_ward"] = float(
                np.linalg.norm(Ksm - KT)
                / np.linalg.norm(KT))
        KT = Ksm
    KM = Kmin_grid
    if KT is None:
        # signed non-Uvarov weights: no kernel route (typed)
        out["ker"] = None
        out["rank"] = None
        return out
    out["ker"] = float(np.linalg.norm(KT - KM)
                       / np.linalg.norm(KM))
    sv = np.linalg.svd(KT - KM, compute_uv=False)
    s1 = float(np.linalg.svd(KM, compute_uv=False)[0])
    out["rank"] = int(np.sum(sv > 1e-2 * s1))
    return out


# ================================================================= main
def main():
    global chain_pack_p
    section("PRIME.JACOBI.POLE.UVAROV.01 -- classical "
            "spectral transformation at the source pole "
            "(EXPLORATION ONLY)")
    sha = hashlib.sha256(FROZEN_SPEC.encode("utf-8")).hexdigest()
    print("    FROZEN_SPEC SHA-256 = %s" % sha)
    print("    NO RH claim.  Construction %s, frozen holdout "
          "%s." % (CONSTRUCTION, HOLDOUT))
    print("\nS0 -- firewall + the machinery ward (synthetic)")
    check("S0.1 AST firewall clean (no zero/prime oracles)",
          not ast_scan(BANNED_IDS))
    # deterministic synthetic measure: 50 Chebyshev atoms,
    # smooth non-constant weights; pole 2.5; lambda 0.3
    xs_s = 2.0 * np.cos(math.pi * (2 * np.arange(50) + 1)
                        / 100.0)
    ws_s = (2.0 + np.sin(3.0 * xs_s)) / 50.0
    ps, ls = 2.5, 0.3
    m_base = weyl(xs_s, ws_s, Z_GRID)
    m0s = float(np.sum(ws_s))
    devs = []
    # Uvarov Weyl identity (unnormalized)
    xu = np.concatenate([xs_s, [ps]])
    wu = np.concatenate([ws_s, [ls]])
    devs.append(np.max(np.abs(weyl(xu, wu, Z_GRID)
                              - (m_base + ls / (ps - Z_GRID)))))
    # Christoffel Weyl identity
    devs.append(np.max(np.abs(
        weyl(xs_s, (ps - xs_s) * ws_s, Z_GRID)
        - ((ps - Z_GRID) * m_base - m0s))))
    # Geronimus Weyl identity
    I0s = float(np.sum(ws_s / (ps - xs_s)))
    devs.append(np.max(np.abs(
        weyl(xs_s, ws_s / (ps - xs_s), Z_GRID)
        - (m_base + I0s) / (ps - Z_GRID))))
    # Sherman-Morrison degree-8 kernel update
    a_s, b_s, m0_s, _ = cd.stieltjes_chain(xs_s, ws_s, 12)
    a_u, b_u, m0_u, _ = cd.stieltjes_chain(xu, wu, 12)
    xg = np.concatenate([X_EVAL, [ps]])
    Ps = poly_mat(a_s, b_s, m0_s, xg, 8)
    Ks = Ps @ Ps.T
    Pu = poly_mat(a_u, b_u, m0_u, X_EVAL, 8)
    Ku = Pu @ Pu.T
    Ksm = Ks[:-1, :-1] - ls * np.outer(Ks[:-1, -1],
                                       Ks[:-1, -1]) \
        / (1.0 + ls * Ks[-1, -1])
    devs.append(float(np.linalg.norm(Ksm - Ku)
                      / np.linalg.norm(Ku)))
    check("S0.2 [MACHINERY WARD] Uvarov/Christoffel/Geronimus "
          "Weyl identities + the Sherman-Morrison kernel "
          "update verified on the synthetic example (max dev "
          "%.1e <= 1e-10)" % max(devs), max(devs) <= 1e-10)

    # ---------------- S1 the two measures
    section("S1 -- THE TWO MEASURES mu_+- in x (wards + "
            "regression)")
    rungs = {}
    orth_ok = True
    merge_ok = True
    for kz in RUNGS:
        b = cd.build_rung(kz)
        xp_, mup = merge_side(b, +1)
        xm_, mum = merge_side(b, -1)
        merge_ok &= (len(xp_) == len(b["xn"])
                     and float(np.max(np.abs(mup - b["mu"])))
                     <= 1e-14)
        m0p, m0m = float(np.sum(mup)), float(np.sum(mum))
        nup, num_ = mup / m0p, mum / m0m
        chp = cd.stieltjes_chain(xp_, nup, 42)[:3]
        chm = cd.stieltjes_chain(xm_, num_, 42)[:3]
        for xs_, ws_, ch in ((xp_, nup, chp),
                             (xm_, num_, chm)):
            P = poly_mat(ch[0], ch[1], ch[2], xs_, 40)
            orth_ok &= float(np.max(np.abs(
                P.T @ (ws_[:, None] * P) - np.eye(40)))) \
                <= 1e-6
        rungs[kz] = dict(b=b, xp_=xp_, nup=nup, xm_=xm_,
                         num_=num_, chp=chp, chm=chm,
                         m0p=m0p, m0m=m0m, D=b["D"],
                         xpole=2.0 * math.cosh(b["D"] / 2.0))
        print("    kz %-3d D %.4f x_pole - 2 = %.3e | "
              "atoms +/-: %d/%d  mass +/-: %.3f/%.3f "
              "(ratio %.4f)"
              % (kz, b["D"], rungs[kz]["xpole"] - 2.0,
                 len(xp_), len(xm_), m0p, m0m, m0m / m0p),
              flush=True)
    check("S1.1 [MERGE + CHAIN WARDS] nu_+ merge reproduces "
          "the cdcore measure (machine); 40-column recurrence "
          "orthonormality <= 1e-6 for BOTH channel chains on "
          "every rung", merge_ok and orth_ok)
    b9 = rungs[9]["b"]
    xm9 = b9["x"][b9["neg"]]
    xp9 = b9["x"][b9["pos"]]
    Rx = xm9[:, None] * b9["Cres"] - b9["Cres"] * xp9[None, :]
    svx = np.linalg.svd(Rx, compute_uv=False)
    check("S1.2 [CDCORE REGRESSION] x-displacement rank@1e-6 "
          "== 2 at kz 9",
          int(np.sum(svx > 1e-6 * svx[0])) == 2)

    # ---------------- S2 the three transformation batteries
    section("S2 -- THE THREE TRANSFORMATIONS (x_pole = "
            "2 cosh(D/2), lambda source-determined)")
    print("    kz   T            lambda      mom      chain"
          "    weyl     gauss_n  gauss_w  ker      rank sm")
    res = {n: {} for n in ("uvarov", "christoffel",
                           "geronimus")}
    lam_tab = {}
    for kz in RUNGS:
        r = rungs[kz]
        xs_p, ws_p = r["xp_"], r["nup"]
        xs_m, ws_m = r["xm_"], r["num_"]
        xp = r["xpole"]
        m1p = float(np.sum(ws_p * xs_p))
        m1m = float(np.sum(ws_m * xs_m))
        I0 = float(np.sum(ws_p / (xp - xs_p)))
        I1 = float(np.sum(ws_p * xs_p / (xp - xs_p)))
        lam_u = (m1m - m1p) / (xp - m1m)
        lam_g = (m1m * I0 - I1) / (xp - m1m)
        lam_tab[kz] = dict(u=lam_u, g=lam_g, D=r["D"])
        chain_pack_p = r["chp"]
        Kmin, _ = kernel_grid(*r["chm"], X_EVAL)
        for name, lam in (("uvarov", lam_u),
                          ("christoffel", 0.0),
                          ("geronimus", lam_g)):
            o = battery(name, xs_p, ws_p, xs_m, ws_m,
                        r["chm"], xp, lam, Kmin)
            res[name][kz] = o
            print("    %-4d %-12s %+.3e  %.2e %s  %.2e  "
                  "%s  %s  %s %2d  %s%s"
                  % (kz, name, lam, o["mom"],
                     ("%.2e" % o["chain"]) if o["chain"]
                     is not None else "signed  ",
                     o["weyl"],
                     ("%.2e" % o["gauss_n"]) if o["gauss_n"]
                     is not None else "--      ",
                     ("%.2e" % o["gauss_w"]) if o["gauss_w"]
                     is not None else "--      ",
                     ("%.2e" % o["ker"]) if o["ker"]
                     is not None else "signed  ",
                     o["rank"] if o["rank"] is not None
                     else -1,
                     ("smw %.0e" % o["sm_ward"])
                     if o["sm_ward"] is not None else "",
                     "  (holdout)" if kz in HOLDOUT else ""),
                  flush=True)
    sm_ok = all(o["sm_ward"] <= 1e-8
                for o in res["uvarov"].values()
                if o["sm_ward"] is not None)
    check("S2.1 [SM INTERNAL WARD] Sherman-Morrison == direct "
          "transformed kernel wherever lambda >= 0 (rel <= "
          "1e-8)", sm_ok)

    # classification per transformation
    def classify(name):
        rr = res[name]
        comps = []
        for kz in RUNGS:
            o = rr[kz]
            vals = [o["mom"], o["weyl"]]
            vals += [v for v in (o["ker"], o["chain"],
                                 o["gauss_n"], o["gauss_w"])
                     if v is not None]
            if o["ker"] is None:
                vals.append(float("inf"))
            comps.append(max(vals))
        full = max(comps) <= 1e-8
        wc = [rr[kz]["weyl"] for kz in CONSTRUCTION]
        wh = [rr[kz]["weyl"] for kz in HOLDOUT]
        rks = [rr[kz]["rank"] if rr[kz]["rank"] is not None
               else 99 for kz in RUNGS]
        partial = (max(rr[kz]["weyl"] for kz in RUNGS) <= 0.05
                   and max(wh) <= 1.5 * max(wc)
                   and max(rks) <= 3)
        return full, partial, float(np.mean(wc)), max(wh)

    stats = {n: classify(n) for n in res}
    best = min(stats, key=lambda n: stats[n][2])
    for n in res:
        f, p, mc, mh = stats[n]
        print("    %-12s: FULL %-5s PARTIAL %-5s | mean "
              "construction weyl %.3e, max holdout %.3e"
              % (n, f, p, mc, mh))
    print("    best transformation: %s" % best)

    # ---------------- S3 lambda law + holdout transfer
    section("S3 -- the lambda(D) law + the holdout transfer")
    Ds = np.array([lam_tab[kz]["D"] for kz in RUNGS])
    lus = np.array([lam_tab[kz]["u"] for kz in RUNGS])
    lgs = np.array([lam_tab[kz]["g"] for kz in RUNGS])
    slu = np.polyfit(np.log(Ds),
                     np.log(np.abs(lus) + 1e-300), 1)[0]
    slg = np.polyfit(np.log(Ds),
                     np.log(np.abs(lgs) + 1e-300), 1)[0]
    print("    lambda_UVAROV:    %s" % "  ".join(
        "%+.2e" % v for v in lus))
    print("    lambda_GERONIMUS: %s" % "  ".join(
        "%+.2e" % v for v in lgs))
    print("    fit-free: Spearman(lam_u, D) = %+.2f, log-log "
          "slope %+.2f; Spearman(lam_g, D) = %+.2f, slope "
          "%+.2f; x_pole - 2 ~ D^2/4 (typed)"
          % (spearman(lus, Ds), slu, spearman(lgs, Ds), slg))
    fullB, partB, mcB, mhB = stats[best]
    check("S3.1 [HOLDOUT TRANSFER] the best transformation "
          "(%s) transfers blind: max holdout weyl %.3e <= "
          "1.5 x max construction %.3e (lambda per-rung "
          "source formula, never tuned)"
          % (best, mhB,
             max(res[best][kz]["weyl"] for kz in CONSTRUCTION)),
          mhB <= 1.5 * max(res[best][kz]["weyl"]
                           for kz in CONSTRUCTION))

    # ---------------- S4 discrimination
    section("S4 -- discrimination at kz 9 (Epstein, scramble) "
            "through the best transformation")
    rr9 = rungs[9]["b"]["rr"]
    N_E = int(math.floor(math.exp(2.0 * rr9["alpha"]))) + 1
    lamE = cd.lambda_eps(N_E)
    nn = np.nonzero(np.abs(lamE) > 1e-12)[0]
    w_t = res[best][9]["weyl"]
    l_t = lam_tab[9]["u" if best != "geronimus" else "g"]
    disc_ok = True
    for nmc, kw in (("Epstein", dict(comb=(
            np.log(nn.astype(float)),
            2.0 * lamE[nn] / np.sqrt(nn.astype(float))))),
            ("scramble", dict(scramble_seed=1))):
        bc = cd.build_rung(9, **kw)
        xpc, mupc = merge_side(bc, +1)
        xmc, mumc = merge_side(bc, -1)
        nupc = mupc / np.sum(mupc)
        numc = mumc / np.sum(mumc)
        chmc = cd.stieltjes_chain(xmc, numc, 42)[:3]
        xpo = 2.0 * math.cosh(bc["D"] / 2.0)
        m1p = float(np.sum(nupc * xpc))
        m1m = float(np.sum(numc * xmc))
        I0c = float(np.sum(nupc / (xpo - xpc)))
        I1c = float(np.sum(nupc * xpc / (xpo - xpc)))
        lam_c = ((m1m - m1p) / (xpo - m1m)
                 if best != "geronimus"
                 else (m1m * I0c - I1c) / (xpo - m1m))
        chain_pack_p = cd.stieltjes_chain(xpc, nupc, 42)[:3]
        Kmc, _ = kernel_grid(*chmc, X_EVAL)
        oc = battery(best, xpc, nupc, xmc, numc, chmc, xpo,
                     lam_c if best != "christoffel" else 0.0,
                     Kmc)
        rat = oc["weyl"] / max(w_t, 1e-300)
        ldev = (abs(lam_c - l_t) / max(abs(l_t), 1e-300)
                if best != "christoffel" else float("nan"))
        ok = rat >= 2.0 or (best != "christoffel"
                            and ldev >= 0.5)
        disc_ok &= ok
        print("    %-8s: weyl_res %.3e (truth %.3e, ratio "
              "%.2f), lambda %+.3e (truth %+.3e, rel dev "
              "%s) -> discriminates: %s"
              % (nmc, oc["weyl"], w_t, rat, lam_c, l_t,
                 ("%.2f" % ldev) if best != "christoffel"
                 else "n/a", ok))
    check("S4.1 [DISCRIMINATION] the controls' measure "
          "relation differs from truth (weyl ratio >= 2 or "
          "lambda rel dev >= 0.5) -- the transformation "
          "carries arithmetic, not just window geometry",
          disc_ok)

    # ---------------- V verdict
    section("V -- FROZEN VERDICT + honest consequence")
    if fullB and disc_ok:
        verdict = "%s-EXACT" % best.upper()
    elif partB:
        verdict = "POLE-TRANSFORM-PARTIAL"
        if fullB and not disc_ok:
            verdict += " (machine-exact but GEOMETRIC -- "\
                       "typed demotion)"
    else:
        verdict = "POLE-TRANSFORM-DEAD"
    print("\n  VERDICT: %s   [best %s | full %s | partial %s "
          "| holdout transfer %s | discrimination %s]"
          % (verdict, best, fullB, partB,
             mhB <= 1.5 * max(res[best][kz]["weyl"]
                              for kz in CONSTRUCTION),
             disc_ok))
    if fullB and disc_ok:
        print("""
  HONEST CONSEQUENCE: the measure relation is NAMED -- mu_-
  is the %s transformation of mu_+ at the source pole
  x_pole = 2 cosh(D/2), machine-exact across the functional
  battery on construction and blind holdouts, with lambda a
  typed source expression.  The kernel correction is then
  Sherman-Morrison-exact: K_- = K_+ - lam K_+(., x_p)
  K_+(x_p, .)/(1 + lam K_+(x_p, x_p)) -- the defect structure
  IS the rank-one pole correction.  What the compensation
  identity still needs: the transported CD kernel bound with
  the rank-one update controlled by the Christoffel function
  at x_p -- a classical object.  NO RH claim.""" % best)
    elif partB:
        wprof = [res[best][kz]["weyl"] for kz in RUNGS]
        rprof = [res[best][kz]["rank"] for kz in RUNGS]
        print("""
  HONEST CONSEQUENCE (typed): no classical transformation is
  machine-exact -- expected, since the two atomic supports
  are disjoint interleaved bands -- but the %s relation
  holds at the %.1f%%-level UNIFORMLY (weyl profile %s),
  window-independent, holdouts included, with correction
  rank profile %s (bar 3) and a source-typed lambda law.
  The relation is a FIXED SMALL correction, not a growing
  one: the pole transformation captures the leading measure
  relation; the residual is the named next object (its rank
  profile above -- the compensation identity needs exactly
  this remainder controlled).  NO RH claim.""" % (
            best, 100.0 * max(wprof),
            "/".join("%.3f" % v for v in wprof),
            "/".join(str(v) for v in rprof)))
    else:
        wprof = [res[best][kz]["weyl"] for kz in RUNGS]
        print("""
  HONEST CONSEQUENCE (typed): all three classical pole
  transformations miss -- best (%s) weyl profile %s across
  the ladder (growth ratio holdout/construction %.2f); the
  correction is not a fixed small-rank object at x_pole.
  The suspiciously-well-fitting hypothesis dies at the
  functional level; the Pruefer/Cotlar plan B activates.
  NO RH claim.""" % (
            best, "/".join("%.3f" % v for v in wprof),
            mhB / max(mcB, 1e-300)))
    n_pass = sum(1 for _n, ok in CHECKS if ok)
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed%s"
          % (time.time() - T0, len(CHECKS), len(FAILS),
             ("  " + ",".join(FAILS)) if FAILS else ""))
    return 0 if n_pass == len(CHECKS) else 1


chain_pack_p = None

if __name__ == "__main__":
    raise SystemExit(main())
'''

# ------------- frozen probe source gauss_crossdefect_probe (embedded BYTE-EXACT, raw string)
_SRC_1 = r'''
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""gauss_crossdefect_probe -- PRIME.GAUSS.CROSSDEFECT.01
(EXPLORATION ONLY, experiments/; round 33 late, probe B,
after GAUSS-STILL-DEFECTIVE, 2026-08-08).

THE QUESTION: is the O(1) co-isometry defect of the
Gauss-frame transition U^G FINITE-RANK and pole-organized
(then U = U_0 + R_pole and the wall shrinks to a small
matrix -- the Uvarov reading), or does its rank grow with h
(diffuse -- the Prufer route activates)?

DERIVED BEFORE RUNNING (frozen):
  (P1) STRUCTURAL SPLIT: E_R = I - U^H U contains the kernel
       block P_ker (dim h - r_-, eigenvalue exactly 1, the
       minus arm's rank compression) which grows with h
       REGARDLESS of cross-measure structure.  The Uvarov
       question lives in the nonzero-sigma pairing =
       E_L = I - U U^H on the minus side.  E_L is EXACTLY
       traceless (unit rows), so the over-normalization
       (negative part) and the loss (positive part) balance
       in trace -- both signs typed.
  (P2) POLE POINT: in x = cos th coordinates the pole is
       x_pole = cosh(D/2) (the task's 2cosh(D/2) in the
       z + 1/z convention -- the same point): the port
       v_k = e^{kD/2} is the kernel evaluation at the complex
       angle th = iD/2; the odd-extended evaluation vector
       f_k(iD/2) = e^{kD/2} - e^{(2h-1-k)D/2} is REAL.
       Two predeclared pole vectors, both Christoffel-
       normalized to U's row coordinates: kpol (kernel column
       at x_pole, task-frozen primary) and kv (the deployed
       plain port v, kappa-probe secondary).
  (P3) CLOSEST CO-ISOMETRY: U_0 = (U U^H)^{-1/2} U satisfies
       U_0 U_0^H = I exactly; with D_- <= 1 the base term
       I - U_0^H D_-^2 U_0 is PSD BY THEOREM, so the entire
       wall relocates into the bracket built from
       R = U - U_0: Delta = base - [U_0^H D_-^2 R + h.c.
       + R^H D_-^2 R].  If R is (near) finite rank the wall
       is a small-matrix condition -- the compensation
       statement.

VERDICT (frozen): CROSSDEFECT-POLE-RANK-ONE /
CROSSDEFECT-FINITE-RANK / CROSSDEFECT-DIFFUSE.
NO RH claim; writes nothing; v563 READ-ONLY.

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/gauss_crossdefect_probe.py
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
PRIME.GAUSS.CROSSDEFECT.01 spec v1 (2026-08-08, frozen before
run).  Machinery = gauss_node_unitary probe verbatim (arm
Gauss systems, U^G, D_-^G); ladder = ALL frame_a_zones with
h <= 900; heavy rungs {9, 12, 13, 26, 40}; anchors
{9, 12, 13}.  S1 DEFECT OPERATORS per rung: E_L = I - UU^H
(minus side, primary -- no structural block; traceless ward
|tr E_L| <= 1e-8 r_-), E_R = I - U^H U (plus side; kernel
block dim h - r_- typed, nonzero-sigma part mirrors E_L);
full eigh; sign structure (pos/neg counts + trace masses);
rank censuses #{|eig| > t max|eig|} at t in {1e-2, 1e-4,
1e-8}.  S2 POLE TEST (fit-free): fpole_k = e^{kD/2} -
e^{(2h-1-k)D/2}; kpol_g = K_+(th_g^-, x_pole) via zp = Rm
fpole (ward: two routes, conj(Zm) zp vs conj(Fm) solve(Gp,
fpole), rel <= 1e-8); kv from plain v; normalized kappa =
kpol/sqrt(Kdiag_-); overlaps o_pole = |<e_top(E_L),
kappa^>|, o3 = ||P_top3 kappa^|| (and same for kv); Rayleigh
gamma = kappa^H E_L kappa / ||kappa||^2 (source-determined,
no fit); residual E_res = E_L - gamma kappa kappa^H/
||kappa||^2; residual rank censuses at the same thresholds
(relative to max|eig E_L|); gamma_h series typed
(descriptive Pearson vs h, alpha; never gates).  S3
STABILITY: o_pole series along the ladder; frozen bar:
std(o_pole over the last 10 rungs) <= 0.15 (wild-rotation
kill); top-3 |eig| ratios at anchors (shape stability,
descriptive); boundary localization of top residual modes
(mass on nodes with th in the outer 5% of [0, pi],
descriptive).  S4 CONSEQUENCE at heavy rungs: U_0 =
(UU^H)^{-1/2} U (eigh route); wards ||U_0 U_0^H - I||_F <=
1e-8 and base = I - U_0^H D_-^2 U_0 PSD (lam_min >= -1e-10,
theorem P3); R = U - U_0: sigma profile, rank censuses,
top-mode pole overlap; bracket B = Delta_pos - base with
Delta_pos = I - (C^G)^H C^G: ||B||_2, rank@1e-2, and the tau
ward |lam_min(Delta_pos) - lam1(Delta_grid)| <= max(1e-9,
0.01 lam1).  GATE WARDS: the Gauss-frame regressions --
frame tightness/rows (max rel <= 1e-8), D_-^G(kz9) in
[0.98, 0.99], max D_-^G ladder <= 0.9975, cert(kz9) in
[1.0, 1.2], sigmax(U^G)(kz9) in [1.40, 1.49], bridge tauerr
<= max(1e-10, lam1/10) every rung; kpol two-route ward;
U_0/base wards; tau ward.  S5 controls at kz 9: Epstein
(x^2+5y^2) + scramble seed 1: lam1 < 0 AND the triple
(max|eig E_L|, o_pole, rank@1e-2(E_L)) differs from truth by
>= 5 percent in >= 1 component.  VERDICT (keyed to E_L,
predeclared): CROSSDEFECT-POLE-RANK-ONE iff gates pass AND
residual rank@1e-2 <= 3 on every rung; CROSSDEFECT-FINITE-
RANK iff gates pass AND residual rank@1e-2 <= 10 on every
rung AND mean(last third by h) < 1.5 mean(first third);
CROSSDEFECT-DIFFUSE otherwise (rank growth typed: the
first/last-third means, the h-correlation).  Float64;
budget ~15 min.  NO RH claim; writes nothing.
"""

HEAVY = (9, 12, 13, 26, 40)
ANCHORS = (9, 12, 13)
THRS = (1e-2, 1e-4, 1e-8)
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
    pos, neg = d > 0.0, d < 0.0
    Gp = np.real(Bp.conj().T @ Bp)
    Gm = np.real(Bm.conj().T @ Bm)
    ev, Vp = np.linalg.eigh(Gp)
    Rm = Vp @ np.diag(ev ** -0.5) @ Vp.T
    Delta = Rm @ Ktoe @ Rm
    Delta = 0.5 * (Delta + Delta.T)
    return dict(rr=rr, d=d, L=L, h=h, D=D, alpha=alpha, F=F,
                pos=pos, neg=neg, Gp=Gp, Gm=Gm, Rm=Rm,
                Delta=Delta)


# ------------------------------------------------ Gauss machinery (verbatim)
def folded_arm_measure(b, arm):
    L = b["L"]
    mask = b["pos"] if arm > 0 else b["neg"]
    jj = np.arange(L)[mask]
    th = 2.0 * math.pi * jj / L
    mu = np.abs(b["d"][mask]) / (2.0 * L)
    wt = mu * 4.0 * np.sin(th / 2.0) ** 2
    fold = np.minimum(jj, L - jj)
    uf, inv = np.unique(fold, return_inverse=True)
    wagg = np.zeros(len(uf))
    np.add.at(wagg, inv, wt)
    thu = 2.0 * math.pi * uf / L
    keep = wagg > 0.0
    return np.cos(thu[keep]), wagg[keep], thu[keep]


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
        if bnorm <= 1e-13 * max(1.0, float(np.max(np.abs(x)))):
            steps = k + 1
            break
        be[k] = bnorm
        Q[:, k + 1] = z / bnorm
    return al[:steps], be[:max(steps - 1, 0)], m0, steps


def arm_gauss_system(b, arm):
    xs, ws, thu = folded_arm_measure(b, arm)
    h = b["h"]
    if len(xs) > h:
        al, be, m0, steps = lanczos_chain(xs, ws, h)
        if steps < h:
            return None, None, "breakdown@%d" % steps
        T = np.diag(al)
        if h > 1:
            T += np.diag(be, 1) + np.diag(be, -1)
        evs, V = np.linalg.eigh(T)
        xg = np.clip(evs, -1.0, 1.0)
        wg = m0 * V[0] ** 2
        th = np.arccos(xg)
        wS = wg / (4.0 * np.sin(th / 2.0) ** 2)
        return th, wS, "gauss"
    th = thu
    wS = ws / (4.0 * np.sin(th / 2.0) ** 2)
    return th, wS, "measure-tight"


def eval_frame(th, h):
    k = np.arange(h)
    ph = np.exp(-1j * np.outer(th, k))
    ph2 = np.exp(-1j * np.outer(th, 2 * h - 1 - k))
    return ph - ph2


def gauss_objects(b):
    h = b["h"]
    thp, wSp, modep = arm_gauss_system(b, +1)
    thm, wSm, modem = arm_gauss_system(b, -1)
    if thp is None or thm is None:
        return dict(mode=(modep, modem), fail=True)
    Fp = eval_frame(thp, h)
    Fm = eval_frame(thm, h)
    Zp = Fp @ b["Rm"]
    Zm = Fm @ b["Rm"]
    Kp = np.sum(np.abs(Zp) ** 2, axis=1)
    Km = np.sum(np.abs(Zm) ** 2, axis=1)
    Knp = Zm @ Zp.conj().T
    U = (1.0 / np.sqrt(Km))[:, None] * Knp \
        * (1.0 / np.sqrt(Kp))[None, :]
    Dp = np.sqrt(wSp * Kp)
    Dm = np.sqrt(wSm * Km)
    CG = np.sqrt(wSm)[:, None] * Knp * np.sqrt(wSp)[None, :]
    w1p = float(np.linalg.norm(np.real(
        (np.sqrt(wSp)[:, None] * Fp).conj().T
        @ (np.sqrt(wSp)[:, None] * Fp)) - b["Gp"])
        / np.linalg.norm(b["Gp"]))
    rown = np.sqrt(np.sum(np.abs(U) ** 2, axis=1))
    w3row = float(np.max(np.abs(rown - 1.0)))
    return dict(mode=(modep, modem), fail=False, thp=thp,
                thm=thm, Fm=Fm, Zp=Zp, Zm=Zm, Kp=Kp, Km=Km,
                U=U, Dp=Dp, Dm=Dm, CG=CG, w1=w1p, w3=w3row,
                rminus=len(thm))


def rank_census(eigs, ref):
    a = np.abs(eigs)
    return tuple(int(np.sum(a > t * ref)) for t in THRS)


def pearson(a, b):
    a = np.asarray(a, float) - np.mean(a)
    b = np.asarray(b, float) - np.mean(b)
    den = np.linalg.norm(a) * np.linalg.norm(b)
    return float(a @ b / den) if den > 0 else 0.0


def defect_analysis(b, go):
    """E_L spectral decomposition + the pole test."""
    U, Zm, Km = go["U"], go["Zm"], go["Km"]
    rmin = go["rminus"]
    EL = np.eye(rmin) - U @ U.conj().T
    EL = 0.5 * (EL + EL.conj().T)
    ev, W = np.linalg.eigh(EL)
    emax = float(np.max(np.abs(ev)))
    tr = float(np.real(np.trace(EL)))
    npos = int(np.sum(ev > 0)); nneg = int(np.sum(ev < 0))
    mpos = float(np.sum(ev[ev > 0]))
    mneg = float(-np.sum(ev[ev < 0]))
    # pole vectors (P2)
    h, D = b["h"], b["D"]
    kk = np.arange(h)
    fpole = np.exp(0.5 * D * kk) \
        - np.exp(0.5 * D * (2 * h - 1 - kk))
    zpol = b["Rm"] @ fpole
    kpol = np.conj(Zm) @ zpol
    kpol2 = np.conj(go["Fm"]) @ np.linalg.solve(b["Gp"], fpole)
    wardk = float(np.linalg.norm(kpol - kpol2)
                  / np.linalg.norm(kpol))
    v = np.exp(0.5 * D * kk)
    kv = np.conj(Zm) @ (b["Rm"] @ v)
    kap = kpol / np.sqrt(Km)
    kap = kap / np.linalg.norm(kap)
    kapv = kv / np.sqrt(Km)
    kapv = kapv / np.linalg.norm(kapv)
    # top defect mode overlaps (by |eig|)
    order = np.argsort(-np.abs(ev))
    etop = W[:, order[0]]
    o_pole = float(abs(np.vdot(etop, kap)))
    o_v = float(abs(np.vdot(etop, kapv)))
    P3 = W[:, order[:3]]
    o3 = float(np.linalg.norm(P3.conj().T @ kap))
    # Rayleigh + residual (fit-free)
    gam = float(np.real(np.vdot(kap, EL @ kap)))
    ERES = EL - gam * np.outer(kap, kap.conj())
    evr = np.linalg.eigvalsh(0.5 * (ERES + ERES.conj().T))
    return dict(EL=EL, ev=ev, emax=emax, tr=tr, npos=npos,
                nneg=nneg, mpos=mpos, mneg=mneg, kap=kap,
                kapv=kapv, wardk=wardk, o_pole=o_pole,
                o_v=o_v, o3=o3, gam=gam, evr=evr,
                rk=rank_census(ev, emax),
                rkres=rank_census(evr, emax),
                W=W, order=order)


# ================================================================= main
def main():
    section("PRIME.GAUSS.CROSSDEFECT.01 (EXPLORATION ONLY)")
    sha = hashlib.sha256(FROZEN_SPEC.encode("utf-8")).hexdigest()
    print("    FROZEN_SPEC SHA-256 = %s" % sha)
    print("    NO RH claim.")
    print("\nS0 -- firewall")
    check("S0.1 AST firewall clean (no zero/prime oracles)",
          not ast_scan(BANNED_IDS))

    zones = list(core.frame_a_zones())

    section("S1/S2 ladder pass -- defect spectra + pole test")
    rows = []
    heavy_data = {}
    skipped = []
    wardk_max = 0.0
    print("    kz    h    r-   |eig|mx  n+/n-     rank"
          "@1e-2/4/8      gamma    o_pole o_v    o3"
          "     res@1e-2/4/8")
    for kz in zones:
        b = build_rung(kz)
        if b["h"] > 900:
            skipped.append(kz)
            continue
        go = gauss_objects(b)
        if go["fail"]:
            check("S1.x kz %d Gauss system FAILED (%s)"
                  % (kz, go["mode"]), False)
            continue
        da = defect_analysis(b, go)
        wardk_max = max(wardk_max, da["wardk"])
        lam1 = float(np.linalg.eigvalsh(b["Delta"])[0])
        svC = np.linalg.svd(go["CG"], compute_uv=False)
        tauerr = abs(float(svC[0]) ** 2 - (1.0 - lam1))
        sv = np.linalg.svd(go["U"], compute_uv=False)
        r = dict(kz=kz, h=b["h"], rminus=go["rminus"],
                 emax=da["emax"], tr=da["tr"],
                 rk=da["rk"], rkres=da["rkres"],
                 gam=da["gam"], o_pole=da["o_pole"],
                 o_v=da["o_v"], o3=da["o3"],
                 maxDm=float(np.max(go["Dm"])),
                 cert=float(np.max(np.abs(sv ** 2 - 1.0))),
                 sig=float(sv[0]), lam1=lam1, tauerr=tauerr,
                 w1=go["w1"], w3=go["w3"], alpha=b["alpha"])
        rows.append(r)
        if kz in HEAVY:
            heavy_data[kz] = (b, go, da)
        print("    %-5d %-4d %-4d %.4f  %3d/%-3d  "
              "%3d/%3d/%3d      %+.4f  %.3f  %.3f  %.3f"
              "  %3d/%3d/%3d"
              % (kz, r["h"], r["rminus"], r["emax"],
                 da["npos"], da["nneg"], *r["rk"], r["gam"],
                 r["o_pole"], r["o_v"], r["o3"], *r["rkres"]),
              flush=True)
    if skipped:
        print("    skipped (h > 900): %s" % skipped)

    # ---------------- S1 wards + sign structure
    section("S1 -- wards and the sign structure of the defect")
    w13 = max(max(r["w1"], r["w3"]) for r in rows)
    check("S1.1 [FRAME REGRESSION] tightness + unit rows "
          "(max %.2e)" % w13, w13 <= 1e-8)
    trmax = max(abs(r["tr"]) / r["rminus"] for r in rows)
    check("S1.2 [P1 TRACELESS] |tr E_L| <= 1e-8 r_- every "
          "rung (max %.2e; over-normalization == loss in "
          "trace)" % trmax, trmax <= 1e-8)
    check("S1.3 [KPOL WARD] two-route kernel column at "
          "x_pole = cosh(D/2), rel <= 1e-8 (max %.2e)"
          % wardk_max, wardk_max <= 1e-8)
    r9 = next(r for r in rows if r["kz"] == 9)
    reg_ok = (0.98 <= r9["maxDm"] <= 0.99
              and 1.0 <= r9["cert"] <= 1.2
              and 1.40 <= r9["sig"] <= 1.49
              and max(r["maxDm"] for r in rows) <= 0.9975)
    check("S1.4 [GAUSS-FRAME REGRESSIONS] D_-^G(kz9) = %.4f, "
          "cert(kz9) = %.3f, sigmax(kz9) = %.4f, ladder "
          "maxD- = %.4f" % (r9["maxDm"], r9["cert"], r9["sig"],
                            max(r["maxDm"] for r in rows)),
          reg_ok)
    tau_ok = all(r["tauerr"] <= max(1e-10, r["lam1"] / 10.0)
                 for r in rows)
    check("S1.5 [BRIDGE] tau preserved every rung", tau_ok)
    for kz in ANCHORS:
        b, go, da = heavy_data[kz]
        ev = da["ev"]
        print("    kz %-3d: E_L eig quantiles q05/q50/q95 = "
              "%+.3f/%+.3f/%+.3f; pos/neg trace mass = "
              "%.2f/%.2f; E_R kernel block dim h - r_- = %d "
              "(structural, typed)"
              % (kz, float(np.quantile(ev, 0.05)),
                 float(np.quantile(ev, 0.50)),
                 float(np.quantile(ev, 0.95)),
                 da["mpos"], da["mneg"],
                 b["h"] - go["rminus"]))

    # ---------------- S3 growth + stability
    section("S3 -- rank growth and mode stability")
    hs = sorted(rows, key=lambda r: r["h"])
    third = len(hs) // 3
    first_m = float(np.mean([r["rkres"][0] for r in
                             hs[:third]]))
    last_m = float(np.mean([r["rkres"][0] for r in
                            hs[-third:]]))
    corr_h = pearson([r["h"] for r in rows],
                     [r["rkres"][0] for r in rows])
    rkres_max = max(r["rkres"][0] for r in rows)
    print("    residual rank@1e-2: max %d; first/last-third "
          "means (by h) %.1f -> %.1f (x%.2f); Pearson vs h = "
          "%+.3f" % (rkres_max, first_m, last_m,
                     last_m / max(first_m, 1e-12), corr_h))
    rk_max = max(r["rk"][0] for r in rows)
    first_f = float(np.mean([r["rk"][0] for r in hs[:third]]))
    last_f = float(np.mean([r["rk"][0] for r in hs[-third:]]))
    print("    full E_L rank@1e-2:  max %d; first/last-third "
          "means %.1f -> %.1f (x%.2f)"
          % (rk_max, first_f, last_f,
             last_f / max(first_f, 1e-12)))
    gam_h = pearson([math.log(r["h"]) for r in rows],
                    [r["gam"] for r in rows])
    gam_a = pearson([r["alpha"] for r in rows],
                    [r["gam"] for r in rows])
    print("    gamma_h series: range [%+.4f, %+.4f], Pearson "
          "vs log h = %+.3f, vs alpha = %+.3f (descriptive)"
          % (min(r["gam"] for r in rows),
             max(r["gam"] for r in rows), gam_h, gam_a))
    tail = [r["o_pole"] for r in rows[-10:]]
    stab = float(np.std(tail))
    check("S3.1 [STABILITY] std(o_pole, last 10 rungs) = "
          "%.3f <= 0.15 (mean %.3f; wild-rotation kill "
          "otherwise)" % (stab, float(np.mean(tail))),
          stab <= 0.15)
    for kz in ANCHORS:
        b, go, da = heavy_data[kz]
        e3 = da["ev"][np.argsort(-np.abs(da["ev"]))[:3]]
        # boundary localization of top residual modes
        thm = go["thm"]
        edge = (thm <= 0.05 * math.pi) | (thm >= 0.95 * math.pi)
        wt = da["W"][:, da["order"][:3]]
        bmass = float(np.sum(np.abs(wt[edge]) ** 2)
                      / np.sum(np.abs(wt) ** 2))
        print("    kz %-3d: top-3 |eig| = %+.4f/%+.4f/%+.4f; "
              "edge-node mass of top-3 modes = %.1f%% "
              "(nodes at edge: %d/%d)"
              % (kz, e3[0], e3[1], e3[2], 100 * bmass,
                 int(np.sum(edge)), len(thm)))

    # ---------------- S4 the consequence: U0 + R
    section("S4 -- closest co-isometry U_0 + R and the "
            "bracket (heavy rungs)")
    u0_ok = True
    base_ok = True
    tau2_ok = True
    for kz in HEAVY:
        b, go, da = heavy_data[kz]
        U, Dm = go["U"], go["Dm"]
        G = U @ U.conj().T
        G = 0.5 * (G + G.conj().T)
        gv, GV = np.linalg.eigh(G)
        Gmh = GV @ np.diag(gv ** -0.5) @ GV.conj().T
        U0 = Gmh @ U
        w0 = float(np.linalg.norm(U0 @ U0.conj().T
                                  - np.eye(len(gv))))
        u0_ok &= w0 <= 1e-8
        R = U - U0
        svR = np.linalg.svd(R, compute_uv=False)
        uR = np.linalg.svd(R, compute_uv=True)[0][:, 0]
        oR = float(abs(np.vdot(uR, da["kap"])))
        rkR = rank_census(svR, float(svR[0]))
        # bracket
        base = np.eye(b["h"]) - U0.conj().T @ (Dm[:, None] ** 2
                                               * U0)
        base = 0.5 * (base + base.conj().T)
        lmb = float(np.linalg.eigvalsh(base)[0])
        base_ok &= lmb >= -1e-10
        Dpos = np.eye(b["h"]) - go["CG"].conj().T @ go["CG"]
        Dpos = 0.5 * (Dpos + Dpos.conj().T)
        lmD = float(np.linalg.eigvalsh(Dpos)[0])
        tau2_ok &= abs(lmD - r_lam1(rows, kz)) \
            <= max(1e-9, 0.01 * r_lam1(rows, kz))
        Brk = Dpos - base
        Brk = 0.5 * (Brk + Brk.conj().T)
        evB = np.linalg.eigvalsh(Brk)
        nB = float(max(np.abs(evB)))
        rkB = rank_census(evB, nB)
        print("    kz %-3d: ||U0U0*-I|| = %.1e; sigma(R) top "
              "%.3f, rank@1e-2 = %d, top-mode pole overlap = "
              "%.3f; lam_min(base) = %+.2e (PSD thm); "
              "||bracket|| = %.3f, rank@1e-2 = %d; "
              "lam_min(Delta_pos) = %+.3e vs tau %.3e"
              % (kz, w0, float(svR[0]), rkR[0], oR, lmb,
                 nB, rkB[0], lmD, r_lam1(rows, kz)))
    check("S4.1 [U0 WARD] U_0 U_0^H = I at heavy rungs "
          "(closest co-isometry constructed)", u0_ok)
    check("S4.2 [P3 BASE PSD] I - U_0^H D_-^2 U_0 >= 0 at "
          "heavy rungs (theorem: D_- <= 1 + co-isometry)",
          base_ok)
    check("S4.3 [TAU WARD] lam_min(I - C^G* C^G) == "
          "lam1(Delta_grid) at heavy rungs", tau2_ok)

    # ---------------- S5 controls
    section("S5 -- controls at kz 9 (Epstein x^2+5y^2, "
            "scramble seed 1)")
    rt = next(r for r in rows if r["kz"] == 9)
    triple_t = np.array([rt["emax"], rt["o_pole"],
                         float(rt["rk"][0])])
    rr9 = core.build_window(9)
    N_E = int(math.floor(math.exp(2.0 * rr9["alpha"]))) + 1
    lamE = lambda_eps(N_E)
    nn = np.nonzero(np.abs(lamE) > 1e-12)[0]
    ctrl_ok = True
    for nmc, kw in (("Epstein", dict(comb=(
            np.log(nn.astype(float)),
            2.0 * lamE[nn] / np.sqrt(nn.astype(float))))),
            ("scramble", dict(scramble_seed=1))):
        bc = build_rung(9, **kw)
        gc = gauss_objects(bc)
        lam1c = float(np.linalg.eigvalsh(bc["Delta"])[0])
        if gc["fail"]:
            print("    %-8s: Gauss system failed (%s) -- "
                  "maximal discrimination" % (nmc, gc["mode"]))
            ctrl_ok &= lam1c < 0.0
            continue
        dc = defect_analysis(bc, gc)
        triple_c = np.array([dc["emax"], dc["o_pole"],
                             float(dc["rk"][0])])
        reldiff = np.abs(triple_c - triple_t) \
            / np.maximum(triple_t, 1e-12)
        ctrl_ok &= (lam1c < 0.0
                    and bool(np.max(reldiff) >= 0.05))
        print("    %-8s: lam1 = %+.3e; (|eig|max, o_pole, "
              "rank@1e-2) = (%.3f, %.3f, %d) vs truth "
              "(%.3f, %.3f, %d); max rel diff %.1f%%"
              % (nmc, lam1c, dc["emax"], dc["o_pole"],
                 dc["rk"][0], rt["emax"], rt["o_pole"],
                 int(rt["rk"][0]),
                 100.0 * float(np.max(reldiff))))
    check("S5.1 [CONTROLS] sign break + defect-structure "
          "difference >= 5%", ctrl_ok)

    # ---------------- verdict
    section("V -- FROZEN VERDICT + honest consequence")
    gates_ok = (w13 <= 1e-8 and trmax <= 1e-8
                and wardk_max <= 1e-8 and reg_ok and tau_ok
                and stab <= 0.15 and u0_ok and base_ok
                and tau2_ok and ctrl_ok)
    growth = last_m >= 1.5 * first_m
    if gates_ok and rkres_max <= 3:
        verdict = "CROSSDEFECT-POLE-RANK-ONE"
        typed = ("residual rank@1e-2 <= %d everywhere; "
                 "gamma law above" % rkres_max)
    elif gates_ok and rkres_max <= 10 and not growth:
        verdict = "CROSSDEFECT-FINITE-RANK"
        typed = ("residual rank@1e-2 <= %d, no growth "
                 "(%.1f -> %.1f)" % (rkres_max, first_m,
                                     last_m))
    else:
        verdict = "CROSSDEFECT-DIFFUSE"
        typed = ("residual rank@1e-2 max %d, first/last "
                 "third %.1f -> %.1f (x%.2f), Pearson vs h "
                 "%+.3f%s -- the Uvarov reading dies, the "
                 "Prufer route activates"
                 % (rkres_max, first_m, last_m,
                    last_m / max(first_m, 1e-12), corr_h,
                    "" if gates_ok else
                    "; GATES FAILED: %s" % sorted(set(FAILS))))
    print("\n  VERDICT: %s" % verdict)
    print("  typed: %s" % typed)
    npass = sum(1 for _, ok in CHECKS if ok)
    print("\n  checks: %d/%d passed; elapsed %.1f s"
          % (npass, len(CHECKS), time.time() - T0))
    print("""
HONEST CONSEQUENCE (no RH claim):
  the pole share of the defect (o_pole, gamma) and the
  U_0 + R bracket sizes above are the honest inventory of
  how much of the cross-measure misalignment is
  pole-organized; the rank censuses decide whether a
  finite-matrix compensation exists at all.  EXPLORATION
  ONLY; nothing here enters verification/ or the papers.""")
    return verdict


def r_lam1(rows, kz):
    return next(r["lam1"] for r in rows if r["kz"] == kz)


if __name__ == "__main__":
    main()
'''

# --------------------------------------------------------------- harness
_PF_RE = re.compile(r"^\s*\[(PASS|FAIL)\]\s+(\S+)", re.M)
_VD_RE = re.compile(r"VERDICT[^\n]*:")


def _probe_file(name):
    cand = os.path.abspath(os.path.join(
        _HERE, os.pardir, "experiments", "tfpt-discovery", name + ".py"))
    return cand if os.path.isfile(cand) else None


def _census(out):
    marks = _PF_RE.findall(out)
    fails = sorted({tok for st, tok in marks if st == "FAIL"})
    verdicts = [ln.strip() for ln in out.splitlines()
                if _VD_RE.search(ln)]
    return len(marks), fails, " | ".join(verdicts)


def _exec_probe(name, src, run_entry=True):
    """Execute one embedded frozen probe source BYTE-EXACT in its own
    module namespace, registered in sys.modules under the probe's
    canonical import name; capture and re-emit stdout; return
    (stdout, exit_code, byte_equal_to_source_file_or_None).  Probes
    whose main() returns the verdict STRING map to exit 0, exactly as
    their own __main__ guards do (main() called, return value dropped)."""
    if src[:1] == "\n":
        src = src[1:]
    path = _probe_file(name)
    same = None
    if path is not None:
        with open(path, encoding="utf-8") as fh:
            same = (fh.read() == src)
    fname = path or os.path.abspath(__file__)
    mod = types.ModuleType(name)
    mod.__file__ = fname
    sys.modules[name] = mod
    buf = io.StringIO()
    code = 0
    with contextlib.redirect_stdout(buf):
        try:
            exec(compile(src, fname, "exec"), mod.__dict__)
            entry = mod.__dict__.get("main") or mod.__dict__.get("run")
            if run_entry and callable(entry):
                rc = entry()
                code = (0 if rc is None or isinstance(rc, str)
                        else int(rc))
        except SystemExit as exc:
            code = 0 if exc.code is None else int(exc.code)
        except Exception:                            # regression guard
            import traceback
            traceback.print_exc(file=sys.stdout)
            code = 99
    out = buf.getvalue()
    sys.stdout.write(out)
    sys.stdout.flush()
    return out, code, same


def _gate(name, out, code, same, exp_n, exp_fails, exp_verdicts,
          exp_code, gates):
    n, fails, verdict = _census(out)
    ok = (n == exp_n and fails == list(exp_fails)
          and all(v in verdict for v in exp_verdicts)
          and code == exp_code and same is not False)
    gates.append(ok)
    prov = ("byte-exact vs experiments source" if same is True else
            "embedded copy (source file not present)" if same is None
            else "SOURCE MISMATCH")
    print("\n[%s] PATTERN GATE %s: %d checks (exp %d) | FAILs %s "
          "(exp %s) | exit %d (exp %d) | %s\n      verdict line(s): %s"
          % ("PASS" if ok else "FAIL", name, n, exp_n,
             ",".join(fails) if fails else "none",
             ",".join(exp_fails) if exp_fails else "none",
             code, exp_code, prov, verdict), flush=True)
    return ok

_PLAN = (
    ('jacobi_pole_uvarov_probe', _SRC_0, 7, (),
     ('POLE-TRANSFORM-DEAD',), 0),
    ('gauss_crossdefect_probe', _SRC_1, 11, (),
     ('CROSSDEFECT-DIFFUSE',), 0),
)


def run():
    t0 = time.time()
    print("=" * 74)
    print('v871 -- PRIME.JACOBI.POLE.UVAROV.01 + PRIME.GAUSS.CROSSDEFECT.01')
    print('(the measure-relation closure: none of Uvarov / Christoffel /')
    print('Geronimus is exact or fixed-small-rank at x_pole = 2 cosh(D/2)')
    print('(typed residue: small-negative-mass Geronimus 3.5-8%, no lambda(D)')
    print('law), and the co-isometry defect is DIFFUSE -- full-rank, growing')
    print('linearly with h; no finite-matrix compensation; NO RH claim)')
    print("=" * 74, flush=True)
    gates = []
    for name, src, exp_n, exp_fails, exp_verdicts, exp_code in _PLAN:
        print("\n" + "-" * 74)
        print("EMBEDDED FROZEN PROBE: %s" % name)
        print("-" * 74, flush=True)
        out, code, same = _exec_probe(name, src)
        _gate(name, out, code, same, exp_n, exp_fails,
              exp_verdicts, exp_code, gates)
    ok = all(gates)
    print("\n" + "=" * 74)
    print("%s: %d/%d probe pattern gates passed | runtime %.1f s"
          % ('v871', sum(gates), len(gates), time.time() - t0))
    print('Both classical escapes are closed with certificates: the')
    print('mu_- <-> mu_+ relation is NOT a classical pole transformation')
    print('(best: Geronimus, small negative mass, 3.5-8% Weyl residual,')
    print('non-growing, discriminating -- but no exact law), and the')
    print('cross-measure defect admits NO finite-rank correction (rank')
    print('grows with h at Pearson +0.996; pole removal changes nothing).')
    print('The Pruefer route is the named plan B -- preregistered.')
    print("[%s] %s VERDICT GATE: POLE-TRANSFORM-DEAD + CROSSDEFECT-DIFFUSE"
          % ("PASS" if ok else "FAIL", 'v871'))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(run())
