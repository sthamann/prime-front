#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""phase_polygon_probe -- PRIME.PHASE.POLYGON.01
(EXPLORATION ONLY, experiments/; round 34, successor of the
executed Pruefer/Cotlar contract (COTLAR-GROWING), 2026-08-08
evening plan).

THE EXACT LEMMA (the analytic target): for H_m = sum_{j<=m}
d_j u(th_j)u(th_j)^T with u(th) = (cos th, sin th)^T:

  H_m = 1/2 [[S0 + Re S2, Im S2], [Im S2, S0 - Re S2]],
  S0 = sum d_j,  S2 = sum d_j e^{2 i th_j},
  eig(H_m) = 1/2 (S0 +- |S2|),
  H_m >= 0  <=>  S0(m) >= |S2(m)|

-- 2D matrix positivity as a scalar inequality on a complex
exponential sum.  NO RH claim; writes nothing; v563 +
gauss_node_unitary + cdcore + pruefer machinery READ-ONLY.

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/phase_polygon_probe.py
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

import v563_paper2_readouts as core            # noqa: E402  (READ-ONLY)
import gauss_node_unitary_probe as gnu         # noqa: E402  (READ-ONLY)
import cdcore_probe as cdc                     # noqa: E402  (READ-ONLY)
import pruefer_compensation_probe as ppc       # noqa: E402  (READ-ONLY)

