#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""directional_defect_correction_probe --
PRIME.PORT.DIRECTIONAL.DEFECT.01
(EXPLORATION ONLY, experiments/; round 63, theorem-engineering on
the RH-side wall: directional defect correction on the n > q half
-- approximate ONLY the one needed solution vector x* = B^{-1} b
and pay the error with the newly certified B-floor.  2026-08-11.)

THE QUESTION (frozen).  P2/P3 split the wall update into (B_h PD)
AND (n_h > q_h) with q = b* B^{-1} b in the frozen Householder
frame (gap n - q min/med 0.052/0.888 on 39/39).  CL measured the
directional Loewner route DEAD (OUTCOME-C: replacing ALL of B^{-1}
by D^{-1} with the floor model D = 1/2 P_G + c_dom I loses qbar/q
med 91.3, max 408).  THE LESSON: never replace all of B^{-1};
model only x* and control the residual.  CLIII certified the floor
    B >= c_B I  with  c_B = 0.5523
(interval rollout, v897 class, 39/39 over the ideal objects) --
THE CONSTANT THIS PROBE IS ALLOWED TO SPEND.  The EXACT identity
(for ANY x0; verified as a ward on every step, machine precision):
    q = 2 b*x0 - x0*B x0 + r* B^{-1} r,      r = b - B x0,
so with the certified floor
    q <= qup(x0) := 2 b*x0 - x0*B x0 + |r|^2 / c_B,
and the SOURCE-ONLY sufficient inequality for the wall is
    n - 2 b*x0 + x0*B x0 - |r|^2/c_B > 0,
with the target-grade version  ... >= (1/2) mu1(h),  mu1(h) =
4 sin^2(pi/(2h+1)) on r2's h (the CLI frozen comparison target,
NO-ADJUST clause upstream; h-convention as the CL deltahat).
Evaluating qup(x0) needs NO inverse of B: only matvecs with B and
the spent floor constant.  THREE FROZEN x0 CANDIDATES, in this
order:
 (i)   TRANSPORTED PREVIOUS-STEP SOLUTION: x0 = E_h x_{prev},
       x_{prev} = B_{prev}^{-1} b_{prev} the PREVIOUS step's true
       solution -- legitimate for a RECURSIVE architecture (the
       ladder is consumed step by step; only the new tail enters
       the residual).  DECLARED TRANSPORT E_h: identity on the
       co-frame coordinates (the 7-dim co-block frame is indexed
       by the FIXED fold set CORE_J minus the soft direction on
       every step -- index embedding, no interpolation needed;
       dims are equal on all steps).  First step has no
       predecessor: declared skip, 38 of 39 evaluable.
 (ii)  PRIME-FREE CLASSICAL SOLUTION: x0 = B_sm^{-1} b_sm from
       the smooth model's co-block system ((n_sm, b_sm, B_sm) =
       corner/edge/co-block of M0 = Q^T (S_sm(r2)/tau(r1)) Q in
       the TRUE frame Q, as the CL C3 build; x0 is invariant
       under the common tau scaling).  KNOWN FACT handled: the
       prime-free B_sm need NOT be PD (CL: exact LDL refuses
       35/35) -- the linear solve is still well-defined while
       B_sm is numerically nonsingular (cond <= SM_COND_MAX); the
       non-PD census is printed per step; if a step's B_sm is
       singular/ill-conditioned the DECLARED FALLBACK is the
       positive completed model (eigenvalue clip of B_sm at
       +SM_CLIP; smooth-model spectral data is classical,
       prime-free -- no target data), used_fallback counted and
       said so.  The residual then MEASURES the arithmetic
       deviation.
 (iii) SHORT KRYLOV: x0_k = argmin of the natural quadratic
       phi(x) = x*Bx - 2 b*x over span{b, Bb, ..., B^{k-1} b},
       k = 1..6 (= the CG iterates) -- all source-only: matrix-
       vector products only, NO inverse of B, NO eigensolve of B
       (the k x k projected solve is on the Krylov-projected
       matrix, not on B).  Grade breakdown (basis exhausts at
       grade g < k) is declared: x0_k = x0_g for k > g.
       THE HEADLINE: the minimal k per step achieving (a) bound
       positivity and (b) the (1/2) mu1 target -- the k* ladder
       over all 39 steps, and is k* bounded in h.
For EVERY candidate and step: the exact identity ward, |r|, the
bound margin n - qup, the half-mu1 margin, the bound-vs-truth
preserved fraction (n - qup)/(n - q), the overhead qup - q, the
improvement factor over the dead Loewner route (qbar - q)/(qup -
q) on the SAME step (the table that showed 91x must now show the
improvement), and tau-screens of the certified margins.

DEEP SPOT-CHECK (frozen a priori, not outcome-dependent): the
extended 4e6-table machinery (deep_blind_holdout_probe, CLIV) is
rebuilt verbatim (byte-exact overlap ward); the DEEP_TAKE = 4
shallowest new rungs (ATOM_MAX < X <= TAB_EXT, h in H_HOLD =
[128, 2900]) give up to 3 deep steps; on them candidates (iii)
(the a-priori headline) and (i) (transport across the deep
consecutive steps) are scored with the SAME spent constant c_B =
0.5523.  HONESTY: at depth c_B is a HYPOTHESIS, not a certificate
(the CLIII interval band ends at h ~ 900); the float floor guard
lam_min(B_deep) >= c_B is measured per deep step and a failing
step REFUSES the spend (typed DEEP-REFUSED, never silently
scored).  FLOAT LEVEL DECLARED at depth (CLIV pattern).

EXACTNESS MODEL (frozen).  Float-level probe on the float64-
computed step matrices; the identity ward q = 2b*x0 - x0*Bx0 +
r*B^{-1}r is verified to ID_WARD relative on every step and
candidate (the ward may use solve(B, r): a ward verifies an
identity, the BOUND itself never touches B^{-1}).  The spent
constant c_B = 0.5523 is the CLIII interval-certified ladder
minimum over the ideal objects (declared input); the float floor
guard lam_min(B) >= c_B is a kill ward on the deployed surface
(W6).  NO RH claim.

