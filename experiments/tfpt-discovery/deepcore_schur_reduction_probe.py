#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""deepcore_schur_reduction_probe -- PRIME.PORT.DEEPCORE.SCHUR.01
(EXPLORATION ONLY, experiments/; round 51, reviewer priority 4:
does the fixed 8-node deep core + a uniform outside margin reduce
the whole wall to a FIXED 8x8 Schur family S_h > 0?, 2026-08-09).

THE QUESTION (frozen): round 50 (deepcore_anatomy_probe,
PRIME.PORT.DEEPCORE.01) identified the arithmetic remnant as the
FIXED even alias set {2, 4, ..., 16} on the folded neg grid -- the
port core at the Bessel-normal coordinates a_m = pi^2 m^2, m =
1..8.  If the wall operator, split along that fixed core, has a
UNIFORMLY positive-definite outside block, then by the Schur
complement / Haynsworth reduction the entire cofinal wall demand
collapses to the positivity of ONE fixed 8x8 matrix family S_h --
the RH wand as a fixed-dimension statement.  This probe measures
the two ingredients honestly on the full ladder.

THE WALL OPERATOR (frozen choice, stated per the contract): the
FULL wall operator is used -- A_h = I - E_h with E_h the plain
Carleson Gram on ALL folded neg nodes (port_schur_reduction round-
38 v2 object, gauge-equivalent to the embedding E; lam_max(E_h) =
1 - tau_h, the wall <=> A_h >= 0).  The full operator is feasible
(the folded neg grid carries O(h) <= ~1800 nodes; dense
eigensolves are cheap), so the deployed port+bulk two-stage
structure of port_schur_reduction is NOT needed and NOT used --
one split, along the deep core, of the whole operator.

THE BLOCK SPLIT (frozen): A_h = [[B_h, X_h], [X_h^T, R_h]] with
B_h = the 8x8 block at the grid indices of the fixed core aliases
CORE_J = {2, 4, 6, 8, 10, 12, 14, 16} (folded index j on the neg
grid), R_h = everything else, X_h the coupling.  S_h = B_h - X_h
R_h^{-1} X_h^T is the 8x8 Schur core.

DIAGONAL-VS-OPERATOR MARGIN HONESTY NOTE (frozen into the
protocol): christoffel_zone_envelope_probe froze theta* = 0.700
with a deep-half OUTSIDE testing margin +0.0214 -- but that number
is an envelope of the DIAGONAL testing quotients T_m = nu~_m
K_h(y_m, y_m), NOT an operator lower bound for the block R_h.  The
operator margin lambda_min(R_h) is a different (and by eigenvalue
interlacing possibly far smaller) quantity: interlacing only
guarantees lambda_min(R_h) >= tau_h.  The reviewer's hope R_h >=
0.0214 I is therefore measured FRESH here and compared honestly;
the diagonal 0.0214 is printed as a REFERENCE ONLY, never as a
bound.

THE LADDER (frozen, christoffel_zone_envelope verbatim):
core.frame_a_zones() restricted to h <= 900 via the closed M_k
formula -- the 42 reachable rungs, sorted by (h, kz); consecutive
pairs (k = 1) for the inheritance ladder.

