#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""transport_discriminator_probe -- PRIME.PORT.TRANSPORT.01
(EXPLORATION ONLY, experiments/; round 54, named object (b) from
CXI: the TRANSPORT factor is where truth and the smooth world
separate -- formulate exactly what "staying PD" costs the
transport, and measure the discriminating law.  2026-08-09.)

THE QUESTION (frozen): ratio_euler_projection_probe (round 53)
factorized the per-step wall-energy ratio EXACTLY as
|r_h| = C_h x M_h x T_h across the exact linear (lag) level, with
    C_h = |delta_v| / S_abs            (cancellation),
    M_h = S_abs / sigma_v              (relative density increment),
    T_h = (|d_h|/a_h) / (|delta_v|/sigma_v)
                                       (operator-level / lag-level
                                        transport in the dangerous
                                        direction).
On truth the medians are C 0.20 / M 2.05 / T 1.19 and |r| < 1 on
all steps; the smooth world is SMOOTH-SIMILAR in C (med 0.12) and
in the density factors, yet its |r| EXPLODES (med ~ 4e2) -- the
explosion lives in the TRANSPORT, through the indefinite operator
level.  This probe dissects T and asks for the law that keeps it
O(1) on truth: does staying PD (margin eta) BOUND the transport,
and is the closed loop  eta_{h+1} >= 1 - C M T(eta_h)
self-consistent as a dynamical system?

THE TRANSPORT ANATOMY (exact, frozen): from the round-53
definitions, with r_abs = |d_h| / |a_h| (a_h > 0 on truth; the
smooth general branch takes |a_h|),
    T_h  =  F_h x R_h   EXACTLY, where
    F_h  =  |d_h| / |delta_v|   (FRAME DISTORTION: the increment
                                 as seen by the compressed operator
                                 vs by the raw alias density, same
                                 direction v),
    R_h  =  sigma_v / |a_h|     (RESOLVENT AMPLIFICATION: the
                                 existing lag-level mass vs the
                                 operator quadratic form -- blows
                                 up exactly when v approaches the
                                 soft/indefinite directions of A).
Report-only diagnostics per step: the A^{-1/2}-weighting
amplification amp(x) = ||A^{-1/2} x|| / sqrt(tr(A^{-1})/12) for
x = v_min and for x = w_top (the maximal-increment direction of
Delta_h), and the ANGLE TRANSPORT rot = angle(v, A^{1/2}v/||.||)
-- how far the whitening rotates the dangerous direction between
the lag frame and the operator frame.  On the smooth world A_s is
indefinite on EVERY pair (round-51 SPEC v2(ii)), so the
diagnostics use the matrix absolute value |A| = V |w| V^T
(pseudo-whitening; documented, report-only); F and R stay exact
with |a_h|.

THE LADDER (frozen, round-51/52/53 verbatim): all frame-A zones
(core.frame_a_zones()) with h <= 900, sorted by (h, kz);
consecutive FULL-WINDOW pairs (both rungs carry all 12 indices of
J = {2, 4, ..., 24}; typed skips counted); truth + smooth-mass
world (B1 LATTICE-SMOOTH masses m_n = 2 e^{u_n/2} du_n, midpoint
cells, lattice_parametrix verbatim); Epstein/scramble frame
status (C).  COORDINATE FREEZES verbatim from round 53 (JWIN
order warded; v_min = A^{-1/2}-transported Euclidean-normalized
minimizer of H_h; HOST geometry; sigma = -+1 ENTER/LEAVE; per-atom
alias tests q_n(j); sigma_v uses |d_a| magnitudes).

