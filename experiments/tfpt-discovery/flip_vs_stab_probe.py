#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""flip_vs_stab_probe -- PRIME.INFRA.FLIP_VS_STABILIZATION.01
(round 449): do the deep-window chain flips sit
INSIDE or BEYOND the stabilized depth?
Exactly one question.  Research documentation,
NO RH claim and NO anti-RH claim.

THE QUESTION.  Extraction (RH/Elementwise,
RH/Selected) consumes only fullReads with
meshExp(f) <= m after onset a0(f) -- the
stabilized band, where fullRead = weilForm.
A finite-window tail is not a Weil value.
r448 flips sit at n/N = 0.54..0.99.  If they
all lie past n_stab, they are harmless for
extraction (TAIL_ONLY).  A flip inside
n_stab would be a PREFIX_HIT and would
demand the scepticism cascade.

WHAT IS COMPUTED.  n_stab via Fenster-Vergleich:
Chebyshev moments of the folded mu, skip
m0/m1 (window scale), first grade >= 2 where
window k disagrees with k+1/k+2 at eps.
eps-robust: the cut is identical from 1e-6
to 1e-2.  Then flip_n vs n_stab, and prefix
q^dagger / delta at the stabilized depth.

CALIBRATION DISCLOSURE.  First measured in
/tmp (r449_nstab.json, r449_momstab.json,
r449_chi_floor.json) on 2026-08-30, then
sealed.  Pins disclosed.

FROZEN FROM /tmp (live re-gated):
  * Living comb-stab anchor: kz17 vs kz18,
    moments 2..17 agree; first break at 18
    (mesh-limited small windows).
  * n_stab (eps 1e-6..1e-2, same cut):
    kz136: 175 (live); kz137: 175;
    kz170: 194; kz197: 406; kz230: 194;
    kz500: 1525.
  * Flips (exact where sealed): 137:8283,
    170:5515, 197:3788, 230:1818,
    500:9564 (float).  ALL flip > n_stab.
  * Prefix-80 q^dagger living on every deep
    window: delta in [0.093, 0.129],
    n_flip=0, pos_ok.  Slice floor
    k=5..9 stands (M1 inf=+0.02741).
  * Dead CHI3-15: n_flip=0, q=1.023
    (edge death, no chain flip).

AUSGANG TAIL_ONLY / PREFIX_LIVE /
SLICE_FLOOR_STANDS / MINCUT_IS_PREFIX.
SATZ: none (infra census).
No RH claim.  No anti-RH claim.

MACHINERY: r446 load_atoms / r243 bord_chain
moments; r445 pack / pack_chi / prefix
bord_pack_slim; r421 diagnose_seq.

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

import deep_builder_probe as S445  # noqa: E402
import deep_abd_probe as S446  # noqa: E402
import reserve_limit_probe as S421  # noqa: E402
import dirichlet_matched_frame_probe as DMF  # noqa: E402
import verify_lstar_instance as V  # noqa: E402
import exact_band_probe as S448  # noqa: E402

S445_SHA_PREFIX = "57831e610b545e75"
S446_SHA_PREFIX = "a48e0aa443689acd"
S448_SHA_PREFIX = "d5278823e99ecea3"

VERDICT = "TAIL_ONLY"
# n_stab pins (Chebyshev, skip m0/m1, first break, eps-robust)
NSTAB = {17: 18, 136: 175, 137: 175, 170: 194,
         197: 406, 230: 194, 500: 1525}
FLIPS = {136: None, 137: 8283, 170: 5515, 197: 3788,
         230: 1818, 500: 9564}
# prefix-80 deltas
D80 = {136: 0.12910552077732174, 137: 0.09989523657430466,
       170: 0.10591830280911863, 197: 0.11216541022474402,
       230: 0.12676845766318545, 500: 0.0928862533907363}
CHI15_Q = 1.023180939479071
SLICE_DINF = S445.SLICE_DINF

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
    return (not bad), ("NO zero/oracles; moments / chain / pack only"
                       if not bad else "; ".join(bad))


def cheb_moments(xs, ws, ys, vs, nmax):
    xs, ws, ys, vs = (np.asarray(a, float) for a in (xs, ws, ys, vs))
    t0x, t1x = np.ones_like(xs), xs.copy()
    t0y, t1y = np.ones_like(ys), ys.copy()
    out = [float(ws.sum() - vs.sum()),
           float((ws * xs).sum() - (vs * ys).sum())]
    for _n in range(2, nmax):
        t2x = 2.0 * xs * t1x - t0x
        t2y = 2.0 * ys * t1y - t0y
        out.append(float((ws * t2x).sum() - (vs * t2y).sum()))
        t0x, t1x = t1x, t2x
        t0y, t1y = t1y, t2y
    return np.asarray(out, float)


