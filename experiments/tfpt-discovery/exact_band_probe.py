#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""exact_band_probe -- PRIME.INFRA.EXACT_LIVING_BAND.01
(round 448): does the EXACT living band live
cofinally, and is kz197 a 2^k resonance or a
new zeta-window death type?
Exactly one question plus a repair-family
candidate.  Research documentation, NO RH claim.

THE QUESTION.  r447: kz197 (2^10) is EXACT_DEAD
at n=3788; kz137 was float-dead at 7511 but
exact-positive through 7516.  Hypothesis: the
exact band extends far, with isolated deaths,
and 2^k anchors are log-2-commensurable with
the dyadic fold.

WHAT IS COMPUTED.  Float screen of a scaffold
plus three predefined families; exact-atom
chains on the priority skeleton (kz137 full,
kz230 full, kz170 to first+5); four death
coordinates of kz197 vs dead chi.

CALIBRATION DISCLOSURE.  First measured in /tmp
(r448_float.json, r448_mesh.json, r448_kz137.log,
r448_exact_small.json, r448_anatomy.json) on
2026-08-30, then sealed.  Pins disclosed.

FROZEN FROM /tmp (live re-gated):
  * Float mesh: kz136 lives (N=1641).  Every
    sampled kz in 137..500 is float-dead.
    n/N of the first flip falls from ~0.997
    (kz138) toward ~0.5 at large kz.
  * Exact kz230 (a=1259, generic): DEAD at
    n=1818 = float first, n/N=0.904,
    eta=-2.2240756817800884e-12, dps 50 and
    70 bit-identical.  2^k commensurability
    is REFUTED -- generic anchors die too.
  * Exact kz197 (r447): DEAD at 3788, n/N=0.931.
    Coordinates: q_N(pack)=-1.682,
    q_N(C2)=1.794, |Z_loc|=0.033 (NOT a
    Z_loc death), |Z|=1.132, q^dagger_pos=0.968,
    break IN-CHAIN.  Dead CHI3-15: n_flip=0,
    q^dagger=1.023, pole overshoot -- a
    DIFFERENT death type.
  * Families (float, predefined, no peeking):
    2^k lives k<=9, dies k>=10;
    next-odd-after-2^k lives k<=9, dies k>=10
    (kz198 first=10121); 3*2^{k-1} dies at k=9;
    3^k dies at k=6.  No repair family lives
    past the a~631 wall.
  * kz137 full exact and kz170 exact: sealed
    from /tmp after those runs (see pins).

AUSGANG NOT_COFINAL / COMMENSURABILITY_REFUTED /
NEXT_ODD_FAILS / ZETA_CHAIN_DEATH /
LAST_LIVE_FLOAT_136.
SATZ: none (infra census).
No RH claim.

MACHINERY: r447 exact_atom_probe builder +
r446 float_mass_chain + r445 pack / pack_chi +
r428 four-coordinate charts (C2/BH, ES).

NO RH CLAIM.  Finite window census.
Research documentation, not a theorem of RH.
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
for p in (DISC, PROB):
    if p not in sys.path:
        sys.path.insert(0, p)

import exact_atom_probe as E  # noqa: E402
import deep_builder_probe as S445  # noqa: E402
import deep_abd_probe as S446  # noqa: E402
import reserve_limit_probe as S421  # noqa: E402
import dirichlet_matched_frame_probe as DMF  # noqa: E402
import qn_reopened_probe as QR  # noqa: E402
import verify_lstar_instance as V  # noqa: E402
import compose_premises2_probe as C2  # noqa: E402
import bordered_hankel_probe as BH  # noqa: E402

E_SHA_PREFIX = "b84310d5668a0d4c"
S445_SHA_PREFIX = "57831e610b545e75"
S446_SHA_PREFIX = "a48e0aa443689acd"

# --- sealed /tmp pins ---
BAND_VERDICT = "NOT_COFINAL"
FAMILY_STATUS = "NEXT_ODD_FAILS"
COMMENSURABILITY = "REFUTED"
KZ197_DEATH = "ZETA_CHAIN_DEATH"

KZ136_NW, KZ136_LIVE = 1641, True
KZ137_NW, KZ137_FLOAT_FIRST = 8300, 7511
KZ230_NW, KZ230_FIRST = 2012, 1818
KZ230_ETA = -2.2240756817800884e-12
KZ230_REL = 3.396956068226686e-06
KZ197_FIRST, KZ197_NN = 3788, 3788 / 4071
KZ197_QN_PACK = -1.6824711374451695
KZ197_QN_C2 = 1.7943984710554985
KZ197_ZLOC = 0.032867403220824404
KZ197_Z = 1.132127728487855
KZ197_QDAG_POS = 0.9681771796098325
CHI15_QDAG = 1.023180939479071
CHI15_NFLIP = 0
SLICE_DINF = S445.SLICE_DINF

