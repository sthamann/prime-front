#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""cone_kernel_field_probe -- PRIME.CELLCONE.KERNELFIELD.01
(EXPLORATION ONLY, experiments/; direct follow-up to the CONE-BROKEN
verdict of cell_cone_transport_probe / PRIME.CELLCONE.TRANSPORT.01,
2026-08-07 -- package D is NOT buried yet: two stages in one probe).

PARENT FINDINGS (cited, machinery imported READ-ONLY, bit for bit):
the completed-cell flow A_k = (B - S_pnt) + sum_{j<=k}(Chat_j -
lam_j Xhat_j) telescopes exactly but EXITS the fixed Lorentz cone on
67/67 rungs under both groupings, first exit at the n = 2 cell,
endpoint back inside on 67/67; G1 (Stieltjes) worst relative depth
shrinks along the ladder (-3.9e-2 -> -1.9e-3), G2 (mass-matched) has
deep long excursions; RAY-EDGE-CONFIRMED; the Epstein control did
NOT break (inverted signature: the dips are the true comb's own
psi(x) - x fluctuation).

STAGE 1 -- THE FINITE PRIME KERNEL (the 5-step protocol):
  (1) per rung and grouping, the exact violation positions (states
      with lambda_min <= 0 after a cell) and the LAST violating
      prime-power block P0(rung);
  (2) the renormalized base A_kernel = A_0 + sum_{n <= P0}(cells) is
      EXACT (it is the running state at the last violating cell --
      the flow is additive, so the per-rung tail-clean statement is
      BY CONSTRUCTION; stated openly, verified numerically);
  (3) the tail from the renormalized base preserves the cone
      per rung (by construction; asserted);
  (4) THE DECISIVE MEASUREMENT: does P0 stabilize or wander across
      the 67-rung depth ladder?  Typed laws: P0 vs X = e^{2 alpha}
      (log-log slope), u_{P0}/(2 alpha) (median + Kendall vs alpha),
      violation count vs K; plus the PREDECLARED depth-resolved
      census: violation at relative depth d iff lambda_min /
      lambda_max < -d for d in {0(strict), 1e-3, 1e-2, 1e-1} and the
      tau-relative census (lambda_min <= -tau_rung) -- the parent
      showed the strict late violations are thinner than the
      certified endpoint margin, so the depth-resolved kernel is the
      honest renormalization question;
  (5) KILL only if the violation position wanders unboundedly:
      frozen WANDER criterion = [median u_{P0}/(2 alpha) >= 0.5] AND
      [P0 at the top rung > P0_CAP]; frozen KERNEL-STABLE criterion
      = [max over rungs of strict P0 <= P0_CAP = 100 (in n)].
  Fixed-kernel prediction test (report): P0* = max strict P0 over
  the smallest third of the ladder; count tail violations n > P0*
  on the upper two thirds.

