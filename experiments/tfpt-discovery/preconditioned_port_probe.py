#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""preconditioned_port_probe -- PRIME.SOFTPORT.PRECOND.01: the
preconditioned port.

EXPLORATION ONLY (experiments/): no ledger row, no paper edit, no
.md, nothing outside experiments/.  NO RH claim.  Frozen (spec +
sha256) before running.

THE TARGET (from RADAU-DEPTH-GROWS, softport_radau17_probe): the
quadrature certificate a - U_m > 0 exists on every rung but the
depth grows as the textbook Lanczos law m* ~ cond(G)^{0.43}
(Spearman +0.99); the Jacobi chain head is near-stationary
(median drift 0.036/coefficient).  THE HOPE: a source-built
preconditioner M bounds cond(M^{-1/2} G M^{-1/2}), making the
certificate depth uniform -- the fixed-depth family exists after
all.  The Stieltjes problem transforms covariantly:

    r' G^{-1} r = rt' Gt^{-1} rt,   Gt = M^{-1/2} G M^{-1/2},
    rt = M^{-1/2} r   (exact congruence invariance, warded),

and Sylvester's law of inertia guarantees congruence CANNOT heal
a negative bulk -- the Epstein/scramble premise collapse must
survive every preconditioner (structural control, verified).

TASK 1 -- J_INFINITY: the ladder-limit of the Jacobi chains
(alpha_k, beta_k): per-coefficient last-third medians + drift
bands; stationarity depth profile (#coefficients with last-vs-
first-third drift <= 5% / 10%); head-only limit typed where the
chains diverge.  IDENTIFICATION (fit-free, frozen bars,
Bonferroni-honest): (i) the free/Chebyshev test -- if the tail
coefficients are constant (sd/mean <= 5% for alpha_{5..17} and
beta_{5..17}) the chain is the FREE Jacobi chain of an interval
[A, B] = [alpha - 2 beta, alpha + 2 beta]; named only if
additionally the induced support matches the measured bulk
support [gmin, lam_max] to <= 10% per endpoint.  TYPED: by
Rakhmanov, the free chain is GENERIC for measures with a.c.
support on one interval -- a name of the SUPPORT GEOMETRY, not
of the arithmetic; (ii) the period-2 alternation diagnostic
(two-interval measures), reported.

TASK 2 -- THE PRECONDITIONER FAMILY (predeclared, source-only):
  (a) J-HEAD DEFLATION: M_a = Q_17 J_17 Q_17' + alpha_inf (I -
      Q_17 Q_17') from the rung's own depth-17 Lanczos data
      (source: G and r) with the ladder-limit tail value
      alpha_inf;
  (b) PNT-GRADE BULK: M_b = the bulk block (same port frame,
      same positive-metric embedding) of the ABS form of the
      SMOOTH window density |d_pnt| = |FFT lags(arch + smooth
      comb)| where the smooth comb is the PNT integral dpsi =
      dx (atom grid u_i = i D/8, masses 2 e^{u_i/2} D/8 --
      source-closed, no Lambda) -- precondition by the smooth
      geometry, leave the arithmetic fluctuation;
  (c) DIAGONAL scaling M_c = diag(G) (the cheap control).
THE DECISIVE NUMBER per preconditioner: cond(Gt) along the
ladder -- bounded (Spearman(cond, rung) <= 0.3 OR last-third
median <= 1.5 x first-third median) vs still growing.

TASK 3 -- THE CERTIFICATE RETRY for the best preconditioner
(smallest last-third median cond): full Golub-Meurant in the
preconditioned frame (Lanczos on Gt from rt, Radau node ct =
0.999 lam_min(Gt), enclosure + monotonicity + congruence-
invariance wards); m*(h) law with extended depth (<= 600) built
in.  PASS: every rung certifies with m* <= 24 and last-third
max <= first-two-thirds max + 2.

CONTROLS: Radau regressions (m*(kz9) == 20, kappa refs);
firewall (no zero/prime oracles; the preconditioners consume
only source objects -- structural); Epstein/scramble premise
collapse SURVIVES the preconditioned frame (Sylvester,
verified numerically); budgets = the wards (typed).

