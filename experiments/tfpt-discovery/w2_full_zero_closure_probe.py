#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""w2_full_zero_closure_probe -- PRIME.PORT.W2.FULLCLOSE.01
(EXPLORATION ONLY, experiments/; round 66 iteration, 2026-08-11).

WHY THIS PROBE EXISTS -- PAY THE PRICED TAIL.  CXCIII
(w2_verified_supply_consumption_probe, SPEC-SHA 921140fa..) proved
that the W2 head-size law was an envelope artifact (+0.191 ->
+0.009 dex/log h), collapsed the fixed-head demand to +0.004 dex,
and closed the recomposed certificate m_cert = FC + PARITH_hat -
TAILB > 0 on 16/67 surface rungs at N_Z = 7000 -- blocked ONLY by
the finite zero budget: the residual W2 demand was priced at med
~1e6 / max ~8.5e6 verified ordinates (surface, cB anatomy), with
the tail law +0.736 dex/log h.  This probe pays that price: a
20,000,000-ordinate verified-zero cache (EXTERNAL-CITED: Odlyzko
zeros6 for n <= 2,001,052 at 4e-9; LMFDB / Platt verified zeros
for the rest; every ordinate below T0 = 3e12 hence ON the line
unconditionally by Platt-Trudgian 2021) is certified and swapped
into the CXCIII machinery UNCHANGED, and the full recomposed
certificate runs on the 67 surface + 8 deep rungs with the
smallest affordable head per rung.

THE EXACT OBJECTS (CXCIII verbatim, one supply swap).  Per rung
and cut, phi_cont (ramp + w + extension, exact atom/continuum
corrections) and the explicit-formula read
    PARITH_hat = -4 Sum_{gamma <= T_c} Re phihat(gamma)
                 - TRIV - RAMP_AT + RAMP_CONT + EXT_CONT - EXT_AT,
    phihat(g)  = -(1/g^2) Sum_m J_m e^{i g v_m},
    |PARITH - PARITH_hat| <= TAILB,
    TAILB = 4 S_Delta Abel[1/gamma^2; T_c -> T0, N(T_c) = N exact]
            + 4 e^{vmax/2} S_Delta S2TAIL   (beyond T0, beta in
              [0,1] NOT assumed on the line)
            + ORD_PAD + NUFFT_PAD + TRIV_PAD  (declared, below),
    m_cert(nc) = FC(nc) + PARITH_hat(nc) - TAILB(nc).
TWO changes against CXCIII, both disclosed and both sound:
 (i) THE ZERO SUM AT N = 2e7 IS EVALUATED BY BANDED TYPE-3 NUFFT
     (finufft, eps 1e-14, source bands split at gamma = 1e4 /
     3e5 / the Odlyzko-LMFDB seam): the unique jump abscissae
     v_m of all reads (~1e5 of them; the deep rungs alone carry
     up to ~4.4e3 slope kinks each) make direct summation
     (~4e12 cos) infeasible.  The NUFFT is DATA-PATH ONLY and is
     warded three ways: (W-i) on the 7000-cache the NUFFT route
     must reproduce the CXCIII chunked zsum4re on EVERY read to
     F7_MATCH; (W-ii) on the big cache the direct chunked sum is
     recomputed on ONE full read (the smallest-support read of
     the ladder -- the direct big sum costs ~len(v) x 2e7 complex
     exponentials, so the cheapest read is the affordable one)
     and must match to FB_MATCH; (W-iii) the transform values
     F(v) = Sum_k cos(gamma_k v)/gamma_k^2 are recomputed
     directly (chunked, float64) at NW = 48 geomspace-sampled
     unique abscissae and must match to F_ERR_BAR, and TAILB
     carries the pad NUFFT_PAD = 4 S_Delta F_ERR_BAR.
(ii) THE TAIL GRID for the big cache is a declared geometric
     grid (ratio GEO_BIG) from T_c to T0 instead of the CXCIII
     per-rung phase grid: for the monotone envelope 1/gamma^2
     ANY grid gives a rigorous Abel upper bound (the corridor
     enters only through N_up/N_lo), a finer grid is only
     tighter, and one grid serves all rungs since 1/gamma^2 is
     rung-independent.  The 7000-cache REPRODUCTION WARD keeps
     the CXCIII per-rung tail_grid verbatim.
ORD_PAD is the window-transform Lipschitz pad, now PER SEGMENT:
|d/dgamma 4 Re phihat| <= 4 S_Delta (vmax gamma + 2)/gamma^3, so
ORD_PAD = 4 S_Delta (vmax Sum_k e_k/gamma_k^2 + 2 Sum_k
e_k/gamma_k^3) with the declared budgets e_k = 4.5e-9 (Odlyzko
segment: 4e-9 table + 5e-10 print quantisation) and e_k =
gamma_k 2^-50 (LMFDB segment: float64 parse rounding dominates;
the stored zeros are ~1e-30 accurate).  Measured below: the
total ORD_PAD + NUFFT_PAD is > 2 dex under the smallest wall
margin -- the accuracy demand is met with room.

WHAT IS MEASURED.
 (a) CACHE CERTIFICATION (kill wards, both caches): census +
     strict monotonicity + gamma_1; Rosser corridor per index,
     both sides, on ALL 2e7 ordinates (unconditional, Rosser
     1941 constants CLXXXI verbatim); Backlund count consistency
     |theta(gamma_k)/pi + 1 - k| <= S_ABS_BAR = 2.8 on the whole
     cache (asymptotic theta, remainder < 1e-9 here; 2.8 is an
     empirical |S(T)| ceiling for this T-range -- the corridor
     ward stays the unconditional one); overlap vs the CLXXXIX
     mpmath 7000-cache (worst |Delta|); Odlyzko-LMFDB seam
     spacing; independent mpmath |zeta(1/2 + i gamma)| spot
     checks at NS = 24 geomspace indices, dps 20; spacing sanity
     relative to the local mean gap; T_c < T0.
 (b) CXCIII REPRODUCTION (the ward): with the 7000-cache and the
     CXCIII read set (surface cuts A in HEAD_A + cB; deep A = 9
     + cB), the full CXCIII A/C/F content must reproduce: split
     ward X1, ARITH med, heart on every read, soundness, the
     16/67 + 0/8 census, minimal head fraction med 0.480 and
     margin med -0.39 dex, the cB blocker band +0.79/+1.79/
     +2.59 dex (deep med +2.84, overall max +3.11), the
     zeros-needed anatomy med 9.8e5 / max 8.5e6 and the
     1e5/1e6/1e7 closability census 7/34/67, and the Buethe
     UNCOND baseline (67/67 at head frac med 0.9534, deep 8/8 at
     0.9712).
 (c) THE FULL CLOSURE (the mission): the same reads priced by the
     2e7 cache -- heart ward on EVERY read (zeros against primes
     at TAILB ~ 1e2x sharper), soundness m_cert <= m, then the
     census: minimal certifying head A* per rung on the frozen
     ladder (A ascending, then cB; the deep rungs get the full
     ladder, a DECLARED extension of CXCIII's deep A = 9 + cB
     reads), head fractions, certified margins log10(m_cert/m),
     and THE HEADLINE census out of 67 + 8.  DEMAND-SIDE
     ECONOMY, measured not planned: the same census with the
     cache truncated at the Odlyzko prefix (N = 2,001,052, its
     own T_c, Abel, pads) -- how much of the ladder the free 2M
     table already buys.  Residual anatomy for any open rung:
     log10(TAILB/m) and the zeros-needed price.
 (d) THE COMPOSED WALL CENSUS: B-half (CLXXVII, SPEC 903714c1,
     CITED: 39/39 surface + 27/27 deep steps covering all 28
     eligible deep rungs), W1 assembly (CLXXXIX, SPEC deea4e1c,
     CITED: 39/39 surface, composed 67/67 with the CLXXXIV deep
     28/28), and W2 (THIS RUN) are matched BY WINDOW kz: the W1/B
     surface ladder is re-enumerated from parent.build_truth_rows
     (39 kz), the deep eligibility scan (H_HOLD, ATOM_MAX < X <=
     4e6, ext_frame arithmetic) is re-run on the byte-exact 4e6
     table; on every W2 rung whose kz lies in those ladders and
     whose W2 certificate closes here, ALL THREE wall faces are
     certified from cited inputs -- the composed number is
     printed with the kz lists, and the W2 rungs OUTSIDE the
     W1/B ladders are reported honestly as W2-only.
 (e) GATES: tau screens (CLXXXV/CXCIII jackknife definitions
     verbatim, PASS |s| <= 0.30 / RELOC >= 0.70) on the new
     margins (c_req_new dex at A = 9 and A = 12, log10(TAILB/m)
     at cB, all big-cache); controls MUST fire (kill): smooth
     world breaks the wall 67/67, Epstein + scramble combs break
     lam_min at kz 9, the scrambled comb breaks the exact
     prime-side heart ward at BOTH control cuts against the ~1e2x
     sharper big TAILB, the off-line impostor (gamma_1 -> beta =
     0.75, FE-symmetrised quadruple, CLXXXIX construction) shifts
     PARITH_hat by >= 10x the genuine big-cache residual.
     ANTI-CIRCULARITY: no wall output is an input to any bound;
     the verified ordinates are the CLXXXIX-sanctioned input
     class, enter ONLY the supply side and are tested AGAINST the
     independent prime side on every read; measured m appears
     only as truth column, soundness ward and denominator.  RNG:
     none except the declared scramble control (seed 1).

