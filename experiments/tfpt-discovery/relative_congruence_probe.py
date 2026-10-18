#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""relative_congruence_probe -- PRIME.PORT.RELCONG.01
(EXPLORATION ONLY, experiments/; round 51, reviewer priority 1:
make round 50's one-sided law EXACT and COMPLETE -- the clean
inheritance form A_{h+1} = A_h^{1/2} (I + H_h) A_h^{1/2} with
H_h hermitian, plus full non-normality diagnostics and the
margin ladder.  2026-08-09.)

THE QUESTION (frozen): factor_avoidance_euler_probe (round 50)
measured the one-sided law max_steps(-min mu) = 0.9950 < 1 on all
31 truth steps, mu = eigenvalues of W^{-1} Delta C with
W = A_h = I - C_J(h) symmetric PD on truth and Delta C symmetric.
The reviewer's point: W^{-1} Delta C is similar to the HERMITIAN
H_h = A_h^{-1/2} Delta_h A_h^{-1/2} -- make this exact and
complete.  The clean object is the CONGRUENCE, not the
non-normal product; rho(W^{-1} Delta C) was a statistic of a
non-normal operator and must be audited as such.

THE HERMITIAN INHERITANCE MINI-THEOREM (stated up front;
elementary, and the R5 deliverable): let A_h be symmetric
positive definite and Delta_h symmetric, with
A_{h+1} = A_h + Delta_h.  Put
    H_h := A_h^{-1/2} Delta_h A_h^{-1/2}    (hermitian -- here
                                             real symmetric).
Then EXACTLY
    A_{h+1} = A_h^{1/2} (I + H_h) A_h^{1/2},
a *congruence* of I + H_h.  By Sylvester's law of inertia
A_{h+1} is positive definite  <=>  I + H_h is positive definite
<=>  lambda_min(H_h) > -1  <=>  eta_h := 1 + lambda_min(H_h) > 0.
Moreover A_h^{-1} Delta_h = A_h^{-1/2} H_h A_h^{1/2}, so
W^{-1} Delta C is SIMILAR to H_h: its spectrum is exactly real
and equals eig(H_h) -- round 50's mu-ledger was the spectrum of
this hermitian object seen through a non-normal similarity.
THE FULL LADDER INDUCTION therefore reduces to
  (i)  one certified base rung A_{h0} PD (exists: v884 certified
       head positivity / v887 certified ladder), and
  (ii) THE MARGIN INEQUALITY (the named inequality):
           eta_h = 1 + lambda_min(H_h) > 0   for every step h.
The probe measures the finite shadow of (ii) on the deployed
ladder and asks whether eta_h is LAWFUL (predictable from step
sources) or merely measured.

THE LADDER (frozen, factor_avoidance verbatim): all frame-A
zones (core.frame_a_zones()) with h <= 900, sorted by (h, kz);
consecutive FULL-WINDOW pairs (both rungs carry all 12 indices
of J = {2, 4, ..., 24}; typed skips counted); truth + smooth-
mass world (B1 LATTICE-SMOOTH masses m_n = 2 e^{u_n/2} du_n,
midpoint cells, lattice_parametrix verbatim); Epstein/scramble
frame status reported (C1).

