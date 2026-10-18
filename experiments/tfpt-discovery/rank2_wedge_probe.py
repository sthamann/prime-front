#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""rank2_wedge_probe -- PRIME.PORT.RANK2.WEDGE.01
(EXPLORATION ONLY, experiments/; round 57, reviewer top priority:
does the congruence increment H_h admit an EXACT (or controlled)
signed rank-2 normal form H = uu* - vv*, and is the wall margin
the reviewer's wedge formula?  2026-08-09.)

THE QUESTION (frozen): relative_congruence_probe (round 51,
PRIME.PORT.RELCONG.01) established the exact congruence
A_{h+1} = A_h^{1/2}(I + H_h)A_h^{1/2} with hermitian
H_h = A_h^{-1/2} Delta_h A_h^{-1/2} and margin eta_h = 1 +
lambda_min(H_h) (truth min 0.0050 on 31 full-window pairs).
normalized_core_update_probe (round 55, PRIME.PORT.NORMALIZED.
CORE.01) showed the 8x8 core update U is effectively 2-dim in
energy BUT positivity is carried by the off-mode 2.5% -- exact
rank 2 is NOT guaranteed and must be tested honestly.  The
reviewer's wedge frame: if H = uu* - vv* then
    det(I + H) = (1 + |u|^2)(1 - |v|^2) + |<u,v>|^2
               = 1 + |u|^2 - |v|^2 - |u ^ v|^2,
with |u ^ v|^2 := |u|^2 |v|^2 - |<u,v>|^2 (Gram determinant),
and the wedge margin
    Delta_wedge := 1 - |v|^2 + |<u,v>|^2 / (1 + |u|^2)
                 = det(I + H) / (1 + |u|^2)
is the Schur-complement margin of the dangerous direction:
"two directions are safe while their common area stays
controlled".  This probe measures the signed rank census of
H_h, tests the wedge formula against the TRUE margin, and makes
the danger bookkeeping (|v|^2 vs the coupling rescue term)
explicit -- on the FULL 12x12 window AND the 8x8 core.
READ-ONLY v563.

THE TWO LADDERS (frozen, predecessors verbatim):
  FULL WINDOW: all frame-A zones h <= 900, 12x12 window
    compression at J = {2,...,24}, consecutive full-window
    pairs, A_h = I - C_J(h), Delta_h = C_J(h) - C_J(h+1),
    H_h = A_h^{-1/2} Delta_h A_h^{-1/2}
    (relative_congruence_probe verbatim, with the window
    compression assembled as C_J = E_ww + Y, Y = E_wo Z,
    Z = (I - E_oo)^{-1} E_ow -- identical floats, but keeping
    the coupling blocks for the telescoping split).
  8x8 CORE: the 42-rung deepcore ladder, full wall A = I - G on
    all folded neg nodes, fixed-core Schur S_h = B_h - Y_h at
    CORE_J = {2,...,16}, consecutive full-core steps,
    H_core = S_h^{-1/2} (S_{h+1} - S_h) S_h^{-1/2}
    (deepcore_schur_reduction / normalized_core_update
    verbatim; eta_core = 1 + lambda_min(H_core)).

THE FROZEN CONSTRUCTIVE SPLIT (R2/R3; ONE split, frozen before
the run): the exact exterior telescoping (normalized_core N2,
identical algebra for the window compression) writes the
increment on the retained block as
    Delta = -(DEww) - [t_dx + t_dz + t_new - t_old]   (window)
    DS    =   DB    - [t_dx + t_dz + t_new - t_old]   (core),
t_dx = coupling increment on the persisting exterior, t_dz =
exterior resolvent update, t_new = new exterior nodes, t_old =
dropped exterior nodes.  FREEZE
    P := sym(-(DEww + t_new))        (window)
         sym(DB - t_new)             (core)
         [the new-node + direct arch/block contribution]
    N := sym(t_dx + t_dz - t_old)    (the rest: persisting-
         exterior coupling/resolvent relaxation minus returns),
so Delta = P - N EXACTLY (up to the telescoping ward).  In
H-space G_P = A^{-1/2} P A^{-1/2}, G_N = A^{-1/2} N A^{-1/2};
the constructive vectors are the rank-1 compressions
    u := sqrt(max(lam_max(G_P), 0)) e_max(G_P),
    v := sqrt(max(lam_max(G_N), 0)) e_max(G_N),
NOT mutually orthogonal in general (the honest wedge test);
degenerate sides (top eigenvalue <= 0 -> zero vector) counted.

FROZEN PROTOCOL (2026-08-09; all bars frozen before the run;
each of R1-R3 runs separately for FULL and CORE):

 W   PIPELINE + REPRODUCTION WARDS: W1 (kill -> PIPELINE-
     BROKEN) >= MIN_PAIRS = 20 truth pairs per world, A_h / S_h
     symmetric PD on every truth step, core ladder = 42 rungs
     with >= 30 full-core.  W2 (kill -> WARD-BROKEN)
     reproduction: FULL 31 pairs with min eta = 0.0050; CORE
     min eta_core = 0.0315 (print precision, tol 5.001e-5).
     W3 (kill -> WARD-BROKEN) increment identities: Delta ==
     -(DEww + DY) resp. DS == DB - DY to 1e-12 rel; the
     four-term telescoping reconstructs DY to 1e-9 rel; the
     constructive split reconstructs Delta = P - N to 1e-8 of
     max(||P||, ||N||, ||Delta||).

 R1  THE SIGNED RANK CENSUS (per step, per world): full signed
     spectrum of H; n_+ = #(eig > dust), n_- = #(eig < -dust),
     dust = DUST_REL * max(1, max|eig|), DUST_REL = 1e-10;
     top-2 share = (lam_+ + |lam_-|) / sum|eig| with lam_+ the
     largest positive and lam_- the most negative eigenvalue
     (a missing sign contributes 0); residual after the best
     signed rank-2  H2 = lam_+ e_+ e_+^T - |lam_-| e_- e_-^T:
     res = ||H - H2||_F / ||H||_F.  TYPED per world:
     RANK2-EXACT iff max res < 1e-10; else RANK2-DOMINANT iff
     min top-2 share >= 0.95; else RANK-RICH(median n_+, n_-,
     share).

 R2  THE WEDGE FORMULA (per step, per world, per split):
     (a) EIGEN SPLIT u = sqrt(lam_+) e_+, v = sqrt(|lam_-|)
     e_- (orthogonal by construction, <u,v> = 0 exactly --
     stated); (b) the FROZEN CONSTRUCTIVE SPLIT above (u,v not
     orthogonal).  For each: Delta_wedge = 1 - |v|^2 +
     <u,v>^2/(1 + |u|^2), geometric form geo = 1 + |u|^2 -
     |v|^2 - (|u|^2|v|^2 - <u,v>^2); WARD (kill ->
     WARD-BROKEN): |Delta_wedge (1 + |u|^2) - geo| <= 1e-10
     max(1, |geo|) on every evaluation (the algebraic
     equivalence).  Compare against the TRUE margin eta = 1 +
     lambda_min(H): ladder of both printed, rel error
     |dw - eta| / |eta| per step.  TYPED per (world, split):
     WEDGE-WRONG(n) iff sign(dw) disagrees with sign(eta) on n
     >= 1 steps; else WEDGE-EXACT iff max rel < 1e-8 (only
     possible if RANK2-EXACT); else WEDGE-PROXY(median, worst).
     Constructive-split capture ||H - (uu^T - vv^T)||_F /
     ||H||_F printed (median, worst) -- the rank-2 shadow
     quality of the constructive vectors.

 R3  THE MARGIN LEDGER IN WEDGE COORDINATES (constructive
     split; for the eigen split the coupling term is
     identically 0, stated): per step print |u|^2, |v|^2,
     <u,v>^2, |u ^ v|^2, Delta_wedge, true eta; the danger
     census: count steps with |v|^2 > 1 (the naive one-
     direction bound 1 - |v|^2 fails) and steps where the
     coupling term is DECISIVE (1 - |v|^2 <= 0 AND Delta_wedge
     > 0: without the common-area term the wedge margin would
     go negative).  REPORT (no bar): where the danger sits.

 C   CONTROLS (kill -> WARD-BROKEN):
     C1 SMOOTH WORLD: the congruence machinery must be
        NORM-DEAD as measured before -- window: 28 smooth
        full-window pairs, ALL 28 CONE-EXITED (A_h indefinite;
        relative_congruence SPEC v2 (ii) reproduction); core:
        neg(A) > 0 on >= 1 smooth rung (normalized_core C1).
     C2 SCRAMBLE at kz 9 (seed 1): window frame must die
        (window unavailable OR lam(C_J) > 1 OR exterior
        supercritical); core wall must break (neg(A) > 0 or
        chain death).
     C3 RANDOM-ROTATION NULL for R1 (both worlds): replace e_-
        by a random unit vector orthogonal to e_+ (weight
        sqrt(|lam_-|) kept; NDRAW = 16 draws/step, seed
        20260809): the median null rank-2 residual must exceed
        the true rank-2 residual on EVERY step (else the
        census/residual instrument is insensitive).

KILLS: K1 pipeline ward breaks -> PIPELINE-BROKEN; KW a
reproduction / identity / equivalence / control ward breaks ->
WARD-BROKEN.

VERDICT (frozen enum): RANK2WEDGE-MEASURED with typed sublabels
R1[full=..., core=...] (RANK2-EXACT / RANK2-DOMINANT /
RANK-RICH), R2eig[full=..., core=...] and R2constr[full=...,
core=...] (WEDGE-EXACT / WEDGE-PROXY / WEDGE-WRONG), R3
rescue counts; else PIPELINE-BROKEN / WARD-BROKEN.

FROZEN BARS: JWIN = (2,...,24); CORE_J = (2,...,16);
H_DEEP_MAX = 900; MIN_PAIRS = 20; MIN_CORE_RUNGS = 30;
N_RUNGS_EXP = 42; REF_WIN = (31 pairs, min eta 0.0050);
REF_CORE_ETA = 0.0315; REF_SMOOTH = (28 pairs, 28 CONE-EXITED);
ROUND_TOL = 5.001e-5; DUST_REL = 1e-10; RANK2_EXACT_BAR =
1e-10; DOM_SHARE = 0.95; WEDGE_EXACT_BAR = 1e-8; EQUIV_WARD =
1e-10; ID_WARD = 1e-12; TELE_WARD = 1e-9; SPLIT_WARD = 1e-8;
NDRAW = 16; NULL_SEED = 20260809; CTRL_KZ = 9; scramble seed 1.

SPEC v1 (2026-08-09, frozen pre-run).  Mechanical
concretizations frozen with v1: (i) core.build_window memoized
per (kz, seed) (pure memoization, bit-identical physics);
(ii) the window compression C_J is assembled as E_ww + sym(E_wo
Z) with Z = (I - E_oo)^{-1} E_ow -- the identical arithmetic of
the predecessor's one-shot formula, retained blocks reused for
the telescoping; (iii) if a truth step has no positive (resp.
negative) eigenvalue the corresponding eigen-split vector is
the zero vector and the step is counted (census prints it);
(iv) the null draw uses a Gaussian vector projected orthogonal
to e_+ and normalized; if H has no positive eigenvalue the
projection is skipped (pure random direction); (v) sign
disagreement in R2 means dw <= 0 while eta > 0 or dw >= 0
while eta < 0 (truth eta > 0 is warded, so in practice
dw <= 0); (vi) R3 also prints, report-only, the closest
approach max(|v|^2) and the coupling term's median share of
Delta_wedge, so "where does the danger sit" has a quantitative
answer even if the rescue count is zero.

NO RH claim -- a signed-rank/wedge measurement on compressed
window truncations of the deployed v563 ladder is a statement
about the deployed ladder, not a theorem about zeros.

FIREWALL: no zeros, no prime oracles (AST scan; banned ids
zetazero / nzeros / primerange / isprime / primepi / nextprime /
prevprime); v563 READ-ONLY; RNG only inside the declared null
(seed 20260809) and scramble (seed 1) controls; stdout only.
No marker moves.

Sources (read-only): v563_paper2_readouts; window compression +
pair ladder verbatim from relative_congruence_probe.py
(PRIME.PORT.RELCONG.01, round 51); full wall + fixed-core Schur
+ exact exterior telescoping verbatim from
normalized_core_update_probe.py (PRIME.PORT.NORMALIZED.CORE.01,
round 55) and deepcore_schur_reduction_probe.py
(PRIME.PORT.DEEPCORE.SCHUR.01, round 51); smooth-mass world
from lattice_parametrix_probe.py (B1).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/rank2_wedge_probe.py
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
REF_CORE_MINETA = 0.0315       # W2 core reproduction
REF_N_SMOOTH_PAIRS = 28        # C1 window smooth reproduction
REF_SMOOTH_CONE = 28
ROUND_TOL = 5.001e-5
DUST_REL = 1e-10               # R1 census dust
RANK2_EXACT_BAR = 1e-10        # R1 typing
DOM_SHARE = 0.95               # R1 typing
WEDGE_EXACT_BAR = 1e-8         # R2 typing
EQUIV_WARD = 1e-10             # R2 algebraic equivalence (kill)
ID_WARD = 1e-12                # W3 increment identity (kill)
TELE_WARD = 1e-9               # W3 telescoping (kill)
SPLIT_WARD = 1e-8              # W3 constructive split (kill)
NDRAW = 16                     # C3 null draws per step
NULL_SEED = 20260809
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
    Lanczos chain -> Gram E on the folded neg nodes (verbatim
    arithmetic of both predecessors).  Returns None on chain
    death; 'TOO-DEEP' beyond the ladder cut."""
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
    Z), Z = (I - E_oo)^{-1} E_ow (relative_congruence verbatim
    arithmetic; SPEC v1 (ii)), with coupling blocks + exterior
    fold labels retained for the telescoping."""
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
        out["lamO"] = float(np.linalg.eigvalsh(
            E[np.ix_(io, io)])[-1])
        out["lamC"] = float(np.linalg.eigvalsh(out["CJ"])[-1])
    return out


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


H_LADDER_MAX_CORE = 900


def gram_anatomy(kz, comb=None, scramble_seed=None):
    """8x8 CORE rung: full wall A = I - E on the folded neg
    nodes, fixed-core split, Schur S = B - Y (normalized_core /
    deepcore verbatim), blocks retained for the telescoping."""
    g = neg_gram(kz, scramble_seed=scramble_seed, comb=comb)
    if not isinstance(g, dict):
        return None if g is None else None
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
    out.update(B=B, Xcpl=Xc, Z=Z, ext=uf_n[ib], S=S, Y=Y,
               lamS=float(evS[0]),
               negS=int(np.sum(evS < 0.0)),
               negR=int(np.sum(np.linalg.eigvalsh(R) < 0.0)))
    return out


# --------------------------------------- shared analysis pieces
def inv_sqrt(M):
    w, V = np.linalg.eigh(M)
    return V @ np.diag(w ** -0.5) @ V.T


def telescope(Xc1, Z1, uf1, Xc2, Z2, uf2):
    """Exact four-term telescoping of DY = Y' - Y over the
    common / dropped / new exterior fold labels
    (normalized_core N2 verbatim)."""
    com, i1, i2 = np.intersect1d(uf1, uf2, return_indices=True)
    o1 = np.setdiff1d(np.arange(len(uf1)), i1)
    n2i = np.setdiff1d(np.arange(len(uf2)), i2)
    t_dx = (Xc2[:, i2] - Xc1[:, i1]) @ Z1[i1, :]
    t_dz = Xc2[:, i2] @ (Z2[i2, :] - Z1[i1, :])
    t_new = Xc2[:, n2i] @ Z2[n2i, :]
    t_old = Xc1[:, o1] @ Z1[o1, :]
    return t_dx, t_dz, t_new, t_old


def census(H):
    """R1: signed spectrum census + best signed rank-2."""
    lam, V = np.linalg.eigh(sym(H))
    amax = float(np.max(np.abs(lam)))
    dust = DUST_REL * max(1.0, amax)
    ip = int(np.argmax(lam))
    im = int(np.argmin(lam))
    lp = float(lam[ip])
    ln = float(lam[im])
    nH = float(np.linalg.norm(H))
    u = (math.sqrt(lp) * V[:, ip] if lp > 0.0
         else np.zeros(len(lam)))
    v = (math.sqrt(-ln) * V[:, im] if ln < 0.0
         else np.zeros(len(lam)))
    H2 = np.outer(u, u) - np.outer(v, v)
    res = float(np.linalg.norm(H - H2)) / max(nH, 1e-300)
    tot = float(np.sum(np.abs(lam)))
    share = (max(lp, 0.0) + max(-ln, 0.0)) / max(tot, 1e-300)
    return dict(lam=lam,
                n_pos=int(np.sum(lam > dust)),
                n_neg=int(np.sum(lam < -dust)),
                lp=lp, ln=ln, share=share, res=res,
                u=u, v=v,
                e_pos=(V[:, ip] if lp > 0.0 else None),
                w_neg=(math.sqrt(-ln) if ln < 0.0 else 0.0))


_EQUIV_DEV = [0.0]


def wedge(u, v):
    """Delta_wedge + geometric form + the equivalence ward."""
    uu2 = float(u @ u)
    vv2 = float(v @ v)
    uv = float(u @ v)
    wedge2 = uu2 * vv2 - uv * uv
    dw = 1.0 - vv2 + uv * uv / (1.0 + uu2)
    geo = 1.0 + uu2 - vv2 - wedge2
    dev = abs(dw * (1.0 + uu2) - geo) / max(1.0, abs(geo))
    _EQUIV_DEV[0] = max(_EQUIV_DEV[0], dev)
    return uu2, vv2, uv * uv, wedge2, dw


def top_vec(G):
    """Rank-1 compression of the top positive eigenpair; zero
    vector if the top eigenvalue is <= 0 (SPEC v1, degenerate
    side counted by the caller)."""
    w, V = np.linalg.eigh(sym(G))
    if float(w[-1]) > 0.0:
        return math.sqrt(float(w[-1])) * V[:, -1], False
    return np.zeros(G.shape[0]), True


def wedge_type(dws, etas, rels):
    n_sign = sum(1 for dw, et in zip(dws, etas)
                 if (dw <= 0.0 < et) or (dw >= 0.0 > et))
    if n_sign:
        return "WEDGE-WRONG(n=%d)" % n_sign
    if float(np.max(rels)) < WEDGE_EXACT_BAR:
        return "WEDGE-EXACT"
    return ("WEDGE-PROXY(med=%.4f,worst=%.4f)"
            % (float(np.median(rels)), float(np.max(rels))))


def rank_type(cens):
    res_max = float(np.max([c["res"] for c in cens]))
    share_min = float(np.min([c["share"] for c in cens]))
    if res_max < RANK2_EXACT_BAR:
        return "RANK2-EXACT"
    if share_min >= DOM_SHARE:
        return "RANK2-DOMINANT(min share=%.4f)" % share_min
    return ("RANK-RICH(med n+=%d, n-=%d, share=%.3f)"
            % (int(np.median([c["n_pos"] for c in cens])),
               int(np.median([c["n_neg"] for c in cens])),
               float(np.median([c["share"] for c in cens]))))


def build_steps_window(rungs):
    """Consecutive full-window pairs -> H, eta, telescoping,
    constructive split (PD branch; non-PD counted)."""
    rows, n_skip, n_cone = [], 0, 0
    n = len(JWIN)
    dev_id, dev_tel, dev_spl = 0.0, 0.0, 0.0
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
        P = sym(-(DEww + t_new))
        N = sym(t_dx + t_dz - t_old)
        dev_spl = max(dev_spl, float(np.linalg.norm(
            Delta - (P - N))) / max(
                float(np.linalg.norm(P)),
                float(np.linalg.norm(N)),
                float(np.linalg.norm(Delta)), 1e-300))
        Wi = Vw @ np.diag(ew ** -0.5) @ Vw.T
        H = sym(Wi @ Delta @ Wi)
        rows.append(dict(ha=r1["h"], hb=r2["h"], H=H,
                         eta=1.0 + float(np.linalg.eigvalsh(
                             H)[0]),
                         GP=sym(Wi @ P @ Wi),
                         GN=sym(Wi @ N @ Wi)))
    return rows, n_skip, n_cone, (dev_id, dev_tel, dev_spl)


def build_steps_core(truth):
    """Consecutive full-core steps -> H_core, eta_core,
    telescoping, constructive split (normalized_core step
    filter verbatim)."""
    rows = []
    dev_id, dev_tel, dev_spl = 0.0, 0.0, 0.0
    for r1, r2 in zip(truth, truth[1:]):
        if (r1 is None or r2 is None or not r1.get("core_ok")
                or not r2.get("core_ok")):
            continue
        if r1["lamS"] <= 0.0 or r1["negA"] > 0:
            continue
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
        P = sym(DB - t_new)
        N = sym(t_dx + t_dz - t_old)
        dev_spl = max(dev_spl, float(np.linalg.norm(
            DS - (P - N))) / max(
                float(np.linalg.norm(P)),
                float(np.linalg.norm(N)),
                float(np.linalg.norm(DS)), 1e-300))
        Wi = inv_sqrt(r1["S"])
        H = sym(Wi @ DS @ Wi)
        rows.append(dict(ha=r1["h"], hb=r2["h"], H=H,
                         eta=1.0 + float(np.linalg.eigvalsh(
                             H)[0]),
                         GP=sym(Wi @ P @ Wi),
                         GN=sym(Wi @ N @ Wi)))
    return rows, (dev_id, dev_tel, dev_spl)


def analyze_world(tag, rows):
    """R1 census + R2 wedge (eigen + constructive) + R3 ledger
    for one world; returns the typed labels + summaries."""
    cens = [census(r["H"]) for r in rows]
    etas = np.array([r["eta"] for r in rows])

    # ------------------------------------------------------ R1
    section("R1[%s] -- THE SIGNED RANK CENSUS of H (%d steps)"
            % (tag, len(rows)))
    print("    step        n+  n-  lam_+      lam_-      "
          "top2 share  rank2 res")
    for r, c in zip(rows, cens):
        print("    h %3d->%3d  %2d  %2d  %+.4e %+.4e   "
              "%.6f   %.4e"
              % (r["ha"], r["hb"], c["n_pos"], c["n_neg"],
                 c["lp"], c["ln"], c["share"], c["res"]))
    shares = [c["share"] for c in cens]
    ress = [c["res"] for c in cens]
    r1lab = rank_type(cens)
    print("\n    top-2 share: min %.4f med %.4f | rank-2 "
          "residual: med %.4f max %.4f"
          % (float(np.min(shares)), float(np.median(shares)),
             float(np.median(ress)), float(np.max(ress))))
    check("R1.%s typed: %s" % (tag, r1lab), True)

    # ------------------------------------------------ R2 eigen
    section("R2[%s] -- THE WEDGE FORMULA, eigen split "
            "(u = sqrt(lam_+) e_+, v = sqrt(|lam_-|) e_-; "
            "<u,v> = 0 exactly)" % tag)
    print("    step        |u|^2     |v|^2     Delta_wedge  "
          "true eta   rel err")
    dwe, rele = [], []
    n_deg_eig = 0
    for r, c in zip(rows, cens):
        if c["e_pos"] is None or c["w_neg"] == 0.0:
            n_deg_eig += 1
        uu2, vv2, _uv2, _w2, dw = wedge(c["u"], c["v"])
        rel = abs(dw - r["eta"]) / max(abs(r["eta"]), 1e-300)
        dwe.append(dw)
        rele.append(rel)
        print("    h %3d->%3d  %8.5f  %8.5f  %+10.5f  "
              "%+9.5f  %.3e"
              % (r["ha"], r["hb"], uu2, vv2, dw, r["eta"],
                 rel))
    r2e = wedge_type(dwe, etas, rele)
    print("\n    degenerate eigen sides (missing sign): %d; "
          "rel err med %.4e worst %.4e"
          % (n_deg_eig, float(np.median(rele)),
             float(np.max(rele))))
    print("    NOTE: eigen u,v are orthogonal, so the coupling "
          "term <u,v>^2/(1+|u|^2) is identically 0")
    print("    here and Delta_wedge = 1 - |v|^2 = 1 + "
          "lam_min(H2) -- the rank-2 shadow of the margin.")
    check("R2.%s.eigen typed: %s" % (tag, r2e), True)

    # ----------------------------------------- R2 constructive
    section("R2[%s] -- THE WEDGE FORMULA, frozen constructive "
            "split (u from P = new-node/arch side, v from N = "
            "the rest)" % tag)
    dwc, relc, caps = [], [], []
    led = []
    n_deg_u, n_deg_v = 0, 0
    for r in rows:
        u, du = top_vec(r["GP"])
        v, dv = top_vec(r["GN"])
        n_deg_u += int(du)
        n_deg_v += int(dv)
        uu2, vv2, uv2, w2, dw = wedge(u, v)
        rel = abs(dw - r["eta"]) / max(abs(r["eta"]), 1e-300)
        cap = float(np.linalg.norm(
            r["H"] - np.outer(u, u) + np.outer(v, v))) \
            / max(float(np.linalg.norm(r["H"])), 1e-300)
        dwc.append(dw)
        relc.append(rel)
        caps.append(cap)
        led.append((r, uu2, vv2, uv2, w2, dw))
    r2c = wedge_type(dwc, etas, relc)
    print("    rank-2 shadow capture ||H - (uu^T - vv^T)||/"
          "||H||: med %.4f worst %.4f"
          % (float(np.median(caps)), float(np.max(caps))))
    print("    degenerate sides: u (P top eig <= 0) on %d "
          "steps, v (N top eig <= 0) on %d steps"
          % (n_deg_u, n_deg_v))
    print("    wedge vs true eta: rel err med %.4e worst %.4e"
          % (float(np.median(relc)), float(np.max(relc))))
    check("R2.%s.constr typed: %s" % (tag, r2c), True)

    # ------------------------------------------------------ R3
    section("R3[%s] -- THE MARGIN LEDGER in wedge coordinates "
            "(constructive split)" % tag)
    print("    step        |u|^2     |v|^2     <u,v>^2    "
          "|u^v|^2    Delta_wedge  true eta")
    n_danger, n_resc = 0, 0
    coup_shares = []
    for (r, uu2, vv2, uv2, w2, dw) in led:
        danger = vv2 > 1.0
        resc = (1.0 - vv2 <= 0.0) and (dw > 0.0)
        n_danger += int(danger)
        n_resc += int(resc)
        coup = uv2 / (1.0 + uu2)
        coup_shares.append(coup / max(abs(dw), 1e-300))
        print("    h %3d->%3d  %8.5f  %8.5f  %9.6f  %9.6f  "
              "%+10.5f  %+9.5f%s%s"
              % (r["ha"], r["hb"], uu2, vv2, uv2, w2, dw,
                 r["eta"],
                 "  |v|^2>1" if danger else "",
                 "  RESCUED" if resc else ""))
    vmax = float(np.max([x[2] for x in led]))
    print("\n    danger census: |v|^2 > 1 on %d/%d steps; "
          "coupling term DECISIVE (1 - |v|^2 <= 0 yet"
          % (n_danger, len(rows)))
    print("    Delta_wedge > 0) on %d/%d steps; closest "
          "approach max |v|^2 = %.5f (SPEC v1 (vi));"
          % (n_resc, len(rows), vmax))
    print("    coupling term <u,v>^2/(1+|u|^2) median share "
          "of Delta_wedge = %.3e."
          % float(np.median(coup_shares)))
    check("R3.%s danger census reported (danger=%d, "
          "rescued=%d)" % (tag, n_danger, n_resc), True)

    return dict(r1=r1lab, r2e=r2e, r2c=r2c, cens=cens,
                n_danger=n_danger, n_resc=n_resc,
                rele=rele, relc=relc, caps=caps)


def null_rotation(tag, rows, cens, rng):
    """C3: replace e_- by a random unit vector orthogonal to
    e_+ (weight kept); median null rank-2 residual must exceed
    the true residual on every step."""
    n_bad, degr = 0, []
    for r, c in zip(rows, cens):
        if c["w_neg"] == 0.0:
            continue
        H = r["H"]
        nH = max(float(np.linalg.norm(H)), 1e-300)
        Hu = np.outer(c["u"], c["u"])
        vals = []
        for _ in range(NDRAW):
            g = rng.standard_normal(H.shape[0])
            if c["e_pos"] is not None:
                g -= (g @ c["e_pos"]) * c["e_pos"]
            g /= max(float(np.linalg.norm(g)), 1e-300)
            vr = c["w_neg"] * g
            vals.append(float(np.linalg.norm(
                H - Hu + np.outer(vr, vr))) / nH)
        med = float(np.median(vals))
        degr.append(med / max(c["res"], 1e-300))
        if med <= c["res"]:
            n_bad += 1
    print("    %s: median null residual / true residual: "
          "med x%.2f min x%.2f (%d steps, %d draws each)"
          % (tag, float(np.median(degr)), float(np.min(degr)),
             len(degr), NDRAW))
    return n_bad


def main():
    section("PRIME.PORT.RANK2.WEDGE.01 -- signed rank-2 normal "
            "form + the wedge margin (EXPLORATION ONLY)")
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
    check("W2.b REPRODUCTION core: min eta_core %.4f == %.4f "
          "(tol %.1e)"
          % (min_eta_c, REF_CORE_MINETA, ROUND_TOL),
          abs(min_eta_c - REF_CORE_MINETA) <= ROUND_TOL,
          kill="KW")
    for lab, dev in (("window", wdev), ("core", cdev)):
        check("W3.%s increment identity %.1e <= %.0e | "
              "telescoping %.1e <= %.0e | split %.1e <= %.0e"
              % (lab[0], dev[0], ID_WARD, dev[1], TELE_WARD,
                 dev[2], SPLIT_WARD),
              dev[0] <= ID_WARD and dev[1] <= TELE_WARD
              and dev[2] <= SPLIT_WARD, kill="KW")
    check("W3.c truth eta > 0 on every step (both worlds)",
          min_eta_w > 0.0 and min_eta_c > 0.0, kill="KW")
    if KILLS:
        return finish({})

    # -------------------------------------------------- R1-R3
    resw = analyze_world("FULL", wrows)
    resc = analyze_world("CORE", crows)
    check("R2.ward ALGEBRAIC EQUIVALENCE: max |dw(1+|u|^2) - "
          "geo| dev %.2e <= %.0e (all wedge evaluations)"
          % (_EQUIV_DEV[0], EQUIV_WARD),
          _EQUIV_DEV[0] <= EQUIV_WARD, kill="KW")

    # ------------------------------------------------------------ C
    section("C -- controls")
    print("  C1 -- smooth world (congruence machinery must be "
          "NORM-DEAD):")
    n_sp, n_scone = 0, 0
    for r1, r2 in zip(srungs[:-1], srungs[1:]):
        if not (r1.get("full") and r2.get("full")):
            continue
        n_sp += 1
        A1 = np.eye(len(JWIN)) - r1["CJ"]
        if float(np.linalg.eigvalsh(A1)[0]) <= 0.0:
            n_scone += 1
    print("    window: %d smooth full-window pairs, %d "
          "CONE-EXITED (A_h indefinite)" % (n_sp, n_scone))
    check("C1.a window smooth reproduction: %d pairs == %d, "
          "CONE-EXITED %d == %d"
          % (n_sp, REF_N_SMOOTH_PAIRS, n_scone,
             REF_SMOOTH_CONE),
          n_sp == REF_N_SMOOTH_PAIRS
          and n_scone == REF_SMOOTH_CONE, kill="KW")
    n_viol = 0
    for kz in zones:
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

    print("  C3 -- random-rotation null for R1 (seed %d):"
          % NULL_SEED)
    rng = np.random.default_rng(NULL_SEED)
    nb_w = null_rotation("FULL", wrows, resw["cens"], rng)
    nb_c = null_rotation("CORE", crows, resc["cens"], rng)
    check("C3 null degrades on every step (median null res > "
          "true res; failures: full %d, core %d)"
          % (nb_w, nb_c), nb_w == 0 and nb_c == 0, kill="KW")

    return finish(dict(w=resw, c=resc, min_eta_w=min_eta_w,
                       min_eta_c=min_eta_c))


def finish(res):
    section("V -- FROZEN VERDICT")
    n_pass = sum(1 for _n, okk in CHECKS if okk)
    n_tot = len(CHECKS)
    if KILLS:
        VERDICT = {"K1": "PIPELINE-BROKEN",
                   "KW": "WARD-BROKEN"}[KILLS[0]]
        print("\n  VERDICT: %s" % VERDICT)
    else:
        w, c = res["w"], res["c"]
        VERDICT = ("RANK2WEDGE-MEASURED / R1[full=%s, core=%s]"
                   " / R2eig[full=%s, core=%s] / R2constr["
                   "full=%s, core=%s]"
                   % (w["r1"], c["r1"], w["r2e"], c["r2e"],
                      w["r2c"], c["r2c"]))
        print("\n  VERDICT: %s" % VERDICT)
        print("  (true margins: min eta full %.4f, core %.4f; "
              "danger |v|^2 > 1: full %d, core %d; coupling"
              % (res["min_eta_w"], res["min_eta_c"],
                 w["n_danger"], c["n_danger"]))
        print("   DECISIVE: full %d, core %d steps)"
              % (w["n_resc"], c["n_resc"]))
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed"
          % (time.time() - T0, n_tot, n_tot - n_pass))
    return 0 if n_pass == n_tot else 1


if __name__ == "__main__":
    raise SystemExit(main())
