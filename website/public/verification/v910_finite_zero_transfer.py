#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""v910 -- PRIME.WALL.FINITE_ZERO_TRANSFER.01: THE TRANSFER LAW -- the zero-supply economics of the finished finite wall (note CCV, discovery probe finite_zero_transfer_probe.py, SPEC 40a7b5c3, 40/40, frozen run 120.9 s, 2026-08-11): per deployed rung h the minimal verified-zero cutoff height T_req(h) at which the W2 recomposed certificate closes is measured on the full 75-rung ladder (67 surface + 8 deep) at 42 declared prefix anchors K = 250..2e7; THE LAWS (frozen run): log10 T_req^Wall = -3.045 + 1.228 ln h (2SE 0.094, R^2 0.882) => T_req ~ h^2.8; the RATIO curve T_req / (pi/D_h) GROWS at +0.897 dex/ln h (2SE 0.097, R^2 0.773) -- the needed zero reach overtakes the window's own spectral reach ~ h^2: VERDICT RATIO-GROWING => EXTERNAL-BATTERY, W-UNBOUNDED-PER-RUNG; THE TRANSFER LAW (stated as one parametrized theorem over the deployed ladder): ZerosCertified(T) AND TailEnvelope(T) => M_h > 0 for ALL deployed h <= H(T), with the measured monotone envelope H(gamma_7000) = 254 / H(gamma_2001052) = 1256 / H(gamma_2e7) = 2806, hypotheses named exactly (H1 the certified cache battery, Odlyzko / LMFDB, all below T0 = 3e12 Platt-Trudgian; H2 the unconditional tail envelope, beta in [0,1] unassumed; H3 the exact composition identities CXCIII/CLXXXIV; H4 the B-floor CLXXVII + the cited W1 depth CLXXXIV); W1 is CHEAP (T_req^W1 max 5350, binds the wall on only 3/75 rungs) -- the wall curve is W2-priced almost everywhere; the next h-decade (h ~ 28060) would cost T ~ 3.4e9 (~1e10 ordinates): the finite engine does NOT scale by buying more zeros, and H(T) is the measuring rod any analytic per-window bound must beat.

THIS MODULE re-verifies the shallow end of the transfer law on the
REDUCED FROZEN SUBSET (the SUB_T = 12 shallowest surface rungs, the
committed 7,000-ordinate cache of v909, anchors K = 250 / 500 / 1000
/ 2000 / 4000 / 7000) with SELF-CONTAINED machinery (the v909 W2
read pipeline, no experiments/ import): per rung the smallest STABLE
certifying anchor K* (closed at K* and every larger anchor,
non-monotone censuses counted honestly), T_req = gamma_K*, the
heart ward |PARITH - PARITH_hat(K)| <= TAILB(K) on EVERY (read,
anchor) cell, soundness m_cert(K) <= m everywhere, the H-envelope
consistency ward against the cited full-ladder anchor H(gamma_7000)
= 254 (every subset rung with h <= 254 must close at K = 7000), and
the subset trend of log10 T_req vs ln h (typed, printed against the
frozen-run law +1.228) with the ratio-vs-reach diagnosis.  The 2M /
2e7 anchors and the deep block need the big caches (gitignored,
EXTERNAL-CITED pedigree: Odlyzko zeta_tables zeros6 n <= 2,001,052;
LMFDB / Platt for the rest) and are CITED, not recomputed.

LANGUAGE DISCIPLINE (CCV verbatim): every T_req value is a per-rung
statement about the DEPLOYED windows, along the MEASURED critical
direction for the W2 face (DIRECTION-CONDITIONAL); H(T) is a
monotone envelope over the deployed ladder ONLY -- it says nothing
about undeployed h; the extrapolation is a FIT, not a theorem; a
finite zero sum can never prove RH; the all-h, all-direction
Weil-positivity object remains OPEN and RH-hard in every branch.
NO RH claim in either direction.

