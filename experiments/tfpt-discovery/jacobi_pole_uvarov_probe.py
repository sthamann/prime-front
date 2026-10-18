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
