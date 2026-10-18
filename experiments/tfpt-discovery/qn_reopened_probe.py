#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""qn_reopened_probe -- PRIME.TERMINAL.QN_REOPENED.01
(round 428): q_N < 1 cofinally on the selected
sequence a_k=2^k, with the four death coordinates
reopened after the lemma-hydra freeze.

THE OBJECT.  The edge chain proved the R-dagger
edge half equivalent to q_N<1 (the original
terminal hole).  New arsenal since the freeze:
(1) four candidate death coordinates
q_N>1 / |Z_loc|>=M / sch>0 / razor-overlap
1e-4 vs 1e-8 (r422); (2) COMPOSE-
{S_F<=R0 D, L1<=Lambda, |Z_loc|<=Z0<M, M3<=phi}
=> q_N<1 (r378/r383/r386); (3) m0 log-complete;
(4) the selected sequence as the minimal
quantifier W_k = W^R(2^k,...).

CALIBRATION DISCLOSURE.  Prime-power map k->kz,
four-coordinate census on selected k=3..9
(except k=8), COMPOSE envelopes, signed overlap
vs hole-Nyquist, P1/VAC razor split on core-42,
dead chi, scramble, false-anchor kz=16, two-period
and depth mutant first measured in /tmp
(r428_cal.py, r428_cal2.py) on the r421/r422
constructors, 2026-08-29.  Frozen floors below
are that measurement, sealed as gates.  Pins
disclosed.  Builder fallback TAKEN for k=8:
r421 pin (N=5690, wall 226 s), not re-gated live.

FROZEN FROM /tmp (live re-gated except k=8):
  * MAP: a_k=2^k is the kz-th prime power
    (k=3..9 -> kz=5,9,17,26,43,69,116).
  * SELECTED q_N: 0.3828, 0.2143, 0.0228,
    0.00176, 0.00151, (k=8 pinned), 0.00070.
    Min margin to 1 is 0.617 at k=3 -- vs the
    42er min-margin 0.0195 at kz=16.
    Falling in k; not monotone in N
    (k=5 N=96 < k=4 N=184).
  * COMPOSE on selected: R in [0.60, 1.40] << 4;
    L1 in [0.31, 0.63] << 3; |Z_loc| max 0.4868
    at k=3 << Z0'=0.84 and M=0.845.
    Z0_sel=1/2 is TIGHT at k=3 (margin 0.013).
  * sch: all selected sch<0, |sch| in
    [0.0378, 0.1086], floor direction of r421.
  * OVERLAP NOT GLOBAL: P1 living razor share
    up to 3.6e-2 (w9 1.0e-2) OVERLAPS dead chi
    (1.5e-4..2.4e-2).  VAC living core max
    2.9e-7 vs dead-VAC chi >= 1.5e-4 -- the
    r422 four-order separator is VAC-RESTRICTED.
    kz=16 (42er razor, q_N=0.9805, |Z_loc|=0.756,
    sch=-0.00151) has razor 5.4e-9: overlap does
    NOT grade near-death.
  * NYQUIST FACE REFUTED on VAC: k=6
    nyq_cos=-0.007 while P1 w9 nyq_cos=-0.386
    (r410 number).  Living VAC s·nyq stays
    O(1e-2); the 1e-8 is orthogonality to an
    implicit C_min mode, not to Nyquist.
  * DEAD chi: q_N>1, sch>0, |Z_loc|>M on
    CHI3-15/23 and CHI4-20 (death channel).
  * SCRAMBLE w9: q_N=0.270 living; |Z_loc|=0.524
    EXCEEDS Z0_sel=1/2 (named kill of that
    constant off MAIN).  Two-period nnegA0=4.
    Depth n+1 moves C_min 0.857 -> 1.000.

AUSGANG SELECTED_MARGIN_GO / OVERLAP_VAC_ONLY /
ZLOC_WINS / COFINAL_OPEN.
SATZ: the r263 dictionary q_N=(7/5)Z^2 and
the r378 COMPOSE implication (imported).
REFUTED: razor-overlap as a global fourth
equivalent death coordinate; Nyquist as the
C_min face on VAC.
REDUZIERT: cofinal q_N<1 on selected is a
comfortable census (margin 0.617 vs 0.0195);
the sharpest remaining sublemma is
|Z_loc(W_k)| <= 1/2 on MAIN selected
(k=3 tight).  Does not move the mincut.
No RH claim.