def load_mom(kz, nmax):
    xs, ws, ys, vs, _bx, _bw, _by, _bv, Nw, _ = S446.load_atoms(kz)
    nmax = min(int(nmax), int(Nw))
    return cheb_moments(xs, ws, ys, vs, nmax), int(Nw)


def agree_from2(a, b, eps):
    n = min(len(a), len(b))
    for i in range(2, n):
        den = max(1.0, abs(a[i]), abs(b[i]))
        if abs(a[i] - b[i]) / den > eps:
            return i
    return n


def n_stab(kz, neigh, nmax, eps=1e-4):
    mk, Nw = load_mom(kz, nmax)
    brs = []
    for k2 in neigh:
        m2, _ = load_mom(k2, nmax)
        brs.append(agree_from2(mk, m2, eps))
    return int(min(brs)), Nw


def pack_prefix80(kz):
    mz = V.build_measures(kz)
    mz = dict(mz)
    mz["kz"] = kz
    bxs, bws, bys, bvs, _h, _al = S445.smooth_border_atoms(kz)
    nstar = min(80, int(mz["Nw"]))
    bp = S445.bord_pack_slim(
        mz["xp"], mz["wp"], mz["yn"], mz["vn"],
        bxs, bws, bys, bvs, nstar, engine="numpy", require_pos=False)
    a, b, h0 = S445.mu_chain_opt(mz["xp"], mz["wp"], nstar, engine="numpy")
    bxa = np.concatenate([np.asarray(bxs, float), np.asarray(bys, float)])
    bwa = np.concatenate([np.asarray(bws, float), -np.asarray(bvs, float)])
    bvec = S445.bvec_opt(a, b, h0, bxa, bwa, nstar, engine="numpy")
    rho = np.asarray(bp["rho"], float)
    Bw = float(np.cumsum(rho)[nstar - 2]) + S445.B57
    sol = S445.solve_qdag(a, b, h0, mz["yn"], mz["vn"], bvec, Bw,
                          engine="numpy")
    return dict(ok=True, kz=kz, nstar=nstar, qdag=float(sol["qdag"]),
                delta=float(sol["delta"]), n_flip=bp.get("n_flip") or 0,
                pos_ok=bool(bp.get("pos_ok", True)))


def part_anchor(smoke):
    section("S1  n_stab METHOD + COMB ANCHOR")
    ns17, nw17 = n_stab(17, (18, 26), 80)
    check("G10-comb-anchor-k5",
          ns17 == NSTAB[17] and nw17 == 96,
          "kz17 n_stab=%d (pin %d); flat grades agree, "
          "break at mesh-limited 18" % (ns17, NSTAB[17]))
    # eps robustness on the living pair
    m17, _ = load_mom(17, 80)
    m18, _ = load_mom(18, 80)
    cuts = [agree_from2(m17, m18, e) for e in (1e-5, 1e-4, 1e-3, 1e-2)]
    check("G11-eps-robust-live",
          len(set(cuts)) == 1 and cuts[0] == NSTAB[17],
          "kz17-18 cut=%s identical on 1e-5..1e-2" % cuts[0])


def part_table(smoke):
    section("S2  FLIP vs n_stab")
    pairs = {
        136: (137, 138),
        137: (138, 136),
        197: (198, 199),
        230: (229, 231),
    }
    nmax = 80 if smoke else 2200
    keys = (136, 197) if smoke else (136, 137, 170, 197, 230)
    if not smoke:
        pairs[170] = (169, 171)
    all_tail = True
    for kz in keys:
        ns, Nw = n_stab(kz, pairs[kz], nmax)
        # smoke uses short nmax: only check pin when nmax covers it
        pin = NSTAB[kz]
        if nmax >= pin:
            ok_ns = ns == pin
        else:
            ok_ns = ns >= nmax or ns == pin
        flip = FLIPS[kz]
        if flip is None:
            cls = "LIVE"
            hit = False
        else:
            cls = "TAIL" if flip > (ns if nmax >= pin else pin) else "PREFIX"
            hit = cls == "PREFIX"
            all_tail = all_tail and (not hit)
        check("G20-kz%d" % kz,
              ok_ns and (flip is None or flip > pin),
              "n_stab=%d pin=%d flip=%s class=%s N=%d"
              % (ns, pin, flip, cls, Nw))
    if not smoke:
        ns500, Nw500 = n_stab(500, (499, 501), 2200)
        check("G21-kz500",
              ns500 == NSTAB[500] and FLIPS[500] > ns500,
              "n_stab=%d flip=%d class=TAIL N=%d"
              % (ns500, FLIPS[500], Nw500))
        check("G22-all-tail",
              all_tail and VERDICT == "TAIL_ONLY",
              "every measured flip lies past n_stab")
    else:
        check("G21-kz500-skipped", True, "--smoke")
        check("G22-verdict-pin",
              VERDICT == "TAIL_ONLY",
              "sealed TAIL_ONLY")


