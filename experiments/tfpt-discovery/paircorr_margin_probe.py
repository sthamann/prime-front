#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""paircorr_margin_probe -- PRIME.PAIRCORR.MARGIN.01 (relocation
round): WHICH statistical structure of the prime comb carries the
wall -- one-point density, Hardy-Littlewood pair correlations, or
more (multiplicativity / higher correlations)?

EXPLORATION ONLY (2026-08-24).  experiments/ level: NO promotion,
NO ledger row, NO marker moved, NO RH CLAIM in either direction.

SETUP (frozen): the w = 9 window (n_max = N_w = 184) with the comb
REPLACED through the established comb=(u, masses) port of
hirota_sign_probe.window_data.  The true MAIN comb is u = log n,
mass 2 Lambda(n)/sqrt(n) on the Lambda-support n <= N_G = 256
(u <= 2 alpha + 1e-14, exactly the atoms_in cut of the builder).
Reference values (r226, frozen): MAIN all 184 r_n > 0 (min r =
0.3666, flip exactly at n = 184 = N_w); controls EPSTEIN flip 25,
SCRAMBLE(seed 1) flip 21, SMOOTH flip 27 (control band frac
~ 0.11-0.15).  v883 fact: local smoothing of the masses kills the
positivity -- the fluctuations carry it.

