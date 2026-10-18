#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""mt_window_family_probe -- PRIME.PORT.MTWINDOW.01
(EXPLORATION ONLY, experiments/; round 64, RH-side auxiliary: the
MONTGOMERY-TAYLOR WINDOW FAMILY TEST -- a FOREIGN test of the
deployed window architecture.  2026-08-11.)

THE QUESTION (frozen).  The deployed wall (v563: atoms u_n = log n,
mu_n = 2 Lambda(n)/sqrt n; width-D triangular TENT lags via
atom_lags_at; arch lags with the SAME tent inside the archimedean
integrand; odd Toeplitz K; margin lam_min(K)) uses ONE window
kernel: the tent.  Build a PARALLEL lag assembly in which the tent
is replaced by alternative window kernels -- everything else
identical (same atoms, same D/M/h frame conventions, same arch
layer treatment) -- and measure whether the wall STRUCTURE
(halfgap, B-floor, x = +1 band, truth-specificity) survives the
window change or only its CONSTANTS move.

THE KERNEL FAMILY (frozen; all supported on [-D, D], k(0) = 1):
 K0 TENT (deployed, regression baseline): k(x) = max(0, 1-|x|/D).
    The parallel assembly with K0 must reproduce the deployed wall
    BIT-FOR-BIT (master ward W1: lag vectors np.array_equal against
    core.arch_lags + core.atom_lags_at on every frame).
 K1 MT (the Montgomery-Taylor cosine): v*(s) = cos(sqrt2 lam s) --
    the optimizer of the two-moment functional (EXTERNAL-CITED
    pedigree: the Anthropic zeta paper's Montgomery-Taylor window;
    no result of that paper is consumed, only the window SHAPE).
    DECLARED support mapping onto the tent's width-D slot: s = x/D
    on |x| <= D, lam = pi/(2 sqrt2) so sqrt2 lam = pi/2 and the
    edge zero v*(+-1) = 0 matches the tent's edge zero;
    normalization v*(0) = 1 = tent(0).  So k(x) = cos((pi/2) x/D).
 K2 FEJ (raised cosine / Hann, the classical family anchor):
    k(x) = (1/2)(1 + cos(pi x/D)) = cos^2((pi/2) x/D) on |x| <= D.
ARCH LAYER KERNEL-DEPENDENCE (documented, frozen): the arch layer
is kernel-dependent in exactly two seats -- the delta term
-(gamma + log pi) k(s) and the principal-value integral of
k(s -+ w) against the archimedean density.  Both are REDERIVED per
kernel by substituting k for the tent in the deployed integrand
(_arch_A_far / _arch_A_near verbatim, kernel swapped); the
Gauss-Legendre panel decomposition and the near-case breakpoints
{0, s, D-s, s+D} are kept tent-verbatim (declared: for the smooth
kernels these are redundant panel splits, harmless to quadrature).
DIAG (recorded, no bar): Bochner positive-definiteness of each
kernel via the numerically evaluated Fourier transform on a
declared grid -- the tent is PD (Fejer square), the MT half-cosine
and the Hann anchor are NOT PD (sign-changing transforms); whether
that kills the wall is exactly what is being measured.

THE SURFACE (frozen): the deployed SUBSET rungs kz = (9, 13, 26,
40, 60, 90, 121) of the faithful 67-rung ladder (race verbatim),
PLUS the DEEP_PICK = 3 shallowest-h NEW holdout rungs of the 4e6
extended table (deep_blind_holdout conventions: TAB_EXT = 4e6,
faithful NEW iff ATOM_MAX < X <= TAB_EXT and h in H_HOLD =
[128, 2900]; prefix arrays warded bitwise).  Edge/band diagnostics
on EDGE_KZ = (9, 13, 26, 40) only (chain cost; declared).

THE FIVE MEASUREMENTS (frozen):
 (a) HALFGAP: per kernel per rung m = lam_min(K), shat = m/mu1(h)
     with mu1(h) = 4 sin^2(pi/(2h+1)) (the deployed shat
     convention, moving_node_second_order verbatim; deployed band
     0.502..2.185).  Typed: wall positivity count, base-halfgap
     count (shat >= 1/2 -- the registered half inequality), min/
     med/max shat, per-rung ratio to the tent column.
 (b) B-FLOOR (full-frame co-block, directional_lanczos_fullframe
     conventions -- the tangent-Schur 8x8 core rebuild is declared
     TOO DEEP for a foreign-window rebuild; the sanctioned wall-
     level object is used instead): v_sm = bottom eigenvector of
     the SAME-KERNEL smooth wall (PNT continuum comb, ng =
     max(6000, 8M) -- the A1 resolution law; at kz = 9 this equals
     the deployed 6000 control convention), Householder split of
     the TRUTH wall along v_sm, floor = lam_min(co-block), report
     floor/tau in that kernel's own tau = lam_min(K) units.
     Reference context (cited, not recomputed here): tangent-split
     core floor min 0.679 absolute; full-frame deployed floor/tau
     ~ 2.1..5.2 with med ~ 2.77.  Typed per kernel: refusals
     (floor <= 0), min/med/max floor/tau, ratio to the tent
     column.
 (c) x = +1 EDGE/BAND (wall_gram_radau / band_arithmetic_anatomy
     conventions): fold the lag vector (grid_density -> folded
     signed families), Lanczos chain on mu_+, localized Lukacs
     floors lam_min(M1x2), lam_min(Mm), lam_min(Mp) at matched
     degree; the WGT negative-side eigenvector-energy band share
     within DELTA = 1e-2 of x = +1 (Mm bottom eigenvector, round-
     60 seat: tent med 0.942), band width delta* at the 0.90
     energy quantile, peak x, RAW mu_- band mass share.  Warded
     (tent): Mm fails on every edge rung and med WGT share >=
     0.90; M0 two-route (I - H vs quadrature) <= M0_WARD per
     kernel (assembly identity; skipped only on CHAIN-INCOMPLETE,
     which is typed, never silent).
 (d) TRUTH-SPECIFICITY: at CTRL_KZ = 9 per kernel, all three
     controls must BREAK the wall (lam_min < 0): smooth PNT comb,
     position scramble (core.build_window scramble_seed = 1),
     Epstein x^2+5y^2 comb (lambda_eps verbatim).  Additionally
     the smooth wall lam_sm is recorded on EVERY rung per kernel.
     A kernel with ANY silent control is typed SPEC-DEAD
     (worthless -- the Weyl lesson); kill-grade ONLY for the tent
     (CONTROL-DEAD).
 (e) TAU-SCREENS on all new margins (CLIX bands: PASS |slope| <=
     0.30, RELOC slope >= 0.70, else AMBIG; OLS of log metric vs
     log tau over positive rungs): shat, floor/tau, |lam_Mm|/
     |tau_gram|.