FROZEN PROTOCOL (2026-08-09, frozen + SHA-hashed before the first
run; all bars frozen before the run):

 B1  THE OUTSIDE BLOCK: per rung lambda_min(R_h) (full ladder
     printed) with the ratio lambda_min(R_h)/tau_h and the
     diagonal reference DIAG_REF = 0.0214.  Log-log slope of
     lambda_min(R_h) vs h over the ladder.  TYPED:
     OPERATOR-MARGIN-UNIFORM(r0) iff min_h lambda_min(R_h) >=
     R_UNIF_BAR = 1e-3 AND slope >= SLOPE_TOL = -0.10 (candidate
     uniform floor r0 = the measured min); else
     OPERATOR-MARGIN-SHRINKS(slope) with the trend printed.

 B2  THE SCHUR CORE: S_h = B_h - X_h R_h^{-1} X_h^T (8x8) on
     every full-core rung.  WARDS (Haynsworth inertia
     bookkeeping): the integer identity neg(A_h) = neg(R_h) +
     neg(S_h) on every evaluable rung (truth, smooth AND both
     controls; rungs with min |eig(R_h)| < R_SING_TOL_REL x
     max |eig(R_h)| are typed SINGULAR-SKIP for the identity --
     the inertia formula needs R nonsingular, and the guard is
     relative because the controls carry eigenvalues of order
     10^3); on truth additionally all
     three PSD (A_h PD <=> R_h PD and S_h PD).  THE WALL IN 8x8:
     lambda_min(S_h) ladder, the ratio lambda_min(S_h)/tau_h, and
     the Pearson correlation of log lambda_min(S_h) vs log tau_h
     across the ladder.  (Anatomy, report only: the soft-mode
     core mass w_core = ||v_top(E_h)|_core||^2; the exact
     asymptotic expectation is lambda_min(S_h) ~ tau_h / w_core
     as tau -> 0, printed as the product check
     lambda_min(S_h) * w_core / tau_h.)  TYPED:
     SCHUR-TAU-TIED(corr, med ratio) iff corr >= TIED_CORR =
     0.99; else SCHUR-TAU-LOOSE(corr).

 B3  THE CORE INHERITANCE (fixed dimension): per consecutive
     full-core pair with S_h PD, H_core = S_h^{-1/2} (S_{h+1} -
     S_h) S_h^{-1/2} and eta_core = 1 + lambda_min(H_core) =
     lambda_min(S_h^{-1/2} S_{h+1} S_h^{-1/2}) (> 0 <=> S_{h+1}
     PD given S_h PD -- the inheritance margin in relative form).
     Ladder printed; census of crossings (eta_core <= 0).  TYPED
     (truth): CORE-INHERITS iff zero crossings, else
     CORE-CROSSES(n).  THE SMOOTH WORLD (masses 2 e^{u/2} du on
     the true lattice, lattice_parametrix B1 / deepcore_anatomy
     verbatim): same census; steps whose base S_h is not PD (or
     whose rung already has neg(A) > 0) are counted separately as
     rung-level failures n_hard.  TYPED:
     CORE-SEES-SMOOTH(n_cross, n_hard) iff n_cross + n_hard > 0;
     else CORE-BLIND-TO-SMOOTH (an honest finding: the smooth
     failure would then live outside the fixed core).

 B4  THE PER-PRIME GRAIN ON FIXED DIMENSION: at the 5 frozen
     heavy rungs kz GRAIN_KZ = {9, 12, 13, 26, 40}, the
     leave-one-prime-out response of S_h for the frozen primes
     GRAIN_PRIMES = {2, 3, 5, 7, 11}: the comb with ALL powers
     p^k of the one prime p removed (power identification by the
     explicit power list of the hard-coded p -- no oracle),
     D_p = S_h(without p) - S_h; plus the joint removal D_all =
     S_h(without all five) - S_h.  Report per rung: ||D_p||_F,
     the relative resolution ||D_p||_F / ||S_h||_F,
     lambda_min(S_h without p), and the ADDITIVITY DEFECT
     ||D_all - sum_p D_p||_F / ||D_all||_F.  TYPED:
     CORE-GRAIN-ACCESSIBLE(max defect) iff on ALL 5 rungs every
     response is resolved (rel >= RESOLVE_BAR = 1e-9), every
     modified world keeps the full core frame, and the additivity
     defect <= GRAIN_DEF_BAR = 0.20; else CORE-GRAIN-DEAD(reason).

 B5  THE REDUCTION STATEMENT (printed, with the measured
     numbers): IF lambda_min(R_h) >= r_0 > 0 uniformly in h
     (measured candidate r_0 = the B1 floor) THEN by Haynsworth
     the wall A_h >= 0 is EQUIVALENT to S_h >= 0 for the FIXED
     8x8 family -- the RH wand as a fixed-dimension statement.
     Its finite shadow = the B2/B3 ladders; the open pieces = the
     uniform R-margin theorem and the core inheritance.

 C   CONTROLS/WARDS: (C1, primary) the SMOOTH-MASS world must
     violate somewhere -- at rung level (some neg(A_h) > 0, the
     Haynsworth ledger then LOCATES the negative directions:
     typed VIOLATION-IN-R / VIOLATION-IN-S / VIOLATION-MIXED
     over the violating rungs) or, failing that, at flow level
     (B3-smooth n_cross > 0, typed VIOLATION-IN-FLOW).  Silent on
     both -> WARD-BROKEN.  (C2, must fire) Epstein x^2+5y^2 comb
     and scramble (seed 1) at kz 9: lam(E) > 1 (neg(A) > 0) on
     both, with the inertia localization printed; either silent
     -> WARD-BROKEN.  (C0, truth anchor) the truth wall holds on
     every rung (neg(A_h) = 0, tau_h > 0) -- the established
     object being reduced; a miss -> WARD-BROKEN.

 W   PIPELINE WARDS: W1 exactly 42 reachable rungs and every
     chain completes; W2 all tau finite; W3 >= 30 rungs carry the
     full core alias set (rungs missing a core alias are typed
     CORE-INCOMPLETE skips, printed).

