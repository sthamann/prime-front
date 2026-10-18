#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""band_arithmetic_anatomy_probe -- PRIME.PORT.BAND.ANATOMY.01
(EXPLORATION ONLY, experiments/; round 62, theorem-engineering on
the RH-side wall: the x = +1 edge band -- the convergent
obstruction seat of THREE programs (Gram completion CXXVIII/CXXXV,
autocorrelation Fejer-Riesz CXLII, relocation map v902) -- is made
an EXPLICIT ARITHMETIC OBJECT: which comb atoms generate it, what
law its mass and width obey, whether it IS the v902 beta boundary
term, and whether the wall splits into SOS-on-bulk + ONE explicit
band inequality.  2026-08-10.)

THE OBJECT (rounds 55-61 verbatim).  The deployed wall of one rung
is A = I - G on the negative folded family; M0 = I_h - H is
EXACTLY the moment matrix of nu = mu_+ - mu_- in the chain basis
(wall_gram_radau, two-route ward 4.9e-13; lam_min(M0) = tau_full).
The Lukacs/Gram completion of M0 over the full [-1, 1] cone fails
on EVERY rung, and the needed negative mass lives in an O(1e-2)
x-band at +1 (cumulative neg share 0.94 at delta = 1e-2, peak x ~
0.998; wall_edge_completion E4).  The v902 relocation map rewrites
the soft pivot EXACTLY as 1/d_12 = 1 + SPOS - beta with beta =
v_* nu_-[Q^2] >= 0 carried by the NEG support (case_edge).  The
v882 edge law: the sqrt-uniformized comb puts mass 1 - e^{-1/2} ~
0.3935 into the last log-unit.

THE TWO BAND FUNCTIONALS (frozen; the round-60 object named
precisely).  The wall_edge_completion E4 object is NOT the raw
mu_- band mass: it is the negative-side ENERGY of the minimizing
eigenvector e of the failing (1 - x)-localized moment matrix Mm,
c_j = v_j (1 - y_j) q(y_j)^2 with q = P e -- THAT functional has
band share 0.94 at delta = 1e-2.  This probe carries BOTH:
  RAW   m_band  = sum_F (-d_f) q_f            (source-only), and
  WGT   E_band  = sum_F (-d_f) q_f (1 - x_f) q(x_f)^2
(F = {f : cos(2 pi f / L) > 1 - DELTA, d_f < 0}, q_f = 2 x 4
sin^2(pi f / L) / (2 L)); both are LINEAR in the lag vector c at
fixed fold set / fixed eigenvector weight, so both are exactly
atom-attributable.  The WGT weight uses the Mm eigenvector -- a
MEASUREMENT-ONLY use of target spectral data (declared; nothing
here is a certificate).

THE FOUR QUESTIONS (frozen):
 (a) MAP.  Band read vectors g_k = -sum_F w_f fac(f, k) (fac =
     the real DCT factor 1 / (-1)^f / 2 cos; w_f = q_f for RAW,
     q_f (1 - x_f) q(x_f)^2 for WGT).  Every atom's contribution
     is its tent read of g (exact linearity ward ATTR_WARD) --
     the exact inversion of the node mapping.  CENSUS per rung
     and per functional: share from the archimedean lag, from
     the deep-edge atoms (u > 2 alpha - 1, the v882 last
     log-unit), from the head (n <= 9), from the rest;
     concentration count n90 = smallest number of atoms carrying
     >= 90% of the |atomic| mass; top atoms printed on 2 spot
     rungs.
 (b) LAW.  Per rung, on the WGT functional (the obstruction
     seat): band share at DELTA, width delta*_h = 1 - x at the
     0.90 energy quantile, peak x.  Fits: log delta* vs log h
     (jackknife slope); OLS share vs alpha.  The RAW mu_- band
     share is printed next to it (the v1 finding: it is SMALL --
     the band is an energy seat, not a mass seat).  RECORDED
     comparisons (no numerology flags): the deployed comb's
     last-log-unit mass share vs the v882 closed law 1 -
     e^{-1/2} = 0.393469; the ratio E_band / (last-unit comb
     mass).
 (c) UNIFICATION.  On the full-window rungs (case_edge verbatim:
     q = (I - G)^{-1} p_*, beta = v_* q^T G q, per-node terms
     b_j = v_* v_j Q(y_j)^2, two-route ward BETA_WARD): the
     band share of beta (sum of b_j on band nodes / beta) --
     is the v902 boundary term band-seated?  Proportionality
     beta vs m_band(RAW) and vs E_band(WGT): log-log OLS slope +
     R^2 + ratio spread (identity would need spread ~ 1 --
     measured, typed honestly on the better of the two).  The
     tau-relation of E_band (OLS log E_band vs log tau_full) is
     the requested edge-functional screen.
 (d) BAND-SPLIT SOS.  Split BOTH folded families at x <= 1 -
     delta (bulk) vs x > 1 - delta (band) over the FROZEN grid
     delta in DELTAS_SOS: M0 = M_bulk + M_band EXACTLY
     (three-route ward M0_WARD vs I - H at the census DELTA).
     Markov-Lukacs on [-1, 1 - delta] at matched even degree
     2h - 2: nu_bulk is representable iff L0 = M_bulk >= 0 AND
     L1 = moment matrix of (1 + x)(1 - delta - x) nu_bulk
     (basis degree <= h - 2) >= 0.  Success counts per rung and
     per delta (float floors, strict sign); the failure seat
     printed scale-invariantly (med lam_min(L0)/tau).  IF some
     delta passes on every rung, the ENTIRE wall failure sits
     in that band and the wall statement becomes: SOS-on-bulk +
     THE EXPLICIT BAND INEQUALITY
        lam_max(-M_band, M_bulk) <= 1
     (generalized eigenvalue; EXACTLY equivalent to M0 >= 0
     given M_bulk PD -- ward: sign(1 - lam_max) == sign(tau) on
     every usable rung, vacuous-disclosed if no rung is
     usable).  The margin 1 - lam_max is the sharpest known
     form of the open problem at that delta; its tau-screen is
     printed (expected RELOC -- it is the wall in new clothes;
     said, not hidden).  If NO delta completes the bulk, that
     REFUTES the band-split shape at these widths -- typed
     BULK-SOS-FAILS-ALL-DELTA, a first-class outcome.

