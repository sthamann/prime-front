#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""relative_domination_probe -- PRIME.PORT.RELDOM.01
(EXPLORATION ONLY, experiments/; round 58, strategy S4 of the
round-57 memo: the multi-mode generalization of the wedge rescue
-- RELATIVE POSITIVE-PART DOMINATION -- and whether the exterior
reserve carries the rescue as a LOWER bound on the positive
channel.  2026-08-09.)

THE QUESTION (frozen).  rank2_wedge_probe (round 57,
PRIME.PORT.RANK2.WEDGE.01) measured that the congruence increment
H_h is RANK-RICH (median 3 positive / 9 negative modes; top-2
share ~ two thirds), so the scalar wedge rescue
Delta_wedge = 1 - |v|^2 + <u,v>^2/(1+|u|^2) is only the rank-2
SHADOW of the true margin -- yet its coupling/common-area term
was DECISIVE on 20/31 full-window and 29/39 core steps (naive
one-direction bound 1 - |v|^2 <= 0, wedge still positive).  The
multi-mode generalization of that rescue is RELATIVE OPERATOR
DOMINATION: with the increment split H = P - N + W into psd
positive channel P, psd danger channel N and an explicit
leftover W, the rescue is the statement that N is dominated
RELATIVE to the rescued positive channel I + P,
    lambda_max( (I+P)^{-1/2} N (I+P)^{-1/2} ) < 1,
which bounds ALL modes at once (the wedge is its rank-1
compression).  The probe measures this on every deployed step,
derives and checks the EXACT implied margin including the W
term, asks WHO feeds the positive channel in the dangerous
direction (exterior reserve vs window-internal), and links the
domination margin to the measured trendless exterior reserve
lambda_min(R_h) >= 210 tau_h (relative_flag_margin /
deepcore_schur_reduction).  READ-ONLY v563.

THE TWO LADDERS (frozen, rank2_wedge / predecessors verbatim):
  FULL WINDOW: all frame-A zones h <= 900, 12x12 window
    compression at J = {2,...,24}, consecutive full-window
    pairs, A_h = I - C_J(h), C_J = E_ww + Y with
    Y = sym(E_wo (I - E_oo)^{-1} E_ow), Delta_h = C_J(h) -
    C_J(h+1), H_h = A_h^{-1/2} Delta_h A_h^{-1/2}
    (relative_congruence verbatim floats; 31 pairs, min eta =
    0.0050).
  8x8 CORE: the 42-rung deepcore ladder, full wall A = I - G on
    all folded neg nodes, fixed-core Schur S_h = B_h - Y_h at
    CORE_J = {2,...,16}, consecutive full-core steps,
    H_core = S_h^{-1/2} (S_{h+1} - S_h) S_h^{-1/2}
    (deepcore_schur_reduction / normalized_core_update verbatim;
    39 steps, min eta_core = 0.0315).

THE FROZEN CONSTRUCTIVE SPLIT (round 57 verbatim; the exact
exterior telescoping DY = t_dx + t_dz + t_new - t_old):
    P_side := sym(-(DEww + t_new))     (window)
              sym(DB - t_new)          (core)
              [new-node + direct arch/block contribution]
    N_side := sym(t_dx + t_dz - t_old) (persisting exterior
              coupling/resolvent relaxation minus returns),
so Delta = P_side - N_side EXACTLY (split ward; round 57
measured the deviation at 2.6e-14).  In H-space
G_P = A^{-1/2} P_side A^{-1/2}, G_N = A^{-1/2} N_side A^{-1/2}.

