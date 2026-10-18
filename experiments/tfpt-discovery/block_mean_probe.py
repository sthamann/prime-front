#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""block_mean_probe -- PRIME.RDAGGER.UNCONDITIONAL_BLOCK_MEAN.01
(round 442): the block mean of kappa^dagger as a
frequency of q^dagger > 1 (reviewer-R439, the
unconditional-mean lane after r440).

THE LEMMA (exactly one).  On the r409/r433
construction,
    kappa^dagger = 1{q^dagger > 1}
hence
    (1/K) sum kappa^dagger = (1/K) sum 1{q^dagger > 1}.
r440 T1/T2/MI2 + r430 exists_index_zero_of_block_mean_lt_one
then turn liminf of that frequency < 1 into infinitely
many index-0 windows.  This round PROVES the dictionary
(finite algebra + machine census) and REDUCES the
analytic question to a bound on that frequency.  It
does NOT claim the bound.

COLLAR DECOMPOSITION.  r440: a fixed circle |s-1/2|=0.40
winds 0 on every living window (interior (0.10,0.90)
empty).  So kappa^dagger is entirely the collar
correction -- which side of s=1 the one collar zero
sits on.  r433: that side is sign(delta)=sign(1-q^dagger).
Hence kappa^dagger = 1{q^dagger > 1}.

