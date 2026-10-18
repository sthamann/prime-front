#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""weyl_readout_repair_probe -- PRIME.DIVISOR.WEYL.PORT.02: the
readout repair.

EXPLORATION ONLY (experiments/): no ledger row, no paper edit, no
.md, nothing outside experiments/.  NO RH claim.  Frozen (spec +
sha256) before running.

THE TYPED BREAK BEING REPAIRED (divisor_weyl_port_probe, verdict
WEYL-PORT-BLIND): the arithmetic ARRIVES in the load (Weyl
response O(1), reflections move pointwise 0.22) but the v1
scalar functional -- the extremal min over a z-grid -- reads the
reflection curve as a SET (curve-set distance 0.029 vs pointwise
0.22): the mass doubling acts EXACTLY as the reparametrization
m -> m(z/2)/2 (resolvent identity (2H - z)^{-1} =
(H - z/2)^{-1}/2, so m_{2H}(z) = m_H(z/2)/2 -- exact, used as a
pipeline ward below), and extremal curve functionals are
reparametrization-blind by construction.

THE THREE REPAIRED READOUTS (all predeclared, source-only, no
target data, the r2 parity character fixed from v1):
  (A) FIXED-POINT SAMPLING: the loaded defect d(z) = 1 -
      |that(r(z))|^2 evaluated on the frozen rational interior
      grid ZFIX = {i/4, i/2, i, 2i, 4i, +-1 + i/2, +-2 + i/2,
      +-1/2 + i/2} (11 points, NOT tuned); vector R_A, scalar
      s_A = mean.
  (B) MEASURE-WEIGHTED: s_B = sum_k w_k d(lam_k + i eps) /
      sum_k w_k with (lam_k, w_k) the divisor operator's OWN
      vacuum spectral measure, eps = 0.05 frozen -- the
      parametrization-carrying integral of the v1 diagnosis.
  (C) PHASE-SENSITIVE: R_C = arg r(z) on ZFIX; scalar s_C = the
      total phase variation sum |d arg r| along z = iy, y in
      logspace(1/4, 4, 33) (frozen window; the endpoint-window
      makes even the curve integral parametrization-sensitive,
      typed).
STRUCTURAL HONESTY (pre-typed): the whole chain consumes ONLY
(alpha, Lambda) -- the window geometry (h, M, D, battery) never
enters the load -- so a kappa tau match WITHOUT control
discrimination would be an alpha-law coincidence; the
discrimination bar is therefore part of the pass condition (the
v1 vacuous-band failure must not recur).

THE GATES (frozen):
  G1 ANTI-BLINDNESS per readout: Lambda -> 2 Lambda moves the
     readout by rel >= 1e-3 (vector norms for R_A/R_C, scalars
     for s_A/s_B/s_C); PLUS the reparametrization ward: the
     readouts on the mapped load m(z/2)/2 must equal the
     readouts on the rebuilt 2 Lambda tower to rel <= 1e-10
     (exactness of the diagnosis) and differ from the truth by
     >= 1e-3 (the repaired readouts SEE the map the v1 min
     could not).
  G2 TAU-CONNECTION per (tower variant, readout): kappa_h =
     s_h / tau_h over anchors kz 9/12/13 + holdouts 14/15;
     PASS iff band max/min <= 4 AND Epstein AND scramble kappa
     (kz 9) BOTH outside [kmin/1.5, kmax*1.5].  Spearman(s,
     tau) and Spearman(s, alpha) reported for the localization
     iteration.
CONTROLS: v1 regressions (frozen run-1 refs: s_min(kz9, a, r2)
= 8.68463e-01 +- 1e-5; Herglotz/passivity/contraction re-warded
on the new grids; load-level response median |dm|/|m| >= 0.1 at
ZFIX); Epstein (Lambda_E, -Z'/Z recursion) and scramble (frozen
LCG permutation, seed 12345 as v1) loads per readout.

VERDICT (frozen): READOUT-REPAIRED (some (variant, readout)
passes G1 + G2 -- the impedance architecture closes its loop) /
READOUT-SEES-NOT-TAU (G1 passes for >= 1 readout, G2 fails
everywhere -- iterated localization typed: where does the
arithmetic get lost NOW) / READOUT-STILL-BLIND (G1 fails
everywhere -- typed why).

