#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""one_defect_gram_probe -- PRIME.LDAGGER.SOURCE_ONE_DEFECT_GRAM.01
(round 404): is there a source-explicit one-defect factor
Q^T A_0 Q = F F^T - ell ell^T, with F built from Lambda(p^r),
log(p^r), Fold, Tent, Digamma and the explicit Bernstein-Szego
reference BEFORE evaluation, and with the identity breaking
exactly under Lambda-permutation and position jitter?

Three classes (reviewer, binding).  Only class 3 counts.
  1  CHOLESKY_TAUTOLOGY -- F from Cholesky / sqrt / eigendecomp
     of M or A_0, or a post-hoc solve X X^T = M.
  2  REFERENCE_COORDINATE_ONLY -- Q from the numerical projector
     of A_ref (or a full Chebyshev-U basis of Y that tautologically
     contains every subspace); the factor of M is still class 1.
  3  SOURCE_GRAM_EXACT -- F closed-form from (p,r) / Digamma /
     Fold / Tent / Uvarov / explicit BS modes; residual 0 on
     MAIN; explodes under Lambda-perm and position jitter.

THE IDENTITY (Satz G).  A_0 = H - ell ell^T with source-pure
H = F F^T succeeds 0 and source-pure ell implies ind_-(A_0)<=1
by congruence.  Working form: Q^T A_0 Q + ell ell^T = F F^T.

LEGS (reviewer 11).
  0  Analytic Y_k, Y^T Y = I, range(Y) = negative space of the
     explicit BS dual, from Fourier / Chebyshev-U modes of the
     reference (numerical projector = control).
  2  Euler block F_Lam from (p,r): amp = sqrt(2 log p) p^{-r/4},
     phase r * theta_{p,j}; B_Lam = F F^T vs the prime block
     of the perturbation.  Fold/Tent as outer linear T.
  3  Digamma block F_Gamma from Cauchy features (m+z_j)^{-1};
     Loewner identity on the function, then: is the arch block
     of A_0 that Loewner Gram?
  4  Uvarov: cross terms as off-diagonal blocks of ONE factor;
     does this explain only-Gram leaves 13?
  5  One null mode ell = sqrt(sum_{p<=e^{2a}} log p) Q^T 1
     plus arch normalisation.  Target Q^T A_0 Q + ell ell^T
     = F F^T exactly.
  Mutants (mandatory): Lambda-perm, position jitter,
     Lambda(p^r) -> log(p^r), Digamma 1/4 -> 3/4, omit null,
     omit Uvarov.

CALIBRATION DISCLOSURE.  Residuals, principal angles, defect
seat, Loewner nsum, Euler alignment first measured in /tmp
(r404_cal.py, r404_cal2.py, r404_cal3.py) on the same
constructors, 2026-08-29.  Frozen floors below are that
measurement, sealed as gates -- not a search over 1/2.
No two-commit pre-blind freeze: pins disclosed.  Builder
fallback NOT taken: full wall < 5 s (bar 120 s).

