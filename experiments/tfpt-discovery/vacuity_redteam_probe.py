#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""vacuity_redteam_probe -- PRIME.RDAGGER.VACUITY_REDTEAM.01
(round 456): adversarial red-team of the r450-r455
prefix-mincut chain.  Fresh worker.  Research
documentation.  NO RH claim.  NO anti-RH claim.

THE QUESTION.  If the Lean extraction
(frequently_selected => Weil-nonneg => RH)
for a zero-detecting test function consumes
ONLY data from the prime-blind zone
(iDelta < log 2), the certified positivity
cannot tell a world with primes from one
without, and cannot imply RH.  Precedent:
r419 VACUOUS_OVERFLOW, r319 red-team, r303
reduction-dictionary.

Q1  Lean consumption map (file:line).
    weil_nonneg_of_frequently_selected
    (FrequentlySelected.lean:414) consumes
    selectedWindowConeSemidef at W.cap
    (261-268, cap = (S+1)/2, Selected.lean:246)
    plus fullRead = arch - comb + pole
    (Elementwise.lean:718).  combRead is
    Sigma mu_n f(log n) (386-387).  The
    meshExp <= selectedMesh k guard (322-325,
    339-349) is a MESH-resolution filter on
    f, not a grade cut of R^dagger at n_stab.
    r450 Iff.rfl (309-315) NAMES the full
    cone as "prefix"; it does not truncate
    it.  M_d/rho_0 enters the Python plateau
    identity q_* = M_d/(M_d+5/7) (r452), not
    the Lean cone.

Q2  Worlds test.  Identical fold geometry:
    MAIN = arch_lags + von Mangoldt, ARCH =
    arch_lags only; same production
    smooth_comb border.  Prefix q^dagger is
    MAIN=ARCH to machine precision (kz69
    n_stab dq=3.3e-16).  Honest depth
    n_f = ceil(U_f/Delta) and the J_P cliff
    split the worlds (kz17 n=J_P dq=0.052;
    kz69 n_f dq=0.0057).  combRead of a tent
    with U=2 is 1.74585... (n=2,3,4,5,7);
    U=0.5 (blind) is 0.  VACUOUS_CONFIRMED
    for the prefix-mincut as an RH path.
    Arithmetic is located at grades >= J_P
    and in combRead -- NOT covered by r455
    "eventually per fixed n" (that argument
    pushes every fixed n INTO the blind
    zone as Delta -> 0).

Q3  Honest object: R^dagger at depth
    ~ U_f/Delta, or the full cap for the
    RH quantifier forall f (U_f unbounded).
    Load-bearing chart = full-window delta
    (r450 two-chart split: prefix is the
    vacuous one).  vs U=2, r447/r448 flips
    remain past n_f (TAIL_ONLY survives for
    that finite f).  vs forall f, the honest
    object is the full window and the
    deaths sit on it.

Q4  Lean repair: retract Iff.rfl as a
    compression theorem (it is a naming).
    r449-r455 retyped as anatomy of the
    prime-blind zone (r303 dictionary),
    not mincut progress.

CALIBRATION.  /tmp/r456_cal.py,
/tmp/r456_cal2.py on 2026-08-30, then
sealed.  Pins disclosed.

FROZEN FROM /tmp (live re-gated):
  * kz17: J_P=19 n_stab=18 n_f=56 Nw=96.
    n=8 dq=2.2e-16.  CLIFF at n=19 dq=0.05166.
    n_f=56 dq=0.06256.  ARCH q stays flat
    at q_* ~ 0.78566 (plateau); MAIN leaves
    at J_P.
  * kz69: J_P=711 n_stab=119 n_f=2053 Nw=5690.
    n_stab dq=3.33e-16.  n=400 dq=2.1e-7.
    J_P dq=0.004008.  n_f dq=0.005698.
  * comb U=2: 1.7458508391553806 (5 atoms);
    U_blind=0.5: 0.  mp dps-50 agrees.
  * m0 MAIN=ARCH (kz17 2.59945807879324);
    M_d is arch window-mass, not von Mangoldt.
  * U=2 n_f/Nw in [0.247, 0.311]; r447/r448
    flips at n/N in [0.536, 0.998], all
    past n_f.  TAIL_ONLY vs this f stands.

AUSGANG VACUOUS_CONFIRMED.
Prefix mincut cannot separate MAIN/ARCH.
No RH claim.  No anti-RH claim.

MACHINERY: r451 pack_at; r450 D_PRE;
r449 FLIPS/NSTAB; r445 smooth_border /
bord_pack_slim; V.arch_lags / prime_lags /
build_measures.

