#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""v879 -- PRIME.ENVELOPE.DERIVATION.01 + PRIME.WAVEPACKET.PARTITION.01: THE PARTITION CLOSURE (the compact closing round 37, 2026-08-08/09 night) -- the decomposition chapter of the certificate hunt is closed ENTIRELY, and the analytic core that survives is named and typed.  STRAND 1, THE ENVELOPE DERIVATION (7 checks with the TWO FROZEN-HONEST FAILs T1.4/C.1 pattern-gated at exit 1, NOT refit; verdict ENVELOPE-EMPIRICAL-ONLY (missed: h-uniformity(K1an,K2an), decay); spec SHA 27d9f0a3..., quoting and re-verifying BOTH inherited contract SHAs 4621b899.../5fd6bf61... at run time): THE ANALYTIC CORE OF THE ROUTE -- multiplication by cos th acts EXACTLY tridiagonally on the odd frame (the mirror symmetry closes the top boundary inside the space, A[h-1,h-1] = -1/2; the single rank-2 defect at k = 0; the Christoffel-Darboux telescoping identity at max residual 1.3e-13 on every rung, battery + all five complete-comb holdouts), and the DERIVED pointwise bound |U_ij| <= min(1, [C_int + sqrt((Gp^{-1})_00)(Km_i^{-1/2} + Kp_j^{-1/2})] / |cos thm_i - cos thp_j|) holds with ZERO entrywise violation (max -4.5e-08) and h-UNIFORM source constants -- C_int in [1.232, 2.328] (max/min 1.89 <= 2.0, log-log slope +0.106 <= 0.15) and sqrt((Gp^{-1})_00) in [0.661, 0.899] (slope -0.111) from h = 168 to 1445: THE FIRST ANALYTIC UNIFORMITY STATEMENT OF THE ROUTE, at entrywise grade ('the pointwise bound is DERIVED' printed and gated).  THE STRUCTURAL CLOSURE (the two honest FAILs are the finding): T1.4 -- the analytic envelope certifies NO decay (worst env(8)/env(0) = 1.000; K1an/K2an blow up as h^2, max/min 77.6/94.5): every Pruefer cell contains near-diagonal geometric pairs, so the CELL-envelope decay is cancellation-carried and provably NOT entrywise-derivable; C.1 -- under the frozen K1an-ratio criterion Epstein (1.8 < 2.0) and scramble (1.1) 'transfer', while C_int itself DISCRIMINATES (1.41 truth / 3.59 Epstein / 12.8 scramble) -- the frozen bar was pointed at the wrong constant, kept and typed.  THE GAP DECOMPOSITION: no predeclared accounting reaches below 3.568 (C1..C4 censuses on all 15 rungs, worst-rung best 4.178, GAP-CLOSABLE False); coarser cells are better but only n = 1 would reach ~1; the diagonal share is 15-24 percent; Sum_r eps_r = 6.88-12.89 with the complete-comb deep holdouts IN/ABOVE the battery band (11.8-12.9, slope +0.237) -- the local defects are real on clean data, alpha-uniform, NOT a truncation artifact: NO cell-partition Cotlar accounting of this family can certify.  STRAND 2, THE WAVE-PACKET DECISION (6/6, zero fails, verdict PARTITION-CLASS-CLOSED; spec SHA 2199e9b1..., re-verifying the whole contract chain incl. the envelope spec 27d9f0a3...): the typed next object of strand 1 -- a NON-CELL partition where the diagonal carries the mass -- is built honestly and KILLED BY MEASUREMENT: both wave-packet designs (rank-Gabor on the node-rank phase space; chain packets through the exact discrete OP transform) are HONEST TIGHT FRAMES on every rung (||B||_2 = ||C^G||_2 exact at 1e-8 rel; conds <= 16; the gauge identity sigma_max(C^G)^2 = 1 - lam1(Delta) exact); the Gabor envelope DECAYS in phase space (0.529 -> 0.007 at kz 243, decay 0.0127 -- the FIRST partition of the program to show decay) and the discrimination is massive (truth E_schur 4.985 vs Epstein 128.7 vs scramble 9006.6); BUT the diagonal does NOT carry under ANY pairing (D1 nearest-packet share <= 0.070; D2 empirical-partner share <= 0.183 at injectivity <= 0.77; row concentration <= 0.14 -- diagonal mass <= 18 percent) and the Schur constant GROWS (best design 4.985 -> 9.222 along the ladder, log-log slope +0.295; chain design 6.4-14.5; every non-killed design >= 3.5 on every rung).  THE TERMINAL STATEMENT (the round's content): the cancellation that holds ||C|| <= 1 is ATOMICALLY GLOBAL -- it lives in NO partition of this family (Pruefer cells at any resolution, wave packets on either natural phase space, any tight-frame decomposition tested or predeclared); no partition-based accounting can certify the wall; certificate routes must be NON-DECOMPOSITIONAL (eigen-enclosure / Loewner-order / passivity arguments that treat the operator whole -- all three measured territory).  THE SURVIVING ASSETS (carried forward, typed): the exact tridiagonal multiplication identity with its rank-2 boundary defect, the h-uniform derived entrywise constants (C_int, (Gp^{-1})_00, min K), and their SOURCE-LAW PERSISTENCE as h -> infty as the named open object.  ONE module from two probes (re-executed verbatim, embedded BYTE-EXACT, ~25 min).  NO marker moves.  NO RH claim.  Python-only per GATE.WOLFRAM.02.

