#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""tail_segment_split_probe -- PRIME.PORT.TAIL.SEGSPLIT.01
(EXPLORATION ONLY, experiments/; round 63, theorem-engineering on
the RH-side wall, probe 4 -- the SEGMENT-SPLIT attack on the
tail, direct successor of PRIME.PORT.TAIL.ABEL.01 (note CLII).
What the predecessor left: the Abel transport of the B-cover tail
onto the integer grid is EXACT (1e-15 class) and the cumulants
are named psi/Riesz objects; NO order r <= 3 fixes the dual
kernel sign globally (census med 3/363/1113 for r = 1/2/3); the
honest all-integer classical envelope (KAPPA_INT = 0.059547,
amendment A1 there) is insufficient GLOBALLY on 67/67 with gap
law e^{+1.744 alpha} (slack med -1.5e5 mu1) -- the missing
ingredient is oscillation bookkeeping, not constants; BUT the
r = 1 dual kernel is NEARLY single-signed: 2..3 deep sign
changes per rung, negative-dominant on 67/67, and the change
positions are CLASSICAL (prime-free -- q_{v_sm} reproduces the
census).  THE FROZEN IDEA: split the deep window at the r = 1
dual kernel's finitely many breakpoints into segments of fixed
kernel sign.  On each segment the transported tail pairs a
SEGMENT-LOCAL cumulative prime mass B_j(k) >= 0 against a
single-signed kernel, so the needed windowed-psi control per
segment is ONE-SIDED -- and on negative-kernel segments the
pairing is NONNEGATIVE EXACTLY (a free floor).  The global
oscillation bookkeeping decomposes into (i) per-segment
one-sided windowed psi statements plus (ii) boundary terms
reading the cumulative mass at the 2..3 classical breakpoints.
2026-08-11.)

THE SEGMENT IDENTITY (frozen).  Grid, masses, cumulants A1/At1/
E1, envelope table machinery, ladder and wards verbatim from the
predecessor (cut nc = n_minB(h); grid k = nc+1 .. N_g; masses
a_k = 2 Lambda(k)/sqrt(k); weight w = q_v on the grid; dual
kernel Dw(k) = w_{k+1} - w_k).  SEGMENTS: maximal runs of fixed
strict sign of Dw among entries with |Dw| > SIGN_EPS max|Dw|
(sub-threshold entries join the current segment -- the identical
threshold semantics as the predecessor's census; segments are
taken from the TRUE kernel q_v so the fixed sign is exact by
construction, and their CLASSICALITY is verified against
q_{v_sm} in (a)).  With segments j = 1..p, [s_j, e_j]
partitioning the Dw-index range, right breakpoints b_{j+1} =
s_{j+1} (b_{p+1} = the last grid point) and segment masses
m_j = A1(e_j) - A1(s_j - 1) (A1(-1) = 0):
  T = sum_j [ m_j w(b_{j+1}) - sum_{k in seg j} B_j(k) Dw(k) ],
  B_j(k) = A1(k) - A1(s_j - 1) >= 0
-- the telescoped regrouping of the order-1 Abel form: each
segment contributes ONE boundary read (its cumulative mass at
its right breakpoint) plus an in-segment pairing of the
segment-local cumulant against the single-signed kernel.  The
raw per-segment boundary terms bt_j = -A1(s_j - 1)(w(e_j + 1) -
w(s_j)) are measured separately for the telescoping census (d).

