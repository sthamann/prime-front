#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""edge_signature_probe -- PRIME.LDAGGER.EDGE_SIGNATURE.01
(round 401): THE AUGMENTED EDGE SIGNATURE -- reviewer 5.5 of
DCCLXII, the 3x3 model family of Phi = J^{-1} + U^T (A^dagger)^{-1} U
with a wandering source parameter tau, independent of the Weyl
analytics (R399).  Coexistence: r369 mixed form, r373 Haynsworth
(Lean), r375 P2 factorization, r397 selected mincut, r398 bulk
cluster (the 1/2-cluster is BULK, not Edge).

THE OBJECT.  M^dagger = A^dagger + U J U^T with
A^dagger = blkdiag(R_{N-3}-I/2, -1/2), U = [two dual CD columns,
SM border], J = diag(1,1,1/den).  Phi is the 3x3
    [ K2 , c0 ; c0^T , phi_bb ],
K2 = I + Ucd^T A0^{-1} Ucd the r367/r375 2x2.  Haynsworth on Phi:
ind_-(Phi) = ind_-(K2) + ind_-(sch) with
sch = phi_bb - c0^T K2^{-1} c0.  On the named census
ind_-(K2) = ind_-(A0), so the shift
    ind_-(Phi) = 1 + ind_-(A0)
is equivalent to sch < 0 (the border mode).

EXPLICIT D (not a fit).  D2 is the 2x2 Sylvester map of K2
(spectral theorem, closed for 2x2); d3 = 1/sqrt(|sch|).
D = blkdiag(D2, d3) is invertible on the living chart sch != 0.
Then D^T Phi D has 2x2 block J2 = diag(signs of K2) and
couplings tau = (a,b).  The unique 3x3 with that J2, those
couplings and Schur = sign(sch) is Phi_edge(a,b).  The
reconstruction identity D^T Phi D = Phi_edge(tau) is a SATZ
(E = 0 up to f64).  Phi_edge depends on wandering (a,b), not
a fixed M0 (r360-conform).

MODEL LEMMA (SATZ, finite 3x3, Haynsworth).  On the P1 chart
J2 = diag(-1,1), sch = -1: ind_-(Phi_edge) = 2 = 1 + 1 for
every (a,b).  On the vacuous chart J2 = I_2, sch = -1:
ind_-(Phi_edge) = 1 = 1 + 0.  det = det(J2)*sch = +/- 1 != 0.
g(tau) = dist(0, sigma(Phi_edge)) is positive on any bounded
K; as |tau|->oo one eigenvalue is ~1/|tau|^2.

TAU CANDIDATES (tested in order).  (i) r375 pair
(rho=gamma/lam, det(I+R+)) projectively (xi, eta): COMPACT and
trend-free on the census, but Spearman(|tau_ab|, xi) = 0.12
-- does not determine the 3x3; isotropic reconstruction from
(rho, delta) has ||E||/g ~ 80 at w9 (KILL as the model
parameter).  (ii) r321 QMAX proxy: Spearman(|tau_ab|, QMAX) =
0.26 and QMAX vs N is -0.96 (shrinks) while |tau_ab| vs N is
-0.32 -- KILL as the 3x3 parameter.  (iii) WINNER: the two
K2-signature couplings (a,b) of the SM-border.  Compact on
core-42 + EXT: |tau| <= 3.144, disk R=3.2 has grid g* >= 0.08;
large-N EXT |tau| is SMALLER (0.07..0.82).  den in [1.46, 1.63].

CALIBRATION DISCLOSURE.  Mixed 3x3, shift, sch sign, (a,b),
(xi, eta), isotropic E, scramble nf, two-period nnegA0, Twin,
chi live/dead were first measured in /tmp (r401_cal.py,
r401_cal2.py, r401_cal3.py) on the same constructors, 2026-08-29.
Frozen floors below are that measurement, sealed as gates.
No two-commit pre-blind freeze: pins disclosed.  Builder
fallback NOT taken: full wall ~20 s on core-42 + chi3/4-42 +
EXT-6 (kz69 N=5690 mixed-invert dropped, disclosed; compactness
already at N=3022).

FROZEN FROM /tmp (live re-gated, not fitted):
  * Fractions: Phi_edge(0,0) = diag(-1,1,-1), In = (1,2,0);
    vacuous diag(-1,1,1), In = (1,1,0); det = 1 on P1.
    Drop-border 4-node: ind_-(K2) = 1, no +1.
  * w9: den = 1.601114, rho = 1.8457, sch = -0.06696,
    (a,b) = (-0.53249, -0.06903), |tau| = 0.53695, g = 0.59007,
    nnegA0 = 1, nnegPhi = 2, nE <= 1e-14, J > 0, balance.
    isotropic nE/g = 80.7.
  * Core-42: 42/42 J > 0, balance, shift; P1 28/28 Phi=2;
    vac 14/14 Phi=1; |tau| max 3.144, min g 0.087;
    xi in [0.121, 0.622], eta in [0.768, 0.991], trend-free.
  * EXT: kz119/35/70/109/42/72 all shift; |tau| 0.075..0.817.
  * Twin kz 9/18/52 |d tau| ~ 1e-7.
  * Living chi3 37/37 shift, sch < 0; living chi4 41/41 shift.
  * Dead chi3 5/5 shift FAILS, ALL sch > 0, |tau| up to 6.7
    (outside living K) or vacuous with Phi = 0.
    Dead chi4-20: Phi = 0, sch = +0.023.
  * Scramble nnegA0 = 21, border pack nf = 37 (J-gate dies).
  * Two-period S=21 nnegA0 = 4 (A_edge chart {0,1} dies).