FROZEN PROTOCOL (pipeline verbatim from
pgram_directional_schur_probe = CL = CXLIV = v900 chain; ONE Gram
per rung; window memoization):

 W   PIPELINE + REPRODUCTION (kill -> PIPELINE-BROKEN /
     WARD-BROKEN): W1 42 rungs, chains complete, tau finite; W2
     >= 30 full-core rungs; W3a truth all-PSD (A, R, S); W3b >=
     20 consecutive full-core steps; W4 REPRODUCTION P2/P3
     ledger: min lam_min(B) == 0.679 (rtol 2e-2), gap min/med ==
     0.052/0.888 (rtol 5e-2), raw-B certified disaster (best
     bound < 0 on every step); W5 REPRODUCTION CXLIV V4: P_G PD
     on every step (float, PG_TOL) and float dominance
     negidx(B - 1/2 P_G) = 0 on >= DOMHALF_MIN steps; W6 FLOOR
     CONSUMPTION GUARD: float lam_min(B) >= C_B_CERT = 0.5523 on
     EVERY step (the spent certified constant sits below the
     measured floor everywhere -- else the spend is dishonest).

 E1  LOEWNER BASELINE (float rebuild of the CL ladder): per step
     c_dom_f = lam_min(B - 1/2 P_G) (float), D = 1/2 P_G +
     c_dom_f I, qbar = b* D^{-1} b; WARD (kill -> WARD-BROKEN):
     median qbar/q == LOEW_MED_REF = 91.3 (rtol 5e-2) -- the CL
     printed ledger, reproduced before any improvement is
     claimed.

 E2  THE THREE CANDIDATES (per candidate: full 39-step table
     printed -- |r|, qup, bound margin bm = n - qup, half-margin
     bm - mu1/2, preserved fraction (n - qup)/(n - q), overhead
     qup - q, improvement (qbar - q)/(qup - q)):
     WARDS per candidate/step (kill -> WARD-BROKEN): E2.w1 exact
     identity |q - (2b*x0 - x0*Bx0 + r*B^{-1}r)| <= ID_WARD
     relative; E2.w2 qup >= q - UPB_WARD*|q| (one-sided float
     allowance; algebraically guaranteed by W6).
     TYPED per candidate (frozen): TARGET-CERTIFIED(n/N, min
     half-margin) iff bm >= mu1/2 on ALL evaluable steps /
     POSITIVE-ONLY(n/N) iff bm > 0 on all evaluable steps but
     the target fails somewhere / FAILS(k of N) otherwise.
     Candidate (iii) is typed at each k and carries E3.

 E3  THE k* LADDERS (candidate iii; the headline): per step
     k*_pos = min k with bm_k > 0 and k*_half = min k with bm_k
     >= mu1/2 (INF if not reached by K_MAX = 6); printed ladder;
     typed KSTAR-BOUNDED(max, med, OLS slope of k*_half vs log
     h) iff k*_half reached on every step, else
     KSTAR-NOT-REACHED(count).  Also the improvement-factor
     ladder at k*_half vs the Loewner baseline.

 D   DEEP SPOT-CHECK (typed, never kill except fidelity): D.w1
     extended-table overlap byte-exact (lam_ext[:ATOM_MAX+1] ==
     core.LAM_TAB, max abs dev == 0.0) + prefix arrays bitwise
     (kill -> WARD-BROKEN if broken); census of the DEEP_TAKE
     shallowest new rungs printed; per deep step: float floor
     guard lam_min(B) >= c_B (fails -> DEEP-REFUSED(step),
     no spend), candidate (iii) k*_pos/k*_half ladder and
     candidate (i) transport row where a predecessor deep step
     exists; typed DEEP-KSTAR(list) / DEEP-REFUSED(k) /
     DEEP-SHORT(reason) -- all measured.  SMOKE mode
     (DDC_SMOKE=1) takes 2 rungs / 1 step, disclosed.

 C   CONTROLS (kill -> WARD-BROKEN if silent): C0 truth neg(A) =
     0 everywhere; C1 smooth world neg(A) > 0 on >= 1 rung; C2
     Epstein x^2+5y^2 comb + scramble (seed 1) at kz 9 fire
     (neg(A) > 0 or frame death); C3 FLOOR REFUSAL in the smooth
     world: float lam_min(B_sm) < c_B on >= REFUSE_MIN usable
     steps -- the certified-floor spend is UNAVAILABLE there,
     the machine must refuse (mirrors the CL exact-LDL refusal
     35/35); C4 BAD-x0 CONTROL (declared RNG, seed BADX0_SEED,
     the ONLY other RNG site): x0 = t* g with g a seeded Gaussian
     direction and t* = (b*g)/(g*B g) the OPTIMAL 1-d scaling --
     the same bookkeeping with a random direction must reproduce
     ~the Loewner disaster: the half-mu1 target must FAIL on >=
     BADX0_FAIL_MIN = 30 of the 39 steps (else the route's power
     would be bookkeeping, not x0 quality); its overhead ladder
     is printed next to the Loewner 91x.

KILLS: K1 pipeline (W1-W3) -> PIPELINE-BROKEN; K2 reproduction /
ward / control failures (W4-W6, E1, E2.w1-w2, D.w1, C0-C4) ->
WARD-BROKEN.  All E2/E3/D typed outcomes are measurements, never
kills.

VERDICT (frozen enum): DIRDEFECT-MEASURED with typed sublabels
TRANSPORT(...), CLASSICAL(...), KRYLOV(...), KSTAR-BOUNDED(...) /
KSTAR-NOT-REACHED(...), IMPROVEMENT(med factor at k*_half),
DEEP-KSTAR(...) / DEEP-REFUSED / DEEP-SHORT, SCREENS(...); else
PIPELINE-BROKEN / WARD-BROKEN.

