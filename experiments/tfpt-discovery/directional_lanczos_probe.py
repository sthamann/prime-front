#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""directional_lanczos_probe -- PRIME.PORT.DIRECTIONAL.LANCZOS.01
(EXPLORATION ONLY, experiments/; round 63, theorem-engineering on
the RH-side wall: the Stieltjes/moment form of directional defect
correction on the n > q half.  2026-08-11.)

THE QUESTION (frozen).  The Schur load is a Stieltjes integral:
    q = b* B^{-1} b = |b|^2 int (1/lam) d nu(lam),
nu = the spectral measure of B in the direction b (the DIRECTIONAL
measure -- all its moments are the source-only scalars b* B^j b).
Short Lanczos (k steps from b) builds the Jacobi matrix J_k of nu;
for the Stieltjes function 1/lam, classical Gauss/Golub-Meurant
theory gives TWO-SIDED bounds:
    GAUSS      G_k = |b|^2 (J_k^{-1})_{11}          <= q
               (monotone nondecreasing in k, lower bound),
    GAUSS-RADAU with the fixed node at the certified floor
    c_B = 0.5523 (CLIII, the constant this probe may spend):
               R_k = |b|^2 (Jtilde_{k+1}^{-1})_{11}  >= q
               (monotone nonincreasing in k, upper bound),
    Jtilde_{k+1} = [[J_k, beta_k e_k], [beta_k e_k^T, ahat]],
    ahat = c_B + delta_k, (J_k - c_B I) delta = beta_k^2 e_k.
Both are implemented; monotonicity in k and the bracket G_k <= q
<= R_k are WARDS.  DISTINCTION (frozen, stated as instructed):
this is NOT the dead pivot-Radau of round 61 -- that was Radau
quadrature on the WALL'S OWN moment matrix (the wall functional's
measure); this is the directional spectral measure OF B RELATIVE
TO b inside the P2/P3 co-block split, with the node pinned at the
NEW certified floor.  THE QUESTION: the smallest k with
    n - R_k(q) >= (1/2) mu1(h),   mu1(h) = 4 sin^2(pi/(2h+1))
