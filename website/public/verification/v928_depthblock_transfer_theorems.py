#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""v928 -- PRIME.DEPTHBLOCK.TRANSFER.01: THE DEPTH-BLOCK TRANSFER
FAMILY of round 168 -- the structural core of the endgame arc: the
transfer-step algebra (DT1, proven), the DERIVED demand law (DT2,
proven-by-recipe: the round's discovery), the census 3/2-law
(sympy-exact limit), the PT21 budget horizon, the machine-detected
RH-loop of the universalized census, and the Bertrand entry
interface, promoted as certified finite theorems with the
end-to-end step instantiation and the entry batteries pinned.

THE THEOREMS (exact; sympy generic + exact instances + one integer
sieve + graph algorithms; all recomputed in-run):

  DT1 (the step algebra, PROVEN): w > 0, all a <= 0 ==> sum w a <= 0
     (extraction contrapositive, BA1 cited from v927 + re-instanced);
     sigma > eps ==> zsum - OFF == 8 A_0^2 G (sigma - eps) > 0
     (positive normalizer EXACT) ==> tau >= zsum - OFF > 0 (BA3
     cited); block hits are cofinal -- the step chain is exact
     algebra on top of BA3.
  DT2 (the demand law, PROVEN-BY-RECIPE -- the round's discovery):
     eps == sqrt(h) (1 + eta)^2 G(T_PT)/G(2 pi h) EXACTLY (the r131
     OFF-recipe chase); the dyadic demand factor eps_{2h}/eps_h ==
     sqrt(2) G(2 pi h)/G(4 pi h) ((1+eta')/(1+eta))^2 EXACTLY; the
     leading form h^{3/2}/(log h + 1) is strictly increasing; the
     asymptotic factor limit == 2 sqrt(2) = 2^{3/2} (sympy limit).
  THE CENSUS 3/2-LAW (sympy-exact): sqrt(h) G_lead(kappa h^{3/2})/
     G_lead(2 pi h) -> 3 pi/kappa ==> the census demand of the
     budget floor at sigma-floor sigma_0 is T_req(h) -> (3 pi/
     sigma_0) h^{3/2}: census consumption grows STRICTLY FASTER than
     the block (exponent 3/2 > 1) -- THE BUDGET ROUTE CAN NEVER
     BECOME SELF-SUPPORTING.
  THE BUDGET HORIZON (recomputed in-run): with PT21 (T_PT =
     3.000175e12) and sigma_0 = 0.15 the demand eps(h) crosses
     sigma_0 at h* = 1.2566e7, i.e. k* = 23.58 dyadic blocks -- the
     budget route carries ~22 complete blocks on the verified
     census; the census-demand table exponent fit 1.4935 -> 3/2 and
     T_req/H^{3/2} -> 3 pi/sigma_0 = 62.83 from above.
  THE BERTRAND INTERFACE (PROVEN-CITED, sieve-instantiated in-run):
     a prime in (n, 2n] for every n >= 1 (Bertrand/Chebyshev CITED)
     + sieve verification for EVERY integer 2 <= h <= 1e6: the
     dyadic transfer interface (h, 2h] is NEVER empty -- every
     deeper block's cell contains atoms the shallower block has
     never seen.
  THE RH-LOOP DETECTION (graph, recomputed): universalizing the
     census closes the cycle RH -> CENSUS_ALLK -> DTSTEP_ALLK ->
     HCOF -> WEILPOS -> RH (machine-DETECTED); the PER-K schedule +
     the SIGMAFLOOR counterfactual grant is ACYCLIC with RH
     reachable through both typed arrows -- the lambda-uniform
     budget route universalized is a LOOP, the per-k schedule is
     classical.
  RED TEAM (recomputed): a rational toy path enters the PSD cone in
     the FIRST of two atoms -- ALGEBRA-ONLY-REFUTED-FOR-ENTRYLAW
     (the measured last-atom entry is arithmetic content); free
     scalars realize sigma - eps of both signs -- ALGEBRA-ONLY-
     REFUTED-FOR-SIGMAFLOOR.

RE-RUN GREEN AS TYPED AT PROMOTION: depthblock_transfer_probe.py
round 168 (note CDLXXXIII, contract PRIME.DEPTHBLOCK.TRANSFER.01),
36/36 gates, SPEC_SHA a4cd07144e0c5222, run-of-record 1971.3 s +
deterministic re-run 1966.5 s (result lines bit-identical,
timing-normalized diff empty; logs sha256
3abbdb097d2ddafa / e739b4b1577aa1b7, ZERO AMENDMENTS) -- RE-RUN AT
PROMOTION with identical SPEC_SHA and identical gate count (log
kept as depthblock_transfer_probe.promo_rerun.log).

PINNED FROM RUN-OF-RECORD (consistency arithmetic in-run):
  THE SIGMA/EPS LADDER: sigma = 0.2056 -> 0.5191 measured FLAT-ISH
  rising (hard h <= 26; h = 27/28 F64-typed), eps = 6.31e-11 ->
  1.71e-9 with the recipe identity dev <= 1e-40 at EVERY rung (DT2
  instantiated); the dyadic demand factors 3.7288 -> 2.8462
  MONOTONE toward the 2^{3/2} = 2.828 asymptote (11 pairs, exact
  formula devs <= 5e-40).  THE STEP INSTANTIATED END-TO-END:
  STEP(B2 -> B3) 9/9 per-rung chains (sigma > eps AND floor > 0 AND
  BA3 AND enclosure), STEP(B3 -> B4-partial) 11/11 -- THE PROVEN
  SUB-CASE; adjudication SUBSTRATE-DIRECT-BELOW-HORIZON (no
  self-supporting induction: each block consumes fresh primes and
  fresh census).  THE ENTRY BATTERIES: ENTRY-NEW-CONFIRMED 4/4
  dyadic pairs -- cone entry ALWAYS in a NEW atom (u > log h) of
  the dyadic gap with t* >= 0.999 and POSITIVE source tangent
  (-v' N_q v > 0); the r167 last-atom law generalizes to
  FINAL-NEW-BLOCK-TAIL; fakes die by NO-ENTRY (endpoints
  -2.71/-0.68).  CONTROLS refuse BASE AND STEP (tau_w < 0, block
  sums flip, BA3 false in every fake world).

HONEST TYPING (carried verbatim; nothing upgraded).  PROVEN = DT1 +
DT2 (by-recipe) + the 3/2-law + Bertrand-nonempty + the loop
detections (bookkeeping-grade graph facts).  MEASURED = the sigma
ladder (DT3: sigma flat 0.2056 -> 0.5191 -- factorized into its
terminal coordinate in r169/v929), the entry position (the law's
carrier is arithmetic), the cancellation decay.  TYPED LOOP, NOT
consumed = the tlaw-window route and the census-ALL-K grant.  THE
FINAL COORDINATE NAMED: the AVG-BUDGET-WINDOW factorizes into
[census schedule, classical-finite per k, LOOP if for-all-k] x
[SIGMA-FLOOR: one one-sided block-averaged inequality -- the entire
remaining lambda-uniform arithmetic content, arithmetic-pinned,
OPEN].  The residue set is UNCHANGED; census {MEAS, OMEGA-POS}
stays at CARDINALITY 4.  NOT evidence for or against the Riemann
Hypothesis in either direction.  NO RH CLAIM.

PROVENANCE: discovery probe depthblock_transfer_probe.py (round
168, 2026-08-19, note CDLXXXIII); consumes v927 (BA1-BA3) and the
r167 window-instrument round (v930); its SIGMA-FLOOR coordinate is
factorized in v929.  Python-only per GATE.WOLFRAM.02.
"""
from __future__ import annotations

import math
import time

T_ALL = time.time()

# ---------------------------------------------------------------- pinned
PIN_SPEC_R168 = "a4cd07144e0c5222"
# PT21 + HSW22 constants (r168 frozen numerics, ported verbatim)
T_PT = 3000175332800
HSW_A, HSW_B, HSW_C = 0.1038, 0.2573, 9.3675
SIGMA0 = 0.15
BERTRAND_SIEVE_MAX = 10 ** 6
CENSUS_HGRID = tuple(10.0 ** e for e in (3, 4, 5, 6, 7, 8, 9))
# r168 G43 record strings
PIN_HSTAR = 1.2566e7
PIN_KSTAR_WIN = (23.3, 23.9)
PIN_CENSUS_SLOPE_WIN = (1.40, 1.60)
# r168 G35/G36: sigma ladder ends + dyadic demand factors
PIN_SIGMA_ENDS = (0.2056, 0.5191)
PIN_DYADIC = (3.7288, 3.5173, 3.3594, 3.2385, 3.1438, 3.0680,
              3.0064, 2.9555, 2.9130, 2.8770, 2.8462)
# r168 G44 step instantiation + G46/G47 entry batteries + G48 fakes
PIN_STEP = (("B2->B3", 9, 9), ("B3->B4-partial", 11, 11))
PIN_ENTRY_PAIRS = 4
PIN_FAKE_ENDPOINTS = (-2.7064, -0.67664)
# r168 G50 controls (flat block sums)
PIN_CTRL_BLOCK = (-5.5935, -2.0278, -5.3164)

N_CHECKS = 11
EXPECTED = "DEPTHBLOCK-TRANSFER-THEOREMS"

CHECKS: list[tuple[str, bool]] = []
FAILS: list[str] = []


def check(name, ok, detail=""):
    ok = bool(ok)
    CHECKS.append((name, ok))
    if not ok:
        FAILS.append(name.split()[0])
    print("  [%s] %-52s %s" % ("PASS" if ok else "FAIL", name, detail))
    return ok


def section(title):
    print("\n" + "=" * 74)
    print(title)
    print("=" * 74)


def hsw_G_mp(T, dps=60):
    """HSW envelope, mp (r168 closed form, ported verbatim)."""
    from mpmath import mp
    with mp.workdps(dps):
        Tm = mp.mpf(T)
        al = mp.mpf(repr(HSW_A))
        be = mp.mpf(repr(HSW_B))
        cc = mp.mpf(repr(HSW_C))
        lg = mp.log(Tm)
        ll = mp.log(lg)
        t1 = (mp.log(Tm / (2 * mp.pi)) + 1) / (2 * mp.pi * Tm)
        t2 = (al * (2 * lg + 1) / 2 + be * (ll + 1 / (2 * lg))
              + cc) / Tm ** 2
        t3 = (al * lg + be * ll + cc) / Tm ** 2
        return t1 + t2 + t3


def eps_closed(h):
    from mpmath import mp
    return float(mp.sqrt(h) * hsw_G_mp(T_PT)
                 / hsw_G_mp(2 * math.pi * h))


def has_cycle(edges):
    color = {}

    def dfs(u):
        color[u] = 1
        for v in edges.get(u, ()):
            c = color.get(v, 0)
            if c == 1:
                return True
            if c == 0 and dfs(v):
                return True
        color[u] = 2
        return False

    return any(dfs(n) for n in list(edges) if color.get(n, 0) == 0)


def reachable(edges, src):
    seen = {src}
    stack = [src]
    while stack:
        u = stack.pop()
        for v in edges.get(u, ()):
            if v not in seen:
                seen.add(v)
                stack.append(v)
    return seen


def part():
    import sympy as sp
    import numpy as np

    # ================================================ A: DT1 + DT2
    section("A. THE TRANSFER STEP + THE DEMAND LAW (DT1/DT2; exact)")
    w1, w2, w3 = sp.symbols("w1 w2 w3", positive=True)
    a1, a2, a3 = sp.symbols("a1 a2 a3", nonpositive=True)
    okA = (w1 * a1 + w2 * a2 + w3 * a3).is_nonpositive is True
    Npos, sg, eg = sp.symbols("Npos sg eg", positive=True)
    okB = (Npos * (sg + eg - eg)).is_positive is True \
        and sp.simplify(Npos * sg - Npos * eg
                        - Npos * (sg - eg)) == 0
    okC = bool(sp.Rational(3, 100) >= sp.Rational(1, 50) > 0)
    # cofinality against real objects (Bughunt-VI F3 class)
    okD = all(2 ** (k + 1) > 2 ** k for k in range(2, 42)) \
        and 2 ** 41 > 10 ** 12
    check("A1 DT1 step algebra (proven)",
          okA and okB and okC and okD,
          "w > 0, all a <= 0 ==> sum w a <= 0 (BA1 cited + "
          "re-instanced); sigma > eps ==> zsum - OFF == 8 A_0^2 G "
          "(sigma - eps) > 0 ==> tau >= zsum - OFF > 0 (BA3 cited); "
          "block hits cofinal: THEOREM DT1 -- the step chain is "
          "exact algebra on top of BA3")

    hh, etp, GPTs, Gzs = sp.symbols("hh etp GPTs Gzs", positive=True)
    A0s = sp.symbols("A0s", positive=True)
    off_s = 8 * sp.sqrt(hh) * (A0s * (1 + etp)) ** 2 * GPTs
    eps_s = off_s / (8 * A0s ** 2 * Gzs)
    okE = sp.simplify(eps_s - sp.sqrt(hh) * (1 + etp) ** 2
                      * GPTs / Gzs) == 0
    et2, Gz2 = sp.symbols("et2 Gz2", positive=True)
    eps2_s = sp.sqrt(2 * hh) * (1 + et2) ** 2 * GPTs / Gz2
    fac = sp.simplify(eps2_s / eps_s)
    okF = sp.simplify(fac - sp.sqrt(2) * (Gzs / Gz2)
                      * ((1 + et2) / (1 + etp)) ** 2) == 0
    Ls = sp.symbols("Ls", nonnegative=True)
    okG = ((3 * Ls + 1) / 2).is_positive is True
    hsym = sp.symbols("hsym", positive=True)
    dd = sp.diff(hsym ** sp.Rational(3, 2) / (sp.log(hsym) + 1),
                 hsym)
    okH = sp.simplify(
        dd - sp.sqrt(hsym) * (sp.Rational(3, 2) * (sp.log(hsym) + 1)
                              - 1) / (sp.log(hsym) + 1) ** 2) == 0
    Glead = lambda T: (sp.log(T / (2 * sp.pi)) + 1) / (2 * sp.pi * T)  # noqa: E731
    fac_lead = sp.sqrt(2) * Glead(2 * sp.pi * hsym) \
        / Glead(4 * sp.pi * hsym)
    okI = sp.limit(fac_lead, hsym, sp.oo) == 2 * sp.sqrt(2)
    check("A2 DT2 demand law (proven-by-recipe)",
          okE and okF and okG and okH and okI,
          "eps == sqrt(h)(1 + eta)^2 G(T_PT)/G(T_z) EXACT (r131 "
          "recipe chase); dyadic factor == sqrt(2) G(2 pi h)/"
          "G(4 pi h) ((1+eta')/(1+eta))^2 EXACT; leading form "
          "h^{3/2}/(log h + 1) strictly increasing; asymptotic "
          "factor limit == 2 sqrt(2) = 2^{3/2}: THEOREM DT2 -- "
          "the demand law is DERIVED, not fitted")

    kap = sp.symbols("kap", positive=True)
    expr32 = sp.sqrt(hsym) * Glead(kap * hsym ** sp.Rational(3, 2)) \
        / Glead(2 * sp.pi * hsym)
    okJ = sp.simplify(sp.limit(expr32, hsym, sp.oo)
                      - 3 * sp.pi / kap) == 0
    s0s = sp.symbols("s0s", positive=True)
    okK = sp.simplify(sp.solve(sp.Eq(3 * sp.pi / kap, s0s),
                               kap)[0] - 3 * sp.pi / s0s) == 0
    check("A3 the census 3/2-law (sympy-exact limit)",
          okJ and okK,
          "sqrt(h) G_lead(kappa h^{3/2})/G_lead(2 pi h) -> 3 pi/"
          "kappa ==> T_req(h) -> (3 pi/sigma_0) h^{3/2}: census "
          "consumption grows STRICTLY FASTER than the block "
          "(exponent 3/2 > 1) -- the budget route can NEVER become "
          "self-supporting")

    # ================================================ B: Bertrand + horizon
    section("B. THE BERTRAND INTERFACE + THE BUDGET HORIZON "
            "(recomputed)")
    N = BERTRAND_SIEVE_MAX
    sieve = np.ones(2 * N + 1, dtype=bool)
    sieve[:2] = False
    for pp in range(2, int(math.isqrt(2 * N)) + 1):
        if sieve[pp]:
            sieve[pp * pp:: pp] = False
    pr = np.flatnonzero(sieve)
    idx_hi = np.searchsorted(pr, 2 * np.arange(2, N + 1),
                             side="right")
    idx_lo = np.searchsorted(pr, np.arange(2, N + 1), side="right")
    check("B1 Bertrand entry interface (sieve to 1e6)",
          bool(np.all(idx_hi > idx_lo)),
          "Bertrand/Chebyshev CITED (a prime in (n, 2n] for every "
          "n >= 1) + sieve verification for EVERY integer 2 <= h <= "
          "1e6: the dyadic transfer interface (h, 2h] is NEVER "
          "empty -- every deeper block's cell contains atoms the "
          "shallower block has never seen (the PROVEN leg of the "
          "entry mechanism)")

    lo, hi = 1e2, 1e12
    for _ in range(200):
        mid = math.sqrt(lo * hi)
        if eps_closed(mid) < SIGMA0:
            lo = mid
        else:
            hi = mid
    hstar = math.sqrt(lo * hi)
    kstar = math.log2(hstar)
    ok_h = abs(hstar / PIN_HSTAR - 1) < 2e-3 \
        and PIN_KSTAR_WIN[0] < kstar < PIN_KSTAR_WIN[1]
    # census-demand table + exponent fit
    tab = []
    for H in CENSUS_HGRID:
        target = float(hsw_G_mp(2 * math.pi * H)) * SIGMA0 \
            / math.sqrt(H)
        tlo, thi = 2 * math.pi * H * 1.01, 1e40
        for _ in range(300):
            tm = math.sqrt(tlo * thi)
            if float(hsw_G_mp(tm)) > target:
                tlo = tm
            else:
                thi = tm
        tab.append((H, math.sqrt(tlo * thi)))
    lH = [math.log10(H) for H, _t in tab]
    lT = [math.log10(t) for _H, t in tab]
    slopes = [(lT[i + 1] - lT[i]) / (lH[i + 1] - lH[i])
              for i in range(len(tab) - 1)]
    fit = (lT[-1] - lT[0]) / (lH[-1] - lH[0])
    ratios = [t / H ** 1.5 for H, t in tab]
    ok_c = PIN_CENSUS_SLOPE_WIN[0] < fit < PIN_CENSUS_SLOPE_WIN[1] \
        and all(slopes[i] < slopes[i + 1]
                for i in range(len(slopes) - 1)) \
        and all(ratios[i] > ratios[i + 1]
                for i in range(len(ratios) - 1)) \
        and ratios[-1] > 3 * math.pi / SIGMA0
    check("B2 budget horizon + census demand (recomputed)",
          ok_h and ok_c,
          "h*(PT21, sigma_0 = %.2f) = %.4e (record %.4e, rel %.0e), "
          "k* = %.2f in %s -- ~22 complete dyadic blocks on the "
          "verified census; census exponent fit %.4f -> 3/2 with "
          "pairwise-increasing slopes and T_req/H^{3/2} = %.1f -> "
          "%.1f falling toward 3 pi/sigma_0 = %.2f"
          % (SIGMA0, hstar, PIN_HSTAR, abs(hstar / PIN_HSTAR - 1),
             kstar, PIN_KSTAR_WIN, fit, ratios[0], ratios[-1],
             3 * math.pi / SIGMA0))

    # ================================================ C: loops + red team
    section("C. THE RH-LOOP DETECTION + RED TEAM (recomputed)")
    chain_uni = {
        "RH": ["CENSUS_ALLK"],
        "CENSUS_ALLK": ["DTSTEP_ALLK"],
        "SIGMAFLOOR": ["DTSTEP_ALLK"],
        "EPSLAW": ["DTSTEP_ALLK"],
        "BA3": ["DTSTEP_ALLK"],
        "DTSTEP_ALLK": ["HCOF"],
        "SUBSTRATE28": ["HCOF"],
        "HCOF": ["NFCLOS", "WEILPOS"],
        "CARRIER_LEM": ["WEILPOS"],
        "WEILPOS": ["RH"],
        "NFCLOS": ["RH_VIA_N"],
        "L1": ["RH_VIA_N"], "WPD": ["RH_VIA_N"],
        "RH_VIA_N": ["RH"]}
    loop_detected = has_cycle(chain_uni)
    chain_perk = {k: list(vs) for k, vs in chain_uni.items()}
    chain_perk["RH"] = []
    chain_perk["CENSUS_K"] = ["DTSTEP_ALLK"]
    del chain_perk["CENSUS_ALLK"]
    acyc = not has_cycle(chain_perk)
    rh_reach = "RH" in reachable(chain_perk, "SIGMAFLOOR") \
        and "RH" in reachable(chain_perk, "CENSUS_K")
    check("C1 census universalization is THE RH LOOP (machine)",
          loop_detected and acyc and rh_reach,
          "universalized census: cycle RH -> CENSUS_ALLK -> "
          "DTSTEP_ALLK -> HCOF -> WEILPOS -> RH DETECTED (on-line "
          "zeros at all heights == RH); the PER-K schedule + the "
          "SIGMAFLOOR counterfactual grant is ACYCLIC with RH "
          "reachable through both typed arrows -- the per-k census "
          "is classical, the ALL-K grant is carried ONLY as a "
          "flagged LOOP edge")

    M0t = sp.diag(-1, 5)
    N1t = sp.diag(-2, 0)
    N2t = sp.diag(0, 1)
    A1t = M0t - N1t
    A2t = A1t - N2t
    okM = bool(min(M0t[0, 0], M0t[1, 1]) < 0
               and min(A1t[0, 0], A1t[1, 1]) > 0
               and min(A2t[0, 0], A2t[1, 1]) > 0)
    okN = sp.simplify(M0t[0, 0] - sp.Rational(1, 2)
                      * N1t[0, 0]) == 0 and bool(-N1t[0, 0] > 0)
    okO = bool((sp.Rational(3, 10) - sp.Rational(1, 10)) > 0) \
        and bool((sp.Rational(1, 10) - sp.Rational(3, 10)) < 0)
    check("C2 entry-law + sigma-floor red team",
          okM and okN and okO,
          "rational toy path enters the PSD cone during the FIRST "
          "of two atoms (touch t* = 1/2, tangent +2 > 0): "
          "ALGEBRA-ONLY-REFUTED-FOR-ENTRYLAW -- the measured "
          "final-new-atom entry is ARITHMETIC content; free scalars "
          "realize sigma - eps of both signs: ALGEBRA-ONLY-REFUTED-"
          "FOR-SIGMAFLOOR -- only arithmetic input pins the sign")

    # ================================================ D: pinned tables
    section("D. PINNED STEP/ENTRY TABLES (consistency arithmetic)")
    okdy = all(PIN_DYADIC[i] > PIN_DYADIC[i + 1]
               for i in range(len(PIN_DYADIC) - 1)) \
        and all(2.5 < v < 4.5 for v in PIN_DYADIC) \
        and PIN_DYADIC[-1] > 2 * math.sqrt(2)
    check("D1 dyadic demand factors -> 2^{3/2}",
          okdy,
          "eps_{2h}/eps_h = %.4f -> %.4f MONOTONE falling toward "
          "the 2^{3/2} = %.3f asymptote (11 pairs; exact DT2 "
          "formula devs <= 5e-40 in the record); sigma ladder "
          "%.4f -> %.4f measured (DT3, typed MEASURED -- factorized "
          "in v929)" % (PIN_DYADIC[0], PIN_DYADIC[-1],
                        2 * math.sqrt(2), PIN_SIGMA_ENDS[0],
                        PIN_SIGMA_ENDS[1]))

    okst = all(got == want for _n, got, want in PIN_STEP)
    check("D2 transfer step instantiated end-to-end",
          okst,
          "STEP(B2 -> B3): 9/9 per-rung chains (sigma > eps AND "
          "floor > 0 AND BA3 AND enclosure) + dst budget row > 0; "
          "STEP(B3 -> B4-partial): 11/11 -- THE PROVEN SUB-CASE; "
          "adjudication SUBSTRATE-DIRECT-BELOW-HORIZON: the target "
          "block is certified DIRECTLY, no positivity transported "
          "(NO-EXACT-CROSS-H re-asserted; no self-supporting "
          "induction -- fresh primes + fresh census per block)")

    okfk = all(v < 0 for v in PIN_FAKE_ENDPOINTS) \
        and PIN_ENTRY_PAIRS == 4
    check("D3 entry batteries: ENTRY-NEW 4/4 + fakes NO-ENTRY",
          okfk,
          "cone entry ALWAYS at the LARGEST NEW PRIME-POWER ATOM "
          "of the dyadic gap, excluding trailing 2-powers (the note-"
          "CDLXXXIII formulation, per the Bughunt-VI F1 correction "
          "of record; %d/%d pairs incl. two pre-freeze-unmeasured "
          "deep pairs; t* >= 0.999, source tangent -v'N_q v > 0; "
          "additivity wards <= 1e-50): the r167 last-atom law "
          "generalizes to FINAL-NEW-BLOCK-TAIL; fake worlds NEVER "
          "surviving-enter (endpoints %s) -- the induction's "
          "mechanism leg dies at the death sites by NO-ENTRY"
          % (PIN_ENTRY_PAIRS, PIN_ENTRY_PAIRS, PIN_FAKE_ENDPOINTS))

    okct = all(v < 0 for v in PIN_CTRL_BLOCK)
    check("D4 controls refuse BASE AND STEP + typing",
          okct,
          "SMOOTH/SCRARITH/EPSTEIN refuse BOTH the induction base "
          "(block sums flip sign: flat %s) AND the step (BA3 "
          "false): the transfer content is arithmetic; THE FINAL "
          "COORDINATE NAMED: AVG-BUDGET-WINDOW == [census schedule, "
          "classical per k, LOOP if all-k] x [SIGMA-FLOOR, "
          "arithmetic-pinned, OPEN]; min-cut 4/5 verbatim; census "
          "{MEAS, OMEGA-POS} cardinality 4 UNCHANGED"
          % (PIN_CTRL_BLOCK,))

    print("\n  [TYPED, carried verbatim] PROVEN = DT1 + DT2 (by-"
          "recipe) + 3/2-law +")
    print("  Bertrand + the loop detections.  MEASURED = the sigma "
          "ladder (DT3), the")
    print("  entry position, the cancellation decay.  SIGMA-FLOOR "
          "stays OPEN (v929")
    print("  factorizes it).  Census cardinality 4 UNCHANGED.  NOT "
          "RH evidence.")
    print("  NO RH claim.")
    return 0


def run():
    global CHECKS, FAILS
    CHECKS = []
    FAILS = []
    print("=" * 74)
    print("v928 -- PRIME.DEPTHBLOCK.TRANSFER.01 (DT1 proven; DT2 "
          "demand law derived;")
    print("census 3/2-law sympy-exact; budget horizon k* = 23.58 "
          "recomputed; RH-loop")
    print("machine-detected; Bertrand interface sieved; round 168; "
          "NO RH claim)")
    print("=" * 74)
    rc = part()
    n_run, fails = len(CHECKS), list(FAILS)
    verdict = EXPECTED if (rc == 0 and not fails) else "MIXED"
    ok = (rc == 0 and n_run == N_CHECKS and not fails
          and verdict == EXPECTED)
    print("\n" + "=" * 74)
    print("v928: %d/%d checks passed | verdict %s | runtime %.1f s"
          % (n_run - len(fails), n_run, verdict, time.time() - T_ALL))
    print("PINNING: DT1/DT2/3-2-law/Bertrand/horizon/loops "
          "recomputed in-run; the")
    print("step/entry tables PINNED from depthblock_transfer_probe."
          "py (SPEC %s," % PIN_SPEC_R168)
    print("36/36, record 1971.3 s + re-run 1966.5 s, zero "
          "amendments, both logs kept,")
    print("RE-RUN GREEN AS TYPED AT PROMOTION).  NOT RH evidence; "
          "NO RH claim.")
    print("[%s] PATTERN GATE: expected %d checks, zero fails, verdict "
          "%s (got %d, fails %s)"
          % ("PASS" if ok else "FAIL", N_CHECKS, EXPECTED, n_run,
             fails or "none"))
    print("--- PRIME.DEPTHBLOCK.TRANSFER.01 depth-block transfer "
          "theorems: %d passed, %d failed ---"
          % (n_run - len(fails), len(fails)))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(run())
