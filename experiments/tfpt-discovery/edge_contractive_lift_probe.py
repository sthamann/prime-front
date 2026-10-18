#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""edge_contractive_lift_probe -- PRIME.LDAGGER.EDGE_CONTRACTIVE_LIFT.01
(round 405): the edge half of the one-defect factorisation
(reviewer DCCLXIX sections 8 and 12, 35 pct lane).  Can the
missing Euler null mode be written ell = V c with
  V = [F_Lam, F_Gamma, F_Uv, U J^{1/2}]
from geometric Euler recurrences (no optimiser), with
1-||c||^2 a manifest positive source sum, and with
1-||c||^2 = kappa(a,b) (-sch) in the r401 Sylvester chart?

Coexistence: r401 EDGE_SIGNATURE_MODEL (exact 3x3 Phi_edge,
sch the living/dead coordinate); r400/r403 one bulk defect
candidate; r404 SOURCE_GRAM_NOT_EXACT (class 3 not reached;
|cos|(v_-, 1)=0.007 -- the ones-mode is not the A0 defect).
This round does not revive P1 as an inequality and does not
use lambda_-, psi_- as a lift input (v_- is a labelled
CONTROL only).

LEGS (reviewer 12).
  1  Contractive lift: c from finite geometric Euler
     recurrences + Uvarov remainder + border + Gamma/pole.
     First check only ell = V c; residual 0 from expansion.
  2  Norm identity: ||c||^2 without an optimiser.  Target
     1-||c||^2 = eta_Gamma + eta_pole + Sum_p (1-p^{-1})|b_p|^2
     + Sum_p p^{-(K_p+1)}|t_p|^2 (or Q-equivalent).
  3  r401 chart: 1-||c||^2 = kappa(a,b)(-sch), kappa>0, by
     finite determinant / congruence bookkeeping.
  4  Worlds must be predicted: MAIN ||c||<1; living chi
     ||c||<1; dead chi ||c||>1 (death as overflow);
     weight-perm already breaks (G); jitter already breaks
     the Euler identity.  Kills: omit tail, wrong J.

CALIBRATION DISCLOSURE.  Euler-tail residuals, Woodbury
Delta, kappa_closed over Q, disk Parseval, tail-vs-border
relres, ones-split (Delta, c2, kappa) on w9 / core-42 /
chi3, vneg-vs-geo residual first measured in /tmp
(r405_cal.py, r405_cal2.py) on the same constructors,
2026-08-29.  Frozen floors below are that measurement,
sealed as gates.  No two-commit pre-blind freeze: pins
disclosed.  Builder fallback NOT taken: full wall < 20 s
(bar 120 s).

FROZEN FROM /tmp (live re-gated, not fitted):
  * SATZ Q: 1 - z^{K+1} = (1-z) Sum_{r=0}^K z^r at z=1/3,
    K=5 (lhs = 728/729).  Omit-tail remainder = z^{K+1}.
  * SATZ Q: disk energy (1-q) Sum_{r=0}^K q^r = 1-q^{K+1}
    at q=1/2, K=6 (||c||^2 = 127/128, reserve q^{K+1}=1/128).
  * SATZ Q: Woodbury Delta = 1 - ell^T B^{-1} ell and
    Delta = kappa_closed (-sch) with
    kappa_closed = -(1-eta) det(K2)/det(K_W) on a rational
    3x3 (eta=13/12, Delta=7/36, sch=21/8, kappa=-2/27).
  * SATZ f64: geometric reconstruction of the constant on Y
    (convex combination of E_p+T_p) residual 8e-16 at w9.
  * REFUTED: SM-border s = aggregated z^{K+1} (relres 0.996
    on arccos*log p; corr 0.07).  All named phase
    conventions leave relres >= 0.96.
  * REFUTED as A0-defect lift: v_- vs geometric V has
    relres 0.81 (geo+Ucd still 0.45).  |cos|(v_-,1)=0.007
    (r400/r404).  Fat [F_Lam,F_Gamma,Ucd] spanning Y is
    an overcomplete tautology, not a source c.
  * Ones-split Woodbury (H = A0 + oo^T, 2-col CD): w9
    Delta=2.110e-3, c2=0.99789, kappa=0.0315, sch=-0.06696.
    Core-42: Delta>0 42/42, kappa>0 42/42, 0<c2<1 42/42,
    Delta in [6.7e-6, 2.11e-3].
  * Worlds: living chi3 37/37 kappa>0 c2<1; dead chi3 5/5
    sch>0 kappa<0 AND c2<1 -- overflow ||c||>1 REFUTED.
    Death remains sch>0 (r401), not a norm overflow of
    this source c.  Geometric 1-||c||^2 (disk sum) is
    O(10^{-1}); Woodbury Delta is O(10^{-5}..10^{-3}):
    they are not the same scalar, so E3 as
    "sum form = kappa(-sch)" is REFUTED on scale.
  * kappa is NOT a function of (a,b) alone (depends on
    the (H,ell) split).  The determinant identity is a
    SATZ; uniqueness of kappa(a,b) is not.
  * Kills: omit tail residual = ||z^{K+1}|| != 0 over Q;
    wrong-sign J mixed residual != 0 (r401); permute
    nneg~20 (r403, (G) breaks); node jitter does NOT
    break the Euler-tail identity (it is an identity in
    z, not a Gram of positions -- the jitter kill sits
    on r403/r404, not here).

