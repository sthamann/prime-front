#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""pruefer_compensation_probe -- PRIME.PRUEFER.COMPENSATION.01
(EXPLORATION ONLY, experiments/; round-34 PREREGISTRATION,
2026-08-08).

THIS FILE IS A FROZEN PREREGISTRATION CONTRACT.  The decisive
analysis (RUN 1/2/3 on deployed data) is locked behind the
flag file `pruefer_unfreeze.flag` and MUST NOT run before the
round-34 commit; only `--freeze` (spec + SHA + synthetic
machinery wards) is executed at preregistration time.  The
normative contract is the FROZEN_SPEC string below (hashed);
this docstring summarizes it.  NO RH claim anywhere.

Run (preregistration):
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/pruefer_compensation_probe.py --freeze

Run (after the parent creates pruefer_unfreeze.flag):
    ... pruefer_compensation_probe.py --run1   (anatomy)
    ... pruefer_compensation_probe.py --run2   (Cotlar decision)
    ... pruefer_compensation_probe.py --run3   (uniformity candidate)
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

import v563_paper2_readouts as core          # noqa: E402  (READ-ONLY)
import gauss_node_unitary_probe as gnu       # noqa: E402  (READ-ONLY)
import cdcore_probe as cdc                   # noqa: E402  (READ-ONLY)

