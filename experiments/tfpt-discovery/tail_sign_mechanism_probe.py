#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""tail_sign_mechanism_probe -- PRIME.PORT.TAILSIGN.01
(EXPLORATION ONLY, experiments/; round 62, theorem-engineering on
the RH-side wall: the CRACK attempt on the n > q half's only
visible seam -- the SIGN MECHANISM of the covering-cut tail.
Predecessor wall_cut_schedule_probe (round 60) measured FULL
COVERAGE 67/67 with minimal cuts n_min in [3, 9], ONE shared cut
n = 9, and tail <= 0 at the first covering cut on 67/67 (the head
OVERSHOOTS).  THE QUESTION HIERARCHY, each level strictly
stronger: (a) NET tail <= 0 (regression), (b) POINTWISE weight
negativity beyond the cut (then the tail sign is DETERMINISTIC
for any nonnegative comb), (c) CLASSICAL reduction of the weight
sign to the prime-free direction v_sm, (d) the HEAD FLOOR
tau-screen (O(1) or relocation -- the headline), (e) the
uniformity boundary named.  2026-08-10.)

THE TWO EXACT BOOKKEEPINGS (frozen; both warded to head + tail =
m EXACTLY).  On the lift-race surface m_h = lam_min(K) = lift -
demand exactly, with lift = E_at(v) - E_sm(v), demand =
-(E_ar(v) + E_sm(v)); hence ALSO m = E_ar(v) + E_at(v) -- the
smooth-comb parts CANCEL IDENTICALLY between lift and demand.
Cut at u_c = log c:
  A (round-59/60 verbatim; smooth counterpart INSIDE the tail):
      G(c)      = sum_{u_n <= u_c} mu_n q_v(u_n)
                  - int_{u <= u_c} 2 e^{u/2} q_v(u) du - demand,
      tail_A(c) = sum_{u_n > u_c} mu_n q_v(u_n)
                  - int_{u > u_c} 2 e^{u/2} q_v(u) du,
      m = G(c) + tail_A(c).  Pointwise weight negativity does NOT
      fix sign(tail_A): the smooth counterpart enters with the
      OPPOSITE sign.
  B (atom-only tail; the mechanism bookkeeping, NEW):
      head_B(c) = E_ar(v) + sum_{u_n <= u_c} mu_n q_v(u_n),
      tail_B(c) = sum_{u_n > u_c} mu_n q_v(u_n),
      m = head_B(c) + tail_B(c).  head_B is a FINITE EXPLICIT
      object (the archimedean read + finitely many atom reads);
      tail_B is a nonnegative-weighted sum of DEEP atom weights,
      so  q_v(u) <= 0 for all u > u_c  ==>  tail_B(c) <= 0  for
      ANY nonnegative comb -- no arithmetic input.
  Relation (warded): G(c) = head_B(c) + smoothtail(c) with
  smoothtail(c) = int_{u > u_c} 2 e^{u/2} q_v(u) du.
  SAID PLAINLY (frozen): tail_B <= 0 alone does NOT lower-bound
  m (m = head_B + tail_B <= head_B).  What the sign mechanism
  buys: the round-59 TWO-SIDED tail-accuracy demand collapses to
  the ONE-SIDED lower bound tail_B > -head_B, with the tail's
  sign known for free; the certificate shape is head_B > |tail_B|
  and at any cut where tail_B <= 0, cert_B := head_B - |tail_B|
  = m EXACTLY (same algebra as round 60).  Whether the remaining
  one-sided statement is between two O(1) quantities or is
  itself tau-small is measured in (d) -- that is the headline.

