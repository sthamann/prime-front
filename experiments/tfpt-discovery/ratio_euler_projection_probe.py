#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""ratio_euler_projection_probe -- PRIME.PORT.RATIOSOURCE.01
(EXPLORATION ONLY, experiments/; round 53, named object (a) from CX:
dissect the O(1) RATIO -- what keeps r_h = (v^T Delta_h v)/(v^T A_h v)
below 1 in magnitude in the dangerous direction?  2026-08-09.)

THE QUESTION (frozen): eta_margin_source_probe (round 52) explained
the SCALE of the margin: the dangerous direction v_min of H_h sits in
the core and d_h = |v^T Delta_h v| and a_h = v^T A_h v collapse
TOGETHER (power slopes -3.716 / -3.456; the fit residuals share 94%
of their variance) -- eta_h = 1 - |r_h| is scale-free because
numerator and denominator are sections of ONE object.  The remaining
question is the bounded ratio itself: r_h at the minimizer IS
lambda_min(H_h) < 0 (Rayleigh ward), with |r_h| <= 0.9950 < 1 on all
31 truth steps.  WHY does the wall energy in the dangerous direction
grow by strictly less than what is already there?  Three frozen
candidates: (C1) DENSITY -- the per-step relative increment of the
v-tested comb mass is bounded by the existing mass (the window grows
by Delta-alpha, the comb mass by ~ e^{u/2} du: a computable window-
geometry number); (C2) ALIGNMENT -- v_min is not aligned with the
direction of maximal increment; (C3) CANCELLATION -- the moving
atoms contribute with oscillating phases cos(tau_j u_n) and the
coherent sum is far below the absolute sum.

THE EXACT LINEAR LEVEL (frozen; the factor_avoidance lesson): the
compressed pipeline has NO separable per-atom OPERATOR channel
(factor_avoidance SPEC v2(ii): on LEAVING steps the moving atoms are
BITWISE invisible to the smaller window -- reproduced here as the X1
nil ward at the lag level -- and on ENTERING steps the grown window
cannot even be built without its new atoms; the increment is the
COLLECTIVE window re-test).  Exact per-atom telescoping through the
pipeline is also infeasible (moving blocks reach thousands of atoms;
one chain build per atom).  The exact per-atom object that DOES
exist is the LAG/DENSITY level (nested_prime_ladder L1.0 machinery):
the alias-node density d(theta_j) is EXACTLY linear in the atoms
(grid_density of atom_lags_at rows), so the |v|^2-tested density
increment splits EXACTLY into per-atom terms + the geometry re-test
(arch change + collective common-atom re-test under the new
geometry).  The operator-level d_h = v^T Delta_h v is tied to this
exact linear level by a MEASURED transport factor; the probe's exact
factorization of |r_h| lives across the two levels.

THE LADDER (frozen, round-51/52 verbatim): all frame-A zones
(core.frame_a_zones()) with h <= 900, sorted by (h, kz); consecutive
FULL-WINDOW pairs (both rungs carry all 12 indices of J = {2, 4,
..., 24}; typed skips counted); truth + smooth-mass world (B1
LATTICE-SMOOTH masses m_n = 2 e^{u_n/2} du_n, midpoint cells,
lattice_parametrix verbatim); Epstein/scramble frame status (C).

COORDINATE FREEZES: on a full window the alias order is exactly
JWIN = (2, 4, ..., 24) (warded); v_min is the A_h^{-1/2}-transported
Euclidean-normalized minimizer of H_h (round-51 convention); v2 =
its squared entries in JWIN order.  HOST geometry of a step = the
rung carrying the moving block (rung b on ENTER, rung a on LEAVE);
the moving block is the U_ALL index range [min(ka, kb), max(ka,
kb)); sigma = -1 on ENTER, +1 on LEAVE (the moebius_source inverse
convention: a leaving block contributes with inverted sign), so the
block terms carry the Delta = C_J(a) - C_J(b) orientation.  The
per-atom alias test is q_n(j) = -(mu_n/2) G_n(theta_j), G_n = the
cosine transform of atom n's tent lag row at alias node j (own
assembly, warded in W5); theta_j = 2 pi j / L, tau_j = theta_j / D.