MACHINERY: r420 den_pack, r422 occ_spec,
r417 chart, r386 row2, r421 selected map.

NO RH CLAIM.  Finite identities, a named
refutation of global overlap-equivalence, a
named selected census.  Research documentation,
not a theorem of RH.  No L* claim.
No R-dagger claim.
Sealed gates: 19/19 smoke / 23/23 full
(G00--G03, G10--G14, G20--G26, G30--G33, G50).
Companion verifier 6/6 QN REOPENED VERIFIED.
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

import cj_sigma_probe as S420  # noqa: E402
import sigma_limit_probe as S422  # noqa: E402
import reserve_limit_probe as S421  # noqa: E402
import gamma_chain_probe as S424  # noqa: E402
import edge_signature_probe as ES  # noqa: E402
import source_sch_sign_probe as S417  # noqa: E402
import compose_premises2_probe as C2  # noqa: E402
import dual_intertwiner_probe as DI  # noqa: E402
import high_moment_inertia_probe as HM  # noqa: E402
import pair_extremal_probe as PX  # noqa: E402
import dirichlet_matched_frame_probe as DMF  # noqa: E402
import final_two_rank_inertia_probe as FTI  # noqa: E402
import verify_lstar_instance as V  # noqa: E402
import bordered_hankel_probe as BH  # noqa: E402

ES_SHA_PREFIX = "395673f2"
S417_SHA_PREFIX = "f2905f2a"
S420_SHA_PREFIX = "46409e2f"
S421_SHA_PREFIX = "234a1113"
S422_SHA_PREFIX = "d81fc5fc"
S424_SHA_PREFIX = "0c85977b"
C2_SHA_PREFIX = "82d07e56"
HM_SHA_PREFIX = "bb1dcf6a"
FTI_SHA_PREFIX = "e0d79840"
DMF_SHA_PREFIX = "4bf1a94b"
DI_SHA_PREFIX = "2ee74c59"

FLOOR = ES.FLOOR
M_W = C2.M_W
Z0P = C2.Z0P
R0 = 4.0
LAMBDA = 3.0
Z0_SEL = 0.5
CORE_N = 42
SCR_NNEG = ES.SCR_NNEG
TP21_NNEG = ES.TP21_NNEG

SEL_LIVE = ((3, 5), (4, 9), (5, 17), (6, 26), (7, 43), (9, 116))
K8_PIN = dict(k=8, kz=69, Nw=5690, den=1.56855,
              Sig=0.38382, reserve=0.04763, P1=True)