WHAT IS MEASURED (frozen; typed, never kills):
 (a) NET: sign census of tail_A at the per-rung first A-covering
     cut c(h) (cert_A > 0, round-60 verbatim) and at the shared
     cut n = 9; sign census of tail_B at the per-rung first
     B-COVERING cut cB(h) (cert_B = head_B - |tail_B| > 0 --
     bookkeeping B has its OWN schedule) and at the shared cut
     n = 9.  Typed NET-A(k/N@cmin | k9/N@9),
     NET-B(kB/N@cB | k9/N@9), plus the B-schedule ladder n_minB.
 (b) POINTWISE: q_v is PIECEWISE LINEAR on the lag knots i*D, so
     sup_{u > u_c} q_v is EXACT from the knot values (+ the cut
     point).  Census beyond log 9, beyond the per-rung u_min (A),
     and beyond the per-rung u_minB (B): positive-knot count, sup
     q_deep / max|q| (exact), number of sign changes beyond the
     cut, the LAST sign change u_last (whole window, exact
     interpolation on knots) in the scaled variable u_last/alpha
     vs the node law 0.3727 - 0.0116 alpha and vs log 9 / alpha,
     the terminal sign.  Atom-level census: deep atoms with
     q_v(u_n) > 0, their count, and positive contribution P =
     sum mu_n q^+ vs |tail_B(9)|.  Typed POINTWISE-V(n/N) iff
     sup q_deep <= 0 beyond log 9 on n rungs.
 (c) CLASSICAL: the same census for q_{v_sm} with v_sm the
     PRIME-FREE smooth-model bottom mode (arch + PNT-continuum
     comb only; branch crossings disclosed per the lift-race
     probe: at most MAX_CROSS rungs with |<v, v_sm>| < OV_MIN,
     each carrying the direction on one of the 4 lowest smooth
     branches).  Agreement of the deep-sign property and of
     u_last between v and v_sm (corr, med |Delta|); jackknife law
     u_last/alpha vs alpha.  Typed CLASSICAL-NEG(n/N) etc.
 (d) THE HEAD FLOOR (tau-screen, decisive): the TYPED screen
     lives at the per-rung first B-COVERING cut cB(h) (the
     mechanism's own schedule; the smoke showed head_B(9) < 0 on
     most rungs -- the shared cut 9 belongs to bookkeeping A's
     schedule): jackknife slope of log head_B(cB) vs log m_h.
     Bands PASS |s| <= 0.30 (HEADFLOOR-O1: the ENTIRE h-decay of
     the wall margin lives in the sign-measured tail; the open
     arithmetic statement tail_B > -head_B is an inequality
     between two O(1) quantities whose gap is m_h) / RELOC s >=
     0.70 (the hardness moved into the finite head -- an honest
     relocation) / else AMBIG.  Context screens (printed, never
     typed): head_B(9), G(9).  Plus the SHARED B-CUT search: the
     single cut value n covering the most rungs in the B sense
     (candidates = all deployed atom values <= CAP_SHARED),
     printed as SCHED-B(n*, count).
 (e) UNIFORMITY BOUNDARY (named): every certificate piece depends
     on h -- the weight through the direction (v arithmetic, v_sm
     prime-free) and through the window (2 alpha(h), lag pitch
     D(h)); the head through e_ar(h) and the h-dependent atom
     weights.  If pointwise negativity HOLDS at the shared cut:
     report the sign margin -sup q_deep / max|q| (med/min, typed
     UNIF-STABLE iff min >= MARGIN_MIN, else UNIF-MARGINAL) and
     its jackknife trend vs alpha.  If it FAILS: report the
     minimal pointwise-valid cut u_pw = last sign change (only
     meaningful when the terminal sign is negative), its scaled
     position and the atom count of the enlarged head <= e^{u_pw}
     -- i.e. whether the pointwise mechanism is restorable at a
     UNIFORMLY FINITE head or only at a head growing with X.

FROZEN PROTOCOL (machinery verbatim from wall_cut_schedule_probe
= round-59/60 chain; v_sm construction verbatim from
arithmetic_lift_race_probe S0):

 W   LADDER + WARDS (kill -> PIPELINE-BROKEN / WARD-BROKEN): W1
     faithful ladder >= MIN_RUNGS = 40 (kz 2..KZMAX, H_MIN <= h
     <= HCAP, X <= ATOM_MAX); W2 WARD m_h > 0 everywhere; W3 WARD
     both exact bookkeepings |lift - demand - m| <= ID_WARD AND
     |e_ar + e_t - m| <= ID_WARD; W4 WARD atom identities (atom
     sum = E_at, PNT grid sum = E_sm, rel <= ID_WARD); W5 WARD
     split exactness on the full scans: max rel dev of
     (head_B + tail_B) - m, (G + tail_A) - m, and G - head_B -
     smoothtail, all <= SCAN_WARD; W6 REPRODUCTION of round
     59/60: G > 0 counts at cuts (50, 100, 200) == (52, 26, 25);
     n_min(h) in [NMIN_LO, NMIN_HI] on every rung; the shared cut
     n = 9 covers N/N (cert > 0); tail_A <= 0 at the first
     covering cut on N/N; W7 WARD the v_sm branch: |<v, v_sm>| >=
     OV_MIN on all but <= MAX_CROSS rungs, each crossing rung
     carrying the direction on one of the 4 lowest smooth
     branches with overlap >= OV_MIN.

 H   THE HIERARCHY (typed as frozen above): Ha NET; Hb POINTWISE
     (v); Hc CLASSICAL (v_sm); Hd HEAD FLOOR + tau-screens; He
     UNIFORMITY BOUNDARY.

 C   CONTROLS (kill -> WARD-BROKEN if silent): scramble (seed 1)
     and Epstein x^2+5y^2 comb at kz 9, smooth comb (lattice
     masses 2 e^{u/2} du): each must show m < 0 AND cert_B =
     head_B - |tail_B| < 0 at EVERY cut AND A-sense cert coverage
     == 0 (the mechanism cannot manufacture a certificate without
     the wall); the smooth comb's DIFFERENT failure (lift
     collapse) recorded.

KILLS: K1 ladder (W1) -> PIPELINE-BROKEN; K2 wards (W2-W7, C) ->
WARD-BROKEN.  All H-typed outcomes are measurements, never kills.

VERDICT (frozen enum): TAILSIGN-MEASURED with typed sublabels
NET-A(k/N|k9/N) + NET-B(kB/N@cB|k9/N@9),
MECH-CLASSICAL-POINTWISE / MECH-POINTWISE-V / MECH-NET-ONLY /
MECH-MIXED(counts) [precedence in that order, decided at the
per-rung first B-covering cut cB(h) -- the mechanism's own
schedule],
HEADFLOOR-O1(slope) / HEADFLOOR-RELOC(slope) /
HEADFLOOR-AMBIG(slope),
UNIF-STABLE(min margin) / UNIF-MARGINAL(min margin) /
UNIF-CUTGROWTH(x_pw med, head atoms med) / UNIF-TERMINAL-POS;
else PIPELINE-BROKEN / WARD-BROKEN.