KILLS: K1 a W ward breaks -> PIPELINE-BROKEN; K2 a C ward breaks
(truth wall broken / Haynsworth integer identity broken on an
evaluable rung / smooth silent on both channels / a C2 control
silent) -> WARD-BROKEN.

VERDICT (frozen enum): DEEPCORESCHUR-MEASURED with typed
sublabels OPERATOR-MARGIN-UNIFORM(r0) / OPERATOR-MARGIN-SHRINKS
(slope) (B1), SCHUR-TAU-TIED / SCHUR-TAU-LOOSE (B2),
CORE-INHERITS / CORE-CROSSES(n) + CORE-SEES-SMOOTH /
CORE-BLIND-TO-SMOOTH (B3), CORE-GRAIN-ACCESSIBLE /
CORE-GRAIN-DEAD (B4); else PIPELINE-BROKEN / WARD-BROKEN.

FROZEN BARS: CORE_J = (2,4,6,8,10,12,14,16); H_LADDER_MAX = 900;
N_RUNGS_EXP = 42; MIN_CORE_RUNGS = 30; DIAG_REF = 0.0214
(reference only, diagonal object); R_UNIF_BAR = 1e-3; SLOPE_TOL =
-0.10; TIED_CORR = 0.99; R_SING_TOL_REL = 1e-10; GRAIN_KZ =
(9,12,13,26,40); GRAIN_PRIMES = (2,3,5,7,11); GRAIN_DEF_BAR =
0.20; RESOLVE_BAR = 1e-9; CTRL_KZ = 9; scramble seed 1.

SPEC AMENDMENTS (documented; fail-first preserved):
  v1 (2026-08-09, frozen pre-run): everything above.  Mechanical
     concretizations frozen with v1: (i) core.build_window
     results are MEMOIZED per (kz, seed) exactly as in
     deepcore_anatomy_probe (pure memoization of a deterministic
     function, bit-identical physics; several worlds share the
     same windows); (ii) negative-eigenvalue counts use the
     strict eig < 0.0 reading (port_schur_reduction precedent);
     (iii) the B3 smooth census requires only the BASE S_h of a
     step to be PD (an indefinite successor is precisely what
     eta_core <= 0 detects); (iv) B4 prime-power removal uses the
     explicit power list {p, p^2, ...} <= max atom of the
     hard-coded prime p -- no primality oracle is ever invoked;
     (v) the Haynsworth SINGULAR-SKIP guard is RELATIVE
     (R_SING_TOL_REL) because control-world blocks carry
     eigenvalues of order 10^3.
  v2 (2026-08-09, after run 1 -- which was already 16/16 green
     with the full typed verdict): THREE transparency-only print
     repairs, no bar, no object, no typed label moved (run-1 and
     run-2 verdicts identical): (a) the B2 summary additionally
     prints max |lamS/tau - 1|, max |lamS*wcore/tau - 1| and min
     wcore at full precision -- run 1 showed the decisive
     correspondence as '1.000' everywhere and the deviation scale
     was invisible; (b) the B4 dead-label aggregates ALL observed
     failure reasons instead of the first (run 1 typed only
     'base frame loss' although the surviving rungs also broke
     the additivity bar by x8-x18); (c) skipped ledger entries
     print 'n/a' instead of the sentinel -1.

NO RH claim: lambda_min ladders of finite-h blocks and an 8x8
Schur family are numerical measurements on the deployed v563
window ladder; the uniform R-margin and the core inheritance
remain open theorems, and no marker moves.

FIREWALL: no zeros, no prime oracles (AST scan; banned ids
zetazero / nzeros / primerange / isprime / primepi / nextprime /
prevprime); v563 READ-ONLY; RNG only inside the declared scramble
control; stdout only.  No marker moves.

Sources (read-only): v563_paper2_readouts; wall Gram + Haynsworth
ledger verbatim from port_schur_reduction_probe.py
(PRIME.PORT.SCHUR.01); fixed core aliases from
deepcore_anatomy_probe.py (PRIME.PORT.DEEPCORE.01); ladder +
diagonal margin context from christoffel_zone_envelope_probe.py
(PRIME.CASE.ZONESPLIT.01, theta* = 0.700); smooth-mass world from
lattice_parametrix_probe.py (B1); Epstein control comb verbatim
from port_schur_reduction_probe.py.

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/deepcore_schur_reduction_probe.py
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