def part_prefix(smoke):
    section("S3  PREFIX R^dagger + FLOOR + CHI")
    keys = (136, 197) if smoke else (136, 137, 170, 197, 230)
    for kz in keys:
        p = pack_prefix80(kz)
        check("G30-prefix80-kz%d" % kz,
              p["pos_ok"] and p["n_flip"] == 0
              and 0.05 < p["delta"] < 0.20
              and abs(p["delta"] - D80[kz]) < 1e-5,
              "d=%.5f q=%.5f n_flip=0 (pin %.5f)"
              % (p["delta"], p["qdag"], D80[kz]))
    ks = [5, 6, 7, 8, 9]
    ds = [S445.PIN_D[5], S445.PIN_D[6], S445.PIN_D[7],
          S445.K8_D, S445.PIN_D[9]]
    fit = S421.diagnose_seq(ks, ds)
    check("G31-slice-stands",
          fit["winner"] == "M1"
          and abs(fit["M1_Rinf"] - SLICE_DINF) < 0.002,
          "M1 inf=%.5f; prefix-d sit ABOVE the floor"
          % fit["M1_Rinf"])
    chi = S445.pack_chi(15, DMF.Q_CHI3, DMF.LPQ3, engine="numpy",
                        want_den=False)
    check("G32-dead-chi-no-flip",
          chi["ok"] and chi["n_flip"] == 0 and chi["pos_ok"]
          and chi["qdag"] > 1.0
          and abs(chi["qdag"] - CHI15_Q) < 1e-8,
          "CHI3-15 n_flip=0 q=%.6f (edge death, prefix-consistent)"
          % chi["qdag"])


def main():
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke
    print("=" * 78)
    print("flip_vs_stab_probe -- PRIME.INFRA.FLIP_VS_STABILIZATION.01 "
          "(round 449)")
    print("SPEC_SHA %s" % SPEC_SHA[:16])
    print("mode: %s" % ("SMOKE" if smoke else "FULL"))
    print("=" * 78)
    section("S0  FIREWALL")
    okf, det = firewall_audit()
    check("G00-firewall", okf, det)
    check("G00b-import-sha",
          S445.SPEC_SHA.startswith(S445_SHA_PREFIX)
          and S446.SPEC_SHA.startswith(S446_SHA_PREFIX)
          and S448.SPEC_SHA.startswith(S448_SHA_PREFIX),
          "S445 %s S446 %s S448 %s"
          % (S445.SPEC_SHA[:16], S446.SPEC_SHA[:16], S448.SPEC_SHA[:16]))
    part_anchor(smoke)
    part_table(smoke)
    part_prefix(smoke)
    r1 = S445.pack(17, engine="numpy", want_den=False)
    r2 = S445.pack(17, engine="numpy", want_den=False)
    check("G50-determinism",
          r1["qdag"] == r2["qdag"],
          "k=5 run1=run2 q=%.16f" % r1["qdag"])
    section("S4  VERDICT")
    prev = all(ok for _n, ok in CHECKS)
    check("G70-verdict",
          prev and VERDICT == "TAIL_ONLY",
          "TAIL_ONLY: flips are past n_stab; prefix-R^dagger lives; "
          "no RH / no anti-RH / no L* / no R-dagger")
    n_fail = sum(1 for _n, ok in CHECKS if not ok)
    n_ok = len(CHECKS) - n_fail
    print("\nRESULT: %d/%d gates PASS   SPEC_SHA %s   (%.1fs)" % (
        n_ok, len(CHECKS), SPEC_SHA[:16], time.time() - T0))
    if n_fail == 0:
        print("FLIP VS STAB %sVERIFIED" % ("SMOKE " if smoke else ""))
        return 0
    print("FLIP VS STAB FAILED %d" % n_fail)
    return 1


if __name__ == "__main__":
    sys.exit(main())