FROZEN PROTOCOL (2026-08-09; all bars frozen before the run):

 W   PIPELINE WARDS (kill -> PIPELINE-BROKEN): W1 >= 30 truth
     rungs; W1b the atom prefix law exact; W2 jav == JWIN in order
     on every truth full-window rung; W3 >= 20 truth full-window
     pairs, all bases PD.  W5 LINEARITY WARD (kill -> WARD-BROKEN):
     on every truth AND smooth rung, max_j |[d(theta_j) -
     d_arch(theta_j)] - sum_n q_n(j)| / max(1, |d(theta_j)|)
     <= 1e-9 over the 12 aliases -- the own per-atom tent rows
     reassemble the deployed alias density exactly (the
     nested_prime_ladder L1.0 ward at the alias nodes).

 R0  THE EXACT CONGRUENCE + ROUND-52 ANCHOR (kill -> WARD-BROKEN):
     per truth pair (a) SYMMETRIZATION ||H - H^T||/||H|| <= 1e-12,
     (b) RECONSTRUCTION rel <= 1e-10, (c) RAYLEIGH IDENTITY
     |vDv/vAv - lambda_min| / max(1, |lambda_min|) <= 1e-9 (r_h IS
     lambda_min), (d) LEDGER: 31 pairs, min eta 0.0050, max(-lam)
     0.9950 (tol 5.001e-5), med eta 0.29 (tol 5.001e-3),
     (e) SLOPES: eta +0.108 (tol 5.001e-4), tau -2.74 (tol
     5.001e-3), and the round-52 collapse slopes b_d = -3.716 and
     b_a = -3.456 (tol 5.001e-4 each; lambda_min < 0 subset,
     first-rung depth h_a, round-52 convention).  All X tables run
     on the lambda_min < 0 steps (the dangerous-direction subset;
     count and ENTER/LEAVE/NONE census printed).

 X1  THE ATOM-RESOLVED PROJECTION (exact at the linear level): per
     step the split delta_v = GEO_v + ATOM_v of the v-tested alias
     density increment delta_v = sum_j v2_j [d_a(theta_j) -
     d_b(theta_j)]; ATOM_v = sum_{block} c_n with c_n = sigma
     sum_j v2_j q_n^host(j) (exact; W5 wards the assembly); GEO_v
     = delta_v - ATOM_v (= arch change + collective common-atom
     re-test, exact by W5).  Printed per step: flow, block size,
     the coherence ratio coh = |sum c_n| / sum |c_n| (C3), the
     top-atom share max |c_n| / sum |c_n|, the geometry share
     |GEO| / (|GEO| + |ATOM|).  X1 NIL WARD (kill -> WARD-BROKEN):
     on every LEAVING step the block atoms' tent rows at the
     ARRIVAL geometry are identically zero (max |G| == 0 bitwise
     -- the factor_avoidance no-atom-channel degeneracy at the lag
     level).  TRANSPORT (typed, never kills): Pearson
     corr(delta_v, d_h) across the neg steps -- TRANSPORT-FAITHFUL
     iff corr >= 0.7; TRANSPORT-PARTIAL iff >= 0.3;
     TRANSPORT-LOOSE otherwise (honest: the density level is
     exact, the operator transport is measured).

 X2  THE DENSITY BOUND (C1): per step the relative v-weighted mass
     increment m_h = sum_{block} mu_n w_v(u_n) / sum_{common
     prefix} mu_n w_v(u_n), with the |v|^2 spectral profile
     w_v(u) = sum_j v2_j cos^2(tau_j^host u); the raw unweighted
     m_raw = block mass / prefix mass printed alongside.  TYPED:
     DENSITY-BOUNDS iff |r_h| <= m_h on ALL neg steps with a
     nonempty block (margin min m_h/|r_h| printed; the O(1)
     statement is then a weighted-density inequality -- a
     PNT-shaped statement); DENSITY-VIOLATED otherwise (honest).
     NONE-flow steps carry an empty block and are excluded
     (counted).

 X3  THE ALIGNMENT (C2): per step align = |<v_min, w_top>|, w_top
     = eigenvector of Delta_h at the largest |eigenvalue| (the
     maximal-increment direction); |<v_min, w_neg>| at the most
     negative eigenvalue reported alongside.  TYPED by the ladder
     median of align: ALIGN-LOCKED iff med >= 0.75; ALIGN-AVOIDED
     iff med <= 0.25; ALIGN-OBLIQUE otherwise.

 X4  THE SOURCE STATEMENT (the deliverable; exact factorization):
     per neg step, with sigma_v = sum_j v2_j |d_a(theta_j)| (the
     existing v-tested density; the aliases live on the negative
     arm, so magnitudes are taken) and S_abs = sum_{block} |c_n| +
     |GEO_v|:
       |r_h| = C_h x M_h x T_h   EXACTLY, where
       C_h = |delta_v| / S_abs                (cancellation, <= 1
                                               by triangle ineq.;
                                               C3 + geo-atom
                                               cancellation),
       M_h = S_abs / sigma_v                  (relative v-tested
                                               density increment;
                                               C1),
       T_h = (|d_h|/a_h) / (|delta_v|/sigma_v)  (operator-level /
                                               density-level
                                               transport;
                                               C2-flavored).
     FACT WARD (kill -> WARD-BROKEN): |C M T - |r|| <= 1e-10
     max(1, |r|) per step.  Ladder medians + the log-share census
     (median of log F_i / log |r|); TYPED: BOUND-BY-COHERENCE /
     BOUND-BY-DENSITY / BOUND-BY-TRANSPORT = the factor with the
     smallest median log (deterministic tie order C, M, T);
     BOUND-BY-NONE iff that smallest median log >= 0 (honest).
     corr(log T, log align) printed (does the transport factor
     carry the alignment physics).

 C   CONTROLS: (C1, kz 9, must fire, kill -> WARD-BROKEN) Epstein
     (lambda_eps recursion comb) + scramble (seed 1): the
     compressed frame must die (exterior supercritical OR
     lam(C_J) > 1 OR window unavailable); channel reported.
     (C2, kill -> WARD-BROKEN) smooth-world reproduction: 28 full-
     window pairs, 0 PD bases (all CONE-EXITED; round-51/52
     ledger).  (C3, typed) THE SMOOTH CONTRAST ("its r crosses -1
     territory"): per smooth pair the general branch (A_s
     indefinite; mu = eig(A_s^{-1} Delta_s), most negative real
     part; v_s = Euclidean-normalized real part of the
     eigenvector, skipped if its norm < 1e-12, counted) feeds the
     SAME decomposition with the smooth masses; censuses of
     a_s < 0 and of 1 + Re mu_min < 0 printed; TYPED by the
     factor-of-2 rule on the ladder medians of (coh, m_h):
     SMOOTH-DIFFERS(...) listing every factor whose smooth/truth
     median ratio is >= 2 or <= 0.5, else SMOOTH-SIMILAR.