VERDICT (frozen enums, decided by these rules and nothing else):
  V1 cache: CACHE-CERTIFIED(N; corridor n/N; Backlund worst;
     overlap; worst zeta spot) -- kill wards decide.
  V2 ward: CXCIII-REPRODUCED(16/67 + 0/8; head frac; blocker
     band) -- kill wards decide.
  V3 headline: W2-FINITE-SURFACE-CLOSED(67/67 + 8/8; minimal
     head fraction min/med/max; margin med dex; economy census
     at N = 2,001,052) iff EVERY rung closes; else
     W2-FULLCLOSE-PARTIAL(n_s/67 + n_d/8; per-rung residual dex;
     the zero price of the remainder) -- symmetric, honest.
  V4 wall: WALL-COMPOSED(n_comp of n_int matched rungs with all
     three faces B + W1 + W2 certified from cited inputs;
     W2-only remainder counted separately).
  V5 gates: DISCRIMINATION-FIRES(scramble 2/2, impostor ratio,
     smooth 67/67, Epstein + scramble lam < 0) + SCREENS(...) /
     DISCRIMINATION-UNRESOLVED(census).
DEAD overrides: K1 PIPELINE-BROKEN / K2 WARD-BROKEN / K3
ALGEBRA-BROKEN as tagged.

FROZEN BARS: N_Z7 = 7000 (verified_zeros_n7000.npy, CLXXXIX cache
REUSED); N_ZB = 20,000,000 (verified_zeros_big.npy, built by the
DISCLOSED builder w2_big_zero_cache_build.py: fetch + certify
modes, meta json with per-request SHA-256 log); SPEC prefixes:
w2 8db29e6e, subgamma c7d8810c, consume 921140fa (docstring SHA,
source parsed not executed for the builder); segment error
budgets E_ODLZ = 4.5e-9 (n <= 2,001,052), E_LMFDB = gamma 2^-50;
ZETA_TOL = 1e-6 at NS = 24 (dps 20); CORR_EPS = 1e-6; S_ABS_BAR
= 2.8; OVERLAP_BAR = 5.5e-9; RELGAP_BAR = 5.0; GEO_BIG = 1.0002;
ABELB_BAND = (1e-7, 5e-7); NUFFT_EPS = 1e-14, band edges
(gamma_1, 1e4, 3e5, seam, T_c]; F_ERR_BAR = 1e-11 at NW = 48
spots; F7_MATCH = 1e-10 scaled; FB_MATCH = 1e-10 scaled (one
full direct read at the smallest support); RECON/CONT/TRANS/SOUND
tolerances = CXCIII verbatim (1e-9 / 1e-12 / 1e-10 / 1e-9);
ABEL_BAND7 = (1e-4, 4e-4); CXCIII reproduction refs (frozen-run
numbers): CLOSE7 = (16, 0) exact, HAFR7 = 0.480 atol 0.005,
MARG7 = -0.39 atol 0.03, BLOCK7 = (+0.79, +1.79, +2.59) atol
0.03, DEEP7_MED = +2.84 atol 0.03, BLOCK7_MAX = +3.11 atol 0.03,
NEED7 = (9.8e5, 8.5e6) rtol 0.05, LEV7 = (7, 34, 67) exact,
ARITH_REF = 0.302 atol 0.010, HAFR_B = 0.9534 / HAFR_B_DEEP =
0.9712 atol 0.005, X1 <= 1e-10, W-census 67 + 8; CLXXXV frame
constants verbatim via the w2 module (HEAD_A, cut ladder, CTRL_KZ
= 9, SUBSET); W1/B ladder: PARENT_ROWS = 39 exact, deep
eligibility count printed (CLXXVII saw 28 eligible -> 27 steps);
IMP_BETA = 0.75, IMP_RATIO_MIN = 10; screens PASS/RELOC bars
CLXXXV verbatim.  Runtime cap declared: 25 min.  Smoke mode
W2FZ_SMOKE=1 restricts the surface to kz <= 30 and DEEP_MAX = 2
and defers the full-only reproduction wards (disclosed prints);
controls always full.

SCOUTING DISCLOSURE (2026-08-11, pre-spec, before any probe run;
nothing here moved a bar afterwards): (1) the builder's `plan`
mode (kept in the repo, not deleted) inverted the tail budget
per rung with main-term + corridor Abel: at margin factor 0.9
the demand is med 1.53e5 / max 1.904e7 ordinates and 67/75 rungs
close on the free Odlyzko 2M table alone -- the 8 DEEP rungs
price the remainder (CXCIII's med 9.8e5 / max 8.5e6 anatomy was
surface-only at cB), hence the frozen procurement N_ZB = 2e7
(~5% headroom over kz 326's 1.904e7); (2) the builder's fetch +
certify modes ran BEFORE this spec was frozen and their numbers
were seen: corridor 20,000,000/20,000,000, Backlund worst
1.9851, overlap vs mpmath 2.91e-9, seam gap 0.4431, zeta spots
worst 1.97e-8 at 39 draws, min gap 2.32e-3, max gap/local-mean
3.469, Sum 1/gamma^2 = 0.02310474, T_c = 9,499,220.4795; the
builder's ONE amendment (a naive absolute max-gap sanity bar of
6.0 that tripped over the genuine gamma_2 - gamma_1 = 6.887 and
was replaced by the local-mean-relative criterion) happened in
the BUILDER, pre-spec, and is disclosed here; (3) two throwaway
finufft sizing checks (uniform random stand-in frequencies, NOT
zeta data): single-band type-3 at N = 2e7 gave abs dev 6.5e-10
vs direct, the frozen 4-band split gave 5.9e-13 and 1.3 s --
F_ERR_BAR = 1e-11 was set from that measurement with > 1 dex
margin BEFORE any zeta-side read.  No closure census, heart
residual, margin or screen value was seen before the freeze.

SMOKE-RUN DISCLOSURE (2026-08-11, before freezing): ONE smoke run
(W2FZ_SMOKE=1: 19 surface rungs kz <= 30, DEEP_MAX = 2, controls
full; 26.9 s, exit 0, 48/48 checks) and NO amendment: cache
wards all green on the full 2e7 cache (corridor 2e7/2e7,
Backlund 1.9851, overlap 2.91e-9, zeta spots worst 2.19e-8,
abel_big 2.552e-7 in band, Se2 1.04e-10 / Se3 3.28e-12); NUFFT
wards F-spot worst 8.4e-14 at 44 spots (bar 1e-11), F7-route
worst 8.1e-14 scaled on 150 reads, big direct read match 1.5e-16
(7-jump read); heart big worst scaled excess -7.2e-9 on 150
reads (slack +2.33/+4.93/+6.76 dex), soundness 0 violations,
ORD_PAD + NUFFT_PAD max 1.12e-8 = 2.10 dex under min m; smoke
census 19/19 surface + 2/2 deep at 2e7 (head frac med 0.0230,
margin med -0.01 dex), economy census 19/19 + 0/2 at the 2M
prefix (the two deep rungs close only with the full cache --
exactly the plan's prediction); controls fire (smooth 19/19,
Epstein -1.0e+01, scramble -7.9e+00, heart-break 2/2 at
1.2e5/3.1e5 x TAILB, impostor 1.6e8 x residual); screens on the
h-truncated smoke subset PASS/PASS/AMBIG (full-run screens
decide); composed-wall intersection on the smoke subset 16/16 +
2/2, deep eligibility 28 reproduced.  The deferred full-only
wards (X2 ARITH med 0.1323 on the subset, CXCIII censuses
14/19 + 0/2, NEED/LEV, UNCOND baseline 19/19 at 0.9412 / deep
2/2 at 0.9770, BLOCK bands) print smoke values but do not gate
in smoke, disclosed inline.  No bar, band, count, rule or enum
was moved after the smoke run; the frozen run repeats everything
on the full 67 + 8 ladder.