CORE_J = (2, 4, 6, 8, 10, 12, 14, 16)
H_LADDER_MAX = 900
N_RUNGS_EXP = 42
MIN_CORE_RUNGS = 30
DIAG_REF = 0.0214              # christoffel diagonal deep-half inf
R_UNIF_BAR = 1e-3              # B1 uniform-floor bar (operator)
SLOPE_TOL = -0.10              # B1 shrink-trend tolerance
TIED_CORR = 0.99               # B2 log-log correlation bar
R_SING_TOL_REL = 1e-10         # Haynsworth relative guard (v2)
GRAIN_KZ = (9, 12, 13, 26, 40)
GRAIN_PRIMES = (2, 3, 5, 7, 11)
GRAIN_DEF_BAR = 0.20
RESOLVE_BAR = 1e-9
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


# --------------- pipeline, verbatim (port_schur_reduction / deepcore)
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


_WIN_CACHE = {}


def window_of(kz, scramble_seed=None):
    """SPEC concretization (i): pure memoization of the
    deterministic core.build_window (deepcore_anatomy verbatim)."""
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


def ladder_zones():
    """The 42 reachable rungs (christoffel_zone_envelope verbatim)."""
    out = []
    for kz in core.frame_a_zones():
        D_k = 0.5 * float(core.G_ALL[kz]) / float(core.NU_MAIN)
        M_k = int(math.ceil(float(core.U_ALL[kz]) / D_k - 1.0e-9)) + 1
        if M_k % 2:
            M_k += 1
        if M_k // 2 <= H_LADDER_MAX:
            out.append(kz)
    return out


def smooth_masses(uu):
    """PNT-mean masses 2 e^{u/2} du (lattice_parametrix B1)."""
    return 2.0 * np.exp(uu / 2.0) * cell_widths(uu)


def world_smooth(uu, mm, rr):
    return uu, smooth_masses(uu)


def world_drop_primes(primes):
    """B4: remove ALL powers p^k of the listed hard-coded primes
    (explicit power lists -- no oracle)."""
    def fn(uu, mm, rr):
        nn = core._NN[:rr["n_atom"]].astype(np.int64)
        mx = int(nn.max())
        drop = np.zeros(len(nn), bool)
        for p in primes:
            pows, v = [], p
            while v <= mx:
                pows.append(v)
                v *= p
            drop |= np.isin(nn, np.asarray(pows, dtype=np.int64))
        keep = ~drop
        return uu[keep], mm[keep]
    return fn


def gram_anatomy(kz, world_fn=None, scramble_seed=None, comb=None,
                 want_vec=False):
    """Full wall operator A = I - E on the folded neg grid + the
    fixed-core block split, inertia ledger and Schur core."""
    rr = window_of(kz, scramble_seed=scramble_seed)
    M, D, alpha, h = rr["M"], rr["D"], rr["alpha"], rr["h"]
    uu = rr["uu"]
    mm = 2.0 * rr["lam"]
    if world_fn is not None:
        uu, mm = world_fn(uu, mm, rr)
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
    G = np.sqrt(vs)[:, None] * (Pn @ Pn.T) * np.sqrt(vs)[None, :]
    G = 0.5 * (G + G.T)
    n = G.shape[0]
    A = np.eye(n) - G
    out = dict(kz=kz, h=h, n=n)
    if want_vec:
        evA, VA = np.linalg.eigh(A)
    else:
        evA = np.linalg.eigvalsh(A)
        VA = None
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
    X = A[np.ix_(ic, ib)]
    R = A[np.ix_(ib, ib)]
    evR = np.linalg.eigvalsh(R)
    out["lamR"] = float(evR[0])
    out["negR"] = int(np.sum(evR < 0.0))
    out["Rsing"] = bool(float(np.min(np.abs(evR)))
                        < R_SING_TOL_REL
                        * float(np.max(np.abs(evR))))
    S = B - X @ np.linalg.solve(R, X.T)
    S = 0.5 * (S + S.T)
    evS = np.linalg.eigvalsh(S)
    out["S"] = S
    out["lamS"] = float(evS[0])
    out["negS"] = int(np.sum(evS < 0.0))
    if want_vec:
        v = VA[:, 0]                    # soft mode of the wall
        out["wcore"] = float(np.sum(v[ic] ** 2))
    return out