FROZEN BARS: KZMAX = 150; MIN_RUNGS = 40; REF_CUTS = (50, 100,
200); REF_COUNTS = (52, 26, 25); NMIN_LO, NMIN_HI = 3, 9;
NC_SHARED = 9; CAP_SHARED = 10000; ID_WARD = 1e-10; SCAN_WARD =
1e-9; NG_SMOOTH = 6000; OV_MIN = 0.8; MAX_CROSS = 2; SLOPE_PASS =
0.30; SLOPE_RELOC = 0.70; MARGIN_MIN = 0.01; NODE_C = 0.3727,
NODE_S = -0.0116 (declared input); CTRL_KZ = 9; scramble seed 1;
jackknife = full leave-one-out, CI = +- 2SE; sign decisions on
exact knot values (float sign, no tolerance -- the sup over a
piecewise-linear function is attained at a knot or at the cut
point).

SMOKE-RUN DISCLOSURE (2026-08-10, before freezing): ONE smoke run
(14/14, 17.6 s) on SPEC v0.  All wards green at 1.9e-13 or better
and the full round-59/60 reproduction exact.  Smoke facts frozen
as the context the frozen run must confirm: (i) NET-A holds
everywhere (tail_A <= 0 on 67/67 at c(h) AND at the shared cut
9), but the ATOM-ONLY tail flips: tail_B(9) <= 0 on only 12/67 --
on 55 rungs head_B(9) < 0 and tail_B(9) > 0 (the atom-only deep
sum CARRIES the positive lift there); (ii) bookkeeping B has its
OWN covering schedule: cert_B > 0 cuts exist on 67/67 with n_minB
med 17, and head_B at that cut is O(1) vs m (slope +0.113 +- 2SE
0.164, R^2 0.02); (iii) POINTWISE FAILS 0/67 (sup q_deep med 0.67
max|q|, positive knot share med 0.65, terminal lobe POSITIVE on
67/67); the same census is CLASSICAL (q_{v_sm}: 0/67, agreement
67/67, corr(u_last) +0.97, law u_last/alpha = +0.0163 alpha + c,
R^2 0.98, kz 97 on its carrier branch); (iv) G(9) screen slope
+0.292 (R^2 0.30); head_B(9) > 0 on only 12/67 -- the v0 typed
head-floor rule (keyed to head_B(9)) was nearly vacuous.
AMENDMENTS (disclosed, no bar/band/tolerance moved): A1 the typed
head-floor screen re-keyed from head_B(9) to head_B(cB) at the
per-rung first B-covering cut (head_B(9), G(9) stay printed as
context); A2 the MECH enum decided at cB(h) instead of the shared
cut 9 (bookkeeping B's own schedule; the shared-cut censuses stay
reported); A3 Ha additionally reports n_minB and the tail_B sign
census at cB; A4 Hb additionally reports the pointwise census
beyond u_minB (both directions, mech input); A5 the shared-B-cut
search added (info print).  Fail-first preserved: pointwise
negativity still fails at EVERY cut on the smoke (terminal lobe
positive), so the amendments cannot upgrade the mechanism verdict
beyond NET-ONLY; they relocate the screens to the bookkeeping the
mechanism actually lives on.

SPEC v1 (2026-08-10, frozen + SHA-hashed before the frozen run):
everything above.  Mechanical concretizations frozen with v1: (i)
cuts INCLUSIVE at atom positions (u_n <= u_c), the shared-cut
read at the largest atom position <= log 9 + 1e-12; (ii) knots
i*D for i = 0..M with the i = 0 value read at u = 1e-12 (q(0+) =
-||g||^2); (iii) u_last by linear interpolation between adjacent
knots with strict sign product < 0; (iv) the crossing-rung
carrier branch chosen as argmax_j |<v, v_sm^{(j)}>| over the 4
lowest smooth branches (disclosed per rung); (v) smoothtail via
the NG_SMOOTH midpoint grid (same grid as E_sm, so the W5
relation ward is exact).

NO-GO COMPLIANCE (frozen): no certified-bound retry, no rank-1
approximation, no Herglotz; no fit where an identity is claimed
(both bookkeepings are exact wards; the u_last law and the
head-floor screens are typed trends with jackknife error bars).

NO RH claim: a deterministic tail sign plus an O(1) explicit head
is a MEASURED SURFACE STRUCTURE -- the one-sided lower bound
tail_B > -head_B remains an unproved arithmetic statement at
every depth, and nothing here bounds it.  No marker moves.

FIREWALL: no zeros, no prime oracles (AST scan; banned ids
zetazero / nzeros / primerange / isprime / primepi / nextprime /
prevprime; the heads read the DEPLOYED window atoms); v563
READ-ONLY; RNG only inside the declared scramble control; stdout
only.

Sources (read-only): v563_paper2_readouts; cut/scan machinery
verbatim from wall_cut_schedule_probe.py (round 60); q_read +
v_sm construction verbatim from arithmetic_lift_race_probe.py;
node drift law from node_origin_arch_probe.py (declared input);
round-59/60 censuses (declared reproduction targets).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/tail_sign_mechanism_probe.py
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
CAP_SHARED = 10000
ID_WARD = 1e-10
SCAN_WARD = 1e-9
NG_SMOOTH = 6000
OV_MIN = 0.8
MAX_CROSS = 2
SLOPE_PASS = 0.30
SLOPE_RELOC = 0.70
MARGIN_MIN = 0.01
NODE_C = 0.3727
NODE_S = -0.0116
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