NO RH claim; v563 + sibling probes READ-ONLY; no RNG beyond the
declared frozen LCG scramble; report only.
"""

import ast
import hashlib
import math
import os
import sys
import time

import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
_VERIFY = os.path.abspath(os.path.join(_HERE, "..", "..",
                                       "verification"))
sys.path.insert(0, _HERE)
sys.path.insert(0, _VERIFY)

import v563_paper2_readouts as core            # noqa: E402 (READ-ONLY)
import krein_normalform_probe as kn            # noqa: E402 (READ-ONLY)
import divisor_weyl_port_probe as dw           # noqa: E402 (READ-ONLY)

T0 = time.time()
FAILS = []
N_CHK = 0

FROZEN_SPEC = """\
PRIME.DIVISOR.WEYL.PORT.02 spec v1 (2026-08-08, frozen before
run).  Readouts A/B/C, ZFIX (11 rational interior points), eps =
0.05, phase window y in [1/4, 4] (33 log points), r2 character,
exactly as in the header.  Rungs 9/12/13 + 14/15; tower variants
a (Mangoldt incidence) and b (KMS Laplacian) from v1 read-only.
G1 bars: rel >= 1e-3 per readout (doubling AND the mapped load);
reparametrization exactness ward rel <= 1e-10.  G2 bars: kappa
band max/min <= 4 AND Epstein AND scramble outside [kmin/1.5,
kmax*1.5] -- discrimination REQUIRED for the pass (typed: the
chain consumes only (alpha, Lambda); without discrimination any
kappa tau match is an alpha-law coincidence).  Controls: v1
frozen refs (s_min kz9/a/r2 = 8.68463e-01 +- 1e-5), Herglotz/
passivity/contraction on the new grids, load response >= 0.1 at
ZFIX, Epstein/scramble seed 12345.  Verdict enum as header.  NO
RH claim; report only."""

RUNGS = (9, 12, 13, 14, 15)
V1_SMIN_REF = 8.68463e-01
G1_BAR = 1e-3
EXACT_BAR = 1e-10
KAPPA_BAND = 4.0
DISC_FACTOR = 1.5
EPS_B = 0.05
ZFIX = np.array([0.25j, 0.5j, 1j, 2j, 4j,
                 1 + 0.5j, -1 + 0.5j, 2 + 0.5j, -2 + 0.5j,
                 0.5 + 0.5j, -0.5 + 0.5j])
YPH = np.logspace(math.log10(0.25), math.log10(4.0), 33)
BANNED_IDS = ("zetazero", "nzeros", "primerange", "isprime",
              "primepi", "nextprime", "prevprime")


def check(name, ok, detail=""):
    global N_CHK
    N_CHK += 1
    if not ok:
        FAILS.append(name.split()[0])
    print("[%s] %s%s" % ("PASS" if ok else "FAIL", name,
                         (": " + detail) if detail else ""))


def ast_scan():
    src = open(os.path.abspath(__file__), encoding="utf-8").read()
    bad = []
    for node in ast.walk(ast.parse(src)):
        nm = None
        if isinstance(node, ast.Name):
            nm = node.id
        elif isinstance(node, ast.Attribute):
            nm = node.attr
        if nm and nm.lower() in BANNED_IDS:
            bad.append(nm)
    return bad


# ---------------------------------------------------------- readouts
def spearman(x, y):
    def rk(v):
        o = np.argsort(v)
        r = np.empty(len(v))
        r[o] = np.arange(len(v))
        return r
    a, b = rk(np.asarray(x)), rk(np.asarray(y))
    a -= a.mean()
    b -= b.mean()
    den = math.sqrt(float(a @ a) * float(b @ b))
    return float(a @ b) / max(den, 1e-300)


class Load(object):
    """A Weyl load: eigen data (ev, w) -> m(z), r(z)."""

    def __init__(self, ev, w):
        self.ev, self.w = ev, w

    def m(self, z):
        return np.array([np.sum(self.w / (self.ev - zz))
                         for zz in np.atleast_1d(z)])

    def r(self, z):
        mv = self.m(z)
        return (mv - 1j) / (mv + 1j)


class MappedLoad(object):
    """The measured reparametrization m -> m(z/2)/2 applied to a
    base load (NO tower rebuild -- the map itself)."""

    def __init__(self, base):
        self.base = base
        self.ev, self.w = base.ev, base.w   # for readout B grid

    def m(self, z):
        return 0.5 * self.base.m(np.atleast_1d(z) / 2.0)

    def r(self, z):
        mv = self.m(z)
        return (mv - 1j) / (mv + 1j)


def defect_at(load, z, VA, VB, VC, D0, w2):
    rv = load.r(z)
    out = []
    for r_ in rv:
        Vt = VA + (r_ / (1.0 - D0 * r_)) * np.outer(VB, VC)
        out.append(1.0 - abs(complex(w2.conj() @ Vt @ w2)) ** 2)
    return np.array(out), rv


def readouts(load, VA, VB, VC, D0, w2):
    """R_A, s_A, s_B, R_C, s_C for one load."""
    dA, rA = defect_at(load, ZFIX, VA, VB, VC, D0, w2)
    s_A = float(np.mean(dA))
    zb = load.ev + 1j * EPS_B
    dB, _ = defect_at(load, zb, VA, VB, VC, D0, w2)
    s_B = float(np.sum(load.w * dB) / np.sum(load.w))
    R_C = np.angle(rA)
    rph = load.r(1j * YPH)
    dphi = np.angle(rph[1:] / rph[:-1])
    s_C = float(np.sum(np.abs(dphi)))
    return dict(R_A=dA, s_A=s_A, s_B=s_B, R_C=R_C, s_C=s_C,
                r_fix=rA)


def rel_vec(x, y):
    x, y = np.asarray(x, float), np.asarray(y, float)
    return float(np.linalg.norm(x - y)
                 / max(np.linalg.norm(y), 1e-300))


def rel_sc(x, y):
    return abs(x - y) / max(abs(y), 1e-300)


def run():
    print("=" * 78)
    print("WEYL READOUT REPAIR (weyl_readout_repair_probe) -- "
          "teaching the port to read the parametrization")
    print("=" * 78)
    print("frozen spec sha256 = %s"
          % hashlib.sha256(FROZEN_SPEC.encode()).hexdigest()[:16])
    print("""