HONEST SCOPE (stated once, repeated in the verdict): every
certified statement is per-rung and along the MEASURED critical
direction v (DIRECTION-CONDITIONAL, CLXXXV d1 verbatim); the
head varies only inside the frozen ladder; nothing is uniform in
h or in direction; the deep block is FLOAT-LEVEL as in CLXXXV.
The inputs are cited verified zeros (Odlyzko / LMFDB-Platt
pedigree, all below the Platt-Trudgian height T0 = 3e12) +
unconditional envelopes (Rosser corridor, Abel, beyond-T0 with
beta in [0,1] unassumed) + exact composition; a finite zero sum
can never prove RH -- a full census is a FINITE-SURFACE theorem
about the deployed rungs, not an asymptotic statement.  The
all-h, all-direction W2 object (the Weil-positivity face)
remains open and RH-hard in EVERY branch.  NO RH claim in either
direction.  No marker moves, no promotion, no ledger row; stdout
only; nothing written outside experiments/.

Sources (read-only): v563_paper2_readouts (core);
w2_pairing_structure_probe (CLXXXV demand machinery verbatim);
w2_verified_supply_consumption_probe (CXCIII translation
machinery IMPORTED and reused function-by-function: phi_cont_of,
direct_read, zsum4re, hat_seg_c, tail_grid, zeros_needed,
recon_of, triv_env_pl); subgamma_fourier_bound_probe (CLXXXI
corridor/Abel/s2_tail/U0/T0); exterior_pg_schur_probe
(build_truth_rows, ladder match only); the disclosed builder
w2_big_zero_cache_build.py (data procurement, parsed not
executed here).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/w2_full_zero_closure_probe.py
"""

import ast
import hashlib
import json
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

import v563_paper2_readouts as core  # noqa: E402  (READ-ONLY)
import w2_pairing_structure_probe as w2  # noqa: E402  (READ-ONLY)
import subgamma_fourier_bound_probe as subg  # noqa: E402 (READ-ONLY)
import w2_verified_supply_consumption_probe as cons  # noqa: E402

SMOKE = os.environ.get("W2FZ_SMOKE", "") == "1"

ZC7_NPY = os.path.join(_HERE, "verified_zeros_n7000.npy")
ZCB_NPY = os.path.join(_HERE, "verified_zeros_big.npy")
ZCB_META = os.path.join(_HERE, "verified_zeros_big_meta.json")
N_Z7 = 7000
N_ZB = 20_000_000
SEAM_N = 2_001_052
E_ODLZ = 4.5e-9
E_LMFDB_ULP = 2.0 ** -50
ZETA_TOL = 1.0e-6
NS_ZETA = 24
CORR_EPS = 1.0e-6
S_ABS_BAR = 2.8
OVERLAP_BAR = 5.5e-9
RELGAP_BAR = 5.0
GEO_BIG = 1.0002
ABELB_BAND = (1.0e-7, 5.0e-7)
NUFFT_EPS = 1.0e-14
BAND_EDGES = (1.0e4, 3.0e5)
F_ERR_BAR = 1.0e-11
NW_SPOTS = 48
F7_MATCH = 1.0e-10
FB_MATCH = 1.0e-10
ABEL_BAND7 = (1.0e-4, 4.0e-4)
CLOSE7 = (16, 0)
HAFR7 = 0.480
HAFR7_ATOL = 0.005
MARG7 = -0.39
MARG7_ATOL = 0.03
BLOCK7 = (0.79, 1.79, 2.59)
BLOCK7_ATOL = 0.03
DEEP7_MED = 2.84
BLOCK7_MAX = 3.11
NEED7 = (9.8e5, 8.5e6)
NEED7_RTOL = 0.05
LEV7 = (7, 34, 67)
NEED_LEVELS = (1.0e5, 1.0e6, 1.0e7)
ARITH_REF = 0.302
ARITH_ATOL = 0.010
HAFR_B = 0.9534
HAFR_B_DEEP = 0.9712
HAFR_B_ATOL = 0.005
PARENT_ROWS = 39
IMP_BETA = 0.75
IMP_RATIO_MIN = 10.0
CUT_A = w2.HEAD_A
A_STR = 9
CTRL_KZ = w2.CTRL_KZ
KZ_TOP = 30 if SMOKE else w2.KZMAX
DEEP_MAX = 2 if SMOKE else 8
N_SURF = 67
N_DEEP = 8
PREFIXES = dict(w2="8db29e6e", subgamma="c7d8810c",
                consume="921140fa")

CHECKS = []
KILLS = []
T0 = time.time()


def check(name, ok, detail="", kill=None):
    CHECKS.append((name, bool(ok)))
    if kill and not ok:
        KILLS.append(kill)
    print("  [%s] %s%s" % ("PASS" if ok else "FAIL", name,
                           ("  -- " + detail) if detail else ""),
          flush=True)
    return bool(ok)


def section(title):
    print("\n" + "=" * 76)
    print(title)
    print("=" * 76, flush=True)


def ast_scan():
    src = open(os.path.abspath(__file__), encoding="utf-8").read()
    bad = []
    for node in ast.walk(ast.parse(src)):
        name = None
        if isinstance(node, ast.Name):
            name = node.id
        elif isinstance(node, ast.Attribute):
            name = node.attr
        if name and name.lower() in w2.BANNED_IDS:
            bad.append(name)
    return bad


def band(v):
    v = np.asarray(v, float)
    return float(np.min(v)), float(np.median(v)), float(np.max(v))


def theta_asym(t):
    """Riemann-Siegel theta, asymptotic (remainder < 1e-9 here)."""
    t = np.asarray(t, float)
    return (0.5 * t * np.log(t / (2.0 * math.pi)) - 0.5 * t
            - math.pi / 8.0 + 1.0 / (48.0 * t)
            + 7.0 / (5760.0 * t ** 3))


def abel_geo(tc, n_at_tc):
    """Abel upper bound of Sum_{gamma > tc} 1/gamma^2 on the
    declared geometric grid (ratio GEO_BIG) with exact N(tc)."""
    ng = int(math.ceil(math.log(subg.T0_RH / tc)
                       / math.log(GEO_BIG))) + 1
    tg = tc * GEO_BIG ** np.arange(ng + 1)
    tg[-1] = subg.T0_RH
    return subg.abel_upper(tg, 1.0 / tg[:-1] ** 2,
                           n_start=float(n_at_tc))


def f_transform(gam, vu):
    """F(v) = Sum_k cos(gamma_k v)/gamma_k^2 at the unique
    abscissae vu, via banded type-3 NUFFT (declared bands)."""
    import finufft
    w = (1.0 / gam ** 2).astype(np.complex128)
    edges = [float(gam[0])] + list(BAND_EDGES) + [float(gam[-1])]
    out = np.zeros(len(vu), np.complex128)
    for a, b in zip(edges[:-1], edges[1:]):
        lo = int(np.searchsorted(gam, a, side="left"))
        hi = int(np.searchsorted(gam, b, side="right")) \
            if b < float(gam[-1]) else len(gam)
        if hi > lo:
            out += finufft.nufft1d3(gam[lo:hi], w[lo:hi],
                                    np.asarray(vu, float),
                                    eps=NUFFT_EPS, isign=1)
    return out.real


def f_direct(gam, vv, chunk=400_000):
    """Direct chunked F(v) for the NUFFT spot ward."""
    acc = np.zeros(len(vv))
    for i0 in range(0, len(gam), chunk):
        g = gam[i0:i0 + chunk]
        acc += (np.cos(np.outer(vv, g)) @ (1.0 / g ** 2))
    return acc


def par_hat_from_f(pc, F, vidx):
    """PARITH_hat with zs = zsum4re rewritten through F(v):
    zs = -4 J.F(v) (pure rearrangement, warded)."""
    zs = -4.0 * float(pc["J"] @ F[vidx])
    return (-zs - pc["triv"] - pc["ramp_at"] + pc["ramp_cont"]
            + pc["ext_cont"] - pc["ext_at"]), zs


def tailb_of(pc, abel, s2t, se2, se3):
    """TAILB with the declared segment ORD_PAD + NUFFT_PAD."""
    sd = pc["sd"]
    ord_pad = 4.0 * sd * (pc["vmax"] * se2 + 2.0 * se3)
    nuf_pad = 4.0 * sd * F_ERR_BAR
    return (4.0 * sd * abel
            + 4.0 * math.exp(0.5 * pc["vmax"]) * sd * s2t
            + ord_pad + nuf_pad
            + 1e-12 * (1.0 + abs(pc["triv"]))), ord_pad + nuf_pad


def finish(labels):
    section("V -- FROZEN VERDICT")
    passed = sum(1 for _n, ok in CHECKS if ok)
    if KILLS:
        verdict = {"K1": "PIPELINE-BROKEN", "K2": "WARD-BROKEN",
                   "K3": "ALGEBRA-BROKEN"}[KILLS[0]]
    else:
        verdict = " / ".join(labels.get(k, "-")
                             for k in ("v1", "v2", "v3", "v4",
                                       "v5"))
    print("\n  VERDICT: %s" % verdict)
    print("""
  HONEST SCOPE: (i) finite deployed surface only -- every statement is
  per-rung on the frozen 67 + 8 ladder; (ii) along the MEASURED
  critical direction v (DIRECTION-CONDITIONAL, the CLXXXV UNIF-PATH
  caveat restated: the L1 -> L2 / Loewner uniformity step is NOT taken
  here, nothing is uniform in h or in direction, the deep block is
  FLOAT-LEVEL); (iii) inputs = cited verified zeros (Odlyzko zeros6 /
  LMFDB-Platt, all below Platt-Trudgian T0 = 3e12 hence ON the line
  unconditionally) + unconditional envelopes (Rosser corridor, Abel,
  beyond-T0 with beta in [0,1] unassumed) + exact composition;
  (iv) the all-h, all-direction Weil-positivity object remains OPEN
  and RH-hard in every branch; (v) NO RH claim in either direction.
  No marker moves, no promotion, no ledger row; stdout only.""")
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed"
          % (time.time() - T0, len(CHECKS), len(CHECKS) - passed))
    if any(not ok for _n, ok in CHECKS):
        print("FAILED: %s" % [nm for nm, ok in CHECKS if not ok])
    return 0 if passed == len(CHECKS) else 1


def main():
    section("PRIME.PORT.W2.FULLCLOSE.01 -- the 2e7 verified-zero "
            "cache pays the CXCIII tail price (EXPLORATION ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s"
          % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
    shas = dict(
        w2=hashlib.sha256(w2.__doc__.encode("utf-8")).hexdigest(),
        subgamma=hashlib.sha256(
            subg.__doc__.encode("utf-8")).hexdigest(),
        consume=hashlib.sha256(
            cons.__doc__.encode("utf-8")).hexdigest())
    for tag in sorted(shas):
        print("    %-8s SPEC SHA-256 = %s" % (tag, shas[tag]))
    print("    PEDIGREE (EXTERNAL-CITED): Odlyzko zeta_tables "
          "zeros6 (first 2,001,052 zeros, 4e-9); LMFDB / Platt "
          "verified zeros (n <= %d);" % N_ZB)
    print("      Platt-Trudgian 2021 T0 = %.1e (every summed zero "
          "ON the line); Rosser 1941 N(T) corridor (tail + cache "
          "ward); Buethe 2016 (baseline)." % subg.T0_RH)
    if SMOKE:
        print("    *** SMOKE MODE: kz <= %d, DEEP_MAX = %d, "
              "full-only wards deferred ***" % (KZ_TOP, DEEP_MAX))
    check("S0 AST firewall clean (CLXXXV identifier ban)",
          not ast_scan(), kill="K2")
    ok_pref = all(shas[k][:8] == v for k, v in PREFIXES.items())
    check("S0b predecessor SPEC prefixes reproduced (%s)"
          % "/".join(PREFIXES[k] for k in sorted(PREFIXES)),
          ok_pref, kill="K2")
    try:
        import finufft  # noqa: F401
        ok_fin = True
    except Exception:                        # noqa: BLE001
        ok_fin = False
    check("S0c finufft available (banded type-3, eps %.0e)"
          % NUFFT_EPS, ok_fin, kill="K1")
    if KILLS:
        return finish({})

    # ------------------------------------------------------------ Z
    section("Z -- both verified-zero caches and their wards")
    check("Z0 caches present", os.path.exists(ZC7_NPY)
          and os.path.exists(ZCB_NPY) and os.path.exists(ZCB_META),
          kill="K1")
    if KILLS:
        return finish({})
    gam7 = np.load(ZC7_NPY)
    t_c7 = float(gam7[-1])
    check("Z1 7000-cache census + monotone + gamma_1 (dev %.1e)"
          % abs(gam7[0] - subg.GAMMA1),
          len(gam7) == N_Z7 and bool(np.all(np.diff(gam7) > 0.0))
          and abs(gam7[0] - subg.GAMMA1) <= 2.0e-6, kill="K2")
    gamb = np.load(ZCB_NPY)
    meta = json.load(open(ZCB_META))
    t_cb = float(gamb[-1])
    check("Z2 big-cache census %d == %d == meta, monotone, gamma_1 "
          "dev %.1e, T_c = %.1f < T0"
          % (len(gamb), N_ZB, abs(gamb[0] - subg.GAMMA1), t_cb),
          len(gamb) == N_ZB and meta["n_zeros"] == N_ZB
          and bool(np.all(np.diff(gamb) > 0.0))
          and abs(gamb[0] - subg.GAMMA1) <= 2.0e-6
          and t_cb < subg.T0_RH, kill="K2")
    kk = np.arange(1, N_ZB + 1, dtype=float)
    up_r = subg.n_up(gamb + CORR_EPS)
    lo_r = subg.n_lo(gamb + CORR_EPS)
    up_l = subg.n_up(np.maximum(gamb - CORR_EPS, 2.0))
    lo_l = subg.n_lo(np.maximum(gamb - CORR_EPS, 2.0))
    n_ok = int(np.sum((kk <= up_r) & (kk >= lo_r)
                      & (kk - 1.0 <= up_l) & (kk - 1.0 >= lo_l)))
    check("Z3 Rosser corridor per index, both sides (%d/%d)"
          % (n_ok, N_ZB), n_ok == N_ZB, kill="K2")
    s_dev = float(np.max(np.abs(theta_asym(gamb) / math.pi + 1.0
                                - kk)))
    check("Z4 Backlund count consistency (worst %.4f <= %.1f, "
          "empirical |S| ceiling; Z3 is the unconditional ward)"
          % (s_dev, S_ABS_BAR), s_dev <= S_ABS_BAR, kill="K2")
    del kk, up_r, lo_r, up_l, lo_l
    dev7 = float(np.max(np.abs(gamb[:N_Z7] - gam7)))
    check("Z5 overlap vs CLXXXIX mpmath cache (worst %.2e <= "
          "%.1e)" % (dev7, OVERLAP_BAR), dev7 <= OVERLAP_BAR,
          kill="K2")
    gaps = np.diff(gamb)
    relmax = float(np.max(gaps * np.log(gamb[:-1]
                                        / (2.0 * math.pi))
                          / (2.0 * math.pi)))
    seam_gap = float(gamb[SEAM_N] - gamb[SEAM_N - 1])
    check("Z6 spacing sanity (min %.2e, max/local-mean %.3f <= "
          "%.1f; seam gap %.4f)"
          % (float(gaps.min()), relmax, RELGAP_BAR, seam_gap),
          float(gaps.min()) > 1e-4 and relmax <= RELGAP_BAR
          and 0.0 < seam_gap < 5.0, kill="K2")
    del gaps
    from mpmath import mp as _mp, mpc as _mpc
    from mpmath import zeta as _zf
    _mp.dps = 20
    idx = np.unique(np.geomspace(1, N_ZB, NS_ZETA).astype(int)) - 1
    worst_z = max(float(abs(_zf(_mpc(0.5, float(gamb[i])))))
                  for i in idx)
    check("Z7 independent mpmath |zeta| spots (%d draws, worst "
          "%.2e <= %.0e, dps 20)" % (len(idx), worst_z, ZETA_TOL),
          worst_z <= ZETA_TOL, kill="K2")
    # error-budget sums (full + 2M prefix + 7000 cache)
    e_k = np.empty(N_ZB)
    e_k[:SEAM_N] = E_ODLZ
    e_k[SEAM_N:] = gamb[SEAM_N:] * E_LMFDB_ULP
    inv2b = float(np.sum(1.0 / gamb ** 2))
    inv3b = float(np.sum(1.0 / gamb ** 3))
    se2b = float(np.sum(e_k / gamb ** 2))
    se3b = float(np.sum(e_k / gamb ** 3))
    inv2m = float(np.sum(1.0 / gamb[:SEAM_N] ** 2))
    se2m = float(np.sum(e_k[:SEAM_N] / gamb[:SEAM_N] ** 2))
    se3m = float(np.sum(e_k[:SEAM_N] / gamb[:SEAM_N] ** 3))
    del e_k
    inv2_7 = float(np.sum(1.0 / gam7 ** 2))
    inv3_7 = float(np.sum(1.0 / gam7 ** 3))
    s2t = subg.s2_tail()
    t_c2m = float(gamb[SEAM_N - 1])
    abel_b = abel_geo(t_cb, N_ZB)
    abel_2m = abel_geo(t_c2m, SEAM_N)
    check("Z8 Abel tail base big %.3e in [%.0e, %.0e] (N(T_c) "
          "exact; 2M prefix %.3e)"
          % (abel_b, ABELB_BAND[0], ABELB_BAND[1], abel_2m),
          ABELB_BAND[0] <= abel_b <= ABELB_BAND[1], kill="K2")
    print("    Sum 1/gamma^2: 7000 %.8f | 2M %.8f | 2e7 %.8f; "
          "segment pads Se2 %.2e / Se3 %.2e"
          % (inv2_7, inv2m, inv2b, se2b, se3b))

    # ------------------------------------------------------------ W
    section("W -- the CLXXXV ladder (demand machinery verbatim)")
    rungs = []
    for kz in range(2, KZ_TOP + 1):
        r = w2.build_rung(kz)
        if r is not None:
            rungs.append(r)
    rungs.sort(key=lambda r: (r["h"], r["kz"]))
    N = len(rungs)
    check("W1 ladder census %d %s" % (N, "== 67" if not SMOKE
                                      else ">= 8 (smoke)"),
          (N == N_SURF) if not SMOKE else (N >= 8),
          "h %d..%d  [%.1f s]" % (rungs[0]["h"], rungs[-1]["h"],
                                  time.time() - T0), kill="K1")
    if KILLS:
        return finish({})
    sub = [r for r in rungs if r["kz"] in w2.SUBSET]
    pres = max(r["pivres"] for r in sub) if sub else 0.0
    check("W2 WARD m > 0 on %d/%d + pivot collapse %.1e <= %.0e"
          % (sum(1 for r in rungs if r["m"] > 0), N, pres,
             w2.RES_WARD),
          all(r["m"] > 0 for r in rungs) and pres <= w2.RES_WARD,
          kill="K2")

    # ------------------------------------------------------------ E
    section("E -- classical inputs + the 4e6 extension table")
    lam_ext = core.von_mangoldt_table(w2.TAB_EXT)
    check("E0 deep-table prefix byte-exact",
          bool(np.array_equal(lam_ext[:core.ATOM_MAX + 1],
                              core.LAM_TAB)), kill="K2")
    xs = core._NN.astype(float)
    psi_c = np.cumsum(core.LAM_TAB[core._NN])
    kp = xs > 11.0
    env_true = float(np.max(np.abs(psi_c[kp] - xs[kp])
                            / np.sqrt(xs[kp])))
    check("E1 Buethe soundness on the deployed table (%.4f <= "
          "%.2f)" % (env_true, w2.BUETHE_C),
          env_true <= w2.BUETHE_C, kill="K2")
    tg0 = cons.tail_grid(rungs[0]["D"], t_c7)
    abel0 = subg.abel_upper(tg0, 1.0 / tg0[:-1] ** 2,
                            n_start=float(N_Z7))
    check("E2 CXCIII Abel base %.4e in [%.0e, %.0e]"
          % ((abel0,) + ABEL_BAND7),
          ABEL_BAND7[0] <= abel0 <= ABEL_BAND7[1], kill="K2")
    NNx = np.nonzero(lam_ext > 0.0)[0]
    EXT = dict(lam=lam_ext, NN=NNx, U=np.log(NNx.astype(float)),
               MU=2.0 * lam_ext[NNx] / np.sqrt(NNx.astype(float)))
    EXT["G"] = np.diff(EXT["U"])
    elig_kz = []
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
        elig_kz.append(kz)
    deep_rows = []
    if elig_kz:
        order = sorted(elig_kz)
        pick = sorted(set(int(round(t)) for t in
                          np.linspace(0, len(order) - 1,
                                      min(DEEP_MAX, len(order)))))
        for ii in pick:
            r = w2.build_rung(order[ii], ext=EXT)
            if r is not None:
                deep_rows.append(r)
        deep_rows.sort(key=lambda r: r["h"])
    check("E3 deep census %d %s (eligible %d)"
          % (len(deep_rows), "== 8" if not SMOKE else "(smoke)",
             len(elig_kz)),
          len(deep_rows) == DEEP_MAX, kill="K1")
    if KILLS:
        return finish({})

    # ------------------------------------------------------------ X
    section("X -- the exact split reproduced (CLXXXV wards)")
    dx = 0.0
    ratio_at = []
    for r in rungs:
        for nc in w2.cut_ladder(r):
            sp = w2.split_at(r, nc)
            if sp is None:
                continue
            dx = max(dx, sp["dev_x1"], sp["dev_x3"])
            if nc == r["ncB"]:
                ratio_at.append(abs(sp["par"])
                                / max(abs(sp["t_int"]), 1e-300))
    check("X1 WARD split identities on the whole ladder: max "
          "%.2e <= %.0e" % (dx, w2.ID_WARD), dx <= w2.ID_WARD,
          kill="K2")
    arith_med = float(np.median(np.array(ratio_at)))
    if not SMOKE:
        check("X2 ARITH-SMALL med %.4f == %.3f (atol %.3f)"
              % (arith_med, ARITH_REF, ARITH_ATOL),
              abs(arith_med - ARITH_REF) <= ARITH_ATOL, kill="K2")
    else:
        print("    (smoke: ARITH med %.4f -- full ward deferred)"
              % arith_med)
        check("X2 deferred in smoke (disclosed)", True)

    # ------------------------------------------------------------ A
    section("A -- CXCIII REPRODUCTION at N = 7000 (the ward) + "
            "read collection")
    reads = []          # dicts: r, is_deep, key, sp, pc, ...
    for is_deep, rset in ((False, rungs), (True, deep_rows)):
        for r in rset:
            tg = cons.tail_grid(r["D"], t_c7)
            r["_abel7"] = subg.abel_upper(tg, 1.0 / tg[:-1] ** 2,
                                          n_start=float(N_Z7))
            for A in CUT_A:
                sp = w2.demand_at_head(r, A)
                if sp is None:
                    continue
                reads.append(dict(r=r, deep=is_deep, key=("A", A),
                                  sp=sp,
                                  repro=(not is_deep
                                         or A == A_STR)))
            spB = w2.split_at(r, r["ncB"])
            if spB is not None:
                reads.append(dict(r=r, deep=is_deep,
                                  key=("cB", 0), sp=spB,
                                  repro=True))
    heart7 = -1e18
    recon7 = 0.0
    cont7 = 0.0
    trans7 = 0.0
    sound7 = 0
    slack7 = []
    spot_r = {0, len(rungs) // 2, len(rungs) - 1}
    for i, rd in enumerate(reads):
        r, sp = rd["r"], rd["sp"]
        pc = cons.phi_cont_of(r, sp)
        rd["pc"] = pc
        ph7, tb7 = cons.direct_read(r, sp, pc, gam7, r["_abel7"],
                                    s2t, inv2_7, inv3_7)
        rd["ph7"], rd["tb7"] = ph7, tb7
        rd["mc7"] = sp["fc"] + ph7 - tb7
        recon7 = max(recon7, cons.recon_of(r, sp, pc))
        cont7 = max(cont7, abs(pc["fend"])
                    / max(1.0, pc["fmax"]))
        ri = rungs.index(r) if not rd["deep"] else -1
        if ri in spot_r and rd["key"] == ("cB", 0):
            hj = complex(-np.sum(
                pc["J"] * np.exp(1j * 25.0 * pc["v"]))
                / 25.0 ** 2)
            hs = cons.hat_seg_c(pc["edges"], pc["fvals"],
                                pc["slopes"], 1j * 25.0)
            trans7 = max(trans7, abs(hj - hs)
                         / max(1.0, abs(hj)))
            tb_env = cons.triv_env_pl(pc["edges"], pc["fvals"])
            if abs(pc["triv"]) > tb_env * (1 + 1e-9) + 1e-15:
                cont7 = max(cont7, 1.0)
        resid = sp["par"] - ph7
        rd["resid7"] = resid
        tol_a = cons.RECON_TOL * (1.0 + abs(sp["t_int"]))
        heart7 = max(heart7, (abs(resid) - tb7 - tol_a)
                     / max(1.0, abs(sp["t_int"])))
        slack7.append(math.log10(tb7 / max(abs(resid), 1e-300)))
        if rd["mc7"] > r["m"] * (1.0 + cons.SOUND_TOL) + 1e-15:
            sound7 += 1
        if (i + 1) % 100 == 0:
            print("    ... %d/%d reads  [%.1f s]"
                  % (i + 1, len(reads), time.time() - T0),
                  flush=True)
    check("A1 continuity at the support end (worst %.1e <= %.0e)"
          % (cont7, cons.CONT_TOL), cont7 <= cons.CONT_TOL,
          kill="K3")
    check("A2 bookkeeping recon (worst %.1e <= %.0e, no zeros)"
          % (recon7, cons.RECON_TOL), recon7 <= cons.RECON_TOL,
          kill="K3")
    check("A3 transform ward at gamma = 25 (worst %.1e <= %.0e)"
          % (trans7, cons.TRANS_TOL), trans7 <= cons.TRANS_TOL,
          kill="K3")
    check("A4 THE HEART at N = 7000 on every read (worst scaled "
          "excess %.1e)" % heart7, heart7 <= 0.0, kill="K2")
    check("A5 soundness m_cert <= m (%d violations)" % sound7,
          sound7 == 0, kill="K2")
    print("    heart anatomy (7000): slack %+.2f/%+.2f/%+.2f dex "
          "over %d reads" % (band(np.array(slack7))
                             + (len(slack7),)))

    # the CXCIII censuses on ITS read set
    def census_of(tag_mc, repro_only):
        n_s = n_d = 0
        hf, mg = [], []
        for is_deep, rset in ((False, rungs), (True, deep_rows)):
            for r in rset:
                mine = [rd for rd in reads if rd["r"] is r
                        and (rd["repro"] or not repro_only)]
                best = None
                for A in CUT_A:
                    rd = next((x for x in mine
                               if x["key"] == ("A", A)), None)
                    if rd is not None and rd[tag_mc] > 0.0:
                        best = (A, rd)
                        hf.append(A / r["natom"])
                        break
                if best is None:
                    rdB = next((x for x in mine
                                if x["key"] == ("cB", 0)), None)
                    if rdB is not None and rdB[tag_mc] > 0.0:
                        best = ("cB", rdB)
                        hf.append(rdB["sp"]["natom_head"]
                                  / r["natom"])
                if best is not None:
                    mg.append(math.log10(best[1][tag_mc] / r["m"]))
                    if is_deep:
                        n_d += 1
                    else:
                        n_s += 1
        return n_s, n_d, hf, mg

    n_s7, n_d7, hf7, mg7 = census_of("mc7", True)
    hf7m = float(np.median(np.array(hf7))) if hf7 else float("nan")
    mg7m = float(np.median(np.array(mg7))) if mg7 else float("nan")
    tbm7 = []
    tbm7_d = []
    need7 = []
    for rd in reads:
        if rd["key"] == ("cB", 0):
            v = math.log10(rd["tb7"] / rd["r"]["m"])
            (tbm7_d if rd["deep"] else tbm7).append(v)
            if not rd["deep"]:
                _t, n_req = cons.zeros_needed(rd["r"]["m"],
                                              rd["pc"]["sd"])
                need7.append(n_req)
    tbm7 = np.array(tbm7)
    tbm7_d = np.array(tbm7_d)
    nn7 = np.array(need7)
    lev = tuple(int(np.sum(nn7 <= lv)) for lv in NEED_LEVELS)
    print("    CXCIII reproduction: census %d/%d + %d/%d; head "
          "frac med %.4f; margin med %+.2f dex"
          % (n_s7, N, n_d7, len(deep_rows), hf7m, mg7m))
    print("    blocker at cB (7000): surface %+.2f/%+.2f/%+.2f, "
          "deep med %+.2f, overall max %+.2f dex"
          % (band(tbm7) + (float(np.median(tbm7_d)),
                           max(float(np.max(tbm7)),
                               float(np.max(tbm7_d))))))
    print("    zeros-needed anatomy: med %.3e / max %.3e; "
          "closable at 1e5/1e6/1e7 on %d/%d/%d of %d"
          % (float(np.median(nn7)), float(np.max(nn7)),
             lev[0], lev[1], lev[2], len(nn7)))
    if not SMOKE:
        ok_c = (n_s7, n_d7) == CLOSE7 \
            and abs(hf7m - HAFR7) <= HAFR7_ATOL \
            and abs(mg7m - MARG7) <= MARG7_ATOL
        bb = band(tbm7)
        ok_b = all(abs(bb[i] - BLOCK7[i]) <= BLOCK7_ATOL
                   for i in range(3)) \
            and abs(float(np.median(tbm7_d)) - DEEP7_MED) \
            <= BLOCK7_ATOL \
            and abs(max(float(np.max(tbm7)),
                        float(np.max(tbm7_d))) - BLOCK7_MAX) \
            <= BLOCK7_ATOL
        ok_n = abs(float(np.median(nn7)) / NEED7[0] - 1.0) \
            <= NEED7_RTOL \
            and abs(float(np.max(nn7)) / NEED7[1] - 1.0) \
            <= NEED7_RTOL and lev == LEV7
        check("A6 CXCIII census reproduced (16/67 + 0/8, hafr "
              "0.480, marg -0.39)", ok_c, kill="K2")
        check("A7 CXCIII blocker bands reproduced", ok_b,
              kill="K2")
        check("A8 CXCIII zeros-needed anatomy reproduced", ok_n,
              kill="K2")
    else:
        check("A6 deferred in smoke (disclosed)", True)
        check("A7 deferred in smoke (disclosed)", True)
        check("A8 deferred in smoke (disclosed)", True)
    # Buethe UNCOND baseline
    hafr_s, hafr_d = [], []
    for is_deep, rset in ((False, rungs), (True, deep_rows)):
        for r in rset:
            x = w2.close_cut(r)
            if x is None:
                (hafr_d if is_deep else hafr_s).append(np.nan)
                continue
            i = int(np.searchsorted(r["nn"], x, side="right"))
            (hafr_d if is_deep else hafr_s).append(i / r["natom"])
    hbs = float(np.nanmedian(np.array(hafr_s)))
    hbd = float(np.nanmedian(np.array(hafr_d)))
    n_cl_s = int(np.sum(np.isfinite(np.array(hafr_s))))
    n_cl_d = int(np.sum(np.isfinite(np.array(hafr_d))))
    if not SMOKE:
        check("A9 Buethe UNCOND baseline reproduced (%d/%d at "
              "%.4f, deep %d/%d at %.4f)"
              % (n_cl_s, N, hbs, n_cl_d, len(deep_rows), hbd),
              n_cl_s == N and n_cl_d == len(deep_rows)
              and abs(hbs - HAFR_B) <= HAFR_B_ATOL
              and abs(hbd - HAFR_B_DEEP) <= HAFR_B_ATOL,
              kill="K2")
    else:
        print("    (smoke: UNCOND %d/%d at %.4f, deep %d/%d at "
              "%.4f -- ward deferred)"
              % (n_cl_s, N, hbs, n_cl_d, len(deep_rows), hbd))
        check("A9 deferred in smoke (disclosed)", True)

    # ------------------------------------------------------------ B
    section("B -- THE FULL CLOSURE at N = %d (banded NUFFT "
            "supply, warded)" % N_ZB)
    v_all = np.unique(np.concatenate([rd["pc"]["v"]
                                      for rd in reads]))
    for rd in reads:
        rd["vidx"] = np.searchsorted(v_all, rd["pc"]["v"])
        assert bool(np.all(v_all[rd["vidx"]] == rd["pc"]["v"]))
    print("    unique jump abscissae: %d (v in [%.3f, %.3f])  "
          "[%.1f s]" % (len(v_all), v_all[0], v_all[-1],
                        time.time() - T0))
    F7 = f_transform(gam7, v_all)
    Fb2m = f_transform(gamb[:SEAM_N], v_all)
    Fbhi = f_transform(gamb[SEAM_N:], v_all)
    Fb = Fb2m + Fbhi
    print("    NUFFT transforms done (7000 / 2M / 2e7)  [%.1f s]"
          % (time.time() - T0))
    # W-iii: direct spot ward on the big cache
    sp_idx = np.unique(np.geomspace(1, len(v_all),
                                    NW_SPOTS).astype(int)) - 1
    fdir = f_direct(gamb, v_all[sp_idx])
    fdev = float(np.max(np.abs(Fb[sp_idx] - fdir)))
    fdir7 = f_direct(gam7, v_all[sp_idx])
    fdev7 = float(np.max(np.abs(F7[sp_idx] - fdir7)))
    check("B1 NUFFT spot ward: worst |F_nufft - F_direct| %.2e "
          "(big) / %.2e (7000) <= %.0e at %d spots"
          % (fdev, fdev7, F_ERR_BAR, len(sp_idx)),
          fdev <= F_ERR_BAR and fdev7 <= F_ERR_BAR, kill="K3")
    # W-i: F7-route reproduces the CXCIII zsum on EVERY read
    f7_worst = 0.0
    for rd in reads:
        ph_f, _zs = par_hat_from_f(rd["pc"], F7, rd["vidx"])
        f7_worst = max(f7_worst, abs(ph_f - rd["ph7"])
                       / max(1.0, abs(rd["sp"]["t_int"])))
    check("B2 F7-route == CXCIII zsum4re on all %d reads (worst "
          "%.1e <= %.0e scaled)" % (len(reads), f7_worst,
                                    F7_MATCH),
          f7_worst <= F7_MATCH, kill="K3")
    # W-ii: one full direct big read (smallest support = cheapest)
    r9 = next((r for r in rungs if r["kz"] == CTRL_KZ), None)
    if r9 is None:
        check("B3 no control rung", False, kill="K1")
        return finish({})
    rd9 = next(rd for rd in reads if rd["r"] is r9
               and rd["key"] == ("cB", 0))
    rd_min = min(reads, key=lambda rd: len(rd["pc"]["v"]))
    zs_dir = cons.zsum4re(rd_min["pc"]["v"], rd_min["pc"]["J"],
                          gamb)
    _phm, zs_fm = par_hat_from_f(rd_min["pc"], Fb,
                                 rd_min["vidx"])
    bdev = abs(zs_fm - zs_dir) / max(1.0, abs(zs_dir))
    check("B3 big direct read ward at kz %d %s, %d jumps (dev "
          "%.1e <= %.0e)  [%.1f s]"
          % (rd_min["r"]["kz"], str(rd_min["key"]),
             len(rd_min["pc"]["v"]), bdev, FB_MATCH,
             time.time() - T0),
          bdev <= FB_MATCH, kill="K3")
    # price every read with the big cache (and the 2M prefix)
    heartB = -1e18
    soundB = 0
    slackB = []
    padmax = 0.0
    for rd in reads:
        pc, sp, r = rd["pc"], rd["sp"], rd["r"]
        phB, _ = par_hat_from_f(pc, Fb, rd["vidx"])
        tbB, pad = tailb_of(pc, abel_b, s2t, se2b, se3b)
        rd["phB"], rd["tbB"] = phB, tbB
        rd["mcB"] = sp["fc"] + phB - tbB
        ph2, _ = par_hat_from_f(pc, Fb2m, rd["vidx"])
        tb2, _p2 = tailb_of(pc, abel_2m, s2t, se2m, se3m)
        rd["mc2"] = sp["fc"] + ph2 - tb2
        padmax = max(padmax, pad)
        resid = sp["par"] - phB
        rd["residB"] = resid
        tol_a = cons.RECON_TOL * (1.0 + abs(sp["t_int"]))
        heartB = max(heartB, (abs(resid) - tbB - tol_a)
                     / max(1.0, abs(sp["t_int"])))
        slackB.append(math.log10(tbB / max(abs(resid), 1e-300)))
        if rd["mcB"] > r["m"] * (1.0 + cons.SOUND_TOL) + 1e-15:
            soundB += 1
    check("B4 THE HEART at N = %d on every read (worst scaled "
          "excess %.1e)" % (N_ZB, heartB), heartB <= 0.0,
          kill="K2")
    check("B5 soundness m_cert <= m (%d violations)" % soundB,
          soundB == 0, kill="K2")
    m_min = min(r["m"] for r in rungs + deep_rows)
    check("B6 accuracy demand met: ORD_PAD + NUFFT_PAD max %.2e "
          "vs min m %.2e (%.2f dex under)"
          % (padmax, m_min, math.log10(m_min / padmax)),
          padmax < 0.1 * m_min, kill="K2")
    print("    heart anatomy (2e7): slack %+.2f/%+.2f/%+.2f dex "
          "over %d reads" % (band(np.array(slackB))
                             + (len(slackB),)))

    # THE CENSUS (full ladder; deep gets all cuts, declared)
    n_sB = n_dB = 0
    hfB, mgB = [], []
    tbmB, tbmB_d, needB = [], [], []
    open_rows = []
    print("\n    per-rung certificate at N = %d (A* = smallest "
          "closing head):" % N_ZB)
    print("      kz    h     m         TAILB(cB)   A*    "
          "hfrac   log10(m_cert/m)")
    for is_deep, rset in ((False, rungs), (True, deep_rows)):
        for r in rset:
            mine = [rd for rd in reads if rd["r"] is r]
            best = None
            for A in CUT_A:
                rd = next((x for x in mine
                           if x["key"] == ("A", A)), None)
                if rd is not None and rd["mcB"] > 0.0:
                    best = (str(A), rd, A / r["natom"])
                    break
            rdB = next((x for x in mine
                        if x["key"] == ("cB", 0)), None)
            if best is None and rdB is not None \
                    and rdB["mcB"] > 0.0:
                best = ("cB", rdB,
                        rdB["sp"]["natom_head"] / r["natom"])
            if rdB is not None:
                v = math.log10(rdB["tbB"] / r["m"])
                (tbmB_d if is_deep else tbmB).append(v)
                _t, n_req = cons.zeros_needed(r["m"],
                                              rdB["pc"]["sd"])
                needB.append((n_req, r["kz"]))
            if best is not None:
                if is_deep:
                    n_dB += 1
                else:
                    n_sB += 1
                hfB.append(best[2])
                mgB.append(math.log10(best[1]["mcB"] / r["m"]))
                if r["kz"] in w2.SUBSET or is_deep:
                    print("      %-5d %-5d %.3e %.3e   %-4s  "
                          "%.4f  %+.2f%s"
                          % (r["kz"], r["h"], r["m"],
                             rdB["tbB"] if rdB else float("nan"),
                             best[0], best[2], mgB[-1],
                             "  [deep]" if is_deep else ""))
            else:
                open_rows.append((r, rdB, is_deep))
                print("      %-5d %-5d %.3e %.3e   OPEN  -       "
                      "-%s" % (r["kz"], r["h"], r["m"],
                               rdB["tbB"] if rdB else float("nan"),
                               "  [deep]" if is_deep else ""))
    r_closed_kz_s = set(r["kz"] for r in rungs
                        if not any(o[0] is r for o in open_rows))
    r_closed_kz_d = set(r["kz"] for r in deep_rows
                        if not any(o[0] is r for o in open_rows))
    print("\n    THE CENSUS at N = %d: %d/%d surface + %d/%d deep"
          % (N_ZB, n_sB, N, n_dB, len(deep_rows)))
    if hfB:
        print("    minimal certifying head fraction "
              "%.4f/%.4f/%.4f (CXCIII 7000-census med %.3f, "
              "Buethe route med %.4f); margin log10(m_cert/m) "
              "med %+.2f dex"
              % (band(np.array(hfB)) + (HAFR7, HAFR_B,
                 float(np.median(np.array(mgB))))))
    print("    residual blocker log10(TAILB/m) at cB: surface "
          "%+.2f/%+.2f/%+.2f, deep %+.2f/%+.2f/%+.2f dex"
          % (band(np.array(tbmB)) + band(np.array(tbmB_d))))
    # ECONOMY: the 2M-prefix census (Step-2 measured)
    n_s2 = n_d2 = 0
    for is_deep, rset in ((False, rungs), (True, deep_rows)):
        for r in rset:
            mine = [rd for rd in reads if rd["r"] is r]
            closed = any(rd["mc2"] > 0.0 for rd in mine)
            if closed:
                if is_deep:
                    n_d2 += 1
                else:
                    n_s2 += 1
    print("    DEMAND-SIDE ECONOMY (measured): the free Odlyzko "
          "2M prefix alone closes %d/%d surface + %d/%d deep "
          "(N = %d, T_c = %.1f)"
          % (n_s2, N, n_d2, len(deep_rows), SEAM_N, t_c2m))
    if open_rows:
        print("    OPEN rungs priced:")
        for r, rdB, is_deep in open_rows:
            _t, n_req = cons.zeros_needed(r["m"], rdB["pc"]["sd"])
            print("      kz %-5d%s log10(TAILB/m - residual) "
                  "%+.3f dex; zeros needed ~ %.2e"
                  % (r["kz"], " [deep]" if is_deep else "",
                     math.log10(rdB["tbB"] / r["m"]), n_req))
    if n_sB == N and n_dB == len(deep_rows) and not SMOKE:
        print("\n  " + "*" * 72)
        print("  THE FINITE-SURFACE W2 CLOSURE (per-rung, "
              "direction-conditional):")
        print("  EVERY deployed rung -- 67 surface + 8 deep -- "
              "certifies m > 0 from")
        print("  HEAD + TCONT + the verified-zero PARITH read "
              "with its unconditional")
        print("  tail budget, from cited inputs alone.  "
              "NO RH claim.")
        print("  " + "*" * 72)
    check("B7 census recorded", True)
    # tail law anatomy at the big cache
    hh = np.concatenate([np.log(np.array([float(r["h"])
                                          for r in rungs])),
                         np.log(np.array([float(r["h"])
                                          for r in deep_rows]))])
    yy = np.concatenate([np.array(tbmB), np.array(tbmB_d)])
    b_t, se_t, r2_t = w2.jack_slope(hh, yy)
    print("    tail law at N = %d: log10(TAILB/m) = %+.3f "
          "dex/log h (2SE %.3f, R^2 %.3f; CXCIII saw +0.736 at "
          "N = 7000)" % (N_ZB, b_t, 2 * se_t, r2_t))

    # ------------------------------------------------------------ S
    section("S -- tau screens (CLXXXV jackknife definitions)")
    lm = np.log(np.array([r["m"] for r in rungs]))
    scr = []
    for nm, key in (("c_req_new dex A=%d" % A_STR, ("A", A_STR)),
                    ("c_req_new dex A=12", ("A", 12))):
        yv = []
        for r in rungs:
            rd = next((x for x in reads if x["r"] is r
                       and x["key"] == key), None)
            yv.append(math.log10((abs(rd["phB"]) + rd["tbB"])
                                 / rd["sp"]["fc"])
                      if rd is not None and rd["sp"]["fc"] > 0
                      else np.nan)
        lab, tag = w2.screen_label(nm, lm, np.array(yv))
        scr.append((nm, tag))
        print("    %s" % lab)
    lab, tag = w2.screen_label("log10 TAILB/m at cB", lm,
                               np.array(tbmB))
    scr.append(("log10 TAILB/m at cB", tag))
    print("    %s" % lab)
    check("S1 screens recorded", True)

    # ------------------------------------------------------------ M
    section("M -- controls (must fire)")
    lam_sm = np.array([r["lam_sm"] for r in rungs])
    check("M1 smooth world breaks the wall on %d/%d (max %+.1e)"
          % (int(np.sum(lam_sm < 0)), N, float(lam_sm.max())),
          bool(np.all(lam_sm < 0)), kill="K2")
    NE = int(math.floor(math.exp(2.0 * r9["alpha"]))) + 1
    lamE = w2.lambda_eps(NE)
    nz = np.nonzero(np.abs(lamE) > 1e-12)[0]
    cE = (np.log(nz.astype(float)),
          2.0 * lamE[nz] / np.sqrt(nz.astype(float)))
    rE = w2.build_rung(CTRL_KZ, comb=cE)
    rS = w2.build_rung(CTRL_KZ, scramble_seed=1)
    check("M2 Epstein + scramble break lam_min at kz %d "
          "(%+.1e, %+.1e)" % (CTRL_KZ, rE["m"], rS["m"]),
          rE["m"] < 0 and rS["m"] < 0, kill="K2")
    fired = tried = 0
    for key in (("cB", 0), ("A", A_STR)):
        rd = next((x for x in reads if x["r"] is r9
                   and x["key"] == key), None)
        if rd is None:
            continue
        tried += 1
        sp = rd["sp"]
        keep = rS["uu"] > math.log(sp["nc"]) + 1e-12
        t_scr = float(np.dot(
            np.asarray(rS["mu"], float)[keep],
            w2.q_read(r9["Wv"], rS["uu"][keep], r9["D"],
                      r9["M"])))
        par_scr = t_scr - sp["tcont"]
        exc = abs(par_scr - rd["phB"]) / rd["tbB"]
        print("    scramble read at %s: |PARITH_scr - "
              "PARITH_hat| / TAILB = %.1e -> %s"
              % (str(key), exc, "FIRES" if exc > 1 else "silent"))
        if exc > 1.0:
            fired += 1
    check("M3 CONTROL C-i: scramble breaks the heart on %d/%d "
          "control cuts (big TAILB)" % (fired, tried),
          tried >= 1 and fired == tried, kill="K2")
    pc9 = rd9["pc"]
    g1 = float(gamb[0])
    on_pair = 4.0 * float((-np.sum(
        pc9["J"] * np.exp(1j * g1 * pc9["v"])) / g1 ** 2).real)
    dlt = IMP_BETA - 0.5
    quad = 4.0 * (cons.hat_seg_c(pc9["edges"], pc9["fvals"],
                                 pc9["slopes"],
                                 dlt + 1j * g1).real
                  + cons.hat_seg_c(pc9["edges"], pc9["fvals"],
                                   pc9["slopes"],
                                   -dlt + 1j * g1).real)
    shift = abs((-quad) - (-on_pair))
    ratio = shift / max(abs(rd9["residB"]), 1e-300)
    check("M4 CONTROL C-ii: off-line impostor (gamma_1 -> beta "
          "%.2f) shifts PARITH_hat by %.4f = %.1e x the genuine "
          "big-cache residual (>= %.0f)"
          % (IMP_BETA, shift, ratio, IMP_RATIO_MIN),
          ratio >= IMP_RATIO_MIN, kill="K2")

    # ------------------------------------------------------------ C
    section("C -- THE COMPOSED WALL CENSUS (B + W1 + W2 by "
            "window kz)")
    import exterior_pg_schur_probe as parent  # noqa: E402
    _z, _t, _f, prows = parent.build_truth_rows()
    w1b_surf = set(int(p["r2"]["kz"]) for p in prows)
    check("C1 W1/B surface ladder re-enumerated (%d == %d kz)"
          % (len(w1b_surf), PARENT_ROWS),
          len(w1b_surf) == PARENT_ROWS, kill="K1")
    w2_surf_kz = set(r["kz"] for r in rungs)
    inter_s = sorted(w2_surf_kz & w1b_surf)
    comp_s = sorted(set(inter_s) & r_closed_kz_s)
    comp_d = sorted(set(elig_kz) & r_closed_kz_d)
    print("    W2 surface ladder %d kz; W1/B ladder %d kz; "
          "intersection %d" % (len(w2_surf_kz), len(w1b_surf),
                               len(inter_s)))
    print("    deep: W2 rungs are %d of the %d eligible "
          "ext-frame rungs; W1 deep 28/28 (CLXXXIV, CITED), "
          "B deep 27/27 steps covering all eligible rungs "
          "(CLXXVII, CITED)" % (len(deep_rows), len(elig_kz)))
    print("    COMPOSED: on %d/%d matched surface rungs + %d/%d "
          "deep rungs the ENTIRE wall (B-half CLXXVII + W1 "
          "CLXXXIX + W2 this run) is certified from cited inputs"
          % (len(comp_s), len(inter_s), len(comp_d),
             len(deep_rows)))
    print("      surface kz: %s" % comp_s)
    print("      deep    kz: %s" % comp_d)
    w2_only = sorted(w2_surf_kz - w1b_surf)
    print("    W2-only surface rungs (outside the W1/B ladder, "
          "wall face W2 alone): %d closed of %d (kz %s...)"
          % (len(set(w2_only) & r_closed_kz_s), len(w2_only),
             w2_only[:12]))
    check("C2 composed census recorded", True)

    # ------------------------------------------------------ verdicts
    v1 = ("CACHE-CERTIFIED(N = %d: Odlyzko 2,001,052 + LMFDB %d; "
          "corridor %d/%d, Backlund %.2f, overlap %.1e, worst "
          "zeta spot %.1e)"
          % (N_ZB, N_ZB - SEAM_N, n_ok, N_ZB, s_dev, dev7,
             worst_z))
    v2 = ("CXCIII-REPRODUCED(%d/%d + %d/%d at N = 7000; hafr "
          "%.3f; blocker %+.2f/%+.2f/%+.2f)"
          % ((n_s7, N, n_d7, len(deep_rows), hf7m) + band(tbm7)))
    full = n_sB == N and n_dB == len(deep_rows)
    if full:
        v3 = ("W2-FINITE-SURFACE-CLOSED(%d/%d + %d/%d; head "
              "fraction %.4f/%.4f/%.4f, was 0.953 Buethe / 0.480 "
              "CXCIII-partial; margin med %+.2f dex; economy: 2M "
              "prefix alone closes %d + %d)"
              % ((n_sB, N, n_dB, len(deep_rows))
                 + band(np.array(hfB))
                 + (float(np.median(np.array(mgB))), n_s2, n_d2)))
    else:
        mx_open = max((math.log10(o[1]["tbB"] / o[0]["m"])
                       for o in open_rows), default=float("nan"))
        pz = max((cons.zeros_needed(o[0]["m"],
                                    o[1]["pc"]["sd"])[1]
                  for o in open_rows), default=float("nan"))
        v3 = ("W2-FULLCLOSE-PARTIAL(%d/%d + %d/%d at N = %d; "
              "worst open blocker %+.2f dex; remainder priced "
              "~ %.1e zeros)"
              % (n_sB, N, n_dB, len(deep_rows), N_ZB, mx_open,
                 pz))
    v4 = ("WALL-COMPOSED(%d/%d matched surface + %d/%d deep "
          "rungs carry B + W1 + W2 from cited inputs; %d W2-only "
          "surface rungs closed besides)"
          % (len(comp_s), len(inter_s), len(comp_d),
             len(deep_rows), len(set(w2_only) & r_closed_kz_s)))
    if fired == tried and tried >= 1 and ratio >= IMP_RATIO_MIN:
        v5 = ("DISCRIMINATION-FIRES(scramble %d/%d, impostor "
              "%.0e x, smooth %d/%d, Epstein+scramble lam < 0) "
              "+ SCREENS(%s)"
              % (fired, tried, ratio, int(np.sum(lam_sm < 0)), N,
                 ", ".join("%s %s" % ab for ab in scr)))
    else:
        v5 = "DISCRIMINATION-UNRESOLVED(scr %d/%d, imp %.1f)" \
            % (fired, tried, ratio)
    check("V1 typed: %s" % v1, True)
    check("V2 typed: %s" % v2, True)
    check("V3 typed: %s" % v3, True)
    check("V4 typed: %s" % v4, True)
    check("V5 typed: %s" % v5, True)
    return finish(dict(v1=v1, v2=v2, v3=v3, v4=v4, v5=v5))


if __name__ == "__main__":
    raise SystemExit(main())
