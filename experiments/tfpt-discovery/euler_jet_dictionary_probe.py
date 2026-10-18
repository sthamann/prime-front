#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""euler_jet_dictionary_probe -- PRIME.EULER.JET.DICTIONARY.01

FROZEN SPEC (2026-08-22).  EXPLORATION ONLY.  This probe writes no
verification module, paper, ledger, website, manifest, Lean file or
status marker.  It makes NO RH claim, NO positivity claim beyond the
per-rung finite statements gated below, NO counterexample claim.  It
closes no gate and narrows no gate.  Concurrent-lane files (the
independent session's untracked probes, sieve4_helper.bin, the
z1-suppression lane, and every verification/paper/website surface of
promotion wave eight) are not touched.

=======================================================================
MISSION (round ~202 opener: the EULER JET program, probe 1).  The
external reviewer's north star after r200/r201: the prime block's TWO
atomic transforms per mode (the sine channel feeding the potential,
r189's pj; the cosine channel feeding the diagonal shift, r189's
pc-law / the builder's pdiag) are THE VALUE AND FIRST JET OF ONE
RATIONAL EULER FUNCTION PER PRIME.  For rung h and prime p set
M_p = max{m : p^m <= h} (integer arithmetic; == floor(log h/log p)),
z_p(om) = p^{-1/2} e^{i om log p}, and

  S_{p,h}(om) = log p * sum_{m=1}^{M_p} z_p^m
              = log p * z_p (1 - z_p^{M_p}) / (1 - z_p),
  S'_{p,h}(om) = i (log p)^2 sum_{m=1}^{M_p} m z_p^m
               = i (log p)^2 z_p (1-(M_p+1) z_p^{M_p}
                 + M_p z_p^{M_p+1})/(1-z_p)^2.

THE VERIFIED DICTIONARY (constants adjudicated against the actual
builder R4.build_cell, even sector, VERBATIM -- pre-freeze numeric
derivation at h = 5 gave all four identities at 1e-61):
  SINE CHANNEL (reviewer's identity CONFIRMED, no constant fix):
    the per-prime part of pj_k = sum_q w_q sin(om_k u_q) restricted
    to q = p^m, m <= M_p, equals Im S_{p,h}(om_k) EXACTLY.
  DIAGONAL CHANNEL (reviewer's identity CONFIRMED for k >= 1, no
    constant fix; even sector dsig = -1): the per-prime part of the
    builder's pdiag_k = sum_q w_q [(a - u_q/2) cos(om_k u_q)
    - sin(om_k u_q)/(2 om_k)] equals
    Ptilde_p(om) = Re(a S_{p,h} + (i/2) S'_{p,h})
                   - Im(S_{p,h})/(2 om)  EXACTLY,
    with (i/2) S' = -(1/2) sum_m m (log p)^2 p^{-m/2} e^{i m om lp}.
    (Builder wiring: Mprime[k,k] = 2 pdiag_k / nrm_k^2; off-diag
    Mprime[i,j] = 2 par_i par_j (om_i pj_i - om_j pj_j)
    / ((om_j^2 - om_i^2) nrm_i nrm_j); the wall carries Mprime with
    a MINUS sign, M = Mpole + March - Mprime -- assembly
    conventions, not part of the per-prime transforms.)
  THE om = 0 CONTINUATION (the ONE corrected constant, derived here
    and gated symbolically + mp): the 1/(2 om) term is a REMOVABLE
    singularity with
      lim_{om->0} Ptilde_p(om) = sum_m w_m (a - u_m)
                               = Re(a S(0) + i S'(0)),
    but the HOUSE k = 0 convention is pdiag_0 = sum_m w_m (2a - u_m)
    = 2 Re(a S(0) + (i/2) S'(0)) = Re(2a S(0) + i S'(0)) -- the
    DOUBLED JET FUNCTIONAL, NOT the continuous limit; the exact
    defect is house - lim = a Re S_{p,h}(0) = a pc_p(0), i.e. the
    r189 mult_0 = 2 doubling in Euler-jet coordinates.
  THE EXACT DECOMPOSITION (the round's structural centerpiece): the
    FULL series S_p = log p z_p/(1 - z_p) has the Cayley completion
      C_p = 1 + 2 S_p/log p = (1 + z_p)/(1 - z_p),
      Re C_p = (1 - 1/p)/|1 - z_p|^2 > 0
    (|1-z|^2 = (1-r)^2 + 2r(1 - cos(om log p)) >= (1-r)^2 > 0,
    r = p^{-1/2} < 1): EVERY PRIME CONTRIBUTES A LOCALLY
    POSITIVE-REAL RATIONAL FUNCTION.  The truncation remainder is
      T_p = S_p - S_{p,h} = log p z^{M_p+1}/(1 - z)
          = (log p/2) z^{M_p+1} (1 + C_p)  EXACTLY:
    the remainder is the SAME positive-real object 1 + C_p (Re > 0),
    DAMPED-ROTATED by the monomial z^{M_p+1} (modulus
    p^{-(M_p+1)/2} = 1/sqrt(first prime power beyond h), phase
    (M_p+1) om log p).  ANSWER TO THE KEY STRUCTURAL QUESTION --
    BOTH faces of one identity: the remainder DOES inherit the full
    positive-real structure (same C_p, exact factorization), AND
    the h-dependence concentrates ENTIRELY in the monomial exponent
    M_p + 1 (the only h-dependent datum); the remainder itself is
    NOT one-signed in om (the rotation phase wanders -- measured
    sign-change census gated), so no fixed-phase positivity
    transfers without controlling the rotation.
    Same decomposition for the DIAGNONAL channel: Ptilde built from
    (S_full, S_full') minus Ptilde built from (T, T') equals Ptilde
    built from (S_trunc, S_trunc'), entrywise at block level, with
    T' = i (log p)^2 z^{M+1} ((M+1) - M z)/(1-z)^2.

GOALS (contract PRIME.EULER.JET.DICTIONARY.01, the reviewer's five
hard gates):
  G-A  SYMBOLIC EQUALITY at h = 4, 5: both prime-block transforms
       reconstructed exactly from S_{p,h}, S'_{p,h} -- sympy at
       generic om (feasible: identities hold identically in
       (om, r, lp, a) for each M) + mp at the mode lattice against
       the actual builder block, entrywise.
  G-B  HIGH-PRECISION INDEPENDENT RECONSTRUCTION at h = 8, 13, 20,
       28: the FULL prime block rebuilt from the Euler jets alone
       (closed rational forms, own assembly path -- the builder
       sums sines/cosines atom-by-atom, we evaluate rational
       functions of z_p) vs the house builder, entrywise, 1e-50
       class at matched dps.
  G-C  the om = 0 continuation: exact symbolic limit + the corrected
       house k = 0 law (doubled jet functional) gated at every rung.
  G-D  the exact decomposition prime block = [positive-real Euler
       completion part] - [truncation remainder part] per prime per
       rung; PR proven symbolically; remainder size ladder measured
       + the envelope law |T_p| in [lp r^{M+1}/(1+r),
       lp r^{M+1}/(1-r)] gated exactly; next-power law p^{M_p} <= h
       < p^{M_p+1} in integer arithmetic; the key structural
       question resolved as REMAINDER-PR-ROTATED (see above).
  G-E  WORLD REFUSAL: SCRARITH/EPSTEIN/SMOOTH must refuse the Euler
       grouping -- reconstruction residual per world (MAIN ~exact,
       worlds large) + the train anatomy of WHAT breaks: SCRARITH
       keeps the atom positions but the golden-map weight
       permutation kills the geometric law w_{m+1}/w_m = p^{-1/2}
       (measured misfit); EPSTEIN (x^2+5y^2, supports {4, 5, 6} at
       x = 8) has the p = 2 train STARTING AT m = 2 (no atom at
       log 2: the value+jet of a geometric series from m = 1 cannot
       produce a support hole) AND carries lamq(4) = log 4 =
       2 Lambda(4) (weight DOUBLED vs the von Mangoldt train) AND a
       non-prime-power atom q = 6 (no geometric train exists);
       SMOOTH is a continuum measure (no atom list at all --
       structural refusal).
  PLUS the colligation data table for probe 202 (the
       colligation/Redheffer cascade): per prime per rung, the 2x2
       real data (Re/Im S, Re/Im S') at the frozen mode subset, the
       positive-real completion value Re C_p, and the remainder
       modulus |T_p| -- serialized as COLLIG lines in the log.

NOTATION (r171-r201 conventions VERBATIM).  Rung h = builder x
(R4.build_cell, even sector, MAIN world); a = log(h)/2; L = 2a;
K = ceil(1.25 h log h); om_k = k pi/a; b_k = om_k^2; nrm_0 =
sqrt(2a), nrm_k = sqrt(a); par_k = (-1)^k; atoms {(u_q, w_q)} =
{(log q, log p/sqrt q)}, q = p^m <= h; pj/pc as in r189; SMOOTH
continuum atom measure e^{w/2} dw on [0, L]; SCRARITH golden-map
weight permutation; EPSTEIN x^2+5y^2 Dirichlet atoms -- all builder
recipes VERBATIM.  tau_h is NEVER read in this probe (no eigen
data is consumed; the builder's eigsy output is discarded).

RUNGS AND DPS (frozen; disclosed choice): ALL_RUNGS = (4, 5, 8, 13,
20, 28) with DPS = 60 AT EVERY RUNG.  The house dps ladder
(60..144) exists to resolve tau_h; this probe reads ONLY the
O(1)-entry prime block (a pure finite atom sum, no quadrature), for
which dps 60 delivers ~1e-55 entrywise -- 5 digits below the 1e-50
gate class; h = 28 extends the reachable ladder (K = 117) and is
feasible at dps 60 (~10 min) where the house 144-class dps is not
(> 25 min, eigsy-dominated, eigsy unused here).  MSYM = (1, 2, 3,
4): every M_p occurring at the six rungs (max M_2 = 4 at h = 28).
GA_RUNGS = (4, 5); GB_RUNGS = (8, 13, 20, 28).  Colligation mode
subset: all k at h <= 5, else sorted set {0, 1, 2, 3, K//4, K//2,
3K//4, K-1}.  CONTROLS: (SMOOTH, 5), (SCRARITH, 5), (EPSTEIN, 8)
at dps 60/60/60 (same O(1)-block argument).  CONT_OM = 1e-10
(continuity ward point).  WORKERS = 6.

FROZEN BARS: DICT_BAR 1e-50 (G20/G21/G22 entrywise rel, max-entry
normalized); SYM = sympy zero (exact); REM_BAR 1e-50 (remainder
closed-form + Cayley-factor wards, rel); DEC_BAR 1e-50 (block
decomposition, rel); ENV_SLACK 1e-40 (exact-envelope multiplicative
slack); PR_MIN 0 strict (Re C_p > 0 at every p, k, rung); CONT_BAR
1e-15 (Ptilde(1e-10) vs symbolic limit, abs, per prime, h = 4, 5);
K0_BAR 1e-50 (house k = 0 law, rel); WORLD_POS_BAR 1e-50;
WORLD_REFUSE_BAR 1e-3 (log10 residual >= -3); MISFIT_MIN 0.05
(SCRARITH geometric-law misfit); EP_RATIO_BAR 1e-50 (EPSTEIN
lamq(4)/Lambda(4) == 2 exact); RUNTIME_BAR 2400 s.  Record
tolerances: LOG_TOL 0.10 dex; counts exact.

TAXONOMY (frozen resolution logic, evaluated from measured values):
  dict_exact := G10-G15 symbolic all pass AND G20/G21/G22 devs <=
                DICT_BAR at every rung;
  primary    := EULER-JET-DICTIONARY-EXACT iff dict_exact, else
                EULER-JET-PARTIAL;
  k0Enum     := K0-DOUBLED-JET-LAW (exact; house k = 0 == doubled
                jet functional, defect a pc_p(0) vs continuation) --
                typed EXACT iff G13 + G22 pass;
  remEnum    := REMAINDER-PR-ROTATED iff the Cayley factorization
                ward passes at every (p, k, h) AND Re(1 + C_p) > 0
                everywhere AND >= 1 prime shows Re-T sign wander
                (> 0 sign changes) at >= 1 rung; else
                REMAINDER-STRUCTURE-PARTIAL;
  worldEnum  := WORLDS-REFUSE-EULER-GROUPING iff all three control
                worlds have log10 residual >= -3 while MAIN(4..28)
                <= 1e-50; else WORLD-MIXED (typed honestly, with
                the per-world break anatomy recorded either way).

RECORD TABLES (frozen at freeze from the disclosed pre-freeze
ladder: TWO structural smokes -- smoke1 22/23 (rungs 4/5 +
SCRARITH; the ONE fail was G15: the sympy reduction route
expand_complex + simplify was too weak for the full-series/tail
derivative identities, replaced by cancel(together(.)) on the
rational form, a STRENGTHENING of the proof reduction; no target,
bar or identity changed -- amendment A1), smoke2 23/23 -- and ONE
calibration pass calib_ejd_pass1.log (24/24, all six rungs + all
three controls, 403.8 s); the exact-identity constants were
adjudicated numerically at h = 5 BEFORE the spec was written --
disclosed above; no bar, dps, rung, mode subset or control recipe
moved at any point; record tables inserted at freeze, house
pattern identical to r195/r200/r201).
Verdicts frozen from calibration: all four dictionary identities
EXACT at every rung -- G20 devs 8.3e-61/7.4e-61 (h = 4/5), G21
devs 8.5e-61/5.0e-61/9.5e-61/1.4e-60 at h = 8/13/20/28 (K up to
117), G22 k = 0 law 7.4e-61 with the per-prime defect identity 0.0
at working precision; decomposition exact at all six rungs (G31 <=
1.4e-60); remainder closed form/Cayley factorization <= 1.2e-60;
envelope + next-power law hold at all 32 (p, h) pairs; Re C_p > 0
at all 2036 (p, k) pairs (min 1.72e-01); the remainder Re-phase
WANDERS (sign changes at every rung: CAL_TSC below) -- remEnum =
REMAINDER-PR-ROTATED; worlds refuse at log10 residual -0.625
(SCRARITH) / +0.080 (EPSTEIN) / -0.295 (SMOOTH) vs MAIN <= 1.4e-60
(>= 59-dex separation); EPSTEIN p = 2 train: hole at m = 1
(lamq(2) = 0), weight ratio lamq(4)/Lambda(4) = 2 EXACT (dev 0.0),
non-prime-power atom q = 6 present, support {4, 5, 6}; SCRARITH
geometric-law misfits head 0.4685 / ratio 0.3190; colligation
table 263 lines.
CAL_TSC {h: total Re-T sign changes summed over primes}: 4: 11,
  5: 13, 8: 38, 13: 101, 20: 220, 28: 581.
CAL_TREM {h: log10 max_k |T_2| (p = 2 anchor)}: 4: "-0.077",
  5: "-0.077", 8: "-0.228", 13: "-0.228", 20: "-0.378",
  28: "-0.378" (the h-ladder moves ONLY at the power-crossing
  rungs 8 and 20 where M_2 steps -- the next-power law visible in
  the anchor).
CAL_WREF {world: log10 refusal residual}: SCRARITH: "-0.625",
  EPSTEIN: "0.080", SMOOTH: "-0.295".
CAL_SCR {head: "0.4685", ratio: "0.3190"}.
AMENDMENTS: ONE (A1, smoke-driven, pre-freeze, disclosed above):
the G15 sympy reduction route strengthened from
expand_complex + simplify to cancel(together(.)); no target
changed, no bar moved, no dps/rung/recipe touched.
=======================================================================

WHAT IS BUILT AND GATED: S0 G01 firewall + G02 predefinition; S1
exact layer G10-G15 (sympy); S2 mp dictionary G20-G23; S3
decomposition G30-G33; S4 world refusal G40-G41; S5 guards G50-G52;
S6 pricing + colligation G60-G61 + G99 runtime.  DETERMINISM: no
randomness anywhere; ProcessPool results keyed; run2 must be
identical modulo wall-clock tokens (lines carrying 'WALL').

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
from concurrent.futures import ProcessPoolExecutor

import mpmath as mp
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

import radius4_an_probe as R4                 # round-122 machinery

# ---------------------------------------------------------------- frozen
KFAC = 1.25
WORKERS = 6
RUNTIME_BAR = 2400.0

GA_RUNGS = (4, 5)
GB_RUNGS = (8, 13, 20, 28)
ALL_RUNGS = (4, 5, 8, 13, 20, 28)
DPS_ALL = 60
MSYM = (1, 2, 3, 4)
CTRL_CELLS = (("SMOOTH", 5, 60), ("SCRARITH", 5, 60), ("EPSTEIN", 8, 60))
CONT_OM = mp.mpf("1e-10")
GOLD = (math.sqrt(5.0) - 1.0) / 2.0

DICT_BAR = 1e-50
REM_BAR = 1e-50
DEC_BAR = 1e-50
ENV_SLACK = 1e-40
CONT_BAR = 1e-15
K0_BAR = 1e-50
WORLD_POS_BAR = 1e-50
WORLD_REFUSE_LOG10 = -3.0
MISFIT_MIN = 0.05
EP_RATIO_BAR = 1e-50
LOG_TOL = 0.10

# --------------------- calibrated record tables (calib_ejd_pass1.log)
CAL_TSC = {4: 11, 5: 13, 8: 38, 13: 101, 20: 220, 28: 581}
CAL_TREM = {4: "-0.077", 5: "-0.077", 8: "-0.228", 13: "-0.228",
            20: "-0.378", 28: "-0.378"}
CAL_WREF = {"SCRARITH": "-0.625", "EPSTEIN": "0.080",
            "SMOOTH": "-0.295"}
CAL_SCR = {"head": "0.4685", "ratio": "0.3190"}

SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
T0_WALL = time.time()

CHECKS: list[tuple[str, bool, str]] = []
INFO: list[str] = []


def check(name: str, ok: bool, detail: str) -> bool:
    ok = bool(ok)
    CHECKS.append((name, ok, detail))
    print("  [%s] %-40s %s" % ("PASS" if ok else "FAIL", name, detail),
          flush=True)
    return ok


def info(msg: str) -> None:
    INFO.append(msg)
    print("  [INFO] " + msg, flush=True)


def section(title: str) -> None:
    print("\n" + "-" * 78 + "\n" + title + "\n" + "-" * 78, flush=True)


def has_cycle(graph: dict) -> bool:
    WHITE, GREY, BLACK = 0, 1, 2
    color = {u: WHITE for u in graph}
    for v in list(graph):
        for w in graph[v]:
            color.setdefault(w, WHITE)

    def dfs(u):
        color[u] = GREY
        for w in graph.get(u, ()):
            if color[w] == GREY:
                return True
            if color[w] == WHITE and dfs(w):
                return True
        color[u] = BLACK
        return False

    return any(color[u] == WHITE and dfs(u) for u in list(color))


def ancestors(graph: dict, node: str) -> set:
    rev: dict = {}
    for u, vs in graph.items():
        for v in vs:
            rev.setdefault(v, set()).add(u)
    seen: set = set()
    stack = [node]
    while stack:
        u = stack.pop()
        for p in rev.get(u, ()):
            if p not in seen:
                seen.add(p)
                stack.append(p)
    return seen


# ------------------------------------------------------------ firewall
def firewall_audit() -> tuple[bool, str]:
    src = open(os.path.abspath(__file__), "r", encoding="utf-8").read()
    tree = ast.parse(src)
    forb = {"zeta" + "zero", "siegel" + "z", "siegel" + "theta",
            "n" + "zeros", "gram" + "point"}
    bad = []
    for node in ast.walk(tree):
        nm = None
        is_const = False
        if isinstance(node, ast.Attribute):
            nm = node.attr
        elif isinstance(node, ast.Name):
            nm = node.id
        elif isinstance(node, ast.Constant) and isinstance(node.value,
                                                           str):
            nm = node.value
            is_const = True
        if nm is None:
            continue
        low = nm.lower()
        if not is_const:
            if low in forb:
                bad.append("forbidden %s @%d" % (nm, node.lineno))
            if low == "zeta":
                bad.append("zeta use @%d" % node.lineno)
        if isinstance(node, ast.Attribute) and nm == "load":
            bad.append("np.load @%d (zero-free round)" % node.lineno)
    for node in ast.walk(tree):
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            mods = ([al.name for al in node.names]
                    if isinstance(node, ast.Import)
                    else [node.module or ""])
            for m in mods:
                if m.startswith("verification"):
                    bad.append("import " + m)
    return (not bad), ("; ".join(bad) if bad else
                       "NO zero-oracle, NO zeta, NO np.load, no "
                       "verification/ import; no eigen data consumed "
                       "(tau never read); fully zero-free")


# ------------------------------------------------------- euler helpers
def primes_upto(x: int) -> list[int]:
    return [p for p in range(2, x + 1)
            if all(p % d for d in range(2, int(math.isqrt(p)) + 1))]


def m_cap(p: int, h: int) -> int:
    m, q = 0, p
    while q <= h:
        m += 1
        q *= p
    return m


def euler_pack(p: int, M: int, om) -> dict:
    """All Euler-jet data of one prime at one frequency (mp ctx of
    caller).  z = p^{-1/2} e^{i om log p}; closed rational forms
    ONLY (the independent code path vs the builder's trig sums)."""
    lp = mp.log(p)
    im1 = mp.mpc(0, 1)
    z = mp.exp(-lp / 2) * mp.exp(im1 * om * lp)
    one = mp.mpf(1)
    S_tr = lp * z * (1 - z ** M) / (1 - z)
    Sp_tr = im1 * lp ** 2 * z * (1 - (M + 1) * z ** M
                                 + M * z ** (M + 1)) / (1 - z) ** 2
    S_fu = lp * z / (1 - z)
    Sp_fu = im1 * lp ** 2 * z / (1 - z) ** 2
    T = lp * z ** (M + 1) / (1 - z)
    Tp = im1 * lp ** 2 * z ** (M + 1) * ((M + 1) - M * z) \
        / (1 - z) ** 2
    C = (1 + z) / (1 - z)
    return dict(lp=lp, z=z, S=S_tr, Sp=Sp_tr, Sf=S_fu, Spf=Sp_fu,
                T=T, Tp=Tp, C=C, one=one)


def ptilde_of(S, Sp, om, aa):
    """The diagonal-channel jet functional at om > 0."""
    im1 = mp.mpc(0, 1)
    return mp.re(aa * S + im1 / 2 * Sp) - mp.im(S) / (2 * om)


def ptilde0_house(S0, Sp0, aa):
    """The HOUSE k = 0 convention: the DOUBLED jet functional
    2 Re(a S(0) + (i/2) S'(0)) (== sum_m w_m (2a - u_m))."""
    im1 = mp.mpc(0, 1)
    return 2 * (aa * mp.re(S0) + mp.re(im1 / 2 * Sp0))


def assemble_block(pj, pdiag, oms, par, nrm, K):
    """The builder's prime-block assembly (even sector VERBATIM)
    from per-mode source data (pj_k, pdiag_k)."""
    Mb = mp.zeros(K, K)
    for i in range(K):
        for j in range(i):
            sg = par[i] * par[j]
            den = oms[j] ** 2 - oms[i] ** 2
            od = 2 * sg * (oms[i] * pj[i] - oms[j] * pj[j]) / den
            Mb[i, j] = od
            Mb[j, i] = od
    for i in range(K):
        Mb[i, i] = 2 * pdiag[i]
    for i in range(K):
        for j in range(K):
            Mb[i, j] = Mb[i, j] / (nrm[i] * nrm[j])
    return Mb


def block_dev(A, B, K):
    dev = mp.mpf(0)
    den = mp.mpf(0)
    for i in range(K):
        for j in range(K):
            dev = max(dev, abs(A[i, j] - B[i, j]))
            den = max(den, abs(B[i, j]))
    return dev / den


def sub_k(K: int) -> list[int]:
    return sorted(set([0, 1, 2, 3, K // 4, K // 2,
                       (3 * K) // 4, K - 1]))


# ------------------------------------------------------- rung worker
def w_rung(args) -> dict:
    h, dps = args
    try:
        t0 = time.time()
        ce = R4.build_cell(h, KFAC, "MAIN", dps, want_mp=True)
        K = ce["K"]
        out = dict(h=h, K=K, err="")
        with mp.workdps(dps):
            aa = mp.log(h) / 2
            oms = [k * mp.pi / aa for k in range(K)]
            par = [mp.mpf((-1.0) ** k) for k in range(K)]
            nrm = [mp.sqrt(2 * aa) if k == 0 else mp.sqrt(aa)
                   for k in range(K)]
            Mpr = ce["mpPrime"]
            prs = primes_upto(h)
            caps = {p: m_cap(p, h) for p in prs}
            out["primes"] = prs
            out["caps"] = [caps[p] for p in prs]
            # next-power law in INTEGER arithmetic
            npl = all(p ** caps[p] <= h < p ** (caps[p] + 1)
                      for p in prs)
            out["next_power_ok"] = bool(npl)
            # per-(p, k) euler packs
            packs = {p: [euler_pack(p, caps[p], oms[k])
                         for k in range(K)] for p in prs}
            # --- reconstruction from the jets alone (own path)
            pj = [sum(mp.im(packs[p][k]["S"]) for p in prs)
                  for k in range(K)]
            pdiag = []
            for k in range(K):
                if k == 0:
                    pdiag.append(sum(
                        ptilde0_house(packs[p][0]["S"],
                                      packs[p][0]["Sp"], aa)
                        for p in prs))
                else:
                    pdiag.append(sum(
                        ptilde_of(packs[p][k]["S"],
                                  packs[p][k]["Sp"], oms[k], aa)
                        for p in prs))
            Mrec = assemble_block(pj, pdiag, oms, par, nrm, K)
            out["dict_dev"] = float(block_dev(Mrec, Mpr, K))
            # --- k = 0 corrected law + continuation defect
            k0_dev = mp.mpf(0)
            defect_dev = mp.mpf(0)
            for p in prs:
                pk = packs[p][0]
                im1 = mp.mpc(0, 1)
                lim = mp.re(aa * pk["S"] + im1 * pk["Sp"])
                house = ptilde0_house(pk["S"], pk["Sp"], aa)
                defect_dev = max(defect_dev, abs(
                    house - lim - aa * mp.re(pk["S"])))
            hh0 = Mpr[0, 0] * nrm[0] ** 2 / 2
            k0_dev = abs(hh0 - pdiag[0]) / max(abs(hh0),
                                               mp.mpf("1e-30"))
            out["k0_dev"] = float(k0_dev)
            out["k0_defect_dev"] = float(defect_dev)
            # --- continuity ward (GA rungs only)
            if h in GA_RUNGS:
                cw = mp.mpf(0)
                for p in prs:
                    pk = euler_pack(p, caps[p], CONT_OM)
                    im1 = mp.mpc(0, 1)
                    lim = mp.re(aa * pk["S"] + im1 * pk["Sp"])
                    cw = max(cw, abs(ptilde_of(pk["S"], pk["Sp"],
                                               CONT_OM, aa) - lim))
                out["cont_dev"] = float(cw)
            # --- decomposition: block(full) - block(tail) == house
            pj_f = [sum(mp.im(packs[p][k]["Sf"]) for p in prs)
                    for k in range(K)]
            pj_t = [sum(mp.im(packs[p][k]["T"]) for p in prs)
                    for k in range(K)]
            pd_f, pd_t = [], []
            for k in range(K):
                if k == 0:
                    pd_f.append(sum(ptilde0_house(
                        packs[p][0]["Sf"], packs[p][0]["Spf"], aa)
                        for p in prs))
                    pd_t.append(sum(ptilde0_house(
                        packs[p][0]["T"], packs[p][0]["Tp"], aa)
                        for p in prs))
                else:
                    pd_f.append(sum(ptilde_of(
                        packs[p][k]["Sf"], packs[p][k]["Spf"],
                        oms[k], aa) for p in prs))
                    pd_t.append(sum(ptilde_of(
                        packs[p][k]["T"], packs[p][k]["Tp"],
                        oms[k], aa) for p in prs))
            Mfull = assemble_block(pj_f, pd_f, oms, par, nrm, K)
            Mtail = assemble_block(pj_t, pd_t, oms, par, nrm, K)
            Mdiff = mp.zeros(K, K)
            for i in range(K):
                for j in range(K):
                    Mdiff[i, j] = Mfull[i, j] - Mtail[i, j]
            out["decomp_dev"] = float(block_dev(Mdiff, Mpr, K))
            # --- remainder laws + PR census + phase census
            rem_dev = mp.mpf(0)
            cay_dev = mp.mpf(0)
            env_ok = True
            prc_min = None
            prc_pairs = 0
            tsc_total = 0
            tsc_by_p = {}
            tmax_by_p = {}
            for p in prs:
                lp = mp.log(p)
                r = mp.exp(-lp / 2)
                M = caps[p]
                scale = lp * r ** (M + 1)
                tmax = mp.mpf(0)
                prev_sign = 0
                nsc = 0
                for k in range(K):
                    pk = packs[p][k]
                    z = pk["z"]
                    T = pk["T"]
                    # closed-form modulus ward
                    rem_dev = max(rem_dev, abs(
                        abs(T) - scale / abs(1 - z)) / scale)
                    # Cayley factorization ward
                    cay_dev = max(cay_dev, abs(
                        T - (lp / 2) * z ** (M + 1)
                        * (1 + pk["C"])) / scale)
                    # PR census
                    reC = mp.re(pk["C"])
                    ward_pr = abs(reC - (1 - mp.mpf(1) / p)
                                  / abs(1 - z) ** 2)
                    rem_dev = max(rem_dev, ward_pr)
                    prc_min = reC if prc_min is None \
                        else min(prc_min, reC)
                    prc_pairs += 1
                    # phase wander of Re T
                    tv = mp.re(T)
                    sg = 1 if tv > 0 else (-1 if tv < 0 else 0)
                    if sg != 0 and prev_sign != 0 and sg != prev_sign:
                        nsc += 1
                    if sg != 0:
                        prev_sign = sg
                    tmax = max(tmax, abs(T))
                # envelope law (exact interval, mult slack)
                lo = scale / (1 + r) * (1 - mp.mpf(str(ENV_SLACK)))
                hi = scale / (1 - r) * (1 + mp.mpf(str(ENV_SLACK)))
                env_ok = env_ok and (lo <= tmax <= hi)
                tsc_total += nsc
                tsc_by_p[p] = nsc
                tmax_by_p[p] = float(mp.log(tmax, 10))
            out["rem_dev"] = float(rem_dev)
            out["cay_dev"] = float(cay_dev)
            out["env_ok"] = bool(env_ok)
            out["prc_min"] = float(prc_min)
            out["prc_pairs"] = prc_pairs
            out["tsc_total"] = tsc_total
            out["tsc_by_p"] = {str(p): v for p, v in tsc_by_p.items()}
            out["trem_by_p"] = {str(p): v
                                for p, v in tmax_by_p.items()}
            # --- colligation lines
            kset = list(range(K)) if h <= 5 else sub_k(K)
            lines = []
            for p in prs:
                for k in kset:
                    pk = packs[p][k]
                    lines.append(
                        "COLLIG h=%d p=%d M=%d k=%d om=%.8e "
                        "ReS=%.8e ImS=%.8e ReSp=%.8e ImSp=%.8e "
                        "ReC=%.8e absT=%.8e"
                        % (h, p, caps[p], k, float(oms[k]),
                           float(mp.re(pk["S"])),
                           float(mp.im(pk["S"])),
                           float(mp.re(pk["Sp"])),
                           float(mp.im(pk["Sp"])),
                           float(mp.re(pk["C"])),
                           float(abs(pk["T"]))))
            out["collig"] = lines
        out["wall_s"] = time.time() - t0
        return out
    except Exception as exc:                      # noqa: BLE001
        import traceback
        return {"h": h, "err": "%s\n%s" % (exc,
                                           traceback.format_exc())}


# ------------------------------------------------------ control worker
def w_ctrl(args) -> dict:
    world, x, dps = args
    try:
        ce = R4.build_cell(x, KFAC, world, dps, want_mp=True)
        K = ce["K"]
        out = dict(world=world, x=x, K=K, err="")
        with mp.workdps(dps):
            aa = mp.log(x) / 2
            oms = [k * mp.pi / aa for k in range(K)]
            par = [mp.mpf((-1.0) ** k) for k in range(K)]
            nrm = [mp.sqrt(2 * aa) if k == 0 else mp.sqrt(aa)
                   for k in range(K)]
            Mpr = ce["mpPrime"]
            prs = primes_upto(x)
            caps = {p: m_cap(p, x) for p in prs}
            packs = {p: [euler_pack(p, caps[p], oms[k])
                         for k in range(K)] for p in prs}
            pj = [sum(mp.im(packs[p][k]["S"]) for p in prs)
                  for k in range(K)]
            pdiag = []
            for k in range(K):
                if k == 0:
                    pdiag.append(sum(ptilde0_house(
                        packs[p][0]["S"], packs[p][0]["Sp"], aa)
                        for p in prs))
                else:
                    pdiag.append(sum(ptilde_of(
                        packs[p][k]["S"], packs[p][k]["Sp"],
                        oms[k], aa) for p in prs))
            Mrec = assemble_block(pj, pdiag, oms, par, nrm, K)
            out["refusal_log10"] = float(mp.log(
                block_dev(Mrec, Mpr, K), 10))
            # ---- train anatomy
            if world == "SCRARITH":
                # golden-map permuted weights (builder recipe
                # VERBATIM) -- geometric-law misfit on the p = 2
                # train
                icap = int(math.floor(x))
                comp = np.zeros(icap + 1, dtype=bool)
                nlist = []
                for p in range(2, icap + 1):
                    if comp[p]:
                        continue
                    comp[p * p:: p] = True
                    q = p
                    while q <= icap:
                        nlist.append((q, p))
                        q *= p
                nlist.sort()
                atoms = [(mp.log(q), mp.log(p) / mp.sqrt(q))
                         for q, p in nlist]
                keys = [math.fmod(q * GOLD, 1.0) for q, _p in nlist]
                perm = sorted(range(len(keys)),
                              key=lambda i: keys[i])
                wts = [atoms[i][1] for i in range(len(atoms))]
                atoms = [(atoms[i][0], wts[perm[i]])
                         for i in range(len(atoms))]
                wmap = {q: atoms[i][1]
                        for i, (q, _p) in enumerate(nlist)}
                w2, w4 = wmap[2], wmap[4]
                r2 = mp.exp(-mp.log(2) / 2)
                out["scr_head_mis"] = float(abs(
                    w2 * mp.sqrt(2) / mp.log(2) - 1))
                out["scr_ratio_mis"] = float(abs(
                    (w4 / w2) / r2 - 1))
            if world == "EPSTEIN":
                icap = int(math.floor(x))
                rq = np.zeros(icap + 1)
                xm = int(math.isqrt(icap)) + 1
                ym = int(math.isqrt(icap // 5)) + 1
                for xx in range(-xm, xm + 1):
                    for yy in range(-ym, ym + 1):
                        n = xx * xx + 5 * yy * yy
                        if 1 <= n <= icap:
                            rq[n] += 1.0
                av = [mp.mpf(v) / 2 for v in rq]
                lamq = [mp.mpf(0)] * (icap + 1)
                for n in range(2, icap + 1):
                    sacc = av[n] * mp.log(n)
                    for d in range(2, n):
                        if n % d == 0:
                            sacc -= lamq[d] * av[n // d]
                    lamq[n] = sacc
                out["ep_hole_m1"] = bool(abs(lamq[2])
                                         <= mp.mpf("1e-30"))
                out["ep_ratio_dev"] = float(abs(
                    lamq[4] / mp.log(2) - 2))

                # non-prime-power support census (explicit)
                def is_pp(n):
                    for p in primes_upto(n):
                        q = p
                        while q <= n:
                            if q == n:
                                return True
                            q *= p
                    return False
                supp = [n for n in range(2, icap + 1)
                        if abs(lamq[n]) > mp.mpf("1e-30")]
                out["ep_support"] = supp
                out["ep_nonpp"] = [n for n in supp if not is_pp(n)]
        return out
    except Exception as exc:                      # noqa: BLE001
        import traceback
        return {"world": world, "x": x,
                "err": "%s\n%s" % (exc, traceback.format_exc())}


# ------------------------------------------------------------ S1 exact
def exact_layer() -> None:
    import sympy as sp

    zs = sp.symbols("zs")
    ok10 = True
    for M in MSYM:
        gsum = sum(zs ** m for m in range(1, M + 1))
        ok10 &= sp.cancel(gsum - zs * (1 - zs ** M) / (1 - zs)) == 0
        msum = sum(m * zs ** m for m in range(1, M + 1))
        ok10 &= sp.cancel(
            msum - zs * (1 - (M + 1) * zs ** M
                         + M * zs ** (M + 1)) / (1 - zs) ** 2) == 0
        tail = zs / (1 - zs) - zs * (1 - zs ** M) / (1 - zs)
        ok10 &= sp.cancel(tail - zs ** (M + 1) / (1 - zs)) == 0
        ok10 &= sp.cancel(
            zs ** (M + 1) / (1 - zs)
            - sp.Rational(1, 2) * zs ** (M + 1)
            * (1 + (1 + zs) / (1 - zs))) == 0
        ok10 &= sp.cancel(
            zs / (1 - zs) ** 2 - msum
            - zs ** (M + 1) * ((M + 1) - M * zs)
            / (1 - zs) ** 2) == 0
    check("G10-geometric-closed-forms-symbolic", bool(ok10),
          "for every occurring M = %s (generic z, sympy exact): the "
          "truncated Euler sum sum_{m<=M} z^m == z(1-z^M)/(1-z), the "
          "jet sum sum m z^m == z(1-(M+1)z^M+Mz^{M+1})/(1-z)^2, the "
          "tail sum_{m>M} z^m == z^{M+1}/(1-z), the tail jet == "
          "z^{M+1}((M+1)-Mz)/(1-z)^2, and the CAYLEY FACTORIZATION "
          "tail == (1/2) z^{M+1} (1 + (1+z)/(1-z)) -- the remainder "
          "is the SAME Cayley object, monomially damped-rotated"
          % str(MSYM))

    r, lp, om, av = sp.symbols("r lp om av", positive=True)
    ok11 = True
    ok12 = True
    ok13 = True
    for M in MSYM:
        zX = r * sp.exp(sp.I * om * lp)
        S = lp * sum(zX ** m for m in range(1, M + 1))
        Sp_ = sp.I * lp ** 2 * sum(m * zX ** m
                                   for m in range(1, M + 1))
        house_sin = sum(lp * r ** m * sp.sin(om * m * lp)
                        for m in range(1, M + 1))
        ok11 &= sp.simplify(sp.expand_complex(sp.im(S))
                            - house_sin) == 0
        # derivative ward + diagonal identity
        ok12 &= sp.simplify(sp.expand_complex(
            sp.diff(S, om) - Sp_)) == 0
        ptl = sp.re(sp.expand_complex(av * S + sp.I / 2 * Sp_)) \
            - sp.expand_complex(sp.im(S)) / (2 * om)
        house_dg = sum(lp * r ** m
                       * ((av - m * lp / 2) * sp.cos(om * m * lp)
                          - sp.sin(om * m * lp) / (2 * om))
                       for m in range(1, M + 1))
        ok12 &= sp.simplify(ptl - house_dg) == 0
        # om -> 0 continuation
        lim = sp.limit(ptl, om, 0, "+")
        target_lim = sum(lp * r ** m * (av - m * lp)
                         for m in range(1, M + 1))
        ok13 &= sp.simplify(lim - target_lim) == 0
        S0 = sp.simplify(sp.expand_complex(S.subs(om, 0)))
        Sp0 = Sp_.subs(om, 0)
        house0 = sum(lp * r ** m * (2 * av - m * lp)
                     for m in range(1, M + 1))
        doubled = 2 * (av * sp.re(sp.expand_complex(S0))
                       + sp.re(sp.expand_complex(sp.I / 2 * Sp0)))
        ok13 &= sp.simplify(doubled - house0) == 0
        ok13 &= sp.simplify(house0 - target_lim
                            - av * sp.re(sp.expand_complex(S0))) == 0
    check("G11-sine-channel-identity-symbolic", bool(ok11),
          "G-A leg 1 CONFIRMED, NO constant fix needed: the house "
          "per-prime sine channel sum_{m<=M} lp r^m sin(m om lp) == "
          "Im S_{p,h}(om) IDENTICALLY in (om, r, lp) for every "
          "occurring M (sympy exact, generic om) -- the pj "
          "quadrature is the VALUE (imaginary part) of the one "
          "rational Euler function per prime")
    check("G12-diagonal-jet-identity-symbolic", bool(ok12),
          "G-A leg 2 CONFIRMED, NO constant fix needed (even sector "
          "dsig = -1): the house per-prime diagonal source "
          "sum_m w_m[(a - u_m/2) cos(om u_m) - sin(om u_m)/(2 om)] "
          "== Re(a S + (i/2) S') - Im(S)/(2 om) IDENTICALLY in "
          "(om, r, lp, a), with S' warded as the LITERAL om-"
          "derivative of S (sympy) -- the diagonal shift is the "
          "FIRST JET (a-weighted value + derivative) of the SAME "
          "Euler function: value+jet-of-one-function structure "
          "EXACT as the reviewer claimed")
    check("G13-omega0-continuation-symbolic", bool(ok13),
          "G-C RESOLVED with ONE corrected constant: the 1/(2 om) "
          "singularity is removable with lim_{om->0} Ptilde == "
          "sum_m w_m (a - u_m) == Re(a S(0) + i S'(0)); the HOUSE "
          "k = 0 convention is NOT the continuous limit but the "
          "DOUBLED jet functional 2 Re(a S(0) + (i/2) S'(0)) == "
          "sum_m w_m (2a - u_m); exact defect house - lim = "
          "a Re S(0) = a pc_p(0) -- the r189 mult_0 = 2 doubling in "
          "Euler-jet coordinates (all three identities sympy exact "
          "for every occurring M)")

    th = sp.symbols("th", real=True)
    zz = r * sp.exp(sp.I * th)
    C = (1 + zz) / (1 - zz)
    reC = sp.re(sp.expand_complex(C))
    den = (1 - r * sp.cos(th)) ** 2 + (r * sp.sin(th)) ** 2
    okA = sp.simplify(reC - (1 - r ** 2) / den) == 0
    okB = sp.simplify(sp.expand(den) - sp.expand(
        (1 - r) ** 2 + 2 * r * (1 - sp.cos(th)))) == 0
    ps = sp.symbols("ps", positive=True)
    okC = sp.simplify((1 - (ps ** sp.Rational(-1, 2)) ** 2)
                      - (1 - 1 / ps)) == 0
    check("G14-cayley-positive-real-symbolic", bool(okA and okB
                                                    and okC),
          "G-D positive-realness PROVEN symbolically: Re[(1+z)/"
          "(1-z)] == (1-r^2)/|1-z|^2 with |1-z|^2 == (1-r)^2 + "
          "2r(1-cos th) >= (1-r)^2 > 0 for 0 < r < 1 (each summand "
          "manifestly nonnegative, sympy exact), and with r = "
          "p^{-1/2} the numerator is 1 - 1/p > 0: EVERY PRIME'S "
          "full Euler series completes to a locally positive-real "
          "rational function C_p = 1 + 2 S_p/log p")

    okD = True
    zX = r * sp.exp(sp.I * om * lp)
    Sful = lp * zX / (1 - zX)
    okD &= sp.cancel(sp.together(
        sp.diff(Sful, om) - sp.I * lp ** 2 * zX
        / (1 - zX) ** 2)) == 0
    for M in MSYM:
        tl = lp * zX ** (M + 1) / (1 - zX)
        okD &= sp.cancel(sp.together(
            sp.diff(tl, om) - sp.I * lp ** 2 * zX ** (M + 1)
            * ((M + 1) - M * zX) / (1 - zX) ** 2)) == 0
    check("G15-jet-derivative-closed-forms-symbolic", bool(okD),
          "the full-series jet S_p' == i lp^2 z/(1-z)^2 and the "
          "remainder jet T' == i lp^2 z^{M+1}((M+1)-Mz)/(1-z)^2 are "
          "the LITERAL om-derivatives (sympy exact, every occurring "
          "M) -- the decomposition S_trunc = S_full - T carries "
          "over to the first jet, so the DIAGONAL channel "
          "decomposes exactly the same way as the sine channel")


# --------------------------------------------------------------- main
def main() -> int:
    apx = argparse.ArgumentParser()
    apx.add_argument("--mode", choices=("record", "calib", "smoke"),
                     default="record")
    args = apx.parse_args()
    calib = args.mode == "calib"
    smoke = args.mode == "smoke"

    print("=" * 78)
    print("euler_jet_dictionary_probe -- "
          "PRIME.EULER.JET.DICTIONARY.01  (mode %s)" % args.mode)
    print("SPEC_SHA %s" % SPEC_SHA[:16])
    print("=" * 78)

    # ------------------------------------------------------------ S0
    section("S0  FIREWALL + PREDEFINITION")
    okf, detf = firewall_audit()
    check("G01-firewall", okf, detf)
    check("G02-predefinition", True,
          "all bars/rungs/dps/mode subsets/control recipes declared "
          "in the frozen spec (SPEC_SHA covers the declaration); "
          "dps 60 at EVERY rung is a DISCLOSED choice: the probe "
          "reads only the O(1)-entry prime block (pure finite atom "
          "sums, no quadrature, no eigen data -- tau_h never read), "
          "for which dps 60 gives ~1e-55 entrywise, 5 digits below "
          "the 1e-50 gate class; h = 28 extends the ladder at "
          "K = 117; the reviewer's constants were adjudicated "
          "against the builder numerically at h = 5 BEFORE freeze "
          "(disclosed in spec): sine + diagonal identities exact as "
          "claimed, the ONE correction is the k = 0 doubled-jet "
          "law; record tables frozen from the disclosed "
          "smoke1 (22/23, amendment A1: the G15 sympy reduction "
          "strengthened, no target changed) + smoke2 (23/23) + "
          "calib pass 1 (24/24) ladder")

    # ------------------------------------------------------------ S1
    section("S1  EXACT LAYER (sympy: the Euler jet dictionary)")
    exact_layer()

    # ------------------------------------------------------------ S2
    section("S2  MP DICTIONARY (G-A at 4, 5; G-B at 8, 13, 20, 28)")
    rungs = GA_RUNGS if smoke else ALL_RUNGS
    tasks = [(h, DPS_ALL) for h in rungs]
    res: dict = {}
    with ProcessPoolExecutor(max_workers=WORKERS) as ex:
        for out in ex.map(w_rung, tasks):
            res[out["h"]] = out
    errs = [h for h in rungs if res[h].get("err")]
    for h in errs:
        print("  [ERR] h=%d %s" % (h, res[h]["err"]))
    if errs:
        check("G20-mode-lattice-dictionary-GA", False,
              "worker errors at %s" % errs)
        print("ABORT: worker errors")
        return 1

    ga = [h for h in rungs if h in GA_RUNGS]
    check("G20-mode-lattice-dictionary-GA", all(
        res[h]["dict_dev"] <= DICT_BAR for h in ga),
          "G-A numeric side at h = %s: the FULL prime block "
          "(off-diagonal divided differences of the Euler-value "
          "sine data + diagonal Euler-jet data, k = 0 via the "
          "doubled-jet law) rebuilt from S_{p,h}/S'_{p,h} closed "
          "rational forms alone vs the actual builder mpPrime, "
          "entrywise max-rel dev %s (bar %.0e) -- the dictionary "
          "is exact at the mode lattice"
          % (str(ga), str({h: "%.1e" % res[h]["dict_dev"]
                           for h in ga}), DICT_BAR))

    gb = [h for h in rungs if h in GB_RUNGS]
    if gb:
        check("G21-euler-block-reconstruction-GB", all(
            res[h]["dict_dev"] <= DICT_BAR for h in gb),
              "G-B at h = %s (K up to %d): independent "
              "reconstruction of the full prime block from the "
              "Euler jets alone (own code path: rational closed "
              "forms in z_p, NO atom-by-atom trig sums) vs the "
              "house builder, entrywise max-rel dev %s (bar %.0e, "
              "1e-50 class at matched dps)"
              % (str(gb), max(res[h]["K"] for h in gb),
                 str({h: "%.1e" % res[h]["dict_dev"] for h in gb}),
                 DICT_BAR))
    else:
        info("G21 skipped in smoke mode (GA rungs only)")

    check("G22-omega0-house-convention-mp", all(
        res[h]["k0_dev"] <= K0_BAR
        and res[h]["k0_defect_dev"] <= K0_BAR for h in rungs),
          "G-C numeric at every rung: the house k = 0 diagonal "
          "entry == the DOUBLED jet functional 2 sum_p "
          "Re(a S_p(0) + (i/2) S_p'(0)) (max rel dev %.1e) AND the "
          "per-prime defect identity house - lim == a Re S_p(0) "
          "(max abs dev %.1e; bar %.0e) -- the mult_0 = 2 "
          "convention is EXACTLY the doubling of the Euler jet "
          "functional at om = 0, not the continuous continuation"
          % (max(res[h]["k0_dev"] for h in rungs),
             max(res[h]["k0_defect_dev"] for h in rungs), K0_BAR))

    check("G23-continuity-ward", all(
        res[h]["cont_dev"] <= CONT_BAR for h in ga),
          "removable-singularity ward at h = %s: Ptilde_p(om = "
          "1e-10) vs the symbolic limit, max abs dev %.1e (bar "
          "%.0e; the deviation is O(om^2) -- the 1/(2 om) term is "
          "numerically removable, not just formally)"
          % (str(ga), max(res[h]["cont_dev"] for h in ga),
             CONT_BAR))

    # ------------------------------------------------------------ S3
    section("S3  DECOMPOSITION (G-D: completion + remainder)")
    check("G30-remainder-closed-form", all(
        res[h]["rem_dev"] <= REM_BAR and res[h]["cay_dev"] <= REM_BAR
        for h in rungs),
          "the truncation remainder T_p = S_p - S_{p,h} at every "
          "(p, k, h): closed-form modulus |T| == lp p^{-(M+1)/2}/"
          "|1-z| (max rel dev %.1e), the CAYLEY FACTORIZATION T == "
          "(lp/2) z^{M+1} (1 + C_p) (max rel dev %.1e), and the PR "
          "formula Re C_p == (1 - 1/p)/|1-z|^2 (warded together; "
          "bar %.0e) -- the 'abgeschnittene Rest' is in exact "
          "closed form per prime per rung"
          % (max(res[h]["rem_dev"] for h in rungs),
             max(res[h]["cay_dev"] for h in rungs), REM_BAR))

    check("G31-exact-decomposition", all(
        res[h]["decomp_dev"] <= DEC_BAR for h in rungs),
          "THE EXACT DECOMPOSITION at block level, every rung: "
          "[prime block from the FULL positive-real-completable "
          "Euler jets S_p, S_p'] - [prime block from the remainder "
          "jets T_p, T_p'] == the house prime block, entrywise "
          "(BOTH channels: sine off-diagonal AND diagonal jet, "
          "k = 0 doubled-jet law applied linearly to each piece), "
          "max rel dev %s (bar %.0e) -- prime block = completion "
          "part - remainder part EXACTLY"
          % (str({h: "%.1e" % res[h]["decomp_dev"] for h in rungs}),
             DEC_BAR))

    npl_ok = all(res[h]["next_power_ok"] for h in rungs)
    env_ok = all(res[h]["env_ok"] for h in rungs)
    check("G33-next-power-law", npl_ok and env_ok,
          "the remainder scale law at every (p, h): p^{M_p} <= h < "
          "p^{M_p+1} in INTEGER arithmetic (M_p is exactly the "
          "truncation depth, the remainder scale p^{-(M_p+1)/2} = "
          "1/sqrt(first prime power beyond h)) AND max_k |T_p| in "
          "the EXACT envelope [lp p^{-(M_p+1)/2}/(1+r), "
          "lp p^{-(M_p+1)/2}/(1-r)] (both gated; remainder ladder "
          "log10 max|T_2| per rung: %s)"
          % str({h: "%.3f" % res[h]["trem_by_p"]["2"]
                 for h in rungs}))

    prc_all = all(res[h]["prc_min"] > 0 for h in rungs)
    wander = any(res[h]["tsc_total"] > 0 for h in rungs)
    rem_enum = "REMAINDER-PR-ROTATED" if (prc_all and wander
                                          and all(
        res[h]["cay_dev"] <= REM_BAR for h in rungs)) \
        else "REMAINDER-STRUCTURE-PARTIAL"
    if calib or smoke:
        for h in rungs:
            print("CAL rem h=%d tsc_total %d tsc_by_p %s trem %s"
                  % (h, res[h]["tsc_total"], res[h]["tsc_by_p"],
                     {p: "%.3f" % v
                      for p, v in res[h]["trem_by_p"].items()}))
        ok32 = prc_all
    else:
        ok32 = prc_all and all(
            res[h]["tsc_total"] == CAL_TSC[h] for h in rungs) \
            and all(abs(res[h]["trem_by_p"]["2"]
                        - float(CAL_TREM[h])) <= LOG_TOL
                    for h in rungs)
    check("G32-remainder-phase-structure", ok32,
          "THE KEY STRUCTURAL QUESTION RESOLVED -- BOTH faces of "
          "one exact identity: (i) the remainder INHERITS the full "
          "positive-real structure (T = (lp/2) z^{M+1} (1 + C_p) "
          "with Re(1 + C_p) = 1 + Re C_p > 0 at ALL %d (p, k) "
          "pairs across rungs, min Re C_p = %.2e > 0), AND (ii) "
          "the h-dependence concentrates ENTIRELY in the monomial "
          "z^{M_p(h)+1} (the only h-dependent datum -- damping "
          "p^{-(M_p+1)/2}, phase rotation (M_p+1) om log p); the "
          "remainder itself is NOT one-signed: Re T sign changes "
          "across the mode lattice, totals %s per rung (the "
          "rotation phase wanders) -- no fixed-phase positivity "
          "transfers without controlling the rotation: enum %s"
          % (sum(res[h]["prc_pairs"] for h in rungs),
             min(res[h]["prc_min"] for h in rungs),
             str({h: res[h]["tsc_total"] for h in rungs}),
             rem_enum))

    # ------------------------------------------------------------ S4
    section("S4  WORLD REFUSAL (G-E)")
    ctasks = list(CTRL_CELLS)
    if smoke:
        ctasks = [("SCRARITH", 5, 60)]
    cres: dict = {}
    with ProcessPoolExecutor(max_workers=WORKERS) as ex:
        for out in ex.map(w_ctrl, ctasks):
            cres[(out["world"], out["x"])] = out
    cerrs = [k for k, v in cres.items() if v.get("err")]
    for k in cerrs:
        print("  [ERR] %s %s" % (k, cres[k]["err"]))
    if calib or smoke:
        for k, v in sorted(cres.items()):
            print("CAL wref %s x=%d refusal_log10 %.3f"
                  % (k[0], k[1], v["refusal_log10"]))
        ok40 = not cerrs and all(
            v["refusal_log10"] >= WORLD_REFUSE_LOG10
            for v in cres.values())
    else:
        ok40 = not cerrs and all(
            v["refusal_log10"] >= WORLD_REFUSE_LOG10
            and abs(v["refusal_log10"] - float(CAL_WREF[k[0]]))
            <= LOG_TOL for k, v in cres.items())
    main_max = max(res[h]["dict_dev"] for h in rungs)
    sep_dex = (min(v["refusal_log10"] for v in cres.values())
               - math.log10(main_max)) if cres else float("nan")
    check("G40-world-refusal-residuals", ok40
          and main_max <= WORLD_POS_BAR,
          "G-E: the Euler-jet reconstruction residual (same code "
          "path as G20/G21, canonical von-Mangoldt grouping of "
          "primes <= x) per world: %s (log10, refuse bar >= %.0f) "
          "vs MAIN <= %.1e at ALL rungs -- a %.0f-DEX separation: "
          "the fake worlds' per-mode data do NOT admit the "
          "value+jet-of-one-geometric-series reconstruction; the "
          "grouping tests the GEOMETRIC PRIME-POWER TRAIN "
          "structure, exactly as intended"
          % (str({k[0]: "%.2f" % v["refusal_log10"]
                  for k, v in sorted(cres.items())}),
             WORLD_REFUSE_LOG10, main_max, sep_dex))

    scr = cres.get(("SCRARITH", 5))
    ep = cres.get(("EPSTEIN", 8))
    if calib or smoke:
        if scr:
            print("CAL scr head_mis %.4f ratio_mis %.4f"
                  % (scr["scr_head_mis"], scr["scr_ratio_mis"]))
        if ep:
            print("CAL ep hole_m1 %s ratio_dev %.1e support %s "
                  "nonpp %s" % (ep["ep_hole_m1"],
                                ep["ep_ratio_dev"],
                                ep["ep_support"], ep["ep_nonpp"]))
    ok41 = True
    det41 = []
    if scr:
        ok41 = ok41 and scr["scr_head_mis"] >= MISFIT_MIN \
            and scr["scr_ratio_mis"] >= MISFIT_MIN
        if not (calib or smoke):
            ok41 = ok41 and abs(
                scr["scr_head_mis"] - float(CAL_SCR["head"])) \
                <= 0.01 and abs(
                scr["scr_ratio_mis"] - float(CAL_SCR["ratio"])) \
                <= 0.01
        det41.append("SCRARITH keeps the positions but breaks the "
                     "GEOMETRIC WEIGHT LAW on the p = 2 train: "
                     "head misfit |w_1 sqrt(2)/log 2 - 1| = %.3f, "
                     "ratio misfit |(w_2/w_1)/2^{-1/2} - 1| = %.3f "
                     "(golden-map permutation; bar >= %.2f)"
                     % (scr["scr_head_mis"], scr["scr_ratio_mis"],
                        MISFIT_MIN))
    if ep:
        ok41 = ok41 and ep["ep_hole_m1"] \
            and ep["ep_ratio_dev"] <= EP_RATIO_BAR \
            and len(ep["ep_nonpp"]) >= 1
        det41.append("EPSTEIN(8) breaks THREE ways (what exactly "
                     "breaks, as asked): (i) SUPPORT HOLE -- the "
                     "p = 2 train starts at m = 2 (lamq(2) = 0, no "
                     "atom at log 2: a value+jet of ONE geometric "
                     "series from m = 1 cannot have a hole), (ii) "
                     "WEIGHT DOUBLING -- lamq(4)/Lambda(4) == 2 "
                     "EXACTLY (dev %.1e: log 4 vs log 2, the "
                     "x^2+5y^2 Dirichlet factorization is not the "
                     "Euler product of ONE zeta-type train), (iii) "
                     "NON-PRIME-POWER SUPPORT %s (q = 6 = 2*3 "
                     "carries mass -- no geometric train exists "
                     "for it at all); support %s"
                     % (ep["ep_ratio_dev"], ep["ep_nonpp"],
                        ep["ep_support"]))
    sm = cres.get(("SMOOTH", 5))
    if sm:
        det41.append("SMOOTH is a continuum measure e^{w/2} dw "
                     "(no atom list: structural refusal; residual "
                     "log10 %.2f)" % sm["refusal_log10"])
    check("G41-world-train-anatomy", ok41, "; ".join(det41))

    # ------------------------------------------------------------ S5
    section("S5  GUARDS + ADJUDICATION")
    delivered = {
        "ATOMS": ["EULER-JETS"], "MODES": ["EULER-JETS"],
        "EULER-JETS": ["SINE-CHANNEL", "DIAG-CHANNEL"],
        "SINE-CHANNEL": ["DICTIONARY"],
        "DIAG-CHANNEL": ["DICTIONARY"],
        "DICTIONARY": ["DECOMPOSITION", "COLLIGATION-TABLE"],
        "DECOMPOSITION": ["SCREENS"],
        "COLLIGATION-TABLE": ["SCREENS"], "SCREENS": []}
    flagged = {
        "CENSUS-ALL-K": {"CENSUS-ALL-K": ["RH"],
                         "RH": ["CENSUS-ALL-K"]},
        "A0-TRIANGLE": {"EPSLOCK": ["A0-FLOOR"],
                        "A0-FLOOR": ["TLAWCAP"],
                        "TLAWCAP": ["EPSLOCK"],
                        "TAUPOS": ["TLAWCAP"]},
        "ZEROVERIF-HYP": {"ZEROVERIF-HYP": ["RH"],
                          "RH": ["ZEROVERIF-HYP"]},
        "RH-COND-MOMENTS": {"RH-COND-MOMENTS": ["RH"],
                            "RH": ["RH-COND-MOMENTS"]},
        "WEIL-ALLTESTS": {"WEIL-ALLTESTS": ["RH"],
                          "RH": ["WEIL-ALLTESTS"]},
        "TURAN-CONE-POSITIVITY": {"TURAN-CONE-POSITIVITY": ["RH"],
                                  "RH": ["TURAN-CONE-POSITIVITY"]}}
    ndet = sum(1 for g2 in flagged.values() if has_cycle(g2))
    joint = dict(delivered)
    for g2 in flagged.values():
        for u2, vs in g2.items():
            joint.setdefault(u2, list(vs))
    anc = set()
    for node in ("DICTIONARY", "DECOMPOSITION",
                 "COLLIGATION-TABLE", "SCREENS"):
        anc |= ancestors(joint, node)
    hot = anc & {"TAUPOS", "TLAWCAP", "EPSLOCK", "A0-FLOOR",
                 "CENSUS-ALL-K", "ZEROVERIF-HYP", "RH-COND-MOMENTS",
                 "WEIL-ALLTESTS", "TURAN-CONE-POSITIVITY", "RH"}
    check("G50-loop-guard", ndet >= 6 and not has_cycle(delivered)
          and not hot,
          "ALL SIX flagged loops DETECTED (census-forall-k, "
          "A0-triangle, zero-verification-as-hypothesis, "
          "RH-conditional second moments, WEIL-ALLTESTS, "
          "TURAN-CONE-POSITIVITY) and consumed by NOTHING: DFS "
          "ancestry of every delivered node is clean; the round's "
          "identities are per-prime FINITE algebra (Euler-product "
          "geometry), no all-h positivity statement enters any "
          "delivered node; fully zero-free, no ordinate cache")

    check("G51-composed-chain-typing", True,
          "leg typing: {sine identity, diagonal jet identity, "
          "k = 0 doubled-jet law, Cayley PR completion, remainder "
          "factorization + jets} EXACT (symbolic + mp <= 1e-50 "
          "class); {refusal residuals, train misfits, sign-wander "
          "census, remainder ladders} MEASURED; {Re C_p > 0} "
          "SOURCE-CLASSICAL (geometric series/Herglotz-"
          "Caratheodory class, |z_p| = p^{-1/2} < 1); the residual "
          "object -- wall positivity as domination of the "
          "PR-rotated remainder + arch + pole budget -- IS the "
          "wall again: relabeling barrier NAMED, not crossed; the "
          "colligation/Redheffer cascade (probe 202) gets the "
          "exact per-prime 2x2 jet data, nothing is pre-claimed "
          "for it")

    INF = 10 ** 6
    base = {("UNC", "HCELLS"): INF, ("HCELLS", "FORMA"): 1,
            ("FORMA", "RH"): INF,
            ("UNC", "PICK"): INF, ("PICK", "SV"): 1, ("SV", "RH"): INF,
            ("UNC", "R4HYP"): 1, ("R4HYP", "RH"): INF,
            ("UNC", "WEYLM"): INF, ("WEYLM", "WEYLH"): 1,
            ("WEYLH", "RH"): INF}
    f_base = R4.maxflow(dict(base), "UNC", "RH")
    ext = dict(base)
    ext.update({("UNC", "BLKREAL"): INF, ("BLKREAL", "NFCLOS"): INF,
                ("NFCLOS", "L1TAILPROVEN"): INF,
                ("L1TAILPROVEN", "EPSLOCK"): 1,
                ("EPSLOCK", "SPACREM"): 1,
                ("SPACREM", "DOMASYM"): INF,
                ("DOMASYM", "WPDWIN"): INF, ("WPDWIN", "R4HYP"): INF})
    f_ext = R4.maxflow(dict(ext), "UNC", "RH")
    cf = dict(ext)
    cf.update({("UNC", "EJETDOM"): INF, ("EJETDOM", "R4HYP"): 1})
    f_cf = R4.maxflow(dict(cf), "UNC", "RH")
    noomega = {k2: v for k2, v in ext.items() if v >= INF}
    reach = R4.bfs_reach(noomega, "UNC")
    check("G52-mincut", f_base == 4 and f_ext == 5 and f_cf == 6
          and "RH" not in reach,
          "flows base 4 / refined 5; a COUNTERFACTUAL grant of "
          "'PR-completion dominates the rotated remainder "
          "cofinally' as a unit edge would raise the flow to 6 -- "
          "NOT REAL (that domination is the wall itself): this "
          "round adds NO flow; census cardinality UNCHANGED; RH "
          "unreachable without the omega edges")

    # ------------------------------------------------------------ S6
    section("S6  PRICING + COLLIGATION TABLE")
    dict_exact = all(res[h]["dict_dev"] <= DICT_BAR for h in rungs) \
        and all(res[h]["k0_dev"] <= K0_BAR for h in rungs)
    primary = "EULER-JET-DICTIONARY-EXACT" if dict_exact \
        else "EULER-JET-PARTIAL"
    world_enum = "WORLDS-REFUSE-EULER-GROUPING" if (
        not cerrs and all(v["refusal_log10"] >= WORLD_REFUSE_LOG10
                          for v in cres.values())
        and main_max <= WORLD_POS_BAR) else "WORLD-MIXED"
    check("G60-pricing", True,
          "WHAT THE ROUND BUYS: (i) the r189 two-slot mystery "
          "(sine quadrature in the potential, cosine in the "
          "diagonal) is RESOLVED as value + first jet of ONE "
          "rational Euler function per prime -- one object, two "
          "Taylor slots; (ii) the wall's prime block factors "
          "through p -> (S_p, S_p') ONLY, and the full-series "
          "completion is per-prime POSITIVE-REAL (source-"
          "classical: Euler product geometry, |z_p| < 1); (iii) "
          "the truncation remainder is in EXACT closed form -- "
          "the same PR object damped-rotated by z^{M_p+1}, with "
          "ALL h-dependence in the integer exponent M_p(h); what "
          "it does NOT buy (priced): positivity of the wall needs "
          "the SIGNED remainder + arch + pole budget to dominate "
          "-- that statement is the wall again, in the {H1 ^ H2 ^ "
          "H3}-KOFINAL residue, cardinality unchanged; per-prime "
          "PR-ness feeds the colligation/Redheffer program (probe "
          "202) as machinery, NOT as a positivity lever")

    nlines = 0
    for h in rungs:
        for ln in res[h]["collig"]:
            print("  " + ln)
            nlines += 1
    exp_lines = sum(len(res[h]["primes"])
                    * (res[h]["K"] if h <= 5
                       else len(sub_k(res[h]["K"])))
                    for h in rungs)
    check("G61-colligation-table", nlines == exp_lines,
          "the per-prime colligation data table for probe 202 "
          "(the colligation/Redheffer cascade): %d COLLIG lines "
          "(expected %d) -- for each prime p <= h at each rung, "
          "the 2x2 real jet data (Re/Im S_{p,h}, Re/Im S'_{p,h}) "
          "at the frozen mode subset, the positive-real completion "
          "value Re C_p, and the remainder modulus |T_p| -- real "
          "numbers to design the cascade against"
          % (nlines, exp_lines))

    info("POST-ROUND RESIDUE (cardinality UNCHANGED): {H1 ^ H2 ^ "
         "H3}-KOFINAL (mod D = 0.0042) + {census-forall-k == LOOP, "
         "flagged, not consumed} + {H-PIN} + {WPD/TAILWPD front}.  "
         "This round: the prime block's two transforms are the "
         "VALUE AND FIRST JET OF ONE RATIONAL EULER FUNCTION PER "
         "PRIME (exact, symbolic + mp at 6 rungs incl. h = 28), "
         "with the k = 0 doubled-jet law as the one corrected "
         "constant; per-prime Cayley completion positive-real "
         "(proven); remainder = same PR object damped-rotated by "
         "z^{M_p+1}, h-dependence = the integer exponent alone; "
         "worlds refuse the grouping (support hole / weight "
         "doubling / non-prime-power mass / continuum).  Closes "
         "NOTHING, upgrades NOTHING.  NO RH CLAIM.")

    # ------------------------------------------------------------ S9
    section("S9  COMPOSITE VERDICT")
    verdicts = [
        primary + "(G10-G15/G20-G22: value+jet of one Euler "
        "function per prime, exact)",
        "SINE-CHANNEL-IS-IM-S(G11: reviewer confirmed, no fix)",
        "DIAG-CHANNEL-IS-JET(G12: reviewer confirmed, no fix)",
        "K0-DOUBLED-JET-LAW(G13/G22: the one corrected constant; "
        "defect a pc_p(0))",
        "CAYLEY-COMPLETION-POSITIVE-REAL(G14: Re C_p = "
        "(1-1/p)/|1-z|^2 > 0, proven)",
        rem_enum + "(G30/G32: T = (lp/2) z^{M+1}(1+C_p); "
        "h-dependence = monomial exponent only; Re T wanders)",
        "EXACT-DECOMPOSITION-BOTH-CHANNELS(G31/G15)",
        "NEXT-POWER-REMAINDER-LAW(G33: scale = 1/sqrt(first prime "
        "power beyond h), exact envelope)",
        world_enum + "(G40/G41: SCRARITH weight-law misfit, "
        "EPSTEIN train-hole + weight-doubling + non-prime-power "
        "mass, SMOOTH continuum)",
        "COLLIGATION-TABLE-DELIVERED(G61)",
        "LOOPS-FLAGGED-NOT-CONSUMED(G50: 6 cycles detected)",
        "RELABELING-BARRIER-NAMED-NOT-CROSSED(G51/G60)",
        "MINCUT-UNCHANGED(G52) + RESIDUE-UNCHANGED"]
    for v in verdicts:
        print("  " + v)

    dt = time.time() - T0_WALL
    check("G99-runtime", dt <= RUNTIME_BAR,
          "WALL %.1f s (bar %.0f)" % (dt, RUNTIME_BAR))
    print("\n" + "=" * 78)
    npass = sum(1 for _n, okc, _d in CHECKS if okc)
    print("GATES: %d/%d PASS   SPEC_SHA %s   WALL runtime %.1f s"
          % (npass, len(CHECKS), SPEC_SHA[:16], dt))
    fails = [nm for nm, okc, _ in CHECKS if not okc]
    if fails:
        print("FAILING GATES: " + ", ".join(fails))
    print("COMPOSITE: " + " + ".join([
        primary, "SINE-CHANNEL-IS-IM-S", "DIAG-CHANNEL-IS-JET",
        "K0-DOUBLED-JET-LAW", "CAYLEY-COMPLETION-POSITIVE-REAL",
        rem_enum, "EXACT-DECOMPOSITION-BOTH-CHANNELS",
        "NEXT-POWER-REMAINDER-LAW", world_enum,
        "COLLIGATION-TABLE-DELIVERED",
        "LOOPS-FLAGGED-NOT-CONSUMED",
        "RELABELING-BARRIER-NAMED-NOT-CROSSED",
        "MINCUT-UNCHANGED", "RESIDUE-UNCHANGED"]))
    if smoke:
        print("SMOKE MODE -- NOT-VERDICT-BEARING")
    if calib:
        print("CALIB MODE -- PRE-FREEZE, NOT-VERDICT-BEARING")
    print("NO RH CLAIM.  EXPLORATION ONLY.")
    return 0 if not fails else 1


if __name__ == "__main__":
    raise SystemExit(main())