AUSGANG EDGE_SIGNATURE_MODEL.  SATZ: mixed form, Haynsworth
balance, reconstruction E = 0, model lemma on both charts,
det != 0.  CENSUS: shift on living, (a,b) in a compact K with
g* > 0, r375 pair compact but not the 3x3 moduli.  TWO-SIDED:
dead chi violate the shift at sch > 0.  Cofinal K is NOT
proved (r360-conform census).  No RH claim.

MACHINERY: r369 MH.mixed_update_toy / haynsworth_mixed_toy,
r367 FTI.cut_rung / inertia_of / fr_inertia, r362 ABD.border
_chain_pack, r375 P2.six_from_AU, r357 DMF chi, r342 PX,
r226 HS, r243 PB, r331 Twin, verify_lstar_instance.

NO RH CLAIM.  Finite identities, a named 3x3 family, named
kills.  Research documentation, not a theorem of RH.
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
import pair_extremal_probe as PX  # noqa: E402
import hirota_sign_probe as HS  # noqa: E402
import principal_bessel_probe as PB  # noqa: E402
import dirichlet_matched_frame_probe as DMF  # noqa: E402
import verify_lstar_instance as V  # noqa: E402
import verify_p2_steps as P2  # noqa: E402
import augmented_borodin_duality_probe as ABD  # noqa: E402
import high_moment_inertia_probe as H  # noqa: E402
import twin_resolution_probe as TR  # noqa: E402
import arch_kernel_diophantine_probe as AKD  # noqa: E402
import minimal_firewall_probe as MF  # noqa: E402

FLOOR = 1.0e-8
E_BAR = 1.0e-10
REL = 5.0e-3
DEAD_CHI3 = (15, 19, 23, 33, 39)
DEAD_CHI4 = (20,)
SAMPLE_EXT = (119, 35, 70, 109, 42, 72)
WORLD_TWIN = (18, 9, 52)
K_RADIUS = 3.2
GSTAR_FLOOR = 0.08
AB_MAX_P1 = 3.15
CORE_N, P1_N, VAC_N = 42, 28, 14
CHI3_LIVE_N, CHI3_DEAD_N = 37, 5
CHI4_LIVE_N, CHI4_DEAD_N = 41, 1
SCR_NNEG, SCR_NF = 21, 37
TP21_NNEG = 4
ISO_RATIO_FLOOR = 10.0
TWIN_D_BAR = 1.0e-5
XI_LO, XI_HI = 0.10, 0.65
ETA_LO, ETA_HI = 0.75, 0.995
DEN_LO, DEN_HI = 1.40, 1.70
TREND_BOX = (0.70, 1.30)

W9_DEN = 1.6011140112
W9_RHO = 1.8457009134
W9_SCH = -0.0669557660
W9_A, W9_B = -0.5324928620, -0.0690327173
W9_AB = 0.5369489400
W9_G = 0.5900737246
W9_XI, W9_ETA = 0.2971854524, 0.8562850183
W9_EVP = (-2.8132291730, -0.0664816325, 1.8039076348)