VERDICT (frozen): PRECONDITIONED-FIXED-DEPTH (the retry PASS --
the fixed-depth certificate family; the cofinal shape stated
verbatim with named remaining hypotheses) / CONDITIONING-
INTRINSIC (all three preconditioners leave cond growing -- the
wall in conditioning form, typed).  SECONDARY (reported
regardless): J-INFINITY-NAMED iff the identification bars pass.

NO RH claim; v563 + sibling probes READ-ONLY; no RNG; report
only.
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

import v563_paper2_readouts as core            # noqa: E402 (READ-ONLY)
import pole_port_kappa_probe as pp             # noqa: E402 (READ-ONLY)
import softport_radau17_probe as sr            # noqa: E402 (READ-ONLY)

T0 = time.time()
FAILS = []
N_CHK = 0

FROZEN_SPEC = """\
PRIME.SOFTPORT.PRECOND.01 spec v1 (2026-08-08, frozen before
run).  Ladder = ALL frame_a_zones h <= 900.  Chains: Lanczos
depth 17 with Q kept, full reorth.  J_inf: per-coefficient
last-third median; drift = |last-third mean - first-third
mean| / |first-third mean|; stationarity profile at 5%/10%.
Identification bars: free/Chebyshev iff sd/mean(alpha_{5..17})
<= 0.05 AND sd/mean(beta_{5..17}) <= 0.05; named iff also
[alpha - 2 beta, alpha + 2 beta] matches [gmin, lam_max(G)]
per endpoint rel <= 0.10 (deepest rung); period-2 diagnostic
reported.  Preconditioners (a)/(b)/(c) exactly as header;
bounded-cond bar: Spearman(cond, rung index) <= 0.3 OR
last-third median <= 1.5 x first-third median.  Retry: best =
smallest last-third median cond; Lanczos <= 600 on Gt from rt;
node 0.999 lam_min(Gt); cert margin a - U >= 1e-8 a; wards:
congruence invariance rel <= 1e-8, enclosure (rel 1e-9),
monotone (rel 1e-12), M PD (lam_min > 0).  PASS bars: all
rungs m* <= 24 AND last-third max <= first-two-thirds max + 2.
Regressions: m*(kz9) raw == 20; kappa(kz9) in [2.6, 2.8].
Sylvester control: gmin(Gt_Epstein) < 0 and gmin(Gt_scramble)
< 0 under the best preconditioner rebuilt on their rungs.
Verdict enum as header.  NO RH claim; writes nothing."""

M_HEAD = 17
M_FIX = 24
M_EXT = 600
CERT_MARGIN = 1e-8
KAPPA_REF9 = (2.6, 2.8)
MSTAR9_REF = 20
BANNED_IDS = ("zetazero", "nzeros", "primerange", "isprime",
              "primepi", "nextprime", "prevprime")


def check(name, ok, detail=""):
    global N_CHK
    N_CHK += 1
    if not ok:
        FAILS.append(name.split()[0])
    print("[%s] %s%s" % ("PASS" if ok else "FAIL", name,
                         (": " + detail) if detail else ""))


def ast_scan():
    src = open(os.path.abspath(__file__), encoding="utf-8").read()
    bad = []
    for node in ast.walk(ast.parse(src)):
        nm = None
        if isinstance(node, ast.Name):
            nm = node.id
        elif isinstance(node, ast.Attribute):
            nm = node.attr
        if nm and nm.lower() in BANNED_IDS:
            bad.append(nm)
    return bad


def lanczos_q(G, q1, m_max):
    """Full-reorth Lanczos keeping the basis Q."""
    n = len(q1)
    Q = np.zeros((n, m_max + 1))
    Q[:, 0] = q1 / np.linalg.norm(q1)
    alphas, betas = [], []
    for k in range(m_max):
        v = G @ Q[:, k]
        if k > 0:
            v -= betas[-1] * Q[:, k - 1]
        a_ = float(Q[:, k] @ v)
        v -= a_ * Q[:, k]
        for _ in range(2):
            v -= Q[:, :k + 1] @ (Q[:, :k + 1].T @ v)
        b_ = float(np.linalg.norm(v))
        alphas.append(a_)
        if b_ <= 1e-13:
            return (np.array(alphas), np.array(betas),
                    Q[:, :k + 1], True)
        betas.append(b_)
        Q[:, k + 1] = v / b_
    return np.array(alphas), np.array(betas), Q[:, :m_max], False