KILLS: K1 a W pipeline ward breaks -> PIPELINE-BROKEN; KW the W5 /
R0 / X1-nil / X4-fact / smooth-reproduction / control ward breaks
-> WARD-BROKEN.  The X1-transport, X2, X3, X4-bound and C3-contrast
labels are TYPED, never kill.

VERDICT (frozen enum): RATIOSOURCE-MEASURED / <TRANSPORT-*> /
<DENSITY-*> / <ALIGN-*> / <BOUND-BY-*> / <SMOOTH-*>; else
PIPELINE-BROKEN / WARD-BROKEN.

FROZEN BARS: H_DEEP_MAX = 900; JWIN = (2, ..., 24); MIN_RUNGS 30;
MIN_PAIRS 20; ASYM_WARD 1e-12; RECON_WARD 1e-10; RAY_WARD 1e-9;
LIN_WARD 1e-9; FACT_WARD 1e-10; TR_HI 0.7; TR_LO 0.3; ALIGN_HI
0.75; ALIGN_LO 0.25; FACT2 2.0; CTRL_KZ 9; scramble seed 1;
reproduction refs (round-52 printed ledger / contract citations):
31 truth pairs / min eta 0.0050 / max(-lam) 0.9950 / med eta 0.29 /
slope eta +0.108 / slope tau -2.74 / slope d -3.716 / slope a
-3.456 / 28 smooth pairs with 0 PD bases; tolerances TOL4 5.001e-5,
TOL3 5.001e-4, TOL2 5.001e-3 (each ref warded at its citation's
print-rounding radius: med eta at TOL2, d/a slopes at TOL3).