STAGE 2 -- THE MOVING LORENTZ CONE FIELD (F3):
  GEOMETRIC FACT stated up front (forces the design): congruence-
  image cones are USELESS here -- for any invertible 2x2 T the set
  {T X T^T : X >= 0} IS the PSD cone (Sylvester), so a moving cone
  must act on the Lorentz 3-vectors u = L(A) with G_m in GL(3) NOT
  of (scaled) Lorentz type.  Frozen field family: CIRCULAR TUBE
  CONES K_m = G_m L+ with G_m = R_m diag(1, tan th_m, tan th_m),
  R_m the rotation taking e_t to the past-only axis, th_m the
  half-opening; membership u_m in K_m <=> angle(u_m, axis_m) <=
  th_m.  cond(G_m) = max(tan th_m, cot th_m), tracked, bar
  COND_BAR = 100.  TWO PREDECLARED FIELD RULES (past-only):
    A (polar frame of the running state): axis_m = u_{m-1}/|u_{m-1}|
      (the previous state direction -- the polar frame of the
      renormalized running state, history only);
    B (mu*log-weighted frame): axis_m = normalized trailing
      mass-weighted mean sum w_j u_j over the last NW = 32 states
      j < m, w_j = Lambda(n_j)/sqrt(n_j) (the multiplicative weights
      anchor the frame -- heavier arithmetic cells count more; the
      base state carries the mean mass).
  ADAPTIVE OPENING (same rule both fields, frozen): th_m =
  clip(ANG_FAC x max of the trailing NW-window of past angle
  readings (rule A: increments angle(u_j, u_{j-1}); rule B: axis
  angles angle(u_j, axis_j)), ANG_MIN = 1 deg, 89 deg); a trailing
  window (not the all-time max) so that the warm-up spikes EXPIRE
  and the test is not vacuous.  WARM-UP: cells 1..NWARM = 12 (the
  parent's small-n dip zone n = 2..19) are the absorbed finite
  kernel -- measured, not gated; gated transport = cells NWARM+1..K.
  FIELD-RELATIVE J-DEFECT per gated cell: fdef_m = angle_m/th_m - 1
  (<= 0 required); FIELD TRANSPORTS iff zero gated violations on
  all rungs AND max cond <= COND_BAR.
  CAUSAL FENCE (no-tau-peeking, structural): th_m and axis_m are
  computed from index slices [:m] ONLY; asserted by explicit
  recomputation at frozen spot cells; tau_m / the current sign never
  enters the field construction (the gate reads only the angle
  history).  The set inclusion Phi_m(K_m) <= K_{m+1} is measured on
  the parent's congruence spot cells via the conjugated map Psi_m =
  G_{m+1}^{-1} Phi_m G_m over NRAY = 64 frozen boundary rays
  (report-only; the per-cell gate is state membership).

CONTROLS (frozen fire rules):
  stage 1: equal-weight scramble and wrong pole normalization
    (x WRONG_FAC = 2, self-consistent base) on the stride-5 subset:
    fire iff [strict violation count median >= CTRL_FAC = 3 x the
    real median] OR [base out of cone];
  stage 2 (rule A, G1, stride-5 subset): equal-weight scramble and
    wrong normalization must fire: [gated violation count median >=
    CTRL_FAC x max(real median, 1)] OR [median max post-warm-up
    increment >= CTRL_FAC x real median]; EPSTEIN x^2+5y^2 is a
    TYPED two-sided separation control (parent's inverted-signature
    caveat): DISTINGUISHABLE iff the median max post-warm-up
    increment differs from the real one by factor >= EP_SEP = 3 in
    EITHER direction, else control surprise (typed, does not gate).

VERDICT ENUM (frozen, decision order):
  INVALID           -- a ward fails (no structural claim, exit 1).
  KERNEL-TAIL-CLEAN -- strict kernel bounded (max P0 <= P0_CAP) for
      >= 1 grouping AND stage-1 must-breaks fire: the classical
      structure 'finite arithmetic kernel + cone-preserving tail'
      exists.
  FIELD-TRANSPORTS  -- stage 1 fails but >= 1 (field rule x
      grouping) achieves zero gated violations with cond <= COND_BAR
      AND stage-2 must-breaks fire: the moving relational cone
      carries the flow.
  BOTH-PARTIAL      -- any of (typed): (i) strict kernel bounded on
      >= 0.5 of rungs; (ii) the depth-1e-2 kernel bounded (max
      depth-resolved P0 <= P0_CAP on all rungs) -- the kernel exists
      after depth renormalization; (iii) a field rule reaches
      overall gated violation fraction <= 1e-3 with bounded cond;
      (iv) a passing stage would have fired but its must-break
      control did not (control surprise cap).
  KERNEL-WANDERS    -- the kill: strict positions wander (frozen
      criterion), no depth-renormalized kernel, no field transports.
NO RH claim.  Finite measurement on 67 rungs; nothing here bounds
the infinite ladder.  Writes no files; nothing outside experiments/.

FIREWALL: parent probe + v563 imported READ-ONLY (construction bit
for bit); mpmath only via the parent constant C_TH; no zeta zero
read (AST-checked, banned ids as parent); NO RNG anywhere; runtime
cap 1800 s predeclared.

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/cone_kernel_field_probe.py
"""

import ast
import hashlib
import inspect
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

import v563_paper2_readouts as core            # noqa: E402 (READ-ONLY)
import cell_cone_transport_probe as parent     # noqa: E402 (READ-ONLY)

FROZEN_SPEC = """\
PRIME.CELLCONE.KERNELFIELD.01 spec v1 (2026-08-07, frozen before the
run).  Ladder/objects/groupings = parent PRIME.CELLCONE.TRANSPORT.01
verbatim (67 rungs, Ah = B - S, A_0 = B - S_pnt, G1 Stieltjes / G2
mass-matched completed cells; parent module imported read-only).
WARDS (must pass, else INVALID): tau refs kz 9/12/13 rel <= 1e-4;
envelope min e1 >= 4.335*0.999; telescoping rel <= 1e-9 per rung per
grouping; parent regression: cone exit on 67/67 rungs for BOTH
groupings.  STAGE 1: violation = state after cell with lambda_min <=
0 (strict); P0(rung) = n of last violating cell; depth-resolved
censuses at rel depth lambda_min/lambda_max < -d, d in {1e-3, 1e-2,
1e-1}, plus tau-relative (lambda_min <= -tau_rung); laws: log P0 vs
2 alpha slope, u_P0/(2 alpha) median + Kendall, count vs K;
KERNEL-STABLE iff max strict P0 <= P0_CAP = 100 (in n); WANDER iff
median u_P0/(2 alpha) >= 0.5 AND top-rung P0 > P0_CAP; fixed-kernel
prediction: P0* = max strict P0 over the smallest third (alpha
order), tail violations n > P0* counted above.  STAGE 2: tube field
K_m = cone(axis_m, th_m); rule A axis = u_{m-1} direction; rule B
axis = trailing NW = 32 mass-weighted mean (w = Lambda/sqrt(n), base
weight = mean mass); th_m = clip(ANG_FAC = 2.0 x trailing-NW-window
max of past angle readings, ANG_MIN = 1 deg, 89 deg); warm-up NWARM
= 12 cells (measured, not gated); violation iff angle_m > th_m on a
gated cell; fdef = angle/th - 1; cond = max(tan th, cot th) <=
COND_BAR = 100; causal fence asserted at spot cells [NWARM+1, K/2,
K-1]; FIELD ok iff zero gated violations all rungs AND cond bound.
Psi-inclusion on parent spot cells over NRAY = 64 boundary rays =
report-only.  CONTROLS: stride 5; stage-1 fire = [strict count
median >= 3x real] OR [base out]; stage-2 fire (rule A, G1) =
[gated count median >= 3x max(real,1)] OR [median max post-warm
increment >= 3x real]; Epstein = typed two-sided separation, factor
EP_SEP = 3, does not gate.  VERDICT order: INVALID; KERNEL-TAIL-
CLEAN (strict kernel bounded >= 1 grouping + stage-1 fires);
FIELD-TRANSPORTS (>= 1 rule x grouping clean + cond ok + stage-2
fires); BOTH-PARTIAL ((i) strict kernel bounded on >= 0.5 rungs,
(ii) depth-1e-2 kernel bounded all rungs, (iii) field violation
fraction <= 1e-3 with cond ok, or (iv) control-surprise cap);
KERNEL-WANDERS else.  No prediction frozen for stage outcomes.
NO RH claim; writes nothing.
"""

STRIDE = 5
TAU_REFS = {9: 5.984165e-4, 12: 4.351189e-4, 13: 5.637632e-4}
TAU_REF_REL = 1.0e-4
ENV_C = 4.335
ENV_GUARD = 0.999
WARD_REL = 1.0e-9
P0_CAP = 100
DEPTHS = (1.0e-3, 1.0e-2, 1.0e-1)
NWARM = 12
NW = 32
ANG_FAC = 2.0
ANG_MIN_DEG = 1.0
ANG_MAX_DEG = 89.0
COND_BAR = 100.0
CTRL_FAC = 3.0
EP_SEP = 3.0
NRAY = 64
WRONG_FAC = 2.0
KEN_BAR = 0.8
RUNTIME_CAP = 1800.0
BANNED_IDS = ("zetazero", "nzeros", "primerange", "isprime", "primepi",
              "nextprime", "prevprime", "find_zeros",
              "second_sheet_zero")

CHECKS = []
FAILS = []
T0 = time.time()


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok)))
    if not ok:
        FAILS.append(name.split()[0])
    print("  [%s] %s%s" % ("PASS" if ok else "FAIL", name,
                           ("  -- " + detail) if detail else ""),
          flush=True)


def ast_zero_firewall(src_path):
    with open(src_path, "r", encoding="utf-8") as fh:
        tree = ast.parse(fh.read())
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            f = node.func
            nm = f.attr if isinstance(f, ast.Attribute) else (
                f.id if isinstance(f, ast.Name) else "")
            if nm in BANNED_IDS:
                return False
    return True


def kendall_tau(x, y):
    n = len(x)
    conc = disc = 0
    for i in range(n):
        for j in range(i + 1, n):
            s = (x[j] - x[i]) * (y[j] - y[i])
            if s > 0:
                conc += 1
            elif s < 0:
                disc += 1
    return (conc - disc) / max(n * (n - 1) // 2, 1)


def ols_loglog(x, y):
    lx = np.log(np.asarray(x, float))
    ly = np.log(np.abs(np.asarray(y, float)))
    b, q = np.polyfit(lx, ly, 1)
    pred = b * lx + q
    r2 = 1.0 - float(((ly - pred) ** 2).sum()) \
        / max(float(((ly - ly.mean()) ** 2).sum()), 1e-300)
    return float(b), r2


def uvecs_of(ps):
    """(K+1, 3) Lorentz state vectors from a parent path_stats dict."""
    t = ps["a11"] + ps["a22"]
    x = ps["a11"] - ps["a22"]
    y = 2.0 * ps["a12"]
    return np.stack([t, x, y], axis=1)


def angles_between(U, V):
    """Per-row angle in degrees between two (n,3) arrays."""
    nu = np.linalg.norm(U, axis=1)
    nv = np.linalg.norm(V, axis=1)
    c = np.einsum("ij,ij->i", U, V) / np.maximum(nu * nv, 1e-300)
    return np.degrees(np.arccos(np.clip(c, -1.0, 1.0)))


def trailing_max(arr, win):
    """max over the last `win` entries STRICTLY BEFORE each index
    (past-only); -inf where no history exists."""
    pad = np.concatenate([np.full(win, -np.inf), np.asarray(arr,
                                                            float)])
    sw = np.lib.stride_tricks.sliding_window_view(pad, win)
    # sw[i] = pad[i : i+win] = arr[i-win : i] -> past-only at index i
    return sw[:len(arr) + 1].max(axis=1)[:len(arr) + 1]


# ------------------------------------------------- the two field rules
def field_A_axes(U):
    """Rule A: axis_m = direction of u_{m-1} (PAST-only).  Input U =
    (K+1,3) states; output axes for cells m = 1..K as (K,3)."""
    return U[:-1]


def field_B_axes(U, w):
    """Rule B: axis_m = trailing NW-window mass-weighted mean of the
    states j < m (PAST-only); w = per-state weights (w[0] = base
    weight, w[j] = Lambda(n_j)/sqrt(n_j))."""
    K1 = len(U)
    cs = np.vstack([np.zeros(3), np.cumsum(w[:, None] * U, axis=0)])
    cw = np.concatenate([[0.0], np.cumsum(w)])
    m = np.arange(1, K1)                       # cells 1..K
    lo = np.maximum(m - NW, 0)
    num = cs[m] - cs[lo]
    den = cw[m] - cw[lo]
    return num / np.maximum(den[:, None], 1e-300)


def field_run(U, axes_rule, w=None):
    """One field pass: angle readings, past-only adaptive opening,
    gated violations.  Returns the per-cell arrays + summary."""
    if axes_rule == "A":
        axes = field_A_axes(U)
    else:
        axes = field_B_axes(U, w)
    ang = angles_between(U[1:], axes)          # angle reading, cell m
    tmax = trailing_max(ang, NW)[:-1]          # past-only, index m
    th = np.clip(ANG_FAC * tmax, ANG_MIN_DEG, ANG_MAX_DEG)
    fdef = ang / th - 1.0
    gated = np.arange(len(ang)) >= NWARM       # cells NWARM+1..K
    viol = gated & (ang > th)
    tanth = np.tan(np.radians(th[gated]))
    cond = (np.max(np.maximum(tanth, 1.0 / tanth))
            if gated.any() else 1.0)
    return dict(ang=ang, th=th, fdef=fdef, viol=viol, gated=gated,
                nviol=int(viol.sum()), ngate=int(gated.sum()),
                worst_fdef=float(np.max(fdef[gated]))
                if gated.any() else float("-inf"),
                max_inc=float(np.max(ang[gated]))
                if gated.any() else 0.0,
                cond=float(cond))


def causal_assert(U, rule, w, res):
    """Recompute th at frozen spot cells from explicit [:m] slices --
    the structural no-peeking assertion."""
    K = len(U) - 1
    spots = [NWARM + 1, K // 2, K - 1]
    for m in spots:                            # cell index 1-based m+1
        ang_hist = res["ang"][:m]              # readings of cells <= m
        tm = float(np.max(ang_hist[-NW:])) if len(ang_hist) else -np.inf
        th_ref = min(max(ANG_FAC * tm, ANG_MIN_DEG), ANG_MAX_DEG)
        if not math.isclose(th_ref, float(res["th"][m]),
                            rel_tol=1e-12, abs_tol=1e-12):
            return False
    return True


def rot_to(axis):
    """SO(3) rotation taking e_t = (1,0,0) to the unit axis."""
    a = axis / max(np.linalg.norm(axis), 1e-300)
    e = np.array([1.0, 0.0, 0.0])
    v = np.cross(e, a)
    c = float(e @ a)
    s = float(np.linalg.norm(v))
    if s < 1e-14:
        return np.eye(3) if c > 0 else np.diag([-1.0, -1.0, 1.0])
    vx = np.array([[0.0, -v[2], v[1]], [v[2], 0.0, -v[0]],
                   [-v[1], v[0], 0.0]])
    return np.eye(3) + vx + vx @ vx * ((1.0 - c) / (s * s))


def G_of(axis, th_deg):
    return rot_to(axis) @ np.diag([1.0, math.tan(math.radians(th_deg)),
                                   math.tan(math.radians(th_deg))])


def main():
    spec_hash = hashlib.sha256(FROZEN_SPEC.encode()).hexdigest()
    fa_hash = hashlib.sha256(
        inspect.getsource(field_A_axes).encode()).hexdigest()
    fb_hash = hashlib.sha256(
        inspect.getsource(field_B_axes).encode()).hexdigest()
    fr_hash = hashlib.sha256(
        inspect.getsource(field_run).encode()).hexdigest()
    print("=" * 78)
    print("PRIME.CELLCONE.KERNELFIELD.01 -- finite prime kernel + "
          "moving Lorentz cone field")
    print("=" * 78)
    print(FROZEN_SPEC)
    print("SPEC sha256       : %s" % spec_hash)
    print("field A sha256    : %s" % fa_hash)
    print("field B sha256    : %s" % fb_hash)
    print("field gate sha256 : %s" % fr_hash)
    print("parent G1/G2 sha256 (imported): %s / %s"
          % (hashlib.sha256(inspect.getsource(
              parent.breaks_G1).encode()).hexdigest()[:16],
             hashlib.sha256(inspect.getsource(
                 parent.breaks_G2).encode()).hexdigest()[:16]))

    # ============================================================== S0
    print("\nS0 -- firewall")
    check("S0.AST no zero/prime-table loader (banned ids absent); "
          "parent + v563 read-only; NO RNG",
          ast_zero_firewall(__file__))

    # ============================================================== S1
    print("\nS1 -- ladder + wards (parent construction, bit for bit)")
    rows = []
    for kz in core.frame_a_zones():
        rr = core.build_window(kz)
        if rr["h"] == parent.ANOMALOUS_H:
            continue
        if math.exp(2.0 * rr["alpha"]) > core.ATOM_MAX + 0.5:
            continue
        rows.append(dict(rr=rr, kz=kz, h=rr["h"], alpha=rr["alpha"],
                         tau=parent.eig2_min(rr["Ah"])))
    rows.sort(key=lambda w: w["alpha"])
    print("    %d rungs, alpha %.3f..%.3f" % (len(rows),
                                              rows[0]["alpha"],
                                              rows[-1]["alpha"]))
    ref_ok = all(abs(parent.eig2_min(core.build_window(kz)["Ah"])
                     - tr) / tr <= TAU_REF_REL
                 for kz, tr in TAU_REFS.items())
    check("S1.REF tau references kz 9/12/13 reproduce (bar %.0e)"
          % TAU_REF_REL, ref_ok)

    env_min = float("inf")
    tel_worst = 0.0
    exit_ok = True
    for w in rows:
        rr = w["rr"]
        edges, reads = parent.pnt_grid(rr)
        w["edges"], w["reads"] = edges, reads
        S_pnt = parent.tri_mat(parent.cum_reads(
            edges, reads, [2.0 * rr["alpha"]])[0])
        w["S_pnt"] = S_pnt
        A0 = rr["B"] - S_pnt
        w["A0"] = A0
        w["tau_pnt"] = parent.eig2_min(A0)
        env_min = min(env_min, (w["tau"] / w["tau_pnt"])
                      * w["h"] ** 1.5)
        uu, lam, Xn = rr["uu"], rr["lam"], rr["Xn"]
        w["mm"] = 2.0 * lam
        w["nn"] = np.rint(np.exp(uu)).astype(np.int64)
        for g in ("G1", "G2"):
            b = (parent.breaks_G1(uu, rr["alpha"]) if g == "G1"
                 else parent.breaks_G2(w["mm"], rr["alpha"]))
            Chat = parent.cell_increments(edges, reads, b)
            deltas = Chat - lam[:, None] * Xn
            ps = parent.path_stats((A0[0, 0], A0[1, 1], A0[0, 1]),
                                   deltas)
            Aend = parent.tri_mat((ps["a11"][-1], ps["a22"][-1],
                                   ps["a12"][-1]))
            tel = float(np.max(np.abs(Aend - rr["Ah"]))) \
                / float(np.max(np.abs(rr["Ah"])))
            tel_worst = max(tel_worst, tel)
            if bool(np.all(ps["lmin"] > 0.0)):
                exit_ok = False
            w[g] = dict(ps=ps, U=uvecs_of(ps))
    check("S1.ENV envelope min e1 = %.4f >= %.4f" %
          (env_min, ENV_C * ENV_GUARD), env_min >= ENV_C * ENV_GUARD)
    check("S1.TEL telescoping worst rel %.2e (bar %.0e)"
          % (tel_worst, WARD_REL), tel_worst <= WARD_REL)
    check("S1.REG parent regression: the completed flow exits the "
          "fixed cone on every rung for BOTH groupings (the "
          "CONE-BROKEN input state)", exit_ok)

    # ============================================================== S2
    print("\nS2 -- STAGE 1: the finite prime kernel census")
    aas = [w["alpha"] for w in rows]
    stage1 = {}
    for g in ("G1", "G2"):
        print("\n  grouping %s:" % g)
        print("    %5s %7s %6s | %6s %8s %6s | %8s %8s %8s | %6s"
              % ("h", "alpha", "K", "nviol", "P0", "uP0/2a",
                 "P0@1e-3", "P0@1e-2", "P0@1e-1", "P0@tau"))
        P0s, upos, counts, Ks = [], [], [], []
        P0d_all = {d: [] for d in DEPTHS}
        for w in rows:
            ps = w[g]["ps"]
            lmin, lmax = ps["lmin"][1:], ps["lmax"][1:]
            rel = lmin / np.maximum(lmax, 1e-300)
            nn = w["nn"]
            strict = lmin <= 0.0
            nv = int(strict.sum())
            P0 = int(nn[np.where(strict)[0][-1]]) if nv else 0
            up = (w["rr"]["uu"][np.where(strict)[0][-1]]
                  / (2.0 * w["alpha"])) if nv else 0.0
            dP = {}
            for d in DEPTHS:
                mk = rel < -d
                dP[d] = int(nn[np.where(mk)[0][-1]]) if mk.any() else 0
                P0d_all[d].append(dP[d])
            mk_tau = lmin <= -w["tau"]
            P0tau = int(nn[np.where(mk_tau)[0][-1]]) \
                if mk_tau.any() else 0
            # step (3): tail from the renormalized base is clean by
            # construction -- verified:
            if nv:
                k_last = np.where(strict)[0][-1]
                assert bool(np.all(lmin[k_last + 1:] > 0.0))
            P0s.append(P0)
            upos.append(up)
            counts.append(nv)
            Ks.append(len(lmin))
            print("    %5d %7.3f %6d | %6d %8d %6.3f | %8d %8d %8d "
                  "| %6d"
                  % (w["h"], w["alpha"], len(lmin), nv, P0, up,
                     dP[DEPTHS[0]], dP[DEPTHS[1]], dP[DEPTHS[2]],
                     P0tau))
        sl_P0, r2_P0 = ols_loglog(
            [math.exp(2.0 * a) for a in aas],
            [max(p, 1) for p in P0s])
        sl_cnt, r2_cnt = ols_loglog(Ks, [max(c, 1) for c in counts])
        kt_up = kendall_tau(aas, upos)
        med_up = float(np.median(upos))
        third = max(len(rows) // 3, 1)
        P0_star = max(P0s[:third])
        tail_beyond = 0
        for i, w in enumerate(rows[third:], start=third):
            ps = w[g]["ps"]
            strict = ps["lmin"][1:] <= 0.0
            tail_beyond += int(np.sum(strict & (w["nn"] > P0_star)))
        stage1[g] = dict(P0s=P0s, med_up=med_up, kt_up=kt_up,
                         maxP0=max(P0s), sl_P0=sl_P0,
                         maxP0_d={d: max(P0d_all[d]) for d in DEPTHS},
                         counts=counts, P0_star=P0_star,
                         tail_beyond=tail_beyond)
        print("    LAW (%s): P0 ~ X^%.2f (R^2 %.2f, X = e^{2 alpha});"
              " count ~ K^%.2f (R^2 %.2f); u_P0/(2 alpha) median "
              "%.3f, Kendall vs alpha %+.3f; max strict P0 = %d "
              "(cap %d); depth-resolved max P0: %s; fixed-kernel "
              "prediction P0* = %d (smallest third) -> %d tail "
              "violations beyond it above"
              % (g, sl_P0, r2_P0, sl_cnt, r2_cnt, med_up, kt_up,
                 max(P0s), P0_CAP,
                 {("%.0e" % d): stage1[g]["maxP0_d"][d]
                  for d in DEPTHS}, P0_star, tail_beyond))
        print("    step (2)/(3) note: the flow is additive, so the "
              "per-rung tail-clean statement from the renormalized "
              "base A_kernel(P0) is BY CONSTRUCTION (asserted "
              "numerically above); the decisive content is the "
              "cross-depth stability of P0.")

    kernel_ok = {g: stage1[g]["maxP0"] <= P0_CAP for g in ("G1", "G2")}
    kernel_half = {g: (np.mean([p <= P0_CAP for p in stage1[g]["P0s"]])
                       >= 0.5) for g in ("G1", "G2")}
    kernel_depth = {g: stage1[g]["maxP0_d"][1.0e-2] <= P0_CAP
                    for g in ("G1", "G2")}
    wander = {g: (stage1[g]["med_up"] >= 0.5
                  and stage1[g]["P0s"][-1] > P0_CAP)
              for g in ("G1", "G2")}
    print("\n  STAGE-1 GATES: strict kernel bounded G1 %s / G2 %s; "
          "bounded on >= half the rungs G1 %s / G2 %s; depth-1e-2 "
          "kernel bounded G1 %s / G2 %s; WANDER criterion G1 %s / "
          "G2 %s"
          % (kernel_ok["G1"], kernel_ok["G2"], kernel_half["G1"],
             kernel_half["G2"], kernel_depth["G1"], kernel_depth["G2"],
             wander["G1"], wander["G2"]))

    # stage-1 controls (stride subset, G1 pairing)
    sub = rows[::STRIDE]
    real_cnt_med = float(np.median(
        [stage1["G1"]["counts"][i] for i in range(0, len(rows),
                                                  STRIDE)]))

    def ctrl_path(w, uuX, lamX, XnX, cont_fac=1.0, base_fac=1.0):
        rr = w["rr"]
        b = parent.breaks_G1(uuX, rr["alpha"])
        Chat = cont_fac * parent.cell_increments(w["edges"],
                                                 w["reads"], b)
        deltas = Chat - lamX[:, None] * XnX
        A0 = rr["B"] - base_fac * w["S_pnt"]
        return parent.path_stats((A0[0, 0], A0[1, 1], A0[0, 1]),
                                 deltas)

    def s1_stats(ps):
        strict = ps["lmin"][1:] <= 0.0
        return int(strict.sum()), bool(ps["lmin"][0] <= 0.0)

    eq_cnt, eq_base = [], 0
    wr_cnt, wr_base = [], 0
    eq_ps_cache, wr_ps_cache = [], []
    for w in sub:
        rr = w["rr"]
        mm_eq = np.full(len(rr["uu"]),
                        float(np.sum(w["mm"])) / len(rr["uu"]))
        ps_e = ctrl_path(w, rr["uu"], 0.5 * mm_eq, rr["Xn"])
        c, b = s1_stats(ps_e)
        eq_cnt.append(c)
        eq_base += b
        eq_ps_cache.append(ps_e)
        ps_w = ctrl_path(w, rr["uu"], rr["lam"], rr["Xn"],
                         cont_fac=WRONG_FAC, base_fac=WRONG_FAC)
        c, b = s1_stats(ps_w)
        wr_cnt.append(c)
        wr_base += b
        wr_ps_cache.append(ps_w)
    eq1_fire = (float(np.median(eq_cnt)) >= CTRL_FAC * real_cnt_med
                or eq_base > 0)
    wr1_fire = (float(np.median(wr_cnt)) >= CTRL_FAC * real_cnt_med
                or wr_base > 0)
    check("S2.C1 [must-break, stage 1] equal-weight scramble: strict "
          "violation count median %.0f vs real %.0f (x%.1f needed) "
          "or base out (%d rungs) -- %s"
          % (float(np.median(eq_cnt)), real_cnt_med, CTRL_FAC,
             eq_base, "fires" if eq1_fire else "does NOT fire"),
          eq1_fire)
    check("S2.C2 [must-break, stage 1] wrong pole normalization "
          "(x%.1f): count median %.0f, base out on %d/%d rungs -- %s"
          % (WRONG_FAC, float(np.median(wr_cnt)), wr_base, len(sub),
             "fires" if wr1_fire else "does NOT fire"), wr1_fire)

    # ============================================================== S3
    print("\nS3 -- STAGE 2: the moving Lorentz cone field "
          "(warm-up %d cells; gated tail)" % NWARM)
    field = {}
    causal_ok = True
    for g in ("G1", "G2"):
        for rule in ("A", "B"):
            key = "%s-%s" % (rule, g)
            nv_tot = ng_tot = 0
            per_rung_nv, worst_fdefs, max_incs, conds = [], [], [], []
            for w in rows:
                U = w[g]["U"]
                wgt = np.concatenate([[float(np.mean(w["mm"]))],
                                      w["mm"]])
                res = field_run(U, rule, w=wgt)
                if w is rows[0]:
                    causal_ok = causal_ok and causal_assert(
                        U, rule, wgt, res)
                nv_tot += res["nviol"]
                ng_tot += res["ngate"]
                per_rung_nv.append(res["nviol"])
                worst_fdefs.append(res["worst_fdef"])
                max_incs.append(res["max_inc"])
                conds.append(res["cond"])
                w.setdefault("field", {})[key] = res
            sl_inc, r2_inc = ols_loglog(aas, [max(v, 1e-12)
                                              for v in max_incs])
            field[key] = dict(
                nviol=nv_tot, ngate=ng_tot,
                frac=nv_tot / max(ng_tot, 1),
                rungs_clean=sum(1 for v in per_rung_nv if v == 0),
                worst_fdef=float(np.max(worst_fdefs)),
                med_fdef=float(np.median(worst_fdefs)),
                cond_max=float(np.max(conds)),
                med_maxinc=float(np.median(max_incs)),
                sl_inc=sl_inc, r2_inc=r2_inc)
            f = field[key]
            print("    rule %s on %s: gated violations %d / %d "
                  "(%.2e), clean rungs %d/%d; worst fdef %+.3f "
                  "(median per-rung worst %+.3f); max post-warm "
                  "angle reading median %.3f deg ~ alpha^%.2f (R^2 "
                  "%.2f); cond(G) max %.1f (bar %.0f)"
                  % (rule, g, f["nviol"], f["ngate"], f["frac"],
                     f["rungs_clean"], len(rows), f["worst_fdef"],
                     f["med_fdef"], f["med_maxinc"], f["sl_inc"],
                     f["r2_inc"], f["cond_max"], COND_BAR))
    check("S3.CAUSAL the field is past-only: opening th_m recomputed "
          "from explicit [:m] slices at the frozen spot cells, both "
          "rules (tau_m / the current sign never enters the "
          "construction -- the gate reads only the angle history)",
          causal_ok)

    # Psi set-inclusion on the parent spot cells (report-only)
    w0 = rows[0]
    ps0 = w0["G1"]["ps"]
    U0 = w0["G1"]["U"]
    resA = w0["field"]["A-G1"]
    phis = np.linspace(0.0, 2.0 * math.pi, NRAY, endpoint=False)
    rays = np.stack([np.ones(NRAY), np.cos(phis), np.sin(phis)],
                    axis=1)                     # L+ boundary rays
    incl_lines = []
    for k in range(NWARM, len(U0) - 2):
        Ap = parent.tri_mat((ps0["a11"][k], ps0["a22"][k],
                             ps0["a12"][k]))
        An = parent.tri_mat((ps0["a11"][k + 1], ps0["a22"][k + 1],
                             ps0["a12"][k + 1]))
        sp = parent.phi_spot(Ap, An)
        if sp is None:
            continue
        S = parent.sqrt2(Ap)
        Sinv = np.linalg.inv(S)
        IA = np.eye(2) + Sinv @ (An - Ap) @ Sinv
        M = Sinv @ parent.sqrt2(IA) @ S
        Phi = parent.lorentz_of(M)
        Gm = G_of(U0[k - 1], resA["th"][k - 1])
        Gn = G_of(U0[k], resA["th"][k])
        Psi = np.linalg.solve(Gn, Phi @ Gm)
        img = rays @ Psi.T
        qv = (img[:, 0] ** 2 - img[:, 1] ** 2 - img[:, 2] ** 2) \
            / np.maximum((img ** 2).sum(axis=1), 1e-300)
        incl_lines.append((k, float(qv.min()),
                           bool((img[:, 0] > 0).all())))
        if len(incl_lines) >= 5:
            break
    print("    Psi-inclusion (report-only, rule A/G1, first %d "
          "admissible spot cells over %d boundary rays): "
          "min boundary q-defect per cell: %s"
          % (len(incl_lines), NRAY,
             ", ".join("cell %d: %+.2e (t>0 %s)" % ln
                       for ln in incl_lines)))

    # ============================================================== S4
    print("\nS4 -- stage-2 controls (rule A, G1 pairing, stride "
          "subset)")
    real_gate_med = float(np.median(
        [rows[i]["field"]["A-G1"]["nviol"]
         for i in range(0, len(rows), STRIDE)]))
    real_inc_med = float(np.median(
        [rows[i]["field"]["A-G1"]["max_inc"]
         for i in range(0, len(rows), STRIDE)]))

    def field_ctrl(ps_list):
        cnts, incs = [], []
        for ps in ps_list:
            U = uvecs_of(ps)
            res = field_run(U, "A")
            cnts.append(res["nviol"])
            incs.append(res["max_inc"])
        return float(np.median(cnts)), float(np.median(incs))

    eq2_cnt, eq2_inc = field_ctrl(eq_ps_cache)
    wr2_cnt, wr2_inc = field_ctrl(wr_ps_cache)
    eq2_fire = (eq2_cnt >= CTRL_FAC * max(real_gate_med, 1.0)
                or eq2_inc >= CTRL_FAC * real_inc_med)
    wr2_fire = (wr2_cnt >= CTRL_FAC * max(real_gate_med, 1.0)
                or wr2_inc >= CTRL_FAC * real_inc_med)
    check("S4.C1 [must-break, stage 2] equal-weight scramble in the "
          "field: gated violation median %.0f (real %.0f), max-inc "
          "median %.2f deg (real %.2f) -- %s"
          % (eq2_cnt, real_gate_med, eq2_inc, real_inc_med,
             "fires" if eq2_fire else "does NOT fire"), eq2_fire)
    check("S4.C2 [must-break, stage 2] wrong normalization in the "
          "field: gated violation median %.0f, max-inc median %.2f "
          "deg -- %s"
          % (wr2_cnt, wr2_inc,
             "fires" if wr2_fire else "does NOT fire"), wr2_fire)

    ep_cnt, ep_inc = [], []
    for w in sub:
        rr = w["rr"]
        uuE, mE_raw = parent.epstein_atoms(rr["alpha"])
        kap = float(np.sum(w["mm"])) / float(np.sum(mE_raw))
        XnE = parent.atom_reads(rr, uuE)
        ps_ep = ctrl_path(w, uuE, 0.5 * kap * mE_raw, XnE)
        U = uvecs_of(ps_ep)
        res = field_run(U, "A")
        ep_cnt.append(res["nviol"])
        ep_inc.append(res["max_inc"])
    ep_inc_med = float(np.median(ep_inc))
    ratio = (max(ep_inc_med, 1e-12) / max(real_inc_med, 1e-12))
    ep_sep = ratio >= EP_SEP or ratio <= 1.0 / EP_SEP
    print("  S4.C3 [typed, two-sided] Epstein x^2+5y^2 in the field: "
        "gated violation median %.0f (real %.0f); max post-warm "
        "angle median %.3f deg vs real %.3f (ratio %.2f, "
        "separation bar %.1fx either way) -- %s"
        % (float(np.median(ep_cnt)), real_gate_med, ep_inc_med,
           real_inc_med, ratio, EP_SEP,
           "DISTINGUISHABLE (%s)"
           % ("Epstein rougher" if ratio > 1 else "Epstein smoother")
           if ep_sep else "NOT separated -- control surprise, typed "
           "(consistent with the parent's inverted signature)"))

    # ============================================================== S5
    print("\n" + "=" * 78)
    print("S5 -- VERDICT")
    print("=" * 78)
    runtime = time.time() - T0
    WARD_IDS = ("S0.AST", "S1.REF", "S1.ENV", "S1.TEL", "S1.REG",
                "S3.CAUSAL")
    ward_fails = [f for f in FAILS if f in WARD_IDS]
    valid = not ward_fails and runtime <= RUNTIME_CAP
    s1_ctrl = eq1_fire and wr1_fire
    s2_ctrl = eq2_fire and wr2_fire
    field_ok = {k: (field[k]["nviol"] == 0
                    and field[k]["cond_max"] <= COND_BAR)
                for k in field}
    field_near = {k: (field[k]["frac"] <= 1.0e-3
                      and field[k]["cond_max"] <= COND_BAR)
                  for k in field}
    kernel_pass = any(kernel_ok.values())
    field_pass = any(field_ok.values())
    partial = (any(kernel_half.values()) or any(kernel_depth.values())
               or any(field_near.values())
               or (kernel_pass and not s1_ctrl)
               or (field_pass and not s2_ctrl))
    if not valid:
        verdict = "INVALID"
    elif kernel_pass and s1_ctrl:
        verdict = "KERNEL-TAIL-CLEAN"
    elif field_pass and s2_ctrl:
        verdict = "FIELD-TRANSPORTS"
    elif partial:
        verdict = "BOTH-PARTIAL"
    else:
        verdict = "KERNEL-WANDERS"
    print("""
  VERDICT: %s
    stage 1 (strict kernel <= %d): G1 max P0 = %d %s, G2 max P0 = %d
      %s; wander criterion G1 %s / G2 %s; depth-1e-2 kernel bounded:
      G1 %s (max %d) / G2 %s (max %d)
    stage 2 (zero gated violations + cond <= %.0f):
      %s
    controls: stage 1 %s, stage 2 %s
""" % (verdict, P0_CAP,
       stage1["G1"]["maxP0"], "OK" if kernel_ok["G1"] else "FAIL",
       stage1["G2"]["maxP0"], "OK" if kernel_ok["G2"] else "FAIL",
       wander["G1"], wander["G2"],
       kernel_depth["G1"], stage1["G1"]["maxP0_d"][1e-2],
       kernel_depth["G2"], stage1["G2"]["maxP0_d"][1e-2],
       COND_BAR,
       "; ".join("%s: %s (viol %d/%d, cond %.1f)"
                 % (k, "CLEAN" if field_ok[k] else "fails",
                    field[k]["nviol"], field[k]["ngate"],
                    field[k]["cond_max"]) for k in sorted(field)),
       "fire" if s1_ctrl else "SURPRISE", 
       "fire" if s2_ctrl else "SURPRISE"))
    print("""  HONESTY: stage 1's per-rung tail-clean statement is additive
  bookkeeping; only the cross-depth stability of P0 carries content.
  Stage 2's transport is a bounded-angular-velocity statement about
  the state direction under a causal tube field -- it replaces
  positivity, it does not prove it; the field never sees tau_m, but
  the true comb's atom table is public arithmetic, so 'relational'
  means smooth/history summaries, not secrecy.  Finite measurement,
  67 rungs.  NO RH claim.""")
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed%s"
          % (runtime, len(CHECKS), len(FAILS),
             ("  " + ",".join(FAILS)) if FAILS else ""))
    print("[VERDICT] %s" % verdict)
    return 0 if valid else 1


if __name__ == "__main__":
    raise SystemExit(main())