FROZEN VERDICT RULES (per metric, per foreign kernel; RATIO_BAR =
0.10, SHARE_BAR = 0.05):
 HALFGAP: WORSE iff any truth lam_min <= 0 or (any shat < 1/2
   while the tent keeps shat >= 1/2 everywhere); BETTER iff no
   violation and min shat >= (1 + RATIO_BAR) x tent min; else
   NEUTRAL.  HALFGAP-BASE-STABLE/VIOLATED typed alongside.
 BFLOOR: WORSE iff any refusal or med(floor/tau) < (1 -
   RATIO_BAR) x tent med; BETTER iff no refusal and med >= (1 +
   RATIO_BAR) x tent med; else NEUTRAL.  (floor/tau only defined
   on tau > 0 rungs; rungs with tau <= 0 count as refusals.)
 BAND: BAND-CERTIFIED (BETTER, structural) iff all three Lukacs
   floors >= -LOC_TOL on all usable edge rungs; else with r_f =
   med(|lam_Mm|/|tau_gram|) ratio to tent and d_s = med share
   difference to tent: BETTER iff (r_f <= 1 - RATIO_BAR or d_s <=
   -SHARE_BAR) and not (r_f >= 1 + RATIO_BAR or d_s >= +
   SHARE_BAR); WORSE iff the mirrored condition; else NEUTRAL;
   NA iff chain incomplete on every edge rung.  AMENDMENT A1
   (disclosed after smoke 1, before freezing; no bar moved): the
   band-shrink comparison presumes a wall to diagnose -- BAND is
   typed MTWINDOW-NA(GRAM-WALL-NEGATIVE) iff any usable edge rung
   has tau_gram <= 0 for that kernel (the smoke exhibited an MT
   Gram frame at tau_gram ~ -2e70 whose ratio r_f = 0.00 would
   have read as a spurious BETTER); the descriptive census
   (floors, share, width, peak) stays recorded either way, and
   GRAM-WALL-NEGATIVE joins the structure flags.
 SPEC: WORSE (SPEC-DEAD) iff any control silent; else NEUTRAL.
STRUCTURAL-VS-CONSTANTS (the honest summary, frozen): a kernel
CHANGES STRUCTURE iff any of {truth wall sign flip, base-halfgap
violation, control silence, Lukacs floor sign flip to certified,
B-floor refusal} differs from the tent column; else it moves
CONSTANTS-ONLY (ratio table printed).

WARDS (kill): K1 BASELINE-BROKEN -- W1 master ward, the parallel
K0 assembly must equal the deployed lag vector np.array_equal
(bit-for-bit) on every frame (deployed frames against core.
arch_lags + core.atom_lags_at; deep frames against the same core
functions on the extended arrays -- the deep-holdout convention);
K2 WALL-BROKEN -- W2 v884 certified floors at kz 9/13 (3.633e-4 /
3.842e-4), W3 tent subset shat inside the 67-rung band [0.502,
2.185] with rtol 2e-2; K3 DEEP-BROKEN -- W4 extended table prefix
bitwise (LAM/NN/U/MU), extended Chebyshev kappa <= KAPPA_REF +
1e-6, >= DEEP_PICK new rungs found; K4 CONTROL-DEAD -- tent
controls must all fire; K5 WARD-BROKEN -- M0 two-route dev >
M0_WARD on a usable rung, or the C-NO-RH check.  Typed outcomes
(a)-(e) are measurements, NEVER kills.

FROZEN BARS: SUBSET = (9, 13, 26, 40, 60, 90, 121); EDGE_KZ =
(9, 13, 26, 40); CTRL_KZ = 9; DEEP_PICK = 3; TAB_EXT = 4e6;
H_HOLD = (128, 2900); KZ_SCAN_MAX = 400; NG_SMOOTH_MIN = 6000;
NG_FACT = 8; DELTA_BAND = 1e-2; LOC_TOL = 1e-10; M0_WARD = 1e-9;
CERT = {9: 3.633e-4, 13: 3.842e-4}; SHAT_BAND = (0.502, 2.185),
band rtol 2e-2; RATIO_BAR = 0.10; SHARE_BAR = 0.05; SCREEN 0.30/
0.70; scramble seed 1; LAM_MT = pi/(2 sqrt2); Bochner grid omega
in [0, 40/D], 4001 points, 20000-point trapezoid in x.

ANTI-CIRCULARITY (frozen): no zero of any L-function, no prime
oracle (AST firewall, banned ids zetazero / nzeros / primerange /
isprime / primepi / nextprime / prevprime); v563 READ-ONLY; RNG
only inside the deployed scramble control (seed 1, inside
core.build_window); tau of a kernel's wall enters that kernel's
OWN reporting units and screens only, never any construction;
v_sm is prime-free given the frame + kernel.

NO RH CLAIM (frozen): this probe measures a FOREIGN window family
against the deployed architecture on finite rungs; nothing here
is evidence for or against RH in either direction; no marker
moves, no ledger row, no paper edit, nothing outside
experiments/.