FROZEN FROM /tmp (live re-gated, not fitted):
  * SATZ, function-level: Chebyshev T_2 T_1 = (T_3+T_1)/2
    over Q.  Loewner
    (psi(z)-conj(psi(w)))/(z-conj(w)) = nsum_m 1/((m+z)(m+conj w))
    to 4.6e-41 at dps 40.  Cauchy kernel over Q:
    1/((m+z)(m+w)) = (1/(z-w))(1/(m+w)-1/(m+z)).
  * SATZ, construction-linear: folded weights are linear in
    lags, ||w-(wP+wA)||_2 / ||w|| = 3.5e-16 on FRAME-A.
  * SATZ, compression: Q^T A_0 Q is already PD on FRAME-A
    (nneg=0, lam_min=5.227e-3).  The one negative of A_0 is
    NOT a null mode of the ref-negative compression.
  * LEG 0 NOT analytic: consecutive Chebyshev-U k-blocks of
    size 49 on Y have max principal angle ~90 deg vs Vn;
    greedy energy selection needs all 104 modes (the whole
    of Y) to cover Vn.  The numerical projector of A_ref
    remains the only identification of the 49-space.
  * LEG 2 NOT exact: Euler-Gram vs M residual ~209 (delta
    and logn phase conventions coincide); LS scale alignment
    0.767, residual 0.642 -- a correlation, not an identity.
    Tent-Gram vs B residual 1.0.  Linear T recovers weights,
    not the CD Gram.
  * LEG 3 NOT the arch block: Loewner/Cauchy-Gram vs A_0
    residual ~207; alignment of Cauchy-Gram with M is 0.098.
  * LEG 4: only-Gram nneg=13 (r403 pin).  ||B_cross||/||B||
    = 0.617, numerical rank 104.  Stacked tent/Euler YY
    blocks do not equal B (residual 1 / 266).
  * LEG 5 NOT the ones-mode: |cos|(v_-, 1)=0.007; |cos|(v_-,
    Vn)=0.761 (mixed with the complement 0.648); |cos|(Q^T 1,
    v_neg of Q^T A_0 Q)=0.069.  Prescribed ell does not
    complete a source Gram.
  * CLASS 1 control: Cholesky of M is exact (rest 2e-16) on
    MAIN and does not exist on a mask-preserving permute
    (M not PD) -- tautology of MAIN-PD, not a source law.
  * Mutants of the Euler/Cauchy candidate stay O(1) residual
    (the identity never held, so nothing "explodes from 0").
    Lambda-perm residual 190 vs MAIN 209 (ratio 0.91).

AUSGANG CHOLESKY_TAUTOLOGY / SOURCE_GRAM_NOT_EXACT.
Class 3 is not reached in one honest round.  The stop rule
fires: do not iterate a Cholesky factor.  SATZ: Loewner
identity; Chebyshev addition; lag-linearity of the fold;
Q^T A_0 Q PD on FRAME-A; Cholesky of a PD Gram is exact
(named tautology).  CENSUS: Euler/Digamma/Uvarov residuals
O(1); analytic Fourier subset does not recover Vn; the one
defect of A_0 is mixed, not Q^T 1.  No RH claim.

MACHINERY: r403 P.gram_of / rebuild / reweight, r400
H.r_of / dual_fejer_R / nneg_sym, r390 GEP.fejer_w, r356
BDH.dual_weights, r226 V.build_measures / prime_lags /
arch_lags / spectral_density.

NO RH CLAIM.  Finite identities, one named class audit.
Research documentation, not a theorem of RH.
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

import bulk_one_defect_probe as H  # noqa: E402
import borodin_dual_hole_probe as BDH  # noqa: E402
import g_eps_mu_probe as GEP  # noqa: E402
import p1_construction_probe as P  # noqa: E402
import verify_lstar_instance as V  # noqa: E402

H_SHA_PREFIX = "91a4afa2"
BDH_SHA_PREFIX = "36141c0a"
GEP_SHA_PREFIX = "c2c9c3f2"
P_SHA_PREFIX = "ba6817f5"

W9_NNEG, W9_NNEG_REF = 1, 49
W9_ONLYGRAM = 13
W9_NPOS_M = 49
QMIN_LO = 1.0e-4
COS_VN_LO, COS_VN_HI = 0.65, 0.85
COS_ONES_HI = 0.05
COS_ELL_HI = 0.25
REL_EULER_LO = 20.0
REL_LOEWNER_LO = 20.0
ALIGN_EULER_LO, ALIGN_EULER_HI = 0.50, 0.90
ALIGN_CAUCHY_HI = 0.30
MAXANG_LO = 45.0
GREEDY_LO = 80
CHOL_REST_HI = 1.0e-12
FOLD_LIN_HI = 1.0e-12
LOEWNER_MP_HI = 1.0e-20
CROSS_SHARE_LO = 0.40
PERM_NNEG_M_LO = 3
MUT_REL_LO = 10.0

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
    return (not bad), ("NO zero/prime oracles; dual CD Gram / "
                       "Euler/Digamma/Fold features / class audit"
                       if not bad else "; ".join(bad))


