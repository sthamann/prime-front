#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""v876 -- PRIME.PHASE.POLYGON.01 + PRIME.RESIDUAL.QUADRATURE.01 + PRIME.PI.RESONANCE.ANATOMY.01: THE CARLESON WAVE (the successor campaign of the executed Cotlar contract, 2026-08-08 evening) -- the Prime Carleson chain is made machine-exact, the polygon compression is typed WRONG, the residual quadrature certifies the floor constructively at FULL degree, and the pi-resonance is measured THICK.  STRAND 1, THE POLYGON + THE CARLESON WARD (6/8 with the two frozen-honest FAILs S3.1/S3.2 at exit 1, POLYGON-BREAKS + HOLONOMY-NULL): LEMMA A is exact machine-grade (W-L1 1.6e-15; W-L2 round-trip 2.4e-12) -- the difference of the two source canonical systems IS a signed rank-one phase sum, and 2x2 prefix positivity IS the scalar polygon inequality S0(m) >= |S2(m)| on a complex exponential sum over source phases; but the polygon BREAKS on ALL 47 battery+holdout rungs (negative true-comb prefixes everywhere, critical prefixes at 2 theta ~ 1.5 pi -- the pi-resonance; the frozen FAILs S3.1/S3.2 kept, NOT refit), TYPED: the two-gauge compression is the WRONG compression of the Loewner order -- tau > 0 does not imply the 2x2 polygon, a negative prefix is a statement about the decomposition's alignment, not a contradiction; and the holonomy test returns NULL with INVERTED contrast (truth median >= the fakes': multiplicative flatness is NOT visible as phase coherence in this coordinate).  THE CARLESON WARD (the round's analytic core): lam_max(M_-) == ||C||^2 = 1 - tau at rel 1.5e-13 / 1.3e-15 (kz 9/13) -- arrows (i)-(iii) of the Prime Carleson chain are MACHINE-EXACT: ||C_h|| <= 1 <=> G_- <= G_+ <=> the Carleson embedding int |P|^2 d nu~_- <= int |P|^2 d mu~_+ on P_{h-1} <=> M(mu~_+ - nu~_-) >= 0, with embedding constant ||C_h||^2 = 1 - tau_h; arrow (iv) (prefix positivity => the embedding) is typed NEEDS PROOF (Lemma C shape).  The surviving analytic target is REGISTERED as the contract candidate PRIME.CARLESON.PRIME.01 [O].  TRUNCATION NOTE (v877 audit): the deep-holdout polygon rows kz 142/177/243 are NUMERIC-VOID at complete combs (the raw-longdouble prefix machinery overflows there; neither confirmed nor refuted) -- the battery-driven verdict on the 42+2 in-cap rungs STANDS.  STRAND 2, THE RESIDUAL HORIZON LAW (7/8 with the frozen-honest FAIL S2.1 at exit 1, RESIDUAL-HORIZON-LAW): the difference Jacobi chain (row-scaled Wheeler, monic Chebyshev basis) realizes the positive representing measure rho_h CONSTRUCTIVELY -- with mp escalation past the 53-bit noise wall the horizon k*_eff reaches FULL degree h on all 44 floor-positive rungs (k*/h median 1.000, slope dk*/dh = 0.974, Pearson r_h = 0.998); the h-point Gauss rule of the difference chain IS rho_h, so M(L) >= 0 is certified constructively wherever tau > 0 with complete comb; the three sub-h rungs (0.896-0.993) are EXACTLY the comb-truncated windows kz 142/177/243 -- the stalls detected the truncation correctly (STRENGTHENED by the v877 audit); the residual measure carries a single atom just beyond the pole port (maxnode 1.00000x, 1-2 nodes outside the hull at ~zero weight -- mass beyond the fold x = 1 is REQUIRED: the Radau-anchored localized functional (1-x)L breaks early, k*/h median 0.184, genuine); truth/fake discrimination 7-9x (truth k* = 184 vs Epstein 25 / scramble 21 at kz 9).  HONEST FRAME (typed): existence of a positive representing rho IS equivalent to the target (Hamburger) -- the content is the CONSTRUCTION, its horizon law, and the discrimination; a stall locates the wall in quadrature-moment coordinates, not a statement about the target's truth.  STRAND 3, THE RESONANCE ANATOMY (5/5, RESONANCE-THICK): the resonant set (2 theta^- in [1.4, 1.6] pi, ONE predeclared indicator) is a constant ~1/5 of the minus nodes (frac max 0.223, Spearman vs h -0.09: neither h- nor alpha-grown), the off-resonance margin floor on certified rungs is 0.0000 -- EXCISION GAINS NOTHING, the razor is decided OFF the resonance; the soft direction and the resonance are DISJOINT (overlap 0.000 at 0.0x concentration); the minus-chain blowup IS resonance-concentrated and h-grown but the carrying set is not removable: THE WALL IS PHASE-DISTRIBUTED at this partition resolution.  The alpha-law addendum is CONFOUNDED by comb truncation at kz 177/243 (the Loewner collapse there was the truncation, per v877) -- the certified-rung findings stand.  ONE module from three probes (re-executed verbatim, embedded BYTE-EXACT, ~9 min).  NO RH claim.  Python-only per GATE.WOLFRAM.02.

