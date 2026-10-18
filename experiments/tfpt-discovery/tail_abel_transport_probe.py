#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""tail_abel_transport_probe -- PRIME.PORT.TAIL.ABEL.01
(EXPLORATION ONLY, experiments/; round 63, theorem-engineering on
the RH-side wall, probe 3 -- the CUMULATIVE attack on the tail.
Predecessors (round 62, PRIME.PORT.TAILSIGN.01/.02) closed the
ATOMWISE route: the net tail sign is an arithmetic CANCELLATION
fact over ~2000 deep atoms (tail_B <= 0 at the per-rung first
B-covering cut on 67/67, n_minB med 17, range 5..47), POINTWISE
weight negativity is impossible (terminal lobe positive 67/67,
onset u/(2 alpha) ~ 0.752), the head margin at those cuts is O(1)
(med 0.388, slope +0.113 vs m) -- the ENTIRE h-decay of the wall
margin lives in the net-negative tail -- and the deep weight
GEOMETRY is prime-free (q_{v_sm} reproduces the sign census
67/67).  THE FROZEN IDEA: the right object is the CUMULATIVE
distribution of the prime comb against the DISCRETE DERIVATIVES
of the weight.  2026-08-11.)

THE TRANSPORT (frozen).  Beyond the per-rung first B-covering cut
n_c = n_minB(h), put the tail on the INTEGER grid k = n_c+1 ..
N_g = floor(X), X = e^{2 alpha}: masses a_k = mu_k = 2 Lambda(k)/
sqrt(k) (zero off prime powers; identical floats to the deployed
window atoms, warded), weights w_k = q_v(log k) with q_v the
deployed piecewise-linear per-atom weight functional (lift-race
S0 verbatim; exact identity sum mu_n q_v(u_n) = E_at warded).
Then T_h = sum_k a_k w_k = tail_B(cB) EXACTLY (tie warded), and
the Abel/partial-summation chain (all sums over [J, N], J =
n_c + 1, A1(k) = sum_{n<=k} a_n, A2 = cumsum A1, A3 = cumsum A2):
  order 1:  T = A1(N) w_N - sum_{k<N} A1(k) Dw(k)
  order 2:  T = A1(N) w_N - A2(N-1) Dw(N-1)
                + sum_{k<N-1} A2(k) D2w(k)
  order 3:  T = A1(N) w_N - A2(N-1) Dw(N-1) + A3(N-2) D2w(N-2)
                - sum_{k<N-2} A3(k) D3w(k)
with Dw(k) = w_{k+1} - w_k etc.  Each summation-by-parts moves a
discrete derivative onto the weight (the DUAL KERNEL D^r w --
prime-free for w = q_{v_sm}: an all-integer grid read of a
prime-free function) and a further cumulation onto the primes.

WHAT IS MEASURED (frozen; typed, never kills unless marked WARD):
 (a) SIGN OF THE DUAL KERNEL: exact sign census of D^r w on the
     deep integer grid for r = 1, 2, 3 and BOTH weights (v
     arithmetic; v_sm prime-free, crossing rungs read on their
     carrier branch as in round 62): number of strict sign
     changes (entries below SIGN_EPS * max|D^r w| treated as
     zero, declared), dominant-sign mass share, last-change
     position u/(2 alpha), dominant sign.  Typed
     DUALSIGN-FIXED(r*, N/N, sign) iff some r <= 3 has ZERO sign
     changes on ALL rungs for q_{v_sm}; else DUALSIGN-OPEN with
     the residual census as the named obstruction.
 (b) WHICH CUMULATIVE PRIME QUANTITY (exact identities, WARD):
     A1(k) = 2 sum_{J<=n<=k} Lambda(n)/sqrt(n) is a windowed
     psi-type partial sum: the exact psi-Abel identity
       A1(k) = 2 [ psi_w(k)/sqrt(k)
                   + sum_{m=J}^{k-1} psi_w(m) delta_m ],
       psi_w(m) = sum_{J<=n<=m} Lambda(n),
       delta_m = m^{-1/2} - (m+1)^{-1/2},
     is warded at EVERY k to PSI_ID_WARD.  A^{(r)}(k) =
     2 sum_n binom(k-n+r-1, r-1) Lambda(n)/sqrt(n) is the
     (r-1)-th Riesz/Cesaro mean of the sqrt-smoothed prime comb
     (r = 2: integrated psi-type / Riesz mean; r = 3: twice
     integrated); warded exactly at two frozen spot indices per
     rung (mid, end) to RIESZ_WARD.  The Abel chain itself is
     warded at all three orders to ABEL_WARD relative to the
     declared term scale sc_r = |boundary| + sum |A_r| |D^r w|
     (float bookkeeping; the identity is exact arithmetic).
 (c) ENVELOPES (decisive): the ONLY deployed unconditional
     envelope in the corpus is the Chebyshev table constant
     kappa = 0.038821: |psi(x) - x| <= kappa x at the JUMP POINTS
     of psi(x)/x on [100, 400000] (v563 S0.KAPPA, reproduced here
     as a WARD; B_PSI = 1.03883 noted, not needed).  The
     transport reads psi at ALL integers, where the deficit side
     just before a jump is larger -- AMENDMENT A1 (disclosed
     below): the bound uses the ALL-INTEGER table constant
     KAPPA_INT = max_{100 <= n <= 400000} |psi(n) - n|/n,
     computed in-run from the same deployed table (same finite-
     verification class, strictly weaker = conservative); below
     100 the table-verified exact deviations |psi(n) - n|.  With
     D(m) = (psi(m) - m) - (psi(J-1) - (J-1)) the exact Abel form
     of E1(k) = A1(k) - At1(k), At1(k) = 2 sum 1/sqrt(n) (the
     integer smooth counterpart), gives the PROVABLE pointwise
     bound
       |E1(k)| <= BE1(k) = 2 [ beta(k)/sqrt(k)
                    + sum_{m=J}^{k-1} beta(m) delta_m ],
       beta(m) = bnd(m) + bnd(J-1),
       bnd(x) = KAPPA_INT x (x >= 100) else |psi(x) - x|_table,
     warded in-window (|E1| <= BE1 everywhere, float slack), and
     BE_{r+1} = cumsum BE_r bounds the higher cumulants.  The
     envelope-certified lower bound at order r:
       T >= Ttilde - ERR_r,  Ttilde = sum_k (2/sqrt(k)) w_k,
       ERR_1 = BE1(N)|w_N| + sum BE1|Dw|,
       ERR_2 = BE1(N)|w_N| + BE2(N-1)|Dw(N-1)| + sum BE2|D2w|,
       ERR_3 = ... + BE3(N-2)|D2w(N-2)| + sum BE3|D3w|.
     THE DECISIVE MEASUREMENT: with H = head_B(cB) and the frozen
     halfgap constant C0 = 1/2 (CLI registration, NO-ADJUST --
     recorded comparison only, no constant move), the per-rung
     per-order slack in mu1 units
       slack_r = (H + Ttilde - ERR_r)/mu1 - C0,
       mu1 = 4 sin^2(pi/(2h+1)) = core.parity_mu(h)[0] (warded),
     slack_best = max_r slack_r.  Typed ENV-SUFFICIENT(min
     slack_best) iff slack_best > 0 on ALL rungs (then the tail
     statement closes classically on the surface -- said
     prominently, with constants); else ENV-INSUFFICIENT(min/med
     slack_best, gap law): jackknife slope of log(ERR_best/mu1)
     vs alpha (the gap law) and vs log m (screen).  Context
     diagnostics (printed): the MEASURED arithmetic remainder
     (T - Ttilde)/mu1 and the envelope OVERSHOOT ERR_best /
     |T - Ttilde| -- how much the absolute envelope loses against
     the actual oscillating sum; Ttilde vs the round-60 continuum
     smoothtail(cB) (Euler-Maclaurin tie, info).
 (d) NORMALIZED CONSTANT (recorded, NO adjustment): chat =
     (H + Ttilde)/mu1 -- the smooth-certified part of the halfgap
     statement.  Census: min/med/max, count chat > 0, count
     chat >= C0; the arithmetic remainder share rhat =
     (T - Ttilde)/mu1 min/med/max.  Connection to the frozen
     HALFGAP 1/2 recorded as a comparison only.
 (e) TAU-SCREENS (typed, jackknife, bands PASS |s| <= 0.30 /
     RELOC s >= 0.70 / else AMBIG): log chat vs log m (on the
     chat > 0 subset, disclosed if not all); log(ERR_best/mu1)
     vs log m.