SMOKE-RUN DISCLOSURE (2026-08-11, two smokes before freezing,
both MTWIN_SMOKE=1: subset restricted to (9, 13), edge to (9,),
deep skipped; NO bar, band, count or rule was moved after them --
the ONLY change between smoke 1 and smoke 2 is amendment A1
above, a typing guard, disclosed).  SMOKE 1 (14/14, 1.3 s):
W1 bit-for-bit EXACT on both frames (max |dc| = 0.0); W2
certified floors cleared (4.04e-4 / 4.27e-4 vs 3.633e-4 /
3.842e-4); W3 tent shat in band (1.228 / 1.392).  Bochner DIAG:
TENT PD (min FT/peak +5.6e-10), MT NOT PD (-7.1e-2), FEJ NOT PD
(-2.7e-2).  (a) THE FOREIGN KERNELS KILL THE WALL OUTRIGHT:
lam_min(K_MT) = -1.950/-1.935, lam_min(K_FEJ) = -0.143/-0.199 on
kz 9/13 against tent +4.0e-4/+4.3e-4 -- shat_MT ~ -6.7e3, a
SIGN FLIP, not a constant move.  (b) MT/FEJ co-block floors
REFUSED on 2/2 (tent floor/tau 2.24/2.71).  (c) the MT Gram frame
is numerically explosive (tau_gram ~ -2.1e70, floors ~ -1e67; the
r_f ratio 0.00 would have typed a spurious BAND-BETTER -> A1);
FEJ tau_gram -3.7, its negative energy is NOT edge-seated (peak
x = -0.47, WGT share 0.000); tent edge seat reproduced (Mm
-2.3e-5 < 0, WGT share 0.966, peak 0.9987).  (d) all three
controls fire under all three kernels; separation (truth > 0 vs
controls < 0) INTACT only for the tent -- MT/FEJ separation DEAD.
(e) screens NA on the 2-rung smoke.  SMOKE 2 (14/14, 1.4 s,
post-A1): identical numbers, BAND now typed
MTWINDOW-NA(GRAM-WALL-NEGATIVE) for MT and FEJ, structure flags
gain GRAM-WALL-NEGATIVE.  The frozen run must decide whether this
persists on the full subset + the 3 deep 4e6 holdout rungs.

SPEC v1 (2026-08-11, frozen + SHA-hashed = sha256 of this
docstring, printed at runtime, BEFORE the frozen run; amendment
A1 and the smoke disclosure are part of the frozen spec).

Sources (read-only): verification/v563_paper2_readouts (deployed
assembly, verbatim-swapped); rh_leverage_probe / moving_node_
second_order_probe (ladder + shat conventions); directional_
lanczos_fullframe_probe (v_sm split, A1 resolution law, deep 4e6
frames); deep_blind_holdout_probe (extension wards); wall_gram_
radau_probe / band_arithmetic_anatomy_probe (fold pipeline,
Lukacs floors, WGT band functional); the Anthropic zeta paper
(EXTERNAL-CITED: the Montgomery-Taylor cosine window shape only).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/mt_window_family_probe.py
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

SMOKE = os.environ.get("MTWIN_SMOKE", "") == "1"

SUBSET = (9, 13) if SMOKE else (9, 13, 26, 40, 60, 90, 121)
EDGE_KZ = (9,) if SMOKE else (9, 13, 26, 40)
CTRL_KZ = 9
DEEP_PICK = 0 if SMOKE else 3
TAB_EXT = 4_000_000
H_HOLD = (128, 2900)
KZ_SCAN_MAX = 400
NG_SMOOTH_MIN = 6000
NG_FACT = 8
DELTA_BAND = 1e-2
LOC_TOL = 1e-10
M0_WARD = 1e-9
CERT = {9: 3.633e-4, 13: 3.842e-4}
SHAT_BAND = (0.502, 2.185)
SHAT_RTOL = 2e-2
RATIO_BAR = 0.10
SHARE_BAR = 0.05
SCREEN_PASS = 0.30
SCREEN_RELOC = 0.70
SEED_SCRAMBLE = 1
SQRT2 = math.sqrt(2.0)
LAM_MT = math.pi / (2.0 * SQRT2)          # sqrt2 * LAM_MT = pi/2
BOCH_WMAX_D = 40.0
BOCH_NW = 4001
BOCH_NX = 20000
BANNED_IDS = ("zetazero", "nzeros", "primerange", "isprime",
              "primepi", "nextprime", "prevprime")

CHECKS = []
KILLS = []
T0 = time.time()
SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()


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


def sym(A):
    return 0.5 * (A + A.T)


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
    pos = (vals > 0) & (taus > 0) & np.isfinite(vals) \
        & np.isfinite(taus)
    if int(pos.sum()) < 3:
        return "NA", float("nan")
    _a, sl, _r2 = ols_line(np.log(taus[pos]), np.log(vals[pos]))
    if abs(sl) <= SCREEN_PASS:
        return "PASS", sl
    if sl >= SCREEN_RELOC:
        return "RELOC", sl
    return "AMBIG", sl


def mu1_of(h):
    return 4.0 * math.sin(math.pi / (2.0 * h + 1.0)) ** 2


# ---------------- the kernel family (support [-D, D], k(0) = 1)
def k_tent(x, D):
    return np.maximum(0.0, 1.0 - np.abs(x) / D)


def k_mt(x, D):
    t = np.abs(x) / D
    return np.where(t < 1.0, np.cos(SQRT2 * LAM_MT * t), 0.0)


def k_fej(x, D):
    t = np.abs(x) / D
    return np.where(t < 1.0, 0.5 * (1.0 + np.cos(math.pi * t)),
                    0.0)


KERNELS = (("TENT", k_tent), ("MT", k_mt), ("FEJ", k_fej))
KNAMES = tuple(n for n, _ in KERNELS)


def bochner_min(kf, D):
    """DIAG only: min of the numerically evaluated FT of the
    kernel over the declared omega grid, relative to its peak."""
    xx = np.linspace(-D, D, BOCH_NX + 1)
    kk = np.asarray(kf(xx, D), float)
    ww = np.linspace(0.0, BOCH_WMAX_D / D, BOCH_NW)
    ft = np.trapezoid(kk[None, :] * np.cos(ww[:, None]
                                           * xx[None, :]),
                      xx, axis=1)
    return float(ft.min() / ft.max())


# ---------------- the parallel assembly (v563 verbatim, kernel
# ---------------- swapped; bit-for-bit for kf = k_tent)
def atom_lags_kernel(alpha, M, positions, masses, kf):
    D = 2.0 * alpha / M
    c = np.zeros(M)
    for u_j, mu_j in zip(positions, masses):
        i0 = int(math.floor(u_j / D))
        for i in range(max(0, i0 - 2), min(M, i0 + 3)):
            v = kf(i * D - u_j, D)
            if v > 0.0:
                c[i] -= mu_j * 0.5 * v
        if u_j < D:
            for i in range(0, min(M, int(math.floor((D - u_j) / D))
                                  + 2)):
                v = kf(i * D + u_j, D)
                if v > 0.0:
                    c[i] -= mu_j * 0.5 * v
    return c, D