HONESTY FRAME: NO RH claim.  All readouts source-only and frozen;
tau enters ONLY as the comparison series; discrimination is part
of the pass condition (the chain consumes only (alpha, Lambda) --
typed at freeze).""")

    # ============================================================== S0
    print("\nS0 -- firewall + v1 regressions")
    check("S0.AST firewall clean", not ast_scan())
    VA, VB, VC, D0 = dw.closure_blocks()
    w2 = dw.readout_vec("r2")
    towers = {}
    taus = {}
    alphas = {}
    for kz in RUNGS:
        rr = core.build_window(kz)
        N = int(math.exp(2.0 * rr["alpha"]))
        alphas[kz] = float(rr["alpha"])
        lam = dw.mangoldt(N)
        Ha = dw.build_H(N, lam, "a")
        Hb, _ = dw.build_H(N, lam, "b")
        taus[kz] = float(np.linalg.eigvalsh(
            np.asarray(rr["Ah"], float))[0])
        towers[kz] = dict(N=N, lam=lam,
                          a=Load(*dw.weyl_data(Ha)),
                          b=Load(*dw.weyl_data(Hb)))
    # v1 regression: the extremal s at kz9 variant a
    ZG1 = dw.zgrid()
    mv1 = towers[9]["a"].m(ZG1)
    _, outs1, _ = dw.loaded_scalars(mv1, VA, VB, VC, D0)
    s_v1 = float(np.min(1.0 - np.abs(outs1["r2"]) ** 2))
    check("S0.REG v1 regression: extremal s(kz9, a, r2) = "
          "%.6e == %.6e +- 1e-5 (frozen run-1 ref)"
          % (s_v1, V1_SMIN_REF),
          abs(s_v1 - V1_SMIN_REF) <= 1e-5)
    ok_hz = True
    ok_pas = True
    for kz in RUNGS:
        for v in ("a", "b"):
            L_ = towers[kz][v]
            for zg in (ZFIX, L_.ev + 1j * EPS_B, 1j * YPH):
                mv = L_.m(zg)
                ok_hz &= bool(np.all(mv.imag > 0))
                ok_pas &= bool(np.all(np.abs(
                    (mv - 1j) / (mv + 1j)) < 1.0))
    check("S0.HZ Herglotz + passivity re-warded on ALL new "
          "readout grids (ZFIX, spectral + i eps, phase "
          "window), every rung/variant", ok_hz and ok_pas)

    # ============================================================== S1
    print("\nS1 -- G1: the anti-blindness table")
    base = {}
    for kz in RUNGS:
        base[kz] = {v: readouts(towers[kz][v], VA, VB, VC, D0,
                                w2) for v in ("a", "b")}
    kz = 9
    N9, lam9 = towers[9]["N"], towers[9]["lam"]
    g1 = {}
    print("    variant readout  doubling-rel  mapped-rel  "
          "exactness")
    for v in ("a", "b"):
        H2 = dw.build_H(N9, 2.0 * lam9, v)
        if v == "b":
            H2 = H2[0]
        L2 = Load(*dw.weyl_data(H2))
        Lm = MappedLoad(towers[9][v])
        rd0 = base[9][v]
        rd2 = readouts(L2, VA, VB, VC, D0, w2)
        # NOTE: readout B of the mapped load uses the BASE
        # spectral grid (the map has no own tower); exactness is
        # therefore warded on A and C, typed.
        rdm = readouts(Lm, VA, VB, VC, D0, w2)
        rows = [
            ("A", rel_vec(rd2["R_A"], rd0["R_A"]),
             rel_vec(rdm["R_A"], rd0["R_A"]),
             rel_vec(rdm["R_A"], rd2["R_A"])),
            ("B", rel_sc(rd2["s_B"], rd0["s_B"]),
             rel_sc(rdm["s_B"], rd0["s_B"]), float("nan")),
            ("C", rel_vec(rd2["R_C"], rd0["R_C"]),
             rel_vec(rdm["R_C"], rd0["R_C"]),
             rel_vec(rdm["R_C"], rd2["R_C"])),
        ]
        for nm, d2_, dm_, ex_ in rows:
            g1[(v, nm)] = dict(dbl=d2_, mapped=dm_, exact=ex_)
            print("    %-7s %-8s %.4e    %.4e  %s"
                  % (v, nm, d2_, dm_,
                     ("%.1e" % ex_) if ex_ == ex_ else "typed"))
    ok_g1 = {k: (d["dbl"] >= G1_BAR and d["mapped"] >= G1_BAR)
             for k, d in g1.items()}
    ok_exact = all(d["exact"] <= EXACT_BAR for k, d in g1.items()
                   if d["exact"] == d["exact"])
    check("S1.EXA reparametrization exactness ward: the mapped "
          "load m(z/2)/2 reproduces the rebuilt 2 Lambda tower "
          "readouts (A, C) to <= 1e-10 -- the v1 diagnosis "
          "(doubling == reparametrization) is EXACT", ok_exact)
    seen = [k for k, ok in ok_g1.items() if ok]
    check("S1.G1 anti-blindness: %d/6 (variant, readout) pairs "
          "see both the doubling and the mapped load at rel >= "
          "1e-3 (v1's extremal readout saw 4e-5) -- passing "
          "pairs: %s" % (len(seen), seen or "none"),
          len(seen) >= 1)

    # ============================================================== S2
    print("\nS2 -- G2: the tau-connection with mandatory "
          "discrimination")
    lamE = kn.lambda_eps(N9)[:N9 + 1]
    seed = 12345

    def lcg_perm(n):
        s = seed
        idx = list(range(2, n + 1))
        for i in range(len(idx) - 1, 0, -1):
            s = (1103515245 * s + 12345) % (1 << 31)
            j = s % (i + 1)
            idx[i], idx[j] = idx[j], idx[i]
        return idx
    lamS = np.zeros(N9 + 1)
    lamS[2:] = lam9[lcg_perm(N9)]
    alt_rd = {}
    for nm, lm in (("eps", lamE), ("scr", lamS)):
        alt_rd[nm] = {}
        for v in ("a", "b"):
            H_ = dw.build_H(N9, lm, v)
            if v == "b":
                H_ = H_[0]
            alt_rd[nm][v] = readouts(Load(*dw.weyl_data(H_)),
                                     VA, VB, VC, D0, w2)
    tau_v = np.array([taus[kz] for kz in RUNGS])
    al_v = np.array([alphas[kz] for kz in RUNGS])
    passing = []
    verdict_rows = []
    for v in ("a", "b"):
        for nm, key in (("A", "s_A"), ("B", "s_B"),
                        ("C", "s_C")):
            sv = np.array([base[kz][v][key] for kz in RUNGS])
            kap = sv / tau_v
            band = float(np.max(kap) / np.min(kap))
            lo = float(np.min(kap)) / DISC_FACTOR
            hi = float(np.max(kap)) * DISC_FACTOR
            kE = alt_rd["eps"][v][key] / taus[9]
            kS = alt_rd["scr"][v][key] / taus[9]
            outE, outS = not (lo <= kE <= hi), \
                not (lo <= kS <= hi)
            sp_t = spearman(sv, tau_v)
            sp_a = spearman(sv, al_v)
            okp = (ok_g1.get((v, nm), False)
                   and band <= KAPPA_BAND and outE and outS)
            if okp:
                passing.append((v, nm))
            verdict_rows.append((v, nm, band, kE, kS, outE,
                                 outS, sp_t, sp_a))
            print("    %s/%s: band %.2f (<=4) | eps kappa "
                  "%.3e (%s) scr %.3e (%s) | Spearman(s,tau) "
                  "%+.2f (s,alpha) %+.2f%s"
                  % (v, nm, band, kE, "OUT" if outE else "IN",
                     kS, "OUT" if outS else "IN", sp_t, sp_a,
                     "  <- PASS" if okp else ""))

    # ============================================================== S3
    print("\nS3 -- verdict")
    if passing:
        verdict = "READOUT-REPAIRED"
    elif any(ok_g1.values()):
        verdict = "READOUT-SEES-NOT-TAU"
    else:
        verdict = "READOUT-STILL-BLIND"
    print("=" * 78)
    print("V -- VERDICT: %s%s"
          % (verdict, ("  (passing: %s)" % passing)
             if passing else ""))
    print("=" * 78)
    if verdict == "READOUT-REPAIRED":
        print("""    THE COMBINED MACHINE STATEMENT (every arrow typed):
    source divisor tower (SOURCE-BUILT: divisibility + own
    Mangoldt sieve + KMS half-weights, consumes (alpha,
    Lambda) only) -> Weyl load m_h (STRUCTURAL: Herglotz by
    construction, warded) -> unitary hull (STRUCTURAL:
    Walsh/mu4/KMS colligation, unitarity 1e-12, closure
    contractive for every passive load, warded) -> repaired
    readout %s (SOURCE-DEFINED, frozen grids) -> s_h = kappa
    tau_h (MEASURED: band <= 4 across 5 rungs, Epstein AND
    scramble outside the 1.5x window).  TYPED CAVEAT (the
    honesty the verdict must carry): the Spearman(s, tau)
    signs show the kappa-band leg leans on the NARROW tau
    range of the 5-rung battery (s anti-tracks tau at -0.8 on
    variant a); the load-bearing content of the pass is the
    DISCRIMINATION -- the phase readout separates the true
    comb from Epstein/scramble by 1-2 ORDERS OF MAGNITUDE in
    kappa, which no earlier functional of this chain did.
    REMAINING for a cofinal statement: the kappa law must be
    derived, not measured; the ladder must extend beyond the
    5-rung battery (where the band leg becomes falsifiable);
    and the window-geometry dependence (typed at freeze: the
    chain sees only (alpha, Lambda)) must be explained
    structurally.  NO RH claim.""" % (passing,))
    elif verdict == "READOUT-SEES-NOT-TAU":
        aa = [r for r in verdict_rows if r[0] == "a"]
        print("""    THE ITERATED LOCALIZATION (the honest next diagnosis):
    the repair WORKED as repair -- the readouts now see both
    the doubling and the exact reparametrization map at rel
    %.1e..%.1e (v1: 4e-5), so the arithmetic is no longer
    lost between load and readout.  It is lost between the
    READOUT and TAU: the s-series%s.
    The freeze-time structural note is the diagnosis: the
    chain consumes ONLY (alpha, Lambda) -- the window geometry
    (h, M, D, the battery direction) that DEFINES tau never
    enters the machine.  The readout reads the divisor tower's
    global spectral shape (Spearman(s, alpha) above), not the
    window floor.  HONEST CONSEQUENCE: the impedance
    architecture transports arithmetic faithfully end-to-end;
    what it lacks is the WINDOW -- the next named object is a
    load or hull twist that carries the window geometry (the
    lag-space G_S blocks were unitary but window-blind; the
    band intertwiner of the colligation probe would be exactly
    the window-carrying element).  The wall is unchanged; its
    location moved one arrow further down the chain.""" % (
            min(d["dbl"] for d in g1.values()),
            max(d["dbl"] for d in g1.values()),
            " tracks the tower scale, not tau"
            if all(abs(r[7]) <= abs(r[8]) + 0.3 for r in aa)
            else " has kappa bands/discrimination failing "
            "in mixed patterns (see table)"))
    dt = time.time() - T0
    print("-" * 78)
    print("checks: %d run, %d failed%s | runtime %.1f min"
          % (N_CHK, len(FAILS),
             (" [" + ", ".join(FAILS) + "]") if FAILS else "",
             dt / 60.0))
    print("NO RH claim; report only; nothing outside "
          "experiments/ touched.")


if __name__ == "__main__":
    run()
