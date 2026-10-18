"""PRIME.DETECTORINVERSION.01 -- the off-line-zero detector INVERTED
into an effective zero-free-region extractor (EXPLORATION ONLY).

THE LATERAL MOVE (user-authorized, 2026-08-06): stop trying to prove
the sector floor; extract what the VERIFIED floor already proves.
Every verified rung "lambda_min(T_X) = m_X > 0" excludes the
computable region of (delta, gamma) whose off-line zero quadruple
would have forced the form negative at that depth.

THE CONDITIONAL THEOREM (frozen).  The deployed GL1 tower (v791/
v793/v794 four-sector system; D = 1/64, T_X = toeplitz(c[:M]),
X = M D) satisfies the tent-read Guinand identity
    c[k]  =  sum_{gamma_r > 0} ell_{gamma_r}[k],
    ell_g[k] = 2 a(g) cos(g k D),  a(g) = D csinc(g D / 2)^2,
(pole and archimedean terms absorbed EXACTLY -- calibration pilot
2026-08-06: residual = the truncation tail of the cached 2500-zero
sum, 0.096 at lag 0 falling to ~8e-4; the pair-layer weight a(g)
EQUALS the deployed zero-side weight wg = D csinc(gD/2)^2 of v692
T_pair -- cross-anchor).  Each on-line pair layer is EXACTLY rank-2
PSD (W0 ward below).  HYPOTHESIS H(gamma, delta): the true zero
multiset contains the quadruple {1/2 +- delta +- i gamma} and NO
OTHER off-line zero in the visible band (single-quadruple dominance
-- honesty gate (a); the v694 masked-pair counterexample is cited as
the known limit of this hypothesis class).  Then
    T_X - Q_{gamma,delta}  =  sum_{other zeros} (rank-2 PSD)  >= 0,
    Q lags = tent reads of 4 cosh(delta u) cos(gamma u)
    (v765 RT3 convention: kernel Re[e^{z1 t}/z1^2 + e^{z2 t}/z2^2]''
     with AMP_Z = 2 == the full quadruple: exact anchor equivalence).
CONTRAPOSITIVE: lambda_min(T_X - Q) < -EXC_BUD  ==>  H(gamma, delta)
is FALSE -- the quadruple is excluded by the verified rung.
Superadditivity drops the on-line rest SAFELY; no counting bound and
no margin subtraction is needed (m_X > 0 is the qualitative input;
its magnitude shifts the boundary only weakly -- sensitivity row).

TASK STRUCTURE:
 S1 TOWER REBUILD + ANCHORS: rungs M = 256 / 640 / 1176 (X = 4 / 10
    / 18.375; deep rung from the deployed 1e8 sieve as v794);
    anchors 5.29e-5 / 1.18e-5 / 3.9e-6 (v791/v793/v794; v780 deep
    anchor 3.882e-6), rel tol 2e-2.  Precision budget typed (gate
    b): margins are float; EXC_BUD = 100 eps (||T||_2 + ||Q||_est).
 S2 CALIBRATION WARDS: W0 the pair layer == 2 a cos(g k D) exactly
    (<= 1e-12); WQ the quadruple lag reads == numerical tent
    quadrature (rel <= 1e-8); W2 the smooth-packet identity
    |x^T T x - sum_cached 2 a |X(g)|^2| <= 3 x TAILBUD(x) with the
    [A2]-integrated tail budget (Hasanalizade-Shen-Wong 2022) and
    the alias-period-exact max|X|^2 (X(g) is 2 pi / D periodic).
 S3 THE EXCLUSION MAP: grid gamma in geomspace(2, 190, 36) (Nyquist
    pi/D = 201.06), delta in linspace(1/60, 1/2, 30); excluded iff
    the SAFE rank-4 subspace bound (span e^{+-delta j D} cos/sin
    (gamma j D); contains the v688 matched filter cos(w gamma)
    sinh(w delta)) gives lambda_min(T - Q) < -EXC_BUD.  Subspace
    min >= full min: the criterion can only UNDER-exclude (safe).
    Boundary delta_min(gamma) per rung + union; full-eig subsample
    ward; monotone-in-X census (deeper rung must not lose more than
    MONO_TOL = 2% of a shallower rung's exclusions on the grid).
 S4 THE SCALING LAW: Xi_eff(gamma) = X delta_min(gamma) census vs
    the v688/v694 calibrated detection threshold Xi_up = 1.9735
    (CITED anchor, frame-A family); X*(delta) = Xi_med/delta with
    benchmark depth table (comb cap e^{X*}); the honest reach
    statement: NEW territory needs gamma > 3e12 ([A1] Platt-Trudgian
    2021), i.e. D < pi/3e12 and M > 1e12 X lags -- printed plainly.
 S5 KNOWN-TERRITORY COMPARISON (gate c, typed plainly): everything
    visible (gamma <= 190) is INSIDE the numerically verified strip
    [A1] -- the extracted region is NOT NEW; in-band comparison vs
    the classical asymptotic region beta <= 1 - 1/(R log|gamma|)
    (R = 5.558691, Mossinghoff-Trudgian-Yang 2024) reported.
CONTROLS: C1a (must-fire) inject Q at interior points (delta = 2
 delta_min capped at 1/2): lambda_min(T + Q) < -EXC_BUD (the RT3-
 style margin break -- the calibration ward); C1b exterior points
 (delta = delta_min/4): NO break (lambda_min(T + Q) > -EXC_BUD).
VERDICT (frozen): DETECTOR-INVERTED (anchors + wards + nonempty
 maps on >= 2 rungs + monotone census + C1a/C1b fire) /
 INVERSION-PARTIAL / INVERSION-INVALID (a ward or C1a fails).

FIREWALL: v563/v755 read-only; NO zetazero()/nzeros() calls (AST-
checked); the cached RvM-checked ordinate list (v684 provenance,
n = 2500) is read for the CALIBRATION WARD and the on-line side
only -- the hypothesised zero enters every exclusion statement as a
HYPOTHESIS whose consequence is computed, never as data.  No RNG.
Nothing outside experiments/ touched.  NO RH claim -- the output is
a conditional-theorem-shaped exclusion statement with typed caveats.

DECLARED CORRECTIONS (run 1 -> run 2, 2026-08-06; the frozen verdict
enum and the T - Q criterion are UNCHANGED):
 (1) WQ ward normalization bug: the deployed lag convention is
     D x (unit-tent read) (ratio exactly 1/64 = D, verified); run 1
     compared against the unit-tent read.  Ward fixed; the pilot
     identity and W0 already certified the internal consistency.
 (2) TWO-ZONE DISCOVERY (run 1): the T - Q exclusion is STRICTLY
     STRONGER than margin-break detection.  At small delta the
     criterion excludes through the window's gamma-RESOLUTION of the
     actual zero pattern (a quadruple parked at an unoccupied or
     singly-occupied ordinate is inconsistent with the measured comb
     regardless of amplification), and there an injected quadruple
     does NOT break the margin (Q ~= 2 x PSD pair layer).  Run 1's
     controls presumed exclusion <=> margin break and correctly
     FAILED.  Run 2 adds the margin-break boundary delta_mb(gamma)
     (subspace-certified lambda_min(T + Q) < 0 -- the detector-
     native object): the controls and the Xi scaling law bind to
     delta_mb; the raw T - Q region is reported as the stronger
     interpolation-zone exclusion with its own honesty typing.
 (3) EXC_BUD upgraded from pure float noise to EXC_BUD = 1e-8 +
     100 eps (||T|| + ||Q||): the zero-sum truncation tail needs NO
     budget (the tail zeros are themselves an on-line sum, dropped
     on the safe side); what remains is the systematic read-
     convention error of the deployed continuum quadrature, typed
     as < 1e-8 per unit-norm witness (anchored by the pilot lag
     residual being pure tail, the W2 packet numbers, and the
     4-digit margin-anchor agreement).  Exclusion magnitudes are
     printed so the budget's headroom is visible.
 (4) C1b redefined (run 2 -> run 3): run 2 injected at delta_mb/4
     and found the margin STILL breaks -- correct behaviour, wrongly
     gated: the subspace-certified boundary delta_mb UNDER-detects
     (safe side), so the true full-spectrum break boundary lies
     BELOW it and 'outside delta_mb' is not outside the true break
     region.  C1b now wards NO-FALSE-EXCLUSION (every claimed
     margin-break point is confirmed by the full eigensolve) and
     MEASURES the under-detection factor delta_mb/delta_full at
     sampled gammas (reported).  'Outside the full boundary must
     not break' is tautological on the shared grid and is typed so.
"""
import ast
import json
import math
import os
import sys
import time