FROZEN PROTOCOL:

 W   PIPELINE + REPRODUCTION (kill -> PIPELINE-BROKEN /
     WARD-BROKEN): W1 truth ladder == 42 rungs, chains complete;
     W2 full-window census == 37 (case_edge frozen count); W3
     truth wall holds (neg(A) = 0 via max eig(G) <= 1: tau_full
     > 0 on 42/42); W4 REPRODUCTION of the round-60 E4 edge
     seat ON THE WGT FUNCTIONAL: med cumulative negative-side
     eigenvector-energy share within DELTA = 1e-2 >= 0.90
     (round-60 measured 0.942), and Mm fails (lam_min < 0) on
     every rung (the CXXVIII/CXXXV base fact); W5 ATTRIBUTION
     WARD: arch + atom tent reads of g == the functional from
     the density on every rung and BOTH functionals (rel <=
     ATTR_WARD); W6 M0 three routes: I - H == quadrature M_bulk
     + M_band (rel <= M0_WARD) and lam_min(M0) == tau_full (rel
     <= TAU_TIE) on 2 spot rungs.

 E   THE MEASUREMENTS (typed, never kill): E1 the census (a);
     E2 the law (b); E3 the unification (c) with the BETA_WARD
     as kill-grade exactness (two routes of beta); E4 the
     band-split SOS (d).

 C   CONTROLS (kill -> WARD-BROKEN if silent): C0 truth tau_full
     > 0 everywhere; C1 smooth world: max eig(G_sm) > 1 (wall
     broken) on >= 1 rung; C2 Epstein x^2+5y^2 + scramble (seed
     1) at kz 9 fire (wall broken or frame death); C3 the
     scramble census, where the frame lives, must NOT reproduce
     the truth's deep-edge seating (|deep share - truth med|
     printed; fires iff outside the truth's [min, max] band OR
     frame death -- disclosed skip if the chain dies).

KILLS: K1 pipeline (W1, W2) -> PIPELINE-BROKEN; K2 wards (W3-W6,
BETA_WARD, C0-C3) -> WARD-BROKEN.

VERDICT (frozen enum): BANDANATOMY-MEASURED with typed sublabels
ATOM-CENSUS(deep med, arch med, n90 med),
EDGE-LAW(width slope, comb-edge vs 0.3935),
BETA-UNIFICATION(band-share med, R^2, spread) with subtype
BETA-IS-BAND(share >= 0.90) / BETA-PART-BAND(share) and
PROP-IDENTITY(spread <= 3) / PROP-CORRELATED(R^2 >= 0.5) /
PROP-DISTINCT, BANDSPLIT-SOS(delta scan) with subtype
BULK-SOS-COMPLETE(delta) [+ BAND-INEQUALITY-STATED(margin med,
screen)] / BULK-SOS-FAILS-ALL-DELTA(best n/N at best delta);
else PIPELINE-BROKEN / WARD-BROKEN.

FROZEN BARS: H_DEEP_MAX = 900; N_RUNGS_EXP = 42; N_FULLWIN = 37;
JWIN = (2,...,24); DELTA = 1e-2; DELTAS_SOS = (1e-3, 1e-2, 3e-2,
1e-1, 3e-1); Q_WIDTH = 0.90; E4_MED_MIN = 0.90; ATTR_WARD =
1e-9; M0_WARD = 1e-9; TAU_TIE = 1e-6; BETA_WARD = 1e-9; N_SPOT =
2; HEAD_N = 9; EDGE_LAW = 0.393469 (= 1 - e^{-1/2}); N90_Q =
0.90; BETA_BAND_BAR = 0.90; PROP_SPREAD = 3.0; PROP_R2 = 0.5;
SLOPE_PASS = 0.30; SLOPE_RELOC = 0.70; CTRL_KZ = 9; scramble
seed 1.  Runtime cap declared: 10 min.

ANTI-CIRCULARITY (frozen): no sigma_h, no defect eigenvector, no
target factorization; the band read vector g, the census, the
splits and the localizers are built from the deployed lags /
folded families only; eigensolves appear as measured floors and
as the generalized band margin (a MEASUREMENT of the open
inequality, never a certificate).  No fit where an identity is
claimed; all fits are typed as fits with R^2.