FROZEN_SPEC = """\
PRIME.PRUEFER.COMPENSATION.01 SPEC v1 (2026-08-08, frozen
BEFORE the round-34 commit; the decisive analysis is locked
behind pruefer_unfreeze.flag and has NOT run at freeze time).

INPUTS (source-only, structural firewall): the two source
Jacobi chains of the folded arm measures nu~_+- (machinery:
gnu.folded_arm_measure + cdc.stieltjes_chain, read-only; the
cdcore / jacobi_pole_uvarov chain conventions); the arm
weights / Christoffel data and the Gauss-frame objects U, D_-
(gnu.gauss_objects); the T_1/T_2 split T_1 = I - U*U, T_2 =
U*(I - D_-^2)U (cd_damping_compensation machinery, read-only).
FORBIDDEN in construction: the computed soft eigenvector,
target eigenvectors/pseudoinverse, any positivity readout
during construction.  Structural firewall: the construction
functions (arm_chain, pruefer_phase, deployed_cells) are
AST-scanned for {softport, esoft, eigh, eigvalsh, pinv, svd}
and must be clean; eigen/SVD readouts happen only AFTER the
cells are fixed.

THE PRUEFER PHASES: for each arm chain (orthonormal three-term
recursion b_{n-1} p_{n-1} + a_n p_n + b_n p_{n+1} = x p_n,
p_0 = 1/sqrt(m0), chain (a, b, m0) from cdc.stieltjes_chain of
the folded arm measure with m_steps = min(h, #support)), the
Prueffer representation u_n = p_n(x), v_n = b_n p_{n+1}(x),
(u_n, v_n) = R_n (cos theta_n, sin theta_n): theta computed
ONLY from the source Jacobi coefficients.  BRANCH/UNWRAPPING
DISCIPLINE (frozen): theta_0 = atan2(v_0, u_0) in (-pi, pi];
for n >= 1 the raw increment atan2(v_n, u_n) -
atan2(v_{n-1}, u_{n-1}) is wrapped to [-pi, pi) and
accumulated (per evaluation point, independently).  PHASE
INDEX (frozen): n* = (#Gauss nodes of that arm) - 2, so that
v_{n*} = b_{n*} p_{n*+1} is nonzero at the arm's own nodes by
interlacing (at n* = m-1 it would vanish identically).  Each
arm's phase is evaluated with ITS OWN chain at ITS OWN Gauss
node set (theta^- = minus chain at minus nodes, theta^+ = plus
chain at plus nodes).  Node-consistency ward at run time:
eig(J_chain) matches cos(theta_node) to 1e-8.

THE FROZEN CELLS: delta_theta_ij = (theta_i^- - theta_j^+)
mod 2 pi in [0, 2 pi); EXACTLY 16 equal-width cells with
boundaries at k pi/8, k = 0..15 (cell r = [r pi/8,
(r+1) pi/8)); FIXED NOW, no posterior width choice.  THE
PAIRING RULE (primary, frozen): the ENTRYWISE partition --
every matrix entry (i, j) of a minus-node x plus-node object
X (X = U and X = C = D_- U) belongs to exactly one cell
r(i,j) = floor(delta_theta_ij / (pi/8)); the pieces X_r keep
entries of cell r and zero the rest; completeness Sum_r X_r =
X exact is a ward.  The secondary two-index variant (blocks
(r, s) = X_r* X_s, i.e. the row/column pair of cells through
the minus-node contraction) is derived from the same pieces;
the entrywise partition is primary.  PREDECLARED DANGER
GEOMETRY: near-phase family DGR1 = cells {0, 15} (|delta
theta| < pi/8 on the circle); resonance family DGR2 = cells
{7, 8} (delta theta near pi); circle distance d(r, s) =
min(|r-s|, 16-|r-s|).

RUN 1 -- ANATOMY (first post-commit run; anchors kz {9, 12,
13, 26, 40}): T_1, T_2, Delta decomposed through the 16
pieces: (a) the 16x16 Gram census g_rs = ||U_r* U_s||_2 and
the danger share = (sum of g_rs with r or s in DGR1 u DGR2) /
(sum of all g_rs); the negativity localization: lam_min(I -
Sum_{r,s in DGR} U_r* U_s) vs lam_min(T_1) -- does the danger
family carry >= 50 percent of |lam_min(T_1)| (frozen bar);
(b) the cell-local inequality with the frozen identity
assignment w_r = ||U_r||_F^2 / ||U||_F^2: eps_r := max(0,
-lam_min(w_r I - U_r* D_-^2 U_r)); the census Sum_r eps_r
(the local compensation defect); (c) the envelope env_X(d) =
max_{d(r,s)=d} ||X_r* X_s||_2 for X in {U, C}: Spearman(env,
d) over d = 0..8 must be <= -0.8 for decay (frozen bar).
RUN 2 -- COTLAR DECISION (the battery = the 42 rungs of the
CD wave, i.e. all frame_a_zones with h <= 900 and plus arm in
gauss mode, PLUS the deep holdouts): all cross norms
||X_r* X_s||_2 and ||X_r X_s*||_2; the Cotlar sums S_X = max_r
Sum_s sqrt(||X_r* X_s||_2), S*_X likewise with X_r X_s*, and
the Cotlar-Stein bound B_X = sqrt(S_X S*_X) for X = U and the
two-channel damped variant X = C = D_- U; DECISION (frozen):
BOUNDED iff max over the deep holdouts <= 1.2 x max over the
42-rung battery AND the least-squares slope of log S vs log h
over battery + holdouts is <= 0.10; GROWING iff that slope
>= 0.20 (power law) OR S vs log h is linear with R^2 >= 0.9
and positive slope (log growth); otherwise PARTIAL (typed).
CONTRAST at kz 9: Epstein (x^2+5y^2, N = floor(e^{2 alpha9})
+1, gnu.lambda_eps) and scramble seed 1 through the SAME
pipeline: their triple (S_U, S_C, danger share) must differ
from truth by >= 25 percent in >= 1 component AND their local
defect Sum_r eps_r must be >= 5 x truth, or their envelope
decay must fail the Spearman bar.
RUN 3 -- UNIFORMITY CANDIDATE (only if RUN 2 gives BOUNDED):
the analytic envelope bound from the source chains.
Derivation sketch (frozen target shape): smooth Jacobi
coefficients (delta_coef = sup_n |a_n - a_{n-1}| + |b_n -
b_{n-1}| small, b_n bounded away from 0) give a Prueffer phase
derivative d theta/d step in (0, pi) with Lipschitz control,
hence quasi-equidistributed relative phases and CD-kernel
decay between phase-separated node pairs; candidate envelope
env_U(d) <= K_1/(1+d), env_C(d) <= K_2/(1+d)^2 (p = 1 for U,
p = 2 for the damped C -- predeclared).  TEST on the frozen
deep holdouts: K_p(h) := max_d env(d) (1+d)^p must be
h-stable (holdout max <= 1.2 x battery max) and delta_coef
h-stable (reported).
THE DEEP-HOLDOUT SET (frozen NOW; never used in the CD wave
whose battery was h <= 900): kz 90 (h 1430), kz 116 (h 1433),
kz 142 (h 1445), kz 177 (h 1219), kz 243 (h 1292) -- the
three deepest windows by h plus the two deepest by kz from
the deployed frame_a_zones ladder.

THE FROZEN SUCCESS CRITERIA (all four): (1) phases from
source coefficients only (structural firewall clean); (2)
cells + pairing fixed pre-run (THIS FILE'S HASH is the
proof); (3) the cross-block envelope decays in phase distance
with h-independent Cotlar sum (RUN 2 BOUNDED); (4) Epstein/
scramble break the local compensation or the summable order
visibly (the contrast bars above).
THE FROZEN KILLS: the relevant-cell count grows with h; the
Cotlar sum grows as a power or log of h; the dangerous blocks
are findable only via the computed soft eigenvector (i.e. the
danger-family localization bar of RUN 1(a) fails while a
soft-eigenvector-selected family succeeds); truth/Epstein/
scramble share the same block geometry (contrast bars fail);
the compensation stays global (no phase-local dominance +
summable rest: RUN 1(b) defect large AND RUN 2 unbounded);
the needed constant approaches 1 from the wrong side as the
margin vanishes (B_C >= 1 with margin 1 - B_C shrinking
faster than tau along the ladder -- reported per rung).

OPERATIONAL LOCK: --run1/--run2/--run3 REFUSE to execute
unless the flag file pruefer_unfreeze.flag exists next to
this file (the parent creates it AFTER the round-34 commit).
--freeze runs ONLY: spec + SHA-256 (of this spec string and
of the file itself), the machinery wards on SYNTHETIC data (a
textbook orthonormal Chebyshev chain, n = 48: a_n = 0, b_0 =
1/sqrt(2), b_n = 1/2; and a perturbed copy a'_n = a_n + 0.02
cos(n+1), b'_n = b_n (1 + 0.02 sin(n+1)) -- frozen formulas):
W-F1 recursion vs closed form p_n(cos t) = sqrt(2) cos(n t)
(n >= 1) to 1e-10 on a 401-point t-grid; W-F2 branch
discipline (all increments in [-pi, pi)) and strict
monotonicity of theta_{n*} across the chain's own sorted
Gauss nodes (|Spearman| = 1); W-F3 cell partition
completeness Sum_r X_r == X exact (0 deviation) on the
synthetic kernel X_ij = 1/(1 + 25 wrap(delta_theta_ij)^2)
built from the two synthetic chains' phases at their node
sets; W-F4 the finite Cotlar-Stein inequality ||X||_2 <=
sqrt(S_X S*_X) verified numerically on the synthetic pieces;
W-F5 the envelope machinery decays on the synthetic
near-diagonal kernel (Spearman(env, d) <= -0.8 over d =
0..8); W-F6 the operational lock self-test (the flag file
must be ABSENT at freeze time and the gate must refuse).
NO deployed-data analysis at freeze time: the freeze path
never calls build_rung / build_window / gauss_objects.
Float64.  NO RH claim; writes nothing; no .md; no commits.
"""

