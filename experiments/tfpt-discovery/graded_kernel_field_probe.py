#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""graded_kernel_field_probe -- PRIME.CELLCONE.GRADEDKERNEL.01
(EXPLORATION ONLY, experiments/; direct follow-up to the
BOTH-PARTIAL verdict of cone_kernel_field_probe /
PRIME.CELLCONE.KERNELFIELD.01, 2026-08-07: decide the graded-kernel
question and give the field teeth).

PARENT FINDINGS (cited; both parent probes imported READ-ONLY, the
construction is bit for bit theirs): the completed-cell flow exits
the fixed Lorentz cone on 67/67 rungs (both groupings); STRICT
violation positions wander with the horizon (P0 ~ X^1.03,
u_P0/(2 alpha) ~ 0.98); G1's violations of relative depth > 1e-2
are confined to n <= 73 on ALL rungs (collapsing to n = 3 at the
top of the 1e-3 census), while G2 has no bounded depth kernel; the
self-calibrating tube field transported cleanly but its must-break
controls also passed (the gate was self-calibrating -- no teeth).

STAGE 1 -- THE GRADED KERNEL LAW (adjudicated on G1, the Stieltjes
completion; G2 runs as the typed mechanism contrast):
  depth of a state = max(0, -lambda_min/lambda_max) (relative).
  (a) DEPTH PROFILE per rung: fit log(depth) vs log(n) on violating
      states (power law) and log(depth) vs n (exponential); the
      winning family by median R^2 is the typed law; plus the
      psi-fluctuation tracker: Spearman correlation between the
      violation depth and |F_k|, F_k = trace(A_k - A_0) = the flow's
      running scalar imbalance (the deployed-units psi(x)-x proxy;
      the inverted-Epstein finding predicts a positive correlation).
  (b) THE GRADED KERNEL FUNCTION P0(eps, X): last position n with
      depth > eps, per rung, for the frozen ladder eps = 1e-1..1e-6;
      per eps: gamma(eps) = log-log slope of max(P0,1) vs
      X = e^{2 alpha}, Kendall over the top half, and M_top(eps) =
      max P0 over the top third of the ladder; eps is RESOLVED iff
      M_top(eps) <= P0_CAP = 100 (the census has collapsed to the
      kernel at the top of the observed range).
      SKIN DEPTH LAW: D(X) = max depth over skin states (position
      u/(2 alpha) >= 0.5), fitted D ~ C X^{-theta}; the decay of D
      is the mechanism that resolves every fixed eps eventually,
      with the predicted threshold X0(eps) = (eps/C)^{-1/theta}.
      FROZEN PASS (KERNEL-GRADED): the resolved set is a nonempty
      UPPER interval of the eps ladder containing 1e-1 AND 1e-2,
      AND the skin decays (theta >= THETA_MIN = 0.1 with Kendall
      (log X, log D) <= -0.5) -- then 'finite kernel + tail' holds
      in the graded form with the typed non-uniform quantifier.
      FROZEN KILL (KERNEL-WANDERS-ALL-DEPTHS): the resolved set is
      EMPTY and every eps has top-half Kendall >= 0.5 (polynomial
      wandering at every depth).  MIXED otherwise (typed).
  (c) G2 MECHANISM: same profiles; plus the predeclared mechanism
      metrics: per-cell interval-centroid offset |mid(I_n) - u_n|
      (mass-matching spreads continuum mass away from the atom) and
      the running imbalance max |F| -- medians G2 vs G1, Spearman
      (offset, depth); the typed mechanism statement.

STAGE 2 -- FIELD TEETH (externally normalized gate):
  The parent field gate was self-calibrating; here every statistic
  is normalized by a FIXED external scale: the flow's OWN certified
  endpoint margin angle th_tau = deg(0.5 asin(clip(dnull_end,0,1))),
  dnull_end = q(u_end)/|u_end|^2 with q = 4 det = 4 tau lambda (the
  tau scale; wardened).  The scramble / Epstein fields are built by
  the SAME rule from THEIR data (their own endpoint scale).  FROZEN
  RULE FAMILY (rule-A tube increments, warm-up NWARM = 12 as the
  parent): T1 = max gated increment / th_tau; T2 = mean gated
  increment / th_tau; T3 = (count of gated increments > KAPPA = 10 x
  th_tau + 1)/ngate; T4 = D_skin/dnull_end (the depth census on the
  tau scale).  SEPARATION per rule = median Q(fake)/median Q(true)
  over the stride-5 subset; STRUCTURAL separation iff the fake's
  endpoint scale is undefined (dnull_end <= 0) on >= half the subset
  while the true is defined on all.  TEETH iff some rule achieves
  finite separation >= SEP = 10; structural-only separation is typed
  FIELD-STRUCTURAL-ONLY (the gate collapses to endpoint positivity
  -- honestly NOT field teeth); no rule >= SEP and no structural =>
  FIELD-NO-TEETH (the moving-cone route has no discriminating
  formulation at this granularity and closes).  If toothed: the
  transport is re-adjudicated = the true flow keeps zero
  self-calibrated membership violations (parent regression) AND
  Q_true x SEP <= Q_fake for the separating rule.  The common-scale
  ratio (both flows on the TRUE th_tau) is reported to type where
  the separation comes from.