FROZEN PROTOCOL (ladder machinery verbatim from
tail_sign_mechanism_probe.py = round-59/60/62 chain; v_sm
construction verbatim from arithmetic_lift_race_probe S0):

 W   LADDER + WARDS (kill -> PIPELINE-BROKEN / WARD-BROKEN): W1
     faithful ladder >= MIN_RUNGS = 40 (kz 2..KZMAX, H_MIN <= h
     <= HCAP, X <= ATOM_MAX); W2 WARD m_h > 0 everywhere; W3 WARD
     both exact bookkeepings (lift - demand = m AND e_ar + E_at =
     m) <= ID_WARD; W4 WARD atom identities (atom sum = E_at, PNT
     grid = E_sm) <= ID_WARD; W5 WARD split exactness on the full
     scans <= SCAN_WARD; W6 REPRODUCTION round 59/60/62: G > 0
     counts at (50, 100, 200) == (52, 26, 25); n_min in [3, 9];
     shared cut 9 covers N/N; tail_A <= 0 at first covering cut
     N/N; B-covering cuts exist N/N with n_minB med == 17 in
     [5, 47]; tail_B <= 0 at cB N/N; head_B(cB) med within
     HEADB_TOL of 0.388; W7 WARD v_sm branch (<= MAX_CROSS
     crossing rungs, carrier branch overlap >= OV_MIN); W8 WARD
     kappa: core.chebyshev_kappa() within 1e-6 of 0.038821; W9
     WARD mu1 closed form == core.parity_mu(h)[0] exactly and the
     CXLIII shat band: shat = m/mu1 min/med/max within SHAT_TOL
     of (0.502, 1.027, 2.185); W10 WARD grid tie: the integer-
     grid tail equals tail_B(cB) <= TIE_WARD; W11 WARD envelope
     in-window: |E1| <= BE1 everywhere on every rung (float
     slack ENV_SLACK).

 A/B/E/N/T  as (a)/(b)/(c)/(d)/(e) above.

 C   CONTROLS at kz 9 (kill -> WARD-BROKEN if silent): C1
     scramble (seed 1), Epstein x^2+5y^2, smooth comb: each must
     show m < 0 AND zero covering cuts in BOTH senses (round-62
     criterion).  C2 envelope battery from the FIXED declared cut
     CTRL_CUT = 17: the scramble comb (true masses at uniform
     positions, read at integer points against the SAME integer
     smooth counterpart, declared) must VIOLATE the classical
     envelope by a factor >= CTRL_VIOL = 5 (the cumulative
     structure is destroyed -- structurally certain, kill if
     silent); the Epstein and smooth-world envelope factors are
     REPORTED as typed measurements (smooth expected <= 1 --
     quadrature only; Epstein's psi-deviation is a measurement,
     honestly typed either way, no kill).

KILLS: K1 ladder (W1) -> PIPELINE-BROKEN; K2 wards (W2-W11, B
wards, C1/C2-scramble) -> WARD-BROKEN.  All typed A/E/N/T
outcomes are measurements, never kills.

VERDICT (frozen enum): TAILABEL-MEASURED with typed sublabels
DUALSIGN-FIXED(r*, N/N, sign) / DUALSIGN-OPEN(best r, count/N,
med changes, med dominant share),
ABEL-EXACT(max dev) + ARITH-ID(psi dev, riesz dev),
ENV-SUFFICIENT(min slack) / ENV-INSUFFICIENT(min/med slack, gap
slope vs alpha),
CHAT(min/med/max, n >= 1/2),
SCREENS(chat, gap);  else PIPELINE-BROKEN / WARD-BROKEN.

FROZEN BARS: KZMAX = 150; MIN_RUNGS = 40; REF_CUTS = (50, 100,
200); REF_COUNTS = (52, 26, 25); NMIN_LO, NMIN_HI = 3, 9;
NC_SHARED = 9; NB_MED = 17; NB_LO, NB_HI = 5, 47; HEADB_MED =
0.388, HEADB_TOL = 0.01; SHAT_REF = (0.502, 1.027, 2.185),
SHAT_TOL = 1.5e-3; ID_WARD = 1e-10; SCAN_WARD = 1e-9; TIE_WARD =
1e-10; ABEL_WARD = 1e-12 (relative to the declared term scale);
PSI_ID_WARD = 1e-12; RIESZ_WARD = 1e-12; ENV_SLACK = 1e-9;
KAPPA_TOL = 1e-6; KAPPA_INT = in-run all-integer table constant
(amendment A1, reported in W8); MU_WARD = 1e-12; NG_SMOOTH =
6000; OV_MIN =
0.8; MAX_CROSS = 2; SIGN_EPS = 1e-15 (relative); C0 = 1/2
(frozen, NO-ADJUST, recorded comparison only); SLOPE_PASS = 0.30;
SLOPE_RELOC = 0.70; CTRL_KZ = 9; CTRL_CUT = 17; CTRL_VIOL = 5.0;
scramble seed 1; jackknife = full leave-one-out, CI = +- 2SE;
sign decisions on exact grid values (float sign with the declared
relative zero threshold); blocked cumulative sums (block 1024,
deterministic error bound) wherever a cumsum feeds a ward.