FTI_SHA_PREFIX = "e0d79840"
ABD_SHA_PREFIX = "7d810a9a"
DMF_SHA_PREFIX = "4bf1a94b"
MH_SHA_PREFIX = "138d0997"

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
    return (not bad), ("NO zero/prime oracles; mixed 3x3 / CD Gram / "
                       "SM border / r375 six-scalars only"
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


# ---- constructors (certificate: 3x3 + explicit D, no fit) ----

def Phi_edge(a, b, chart):
    """THE EXPLICIT 3x3 FAMILY.  chart=1 (P1): J2=diag(-1,1),
    sch=-1.  chart=0 (vacuous): J2=I, sch=-1.  Entries closed
    in (a,b).  Consumes the two couplings and the chart only."""
    a, b = float(a), float(b)
    if chart == 1:
        J2 = np.diag([-1.0, 1.0])
        sch = -1.0
    else:
        J2 = np.eye(2)
        sch = -1.0
    tau = np.array([a, b], float)
    J2inv = J2  # both charts have J2^{-1} = J2
    phibb = sch + float(tau @ J2inv @ tau)
    P = np.zeros((3, 3))
    P[:2, :2] = J2
    P[0, 2] = P[2, 0] = a
    P[1, 2] = P[2, 1] = b
    P[2, 2] = phibb
    return 0.5 * (P + P.T)


def sylvester_D2(K2):
    """2x2 Sylvester map: D2^T K2 D2 = diag(signs).  Spectral
    theorem on a 2x2 (explicit).  Consumes K2 only."""
    K2 = 0.5 * (np.asarray(K2, float) + np.asarray(K2, float).T)
    ev, V = np.linalg.eigh(K2)
    d = np.ones(2)
    signs = np.zeros(2)
    ok = True
    for i in range(2):
        if abs(ev[i]) < FLOOR:
            ok = False
            signs[i] = 0.0
        else:
            signs[i] = 1.0 if ev[i] > 0 else -1.0
            d[i] = 1.0 / math.sqrt(abs(ev[i]))
    return V @ np.diag(d), signs, ev, ok


def iso_model(rho, dlt, lam, den):
    """CANDIDATE (i) isotropic reconstruction -- MUST FAIL as
    the 3x3 model.  Consumes r375 scalars + den only."""
    r = math.sqrt(max(float(dlt), 0.0)) - 1.0
    K2e = np.array([[(1.0 + r) * (1.0 - float(rho)), 0.0],
                     [0.0, 1.0 + r]])
    D2s = np.eye(2) / math.sqrt(max(float(lam), 1e-18))
    P = np.zeros((3, 3))
    P[:2, :2] = D2s.T @ K2e @ D2s
    P[2, 2] = 1.0 - 2.0 / float(den)
    return 0.5 * (P + P.T)


def phi_block(xu, wu, yn, vn, Nw, S, L, i1, i2,
              xp, wp, bxs, bws, bys, bvs, Bm=None):
    """THE r401 BLOCK: mixed 3x3 Phi, r375 scalars, signature
    D, Phi_edge(a,b), E, shift.  Consumes measure arrays, pair
    indices and the border window only."""
    cut = FTI.cut_rung(xu, wu, yn, vn, Nw, S, L, i1, i2, keep=True)
    six = P2.six_from_AU(cut["A0"], cut["U"])
    yn = np.asarray(yn, float)
    vn = np.asarray(vn, float)
    bp = ABD.border_chain_pack(np.asarray(xp, float), np.asarray(wp, float),
                               yn, vn, bxs, bws, bys, bvs, Nw)
    A0 = np.asarray(cut["A0"], float)
    Ucd = np.asarray(cut["U"], float)
    out = dict(ok=False, nnegA0=int(cut["nneg"]), P1=bool(cut["P1"]),
               P2=bool(cut["P2"]), detK=float(cut["detK"]),
               Nw=int(Nw), Sm=int(A0.shape[0]), nf=bp.get("nf"),
               lam=six["lam"], gamma=six["gamma"], detIRp=six["detIRp"],
               excess=six["excess"],
               rho=(six["gamma"] / six["lam"] if six["lam"] > 0
                    else float("nan")))
    if not bp["ok"]:
        return out
    a_mu, b_mu, h0_mu = V.mu_chain(np.asarray(xp, float),
                                  np.asarray(wp, float), Nw)
    bxa = np.concatenate([np.asarray(bxs, float), np.asarray(bys, float)])
    bwa = np.concatenate([np.asarray(bws, float), -np.asarray(bvs, float)])
    bvec = ABD.bvec_chunked(a_mu, b_mu, h0_mu, bxa, bwa, Nw)
    gam = float(bvec @ bvec) / float(bp["Bw"])
    if Bm is None:
        Bm = V.b_matrix(a_mu, b_mu, h0_mu, yn, vn, Nw)
    vt = cut["epsY"] * (Bm @ (bvec / math.sqrt(bp["Bw"])))
    s = cut["Rm"] @ vt
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
    Jinv = np.diag([1.0, 1.0, float(den)])
    Phi = Jinv + U.T @ np.linalg.solve(A, U)
    Phi = 0.5 * (Phi + Phi.T)
    Mdag = 0.5 * ((A + U @ J @ U.T) + (A + U @ J @ U.T).T)
    IA = FTI.inertia_of(A)
    IP = FTI.inertia_of(Phi)
    IMn = FTI.inertia_of(-Phi)
    IJ = FTI.inertia_of(-Jinv)
    IM = FTI.inertia_of(Mdag)
    bal = (IA["npos"] + IMn["npos"] == IJ["npos"] + IM["npos"]
           and IA["nneg"] + IMn["nneg"] == IJ["nneg"] + IM["nneg"]
           and IA["nzer"] + IMn["nzer"] == IJ["nzer"] + IM["nzer"])
    K2 = np.eye(2) + Ucd.T @ np.linalg.solve(A0, Ucd)
    K2 = 0.5 * (K2 + K2.T)
    evK = np.linalg.eigvalsh(K2)
    nnegK2 = int(np.sum(evK < -FLOOR))
    c0 = Ucd.T @ np.linalg.solve(A0, s)
    qbb = float(s @ np.linalg.solve(A0, s))
    phibb = float(den) - 2.0 + qbb
    sch = phibb - float(c0 @ np.linalg.solve(K2, c0))
    D2, signs, _evD, okD = sylvester_D2(K2)
    if abs(sch) > FLOOR:
        d3 = 1.0 / math.sqrt(abs(sch))
        sch_chart = math.copysign(1.0, sch)
    else:
        d3 = 1.0 / math.sqrt(max(abs(den), 1e-18))
        sch_chart = float("nan")
        okD = False
    D = np.zeros((3, 3))
    D[:2, :2] = D2
    D[2, 2] = d3
    Pn = 0.5 * ((D.T @ Phi @ D) + (D.T @ Phi @ D).T)
    a, b = float(Pn[0, 2]), float(Pn[1, 2])
    tau_v = np.array([a, b])
    J2 = np.diag(signs)
    J2inv = np.diag(np.where(np.abs(signs) > 0.5, signs, np.ones(2)))
    phibb_e = sch_chart + float(tau_v @ J2inv @ tau_v)
    Pe = np.zeros((3, 3))
    Pe[:2, :2] = J2
    Pe[0, 2] = Pe[2, 0] = a
    Pe[1, 2] = Pe[2, 1] = b
    Pe[2, 2] = phibb_e
    E = Pn - Pe
    nE = float(np.linalg.norm(E, 2))
    g = float(np.min(np.abs(np.linalg.eigvalsh(Pe))))
    nneg_e = int(np.sum(np.linalg.eigvalsh(Pe) < -FLOOR))
    rho = out["rho"]
    dlt = six["detIRp"]
    xi = ((rho - 1.0) / (rho + 1.0) if np.isfinite(rho)
          else float("nan"))
    eta = dlt / (1.0 + dlt) if np.isfinite(dlt) else float("nan")
    chart = 1 if cut["nneg"] >= 1 else 0
    shift = (IP["nneg"] == 1 + cut["nneg"])
    qmax = float(np.max(np.abs(Ucd)))
    evP = np.linalg.eigvalsh(Phi)
    out.update(
        ok=True, den=float(den), Jsucc=bool(den > FLOOR),
        nnegA=IA["nneg"], nnegPhi=IP["nneg"], nnegK2=nnegK2,
        nnegM=IM["nneg"], bal=bal, sch=sch, a=a, b=b,
        ab=math.hypot(a, b), nE=nE, g=g,
        ratio=nE / g if g > 0 else float("nan"),
        nneg_e=nneg_e, sch_chart=sch_chart, okD=okD, signs=tuple(signs),
        xi=xi, eta=eta, dlt=float(dlt), chart=chart, shift=shift,
        qmax=qmax, evP=tuple(float(x) for x in evP),
        evK=tuple(float(x) for x in evK),
        nzerA=IA["nzer"], nposPhi=IP["npos"],
    )
    if np.isfinite(rho) and six["lam"] > 0:
        Piso = iso_model(rho, dlt, six["lam"], den)
        # compare isotropic model in the w-aligned 1/sqrt(lam) frame
        w = np.array([six["alpha"], six["beta"]], float)
        nw = float(np.linalg.norm(w))
        Rw = np.eye(2)
        if nw > 1e-14:
            e1 = w / nw
            Rw = np.column_stack([e1, np.array([-e1[1], e1[0]])])
        Diso = np.eye(3)
        Diso[:2, :2] = Rw / math.sqrt(max(six["lam"], 1e-18))
        Diso[2, 2] = 1.0 / math.sqrt(max(abs(den), 1e-18))
        Pn_iso = 0.5 * ((Diso.T @ Phi @ Diso) + (Diso.T @ Phi @ Diso).T)
        nE_iso = float(np.linalg.norm(Pn_iso - Piso, 2))
        g_iso = float(np.min(np.abs(np.linalg.eigvalsh(Piso))))
        out["nE_iso"] = nE_iso
        out["g_iso"] = g_iso
        out["iso_ratio"] = (nE_iso / g_iso if g_iso > 0 else float("nan"))
    else:
        out["iso_ratio"] = float("nan")
    return out


def main_row(kz):
    R = PX.build_rung(kz)
    mz = R["mz"]
    alk = float(V.window_shape(kz)[0])
    dsm = HS.window_data(kz, comb=PB.smooth_comb(alk))
    p = phi_block(mz["xu"], mz["wu"], mz["yn"], mz["vn"],
                  R["Nw"], R["S"], mz["L"], R["i1"], R["i2"],
                  mz["xp"], mz["wp"], dsm["xs"], dsm["ws"],
                  dsm["ys"], dsm["vs"], Bm=R["B"])
    p["kz"] = kz
    p["tag"] = "MAIN-%d" % kz
    return p


def chi_row(kz, q, lpq, tag):
    uu, ww, _nn, _ch = DMF.chi_window_comb(kz, q)
    if len(uu) < V.N_ATOM_MIN:
        return None
    mzc = DMF.chi_build_measures(kz, uu, ww, 1.0, lpq)
    j1, j2 = PX.pair_select(mzc["yn"])
    usm, wsm = PB.smooth_comb(mzc["alpha"])
    mzb = DMF.chi_build_measures(kz, usm, wsm, 1.0, lpq)
    p = phi_block(mzc["xu"], mzc["wu"], mzc["yn"], mzc["vn"],
                  mzc["Nw"], mzc["S"], mzc["L"], j1, j2,
                  mzc["xp"], mzc["wp"], mzb["xp"], mzb["wp"],
                  mzb["yn"], mzb["vn"])
    p["kz"] = kz
    p["tag"] = tag
    return p


def g_of(a, b, chart):
    ev = np.linalg.eigvalsh(Phi_edge(a, b, chart))
    return float(np.min(np.abs(ev))), int(np.sum(ev < -FLOOR))


def spearman(x, y):
    x, y = np.asarray(x, float), np.asarray(y, float)
    rx = np.argsort(np.argsort(x))
    ry = np.argsort(np.argsort(y))
    return float(np.corrcoef(rx, ry)[0, 1])


def Phi_edge_Q(a, b, chart):
    """Fractions 3x3 at rational (a,b)."""
    a, b = Fr(a), Fr(b)
    if chart == 1:
        J00, J11, sch = Fr(-1), Fr(1), Fr(-1)
    else:
        J00, J11, sch = Fr(1), Fr(1), Fr(-1)
    phibb = sch + a * (J00 * a) + b * (J11 * b)
    return [[J00, Fr(0), a],
            [Fr(0), J11, b],
            [a, b, phibb]]


# ---- legs ----

def part_a_toy():
    section("S1  LEG C -- MODEL LEMMA / RECONSTRUCTION / MUTANTS (TOY)")
    Tm = MH.mixed_update_toy()
    check("G01-Fractions-mixed",
          Tm["dev"] == 0 and Tm["den"] != 0,
          "M^dagger == A + U J U^T, den=%s residual EXACT 0" % Tm["den"])
    Th = MH.haynsworth_mixed_toy()
    ok_add = (Th["iH"][0] == Th["iA"][0] + Th["iMPhi"][0]
              and Th["iH"][1] == Th["iA"][1] + Th["iMPhi"][1]
              and Th["iH"][0] == Th["iMJ"][0] + Th["iM"][0]
              and Th["iH"][1] == Th["iMJ"][1] + Th["iM"][1])
    check("G02-Haynsworth-mixed-Q",
          ok_add and Th["iJ"][1] >= 1,
          "In(H)=In(A)+In(-Phi)=In(-J^{-1})+In(M) EXACT")
    P0 = Phi_edge_Q(0, 0, 1)
    i0 = FTI.fr_inertia(P0)
    check("G03-model-P1-origin",
          i0 == (1, 2, 0) and P0[0][0] * P0[1][1] * P0[2][2] == Fr(1),
          "Phi_edge(0,0)_P1 = diag(-1,1,-1), In=%s, det-sign +" % (i0,))
    Pv = Phi_edge_Q(0, 0, 0)
    iv = FTI.fr_inertia(Pv)
    check("G04-model-vac-origin",
          iv == (2, 1, 0),
          "Phi_edge(0,0)_vac In=%s (one negative = border)" % (iv,))
    # det = det(J2)*sch = 1 on P1, for a rational point
    P1 = Phi_edge_Q(Fr(1), 0, 1)
    # det via expansion
    det1 = (P1[0][0] * (P1[1][1] * P1[2][2] - P1[1][2] * P1[2][1])
            - P1[0][1] * (P1[1][0] * P1[2][2] - P1[1][2] * P1[2][0])
            + P1[0][2] * (P1[1][0] * P1[2][1] - P1[1][1] * P1[2][0]))
    check("G05-model-det-one",
          det1 == Fr(1) and FTI.fr_inertia(P1)[1] == 2,
          "P1 chart (a,b)=(1,0): det=%s In nneg=2" % det1)
    # grid inertia on the disk (finite check of the SATZ)
    nbad, gmin = 0, 1e9
    for th in np.linspace(0, 2 * np.pi, 64, endpoint=False):
        a, b = K_RADIUS * math.cos(th), K_RADIUS * math.sin(th)
        g, nneg = g_of(a, b, 1)
        gmin = min(gmin, g)
        if nneg != 2:
            nbad += 1
    check("G06-model-disk-P1",
          nbad == 0 and gmin >= GSTAR_FLOOR,
          "64-pt circle R=%.1f nneg=2 all, gmin=%.4f >= %.2f"
          % (K_RADIUS, gmin, GSTAR_FLOOR))
    nbad0 = 0
    for th in np.linspace(0, 2 * np.pi, 32, endpoint=False):
        if g_of(2.0 * math.cos(th), 2.0 * math.sin(th), 0)[1] != 1:
            nbad0 += 1
    check("G07-model-disk-vac",
          nbad0 == 0,
          "vacuous chart R=2: nneg=1 on 32/32")
    # drop-border mutant on the 4-node: K2 only, shift by 0
    A0 = np.diag([-1.0, 1.0, 2.0, 3.0])
    Ucd = np.array([[2.0, 1.0], [0.0, 1.0], [0.0, 0.0], [0.0, 0.0]])
    K2 = np.eye(2) + Ucd.T @ np.linalg.solve(A0, Ucd)
    nK = int(np.sum(np.linalg.eigvalsh(K2) < -FLOOR))
    nA0 = int(np.sum(np.linalg.eigvalsh(A0) < -FLOOR))
    check("G08-mutant-drop-border",
          nK == nA0 and nK == 1,
          "two-rank K2 nneg=%d == nnegA0 (shift by 0, not +1)" % nK)
    check("G08b-wrong-sign-J",
          Tm["dev_w"] > 0,
          "wrong-sign J residual %s != 0 (border scale load-bearing)"
          % Tm["dev_w"])


def part_b_w9():
    section("S2  LEG A -- w9 3x3 + SHIFT + MODEL")
    p = main_row(9)
    check("G10-w9-gates",
          p["ok"] and p["Jsucc"] and p["bal"] and p["okD"]
          and p["nnegA0"] == 1 and p["nnegPhi"] == 2 and p["shift"],
          "J>0 balance D-ok nnegA0=1 nnegPhi=2 SHIFT")
    check("G11-w9-pins",
          abs(p["den"] / W9_DEN - 1.0) <= REL
          and abs(p["rho"] / W9_RHO - 1.0) <= REL
          and abs(p["sch"] / W9_SCH - 1.0) <= 0.02
          and abs(p["a"] - W9_A) <= 0.01
          and abs(p["b"] - W9_B) <= 0.01
          and abs(p["ab"] / W9_AB - 1.0) <= REL
          and abs(p["g"] / W9_G - 1.0) <= REL,
          "den=%.6f rho=%.4f sch=%.5f (a,b)=(%.4f,%.4f) |τ|=%.4f g=%.4f"
          % (p["den"], p["rho"], p["sch"], p["a"], p["b"], p["ab"], p["g"]))
    check("G12-w9-E-zero",
          p["nE"] <= E_BAR and p["nE"] < 0.5 * p["g"],
          "||E||=%.2e < g/2 (g=%.4f) -- reconstruction SATZ"
          % (p["nE"], p["g"]))
    check("G13-w9-iso-KILL",
          np.isfinite(p["iso_ratio"]) and p["iso_ratio"] >= ISO_RATIO_FLOOR,
          "isotropic (rho,detIRp) reconstruction ||E||/g=%.1f >= %g "
          "(candidate i is NOT the 3x3 model)"
          % (p["iso_ratio"], ISO_RATIO_FLOOR))
    check("G14-w9-Phi-eigs",
          abs(p["evP"][0] / W9_EVP[0] - 1.0) <= 0.02
          and abs(p["evP"][2] / W9_EVP[2] - 1.0) <= 0.02,
          "evP=(%.4f, %.5f, %.4f) large pair tracks K2"
          % p["evP"])
    return p


def part_d_kills():
    section("S3  LEG D -- DEAD CHI / SCRAMBLE / TWO-PERIOD")
    p15 = chi_row(15, DMF.Q_CHI3, DMF.LPQ3, "C3-15-DEAD")
    check("G20-dead-chi3-15",
          p15["ok"] and (not p15["shift"]) and p15["sch"] > 0
          and p15["nnegA0"] == 1 and p15["nnegPhi"] == 1,
          "DEAD: nnegA0=1 nnegPhi=1 sch=%+.4f > 0 (shift FAILS)"
          % p15["sch"])
    p3 = chi_row(9, DMF.Q_CHI3, DMF.LPQ3, "C3-9-LIVE")
    check("G21-live-chi3-9",
          p3["ok"] and p3["shift"] and p3["sch"] < 0
          and p3["nnegA0"] == 0 and p3["nnegPhi"] == 1,
          "LIVE vacuous: nnegA0=0 nnegPhi=1 sch=%.4f SHIFT"
          % p3["sch"])
    mz_s = H.scramble_mz()
    j1, j2 = PX.pair_select(mz_s["yn"])
    oS = FTI.cut_rung(mz_s["xu"], mz_s["wu"], mz_s["yn"], mz_s["vn"],
                       mz_s["Nw"], mz_s["S"], mz_s["L"], j1, j2)
    usm, wsm = PB.smooth_comb(mz_s["alpha"])
    mzb = DMF.chi_build_measures(9, usm, wsm, 1.0, DMF.LPQ3)
    pSc = phi_block(mz_s["xu"], mz_s["wu"], mz_s["yn"], mz_s["vn"],
                    mz_s["Nw"], mz_s["S"], mz_s["L"], j1, j2,
                    mz_s["xp"], mz_s["wp"], mzb["xp"], mzb["wp"],
                    mzb["yn"], mzb["vn"])
    check("G22-scramble",
          oS["nneg"] == SCR_NNEG and (not pSc.get("ok"))
          and pSc.get("nf") == SCR_NF,
          "nnegA0=%d (not in {0,1}); border pack nf=%s (J-gate dies)"
          % (oS["nneg"], pSc.get("nf")))
    mz = H.two_period_mz(21, 2.0 / 3.0)
    j1, j2 = PX.pair_select(mz["yn"])
    oT = FTI.cut_rung(mz["xu"], mz["wu"], mz["yn"], mz["vn"],
                       mz["Nw"], mz["S"], mz["L"], j1, j2)
    check("G23-two-period",
          oT["nneg"] >= TP21_NNEG,
          "S=21 nnegA0=%d >= 4 (A_edge chart {0,1} dies)"
          % oT["nneg"])
    p4d = chi_row(20, DMF.Q_CHI4, DMF.LPQ4, "C4-20-DEAD")
    check("G24-dead-chi4-20",
          p4d["ok"] and (not p4d["shift"]) and p4d["sch"] > 0
          and p4d["nnegPhi"] == 0,
          "dead chi4-20 nnegPhi=0 sch=%+.4f (dies at the border mode)"
          % p4d["sch"])
    return p15, p3


def part_full():
    section("S4  LEG A/B -- CORE-42 + CHI + EXT + TWIN")
    core = list(V.admissible_indices())
    rows = []
    for kz in core:
        p = main_row(kz)
        p["kz"] = kz
        rows.append(p)
    ok = [r for r in rows if r.get("ok")]
    p1 = [r for r in ok if r["nnegA0"] == 1]
    vac = [r for r in ok if r["nnegA0"] == 0]
    check("G40-core42-shift",
          len(ok) == CORE_N and all(r["shift"] and r["Jsucc"] and r["bal"]
                                    for r in ok)
          and len(p1) == P1_N and len(vac) == VAC_N
          and all(r["nnegPhi"] == 2 for r in p1)
          and all(r["nnegPhi"] == 1 for r in vac),
          "42/42 J>0+balance+SHIFT; P1 %d Phi=2; vac %d Phi=1"
          % (len(p1), len(vac)))
    ab_max = max(r["ab"] for r in p1)
    g_min = min(r["g"] for r in p1)
    e_max = max(r["nE"] for r in p1)
    check("G41-compact-ab",
          ab_max <= AB_MAX_P1 and g_min >= GSTAR_FLOOR
          and e_max <= E_BAR and all(r["sch"] < 0 for r in p1),
          "P1 |τ| max=%.3f <= %.2f; min g=%.4f; max ||E||=%.1e; sch<0"
          % (ab_max, AB_MAX_P1, g_min, e_max))
    xis = [r["xi"] for r in p1]
    etas = [r["eta"] for r in p1]
    dens = [r["den"] for r in ok]
    check("G42-r375-compact",
          min(xis) >= XI_LO and max(xis) <= XI_HI
          and min(etas) >= ETA_LO and max(etas) <= ETA_HI
          and min(dens) >= DEN_LO and max(dens) <= DEN_HI,
          "xi [%.3f, %.3f] eta [%.3f, %.3f] den [%.3f, %.3f] "
          "(compact, not the 3x3 moduli)"
          % (min(xis), max(xis), min(etas), max(etas),
             min(dens), max(dens)))
    p1s = sorted(p1, key=lambda r: r["Nw"])
    nmid = len(p1s) // 2
    trend_ok = True
    for key in ("xi", "eta", "den", "ab"):
        lo = [r[key] for r in p1s[:nmid] if np.isfinite(r[key])]
        hi = [r[key] for r in p1s[nmid:] if np.isfinite(r[key])]
        if not lo or not hi:
            trend_ok = False
            break
        rat = float(np.median(hi)) / float(np.median(lo))
        trend_ok = trend_ok and TREND_BOX[0] <= rat <= TREND_BOX[1]
    check("G43-trend-free",
          trend_ok,
          "halves med(xi,eta,den,|τ|) ratio in %s (K stable, r360)"
          % (TREND_BOX,))
    sp_q = spearman([r["ab"] for r in ok], [r["qmax"] for r in ok])
    sp_xi = spearman([r["ab"] for r in p1], [r["xi"] for r in p1])
    check("G44-cand-i-ii-KILL",
          abs(sp_q) < 0.5 and abs(sp_xi) < 0.5,
          "Spearman(|τ|, QMAX)=%.3f; (|τ|, xi)=%.3f -- neither "
          "parametrizes the 3x3 (iii wins)"
          % (sp_q, sp_xi))

    live3, dead3, live4, dead4 = [], [], [], []
    for kz in core:
        p = chi_row(kz, DMF.Q_CHI3, DMF.LPQ3, "C3-%d" % kz)
        if p is not None:
            (dead3 if kz in DEAD_CHI3 else live3).append(p)
        p4 = chi_row(kz, DMF.Q_CHI4, DMF.LPQ4, "C4-%d" % kz)
        if p4 is not None:
            (dead4 if kz in DEAD_CHI4 else live4).append(p4)
    check("G45-chi3-live",
          len(live3) == CHI3_LIVE_N
          and all(r.get("ok") and r["shift"] and r["sch"] < 0
                  for r in live3),
          "live chi3 %d/%d SHIFT sch<0" % (len(live3), CHI3_LIVE_N))
    check("G46-chi3-dead",
          len(dead3) == CHI3_DEAD_N
          and all(r.get("ok") and (not r["shift"]) and r["sch"] > 0
                  for r in dead3),
          "dead chi3 %d/%d SHIFT FAILS, ALL sch>0 (two-sided)"
          % (len(dead3), CHI3_DEAD_N))
    check("G47-chi4",
          len(live4) == CHI4_LIVE_N
          and all(r.get("ok") and r["shift"] for r in live4)
          and len(dead4) == CHI4_DEAD_N
          and all((not r["shift"]) and r["sch"] > 0 for r in dead4),
          "live chi4 %d/%d SHIFT; dead %d sch>0"
          % (len(live4), CHI4_LIVE_N, len(dead4)))

    ext_ok = True
    ext_ab = []
    for kz in SAMPLE_EXT:
        p = main_row(kz)
        ext_ok = (ext_ok and p.get("ok") and p["shift"]
                  and p["nE"] <= E_BAR)
        ext_ab.append(p["ab"] if p.get("ok") else 99.0)
        print("    EXT-%d N=%d A0=%d Phi=%d |t|=%.3f sch=%+.4f"
              % (kz, p["Nw"], p["nnegA0"], p["nnegPhi"],
                 p.get("ab", -1), p.get("sch", float("nan"))),
              flush=True)
    check("G48-EXT",
          ext_ok and max(ext_ab) < AB_MAX_P1,
          "%d EXT rows SHIFT, |τ| max=%.3f (not exploding vs core 3.14)"
          % (len(SAMPLE_EXT), max(ext_ab)))

    tw_ok = True
    for kz in WORLD_TWIN:
        uuc, mmc = TR.base_comb(kz)
        mzD = TR.build_world(kz, uuc, mmc)
        gapsc = MF.local_gaps(uuc)
        u2c, m2c, _dn, _du = AKD.twin_rational(
            uuc, mmc, gapsc, mzD["D"], 1.0e-8)
        mzT = TR.build_world(kz, u2c, m2c)
        alk = float(V.window_shape(kz)[0])
        dsm = HS.window_data(kz, comb=PB.smooth_comb(alk))
        j1, j2 = PX.pair_select(mzT["yn"])
        pT = phi_block(mzT["xu"], mzT["wu"], mzT["yn"], mzT["vn"],
                       mzT["Nw"], mzT["S"], mzT["L"], j1, j2,
                       mzT["xp"], mzT["wp"], dsm["xs"], dsm["ws"],
                       dsm["ys"], dsm["vs"])
        pM = main_row(kz)
        tw_ok = (tw_ok and pT.get("ok") and pT["shift"]
                 and abs(pT["ab"] - pM["ab"]) <= TWIN_D_BAR
                 and abs(pT["sch"] - pM["sch"]) <= TWIN_D_BAR)
    check("G49-twin",
          tw_ok, "Twin kz %s |d τ|,|d sch| <= %g, SHIFT"
          % (WORLD_TWIN, TWIN_D_BAR))
    return rows


def main():
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke

    print("=" * 78)
    print("edge_signature_probe -- "
          "PRIME.LDAGGER.EDGE_SIGNATURE.01 (round 401)")
    print("SPEC_SHA %s   (FTI %s / ABD %s / MH %s)"
          % (SPEC_SHA[:16], FTI.SPEC_SHA[:16], ABD.SPEC_SHA[:16],
             MH.SPEC_SHA[:16]))
    print("mode: %s" % ("SMOKE" if smoke else
                         "FULL (core-42 + chi + EXT-6 + Twin)"))
    print("=" * 78)

    section("S0  FIREWALL + IMPORT INTEGRITY")
    okf, det = firewall_audit()
    check("G00-firewall", okf, det)
    sha_ok = (FTI.SPEC_SHA.startswith(FTI_SHA_PREFIX)
              and ABD.SPEC_SHA.startswith(ABD_SHA_PREFIX)
              and DMF.SPEC_SHA.startswith(DMF_SHA_PREFIX)
              and MH.SPEC_SHA.startswith(MH_SHA_PREFIX))
    check("G00b-import-sha", sha_ok,
          "FTI %s / ABD %s / DMF %s / MH %s"
          % (FTI.SPEC_SHA[:8], ABD.SPEC_SHA[:8], DMF.SPEC_SHA[:8],
             MH.SPEC_SHA[:8]))
    ag = antigate_fragment_audit()
    check("G00c-no-fit", not ag,
          "no fit primitives" if not ag else "; ".join(ag))

    part_a_toy()
    pw9 = part_b_w9()
    part_d_kills()
    if not smoke:
        part_full()
    else:
        section("S4  FULL CENSUS skipped (--smoke)")

    section("S5  VERDICT")
    prev_ok = all(ok for _n, ok in CHECKS)
    check("G50-verdict-EDGE_SIGNATURE_MODEL",
          prev_ok,
          "EDGE_SIGNATURE_MODEL: model lemma SATZ; E=0 SATZ; "
          "shift on living; dead chi sch>0; (a,b) compact census; "
          "no cofinal K; no RH claim")

    n_fail = sum(1 for _n, ok in CHECKS if not ok)
    n_ok = len(CHECKS) - n_fail
    verd = "EDGE_SIGNATURE_MODEL"
    print("\nRESULT: %d/%d gates PASS   SPEC_SHA %s   (%.1fs)  %s" % (
        n_ok, len(CHECKS), SPEC_SHA[:16], time.time() - T0, verd))
    if n_fail == 0:
        print("EDGE SIGNATURE %sVERIFIED" % ("SMOKE " if smoke else ""))
        return 0
    print("EDGE SIGNATURE FAILED %d" % n_fail)
    return 1


if __name__ == "__main__":
    sys.exit(main())