CONTROLS: G1/G2 census regressions (frozen exact integers from the
parent run: G1 strict max P0 = 244333, G2 = 283607, G1 depth-1e-2
kernel max = 73, G2 = 77557, exits 67/67 both); scramble depth
profile must differ structurally (skin cells with depth > 1e-2:
median count >= 10 x max(true,1) on the subset); Epstein in-cone
anchor (median strict violation count == 0 on the subset, typed if
not); the tau-scale ward |q_end - 4 tau lambda| rel <= 1e-9.

VERDICT (frozen): KERNEL-GRADED (field sub-verdict typed
separately: FIELD-TOOTHED-TRANSPORTS / FIELD-TOOTHED-NO-TRANSPORT /
FIELD-STRUCTURAL-ONLY / FIELD-NO-TEETH) / KERNEL-WANDERS-ALL-DEPTHS
(the graded kill) / MIXED (typed).  INVALID on ward failure.
SYNTHESIS: the candidate depth-eps theorem verbatim if stage 1
passes, else the obituary.  NO RH claim; finite measurement on 67
rungs; writes nothing; nothing outside experiments/.

FIREWALL: parents + v563 imported READ-ONLY; no zero/prime-table
loaders (AST-checked); NO RNG; runtime cap 1800 s predeclared.

DECLARED IMPLEMENTATION CORRECTIONS (post-freeze, documented):
(1) the S3 interval-centroid computation initially assumed K+1
break edges; the parent convention is K right edges with the left
edge U0 implicit -- fixed to mid_j = (left_j + b_j)/2, left_1 = U0.
Purely a shape convention in a report-only mechanism metric.
(2) the tau-scale ward bar 1e-9 ignored the det-cancellation
conditioning: q_end = 4 det(A_end) at tau/lambda ~ 3e-8 amplifies
the 3.4e-15 telescoping noise by lambda/tau to ~5e-8 relative --
the identity is exact, the bar was mis-calibrated.  Corrected to
the conditioning-aware bar rel <= max(1e-9, 1e3 * eps_mach *
lambda_end/tau) per rung (a genuine normalization error would show
O(1)).  No structural bar changed; the first run's failure and this
correction are declared here.

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/graded_kernel_field_probe.py
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

import v563_paper2_readouts as core             # noqa: E402 (READ-ONLY)
import cell_cone_transport_probe as parent      # noqa: E402 (READ-ONLY)
import cone_kernel_field_probe as probe3        # noqa: E402 (READ-ONLY)

FROZEN_SPEC = """\
PRIME.CELLCONE.GRADEDKERNEL.01 spec v1 (2026-08-07, frozen before
the run).  Ladder/objects/groupings = PRIME.CELLCONE.TRANSPORT.01
verbatim (parents imported read-only).  depth = max(0, -lmin/lmax).
WARDS: tau refs kz 9/12/13 rel <= 1e-4; envelope >= 4.335*0.999;
telescoping rel <= 1e-9; tau-scale identity |q_end - 4 tau lambda|
rel <= 1e-9 per rung; census regressions EXACT (G1 strict maxP0
244333, G2 283607, G1 K(1e-2) 73, G2 K(1e-2) 77557, exits 67/67
both groupings).  STAGE 1 (adjudicated on G1): eps ladder {1e-1,
1e-2, 1e-3, 1e-4, 1e-5, 1e-6}; P0(eps, rung) = last n with depth >
eps; M_top(eps) = max over the top third (alpha order); RESOLVED
iff M_top <= P0_CAP = 100; skin = states with u/(2 alpha) >= 0.5;
D(rung) = max skin depth; fit log D vs log X -> theta;
KERNEL-GRADED iff resolved set = upper interval containing {1e-1,
1e-2} AND theta >= 0.1 AND Kendall(log X, log D) <= -0.5;
KERNEL-WANDERS-ALL-DEPTHS iff resolved set empty AND all-eps
top-half Kendall >= 0.5; MIXED else.  Depth profile: per-rung OLS
log depth vs log n (power) vs log depth vs n (exp), winner by
median R^2; psi-tracker = Spearman(depth, |F|) on violating cells
(subsample <= 2000, deterministic); mechanism metrics = interval
centroid offset + max |F|, G2 vs G1.  STAGE 2 (stride-5 subset,
rule-A tube, NWARM = 12): own-scale th_tau = deg(0.5 asin
clip(dnull_end, 0, 1)); rules T1 max-inc/th_tau, T2 mean-inc/
th_tau, T3 (count inc > 10 th_tau + 1)/ngate, T4 D_skin/dnull_end;
separation = med Q(scramble)/med Q(true), SEP = 10; structural iff
scramble dnull_end <= 0 on >= half subset & true defined on all;
FIELD-TOOTHED iff finite separation >= SEP for some rule;
structural-only => FIELD-STRUCTURAL-ONLY; else FIELD-NO-TEETH;
toothed transport iff parent membership regression clean AND
Q_true x SEP <= Q_fake.  Epstein: same rules, typed two-sided, bar
SEP, non-gating anchor (in-cone regression median strict count ==
0).  Scramble depth-profile control: median skin count depth >
1e-2 >= 10 x max(true median, 1).  VERDICT: KERNEL-GRADED (+ field
typed) / KERNEL-WANDERS-ALL-DEPTHS / MIXED; INVALID on wards.  No
prediction frozen for the outcomes.  NO RH claim; writes nothing.
"""