SMOKE-RUN DISCLOSURE (2026-08-11, before freezing): TWO smoke
runs disclosed.  SMOKE 1 (SPEC v0, W11 FAILED at min slack
-0.386): the deployed jump-point kappa does NOT majorize the
all-integer psi deviations -- measured all-integer table constant
0.059547 (worst at n = 100, deficit side) vs jump-point 0.038821.
AMENDMENT A1 (disclosed, conservative -- the envelope gets
WEAKER, fail-first preserved): the bound switches to the
ALL-INTEGER table constant KAPPA_INT as frozen in (c) above; the
jump-point kappa stays as the W8 reproduction ward.  SMOKE 2
(22/22, 18.3 s) facts frozen as the context the frozen run must
confirm: (i) DUALSIGN-OPEN at EVERY order: single-signed 0/67 for
r = 1, 2, 3 (q_{v_sm}); med sign changes 3/363/1113 -- r = 1 is
NEARLY fixed (2..3 changes per rung, negative-dominant on 67/67,
dominant mass share med 0.757: the first difference inherits the
2..4 deep slope-sign changes of the weight itself) and each
further difference EXPLODES the census (the lag-knot jumps of the
piecewise-linear weight dominate D^2 w, D^3 w) -- the r = 2
curvature hypothesis is DEAD; (ii) all identity wards at the
1e-15 class (Abel 8.9e-16, psi 1.5e-15, Riesz 3.3e-15, tie
9.7e-15, envelope in-window slack -8.9e-16 = float zero); (iii)
ENV-INSUFFICIENT on 67/67 with best order r = 1 on 67/67 (the
cumulated bounds BE2/BE3 grow faster than the extra difference
decays): slack min/med -3.32e+06/-1.51e+05, ERR_best/mu1 med
1.59e+05, gap law slope vs alpha +1.744 (2SE 0.202, R^2 0.77);
(iv) the MEASURED remainder (T - Ttilde)/mu1 is itself LARGE (med
-9847) and chat = (H + Ttilde)/mu1 correspondingly large (med
+9850, >= 1/2 on 64/67, NEGATIVE on 3 deep rungs) -- the integer
smooth counterpart and the atom comb differ at the cB cut by
O(0.1) absolute ~ 1e4 mu1 units: the halfgap does NOT live at the
(H + Ttilde) split, it lives in the near-cancellation chat + rhat
= shat; envelope overshoot vs the actual oscillating remainder
med 2.0e+01; (v) both screens anti-correlated (chat -1.068 R^2
0.81, gap -1.208 R^2 0.93 -> AMBIG per the frozen bands: budget
and mismatch explode exactly where the margin shrinks); (vi)
controls: C1 3/3, scramble envelope factor 5.99 >= 5 FIRES,
smooth 0.837 <= 1 as declared, Epstein 7.51 OUTSIDE the classical
envelope (measured, typed).  AMENDMENTS beyond A1: NONE -- no
bar, band, tolerance, enum or rule moved after the smoke.

SPEC v1 (2026-08-11, frozen + SHA-hashed before the frozen run):
everything above.  Mechanical concretizations frozen with v1:
(i) the cut is INCLUSIVE at the covering atom (grid starts at
n_c + 1); (ii) N_g = max(floor(X), largest window atom); (iii)
Lambda on the grid read from the deployed core.LAM_TAB (the same
sieve that builds the window atoms; equality of masses warded via
the grid tie W10); (iv) Riesz spot indices per rung: i = (L-1)//2
and i = L-1; (v) the smooth-world control snaps its prime-power
positions to integers by round(exp(u)) (exact); the scramble
control reads its cumulative mass at integer points by
searchsorted (declared above); (vi) runtime ~ 20 s (67 eigh
pairs dominate).

NO-GO COMPLIANCE (frozen): no certified-bound retry, no rank-1
approximation, no Herglotz; no fit where an identity is claimed
(the Abel chain, the psi-Abel identity, the Riesz identity and
the envelope bound are exact wards; all trends are typed
jackknife screens).

NO RH claim: everything here is float-level MEASURED SURFACE
STRUCTURE on the 67-rung ladder; the direction v is computed
per-rung data (the round-62 uniformity boundary applies
verbatim); an ENV-SUFFICIENT outcome would still be a per-rung
surface certificate, not a theorem, and an ENV-INSUFFICIENT
outcome is a measured gap law, not a proof of impossibility.  The
halfgap constant 1/2 is the CLI registration and is NEVER
adjusted here.  No marker moves.

FIREWALL: no zeros, no prime oracles (AST scan; banned ids
zetazero / nzeros / primerange / isprime / primepi / nextprime /
prevprime; Lambda is read from the DEPLOYED window table only);
v563 READ-ONLY; RNG only inside the declared scramble control;
stdout only.

Sources (read-only): v563_paper2_readouts (core; kappa envelope
S0.KAPPA, B_PSI noted); ladder + cut/scan machinery verbatim from
tail_sign_mechanism_probe.py (round 62); q_read + v_sm
construction verbatim from arithmetic_lift_race_probe.py; mu1
normalization from moving_node_second_order_probe.py (CXLIII);
halfgap constant C0 = 1/2 from halfgap_registration_probe.py
(CLI, NO-ADJUST); round-62 censuses (declared reproduction
targets).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/tail_abel_transport_probe.py
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

KZMAX = 150
MIN_RUNGS = 40
REF_CUTS = (50, 100, 200)
REF_COUNTS = (52, 26, 25)
NMIN_LO, NMIN_HI = 3, 9
NC_SHARED = 9
NB_MED = 17
NB_LO, NB_HI = 5, 47
HEADB_MED = 0.388
HEADB_TOL = 0.01
SHAT_REF = (0.502, 1.027, 2.185)
SHAT_TOL = 1.5e-3
ID_WARD = 1e-10
SCAN_WARD = 1e-9
TIE_WARD = 1e-10
ABEL_WARD = 1e-12
PSI_ID_WARD = 1e-12
RIESZ_WARD = 1e-12
ENV_SLACK = 1e-9
KAPPA_TOL = 1e-6
MU_WARD = 1e-12
NG_SMOOTH = 6000
OV_MIN = 0.8
MAX_CROSS = 2
SIGN_EPS = 1e-15
C0 = 0.5
SLOPE_PASS = 0.30
SLOPE_RELOC = 0.70
CTRL_KZ = 9
CTRL_CUT = 17
CTRL_VIOL = 5.0
KAPPA_LOW_X = 100
BLOCK = 1024
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


def jack_slope(x, y):
    x = np.asarray(x, float)
    y = np.asarray(y, float)
    _a, b, r2 = ols_line(x, y)
    n = len(x)
    bb = []
    for i in range(n):
        m = np.ones(n, bool)
        m[i] = False
        bb.append(ols_line(x[m], y[m])[1])
    bb = np.array(bb)
    se = math.sqrt((n - 1) / n * float(np.sum((bb - bb.mean())
                                              ** 2)))
    return b, se, r2


def q_read(W, u, D, M):
    u = np.asarray(u, float)
    i0 = np.floor(u / D).astype(int)
    f = u / D - i0
    val = np.zeros_like(u)
    ok0 = (i0 >= 0) & (i0 < M)
    val[ok0] += (1.0 - f[ok0]) * W[i0[ok0]]
    ok1 = (i0 + 1 >= 0) & (i0 + 1 < M)
    val[ok1] += f[ok1] * W[i0[ok1] + 1]
    refl = u < D
    val[refl] += (1.0 - u[refl] / D) * W[0]
    return -0.5 * val


def smooth_comb(alpha, ng=NG_SMOOTH):
    ug = (np.arange(ng) + 0.5) * (2.0 * alpha / ng)
    mg = 2.0 * np.exp(ug / 2.0) * (2.0 * alpha / ng)
    return ug, mg


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


def blocked_cumsum(x):
    """Deterministic error-bounded cumulative sum: within-block
    cumsum (<= BLOCK adds) + block-prefix offsets (<= L/BLOCK
    adds) -- feeds every warded identity."""
    x = np.asarray(x, float)
    n = len(x)
    if n <= BLOCK:
        return np.cumsum(x)
    pad = (-n) % BLOCK
    xb = np.concatenate([x, np.zeros(pad)]).reshape(-1, BLOCK)
    cs = np.cumsum(xb, axis=1)
    off = np.concatenate([[0.0], np.cumsum(cs[:-1, -1])])
    return (cs + off[:, None]).reshape(-1)[:n]