W9_QN, W9_SCH, W9_RAZ = 0.21425, -0.06696, 1.012e-2
W9_ZLOC, W9_R, W9_L1 = 0.15721, 1.3961, 0.4038
K5_QN, K5_SCH = 0.02284, -0.10864
K6_QN, K6_RAZ, K6_ZLOC = 0.00176, 1.186e-8, 0.01098
K3_QN, K3_ZLOC = 0.38279, 0.48685
K9_QN, K9_ZLOC = 0.00070, 0.07630
KZ16_QN, KZ16_ZLOC, KZ16_SCH = 0.98050, 0.75567, -0.00151
KZ16_RAZ = 5.390e-9
DEAD15_QN, DEAD23_QN = 1.277, 1.206
DEAD15_ZLOC, DEAD23_RAZ = 1.021, 5.745e-4
SCR_QN, SCR_ZLOC = 0.2696, 0.5236
CORE_QN_HI, CORE_MARGIN = 0.98050, 0.01950
P1_RAZ_HI, VAC_RAZ_HI = 4.0e-2, 4.0e-7
DEAD_VAC_RAZ_LO = 1.0e-4
REL = 5.0e-3
NYQ_P1_ABS, NYQ_VAC_ABS = 0.25, 0.05

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
    return (not bad), ("NO zero/prime oracles; selected "
                       "census / four coordinates only"
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


def dict_Q():
    """q_N = (7/5) Z^2  iff  q_N<1 <=> |Z|<M."""
    Z = Fr(1, 2)
    q = Fr(7, 5) * Z * Z
    M2 = Fr(5, 7)
    return dict(Z=Z, q=q, lt=Z * Z < M2, q_lt=q < Fr(1),
                z0=Fr(1, 2), z0_lt_M=(Fr(1, 4) < M2))


def orth_Q():
    """living model e1 perp e2; dead model not."""
    e1, e2 = (Fr(1), Fr(0)), (Fr(0), Fr(1))
    live = e1[0] * e2[0] + e1[1] * e2[1]
    dead = Fr(1) * Fr(0) + Fr(1) * Fr(1)
    ratio = Fr(1, 10 ** 4) / Fr(1, 10 ** 8)
    return dict(live=live, dead=dead, ratio=ratio)


def pp_kz(k):
    a = 2 ** k
    kz = int(np.searchsorted(V.U, math.log(a) - 1e-12, side="left"))
    return kz, a, float(math.exp(float(V.U[kz])))


def four_pack(kz, compose=False):
    d = S420.den_pack(kz)
    p = ES.main_row(kz)
    out = dict(
        kz=kz, Nw=int(d["Nw"]), qN=float(d["qN"]),
        sch=float(p["sch"]), razor=float(d["razor_share"]),
        P1=bool(d["P1"]), s2=float(d["s2"]),
    )
    if compose:
        r = C2.row2(BH.wpack(kz), with_gram=True)
        out.update(
            absZloc=r["absZloc"], absZ=r["absZ"],
            R=r["R"], L1=r["L1"], M3=r.get("M3", float("nan")),
            qN_c=r["qN"], dict_dev=r["dict_dev"],
            living=r["living"],
        )
    return out


def nyquist_cos(kz):
    """<psi_Cmin, v_Nyq> on theta-sorted holes."""
    R = PX.build_rung(kz)
    mz = R["mz"]
    Cmat, _ = DI.chain_C(mz)
    _ev, WC = np.linalg.eigh(Cmat)
    psi = WC[:, 0]
    yn = np.asarray(mz["yn"], float)
    th = np.arccos(np.clip(yn, -1.0, 1.0))
    oo = np.argsort(th)
    N = len(oo)
    v = np.exp(2j * math.pi * (N // 2) * np.arange(N) / N).real
    v = v / (np.linalg.norm(v) + 1e-30)
    vnq = np.zeros(N)
    vnq[oo] = v
    if psi.size != N:
        return float("nan")
    return float(psi @ vnq)


def part_satz():
    section("S1  LEG C -- DICTIONARY / Z0 / ORTHOGONALITY OVER Q")
    t = dict_Q()
    check("G01-dictionary-Q",
          t["q"] == Fr(7, 20) and t["lt"] and t["q_lt"],
          "Z=1/2 => q_N=7/20<1 iff Z^2<5/7")
    check("G02-Z0sel-lt-M-Q",
          t["z0_lt_M"] and t["z0"] == Fr(1, 2),
          "Z0_sel=1/2, (1/2)^2=1/4 < 5/7=M^2")
    o = orth_Q()
    check("G03-orth-Q",
          o["live"] == Fr(0) and o["dead"] == Fr(1)
          and o["ratio"] == Fr(10000),
          "living inner=0; dead=1; 1e-4/1e-8=10^4")


def part_pins():
    section("S2  FLAGSHIP PINS -- w9 / k=5 / k=6 VAC / map")
    kz4, a4, rec4 = pp_kz(4)
    kz5, _a5, _r5 = pp_kz(5)
    kz6, _a6, _r6 = pp_kz(6)
    check("G10-pp-map",
          kz4 == 9 and a4 == 16 and abs(rec4 - 16.0) <= 1e-9
          and kz5 == 17 and kz6 == 26,
          "k=4->kz9 (2^4=16); k=5->17; k=6->26")
    w = four_pack(9, compose=True)
    check("G11-w9-four",
          abs(w["qN"] - W9_QN) <= 0.001
          and abs(w["sch"] - W9_SCH) <= 0.001
          and abs(w["razor"] / W9_RAZ - 1.0) <= 0.15
          and abs(w["absZloc"] - W9_ZLOC) <= 0.002
          and w["R"] <= R0 and w["L1"] <= LAMBDA
          and w["absZloc"] < Z0_SEL < M_W
          and w["qN"] < 1 and w["sch"] < 0 and w["P1"]
          and w["dict_dev"] < 1e-12,
          "qN=%.4f sch=%+.4f raz=%.2e |Zloc|=%.4f R=%.3f L1=%.3f"
          % (w["qN"], w["sch"], w["razor"], w["absZloc"],
             w["R"], w["L1"]))
    k5 = four_pack(17, compose=True)
    check("G12-k5",
          abs(k5["qN"] - K5_QN) <= 0.001
          and abs(k5["sch"] - K5_SCH) <= 0.002
          and k5["qN"] < 0.03 and k5["sch"] < 0
          and k5["absZloc"] < Z0_SEL and k5["P1"],
          "qN=%.4f sch=%+.4f |Zloc|=%.4f P1"
          % (k5["qN"], k5["sch"], k5["absZloc"]))
    k6 = four_pack(26, compose=True)
    check("G13-k6-VAC-overlap",
          abs(k6["qN"] - K6_QN) <= 0.0005
          and k6["razor"] <= 1e-6
          and abs(k6["absZloc"] - K6_ZLOC) <= 0.002
          and (not k6["P1"]) and k6["sch"] < 0
          and k6["qN"] < 0.003,
          "VAC qN=%.5f raz=%.2e |Zloc|=%.4f (1e-8 class)"
          % (k6["qN"], k6["razor"], k6["absZloc"]))
    c_p1 = nyquist_cos(9)
    c_vac = nyquist_cos(26)
    check("G14-nyquist-face-VAC-refuted",
          abs(c_p1) >= NYQ_P1_ABS and abs(c_vac) <= NYQ_VAC_ABS,
          "w9 nyq_cos=%.3f (P1 has a Nyquist face); "
          "k=6 nyq_cos=%.3f (VAC C_min is NOT Nyquist)"
          % (c_p1, c_vac))
    return w, k5, k6


def part_kills():
    section("S3  LEG D -- DEAD CHI / SCRAMBLE / ANCHOR / DEPTH")
    d15 = C2.row2(C2.chi_pack("CHI3", 15))
    p15 = ES.chi_row(15, DMF.Q_CHI3, DMF.LPQ3, "D15")
    uu, ww, _n, _c = DMF.chi_window_comb(15, DMF.Q_CHI3)
    mz15 = DMF.chi_build_measures(15, uu, ww, 1.0, DMF.LPQ3)
    oc15 = S422.occ_spec(15, mz=mz15, chi=True, q=DMF.Q_CHI3,
                         lpq=DMF.LPQ3)
    check("G20-dead15-all-four",
          d15["qN"] > 1.0 and d15["absZloc"] > M_W
          and p15["sch"] > 0 and oc15["razor"] >= 1e-3
          and abs(d15["qN"] - DEAD15_QN) <= 0.01
          and abs(d15["absZloc"] - DEAD15_ZLOC) <= 0.02,
          "qN=%.3f |Zloc|=%.3f sch=%+.4f raz=%.2e (all death)"
          % (d15["qN"], d15["absZloc"], p15["sch"], oc15["razor"]))
    d23 = C2.row2(C2.chi_pack("CHI3", 23))
    p23 = ES.chi_row(23, DMF.Q_CHI3, DMF.LPQ3, "D23")
    uu, ww, _n, _c = DMF.chi_window_comb(23, DMF.Q_CHI3)
    mz23 = DMF.chi_build_measures(23, uu, ww, 1.0, DMF.LPQ3)
    oc23 = S422.occ_spec(23, mz=mz23, chi=True, q=DMF.Q_CHI3,
                         lpq=DMF.LPQ3)
    check("G21-dead23-VAC-overlap",
          d23["qN"] > 1.0 and p23["sch"] > 0
          and d23["absZloc"] > M_W
          and oc23["razor"] >= DEAD_VAC_RAZ_LO
          and abs(oc23["razor"] - DEAD23_RAZ) / DEAD23_RAZ <= 0.25,
          "VAC-dead qN=%.3f raz=%.2e |Zloc|=%.3f"
          % (d23["qN"], oc23["razor"], d23["absZloc"]))
    s = C2.row2(BH.wpack(9, dict(scramble_seed=1)))
    check("G22-scramble-breaks-Z0sel-not-qN",
          s["living"] and s["qN"] < 1
          and abs(s["qN"] - SCR_QN) <= 0.01
          and s["absZloc"] > Z0_SEL
          and s["absZloc"] < Z0P
          and abs(s["absZloc"] - SCR_ZLOC) <= 0.02,
          "SCR qN=%.4f living; |Zloc|=%.3f > 1/2 "
          "(Z0_sel is MAIN-selected, not scramble-stable)"
          % (s["qN"], s["absZloc"]))
    a16 = four_pack(16, compose=True)
    check("G23-false-anchor-kz16",
          abs(a16["qN"] - KZ16_QN) <= 0.002
          and abs(a16["absZloc"] - KZ16_ZLOC) <= 0.002
          and abs(a16["sch"] - KZ16_SCH) <= 0.001
          and a16["razor"] <= 1e-7
          and a16["qN"] < 1 and (not a16["P1"])
          and a16["absZloc"] > Z0_SEL,
          "42er razor qN=%.4f |Zloc|=%.4f sch=%+.4f raz=%.2e "
          "(selected SKIPS this rung; overlap does NOT see it)"
          % (a16["qN"], a16["absZloc"], a16["sch"], a16["razor"]))
    mz = HM.two_period_mz(21, 2.0 / 3.0)
    j1, j2 = PX.pair_select(mz["yn"])
    oT = FTI.cut_rung(mz["xu"], mz["wu"], mz["yn"], mz["vn"],
                       mz["Nw"], mz["S"], mz["L"], j1, j2)
    check("G24-two-period",
          oT["nneg"] >= TP21_NNEG,
          "nnegA0=%d >= 4 (chart dies)" % oT["nneg"])
    mz9 = PX.build_rung(9)["mz"]
    C0, _ = DI.chain_C(mz9)
    C1, _ = DI.chain_C(mz9, n=int(mz9["Nw"]) + 1)
    c0 = float(np.linalg.eigvalsh(C0)[0])
    c1 = float(np.linalg.eigvalsh(C1)[0])
    check("G25-depth-mutant",
          c0 < 0.90 and c1 > 0.999,
          "n Cmin=%.4f -> n+1 Cmin=%.4f (wrong depth "
          "moves the P1 razor across 1)" % (c0, c1))
    check("G26-k8-pinned-not-live",
          K8_PIN["kz"] == 69 and K8_PIN["Nw"] == 5690
          and abs(K8_PIN["den"] - S421.K8_PIN["den"]) <= 1e-4,
          "k=8 kz=69 N=5690 den pin from r421 (builder fallback)")


def part_census(smoke):
    section("S4  LEG A -- SELECTED CENSUS / CORE-42 REGRESSION")
    if smoke:
        section("S4b  selected-full / core-42 skipped (--smoke)")
        return None
    rows = []
    for k, kz in SEL_LIVE:
        r = four_pack(kz, compose=True)
        r["k"] = k
        rows.append(r)
        print("    k=%d kz=%d N=%d qN=%.5f |Zloc|=%.4f R=%.3f "
              "L1=%.3f sch=%+.4f raz=%.2e P1=%s"
              % (k, kz, r["Nw"], r["qN"], r["absZloc"], r["R"],
                 r["L1"], r["sch"], r["razor"], r["P1"]),
              flush=True)
    qns = [r["qN"] for r in rows]
    zls = [r["absZloc"] for r in rows]
    check("G30-selected-qn-away-from-one",
          max(qns) < 0.40 and min(qns) > 0
          and all(r["qN"] < 1 and r["sch"] < 0 for r in rows)
          and abs(rows[0]["qN"] - K3_QN) <= 0.002
          and abs(rows[-1]["qN"] - K9_QN) <= 0.0002
          and rows[0]["qN"] > rows[1]["qN"] > rows[2]["qN"],
          "qN in [%.5f, %.4f]; min-margin=%.3f vs 42er 0.0195; "
          "falling in k at the P1 head"
          % (min(qns), max(qns), 1.0 - max(qns)))
    check("G31-compose-comfortable",
          max(r["R"] for r in rows) <= 1.5 < R0
          and max(r["L1"] for r in rows) <= 0.70 < LAMBDA
          and max(zls) < Z0_SEL < Z0P < M_W
          and abs(max(zls) - K3_ZLOC) <= 0.002
          and all(r["dict_dev"] < 1e-11 for r in rows),
          "R<=%.3f L1<=%.3f |Zloc|<=%.4f < 1/2 "
          "(envelopes comfortable; k=3 tight to 1/2)"
          % (max(r["R"] for r in rows),
             max(r["L1"] for r in rows), max(zls)))
    vac = [r for r in rows if not r["P1"]]
    p1 = [r for r in rows if r["P1"]]
    check("G32-overlap-split-on-selected",
          all(r["razor"] <= 1e-6 for r in vac)
          and all(r["razor"] >= 1e-6 for r in p1)
          and min(r["razor"] for r in p1) / max(r["razor"] for r in vac)
          >= 10,
          "VAC raz<=1e-6; P1 raz>=1e-6 (overlap tracks the "
          "chart, not q_N)")
    core = list(V.admissible_indices())
    cq, p1r, vacr = [], [], []
    for kz in core:
        d = S420.den_pack(kz)
        cq.append(d["qN"])
        (p1r if d["P1"] else vacr).append(d["razor_share"])
    check("G33-core42-regression",
          len(core) == CORE_N and max(cq) < 1
          and abs(max(cq) - CORE_QN_HI) <= 0.002
          and (1.0 - max(cq)) <= 0.021
          and (1.0 - max(cq)) >= 0.018
          and max(p1r) <= P1_RAZ_HI
          and max(vacr) <= VAC_RAZ_HI
          and max(p1r) / max(vacr) >= 100,
          "42er qN-max=%.4f margin=%.4f; P1 raz-max=%.2e "
          "VAC raz-max=%.2e (overlap is VAC-restricted)"
          % (max(cq), 1.0 - max(cq), max(p1r), max(vacr)))
    return rows


def main():
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke

    print("=" * 78)
    print("qn_reopened_probe -- "
          "PRIME.TERMINAL.QN_REOPENED.01 (round 428)")
    print("SPEC_SHA %s" % SPEC_SHA[:16])
    print("mode: %s" % ("SMOKE" if smoke else
                        "FULL (selected k=3..7,9 + core-42; "
                        "k=8 pinned)"))
    print("=" * 78)

    section("S0  FIREWALL + IMPORT SHA")
    okf, det = firewall_audit()
    check("G00-firewall", okf, det)
    sha_ok = (ES.SPEC_SHA.startswith(ES_SHA_PREFIX)
              and S417.SPEC_SHA.startswith(S417_SHA_PREFIX)
              and S420.SPEC_SHA.startswith(S420_SHA_PREFIX)
              and S421.SPEC_SHA.startswith(S421_SHA_PREFIX)
              and S422.SPEC_SHA.startswith(S422_SHA_PREFIX)
              and S424.SPEC_SHA.startswith(S424_SHA_PREFIX)
              and C2.SPEC_SHA.startswith(C2_SHA_PREFIX)
              and HM.SPEC_SHA.startswith(HM_SHA_PREFIX)
              and FTI.SPEC_SHA.startswith(FTI_SHA_PREFIX)
              and DMF.SPEC_SHA.startswith(DMF_SHA_PREFIX)
              and DI.SPEC_SHA.startswith(DI_SHA_PREFIX))
    check("G00b-import-sha", sha_ok,
          "S422 %s C2 %s" % (S422.SPEC_SHA[:8], C2.SPEC_SHA[:8]))
    ag = antigate_fragment_audit()
    check("G00c-no-fit", not ag,
          "no fit primitives" if not ag else "; ".join(ag))

    part_satz()
    part_pins()
    part_kills()
    part_census(smoke)

    section("S5  VERDICT")
    prev_ok = all(ok for _n, ok in CHECKS)
    check("G50-verdict",
          prev_ok,
          "SELECTED_MARGIN_GO / OVERLAP_VAC_ONLY / "
          "ZLOC_WINS / COFINAL_OPEN.  no RH / L* / R-dagger")

    n_fail = sum(1 for _n, ok in CHECKS if not ok)
    n_ok = len(CHECKS) - n_fail
    verd = ("SELECTED_MARGIN_GO / OVERLAP_VAC_ONLY / "
            "ZLOC_WINS / COFINAL_OPEN")
    print("\nRESULT: %d/%d gates PASS   SPEC_SHA %s   (%.1fs)  %s" % (
        n_ok, len(CHECKS), SPEC_SHA[:16], time.time() - T0, verd))
    if n_fail == 0:
        print("QN REOPENED %sVERIFIED" % ("SMOKE " if smoke else ""))
        return 0
    print("QN REOPENED FAILED %d" % n_fail)
    return 1


if __name__ == "__main__":
    sys.exit(main())