STRIDE = 5
TAU_REFS = {9: 5.984165e-4, 12: 4.351189e-4, 13: 5.637632e-4}
TAU_REF_REL = 1.0e-4
ENV_C = 4.335
ENV_GUARD = 0.999
WARD_REL = 1.0e-9
REG_EXACT = dict(G1_strict=244333, G2_strict=283607,
                 G1_k2=73, G2_k2=77557)
EPS_LADDER = (1.0e-1, 1.0e-2, 1.0e-3, 1.0e-4, 1.0e-5, 1.0e-6)
P0_CAP = 100
SKIN_POS = 0.5
THETA_MIN = 0.1
KEN_BAR = 0.5
DEPTH_KER = 1.0e-2
NSUB = 2000
NWARM = probe3.NWARM
KAPPA = 10.0
SEP = 10.0
RUNTIME_CAP = 1800.0
BANNED_IDS = parent.BANNED_IDS if hasattr(parent, "BANNED_IDS") else (
    "zetazero", "nzeros", "primerange", "isprime", "primepi",
    "nextprime", "prevprime", "find_zeros", "second_sheet_zero")

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


def spearman(x, y):
    x = np.asarray(x, float)
    y = np.asarray(y, float)
    rx = np.argsort(np.argsort(x)).astype(float)
    ry = np.argsort(np.argsort(y)).astype(float)
    rx -= rx.mean()
    ry -= ry.mean()
    d = math.sqrt(float((rx * rx).sum()) * float((ry * ry).sum()))
    return float((rx * ry).sum() / d) if d > 0 else 0.0


def ols_fit(x, y):
    """slope, intercept, R^2 of y on x."""
    x = np.asarray(x, float)
    y = np.asarray(y, float)
    b, q = np.polyfit(x, y, 1)
    pred = b * x + q
    ssr = float(((y - pred) ** 2).sum())
    sst = max(float(((y - y.mean()) ** 2).sum()), 1e-300)
    return float(b), float(q), 1.0 - ssr / sst


def subsample(idx):
    if len(idx) <= NSUB:
        return idx
    sel = np.unique(np.linspace(0, len(idx) - 1, NSUB).astype(int))
    return idx[sel]


def dnull_end_of(ps):
    t = float(ps["a11"][-1] + ps["a22"][-1])
    x = float(ps["a11"][-1] - ps["a22"][-1])
    y = 2.0 * float(ps["a12"][-1])
    q = t * t - x * x - y * y
    return q / max(t * t + x * x + y * y, 1e-300), q


def skin_depth(ps, uu, alpha):
    depth = np.maximum(0.0, -ps["lmin"][1:]
                       / np.maximum(ps["lmax"][1:], 1e-300))
    skin = (uu / (2.0 * alpha)) >= SKIN_POS
    return (float(depth[skin].max()) if skin.any() else 0.0, depth,
            skin)


def toothed_stats(ps, uu, alpha):
    """Externally normalized field statistics for one flow (own
    endpoint scale).  Returns dict or scale=None if undefined."""
    U = probe3.uvecs_of(ps)
    res = probe3.field_run(U, "A")
    ang = res["ang"][res["gated"]]
    nd, _q = dnull_end_of(ps)
    D, _, _ = skin_depth(ps, uu, alpha)
    out = dict(nviol_self=res["nviol"], max_inc=float(ang.max()),
               mean_inc=float(ang.mean()), ngate=len(ang),
               nd=nd, D=D)
    if nd <= 0.0:
        out["scale"] = None
        return out
    th = math.degrees(0.5 * math.asin(min(1.0, nd)))
    out["scale"] = th
    out["T1"] = out["max_inc"] / th
    out["T2"] = out["mean_inc"] / th
    out["T3"] = (float(np.sum(ang > KAPPA * th)) + 1.0) / len(ang)
    out["T4"] = D / nd
    return out


