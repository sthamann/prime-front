#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""tp_da_probe -- DEVIL'S ADVOCATE vs the THINNING-PERSISTENCE LEMMA

FROZEN SPEC v1 (2026-08-14).  EXPLORATION ONLY.  ADVERSARIAL ROLE.
This probe writes no files, changes no verification module, paper,
ledger, website, manifest or status marker.  It makes NO RH claim in
ANY direction, closes no gate, narrows no gate.

=======================================================================
TARGET
=======================================================================
TPL (thinning-persistence lemma), the surviving statement of rounds
CCCLXXXII-CCCLXXXIII for the Connes extremal family (trig-Galerkin
minimizer of the Weil form on [-a,a], a = log(x)/2, K = ceil(1.25 x
log x)): (i) fixed-band zero counts of E_x equal the true Xi census
eventually; (ii) the Nyquist-excess zeros stay exiled beyond a growing
threshold.  Measured support on record: census (0,30)=3, (0,60)=13,
(0,100)=29 at x = 5,8,13,21; zeros tracking ordinates to 7e-15;
controls separating at ~1e6.  This probe attacks the SUPPORT, not the
lemma's truth value: kill it, convict it circular, or measure exactly
where its instrument is blind.

=======================================================================
THE BRIDGE (measured fact, arbiter Z1T, reused adversarially)
=======================================================================
The unnormalized Galerkin matrix IS the Gram matrix of zero
evaluations:  M[j,k] = sum_{zeros rho} B_j(t_rho) B_k(t_rho)  with
B_j(t) = sin(a(t-om_j))/(t-om_j) + sin(a(t+om_j))/(t+om_j), t_rho =
(rho-1/2)/i.  For the true (all-real) measure this is
2 sum_{gamma>0} B_j B_k(gamma).  Therefore ANY zero measure -- in
particular one with a planted off-line quadruple -- induces an exact
Galerkin matrix through the identity, and the extremal instrument can
be fed counterfactual worlds.  Planted matrices are assembled in mp as
M_true(cell dps, captured from lane 1's own HP builder via an eigsy
spy) plus an EXACT closed-form Gram delta; the unmoved measure and its
tail cancel identically, so no tail model enters any plant.

=======================================================================
ATTACK LINES
=======================================================================
A1 EPISTEMIC CONTENT.  (a) Influence radius: move ONE true ordinate by
   +0.1 at heights 14.1 / 30.4 / 37.6 (in-band), 43.3 (edge+4),
   53.0 / 95.9 / 236.5 (far) at x = 5; measure the (0,30) census
   count, the (0,30) position response resp30, and the full response.
   F-A1-COUNT-LOCAL: every far mover (height > om_max + 5) leaves the
   (0,30) count unchanged with resp30 < 1e-2, while every in-band
   mover produces a full-band response > 0.05 (transcription).  (b) Audit: compare the recorded census values 3/13/29
   against the SMOOTH Riemann-von Mangoldt count N_s(T) =
   (T/2pi)log(T/2pi) - T/2pi + 7/8 (no zeros, Stirling only); print
   band-edge coverage om_max(x) ~ 2.5 pi x and the cutoff x / dps that
   would be needed to outrun the classical verification height
   HV = 3e12 (literature constant, audit only).