AUSGANG EDGE_LIFT_PARTIAL.  SATZ: Euler tail; disk
Parseval; Woodbury Delta; kappa_closed determinant
identity.  CENSUS: ones-split ||c||<1 on living and on
dead; dead die at kappa<0 (sch>0).  REFUTED: border=
tail; dead as ||c||>1; geometric sum = kappa(-sch);
kappa=kappa(a,b) only.  OPEN: source c for the mixed
A0 defect (blocked by r404 class-3 stop and by
v_- not in the geometric span).  No RH claim.

MACHINERY: r401 ES.Phi_edge / main_row / chi_row /
sylvester_D2, r369 MH.mixed_update_toy, r367 FTI.cut_rung,
r404 G.euler_F / cauchy_F (SHA gate + cosine control),
r403 P.reweight permute, r398 HM.scramble / two-period,
r226 V.build_measures / admissible_indices.

NO RH CLAIM.  Finite identities, named refutations,
named open edge.  Research documentation, not a
theorem of RH.
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

import edge_signature_probe as ES  # noqa: E402
import mixed_haynsworth_probe as MH  # noqa: E402
import final_two_rank_inertia_probe as FTI  # noqa: E402
import pair_extremal_probe as PX  # noqa: E402
import dirichlet_matched_frame_probe as DMF  # noqa: E402
import high_moment_inertia_probe as HM  # noqa: E402
import p1_construction_probe as P1  # noqa: E402
import one_defect_gram_probe as G404  # noqa: E402
import verify_lstar_instance as V  # noqa: E402
import hirota_sign_probe as HS  # noqa: E402
import principal_bessel_probe as PB  # noqa: E402
import augmented_borodin_duality_probe as ABD  # noqa: E402

ES_SHA_PREFIX = "395673f2"
MH_SHA_PREFIX = "138d0997"
FTI_SHA_PREFIX = "e0d79840"
G404_SHA_PREFIX = "c0260053"
P1_SHA_PREFIX = "ba6817f5"

FLOOR = 1.0e-8
REL = 5.0e-2
GEO_RES_HI = 1.0e-12
TAIL_RELRES_LO = 0.90
VNEG_GEO_LO = 0.50
COS_ONES_HI = 0.05
CORE_N = 42
CHI3_LIVE_N, CHI3_DEAD_N = 37, 5
SCR_NNEG, TP21_NNEG = 21, 4
PERM_NNEG_LO = 15

W9_SCH = ES.W9_SCH
W9_DLT = 2.109956e-3
W9_C2 = 0.997890
W9_KAPPA = 3.151e-2
D15_DLT = 5.1103841075e-3
D15_KAPPA = -0.220456
D15_C2 = 0.9948896159