PROVENANCE: both probes frozen + SHA-hashed before first run (FROZEN_SPEC
SHA-256 gated below); the envelope probe QUOTES and re-verifies the v1/v2
Cotlar contract SHAs (4621b899... / 5fd6bf61...) against the committed
pruefer_compensation_probe / cotlar_v2_complete_comb_probe at run time,
and the wave-packet probe re-verifies the WHOLE chain including the
envelope spec 27d9f0a3... -- the round-34 -> 35 -> 36 -> 37 contract
chain is machine-warded end to end.  Executed 2026-08-08/09 night,
re-executed verbatim at this promotion in isolated namespaces with the
byte-equality provenance ward; the wave-packet probe imports
envelope_derivation_gap_probe READ-ONLY (resolved to the embedded
executed copy via sys.modules -- the same source, byte-exact).  The
probes import v563_paper2_readouts, gauss_node_unitary_probe,
pruefer_compensation_probe (v873) and cotlar_v2_complete_comb_probe
(v877) READ-ONLY -- not re-gated here.  The TWO honest FAILs T1.4/C.1
are FROZEN findings (the decay non-derivability and the mistargeted
discrimination bar) -- pattern-gated at exit 1, NOT refit.  NO RH claim
anywhere; the closure is a route statement about decompositional
accountings, not a positivity claim.
"""

import contextlib
import io
import os
import re
import sys
import time
import types

_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)

EXPECT_SHA_ENVELOPE = ("27d9f0a30b8e2cc21e14b7003f42aa27db715eb6"
                       "acd3d0968013af191d92181c")
EXPECT_SHA_WAVEPACKET = ("2199e9b1dff0bdd7b7bb3169b8570fb81b4a9c6a"
                         "d753b5cba74342803edeb21a")

# ------------- frozen probe sources (embedded BYTE-EXACT, raw strings)
_SRC_ENVELOPE = r'''
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""envelope_derivation_gap_probe -- PRIME.ENVELOPE.DERIVATION.01
(EXPLORATION ONLY, experiments/; direct follow-up to
COTLAR-BOUNDED-V2, 2026-08-08 late night).

THE REOPENED ROUTE'S NEXT STEP.  v2 established: corrected
Cotlar sums bounded (S_U ~ 5.9, S_C ~ 4.3, slopes ~ 0.007);
envelope constants K1 ~ 8.2, K2 ~ 40.4 h-stable on all five
complete-comb holdouts.  But bounded != certifying: the
certificate shape needs the (damped) Cotlar constant BELOW 1,
and the local inequality carries sum eps_r ~ 7-10.

THE ANALYTIC OBJECT (identified here from the deployed
construction, source-only): U[i,j] = K(thm_i, thp_j) /
sqrt(K(thm_i,thm_i) K(thp_j,thp_j)) where K(th, ph) =
f(th) Gp^{-1} f(ph)^H is the reproducing kernel of the odd
frame space under the plus measure (f_k(th) = e^{-i th k}
- e^{-i th (2h-1-k)}, k = 0..h-1).  THE DERIVATION
(Christoffel-Darboux telescoping; the standard oscillation-
theory shape; ALL constants from source data): multiplication
by cos th acts EXACTLY tridiagonally on the frame,
  cos th f(th) = A f(th) + (rho(th)/2) e_0,
  A = (S + S^T)/2 with A[h-1, h-1] = -1/2 (the mirror closes
  the top boundary inside the space),
  rho(th) = e^{i th} - e^{-2 i h th}, |rho| <= 2,
so with x = cos thm_i, y = cos thp_j:
  (x - y) K = f(th)^T (A Gi - Gi A) f(ph)^H + boundary,
  Gi = Gp^{-1}; [A, Gi] = -Gi [A, Gp] Gi is rank <= 2 by the
  G-symmetry of multiplication (defect only at k = 0).
RKHS Cauchy-Schwarz (|f(th)^T u| <= sqrt(K_thth) ||u||_Gp)
per singular direction of Qm = A Gi - Gi A gives
  |U_ij| <= min(1, [C_int + sqrt(Gi_00)(Km_i^{-1/2}
            + Kp_j^{-1/2})] / |x_i - y_j|),
  C_int = sum_k sigma_k(Qm) ||u_k||_Gp ||w_k||_Gp
(effective rank ~ 2, warded).  |x - y| = 2|sin(dth_geo/2)
sin(sth_geo/2)| -- the sum-frequency factor is exactly the
pi-resonance channel.  Blocks: per-cell Schur bounds
sigma_an(r) from the entrywise bounds on the DEPLOYED
(Pruefer) cells, N_an[r,s] = sigma_an(r) sigma_an(s)
>= ||X_r^* X_s||.  WARDS: the CD identity at machine
precision, the rank of Qm, entrywise |U| <= bnd, blockwise
N_meas <= N_an.

TASKS: (1) the derivation + wards (entrywise, blockwise,
analytic >= measured everywhere; h-uniformity + nontrivial
decay typed); (2) the certificate-gap anatomy (cell-count
variants 8/16/32; diagonal share; frozen damped accountings
C1..C4 -- no post-hoc tuning); (3) the local-dominance
revisit at complete-comb deep holdouts (eps_r profiles);
(4) the honest synthesis + the PRIME.KREIN.CONTRACTOR.01
round-36 contract note.  VERDICT (frozen): ENVELOPE-DERIVED /
ENVELOPE-EMPIRICAL-ONLY / GAP-CLOSABLE-SHAPE.  NO RH claim;
writes nothing; no .md; no commits.

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/envelope_derivation_gap_probe.py
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

import v563_paper2_readouts as core            # noqa: E402  (READ-ONLY)
import gauss_node_unitary_probe as gnu         # noqa: E402  (READ-ONLY)
import pruefer_compensation_probe as ppc       # noqa: E402  (READ-ONLY)
import cotlar_v2_complete_comb_probe as cv2    # noqa: E402  (READ-ONLY)

FROZEN_SPEC = """\
PRIME.ENVELOPE.DERIVATION.01 spec v1 (2026-08-08, frozen
before run).  Sample (frozen): battery BATT10 = (9, 13, 15,
23, 26, 32, 40, 52, 64, 82) + all five holdouts (90, 116
in-cap; 142, 177, 243 COMPLETE comb via the v2 extended
builder).  Cells/pairing/sums: the v1/v2 contract verbatim
(SHA 4621b899... / 5fd6bf61...).  TASK 1 (derivation): the
Christoffel-Darboux entrywise bound with source constants
(docstring formulas: C_int from the rank-2 commutator
Qm = A Gi - Gi A via RKHS Cauchy-Schwarz, boundary
sqrt(Gi_00) terms, CS cap 1); per-cell Schur sigma_an on the
DEPLOYED Pruefer cells; N_an = sigma sigma; env_an(d);
(sigma_an = min of the Schur and Frobenius bounds, both
valid); K1_an = max env_an_U (1+d), K2_an = max env_an_C
(1+d)^2 (C channel = Dm-weighted entries).  The ENTRYWISE
constants (C_int, Gi_00, min K) are typed for h-uniformity
SEPARATELY from the cell-envelope decay (the two-level
honesty: a pointwise bound may be derived while the cell
decay is cancellation-carried).  WARDS: W-I the CD
identity residual <= 1e-8 x scale; W-E max(|U_ij| - bndU_ij)
<= 1e-10; W-B max(N_meas - N_an) <= 1e-8; effective rank of
Qm typed; looseness ratio typed (median + max of
N_an/N_meas on nonzero blocks).  DERIVED requires
(frozen): wards pass on every sample rung AND h-uniformity
(K1_an and K2_an: max/min <= 2.0 AND |OLS slope log K vs
log h| <= 0.15) AND nontrivial decay (env_an_U(8) <= 0.5
env_an_U(0) on every rung).  TASK 2 (gap anatomy): (a) cell
variants n = 8/16/32 at VAR_RUNGS = (9, 26, 40, 142c): S_U,
S_C per n; (b) diagonal share: sqrt(N[r*,r*]) / row sum at
the arg-max row, U and C channels, every sample rung; (c)
frozen damped accountings on the C channel: C1 = max_r
sum_s sqrt(Nc), C2 = max_r [Nc[r,r] + sum_{s!=r} sqrt(Nc)],
C3 = max_r sum_s (Nc Ncs)^{1/4}, C4 = max_r [Nc[r,r] +
sum_{s!=r} (Nc Ncs)^{1/4}]; GAP-CLOSABLE iff some predeclared
accounting (a n-variant Cotlar sum or C1..C4) < 1.0 on every
tested rung.  TASK 3: eps_r profiles (16 cells) at complete
kz 142/177/243 vs battery band (v2 anchors 6.9-10.1); trend
typed.  CONTROLS: v2 regressions (S_U/S_C at all 15 sample
rungs vs the v2 log to 1e-3; K1/K2 at anchors 9/26/40 +
holdouts to 2e-3; Krein floors at deep rungs rel 0.2; eps_sum
anchors rel 1 percent); Epstein + scramble at kz 9: their
analytic constants must blow up (K1_an control >= 2.0 x
truth) or their gauss construction fails (typed).  VERDICT
(frozen): GAP-CLOSABLE-SHAPE (prominent) else
ENVELOPE-DERIVED (+ typed remaining gap) else
ENVELOPE-EMPIRICAL-ONLY (typed where the derivation misses).
NO RH claim; writes nothing."""

BATT10 = (9, 13, 15, 23, 26, 32, 40, 52, 64, 82)
HOLDOUTS = ppc.HOLDOUTS
DEEP = (142, 177, 243)
VAR_RUNGS = (9, 26, 40, 142)
NCELL_VARIANTS = (8, 16, 32)
H_UNIF_RATIO = 2.0
H_UNIF_SLOPE = 0.15
DECAY_BAR = 0.5
CTRL_RATIO = 2.0

# v2 regression references (cotlar_v2 run3 log, 2026-08-08)
S_REFS = {9: (5.8885, 4.1102), 13: (5.5684, 4.2295),
          15: (6.0377, 4.5977), 23: (6.2643, 4.5234),
          26: (5.6614, 4.1204), 32: (5.9206, 4.6336),
          40: (5.8282, 4.3158), 52: (5.8268, 4.3439),
          64: (6.1347, 4.4140), 82: (6.0512, 4.3799),
          90: (5.9456, 4.4887), 116: (5.8426, 4.3794),
          142: (5.6483, 4.1008), 177: (5.9725, 4.5098),
          243: (5.8651, 4.3105)}
K_REFS = {9: (7.2871, 40.0579), 26: (7.1579, 39.7952),
          40: (8.3603, 40.3521), 90: (6.7470, 40.3530),
          116: (6.5232, 40.4139), 142: (7.5663, 40.4137),
          177: (7.1361, 40.4591), 243: (8.1428, 40.4745)}
EPS_REFS = {9: 6.881, 13: 7.095, 26: 10.08, 40: 9.741}
KREIN_REFS = {142: 1.2389e-8, 177: 1.3284e-8, 243: 6.6742e-9}
BANNED_IDS = ("zetazero", "nzeros", "primerange", "isprime",
              "primepi", "nextprime", "prevprime")

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


# --------------------------------------------- generalized census
def cell_index_n(dth, n):
    d = np.mod(dth, 2.0 * math.pi)
    return np.minimum((d / (2.0 * math.pi / n)).astype(int),
                      n - 1)


def cross_norms_fast_n(pieces, n):
    P = [X @ X.conj().T for X in pieces]
    Ph = []
    for Pr in P:
        Ps = 0.5 * (Pr + Pr.conj().T)
        w, V = np.linalg.eigh(Ps)
        w = np.sqrt(np.clip(w, 0.0, None))
        Ph.append((V * w) @ V.conj().T)
    N = np.zeros((n, n))
    Ns = np.zeros((n, n))
    for r in range(n):
        for s in range(r, n):
            Mrs = Ph[r] @ P[s] @ Ph[r]
            Mrs = 0.5 * (Mrs + Mrs.conj().T)
            lmx = float(np.linalg.eigvalsh(Mrs)[-1])
            N[r, s] = N[s, r] = math.sqrt(max(lmx, 0.0))
            G = pieces[r] @ pieces[s].conj().T
            sv = np.linalg.svd(G, compute_uv=False)
            Ns[r, s] = Ns[s, r] = float(sv[0]) if len(sv) \
                else 0.0
    return N, Ns


def census(dc, ncells=16, light=False):
    """The v1/v2 readout math on a prebuilt dc, with the cell
    count as a parameter (n = 16 reproduces v2 verbatim)."""
    b, go = dc["b"], dc["go"]
    h = b["h"]
    # deployed cells: the PRUEFER phases (v1/v2 verbatim)
    dth = dc["thm"][:, None] - dc["thp"][None, :]
    cell = dc["cell"] if ncells == 16 \
        else cell_index_n(dth, ncells)
    U = go["U"]
    Dm2 = go["Dm"] ** 2
    Cc = go["Dm"][:, None] * U
    pu = [np.where(cell == r, U, 0.0) for r in range(ncells)]
    pc = [np.where(cell == r, Cc, 0.0) for r in range(ncells)]
    Nu, Nus = cross_norms_fast_n(pu, ncells)
    Nc, Ncs = cross_norms_fast_n(pc, ncells)
    Su = float(np.max(np.sum(np.sqrt(Nu), axis=1)))
    Sc = float(np.max(np.sum(np.sqrt(Nc), axis=1)))
    out = dict(kz=dc["kz"], h=h, ncells=ncells, Su=Su, Sc=Sc,
               Nu=Nu, Nus=Nus, Nc=Nc, Ncs=Ncs, cell=cell,
               dth=dth)
    if light:
        return out
    wr = np.array([float(np.sum(np.abs(p) ** 2)) for p in pu])
    wr = wr / max(float(np.sum(wr)), 1e-300)
    eps = []
    for r in range(ncells):
        Ar = pu[r]
        Mr = wr[r] * np.eye(h) - Ar.conj().T \
            @ (Dm2[:, None] * Ar)
        Mr = 0.5 * (Mr + Mr.conj().T)
        eps.append(max(0.0, -float(np.linalg.eigvalsh(Mr)[0])))
    cd = np.abs(np.arange(ncells)[:, None]
                - np.arange(ncells)[None, :])
    cd = np.minimum(cd, ncells - cd)
    env_u = np.array([float(np.max(Nu[cd == d]))
                      for d in range(ncells // 2 + 1)])
    env_c = np.array([float(np.max(Nc[cd == d]))
                      for d in range(ncells // 2 + 1)])
    dd = np.arange(len(env_u), dtype=float)
    out.update(eps=eps, eps_sum=float(np.sum(eps)),
               env_u=env_u, env_c=env_c,
               K1=float(np.max(env_u * (1.0 + dd))),
               K2=float(np.max(env_c * (1.0 + dd) ** 2)),
               lam1=float(np.linalg.eigvalsh(b["Delta"])[0]),
               cd=cd)
    return out


# --------------------------------------------- the analytic bound
def analytic_envelope(dc, cs):
    """Christoffel-Darboux entrywise bound + per-cell Schur
    blocks on the deployed cells.  Source data only (Gp,
    Gp^{-1} via Rm, geometric node angles, Christoffel
    normalizers Km/Kp, damping Dm)."""
    b, go = dc["b"], dc["go"]
    h = b["h"]
    Gi = b["Rm"] @ b["Rm"]
    Gp = b["Gp"]
    # multiplication by cos th on the frame: exact tridiag
    A = 0.5 * (np.eye(h, k=1) + np.eye(h, k=-1))
    A[h - 1, h - 1] = -0.5
    Qm = A @ Gi - Gi @ A
    Uq, sq, Wq = np.linalg.svd(Qm)
    keep = sq > 1e-12 * max(sq[0], 1e-300)
    rank_eff = int(np.sum(keep))
    C_int = 0.0
    for k in range(rank_eff):
        nu = math.sqrt(max(float(Uq[:, k] @ (Gp
                                             @ Uq[:, k])), 0.0))
        nw = math.sqrt(max(float(Wq[k] @ (Gp @ Wq[k])), 0.0))
        C_int += float(sq[k]) * nu * nw
    gi00 = math.sqrt(max(float(Gi[0, 0]), 0.0))
    thm, thp = go["thm"], go["thp"]
    Km, Kp = go["Km"], go["Kp"]
    xm, xp = np.cos(thm), np.cos(thp)
    dxy = np.abs(xm[:, None] - xp[None, :])
    num_c = (C_int
             + gi00 * (1.0 / np.sqrt(Km)[:, None]
                       + 1.0 / np.sqrt(Kp)[None, :]))
    bndU = np.minimum(1.0, num_c / np.maximum(dxy, 1e-300))
    bndC = go["Dm"][:, None] * bndU
    # CD identity ward (machine-grade; scale = ||num||_max)
    root = np.sqrt(np.outer(Km, Kp))
    num = go["U"] * root
    lhs = xm[:, None] * num - num * xp[None, :]
    FpH = gnu.eval_frame(thp, h).conj().T
    Fm = gnu.eval_frame(thm, h)
    rho_m = np.exp(1j * thm) - np.exp(-2j * h * thm)
    rho_p = np.exp(1j * thp) - np.exp(-2j * h * thp)
    rhs = Fm @ Qm @ FpH \
        + 0.5 * rho_m[:, None] * (Gi[0] @ FpH)[None, :] \
        - 0.5 * (Fm @ Gi[:, 0])[:, None] \
        * np.conj(rho_p)[None, :]
    idres = float(np.max(np.abs(lhs - rhs))) \
        / max(float(np.max(np.abs(num))), 1e-300)
    n = cs["ncells"]
    cell = cs["cell"]
    sig_u = np.zeros(n)
    sig_c = np.zeros(n)
    for r in range(n):
        m = (cell == r)
        bu = np.where(m, bndU, 0.0)
        bc = np.where(m, bndC, 0.0)
        # min of two valid norm bounds: Schur and Frobenius
        sig_u[r] = min(
            math.sqrt(max(float(np.max(np.sum(bu, axis=1)))
                          * float(np.max(np.sum(bu, axis=0))),
                          0.0)),
            float(np.linalg.norm(bu)))
        sig_c[r] = min(
            math.sqrt(max(float(np.max(np.sum(bc, axis=1)))
                          * float(np.max(np.sum(bc, axis=0))),
                          0.0)),
            float(np.linalg.norm(bc)))
    Nan_u = np.outer(sig_u, sig_u)
    Nan_c = np.outer(sig_c, sig_c)
    cd = cs["cd"]
    env_u = np.array([float(np.max(Nan_u[cd == d]))
                      for d in range(n // 2 + 1)])
    env_c = np.array([float(np.max(Nan_c[cd == d]))
                      for d in range(n // 2 + 1)])
    dd = np.arange(len(env_u), dtype=float)
    ew = float(np.max(np.abs(go["U"]) - bndU))
    bw_u = float(np.max(cs["Nu"] - Nan_u))
    bw_c = float(np.max(cs["Nc"] - Nan_c))
    nz = cs["Nu"] > 1e-12
    loose = Nan_u[nz] / cs["Nu"][nz]
    return dict(C_int=C_int, gi00=gi00, rank_eff=rank_eff,
                idres=idres,
                minKm=float(np.min(Km)),
                minKp=float(np.min(Kp)),
                env_u=env_u, env_c=env_c,
                K1an=float(np.max(env_u * (1.0 + dd))),
                K2an=float(np.max(env_c * (1.0 + dd) ** 2)),
                ew=ew, bw=max(bw_u, bw_c),
                loose_med=float(np.median(loose)),
                loose_max=float(np.max(loose)),
                decay=float(env_u[-1] / max(env_u[0],
                                            1e-300)))


def get_dc(kz, **kw):
    dc, err = ppc.deployed_cells(kz, **kw)
    if dc is None:
        return None, err
    dc["kz"] = kz
    return dc, None


# ================================================================= main
def main():
    section("PRIME.ENVELOPE.DERIVATION.01 -- the envelope "
            "derivation + the certificate gap (EXPLORATION "
            "ONLY)")
    sha = hashlib.sha256(FROZEN_SPEC.encode("utf-8")).hexdigest()
    print("    FROZEN_SPEC SHA-256 = %s" % sha)
    print("    NO RH claim.")
    print("\nS0 -- firewall + inherited contracts")
    check("S0.1 AST firewall clean", not ast_scan(BANNED_IDS))
    v1sha = hashlib.sha256(
        ppc.FROZEN_SPEC.encode("utf-8")).hexdigest()
    v2sha = hashlib.sha256(
        cv2.FROZEN_SPEC.encode("utf-8")).hexdigest()
    check("S0.2 [CONTRACT CHAIN] v1 spec %s..., v2 spec "
          "%s... verified" % (v1sha[:8], v2sha[:8]),
          v1sha.startswith("4621b899")
          and v2sha.startswith("5fd6bf61"))
    cv2.U_EXT, cv2.MU_EXT = cv2.build_ext_table()

    # ---------------- TASK 1 + regressions: the main loop
    section("TASK 1 -- the analytic envelope derivation "
            "(battery sample + complete holdouts)")
    rows = {}
    an = {}
    reg_ok, krein_ok = True, True
    for kz in list(BATT10) + list(HOLDOUTS):
        kw = dict(comb=cv2.comb_ext(kz)) if kz in DEEP else {}
        dc, err = get_dc(kz, **kw)
        if dc is None:
            print("    kz %d: %s" % (kz, err))
            continue
        cs = census(dc)
        aa = analytic_envelope(dc, cs)
        rows[kz] = cs
        an[kz] = aa
        rS = S_REFS[kz]
        reg_ok &= (abs(cs["Su"] - rS[0]) <= 1e-3
                   and abs(cs["Sc"] - rS[1]) <= 1e-3)
        if kz in K_REFS:
            rK = K_REFS[kz]
            reg_ok &= (abs(cs["K1"] - rK[0]) <= 2e-3
                       and abs(cs["K2"] - rK[1]) <= 2e-3)
        if kz in EPS_REFS:
            reg_ok &= abs(cs["eps_sum"] - EPS_REFS[kz]) \
                / EPS_REFS[kz] <= 0.01
        if kz in DEEP:
            krein_ok &= (cs["lam1"] > 0.0
                         and abs(cs["lam1"] - KREIN_REFS[kz])
                         / KREIN_REFS[kz] <= 0.2)
        print("    kz %-4d h %-4d%s: S_U %.4f S_C %.4f | "
              "K1/K2 meas %.2f/%.2f an %.3g/%.3g | C_int "
              "%.3g rk %d gi00 %.3g minK -/+ %.2e/%.2e | "
              "id ward %.1e entry %.1e block %.1e | decay "
              "%.3f loose med/max %.1f/%.1f"
              % (kz, cs["h"],
                 " C" if kz in DEEP else "",
                 cs["Su"], cs["Sc"], cs["K1"], cs["K2"],
                 aa["K1an"], aa["K2an"], aa["C_int"],
                 aa["rank_eff"], aa["gi00"],
                 aa["minKm"], aa["minKp"], aa["idres"],
                 aa["ew"], aa["bw"], aa["decay"],
                 aa["loose_med"], aa["loose_max"]),
              flush=True)
    check("T1.1 [V2 REGRESSION] all sample sums, K's, and "
          "anchor eps reproduce the v2 log", reg_ok)
    check("T1.2 [KREIN REGRESSION] complete-comb floors at "
          "kz 142/177/243 positive + reproduce", krein_ok)
    id_all = max(a["idres"] for a in an.values())
    ew_all = max(a["ew"] for a in an.values())
    bw_all = max(a["bw"] for a in an.values())
    rk_all = max(a["rank_eff"] for a in an.values())
    check("T1.3 [DERIVATION WARD] CD identity residual "
          "(max %.1e <= 1e-8), entrywise |U| <= bnd (max "
          "viol %.1e <= 1e-10), blockwise N_meas <= N_an "
          "(max viol %.1e <= 1e-8) on every rung; "
          "eff rank(Qm) <= %d"
          % (id_all, ew_all, bw_all, rk_all),
          id_all <= 1e-8 and ew_all <= 1e-10
          and bw_all <= 1e-8)
    hh = np.log([float(rows[kz]["h"]) for kz in rows])
    unif = {}
    entry_unif = {}
    for lbl, tgt in (("K1an", unif), ("K2an", unif),
                     ("C_int", entry_unif),
                     ("gi00", entry_unif)):
        vals = np.array([an[kz][lbl] for kz in rows])
        ratio = float(np.max(vals) / np.min(vals))
        slope = float(np.polyfit(hh, np.log(vals), 1)[0])
        tgt[lbl] = (ratio <= H_UNIF_RATIO
                    and abs(slope) <= H_UNIF_SLOPE)
        print("    %-5s: range [%.4g, %.4g], max/min %.2f "
              "(bar %.1f), log-log slope %+.3f (bar %.2f) "
              "-> h-uniform: %s"
              % (lbl, float(np.min(vals)),
                 float(np.max(vals)), ratio, H_UNIF_RATIO,
                 slope, H_UNIF_SLOPE, tgt[lbl]))
    entry_derived = (id_all <= 1e-8 and ew_all <= 1e-10
                     and all(entry_unif.values()))
    print("    ENTRYWISE level: CD identity exact, rank-2 "
          "commutator, constants %sh-uniform -> the "
          "pointwise bound is %sDERIVED"
          % ("" if all(entry_unif.values()) else "NOT ",
             "" if entry_derived else "NOT "))
    decay_ok = all(a["decay"] <= DECAY_BAR
                   for a in an.values())
    check("T1.4 [NONTRIVIAL DECAY] the analytic envelope "
          "certifies env(8) <= %.1f env(0) on every rung "
          "(worst %.3f)"
          % (DECAY_BAR, max(a["decay"] for a in an.values())),
          decay_ok)
    derived = (ew_all <= 1e-10 and bw_all <= 1e-8
               and all(unif.values()) and decay_ok)
    if derived:
        print("""
    CANDIDATE LEMMA (envelope, verbatim): multiplication by
    cos th is exactly tridiagonal on the odd frame with a
    single k = 0 defect; hence (CD telescoping + RKHS CS)
    every deployed rung obeys |U_ij| <= min(1, [C_int +
    sqrt((Gp^{-1})_00)(Km_i^{-1/2} + Kp_j^{-1/2})] /
    |cos thm_i - cos thp_j|) with C_int = sum sigma_k(Qm)
    ||u_k||_Gp ||w_k||_Gp over the rank-2 commutator
    Qm = [A, Gp^{-1}], and the deployed 16-cell envelope
    obeys env_U(d) <= K1_an/(1+d), env_C(d) <= K2_an/(1+d)^2
    with the h-uniform K_an ranges above.  REMAINING (typed):
    the source-law persistence of C_int, (Gp^{-1})_00, and
    the Christoffel floors min Km, min Kp as h -> infty.""")

    # ---------------- TASK 2 -- the certificate-gap anatomy
    section("TASK 2 -- the certificate-gap anatomy")
    print("  (a) cell-count variants (frozen n = 8/16/32):")
    var_ok_lt1 = []
    for kz in VAR_RUNGS:
        kw = dict(comb=cv2.comb_ext(kz)) if kz in DEEP else {}
        dc, err = get_dc(kz, **kw)
        line = "    kz %-4d:" % kz
        for n in NCELL_VARIANTS:
            if n == 16:
                cs = rows[kz]
            else:
                cs = census(dc, ncells=n, light=True)
            line += "  n=%-2d S_U %.3f S_C %.3f |" \
                % (n, cs["Su"], cs["Sc"])
            var_ok_lt1.append(cs["Sc"] < 1.0)
        print(line, flush=True)
    print("\n  (b) the diagonal share (arg-max row of the "
          "sqrt census):")
    for kz in list(BATT10) + list(HOLDOUTS):
        cs = rows[kz]
        outp = []
        for lbl, Nm in (("U", cs["Nu"]), ("C", cs["Nc"])):
            rs = np.sum(np.sqrt(Nm), axis=1)
            r0 = int(np.argmax(rs))
            share = math.sqrt(Nm[r0, r0]) / float(rs[r0])
            outp.append("%s: cell %2d share %.3f (diag "
                        "sqrt %.3f of %.3f)"
                        % (lbl, r0, share,
                           math.sqrt(Nm[r0, r0]),
                           float(rs[r0])))
        print("    kz %-4d: %s | %s"
              % (kz, outp[0], outp[1]))
    print("\n  (c) frozen damped accountings (C channel, "
          "vs the certificate bar 1):")
    acc_names = ("C1 sqrt-sum", "C2 diag-as-norm",
                 "C3 geo-mean", "C4 geo+diag-norm")
    acc_best = {}
    for kz in list(BATT10) + list(HOLDOUTS):
        cs = rows[kz]
        Nc, Ncs = cs["Nc"], cs["Ncs"]
        g4 = (Nc * Ncs) ** 0.25
        offm = ~np.eye(16, dtype=bool)
        c1 = float(np.max(np.sum(np.sqrt(Nc), axis=1)))
        c2 = float(np.max(np.diag(Nc)
                          + np.sum(np.where(offm,
                                            np.sqrt(Nc), 0.0),
                                   axis=1)))
        c3 = float(np.max(np.sum(g4, axis=1)))
        c4 = float(np.max(np.diag(Nc)
                          + np.sum(np.where(offm, g4, 0.0),
                                   axis=1)))
        acc_best[kz] = min(c1, c2, c3, c4)
        print("    kz %-4d: C1 %.3f  C2 %.3f  C3 %.3f  "
              "C4 %.3f   best %.3f" % (kz, c1, c2, c3, c4,
                                       acc_best[kz]))
    gap_closable = (all(v < 1.0 for v in acc_best.values())
                    or (len(var_ok_lt1) > 0
                        and all(var_ok_lt1)))
    print("    best predeclared accounting over all rungs: "
          "max %.3f -> GAP-CLOSABLE: %s"
          % (max(acc_best.values()), gap_closable))

    # ---------------- TASK 3 -- local dominance at depth
    section("TASK 3 -- the local-dominance revisit "
            "(complete combs at depth)")
    batt_eps = [rows[kz]["eps_sum"] for kz in BATT10]
    print("    battery band: sum eps_r in [%.2f, %.2f] "
          "(n = %d)" % (min(batt_eps), max(batt_eps),
                        len(batt_eps)))
    for kz in HOLDOUTS:
        cs = rows[kz]
        top = np.argsort(cs["eps"])[::-1][:3]
        print("    kz %-4d%s: sum eps_r %.3f | top cells %s "
              "(%.2f, %.2f, %.2f)"
              % (kz, " COMPLETE" if kz in DEEP else "",
                 cs["eps_sum"], list(top),
                 *[cs["eps"][t] for t in top]))
    he = np.log([float(rows[kz]["h"])
                 for kz in list(BATT10) + list(HOLDOUTS)])
    ee = np.log([rows[kz]["eps_sum"]
                 for kz in list(BATT10) + list(HOLDOUTS)])
    eps_slope = float(np.polyfit(he, ee, 1)[0])
    deep_eps = [rows[kz]["eps_sum"] for kz in DEEP]
    improves = max(deep_eps) < min(batt_eps)
    print("    eps_sum log-log slope vs h: %+.3f; deep "
          "holdouts %s the battery band -> local-dominance "
          "gap %s"
          % (eps_slope,
             "IMPROVE below" if improves else "stay in/above",
             "improves at depth" if improves
             else "is real and alpha-uniform"))

    # ---------------- controls
    section("CONTROLS -- Epstein / scramble (the analytic "
            "constants must not transfer)")
    rr9 = core.build_window(9)
    N_E = int(math.floor(math.exp(2.0 * rr9["alpha"]))) + 1
    lamE = gnu.lambda_eps(N_E)
    nn = np.nonzero(np.abs(lamE) > 1e-12)[0]
    truthK1 = an[9]["K1an"]
    ctrl_ok = True
    for nmc, kw in (("Epstein", dict(comb=(
            np.log(nn.astype(float)),
            2.0 * lamE[nn] / np.sqrt(nn.astype(float))))),
            ("scramble", dict(scramble_seed=1))):
        dc, err = get_dc(9, **kw)
        if dc is None:
            print("    %-8s: gauss construction fails (%s) "
                  "-> breaks (typed)" % (nmc, err))
            continue
        cs = census(dc, light=True)
        cs["cd"] = np.minimum(
            np.abs(np.arange(16)[:, None]
                   - np.arange(16)[None, :]),
            16 - np.abs(np.arange(16)[:, None]
                        - np.arange(16)[None, :]))
        aa = analytic_envelope(dc, cs)
        ratio = aa["K1an"] / truthK1
        okc = ratio >= CTRL_RATIO
        ctrl_ok &= okc
        print("    %-8s: K1_an %.4g vs truth %.4g (ratio "
              "%.1f, bar %.1f); C_int %.3g vs %.3g -> %s"
              % (nmc, aa["K1an"], truthK1, ratio, CTRL_RATIO,
                 aa["C_int"], an[9]["C_int"],
                 "breaks" if okc else "TRANSFERS"))
    check("C.1 [DISCRIMINATION] the analytic envelope "
          "constants do not transfer to Epstein/scramble",
          ctrl_ok)

    # ---------------- TASK 4 -- synthesis + verdict
    section("V -- FROZEN VERDICT + the honest ledger")
    if gap_closable:
        verdict = "GAP-CLOSABLE-SHAPE"
    elif derived:
        verdict = "ENVELOPE-DERIVED"
    else:
        misses = []
        if not (ew_all <= 1e-10 and bw_all <= 1e-8):
            misses.append("wards")
        if not all(unif.values()):
            misses.append("h-uniformity(%s)" % ",".join(
                k for k, v in unif.items() if not v))
        if not decay_ok:
            misses.append("decay")
        verdict = "ENVELOPE-EMPIRICAL-ONLY (missed: %s)" \
            % ", ".join(misses)
    print("\n  VERDICT: %s" % verdict)
    smax = max(rows[kz]["Sc"] for kz in rows)
    print("""
  THE LEDGER (honest):
    h-STABLE + BOUNDED: the measured envelopes (K1 ~ %.1f,
      K2 ~ %.1f) and the Cotlar sums (S_C <= %.2f) on
      complete-comb data, battery + all five holdouts.
    ANALYTIC: %s
    TOO BIG: every predeclared accounting stays >= %.2f
      (bar 1); the factor lives in the sqrt of O(1) block
      norms summed over ~%d effective neighbours plus the
      diagonal (shares above).
    LOCALLY FAILING: sum eps_r stays O(10) at complete-comb
      depth (slope %+.2f) -- phase-local dominance is absent
      on clean data too; the eps_r are NOT a truncation
      artifact.
  A CERTIFICATE WOULD NEED: an accounting in which the damped
  diagonal (C2-style, carrying the eps_r budget through the
  T2 channel) AND an off-diagonal constant below 1 - sum eps
  coexist; measured, the off-diagonal alone is >= %.2f and
  sum eps ~ %.0f >> 1, so NO cell-partition Cotlar accounting
  of this family can certify -- the gap is structural to the
  16-cell frame, not a constant to be tuned.  CONTRACT NOTE
  (PRIME.KREIN.CONTRACTOR.01, round 36): the COTLAR-GROWING
  kill is REVERSED on complete combs (v2 BOUNDED, envelopes
  h-stable%s); the route is REOPENED but not certifying: the
  remaining gap is the accounting constant (~%.1f vs 1) and
  the O(10) local defect budget; next typed objects: the
  source-law persistence of (C_-, C_+, ||Gp^{-1}||, min K)
  and a non-cell (coherent-state / wave-packet) partition
  where the diagonal carries mass ~1.  NO RH claim.""" % (
        max(rows[kz]["K1"] for kz in rows),
        max(rows[kz]["K2"] for kz in rows), smax,
        ("the entrywise + block envelope bounds are DERIVED "
         "with h-uniform source constants (lemma above)")
        if derived else
        ("the ENTRYWISE CD bound is DERIVED (identity "
         "exact, rank-2 commutator, h-uniform constants); "
         "the CELL-envelope decay is NOT entrywise-"
         "derivable -- it is cancellation-carried "
         "(empirical at the block level)")
        if entry_derived else
        ("the derivation bounds hold but the constants are "
         "not h-uniform -- typed above"),
        min(acc_best.values()), 16,
        eps_slope, min(acc_best.values()),
        float(np.mean([rows[kz]["eps_sum"] for kz in rows])),
        ", derivation " + ("closes" if derived else "open"),
        min(acc_best.values())))
    npass = sum(1 for _n, ok in CHECKS if ok)
    print("\n[TIME] %.1f min   [CHECKS] %d run, %d failed%s"
          % ((time.time() - T0) / 60.0, len(CHECKS),
             len(FAILS),
             ("  " + ",".join(FAILS)) if FAILS else ""))
    return 0 if npass == len(CHECKS) else 1


if __name__ == "__main__":
    raise SystemExit(main())
'''

_SRC_WAVEPACKET = r'''
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""wave_packet_partition_probe -- PRIME.WAVEPACKET.PARTITION.01
(EXPLORATION ONLY, experiments/; direct follow-up to
ENVELOPE-EMPIRICAL-ONLY, 2026-08-08 night).

THE TYPED NEXT OBJECT.  The envelope probe closed the cell
class: every Pruefer cell contains near-diagonal geometric
pairs, pointwise bounds saturate, no cell accounting reaches
below 3.57 (bar 1), and the measured envelope decay is
cancellation-carried.  THE DEMAND: a NON-CELL decomposition
where the diagonal carries the mass and the cancellation
stays INSIDE the blocks -- wave packets on the natural
position-frequency phase space of the odd frame (cos th acts
tridiagonally: generator bandwidth 1, commutator cost O(1)
h-uniform at C_int grade -- the balanced uncertainty scale
s^2 ~ pi/(2 dim) is the packet width both designs use).

THE FORMALIZATION (frozen): canonical TIGHT packet frames on
both node spaces, Psi~ = S^{-1/2} Psi with S the frame
operator; then C^G = Psi~_m B Psi~_p^H with B = Psi~_m^H C^G
Psi~_p and ||C^G|| = ||B||_2 EXACTLY (sanity ward).  The
accounting object is B: diagonal = nearest-packet pairing in
normalized phase-space coordinates; the effective constant is
the Schur bound sqrt(maxrow x maxcol) of |B| -- the honest
number vs the cell frame's 3.57 and vs the certificate bar 1.

DESIGNS (predeclared, source-only):
  (a) RANK-GABOR (measure-adapted; the naive angle lattice
      is structurally killed by node clustering -- the
      folded minus support is patchy, so a uniform angle
      lattice cannot span the clustered node space): the
      position coordinate is the node RANK u_j = (rank(th_j)
      + 1/2)/r (uniform by construction), packets
      psi_{(u0,q)}[j] = exp(-(u_j - u0)^2/(2 su^2))
      e^{2 pi i q u_j}, su = 1/sqrt(2 r), lattice u0 step su
      over (0,1), q step 1/(2 su) over [-r/2, r/2]
      (2x oversampled, N ~ 2 r).
  (b) CHAIN packets: Phi = the orthogonal eigenvector matrix
      of the arm's tridiagonal chain (the exact discrete OP
      transform, columns matched to the deployed nodes);
      psi_{(n0, phi)} = Phi^T-transform of a Gaussian window
      exp(-(n - n0)^2/(2 sig^2)) e^{i n phi}, sig = sqrt(m),
      n0 step sig, phi step pi/sig (N ~ 2 m).
FRAME WARDS: cond(S) <= 1e10 both sides (else the design is
KILLED for that rung, typed); node-eigenvalue match <= 1e-8
for (b); ||B||_2 == ||C^G||_2 to 1e-8 rel (tightness).

TASKS: (2a) the diagonal question under TWO frozen pairings:
D1 the geometric nearest packet in normalized coordinates,
and D2 the EMPIRICAL partner map Q*(P) = argmax_Q |B_PQ|
(share + injectivity + the median coordinate offset -- the
measured pairing law; a near-permutation B with coherent
offsets is the cancellation-respecting structure even if the
naive geometric pairing misses it); plus the row
concentration (mean share of each row's energy in its best
entry); (2b) the off-diagonal envelope in normalized
phase-space distance rho (bins, decay typed); (2c) the
effective Schur constant vs 3.57 and vs 1; (3) the
certificate assembly: E_schur vs the known ||C^G|| =
sqrt(1 - lam1) per rung along ladder + complete-comb deep
holdouts; (4) Epstein/scramble in the same frame.
VERDICT (frozen): PACKETS-CARRY (on every rung the best
design has E_schur <= 1.2 AND [D1 share >= 0.5 OR (D2 share
>= 0.5 AND injectivity >= 0.8)] -- prominent) / PARTITION-
CLASS-CLOSED (every functioning design has E_schur >= 3.5
on every rung -- the atomically-global typing) /
PACKETS-PARTIAL (typed which piece).  NO RH claim; writes
nothing; no .md; no commits.

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/wave_packet_partition_probe.py
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

import v563_paper2_readouts as core            # noqa: E402  (READ-ONLY)
import gauss_node_unitary_probe as gnu         # noqa: E402  (READ-ONLY)
import pruefer_compensation_probe as ppc       # noqa: E402  (READ-ONLY)
import cotlar_v2_complete_comb_probe as cv2    # noqa: E402  (READ-ONLY)
import envelope_derivation_gap_probe as edg    # noqa: E402  (READ-ONLY)

FROZEN_SPEC = """\
PRIME.WAVEPACKET.PARTITION.01 spec v1 (2026-08-08, frozen
before run).  SAMPLE (frozen): kz (9, 13, 26, 40, 64, 90,
142, 243); 142/243 with the v2 COMPLETE comb.  OBJECT: C^G =
Dm-weighted U from gauss_objects (node coordinates); ward
|sigma_max(C^G)^2 - (1 - lam1(Delta))| <= 1e-8 rel.  DESIGNS
(a) RANK-GABOR: position = node rank u_j (uniform), su =
1/sqrt(2 r), lattice (u0: step su in (0,1); q: step
1/(2 su) in [-r/2, r/2]) and (b) chain packets sig =
sqrt(m), lattice (n0: step sig in (0, m); phi: step pi/sig
in (-pi, pi)) -- docstring formulas verbatim; packets of raw
norm < 1e-8 dropped (typed count); canonical tight frames
via S^{-1/2}.  FRAME KILL: lam_min(S) <= 0 or cond(S) > 1e10
on either side.  Normalized packet coords: (u0, q/r) resp
(n0/m, phi/(2 pi)).  READOUTS per rung x design: N_m, N_p,
cond_m, cond_p; ||B||_2 vs ||C^G|| (tightness ward 1e-8
rel); E_schur = sqrt(max row l1 x max col l1 of |B|); E_row
= max row l1; D1 diag: Q*(P) = nearest plus packet in
normalized coords -- max_P |B|, Frobenius share; D2 diag:
Q*(P) = argmax_Q |B_PQ| -- Frobenius share, injectivity
fraction, median |offset| in both coords (the measured
pairing law); row concentration = mean_P max_Q |B_PQ|^2 /
sum_Q |B_PQ|^2; envelope: max |B| in normalized-rho bins
(0, .02, .05, .1, .2, .4, .7, 1, 1.5+); decay = env(last
nonempty)/env(0).  DECISION (frozen): PACKETS-CARRY iff the
best design on every rung has E_schur <= 1.2 AND [D1 share
>= 0.5 OR (D2 share >= 0.5 AND injectivity >= 0.8)];
PARTITION-CLASS-CLOSED iff every non-killed design on every
rung has E_schur >= 3.5; else PACKETS-PARTIAL (typed).
DISCRIMINATION (kz 9, design a): Epstein and scramble must
move (E_schur rel >= 0.25 or diag share abs >= 0.25) --
else typed failure.  CONTROLS: envelope-probe regressions at
kz 9 (CD identity residual <= 1e-8, C_int within 1e-3 rel of
1.412); frame wards; certified budgets (runtime + peak N).
NO RH claim; writes nothing."""

SAMPLE = (9, 13, 26, 40, 64, 90, 142, 243)
DEEP = (142, 243)
RHO_BINS = (0.0, 0.02, 0.05, 0.10, 0.20, 0.40, 0.70,
            1.00, 1.50)
COND_KILL = 1e10
DIAG_BAR = 0.5
SCHUR_CARRY = 1.2
SCHUR_CLOSED = 3.5
CTRL_MOVE = 0.25
C_INT_REF = 1.412
BANNED_IDS = ("zetazero", "nzeros", "primerange", "isprime",
              "primepi", "nextprime", "prevprime")

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


# ------------------------------------------------ packet frames
def tighten(Psi):
    """Canonical tight frame; returns (Psi_tight, cond) or
    (None, cond) on frame kill."""
    S = Psi @ Psi.conj().T
    S = 0.5 * (S + S.conj().T)
    w, V = np.linalg.eigh(S)
    if w[0] <= 0.0 or w[-1] / w[0] > COND_KILL:
        return None, float(w[-1] / max(w[0], 1e-300))
    Si = (V * (w ** -0.5)) @ V.conj().T
    return Si @ Psi, float(w[-1] / w[0])


def gabor_frame(th, r):
    """Design (a): rank-Gabor packets (position = node
    rank, uniform by construction)."""
    u = (np.argsort(np.argsort(th)).astype(float) + 0.5) / r
    su = 1.0 / math.sqrt(2.0 * r)
    u0s = np.arange(su / 2.0, 1.0, su)
    dq = 1.0 / (2.0 * su)
    qs = np.arange(-r / 2.0, r / 2.0 + 1e-9, dq)
    packets, meta = [], []
    for u0 in u0s:
        g = np.exp(-(u - u0) ** 2 / (2.0 * su * su))
        ng = float(np.linalg.norm(g))
        if ng < 1e-8:
            continue
        for q in qs:
            v = g * np.exp(2j * math.pi * q * u)
            packets.append(v / ng)
            meta.append((u0, q / r))
    Psi = np.array(packets).T
    return Psi, np.array(meta)


def chain_matrix(al, be, th):
    """Eigenvector matrix of the tridiagonal chain, columns
    matched to the deployed node ordering.  Returns (Phi,
    match_err); Phi[j, n] = orthonormal OP transform."""
    m = len(al)
    J = np.diag(al)
    if m > 1:
        J += np.diag(be[:m - 1], 1) + np.diag(be[:m - 1], -1)
    evs, V = np.linalg.eigh(J)
    x = np.cos(th)
    order = np.argsort(np.argsort(x))
    err = float(np.max(np.abs(evs[order] - x)))
    return V[:, order].T, err


def chain_frame(al, be, th):
    """Design (b): Gaussian windows in the chain index,
    transported by the exact OP transform."""
    Phi, err = chain_matrix(al, be, th)
    m = Phi.shape[1]
    sig = math.sqrt(float(m))
    n0s = np.arange(sig / 2.0, m, sig)
    dph = math.pi / sig
    phs = np.arange(-math.pi, math.pi - 1e-9, dph)
    nn = np.arange(m, dtype=float)
    packets, meta = [], []
    for n0 in n0s:
        g = np.exp(-(nn - n0) ** 2 / (2.0 * sig * sig))
        ng = float(np.linalg.norm(g))
        if ng < 1e-8:
            continue
        for ph in phs:
            c = g * np.exp(1j * nn * ph)
            packets.append(Phi @ (c / ng))
            meta.append((n0 / m, ph / (2.0 * math.pi)))
    Psi = np.array(packets).T
    return Psi, np.array(meta), err


def block_readout(CG, Pm, mm, Pp, mp):
    """B = Pm^H C Pp + the frozen readouts."""
    B = Pm.conj().T @ CG @ Pp
    aB = np.abs(B)
    nB = float(np.linalg.svd(B, compute_uv=False)[0])
    rowl1 = np.sum(aB, axis=1)
    coll1 = np.sum(aB, axis=0)
    E_schur = math.sqrt(float(np.max(rowl1))
                        * float(np.max(coll1)))
    E_row = float(np.max(rowl1))
    fro2 = max(float(np.sum(aB ** 2)), 1e-300)
    # D1: nearest-packet diagonal (normalized coords)
    d2 = ((mm[:, 0][:, None] - mp[:, 0][None, :]) ** 2
          + (mm[:, 1][:, None] - mp[:, 1][None, :]) ** 2)
    qstar = np.argmin(d2, axis=1)
    diag = aB[np.arange(aB.shape[0]), qstar]
    dshare = float(np.sum(diag ** 2)) / fro2
    offrow = rowl1 - diag
    worst = int(np.argmax(rowl1))
    ratio_worst = float(offrow[worst]) \
        / max(float(diag[worst]), 1e-300)
    # D2: the empirical partner map (the measured pairing)
    qbest = np.argmax(aB, axis=1)
    dbest = aB[np.arange(aB.shape[0]), qbest]
    dshare2 = float(np.sum(dbest ** 2)) / fro2
    inj = float(len(np.unique(qbest))) / len(qbest)
    off_pos = float(np.median(np.abs(
        mm[:, 0] - mp[qbest, 0])))
    off_frq = float(np.median(np.abs(
        mm[:, 1] - mp[qbest, 1])))
    row2 = np.sum(aB ** 2, axis=1)
    conc = float(np.mean(dbest ** 2
                         / np.maximum(row2, 1e-300)))
    # envelope in normalized phase-space distance
    rho = np.sqrt(d2)
    env = []
    for k in range(len(RHO_BINS) - 1):
        m_ = (rho >= RHO_BINS[k]) & (rho < RHO_BINS[k + 1])
        env.append(float(np.max(aB[m_])) if np.any(m_)
                   else float("nan"))
    m_ = rho >= RHO_BINS[-1]
    env.append(float(np.max(aB[m_])) if np.any(m_)
               else float("nan"))
    fin = [e for e in env if math.isfinite(e)]
    decay = (fin[-1] / fin[0]) if len(fin) >= 2 else 1.0
    return dict(nB=nB, E_schur=E_schur, E_row=E_row,
                dmax=float(np.max(diag)), dshare=dshare,
                ratio_worst=ratio_worst, dshare2=dshare2,
                inj=inj, off=(off_pos, off_frq), conc=conc,
                env=env, decay=decay,
                Nm=Pm.shape[1], Np=Pp.shape[1])


def rung_packets(kz, **kw):
    """Both designs on one rung; returns per-design readouts
    or typed kills."""
    dc, err = ppc.deployed_cells(kz, **kw)
    if dc is None:
        return None, err
    b, go = dc["b"], dc["go"]
    CG = go["Dm"][:, None] * go["U"]
    nC = float(np.linalg.svd(CG, compute_uv=False)[0])
    lam1 = float(np.linalg.eigvalsh(b["Delta"])[0])
    id_ok = abs(nC ** 2 - (1.0 - lam1)) \
        <= 1e-8 * max(1.0, nC ** 2)
    out = dict(kz=kz, h=b["h"], nC=nC, lam1=lam1,
               id_ok=id_ok, designs={})
    thm, thp = go["thm"], go["thp"]
    ch = dc["chains"]
    # design (a)
    Pm_raw, mm = gabor_frame(thm, len(thm))
    Pp_raw, mp = gabor_frame(thp, len(thp))
    Pm, cm = tighten(Pm_raw)
    Pp, cp = tighten(Pp_raw)
    if Pm is None or Pp is None:
        out["designs"]["gabor"] = dict(
            kill="frame (cond %.1e/%.1e)" % (cm, cp))
    else:
        rd = block_readout(CG, Pm, mm, Pp, mp)
        rd.update(cond=(cm, cp))
        out["designs"]["gabor"] = rd
    # design (b)
    Pm_raw, mm, em = chain_frame(ch["alm"], ch["bem"], thm)
    Pp_raw, mp, ep = chain_frame(ch["alp"], ch["bep"], thp)
    if max(em, ep) > 1e-8:
        out["designs"]["chain"] = dict(
            kill="node match (%.1e/%.1e)" % (em, ep))
    else:
        Pm, cm = tighten(Pm_raw)
        Pp, cp = tighten(Pp_raw)
        if Pm is None or Pp is None:
            out["designs"]["chain"] = dict(
                kill="frame (cond %.1e/%.1e)" % (cm, cp))
        else:
            rd = block_readout(CG, Pm, mm, Pp, mp)
            rd.update(cond=(cm, cp))
            out["designs"]["chain"] = rd
    return out, None


def show(kz, h, name, rd):
    if "kill" in rd:
        print("    kz %-4d h %-4d [%s]: KILLED -- %s"
              % (kz, h, name, rd["kill"]), flush=True)
        return
    es = " ".join(("%.3f" % e) if math.isfinite(e) else "--"
                  for e in rd["env"])
    print("    kz %-4d h %-4d [%-5s N %4d/%4d cond "
          "%.1e/%.1e]: ||B|| %.6f | E_schur %.3f E_row %.3f"
          % (kz, h, name, rd["Nm"], rd["Np"], rd["cond"][0],
             rd["cond"][1], rd["nB"], rd["E_schur"],
             rd["E_row"]), flush=True)
    print("      D1 diag: max %.3f share %.3f (worst "
          "off/diag %.2f) | D2 partner: share %.3f inj "
          "%.2f offset (%.3f, %.3f) | row conc %.3f"
          % (rd["dmax"], rd["dshare"], rd["ratio_worst"],
             rd["dshare2"], rd["inj"], rd["off"][0],
             rd["off"][1], rd["conc"]), flush=True)
    print("      env %s | decay %.4f" % (es, rd["decay"]),
          flush=True)


# ================================================================= main
def main():
    section("PRIME.WAVEPACKET.PARTITION.01 -- the coherent-"
            "state partition of the contractor (EXPLORATION "
            "ONLY)")
    sha = hashlib.sha256(FROZEN_SPEC.encode("utf-8")).hexdigest()
    print("    FROZEN_SPEC SHA-256 = %s" % sha)
    print("    NO RH claim.")
    print("\nS0 -- firewall + inherited contracts + "
          "regressions")
    check("S0.1 AST firewall clean", not ast_scan(BANNED_IDS))
    shas = [hashlib.sha256(m.FROZEN_SPEC.encode()).hexdigest()
            for m in (ppc, cv2, edg)]
    check("S0.2 [CONTRACT CHAIN] v1 %s... v2 %s... envelope "
          "%s..." % tuple(s[:8] for s in shas),
          shas[0].startswith("4621b899")
          and shas[1].startswith("5fd6bf61")
          and shas[2].startswith("27d9f0a3"))
    cv2.U_EXT, cv2.MU_EXT = cv2.build_ext_table()
    dc9, _ = edg.get_dc(9)
    cs9 = edg.census(dc9)
    aa9 = edg.analytic_envelope(dc9, cs9)
    check("S0.3 [ENVELOPE REGRESSION] CD identity residual "
          "%.1e <= 1e-8 and C_int %.4f within 1e-3 rel of "
          "%.3f" % (aa9["idres"], aa9["C_int"], C_INT_REF),
          aa9["idres"] <= 1e-8
          and abs(aa9["C_int"] - C_INT_REF) / C_INT_REF
          <= 1e-3)

    # ---------------- the main table
    section("TASK 1+2 -- packet frames + the block structure "
            "of C^G  (env bins: rho = %s)"
            % (RHO_BINS,))
    res = {}
    id_all, tight_all = True, True
    for kz in SAMPLE:
        kw = dict(comb=cv2.comb_ext(kz)) if kz in DEEP \
            else {}
        out, err = rung_packets(kz, **kw)
        if out is None:
            print("    kz %d: %s" % (kz, err))
            continue
        res[kz] = out
        id_all &= out["id_ok"]
        print("    kz %-4d: ||C^G|| = %.8f  (1 - lam1 = "
              "%.8f)%s" % (kz, out["nC"],
                           math.sqrt(max(0.0,
                                         1.0 - out["lam1"])),
                           "  [COMPLETE comb]"
                           if kz in DEEP else ""))
        for name, rd in out["designs"].items():
            show(kz, out["h"], name, rd)
            if "kill" not in rd:
                tight_all &= abs(rd["nB"] - out["nC"]) \
                    <= 1e-8 * max(1.0, out["nC"])
    check("P.1 [GAUGE IDENTITY] sigma_max(C^G)^2 == 1 - "
          "lam1(Delta) on every rung", id_all)
    check("P.2 [TIGHTNESS] ||B||_2 == ||C^G||_2 (1e-8 rel) "
          "for every non-killed design", tight_all)

    # ---------------- task 3: the certificate assembly
    section("TASK 3 -- the certificate assembly (E_schur vs "
            "the known norm, per rung)")
    best = {}
    for kz in res:
        live = {n: r for n, r in res[kz]["designs"].items()
                if "kill" not in r}
        if not live:
            continue
        bn = min(live, key=lambda n: live[n]["E_schur"])
        best[kz] = (bn, live[bn])
        print("    kz %-4d h %-4d: best design %-5s  "
              "E_schur %.3f  vs ||C^G|| %.6f  (gap ratio "
              "%.2f; cell-class best was 3.57)"
              % (kz, res[kz]["h"], bn,
                 live[bn]["E_schur"], res[kz]["nC"],
                 live[bn]["E_schur"] / res[kz]["nC"]))
    hh = np.log([float(res[kz]["h"]) for kz in best])
    ee = np.log([best[kz][1]["E_schur"] for kz in best])
    slope = float(np.polyfit(hh, ee, 1)[0])
    print("    E_schur log-log slope vs h: %+.3f "
          "(decaying toward 1 would need < 0)" % slope)

    # ---------------- task 4: discrimination
    section("TASK 4 -- Epstein / scramble in the same "
            "packet frame (kz 9, design a)")
    t9 = res[9]["designs"]["gabor"]
    rr9 = core.build_window(9)
    N_E = int(math.floor(math.exp(2.0 * rr9["alpha"]))) + 1
    lamE = gnu.lambda_eps(N_E)
    nn = np.nonzero(np.abs(lamE) > 1e-12)[0]
    ctrl_ok = True
    for nmc, kw in (("Epstein", dict(comb=(
            np.log(nn.astype(float)),
            2.0 * lamE[nn] / np.sqrt(nn.astype(float))))),
            ("scramble", dict(scramble_seed=1))):
        out, err = rung_packets(9, **kw)
        if out is None:
            print("    %-8s: %s (typed break)" % (nmc, err))
            continue
        rd = out["designs"]["gabor"]
        if "kill" in rd:
            print("    %-8s: %s (typed break)"
                  % (nmc, rd["kill"]))
            continue
        dE = abs(rd["E_schur"] - t9["E_schur"]) \
            / t9["E_schur"]
        dD = abs(rd["dshare"] - t9["dshare"])
        moved = dE >= CTRL_MOVE or dD >= CTRL_MOVE
        ctrl_ok &= moved
        print("    %-8s: E_schur %.3f (truth %.3f, rel "
              "%.2f) diag share %.3f (truth %.3f, abs "
              "%.2f) -> %s"
              % (nmc, rd["E_schur"], t9["E_schur"], dE,
                 rd["dshare"], t9["dshare"], dD,
                 "moves" if moved else "BLIND"))
    check("D.1 [DISCRIMINATION] the packet structure moves "
          "under Epstein/scramble", ctrl_ok)

    # ---------------- verdict
    section("V -- FROZEN VERDICT + honest consequence")
    def diag_ok(rd):
        return (rd["dshare"] >= DIAG_BAR
                or (rd["dshare2"] >= DIAG_BAR
                    and rd["inj"] >= 0.8))

    carry = all(diag_ok(r[1])
                and r[1]["E_schur"] <= SCHUR_CARRY
                for r in best.values()) and len(best) > 0
    closed = all(
        all(rd["E_schur"] >= SCHUR_CLOSED
            for rd in res[kz]["designs"].values()
            if "kill" not in rd)
        for kz in res) and len(res) > 0
    if carry:
        verdict = "PACKETS-CARRY"
    elif closed:
        verdict = "PARTITION-CLASS-CLOSED"
    else:
        dmin = min(r[1]["dshare"] for r in best.values())
        d2mn = min(r[1]["dshare2"] for r in best.values())
        imin = min(r[1]["inj"] for r in best.values())
        cmin = min(r[1]["conc"] for r in best.values())
        emin = min(r[1]["E_schur"] for r in best.values())
        emax = max(r[1]["E_schur"] for r in best.values())
        pieces = []
        pieces.append("diagonal %s (D1 min %.3f, D2 min "
                      "%.3f inj %.2f, conc %.3f; bar %.1f)"
                      % ("carries" if (dmin >= DIAG_BAR
                                       or (d2mn >= DIAG_BAR
                                           and imin >= 0.8))
                         else "does NOT carry", dmin, d2mn,
                         imin, cmin, DIAG_BAR))
        pieces.append("E_schur in [%.2f, %.2f] (carry bar "
                      "%.1f, closed bar %.1f)"
                      % (emin, emax, SCHUR_CARRY,
                         SCHUR_CLOSED))
        verdict = "PACKETS-PARTIAL (%s)" % "; ".join(pieces)
    print("\n  VERDICT: %s" % verdict)
    print("""
  HONEST CONSEQUENCE: the packet frame is the first
  decomposition tested against the cancellation finding of
  the envelope probe.  The numbers above are the honest
  comparison: cell class >= 3.57 everywhere (closed); the
  packet class delivers the E_schur column, the diagonal
  shares, and the phase-space envelope per rung -- whatever
  the enum says, the certificate shape requires E_schur ~ 1
  with an h-decaying excess, and the assembly table plus the
  slope above is the measured status of that demand.  NO RH
  claim.""")
    npass = sum(1 for _n, ok in CHECKS if ok)
    print("\n[TIME] %.1f min   [CHECKS] %d run, %d failed%s"
          % ((time.time() - T0) / 60.0, len(CHECKS),
             len(FAILS),
             ("  " + ",".join(FAILS)) if FAILS else ""))
    return 0 if npass == len(CHECKS) else 1


if __name__ == "__main__":
    raise SystemExit(main())
'''

# --------------------------------------------------------------- harness
_PF_RE = re.compile(r"^\s*\[(PASS|FAIL)\]\s+(\S+)", re.M)
_VD_RE = re.compile(r"VERDICT[:\]]")
_SHA_RE = re.compile(r"FROZEN_SPEC SHA-256[ :=]+([0-9a-f]{64})")


def _probe_file(name):
    cand = os.path.abspath(os.path.join(
        _HERE, os.pardir, "experiments", "tfpt-discovery", name + ".py"))
    return cand if os.path.isfile(cand) else None


def _census(out):
    marks = _PF_RE.findall(out)
    fails = sorted({tok for st, tok in marks if st == "FAIL"})
    verdict = ""
    for line in out.splitlines():
        if _VD_RE.search(line):
            verdict = line.strip()
    return len(marks), fails, verdict


def _exec_probe(name, src):
    """Execute one embedded frozen probe source BYTE-EXACT in its own
    module namespace, registered under the probe's canonical import name
    (so the wave-packet probe's READ-ONLY import of the envelope probe
    resolves to the executed embedded copy); call its main(); capture and
    re-emit stdout."""
    if src[:1] == "\n":
        src = src[1:]
    path = _probe_file(name)
    same = None
    if path is not None:
        with open(path, encoding="utf-8") as fh:
            same = (fh.read() == src)
    fname = path or os.path.abspath(__file__)
    mod = types.ModuleType(name)
    mod.__file__ = fname
    sys.modules[name] = mod
    buf = io.StringIO()
    code = 0
    with contextlib.redirect_stdout(buf):
        try:
            exec(compile(src, fname, "exec"), mod.__dict__)
            entry = mod.__dict__.get("main")
            if callable(entry):
                rc = entry()
                code = 0 if rc is None else int(rc)
        except SystemExit as exc:
            code = 0 if exc.code is None else int(exc.code)
        except Exception:
            import traceback
            traceback.print_exc(file=sys.stdout)
            code = 99
    out = buf.getvalue()
    sys.stdout.write(out)
    sys.stdout.flush()
    return out, code, same


def _gate(name, out, code, same, exp_n, exp_fails, exp_verdict, exp_code,
          exp_sha, gates, extra=()):
    n, fails, verdict = _census(out)
    m = _SHA_RE.search(out)
    sha_ok = m is not None and m.group(1) == exp_sha
    ok = (n == exp_n and fails == list(exp_fails)
          and exp_verdict in verdict and code == exp_code
          and same is not False and sha_ok)
    for tag, pat in extra:
        hit = re.search(pat, out) is not None
        ok &= hit
        print("  [%s] EXTRA %s: /%s/" % ("PASS" if hit else "FAIL",
                                         tag, pat), flush=True)
    gates.append(ok)
    prov = ("byte-exact vs experiments source" if same is True else
            "embedded copy (source file not present)" if same is None
            else "SOURCE MISMATCH")
    print("\n[%s] PATTERN GATE %s: %d checks (exp %d) | FAILs %s (exp %s) "
          "| exit %d (exp %d) | spec SHA %s | %s\n      verdict line: %s"
          % ("PASS" if ok else "FAIL", name, n, exp_n,
             ",".join(fails) if fails else "none",
             ",".join(exp_fails) if exp_fails else "none",
             code, exp_code, "ok" if sha_ok else "MISMATCH", prov,
             verdict[:140]), flush=True)
    return ok


_PLAN = (
    ("envelope_derivation_gap_probe", _SRC_ENVELOPE, 7, ("C.1", "T1.4"),
     "ENVELOPE-EMPIRICAL-ONLY", 1, EXPECT_SHA_ENVELOPE, (
         ("CONTRACT-CHAIN",
          r"\[PASS\] S0\.2 \[CONTRACT CHAIN\] v1 spec 4621b899\.\.\., "
          r"v2 spec 5fd6bf61\.\.\. verified"),
         ("CD-WARD-EXACT",
          r"CD identity residual \(max 1\.3e-13 <= 1e-8\), entrywise "
          r"\|U\| <= bnd \(max viol -4\.5e-08 <= 1e-10\)"),
         ("ENTRYWISE-DERIVED",
          r"ENTRYWISE level: CD identity exact, rank-2 commutator, "
          r"constants h-uniform -> the pointwise bound is DERIVED"),
         ("CINT-H-UNIFORM",
          r"C_int: range \[1\.232, 2\.328\], max/min 1\.89 \(bar 2\.0\), "
          r"log-log slope \+0\.106 \(bar 0\.15\) -> h-uniform: True"),
         ("GAP-FLOOR",
          r"best predeclared accounting over all rungs: max 4\.178 "
          r"-> GAP-CLOSABLE: False"),
         ("EPS-ALPHA-UNIFORM",
          r"eps_sum log-log slope vs h: \+0\.237; deep holdouts stay "
          r"in/above the battery band -> local-dominance gap is real "
          r"and alpha-uniform"),
         ("NO-CELL-ACCOUNTING",
          r"so NO cell-partition Cotlar accounting"),
         ("CINT-DISCRIMINATES",
          r"Epstein : K1_an 1\.351e\+04 vs truth 7445 \(ratio 1\.8, "
          r"bar 2\.0\); C_int 3\.59 vs 1\.41"),
         ("CINT-DISCRIMINATES-SCRAMBLE",
          r"scramble: K1_an 7883 vs truth 7445 \(ratio 1\.1, "
          r"bar 2\.0\); C_int 12\.8 vs 1\.41"),
     )),
    ("wave_packet_partition_probe", _SRC_WAVEPACKET, 6, (),
     "PARTITION-CLASS-CLOSED", 0, EXPECT_SHA_WAVEPACKET, (
         ("CHAIN-INCL-ENVELOPE",
          r"\[PASS\] S0\.2 \[CONTRACT CHAIN\] v1 4621b899\.\.\. "
          r"v2 5fd6bf61\.\.\. envelope 27d9f0a3\.\.\."),
         ("TIGHTNESS",
          r"\[PASS\] P\.2 \[TIGHTNESS\] \|\|B\|\|_2 == \|\|C\^G\|\|_2 "
          r"\(1e-8 rel\) for every non-killed design"),
         ("GABOR-DECAYS",
          r"env 0\.529 0\.387 0\.354 0\.239 0\.166 0\.108 0\.362 "
          r"0\.007 -- \| decay 0\.0127"),
         ("DIAG-DOES-NOT-CARRY",
          r"D1 diag: max 0\.529 share 0\.024 \(worst off/diag "
          r"50\.25\) \| D2 partner: share 0\.122 inj 0\.77 offset "
          r"\(0\.072, 0\.069\) \| row conc 0\.099"),
         ("SCHUR-GROWS",
          r"E_schur log-log slope vs h: \+0\.295 \(decaying toward 1 "
          r"would need < 0\)"),
         ("ASSEMBLY-DEEP",
          r"kz 243  h 1292: best design gabor  E_schur 9\.074  vs "
          r"\|\|C\^G\|\| 1\.000000  \(gap ratio 9\.07; cell-class "
          r"best was 3\.57\)"),
         ("DISCRIMINATION",
          r"scramble: E_schur 9006\.611 \(truth 4\.985, rel "
          r"1805\.77\)"),
     )),
)


def run():
    t0 = time.time()
    print("=" * 74)
    print("v879 -- PRIME.ENVELOPE.DERIVATION.01 + "
          "PRIME.WAVEPACKET.PARTITION.01")
    print("(THE PARTITION CLOSURE, round 37: the analytic core saved -- "
          "the exact")
    print("tridiagonal CD identity with h-uniform derived entrywise "
          "constants -- and")
    print("the decomposition chapter closed ENTIRELY: cells, packets, "
          "all frames;")
    print("the cancellation is atomically global, the certificate demand "
          "retyped")
    print("non-decompositional; two frozen-honest FAILs kept; NO RH claim)")
    print("=" * 74, flush=True)
    gates = []
    for (name, src, exp_n, exp_fails, exp_verdict, exp_code, exp_sha,
         extra) in _PLAN:
        print("\n" + "-" * 74)
        print("EMBEDDED FROZEN PROBE: %s" % name)
        print("-" * 74, flush=True)
        out, code, same = _exec_probe(name, src)
        _gate(name, out, code, same, exp_n, exp_fails, exp_verdict,
              exp_code, exp_sha, gates, extra)
    ok = all(gates)
    print("\n" + "=" * 74)
    print("v879: %d/%d probe pattern gates passed | runtime %.1f min"
          % (sum(gates), len(gates), (time.time() - t0) / 60.0))
    print("The partition chapter is closed on its own measurements: the "
          "pointwise")
    print("bound is DERIVED with h-uniform source constants, but the "
          "cancellation that")
    print("holds the wall is atomically global -- no cell, packet or "
          "frame accounting")
    print("of this family can certify; the surviving assets are the "
          "tridiagonal")
    print("identity, the derived constants, and their source-law "
          "persistence as the")
    print("named open object.  NO RH claim.")
    print("[%s] v879 VERDICT GATE: ENVELOPE-EMPIRICAL-ONLY + "
          "PARTITION-CLASS-CLOSED" % ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(run())