(the CLI frozen comparison target on r2's h, NO-ADJUST upstream)
per step -- the k* ladder over the 39 steps, bounded or not.  If
k* <= 5 uniformly, the wall reduces to finitely many source-only
moments b* B^j b: they are printed explicitly at the median rung
with their head/tail atom anatomy (declared attribution
convention below); if not uniform, the same printout is given as
RECORDED CONTEXT (MOMENTS-CONTEXT, disclosed, no claim).  Also
reported: the Gauss/Radau bracket width (R_k - G_k)/q vs k (the
certification gap of the k-moment reduction).
MATHEMATICAL RELATION TO PROBE 1(iii) (frozen, verified
numerically as a ward): the Radau upper bound IS the optimal
Krylov defect bound given the floor --
    R_k = min over x in K_k(B, b) of
          [ 2 b*x - x*B x + |b - Bx|^2 / c_B ],
so R_k <= the CG defect bound of
directional_defect_correction_probe at the same k (census
printed).  The minimizer is computed in the Lanczos basis (the
projected quadratic uses only J_k, beta_k, |b|, c_B) and compared
to R_k at OPT_WARD relative.

EXACTNESS MODEL (frozen).  Float-level probe on the float64-
computed step matrices; q by direct solve appears ONLY in wards
(bracket, CG tie, grade exactness) -- the BOUNDS themselves use
only the Lanczos recurrence on matvecs with B, |b|, and the spent
constant c_B = 0.5523 (CLIII interval-certified ladder minimum,
declared input; float floor guard lam_min(B) >= c_B is a kill
ward, W6).  NO RH claim.

FROZEN PROTOCOL (pipeline verbatim from
pgram_directional_schur_probe = CL = CXLIV = v900 chain; ONE Gram
per rung; window memoization):

 W   PIPELINE + REPRODUCTION (kill -> PIPELINE-BROKEN /
     WARD-BROKEN): W1 42 rungs, chains complete, tau finite; W2
     >= 30 full-core rungs; W3a truth all-PSD (A, R, S); W3b >=
     20 consecutive full-core steps; W4 REPRODUCTION P2/P3
     ledger: min lam_min(B) == 0.679 (rtol 2e-2), gap min/med ==
     0.052/0.888 (rtol 5e-2); W6 FLOOR CONSUMPTION GUARD: float
     lam_min(B) >= C_B_CERT = 0.5523 on EVERY step.

 E1  THE LANCZOS BRACKET (per step, k = 1..K_MAX = 6; grade
     breakdown at GRADE_BD declared -- values frozen at the grade
     for k > g):  WARDS (kill -> WARD-BROKEN):
     E1.w1 bracket G_k <= q <= R_k on every step and k (one-sided
           float allowance BRK_WARD relative);
     E1.w2 monotonicity: G_k nondecreasing, R_k nonincreasing in
           k (violation <= MONO_WARD relative to q);
     E1.w3 CG TIE: G_k == b* x_k with x_k the k-step CG/Krylov
           minimizer (the classical CG-Gauss identity; CGTIE_WARD
           relative);
     E1.w4 RADAU = OPTIMAL KRYLOV DEFECT BOUND: R_k == min over
           K_k of the floor-defect quadratic (projected form;
           OPT_WARD relative) -- the frozen relation to probe
           1(iii);
     E1.w5 grade exactness: if the recurrence exhausts at grade g
           (beta_g <= GRADE_BD), G_g == q (GRADE_WARD relative).

 E2  THE k* LADDER (the headline): per step k*_pos = min k with
     n - R_k > 0 and k*_half = min k with n - R_k >= mu1/2 (INF
     if not reached by K_MAX); printed ladder; typed
     KSTAR-BOUNDED(max, med, census, OLS slope vs log h) iff
     reached on every step, else KSTAR-NOT-REACHED(count).
     Census R_k vs the probe-1 CG defect bound at the same k
     (R_k <= qup_CG expected on every step/k, counted).
     Bracket-width table: med (R_k - G_k)/q per k.

 E3  THE MOMENT PRINTOUT: at the median step (by h order) print
     the source-only moments m_j = b* B^j b, j = 0..2*kprint
     (kprint = the median k*_half, capped at K_MAX), and the
     declared atom anatomy: in co-frame coordinates the moment
     splits as m_j = sum_i (b)_i (B^j b)_i; each co-frame
     coordinate i is attributed to the core folds a in CORE_J by
     the frame weights Q[a, 1+i]^2 (rows of the Householder
     frame; sums to 1 per coordinate) -- printed as the 8-fold
     share table (which atoms carry each moment; the connection
     to the O(1)-head result CXLVII is descriptive context).
     Typed MOMENTS-REDUCED iff k*_half <= 5 on all steps (the
     wall on this surface reduces to <= 11 source-only moments +
     the floor), else MOMENTS-CONTEXT (recorded, no claim).

 C   CONTROLS (kill -> WARD-BROKEN if silent): C0 truth neg(A) =
     0 everywhere; C1 smooth world neg(A) > 0 on >= 1 rung; C2
     Epstein x^2+5y^2 comb + scramble (seed 1) at kz 9 fire
     (neg(A) > 0 or frame death); C3 FLOOR REFUSAL in the smooth
     world: float lam_min(B_sm) < c_B on >= REFUSE_MIN usable
     steps -- the Radau node premise (node <= lam_min) is
     unavailable there, the machine refuses.  C4 ILLEGAL-NODE
     CENSUS (recorded, measured, no kill): Radau with the node
     ILLEGALLY placed at 1.05 x lam_min(B) (above the spectrum
     floor -- target data, allowed in a control) loses the
     upper-bound property; the census of steps where the illegal
     R_1 < q is printed (the legality of the node = the certified
     floor is load-bearing).

 S   SCREENS: tau-screen (OLS slope of log margin vs log tau on
     the positive subset, bands PASS |s| <= 0.30 / RELOC >= 0.70
     / AMBIG) of the half-margin n - R_{k*} - mu1/2 at k*_half.

KILLS: K1 pipeline (W1-W3) -> PIPELINE-BROKEN; K2 reproduction /
ward / control failures (W4, W6, E1.w1-w5, C0-C3) ->
WARD-BROKEN.  E2/E3/C4 typed outcomes are measurements, never
kills.

VERDICT (frozen enum): DIRLANCZOS-MEASURED with typed sublabels
BRACKET-WARDED(max devs), KSTAR-BOUNDED(...) /
KSTAR-NOT-REACHED(...), RADAU-IS-KRYLOV-OPT(max rel dev),
RADAU-BEATS-CG(n/N), WIDTH(med at k*), MOMENTS-REDUCED /
MOMENTS-CONTEXT, ILLEGAL-NODE(count), SCREENS(...); else
PIPELINE-BROKEN / WARD-BROKEN.

FROZEN BARS: CORE_J = (2,...,16); H_LADDER_MAX = 900; N_RUNGS_EXP
= 42; MIN_CORE_RUNGS = 30; MIN_STEPS = 20; MINB_REF = 0.679 (rtol
2e-2); GAPMIN_REF = 0.052, GAPMED_REF = 0.888 (rtol 5e-2);
C_B_CERT = 0.5523 (CLIII, declared input); K_MAX = 6; GRADE_BD =
1e-13; BRK_WARD = 1e-9; MONO_WARD = 1e-9; CGTIE_WARD = 1e-8;
OPT_WARD = 1e-7; GRADE_WARD = 1e-9; KRY_BD = 1e-12; REFUSE_MIN =
30; ILLEGAL_FACT = 1.05; SLOPE_PASS = 0.30; SLOPE_RELOC = 0.70;
CTRL_KZ = 9; scramble seed 1; mu1(h) = 4 sin^2(pi/(2h+1)) on r2's
h.  Runtime cap declared: 5 min.

ANTI-CIRCULARITY (frozen): the bounds use ONLY matvecs with B
from the source vector b (the Lanczos recurrence), |b|, and the
frozen upstream certificate constant c_B; q by direct solve and
float lam_min(B) appear ONLY in wards/guards/controls (decisions,
never constructions); the illegal-node control may use anything
(it is a control).

NO-GO COMPLIANCE (frozen): no rank-1 approximation of the core
update; no plain Herglotz certificate; no fit where an identity
is claimed; the round-61 pivot-Radau no-go does not apply (the
measure here is the directional measure of B relative to b, not
the wall's own moment matrix -- stated above).

SMOKE-RUN DISCLOSURE (2026-08-11, before freezing): one smoke run
of this script (21/21; 3.6 s; identical bars; NO bar, band,
count, rule or enum was moved after it) measured: pipeline +
P2/P3 reproduction green (min lam_min(B) 0.6790, gap
0.0520/0.8875), W6 floor guard 39/39.  THE WARDS ARE EXACT-GRADE:
bracket violation 0.0, monotonicity violation 0.0, CG tie
7.2e-15, grade breakdown on 0/39 steps, and the frozen relation
to probe 1(iii) CONFIRMED NUMERICALLY: Radau == optimal Krylov
defect bound, max rel dev 6.1e-12, with Radau <= the sibling CG
defect bound on 39/39 steps at every k.  THE k* LADDER: k*_half
reached on 37/39 with census {2: 11, 3: 10, 4: 4, 5: 8, 6: 4},
med 3; the SAME two steps as the sibling probe stay INF at K_MAX
= 6 (kz 16/h 434 and kz 24/h 490, half-margins -5.34/-5.34 at k
= 6 -- the optimal bound cuts the sibling CG deficits -2.4e+01/
-1.3e+01 by ~4x but does not close them; k = 7 is exact in the
7-dim co-block, so no bounded-k* theorem on this surface).
Bracket width med (R_k - G_k)/q: 42.7/17.3/5.84/2.72/0.816/0.105
for k = 1..6.  MOMENTS-CONTEXT (k* not uniformly <= 5); the
median-rung printout (kz 16/h 434) shows every fold carrying
O(10-20%) of every moment with the deepest fold 16 the largest
single carrier -- no few-atom concentration.  Controls: C1-C3
fire (floor refusal 35/35); C4 illegal-node census 0/39
undershoots at factor 1.05, k = 1 -- the control is
UNINFORMATIVE at this strength, recorded honestly per the frozen
no-kill rule (no strengthening after the fact).  Fail-first
preserved: nothing was weakened; the verdict rule, bars and
enums are exactly as frozen above.

SPEC v1 (2026-08-11, frozen + SHA-hashed before the frozen run):
everything above.  Mechanical concretizations frozen with v1: (i)
window memoization per (kz, seed); (ii) Householder frame as
P2/CL/CXLIV; (iii) directional Lanczos with double full
reorthogonalization; J_k = tridiag(alpha_1..alpha_k,
beta_1..beta_{k-1}); Radau extension uses beta_k; at grade
(beta_g = 0) the Radau extension appends a zero-weight node at
c_B and R_g = G_g = q (natural limit, declared); (iv) steps
sorted by (h, kz), consecutive full-core pairs with r1 all-PSD,
lamS > 0; (v) OLS population statistics as v900; screens read
positive subsets; (vi) the probe-1 CG defect bound rebuilt
in-file with the identical krylov_iterates machinery (declared
reproduction, not an import).

NO RH claim: a certified half-mu1 margin (had it held) is a
SURFACE statement about the computed step matrices of the
deployed ladder ONLY; the k* ladder and the moment reduction are
measurements; no marker moves.

FIREWALL: no zeros, no prime oracles (AST scan; banned ids
zetazero / nzeros / primerange / isprime / primepi / nextprime /
prevprime); v563 READ-ONLY; RNG only inside the declared scramble
control; stdout only.

Sources (read-only): v563_paper2_readouts; wall + fixed-core
machinery verbatim from pgram_directional_schur_probe (CL) =
bfloor_pg_dominance_probe (CXLIV); c_B = 0.5523 from
pg_chain_interval_rollout_probe (CLIII, declared input); mu1
target from halfgap_registration_probe (CLI, declared input);
sibling probe directional_defect_correction_probe (CLVIII, same
day -- the CG defect route this probe optimizes).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/directional_lanczos_probe.py
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

CORE_J = (2, 4, 6, 8, 10, 12, 14, 16)
H_LADDER_MAX = 900
N_RUNGS_EXP = 42
MIN_CORE_RUNGS = 30
MIN_STEPS = 20
MINB_REF = 0.679
MINB_RTOL = 2e-2
GAPMIN_REF = 0.052
GAPMED_REF = 0.888
GAP_RTOL = 5e-2
C_B_CERT = 0.5523            # CLIII certified ladder min (spent)
K_MAX = 6
GRADE_BD = 1e-13
BRK_WARD = 1e-9
MONO_WARD = 1e-9
CGTIE_WARD = 1e-8
OPT_WARD = 1e-7
GRADE_WARD = 1e-9
KRY_BD = 1e-12
REFUSE_MIN = 30
ILLEGAL_FACT = 1.05
SLOPE_PASS = 0.30
SLOPE_RELOC = 0.70
CTRL_KZ = 9
BANNED_IDS = ("zetazero", "nzeros", "primerange", "isprime",
              "primepi", "nextprime", "prevprime")

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


# --------------- pipeline, verbatim (pgram_directional_schur_probe)
def grid_density(c):
    c = np.asarray(c, float)
    a = np.concatenate([c, c[-2:0:-1]])
    d = np.fft.fft(a)
    assert float(np.max(np.abs(d.imag))) <= 1e-9 * max(
        1.0, float(np.max(np.abs(d.real))))
    return d.real


def cell_widths(uu):
    du = np.zeros(len(uu))
    du[1:-1] = 0.5 * (uu[2:] - uu[:-2])
    du[0] = uu[1] - uu[0]
    du[-1] = uu[-1] - uu[-2]
    return du


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


def lambda_eps(N):
    """Epstein x^2+5y^2 comb (port_schur_reduction verbatim)."""
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


_WIN_CACHE = {}


def window_of(kz, scramble_seed=None):
    key = (kz, scramble_seed)
    if key not in _WIN_CACHE:
        rr = core.build_window(kz, scramble_seed=scramble_seed)
        _WIN_CACHE[key] = dict(
            h=rr["h"], M=rr["M"], D=rr["D"], alpha=rr["alpha"],
            n_atom=rr["n_atom"],
            uu=np.asarray(rr["uu"], float).copy(),
            lam=np.asarray(rr["lam"], float).copy(),
            c_ar=np.asarray(core.arch_lags(rr["M"], rr["D"]),
                            float))
    return _WIN_CACHE[key]


def ladder_zones():
    out = []
    for kz in core.frame_a_zones():
        D_k = 0.5 * float(core.G_ALL[kz]) / float(core.NU_MAIN)
        M_k = int(math.ceil(float(core.U_ALL[kz]) / D_k - 1.0e-9)) + 1
        if M_k % 2:
            M_k += 1
        if M_k // 2 <= H_LADDER_MAX:
            out.append(kz)
    return out


def smooth_masses(uu):
    return 2.0 * np.exp(uu / 2.0) * cell_widths(uu)


def world_smooth(uu, mm, rr):
    return uu, smooth_masses(uu)


def gram_anatomy(kz, world_fn=None, scramble_seed=None, comb=None):
    """v900 verbatim wall + fixed-core split."""
    rr = window_of(kz, scramble_seed=scramble_seed)
    M, D, alpha, h = rr["M"], rr["D"], rr["alpha"], rr["h"]
    uu = rr["uu"]
    mm = 2.0 * rr["lam"]
    if world_fn is not None:
        uu, mm = world_fn(uu, mm, rr)
    if comb is not None:
        uu, mm = comb
    c_at, _ = core.atom_lags_at(alpha, M, uu, mm)
    d = grid_density(rr["c_ar"] + np.asarray(c_at, float))
    L = 2 * M - 2
    xs, ws, _ = folded_measure(d, L, +1.0)
    ys, vs, uf_n = folded_measure(d, L, -1.0)
    al, be, m0, steps = lanczos_chain(xs, ws, h + 1)
    if steps < h + 1 or np.any(be <= 0):
        return None
    Pn = eval_chain(al, be, m0, ys, h)
    G = np.sqrt(vs)[:, None] * (Pn @ Pn.T) * np.sqrt(vs)[None, :]
    G = 0.5 * (G + G.T)
    n = G.shape[0]
    A = np.eye(n) - G
    evA = np.linalg.eigvalsh(A)
    out = dict(kz=kz, h=h, n=n, alpha=float(alpha), M=M, D=D)
    out["tau"] = float(evA[0])
    out["negA"] = int(np.sum(evA < 0.0))
    idx = {int(j): k for k, j in enumerate(uf_n)}
    out["core_ok"] = all(j in idx for j in CORE_J)
    if not out["core_ok"]:
        return out
    ic = np.array([idx[j] for j in CORE_J], dtype=int)
    icset = set(ic.tolist())
    ib = np.array([k for k in range(n) if k not in icset],
                  dtype=int)
    B = A[np.ix_(ic, ic)]
    Xc = A[np.ix_(ic, ib)]
    R = A[np.ix_(ib, ib)]
    evR = np.linalg.eigvalsh(R)
    out["negR"] = int(np.sum(evR < 0.0))
    Z = np.linalg.solve(R, Xc.T)
    Y = Xc @ Z
    Y = 0.5 * (Y + Y.T)
    S = B - Y
    S = 0.5 * (S + S.T)
    evS = np.linalg.eigvalsh(S)
    out["S"] = S
    out["lamS"] = float(evS[0])
    out["negS"] = int(np.sum(evS < 0.0))
    return out


def householder_frame(v):
    n = len(v)
    v = v / float(np.linalg.norm(v))
    e1 = np.zeros(n)
    e1[0] = 1.0
    u = e1 - v
    nu = float(np.linalg.norm(u))
    if nu < 1e-14:
        return np.eye(n)
    u = u / nu
    Q = np.eye(n) - 2.0 * np.outer(u, u)
    if float(Q[:, 0] @ v) < 0:
        Q = -Q
    return Q


def ols_line(x, y):
    x = np.asarray(x, float)
    y = np.asarray(y, float)
    vx = float(np.var(x))
    if vx == 0.0:
        return float(np.mean(y)), 0.0, float("nan")
    b = float(np.cov(x, y, bias=True)[0, 1] / vx)
    a = float(np.mean(y) - b * np.mean(x))
    ss = float(np.sum((y - a - b * x) ** 2))
    st = float(np.sum((y - np.mean(y)) ** 2))
    return a, b, (1.0 - ss / st if st > 0 else float("nan"))


def screen(vals, taus):
    vals = np.asarray(vals, float)
    taus = np.asarray(taus, float)
    pos = vals > 0
    if int(np.sum(pos)) >= 3:
        _a, sl, r2 = ols_line(np.log(taus[pos]), np.log(vals[pos]))
    else:
        return "vacuous(pos=%d)" % int(np.sum(pos)), float("nan")
    lab = ("PASS" if abs(sl) <= SLOPE_PASS
           else "RELOC" if sl >= SLOPE_RELOC else "AMBIG")
    return "%s(slope=%+.3f, R2=%.3f)" % (lab, sl, r2), sl


def mu1_of(h):
    return 4.0 * math.sin(math.pi / (2.0 * h + 1.0)) ** 2


# ------------------------- directional Lanczos + quadrature (new)
def dir_lanczos(B, b, kmax):
    """k-step Lanczos on B from b (double full reorth); returns
    (alphas, betas, beta0, grade) with betas[k-1] = beta_k; grade
    = None if the recurrence survives kmax steps."""
    beta0 = float(np.linalg.norm(b))
    V = [b / beta0]
    alphas, betas = [], []
    grade = None
    for k in range(kmax):
        w = B @ V[k]
        a = float(V[k] @ w)
        alphas.append(a)
        w = w - a * V[k]
        if k > 0:
            w = w - betas[k - 1] * V[k - 1]
        for _ in range(2):
            for u in V:
                w = w - float(u @ w) * u
        bn = float(np.linalg.norm(w))
        if bn <= GRADE_BD:
            betas.append(0.0)
            grade = k + 1
            break
        betas.append(bn)
        V.append(w / bn)
    return alphas, betas, beta0, grade


def jk_of(alphas, betas, k):
    J = np.diag(np.array(alphas[:k], float))
    if k > 1:
        off = np.array(betas[:k - 1], float)
        J += np.diag(off, 1) + np.diag(off, -1)
    return J


def gauss_lower(alphas, betas, beta0, k):
    J = jk_of(alphas, betas, k)
    e1 = np.zeros(k)
    e1[0] = 1.0
    return beta0 * beta0 * float(np.linalg.solve(J, e1)[0])


def radau_upper(alphas, betas, beta0, k, node):
    """Gauss-Radau with prescribed node (Golub-Meurant)."""
    J = jk_of(alphas, betas, k)
    bk = float(betas[k - 1])
    ek = np.zeros(k)
    ek[-1] = 1.0
    if bk == 0.0:                      # grade: zero-weight node
        ahat = node
    else:
        delta = np.linalg.solve(J - node * np.eye(k),
                                bk * bk * ek)
        ahat = node + float(delta[-1])
    Jt = np.zeros((k + 1, k + 1))
    Jt[:k, :k] = J
    Jt[k, k] = ahat
    Jt[k - 1, k] = Jt[k, k - 1] = bk
    e1 = np.zeros(k + 1)
    e1[0] = 1.0
    return beta0 * beta0 * float(np.linalg.solve(Jt, e1)[0])


def krylov_opt_defect(alphas, betas, beta0, k, node):
    """min over K_k of 2b*x - x*Bx + |b - Bx|^2/node, in the
    Lanczos basis (projected: only J_k, beta_k, beta0, node)."""
    J = jk_of(alphas, betas, k)
    bk = float(betas[k - 1])
    ek = np.zeros(k)
    ek[-1] = 1.0
    J2 = J @ J + (bk * bk) * np.outer(ek, ek)
    e1 = np.zeros(k)
    e1[0] = 1.0
    H = J2 / node - J
    rhs = (beta0 / node) * (J @ e1) - beta0 * e1
    y = np.linalg.solve(H, rhs)
    return (2.0 * beta0 * y[0] - float(y @ (J @ y))
            + (beta0 * beta0 - 2.0 * beta0 * float((J @ y)[0])
               + float(y @ (J2 @ y))) / node)


def krylov_iterates(b, B, kmax):
    """probe-1 CG-equivalent Krylov minimizers (declared
    reproduction)."""
    V = []
    v = b.copy()
    n0 = float(np.linalg.norm(v))
    xs = []
    for k in range(kmax):
        nv = float(np.linalg.norm(v))
        if nv <= KRY_BD * max(n0, 1e-300):
            break
        v = v / nv
        for _ in range(2):
            for u in V:
                v = v - float(u @ v) * u
        nv2 = float(np.linalg.norm(v))
        if nv2 <= KRY_BD:
            break
        V.append(v / nv2)
        Vm = np.array(V).T
        Bp = Vm.T @ B @ Vm
        Bp = 0.5 * (Bp + Bp.T)
        y = np.linalg.solve(Bp, Vm.T @ b)
        xs.append(Vm @ y)
        v = B @ V[-1]
    while len(xs) < kmax:
        xs.append(xs[-1].copy())
    return xs


def main():
    section("PRIME.PORT.DIRECTIONAL.LANCZOS.01 -- Gauss/Gauss-"
            "Radau brackets of the Schur load q from the "
            "directional measure of B along b; Radau node pinned "
            "at the certified floor c_B = %.4f (EXPLORATION "
            "ONLY)" % C_B_CERT)
    print("    FROZEN_SPEC SHA-256 = %s"
          % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
    print("    NO RH claim; no marker moves.  NOT the round-61 "
          "pivot-Radau (that was the wall's own moment matrix); "
          "this is the directional spectral measure of B "
          "relative to b.")
    print("\nS0 -- firewall")
    check("S0.1 AST firewall clean", not ast_scan(BANNED_IDS))

    # ------------------------------------------------------------ W
    section("W -- the truth ladder + P2/P3 reproduction + the "
            "floor-consumption guard")
    zones = ladder_zones()
    check("W1 frozen rung count %d" % N_RUNGS_EXP,
          len(zones) == N_RUNGS_EXP, "found %d" % len(zones),
          kill="K1")
    truth = []
    sm_map = {}
    for kz in zones:
        r = gram_anatomy(kz)
        if r is None:
            print("    kz %-3d: CHAIN SHORT" % kz, flush=True)
            truth.append(None)
            continue
        truth.append(r)
        rs = gram_anatomy(kz, world_fn=world_smooth)
        if isinstance(rs, dict):
            sm_map[kz] = rs
    ok_chain = all(r is not None for r in truth)
    check("W1b all chains complete", ok_chain, kill="K1")
    if not ok_chain:
        return finish({})
    truth.sort(key=lambda r: (r["h"], r["kz"]))
    check("W1c all tau finite",
          all(np.isfinite(r["tau"]) for r in truth), kill="K1")
    full = [r for r in truth if r["core_ok"]]
    check("W2 >= %d full-core rungs" % MIN_CORE_RUNGS,
          len(full) >= MIN_CORE_RUNGS,
          "%d full-core rungs" % len(full), kill="K1")
    ok_psd = all(r["negA"] == 0 and r["negR"] == 0
                 and r["negS"] == 0 for r in full)
    check("W3a WARD truth all-PSD (A, R, S)", ok_psd, kill="K1")
    steps = []
    for r1, r2 in zip(truth, truth[1:]):
        if not (r1.get("core_ok") and r2.get("core_ok")):
            continue
        if r1["lamS"] <= 0.0 or r1["negA"] > 0:
            continue
        steps.append((r1, r2))
    check("W3b >= %d consecutive full-core steps" % MIN_STEPS,
          len(steps) >= MIN_STEPS, "%d steps" % len(steps),
          kill="K1")
    print("    h range %d..%d  [%.1f s]"
          % (truth[0]["h"], truth[-1]["h"], time.time() - T0))
    if KILLS:
        return finish({})
    rows = []
    for r1, r2 in steps:
        wS, VS = np.linalg.eigh(r1["S"])
        Q = householder_frame(VS[:, 0])
        Mt = Q.T @ (r2["S"] / r1["tau"]) @ Q
        Mt = 0.5 * (Mt + Mt.T)
        nsc = float(Mt[0, 0])
        b = Mt[1:, 0].copy()
        B = Mt[1:, 1:].copy()
        minB = float(np.linalg.eigvalsh(B)[0])
        q = float(b @ np.linalg.solve(B, b))
        rs2 = sm_map.get(r2["kz"])
        Bsm = None
        if isinstance(rs2, dict) and "S" in rs2:
            M0 = Q.T @ (rs2["S"] / r1["tau"]) @ Q
            M0 = 0.5 * (M0 + M0.T)
            Bsm = M0[1:, 1:].copy()
        rows.append(dict(r1=r1, r2=r2, Q=Q, B=B, b=b, nsc=nsc,
                         q=q, gap=nsc - q, minB=minB, Bsm=Bsm,
                         tau=r1["tau"], mu1=mu1_of(r2["h"])))
    minB_all = float(np.min([w["minB"] for w in rows]))
    gaps = np.array([w["gap"] for w in rows])
    gmin, gmed = float(np.min(gaps)), float(np.median(gaps))
    ok_repro = (abs(minB_all / MINB_REF - 1.0) <= MINB_RTOL
                and abs(gmin / GAPMIN_REF - 1.0) <= GAP_RTOL
                and abs(gmed / GAPMED_REF - 1.0) <= GAP_RTOL)
    check("W4 REPRODUCTION P2/P3 ledger: min lam_min(B) %.4f == "
          "%.3f; gap min/med %.4f/%.4f == %.3f/%.3f"
          % (minB_all, MINB_REF, gmin, gmed, GAPMIN_REF,
             GAPMED_REF), ok_repro, kill="K2")
    check("W6 FLOOR CONSUMPTION GUARD: float lam_min(B) = %.4f "
          ">= C_B_CERT = %.4f on %d/%d steps"
          % (minB_all, C_B_CERT,
             sum(1 for w in rows if w["minB"] >= C_B_CERT),
             len(rows)),
          all(w["minB"] >= C_B_CERT for w in rows), kill="K2")
    if KILLS:
        return finish({})

    # ----------------------------------------------------------- E1
    section("E1 -- the Lanczos bracket: Gauss lower / Radau upper "
            "(node at c_B), k = 1..%d" % K_MAX)
    dev_brk = dev_mono = dev_tie = dev_opt = dev_grade = 0.0
    n_grade = 0
    for w in rows:
        al, be, b0, grade = dir_lanczos(w["B"], w["b"], K_MAX)
        keff = len(al)
        G_l, R_l, O_l = [], [], []
        for k in range(1, keff + 1):
            G_l.append(gauss_lower(al, be, b0, k))
            R_l.append(radau_upper(al, be, b0, k, C_B_CERT))
            O_l.append(krylov_opt_defect(al, be, b0, k,
                                         C_B_CERT))
        while len(G_l) < K_MAX:            # frozen at grade
            G_l.append(G_l[-1])
            R_l.append(R_l[-1])
            O_l.append(O_l[-1])
        q = w["q"]
        for k in range(K_MAX):
            dev_brk = max(dev_brk,
                          (G_l[k] - q) / max(abs(q), 1e-300),
                          (q - R_l[k]) / max(abs(q), 1e-300))
            dev_opt = max(dev_opt, abs(R_l[k] - O_l[k])
                          / max(abs(R_l[k]), 1e-300))
        for k in range(1, K_MAX):
            dev_mono = max(dev_mono,
                           (G_l[k - 1] - G_l[k])
                           / max(abs(q), 1e-300),
                           (R_l[k] - R_l[k - 1])
                           / max(abs(q), 1e-300))
        xs = krylov_iterates(w["b"], w["B"], K_MAX)
        cg_bounds = []
        for k in range(K_MAX):
            xk = xs[k]
            rv = w["b"] - w["B"] @ xk
            cg_bounds.append(2.0 * float(w["b"] @ xk)
                             - float(xk @ (w["B"] @ xk))
                             + float(rv @ rv) / C_B_CERT)
            gk = float(w["b"] @ xk)
            kk = min(k, keff - 1)
            dev_tie = max(dev_tie, abs(G_l[kk] - gk)
                          / max(abs(gk), 1e-300))
        if grade is not None:
            n_grade += 1
            dev_grade = max(dev_grade,
                            abs(G_l[grade - 1] - q)
                            / max(abs(q), 1e-300))
        w["G"], w["R"], w["cg"] = G_l, R_l, cg_bounds
    check("E1.w1 WARD bracket G_k <= q <= R_k: max one-sided "
          "violation %.2e <= %.0e" % (max(dev_brk, 0.0),
                                      BRK_WARD),
          dev_brk <= BRK_WARD, kill="K2")
    check("E1.w2 WARD monotonicity (G up, R down): max violation "
          "%.2e <= %.0e" % (max(dev_mono, 0.0), MONO_WARD),
          dev_mono <= MONO_WARD, kill="K2")
    check("E1.w3 WARD CG tie G_k == b*x_k: max rel dev %.2e <= "
          "%.0e" % (dev_tie, CGTIE_WARD), dev_tie <= CGTIE_WARD,
          kill="K2")
    check("E1.w4 WARD Radau == optimal Krylov defect bound "
          "(projected min): max rel dev %.2e <= %.0e"
          % (dev_opt, OPT_WARD), dev_opt <= OPT_WARD, kill="K2")
    check("E1.w5 WARD grade exactness G_g == q on %d graded "
          "steps: max rel dev %.2e <= %.0e"
          % (n_grade, dev_grade, GRADE_WARD),
          dev_grade <= GRADE_WARD, kill="K2")
    if KILLS:
        return finish({})

    # ----------------------------------------------------------- E2
    section("E2 -- the k* ladder (n - R_k >= mu1/2) + bracket "
            "width + Radau-vs-CG census")
    print("      kz    h    k*_pos  k*_half  half-marg@k*   "
          "width@k*    R<=CG(all k)")
    khalf_l, hs, n_nr = [], [], 0
    hm_at = []
    n_rcg_all = 0
    for w in rows:
        kpos = next((k + 1 for k in range(K_MAX)
                     if w["nsc"] - w["R"][k] > 0.0), None)
        khalf = next((k + 1 for k in range(K_MAX)
                      if w["nsc"] - w["R"][k]
                      >= 0.5 * w["mu1"]), None)
        if khalf is None:
            n_nr += 1
        kk = (khalf or K_MAX) - 1
        hm = w["nsc"] - w["R"][kk] - 0.5 * w["mu1"]
        hm_at.append(hm)
        khalf_l.append(khalf)
        hs.append(w["r2"]["h"])
        wid = (w["R"][kk] - w["G"][kk]) / max(abs(w["q"]),
                                              1e-300)
        rcg = all(w["R"][k] <= w["cg"][k]
                  * (1.0 + 1e-12) + 1e-12 for k in range(K_MAX))
        n_rcg_all += int(rcg)
        print("    %4d %5d     %s      %s      %+9.3e    "
              "%9.3e     %s"
              % (w["r2"]["kz"], w["r2"]["h"],
                 str(kpos) if kpos else "INF",
                 str(khalf) if khalf else "INF", hm, wid,
                 "yes" if rcg else "NO"), flush=True)
    if n_nr == 0:
        kh = np.array([float(k) for k in khalf_l])
        _a, slk, r2k = ols_line(np.log(np.array(hs, float)), kh)
        cen = {int(v): int(np.sum(kh == v))
               for v in sorted(set(kh.tolist()))}
        kstar_lab = ("KSTAR-BOUNDED(max=%d, med=%.1f, census %s, "
                     "slope vs log h %+.3f R2 %.2f)"
                     % (int(kh.max()), float(np.median(kh)), cen,
                        slk, r2k))
    else:
        kstar_lab = "KSTAR-NOT-REACHED(%d of %d)" % (n_nr,
                                                     len(rows))
    print("\n    bracket width med (R_k - G_k)/q per k: %s"
          % ", ".join("k=%d: %.3e"
                      % (k + 1, float(np.median(
                          [(w["R"][k] - w["G"][k])
                           / max(abs(w["q"]), 1e-300)
                           for w in rows])))
                      for k in range(K_MAX)))
    scr_l, _ = screen(hm_at, [w["tau"] for w in rows])
    check("E2 typed: %s; Radau <= CG defect bound on %d/%d "
          "steps (all k); half-margin@k* screen %s"
          % (kstar_lab, n_rcg_all, len(rows), scr_l), True)

    # ----------------------------------------------------------- E3
    section("E3 -- the moment printout at the median rung")
    kh_arr = [k for k in khalf_l if k is not None]
    reduced = (n_nr == 0 and max(kh_arr) <= 5)
    kprint = int(min(np.median(kh_arr) if kh_arr else K_MAX,
                     K_MAX))
    wmed = rows[len(rows) // 2]
    print("    median step kz %d h %d (k*_half here: %s); "
          "moments m_j = b*B^j b, j = 0..%d:"
          % (wmed["r2"]["kz"], wmed["r2"]["h"],
             str(khalf_l[len(rows) // 2]), 2 * kprint))
    Bj = wmed["b"].copy()
    Qf = wmed["Q"]
    for j in range(2 * kprint + 1):
        if j > 0:
            Bj = wmed["B"] @ Bj
        mj = float(wmed["b"] @ Bj)
        pi_ = wmed["b"] * Bj
        shares = np.zeros(len(CORE_J))
        for i in range(len(pi_)):
            shares += pi_[i] * (Qf[:, 1 + i] ** 2)
        stxt = ", ".join("%d: %+.2e" % (a, s)
                         for a, s in zip(CORE_J, shares))
        print("      m_%d = %+.6e   [fold shares: %s]"
              % (j, mj, stxt), flush=True)
    print("    (declared attribution: m_j = sum_i (b)_i "
          "(B^j b)_i in co-frame coordinates, coordinate i "
          "attributed to fold a by Q[a, 1+i]^2; the head/tail "
          "reading -- which folds carry each moment -- is "
          "context for the CXLVII O(1)-head result, no claim.)")
    mom_lab = ("MOMENTS-REDUCED(k* <= 5 on 39/39: the surface "
               "wall reduces to <= 11 source-only moments + the "
               "floor)" if reduced else
               "MOMENTS-CONTEXT(k* not uniformly <= 5; printout "
               "recorded, no claim)")
    check("E3 typed: %s" % mom_lab, True)

    # ------------------------------------------------------------ C
    section("C -- controls")
    check("C0.1 WARD truth wall holds (neg(A) = 0 on all rungs)",
          all(r["negA"] == 0 for r in truth), kill="K2")
    n_viol = sum(1 for kz in zones
                 if isinstance(sm_map.get(kz), dict)
                 and sm_map[kz]["negA"] > 0)
    check("C1 WARD smooth world violates (neg(A) > 0 on %d rungs)"
          % n_viol, n_viol > 0, kill="K2")
    rr9 = window_of(CTRL_KZ)
    N_E = int(math.floor(math.exp(2.0 * rr9["alpha"]))) + 1
    lamE_ = lambda_eps(N_E)
    nn = np.nonzero(np.abs(lamE_) > 1e-12)[0]
    ctl = {"Epstein": gram_anatomy(
               CTRL_KZ, comb=(np.log(nn.astype(float)),
                              2.0 * lamE_[nn]
                              / np.sqrt(nn.astype(float)))),
           "scramble": gram_anatomy(CTRL_KZ, scramble_seed=1)}
    fired_all = True
    for name, r in ctl.items():
        if not isinstance(r, dict):
            print("    %-9s: chain dies -> fires" % name)
            continue
        f = r["negA"] > 0
        fired_all &= f
        print("    %-9s: tau %+.3e  neg(A) %d -> %s"
              % (name, r["tau"], r["negA"],
                 "FIRES" if f else "SILENT"), flush=True)
    check("C2.1 WARD both controls fire", fired_all, kill="K2")
    n_ref, n_use = 0, 0
    for w in rows:
        if w["Bsm"] is None:
            continue
        n_use += 1
        if float(np.linalg.eigvalsh(w["Bsm"])[0]) < C_B_CERT:
            n_ref += 1
    check("C3 WARD FLOOR REFUSAL in the smooth world: lam_min("
          "B_sm) < c_B on %d/%d usable steps (>= %d) -- the "
          "Radau node premise dies there, the machine refuses"
          % (n_ref, n_use, REFUSE_MIN), n_ref >= REFUSE_MIN,
          kill="K2")
    n_ill = 0
    for w in rows:
        al, be, b0, _g = dir_lanczos(w["B"], w["b"], 1)
        r1_ill = radau_upper(al, be, b0, 1,
                             ILLEGAL_FACT * w["minB"])
        if r1_ill < w["q"]:
            n_ill += 1
    check("C4 ILLEGAL-NODE census (recorded, measured): Radau "
          "with the node at %.2f x lam_min(B) UNDERSHOOTS q on "
          "%d/%d steps -- the legality of the node (the "
          "certified floor) is load-bearing"
          % (ILLEGAL_FACT, n_ill, len(rows)), True)

    labels = dict(
        brk="BRACKET-WARDED(brk %.1e, mono %.1e)" % (dev_brk,
                                                     dev_mono),
        kstar=kstar_lab,
        opt="RADAU-IS-KRYLOV-OPT(%.1e)" % dev_opt,
        rcg="RADAU-BEATS-CG(%d/%d)" % (n_rcg_all, len(rows)),
        mom=mom_lab.split("(")[0],
        ill="ILLEGAL-NODE(%d/%d)" % (n_ill, len(rows)),
        scr="SCREENS(%s)" % scr_l)
    return finish(labels)


def finish(labels):
    section("V -- FROZEN VERDICT")
    n_pass = sum(1 for _n, okk in CHECKS if okk)
    n_tot = len(CHECKS)
    if KILLS:
        VERDICT = {"K1": "PIPELINE-BROKEN",
                   "K2": "WARD-BROKEN"}[KILLS[0]]
        print("\n  VERDICT: %s" % VERDICT)
    else:
        VERDICT = ("DIRLANCZOS-MEASURED / %s / %s / %s / %s / %s "
                   "/ %s / %s"
                   % (labels.get("brk", "-"),
                      labels.get("kstar", "-"),
                      labels.get("opt", "-"),
                      labels.get("rcg", "-"),
                      labels.get("mom", "-"),
                      labels.get("ill", "-"),
                      labels.get("scr", "-")))
        print("\n  VERDICT: %s" % VERDICT)
    print("""
  HONEST FRAME (as frozen): float-level probe on the float64-
  computed step matrices; the spent constant c_B = 0.5523 is the
  CLIII interval-certified ladder minimum over the ideal objects
  on the deployed 39-step surface.  The Gauss/Radau bracket, the
  k* ladder and the moment reduction are SURFACE measurements;
  they prove neither h-uniformity nor any tail statement.  NO RH
  claim.  No marker moves.""")
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed"
          % (time.time() - T0, n_tot, n_tot - n_pass))
    return 0 if n_pass == n_tot else 1


if __name__ == "__main__":
    raise SystemExit(main())