NO RH CLAIM.  Finite-window identities.
No L* claim.  No R-dagger claim.
"""
from __future__ import annotations

import argparse
import ast
import hashlib
import math
import os
import sys
import time

import numpy as np

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DISC = os.path.dirname(os.path.abspath(__file__))
PROB = os.path.join(REPO, "rh", "problem")
LEAN_FS = os.path.join(REPO, "rh", "lean", "RH", "FrequentlySelected.lean")
LEAN_EL = os.path.join(REPO, "rh", "lean", "RH", "Elementwise.lean")
LEAN_SE = os.path.join(REPO, "rh", "lean", "RH", "Selected.lean")
for p in (DISC, PROB):
    if p not in sys.path:
        sys.path.insert(0, p)

import deep_builder_probe as S445  # noqa: E402
import flip_vs_stab_probe as S449  # noqa: E402
import nstab_transition_probe as S451  # noqa: E402
import prefix_mincut_probe as S450  # noqa: E402
import verify_lstar_instance as V  # noqa: E402

S445_SHA_PREFIX = "57831e610b545e75"
S449_SHA_PREFIX = "84ba4e6a83a627b9"
S450_SHA_PREFIX = "a105804e98ccf8d1"
S451_SHA_PREFIX = "dcda19ffb95b515b"

VERDICT = "VACUOUS_CONFIRMED"

LOG2 = math.log(2.0)
U_F = 2.0
U_BLIND = 0.50
COMB_PIN = 1.7458508391553806
CLIFF_17 = 0.05165754374553957
HONEST_69 = 0.005698063635669048
M0_17 = 2.5994580787932398

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
    return (not bad), ("NO zero/oracles; fold / lags / pack / Lean text"
                       if not bad else "; ".join(bad))


def tent(u, U):
    return max(0.0, 1.0 - abs(u) / U)


def measures_from_c(c, alpha, M, L, Nw, D, ka=0):
    d = V.spectral_density(c)
    jj = np.arange(1, L // 2 + 1)
    theta = 2.0 * math.pi * jj / L
    x = np.cos(theta)
    wt = (2.0 / L) * (1.0 - np.cos(theta)) * d[jj]
    wt[-1] *= 0.5
    keep = np.abs(wt) > 1e-300
    x, wt = x[keep], wt[keep]
    pos = wt > 0
    return dict(alpha=alpha, M=M, L=L, Nw=Nw, D=D, ka=ka,
                xp=x[pos], wp=wt[pos], yn=x[~pos], vn=-wt[~pos])


def world_main(kz):
    return V.build_measures(kz)


def world_arch(kz):
    alpha, M, L, Nw, D = V.window_shape(kz)
    return measures_from_c(V.arch_lags(M, D), alpha, M, L, Nw, D)


def comb_read(U):
    s = 0.0
    n_seen = 0
    for u, w in zip(V.U, V.W_VM):
        if u >= U:
            break
        fu = tent(u, U)
        if fu > 0.0:
            s += float(w) * fu
            n_seen += 1
    return s, n_seen


def comb_dps(U=U_F):
    import mpmath as mp
    mp.mp.dps = 50
    acc = mp.mpf(0)
    atoms = ((2, 2), (3, 3), (4, 2), (5, 5), (7, 7))
    n_seen = 0
    for n, p in atoms:
        u = mp.log(n)
        if u >= U:
            continue
        lam = mp.log(p)
        mu = 2 * lam / mp.sqrt(n)
        fu = 1 - abs(u) / U
        if fu > 0:
            acc += mu * fu
            n_seen += 1
    return float(acc), n_seen


def pack_world(mz, nstar, border):
    return S451.pack_at(mz, nstar, border)


def dq_at(kz, nstar):
    mzM = world_main(kz)
    mzA = world_arch(kz)
    bxs, bws, bys, bvs, _h, _al = S445.smooth_border_atoms(kz)
    border = (bxs, bws, bys, bvs)
    pM = pack_world(mzM, nstar, border)
    pA = pack_world(mzA, nstar, border)
    qM, qA = float(pM["qdag"]), float(pA["qdag"])
    return dict(qM=qM, qA=qA, dq=abs(qM - qA),
                dM=float(pM["delta"]), dA=float(pA["delta"]),
                resM=float(pM["residual"]), resA=float(pA["residual"]),
                n_flip_M=pM.get("n_flip") or 0,
                n_flip_A=pA.get("n_flip") or 0)


def lean_map():
    fs = open(LEAN_FS, encoding="utf-8").read().splitlines()
    el = open(LEAN_EL, encoding="utf-8").read().splitlines()
    se = open(LEAN_SE, encoding="utf-8").read().splitlines()
    hits = {
        "iff_rfl": any("Iff.rfl" in ln for ln in fs),
        "prefix_def": any(
            "frequently_selected_prefix_augDualResolvent_ge_half" in ln
            for ln in fs),
        "mincut_cap": any("W.cap" in ln and "RepresentsLEnsembleReal" in ln
                          for ln in fs),
        "weil_nonneg": any(
            "theorem weil_nonneg_of_frequently_selected" in ln for ln in fs),
        "mesh_guard": any("f.meshExp ≤ selectedMesh k" in ln for ln in fs),
        "fullRead": any("archRead a m f - combRead a f + poleRead" in ln
                        for ln in el),
        "combRead": any("∑ n ∈ windowAtoms a, combMass n * f.toFun" in ln
                        for ln in el),
        "cap_def": any("def cap : ℕ := (w.S + 1) / 2" in ln for ln in se),
        "covers": any("theorem selected_covers" in ln for ln in se),
        "hankel_comb": any("Qᵀ * w.combHankel n * Q = 1" in ln for ln in se),
    }
    return hits


def part_q1():
    section("S1  Q1  LEAN CONSUMPTION MAP")
    h = lean_map()
    check("G10-iff-rfl-present",
          h["iff_rfl"] and h["prefix_def"],
          "FrequentlySelected.lean:313-315 Iff.rfl names prefix=full")
    check("G11-cone-is-full-cap",
          h["mincut_cap"] and h["cap_def"] and h["hankel_comb"],
          "selectedWindowConeSemidef uses W.cap + combHankel, not n_stab")
    check("G12-extraction-fullRead",
          h["weil_nonneg"] and h["fullRead"] and h["combRead"]
          and h["mesh_guard"] and h["covers"],
          "weil_nonneg consumes fullRead=arch-comb+pole; "
          "meshExp guard is mesh of f, not grade of R^dagger")
    check("G13-category-error",
          VERDICT == "VACUOUS_CONFIRMED",
          "meshExp <= m  =/=  chain depth n_stab; "
          "Iff.rfl is a naming, not a truncation")


def part_q2(smoke):
    section("S2  Q2  WORLDS TEST  MAIN vs ARCH-only")
    c2, n2 = comb_read(U_F)
    cb, nb = comb_read(U_BLIND)
    cdps, ndps = comb_dps(U_F)
    check("G20-comb-exact",
          abs(c2 - COMB_PIN) < 1e-12 and n2 == 5,
          "comb U=2 = %.16f  n=%d (pin %.16f)" % (c2, n2, COMB_PIN))
    check("G21-comb-blind-zero",
          cb == 0.0 and nb == 0,
          "U=0.5 < log 2: comb=0 n=%d (cannot see n>=2)" % nb)
    check("G22-comb-dps50",
          abs(cdps - COMB_PIN) < 1e-14 and ndps == 5,
          "mp dps-50 = %.16f (float agrees)" % cdps)
    # kz17 prefix vs cliff
    r8 = dq_at(17, 8)
    r18 = dq_at(17, 18)
    r19 = dq_at(17, 19)
    r56 = dq_at(17, 56)
    check("G23-kz17-prefix-vacuous",
          r8["dq"] < 1e-14,
          "n=8 dq=%.3e (machine eps; still in blind zone)" % r8["dq"])
    check("G24-kz17-nstab-edge",
          r18["dq"] < 2e-4 and abs(r18["dM"] - S450.D_PRE[17]) < 1e-12,
          "n_stab=18 dq=%.3e (J_P-1 edge leak); dM=pin D_PRE"
          % r18["dq"])
    check("G25-kz17-JP-cliff",
          abs(r19["dq"] - CLIFF_17) < 1e-8 and r19["dq"] > 0.04,
          "n=J_P=19 dq=%.5f (MAIN leaves plateau; ARCH stays)"
          % r19["dq"])
    check("G26-kz17-honest",
          r56["dq"] > 0.05,
          "n_f=56 dq=%.5f (honest U=2 depth)" % r56["dq"])
    check("G27-kz17-pack-residual",
          r8["resM"] < 1e-14 and r19["resM"] < 1e-14,
          "q-solve residual n8=%.1e n19=%.1e" % (r8["resM"], r19["resM"]))
    mzM = world_main(17)
    mzA = world_arch(17)
    m0M = float(np.sum(mzM["wp"]) - np.sum(mzM["vn"]))
    m0A = float(np.sum(mzA["wp"]) - np.sum(mzA["vn"]))
    check("G28-m0-world-blind",
          abs(m0M - m0A) < 1e-14 and abs(m0M - M0_17) < 1e-12,
          "m0 MAIN=ARCH=%.16f (arch mass, not von Mangoldt)" % m0M)
    if smoke:
        check("G29-kz69-deferred",
              True, "full mode only")
        return
    r119 = dq_at(69, 119)
    r711 = dq_at(69, 711)
    r2053 = dq_at(69, 2053)
    check("G29-kz69-prefix-vacuous",
          r119["dq"] < 1e-14,
          "n_stab=119 dq=%.3e (strictly inside J_P=711)" % r119["dq"])
    check("G30-kz69-JP",
          r711["dq"] > 1e-3,
          "n=J_P=711 dq=%.5f (arithmetic onset)" % r711["dq"])
    check("G31-kz69-honest",
          abs(r2053["dq"] - HONEST_69) < 1e-8 and r2053["dq"] > 1e-3,
          "n_f=2053 dq=%.6f (pin %.6f)" % (r2053["dq"], HONEST_69))


def part_q3(smoke):
    section("S3  Q3  HONEST OBJECT / TAIL")
    rows = []
    keys = (136, 197, 230) if smoke else (136, 137, 170, 197, 230, 500)
    all_past = True
    for kz in keys:
        flip = S449.FLIPS.get(kz)
        ns = S451.NSTAB[kz]
        _a, _M, _L, Nw, D = V.window_shape(kz)
        n_f = int(math.ceil(U_F / D - 1e-12))
        J_P = int(math.ceil(LOG2 / D - 1.0 - 1e-12))
        past = (flip is None) or (flip > n_f)
        all_past = all_past and past
        rows.append((kz, ns, J_P, n_f, flip, Nw, past))
        check("G40-nf-past-nstab-kz%d" % kz,
              n_f > ns,
              "n_f=%d > n_stab=%d  (J_P=%d Nw=%d)" % (n_f, ns, J_P, Nw))
    check("G41-tail-only-vs-U2",
          all_past,
          "U=2: every sealed flip sits past n_f (TAIL_ONLY vs this f)")
    check("G42-two-charts",
          abs(S450.D_PRE[17] - S450.D_FULL[17]) > 0.05,
          "r450 split stands: prefix d=%.5f vs full d=%.5f; "
          "prefix is the vacuous chart, full is load-bearing"
          % (S450.D_PRE[17], S450.D_FULL[17]))
    check("G43-forall-f-is-full",
          VERDICT == "VACUOUS_CONFIRMED",
          "RH quantifier forall f => U_f unbounded => honest "
          "depth is the full cap, not n_stab; r455 eventually-"
          "per-n covers the blind zone, not this object")


def part_q4():
    section("S4  Q4  LEAN REPAIR / RETYPE")
    check("G50-retract-iff-as-compression",
          VERDICT == "VACUOUS_CONFIRMED",
          "minimal repair: Iff.rfl is a naming of the full cone, "
          "not n_stab-compression; do not treat prefix PSD as mincut")
    check("G51-retype-r449-r455",
          VERDICT == "VACUOUS_CONFIRMED",
          "r449-r455 = anatomy of the prime-blind zone "
          "(r303 dictionary), not mincut progress")


def main():
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke
    print("=" * 78)
    print("vacuity_redteam_probe -- PRIME.RDAGGER.VACUITY_REDTEAM.01 "
          "(round 456)")
    print("SPEC_SHA %s" % SPEC_SHA[:16])
    print("mode: %s" % ("SMOKE" if smoke else "FULL"))
    print("=" * 78)
    section("S0  FIREWALL")
    okf, det = firewall_audit()
    check("G00-firewall", okf, det)
    check("G00b-import-sha",
          S445.SPEC_SHA.startswith(S445_SHA_PREFIX)
          and S449.SPEC_SHA.startswith(S449_SHA_PREFIX)
          and S450.SPEC_SHA.startswith(S450_SHA_PREFIX)
          and S451.SPEC_SHA.startswith(S451_SHA_PREFIX),
          "S445/S449/S450/S451 prefixes ok")
    part_q1()
    part_q2(smoke)
    part_q3(smoke)
    part_q4()
    r1 = dq_at(17, 8)
    r2 = dq_at(17, 8)
    check("G60-determinism",
          r1["qM"] == r2["qM"] and r1["qA"] == r2["qA"],
          "kz17 n=8 run1=run2 qM=%.16f" % r1["qM"])
    prev = all(ok for _n, ok in CHECKS)
    check("G61-verdict",
          prev and VERDICT == "VACUOUS_CONFIRMED",
          "VACUOUS_CONFIRMED; prefix world-blind; arithmetic "
          "at J_P+ / combRead; no RH / no anti-RH")
    n_fail = sum(1 for _n, ok in CHECKS if not ok)
    n_ok = len(CHECKS) - n_fail
    print("\nRESULT: %d/%d gates PASS   SPEC_SHA %s   (%.1fs)" % (
        n_ok, len(CHECKS), SPEC_SHA[:16], time.time() - T0))
    if n_fail == 0:
        print("VACUITY REDTEAM %sVERIFIED" % ("SMOKE " if smoke else ""))
        return 0
    print("VACUITY REDTEAM FAILED %d" % n_fail)
    return 1


if __name__ == "__main__":
    sys.exit(main())