FROZEN BARS: CORE_J = (2,...,16); H_LADDER_MAX = 900; N_RUNGS_EXP
= 42; MIN_CORE_RUNGS = 30; MIN_STEPS = 20; MINB_REF = 0.679 (rtol
2e-2); GAPMIN_REF = 0.052, GAPMED_REF = 0.888 (rtol 5e-2); PG_TOL
= 1e-12; DOMHALF_MIN = 37; C_B_CERT = 0.5523 (CLIII certified
ladder min, declared input); LOEW_MED_REF = 91.3 (rtol 5e-2);
ID_WARD = 1e-9; UPB_WARD = 1e-9; K_MAX = 6; KRY_BD = 1e-12 (grade
breakdown); SM_COND_MAX = 1e12; SM_CLIP = 1e-8; REFUSE_MIN = 30;
BADX0_SEED = 20260811; BADX0_FAIL_MIN = 30; SLOPE_PASS = 0.30;
SLOPE_RELOC = 0.70; CTRL_KZ = 9; scramble seed 1; mu1(h) =
4 sin^2(pi/(2h+1)) on r2's h; deep: TAB_EXT = 4_000_000, H_HOLD =
(128, 2900), KZ_SCAN_MAX = 400, DEEP_TAKE = 4 (smoke 2).  Runtime
cap declared: 12 min.

ANTI-CIRCULARITY (frozen): no sigma_h, no defect eigenvector, no
pivot sign, no spectral data of the TARGET B in any CONSTRUCTION:
candidate (i) uses only the PREVIOUS step's solved system
(declared recursive architecture), candidate (ii) only the
prime-free smooth model, candidate (iii) only matvecs with B from
the source vector b; c_B is a frozen upstream certificate
constant; float eigensolves of B appear ONLY in wards/guards
(W6, D floor guard) and in the Loewner BASELINE reproduction --
decisions and guards, never constructions.  The bad-x0 control
may use anything (it is a control).

NO-GO COMPLIANCE (frozen): no rank-1 approximation of the core
update; no plain Herglotz certificate; no fit where an identity
is claimed; the dead Loewner route is rebuilt ONLY as the
comparison baseline, never as a bound.

SMOKE-RUN DISCLOSURE (2026-08-11, before freezing): one smoke run
of this script (DDC_SMOKE=1: identical bars, deep block limited
to 2 rungs / 1 step; 23/23; 4.7 s; NO bar, band, count, rule or
enum was moved after it) measured: pipeline + P2/P3 + CXLIV
reproduction green (min lam_min(B) 0.6790, gap 0.0520/0.8875,
raw disaster -88.2, P_G PD 39/39, dominance 39/39); W6 floor
guard 39/39 (0.6790 >= 0.5523); Loewner baseline reproduced (med
qbar/q 91.31, min/max 4.39/408.18).  CANDIDATES: (i) TRANSPORT
FAILS TOTALLY (bound positive 0/38, med |r| 23.3, med preserved
fraction -1482, med improvement 5.5e-03 -- i.e. ~200x WORSE than
the dead Loewner route: the step objects (B, b) jump by orders
of magnitude in the co-frame coordinates, the previous solution
is no model of the next); (ii) CLASSICAL FAILS TOTALLY (0/35
positive, med |r| 19.4, med preserved fraction -1.1e+03; B_sm
nonsingular 35/35, non-PD 35/35 as known, fallback 0, smooth
missing on 4 -- the arithmetic deviation IS the object, not a
correction); (iii) KRYLOV largely certifies: per-k half census
0/8/16/20/31/37 of 39 for k = 1..6, k*_half reached on 37/39
(med ~3), TWO steps NOT reached at the frozen K_MAX = 6 (kz 16/
h 434 half-margin -2.4e+01, kz 24/h 490 -1.3e+01 -- the two
largest-|b| steps; k = 7 would be exact in the 7-dim co-block,
so the honest headline is 37/39 at k <= 6, not a bounded-k*
theorem), med improvement over Loewner at k*_half 4.0e+01,
half-margin@k* tau-screen PASS(-0.182, R2 0.04); deep smoke
step (kz 243, h 1292): floor guard 3.9638 >= 0.5523 holds, k* =
1.  Controls: C1-C4 all fire (smooth floor refusal 35/35;
bad-x0 fails the target on 38/39, med overhead 32.5 vs Loewner
5.8).  Identity ward max rel dev 6.03e-10 (bar 1e-9 -- close,
disclosed; the E2 surface is deterministic, the frozen run
reproduces it).  Fail-first preserved: nothing was weakened; the
verdict rule, bars and enums are exactly as frozen above.

SPEC v1 (2026-08-11, frozen + SHA-hashed before the frozen run):
everything above.  Mechanical concretizations frozen with v1: (i)
window memoization per (kz, seed); (ii) Householder frame as
P2/CL/CXLIV; (iii) P_G via eval_chain on r2's own chain at r2's
core nodes (CXLIV V4, s = 1/2); (iv) Krylov basis by modified
Gram-Schmidt with double reorthogonalization, breakdown bar
KRY_BD relative to the first basis norm; (v) steps sorted by
(h, kz), consecutive full-core pairs with r1 all-PSD, lamS > 0;
(vi) OLS population statistics as v900; screens read positive
subsets; (vii) deep census sorted by (h, kz), the DEEP_TAKE
shallowest taken; (viii) evaluable = the candidate's declared
domain (38 steps for (i), usable smooth steps for (ii), 39 for
(iii)).

NO RH claim: a certified half-mu1 margin (had it held) is a
SURFACE statement about the computed step matrices of the
deployed ladder ONLY; it does not prove n > q uniformity in h,
the pipeline enclosure at depth, or any tail statement.  The k*
ladder is a measurement.  No marker moves.

FIREWALL: no zeros, no prime oracles (AST scan; banned ids
zetazero / nzeros / primerange / isprime / primepi / nextprime /
prevprime; the extended table comes from the deployed sieve
generator, not an oracle); v563 READ-ONLY; RNG ONLY inside the
declared scramble control and the declared bad-x0 control;
stdout only.