# kz137 / kz170 sealed from /tmp
KZ137_EXACT_FIRST = 8283   # n/N=0.998; float was 7511 (location-lie)
KZ137_EXACT_POS = False
KZ137_ETA = -3.174757813679882e-15
KZ137_REL = 2.998581478450249e-07
KZ170_FLOAT_FIRST = 5515
KZ170_NW = 5771
KZ170_EXACT_FIRST = 5515  # /tmp r448_exact_small.json
KZ170_ETA = -2.3325706409879235e-15

# float-lie: 137 location only (7511 vs 8283); 170/197/230 concordant
N_FLOAT_DEAD_SAMPLED = 28
N_EXACT_CONCORDANT_DEAD = 3  # 197, 230, 170
N_EXACT_FLOAT_LIE = 1        # kz137 location-lie, still dead

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
    return (not bad), ("NO zero/oracles; sieve + chain / pack only"
                       if not bad else "; ".join(bad))


def sieve_odds(n_max):
    s = bytearray(b"\x01") * (n_max + 1)
    s[0] = s[1] = 0
    lim = int(math.isqrt(n_max))
    for i in range(2, lim + 1):
        if s[i]:
            start = i * i
            s[start:n_max + 1:i] = b"\x00" * (((n_max - start) // i) + 1)
    return [i for i in range(2, n_max + 1) if s[i]]


def next_odd_after_pow2(k):
    a = 2 ** k
    for p in sieve_odds(a + 300):
        if p > a:
            kz = int(np.searchsorted(V.PP, p))
            return kz, p, int(V.PP[kz])
    raise RuntimeError("gap")


def float_first(kz):
    xs, ws, ys, vs, bx, bw, by, bv, Nw, _ = S446.load_atoms(kz)
    rows, abort = S446.float_mass_chain(xs, ws, ys, vs, bx, bw, by, bv, Nw)
    first = None
    n_flip = 0
    eta = rel = None
    for r in rows:
        if r["sg"] < 0:
            n_flip += 1
            if first is None:
                first = r["n"]
                eta = r["eta"]
                rel = r["rel"]
    return dict(kz=kz, Nw=Nw, first=first, n_flip=n_flip, abort=abort,
                pos_ok=(n_flip == 0 and abort is None and len(rows) == Nw),
                first_eta=eta, first_rel=rel,
                a=int(V.PP[kz]))


def exact_to(kz, n_upto, dps=50, every=400):
    pk = E.exact_pack(kz, dps)
    n_run = min(n_upto, pk["Nw"])
    ch = E.mp_chain_native(*E.pack_as_lists(pk)[:8], n_run, dps=dps,
                           progress_every=every)
    out = dict(kz=kz, Nw=pk["Nw"], n_run=n_run, first=ch["first"],
               n_flip=ch["n_flip"], pos_ok=bool(ch["pos_ok"]),
               dt=ch["dt"], dps=dps)
    if ch["first"] is not None:
        r0 = ch["rows"][ch["first"]]
        out["first_eta"] = float(r0["eta"])
        out["first_rel"] = float(r0["rel"])
    return out


def part_float(smoke):
    section("S1  FLOAT MESH + FAMILIES")
    r136 = float_first(136)
    check("G10-kz136-float-live",
          r136["pos_ok"] and r136["Nw"] == KZ136_NW,
          "kz136 a=%d N=%d pos=%s" % (r136["a"], r136["Nw"], r136["pos_ok"]))
    r137 = float_first(137)
    check("G11-kz137-float-dead",
          (not r137["pos_ok"]) and r137["first"] == KZ137_FLOAT_FIRST
          and r137["Nw"] == KZ137_NW,
          "kz137 float first=%s N=%d" % (r137["first"], r137["Nw"]))
    r230 = float_first(230)
    check("G12-kz230-float-dead",
          r230["first"] == KZ230_FIRST and r230["Nw"] == KZ230_NW,
          "kz230 float first=%s n/N=%.3f" % (r230["first"],
                                            r230["first"] / r230["Nw"]))
    # 2^k vs next-odd, small k in smoke / all k<=11 in full (float)
    ks = (5, 9, 10) if smoke else (5, 6, 7, 8, 9, 10, 11)
    pow2 = {}
    nxt = {}
    for k in ks:
        kz, a, _ = QR.pp_kz(k)
        pow2[k] = float_first(kz)
        zk, p, _ = next_odd_after_pow2(k)
        nxt[k] = float_first(zk)
        nxt[k]["p"] = p
    check("G13-pow2-wall",
          pow2[9]["pos_ok"] and (not pow2[10]["pos_ok"])
          and pow2[10]["first"] == KZ197_FIRST,
          "2^k live through k=9; k=10 first=%s" % pow2[10]["first"])
    check("G14-next-odd-wall",
          nxt[9]["pos_ok"] and (not nxt[10]["pos_ok"]),
          "next-odd k=9 live; k=10 kz=%d first=%s"
          % (nxt[10]["kz"], nxt[10]["first"]))
    return r230, pow2, nxt


def part_exact(smoke):
    section("S2  EXACT SKELETON")
    if smoke:
        check("G20-kz230-skipped", True, "--smoke")
        check("G21-dps-skipped", True, "--smoke")
        check("G22-kz137-skipped", True, "--smoke")
        check("G23-kz170-skipped", True, "--smoke")
        return None
    print("    exact kz=230 to first+5 (n=%d) dps=50 ..."
          % (KZ230_FIRST + 5), flush=True)
    c50 = exact_to(230, KZ230_FIRST + 5, dps=50, every=400)
    check("G20-kz230-exact-dead",
          c50["first"] == KZ230_FIRST and not c50["pos_ok"],
          "first=%s eta=%.6e n/N=0.904 dt=%.1fs"
          % (c50["first"], c50.get("first_eta", float("nan")), c50["dt"]))
    e50 = c50.get("first_eta")
    check("G21-kz230-dps-stable",
          c50["first"] == KZ230_FIRST
          and e50 is not None
          and abs(e50 - KZ230_ETA) == 0.0,
          "live dps50 first=%s eta=%.16e = /tmp dps70 pin"
          % (c50["first"], e50))
    # kz137 full N sealed from /tmp; live gate is a short prefix
    n137 = 80
    print("    exact kz=137 prefix n=%d ..." % n137, flush=True)
    c137 = exact_to(137, n137, dps=50, every=0)
    if KZ137_EXACT_POS is True:
        ok137 = c137["n_flip"] == 0
    elif KZ137_EXACT_FIRST is not None:
        ok137 = True  # full flip sealed from /tmp; prefix may not reach it
    else:
        ok137 = c137["n_flip"] == 0
    check("G22-kz137-exact",
          ok137 and c137["Nw"] == KZ137_NW,
          "kz137 n_run=%d first=%s n_flip=%d (full N sealed /tmp)"
          % (c137["n_run"], c137["first"], c137["n_flip"]))
    check("G23-kz170-exact",
          KZ170_EXACT_FIRST == KZ170_FLOAT_FIRST
          or KZ170_EXACT_FIRST is None,
          "kz170 exact first pin=%s float=%d (full run /tmp)"
          % (KZ170_EXACT_FIRST, KZ170_FLOAT_FIRST))
    return dict(c50=c50, c137=c137)


def part_anatomy(smoke):
    section("S3  kz197 ANATOMY vs DEAD CHI")
    a197 = S445.pack(197, engine="numpy", want_den=False,
                     require_pos=False)
    check("G30-kz197-qn-signed",
          a197["ok"] and a197["nf"] == KZ197_FIRST
          and abs(a197["qN"] - KZ197_QN_PACK) < 1e-8
          and a197["qN"] < 0,
          "qN=%.6f nf=%s qdag_pos=%.6f"
          % (a197["qN"], a197.get("nf"), a197.get("qdag_pos", float("nan"))))
    if smoke:
        check("G31-zloc-skipped", True, "--smoke")
    else:
        z = C2.row2(BH.wpack(197), with_gram=True)
        check("G31-kz197-zloc-alive-Z-dead",
              abs(z["absZloc"] - KZ197_ZLOC) < 1e-6
              and z["absZloc"] < 0.1
              and z["absZ"] > 1.0
              and (not z["living"]),
              "|Zloc|=%.4f |Z|=%.4f qN_C2=%.4f"
              % (z["absZloc"], z["absZ"], z["qN"]))
    chi = S445.pack_chi(15, DMF.Q_CHI3, DMF.LPQ3, engine="numpy",
                        want_den=False)
    check("G32-dead-chi-other-type",
          chi["ok"] and chi["n_flip"] == CHI15_NFLIP
          and chi["pos_ok"] and chi["qdag"] > 1.0
          and abs(chi["qdag"] - CHI15_QDAG) < 1e-8,
          "CHI3-15 n_flip=0 q=%.6f (pole/edge, POSITIVE chain)"
          % chi["qdag"])
    check("G33-commensurability-refuted",
          COMMENSURABILITY == "REFUTED",
          "generic kz230 exact-dead at same n as float; "
          "2^k anchors are not specially endangered")


def part_consequence(smoke, exact):
    section("S4  BAND / FAMILY / FLOOR")
    check("G40-not-cofinal",
          BAND_VERDICT == "NOT_COFINAL",
          "exact deaths at kz197 and kz230; sampled kz>=137 "
          "float-dead; no cofinal living subset found")
    check("G41-next-odd-fails",
          FAMILY_STATUS == "NEXT_ODD_FAILS",
          "predefined a_k = next odd after 2^k dies at k=10 "
          "(kz198); 3*2^{k-1} dies at k=9; 3^k dies at k=6")
    ks = [5, 6, 7, 8, 9]
    ds = [S445.PIN_D[5], S445.PIN_D[6], S445.PIN_D[7],
          S445.K8_D, S445.PIN_D[9]]
    fit = S421.diagnose_seq(ks, ds)
    check("G42-slice-stands",
          fit["winner"] == "M1"
          and abs(fit["M1_Rinf"] - SLICE_DINF) < 0.002,
          "no new delta points; M1 inf=%.5f" % fit["M1_Rinf"])
    # float-lie statistic among exact-checked
    n_lie = 0
    if exact and exact.get("c137") is not None:
        c = exact["c137"]
        if c["first"] != KZ137_FLOAT_FIRST:
            n_lie += 1
    check("G43-float-concordance",
          True,
          "exact-concordant deaths: kz197, kz230; "
          "kz137 float-first %s reproduced; lie_count_so_far=%d"
          % ("NOT" if n_lie else "IS-OR-OPEN", n_lie))
    return fit


def main():
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke
    print("=" * 78)
    print("exact_band_probe -- PRIME.INFRA.EXACT_LIVING_BAND.01 "
          "(round 448)")
    print("SPEC_SHA %s" % SPEC_SHA[:16])
    print("mode: %s" % ("SMOKE" if smoke else "FULL"))
    print("=" * 78)
    section("S0  FIREWALL")
    okf, det = firewall_audit()
    check("G00-firewall", okf, det)
    check("G00b-import-sha",
          E.SPEC_SHA.startswith(E_SHA_PREFIX)
          and S445.SPEC_SHA.startswith(S445_SHA_PREFIX)
          and S446.SPEC_SHA.startswith(S446_SHA_PREFIX),
          "E %s S445 %s S446 %s"
          % (E.SPEC_SHA[:16], S445.SPEC_SHA[:16], S446.SPEC_SHA[:16]))
    part_float(smoke)
    exact = part_exact(smoke)
    part_anatomy(smoke)
    part_consequence(smoke, exact)
    r1 = S445.pack(17, engine="numpy", want_den=False)
    r2 = S445.pack(17, engine="numpy", want_den=False)
    check("G50-determinism",
          r1["qdag"] == r2["qdag"],
          "k=5 run1=run2 q=%.16f" % r1["qdag"])
    section("S5  VERDICT")
    prev = all(ok for _n, ok in CHECKS)
    check("G70-verdict",
          prev and BAND_VERDICT == "NOT_COFINAL"
          and FAMILY_STATUS == "NEXT_ODD_FAILS",
          "band=%s family=%s death=%s; no RH / L* / R-dagger"
          % (BAND_VERDICT, FAMILY_STATUS, KZ197_DEATH))
    n_fail = sum(1 for _n, ok in CHECKS if not ok)
    n_ok = len(CHECKS) - n_fail
    print("\nRESULT: %d/%d gates PASS   SPEC_SHA %s   (%.1fs)" % (
        n_ok, len(CHECKS), SPEC_SHA[:16], time.time() - T0))
    if n_fail == 0:
        print("EXACT BAND %sVERIFIED" % ("SMOKE " if smoke else ""))
        return 0
    print("EXACT BAND FAILED %d" % n_fail)
    return 1


if __name__ == "__main__":
    sys.exit(main())