FROZEN_SPEC = """\
PRIME.PHASE.POLYGON.01 spec v1 (2026-08-08, frozen before
run).  Machinery read-only: gnu.build_rung/folded_arm_measure,
cdc.stieltjes_chain, ppc.pruefer_phase (the executed round-34
contract's phase discipline).  Ladder: battery = frame_a_zones
with h <= 900 (the 42 CD rungs) + the frozen deep holdouts
kz {90, 116, 142, 177, 243}.  LEMMA A (frozen construction):
per arm the source chain (al, be, m0) = stieltjes_chain of
the folded arm measure with m_steps = min(h, #support); the
canonical rank-one terms at the FROZEN reference energy x0
are y_j = (p_j(x0), be_j p_{j+1}(x0)) = R_j u(th_j) for j =
0..len(be)-1 (orthonormal gauge p_0 = 1/sqrt(m0) -- the
common Pruefer gauge carries each measure's mass); H_+- :=
sum_j R_j^2 u(th_j)u(th_j)^T; the signed decomposition
H_+ - H_- = sum d_j u(th_j)u(th_j)^T with d_j = +R_j^2(plus),
-R_j^2(minus).  Reference energies: PRIMARY x0 = 0 (band
center), secondary x0 = +-1/2 (min-margin census only).
PREFIX ORDER (frozen): interleaved by step index, plus term
then minus term at each j, continuing with the longer chain's
remaining terms.  WARDS: W-L1 (synthetic, seed 0, n = 50
random d/th): the lemma identity matrix + eigenvalues to
1e-12; W-L2 (deployed, anchors {9, 12, 13, 26, 40} + the
holdouts): round-trip -- the trig assembly 1/2[[S0+ReS2,
ImS2],[ImS2, S0-ReS2]] from the renormalized-double Pruefer
path must equal the RAW long-double recursion sums
[[sum p^2, sum be p p'],[., sum be^2 p'^2]] per arm, rel <=
1e-6 (long-double overflow at a rung -> ward typed SKIPPED
there); accumulation of d_j and prefix sums in long double.
LEMMA-A-FAILS iff W-L1 or any evaluable W-L2 breaches.
POLYGON EXPORT per rung: the prefix series margin(m) = S0(m)
- |S2(m)| for all m at x0 = 0: the SIGN census (no delta
needed): #negative prefixes, min margin (raw and relative
margin/(S0+|S2|)), the critical prefix m* (argmin), its
fraction m*/M, the last-added term's 2 th mod 2 pi and
arg(S2) at m* (the pi-resonance alignment question: delta th
= pi doubles to 2 th = 0 -- constructive in S2); the full-sum
margin (the canonical 2x2 statement H_+ - H_- >= 0 at x0).
CONTROLS at kz 9: Epstein (x^2+5y^2, N = floor(e^{2 alpha})
+1) and scramble seed 1 through the same construction -- the
expression must go negative on some prefix (measure where);
required for POLYGON-HOLDS.  CERTIFIED-TAU WARD: every
battery/holdout rung has upstream tau > 0; the frozen
question is whether the polygon holds at ALL prefixes AND at
the full sum -- measured honestly; the implication tau > 0 =>
2x2 polygon is NOT a theorem (typed): a clean negative on a
certified rung is reported as POLYGON-BREAKS with both
readings (decomposition inconsistency vs genuine
non-implication) typed.  HOLONOMY TEST (run first, cheapest
kill; rungs kz {9, 13}): theta(n) := ppc.pruefer_phase of the
PLUS chain (nstar = len(be)-2, the executed discipline) at
x_n = cos(D log n), unwrapped; squares: support events a < b,
c < d (indices, c-block >= a-block start to kill the
(ab|cd)<->(cd|ab) duplicate), all four products with
log(a c), log(a d), log(b c), log(b d) <= max window lag;
deterministic lexicographic enumeration, cap 2000 squares;
holonomy Dth = th(ac) + th(bd) - th(ad) - th(bc) (unwrapped
primary; wrapped-to-(-pi, pi] secondary); metric = median
|Dth|.  BARS (frozen): HOLONOMY-FLAT iff truth median <= 0.5
x min(Epstein, scramble) at BOTH rungs; HOLONOMY-NULL iff
truth median >= 0.8 x min(fakes) at some rung; else
HOLONOMY-PARTIAL.  CARLESON FRAME (report + one exact ward):
the chain ||C_h|| <= 1 <=> G_- <= G_+ (EXACT, proven
upstream: source_contractor_norm) <=> int |P|^2 d nu~_- <=
int |P|^2 d mu~_+ for all P in P_{h-1} (EXACT modulo the
Christoffel bridge, verified 2e-13 upstream) <=> M(mu~_+ -
nu~_-) >= 0 (same statement, moment coordinates); ward at kz
{9, 13}: in the plus-chain orthonormal polynomial basis the
embedding reads lam_max(M_-) <= 1 with M_- = sum_i w~_i^-
p_a(x_i^-) p_b(x_i^-), and lam_max(M_-) == ||C||^2 = 1 -
lam_1(Delta) (softport readout, post-construction); bar rel
1e-2 (chain conditioning budget typed), measured value
reported.  The polygon reduction (prefix positivity of the
canonical Hamiltonians => the embedding) is typed NEEDS
PROOF (Lemma C shape) -- the probe measures its premise.
REGRESSION: ppc.deployed_cells + the 16-cell census at kz 9
must reproduce the executed run's danger share 0.336 +- 0.02.
VERDICT (frozen): LEMMA-A-FAILS (typed) / POLYGON-HOLDS (no
negative true-comb prefix on any battery/holdout rung at x0 =
0, full sums included, AND Epstein/scramble go negative;
+ HOLONOMY-FLAT / -NULL / -PARTIAL typed separately) /
POLYGON-BREAKS (the negative prefixes typed: which rungs,
which m*/M, both readings).  Float64 + long double
accumulation; budgets typed.  NO RH claim; writes nothing;
no .md; no commits."""

BATTERY_MAX_H = 900
HOLDOUTS = (90, 116, 142, 177, 243)
ANCHORS = (9, 12, 13, 26, 40)
HOLONOMY_KZ = (9, 13)
X0_PRIMARY = 0.0
X0_SECONDARY = (-0.5, 0.5)
SQUARE_CAP = 2000
DANGER_SHARE_KZ9 = (0.316, 0.356)
BANNED_IDS = ("zetazero", "nzeros", "primerange", "isprime",
              "primepi", "nextprime", "prevprime")

CHECKS = []
FAILS = []
T0 = time.time()


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok)))
    if not ok:
        FAILS.append(name.split()[0])
    print("  [%s] %s%s" % ("PASS" if ok else "FAIL", name,
                           ("  -- " + detail) if detail else ""),
          flush=True)
    return bool(ok)


