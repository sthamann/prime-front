#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""signed_border_mean_probe -- PRIME.RDAGGER.SIGNED_BORDER_MEAN.01
(round 444): the signed mean of q^dagger as a triple sum
over blocks and border atoms, with a circularity gate
(the last analytic object of the RH path after r442).

THE OBJECT.  r442: kappa^dagger = 1{q^dagger > 1}, so the
block mean of the index is the frequency of q^dagger > 1.
Source form q^dagger = B_w^{-1} b^T (I-C)^{-1} b, residual
10^{-15}.  Unsigned envelopes 38.5 / 87 REFUTED as a <1
majorant.  This round expands the quadratic form into the
triple sum (block x atom x atom), splits diagonal /
off-diagonal and pole / regular, and attempts a classical
mean-value bound under the honesty gate.

LEG A (triple sum).  On window W_k,
  q_k^dagger = sum_{a,a'} (sigma_a sigma_{a'}/B_{w,k})
    <phi_k(t_a), (I-C_k)^{-1} phi_k(t_{a'})>
with atoms the signed von-Mangoldt border measure at the
dyadic zeta-anchor a_k = 2^k.  The block mean is the
average of these double sums.  DIAGONAL a=a' is the
unsigned skeleton (sigma^2).  OFF-DIAGONAL carries the
classical bilinear phases log n - log n'.

LEG B (resolvent kernel).  Spectral split
  (I-C)^{-1} = psi_max psi_max^T / (1-lambda_max) + R_reg
as in r436.  If the pole carried q^dagger-growth and R_reg
were block-stable, the mean would be a pole-weighted prime
sum.  Measured: the opposite.

LEG C (bound + gate).  Tools: Montgomery-Vaughan MVT on
the bilinear off-diagonal, Cauchy-Schwarz block/atom,
Gallagher.  Each brick typed unconditional / PNT / RH-near.
Honest exit allowed: ZIRKULAER, naming the missing signed
strength (second precise circularity verdict after r399).

LEG D (kills).  Unsigned regression 38.5/87; dead-chi
consistency (q^dagger>1 visible in the split); mutants
(drop-pole, wrong block normalisation); soft means (r440).

CALIBRATION DISCLOSURE.  Triple-sum residual, diagonal/off,
pole/reg, selected sequence, dead-chi overshoot, unsigned
envelopes, cosine-kernel correlation first measured in
/tmp (r444_cal.py, r444_cal2.py) on the r433/r442
constructors, 2026-08-30.  Frozen floors below are that
measurement, sealed as gates.  Pins disclosed.
Builder fallback NOT taken: full wall << 120 s
(no k=8 rebuild; r421 pin unused).

FROZEN FROM /tmp (live re-gated, not fitted):
  * SATZ Q: C=diag(1/2,0), atoms phi=(1,0) and (1,1),
    sigma=1,1, B_w=1 => q=9, q_diag=5, q_off=4 exact.
    Pole split: C=diag(1/2,1/4), b=(1,1) => q=10/3,
    q_pole=2, q_reg=4/3 exact.
  * w9: recon residual 1.4e-16; q=0.93304423;
    q_diag=0.48228140, q_off=0.45076283;
    q_pole=0.00068037, q_reg=0.93236386;
    pole_share=0.00073; C-gap=1.6752e-4 (n_ge1=0);
    |b|-envelope 38.486; corr(K_off, cos Delta log)=0.026.
  * Selected k=3,4,5,6,7,9
    q_diag 0.515169, 0.482281, 0.892171, 0.834508,
           2.272079, 40.777313  (OVERFLOW from k=7);
    q_off  +0.413266, +0.450763, -0.000807, +0.096596,
           -1.327475, -39.815098  (cancellation load-bearing
           from k=7);
    q_pole 0.000297, 0.000680, 0.002725, 0.000879,
           0.000488, 0.000087  (share <= 0.0031);
    q_reg  0.928139, 0.932364, 0.888639, 0.930225,
           0.944116, 0.962128  (= q to 10^{-3});
    C-gap  2.987e-3 -> 1.913e-8 (same shrink as r440 collar).
    Mean q=0.931794; mean q_diag=7.629 >1; mean q_pole=8.6e-4.
    Near-1 cluster grows (k=9: 65 modes with gap<0.01) but
    energy share of q is 0.008 -- bulk regular, not the
    collar, carries q^dagger on living windows.
  * Dead chi 6/6: q>1 AND q_reg<1 AND q_pole > 1-q_reg
    (pole overshoot is the death).  CHI3-15 q=1.023181
    q_pole=0.03795 q_reg=0.98523; CHI3-39 q_pole=0.0946
    (largest).  Live CHI3-9 q_pole=0.00342.  Drop-pole
    mutant: all 6 dead read as living.
  * Unsigned |sigma| kz17=2.103, kz116=87.08 (r442 regression).
  * Core-42 (cal2, not re-gated in the probe): 42/42 q_reg<1,
    mean_top1=4.5e-4, max q=0.99849 is q_reg itself
    (MAIN risk is bulk drift, not a pole spike).

AUSGANG ZIRKULAER / TRIPLE_SUM_EXACT / POLE_NOT_CARRIER /
DIAGONAL_OVERFLOWS / OFFDIAG_LOADBEARING /
DEAD_CHI_POLE_OVERSHOOT.
SATZ: the triple-sum expansion and the spectral split
(finite linear algebra).  REFUTED: diagonal as a <1
majorant; reduction of the living mean to a pole-weighted
prime sum; cosine/MVT/CS/Gallagher as closing tools.
CENSUS: Selected living by regular-kernel cancellation
that becomes load-bearing at k=7; dead chi die by a
pole overshoot over a still-sub-1 regular part.
ZIRKULAER: the missing signed strength is a uniform bound
on the REGULAR off-diagonal cancellation matching the
diagonal growth (already 40 at k=9), against a
window-dependent OP-resolvent kernel that is not a
classical k(log n/n').  That quality is RH-near
(second precise circularity verdict after r399).
No RH claim.

MACHINERY: r442 BM.source_q / SEL_LIVE, r433 ER._measures /
redheffer_of, r362 ABD.bvec_chunked / border_chain_pack,
r420/r424 signed border, r436 pole/reg template, r440
collar gap, r399 circularity protocol, r226 V.mu_chain /
b_matrix / admissible_indices.

NO RH CLAIM.  Finite identities, named refutations, a
named census, a named circularity.  Research
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

import edge_redheffer_probe as ER  # noqa: E402
import block_mean_probe as BM  # noqa: E402
import mean_tau_index_probe as MT  # noqa: E402
import dirichlet_matched_frame_probe as DMF  # noqa: E402
import verify_lstar_instance as V  # noqa: E402
import augmented_borodin_duality_probe as ABD  # noqa: E402
import final_two_rank_inertia_probe as FTI  # noqa: E402
import high_moment_inertia_probe as HM  # noqa: E402

ER_SHA_PREFIX = "8371b954"
BM_SHA_PREFIX = "bc5644a9"
MT_SHA_PREFIX = "3807189a"
ABD_SHA_PREFIX = "7d810a9a"
DMF_SHA_PREFIX = "4bf1a94b"

SEL_LIVE = BM.SEL_LIVE
SEL_SMOKE = BM.SEL_SMOKE
DEAD_CHI3 = BM.DEAD_CHI3
DEAD_CHI4 = BM.DEAD_CHI4
SCR_NNEG = BM.SCR_NNEG

# frozen /tmp pins
W9_QDAG = BM.W9_QDAG
W9_QDIAG = 0.48228140
W9_QOFF = 0.45076283
W9_QPOLE = 0.00068037
W9_QREG = 0.93236386
W9_GAP = 1.6752e-4
W9_QABS = 38.486
W9_CORRCOS = 0.026
SEL_QDIAG = {
    3: 0.51516909,
    4: 0.48228140,
    5: 0.89217125,
    6: 0.83450788,
    7: 2.27207887,
    9: 40.77731332,
}
SEL_QOFF = {
    3: 0.41326642,
    4: 0.45076283,
    5: -0.00080730,
    6: 0.09659630,
    7: -1.32747518,
    9: -39.81509833,
}
SEL_QPOLE = {
    3: 0.00029700,
    4: 0.00068037,
    5: 0.00272505,
    6: 0.00087949,
    7: 0.00048759,
    9: 0.00008685,
}
SEL_QREG = {
    3: 0.92813851,
    4: 0.93236386,
    5: 0.88863890,
    6: 0.93022469,
    7: 0.94411610,
    9: 0.96212814,
}
SEL_GAP = {
    3: 2.9872e-3,
    4: 1.6752e-4,
    5: 8.5993e-5,
    6: 2.7938e-6,
    7: 1.8239e-7,
    9: 1.9132e-8,
}
DEAD_POLE = {
    15: (1.02318094, 0.03795, 0.98523),
    19: (1.00430413, 0.02565, 0.97865),
    23: (1.012749, 0.03477, 0.97798),
    33: (1.017413, 0.06905, 0.94837),
    39: (1.002095, 0.09459, 0.90750),
}
DEAD20 = (1.022908, 0.03845, 0.98445)
LIVE9_QPOLE = 0.00342
LIVE9_QREG = 0.93119
QSIG_K5 = 2.103
QSIG_K9 = 87.08
Q_BAR = 5.0e-8
SPLIT_BAR = 5.0e-7
POLE_BAR = 5.0e-6
GAP_REL = 0.05
CHI_BAR = 5.0e-4
SRC_RES = 1.0e-12
RECON_BAR = 1.0e-12
CORR_BAR = 0.08
W9_TRG = BM.W9_TRG
W9_M2 = BM.W9_M2
DEAD15_TRG = BM.DEAD15_TRG

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
    return (not bad), ("NO zero/prime oracles; signed border "
                       "triple sum / C-resolvent only"
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
        if nm and any(f in nm for f in frags):
            hits.append("%s@%d" % (nm, node.lineno))
    return hits


def phi_chunked(a_mu, b_mu, h0_mu, t, Nw):
    t = np.asarray(t, float)
    n = t.size
    Phi = np.empty((Nw, n), dtype=float)
    u = np.full(n, 1.0 / math.sqrt(h0_mu))
    um = np.zeros(n)
    Phi[0] = u
    for i in range(Nw - 1):
        r = (t - a_mu[i]) * u - (b_mu[i - 1] * um if i > 0 else 0.0)
        um, u = u, r / b_mu[i]
        Phi[i + 1] = u
    return Phi


def split_q(kz, chi=None, phase=False, chunk=512):
    """Diagonal / off / pole / regular split of q^dagger.
    Consumes measure arrays + mu-chain only."""
    m = ER._measures(kz, chi=chi)
    cut = FTI.cut_rung(m["xu"], m["wu"], m["yn"], m["vn"],
                       m["Nw"], m["S"], m["L"], m["i1"], m["i2"],
                       keep=True)
    bp = ABD.border_chain_pack(
        np.asarray(m["xp"], float), np.asarray(m["wp"], float),
        np.asarray(m["yn"], float), np.asarray(m["vn"], float),
        m["bxs"], m["bws"], m["bys"], m["bvs"], m["Nw"])
    a_mu, b_mu, h0_mu = V.mu_chain(
        np.asarray(m["xp"], float), np.asarray(m["wp"], float), m["Nw"])
    bxa = np.concatenate([np.asarray(m["bxs"], float),
                          np.asarray(m["bys"], float)])
    bwa = np.concatenate([np.asarray(m["bws"], float),
                          -np.asarray(m["bvs"], float)])
    bvec = ABD.bvec_chunked(a_mu, b_mu, h0_mu, bxa, bwa, m["Nw"])
    Bm = m["Bm"]
    if Bm is None:
        Bm = V.b_matrix(a_mu, b_mu, h0_mu, m["yn"], m["vn"], m["Nw"])
    C = Bm.T @ Bm
    Nw = m["Nw"]
    I = np.eye(Nw)
    Bw = float(bp["Bw"])
    qform = float(bvec @ np.linalg.solve(I - C, bvec)) / Bw
    ce, cv = np.linalg.eigh(C)
    lmax = float(ce[-1])
    gap = 1.0 - lmax
    psi = cv[:, -1]
    q_pole = float((bvec @ psi) ** 2) / (Bw * gap)
    q_reg = qform - q_pole
    q_diag = 0.0
    recon = np.zeros(Nw)
    for s in range(0, len(bxa), chunk):
        t = bxa[s:s + chunk]
        w = bwa[s:s + chunk]
        Phi = phi_chunked(a_mu, b_mu, h0_mu, t, Nw)
        recon += Phi @ w
        Kphi = np.linalg.solve(I - C, Phi)
        quad = np.sum(Kphi * Phi, axis=0)
        q_diag += float((w * w) @ quad)
    q_diag /= Bw
    recon_res = float(np.linalg.norm(recon - bvec)
                      / (np.linalg.norm(bvec) + 1e-30))
    qabs = float(np.abs(bvec) @ np.linalg.solve(I - C, np.abs(bvec))) / Bw
    babs = ABD.bvec_chunked(a_mu, b_mu, h0_mu, bxa, np.abs(bwa), Nw)
    qsig = float(babs @ np.linalg.solve(I - C, babs)) / Bw
    corr_cos = float("nan")
    if phase:
        nx = len(m["bxs"])
        logs = np.log(np.clip(bxa[:nx], 1e-12, None))
        rng = np.random.default_rng(0)
        take = min(80, nx)
        idx = (rng.choice(nx, size=take, replace=False)
               if nx > take else np.arange(nx))
        dlog = np.abs(logs[idx][:, None] - logs[idx][None, :])
        iu = np.triu_indices(dlog.shape[0], 1)
        Phi_s = phi_chunked(a_mu, b_mu, h0_mu, bxa[idx], Nw)
        Ks = Phi_s.T @ np.linalg.solve(I - C, Phi_s)
        k_off = Ks[iu]
        d_off = dlog[iu]
        if k_off.size > 2:
            corr_cos = float(np.corrcoef(k_off, np.cos(d_off))[0, 1])
    _ = cut
    return dict(
        qform=qform, q_diag=q_diag, q_off=qform - q_diag,
        q_pole=q_pole, q_reg=q_reg, gap=gap, lmax=lmax,
        recon_res=recon_res, qabs=qabs, qsig=qsig, Bw=Bw,
        n_atoms=len(bxa), Nw=Nw, n_ge1=int(np.sum(ce >= 1.0 - 1e-12)),
        pole_share=q_pole / qform if qform != 0 else float("nan"),
        corr_cos=corr_cos, kz=kz,
    )


def spectral_only(kz, chi=None):
    """Pole/regular without Phi (dead-chi mutant, cheaper)."""
    m = ER._measures(kz, chi=chi)
    bp = ABD.border_chain_pack(
        np.asarray(m["xp"], float), np.asarray(m["wp"], float),
        np.asarray(m["yn"], float), np.asarray(m["vn"], float),
        m["bxs"], m["bws"], m["bys"], m["bvs"], m["Nw"])
    a_mu, b_mu, h0_mu = V.mu_chain(
        np.asarray(m["xp"], float), np.asarray(m["wp"], float), m["Nw"])
    bxa = np.concatenate([np.asarray(m["bxs"], float),
                          np.asarray(m["bys"], float)])
    bwa = np.concatenate([np.asarray(m["bws"], float),
                          -np.asarray(m["bvs"], float)])
    bvec = ABD.bvec_chunked(a_mu, b_mu, h0_mu, bxa, bwa, m["Nw"])
    Bm = m["Bm"]
    if Bm is None:
        Bm = V.b_matrix(a_mu, b_mu, h0_mu, m["yn"], m["vn"], m["Nw"])
    C = Bm.T @ Bm
    Bw = float(bp["Bw"])
    I = np.eye(C.shape[0])
    qform = float(bvec @ np.linalg.solve(I - C, bvec)) / Bw
    ce, cv = np.linalg.eigh(C)
    gap = 1.0 - float(ce[-1])
    psi = cv[:, -1]
    q_pole = float((bvec @ psi) ** 2) / (Bw * gap)
    return dict(qform=qform, q_pole=q_pole, q_reg=qform - q_pole,
                gap=gap, kz=kz)


def part_satz():
    section("S1  SATZ -- TRIPLE SUM AND POLE SPLIT OVER Q")
    # C = diag(1/2, 0), K = diag(2, 1)
    # atoms: phi1=(1,0) s=1; phi2=(1,1) s=1; b=(2,1); Bw=1
    q = Fr(9)
    q_diag = Fr(5)
    q_off = Fr(4)
    check("G01-Q-triple-sum",
          q == q_diag + q_off and q_diag > 0,
          "q=9 = q_diag=5 + q_off=4 (unsigned skeleton "
          "does not exhaust q)")
    # pole: C=diag(1/2,1/4), b=(1,1), Bw=1
    # K=diag(2, 4/3), q=10/3, pole=1/(1/2)=2, reg=4/3
    qp = Fr(10, 3)
    qpole = Fr(2)
    qreg = Fr(4, 3)
    check("G02-Q-pole-split",
          qp == qpole + qreg and qpole == Fr(1) / (Fr(1) - Fr(1, 2)),
          "q=10/3 = pole=2 + reg=4/3 exact")


def part_w9():
    section("S2  w9 IDENTITY + DIAG/OFF + POLE/REG")
    S = split_q(9, phase=True)
    r = ER.redheffer_of(ER._measures(9))
    check("G10-w9-triple-identity",
          abs(S["qform"] - r["qdag"]) < SRC_RES
          and abs(S["qform"] - W9_QDAG) <= 1e-8
          and S["recon_res"] < RECON_BAR
          and S["n_ge1"] == 0,
          "qform=q^d at %.2e; recon=%.2e; atoms=%d n_ge1=0"
          % (abs(S["qform"] - r["qdag"]), S["recon_res"],
             S["n_atoms"]))
    check("G11-w9-diag-pole",
          abs(S["q_diag"] - W9_QDIAG) < SPLIT_BAR
          and abs(S["q_off"] - W9_QOFF) < SPLIT_BAR
          and abs(S["q_pole"] - W9_QPOLE) < POLE_BAR
          and abs(S["q_reg"] - W9_QREG) < SPLIT_BAR
          and abs(S["gap"] - W9_GAP) / W9_GAP < GAP_REL
          and S["pole_share"] < 0.01
          and abs(S["q_diag"] + S["q_off"] - S["qform"]) < 1e-12
          and abs(S["q_pole"] + S["q_reg"] - S["qform"]) < 1e-12,
          "diag=%.8f off=%.8f pole=%.6f share=%.4f gap=%.4e"
          % (S["q_diag"], S["q_off"], S["q_pole"],
             S["pole_share"], S["gap"]))
    check("G12-w9-phase-unsigned",
          S["qabs"] > 10.0
          and abs(S["qabs"] - W9_QABS) / W9_QABS < 0.05
          and abs(S["corr_cos"]) < CORR_BAR,
          "|b|-env=%.2f; corr(K_off, cos dlog)=%.4f "
          "(not a cosine kernel)"
          % (S["qabs"], S["corr_cos"]))
    return S


def part_selected(smoke):
    section("S3  SELECTED -- DIAGONAL OVERFLOW / POLE NOT CARRIER")
    sel = SEL_SMOKE if smoke else SEL_LIVE
    rows = []
    for k, kz in sel:
        phase = (k == 4)
        S = split_q(kz, phase=phase)
        rows.append(dict(k=k, **S))
        print("    k=%d kz=%d q=%.6f diag=%.6f off=%+.6f "
              "pole=%.6f share=%.4f gap=%.3e"
              % (k, kz, S["qform"], S["q_diag"], S["q_off"],
                 S["q_pole"], S["pole_share"], S["gap"]),
              flush=True)
    check("G20-selected-split-pins",
          all(abs(row["qform"] - BM.SEL_Q[row["k"]]) < Q_BAR
              and abs(row["q_diag"] - SEL_QDIAG[row["k"]]) < SPLIT_BAR
              and abs(row["q_off"] - SEL_QOFF[row["k"]]) < SPLIT_BAR
              and abs(row["q_pole"] - SEL_QPOLE[row["k"]]) < POLE_BAR
              and abs(row["q_reg"] - SEL_QREG[row["k"]]) < SPLIT_BAR
              and abs(row["gap"] - SEL_GAP[row["k"]]) / SEL_GAP[row["k"]]
              < GAP_REL
              and row["pole_share"] < 0.01
              and row["qform"] < 1.0
              for row in rows),
          "%d/%d selected pins; all pole_share<0.01; all q<1"
          % (len(rows), len(rows)))
    mean_q = float(np.mean([row["qform"] for row in rows]))
    mean_d = float(np.mean([row["q_diag"] for row in rows]))
    mean_p = float(np.mean([row["q_pole"] for row in rows]))
    if smoke:
        check("G21-diag-overflow-skipped", True,
              "--smoke (k=3..5 still sub-1 diag; overflow is k>=7)")
        check("G22-off-loadbearing-skipped", True, "--smoke")
    else:
        r7 = next(row for row in rows if row["k"] == 7)
        r9 = next(row for row in rows if row["k"] == 9)
        check("G21-diag-overflow",
              r7["q_diag"] > 1.0 and r9["q_diag"] > 10.0
              and mean_d > 1.0,
              "k=7 q_diag=%.4f k=9 q_diag=%.2f mean_diag=%.3f >1 "
              "(unsigned skeleton cannot bound the mean)"
              % (r7["q_diag"], r9["q_diag"], mean_d))
        check("G22-off-loadbearing",
              r9["q_off"] < -10.0
              and abs(r9["q_off"] + r9["q_diag"] - r9["qform"]) < 1e-8
              and mean_p < 0.01,
              "k=9 q_off=%.2f cancels diag=%.2f down to q=%.4f; "
              "mean_pole=%.2e (pole is not the carrier)"
              % (r9["q_off"], r9["q_diag"], r9["qform"], mean_p))
    _ = mean_q
    return rows


def part_chi(smoke):
    section("S4  DEAD CHI -- POLE OVERSHOOT; DROP-POLE MUTANT")
    specs = [(kz, DMF.Q_CHI3, DMF.LPQ3, "CHI3-%d" % kz, DEAD_POLE[kz])
             for kz in DEAD_CHI3]
    specs.append((20, DMF.Q_CHI4, DMF.LPQ4, "CHI4-20", DEAD20))
    if smoke:
        specs = [specs[0], specs[-1]]
    deads = []
    n_over = 0
    n_reg_lt1 = 0
    for kz, q, lp, tag, pin in specs:
        S = spectral_only(kz, chi=(q, lp, tag))
        deads.append((tag, S))
        over = S["q_pole"] > (1.0 - S["q_reg"]) - 1e-9
        if over:
            n_over += 1
        if S["q_reg"] < 1.0:
            n_reg_lt1 += 1
        print("    %s q=%.6f pole=%.5f reg=%.6f overshoot=%s"
              % (tag, S["qform"], S["q_pole"], S["q_reg"], over),
              flush=True)
        ok_pin = (abs(S["qform"] - pin[0]) < CHI_BAR
                  and abs(S["q_pole"] - pin[1]) < 5e-4
                  and abs(S["q_reg"] - pin[2]) < CHI_BAR
                  and S["qform"] > 1.0
                  and S["q_reg"] < 1.0
                  and over)
        if not ok_pin:
            n_over = -1
    check("G30-dead-chi-pole-overshoot",
          n_over == len(deads) and n_reg_lt1 == len(deads)
          and (smoke or len(deads) == 6),
          "%d/%d dead: q>1, q_reg<1, pole > 1-q_reg "
          "(death is the pole overshoot, not bulk overflow)"
          % (len(deads), 2 if smoke else 6))
    live = spectral_only(9, chi=(DMF.Q_CHI3, DMF.LPQ3, "CHI3-9"))
    check("G31-live-chi-no-overshoot",
          live["qform"] < 1.0
          and abs(live["q_pole"] - LIVE9_QPOLE) < 5e-4
          and abs(live["q_reg"] - LIVE9_QREG) < CHI_BAR
          and live["q_pole"] < 0.01,
          "CHI3-9 q=%.6f pole=%.5f (no overshoot)"
          % (live["qform"], live["q_pole"]))
    check("G32-drop-pole-mutant",
          n_reg_lt1 == len(deads),
          "drop-pole reads q_reg<1 on every dead window "
          "(false life).  The pole is the death certificate, "
          "not the living-mean carrier")
    return deads


def part_kills(S9, rows, smoke):
    section("S5  BOUND INVENTORY + KILLS")
    # typed gate witnesses (numeric)
    check("G40-kernel-not-cosine",
          abs(S9["corr_cos"]) < CORR_BAR,
          "corr(K_off, cos dlog)=%.4f; MVT/Gallagher want a "
          "translation kernel in log n.  GATE: unconditional "
          "tools structurally inapplicable (not RH-near yet -- "
          "the kernel class is wrong)"
          % S9["corr_cos"])
    if smoke:
        check("G41-CS-sign-skipped", True, "--smoke")
        check("G42-unsigned-sigma-skipped", True, "--smoke")
    else:
        r9 = next(row for row in rows if row["k"] == 9)
        check("G41-CS-loses-sign",
              r9["q_off"] < 0 and r9["q_diag"] > 1.0
              and abs(r9["q_off"]) > 0.9 * r9["q_diag"],
              "CS between block and atoms drops the sign of "
              "q_off; at k=9 |q_off|/q_diag=%.3f (near-perfect "
              "cancellation).  GATE: unconditional, cannot close"
              % (abs(r9["q_off"]) / r9["q_diag"]))
        s5 = BM.source_q(ER._measures(17))
        s9 = BM.source_q(ER._measures(116))
        check("G42-unsigned-sigma-regression",
              s5["qsig"] > 1.5 and s9["qsig"] > 20.0
              and abs(s5["qsig"] - QSIG_K5) / QSIG_K5 < 0.05
              and abs(s9["qsig"] - QSIG_K9) / QSIG_K9 < 0.10,
              "|sigma| kz17=%.2f kz116=%.1f (r442 2.10/87 reproduced)"
              % (s5["qsig"], s9["qsig"]))
    check("G43-wrong-norm",
          S9["qform"] * S9["Bw"] > 2.0,
          "q*B_w=%.3f is not a <1 object (block-normalisation "
          "is load-bearing)"
          % (S9["qform"] * S9["Bw"]))
    p9 = MT.pack_tau(MT.tdag_main(9)[0])
    pD = BM.kappa_of(15, chi=(DMF.Q_CHI3, DMF.LPQ3, "CHI3-15"))
    check("G44-soft-r440",
          p9["trG"] > 20.0 and pD["trG"] > 20.0
          and abs(p9["trG"] - W9_TRG) / W9_TRG < 0.02
          and abs(pD["trG"] - DEAD15_TRG) / DEAD15_TRG < 0.05
          and p9["M2"] > 20.0 and pD["M2"] > 20.0,
          "trG living=%.2f dead=%.2f; M2 %.2f vs %.2f "
          "(r440: soft means blind to the collar)"
          % (p9["trG"], pD["trG"], p9["M2"], pD["M2"]))
    ps = HM.row_mz(HM.scramble_mz(), "SCR")
    check("G45-scramble",
          ps["nneg"] == SCR_NNEG,
          "scramble nneg(R)=%d (bulk already dead)"
          % ps["nneg"])
    del ps["R"]


def main():
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke

    print("=" * 78)
    print("signed_border_mean_probe -- "
          "PRIME.RDAGGER.SIGNED_BORDER_MEAN.01 (round 444)")
    print("SPEC_SHA %s" % SPEC_SHA[:16])
    print("mode: %s" % ("SMOKE" if smoke else
                        "FULL (selected k=3..7,9 + dead chi 6; "
                        "k=8 not rebuilt)"))
    print("=" * 78)

    section("S0  FIREWALL + IMPORT SHA")
    okf, det = firewall_audit()
    check("G00-firewall", okf, det)
    sha_ok = (ER.SPEC_SHA.startswith(ER_SHA_PREFIX)
              and BM.SPEC_SHA.startswith(BM_SHA_PREFIX)
              and MT.SPEC_SHA.startswith(MT_SHA_PREFIX)
              and ABD.SPEC_SHA.startswith(ABD_SHA_PREFIX)
              and DMF.SPEC_SHA.startswith(DMF_SHA_PREFIX))
    check("G00b-import-sha", sha_ok,
          "ER %s BM %s MT %s ABD %s DMF %s"
          % (ER.SPEC_SHA[:8], BM.SPEC_SHA[:8], MT.SPEC_SHA[:8],
             ABD.SPEC_SHA[:8], DMF.SPEC_SHA[:8]))
    ag = antigate_fragment_audit()
    check("G00c-no-fit", not ag,
          "no fit primitives" if not ag else "; ".join(ag))

    part_satz()
    S9 = part_w9()
    rows = part_selected(smoke)
    part_chi(smoke)
    part_kills(S9, rows, smoke)

    section("S6  VERDICT")
    prev_ok = all(ok for _n, ok in CHECKS)
    verd = ("ZIRKULAER / TRIPLE_SUM_EXACT / POLE_NOT_CARRIER / "
            "DIAGONAL_OVERFLOWS / OFFDIAG_LOADBEARING / "
            "DEAD_CHI_POLE_OVERSHOOT")
    check("G50-verdict",
          prev_ok,
          verd + ".  Missing signed strength: regular "
          "off-diagonal cancellation matching q_diag growth, "
          "against a window-dependent OP kernel (not "
          "k(log n/n')).  Second circularity after r399.  "
          "no RH / L* / R-dagger")

    n_fail = sum(1 for _n, ok in CHECKS if not ok)
    n_ok = len(CHECKS) - n_fail
    print("\nRESULT: %d/%d gates PASS   SPEC_SHA %s   (%.1fs)  %s" % (
        n_ok, len(CHECKS), SPEC_SHA[:16], time.time() - T0, verd))
    if n_fail == 0:
        print("SIGNED BORDER MEAN %sVERIFIED" % ("SMOKE " if smoke else ""))
        return 0
    print("SIGNED BORDER MEAN FAILED %d" % n_fail)
    return 1


if __name__ == "__main__":
    sys.exit(main())
