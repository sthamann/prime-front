#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""edge_redheffer_probe -- PRIME.RDAGGER.EDGE_REDHEFFER_COMPLETION.01
(round 433): the border augmentation as an explicit
three-channel Redheffer / Schur step, and the last
Potapov pivot identity.

THE OBJECT.  r362/r369 write R -> R^dagger by a rank-1
Sherman-Morrison border of the dual kernel, equivalently
the mixed form M^dagger = A + U J U^T with
    A = blkdiag(A0, -1/2),
    U = [two last dual CD columns, SM border],
    J = diag(1, 1, 1/den).
This round IDENTIFIES that construction as the terminating
2x2-block Redheffer star of the bulk colligation
    Theta = [[A, U], [U^T, 0_3]]
with the 3x3 edge factor E = J (CD port I_2 plus border
channel 1/den), and equivalently as the sequential
CD-then-border Redheffer.  The last Schur / Potapov pivot
of the closed system is extracted from the border
coordinate of M^dagger (r362 schur_b / q^dagger), NOT
by quoting sch.  The identification is then
    delta := 1 - q^dagger = 4 sch_b / (1 + 2 sch_b) = -sch
with c' = 1.  The companion form
    delta = c (1/4 - |Z_loc|^2)
is NOT a universal-c identity (window-dependent conversion;
sign disagreement on vacuous MAIN and living chi).

CALIBRATION DISCLOSURE.  Redheffer residuals, last-pivot
dictionary over Q, w9 / selected / dead-chi / ones-kill
first measured in /tmp (r433_cal.py, r433_cal2.py) on the
r362/r369/r401/r429 constructors, 2026-08-30.  Frozen
floors below are that measurement, sealed as gates.
Pins disclosed.  Builder fallback NOT taken: full wall
<< 120 s (no k=8 rebuild; r421 pin unused).

FROZEN FROM /tmp (live re-gated, not fitted):
  * SATZ Q: mixed form == Redheffer load A + U J U^T
    residual 0; sequential CD-then-border residual 0;
    2x2-block star residual 0.  den = 23/30.
    Last 1x1 of Phi = sch = -187/450.
    Last Schur of M^dagger onto the border
    sch_b = 187/1426 equals -sch / (2(2+sch)).
    delta = 4 sch_b / (1+2 sch_b) = 187/450 = -sch.
  * SATZ Q: 1/4 < 5/7 (the r263 M^2 threshold strictly
    above the 1/2-threshold).
  * w9: Redheffer / sequential / star residual 1.9e-15;
    sch = -0.066955766; q^dagger = 0.933044234;
    1-q^dagger = -sch at 1e-15; sch_b = 0.017318736
    = (1-q^dagger)/(2(1+q^dagger)); |Z_loc| = 0.157211;
    qtr = 0.225285; nE of Phi 3e-15.
  * k=3 (kz=5): |Z_loc| = 0.486846, air to 1/2 = 0.013154,
    qtr = 0.012981, delta = 0.071564 (small but positive).
  * Selected k=3..7,9: delta > 0 AND qtr > 0, conversion
    c = delta/qtr in [0.155, 5.51] -- NOT constant.
    1-q^dagger = -sch is f64-exact on shallow windows
    (w9 9.5e-13) and grows with the dual Gram (k=9
    kz=116 residual 5.5e-8, disclosed; bar 2e-7).
  * Dead chi 6/6: delta < 0 (CHI3-15/19/23/33/39 +
    CHI4-20).  Living CHI3-9: delta > 0 but qtr < 0
    (quarter is NOT the living/dead coordinate).
  * Vacuous MAIN kz12/16: delta > 0 (edge alive) but
    qtr < 0 (|Z_loc| > 1/2; selected-only census).
  * Scramble: nnegA0 = 21 (bulk already dead; edge
    pivot irrelevant).  Drop-border: no 3x3 last pivot
    (Y-block residual of the mixed toy is nonzero).
  * Ones-Woodbury Delta (r415 constant) at w9 is
    2.11e-3, not delta = 0.06696 (wrong pivot).
  * r263: q_N = (7/5) Z^2 EXACT on the FULL Z, not on
    Z_loc; q^dagger != q_N (w9 0.933 vs 0.214).

AUSGANG REDHEFFER_EXACT / PIVOT_IS_ONE_MINUS_QDAG /
QUARTER_NOT_UNIVERSAL.
SATZ: Redheffer identification of R -> R^dagger;
last-pivot dictionary delta = 1-q^dagger = -sch.
REFUTED: delta = c (1/4 - |Z_loc|^2) with world-blind
c > 0.  CENSUS: dead chi via delta < 0 (6/6); living
MAIN+chi delta > 0; selected same-sign with the
quarter, conversion window-dependent.  No RH claim.