def section(title):
    print("\n" + "=" * 74)
    print(title)
    print("=" * 74, flush=True)


def ast_scan(banned):
    src = open(os.path.abspath(__file__), encoding="utf-8").read()
    bad = []
    for node in ast.walk(ast.parse(src)):
        name = None
        if isinstance(node, ast.Name):
            name = node.id
        elif isinstance(node, ast.Attribute):
            name = node.attr
        if name and name.lower() in banned:
            bad.append(name)
    return bad


# ------------------------------------------------ Lemma A machinery
def pruefer_steps(al, be, m0, x0):
    """Per-step Pruefer data of one chain at the single
    reference energy x0: unwrapped th_j and log(R_j^2), j =
    0..len(be)-1, with joint positive renormalization (scale
    tracked in log).  SOURCE ONLY."""
    nb = len(be)
    p_prev, p_cur = 0.0, 1.0 / math.sqrt(m0)
    lsc = 0.0
    th = prev_raw = None
    ths = np.zeros(nb)
    l2 = np.zeros(nb)
    for j in range(nb):
        s = max(abs(p_cur), abs(p_prev), 1.0)
        if s > 1.0:
            p_prev /= s
            p_cur /= s
            lsc += math.log(s)
        p_next = ((x0 - al[j]) * p_cur
                  - (be[j - 1] * p_prev if j > 0 else 0.0)) \
            / be[j]
        u, v = p_cur, be[j] * p_next
        raw = math.atan2(v, u)
        if th is None:
            th = raw
        else:
            inc = raw - prev_raw
            inc = (inc + math.pi) % (2.0 * math.pi) - math.pi
            th = th + inc
        prev_raw = raw
        ths[j] = th
        l2[j] = 2.0 * lsc + math.log(u * u + v * v)
        p_prev, p_cur = p_cur, p_next
    return ths, l2


def raw_longdouble_sums(al, be, m0, x0):
    """Independent raw long-double recursion: (sum p_j^2,
    sum be_j p_j p_{j+1}, sum be_j^2 p_{j+1}^2) over j =
    0..len(be)-1.  Returns None on overflow (typed)."""
    nb = len(be)
    p_prev = np.longdouble(0.0)
    p_cur = np.longdouble(1.0) / np.sqrt(np.longdouble(m0))
    A = B = C = np.longdouble(0.0)
    x = np.longdouble(x0)
    for j in range(nb):
        p_next = ((x - np.longdouble(al[j])) * p_cur
                  - (np.longdouble(be[j - 1]) * p_prev
                     if j > 0 else np.longdouble(0.0))) \
            / np.longdouble(be[j])
        u, v = p_cur, np.longdouble(be[j]) * p_next
        A += u * u
        B += u * v
        C += v * v
        if not (np.isfinite(A) and np.isfinite(C)
                and np.isfinite(p_next)):
            return None
        p_prev, p_cur = p_cur, p_next
    return A, B, C


def arm_chain(b, arm):
    xs, ws, _ = gnu.folded_arm_measure(b, arm)
    m = min(b["h"], len(xs))
    al, be, m0, brk = cdc.stieltjes_chain(xs, ws, m)
    return al, be, m0