FROZEN PROTOCOL (2026-08-09; all bars frozen before the run):

 R1  THE EXACT CONGRUENCE (per truth full-window step):
     A_h = I - C_J(h) (12x12), Delta_h = C_J(h) - C_J(h+1) so
     A_{h+1} = A_h + Delta_h; symmetric eigendecomposition
     A_h = V diag(w) V^T (eigh), A_h^{+-1/2} = V diag(w^{+-1/2})
     V^T; H_h = A_h^{-1/2} Delta_h A_h^{-1/2}.  WARDS (kill ->
     WARD-BROKEN):
       R1.a SYMMETRIZATION: ||H - H^T||_F / ||H||_F <= 1e-12
            on every step (exact hermitian object);
       R1.b RECONSTRUCTION: ||A_h^{1/2} (I + H_h) A_h^{1/2}
            - A_{h+1}||_F / ||A_{h+1}||_F <= 1e-10 (the exact
            identity);
       R1.c SIMILARITY: sorted eig(H_h) == sorted real parts of
            eig(W^{-1} Delta C) (general nonsymmetric solver)
            within 1e-9 relative, and max |Im mu| <= 1e-9
            (1 + |mu|) -- this pins round 50's mu-ledger to the
            hermitian spectrum;
       R1.d REPRODUCTION (round-50 ledger): 31 truth full-window
            pairs, 0 crossings, min eta = 0.0050 and
            max(-lambda_min(H)) = 0.9950 (print precision, tol
            5.001e-5).

 R2  THE MARGIN LADDER (the deliverable): per step
     eta_h = 1 + lambda_min(H_h); the FULL ladder printed with
     h, flow, lambda_min, eta, tau_h = lambda_min(A_h), the
     spectral gap g_h = lambda_2(A_h) - lambda_min(A_h),
     ||Delta_h||_F, the moving-block atom mass, and the
     soft-mode overlap |<v_min, s_h>| (v_min = A_h^{-1/2}-
     transported normalized minimizing eigenvector of H_h,
     s_h = eigenvector of A_h at its smallest eigenvalue).
     TREND (leave-last-third-out, frozen): sort by h, fit OLS
     on the first ceil(2n/3) steps, score RMSE on the held-out
     last third, for the three frozen candidates
       POWER  log eta ~ a + b log h,
       LOG    log eta ~ a + b log log h,
       EXP    log eta ~ a + b h;
     report in-sample R^2 + held-out RMSE, best = smallest
     held-out RMSE; and the shrink comparison: the POWER slope
     of eta vs the POWER slopes of tau_h, g_h, ||Delta_h||_F
     (does eta shrink like tau? like the gap?).
     THE SOURCE QUESTION (frozen table): corr(log eta, z) and
     R^2 = corr^2 for z in { log(moving-block atom mass),
     log ||Delta_h||_F, log tau_h, log g_h, ovl (raw) }.
     TYPED: MARGIN-LAWFUL iff some single source reaches
     R^2 >= 0.8; MARGIN-UNEXPLAINED otherwise (honest).

 R3  NON-NORMALITY DIAGNOSTICS (the reviewer's mandated
     additions, per truth step, for M = W^{-1} Delta C computed
     by the general solver): ||M||_2 (operator norm, largest
     singular value), lambda_min of the symmetric part
     (M + M^T)/2, the eigenvector condition number kappa(V) of
     M (2-norm cond of the eig eigenvector matrix), printed
     alongside rho(M) = max |mu| and the bound check
     kappa(V) <= sqrt(cond(A_h)) (similarity transport).  THE
     CENSUS: per-step non-normality ratio ||M||_2 / rho; typed
     RHO-MISLEADING iff the ratio >= NN_RATIO_BAR = 3 on >= 1/2
     of the steps (rho then materially understates the operator
     as a NORM statistic), RHO-FAITHFUL otherwise.  STATED
     EITHER WAY: the spectrum itself was always exact (R1.c
     similarity) -- what non-normality breaks is norm reasoning
     (||M||_2, transient growth, symmetric-part bounds), and
     the honest object carrying the inheritance is the
     hermitian H_h.

 R4  THE SMOOTH WORLD (same ladder, B1 smooth masses): per
     full-window step, if A_h is PD the same H_h ladder
     (lambda_min, eta); if A_h is NOT PD the real congruence
     form is unavailable -- typed CONE-EXITED and counted (the
     general-branch crossing flag still computed, predecessor
     verbatim).  WHERE DOES lambda_min(H) CROSS -1: first
     eta < 0 step printed.  WARD (kill -> WARD-BROKEN,
     round-50 ledger): 28 smooth full-window pairs, 22 crossing
     steps (Q < 0 or a real factor < 0), first crossing at
     h 210 -> 218, Q < 0 on 16 steps.  THE CONTRAST: truth
     min eta vs smooth min eta (PD steps) and the count of
     smooth eta < 0 -- the discriminating gap, printed.  TYPED:
     SMOOTH-DISCRIMINATES iff truth min eta > 0 AND (some
     smooth PD step has eta < 0 OR some smooth step is
     CONE-EXITED); SMOOTH-NONDISCRIMINATING otherwise.

 R5  THE MINI-THEOREM, NUMERICALLY (report + ward): on every
     truth step verify that eta_h > 0 AND the reconstructed
     A_{h+1} = A_h^{1/2}(I + H_h)A_h^{1/2} has
     lambda_min > 0 (Sylvester inheritance, one step, exact);
     print the induction statement with the measured eta ladder
     as its finite shadow: certified base (v884/v887) +
     eta_h > 0 for all h  =>  A_h PD for all h.  No claim
     beyond the deployed ladder.

 C   CONTROLS: (C1, kz 9, must fire, kill -> CONTROL-DEAD)
     Epstein (lambda_eps recursion comb) + scramble (seed 1):
     the compressed frame must die (exterior supercritical OR
     lam(C_J) > 1 OR window unavailable); channel reported.
     (C2) the SMOOTH-MASS world is the PRIMARY embedded
     control; its detection (crossings present) is
     ward-anchored in R4 -- if the smooth ladder shows no
     crossing the probe is CONTROL-DEAD.

 W   PIPELINE WARDS (kill -> PIPELINE-BROKEN): W1 >= 30 truth
     rungs; W1b the atom prefix law exact; W2 A_h symmetric PD
     on every truth full-window rung; W3 >= 20 truth
     full-window pairs.

KILLS: K1 pipeline ward breaks -> PIPELINE-BROKEN; KW an R1/R4
reproduction / symmetrization / reconstruction / similarity
ward breaks -> WARD-BROKEN; K3 controls silent -> CONTROL-DEAD.

VERDICT (frozen enum): RELCONG-MEASURED with typed sublabels
MARGIN-LAWFUL / MARGIN-UNEXPLAINED (R2), RHO-MISLEADING /
RHO-FAITHFUL (R3), SMOOTH-DISCRIMINATES /
SMOOTH-NONDISCRIMINATING (R4); else PIPELINE-BROKEN /
WARD-BROKEN / CONTROL-DEAD.