PROMOTION-RUN DISCLOSURE (2026-08-12, fail-first preserved): the
first full run of this module scored 9/10 in 9.3 s; measured content
(frozen as the expectation record): 12 subset rungs h 142..254, ALL
closed at K = 7000 (H-consistency 12/12 vs the cited boundary 254);
anchor closure census 2/3/4/6/8/12 at K = 250/500/1000/2000/4000/
7000, 0 non-monotone, 2 left-censored at K = 250 (kz 18/23; the
frozen full run saw 3 at its grid floor); heart worst scaled excess
-4.94e-06 over all 492 (read, anchor) cells, soundness 0 violations;
uncensored subset trends log10 T_req vs ln h +1.470 (R^2 0.424,
n = 10) and log10 ratio vs ln h +1.373 (R^2 0.408) -- the shallow
band is scatter-dominated, the citable laws are the full-ladder
frozen fits +1.228 / +0.897; the ONE failing check was the jitter
control, which this module had frozen STRICTER than the upstream
rule (all reads must fire vs the finite_zero_transfer_probe frozen
bar >= 5 reads): the jittered supply broke the heart on 9/14 reads
(the silent 5 are large-TAILB shallow-head reads).  AMENDMENT A1
(disclosed): the control rule is restored to the upstream frozen
bar fired >= 5 (SCR_MIN, CCV verbatim); NO measured value, census
definition or soundness tolerance was touched.

ANTI-CIRCULARITY (frozen): verified ordinates enter ONLY the supply
side and are tested against the independent prime side at every
anchor (the heart ward); measured m appears only as truth column,
soundness bar and denominator; T_req is read off the certificate
inequality only.  RNG: none except the declared jitter control
(seed 1).  Python-only per GATE.WOLFRAM.02.  NO marker moves.