def arch_far_kernel(s, D, kf):
    s = np.asarray(s, dtype=float).reshape(-1, 1)
    out = np.zeros(s.shape[0])
    for lo, hi in ((s - D, s), (s, s + D)):
        mid = 0.5 * (lo + hi)
        half = 0.5 * (hi - lo)
        w = mid + half * core._GLX[None, :]
        val = (kf(s - w, D) * np.exp(-0.5 * w)
               / (-np.expm1(-2.0 * w)))
        out -= half[:, 0] * (val @ core._GLW)
    return out


def arch_near_kernel(s, D, kf):
    s = abs(float(s))
    k_s = float(kf(s, D))
    W = s + D
    pts = sorted({0.0, s, D - s, W})
    pts = [p for p in pts if 0.0 <= p <= W]
    tot = 0.0
    for lo, hi in zip(pts[:-1], pts[1:]):
        if hi <= lo:
            continue
        mid = 0.5 * (lo + hi)
        half = 0.5 * (hi - lo)
        w = mid + half * core._GLX
        S = 0.5 * (kf(s - w, D) + kf(s + w, D))
        integ = ((k_s * np.exp(-2.0 * w) - S * np.exp(-0.5 * w))
                 / (-np.expm1(-2.0 * w)))
        tot += half * float(np.dot(core._GLW, integ))
    return (-(core.EULER + core.LOG_PI) * k_s + 2.0 * tot
            + k_s * (-math.log1p(-math.exp(-2.0 * W))))


def arch_A_kernel(sv, D, kf):
    sv = np.abs(np.asarray(sv, dtype=float))
    out = np.empty(sv.shape[0])
    far = sv >= D
    if far.any():
        out[far] = arch_far_kernel(sv[far], D, kf)
    for i in np.nonzero(~far)[0]:
        out[i] = arch_near_kernel(sv[i], D, kf)
    return out


def arch_lags_kernel(M, D, kf):
    out = np.empty(M)
    for a in range(0, M, core.CHUNK):
        b = min(M, a + core.CHUNK)
        out[a:b] = arch_A_kernel(np.arange(a, b) * D, D, kf)
    return out


# ---------------- fold pipeline (wall_gram_radau verbatim)
def grid_density(c):
    c = np.asarray(c, float)
    a = np.concatenate([c, c[-2:0:-1]])
    d = np.fft.fft(a)
    assert float(np.max(np.abs(d.imag))) <= 1e-9 * max(
        1.0, float(np.max(np.abs(d.real))))
    return d.real


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


def edge_diag(cvec, M, h):
    """Fold pipeline + Lukacs floors + WGT/RAW band functionals."""
    d = grid_density(cvec)
    L = 2 * M - 2
    xs, ws, _uf = folded_measure(d, L, +1.0)
    ys, vs, _un = folded_measure(d, L, -1.0)
    al, be, m0, steps = lanczos_chain(xs, ws, h + 1)
    if steps < h + 1 or (len(be) and bool(np.any(be <= 0.0))):
        return dict(ok=False, steps=int(steps))
    Px = eval_chain(al, be, m0, xs, h)
    Pn = eval_chain(al, be, m0, ys, h)
    H = sym((Pn * vs[:, None]).T @ Pn)
    M0a = np.eye(h) - H
    Gp = sym((Px * ws[:, None]).T @ Px)
    M0b = Gp - H
    dev = (float(np.linalg.norm(M0a - M0b))
           / max(float(np.linalg.norm(M0a)), 1e-300))
    out = dict(ok=True, dev=dev,
               tau_g=float(np.linalg.eigvalsh(M0a)[0]))
    hm = h - 1
    Pxm, Pnm = Px[:, :hm], Pn[:, :hm]
    floors = {}
    Mm_mat = None
    for tag, gx, gy in (("x2", 1.0 - xs ** 2, 1.0 - ys ** 2),
                        ("m", 1.0 - xs, 1.0 - ys),
                        ("p", 1.0 + xs, 1.0 + ys)):
        Mloc = sym((Pxm * (ws * gx)[:, None]).T @ Pxm
                   - (Pnm * (vs * gy)[:, None]).T @ Pnm)
        if tag == "m":
            Mm_mat = Mloc
        floors[tag] = float(np.linalg.eigvalsh(Mloc)[0])
    out.update(lam_x2=floors["x2"], lam_m=floors["m"],
               lam_p=floors["p"])
    wm, Vm = np.linalg.eigh(Mm_mat)
    e = Vm[:, 0]
    q = Pnm @ e
    En = vs * (1.0 - ys) * q * q
    tot = float(En.sum())
    band = ys > 1.0 - DELTA_BAND
    out["share"] = float(En[band].sum() / tot) if tot > 0 else \
        float("nan")
    o = np.argsort(1.0 - ys)
    cum = np.cumsum(En[o]) / max(tot, 1e-300)
    i90 = min(int(np.searchsorted(cum, 0.90)), len(o) - 1)
    out["width"] = float((1.0 - ys)[o][i90])
    out["peak"] = float(ys[int(np.argmax(En))])
    out["raw"] = float(vs[band].sum() / vs.sum())
    return out


# ---------------- full-frame split (fullframe verbatim)
def householder_u(v):
    v = v / float(np.linalg.norm(v))
    e1 = np.zeros(len(v))
    e1[0] = 1.0
    w = e1 - v
    nw = float(np.linalg.norm(w))
    if nw < 1e-14:
        return None
    return w / nw


def apply_q(u, X):
    if u is None:
        return np.array(X, float, copy=True)
    if X.ndim == 1:
        return X - 2.0 * u * float(u @ X)
    return X - 2.0 * np.outer(u, u @ X)


def split_floor(K, v):
    u = householder_u(v)
    KQ = apply_q(u, apply_q(u, K).T)
    KQ = sym(KQ)
    B = np.ascontiguousarray(KQ[1:, 1:])
    return float(np.linalg.eigvalsh(B)[0])


def smooth_comb(alpha, M):
    ng = max(NG_SMOOTH_MIN, NG_FACT * M)
    ug = (np.arange(ng) + 0.5) * (2.0 * alpha / ng)
    mg = 2.0 * np.exp(ug / 2.0) * (2.0 * alpha / ng)
    return ug, mg


def lambda_eps(N):
    """Epstein x^2+5y^2 comb (port chain verbatim)."""
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