def sign_census(z, uu, alpha):
    """Exact sign census of a dual-kernel array z on the deep
    grid: strict sign changes among entries with |z| >
    SIGN_EPS max|z| (declared zero threshold), dominant-sign
    mass share, last-change scaled position, dominant sign."""
    z = np.asarray(z, float)
    az = np.abs(z)
    mx = float(az.max()) if len(z) else 0.0
    if mx == 0.0:
        return dict(n_changes=0, single=True, dom=1.0,
                    x_last=float("nan"), sign=0)
    mask = az > SIGN_EPS * mx
    s = np.sign(z[mask])
    um = uu[mask]
    ch = np.nonzero(s[1:] * s[:-1] < 0.0)[0]
    pos = float(z[z > 0.0].sum())
    neg = float(-z[z < 0.0].sum())
    dom = max(pos, neg) / max(pos + neg, 1e-300)
    x_last = (float(um[ch[-1] + 1]) / (2.0 * alpha)
              if len(ch) else float("nan"))
    return dict(n_changes=int(len(ch)), single=(len(ch) == 0),
                dom=dom, x_last=x_last,
                sign=(1 if pos >= neg else -1))


def build_rung(kz, comb=None, scramble_seed=None,
               smooth_world=False, need_sm=True):
    """One rung of the lift-race surface with both bookkeepings
    and the full atom-cut scans (tail_sign_mechanism_probe
    verbatim; additionally stores the raw mass vector mu)."""
    try:
        rr = core.build_window(kz, scramble_seed=scramble_seed)
    except Exception:
        return None
    if not (core.H_MIN <= rr["h"] <= core.HCAP):
        return None
    if rr["X"] > core.ATOM_MAX:
        return None
    alpha, M, D, h = rr["alpha"], rr["M"], rr["D"], rr["h"]
    uu = np.asarray(rr["uu"], float)
    mu = 2.0 * np.asarray(rr["lam"], float)
    if smooth_world:
        du = np.zeros(len(uu))
        du[1:-1] = 0.5 * (uu[2:] - uu[:-2])
        du[0] = uu[1] - uu[0]
        du[-1] = uu[-1] - uu[-2]
        mu = 2.0 * np.exp(uu / 2.0) * du
    if comb is not None:
        uu, mu = comb
    c_at = core.atom_lags_at(alpha, M, uu, mu)[0]
    c_ar = np.asarray(core.arch_lags(M, D), float)
    w, V = np.linalg.eigh(core.odd_toeplitz(c_ar + c_at, M))
    v = V[:, 0]
    ug, mg = smooth_comb(alpha)
    c_sm = core.atom_lags_at(alpha, M, ug, mg)[0]
    row = dict(kz=kz, alpha=float(alpha), h=h, M=M, D=D,
               m=float(w[0]), uu=uu, mu=mu, X=float(rr["X"]))
    Wv = core.lag_weights_from_v(v, h)
    e_ar = float(c_ar @ Wv)
    e_t = float(c_at @ Wv)
    e_s = float(c_sm @ Wv)
    qa = mu * q_read(Wv, uu, D, M)
    qg = mg * q_read(Wv, ug, D, M)
    row.update(e_ar=e_ar, e_t=e_t, e_s=e_s, lift=e_t - e_s,
               demand=-(e_ar + e_s),
               dev_at=max(abs(float(qa.sum()) - e_t)
                          / max(abs(e_t), 1e-30),
                          abs(float(qg.sum()) - e_s)
                          / max(abs(e_s), 1e-30)))
    cq = np.cumsum(qa)
    idxg = np.searchsorted(ug, uu, side="right")
    cg_all = np.concatenate([[0.0], np.cumsum(qg)])
    head_err = cq - cg_all[idxg]
    G = head_err - row["demand"]
    tail_A = row["lift"] - head_err
    cert_A = G - np.abs(tail_A)
    head_B = e_ar + cq
    tail_B = float(qa.sum()) - cq
    cert_B = head_B - np.abs(tail_B)
    smoothtail = float(qg.sum()) - cg_all[idxg]
    row.update(G=G, tail_A=tail_A, cert_A=cert_A, head_B=head_B,
               tail_B=tail_B, cert_B=cert_B, smoothtail=smoothtail,
               qa=qa)
    row["Gref"] = {}
    for nc in REF_CUTS:
        ucut = math.log(nc)
        he = (float(qa[uu <= ucut].sum())
              - float(qg[ug <= ucut].sum()))
        row["Gref"][nc] = he - row["demand"]
    if need_sm:
        ws, Vs = np.linalg.eigh(core.odd_toeplitz(c_ar + c_sm, M))
        vsm = Vs[:, 0]
        if float(v @ vsm) < 0:
            vsm = -vsm
        ov4 = [abs(float(v @ Vs[:, j])) for j in range(4)]
        jcar = int(np.argmax(ov4))
        vcar = Vs[:, jcar] * (1.0 if float(v @ Vs[:, jcar]) >= 0
                              else -1.0)
        row.update(ov=float(abs(v @ vsm)), ov4=ov4, jcar=jcar)
        row["Wsm"] = core.lag_weights_from_v(vsm, h)
        row["Wcar"] = core.lag_weights_from_v(vcar, h)
    row["Wv"] = Wv
    return row


# --------------------------------------------------------------- Abel
PSI_FULL = np.cumsum(core.LAM_TAB)                # psi(n) at index n
DEVPSI = np.abs(PSI_FULL - np.arange(len(PSI_FULL), dtype=float))
KAP = core.chebyshev_kappa()
# AMENDMENT A1 (disclosed): the deployed kappa is verified at the
# JUMP POINTS of psi(x)/x; the transport reads psi at ALL integers
# (the deficit side just before a jump is larger).  The envelope
# used is the ALL-INTEGER table constant on [100, ATOM_MAX] --
# same table, same finite verification class, strictly weaker
# (conservative) than the jump-point kappa.
KAPPA_INT = float(np.max(np.where(
    np.arange(len(PSI_FULL)) >= KAPPA_LOW_X,
    DEVPSI / np.maximum(np.arange(len(PSI_FULL), dtype=float),
                        1.0), 0.0)))


def bnd_psi(x):
    """The classical table envelope for |psi(x) - x| at integer
    x: KAPPA_INT x on [100, ATOM_MAX] (all-integer table
    verification, amendment A1), the table-verified exact
    deviation below 100."""
    x = np.asarray(x)
    return np.where(x >= KAPPA_LOW_X, KAPPA_INT * x.astype(float),
                    DEVPSI[np.minimum(x, KAPPA_LOW_X)])