def class_audit_ast():
    """Cholesky / sqrtm of M or A0 may appear ONLY inside
    cholesky_tautology_control (named class-1 control)."""
    src = open(os.path.abspath(__file__), "r", encoding="utf-8").read()
    tree = ast.parse(src)
    bad = []
    for fn in tree.body:
        if not isinstance(fn, ast.FunctionDef):
            continue
        if fn.name == "cholesky_tautology_control":
            continue
        for node in ast.walk(fn):
            if isinstance(node, ast.Attribute) and node.attr in (
                    "cholesky", "sqrtm", "eighc"):
                bad.append("%s.%s@%d" % (fn.name, node.attr, node.lineno))
    return (not bad), ("source F is not a Cholesky/sqrt of M/A0"
                       if not bad else "; ".join(bad))


def relres(A, B):
    A = np.asarray(A, float)
    B = np.asarray(B, float)
    return float(np.linalg.norm(A - B)) / (float(np.linalg.norm(B)) + 1e-30)


def prin_maxang_deg(A, B):
    Qa, _ = np.linalg.qr(np.asarray(A, float), mode="reduced")
    Qb, _ = np.linalg.qr(np.asarray(B, float), mode="reduced")
    s = np.clip(np.linalg.svd(Qa.T @ Qb, compute_uv=False), 0.0, 1.0)
    return float(math.degrees(math.acos(float(s.min()))))


def pack_ref(mz):
    R, _ = H.r_of(mz)
    Rr = H.dual_fejer_R(mz)
    B = R - Rr
    n = R.shape[0]
    A0 = R - 0.5 * np.eye(n)
    Aref = Rr - 0.5 * np.eye(n)
    evA, VA = np.linalg.eigh(Aref)
    mneg = evA < -1e-12
    Vn = VA[:, mneg]
    M = 0.5 * (Vn.T @ B @ Vn + (Vn.T @ B @ Vn).T)
    yn = np.asarray(mz["yn"], float)
    ev0, V0 = np.linalg.eigh(A0)
    return dict(
        R=R, Rr=Rr, B=B, A0=A0, Aref=Aref, Vn=Vn, M=M, yn=yn,
        n=n, nneg=int(np.sum(ev0 < -1e-12)),
        nneg_ref=int(np.sum(mneg)),
        vneg=V0[:, 0], evM=np.linalg.eigvalsh(M),
        QA0=Vn.T @ A0 @ Vn,
    )


def chebU_on_Y(yn, k0, k1):
    yn = np.asarray(yn, float)
    phi = np.arccos(np.clip(yn, -1.0, 1.0))
    s = np.sin(phi)
    s = np.where(np.abs(s) < 1e-14, 1e-14, s)
    ks = np.arange(k0, k1)
    return np.sin(phi[:, None] * ks[None, :]) / s[:, None]


def euler_F(mz, yn, lam=None, u_pos=None, amp="logp"):
    """Closed-form Euler features on Y.  No eigendecomp.
    amp='logp': sqrt(2 Lambda) n^{-1/4}; amp='logn': sqrt(2 u) n^{-1/4}."""
    ka = int(mz["ka"])
    D = float(mz["D"])
    phi = np.arccos(np.clip(yn, -1.0, 1.0))
    lam = V.LAM if lam is None else lam
    u_pos = V.U if u_pos is None else u_pos
    cols = []
    for n, u in zip(V.PP[:ka], u_pos[:ka]):
        n = int(n)
        lp = float(lam[n]) if n < len(lam) else float(lam[int(n)])
        if amp == "logp":
            a = lp
        else:
            a = float(u)
        if a <= 0.0:
            continue
        amp_ = math.sqrt(2.0 * a) * math.exp(-0.25 * float(u))
        ang = (float(u) / D) * phi
        cols.append(amp_ * np.cos(ang))
        cols.append(amp_ * np.sin(ang))
    if not cols:
        return np.zeros((len(yn), 1))
    return np.column_stack(cols)


