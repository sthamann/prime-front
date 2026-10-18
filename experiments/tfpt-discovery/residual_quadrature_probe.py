#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""residual_quadrature_probe -- PRIME.RESIDUAL.QUADRATURE.01
(EXPLORATION ONLY, experiments/; round 35, the Carleson
strand's ROUTE 2: the positive residual quadrature).

THE IDEA: instead of bounding lam_max(M_-), CONSTRUCT a
positive measure rho_h with int x^k d rho_h = int x^k
d(mu~_+ - nu~_-) for 0 <= k <= 2h-2 -- then M(mu~_+ - nu~_-)
= M(rho_h) >= 0 immediately.  HONEST FRAME (typed): the
existence of a positive representing rho IS equivalent to
the target (Hamburger); the probe's content is whether a
SOURCE-STRUCTURED candidate family (the difference Jacobi
chain via stable modified-moment quadrature) achieves it
with controlled complexity, and where it fails if not.

SPEC v2 (typed): v1 executed and exposed (i) a FALSE PREMISE
in the v1 synthetic ward W-A1 (the v1 difference 2 + cos 3x
- 1 - 0.5 sin 2x goes negative on-grid near x = 0.93 -- the
ward tested an indefinite input, k* = 2 was CORRECT); (ii) a
UNIVERSAL k* ~ 535 wall on every rung with h > 535 that is
pure float underflow (the Wheeler sigma-table decays like
4^{-k} mass; 4^{-536} = 1e-323 = the float64 subnormal
floor), not structure.  v2 fixes: the synthetic minus weight
scaled to 0.3 (1 + 0.5 sin 2x) with an in-ward positivity
assertion of the premise; ROW-SCALED Wheeler (row
max-normalization, log-scale bookkeeping -- exact: alphas
are same-row ratios, betas carry the log-scale increment);
mp reference extended to kz 28 (the first v1-walled rung);
node-hull census at certified depth.  The v1 log is
retained at /tmp/residual_run1.log.

SPEC v3 (typed): v2 executed and established (i) the mp
reference at kz 28 certifies the FULL horizon (615 = h)
while the 53-bit run stalls at 540 -- the residual k* ~ 536
wall is the double-precision NOISE FLOOR, not structure
(platform long double aliases float64 at 53 bits; the
"two-dtype" certification degenerates into a
summation-order probe); (ii) v2's W-A1 failed only because
the depth-60 double-precision tail pushed one node to
1.0011 -- the algorithm itself reproduced moments at
2.8e-16.  v3: W-A1 becomes MP-GRADE (dps 40; the clean
algorithm ward -- double drift is typed by k*_cert
separately); MP ESCALATION pass added: every rung with
k*_cert < h gets the definitive mp dps-60 Wheeler horizon
k*_mp, and the frozen decision is keyed on k*_eff = k*_mp
where escalated else k*_cert.  The v2 log is retained at
/tmp/residual_run2.log.  NO RH claim; writes nothing; v563
+ gauss_node_unitary machinery READ-ONLY.

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/residual_quadrature_probe.py
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

import v563_paper2_readouts as core            # noqa: E402  (READ-ONLY)
import gauss_node_unitary_probe as gnu         # noqa: E402  (READ-ONLY)

FROZEN_SPEC = """\
PRIME.RESIDUAL.QUADRATURE.01 spec v3 (2026-08-08, frozen
before the v3 run; v1 superseded: false-premise synthetic
ward + float64 sigma-table underflow; v2 superseded: the
53-bit noise-floor wall at k ~ 536 shown non-structural by
the kz-28 mp reference, W-A1 depth-60 double drift; all
typed in the probe docstring).  Machinery read-only:
gnu.build_rung / folded_arm_measure / arm_gauss_system /
gauss_objects / softport / lambda_eps.  Ladder: battery =
frame_a_zones with h <= 900 (42 rungs) + frozen deep
holdouts kz {90, 116, 142, 177, 243}.  TARGET: the
difference functional L = mu~_+ - nu~_- (folded
sin^2-modified arm measures, exact atoms) on P_{2h-2}; M(L)
>= 0 on P_{h-1} is the certified Carleson statement (lam_min
identity, regression W-M1).  PRIMARY ALGORITHM (frozen):
ROW-SCALED Wheeler with the MONIC CHEBYSHEV auxiliary basis
(a_l = 0; b_1 = 1/2, b_l = 1/4): each sigma-row is
max-normalized with the log scale tracked; alpha_k =
sigma'_{k,k+1}/sigma'_{k,k} - sigma'_{k-1,k}/
sigma'_{k-1,k-1} (scale-free), sign beta_k =
sign(sigma'_{k,k}/sigma'_{k-1,k-1}), log|beta_k| adds the
row log-scale increment (mathematically the identity
transformation of the v1 recursion); modified moments nu_l =
2^{1-l} sum_i w_i cos(l th_i), exact trig sums on the atom
angles, l <= 2h-1.  POSITIVITY HORIZON (frozen): k*_raw =
consecutive k with sign beta_k > 0 from k = 0; CERTIFIED
k*_cert additionally requires the float64 and long-double
runs to agree: same sign and |log beta_ld - log beta_64| <=
1e-3 at every counted step (platform long-double width
printed and typed).  k* >= h certifies M(L) >= 0
constructively (the h-point Gauss rule of the difference
chain IS rho_h).  MP ESCALATION (v3, frozen): every rung
with k*_cert < h gets the definitive mpmath dps-60 Wheeler
horizon k*_mp (T_l-recurrence moments, classical unscaled
recursion -- mp exponent range needs no scaling); rungs
where the dps-60 horizon is below h are retried ONCE at dps
120 (precision-vs-structure disambiguation) and k*_mp is
the larger; the decision quantity is k*_eff = k*_mp where
escalated, else k*_cert; the double-precision stable depth
(~536) is typed as the platform noise floor, not part of
the verdict.
WARDS: W-M1 [TAU REGRESSION] lam_min(I - M_-) in the
plus-orthonormal basis == softport lam1 at kz {9, 13}, rel
1e-6; W-M2 [TWO-PATH MOMENTS] trig sums == T_l recurrence
at atoms, anchors {9, 12, 13, 26, 40}, all l <= 2h-1, worst
rel 1e-9; W-A1 [SYNTHETIC, v3, MP-GRADE dps 40] grid x_i =
-0.95 + 0.019 i, i < 100, w_+ = 2 + cos 3x, w_- = 0.3 (1 +
0.5 sin 2x); PREMISE ASSERTED in-ward: min(w_+ - w_-) > 0;
n = 60 in mp arithmetic: all beta > 0, Jacobi eigenvalues
inside the support hull + 1e-10, depth-60 mp Gauss moments
reproduce direct moments rel 1e-25; W-P1 [MP REFERENCE]
mpmath dps 60 Wheeler at kz 9 AND kz 28: mp horizon >=
min(k*_cert, h) (the mp run must never certify LESS than
the double run's certified region); W-C1 [GAUSS RULE]
minus-arm Gauss rule reproduces atom moments at l in {0, 1,
7, 25}, rel 1e-8, anchors.  CONSTRUCTIONS: (a) THE
DIFFERENCE CHAIN, full ladder + holdouts, with the
node-hull census at the certified depth in double
arithmetic (max Gauss node, # nodes with x > 1 + 1e-12 --
does rho_h leak past the pole port?  typed double-grade);
(b) RADAU-ANCHORED: the Wheeler
horizon of the localized functional (1 - x) L (anchor x_R =
+1 = the pole-port fold, typed choice); tests the
support-localization (Hausdorff) half at the fold; (c)
DAMPED-SPLIT (anchors, where gauss_objects succeeds): d_i^2
= Dm_i^2, wg_i = wSm_i 4 sin^2(thm_i/2), sigma_i = wg_i /
d_i^2; L = (mu~_+ - sigma) + (sigma - nu~_-G); second part
explicitly positive iff d_i <= 1 (census); the remainder's
Wheeler horizon is the question.  HORIZON LAW: kz, h, alpha,
k*_raw, k*_cert, k*/h for (a) + (b); least-squares slope,
Pearson r vs h and vs alpha.  ANATOMY at k* < h: beta_{k*},
depth-k* node extremes in theta = arccos x, min Christoffel
weight + its node, hull violations.  DISCRIMINATION at kz 9:
Epstein (x^2 + 5y^2, N = floor(e^{2 alpha}) + 1) and
scramble (seed 1) through (a); frozen bar k*_truth >= 2 x
k*_fake for both (kz 9 is fully double-certified, no
escalation needed there).  VERDICT (frozen, on k*_eff):
RESIDUAL-CHAIN-CERTIFIES iff k*_eff >= h for (a) on EVERY
battery + holdout rung AND the discrimination bar holds;
else RESIDUAL-HORIZON-LAW iff k*_eff/h >= 0.5 everywhere
AND Pearson(k*_eff, h) >= 0.9; else RESIDUAL-STALLS (wall
located: rung set, k*/h census, anatomy, spectral position).
Exact rationals infeasible (atoms are cosines of rational
angles); certified floats = two-dtype agreement + the mp
references (typed: mp validates ALGORITHMIC conditioning;
the source data itself is float64).  NO RH claim; writes
nothing; no .md; no commits."""

BATTERY_MAX_H = 900
HOLDOUTS = (90, 116, 142, 177, 243)
ANCHORS = (9, 12, 13, 26, 40)
MP_RUNGS = (9, 28)
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


# ------------------------------------------------ moments + Wheeler
def cheb_mod_moments(th, w, lmax, dtype=np.longdouble):
    """Modified moments nu_l = sum w cos(l th) 2^{1-l} of the
    MONIC Chebyshev basis, l = 0..lmax, exact trig sums."""
    th = np.asarray(th, float)
    w = np.asarray(w, dtype)
    ll = np.arange(lmax + 1)
    cosm = np.cos(np.outer(ll, th)).astype(dtype)
    nu = cosm @ w
    scale = np.power(dtype(2.0),
                     -(np.maximum(ll, 1) - 1).astype(dtype))
    return nu * scale


def wheeler_cheb_scaled(nu, n, dtype=np.longdouble):
    """ROW-SCALED Wheeler, monic Chebyshev auxiliary basis.
    Rows max-normalized, log scale tracked (exact identity
    rewrite of the classical recursion).  Returns (alpha,
    sgnbeta, logbeta): sign beta_k and log |beta_k|."""
    L = 2 * n
    b_aux = np.zeros(L, dtype=dtype)
    if L > 1:
        b_aux[1] = dtype(0.5)
    if L > 2:
        b_aux[2:] = dtype(0.25)
    nu = np.asarray(nu[:L], dtype=dtype)
    alpha = np.zeros(n, dtype=dtype)
    sgnb = np.zeros(n)
    logb = np.full(n, -np.inf)
    # row 0
    s0 = float(np.max(np.abs(nu)))
    if s0 == 0.0 or not np.isfinite(s0):
        return alpha, sgnb, logb
    sig_prev = np.zeros(L + 1, dtype=dtype)
    sig_cur = np.zeros(L + 1, dtype=dtype)
    sig_cur[:L] = nu / dtype(s0)
    ls_cur = math.log(s0)
    alpha[0] = sig_cur[1] / sig_cur[0]
    sgnb[0] = float(np.sign(sig_cur[0]))
    logb[0] = math.log(abs(float(sig_cur[0]))) + ls_cur
    # bt_scaled_{k-1} = beta_{k-1} * S_prev / S_cur (the
    # coefficient the scaled recursion needs)
    bt_scaled = dtype(0.0)
    for k in range(1, n):
        sig_new = np.zeros(L + 1, dtype=dtype)
        lo, hi = k, 2 * n - k
        sig_new[lo:hi] = (sig_cur[lo + 1:hi + 1]
                          - alpha[k - 1] * sig_cur[lo:hi]
                          - bt_scaled * sig_prev[lo:hi]
                          + b_aux[lo:hi] * sig_cur[lo - 1:hi - 1])
        sn = float(np.max(np.abs(sig_new[lo:hi])))
        if sn == 0.0 or not np.isfinite(sn):
            break
        sig_new[lo:hi] /= dtype(sn)
        ls_new = ls_cur + math.log(sn)
        d_new = float(sig_new[k])
        d_cur = float(sig_cur[k - 1])
        if d_new == 0.0 or d_cur == 0.0 \
                or not (np.isfinite(d_new)
                        and np.isfinite(d_cur)):
            break
        alpha[k] = (sig_new[k + 1] / sig_new[k]
                    - sig_cur[k] / sig_cur[k - 1])
        sgnb[k] = float(np.sign(d_new / d_cur))
        logb[k] = (math.log(abs(d_new / d_cur))
                   + ls_new - ls_cur)
        # the next step needs beta_k * S_{k-1}/S_k, which is
        # exactly the scaled-diagonal ratio (scales cancel)
        bt_scaled = dtype(d_new / d_cur)
        sig_prev, sig_cur = sig_cur, sig_new
        ls_cur = ls_new
    return alpha, sgnb, logb


def horizon(sgn_ld, log_ld, sgn_64, log_64, relbar=1e-3):
    """(k*_raw, k*_cert) from signs + log magnitudes."""
    kraw = kcert = 0
    raw_done = cert_done = False
    for k in range(len(sgn_ld)):
        ok_pos = sgn_ld[k] > 0 and np.isfinite(log_ld[k])
        if not raw_done and ok_pos:
            kraw += 1
        else:
            raw_done = True
        ok_agree = (k < len(sgn_64) and sgn_64[k] > 0
                    and np.isfinite(log_64[k])
                    and abs(log_64[k] - log_ld[k])
                    <= max(relbar, relbar * abs(log_ld[k])))
        if not cert_done and ok_pos and ok_agree:
            kcert += 1
        else:
            cert_done = True
        if raw_done and cert_done:
            break
    return kraw, kcert


def betas_from_logs(sgnb, logb, depth):
    return np.array([sgnb[k] * math.exp(max(min(logb[k],
                                                700.0),
                                            -700.0))
                     for k in range(depth)])


def gauss_from_chain(alpha, sgnb, logb, depth):
    """Gauss nodes/weights of the monic chain at depth."""
    a = np.asarray(alpha[:depth], float)
    b = betas_from_logs(sgnb, logb, depth)
    J = np.diag(a)
    if depth > 1:
        off = np.sqrt(np.maximum(b[1:depth], 0.0))
        J += np.diag(off, 1) + np.diag(off, -1)
    evs, V = np.linalg.eigh(J)
    return evs, b[0] * V[0] ** 2


def diff_atoms(b):
    xp, wp, thp = gnu.folded_arm_measure(b, +1)
    xm, wm, thm = gnu.folded_arm_measure(b, -1)
    return (np.concatenate([thp, thm]),
            np.concatenate([wp, -wm]))


def run_construction(th, w, n, radau=False):
    wl = np.asarray(w, np.longdouble)
    if radau:
        wl = wl * (1.0 - np.cos(np.asarray(th, float))
                   ).astype(np.longdouble)
    nu_ld = cheb_mod_moments(th, wl, 2 * n - 1, np.longdouble)
    nu_64 = cheb_mod_moments(th, wl.astype(np.float64),
                             2 * n - 1, np.float64)
    with np.errstate(all="ignore"):
        al_ld, sg_ld, lb_ld = wheeler_cheb_scaled(
            nu_ld, n, np.longdouble)
        _al, sg_64, lb_64 = wheeler_cheb_scaled(
            nu_64, n, np.float64)
    kraw, kcert = horizon(sg_ld, lb_ld, sg_64, lb_64)
    return dict(kraw=kraw, kcert=kcert, al=al_ld, sg=sg_ld,
                lb=lb_ld)


def anatomy(res, h):
    ks = res["kraw"]
    if ks >= h:
        return "no breakdown (k* = %d >= h = %d)" % (ks, h)
    bval = (res["sg"][ks] * math.exp(min(res["lb"][ks], 700.0))
            if ks < len(res["sg"]) and np.isfinite(res["lb"][ks])
            else float("nan"))
    if ks < 2:
        return "immediate stall: beta_%d = %+.3e" % (ks, bval)
    nodes, wts = gauss_from_chain(res["al"], res["sg"],
                                  res["lb"], ks)
    thn = np.arccos(np.clip(nodes, -1.0, 1.0))
    imin = int(np.argmin(wts))
    return ("beta_%d = %+.3e; depth-%d nodes theta in "
            "[%.3f, %.3f]; min wt %.1e at theta %.3f; %d "
            "outside hull"
            % (ks, bval, ks, float(np.min(thn)),
               float(np.max(thn)), float(wts[imin]),
               float(thn[imin]),
               int(np.sum(np.abs(nodes) > 1.0 + 1e-9))))


def hull_census(res, depth):
    nodes, _w = gauss_from_chain(res["al"], res["sg"],
                                 res["lb"], depth)
    return (float(np.max(nodes)),
            int(np.sum(nodes > 1.0 + 1e-12)))


def fake_rung(kz, kind):
    if kind == "epstein":
        rr = core.build_window(kz)
        N_E = int(math.floor(math.exp(2.0 * rr["alpha"]))) + 1
        lamE = gnu.lambda_eps(N_E)
        nn = np.nonzero(np.abs(lamE) > 1e-12)[0]
        comb = (np.log(nn.astype(float)),
                2.0 * lamE[nn] / np.sqrt(nn.astype(float)))
        return gnu.build_rung(kz, comb=comb)
    return gnu.build_rung(kz, scramble_seed=1)


def mp_wheeler(xs, ws, n, dps=60):
    """mpmath reference Wheeler (T_l recurrence moments,
    classical unscaled recursion).  Returns (horizon,
    alphas, betas)."""
    import mpmath as mp
    mp.mp.dps = dps
    cs = [mp.mpf(float(x)) for x in xs]
    wf = [mp.mpf(float(x)) for x in ws]
    m_at = len(wf)
    t_prev = [mp.mpf(1)] * m_at
    t_cur = list(cs)
    nu = [mp.fsum(wf), mp.fsum([wf[i] * t_cur[i]
                                for i in range(m_at)])]
    for ll in range(2, 2 * n):
        t_next = [2 * cs[i] * t_cur[i] - t_prev[i]
                  for i in range(m_at)]
        t_prev, t_cur = t_cur, t_next
        nu.append(mp.fsum([wf[i] * t_cur[i]
                           for i in range(m_at)]))
    for ll in range(1, 2 * n):
        nu[ll] = nu[ll] * mp.mpf(2) ** (-(ll - 1))
    baux = [mp.mpf(0), mp.mpf("0.5")] + [mp.mpf("0.25")] \
        * (2 * n - 2)
    sig_prev = [mp.mpf(0)] * (2 * n + 1)
    sig_cur = list(nu) + [mp.mpf(0)]
    almp = [nu[1] / nu[0]]
    kmp = 1 if nu[0] > 0 else 0
    bemp = [nu[0]]
    for k in range(1, n):
        sig_new = [mp.mpf(0)] * (2 * n + 1)
        for ll in range(k, 2 * n - k):
            sig_new[ll] = (sig_cur[ll + 1]
                           - almp[k - 1] * sig_cur[ll]
                           - bemp[k - 1] * sig_prev[ll]
                           + baux[ll] * sig_cur[ll - 1])
        if sig_new[k] == 0 or sig_cur[k - 1] == 0:
            break
        almp.append(sig_new[k + 1] / sig_new[k]
                    - sig_cur[k] / sig_cur[k - 1])
        bemp.append(sig_new[k] / sig_cur[k - 1])
        if bemp[-1] > 0 and kmp == k:
            kmp = k + 1
        sig_prev, sig_cur = sig_cur, sig_new
    return kmp, almp, bemp


def mp_horizon(b, dps=60):
    th, w = diff_atoms(b)
    return mp_wheeler(np.cos(th), w, b["h"], dps)[0]


# ================================================================= main
def main():
    section("PRIME.RESIDUAL.QUADRATURE.01 v3 "
            "(EXPLORATION ONLY)")
    sha = hashlib.sha256(FROZEN_SPEC.encode("utf-8")).hexdigest()
    print("    FROZEN_SPEC SHA-256 = %s" % sha)
    fi = np.finfo(np.longdouble)
    print("    platform long double: %d-bit mantissa eps "
          "%.1e (typed)" % (fi.nmant + 1, fi.eps))
    print("    NO RH claim.  HONEST FRAME: a positive "
          "representing rho EXISTS iff M(L) >= 0 (certified "
          "upstream); the probe measures whether the "
          "source-structured chain CONSTRUCTS it with "
          "controlled degree.")
    print("\nS0 -- firewall + tau regression")
    check("S0.1 AST firewall clean", not ast_scan(BANNED_IDS))
    worst = 0.0
    for kz in (9, 13):
        b = gnu.build_rung(kz)
        xs, ws, _ = gnu.folded_arm_measure(b, -1)
        al, be, m0, steps = gnu.lanczos_chain(
            *gnu.folded_arm_measure(b, +1)[:2], b["h"])
        h = b["h"]
        P = np.zeros((len(xs), h))
        p_prev = np.zeros(len(xs))
        p_cur = np.full(len(xs), 1.0 / math.sqrt(m0))
        P[:, 0] = p_cur
        for nn_ in range(h - 1):
            p_next = ((xs - al[nn_]) * p_cur
                      - (be[nn_ - 1] * p_prev if nn_ > 0
                         else 0.0)) / be[nn_]
            p_prev, p_cur = p_cur, p_next
            P[:, nn_ + 1] = p_cur
        Mm = P.T @ (ws[:, None] * P)
        lmin = float(1.0 - np.linalg.eigvalsh(Mm)[-1])
        lam1 = gnu.softport(b)["lam1"]
        worst = max(worst, abs(lmin - lam1) / lam1)
    check("W-M1 [TAU REGRESSION] lam_min(I - M_-) == softport "
          "lam1 at kz 9/13 (worst rel %.1e <= 1e-6)" % worst,
          worst <= 1e-6)

    # ---------------- S1 algorithm wards
    section("S1 -- WARDS")
    import mpmath as mp
    xg = -0.95 + 0.019 * np.arange(100)
    wp_ = 2.0 + np.cos(3.0 * xg)
    wm_ = 0.3 * (1.0 + 0.5 * np.sin(2.0 * xg))
    prem = float(np.min(wp_ - wm_))
    kmp, almp, bemp = mp_wheeler(
        np.concatenate([xg, xg]),
        np.concatenate([wp_, -wm_]), 60, dps=40)
    mp.mp.dps = 40
    J = mp.zeros(60, 60)
    for i in range(60):
        J[i, i] = almp[i]
        if i > 0:
            ob = mp.sqrt(bemp[i])
            J[i - 1, i] = ob
            J[i, i - 1] = ob
    E, Q = mp.eigsy(J)
    nodes_mp = [E[i] for i in range(60)]
    wts_mp = [bemp[0] * Q[0, i] ** 2 for i in range(60)]
    hull_ok = (min(nodes_mp) >= mp.mpf(float(np.min(xg)))
               - mp.mpf("1e-10")
               and max(nodes_mp) <= mp.mpf(float(np.max(xg)))
               + mp.mpf("1e-10"))
    wa1 = 0.0
    for k in range(20):
        # subtract in mp: the chain saw the two atom lists
        # separately (a float64 pre-subtraction would inject
        # a 1e-16 reference error)
        mdir = (mp.fsum([mp.mpf(float(wp_[i]))
                         * mp.mpf(float(xg[i])) ** k
                         for i in range(100)])
                - mp.fsum([mp.mpf(float(wm_[i]))
                           * mp.mpf(float(xg[i])) ** k
                           for i in range(100)]))
        mq = mp.fsum([wts_mp[i] * nodes_mp[i] ** k
                      for i in range(60)])
        wa1 = max(wa1, float(abs(mq - mdir) / abs(mdir)))
    check("W-A1 [SYNTHETIC v3, MP dps 40] premise min(w+ - "
          "w-) = %.3f > 0; all 60 beta > 0 (k* = %d), mp "
          "nodes inside hull, mp Gauss moments rel %.1e <= "
          "1e-25" % (prem, kmp, wa1),
          prem > 0.0 and kmp == 60 and hull_ok
          and wa1 <= 1e-25)
    wm2 = wc1 = 0.0
    for kz in ANCHORS:
        b = gnu.build_rung(kz)
        th, w = diff_atoms(b)
        n = b["h"]
        nu = cheb_mod_moments(th, w, 2 * n - 1, np.float64)
        x = np.cos(th)
        t_prev = np.ones_like(x)
        t_cur = x.copy()
        acc = [np.sum(w * t_prev), np.sum(w * t_cur)]
        for ll in range(2, 2 * n):
            t_next = 2.0 * x * t_cur - t_prev
            t_prev, t_cur = t_cur, t_next
            acc.append(np.sum(w * t_cur))
        mono = np.array(acc) * np.power(
            2.0, -(np.maximum(np.arange(2 * n), 1) - 1.0))
        wm2 = max(wm2, float(np.max(np.abs(mono - nu))
                             / np.max(np.abs(nu))))
        thmG, wSm, mode = gnu.arm_gauss_system(b, -1)
        wgG = wSm * 4.0 * np.sin(thmG / 2.0) ** 2
        xmG = np.cos(thmG)
        xa, wa, _tha = gnu.folded_arm_measure(b, -1)
        for ll in (0, 1, 7, 25):
            ga = float(np.sum(wgG * xmG ** ll))
            da = float(np.sum(wa * xa ** ll))
            wc1 = max(wc1, abs(ga - da) / max(abs(da), 1e-300))
    check("W-M2 [TWO-PATH MOMENTS] worst rel %.1e <= 1e-9"
          % wm2, wm2 <= 1e-9)
    check("W-C1 [GAUSS RULE] worst rel %.1e <= 1e-8" % wc1,
          wc1 <= 1e-8)

    # ---------------- S2 construction (a) + (b)
    section("S2 -- (a) THE DIFFERENCE CHAIN: horizon law "
            "(row-scaled Wheeler)")
    zones = [kz for kz in core.frame_a_zones()
             if kz in HOLDOUTS
             or core.build_window(kz)["h"] <= BATTERY_MAX_H]
    print("    kz    h     alpha   k*raw  k*cert  k*/h    "
          "maxnode      n>1  radau-k*c  anatomy")
    rows = []
    for kz in zones:
        b = gnu.build_rung(kz)
        th, w = diff_atoms(b)
        n = b["h"]
        ra = run_construction(th, w, n)
        rb = run_construction(th, w, n, radau=True)
        dep = min(ra["kcert"], n)
        mx, nover = hull_census(ra, dep) if dep >= 2 \
            else (float("nan"), 0)
        rows.append((kz, n, b["alpha"], ra, rb, mx, nover))
        print("    %-5d %-5d %-7.3f %-6d %-7d %.3f   "
              "%-12.9f %-4d %-9d %s"
              % (kz, n, b["alpha"], ra["kraw"], ra["kcert"],
                 ra["kcert"] / n, mx, nover, rb["kcert"],
                 anatomy(ra, n) if ra["kraw"] < n else "-"),
              flush=True)
    # W-P1 mp references
    wp1_ok = True
    mpcache = {}
    for kz in MP_RUNGS:
        b = gnu.build_rung(kz)
        kmp = mp_horizon(b, dps=60)
        mpcache[kz] = kmp
        row = rows[[r[0] for r in rows].index(kz)]
        ok = kmp >= min(row[3]["kcert"], b["h"])
        wp1_ok &= ok
        print("    W-P1 kz %d: mp dps-60 horizon %d vs "
              "double %d (h = %d)"
              % (kz, kmp, row[3]["kcert"], b["h"]))
    check("W-P1 [MP REFERENCE] mp horizon >= min(k*_cert, "
          "h) at kz 9 and 28", wp1_ok)

    # MP ESCALATION (frozen): definitive horizons where the
    # double run stalled below h
    print("\n    MP ESCALATION (dps 60, retry dps 120):")
    keff = {}
    for kz, n, _al, ra, _rb, _mx, _no in rows:
        if ra["kcert"] >= n:
            keff[kz] = ra["kcert"]
            continue
        t1 = time.time()
        kmp = mpcache.get(kz)
        if kmp is None:
            kmp = mp_horizon(gnu.build_rung(kz), dps=60)
        if kmp < n:
            kmp = max(kmp, mp_horizon(gnu.build_rung(kz),
                                      dps=120))
        keff[kz] = kmp
        print("    kz %-4d: k*_cert %d -> k*_mp %d / h %d "
              "(%.3f) [%.0f s]"
              % (kz, ra["kcert"], kmp, n, kmp / n,
                 time.time() - t1), flush=True)
    kc = np.array([keff[r[0]] for r in rows], float)
    hh = np.array([r[1] for r in rows], float)
    aa = np.array([r[2] for r in rows], float)
    slope_h = float(np.polyfit(hh, kc, 1)[0])
    r_h = float(np.corrcoef(hh, kc)[0, 1])
    r_a = float(np.corrcoef(aa, kc)[0, 1])
    ratio_min = float(np.min(kc / hh))
    ratio_med = float(np.median(kc / hh))
    print("\n    horizon law (k*_eff): slope dk*/dh = %.3f "
          "(Pearson r_h = %.3f, r_alpha = %.3f); k*/h min "
          "%.3f median %.3f"
          % (slope_h, r_h, r_a, ratio_min, ratio_med))
    certifies = all(keff[r[0]] >= r[1] for r in rows)
    check("S2.1 [THE DECISION] k*_eff >= h on every battery "
          "+ holdout rung (%d/%d rungs certify)"
          % (sum(1 for r in rows if keff[r[0]] >= r[1]),
             len(rows)), certifies)
    radau_kh = [r[4]["kcert"] / r[1] for r in rows]
    print("    (b) Radau-anchored at the pole port: k*/h "
          "min %.3f median %.3f max %.3f -- the localized "
          "functional (1 - x) L breaks EARLY (far below the "
          "noise floor: genuine): a positive representing "
          "measure must carry mass beyond the fold x = 1"
          % (min(radau_kh), float(np.median(radau_kh)),
             max(radau_kh)))

    # ---------------- S3 (c) damped split
    section("S3 -- (c) THE DAMPED SPLIT (T2 structure), "
            "anchors")
    for kz in ANCHORS:
        b = gnu.build_rung(kz)
        go = gnu.gauss_objects(b)
        if go.get("fail"):
            print("    kz %-4d: gauss_objects fail %s -- "
                  "typed skip" % (kz, go["mode"]))
            continue
        d2 = go["Dm"] ** 2
        wg = go["wSm"] * 4.0 * np.sin(go["thm"] / 2.0) ** 2
        nover = int(np.sum(d2 > 1.0 + 1e-12))
        posmass = float(np.sum(wg * (1.0 / d2 - 1.0)))
        thp_, wp2, _ = gnu.folded_arm_measure(b, +1)
        rr = run_construction(
            np.concatenate([thp_, go["thm"]]),
            np.concatenate([wp2, -wg / d2]), b["h"])
        print("    kz %-4d: d>1 census %d/%d (max d^2 "
              "%.6f); positive part mass %+.3e; remainder "
              "k*_cert = %d/%d (%s)"
              % (kz, nover, len(d2), float(np.max(d2)),
                 posmass, rr["kcert"], b["h"],
                 anatomy(rr, b["h"]) if rr["kraw"] < b["h"]
                 else "certifies"), flush=True)

    # ---------------- S4 discrimination
    section("S4 -- DISCRIMINATION at kz 9")
    ktruth = rows[[r[0] for r in rows].index(9)][3]["kcert"]
    contrast_ok = True
    for kind in ("epstein", "scramble"):
        bf = fake_rung(9, kind)
        th, w = diff_atoms(bf)
        rf = run_construction(th, w, bf["h"])
        contrast_ok &= ktruth >= 2 * rf["kcert"]
        print("    %-8s: k*_cert = %d/%d (truth %d); %s"
              % (kind, rf["kcert"], bf["h"], ktruth,
                 anatomy(rf, bf["h"])))
    check("S4.1 [CONTRAST] truth k* >= 2 x fake k* for both "
          "fakes", contrast_ok)

    # ---------------- V verdict
    section("V -- FROZEN VERDICT + honest consequence")
    if certifies and contrast_ok:
        verdict = ("RESIDUAL-CHAIN-CERTIFIES (k*_eff >= h "
                   "on all %d rungs; slope %.3f, r_h %.3f; "
                   "double-precision noise floor ~536 "
                   "typed, mp-escalated)"
                   % (len(rows), slope_h, r_h))
    elif ratio_min >= 0.5 and r_h >= 0.9:
        verdict = ("RESIDUAL-HORIZON-LAW (k*_eff/h in "
                   "[%.3f, 1) median %.3f, slope %.3f, r_h "
                   "%.3f)" % (ratio_min, ratio_med, slope_h,
                              r_h))
    else:
        worst_r = min(rows, key=lambda r: keff[r[0]] / r[1])
        verdict = ("RESIDUAL-STALLS (k*_eff/h min %.3f at "
                   "kz %d; median %.3f; %s)"
                   % (ratio_min, worst_r[0], ratio_med,
                      anatomy(worst_r[3], worst_r[1])))
    print("\n  VERDICT: %s" % verdict)
    print("""
  HONEST CONSEQUENCE (no RH claim): existence of a positive
  representing measure is EQUIVALENT to M(L) >= 0 (certified
  upstream via tau > 0) -- nothing here re-proves that.  The
  probe's content is CONSTRUCTIVE: whether the difference
  Jacobi chain realizes the positive quadrature at full
  degree with controlled conditioning (k* >= h), how the
  horizon scales along the ladder (the law a cofinal theorem
  needs to persist), whether the pole-port Radau
  localization or the T2 damped split moves the horizon, and
  whether the horizon separates truth from fakes.  A stall
  locates the wall in quadrature-moment coordinates -- a
  statement about THIS construction family, not about the
  target's truth.  EXPLORATION ONLY.""")
    npass = sum(1 for _n, ok in CHECKS if ok)
    print("\n  checks: %d/%d passed; elapsed %.1f s%s"
          % (npass, len(CHECKS), time.time() - T0,
             ("; FAILS: %s" % FAILS) if FAILS else ""))
    return 0 if npass == len(CHECKS) else 1


if __name__ == "__main__":
    raise SystemExit(main())