def polygon_rung(b, x0):
    """The signed canonical decomposition + prefix polygon of
    one rung at reference x0."""
    alp, bep, m0p = arm_chain(b, +1)
    alm, bem, m0m = arm_chain(b, -1)
    thp, l2p = pruefer_steps(alp, bep, m0p, x0)
    thm, l2m = pruefer_steps(alm, bem, m0m, x0)
    # interleaved prefix order (frozen): plus then minus per j
    n_p, n_m = len(thp), len(thm)
    ths, ds = [], []
    for j in range(max(n_p, n_m)):
        if j < n_p:
            ths.append(thp[j])
            ds.append(np.exp(np.longdouble(l2p[j])))
        if j < n_m:
            ths.append(thm[j])
            ds.append(-np.exp(np.longdouble(l2m[j])))
    ths = np.array(ths, float)
    ds = np.array(ds, dtype=np.longdouble)
    S0 = np.cumsum(ds)
    c2 = np.cumsum(ds * np.cos(2.0 * ths).astype(np.longdouble))
    s2 = np.cumsum(ds * np.sin(2.0 * ths).astype(np.longdouble))
    absS2 = np.sqrt(c2 * c2 + s2 * s2)
    margin = S0 - absS2
    rel = np.asarray(margin / np.maximum(S0 + absS2,
                                         np.longdouble(1e-300)),
                     float)
    mstar = int(np.argmin(np.asarray(margin, float)))
    nneg = int(np.sum(np.asarray(margin, float) < 0.0))
    return dict(ths=ths, ds=ds, margin=margin, rel=rel,
                mstar=mstar, nneg=nneg,
                minmarg=float(margin[mstar]),
                minrel=float(rel[mstar]),
                fullmarg=float(margin[-1]),
                fullrel=float(rel[-1]),
                M=len(ths),
                th_at=float(np.mod(2.0 * ths[mstar],
                                   2.0 * math.pi)),
                argS2=float(math.atan2(float(s2[mstar]),
                                       float(c2[mstar]))),
                chains=(alp, bep, m0p, alm, bem, m0m))


# ------------------------------------------------ holonomy machinery
def comb_support(kz, kind):
    """(n values, chain data, D, umax) of one comb at rung
    kz.  kind in {'truth', 'epstein', 'scramble'}."""
    if kind == "epstein":
        rr9 = core.build_window(kz)
        N_E = int(math.floor(math.exp(2.0 * rr9["alpha"]))) + 1
        lamE = gnu.lambda_eps(N_E)
        nn = np.nonzero(np.abs(lamE) > 1e-12)[0]
        comb = (np.log(nn.astype(float)),
                2.0 * lamE[nn] / np.sqrt(nn.astype(float)))
        b = gnu.build_rung(kz, comb=comb)
        nvals = nn.astype(np.int64)
        uu = comb[0]
    elif kind == "scramble":
        b = gnu.build_rung(kz, scramble_seed=1)
        uu = np.asarray(b["rr"]["uu"], float)
        nvals = np.rint(np.exp(uu)).astype(np.int64)
    else:
        b = gnu.build_rung(kz)
        uu = np.asarray(b["rr"]["uu"], float)
        nvals = np.rint(np.exp(uu)).astype(np.int64)
    return b, nvals, float(np.max(uu))


def enumerate_squares(lu, umax, cap):
    """Deterministic lexicographic squares over sorted event
    logs lu: indices ia < ib, ic < id, ic >= ia, all four
    product-logs <= umax; capped."""
    out = []
    n = len(lu)
    for ia in range(n):
        if 2.0 * lu[ia] > umax:
            break
        for ib in range(ia + 1, n):
            if lu[ia] + lu[ib] > umax:
                break
            for ic in range(ia, n):
                if lu[ib] + lu[ic] > umax:
                    break
                for idd in range(ic + 1, n):
                    if lu[ib] + lu[idd] > umax:
                        break
                    out.append((ia, ib, ic, idd))
                    if len(out) >= cap:
                        return out
    return out


def holonomy(kz, kind):
    """Holonomy distribution of one comb at rung kz."""
    b, nvals, umax = comb_support(kz, kind)
    alp, bep, m0p = arm_chain(b, +1)
    nstar = len(bep) - 2
    lu = np.log(nvals.astype(float))
    o = np.argsort(lu)
    lu = lu[o]
    sq = enumerate_squares(lu, umax, SQUARE_CAP)
    if not sq:
        return None
    prods = set()
    for ia, ib, ic, idd in sq:
        prods |= {(ia, ic), (ia, idd), (ib, ic), (ib, idd)}
    prods = sorted(prods)
    xv = np.cos(b["D"] * np.array([lu[i] + lu[j]
                                   for i, j in prods]))
    th_all, _r, _u, _v = ppc.pruefer_phase(alp, bep, m0p, xv,
                                           nstar)
    idx = {pr: k for k, pr in enumerate(prods)}
    hol = np.array([th_all[idx[(ia, ic)]]
                    + th_all[idx[(ib, idd)]]
                    - th_all[idx[(ia, idd)]]
                    - th_all[idx[(ib, ic)]]
                    for ia, ib, ic, idd in sq])
    holw = np.abs(np.mod(hol + math.pi, 2.0 * math.pi)
                  - math.pi)
    return dict(nsq=len(sq), med=float(np.median(np.abs(hol))),
                q90=float(np.quantile(np.abs(hol), 0.9)),
                medw=float(np.median(holw)))