CELLS = 16
CELL_W = math.pi / 8.0
DGR1 = (0, 15)
DGR2 = (7, 8)
ANCHORS = (9, 12, 13, 26, 40)
HOLDOUTS = (90, 116, 142, 177, 243)
FLAG = os.path.join(_HERE, "pruefer_unfreeze.flag")
BANNED_IDS = ("zetazero", "nzeros", "primerange", "isprime",
              "primepi", "nextprime", "prevprime")
CONSTRUCTION_BANNED = ("softport", "esoft", "eigh", "eigvalsh",
                       "pinv", "svd")

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
    return bool(ok)


def section(title):
    print("\n" + "=" * 74)
    print(title)
    print("=" * 74, flush=True)


def ast_scan(banned, func_names=None):
    """Scan this file (or only the named function bodies) for
    banned identifiers."""
    src = open(os.path.abspath(__file__), encoding="utf-8").read()
    tree = ast.parse(src)
    nodes = []
    if func_names is None:
        nodes = list(ast.walk(tree))
    else:
        for fn in ast.walk(tree):
            if isinstance(fn, ast.FunctionDef) \
                    and fn.name in func_names:
                nodes.extend(ast.walk(fn))
    bad = []
    for node in nodes:
        name = None
        if isinstance(node, ast.Name):
            name = node.id
        elif isinstance(node, ast.Attribute):
            name = node.attr
        if name and name.lower() in banned:
            bad.append(name)
    return bad


def spearman(a, b):
    ra = np.argsort(np.argsort(a)).astype(float)
    rb = np.argsort(np.argsort(b)).astype(float)
    ra -= ra.mean()
    rb -= rb.mean()
    den = math.sqrt(float(ra @ ra) * float(rb @ rb))
    return float(ra @ rb) / den if den > 0 else 0.0