SPEC v2 (2026-08-09, after run 1; fail-first preserved -- run 1
passed ALL 16 checks; no bar was moved and every run-1 number
stands; two REPORT-ONLY prints are documented/clarified):

 (i)  R3 kappa bound bookkeeping: the transport inequality
      kappa(V) <= sqrt(cond A_h) holds for the OPTIMALLY
      COLUMN-SCALED diagonalizer of W^{-1}Delta (the
      A_h^{1/2}-transported orthonormal eigenbasis);
      np.linalg.eig returns UNIT columns, whose condition
      number can exceed the optimal one by the column-scaling
      ambiguity (run 1 measured excesses of order 10%, e.g.
      kappa 84.3 vs bound 80.0 at h 149->151).  The print is
      annotated accordingly; the raw kappa numbers stand and
      the diagnostic remains report-only (never a ward).

 (ii) R4 zero-PD bookkeeping: run 1 measured that A_h is
      indefinite on EVERY smooth full-window pair (28/28
      CONE-EXITED; the smooth pair ladder only begins at
      h 210, after 13 typed skips) -- the measured answer to
      "where does lambda_min(H) cross -1" is that the smooth
      world exits the PD cone BEFORE its full-window pair
      ladder even starts, so the PD-branch eta ladder is
      EMPTY there.  The contrast print handles the empty PD
      branch explicitly ("none" instead of nan); the
      SMOOTH-DISCRIMINATES typing bar (frozen in R4) already
      covered this case via the CONE-EXITED count and is
      unchanged.

NO RH claim -- a per-step congruence measurement on compressed
window truncations is a statement about the deployed ladder,
not a theorem about zeros.

FIREWALL: no zeros, no prime oracles (AST scan; banned ids
zetazero / nzeros / primerange / isprime / primepi / nextprime /
prevprime); v563 READ-ONLY; RNG only inside the declared
scramble control; stdout only.  No marker moves.

Sources (read-only): v563_paper2_readouts (U_ALL / MU_ALL
prefix law, build_window, atom_lags_at, arch_lags -- read
verbatim); window compression + smooth-mass world verbatim from
factor_avoidance_euler_probe.py (PRIME.PORT.FACTORAVOID.01,
round 50) via tau_mobius_factor_probe.py
(PRIME.PORT.TAU.MOEBIUS.01, the exact quotient identity) and
lattice_parametrix_probe.py (B1); certified base rungs:
v884_certified_head_positivity / v887_certified_ladder_complete
(cited as the induction base, not re-run here).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/relative_congruence_probe.py
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
MIN_RUNGS = 30
MIN_PAIRS = 20
MIN_COMMON_J = 8
ASYM_WARD = 1e-12           # R1.a symmetrization (kill)
RECON_WARD = 1e-10          # R1.b reconstruction (kill)
SIM_WARD = 1e-9             # R1.c similarity (kill)
R2_BAR = 0.8                # R2 MARGIN-LAWFUL bar
HOLDOUT_FRAC = 3            # R2 leave-last-1/3-out
NN_RATIO_BAR = 3.0          # R3 non-normality ratio bar
NN_STEP_FRAC = 0.5          # R3 RHO-MISLEADING step fraction
CTRL_KZ = 9
BANNED_IDS = ("zetazero", "nzeros", "primerange", "isprime",
              "primepi", "nextprime", "prevprime")

# R1.d / R4 reproduction wards (factor_avoidance_euler_probe +
# tau_mobius_factor_probe printed ledgers, round 50)
REF_N_TRUTH_PAIRS = 31
REF_TRUTH_CROSS = 0
REF_TRUTH_MINETA = 0.0050
REF_TRUTH_MAXNEG = 0.9950
REF_N_SMOOTH_PAIRS = 28
REF_SMOOTH_CROSS = 22
REF_SMOOTH_FIRST = (210, 218)
REF_SMOOTH_QNEG = 16
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


# --------- pipeline, verbatim from factor_avoidance_euler_probe
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


def rung_win(kz, scramble_seed=None, comb=None, rr_cache=None):
    """One rung -> 12x12 window compression (factor_avoidance
    verbatim)."""
    b = build_rung(kz, scramble_seed=scramble_seed, comb=comb,
                   rr_cache=rr_cache)
    h, L = b["h"], b["L"]
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
    return out


def eps_comb(kz):
    rr = core.build_window(kz)
    N_E = int(math.floor(math.exp(2.0 * rr["alpha"]))) + 1
    lamE_ = lambda_eps(N_E)
    nn = np.nonzero(np.abs(lamE_) > 1e-12)[0]
    return (np.log(nn.astype(float)),
            2.0 * lamE_[nn] / np.sqrt(nn.astype(float)))


# ------------------------------------------- smooth-mass world (B1)
def cell_widths(uu):
    du = np.zeros(len(uu))
    du[1:-1] = 0.5 * (uu[2:] - uu[:-2])
    du[0] = uu[1] - uu[0]
    du[-1] = uu[-1] - uu[-2]
    return du


def smooth_masses(uu):
    """B1 LATTICE-SMOOTH masses m_n = 2 e^{u_n/2} du_n (verbatim)."""
    return 2.0 * np.exp(np.asarray(uu, float) / 2.0) \
        * cell_widths(np.asarray(uu, float))