Sources (read-only): v563_paper2_readouts; wall + fixed-core +
P_G machinery verbatim from pgram_directional_schur_probe (CL) =
bfloor_pg_dominance_probe (CXLIV); c_B = 0.5523 from
pg_chain_interval_rollout_probe (CLIII, declared input); mu1
target from halfgap_registration_probe (CLI, declared input);
smooth co-block build from CL C3; extended-table machinery from
deep_blind_holdout_probe (CLIV).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/directional_defect_correction_probe.py
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
PG_TOL = 1e-12
DOMHALF_MIN = 37
C_B_CERT = 0.5523            # CLIII certified ladder min (spent)
LOEW_MED_REF = 91.3
LOEW_RTOL = 5e-2
ID_WARD = 1e-9
UPB_WARD = 1e-9
K_MAX = 6
KRY_BD = 1e-12
SM_COND_MAX = 1e12
SM_CLIP = 1e-8
REFUSE_MIN = 30
BADX0_SEED = 20260811
BADX0_FAIL_MIN = 30
SLOPE_PASS = 0.30
SLOPE_RELOC = 0.70
CTRL_KZ = 9
TAB_EXT = 4_000_000
H_HOLD = (128, 2900)
KZ_SCAN_MAX = 400
SMOKE = os.environ.get("DDC_SMOKE", "") == "1"
DEEP_TAKE = 2 if SMOKE else 4
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


def gram_anatomy(kz, world_fn=None, scramble_seed=None, comb=None,
                 keep_chain=False):
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
    out = dict(kz=kz, h=h, n=n, alpha=float(alpha), M=M, D=D, L=L)
    out["tau"] = float(evA[0])
    out["negA"] = int(np.sum(evA < 0.0))
    if keep_chain:
        out["chain"] = (al, be, m0)
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
    out["lamR"] = float(evR[0])
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
    if keep_chain:
        out["y_core"] = np.array([ys[idx[j]] for j in CORE_J])
        out["v_core"] = np.array([vs[idx[j]] for j in CORE_J])
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


# ------------------------------ certified bounds (P3 verbatim)
def gersh_min(B):
    d = np.diag(B)
    r = np.sum(np.abs(B), axis=1) - np.abs(d)
    return float(np.min(d - r))


def gersh_scaled(B):
    d = np.diag(B)
    if float(np.min(d)) <= 0.0:
        return float("-inf")
    s = 1.0 / np.sqrt(d)
    C = B * np.outer(s, s)
    r = np.sum(np.abs(C), axis=1) - np.abs(np.diag(C))
    lamg = float(np.min(1.0 - r))
    return lamg * (float(np.min(d)) if lamg >= 0.0
                   else float(np.max(d)))


def cassini_scaled(B):
    d = np.diag(B)
    if float(np.min(d)) <= 0.0:
        return float("-inf")
    s = 1.0 / np.sqrt(d)
    C = B * np.outer(s, s)
    r = np.sum(np.abs(C), axis=1) - np.abs(np.diag(C))
    rr = np.sort(r)[::-1]
    lamc = 1.0 - math.sqrt(float(rr[0]) * float(rr[1]))
    return lamc * (float(np.min(d)) if lamc >= 0.0
                   else float(np.max(d)))


def best_cert(B):
    return max(gersh_min(B), gersh_scaled(B), cassini_scaled(B))


def build_pg(w):
    """The source-only P_G co-block (CXLIV V0 direction)."""
    r2 = w["r2"]
    ch = r2.get("chain")
    if ch is None:
        return None
    al, be, m0 = ch
    Pc = eval_chain(al, be, m0, r2["y_core"], r2["h"])
    Gc = (np.sqrt(r2["v_core"])[:, None] * (Pc @ Pc.T)
          * np.sqrt(r2["v_core"])[None, :])
    Gc = 0.5 * (Gc + Gc.T)
    PG = (w["Q"].T @ Gc @ w["Q"])[1:, 1:]
    return 0.5 * (PG + PG.T)


def mu1_of(h):
    return 4.0 * math.sin(math.pi / (2.0 * h + 1.0)) ** 2


# ---------------------- the defect-correction bookkeeping (new)
def eval_x0(nsc, b, B, x0, q, mu1):
    """SOURCE-ONLY bookkeeping for one candidate x0 (matvecs with
    B only; solve(B, r) appears ONLY in the returned identity
    deviation = a ward, never in the bound)."""
    rvec = b - B @ x0
    rn = float(np.linalg.norm(rvec))
    s1 = 2.0 * float(b @ x0) - float(x0 @ (B @ x0))
    qup = s1 + rn * rn / C_B_CERT
    q_id = s1 + float(rvec @ np.linalg.solve(B, rvec))
    id_dev = abs(q - q_id) / max(abs(q), 1e-300)
    bm = nsc - qup
    return dict(rn=rn, qup=qup, bm=bm, hm=bm - 0.5 * mu1,
                pf=(nsc - qup) / (nsc - q), ovh=qup - q,
                id_dev=id_dev)


def krylov_iterates(b, B, kmax):
    """CG-equivalent Krylov minimizers x_k over span{b,...,
    B^{k-1}b}, k = 1..kmax; modified Gram-Schmidt, double
    reorthogonalization, grade breakdown at KRY_BD."""
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
    while len(xs) < kmax:                     # grade reached
        xs.append(xs[-1].copy())
    return xs


def type_candidate(label, bms, hms, n_dom):
    n_eval = len(bms)
    n_half = sum(1 for x in hms if x >= 0.0)
    n_pos = sum(1 for x in bms if x > 0.0)
    if n_eval == 0:
        return "%s-EMPTY(0 of %d evaluable)" % (label, n_dom)
    if n_half == n_eval:
        return ("%s-TARGET-CERTIFIED(%d/%d, min half-margin "
                "%+.3e)" % (label, n_half, n_eval,
                            float(np.min(hms))))
    if n_pos == n_eval:
        return ("%s-POSITIVE-ONLY(%d/%d pos, half %d/%d)"
                % (label, n_pos, n_eval, n_half, n_eval))
    return ("%s-FAILS(pos %d/%d, half %d/%d)"
            % (label, n_pos, n_eval, n_half, n_eval))


# ---------------- extended surface (deep_blind_holdout verbatim)
EXT = {}


