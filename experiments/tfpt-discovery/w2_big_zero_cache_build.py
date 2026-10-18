#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""w2_big_zero_cache_build -- DISCLOSED BUILDER of the big verified-zero
cache consumed by w2_full_zero_closure_probe.py (EXPLORATION ONLY,
experiments/; NOT a frozen probe -- this is the data-procurement step,
separate from the frozen closure run, exactly as j16_zero_cache_build.py
was for CLXXXIX).

WHY.  CXCIII (w2_verified_supply_consumption_probe) closed the W2
recomposed certificate on 16/67 surface rungs at N_Z = 7000 and priced
the remainder PURELY in verified zeros (TAILB ~ 4 S_Delta
Sum_{gamma>T_c} 1/gamma^2; anatomy med ~1e6 / max ~8.5e6 ordinates).
mpmath.zetazero at index ~1e6+ is far too slow, so the cache is
procured from EXTERNAL-CITED verified tables:

  SEGMENT 1 (n = 1 .. 2,001,052): A. M. Odlyzko, "Tables of zeros of
    the Riemann zeta function", zeros6 -- "The first 2,001,052 zeros
    of the Riemann zeta function, accurate to within 4*10^(-9)"
    (https://www-users.cse.umn.edu/~odlyzko/zeta_tables/zeros6.gz).
    Printed to 9 decimals; declared per-ordinate error budget
    E1 = 4e-9 + 5e-10 (table accuracy + print quantisation).
  SEGMENT 2 (n = 2,001,053 .. N_BIG): LMFDB, "Zeros of zeta(s)"
    (https://www.lmfdb.org/zeros/zeta/ -- D. J. Platt's rigorously
    verified zeros, stored to ~1e-30; list endpoint
    /zeros/zeta/list?limit=L&t=T prints 37 decimals).  Declared
    per-ordinate error budget E2 = gamma * 2^-50 (float64 parse
    rounding dominates; the table error ~1e-30 is negligible).

PEDIGREE: every ordinate is far below T0 = 3e12, hence ON the critical
line unconditionally (Platt-Trudgian 2021, Bull. LMS 53).  The cache is
DATA with a declared per-segment error budget, not an oracle; the
consuming probe carries the ordinate-perturbation pad
4*S_Delta*(vmax/gamma^2 + 2/gamma^3)*e_k per zero (window-transform
Lipschitz bound |d/dgamma 4 Re phihat| <= 4 S_Delta (vmax gamma + 2)
/ gamma^3) in every TAILB.

ACCURACY DEMAND (quantified): with S_Delta <= 5, vmax <= 16 and the
segment budgets above, the total pad is
  4*S_Delta*(vmax*Sum e_k/gamma_k^2 + 2*Sum e_k/gamma_k^3) < 2e-8,
i.e. > 2.5 dex below the smallest wall margin on the ladder
(min m ~ 7e-6) -- the certification battery below re-verifies the
measured pad numbers and the probe prints them per rung.

MODES:
  plan     -- Step-2 demand-side economy: build the 67+8 W2 rungs
              (CLXXXV machinery verbatim, read-only), compute per
              (rung, cut) the jump mass S_Delta of phi_cont and the
              exact prime-side margin, then invert the tail budget
              TAILB_plan(T) = 4 S_Delta AbelMain(T) + beyond-T0 + pad
              for the minimal T_c / zero count per rung (min over the
              frozen cut ladder), at margin factors f = 0.9/0.7/0.5.
              PRINTS the procurement decision; writes nothing.
  fetch    -- parse Odlyzko zeros6 (local gz; re-downloads if absent),
              fetch the LMFDB remainder up to N_BIG in pages of 1e5
              (paced), save verified_zeros_big.npy + meta json.
  certify  -- certification battery on the saved cache:
              B1 census + strict monotonicity + gamma_1 identity;
              B2 Rosser corridor per index, both sides (unconditional
                 kill-grade: Rosser 1941 constants, CLXXXI verbatim);
              B3 Backlund/theta count consistency per index:
                 |theta(gamma_k)/pi + 1 - k| <= 2.8 on the whole cache
                 (asymptotic theta, remainder < 1e-9 here; the 2.8 bar
                 is the empirical |S(T)| ceiling in this T-range,
                 reported as anatomy -- B2 stays the unconditional ward);
              B4 seam + overlap: Odlyzko vs LMFDB and vs the CLXXXIX
                 mpmath 7000-cache (worst |Delta gamma|);
              B5 independent mpmath |zeta(1/2 + i gamma)| spot checks
                 at 40 geomspace indices, dps 20 (worst reported,
                 bar 1e-6);
              B6 spacing sanity (min/max gap vs local mean gap) +
                 Sum 1/gamma^2 partial-vs-full anatomy.
              Writes the certification block into the meta json.

Run:  .venv/bin/python w2_big_zero_cache_build.py plan|fetch|certify
      (from experiments/tfpt-discovery/; wall-clock: plan ~2 min,
      fetch ~15 min network-bound, certify ~2 min)

No wall output, no target eigendata, no RNG anywhere in this builder.
Stdout only, plus the two cache artefacts (npy + meta json).  NO RH
claim -- this is data procurement with pedigree.
"""

import hashlib
import json
import math
import os
import subprocess
import sys
import time
import urllib.request

import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
_VERIFY = os.path.abspath(os.path.join(_HERE, "..", "..",
                                       "verification"))
sys.path.insert(0, _HERE)
sys.path.insert(0, _VERIFY)

ODLYZKO_URL = ("https://www-users.cse.umn.edu/~odlyzko/zeta_tables/"
               "zeros6.gz")
ODLYZKO_GZ = os.path.join(_HERE, "odlyzko_zeros6.gz")
ODLYZKO_N = 2_001_052
ODLYZKO_ERR = 4.0e-9 + 5.0e-10
LMFDB_URL = "https://www.lmfdb.org/zeros/zeta/list?limit=%d&t=%s"
LMFDB_PAGE = 100_000
LMFDB_PACE_S = 0.35
LMFDB_ERR_ULP = 2.0 ** -50          # * gamma, float64 parse rounding
OUT_NPY = os.path.join(_HERE, "verified_zeros_big.npy")
OUT_META = os.path.join(_HERE, "verified_zeros_big_meta.json")
OLD_NPY = os.path.join(_HERE, "verified_zeros_n7000.npy")

# frozen procurement target (decided by `plan`: worst rung kz 326
# needs N_req = 1.904e7 at margin factor f = 0.9; 2.0e7 gives ~5%
# headroom over the main-term planning approximation; see the plan
# output quoted in the closure probe's scouting disclosure):
N_BIG = 20_000_000

GAMMA1 = 14.134725141734695
S_ABS_BAR = 2.8
ZETA_TOL = 1.0e-6
NS_ZETA = 40
CORR_EPS = 1.0e-6
PLAN_FACTORS = (0.9, 0.7, 0.5)
PLAN_GEO = 1.001


def theta_asym(t):
    """Riemann-Siegel theta, asymptotic expansion; remainder
    < 1/(t^5) for t >= 14 (next term 31/(80640 t^5))."""
    t = np.asarray(t, float)
    return (0.5 * t * np.log(t / (2.0 * math.pi)) - 0.5 * t
            - math.pi / 8.0 + 1.0 / (48.0 * t)
            + 7.0 / (5760.0 * t ** 3))


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for blk in iter(lambda: fh.read(1 << 20), b""):
            h.update(blk)
    return h.hexdigest()


# --------------------------------------------------------------- plan
def mode_plan():
    import subgamma_fourier_bound_probe as subg
    import w2_pairing_structure_probe as w2
    import w2_verified_supply_consumption_probe as cons
    import v563_paper2_readouts as core
    t0 = time.time()
    s2t = subg.s2_tail()
    print("PLAN -- demand-side economy on the 67+8 W2 ladder")
    print("  (CLXXXV/CXCIII machinery read-only; main-term+corridor "
          "tail inversion; beyond-T0 %.3e per unit e^{vmax/2} S)"
          % (4.0 * s2t))

    # abel table: Sum_{gamma > T} 1/gamma^2 upper bound on a fine
    # geometric grid (c = 1/t^2 monotone -> any grid is rigorous;
    # finer = tighter), n_start = exact count at T (cache census).
    def abel_at(tc, n_at_tc):
        ng = int(math.ceil(math.log(subg.T0_RH / tc)
                           / math.log(PLAN_GEO))) + 1
        tg = tc * PLAN_GEO ** np.arange(ng + 1)
        tg[-1] = subg.T0_RH
        return subg.abel_upper(tg, 1.0 / tg[:-1] ** 2,
                               n_start=float(n_at_tc))

    # T ladder for inversion (planning table)
    T_lad = np.geomspace(2.0e4, 3.0e7, 160)
    N_lad = subg.n_main(T_lad)          # planning count (main term)
    A_lad = np.array([abel_at(t, max(subg.n_lo(np.array([t]))[0], 0))
                      for t in T_lad])
    print("  abel table built (%d T-points)  [%.1f s]"
          % (len(T_lad), time.time() - t0))

    rungs = []
    for kz in range(2, w2.KZMAX + 1):
        r = w2.build_rung(kz)
        if r is not None:
            rungs.append(r)
    rungs.sort(key=lambda r: (r["h"], r["kz"]))
    print("  surface rungs: %d  [%.1f s]" % (len(rungs),
                                             time.time() - t0))
    lam_ext = core.von_mangoldt_table(w2.TAB_EXT)
    NNx = np.nonzero(lam_ext > 0.0)[0]
    EXT = dict(lam=lam_ext, NN=NNx,
               U=np.log(NNx.astype(float)),
               MU=2.0 * lam_ext[NNx] / np.sqrt(NNx.astype(float)))
    EXT["G"] = np.diff(EXT["U"])
    new_kz = []
    for kz in range(2, min(w2.KZ_SCAN_MAX, len(EXT["NN"]) - 2)):
        a_ = float(EXT["U"][kz])
        Xk = math.exp(2.0 * a_)
        if Xk > w2.TAB_EXT:
            break
        if Xk <= core.ATOM_MAX:
            continue
        D_k = 0.5 * float(EXT["G"][kz]) / float(core.NU_MAIN)
        Mk = int(math.ceil(a_ / D_k - 1.0e-9)) + 1
        if Mk % 2:
            Mk += 1
        if not (w2.H_HOLD[0] <= Mk // 2 <= w2.H_HOLD[1]):
            continue
        new_kz.append(kz)
    deep = []
    if new_kz:
        order = sorted(new_kz)
        pick = sorted(set(int(round(t)) for t in
                          np.linspace(0, len(order) - 1, 8)))
        for ii in pick:
            r = w2.build_rung(order[ii], ext=EXT)
            if r is not None:
                deep.append(r)
        deep.sort(key=lambda r: r["h"])
    print("  deep rungs: %d  [%.1f s]" % (len(deep),
                                          time.time() - t0))

    need = {f: [] for f in PLAN_FACTORS}
    worst = {f: (0.0, None) for f in PLAN_FACTORS}
    for r in rungs + deep:
        reads = []
        for A in w2.HEAD_A:
            sp = w2.demand_at_head(r, A)
            if sp is not None:
                reads.append(sp)
        spB = w2.split_at(r, r["ncB"])
        if spB is not None:
            reads.append(spB)
        m = r["m"]
        packs = []
        for sp in reads:
            pc = cons.phi_cont_of(r, sp)
            fixed = 4.0 * math.exp(0.5 * pc["vmax"]) * pc["sd"] * s2t \
                + 2.0e-8
            packs.append((pc["sd"], fixed))
        for f in PLAN_FACTORS:
            best = None
            for sd, fixed in packs:
                tgt = f * m - fixed
                if tgt <= 0.0:
                    continue
                idx = np.searchsorted(-4.0 * sd * A_lad, -tgt)
                if idx >= len(T_lad):
                    continue
                n_req = float(N_lad[idx])
                if best is None or n_req < best:
                    best = n_req
            if best is None:
                best = float("inf")
            need[f].append(best)
            if best > worst[f][0]:
                worst[f] = (best, r["kz"])
    all_r = rungs + deep
    for f in PLAN_FACTORS:
        arr = np.array(need[f])
        fin = arr[np.isfinite(arr)]
        print("  f = %.1f (TAILB <= %.1f m): med %.3e / max %.3e "
              "zeros (worst kz %s); closable at N <= 2,001,052 "
              "(Odlyzko alone) on %d/%d rungs"
              % (f, f, float(np.median(fin)), float(np.max(fin)),
                 str(worst[f][1]), int(np.sum(arr <= ODLYZKO_N)),
                 len(arr)))
        hard = sorted(((need[f][i], all_r[i]["kz"],
                        all_r[i]["h"], all_r[i]["m"])
                       for i in range(len(all_r))
                       if need[f][i] > ODLYZKO_N), reverse=True)
        for nr, kz, h, m in hard:
            print("      kz %-5d h %-5d m %.3e -> N_req %.3e"
                  % (kz, h, m, nr))
    print("  -> frozen procurement N_BIG = %d" % N_BIG)
    print("[PLAN done %.1f s]" % (time.time() - t0))


# -------------------------------------------------------------- fetch
def mode_fetch():
    t0 = time.time()
    if not os.path.exists(ODLYZKO_GZ):
        print("downloading %s ..." % ODLYZKO_URL)
        urllib.request.urlretrieve(ODLYZKO_URL, ODLYZKO_GZ)
    gz_sha = sha256_file(ODLYZKO_GZ)
    print("odlyzko zeros6.gz sha256 = %s" % gz_sha)
    txt = subprocess.run(["gunzip", "-c", ODLYZKO_GZ],
                         capture_output=True, check=True).stdout
    seg1 = np.array(txt.split(), dtype=float)
    del txt
    assert len(seg1) == ODLYZKO_N, len(seg1)
    assert np.all(np.diff(seg1) > 0.0)
    print("segment 1 (Odlyzko): %d ordinates, gamma_N = %.9f  [%.0f s]"
          % (len(seg1), seg1[-1], time.time() - t0))

    ckpt = OUT_NPY + ".partial.npy"
    if os.path.exists(ckpt):
        prev = np.load(ckpt)
        assert len(prev) >= ODLYZKO_N \
            and abs(prev[ODLYZKO_N - 1] - seg1[-1]) < 1e-6
        parts = [prev]
        n_have = len(prev)
        print("resuming from checkpoint: %d ordinates" % n_have)
    else:
        parts = [seg1]
        n_have = len(seg1)
    t_last = repr(float(parts[-1][-1]))
    req_log = []
    fail = 0
    n_ck = n_have
    while n_have < N_BIG:
        want = min(LMFDB_PAGE, N_BIG - n_have + 8)
        url = LMFDB_URL % (want, t_last)
        try:
            req = urllib.request.Request(
                url, headers={"User-Agent":
                              "tfpt-w2-closure/1.0 (research; "
                              "paced bulk read of verified zeros)"})
            with urllib.request.urlopen(req, timeout=180) as fh:
                body = fh.read()
            rows = body.split()
            if len(rows) < 2 or rows[0][:1] == b"<":
                raise ValueError("non-tabular response (%r...)"
                                 % body[:40])
            idx = np.array(rows[0::2], dtype=np.int64)
            gam = np.array(rows[1::2], dtype=float)
        except Exception as exc:            # noqa: BLE001
            fail += 1
            print("  ! fetch/parse error (%s), retry %d in %d s"
                  % (str(exc)[:120], fail, 20 * fail), flush=True)
            if fail > 10:
                raise
            time.sleep(20.0 * fail)
            continue
        fail = 0
        keep = idx > n_have
        idx, gam = idx[keep], gam[keep]
        if len(idx) == 0:
            raise RuntimeError("no new rows at t=%s" % t_last)
        if idx[0] != n_have + 1 or not np.all(np.diff(idx) == 1):
            raise RuntimeError("index discontinuity at n=%d" % n_have)
        parts.append(gam)
        n_have += len(gam)
        t_last = rows[-1].decode() if isinstance(rows[-1], bytes) \
            else rows[-1]
        req_log.append(dict(url=url, rows=int(len(gam)),
                            sha256=hashlib.sha256(body).hexdigest()))
        if n_have - n_ck >= 1_000_000:
            parts = [np.concatenate(parts)]
            np.save(ckpt, parts[0])
            n_ck = n_have
            print("  ... %d / %d ordinates (checkpoint)  [%.0f s]"
                  % (n_have, N_BIG, time.time() - t0), flush=True)
        time.sleep(LMFDB_PACE_S)
    gam_all = np.concatenate(parts)[:N_BIG]
    assert np.all(np.diff(gam_all) > 0.0)
    np.save(OUT_NPY, gam_all)
    meta = dict(
        n_zeros=int(N_BIG),
        gamma_1=float(gam_all[0]), gamma_N=float(gam_all[-1]),
        segments=[
            dict(source="odlyzko_zeros6", url=ODLYZKO_URL,
                 sha256_gz=gz_sha, n_lo=1, n_hi=ODLYZKO_N,
                 err_abs=ODLYZKO_ERR),
            dict(source="lmfdb_platt", url_template=LMFDB_URL,
                 n_lo=ODLYZKO_N + 1, n_hi=int(N_BIG),
                 err_rel_ulp=LMFDB_ERR_ULP,
                 n_requests=len(req_log)),
        ],
        pedigree=("Odlyzko zeta_tables zeros6 (4e-9); LMFDB / Platt "
                  "verified zeros; all below T0 = 3e12 hence on the "
                  "critical line unconditionally (Platt-Trudgian "
                  "2021)"),
        lmfdb_requests=req_log,
        built_s=round(time.time() - t0, 1))
    with open(OUT_META, "w") as fh:
        json.dump(meta, fh)
    if os.path.exists(ckpt):
        os.remove(ckpt)
    print("wrote %s (%d ordinates, gamma_N = %.6f)  [%.0f s]"
          % (OUT_NPY, N_BIG, gam_all[-1], time.time() - t0))


# ------------------------------------------------------------ certify
def mode_certify():
    import subgamma_fourier_bound_probe as subg
    t0 = time.time()
    gam = np.load(OUT_NPY)
    meta = json.load(open(OUT_META))
    n = len(gam)
    rep = {}
    ok_all = True

    def rec(name, ok, detail):
        nonlocal ok_all
        ok_all = ok_all and bool(ok)
        rep[name] = dict(ok=bool(ok), detail=detail)
        print("  [%s] %s -- %s" % ("PASS" if ok else "FAIL", name,
                                   detail), flush=True)

    d1 = abs(float(gam[0]) - GAMMA1)
    rec("B1 census+monotone+gamma_1",
        n == meta["n_zeros"] and bool(np.all(np.diff(gam) > 0.0))
        and d1 <= 5.0e-9,
        "n = %d, gamma_1 dev %.1e" % (n, d1))

    kk = np.arange(1, n + 1, dtype=float)
    up_r = subg.n_up(gam + CORR_EPS)
    lo_r = subg.n_lo(gam + CORR_EPS)
    up_l = subg.n_up(np.maximum(gam - CORR_EPS, 2.0))
    lo_l = subg.n_lo(np.maximum(gam - CORR_EPS, 2.0))
    n_ok = int(np.sum((kk <= up_r) & (kk >= lo_r)
                      & (kk - 1.0 <= up_l) & (kk - 1.0 >= lo_l)))
    rec("B2 Rosser corridor per index (both sides, unconditional)",
        n_ok == n, "%d/%d" % (n_ok, n))

    s_dev = theta_asym(gam) / math.pi + 1.0 - kk
    worst_s = float(np.max(np.abs(s_dev)))
    rec("B3 Backlund count consistency |theta/pi + 1 - k|",
        worst_s <= S_ABS_BAR,
        "worst %.4f (bar %.1f, empirical |S| ceiling)"
        % (worst_s, S_ABS_BAR))

    old = np.load(OLD_NPY)
    dev_old = float(np.max(np.abs(gam[:len(old)] - old)))
    rec("B4 overlap vs CLXXXIX mpmath 7000-cache",
        dev_old <= ODLYZKO_ERR + 1.0e-9, "worst %.2e" % dev_old)
    seam = float(gam[ODLYZKO_N] - gam[ODLYZKO_N - 1])
    mean_gap = 2.0 * math.pi / math.log(float(gam[ODLYZKO_N])
                                        / (2.0 * math.pi))
    rec("B4b seam spacing Odlyzko|LMFDB",
        0.0 < seam < 10.0 * mean_gap,
        "gap %.4f (local mean %.4f)" % (seam, mean_gap))

    from mpmath import mp as _mp, mpc as _mpc, zeta as _zf
    _mp.dps = 20
    idx = np.unique(np.geomspace(1, n, NS_ZETA).astype(int)) - 1
    worst_z = 0.0
    for i in idx:
        worst_z = max(worst_z,
                      float(abs(_zf(_mpc(0.5, float(gam[i]))))))
    rec("B5 independent mpmath |zeta(1/2+i gamma)| spots (dps 20)",
        worst_z <= ZETA_TOL,
        "%d spots, worst %.2e (bar %.0e)" % (len(idx), worst_z,
                                             ZETA_TOL))

    gaps = np.diff(gam)
    gmin, gmax = float(gaps.min()), float(gaps.max())
    # local-mean-relative: gap_k <= 5 x 2 pi / log(gamma_k / 2 pi)
    rel = gaps * np.log(gam[:-1] / (2.0 * math.pi)) \
        / (2.0 * math.pi)
    relmax = float(rel.max())
    rec("B6 spacing sanity (relative to local mean gap)",
        gmin > 1.0e-4 and relmax < 5.0,
        "min gap %.2e, max gap %.3f, max gap/local-mean %.3f"
        % (gmin, gmax, relmax))
    inv2 = float(np.sum(1.0 / gam ** 2))
    print("  anatomy: Sum 1/gamma^2 over cache = %.8f "
          "(first 7000: %.8f); T_c = %.4f" %
          (inv2, float(np.sum(1.0 / old ** 2)), float(gam[-1])))

    meta["certification"] = dict(report=rep, all_pass=bool(ok_all),
                                 worst_backlund=worst_s,
                                 worst_zeta_spot=worst_z,
                                 overlap_dev_7000=dev_old,
                                 inv2=inv2,
                                 certified_s=round(time.time() - t0,
                                                   1))
    with open(OUT_META, "w") as fh:
        json.dump(meta, fh)
    print("[CERTIFY %s  %.1f s]" % ("ALL PASS" if ok_all
                                    else "FAILURES", time.time() - t0))
    return 0 if ok_all else 1


if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else ""
    if mode == "plan":
        mode_plan()
    elif mode == "fetch":
        mode_fetch()
    elif mode == "certify":
        raise SystemExit(mode_certify())
    else:
        print("usage: w2_big_zero_cache_build.py plan|fetch|certify")
        raise SystemExit(2)