SOURCE FORM.  q^dagger = gamma + v^T (I-BB^T)^{-1} v
= (1/B_w) b^T (I-C)^{-1} b with C = B^T B, gamma =
||b||^2/B_w, b the mu-OP coefficient of the signed
border measure sigma (r420/r424).  As a double sum
over border atoms,
    q^dagger = sum_{a,a'} (sigma_a sigma_{a'}/B_w)
               <phi(t_a),(I-C)^{-1} phi(t_{a'})>.
Selected anchors a_k = 2^k are zeta-windows: the
atoms include primes in dyadic ranges.

GATE.  The unsigned |b| envelope is >>1 (w9: 38.5).
The unsigned |sigma| envelope already exceeds 1 on
k>=5 (kz17: 2.10; kz116: 87).  A positive
Chebyshev/Mertens majorant does NOT give q^dagger<1.
The remaining bound needs signed cancellation.
RH-quality prime-error on that oscillatory sum is
the circularity gate (forbidden).  PNT controls the
main term of Lambda but not the signed pairing
against (I-C)^{-1}.  Unconditional-positive: REFUTED.
Signed-oscillatory bound: OPEN.

CALIBRATION DISCLOSURE.  Dictionary, q^dagger trend,
source residual, unsigned envelopes, core-42 q-only,
dead/live chi first measured in /tmp (r442_cal.py,
r442_cal2.py) on the r433/r440 constructors,
2026-08-30.  Frozen floors below are that
measurement, sealed as gates.  Pins disclosed.
Builder fallback NOT taken: full wall << 120 s
(no k=8 rebuild; r421 pin unused).

FROZEN FROM /tmp (live re-gated, not fitted):
  * SATZ Q: delta = 187/450, q^dagger = 263/450,
    1-q^dagger = -sch.
  * SATZ w9: kappa=0, q^dagger=0.933044234,
    source residual 1.2e-15; |1-q+sch|=9.5e-13.
  * Selected k=3,4,5,6,7,9 q^dagger
    0.92843551, 0.93304423, 0.89136395,
    0.93110418, 0.94460369, 0.96221499;
    ALL <1, mean 0.931794; kappa=0 on 6/6.
    Trend is NOT falling: dip at k=5 then rise
    toward 1 (k=9: 0.962).  Markov room 0.068.
  * EXT-6: all q^dagger<1, mean 0.964278, kappa=0.
  * Core-42 q-only: 42/42 q^dagger<1, mean 0.961083,
    min 0.908091 (kz22), max 0.998490 (kz16);
    four near-threshold (kz12/15/16/21 > 0.99)
    still living.  NO dead Selected window.
  * Dead chi 6/6 q^dagger>1 and kappa=1
    (CHI3-15/19/23/33/39 + CHI4-20).
    Living CHI3-9 q^dagger=0.934613 kappa=0.
  * Unsigned |b| envelope w9 = 38.49 >>1.
    Unsigned |sigma| kz17 = 2.10, kz116 = 87.08.
  * MI2 on {w9,kz5}: 4e-15 (r440 identity).
  * Soft: trG 50.89 vs 53.04; M2 32.96 vs 39.01.

AUSGANG REDUZIERT / DICTIONARY_EXACT /
UNSIGNED_MAJORANT_REFUTED / SELECTED_POINTWISE_CENSUS /
MEAN_BOUND_OPEN.
SATZ: the one lemma (kappa^dagger = 1{q^dagger>1}
and the frequency identity).  REFUTED: unsigned
Chebyshev/Mertens as a <1 majorant.  CENSUS:
Selected+EXT+core-42 all living (pointwise q^dagger<1);
q^dagger rises toward 1 at the deep end.  OPEN: an
unconditional signed bound that keeps the frequency
<1 cofinally.  No RH claim.

MACHINERY: r433 ER.redheffer_of / _measures /
mixed_toy_blocks, r440 MT.tdag_main / pack_tau /
winding_*, r420/r424 ABD.bvec_chunked / border_chain,
r226 V.admissible_indices, r430 Lean landing site
(not proved here).

NO RH CLAIM.  One finite lemma, a named unsigned
refutation, a named census, named kills.  Research
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
import mean_tau_index_probe as MT  # noqa: E402
import dirichlet_matched_frame_probe as DMF  # noqa: E402
import verify_lstar_instance as V  # noqa: E402
import edge_signature_probe as ES  # noqa: E402
import augmented_borodin_duality_probe as ABD  # noqa: E402
import final_two_rank_inertia_probe as FTI  # noqa: E402
import pair_extremal_probe as PX  # noqa: E402
import high_moment_inertia_probe as HM  # noqa: E402
import borodin_birkhoff_intertwiner_probe as B  # noqa: E402

ER_SHA_PREFIX = "8371b954"
MT_SHA_PREFIX = "3807189a"
ABD_SHA_PREFIX = "7d810a9a"
DMF_SHA_PREFIX = "4bf1a94b"
ES_SHA_PREFIX = "395673f2"

SEL_LIVE = ((3, 5), (4, 9), (5, 17), (6, 26), (7, 43), (9, 116))
SEL_SMOKE = ((3, 5), (4, 9), (5, 17))
DEAD_CHI3 = (15, 19, 23, 33, 39)
DEAD_CHI4 = (20,)
SCR_NNEG = 21

W9_QDAG = 0.933044234
W9_TRG = 50.894597
W9_M2 = 32.96
DEAD15_QDAG = 1.02318094
DEAD15_TRG = 53.04
DEAD15_M2 = 39.01
LIVE9_QDAG = 0.93461344
SEL_Q = {
    3: 0.92843551,
    4: 0.93304423,
    5: 0.89136395,
    6: 0.93110418,
    7: 0.94460369,
    9: 0.96221499,
}
SEL_MEAN = 0.93179442
EXT_MEAN = 0.96427792
CORE_MEAN = 0.961083
CORE_MIN = 0.908091
CORE_MAX = 0.998490
QABS_W9 = 38.48
QSIG_K5 = 2.10
QSIG_K9 = 87.0
SRC_RES = 1.0e-12
ID_RES = 2.0e-7
Q_BAR = 5.0e-8
MI2_BAR = 1.0e-10

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
    return (not bad), ("NO zero/prime oracles; T^dagger Gram / "
                       "q^dagger Redheffer / signed border only"
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


def source_q(m):
    cut = FTI.cut_rung(m["xu"], m["wu"], m["yn"], m["vn"],
                       m["Nw"], m["S"], m["L"], m["i1"], m["i2"],
                       keep=True)
    bp = ABD.border_chain_pack(
        np.asarray(m["xp"], float), np.asarray(m["wp"], float),
        np.asarray(m["yn"], float), np.asarray(m["vn"], float),
        m["bxs"], m["bws"], m["bys"], m["bvs"], m["Nw"])
    if not bp.get("ok"):
        return None
    a_mu, b_mu, h0_mu = V.mu_chain(np.asarray(m["xp"], float),
                                  np.asarray(m["wp"], float), m["Nw"])
    bxa = np.concatenate([np.asarray(m["bxs"], float),
                          np.asarray(m["bys"], float)])
    bwa = np.concatenate([np.asarray(m["bws"], float),
                          -np.asarray(m["bvs"], float)])
    bvec = ABD.bvec_chunked(a_mu, b_mu, h0_mu, bxa, bwa, m["Nw"])
    Bw = float(bp["Bw"])
    Bm = m["Bm"]
    if Bm is None:
        Bm = V.b_matrix(a_mu, b_mu, h0_mu, m["yn"], m["vn"], m["Nw"])
    C = Bm.T @ Bm
    I = np.eye(C.shape[0])
    qform = float(bvec @ np.linalg.solve(I - C, bvec)) / Bw
    gam = float(bvec @ bvec) / Bw
    v = Bm @ (bvec / math.sqrt(Bw))
    En = Bm @ Bm.T
    qsplit = gam + float(v @ np.linalg.solve(
        np.eye(En.shape[0]) - En, v))
    qabs = float(np.abs(bvec) @ np.linalg.solve(I - C, np.abs(bvec))) / Bw
    babs = ABD.bvec_chunked(a_mu, b_mu, h0_mu, bxa, np.abs(bwa), m["Nw"])
    qsig = float(babs @ np.linalg.solve(I - C, babs)) / Bw
    _ = cut
    return dict(qform=qform, qsplit=qsplit, gam=gam, qabs=qabs,
                qsig=qsig, Bw=Bw, n_atoms=len(bxa))


def kappa_of(kz, chi=None):
    if chi is None:
        td, _mz = MT.tdag_main(kz)
        return MT.pack_tau(td)
    q, lp, _tag = chi
    mzc, dsmc = B.chi_border_rung(kz, q, lp)
    return MT.pack_tau(B.source_Tdag(mzc, dsmc))


def part_satz():
    section("S1  LEMMA -- kappa^dagger = 1{q^dagger > 1} OVER Q")
    T = ER.mixed_toy_blocks()
    qQ = Fr(263, 450)
    dlt = Fr(187, 450)
    check("G01-Q-dictionary",
          T["sch"] == -dlt and (Fr(1) - qQ) == -T["sch"]
          and qQ < 1 and dlt > 0,
          "q^d=263/450<1; delta=187/450=-sch")
    check("G02-Q-living",
          qQ < 1,
          "toy last pivot living (kappa-pred=0)")


def part_w9():
    section("S2  w9 THREE-WAY + SOURCE DOUBLE SUM")
    p = kappa_of(9)
    m = ER._measures(9)
    r = ER.redheffer_of(m)
    src = source_q(m)
    pred = int(r["qdag"] > 1.0 + 1e-12)
    check("G10-w9-dictionary",
          p["kappa_G"] == 0 and p["nzeros01"] == 0
          and pred == 0
          and abs(r["qdag"] - W9_QDAG) <= 1e-8
          and abs(r["delta"] + r["sch"]) < ID_RES,
          "kappa=nzeros=1{q>1}=0; q^d=%.10f; |1-q+sch|=%.2e"
          % (r["qdag"], abs(r["delta"] + r["sch"])))
    check("G11-w9-source-form",
          src is not None
          and abs(src["qform"] - r["qdag"]) < SRC_RES
          and abs(src["qsplit"] - r["qdag"]) < SRC_RES,
          "qform=qsplit=q^d at %.2e / %.2e; atoms=%d"
          % (abs(src["qform"] - r["qdag"]),
             abs(src["qsplit"] - r["qdag"]), src["n_atoms"]))
    return p, r, src


def part_census(smoke):
    section("S3  SELECTED / EXT / CORE -- q^dagger TREND")
    sel = SEL_SMOKE if smoke else SEL_LIVE
    rows = []
    for k, kz in sel:
        r = ER.redheffer_of(ER._measures(kz))
        p = kappa_of(kz)
        rows.append(dict(k=k, kz=kz, q=r["qdag"], dlt=r["delta"],
                         kappa=p["kappa_G"], G=p["G"], n=p["n"]))
        print("    k=%d kz=%d n=%d kappa=%d q^d=%.8f delta=%+.6f"
              % (k, kz, p["n"], p["kappa_G"], r["qdag"], r["delta"]),
              flush=True)
    check("G20-selected-dictionary",
          all(row["kappa"] == int(row["q"] > 1.0 + 1e-12)
              and row["kappa"] == 0
              and abs(row["q"] - SEL_Q[row["k"]]) < Q_BAR
              for row in rows),
          "%d/%d selected kappa=1{q>1}=0; pins match"
          % (len(rows), len(rows)))
    mean_q = float(np.mean([row["q"] for row in rows]))
    pin_mean = float(np.mean([SEL_Q[row["k"]] for row in rows]))
    check("G21-selected-mean-lt1",
          mean_q < 1.0 and all(row["q"] < 1.0 for row in rows)
          and abs(mean_q - pin_mean) < 1e-7,
          "mean q^d=%.8f <1 (Markov room %.4f); NOT falling "
          "(k=5 dip then rise to k=9)"
          % (mean_q, 1.0 - mean_q))
    if smoke:
        check("G22-EXT-skipped", True, "--smoke")
        check("G23-core-skipped", True, "--smoke")
        return rows
    ext = []
    for kz in ES.SAMPLE_EXT:
        r = ER.redheffer_of(ER._measures(kz))
        ext.append(r["qdag"])
        print("    EXT-%d q^d=%.8f delta=%+.6f"
              % (kz, r["qdag"], r["delta"]), flush=True)
    check("G22-EXT-living",
          all(q < 1.0 for q in ext) and len(ext) == 6
          and abs(float(np.mean(ext)) - EXT_MEAN) < 5e-7,
          "EXT 6/6 q^d<1; mean=%.6f" % float(np.mean(ext)))
    core_q = []
    n_dead = 0
    n_near = 0
    for kz in V.admissible_indices():
        r = ER.redheffer_of(ER._measures(kz))
        core_q.append(r["qdag"])
        if r["qdag"] > 1.0:
            n_dead += 1
        if r["qdag"] > 0.99:
            n_near += 1
    mq = float(np.mean(core_q))
    check("G23-core-pointwise-living",
          n_dead == 0 and len(core_q) == 42
          and abs(mq - CORE_MEAN) < 5e-6
          and abs(min(core_q) - CORE_MIN) < 5e-6
          and abs(max(core_q) - CORE_MAX) < 5e-6
          and n_near == 4,
          "core 42/42 q^d<1; mean=%.6f min=%.6f max=%.6f "
          "near>0.99: %d (still living)"
          % (mq, min(core_q), max(core_q), n_near))
    return rows


def part_chi(smoke):
    section("S4  CHI -- DEAD q^d>1 IS kappa=1")
    specs = [(kz, DMF.Q_CHI3, DMF.LPQ3, "CHI3-%d" % kz)
             for kz in DEAD_CHI3]
    specs.append((20, DMF.Q_CHI4, DMF.LPQ4, "CHI4-20"))
    if smoke:
        specs = [specs[0], specs[-1]]
    deads = []
    for kz, q, lp, tag in specs:
        r = ER.redheffer_of(ER._measures(kz, chi=(q, lp, tag)))
        p = kappa_of(kz, chi=(q, lp, tag))
        deads.append((tag, r["qdag"], p["kappa_G"]))
        print("    %s kappa=%d q^d=%.8f"
              % (tag, p["kappa_G"], r["qdag"]), flush=True)
    check("G30-dead-chi-dictionary",
          all(kap == 1 and qv > 1.0 for _t, qv, kap in deads)
          and (smoke or len(deads) == 6),
          "%d/%d dead chi kappa=1{q>1}=1"
          % (len(deads), 2 if smoke else 6))
    live = ER.redheffer_of(ER._measures(
        9, chi=(DMF.Q_CHI3, DMF.LPQ3, "CHI3-9")))
    pl = kappa_of(9, chi=(DMF.Q_CHI3, DMF.LPQ3, "CHI3-9"))
    check("G31-live-chi",
          pl["kappa_G"] == 0 and live["qdag"] < 1.0
          and abs(live["qdag"] - LIVE9_QDAG) < Q_BAR,
          "CHI3-9 kappa=0 q^d=%.8f" % live["qdag"])
    return deads


def part_kills(p9, src, rows, smoke):
    section("S5  KILLS -- unsigned majorant / soft / MI2 / scramble")
    check("G40-unsigned-b-envelope",
          src["qabs"] > 10.0
          and abs(src["qabs"] - QABS_W9) / QABS_W9 < 0.05,
          "|b|-envelope w9=%.2f >>1 (positive majorant dead)"
          % src["qabs"])
    if smoke:
        check("G41-unsigned-sigma-skipped", True, "--smoke")
    else:
        m5 = ER._measures(17)
        s5 = source_q(m5)
        m9 = ER._measures(116)
        s9 = source_q(m9)
        check("G41-unsigned-sigma-envelope",
              s5["qsig"] > 1.5 and s9["qsig"] > 20.0
              and abs(s5["qsig"] - QSIG_K5) / QSIG_K5 < 0.05
              and abs(s9["qsig"] - QSIG_K9) / QSIG_K9 < 0.10,
              "|sigma|-envelope kz17=%.2f kz116=%.1f >>1 "
              "(Chebyshev/Mertens unsigned FAILS; signed "
              "cancellation is load-bearing)"
              % (s5["qsig"], s9["qsig"]))
    pD = kappa_of(15, chi=(DMF.Q_CHI3, DMF.LPQ3, "CHI3-15"))
    check("G42-soft-mutants",
          p9["trG"] > 20.0 and pD["trG"] > 20.0
          and abs(p9["trG"] - W9_TRG) / W9_TRG < 0.02
          and abs(pD["trG"] - DEAD15_TRG) / DEAD15_TRG < 0.05
          and p9["M2"] > 20.0 and pD["M2"] > 20.0,
          "trG living=%.2f dead=%.2f; M2 %.2f vs %.2f "
          "(r398: 1/2-cluster blinds moments)"
          % (p9["trG"], pD["trG"], p9["M2"], pD["M2"]))
    G9 = p9["G"]
    G3 = rows[0]["G"]
    w1 = MT.winding_circle(G9, 0.5, 0.40, n=64)
    w2 = MT.winding_circle(G3, 0.5, 0.40, n=64)
    wm = MT.winding_mean([G9, G3], 0.5, 0.40, n=64)
    check("G43-MI2-block",
          abs(wm - 0.5 * (w1 + w2)) < MI2_BAR
          and abs(w1.real) < 5e-3 and abs(w2.real) < 5e-3,
          "MI2 residual %.2e; fixed r=0.40 winds 0 "
          "(collar carries all of kappa)"
          % abs(wm - 0.5 * (w1 + w2)))
    ps = HM.row_mz(HM.scramble_mz(), "SCR")
    check("G44-scramble-circularity",
          ps["nneg"] == SCR_NNEG,
          "scramble nneg(R)=%d (bulk already dead).  "
          "Circularity: pointwise X^eps is not a mean carrier"
          % ps["nneg"])
    del ps["R"]


def main():
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke

    print("=" * 78)
    print("block_mean_probe -- "
          "PRIME.RDAGGER.UNCONDITIONAL_BLOCK_MEAN.01 (round 442)")
    print("SPEC_SHA %s" % SPEC_SHA[:16])
    print("mode: %s" % ("SMOKE" if smoke else
                        "FULL (selected k=3..7,9 + EXT-6 + "
                        "core-42 q-only; k=8 not rebuilt)"))
    print("=" * 78)

    section("S0  FIREWALL + IMPORT SHA")
    okf, det = firewall_audit()
    check("G00-firewall", okf, det)
    sha_ok = (ER.SPEC_SHA.startswith(ER_SHA_PREFIX)
              and MT.SPEC_SHA.startswith(MT_SHA_PREFIX)
              and ABD.SPEC_SHA.startswith(ABD_SHA_PREFIX)
              and DMF.SPEC_SHA.startswith(DMF_SHA_PREFIX)
              and ES.SPEC_SHA.startswith(ES_SHA_PREFIX))
    check("G00b-import-sha", sha_ok,
          "ER %s MT %s ABD %s DMF %s ES %s"
          % (ER.SPEC_SHA[:8], MT.SPEC_SHA[:8], ABD.SPEC_SHA[:8],
             DMF.SPEC_SHA[:8], ES.SPEC_SHA[:8]))
    ag = antigate_fragment_audit()
    check("G00c-no-fit", not ag,
          "no fit primitives" if not ag else "; ".join(ag))

    part_satz()
    p9, _r9, src = part_w9()
    rows = part_census(smoke)
    part_chi(smoke)
    part_kills(p9, src, rows, smoke)

    section("S6  VERDICT")
    prev_ok = all(ok for _n, ok in CHECKS)
    check("G50-verdict",
          prev_ok,
          "REDUZIERT / DICTIONARY_EXACT / "
          "UNSIGNED_MAJORANT_REFUTED / "
          "SELECTED_POINTWISE_CENSUS / MEAN_BOUND_OPEN.  "
          "no RH / L* / R-dagger")

    n_fail = sum(1 for _n, ok in CHECKS if not ok)
    n_ok = len(CHECKS) - n_fail
    verd = ("REDUZIERT / DICTIONARY_EXACT / "
            "UNSIGNED_MAJORANT_REFUTED / "
            "SELECTED_POINTWISE_CENSUS / MEAN_BOUND_OPEN")
    print("\nRESULT: %d/%d gates PASS   SPEC_SHA %s   (%.1fs)  %s" % (
        n_ok, len(CHECKS), SPEC_SHA[:16], time.time() - T0, verd))
    if n_fail == 0:
        print("BLOCK MEAN %sVERIFIED" % ("SMOKE " if smoke else ""))
        return 0
    print("BLOCK MEAN FAILED %d" % n_fail)
    return 1


if __name__ == "__main__":
    sys.exit(main())
