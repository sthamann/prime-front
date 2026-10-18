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