WHAT IS MEASURED (frozen; typed, never kills unless marked WARD):
 (a) BREAKPOINT CENSUS: per rung, the segment count and the
     breakpoint positions x = u/(2 alpha) from BOTH kernels
     (q_v true; q_{v_sm} prime-free, crossing rungs on their
     carrier branch as in round 62): count histogram, per-rung
     count agreement v vs v_sm, max matched-position deviation
     |dx| where counts agree, first/last position medians, drift
     law: jackknife slope of the LAST breakpoint position vs
     alpha (and the first; CXLVIII expectation: flat), dominant
     sign share (negative-dominant expectation 67/67).  Typed
     BP-CENSUS(...) + CLASSICAL-BP(match n/N, med/max |dx|).
 (b) EXACT SEGMENT IDENTITY (WARD): the telescoped identity
     above vs T = sum a_k w_k on every rung, relative to the
     declared term scale sum_j (|m_j w_b| + sum |B_j Dw|), ward
     <= SEG_ID_WARD; the same identity on the SMOOTH masses
     (At1/Bt_j) vs Ttilde = sum (2/sqrt(k)) w_k, ward <=
     SEG_ID_WARD; the regrouping ward: sum_j bt_j + A1(N) w_N ==
     sum_j m_j w(b_{j+1}) exactly (same scale).
 (c) ONE-SIDED DEMAND + SEGMENT-WISE ENVELOPE (decisive): on
     segment j with sign sigma_j the error term is -sum E_j Dw,
     E_j(k) = E1(k) - E1(s_j - 1) the SEGMENT-ANCHORED windowed
     psi deviation (the windowed psi sum starts at the segment,
     not at the cut): sigma_j = -1 needs ONLY the lower side
     E_j >= -BE_j (the windowed psi mass may not UNDERSHOOT),
     sigma_j = +1 needs ONLY the upper side E_j <= +BE_j.  The
     provable segment envelope (same argument as the
     predecessor's, anchored at the segment start):
       |E_j(k)| <= BE_j(k) = 2 [ beta_j(k)/sqrt(k)
                    + sum_{m=s_j}^{k-1} beta_j(m) delta_m ],
       beta_j(m) = bnd(m) + bnd(n(s_j) - 1),
     bnd = the all-integer table bound (KAPPA_INT x above 100,
     exact table deviations below; predecessor amendment A1
     adopted as deployed here), warded in-window on every
     segment of every rung (WARD).  Segment certificates:
       env_j  = sum BE_j |Dw|,   ts_j = -sum Bt_j Dw,
       cert_j = ts_j - env_j;
     on sigma_j = -1 additionally the EXACT floor: the pairing
     t_j = -sum B_j Dw >= floor_j = -sum_{off} (Bt_j + BE_j) Dw
     over the sub-threshold off-sign entries (tiny, disclosed),
     cert_j = max(ts_j - env_j, floor_j).  Boundary reads:
     m_j = mt_j + (E1(e_j) - E1(s_j-1)), |.| <= BE_j(e_j):
       b_cert_j = mt_j w(b) - BE_j(e_j) |w(b)|.
     Tabulated per rung: per-segment sign, required direction,
     measured one-sided margin min(BE_j -+ E_j), t_j/ts_j/env_j/
     cert_j in mu1 units (full table on the three frozen sample
     rungs, first/mid/deepest; compact per-rung line for all).
 (d) BOUNDARY TERMS: sizes |m_j w_b|/mu1, signs, the raw-form
     telescoping ratio |sum bt_j| / sum |bt_j|, the boundary
     envelope cost sum BE_j(e_j)|w_b|/mu1 (are the 2..3
     classical reads cheap against the in-segment budgets?).
 (e) ASSEMBLY (decisive): T_cert = sum_j (b_cert_j + cert_j),
     ERRseg_eff = Ttilde - T_cert >= 0 (the effective segment-
     route budget), slack_seg = (H + T_cert)/mu1 - C0 with H =
     head_B(cB), mu1 = 4 sin^2(pi/(2h+1)), C0 = 1/2 (CLI
     registration, NO-ADJUST, recorded comparison only).  Typed
     SEGENV-SUFFICIENT(min slack) iff slack_seg > 0 on ALL rungs
     (then the surface theorem shape T >= -H + c0 mu1 is stated
     with explicit constants and c0 = min (H + T_cert)/mu1
     recorded vs the frozen 1/2); else SEGENV-INSUFFICIENT
     (min/med slack, residual gap law: jackknife slope of
     log(ERRseg_eff/mu1) vs alpha, compared to the predecessor's
     global +1.744 -- recorded), plus the CARRIER census: per
     rung the segment with the largest certified deficit share
     cost_j = BE_j(e_j)|w_b| + (ts_j - cert_j) (index, sign,
     terminal?, position), and the GAIN ledger ERR_best(global,
     predecessor form) / ERRseg_eff min/med/max.  Floor usage
     census (how often the exact nonnegativity floor beats the
     envelope certificate).
 (f) TAU-SCREENS (typed, jackknife, bands PASS |s| <= 0.30 /
     RELOC s >= 0.70 / else AMBIG): log(ERRseg_eff/mu1) vs
     log m; log(sum_j |m_j w_b|/mu1) vs log m; log(gain) vs
     log m.

FROZEN PROTOCOL (ladder machinery verbatim from
tail_abel_transport_probe.py = round-59/60/62/63 chain):

 W   LADDER + WARDS W1-W11 verbatim from the predecessor
     (faithful ladder, both exact bookkeepings, atom identities,
     scan splits, round-59/60/62 reproduction incl. n_minB med
     17 and head_B(cB) med 0.388, v_sm carrier branch, kappa
     reproduction + KAPPA_INT, mu1 closed form + CXLIII shat
     band, grid tie T == tail_B(cB), global envelope in-window
     |E1| <= BE1).  Kills -> PIPELINE-BROKEN / WARD-BROKEN.

 A/B/D/E/T  as (a)/(b)/(d)/(c)+(e)/(f) above.  New WARDS: B.1
     segment identity, B.2 smooth segment identity, B.3
     regrouping, B.4 segment envelope in-window (all segments,
     all rungs), B.5 certificate order T_cert <= T (float slack).

 C   CONTROLS at kz 9 (kill -> WARD-BROKEN if silent): C1
     scramble (seed 1), Epstein x^2+5y^2, smooth comb: m < 0 AND
     zero covering cuts in BOTH senses (predecessor verbatim).
     C2 GLOBAL envelope battery from the fixed cut CTRL_CUT = 17
     (predecessor verbatim): scramble must violate the classical
     envelope by >= CTRL_VIOL = 5 (kill if silent); smooth /
     Epstein factors typed.  C3 SEGMENT battery (typed, no
     kill): each control's own integer-grid kernel is segmented
     by the same rule and the SEGMENT-ANCHORED envelope factor
     max |E_j|/BE_j is measured per control -- expectation
     declared: scramble largest (structure destroyed), smooth
     <= 1 (quadrature only), Epstein typed either way; if the
     scramble sits INSIDE all segment envelopes that is a
     first-class finding against the segment route's
     discriminating power, said prominently.

KILLS: K1 ladder (W1) -> PIPELINE-BROKEN; K2 wards (W2-W11,
B.1-B.5, C1, C2-scramble) -> WARD-BROKEN.  All typed A/D/E/T/C3
outcomes are measurements, never kills.

VERDICT (frozen enum): SEGSPLIT-MEASURED with typed sublabels
BP-CENSUS(...) + CLASSICAL-BP(...), SEG-ID-EXACT(...),
BDRY(...), SEGENV-SUFFICIENT(...)/SEGENV-INSUFFICIENT(...) +
GAIN(...), SCREENS(...), CTRL-SEG(...); else PIPELINE-BROKEN /
WARD-BROKEN.

FROZEN BARS (predecessor values verbatim unless new): KZMAX =
150; MIN_RUNGS = 40; REF_CUTS = (50, 100, 200); REF_COUNTS =
(52, 26, 25); NMIN_LO, NMIN_HI = 3, 9; NC_SHARED = 9; NB_MED =
17; NB_LO, NB_HI = 5, 47; HEADB_MED = 0.388, HEADB_TOL = 0.01;
SHAT_REF = (0.502, 1.027, 2.185), SHAT_TOL = 1.5e-3; ID_WARD =
1e-10; SCAN_WARD = 1e-9; TIE_WARD = 1e-10; ENV_SLACK = 1e-9;
KAPPA_TOL = 1e-6; MU_WARD = 1e-12; NG_SMOOTH = 6000; OV_MIN =
0.8; MAX_CROSS = 2; SIGN_EPS = 1e-15 (relative); C0 = 1/2
(frozen, NO-ADJUST, recorded comparison only); SLOPE_PASS =
0.30; SLOPE_RELOC = 0.70; CTRL_KZ = 9; CTRL_CUT = 17; CTRL_VIOL
= 5.0; KAPPA_LOW_X = 100; BLOCK = 1024; scramble seed 1;
jackknife = full leave-one-out, CI = +- 2SE.  NEW: SEG_ID_WARD =
1e-12 (relative to the declared term scale); SEG_ENV_SLACK =
1e-9; CERT_ORD_WARD = 1e-9 (relative); SAMPLE = (first, mid,
deepest) rung indices (0, N//2, N-1); breakpoint position x =
u(s_j)/(2 alpha) read at the segment-start grid index;
GAIN_EPS = 1e-300 guards on ratios/logs (declared).

SMOKE-RUN DISCLOSURE (2026-08-11, before freezing): ONE smoke
run (SPEC v0), 23/24 checks green, 18.9 s; the single failure
was a MECHANICAL format-string bug in the C3 control label
(missing Epstein argument -- fixed for v1, disclosed here; no
measurement, bar, band, enum or rule was touched, all
measurements had already completed and printed).  The smoke
facts are frozen here as the context the frozen run must
confirm.  (i) BREAKPOINTS: the true kernel splits into med 4
segments (histogram {3: 24, 4: 42, 5: 1}, pattern med +-+-),
negative-dominant 67/67 (mass share med 0.766); x_first med
0.313 with drift -0.1103/alpha (R^2 0.58, migrates inward),
x_last med 0.827 FLAT (+0.0004, R^2 0.00); classicality: count
agreement v vs v_sm on 49/67 only (the true kernel carries
extra arithmetic micro-crossings the prime-free kernel lacks),
matched-position |dx| med 0.0397 max 0.1146 -- the DEEP
breakpoints are classical positions, the count itself is not
fully prime-free.  (ii) IDENTITIES: segment identity 3.5e-16,
smooth twin 6.1e-16, regrouping 5.8e-17, segment envelopes
in-window everywhere (min slack -1.0e-15), T_cert <= T
everywhere.  (iii) THE DECISIVE MEASUREMENT -- the segment
split is a clean NEGATIVE with a sharp mechanism: slack min/med
-4.69e+06/-2.17e+05, positive on 0/67, residual law +1.824
alpha (2SE 0.194, R^2 0.80) ~ the predecessor's global +1.744;
GAIN med 0.694 (min 0.555, max 0.957) -- the segment-wise
budget is WORSE than the global one on 67/67, because the
segment anchor adds bnd(n_anchor) ~ KAPPA_INT n_anchor to
beta_j at EVERY point of the segment and the classical
breakpoints sit deep (the anchor penalty dominates the
one-sided saving, which is numerically ZERO for a symmetric
envelope); the free nonnegativity floor fires on only 1/135
negative segments (their envelope certificates are already
positive -- the floor is redundant where it holds); one-sided
demand census 135 lower / 110 upper, measured one-sided margin
min -0.000 (one saturated read at a segment start, within
float slack of the ward) med 0.318.  (iv) CARRIER: NOT the
terminal lobe (0/67) -- the deficit carrier is the INTERIOR
segment (onset x med 0.572, positive-sign on 43/67; the
mid-window +segment or the long -segment before it), i.e. the
budget lives where |Dw| mass meets deep anchors, not at the
last lobe.  (v) BOUNDARY: reads med -2.29e+05 mu1 (large and
NEGATIVE -- w < 0 at the deep breakpoints), envelope cost of
the reads med 6.45e+04 mu1 = a subdominant but non-negligible
fraction of ERRseg med 2.29e+05 mu1; raw telescoping ratio med
0.214 (adjacent raw boundary terms DO cancel ~5x).  (vi)
SCREENS: budget -1.242 AMBIG, boundary -1.194 AMBIG (both
anti-correlated exactly as the predecessor's), gain +0.034 PASS
(R^2 0.13) -- the split's cost factor is tau-FLAT: it neither
helps nor hurts where the margin shrinks.  (vii) CONTROLS: C1
3/3, C2 scramble 5.99 >= 5 FIRES, smooth 0.837, Epstein 7.51
(predecessor-verbatim); C3 segment battery: scramble 4.15
DISCRIMINATES (15 segments), Epstein 34.6, smooth 2.93 -- the
declared smooth <= 1 expectation is VIOLATED (recorded, typed,
no kill as frozen): the segment-anchored read is a single-
integer-point object near the segment start where the round-
snap quadrature error of the smooth comb exceeds the local
envelope -- an honest limit of the anchored form, not a
scramble-class violation.  AMENDMENT LEDGER: the C3 label
format fix above is the ONLY change after the smoke; no bar,
band, tolerance, enum or rule moved.

SPEC v1 (2026-08-11, frozen + SHA-hashed before the frozen
run): everything above.  Mechanical concretizations frozen:
(i) segment splitting is index-exact on the Dw array (length
L-1); (ii) the first segment's anchor is the cut itself
(A1(-1) = 0, beta_1 = predecessor's global beta -- BE_1 == BE1
restricted, a consistency tie); (iii) sigma_j = 0 (all-
sub-threshold segment) is handled as two-sided (no floor),
disclosed if it ever occurs; (iv) controls C3 read their
integer-grid masses exactly as the predecessor's C2 (round-snap
for smooth/Epstein, searchsorted cumulative for scramble) and
segment their OWN kernel from the fixed cut; (v) runtime ~ 45 s
(67 eigh pairs + full-grid segment envelopes dominate).

NO-GO COMPLIANCE (frozen): no certified-bound retry, no rank-1
approximation, no Herglotz; no fit where an identity is claimed
(the segment identity, its smooth twin, the regrouping and the
segment envelope bound are exact wards; all trends are typed
jackknife screens).

NO RH claim: everything here is float-level MEASURED SURFACE
STRUCTURE on the 67-rung ladder; the direction v is computed
per-rung data (the round-62 uniformity boundary applies
verbatim); a SEGENV-SUFFICIENT outcome would still be a per-rung
surface certificate, not a theorem, and a SEGENV-INSUFFICIENT
outcome is a measured residual demand, not a proof of
impossibility.  The halfgap constant 1/2 is the CLI registration
and is NEVER adjusted here.  No marker moves.

FIREWALL: no zeros, no prime oracles (AST scan; banned ids
zetazero / nzeros / primerange / isprime / primepi / nextprime /
prevprime; Lambda is read from the DEPLOYED window table only);
v563 READ-ONLY; RNG only inside the declared scramble control;
stdout only.

Sources (read-only): v563_paper2_readouts (core); ladder + cut/
scan machinery, grid/cumulant/envelope machinery and controls
verbatim from tail_abel_transport_probe.py (CLII, incl. its
amendment A1 = the all-integer KAPPA_INT, adopted as deployed);
q_read + v_sm construction verbatim from
arithmetic_lift_race_probe.py; mu1 normalization from
moving_node_second_order_probe.py (CXLIII); halfgap constant
C0 = 1/2 from halfgap_registration_probe.py (CLI, NO-ADJUST);
round-62 censuses (declared reproduction targets).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/tail_segment_split_probe.py
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
SEG_ID_WARD = 1e-12
SEG_ENV_SLACK = 1e-9
CERT_ORD_WARD = 1e-9
GAIN_EPS = 1e-300
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
    dom = max(pos, neg) / max(pos + neg, GAIN_EPS)
    x_last = (float(um[ch[-1] + 1]) / (2.0 * alpha)
              if len(ch) else float("nan"))
    return dict(n_changes=int(len(ch)), single=(len(ch) == 0),
                dom=dom, x_last=x_last,
                sign=(1 if pos >= neg else -1))


def segment_split(dw):
    """Maximal fixed-strict-sign runs of dw among entries with
    |dw| > SIGN_EPS max|dw| (sub-threshold entries join the
    current segment) -- the predecessor's census semantics.
    Returns list of (start, end, sign) over dw indices."""
    dw = np.asarray(dw, float)
    n = len(dw)
    az = np.abs(dw)
    mx = float(az.max()) if n else 0.0
    if mx == 0.0:
        return [(0, n - 1, 0)]
    idx = np.nonzero(az > SIGN_EPS * mx)[0]
    ss = np.sign(dw[idx])
    ch = np.nonzero(ss[1:] * ss[:-1] < 0.0)[0]
    starts = [0] + [int(idx[c + 1]) for c in ch]
    signs = [int(ss[0])] + [int(ss[c + 1]) for c in ch]
    segs = []
    for j, s in enumerate(starts):
        e = (starts[j + 1] - 1) if j + 1 < len(starts) else n - 1
        segs.append((s, e, signs[j]))
    return segs


def build_rung(kz, comb=None, scramble_seed=None,
               smooth_world=False, need_sm=True):
    """One rung of the lift-race surface (predecessor verbatim)."""
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
PSI_FULL = np.cumsum(core.LAM_TAB)
DEVPSI = np.abs(PSI_FULL - np.arange(len(PSI_FULL), dtype=float))
KAP = core.chebyshev_kappa()
# Predecessor amendment A1 adopted as deployed: the bound is the
# ALL-INTEGER table constant on [100, ATOM_MAX] (the jump-point
# kappa does not majorize integer psi reads).
KAPPA_INT = float(np.max(np.where(
    np.arange(len(PSI_FULL)) >= KAPPA_LOW_X,
    DEVPSI / np.maximum(np.arange(len(PSI_FULL), dtype=float),
                        1.0), 0.0)))


def bnd_psi(x):
    x = np.asarray(x)
    return np.where(x >= KAPPA_LOW_X, KAPPA_INT * x.astype(float),
                    DEVPSI[np.minimum(x, KAPPA_LOW_X)])


def make_grid(row, nc):
    """Integer transport grid beyond the cut nc (predecessor
    verbatim + stored delta)."""
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
    At1 = blocked_cumsum(2.0 * inv_sq)
    E1 = A1 - At1
    delta = inv_sq[:-1] - inv_sq[1:]
    beta = bnd_psi(kk) + float(bnd_psi(np.array([nc]))[0])
    Cb = np.concatenate([[0.0],
                         blocked_cumsum(beta[:-1] * delta)])
    BE1 = 2.0 * (beta * inv_sq + Cb)
    BE2 = blocked_cumsum(BE1)
    BE3 = blocked_cumsum(BE2)
    env_min_slack = float(np.min(BE1 - np.abs(E1)))
    return dict(kk=kk, kf=kf, ug=ug, a=a, inv_sq=inv_sq, L=L,
                A1=A1, At1=At1, E1=E1, delta=delta,
                BE1=BE1, BE2=BE2, BE3=BE3,
                env_min_slack=env_min_slack, alpha=alpha, nc=nc)


def transport(grid, row, W):
    """Global order-1..3 transport (predecessor verbatim; gives
    the reference ERR budgets and the r=1 census)."""
    L = grid["L"]
    w = q_read(W, grid["ug"], row["D"], row["M"])
    dw1 = w[1:] - w[:-1]
    dw2 = dw1[1:] - dw1[:-1]
    dw3 = dw2[1:] - dw2[:-1]
    a = grid["a"]
    A1 = grid["A1"]
    A2 = blocked_cumsum(A1)
    A3 = blocked_cumsum(A2)
    T = float(np.dot(a, w))
    bdry = A1[L - 1] * w[L - 1]
    T1 = bdry - float(np.dot(A1[:L - 1], dw1))
    sc1 = abs(bdry) + float(np.dot(np.abs(A1[:L - 1]),
                                   np.abs(dw1)))
    dev_abel = abs(T1 - T) / max(sc1, 1.0)
    Tt = float(np.dot(2.0 * grid["inv_sq"], w))
    BE1, BE2, BE3 = grid["BE1"], grid["BE2"], grid["BE3"]
    e_bdry = BE1[L - 1] * abs(w[L - 1])
    ERR1 = e_bdry + float(np.dot(BE1[:L - 1], np.abs(dw1)))
    ERR2 = (e_bdry + BE2[L - 2] * abs(dw1[L - 2])
            + float(np.dot(BE2[:L - 2], np.abs(dw2))))
    ERR3 = (e_bdry + BE2[L - 2] * abs(dw1[L - 2])
            + BE3[L - 3] * abs(dw2[L - 3])
            + float(np.dot(BE3[:L - 3], np.abs(dw3))))
    cen1 = sign_census(dw1, grid["ug"][:len(dw1)], grid["alpha"])
    return dict(w=w, dw1=dw1, T=T, Tt=Tt, dev_abel=dev_abel,
                ERR=(ERR1, ERR2, ERR3), cen1=cen1)


def seg_analyze(grid, row, W):
    """The segment-split bookkeeping: exact telescoped identity,
    per-segment one-sided envelopes, boundary reads, floors and
    the assembled certificate."""
    L = grid["L"]
    ug = grid["ug"]
    alpha = grid["alpha"]
    w = q_read(W, ug, row["D"], row["M"])
    dw = w[1:] - w[:-1]
    segs = segment_split(dw)
    A1, At1, E1 = grid["A1"], grid["At1"], grid["E1"]
    kk, inv, delta = grid["kk"], grid["inv_sq"], grid["delta"]
    a = grid["a"]
    T = float(np.dot(a, w))
    Tt = float(np.dot(2.0 * inv, w))
    out = []
    scale = 0.0
    for (s, e, sg) in segs:
        A1p = float(A1[s - 1]) if s > 0 else 0.0
        At1p = float(At1[s - 1]) if s > 0 else 0.0
        E1p = float(E1[s - 1]) if s > 0 else 0.0
        Bj = A1[s:e + 1] - A1p
        Btj = At1[s:e + 1] - At1p
        Ej = E1[s:e + 1] - E1p
        beta = (bnd_psi(kk[s:e + 1])
                + float(bnd_psi(np.array([int(kk[s]) - 1]))[0]))
        Cb = np.concatenate(
            [[0.0], blocked_cumsum(beta[:-1] * delta[s:e])])
        BE = 2.0 * (beta * inv[s:e + 1] + Cb)
        dws = dw[s:e + 1]
        adws = np.abs(dws)
        env = float(np.dot(BE, adws))
        t_m = -float(np.dot(Bj, dws))
        ts = -float(np.dot(Btj, dws))
        wb = float(w[e + 1])
        m_i = float(A1[e] - A1p)
        mt_i = float(At1[e] - At1p)
        BEe = float(BE[-1])
        b_meas = m_i * wb
        b_cert = mt_i * wb - BEe * abs(wb)
        bt_raw = -A1p * (float(w[e + 1]) - float(w[s]))
        slack2 = float(np.min(BE - np.abs(Ej)))
        if sg < 0:
            m1 = float(np.min(BE + Ej))
            off = dws > 0.0
        elif sg > 0:
            m1 = float(np.min(BE - Ej))
            off = dws < 0.0
        else:
            m1 = slack2
            off = np.zeros(len(dws), bool)
        floored = False
        cert = ts - env
        if sg < 0:
            floor = -float(np.dot((Btj + BE)[off], dws[off]))
            if floor > cert:
                cert = floor
                floored = True
        scale += abs(b_meas) + float(np.dot(np.abs(Bj), adws))
        out.append(dict(
            s=s, e=e, sg=sg, x0=float(ug[s]) / (2.0 * alpha),
            x1=float(ug[min(e + 1, L - 1)]) / (2.0 * alpha),
            m=m_i, mt=mt_i, t=t_m, ts=ts, env=env, cert=cert,
            b_meas=b_meas, b_cert=b_cert, bt_raw=bt_raw, BEe=BEe,
            wb=wb, slack2=slack2, m1=m1, floored=floored,
            n_off=int(np.sum(off)),
            m1rel=m1 / max(float(np.max(BE)), GAIN_EPS)))
    T_seg = sum(o["b_meas"] + o["t"] for o in out)
    Tt_seg = sum(o["mt"] * o["wb"] + o["ts"] for o in out)
    T_cert = sum(o["b_cert"] + o["cert"] for o in out)
    bdry_glob = float(A1[L - 1] * w[L - 1])
    regroup = abs(sum(o["bt_raw"] for o in out) + bdry_glob
                  - sum(o["b_meas"] for o in out))
    dev_seg = abs(T_seg - T) / max(scale, 1.0)
    dev_sm = abs(Tt_seg - Tt) / max(scale, 1.0)
    dev_rg = regroup / max(scale, 1.0)
    env_ward = min(o["slack2"] for o in out)
    bts = [o["bt_raw"] for o in out]
    tel = (abs(sum(bts)) / max(sum(abs(b) for b in bts),
                               GAIN_EPS))
    return dict(segs=out, T=T, Tt=Tt, T_cert=T_cert,
                dev_seg=dev_seg, dev_sm=dev_sm, dev_rg=dev_rg,
                env_ward=env_ward, tel=tel, scale=scale,
                nseg=len(out),
                xbp=[o["x0"] for o in out[1:]],
                pattern="".join("+" if o["sg"] > 0 else
                                "-" if o["sg"] < 0 else "0"
                                for o in out))


def ctrl_seg_battery(r, cut):
    """C3: segment-anchored envelope factor for a control rung
    from the fixed cut (integer reads exactly as the
    predecessor's C2; segments from the control's OWN kernel)."""
    Ng = int(math.floor(r["X"]))
    kk = np.arange(cut + 1, Ng + 1, dtype=np.int64)
    kf = kk.astype(float)
    inv = 1.0 / np.sqrt(kf)
    delta = inv[:-1] - inv[1:]
    At1 = blocked_cumsum(2.0 * inv)
    if "scr" in r and r["scr"]:
        cmass = np.concatenate([[0.0], blocked_cumsum(r["mu"])])
        idx = np.searchsorted(r["uu"], np.log(kf), side="right")
        i0 = int(np.searchsorted(r["uu"], math.log(cut) + 1e-12,
                                 side="right"))
        A1c = cmass[idx] - cmass[i0]
    else:
        nn = np.round(np.exp(r["uu"])).astype(int)
        ag = np.zeros(Ng + 1)
        keep = nn <= Ng
        np.add.at(ag, nn[keep], r["mu"][keep])
        A1c = blocked_cumsum(ag[cut + 1:Ng + 1])
    E1c = A1c - At1
    wc = q_read(r["Wv"], np.log(kf), r["D"], r["M"])
    dwc = wc[1:] - wc[:-1]
    segs = segment_split(dwc)
    fac = 0.0
    for (s, e, _sg) in segs:
        E1p = float(E1c[s - 1]) if s > 0 else 0.0
        Ej = E1c[s:e + 1] - E1p
        beta = (bnd_psi(kk[s:e + 1])
                + float(bnd_psi(np.array([int(kk[s]) - 1]))[0]))
        Cb = np.concatenate(
            [[0.0], blocked_cumsum(beta[:-1] * delta[s:e])])
        BE = 2.0 * (beta * inv[s:e + 1] + Cb)
        fac = max(fac, float(np.max(np.abs(Ej) / BE)))
    return fac, len(segs)


def main():
    section("PRIME.PORT.TAIL.SEGSPLIT.01 -- the segment-split "
            "attack on the tail (EXPLORATION ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s"
          % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
    print("    NO RH claim; no marker moves; C0 = 1/2 is the CLI "
          "registration, NO-ADJUST.")
    print("\nS0 -- firewall")
    check("S0.1 AST firewall clean", not ast_scan(BANNED_IDS))

    # ------------------------------------------------------------ W
    section("W -- the faithful ladder + wards (predecessor "
            "verbatim)")
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
          "of %.6f (jump points; ALL-INTEGER table envelope "
          "KAPPA_INT = %.6f deployed, predecessor amendment A1)"
          % (KAP, KAPPA_TOL, core.KAPPA_REF, KAPPA_INT),
          abs(KAP - core.KAPPA_REF) <= KAPPA_TOL, kill="K2")
    mu1 = np.array([float(core.parity_mu(r["h"])[0])
                    for r in rungs])
    mu1_cf = np.array([4.0 * math.sin(math.pi
                                      / (2 * r["h"] + 1)) ** 2
                       for r in rungs])
    dev_mu = float(np.max(np.abs(mu1 - mu1_cf)
                          / np.maximum(mu1, GAIN_EPS)))
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

    grids, trv, sgv, sgs = [], [], [], []
    for r, nc in zip(rungs, nB_min):
        g = make_grid(r, nc)
        grids.append(g)
        trv.append(transport(g, r, r["Wv"]))
        sgv.append(seg_analyze(g, r, r["Wv"]))
        Ws = r["Wcar"] if r["ov"] < OV_MIN else r["Wsm"]
        sgs.append(seg_analyze(g, r, Ws))
    tie = max(abs(t["T"] - float(r["tail_B"][i]))
              / max(1.0, abs(float(r["tail_B"][i])))
              for t, r, i in zip(trv, rungs, icBs))
    check("W10 WARD grid tie: integer-grid tail == tail_B(cB) "
          "max rel dev %.2e <= %.0e  [%.1f s]"
          % (tie, TIE_WARD, time.time() - T0),
          tie <= TIE_WARD, kill="K2")
    env_slk = min(g["env_min_slack"] for g in grids)
    check("W11 WARD global envelope in-window: |E1| <= BE1 "
          "everywhere on every rung (min slack %+.3e >= %.0e)"
          % (env_slk, -ENV_SLACK), env_slk >= -ENV_SLACK,
          kill="K2")
    if KILLS:
        return finish({})

    # ------------------------------------------------------------ A
    section("A -- (a) BREAKPOINT CENSUS: the r = 1 dual kernel's "
            "sign-change points, both kernels")
    print("    segments from the TRUE kernel q_v (exact fixed "
          "sign); classicality vs the prime-free q_{v_sm} "
          "(carrier branch).  Zero threshold %.0e * max|Dw| "
          "(declared)." % SIGN_EPS)
    aa = np.array([r["alpha"] for r in rungs])
    nsegv = np.array([s["nseg"] for s in sgv])
    nsegs = np.array([s["nseg"] for s in sgs])
    match = nsegv == nsegs
    dxs = []
    for sv, ss_, mt in zip(sgv, sgs, match):
        if mt and sv["nseg"] > 1:
            dxs.append(max(abs(a - b) for a, b in
                           zip(sv["xbp"], ss_["xbp"])))
    dxs = np.array(dxs) if dxs else np.array([float("nan")])
    hist = {}
    for n in nsegv:
        hist[int(n)] = hist.get(int(n), 0) + 1
    dom_neg = sum(1 for t in trv if t["cen1"]["sign"] < 0)
    dom_med = float(np.median([t["cen1"]["dom"] for t in trv]))
    xf = np.array([s["xbp"][0] for s in sgv if s["nseg"] > 1])
    xl = np.array([s["xbp"][-1] for s in sgv if s["nseg"] > 1])
    af = np.array([r["alpha"] for r, s in zip(rungs, sgv)
                   if s["nseg"] > 1])
    slF, seF, r2F = jack_slope(af, xf)
    slL, seL, r2L = jack_slope(af, xl)
    print("    segment count histogram (true kernel): %s; "
          "pattern med %s"
          % (dict(sorted(hist.items())),
             sorted((s["pattern"] for s in sgv),
                    key=len)[len(sgv) // 2]))
    print("    dominant sign negative on %d/%d (mass share med "
          "%.3f)" % (dom_neg, N, dom_med))
    print("    breakpoint positions x = u/(2a): first med %.3f "
          "(drift %+.4f/alpha +- 2SE %.4f, R^2 %.2f); last med "
          "%.3f (drift %+.4f/alpha +- 2SE %.4f, R^2 %.2f)"
          % (float(np.median(xf)), slF, 2 * seF, r2F,
             float(np.median(xl)), slL, 2 * seL, r2L))
    print("    classicality: count agreement v vs v_sm on %d/%d; "
          "matched-position |dx| med %.4f max %.4f"
          % (int(np.sum(match)), N, float(np.nanmedian(dxs)),
             float(np.nanmax(dxs))))
    lab_a = ("BP-CENSUS(nseg med %d (%d..%d), neg-dom %d/%d, "
             "x_last %.3f drift %+.4f) + CLASSICAL-BP(match "
             "%d/%d, med|dx| %.4f)"
             % (int(np.median(nsegv)), int(nsegv.min()),
                int(nsegv.max()), dom_neg, N,
                float(np.median(xl)), slL, int(np.sum(match)),
                N, float(np.nanmedian(dxs))))
    check("A.1 typed (a): %s" % lab_a, True)

    # ------------------------------------------------------------ B
    section("B -- (b) THE EXACT SEGMENT IDENTITY (WARDS)")
    dev_seg = max(s["dev_seg"] for s in sgv)
    check("B.1 WARD segment identity T = sum_j [m_j w(b) - sum "
          "B_j Dw] on every rung: max rel dev %.2e <= %.0e"
          % (dev_seg, SEG_ID_WARD), dev_seg <= SEG_ID_WARD,
          kill="K2")
    dev_sm = max(s["dev_sm"] for s in sgv)
    check("B.2 WARD smooth twin identity (At1/Bt vs Ttilde): "
          "max rel dev %.2e <= %.0e" % (dev_sm, SEG_ID_WARD),
          dev_sm <= SEG_ID_WARD, kill="K2")
    dev_rg = max(s["dev_rg"] for s in sgv)
    check("B.3 WARD regrouping sum bt_j + A1(N)w_N == sum m_j "
          "w(b): max rel dev %.2e <= %.0e"
          % (dev_rg, SEG_ID_WARD), dev_rg <= SEG_ID_WARD,
          kill="K2")
    env_w = min(s["env_ward"] for s in sgv)
    check("B.4 WARD segment envelope in-window |E_j| <= BE_j on "
          "every segment of every rung (min slack %+.3e >= %.0e)"
          % (env_w, -SEG_ENV_SLACK), env_w >= -SEG_ENV_SLACK,
          kill="K2")
    dev_ord = max((s["T_cert"] - s["T"]) / max(s["scale"], 1.0)
                  for s in sgv)
    check("B.5 WARD certificate order T_cert <= T on every rung "
          "(max rel excess %+.2e <= %.0e)"
          % (dev_ord, CERT_ORD_WARD), dev_ord <= CERT_ORD_WARD,
          kill="K2")
    lab_b = ("SEG-ID-EXACT(%.1e, smooth %.1e, regroup %.1e)"
             % (dev_seg, dev_sm, dev_rg))
    if KILLS:
        return finish({})

    # ------------------------------------------------------------ D
    section("D -- (d) BOUNDARY TERMS at the classical "
            "breakpoints")
    bdry_tot = np.array([sum(o["b_meas"] for o in s["segs"])
                         for s in sgv]) / mu1
    bdry_env = np.array([sum(o["BEe"] * abs(o["wb"])
                             for o in s["segs"])
                         for s in sgv]) / mu1
    tels = np.array([s["tel"] for s in sgv])
    print("    boundary content sum m_j w(b)/mu1: min/med/max "
          "%+.3e/%+.3e/%+.3e; envelope cost of the reads "
          "min/med/max %.3e/%.3e/%.3e mu1"
          % (float(np.min(bdry_tot)), float(np.median(bdry_tot)),
             float(np.max(bdry_tot)), float(np.min(bdry_env)),
             float(np.median(bdry_env)),
             float(np.max(bdry_env))))
    print("    raw-form telescoping |sum bt_j|/sum|bt_j|: "
          "min/med/max %.3f/%.3f/%.3f (1 = no cancellation)"
          % (float(np.min(tels)), float(np.median(tels)),
             float(np.max(tels))))
    lab_d = ("BDRY(reads med %.2e mu1, env med %.2e mu1, tel "
             "med %.2f)"
             % (float(np.median(np.abs(bdry_tot))),
                float(np.median(bdry_env)),
                float(np.median(tels))))
    check("D.1 typed (d): %s" % lab_d, True)

    # ------------------------------------------------------------ E
    section("E -- (c)+(e) THE SEGMENT-WISE ENVELOPE + ASSEMBLY "
            "(decisive): KAPPA_INT = %.6f segment-anchored"
            % KAPPA_INT)
    H = hBc
    Tcert = np.array([s["T_cert"] for s in sgv])
    Ttv = np.array([s["Tt"] for s in sgv])
    ERRg = np.array([min(t["ERR"]) for t in trv])
    ERRseg = Ttv - Tcert
    slack_seg = (H + Tcert) / mu1 - C0
    slack_glb = (H + Ttv - ERRg) / mu1 - C0
    gain = ERRg / np.maximum(ERRseg, GAIN_EPS)
    car_idx, car_term, car_sign, car_x = [], [], [], []
    n_floor, n_negseg, n_needlow, n_needup = 0, 0, 0, 0
    m1_all = []
    for s in sgv:
        costs = [o["BEe"] * abs(o["wb"]) + (o["ts"] - o["cert"])
                 for o in s["segs"]]
        ci = int(np.argmax(costs))
        car_idx.append(ci)
        car_term.append(ci == s["nseg"] - 1)
        car_sign.append(s["segs"][ci]["sg"])
        car_x.append(s["segs"][ci]["x0"])
        for o in s["segs"]:
            if o["sg"] < 0:
                n_negseg += 1
                n_needlow += 1
                if o["floored"]:
                    n_floor += 1
            elif o["sg"] > 0:
                n_needup += 1
            m1_all.append(o["m1rel"])
    m1_all = np.array(m1_all)
    print("    per-rung ledger (certificates in mu1 units):")
    print("    kz   h    nseg pat    slack_seg   ERRseg/mu1  "
          "ERR_glb/mu1 gain  carrier")
    for i, (r, s) in enumerate(zip(rungs, sgv)):
        print("    %-4d %-4d %-4d %-6s %+.3e %.3e %.3e %5.2f "
              "seg%d(%s%s)"
              % (r["kz"], r["h"], s["nseg"], s["pattern"],
                 slack_seg[i], ERRseg[i] / mu1[i],
                 ERRg[i] / mu1[i], gain[i], car_idx[i] + 1,
                 "+" if car_sign[i] > 0 else "-",
                 ",term" if car_term[i] else ""), flush=True)
    for si, tag in ((0, "first"), (N // 2, "mid"),
                    (N - 1, "deepest")):
        r, s = rungs[si], sgv[si]
        print("\n    SAMPLE rung (%s) kz %d h %d (nc %d, mu1 "
              "%.3e): per-segment ladder"
              % (tag, r["kz"], r["h"], grids[si]["nc"], mu1[si]))
        print("      j sgn x-range        need     m1/maxBE  "
              "t/mu1       ts/mu1      env/mu1     cert/mu1")
        for j, o in enumerate(s["segs"]):
            need = ("E >= -BE" if o["sg"] < 0 else
                    "E <= +BE" if o["sg"] > 0 else "two-sided")
            print("      %d  %s  [%.3f,%.3f] %-9s %.3f     "
                  "%+.3e %+.3e %.3e %+.3e%s"
                  % (j + 1, "+" if o["sg"] > 0 else "-",
                     o["x0"], o["x1"], need, o["m1rel"],
                     o["t"] / mu1[si], o["ts"] / mu1[si],
                     o["env"] / mu1[si], o["cert"] / mu1[si],
                     "  FLOOR" if o["floored"] else ""))
    n_pos = int(np.sum(slack_seg > 0.0))
    print("\n    one-sided demand census: %d segments need the "
          "LOWER side (sigma = -1), %d the UPPER (sigma = +1); "
          "measured one-sided margin min(BE -+ E)/max BE "
          "min/med %.3f/%.3f"
          % (n_needlow, n_needup, float(np.min(m1_all)),
             float(np.median(m1_all))))
    print("    nonnegativity floor fires on %d/%d negative "
          "segments (replaces a worse envelope certificate)"
          % (n_floor, n_negseg))
    print("    GAIN ledger ERR_best(global)/ERRseg_eff: "
          "min/med/max %.3f/%.3f/%.3f; global slack min/med "
          "%+.2e/%+.2e (predecessor form, reference)"
          % (float(np.min(gain)), float(np.median(gain)),
             float(np.max(gain)), float(np.min(slack_glb)),
             float(np.median(slack_glb))))
    nt = int(np.sum(car_term))
    print("    CARRIER census: terminal segment on %d/%d; "
          "carrier sign + on %d/%d; carrier onset x med %.3f"
          % (nt, N, int(np.sum(np.array(car_sign) > 0)), N,
             float(np.median(car_x))))
    if n_pos == N:
        c0_rec = float(np.min((H + Tcert) / mu1))
        lab_e = "SEGENV-SUFFICIENT(min slack %+.3e)" % float(
            np.min(slack_seg))
        print("    ==> THE TAIL STATEMENT CLOSES SEGMENT-WISE "
              "ON THE SURFACE: T >= -H + c0 mu1 with c0 = %.4f "
              "(recorded vs frozen 1/2, NO adjustment; "
              "KAPPA_INT = %.6f, cuts n_minB, breakpoints "
              "classical)" % (c0_rec, KAPPA_INT))
    else:
        slG, seG, r2G = jack_slope(aa, np.log(ERRseg / mu1))
        lab_e = ("SEGENV-INSUFFICIENT(slack min/med %+.2e/%+.2e, "
                 "residual law %+.3f, carrier term %d/%d)"
                 % (float(np.min(slack_seg)),
                    float(np.median(slack_seg)), slG, nt, N))
        print("    ==> SEGMENT-WISE ENVELOPES INSUFFICIENT on "
              "%d/%d: residual demand law log(ERRseg_eff/mu1) = "
              "%+.3f alpha + c (2SE %.3f, R^2 %.2f) vs global "
              "+1.744 (CLII, recorded); the residual object is "
              "the carrier segment's one-sided windowed-psi "
              "demand at scale med %.2e mu1"
              % (N - n_pos, N, slG, 2 * seG, r2G,
                 float(np.median(ERRseg / mu1))))
    lab_g = "GAIN(med %.2f, max %.2f)" % (
        float(np.median(gain)), float(np.max(gain)))
    check("E.1 typed (c)+(e): %s / %s" % (lab_e, lab_g), True)

    # ------------------------------------------------------------ T
    section("T -- (f) TAU-SCREENS (jackknife, typed)")
    scr = []
    for nm, yv in (("ERRseg/mu1", ERRseg / mu1),
                   ("bdry reads/mu1", np.abs(bdry_tot) + 1e-30),
                   ("gain", gain)):
        sl, se, r2 = jack_slope(np.log(mm), np.log(yv))
        ty = ("PASS" if abs(sl) <= SLOPE_PASS else
              "RELOC" if sl >= SLOPE_RELOC else "AMBIG")
        scr.append((nm, sl, ty))
        print("    screen log %s vs log m: slope %+.3f +- 2SE "
              "%.3f (R^2 %.2f) -> %s" % (nm, sl, 2 * se, r2, ty))
    lab_t = "SCREENS(%s)" % ", ".join(
        "%s %+.2f %s" % s for s in scr)
    check("T.1 typed (f): %s" % lab_t, True)

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
    ctl["scramble"]["scr"] = True
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
        print("    %-9s GLOBAL envelope factor max |E1|/BE1 = "
              "%.3g" % (name, facs[name]), flush=True)
    check("C2 WARD scramble violates the classical envelope: "
          "factor %.3g >= %.1f (cumulative structure destroyed)"
          % (facs["scramble"], CTRL_VIOL),
          facs["scramble"] >= CTRL_VIOL, kill="K2")
    segf = {}
    for name in ("Epstein", "smooth", "scramble"):
        segf[name], nsg = ctrl_seg_battery(ctl[name], CTRL_CUT)
        print("    %-9s SEGMENT-anchored factor max |E_j|/BE_j "
              "= %.3g (%d segments of its own kernel)"
              % (name, segf[name], nsg), flush=True)
    if segf["scramble"] <= 1.0:
        print("    ==> WARNING (first-class): the scramble sits "
              "INSIDE all segment envelopes -- the segment "
              "route would NOT discriminate")
    lab_c = ("CTRL-SEG(scramble %.3g%s, smooth %.3g%s, Epstein "
             "%.3g -- measured, typed)"
             % (segf["scramble"],
                " DISCRIMINATES" if segf["scramble"] > 1.0
                else " NON-DISCRIMINATING",
                segf["smooth"],
                " <= 1 as declared" if segf["smooth"] <= 1.0
                else " > 1 (recorded)",
                segf["Epstein"]))
    check("C3 typed segment battery: %s" % lab_c, True)

    return finish(dict(a=lab_a, b=lab_b, d=lab_d, e=lab_e,
                       g=lab_g, t=lab_t, c=lab_c))


def finish(labels):
    section("V -- FROZEN VERDICT")
    n_pass = sum(1 for _n, okk in CHECKS if okk)
    n_tot = len(CHECKS)
    if KILLS:
        VERDICT = {"K1": "PIPELINE-BROKEN",
                   "K2": "WARD-BROKEN"}[KILLS[0]]
        print("\n  VERDICT: %s" % VERDICT)
    else:
        VERDICT = ("SEGSPLIT-MEASURED / %(a)s / %(b)s / %(d)s / "
                   "%(e)s / %(g)s / %(t)s / %(c)s" % labels)
        print("\n  VERDICT: %s" % VERDICT)
    print("""
  HONEST FRAME (as frozen): the segment identity, its smooth
  twin, the regrouping and the segment-anchored envelope bound
  are EXACT bookkeeping; the breakpoint census, the per-segment
  slack ladders, the floors, the carrier census and the gain
  ledger are MEASURED SURFACE STRUCTURE at float level.  An
  insufficient segment-wise envelope is a measured residual
  demand, not an impossibility proof; a sufficient one would
  still be a per-rung surface certificate, not a theorem.  The
  halfgap constant 1/2 (CLI) is never adjusted here.  NO RH
  claim.  No marker moves.""")
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed"
          % (time.time() - T0, n_tot, n_tot - n_pass))
    return 0 if n_pass == n_tot else 1


if __name__ == "__main__":
    raise SystemExit(main())