PRIMES_GEO = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29)
K_GEO = 4

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
    return (not bad), ("NO zero/prime oracles; Euler tail / "
                       "Woodbury / r401 sch / geometric c only"
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


def np_sym(A):
    A = np.asarray(A, float)
    return 0.5 * (A + A.T)


# ---- SATZ constructors (no fit, no lambda_-) ----

def euler_tail_Q(z=Fr(1, 3), K=5):
    s = sum((z ** r) for r in range(K + 1))
    lhs = Fr(1) - z ** (K + 1)
    rhs = (Fr(1) - z) * s
    omit = lhs - (Fr(1) - z) * sum((z ** r) for r in range(K + 1))
    # omit-tail: drop z^{K+1} from the identity => remainder z^{K+1}
    rem = z ** (K + 1)
    return dict(lhs=lhs, rhs=rhs, ok=(lhs == rhs), rem=rem,
                omit_neq=(rem != 0))


def disk_parseval_Q(q=Fr(1, 2), K=6):
    """(1-q) Sum_{r=0}^K q^r = 1 - q^{K+1}.  q = |z|^2 = p^{-1}."""
    lhs = (Fr(1) - q) * sum((q ** r) for r in range(K + 1))
    rhs = Fr(1) - q ** (K + 1)
    return dict(lhs=lhs, rhs=rhs, ok=(lhs == rhs), reserve=rhs)


def kappa_closed_Q():
    """Rational 3x3 Woodbury / Schur identity.  H=diag(2,3,4),
    ell=(1,1,1), U=I, Jinv=diag(1,1,2).  Closed over Q."""
    Hinv = [Fr(1, 2), Fr(1, 3), Fr(1, 4)]
    ell = [Fr(1), Fr(1), Fr(1)]
    eta = sum(ell[i] * Hinv[i] * ell[i] for i in range(3))
    Jinv = [Fr(1), Fr(1), Fr(2)]
    Kw = [Hinv[i] + Jinv[i] for i in range(3)]
    r = [Hinv[i] * ell[i] for i in range(3)]
    rKw_r = sum(r[i] * r[i] / Kw[i] for i in range(3))
    Delta = Fr(1) - eta + rKw_r
    H = [[Fr(2), Fr(0), Fr(0)],
         [Fr(0), Fr(3), Fr(0)],
         [Fr(0), Fr(0), Fr(4)]]
    A = [[H[i][j] - ell[i] * ell[j] for j in range(3)]
         for i in range(3)]

    def det3(M):
        return (M[0][0] * (M[1][1] * M[2][2] - M[1][2] * M[2][1])
                - M[0][1] * (M[1][0] * M[2][2] - M[1][2] * M[2][0])
                + M[0][2] * (M[1][0] * M[2][1] - M[1][1] * M[2][0]))

    dA = det3(A)

    def cof(M, i, j):
        minor = [[M[a][b] for b in range(3) if b != j]
                 for a in range(3) if a != i]
        dm = minor[0][0] * minor[1][1] - minor[0][1] * minor[1][0]
        return dm * (Fr(1) if (i + j) % 2 == 0 else Fr(-1))

    Ainv = [[cof(A, j, i) / dA for j in range(3)] for i in range(3)]
    Phi = [[(Fr(1) if i == j and i < 2 else
             (Fr(2) if i == j else Fr(0))) + Ainv[i][j]
            for j in range(3)] for i in range(3)]
    K2 = [[Phi[0][0], Phi[0][1]], [Phi[1][0], Phi[1][1]]]
    detK2 = K2[0][0] * K2[1][1] - K2[0][1] * K2[1][0]
    c0 = [Phi[0][2], Phi[1][2]]
    inv0 = (K2[1][1] * c0[0] - K2[0][1] * c0[1]) / detK2
    inv1 = (-K2[1][0] * c0[0] + K2[0][0] * c0[1]) / detK2
    sch = Phi[2][2] - (c0[0] * inv0 + c0[1] * inv1)
    detKw = Kw[0] * Kw[1] * Kw[2]
    kappa = -(Fr(1) - eta) * detK2 / detKw
    return dict(eta=eta, Delta=Delta, sch=sch, kappa=kappa,
                equal=(Delta == kappa * (-sch)), detK2=detK2)


def cauchy_gram_Q():
    """2-point Cauchy Gram 1/(z_i z_j) at z=1,2 over Q is PD."""
    G00, G01, G11 = Fr(1, 2), Fr(1, 3), Fr(1, 4)
    det = G00 * G11 - G01 * G01
    return det, det > 0


def geometric_ones(yn, primes=PRIMES_GEO, K=K_GEO):
    """Source-explicit c: nu_p from log p, 1 = Sum nu_p (E_p+T_p)
    pointwise from the Euler tail.  No optimiser."""
    yn = np.asarray(yn, float)
    th = np.arccos(np.clip(yn, -1.0, 1.0))
    logs = np.array([math.log(p) for p in primes], float)
    nu = logs / float(np.sum(logs))
    rec = np.zeros(len(yn), dtype=complex)
    cols = []
    bterm = tterm = 0.0
    for p, w in zip(primes, nu):
        z = (p ** -0.5) * np.exp(1j * th * math.log(p))
        geom = sum(z ** r for r in range(K + 1))
        E = (1.0 - z) * geom
        T = z ** (K + 1)
        rec += w * (E + T)
        cols.append(np.real(w * E))
        cols.append(np.imag(w * E))
        cols.append(np.real(w * T))
        cols.append(np.imag(w * T))
        bterm += (1.0 - 1.0 / p) * float(w * w)
        tterm += (p ** -(K + 1)) * float(w * w)
    ones = np.ones(len(yn))
    res = float(np.linalg.norm(ones - rec.real))
    Vgeo = np.column_stack(cols)
    return dict(res=res, res_im=float(np.linalg.norm(rec.imag)),
                sumform=bterm + tterm, bterm=bterm, tterm=tterm,
                V=Vgeo, rec=rec.real, nu=nu)


def omit_tail_residual(yn, primes=PRIMES_GEO, K=K_GEO):
    yn = np.asarray(yn, float)
    th = np.arccos(np.clip(yn, -1.0, 1.0))
    logs = np.array([math.log(p) for p in primes], float)
    nu = logs / float(np.sum(logs))
    rec = np.zeros(len(yn), dtype=complex)
    for p, w in zip(primes, nu):
        z = (p ** -0.5) * np.exp(1j * th * math.log(p))
        geom = sum(z ** r for r in range(K + 1))
        rec += w * (1.0 - z) * geom   # no T
    ones = np.ones(len(yn))
    return float(np.linalg.norm(ones - rec.real))


def tail_span_relres(s, yn, primes=PRIMES_GEO, K=K_GEO):
    yn = np.asarray(yn, float)
    s = np.asarray(s, float).ravel()
    th = np.arccos(np.clip(yn, -1.0, 1.0))
    logs = np.array([math.log(p) for p in primes], float)
    nu = logs / float(np.sum(logs))
    T = np.zeros(len(yn), dtype=complex)
    for p, w in zip(primes, nu):
        z = (p ** -0.5) * np.exp(1j * th * math.log(p))
        T += w * z ** (K + 1)
    F = np.column_stack([T.real, T.imag])
    Q, _R = np.linalg.qr(F, mode="reduced")
    rel = float(np.linalg.norm(s - Q @ (Q.T @ s))
                / (np.linalg.norm(s) + 1e-30))
    corr = float(np.corrcoef(s, T.real)[0, 1])
    return rel, corr


def ones_woodbury_Y(A0, Ucd):
    """Woodbury Delta for the source ones-split H = A0+oo^T
    on Y with the two CD columns.  Closed form, no optimiser.
    c_min identity: ||c||^2 = ell^T B^{-1} ell = 1-Delta."""
    A0 = np_sym(A0)
    U = np.asarray(Ucd, float)
    n = A0.shape[0]
    o = np.ones(n)
    o = o / math.sqrt(float(o @ o))
    H = np_sym(A0 + np.outer(o, o))
    eta = float(o @ np.linalg.solve(H, o))
    r = U.T @ np.linalg.solve(H, o)
    Kw = np_sym(np.eye(U.shape[1]) + U.T @ np.linalg.solve(H, U))
    Delta = 1.0 - eta + float(r @ np.linalg.solve(Kw, r))
    nnegH = int(np.sum(np.linalg.eigvalsh(H) < -FLOOR))
    return dict(eta=eta, Delta=Delta, c2=1.0 - Delta,
                cnrm=math.sqrt(max(1.0 - Delta, 0.0)), nnegH=nnegH)


def cut_of(kz, chi=None):
    if chi is None:
        R = PX.build_rung(kz)
        mz = R["mz"]
        cut = FTI.cut_rung(mz["xu"], mz["wu"], mz["yn"], mz["vn"],
                           R["Nw"], R["S"], mz["L"], R["i1"], R["i2"],
                           keep=True)
        row = ES.main_row(kz)
        return cut, row, mz
    q, lpq = chi
    uu, ww, _n, _c = DMF.chi_window_comb(kz, q)
    mzc = DMF.chi_build_measures(kz, uu, ww, 1.0, lpq)
    j1, j2 = PX.pair_select(mzc["yn"])
    cut = FTI.cut_rung(mzc["xu"], mzc["wu"], mzc["yn"], mzc["vn"],
                       mzc["Nw"], mzc["S"], mzc["L"], j1, j2, keep=True)
    row = ES.chi_row(kz, q, lpq, "C")
    return cut, row, mzc


def ones_row(kz, chi=None):
    cut, row, mz = cut_of(kz, chi=chi)
    w = ones_woodbury_Y(cut["A0"], cut["U"])
    sch = float(row["sch"])
    kappa = w["Delta"] / (-sch) if abs(sch) > FLOOR else float("nan")
    w.update(sch=sch, kappa=kappa, nnegA0=int(row["nnegA0"]),
             a=float(row["a"]), b=float(row["b"]),
             ab=float(row["ab"]), ok=bool(row.get("ok")),
             yn=np.asarray(mz["yn"], float), s=None)
    return w, cut, mz


def sm_border_Y(kz, cut):
    """Y-component of the Sherman-Morrison border (r401)."""
    R = PX.build_rung(kz)
    alk = float(V.window_shape(kz)[0])
    dsm = HS.window_data(kz, comb=PB.smooth_comb(alk))
    bp = ABD.border_chain_pack(R["mz"]["xp"], R["mz"]["wp"],
                               R["mz"]["yn"], R["mz"]["vn"],
                               dsm["xs"], dsm["ws"], dsm["ys"], dsm["vs"],
                               R["Nw"])
    a_mu, b_mu, h0_mu = V.mu_chain(R["mz"]["xp"], R["mz"]["wp"], R["Nw"])
    bxa = np.concatenate([np.asarray(dsm["xs"], float),
                          np.asarray(dsm["ys"], float)])
    bwa = np.concatenate([np.asarray(dsm["ws"], float),
                          -np.asarray(dsm["vs"], float)])
    bvec = ABD.bvec_chunked(a_mu, b_mu, h0_mu, bxa, bwa, R["Nw"])
    vt = cut["epsY"] * (R["B"] @ (bvec / math.sqrt(bp["Bw"])))
    return cut["Rm"] @ vt


# ---- legs ----

def part_toys():
    section("S1  SATZ -- EULER TAIL / DISK / WOODBURY-KAPPA / CAUCHY")
    et = euler_tail_Q()
    check("G01-euler-tail-Q",
          et["ok"] and et["lhs"] == Fr(728, 729),
          "z=1/3 K=5: 1-z^{K+1}=(1-z)Sum z^r EXACT lhs=%s" % et["lhs"])
    check("G02-omit-tail-Q",
          et["omit_neq"] and et["rem"] == Fr(1, 3) ** 6,
          "omit T: remainder z^{K+1}=%s != 0" % et["rem"])
    dp = disk_parseval_Q()
    check("G03-disk-parseval-Q",
          dp["ok"] and dp["rhs"] == Fr(127, 128)
          and (Fr(1) - dp["rhs"]) == Fr(1, 128),
          "q=1/2 K=6: ||c||^2=127/128, 1-||c||^2=1/128 EXACT")
    kq = kappa_closed_Q()
    check("G04-woodbury-kappa-Q",
          kq["equal"] and kq["Delta"] == Fr(7, 36)
          and kq["kappa"] == Fr(-2, 27),
          "Delta=%s = kappa*(-sch) kappa=%s sch=%s EXACT"
          % (kq["Delta"], kq["kappa"], kq["sch"]))
    detC, pdC = cauchy_gram_Q()
    check("G05-cauchy-gram-Q",
          pdC and detC == Fr(1, 72),
          "2-pt Cauchy Gram det=%s > 0 (F_Gamma block PD over Q)"
          % detC)
    Tm = MH.mixed_update_toy()
    check("G06-wrong-J-mixed",
          Tm["dev"] == 0 and Tm["dev_w"] > 0,
          "mixed form residual 0; wrong-sign J residual %s != 0"
          % Tm["dev_w"])


def part_w9():
    section("S2  LEG 1/2/3 -- w9 GEOMETRIC LIFT + WOODBURY + BORDER")
    w, cut, mz = ones_row(9)
    yn = np.asarray(mz["yn"], float)
    geo = geometric_ones(yn)
    check("G10-E1-ones-residual",
          geo["res"] <= GEO_RES_HI and geo["res_im"] <= 1e-12,
          "||1 - Sum nu(E+T)||=%.3e (explicit c, no optimiser)"
          % geo["res"])
    omit = omit_tail_residual(yn)
    check("G11-omit-tail-kills-E1",
          omit > 0.02,
          "omit T residual %.3f != 0 (tail load-bearing for E1)"
          % omit)
    A0 = np.asarray(cut["A0"], float)
    ev, VV = np.linalg.eigh(A0)
    vneg = VV[:, 0]
    ones = np.ones(len(yn))
    ones = ones / math.sqrt(float(ones @ ones))
    c_ones = abs(float(vneg @ ones))
    Qg, _ = np.linalg.qr(geo["V"], mode="reduced")
    rel_v = float(np.linalg.norm(vneg - Qg @ (Qg.T @ vneg)))
    check("G12-ones-not-defect",
          c_ones <= COS_ONES_HI and rel_v >= VNEG_GEO_LO,
          "|cos|(v_-,1)=%.4f; v_- vs geometric V relres=%.3f "
          "(A0-defect lift OPEN / not this c)"
          % (c_ones, rel_v))
    # r404 cosine control (same constructors)
    check("G12b-r404-cosine-gate",
          G404.SPEC_SHA.startswith(G404_SHA_PREFIX),
          "r404 SPEC %s (ones-mode is not the null mode)"
          % G404.SPEC_SHA[:8])
    sY = sm_border_Y(9, cut)
    rel_t, corr_t = tail_span_relres(sY, yn)
    check("G13-border-ne-tail",
          rel_t >= TAIL_RELRES_LO and abs(corr_t) < 0.3,
          "SM-border vs aggregated z^{K+1}: relres=%.3f corr=%.3f "
          "(identification REFUTED)" % (rel_t, corr_t))
    check("G14-w9-sch-pin",
          abs(w["sch"] / W9_SCH - 1.0) <= 0.02,
          "sch=%.6f (r401 living chart)" % w["sch"])
    check("G15-E2-ones-woodbury",
          w["Delta"] > 0 and 0.0 < w["c2"] < 1.0
          and abs(w["Delta"] / W9_DLT - 1.0) <= REL
          and abs(w["c2"] / W9_C2 - 1.0) <= REL,
          "Delta=%.6e c2=%.6f ||c||=%.4f (ones-split, no optimiser)"
          % (w["Delta"], w["c2"], w["cnrm"]))
    check("G16-E3-kappa-sign-living",
          w["kappa"] > 0
          and abs(w["kappa"] / W9_KAPPA - 1.0) <= REL,
          "kappa=Delta/(-sch)=%.5f > 0 on MAIN (not a function "
          "of (a,b) alone)" % w["kappa"])
    check("G17-sumform-not-Delta",
          geo["sumform"] > 0.05 and geo["sumform"] > 20 * w["Delta"],
          "disk sumform=%.4f vs Woodbury Delta=%.3e -- E3 as "
          "'sum = kappa(-sch)' scale-REFUTED" % (
              geo["sumform"], w["Delta"]))
    return w, geo, sY, rel_v


def part_kills():
    section("S3  LEG 4 -- KILLS / WORLDS (SMOKE)")
    mz_s = HM.scramble_mz()
    j1, j2 = PX.pair_select(mz_s["yn"])
    oS = FTI.cut_rung(mz_s["xu"], mz_s["wu"], mz_s["yn"], mz_s["vn"],
                      mz_s["Nw"], mz_s["S"], mz_s["L"], j1, j2)
    check("G20-scramble-P1-breaks",
          oS["nneg"] == SCR_NNEG,
          "scramble nnegA0=%d (factorisation (G) already dead)"
          % oS["nneg"])
    mz_t = HM.two_period_mz(21, 2.0 / 3.0)
    j1, j2 = PX.pair_select(mz_t["yn"])
    oT = FTI.cut_rung(mz_t["xu"], mz_t["wu"], mz_t["yn"], mz_t["vn"],
                      mz_t["Nw"], mz_t["S"], mz_t["L"], j1, j2)
    check("G21-two-period",
          oT["nneg"] >= TP21_NNEG,
          "two-period nnegA0=%d" % oT["nneg"])
    mz = V.build_measures(9)
    mz_p = P1.reweight(mz, "permute", 1)
    pp = P1.spec_of(mz_p, need_ref=False)
    check("G22-perm-breaks-G",
          pp["nneg"] >= PERM_NNEG_LO,
          "weight-perm nneg=%d (r403: (G) breaks before the lift)"
          % pp["nneg"])
    # jitter of Y does NOT break the tail identity
    yn = np.asarray(mz["yn"], float)
    geo0 = geometric_ones(yn)
    yn_j = yn + 1e-4 * np.sin(np.arange(len(yn)))
    geo_j = geometric_ones(yn_j)
    check("G23-jitter-does-not-kill-tail",
          geo0["res"] <= GEO_RES_HI and geo_j["res"] <= GEO_RES_HI,
          "Euler tail is an identity in z: jitter residual %.3e "
          "(the jitter kill of the GRAM sits on r403/r404)"
          % geo_j["res"])
    wd, _c, _m = ones_row(15, chi=(DMF.Q_CHI3, DMF.LPQ3))
    check("G24-dead-chi-no-overflow",
          wd["sch"] > 0 and wd["kappa"] < 0
          and 0.0 < wd["c2"] < 1.0
          and abs(wd["Delta"] / D15_DLT - 1.0) <= 0.1
          and abs(wd["kappa"] / D15_KAPPA - 1.0) <= 0.1,
          "dead chi3-15 sch=%+.4f Delta=%.4e c2=%.5f kappa=%.3f "
          "(||c||<1 -- overflow REFUTED; death is kappa<0)"
          % (wd["sch"], wd["Delta"], wd["c2"], wd["kappa"]))
    wl, _c, _m = ones_row(9, chi=(DMF.Q_CHI3, DMF.LPQ3))
    check("G25-live-chi-contractive",
          wl["sch"] < 0 and wl["kappa"] > 0 and wl["c2"] < 1.0,
          "live chi3-9 sch=%.4f c2=%.5f kappa=%.3f"
          % (wl["sch"], wl["c2"], wl["kappa"]))
    return wd, wl


def part_full():
    section("S4  LEG 2/4 -- CORE-42 + CHI3 CENSUS")
    core = list(V.admissible_indices())
    n_dlt = n_k = n_c = 0
    dlts, ks, c2s = [], [], []
    for kz in core:
        w, _c, _m = ones_row(kz)
        dlts.append(w["Delta"])
        ks.append(w["kappa"])
        c2s.append(w["c2"])
        if w["Delta"] > 0:
            n_dlt += 1
        if w["kappa"] > 0:
            n_k += 1
        if 0.0 < w["c2"] < 1.0:
            n_c += 1
    check("G40-core42-Delta-pos",
          n_dlt == CORE_N and min(dlts) > 1e-8,
          "MAIN ones-split Delta>0 %d/%d  range [%.3e, %.3e]"
          % (n_dlt, CORE_N, min(dlts), max(dlts)))
    check("G41-core42-kappa-pos",
          n_k == CORE_N,
          "MAIN kappa>0 %d/%d  med=%.3e (living chart sch<0)"
          % (n_k, CORE_N, float(np.median(ks))))
    check("G42-core42-contractive",
          n_c == CORE_N and max(c2s) < 1.0,
          "MAIN 0<c2<1 %d/%d  c2 in [%.5f, %.5f] -- ||c||<1"
          % (n_c, CORE_N, min(c2s), max(c2s)))
    live_ok = dead_ok = dead_ov = 0
    for kz in core:
        w, _c, _m = ones_row(kz, chi=(DMF.Q_CHI3, DMF.LPQ3))
        if kz in ES.DEAD_CHI3:
            if w["sch"] > 0 and w["kappa"] < 0 and w["c2"] < 1.0:
                dead_ok += 1
            if w["c2"] > 1.0:
                dead_ov += 1
        else:
            if w["sch"] < 0 and w["kappa"] > 0 and w["c2"] < 1.0:
                live_ok += 1
    check("G43-chi3-live",
          live_ok == CHI3_LIVE_N,
          "live chi3 %d/%d kappa>0 c2<1" % (live_ok, CHI3_LIVE_N))
    check("G44-chi3-dead-no-overflow",
          dead_ok == CHI3_DEAD_N and dead_ov == 0,
          "dead chi3 %d/%d sch>0 kappa<0 AND c2<1 "
          "(overflow 0/%d -- death is not ||c||>1)"
          % (dead_ok, CHI3_DEAD_N, CHI3_DEAD_N))


def main():
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke

    print("=" * 78)
    print("edge_contractive_lift_probe -- "
          "PRIME.LDAGGER.EDGE_CONTRACTIVE_LIFT.01 (round 405)")
    print("SPEC_SHA %s   (ES %s / MH %s / G404 %s)"
          % (SPEC_SHA[:16], ES.SPEC_SHA[:16], MH.SPEC_SHA[:16],
             G404.SPEC_SHA[:16]))
    print("mode: %s" % ("SMOKE" if smoke else
                         "FULL (core-42 + chi3-42)"))
    print("=" * 78)

    section("S0  FIREWALL + IMPORT INTEGRITY")
    okf, det = firewall_audit()
    check("G00-firewall", okf, det)
    sha_ok = (ES.SPEC_SHA.startswith(ES_SHA_PREFIX)
              and MH.SPEC_SHA.startswith(MH_SHA_PREFIX)
              and FTI.SPEC_SHA.startswith(FTI_SHA_PREFIX)
              and G404.SPEC_SHA.startswith(G404_SHA_PREFIX)
              and P1.SPEC_SHA.startswith(P1_SHA_PREFIX))
    check("G00b-import-sha", sha_ok,
          "ES %s / MH %s / FTI %s / G404 %s / P1 %s"
          % (ES.SPEC_SHA[:8], MH.SPEC_SHA[:8], FTI.SPEC_SHA[:8],
             G404.SPEC_SHA[:8], P1.SPEC_SHA[:8]))
    ag = antigate_fragment_audit()
    check("G00c-no-fit", not ag,
          "no fit primitives" if not ag else "; ".join(ag))

    part_toys()
    part_w9()
    part_kills()
    if not smoke:
        part_full()
    else:
        section("S4  FULL CENSUS skipped (--smoke)")

    section("S5  VERDICT")
    prev_ok = all(ok for _n, ok in CHECKS)
    check("G50-verdict-EDGE_LIFT_PARTIAL",
          prev_ok,
          "EDGE_LIFT_PARTIAL: Euler/disk/Woodbury SATZ; "
          "ones-lift residual 0; border=tail REFUTED; "
          "dead overflow REFUTED; A0-defect c OPEN")

    n_fail = sum(1 for _n, ok in CHECKS if not ok)
    n_ok = len(CHECKS) - n_fail
    verd = "EDGE_LIFT_PARTIAL"
    print("\nRESULT: %d/%d gates PASS   SPEC_SHA %s   (%.1fs)  %s" % (
        n_ok, len(CHECKS), SPEC_SHA[:16], time.time() - T0, verd))
    if n_fail == 0:
        print("EDGE LIFT %sVERIFIED" % ("SMOKE " if smoke else ""))
        return 0
    print("EDGE LIFT FAILED %d" % n_fail)
    return 1


if __name__ == "__main__":
    sys.exit(main())