def corr(x, y):
    return float(np.corrcoef(np.asarray(x, float),
                             np.asarray(y, float))[0, 1])


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


def knot_census(W, D, M, alpha, u_cut):
    """Exact deep-sign census of the piecewise-linear weight
    q(u) = q_read(W, u): knot values (i*D, i = 0..M, i = 0 read at
    u = 1e-12), sup over u > u_cut (exact: knots above the cut +
    the cut point), sign changes, last sign change (interpolated),
    terminal sign.  A non-finite cut is read as u_cut = 0+ (the
    whole window; the harshest census)."""
    if not math.isfinite(float(u_cut)):
        u_cut = 1e-12
    uk = np.arange(M + 1) * D
    ue = uk.copy()
    ue[0] = 1e-12
    qk = q_read(W, ue, D, M)
    qmax = float(np.max(np.abs(qk)))
    q_cut = float(q_read(W, np.array([u_cut]), D, M)[0])
    deep = uk > u_cut
    q_deep = np.concatenate([[q_cut], qk[deep]])
    sup_deep = float(np.max(q_deep))
    pos_frac = float(np.mean(q_deep > 0.0))
    prod = qk[:-1] * qk[1:]
    idx = np.nonzero(prod < 0.0)[0]
    ucross = np.array([uk[i] + D * qk[i] / (qk[i] - qk[i + 1])
                       for i in idx])
    n_deep_cross = int(np.sum(ucross > u_cut))
    u_last = float(ucross[-1]) if len(ucross) else float("nan")
    end_sign = float(np.sign(qk[np.max(np.nonzero(
        np.abs(qk) > 1e-15 * max(qmax, 1e-30))[0])]))
    return dict(qmax=qmax, sup_deep=sup_deep,
                sup_rel=sup_deep / max(qmax, 1e-30),
                pos_frac=pos_frac, n_deep_cross=n_deep_cross,
                u_last=u_last, end_sign=end_sign,
                n_cross=len(ucross))


def build_rung(kz, comb=None, scramble_seed=None,
               smooth_world=False, need_sm=True):
    """One rung of the lift-race surface with both bookkeepings,
    the full atom-cut scans, and (optionally) the smooth-model
    bottom direction (lift-race S0 verbatim)."""
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
               m=float(w[0]), uu=uu)
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
    # ---- the atom-cut scans (cumsum routes; A verbatim round 60)
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
    # reference-cut split (round-59 census reproduction)
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