def hayns_ok(r):
    """Integer Haynsworth identity on an evaluable rung
    (None = SINGULAR-SKIP, concretization v2: relative guard)."""
    if not r.get("core_ok", False):
        return None
    if r["Rsing"]:
        return None
    return r["negA"] == r["negR"] + r["negS"]


def inherit_ladder(rungs, tag):
    """B3: eta_core = lam_min(S^-1/2 S' S^-1/2) per consecutive
    full-core pair with PD base S; returns (rows, n_cross,
    n_hard, n_skip)."""
    rows, n_cross, n_hard, n_skip = [], 0, 0, 0
    for r1, r2 in zip(rungs, rungs[1:]):
        if (r1 is None or r2 is None
                or not r1.get("core_ok") or not r2.get("core_ok")):
            n_skip += 1
            continue
        if r1["lamS"] <= 0.0 or r1["negA"] > 0:
            n_hard += 1
            continue
        w, V = np.linalg.eigh(r1["S"])
        Wm = V @ np.diag(1.0 / np.sqrt(w)) @ V.T
        eta = float(np.linalg.eigvalsh(
            Wm @ r2["S"] @ Wm)[0])
        rows.append((r1["h"], r2["h"], eta - 1.0, eta))
        if eta <= 0.0:
            n_cross += 1
    print("    [%s] %d steps computable, %d crossings "
          "(eta_core <= 0), %d rung-level failures, %d skips"
          % (tag, len(rows), n_cross, n_hard, n_skip))
    return rows, n_cross, n_hard, n_skip