A2 PLANTED WORLDS (priority).  At x = 5 merge the pair (gamma_2,
   gamma_3) and at x = 8 the tight pair (gamma_4, gamma_5) into
   gamma* = midpoint, in three variants: ON(delta) = real pair
   gamma* +- delta (RH-true world), PINCH = real double zero at gamma*
   (RH-true world, delta = 0), OFF(delta) = off-line quadruple
   gamma* +- i delta (RH-false world).  Sweep delta = 0.4, 0.2, 0.1,
   0.05, 0.02, 0.01.  For each planted matrix: bottom eigenpair in mp
   at the cell's frozen dps, complete zero census via the exact
   numerator polynomial in y = z^2 (mp.polyroots), typed
   real/imaginary/complex.  Record per delta:
     rec = (fixed-band census, probe-window real count,
            #complex roots near gamma*),
     ABSORB-FULL(delta):  rec_OFF == rec_BASE (plant invisible),
     MIMIC-PINCH(delta):  rec_OFF == rec_PINCH  AND  max window
                          position |z_OFF - z_PINCH| < POS_SAME = 0.05
                          (off-line-ness invisible: OFF-world
                          indistinguishable from an RH-true world),
     FAITHFUL(delta):     band census == the planted world's own real
                          census (the count a faithful census reader
                          would report),
     plus tau = lam_min sign (does the WALL scalar detect while the
   census does not?), the full real-zero list of each planted cell,
   and the OLS slope of log10 |tau_OFF| vs log10 delta (mechanism
   check: tau_OFF ~ -4 delta^2 E'(gamma*)^2 predicts slope 2 -- the
   census's off-line sensitivity is the wall scalar's sign flip, not
   an independent channel).
A3 CONTROL TRANSCRIPTION.  Feed the SAME instrument four fully known
   synthetic measures at x = 5 through the Gram bridge (worlds
   truncated at G_SYN = 120, declared): TRUE-TRUNC (cache ordinates),
   SMOOTH (zeros of the smooth RvM count, no arithmetic), UNIF
   (uniform comb at density l/2pi, the mesh-family density), SCR
   (golden-jitter 0.35 of the true ordinates).  TRANSCRIBED iff the
   measured (0,30) census equals the world's own census and every
   measured zero in (0,30) sits within 0.5 of a world zero.  Exile
   bookkeeping: #excess == (K-1) - N_world(0, om_max) +- 1 for every
   world ==> the exile is window arithmetic, not prime physics.  Plus
   one SOURCE-built EPSTEIN cell at x = 5 (lane 1's own builder) as
   the arithmetic-world row.
A4 PROOF-SIDE EXISTENCE.  From the MAIN ladder x = 3,5,8,13: OLS
   slopes of log10 tau and log10 gap vs x.  The typed statement is
   printed: what exists source-only vs what is a measured premise
   behind an e^{-Theta(x)} wall (sign of tau; SIMPLICITY gap -- the
   only hypothesis Theorem A consumes; the minimizer direction).
A5 TAU-SCREEN OF THE ESCAPE.  Screened quantities per rung x = 5, 8,
   13: m_edge = om_max - (last matched ordinate), m_b30 = min distance
   of any zero to the band boundary 30, disp = mean |z_i - gamma_i|
   over the matched prefix (matched: |z_i - gamma_i| < 0.4 local gap).
   OLS slope of log10(quantity) vs log10 |tau|; atlas bands PASS
   |s| <= 0.30, RELOCATION s >= 0.70.

=======================================================================
FROZEN LADDERS, BARS, INSTRUMENTS
=======================================================================
 X_MAIN = (3, 5, 8, 13), dps = (45, 60, 80, 120) (lane 1's frozen HP
 ladder; x = 21 NOT rebuilt -- its census is cited from the arbiter
 record, and every structural attack here is x-uniform).
 KFAC = 1.25.  PLANT pairs: x=5 -> (gamma_2, gamma_3); x=8 ->
 (gamma_4, gamma_5).  DELTAS = (0.4, 0.2, 0.1, 0.05, 0.02, 0.01);
 SMALL = (0.05, 0.02, 0.01).  WINDOW_PAD = 3.0.  BANDS: x=5 (0,30);
 x=8 (0,30) and (0,60).  POS_SAME = 0.05.  G_SYN = 120 (A3 worlds
 truncated there; DECLARED subsampling -- B_j tails beyond G_SYN are
 O(1e-3) rank-one-like and identical across worlds).  JIT = 0.35,
 GOLDEN = (sqrt5-1)/2.  INFL_IDX = (0, 3, 5, 7, 10, 27, 99), shift
 +0.1.  Census: exact numerator polynomial in y = z^2 at working dps,
 mp.polyroots maxsteps 600 extraprec 2 dps; complex tolerance
 im_tol = S 10^{-dps/4}; no float64 coefficient path anywhere
 (amendment-A2 pathology avoided by construction).  Eigsy-spy: lane
 1's build_trig_cell_hp is run unmodified; the mp matrix is captured
 at the single mp.eigsy call site and re-diagonalized bit-identically
 (ward W3).  HV_LIT = 3e12.  RUNTIME_BAR = 2400 s.
 --smoke: X_MAIN = (3,5), plant x = 5 only, DELTAS = (0.4, 0.05),
 2 worlds, no EPSTEIN, no screens; NOT verdict-bearing.

=======================================================================
GATES (instrument-only; findings select the branch)
=======================================================================
 W1 AST firewall (no zeta/zero oracle; cache name only in ward_/
    target_/main).
 W2 zero cache health (X5-typed, read-only).
 W3 eigsy-spy capture: mp matrix K x K, re-diagonalization reproduces
    the cell's tau to rel 1e-8 and cn to 1e-20.
 W4 census cross-ward at x = 5 and x = 8: this probe's mp census ==
    lane 1's hp_zero_data census (count equal, 0 complex, max |dz| <
    1e-6 on zeros below om_max, < 1e-3 beyond -- lane 1 refines far
    zeros on the float64 profile whose noise floor the smoke measured
    at 2e-6; this probe's pure-mp polynomial roots are exact).
 W5 plant-delta sanity: OFF(1e-9) == PINCH == ON(1e-9) entrywise to
    1e-12; deltas exactly symmetric.
 W6 mp.polyroots succeeds on every planted/synthetic cell.
 W7 Gram worlds PSD: tau_syn >= -10^{-dps/3}.
 W8 runtime <= RUNTIME_BAR.

=======================================================================
COMPOSITE VERDICT (frozen; exactly one)
=======================================================================
 TP-DA-INSTRUMENT-EDGE  any gate fails (exit 1).
 TPL-BLIND-AT(delta*)   at the deep plant rung x = 8 every delta in
    SMALL is ABSORB-FULL or MIMIC-PINCH; delta* = largest blind delta
    over the full sweep.  Mechanism recorded if tau_OFF < 0 throughout:
    the extremal mechanism monetizes off-line mass as NEGATIVE form
    value (the wall scalar), not as census deviation -- the band-count
    form of TPL is blind exactly in the RH direction.
 TPL-BROKEN(instrument) not blind, but >= 2 synthetic real worlds fail
    transcription by >= 2 counts, or the ON control census misreads
    its own world at >= 4 of 6 deltas at x = 8.
 TPL-CIRCULAR(typed)    not blind; >= 3 of 4 worlds TRANSCRIBED and
    influence bounded and |N_s - census| < 1 on all three recorded
    bands: detection happens exactly because the instrument
    transcribes its input measure; typed TRANSCRIPTION-TAUTOLOGY +
    EPISTEMIC-EMPTINESS + PRECISION-WALL.
 TPL-RESISTED(report)   otherwise: what was tried, why it held.

SMOKE DISCLOSURE: instruments shaken out on x <= 5 pre-freeze; smoke
numbers not verdict-bearing.

AMENDMENT A-1 (instrument only; found by frozen-run-1's own ward W4;
no plant, world, delta, band or branch rule changed).  Frozen-run-1
measured that lane 1's hp_zero_data REFINEMENT step (bisection on the
float64 trig profile) degrades the exact polynomial roots in the upper
half of the band: at x = 8 the lane zeros above t ~ 50 deviate from
the exact mp numerator roots by 8.8e-5 (t=56.4), 6.8e-4 (t=59.3),
7.6e-3 (t=60.8), 4.9e-2 (t=65.3), and |E_mp| at the lane zeros is
~1e-17 while at this probe's roots it is 1e-27..1e-30: the probe roots
are the sharper instrument, the deviation is lane 1's float64
refinement floor (same pathology class as lane 1's own amendment A2).
W4 bars now: counts equal, 0 complex, max |dz| < 1e-6 on zeros below
0.75 om_max; the deviation profile above is REPORTED, not gated.

AMENDMENT A-2 (instrument only; found by frozen-run-1's own A2 table;
no plant, world, delta, band changed; the BROKEN counting rule is
refined to exclude a measured artifact class).  Frozen-run-1 measured
tau < 0 (~ -1.7e-17) for the PSD-EXACT planted worlds ON and PINCH at
x = 8: the plant deltas subtract the pair with CACHE ordinates
(~1e-13 accurate) while the source-built matrix encodes the TRUE
ordinates, so the mismatch dipole (~1e-13 entries) dwarfs the genuine
cluster (1e-30 at x = 8) and pollutes the census of legitimate
worlds.  This is a REAL property of the construction -- the census
functional is discontinuous at e^{-Theta(x)} input precision, typed
finding F-A4-FLOOR -- but it is an input-precision artifact, not a
world-content misread.  Frozen therefore: FLOOR(x) = max(0, -tau_ON
over the sweep, -tau_PINCH); a world's census read is FLOOR-TYPED iff
its |tau| <= 100 FLOOR; the TPL-BROKEN rule counts only ON misreads
that are NOT floor-typed; at x = 5 the floor is measured ZERO
(tau_ON = +1.6e-16 = tau_BASE class, tau_PINCH = +2.9e-18 >= 0), so
the x = 5 discrimination column is floor-free.  Additionally printed:
E'(gamma*) of the BASE minimizer (mp finite difference) and the
predicted blindness onset delta_blind(x) = sqrt(tau_BASE /
(4 E'(gamma*)^2)) -- the delta below which an off-line plant would sit
inside the true cluster and become invisible -- evaluated on the
ladder and extrapolated to x = 21 with the record tau = 1.25e-93.

NO RH CLAIM.  NO POSITIVITY CLAIM.  EXPLORATION ONLY.
"""

from __future__ import annotations

import argparse
import ast
import hashlib
import math
import os
import sys
import time

import mpmath as mp
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

import semilocal_realroot_limit_probe as lane1  # noqa: E402

# ---------------------------------------------------------------- bars
KFAC = 1.25
X_MAIN = (3, 5, 8, 13)
DPS = {3: 45, 5: 60, 8: 80, 13: 120}
PLANT = {5: (1, 2), 8: (3, 4)}          # 0-based cache indices of pair
DELTAS = (0.4, 0.2, 0.1, 0.05, 0.02, 0.01)
SMALL_DELTAS = (0.05, 0.02, 0.01)
WINDOW_PAD = 3.0
BANDS = {5: (30.0,), 8: (30.0, 60.0)}
POS_SAME = 0.05
G_SYN = 120.0
JIT = 0.35
GOLDEN = (math.sqrt(5.0) - 1.0) / 2.0
INFL_IDX = (0, 3, 5, 7, 10, 27, 99)
INFL_SHIFT = 0.1
INFL_FAR_MARGIN = 5.0
INFL_FAR_BAR = 1e-6
INFL_NEAR_BAR = 0.01
TRANS_POS_BAR = 0.5
SCREEN_X = (5, 8, 13)
TAU_PASS = 0.30
TAU_RELOC = 0.70
HV_LIT = 3.0e12                         # classical verification height
RUNTIME_BAR = 2400.0
GAMMA1_LIT = 14.134725141734693790      # literature constant, ward only

SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
T0_WALL = time.time()
CACHE_N7000 = os.path.join(HERE, "verified_zeros_n7000.npy")

CHECKS: list[tuple[str, bool, str]] = []


def check(name: str, ok: bool, detail: str) -> bool:
    ok = bool(ok)
    CHECKS.append((name, ok, detail))
    print("  [%s] %-52s %s" % ("PASS" if ok else "FAIL", name, detail),
          flush=True)
    return ok


def section(title: str) -> None:
    print("\n" + "-" * 78 + "\n" + title + "\n" + "-" * 78, flush=True)


# ------------------------------------------------------------ firewall
def firewall_audit() -> tuple[bool, str]:
    with open(os.path.abspath(__file__), "r", encoding="utf-8") as fh:
        tree = ast.parse(fh.read())
    bad: list[str] = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Attribute):
            if node.attr.lower() in {"zeta", "zetazero", "zetazeros",
                                     "nzeros", "siegelz", "siegeltheta"}:
                bad.append("attr " + node.attr)
        if isinstance(node, ast.Call):
            fn = node.func
            name = (fn.id if isinstance(fn, ast.Name)
                    else fn.attr if isinstance(fn, ast.Attribute) else "")
            if name.lower() in {"zetazero", "zetazeros", "nzeros",
                                "declared_zeros"}:
                bad.append("call " + name)
    for node in ast.walk(tree):
        if not isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            continue
        cache_ok = node.name.startswith(("ward_", "target_")) \
            or node.name == "main"
        for ch in ast.walk(node):
            if isinstance(ch, ast.Name) and ch.id == "CACHE_N7000" \
                    and not cache_ok:
                bad.append("cache in " + node.name)
    return not bad, "violations: %s" % (bad or "none")


def ward_cache_load() -> np.ndarray:
    return np.asarray(np.load(CACHE_N7000), float)


# --------------------------------------------------------- eigsy spy
def capture_build(x: int, world: str, dps: int) -> dict:
    """Run lane 1's HP builder UNMODIFIED and capture the normalized
    mp Galerkin matrix at its single mp.eigsy call site."""
    box: dict = {}
    orig = mp.eigsy

    def spy(mat, *a, **k):
        box["M"] = mat.copy()
        return orig(mat, *a, **k)

    mp.eigsy = spy
    try:
        cell = lane1.build_trig_cell_hp(x, KFAC, world, dps)
    finally:
        mp.eigsy = orig
    cell["M_mp"] = box.get("M")
    return cell


# ------------------------------------------------ mp Gram machinery
def _bvec(aa, oms, z):
    """[B_j(z)] with B_j(t) = sin(a(t-om))/(t-om) + sin(a(t+om))/(t+om)
    (limit aa at the removable point); z may be mpf or mpc."""
    out = []
    for o in oms:
        d1 = z - o
        d2 = z + o
        v1 = aa if abs(d1) < mp.mpf("1e-30") else mp.sin(aa * d1) / d1
        v2 = aa if abs(d2) < mp.mpf("1e-30") else mp.sin(aa * d2) / d2
        out.append(v1 + v2)
    return out


def _norms(K: int, aa):
    return [mp.sqrt(2 * aa) if k == 0 else mp.sqrt(aa)
            for k in range(K)]


def target_plant_delta(x: int, K: int, dps: int, kind: str,
                       ga: float, gb: float, delta: float):
    """EXACT normalized Gram delta replacing the true on-line pair
    (ga, gb) by: OFF = quadruple gamma* +- i delta; ON = real pair
    gamma* +- delta; PINCH = real double zero at gamma*."""
    with mp.workdps(dps):
        aa = mp.log(x) / 2
        oms = [k * mp.pi / aa for k in range(K)]
        nn = _norms(K, aa)
        gam_a = mp.mpf(ga)
        gam_b = mp.mpf(gb)
        gs = (gam_a + gam_b) / 2
        Ba = _bvec(aa, oms, gam_a)
        Bb = _bvec(aa, oms, gam_b)
        D = mp.zeros(K, K)
        if kind == "OFF":
            Bz = _bvec(aa, oms, mp.mpc(gs, mp.mpf(delta)))
            for i in range(K):
                for j in range(i + 1):
                    v = (4 * mp.re(Bz[i] * Bz[j])
                         - 2 * Ba[i] * Ba[j] - 2 * Bb[i] * Bb[j])
                    D[i, j] = D[j, i] = v / (nn[i] * nn[j])
        elif kind == "ON":
            B1 = _bvec(aa, oms, gs - mp.mpf(delta))
            B2 = _bvec(aa, oms, gs + mp.mpf(delta))
            for i in range(K):
                for j in range(i + 1):
                    v = (2 * B1[i] * B1[j] + 2 * B2[i] * B2[j]
                         - 2 * Ba[i] * Ba[j] - 2 * Bb[i] * Bb[j])
                    D[i, j] = D[j, i] = v / (nn[i] * nn[j])
        elif kind == "PINCH":
            Bg = _bvec(aa, oms, gs)
            for i in range(K):
                for j in range(i + 1):
                    v = (4 * Bg[i] * Bg[j]
                         - 2 * Ba[i] * Ba[j] - 2 * Bb[i] * Bb[j])
                    D[i, j] = D[j, i] = v / (nn[i] * nn[j])
        else:
            raise ValueError(kind)
    return D


def target_move_delta(x: int, K: int, dps: int, g_old: float,
                      shift: float):
    """EXACT normalized Gram delta moving ONE ordinate g_old ->
    g_old + shift (influence-radius instrument)."""
    with mp.workdps(dps):
        aa = mp.log(x) / 2
        oms = [k * mp.pi / aa for k in range(K)]
        nn = _norms(K, aa)
        B0 = _bvec(aa, oms, mp.mpf(g_old))
        B1 = _bvec(aa, oms, mp.mpf(g_old + shift))
        D = mp.zeros(K, K)
        for i in range(K):
            for j in range(i + 1):
                v = 2 * (B1[i] * B1[j] - B0[i] * B0[j])
                D[i, j] = D[j, i] = v / (nn[i] * nn[j])
    return D


def target_gram_tilde(x: int, K: int, dps: int, zlist):
    """Normalized Gram matrix 2 sum_gamma B B^T / (n_i n_j) of a fully
    known FINITE synthetic measure (A3 worlds)."""
    with mp.workdps(dps):
        aa = mp.log(x) / 2
        oms = [k * mp.pi / aa for k in range(K)]
        nn = _norms(K, aa)
        M = mp.zeros(K, K)
        for g in zlist:
            B = _bvec(aa, oms, mp.mpf(float(g)))
            for i in range(K):
                for j in range(i + 1):
                    M[i, j] += 2 * B[i] * B[j]
        for i in range(K):
            for j in range(i + 1):
                v = M[i, j] / (nn[i] * nn[j])
                M[i, j] = v
                M[j, i] = v
    return M


def diag_bottom(Mmp, x: int, K: int, dps: int) -> dict:
    """Bottom eigenpair of a normalized mp Galerkin matrix; returns a
    synthetic cell dict compatible with the census instruments."""
    with mp.workdps(dps):
        E, Q = mp.eigsy(Mmp.copy())
        order = sorted(range(K), key=lambda i: E[i])
        i0, i1 = order[0], order[1]
        tau_mp = E[i0]
        gap_mp = E[i1] - E[i0]
        aa = mp.log(x) / 2
        L2 = 2 * aa
        cvec = [Q[i, i0] for i in range(K)]
        cn_mp = [cvec[i] / (mp.sqrt(L2) if i == 0 else mp.sqrt(aa))
                 for i in range(K)]
        imax = int(np.argmax([abs(float(v)) for v in cn_mp]))
        if float(cn_mp[imax]) < 0:
            cn_mp = [-v for v in cn_mp]
        cn_mp_str = [mp.nstr(v, dps) for v in cn_mp]
        cn = np.array([float(v) for v in cn_mp])
        tau_f = float(tau_mp)
        tau_str = mp.nstr(tau_mp, 6)
        gap_str = mp.nstr(gap_mp, 6)
        a_f = float(aa)
    return {"x": x, "K": K, "a": a_f,
            "om": np.arange(K, dtype=float) * math.pi / a_f,
            "cn": cn, "cn_mp_str": cn_mp_str, "dps": dps,
            "tau": tau_f, "tau_str": tau_str, "gap_str": gap_str}


def target_mp_census(cellS: dict) -> dict:
    """Complete typed zero census of E = sum cn_k B_k at working
    precision via the EXACT numerator polynomial in y = z^2 (lane 1's
    construction, no float64 coefficient path).  Returns real zeros
    (sorted), imaginary-pair count, complex roots z (Re, Im > 0)."""
    with mp.workdps(cellS["dps"]):
        aa = mp.log(cellS["x"]) / 2
        K = cellS["K"]
        b = [(k * mp.pi / aa) ** 2 for k in range(1, K)]
        s_mp = b[-1] + 1
        b = [v / s_mp for v in b]
        cs = [mp.mpf(s) for s in cellS["cn_mp_str"]]

        def pmul(p, q):
            out = [mp.mpf(0)] * (len(p) + len(q) - 1)
            for i, pv in enumerate(p):
                for j, qv in enumerate(q):
                    out[i + j] += pv * qv
            return out

        def padd(p, q):
            if len(p) < len(q):
                p, q = q, p
            out = list(p)
            off = len(p) - len(q)
            for j, qv in enumerate(q):
                out[off + j] += qv
            return out

        def deflate(p, root):
            out = [p[0]]
            for c in p[1:-1]:
                out.append(c + out[-1] * root)
            return out

        prod_all = [mp.mpf(1)]
        for bj in b:
            prod_all = pmul(prod_all, [mp.mpf(1), -bj])
        poly = [2 * cs[0] * c for c in prod_all]
        for i, k in enumerate(range(1, K)):
            q = deflate(prod_all, b[i])
            term = [2 * cs[k] * ((-1) ** k) * c for c in q] \
                + [mp.mpf(0)]
            poly = padd(poly, term)
        try:
            rts = mp.polyroots(poly, maxsteps=600,
                               extraprec=2 * cellS["dps"])
        except Exception:
            try:
                rts = mp.polyroots(poly, maxsteps=1500,
                                   extraprec=3 * cellS["dps"])
            except Exception as exc:
                return {"ok": False, "err": repr(exc)}
        im_tol = s_mp * mp.mpf(10) ** (-(cellS["dps"] // 4))
        real_z: list[float] = []
        n_imag = 0
        cplx: list[complex] = []
        for r in rts:
            y = r * s_mp
            if abs(mp.im(y)) <= im_tol:
                yr = mp.re(y)
                if yr > 0:
                    real_z.append(float(mp.sqrt(yr)))
                else:
                    n_imag += 1
            else:
                z = mp.sqrt(y)
                zz = complex(z)
                if zz.real < 0:
                    zz = -zz
                cplx.append(complex(zz.real, abs(zz.imag)))
    return {"ok": True, "real": np.array(sorted(real_z)),
            "n_imag": n_imag, "cplx": cplx}


# ----------------------------------------------------------- helpers
def band_counts(zs, bands) -> tuple:
    zs = np.asarray(zs, float)
    return tuple(int(np.sum(zs < b)) for b in bands)


def window_zeros(zs, lo: float, hi: float) -> np.ndarray:
    zs = np.asarray(zs, float)
    return zs[(zs > lo) & (zs < hi)]


def max_match_dev(z1, z2) -> float:
    if len(z1) != len(z2):
        return float("inf")
    if len(z1) == 0:
        return 0.0
    return float(np.max(np.abs(np.sort(np.asarray(z1))
                               - np.sort(np.asarray(z2)))))


def n_smooth(T: float) -> float:
    u = T / (2.0 * math.pi)
    return u * math.log(u) - u + 7.0 / 8.0


def smooth_zero_list(g_max: float) -> list[float]:
    """Zeros of the smooth RvM count: N_s(gamma_n) = n - 1/2."""
    out = []
    n = 1
    t = 14.0
    while True:
        tgt = n - 0.5
        for _ in range(80):
            u = t / (2.0 * math.pi)
            f = u * math.log(u) - u + 0.875 - tgt
            fp = math.log(u) / (2.0 * math.pi)
            step = f / fp
            t -= step
            if abs(step) < 1e-12:
                break
        if t > g_max:
            break
        out.append(t)
        n += 1
        t += 3.0
    return out


def eprime_mp(cellS: dict, t0: float) -> float:
    """E'(t0) of a cell's minimizer transform, mp finite difference."""
    with mp.workdps(cellS["dps"]):
        aa = mp.log(cellS["x"]) / 2
        cs = [mp.mpf(s) for s in cellS["cn_mp_str"]]
        oms = [k * mp.pi / aa for k in range(cellS["K"])]

        def ee(t):
            tot = mp.mpf(0)
            for c, o in zip(cs, oms):
                for sg in (1, -1):
                    d = t - sg * o
                    tot += c * (aa if abs(d) < mp.mpf("1e-30")
                                else mp.sin(aa * d) / d)
            return tot

        h = mp.mpf("1e-8")
        return float((ee(mp.mpf(t0) + h) - ee(mp.mpf(t0) - h))
                     / (2 * h))


def ols_slope(xs, ys) -> float:
    xa = np.asarray(xs, float)
    ya = np.asarray(ys, float)
    live = np.isfinite(xa) & np.isfinite(ya)
    if live.sum() < 2:
        return float("nan")
    return float(np.polyfit(xa[live], ya[live], 1)[0])


# ---------------------------------------------------------------- main
def main() -> int:
    global X_MAIN, DELTAS
    ap = argparse.ArgumentParser()
    ap.add_argument("--smoke", action="store_true")
    args = ap.parse_args()
    smoke = bool(args.smoke)
    plant_xs = [5] if smoke else [5, 8]
    if smoke:
        X_MAIN = (3, 5)
        DELTAS = (0.4, 0.05)

    print("=" * 78)
    print("tp_da_probe  DEVIL'S ADVOCATE vs THINNING-PERSISTENCE LEMMA")
    print("FROZEN SPEC_SHA %s%s" % (SPEC_SHA[:16],
          "   *** SMOKE -- NOT VERDICT-BEARING ***" if smoke else ""))
    print("=" * 78)

    # ===================================================== I. WARDS
    section("I. INSTRUMENT WARDS")
    fw_ok, fw_det = firewall_audit()
    check("W1 AST firewall (no zero oracle; cache in ward_/target_/"
          "main)", fw_ok, fw_det)
    gammas = ward_cache_load()
    check("W2 zero cache health (READ-ONLY, X5-typed)",
          len(gammas) >= 5000
          and abs(float(gammas[0]) - GAMMA1_LIT) < 1e-9
          and bool(np.all(np.diff(gammas) > 0)),
          "n=%d gamma_1 dev %.1e top %.4f"
          % (len(gammas), abs(float(gammas[0]) - GAMMA1_LIT),
             float(gammas[-1])))

    cells: dict[int, dict] = {}
    cap_ok = True
    for x in X_MAIN:
        t0 = time.time()
        cell = capture_build(x, "MAIN", DPS[x])
        lane1.hp_zero_data(cell)
        cells[x] = cell
        cap_ok &= (cell["M_mp"] is not None
                   and cell["M_mp"].rows == cell["K"])
        z = cell["zeros"]
        print("    MAIN x=%3d K=%3d dps=%3d tau=%s gap=%s census %d/%d"
              " (0,30)=%d minz=%.6f  %.1fs"
              % (x, cell["K"], DPS[x], cell["tau_str"], cell["gap_str"],
                 len(z), cell["census_expect"], int((z < 30.0).sum()),
                 cell["min_zero"], time.time() - t0), flush=True)
    check("W3a eigsy-spy captured the mp Galerkin matrix on every rung",
          cap_ok, "K x K mp matrices at cell dps for x in %s"
          % (X_MAIN,))
    rep_ok = True
    rep_det = []
    for x in X_MAIN[:2]:
        cs = diag_bottom(cells[x]["M_mp"], x, cells[x]["K"], DPS[x])
        rel = abs(cs["tau"] - cells[x]["tau"]) \
            / max(abs(cells[x]["tau"]), 1e-300)
        cdev = float(np.max(np.abs(cs["cn"] - cells[x]["cn"])))
        rep_ok &= rel < 1e-8 and cdev < 1e-12
        rep_det.append("x=%d tau rel %.1e cn dev %.1e" % (x, rel, cdev))
    check("W3b re-diagonalization reproduces the cell bit-stably",
          rep_ok, "; ".join(rep_det))

    cen_ok = True
    cen_det = []
    for x in [xx for xx in (5, 8) if xx in cells]:
        cs = diag_bottom(cells[x]["M_mp"], x, cells[x]["K"], DPS[x])
        cen = target_mp_census(cs)
        if not cen["ok"]:
            cen_ok = False
            cen_det.append("x=%d polyroots FAILED" % x)
            continue
        om_max = float(cells[x]["om"][-1])
        cut = 0.75 * om_max
        zl = cells[x]["zeros"]
        dev_lo = max_match_dev(cen["real"][cen["real"] < cut],
                               zl[zl < cut])
        dev_hi = max_match_dev(cen["real"][cen["real"] >= cut],
                               zl[zl >= cut])
        cen_ok &= (len(cen["real"]) == len(zl)
                   and dev_lo < 1e-6 and len(cen["cplx"]) == 0)
        cen_det.append("x=%d n=%d dev(<%.0f) %.1e cplx %d [dev(>=%.0f)"
                       " %.1e = lane's float64 refinement floor,"
                       " reported, amendment A-1]"
                       % (x, len(cen["real"]), cut, dev_lo,
                          len(cen["cplx"]), cut, dev_hi))
    check("W4 census cross-ward: probe census == lane-1 census"
          " (A-1 bars)", cen_ok, "; ".join(cen_det))

    xw = 5
    ia, ib = PLANT[xw]
    ga, gb = float(gammas[ia]), float(gammas[ib])
    d_off = target_plant_delta(xw, cells[xw]["K"], DPS[xw], "OFF",
                               ga, gb, 1e-9)
    d_on = target_plant_delta(xw, cells[xw]["K"], DPS[xw], "ON",
                              ga, gb, 1e-9)
    d_pin = target_plant_delta(xw, cells[xw]["K"], DPS[xw], "PINCH",
                               ga, gb, 0.0)
    wd = 0.0
    K5 = cells[xw]["K"]
    for i in range(K5):
        for j in range(K5):
            wd = max(wd, abs(float(d_off[i, j] - d_pin[i, j])),
                     abs(float(d_on[i, j] - d_pin[i, j])))
    check("W5 plant deltas: OFF(1e-9) == ON(1e-9) == PINCH entrywise",
          wd < 1e-12, "max dev %.2e (bar 1e-12)" % wd)

    poly_fail: list[str] = []

    def census_of(tag: str, cellS: dict) -> dict:
        cen = target_mp_census(cellS)
        if not cen["ok"]:
            poly_fail.append(tag)
        return cen

    # ================================================ II. A1 INFLUENCE
    section("II. A1 -- EPISTEMIC CONTENT: influence radius + audit")
    xw = 5
    base_z5 = cells[5]["zeros"]
    om_max5 = float(cells[5]["om"][-1])
    print("  x=5: om_max = %.4f, K-1 = %d forced zeros, BASE zeros:"
          % (om_max5, cells[5]["K"] - 1))
    print("    %s" % " ".join("%.6f" % v for v in base_z5))
    z30_base = base_z5[base_z5 < 30.0]
    infl_rows = []
    for idx in INFL_IDX:
        gmv = float(gammas[idx])
        dm = target_move_delta(5, cells[5]["K"], DPS[5], gmv,
                               INFL_SHIFT)
        Mp = cells[5]["M_mp"].copy()
        for i in range(cells[5]["K"]):
            for j in range(cells[5]["K"]):
                Mp[i, j] = Mp[i, j] + dm[i, j]
        cS = diag_bottom(Mp, 5, cells[5]["K"], DPS[5])
        cen = census_of("INFL-%d" % idx, cS)
        if not cen["ok"]:
            continue
        resp_all = max_match_dev(cen["real"], base_z5)
        resp30 = max_match_dev(cen["real"][cen["real"] < 30.0],
                               z30_base)
        dmmax = max(abs(float(dm[i, j]))
                    for i in range(cells[5]["K"])
                    for j in range(cells[5]["K"]))
        c30 = band_counts(cen["real"], (30.0,))[0]
        infl_rows.append((gmv, gmv - om_max5, dmmax, resp_all,
                          resp30, c30, len(cen["cplx"])))
        print("    move gamma=%9.4f (edge%+8.3f) by +%.1f:"
              " ||dM||max %.3e  resp_all %.3e  resp30 %.3e"
              "  (0,30)=%d cplx=%d"
              % (gmv, gmv - om_max5, INFL_SHIFT, dmmax, resp_all,
                 resp30, c30, len(cen["cplx"])))
    near = [r for r in infl_rows if r[0] < om_max5]
    far = [r for r in infl_rows if r[1] > INFL_FAR_MARGIN]
    f_a1_bounded = (all(r[5] == len(z30_base) and r[4] < INFL_NEAR_BAR
                        for r in far)
                    and all(r[3] > 0.05 for r in near)
                    and len(far) >= 2 and len(near) >= 2)
    print("  F-A1-COUNT-LOCAL = %s (far movers: (0,30) count fixed"
          " and resp30 < %.0e; in-band movers: full response > 0.05"
          " -- transcription)"
          % (f_a1_bounded, INFL_NEAR_BAR))

    print("\n  A1 AUDIT -- what the recorded census values contain:")
    xi_census = {T: int((gammas < T).sum()) for T in (30.0, 60.0,
                                                      100.0)}
    f_smooth = True
    for T in (30.0, 60.0, 100.0):
        ns = n_smooth(T)
        dev = abs(ns - xi_census[T])
        f_smooth &= dev < 1.0
        print("    T=%5.0f  Xi census %2d   smooth RvM N_s(T) = %8.4f"
              "   |N_s - census| = %.4f  (S(T) content < 1)"
              % (T, xi_census[T], ns, dev))
    print("    band-edge coverage om_max(x) ~ 2.5 pi x:  %s"
          % "  ".join("x=%d: %.1f" % (x, float(cells[x]["om"][-1]))
                      for x in X_MAIN))
    print("    => the deepest recorded census (x=21, om_max = 163.0)"
          " is a functional of the zero measure below ~168; the cache"
          " itself reaches %.1f (n=%d); classical verification"
          " reaches HV = %.1e."
          % (float(gammas[-1]), len(gammas), HV_LIT))
    x_need = HV_LIT / (2.5 * math.pi)
    dps_need = 4.0 * math.pi * x_need / math.log(10.0)
    print("    to make the band census probe UNVERIFIED heights the"
          " cutoff must reach x ~ %.3e, whose minimizer lives at"
          " internal precision ~e^{-4 pi x} = 10^{-%.3e} (dps %.3e):"
          " no computation.  The instrument cannot outrun the zero"
          " census it is made of." % (x_need, dps_need, dps_need))

    # ================================================ III. A2 PLANTS
    section("III. A2 -- PLANTED OFF-LINE WORLDS (the priority attack)")
    a2: dict[int, dict] = {}
    for x in plant_xs:
        K = cells[x]["K"]
        ia, ib = PLANT[x]
        ga, gb = float(gammas[ia]), float(gammas[ib])
        gstar = 0.5 * (ga + gb)
        wlo, whi = ga - WINDOW_PAD, gb + WINDOW_PAD
        bands = BANDS[x]
        print("  x=%d: plant pair (gamma_%d, gamma_%d) = (%.6f, %.6f),"
              " gamma* = %.6f, window (%.2f, %.2f), bands %s"
              % (x, ia + 1, ib + 1, ga, gb, gstar, wlo, whi,
                 tuple(int(b) for b in bands)))
        true_list = gammas[gammas < 300.0]
        rest = np.array([g for k, g in enumerate(true_list)
                         if k not in (ia, ib)])
        ref = {}
        ref["BASE"] = band_counts(true_list, bands)
        ref["OFF"] = band_counts(rest, bands)
        ref["PINCH"] = band_counts(np.concatenate(
            [rest, [gstar, gstar]]), bands)
        print("    faithful-reader reference censuses: BASE %s"
              "  OFF %s  PINCH %s  ON(delta) == BASE"
              % (ref["BASE"], ref["OFF"], ref["PINCH"]))

        rec_base = (band_counts(cells[x]["zeros"], bands),
                    len(window_zeros(cells[x]["zeros"], wlo, whi)), 0)
        print("    measured BASE: bands %s window %d cplx 0  tau=%s"
              % (rec_base[0], rec_base[1], cells[x]["tau_str"]))

        def planted_cell(kind: str, delta: float) -> tuple[dict, dict]:
            dm = target_plant_delta(x, K, DPS[x], kind, ga, gb, delta)
            Mp = cells[x]["M_mp"].copy()
            for i in range(K):
                for j in range(K):
                    Mp[i, j] = Mp[i, j] + dm[i, j]
            cS = diag_bottom(Mp, x, K, DPS[x])
            cen = census_of("%s-x%d-d%g" % (kind, x, delta), cS)
            return cS, cen

        cp, cen_p = planted_cell("PINCH", 0.0)
        wz_pin = window_zeros(cen_p["real"], wlo, whi) \
            if cen_p["ok"] else np.array([])
        ncx_pin = sum(1 for z in cen_p.get("cplx", [])
                      if abs(z.real - gstar) < WINDOW_PAD)
        rec_pin = ((band_counts(cen_p["real"], bands),
                    len(wz_pin), ncx_pin) if cen_p["ok"] else None)
        print("    PINCH (delta=0): tau=%s gap=%s bands %s window"
              " zeros [%s] cplx-near %d"
              % (cp["tau_str"], cp["gap_str"],
                 rec_pin[0] if rec_pin else "?",
                 " ".join("%.5f" % v for v in wz_pin), ncx_pin))

        rows = []
        print("    %-6s %-4s %13s %8s %8s %6s %9s %9s %s"
              % ("delta", "kind", "tau", "bands", "window", "cplx",
                 "vsPINCH", "vsON", "flags"))
        for delta in DELTAS:
            per = {}
            for kind in ("OFF", "ON"):
                cS, cen = planted_cell(kind, delta)
                if not cen["ok"]:
                    per[kind] = None
                    continue
                wz = window_zeros(cen["real"], wlo, whi)
                ncx = sum(1 for z in cen["cplx"]
                          if abs(z.real - gstar) < WINDOW_PAD)
                per[kind] = {"cell": cS, "cen": cen, "wz": wz,
                             "rec": (band_counts(cen["real"], bands),
                                     len(wz), ncx)}
            if per["OFF"] is None or per["ON"] is None:
                continue
            off, on = per["OFF"], per["ON"]
            d_pinch = max_match_dev(off["wz"], wz_pin)
            d_on = max_match_dev(off["wz"], on["wz"])
            absorb = off["rec"] == rec_base
            mimic = (rec_pin is not None and off["rec"] == rec_pin
                     and d_pinch < POS_SAME)
            faithful = off["rec"][0] == ref["OFF"]
            on_reads_own = on["rec"][0] == ref["BASE"]
            flags = []
            if absorb:
                flags.append("ABSORB-FULL")
            if mimic:
                flags.append("MIMIC-PINCH")
            if faithful:
                flags.append("FAITHFUL")
            if not on_reads_own:
                flags.append("ON-MISREAD")
            rows.append({"delta": delta, "off": off, "on": on,
                         "absorb": absorb, "mimic": mimic,
                         "faithful": faithful,
                         "on_reads_own": on_reads_own,
                         "tau_off": off["cell"]["tau"],
                         "d_pinch": d_pinch, "d_on": d_on})
            for kind in ("OFF", "ON"):
                p = per[kind]
                print("    %-6g %-4s %13s %8s %8d %6d %9s %9s %s"
                      % (delta, kind, p["cell"]["tau_str"],
                         p["rec"][0], p["rec"][1], p["rec"][2],
                         ("%.2e" % d_pinch) if kind == "OFF" else "",
                         ("%.2e" % d_on) if kind == "OFF" else "",
                         " ".join(flags) if kind == "OFF" else
                         ("" if per["ON"]["rec"][0] == ref["BASE"]
                          else "reads %s != %s"
                          % (per["ON"]["rec"][0], ref["BASE"]))))
                print("           %-4s real zeros [%s]  n_imag=%d"
                      % (kind,
                         " ".join("%.5f" % v for v in p["cen"]["real"]),
                         p["cen"]["n_imag"]))
                if p["cen"]["cplx"]:
                    print("           %-4s complex zeros: %s"
                          % (kind,
                             " ".join("%.4f%+.4fi" % (z.real, z.imag)
                                      for z in p["cen"]["cplx"])))
        neg = [(math.log10(r["delta"]), math.log10(-r["tau_off"]))
               for r in rows if r["tau_off"] < 0]
        if len(neg) >= 3:
            s_mech = ols_slope([p[0] for p in neg],
                               [p[1] for p in neg])
            print("    mechanism check: OLS slope of log10|tau_OFF|"
                  " vs log10 delta = %+.3f over %d negative rungs"
                  " (prediction 2.000: tau_OFF ~ -4 delta^2"
                  " E'(gamma*)^2 -- the wall scalar IS the detector)"
                  % (s_mech, len(neg)))
        # amendment A-2: cache-precision floor of the plant instrument
        floor_x = max([0.0] + [-r["on"]["cell"]["tau"] for r in rows]
                      + [-cp["tau"]])
        n_mis_hard = 0
        ft_tags = []
        for r in rows:
            if r["on_reads_own"]:
                continue
            if abs(r["on"]["cell"]["tau"]) <= 100.0 * floor_x:
                ft_tags.append("%g" % r["delta"])
            else:
                n_mis_hard += 1
        print("    A-2 floor: FLOOR(x=%d) = %.3e (PSD-exact worlds"
              " measured tau < 0 by this much = cache-ordinate error"
              " 1e-13 >> cluster %.1e); ON misreads floor-typed at"
              " delta {%s}, hard misreads %d"
              % (x, floor_x, cells[x]["tau"], ", ".join(ft_tags)
                 or "-", n_mis_hard))
        ep = eprime_mp(diag_bottom(cells[x]["M_mp"], x, K, DPS[x]),
                       gstar)
        d_blind = math.sqrt(max(cells[x]["tau"], 0.0)
                            / (4.0 * ep * ep)) if ep != 0 else \
            float("nan")
        print("    blindness onset: E'(gamma*) of BASE = %+.4e ->"
              " delta_blind(x=%d) ~ sqrt(tau/(4 E'^2)) = %.3e"
              " (an off-line offset below this sits inside the true"
              " cluster and is invisible in principle)"
              % (ep, x, d_blind))
        if x == 8:
            d21 = math.sqrt(1.25e-93 / (4.0 * ep * ep))
            print("    extrapolated with the record tau(21) ="
                  " 1.25e-93 and this E' proxy: delta_blind(x=21)"
                  " ~ %.3e -- detection reaches absurd depth IFF the"
                  " matrix is resolved at dps ~ 4 pi x/ln 10; the"
                  " sensitivity IS the precision wall" % d21)
        a2[x] = {"rows": rows, "rec_base": rec_base,
                 "rec_pin": rec_pin, "ref": ref, "gstar": gstar,
                 "floor": floor_x, "on_misreads_hard": n_mis_hard}

    # ================================================ IV. A3 WORLDS
    section("IV. A3 -- CONTROL TRANSCRIPTION (Gram-fed known worlds,"
            " x = 5)")
    worlds: dict[str, list] = {}
    tt = [float(g) for g in gammas[gammas <= G_SYN]]
    worlds["TRUE-TRUNC"] = tt
    worlds["SMOOTH"] = smooth_zero_list(G_SYN)
    if not smoke:
        sp = 2.0 * math.pi / math.log(5.0)
        worlds["UNIF"] = [(n + 0.5) * sp for n in range(200)
                          if (n + 0.5) * sp <= G_SYN]
        scr = []
        for n, g in enumerate(tt):
            lo = tt[n - 1] if n > 0 else 0.0
            hi = tt[n + 1] if n + 1 < len(tt) else g + (g - lo)
            half = 0.5 * (hi - lo) / 2.0
            u = (n + 1) * GOLDEN
            scr.append(g + JIT * half * (2.0 * (u - math.floor(u))
                                         - 1.0))
        worlds["SCR"] = sorted(scr)
    K5 = cells[5]["K"]
    om_max5 = float(cells[5]["om"][-1])
    n_trans = 0
    exile_ok = True
    world_rows = []
    syn_taus: list[tuple[str, float]] = []
    for name, zl in worlds.items():
        t0 = time.time()
        M = target_gram_tilde(5, K5, DPS[5], zl)
        cS = diag_bottom(M, 5, K5, DPS[5])
        cen = census_of("WORLD-" + name, cS)
        if not cen["ok"]:
            continue
        own30 = int(sum(1 for g in zl if g < 30.0))
        own_band = int(sum(1 for g in zl if g < om_max5))
        meas30 = band_counts(cen["real"], (30.0,))[0]
        z30 = window_zeros(cen["real"], 0.0, 30.0)
        devs = [min(abs(z - g) for g in zl) for z in z30]
        maxdev = max(devs) if devs else 0.0
        transcribed = (meas30 == own30
                       and (maxdev < TRANS_POS_BAR))
        n_trans += int(transcribed)
        # exile bookkeeping: the K-1 forced zeros minus the world's
        # own in-band supply must reappear at/beyond the band edge
        exc_pred = (K5 - 1) - own_band
        n_beyond = (K5 - 1) - int(np.sum(cen["real"]
                                         < om_max5 - 1e-9))
        exile_ok &= abs(n_beyond - exc_pred) <= 1
        syn_taus.append((name, cS["tau"]))
        world_rows.append((name, own30, meas30, maxdev, transcribed,
                           own_band, exc_pred, n_beyond))
        print("  %-11s own(0,30)=%2d meas(0,30)=%2d tau=%s gap=%s"
              " max|z-world| in (0,30) = %.2e -> %s   %.1fs"
              % (name, own30, meas30, cS["tau_str"], cS["gap_str"],
                 maxdev,
                 "TRANSCRIBED" if transcribed else "NOT-TRANSCRIBED",
                 time.time() - t0))
        print("    world zeros < 30: %s"
              % " ".join("%.4f" % g for g in zl if g < 30.0))
        print("    meas  zeros < 30: %s"
              % " ".join("%.4f" % v for v in z30))
        print("    exile bookkeeping: own in-band(0,%.1f) = %d,"
              " forced K-1 = %d, predicted excess = %d, measured"
              " zeros beyond own in-band count = %d, cplx = %d"
              % (om_max5, own_band, K5 - 1, exc_pred, n_beyond,
                 len(cen["cplx"])))
    f_transcriber = n_trans >= (3 if not smoke else 1)
    print("  F-A3-TRANSCRIBER = %s (%d/%d worlds transcribed)"
          % (f_transcriber, n_trans, len(worlds)))
    print("  F-A3-EXILE-BOOKKEEPING = %s (excess == K-1 - N_world"
          "(0, om_max) +- 1 on every world)" % exile_ok)

    if not smoke:
        t0 = time.time()
        ecell = capture_build(5, "EPSTEIN", DPS[5])
        lane1.hp_zero_data(ecell)
        ez = ecell["zeros"]
        print("  EPSTEIN (source-built, lane 1's own builder): tau=%s"
              " census %d/%d (0,30)=%d zeros<30: %s   %.1fs"
              % (ecell["tau_str"], len(ez), ecell["census_expect"],
                 int((ez < 30.0).sum()),
                 " ".join("%.4f" % v for v in ez[ez < 30.0]),
                 time.time() - t0))
        print("    (Xi (0,30) = 3 at 14.13/21.02/25.01: a genuinely"
              " different arithmetic world yields a different census"
              " through the same instrument -- transcription, not"
              " preference.)")

    # ================================================ V. A4 EXISTENCE
    section("V. A4 -- PROOF-SIDE EXISTENCE: what is source-only, what"
            " is a measured premise")
    xs = list(X_MAIN)
    tau_l10 = [cells[x]["tau_log10"] for x in xs]
    gap_l10 = [math.log10(abs(cells[x]["gap"]))
               if cells[x]["gap"] != 0 else float("nan") for x in xs]
    s_tau = ols_slope(xs, tau_l10)
    s_gap = ols_slope(xs, gap_l10)
    print("  ladder: %s" % "  ".join(
        "x=%d tau=%s gap=%s" % (x, cells[x]["tau_str"],
                                cells[x]["gap_str"]) for x in xs))
    print("  OLS slopes: dlog10(tau)/dx = %+.3f   dlog10(gap)/dx ="
          " %+.3f   (Connes-scale reference -4pi/ln10 = %.3f)"
          % (s_tau, s_gap, -4.0 * math.pi / math.log(10.0)))
    for xf in (34, 55):
        print("    certifying SIMPLICITY (Theorem A's only hypothesis)"
              " at x=%d requires resolving a gap ~ 10^%.1f"
              % (xf, s_gap * xf + (gap_l10[-1] - s_gap * xs[-1])))
    print("  TYPED STATEMENT (A4): the exact objects M(x), its"
          " spectrum, and E_x exist source-only over the closed-form"
          " entries -- existence is NOT the gap.  But every property"
          " TPL consumes is a WALL-CLASS SCALAR of the zero measure"
          " via Z1: sign(lam_min) IS Weil positivity; the simplicity"
          " gap and the minimizer direction decay at the measured"
          " e^{-Theta(x)} rate above; and Theorem A's realness input"
          " (simplicity + even minimizer) is a MEASURED premise on"
          " every rung, not a source-side theorem.  No exact route to"
          " the census at cutoff x avoids resolving these scalars.")

    # ================================================ VI. A5 SCREENS
    section("VI. A5 -- TAU-SCREEN OF THE ESCAPE MARGINS")
    scr_rows = []
    for x in [xx for xx in SCREEN_X if xx in cells]:
        z = cells[x]["zeros"]
        k = 0
        while k < min(len(z), len(gammas) - 1):
            tol = 0.4 * (float(gammas[k + 1]) - float(gammas[k]))
            if abs(float(z[k]) - float(gammas[k])) <= tol:
                k += 1
            else:
                break
        disp = (float(np.mean(np.abs(
            np.asarray(z[:k]) - gammas[:k]))) if k else float("nan"))
        om_max = float(cells[x]["om"][-1])
        m_edge = om_max - float(gammas[k - 1]) if k else float("nan")
        m_b30 = float(np.min(np.abs(np.asarray(z) - 30.0)))
        scr_rows.append((x, cells[x]["tau_log10"], k, m_edge, m_b30,
                         disp))
        print("  x=%3d  log10tau=%8.2f  matched prefix k=%2d/%2d"
              "  m_edge=%8.4f  m_b30=%8.4f  mean disp=%.3e"
              % (x, cells[x]["tau_log10"], k, cells[x]["K"] - 1,
                 m_edge, m_b30, disp))
    screen_verdicts = []
    if len(scr_rows) >= 3:
        tl = [r[1] for r in scr_rows]
        for qi, qn in ((3, "m_edge"), (4, "m_b30"), (5, "mean_disp")):
            ql = [math.log10(max(r[qi], 1e-300)) for r in scr_rows]
            s = ols_slope(tl, ql)
            band = ("PASS" if abs(s) <= TAU_PASS
                    else "RELOCATION" if s >= TAU_RELOC else "MID")
            screen_verdicts.append((qn, s, band))
            print("  screen %-10s slope dlog10(q)/dlog10|tau| = %+.4f"
                  "  band %s" % (qn, s, band))
    else:
        print("  (screens need 3 rungs -- skipped in smoke)")

    # ================================================ VII. VERDICT
    section("VII. GATES + COMPOSITE VERDICT")
    check("W6 mp.polyroots succeeded on every planted/synthetic cell",
          not poly_fail, "failures: %s" % (poly_fail or "none"))
    psd_bar = -10.0 ** (-(DPS[5] // 3))
    check("W7 Gram worlds PSD (tau_syn >= -10^{-dps/3})",
          all(t >= psd_bar for _n, t in syn_taus),
          "  ".join("%s: %.3e" % (n, t) for n, t in syn_taus))
    wall = time.time() - T0_WALL
    check("W8 runtime", wall <= RUNTIME_BAR,
          "%.1f s (bar %.0f)" % (wall, RUNTIME_BAR))
    instrument_ok = all(ok for _n, ok, _d in CHECKS)

    deep_x = plant_xs[-1]
    rows_deep = a2.get(deep_x, {}).get("rows", [])
    by_delta = {r["delta"]: r for r in rows_deep}
    blind_small = (bool(rows_deep)
                   and all(d in by_delta
                           and (by_delta[d]["absorb"]
                                or by_delta[d]["mimic"])
                           for d in (SMALL_DELTAS if not smoke
                                     else DELTAS[-1:])))
    blind_deltas = [r["delta"] for r in rows_deep
                    if r["absorb"] or r["mimic"]]
    delta_star = max(blind_deltas) if blind_deltas else float("nan")
    wall_detects = bool(rows_deep) and all(r["tau_off"] < 0
                                           for r in rows_deep)
    on_misreads = a2.get(deep_x, {}).get("on_misreads_hard", 0)
    faithful_any = any(r["faithful"] for r in rows_deep)
    hard_fail_worlds = sum(
        1 for (name, own30, meas30, _d, tr, *_r) in world_rows
        if abs(meas30 - own30) >= 2)

    if not instrument_ok:
        verdict = "TP-DA-INSTRUMENT-EDGE"
    elif blind_small:
        verdict = ("TPL-BLIND-AT(delta <= %g at x = %d: the OFF-plant"
                   " is %s for every small delta; the faithful"
                   " reading (planted real census %s) is NEVER"
                   " produced%s)"
                   % (delta_star, deep_x,
                      "ABSORB-FULL" if any(r["absorb"]
                                           for r in rows_deep)
                      else "census-identical to the RH-true PINCH"
                      " world",
                      a2[deep_x]["ref"]["OFF"],
                      "; mechanism: tau_OFF < 0 throughout -- the"
                      " off-line mass is monetized as NEGATIVE form"
                      " value (the RH-hard wall scalar), not as a"
                      " census deviation" if wall_detects else ""))
    elif hard_fail_worlds >= 2 or on_misreads >= 4:
        verdict = ("TPL-BROKEN(instrument: %d worlds mis-transcribed"
                   " by >= 2 counts, ON control misread %d/6 hard"
                   " (non-floor-typed, amendment A-2) -- the"
                   " band-count instrument does not read censuses)"
                   % (hard_fail_worlds, on_misreads))
    elif f_transcriber and f_a1_bounded and f_smooth:
        verdict = ("TPL-CIRCULAR(TRANSCRIPTION-TAUTOLOGY: the"
                   " instrument transcribes whatever measure it is"
                   " fed (%d/%d worlds); EPISTEMIC-EMPTINESS: the"
                   " recorded band counts equal the smooth RvM counts"
                   " to < 1 and the census is a functional of the"
                   " measure below om_max ~ 2.5 pi x, all classically"
                   " verified at any feasible x; PRECISION-WALL:"
                   " outrunning verification needs dps ~ 2e12)"
                   % (n_trans, len(worlds)))
    else:
        verdict = ("TPL-RESISTED(plants detected at all measured"
                   " delta and transcription/boundedness incomplete:"
                   " %d/%d worlds transcribed, F-A1-BOUNDED %s,"
                   " F-SMOOTH %s; see tables)"
                   % (n_trans, len(worlds), f_a1_bounded, f_smooth))

    n_pass = sum(1 for _n, ok, _d in CHECKS if ok)
    print("\n" + "=" * 78)
    print("CHECKS %d/%d PASS   runtime %.1f s   SPEC_SHA %s"
          % (n_pass, len(CHECKS), wall, SPEC_SHA[:16]))
    print("VERDICT: %s" % verdict)
    if smoke:
        print("*** SMOKE RUN -- NOT VERDICT-BEARING ***")
    print("NO RH CLAIM. NO POSITIVITY CLAIM. EXPLORATION ONLY.")
    print("=" * 78)
    return 0 if n_pass == len(CHECKS) else 1


if __name__ == "__main__":
    sys.exit(main())