# ================================================================= main
def main():
    section("PRIME.PHASE.POLYGON.01 (EXPLORATION ONLY)")
    sha = hashlib.sha256(FROZEN_SPEC.encode("utf-8")).hexdigest()
    print("    FROZEN_SPEC SHA-256 = %s" % sha)
    print("    NO RH claim.")
    print("\nS0 -- firewall + regression")
    check("S0.1 AST firewall clean (no zero/prime oracles)",
          not ast_scan(BANNED_IDS))
    r9, err = ppc.rung_readouts(9)
    check("S0.2 [PRUEFER REGRESSION] the executed contract's "
          "16-cell census reproduces at kz 9 (danger share "
          "%.3f in [%.3f, %.3f]; partition %.1e)"
          % (r9["dshare"], *DANGER_SHARE_KZ9, r9["compl"]),
          DANGER_SHARE_KZ9[0] <= r9["dshare"]
          <= DANGER_SHARE_KZ9[1] and r9["compl"] == 0.0)

    # ---------------- S1 Lemma A wards
    section("S1 -- LEMMA A: the canonical rank-one "
            "decomposition + wards")
    rng = np.random.default_rng(0)
    dsy = rng.normal(size=50)
    tsy = rng.uniform(0.0, 2.0 * math.pi, size=50)
    Hd = np.zeros((2, 2))
    for d, t in zip(dsy, tsy):
        uv = np.array([math.cos(t), math.sin(t)])
        Hd += d * np.outer(uv, uv)
    S0s = float(np.sum(dsy))
    S2s = complex(np.sum(dsy * np.exp(2j * tsy)))
    Ht = 0.5 * np.array([[S0s + S2s.real, S2s.imag],
                         [S2s.imag, S0s - S2s.real]])
    ev = np.linalg.eigvalsh(Hd)
    lem = max(float(np.max(np.abs(Hd - Ht))),
              abs(ev[1] - 0.5 * (S0s + abs(S2s))),
              abs(ev[0] - 0.5 * (S0s - abs(S2s))))
    check("W-L1 [LEMMA] identity + eigenvalues on synthetic "
          "(n=50, seed 0): max dev %.1e <= 1e-12" % lem,
          lem <= 1e-12)

    zones = [kz for kz in core.frame_a_zones()
             if kz in HOLDOUTS
             or core.build_window(kz)["h"] <= BATTERY_MAX_H]
    ward_rungs = [kz for kz in zones
                  if kz in ANCHORS or kz in HOLDOUTS]
    wl2_worst, wl2_skipped = 0.0, []
    cache = {}
    for kz in ward_rungs:
        b = gnu.build_rung(kz)
        cache[kz] = b
        pg = polygon_rung(b, X0_PRIMARY)
        alp, bep, m0p, alm, bem, m0m = pg["chains"]
        for arm, (al, be, m0) in (("+", (alp, bep, m0p)),
                                  ("-", (alm, bem, m0m))):
            raw = raw_longdouble_sums(al, be, m0, X0_PRIMARY)
            if raw is None:
                wl2_skipped.append((kz, arm))
                continue
            A, B, C = (float(x) for x in raw)
            ths, l2 = pruefer_steps(al, be, m0, X0_PRIMARY)
            dd = np.exp(np.asarray(l2, dtype=np.longdouble))
            S0 = float(np.sum(dd))
            c2 = float(np.sum(dd * np.cos(2 * ths)))
            s2 = float(np.sum(dd * np.sin(2 * ths)))
            Ht2 = np.array([[0.5 * (S0 + c2), 0.5 * s2],
                            [0.5 * s2, 0.5 * (S0 - c2)]])
            Hd2 = np.array([[A, B], [B, C]])
            rel = float(np.max(np.abs(Ht2 - Hd2))
                        / max(np.max(np.abs(Hd2)), 1e-300))
            wl2_worst = max(wl2_worst, rel)
    check("W-L2 [ROUND-TRIP] trig assembly == raw long-double "
          "recursion sums on anchors + holdouts, both arms "
          "(worst rel %.1e <= 1e-6%s)"
          % (wl2_worst, "; skipped (overflow): %s"
             % wl2_skipped if wl2_skipped else ""),
          wl2_worst <= 1e-6)
    lemma_ok = lem <= 1e-12 and wl2_worst <= 1e-6

    # ---------------- S2 holonomy (cheapest kill first)
    section("S2 -- THE HOLONOMY TEST (multiplicative "
            "flatness -> phase coherence?)")
    hol_flat, hol_null = True, False
    for kz in HOLONOMY_KZ:
        row = {}
        for kind in ("truth", "epstein", "scramble"):
            row[kind] = holonomy(kz, kind)
        t, e, s = (row[k] for k in ("truth", "epstein",
                                    "scramble"))
        fake_min = min(e["med"], s["med"])
        ratio = t["med"] / max(fake_min, 1e-300)
        hol_flat &= ratio <= 0.5
        hol_null |= ratio >= 0.8
        print("    kz %-3d (%d squares): median |hol| truth "
              "%.4f | Epstein %.4f | scramble %.4f (ratio "
              "truth/min-fake %.2f); q90 truth %.3f; wrapped "
              "medians %.3f/%.3f/%.3f"
              % (kz, t["nsq"], t["med"], e["med"], s["med"],
                 ratio, t["q90"], t["medw"], e["medw"],
                 s["medw"]))
    hol_verdict = ("HOLONOMY-FLAT" if hol_flat else
                   ("HOLONOMY-NULL" if hol_null
                    else "HOLONOMY-PARTIAL"))
    print("    holonomy verdict (frozen bars 0.5/0.8): %s"
          % hol_verdict)

    # ---------------- S3 the polygon export
    section("S3 -- THE POLYGON EXPORT (S0 >= |S2| on all "
            "prefixes; x0 = 0 primary)")
    print("    kz    h    M     #neg  min-rel     m*/M   "
          "2th(m*)/pi argS2/pi  full-rel    sec(-1/2,+1/2)")
    rows = []
    for kz in zones:
        b = cache.get(kz) or gnu.build_rung(kz)
        pg = polygon_rung(b, X0_PRIMARY)
        secs = []
        for x0 in X0_SECONDARY:
            pgs = polygon_rung(b, x0)
            secs.append(pgs["minrel"])
        rows.append((kz, b["h"], pg, secs))
        print("    %-5d %-4d %-5d %-5d %+.2e  %.3f  %.2f"
              "       %+.2f     %+.2e  %+.1e/%+.1e"
              % (kz, b["h"], pg["M"], pg["nneg"],
                 pg["minrel"], pg["mstar"] / pg["M"],
                 pg["th_at"] / math.pi,
                 pg["argS2"] / math.pi, pg["fullrel"],
                 secs[0], secs[1]), flush=True)
    nneg_tot = sum(pg["nneg"] for _k, _h, pg, _s in rows)
    minrel_all = min(pg["minrel"] for _k, _h, pg, _s in rows)
    worst = min(rows, key=lambda r: r[2]["minrel"])
    poly_true = nneg_tot == 0
    check("S3.1 [THE SIGN] S0 >= |S2| on ALL prefixes of ALL "
          "%d battery+holdout rungs at x0 = 0 (total negative "
          "prefixes: %d; ladder min relative margin %+.2e at "
          "kz %d)" % (len(rows), nneg_tot, minrel_all,
                      worst[0]), poly_true)
    full_ok = all(pg["fullmarg"] >= 0.0
                  for _k, _h, pg, _s in rows)
    check("S3.2 [FULL SUM] the canonical 2x2 statement "
          "H_+ - H_- >= 0 at x0 = 0 on every rung (min full "
          "rel margin %+.2e)"
          % min(pg["fullrel"] for _k, _h, pg, _s in rows),
          full_ok)
    sec_neg = [(kz, s) for kz, _h, _pg, s in rows
               if min(s) < 0.0]
    print("    secondary x0 = -1/2, +1/2: rungs with a "
          "negative prefix: %s"
          % (["kz %d (min rel %+.1e)" % (kz, min(s))
               for kz, s in sec_neg] if sec_neg else "none"))
    # controls
    print("\n    controls at kz 9 (same construction):")
    ctrl_break = True
    b9t = cache.get(9) or gnu.build_rung(9)
    for kind in ("epstein", "scramble"):
        bc, _nv, _um = comb_support(9, kind)
        pgc = polygon_rung(bc, X0_PRIMARY)
        ctrl_break &= pgc["nneg"] > 0
        print("    %-8s: #neg prefixes %d/%d (first at m/M = "
              "%.3f), min rel margin %+.2e, full rel %+.2e"
              % (kind, pgc["nneg"], pgc["M"],
                 (int(np.argmax(np.asarray(pgc["margin"],
                                           float) < 0.0))
                  / pgc["M"]) if pgc["nneg"] else float("nan"),
                 pgc["minrel"], pgc["fullrel"]))
    check("S3.3 [DISCRIMINATION] Epstein and scramble go "
          "negative on some prefix", ctrl_break)

    # critical-prefix map for anchors + holdouts
    print("\n    critical-prefix map (anchors + holdouts):")
    for kz, h, pg, _s in rows:
        if kz not in ANCHORS and kz not in HOLDOUTS:
            continue
        m = np.asarray(pg["margin"], float)
        s0 = np.asarray(np.cumsum(pg["ds"]), float)
        print("    kz %-4d: m* = %d/%d, margin(m*) %+.3e, "
              "S0(m*) %.3e, |S2|/S0 at m* %.6f, 2th(last) = "
              "%.2f pi, arg S2 = %+.2f pi"
              % (kz, pg["mstar"], pg["M"], pg["minmarg"],
                 s0[pg["mstar"]],
                 1.0 - m[pg["mstar"]] / max(s0[pg["mstar"]],
                                            1e-300),
                 pg["th_at"] / math.pi,
                 pg["argS2"] / math.pi))

    # ---------------- S4 the Carleson frame
    section("S4 -- THE PRIME CARLESON FRAME (statement + "
            "exact ward)")
    car_ok = True
    for kz in (9, 13):
        b = cache.get(kz) or gnu.build_rung(kz)
        alp, bep, m0p = arm_chain(b, +1)
        xs, ws, _ = gnu.folded_arm_measure(b, -1)
        h = b["h"]
        # plus-chain orthonormal polys at the minus support
        P = np.zeros((len(xs), h))
        p_prev = np.zeros(len(xs))
        p_cur = np.full(len(xs), 1.0 / math.sqrt(m0p))
        P[:, 0] = p_cur
        for n in range(h - 1):
            p_next = ((xs - alp[n]) * p_cur
                      - (bep[n - 1] * p_prev if n > 0
                         else 0.0)) / bep[n]
            p_prev, p_cur = p_cur, p_next
            P[:, n + 1] = p_cur
        Mm = P.T @ (ws[:, None] * P)
        lmax = float(np.linalg.eigvalsh(Mm)[-1])
        sp = gnu.softport(b)
        c2 = 1.0 - sp["lam1"]
        rel = abs(lmax - c2) / c2
        car_ok &= rel <= 1e-2
        print("    kz %-3d: lam_max(M_-) = %.9f vs ||C||^2 = "
              "1 - lam1 = %.9f (rel %.1e) -- the Carleson "
              "embedding constant IS the contractor norm"
              % (kz, lmax, c2, rel))
    check("S4.1 [CARLESON WARD] lam_max(M_- in plus-poly "
          "basis) == ||C||^2 at kz 9/13 (bar rel 1e-2, "
          "chain-conditioning budget)", car_ok)
    print("""
    THE EQUIVALENCE CHAIN (status of each arrow):
      (i)   ||C_h|| <= 1  <=>  G_- <= G_+          [EXACT;
            proven upstream, source_contractor_norm probe]
      (ii)  G_- <= G_+  <=>  int |P|^2 d nu~_- <=
            int |P|^2 d mu~_+  for all P in P_{h-1} [EXACT
            modulo the Christoffel bridge (2e-13 upstream);
            ward S4.1 above: the embedding constant equals
            ||C||^2 machine-grade]
      (iii) the embedding  <=>  M(mu~_+ - nu~_-) >= 0 on
            P_{h-1}                                 [EXACT;
            same statement in moment coordinates]
      (iv)  prefix positivity of the canonical rank-one
            Hamiltonians (THE POLYGON, this probe) ==> the
            embedding                               [NEEDS
            PROOF -- Lemma C shape; the probe measures the
            premise along the ladder]
    CONTRACT CANDIDATE PRIME.CARLESON.PRIME.01 (next
    promotion round): "For the canonical window family, the
    Krein floor tau_h > 0 is equivalent to the Carleson
    embedding of the negative arm measure into the positive
    arm measure at polynomial degree h-1, with embedding
    constant ||C_h||^2 = 1 - tau_h; the polygon reduction
    S0(m) >= |S2(m)| of the interleaved canonical chains at
    band center [status: measured this probe] would upgrade
    the embedding to a prefix-local scalar inequality on a
    complex exponential sum."  NO RH claim.""")

    # ---------------- V verdict
    section("V -- FROZEN VERDICT + honest consequence")
    if not lemma_ok:
        verdict = "LEMMA-A-FAILS"
    elif poly_true and full_ok and ctrl_break:
        verdict = "POLYGON-HOLDS + %s" % hol_verdict
    else:
        bad = []
        if not poly_true:
            negs = [(kz, pg["nneg"], pg["mstar"], pg["M"])
                    for kz, _h, pg, _s in rows
                    if pg["nneg"] > 0]
            bad.append("negative true-comb prefixes at %s"
                       % negs)
        if not full_ok:
            bad.append("full-sum 2x2 fails somewhere")
        if not ctrl_break:
            bad.append("controls fail to break")
        verdict = "POLYGON-BREAKS (%s) + %s" \
            % ("; ".join(bad), hol_verdict)
    print("\n  VERDICT: %s" % verdict)
    print("""
  HONEST CONSEQUENCE (no RH claim): Lemma A is exact
  machine-grade: the difference of the two source canonical
  systems IS a signed rank-one phase sum, and 2x2 prefix
  positivity IS the scalar polygon inequality S0 >= |S2| --
  positivity of a 2D compression as a statement about a
  complex exponential sum over source phases.  What the
  polygon does NOT give by itself: the full h-dim Loewner
  statement G_- <= G_+ (arrow (iv) needs the Lemma-C-shaped
  proof); tau > 0 does not imply the 2x2 polygon a priori,
  so a negative prefix on a certified rung is a statement
  about the decomposition's alignment, not a contradiction.
  The holonomy verdict types whether multiplicative flatness
  is visible as phase coherence -- the bridge the Cotlar
  route lacked.  EXPLORATION ONLY; nothing here enters
  verification/ or the papers.""")
    npass = sum(1 for _n, ok in CHECKS if ok)
    print("\n  checks: %d/%d passed; elapsed %.1f s%s"
          % (npass, len(CHECKS), time.time() - T0,
             ("; FAILS: %s" % FAILS) if FAILS else ""))
    return 0 if npass == len(CHECKS) else 1


if __name__ == "__main__":
    raise SystemExit(main())