import numpy as np
import scipy.linalg as sla

_here = os.path.dirname(os.path.abspath(__file__))
for _cand in (os.path.join(_here, "..", "..", "verification"), _here):
    if os.path.exists(os.path.join(_cand, "v563_paper2_readouts.py")):
        sys.path.insert(0, os.path.abspath(_cand))
        break

import v563_paper2_readouts as core            # noqa: E402 (READ-ONLY)
import v755_simpler_schur_recursion as srp     # noqa: E402 (READ-ONLY)

T0 = time.time()
FAILS = []
N_CHK = 0

# ------------------------------------------------- frozen bars / constants
DGRID = 1.0 / 64.0
RUNGS = ((256, 5.29e-5), (640, 1.18e-5), (1176, 3.9e-6))
V780_DEEP = 3.882e-6
ANCH_REL = 2.0e-2
ATOM_MAX_DEEP = 100000000
GAMMAS_GRID = np.geomspace(2.0, 190.0, 36)
DELTAS_GRID = np.linspace(1.0 / 60.0, 0.5, 30)
W0_BAR = 1.0e-12
WQ_BAR = 1.0e-8
W2_SLACK = 3.0
MONO_TOL = 0.02
XI_UP_CITED = 1.9735          # v688/v694 detection threshold (frame-A)
R_CLASSICAL = 5.558691        # Mossinghoff-Trudgian-Yang 2024
T_RH_CITED = 3.0e12           # [A1] Platt-Trudgian 2021
# [A2] Hasanalizade-Shen-Wong 2022: |N(T) - RvM| <= A2A logT +
A2A, A2B, A2C = 0.1038, 0.2573, 9.3675
N_SUB_WARD = 12               # full-eig subsample per rung
W2_PACKETS = (30.0, 50.0, 80.0)
SENS_FACTOR = 100.0           # margin sensitivity row (report only)
IDENT_BUD = 1.0e-8            # systematic read-convention allowance
N_ONZERO = 30                 # on-ordinate gamma family (report)