def main():
    spec_hash = hashlib.sha256(FROZEN_SPEC.encode()).hexdigest()
    print("=" * 78)
    print("PRIME.CELLCONE.GRADEDKERNEL.01 -- graded kernel law + "
          "field teeth")
    print("=" * 78)
    print(FROZEN_SPEC)
    print("SPEC sha256          : %s" % spec_hash)
    print("toothed-gate sha256  : %s" % hashlib.sha256(
        inspect.getsource(toothed_stats).encode()).hexdigest())
    print("parent field sha256  : %s (reused read-only)"
          % hashlib.sha256(inspect.getsource(
              probe3.field_run).encode()).hexdigest()[:16])

    # ============================================================== S0
    print("\nS0 -- firewall")
    check("S0.AST no zero/prime-table loader; parents read-only; "
          "NO RNG", ast_zero_firewall(__file__))

    # ============================================================== S1
    print("\nS1 -- ladder + wards + exact census regressions")
    rows = []
    for kz in core.frame_a_zones():
        rr = core.build_window(kz)
        if rr["h"] == parent.ANOMALOUS_H:
            continue
        if math.exp(2.0 * rr["alpha"]) > core.ATOM_MAX + 0.5:
            continue
        rows.append(dict(rr=rr, h=rr["h"], alpha=rr["alpha"],
                         X=math.exp(2.0 * rr["alpha"]),
                         tau=parent.eig2_min(rr["Ah"])))
    rows.sort(key=lambda w: w["alpha"])
    ref_ok = all(abs(parent.eig2_min(core.build_window(kz)["Ah"])
                     - tr) / tr <= TAU_REF_REL
                 for kz, tr in TAU_REFS.items())
    check("S1.REF tau references reproduce (bar %.0e)" % TAU_REF_REL,
          ref_ok)

    env_min = float("inf")
    tel_worst = 0.0
    tau_ward_worst = 0.0
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
        env_min = min(env_min, (w["tau"] / parent.eig2_min(A0))
                      * w["h"] ** 1.5)
        uu, lam, Xn = rr["uu"], rr["lam"], rr["Xn"]
        w["mm"] = 2.0 * lam
        w["nn"] = np.rint(np.exp(uu)).astype(np.int64)
        lam_end = float(np.linalg.eigvalsh(rr["Ah"])[-1])
        for g in ("G1", "G2"):
            b = (parent.breaks_G1(uu, rr["alpha"]) if g == "G1"
                 else parent.breaks_G2(w["mm"], rr["alpha"]))
            Chat = parent.cell_increments(edges, reads, b)
            deltas = Chat - lam[:, None] * Xn
            ps = parent.path_stats((A0[0, 0], A0[1, 1], A0[0, 1]),
                                   deltas)
            Aend = parent.tri_mat((ps["a11"][-1], ps["a22"][-1],
                                   ps["a12"][-1]))
            tel_worst = max(tel_worst, float(np.max(np.abs(
                Aend - rr["Ah"]))) / float(np.max(np.abs(rr["Ah"]))))
            if bool(np.all(ps["lmin"] > 0.0)):
                exit_ok = False
            nd, q_end = dnull_end_of(ps)
            # conditioning-aware normalization (declared correction
            # (2)): the det cancellation amplifies fp noise by
            # lambda/tau
            bar_rung = max(WARD_REL, 1.0e3 * np.finfo(float).eps
                           * lam_end / w["tau"])
            tau_ward_worst = max(tau_ward_worst, (abs(
                q_end - 4.0 * w["tau"] * lam_end)
                / (4.0 * w["tau"] * lam_end)) / bar_rung)
            w[g] = dict(ps=ps, deltas=deltas, breaks=b, nd=nd)
    check("S1.ENV envelope min e1 = %.4f >= %.4f"
          % (env_min, ENV_C * ENV_GUARD), env_min >= ENV_C * ENV_GUARD)
    check("S1.TEL telescoping worst rel %.2e (bar %.0e)"
          % (tel_worst, WARD_REL), tel_worst <= WARD_REL)
    check("S1.TAU tau-scale identity q_end = 4 tau lambda, worst "
          "bar-normalized %.2e <= 1 (conditioning-aware bar, "
          "declared correction (2))" % tau_ward_worst,
          tau_ward_worst <= 1.0)

    # depth arrays + strict/graded censuses
    for w in rows:
        for g in ("G1", "G2"):
            ps = w[g]["ps"]
            depth = np.maximum(0.0, -ps["lmin"][1:]
                               / np.maximum(ps["lmax"][1:], 1e-300))
            w[g]["depth"] = depth
            w[g]["P0"] = {}
            for eps in EPS_LADDER:
                mk = depth > eps
                w[g]["P0"][eps] = int(w["nn"][np.where(mk)[0][-1]]) \
                    if mk.any() else 0
            strict = ps["lmin"][1:] <= 0.0
            w[g]["strict_P0"] = int(w["nn"][np.where(strict)[0][-1]]) \
                if strict.any() else 0
            F = np.cumsum(w[g]["deltas"][:, 0] + w[g]["deltas"][:, 1])
            w[g]["F"] = F
    reg_ok = (max(w["G1"]["strict_P0"] for w in rows)
              == REG_EXACT["G1_strict"]
              and max(w["G2"]["strict_P0"] for w in rows)
              == REG_EXACT["G2_strict"]
              and max(w["G1"]["P0"][DEPTH_KER] for w in rows)
              == REG_EXACT["G1_k2"]
              and max(w["G2"]["P0"][DEPTH_KER] for w in rows)
              == REG_EXACT["G2_k2"])
    check("S1.REG parent censuses reproduce EXACTLY (G1/G2 strict "
          "maxP0 %d/%d, depth-1e-2 kernels %d/%d) + exits 67/67"
          % (max(w["G1"]["strict_P0"] for w in rows),
             max(w["G2"]["strict_P0"] for w in rows),
             max(w["G1"]["P0"][DEPTH_KER] for w in rows),
             max(w["G2"]["P0"][DEPTH_KER] for w in rows)),
          reg_ok and exit_ok)

    # ============================================================== S2
    print("\nS2 -- STAGE 1: the graded kernel law")
    aas = [w["alpha"] for w in rows]
    Xs = [w["X"] for w in rows]
    third = max(len(rows) // 3, 1)
    half = len(rows) // 2
    stage1 = {}
    for g in ("G1", "G2"):
        print("\n  grouping %s -- P0(eps, X) census "
              "(eps columns %s):" % (g, ", ".join(
                  "%.0e" % e for e in EPS_LADDER)))
        print("    %5s %7s %9s | %s" % ("h", "alpha", "X", " ".join(
            "%8s" % ("P0@%.0e" % e) for e in EPS_LADDER)))
        for w in rows:
            print("    %5d %7.3f %9.0f | %s"
                  % (w["h"], w["alpha"], w["X"], " ".join(
                      "%8d" % w[g]["P0"][e] for e in EPS_LADDER)))
        res_eps = {}
        print("    per-eps laws:")
        for eps in EPS_LADDER:
            p0 = np.array([w[g]["P0"][eps] for w in rows], float)
            m_top = int(p0[-third:].max())
            nz = p0 > 0
            if nz.sum() >= 5:
                gam, _, r2 = ols_fit(np.log(np.array(Xs)[nz]),
                                     np.log(p0[nz]))
            else:
                gam, r2 = float("nan"), float("nan")
            kt = kendall_tau([math.log(x) for x in Xs[-half:]],
                             [math.log(max(v, 1.0))
                              for v in p0[-half:]])
            resolved = m_top <= P0_CAP
            res_eps[eps] = dict(m_top=m_top, gam=gam, kt=kt,
                                resolved=resolved,
                                gmax=int(p0.max()))
            print("      eps %.0e: global max P0 %8d, M_top %8d "
                  "-> %-11s gamma %5s (R^2 %s), top-half Kendall "
                  "%+.2f"
                  % (eps, int(p0.max()), m_top,
                     "RESOLVED" if resolved else "unresolved",
                     ("%.2f" % gam) if math.isfinite(gam) else "--",
                     ("%.2f" % r2) if math.isfinite(r2) else "--",
                     kt))
        # skin depth law
        Ds = []
        for w in rows:
            D, _, _ = skin_depth(w[g]["ps"], w["rr"]["uu"],
                                 w["alpha"])
            Ds.append(max(D, 1e-300))
        th_sl, th_ic, th_r2 = ols_fit(np.log(Xs), np.log(Ds))
        kt_D = kendall_tau([math.log(x) for x in Xs],
                           [math.log(d) for d in Ds])
        theta = -th_sl
        C_D = math.exp(th_ic)
        nd_ratio = float(np.median(
            [Ds[i] / max(rows[i][g]["nd"], 1e-300)
             for i in range(len(rows))]))
        print("    SKIN DEPTH LAW (%s): D(X) ~ %.3g * X^-%.3f "
              "(R^2 %.2f, Kendall %+.2f); median D/dnull_end = %.1f "
              "(the skin vs the certified tau scale); predicted "
              "X0(eps) = (eps/C)^(-1/theta): X0(1e-3) ~ %.1e, "
              "X0(1e-4) ~ %.1e"
              % (g, C_D, theta, th_r2, kt_D, nd_ratio,
                 (1e-3 / C_D) ** (-1.0 / theta) if theta > 0 else
                 float("inf"),
                 (1e-4 / C_D) ** (-1.0 / theta) if theta > 0 else
                 float("inf")))
        # depth profile law (a)
        sl_pow, r2_pow, r2_exp, sp_F = [], [], [], []
        for w in rows:
            depth = w[g]["depth"]
            idx = np.where(depth > 0.0)[0]
            if len(idx) < 8:
                continue
            idx = subsample(idx)
            ln_n = np.log(w["nn"][idx].astype(float))
            ln_d = np.log(depth[idx])
            b1, _, rp = ols_fit(ln_n, ln_d)
            _, _, re = ols_fit(w["nn"][idx].astype(float), ln_d)
            sl_pow.append(b1)
            r2_pow.append(rp)
            r2_exp.append(re)
            sp_F.append(spearman(depth[idx],
                                 np.abs(w[g]["F"][idx])))
        fam = "POWER" if np.median(r2_pow) >= np.median(r2_exp) \
            else "EXPONENTIAL"
        print("    DEPTH PROFILE (%s): depth(n) ~ n^%.2f (median "
              "slope; median R^2 power %.2f vs exp %.2f -> %s "
              "family); psi-tracker Spearman(depth, |F|) median "
              "%+.2f over rungs"
              % (g, float(np.median(sl_pow)),
                 float(np.median(r2_pow)), float(np.median(r2_exp)),
                 fam, float(np.median(sp_F))))
        stage1[g] = dict(res_eps=res_eps, theta=theta, C_D=C_D,
                         th_r2=th_r2, kt_D=kt_D,
                         sp_F=float(np.median(sp_F)),
                         slope_pow=float(np.median(sl_pow)), fam=fam)

    r1 = stage1["G1"]["res_eps"]
    flags = [r1[e]["resolved"] for e in EPS_LADDER]   # eps descending
    upper_interval = all(flags[:flags.index(False)]) \
        if False in flags else True
    nonempty_top2 = flags[0] and flags[1]
    decay_ok = (stage1["G1"]["theta"] >= THETA_MIN
                and stage1["G1"]["kt_D"] <= -KEN_BAR)
    graded = nonempty_top2 and upper_interval and decay_ok
    wander_all = (not any(flags)) and all(
        r1[e]["kt"] >= KEN_BAR for e in EPS_LADDER)
    print("\n  STAGE-1 GATES (G1): resolved flags %s (upper interval "
          "%s, {1e-1,1e-2} resolved %s); skin decay theta = %.3f "
          "(>= %.1f: %s), Kendall %+.2f (<= -%.1f: %s) => "
          "KERNEL-GRADED %s / WANDERS-ALL-DEPTHS %s"
          % (["%d" % f for f in flags], upper_interval, nonempty_top2,
             stage1["G1"]["theta"], THETA_MIN,
             stage1["G1"]["theta"] >= THETA_MIN, stage1["G1"]["kt_D"],
             KEN_BAR, stage1["G1"]["kt_D"] <= -KEN_BAR,
             graded, wander_all))

    # ============================================================== S3
    print("\nS3 -- the G2 mechanism (typed contrast)")
    off_med = {}
    sp_off = {}
    Fmax_med = {}
    for g in ("G1", "G2"):
        offs_all, sps, fmaxs = [], [], []
        for w in rows:
            b = w[g]["breaks"]
            # parent convention: b = the K right edges, left edge U0
            # implicit -- I_j = (left_j, b_j]
            left = np.concatenate([[parent.U0], b[:-1]])
            mid = 0.5 * (left + b)
            off = np.abs(mid - w["rr"]["uu"])
            offs_all.append(float(np.median(off)))
            fmaxs.append(float(np.max(np.abs(w[g]["F"]))))
            idx = np.where(w[g]["depth"] > 0.0)[0]
            if len(idx) >= 8:
                idx = subsample(idx)
                sps.append(spearman(off[idx], w[g]["depth"][idx]))
        off_med[g] = float(np.median(offs_all))
        sp_off[g] = float(np.median(sps))
        Fmax_med[g] = float(np.median(fmaxs))
    print("    interval-centroid offset |mid(I_n) - u_n| median: "
          "G1 %.4f vs G2 %.4f (ratio %.1f); Spearman(offset, depth) "
          "median: G1 %+.2f vs G2 %+.2f; running imbalance max |F| "
          "median: G1 %.3f vs G2 %.3f (ratio %.1f)"
          % (off_med["G1"], off_med["G2"],
             off_med["G2"] / max(off_med["G1"], 1e-300),
             sp_off["G1"], sp_off["G2"], Fmax_med["G1"],
             Fmax_med["G2"],
             Fmax_med["G2"] / max(Fmax_med["G1"], 1e-300)))
    print("    typed mechanism: G2's mass-matched intervals sit "
          "further from their atoms and carry a larger running "
          "imbalance -- the compensation is delayed, the violation "
          "mass spreads into the window instead of collapsing onto "
          "the small-n kernel (numbers above; kernel censuses in "
          "S2).")

    # ============================================================== S4
    print("\nS4 -- STAGE 2: field teeth (externally normalized "
          "gate, stride-%d subset)" % STRIDE)
    sub = rows[::STRIDE]

    def flow_ps(w, uuX, lamX, XnX):
        rr = w["rr"]
        b = parent.breaks_G1(uuX, rr["alpha"])
        Chat = parent.cell_increments(w["edges"], w["reads"], b)
        deltas = Chat - lamX[:, None] * XnX
        A0 = w["A0"]
        return parent.path_stats((A0[0, 0], A0[1, 1], A0[0, 1]),
                                 deltas)

    stats = dict(true=[], scr=[], eps=[])
    scr_strict, eps_strict = [], []
    scr_skin, true_skin = [], []
    for w in sub:
        rr = w["rr"]
        uu = rr["uu"]
        st_t = toothed_stats(w["G1"]["ps"], uu, w["alpha"])
        stats["true"].append(st_t)
        _, dep_t, skin_t = skin_depth(w["G1"]["ps"], uu, w["alpha"])
        true_skin.append(int(np.sum((dep_t > DEPTH_KER) & skin_t)))
        mm_eq = np.full(len(uu), float(np.sum(w["mm"])) / len(uu))
        ps_s = flow_ps(w, uu, 0.5 * mm_eq, rr["Xn"])
        stats["scr"].append(toothed_stats(ps_s, uu, w["alpha"]))
        scr_strict.append(int(np.sum(ps_s["lmin"][1:] <= 0.0)))
        _, dep_s, skin_s = skin_depth(ps_s, uu, w["alpha"])
        scr_skin.append(int(np.sum((dep_s > DEPTH_KER) & skin_s)))
        uuE, mE_raw = parent.epstein_atoms(rr["alpha"])
        kap = float(np.sum(w["mm"])) / float(np.sum(mE_raw))
        XnE = parent.atom_reads(rr, uuE)
        ps_e = flow_ps(w, uuE, 0.5 * kap * mE_raw, XnE)
        stats["eps"].append(toothed_stats(ps_e, uuE, w["alpha"]))
        eps_strict.append(int(np.sum(ps_e["lmin"][1:] <= 0.0)))

    true_def = [s for s in stats["true"] if s["scale"] is not None]
    scr_undef = sum(1 for s in stats["scr"] if s["scale"] is None)
    structural = (scr_undef >= len(sub) / 2.0
                  and len(true_def) == len(sub))
    print("    endpoint scales: true th_tau defined %d/%d (median "
          "%.2e deg); scramble undefined (endpoint out of cone) on "
          "%d/%d; Epstein undefined on %d/%d"
          % (len(true_def), len(sub),
             float(np.median([s["scale"] for s in true_def]))
             if true_def else float("nan"),
             scr_undef, len(sub),
             sum(1 for s in stats["eps"] if s["scale"] is None),
             len(sub)))

    seps, seps_ep = {}, {}
    for Tn in ("T1", "T2", "T3", "T4"):
        qt = [s[Tn] for s in stats["true"] if s["scale"] is not None]
        qs = [s[Tn] for s in stats["scr"] if s["scale"] is not None]
        qe = [s[Tn] for s in stats["eps"] if s["scale"] is not None]
        mt = float(np.median(qt)) if qt else float("nan")
        seps[Tn] = (float(np.median(qs)) / mt) if (qs and mt > 0) \
            else float("inf") if structural else float("nan")
        seps_ep[Tn] = (float(np.median(qe)) / mt) if (qe and mt > 0) \
            else float("nan")
        print("    rule %s: Q_true median %10.3g | scramble "
              "separation %8s | Epstein ratio %8s"
              % (Tn, mt,
                 ("%.2f" % seps[Tn]) if math.isfinite(seps[Tn])
                 else ("STRUCT" if structural else "--"),
                 ("%.2f" % seps_ep[Tn])
                 if math.isfinite(seps_ep[Tn]) else "--"))
    common = (float(np.median([s["max_inc"] for s in stats["scr"]]))
              / max(float(np.median([s["max_inc"]
                                     for s in stats["true"]])),
                    1e-300))
    print("    common-scale (true th_tau on both) max-inc ratio: "
          "%.2f -- where the separation does NOT come from"
          % common)

    finite_teeth = [Tn for Tn in seps
                    if math.isfinite(seps[Tn]) and seps[Tn] >= SEP]
    if finite_teeth:
        best = max(finite_teeth, key=lambda t: seps[t])
        member_ok = all(s["nviol_self"] == 0 for s in stats["true"])
        transport = member_ok and seps[best] >= SEP
        field_verdict = ("FIELD-TOOTHED-TRANSPORTS" if transport
                         else "FIELD-TOOTHED-NO-TRANSPORT")
        detail = ("rule %s separates x%.1f (bar %.0f); membership "
                  "regression %s" % (best, seps[best], SEP,
                                     "clean" if member_ok else
                                     "BROKEN"))
    elif structural:
        field_verdict = "FIELD-STRUCTURAL-ONLY"
        detail = ("scramble cannot define its own certified scale "
                  "(endpoint out on %d/%d) -- the gate collapses to "
                  "endpoint positivity, honestly NOT field teeth"
                  % (scr_undef, len(sub)))
    else:
        field_verdict = "FIELD-NO-TEETH"
        detail = ("best finite separation %.2f < %.0f; the "
                  "moving-cone route has no discriminating "
                  "formulation at this granularity and closes"
                  % (max(v for v in seps.values()
                         if math.isfinite(v)), SEP))
    print("    FIELD SUB-VERDICT: %s (%s)" % (field_verdict, detail))

    # ============================================================== S5
    print("\nS5 -- controls")
    scr_fire = (float(np.median(scr_skin))
                >= 10.0 * max(float(np.median(true_skin)), 1.0))
    check("S5.C1 [must-differ] scramble depth profile is "
          "scale-free/everywhere: median skin cells with depth > "
          "%.0e = %.0f vs true %.0f (x10 needed) -- %s"
          % (DEPTH_KER, float(np.median(scr_skin)),
             float(np.median(true_skin)),
             "fires" if scr_fire else "does NOT fire"), scr_fire)
    ep_incone = float(np.median(eps_strict)) == 0.0
    print("  S5.C2 [anchor, typed] Epstein in-cone regression: "
          "median strict violation count %.0f (0 expected) -- %s"
          % (float(np.median(eps_strict)),
             "reproduces (the contrast anchor holds)" if ep_incone
             else "SURPRISE, typed"))

    # ============================================================== S6
    print("\n" + "=" * 78)
    print("S6 -- VERDICT + SYNTHESIS")
    print("=" * 78)
    runtime = time.time() - T0
    WARD_IDS = ("S0.AST", "S1.REF", "S1.ENV", "S1.TEL", "S1.TAU",
                "S1.REG")
    ward_fails = [f for f in FAILS if f in WARD_IDS]
    valid = not ward_fails and runtime <= RUNTIME_CAP
    if not valid:
        verdict = "INVALID"
    elif graded:
        verdict = "KERNEL-GRADED"
    elif wander_all:
        verdict = "KERNEL-WANDERS-ALL-DEPTHS"
    else:
        verdict = "MIXED"
    print("\n  VERDICT: %s   (field: %s; scramble depth control %s; "
          "Epstein anchor %s)"
          % (verdict, field_verdict,
             "fires" if scr_fire else "SURPRISE",
             "holds" if ep_incone else "SURPRISE"))
    if verdict == "KERNEL-GRADED":
        print("""
  CANDIDATE STATEMENT (verbatim, the depth-eps cone; G1/Stieltjes
  completion; measured on 67 rungs, NOT proven, NOT uniform in eps,
  NOT an RH claim):
    "For every eps > 0 there exist finite P0(eps) and X0(eps) such
     that for every window X >= X0(eps), every state of the
     completed-cell flow beyond n = P0(eps) has relative depth
     -lambda_min/lambda_max <= eps.  Measured witnesses: P0(1e-1) =
     0, P0(1e-2) <= %d (collapsing to {2,3} above alpha ~ 3.9);
     skin depth D(X) ~ %.3g X^-%.3f (R^2 %.2f) predicts X0(eps) ~
     (eps/%.3g)^(-1/%.3f); the strict (eps -> 0) census wanders
     with the horizon (P0 ~ X^1.03 at relative position 0.98) --
     the wandering is vanishing-depth skin, not kernel growth."
  SURVIVES: the graded kernel law above + the exact congruence
  calculus (telescoping exact to 1e-13) + the ray cascade
  (RAY-EDGE-CONFIRMED, parent).  The fixed-cone layer statement
  stays dead; the field is typed %s."""
              % (REG_EXACT["G1_k2"], stage1["G1"]["C_D"],
                 stage1["G1"]["theta"], stage1["G1"]["th_r2"],
                 stage1["G1"]["C_D"], stage1["G1"]["theta"],
                 field_verdict))
    elif verdict == "KERNEL-WANDERS-ALL-DEPTHS":
        print("""
  OBITUARY: the violation positions grow polynomially in X at every
  depth of the eps ladder -- the wandering is real, not
  vanishing-depth noise; package D is dead in graded form too.
  What survives regardless: the exact congruence calculus and the
  ray cascade.  Field: %s.""" % field_verdict)
    else:
        print("""
  MIXED (typed above): the resolved set / decay law / wander flags
  disagree -- see the S2 gate line for exactly which clause failed;
  the field is typed %s.""" % field_verdict)
    print("""
  HONESTY: 'resolved' is an in-range statement (the census collapsed
  within the observed 67 rungs); the eps < 1e-2 rows are extrapolated
  only through the fitted D(X) law; the toothed gate compares flows
  through their OWN certified scales, so a fake without a certified
  endpoint separates structurally, not dynamically.  NO RH claim.""")
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed%s"
          % (runtime, len(CHECKS), len(FAILS),
             ("  " + ",".join(FAILS)) if FAILS else ""))
    print("[VERDICT] %s" % verdict)
    return 0 if valid else 1


if __name__ == "__main__":
    raise SystemExit(main())