FROZEN PROTOCOL (2026-08-09; all bars frozen before the run):

 W   PIPELINE WARDS (kill -> PIPELINE-BROKEN): W1 >= 30 truth
     rungs; W1b the atom prefix law exact; W2 jav == JWIN in order
     on every truth full-window rung; W3 >= 20 truth full-window
     pairs, all bases PD.  W5 LINEARITY WARD (kill -> WARD-BROKEN):
     on every truth AND smooth rung, max_j |[d(theta_j) -
     d_arch(theta_j)] - sum_n q_n(j)| / max(1, |d(theta_j)|)
     <= 1e-9 over the 12 aliases.  X1-NIL WARD (kill ->
     WARD-BROKEN): on every LEAVING step the block atoms' tent
     rows at the arrival geometry are identically zero (bitwise).

 R0  THE EXACT CONGRUENCE + ROUND-52/53 ANCHORS (kill ->
     WARD-BROKEN): per truth pair (a) SYMMETRIZATION
     ||H - H^T||/||H|| <= 1e-12, (b) RECONSTRUCTION rel <= 1e-10,
     (c) RAYLEIGH IDENTITY |vDv/vAv - lambda_min| / max(1,
     |lambda_min|) <= 1e-9, (d) LEDGER: 31 pairs, min eta 0.0050,
     max(-lam) 0.9950 (tol 5.001e-5), med eta 0.29 (tol 5.001e-3),
     (e) SLOPES: eta +0.108 (tol 5.001e-4), tau -2.74 (tol
     5.001e-3), b_d -3.716, b_a -3.456 (tol 5.001e-4 each).
     All T tables run on the lambda_min < 0 steps (census
     printed).  (f) ROUND-53 FACTOR ANCHOR: the truth ladder
     medians of the exact factorization reproduce C 0.20 /
     M 2.05 / T 1.19 (tol 5.001e-3 each; round-53 printed
     medians at their citation rounding), with the FACT ward
     |C M T - |r|| <= 1e-10 max(1, |r|) per step.

 T1  THE TRANSPORT ANATOMY: per neg truth step the exact
     sub-factorization T = F x R (definitions above).  TFACT WARD
     (kill -> WARD-BROKEN): |F R - T| <= 1e-10 max(1, T) per step
     (both worlds).  Printed per step (truth, then smooth):
     |r|, T, F, R, amp(v), amp(w_top), rot(deg); the sub-factor
     LADDERS (quartiles) truth vs smooth and the median
     truth-vs-smooth contrast per sub-factor -- WHERE does the
     explosion live (report; the typed discrimination is T2/T3).

 T2  THE DISCRIMINATING LAW (the deliverable): candidate
     T <= f(eta_prev), eta_prev = the margin of the immediately
     preceding full-window truth pair in ladder order (the
     self-consistency loop: PD with margin eta => transport
     bounded => next margin bounded => ...).  On the neg
     factorized truth steps with a predecessor (first pair
     excluded, counted): (i) THREE FITS T = a + b x for
     x in { 1/eta_prev, 1/sqrt(eta_prev), log(1/eta_prev) },
     train = first ceil(2n/3) in ladder order, score RMSE on the
     held-out last third; print which holds (smallest held-out
     RMSE); corr(log T, log(1/eta_prev)) printed.  (ii) THE
     ENVELOPE: p = max(0, OLS slope of log T on log(1/eta_prev),
     train only) (a negative exponent means a CONSTANT bound;
     clamped, documented), c = max_train T eta_prev^p; the bound
     T <= c / eta_prev^p must hold on the held-out third within
     slack factor 2.0 (max test excess printed).  (iii) THE
     SELF-CONSISTENT INDUCTION CANDIDATE: with K = medC x medM x
     c (this run's truth medians; a MODEL of the loop, median
     coupling + envelope transport), the map
         g(eta) = 1 - K eta^{-p}
     is analyzed exactly: fixed points on (0, 1] (log-grid scan +
     bisection), stability |g'(eta*)| = p K eta*^{-p-1} < 1,
     basin of the upper fixed point = (eta_unstable, 1] (g is
     increasing; below the lower root the margin dies), and the
     CENSUS: which of the 31 measured ladder etas sit in the
     basin.  Report-only K variants (q75 coupling; median-c)
     printed alongside.  TYPED (frozen mapping):
       SELFCONSISTENT(c, p, eta*) iff the envelope holds on the
         held-out third (excess <= 2.0) AND a positive attracting
         fixed point exists AND >= 1/2 of the ladder etas lie in
         its basin;
       TRANSPORT-UNBOUNDED iff the envelope FAILS on the held-out
         third (no measured eta-law of the fitted form bounds T);
       TRANSPORT-LAWLESS otherwise (a bound exists but the closed
         loop has no positive attracting fixed point capturing
         the ladder).
     Fewer than 8 usable law steps also types TRANSPORT-LAWLESS
     (honest small-n guard, printed).

 T3  THE SMOOTH DIVERGENCE POINT: T_env = max truth T (neg
     factorized steps).  Along the smooth pair ladder (in ladder
     order), print per step T_s, a_s sign, and the two flags
     T_s > T_env (transport outside the truth envelope) and
     a_s < 0 (the cone exit at the PAIR level in the dangerous
     direction; the BASE A_s is already indefinite on every
     smooth pair -- round-51 SPEC v2(ii) -- so the pair-level
     sign event is carried by a_s).  Print the two first indices
     per ladder (first T-explosion, first a_s < 0) and the lead
     (is the transport explosion an EARLY WARNING of the
     crossing); report-only.

 C   CONTROLS: (C1, kz 9, must fire, kill -> WARD-BROKEN)
     Epstein (lambda_eps recursion comb) + scramble (seed 1): the
     compressed frame must die (exterior supercritical OR
     lam(C_J) > 1 OR window unavailable); channel reported.
     (C2, kill -> WARD-BROKEN) smooth-world reproduction: 28
     full-window pairs, 0 PD bases (round-51/52/53 ledger);
     smooth is the PRIMARY control.

KILLS: K1 a W pipeline ward breaks -> PIPELINE-BROKEN; KW the
W5 / X1-nil / R0 / TFACT / FACT / smooth-reproduction / control
ward breaks -> WARD-BROKEN.  The T2 law label and every T1/T3
census are TYPED / report-only, never kills.

VERDICT (frozen enum): TRANSPORT-MEASURED / <SELFCONSISTENT(c,
p, eta*) | TRANSPORT-UNBOUNDED | TRANSPORT-LAWLESS>; else
PIPELINE-BROKEN / WARD-BROKEN.