def build_ext_tables():
    lam_ext = core.von_mangoldt_table(TAB_EXT)
    NN = np.nonzero(lam_ext > 0.0)[0]
    EXT["lam"] = lam_ext
    EXT["NN"] = NN
    EXT["U"] = np.log(NN.astype(float))
    EXT["MU"] = 2.0 * lam_ext[NN] / np.sqrt(NN.astype(float))
    EXT["G"] = np.diff(EXT["U"])
    return lam_ext


def ext_frame(kz):
    alpha = float(EXT["U"][kz])
    D_k = 0.5 * float(EXT["G"][kz]) / float(core.NU_MAIN)
    Mz = int(math.ceil(alpha / D_k - 1.0e-9)) + 1
    if Mz % 2:
        Mz += 1
    hz = Mz // 2
    ka = int(np.searchsorted(EXT["U"], 2.0 * alpha + 1.0e-14,
                             side="right"))
    return alpha, Mz, hz, ka


def ext_gram(kz):
    """bfloor/CLIV gram_anatomy verbatim on the extended frame."""
    alpha, M, h, ka = ext_frame(kz)
    c_at, D = core.atom_lags_at(alpha, M, EXT["U"][:ka],
                                EXT["MU"][:ka])
    c_ar = np.asarray(core.arch_lags(M, D), float)
    d = grid_density(c_ar + np.asarray(c_at, float))
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
    out = dict(kz=kz, h=h, n=n, alpha=alpha, M=M)
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