PROVENANCE: all three probes frozen + SHA-hashed before first run
(FROZEN_SPEC SHA-256 gated below); the residual probe carries its
spec-v1 -> v2 -> v3 supersession history typed verbatim in its docstring
(false-premise synthetic ward; float64 sigma-table underflow; the 53-bit
noise-floor wall shown non-structural by the kz-28 mp reference); the
resonance probe carries the v1.1 premise-census addendum typed (bars
untouched, SHA re-verified); executed 2026-08-08 evening/night,
re-executed verbatim at this promotion in isolated namespaces with the
byte-equality provenance ward vs experiments/tfpt-discovery/.  The probes
import v563_paper2_readouts, gauss_node_unitary_probe, cdcore_probe and
pruefer_compensation_probe (v873) READ-ONLY -- not re-gated here.  The
frozen-honest FAILs (S3.1/S3.2 polygon sign census; S2.1 residual full-
degree decision) are pattern-gated and kept; nothing is refit.  NO RH
claim anywhere.
"""

import contextlib
import io
import os
import re
import sys
import time
import types

_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)

EXPECT_SHA_POLYGON = ("6000986aeb8f360bd049b9c2e7398de18ed21c46"
                      "40b339ce9f41814258cde365")
EXPECT_SHA_RESIDUAL = ("3fad2f12b149ef3776b3b9e6390cbbf56296dac"
                       "509e8c10bbe061564a002ffe1")
EXPECT_SHA_RESONANCE = ("a122fc13adfd615ceb64fde601d4112839801e5"
                        "6dc47b263da0359e41d15164b")

# ------------- frozen probe sources (embedded BYTE-EXACT, raw strings)
_SRC_POLYGON = r'''
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
'''

_SRC_RESIDUAL = r'''
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""residual_quadrature_probe -- PRIME.RESIDUAL.QUADRATURE.01
(EXPLORATION ONLY, experiments/; round 35, the Carleson
strand's ROUTE 2: the positive residual quadrature).

THE IDEA: instead of bounding lam_max(M_-), CONSTRUCT a
positive measure rho_h with int x^k d rho_h = int x^k
d(mu~_+ - nu~_-) for 0 <= k <= 2h-2 -- then M(mu~_+ - nu~_-)
= M(rho_h) >= 0 immediately.  HONEST FRAME (typed): the
existence of a positive representing rho IS equivalent to
the target (Hamburger); the probe's content is whether a
SOURCE-STRUCTURED candidate family (the difference Jacobi
chain via stable modified-moment quadrature) achieves it
with controlled complexity, and where it fails if not.

SPEC v2 (typed): v1 executed and exposed (i) a FALSE PREMISE
in the v1 synthetic ward W-A1 (the v1 difference 2 + cos 3x
- 1 - 0.5 sin 2x goes negative on-grid near x = 0.93 -- the
ward tested an indefinite input, k* = 2 was CORRECT); (ii) a
UNIVERSAL k* ~ 535 wall on every rung with h > 535 that is
pure float underflow (the Wheeler sigma-table decays like
4^{-k} mass; 4^{-536} = 1e-323 = the float64 subnormal
floor), not structure.  v2 fixes: the synthetic minus weight
scaled to 0.3 (1 + 0.5 sin 2x) with an in-ward positivity
assertion of the premise; ROW-SCALED Wheeler (row
max-normalization, log-scale bookkeeping -- exact: alphas
are same-row ratios, betas carry the log-scale increment);
mp reference extended to kz 28 (the first v1-walled rung);
node-hull census at certified depth.  The v1 log is
retained at /tmp/residual_run1.log.

SPEC v3 (typed): v2 executed and established (i) the mp
reference at kz 28 certifies the FULL horizon (615 = h)
while the 53-bit run stalls at 540 -- the residual k* ~ 536
wall is the double-precision NOISE FLOOR, not structure
(platform long double aliases float64 at 53 bits; the
"two-dtype" certification degenerates into a
summation-order probe); (ii) v2's W-A1 failed only because
the depth-60 double-precision tail pushed one node to
1.0011 -- the algorithm itself reproduced moments at
2.8e-16.  v3: W-A1 becomes MP-GRADE (dps 40; the clean
algorithm ward -- double drift is typed by k*_cert
separately); MP ESCALATION pass added: every rung with
k*_cert < h gets the definitive mp dps-60 Wheeler horizon
k*_mp, and the frozen decision is keyed on k*_eff = k*_mp
where escalated else k*_cert.  The v2 log is retained at
/tmp/residual_run2.log.  NO RH claim; writes nothing; v563
+ gauss_node_unitary machinery READ-ONLY.

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/residual_quadrature_probe.py
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

FROZEN_SPEC = """\
PRIME.RESIDUAL.QUADRATURE.01 spec v3 (2026-08-08, frozen
before the v3 run; v1 superseded: false-premise synthetic
ward + float64 sigma-table underflow; v2 superseded: the
53-bit noise-floor wall at k ~ 536 shown non-structural by
the kz-28 mp reference, W-A1 depth-60 double drift; all
typed in the probe docstring).  Machinery read-only:
gnu.build_rung / folded_arm_measure / arm_gauss_system /
gauss_objects / softport / lambda_eps.  Ladder: battery =
frame_a_zones with h <= 900 (42 rungs) + frozen deep
holdouts kz {90, 116, 142, 177, 243}.  TARGET: the
difference functional L = mu~_+ - nu~_- (folded
sin^2-modified arm measures, exact atoms) on P_{2h-2}; M(L)
>= 0 on P_{h-1} is the certified Carleson statement (lam_min
identity, regression W-M1).  PRIMARY ALGORITHM (frozen):
ROW-SCALED Wheeler with the MONIC CHEBYSHEV auxiliary basis
(a_l = 0; b_1 = 1/2, b_l = 1/4): each sigma-row is
max-normalized with the log scale tracked; alpha_k =
sigma'_{k,k+1}/sigma'_{k,k} - sigma'_{k-1,k}/
sigma'_{k-1,k-1} (scale-free), sign beta_k =
sign(sigma'_{k,k}/sigma'_{k-1,k-1}), log|beta_k| adds the
row log-scale increment (mathematically the identity
transformation of the v1 recursion); modified moments nu_l =
2^{1-l} sum_i w_i cos(l th_i), exact trig sums on the atom
angles, l <= 2h-1.  POSITIVITY HORIZON (frozen): k*_raw =
consecutive k with sign beta_k > 0 from k = 0; CERTIFIED
k*_cert additionally requires the float64 and long-double
runs to agree: same sign and |log beta_ld - log beta_64| <=
1e-3 at every counted step (platform long-double width
printed and typed).  k* >= h certifies M(L) >= 0
constructively (the h-point Gauss rule of the difference
chain IS rho_h).  MP ESCALATION (v3, frozen): every rung
with k*_cert < h gets the definitive mpmath dps-60 Wheeler
horizon k*_mp (T_l-recurrence moments, classical unscaled
recursion -- mp exponent range needs no scaling); rungs
where the dps-60 horizon is below h are retried ONCE at dps
120 (precision-vs-structure disambiguation) and k*_mp is
the larger; the decision quantity is k*_eff = k*_mp where
escalated, else k*_cert; the double-precision stable depth
(~536) is typed as the platform noise floor, not part of
the verdict.
WARDS: W-M1 [TAU REGRESSION] lam_min(I - M_-) in the
plus-orthonormal basis == softport lam1 at kz {9, 13}, rel
1e-6; W-M2 [TWO-PATH MOMENTS] trig sums == T_l recurrence
at atoms, anchors {9, 12, 13, 26, 40}, all l <= 2h-1, worst
rel 1e-9; W-A1 [SYNTHETIC, v3, MP-GRADE dps 40] grid x_i =
-0.95 + 0.019 i, i < 100, w_+ = 2 + cos 3x, w_- = 0.3 (1 +
0.5 sin 2x); PREMISE ASSERTED in-ward: min(w_+ - w_-) > 0;
n = 60 in mp arithmetic: all beta > 0, Jacobi eigenvalues
inside the support hull + 1e-10, depth-60 mp Gauss moments
reproduce direct moments rel 1e-25; W-P1 [MP REFERENCE]
mpmath dps 60 Wheeler at kz 9 AND kz 28: mp horizon >=
min(k*_cert, h) (the mp run must never certify LESS than
the double run's certified region); W-C1 [GAUSS RULE]
minus-arm Gauss rule reproduces atom moments at l in {0, 1,
7, 25}, rel 1e-8, anchors.  CONSTRUCTIONS: (a) THE
DIFFERENCE CHAIN, full ladder + holdouts, with the
node-hull census at the certified depth in double
arithmetic (max Gauss node, # nodes with x > 1 + 1e-12 --
does rho_h leak past the pole port?  typed double-grade);
(b) RADAU-ANCHORED: the Wheeler
horizon of the localized functional (1 - x) L (anchor x_R =
+1 = the pole-port fold, typed choice); tests the
support-localization (Hausdorff) half at the fold; (c)
DAMPED-SPLIT (anchors, where gauss_objects succeeds): d_i^2
= Dm_i^2, wg_i = wSm_i 4 sin^2(thm_i/2), sigma_i = wg_i /
d_i^2; L = (mu~_+ - sigma) + (sigma - nu~_-G); second part
explicitly positive iff d_i <= 1 (census); the remainder's
Wheeler horizon is the question.  HORIZON LAW: kz, h, alpha,
k*_raw, k*_cert, k*/h for (a) + (b); least-squares slope,
Pearson r vs h and vs alpha.  ANATOMY at k* < h: beta_{k*},
depth-k* node extremes in theta = arccos x, min Christoffel
weight + its node, hull violations.  DISCRIMINATION at kz 9:
Epstein (x^2 + 5y^2, N = floor(e^{2 alpha}) + 1) and
scramble (seed 1) through (a); frozen bar k*_truth >= 2 x
k*_fake for both (kz 9 is fully double-certified, no
escalation needed there).  VERDICT (frozen, on k*_eff):
RESIDUAL-CHAIN-CERTIFIES iff k*_eff >= h for (a) on EVERY
battery + holdout rung AND the discrimination bar holds;
else RESIDUAL-HORIZON-LAW iff k*_eff/h >= 0.5 everywhere
AND Pearson(k*_eff, h) >= 0.9; else RESIDUAL-STALLS (wall
located: rung set, k*/h census, anatomy, spectral position).
Exact rationals infeasible (atoms are cosines of rational
angles); certified floats = two-dtype agreement + the mp
references (typed: mp validates ALGORITHMIC conditioning;
the source data itself is float64).  NO RH claim; writes
nothing; no .md; no commits."""

BATTERY_MAX_H = 900
HOLDOUTS = (90, 116, 142, 177, 243)
ANCHORS = (9, 12, 13, 26, 40)
MP_RUNGS = (9, 28)
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


# ------------------------------------------------ moments + Wheeler
def cheb_mod_moments(th, w, lmax, dtype=np.longdouble):
    """Modified moments nu_l = sum w cos(l th) 2^{1-l} of the
    MONIC Chebyshev basis, l = 0..lmax, exact trig sums."""
    th = np.asarray(th, float)
    w = np.asarray(w, dtype)
    ll = np.arange(lmax + 1)
    cosm = np.cos(np.outer(ll, th)).astype(dtype)
    nu = cosm @ w
    scale = np.power(dtype(2.0),
                     -(np.maximum(ll, 1) - 1).astype(dtype))
    return nu * scale


def wheeler_cheb_scaled(nu, n, dtype=np.longdouble):
    """ROW-SCALED Wheeler, monic Chebyshev auxiliary basis.
    Rows max-normalized, log scale tracked (exact identity
    rewrite of the classical recursion).  Returns (alpha,
    sgnbeta, logbeta): sign beta_k and log |beta_k|."""
    L = 2 * n
    b_aux = np.zeros(L, dtype=dtype)
    if L > 1:
        b_aux[1] = dtype(0.5)
    if L > 2:
        b_aux[2:] = dtype(0.25)
    nu = np.asarray(nu[:L], dtype=dtype)
    alpha = np.zeros(n, dtype=dtype)
    sgnb = np.zeros(n)
    logb = np.full(n, -np.inf)
    # row 0
    s0 = float(np.max(np.abs(nu)))
    if s0 == 0.0 or not np.isfinite(s0):
        return alpha, sgnb, logb
    sig_prev = np.zeros(L + 1, dtype=dtype)
    sig_cur = np.zeros(L + 1, dtype=dtype)
    sig_cur[:L] = nu / dtype(s0)
    ls_cur = math.log(s0)
    alpha[0] = sig_cur[1] / sig_cur[0]
    sgnb[0] = float(np.sign(sig_cur[0]))
    logb[0] = math.log(abs(float(sig_cur[0]))) + ls_cur
    # bt_scaled_{k-1} = beta_{k-1} * S_prev / S_cur (the
    # coefficient the scaled recursion needs)
    bt_scaled = dtype(0.0)
    for k in range(1, n):
        sig_new = np.zeros(L + 1, dtype=dtype)
        lo, hi = k, 2 * n - k
        sig_new[lo:hi] = (sig_cur[lo + 1:hi + 1]
                          - alpha[k - 1] * sig_cur[lo:hi]
                          - bt_scaled * sig_prev[lo:hi]
                          + b_aux[lo:hi] * sig_cur[lo - 1:hi - 1])
        sn = float(np.max(np.abs(sig_new[lo:hi])))
        if sn == 0.0 or not np.isfinite(sn):
            break
        sig_new[lo:hi] /= dtype(sn)
        ls_new = ls_cur + math.log(sn)
        d_new = float(sig_new[k])
        d_cur = float(sig_cur[k - 1])
        if d_new == 0.0 or d_cur == 0.0 \
                or not (np.isfinite(d_new)
                        and np.isfinite(d_cur)):
            break
        alpha[k] = (sig_new[k + 1] / sig_new[k]
                    - sig_cur[k] / sig_cur[k - 1])
        sgnb[k] = float(np.sign(d_new / d_cur))
        logb[k] = (math.log(abs(d_new / d_cur))
                   + ls_new - ls_cur)
        # the next step needs beta_k * S_{k-1}/S_k, which is
        # exactly the scaled-diagonal ratio (scales cancel)
        bt_scaled = dtype(d_new / d_cur)
        sig_prev, sig_cur = sig_cur, sig_new
        ls_cur = ls_new
    return alpha, sgnb, logb


def horizon(sgn_ld, log_ld, sgn_64, log_64, relbar=1e-3):
    """(k*_raw, k*_cert) from signs + log magnitudes."""
    kraw = kcert = 0
    raw_done = cert_done = False
    for k in range(len(sgn_ld)):
        ok_pos = sgn_ld[k] > 0 and np.isfinite(log_ld[k])
        if not raw_done and ok_pos:
            kraw += 1
        else:
            raw_done = True
        ok_agree = (k < len(sgn_64) and sgn_64[k] > 0
                    and np.isfinite(log_64[k])
                    and abs(log_64[k] - log_ld[k])
                    <= max(relbar, relbar * abs(log_ld[k])))
        if not cert_done and ok_pos and ok_agree:
            kcert += 1
        else:
            cert_done = True
        if raw_done and cert_done:
            break
    return kraw, kcert


def betas_from_logs(sgnb, logb, depth):
    return np.array([sgnb[k] * math.exp(max(min(logb[k],
                                                700.0),
                                            -700.0))
                     for k in range(depth)])


def gauss_from_chain(alpha, sgnb, logb, depth):
    """Gauss nodes/weights of the monic chain at depth."""
    a = np.asarray(alpha[:depth], float)
    b = betas_from_logs(sgnb, logb, depth)
    J = np.diag(a)
    if depth > 1:
        off = np.sqrt(np.maximum(b[1:depth], 0.0))
        J += np.diag(off, 1) + np.diag(off, -1)
    evs, V = np.linalg.eigh(J)
    return evs, b[0] * V[0] ** 2


def diff_atoms(b):
    xp, wp, thp = gnu.folded_arm_measure(b, +1)
    xm, wm, thm = gnu.folded_arm_measure(b, -1)
    return (np.concatenate([thp, thm]),
            np.concatenate([wp, -wm]))


def run_construction(th, w, n, radau=False):
    wl = np.asarray(w, np.longdouble)
    if radau:
        wl = wl * (1.0 - np.cos(np.asarray(th, float))
                   ).astype(np.longdouble)
    nu_ld = cheb_mod_moments(th, wl, 2 * n - 1, np.longdouble)
    nu_64 = cheb_mod_moments(th, wl.astype(np.float64),
                             2 * n - 1, np.float64)
    with np.errstate(all="ignore"):
        al_ld, sg_ld, lb_ld = wheeler_cheb_scaled(
            nu_ld, n, np.longdouble)
        _al, sg_64, lb_64 = wheeler_cheb_scaled(
            nu_64, n, np.float64)
    kraw, kcert = horizon(sg_ld, lb_ld, sg_64, lb_64)
    return dict(kraw=kraw, kcert=kcert, al=al_ld, sg=sg_ld,
                lb=lb_ld)


def anatomy(res, h):
    ks = res["kraw"]
    if ks >= h:
        return "no breakdown (k* = %d >= h = %d)" % (ks, h)
    bval = (res["sg"][ks] * math.exp(min(res["lb"][ks], 700.0))
            if ks < len(res["sg"]) and np.isfinite(res["lb"][ks])
            else float("nan"))
    if ks < 2:
        return "immediate stall: beta_%d = %+.3e" % (ks, bval)
    nodes, wts = gauss_from_chain(res["al"], res["sg"],
                                  res["lb"], ks)
    thn = np.arccos(np.clip(nodes, -1.0, 1.0))
    imin = int(np.argmin(wts))
    return ("beta_%d = %+.3e; depth-%d nodes theta in "
            "[%.3f, %.3f]; min wt %.1e at theta %.3f; %d "
            "outside hull"
            % (ks, bval, ks, float(np.min(thn)),
               float(np.max(thn)), float(wts[imin]),
               float(thn[imin]),
               int(np.sum(np.abs(nodes) > 1.0 + 1e-9))))


def hull_census(res, depth):
    nodes, _w = gauss_from_chain(res["al"], res["sg"],
                                 res["lb"], depth)
    return (float(np.max(nodes)),
            int(np.sum(nodes > 1.0 + 1e-12)))


def fake_rung(kz, kind):
    if kind == "epstein":
        rr = core.build_window(kz)
        N_E = int(math.floor(math.exp(2.0 * rr["alpha"]))) + 1
        lamE = gnu.lambda_eps(N_E)
        nn = np.nonzero(np.abs(lamE) > 1e-12)[0]
        comb = (np.log(nn.astype(float)),
                2.0 * lamE[nn] / np.sqrt(nn.astype(float)))
        return gnu.build_rung(kz, comb=comb)
    return gnu.build_rung(kz, scramble_seed=1)


def mp_wheeler(xs, ws, n, dps=60):
    """mpmath reference Wheeler (T_l recurrence moments,
    classical unscaled recursion).  Returns (horizon,
    alphas, betas)."""
    import mpmath as mp
    mp.mp.dps = dps
    cs = [mp.mpf(float(x)) for x in xs]
    wf = [mp.mpf(float(x)) for x in ws]
    m_at = len(wf)
    t_prev = [mp.mpf(1)] * m_at
    t_cur = list(cs)
    nu = [mp.fsum(wf), mp.fsum([wf[i] * t_cur[i]
                                for i in range(m_at)])]
    for ll in range(2, 2 * n):
        t_next = [2 * cs[i] * t_cur[i] - t_prev[i]
                  for i in range(m_at)]
        t_prev, t_cur = t_cur, t_next
        nu.append(mp.fsum([wf[i] * t_cur[i]
                           for i in range(m_at)]))
    for ll in range(1, 2 * n):
        nu[ll] = nu[ll] * mp.mpf(2) ** (-(ll - 1))
    baux = [mp.mpf(0), mp.mpf("0.5")] + [mp.mpf("0.25")] \
        * (2 * n - 2)
    sig_prev = [mp.mpf(0)] * (2 * n + 1)
    sig_cur = list(nu) + [mp.mpf(0)]
    almp = [nu[1] / nu[0]]
    kmp = 1 if nu[0] > 0 else 0
    bemp = [nu[0]]
    for k in range(1, n):
        sig_new = [mp.mpf(0)] * (2 * n + 1)
        for ll in range(k, 2 * n - k):
            sig_new[ll] = (sig_cur[ll + 1]
                           - almp[k - 1] * sig_cur[ll]
                           - bemp[k - 1] * sig_prev[ll]
                           + baux[ll] * sig_cur[ll - 1])
        if sig_new[k] == 0 or sig_cur[k - 1] == 0:
            break
        almp.append(sig_new[k + 1] / sig_new[k]
                    - sig_cur[k] / sig_cur[k - 1])
        bemp.append(sig_new[k] / sig_cur[k - 1])
        if bemp[-1] > 0 and kmp == k:
            kmp = k + 1
        sig_prev, sig_cur = sig_cur, sig_new
    return kmp, almp, bemp


def mp_horizon(b, dps=60):
    th, w = diff_atoms(b)
    return mp_wheeler(np.cos(th), w, b["h"], dps)[0]


# ================================================================= main
def main():
    section("PRIME.RESIDUAL.QUADRATURE.01 v3 "
            "(EXPLORATION ONLY)")
    sha = hashlib.sha256(FROZEN_SPEC.encode("utf-8")).hexdigest()
    print("    FROZEN_SPEC SHA-256 = %s" % sha)
    fi = np.finfo(np.longdouble)
    print("    platform long double: %d-bit mantissa eps "
          "%.1e (typed)" % (fi.nmant + 1, fi.eps))
    print("    NO RH claim.  HONEST FRAME: a positive "
          "representing rho EXISTS iff M(L) >= 0 (certified "
          "upstream); the probe measures whether the "
          "source-structured chain CONSTRUCTS it with "
          "controlled degree.")
    print("\nS0 -- firewall + tau regression")
    check("S0.1 AST firewall clean", not ast_scan(BANNED_IDS))
    worst = 0.0
    for kz in (9, 13):
        b = gnu.build_rung(kz)
        xs, ws, _ = gnu.folded_arm_measure(b, -1)
        al, be, m0, steps = gnu.lanczos_chain(
            *gnu.folded_arm_measure(b, +1)[:2], b["h"])
        h = b["h"]
        P = np.zeros((len(xs), h))
        p_prev = np.zeros(len(xs))
        p_cur = np.full(len(xs), 1.0 / math.sqrt(m0))
        P[:, 0] = p_cur
        for nn_ in range(h - 1):
            p_next = ((xs - al[nn_]) * p_cur
                      - (be[nn_ - 1] * p_prev if nn_ > 0
                         else 0.0)) / be[nn_]
            p_prev, p_cur = p_cur, p_next
            P[:, nn_ + 1] = p_cur
        Mm = P.T @ (ws[:, None] * P)
        lmin = float(1.0 - np.linalg.eigvalsh(Mm)[-1])
        lam1 = gnu.softport(b)["lam1"]
        worst = max(worst, abs(lmin - lam1) / lam1)
    check("W-M1 [TAU REGRESSION] lam_min(I - M_-) == softport "
          "lam1 at kz 9/13 (worst rel %.1e <= 1e-6)" % worst,
          worst <= 1e-6)

    # ---------------- S1 algorithm wards
    section("S1 -- WARDS")
    import mpmath as mp
    xg = -0.95 + 0.019 * np.arange(100)
    wp_ = 2.0 + np.cos(3.0 * xg)
    wm_ = 0.3 * (1.0 + 0.5 * np.sin(2.0 * xg))
    prem = float(np.min(wp_ - wm_))
    kmp, almp, bemp = mp_wheeler(
        np.concatenate([xg, xg]),
        np.concatenate([wp_, -wm_]), 60, dps=40)
    mp.mp.dps = 40
    J = mp.zeros(60, 60)
    for i in range(60):
        J[i, i] = almp[i]
        if i > 0:
            ob = mp.sqrt(bemp[i])
            J[i - 1, i] = ob
            J[i, i - 1] = ob
    E, Q = mp.eigsy(J)
    nodes_mp = [E[i] for i in range(60)]
    wts_mp = [bemp[0] * Q[0, i] ** 2 for i in range(60)]
    hull_ok = (min(nodes_mp) >= mp.mpf(float(np.min(xg)))
               - mp.mpf("1e-10")
               and max(nodes_mp) <= mp.mpf(float(np.max(xg)))
               + mp.mpf("1e-10"))
    wa1 = 0.0
    for k in range(20):
        # subtract in mp: the chain saw the two atom lists
        # separately (a float64 pre-subtraction would inject
        # a 1e-16 reference error)
        mdir = (mp.fsum([mp.mpf(float(wp_[i]))
                         * mp.mpf(float(xg[i])) ** k
                         for i in range(100)])
                - mp.fsum([mp.mpf(float(wm_[i]))
                           * mp.mpf(float(xg[i])) ** k
                           for i in range(100)]))
        mq = mp.fsum([wts_mp[i] * nodes_mp[i] ** k
                      for i in range(60)])
        wa1 = max(wa1, float(abs(mq - mdir) / abs(mdir)))
    check("W-A1 [SYNTHETIC v3, MP dps 40] premise min(w+ - "
          "w-) = %.3f > 0; all 60 beta > 0 (k* = %d), mp "
          "nodes inside hull, mp Gauss moments rel %.1e <= "
          "1e-25" % (prem, kmp, wa1),
          prem > 0.0 and kmp == 60 and hull_ok
          and wa1 <= 1e-25)
    wm2 = wc1 = 0.0
    for kz in ANCHORS:
        b = gnu.build_rung(kz)
        th, w = diff_atoms(b)
        n = b["h"]
        nu = cheb_mod_moments(th, w, 2 * n - 1, np.float64)
        x = np.cos(th)
        t_prev = np.ones_like(x)
        t_cur = x.copy()
        acc = [np.sum(w * t_prev), np.sum(w * t_cur)]
        for ll in range(2, 2 * n):
            t_next = 2.0 * x * t_cur - t_prev
            t_prev, t_cur = t_cur, t_next
            acc.append(np.sum(w * t_cur))
        mono = np.array(acc) * np.power(
            2.0, -(np.maximum(np.arange(2 * n), 1) - 1.0))
        wm2 = max(wm2, float(np.max(np.abs(mono - nu))
                             / np.max(np.abs(nu))))
        thmG, wSm, mode = gnu.arm_gauss_system(b, -1)
        wgG = wSm * 4.0 * np.sin(thmG / 2.0) ** 2
        xmG = np.cos(thmG)
        xa, wa, _tha = gnu.folded_arm_measure(b, -1)
        for ll in (0, 1, 7, 25):
            ga = float(np.sum(wgG * xmG ** ll))
            da = float(np.sum(wa * xa ** ll))
            wc1 = max(wc1, abs(ga - da) / max(abs(da), 1e-300))
    check("W-M2 [TWO-PATH MOMENTS] worst rel %.1e <= 1e-9"
          % wm2, wm2 <= 1e-9)
    check("W-C1 [GAUSS RULE] worst rel %.1e <= 1e-8" % wc1,
          wc1 <= 1e-8)

    # ---------------- S2 construction (a) + (b)
    section("S2 -- (a) THE DIFFERENCE CHAIN: horizon law "
            "(row-scaled Wheeler)")
    zones = [kz for kz in core.frame_a_zones()
             if kz in HOLDOUTS
             or core.build_window(kz)["h"] <= BATTERY_MAX_H]
    print("    kz    h     alpha   k*raw  k*cert  k*/h    "
          "maxnode      n>1  radau-k*c  anatomy")
    rows = []
    for kz in zones:
        b = gnu.build_rung(kz)
        th, w = diff_atoms(b)
        n = b["h"]
        ra = run_construction(th, w, n)
        rb = run_construction(th, w, n, radau=True)
        dep = min(ra["kcert"], n)
        mx, nover = hull_census(ra, dep) if dep >= 2 \
            else (float("nan"), 0)
        rows.append((kz, n, b["alpha"], ra, rb, mx, nover))
        print("    %-5d %-5d %-7.3f %-6d %-7d %.3f   "
              "%-12.9f %-4d %-9d %s"
              % (kz, n, b["alpha"], ra["kraw"], ra["kcert"],
                 ra["kcert"] / n, mx, nover, rb["kcert"],
                 anatomy(ra, n) if ra["kraw"] < n else "-"),
              flush=True)
    # W-P1 mp references
    wp1_ok = True
    mpcache = {}
    for kz in MP_RUNGS:
        b = gnu.build_rung(kz)
        kmp = mp_horizon(b, dps=60)
        mpcache[kz] = kmp
        row = rows[[r[0] for r in rows].index(kz)]
        ok = kmp >= min(row[3]["kcert"], b["h"])
        wp1_ok &= ok
        print("    W-P1 kz %d: mp dps-60 horizon %d vs "
              "double %d (h = %d)"
              % (kz, kmp, row[3]["kcert"], b["h"]))
    check("W-P1 [MP REFERENCE] mp horizon >= min(k*_cert, "
          "h) at kz 9 and 28", wp1_ok)

    # MP ESCALATION (frozen): definitive horizons where the
    # double run stalled below h
    print("\n    MP ESCALATION (dps 60, retry dps 120):")
    keff = {}
    for kz, n, _al, ra, _rb, _mx, _no in rows:
        if ra["kcert"] >= n:
            keff[kz] = ra["kcert"]
            continue
        t1 = time.time()
        kmp = mpcache.get(kz)
        if kmp is None:
            kmp = mp_horizon(gnu.build_rung(kz), dps=60)
        if kmp < n:
            kmp = max(kmp, mp_horizon(gnu.build_rung(kz),
                                      dps=120))
        keff[kz] = kmp
        print("    kz %-4d: k*_cert %d -> k*_mp %d / h %d "
              "(%.3f) [%.0f s]"
              % (kz, ra["kcert"], kmp, n, kmp / n,
                 time.time() - t1), flush=True)
    kc = np.array([keff[r[0]] for r in rows], float)
    hh = np.array([r[1] for r in rows], float)
    aa = np.array([r[2] for r in rows], float)
    slope_h = float(np.polyfit(hh, kc, 1)[0])
    r_h = float(np.corrcoef(hh, kc)[0, 1])
    r_a = float(np.corrcoef(aa, kc)[0, 1])
    ratio_min = float(np.min(kc / hh))
    ratio_med = float(np.median(kc / hh))
    print("\n    horizon law (k*_eff): slope dk*/dh = %.3f "
          "(Pearson r_h = %.3f, r_alpha = %.3f); k*/h min "
          "%.3f median %.3f"
          % (slope_h, r_h, r_a, ratio_min, ratio_med))
    certifies = all(keff[r[0]] >= r[1] for r in rows)
    check("S2.1 [THE DECISION] k*_eff >= h on every battery "
          "+ holdout rung (%d/%d rungs certify)"
          % (sum(1 for r in rows if keff[r[0]] >= r[1]),
             len(rows)), certifies)
    radau_kh = [r[4]["kcert"] / r[1] for r in rows]
    print("    (b) Radau-anchored at the pole port: k*/h "
          "min %.3f median %.3f max %.3f -- the localized "
          "functional (1 - x) L breaks EARLY (far below the "
          "noise floor: genuine): a positive representing "
          "measure must carry mass beyond the fold x = 1"
          % (min(radau_kh), float(np.median(radau_kh)),
             max(radau_kh)))

    # ---------------- S3 (c) damped split
    section("S3 -- (c) THE DAMPED SPLIT (T2 structure), "
            "anchors")
    for kz in ANCHORS:
        b = gnu.build_rung(kz)
        go = gnu.gauss_objects(b)
        if go.get("fail"):
            print("    kz %-4d: gauss_objects fail %s -- "
                  "typed skip" % (kz, go["mode"]))
            continue
        d2 = go["Dm"] ** 2
        wg = go["wSm"] * 4.0 * np.sin(go["thm"] / 2.0) ** 2
        nover = int(np.sum(d2 > 1.0 + 1e-12))
        posmass = float(np.sum(wg * (1.0 / d2 - 1.0)))
        thp_, wp2, _ = gnu.folded_arm_measure(b, +1)
        rr = run_construction(
            np.concatenate([thp_, go["thm"]]),
            np.concatenate([wp2, -wg / d2]), b["h"])
        print("    kz %-4d: d>1 census %d/%d (max d^2 "
              "%.6f); positive part mass %+.3e; remainder "
              "k*_cert = %d/%d (%s)"
              % (kz, nover, len(d2), float(np.max(d2)),
                 posmass, rr["kcert"], b["h"],
                 anatomy(rr, b["h"]) if rr["kraw"] < b["h"]
                 else "certifies"), flush=True)

    # ---------------- S4 discrimination
    section("S4 -- DISCRIMINATION at kz 9")
    ktruth = rows[[r[0] for r in rows].index(9)][3]["kcert"]
    contrast_ok = True
    for kind in ("epstein", "scramble"):
        bf = fake_rung(9, kind)
        th, w = diff_atoms(bf)
        rf = run_construction(th, w, bf["h"])
        contrast_ok &= ktruth >= 2 * rf["kcert"]
        print("    %-8s: k*_cert = %d/%d (truth %d); %s"
              % (kind, rf["kcert"], bf["h"], ktruth,
                 anatomy(rf, bf["h"])))
    check("S4.1 [CONTRAST] truth k* >= 2 x fake k* for both "
          "fakes", contrast_ok)

    # ---------------- V verdict
    section("V -- FROZEN VERDICT + honest consequence")
    if certifies and contrast_ok:
        verdict = ("RESIDUAL-CHAIN-CERTIFIES (k*_eff >= h "
                   "on all %d rungs; slope %.3f, r_h %.3f; "
                   "double-precision noise floor ~536 "
                   "typed, mp-escalated)"
                   % (len(rows), slope_h, r_h))
    elif ratio_min >= 0.5 and r_h >= 0.9:
        verdict = ("RESIDUAL-HORIZON-LAW (k*_eff/h in "
                   "[%.3f, 1) median %.3f, slope %.3f, r_h "
                   "%.3f)" % (ratio_min, ratio_med, slope_h,
                              r_h))
    else:
        worst_r = min(rows, key=lambda r: keff[r[0]] / r[1])
        verdict = ("RESIDUAL-STALLS (k*_eff/h min %.3f at "
                   "kz %d; median %.3f; %s)"
                   % (ratio_min, worst_r[0], ratio_med,
                      anatomy(worst_r[3], worst_r[1])))
    print("\n  VERDICT: %s" % verdict)
    print("""
  HONEST CONSEQUENCE (no RH claim): existence of a positive
  representing measure is EQUIVALENT to M(L) >= 0 (certified
  upstream via tau > 0) -- nothing here re-proves that.  The
  probe's content is CONSTRUCTIVE: whether the difference
  Jacobi chain realizes the positive quadrature at full
  degree with controlled conditioning (k* >= h), how the
  horizon scales along the ladder (the law a cofinal theorem
  needs to persist), whether the pole-port Radau
  localization or the T2 damped split moves the horizon, and
  whether the horizon separates truth from fakes.  A stall
  locates the wall in quadrature-moment coordinates -- a
  statement about THIS construction family, not about the
  target's truth.  EXPLORATION ONLY.""")
    npass = sum(1 for _n, ok in CHECKS if ok)
    print("\n  checks: %d/%d passed; elapsed %.1f s%s"
          % (npass, len(CHECKS), time.time() - T0,
             ("; FAILS: %s" % FAILS) if FAILS else ""))
    return 0 if npass == len(CHECKS) else 1


if __name__ == "__main__":
    raise SystemExit(main())
'''

_SRC_RESONANCE = r'''
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""pi_resonance_anatomy_probe -- PRIME.PI.RESONANCE.ANATOMY.01
(EXPLORATION ONLY, experiments/; round 34, after the executed
Pruefer/Cotlar contract + the polygon run + the compensation
split, 2026-08-08 night).

THE QUESTION NOBODY ASKED: three independent runs localized the
critical structure at the pi-resonance (the Cotlar envelope's
second peak at the resonance cells; the polygon breaks at 2
theta ~ 1.5 pi driven by the minus chain's Christoffel blowup;
the compensation's soft direction carries the razor
cancellation) -- but WHO sits at the resonance: which arithmetic
events carry the resonant phase mass, and what law governs the
minus-chain blowup there?

MACHINERY (READ-ONLY): gnu.build_rung / gauss_objects /
folded_arm_measure / softport; ppc.arm_chain / pruefer_phase /
cell_index (the EXECUTED round-34 phase discipline: nstar =
#nodes - 2, wrapped increments); ppg.pruefer_steps (the polygon
step phases at x0 = 0); cdc chain conventions.

THE FROZEN RESONANT SET: a node/bin x is RESONANT iff
2 theta^-(x) mod 2 pi in [1.4 pi, 1.6 pi] with theta^- the
minus-chain Pruefer phase at the executed nstar discipline
(adjacent windows [1.2, 1.4) pi and (1.6, 1.8] pi reported as
the census's shoulders).  Same recipe on the plus side for
frac^+.  Everything downstream (blowup, overlap, excision) uses
this ONE predeclared indicator; no posterior window choice.

VERDICT (frozen): RESONANCE-THIN-SKIN (frac^- <= 0.15 on every
rung incl deep holdouts AND Spearman(frac^-, h) <= 0.3 AND the
off-resonance contraction is uniform: 1 - ||C^G_off|| >= 0.01
everywhere AND the Epstein pathology is NOT confined: its
||C_off|| stays > 1) / RESONANCE-IS-SOFT-DIRECTION (the soft
vector's minus-node mass concentrates on the resonant set:
mean overlap over anchors >= 0.5 with concentration factor
overlap/frac >= 3) / RESONANCE-THICK (neither -- the typed
law).  The two positive verdicts may co-occur (reported
combined).  NO RH claim; writes nothing; no .md; no commits.

ADDENDUM v1.1 (post first run, mechanical typing fix; the
FROZEN_SPEC literal and all bars untouched, SHA re-verified):
the first run surfaced that the deep-alpha holdouts kz 177/243
are PREMISE-COLLAPSE rungs in this machinery (lam1(Delta) =
-134.5/-214.7, inverse-free pencil lam_min(G_+ - G_-) =
-204/-363 with well-conditioned G_+, cond ~1e4 -- genuine, not
numerical).  v1.1 adds the premise census (lam1 sign, negative
-density mass, pencil floor) per rung and evaluates the
off-resonance-margin bar over the CERTIFIED rungs (lam1 > 0):
on collapsed rungs there is no contraction to uniformize, so
they cannot decide the excision bar; their (non-)healing under
excision is typed separately.  The first-run verdict
(RESONANCE-THICK) is unchanged by this refinement.

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/pi_resonance_anatomy_probe.py
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
import pruefer_compensation_probe as ppc       # noqa: E402  (READ-ONLY)
import phase_polygon_probe as ppg              # noqa: E402  (READ-ONLY)

FROZEN_SPEC = """\
PRIME.PI.RESONANCE.ANATOMY.01 spec v1 (2026-08-08, frozen
before run).  Ladder = battery (frame_a_zones, h <= 900)
thinned to every len//8-th rung with anchors {9, 12, 13, 26,
40} forced, PLUS the alpha/h holdout quartet {90, 116} (deep
h ~1430, moderate alpha) vs {177, 243} (moderate h ~1250, deep
alpha).  Resonant window on 2 theta mod 2 pi: PRIMARY [1.4 pi,
1.6 pi]; shoulders [1.2, 1.4) pi and (1.6, 1.8] pi reported.
Phases: ppc.pruefer_phase with the executed discipline (each
arm's own chain at its own Gauss nodes, nstar = #nodes - 2);
node ward eig(J_minus) vs cos(theta_node) <= 1e-8 every rung.
S1 census: frac^-/frac^+ per rung; position = median |x|,
share |x| > 0.9, median tau = th/D and IQR of the resonant
minus nodes; arithmetic identity at anchors + holdouts via
LINEAR density attribution on the folded minus-support bins:
classes {arch, small primes p <= 13 (n in {2,3,5,7,11,13}),
large primes, prime powers p^k k >= 2 (perfect-power test by
integer root, no oracle)}; linearity ward |d_arch + sum
d_class - d| <= 1e-9 max|d|; shares on/off resonance +
enrichment.  S2 blowup: log10 rho(x) = log10 K_-(x,x)/
K_+(x,x) (log-safe rescaled recurrences, each arm's full
chain) at the minus Gauss nodes: median on/off resonance, max
on resonance; ladder trend Spearman(max log rho, alpha) and
(., h); soft overlap ov = sum_{g in R} |v_m(g)|^2 with v_m =
B_-^G G_+^{-1/2} e_soft normalized; DGR2 tie-in at anchors:
enrichment of resonant rows among the pi-cells {7, 8} entries
vs frac^-; polygon-step secondary census at anchors (x0 = 0
minus-chain step phases: step fraction + R^2-mass share in
the window, log-sum-exp).  S3 alpha-vs-h: the quartet
separation -- alpha-phenomenon iff |mean frac(deep-alpha
pair) - mean frac(deep-h pair)| >= 2 x max within-pair spread
with the deep-alpha pair on the larger side iff Spearman(
frac, alpha) > 0 (sign consistency); Spearman(frac, alpha)
vs (frac, h) over ladder + holdouts reported.  S4 excision:
C_off = C^G with resonant minus rows AND resonant plus
columns removed; readouts ||C_off||, margin 1 - ||C_off||,
tau_off = 1 - ||C_off||^2, the split tau_off / tau; bars in
the verdict enum; kz-9 controls (Epstein x^2+5y^2 relation-
level, scramble seed 1) through the SAME recipe: lam1 < 0
AND (gauss-fail typed OR ||C_off|| > 1) -- excision must NOT
heal the fakes.  Regressions: ppc.rung_readouts(9) danger
share in [0.316, 0.356], partition completeness == 0.
Budgets: the stated wards; float64 with log-scale kernel
evaluation.  Verdict enum as header, positives may combine.
NO RH claim; writes nothing."""

ANCHORS = (9, 12, 13, 26, 40)
HOLD_H = (90, 116)      # deep h, moderate alpha
HOLD_A = (177, 243)     # moderate h, deep alpha
HOLDOUTS = HOLD_H + HOLD_A
W2LO, W2HI = 1.4 * math.pi, 1.6 * math.pi
SHOULDERS = ((1.2 * math.pi, 1.4 * math.pi),
             (1.6 * math.pi, 1.8 * math.pi))
SMALL_PRIMES = (2, 3, 5, 7, 11, 13)
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


# ------------------------------------------------ anatomy machinery
def log_kernel_diag(al, be, m0, xs):
    """log K(x, x) = log sum_{n=0}^{len(be)} p_n(x)^2 with
    per-point positive rescaling (log-safe at gap points).
    SOURCE ONLY (chain + evaluation points)."""
    xs = np.asarray(xs, float)
    p_prev = np.zeros_like(xs)
    p_cur = np.full_like(xs, 1.0 / math.sqrt(m0))
    acc = p_cur ** 2
    lsc = np.zeros_like(xs)
    for n in range(len(be)):
        p_next = ((xs - al[n]) * p_cur
                  - (be[n - 1] * p_prev if n > 0 else 0.0)
                  ) / be[n]
        s = np.maximum(np.abs(p_next), 1.0)
        big = s > 1e100
        if np.any(big):
            sc = np.where(big, s, 1.0)
            p_next = p_next / sc
            p_cur = p_cur / sc
            acc = acc / sc ** 2
            lsc = lsc + np.log(sc)
        acc = acc + p_next ** 2
        p_prev, p_cur = p_cur, p_next
    return np.log(acc) + 2.0 * lsc


def res_mask(two_theta):
    d = np.mod(two_theta, 2.0 * math.pi)
    return (d >= W2LO) & (d <= W2HI)


def is_perfect_power(n):
    if n < 4:
        return False
    for k in range(2, int(math.log2(n)) + 1):
        r = int(round(n ** (1.0 / k)))
        for rr in (r - 1, r, r + 1):
            if rr >= 2 and rr ** k == n:
                return True
    return False


def rung_anatomy(kz, **kw):
    """One rung: resonant census + blowup + overlap +
    excision.  The resonant indicator is fixed BEFORE any
    excision readout."""
    b = gnu.build_rung(kz, **kw)
    go = gnu.gauss_objects(b)
    sp = gnu.softport(b)
    if go["fail"]:
        return dict(kz=kz, h=b["h"], alpha=b["alpha"],
                    fail=str(go["mode"]), lam1=sp["lam1"])
    alp, bep, m0p, _ = ppc.arm_chain(b, +1)
    alm, bem, m0m, _ = ppc.arm_chain(b, -1)
    thm, thp = go["thm"], go["thp"]
    xm, xp = np.cos(thm), np.cos(thp)
    nsm, nsp = len(thm) - 2, len(thp) - 2
    phm, _r, _u, _v = ppc.pruefer_phase(alm, bem, m0m, xm, nsm)
    php, _r, _u, _v = ppc.pruefer_phase(alp, bep, m0p, xp, nsp)
    # node ward: minus chain eigenvalues vs Gauss nodes
    nJ = len(alm)
    Jm = np.diag(alm) + np.diag(bem[:nJ - 1], 1) \
        + np.diag(bem[:nJ - 1], -1)
    nodew = float(np.max(np.abs(
        np.sort(np.linalg.eigvalsh(Jm)) - np.sort(xm)))) \
        if nJ == len(xm) else float("nan")
    Rm = res_mask(2.0 * phm)
    Rp = res_mask(2.0 * php)
    fracm = float(np.mean(Rm))
    fracp = float(np.mean(Rp))
    sh = [float(np.mean((np.mod(2.0 * phm, 2 * math.pi) >= a)
                        & (np.mod(2.0 * phm, 2 * math.pi)
                           < bnd))) for a, bnd in SHOULDERS]
    # position of the resonant minus nodes
    if np.any(Rm):
        xr = xm[Rm]
        tr = thm[Rm] / b["D"]
        pos = dict(medx=float(np.median(np.abs(xr))),
                   edge=float(np.mean(np.abs(xr) > 0.9)),
                   medtau=float(np.median(tr)),
                   iqtau=(float(np.quantile(tr, 0.25)),
                          float(np.quantile(tr, 0.75))))
    else:
        pos = None
    # blowup: log10 K_-/K_+ at the minus nodes
    lrho = (log_kernel_diag(alm, bem, m0m, xm)
            - log_kernel_diag(alp, bep, m0p, xm)) / math.log(10)
    med_on = float(np.median(lrho[Rm])) if np.any(Rm) \
        else float("nan")
    med_off = float(np.median(lrho[~Rm])) if np.any(~Rm) \
        else float("nan")
    max_on = float(np.max(lrho[Rm])) if np.any(Rm) \
        else float("nan")
    # soft overlap on the minus nodes
    vm = go["BmG"] @ (b["Rm"] @ sp["esoft"])
    pmass = np.abs(vm) ** 2
    pmass = pmass / max(float(np.sum(pmass)), 1e-300)
    ov = float(np.sum(pmass[Rm]))
    # excision (indicator fixed above)
    CG = go["CG"]
    nC = float(np.linalg.svd(CG, compute_uv=False)[0])
    if np.any(~Rm) and np.any(~Rp):
        Coff = CG[np.ix_(~Rm, ~Rp)]
        nCoff = float(np.linalg.svd(Coff,
                                    compute_uv=False)[0])
    else:
        nCoff = float("nan")
    tau = sp["lam1"]
    tau_off = 1.0 - nCoff ** 2
    # ADDENDUM v1.1 premise census (readout only)
    negm = float(np.sum(np.abs(b["d"][b["d"] < 0.0]))
                 / np.sum(np.abs(b["d"])))
    penc = float(np.linalg.eigvalsh(b["Gp"] - b["Gm"])[0])
    return dict(negm=negm, penc=penc,
                kz=kz, h=b["h"], alpha=b["alpha"], fail=None,
                b=b, go=go, sp=sp, chains=(alp, bep, m0p, alm,
                bem, m0m), phm=phm, php=php, Rm=Rm, Rp=Rp,
                fracm=fracm, fracp=fracp, shoulders=sh,
                pos=pos, med_on=med_on, med_off=med_off,
                max_on=max_on, ov=ov, nC=nC, nCoff=nCoff,
                lam1=tau, tau_off=tau_off, nodew=nodew,
                rminus=len(thm))


def arith_census(r):
    """Linear density attribution on the folded minus-support
    bins: who carries the resonant mass."""
    b = r["b"]
    rr = b["rr"]
    h, M, D, alpha = rr["h"], rr["M"], rr["D"], rr["alpha"]
    uu = np.asarray(rr["uu"], float)
    mm = 2.0 * np.asarray(rr["lam"], float)
    nvals = np.rint(np.exp(uu)).astype(np.int64)
    cls = np.zeros(len(nvals), int)  # 0 small-p 1 large-p 2 pp
    for i, n in enumerate(nvals):
        if is_perfect_power(int(n)):
            cls[i] = 2
        elif int(n) in SMALL_PRIMES:
            cls[i] = 0
        else:
            cls[i] = 1
    d_cls = []
    for c in range(3):
        sel = cls == c
        if not np.any(sel):
            d_cls.append(np.zeros(2 * M - 2))
            continue
        c_at, _ = core.atom_lags_at(alpha, M, uu[sel], mm[sel])
        d_cls.append(gnu.grid_density(c_at))
    d_ar = gnu.grid_density(np.asarray(core.arch_lags(M, D),
                                       float))
    lin = float(np.max(np.abs(d_ar + sum(d_cls) - b["d"]))
                / np.max(np.abs(b["d"])))
    # folded minus-support bins (gnu.folded_arm_measure path)
    L = b["L"]
    mask = b["neg"]
    jj = np.arange(L)[mask]
    th = 2.0 * math.pi * jj / L
    mu = np.abs(b["d"][mask]) / (2.0 * L)
    wt = mu * 4.0 * np.sin(th / 2.0) ** 2
    fold = np.minimum(jj, L - jj)
    uf, inv = np.unique(fold, return_inverse=True)
    wagg = np.zeros(len(uf))
    np.add.at(wagg, inv, wt)
    keep = wagg > 0.0
    thu = 2.0 * math.pi * uf / L
    xs = np.cos(thu[keep])
    # class magnitudes folded onto the same bins
    A = np.zeros((4, len(uf)))
    for c in range(3):
        np.add.at(A[c], inv, np.abs(d_cls[c][jj]))
    np.add.at(A[3], inv, np.abs(d_ar[jj]))
    A = A[:, keep]
    # phases at the bins (minus chain, executed discipline)
    _alp, _bep, _m0p, alm, bem, m0m = r["chains"]
    nsm = r["rminus"] - 2
    phb, _r2, _u2, _v2 = ppc.pruefer_phase(alm, bem, m0m, xs,
                                           nsm)
    Rb = res_mask(2.0 * phb)
    names = ("small-p", "large-p", "p-power", "arch")
    out = {}
    for tag, msk in (("on", Rb), ("off", ~Rb)):
        tot = float(np.sum(A[:, msk]))
        out[tag] = [float(np.sum(A[c][msk]))
                    / max(tot, 1e-300) for c in range(4)]
    out["binfrac"] = float(np.mean(Rb))
    out["lin"] = lin
    out["names"] = names
    return out


# ================================================================= main
def main():
    section("PRIME.PI.RESONANCE.ANATOMY.01 -- who sits at the "
            "pi-resonance (EXPLORATION ONLY)")
    sha = hashlib.sha256(FROZEN_SPEC.encode("utf-8")).hexdigest()
    print("    FROZEN_SPEC SHA-256 = %s" % sha)
    print("    NO RH claim.  Resonant window (frozen): "
          "2 theta in [1.4 pi, 1.6 pi].")
    print("\nS0 -- firewall + regressions")
    check("S0.1 AST firewall clean (no zero/prime oracles)",
          not ast_scan(BANNED_IDS))
    r9c, _err = ppc.rung_readouts(9)
    check("S0.2 [PRUEFER REGRESSION] executed-contract census "
          "reproduces at kz 9 (danger share %.3f in [%.3f, "
          "%.3f]; partition dev %.1e == 0)"
          % (r9c["dshare"], *DANGER_SHARE_KZ9, r9c["compl"]),
          DANGER_SHARE_KZ9[0] <= r9c["dshare"]
          <= DANGER_SHARE_KZ9[1] and r9c["compl"] == 0.0)

    zones = list(core.frame_a_zones())
    battery = [kz for kz in zones if kz not in HOLDOUTS
               and core.build_window(kz)["h"] <= 900]
    step = max(1, len(battery) // 8)
    ladder = sorted(set(battery[::step]) | set(ANCHORS))
    all_rungs = ladder + list(HOLDOUTS)

    # ---------------- S1+S2+S4 ladder pass
    section("S1/S2/S4 -- census, blowup, excision "
            "(%d rungs + %d holdouts)"
            % (len(ladder), len(HOLDOUTS)))
    print("    kz    h    alpha  r-   frac-  frac+  "
          "rho(on)  rho(off) rhomax  ov     ||C||    "
          "||Coff||  marg_off  tau_off/tau")
    rows = {}
    nodew_max = 0.0
    for kz in all_rungs:
        r = rung_anatomy(kz)
        if r["fail"]:
            print("    kz %d: gauss fail (%s) -- typed skip"
                  % (kz, r["fail"]))
            continue
        rows[kz] = r
        nodew_max = max(nodew_max, r["nodew"])
        print("    %-5d %-4d %.2f  %-4d %.3f  %.3f  "
              "%+7.2f  %+7.2f %+7.2f %.3f  %.6f %.6f  "
              "%.4f    %.1e%s"
              % (kz, r["h"], r["alpha"], r["rminus"],
                 r["fracm"], r["fracp"], r["med_on"],
                 r["med_off"], r["max_on"], r["ov"],
                 r["nC"], r["nCoff"], 1.0 - r["nCoff"],
                 r["tau_off"] / max(r["lam1"], 1e-300),
                 "  (holdout)" if kz in HOLDOUTS else ""),
              flush=True)
    check("S1.0 [NODE WARD] minus-chain eigenvalues == Gauss "
          "nodes on every rung (max dev %.1e <= 1e-8)"
          % nodew_max, nodew_max <= 1e-8)
    kzs = [kz for kz in all_rungs if kz in rows]
    fr = np.array([rows[kz]["fracm"] for kz in kzs])
    hh = np.array([float(rows[kz]["h"]) for kz in kzs])
    aa = np.array([rows[kz]["alpha"] for kz in kzs])
    sp_h = ppc.spearman(fr, hh)
    sp_a = ppc.spearman(fr, aa)
    print("    size law (fit-free): frac^- in [%.3f, %.3f]; "
          "Spearman(frac, h) = %+.2f, Spearman(frac, alpha) "
          "= %+.2f; shoulder fractions at kz 9: %s"
          % (float(np.min(fr)), float(np.max(fr)), sp_h,
             sp_a, ["%.3f" % s for s in
                    rows[9]["shoulders"]]))
    for kz in ANCHORS:
        p = rows[kz]["pos"]
        if p is None:
            continue
        print("    kz %-3d position: median |x| %.3f, share "
              "|x|>0.9: %.2f, median tau %.2f (IQR %.2f-"
              "%.2f)" % (kz, p["medx"], p["edge"],
                         p["medtau"], *p["iqtau"]))

    # blowup trend
    mx = np.array([rows[kz]["max_on"] for kz in kzs])
    print("    blowup law: max log10 rho on resonance vs "
          "alpha Spearman %+.2f, vs h %+.2f; on-off median "
          "gap [%.2f, %.2f] dex"
          % (ppc.spearman(mx, aa), ppc.spearman(mx, hh),
             float(np.min([rows[k]["med_on"]
                           - rows[k]["med_off"]
                           for k in kzs])),
             float(np.max([rows[k]["med_on"]
                           - rows[k]["med_off"]
                           for k in kzs]))))

    # ---------------- S1b arithmetic identity
    section("S1b -- the arithmetic identity of the resonant "
            "set (anchors + holdouts)")
    lin_max = 0.0
    for kz in list(ANCHORS) + list(HOLDOUTS):
        if kz not in rows:
            continue
        ac = arith_census(rows[kz])
        lin_max = max(lin_max, ac["lin"])
        enr = [ac["on"][c] / max(ac["off"][c], 1e-300)
               for c in range(4)]
        print("    kz %-4d (bin frac %.3f): ON  %s"
              % (kz, ac["binfrac"],
                 "  ".join("%s %.3f" % (n, v) for n, v in
                           zip(ac["names"], ac["on"]))))
        print("             %s OFF %s | enrichment %s"
              % (" " * 6, "  ".join("%s %.3f" % (n, v)
                                    for n, v in
                                    zip(ac["names"],
                                        ac["off"])),
                 "/".join("%.2f" % e for e in enr)))
    check("S1.1 [LINEARITY WARD] arch + class densities "
          "rebuild d exactly on every census rung (max rel "
          "%.1e <= 1e-9)" % lin_max, lin_max <= 1e-9)

    # ---------------- S2b soft direction + DGR2 + polygon steps
    section("S2b -- soft direction, pi-cells, polygon steps")
    ovs = [rows[kz]["ov"] for kz in ANCHORS]
    cfs = [rows[kz]["ov"] / max(rows[kz]["fracm"], 1e-9)
           for kz in ANCHORS]
    soft_id = (float(np.mean(ovs)) >= 0.5
               and float(np.mean(cfs)) >= 3.0)
    print("    soft overlap ov (anchors): %s (mean %.3f); "
          "concentration ov/frac: %s (mean %.1f)"
          % ("/".join("%.3f" % v for v in ovs),
             float(np.mean(ovs)),
             "/".join("%.1f" % v for v in cfs),
             float(np.mean(cfs))))
    for kz in ANCHORS:
        r = rows[kz]
        dth = r["phm"][:, None] - r["php"][None, :]
        cell = ppc.cell_index(dth)
        pi_cells = (cell == 7) | (cell == 8)
        if np.any(pi_cells):
            rowres = np.broadcast_to(r["Rm"][:, None],
                                     cell.shape)
            share = float(np.sum(rowres & pi_cells)
                          / np.sum(pi_cells))
        else:
            share = float("nan")
        enrich = share / max(r["fracm"], 1e-9)
        # polygon-step census (secondary; x0 = 0)
        _ap, _bp, _mp, alm, bem, m0m = r["chains"]
        ths, l2 = ppg.pruefer_steps(alm, bem, m0m, 0.0)
        stR = res_mask(2.0 * ths)
        shift = float(np.max(l2))
        wgt = np.exp(l2 - shift)
        mass = float(np.sum(wgt[stR]) / np.sum(wgt))
        print("    kz %-3d: resonant rows carry %.3f of the "
              "pi-cell {7,8} entries (baseline %.3f, "
              "enrichment %.2f) | polygon steps: %.3f of "
              "steps, %.3f of R^2 mass in the window"
              % (kz, share, r["fracm"], enrich,
                 float(np.mean(stR)), mass))

    # ---------------- S3 the alpha-vs-h separation
    section("S3 -- the alpha-not-h law on the holdout quartet")
    ok_quart = all(kz in rows for kz in HOLDOUTS)
    if ok_quart:
        fH = [rows[kz]["fracm"] for kz in HOLD_H]
        fA = [rows[kz]["fracm"] for kz in HOLD_A]
        gap = abs(float(np.mean(fA)) - float(np.mean(fH)))
        spread = max(abs(fH[0] - fH[1]), abs(fA[0] - fA[1]))
        sign_ok = ((float(np.mean(fA)) > float(np.mean(fH)))
                   == (sp_a > 0)) or sp_a == 0
        alpha_law = gap >= 2.0 * spread and sign_ok
        print("    deep-h pair (kz %s): frac %s (h %s, alpha "
              "%s)" % (HOLD_H,
                       ["%.3f" % v for v in fH],
                       [rows[k]["h"] for k in HOLD_H],
                       ["%.2f" % rows[k]["alpha"]
                        for k in HOLD_H]))
        print("    deep-alpha pair (kz %s): frac %s (h %s, "
              "alpha %s)" % (HOLD_A,
                             ["%.3f" % v for v in fA],
                             [rows[k]["h"] for k in HOLD_A],
                             ["%.2f" % rows[k]["alpha"]
                              for k in HOLD_A]))
        print("    separation: |mean gap| %.4f vs 2 x "
              "within-pair spread %.4f; sign consistent with "
              "Spearman(frac, alpha) = %+.2f: %s -> "
              "alpha-phenomenon: %s"
              % (gap, 2.0 * spread, sp_a, sign_ok, alpha_law))
        # blowup separation too
        mH = [rows[kz]["max_on"] for kz in HOLD_H]
        mA = [rows[kz]["max_on"] for kz in HOLD_A]
        print("    blowup separation: max log10 rho deep-h "
              "%s vs deep-alpha %s"
              % (["%.1f" % v for v in mH],
                 ["%.1f" % v for v in mA]))
    else:
        alpha_law = False
        print("    quartet incomplete (gauss fails typed "
              "above)")

    # ---------------- S3b ADDENDUM v1.1 premise census
    section("S3b -- ADDENDUM v1.1: the premise census "
            "(certified vs collapsed rungs)")
    cert_kz = [kz for kz in kzs if rows[kz]["lam1"] > 0.0]
    coll_kz = [kz for kz in kzs if rows[kz]["lam1"] <= 0.0]
    for kz in kzs:
        r = rows[kz]
        print("    kz %-4d h %-5d alpha %.2f: lam1 %+.3e "
              "[%s]  neg-mass %.4f  pencil lam_min(G+-G-) "
              "%+.3e" % (kz, r["h"], r["alpha"], r["lam1"],
                         "CERT" if r["lam1"] > 0.0
                         else "COLLAPSED", r["negm"],
                         r["penc"]))
    if coll_kz:
        nm_c = [rows[kz]["negm"] for kz in cert_kz]
        nm_x = [rows[kz]["negm"] for kz in coll_kz]
        print("    collapse anatomy: neg-density mass "
              "certified [%.3f, %.3f] vs collapsed [%.3f, "
              "%.3f]; on collapsed rungs excision does NOT "
              "heal (||C_off||/||C|| = %s) -- the true comb "
              "matches the fakes' signature there"
              % (float(np.min(nm_c)), float(np.max(nm_c)),
                 float(np.min(nm_x)), float(np.max(nm_x)),
                 ["%.4f" % (rows[kz]["nCoff"]
                            / rows[kz]["nC"])
                  for kz in coll_kz]))
        nm_all = np.array([rows[kz]["negm"] for kz in kzs])
        print("    neg-mass law: Spearman(neg-mass, alpha) "
              "= %+.2f, (neg-mass, h) = %+.2f -- the "
              "alpha-law lives at the PREMISE level"
              % (ppc.spearman(nm_all, aa),
                 ppc.spearman(nm_all, hh)))

    # ---------------- S4b controls under excision
    section("S4b -- controls at kz 9: excision must NOT heal "
            "the fakes")
    rr9 = core.build_window(9)
    N_E = int(math.floor(math.exp(2.0 * rr9["alpha"]))) + 1
    lamE = gnu.lambda_eps(N_E)
    nn = np.nonzero(np.abs(lamE) > 1e-12)[0]
    disc_ok = True
    for nmc, kw in (("Epstein", dict(comb=(
            np.log(nn.astype(float)),
            2.0 * lamE[nn] / np.sqrt(nn.astype(float))))),
            ("scramble", dict(scramble_seed=1))):
        rc = rung_anatomy(9, **kw)
        if rc["fail"]:
            ok = rc["lam1"] < 0.0
            disc_ok &= ok
            print("    %-8s: gauss fail (%s), lam1 = %+.3e "
                  "< 0: %s (typed: maximal discrimination)"
                  % (nmc, rc["fail"], rc["lam1"], ok))
            continue
        ok = rc["lam1"] < 0.0 and rc["nCoff"] > 1.0
        disc_ok &= ok
        print("    %-8s: lam1 %+.3e, frac- %.3f, ||C|| "
              "%.4f -> ||C_off|| %.4f (still > 1: %s)"
              % (nmc, rc["lam1"], rc["fracm"], rc["nC"],
                 rc["nCoff"], rc["nCoff"] > 1.0))
    check("S4.1 [DISCRIMINATION] the fakes' pathology is NOT "
          "confined to the resonance (||C_off|| > 1 or "
          "gauss-fail, lam1 < 0 both)", disc_ok)

    # ---------------- V verdict
    section("V -- FROZEN VERDICT + honest consequence")
    frac_ok = bool(np.max(fr) <= 0.15)
    marg = np.array([1.0 - rows[kz]["nCoff"]
                     for kz in cert_kz])
    marg_ok = bool(np.min(marg) >= 0.01)
    thin = (frac_ok and sp_h <= 0.3 and marg_ok and disc_ok)
    names = []
    if thin:
        names.append("RESONANCE-THIN-SKIN")
    if soft_id:
        names.append("RESONANCE-IS-SOFT-DIRECTION")
    verdict = " + ".join(names) if names else "RESONANCE-THICK"
    print("\n  VERDICT: %s   [frac max %.3f (bar 0.15) | "
          "Spearman(frac, h) %+.2f (bar 0.3) | min "
          "off-margin %.4f over %d certified rungs (bar "
          "0.01; collapsed rungs %s typed in S3b) | soft "
          "mean ov %.3f (bar 0.5) x conc %.1f (bar 3) | "
          "discrimination %s | alpha-law %s]"
          % (verdict, float(np.max(fr)), sp_h,
             float(np.min(marg)), len(cert_kz), coll_kz,
             float(np.mean(ovs)),
             float(np.mean(cfs)), disc_ok, alpha_law))
    if thin:
        print("""
  HONEST CONSEQUENCE: THE LOCALIZATION RESULT.  The resonant
  set (2 theta in [1.4 pi, 1.6 pi], the executed Pruefer
  discipline) is a THIN SKIN: at most %.1f%% of the minus
  nodes on every rung including the deep holdouts, with no
  h-growth, and OFF the resonance the contraction is UNIFORM
  with margin >= %.3f -- three to four orders fatter than the
  razor tau.  The entire cofinal problem lives on the
  measured thin set: a phase-aware bound needs to control
  ONLY the resonant skin (whose arithmetic identity and
  blowup law are printed above), while the fakes stay broken
  even off-resonance -- the excision is arithmetic-sensitive,
  not cosmetic.  The cofinal restatement: source tower ->
  Gauss frame -> off-resonance uniform contraction (measured
  margin) + resonant-skin correction (the named remaining
  object, size law typed above).  NO RH claim.""" % (
            100.0 * float(np.max(fr)),
            float(np.min(marg))))
    elif soft_id:
        print("""
  HONEST CONSEQUENCE: THE ANATOMY UNIFICATION.  The soft
  direction's minus-node mass concentrates on the resonant
  set (mean overlap %.2f at concentration %.1fx) -- the
  razor cancellation and the pi-resonance are the SAME
  object seen in two coordinates; but the skin is not thin
  enough (or the off-resonance margin not uniform enough)
  for the excision statement.  The blowup and census laws
  above type where the thickness lives.  NO RH claim."""
              % (float(np.mean(ovs)), float(np.mean(cfs))))
    else:
        print("""
  HONEST CONSEQUENCE (typed): the resonance is THICK -- the
  resonant fraction is a constant ~1/5 of the minus nodes
  (max %.2f, Spearman vs h %+.2f: neither h- nor alpha-
  grown), the off-resonance margin floor on the certified
  rungs is %.4f (excision gains nothing: the razor is
  decided OFF the resonance), and the soft overlap is %.2f
  at %.1fx concentration (the soft direction and the
  resonance are DISJOINT objects).  The minus-chain blowup
  IS resonance-concentrated and grows with h (typed above),
  but the set carrying it is not removable: the wall is
  phase-distributed at this partition resolution.  ADDENDUM
  finding: the alpha-law lives at the PREMISE level -- the
  deep-alpha holdouts collapse the Loewner premise itself
  (S3b), and there excision does not heal the true comb,
  the same signature as the fakes.  NO RH claim.""" % (
            float(np.max(fr)), sp_h, float(np.min(marg)),
            float(np.mean(ovs)), float(np.mean(cfs))))
    npass = sum(1 for _n, ok in CHECKS if ok)
    print("\n[TIME] %.1f min   [CHECKS] %d run, %d failed%s"
          % ((time.time() - T0) / 60.0, len(CHECKS),
             len(FAILS),
             ("  " + ",".join(FAILS)) if FAILS else ""))
    return 0 if npass == len(CHECKS) else 1


if __name__ == "__main__":
    raise SystemExit(main())
'''

# --------------------------------------------------------------- harness
_PF_RE = re.compile(r"^\s*\[(PASS|FAIL)\]\s+(\S+)", re.M)
_VD_RE = re.compile(r"VERDICT[:\]]")
_SHA_RE = re.compile(r"FROZEN_SPEC SHA-256[ :=]+([0-9a-f]{64})")


def _probe_file(name):
    cand = os.path.abspath(os.path.join(
        _HERE, os.pardir, "experiments", "tfpt-discovery", name + ".py"))
    return cand if os.path.isfile(cand) else None


def _census(out):
    marks = _PF_RE.findall(out)
    fails = sorted({tok for st, tok in marks if st == "FAIL"})
    verdict = ""
    for line in out.splitlines():
        if _VD_RE.search(line):
            verdict = line.strip()
    return len(marks), fails, verdict


def _exec_probe(name, src):
    """Execute one embedded frozen probe source BYTE-EXACT in its own
    module namespace, registered under the probe's canonical import name
    (later probes import earlier ones READ-ONLY through sys.modules);
    call its main(); capture and re-emit stdout."""
    if src[:1] == "\n":
        src = src[1:]
    path = _probe_file(name)
    same = None
    if path is not None:
        with open(path, encoding="utf-8") as fh:
            same = (fh.read() == src)
    fname = path or os.path.abspath(__file__)
    mod = types.ModuleType(name)
    mod.__file__ = fname
    sys.modules[name] = mod
    buf = io.StringIO()
    code = 0
    with contextlib.redirect_stdout(buf):
        try:
            exec(compile(src, fname, "exec"), mod.__dict__)
            entry = mod.__dict__.get("main")
            if callable(entry):
                rc = entry()
                code = 0 if rc is None else int(rc)
        except SystemExit as exc:
            code = 0 if exc.code is None else int(exc.code)
        except Exception:
            import traceback
            traceback.print_exc(file=sys.stdout)
            code = 99
    out = buf.getvalue()
    sys.stdout.write(out)
    sys.stdout.flush()
    return out, code, same


def _gate(name, out, code, same, exp_n, exp_fails, exp_verdict, exp_code,
          exp_sha, gates, extra=()):
    n, fails, verdict = _census(out)
    m = _SHA_RE.search(out)
    sha_ok = m is not None and m.group(1) == exp_sha
    ok = (n == exp_n and fails == list(exp_fails)
          and exp_verdict in verdict and code == exp_code
          and same is not False and sha_ok)
    for tag, pat in extra:
        hit = re.search(pat, out) is not None
        ok &= hit
        print("  [%s] EXTRA %s: /%s/" % ("PASS" if hit else "FAIL",
                                         tag, pat), flush=True)
    gates.append(ok)
    prov = ("byte-exact vs experiments source" if same is True else
            "embedded copy (source file not present)" if same is None
            else "SOURCE MISMATCH")
    print("\n[%s] PATTERN GATE %s: %d checks (exp %d) | FAILs %s (exp %s) "
          "| exit %d (exp %d) | spec SHA %s | %s\n      verdict line: %s"
          % ("PASS" if ok else "FAIL", name, n, exp_n,
             ",".join(fails) if fails else "none",
             ",".join(exp_fails) if exp_fails else "none",
             code, exp_code, "ok" if sha_ok else "MISMATCH", prov,
             verdict[:140]), flush=True)
    return ok


_PLAN = (
    ("phase_polygon_probe", _SRC_POLYGON, 8, ("S3.1", "S3.2"),
     "POLYGON-BREAKS", 1, EXPECT_SHA_POLYGON, (
         ("CARLESON-WARD",
          r"\[PASS\] S4\.1 \[CARLESON WARD\] lam_max\(M_- in plus-poly "
          r"basis\) == \|\|C\|\|\^2 at kz 9/13"),
         ("ALL-47-RUNGS-BREAK",
          r"S0 >= \|S2\| on ALL prefixes of ALL 47 battery\+holdout "
          r"rungs"),
         ("HOLONOMY-NULL", r"holonomy verdict \(frozen bars "
                           r"0\.5/0\.8\): HOLONOMY-NULL"),
         ("CONTRACT-CANDIDATE",
          r"CONTRACT CANDIDATE PRIME\.CARLESON\.PRIME\.01"),
     )),
    ("residual_quadrature_probe", _SRC_RESIDUAL, 8, ("S2.1",),
     "RESIDUAL-HORIZON-LAW", 1, EXPECT_SHA_RESIDUAL, (
         ("FULL-DEGREE-44-OF-47",
          r"k\*_eff >= h on every battery \+ holdout rung \(44/47 rungs "
          r"certify\)"),
         ("HORIZON-LAW",
          r"slope dk\*/dh = 0\.97\d \(Pearson r_h = 0\.99\d"),
         ("MEDIAN-FULL", r"k\*/h min 0\.89\d median 1\.000"),
         ("DISCRIMINATION",
          r"\[PASS\] S4\.1 \[CONTRAST\] truth k\* >= 2 x fake k\*"),
     )),
    ("pi_resonance_anatomy_probe", _SRC_RESONANCE, 5, (),
     "RESONANCE-THICK", 0, EXPECT_SHA_RESONANCE, (
         ("THICK-CONSTANT-FIFTH", r"frac max 0\.2\d+ \(bar 0\.15\)"),
         ("SOFT-DISJOINT", r"soft mean ov 0\.0+ \(bar 0\.5\)"),
         ("ALPHA-LAW-CONFOUNDED", r"alpha-law False"),
     )),
)


def run():
    t0 = time.time()
    print("=" * 74)
    print("v876 -- PRIME.PHASE.POLYGON.01 + PRIME.RESIDUAL.QUADRATURE.01 +")
    print("PRIME.PI.RESONANCE.ANATOMY.01 (the Carleson wave: arrows "
          "(i)-(iii) of the")
    print("Prime Carleson chain machine-exact with embedding constant "
          "1 - tau; the")
    print("polygon compression breaks and is typed WRONG; rho_h certified "
          "at full degree")
    print("on all 44 floor-positive rungs; the resonance is THICK; the "
          "frozen-honest")
    print("FAILs kept; NO RH claim)")
    print("=" * 74, flush=True)
    gates = []
    for (name, src, exp_n, exp_fails, exp_verdict, exp_code, exp_sha,
         extra) in _PLAN:
        print("\n" + "-" * 74)
        print("EMBEDDED FROZEN PROBE: %s" % name)
        print("-" * 74, flush=True)
        out, code, same = _exec_probe(name, src)
        _gate(name, out, code, same, exp_n, exp_fails, exp_verdict,
              exp_code, exp_sha, gates, extra)
    ok = all(gates)
    print("\n" + "=" * 74)
    print("v876: %d/%d probe pattern gates passed | runtime %.1f min"
          % (sum(gates), len(gates), (time.time() - t0) / 60.0))
    print("The Carleson embedding statement survives as the registered "
          "analytic target")
    print("PRIME.CARLESON.PRIME.01 [O]; the polygon and holonomy "
          "compressions are closed")
    print("with typed reasons; the residual quadrature is the "
          "constructive certificate")
    print("family with its horizon law measured.  NO RH claim.")
    print("[%s] v876 VERDICT GATE: POLYGON-BREAKS + HOLONOMY-NULL + "
          "RESIDUAL-HORIZON-LAW + RESONANCE-THICK"
          % ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(run())