FROZEN BARS: H_DEEP_MAX = 900; JWIN = (2, ..., 24); MIN_RUNGS 30;
MIN_PAIRS 20; ASYM_WARD 1e-12; RECON_WARD 1e-10; RAY_WARD 1e-9;
LIN_WARD 1e-9; FACT_WARD 1e-10; TFACT_WARD 1e-10; ENV_SLACK 2.0;
BASIN_FRAC 0.5; MIN_LAW 8; HOLDOUT thirds (train ceil(2n/3));
CTRL_KZ 9; scramble seed 1; reproduction refs (round-52/53
printed ledgers / contract citations): 31 truth pairs / min eta
0.0050 / max(-lam) 0.9950 / med eta 0.29 / slope eta +0.108 /
slope tau -2.74 / slope d -3.716 / slope a -3.456 / truth factor
medians C 0.20, M 2.05, T 1.19 / 28 smooth pairs with 0 PD bases;
tolerances TOL4 5.001e-5, TOL3 5.001e-4, TOL2 5.001e-3 (each ref
warded at its citation's print-rounding radius).

SPEC v1 (2026-08-09, frozen + SHA-hashed before the first run);
mechanical concretizations frozen with it: (i) build_window
results are cached per kz and shared truth/smooth; the tent-row
alias matrices G are MASS-FREE and shared truth/smooth per kz
(round-53 SPEC v1(i) verbatim); (ii) eta_prev is the eta of the
immediately preceding full-window truth pair in the pairs list
(ladder order; typed skips break adjacency and are simply
bridged by list order, as frozen); the first pair has no
predecessor and is excluded (counted); (iii) the smooth
pseudo-whitening for the report diagnostics uses |A| =
V diag(|w|) V^T; F and R use |a_h| (exact); (iv) p < 0 fits are
clamped to p = 0 (constant envelope; the loop map is then
constant with fixed point 1 - K, stable, full basin iff K < 1);
(v) fixed-point roots: phi(e) = e - 1 + K e^{-p} scanned on the
log grid e in [1e-8, 1] (20001 points) + 200-step bisection per
sign change; two roots = (unstable lower, upper) with stability
from |g'|; zero roots = no fixed point; (vi) medians of C, M
(the loop coupling) are taken over the neg factorized truth
steps (the round-53 population), the basin census over ALL truth
pair etas; (vii) smooth factor medians are REPORT-ONLY (round 53
printed the smooth C median 0.12 under SPEC v2(b); the smooth M
and T medians were reported downstream, so they are printed here
for the contrast but not warded).

SPEC v2 (2026-08-09, after run 1; fail-first preserved -- run 1
passed ALL 20 checks under SPEC v1 (SHA db8d5c11...) with verdict
TRANSPORT-MEASURED / TRANSPORT-LAWLESS; no bar, reference or
typed label is touched; two REPORT-ONLY print fixes are
documented here): (a) the verdict parenthetical printed the
truth F median with %.4f, which renders the measured
medF ~ 2.4e-6 as "0.0000"; the F and R medians are now printed
in scientific notation (pure formatting; the underlying numbers
of run 1 stand).  (b) the smooth-|r| report line cited "~4e2"
from the round-53 report; run 1 measured the smooth |r| MEDIAN
at 4.184 and the 4e2 figure is the single worst step
(h 488->490, |r| = 4.024e2, reproduced bitwise in the per-step
table); the print now shows median AND max with the step id so
the citation is pinned to its object.  Run-1 headline numbers
(unchanged by v2): truth med F 2.40e-6 / med R 6.17e+5; smooth
excess F 10^+2.03, R 10^-1.52 -> explosion in FRAME;
corr(log T, log(1/eta_prev)) = -0.011; envelope p 0.1523,
c 8.1684, held-out excess 1.922 (holds); PRIMARY loop K 3.408
has NO positive fixed point -> TRANSPORT-LAWLESS (median-c
variant K 0.434: stable eta* 0.521, 31/31 etas in basin --
printed as the report-only contrast); smooth first T-explosion
idx 1 vs first a_s < 0 idx 0 (transport TRAILS by 1).

NO RH claim: transport factors, envelope constants and
fixed-point structure on finite-h window truncations are
measurements on the deployed v563 ladder, not theorems about
zeros.  No marker moves.

FIREWALL: no zeros, no prime oracles (AST scan; banned ids
zetazero / nzeros / primerange / isprime / primepi / nextprime /
prevprime); NO sieve is needed (all atoms are read from the
deployed U_ALL / MU_ALL prefix tables); v563 READ-ONLY; RNG only
inside the declared scramble control; stdout only.

Sources (read-only): v563_paper2_readouts (build_window,
atom_lags_at, arch_lags, U_ALL / MU_ALL prefix law -- verbatim);
pipeline + factorization verbatim from
ratio_euler_projection_probe.py (PRIME.PORT.RATIOSOURCE.01,
round 53, the T definition and the C/M/T anchors); congruence +
margin machinery from relative_congruence_probe.py
(PRIME.PORT.RELCONG.01, round 51: H_h, eta_h, the smooth
CONE-EXITED bookkeeping) via eta_margin_source_probe.py
(PRIME.PORT.ETASOURCE.01, round 52, the anchor ledger); certified
base rungs v884/v887 (cited, not re-run).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/transport_discriminator_probe.py
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
NJ = len(JWIN)
MIN_RUNGS = 30
MIN_PAIRS = 20
MIN_COMMON_J = 8
ASYM_WARD = 1e-12
RECON_WARD = 1e-10
RAY_WARD = 1e-9
LIN_WARD = 1e-9
FACT_WARD = 1e-10
TFACT_WARD = 1e-10
ENV_SLACK = 2.0
BASIN_FRAC = 0.5
MIN_LAW = 8
CTRL_KZ = 9
BANNED_IDS = ("zetazero", "nzeros", "primerange", "isprime",
              "primepi", "nextprime", "prevprime")

# reproduction refs (round-52/53 printed ledgers / citations)
REF_N_TRUTH_PAIRS = 31
REF_TRUTH_MINETA = 0.0050
REF_TRUTH_MAXNEG = 0.9950
REF_TRUTH_MEDETA = 0.29
REF_SLOPE_ETA = +0.108
REF_SLOPE_TAU = -2.74
REF_SLOPE_D = -3.716
REF_SLOPE_A = -3.456
REF_MED_C = 0.20
REF_MED_M = 2.05
REF_MED_T = 1.19
REF_N_SMOOTH_PAIRS = 28
REF_SMOOTH_PD = 0
TOL4 = 5.001e-5
TOL3 = 5.001e-4
TOL2 = 5.001e-3

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


# --------- pipeline, verbatim from ratio_euler_projection_probe
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


def rung_rec(kz, scramble_seed=None, comb=None, rr_cache=None):
    """One rung: build (verbatim path), window compression, and the
    alias-density bookkeeping (dJ, darchJ) for the exact linear
    level."""
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
    darch = grid_density(c_ar)
    L = 2 * M - 2
    if h > H_DEEP_MAX:
        return "TOO-DEEP"
    xs, ws, _ = folded_measure(d, L, +1.0)
    ys, vs, uf_n = folded_measure(d, L, -1.0)
    al, be, m0, steps = lanczos_chain(xs, ws, h + 1)
    if steps < h + 1 or np.any(be <= 0):
        return None
    Pn = eval_chain(al, be, m0, ys, h)
    E = np.sqrt(vs)[:, None] * (Pn @ Pn.T) * np.sqrt(vs)[None, :]
    E = 0.5 * (E + E.T)
    out = dict(kz=kz, h=h, alpha=alpha, M=M, D=D, L=L,
               n_atom=len(uu), uu=uu, mm=mm,
               dJ=d[list(JWIN)].copy(),
               darchJ=darch[list(JWIN)].copy(),
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


def eps_comb(rr):
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


# ------------------------------------- the exact linear atom level
def tent_alias_G(uu, alpha, M):
    """Mass-free tent-row alias tests: G[n, j] = cosine transform of
    atom n's UNIT tent lag row at alias node theta_j (round-53
    verbatim; warded in W5)."""
    uu = np.asarray(uu, float)
    D = 2.0 * alpha / M
    L = 2 * M - 2
    th = 2.0 * math.pi * np.array(JWIN, float) / L
    G = np.zeros((len(uu), NJ))
    i0 = np.floor(uu / D).astype(int)
    for off in range(-2, 3):
        ii = i0 + off
        w = 1.0 - np.abs(ii * D - uu) / D
        m = (ii >= 0) & (ii < M) & (w > 0.0)
        if not np.any(m):
            continue
        iv = ii[m]
        cosmat = np.cos(np.outer(iv.astype(float), th))
        fac = 2.0 * cosmat
        fac[iv == 0, :] = 1.0
        sel = iv == M - 1
        fac[sel, :] = cosmat[sel, :]
        G[m, :] += w[m][:, None] * fac
    for n in np.nonzero(uu < D)[0]:      # deployed reflection branch
        u_j = float(uu[n])
        for i in range(0, min(M, int(math.floor((D - u_j) / D)) + 2)):
            v = 1.0 - (i * D + u_j) / D
            if v > 0.0:
                gfac = (1.0 if i == 0 else
                        np.cos((M - 1) * th) if i == M - 1
                        else 2.0 * np.cos(i * th))
                G[n, :] += v * gfac
    return G


def lin_dev(rec, G):
    """W5: rel deviation of the own per-atom reassembly of the alias
    density (exact linearity of the lag map)."""
    rhs = -0.5 * (rec["mm"] @ G)
    lhs = rec["dJ"] - rec["darchJ"]
    return float(np.max(np.abs(lhs - rhs)
                        / np.maximum(1.0, np.abs(rec["dJ"]))))


def step_projection(ra, rb, v, Ga, Gb):
    """The exact linear-level split for one step in direction v
    (round-53 verbatim; delta_v, sigma_v, GEO/ATOM, S_abs)."""
    v2 = np.asarray(v, float) ** 2
    ka, kb = ra["n_atom"], rb["n_atom"]
    klo, khi = min(ka, kb), max(ka, kb)
    flow = "ENTER" if kb > ka else "LEAVE" if kb < ka else "NONE"
    host = rb if kb > ka else ra
    Gh = Gb if kb > ka else Ga
    sigma = -1.0 if kb > ka else 1.0
    dv = float(np.sum(v2 * (ra["dJ"] - rb["dJ"])))
    out = dict(flow=flow, nblk=khi - klo, dv=dv,
               sig_v=float(np.sum(v2 * np.abs(ra["dJ"]))))
    if khi > klo:
        mmb = host["mm"][klo:khi]
        cvec = sigma * (-0.5) * mmb * (Gh[klo:khi] @ v2)
        out["atom"] = float(np.sum(cvec))
        out["cabs"] = float(np.sum(np.abs(cvec)))
    else:
        out["atom"] = 0.0
        out["cabs"] = 0.0
    out["geo"] = dv - out["atom"]
    out["sabs"] = out["cabs"] + abs(out["geo"])
    return out


def factorize(row):
    """Round-53 X4 verbatim: |r| = C x M x T exactly, plus the exact
    sub-factorization T = F x R (frame distortion x resolvent
    amplification)."""
    r_abs = abs(row["d_h"]) / abs(row["a_h"])
    if abs(row["dv"]) <= 0.0 or row["sabs"] <= 0.0 \
            or row["sig_v"] <= 0.0:
        return None
    C = abs(row["dv"]) / row["sabs"]
    Mf = row["sabs"] / row["sig_v"]
    T = r_abs / (abs(row["dv"]) / row["sig_v"])
    F = abs(row["d_h"]) / abs(row["dv"])
    R = row["sig_v"] / abs(row["a_h"])
    return dict(r_abs=r_abs, C=C, M=Mf, T=T, F=F, R=R,
                dev=abs(C * Mf * T - r_abs) / max(1.0, r_abs),
                tdev=abs(F * R - T) / max(1.0, T))


def frame_diags(Aa, DC, v, pseudo_abs=False):
    """Report-only transport diagnostics: the A^{-1/2}-weighting
    amplification along v and along w_top (vs the isotropic
    reference sqrt(tr A^{-1}/n)), and the angle transport between
    the lag frame and the operator frame.  pseudo_abs: use |A|
    (smooth world, SPEC v1(iii))."""
    n = Aa.shape[0]
    ew, Vw = np.linalg.eigh(Aa)
    w_use = np.abs(ew) if pseudo_abs else ew
    Wisq = Vw @ np.diag(w_use ** -0.5) @ Vw.T
    Wsq = Vw @ np.diag(w_use ** 0.5) @ Vw.T
    ref = math.sqrt(float(np.sum(1.0 / w_use)) / n)
    ed, Vd = np.linalg.eigh(DC)
    wtop = Vd[:, int(np.argmax(np.abs(ed)))]
    amp_v = float(np.linalg.norm(Wisq @ v)) / ref
    amp_u = float(np.linalg.norm(Wisq @ wtop)) / ref
    wv = Wsq @ v
    wv = wv / max(float(np.linalg.norm(wv)), 1e-300)
    rot = math.degrees(math.acos(
        min(1.0, abs(float(np.dot(v, wv))))))
    return amp_v, amp_u, rot


def truth_pairs(rungs, Gs):
    """Consecutive full-window pairs: exact congruence + minimizer
    (round-51/52/53 verbatim) + the linear-level projection +
    transport diagnostics."""
    rows = []
    n_skip = 0
    n = NJ
    for ra, rb in zip(rungs[:-1], rungs[1:]):
        if not (ra.get("full") and rb.get("full")):
            n_skip += 1
            continue
        Aa = np.eye(n) - ra["CJ"]
        Ab = np.eye(n) - rb["CJ"]
        DC = ra["CJ"] - rb["CJ"]           # A_{h+1} = A_h + DC
        ew, Vw = np.linalg.eigh(Aa)
        row = dict(ha=ra["h"], hb=rb["h"], kza=ra["kz"],
                   kzb=rb["kz"], pd=bool(ew[0] > 0.0),
                   tau=float(ew[0]))
        if not row["pd"]:
            rows.append(row)
            continue
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
                      / max(float(np.linalg.norm(Ab)), 1e-300))
        row["lam_min"] = float(lam[0])
        row["eta"] = 1.0 + float(lam[0])
        vmin = Wisq @ U[:, 0]
        vmin = vmin / float(np.linalg.norm(vmin))
        row["a_h"] = float(vmin @ (Aa @ vmin))
        row["d_h"] = float(vmin @ (DC @ vmin))
        row["ray_dev"] = (abs(row["d_h"] / row["a_h"]
                              - row["lam_min"])
                          / max(1.0, abs(row["lam_min"])))
        row["amp_v"], row["amp_u"], row["rot"] = frame_diags(
            Aa, DC, vmin, pseudo_abs=False)
        row.update(step_projection(ra, rb, vmin,
                                   Gs[ra["kz"]], Gs[rb["kz"]]))
        rows.append(row)
    return rows, n_skip


def smooth_pairs(rungs, Gs):
    """Smooth full-window pairs: the general branch (A_s indefinite)
    + the same projection with smooth masses + |A| diagnostics."""
    rows = []
    n_skip = n_vdead = 0
    n = NJ
    for ra, rb in zip(rungs[:-1], rungs[1:]):
        if not (ra.get("full") and rb.get("full")):
            n_skip += 1
            continue
        Aa = np.eye(n) - ra["CJ"]
        DC = ra["CJ"] - rb["CJ"]
        ew = np.linalg.eigvalsh(Aa)
        row = dict(ha=ra["h"], hb=rb["h"], pd=bool(ew[0] > 0.0))
        mu, Vg = np.linalg.eig(np.linalg.solve(Aa, DC))
        i_min = int(np.argmin(mu.real))
        row["mu_min"] = float(mu[i_min].real)
        vs = np.real(Vg[:, i_min])
        nv = float(np.linalg.norm(vs))
        if nv < 1e-12:
            n_vdead += 1
            rows.append(row)
            continue
        vs = vs / nv
        row["a_h"] = float(vs @ (Aa @ vs))
        row["d_h"] = float(vs @ (DC @ vs))
        row["amp_v"], row["amp_u"], row["rot"] = frame_diags(
            Aa, DC, vs, pseudo_abs=True)
        row.update(step_projection(ra, rb, vs,
                                   Gs[ra["kz"]], Gs[rb["kz"]]))
        rows.append(row)
    return rows, n_skip, n_vdead


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


def med(v):
    v = [x for x in v if np.isfinite(x)]
    return float(np.median(v)) if v else float("nan")


def fixed_points(K, p):
    """Fixed points of g(eta) = 1 - K eta^{-p} on (0, 1]
    (SPEC v1(iv)/(v)).  Returns a list of dicts (eta, gp, stable),
    sorted ascending."""
    if p <= 0.0:
        if K < 1.0:
            return [dict(eta=1.0 - K, gp=0.0, stable=True)]
        return []
    es = np.logspace(-8, 0.0, 20001)
    ph = es - 1.0 + K * np.power(es, -p)

    def phi(e):
        return e - 1.0 + K * e ** (-p)

    roots = []
    for i in range(len(es) - 1):
        if ph[i] == 0.0:
            roots.append(float(es[i]))
        elif ph[i] * ph[i + 1] < 0.0:
            lo, hi = float(es[i]), float(es[i + 1])
            for _ in range(200):
                mid = 0.5 * (lo + hi)
                if phi(lo) * phi(mid) <= 0.0:
                    hi = mid
                else:
                    lo = mid
            roots.append(0.5 * (lo + hi))
    out = []
    for r in sorted(roots):
        gp = p * K * r ** (-p - 1.0)
        out.append(dict(eta=r, gp=gp, stable=bool(gp < 1.0)))
    return out


def loop_analysis(tag, K, p, etas_all):
    """Print the fixed-point structure of g(eta) = 1 - K eta^{-p}
    and return (has_attractor, basin_frac, eta_star)."""
    fps = fixed_points(K, p)
    if not fps:
        print("    %-22s K %.4f  p %.4f: NO positive fixed point "
              "(K above the tangency) -- loop has no anchor"
              % (tag, K, p))
        return False, 0.0, float("nan")
    for f in fps:
        print("    %-22s K %.4f  p %.4f: eta* %.4f  |g'| %.4f  "
              "-> %s" % (tag, K, p, f["eta"], f["gp"],
                         "STABLE" if f["stable"] else "UNSTABLE"))
    upper = fps[-1]
    if not upper["stable"]:
        return False, 0.0, float(upper["eta"])
    thresh = fps[0]["eta"] if len(fps) >= 2 else 0.0
    basin = float(np.mean(np.asarray(etas_all) > thresh))
    print("    %-22s basin of eta* = (%.4f, 1]; ladder census: "
          "%d/%d etas inside (frac %.2f); min ladder eta %.4f"
          % ("", thresh, int(round(basin * len(etas_all))),
             len(etas_all), basin, float(np.min(etas_all))))
    return True, basin, float(upper["eta"])


def main():
    section("PRIME.PORT.TRANSPORT.01 -- what staying PD costs the "
            "transport (EXPLORATION ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s"
          % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
    print("    NO RH claim; no marker moves.")
    print("\nS0 -- firewall")
    check("S0.1 AST firewall clean (no sieve needed: deployed "
          "prefix tables only)", not ast_scan(BANNED_IDS))

    # ------------------------------------------------------------ W
    section("W -- build the ladders (one Gram per rung; alias "
            "densities + mass-free tent tests; h <= %d)"
            % H_DEEP_MAX)
    rungs, srungs = [], []
    rrs, Gs = {}, {}
    n_smooth_dead = 0
    for kz in core.frame_a_zones():
        rr = core.build_window(kz)
        r = rung_rec(kz, rr_cache=rr)
        if not isinstance(r, dict):
            continue
        rrs[kz] = rr
        Gs[kz] = tent_alias_G(r["uu"], r["alpha"], r["M"])
        rungs.append(r)
        uu = np.asarray(rr["uu"], float)
        rs = rung_rec(kz, comb=(uu, smooth_masses(uu)),
                      rr_cache=rr)
        if isinstance(rs, dict):
            srungs.append(rs)
        else:
            n_smooth_dead += 1
    rungs.sort(key=lambda r: (r["h"], r["kz"]))
    srungs.sort(key=lambda r: (r["h"], r["kz"]))
    print("    truth: %d rungs, h %d .. %d | smooth-mass: %d "
          "rungs, %d chain/window deaths  [%.1f s]"
          % (len(rungs), rungs[0]["h"], rungs[-1]["h"],
             len(srungs), n_smooth_dead, time.time() - T0))
    pref_dev = max(float(np.max(np.abs(
        2.0 * np.asarray(rr["lam"], float)
        - np.asarray(core.MU_ALL, float)[:int(rr["n_atom"])])))
        for rr in rrs.values())
    check("W1 >= %d truth rungs built" % MIN_RUNGS,
          len(rungs) >= MIN_RUNGS, "%d rungs" % len(rungs),
          kill="K1")
    check("W1b atom prefix law exact (max |mm - MU_ALL prefix| "
          "%.1e == 0)" % pref_dev, pref_dev == 0.0, kill="K1")
    jav_ok = all(r["jav"] == list(JWIN) for r in rungs
                 if r.get("full"))
    check("W2 coordinate freeze: jav == JWIN in order on every "
          "truth full-window rung", jav_ok, kill="K1")
    lin_t = max(lin_dev(r, Gs[r["kz"]]) for r in rungs)
    lin_s = max(lin_dev(r, Gs[r["kz"]]) for r in srungs)
    check("W5 LINEARITY WARD: own per-atom tent rows reassemble "
          "the deployed alias density (max rel dev truth %.1e, "
          "smooth %.1e <= %.0e)" % (lin_t, lin_s, LIN_WARD),
          lin_t <= LIN_WARD and lin_s <= LIN_WARD, kill="KW")
    if KILLS:
        return finish({})

    trows_all, n_skip_t = truth_pairs(rungs, Gs)
    trows = [r for r in trows_all if r["pd"]]
    check("W3 >= %d truth full-window pairs (%d skips), all "
          "bases PD" % (MIN_PAIRS, n_skip_t),
          len(trows) >= MIN_PAIRS
          and len(trows) == len(trows_all),
          "%d pairs" % len(trows), kill="K1")
    if KILLS:
        return finish({})
    nil_max = 0.0
    for r in trows:
        if r["flow"] != "LEAVE":
            continue
        rb = next(x for x in rungs
                  if x["kz"] == r["kzb"] and x["h"] == r["hb"])
        klo, khi = rb["n_atom"], rb["n_atom"] + r["nblk"]
        Gb_blk = tent_alias_G(
            np.asarray(core.U_ALL, float)[klo:khi],
            rb["alpha"], rb["M"])
        nil_max = max(nil_max, float(np.max(np.abs(Gb_blk))))
    check("W6 X1-NIL WARD: leaving blocks are BITWISE invisible "
          "to the arrival geometry (max |G| %.1e == 0)"
          % nil_max, nil_max == 0.0, kill="KW")

    # ------------------------------------------------------------ R0
    section("R0 -- the exact congruence + the round-52 anchors "
            "(%d truth pairs)" % len(trows))
    asym_max = float(np.max([r["asym"] for r in trows]))
    rec_max = float(np.max([r["rec"] for r in trows]))
    ray_max = float(np.max([r["ray_dev"] for r in trows]))
    check("R0.a SYMMETRIZATION WARD: max ||H - H^T||/||H|| "
          "%.2e <= %.0e" % (asym_max, ASYM_WARD),
          asym_max <= ASYM_WARD, kill="KW")
    check("R0.b RECONSTRUCTION WARD: max rel "
          "||A^{1/2}(I+H)A^{1/2} - A_{h+1}|| %.2e <= %.0e"
          % (rec_max, RECON_WARD), rec_max <= RECON_WARD,
          kill="KW")
    check("R0.c RAYLEIGH IDENTITY WARD: max |vDv/vAv - lam_min| "
          "%.2e <= %.0e (r_h IS lambda_min)"
          % (ray_max, RAY_WARD), ray_max <= RAY_WARD, kill="KW")
    etas = np.array([r["eta"] for r in trows])
    min_eta = float(np.min(etas))
    med_eta = float(np.median(etas))
    max_neg = float(np.max([-r["lam_min"] for r in trows]))
    check("R0.d LEDGER: %d pairs == %d, min eta %.4f == %.4f, "
          "max(-lam_min) %.4f == %.4f (tol %.0e), med eta %.4f "
          "== %.2f (tol %.0e)"
          % (len(trows), REF_N_TRUTH_PAIRS, min_eta,
             REF_TRUTH_MINETA, max_neg, REF_TRUTH_MAXNEG, TOL4,
             med_eta, REF_TRUTH_MEDETA, TOL2),
          len(trows) == REF_N_TRUTH_PAIRS
          and abs(min_eta - REF_TRUTH_MINETA) <= TOL4
          and abs(max_neg - REF_TRUTH_MAXNEG) <= TOL4
          and abs(med_eta - REF_TRUTH_MEDETA) <= TOL2,
          kill="KW")
    lha = np.log([r["ha"] for r in trows])
    _, b_eta, _ = ols(lha, np.log(etas))
    _, b_tau, _ = ols(lha, np.log([r["tau"] for r in trows]))
    neg = [r for r in trows if r["lam_min"] < 0.0]
    lhn = np.log([r["ha"] for r in neg])
    _, b_d, _ = ols(lhn, np.log([abs(r["d_h"]) for r in neg]))
    _, b_a, _ = ols(lhn, np.log([r["a_h"] for r in neg]))
    check("R0.e SLOPES: eta %+0.4f == %+0.3f (tol %.0e), tau "
          "%+0.4f == %+0.2f (tol %.0e), b_d %+0.4f == %+0.3f, "
          "b_a %+0.4f == %+0.3f (tol %.0e)"
          % (b_eta, REF_SLOPE_ETA, TOL3, b_tau, REF_SLOPE_TAU,
             TOL2, b_d, REF_SLOPE_D, b_a, REF_SLOPE_A, TOL3),
          abs(b_eta - REF_SLOPE_ETA) <= TOL3
          and abs(b_tau - REF_SLOPE_TAU) <= TOL2
          and abs(b_d - REF_SLOPE_D) <= TOL3
          and abs(b_a - REF_SLOPE_A) <= TOL3, kill="KW")
    print("    dangerous-direction subset: lambda_min < 0 on "
          "%d/%d steps" % (len(neg), len(trows)))

    # ------------------------------------------------------------ T1
    section("T1 -- THE TRANSPORT ANATOMY: T = F (frame "
            "distortion) x R (resolvent amplification), exactly")
    print("    truth (neg steps):")
    print("    step        |r|      T          F          R     "
          "     amp(v)    amp(wtop)  rot(deg)")
    facts = []
    n_degen = 0
    fact_dev = tfact_dev = 0.0
    for pos, r in enumerate(trows):
        r["pos"] = pos
        if r["lam_min"] >= 0.0:
            continue
        f = factorize(r)
        if f is None:
            n_degen += 1
            continue
        fact_dev = max(fact_dev, f["dev"])
        tfact_dev = max(tfact_dev, f["tdev"])
        r["fact"] = f
        facts.append((r, f))
        print("    h %3d->%3d  %.4f  %.3e  %.3e  %.3e  %8.3f  "
              "%8.3f  %7.2f"
              % (r["ha"], r["hb"], f["r_abs"], f["T"], f["F"],
                 f["R"], r["amp_v"], r["amp_u"], r["rot"]))
    check("T1.1 FACT WARD: |C M T - |r|| %.1e <= %.0e on every "
          "step (%d degenerate excluded)"
          % (fact_dev, FACT_WARD, n_degen),
          fact_dev <= FACT_WARD, kill="KW")
    medC = med([math.log(f["C"]) for _r, f in facts])
    medM = med([math.log(f["M"]) for _r, f in facts])
    medT = med([math.log(f["T"]) for _r, f in facts])
    mC, mM, mT = math.exp(medC), math.exp(medM), math.exp(medT)
    check("R0.f ROUND-53 FACTOR ANCHOR: truth medians C %.4f == "
          "%.2f, M %.4f == %.2f, T %.4f == %.2f (tol %.0e)"
          % (mC, REF_MED_C, mM, REF_MED_M, mT, REF_MED_T, TOL2),
          abs(mC - REF_MED_C) <= TOL2
          and abs(mM - REF_MED_M) <= TOL2
          and abs(mT - REF_MED_T) <= TOL2, kill="KW")

    srows, n_skip_s, n_vdead = smooth_pairs(srungs, Gs)
    s_ok = [r for r in srows if "dv" in r]
    sfacts = []
    n_sdegen = 0
    for i, r in enumerate(srows):
        r["pos"] = i
        if "dv" not in r:
            continue
        f = factorize(r)
        if f is None:
            n_sdegen += 1
            continue
        tfact_dev = max(tfact_dev, f["tdev"])
        r["fact"] = f
        sfacts.append((r, f))
    check("T1.2 TFACT WARD: |F R - T| %.1e <= %.0e on every "
          "truth AND smooth step (%d smooth degenerate)"
          % (tfact_dev, TFACT_WARD, n_sdegen),
          tfact_dev <= TFACT_WARD, kill="KW")
    print("\n    smooth (general branch, |A| diagnostics; %d "
          "pairs, %d eigenvector deaths):" % (len(srows), n_vdead))
    print("    step        |r|        T          F          R    "
          "      a-sign  amp(v)    rot(deg)")
    for r, f in sfacts:
        print("    h %3d->%3d  %.3e  %.3e  %.3e  %.3e  %-4s   "
              "%8.3f  %7.2f"
              % (r["ha"], r["hb"], f["r_abs"], f["T"], f["F"],
                 f["R"], "neg" if r["a_h"] < 0.0 else "pos",
                 r["amp_v"], r["rot"]))
    print("\n    SUB-FACTOR LADDERS (log10), truth vs smooth:")
    for nm, key in (("T", "T"), ("F (frame)", "F"),
                    ("R (resolvent)", "R")):
        lt = [math.log10(f[key]) for _r, f in facts]
        ls = [math.log10(f[key]) for _r, f in sfacts]
        print("      %-14s truth %s" % (nm, quart(lt)))
        print("      %-14s smooth %s  (med ratio smooth/truth "
              "10^%+.2f)" % ("", quart(ls), med(ls) - med(lt)))
    for nm, key in (("amp(v)", "amp_v"), ("rot(deg)", "rot")):
        lt = [r[key] for r, _f in facts]
        ls = [r[key] for r, _f in sfacts]
        print("      %-14s truth med %.3f | smooth med %.3f"
              % (nm, med(lt), med(ls)))
    medT_s = med([math.log(f["T"]) for _r, f in sfacts])
    medR_s = med([math.log(f["R"]) for _r, f in sfacts])
    medF_s = med([math.log(f["F"]) for _r, f in sfacts])
    medR_t = med([math.log(f["R"]) for _r, f in facts])
    medF_t = med([math.log(f["F"]) for _r, f in facts])
    domin = ("RESOLVENT" if (medR_s - medR_t)
             >= (medF_s - medF_t) else "FRAME")
    r_worst, f_worst = max(sfacts, key=lambda t: t[1]["r_abs"])
    print("    smooth |r| median %.3e, max %.3e at h %d->%d "
          "(the round-53 '4e2' step; SPEC v2(b)); smooth T "
          "median %.3e"
          % (math.exp(med([math.log(f["r_abs"])
                           for _r, f in sfacts])),
             f_worst["r_abs"], r_worst["ha"], r_worst["hb"],
             math.exp(medT_s)))
    print("    WHERE THE EXPLOSION LIVES (median log10 excess "
          "smooth - truth): F %+0.2f | R %+0.2f -> %s"
          % ((medF_s - medF_t) / math.log(10.0),
             (medR_s - medR_t) / math.log(10.0), domin))
    check("T1.3 report: smooth transport explosion is carried by "
          "the %s sub-factor (typed report, never kills)"
          % domin, True)

    # ------------------------------------------------------------ T2
    section("T2 -- THE DISCRIMINATING LAW: is T bounded by the "
            "PREVIOUS step's margin eta_prev?")
    seq = []
    n_nopred = 0
    for r, f in facts:
        if r["pos"] == 0:
            n_nopred += 1
            continue
        seq.append((trows[r["pos"] - 1]["eta"], f["T"], r))
    print("    %d law steps (neg factorized with predecessor; "
          "%d excluded without one)" % (len(seq), n_nopred))
    print("    step        eta_prev   T          eta_this")
    for ep, tt, r in seq:
        print("    h %3d->%3d  %.4f     %.3e  %.4f"
              % (r["ha"], r["hb"], ep, tt, r["eta"]))
    lab = "TRANSPORT-LAWLESS"
    c_env = p_env = eta_star = float("nan")
    if len(seq) >= MIN_LAW:
        ep_v = np.array([s[0] for s in seq])
        t_v = np.array([s[1] for s in seq])
        n_fit = int(math.ceil(2.0 * len(seq) / 3.0))
        corr_le = float(np.corrcoef(np.log(t_v),
                                    np.log(1.0 / ep_v))[0, 1])
        print("\n    corr(log T, log(1/eta_prev)) = %+0.4f  "
              "(positive = the candidate direction T grows as "
              "the previous" % corr_le)
        print("    margin thins; negative = INVERTED: the "
              "transport is smallest after the thinnest margins)")
        print("    THREE FITS T = a + b x (train %d, held-out "
              "%d):" % (n_fit, len(seq) - n_fit))
        best = None
        for nm, x in (("1/eta_prev", 1.0 / ep_v),
                      ("1/sqrt(eta_prev)", 1.0 / np.sqrt(ep_v)),
                      ("log(1/eta_prev)", np.log(1.0 / ep_v))):
            a, b, r2 = ols(x[:n_fit], t_v[:n_fit])
            rmse = float(np.sqrt(np.mean(
                (t_v[n_fit:] - a - b * x[n_fit:]) ** 2)))
            print("      T ~ a + b %-18s b %+8.4f  R^2(in) "
                  "%6.3f  RMSE(out) %.4f" % (nm, b, r2, rmse))
            if best is None or rmse < best[1]:
                best = (nm, rmse)
        print("    best held-out candidate: %s (RMSE %.4f)"
              % best)
        # (ii) the envelope T <= c / eta^p
        _, b_pow, r2_pow = ols(np.log(1.0 / ep_v[:n_fit]),
                               np.log(t_v[:n_fit]))
        p_env = max(0.0, b_pow)
        c_env = float(np.max(t_v[:n_fit] * ep_v[:n_fit] ** p_env))
        excess = float(np.max(t_v[n_fit:]
                              * ep_v[n_fit:] ** p_env)) / c_env
        env_ok = excess <= ENV_SLACK
        print("    ENVELOPE: log-log slope %+0.4f (R^2 %.3f) -> "
              "p = %.4f%s, c = %.4f; held-out max excess %.3f "
              "(slack %.1f) -> %s"
              % (b_pow, r2_pow, p_env,
                 " (clamped, SPEC v1(iv))" if b_pow < 0.0 else "",
                 c_env, excess, ENV_SLACK,
                 "HOLDS" if env_ok else "FAILS"))
        # (iii) the self-consistent induction candidate
        print("\n    THE SELF-CONSISTENT INDUCTION CANDIDATE: "
              "eta_{h+1} >= 1 - K eta_h^{-p} with K = medC x "
              "medM x c:")
        K = mC * mM * c_env
        has_fp, basin, eta_star = loop_analysis(
            "PRIMARY (med,med,c)", K, p_env, etas)
        q75C = math.exp(float(np.percentile(
            [math.log(f["C"]) for _r, f in facts], 75)))
        q75M = math.exp(float(np.percentile(
            [math.log(f["M"]) for _r, f in facts], 75)))
        c_med = float(np.median(t_v * ep_v ** p_env))
        loop_analysis("variant q75 coupling",
                      q75C * q75M * c_env, p_env, etas)
        loop_analysis("variant median-c",
                      mC * mM * c_med, p_env, etas)
        if env_ok:
            if has_fp and basin >= BASIN_FRAC:
                lab = ("SELFCONSISTENT(c=%.3f, p=%.3f, "
                       "eta*=%.4f)" % (c_env, p_env, eta_star))
            else:
                lab = "TRANSPORT-LAWLESS"
        else:
            lab = "TRANSPORT-UNBOUNDED"
    else:
        print("    fewer than %d law steps -> typed "
              "TRANSPORT-LAWLESS (small-n guard)" % MIN_LAW)
    check("T2.1 typed: %s" % lab, True)

    # ------------------------------------------------------------ T3
    section("T3 -- THE SMOOTH DIVERGENCE POINT: transport "
            "explosion as the EARLY WARNING of the crossing")
    t_env_max = float(np.max([f["T"] for _r, f in facts]))
    print("    truth envelope T_env = max truth T = %.4f"
          % t_env_max)
    print("    idx  step        T_s        T>env  a_s<0")
    first_exp = first_aneg = None
    n_exp = n_aneg = 0
    for r, f in sfacts:
        exp_f = f["T"] > t_env_max
        an_f = r["a_h"] < 0.0
        n_exp += int(exp_f)
        n_aneg += int(an_f)
        if exp_f and first_exp is None:
            first_exp = r["pos"]
        if an_f and first_aneg is None:
            first_aneg = r["pos"]
        print("    %3d  h %3d->%3d  %.3e  %-5s  %-5s"
              % (r["pos"], r["ha"], r["hb"], f["T"],
                 str(exp_f), str(an_f)))
    print("\n    censuses: T_s > T_env on %d/%d smooth steps; "
          "a_s < 0 on %d/%d" % (n_exp, len(sfacts), n_aneg,
                                len(sfacts)))
    print("    (the BASE A_s is indefinite on every smooth pair "
          "-- round-51 SPEC v2(ii) -- so the pair-level")
    print("    sign event is carried by a_s in the dangerous "
          "direction)")
    if first_exp is not None and first_aneg is not None:
        lead = first_aneg - first_exp
        print("    FIRST T-explosion at smooth index %d vs first "
              "a_s < 0 at index %d -> lead %+d step(s): the"
              % (first_exp, first_aneg, lead))
        print("    transport %s the dangerous-direction sign "
              "exit (early-warning reading %s)"
              % ("PRECEDES" if lead > 0 else
                 "coincides with" if lead == 0 else "TRAILS",
                 "stands" if lead >= 0 else "fails"))
    else:
        print("    first indices: T-explosion %s | a_s < 0 %s "
              "(one census empty -- no lead defined)"
              % (str(first_exp), str(first_aneg)))
    check("T3.1 report: divergence indices printed (first "
          "T-explosion %s, first a_s < 0 %s; report-only)"
          % (str(first_exp), str(first_aneg)), True)

    # ------------------------------------------------------------ C
    section("C -- controls")
    n_pd_s = sum(1 for r in srows if r["pd"])
    check("C2 smooth reproduction: %d pairs == %d (%d skips), "
          "PD bases %d == %d (smooth is the PRIMARY control)"
          % (len(srows), REF_N_SMOOTH_PAIRS, n_skip_s, n_pd_s,
             REF_SMOOTH_PD),
          len(srows) == REF_N_SMOOTH_PAIRS
          and n_pd_s == REF_SMOOTH_PD, kill="KW")
    print("\n  C1 -- Epstein/scramble (kz %d, frame must die):"
          % CTRL_KZ)
    ok1 = True
    for nmc, kw in (("Epstein",
                     dict(comb=eps_comb(rrs[CTRL_KZ]),
                          rr_cache=rrs[CTRL_KZ])),
                    ("scramble", dict(scramble_seed=1))):
        try:
            rc = rung_rec(CTRL_KZ, **kw)
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
          ok1, kill="KW")

    return finish(dict(lab=lab, mT=mT,
                       medF=math.exp(medF_t),
                       medR=math.exp(medR_t),
                       medTs=math.exp(medT_s),
                       domin=domin, t_env=t_env_max,
                       first_exp=first_exp,
                       first_aneg=first_aneg))


def finish(lab):
    section("V -- FROZEN VERDICT")
    n_pass = sum(1 for _n, okk in CHECKS if okk)
    n_tot = len(CHECKS)
    if KILLS:
        VERDICT = {"K1": "PIPELINE-BROKEN",
                   "KW": "WARD-BROKEN"}[KILLS[0]]
        print("\n  VERDICT: %s" % VERDICT)
    else:
        VERDICT = "TRANSPORT-MEASURED / %(lab)s" % lab
        print("\n  VERDICT: %s" % VERDICT)
        print("  (truth T med %(mT).4f = F med %(medF).3e x R "
              "med %(medR).3e (SPEC v2(a)); smooth T med "
              "%(medTs).3e, explosion in %(domin)s;" % lab)
        print("   truth envelope T_env %(t_env).4f; smooth "
              "divergence: first T-explosion idx "
              "%(first_exp)s vs first a_s<0 idx %(first_aneg)s)"
              % lab)
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed"
          % (time.time() - T0, n_tot, n_tot - n_pass))
    return 0 if n_pass == n_tot else 1


if __name__ == "__main__":
    raise SystemExit(main())