# ------------------------------------------- congruence machinery
def logdet_sgn(W):
    sgn, ld = np.linalg.slogdet(W)
    return float(sgn), float(ld)


def congruence_pairs(rungs, rrs):
    """Consecutive full-window pairs: the exact congruence (PD
    branch), the general nonsymmetric branch (R1.c / R3), and the
    round-50 crossing flag (both worlds, predecessor verbatim)."""
    rows = []
    n_skip = 0
    n = len(JWIN)
    for k, (ra, rb) in enumerate(zip(rungs[:-1], rungs[1:])):
        if not (ra.get("full") and rb.get("full")):
            n_skip += 1
            continue
        Aa = np.eye(n) - ra["CJ"]
        Ab = np.eye(n) - rb["CJ"]
        DC = ra["CJ"] - rb["CJ"]           # A_{h+1} = A_h + DC
        sga, lda = logdet_sgn(Aa)
        sgb, ldb = logdet_sgn(Ab)
        Q = sga * sgb * math.exp(ldb - lda)
        ka = int(rrs[ra["kz"]]["n_atom"])
        kb = int(rrs[rb["kz"]]["n_atom"])
        blk = np.asarray(core.MU_ALL, float)[min(ka, kb):
                                             max(ka, kb)]
        row = dict(k=k, ha=ra["h"], hb=rb["h"], kza=ra["kz"],
                   kzb=rb["kz"], ka=ka, kb=kb,
                   flow=("ENTER" if kb > ka else
                         "LEAVE" if kb < ka else "NONE"),
                   blkmass=float(np.sum(np.abs(blk))),
                   dnorm=float(np.linalg.norm(DC)), Q=Q)
        # ---- general nonsymmetric branch (always; R1.c / R3)
        Mg = np.linalg.solve(Aa, DC)
        mu, Vg = np.linalg.eig(Mg)
        rho = float(np.max(np.abs(mu))) if len(mu) else 0.0
        real_m = np.abs(mu.imag) <= 1e-9 * (1.0 + np.abs(mu))
        fac_r = 1.0 + mu.real[real_m]
        row.update(
            mu=mu, rho=rho,
            imax=float(np.max(np.abs(mu.imag)
                              / (1.0 + np.abs(mu)))),
            opn=float(np.linalg.norm(Mg, 2)),
            symp=float(np.linalg.eigvalsh(
                0.5 * (Mg + Mg.T))[0]),
            kapV=float(np.linalg.cond(Vg)),
            min_fac=(float(np.min(fac_r)) if len(fac_r)
                     else float("nan")),
            cross=bool(Q < 0.0
                       or (len(fac_r)
                           and float(np.min(fac_r)) < 0.0)))
        # ---- exact congruence branch (A_h PD only)
        ew, Vw = np.linalg.eigh(Aa)
        row["pd"] = bool(ew[0] > 0.0)
        row["tau"] = float(ew[0])
        row["gap"] = float(ew[1] - ew[0])
        row["condA"] = (float(ew[-1] / ew[0]) if ew[0] > 0.0
                        else float("inf"))
        if row["pd"]:
            Wisq = Vw @ np.diag(ew ** -0.5) @ Vw.T
            Wsq = Vw @ np.diag(ew ** 0.5) @ Vw.T
            H = Wisq @ DC @ Wisq
            nH = float(np.linalg.norm(H))
            row["asym"] = (float(np.linalg.norm(H - H.T))
                           / max(nH, 1e-300))
            Hs = 0.5 * (H + H.T)
            lam, U = np.linalg.eigh(Hs)
            recon = Wsq @ (np.eye(n) + Hs) @ Wsq
            row["rec"] = (float(np.linalg.norm(recon - Ab))
                          / max(float(np.linalg.norm(Ab)),
                                1e-300))
            row["recon_min"] = float(np.linalg.eigvalsh(
                0.5 * (recon + recon.T))[0])
            row["lam_min"] = float(lam[0])
            row["eta"] = 1.0 + float(lam[0])
            row["sim"] = (float(np.max(np.abs(
                np.sort(lam) - np.sort(mu.real))))
                / max(1.0, float(np.max(np.abs(lam)))))
            vmin = Wisq @ U[:, 0]
            vmin = vmin / float(np.linalg.norm(vmin))
            row["ovl"] = float(abs(vmin @ Vw[:, 0]))
        rows.append(row)
    return rows, n_skip


def corr_or_nan(x, y):
    x = np.asarray(x, float)
    y = np.asarray(y, float)
    m = np.isfinite(x) & np.isfinite(y)
    if int(np.sum(m)) < 3 or np.std(x[m]) == 0 or np.std(y[m]) == 0:
        return float("nan")
    return float(np.corrcoef(x[m], y[m])[0, 1])


def ols(x, y):
    """OLS y = a + b x; returns (a, b, R^2)."""
    x = np.asarray(x, float)
    y = np.asarray(y, float)
    b = float(np.cov(x, y, bias=True)[0, 1] / np.var(x))
    a = float(np.mean(y) - b * np.mean(x))
    ss = float(np.sum((y - a - b * x) ** 2))
    st = float(np.sum((y - np.mean(y)) ** 2))
    return a, b, (1.0 - ss / st if st > 0 else float("nan"))