def main():
    section("PRIME.PORT.DIRECTIONAL.DEFECT.01 -- directional "
            "defect correction: approximate only x* = B^{-1} b, "
            "pay the residual with the certified floor c_B = "
            "%.4f (EXPLORATION ONLY)" % C_B_CERT)
    print("    FROZEN_SPEC SHA-256 = %s"
          % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
    print("    NO RH claim; no marker moves.  Float-level probe "
          "on the float64-computed step matrices; c_B = 0.5523 "
          "is the CLIII interval-certified ladder minimum "
          "(declared input, spent as a constant).")
    if SMOKE:
        print("    *** SMOKE MODE (DDC_SMOKE=1): deep block "
              "limited to 2 rungs / 1 step ***")
    print("\nS0 -- firewall")
    check("S0.1 AST firewall clean", not ast_scan(BANNED_IDS))

    # ------------------------------------------------------------ W
    section("W -- the truth ladder + P2/P3 + CXLIV reproduction "
            "+ the floor-consumption guard")
    zones = ladder_zones()
    check("W1 frozen rung count %d" % N_RUNGS_EXP,
          len(zones) == N_RUNGS_EXP, "found %d" % len(zones),
          kill="K1")
    truth = []
    sm_map = {}
    for kz in zones:
        r = gram_anatomy(kz, keep_chain=True)
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
        Bsm, bsm = None, None
        if isinstance(rs2, dict) and "S" in rs2:
            M0 = Q.T @ (rs2["S"] / r1["tau"]) @ Q
            M0 = 0.5 * (M0 + M0.T)
            Bsm = M0[1:, 1:].copy()
            bsm = M0[1:, 0].copy()
        rows.append(dict(r1=r1, r2=r2, Q=Q, B=B, b=b, nsc=nsc,
                         q=q, gap=nsc - q, minB=minB, Bsm=Bsm,
                         bsm=bsm, tau=r1["tau"],
                         mu1=mu1_of(r2["h"]), bestg=best_cert(B)))
    minB_all = float(np.min([w["minB"] for w in rows]))
    gaps = np.array([w["gap"] for w in rows])
    bests = np.array([w["bestg"] for w in rows])
    gmin, gmed = float(np.min(gaps)), float(np.median(gaps))
    ok_repro = (abs(minB_all / MINB_REF - 1.0) <= MINB_RTOL
                and abs(gmin / GAPMIN_REF - 1.0) <= GAP_RTOL
                and abs(gmed / GAPMED_REF - 1.0) <= GAP_RTOL
                and float(np.max(bests)) < 0.0)
    check("W4 REPRODUCTION P2/P3 ledger: min lam_min(B) %.4f == "
          "%.3f; gap min/med %.4f/%.4f == %.3f/%.3f; raw-B "
          "certified disaster (best max %+.1f < 0 on %d steps)"
          % (minB_all, MINB_REF, gmin, gmed, GAPMIN_REF,
             GAPMED_REF, float(np.max(bests)), len(rows)),
          ok_repro, kill="K2")
    pg_ok = True
    n_dom = 0
    for w in rows:
        PG = build_pg(w)
        if PG is None:
            pg_ok = False
            continue
        if float(np.linalg.eigvalsh(PG)[0]) <= PG_TOL:
            pg_ok = False
        w["PG"] = PG
        Dm = w["B"] - 0.5 * PG
        Dm = 0.5 * (Dm + Dm.T)
        evd = np.linalg.eigvalsh(Dm)
        w["cdom_f"] = float(evd[0])
        if int(np.sum(evd < 0.0)) == 0:
            n_dom += 1
    check("W5 REPRODUCTION CXLIV V4: P_G PD on every step; float "
          "dominance negidx(B - 1/2 P_G) = 0 on %d/%d (>= %d)"
          % (n_dom, len(rows), DOMHALF_MIN),
          pg_ok and n_dom >= DOMHALF_MIN, kill="K2")
    check("W6 FLOOR CONSUMPTION GUARD: float lam_min(B) = %.4f "
          ">= C_B_CERT = %.4f on %d/%d steps (the spent CLIII "
          "constant sits below the measured floor everywhere)"
          % (minB_all, C_B_CERT,
             sum(1 for w in rows if w["minB"] >= C_B_CERT),
             len(rows)),
          all(w["minB"] >= C_B_CERT for w in rows), kill="K2")
    if KILLS:
        return finish({})

    # ----------------------------------------------------------- E1
    section("E1 -- the Loewner baseline (float rebuild of the CL "
            "ladder; the 91x table the candidates must beat)")
    for w in rows:
        D = 0.5 * w["PG"] + w["cdom_f"] * np.eye(7)
        w["qbar"] = float(w["b"] @ np.linalg.solve(D, w["b"]))
    qratio = np.array([w["qbar"] / w["q"] for w in rows])
    med_qr = float(np.median(qratio))
    check("E1 WARD Loewner baseline reproduced: med qbar/q %.2f "
          "== %.1f (rtol %.0e); min/max %.2f/%.2f"
          % (med_qr, LOEW_MED_REF, LOEW_RTOL,
             float(qratio.min()), float(qratio.max())),
          abs(med_qr / LOEW_MED_REF - 1.0) <= LOEW_RTOL,
          kill="K2")
    if KILLS:
        return finish({})

    # ----------------------------------------------------------- E2
    section("E2 -- the three frozen x0 candidates")
    id_dev_max = 0.0
    upb_viol_max = 0.0
    labels = {}

    def table_for(name, evals, idxs):
        nonlocal id_dev_max, upb_viol_max
        print("\n    CANDIDATE %s:" % name)
        print("      kz    h      |r|       qup     bound-marg  "
              "half-marg   presfrac    overhead    improve")
        bms, hms = [], []
        for w, ev in zip(idxs, evals):
            id_dev_max = max(id_dev_max, ev["id_dev"])
            upb_viol_max = max(upb_viol_max,
                               (w["q"] - ev["qup"])
                               / max(abs(w["q"]), 1e-300))
            imp = ((w["qbar"] - w["q"]) / ev["ovh"]
                   if ev["ovh"] > 0 else float("inf"))
            bms.append(ev["bm"])
            hms.append(ev["hm"])
            print("    %4d %5d  %9.3e %9.3f  %+9.4f  %+9.3e  "
                  "%+9.4f  %9.3e  %9.3e"
                  % (w["r2"]["kz"], w["r2"]["h"], ev["rn"],
                     ev["qup"], ev["bm"], ev["hm"], ev["pf"],
                     ev["ovh"], imp), flush=True)
        return bms, hms

    # (i) transported previous-step solution
    ev_tr, w_tr = [], []
    x_prev = None
    for w in rows:
        x_true = np.linalg.solve(w["B"], w["b"])
        if x_prev is not None:
            ev_tr.append(eval_x0(w["nsc"], w["b"], w["B"], x_prev,
                                 w["q"], w["mu1"]))
            w_tr.append(w)
        x_prev = x_true            # recursive architecture
    bms, hms = table_for("(i) TRANSPORT (E_h = identity on the "
                         "co-frame coordinates, declared; first "
                         "step skipped)", ev_tr, w_tr)
    lab_tr = type_candidate("TRANSPORT", bms, hms, len(rows))
    scr_tr, _ = screen(np.array(hms) + 0.5e-300,
                       [w["tau"] for w in w_tr])
    pf_tr = float(np.median([e["pf"] for e in ev_tr]))
    imp_tr = float(np.median([(w["qbar"] - w["q"]) / e["ovh"]
                              for w, e in zip(w_tr, ev_tr)
                              if e["ovh"] > 0])) \
        if any(e["ovh"] > 0 for e in ev_tr) else float("nan")
    check("E2.i typed: %s (med |r| %.3e, med presfrac %+.3f, med "
          "improve %.3e, half-margin screen %s)"
          % (lab_tr, float(np.median([e["rn"] for e in ev_tr])),
             pf_tr, imp_tr, scr_tr), True)
    labels["tr"] = lab_tr

    # (ii) prime-free classical solution
    ev_sm, w_sm = [], []
    n_nonpd, n_fallback, n_skip = 0, 0, 0
    for w in rows:
        if w["Bsm"] is None:
            n_skip += 1
            continue
        Bs = w["Bsm"]
        evs = np.linalg.eigvalsh(Bs)
        if float(evs[0]) <= 0.0:
            n_nonpd += 1
        cond = (float(np.max(np.abs(evs)))
                / max(float(np.min(np.abs(evs))), 1e-300))
        if cond > SM_COND_MAX:
            n_fallback += 1        # positive completed model
            ws_, Vs_ = np.linalg.eigh(Bs)
            ws_ = np.maximum(ws_, SM_CLIP)
            x0 = Vs_ @ ((Vs_.T @ w["bsm"]) / ws_)
        else:
            x0 = np.linalg.solve(Bs, w["bsm"])
        ev_sm.append(eval_x0(w["nsc"], w["b"], w["B"], x0,
                             w["q"], w["mu1"]))
        w_sm.append(w)
    bms, hms = table_for("(ii) CLASSICAL (x0 = B_sm^{-1} b_sm, "
                         "prime-free smooth co-block; non-PD "
                         "B_sm on %d, fallback on %d, smooth-"
                         "missing skip on %d)"
                         % (n_nonpd, n_fallback, n_skip),
                         ev_sm, w_sm)
    lab_sm = type_candidate("CLASSICAL", bms, hms, len(rows))
    scr_sm, _ = screen(np.array(hms) + 0.5e-300,
                       [w["tau"] for w in w_sm])
    check("E2.ii typed: %s (med |r| %.3e, med presfrac %+.3e, "
          "half-margin screen %s; the residual IS the arithmetic "
          "deviation)"
          % (lab_sm, float(np.median([e["rn"] for e in ev_sm]))
             if ev_sm else float("nan"),
             float(np.median([e["pf"] for e in ev_sm]))
             if ev_sm else float("nan"), scr_sm), True)
    labels["sm"] = lab_sm

    # (iii) short Krylov (CG iterates), k = 1..K_MAX
    kry = []
    for w in rows:
        xs = krylov_iterates(w["b"], w["B"], K_MAX)
        evk = [eval_x0(w["nsc"], w["b"], w["B"], x, w["q"],
                       w["mu1"]) for x in xs]
        kry.append(evk)
    print("\n    CANDIDATE (iii) KRYLOV/CG (source-only matvecs; "
          "per-k census over %d steps):" % len(rows))
    print("      k   pos n/N   half n/N   med presfrac   med "
          "improve")
    lab_k_final = None
    for k in range(K_MAX):
        bmk = [evk[k]["bm"] for evk in kry]
        hmk = [evk[k]["hm"] for evk in kry]
        n_pos = sum(1 for x in bmk if x > 0.0)
        n_half = sum(1 for x in hmk if x >= 0.0)
        pf_med = float(np.median([evk[k]["pf"] for evk in kry]))
        imps = [(w["qbar"] - w["q"]) / evk[k]["ovh"]
                for w, evk in zip(rows, kry)
                if evk[k]["ovh"] > 0]
        imp_med = float(np.median(imps)) if imps else float("inf")
        print("      %d   %2d/%2d     %2d/%2d      %+9.4f     "
              "%9.3e" % (k + 1, n_pos, len(rows), n_half,
                         len(rows), pf_med, imp_med), flush=True)
        for evk in kry:
            id_dev_max = max(id_dev_max, evk[k]["id_dev"])
        if n_half == len(rows) and lab_k_final is None:
            lab_k_final = k + 1
    check("E2.w1 WARD exact identity q == 2b*x0 - x0*Bx0 + "
          "r*B^{-1}r: max rel dev %.2e <= %.0e (all candidates, "
          "all steps, all k)" % (id_dev_max, ID_WARD),
          id_dev_max <= ID_WARD, kill="K2")
    check("E2.w2 WARD qup >= q (one-sided float allowance): max "
          "violation %.2e <= %.0e" % (max(upb_viol_max, 0.0),
                                      UPB_WARD),
          upb_viol_max <= UPB_WARD, kill="K2")

    # ----------------------------------------------------------- E3
    section("E3 -- the k* ladders (candidate iii; the headline)")
    kpos_l, khalf_l, hs = [], [], []
    print("      kz    h    k*_pos  k*_half   half-marg@k*   "
          "improve@k*")
    n_nr = 0
    for w, evk in zip(rows, kry):
        kpos = next((k + 1 for k in range(K_MAX)
                     if evk[k]["bm"] > 0.0), None)
        khalf = next((k + 1 for k in range(K_MAX)
                      if evk[k]["hm"] >= 0.0), None)
        if khalf is None:
            n_nr += 1
        kpos_l.append(kpos)
        khalf_l.append(khalf)
        hs.append(w["r2"]["h"])
        kk = (khalf or K_MAX) - 1
        imp = ((w["qbar"] - w["q"]) / evk[kk]["ovh"]
               if evk[kk]["ovh"] > 0 else float("inf"))
        print("    %4d %5d     %s      %s      %+9.3e    %9.3e"
              % (w["r2"]["kz"], w["r2"]["h"],
                 str(kpos) if kpos else "INF",
                 str(khalf) if khalf else "INF",
                 evk[kk]["hm"], imp), flush=True)
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
    hm_at = [evk[(kh or K_MAX) - 1]["hm"]
             for evk, kh in zip(kry, khalf_l)]
    scr_k, _ = screen(hm_at, [w["tau"] for w in rows])
    imps_at = [(w["qbar"] - w["q"]) / evk[(kh or K_MAX) - 1]["ovh"]
               for w, evk, kh in zip(rows, kry, khalf_l)
               if evk[(kh or K_MAX) - 1]["ovh"] > 0]
    imp_med_at = (float(np.median(imps_at)) if imps_at
                  else float("inf"))
    check("E3 typed: %s; half-margin@k* screen %s; med "
          "improvement over the Loewner route at k*_half: %.3e"
          % (kstar_lab, scr_k, imp_med_at), True)
    labels["kry"] = ("KRYLOV[%s]"
                     % type_candidate(
                         "K%d" % (lab_k_final or K_MAX),
                         [evk[(lab_k_final or K_MAX) - 1]["bm"]
                          for evk in kry],
                         [evk[(lab_k_final or K_MAX) - 1]["hm"]
                          for evk in kry], len(rows)))
    labels["kstar"] = kstar_lab
    labels["imp"] = "IMPROVEMENT(med %.1e at k*_half)" % imp_med_at
    labels["scr"] = "SCREENS(kry %s)" % scr_k

    # ------------------------------------------------------------ D
    section("D -- deep spot-check (4e6 table; c_B spent as a "
            "HYPOTHESIS at depth, float floor guard per step)")
    deep_lab = "DEEP-SHORT(not run)"
    try:
        lam_ext = build_ext_tables()
        dev = float(np.max(np.abs(lam_ext[:core.ATOM_MAX + 1]
                                  - core.LAM_TAB)))
        nP = len(core.U_ALL)
        ok_pref = (np.array_equal(EXT["NN"][:nP], core._NN)
                   and np.array_equal(EXT["U"][:nP], core.U_ALL)
                   and np.array_equal(EXT["MU"][:nP],
                                      core.MU_ALL)
                   and np.array_equal(EXT["G"][:nP - 1],
                                      core.G_ALL[:nP - 1]))
        check("D.w1 WARD extended-table fidelity: overlap max abs "
              "dev %.1e == 0.0; prefix arrays bitwise %s"
              % (dev, ok_pref), dev == 0.0 and ok_pref,
              kill="K2")
        cens = []
        for kz in range(2, KZ_SCAN_MAX):
            if kz >= len(EXT["G"]):
                break
            alpha, Mz, hz, ka = ext_frame(kz)
            X = math.exp(2.0 * alpha)
            if X <= core.ATOM_MAX or X > TAB_EXT:
                continue
            if not (H_HOLD[0] <= hz <= H_HOLD[1]):
                continue
            cens.append((hz, kz))
        cens.sort()
        take = cens[:DEEP_TAKE]
        print("    deep census: %d new rungs; taking %d "
              "shallowest: %s  [%.1f s]"
              % (len(cens), len(take),
                 ["kz %d/h %d" % (kz, hz) for hz, kz in take],
                 time.time() - T0), flush=True)
        deeps = []
        for hz, kz in take:
            r = ext_gram(kz)
            if r is None or not r.get("core_ok"):
                print("    kz %d h %d: chain short / core "
                      "missing -> SKIPPED" % (kz, hz))
                continue
            deeps.append(r)
        deeps.sort(key=lambda r: (r["h"], r["kz"]))
        dsteps = []
        for r1, r2 in zip(deeps, deeps[1:]):
            if r1["negA"] > 0 or r1["lamS"] <= 0.0:
                continue
            dsteps.append((r1, r2))
        if not dsteps:
            deep_lab = "DEEP-SHORT(no scoreable deep step)"
            check("D typed: %s" % deep_lab, True)
        else:
            dk_list, n_ref = [], 0
            x_prev_d, tr_rows = None, []
            print("      kz    h    lam_min(B)  guard   k*_pos  "
                  "k*_half  half-marg@k*")
            for r1, r2 in dsteps:
                wS, VS = np.linalg.eigh(r1["S"])
                Qd = householder_frame(VS[:, 0])
                Mt = Qd.T @ (r2["S"] / r1["tau"]) @ Qd
                Mt = 0.5 * (Mt + Mt.T)
                nsc = float(Mt[0, 0])
                bd = Mt[1:, 0].copy()
                Bd = Mt[1:, 1:].copy()
                minBd = float(np.linalg.eigvalsh(Bd)[0])
                qd = float(bd @ np.linalg.solve(Bd, bd))
                mu1d = mu1_of(r2["h"])
                if minBd < C_B_CERT:
                    n_ref += 1
                    print("    %4d %5d  %9.4f   REFUSED (< c_B)"
                          % (r2["kz"], r2["h"], minBd),
                          flush=True)
                    x_prev_d = np.linalg.solve(Bd, bd)
                    continue
                xs = krylov_iterates(bd, Bd, K_MAX)
                evk = [eval_x0(nsc, bd, Bd, x, qd, mu1d)
                       for x in xs]
                kpos = next((k + 1 for k in range(K_MAX)
                             if evk[k]["bm"] > 0.0), None)
                khalf = next((k + 1 for k in range(K_MAX)
                              if evk[k]["hm"] >= 0.0), None)
                kk = (khalf or K_MAX) - 1
                dk_list.append((r2["kz"], r2["h"], kpos, khalf))
                print("    %4d %5d  %9.4f   ok       %s      %s"
                      "      %+9.3e"
                      % (r2["kz"], r2["h"], minBd,
                         str(kpos) if kpos else "INF",
                         str(khalf) if khalf else "INF",
                         evk[kk]["hm"]), flush=True)
                if x_prev_d is not None:
                    evt = eval_x0(nsc, bd, Bd, x_prev_d, qd,
                                  mu1d)
                    print("           transport(i): |r| %.3e  "
                          "bound-marg %+9.4f  half-marg %+9.3e"
                          % (evt["rn"], evt["bm"], evt["hm"]),
                          flush=True)
                    tr_rows.append(evt["hm"] >= 0.0)
                x_prev_d = np.linalg.solve(Bd, bd)
            if dk_list:
                deep_lab = ("DEEP-KSTAR(%s%s%s)"
                            % (", ".join(
                                "h%d:k*=%s" % (hh,
                                               str(kh) if kh
                                               else "INF")
                                for _kz, hh, _kp, kh in dk_list),
                               "; refused %d" % n_ref
                               if n_ref else "",
                               "; transport half-pass %d/%d"
                               % (sum(tr_rows), len(tr_rows))
                               if tr_rows else ""))
            else:
                deep_lab = "DEEP-REFUSED(%d)" % n_ref
            check("D typed: %s (float level, hypothesis spend "
                  "declared)" % deep_lab, True)
    except MemoryError:
        deep_lab = "DEEP-SHORT(memory)"
        check("D typed: %s" % deep_lab, True)
    labels["deep"] = deep_lab

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
          "certified-floor spend is unavailable there, the "
          "machine refuses (mirrors CL exact-LDL refusal)"
          % (n_ref, n_use, REFUSE_MIN), n_ref >= REFUSE_MIN,
          kill="K2")
    rng = np.random.default_rng(BADX0_SEED)
    n_fail_bad = 0
    ovh_bad = []
    for w in rows:
        g = rng.standard_normal(7)
        t = float(w["b"] @ g) / float(g @ (w["B"] @ g))
        evb = eval_x0(w["nsc"], w["b"], w["B"], t * g, w["q"],
                      w["mu1"])
        if evb["hm"] < 0.0:
            n_fail_bad += 1
        ovh_bad.append(evb["ovh"])
    ovh_loew = [w["qbar"] - w["q"] for w in rows]
    check("C4 WARD BAD-x0 control: the seeded random direction "
          "(optimal 1-d scaling) FAILS the half-mu1 target on "
          "%d/%d steps (>= %d); med overhead %.3e vs Loewner med "
          "overhead %.3e -- the route's power is x0 quality, not "
          "bookkeeping"
          % (n_fail_bad, len(rows), BADX0_FAIL_MIN,
             float(np.median(ovh_bad)),
             float(np.median(ovh_loew))),
          n_fail_bad >= BADX0_FAIL_MIN, kill="K2")

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
        VERDICT = ("DIRDEFECT-MEASURED / %s / %s / %s / %s / %s "
                   "/ %s / %s"
                   % (labels.get("tr", "-"),
                      labels.get("sm", "-"),
                      labels.get("kry", "-"),
                      labels.get("kstar", "-"),
                      labels.get("imp", "-"),
                      labels.get("deep", "-"),
                      labels.get("scr", "-")))
        print("\n  VERDICT: %s" % VERDICT)
    print("""
  HONEST FRAME (as frozen): float-level probe on the float64-
  computed step matrices; the spent constant c_B = 0.5523 is the
  CLIII interval-certified ladder minimum over the ideal objects
  on the deployed 39-step surface -- at depth it is a declared
  HYPOTHESIS guarded per step.  A certified half-mu1 margin here
  is a SURFACE statement; it proves neither h-uniformity nor any
  tail statement.  NO RH claim.  No marker moves.""")
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed"
          % (time.time() - T0, n_tot, n_tot - n_pass))
    return 0 if n_pass == n_tot else 1


if __name__ == "__main__":
    raise SystemExit(main())