def main():
    section("PRIME.PORT.TAILSIGN.01 -- the sign mechanism of the "
            "covering-cut tail (EXPLORATION ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s"
          % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
    print("    NO RH claim; no marker moves.")
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
    check("W3 WARD both exact bookkeepings (lift - demand = m AND "
          "e_ar + E_at = m -- the smooth parts cancel "
          "identically): max dev %.2e <= %.0e" % (dev_bk, ID_WARD),
          dev_bk <= ID_WARD, kill="K2")
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
    check("W5 WARD split exactness on the full scans (head_B + "
          "tail_B = m, G + tail_A = m, G = head_B + smoothtail): "
          "max rel dev %.2e <= %.0e" % (dev_sc, SCAN_WARD),
          dev_sc <= SCAN_WARD, kill="K2")
    cnts = tuple(int(np.sum(np.array(
        [r["Gref"][nc] for r in rungs]) > 0)) for nc in REF_CUTS)
    n_min, u_min, i9s = [], [], []
    for r in rungs:
        nn = np.round(np.exp(r["uu"])).astype(int)
        covC = r["cert_A"] > 0.0
        i0 = int(np.argmax(covC)) if bool(np.any(covC)) else -1
        n_min.append(int(nn[i0]) if i0 >= 0 else -1)
        u_min.append(float(r["uu"][i0]) if i0 >= 0
                     else float("nan"))
        i9 = int(np.searchsorted(r["uu"],
                                 math.log(NC_SHARED) + 1e-12,
                                 side="right")) - 1
        i9s.append(i9)
    cov9 = sum(1 for r, i9 in zip(rungs, i9s)
               if i9 >= 0 and r["cert_A"][i9] > 0)
    tneg_cut = sum(1 for r, nm in zip(rungs, n_min) if nm > 0
                   and r["tail_A"][int(np.argmax(
                       r["cert_A"] > 0))] <= 0.0)
    ok_rep = (cnts == REF_COUNTS
              and all(NMIN_LO <= nm <= NMIN_HI for nm in n_min)
              and cov9 == N and tneg_cut == N)
    check("W6 REPRODUCTION round 59/60: G > 0 at %s = %s == %s; "
          "n_min in [%d, %d] on %d/%d; shared cut n = %d covers "
          "%d/%d; tail_A <= 0 at first covering cut %d/%d"
          % (REF_CUTS, cnts, REF_COUNTS, NMIN_LO, NMIN_HI,
             sum(1 for nm in n_min
                 if NMIN_LO <= nm <= NMIN_HI), N, NC_SHARED,
             cov9, N, tneg_cut, N), ok_rep, kill="K2")
    n_cross = sum(1 for r in rungs if r["ov"] < OV_MIN)
    cross_ok = all(max(r["ov4"]) >= OV_MIN for r in rungs
                   if r["ov"] < OV_MIN)
    check("W7 WARD v_sm branch: %d rung(s) with |<v, v_sm>| < "
          "%.1f (%s; ward <= %d), each carried on smooth branch "
          "j = %s with overlap >= %.1f"
          % (n_cross,
             OV_MIN, ", ".join("kz%d ov %.4f" % (r["kz"], r["ov"])
                               for r in rungs
                               if r["ov"] < OV_MIN) or "none",
             MAX_CROSS,
             "/".join(str(r["jcar"]) for r in rungs
                      if r["ov"] < OV_MIN) or "-", OV_MIN),
          n_cross <= MAX_CROSS and cross_ok, kill="K2")
    if KILLS:
        return finish({})

    # ------------------------------------------------------------ Ha
    section("Ha -- NET: the tail sign at c(h) and at the shared "
            "cut n = %d (both bookkeepings)" % NC_SHARED)
    print("    bookkeeping A: tail_A = deep atoms - deep smooth "
          "counterpart (round-59/60 verbatim); m = G + tail_A")
    print("    bookkeeping B: tail_B = deep atoms ONLY (smooth "
          "parts cancel in m = e_ar + E_at); m = head_B + tail_B")
    print("    kz   h    m_h        n_min  tailA@cmin  tailA@9   "
          " tailB@9    headB@9   n_minB  tailB@cB")
    kA_c = kA_9 = kB_cB = kB_9 = 0
    nB_min, uB_min, hB_cut = [], [], []
    for r, nm, i9 in zip(rungs, n_min, i9s):
        ic = int(np.argmax(r["cert_A"] > 0))
        tAc = float(r["tail_A"][ic])
        tA9 = float(r["tail_A"][i9])
        tB9 = float(r["tail_B"][i9])
        hB9 = float(r["head_B"][i9])
        nn = np.round(np.exp(r["uu"])).astype(int)
        covB = r["cert_B"] > 0.0
        if bool(np.any(covB)):
            icB = int(np.argmax(covB))
            nB_min.append(int(nn[icB]))
            uB_min.append(float(r["uu"][icB]))
            hB_cut.append(float(r["head_B"][icB]))
            tBc = float(r["tail_B"][icB])
        else:
            nB_min.append(-1)
            uB_min.append(float("nan"))
            hB_cut.append(float("nan"))
            tBc = float("nan")
        kA_c += tAc <= 0
        kA_9 += tA9 <= 0
        kB_cB += (tBc <= 0) if np.isfinite(tBc) else 0
        kB_9 += tB9 <= 0
        print("    %-4d %-4d %.3e  %-6d %+.3e  %+.3e  %+.3e  "
              "%+.3f    %-7d %+.3e"
              % (r["kz"], r["h"], r["m"], nm, tAc, tA9, tB9,
                 hB9, nB_min[-1], tBc), flush=True)
    n_covB = sum(1 for n in nB_min if n > 0)
    ha = ("NET-A(%d/%d@cmin|%d/%d@9) + NET-B(%d/%d@cB|%d/%d@9)"
          % (kA_c, N, kA_9, N, kB_cB, N, kB_9, N))
    print("\n    B-covering schedule: cert_B > 0 cuts exist on "
          "%d/%d; n_minB med %d (%d..%d)"
          % (n_covB, N,
             int(np.median([n for n in nB_min if n > 0])),
             min(n for n in nB_min if n > 0),
             max(n for n in nB_min if n > 0)))
    check("Ha.1 typed (a): %s (definitions pinned above; both "
          "splits warded to m exactly; the atom-only bookkeeping "
          "has its OWN schedule)" % ha, True)

    # ------------------------------------------------------------ Hb
    section("Hb -- POINTWISE: exact knot census of q_v beyond the "
            "cut")
    u9 = math.log(NC_SHARED)
    cen_v, cen_v_cmin, cen_v_cB = [], [], []
    at_pos = []
    for r, um, umB, i9 in zip(rungs, u_min, uB_min, i9s):
        c9 = knot_census(r["Wv"], r["D"], r["M"], r["alpha"], u9)
        cm = knot_census(r["Wv"], r["D"], r["M"], r["alpha"], um)
        cB = knot_census(r["Wv"], r["D"], r["M"], r["alpha"],
                         umB)
        cen_v.append(c9)
        cen_v_cmin.append(cm)
        cen_v_cB.append(cB)
        qan = q_read(r["Wv"], r["uu"], r["D"], r["M"])
        deep = r["uu"] > u9
        pos = deep & (qan > 0.0)
        Ppos = float(np.sum((r["qa"])[pos]))
        at_pos.append((int(np.sum(pos)), Ppos,
                       abs(float(r["tail_B"][i9]))))
    n_pw9 = sum(1 for c in cen_v if c["sup_deep"] <= 0.0)
    n_pwc = sum(1 for c in cen_v_cmin if c["sup_deep"] <= 0.0)
    n_pwB = sum(1 for c in cen_v_cB if c["sup_deep"] <= 0.0)
    sup_rel = np.array([c["sup_rel"] for c in cen_v])
    posf = np.array([c["pos_frac"] for c in cen_v])
    ndc = np.array([c["n_deep_cross"] for c in cen_v])
    print("    beyond log %d: sup q_deep <= 0 on %d/%d rungs; "
          "sup rel to max|q| med %.3f (%.3f..%.3f); positive "
          "knot share med %.3f; deep sign changes %d..%d"
          % (NC_SHARED, n_pw9, N, float(np.median(sup_rel)),
             float(np.min(sup_rel)), float(np.max(sup_rel)),
             float(np.median(posf)), int(ndc.min()),
             int(ndc.max())))
    print("    beyond the per-rung u_min (A): sup q_deep <= 0 on "
          "%d/%d rungs; beyond the per-rung u_minB (B): %d/%d"
          % (n_pwc, N, n_pwB, N))
    npos_at = np.array([a[0] for a in at_pos])
    ratP = np.array([a[1] / max(a[2], 1e-30) for a in at_pos])
    print("    atom census beyond n = %d: positive-weight atoms "
          "med %d (%d..%d); positive contribution P = sum mu q^+ "
          "= %.3f..%.3f of |tail_B(9)| (med %.3f)"
          % (NC_SHARED, int(np.median(npos_at)),
             int(npos_at.min()), int(npos_at.max()),
             float(np.min(ratP)), float(np.max(ratP)),
             float(np.median(ratP))))
    if n_pw9 == N:
        hb = "POINTWISE-V(%d/%d)" % (n_pw9, N)
    else:
        hb = ("POINTWISE-FAIL-V(%d/%d, sup med %.2f max|q|, "
              "pos share med %.2f)"
              % (n_pw9, N, float(np.median(sup_rel)),
                 float(np.median(posf))))
    check("Hb.1 typed (b): %s (exact: sup over a piecewise-linear "
          "weight is attained at a knot or the cut point)" % hb,
          True)

    # ------------------------------------------------------------ Hc
    section("Hc -- CLASSICAL: the same census for the prime-free "
            "q_{v_sm}")
    cen_s, cen_s_cB, cen_car = [], [], []
    for r, umB in zip(rungs, uB_min):
        cs = knot_census(r["Wsm"], r["D"], r["M"], r["alpha"], u9)
        cen_s.append(cs)
        cen_s_cB.append(knot_census(r["Wsm"], r["D"], r["M"],
                                    r["alpha"], umB))
        if r["ov"] < OV_MIN:
            cen_car.append((r["kz"], knot_census(
                r["Wcar"], r["D"], r["M"], r["alpha"], u9)))
    n_sm9 = sum(1 for c in cen_s if c["sup_deep"] <= 0.0)
    n_smB = sum(1 for c in cen_s_cB if c["sup_deep"] <= 0.0)
    sup_s = np.array([c["sup_rel"] for c in cen_s])
    print("    beyond log %d: sup q_sm <= 0 on %d/%d rungs; sup "
          "rel med %.3f (%.3f..%.3f); beyond u_minB: %d/%d"
          % (NC_SHARED, n_sm9, N, float(np.median(sup_s)),
             float(np.min(sup_s)), float(np.max(sup_s)), n_smB,
             N))
    for kzc, cc in cen_car:
        print("    crossing rung kz %d read on its carrier "
              "branch: sup rel %.3f, u_last %.3f, end sign %+d"
              % (kzc, cc["sup_rel"], cc["u_last"],
                 int(cc["end_sign"])))
    # u_last agreement + law (crossing rungs read on the carrier)
    ul_v = np.array([c["u_last"] for c in cen_v])
    ul_s = np.array([c["u_last"] for c in cen_s])
    for i, r in enumerate(rungs):
        if r["ov"] < OV_MIN:
            cc = dict(cen_car)[r["kz"]]
            ul_s[i] = cc["u_last"]
    okl = np.isfinite(ul_v) & np.isfinite(ul_s)
    co_ul = corr(ul_v[okl], ul_s[okl])
    dmed = float(np.median(np.abs(ul_v[okl] - ul_s[okl])))
    aa = np.array([r["alpha"] for r in rungs])
    sl_l, se_l, r2_l = jack_slope(aa[okl], (ul_s / aa)[okl])
    ustar = (NODE_C + NODE_S * aa) * aa
    co_node = corr(ul_s[okl], ustar[okl])
    x_last = ul_s[okl] / aa[okl]
    print("    u_last agreement v vs v_sm: corr %+.3f, med "
          "|Delta| %.1e; law u_last/alpha = %+.4f alpha + c "
          "(2SE %.4f, R^2 %.2f); med u_last/alpha %.3f vs node "
          "law med %.3f vs log%d/alpha med %.3f; corr(u_last, "
          "u*) = %+.3f; terminal sign negative on %d/%d (v) / "
          "%d/%d (v_sm)"
          % (co_ul, dmed, sl_l, 2 * se_l, r2_l,
             float(np.median(x_last)),
             float(np.median(NODE_C + NODE_S * aa)),
             NC_SHARED, float(np.median(u9 / aa)), co_node,
             sum(1 for c in cen_v if c["end_sign"] < 0), N,
             sum(1 for c in cen_s if c["end_sign"] < 0), N))
    agree = sum(1 for cv, cs in zip(cen_v, cen_s)
                if (cv["sup_deep"] <= 0) == (cs["sup_deep"] <= 0))
    if n_sm9 == N:
        hc = "CLASSICAL-NEG(%d/%d)" % (n_sm9, N)
    else:
        hc = ("CLASSICAL-CENSUS(%d/%d neg, sign-agreement with v "
              "%d/%d, corr(u_last) %+.2f)"
              % (n_sm9, N, agree, N, co_ul))
    check("Hc.1 typed (c): %s -- the weight geometry (deep sign "
          "pattern + last sign change) is a property of the "
          "PRIME-FREE smooth model" % hc, True)

    # ------------------------------------------------------------ Hd
    section("Hd -- THE HEAD FLOOR (tau-screen, decisive; typed "
            "at the per-rung first B-covering cut)")
    mm = np.array([r["m"] for r in rungs])
    hB9 = np.array([float(r["head_B"][i9])
                    for r, i9 in zip(rungs, i9s)])
    G9 = np.array([float(r["G"][i9])
                   for r, i9 in zip(rungs, i9s)])
    n_hpos = int(np.sum(hB9 > 0))
    slG, seG, r2G = jack_slope(np.log(mm[G9 > 0]),
                               np.log(G9[G9 > 0]))
    okB = np.array([n > 0 for n in nB_min])
    hBc = np.array(hB_cut)
    slC, seC, r2C = jack_slope(np.log(mm[okB]), np.log(hBc[okB]))
    print("    head_B(cB) = e_ar + sum_{n <= cB} mu_n q_v(u_n) "
          "at the first B-covering cut (covers %d/%d, n_minB med "
          "%d): med %.3f, min %.3f, max %.3f; head_B(cB)/m med "
          "%.1f; |tail_B(cB)| = head_B - m, med %.3f"
          % (int(np.sum(okB)), N,
             int(np.median(np.array(nB_min)[okB])),
             float(np.median(hBc[okB])), float(np.min(hBc[okB])),
             float(np.max(hBc[okB])),
             float(np.median(hBc[okB] / mm[okB])),
             float(np.median(hBc[okB] - mm[okB]))))
    print("    TYPED tau-screen log head_B(cB) vs log m: slope "
          "%+.3f +- 2SE %.3f (R^2 %.2f)"
          % (slC, 2 * seC, r2C))
    print("    context screens: G(9) slope %+.3f +- %.3f (R^2 "
          "%.2f, > 0 on %d/%d); head_B(9) med %.3f, > 0 on only "
          "%d/%d (the shared cut 9 belongs to bookkeeping A's "
          "schedule)"
          % (slG, 2 * seG, r2G, int(np.sum(G9 > 0)), N,
             float(np.median(hB9)), n_hpos, N))
    # shared single B-cut search (info)
    grid_n = np.unique(np.concatenate(
        [np.round(np.exp(r["uu"])).astype(int) for r in rungs]))
    grid_n = grid_n[grid_n <= CAP_SHARED]
    covmat = np.zeros((N, len(grid_n)), int)
    for i, r in enumerate(rungs):
        pos = np.searchsorted(r["uu"],
                              np.log(grid_n.astype(float))
                              + 1e-12, side="right") - 1
        okp = pos >= 0
        covmat[i, okp] = (r["cert_B"][pos[okp]] > 0.0)
    cov_cnt = covmat.sum(axis=0)
    jb = int(np.argmax(cov_cnt))
    print("    shared single B-cut search (candidates <= %d): "
          "best n = %d covers %d/%d"
          % (CAP_SHARED, int(grid_n[jb]), int(cov_cnt[jb]), N))
    if abs(slC) <= SLOPE_PASS:
        hd = "HEADFLOOR-O1(slope=%+.3f)" % slC
        print("    ==> O(1): the ENTIRE h-decay of the wall "
              "margin lives in the (sign-measured) atom tail "
              "tail_B(cB) = m - head_B(cB); the open arithmetic "
              "statement tail_B > -head_B is an inequality "
              "between two O(1) quantities whose gap IS m_h")
    elif slC >= SLOPE_RELOC:
        hd = "HEADFLOOR-RELOC(slope=%+.3f)" % slC
        print("    ==> RELOCATION: the head margin tracks tau -- "
              "the hardness moved into the finite head; recorded "
              "honestly")
    else:
        hd = "HEADFLOOR-AMBIG(slope=%+.3f)" % slC
    check("Hd.1 typed (d): %s + SCHED-B(n=%d, %d/%d) (bands PASS "
          "|s| <= %.2f, RELOC s >= %.2f)"
          % (hd, int(grid_n[jb]), int(cov_cnt[jb]), N,
             SLOPE_PASS, SLOPE_RELOC), True)

    # ------------------------------------------------------------ He
    section("He -- THE UNIFORMITY BOUNDARY (named)")
    print("    h-dependence of the certificate pieces: the weight "
          "q depends on h through the DIRECTION (v arithmetic; "
          "v_sm prime-free) and the WINDOW (2 alpha(h), lag pitch "
          "D(h)); the head through e_ar(h) and the h-dependent "
          "weights of the 7 fixed atoms.")
    if n_pw9 == N:
        marg = -sup_rel
        slM, seM, r2M = jack_slope(aa, marg)
        he = ("UNIF-STABLE(min=%.3f)" % float(np.min(marg))
              if float(np.min(marg)) >= MARGIN_MIN else
              "UNIF-MARGINAL(min=%.3f)" % float(np.min(marg)))
        print("    deep-sign margin -sup q_deep / max|q|: med "
              "%.3f, min %.3f; trend vs alpha %+.4f +- %.4f "
              "(R^2 %.2f)"
              % (float(np.median(marg)), float(np.min(marg)),
                 slM, 2 * seM, r2M))
    else:
        n_endneg = sum(1 for c in cen_v if c["end_sign"] < 0)
        if n_endneg == N:
            x_pw = np.array([c["u_last"] for c in cen_v]) \
                / (2.0 * aa)
            n_head = np.array([int(np.sum(
                r["uu"] <= c["u_last"] + 1e-12))
                for r, c in zip(rungs, cen_v)])
            slP, seP, r2P = jack_slope(
                np.log(np.exp(2.0 * aa)),
                np.log(np.maximum(n_head, 1)))
            he = ("UNIF-CUTGROWTH(x_pw med %.3f, head atoms med "
                  "%d ~ X^%.2f)"
                  % (float(np.median(x_pw)),
                     int(np.median(n_head)), slP))
            print("    pointwise negativity fails at n = %d but "
                  "the TERMINAL lobe is negative on %d/%d: a "
                  "per-rung pointwise-valid cut exists at u_pw = "
                  "u_last, scaled x_pw = u_pw/(2 alpha) med %.3f "
                  "(%.3f..%.3f); enlarged head atom count med %d "
                  "(%d..%d), growth ~ X^%.2f +- %.2f (R^2 %.2f) "
                  "-- the pointwise mechanism is restorable ONLY "
                  "at a head growing with X, not uniformly finite"
                  % (NC_SHARED, n_endneg, N,
                     float(np.median(x_pw)), float(np.min(x_pw)),
                     float(np.max(x_pw)), int(np.median(n_head)),
                     int(np.min(n_head)), int(np.max(n_head)),
                     slP, 2 * seP, r2P))
        else:
            he = ("UNIF-TERMINAL-POS(%d/%d end positive)"
                  % (N - n_endneg, N))
            xon = np.array([c["u_last"] for c in cen_v]) \
                / (2.0 * aa)
            xon = xon[np.isfinite(xon)]
            print("    the terminal weight lobe is POSITIVE on "
                  "%d/%d rungs -- NO enlarged cut restores "
                  "pointwise negativity; the mechanism is "
                  "NET-only there.  Terminal-lobe onset u_last/"
                  "(2 alpha) med %.3f (%.3f..%.3f): the positive "
                  "lobe occupies the deepest ~%.0f%% of the "
                  "window at every h -- the u-region repair "
                  "(probe 2 object) must name it"
                  % (N - n_endneg, N, float(np.median(xon)),
                     float(np.min(xon)), float(np.max(xon)),
                     100.0 * (1.0 - float(np.median(xon)))))
    check("He.1 typed (e): %s" % he, True)

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
        print("    %-9s: m %+.3e  lift %+.3e  covering cuts "
              "A/B %d/%d -> %s"
              % (name, r["m"], r["lift"], ncovA, ncovB,
                 "FIRES" if f else "SILENT"), flush=True)
    print("    truth |lift| med %.3f (smooth failure = lift "
          "collapse, a DIFFERENT anatomy, recorded)"
          % float(np.median([abs(r["lift"]) for r in rungs])))
    check("C1 WARD all three controls fire (m < 0 and zero "
          "coverage in BOTH senses)", fired, kill="K2")

    # mechanism verdict (frozen precedence, decided at the
    # per-rung first B-covering cut cB(h))
    if n_pwB == N and n_smB == N:
        mech = "MECH-CLASSICAL-POINTWISE"
    elif n_pwB == N:
        mech = "MECH-POINTWISE-V"
    elif kB_cB == N:
        mech = ("MECH-NET-ONLY(B-net %d/%d@cB, pointwise %d/%d"
                "@cB)" % (kB_cB, N, n_pwB, N))
    else:
        mech = ("MECH-MIXED(B-net %d/%d@cB, pointwise %d/%d@cB)"
                % (kB_cB, N, n_pwB, N))

    return finish(dict(ha=ha, hb=hb, hc=hc, hd=hd, he=he,
                       mech=mech))


def finish(labels):
    section("V -- FROZEN VERDICT")
    n_pass = sum(1 for _n, okk in CHECKS if okk)
    n_tot = len(CHECKS)
    if KILLS:
        VERDICT = {"K1": "PIPELINE-BROKEN",
                   "K2": "WARD-BROKEN"}[KILLS[0]]
        print("\n  VERDICT: %s" % VERDICT)
    else:
        VERDICT = ("TAILSIGN-MEASURED / %(ha)s / %(hb)s / %(hc)s "
                   "/ %(mech)s / %(hd)s / %(he)s" % labels)
        print("\n  VERDICT: %s" % VERDICT)
    print("""
  HONEST FRAME (as frozen): the tail sign and the head floor are
  MEASURED SURFACE STRUCTURE.  A deterministic tail sign (where it
  holds) converts the round-59 two-sided tail-accuracy demand into
  the one-sided lower bound tail_B > -head_B -- it does NOT prove
  it; the one-sided statement remains the open arithmetic content
  at every depth.  A NET-only sign is an arithmetic cancellation
  fact, not a weight-sign fact.  NO RH claim.  No marker moves.""")
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed"
          % (time.time() - T0, n_tot, n_tot - n_pass))
    return 0 if n_pass == n_tot else 1


if __name__ == "__main__":
    raise SystemExit(main())