def quart(v):
    q = np.percentile(np.asarray(v, float), [25, 50, 75])
    return "q25 %.4f  med %.4f  q75 %.4f" % tuple(q)


def main():
    section("PRIME.PORT.RELCONG.01 -- the exact hermitian "
            "congruence + the margin ladder (EXPLORATION ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s"
          % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
    print("    NO RH claim; no marker moves.")
    print("\nS0 -- firewall")
    check("S0.1 AST firewall clean", not ast_scan(BANNED_IDS))

    # ------------------------------------------------------------ W
    section("W -- build the truth + smooth-mass ladders (all "
            "frame-A zones, h <= %d)" % H_DEEP_MAX)
    rungs, srungs = [], []
    rrs = {}
    n_smooth_dead = 0
    for kz in core.frame_a_zones():
        rr = core.build_window(kz)
        r = rung_win(kz, rr_cache=rr)
        if not isinstance(r, dict):
            continue
        rrs[kz] = rr
        rungs.append(r)
        uu = np.asarray(rr["uu"], float)
        rs = rung_win(kz, comb=(uu, smooth_masses(uu)),
                      rr_cache=rr)
        if isinstance(rs, dict):
            srungs.append(rs)
        else:
            n_smooth_dead += 1
    rungs.sort(key=lambda r: (r["h"], r["kz"]))
    srungs.sort(key=lambda r: (r["h"], r["kz"]))
    print("    truth: %d rungs, h %d .. %d | smooth-mass: %d "
          "rungs, %d chain/window deaths"
          % (len(rungs), rungs[0]["h"], rungs[-1]["h"],
             len(srungs), n_smooth_dead))
    pref_dev = max(float(np.max(np.abs(
        2.0 * np.asarray(rr["lam"], float)
        - np.asarray(core.MU_ALL, float)[:int(rr["n_atom"])])))
        for rr in rrs.values())
    check("W1 >= %d truth rungs built" % MIN_RUNGS,
          len(rungs) >= MIN_RUNGS, "%d rungs" % len(rungs),
          kill="K1")
    check("W1b atom prefix law exact (max |mm - MU_ALL prefix| "
          "%.1e == 0)" % pref_dev, pref_dev == 0.0, kill="K1")

    trows, n_skip_t = congruence_pairs(rungs, rrs)
    srows, n_skip_s = congruence_pairs(srungs, rrs)

    # ------------------------------------------------------------ R1
    section("R1 -- THE EXACT CONGRUENCE  A_{h+1} = A_h^{1/2} "
            "(I + H_h) A_h^{1/2}  (%d truth pairs; %d skips)"
            % (len(trows), n_skip_t))
    print("    H_h = A_h^{-1/2} Delta_h A_h^{-1/2}; wards: "
          "sym %.0e, recon %.0e, similarity %.0e"
          % (ASYM_WARD, RECON_WARD, SIM_WARD))
    check("W2 A_h symmetric PD on every truth full-window rung",
          all(r["pd"] for r in trows), kill="K1")
    check("W3 >= %d truth full-window pairs" % MIN_PAIRS,
          len(trows) >= MIN_PAIRS, "%d" % len(trows), kill="K1")
    asym_max = float(np.max([r["asym"] for r in trows]))
    rec_max = float(np.max([r["rec"] for r in trows]))
    sim_max = float(np.max([r["sim"] for r in trows]))
    imax = float(np.max([r["imax"] for r in trows]))
    check("R1.a SYMMETRIZATION WARD: max ||H - H^T||/||H|| "
          "%.2e <= %.0e" % (asym_max, ASYM_WARD),
          asym_max <= ASYM_WARD, kill="KW")
    check("R1.b RECONSTRUCTION WARD: max rel "
          "||A^{1/2}(I+H)A^{1/2} - A_{h+1}|| %.2e <= %.0e"
          % (rec_max, RECON_WARD), rec_max <= RECON_WARD,
          kill="KW")
    check("R1.c SIMILARITY WARD: eig(H) == eig(W^{-1}Delta), "
          "max dev %.2e <= %.0e; max rel |Im mu| %.2e <= %.0e"
          % (sim_max, SIM_WARD, imax, SIM_WARD),
          sim_max <= SIM_WARD and imax <= SIM_WARD, kill="KW")
    etas = np.array([r["eta"] for r in trows])
    n_cross_t = sum(1 for r in trows if r["cross"])
    min_eta = float(np.min(etas))
    max_neg = float(np.max([-r["lam_min"] for r in trows]))
    check("R1.d REPRODUCTION (round-50 ledger): %d pairs == %d, "
          "%d crossings == %d, min eta %.4f == %.4f, "
          "max(-lam_min) %.4f == %.4f (tol %.1e)"
          % (len(trows), REF_N_TRUTH_PAIRS, n_cross_t,
             REF_TRUTH_CROSS, min_eta, REF_TRUTH_MINETA,
             max_neg, REF_TRUTH_MAXNEG, ROUND_TOL),
          len(trows) == REF_N_TRUTH_PAIRS
          and n_cross_t == REF_TRUTH_CROSS
          and abs(min_eta - REF_TRUTH_MINETA) <= ROUND_TOL
          and abs(max_neg - REF_TRUTH_MAXNEG) <= ROUND_TOL,
          kill="KW")
    print("\n    THE EXACT FORM ESTABLISHED: on every truth step "
          "H_h is hermitian (real symmetric), the")
    print("    congruence identity reconstructs A_{h+1} to %.1e, "
          "and round 50's mu-ledger IS the" % rec_max)
    print("    hermitian spectrum eig(H_h) seen through the "
          "similarity W^{-1}Delta = A^{-1/2} H A^{1/2}.")

    # ------------------------------------------------------------ R2
    section("R2 -- THE MARGIN LADDER  eta_h = 1 + "
            "lambda_min(H_h)")
    print("    step        flow    lam_min    eta       tau_h"
          "      gap_h      ||D||_F   blkmass   ovl(soft)")
    for r in trows:
        print("    h %3d->%3d %-5s  %+.4f   %.4f   %.3e  %.3e"
              "  %.5f   %8.3f  %.3f"
              % (r["ha"], r["hb"], r["flow"], r["lam_min"],
                 r["eta"], r["tau"], r["gap"], r["dnorm"],
                 r["blkmass"], r["ovl"]))
    print("\n    eta ladder: %s | min %.4f (h %d->%d)"
          % (quart(etas), min_eta,
             trows[int(np.argmin(etas))]["ha"],
             trows[int(np.argmin(etas))]["hb"]))

    # trend fit, leave-last-third-out
    hs = np.array([r["ha"] for r in trows], float)
    order = np.argsort(hs)
    hs_o = hs[order]
    ly_o = np.log(etas[order])
    n_all = len(hs_o)
    n_fit = int(math.ceil(2.0 * n_all / HOLDOUT_FRAC))
    cands = (("POWER log eta ~ a + b log h", np.log(hs_o)),
             ("LOG   log eta ~ a + b log log h",
              np.log(np.log(hs_o))),
             ("EXP   log eta ~ a + b h", hs_o))
    print("\n    TREND (fit first %d steps by h, score RMSE on "
          "the held-out last %d):" % (n_fit, n_all - n_fit))
    best = None
    for name, x in cands:
        a, b, r2 = ols(x[:n_fit], ly_o[:n_fit])
        rmse = float(np.sqrt(np.mean(
            (ly_o[n_fit:] - a - b * x[n_fit:]) ** 2)))
        print("      %-33s b %+8.4f  R^2(in) %6.3f  "
              "RMSE(out) %.4f" % (name, b, r2, rmse))
        if best is None or rmse < best[1]:
            best = (name.split()[0], rmse, b)
    _, b_tau, _ = ols(np.log(hs_o),
                      np.log([trows[i]["tau"] for i in order]))
    _, b_gap, _ = ols(np.log(hs_o),
                      np.log([trows[i]["gap"] for i in order]))
    _, b_dn, _ = ols(np.log(hs_o),
                     np.log([trows[i]["dnorm"] for i in order]))
    _, b_eta, _ = ols(np.log(hs_o), ly_o)
    print("    best held-out candidate: %s (RMSE %.4f)"
          % (best[0], best[1]))
    print("    SHRINK COMPARISON (full-ladder power slopes vs "
          "h): eta %+0.3f | tau %+0.3f | gap %+0.3f | "
          "||D||_F %+0.3f" % (b_eta, b_tau, b_gap, b_dn))

    print("\n    THE SOURCE QUESTION: corr(log eta, z) and "
          "R^2 = corr^2 (bar %.2f):" % R2_BAR)
    leta = np.log(etas)
    sources = (
        ("log blkmass (moving-block atom mass)",
         np.log(np.maximum([r["blkmass"] for r in trows],
                           1e-300))),
        ("log ||Delta||_F (window increment)",
         np.log([r["dnorm"] for r in trows])),
        ("log tau_h (min eig A_h)",
         np.log([r["tau"] for r in trows])),
        ("log gap_h (eig2 - eig1 of A_h)",
         np.log([r["gap"] for r in trows])),
        ("ovl (soft-mode overlap, raw)",
         np.array([r["ovl"] for r in trows])))
    best_r2, best_src = -1.0, "none"
    for name, z in sources:
        c = corr_or_nan(leta, z)
        r2 = c * c if np.isfinite(c) else float("nan")
        print("      %-38s corr %+7.3f  R^2 %6.3f"
              % (name, c if np.isfinite(c) else float("nan"),
                 r2 if np.isfinite(r2) else float("nan")))
        if np.isfinite(r2) and r2 > best_r2:
            best_r2, best_src = r2, name
    margin_lab = ("MARGIN-LAWFUL" if best_r2 >= R2_BAR
                  else "MARGIN-UNEXPLAINED")
    print("    best single source: %s (R^2 %.3f)"
          % (best_src, best_r2))
    check("R2.1 typed: %s (best R^2 %.3f vs bar %.2f)"
          % (margin_lab, best_r2, R2_BAR), True)

    # ------------------------------------------------------------ R3
    section("R3 -- NON-NORMALITY DIAGNOSTICS for "
            "M = W^{-1} Delta C (general solver)")
    print("    step        rho      ||M||_2   ||M||/rho  "
          "lam_min(sym part)  kappa(V)   sqrt(cond A)  eta")
    nn_flags = []
    kap_bound_ok = True
    for r in trows:
        ratio = r["opn"] / max(r["rho"], 1e-300)
        nn_flags.append(ratio >= NN_RATIO_BAR)
        kb = math.sqrt(r["condA"])
        kap_bound_ok &= (r["kapV"] <= kb * (1.0 + 1e-6))
        print("    h %3d->%3d %7.4f  %8.4f  %8.2f   %+12.4f"
              "       %8.2f   %8.2f     %.4f"
              % (r["ha"], r["hb"], r["rho"], r["opn"], ratio,
                 r["symp"], r["kapV"], kb, r["eta"]))
    n_nn = sum(nn_flags)
    ratios = [r["opn"] / max(r["rho"], 1e-300) for r in trows]
    symp_min = float(np.min([r["symp"] for r in trows]))
    kap_med = float(np.median([r["kapV"] for r in trows]))
    rho_lab = ("RHO-MISLEADING"
               if n_nn >= NN_STEP_FRAC * len(trows)
               else "RHO-FAITHFUL")
    print("\n    CENSUS: ||M||_2/rho >= %.1f on %d/%d steps "
          "(ratio ladder: %s);" % (NN_RATIO_BAR, n_nn,
                                   len(trows), quart(ratios)))
    print("    median kappa(V) %.1f (transport bound kappa <= "
          "sqrt(cond A) holds on all steps: %s;"
          % (kap_med, kap_bound_ok))
    print("    unit-column eig basis -- the bound is for the "
          "optimally scaled diagonalizer, so excess")
    print("    is column-scaling ambiguity, SPEC v2 (i); "
          "report-only);")
    print("    lambda_min of the symmetric part reaches %+0.3f "
          "(can pass -1 with NO crossing -- the" % symp_min)
    print("    non-normal signature: symmetric-part bounds are "
          "NOT the inheritance criterion).")
    print("    STATED: the operator IS non-normal (kappa(V) >> 1"
          ", ||M||_2 > rho), so rho and any norm")
    print("    reasoning on W^{-1}Delta were the wrong "
          "instruments for margins; the SPECTRUM round 50")
    print("    reported was nevertheless exact (R1.c), and the "
          "honest carrier of the inheritance is the")
    print("    hermitian H_h, where lambda_min IS the margin.")
    check("R3.1 typed: %s (%d/%d steps with ||M||/rho >= %.1f)"
          % (rho_lab, n_nn, len(trows), NN_RATIO_BAR), True)

    # ------------------------------------------------------------ R4
    section("R4 -- THE SMOOTH WORLD (%d pairs; %d skips): where "
            "does lambda_min(H) cross -1?"
            % (len(srows), n_skip_s))
    print("    step        A_h PD  lam_min(H)  eta        "
          "cross  Q")
    first_eta_neg = None
    n_cone = 0
    for r in srows:
        if r["pd"]:
            if r["eta"] < 0.0 and first_eta_neg is None:
                first_eta_neg = r
            print("    h %3d->%3d  yes    %+9.4f  %+9.4f   "
                  "%-5s  %+.3e%s"
                  % (r["ha"], r["hb"], r["lam_min"], r["eta"],
                     str(r["cross"]), r["Q"],
                     "  <-- CROSSING" if r["cross"] else ""))
        else:
            n_cone += 1
            print("    h %3d->%3d  NO     CONE-EXITED (real "
                  "congruence unavailable)   %-5s  %+.3e%s"
                  % (r["ha"], r["hb"], str(r["cross"]), r["Q"],
                     "  <-- CROSSING" if r["cross"] else ""))
    n_cross_s = sum(1 for r in srows if r["cross"])
    n_qneg = sum(1 for r in srows if r["Q"] < 0.0)
    first_s = next((r for r in srows if r["cross"]), None)
    first_hh = ((first_s["ha"], first_s["hb"])
                if first_s is not None else (-1, -1))
    check("R4.1 REPRODUCTION (round-50 smooth ledger): %d pairs "
          "== %d, %d crossings == %d, first at h %d->%d == "
          "%d->%d, Q < 0 on %d == %d"
          % (len(srows), REF_N_SMOOTH_PAIRS, n_cross_s,
             REF_SMOOTH_CROSS, first_hh[0], first_hh[1],
             REF_SMOOTH_FIRST[0], REF_SMOOTH_FIRST[1], n_qneg,
             REF_SMOOTH_QNEG),
          len(srows) == REF_N_SMOOTH_PAIRS
          and n_cross_s == REF_SMOOTH_CROSS
          and first_hh == REF_SMOOTH_FIRST
          and n_qneg == REF_SMOOTH_QNEG, kill="KW")
    s_pd = [r for r in srows if r["pd"]]
    s_eta_neg = [r for r in s_pd if r["eta"] < 0.0]
    s_min_eta = (float(np.min([r["eta"] for r in s_pd]))
                 if s_pd else float("nan"))
    if first_eta_neg is not None:
        print("\n    FIRST lambda_min(H) < -1 (PD branch): "
              "h %d->%d (eta %+0.4f)"
              % (first_eta_neg["ha"], first_eta_neg["hb"],
                 first_eta_neg["eta"]))
    print("    CONTRAST: truth min eta = %+0.4f (all %d steps "
          "> 0) vs smooth min eta = %s on %d PD"
          % (min_eta, len(trows),
             ("%+0.4f" % s_min_eta) if s_pd else
             "none (empty PD branch, SPEC v2 (ii))",
             len(s_pd)))
    print("    steps (eta < 0 on %d of them) + %d CONE-EXITED "
          "steps (A_h itself indefinite -- the smooth"
          % (len(s_eta_neg), n_cone))
    print("    world does not even keep the congruence's PD "
          "premise).  The discriminating gap is the")
    print("    margin sign: truth stays a strictly positive "
          "eta ladder; smooth crosses and exits.")
    smooth_lab = ("SMOOTH-DISCRIMINATES"
                  if (min_eta > 0.0
                      and (len(s_eta_neg) > 0 or n_cone > 0))
                  else "SMOOTH-NONDISCRIMINATING")
    check("R4.2 typed: %s (smooth eta < 0 on %d PD steps, "
          "CONE-EXITED on %d)"
          % (smooth_lab, len(s_eta_neg), n_cone), True)

    # ------------------------------------------------------------ R5
    section("R5 -- THE HERMITIAN INHERITANCE MINI-THEOREM, "
            "numerically")
    rec_pd_ok = all(r["recon_min"] > 0.0 for r in trows)
    eta_pos_ok = all(r["eta"] > 0.0 for r in trows)
    rec_min_min = float(np.min([r["recon_min"] for r in trows]))
    check("R5.1 one-step Sylvester inheritance verified: eta_h "
          "> 0 on all %d steps AND reconstructed A_{h+1} PD "
          "(min eig %+0.3e > 0) on all steps"
          % (len(trows), rec_min_min),
          rec_pd_ok and eta_pos_ok)
    print("\n    THE MINI-THEOREM (exact): A_h PD, Delta_h "
          "symmetric, A_{h+1} = A_h + Delta_h,")
    print("    H_h = A_h^{-1/2} Delta_h A_h^{-1/2}  ==>  "
          "A_{h+1} = A_h^{1/2}(I + H_h)A_h^{1/2}, and by")
    print("    Sylvester congruence  A_{h+1} PD  <=>  "
          "lambda_min(H_h) > -1  <=>  eta_h > 0.")
    print("    THE FULL LADDER INDUCTION reduces to:")
    print("      (i)  ONE certified base rung A_{h0} PD "
          "(exists: v884 certified head positivity /")
    print("           v887 certified ladder -- cited, not "
          "re-run);")
    print("      (ii) THE MARGIN INEQUALITY: eta_h = 1 + "
          "lambda_min(H_h) > 0 for every step h.")
    print("    FINITE SHADOW (measured, this run): eta_h > 0 on "
          "%d/%d deployed steps; min eta = %.4f"
          % (int(np.sum(etas > 0.0)), len(trows), min_eta))
    print("    at h %d->%d; margin trend and sources in R2 "
          "(typed %s).  NO claim beyond the ladder."
          % (trows[int(np.argmin(etas))]["ha"],
             trows[int(np.argmin(etas))]["hb"], margin_lab))

    # ------------------------------------------------------------ C
    section("C -- controls")
    print("  C1 -- Epstein/scramble (kz %d, frame must die):"
          % CTRL_KZ)
    ok1 = True
    for nmc, kw in (("Epstein", dict(comb=eps_comb(CTRL_KZ))),
                    ("scramble", dict(scramble_seed=1))):
        try:
            rc = rung_win(CTRL_KZ, **kw)
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
    print("  C2 -- smooth-mass world: PRIMARY embedded control; "
          "crossings ward-anchored in R4.1 (%d crossing steps)."
          % n_cross_s)
    check("C2 smooth detector fired (%d crossings)" % n_cross_s,
          n_cross_s > 0, kill="K3")

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
        VERDICT = ("RELCONG-MEASURED / %s / %s / %s"
                   % (margin_lab, rho_lab, smooth_lab))
        print("\n  VERDICT: %s" % VERDICT)
        print("  (min eta %.4f on %d truth steps; best source "
              "R^2 %.3f (%s); ||M||/rho >= %.1f on %d/%d;"
              % (min_eta, len(trows), best_r2, best_src,
                 NN_RATIO_BAR, n_nn, len(trows)))
        print("   smooth: eta < 0 on %d PD steps + %d "
              "CONE-EXITED, first crossing h %d->%d)"
              % (len(s_eta_neg), n_cone, first_hh[0],
                 first_hh[1]))
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed"
          % (time.time() - T0, n_tot, n_tot - n_pass))
    return 0 if n_pass == n_tot else 1


if __name__ == "__main__":
    raise SystemExit(main())