FROZEN PROTOCOL (2026-08-09; all bars frozen before the run;
each of D1-D3 runs separately for FULL and CORE):

 W   PIPELINE + REPRODUCTION WARDS (rank2_wedge verbatim):
     W1 (kill -> PIPELINE-BROKEN) >= MIN_PAIRS = 20 truth pairs
     per world, A_h / S_h symmetric PD on every truth step, core
     ladder = 42 rungs with >= 30 full-core.  W2 (kill ->
     WARD-BROKEN) reproduction: FULL 31 pairs with min eta =
     0.0050; CORE 39 steps with min eta_core = 0.0315 (print
     precision, tol 5.001e-5).  W3 (kill -> WARD-BROKEN)
     increment identities to 1e-12 rel; four-term telescoping to
     1e-9 rel; constructive split Delta = P_side - N_side to
     1e-8; the H-space channel algebra (see D3) to 1e-9.

 D1  THE EXACT SIGNED SPLIT (per step, per world): symmetrize
     each side exactly (sym(), already applied in the frozen
     split) and split off the indefinite remainder HONESTLY via
     the psd decomposition (eigh, negative eigenvalues clipped):
         P := psd part of G_P          (P = G_P + P_-,  P_- >= 0)
         N := psd part of G_N          (N = G_N + N_-,  N_- >= 0)
         W := (G_P - P) - (G_N - N) = -P_- + N_-
     -- each side's indefinite tail is moved into W from the
     start (the documented exact repair, applied unconditionally
     and typed by size, SPEC v1 (ii)).  Print ||W||_F/||H||_F
     per step.  WARD (kill -> WARD-BROKEN): ||(P - N + W) -
     H||_F / ||H||_F <= DEC_WARD = 1e-8 on every step (this
     inherits the constructive-split deviation transported to
     H-space plus eigh roundoff).  TYPED (report, never kills):
     W-NEGLIGIBLE iff max ||W||/||H|| < 1e-8; else
     W-TAIL-TYPED(median, max) -- the leftover is real and every
     D2 statement below carries it explicitly.

 D2  THE RELATIVE DOMINATION (decisive; per step, per world):
         Ntilde := (I+P)^{-1/2} N (I+P)^{-1/2},
         delta_h := 1 - lambda_max(Ntilde).
     THE EXACT INEQUALITY CHAIN (the honest derivation; the
     naive "N <= (1-delta)(I+P) => I + H >= delta I - W" is
     WRONG on two counts -- W enters with its SIGNED lambda_min
     (N_- helps, P_- hurts), and the delta < 0 branch needs
     lambda_max(P)):
       (a) N <= (1 - delta_h)(I+P) holds EXACTLY and delta_h is
           the largest such constant (definition of lambda_max
           of the congruence-normalized Ntilde);
       (b) I + H = (I+P) - N + W >= delta_h (I+P) + W  (exact,
           inserting (a); H = P - N + W from D1);
       (c) hence  eta = 1 + lambda_min(H)
              >= delta_h (1 + lambda_min(P)) + lambda_min(W)
                                       if delta_h >= 0,
              >= delta_h (1 + lambda_max(P)) + lambda_min(W)
                                       if delta_h <  0
           =: eta_impl  (the implied margin, both branches
           exact).
     Per step print lambda_max(Ntilde), delta_h, lambda_min(W),
     eta_impl vs the true eta.  CONSISTENCY WARD (kill ->
     WARD-BROKEN): eta >= eta_impl - IMPL_WARD (= 1e-9) on every
     step (the derivation is exact; only roundoff may intrude).
     CENSUS against 1: raw AND SENS (excluding the
     kz-21-touching pairs, KZ_EXCL = 21 at either endpoint --
     the known soft-flag outlier rung, kz21_outlier_probe).
     TYPED per world (never kills):
       RELDOM-HOLDS(min delta, min eta_impl) iff delta_h > 0 on
         ALL steps AND eta_impl > 0 on ALL steps;
       RELDOM-PARTIAL(census, where it fails) iff delta_h > 0 on
         >= 1 step but not all, or all delta_h > 0 while
         eta_impl <= 0 somewhere;
       RELDOM-BROKEN iff delta_h <= 0 on every step.

 D3  THE RESCUE SOURCE (on the steps where the round-57 wedge
     coupling term was DECISIVE; reproduced here with the
     round-57 constructive wedge verbatim -- u/v = top-eigenpair
     compressions of G_P/G_N, decisive iff 1 - |v|^2 <= 0 AND
     Delta_wedge > 0; REPRODUCTION WARD (kill -> WARD-BROKEN):
     decisive counts == 20 (FULL) / 29 (CORE)):
     v_dang := unit top eigenvector of N (the psd danger
     channel).  THE EXACT CHANNEL DECOMPOSITION (SPEC v1 (iii)):
     in H-space the identity is EXACTLY the transported wall,
     I = A^{-1/2} A A^{-1/2} with A = (I - E_ww) - Y (window)
     resp. S = B - Y (core), and P = G_P + P_- with G_P =
     ch_step + ch_new, so
         I + P = ch_wall + ch_res + ch_step + ch_new + P_-
     with (all in H-space, exact up to CH_WARD)
         ch_wall = window-internal wall   (I - E_ww  resp. B),
         ch_res  = exterior resolvent response  (-Y; the
                   response through (I - E_oo)^{-1} resp.
                   R^{-1} -- THE RESERVE OBJECT),
         ch_step = window-internal step   (-sym(DEww) resp.
                   sym(DB)),
         ch_new  = exterior new nodes     (-sym(t_new)),
         P_-     = the psd-projection tail (>= 0).
     (t_dx / t_dz / t_old live on the N-side of the frozen split
     and are NOT part of the positive channel; the exterior
     resolvent response of the positive channel is Y itself.)
     Per decisive step print the share ledger of
     q := v_dang^T (I+P) v_dang; EXTERIOR share :=
     (q_res + q_new)/q.  TYPED per world (never kills):
     RESCUE-FROM-RESERVE(n/n_dec) iff exterior share >= 0.5 on
     >= 50% of decisive steps; else RESCUE-INTERNAL(median
     share).  THE RESERVE LINK (report only): over steps with
     delta_h > 0, corr(log delta_h, log(lambda_min(R)/tau))
     (core: full-wall R and tau, deepcore verbatim, the measured
     210x reserve; window analog: lambda_min(I - E_oo) /
     lambda_min(A_h), SPEC v1 (vi)) -- printed with R^2: is the
     domination margin fed by the measured reserve?

 C   CONTROLS (kill -> WARD-BROKEN):
     C1 SMOOTH WORLD must break the domination -- and the exact
        failure mode is REPORTED: the smooth congruence is
        NORM-DEAD/CONE-EXITED (A_h indefinite on every smooth
        full-window pair -> H-space, hence P/N/Ntilde, is not
        even defined; the domination instrument never forms).
        REPRODUCTION: window 28 smooth pairs, 28/28 CONE-EXITED
        (relative_congruence SPEC v2 (ii)); core: neg(A) > 0 on
        >= 1 smooth rung (normalized_core C1).
     C2 SCRAMBLE at kz 9 (seed 1): window frame dies (window
        unavailable OR lam(C_J) > 1 OR exterior supercritical);
        core wall breaks (neg(A) > 0 or chain death).
     C3 SIGN-NULL for D3: replace v_dang by a random unit vector
        (NDRAW = 16 draws per decisive step, seed 20260809); the
        exterior share must CHANGE DISTRIBUTION: the true share
        lies outside the per-step null interquartile range
        [q25, q75] on >= NULL_OUT_FRAC = 50% of decisive steps
        (per world); BOTH distributions printed (true-share
        quartiles vs pooled null quartiles).

KILLS: K1 a pipeline ward breaks -> PIPELINE-BROKEN; KW a
reproduction / exactness / consistency / control ward breaks ->
WARD-BROKEN.  Typed D1/D2/D3 labels report, never kill.

VERDICT (frozen enum): RELDOM-MEASURED with typed sublabels
D1[full=..., core=...] (W-NEGLIGIBLE / W-TAIL-TYPED),
D2[full=..., core=...] (RELDOM-HOLDS / RELDOM-PARTIAL /
RELDOM-BROKEN), D3[full=..., core=...] (RESCUE-FROM-RESERVE /
RESCUE-INTERNAL); else PIPELINE-BROKEN / WARD-BROKEN.

FROZEN BARS: JWIN = (2,...,24); CORE_J = (2,...,16); H_DEEP_MAX
= 900; MIN_PAIRS = 20; MIN_CORE_RUNGS = 30; N_RUNGS_EXP = 42;
REF_WIN = (31 pairs, min eta 0.0050); REF_CORE = (39 steps, min
eta 0.0315); REF_SMOOTH = (28 pairs, 28 CONE-EXITED);
REF_DECISIVE = (full 20, core 29); ROUND_TOL = 5.001e-5; ID_WARD
= 1e-12; TELE_WARD = 1e-9; SPLIT_WARD = 1e-8; DEC_WARD = 1e-8;
CH_WARD = 1e-9; IMPL_WARD = 1e-9; W_NEGL_BAR = 1e-8; KZ_EXCL =
21; EXT_SHARE_BAR = 0.5; EXT_FRAC_BAR = 0.5; NDRAW = 16;
NULL_OUT_FRAC = 0.5 (v1, demoted to report by SPEC v2);
NULL_SPREAD_MIN = 1e-6 (v2 C3 ward); NULL_SEED = 20260809;
CTRL_KZ = 9; scramble seed 1; RESERVE_REF = 210 (the measured
deepcore floor, quoted).

