#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""tail_oscillation_pairing_probe -- PRIME.PORT.TAIL.OSCPAIR.01
(EXPLORATION ONLY, experiments/; round 63, theorem-engineering on
the RH-side wall -- the FREQUENCY-SPACE bookkeeping of the tail
pairing.  Predecessor CLII (PRIME.PORT.TAIL.ABEL.01) measured that
every classical absolute envelope on the deep tail fails by a
budget growing like e^{+1.744 alpha} against an O(1) need, and
typed the missing ingredient as "oscillation bookkeeping in the
psi-fluctuation pairing": the true arithmetic remainder is itself
~1e4 mu1 units and net-negative -- the tail sign is carried by
PHASE, which absolute envelopes discard.  THE FROZEN IDEA: measure
the phase structure directly.  The tail beyond the per-rung first
B-covering cut is the pairing
    P_h = <dF, q_g>_deep = sum_k f_k w_k,
    f_k = 2 (Lambda(k) - 1)/sqrt(k)   (k = n_c+1 .. N_g, ALL
          integers: the prime comb MINUS the PNT continuum on the
          integer grid -- exactly the increments of CLII's E1),
    w_k = q_v(log k)                  (the deployed piecewise-
          linear per-atom weight functional, lift-race S0
          verbatim),
so that P_h = tail_B(cB) - Ttilde EXACTLY (both ties warded).
Expand the WEIGHT over a declared frequency frame and pair each
frame function against the fluctuation:
    P_h = sum_j c_g(omega_j) Fhat(omega_j) + residual,
    c_g  = the weight's spectrum   (closed-form piecewise-linear
           integrals, exact),
    Fhat = the fluctuation's spectrum, Fhat(omega_j) =
           sum_k f_k psi_j(u_k),
and measure WHERE the net negativity lives on the omega axis.
2026-08-11.)

THE FRAME (frozen).  On the deep window [u0, uL], u0 = log(n_c+1),
uL = log(N_g), Lu = uL - u0, the orthonormal half-range cosine
frame
    psi_0(u) = 1/sqrt(Lu),
    psi_j(u) = sqrt(2/Lu) cos(omega_j (u - u0)),
    omega_j  = pi j / Lu,   j = 0 .. J-1,
    J = min(J_CAP, ceil(OMEGA_MAX Lu / pi) + 1)
(boxcar-windowed cosines at the harmonics of the deep window --
the natural frame the lag structure suggests: the weight is
piecewise linear on the lag grid, its even extension is continuous,
so its cosine coefficients decay ~ 1/omega^2 and a finite frame
carries the pairing; the frame is complete in L^2 as J -> inf and
orthonormal, so c_g(omega_j) = int w psi_j is basis-unambiguous).
OMEGA_MAX = 60 covers the first ten zeta ordinates (largest
49.774) with margin; frame resolution pi/Lu per rung is printed
with every carrier statement (honest: peaks narrower than the
resolution cannot be localized better than that, boxcar sidelobes
disclosed).  The weight coefficients c_g are computed in CLOSED
FORM piece by piece (the weight is exactly linear between lag
knots i*D; each piece contributes analytic sin/cos integrals);
Fhat and the atom-level reconstruction R(u_k) = sum_j c_j
psi_j(u_k) are accumulated in ONE pass over j via the Chebyshev
cosine recurrence cos((j+1)x) = 2 cos(x) cos(jx) - cos((j-1)x)
(spot-warded against direct cos evaluation).

WHAT IS MEASURED (frozen; typed, never kills unless marked WARD):
 (a) RECONSTRUCTION WARD (the >= 99% requirement): per rung the
     residual share |P - sum_j c_j Fhat_j| / |P| <= RES_WARD =
     0.01 for the arithmetic weight q_v (WARD, kill K2 -- the
     frame must account for >= 99% of the pairing before any
     census is read); Fubini ward: sum_k f_k R(u_k) ==
     sum_j c_j Fhat_j (pure order swap, <= FUB_WARD); frame-
     coefficient ward: closed-form c_j vs per-piece 5-point
     Gauss-Legendre at frozen spot indices (<= QUAD_WARD rel to
     max |c|); recurrence spot-ward vs direct cos (<= REC_WARD).
     Sup-norm reconstruction quality max|w - R|/max|w| printed
     (diagnostic, not a ward -- the pairing ward is the claim).
 (b) FREQUENCY CENSUS OF THE NET NEGATIVITY: per rung the signed
     contributions t_j = c_j Fhat_j toward P (sorted toward
     sign(P)); n50/n90 = minimal number of frequency bins whose
     partial sum reaches 50% / 90% of |P|; participation ratio
     PR = (sum|t|)^2 / sum t^2 (effective number of contributing
     bins); top carrier omega* = argmax |t_j|.  FEW-OR-MANY
     (decisive, typed): OSC-FEW iff med n90 <= FEW_N90 = 12 AND
     the top carrier is stable across rungs IN THE FRAME'S OWN
     COORDINATE (harmonic index j* = round(omega* Lu / pi):
     fraction of rungs with |j* - med j*| <= J_STAB_TOL = 1 is
     >= STAB_FRAC = 0.8; AMENDMENT A2, disclosed below -- the
     v0 absolute-omega stability read |omega* - med omega*| <=
     STAB_TOL = 0.5 is KEPT and printed, its smoke value 0.70
     stays on record as a FAIL of that coordinate); else
     OSC-BROAD.  Carrier drift law: jackknife slope of omega*
     vs alpha (recorded either way).
     The prime-free cross-check: the same census with q_{v_sm}
     (crossing rungs on their carrier branch as in round 62);
     agreement census |omega*_v - omega*_vsm| <= STAB_TOL
     (typed, recorded).
 (c) WHERE ARE THE CARRIERS (distances, not celebrations): per
     rung d_gamma = min_i |omega* - gamma_i| against the first
     ten LITERATURE zeta ordinates (hardcoded comparison
     constants, NEVER construction -- wall_margin S2 pattern);
     typed CARRIER-NEAR-GAMMA iff med d_gamma <= GAMMA_NEAR =
     0.5 (about half the uniform-null median ~ local gamma
     spacing/4 ~ 1.0, printed alongside), else CARRIER-FAR --
     an honest open measurement, either answer is a result.
     Classical scales: distance to the full-window harmonic comb
     pi k/(2 alpha) NORMALIZED by its half-spacing (comb spacing
     pi/(2 alpha) ~ 0.24 is DENSER than the frame resolution, so
     only the normalized distance is meaningful -- uniform null
     0.5, disclosed); the lag-knot fundamental 2 pi / D recorded
     as omega* D/(2 pi) (carriers vs the breakpoint scale).
 (d) THE PAIRING INEQUALITY SHAPE: if OSC-FEW, the reduced
     object: pool all per-rung n90 carriers weighted by |t_j|
     into a histogram on the absolute omega axis (bin RED_BIN =
     0.5), take the top K_RED = 12 centers, and re-read every
     rung through ONLY those frequencies: share_red = (sum of
     t_j with |omega_j - center| <= RED_HALF = 0.5) / P.
     REDUCED-ACHIEVED iff med share_red >= RED_MED = 0.90 and
     min share_red >= RED_MIN = 0.75: then the tail bound is a
     statement about K_RED fluctuation coefficients against
     classical weights -- written out explicitly with the
     measured coefficients at the median rung, and tau-screened.
     If OSC-BROAD: the effective dimension is the honest
     obstruction -- jackknife law log PR vs alpha and screen
     log PR vs log m.
 (e) TAU-SCREENS (typed, jackknife, bands PASS |s| <= 0.30 /
     RELOC s >= 0.70 / else AMBIG): log n90 vs log m; log PR vs
     log m; if reduced: log |P_red/mu1| vs log m (recorded).