MACHINERY: r369 MH.mixed_update_toy / mixed_rung,
r367 FTI.cut_rung / fr_*, r362 ABD.border_chain_pack /
bvec_chunked / scramble via r398 H, r401 ES.phi_block /
main_row / chi_row, r405 E.ones_woodbury_Y (kill),
r429 ZH.dissect / pack, r417 Woodbury-sch (readout).

NO RH CLAIM.  Finite identities, a named Redheffer
identification, a named last-pivot dictionary, a named
refutation of the universal quarter identity.  Research
documentation, not a theorem of RH.  No L* claim.
No R-dagger claim.
"""
from __future__ import annotations

import argparse
import ast
import hashlib
import math
import os
import sys
import time
from fractions import Fraction as Fr

import numpy as np

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DISC = os.path.dirname(os.path.abspath(__file__))
PROB = os.path.join(REPO, "rh", "problem")
for p in (DISC, PROB):
    if p not in sys.path:
        sys.path.insert(0, p)

import mixed_haynsworth_probe as MH  # noqa: E402
import final_two_rank_inertia_probe as FTI  # noqa: E402
import borodin_dual_hole_probe as BDH  # noqa: E402
import edge_signature_probe as ES  # noqa: E402
import zloc_head_probe as ZH  # noqa: E402
import compose_premises2_probe as C2  # noqa: E402
import dirichlet_matched_frame_probe as DMF  # noqa: E402
import pair_extremal_probe as PX  # noqa: E402
import verify_lstar_instance as V  # noqa: E402
import hirota_sign_probe as HS  # noqa: E402
import principal_bessel_probe as PB  # noqa: E402
import augmented_borodin_duality_probe as ABD  # noqa: E402
import high_moment_inertia_probe as H  # noqa: E402
import edge_contractive_lift_probe as E405  # noqa: E402

MH_SHA_PREFIX = "138d0997"
ES_SHA_PREFIX = "395673f2"
ZH_SHA_PREFIX = "cb57a725"
ABD_SHA_PREFIX = "7d810a9a"
FTI_SHA_PREFIX = "e0d79840"

FLOOR = 1.0e-8
ID_RES = 2.0e-12
ID_CENSUS = 2.0e-7
DEV_CENSUS = 1.0e-9
REL = 5.0e-3
M2 = Fr(5, 7)
SEL_LIVE = ((3, 5), (4, 9), (5, 17), (6, 26), (7, 43), (9, 116))
DEAD_CHI3 = (15, 19, 23, 33, 39)
CORE_SAMPLE = (9, 12, 16, 18, 20, 36)
SCR_NNEG = 21

W9_SCH = -0.0669557660032
W9_QDAG = 0.933044234
W9_SCHB = 1.731873612e-2
W9_ZLOC = 0.157211
W9_QTR = 0.225285
K3_ZLOC = 0.486846
K3_AIR = 0.013154
K3_SCH = -0.0715644904
K3_QTR = 0.012981
ONES_DLT_W9 = 2.110e-3
TOY_SCH = Fr(-187, 450)
TOY_SCHB = Fr(187, 1426)
TOY_DEN = Fr(23, 30)

SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
CHECKS = []
T0 = time.time()


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok)))
    print("  [%s] %-44s %s" % ("PASS" if ok else "FAIL", name, detail),
          flush=True)
    return bool(ok)


def section(t):
    print("\n" + "=" * 78)
    print(t)
    print("=" * 78, flush=True)


def firewall_audit():
    src = open(os.path.abspath(__file__), "r", encoding="utf-8").read()
    tree = ast.parse(src)
    forb = {"zeta" + "zero", "n" + "zeros", "prime" + "range",
            "is" + "prime", "gram" + "point"}
    bad = []
    for node in ast.walk(tree):
        nm = node.attr if isinstance(node, ast.Attribute) else (
            node.id if isinstance(node, ast.Name) else None)
        if nm and nm.lower() in forb:
            bad.append("%s@%d" % (nm, node.lineno))
    return (not bad), ("NO zero/prime oracles; Redheffer / mixed "
                       "3x3 / SM border / Z_loc formula only"
                       if not bad else "; ".join(bad))


def antigate_fragment_audit():
    frags = ("poly" + "fit", "curve_" + "fit", "lst" + "sq",
             "mini" + "mize", "Line" + "arRegression")
    src = open(os.path.abspath(__file__), "r", encoding="utf-8").read()
    tree = ast.parse(src)
    hits = []
    for node in ast.walk(tree):
        nm = None
        if isinstance(node, ast.Attribute):
            nm = node.attr
        elif isinstance(node, ast.Name):
            nm = node.id
        elif isinstance(node, ast.FunctionDef):
            nm = node.name
        if nm and any(f in nm for f in frags):
            hits.append("%s@%d" % (nm, node.lineno))
    return hits


# ---- Redheffer algebra ----

def redheffer_load(A, U, E):
    """Terminating Redheffer: T = A + U E U^T.
    Colligation Theta = [[A, U],[U.T, 0]], load E."""
    return A + U @ E @ U.T


def redheffer_star(A, B, C, D, P, Q, R, S):
    """2x2-block Redheffer star Theta star E.
    Theta=[[A,B],[C,D]], E=[[P,Q],[R,S]]."""
    k = D.shape[0]
    W = np.linalg.inv(np.eye(k) - P @ D)
    A2 = A + B @ W @ P @ C
    B2 = B @ W @ Q
    C2 = R @ np.linalg.inv(np.eye(k) - D @ P) @ C
    D2 = S + R @ D @ W @ Q
    return A2, B2, C2, D2


def last_schur_1x1(Phi):
    """Last 1x1 after eliminating the leading 2x2 of a 3x3."""
    K2 = Phi[:2, :2]
    c0 = Phi[:2, 2]
    return float(Phi[2, 2] - c0 @ np.linalg.solve(K2, c0))


def delta_from_schb(sch_b):
    """Energy pivot from the last M^dagger Schur (A6 inverted).
    q^dagger = (1-2 sch_b)/(1+2 sch_b), delta = 1-q^dagger
    = 4 sch_b / (1+2 sch_b).  Does not quote sch."""
    return (Fr(4) * sch_b) / (Fr(1) + Fr(2) * sch_b)


def mixed_toy_blocks():
    """The r369 4-node mixed update, Fractions.  Returns
    A, U, J, Md, den, sch, sch_b."""
    A0 = [[Fr(-1), Fr(0), Fr(0), Fr(0)],
          [Fr(0), Fr(1), Fr(0), Fr(0)],
          [Fr(0), Fr(0), Fr(2), Fr(0)],
          [Fr(0), Fr(0), Fr(0), Fr(3)]]
    Ucd = [[Fr(2), Fr(1)],
           [Fr(0), Fr(1)],
           [Fr(0), Fr(0)],
           [Fr(0), Fr(0)]]
    half = Fr(1, 2)
    I4 = MH.fr_diag(Fr(1), Fr(1), Fr(1), Fr(1))
    UU = FTI.fr_mul(Ucd, MH.fr_tr(Ucd))
    R = FTI.fr_add(FTI.fr_add(A0, MH.fr_scale(I4, half)), UU)
    vt = [[Fr(1, 3)], [Fr(1, 5)], [Fr(0)], [Fr(0)]]
    gam = Fr(1, 2)
    s = FTI.fr_mul(R, vt)
    den = (Fr(1) + gam) - sum(vt[i][0] * s[i][0] for i in range(4))
    A = MH.fr_blkdiag(A0, -half)
    U = [[Fr(0)] * 3 for _ in range(5)]
    for i in range(4):
        U[i][0] = Ucd[i][0]
        U[i][1] = Ucd[i][1]
        U[i][2] = s[i][0]
    U[4][2] = Fr(-1)
    J = MH.fr_diag(Fr(1), Fr(1), Fr(1) / den)
    Md = FTI.fr_add(A, FTI.fr_mul(U, FTI.fr_mul(J, MH.fr_tr(U))))
    S = [row[:4] for row in Md[:4]]
    b = [Md[i][4] for i in range(4)]
    c = Md[4][4]
    Si = BDH.fr_inv(S)
    xb = [sum(Si[i][j] * b[j] for j in range(4)) for i in range(4)]
    sch_b = c - sum(b[i] * xb[i] for i in range(4))
    Ainv = BDH.fr_inv(A)
    Phi = FTI.fr_add(MH.fr_diag(Fr(1), Fr(1), den),
                     FTI.fr_mul(MH.fr_tr(U), FTI.fr_mul(Ainv, U)))
    K2 = [row[:2] for row in Phi[:2]]
    c0 = [Phi[0][2], Phi[1][2]]
    K2i = BDH.fr_inv(K2)
    cKc = (c0[0] * (K2i[0][0] * c0[0] + K2i[0][1] * c0[1])
           + c0[1] * (K2i[1][0] * c0[0] + K2i[1][1] * c0[1]))
    sch = Phi[2][2] - cKc
    # sequential CD then border
    MY = FTI.fr_add(A0, UU)
    Ap = MH.fr_blkdiag(MY, -half)
    ub = [[s[i][0]] for i in range(4)] + [[Fr(-1)]]
    Jb = [[Fr(1) / den]]
    Mseq = FTI.fr_add(Ap, FTI.fr_mul(ub, FTI.fr_mul(Jb, MH.fr_tr(ub))))
    dev_seq = max(abs(Md[i][j] - Mseq[i][j])
                  for i in range(5) for j in range(5))
    Tm = MH.mixed_update_toy()
    return dict(A=A, U=U, J=J, Md=Md, den=den, sch=sch, sch_b=sch_b,
                Phi=Phi, dev_mix=Tm["dev"], dev_seq=dev_seq,
                dev2=Tm["dev2"], A0=A0, Ucd=Ucd, UU=UU)


def dict_Q():
    z0 = Fr(1, 2)
    return dict(z0=z0, qtr=z0 * z0, M2=M2,
                qtr_lt_M2=z0 * z0 < M2,
                qN_at_half=Fr(7, 5) * z0 * z0)


def fr_mat(A):
    return np.array([[float(x) for x in row] for row in A], float)


# ---- window pack ----

def _measures(kz, chi=None):
    if chi is None:
        R = PX.build_rung(kz)
        mz = R["mz"]
        alk = float(V.window_shape(kz)[0])
        dsm = HS.window_data(kz, comb=PB.smooth_comb(alk))
        return dict(
            xu=mz["xu"], wu=mz["wu"], yn=mz["yn"], vn=mz["vn"],
            Nw=R["Nw"], S=R["S"], L=mz["L"], i1=R["i1"], i2=R["i2"],
            xp=mz["xp"], wp=mz["wp"],
            bxs=dsm["xs"], bws=dsm["ws"],
            bys=dsm["ys"], bvs=dsm["vs"], Bm=R["B"],
            tag="MAIN-%d" % kz, kz=kz)
    q, lpq, tag = chi
    uu, ww, _nn, _ch = DMF.chi_window_comb(kz, q)
    mzc = DMF.chi_build_measures(kz, uu, ww, 1.0, lpq)
    j1, j2 = PX.pair_select(mzc["yn"])
    usm, wsm = PB.smooth_comb(mzc["alpha"])
    mzb = DMF.chi_build_measures(kz, usm, wsm, 1.0, lpq)
    return dict(
        xu=mzc["xu"], wu=mzc["wu"], yn=mzc["yn"], vn=mzc["vn"],
        Nw=mzc["Nw"], S=mzc["S"], L=mzc["L"], i1=j1, i2=j2,
        xp=mzc["xp"], wp=mzc["wp"],
        bxs=mzb["xp"], bws=mzb["wp"],
        bys=mzb["yn"], bvs=mzb["vn"], Bm=None,
        tag=tag, kz=kz)


def redheffer_of(m):
    """Build the mixed colligation and read the Redheffer
    residuals plus the last pivot.  Consumes measure arrays
    only (no target sch, no Z_loc)."""
    cut = FTI.cut_rung(m["xu"], m["wu"], m["yn"], m["vn"],
                       m["Nw"], m["S"], m["L"], m["i1"], m["i2"],
                       keep=True)
    bp = ABD.border_chain_pack(
        np.asarray(m["xp"], float), np.asarray(m["wp"], float),
        np.asarray(m["yn"], float), np.asarray(m["vn"], float),
        m["bxs"], m["bws"], m["bys"], m["bvs"], m["Nw"])
    out = dict(ok=False, tag=m["tag"], kz=m["kz"],
               nnegA0=int(cut["nneg"]), P1=bool(cut["P1"]))
    if not bp.get("ok"):
        out["nf"] = bp.get("nf")
        return out
    a_mu, b_mu, h0_mu = V.mu_chain(np.asarray(m["xp"], float),
                                  np.asarray(m["wp"], float), m["Nw"])
    bxa = np.concatenate([np.asarray(m["bxs"], float),
                          np.asarray(m["bys"], float)])
    bwa = np.concatenate([np.asarray(m["bws"], float),
                          -np.asarray(m["bvs"], float)])
    bvec = ABD.bvec_chunked(a_mu, b_mu, h0_mu, bxa, bwa, m["Nw"])
    gam = float(bvec @ bvec) / float(bp["Bw"])
    Bm = m["Bm"]
    if Bm is None:
        Bm = V.b_matrix(a_mu, b_mu, h0_mu, m["yn"], m["vn"], m["Nw"])
    v = Bm @ (bvec / math.sqrt(bp["Bw"]))
    vt = cut["epsY"] * v
    A0 = np.asarray(cut["A0"], float)
    Ucd = np.asarray(cut["U"], float)
    Rm = cut["Rm"]
    s = Rm @ vt
    den = (1.0 + gam) - float(vt @ s)
    Sm = A0.shape[0]
    A = np.zeros((Sm + 1, Sm + 1))
    A[:Sm, :Sm] = A0
    A[Sm, Sm] = -0.5
    U = np.zeros((Sm + 1, 3))
    U[:Sm, :2] = Ucd
    U[:Sm, 2] = s
    U[Sm, 2] = -1.0
    J = np.diag([1.0, 1.0, 1.0 / den])
    Mred = redheffer_load(A, U, J)
    D0 = np.zeros((3, 3))
    P, Q = J, np.zeros((3, 1))
    Rr, Sblk = np.zeros((1, 3)), np.zeros((1, 1))
    A2, _B2, _C2, _D2 = redheffer_star(A, U, U.T, D0, P, Q, Rr, Sblk)
    Rinv = np.linalg.inv(Rm)
    Z = np.zeros((Sm + 1, Sm + 1))
    Z[:Sm, :Sm] = Rinv
    Z[:Sm, Sm] = vt
    Z[Sm, :Sm] = vt
    Z[Sm, Sm] = 1.0 + gam
    Rdag = 0.5 * (np.linalg.inv(Z) + np.linalg.inv(Z).T)
    Mdag = Rdag - 0.5 * np.eye(Sm + 1)
    MY = A0 + Ucd @ Ucd.T
    Ap = np.zeros((Sm + 1, Sm + 1))
    Ap[:Sm, :Sm] = MY
    Ap[Sm, Sm] = -0.5
    ub = np.zeros((Sm + 1, 1))
    ub[:Sm, 0] = s
    ub[Sm, 0] = -1.0
    Mseq = Ap + (1.0 / den) * (ub @ ub.T)
    En = Bm @ Bm.T
    qdag = gam + float(v @ np.linalg.solve(np.eye(Sm) - En, v))
    xb = np.linalg.solve(Mdag[:Sm, :Sm], Mdag[:Sm, Sm])
    sch_b = float(Mdag[Sm, Sm] - Mdag[Sm, :Sm] @ xb)
    pred_b = (1.0 - qdag) / (2.0 * (1.0 + qdag))
    Phi = np.diag([1.0, 1.0, float(den)]) + U.T @ np.linalg.solve(A, U)
    Phi = 0.5 * (Phi + Phi.T)
    sch = last_schur_1x1(Phi)
    delta = 1.0 - qdag
    out.update(
        ok=True, den=float(den), gam=gam, qN=float(bp["qN"]),
        qdag=qdag, sch=sch, sch_b=sch_b, pred_b=pred_b,
        delta=delta, msch=-sch,
        id_q=abs(delta + sch),
        id_a6=abs(sch_b / pred_b - 1.0) if pred_b else float("inf"),
        dev_load=float(np.max(np.abs(Mred - Mdag))),
        dev_star=float(np.max(np.abs(A2 - Mdag))),
        dev_seq=float(np.max(np.abs(Mseq - Mdag))),
        nnegPhi=int(np.sum(np.linalg.eigvalsh(Phi) < -FLOOR)),
    )
    return out


def zloc_of(kz, chi=None):
    if chi is None:
        d = ZH.dissect(ZH.pack(kz))
    else:
        fam = "CHI3" if chi[0] == DMF.Q_CHI3 else "CHI4"
        d = ZH.dissect(C2.chi_pack(fam, kz))
    z = float(d["Zloc"])
    return dict(Zloc=z, absZ=abs(z), qtr=0.25 - z * z,
                Z=float(d["Z"]))


def row_of(kz, chi=None):
    m = _measures(kz, chi=chi)
    p = redheffer_of(m)
    z = zloc_of(kz, chi=chi)
    p.update(z)
    if p.get("ok") and abs(p["qtr"]) > 1e-18:
        p["c_qtr"] = p["delta"] / p["qtr"]
    else:
        p["c_qtr"] = float("nan")
    return p


# ---- legs ----

def part_satz():
    section("S1  SATZ / Q -- Redheffer step + last-pivot dictionary")
    T = mixed_toy_blocks()
    check("G01-Redheffer-mixed-Q",
          T["dev_mix"] == 0 and T["den"] == TOY_DEN,
          "A+UJU^T == M^dagger, den=%s residual EXACT 0" % T["den"])
    check("G02-sequential-CD-border-Q",
          T["dev_seq"] == 0,
          "CD-then-border Redheffer == packed 3x3, residual 0")
    Af, Uf, Jf = fr_mat(T["A"]), fr_mat(T["U"]), fr_mat(T["J"])
    Md = fr_mat(T["Md"])
    load = redheffer_load(Af, Uf, Jf)
    D0 = np.zeros((3, 3))
    A2, _B, _C, _D = redheffer_star(
        Af, Uf, Uf.T, D0, Jf, np.zeros((3, 1)),
        np.zeros((1, 3)), np.zeros((1, 1)))
    check("G03-star-load-float",
          float(np.max(np.abs(load - Md))) < 1e-14
          and float(np.max(np.abs(A2 - Md))) < 1e-14,
          "2x2-block star residual %.1e" % float(np.max(np.abs(A2 - Md))))
    check("G04-last-Phi-is-sch-Q",
          T["sch"] == TOY_SCH,
          "last 1x1 of E=Phi = sch = %s" % T["sch"])
    rhs = -T["sch"] / (Fr(2) * (Fr(2) + T["sch"]))
    check("G05-schb-dictionary-Q",
          T["sch_b"] == TOY_SCHB and T["sch_b"] == rhs,
          "sch_b = %s = -sch/(2(2+sch))" % T["sch_b"])
    dlt = delta_from_schb(T["sch_b"])
    check("G06-delta-from-schb-Q",
          dlt == -T["sch"] and dlt == Fr(187, 450),
          "delta = 4 sch_b/(1+2 sch_b) = -sch = %s (c'=1)" % dlt)
    t = dict_Q()
    check("G07-quarter-below-M2",
          t["qtr_lt_M2"] and t["qN_at_half"] == Fr(7, 20),
          "1/4 < 5/7; q_N(Z=1/2)=7/20 < 1")
    check("G08-drop-border-Q",
          T["dev2"] != 0,
          "Y-block without border != M^dagger (no last pivot)")
    return T


def part_pins():
    section("S2  PINS -- w9 Redheffer + k=3 margin")
    w = row_of(9)
    check("G10-w9-Redheffer",
          w["ok"]
          and w["dev_load"] < 1e-12
          and w["dev_star"] < 1e-12
          and w["dev_seq"] < 1e-12,
          "load/star/seq residual %.1e / %.1e / %.1e"
          % (w["dev_load"], w["dev_star"], w["dev_seq"]))
    check("G11-w9-delta-identity",
          abs(w["sch"] - W9_SCH) <= 1e-10
          and abs(w["qdag"] - W9_QDAG) <= 1e-8
          and w["id_q"] < ID_RES
          and abs(w["sch_b"] - W9_SCHB) <= 1e-10
          and w["id_a6"] < 1e-8,
          "sch=%.10f q^d=%.10f 1-q^d=-sch (%.1e); sch_b=%.10f A6"
          % (w["sch"], w["qdag"], w["id_q"], w["sch_b"]))
    check("G12-w9-Zloc-quarter",
          abs(w["absZ"] - W9_ZLOC) <= 2e-6
          and abs(w["qtr"] - W9_QTR) <= 2e-6
          and w["qtr"] > 0 and w["delta"] > 0,
          "|Zloc|=%.6f qtr=%.6f delta=%.6f c=%.4f"
          % (w["absZ"], w["qtr"], w["delta"], w["c_qtr"]))
    k3 = row_of(5)
    check("G13-k3-margin",
          abs(k3["absZ"] - K3_ZLOC) <= 2e-6
          and abs((0.5 - k3["absZ"]) - K3_AIR) <= 2e-6
          and abs(k3["qtr"] - K3_QTR) <= 2e-6
          and abs(k3["sch"] - K3_SCH) <= 1e-8
          and k3["delta"] > 0 and k3["id_q"] < ID_RES,
          "|Zloc|=%.10f air=%.10f qtr=%.6f delta=%.6f"
          % (k3["absZ"], 0.5 - k3["absZ"], k3["qtr"], k3["delta"]))
    return w, k3


def part_worlds(smoke):
    section("S3  WORLDS -- selected / dead chi / scramble")
    sel = []
    for k, kz in SEL_LIVE:
        if smoke and k > 4:
            continue
        r = row_of(kz)
        r["k"] = k
        sel.append(r)
        print("    k=%d kz=%d delta=%+.6f qtr=%+.6f c=%.4f "
              "1-q^d+sch=%.1e" % (
                  k, kz, r["delta"], r["qtr"], r["c_qtr"], r["id_q"]),
              flush=True)
    check("G20-selected-delta-pos",
          all(r["ok"] and r["delta"] > 0 and r["qtr"] > 0
              and r["id_q"] < ID_CENSUS for r in sel),
          "%d/%d selected delta>0 AND qtr>0; identity 1-q^d=-sch"
          % (len(sel), len(sel)))
    deads = []
    dead_spec = [(kz, DMF.Q_CHI3, DMF.LPQ3, "CHI3-%d" % kz)
                 for kz in DEAD_CHI3]
    dead_spec.append((20, DMF.Q_CHI4, DMF.LPQ4, "CHI4-20"))
    if smoke:
        dead_spec = [dead_spec[0], dead_spec[-1]]
    for kz, q, lp, tag in dead_spec:
        r = row_of(kz, chi=(q, lp, tag))
        deads.append(r)
        print("    %s delta=%+.6f sch=%+.6f qtr=%+.5f nneg=%d id=%.1e"
              % (tag, r["delta"], r["sch"], r["qtr"], r["nnegA0"],
                 r["id_q"]),
              flush=True)
    check("G21-dead-chi-delta-neg",
          all(r["ok"] and r["delta"] < 0 and r["sch"] > 0
              and r["id_q"] < ID_CENSUS for r in deads)
          and (smoke or len(deads) == 6),
          "%d/%d dead chi delta<0 (q^d>1); identity holds"
          % (len(deads), 2 if smoke else 6))
    live9 = row_of(9, chi=(DMF.Q_CHI3, DMF.LPQ3, "CHI3-9"))
    check("G22-live-chi-quarter-disagrees",
          live9["ok"] and live9["delta"] > 0 and live9["qtr"] < 0
          and live9["id_q"] < ID_CENSUS,
          "CHI3-9 living delta=%+.4f but qtr=%+.4f (quarter "
          "is not the death coordinate)" % (live9["delta"], live9["qtr"]))
    mz_s = H.scramble_mz()
    j1, j2 = PX.pair_select(mz_s["yn"])
    oS = FTI.cut_rung(mz_s["xu"], mz_s["wu"], mz_s["yn"], mz_s["vn"],
                       mz_s["Nw"], mz_s["S"], mz_s["L"], j1, j2)
    check("G23-scramble-bulk-dead",
          oS["nneg"] == SCR_NNEG,
          "scramble nnegA0=%d (bulk already dead; edge "
          "pivot of a 3x3 is irrelevant)" % oS["nneg"])
    return sel, deads, live9


def part_kills(w9):
    section("S4  KILLS -- drop-border / ones / quarter / r263")
    cut = FTI.cut_rung
    R = PX.build_rung(9)
    mz = R["mz"]
    c9 = FTI.cut_rung(mz["xu"], mz["wu"], mz["yn"], mz["vn"],
                      R["Nw"], R["S"], mz["L"], R["i1"], R["i2"],
                      keep=True)
    ones = E405.ones_woodbury_Y(c9["A0"], c9["U"])
    check("G30-ones-not-the-pivot",
          abs(ones["Delta"] - ONES_DLT_W9) <= 2e-4
          and abs(ones["Delta"] - w9["delta"]) > 0.05,
          "ones Delta=%.4e != delta=%.4e (r415 constant "
          "is the wrong pivot)" % (ones["Delta"], w9["delta"]))
    # quarter conversion not constant on selected k=3 vs k=4
    r3 = row_of(5)
    c3, c4 = r3["c_qtr"], w9["c_qtr"]
    check("G31-quarter-c-not-universal",
          abs(c3 - c4) / max(abs(c3), abs(c4)) > 0.5
          and c3 > 0 and c4 > 0,
          "c_3=%.3f c_4=%.3f (window-dependent; both "
          "positive on selected)" % (c3, c4))
    qN_Z = (7.0 / 5.0) * w9["Z"] ** 2
    qN_Zl = (7.0 / 5.0) * w9["Zloc"] ** 2
    check("G32-r263-full-Z-not-Zloc",
          abs(w9["qN"] - qN_Z) / max(abs(w9["qN"]), 1e-18) < 1e-8
          and abs(qN_Zl - w9["qN"]) > 0.1
          and abs(w9["qdag"] - w9["qN"]) > 0.5
          and (0.25 < 5.0 / 7.0),
          "q_N=(7/5)Z^2=%.6f; (7/5)Zloc^2=%.6f; q^d=%.6f "
          "!= q_N; 1/4<5/7" % (qN_Z, qN_Zl, w9["qdag"]))
    # mutant threshold 5/7 - |Z_loc|^2 vs 1/4
    m2form = (5.0 / 7.0) - w9["Zloc"] ** 2
    check("G33-M2-form-not-delta",
          abs(m2form - w9["delta"]) > 0.5
          and m2form > 0,
          "M^2-|Zloc|^2=%.4f != delta=%.4f (r263 "
          "dictionary is a different coordinate)"
          % (m2form, w9["delta"]))
    return ones


def part_census(smoke):
    section("S5  CENSUS" + (" (smoke skip)" if smoke else ""))
    if smoke:
        return []
    rows = []
    for k, kz in SEL_LIVE:
        r = row_of(kz)
        r["k"] = k
        rows.append(r)
    cs = [r["c_qtr"] for r in rows]
    check("G40-selected-full-identity",
          len(rows) == 6
          and all(r["delta"] > 0 and r["qtr"] > 0
                  and r["id_q"] < ID_CENSUS
                  and r["dev_load"] < DEV_CENSUS for r in rows),
          "6/6 selected: Redheffer exact, delta>0, qtr>0, "
          "c in [%.3f, %.3f]" % (min(cs), max(cs)))
    core = []
    for kz in CORE_SAMPLE:
        r = row_of(kz)
        core.append(r)
        print("    CORE kz=%d P1=%s delta=%+.5f qtr=%+.5f "
              "id=%.1e" % (kz, r["P1"], r["delta"], r["qtr"],
                           r["id_q"]), flush=True)
    check("G41-core-identity",
          all(r["ok"] and r["id_q"] < ID_CENSUS for r in core)
          and all(r["delta"] > 0 for r in core),
          "core-sample 6/6 1-q^d=-sch; all delta>0 "
          "(kz12/16 qtr<0: quarter selected-only)")
    vac = [r for r in core if not r["P1"]]
    check("G42-vacuous-quarter-split",
          len(vac) >= 2
          and all(r["delta"] > 0 and r["qtr"] < 0 for r in vac),
          "vacuous MAIN (kz12/16 class) alive by delta, "
          "dead by quarter -- conversion may be negative")
    return rows


def main():
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke

    print("=" * 78)
    print("edge_redheffer_probe -- "
          "PRIME.RDAGGER.EDGE_REDHEFFER_COMPLETION.01 (round 433)")
    print("SPEC_SHA %s" % SPEC_SHA[:16])
    print("mode: %s" % ("SMOKE" if smoke else
                        "FULL (selected k=3..7,9; k=8 not rebuilt)"))
    print("=" * 78)

    section("S0  FIREWALL + IMPORT SHA")
    okf, det = firewall_audit()
    check("G00-firewall", okf, det)
    sha_ok = (MH.SPEC_SHA.startswith(MH_SHA_PREFIX)
              and ES.SPEC_SHA.startswith(ES_SHA_PREFIX)
              and ZH.SPEC_SHA.startswith(ZH_SHA_PREFIX)
              and ABD.SPEC_SHA.startswith(ABD_SHA_PREFIX)
              and FTI.SPEC_SHA.startswith(FTI_SHA_PREFIX))
    check("G00b-import-sha", sha_ok,
          "MH %s ES %s ZH %s ABD %s FTI %s"
          % (MH.SPEC_SHA[:8], ES.SPEC_SHA[:8], ZH.SPEC_SHA[:8],
             ABD.SPEC_SHA[:8], FTI.SPEC_SHA[:8]))
    ag = antigate_fragment_audit()
    check("G00c-no-fit", not ag,
          "no fit primitives" if not ag else "; ".join(ag))

    part_satz()
    w9, _k3 = part_pins()
    part_worlds(smoke)
    part_kills(w9)
    part_census(smoke)

    section("S6  VERDICT")
    prev_ok = all(ok for _n, ok in CHECKS)
    check("G50-verdict",
          prev_ok,
          "REDHEFFER_EXACT / PIVOT_IS_ONE_MINUS_QDAG / "
          "QUARTER_NOT_UNIVERSAL.  no RH / L* / R-dagger")

    n_fail = sum(1 for _n, ok in CHECKS if not ok)
    n_ok = len(CHECKS) - n_fail
    verd = ("REDHEFFER_EXACT / PIVOT_IS_ONE_MINUS_QDAG / "
            "QUARTER_NOT_UNIVERSAL")
    print("\nRESULT: %d/%d gates PASS   SPEC_SHA %s   (%.1fs)  %s" % (
        n_ok, len(CHECKS), SPEC_SHA[:16], time.time() - T0, verd))
    if n_fail == 0:
        print("EDGE REDHEFFER %sVERIFIED" % ("SMOKE " if smoke else ""))
        return 0
    print("EDGE REDHEFFER FAILED %d" % n_fail)
    return 1


if __name__ == "__main__":
    sys.exit(main())
