#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""compose_premises2_probe -- LEMMA.COMPOSE.PREMISES2.01 (round 386):
LIVING-LADDER (Z') AND COFINAL R0.

Coexistence: r383 reduced (R)(L)(Z) to census constants on 181,
with (Z) family-uniform REFUTED on six chi windows (exactly the
terminal-dead q_N>1 sprouts) and cofinal R0 open.  This round
has TWO letters.

LEGS (lemma-first; each exit PROVED / REFUTED / REDUCED):
  Z'  |Z_loc| <= Z0' < M on the cofinal LIVING ladder
      (FRAME-A 89 + FRAME-B 8 + chi with q_N<1).  Death
      channel |Z_loc|>=M ==> q_N>1.  Source bound: finite
      Chebyshev head vs cancellation vs m2+census.
  R0  S_F <= R0 D cofinally.  Weaker MAIN: B(omega,omega)<=C D.
      CS on B(Delta, omega+beta) plus FAB/K2.  Else name the
      smallest remainder.

CALIBRATION DISCLOSURE.  Numbers below were first measured in
/tmp/tfpt_r386_cal.py (WALL 628.2 s, 181 live rows) on the same
constructors as r383, 2026-08-28.  Frozen constants are that
measurement, sealed as gates -- not a search over Z0'/C_MAIN.
Pins disclosed.

FROZEN FROM /tmp (live re-gated, not fitted):
  * Living ladder n=175 (181 minus 6 dead).  Dead chi are
    exactly CHI3 {15,19,23,33,39} and CHI4 {20}, q_N in
    [1.040, 1.330], matching r362/r370 TERMINAL-DEAD.
  * Death channel |Z_loc|>=M iff |Z|>=M iff q_N>1 on 181/181
    (biconditional CENSUS; converse extras 0).
  * sup |Z_loc| on living = 0.833870 at CHI4 kz46 < M=0.845154
    but > Z0_r383=4/5.  Z0' = 21/25 = 0.84 (disclosed ceiling).
    Mutant 4/5 FAILS at CHI4-46.  FRAME-A max still 0.755675.
  * Dictionary q_N = rho_{N-1}/(5/7) = (7/5) Z^2 at w9 (r263).
  * Naive finite-head Chebyshev REFUTED (n_edge 167..4689;
    triangle tri 2.86..14.51 grows, slope +0.253).  Signed
    cancellation is real (cancel med 0.055, max 0.281) but
    cancel_max * tri_max = 4.08 > M: uniform-cancel * triangle
    does NOT close.  sl_zloc living -0.114 (census, not SATZ).
  * MAIN/D max 0.129976, med 0.0100, log-log slope -1.163
    (falling).  C_MAIN = 3/10.  DC toy MAIN/D=3.6875 FAILS
    any field-independent C_MAIN<=1.  Tdel/D max 2.9116
    (almost all of R).  CS on Tdel: 181/181 SATZ, tight at
    kz37 (Tdel/D 2.9116 vs sqrt(Bdd Bsum)/D ~ 2.921).
  * Bdd/D max 2.8688, Bsum/D 2.975 at R-star kz37.  FAB max
    18.07 > 14.93 (FRAME-B family-indexed, r353).  CS+FAB
    does NOT prove O(polylog) on S_F/D: FAB controls Pd not
    Pw.  Named remainder: B(omega+beta, omega+beta) <= K D.
  * R_max still 2.916788 at kz37; sl_R -0.328 (census).
    R0=4 unchanged.  Scramble seed=1 at w9 does NOT break
    (Z') or R0 (R=0.598, |Zloc|=0.524, still living).

NO RH CLAIM.  Finite identities, named reductions.  Research
documentation, not a theorem of RH.
Sealed gates: 12/12 smoke / 20/20 full (G1--G6 toys, G10--G15
pins, G20--G27 census).  Companion verifier adds G8/G9.
"""
from __future__ import annotations

import argparse
import hashlib
import math
import os
import sys
import time
from fractions import Fraction as Fr

import numpy as np

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DISC = os.path.dirname(os.path.abspath(__file__))
if DISC not in sys.path:
    sys.path.insert(0, DISC)

import compose_premises_probe as C  # noqa: E402
import dirichlet_matched_frame_probe as DMF  # noqa: E402
import mean_sieve_floor_probe as MSF  # noqa: E402

M_W = C.M_W
R0 = C.R0
C_MAIN = float(Fr(3, 10))
Z0_OLD = float(Fr(4, 5))
Z0P = float(Fr(21, 25))
Z_STAR_LIV = 0.8338699135327932
Z_STAR_FAM, Z_STAR_KZ = "CHI4", 46
R_STAR = C.R_STAR
R_STAR_KZ = C.R_STAR_KZ
MAIN_D_STAR = 0.12997560289435886
N_181, N_LIVING, N_DEAD = 181, 175, 6
CHI_DEAD = set(C.CHI_Z_VIOL)
SCR_SEED = 1
FAB_A = 14.93
DEC_BAR = C.DEC_BAR
ID_BAR = 1e-9

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


def chi_pack(fam, kz):
    if fam == "CHI3":
        u, w, _n, _c = DMF.chi_window_comb(kz, MSF.Q_CHI3)
        return DMF.chi_wpack(kz, 1.0, MSF.LPQ3, (u, w))
    u, w, _n, _c = DMF.chi_window_comb(kz, MSF.Q_CHI4)
    return DMF.chi_wpack(kz, 1.0, MSF.LPQ4, (u, w))


def qN_of(p, r0):
    rho = float(p["rows"][p["N"] - 1]["rho"])
    qN = rho / (5.0 / 7.0)
    dict_q = (7.0 / 5.0) * (r0["Z"] ** 2)
    return qN, abs(qN - dict_q) / max(abs(qN), 1e-300)


def gram_head(p, r0):
    """Bdd, Bsum, edge triangle, signed cancel.  Source-pure."""
    N = p["N"]
    rows = p["rows"]
    xu, wu = C.CT.union_arrays(p["d"])
    bx, bw = C.CT.union_arrays(p["dsm"])
    lo = min(float(np.min(xu)), float(np.min(bx)))
    hi = max(float(np.max(xu)), float(np.max(bx)))
    v2 = C.BR.eval_scaled(rows, bx, N - 2)
    v2w = C.BR.eval_scaled(rows, xu, N - 2)
    fac = math.exp(rows[N - 2]["Ls"] - rows[N - 1]["Ls"]) \
        / math.sqrt(abs(rows[N - 1]["eta"]))
    ct = bw * bx * v2 * fac
    cw = wu * xu * v2w * fac
    o = np.argsort(bx, kind="stable")
    bxs, cts = bx[o], ct[o]
    ed = C.PBB.mask_edge(bxs, lo, hi, C.PBB.EDGE_F)
    t_loc = float(np.sum(cts[ed])) if np.any(ed) else 0.0
    tri = float(np.sum(np.abs(cts[ed]))) if np.any(ed) else 0.0
    cb, xb = cts[~ed], bxs[~ed]
    runs = C.PBB.runs_split(cb)
    brk, mblk, jb = C.WBT.block_breaks(xb, runs)
    Pb = np.bincount(jb, weights=cb, minlength=mblk) if mblk \
        else np.zeros(0)
    Pw = C.WBT.aggregate_blocks(xu, cw, lo, hi, brk, mblk)
    Pd = Pb - Pw
    H = r0["H"]
    Bdd = C.WBT.fejer_bil(Pd, Pd, H) if mblk else 0.0
    Bsum = C.WBT.fejer_bil(Pb + Pw, Pb + Pw, H) if mblk else 0.0
    D = r0["D"]
    L1 = r0["L1"]
    m = max(r0["m"], 2)
    qmax = (float(np.max(np.abs(Pd)) / max(L1, 1e-300))
            if L1 > 0 and Pd.size else 0.0)
    FAB = m * qmax / math.log(m)
    Tdel = r0["Tdel"]
    cs_ok = (Tdel * Tdel) <= Bdd * Bsum + 1e-10 * max(1.0, Tdel * Tdel)
    return dict(
        t_loc=t_loc, tri=tri,
        cancel=abs(t_loc) / max(tri, 1e-300),
        Bdd=Bdd, Bsum=Bsum, cs_ok=cs_ok, FAB=FAB, qmax=qmax,
        MAIN_over_D=(r0["MAIN"] / D) if D > 0 else 0.0,
        Bdd_over_D=(Bdd / D) if D > 0 else 0.0,
        Bsum_over_D=(Bsum / D) if D > 0 else 0.0,
    )


def row2(p, with_gram=False):
    r0 = C.row_of(p)
    qN, ddev = qN_of(p, r0)
    r0["qN"] = qN
    r0["dict_dev"] = ddev
    r0["living"] = qN < 1.0 - 1e-12
    r0["dead_zloc"] = r0["absZloc"] >= M_W - 1e-12
    r0["dead_z"] = r0["absZ"] >= M_W - 1e-12
    r0["MAIN_over_D"] = (r0["MAIN"] / r0["D"]) if r0["D"] > 0 else 0.0
    if with_gram:
        r0.update(gram_head(p, r0))
    return r0


def part_toys():
    section("TOYS / SATZ (no window builders)")
    Q = np.ones(16)
    Sdc = C.WBT.fejer_bil(Q, Q, 4)
    Ddc = float(np.dot(Q, Q))
    Rdc = Sdc / Ddc
    check("G1-DC-MAIN-eq-R-breaks-CMAIN",
          abs(Rdc - 3.6875) < 1e-9 and Rdc > C_MAIN and Rdc <= 4.0,
          "DC MAIN/D=R=%.4f > C_MAIN=3/10: field-independent "
          "MAIN bound REFUTED; still <= R0=4" % Rdc)
    P = np.array([1.0, -1.0] * 8)
    Sf = C.WBT.fejer_bil(P, P, 4)
    D = float(np.dot(P, P))
    check("G2-period2-R-one-sixteenth",
          abs(Sf / D - 1.0 / 16.0) < 1e-12,
          "period-2 even-H R=%.6f" % (Sf / D))
    u = np.array([1.0, 0.0, -1.0, 2.0])
    v = np.array([0.5, -0.5, 1.0, 0.0])
    Buv = C.WBT.fejer_bil(u, v, 2)
    Buu = C.WBT.fejer_bil(u, u, 2)
    Bvv = C.WBT.fejer_bil(v, v, 2)
    check("G3-fejer-CS",
          Buv * Buv <= Buu * Bvv + 1e-12,
          "B(u,v)^2 <= B(u,u)B(v,v)")
    # death-triangle: |Z| >= |Zloc|-|t_bulk|
    zloc, tb, Mv = 1.0, -0.1, M_W
    z = zloc + tb
    check("G4-death-triangle-algebra",
          abs(z) >= abs(zloc) - abs(tb) - 1e-15
          and abs(zloc) >= Mv
          and abs(tb) <= abs(zloc) - Mv
          and abs(z) >= Mv,
          "|Zloc|=1, t_bulk=-0.1: |Z|=0.9 >= M and the "
          "sufficient |t_bulk| <= |Zloc|-M holds")
    check("G5-Z0p-between-old-and-M",
          Z0_OLD < Z_STAR_LIV < Z0P < M_W
          and abs(Z0P - 0.84) < 1e-15
          and float(Fr(21, 25)) == Z0P,
          "4/5=0.8 < living-sup %.6f < 21/25=0.84 < M=%.6f"
          % (Z_STAR_LIV, M_W))
    fw_ok, fw_d = C.firewall_audit()
    sha_ok = (C.WBT.SPEC_SHA.startswith(C.WBT_SHA_PREFIX)
              and C.L2D.SPEC_SHA.startswith(C.L2D_SHA_PREFIX)
              and C.DMF.SPEC_SHA.startswith(C.DMF_SHA_PREFIX)
              and C.SFE.SPEC_SHA.startswith(C.SFE_SHA_PREFIX)
              and C.MSF.SPEC_SHA.startswith(C.MSF_SHA_PREFIX))
    check("G6-firewall-and-sha",
          fw_ok and sha_ok,
          "%s; WBT/L2D/DMF/SFE/MSF prefixes" % fw_d)


def part_pins():
    section("CONSTRUCTION PINS (w9, scramble, R-star, living/dead chi)")
    pA = C.BH.wpack(9)
    a = row2(pA, with_gram=True)
    qN, ddev = a["qN"], a["dict_dev"]
    check("G10-w9-living-dict-R",
          a["living"] and a["absZloc"] < Z0P
          and a["R"] <= R0 and a["MAIN_over_D"] <= C_MAIN
          and ddev < ID_BAR and a["cs_ok"] and a["split_ok"],
          "qN=%.4f |Zloc|=%.4f R=%.4f MAIN/D=%.4f dict=%.1e CS=%s"
          % (qN, a["absZloc"], a["R"], a["MAIN_over_D"], ddev,
             a["cs_ok"]))
    pS = C.BH.wpack(9, dict(scramble_seed=SCR_SEED))
    s = row2(pS)
    check("G11-scramble-does-not-break-Zp-or-R0",
          s["R"] <= R0 and s["absZloc"] < Z0P and s["living"],
          "SCR R=%.4f |Zloc|=%.4f living=%s (does NOT break "
          "(Z') or R0; named (Z) kill remains the 6 dead chi)"
          % (s["R"], s["absZloc"], s["living"]))
    p37 = C.BH.wpack(R_STAR_KZ)
    a37 = row2(p37, with_gram=True)
    check("G12-R-star-kz37-grams",
          abs(a37["R"] - R_STAR) < 1e-4
          and a37["R"] <= R0
          and a37["MAIN_over_D"] <= C_MAIN
          and a37["Bsum_over_D"] < R0
          and a37["Bdd_over_D"] < R0
          and a37["cs_ok"],
          "kz37 R=%.6f MAIN/D=%.4f Bdd/D=%.4f Bsum/D=%.4f CS"
          % (a37["R"], a37["MAIN_over_D"], a37["Bdd_over_D"],
             a37["Bsum_over_D"]))
    p46 = chi_pack(Z_STAR_FAM, Z_STAR_KZ)
    a46 = row2(p46)
    check("G13-living-Z-star-CHI4-46",
          a46["living"]
          and abs(a46["absZloc"] - Z_STAR_LIV) < 1e-4
          and a46["absZloc"] > Z0_OLD
          and a46["absZloc"] < Z0P < M_W,
          "|Zloc|=%.6f (pin %.6f) > 4/5 and < 21/25; qN=%.4f"
          % (a46["absZloc"], Z_STAR_LIV, a46["qN"]))
    p15 = chi_pack("CHI3", 15)
    a15 = row2(p15)
    check("G14-dead-CHI3-15-death-channel",
          (not a15["living"]) and a15["dead_zloc"] and a15["dead_z"]
          and a15["qN"] > 1.0
          and a15["absZloc"] >= M_W and a15["absZ"] >= M_W,
          "CHI3-15 qN=%.4f |Zloc|=%.4f |Z|=%.4f (dead; both >= M)"
          % (a15["qN"], a15["absZloc"], a15["absZ"]))
    check("G15-mutant-Z0-four-fifths-fails-living-chi",
          a46["absZloc"] > Z0_OLD,
          "mutant Z0=4/5 FAILS on living CHI4-46 "
          "(%.6f > 0.8); living restriction is necessary"
          % a46["absZloc"])
    return dict(w9=a, scr=s, kz37=a37, chi46=a46, chi15=a15)


def part_full():
    section("181-WINDOW CENSUS (living ladder + death channel + R0)")
    print("  loading packs...", flush=True)
    fams = C.load_surface()
    all_rows = []
    for lab in ("A", "B", "CHI3", "CHI4"):
        for p in fams[lab]:
            if p.get("nf") is not None:
                continue
            r = row2(p, with_gram=True)
            r["fam"] = lab
            all_rows.append(r)
        print("    %s done" % lab, flush=True)
    n = len(all_rows)
    living = [r for r in all_rows if r["living"]]
    dead = [r for r in all_rows if not r["living"]]
    dead_zloc = [r for r in all_rows if r["dead_zloc"]]
    dead_z = [r for r in all_rows if r["dead_z"]]
    chi_dead = [(r["fam"], r["kz"]) for r in all_rows
                if r["fam"] in ("CHI3", "CHI4") and not r["living"]]
    check("G20-181-living-175-dead-6",
          n == N_181 and len(living) == N_LIVING
          and len(dead) == N_DEAD,
          "n=%d living=%d dead=%d" % (n, len(living), len(dead)))
    iff_ok = (len(dead_zloc) == N_DEAD and len(dead_z) == N_DEAD
              and all(r["dead_z"] for r in dead_zloc)
              and all(r["dead_zloc"] for r in dead_z)
              and all((not r["living"]) for r in dead_zloc)
              and all(r["living"] for r in all_rows
                      if not r["dead_zloc"]))
    check("G21-death-channel-iff-181",
          iff_ok,
          "|Zloc|>=M iff |Z|>=M iff qN>1 on 181/181 "
          "(biconditional CENSUS; 6=6=6)")
    zliv = max(r["absZloc"] for r in living)
    zrow = max(living, key=lambda r: r["absZloc"])
    okZ = all(r["absZloc"] <= Z0P + 1e-12 for r in living)
    check("G22-Zp-living-Z0p-21-25",
          okZ and abs(zliv - Z_STAR_LIV) < 1e-4
          and zrow["fam"] == Z_STAR_FAM and zrow["kz"] == Z_STAR_KZ
          and zliv < M_W,
          "living 175/175 |Zloc|<=0.84; max=%.6f at %s kz%s"
          % (zliv, zrow["fam"], zrow["kz"]))
    check("G23-dead-chi-exact-six",
          set(chi_dead) == CHI_DEAD,
          "dead chi %s" % (sorted(chi_dead),))
    mD = max(r["MAIN_over_D"] for r in all_rows)
    check("G24-MAIN-over-D-le-CMAIN",
          all(r["MAIN_over_D"] <= C_MAIN + 1e-12 for r in all_rows)
          and abs(mD - MAIN_D_STAR) < 1e-4,
          "MAIN/D <= 3/10 on 181/181; max=%.6f (pin %.6f)"
          % (mD, MAIN_D_STAR))
    rmax = max(r["R"] for r in all_rows)
    n_cs = sum(1 for r in all_rows if r.get("cs_ok"))
    n_dec = sum(1 for r in all_rows if r["dec_dev"] < DEC_BAR)
    check("G25-R0-and-CS-181",
          all(r["R"] <= R0 + 1e-12 for r in all_rows)
          and abs(rmax - R_STAR) < 1e-4
          and n_cs == N_181 and n_dec == N_181,
          "R<=4 on 181/181 max=%.6f; CS %d/%d; r298 %d/%d"
          % (rmax, n_cs, N_181, n_dec, N_181))
    n_edge_min = min(r["n_edge"] for r in all_rows)
    n_edge_max = max(r["n_edge"] for r in all_rows)
    tri_max = max(r["tri"] for r in all_rows)
    can_max = max(r["cancel"] for r in all_rows)
    check("G26-chebyshev-triangle-and-uniform-cancel-refuted",
          n_edge_min >= 100 and n_edge_max >= 1000
          and tri_max > M_W and can_max * tri_max > M_W,
          "n_edge %d..%d; tri_max=%.3f; cancel_max*tri_max=%.3f > M "
          "(finite-head AND uniform-cancel*triangle REFUTED)"
          % (n_edge_min, n_edge_max, tri_max, can_max * tri_max))
    fab_max = max(r["FAB"] for r in all_rows)
    check("G27-FAB-A-not-family-uniform",
          fab_max > FAB_A,
          "FAB_max=%.3f > 14.93 (A-law not family-uniform; "
          "CS+FAB does not close cofinal R0)" % fab_max)
    return all_rows


def main():
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    print("=" * 78)
    print("compose_premises2_probe -- LEMMA.COMPOSE.PREMISES2.01 "
          "(round 386)")
    print("SPEC_SHA %s" % SPEC_SHA[:16])
    print("NO RH CLAIM.", flush=True)
    part_toys()
    pins = part_pins()
    if not args.smoke:
        part_full()
    n_fail = sum(1 for _n, ok in CHECKS if not ok)
    print("\nRESULT: %d/%d gates PASS%s   SPEC_SHA %s   (%.1fs)"
          % (len(CHECKS) - n_fail, len(CHECKS),
             "" if n_fail == 0 else "  ** FAIL **",
             SPEC_SHA[:16], time.time() - T0))
    print("COMPOSE PREMISES2 "
          + ("VERIFIED" if n_fail == 0 else "FAILED %d" % n_fail))
    print("LETTERS: (Z') REDUCED (Z0'=21/25 on living 175/175; "
          "death channel CENSUS iff 181/181; Chebyshev head "
          "REFUTED; uniform-cancel*triangle REFUTED)  "
          "(R) REDUCED (R0=4 census; MAIN/D<=3/10 census falling; "
          "CS SATZ; CS+FAB does NOT prove O(polylog); named "
          "remainder B(omega+beta,omega+beta)<=K D)")
    print("T1-COMBO: not this round (r383: does not carry).")
    print("KILL: DC toy breaks field-independent C_MAIN; mutant "
          "Z0=4/5 fails on living CHI4-46; scramble does NOT "
          "break (Z') or R0; family-uniform (Z) still killed "
          "by the 6 terminal-dead chi.")
    _ = pins
    return 0 if n_fail == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