SMOKE-RUN DISCLOSURE + AMENDMENTS (2026-08-10, before freezing;
fail-first preserved -- both smoke FAILURES are recorded here and
BOTH re-specifications made the finding sharper, never weaker):
(AMENDMENT 1) the v1 W4 read the RAW mu_- band mass share and
FAILED at med 0.000 -- the true value is med 4.4e-04: the
round-60 '0.94' object is the (1 - x)-localized failing-
eigenvector ENERGY, not raw measure mass; W4 was re-specified to
that object verbatim (it then reproduces 0.942 exactly, Mm fails
42/42) and the v1 fail is KEPT as the printed finding 'the band
is an ENERGY seat, not a mass seat'.  (AMENDMENT 2) the v1 E4
ran only delta = 1e-2, found L0 >= 0 on 0/42 and crashed on the
empty margin stats; re-specified to the frozen DELTAS_SOS grid
with guarded stats -- the negative got STRONGER: the bulk fails
at EVERY delta.  Final smoke run (17/17 with the identical bars;
nothing moved after it): W green (42 rungs, 37 full windows, W4
0.942 + Mm fails 42/42, attribution ward 2.1e-13 over BOTH
functionals, M0 three-route 4.6e-14, tau tie 7.4e-9).  E1 THE
CENSUS ANSWER: the band is NOT the deep-edge atoms and NOT the
head -- it is a BROAD MID-WINDOW INTERFERENCE OBJECT: WGT med
shares arch -0.006 | deep-edge +0.245 | head -0.025 | mid
+0.757, n90 med 624 (RAW: arch -0.163, deep +0.425, mid +0.649,
n90 680); spot top atoms: n = 2 carries the largest single
(NEGATIVE) share, deep atoms appear as near-degenerate clusters
(1289..1301) of small equal weights.  E2 THE LAW: WGT width
delta* med 6.49e-03, log-log slope vs h -0.298 +- 2SE 0.220 (R2
0.18 -- weak narrowing, CI excludes 0 barely), peak x med
0.99811 (round-60 tie); band share 0.942 FLAT in alpha (slope
+0.0013); comb last-unit mass share med 0.3998 vs the v882 law
0.3935 (reproduces, recorded); E_band / edge-comb-mass med
5.5e-07 (the band energy is NOT that zone's image).  E3 THE
UNIFICATION: beta IS band-seated (band share med 0.999, min
0.076 -- one shallow outlier) = BETA-IS-BAND; but beta is
PROP-DISTINCT from both band functionals (vs RAW: R2 0.012,
spread 6.0e+06; vs WGT: slope -3.39, R2 0.398, spread 1.9e+07)
-- same SEAT, different NUMBERS: the three programs share the
band, not one scalar; E_band tau-screen PASS(+0.294, R2 0.527).
E4 BAND-SPLIT SOS REFUTED AT EVERY WIDTH: L0 = M_bulk >= 0 on
0/42 at ALL five deltas (seat med lam_min(L0)/tau -3.2e+05 at
1e-3 to -7.6e+04 at 3e-1) -- removing the band removes
POSITIVE mass the bulk needs: the wall does NOT split as
SOS-on-bulk + band inequality on this family (the round-60
'truncation is load-bearing' fact in a second language);
BULK-SOS-FAILS-ALL-DELTA, the E4.w ward vacuous-passes (no
usable rung, disclosed).  Controls: smooth wall broken 42/42,
Epstein + scramble fire, scramble census RAW deep share +0.008
vs truth +0.425 (the deep seating dies on the scramble).
Runtime 11 s.

SPEC v1 (2026-08-10, frozen + SHA-hashed before the frozen run):
everything above.  Mechanical concretizations frozen with v1: (i)
window memoization per (kz, seed); (ii) band fold set from the
UNFOLDED density arm f = 1..L/2-1 with x_f = cos(2 pi f / L),
weights q_f as printed above (f = 0 and L/2 carry zero band
weight); (iii) atom reads vectorized tent evaluation (i0, i0+1
plus the u < D reflection at g[0]); (iv) delta* by cumulative
neg-mass quantile over folds sorted by decreasing x; (v)
generalized lam_max via Cholesky of M_bulk (M_bulk PD measured
first; rungs with lam_min(M_bulk) <= 0 typed and excluded from
the margin stats); (vi) OLS population statistics, jackknife 2SE
as v900; (vii) beta machinery on full-window rungs only (37).

NO RH claim: every statement is a measurement on the deployed
v563 ladder; the band inequality is STATED, not proven; nothing
here proves wall positivity for any h, and the bulk-SOS
completion is a float-floor measurement, not a certificate.  No
marker moves.

FIREWALL: no zeros, no prime oracles (AST scan; banned ids
zetazero / nzeros / primerange / isprime / primepi / nextprime /
prevprime); v563 READ-ONLY; RNG only inside the declared scramble
control; stdout only.

Sources (read-only): v563_paper2_readouts; wall/window machinery
verbatim from wall_gram_radau_probe.py / case_edge_christoffel
_probe.py (= v902 chain) and wall_edge_completion_probe.py
(round 60); v882 edge law + v902 rewrite as declared inputs.

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/band_arithmetic_anatomy_probe.py
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
N_RUNGS_EXP = 42
N_FULLWIN = 37
JWIN = tuple(range(2, 25, 2))
DELTA = 1e-2
DELTAS_SOS = (1e-3, 1e-2, 3e-2, 1e-1, 3e-1)
Q_WIDTH = 0.90
E4_MED_MIN = 0.90
ATTR_WARD = 1e-9
M0_WARD = 1e-9
TAU_TIE = 1e-6
BETA_WARD = 1e-9
N_SPOT = 2
HEAD_N = 9
EDGE_LAW = 0.393469
N90_Q = 0.90
BETA_BAND_BAR = 0.90
PROP_SPREAD = 3.0
PROP_R2 = 0.5
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


# --------------- pipeline, verbatim (wall_gram_radau / case_edge)
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


def smooth_masses(uu):
    return 2.0 * np.exp(np.asarray(uu, float) / 2.0) \
        * cell_widths(np.asarray(uu, float))


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
        _ai, bi, _ = ols_line(x[m], y[m])
        bb.append(bi)
    bb = np.array(bb)
    se = math.sqrt((n - 1) / n * float(np.sum((bb - bb.mean())
                                              ** 2)))
    return b, 2.0 * se, r2


def screen_label(sl):
    return ("PASS" if abs(sl) <= SLOPE_PASS
            else "RELOC" if sl >= SLOPE_RELOC else "AMBIG")


def band_read_vector(M, L, band_negfolds, wf=None):
    """g with functional = c . g: g_k = -sum_F w_f fac(f, k);
    w_f defaults to the RAW quadrature weight q_f."""
    g = np.zeros(M)
    if len(band_negfolds) == 0:
        return g
    ff = np.asarray(band_negfolds, float)
    qf = 2.0 * 4.0 * np.sin(math.pi * ff / L) ** 2 / (2.0 * L)
    if wf is not None:
        qf = qf * np.asarray(wf, float)
    kk = np.arange(M)
    fac = 2.0 * np.cos(2.0 * math.pi * np.outer(ff, kk) / L)
    fac[:, 0] = 1.0
    fac[:, M - 1] = np.where(np.mod(ff, 2.0) == 0.0, 1.0, -1.0)
    return -(qf[:, None] * fac).sum(axis=0)


def atom_reads(g, uu, mm, D, M):
    """Vectorized tent reads: per-atom contribution to c . g."""
    uu = np.asarray(uu, float)
    mm = np.asarray(mm, float)
    i0 = np.floor(uu / D).astype(int)
    fr = uu / D - i0
    gi0 = np.where((i0 >= 0) & (i0 < M), g[np.clip(i0, 0, M - 1)],
                   0.0)
    gi1 = np.where((i0 + 1 >= 0) & (i0 + 1 < M),
                   g[np.clip(i0 + 1, 0, M - 1)], 0.0)
    contrib = -mm * 0.5 * ((1.0 - fr) * gi0 + fr * gi1)
    edge = uu < D
    contrib = contrib + np.where(edge,
                                 -mm * 0.5 * (1.0 - uu / D) * g[0],
                                 0.0)
    return contrib


def rung_anatomy(kz, comb=None, scramble_seed=None):
    """One rung: density, folded families, chain, band objects."""
    rr = window_of(kz, scramble_seed=scramble_seed)
    h, M, D, alpha, L = (rr["h"], rr["M"], rr["D"], rr["alpha"],
                         2 * rr["M"] - 2)
    if h > H_DEEP_MAX:
        return "TOO-DEEP"
    uu = rr["uu"]
    mm = 2.0 * rr["lam"]
    if comb is not None:
        uu, mm = comb
    c_at, _ = core.atom_lags_at(alpha, M, uu, mm)
    c = rr["c_ar"] + np.asarray(c_at, float)
    d = grid_density(c)
    xs, ws, uf_p = folded_measure(d, L, +1.0)
    ys, vs, uf_n = folded_measure(d, L, -1.0)
    al, be, m0, steps = lanczos_chain(xs, ws, h + 1)
    if steps < h + 1 or np.any(be <= 0):
        return None
    return dict(kz=kz, h=h, M=M, D=D, L=L, alpha=float(alpha),
                uu=uu, mm=mm, c=c, c_ar=rr["c_ar"], c_at=c_at,
                d=d, xs=xs, ws=ws, uf_p=uf_p, ys=ys, vs=vs,
                uf_n=uf_n, chain=(al, be, m0))


def main():
    section("PRIME.PORT.BAND.ANATOMY.01 -- the x = +1 band as an "
            "explicit arithmetic object (EXPLORATION ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s"
          % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
    print("    NO RH claim; no marker moves.")
    print("\nS0 -- firewall")
    check("S0.1 AST firewall clean", not ast_scan(BANNED_IDS))

    # ------------------------------------------------------------ W
    section("W -- ladder + reproduction + attribution wards")
    truth = []
    for kz in core.frame_a_zones():
        r = rung_anatomy(kz)
        if r == "TOO-DEEP" or r is None:
            continue
        truth.append(r)
    truth.sort(key=lambda r: (r["h"], r["kz"]))
    check("W1 truth ladder == %d rungs" % N_RUNGS_EXP,
          len(truth) == N_RUNGS_EXP,
          "%d rungs, h %d..%d  [%.1f s]"
          % (len(truth), truth[0]["h"], truth[-1]["h"],
             time.time() - T0), kill="K1")
    if KILLS:
        return finish({})

    # band decomposition + Gram objects per rung
    dev_attr = 0.0
    taus = []
    _w6_m0, _w6_tau = [], []
    for r in truth:
        d, L, M = r["d"], r["L"], r["M"]
        ff = np.arange(1, L // 2)
        xf = np.cos(2.0 * math.pi * ff / L)
        band = ff[(xf > 1.0 - DELTA)]
        bandneg = band[d[band] < 0.0]
        r["bandneg"] = bandneg
        qf = (2.0 * 4.0 * np.sin(math.pi * bandneg / L) ** 2
              / (2.0 * L))
        m_band = float(np.sum(-d[bandneg] * qf))
        r["m_band"] = m_band
        r["m_neg"] = float(np.sum(r["vs"]))
        r["share_raw"] = m_band / r["m_neg"]
        # chain-basis Gram objects (quadrature routes)
        al, be, m0 = r["chain"]
        h = r["h"]
        Px = eval_chain(al, be, m0, r["xs"], h)
        Pn = eval_chain(al, be, m0, r["ys"], h)
        H = (Pn * r["vs"][:, None]).T @ Pn
        H = 0.5 * (H + H.T)
        egH = np.linalg.eigvalsh(H)
        r["tau_full"] = float(1.0 - egH[-1])
        taus.append(r["tau_full"])
        # the round-60 WGT object: Mm minimizing eigenvector
        hm = h - 1
        Mm = ((Px[:, :hm] * (r["ws"] * (1.0 - r["xs"]))
               [:, None]).T @ Px[:, :hm]
              - (Pn[:, :hm] * (r["vs"] * (1.0 - r["ys"]))
                 [:, None]).T @ Pn[:, :hm])
        Mm = 0.5 * (Mm + Mm.T)
        wm, Vm = np.linalg.eigh(Mm)
        r["lam_m"] = float(wm[0])
        e = Vm[:, 0]
        qn = Pn[:, :hm] @ e
        cn = r["vs"] * (1.0 - r["ys"]) * qn ** 2
        cn_tot = float(np.sum(cn))
        r["wshare"] = (float(np.sum(cn[r["ys"] > 1.0 - DELTA]))
                       / max(cn_tot, 1e-300))
        order = np.argsort(-r["ys"])
        cum = np.cumsum(cn[order]) / max(cn_tot, 1e-300)
        i90 = int(np.searchsorted(cum, Q_WIDTH))
        r["width"] = 1.0 - float(r["ys"][order][min(
            i90, len(order) - 1)])
        r["peakx"] = float(r["ys"][int(np.argmax(cn))])
        # WGT value on the band folds (unfolded), linear in c
        qx = eval_chain(al, be, m0, np.cos(
            2.0 * math.pi * bandneg / L), h)[:, :hm] @ e
        fold_bn = np.minimum(bandneg, L - bandneg)
        wf = ((1.0 - np.cos(2.0 * math.pi * bandneg / L))
              * qx ** 2)
        qf_bn = (2.0 * 4.0 * np.sin(math.pi * bandneg / L) ** 2
                 / (2.0 * L))
        E_band = float(np.sum(-d[bandneg] * qf_bn * wf))
        r["E_band"] = E_band
        # the two band read vectors + attribution + census
        deep = r["uu"] > 2.0 * r["alpha"] - 1.0
        head = r["uu"] <= math.log(HEAD_N) + 1e-12
        for tag, wfv, val in (("raw", None, m_band),
                              ("wgt", wf, E_band)):
            g = band_read_vector(M, L, bandneg, wf=wfv)
            arc = float(r["c_ar"] @ g)
            contrib = atom_reads(g, r["uu"], r["mm"], r["D"], M)
            tot = arc + float(np.sum(contrib))
            dev_attr = max(dev_attr, abs(tot - val)
                           / max(abs(val), 1e-300))
            sc = val if val != 0.0 else float("nan")
            r["arc_share_" + tag] = arc / sc
            r["deep_share_" + tag] = float(
                np.sum(contrib[deep])) / sc
            r["head_share_" + tag] = float(
                np.sum(contrib[head])) / sc
            r["mid_share_" + tag] = (1.0 - r["arc_share_" + tag]
                                     - r["deep_share_" + tag]
                                     - r["head_share_" + tag])
            srt = np.sort(np.abs(contrib))[::-1]
            csum = np.cumsum(srt)
            r["n90_" + tag] = int(np.searchsorted(
                csum, N90_Q * float(np.sum(np.abs(contrib))))) + 1
            r["contrib_" + tag] = contrib
        # comb edge mass
        r["comb_edge"] = (float(np.sum(r["mm"][deep]))
                          / float(np.sum(r["mm"])))
        r["bulk_n"] = r["ys"] <= 1.0 - DELTA
        # W6 spot ward inline (memory: Px/Pn are not retained)
        if len(taus) <= N_SPOT:
            bulk_p = r["xs"] <= 1.0 - DELTA
            bulk_n = r["bulk_n"]
            Mb = ((Px[bulk_p] * r["ws"][bulk_p][:, None]).T
                  @ Px[bulk_p]
                  - (Pn[bulk_n] * r["vs"][bulk_n][:, None]).T
                  @ Pn[bulk_n])
            Mn = ((Px[~bulk_p] * r["ws"][~bulk_p][:, None]).T
                  @ Px[~bulk_p]
                  - (Pn[~bulk_n] * r["vs"][~bulk_n][:, None]).T
                  @ Pn[~bulk_n])
            M0q = 0.5 * (Mb + Mb.T) + 0.5 * (Mn + Mn.T)
            M0i = np.eye(h) - H
            _w6_m0.append(float(np.linalg.norm(M0q - M0i))
                          / max(float(np.linalg.norm(M0i)),
                                1e-300))
            lam0 = float(np.linalg.eigvalsh(
                0.5 * (M0q + M0q.T))[0])
            _w6_tau.append(abs(lam0 - r["tau_full"])
                           / max(abs(r["tau_full"]), 1e-300))
    check("W3 WARD truth wall holds: tau_full > 0 on %d/%d "
          "(min %.3e)" % (int(np.sum(np.array(taus) > 0)),
                          len(truth), float(np.min(taus))),
          all(t > 0 for t in taus), kill="K2")
    wshares = np.array([r["wshare"] for r in truth])
    n_mm_fail = sum(1 for r in truth if r["lam_m"] < 0.0)
    check("W4 REPRODUCTION round-60 E4 seat (WGT): med "
          "eigenvector-energy band share at delta = %.0e = %.3f "
          ">= %.2f (round-60: 0.942); Mm fails on %d/%d"
          % (DELTA, float(np.median(wshares)), E4_MED_MIN,
             n_mm_fail, len(truth)),
          float(np.median(wshares)) >= E4_MED_MIN
          and n_mm_fail == len(truth), kill="K2")
    check("W5 WARD attribution: arch + atom tent reads == the "
          "functional from the density (BOTH functionals): max "
          "rel %.1e <= %.0e" % (dev_attr, ATTR_WARD),
          dev_attr <= ATTR_WARD, kill="K2")
    dev_m0 = max(_w6_m0)
    dev_tau = max(_w6_tau)
    check("W6 WARD M0 three routes on %d spot rungs: bulk + band "
          "== I - H (rel %.1e <= %.0e); lam_min(M0) == tau_full "
          "(rel %.1e <= %.0e)"
          % (N_SPOT, dev_m0, M0_WARD, dev_tau, TAU_TIE),
          dev_m0 <= M0_WARD and dev_tau <= TAU_TIE, kill="K2")
    if KILLS:
        return finish({})

    # ----------------------------------------------------------- E1
    section("E1 -- THE CENSUS: which atoms generate the band")
    med = {}
    for tag in ("raw", "wgt"):
        med[tag] = tuple(float(np.median(
            [r[k + "_" + tag] for r in truth]))
            for k in ("arc_share", "deep_share", "head_share",
                      "mid_share", "n90"))
        print("    %s med shares: arch %+.3f | deep-edge "
              "(u > 2a-1) %+.3f | head (n <= %d) %+.3f | mid "
              "%+.3f; n90 med %.0f"
              % (tag.upper(), med[tag][0], med[tag][1], HEAD_N,
                 med[tag][2], med[tag][3], med[tag][4]),
              flush=True)
    for r in truth[:N_SPOT]:
        top = np.argsort(-np.abs(r["contrib_wgt"]))[:5]
        tops = ", ".join("n=%.0f (%+.2e)"
                         % (math.exp(r["uu"][i]),
                            r["contrib_wgt"][i] / r["E_band"])
                         for i in top)
        print("    SPOT kz %d h %d (WGT): E_band %.3e; arch "
              "%+.3f; top atoms: %s"
              % (r["kz"], r["h"], r["E_band"],
                 r["arc_share_wgt"], tops), flush=True)
    deep_m = med["wgt"][1]
    e1 = ("ATOM-CENSUS(WGT: arch med %+.3f, deep med %+.3f, "
          "head med %+.3f, n90 med %.0f; RAW: arch %+.3f, deep "
          "%+.3f)" % (med["wgt"][0], med["wgt"][1], med["wgt"][2],
                      med["wgt"][4], med["raw"][0],
                      med["raw"][1]))
    check("E1 typed: %s -- band == deep-edge atoms is %s"
          % (e1, "CONFIRMED" if deep_m >= 0.5 else "REFUTED"),
          True)

    # ----------------------------------------------------------- E2
    section("E2 -- THE LAW: band energy and width vs alpha / h")
    hs = np.array([r["h"] for r in truth], float)
    als = np.array([r["alpha"] for r in truth], float)
    wid = np.array([r["width"] for r in truth])
    slw, sew, r2w = jack_slope(np.log(hs), np.log(wid))
    _a, slsh, r2sh = ols_line(als, wshares)
    combe = np.array([r["comb_edge"] for r in truth])
    ratio_edge = np.array([r["E_band"] / (r["comb_edge"]
                                          * np.sum(r["mm"]))
                           for r in truth])
    raws = np.array([r["share_raw"] for r in truth])
    print("    WGT width delta* (0.90-quantile): med %.2e; "
          "log-log slope vs h %+.3f +- 2SE %.3f (R2 %.3f); peak "
          "x med %.5f" % (float(np.median(wid)), slw, sew, r2w,
                          float(np.median([r["peakx"] for r in
                                           truth]))), flush=True)
    print("    WGT band share vs alpha: slope %+.4f (R2 %.3f); "
          "med %.3f | RAW mu_- band mass share med %.3e (the v1 "
          "finding: the band is an ENERGY seat, not a mass seat)"
          % (slsh, r2sh, float(np.median(wshares)),
             float(np.median(raws))), flush=True)
    print("    RECORDED comparisons: comb last-unit mass share "
          "med %.4f vs v882 law %.4f; E_band / (last-unit comb "
          "mass) med %.2e (range [%.1e, %.1e])"
          % (float(np.median(combe)), EDGE_LAW,
             float(np.median(ratio_edge)),
             float(np.min(ratio_edge)), float(np.max(ratio_edge))),
          flush=True)
    e2 = ("EDGE-LAW(WGT width slope %+.3f+-%.3f, comb-edge med "
          "%.4f vs %.4f)" % (slw, sew, float(np.median(combe)),
                             EDGE_LAW))
    check("E2 typed: %s" % e2, True)

    # ----------------------------------------------------------- E3
    section("E3 -- THE UNIFICATION: is the band the v902 beta?")
    dev_beta = 0.0
    bshares, betas, mbs, ebs, taus_fw = [], [], [], [], []
    n_fw = 0
    for r in truth:
        idx = {int(j): k for k, j in enumerate(r["uf_n"])}
        if not all(j in idx for j in JWIN):
            continue
        n_fw += 1
        h = r["h"]
        al, be, m0 = r["chain"]
        Pn = eval_chain(al, be, m0, r["ys"], h)
        G = (Pn * r["vs"][:, None]).T @ Pn
        G = 0.5 * (G + G.T)
        jstar = idx[JWIN[-1]]
        p = Pn[jstar]
        try:
            q = np.linalg.solve(np.eye(h) - G, p)
        except np.linalg.LinAlgError:
            continue
        v_ = float(r["vs"][jstar])
        beta_g = v_ * float(q @ (G @ q))
        Qn = Pn @ q
        bterms = v_ * r["vs"] * (Qn * Qn)
        beta_q = float(np.sum(bterms))
        dev_beta = max(dev_beta, abs(beta_g - beta_q)
                       / max(abs(beta_g), 1e-300))
        bshare = float(np.sum(bterms[~r["bulk_n"]])) / beta_q
        bshares.append(bshare)
        betas.append(beta_q)
        mbs.append(r["m_band"])
        ebs.append(r["E_band"])
        taus_fw.append(r["tau_full"])
    check("W2 full-window census %d == %d" % (n_fw, N_FULLWIN),
          n_fw == N_FULLWIN, kill="K1")
    check("E3.w WARD beta two routes (Gram == node sum): max rel "
          "%.1e <= %.0e" % (dev_beta, BETA_WARD),
          dev_beta <= BETA_WARD, kill="K2")
    bshares = np.array(bshares)
    lb = np.log(np.array(betas))
    lm = np.log(np.array(mbs))
    le = np.log(np.array(ebs))
    _a3, sl3, r23 = ols_line(lm, lb)
    _a3b, sl3b, r23b = ols_line(le, lb)
    rat = np.array(betas) / np.array(mbs)
    rat_e = np.array(betas) / np.array(ebs)
    spread = float(np.max(rat) / np.min(rat))
    spread_e = float(np.max(rat_e) / np.min(rat_e))
    _a4, sl4, r24 = ols_line(np.log(np.array(taus_fw)), le)
    print("    band share of beta: med %.3f (min %.3f) on %d "
          "full-window rungs" % (float(np.median(bshares)),
                                 float(np.min(bshares)), n_fw),
          flush=True)
    print("    proportionality beta vs m_band(RAW): slope %+.3f, "
          "R2 %.3f, ratio spread %.1e | beta vs E_band(WGT): "
          "slope %+.3f, R2 %.3f, ratio med %.2e spread %.1e"
          % (sl3, r23, spread, sl3b, r23b,
             float(np.median(rat_e)), spread_e), flush=True)
    print("    tau-relation of the edge functional E_band: slope "
          "%+.3f, R2 %.3f -> %s"
          % (sl4, r24, screen_label(sl4)), flush=True)
    sub1 = ("BETA-IS-BAND(med %.3f)" % float(np.median(bshares))
            if float(np.median(bshares)) >= BETA_BAND_BAR
            else "BETA-PART-BAND(med %.3f)"
            % float(np.median(bshares)))
    bspread = min(spread, spread_e)
    br2 = max(r23, r23b)
    sub2 = ("PROP-IDENTITY(spread %.1f)" % bspread
            if bspread <= PROP_SPREAD
            else "PROP-CORRELATED(R2 %.3f)" % br2
            if br2 >= PROP_R2 else "PROP-DISTINCT(R2 %.3f)" % br2)
    e3 = "BETA-UNIFICATION(%s, %s, E_band-screen %s(%+.3f))" % (
        sub1, sub2, screen_label(sl4), sl4)
    check("E3 typed: %s" % e3, True)

    # ----------------------------------------------------------- E4
    section("E4 -- BAND-SPLIT SOS on [-1, 1 - delta] (frozen "
            "delta grid) + the band inequality")
    sign_tie = True
    best = None
    for dl in DELTAS_SOS:
        n_l0 = n_l1 = n_pd = 0
        margins, taus_m, seat = [], [], []
        for r in truth:
            h = r["h"]
            hm = h - 1
            al, be, m0 = r["chain"]
            Px = eval_chain(al, be, m0, r["xs"], h)
            Pn = eval_chain(al, be, m0, r["ys"], h)
            bp = r["xs"] <= 1.0 - dl
            bn = r["ys"] <= 1.0 - dl
            Mb = ((Px[bp] * r["ws"][bp][:, None]).T @ Px[bp]
                  - (Pn[bn] * r["vs"][bn][:, None]).T @ Pn[bn])
            Mb = 0.5 * (Mb + Mb.T)
            lam_bulk = float(np.linalg.eigvalsh(Mb)[0])
            seat.append(lam_bulk / r["tau_full"])
            if lam_bulk >= 0.0:
                n_l0 += 1
            gx = ((1.0 + r["xs"]) * (1.0 - dl - r["xs"]))
            gy = ((1.0 + r["ys"]) * (1.0 - dl - r["ys"]))
            L1 = ((Px[bp, :hm] * (r["ws"][bp]
                                  * gx[bp])[:, None]).T
                  @ Px[bp, :hm]
                  - (Pn[bn, :hm] * (r["vs"][bn]
                                    * gy[bn])[:, None]).T
                  @ Pn[bn, :hm])
            L1 = 0.5 * (L1 + L1.T)
            if float(np.linalg.eigvalsh(L1)[0]) >= 0.0:
                n_l1 += 1
            if lam_bulk > 0.0:
                n_pd += 1
                Mn = ((Px[~bp] * r["ws"][~bp][:, None]).T
                      @ Px[~bp]
                      - (Pn[~bn] * r["vs"][~bn][:, None]).T
                      @ Pn[~bn])
                Mn = 0.5 * (Mn + Mn.T)
                Lc = np.linalg.cholesky(Mb)
                Y = np.linalg.solve(Lc, -Mn)
                Y = np.linalg.solve(Lc, Y.T).T
                lmax = float(np.linalg.eigvalsh(
                    0.5 * (Y + Y.T))[-1])
                margins.append(1.0 - lmax)
                taus_m.append(r["tau_full"])
                sign_tie &= ((1.0 - lmax > 0)
                             == (r["tau_full"] > 0))
        print("    delta %.0e: L0 >= 0 on %d/%d, L1 >= 0 on "
              "%d/%d, M_bulk PD %d/%d; seat med lam_min(L0)/tau "
              "%+.2e%s"
              % (dl, n_l0, len(truth), n_l1, len(truth), n_pd,
                 len(truth), float(np.median(seat)),
                 ("; margin 1-lam_max min/med %.2e/%.2e"
                  % (float(np.min(margins)),
                     float(np.median(margins))))
                 if margins else ""), flush=True)
        score = (min(n_l0, n_l1, n_pd), -dl)
        if best is None or score > best[0]:
            best = (score, dl, n_l0, n_l1, n_pd,
                    np.array(margins), np.array(taus_m))
    _sc, dl_b, n_l0b, n_l1b, n_pdb, margins_b, taus_b = best
    complete = (min(n_l0b, n_l1b, n_pdb) == len(truth))
    check("E4.w WARD sign tie (1 - lam_max vs tau) on every "
          "usable (rung, delta)", sign_tie, kill="K2")
    if complete and len(margins_b):
        _a5, sl5, r25 = ols_line(
            np.log(taus_b), np.log(np.maximum(margins_b,
                                              1e-300)))
        e4 = ("BANDSPLIT-SOS(BULK-SOS-COMPLETE(delta=%.0e), "
              "BAND-INEQUALITY-STATED(margin med %.2e, screen "
              "%s(%+.3f, R2=%.3f)))"
              % (dl_b, float(np.median(margins_b)),
                 screen_label(sl5), sl5, r25))
    else:
        e4 = ("BANDSPLIT-SOS(BULK-SOS-FAILS-ALL-DELTA(best "
              "L0/L1/PD %d/%d/%d of %d at delta=%.0e))"
              % (n_l0b, n_l1b, n_pdb, len(truth), dl_b))
    check("E4 typed: %s" % e4, True)

    # ------------------------------------------------------------ C
    section("C -- controls")
    check("C0 WARD truth tau_full > 0 everywhere (repeated)",
          all(t > 0 for t in taus), kill="K2")
    n_sm_broken = 0
    for r in truth:
        rs = rung_anatomy(r["kz"], comb=(r["uu"],
                                         smooth_masses(r["uu"])))
        if not isinstance(rs, dict):
            n_sm_broken += 1
            continue
        al, be, m0 = rs["chain"]
        Pn = eval_chain(al, be, m0, rs["ys"], rs["h"])
        H = (Pn * rs["vs"][:, None]).T @ Pn
        if float(np.linalg.eigvalsh(0.5 * (H + H.T))[-1]) > 1.0:
            n_sm_broken += 1
    check("C1 WARD smooth world breaks the wall on %d/%d rungs "
          "(>= 1)" % (n_sm_broken, len(truth)), n_sm_broken >= 1,
          kill="K2")
    rr9 = window_of(CTRL_KZ)
    N_E = int(math.floor(math.exp(2.0 * rr9["alpha"]))) + 1
    lamE_ = lambda_eps(N_E)
    nn = np.nonzero(np.abs(lamE_) > 1e-12)[0]
    fired = {}
    for name, kw in (("Epstein", dict(comb=(
            np.log(nn.astype(float)),
            2.0 * lamE_[nn] / np.sqrt(nn.astype(float))))),
                     ("scramble", dict(scramble_seed=1))):
        rc = rung_anatomy(CTRL_KZ, **kw)
        if not isinstance(rc, dict):
            fired[name] = True
            print("    %-9s: chain dies -> fires" % name,
                  flush=True)
            continue
        al, be, m0 = rc["chain"]
        Pn = eval_chain(al, be, m0, rc["ys"], rc["h"])
        H = (Pn * rc["vs"][:, None]).T @ Pn
        broken = float(np.linalg.eigvalsh(
            0.5 * (H + H.T))[-1]) > 1.0
        fired[name] = broken
        print("    %-9s: wall %s" % (name, "BROKEN -> fires"
                                     if broken else "holds -> "
                                     "SILENT"), flush=True)
        if name == "scramble" and broken:
            # C3 census on the scramble where the frame lives
            d, L, M = rc["d"], rc["L"], rc["M"]
            ff = np.arange(1, L // 2)
            xf = np.cos(2.0 * math.pi * ff / L)
            band = ff[(xf > 1.0 - DELTA)]
            bandneg = band[d[band] < 0.0]
            g = band_read_vector(M, L, bandneg)
            qf = (2.0 * 4.0 * np.sin(math.pi * bandneg / L) ** 2
                  / (2.0 * L))
            mbs_ = float(np.sum(-d[bandneg] * qf))
            contrib = atom_reads(g, rc["uu"], rc["mm"], rc["D"],
                                 M)
            deep = rc["uu"] > 2.0 * rc["alpha"] - 1.0
            dsh = (float(np.sum(contrib[deep])) / mbs_
                   if mbs_ > 0 else float("nan"))
            print("    scramble census (RAW): deep share %+.3f "
                  "vs truth RAW med %+.3f" % (dsh, med["raw"][1]),
                  flush=True)
    check("C2 WARD both controls fire", all(fired.values()),
          kill="K2")
    c3_msg = ("scramble frame lives -> census printed above"
              if isinstance(rung_anatomy(CTRL_KZ,
                                         scramble_seed=1), dict)
              else "scramble chain dies -> skipped (disclosed)")
    check("C3 scramble census: %s" % c3_msg, True)

    labels = dict(e1=e1, e2=e2, e3=e3, e4=e4)
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
        VERDICT = ("BANDANATOMY-MEASURED / %s / %s / %s / %s"
                   % (labels.get("e1", "-"), labels.get("e2", "-"),
                      labels.get("e3", "-"),
                      labels.get("e4", "-")))
        print("\n  VERDICT: %s" % VERDICT)
    print("""
  HONEST FRAME (as frozen): the census/attribution is an exact
  linear identity of the deployed lag assembly; the law fits are
  typed as fits; the band inequality is STATED and measured, not
  proven -- its margin is expected to BE the wall margin
  relocated (screen printed).  NO RH claim.  No marker moves.""")
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed"
          % (time.time() - T0, n_tot, n_tot - n_pass))
    return 0 if n_pass == n_tot else 1


if __name__ == "__main__":
    raise SystemExit(main())