# ---------------- the deep 4e6 machinery (deep_blind_holdout /
# ---------------- fullframe conventions)
EXT = {}


def build_ext():
    lam_ext = core.von_mangoldt_table(TAB_EXT)
    NN = np.nonzero(lam_ext > 0.0)[0]
    EXT["lam"] = lam_ext
    EXT["NN"] = NN
    EXT["U"] = np.log(NN.astype(float))
    EXT["MU"] = 2.0 * lam_ext[NN] / np.sqrt(NN.astype(float))
    EXT["G"] = np.diff(EXT["U"])


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


def ext_kappa():
    nn = EXT["NN"].astype(float)
    psi = np.cumsum(EXT["lam"][EXT["NN"]])
    keep = nn >= core.KAPPA_X0
    return float(np.max(np.abs(psi[keep] - nn[keep]) / nn[keep]))


def main():
    section("PRIME.PORT.MTWINDOW.01 -- the Montgomery-Taylor "
            "window family test (EXPLORATION ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s" % SPEC_SHA)
    print("    smoke mode: %s" % SMOKE)
    print("    NO RH claim; no marker moves; nothing outside "
          "experiments/.")
    print("\nS0 -- firewall")
    check("S0.1 AST firewall clean (banned ids %s)"
          % (BANNED_IDS,), not ast_scan(BANNED_IDS), kill="K5")

    # DIAG: Bochner PD-ness of the kernel family (recorded, no bar)
    dprint = []
    for name, kf in KERNELS:
        bm = bochner_min(kf, 1.0)
        dprint.append("%s %+.3e" % (name, bm))
    print("    DIAG Bochner min FT / peak FT on the declared "
          "grid: %s" % ", ".join(dprint))

    # ------------------------------------------------------ frames
    section("W -- frames + the master baseline ward")
    frames = []
    for kz in SUBSET:
        rr = core.build_window(kz)
        frames.append(dict(src="dep", kz=kz, alpha=float(rr["alpha"]),
                           M=rr["M"], D=rr["D"], h=rr["h"],
                           uu=np.asarray(rr["uu"], float),
                           mm=2.0 * np.asarray(rr["lam"], float)))
    if DEEP_PICK > 0:
        build_ext()
        ok_tab = bool(np.array_equal(
            EXT["lam"][:core.ATOM_MAX + 1], core.LAM_TAB))
        ok_pref = (bool(np.array_equal(EXT["NN"][:len(core._NN)],
                                       core._NN))
                   and bool(np.array_equal(EXT["U"][:len(core.U_ALL)],
                                           core.U_ALL))
                   and bool(np.array_equal(EXT["MU"][:len(core.MU_ALL)],
                                           core.MU_ALL)))
        kap = ext_kappa()
        new_kz = []
        for kz in range(2, min(KZ_SCAN_MAX, len(EXT["NN"]) - 2)):
            alpha = float(EXT["U"][kz])
            X = math.exp(2.0 * alpha)
            if X > TAB_EXT:
                break
            if X <= core.ATOM_MAX:
                continue
            _a, _M, h, _ka = ext_frame(kz)
            if H_HOLD[0] <= h <= H_HOLD[1]:
                new_kz.append(kz)
        order = sorted(new_kz, key=lambda k: (ext_frame(k)[2], k))
        check("W4 deep fidelity: table prefix bitwise %s, arrays "
              "bitwise %s, extended kappa %.6f <= %.6f + 1e-6, "
              "%d new rungs found (>= %d)"
              % (ok_tab, ok_pref, kap, core.KAPPA_REF,
                 len(order), DEEP_PICK),
              ok_tab and ok_pref
              and kap <= core.KAPPA_REF + 1e-6
              and len(order) >= DEEP_PICK, kill="K3")
        for kz in order[:DEEP_PICK]:
            alpha, Mz, hz, ka = ext_frame(kz)
            frames.append(dict(src="deep", kz=kz, alpha=alpha,
                               M=Mz, D=2.0 * alpha / Mz, h=hz,
                               uu=EXT["U"][:ka].copy(),
                               mm=EXT["MU"][:ka].copy()))

    # W1: master ward -- the parallel TENT assembly must equal the
    # deployed lag vector bit-for-bit on every frame; the per-frame
    # per-kernel lag vectors + arch layers are built and cached here
    max_dc = 0.0
    for fr in frames:
        c_dep = (np.asarray(core.arch_lags(fr["M"], fr["D"]), float)
                 + np.asarray(core.atom_lags_at(
                     fr["alpha"], fr["M"], fr["uu"], fr["mm"])[0],
                     float))
        fr["c"], fr["car"] = {}, {}
        for name, kf in KERNELS:
            car = arch_lags_kernel(fr["M"], fr["D"], kf)
            cat, _ = atom_lags_kernel(fr["alpha"], fr["M"],
                                      fr["uu"], fr["mm"], kf)
            fr["car"][name] = car
            fr["c"][name] = car + cat
        eq = bool(np.array_equal(fr["c"]["TENT"], c_dep))
        if not eq:
            max_dc = max(max_dc, float(np.max(np.abs(
                fr["c"]["TENT"] - c_dep))))
        fr["w1"] = eq
    check("W1 MASTER WARD: parallel TENT assembly == deployed lag "
          "vector np.array_equal (bit-for-bit) on all %d frames "
          "(max |dc| where unequal: %.1e)"
          % (len(frames), max_dc),
          all(fr["w1"] for fr in frames), kill="K1")
    if KILLS:
        return finish({})
    print("    frames: %s"
          % ", ".join("%s-kz%d(h=%d)" % (fr["src"], fr["kz"],
                                         fr["h"]) for fr in frames))

    # ------------------------------------------------------ E1
    section("E1 -- (a) HALFGAP: the wall + shat census per kernel")
    for fr in frames:
        fr["m"], fr["shat"] = {}, {}
        for name in KNAMES:
            K = core.odd_toeplitz(fr["c"][name], fr["M"])
            m = float(np.linalg.eigvalsh(K)[0])
            fr["m"][name] = m
            fr["shat"][name] = m / mu1_of(fr["h"])
    print("      src  kz    h  " + "".join(
        "%14s" % ("lam_" + n) for n in KNAMES) + "".join(
        "%11s" % ("shat_" + n) for n in KNAMES))
    for fr in frames:
        print("     %4s %4d %5d " % (fr["src"], fr["kz"], fr["h"])
              + "".join("%+14.4e" % fr["m"][n] for n in KNAMES)
              + "".join("%+11.3f" % fr["shat"][n] for n in KNAMES))
    dep = [fr for fr in frames if fr["src"] == "dep"]
    check("W2 v884 certified floors: tent lam_min at kz 9/13 = "
          "%.4e/%.4e >= %.3e/%.3e"
          % (dep[0]["m"]["TENT"], dep[1]["m"]["TENT"],
             CERT[9], CERT[13]),
          dep[0]["m"]["TENT"] >= CERT[9]
          and dep[1]["m"]["TENT"] >= CERT[13], kill="K2")
    sh_t = [fr["shat"]["TENT"] for fr in dep]
    check("W3 tent subset shat in the 67-rung band [%.3f, %.3f] "
          "(rtol %.0e): measured %.3f..%.3f"
          % (SHAT_BAND[0], SHAT_BAND[1], SHAT_RTOL,
             min(sh_t), max(sh_t)),
          min(sh_t) >= SHAT_BAND[0] * (1.0 - SHAT_RTOL)
          and max(sh_t) <= SHAT_BAND[1] * (1.0 + SHAT_RTOL),
          kill="K2")
    hg = {}
    for name in KNAMES:
        sh = np.array([fr["shat"][name] for fr in frames])
        mm_ = np.array([fr["m"][name] for fr in frames])
        hg[name] = dict(npos=int(np.sum(mm_ > 0.0)),
                        nbase=int(np.sum(sh >= 0.5)),
                        mn=float(sh.min()), md=float(np.median(sh)),
                        mx=float(sh.max()))
        print("    %4s: wall > 0 on %d/%d, base-halfgap shat >= "
              "1/2 on %d/%d, shat min/med/max %+.3f/%+.3f/%+.3f"
              % (name, hg[name]["npos"], len(frames),
                 hg[name]["nbase"], len(frames), hg[name]["mn"],
                 hg[name]["md"], hg[name]["mx"]))
    check("E1 typed: tent HALFGAP-BASE-%s; MT %s; FEJ %s "
          "(measurement, never a kill)"
          % tuple(("STABLE" if hg[n]["nbase"] == len(frames)
                   else "VIOLATED(%d/%d)" % (hg[n]["nbase"],
                                             len(frames)))
                  for n in KNAMES), True)

    # ------------------------------------------------------ E2
    section("E2 -- (b) B-FLOOR: full-frame co-block along the "
            "same-kernel smooth direction")
    print("    (tangent-Schur core rebuild declared TOO DEEP for "
          "a foreign window; wall-level co-block used, fullframe "
          "conventions.  Cited context: core floor min 0.679 abs; "
          "full-frame deployed floor/tau ~ 2.1..5.2, med ~ 2.77.)")
    for fr in frames:
        ug, mg = smooth_comb(fr["alpha"], fr["M"])
        fr["lam_sm"], fr["floor"] = {}, {}
        for name, kf in KERNELS:
            cat_s, _ = atom_lags_kernel(fr["alpha"], fr["M"], ug,
                                        mg, kf)
            Ksm = core.odd_toeplitz(fr["car"][name] + cat_s,
                                    fr["M"])
            wsm, Vsm = np.linalg.eigh(Ksm)
            fr["lam_sm"][name] = float(wsm[0])
            v_sm = Vsm[:, 0]
            K = core.odd_toeplitz(fr["c"][name], fr["M"])
            fr["floor"][name] = split_floor(K, v_sm)
            del K, Ksm, Vsm
    print("      src  kz    h  " + "".join(
        "%12s" % ("smK_" + n) for n in KNAMES) + "".join(
        "%12s" % ("flr_" + n) for n in KNAMES))
    for fr in frames:
        print("     %4s %4d %5d " % (fr["src"], fr["kz"], fr["h"])
              + "".join("%+12.3e" % fr["lam_sm"][n] for n in KNAMES)
              + "".join("%+12.3e" % fr["floor"][n]
                        for n in KNAMES))
    bf = {}
    for name in KNAMES:
        ft, nref = [], 0
        for fr in frames:
            tau = fr["m"][name]
            if tau <= 0.0 or fr["floor"][name] <= 0.0:
                nref += 1
            else:
                ft.append(fr["floor"][name] / tau)
        bf[name] = dict(nref=nref,
                        med=(float(np.median(ft)) if ft
                             else float("nan")),
                        mn=(float(min(ft)) if ft else float("nan")),
                        mx=(float(max(ft)) if ft else float("nan")),
                        ft=ft)
        print("    %4s: refusals %d/%d; floor/tau min/med/max "
              "%.3f/%.3f/%.3f"
              % (name, nref, len(frames), bf[name]["mn"],
                 bf[name]["med"], bf[name]["mx"]))
    check("E2 typed: co-block floor census recorded per kernel "
          "(measurement, never a kill)", True)

    # ------------------------------------------------------ E3
    section("E3 -- (c) x = +1 EDGE/BAND: Lukacs floors + band "
            "energy per kernel")
    edge = {n: [] for n in KNAMES}
    dev_max = 0.0
    for fr in frames:
        if fr["src"] != "dep" or fr["kz"] not in EDGE_KZ:
            continue
        for name in KNAMES:
            r = edge_diag(fr["c"][name], fr["M"], fr["h"])
            r["kz"], r["h"] = fr["kz"], fr["h"]
            edge[name].append(r)
            if r["ok"]:
                dev_max = max(dev_max, r["dev"])
                print("    %4s kz %3d h %4d: tau_g %+.3e | floors "
                      "x2/m/p %+.2e/%+.2e/%+.2e | WGT share %.3f "
                      "width %.2e peak %.4f | RAW share %.3f"
                      % (name, r["kz"], r["h"], r["tau_g"],
                         r["lam_x2"], r["lam_m"], r["lam_p"],
                         r["share"], r["width"], r["peak"],
                         r["raw"]))
            else:
                print("    %4s kz %3d h %4d: CHAIN-INCOMPLETE "
                      "(steps %d < h + 1 = %d) -- the foreign "
                      "fold is not chain-constructible"
                      % (name, r["kz"], r["h"], r["steps"],
                         r["h"] + 1))
    usable = [r for rs in edge.values() for r in rs if r["ok"]]
    check("W5 WARD assembly identity: M0 two-route rel dev "
          "%.2e <= %.0e on all %d usable edge builds"
          % (dev_max, M0_WARD, len(usable)),
          all(r["dev"] <= M0_WARD for r in usable), kill="K5")
    tent_edge = [r for r in edge["TENT"] if r["ok"]]
    tent_sh = [r["share"] for r in tent_edge]
    check("W6 WARD tent edge seat reproduced: Mm fails (lam_m < "
          "0) on %d/%d tent edge rungs and med WGT share %.3f >= "
          "0.90 (round-60 seat 0.942)"
          % (sum(1 for r in tent_edge if r["lam_m"] < 0.0),
             len(tent_edge),
             float(np.median(tent_sh)) if tent_sh else float("nan")),
          len(tent_edge) == len(EDGE_KZ)
          and all(r["lam_m"] < 0.0 for r in tent_edge)
          and float(np.median(tent_sh)) >= 0.90, kill="K2")
    check("E3 typed: edge/band census recorded per kernel "
          "(measurement, never a kill)", True)

    # ------------------------------------------------------ E4
    section("E4 -- (d) TRUTH-SPECIFICITY: the three controls per "
            "kernel at kz = %d" % CTRL_KZ)
    fr9 = next(fr for fr in frames
               if fr["src"] == "dep" and fr["kz"] == CTRL_KZ)
    rr_s = core.build_window(CTRL_KZ, scramble_seed=SEED_SCRAMBLE)
    uu_s = np.asarray(rr_s["uu"], float)
    mm_s = 2.0 * np.asarray(rr_s["lam"], float)
    N_E = int(math.floor(math.exp(2.0 * fr9["alpha"]))) + 1
    lamE = lambda_eps(N_E)
    nnE = np.nonzero(np.abs(lamE) > 1e-12)[0]
    uu_e = np.log(nnE.astype(float))
    mm_e = 2.0 * lamE[nnE] / np.sqrt(nnE.astype(float))
    spec = {}
    for name, kf in KERNELS:
        vals = {"smooth": fr9["lam_sm"][name]}
        for tag, (uc, mc) in (("scramble", (uu_s, mm_s)),
                              ("epstein", (uu_e, mm_e))):
            cat_c, _ = atom_lags_kernel(fr9["alpha"], fr9["M"],
                                        uc, mc, kf)
            vals[tag] = float(np.linalg.eigvalsh(
                core.odd_toeplitz(fr9["car"][name] + cat_c,
                                  fr9["M"]))[0])
        fire = all(v < 0.0 for v in vals.values())
        sep = fire and fr9["m"][name] > 0.0
        spec[name] = dict(vals=vals, fire=fire, sep=sep)
        print("    %4s: truth %+.3e | smooth %+.3e scramble "
              "%+.3e epstein %+.3e -> controls %s, separation %s"
              % (name, fr9["m"][name], vals["smooth"],
                 vals["scramble"], vals["epstein"],
                 "FIRE" if fire else "SILENT",
                 "INTACT" if sep else "DEAD"))
    check("W7 tent controls must all fire (CONTROL-DEAD kill) and "
          "tent separation intact",
          spec["TENT"]["fire"] and spec["TENT"]["sep"], kill="K4")
    check("E4 typed: MT spec %s / separation %s; FEJ spec %s / "
          "separation %s (a kernel with silent controls is "
          "worthless -- the Weyl lesson)"
          % ("FIRE" if spec["MT"]["fire"] else "SILENT",
             "INTACT" if spec["MT"]["sep"] else "DEAD",
             "FIRE" if spec["FEJ"]["fire"] else "SILENT",
             "INTACT" if spec["FEJ"]["sep"] else "DEAD"), True)

    # ------------------------------------------------------ E5
    section("E5 -- (e) tau-screens on all new margins")
    scr = {}
    for name in KNAMES:
        taus = np.array([fr["m"][name] for fr in frames])
        sh = np.array([fr["shat"][name] for fr in frames])
        fl = np.array([fr["floor"][name] / fr["m"][name]
                       if fr["m"][name] > 0 else float("nan")
                       for fr in frames])
        el = [(abs(r["lam_m"]) / max(abs(r["tau_g"]), 1e-300),
               abs(r["tau_g"])) for r in edge[name] if r["ok"]]
        s1 = screen(sh, taus)
        s2 = screen(fl, taus)
        s3 = (screen([e[0] for e in el], [e[1] for e in el])
              if el else ("NA", float("nan")))
        scr[name] = (s1, s2, s3)
        print("    %4s: shat %s(%+.3f) | floor/tau %s(%+.3f) | "
              "|lam_m|/|tau_g| %s(%+.3f)"
              % (name, s1[0], s1[1], s2[0], s2[1], s3[0], s3[1]))
    check("E5 typed: tau-screens recorded (measurement, never a "
          "kill)", True)

    # ------------------------------------------------------ V
    section("V -- per-metric verdicts + the structural answer")
    n_fr = len(frames)
    verd = {}
    for name in ("MT", "FEJ"):
        v = {}
        # HALFGAP
        viol = (hg[name]["npos"] < n_fr
                or (hg[name]["nbase"] < n_fr
                    and hg["TENT"]["nbase"] == n_fr))
        if viol:
            v["HALFGAP"] = "MTWINDOW-WORSE"
        elif hg[name]["mn"] >= (1.0 + RATIO_BAR) * hg["TENT"]["mn"]:
            v["HALFGAP"] = "MTWINDOW-BETTER"
        else:
            v["HALFGAP"] = "MTWINDOW-NEUTRAL"
        # BFLOOR
        if (bf[name]["nref"] > 0
                or not np.isfinite(bf[name]["med"])
                or bf[name]["med"] < (1.0 - RATIO_BAR)
                * bf["TENT"]["med"]):
            v["BFLOOR"] = "MTWINDOW-WORSE"
        elif bf[name]["med"] >= (1.0 + RATIO_BAR) * bf["TENT"]["med"]:
            v["BFLOOR"] = "MTWINDOW-BETTER"
        else:
            v["BFLOOR"] = "MTWINDOW-NEUTRAL"
        # BAND
        ok_e = [r for r in edge[name] if r["ok"]]
        if not ok_e:
            v["BAND"] = "MTWINDOW-NA(CHAIN-INCOMPLETE)"
        elif any(r["tau_g"] <= 0.0 for r in ok_e):
            v["BAND"] = "MTWINDOW-NA(GRAM-WALL-NEGATIVE)"
        elif all(min(r["lam_x2"], r["lam_m"], r["lam_p"])
                 >= -LOC_TOL for r in ok_e):
            v["BAND"] = "MTWINDOW-BETTER(BAND-CERTIFIED)"
        else:
            r_f = (float(np.median(
                [abs(r["lam_m"]) / max(abs(r["tau_g"]), 1e-300)
                 for r in ok_e]))
                / float(np.median(
                    [abs(r["lam_m"]) / max(abs(r["tau_g"]), 1e-300)
                     for r in tent_edge])))
            d_s = (float(np.median([r["share"] for r in ok_e]))
                   - float(np.median(tent_sh)))
            better = ((r_f <= 1.0 - RATIO_BAR or d_s <= -SHARE_BAR)
                      and not (r_f >= 1.0 + RATIO_BAR
                               or d_s >= SHARE_BAR))
            worse = ((r_f >= 1.0 + RATIO_BAR or d_s >= SHARE_BAR)
                     and not (r_f <= 1.0 - RATIO_BAR
                              or d_s <= -SHARE_BAR))
            v["BAND"] = ("MTWINDOW-BETTER" if better else
                         "MTWINDOW-WORSE" if worse else
                         "MTWINDOW-NEUTRAL")
            v["BAND"] += "(r_f=%.2f,d_s=%+.3f)" % (r_f, d_s)
        # SPEC
        v["SPEC"] = ("MTWINDOW-WORSE(SPEC-DEAD)"
                     if not spec[name]["fire"]
                     else "MTWINDOW-NEUTRAL")
        # structure flags vs tent
        flags = []
        if hg[name]["npos"] < n_fr <= hg["TENT"]["npos"]:
            flags.append("WALL-SIGN-FLIP(%d/%d)"
                         % (n_fr - hg[name]["npos"], n_fr))
        if hg[name]["nbase"] < n_fr <= hg["TENT"]["nbase"]:
            flags.append("HALFGAP-BASE-VIOLATED")
        if spec[name]["fire"] != spec["TENT"]["fire"]:
            flags.append("CONTROL-SILENCE")
        if not spec[name]["sep"] and spec["TENT"]["sep"]:
            flags.append("SEPARATION-DEAD")
        if ok_e and all(min(r["lam_x2"], r["lam_m"], r["lam_p"])
                        >= -LOC_TOL for r in ok_e):
            flags.append("LUKACS-CERTIFIED-FLIP")
        if ok_e and any(r["tau_g"] <= 0.0 for r in ok_e):
            flags.append("GRAM-WALL-NEGATIVE")
        if not ok_e and tent_edge:
            flags.append("GRAM-CHAIN-LOST")
        if bf[name]["nref"] > 0 and bf["TENT"]["nref"] == 0:
            flags.append("BFLOOR-REFUSAL")
        v["FLAGS"] = flags
        verd[name] = v
    for name in ("MT", "FEJ"):
        v = verd[name]
        print("    %4s: HALFGAP %s | BFLOOR %s | BAND %s | SPEC %s"
              % (name, v["HALFGAP"], v["BFLOOR"], v["BAND"],
                 v["SPEC"]))
        print("          structure flags: %s"
              % (", ".join(v["FLAGS"]) if v["FLAGS"] else "none"))
    struct = {n: bool(verd[n]["FLAGS"]) for n in ("MT", "FEJ")}
    if any(struct.values()):
        answer = ("STRUCTURE-CHANGED(%s)"
                  % "; ".join("%s: %s" % (n, ",".join(
                      verd[n]["FLAGS"]))
                      for n in ("MT", "FEJ") if struct[n]))
    else:
        answer = ("CONSTANTS-ONLY(shat-min ratios MT %.3f, FEJ "
                  "%.3f; floor/tau med ratios MT %.3f, FEJ %.3f)"
                  % (hg["MT"]["mn"] / hg["TENT"]["mn"],
                     hg["FEJ"]["mn"] / hg["TENT"]["mn"],
                     bf["MT"]["med"] / bf["TENT"]["med"],
                     bf["FEJ"]["med"] / bf["TENT"]["med"]))
    check("V typed: the structural answer is %s" % answer, True)
    return finish(dict(verd=verd, answer=answer))