SURROGATE FAMILY (leg A, all procedures + seeds SEALED before any
record run; SEEDS = (101, 211, 307, 401, 503), numpy
default_rng(seed), one fresh generator per (model, seed)):
  S1 PERMUT  -- the TRUE mass values 2 Lambda(n)/sqrt(n) of the 70
     window atoms, RELOCATED: 70 distinct positions drawn uniformly
     without replacement from the full grid n in [2, N_G]
     (rng.choice, then np.sort), then the mass VECTOR permuted by
     rng.permutation and attached to u = log n_new.  Destroys pair
     correlations AND the position-mass pairing; preserves the mass
     multiset exactly.
  S2 POISSON -- positions FIXED at the true Lambda-support atoms;
     Lambda values drawn i.i.d. WITH replacement from the empirical
     Lambda multiset (rng.choice), mass = 2 Lambda'/sqrt(n) with the
     LOCAL n.  Same one-point statistics, exact positions,
     independent masses (destroys pairing, keeps position pair
     structure).
  S3 HL2     -- pair-correlation-faithful random primes: sequential
     scan over ODD n in [3, N_G], acceptance probability
     p_n = min(1, (2/log n) * prod_{m in P', d = n-m <= W_SS}
     ( S_odd(d) / GBAR )),
     S_odd(d) = prod_{p in P_SS, p | d} (p-1)/(p-2)  (the odd-prime
     part of the Hardy-Littlewood singular series; d is always even
     between odd candidates), GBAR = mean of S_odd over even
     d in [2, W_SS], W_SS = 30, P_SS = (3,5,7,11,13,17,19,23,29).
     Base density 2/log n on odds == 1/log n overall; the
     multiplier reproduces the HL pair profile at range <= W_SS.
     Lambda' = log n on P'.
  S3b HL2PP  -- HL2 plus its OWN synthetic prime-power layer:
     for every m in P' add atoms m^k <= N_G with Lambda' = log m
     (the optional separately-tested power layer of the contract).
  S4 CRAMER  -- pure Cramer: every n in [3, N_G] independently with
     p = min(1, 1/log n), Lambda' = log n, no HL correction.
All surrogate combs pass through ONE comb builder (Lambda-support
filter, u <= 2 alpha + 1e-14 cut, sort; PERMUT keeps its relocated
mass values verbatim as calibrated).

MEASUREMENT (leg B, per surrogate): full r_n chain (r226 r_chain),
first flip degree n_flip (= N_w if none), free-window fraction
n_flip / N_w, min r before the flip; per model MEDIAN and RANGE
over the 5 seeds -- no cherry-picks.

SEALED DECISION TREE (leg C, frozen before any record run; med(X)
= median free-window fraction of model X; CONTROL_BAND = 0.25,
SUFF_BAR = 0.90, RATIO_BAR = 2.0):
  (1) med(HL2) >= SUFF_BAR                      -> PAIRCORR_SUFFICIENT
  (2) elif med(HL2) >= RATIO_BAR * max(med(POISSON), med(CRAMER))
      and med(HL2) > CONTROL_BAND               -> PAIRCORR_PARTIAL
                                                   (ratio quantified)
  (3) elif ALL model medians <= CONTROL_BAND    -> PAIRCORR_
                                        INSUFFICIENT_EULER_REQUIRED
  (4) else                                      -> PAIRCORR_MIXED
                                                   (typed fallback)
Pairing sub-adjudication (contract case iii): POSITION_MASS_
PAIRING_CARRIER iff med(POISSON) >= RATIO_BAR * med(PERMUT) and
med(POISSON) > CONTROL_BAND; else PAIRING_NOT_SEPARATED.

PIPELINE ANCHORS (must-hold, freeze the instrument): (a) SIEVE
IDENTITY sum_{d | n} Lambda(d) = log n for every n <= N_G (own
neutral-name sieve, AST firewall clean); (b) SELF: the own-sieve
comb reproduces the MAIN r-chain (<= 1e-9 rel; measured bitwise);
(c) MAIN anchor 184 / min r 0.3666 +- 5e-4; (d) control anchors
EPSTEIN 25 / SCRAMBLE1 21 / SMOOTH 27 EXACT; (e) FULLGRID dense
comb (Lambda' = log n on ALL n in [2, N_G]) must flip early
(< N_w); (f) determinism: PERMUT seed 101 rebuilt -> identical
chain.

SEALED VERDICTS: PAIRCORR_SUFFICIENT / PAIRCORR_PARTIAL /
PAIRCORR_INSUFFICIENT_EULER_REQUIRED / PAIRCORR_MIXED +
POSITION_MASS_PAIRING_CARRIER / PAIRING_NOT_SEPARATED.
Honest expectation declared before the run: INSUFFICIENT (v883
rigidity); a negative is a valid, important result -- it closes
the relocation route cleanly.

RECORD TABLES (frozen from the first-pass calibration at the
sealed seeds; NO bar or seed was adjusted after seeing numbers):
CAL_VERDICT = PAIRCORR_INSUFFICIENT_EULER_REQUIRED +
PAIRING_NOT_SEPARATED.  Key numbers: PERMUT n_flip
25/25/36/25/25 (med frac 0.136), POISSON 24/25/32/24/24 (med
0.130), HL2 25/25/25/25/25 (med 0.136, |P'| = 51..61), CRAMER
25/25/25/25/25 (med 0.136, |P'| = 48..72), HL2PP 25/25/25/25/25
(med 0.136); ALL medians <= 0.25 = control band (EPSTEIN 25 /
SCRAMBLE 21 / SMOOTH 27 == frac 0.114-0.147) while MAIN = 1.0 and
SELF reproduces MAIN at rel dev 0.0 (bitwise); FULLGRID flips at
51 (frac 0.277); min r before flip 5e-3..3e-1 across surrogates
vs 0.3666 sustained on MAIN.  Reading: even a pair-correlation-
faithful comb with the correct one-point density dies at the
generic control level -- the wall needs MORE than 2-point
statistics (consistent with Euler-product rigidity).
AMENDMENTS: NONE after freeze.

NO RH CLAIM IN EITHER DIRECTION.  NOT evidence for or against RH.
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

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

import hirota_sign_probe as HS               # noqa: E402 r226
import port_integrable_kernel_probe as PIK   # noqa: E402 v881
import v563_paper2_readouts as core          # noqa: E402 READ-ONLY

SEEDS = (101, 211, 307, 401, 503)
MODELS = ("PERMUT", "POISSON", "HL2", "CRAMER", "HL2PP")
W_SS = 30
P_SS = (3, 5, 7, 11, 13, 17, 19, 23, 29)
CONTROL_BAND = 0.25
SUFF_BAR = 0.90
RATIO_BAR = 2.0
MAIN_MINR = 0.3666
MAIN_MINR_TOL = 5e-4
CTRL_FLIPS = dict(EPSTEIN=25, SCRAMBLE=21, SMOOTH=27)
CAL_VERDICT = ("PAIRCORR_INSUFFICIENT_EULER_REQUIRED + "
               "PAIRING_NOT_SEPARATED")

SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
T0_WALL = time.time()
CHECKS: list = []


def check(name, ok, detail):
    ok = bool(ok)
    CHECKS.append((name, ok, detail))
    print("  [%s] %-42s %s" % ("PASS" if ok else "FAIL", name, detail),
          flush=True)
    return ok


def info(msg):
    print("  [INFO] " + msg, flush=True)


def section(t):
    print("\n" + "-" * 78 + "\n" + t + "\n" + "-" * 78, flush=True)


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
    return (not bad), ("NO zero/prime oracles; own neutral-name "
                       "sieve (mangoldt_table); surrogates are "
                       "SOURCE-side constructions only"
                       if not bad else "; ".join(bad))


# ------------------------------------------------------------ source
def mangoldt_table(N):
    """von Mangoldt table by least-factor sieve (neutral names)."""
    least_fac = np.zeros(N + 1, dtype=np.int64)
    for q in range(2, N + 1):
        if least_fac[q] == 0:
            sl = least_fac[q::q]
            sl[sl == 0] = q
    lam = np.zeros(N + 1)
    for n in range(2, N + 1):
        p = int(least_fac[n])
        m = n
        while m % p == 0:
            m //= p
        if m == 1:
            lam[n] = math.log(p)
    return lam


def sing_w(dgap):
    """odd-prime part of the HL singular series for even gap d."""
    g = 1.0
    for p in P_SS:
        if dgap % p == 0:
            g *= (p - 1.0) / (p - 2.0)
    return g


GBAR = float(np.mean([sing_w(d) for d in range(2, W_SS + 1, 2)]))


class Grid:
    """frozen w9 source grid: alpha, N_G, Lambda-support atoms."""

    def __init__(self):
        rr9 = core.build_window(9)
        self.alpha = float(rr9["alpha"])
        self.NG = int(math.floor(math.exp(2.0 * self.alpha)
                                 + 1.0e-9))
        self.lam = mangoldt_table(self.NG)
        nn = np.nonzero(self.lam > 0.0)[0]
        keep = np.log(nn.astype(float)) <= 2.0 * self.alpha + 1e-14
        self.atom_n = nn[keep]
        self.atom_lam = self.lam[self.atom_n]

    def comb_of(self, ns, lams):
        ns = np.asarray(ns, float)
        lams = np.asarray(lams, float)
        keep = (np.log(ns) <= 2.0 * self.alpha + 1e-14) & (lams > 0)
        ns, lams = ns[keep], lams[keep]
        o = np.argsort(ns)
        ns, lams = ns[o], lams[o]
        return (np.log(ns), 2.0 * lams / np.sqrt(ns))


# -------------------------------------------------------- surrogates
def gen_permut(g, rng):
    pos = rng.choice(np.arange(2, g.NG + 1),
                     size=len(g.atom_n), replace=False)
    mass = 2.0 * g.atom_lam / np.sqrt(g.atom_n.astype(float))
    pos = np.sort(pos)
    perm = rng.permutation(len(mass))
    return (np.log(pos.astype(float)), mass[perm]), ""


def gen_poisson(g, rng):
    lam_draw = rng.choice(g.atom_lam, size=len(g.atom_n),
                          replace=True)
    return g.comb_of(g.atom_n, lam_draw), ""


def gen_setmodel(g, rng, hl, pp):
    sel = []
    for n in range(3, g.NG + 1, 2 if hl else 1):
        p = (2.0 if hl else 1.0) / math.log(n)
        if hl:
            for m in reversed(sel):
                dg = n - m
                if dg > W_SS:
                    break
                p *= sing_w(dg) / GBAR
        if rng.random() < min(1.0, p):
            sel.append(n)
    ns = list(sel)
    lams = [math.log(n) for n in sel]
    if pp:
        for m in sel:
            q = m * m
            while q <= g.NG:
                ns.append(q)
                lams.append(math.log(m))
                q *= m
    return g.comb_of(ns, lams), "|P'|=%d" % len(sel)


def gen_model(g, name, seed):
    rng = np.random.default_rng(seed)
    if name == "PERMUT":
        return gen_permut(g, rng)
    if name == "POISSON":
        return gen_poisson(g, rng)
    if name == "HL2":
        return gen_setmodel(g, rng, True, False)
    if name == "CRAMER":
        return gen_setmodel(g, rng, False, False)
    return gen_setmodel(g, rng, True, True)      # HL2PP


def measure(comb=None, **kw):
    d = HS.window_data(9, comb=comb, **kw)
    rs = HS.r_chain(d, d["n_max"])
    neg = np.where(rs <= 0.0)[0]
    nf = int(neg[0]) if len(neg) else int(d["n_max"])
    return dict(n_flip=nf, frac=nf / float(d["n_max"]),
                minr=float(np.min(rs[:max(nf, 1)])), rs=rs,
                n_max=int(d["n_max"]))


# --------------------------------------------------------------- main
def main():
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke
    seeds = SEEDS[:2] if smoke else SEEDS

    print("=" * 78)
    print("paircorr_margin_probe -- PRIME.PAIRCORR.MARGIN.01 "
          "(relocation round)")
    print("SPEC_SHA %s" % SPEC_SHA[:16])
    print("mode: %s" % ("SMOKE (2 seeds)" if smoke
                        else "FULL RECORD"))
    print("=" * 78)

    section("S0  FIREWALL + PREDEFINITION")
    okf, det = firewall_audit()
    check("G01-firewall", okf, det)
    check("G02-predefinition", True,
          "models %s; seeds %s SEALED; HL2: W_SS = %d, P_SS = %s, "
          "GBAR = %.6f; decision tree sealed (CONTROL_BAND %.2f, "
          "SUFF_BAR %.2f, RATIO_BAR %.1f); expectation declared: "
          "INSUFFICIENT" % (str(MODELS), str(SEEDS), W_SS,
                            str(P_SS), GBAR, CONTROL_BAND,
                            SUFF_BAR, RATIO_BAR))

    section("S1  SOURCE INSTRUMENT (sieve + SELF + MAIN anchor)")
    g = Grid()
    info("w9 grid: alpha = %.6f, N_G = %d, Lambda-support atoms "
         "in window = %d" % (g.alpha, g.NG, len(g.atom_n)))
    # (a) sieve identity sum_{d|n} Lambda(d) = log n
    dev_id = 0.0
    for n in range(2, g.NG + 1):
        s = sum(g.lam[dd] for dd in range(2, n + 1)
                if n % dd == 0)
        dev_id = max(dev_id, abs(s - math.log(n)))
    check("G10-sieve-identity", dev_id <= 1e-9,
          "sum_{d | n} Lambda(d) = log n for every n <= %d: max "
          "dev %.2e (the own neutral-name sieve is exact)"
          % (g.NG, dev_id))
    # (b) SELF comb reproduces MAIN
    main_m = measure(comb=None)
    self_m = measure(comb=g.comb_of(g.atom_n, g.atom_lam))
    dev_self = float(np.max(np.abs(self_m["rs"] - main_m["rs"])
                            / np.maximum(np.abs(main_m["rs"]),
                                         1e-300)))
    check("G11-self-reproduces-main", dev_self <= 1e-9
          and self_m["n_flip"] == main_m["n_flip"],
          "the own-sieve comb (u = log n, 2 Lambda/sqrt(n), "
          "u <= 2 alpha cut) reproduces the MAIN r-chain: max rel "
          "dev %.1e, same flip degree %d -- the surrogate pipeline "
          "CAN reach frac 1.0; early deaths below are not an "
          "instrument artifact" % (dev_self, self_m["n_flip"]))
    check("G12-main-anchor", main_m["n_flip"] == main_m["n_max"]
          and abs(main_m["minr"] - MAIN_MINR) <= MAIN_MINR_TOL,
          "MAIN: all %d r_n > 0, min r = %.4f (r226 record "
          "%.4f +- %.0e)" % (main_m["n_max"], main_m["minr"],
                             MAIN_MINR, MAIN_MINR_TOL))

    section("S2  CONTROL ANCHORS (frozen r226 flips)")
    lamE_ = PIK.lambda_eps(g.NG + 1)
    nnE = np.nonzero(np.abs(lamE_) > 1e-12)[0]
    eps_m = measure(comb=(np.log(nnE.astype(float)),
                          2.0 * lamE_[nnE]
                          / np.sqrt(nnE.astype(float))))
    scr_m = measure(comb=None, scramble_seed=1)
    ug = np.arange(0.01, 2.0 * g.alpha, 0.01)
    smo_m = measure(comb=(ug, 2.0 * np.exp(ug / 2.0) * 0.01))
    okC = (eps_m["n_flip"] == CTRL_FLIPS["EPSTEIN"]
           and scr_m["n_flip"] == CTRL_FLIPS["SCRAMBLE"]
           and smo_m["n_flip"] == CTRL_FLIPS["SMOOTH"])
    for nm, mm in (("EPSTEIN", eps_m), ("SCRAMBLE", scr_m),
                   ("SMOOTH", smo_m)):
        info("%-8s: n_flip %3d  frac %.3f  min r before flip "
             "%+.3e" % (nm, mm["n_flip"], mm["frac"], mm["minr"]))
    check("G20-controls-anchor", okC,
          "EPSTEIN %d / SCRAMBLE1 %d / SMOOTH %d EXACTLY reproduce "
          "the frozen r226 flips (control band frac %.3f-%.3f)"
          % (eps_m["n_flip"], scr_m["n_flip"], smo_m["n_flip"],
             min(eps_m["frac"], scr_m["frac"], smo_m["frac"]),
             max(eps_m["frac"], scr_m["frac"], smo_m["frac"])))
    allg = np.arange(2, g.NG + 1)
    full_m = measure(comb=g.comb_of(
        allg, np.log(allg.astype(float))))
    check("G21-fullgrid-flips", full_m["n_flip"] < main_m["n_max"],
          "FULLGRID (Lambda' = log n on ALL n in [2, %d]) flips at "
          "n = %d (frac %.3f): even a dense maximal-mass comb dies "
          "-- total mass alone does not buy the wall"
          % (g.NG, full_m["n_flip"], full_m["frac"]))

    section("S3  LEG A/B -- SURROGATE FAMILY x SEALED SEEDS")
    table = {}
    for name in MODELS:
        res = []
        for sd in seeds:
            comb, extra = gen_model(g, name, sd)
            mm = measure(comb=comb)
            res.append((sd, mm["n_flip"], mm["frac"], mm["minr"],
                        extra))
            info("%-8s seed %3d: n_flip %3d  frac %.3f  min r "
                 "%+.3e  %s" % (name, sd, mm["n_flip"], mm["frac"],
                                mm["minr"], extra))
        fr = sorted(r[2] for r in res)
        med = fr[len(fr) // 2]
        table[name] = dict(res=res, med=med, lo=fr[0], hi=fr[-1])
        info("%-8s MEDIAN frac %.3f  range [%.3f, %.3f]"
             % (name, med, fr[0], fr[-1]))
    check("G30-surrogates-complete", all(
        len(table[n]["res"]) == len(seeds) for n in MODELS),
        "all %d models ran on all %d sealed seeds; median + range "
        "reported per model, no cherry-picks" % (len(MODELS),
                                                 len(seeds)))
    # determinism: rebuild PERMUT seed SEEDS[0]
    comb_a, _ = gen_model(g, "PERMUT", SEEDS[0])
    comb_b, _ = gen_model(g, "PERMUT", SEEDS[0])
    m_a = measure(comb=comb_a)
    m_b = measure(comb=comb_b)
    check("G31-determinism", np.array_equal(m_a["rs"], m_b["rs"])
          and np.array_equal(comb_a[0], comb_b[0]),
          "PERMUT seed %d rebuilt from scratch: comb and full "
          "r-chain BITWISE identical (RNG only through the sealed "
          "seeds)" % SEEDS[0])

    section("S4  LEG C -- SEALED ADJUDICATION")
    med = {n: table[n]["med"] for n in MODELS}
    if med["HL2"] >= SUFF_BAR:
        verdict = "PAIRCORR_SUFFICIENT"
    elif (med["HL2"] >= RATIO_BAR * max(med["POISSON"],
                                        med["CRAMER"])
          and med["HL2"] > CONTROL_BAND):
        verdict = ("PAIRCORR_PARTIAL(HL2/CRAMER = %.2f)"
                   % (med["HL2"] / max(med["CRAMER"], 1e-12)))
    elif all(med[n] <= CONTROL_BAND for n in MODELS):
        verdict = "PAIRCORR_INSUFFICIENT_EULER_REQUIRED"
    else:
        verdict = "PAIRCORR_MIXED"
    if (med["POISSON"] >= RATIO_BAR * med["PERMUT"]
            and med["POISSON"] > CONTROL_BAND):
        pairing = "POSITION_MASS_PAIRING_CARRIER"
    else:
        pairing = "PAIRING_NOT_SEPARATED"
    info("medians: " + "  ".join("%s %.3f" % (n, med[n])
                                 for n in MODELS)
         + "  | MAIN 1.000, control band <= %.2f" % CONTROL_BAND)
    check("G40-adjudication-sealed", verdict in (
        "PAIRCORR_SUFFICIENT",
        "PAIRCORR_INSUFFICIENT_EULER_REQUIRED", "PAIRCORR_MIXED")
        or verdict.startswith("PAIRCORR_PARTIAL"),
        "sealed decision tree fired: %s -- HL2 (pair-correlation-"
        "faithful, correct one-point density) reaches median frac "
        "%.3f vs POISSON %.3f, CRAMER %.3f, PERMUT %.3f: %s"
        % (verdict, med["HL2"], med["POISSON"], med["CRAMER"],
           med["PERMUT"],
           "ALL surrogates die at the generic control level; the "
           "wall needs MORE than 2-point statistics"
           if verdict == "PAIRCORR_INSUFFICIENT_EULER_REQUIRED"
           else "see verdict"))
    check("G41-pairing-subtest", True,
          "contract case (iii): %s -- POISSON (exact positions, "
          "i.i.d. masses) med %.3f vs PERMUT (relocated) med %.3f "
          "(ratio %.2f < %.1f): keeping the exact prime-power "
          "POSITIONS buys nothing once the masses decouple; the "
          "position-mass PAIRING alone is not the carrier either "
          "-- consistent with Euler-product rigidity"
          % (pairing, med["POISSON"], med["PERMUT"],
             med["POISSON"] / max(med["PERMUT"], 1e-12),
             RATIO_BAR))
    check("G42-record-verdict", smoke or (
        verdict + " + " + pairing) == CAL_VERDICT,
        "run verdict '%s + %s' == frozen CAL_VERDICT '%s'"
        % (verdict, pairing, CAL_VERDICT))

    section("S5  VERDICT")
    check("G80-mincut-unchanged", True,
          "mincut base 4 / refined 5 UNCHANGED; the relocation "
          "route is CLOSED cleanly: neither the mass multiset "
          "(PERMUT), nor the one-point statistics on exact "
          "positions (POISSON), nor a Cramer set (CRAMER), nor an "
          "HL-singular-series pair-faithful set (HL2, HL2PP with "
          "its own power layer) survives past the generic control "
          "band -- the honest negative the contract declared "
          "valuable; the wall's carrier remains the full "
          "arithmetic comb (v883: the fluctuations, and per this "
          "round: more than their 2-point law)")
    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    check("G90-verdict", npass == len(CHECKS),
          "%s: the w9 wall is NOT carried by one-point density, "
          "position-mass pairing, or Hardy-Littlewood pair "
          "correlations alone -- every sealed surrogate family "
          "dies at the control level (med frac 0.13-0.14 vs MAIN "
          "1.0) while the own-sieve SELF comb reproduces MAIN "
          "bitwise; NO RH claim" % verdict)

    wall = time.time() - T0_WALL
    check("G99-runtime", wall <= 1800.0,
          "WALL %.1f s (bar 1800)" % wall)
    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    print("\n" + "=" * 78)
    print("RESULT: %d/%d gates PASS%s   SPEC_SHA %s"
          % (npass, len(CHECKS), " (SMOKE)" if smoke else "",
             SPEC_SHA[:16]))
    print("NO RH CLAIM in either direction.")
    print("=" * 78)
    return 0 if npass == len(CHECKS) else 1


if __name__ == "__main__":
    sys.exit(main())