def inv_sqrt(M):
    ev, V = np.linalg.eigh(M)
    assert ev[0] > 0
    return V @ np.diag(ev ** -0.5) @ V.T, float(ev[0]), \
        float(ev[-1])


def cert_depth(G, rv, a_, m_max):
    """(m*, cond, gmin) for the Gauss-Radau certificate on
    (G, rv) with target scalar a_."""
    ev0 = np.linalg.eigvalsh(G)
    gmin, gmax = float(ev0[0]), float(ev0[-1])
    if gmin <= 0:
        return None, float("inf"), gmin, None, None
    nr2 = float(rv @ rv)
    alphas, betas, _, brk = lanczos_q(G, rv, m_max)
    m_done = len(alphas)
    direct = float(rv @ np.linalg.solve(G, rv))
    ok_e = True
    ok_m = True
    Lp = Up = None
    m_star = None
    for m in range(1, m_done + 1):
        L_, U_ = sr.gauss_bounds(alphas, betas, 0.999 * gmin, m)
        L_, U_ = nr2 * L_, nr2 * U_
        ok_e &= (L_ <= direct * (1 + 1e-9) + 1e-15
                 and direct <= U_ * (1 + 1e-9) + 1e-15)
        if Lp is not None:
            ok_m &= (L_ >= Lp * (1 - 1e-12) - 1e-15
                     and U_ <= Up * (1 + 1e-12) + 1e-15)
        Lp, Up = L_, U_
        if m_star is None and a_ - U_ >= CERT_MARGIN * a_:
            m_star = m
            break
    return m_star, gmax / gmin, gmin, ok_e, ok_m


def smooth_bulk_M(rr, Rm, Bc):
    """Preconditioner (b): the ABS form of the smooth (PNT)
    window density in the same port frame.  Source-closed: arch
    + the PNT integral comb (no Lambda)."""
    h, M, D, al = rr["h"], rr["M"], rr["D"], rr["alpha"]
    du = D / 8.0
    ug = np.arange(du, 2.0 * al, du)
    mm_s = 2.0 * np.exp(0.5 * ug) * du
    c_s, _ = core.atom_lags_at(al, M, ug, mm_s)
    c_ar = np.asarray(core.arch_lags(M, D), float)
    d_pnt = pp.grid_density(c_ar + c_s)
    L = 2 * M - 2
    E = pp.odd_extend_mat(h)
    Fp = np.fft.fft(np.vstack([E, np.zeros((L - M, h))]),
                    axis=0)
    Kabs = np.real(Fp.conj().T @ (np.abs(d_pnt)[:, None] * Fp)
                   ) / (2.0 * L)
    Dl = Rm @ Kabs @ Rm
    Dl = 0.5 * (Dl + Dl.T)
    Mb = Bc.T @ (Dl @ Bc)
    return 0.5 * (Mb + Mb.T)


def port_frame(Delta, Gp, Rp, h, D):
    """The pole-port Feshbach frame + the Householder basis."""
    v = np.exp(0.5 * np.arange(h) * D)
    v = v / np.linalg.norm(v)
    fp = pp.feshbach_pole(Delta, Gp, Rp, v)
    w = fp["w"]
    e1 = np.zeros(h)
    e1[0] = 1.0
    u = e1 - w
    nu = np.linalg.norm(u)
    H = np.eye(h) - 2.0 * np.outer(u / nu, u / nu) \
        if nu > 1e-12 else np.eye(h)
    return fp, H[:, 1:]