def make_grid(row, nc):
    """The integer transport grid beyond the cut nc, with the
    cumulants A1..A3, the smooth counterpart, the exact psi/Riesz
    identity deviations, and the envelope bound ladder BE1..BE3."""
    alpha = row["alpha"]
    Ng = max(int(math.floor(row["X"])),
             int(np.round(math.exp(float(row["uu"][-1])))))
    kk = np.arange(nc + 1, Ng + 1, dtype=np.int64)
    kf = kk.astype(float)
    ug = np.log(kf)
    lamg = core.LAM_TAB[nc + 1:Ng + 1]
    inv_sq = 1.0 / np.sqrt(kf)
    a = 2.0 * lamg * inv_sq
    L = len(kk)
    A1 = blocked_cumsum(a)
    A2 = blocked_cumsum(A1)
    A3 = blocked_cumsum(A2)
    At1 = blocked_cumsum(2.0 * inv_sq)
    E1 = A1 - At1
    # (b) exact psi-Abel identity for A1, warded at every k
    delta = inv_sq[:-1] - inv_sq[1:]
    psiw = blocked_cumsum(lamg)
    Cpsi = np.concatenate([[0.0],
                           blocked_cumsum(psiw[:-1] * delta)])
    rhs = 2.0 * (psiw * inv_sq + Cpsi)
    dev_psi = float(np.max(np.abs(A1 - rhs))
                    / max(float(np.max(np.abs(A1))), 1.0))
    # (b) Riesz/Cesaro spot-wards for A2, A3 (frozen indices)
    dev_riesz = 0.0
    for i in ((L - 1) // 2, L - 1):
        c = kf[i] - kf[:i + 1] + 1.0
        d2 = float(np.dot(a[:i + 1], c))
        d3 = float(np.dot(a[:i + 1], c * (c + 1.0) / 2.0))
        dev_riesz = max(
            dev_riesz,
            abs(A2[i] - d2) / max(abs(A2[i]), 1.0),
            abs(A3[i] - d3) / max(abs(A3[i]), 1.0))
    # (c) the envelope bound ladder
    beta = bnd_psi(kk) + float(bnd_psi(np.array([nc]))[0])
    Cb = np.concatenate([[0.0],
                         blocked_cumsum(beta[:-1] * delta)])
    BE1 = 2.0 * (beta * inv_sq + Cb)
    BE2 = blocked_cumsum(BE1)
    BE3 = blocked_cumsum(BE2)
    env_min_slack = float(np.min(BE1 - np.abs(E1)))
    return dict(kk=kk, kf=kf, ug=ug, a=a, inv_sq=inv_sq, L=L,
                A1=A1, A2=A2, A3=A3, At1=At1, E1=E1,
                BE1=BE1, BE2=BE2, BE3=BE3,
                dev_psi=dev_psi, dev_riesz=dev_riesz,
                env_min_slack=env_min_slack, alpha=alpha)


def transport(grid, row, W):
    """Per-weight transport: w on the grid, the dual kernels
    D^r w, the exact Abel chain at orders 1..3 (warded), the
    smooth tail Ttilde and the envelope budgets ERR_1..3."""
    L = grid["L"]
    w = q_read(W, grid["ug"], row["D"], row["M"])
    dw1 = w[1:] - w[:-1]
    dw2 = dw1[1:] - dw1[:-1]
    dw3 = dw2[1:] - dw2[:-1]
    a = grid["a"]
    A1, A2, A3 = grid["A1"], grid["A2"], grid["A3"]
    T = float(np.dot(a, w))
    bdry = A1[L - 1] * w[L - 1]
    T1 = bdry - float(np.dot(A1[:L - 1], dw1))
    T2 = (bdry - A2[L - 2] * dw1[L - 2]
          + float(np.dot(A2[:L - 2], dw2)))
    T3 = (bdry - A2[L - 2] * dw1[L - 2]
          + A3[L - 3] * dw2[L - 3]
          - float(np.dot(A3[:L - 3], dw3)))
    sc1 = abs(bdry) + float(np.dot(np.abs(A1[:L - 1]),
                                   np.abs(dw1)))
    sc2 = (abs(bdry) + abs(A2[L - 2] * dw1[L - 2])
           + float(np.dot(np.abs(A2[:L - 2]), np.abs(dw2))))
    sc3 = (abs(bdry) + abs(A2[L - 2] * dw1[L - 2])
           + abs(A3[L - 3] * dw2[L - 3])
           + float(np.dot(np.abs(A3[:L - 3]), np.abs(dw3))))
    dev_abel = max(abs(T1 - T) / max(sc1, 1.0),
                   abs(T2 - T) / max(sc2, 1.0),
                   abs(T3 - T) / max(sc3, 1.0))
    Tt = float(np.dot(2.0 * grid["inv_sq"], w))
    BE1, BE2, BE3 = grid["BE1"], grid["BE2"], grid["BE3"]
    e_bdry = BE1[L - 1] * abs(w[L - 1])
    ERR1 = e_bdry + float(np.dot(BE1[:L - 1], np.abs(dw1)))
    ERR2 = (e_bdry + BE2[L - 2] * abs(dw1[L - 2])
            + float(np.dot(BE2[:L - 2], np.abs(dw2))))
    ERR3 = (e_bdry + BE2[L - 2] * abs(dw1[L - 2])
            + BE3[L - 3] * abs(dw2[L - 3])
            + float(np.dot(BE3[:L - 3], np.abs(dw3))))
    cens = [sign_census(dz, grid["ug"][:len(dz)], grid["alpha"])
            for dz in (dw1, dw2, dw3)]
    return dict(w=None, T=T, Tt=Tt, dev_abel=dev_abel,
                ERR=(ERR1, ERR2, ERR3), cens=cens)


def main():
    section("PRIME.PORT.TAIL.ABEL.01 -- the cumulative (Abel-"
            "transport) attack on the tail (EXPLORATION ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s"
          % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
    print("    NO RH claim; no marker moves; C0 = 1/2 is the CLI "
          "registration, NO-ADJUST.")
    print("\nS0 -- firewall")
    check("S0.1 AST firewall clean", not ast_scan(BANNED_IDS))

    # ------------------------------------------------------------ W
    section("W -- the faithful ladder + wards")
    rungs = []
    for kz in range(2, KZMAX + 1):
        row = build_rung(kz)
        if row is not None:
            rungs.append(row)
    rungs.sort(key=lambda r: (r["h"], r["kz"]))
    check("W1 faithful ladder >= %d rungs" % MIN_RUNGS,
          len(rungs) >= MIN_RUNGS,
          "%d rungs, h %d..%d  [%.1f s]"
          % (len(rungs), rungs[0]["h"], rungs[-1]["h"],
             time.time() - T0), kill="K1")
    if KILLS:
        return finish({})
    N = len(rungs)
    check("W2 WARD truth margin m_h > 0 on every rung (min %.3e)"
          % min(r["m"] for r in rungs),
          all(r["m"] > 0 for r in rungs), kill="K2")
    dev_bk = max(max(abs((r["lift"] - r["demand"]) - r["m"]),
                     abs((r["e_ar"] + r["e_t"]) - r["m"]))
                 / max(1.0, abs(r["m"])) for r in rungs)
    check("W3 WARD both exact bookkeepings: max dev %.2e <= %.0e"
          % (dev_bk, ID_WARD), dev_bk <= ID_WARD, kill="K2")
    dev_at = max(r["dev_at"] for r in rungs)
    check("W4 WARD atom identities (atom sum = E_at, PNT grid = "
          "E_sm): max rel dev %.2e <= %.0e" % (dev_at, ID_WARD),
          dev_at <= ID_WARD, kill="K2")
    dev_sc = 0.0
    for r in rungs:
        sc = max(float(np.max(np.abs((r["head_B"] + r["tail_B"])
                                     - r["m"]))),
                 float(np.max(np.abs((r["G"] + r["tail_A"])
                                     - r["m"]))),
                 float(np.max(np.abs(r["G"] - r["head_B"]
                                     - r["smoothtail"]))))
        dev_sc = max(dev_sc, sc / max(1.0, abs(r["e_t"])))
    check("W5 WARD split exactness on the full scans: max rel "
          "dev %.2e <= %.0e" % (dev_sc, SCAN_WARD),
          dev_sc <= SCAN_WARD, kill="K2")
    # round-59/60/62 reproduction
    cnts = tuple(int(np.sum(np.array(
        [r["Gref"][nc] for r in rungs]) > 0)) for nc in REF_CUTS)
    n_min, nB_min, icBs, tB_neg = [], [], [], 0
    for r in rungs:
        nn = np.round(np.exp(r["uu"])).astype(int)
        covA = r["cert_A"] > 0.0
        i0 = int(np.argmax(covA)) if bool(np.any(covA)) else -1
        n_min.append(int(nn[i0]) if i0 >= 0 else -1)
        covB = r["cert_B"] > 0.0
        icB = int(np.argmax(covB)) if bool(np.any(covB)) else -1
        icBs.append(icB)
        nB_min.append(int(nn[icB]) if icB >= 0 else -1)
        if icB >= 0 and float(r["tail_B"][icB]) <= 0.0:
            tB_neg += 1
    i9s = [int(np.searchsorted(r["uu"],
                               math.log(NC_SHARED) + 1e-12,
                               side="right")) - 1 for r in rungs]
    cov9 = sum(1 for r, i9 in zip(rungs, i9s)
               if i9 >= 0 and r["cert_A"][i9] > 0)
    tA_neg = sum(1 for r in rungs if bool(np.any(r["cert_A"] > 0))
                 and r["tail_A"][int(np.argmax(
                     r["cert_A"] > 0))] <= 0.0)
    covB_n = sum(1 for i in icBs if i >= 0)
    hBc = np.array([float(r["head_B"][i])
                    for r, i in zip(rungs, icBs)])
    medB = float(np.median([n for n in nB_min if n > 0]))
    ok_rep = (cnts == REF_COUNTS
              and all(NMIN_LO <= nm <= NMIN_HI for nm in n_min)
              and cov9 == N and tA_neg == N and covB_n == N
              and medB == NB_MED
              and min(nB_min) >= NB_LO and max(nB_min) <= NB_HI
              and tB_neg == N
              and abs(float(np.median(hBc)) - HEADB_MED)
              <= HEADB_TOL)
    check("W6 REPRODUCTION 59/60/62: G > 0 at %s = %s == %s; "
          "n_min in [%d, %d]; cut 9 covers %d/%d; tail_A <= 0 "
          "%d/%d; B-cuts exist %d/%d, n_minB med %d in [%d, %d]; "
          "tail_B <= 0 at cB %d/%d; head_B(cB) med %.3f ~ %.3f"
          % (REF_CUTS, cnts, REF_COUNTS, NMIN_LO, NMIN_HI, cov9,
             N, tA_neg, N, covB_n, N, int(medB), min(nB_min),
             max(nB_min), tB_neg, N, float(np.median(hBc)),
             HEADB_MED), ok_rep, kill="K2")
    n_cross = sum(1 for r in rungs if r["ov"] < OV_MIN)
    cross_ok = all(max(r["ov4"]) >= OV_MIN for r in rungs
                   if r["ov"] < OV_MIN)
    check("W7 WARD v_sm branch: %d crossing rung(s) (%s; ward <= "
          "%d), carrier ok"
          % (n_cross,
             ", ".join("kz%d ov %.4f" % (r["kz"], r["ov"])
                       for r in rungs if r["ov"] < OV_MIN)
             or "none", MAX_CROSS),
          n_cross <= MAX_CROSS and cross_ok, kill="K2")
    check("W8 WARD kappa: chebyshev_kappa() = %.6f within %.0e "
          "of %.6f (v563 S0.KAPPA, jump points; ALL-INTEGER "
          "table envelope KAPPA_INT = %.6f used for the bound, "
          "amendment A1; B_PSI = %.5f noted)"
          % (KAP, KAPPA_TOL, core.KAPPA_REF, KAPPA_INT,
             core.B_PSI),
          abs(KAP - core.KAPPA_REF) <= KAPPA_TOL, kill="K2")
    mu1 = np.array([float(core.parity_mu(r["h"])[0])
                    for r in rungs])
    mu1_cf = np.array([4.0 * math.sin(math.pi
                                      / (2 * r["h"] + 1)) ** 2
                       for r in rungs])
    dev_mu = float(np.max(np.abs(mu1 - mu1_cf)
                          / np.maximum(mu1, 1e-300)))
    mm = np.array([r["m"] for r in rungs])
    shat = mm / mu1
    s3 = (float(np.min(shat)), float(np.median(shat)),
          float(np.max(shat)))
    ok_shat = all(abs(s3[i] - SHAT_REF[i]) <= SHAT_TOL
                  for i in range(3))
    check("W9 WARD mu1 closed form (dev %.1e) + CXLIII shat band "
          "min/med/max %.4f/%.4f/%.4f ~ %s"
          % (dev_mu, s3[0], s3[1], s3[2], SHAT_REF),
          dev_mu <= MU_WARD and ok_shat, kill="K2")
    if KILLS:
        return finish({})

    # ---------------------------------------------- the transports
    grids, trv, trs = [], [], []
    for r, icB, nc in zip(rungs, icBs, nB_min):
        g = make_grid(r, nc)
        grids.append(g)
        trv.append(transport(g, r, r["Wv"]))
        Ws = r["Wcar"] if r["ov"] < OV_MIN else r["Wsm"]
        trs.append(transport(g, r, Ws))
    tie = max(abs(t["T"] - float(r["tail_B"][i]))
              / max(1.0, abs(float(r["tail_B"][i])))
              for t, r, i in zip(trv, rungs, icBs))
    check("W10 WARD grid tie: integer-grid tail == tail_B(cB) "
          "max rel dev %.2e <= %.0e  [%.1f s]"
          % (tie, TIE_WARD, time.time() - T0),
          tie <= TIE_WARD, kill="K2")
    env_slk = min(g["env_min_slack"] for g in grids)
    check("W11 WARD envelope in-window: |E1| <= BE1 everywhere "
          "on every rung (min slack %+.3e >= %.0e)"
          % (env_slk, -ENV_SLACK), env_slk >= -ENV_SLACK,
          kill="K2")
    if KILLS:
        return finish({})

    # ------------------------------------------------------------ A
    section("A -- (a) THE DUAL KERNEL SIGN LADDER: D^r w on the "
            "deep integer grid, r = 1, 2, 3")
    print("    q_{v_sm} is PRIME-FREE; its integer-grid "
          "differences are a purely classical object.  Zero "
          "threshold %.0e * max|D^r w| (declared)." % SIGN_EPS)
    lab_a = None
    fix_r = 0
    for name, trl in (("v (arithmetic)", trv),
                      ("v_sm (prime-free)", trs)):
        for ri in range(3):
            cc = [t["cens"][ri] for t in trl]
            n_single = sum(1 for c in cc if c["single"])
            chg = np.array([c["n_changes"] for c in cc])
            dom = np.array([c["dom"] for c in cc])
            xl = np.array([c["x_last"] for c in cc])
            xl = xl[np.isfinite(xl)]
            sgn = np.array([c["sign"] for c in cc])
            print("    %-18s r=%d: single-signed %2d/%d; sign "
                  "changes med %4d (%d..%d); dominant share med "
                  "%.3f (sign - on %d/%d); last change x = u/"
                  "(2a) med %.3f"
                  % (name, ri + 1, n_single, N,
                     int(np.median(chg)), int(chg.min()),
                     int(chg.max()), float(np.median(dom)),
                     int(np.sum(sgn < 0)), N,
                     float(np.median(xl)) if len(xl)
                     else float("nan")), flush=True)
            if (name.startswith("v_sm") and n_single == N
                    and fix_r == 0):
                fix_r = ri + 1
                lab_a = ("DUALSIGN-FIXED(r=%d, %d/%d, sign %+d)"
                         % (fix_r, n_single, N,
                            int(np.sign(np.sum(sgn)))))
    if lab_a is None:
        best = max(range(3), key=lambda ri: sum(
            1 for t in trs if t["cens"][ri]["single"]))
        nb = sum(1 for t in trs if t["cens"][best]["single"])
        lab_a = ("DUALSIGN-OPEN(best r=%d: %d/%d single; med "
                 "changes r1/r2/r3 = %d/%d/%d)"
                 % (best + 1, nb, N,
                    int(np.median([t["cens"][0]["n_changes"]
                                   for t in trs])),
                    int(np.median([t["cens"][1]["n_changes"]
                                   for t in trs])),
                    int(np.median([t["cens"][2]["n_changes"]
                                   for t in trs]))))
        print("    ==> NO order r <= 3 fixes the dual kernel's "
              "sign: the residual sign-change census above IS "
              "the named obstruction of the cumulative route")
    check("A.1 typed (a): %s" % lab_a, True)

    # ------------------------------------------------------------ B
    section("B -- (b) THE ABEL IDENTITY CHAIN + the arithmetic "
            "identity of A^{(r)} (WARDS)")
    dev_ab = max(t["dev_abel"] for t in trv + trs)
    check("B.1 WARD Abel chain exact at orders 1..3, both "
          "weights, all rungs: max rel dev %.2e <= %.0e"
          % (dev_ab, ABEL_WARD), dev_ab <= ABEL_WARD, kill="K2")
    dev_ps = max(g["dev_psi"] for g in grids)
    check("B.2 WARD psi-Abel identity (A1 = windowed psi-type "
          "partial sum, exact at every k): max rel dev %.2e <= "
          "%.0e" % (dev_ps, PSI_ID_WARD),
          dev_ps <= PSI_ID_WARD, kill="K2")
    dev_rz = max(g["dev_riesz"] for g in grids)
    check("B.3 WARD Riesz/Cesaro identity (A^{(r)}(k) = 2 sum "
          "binom(k-n+r-1, r-1) Lambda(n)/sqrt(n), r = 2, 3, "
          "frozen spot indices): max rel dev %.2e <= %.0e"
          % (dev_rz, RIESZ_WARD), dev_rz <= RIESZ_WARD,
          kill="K2")
    print("    ==> A^{(1)} = smoothed (1/sqrt) prime counting "
          "in the window; A^{(2)} = its Riesz mean (integrated "
          "psi-type); A^{(3)} = twice integrated -- verified as "
          "EXACT identities, not asymptotics")
    lab_b = ("ABEL-EXACT(%.1e) + ARITH-ID(psi %.1e, riesz %.1e)"
             % (dev_ab, dev_ps, dev_rz))
    if KILLS:
        return finish({})

    # ------------------------------------------------------------ E
    section("E -- (c) THE ENVELOPE CERTIFICATE (decisive): does "
            "the classical table envelope (KAPPA_INT = %.6f) "
            "close the tail on the surface?" % KAPPA_INT)
    H = hBc
    Tarr = np.array([t["T"] for t in trv])
    Tt = np.array([t["Tt"] for t in trv])
    ERR = np.array([t["ERR"] for t in trv])       # (N, 3)
    slack = ((H + Tt - ERR.T) / mu1 - C0).T       # (N, 3)
    slack_best = slack.max(axis=1)
    best_r = slack.argmax(axis=1) + 1
    chat = (H + Tt) / mu1
    rhat = (Tarr - Tt) / mu1
    ovsh = ERR.min(axis=1) / np.maximum(np.abs(Tarr - Tt), 1e-300)
    st_cB = np.array([float(r["smoothtail"][i])
                      for r, i in zip(rungs, icBs)])
    print("    kz   h    m_h       mu1       nc  H+Tt/mu1   "
          "(T-Tt)/mu1  ERR1/mu1   ERR2/mu1   ERR3/mu1   slack")
    for i, r in enumerate(rungs):
        print("    %-4d %-4d %.3e %.3e %-3d %+.3e %+.3e %.3e "
              "%.3e %.3e %+.3e"
              % (r["kz"], r["h"], r["m"], mu1[i], nB_min[i],
                 chat[i], rhat[i], ERR[i, 0] / mu1[i],
                 ERR[i, 1] / mu1[i], ERR[i, 2] / mu1[i],
                 slack_best[i]), flush=True)
    n_pos = int(np.sum(slack_best > 0.0))
    cnt_r = [int(np.sum(best_r == ri)) for ri in (1, 2, 3)]
    print("\n    best order census r=1/2/3: %d/%d/%d; envelope "
          "budget ERR_best/mu1 min/med/max %.2e/%.2e/%.2e"
          % (cnt_r[0], cnt_r[1], cnt_r[2],
             float(np.min(ERR.min(axis=1) / mu1)),
             float(np.median(ERR.min(axis=1) / mu1)),
             float(np.max(ERR.min(axis=1) / mu1))))
    print("    MEASURED arithmetic remainder (T - Ttilde)/mu1 "
          "min/med/max %+.2f/%+.2f/%+.2f; envelope OVERSHOOT "
          "ERR_best/|T - Ttilde| med %.2e -- the budget vs the "
          "actual oscillating sum"
          % (float(np.min(rhat)), float(np.median(rhat)),
             float(np.max(rhat)), float(np.median(ovsh))))
    print("    integer smooth tail vs round-60 continuum "
          "smoothtail(cB): med |Ttilde - st| = %.2e (Euler-"
          "Maclaurin tie, info)"
          % float(np.median(np.abs(Tt - st_cB))))
    aa = np.array([r["alpha"] for r in rungs])
    if n_pos == N:
        slE, seE, r2E = jack_slope(aa, np.log(slack_best))
        lab_e = "ENV-SUFFICIENT(min slack %+.3e)" % float(
            np.min(slack_best))
        print("    ==> THE TAIL STATEMENT CLOSES CLASSICALLY ON "
              "THE SURFACE: H + Ttilde - ERR >= %.1f mu1 on "
              "%d/%d rungs (min slack %+.3e; KAPPA_INT = %.6f, "
              "C0 = %.1f frozen)" % (C0, n_pos, N,
                                     float(np.min(slack_best)),
                                     KAPPA_INT, C0))
    else:
        gap = ERR.min(axis=1) / mu1
        slE, seE, r2E = jack_slope(aa, np.log(gap))
        lab_e = ("ENV-INSUFFICIENT(slack min/med %+.2e/%+.2e, "
                 "gap law %+.3f)"
                 % (float(np.min(slack_best)),
                    float(np.median(slack_best)), slE))
        print("    ==> ENVELOPES INSUFFICIENT on %d/%d rungs: "
              "GAP LAW log(ERR_best/mu1) = %+.3f alpha + c "
              "(2SE %.3f, R^2 %.2f) -- the classical budget "
              "grows ~ e^{%.2f alpha} while the need chat - %.1f "
              "is O(1)"
              % (N - n_pos, N, slE, 2 * seE, r2E, slE, C0))
    check("E.1 typed (c): %s (per-order slacks valid "
          "certificates each; slack_best = max_r)" % lab_e, True)

    # ------------------------------------------------------------ N
    section("N -- (d) THE NORMALIZED CONSTANT vs the frozen "
            "1/2 (recorded, NO adjustment)")
    n_ch = int(np.sum(chat >= C0))
    print("    chat = (H + Ttilde)/mu1: min/med/max %.3f/%.3f/"
          "%.3f; chat > 0 on %d/%d; chat >= %.1f on %d/%d"
          % (float(np.min(chat)), float(np.median(chat)),
             float(np.max(chat)), int(np.sum(chat > 0)), N, C0,
             n_ch, N))
    print("    rhat = (T - Ttilde)/mu1: min/med/max %+.3f/%+.3f/"
          "%+.3f  (the arithmetic remainder the envelope must "
          "control; shat = chat + rhat, warded band above)"
          % (float(np.min(rhat)), float(np.median(rhat)),
             float(np.max(rhat))))
    print("    recorded comparison to the CLI halfgap: shat - "
          "1/2 min %+.2e (registration margin); the smooth-"
          "certified part chat clears 1/2 on %d/%d -- NO "
          "constant is moved" % (float(np.min(shat - C0)), n_ch,
                                 N))
    lab_n = ("CHAT(%.2f/%.2f/%.2f, >=1/2 on %d/%d)"
             % (float(np.min(chat)), float(np.median(chat)),
                float(np.max(chat)), n_ch, N))
    check("N.1 typed (d): %s" % lab_n, True)

    # ------------------------------------------------------------ T
    section("T -- (e) TAU-SCREENS (jackknife, typed)")
    okc = chat > 0
    slC, seC, r2C = jack_slope(np.log(mm[okc]),
                               np.log(chat[okc]))
    scr_c = ("PASS" if abs(slC) <= SLOPE_PASS else
             "RELOC" if slC >= SLOPE_RELOC else "AMBIG")
    print("    screen log chat vs log m (on %d/%d with chat > 0"
          "%s): slope %+.3f +- 2SE %.3f (R^2 %.2f) -> %s"
          % (int(np.sum(okc)), N,
             "" if bool(np.all(okc)) else " -- subset disclosed",
             slC, 2 * seC, r2C, scr_c))
    gap = ERR.min(axis=1) / mu1
    slG, seG, r2G = jack_slope(np.log(mm), np.log(gap))
    scr_g = ("PASS" if abs(slG) <= SLOPE_PASS else
             "RELOC" if slG >= SLOPE_RELOC else "AMBIG")
    print("    screen log(ERR_best/mu1) vs log m: slope %+.3f "
          "+- 2SE %.3f (R^2 %.2f) -> %s"
          % (slG, 2 * seG, r2G, scr_g))
    lab_t = ("SCREENS(chat %+.2f %s, gap %+.2f %s)"
             % (slC, scr_c, slG, scr_g))
    check("T.1 typed (e): %s" % lab_t, True)

    # ------------------------------------------------------------ C
    section("C -- controls on this surface at kz %d" % CTRL_KZ)
    rr9 = core.build_window(CTRL_KZ)
    N_E = int(math.floor(math.exp(2.0 * rr9["alpha"]))) + 1
    lamE_ = lambda_eps(N_E)
    nnE = np.nonzero(np.abs(lamE_) > 1e-12)[0]
    ctl = {}
    ctl["Epstein"] = build_rung(CTRL_KZ, comb=(
        np.log(nnE.astype(float)),
        2.0 * lamE_[nnE] / np.sqrt(nnE.astype(float))),
        need_sm=False)
    ctl["scramble"] = build_rung(CTRL_KZ, scramble_seed=1,
                                 need_sm=False)
    ctl["smooth"] = build_rung(CTRL_KZ, smooth_world=True,
                               need_sm=False)
    fired = True
    for name, r in ctl.items():
        if r is None:
            print("    %-9s: rung dies -> fires" % name)
            continue
        ncovA = int(np.sum(r["cert_A"] > 0))
        ncovB = int(np.sum(r["cert_B"] > 0))
        f = (r["m"] < 0) and ncovA == 0 and ncovB == 0
        fired &= f
        print("    %-9s: m %+.3e  covering cuts A/B %d/%d -> %s"
              % (name, r["m"], ncovA, ncovB,
                 "FIRES" if f else "SILENT"), flush=True)
    check("C1 WARD all three controls fire (m < 0 and zero "
          "coverage in BOTH senses)", fired, kill="K2")
    # C2 -- the envelope battery from the fixed cut CTRL_CUT
    facs = {}
    for name in ("Epstein", "smooth", "scramble"):
        r = ctl[name]
        Ng = int(math.floor(r["X"]))
        kk = np.arange(CTRL_CUT + 1, Ng + 1, dtype=np.int64)
        kf = kk.astype(float)
        inv_sq = 1.0 / np.sqrt(kf)
        delta = inv_sq[:-1] - inv_sq[1:]
        beta = (bnd_psi(kk)
                + float(bnd_psi(np.array([CTRL_CUT]))[0]))
        Cb = np.concatenate(
            [[0.0], blocked_cumsum(beta[:-1] * delta)])
        BE1 = 2.0 * (beta * inv_sq + Cb)
        At1 = blocked_cumsum(2.0 * inv_sq)
        if name == "scramble":
            cmass = np.concatenate([[0.0],
                                    blocked_cumsum(r["mu"])])
            idx = np.searchsorted(r["uu"], np.log(kf),
                                  side="right")
            i0 = int(np.searchsorted(
                r["uu"], math.log(CTRL_CUT) + 1e-12,
                side="right"))
            A1c = cmass[idx] - cmass[i0]
        else:
            nn = np.round(np.exp(r["uu"])).astype(int)
            ag = np.zeros(Ng + 1)
            keep = nn <= Ng
            np.add.at(ag, nn[keep], r["mu"][keep])
            A1c = blocked_cumsum(ag[CTRL_CUT + 1:Ng + 1])
        facs[name] = float(np.max(np.abs(A1c - At1) / BE1))
        print("    %-9s envelope factor max |E1|/BE1 = %.3g"
              % (name, facs[name]), flush=True)
    check("C2 WARD scramble violates the classical envelope: "
          "factor %.3g >= %.1f (cumulative structure destroyed)"
          % (facs["scramble"], CTRL_VIOL),
          facs["scramble"] >= CTRL_VIOL, kill="K2")
    lab_c = ("CTRL-ENV(scramble %.2g FIRES, smooth %.2g%s, "
             "Epstein %.2g %s -- measured, typed)"
             % (facs["scramble"], facs["smooth"],
                " <= 1 as declared" if facs["smooth"] <= 1.0
                else " > 1 (recorded)", facs["Epstein"],
                "inside" if facs["Epstein"] <= 1.0 else
                "OUTSIDE"))
    check("C3 typed control battery: %s" % lab_c, True)

    return finish(dict(a=lab_a, b=lab_b, e=lab_e, n=lab_n,
                       t=lab_t, c=lab_c))


def finish(labels):
    section("V -- FROZEN VERDICT")
    n_pass = sum(1 for _n, okk in CHECKS if okk)
    n_tot = len(CHECKS)
    if KILLS:
        VERDICT = {"K1": "PIPELINE-BROKEN",
                   "K2": "WARD-BROKEN"}[KILLS[0]]
        print("\n  VERDICT: %s" % VERDICT)
    else:
        VERDICT = ("TAILABEL-MEASURED / %(a)s / %(b)s / %(e)s / "
                   "%(n)s / %(t)s / %(c)s" % labels)
        print("\n  VERDICT: %s" % VERDICT)
    print("""
  HONEST FRAME (as frozen): the Abel chain and the arithmetic
  identity of the cumulants are EXACT bookkeeping; the dual-kernel
  sign census, the envelope slack ladder and the normalized
  constant are MEASURED SURFACE STRUCTURE at float level.  An
  insufficient envelope is a measured gap law, not an
  impossibility proof; a sufficient one would still be a per-rung
  surface certificate, not a theorem.  The halfgap constant 1/2
  (CLI) is never adjusted here.  NO RH claim.  No marker moves.""")
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed"
          % (time.time() - T0, n_tot, n_tot - n_pass))
    return 0 if n_pass == n_tot else 1


if __name__ == "__main__":
    raise SystemExit(main())