# ------------------------------------------- construction (firewalled)
def pruefer_phase(al, be, m0, xs, nstar):
    """Unwrapped Pruefer phase theta_{nstar}(xs) of the
    orthonormal chain (al, be, m0): u_n = p_n, v_n = b_n
    p_{n+1}; theta_0 = atan2 in (-pi, pi]; increments wrapped
    to [-pi, pi) and accumulated per point.  SOURCE ONLY
    (chain coefficients + evaluation points).
    MECHANICAL FIX post-commit 526ca3eb: per-step joint
    positive renormalization of (p_prev, p_cur) to prevent
    float overflow at near-breakdown chain tails (deep minus
    arms reach |p| ~ 1e250..inf); a joint positive rescaling
    leaves atan2(v, u) and the wrapped increments unchanged
    in exact arithmetic, so the frozen phase definition is
    untouched (spec literal SHA re-verified)."""
    xs = np.asarray(xs, float)
    p_prev = np.zeros_like(xs)
    p_cur = np.full_like(xs, 1.0 / math.sqrt(m0))
    th = None
    prev_raw = None
    u = v = None
    for n in range(nstar + 1):
        scale = np.maximum(np.abs(p_cur), np.abs(p_prev))
        scale = np.where(scale > 1.0, scale, 1.0)
        p_prev = p_prev / scale
        p_cur = p_cur / scale
        p_next = ((xs - al[n]) * p_cur
                  - (be[n - 1] * p_prev if n > 0 else 0.0)
                  ) / be[n]
        u, v = p_cur, be[n] * p_next
        raw = np.arctan2(v, u)
        if th is None:
            th = raw.copy()
        else:
            inc = raw - prev_raw
            inc = (inc + math.pi) % (2.0 * math.pi) - math.pi
            th = th + inc
        prev_raw = raw
        p_prev, p_cur = p_cur, p_next
    R = np.hypot(u, v)
    return th, R, u, v


def arm_chain(b, arm):
    """Source Jacobi chain of one folded arm measure
    (cdc.stieltjes_chain conventions).  SOURCE ONLY."""
    xs, ws, _thu = gnu.folded_arm_measure(b, arm)
    m = min(b["h"], len(xs))
    al, be, m0, brk = cdc.stieltjes_chain(xs, ws, m)
    return al, be, m0, brk


def cell_index(dth):
    """delta_theta mod 2 pi -> cell 0..15 (boundaries at
    k pi/8)."""
    d = np.mod(dth, 2.0 * math.pi)
    return np.minimum((d / CELL_W).astype(int), CELLS - 1)


def deployed_cells(kz, **kw):
    """The frozen entrywise cell partition of one deployed
    rung.  Construction uses ONLY: source chains + Gauss node
    sets.  No soft eigenvector, no target pseudoinverse, no
    positivity readout enters this function."""
    b = gnu.build_rung(kz, **kw)
    go = gnu.gauss_objects(b)
    if go["fail"]:
        return None, "gauss-fail:%s" % (go["mode"],)
    alp, bep, m0p, _ = arm_chain(b, +1)
    alm, bem, m0m, _ = arm_chain(b, -1)
    xp = np.cos(go["thp"])
    xm = np.cos(go["thm"])
    nsp = len(go["thp"]) - 2
    nsm = len(go["thm"]) - 2
    thp, _rp, _up, _vp = pruefer_phase(alp, bep, m0p, xp, nsp)
    thm, _rm, _um, _vm = pruefer_phase(alm, bem, m0m, xm, nsm)
    dth = thm[:, None] - thp[None, :]
    cell = cell_index(dth)
    return dict(b=b, go=go, thp=thp, thm=thm, cell=cell,
                chains=dict(alp=alp, bep=bep, m0p=m0p,
                            alm=alm, bem=bem, m0m=m0m)), None


# ------------------------------------------- readout machinery
def split_pieces(X, cell):
    """Entrywise partition of X into the 16 cell pieces."""
    return [np.where(cell == r, X, 0.0) for r in range(CELLS)]


def cross_norms(pieces):
    """N[r, s] = ||X_r* X_s||_2 and Nstar[r, s] =
    ||X_r X_s*||_2 (16 x 16 each)."""
    N = np.zeros((CELLS, CELLS))
    Ns = np.zeros((CELLS, CELLS))
    for r in range(CELLS):
        for s in range(r, CELLS):
            a = float(np.linalg.norm(
                pieces[r].conj().T @ pieces[s], 2))
            c = float(np.linalg.norm(
                pieces[r] @ pieces[s].conj().T, 2))
            N[r, s] = N[s, r] = a
            Ns[r, s] = Ns[s, r] = c
    return N, Ns


def cotlar_sums(N, Ns):
    S = float(np.max(np.sum(np.sqrt(N), axis=1)))
    Ss = float(np.max(np.sum(np.sqrt(Ns), axis=1)))
    return S, Ss, math.sqrt(S * Ss)


def circle_dist():
    r = np.arange(CELLS)
    d = np.abs(r[:, None] - r[None, :])
    return np.minimum(d, CELLS - d)