def check(name, ok, detail=""):
    global N_CHK
    N_CHK += 1
    if not ok:
        FAILS.append(name.split()[0])
    print("[%s] %s%s" % ("PASS" if ok else "FAIL", name,
                         (": " + detail) if detail else ""))


def ast_zero_firewall(src_path):
    with open(src_path, "r", encoding="utf-8") as fh:
        tree = ast.parse(fh.read())
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            f = node.func
            nm = f.attr if isinstance(f, ast.Attribute) else (
                f.id if isinstance(f, ast.Name) else "")
            if nm in ("zetazero", "nzeros", "find_zeros"):
                return False
    return True


def pair_lags(M, gamma):
    """One on-line conjugate pair {1/2 +- i gamma}: tent reads of
    2 cos(gamma u) (second-difference convention, v765)."""
    t = np.abs(np.arange(-1, M + 1)) * DGRID
    g = -2.0 * np.cos(gamma * t) / gamma ** 2
    return (g[:-2] - 2.0 * g[1:-1] + g[2:]) / DGRID


def quad_lags(M, gamma, delta):
    """Full off-line quadruple {1/2 +- delta +- i gamma}: tent reads
    of 4 cosh(delta u) cos(gamma u).  v765 RT3 kernel with AMP_Z = 2
    == this convention (anchor equivalence)."""
    z1, z2 = complex(delta, gamma), complex(-delta, gamma)
    t = np.abs(np.arange(-1, M + 1)) * DGRID
    g = 2.0 * (np.exp(z1 * t) / z1 ** 2 + np.exp(z2 * t) / z2 ** 2).real
    return (g[:-2] - 2.0 * g[1:-1] + g[2:]) / DGRID


def a_weight(g):
    x = g * DGRID / 2.0
    return DGRID * (np.sin(x) / x) ** 2


def subspace_lam_min(TQ, M, gamma, delta):
    """SAFE lower-bounding test: lambda_min of T - Q restricted to
    the rank-4 exponential family (>= the full minimum)."""
    jj = np.arange(M) * DGRID
    B = np.stack([np.exp(delta * jj) * np.cos(gamma * jj),
                  np.exp(delta * jj) * np.sin(gamma * jj),
                  np.exp(-delta * jj) * np.cos(gamma * jj),
                  np.exp(-delta * jj) * np.sin(gamma * jj)], axis=1)
    Qb, _ = np.linalg.qr(B)
    S4 = Qb.T @ (TQ @ Qb)
    return float(np.linalg.eigvalsh(0.5 * (S4 + S4.T))[0])


def n_upper(t):
    """[A2] upper bound for N(t)."""
    return (t / (2.0 * math.pi) * math.log(t / (2.0 * math.pi * math.e))
            + A2A * math.log(t) + A2B * math.log(math.log(t)) + A2C)