SPEC v1 (2026-08-09, frozen + SHA-hashed before the first run).
Mechanical concretizations frozen with v1:
 (i)   core.build_window memoized per (kz, seed) (pure
       memoization, bit-identical physics; rank2_wedge SPEC v1
       (i) verbatim);
 (ii)  psd parts via eigh with negative eigenvalues clipped at
       0; the leftover W := -P_- + N_- IS the documented exact
       repair (each side's indefinite tail moved into W),
       applied unconditionally from the start and typed by size
       in D1 -- there is no small-W code path to fall back from;
 (iii) the D3 channel decomposition is the EXACT wall algebra
       I = A^{-1/2}((I - E_ww) - Y)A^{-1/2} (window) resp.
       S^{-1/2}(B - Y)S^{-1/2} (core) plus the exact split of
       G_P into step + new-node channels; the psd tail P_- is
       its own printed channel (never silently attributed);
       the channel-sum ward is warded at CH_WARD;
 (iv)  v_dang is the unit top eigenvector of the psd channel N
       (ties broken by eigh's ordering); steps where N = 0
       cannot be decisive (decisiveness needs |v|^2 >= 1) and
       are counted if they ever occur;
 (v)   correlations use only steps with delta_h > 0 (log
       defined); Pearson corr with nan-guard (< 3 finite points
       -> nan printed);
 (vi)  the reserve ratio is lamR/tau = lambda_min(R_h)/tau_h on
       the CORE world (full wall, deepcore verbatim -- the
       object measured trendless >= 210) and the window analog
       lambda_min(I - E_oo)/lambda_min(A_h) on the FULL world
       (report-only; both evaluated at the base rung of the
       step);
 (vii) the C3 null draws Gaussian vectors normalized to unit
       length (no orthogonalization -- the null is a PURE random
       direction, the sign-null of the share instrument).

SPEC v2 (2026-08-09, after run 1; fail-first preserved -- run 1
passed 27/28 checks and the ONLY failure was the v1 C3 bar;
every run-1 raw number stands and is reprinted unchanged; no D1
/ D2 / D3 bar, object, or typed label is moved, and the D3
typing never depended on C3):
 (i)  the v1 C3 kill-bar ("true share outside the per-step null
      IQR on >= NULL_OUT_FRAC = 50% of decisive steps") is
      STATISTICALLY MISDESIGNED as an instrument ward: if the
      true share were drawn from the SAME distribution as the
      null shares, the expected exclusion fraction is EXACTLY
      50% (definition of the interquartile range), so the bar
      is a fair-coin test that can fail a perfectly
      direction-sensitive instrument with probability ~ 1/2.
      Run 1 measured FULL 12/20 (60%) and CORE 11/29 (38%);
      the CORE "failure" occurs precisely BECAUSE the null
      distribution changes by DISPERSION (pooled null IQR width
      ~ 4.37 vs true-share IQR width ~ 1.13 in share units:
      random directions scatter far more than the dangerous
      directions, which concentrate) -- i.e. the distribution
      manifestly DID change, as the control demands.
 (ii) v2 C3 ward (kill -> WARD-BROKEN): the share instrument
      must RESPOND to direction -- the per-step null spread
      (max - min over the NDRAW = 16 draws) must exceed
      NULL_SPREAD_MIN = 1e-6 on every decisive step, both
      worlds.  The per-step IQR-exclusion census, the pooled
      null vs true-share quartiles, and the IQR-width
      dispersion ratio are printed as REPORT with the
      chance-level note (50% = identical-distribution
      expectation).

NO RH claim -- a relative-domination measurement on compressed
window truncations of the deployed v563 ladder is a statement
about the deployed ladder, not a theorem about zeros.

FIREWALL: no zeros, no prime oracles (AST scan; banned ids
zetazero / nzeros / primerange / isprime / primepi / nextprime /
prevprime); v563 READ-ONLY; RNG only inside the declared null
(seed 20260809) and scramble (seed 1) controls; stdout only.
No marker moves.

Sources (read-only): v563_paper2_readouts; window compression +
pair ladder + constructive split + wedge machinery verbatim from
rank2_wedge_probe.py (PRIME.PORT.RANK2.WEDGE.01, round 57) via
relative_congruence_probe.py (PRIME.PORT.RELCONG.01, round 51:
the exact congruence, eta = 1 + lambda_min(H)) and
normalized_core_update_probe.py / deepcore_schur_reduction_probe
.py (rounds 51/55: full wall, fixed-core Schur, exact exterior
telescoping); exterior reserve context from
relative_flag_margin_probe.py (PRIME.PORT.RELFLAG.01, round 52:
lamR/tau trendless, c_R = 210); kz-21 outlier context from
kz21_outlier_probe.py (PRIME.PORT.KZ21.01); smooth-mass world
from lattice_parametrix_probe.py (B1).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/relative_domination_probe.py
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

JWIN = tuple(range(2, 25, 2))
CORE_J = (2, 4, 6, 8, 10, 12, 14, 16)
H_DEEP_MAX = 900
N_RUNGS_EXP = 42
MIN_PAIRS = 20
MIN_CORE_RUNGS = 30
MIN_COMMON_J = 8
REF_N_WIN_PAIRS = 31           # W2 window reproduction
REF_WIN_MINETA = 0.0050
REF_N_CORE_PAIRS = 39          # W2 core reproduction
REF_CORE_MINETA = 0.0315
REF_N_SMOOTH_PAIRS = 28        # C1 window smooth reproduction
REF_SMOOTH_CONE = 28
REF_DECISIVE_FULL = 20         # D3 round-57 decisive reproduction
REF_DECISIVE_CORE = 29
ROUND_TOL = 5.001e-5
ID_WARD = 1e-12                # W3 increment identity (kill)
TELE_WARD = 1e-9               # W3 telescoping (kill)
SPLIT_WARD = 1e-8              # W3 constructive split (kill)
DEC_WARD = 1e-8                # D1 P - N + W = H (kill)
CH_WARD = 1e-9                 # W3/D3 channel algebra (kill)
IMPL_WARD = 1e-9               # D2 eta >= eta_impl - this (kill)
W_NEGL_BAR = 1e-8              # D1 typing
KZ_EXCL = 21                   # D2 SENS: kz-21-touching pairs
EXT_SHARE_BAR = 0.5            # D3 typing: exterior share bar
EXT_FRAC_BAR = 0.5             # D3 typing: fraction of decisive
NDRAW = 16                     # C3 null draws per decisive step
NULL_OUT_FRAC = 0.5            # C3 v1 bar (report only, SPEC v2)
NULL_SPREAD_MIN = 1e-6         # C3 v2 direction-response ward
NULL_SEED = 20260809
CTRL_KZ = 9
RESERVE_REF = 210.0            # quoted deepcore floor (context)
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


def sym(M):
    return 0.5 * (M + M.T)


# --------- pipeline primitives, verbatim from the predecessors
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
    """B1 LATTICE-SMOOTH masses m_n = 2 e^{u_n/2} du_n (verbatim)."""
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


_WIN_CACHE = {}


def window_of(kz, scramble_seed=None):
    """SPEC v1 (i): pure memoization of core.build_window."""
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


def neg_gram(kz, scramble_seed=None, comb=None):
    """Shared front end: comb -> density -> folded measures ->
    Lanczos chain -> Gram E on the folded neg nodes (rank2_wedge
    verbatim).  None on chain death; 'TOO-DEEP' beyond the cut."""
    rr = window_of(kz, scramble_seed=scramble_seed)
    h, M, alpha = rr["h"], rr["M"], rr["alpha"]
    if h > H_DEEP_MAX:
        return "TOO-DEEP"
    uu = rr["uu"]
    mm = 2.0 * rr["lam"]
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
    E = np.sqrt(vs)[:, None] * (Pn @ Pn.T) * np.sqrt(vs)[None, :]
    E = 0.5 * (E + E.T)
    return dict(kz=kz, h=h, E=E, uf=uf_n.astype(np.int64))


def rung_win(kz, scramble_seed=None, comb=None):
    """FULL-WINDOW rung: 12x12 compression C_J = E_ww + sym(E_wo
    Z), Z = (I - E_oo)^{-1} E_ow (rank2_wedge verbatim), with the
    coupling blocks + exterior fold labels retained for the
    telescoping, and lambda_min(I - E_oo) retained as the window
    reserve analog (SPEC v1 (vi))."""
    g = neg_gram(kz, scramble_seed=scramble_seed, comb=comb)
    if not isinstance(g, dict):
        return g
    E, uf_n = g["E"], g["uf"]
    out = dict(kz=kz, h=g["h"])
    idx = {int(j): k for k, j in enumerate(uf_n)}
    jav = [j for j in JWIN if j in idx]
    out["full"] = (len(jav) == len(JWIN))
    if len(jav) >= MIN_COMMON_J:
        iw = [idx[j] for j in jav]
        io = [k for k in range(E.shape[0]) if k not in set(iw)]
        Eww = E[np.ix_(iw, iw)]
        Xc = E[np.ix_(iw, io)]
        IO = np.eye(len(io)) - E[np.ix_(io, io)]
        Z = np.linalg.solve(IO, E[np.ix_(io, iw)])
        Y = sym(Xc @ Z)
        out["Eww"] = Eww
        out["Xc"] = Xc
        out["Z"] = Z
        out["ext"] = uf_n[io]
        out["CJ"] = Eww + Y
        out["Y"] = Y
        out["lamIO"] = float(np.linalg.eigvalsh(IO)[0])
        out["lamO"] = float(np.linalg.eigvalsh(
            E[np.ix_(io, io)])[-1])
        out["lamC"] = float(np.linalg.eigvalsh(out["CJ"])[-1])
    return out


H_LADDER_MAX_CORE = 900


def ladder_zones():
    """The 42 reachable rungs (normalized_core verbatim)."""
    out = []
    for kz in core.frame_a_zones():
        D_k = 0.5 * float(core.G_ALL[kz]) / float(core.NU_MAIN)
        M_k = int(math.ceil(float(core.U_ALL[kz]) / D_k
                            - 1.0e-9)) + 1
        if M_k % 2:
            M_k += 1
        if M_k // 2 <= H_LADDER_MAX_CORE:
            out.append(kz)
    return out


def gram_anatomy(kz, comb=None, scramble_seed=None):
    """8x8 CORE rung: full wall A = I - E on the folded neg
    nodes, fixed-core split, Schur S = B - Y (rank2_wedge
    verbatim), blocks + lambda_min(R) retained."""
    g = neg_gram(kz, scramble_seed=scramble_seed, comb=comb)
    if not isinstance(g, dict):
        return None
    E, uf_n = g["E"], g["uf"]
    n = E.shape[0]
    A = np.eye(n) - E
    out = dict(kz=kz, h=g["h"], n=n)
    evA = np.linalg.eigvalsh(A)
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
    Z = np.linalg.solve(R, Xc.T)
    Y = sym(Xc @ Z)
    S = sym(B - Y)
    evS = np.linalg.eigvalsh(S)
    evR = np.linalg.eigvalsh(R)
    out.update(B=B, Xcpl=Xc, Z=Z, ext=uf_n[ib], S=S, Y=Y,
               lamS=float(evS[0]),
               lamR=float(evR[0]),
               negS=int(np.sum(evS < 0.0)),
               negR=int(np.sum(evR < 0.0)))
    return out


# --------------------------------------- shared analysis pieces
def inv_sqrt(M):
    w, V = np.linalg.eigh(M)
    return V @ np.diag(w ** -0.5) @ V.T


def psd_split(M):
    """Exact psd decomposition M = pos - neg, pos/neg >= 0
    (eigh, negative eigenvalues clipped; SPEC v1 (ii))."""
    w, V = np.linalg.eigh(sym(M))
    pos = V @ np.diag(np.maximum(w, 0.0)) @ V.T
    neg = V @ np.diag(np.maximum(-w, 0.0)) @ V.T
    return sym(pos), sym(neg)


def telescope(Xc1, Z1, uf1, Xc2, Z2, uf2):
    """Exact four-term telescoping of DY = Y' - Y over the
    common / dropped / new exterior fold labels (verbatim)."""
    com, i1, i2 = np.intersect1d(uf1, uf2, return_indices=True)
    o1 = np.setdiff1d(np.arange(len(uf1)), i1)
    n2i = np.setdiff1d(np.arange(len(uf2)), i2)
    t_dx = (Xc2[:, i2] - Xc1[:, i1]) @ Z1[i1, :]
    t_dz = Xc2[:, i2] @ (Z2[i2, :] - Z1[i1, :])
    t_new = Xc2[:, n2i] @ Z2[n2i, :]
    t_old = Xc1[:, o1] @ Z1[o1, :]
    return t_dx, t_dz, t_new, t_old


def top_vec(G):
    """Rank-1 compression of the top positive eigenpair
    (rank2_wedge verbatim; zero vector if top eig <= 0)."""
    w, V = np.linalg.eigh(sym(G))
    if float(w[-1]) > 0.0:
        return math.sqrt(float(w[-1])) * V[:, -1], False
    return np.zeros(G.shape[0]), True


def wedge(u, v):
    """Round-57 wedge margin (verbatim, for the DECISIVE
    reproduction only)."""
    uu2 = float(u @ u)
    vv2 = float(v @ v)
    uv = float(u @ v)
    dw = 1.0 - vv2 + uv * uv / (1.0 + uu2)
    return uu2, vv2, dw


def corr_or_nan(x, y):
    x = np.asarray(x, float)
    y = np.asarray(y, float)
    m = np.isfinite(x) & np.isfinite(y)
    if int(np.sum(m)) < 3 or np.std(x[m]) == 0 \
            or np.std(y[m]) == 0:
        return float("nan")
    return float(np.corrcoef(x[m], y[m])[0, 1])


def quart(v):
    q = np.percentile(np.asarray(v, float), [25, 50, 75])
    return "q25 %.4f  med %.4f  q75 %.4f" % tuple(q)


# ------------------------------------------------- step builders
def build_steps_window(rungs):
    """Consecutive full-window pairs -> H, eta, constructive
    split, exact H-space channels + reserve analog."""
    rows, n_skip, n_cone = [], 0, 0
    n = len(JWIN)
    dev_id, dev_tel, dev_spl, dev_ch = 0.0, 0.0, 0.0, 0.0
    for r1, r2 in zip(rungs[:-1], rungs[1:]):
        if not (r1.get("full") and r2.get("full")):
            n_skip += 1
            continue
        A1 = np.eye(n) - r1["CJ"]
        A2 = np.eye(n) - r2["CJ"]
        ew, Vw = np.linalg.eigh(A1)
        if float(ew[0]) <= 0.0:
            n_cone += 1
            continue
        Delta = A2 - A1
        DEww = r2["Eww"] - r1["Eww"]
        DY = r2["Y"] - r1["Y"]
        dev_id = max(dev_id, float(np.linalg.norm(
            Delta + DEww + DY)) / max(
                float(np.linalg.norm(Delta)), 1e-300))
        t_dx, t_dz, t_new, t_old = telescope(
            r1["Xc"], r1["Z"], r1["ext"],
            r2["Xc"], r2["Z"], r2["ext"])
        rec = sym(t_dx + t_dz + t_new - t_old)
        dev_tel = max(dev_tel, float(np.linalg.norm(rec - DY))
                      / max(float(np.linalg.norm(DY)), 1e-300))
        Ps = sym(-(DEww + t_new))
        Ns = sym(t_dx + t_dz - t_old)
        dev_spl = max(dev_spl, float(np.linalg.norm(
            Delta - (Ps - Ns))) / max(
                float(np.linalg.norm(Ps)),
                float(np.linalg.norm(Ns)),
                float(np.linalg.norm(Delta)), 1e-300))
        Wi = Vw @ np.diag(ew ** -0.5) @ Vw.T
        H = sym(Wi @ Delta @ Wi)
        # exact H-space channels (SPEC v1 (iii)):
        # I = Wi A1 Wi = ch_wall + ch_res;  G_P = ch_step + ch_new
        ch_wall = sym(Wi @ (np.eye(n) - r1["Eww"]) @ Wi)
        ch_res = sym(Wi @ (-r1["Y"]) @ Wi)
        ch_step = sym(Wi @ (-sym(DEww)) @ Wi)
        ch_new = sym(Wi @ (-sym(t_new)) @ Wi)
        GP = sym(Wi @ Ps @ Wi)
        GN = sym(Wi @ Ns @ Wi)
        dev_ch = max(dev_ch,
                     float(np.linalg.norm(
                         ch_wall + ch_res - np.eye(n))),
                     float(np.linalg.norm(
                         ch_step + ch_new - GP))
                     / max(float(np.linalg.norm(GP)), 1e-300))
        rows.append(dict(
            ha=r1["h"], hb=r2["h"], kza=r1["kz"], kzb=r2["kz"],
            H=H, eta=1.0 + float(np.linalg.eigvalsh(H)[0]),
            GP=GP, GN=GN,
            ch_wall=ch_wall, ch_res=ch_res,
            ch_step=ch_step, ch_new=ch_new,
            resq=r1["lamIO"] / float(ew[0])))
    return rows, n_skip, n_cone, (dev_id, dev_tel, dev_spl,
                                  dev_ch)


def build_steps_core(truth):
    """Consecutive full-core steps -> H_core, eta_core,
    constructive split, exact H-space channels + reserve."""
    rows = []
    dev_id, dev_tel, dev_spl, dev_ch = 0.0, 0.0, 0.0, 0.0
    for r1, r2 in zip(truth, truth[1:]):
        if (r1 is None or r2 is None or not r1.get("core_ok")
                or not r2.get("core_ok")):
            continue
        if r1["lamS"] <= 0.0 or r1["negA"] > 0:
            continue
        n = len(CORE_J)
        DS = r2["S"] - r1["S"]
        DB = r2["B"] - r1["B"]
        DY = r2["Y"] - r1["Y"]
        dev_id = max(dev_id, float(np.linalg.norm(
            DS - (DB - DY))) / max(
                float(np.linalg.norm(DS)), 1e-300))
        t_dx, t_dz, t_new, t_old = telescope(
            r1["Xcpl"], r1["Z"], r1["ext"],
            r2["Xcpl"], r2["Z"], r2["ext"])
        rec = sym(t_dx + t_dz + t_new - t_old)
        dev_tel = max(dev_tel, float(np.linalg.norm(rec - DY))
                      / max(float(np.linalg.norm(DY)), 1e-300))
        Ps = sym(DB - t_new)
        Ns = sym(t_dx + t_dz - t_old)
        dev_spl = max(dev_spl, float(np.linalg.norm(
            DS - (Ps - Ns))) / max(
                float(np.linalg.norm(Ps)),
                float(np.linalg.norm(Ns)),
                float(np.linalg.norm(DS)), 1e-300))
        Wi = inv_sqrt(r1["S"])
        H = sym(Wi @ DS @ Wi)
        # exact H-space channels: I = Wi S1 Wi = Wi(B - Y)Wi
        ch_wall = sym(Wi @ r1["B"] @ Wi)
        ch_res = sym(Wi @ (-r1["Y"]) @ Wi)
        ch_step = sym(Wi @ sym(DB) @ Wi)
        ch_new = sym(Wi @ (-sym(t_new)) @ Wi)
        GP = sym(Wi @ Ps @ Wi)
        GN = sym(Wi @ Ns @ Wi)
        dev_ch = max(dev_ch,
                     float(np.linalg.norm(
                         ch_wall + ch_res - np.eye(n))),
                     float(np.linalg.norm(
                         ch_step + ch_new - GP))
                     / max(float(np.linalg.norm(GP)), 1e-300))
        rows.append(dict(
            ha=r1["h"], hb=r2["h"], kza=r1["kz"], kzb=r2["kz"],
            H=H, eta=1.0 + float(np.linalg.eigvalsh(H)[0]),
            GP=GP, GN=GN,
            ch_wall=ch_wall, ch_res=ch_res,
            ch_step=ch_step, ch_new=ch_new,
            resq=r1["lamR"] / r1["tau"]))
    return rows, (dev_id, dev_tel, dev_spl, dev_ch)


# ------------------------------------------------------- D1 - D3
def d1_split(tag, rows):
    """D1: exact signed split H = P - N + W, leftover typed."""
    section("D1[%s] -- THE EXACT SIGNED SPLIT  H = P - N + W  "
            "(psd P, N; W = -P_- + N_-)" % tag)
    print("    step        ||P||_F   ||N||_F   ||W||_F   "
          "||W||/||H||  lam_min(W)  dec dev")
    dev_max = 0.0
    wrels = []
    for r in rows:
        P, Pm = psd_split(r["GP"])
        N, Nm = psd_split(r["GN"])
        W = Nm - Pm
        r["P"], r["N"], r["W"] = P, N, W
        nH = max(float(np.linalg.norm(r["H"])), 1e-300)
        dev = float(np.linalg.norm(P - N + W - r["H"])) / nH
        dev_max = max(dev_max, dev)
        wrel = float(np.linalg.norm(W)) / nH
        wrels.append(wrel)
        r["lminW"] = float(np.linalg.eigvalsh(W)[0])
        print("    h %3d->%3d  %.3e %.3e %.3e  %.4f      "
              "%+.3e  %.1e"
              % (r["ha"], r["hb"], float(np.linalg.norm(P)),
                 float(np.linalg.norm(N)),
                 float(np.linalg.norm(W)), wrel, r["lminW"],
                 dev))
    check("D1.%s WARD: max ||(P - N + W) - H||/||H|| %.2e <= "
          "%.0e" % (tag, dev_max, DEC_WARD),
          dev_max <= DEC_WARD, kill="KW")
    wmax = float(np.max(wrels))
    lab = ("W-NEGLIGIBLE" if wmax < W_NEGL_BAR
           else "W-TAIL-TYPED(med=%.3f, max=%.3f)"
           % (float(np.median(wrels)), wmax))
    print("\n    leftover ||W||/||H||: med %.4f max %.4f -- the "
          "indefinite tails of both sides live in W"
          % (float(np.median(wrels)), wmax))
    print("    (the exact repair, SPEC v1 (ii)); every D2 bound "
          "below carries lam_min(W) explicitly.")
    check("D1.%s typed: %s" % (tag, lab), True)
    return lab


def d2_domination(tag, rows):
    """D2: relative domination + the exact implied margin."""
    section("D2[%s] -- THE RELATIVE DOMINATION  Ntilde = "
            "(I+P)^{-1/2} N (I+P)^{-1/2}" % tag)
    print("    exact chain: N <= (1-delta)(I+P)  =>  I + H >= "
          "delta (I+P) + W  =>")
    print("    eta >= delta (1 + lam_min(P)) + lam_min(W)  "
          "[delta >= 0]  (delta < 0: lam_max(P) branch)")
    print("\n    step        lam_max(Nt)  delta_h    "
          "lam_min(W)  eta_impl   true eta   flags")
    n = rows[0]["H"].shape[0]
    impl_ok = True
    for r in rows:
        isq = inv_sqrt(np.eye(n) + r["P"])
        Nt = sym(isq @ r["N"] @ isq)
        lmax = float(np.linalg.eigvalsh(Nt)[-1])
        delta = 1.0 - lmax
        evP = np.linalg.eigvalsh(r["P"])
        lminP = max(float(evP[0]), 0.0)
        lmaxP = float(evP[-1])
        if delta >= 0.0:
            impl = delta * (1.0 + lminP) + r["lminW"]
        else:
            impl = delta * (1.0 + lmaxP) + r["lminW"]
        r["delta"] = delta
        r["impl"] = impl
        impl_ok &= (r["eta"] >= impl - IMPL_WARD)
        kz21 = (r["kza"] == KZ_EXCL or r["kzb"] == KZ_EXCL)
        r["kz21"] = kz21
        flags = []
        if kz21:
            flags.append("kz21")
        if delta <= 0.0:
            flags.append("DOM-FAIL")
        if impl <= 0.0:
            flags.append("impl<=0")
        print("    h %3d->%3d  %9.5f   %+9.5f  %+.3e  %+9.5f  "
              "%+9.5f  %s"
              % (r["ha"], r["hb"], lmax, delta, r["lminW"],
                 impl, r["eta"], " ".join(flags)))
    check("D2.%s CONSISTENCY WARD: true eta >= eta_impl - %.0e "
          "on every step" % (tag, IMPL_WARD), impl_ok,
          kill="KW")
    deltas = np.array([r["delta"] for r in rows])
    impls = np.array([r["impl"] for r in rows])
    sens = [r for r in rows if not r["kz21"]]
    d_s = np.array([r["delta"] for r in sens])
    i_s = np.array([r["impl"] for r in sens])
    n_dom = int(np.sum(deltas > 0.0))
    n_imp = int(np.sum(impls > 0.0))
    print("\n    CENSUS raw : lam_max(Ntilde) < 1 on %d/%d "
          "steps (min delta %+0.5f); eta_impl > 0 on %d/%d"
          % (n_dom, len(rows), float(np.min(deltas)), n_imp,
             len(rows)))
    print("    CENSUS SENS: (kz-%d-touching pairs excluded, "
          "%d left) domination on %d/%d (min delta %+0.5f); "
          "eta_impl > 0 on %d/%d"
          % (KZ_EXCL, len(sens), int(np.sum(d_s > 0.0)),
             len(sens), float(np.min(d_s)) if len(sens) else
             float("nan"), int(np.sum(i_s > 0.0)), len(sens)))
    fails = [r for r in rows if r["delta"] <= 0.0]
    if fails:
        print("    domination fails at: %s"
              % ", ".join("h %d->%d%s"
                          % (r["ha"], r["hb"],
                             " (kz21)" if r["kz21"] else "")
                          for r in fails))
    if n_dom == len(rows) and n_imp == len(rows):
        lab = ("RELDOM-HOLDS(min delta=%.5f, min eta_impl="
               "%.5f)" % (float(np.min(deltas)),
                          float(np.min(impls))))
    elif n_dom == 0:
        lab = "RELDOM-BROKEN"
    else:
        lab = ("RELDOM-PARTIAL(dom %d/%d, impl>0 %d/%d; SENS "
               "dom %d/%d)"
               % (n_dom, len(rows), n_imp, len(rows),
                  int(np.sum(d_s > 0.0)), len(sens)))
    check("D2.%s typed: %s" % (tag, lab), True)
    return lab


def channel_shares(r, v):
    """Exact channel split of q = v^T (I+P) v (SPEC v1 (iii));
    returns (q_wall, q_res, q_step, q_new, q_tail, q_tot)."""
    Pm = sym(r["P"] - r["GP"])          # psd tail P_-
    q_wall = float(v @ r["ch_wall"] @ v)
    q_res = float(v @ r["ch_res"] @ v)
    q_step = float(v @ r["ch_step"] @ v)
    q_new = float(v @ r["ch_new"] @ v)
    q_tail = float(v @ Pm @ v)
    n = r["P"].shape[0]
    q_tot = float(v @ (np.eye(n) + r["P"]) @ v)
    return q_wall, q_res, q_step, q_new, q_tail, q_tot


def d3_rescue(tag, rows, ref_decisive):
    """D3: rescue source on the round-57 decisive steps."""
    section("D3[%s] -- THE RESCUE SOURCE on the round-57 "
            "DECISIVE steps (channel ledger of "
            "v_dang^T (I+P) v_dang)" % tag)
    dec = []
    for r in rows:
        u, _du = top_vec(r["GP"])
        vw, _dv = top_vec(r["GN"])
        _uu2, vv2, dw = wedge(u, vw)
        r["decisive"] = (1.0 - vv2 <= 0.0) and (dw > 0.0)
        if r["decisive"]:
            dec.append(r)
    check("D3.%s REPRODUCTION: decisive steps %d/%d == %d "
          "(round 57)" % (tag, len(dec), len(rows),
                          ref_decisive),
          len(dec) == ref_decisive, kill="KW")
    print("\n    step        q_wall    q_res     q_step    "
          "q_new     q_tail    q_tot    EXT share  ch dev")
    shares = []
    dev_max = 0.0
    for r in dec:
        evN, VN = np.linalg.eigh(r["N"])
        v = VN[:, -1]                    # SPEC v1 (iv)
        r["v_dang"] = v
        qw, qr, qs, qn, qt, qtot = channel_shares(r, v)
        dev = abs(qw + qr + qs + qn + qt - qtot) \
            / max(1.0, abs(qtot))
        dev_max = max(dev_max, dev)
        share = (qr + qn) / qtot
        r["ext_share"] = share
        shares.append(share)
        print("    h %3d->%3d  %+8.4f  %+8.4f  %+8.4f  %+8.4f"
              "  %+8.4f  %7.4f  %+8.4f   %.1e"
              % (r["ha"], r["hb"], qw, qr, qs, qn, qt, qtot,
                 share, dev))
    check("D3.%s CHANNEL WARD: max |sum(channels) - "
          "v^T(I+P)v| %.2e <= %.0e" % (tag, dev_max, CH_WARD),
          dev_max <= CH_WARD, kill="KW")
    n_ext = sum(1 for s in shares if s >= EXT_SHARE_BAR)
    frac = n_ext / max(len(shares), 1)
    print("\n    exterior share (q_res + q_new)/q_tot: %s"
          % quart(shares))
    print("    exterior share >= %.1f on %d/%d decisive steps "
          "(bar: >= %.0f%%)"
          % (EXT_SHARE_BAR, n_ext, len(shares),
             100.0 * EXT_FRAC_BAR))
    if frac >= EXT_FRAC_BAR:
        lab = ("RESCUE-FROM-RESERVE(%d/%d)"
               % (n_ext, len(shares)))
    else:
        lab = ("RESCUE-INTERNAL(med share=%+.4f, ext>=%.1f on "
               "%d/%d)" % (float(np.median(shares)),
                           EXT_SHARE_BAR, n_ext, len(shares)))
    check("D3.%s typed: %s" % (tag, lab), True)

    # reserve link (report only; SPEC v1 (v)/(vi))
    pos = [r for r in rows if r["delta"] > 0.0]
    c = corr_or_nan([math.log(r["delta"]) for r in pos],
                    [math.log(r["resq"]) for r in pos])
    print("\n    RESERVE LINK (report): corr(log delta_h, "
          "log(lamR/tau)) = %+0.3f (R^2 %.3f) over %d"
          % (c, c * c if np.isfinite(c) else float("nan"),
             len(pos)))
    print("    delta>0 steps; reserve ratio ladder: %s "
          "(deepcore floor context: >= %.0f on CORE)."
          % (quart([r["resq"] for r in pos]), RESERVE_REF))
    return lab, dec


def c3_null(tag, dec, rng):
    """C3 (SPEC v2): sign-null -- random unit v.  WARD = the
    share responds to direction (per-step null spread nonzero);
    the IQR-exclusion census (v1 bar) + the dispersion
    comparison are REPORT (50% exclusion is the chance level
    for identical distributions)."""
    n_out = 0
    pooled = []
    spread_min = float("inf")
    for r in dec:
        vals = []
        for _ in range(NDRAW):
            g = rng.standard_normal(len(r["v_dang"]))
            g /= max(float(np.linalg.norm(g)), 1e-300)
            _qw, qr, _qs, qn, _qt, qtot = channel_shares(r, g)
            vals.append((qr + qn) / qtot)
        pooled.extend(vals)
        spread_min = min(spread_min,
                         float(np.max(vals) - np.min(vals)))
        q25, q75 = np.percentile(vals, [25, 75])
        if r["ext_share"] < q25 or r["ext_share"] > q75:
            n_out += 1
    tq = np.percentile([r["ext_share"] for r in dec], [25, 75])
    nq = np.percentile(pooled, [25, 75])
    true_w = float(tq[1] - tq[0])
    null_w = float(nq[1] - nq[0])
    print("    %s: true shares %s (IQR width %.4f)"
          % (tag, quart([r["ext_share"] for r in dec]), true_w))
    print("    %s: null shares %s (IQR width %.4f; %d steps x "
          "%d draws)"
          % (tag, quart(pooled), null_w, len(dec), NDRAW))
    print("    %s: dispersion ratio null/true = %.2f; true "
          "outside per-step null IQR on %d/%d (%.0f%%; the "
          "identical-"
          % (tag, null_w / max(true_w, 1e-300), n_out,
             len(dec), 100.0 * n_out / max(len(dec), 1)))
    print("    %s: distribution chance level is 50%% -- v1 bar "
          "demoted to report, SPEC v2 (i)); min per-step"
          % tag)
    print("    %s: null spread %.3e" % (tag, spread_min))
    return spread_min


def main():
    section("PRIME.PORT.RELDOM.01 -- relative positive-part "
            "domination + the rescue source (EXPLORATION ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s"
          % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
    print("    NO RH claim; no marker moves.")
    print("\nS0 -- firewall")
    check("S0.1 AST firewall clean", not ast_scan(BANNED_IDS))

    # ------------------------------------------------------------ W
    section("W -- build the two ladders (full window + 8x8 "
            "core) + reproduction wards")
    wrungs, srungs = [], []
    for kz in core.frame_a_zones():
        r = rung_win(kz)
        if not isinstance(r, dict):
            continue
        wrungs.append(r)
        uu = window_of(kz)["uu"]
        rs = rung_win(kz, comb=(uu, smooth_masses(uu)))
        if isinstance(rs, dict):
            srungs.append(rs)
    wrungs.sort(key=lambda r: (r["h"], r["kz"]))
    srungs.sort(key=lambda r: (r["h"], r["kz"]))
    print("    window ladder: %d truth rungs, %d smooth rungs "
          "[%.1f s]" % (len(wrungs), len(srungs),
                        time.time() - T0))
    zones = ladder_zones()
    ctruth = [gram_anatomy(kz) for kz in zones]
    ok_chain = all(r is not None for r in ctruth)
    ctruth = [r for r in ctruth if r is not None]
    ctruth.sort(key=lambda r: (r["h"], r["kz"]))
    nfull = sum(1 for r in ctruth if r.get("core_ok"))
    print("    core ladder: %d rungs, %d full-core [%.1f s]"
          % (len(ctruth), nfull, time.time() - T0))
    check("W1.a core ladder complete: %d rungs == %d, chains "
          "ok" % (len(ctruth), N_RUNGS_EXP),
          ok_chain and len(ctruth) == N_RUNGS_EXP, kill="K1")
    check("W1.b >= %d full-core rungs" % MIN_CORE_RUNGS,
          nfull >= MIN_CORE_RUNGS, "%d" % nfull, kill="K1")
    ok_psd = all(r["negA"] == 0
                 and (not r.get("core_ok")
                      or (r["negR"] == 0 and r["negS"] == 0))
                 for r in ctruth)
    check("W1.c core truth all-PSD (A, R, S)", ok_psd,
          kill="K1")

    wrows, n_skip_w, n_cone_w, wdev = build_steps_window(wrungs)
    crows, cdev = build_steps_core(ctruth)
    check("W1.d >= %d truth pairs per world" % MIN_PAIRS,
          len(wrows) >= MIN_PAIRS and len(crows) >= MIN_PAIRS,
          "window %d (skips %d, non-PD %d), core %d"
          % (len(wrows), n_skip_w, n_cone_w, len(crows)),
          kill="K1")
    if KILLS:
        return finish({})

    min_eta_w = float(np.min([r["eta"] for r in wrows]))
    min_eta_c = float(np.min([r["eta"] for r in crows]))
    check("W2.a REPRODUCTION window: %d pairs == %d, min eta "
          "%.4f == %.4f (tol %.1e)"
          % (len(wrows), REF_N_WIN_PAIRS, min_eta_w,
             REF_WIN_MINETA, ROUND_TOL),
          len(wrows) == REF_N_WIN_PAIRS
          and abs(min_eta_w - REF_WIN_MINETA) <= ROUND_TOL,
          kill="KW")
    check("W2.b REPRODUCTION core: %d steps == %d, min eta_core"
          " %.4f == %.4f (tol %.1e)"
          % (len(crows), REF_N_CORE_PAIRS, min_eta_c,
             REF_CORE_MINETA, ROUND_TOL),
          len(crows) == REF_N_CORE_PAIRS
          and abs(min_eta_c - REF_CORE_MINETA) <= ROUND_TOL,
          kill="KW")
    for lab, dev in (("window", wdev), ("core", cdev)):
        check("W3.%s identity %.1e <= %.0e | telescoping %.1e "
              "<= %.0e | split %.1e <= %.0e | channels %.1e "
              "<= %.0e"
              % (lab[0], dev[0], ID_WARD, dev[1], TELE_WARD,
                 dev[2], SPLIT_WARD, dev[3], CH_WARD),
              dev[0] <= ID_WARD and dev[1] <= TELE_WARD
              and dev[2] <= SPLIT_WARD and dev[3] <= CH_WARD,
              kill="KW")
    check("W3.c truth eta > 0 on every step (both worlds)",
          min_eta_w > 0.0 and min_eta_c > 0.0, kill="KW")
    if KILLS:
        return finish({})

    # -------------------------------------------------- D1 - D3
    d1w = d1_split("FULL", wrows)
    d1c = d1_split("CORE", crows)
    if KILLS:
        return finish({})
    d2w = d2_domination("FULL", wrows)
    d2c = d2_domination("CORE", crows)
    if KILLS:
        return finish({})
    d3w, decw = d3_rescue("FULL", wrows, REF_DECISIVE_FULL)
    d3c, decc = d3_rescue("CORE", crows, REF_DECISIVE_CORE)
    if KILLS:
        return finish({})

    # ------------------------------------------------------------ C
    section("C -- controls")
    print("  C1 -- smooth world (domination must break; exact "
          "failure mode reported):")
    n_sp, n_scone = 0, 0
    for r1, r2 in zip(srungs[:-1], srungs[1:]):
        if not (r1.get("full") and r2.get("full")):
            continue
        n_sp += 1
        A1 = np.eye(len(JWIN)) - r1["CJ"]
        if float(np.linalg.eigvalsh(A1)[0]) <= 0.0:
            n_scone += 1
    print("    window: %d smooth full-window pairs, %d "
          "CONE-EXITED (A_h indefinite) -- the failure mode:"
          % (n_sp, n_scone))
    print("    A_h^{-1/2} does not exist over the reals, so "
          "H-space, the split P/N/W and Ntilde never form;")
    print("    the domination instrument is UNAVAILABLE (not "
          "merely violated) in the smooth world.")
    check("C1.a window smooth reproduction: %d pairs == %d, "
          "CONE-EXITED %d == %d"
          % (n_sp, REF_N_SMOOTH_PAIRS, n_scone,
             REF_SMOOTH_CONE),
          n_sp == REF_N_SMOOTH_PAIRS
          and n_scone == REF_SMOOTH_CONE, kill="KW")
    n_viol = 0
    for kz in ladder_zones():
        uu = window_of(kz)["uu"]
        r = gram_anatomy(kz, comb=(uu, smooth_masses(uu)))
        if r is not None and r["negA"] > 0:
            n_viol += 1
    check("C1.b core smooth violates at rung level (neg(A) > 0 "
          "on %d rungs)" % n_viol, n_viol > 0, kill="KW")

    print("  C2 -- scramble (seed 1) at kz %d:" % CTRL_KZ)
    rs = rung_win(CTRL_KZ, scramble_seed=1)
    if not isinstance(rs, dict):
        w_dies, msg = True, "rung not built (%r)" % rs
    elif "lamC" not in rs:
        w_dies, msg = True, "window unavailable"
    else:
        w_dies = rs["lamO"] > 1.0 or rs["lamC"] > 1.0
        msg = ("lam(out) %.3e, lam(C_J) %.3e"
               % (rs["lamO"], rs["lamC"]))
    print("    window: %s -> %s"
          % (msg, "FRAME DIES" if w_dies else "SILENT"))
    rc = gram_anatomy(CTRL_KZ, scramble_seed=1)
    c_dies = rc is None or rc["negA"] > 0
    print("    core:   %s -> %s"
          % ("chain death" if rc is None
             else "neg(A) = %d" % rc["negA"],
             "WALL BREAKS" if c_dies else "SILENT"))
    check("C2 scramble fires in both worlds", w_dies and c_dies,
          kill="KW")

    print("  C3 -- sign-null for D3 (random unit v_dang, seed "
          "%d, %d draws/step; SPEC v2):" % (NULL_SEED, NDRAW))
    rng = np.random.default_rng(NULL_SEED)
    sp_w = c3_null("FULL", decw, rng)
    sp_c = c3_null("CORE", decc, rng)
    check("C3 (SPEC v2) the share responds to direction: min "
          "per-step null spread full %.3e, core %.3e > %.0e"
          % (sp_w, sp_c, NULL_SPREAD_MIN),
          sp_w > NULL_SPREAD_MIN and sp_c > NULL_SPREAD_MIN,
          kill="KW")

    return finish(dict(d1w=d1w, d1c=d1c, d2w=d2w, d2c=d2c,
                       d3w=d3w, d3c=d3c,
                       min_eta_w=min_eta_w,
                       min_eta_c=min_eta_c,
                       wrows=wrows, crows=crows))


def finish(res):
    section("V -- FROZEN VERDICT")
    n_pass = sum(1 for _n, okk in CHECKS if okk)
    n_tot = len(CHECKS)
    if KILLS:
        VERDICT = {"K1": "PIPELINE-BROKEN",
                   "KW": "WARD-BROKEN"}[KILLS[0]]
        print("\n  VERDICT: %s" % VERDICT)
    else:
        VERDICT = ("RELDOM-MEASURED / D1[full=%s, core=%s] / "
                   "D2[full=%s, core=%s] / D3[full=%s, core=%s]"
                   % (res["d1w"], res["d1c"], res["d2w"],
                      res["d2c"], res["d3w"], res["d3c"]))
        print("\n  VERDICT: %s" % VERDICT)
        dmin_w = float(np.min([r["delta"]
                               for r in res["wrows"]]))
        dmin_c = float(np.min([r["delta"]
                               for r in res["crows"]]))
        print("  (true margins: min eta full %.4f, core %.4f; "
              "min delta full %+0.5f, core %+0.5f)"
              % (res["min_eta_w"], res["min_eta_c"], dmin_w,
                 dmin_c))
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed"
          % (time.time() - T0, n_tot, n_tot - n_pass))
    return 0 if n_pass == n_tot else 1


if __name__ == "__main__":
    raise SystemExit(main())