def envelope(N):
    """env(d) = max over pairs at circle distance d."""
    cd = circle_dist()
    return np.array([float(np.max(N[cd == d]))
                     for d in range(CELLS // 2 + 1)])


def require_unfreeze(mode):
    if not os.path.exists(FLAG):
        print("REFUSED: %s is a deployed-data run and the "
              "unfreeze flag is absent." % mode)
        print("  create %s AFTER the round-34 commit to "
              "unlock." % FLAG)
        return False
    return True


# ============================================ deployed runs (LOCKED)
def battery_rungs():
    """The 42-rung battery: frame_a_zones, h <= 900, plus arm
    square (the CD-wave ladder).  MECHANICAL FIX post-commit
    526ca3eb: the committed version omitted the h <= 900
    filter that the FROZEN_SPEC battery definition mandates
    ("all frame_a_zones with h <= 900"); the spec literal is
    untouched (SHA re-verified)."""
    out = []
    for kz in core.frame_a_zones():
        if kz in HOLDOUTS:
            continue
        if core.build_window(kz)["h"] > 900:
            continue
        out.append(kz)
    return out


def rung_readouts(kz, **kw):
    """Pieces + census of one rung (cells FIXED before any
    eigen/SVD readout below this line)."""
    dc, err = deployed_cells(kz, **kw)
    if dc is None:
        return None, err
    b, go, cell = dc["b"], dc["go"], dc["cell"]
    if b["h"] > 1500:
        return None, "skip-h"
    # node-consistency ward (chain vs Gauss nodes)
    ch = dc["chains"]
    Jp = np.diag(ch["alp"]) + np.diag(ch["bep"][:len(
        ch["alp"]) - 1], 1) + np.diag(ch["bep"][:len(
            ch["alp"]) - 1], -1)
    evp = np.linalg.eigvalsh(Jp)
    nodew = float(np.max(np.abs(np.sort(evp)
                                - np.sort(np.cos(go["thp"])))))
    U = go["U"]
    Dm2 = go["Dm"] ** 2
    C = go["Dm"][:, None] * U
    pu = split_pieces(U, cell)
    pc = split_pieces(C, cell)
    compl_u = float(np.max(np.abs(sum(pu) - U)))
    compl_c = float(np.max(np.abs(sum(pc) - C)))
    Nu, Nus = cross_norms(pu)
    Nc, Ncs = cross_norms(pc)
    Su, Sus, Bu = cotlar_sums(Nu, Nus)
    Sc, Scs, Bc = cotlar_sums(Nc, Ncs)
    # danger census
    dgr = set(DGR1) | set(DGR2)
    tot = float(np.sum(Nu))
    dmask = np.zeros((CELLS, CELLS), bool)
    for r in range(CELLS):
        for s in range(CELLS):
            dmask[r, s] = (r in dgr) or (s in dgr)
    dshare = float(np.sum(Nu[dmask])) / max(tot, 1e-300)
    # local inequality census (readout AFTER cells fixed)
    h = b["h"]
    wr = np.array([float(np.sum(np.abs(p) ** 2)) for p in pu])
    wr = wr / max(float(np.sum(wr)), 1e-300)
    eps = []
    for r in range(CELLS):
        Ar = pu[r]
        Mr = wr[r] * np.eye(h) - Ar.conj().T \
            @ (Dm2[:, None] * Ar)
        Mr = 0.5 * (Mr + Mr.conj().T)
        eps.append(max(0.0, -float(np.linalg.eigvalsh(Mr)[0])))
    # negativity localization (danger-family truncation)
    T1 = np.eye(h) - U.conj().T @ U
    T1 = 0.5 * (T1 + T1.conj().T)
    lmin_T1 = float(np.linalg.eigvalsh(T1)[0])
    Udgr = sum(pu[r] for r in sorted(dgr))
    T1d = np.eye(h) - Udgr.conj().T @ Udgr
    T1d = 0.5 * (T1d + T1d.conj().T)
    lmin_d = float(np.linalg.eigvalsh(T1d)[0])
    env_u = envelope(Nu)
    env_c = envelope(Nc)
    sp_u = spearman(env_u[:9], np.arange(9.0))
    sp_c = spearman(env_c[:9], np.arange(9.0))
    return dict(kz=kz, h=h, nodew=nodew, compl=max(compl_u,
                compl_c), Su=Su, Sus=Sus, Bu=Bu, Sc=Sc,
                Scs=Scs, Bc=Bc, dshare=dshare,
                eps_sum=float(np.sum(eps)), eps=eps,
                lmin_T1=lmin_T1, lmin_d=lmin_d,
                env_u=env_u, env_c=env_c, sp_u=sp_u,
                sp_c=sp_c, Nu=Nu, Nc=Nc), None


def run1():
    """RUN 1 -- anatomy on the anchors (post-unfreeze
    only)."""
    if not require_unfreeze("--run1"):
        return 2
    section("RUN 1 -- phase-cell anatomy (anchors %s)"
            % (ANCHORS,))
    for kz in ANCHORS:
        r, err = rung_readouts(kz)
        if r is None:
            print("    kz %d: %s" % (kz, err))
            continue
        print("    kz %-3d h %-4d: node ward %.1e, partition "
              "%.1e | danger share %.3f | lam_min(T1) %+ .4f "
              "vs danger-trunc %+ .4f (capture %.2f) | "
              "sum eps_r %.3e | env Spearman U/C %.2f/%.2f"
              % (kz, r["h"], r["nodew"], r["compl"],
                 r["dshare"], r["lmin_T1"], r["lmin_d"],
                 (r["lmin_d"] / r["lmin_T1"])
                 if r["lmin_T1"] < 0 else float("nan"),
                 r["eps_sum"], r["sp_u"], r["sp_c"]))
        with np.printoptions(precision=2, suppress=False,
                             linewidth=100):
            print("      env_U(d):", r["env_u"])
            print("      env_C(d):", r["env_c"])
    return 0


def run2():
    """RUN 2 -- the Cotlar decision (post-unfreeze only)."""
    if not require_unfreeze("--run2"):
        return 2
    section("RUN 2 -- Cotlar sums, battery + deep holdouts")
    series = []
    for kz in battery_rungs() + list(HOLDOUTS):
        r, err = rung_readouts(kz)
        if r is None:
            print("    kz %d: %s" % (kz, err))
            continue
        tag = "HOLDOUT" if kz in HOLDOUTS else "battery"
        series.append((kz, r["h"], r["Su"], r["Sc"], r["Bu"],
                       r["Bc"], tag))
        print("    kz %-4d h %-4d [%s]: S_U %.4f  S_C %.4f  "
              "B_U %.4f  B_C %.4f  (1-B_C %.2e)"
              % (kz, r["h"], tag, r["Su"], r["Sc"], r["Bu"],
                 r["Bc"], 1.0 - r["Bc"]), flush=True)
    bat = [x for x in series if x[6] == "battery"]
    hol = [x for x in series if x[6] == "HOLDOUT"]
    for lbl, ix in (("S_U", 2), ("S_C", 3)):
        mb = max(x[ix] for x in bat)
        mh = max(x[ix] for x in hol) if hol else float("nan")
        hh = np.log([x[1] for x in series])
        ss = np.log([x[ix] for x in series])
        slope = float(np.polyfit(hh, ss, 1)[0])
        bounded = mh <= 1.2 * mb and slope <= 0.10
        growing = slope >= 0.20
        print("    %s: battery max %.4f, holdout max %.4f, "
              "log-log slope %.3f -> %s"
              % (lbl, mb, mh, slope,
                 "BOUNDED" if bounded else
                 ("GROWING" if growing else "PARTIAL")))
    section("RUN 2 -- truth/Epstein/scramble contrast (kz 9)")
    rt, _ = rung_readouts(9)
    rr9 = core.build_window(9)
    N_E = int(math.floor(math.exp(2.0 * rr9["alpha"]))) + 1
    lamE = gnu.lambda_eps(N_E)
    nn = np.nonzero(np.abs(lamE) > 1e-12)[0]
    for nmc, kw in (("Epstein", dict(comb=(
            np.log(nn.astype(float)),
            2.0 * lamE[nn] / np.sqrt(nn.astype(float))))),
            ("scramble", dict(scramble_seed=1))):
        rc, err = rung_readouts(9, **kw)
        if rc is None:
            print("    %-8s: %s (typed)" % (nmc, err))
            continue
        tri_t = np.array([rt["Su"], rt["Sc"], rt["dshare"]])
        tri_c = np.array([rc["Su"], rc["Sc"], rc["dshare"]])
        rel = float(np.max(np.abs(tri_c - tri_t)
                           / np.maximum(tri_t, 1e-12)))
        print("    %-8s: (S_U, S_C, danger) = (%.3f, %.3f, "
              "%.3f) vs truth (%.3f, %.3f, %.3f): max rel "
              "%.0f%%; eps ratio %.1f; env Spearman U %.2f"
              % (nmc, *tri_c, *tri_t, 100 * rel,
                 rc["eps_sum"] / max(rt["eps_sum"], 1e-300),
                 rc["sp_u"]))
    return 0


def run3():
    """RUN 3 -- the uniformity candidate (post-unfreeze only,
    only if RUN 2 was BOUNDED)."""
    if not require_unfreeze("--run3"):
        return 2
    section("RUN 3 -- analytic envelope candidate on the "
            "deep holdouts")
    refs = []
    for kz in list(ANCHORS) + list(HOLDOUTS):
        r, err = rung_readouts(kz)
        if r is None:
            print("    kz %d: %s" % (kz, err))
            continue
        dc, _ = deployed_cells(kz)
        ch = dc["chains"]
        dco = max(
            float(np.max(np.abs(np.diff(ch["alp"]))
                         + np.abs(np.diff(ch["bep"][:len(
                             ch["alp"]) - 1])))),
            float(np.max(np.abs(np.diff(ch["alm"]))
                         + np.abs(np.diff(ch["bem"][:max(len(
                             ch["alm"]) - 1, 1)])))))
        dd = np.arange(len(r["env_u"]), dtype=float)
        K1 = float(np.max(r["env_u"] * (1.0 + dd)))
        K2 = float(np.max(r["env_c"] * (1.0 + dd) ** 2))
        tag = "HOLDOUT" if kz in HOLDOUTS else "anchor"
        refs.append((kz, tag, K1, K2, dco))
        print("    kz %-4d h %-4d [%s]: K_1 = %.4f, K_2 = "
              "%.4f, delta_coef = %.3e"
              % (kz, r["h"], tag, K1, K2, dco))
    for lbl, ix in (("K_1", 2), ("K_2", 3)):
        mb = max(x[ix] for x in refs if x[1] == "anchor")
        mh = max(x[ix] for x in refs if x[1] == "HOLDOUT")
        print("    %s: anchor max %.4f, holdout max %.4f -> "
              "h-stable: %s (bar 1.2x)"
              % (lbl, mb, mh, mh <= 1.2 * mb))
    return 0


# ============================================ freeze mode (synthetic)
def chebyshev_chain(n):
    """Orthonormal Chebyshev chain on [-1, 1], measure
    dx/(pi sqrt(1-x^2)): a_k = 0, b_0 = 1/sqrt(2), b_k =
    1/2."""
    al = np.zeros(n)
    be = np.full(n, 0.5)
    be[0] = 1.0 / math.sqrt(2.0)
    return al, be, 1.0


def perturbed_chain(al, be):
    """The frozen perturbed copy (spec formulas)."""
    k = np.arange(len(al), dtype=float)
    al2 = al + 0.02 * np.cos(k + 1.0)
    be2 = be * (1.0 + 0.02 * np.sin(k + 1.0))
    return al2, be2, 1.0


def gauss_nodes(al, be, m):
    J = np.diag(al[:m]) + np.diag(be[:m - 1], 1) \
        + np.diag(be[:m - 1], -1)
    return np.sort(np.linalg.eigvalsh(J))


def freeze_mode():
    section("PRIME.PRUEFER.COMPENSATION.01 -- FREEZE "
            "(preregistration; no deployed data)")
    sha_spec = hashlib.sha256(
        FROZEN_SPEC.encode("utf-8")).hexdigest()
    sha_file = hashlib.sha256(
        open(os.path.abspath(__file__), "rb").read()).hexdigest()
    print("    FROZEN_SPEC SHA-256 = %s" % sha_spec)
    print("    FILE       SHA-256 = %s" % sha_file)
    print("    NO RH claim.")

    print("\nS0 -- firewalls")
    check("S0.1 AST firewall clean (no zero/prime oracles)",
          not ast_scan(BANNED_IDS))
    bad = ast_scan(CONSTRUCTION_BANNED,
                   func_names=("pruefer_phase", "arm_chain",
                               "cell_index", "deployed_cells"))
    check("S0.2 [CONSTRUCTION FIREWALL] the cell construction "
          "functions contain no eigen/SVD/pinv/soft-vector "
          "identifiers (structural)", not bad,
          str(bad) if bad else "")

    section("S1 -- synthetic machinery wards "
            "(Chebyshev n=48 + frozen perturbed copy)")
    n = 48
    al, be, m0 = chebyshev_chain(n)
    al2, be2, m02 = perturbed_chain(al, be)

    # W-F1: recursion vs closed form
    tg = np.linspace(0.05, math.pi - 0.05, 401)
    xg = np.cos(tg)
    nstar = n - 2
    th, R, u, v = pruefer_phase(al, be, m0, xg, nstar)
    p_ns = math.sqrt(2.0) * np.cos(nstar * tg)
    p_ns1 = math.sqrt(2.0) * np.cos((nstar + 1) * tg)
    dev = max(float(np.max(np.abs(u - p_ns))),
              float(np.max(np.abs(v / be[nstar] - p_ns1))))
    check("W-F1 recursion vs closed form sqrt(2) cos(n t) "
          "(max dev %.1e <= 1e-10) and R > 0 everywhere "
          "(min %.2e)" % (dev, float(np.min(R))),
          dev <= 1e-10 and float(np.min(R)) > 0.0)

    # W-F2: branch discipline + node monotonicity
    xn = gauss_nodes(al, be, n)
    thn, Rn, _u, _v = pruefer_phase(al, be, m0, xn, nstar)
    d_thn = np.diff(thn)
    mono = bool(np.all(d_thn > 0.0) or np.all(d_thn < 0.0))
    sp = spearman(thn, np.arange(float(n)))
    check("W-F2 branch discipline: theta_{n*} strictly "
          "monotone across the chain's own %d sorted Gauss "
          "nodes (|Spearman| = %.3f, strict: %s; R_min %.2e "
          "> 0)" % (n, abs(sp), mono, float(np.min(Rn))),
          mono and abs(sp) == 1.0 and float(np.min(Rn)) > 0.0)

    # W-F3: cells + partition completeness on synthetic kernel
    xn2 = gauss_nodes(al2, be2, n)
    thn2, _r2, _u2, _v2 = pruefer_phase(al2, be2, m02, xn2,
                                        nstar)
    dth = thn2[:, None] - thn[None, :]
    wrapd = np.mod(dth + math.pi, 2.0 * math.pi) - math.pi
    X = 1.0 / (1.0 + 25.0 * wrapd ** 2)
    cell = cell_index(dth)
    pieces = split_pieces(X, cell)
    compl = float(np.max(np.abs(sum(pieces) - X)))
    ncells = int(np.sum([np.any(p != 0.0) for p in pieces]))
    check("W-F3 cell partition completeness Sum_r X_r == X "
          "exact (dev %.1e == 0; %d/16 cells populated)"
          % (compl, ncells), compl == 0.0)

    # W-F4: finite Cotlar-Stein inequality on the pieces
    N, Ns = cross_norms(pieces)
    S, Ss, B = cotlar_sums(N, Ns)
    nX = float(np.linalg.norm(X, 2))
    check("W-F4 finite Cotlar-Stein: ||X||_2 = %.4f <= "
          "sqrt(S S*) = %.4f (S = %.4f, S* = %.4f)"
          % (nX, B, S, Ss), nX <= B + 1e-12)

    # W-F5: envelope decay on the near-diagonal kernel
    env = envelope(N)
    spe = spearman(env[:9], np.arange(9.0))
    check("W-F5 envelope machinery decays on the synthetic "
          "near-phase kernel (Spearman(env, d) = %.2f <= "
          "-0.8)" % spe, spe <= -0.8)

    # W-F6: the operational lock
    flag_absent = not os.path.exists(FLAG)
    refused = not require_unfreeze("--run1 (self-test)")
    check("W-F6 operational lock: pruefer_unfreeze.flag "
          "ABSENT at freeze time and the run gate REFUSES",
          flag_absent and refused)

    section("S2 -- the frozen deep-holdout set")
    print("    HOLDOUTS (kz, h): (90, 1430), (116, 1433), "
          "(142, 1445), (177, 1219), (243, 1292)")
    print("    battery = the 42 CD-wave rungs (frame_a_zones, "
          "h <= 900); the holdouts were never used in the CD "
          "wave's construction.")

    section("S3 -- freeze confirmation")
    print("    NO deployed-data analysis ran: the freeze path "
          "calls neither build_rung nor build_window nor "
          "gauss_objects (synthetic chains only).")
    print("    RUN 1/2/3 are locked behind %s"
          % os.path.basename(FLAG))
    npass = sum(1 for _n, ok in CHECKS if ok)
    print("\n  checks: %d/%d passed; elapsed %.1f s"
          % (npass, len(CHECKS), time.time() - T0))
    print("""
PREREGISTRATION STATEMENT (no RH claim): this file freezes the
Pruefer phase discipline, the 16 fixed cells, the entrywise
pairing rule, the danger geometry, the Cotlar decision bars,
the success criteria, the kills, and the deep-holdout set
BEFORE any deployed-data analysis.  The file hash above is
the proof of precedence.  EXPLORATION ONLY; nothing here
enters verification/ or the papers.""")
    return 0 if npass == len(CHECKS) else 1


def main():
    args = sys.argv[1:]
    if args == ["--freeze"]:
        return freeze_mode()
    if args == ["--run1"]:
        return run1()
    if args == ["--run2"]:
        return run2()
    if args == ["--run3"]:
        return run3()
    print("usage: pruefer_compensation_probe.py "
          "--freeze | --run1 | --run2 | --run3")
    print("  (--run* refuse unless pruefer_unfreeze.flag "
          "exists; --freeze is the preregistration mode)")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