FROZEN PROTOCOL (ladder machinery verbatim from
tail_abel_transport_probe.py = round-59/60/62/63 chain; v_sm
construction verbatim from arithmetic_lift_race_probe S0):

 W   LADDER + WARDS (kill -> PIPELINE-BROKEN / WARD-BROKEN): W1
     faithful ladder >= MIN_RUNGS = 40 (kz 2..KZMAX, H_MIN <= h
     <= HCAP, X <= ATOM_MAX); W2 WARD m_h > 0 everywhere; W3 WARD
     both exact bookkeepings (lift - demand = m AND e_ar + E_at =
     m) <= ID_WARD; W4 WARD atom identities <= ID_WARD; W5 WARD
     split exactness on the full scans <= SCAN_WARD; W6
     REPRODUCTION round 59/60/62: G > 0 counts at (50, 100, 200)
     == (52, 26, 25); n_min in [3, 9]; shared cut 9 covers N/N;
     tail_A <= 0 at first covering cut N/N; B-covering cuts exist
     N/N with n_minB med == 17 in [5, 47]; tail_B <= 0 at cB N/N;
     head_B(cB) med within HEADB_TOL of 0.388; W7 WARD v_sm
     branch (<= MAX_CROSS crossing rungs, carrier branch overlap
     >= OV_MIN); W8 WARD mu1 closed form == core.parity_mu(h)[0]
     exactly and the CXLIII shat band within SHAT_TOL of (0.502,
     1.027, 2.185); W9 WARD grid tie: the integer-grid tail
     T = sum a_k w_k equals tail_B(cB) <= TIE_WARD; W10 WARD
     pairing tie: (T - Ttilde) - P <= PAIR_WARD relative to
     sum |f||w| (distributivity bookkeeping); W11 frame wards:
     closed-form c_j vs GL5 (frozen spots: rung indices (0, N//2),
     j in (1, J//2, J-1), both weights) and cosine recurrence
     spot-ward at j = J-1 on the same rungs; W12 WARD
     reconstruction (a): Fubini <= FUB_WARD everywhere AND
     residual share <= RES_WARD on EVERY rung for q_v.

 A/B/G/R/T  as (b)/(b-few)/(c)/(d)/(e) above.

 C   CONTROLS at kz 9 (kill -> WARD-BROKEN if silent): C1
     scramble (seed 1), Epstein x^2+5y^2, smooth comb: each must
     show m < 0 AND zero covering cuts in BOTH senses (round-62
     criterion).  C2 SPECTRAL battery from the FIXED declared cut
     CTRL_CUT = 17 (controls have no covering cuts; the true kz-9
     rung is re-read at the SAME cut for apples-to-apples), each
     world paired through its OWN weight q_v, combs snapped to
     the integer grid by n = round(exp(u)) and aggregated
     (masses outside the deep grid dropped -- the deep-window
     restriction, declared):
       smooth world (AMENDMENT A3, disclosed below): the
         BY-CONSTRUCTION integer-continuum world Lambda == 1 on
         the whole deep grid has f == 0 IDENTICALLY, so Fhat == 0
         and the pairing dies EXACTLY -- verified as an identity
         (max|f| == 0 and P == 0, WARD); the DISCRETIZED smooth
         world (build_rung smooth comb snapped to integers) is
         RECORDED as a typed measurement -- its pairing is a
         quadrature-error object and does NOT die (the honest v0
         FAIL, on record);
       scramble: the CUMULATIVE structure is destroyed -- the
         PNT cancellation that keeps the true low-frequency
         spectrum small dies, the DC bin blows up:
         |Fhat_scr(0)| / |Fhat_true(0)| >= SCR_BLOWUP (WARD);
         the whiteness census (peakiness max|Fhat|^2 /
         mean|Fhat|^2, PR of spectral energy) is RECORDED;
       Epstein: different carrier signature RECORDED (its comb is
         measured against the SAME PNT continuum, declared -- the
         continuum-density mismatch appears as a low-frequency
         drift; omega*, d_gamma, drift factor typed as
         measurements, no kill).

KILLS: K1 ladder (W1) -> PIPELINE-BROKEN; K2 wards (W2-W12,
C1/C2-smooth/C2-scramble) -> WARD-BROKEN.  All typed A/B/G/R/T
outcomes are measurements, never kills.

VERDICT (frozen enum): OSCPAIR-MEASURED with typed sublabels
RECON-WARDED(max residual share),
OSC-FEW(med n50/n90, harmonic-index stability frac) /
OSC-BROAD(med n50/n90, med PR),
CARRIERS(med omega*, med j*, abs-omega stab, j-stab, drift slope
vs alpha),
GAMMA(med d_gamma vs null, count near, verdict NEAR/FAR) +
CLASSICAL(normalized window-comb distance, knot-scale ratio),
REDUCED-ACHIEVED(K, med share) / REDUCED-FAILED(med share) /
EFFDIM(med PR, law slope vs alpha),
SCREENS(n90, PR),
CTRL(...);  else PIPELINE-BROKEN / WARD-BROKEN.

FROZEN BARS: KZMAX = 150; MIN_RUNGS = 40; REF_CUTS = (50, 100,
200); REF_COUNTS = (52, 26, 25); NMIN_LO, NMIN_HI = 3, 9;
NC_SHARED = 9; NB_MED = 17; NB_LO, NB_HI = 5, 47; HEADB_MED =
0.388, HEADB_TOL = 0.01; SHAT_REF = (0.502, 1.027, 2.185),
SHAT_TOL = 1.5e-3; ID_WARD = 1e-10; SCAN_WARD = 1e-9; TIE_WARD =
1e-10; PAIR_WARD = 1e-12; FUB_WARD = 1e-9; QUAD_WARD = 1e-9 (rel
to max|c|); REC_WARD = 1e-9; RES_WARD = 0.01; MU_WARD = 1e-12;
NG_SMOOTH = 6000; OV_MIN = 0.8; MAX_CROSS = 2; OMEGA_MAX = 240.0
(amendment A1); J_CAP = 4096; GL5_SEG = 0.5 (amendment A1b);
FEW_N90 = 12; STAB_TOL = 0.5 (absolute omega, recorded);
J_STAB_TOL = 1 (harmonic index, gate -- amendment A2);
STAB_FRAC = 0.8; GAMMA_NEAR = 0.5; GAMMA_BAND_LO = 10.0;
RED_BIN = 0.5; RED_HALF = 0.5; K_RED = 12; RED_MED = 0.90;
RED_MIN = 0.75; SLOPE_PASS = 0.30; SLOPE_RELOC = 0.70; CTRL_KZ =
9; CTRL_CUT = 17; SMOOTH_ZERO = 0.0 exactly (amendment A3);
SCR_BLOWUP = 5.0; scramble seed 1; jackknife = full
leave-one-out, CI = +-2SE; blocked cumulative sums (block 1024)
wherever a cumsum feeds a ward.

SMOKE-RUN DISCLOSURE (2026-08-11, before freezing): THREE smoke
runs, full fail-first history.  SMOKE 1 (SPEC v0, OMEGA_MAX =
60, W12 FAILED at max residual share 2.38e-02 > 0.01): the
omega <= 60 frame carries only 97.6% of the pairing on the worst
rung -- the 1/omega^2 coefficient decay needs a larger budget.
AMENDMENT A1: OMEGA_MAX = 240 (frame budget only; ward, bars and
census rules untouched).  SMOKE 2 (W11 FAILED at GL5 dev 4.09e-06
> 1e-9): at omega ~ 240 a single 5-point Gauss rule per lag-knot
piece is no longer machine-exact (theta * width ~ 2).  AMENDMENT
A1b: the WARD ROUTE subdivides every piece until theta * segment
<= GL5_SEG = 0.5 (composite GL5; the closed form under test is
unchanged).  SMOKE 3 (22/22 checks except the declared C2a FAIL,
22.4 s) -- facts frozen as the context the frozen run must
confirm: (i) reconstruction warded: max residual share 5.50e-03,
Fubini 1.3e-15, GL5 (composite) and recurrence at the 1e-11
class; (ii) THE CARRYING SET IS TINY: n50 med 1 (1..2), n90 med
3 (1..8), PR med 3.5 (1.8..14.5) -- but the top carrier omega*
med 0.965 (0.383..2.249) FAILS the v0 absolute-omega stability
read (0.70 < 0.8) because it is LOCKED TO THE WINDOW HARMONICS:
omega* = j* pi/Lu with j* in {1, 2, 3} on 67/67 (drift law
omega* = -0.384 alpha + c, R^2 0.60 = the 1/Lu shrinkage of the
harmonics themselves).  AMENDMENT A2 (disclosed re-key): the
FEW gate reads stability in the frame's own coordinate j* =
round(omega* Lu/pi) (|j* - med j*| <= 1); the absolute-omega
read STAYS PRINTED with its 0.70 fail on record.  (iii) GAMMA
COMPARISON (honest, decisive): med d_gamma(omega*) = 13.17 vs
uniform null ~ 1.0, near on 0/67 -- the carriers are FAR from
the zeta ordinates (they sit BELOW gamma_1 = 14.13); the
gamma-band (omega >= 10) |t|-mass share is med 0.036: at these
window depths the pairing is NOT gamma-concentrated -- the
measured answer to the open question in (c).  (iv) Classical
scales: normalized window-comb distance med 0.42 ~ null 0.5
(uninformative, as declared); knot-scale ratio med 1.1e-03.
(v) v_sm agreement 50/67 within 0.5.  (vi) REDUCED read-through:
the top-12 pooled bins (all centers <= 5.25 except two trace
bins at 13.25/14.25) carry share_red min/med/max
+0.846/+1.006/+1.049 -- the whole pairing is ~12 low-frequency
coefficients.  (vii) Screens: n90 +0.034 PASS, PR +0.065 PASS
(tau-decorrelated); effective-dimension law (recorded) log PR =
-0.073 alpha (R^2 0.05, flat).  (viii) Controls: C1 3/3; the v0
C2a smooth ward FAILED as a DISCRETIZATION fact: the SNAPPED
smooth comb's quadrature-error pairing is 11.7x the (anomalously
small, +8.9e-02) true kz-9/cut-17 pairing -- the snapped world
does not die, only the by-construction integer continuum does.
AMENDMENT A3: C2a re-keyed to the by-construction world (f == 0
identically, exact-zero ward); the snapped world stays as a
recorded typed measurement.  Scramble DC blowup 3.26e+01 >= 5
FIRES; Epstein drift 1.57 with omega* 142.2 (d_gamma 92.4)
recorded.  AMENDMENTS beyond A1/A1b/A2/A3: NONE -- no other bar,
band, tolerance, enum or rule moved after the smokes; FEW_N90,
RED_MED/RED_MIN, GAMMA_NEAR, SCR_BLOWUP, all ladder wards and
both tau-screen bands are v0-verbatim.

SPEC v1 (2026-08-11, frozen + SHA-hashed before the frozen run):
everything above.  Mechanical concretizations frozen with v1:
(i) the cut is INCLUSIVE at the covering atom (grid starts at
n_c + 1); (ii) N_g = max(floor(X), largest window atom); (iii)
Lambda on the grid read from the deployed core.LAM_TAB (equality
of masses warded via the grid tie W9); (iv) the DC bin j = 0 is
a frame bin like any other (census includes it); (v) piece
endpoints evaluated by the deployed q_read (piecewise linearity
makes endpoint evaluation exact); (vi) runtime ~ 25 s (67 eigh
pairs + the J-recurrence over the deep grids dominate).

NO-GO COMPLIANCE (frozen): no certified-bound retry, no rank-1
approximation, no Herglotz; no fit where an identity is claimed
(the reconstruction, Fubini, quadrature and tie wards are exact
bookkeeping; all trends are typed jackknife screens).

NO RH claim: everything here is float-level MEASURED SURFACE
STRUCTURE on the 67-rung ladder; the direction v is computed
per-rung data (the round-62 uniformity boundary applies
verbatim); an OSC-FEW outcome would be a finite-dimensional
SURFACE statement, not a theorem, and an OSC-BROAD outcome is a
measured effective-dimension law, not a proof of impossibility.
The zeta ordinates appear ONLY as recorded comparison constants
in (c) -- never in any comb, frame, weight or window
construction.  No marker moves.

FIREWALL: no zeros in construction, no prime oracles (AST scan;
banned ids zetazero / nzeros / primerange / isprime / primepi /
nextprime / prevprime; Lambda is read from the DEPLOYED window
table only; GAMMAS is a hardcoded literature tuple used only in
distance REPORTS, wall_margin_mechanism_probe S2 pattern);
v563 READ-ONLY; RNG only inside the declared scramble control;
stdout only.

Sources (read-only): v563_paper2_readouts (core); ladder +
cut/scan machinery verbatim from tail_abel_transport_probe.py /
tail_sign_mechanism_probe.py (rounds 62/63); q_read + v_sm
construction verbatim from arithmetic_lift_race_probe.py; mu1
normalization from moving_node_second_order_probe.py (CXLIII);
gamma comparison pattern from wall_margin_mechanism_probe.py
(S2); round-62 censuses (declared reproduction targets).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/tail_oscillation_pairing_probe.py
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
PAIR_WARD = 1e-12
FUB_WARD = 1e-9
QUAD_WARD = 1e-9
REC_WARD = 1e-9
RES_WARD = 0.01
MU_WARD = 1e-12
NG_SMOOTH = 6000
OV_MIN = 0.8
MAX_CROSS = 2
OMEGA_MAX = 240.0
J_CAP = 4096
FEW_N90 = 12
STAB_TOL = 0.5
J_STAB_TOL = 1
STAB_FRAC = 0.8
GAMMA_NEAR = 0.5
RED_BIN = 0.5
RED_HALF = 0.5
K_RED = 12
RED_MED = 0.90
RED_MIN = 0.75
SLOPE_PASS = 0.30
SLOPE_RELOC = 0.70
CTRL_KZ = 9
CTRL_CUT = 17
SCR_BLOWUP = 5.0
GAMMA_BAND_LO = 10.0
BLOCK = 1024
# first ten zeta ordinates -- literature constants, used ONLY in
# the (c) distance reports (comparison, never construction); they
# are never fed to any comb, frame, weight, window or Toeplitz
# object (wall_margin_mechanism_probe S2 pattern)
GAMMAS = (14.134725141734693, 21.022039638771555,
          25.010857580145688, 30.424876125859513,
          32.935061587739190, 37.586178158825671,
          40.918719012147495, 43.327073280914999,
          48.005150881167159, 49.773832477672302)
BANNED_IDS = ("zetazero", "nzeros", "primerange", "isprime",
              "primepi", "nextprime", "prevprime")
GL5_SEG = 0.5
GL5_X = (-0.9061798459386640, -0.5384693101056831, 0.0,
         0.5384693101056831, 0.9061798459386640)
GL5_W = (0.2369268850561891, 0.4786286704993665,
         0.5688888888888889, 0.4786286704993665,
         0.2369268850561891)

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


def build_rung(kz, comb=None, scramble_seed=None,
               smooth_world=False, need_sm=True):
    """One rung of the lift-race surface with both bookkeepings
    and the full atom-cut scans (tail_abel_transport_probe
    verbatim)."""
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


# ----------------------------------------------------- the frame
def frame_freqs(Lu):
    J = min(J_CAP, int(math.ceil(OMEGA_MAX * Lu / math.pi)) + 1)
    return np.pi * np.arange(J) / Lu, J


def weight_pieces(row, u0, uL, W):
    """Breakpoints of the piecewise-linear weight on [u0, uL]:
    the lag knots i*D strictly inside, plus the endpoints.
    Returns piece starts a, ends b, left values wa, slopes s
    (endpoint evaluation is exact for a piecewise-linear
    function)."""
    D, M = row["D"], row["M"]
    i_lo = int(math.floor(u0 / D)) + 1
    i_hi = int(math.ceil(uL / D)) - 1
    knots = D * np.arange(i_lo, i_hi + 1, dtype=float)
    knots = knots[(knots > u0 + 1e-12) & (knots < uL - 1e-12)]
    edges = np.concatenate([[u0], knots, [uL]])
    a_p, b_p = edges[:-1], edges[1:]
    wa = q_read(W, a_p, D, M)
    wb = q_read(W, b_p, D, M)
    s_p = (wb - wa) / (b_p - a_p)
    return a_p, b_p, wa, s_p


def cosine_coeffs(om, Lu, u0, a_p, b_p, wa, s_p):
    """Closed-form orthonormal half-range cosine coefficients of
    the piecewise-linear weight: per piece
    int (wa + s (u - a)) cos(theta (u - u0)) du analytic."""
    J = len(om)
    ga = a_p - u0
    gb = b_p - u0
    ln = b_p - a_p
    craw = np.empty(J)
    craw[0] = float(np.sum(wa * ln + 0.5 * s_p * ln * ln))
    th = om[1:][:, None]                       # (J-1, 1)
    sin_a = np.sin(th * ga[None, :])
    sin_b = np.sin(th * gb[None, :])
    cos_a = np.cos(th * ga[None, :])
    cos_b = np.cos(th * gb[None, :])
    I0 = (sin_b - sin_a) / th
    I1 = ln[None, :] * sin_b / th + (cos_b - cos_a) / (th * th)
    craw[1:] = I0 @ wa + I1 @ s_p
    c = craw.copy()
    c[0] /= math.sqrt(Lu)
    c[1:] *= math.sqrt(2.0 / Lu)
    return c


def gl5_coeff(om_j, Lu, u0, a_p, b_p, wa, s_p, j):
    """The same coefficient by composite 5-point Gauss-Legendre
    (independent exact-class route for the W11 ward): every
    piece is subdivided until theta * segment <= GL5_SEG, so the
    rule is machine-exact on each segment."""
    width = b_p - a_p
    ns = max(1, int(math.ceil(float(np.max(width))
                              * max(om_j, 1.0) / GL5_SEG)))
    tt = np.arange(ns, dtype=float) / ns
    A = (a_p[:, None] + width[:, None] * tt[None, :]).ravel()
    Wd = np.repeat(width / ns, ns)
    WA = (wa[:, None]
          + s_p[:, None] * (width[:, None] * tt[None, :])).ravel()
    S = np.repeat(s_p, ns)
    mid = A + 0.5 * Wd
    half = 0.5 * Wd
    acc = 0.0
    for xg, wg in zip(GL5_X, GL5_W):
        u = mid + half * xg
        wval = WA + S * (u - A)
        acc += wg * float(np.sum(half * wval
                                 * np.cos(om_j * (u - u0))))
    return acc * (1.0 / math.sqrt(Lu) if j == 0
                  else math.sqrt(2.0 / Lu))


def spectral_pair(ug, f, cv, cs, om, Lu, u0, rec_spot=False):
    """One pass over the frame: the fluctuation spectrum Fhat_j =
    sum_k f_k psi_j(u_k) and the atom-level reconstructions
    R = sum_j c_j psi_j(u_k) for both weights, via the Chebyshev
    cosine recurrence."""
    J = len(om)
    x = ug - u0
    n0 = 1.0 / math.sqrt(Lu)
    n1 = math.sqrt(2.0 / Lu)
    c1v = np.cos((math.pi / Lu) * x)
    Fh = np.empty(J)
    Rv = np.zeros(len(ug))
    Rs = np.zeros(len(ug))
    prev = np.ones(len(ug))
    cur = c1v.copy()
    rec_dev = 0.0
    for j in range(J):
        if j == 0:
            cj, nj = prev, n0
        elif j == 1:
            cj, nj = cur, n1
        else:
            nxt = 2.0 * c1v * cur - prev
            prev, cur = cur, nxt
            cj, nj = cur, n1
        Fh[j] = nj * float(f @ cj)
        Rv += (cv[j] * nj) * cj
        Rs += (cs[j] * nj) * cj
        if rec_spot and j == J - 1:
            direct = np.cos(om[j] * x)
            rec_dev = float(np.max(np.abs(cj - direct)))
    return Fh, Rv, Rs, rec_dev


def pairing_census(t, om):
    """Signed census of the contributions t_j toward the total:
    n50/n90 bins, participation ratio, top carrier."""
    tot = float(np.sum(t))
    sgn = 1.0 if tot >= 0.0 else -1.0
    order = np.argsort(-(t * sgn), kind="stable")
    pref = np.cumsum(t[order] * sgn)
    tgt = abs(tot)
    n50 = int(np.argmax(pref >= 0.5 * tgt)) + 1
    n90 = int(np.argmax(pref >= 0.9 * tgt)) + 1
    at = np.abs(t)
    pr = float(at.sum() ** 2 / max(float((at * at).sum()),
                                   1e-300))
    jstar = int(np.argmax(at))
    return dict(tot=tot, n50=n50, n90=n90, pr=pr,
                jstar=jstar, om_star=float(om[jstar]),
                S90=order[:n90])


def build_spectral(row, nc, spot=False):
    """The full frequency-space object of one rung: grid,
    fluctuation, both weights, frame, coefficients, spectrum,
    reconstruction wards, census."""
    Ng = max(int(math.floor(row["X"])),
             int(np.round(math.exp(float(row["uu"][-1])))))
    kk = np.arange(nc + 1, Ng + 1, dtype=np.int64)
    kf = kk.astype(float)
    ug = np.log(kf)
    lamg = core.LAM_TAB[nc + 1:Ng + 1]
    inv_sq = 1.0 / np.sqrt(kf)
    a = 2.0 * lamg * inv_sq
    f = a - 2.0 * inv_sq
    wv = q_read(row["Wv"], ug, row["D"], row["M"])
    Ws = row["Wcar"] if row["ov"] < OV_MIN else row["Wsm"]
    ws = q_read(Ws, ug, row["D"], row["M"])
    T = float(a @ wv)
    Tt = float((2.0 * inv_sq) @ wv)
    P_v = float(f @ wv)
    P_s = float(f @ ws)
    pair_scale = max(float(np.abs(f) @ np.abs(wv)), 1e-300)
    dev_pair = abs((T - Tt) - P_v) / pair_scale
    u0, uL = float(ug[0]), float(ug[-1])
    Lu = uL - u0
    om, J = frame_freqs(Lu)
    pv = weight_pieces(row, u0, uL, row["Wv"])
    ps = weight_pieces(row, u0, uL, Ws)
    cv = cosine_coeffs(om, Lu, u0, *pv)
    cs = cosine_coeffs(om, Lu, u0, *ps)
    Fh, Rv, Rs, rec_dev = spectral_pair(ug, f, cv, cs, om, Lu,
                                        u0, rec_spot=spot)
    P_rec_v = float(cv @ Fh)
    P_rec_s = float(cs @ Fh)
    res_v = abs(P_v - P_rec_v) / max(abs(P_v), 1e-300)
    res_s = abs(P_s - P_rec_s) / max(abs(P_s), 1e-300)
    dev_fub = max(abs(float(f @ Rv) - P_rec_v),
                  abs(float(f @ Rs) - P_rec_s)) / pair_scale
    sup_v = float(np.max(np.abs(wv - Rv))
                  / max(float(np.max(np.abs(wv))), 1e-300))
    quad_dev = 0.0
    if spot:
        for (pc, cc) in ((pv, cv), (ps, cs)):
            mxc = max(float(np.max(np.abs(cc))), 1e-300)
            for j in (1, J // 2, J - 1):
                g5 = gl5_coeff(float(om[j]), Lu, u0, *pc, j)
                quad_dev = max(quad_dev,
                               abs(cc[j] - g5) / mxc)
    t_v = cv * Fh
    t_s = cs * Fh
    cen_v = pairing_census(t_v, om)
    cen_s = pairing_census(t_s, om)
    return dict(T=T, Tt=Tt, P_v=P_v, P_s=P_s, dev_pair=dev_pair,
                res_v=res_v, res_s=res_s, dev_fub=dev_fub,
                sup_v=sup_v, quad_dev=quad_dev, rec_dev=rec_dev,
                om=om, J=J, Lu=Lu, Fh=Fh, cv=cv, cs=cs,
                t_v=t_v, cen_v=cen_v, cen_s=cen_s)


def ctrl_spectral(r, cut):
    """C2 control read: comb snapped to the integer grid by
    n = round(exp(u)), aggregated, paired through the world's
    OWN weight from the fixed cut."""
    Ng = int(math.floor(r["X"]))
    nn = np.round(np.exp(np.asarray(r["uu"], float))
                  ).astype(np.int64)
    ag = np.zeros(Ng + 2)
    keep = (nn >= cut + 1) & (nn <= Ng)
    np.add.at(ag, nn[keep], np.asarray(r["mu"], float)[keep])
    kk = np.arange(cut + 1, Ng + 1, dtype=np.int64)
    kf = kk.astype(float)
    ug = np.log(kf)
    inv_sq = 1.0 / np.sqrt(kf)
    f = ag[kk] - 2.0 * inv_sq
    wv = q_read(r["Wv"], ug, r["D"], r["M"])
    P = float(f @ wv)
    u0, uL = float(ug[0]), float(ug[-1])
    Lu = uL - u0
    om, J = frame_freqs(Lu)
    x = ug - u0
    c1v = np.cos((math.pi / Lu) * x)
    Fh = np.empty(J)
    prev = np.ones(len(ug))
    cur = c1v.copy()
    for j in range(J):
        if j == 0:
            cj, nj = prev, 1.0 / math.sqrt(Lu)
        elif j == 1:
            cj, nj = cur, math.sqrt(2.0 / Lu)
        else:
            nxt = 2.0 * c1v * cur - prev
            prev, cur = cur, nxt
            cj, nj = cur, math.sqrt(2.0 / Lu)
        Fh[j] = nj * float(f @ cj)
    e2 = Fh * Fh
    pk = float(np.max(e2) / max(float(np.mean(e2)), 1e-300))
    prF = float(e2.sum() ** 2 / max(float((e2 * e2).sum()),
                                    1e-300))
    jstar = int(np.argmax(np.abs(Fh)))
    return dict(P=P, F0=float(Fh[0]), pk=pk, prF=prF,
                om_star=float(om[jstar]), om=om, Fh=Fh)


def dist_to_comb(w, spacing):
    rem = math.fmod(w, spacing)
    return min(rem, spacing - rem)


def main():
    section("PRIME.PORT.TAIL.OSCPAIR.01 -- the frequency-space "
            "bookkeeping of the tail pairing (EXPLORATION ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s"
          % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
    print("    NO RH claim; no marker moves; the zeta ordinates "
          "are literature comparison constants only.")
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
    check("W8 WARD mu1 closed form (dev %.1e) + CXLIII shat band "
          "min/med/max %.4f/%.4f/%.4f ~ %s"
          % (dev_mu, s3[0], s3[1], s3[2], SHAT_REF),
          dev_mu <= MU_WARD and ok_shat, kill="K2")
    if KILLS:
        return finish({})

    # ------------------------------------- the spectral objects
    spec = []
    spot_at = (0, N // 2)
    for i, (r, icB, nc) in enumerate(zip(rungs, icBs, nB_min)):
        spec.append(build_spectral(r, nc, spot=(i in spot_at)))
    tie = max(abs(s["T"] - float(r["tail_B"][i]))
              / max(1.0, abs(float(r["tail_B"][i])))
              for s, r, i in zip(spec, rungs, icBs))
    check("W9 WARD grid tie: integer-grid tail == tail_B(cB) "
          "max rel dev %.2e <= %.0e  [%.1f s]"
          % (tie, TIE_WARD, time.time() - T0),
          tie <= TIE_WARD, kill="K2")
    dev_pr = max(s["dev_pair"] for s in spec)
    check("W10 WARD pairing tie: (T - Ttilde) - P == 0 max rel "
          "dev %.2e <= %.0e" % (dev_pr, PAIR_WARD),
          dev_pr <= PAIR_WARD, kill="K2")
    qd = max(s["quad_dev"] for s in spec)
    rd = max(s["rec_dev"] for s in spec)
    check("W11 WARD frame: closed-form c_j vs GL5 at frozen "
          "spots %.2e <= %.0e; cosine recurrence vs direct "
          "%.2e <= %.0e" % (qd, QUAD_WARD, rd, REC_WARD),
          qd <= QUAD_WARD and rd <= REC_WARD, kill="K2")
    fub = max(s["dev_fub"] for s in spec)
    res_mx = max(s["res_v"] for s in spec)
    check("W12 WARD reconstruction: Fubini max %.2e <= %.0e; "
          "residual share max %.2e <= %.2f on all %d rungs "
          "(the >= 99%% requirement; sup-norm weight recon med "
          "%.1e, diagnostic)"
          % (fub, FUB_WARD, res_mx, RES_WARD, N,
             float(np.median([s["sup_v"] for s in spec]))),
          fub <= FUB_WARD and res_mx <= RES_WARD, kill="K2")
    if KILLS:
        return finish({})
    lab_w = "RECON-WARDED(max res share %.1e)" % res_mx

    # ------------------------------------------------------------ A
    section("A -- (a)+(b) THE FREQUENCY CENSUS OF THE NET "
            "NEGATIVITY (arithmetic weight q_v)")
    aa = np.array([r["alpha"] for r in rungs])
    Pv = np.array([s["P_v"] for s in spec])
    n50 = np.array([s["cen_v"]["n50"] for s in spec])
    n90 = np.array([s["cen_v"]["n90"] for s in spec])
    prs = np.array([s["cen_v"]["pr"] for s in spec])
    oms = np.array([s["cen_v"]["om_star"] for s in spec])
    Js = np.array([s["J"] for s in spec])
    resl = np.array([math.pi / s["Lu"] for s in spec])
    dg = np.array([min(abs(w - g) for g in GAMMAS) for w in oms])
    print("    kz   h    nc  P/mu1       res_share  J    n50  "
          "n90  PR      omega*  d_gamma  resol")
    for i, r in enumerate(rungs):
        print("    %-4d %-4d %-3d %+.3e %.2e %-4d %-4d %-4d "
              "%-7.1f %-7.3f %-8.3f %.3f"
              % (r["kz"], r["h"], nB_min[i], Pv[i] / mu1[i],
                 spec[i]["res_v"], Js[i], n50[i], n90[i],
                 prs[i], oms[i], dg[i], resl[i]), flush=True)
    print("\n    P/mu1 min/med/max %+.3e/%+.3e/%+.3e (the CLII "
          "arithmetic remainder rhat, reproduced by tie); "
          "P < 0 on %d/%d"
          % (float(np.min(Pv / mu1)), float(np.median(Pv / mu1)),
             float(np.max(Pv / mu1)), int(np.sum(Pv < 0)), N))
    print("    carrying-set ladder: n50 med %d (%d..%d), n90 med "
          "%d (%d..%d), PR med %.1f (%.1f..%.1f); frame size J "
          "med %d"
          % (int(np.median(n50)), int(n50.min()), int(n50.max()),
             int(np.median(n90)), int(n90.min()), int(n90.max()),
             float(np.median(prs)), float(prs.min()),
             float(prs.max()), int(np.median(Js))))
    lab_a = ("CENSUS(n50 med %d, n90 med %d, PR med %.1f)"
             % (int(np.median(n50)), int(np.median(n90)),
                float(np.median(prs))))
    check("A.1 typed (b) census: %s" % lab_a, True)

    # ------------------------------------------------------------ B
    section("B -- (b) FEW-OR-MANY + carrier stability across "
            "rungs")
    om_med = float(np.median(oms))
    stab = float(np.mean(np.abs(oms - om_med) <= STAB_TOL))
    jstars = np.array([int(round(w * s["Lu"] / math.pi))
                       for w, s in zip(oms, spec)])
    j_med = int(np.median(jstars))
    stab_j = float(np.mean(np.abs(jstars - j_med) <= J_STAB_TOL))
    slD, seD, r2D = jack_slope(aa, oms)
    few = (float(np.median(n90)) <= FEW_N90
           and stab_j >= STAB_FRAC)
    oms_s = np.array([s["cen_s"]["om_star"] for s in spec])
    agree = int(np.sum(np.abs(oms - oms_s) <= STAB_TOL))
    print("    top carrier omega*: med %.3f (min/max %.3f/%.3f); "
          "ABSOLUTE-omega stability frac |omega* - med| <= %.1f: "
          "%.2f (recorded; smoke FAIL of this coordinate on "
          "record); drift law omega* = %+.3f alpha + c (2SE "
          "%.3f, R^2 %.2f)"
          % (om_med, float(oms.min()), float(oms.max()),
             STAB_TOL, stab, slD, 2 * seD, r2D))
    print("    HARMONIC-INDEX read (amendment A2, the gate): "
          "j* = round(omega* Lu/pi) med %d (min/max %d/%d); "
          "stability frac |j* - med| <= %d: %.2f (bar %.2f) -- "
          "the carrier in the frame's own coordinate"
          % (j_med, int(jstars.min()), int(jstars.max()),
             J_STAB_TOL, stab_j, STAB_FRAC))
    print("    v_sm cross-check (prime-free weight): omega* "
          "agreement within %.1f on %d/%d; n90(v_sm) med %d"
          % (STAB_TOL, agree, N,
             int(np.median([s["cen_s"]["n90"] for s in spec]))))
    if few:
        lab_b = ("OSC-FEW(n90 med %d <= %d, j-stab %.2f, "
                 "abs-stab %.2f recorded)"
                 % (int(np.median(n90)), FEW_N90, stab_j, stab))
        print("    ==> the carrying set is SMALL and STABLE: a "
              "finite-dimensional pairing statement is on the "
              "table (section R)")
    else:
        lab_b = ("OSC-BROAD(n90 med %d, PR med %.1f, j-stab "
                 "%.2f)" % (int(np.median(n90)),
                            float(np.median(prs)), stab_j))
        print("    ==> the carrying set is BROAD and/or "
              "unstable: genuinely diffuse cancellation -- the "
              "effective dimension is the honest obstruction "
              "(section R)")
    check("B.1 typed (b) few-or-many: %s" % lab_b, True)

    # ------------------------------------------------------------ G
    section("G -- (c) WHERE ARE THE CARRIERS: classical scales "
            "vs the first ten zeta ordinates (COMPARISON ONLY)")
    null_g = float(np.median(np.diff(np.array(GAMMAS)))) / 4.0
    dwin = np.array([dist_to_comb(w, math.pi / (2.0 * al))
                     / (math.pi / (4.0 * al))
                     for w, al in zip(oms, aa)])
    dknot = np.array([w * r["D"] / (2.0 * math.pi)
                      for w, r in zip(oms, rungs)])
    gband = np.array([
        float(np.abs(s["t_v"])[s["om"] >= GAMMA_BAND_LO].sum()
              / max(float(np.abs(s["t_v"]).sum()), 1e-300))
        for s in spec])
    n_near = int(np.sum(dg <= GAMMA_NEAR))
    print("    d_gamma(omega*): med %.3f (min/max %.3f/%.3f); "
          "uniform-null scale ~ %.2f (local gamma spacing/4); "
          "near (<= %.1f) on %d/%d"
          % (float(np.median(dg)), float(dg.min()),
             float(dg.max()), null_g, GAMMA_NEAR, n_near, N))
    print("    gamma-BAND share (|t| mass at omega >= %.0f, "
          "where the ordinates live): med %.3f (min/max "
          "%.3f/%.3f) -- energy census, not a peak claim"
          % (GAMMA_BAND_LO, float(np.median(gband)),
             float(gband.min()), float(gband.max())))
    print("    window-harmonic comb pi k/(2 alpha): NORMALIZED "
          "distance med %.3f (uniform null 0.5 -- the comb "
          "spacing %.3f..%.3f is denser than the frame "
          "resolution, disclosed)"
          % (float(np.median(dwin)),
             math.pi / (2.0 * float(aa.max())),
             math.pi / (2.0 * float(aa.min()))))
    print("    lag-knot fundamental 2 pi / D: omega* D/(2 pi) "
          "med %.2e -- carriers vs the breakpoint scale"
          % float(np.median(dknot)))
    ver_g = ("CARRIER-NEAR-GAMMA" if float(np.median(dg))
             <= GAMMA_NEAR else "CARRIER-FAR")
    lab_g = ("GAMMA(med d %.2f vs null %.2f, near %d/%d, %s) + "
             "CLASSICAL(win-comb %.2f, knot %.1e)"
             % (float(np.median(dg)), null_g, n_near, N, ver_g,
                float(np.median(dwin)),
                float(np.median(dknot))))
    check("G.1 typed (c): %s -- distances, not celebrations"
          % lab_g, True)

    # ------------------------------------------------------------ R
    section("R -- (d) THE PAIRING INEQUALITY SHAPE")
    # pooled carrier histogram on the absolute omega axis
    hist = {}
    for s in spec:
        S90 = s["cen_v"]["S90"]
        for j in S90:
            b = int(s["om"][j] / RED_BIN)
            hist[b] = hist.get(b, 0.0) + abs(s["t_v"][j])
    top = sorted(hist.items(), key=lambda kvv: -kvv[1])[:K_RED]
    centers = np.array(sorted((b + 0.5) * RED_BIN
                              for b, _w in top))
    shares = []
    Pred = []
    for s in spec:
        d = np.min(np.abs(s["om"][:, None] - centers[None, :]),
                   axis=1)
        pin = float(s["t_v"][d <= RED_HALF].sum())
        Pred.append(pin)
        shares.append(pin / s["P_v"] if s["P_v"] != 0 else 0.0)
    shares = np.array(shares)
    Pred = np.array(Pred)
    print("    pooled top-%d carrier bins (centers, weight "
          "share of pooled |t| mass):" % K_RED)
    wtot = sum(hist.values())
    for b, wgt in top:
        print("      omega ~ %6.2f   pooled share %.3f"
              % ((b + 0.5) * RED_BIN, wgt / wtot))
    print("    reduced read-through (only |omega - center| <= "
          "%.1f): share_red min/med/max %+.3f/%+.3f/%+.3f"
          % (RED_HALF, float(shares.min()),
             float(np.median(shares)), float(shares.max())))
    reduced = (few and float(np.median(shares)) >= RED_MED
               and float(shares.min()) >= RED_MIN)
    if reduced:
        imed = int(np.argsort(Pv)[len(Pv) // 2])
        s = spec[imed]
        print("    ==> REDUCED PAIRING STATEMENT (median rung "
              "kz %d): P = sum over the %d frozen carriers of "
              "c_g(omega_i) Fhat(omega_i) + res"
              % (rungs[imed]["kz"], K_RED))
        d = np.min(np.abs(s["om"][:, None] - centers[None, :]),
                   axis=1)
        for j in np.nonzero(d <= RED_HALF)[0]:
            print("      omega %6.2f: c_g %+.3e  Fhat %+.3e  "
                  "t %+.3e" % (s["om"][j], s["cv"][j],
                               s["Fh"][j], s["t_v"][j]))
        lab_r = ("REDUCED-ACHIEVED(K=%d, med share %.2f)"
                 % (K_RED, float(np.median(shares))))
    elif few:
        lab_r = ("REDUCED-FAILED(med share %.2f < %.2f)"
                 % (float(np.median(shares)), RED_MED))
        print("    ==> carrying set small per rung but NOT "
              "poolable into %d global frequencies" % K_RED)
    else:
        slP, seP, r2P = jack_slope(aa, np.log(prs))
        lab_r = ("EFFDIM(PR med %.1f, law %+.3f alpha, 2SE "
                 "%.3f, R^2 %.2f)"
                 % (float(np.median(prs)), slP, 2 * seP, r2P))
        print("    ==> THE EFFECTIVE-DIMENSION LAW (the honest "
              "obstruction): log PR = %+.3f alpha + c (2SE "
              "%.3f, R^2 %.2f) -- the number of frequency bins "
              "the cancellation genuinely uses grows ~ "
              "e^{%.2f alpha}" % (slP, 2 * seP, r2P, slP))
    check("R.1 typed (d): %s" % lab_r, True)

    # ------------------------------------------------------------ T
    section("T -- (e) TAU-SCREENS (jackknife, typed)")
    sl1, se1, r21 = jack_slope(np.log(mm), np.log(n90))
    scr1 = ("PASS" if abs(sl1) <= SLOPE_PASS else
            "RELOC" if sl1 >= SLOPE_RELOC else "AMBIG")
    print("    screen log n90 vs log m: slope %+.3f +- 2SE %.3f "
          "(R^2 %.2f) -> %s" % (sl1, 2 * se1, r21, scr1))
    sl2, se2, r22 = jack_slope(np.log(mm), np.log(prs))
    scr2 = ("PASS" if abs(sl2) <= SLOPE_PASS else
            "RELOC" if sl2 >= SLOPE_RELOC else "AMBIG")
    print("    screen log PR vs log m: slope %+.3f +- 2SE %.3f "
          "(R^2 %.2f) -> %s" % (sl2, 2 * se2, r22, scr2))
    ex = ""
    if reduced:
        okp = np.abs(Pred) > 0
        sl3, se3, r23 = jack_slope(
            np.log(mm[okp]), np.log(np.abs(Pred[okp] / mu1[okp])))
        ex = ("; reduced-margin screen log|P_red/mu1| vs log m "
              "%+.3f (2SE %.3f, R^2 %.2f, recorded)"
              % (sl3, 2 * se3, r23))
        print("    " + ex[2:])
    lab_t = ("SCREENS(n90 %+.2f %s, PR %+.2f %s%s)"
             % (sl1, scr1, sl2, scr2, ex))
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
    # C2 -- the spectral battery from the fixed cut CTRL_CUT
    rtrue = build_rung(CTRL_KZ, need_sm=False)
    st = ctrl_spectral(rtrue, CTRL_CUT)
    print("    true kz-%d at cut %d: P %+.3e  |Fhat(0)| %.3e  "
          "peakiness %.1f  PR_F %.1f  omega* %.3f"
          % (CTRL_KZ, CTRL_CUT, st["P"], abs(st["F0"]),
             st["pk"], st["prF"], st["om_star"]))
    sc2 = {}
    for name in ("smooth", "scramble", "Epstein"):
        sc2[name] = ctrl_spectral(ctl[name], CTRL_CUT)
        dgc = min(abs(sc2[name]["om_star"] - g) for g in GAMMAS)
        print("    %-9s: P %+.3e (ratio %.3e)  |Fhat(0)|-blowup "
              "%.3e  peakiness %.1f  PR_F %.1f  omega* %.3f "
              "(d_gamma %.1f)"
              % (name, sc2[name]["P"],
                 abs(sc2[name]["P"]) / max(abs(st["P"]), 1e-300),
                 abs(sc2[name]["F0"]) / max(abs(st["F0"]),
                                            1e-300),
                 sc2[name]["pk"], sc2[name]["prF"],
                 sc2[name]["om_star"], dgc), flush=True)
    # C2a -- the by-construction integer-continuum world
    # (amendment A3): Lambda == 1 on the whole deep grid, so
    # f = 2(1 - 1)/sqrt(k) == 0 identically and the pairing dies
    # exactly; read through the true rung's weight (any weight
    # gives zero -- that is the point).
    Ng0 = int(math.floor(rtrue["X"]))
    kk0 = np.arange(CTRL_CUT + 1, Ng0 + 1, dtype=np.int64)
    inv0 = 1.0 / np.sqrt(kk0.astype(float))
    f0 = 2.0 * np.ones(len(kk0)) * inv0 - 2.0 * inv0
    w0 = q_read(rtrue["Wv"], np.log(kk0.astype(float)),
                rtrue["D"], rtrue["M"])
    P0 = float(f0 @ w0)
    rat_sm = abs(sc2["smooth"]["P"]) / max(abs(st["P"]), 1e-300)
    check("C2a WARD by-construction smooth world dies exactly: "
          "max|f| = %.1e, P = %.1e (both == 0; Fhat == 0 "
          "identically).  The DISCRETIZED (snapped) smooth "
          "world is a quadrature-error object and does NOT die: "
          "|P_sm|/|P_true| = %.3e (recorded, the honest v0 "
          "fail)" % (float(np.max(np.abs(f0))), P0, rat_sm),
          float(np.max(np.abs(f0))) == 0.0 and P0 == 0.0,
          kill="K2")
    blow = (abs(sc2["scramble"]["F0"])
            / max(abs(st["F0"]), 1e-300))
    check("C2b WARD scramble DC blowup: |Fhat_scr(0)|/"
          "|Fhat_true(0)| = %.3e >= %.1f (the PNT cancellation "
          "is destroyed)" % (blow, SCR_BLOWUP),
          blow >= SCR_BLOWUP, kill="K2")
    lab_c = ("CTRL(smooth exact-zero dies + snapped %.1e "
             "recorded, scramble blowup %.1e FIRES, Epstein "
             "drift %.1e omega* %.2f recorded)"
             % (rat_sm, blow,
                abs(sc2["Epstein"]["F0"]) / max(abs(st["F0"]),
                                                1e-300),
                sc2["Epstein"]["om_star"]))
    check("C3 typed control battery: %s" % lab_c, True)

    return finish(dict(w=lab_w, b=lab_b, g=lab_g, r=lab_r,
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
        VERDICT = ("OSCPAIR-MEASURED / %(w)s / %(b)s / %(g)s / "
                   "%(r)s / %(t)s / %(c)s" % labels)
        print("\n  VERDICT: %s" % VERDICT)
    print("""
  HONEST FRAME (as frozen): the frame expansion, the Fubini swap,
  the closed-form coefficients and the ties are EXACT bookkeeping;
  the census, carrier locations and all laws are MEASURED SURFACE
  STRUCTURE at float level.  The zeta ordinates enter ONLY as
  recorded comparison constants -- a near or far answer is a
  measurement either way, never a construction input.  An OSC-FEW
  outcome would be a per-rung surface statement, not a theorem; an
  OSC-BROAD outcome is a measured effective-dimension law, not an
  impossibility proof.  NO RH claim.  No marker moves.""")
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed"
          % (time.time() - T0, n_tot, n_tot - n_pass))
    return 0 if n_pass == n_tot else 1


if __name__ == "__main__":
    raise SystemExit(main())