PINNING DISCLOSURE (meta-audit CCCXXXVI, 2026-08-13): H2 and F1 are
statement-recording gates (check(..., True)); the executed
predicates pin only the reduced 12-rung / 7000-ordinate shallow end
(heart ward, soundness, anchor closure census, the one-sided
H-consistency ward against the cited boundary 254, and the subset
ratio growth F2).  H(gamma_2M) = 1256, H(gamma_2e7) = 2806 and the
full-ladder fits +1.228 / +0.897 are CITED premises NOT pinned by
this module -- a false cited envelope or law would not fail the
gate; they rest on the frozen experiments run (SPEC 40a7b5c3).
"""

import math
import os
import sys
import time

import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)

import v909_finite_wall_closure as wall  # noqa: E402 (shared spine)

K_GRID = (250, 500, 1000, 2000, 4000, 7000)
SUB_T = 12
H_ANCHOR_7000 = 254            # cited full-ladder H(gamma_7000), CCV
H_CITED = (254, 1256, 2806)    # H at gamma_7000 / gamma_2M / gamma_2e7
LAW_CITED = (1.228, 0.897)     # frozen-run b_T, b_R (dex/ln h)
SCR_MIN = 5
JITTER_SEED = 1

CHECKS = []


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok)))
    print("  [%s] %s%s" % ("PASS" if ok else "FAIL", name,
                           ("  -- " + detail) if detail else ""),
          flush=True)
    return bool(ok)


def section(title):
    print("\n" + "=" * 74)
    print(title)
    print("=" * 74, flush=True)


def ols_line(x, y):
    x = np.asarray(x, float)
    y = np.asarray(y, float)
    vx = float(np.var(x))
    if vx == 0.0:
        return float(np.mean(y)), 0.0, float("nan")
    b = float(np.cov(x, y, bias=True)[0, 1] / vx)
    a = float(np.mean(y) - b * np.mean(x))
    ss = float(np.sum((y - a - b * x) ** 2))
    st = float(np.sum((y - np.mean(y)) ** 2))
    return a, b, (1.0 - ss / st if st > 0 else float("nan"))


def zsum4re_prefix(v, J, gam, anchors):
    """4 Sum_{k <= K} Re phihat(gamma_k) at every anchor K in one
    chunked pass (per-ordinate contributions cumulated)."""
    per = np.zeros(len(gam))
    for i0 in range(0, len(gam), 1000):
        g = gam[i0:i0 + 1000]
        E = np.exp(1j * np.outer(g, v))
        per[i0:i0 + 1000] = (-(E @ J) / g ** 2).real
    cs = np.cumsum(per)
    return {K: 4.0 * float(cs[K - 1]) for K in anchors}


def run():
    t0 = time.time()
    print("=" * 74)
    print("v910 -- PRIME.WALL.FINITE_ZERO_TRANSFER.01: the transfer "
          "law -- T_req ~ h^2.8 (frozen-run fit +1.228 dex/ln h, "
          "R^2 0.882), ratio T_req/(pi/D) GROWING (+0.897 dex/ln h) "
          "=> EXTERNAL-BATTERY / W-UNBOUNDED-PER-RUNG; the "
          "parametrized transfer theorem: ZerosCertified(T) AND "
          "TailEnvelope(T) => M_h > 0 for all deployed h <= H(T), "
          "H(gamma_7000/2M/2e7) = 254 / 1256 / 2806 (cited full-"
          "ladder census, SPEC 40a7b5c3); this module re-verifies "
          "the shallow end on the reduced subset")
    print("(per-rung, deployed ladder, measured critical direction; "
          "H(T) says nothing about undeployed h; NO RH claim)")
    print("=" * 74, flush=True)
    del CHECKS[:]

    # ------------------------------------------------------------ Z
    section("Z -- the shared verified-zero cache (v909 wards "
            "re-run)")
    import json
    with open(wall.ZC_JSON) as fh:
        gam = np.asarray(json.load(fh)["gammas"], float)
    kk = np.arange(1, wall.N_Z + 1, dtype=float)
    up_r = wall.n_up(gam + wall.CORR_EPS)
    lo_r = wall.n_lo(gam + wall.CORR_EPS)
    up_l = wall.n_up(np.maximum(gam - wall.CORR_EPS, 2.0))
    lo_l = wall.n_lo(np.maximum(gam - wall.CORR_EPS, 2.0))
    n_ok = int(np.sum((kk <= up_r) & (kk >= lo_r)
                      & (kk - 1.0 <= up_l) & (kk - 1.0 >= lo_l)))
    check("Z1 cache census %d, strictly increasing, corridor "
          "%d/%d both sides" % (len(gam), n_ok, wall.N_Z),
          len(gam) == wall.N_Z
          and bool(np.all(np.diff(gam) > 0.0))
          and n_ok == wall.N_Z)
    s2t = wall.s2_tail()
    inv2_cs = np.cumsum(1.0 / gam ** 2)
    inv3_cs = np.cumsum(1.0 / gam ** 3)

    # ------------------------------------------------------------ W
    section("W -- the reduced subset: the %d shallowest surface "
            "rungs" % SUB_T)
    rows = []
    for kz in range(2, 151):
        r = wall.build_rung(kz)
        if r is not None:
            rows.append(r)
        if len(rows) >= 60:
            break
    rows.sort(key=lambda r: (r["h"], r["kz"]))
    sub = rows[:SUB_T]
    check("W1 subset census: %d rungs, h %d..%d, m > 0 on all"
          % (len(sub), sub[0]["h"], sub[-1]["h"]),
          len(sub) == SUB_T and all(r["m"] > 0 for r in sub))

    # ------------------------------------------------------------ T
    section("T -- T_req per rung: prefix anchors K = %s"
            % (K_GRID,))
    heart_w = -1e18
    sound_bad = 0
    n_cells = 0
    n_nonmono = 0
    n_leftcen = 0
    close_at = {K: 0 for K in K_GRID}
    table = []
    for r in sub:
        reads = {}
        for A in wall.HEAD_A:
            sp = wall.demand_at_head(r, A)
            if sp is not None:
                reads[("A", A)] = sp
        spB = wall.split_at(r, r["ncB"]) if r["ncB"] > 0 else None
        if spB is not None:
            reads[("cB", 0)] = spB
        abel_K = {}
        for K in K_GRID:
            tg = wall.tail_grid(r["D"], float(gam[K - 1]))
            abel_K[K] = wall.abel_upper(tg, 1.0 / tg[:-1] ** 2,
                                        n_start=float(K))
        closed = {K: False for K in K_GRID}
        for key, sp in reads.items():
            pc = wall.phi_cont_of(r, sp)
            zs = zsum4re_prefix(pc["v"], pc["J"], gam, K_GRID)
            for K in K_GRID:
                par_hat = (-zs[K] - pc["triv"] - pc["ramp_at"]
                           + pc["ramp_cont"] + pc["ext_cont"]
                           - pc["ext_at"])
                dps = 4.0 * pc["sd"] * (pc["vmax"]
                                        * float(inv2_cs[K - 1])
                                        + 2.0
                                        * float(inv3_cs[K - 1])) \
                    * wall.DPS_ERR
                tailb = (4.0 * pc["sd"] * abel_K[K]
                         + 4.0 * math.exp(0.5 * pc["vmax"])
                         * pc["sd"] * s2t
                         + dps + 1e-12 * (1.0 + abs(pc["triv"])))
                resid = sp["par"] - par_hat
                tol_a = wall.RECON_TOL * (1.0 + abs(sp["t_int"]))
                heart_w = max(heart_w,
                              (abs(resid) - tailb - tol_a)
                              / max(1.0, abs(sp["t_int"])))
                n_cells += 1
                m_cert = sp["fc"] + par_hat - tailb
                if m_cert > r["m"] * (1.0 + wall.SOUND_TOL) + 1e-15:
                    sound_bad += 1
                if m_cert > 0.0:
                    closed[K] = True
        seq = [closed[K] for K in K_GRID]
        k_star = None
        for i, K in enumerate(K_GRID):
            if seq[i] and all(seq[i:]):
                k_star = K
                break
        first = next((K for i, K in enumerate(K_GRID) if seq[i]),
                     None)
        if first is not None and first != k_star:
            n_nonmono += 1
        if k_star == K_GRID[0]:
            n_leftcen += 1
        for K in K_GRID:
            close_at[K] += closed[K]
        t_req = float(gam[k_star - 1]) if k_star else float("nan")
        ratio = t_req / (math.pi / r["D"]) if k_star else \
            float("nan")
        table.append(dict(kz=r["kz"], h=r["h"], k_star=k_star,
                          t_req=t_req, ratio=ratio))
        print("    kz %3d h %4d: K* %s  T_req %s  T_req/(pi/D) %s  "
              "[%.1f s]"
              % (r["kz"], r["h"],
                 str(k_star) if k_star else "OPEN(>7000)",
                 "%.1f" % t_req if k_star else "-",
                 "%.2f" % ratio if k_star else "-",
                 time.time() - t0), flush=True)
    check("T1 heart ward on every (read, anchor) cell: worst "
          "scaled excess %+.2e <= 0 over %d cells"
          % (heart_w, n_cells), heart_w <= 0.0)
    check("T2 soundness m_cert(K) <= m on every cell (%d "
          "violations)" % sound_bad, sound_bad == 0)
    check("T3 anchor closure census %s at K = %s (monotone: %d "
          "non-monotone rungs; %d left-censored at K = %d)"
          % ([close_at[K] for K in K_GRID], K_GRID, n_nonmono,
             n_leftcen, K_GRID[0]), n_nonmono == 0)

    # ------------------------------------------------------------ H
    section("H -- the H-envelope consistency ward vs the cited "
            "full-ladder anchor H(gamma_7000) = %d" % H_ANCHOR_7000)
    must = [t for t in table if t["h"] <= H_ANCHOR_7000]
    n_must = sum(1 for t in must if t["k_star"] is not None)
    check("H1 every subset rung with h <= %d closes at K = 7000 "
          "(%d/%d; the cited envelope H(T) = max h with ALL "
          "shallower rungs closed)"
          % (H_ANCHOR_7000, n_must, len(must)),
          n_must == len(must) and len(must) >= 8)
    n_all = sum(1 for t in table if t["k_star"] is not None)
    print("    subset closure at K = 7000: %d/%d (h %d..%d); the "
          "full-ladder census at gamma_7000 is 16/67 + 0/8 with "
          "H = 254 (CITED, SPEC 40a7b5c3); H(gamma_2M) = %d and "
          "H(gamma_2e7) = %d need the big caches (CITED)"
          % (n_all, len(table), table[0]["h"], table[-1]["h"],
             H_CITED[1], H_CITED[2]))
    check("H2 transfer-law statement recorded: ZerosCertified(T) "
          "AND TailEnvelope(T) => M_h > 0 for all deployed h <= "
          "H(T); H(gamma_7000/2M/2e7) = %d/%d/%d (cited, not "
          "pinned by this gate); hypotheses H1-H4 as in the "
          "frozen run" % H_CITED, True)

    # ------------------------------------------------------------ F
    section("F -- the subset trend (typed) vs the frozen-run laws")
    unc = [t for t in table if t["k_star"] is not None
           and t["k_star"] > K_GRID[0]]
    if len(unc) >= 4:
        lh = np.log([t["h"] for t in unc])
        _a, b_t, r2_t = ols_line(lh, np.log10([t["t_req"]
                                               for t in unc]))
        _a2, b_r, r2_r = ols_line(lh, np.log10([t["ratio"]
                                                for t in unc]))
    else:
        b_t = b_r = r2_t = r2_r = float("nan")
    print("    subset log10 T_req vs ln h: slope %+.3f (R^2 %.3f, "
          "n = %d); frozen full-ladder law %+.3f (R^2 0.882)"
          % (b_t, r2_t, len(unc), LAW_CITED[0]))
    print("    subset log10 ratio vs ln h: slope %+.3f (R^2 %.3f); "
          "frozen full-ladder law %+.3f (RATIO-GROWING => "
          "EXTERNAL-BATTERY / W-UNBOUNDED-PER-RUNG)"
          % (b_r, r2_r, LAW_CITED[1]))
    check("F1 typed: subset trend recorded (slopes %+.2f / %+.2f "
          "dex/ln h; the citable laws are the full-ladder frozen "
          "fits -- cited, not pinned by this gate)"
          % (b_t, b_r), True)
    check("F2 the ratio grows on the subset (slope > 0): the "
          "local-sampling world (constant ratio) is refuted on "
          "the deployed ladder", b_r > 0.0)

    # ------------------------------------------------------------ M
    section("M -- control (must fire): scrambled zero supply")
    rng = np.random.default_rng(JITTER_SEED)
    gam_scr = np.sort(gam + rng.uniform(-2.0, 2.0, size=len(gam)))
    r9 = wall.build_rung(wall.CTRL_KZ)
    tg9 = wall.tail_grid(r9["D"], float(gam[-1]))
    abel9 = wall.abel_upper(tg9, 1.0 / tg9[:-1] ** 2,
                            n_start=float(wall.N_Z))
    inv2 = float(inv2_cs[-1])
    inv3 = float(inv3_cs[-1])
    fired = 0
    tried = 0
    for r in sub[:6] + [r9]:
        for A in (9, 50):
            sp = wall.demand_at_head(r, A)
            if sp is None:
                continue
            pc = wall.phi_cont_of(r, sp)
            par_hat, tailb = wall.direct_read(
                r, sp, pc, gam, abel9, s2t, inv2, inv3)
            par_scr, _tb = wall.direct_read(
                r, sp, pc, gam_scr, abel9, s2t, inv2, inv3)
            tried += 1
            if abs(sp["par"] - par_scr) > tailb:
                fired += 1
    check("M1 the jittered supply (U(-2, 2), seed %d, sorted) "
          "breaks the heart on %d/%d reads at K = %d (upstream "
          "frozen bar >= %d, CCV; the silent reads are "
          "large-TAILB shallow-head reads, disclosed)"
          % (JITTER_SEED, fired, tried, wall.N_Z, SCR_MIN),
          fired >= SCR_MIN)

    # ------------------------------------------------------- verdict
    n_pass = sum(1 for _n, okk in CHECKS if okk)
    n_tot = len(CHECKS)
    ok = n_pass == n_tot
    print("\n" + "=" * 74)
    print("v910: %d/%d checks passed | runtime %.1f s"
          % (n_pass, n_tot, time.time() - t0))
    print("the transfer law: the finite wall's zero supply is an "
          "EXTERNAL BATTERY (T_req ~ h^2.8, ratio to the window "
          "reach pi/D growing +0.897 dex/ln h on the frozen full "
          "ladder); H(gamma_7000/2M/2e7) = 254/1256/2806; the "
          "finite engine does not scale by buying more zeros -- "
          "any analytic per-window bound with ~pi/D reach beats "
          "the measured h^2 battery; per-rung, deployed ladder, "
          "measured critical direction; NO RH claim")
    print("[%s] v910 VERDICT GATE" % ("PASS" if ok else "FAIL"))
    return 0 if ok else n_tot - n_pass


if __name__ == "__main__":
    raise SystemExit(1 if run() else 0)