def tail_budget(x, gamma_top, n_cached):
    """Safe bound for the zero-sum truncation in x^T T x: pairs
    beyond the cache contribute <= max_band |X|^2 * int 2a dN, with
    2a(t) <= 8/(D t^2) and dN via [A2] (Stieltjes-safe by parts).
    X(g) is exactly 2 pi / D periodic -> band max is a global max."""
    jj = np.arange(len(x)) * DGRID
    band = np.linspace(0.0, 2.0 * math.pi / DGRID, 4096)
    Xb = np.abs(np.exp(1j * np.outer(band, jj)) @ x)
    x2max = float(np.max(Xb) ** 2)
    f0 = 8.0 / (DGRID * gamma_top ** 2)
    tt = np.geomspace(gamma_top, 1.0e9, 4000)
    integ = np.trapezoid(
        16.0 / (DGRID * tt ** 3)
        * np.array([n_upper(t) - n_cached for t in tt]), tt)
    return x2max * (integ + f0 * 0.0 + 16.0 / (DGRID * 1.0e9)
                    * n_upper(1.0e9) / 2.0)


def run():
    global N_CHK, FAILS
    N_CHK = 0
    FAILS = []
    print("=" * 78)
    print("PRIME.DETECTORINVERSION.01 -- exclusion-ladder extraction "
          "(detector_inversion_probe)")
    print("=" * 78)

    print("\nS0 -- firewall + zero cache (ward-side only)")
    check("S0.AST no zeta-zero generator call in this file "
          "(cached RvM-checked list read for calibration/on-line "
          "side only, v684 provenance)", ast_zero_firewall(__file__))
    d1 = json.load(open(os.path.join(_here,
                                     "zero_comb_cache_n2000.json")))
    d2 = json.load(open(os.path.join(_here, "c1_zero_ext_n2500.json")))
    gam_c = np.array(list(d1["gammas"]) + list(d2["gammas"]), float)
    check("S0.CACHE %d cached ordinates, gamma_1 = %.4f, gamma_top = "
          "%.1f" % (len(gam_c), gam_c[0], gam_c[-1]),
          len(gam_c) == 2500 and abs(gam_c[0] - 14.134725) < 1e-5)

    # ============================================================== S1
    print("\nS1 -- tower rebuild + verified-margin anchors")
    towers = {}
    for M, anch in RUNGS[:2]:
        alpha = 0.5 * M * DGRID
        ka = core.atoms_in(alpha)
        c_at, _ = core.atom_lags_at(alpha, M, core.U_ALL[:ka],
                                    core.MU_ALL[:ka])
        towers[M] = srp.continuum_lags(M) + c_at
    t0 = time.time()
    lam_tab = core.von_mangoldt_table(ATOM_MAX_DEEP)
    nn = np.nonzero(lam_tab > 0.0)[0]
    u_all = np.log(nn.astype(float))
    mu_all = 2.0 * lam_tab[nn] / np.sqrt(nn.astype(float))
    del lam_tab
    M_deep = RUNGS[2][0]
    al_deep = 0.5 * M_deep * DGRID
    ka = int(np.searchsorted(u_all, 2.0 * al_deep + 1e-14, "right"))
    c_at, _ = core.atom_lags_at(al_deep, M_deep, u_all[:ka],
                                mu_all[:ka])
    towers[M_deep] = srp.continuum_lags(M_deep) + c_at
    print("    deep comb: %d atoms to e^%.3f (sieve+reads %.1f s)"
          % (ka, 2.0 * al_deep, time.time() - t0))
    del u_all, mu_all

    T_of, m_of = {}, {}
    for M, anch in RUNGS:
        T = sla.toeplitz(towers[M][:M])
        lam = float(sla.eigvalsh(T, subset_by_index=[0, 0])[0])
        nrm = float(sla.norm(T, 2))
        T_of[M], m_of[M] = T, lam
        rel = abs(lam - anch) / anch
        fl = 100.0 * np.finfo(float).eps * nrm
        check("S1.%d rung M = %d (X = %.3f): lambda_min = %.4e vs "
              "cited anchor %.2e (rel dev %.3f <= %.2f); float budget "
              "100 eps ||T|| = %.1e, margin/budget = %.0f [gate b]"
              % (M, M, M * DGRID, lam, anch, rel, ANCH_REL, fl,
                 lam / fl), rel <= ANCH_REL and lam > fl)
    rel780 = abs(m_of[1176] - V780_DEEP) / V780_DEEP
    check("S1.DEEP v780 drainage anchor 3.882e-6 reproduced (rel "
          "dev %.3f <= %.2f)" % (rel780, ANCH_REL), rel780 <= ANCH_REL)

    # ============================================================== S2
    print("\nS2 -- calibration wards")
    gtest = 47.3
    lp = pair_lags(256, gtest)
    rank2 = 2.0 * a_weight(gtest) * np.cos(
        gtest * DGRID * np.arange(256))
    dev0 = float(np.max(np.abs(lp - rank2)))
    check("W0 the on-line pair layer == 2 a(g) cos(g k D) EXACTLY "
          "(rank-2 PSD; a(g) = D csinc(gD/2)^2 == the v692 zero-side "
          "weight): max dev %.2e <= %.0e" % (dev0, W0_BAR),
          dev0 <= W0_BAR)

    dev_q = 0.0
    for (gq, dq, kq) in ((31.7, 0.21, 40), (88.2, 0.44, 130),
                         (9.4, 0.08, 3)):
        ql = quad_lags(200, gq, dq)
        uu = np.linspace((kq - 1) * DGRID, (kq + 1) * DGRID, 20001)
        tent = (1.0 - np.abs(uu / DGRID - kq)) / DGRID
        integ = DGRID * float(np.trapezoid(
            tent * 4.0 * np.cosh(dq * uu) * np.cos(gq * uu), uu))
        dev_q = max(dev_q, abs(ql[kq] - integ) / abs(integ))
    check("WQ the quadruple lag reads == D x tent quadrature of "
          "4 cosh(delta u) cos(gamma u) (deployed D-normalized read "
          "convention, declared correction 1; 3 samples, max rel dev "
          "%.1e <= %.0e); v765 RT3 kernel with AMP_Z = 2 == this "
          "convention" % (dev_q, WQ_BAR), dev_q <= WQ_BAR)

    aw = a_weight(gam_c)
    for M in (256, 640):
        jj = np.arange(M) * DGRID
        worst = 0.0
        for g0 in W2_PACKETS:
            x = np.exp(-0.5 * ((jj - jj[M // 2]) / (M * DGRID / 8.0))
                       ** 2) * np.cos(g0 * jj)
            xTx = float(x @ (T_of[M] @ x))
            Xg = np.abs(np.exp(1j * np.outer(gam_c, jj)) @ x) ** 2
            zside = float(np.sum(2.0 * aw * Xg))
            tb = tail_budget(x, gam_c[-1], len(gam_c))
            worst = max(worst, abs(xTx - zside) / max(tb, 1e-300))
        check("W2 smooth-packet Guinand identity at M = %d: "
              "|x^T T x - zero side| <= %.1f x tail budget on all %d "
              "packets (worst ratio %.3f)"
              % (M, W2_SLACK, len(W2_PACKETS), worst),
              worst <= W2_SLACK)

    # ============================================================== S3
    print("\nS3 -- the exclusion map (safe rank-4 criterion; two "
          "boundaries, declared correction 2)")
    maps, maps_mb, mags = {}, {}, {}
    for M, _anch in RUNGS:
        T = T_of[M]
        nrmT = float(sla.norm(T, 2))
        exc = np.zeros((len(GAMMAS_GRID), len(DELTAS_GRID)), bool)
        mbk = np.zeros_like(exc)
        mag = np.zeros(exc.shape)
        t0 = time.time()
        for ig, g in enumerate(GAMMAS_GRID):
            for idl, dl in enumerate(DELTAS_GRID):
                ql = quad_lags(M, g, dl)
                Q = sla.toeplitz(ql[:M])
                bud = IDENT_BUD + 100.0 * np.finfo(float).eps \
                    * (nrmT + M * float(np.max(np.abs(ql))))
                lam4 = subspace_lam_min(T - Q, M, g, dl)
                exc[ig, idl] = lam4 < -bud
                mag[ig, idl] = lam4
                mbk[ig, idl] = subspace_lam_min(T + Q, M, g, dl) < -bud
        maps[M], maps_mb[M], mags[M] = exc, mbk, mag
        neg = -mag[exc] if exc.any() else np.array([0.0])
        print("    M = %4d: T-Q exclusion %4d/%d pts (|lam| median "
              "%.2e, min %.2e vs budget ~%.0e); margin-break %4d/%d "
              "pts (%.1f s)"
              % (M, int(exc.sum()), exc.size, float(np.median(neg)),
                 float(np.min(neg)), IDENT_BUD, int(mbk.sum()),
                 mbk.size, time.time() - t0))
    check("S3.1 both exclusion regions NONEMPTY on >= 2 rungs "
          "(T-Q: %s | margin-break: %s)"
          % (", ".join("M=%d: %d" % (M, maps[M].sum())
                       for M, _ in RUNGS),
             ", ".join("M=%d: %d" % (M, maps_mb[M].sum())
                       for M, _ in RUNGS)),
          sum(1 for M, _ in RUNGS if maps[M].sum() > 0) >= 2
          and sum(1 for M, _ in RUNGS if maps_mb[M].sum() > 0) >= 2)

    # boundaries per rung: raw T-Q (delta_min) and margin-break
    print("    boundaries: raw T-Q delta_min | margin-break "
          "delta_mb (-- = none):")
    print("    %8s | %7s %7s %8s | %7s %7s %8s"
          % ("gamma", "X=4", "X=10", "X=18.375", "X=4", "X=10",
             "X=18.375"))
    bounds = {M: np.full(len(GAMMAS_GRID), np.nan) for M, _ in RUNGS}
    bounds_mb = {M: np.full(len(GAMMAS_GRID), np.nan)
                 for M, _ in RUNGS}
    for ig, g in enumerate(GAMMAS_GRID):
        row_a, row_b = [], []
        for M, _ in RUNGS:
            for mp, bb, row in ((maps, bounds, row_a),
                                (maps_mb, bounds_mb, row_b)):
                idx = np.nonzero(mp[M][ig])[0]
                if len(idx):
                    bb[M][ig] = DELTAS_GRID[idx[0]]
                    row.append("%7.3f" % DELTAS_GRID[idx[0]])
                else:
                    row.append("%7s" % "--")
        if ig % 3 == 0:
            print("    %8.2f | %s | %s"
                  % (g, " ".join(row_a), " ".join(row_b)))
    print("    TYPING: the raw T-Q region includes the "
          "INTERPOLATION ZONE (small delta -- exclusion through the "
          "gamma-resolution of the actual zero pattern: placement/"
          "multiplicity, no margin break under injection); the "
          "margin-break region is the AMPLIFICATION ZONE (the "
          "detector-native cosh(delta u) mechanism).")

    # on-ordinate gamma family (report): quadruples parked exactly
    # on actual zero ordinates -- the pure off-line-width question
    M = 1176
    on_mb = []
    for gz in gam_c[:N_ONZERO]:
        if gz > GAMMAS_GRID[-1]:
            break
        dmb = np.nan
        for dl in DELTAS_GRID:
            ql = quad_lags(M, float(gz), float(dl))
            lam_pm = subspace_lam_min(
                T_of[M] + sla.toeplitz(ql[:M]), M, float(gz),
                float(dl))
            if lam_pm < -IDENT_BUD:
                dmb = dl
                break
        on_mb.append((float(gz), dmb))
    fin_on = [d for _, d in on_mb if np.isfinite(d)]
    print("    on-ordinate family (X = 18.375, first %d actual "
          "ordinates <= %.0f): margin-break delta_mb median %.4f, "
          "range [%.4f, %.4f] over %d ordinates"
          % (len(on_mb), GAMMAS_GRID[-1],
             float(np.median(fin_on)) if fin_on else float("nan"),
             min(fin_on) if fin_on else float("nan"),
             max(fin_on) if fin_on else float("nan"), len(fin_on)))

    # monotone census (both boundaries)
    mono_ok = True
    for mp, lab in ((maps, "T-Q"), (maps_mb, "margin-break")):
        for (M1, _), (M2, _) in zip(RUNGS[:-1], RUNGS[1:]):
            lost = int((mp[M1] & ~mp[M2]).sum())
            frac = lost / max(int(mp[M1].sum()), 1)
            mono_ok = mono_ok and frac <= MONO_TOL
            print("    monotone [%s]: region(M=%d) minus region(M=%d)"
                  ": %d pts (%.1f%%)" % (lab, M1, M2, lost,
                                         100 * frac))
    check("S3.2 deeper rungs keep shallower exclusions on BOTH "
          "boundaries (loss <= %.0f%%)" % (100 * MONO_TOL), mono_ok)

    # full-eig subsample ward (the subspace criterion is safe;
    # measure how much the full spectrum would add)
    agree, extra, n_samp = 0, 0, 0
    for M in (256, 1176):
        T = T_of[M]
        step = max(1, len(GAMMAS_GRID) // N_SUB_WARD)
        for ig in range(0, len(GAMMAS_GRID), step):
            g = GAMMAS_GRID[ig]
            b = bounds[M][ig]
            dl = b if np.isfinite(b) else DELTAS_GRID[-1]
            ql = quad_lags(M, g, dl)
            lam_full = float(sla.eigvalsh(
                T - sla.toeplitz(ql[:M]), subset_by_index=[0, 0])[0])
            lam_sub = subspace_lam_min(T - sla.toeplitz(ql[:M]), M,
                                       g, dl)
            n_samp += 1
            if lam_full <= lam_sub + 1e-12:
                agree += 1
            if lam_full < 0 <= lam_sub:
                extra += 1
    check("S3.3 subsample ward: full lambda_min <= subspace bound on "
          "%d/%d samples (safety); full spectrum would exclude %d "
          "additional boundary points (under-exclusion typed, safe "
          "side)" % (agree, n_samp, extra), agree == n_samp)

    # margin sensitivity (report only)
    M = 1176
    Tinfl = T_of[M] + (SENS_FACTOR - 1.0) * m_of[M] * np.eye(M)
    moved = 0
    for ig in range(0, len(GAMMAS_GRID), 6):
        g = GAMMAS_GRID[ig]
        b = bounds[M][ig]
        if not np.isfinite(b):
            continue
        ql = quad_lags(M, g, b)
        if subspace_lam_min(Tinfl - sla.toeplitz(ql[:M]), M, g, b) \
                >= 0.0:
            moved += 1
    print("    sensitivity (report): margin inflated x%.0f -> %d/6 "
          "sampled boundary points lose exclusion -- the region is "
          "driven by the on-line spectral mass near gamma, NOT by "
          "the margin's smallness (typed)" % (SENS_FACTOR, moved))

    # ============================================================== S4
    print("\nS4 -- the scaling law (margin-break boundary = the "
          "cosh-amplification object)")
    xi_med = {}
    for M, _ in RUNGS:
        X = M * DGRID
        fin = bounds_mb[M][np.isfinite(bounds_mb[M])]
        if len(fin):
            xi_med[M] = float(np.median(fin)) * X
            print("    X = %7.3f: median delta_mb = %.4f  ->  "
                  "Xi_eff = X delta_mb = %.3f  (%d/%d gammas reach)"
                  % (X, float(np.median(fin)), xi_med[M], len(fin),
                     len(GAMMAS_GRID)))
    if xi_med:
        xi_all = float(np.median(list(xi_med.values())))
        print("    cited v688/v694 detection threshold Xi_up = %.4f "
              "(frame-A family) -- Xi_eff/%0.4f = %.2f"
              % (XI_UP_CITED, XI_UP_CITED, xi_all / XI_UP_CITED))
        print("    X*(delta) = Xi_eff/delta benchmark ladder "
              "(comb cap e^{X*} atoms):")
        for dl in (0.5, 0.25, 0.1, 0.05, 0.01):
            xs = xi_all / dl
            print("      delta >= %5.2f excluded at depth X* = %7.1f"
                  "  (comb cap e^{X*} = %.2e)" % (dl, xs,
                                                  math.exp(xs)))
        print("    REACH (honest): the gamma-window is Nyquist-"
              "limited to pi/D = %.1f; NEW territory needs gamma > "
              "3e12 [A1], i.e. D < %.1e and M > %.1e X lags -- "
              "computationally out of reach by ~10 orders; the "
              "exclusion ladder is a DEPTH-to-WIDTH bridge, not a "
              "record claim." % (math.pi / DGRID, math.pi / 3.0e12,
                                 3.0e12 / math.pi))

    # ============================================================== S5
    print("\nS5 -- known-territory comparison (gate c, typed plainly)")
    print("    [A1] Platt-Trudgian 2021: all zeros with |gamma| <= "
          "3e12 are ON the critical line.  Every visible gamma "
          "(<= 190) is INSIDE that strip: the extracted region is "
          "NOT NEW -- it is an independent, TFPT-data-only "
          "re-derivation of a %.0e-times-smaller corner." % (3e12 / 190))
    M = 1176
    for gb in (50.0, 100.0, 180.0):
        ig = int(np.argmin(np.abs(GAMMAS_GRID - gb)))
        ours = bounds_mb[M][ig]
        dcl = 0.5 - 1.0 / (R_CLASSICAL * math.log(gb))
        print("    gamma = %5.1f: margin-break delta_mb >= %s | raw "
              "T-Q delta_min >= %s | classical (MTY 2024) delta > "
              "%.3f -- the margin-break band is %s in-band"
              % (gb, ("%.3f" % ours) if np.isfinite(ours) else "--",
                 ("%.3f" % bounds[M][ig])
                 if np.isfinite(bounds[M][ig]) else "--", dcl,
                 "WIDER" if (np.isfinite(ours) and ours < dcl)
                 else "narrower"))

    # ============================================================== C
    print("\nC -- controls (RT3-style injection wards, bound to the "
          "margin-break boundary; declared correction 2)")
    inside_ok, n_in = True, 0
    valid_ok, n_val = True, 0
    under = []
    for M in (640, 1176):
        T = T_of[M]
        nrmT = float(sla.norm(T, 2))
        for ig in (6, 18, 30):
            g = GAMMAS_GRID[ig]
            b = bounds_mb[M][ig]
            if not np.isfinite(b) or 2.0 * b > 0.5:
                continue

            def lam_full_at(dl):
                ql = quad_lags(M, g, dl)
                return float(sla.eigvalsh(
                    T + sla.toeplitz(ql[:M]),
                    subset_by_index=[0, 0])[0]), \
                    IDENT_BUD + 100.0 * np.finfo(float).eps \
                    * (nrmT + M * float(np.max(np.abs(ql))))

            lam, bud = lam_full_at(2.0 * b)
            n_in += 1
            inside_ok = inside_ok and (lam < -bud)
            # no-false-exclusion: the claimed boundary point itself
            lam, bud = lam_full_at(b)
            n_val += 1
            valid_ok = valid_ok and (lam < -bud)
            # measured under-detection: full break boundary below b
            d_full = b
            for dl in DELTAS_GRID[DELTAS_GRID < b][::-1]:
                lam, bud = lam_full_at(float(dl))
                if lam < -bud:
                    d_full = float(dl)
                else:
                    break
            under.append(b / d_full)
    check("C1a [must-fire] a synthetic quadruple INSIDE the margin-"
          "break region (2 delta_mb) breaks the verified margin: "
          "lambda_min(T + Q) < 0 at %d/%d interior points"
          % (n_in if inside_ok else -1, n_in),
          inside_ok and n_in >= 4)
    check("C1b [no-false-exclusion, declared correction 4] every "
          "claimed margin-break boundary point is confirmed by the "
          "FULL eigensolve: %d/%d; measured under-detection factor "
          "delta_mb/delta_full = %.2f..%.2f (median %.2f) -- the "
          "subspace boundary is conservative, as designed"
          % (n_val if valid_ok else -1, n_val, min(under),
             max(under), float(np.median(under))),
          valid_ok and n_val >= 4)

    # ============================================================== V
    print("\n" + "=" * 78)
    print("V -- verdict + recommended contract text (report only)")
    print("=" * 78)
    core_ok = (not FAILS)
    if core_ok:
        verdict = "DETECTOR-INVERTED"
    elif any(f.startswith(("W", "C1a")) for f in FAILS):
        verdict = "INVERSION-INVALID"
    else:
        verdict = "INVERSION-PARTIAL"
    print("""
  VERDICT: %s

  THE CONDITIONAL EXCLUSION STATEMENT (typed, two zones):
  'For every (gamma, delta) in the mapped T-Q region R (union over
  the three verified rungs), the hypothesis "the zero multiset
  contains the quadruple 1/2 +- delta +- i gamma and no other
  off-line zero in the visible band" contradicts the tent-level
  Guinand identity of the machine-verified GL1 tower.  Inside the
  margin-break subregion the exclusion is DETECTOR-NATIVE (an
  injected quadruple flips the verified margin -- the cosh
  amplification); the remainder is INTERPOLATION-ZONE exclusion
  (the window resolves the actual zero pattern: placement and
  multiplicity), strictly stronger than the detector but resting
  on the identity budget rather than a sign flip.'
  CAVEATS (typed): (a) single-quadruple dominance -- the v694
  masked-pair configurations (two sub-resolution pairs, Cholesky-PD
  on both family windows) are the known evasion class; the exclusion
  is per-hypothesis, not multiset-complete.  (b) float margins --
  every exclusion demanded below -(1e-8 + 100 eps (||T|| + ||Q||)),
  the 1e-8 covering the deployed continuum's read-convention
  systematics.  (c) the region is INSIDE the [A1]-verified strip:
  consistency re-derivation, not new zero-free territory.

  RECOMMENDED CONTRACT TEXT (PRIME.FLOOR.RATIO.01, new deliverable
  class, report only): 'EXCLUSION LADDER: each newly verified PSD
  rung (X, m_X) of the GL1 tower shall be published together with
  its excluded quadruple region R_X = {(gamma, delta):
  lambda_min(T_X - Q_{gamma,delta}) < 0} and the threshold census
  Xi_eff = X delta_min(gamma); the ladder turns computation depth
  into effective zero-free width at the calibrated rate X*(delta)
  ~= Xi_eff/delta, subject to the single-quadruple dominance caveat
  and Nyquist reach pi/D.'
""" % verdict)
    print("[TIME] %.1f s   [CHECKS] %d run, %d failed%s"
          % (time.time() - T0, N_CHK, len(FAILS),
             ("  " + ",".join(FAILS)) if FAILS else ""))
    return 0 if not FAILS else 1


if __name__ == "__main__":
    raise SystemExit(run())