def main():
    section("PRIME.PORT.DEEPCORE.SCHUR.01 -- the fixed 8x8 Schur "
            "reduction of the wall (EXPLORATION ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s"
          % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
    print("    NO RH claim; full wall operator A = I - E; the "
          "diagonal 0.0214 is a REFERENCE, not an operator bound.")
    print("\nS0 -- firewall")
    check("S0.1 AST firewall clean", not ast_scan(BANNED_IDS))

    # ------------------------------------------------------------ W
    section("W -- the truth ladder (42 reachable rungs, h <= %d)"
            % H_LADDER_MAX)
    zones = ladder_zones()
    check("W1 frozen rung count %d" % N_RUNGS_EXP,
          len(zones) == N_RUNGS_EXP, "found %d" % len(zones),
          kill="K1")
    truth = []
    for kz in zones:
        r = gram_anatomy(kz, want_vec=True)
        if r is None:
            print("    kz %-3d: CHAIN SHORT" % kz, flush=True)
        truth.append(r)
    ok_chain = all(r is not None for r in truth)
    check("W1b all chains complete", ok_chain, kill="K1")
    if not ok_chain:
        return finish({})
    truth.sort(key=lambda r: (r["h"], r["kz"]))
    fin = all(np.isfinite(r["tau"]) for r in truth)
    check("W2 all tau finite", fin, kill="K1")
    full = [r for r in truth if r["core_ok"]]
    n_inc = len(truth) - len(full)
    check("W3 >= %d full-core rungs (CORE-INCOMPLETE skips: %d)"
          % (MIN_CORE_RUNGS, n_inc), len(full) >= MIN_CORE_RUNGS,
          "%d full-core rungs" % len(full), kill="K1")
    print("    h range %d..%d  [%.1f s]"
          % (truth[0]["h"], truth[-1]["h"], time.time() - T0))
    if KILLS:
        return finish({})

    # ------------------------------------------------- B1 + B2 table
    section("B1/B2 -- THE LADDER: lam_min(R_h), the Schur core "
            "lam_min(S_h), tau_h  (diagonal ref %.4f)" % DIAG_REF)
    print("    kz   h     n    tau        lamR       lamR/tau   "
          "lamS       lamS/tau  S*w/tau  wcore  neg A/R/S Hay")
    hay_all = True
    for r in full:
        hk = hayns_ok(r)
        if hk is False:
            hay_all = False
        prod = (r["lamS"] * r["wcore"] / r["tau"]
                if r["tau"] > 0 else float("nan"))
        print("    %-4d %-4d %-5d %.3e %.3e %9.2f  %.3e %8.3f  "
              "%7.3f  %.3f  %d/%d/%d  %s"
              % (r["kz"], r["h"], r["n"], r["tau"], r["lamR"],
                 r["lamR"] / r["tau"] if r["tau"] > 0 else
                 float("nan"), r["lamS"],
                 r["lamS"] / r["tau"] if r["tau"] > 0 else
                 float("nan"), prod, r["wcore"], r["negA"],
                 r["negR"], r["negS"],
                 {True: "ok", False: "BRK", None: "skip"}[hk]),
              flush=True)

    # B1 typed
    hh = np.array([r["h"] for r in full], float)
    lamR = np.array([r["lamR"] for r in full], float)
    r0 = float(np.min(lamR))
    if np.all(lamR > 0.0):
        slope = float(np.polyfit(np.log(hh), np.log(lamR), 1)[0])
    else:
        slope = float("nan")
    ok_unif = (r0 >= R_UNIF_BAR
               and np.isfinite(slope) and slope >= SLOPE_TOL)
    b1 = ("OPERATOR-MARGIN-UNIFORM(r0=%.3e)" % r0 if ok_unif
          else "OPERATOR-MARGIN-SHRINKS(slope=%+.3f)" % slope)
    print("\n    B1: min lam_min(R) = %.3e (bar %.0e), log-log "
          "slope vs h %+.3f (tol %+.2f)"
          % (r0, R_UNIF_BAR, slope, SLOPE_TOL))
    print("    B1 honesty: diagonal deep-half ref %.4f (T_m "
          "envelope, theta*=0.700) -- measured OPERATOR floor is "
          "%.3e = %.3f x the diagonal reference"
          % (DIAG_REF, r0, r0 / DIAG_REF))
    check("B1.1 typed: %s" % b1, True)

    # B2 typed
    tau = np.array([r["tau"] for r in full], float)
    lamS = np.array([r["lamS"] for r in full], float)
    msk = (tau > 0.0) & (lamS > 0.0)
    corr = (float(np.corrcoef(np.log(tau[msk]),
                              np.log(lamS[msk]))[0, 1])
            if int(np.sum(msk)) >= 3 else float("nan"))
    ratio_med = float(np.median(lamS[msk] / tau[msk]))
    b2 = ("SCHUR-TAU-TIED(corr=%.4f, med S/tau=%.2f)"
          % (corr, ratio_med)
          if np.isfinite(corr) and corr >= TIED_CORR
          else "SCHUR-TAU-LOOSE(corr=%.4f)" % corr)
    prods = np.array([r["lamS"] * r["wcore"] / r["tau"]
                      for r in full if r["tau"] > 0])
    wcs = np.array([r["wcore"] for r in full])
    print("    B2: corr(log lamS, log tau) = %.4f (bar %.2f); "
          "lamS/tau med %.6f range [%.6f, %.6f]"
          % (corr, TIED_CORR, ratio_med,
             float(np.min(lamS[msk] / tau[msk])),
             float(np.max(lamS[msk] / tau[msk]))))
    print("    B2 deviations (v2 transparency): max |lamS/tau-1| "
          "= %.3e; product lamS*wcore/tau med %.6f, max |.-1| = "
          "%.3e; min wcore = %.6f"
          % (float(np.max(np.abs(lamS[msk] / tau[msk] - 1.0))),
             float(np.median(prods)),
             float(np.max(np.abs(prods - 1.0))),
             float(np.min(wcs))))
    check("B2.1 typed: %s" % b2, True)
    check("B2.2 WARD truth all-PSD (A, R, S) on every full-core "
          "rung",
          all(r["negA"] == 0 and r["negR"] == 0 and r["negS"] == 0
              for r in full), kill="K2")

    # ------------------------------------------------------------ B3
    section("B3 -- CORE INHERITANCE: eta_core = "
            "lam_min(S_h^-1/2 S_h+1 S_h^-1/2) (fixed 8x8 frame)")
    rows_t, ncr_t, nh_t, nsk_t = inherit_ladder(truth, "TRUTH")
    for h1, h2, lmH, eta in rows_t:
        print("    h %3d->%3d  lam_min(H_core) %+.4e  eta_core "
              "%.6f" % (h1, h2, lmH, eta))
    b3t = ("CORE-INHERITS" if ncr_t == 0
           else "CORE-CROSSES(n=%d)" % ncr_t)
    if rows_t:
        etas = [e for *_x, e in rows_t]
        print("    truth eta_core: min %.4f med %.4f max %.4f"
              % (min(etas), float(np.median(etas)), max(etas)))
    check("B3.1 typed (truth): %s" % b3t, True)

    print("\n    the smooth world (masses 2 e^{u/2} du):")
    sm = []
    for kz in zones:
        sm.append(gram_anatomy(kz, world_fn=world_smooth))
    sm = [r for r in sm if r is not None]
    sm.sort(key=lambda r: (r["h"], r["kz"]))
    rows_s, ncr_s, nh_s, nsk_s = inherit_ladder(sm, "SMOOTH")
    b3s = ("CORE-SEES-SMOOTH(n_cross=%d, n_hard=%d)"
           % (ncr_s, nh_s) if (ncr_s + nh_s) > 0
           else "CORE-BLIND-TO-SMOOTH")
    check("B3.2 typed (smooth): %s" % b3s, True)

    # ------------------------------------------------------------ C1
    section("C1 -- WARD: the smooth world must violate; the "
            "ledger locates the failure")
    viol = [r for r in sm if r["negA"] > 0]
    print("    smooth ladder: %d rungs built, %d with neg(A) > 0"
          % (len(sm), len(viol)))
    loc = "none"
    if viol:
        for r in viol[:12]:
            hk = hayns_ok(r)
            print("      kz %-3d h %4d: neg(A) %d = neg(R) %s + "
                  "neg(S) %s  (tau %.3e, Hayns %s)"
                  % (r["kz"], r["h"], r["negA"],
                     r.get("negR", "n/a") if hk is not None
                     else "n/a",
                     r.get("negS", "n/a") if hk is not None
                     else "n/a", r["tau"],
                     {True: "ok", False: "BROKEN",
                      None: "skip"}[hk]))
        if len(viol) > 12:
            print("      ... (%d more violating rungs)"
                  % (len(viol) - 12))
        in_r = sum(1 for r in viol if r.get("negR", 0) > 0)
        in_s = sum(1 for r in viol if r.get("negS", 0) > 0)
        if in_r > 0 and in_s == 0:
            loc = "VIOLATION-IN-R"
        elif in_s > 0 and in_r == 0:
            loc = "VIOLATION-IN-S"
        else:
            loc = "VIOLATION-MIXED"
    elif ncr_s > 0:
        loc = "VIOLATION-IN-FLOW"
    fired = bool(viol) or ncr_s > 0
    print("    location: %s" % loc)
    check("C1.1 WARD smooth violates (rung level or flow level): "
          "%s" % loc, fired, kill="K2")
    check("C0.1 WARD truth wall holds on every rung (neg(A) = 0)",
          all(r["negA"] == 0 for r in truth), kill="K2")

    # ------------------------------------------------------------ B4
    section("B4 -- PER-PRIME GRAIN on the fixed 8x8 core "
            "(leave-one-prime-out at kz %s; primes %s)"
            % (GRAIN_KZ, GRAIN_PRIMES))
    grain_ok = True
    grain_defects = []
    grain_reasons = []
    by_kz = {r["kz"]: r for r in full}
    for kz in GRAIN_KZ:
        base = by_kz.get(kz)
        if base is None:
            grain_ok = False
            grain_reasons.append("base frame loss")
            print("    kz %-3d: BASE FRAME LOSS (core incomplete)"
                  % kz)
            continue
        S0 = base["S"]
        nS0 = float(np.linalg.norm(S0))
        Dsum = np.zeros_like(S0)
        print("    kz %-3d h %4d (lam_min S %.3e):"
              % (kz, base["h"], base["lamS"]))
        all_res = True
        frame_loss = False
        for p in GRAIN_PRIMES:
            rp = gram_anatomy(kz,
                              world_fn=world_drop_primes((p,)))
            if rp is None or not rp.get("core_ok"):
                frame_loss = True
                print("      drop p=%-2d : FRAME LOSS" % p)
                continue
            Dp = rp["S"] - S0
            Dsum += Dp
            rel = float(np.linalg.norm(Dp)) / nS0
            all_res &= rel >= RESOLVE_BAR
            print("      drop p=%-2d : ||D_p||_F %.3e  rel %.3e  "
                  "lam_min(S\\p) %+.3e" % (p, np.linalg.norm(Dp),
                                           rel, rp["lamS"]))
        ra = gram_anatomy(kz,
                          world_fn=world_drop_primes(GRAIN_PRIMES))
        if ra is None or not ra.get("core_ok") or frame_loss:
            grain_ok = False
            grain_reasons.append("frame loss")
            print("      joint drop: FRAME LOSS -> GRAIN-DEAD "
                  "at this rung")
            continue
        Dall = ra["S"] - S0
        defect = (float(np.linalg.norm(Dall - Dsum))
                  / max(float(np.linalg.norm(Dall)), 1e-300))
        grain_defects.append(defect)
        print("      joint drop: ||D_all||_F %.3e  additivity "
              "defect %.4f (bar %.2f)  lam_min(S\\all) %+.3e"
              % (np.linalg.norm(Dall), defect, GRAIN_DEF_BAR,
                 ra["lamS"]), flush=True)
        if not all_res:
            grain_ok = False
            grain_reasons.append("response unresolved")
        if defect > GRAIN_DEF_BAR:
            grain_ok = False
            grain_reasons.append("additivity defect > bar")
    reasons = " + ".join(sorted(set(grain_reasons))) \
        if grain_reasons else "no rung evaluable"
    b4 = ("CORE-GRAIN-ACCESSIBLE(max defect=%.4f)"
          % (max(grain_defects) if grain_defects else
             float("nan"))
          if grain_ok and grain_defects
          else "CORE-GRAIN-DEAD(%s)" % reasons)
    check("B4.1 typed: %s" % b4, True)

    # ------------------------------------------------------------ C2
    section("C2 -- controls at kz %d: Epstein + scramble frame "
            "status" % CTRL_KZ)
    rr9 = window_of(CTRL_KZ)
    N_E = int(math.floor(math.exp(2.0 * rr9["alpha"]))) + 1
    lamE_ = lambda_eps(N_E)
    nn = np.nonzero(np.abs(lamE_) > 1e-12)[0]
    ctl = {"Epstein": gram_anatomy(
               CTRL_KZ, comb=(np.log(nn.astype(float)),
                              2.0 * lamE_[nn]
                              / np.sqrt(nn.astype(float)))),
           "scramble": gram_anatomy(CTRL_KZ, scramble_seed=1)}
    fired_all = True
    hay_ctl = True
    for name, r in ctl.items():
        if r is None:
            print("    %-9s: chain dies -> fires (frame death)"
                  % name)
            continue
        f = r["negA"] > 0
        fired_all &= f
        hk = hayns_ok(r)
        if hk is False:
            hay_ctl = False
        print("    %-9s: tau %+.3e  neg(A) %d = neg(R) %s + "
              "neg(S) %s  Hayns %s -> %s"
              % (name, r["tau"], r["negA"],
                 r.get("negR", "-"), r.get("negS", "-"),
                 {True: "ok", False: "BROKEN",
                  None: "skip"}[hk],
                 "FIRES" if f else "SILENT"), flush=True)
    check("C2.1 WARD both controls fire (neg(A) > 0)", fired_all,
          kill="K2")
    hay_sm = all(hayns_ok(r) is not False for r in sm)
    check("B2.3 WARD Haynsworth integer identity on every "
          "evaluable rung (truth/smooth/controls)",
          hay_all and hay_sm and hay_ctl, kill="K2")

    # ------------------------------------------------------------ B5
    section("B5 -- THE REDUCTION STATEMENT (measured shadow)")
    print("    IF  lam_min(R_h) >= r_0 > 0 uniformly in h "
          "(measured candidate r_0 = %.3e; typed %s)" % (r0, b1))
    print("    THEN (Haynsworth, warded above)  the wall "
          "A_h >= 0  <=>  S_h >= 0 for the FIXED 8x8 family")
    print("    at the core aliases %s -- the RH wand as a "
          "fixed-dimension statement." % (list(CORE_J),))
    print("    finite shadow: the B2 ladder (lam_min(S) ~ "
          "tau-scale: %s) and the B3 inheritance (%s)."
          % (b2, b3t))
    print("    open pieces: (1) the uniform R-margin theorem "
          "(B1 measured: %s -- the diagonal +%.4f envelope does "
          "NOT transfer to the operator block as measured); "
          "(2) the core inheritance theorem." % (b1, DIAG_REF))
    check("B5.1 reduction statement printed", True)

    return finish(dict(b1=b1, b2=b2, b3t=b3t, b3s=b3s, b4=b4,
                       loc=loc))


def finish(labels):
    section("V -- FROZEN VERDICT")
    n_pass = sum(1 for _n, okk in CHECKS if okk)
    n_tot = len(CHECKS)
    if KILLS:
        VERDICT = {"K1": "PIPELINE-BROKEN",
                   "K2": "WARD-BROKEN"}[KILLS[0]]
        print("\n  VERDICT: %s" % VERDICT)
    else:
        VERDICT = ("DEEPCORESCHUR-MEASURED / %(b1)s / %(b2)s / "
                   "%(b3t)s / %(b3s)s / %(b4)s [%(loc)s]"
                   % labels)
        print("\n  VERDICT: %s" % VERDICT)
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed"
          % (time.time() - T0, n_tot, n_tot - n_pass))
    return 0 if n_pass == n_tot else 1


if __name__ == "__main__":
    raise SystemExit(main())