SPEC v1 (2026-08-09, frozen + SHA-hashed before the first run);
mechanical concretizations frozen with it: (i) build_window results
are cached per kz and shared truth/smooth (deepcore precedent); the
tent-row alias matrices G are MASS-FREE and shared truth/smooth per
kz (the mass enters linearly at use time -- exactness unchanged);
(ii) all fits use the step's first rung depth h_a and the
lambda_min < 0 subset (round-52 convention); (iii) flow NONE steps
carry an empty block (ATOM_v = 0; coherence and m_h undefined;
excluded from those censuses, counted); (iv) sigma_v uses |d_a|
magnitudes (negative-arm aliases); (v) delta_v == 0 marks a step
DEGENERATE (excluded from the factorization, counted); (vi) the
LEAVE-nil ward is bitwise (== 0.0): a leaving atom has u > 2
alpha_b + 1e-14, and every arrival-geometry tent weight 1 - |iD -
u|/D with i <= M - 1 = 2 alpha/D - 1 is then <= 0 exactly.

SPEC v2 (2026-08-09, after run 1; fail-first preserved -- run 1
passed ALL 20 checks; no bar, reference or typed label was touched;
two REPORT-ONLY prints are added, documented here): (a) X1 gains
the GEOMETRY-OPPOSITION census: run 1's table shows sign(GEO_v)
opposite to sign(ATOM_v) on every neg step -- the bounding
cancellation is GEOMETRY-vs-BLOCK, not atom-vs-atom (the per-atom
coherence has median 1.0000: the moving block lives at the grid
edge, where every even-parity alias j tests it with the SAME sign,
cos((M-1) pi j/(M-1)) = +1 -- the C3 phase mechanism is REFUTED at
the alias level and the census makes the opposition a printed
number).  (b) C3 gains the smooth-vs-truth contrast of the
cancellation factor C = |delta_v|/S_abs: run 1 typed SMOOTH-SIMILAR
on (coh, m_h), so the discriminating physics must sit in the
cancellation/transport pair; the C medians are printed for the
contrast (the frozen C3 typing bar is unchanged).

NO RH claim: coherence ratios, density bounds, alignment angles and
transport factors on finite-h window truncations are measurements
on the deployed v563 ladder, not theorems about zeros.  No marker
moves.

FIREWALL: no zeros, no prime oracles (AST scan; banned ids zetazero
/ nzeros / primerange / isprime / primepi / nextprime / prevprime);
NO sieve is needed (all atoms are read from the deployed U_ALL /
MU_ALL prefix tables); v563 READ-ONLY; RNG only inside the declared
scramble control; stdout only.

Sources (read-only): v563_paper2_readouts (build_window,
atom_lags_at, arch_lags, U_ALL / MU_ALL prefix law -- verbatim);
window compression + congruence + smooth-mass world verbatim from
relative_congruence_probe.py (PRIME.PORT.RELCONG.01) via
eta_margin_source_probe.py (PRIME.PORT.ETASOURCE.01, round 52, the
anchor ledger); the no-atom-channel degeneracy from
factor_avoidance_euler_probe.py (PRIME.PORT.FACTORAVOID.01, SPEC
v2(ii)); per-atom lag linearity from nested_prime_ladder_probe.py
(PRIME.PORT.PRIMELADDER.01, L1.0); the leaving-block inverse
convention from moebius_source_step_probe.py
(PRIME.PORT.MOEBIUS.SOURCE.01); certified base rungs v884/v887
(cited, not re-run).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/ratio_euler_projection_probe.py
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
TR_HI = 0.7
TR_LO = 0.3
ALIGN_HI = 0.75
ALIGN_LO = 0.25
FACT2 = 2.0
CTRL_KZ = 9
BANNED_IDS = ("zetazero", "nzeros", "primerange", "isprime",
              "primepi", "nextprime", "prevprime")

# reproduction refs (round-52 printed ledger / contract citations)
REF_N_TRUTH_PAIRS = 31
REF_TRUTH_MINETA = 0.0050
REF_TRUTH_MAXNEG = 0.9950
REF_TRUTH_MEDETA = 0.29
REF_SLOPE_ETA = +0.108
REF_SLOPE_TAU = -2.74
REF_SLOPE_D = -3.716
REF_SLOPE_A = -3.456
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