def cauchy_F(yn, shift=0.25, nterm=80):
    phi = np.arccos(np.clip(yn, -1.0, 1.0))
    z = shift + 0.5j * phi
    cols = []
    for m in range(nterm):
        cols.append(np.real(1.0 / (m + z)))
        cols.append(np.imag(1.0 / (m + z)))
    return np.column_stack(cols)


def weights_from_c(kz, c):
    d = V.spectral_density(c)
    _a, M, L, _Nw, _D = V.window_shape(kz)
    jj = np.arange(1, L // 2 + 1)
    theta = 2.0 * math.pi * jj / L
    x = np.cos(theta)
    wt = (2.0 / L) * (1.0 - np.cos(theta)) * d[jj]
    wt[-1] *= 0.5
    keep = np.abs(wt) > 1e-300
    x, wt = x[keep], wt[keep]
    o = np.argsort(x)
    return x[o], wt[o]


def align_fro(A, B):
    A = np.asarray(A, float).ravel()
    B = np.asarray(B, float).ravel()
    num = float(np.dot(A, B))
    den = math.sqrt(float(np.dot(A, A) * np.dot(B, B))) + 1e-30
    return num / den


def cholesky_tautology_control(M):
    """CLASS 1 control -- not a source factor."""
    L = np.linalg.cholesky(0.5 * (M + M.T))
    return relres(L @ L.T, M)


def part_satz():
    section("S1  SATZ -- ADDITION / LOEWNER / FOLD / CAUCHY-Q")
    x = Fr(3, 7)
    T0, T1 = Fr(1), x
    T2 = 2 * x * T1 - T0
    T3 = 2 * x * T2 - T1
    check("G01-chebyshev-addition-Q",
          2 * T2 * T1 == T3 + T1,
          "T2 T1 = (T3+T1)/2 over Q, T2=%s" % T2)

    z, w = Fr(1, 4), Fr(3, 4)
    m = Fr(2)
    lhs = 1 / ((m + z) * (m + w))
    rhs = (1 / (z - w)) * (1 / (m + w) - 1 / (m + z))
    check("G02-cauchy-kernel-Q",
          lhs == rhs,
          "1/((m+z)(m+w)) telescopes over Q")

    import mpmath as mp
    mp.mp.dps = 40
    zz = mp.mpc("1/4", "7/10")
    ww = mp.mpc("1/4", "-3/10")
    lhs = ((mp.digamma(zz) - mp.conj(mp.digamma(ww)))
           / (zz - mp.conj(ww)))
    rhs = mp.nsum(lambda k: 1 / ((k + zz) * (k + mp.conj(ww))),
                  [0, mp.inf])
    err = float(abs(lhs - rhs))
    check("G03-loewner-psi-nsum",
          err <= LOEWNER_MP_HI,
          "|psi-Loewner|=%.3e (dps 40)" % err)

    mz = V.build_measures(9)
    cP, _ka = V.prime_lags(mz["alpha"], mz["M"], mz["D"])
    cA = V.arch_lags(mz["M"], mz["D"])
    _xP, wP = weights_from_c(9, cP)
    _xA, wA = weights_from_c(9, cA)
    _xF, wF = weights_from_c(9, cP + cA)
    lin = float(np.linalg.norm(wF - (wP + wA))) / (
        float(np.linalg.norm(wF)) + 1e-30)
    check("G04-fold-linear-in-lags",
          lin <= FOLD_LIN_HI,
          "||w-(wP+wA)||/||w||=%.3e" % lin)
    return mz


def part_w9(mz):
    section("S2  LEG 0/2/3/4/5 -- FRAME-A CLASS AUDIT")
    pk = pack_ref(mz)
    g = P.gram_of(mz)
    Vn, M, B, A0, yn = pk["Vn"], pk["M"], pk["B"], pk["A0"], pk["yn"]
    vneg = pk["vneg"]
    QA0 = pk["QA0"]
    evQ = np.linalg.eigvalsh(QA0)
    check("G10-w9-inertia",
          pk["nneg"] == W9_NNEG and pk["nneg_ref"] == W9_NNEG_REF
          and g["nneg_M"] == 0 and g["npos_M"] == W9_NPOS_M,
          "nneg=%d nneg_ref=%d nneg_M=%d npos_M=%d"
          % (pk["nneg"], pk["nneg_ref"], g["nneg_M"], g["npos_M"]))
    check("G11-QA0-already-PD",
          int(np.sum(evQ < -1e-12)) == 0 and float(evQ[0]) >= QMIN_LO,
          "Q^T A0 Q nneg=%d lam_min=%.4e (defect NOT in ref-neg)"
          % (int(np.sum(evQ < -1e-12)), float(evQ[0])))

    nY = pk["n"]
    nneg_ref = pk["nneg_ref"]
    angs = []
    for lo, hi in ((1, 1 + nneg_ref),
                   (nY - nneg_ref + 1, nY + 1),
                   (max(1, int(mz["Nw"]) - 3 - nneg_ref + 1),
                    int(mz["Nw"]) - 3 + 1)):
        hi = min(hi, nY + 1)
        lo = max(1, lo)
        if hi - lo < nneg_ref:
            continue
        Ublk = chebU_on_Y(yn, lo, lo + nneg_ref)
        angs.append(prin_maxang_deg(Ublk, Vn))
    Uall = chebU_on_Y(yn, 1, nY + 1)
    energy = np.sum((Uall.T @ Vn) ** 2, axis=1)
    order = np.argsort(energy)[::-1]
    greedy = nY
    for m in range(nneg_ref, nY + 1):
        if prin_maxang_deg(Uall[:, order[:m]], Vn) < 1.0:
            greedy = m
            break
    check("G12-leg0-no-fourier-subset",
          min(angs) >= MAXANG_LO and greedy >= GREEDY_LO,
          "consec 49-blocks maxang=%s deg; greedy cover=%d (need 49)"
          % ([round(a, 1) for a in angs], greedy))

    Fe = euler_F(mz, yn)
    Ge = Vn.T @ (Fe @ Fe.T) @ Vn
    rE = relres(Ge, M)
    aE = align_fro(Ge, M)
    check("G13-leg2-euler-not-exact",
          rE >= REL_EULER_LO
          and ALIGN_EULER_LO <= aE <= ALIGN_EULER_HI,
          "Euler vs M rel=%.3f align=%.3f (correlation, not identity)"
          % (rE, aE))

    Fg = cauchy_F(yn, 0.25, 80)
    Gg = Vn.T @ (Fg @ Fg.T) @ Vn
    rL = relres(Fg @ Fg.T, A0)
    aC = align_fro(Gg, M)
    check("G14-leg3-loewner-not-arch-block",
          rL >= REL_LOEWNER_LO and aC <= ALIGN_CAUCHY_HI,
          "Cauchy-Gram vs A0 rel=%.3f; vs M align=%.3f"
          % (rL, aC))

    Pneg = Vn @ Vn.T
    Bmm = Pneg @ B @ Pneg
    Bcross = B - Bmm
    nB = float(np.linalg.norm(B))
    share = float(np.linalg.norm(Bcross)) / (nB + 1e-30)
    check("G15-leg4-onlyGram-cross",
          g["nneg_gram"] == W9_ONLYGRAM and share >= CROSS_SHARE_LO,
          "only-Gram nneg=%d; ||B_cross||/||B||=%.3f (YY-block of a "
          "source factor does not finish the lift)"
          % (g["nneg_gram"], share))

    ones = np.ones(nY)
    cos1 = abs(float(vneg @ ones)) / (
        float(np.linalg.norm(vneg) * np.linalg.norm(ones)) + 1e-30)
    cosVn = float(np.linalg.norm(Vn.T @ vneg))
    ka = int(mz["ka"])
    sumlog = float(np.sum(V.LAM[V.PP[:ka]]))
    ell = math.sqrt(max(sumlog, 0.0)) * (Vn.T @ ones)
    evQvec = np.linalg.eigh(QA0)
    vQ = evQvec[1][:, 0]
    nrm_ell = float(np.linalg.norm(ell)) + 1e-30
    cos_ell = abs(float(ell @ vQ)) / nrm_ell
    check("G16-leg5-null-not-ones",
          cos1 <= COS_ONES_HI
          and COS_VN_LO <= cosVn <= COS_VN_HI
          and cos_ell <= COS_ELL_HI,
          "|cos|(v-,1)=%.4f |cos|(v-,Vn)=%.3f |cos|(Q^T 1, vQ)=%.3f"
          % (cos1, cosVn, cos_ell))
    return dict(pk=pk, g=g, rE=rE, aE=aE, rL=rL, greedy=greedy,
                Fe=Fe, Ge=Ge)


def part_mutants(mz, w9):
    section("S3  MUTANTS + CLASS-1 CONTROL")
    pk = w9["pk"]
    Vn, M, yn = pk["Vn"], pk["M"], pk["yn"]
    rest = cholesky_tautology_control(M)
    check("G20-cholesky-tautology-MAIN",
          rest <= CHOL_REST_HI,
          "||LL^T-M||/||M||=%.3e  (CLASS 1: always exact when M PD)"
          % rest)

    mzP = P.reweight(mz, "permute", 1000)
    gP = P.gram_of(mzP)
    check("G21-cholesky-not-a-source-law",
          gP["nneg_M"] >= PERM_NNEG_M_LO,
          "permute nneg_M=%d (M not PD; Cholesky of MAIN is not "
          "the von Mangoldt identity)" % gP["nneg_M"])

    rng = np.random.default_rng(404)
    ka = int(mz["ka"])
    lam_p = V.LAM.copy()
    pp = np.asarray(V.PP[:ka], int)
    lam_p[pp] = rng.permutation(lam_p[pp])
    Fp = euler_F(mz, yn, lam=lam_p)
    rP = relres(Vn.T @ (Fp @ Fp.T) @ Vn, M)
    u_j = np.asarray(V.U[:ka], float).copy()
    u_full = V.U.copy()
    u_full[:ka] = u_j * (1.0 + 1.0e-3 * rng.normal(0.0, 1.0, size=ka))
    Fj = euler_F(mz, yn, u_pos=u_full)
    rJ = relres(Vn.T @ (Fj @ Fj.T) @ Vn, M)
    Fn = euler_F(mz, yn, amp="logn")
    rN = relres(Vn.T @ (Fn @ Fn.T) @ Vn, M)
    Fg34 = cauchy_F(yn, 0.75, 80)
    r34 = relres(Vn.T @ (Fg34 @ Fg34.T) @ Vn, M)
    r14 = relres(Vn.T @ (cauchy_F(yn, 0.25, 80) @ cauchy_F(yn, 0.25, 80).T)
                 @ Vn, M)
    check("G22-mutants-stay-O1",
          rP >= MUT_REL_LO and rJ >= MUT_REL_LO
          and rN >= MUT_REL_LO and r34 >= MUT_REL_LO,
          "Lambda-perm rel=%.1f jitter rel=%.1f logn-amp rel=%.1f "
          "digamma-3/4 rel=%.1f (MAIN Euler %.1f, Cauchy-1/4 %.1f); "
          "no identity to break"
          % (rP, rJ, rN, r34, w9["rE"], r14))
    check("G23-omit-null-uvarov-vacuous",
          w9["rE"] >= REL_EULER_LO,
          "omitting a null mode / Uvarov block cannot break an "
          "identity that is already residual %.1f" % w9["rE"])
    return dict(rP=rP, rJ=rJ, rN=rN, r34=r34, chol=rest)


def part_small():
    section("S4  SMALL WINDOW kz=3")
    mz3 = V.build_measures(3)
    pk3 = pack_ref(mz3)
    Fe = euler_F(mz3, pk3["yn"])
    rE = relres(pk3["Vn"].T @ (Fe @ Fe.T) @ pk3["Vn"], pk3["M"])
    Ublk = chebU_on_Y(pk3["yn"], 1, 1 + pk3["nneg_ref"])
    ang = prin_maxang_deg(Ublk, pk3["Vn"])
    check("G40-kz3-euler-not-exact",
          rE >= 1.0,
          "kz3 nY=%d nneg_ref=%d Euler vs M rel=%.3f"
          % (pk3["n"], pk3["nneg_ref"], rE))
    check("G41-kz3-leg0-no-subset",
          ang >= MAXANG_LO,
          "kz3 first-%d U-modes maxang=%.1f deg"
          % (pk3["nneg_ref"], ang))
    return dict(rE=rE, ang=ang, nneg_ref=pk3["nneg_ref"])


def main():
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke

    print("=" * 78)
    print("one_defect_gram_probe -- "
          "PRIME.LDAGGER.SOURCE_ONE_DEFECT_GRAM.01 (round 404)")
    print("SPEC_SHA %s   (H %s / BDH %s / GEP %s / P %s)"
          % (SPEC_SHA[:16], H.SPEC_SHA[:16], BDH.SPEC_SHA[:16],
             GEP.SPEC_SHA[:16], P.SPEC_SHA[:16]))
    print("mode: %s" % ("SMOKE" if smoke else "FULL (kz3 + mutant table)"))
    print("=" * 78)

    section("S0  FIREWALL + CLASS-AST + IMPORT INTEGRITY")
    okf, det = firewall_audit()
    check("G00-firewall", okf, det)
    okc, detc = class_audit_ast()
    check("G00b-class-ast", okc, detc)
    sha_ok = (H.SPEC_SHA.startswith(H_SHA_PREFIX)
              and BDH.SPEC_SHA.startswith(BDH_SHA_PREFIX)
              and GEP.SPEC_SHA.startswith(GEP_SHA_PREFIX)
              and P.SPEC_SHA.startswith(P_SHA_PREFIX))
    check("G00c-import-sha", sha_ok,
          "H %s / BDH %s / GEP %s / P %s"
          % (H.SPEC_SHA[:8], BDH.SPEC_SHA[:8],
             GEP.SPEC_SHA[:8], P.SPEC_SHA[:8]))

    mz = part_satz()
    w9 = part_w9(mz)
    mut = part_mutants(mz, w9)
    if not smoke:
        part_small()
    else:
        section("S4  kz3 skipped (--smoke)")

    section("S5  VERDICT")
    prev_ok = all(ok for _n, ok in CHECKS)
    check("G50-verdict-CLASS1",
          prev_ok,
          "CHOLESKY_TAUTOLOGY / SOURCE_GRAM_NOT_EXACT: "
          "class 3 not reached; stop rule fires; no RH claim")

    n_fail = sum(1 for _n, ok in CHECKS if not ok)
    n_ok = len(CHECKS) - n_fail
    verd = "CHOLESKY_TAUTOLOGY"
    print("\nRESULT: %d/%d gates PASS   SPEC_SHA %s   (%.1fs)  %s" % (
        n_ok, len(CHECKS), SPEC_SHA[:16], time.time() - T0, verd))
    if n_fail == 0:
        print("ONE DEFECT GRAM %sVERIFIED" % ("SMOKE " if smoke else ""))
        return 0
    print("ONE DEFECT GRAM FAILED %d" % n_fail)
    return 1


if __name__ == "__main__":
    sys.exit(main())