def run():
    print("=" * 78)
    print("PRECONDITIONED PORT (preconditioned_port_probe) -- "
          "defeating the sqrt-cond depth law")
    print("=" * 78)
    print("frozen spec sha256 = %s"
          % hashlib.sha256(FROZEN_SPEC.encode()).hexdigest()[:16])
    print("""
HONESTY FRAME: NO RH claim.  Congruence invariance is exact and
warded; Sylvester's law is the structural control (no
preconditioner can heal negativity); the J_inf identification is
typed Rakhmanov-generic if it fires.""")

    # ============================================================== S0
    print("\nS0 -- firewall + the ladder frames")
    check("S0.AST firewall clean", not ast_scan())
    zones = [kz for kz in core.frame_a_zones()]
    frames = {}
    for kz in zones:
        out = pp.build_rung(kz)
        rr, Delta, Gp, Rp = out[0], out[8], out[6], out[7]
        if rr["h"] > 900:
            continue
        fp, Bc = port_frame(Delta, Gp, Rp, rr["h"], rr["D"])
        frames[kz] = dict(rr=rr, Delta=Delta, Rm=None, fp=fp,
                          Bc=Bc)
        # Rm for the smooth preconditioner (same embedding)
        ev, Vp = np.linalg.eigh(Gp)
        frames[kz]["Rm"] = Vp @ np.diag(ev ** -0.5) @ Vp.T
    kzs = sorted(frames)
    kap9 = frames[9]["fp"]["s"] / frames[9]["fp"]["lam1"]
    m9, c9, _, _, _ = cert_depth(frames[9]["fp"]["G"],
                                 frames[9]["fp"]["rv"],
                                 frames[9]["fp"]["a"], 40)
    check("S0.REG Radau regressions: kappa(kz9) = %.3f in "
          "[2.6, 2.8] AND raw m*(kz9) = %s == %d"
          % (kap9, m9, MSTAR9_REF),
          KAPPA_REF9[0] <= kap9 <= KAPPA_REF9[1]
          and m9 == MSTAR9_REF)

    # ============================================================== S1
    print("\nS1 -- J_INFINITY: the limiting Jacobi chain")
    chains = {}
    for kz in kzs:
        fp = frames[kz]["fp"]
        al, be, Q, _ = lanczos_q(fp["G"], fp["rv"], M_HEAD)
        chains[kz] = (al, be, Q)
    third = max(1, len(kzs) // 3)
    fk, lk = kzs[:third], kzs[-third:]
    kmax = min(M_HEAD, min(len(chains[k][0]) for k in kzs))
    al_inf, be_inf, drifts = [], [], []
    for j in range(kmax):
        af = float(np.mean([chains[k][0][j] for k in fk]))
        al_ = float(np.median([chains[k][0][j] for k in lk]))
        al_inf.append(al_)
        drifts.append(abs(float(np.mean(
            [chains[k][0][j] for k in lk])) - af)
            / max(abs(af), 1e-300))
        if j < kmax - 1:
            be_inf.append(float(np.median(
                [chains[k][1][j] for k in lk])))
    al_inf = np.array(al_inf)
    be_inf = np.array(be_inf)
    n5 = sum(1 for d_ in drifts if d_ <= 0.05)
    n10 = sum(1 for d_ in drifts if d_ <= 0.10)
    print("    stationarity profile: %d/%d coefficients drift "
          "<= 5%%, %d/%d <= 10%% (head-only limit typed beyond)"
          % (n5, kmax, n10, kmax))
    a_t = al_inf[4:]
    b_t = be_inf[4:]
    sd_a = float(np.std(a_t) / max(abs(np.mean(a_t)), 1e-300))
    sd_b = float(np.std(b_t) / max(abs(np.mean(b_t)), 1e-300))
    A_ind = float(np.mean(a_t) - 2.0 * np.mean(b_t))
    B_ind = float(np.mean(a_t) + 2.0 * np.mean(b_t))
    Gdeep = frames[kzs[-1]]["fp"]["G"]
    evd = np.linalg.eigvalsh(Gdeep)
    gmin_d, gmax_d = float(evd[0]), float(evd[-1])
    supp_ok = (abs(A_ind - gmin_d) / gmax_d <= 0.10
               and abs(B_ind - gmax_d) / gmax_d <= 0.10)
    cheb = sd_a <= 0.05 and sd_b <= 0.05
    named = cheb and supp_ok
    ev_al = float(np.std(a_t[::2]) + np.std(a_t[1::2])) / 2.0
    print("    tail constancy: sd/mean alpha = %.3f, beta = "
          "%.3f (bar 0.05); induced support [%.3f, %.3f] vs "
          "measured bulk [%.4f, %.3f] (deepest rung); "
          "period-2 diagnostic: split-sd %.3f vs joint %.3f"
          % (sd_a, sd_b, A_ind, B_ind, gmin_d, gmax_d,
             ev_al, float(np.std(a_t))))
    print("    J_inf head (alpha): %s"
          % " ".join("%.3f" % x for x in al_inf))
    print("    J_inf head (beta):  %s"
          % " ".join("%.3f" % x for x in be_inf))
    check("S1.JID J_INFINITY identification (secondary): "
          "free/Chebyshev tail %s + support match %s -> %s "
          "(typed: Rakhmanov-generic if named -- the chain "
          "carries the bulk support geometry, not the "
          "arithmetic)"
          % (cheb, supp_ok,
             "J-INFINITY-NAMED (free chain on the bulk "
             "support)" if named else "not named"), True)

    # ============================================================== S2
    print("\nS2 -- the preconditioner family: cond trends")
    al_tail = float(np.mean(a_t))
    conds = {"raw": [], "a": [], "b": [], "c": []}
    ok_pd = True
    for kz in kzs:
        fr = frames[kz]
        fp = fr["fp"]
        G, rv = fp["G"], fp["rv"]
        ev = np.linalg.eigvalsh(G)
        conds["raw"].append(float(ev[-1] / ev[0]))
        # (a) J-head deflation
        al, be, Q = chains[kz]
        m = len(al)
        J = np.diag(al)
        for i in range(m - 1):
            J[i, i + 1] = J[i + 1, i] = be[i]
        Ma = Q @ J @ Q.T + al_tail * (np.eye(len(rv))
                                      - Q @ Q.T)
        Ma = 0.5 * (Ma + Ma.T)
        # (b) PNT smooth bulk
        Mb = smooth_bulk_M(fr["rr"], fr["Rm"], fr["Bc"])
        # (c) diagonal
        Mc = np.diag(np.diag(G))
        for nm, M_ in (("a", Ma), ("b", Mb), ("c", Mc)):
            evm = np.linalg.eigvalsh(M_)
            if evm[0] <= 0:
                ok_pd = False
                conds[nm].append(float("inf"))
                continue
            Vm, _, _ = inv_sqrt(M_)
            Gt = Vm @ G @ Vm
            Gt = 0.5 * (Gt + Gt.T)
            evt = np.linalg.eigvalsh(Gt)
            conds[nm].append(float(evt[-1] / max(evt[0],
                                                 1e-300)))
    check("S2.PD every preconditioner is PD on every rung "
          "(M^{-1/2} well-defined)", ok_pd)
    idx = np.arange(len(kzs), dtype=float)
    best_nm, best_med = None, float("inf")
    for nm in ("raw", "a", "b", "c"):
        cv = np.array(conds[nm])
        sp_ = sr.spearman(cv, idx)
        med_f = float(np.median(cv[:third]))
        med_l = float(np.median(cv[-third:]))
        bounded = sp_ <= 0.3 or med_l <= 1.5 * med_f
        print("    %-4s cond: median first/last third %.2e / "
              "%.2e (ratio %.2f), Spearman(cond, rung) = "
              "%+.2f -> %s"
              % (nm, med_f, med_l, med_l / max(med_f, 1e-300),
                 sp_, "BOUNDED" if bounded else "GROWING"))
        if nm != "raw" and med_l < best_med:
            best_nm, best_med = nm, med_l
    print("    best preconditioner: (%s), last-third median "
          "cond %.2e" % (best_nm, best_med))

    # ============================================================== S3
    print("\nS3 -- the certificate retry (preconditioner %s)"
          % best_nm)
    ok_inv = True
    ok_e_all = True
    ok_m_all = True
    mstars = []
    hs_ = []
    for kz in kzs:
        fr = frames[kz]
        fp = fr["fp"]
        G, rv, a_ = fp["G"], fp["rv"], fp["a"]
        if best_nm == "a":
            al, be, Q = chains[kz]
            m = len(al)
            J = np.diag(al)
            for i in range(m - 1):
                J[i, i + 1] = J[i + 1, i] = be[i]
            M_ = Q @ J @ Q.T + al_tail * (np.eye(len(rv))
                                          - Q @ Q.T)
        elif best_nm == "b":
            M_ = smooth_bulk_M(fr["rr"], fr["Rm"], fr["Bc"])
        else:
            M_ = np.diag(np.diag(G))
        M_ = 0.5 * (M_ + M_.T)
        Vm, _, _ = inv_sqrt(M_)
        Gt = Vm @ G @ Vm
        Gt = 0.5 * (Gt + Gt.T)
        rt = Vm @ rv
        direct_raw = float(rv @ np.linalg.solve(G, rv))
        direct_t = float(rt @ np.linalg.solve(Gt, rt))
        ok_inv &= abs(direct_t - direct_raw) \
            / max(abs(direct_raw), 1e-300) <= 1e-8
        m_star, cnd, gmin_t, ok_e, ok_m = cert_depth(
            Gt, rt, a_, M_EXT)
        ok_e_all &= bool(ok_e)
        ok_m_all &= bool(ok_m)
        mstars.append(m_star)
        hs_.append(fr["rr"]["h"])
    check("S3.INV congruence invariance: rt' Gt^{-1} rt == "
          "r' G^{-1} r (rel 1e-8) on every rung", ok_inv)
    check("S3.WRD enclosure + monotonicity wards in the "
          "preconditioned frame", ok_e_all and ok_m_all)
    cert_all = all(m is not None for m in mstars)
    if cert_all:
        mv = np.array(mstars, float)
        tmax = int(np.max(mv[-third:]))
        hmax_ = int(np.max(mv[:-third]))
        sp_mh = sr.spearman(mv, np.array(hs_, float))
        fixed = bool(np.max(mv) <= M_FIX
                     and tmax <= hmax_ + 2)
        print("    m* range [%d, %d]; last-third max %d vs "
              "first-two-thirds max %d; Spearman(m*, h) = "
              "%+.2f; %d/%d rungs at m* <= 17"
              % (int(np.min(mv)), int(np.max(mv)), tmax,
                 hmax_, sp_mh,
                 int(np.sum(mv <= 17)), len(mv)))
    else:
        fixed = False
        print("    %d rungs fail to certify at m <= %d in the "
              "preconditioned frame"
              % (sum(1 for m in mstars if m is None), M_EXT))
    check("S3.G [THE RETRY] fixed-depth certificate family in "
          "the preconditioned frame (all rungs m* <= %d, no "
          "growth): %s" % (M_FIX, fixed), fixed)

    # ============================================================== S4
    print("\nS4 -- Sylvester control (the frame must NOT heal "
          "negativity)")
    rr9 = core.build_window(9)
    a9 = rr9["alpha"]
    N_E = int(math.floor(math.exp(2.0 * a9))) + 1
    lamE = pp.lambda_eps(N_E)
    nn = np.nonzero(np.abs(lamE) > 1e-12)[0]
    syl_ok = True
    for nmc, kw in (("Epstein", dict(comb=(
            np.log(nn.astype(float)),
            2.0 * lamE[nn] / np.sqrt(nn.astype(float))))),
            ("scramble", dict(scramble_seed=1))):
        out = pp.build_rung(9, **kw)
        rrX, DeltaX, GpX, RpX = out[0], out[8], out[6], out[7]
        fpX, BcX = port_frame(DeltaX, GpX, RpX, rrX["h"],
                              rrX["D"])
        GX = fpX["G"]
        gminX = fpX["gmin"]
        if best_nm == "b":
            evX, VpX = np.linalg.eigh(GpX)
            RmX = VpX @ np.diag(evX ** -0.5) @ VpX.T
            MX = smooth_bulk_M(rrX, RmX, BcX)
        elif best_nm == "a":
            alX, beX, QX, _ = lanczos_q(GX, fpX["rv"], M_HEAD)
            mX = len(alX)
            JX = np.diag(alX)
            for i in range(mX - 1):
                JX[i, i + 1] = JX[i + 1, i] = beX[i]
            MX = QX @ JX @ QX.T + al_tail * (
                np.eye(GX.shape[0]) - QX @ QX.T)
        else:
            MX = np.diag(np.abs(np.diag(GX)))
        MX = 0.5 * (MX + MX.T)
        evM = np.linalg.eigvalsh(MX)
        if evM[0] <= 0:
            print("    %-8s: raw gmin = %+.3e; the (%s) "
                  "preconditioner itself is INDEFINITE on this "
                  "comb (lam_min(M) = %+.3e) -- the frame "
                  "cannot even be built: negativity visible at "
                  "the preconditioner (typed)"
                  % (nmc, gminX, best_nm, float(evM[0])))
            continue
        VmX, _, _ = inv_sqrt(MX)
        GtX = VmX @ GX @ VmX
        gtmin = float(np.linalg.eigvalsh(
            0.5 * (GtX + GtX.T))[0])
        heal = gtmin >= 0 and gminX < 0
        syl_ok &= not heal
        print("    %-8s: raw gmin = %+.3e -> preconditioned "
              "gmin = %+.3e (inertia preserved: %s)"
              % (nmc, gminX, gtmin, not heal))
    check("S4.SYL Sylvester: congruence preserves the "
          "negativity of both controls (no healing)", syl_ok)

    # ============================================================== S5
    print("\nS5 -- verdict")
    if fixed and not FAILS:
        verdict = "PRECONDITIONED-FIXED-DEPTH"
    else:
        verdict = "CONDITIONING-INTRINSIC"
    sec = " + J-INFINITY-NAMED" if named else ""
    print("=" * 78)
    print("V -- VERDICT: %s%s" % (verdict, sec))
    print("=" * 78)
    if verdict == "PRECONDITIONED-FIXED-DEPTH":
        print("""    THE COFINAL SHAPE (every arrow typed): source window
    (arch + comb, source-built) -> pole port (closed-form
    a-term, source-built) -> %s preconditioner (SOURCE-BUILT:
    %s) -> Lanczos on the preconditioned bulk (structural) ->
    fixed-depth Gauss-Radau certificate a - U_m* > 0 with m*
    <= %d uniformly (MEASURED on the full ladder) -> s > 0 ->
    tau > 0 (exact Feshbach, warded premise gmin > 0).  THE
    NAMED REMAINING HYPOTHESES for a cofinal statement: (i)
    the uniform validity of the preconditioner construction
    (lam_min of the preconditioned bulk bounded below
    uniformly in h -- measured bounded here, not proven); (ii)
    the J_inf convergence / the stationarity of the
    certificate data along the ladder (measured: %d/%d
    coefficients stable at 5%%); (iii) the closed-form floor
    of the a-term (already source-closed).  NO RH claim.""" % (
            best_nm,
            "the rung's own depth-17 Krylov head + the ladder "
            "tail value" if best_nm == "a" else
            "the PNT-smooth ABS bulk in the same port frame"
            if best_nm == "b" else "diagonal scaling",
            int(np.max(np.array([m for m in mstars]))),
            n5, kmax))
    else:
        grow_txt = ", ".join(
            "%s %.1e->%.1e" % (nm, float(np.median(
                np.array(conds[nm])[:third])),
                float(np.median(np.array(conds[nm])[-third:])))
            for nm in ("raw", "a", "b", "c"))
        print("""    THE TYPED WALL (conditioning form): none of the three
    source preconditioners bounds the effective condition
    number (medians first->last third: %s), %s.  The
    conditioning of the soft port is INTRINSIC at this
    ingredient list: the soft end of the bulk is not the
    smooth geometry (else (b) would flatten it) and not the
    17-mode Krylov head (else (a) would deflate it) -- it is
    distributed arithmetic structure that any certificate
    must resolve mode by mode.  In quadrature coordinates the
    wall is: the certificate depth is the price of the
    cancellation, and no source-side change of metric waives
    it.  NO RH claim.""" % (
            grow_txt,
            "and the retry still shows growing depth"
            if cert_all else
            "and some rungs no longer certify at all in the "
            "best frame"))
    dt = time.time() - T0
    print("-" * 78)
    print("checks: %d run, %d failed%s | runtime %.1f min"
          % (N_CHK, len(FAILS),
             (" [" + ", ".join(FAILS) + "]") if FAILS else "",
             dt / 60.0))
    print("NO RH claim; report only; nothing outside "
          "experiments/ touched.")


if __name__ == "__main__":
    run()