# --------- pipeline, verbatim from relative_congruence / eta_margin
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
    atom n's UNIT tent lag row at alias node theta_j (own assembly
    of the deployed atom_lags_at tents, incl. the u < D reflection;
    warded in W5 against the deployed builder).  q_n(j) =
    -(mu_n/2) G[n, j]."""
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
    """The exact linear-level split + the X2/X4 quantities for one
    step in direction v (world-agnostic; masses from the recs)."""
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
        out["coh"] = (abs(out["atom"]) / out["cabs"]
                      if out["cabs"] > 0.0 else float("nan"))
        out["top"] = (float(np.max(np.abs(cvec))) / out["cabs"]
                      if out["cabs"] > 0.0 else float("nan"))
        tau = (2.0 * math.pi * np.array(JWIN, float)
               / host["L"]) / host["D"]
        wv_blk = np.cos(np.outer(host["uu"][klo:khi], tau)) ** 2 @ v2
        wv_pre = np.cos(np.outer(host["uu"][:klo], tau)) ** 2 @ v2
        num = float(np.sum(host["mm"][klo:khi] * wv_blk))
        den = float(np.sum(host["mm"][:klo] * wv_pre))
        out["m_h"] = num / den if den > 0.0 else float("nan")
        out["m_raw"] = (float(np.sum(host["mm"][klo:khi]))
                        / float(np.sum(host["mm"][:klo])))
    else:
        out["atom"] = 0.0
        out["cabs"] = 0.0
        out["coh"] = float("nan")
        out["top"] = float("nan")
        out["m_h"] = float("nan")
        out["m_raw"] = float("nan")
    out["geo"] = dv - out["atom"]
    tot = abs(out["geo"]) + abs(out["atom"])
    out["geoshare"] = abs(out["geo"]) / tot if tot > 0.0 \
        else float("nan")
    out["sabs"] = out["cabs"] + abs(out["geo"])
    return out


def factorize(row):
    """X4: |r| = C x M x T exactly (definitions; SPEC v1(v))."""
    r_abs = abs(row["d_h"]) / abs(row["a_h"])
    if abs(row["dv"]) <= 0.0 or row["sabs"] <= 0.0 \
            or row["sig_v"] <= 0.0:
        return None
    C = abs(row["dv"]) / row["sabs"]
    Mf = row["sabs"] / row["sig_v"]
    T = r_abs / (abs(row["dv"]) / row["sig_v"])
    return dict(r_abs=r_abs, C=C, M=Mf, T=T,
                dev=abs(C * Mf * T - r_abs) / max(1.0, r_abs))


def truth_pairs(rungs, Gs):
    """Consecutive full-window pairs: exact congruence + minimizer
    (round-51/52 verbatim) + the linear-level projection."""
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
        ed, Vd = np.linalg.eigh(DC)
        itop = int(np.argmax(np.abs(ed)))
        row["align"] = float(abs(vmin @ Vd[:, itop]))
        row["align_neg"] = float(abs(vmin @ Vd[:, 0]))
        row.update(step_projection(ra, rb, vmin,
                                   Gs[ra["kz"]], Gs[rb["kz"]]))
        rows.append(row)
    return rows, n_skip


def smooth_pairs(rungs, Gs):
    """Smooth full-window pairs: the general branch (A_s possibly
    indefinite) + the same projection with smooth masses."""
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


def main():
    section("PRIME.PORT.RATIOSOURCE.01 -- the SOURCE of the O(1) "
            "ratio r_h = vDv/vAv (EXPLORATION ONLY)")
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

    # ------------------------------------------------------------ R0
    section("R0 -- the exact congruence + the round-52 anchor "
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
          "b_a %+0.4f == %+0.3f (tol %.0e; round-52 collapse "
          "slopes)"
          % (b_eta, REF_SLOPE_ETA, TOL3, b_tau, REF_SLOPE_TAU,
             TOL2, b_d, REF_SLOPE_D, b_a, REF_SLOPE_A, TOL3),
          abs(b_eta - REF_SLOPE_ETA) <= TOL3
          and abs(b_tau - REF_SLOPE_TAU) <= TOL2
          and abs(b_d - REF_SLOPE_D) <= TOL3
          and abs(b_a - REF_SLOPE_A) <= TOL3, kill="KW")
    n_e = sum(1 for r in trows if r["flow"] == "ENTER")
    n_l = sum(1 for r in trows if r["flow"] == "LEAVE")
    n_n = sum(1 for r in trows if r["flow"] == "NONE")
    print("    dangerous-direction subset: lambda_min < 0 on "
          "%d/%d steps; flow census ENTER %d / LEAVE %d / NONE "
          "%d" % (len(neg), len(trows), n_e, n_l, n_n))

    # ------------------------------------------------------------ X1
    section("X1 -- THE ATOM-RESOLVED PROJECTION (exact at the "
            "linear level; %d neg steps)" % len(neg))
    print("    delta_v = sum_j v2_j [d_a - d_b](theta_j) = GEO_v "
          "+ ATOM_v; c_n = sigma sum_j v2_j q_n(j)")
    print("    step        flow   nblk   delta_v     GEO_v       "
          "ATOM_v      geo-sh  coh     top")
    for r in neg:
        print("    h %3d->%3d  %-5s %5d  %+.3e  %+.3e  %+.3e  "
              "%.4f  %.4f  %.4f"
              % (r["ha"], r["hb"], r["flow"], r["nblk"], r["dv"],
                 r["geo"], r["atom"], r["geoshare"], r["coh"],
                 r["top"]))
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
    check("X1.1 NIL WARD: leaving blocks are BITWISE invisible "
          "to the arrival geometry (max |G| %.1e == 0 over all "
          "LEAVE steps -- the factor_avoidance no-atom-channel "
          "degeneracy at the lag level)" % nil_max,
          nil_max == 0.0, kill="KW")
    dv_v = np.array([r["dv"] for r in neg])
    dh_v = np.array([r["d_h"] for r in neg])
    tr_corr = float(np.corrcoef(dv_v, dh_v)[0, 1])
    cohs = [r["coh"] for r in neg if np.isfinite(r["coh"])]
    n_blk = [r for r in neg if r["nblk"] > 0]
    n_opp = sum(1 for r in n_blk
                if r["geo"] * r["atom"] < 0.0)
    print("\n    GEOMETRY-OPPOSITION census (SPEC v2(a), report):"
          " sign(GEO_v) opposite to sign(ATOM_v) on %d/%d steps"
          % (n_opp, len(n_blk)))
    print("    coherence ladder (C3, block atoms): %s"
          % quart(cohs))
    print("    top-atom share ladder: %s"
          % quart([r["top"] for r in neg
                   if np.isfinite(r["top"])]))
    print("    geometry-share ladder: %s"
          % quart([r["geoshare"] for r in neg]))
    tr_label = ("TRANSPORT-FAITHFUL" if tr_corr >= TR_HI
                else "TRANSPORT-PARTIAL" if tr_corr >= TR_LO
                else "TRANSPORT-LOOSE")
    check("X1.2 typed: %s (Pearson corr(delta_v, d_h) = %+0.4f; "
          "bars %.1f / %.1f)"
          % (tr_label, tr_corr, TR_HI, TR_LO), True)

    # ------------------------------------------------------------ X2
    section("X2 -- THE DENSITY BOUND (C1): is |r_h| <= m_h, the "
            "relative |v|^2-weighted mass increment?")
    print("    step        flow    |r_h|    m_h       m_raw     "
          "m_h/|r_h|")
    ratios = []
    n_none = 0
    for r in neg:
        r_abs = abs(r["d_h"]) / abs(r["a_h"])
        if not np.isfinite(r["m_h"]):
            n_none += 1
            print("    h %3d->%3d  %-5s  %.4f   (empty block -- "
                  "excluded)" % (r["ha"], r["hb"], r["flow"],
                                 r_abs))
            continue
        ratios.append(r["m_h"] / r_abs)
        print("    h %3d->%3d  %-5s  %.4f   %.4f    %.4f    "
              "%8.3f"
              % (r["ha"], r["hb"], r["flow"], r_abs, r["m_h"],
                 r["m_raw"], r["m_h"] / r_abs))
    min_ratio = float(np.min(ratios)) if ratios else float("nan")
    dens_label = ("DENSITY-BOUNDS" if ratios and min_ratio >= 1.0
                  else "DENSITY-VIOLATED")
    print("\n    margin ladder m_h/|r_h|: %s | min %.3f (%d "
          "empty-block steps excluded)"
          % (quart(ratios), min_ratio, n_none))
    check("X2.1 typed: %s (min m_h/|r_h| = %.3f vs bar 1.0)"
          % (dens_label, min_ratio), True)
    if dens_label == "DENSITY-BOUNDS":
        print("    THE O(1) STATEMENT IS A WEIGHTED-DENSITY "
              "INEQUALITY: the v-tested comb mass entering per")
        print("    step never exceeds the existing v-tested mass "
              "-- a PNT-shaped relative-density bound.")

    # ------------------------------------------------------------ X3
    section("X3 -- THE ALIGNMENT (C2): v_min vs the maximal-"
            "increment direction of Delta_h")
    print("    step        align(top |eig|)  align(most neg "
          "eig)  eta")
    for r in neg:
        print("    h %3d->%3d      %.4f            %.4f         "
              "%.4f" % (r["ha"], r["hb"], r["align"],
                        r["align_neg"], r["eta"]))
    al_v = [r["align"] for r in neg]
    med_al = float(np.median(al_v))
    align_label = ("ALIGN-LOCKED" if med_al >= ALIGN_HI
                   else "ALIGN-AVOIDED" if med_al <= ALIGN_LO
                   else "ALIGN-OBLIQUE")
    print("\n    align ladder: %s | align(neg) ladder: %s"
          % (quart(al_v), quart([r["align_neg"] for r in neg])))
    check("X3.1 typed: %s (median align %.4f; bars %.2f / %.2f)"
          % (align_label, med_al, ALIGN_HI, ALIGN_LO), True)

    # ------------------------------------------------------------ X4
    section("X4 -- THE SOURCE STATEMENT: |r| = C (coherence) x M "
            "(density) x T (transport), exactly")
    print("    step        |r_h|     C         M          T     "
          "     logC    logM    logT")
    facts = []
    n_degen = 0
    fact_dev = 0.0
    for r in neg:
        f = factorize(r)
        if f is None:
            n_degen += 1
            continue
        fact_dev = max(fact_dev, f["dev"])
        facts.append((r, f))
        print("    h %3d->%3d  %.4f   %.4f   %.3e  %.3e  %+7.3f "
              "%+7.3f %+7.3f"
              % (r["ha"], r["hb"], f["r_abs"], f["C"], f["M"],
                 f["T"], math.log(f["C"]), math.log(f["M"]),
                 math.log(f["T"])))
    check("X4.1 FACT WARD: |C M T - |r|| %.1e <= %.0e on every "
          "step (%d degenerate excluded)"
          % (fact_dev, FACT_WARD, n_degen),
          fact_dev <= FACT_WARD, kill="KW")
    logC = [math.log(f["C"]) for _r, f in facts]
    logM = [math.log(f["M"]) for _r, f in facts]
    logT = [math.log(f["T"]) for _r, f in facts]
    logR = [math.log(f["r_abs"]) for _r, f in facts]
    medC, medM, medT = med(logC), med(logM), med(logT)
    print("\n    ladder medians: C %.4f | M %.4f | T %.4f  "
          "(log medians %+0.3f / %+0.3f / %+0.3f; median "
          "log|r| %+0.3f)"
          % (math.exp(medC), math.exp(medM), math.exp(medT),
             medC, medM, medT, med(logR)))
    print("    log-share census (median log F / median log |r|):"
          " C %.3f | M %.3f | T %.3f"
          % (medC / med(logR), medM / med(logR),
             medT / med(logR)))
    labels3 = (("BOUND-BY-COHERENCE", medC),
               ("BOUND-BY-DENSITY", medM),
               ("BOUND-BY-TRANSPORT", medT))
    bound_label, bound_med = min(labels3, key=lambda t: t[1])
    if bound_med >= 0.0:
        bound_label = "BOUND-BY-NONE"
    alog = [math.log(max(r["align"], 1e-12)) for r, _f in facts]
    cTA = float(np.corrcoef(logT, alog)[0, 1])
    print("    corr(log T, log align) = %+0.4f (does the "
          "transport factor carry the alignment physics)" % cTA)
    check("X4.2 typed: %s (smallest median log factor %+0.3f)"
          % (bound_label, bound_med), True)
    print("\n    THE NAMED CANDIDATE (printed, not claimed): in "
          "the dangerous direction the per-step wall-energy")
    print("    ratio factorizes exactly as coherence x density x "
          "transport across the exact linear (lag)")
    print("    level; the typed labels above name which factor "
          "carries |r| < 1 on the deployed ladder.")

    # ------------------------------------------------------------ C
    section("C -- controls")
    srows, n_skip_s, n_vdead = smooth_pairs(srungs, Gs)
    n_pd_s = sum(1 for r in srows if r["pd"])
    check("C2 smooth reproduction: %d pairs == %d (%d skips), "
          "PD bases %d == %d (all CONE-EXITED)"
          % (len(srows), REF_N_SMOOTH_PAIRS, n_skip_s, n_pd_s,
             REF_SMOOTH_PD),
          len(srows) == REF_N_SMOOTH_PAIRS
          and n_pd_s == REF_SMOOTH_PD, kill="KW")
    print("\n  C3 -- the smooth contrast (general branch, %d "
          "pairs, %d eigenvector deaths):" % (len(srows),
                                              n_vdead))
    print("    step        1+mu_min   a_h sign  |r_s|      coh   "
          "  m_h      geo-sh")
    s_ok = [r for r in srows if "dv" in r]
    n_cross = sum(1 for r in srows
                  if 1.0 + r.get("mu_min", 0.0) < 0.0)
    n_aneg = sum(1 for r in s_ok if r["a_h"] < 0.0)
    for r in s_ok:
        r_abs = abs(r["d_h"]) / max(abs(r["a_h"]), 1e-300)
        print("    h %3d->%3d  %+8.3f   %-4s      %.3e  %.4f  "
              "%.4f   %.4f"
              % (r["ha"], r["hb"], 1.0 + r["mu_min"],
                 "neg" if r["a_h"] < 0.0 else "pos", r_abs,
                 r["coh"], r["m_h"], r["geoshare"]))
    print("    censuses: 1 + mu_min < 0 on %d/%d steps "
          "(crossing territory); a_s < 0 on %d/%d (cone-exit "
          "signature)" % (n_cross, len(srows), n_aneg,
                          len(s_ok)))
    med_coh_t = med(cohs)
    med_coh_s = med([r["coh"] for r in s_ok])
    med_m_t = med([r["m_h"] for r in neg])
    med_m_s = med([r["m_h"] for r in s_ok])
    print("    medians  truth vs smooth: coh %.4f vs %.4f "
          "(ratio %.2f) | m_h %.4f vs %.4f (ratio %.2f)"
          % (med_coh_t, med_coh_s, med_coh_s / med_coh_t,
             med_m_t, med_m_s, med_m_s / med_m_t))
    medC_s = med([abs(r["dv"]) / r["sabs"] for r in s_ok
                  if r["sabs"] > 0.0])
    medC_t = med([abs(r["dv"]) / r["sabs"] for r in neg
                  if r["sabs"] > 0.0])
    print("    cancellation factor C = |delta_v|/S_abs (SPEC "
          "v2(b), report): truth med %.4f vs smooth med %.4f "
          "(ratio %.2f)" % (medC_t, medC_s, medC_s / medC_t))
    differs = []
    for nm, a, b in (("COHERENCE", med_coh_t, med_coh_s),
                     ("DENSITY", med_m_t, med_m_s)):
        if np.isfinite(a) and np.isfinite(b) and a > 0:
            rat = b / a
            if rat >= FACT2 or rat <= 1.0 / FACT2:
                differs.append(nm)
    smooth_label = ("SMOOTH-DIFFERS(%s)" % ",".join(differs)
                    if differs else "SMOOTH-SIMILAR")
    check("C3 typed: %s (factor-of-2 rule on the ladder medians)"
          % smooth_label, True)
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

    return finish(dict(tr=tr_label, dens=dens_label,
                       align=align_label, bound=bound_label,
                       smooth=smooth_label, min_ratio=min_ratio,
                       med_coh=med_coh_t, med_al=med_al,
                       medC=medC, medM=medM, medT=medT,
                       tr_corr=tr_corr))


def finish(lab):
    section("V -- FROZEN VERDICT")
    n_pass = sum(1 for _n, okk in CHECKS if okk)
    n_tot = len(CHECKS)
    if KILLS:
        VERDICT = {"K1": "PIPELINE-BROKEN",
                   "KW": "WARD-BROKEN"}[KILLS[0]]
        print("\n  VERDICT: %s" % VERDICT)
    else:
        VERDICT = ("RATIOSOURCE-MEASURED / %(tr)s / %(dens)s / "
                   "%(align)s / %(bound)s / %(smooth)s" % lab)
        print("\n  VERDICT: %s" % VERDICT)
        print("  (median coherence %(med_coh).4f; density "
              "margin min m/|r| %(min_ratio).3f; median align "
              "%(med_al).4f; median log factors C %(medC)+.3f / "
              "M %(medM)+.3f / T %(medT)+.3f; transport corr "
              "%(tr_corr)+.3f)" % lab)
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed"
          % (time.time() - T0, n_tot, n_tot - n_pass))
    return 0 if n_pass == n_tot else 1


if __name__ == "__main__":
    raise SystemExit(main())