def finish(labels):
    section("FROZEN VERDICT")
    n_pass = sum(1 for _n, okk in CHECKS if okk)
    n_tot = len(CHECKS)
    if KILLS:
        VD = {"K1": "BASELINE-BROKEN", "K2": "WALL-BROKEN",
              "K3": "DEEP-BROKEN", "K4": "CONTROL-DEAD",
              "K5": "WARD-BROKEN"}[KILLS[0]]
        print("\n  VERDICT: %s" % VD)
    else:
        v = labels["verd"]
        VD = ("MTWINDOW-FAMILY-MEASURED / MT[%s|%s|%s|%s] / "
              "FEJ[%s|%s|%s|%s] / %s"
              % (v["MT"]["HALFGAP"], v["MT"]["BFLOOR"],
                 v["MT"]["BAND"], v["MT"]["SPEC"],
                 v["FEJ"]["HALFGAP"], v["FEJ"]["BFLOOR"],
                 v["FEJ"]["BAND"], v["FEJ"]["SPEC"],
                 labels["answer"]))
        print("\n  VERDICT: %s" % VD)
    ok_norh = ("RH-TRUE" not in VD and "RH-FALSE" not in VD)
    check("C-NO-RH: the verdict asserts nothing about the truth "
          "of RH in either direction", ok_norh, kill="K5")
    n_pass = sum(1 for _n, okk in CHECKS if okk)
    n_tot = len(CHECKS)
    print("""
  HONEST FRAME (as frozen): a FOREIGN window family is measured
  against the deployed tent architecture on finite rungs.  The
  deployed baseline is reproduced bit-for-bit through the same
  parallel assembly (the master ward); every foreign number is a
  surface measurement, typed BETTER/NEUTRAL/WORSE per metric
  under the frozen bars.  NO RH claim in either direction; no
  marker moves; nothing outside experiments/.""")
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed"
          % (time.time() - T0, n_tot, n_tot - n_pass))
    return 0 if n_pass == n_tot else 1


if __name__ == "__main__":
    raise SystemExit(main())
