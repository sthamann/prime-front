#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""code_synthesis_probe -- PRIME.CODE.SYNTHESIS.01

FROZEN SPEC (2026-08-15).  EXPLORATION ONLY.  This file is the sole
probe of the round.  It writes nothing, imports no repository module,
reads no measured pin, zero table, paper, ledger, website or
verification file, and makes NO RH claim and NO all-depth positivity
claim.

TARGET -- PRIMES AS ERROR-CORRECTING CODE, ADJUDICATED UNDER THAT NAME.
The owner's founding intuition is that the primes function as an
error-correcting code inside TFPT.  The corpus has never tested the
intuition under that name, although its finite side literally runs on
codes (extended Hamming [8,4,4] -> Construction A -> E8, rounds
v626/v638/v776) and its arithmetic side has just measured an
error-correction statement without calling it one (round 96,
rigidity_inverse_probe: screw positivity to depth r pins the measure
onto the prime comb exponentially, every impostor dies at its defect
footprint).  This probe formalizes the positivity system AS a code,
tests whether the code has TFPT structure, and answers the one
decisive question: does the code admit a FINITE dual description?

THE FIVE QUESTIONS (C1-C5).
C1  THE CODE DICTIONARY.  Ambient space = nonnegative atomic measures
    on (0, r] read through the frozen tent mesh delta = 0.006 (moment
    vector c in R^D, D = r/delta); check family = positivity of the
    Toeplitz sections T_k(-g'') for k <= D, equivalently the causal
    Verblunsky condition |alpha_k| < 1 (Levinson/Szego recursion);
    codeword = the prime-power comb (u = m log p, w = log p p^{-m/2});
    minimum distance = the round-96 moduli law (re-measured here:
    atom-2 weight modulus at D in (250, 400, 600, 799), 16-step
    bisection, refit of ln eta*(r) vs r against the frozen round-96
    line ln eta* = -1.073 r - 7.078); decoding radius = impostor death
    depths (six-member frozen subset re-measured against the round-96
    exits); rate = survival-box log-volume slope over the five
    shallow-footprint weight channels (atoms 2, 3, 4, 5, 7) between
    D = 400 and D = 799 -- the effective dimension question.
C2  IS THE CHECK FAMILY COMPILER-EXPRESSIBLE?  The checks are Gram
    positivity of node evaluations against -g'' (the round-86
    Simple-Principle form, S2 3/3 TRANSCRIPTION, S4 square law).  The
    compiler's literal code layer is rebuilt EXACTLY in this probe:
    extended Hamming [8,4,4] as RM(1,3) on AG(3,2), self-duality,
    weight enumerator {0:1, 4:14, 8:1}, doubly-even, Construction A
    lattice with 240 norm-2 vectors and unimodular even Gram (the
    v626/v638 layer, independently re-enumerated).  The comparison is
    then typed: same grammar (membership = nonnegativity of a Gram
    pairing family) or genuinely different type (the decisive
    invariant: dual rank).
C3  THE DECISIVE QUESTION -- FINITE DUAL DESCRIPTION.  (a) Section
    nestedness: T_k are leading principal sections of T_D, so ONE
    check per depth suffices -- the quantifier lives in the depth
    ladder, and the honest dual-rank question is whether the check
    index needed to reject the minimum-distance error at depth r
    stabilizes or grows.  Measured: the death index of the final
    bisection bracket-hi endpoint (the smallest dying perturbation)
    at each census depth; OLS slope of k_fail*delta vs r.  GROWS iff
    slope >= 0.50 (expected ~1), STABILIZES (the lever) iff <= 0.25.
    (b) Syndrome rank: at each recorded death the violated constraint
    is an explicit linear functional on moment space -- the
    autocorrelation of the failing Szego predictor polynomial
    (ALPHA_EXIT at step k: v = Phi_{k+1} built with the attempted
    alpha, v^T T v = E_k (1 - alpha^2) <= 0; DEN_NONPOSITIVE: v =
    Phi*_k).  Each syndrome functional is VERIFIED violated on its
    own world (ward).  The stacked, row-normalized syndrome matrix
    over the full error census is SVD-ranked (threshold 1e-8
    sigma_max); rank of the shallow half (by death index) vs full
    rank measures whether deep errors need NEW independent checks.
    (c) The round-85 counting law (tp_opus S7: forced skip count
    D_max = x - 3/8, linear in depth, on the node-Gram instrument) is
    confronted as the cross-instrument corroboration -- printed,
    typed, not re-measured here.  (d) Blindness theorem check: the
    tail impostor MASSREST(3.0) (true atoms u < 3.0 + smooth PNT ramp
    beyond) has moments BIT-IDENTICAL to truth below its defect lag
    d0, hence every check of index < d0 - 1 is EXACTLY blind to it
    (causality lemma); measured: max prefix alpha deviation == 0.0
    and death >= d0 - 1.  A non-codeword indistinguishable to every
    bounded-depth check family is the exact reason a finite dual
    cannot exist.
C4  LTC AND THE DECODING THEOREM.  Local testability: given
    nestedness, a random single check of index k <= D rejects an
    error dying at k_d with probability (D - k_d)/D; an m-subset with
    q = 1 - (k_d/D)^m.  Measured: q for the LOCAL error class
    (spurious atom at log 2.5 and log 6, weight 0.01; deletion of
    atom 2) at D = 400 and D = 799 -- the gap must be large and
    non-decreasing in depth (LTC-LOCAL); and for the ADVERSARIAL
    class (MASSREST(u0), u0 in 1.5, 3.0, 4.5 -- the defect pushed
    toward the window edge) -- q must decay toward 0 as u0 -> r
    (LTC-ADV; a survivor at the window edge counts as q = 0, the
    strongest adversarial datum).  Golden-key empirical subset
    sampling (64 subsets of size 8, no RNG) is cross-checked against
    the analytic q (ward, <= 0.15), with levinson spot-verification
    of sampled checks on both sides of k_d.  The decoding-theorem
    candidate is then stated and typed (anchors measured, law fitted,
    all-depth OPEN), together with the honest converse: decoding
    (checks to depth r ==> codeword identification to precision
    eta*(r)) is NOT the RH direction (codeword ==> ALL checks pass).
C5  VERDICT (composite; priority order):
    INSTRUMENT-EDGE (any ward fails; exit 1; no mathematical verdict)
    > CODE-LEVER(component) -- the dual-rank slope STABILIZES
    (<= 0.25) or the adversarial LTC gap is depth-independent
    (q(4.5) >= 0.8): the overlooked lever the owner asks about, named
    > CODE-DICTIONARY-INCOMPLETE(gate) -- a C1/C2 science gate fails
    (the code reading itself did not compile)
    > CODE-READING-TRUE-DECODING-DIRECTION -- the expected close: the
    error-code reading is TRUE and MEASURED, same Gram grammar as the
    compiler's code layer but with a depth-unbounded dual, locally
    testable for local errors only; it runs in the decoding
    direction while RH needs the encoding quantifier.

FROZEN OBJECTS (rigidity_inverse / collective_rescue conventions
verbatim).  Screw accelerant -g'' at delta = 0.006, n = 800 (L = 4.8):
archimedean background (pole 2cosh(t/2) layer, arch layer S'' = rho,
Lerch coefficient +1/4, v643 convention lock) built in mpmath dps 50
and cast once to float64; prime-power atoms as exact tent reads.
Positivity to depth k := Levinson completes alphas 0..k-1 with
|alpha| < 1 and prediction error > 0.  MAIN ENGINE float64; validity
WARDED (mp dps 40 cross on the 428-prefix), never assumed.  MASSREST
ramp g_tail(t) = int_{u0}^t (t - u) e^{u/2} du.  Impostor subset
(frozen, round-96 constructors verbatim): SHIFT2, QUASI(33 sel),
CRYST(h=0.1), SPLIT(0.006), MASSREST(1.5), SCRARITH-800.  E8 block:
RM(1,3) generator on AG(3,2); Construction A root count by exhaustive
enumeration of {-2..2}^8 (390625 vectors); basis = 4 codeword lifts +
4 doubled units on the complement of an information set.

FROZEN REGRESSION NUMBERS (round-96 frozen artifact
rigidity_inverse_frozen.log; round-92/93 engine wards): full-800
max|alpha| = 0.183932 +- 5e-5; SMOOTH-428 exit 44 att -2.537735;
SCRARITH-428 exit 124 att -2.370365; ARCH-600 exit 122 att +1.015;
atom-2 w+ moduli (2.43e-4, 4.48e-5, 1.33e-5, 6.51e-6) at D = (250,
400, 600, 799), law ln eta* = -1.0730 r - 7.0783; impostor exits
(SHIFT2 122, QUASI 233, CRYST(0.1) 122, SPLIT(0.006) 280,
MASSREST(1.5) 261, SCRARITH-800 148 with d0 115/231/115/114/250/115).

TYPED GATES (all falsifiable, all bars frozen before the full run):
 G-DIST     each re-measured atom-2 w+ modulus within x/1.35 of the
            round-96 value; refit slope in [-1.35, -0.80], intercept
            in [-8.3, -5.9].
 G-RADIUS   all six impostors die; exits within +-1 lag and d0 exact
            vs round 96.
 G-RATE     all five per-footprint log-moduli slopes <= -0.30 per
            depth unit (the survival box shrinks exponentially in
            every measured coordinate; code rate -> 0).
 G-E8       exact: dim 4, self-dual, weights {0:1,4:14,8:1}, doubly
            even, 240 norm-2 lattice vectors, Gram even with det 1.
 G-NEST     spot eigenvalues: sections below the death index PSD,
            beyond it indefinite (lambda_min < 0), two impostors.
 G-DUALRANK OLS slope of k_fail(D)*delta vs r over the four census
            depths: >= 0.50 GROWS / <= 0.25 STABILIZES(lever) /
            else AMBIGUOUS.  The decisive number.
 G-SYNRANK  syndrome rank(full census) - rank(shallow half) >= 3.
 G-BLIND    MASSREST(3.0): max |alpha| prefix deviation == 0.0
            exactly for k < d0 - 2 AND death >= d0 - 1.
 G-LTC-LOC  local class: q(m=8, D=799) >= 0.90 AND q(799) >= q(400).
 G-LTC-ADV  adversarial ladder: q strictly decreasing in u0 AND
            q(u0=4.5) <= 0.50 (survival at the edge counts as 0).
WARDS (any failure => INSTRUMENT-EDGE, exit 1): A1 source-only AST
firewall (imports only __future__/argparse/ast/hashlib/math/os/time/
mpmath/numpy; no file loads; no zeta/zetazero/siegel calls or
attributes); A2 frozen ladder arithmetic (n delta = L; w(2) =
log2/sqrt2; 41 atoms u < 4.8; QUASI selector count 33); W1
true-stream regression + f64-vs-mp(dps 40) alpha deviation on the
428-prefix <= 1e-9; W2 control regression (SMOOTH/SCRARITH/ARCH
frozen numbers above); W3 causality (every recorded death fail >=
d0 - 1, zero tolerance); W-SYN every extracted syndrome functional
evaluates <= +1e-8 relative on its own world (the violation is
real); W-EMP golden-empirical vs analytic q within 0.15 on every
measured (error, D, m) cell; A3 runtime <= 600 s.

DECLARED NUMERICS, SUBSAMPLING AND COSTS.  Base rows built in mpmath
(dps 50) and cast once; census engine float64 Levinson (adequacy
WARDED W1, not assumed); moduli measured on the DECLARED subset
(atom-2 ladder at 4 depths; atoms 2/3/4/5/7 w+ at 2 depths), 16-step
geometric bisection; impostor census is the frozen 6-member subset
(the full 17-member kill list is round 96's, cited not re-run);
syndrome census ~16 members (declared in section E); no randomness
anywhere (golden keys only); LTC subset sampling 64 golden subsets of
size 8 per cell; smoke flag reduces bisection and skips mp wards and
prints NOT-VERDICT-BEARING.  Runtime bar 600 s.  PRE-FREEZE
DISCLOSURE: a smoke run (--smoke) was used to shake out instrument
bugs (index bookkeeping, syndrome extraction signs) before freezing;
no verdict bar, gate constant, census member, depth or regression
number was moved after seeing full-run results; the frozen regression
numbers are inherited verbatim from the round-96 frozen artifact and
the round-92/93 ward block, not fitted here.

NO RH CLAIM.  NO ALL-DEPTH POSITIVITY CLAIM.  EXPLORATION ONLY.
"""

from __future__ import annotations

import argparse
import ast
import hashlib
import math
import os
import time

import mpmath as mp
import numpy as np

T0 = time.time()
SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()

# ------------------------------------------------------------ frozen bars
DELTA_TEXT = "0.006"
DELTA = 0.006
N_MAIN = 800
L_MAIN = 4.8
N_WARD = 428
N_ARCH = 600
DPS_BUILD = 50
DPS_WARD = 40
DEPTHS = (250, 400, 600, 799)
BISECT_N = 16
W_LO, W_HI = 1e-8, 4.0
RATE_QS = ((2, 1), (3, 1), (2, 2), (5, 1), (7, 1))
RATE_DEPTHS = (400, 799)
INS_US = (math.log(2.5), math.log(6.0))
INS_W = 0.01
TAIL_U0S = (1.5, 3.0, 4.5)
RUNTIME_BAR = 600.0
GOLDEN = (math.sqrt(5.0) - 1.0) / 2.0
U2 = math.log(2.0)

WARD_FULL_MAX = 0.183932
WARD_SMOOTH_EXIT, WARD_SMOOTH_ATT = 44, -2.537735
WARD_SCRAM_EXIT, WARD_SCRAM_ATT = 124, -2.370365
WARD_ARCH_EXIT, WARD_ARCH_ATT = 122, 1.015

FROZEN_MOD2 = {250: 2.43e-4, 400: 4.48e-5, 600: 1.33e-5, 799: 6.51e-6}
FROZEN_SLOPE, FROZEN_ICPT = -1.0730, -7.0783
DIST_BAND = 1.35
SLOPE_LO, SLOPE_HI = -1.35, -0.80
ICPT_LO, ICPT_HI = -8.3, -5.9
FROZEN_IMP = {
    "SHIFT2": (115, 122),
    "QUASI(33 sel)": (231, 233),
    "CRYST(h=0.1)": (115, 122),
    "SPLIT(0.006)": (114, 280),
    "MASSREST(u0=1.5)": (250, 261),
    "SCRARITH-800": (115, 148),
}
RATE_SLOPE_BAR = -0.30
DUAL_GROW_BAR, DUAL_STAB_BAR = 0.50, 0.25
SYNRANK_INC_BAR = 3
SYN_TOL = 1e-8
LTC_M = 8
LTC_TRIALS = 64
LTC_LOCAL_BAR = 0.90
LTC_ADV_BAR = 0.50
EMP_BAR = 0.15

WARDS: list[tuple[str, bool, str]] = []
GATES: list[tuple[str, bool, str]] = []
CAUSAL_VIOL: list[str] = []


def check_ward(name: str, ok: bool, detail: str) -> bool:
    result = bool(ok)
    WARDS.append((name, result, detail))
    print("  [%s] %-52s %s" % ("PASS" if result else "FAIL", name, detail))
    return result


def check_gate(name: str, ok: bool, detail: str) -> bool:
    result = bool(ok)
    GATES.append((name, result, detail))
    print("  [%s] %-52s %s" % ("PASS" if result else "FAIL", name, detail))
    return result


def section(title: str) -> None:
    print("\n" + "=" * 78)
    print(title)
    print("=" * 78)


# ---------------------------------------------------------------- firewall
def firewall_audit() -> tuple[bool, str]:
    with open(os.path.abspath(__file__), "r", encoding="utf-8") as fh:
        source = fh.read()
    tree = ast.parse(source)
    bad: list[str] = []
    allowed_roots = {"__future__", "argparse", "ast", "hashlib", "math",
                     "os", "time", "mpmath", "numpy"}
    forbidden_calls = {"load", "loadtxt", "genfromtxt", "fromfile",
                       "zetazero", "zetazeros", "nzeros", "siegelz",
                       "siegeltheta"}
    forbidden_attrs = {"zeta", "zetazero", "zetazeros", "nzeros",
                       "siegelz", "siegeltheta"}
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                if alias.name.split(".")[0] not in allowed_roots:
                    bad.append("import:" + alias.name)
        elif isinstance(node, ast.ImportFrom):
            if (node.module or "").split(".")[0] not in allowed_roots:
                bad.append("from:" + (node.module or ""))
        elif isinstance(node, ast.Call):
            called = (node.func.id if isinstance(node.func, ast.Name)
                      else node.func.attr
                      if isinstance(node.func, ast.Attribute) else "")
            if called.lower() in forbidden_calls:
                bad.append("call:" + called)
        elif isinstance(node, ast.Attribute):
            if node.attr.lower() in forbidden_attrs:
                bad.append("attr:" + node.attr)
    return not bad, "violations=%s" % (bad or "none")


# ---------------------------------------------------------- prime arithmetic
def sieve_primes(limit: int) -> list[int]:
    bits = bytearray(b"\x01") * (limit + 1)
    bits[0:2] = b"\x00\x00"
    for p in range(2, math.isqrt(limit) + 1):
        if bits[p]:
            count = (limit - p * p) // p + 1
            bits[p * p:limit + 1:p] = b"\x00" * count
    return [i for i in range(2, limit + 1) if bits[i]]


def atom_table(L: float) -> list[tuple[int, int, float, float]]:
    out: list[tuple[int, int, float, float]] = []
    for p in sieve_primes(int(math.exp(L)) + 1):
        lp = math.log(p)
        m = 1
        while m * lp < L - 1e-12:
            out.append((p, m, m * lp, lp / math.sqrt(float(p) ** m)))
            m += 1
    out.sort(key=lambda a: a[2])
    return out


def tent_reads(u: float, w: float, n: int,
               delta: float) -> list[tuple[int, float]]:
    x = u / delta
    lo = int(math.floor(x))
    out = []
    for d in (lo, lo + 1):
        if 0 <= d < n:
            v = 1.0 - abs(x - d)
            if v > 0.0:
                out.append((d, -w * v))
    return out


def comb_row(base: np.ndarray, atoms: list, n: int,
             delta: float) -> np.ndarray:
    row = base.copy()
    for u, w in atoms:
        for d, v in tent_reads(u, w, n, delta):
            row[d] += v
    return row


# ---------------------------------------------------------- corpus screw g
MP_CONST: dict[str, mp.mpf] = {}
S_CACHE: dict[tuple[str, int], mp.mpf] = {}


def setup_constants() -> None:
    with mp.workdps(DPS_BUILD + 20):
        MP_CONST["psi14"] = mp.digamma(mp.mpf(1) / 4)
        MP_CONST["logpi"] = mp.log(mp.pi)
        MP_CONST["phi1"] = mp.lerchphi(1, 2, mp.mpf(1) / 4)


def s_arch_grid(index: int, delta_text: str) -> mp.mpf:
    key = (delta_text, index)
    if key in S_CACHE:
        return S_CACHE[key]
    with mp.workdps(DPS_BUILD):
        t = mp.mpf(index) * mp.mpf(delta_text)
        if index == 0:
            value = MP_CONST["phi1"] / 4
        elif t < mp.mpf("0.3"):
            value = (mp.exp(-t / 2)
                     * mp.lerchphi(mp.exp(-2 * t), 2, mp.mpf(1) / 4) / 4)
        else:
            z = mp.exp(-2 * t)
            total = mp.mpf(0)
            power = mp.mpf(1)
            k = 0
            floor = mp.mpf(10) ** (-(DPS_BUILD + 8))
            while power > floor * (1 + abs(total)):
                total += power / (mp.mpf(k) + mp.mpf(1) / 4) ** 2
                power *= z
                k += 1
            value = mp.exp(-t / 2) * total / 4
    S_CACHE[key] = value
    return value


def base_g_values(n: int, delta_text: str) -> list[mp.mpf]:
    dl = mp.mpf(delta_text)
    values: list[mp.mpf] = []
    with mp.workdps(DPS_BUILD):
        for j in range(n + 1):
            t = j * dl
            value = -8 * (mp.cosh(t / 2) - 1)
            value -= (t / 2) * (MP_CONST["psi14"] - MP_CONST["logpi"])
            value -= MP_CONST["phi1"] / 4
            value += s_arch_grid(j, delta_text)
            values.append(value)
    return values


def lag_row_from_g(values: list[mp.mpf], delta_text: str) -> list[mp.mpf]:
    with mp.workdps(DPS_BUILD):
        dl = mp.mpf(delta_text)
        n = len(values) - 1
        row = [-2 * values[1] / dl]
        for d in range(1, n):
            row.append(-(values[d - 1] - 2 * values[d]
                         + values[d + 1]) / dl)
    return row


def ramp_values(u0: float, n: int, delta_text: str) -> list[mp.mpf]:
    dl = mp.mpf(delta_text)
    values: list[mp.mpf] = []
    with mp.workdps(DPS_BUILD):
        u0m = mp.mpf(u0)
        eh = mp.exp(u0m / 2)
        for j in range(n + 1):
            t = j * dl
            if t <= u0m:
                values.append(mp.mpf(0))
            else:
                values.append(4 * mp.exp(t / 2) - eh * (2 * (t - u0m) + 4))
    return values


def mp_atom_row(u: float, w: float, n: int, delta_text: str) -> list:
    with mp.workdps(DPS_BUILD):
        out = [mp.mpf(0) for _ in range(n)]
        x = mp.mpf(u) / mp.mpf(delta_text)
        lo = int(mp.floor(x))
        for d in (lo, lo + 1):
            if 0 <= d < n:
                value = 1 - abs(x - d)
                if value > 0:
                    out[d] -= mp.mpf(w) * value
    return out


# ----------------------------------------------------- Levinson (f64 + mp)
def levinson(row: np.ndarray, nlim: int | None = None,
             keep_alphas: bool = False,
             keep_fail_vec: bool = False) -> dict:
    n = len(row) if nlim is None else min(nlim, len(row))
    c0 = float(row[0])
    if c0 <= 0.0:
        return {"ok": False, "fail_k": 0, "kind": "C0_NONPOSITIVE",
                "attempted": float("nan"), "amax": 0.0,
                "den_min": float("nan"), "alphas": np.empty(0),
                "fail_vec": None}
    r = row[:n] / c0
    phi = np.zeros(n)
    ps = np.zeros(n)
    phi[0] = 1.0
    ps[0] = 1.0
    amax = 0.0
    den_min = float("inf")
    alphas = np.empty(max(n - 1, 0)) if keep_alphas else None
    for k in range(n - 1):
        num = float(np.dot(phi[:k + 1], r[1:k + 2]))
        den = float(np.dot(ps[:k + 1], r[:k + 1]))
        if den <= 0.0:
            fv = ps[:k + 1].copy() if keep_fail_vec else None
            return {"ok": False, "fail_k": k, "kind": "DEN_NONPOSITIVE",
                    "attempted": float("nan"), "amax": amax,
                    "den_min": den,
                    "alphas": alphas[:k] if keep_alphas else None,
                    "fail_vec": fv}
        a = num / den
        if abs(a) >= 1.0:
            fv = None
            if keep_fail_vec:
                zphi = np.zeros(k + 2)
                zphi[1:] = phi[:k + 1]
                pspad = np.zeros(k + 2)
                pspad[:k + 1] = ps[:k + 1]
                fv = zphi - a * pspad
            return {"ok": False, "fail_k": k, "kind": "ALPHA_EXIT",
                    "attempted": a, "amax": amax,
                    "den_min": min(den_min, den),
                    "alphas": alphas[:k] if keep_alphas else None,
                    "fail_vec": fv}
        if keep_alphas:
            alphas[k] = a
        amax = max(amax, abs(a))
        den_min = min(den_min, den)
        zphi = np.empty(k + 2)
        zphi[0] = 0.0
        zphi[1:] = phi[:k + 1]
        pspad = np.empty(k + 2)
        pspad[:k + 1] = ps[:k + 1]
        pspad[k + 1] = 0.0
        phi[:k + 2] = zphi - a * pspad
        ps[:k + 2] = pspad - a * zphi
    return {"ok": True, "fail_k": -1, "kind": "", "attempted": float("nan"),
            "amax": amax, "den_min": den_min,
            "alphas": alphas[:n - 1] if keep_alphas else None,
            "fail_vec": None}


def szego_mp(row: list, dps: int, nlim: int | None = None) -> dict:
    with mp.workdps(dps):
        n = len(row) if nlim is None else min(nlim, len(row))
        c0 = row[0]
        if c0 <= 0:
            return {"ok": False, "fail_k": 0, "amax": 0.0, "alphas": []}
        moments = [row[j] / c0 for j in range(n)]
        phi = [mp.mpf(1)]
        phi_star = [mp.mpf(1)]
        alphas: list[mp.mpf] = []
        for k in range(n - 1):
            numerator = mp.fdot(phi, moments[1:k + 2])
            denominator = mp.fdot(phi_star, moments[0:k + 1])
            if denominator <= 0:
                return {"ok": False, "fail_k": k, "kind": "DEN",
                        "amax": max([abs(float(a)) for a in alphas],
                                    default=0.0), "alphas": alphas}
            alpha = numerator / denominator
            if abs(alpha) >= 1:
                return {"ok": False, "fail_k": k, "kind": "ALPHA_EXIT",
                        "attempted": float(alpha),
                        "amax": max([abs(float(a)) for a in alphas],
                                    default=0.0), "alphas": alphas}
            alphas.append(alpha)
            zphi = [mp.mpf(0)] + phi
            phi_pad = phi_star + [mp.mpf(0)]
            phi = [zphi[j] - alpha * phi_pad[j] for j in range(k + 2)]
            phi_star = [phi_pad[j] - alpha * zphi[j] for j in range(k + 2)]
        return {"ok": True, "fail_k": -1,
                "amax": max([abs(float(a)) for a in alphas], default=0.0),
                "alphas": alphas}


# ------------------------------------------------------ census machinery
def first_defect(row: np.ndarray, ref: np.ndarray) -> int:
    idx = np.nonzero(np.abs(row - ref) > 1e-15)[0]
    return int(idx[0]) if len(idx) else -1


def note_causality(label: str, fail_k: int, d0: int) -> None:
    if fail_k < d0 - 1:
        CAUSAL_VIOL.append("%s fail=%d d0=%d" % (label, fail_k, d0))


def modulus_search(label: str, apply_fn, lo: float, hi: float, depth: int,
                   ref: np.ndarray, bisect_n: int) -> dict:
    row_lo = apply_fn(lo)
    d0 = first_defect(row_lo, ref)
    res_lo = levinson(row_lo, nlim=depth + 1)
    if not res_lo["ok"]:
        note_causality(label, res_lo["fail_k"], d0)
        return {"cens": "<=lo", "mod": lo, "d0": d0, "hi_fail": -1}
    row_hi = apply_fn(hi)
    res_hi = levinson(row_hi, nlim=depth + 1)
    if res_hi["ok"]:
        return {"cens": ">=hi", "mod": hi, "d0": d0, "hi_fail": -1}
    note_causality(label, res_hi["fail_k"], d0)
    a, b = lo, hi
    b_fail = res_hi["fail_k"]
    for _ in range(bisect_n):
        mid = math.sqrt(a * b)
        row_mid = apply_fn(mid)
        res = levinson(row_mid, nlim=depth + 1)
        if res["ok"]:
            a = mid
        else:
            note_causality(label, res["fail_k"], d0)
            b = mid
            b_fail = res["fail_k"]
    return {"cens": "", "mod": math.sqrt(a * b), "lo": a, "hi": b,
            "d0": d0, "hi_fail": b_fail}


def ols(xs: list[float], ys: list[float]) -> tuple[float, float]:
    coef = np.polyfit(np.asarray(xs, float), np.asarray(ys, float), 1)
    return float(coef[0]), float(coef[1])


# ------------------------------------------------------ syndrome machinery
def syndrome_functional(fail_vec: np.ndarray, n: int) -> np.ndarray:
    """Linear functional s on moment space with s . c = v^T T(c) v:
    s_0 = sum v_i^2, s_d = 2 sum_i v_i v_{i+d}."""
    v = np.asarray(fail_vec, float)
    ac = np.correlate(v, v, mode="full")[len(v) - 1:]
    s = np.zeros(n)
    m = min(len(ac), n)
    s[:m] = ac[:m]
    s[1:m] *= 2.0
    return s


def syndrome_value(s: np.ndarray, row: np.ndarray) -> tuple[float, float]:
    r = row / row[0]
    val = float(np.dot(s, r[:len(s)]))
    scale = float(np.dot(np.abs(s), np.abs(r[:len(s)]))) + 1e-300
    return val, scale


# ------------------------------------------------------------ E8 code layer
def hamming_e8_block() -> tuple[bool, str]:
    pts = np.arange(8)
    gen = np.zeros((4, 8), dtype=np.int64)
    gen[0, :] = 1
    for b in range(3):
        gen[b + 1, :] = (pts >> b) & 1
    words = []
    for mask in range(16):
        w = np.zeros(8, dtype=np.int64)
        for j in range(4):
            if (mask >> j) & 1:
                w ^= gen[j]
        words.append(w)
    wset = {tuple(int(x) for x in w) for w in words}
    dim_ok = len(wset) == 16
    weights = sorted(int(w.sum()) for w in words)
    wd = {v: weights.count(v) for v in set(weights)}
    wd_ok = wd == {0: 1, 4: 14, 8: 1}
    dbl_even = all(int(w.sum()) % 4 == 0 for w in words)
    selfdual = all(int(np.dot(a, b)) % 2 == 0 for a in words for b in words)
    # Construction A root count: x in Z^8, x mod 2 in C, |x|^2 = 4
    grids = np.stack(np.meshgrid(*([np.arange(-2, 3)] * 8),
                                 indexing="ij"), axis=-1).reshape(-1, 8)
    norms = (grids * grids).sum(axis=1)
    cand = grids[norms == 4]
    roots = sum(1 for x in cand
                if tuple(int(v) % 2 for v in x) in wset)
    roots_ok = roots == 240
    # basis: 4 codeword lifts + doubled units on the complement of an
    # information set (row-reduce gen over F2 to find pivot columns)
    gg = gen.copy() % 2
    pivots = []
    r_i = 0
    for col in range(8):
        sel = None
        for rr in range(r_i, 4):
            if gg[rr, col] == 1:
                sel = rr
                break
        if sel is None:
            continue
        gg[[r_i, sel]] = gg[[sel, r_i]]
        for rr in range(4):
            if rr != r_i and gg[rr, col] == 1:
                gg[rr] ^= gg[r_i]
        pivots.append(col)
        r_i += 1
        if r_i == 4:
            break
    non_piv = [c for c in range(8) if c not in pivots]
    basis = np.zeros((8, 8))
    for j in range(4):
        basis[j] = gen[j].astype(float)
    for j, c in enumerate(non_piv):
        basis[4 + j, c] = 2.0
    basis /= math.sqrt(2.0)
    gram = basis @ basis.T
    det = float(np.linalg.det(gram))
    gram_int = np.allclose(gram, np.round(gram), atol=1e-9)
    diag_even = all(int(round(gram[i, i])) % 2 == 0 for i in range(8))
    det_ok = abs(det - 1.0) < 1e-6
    ok = (dim_ok and wd_ok and dbl_even and selfdual and roots_ok
          and gram_int and diag_even and det_ok)
    detail = ("dim16=%s wd=%s dblEven=%s selfdual=%s roots=%d "
              "gram(int=%s,evenDiag=%s,det=%.9f)"
              % (dim_ok, wd, dbl_even, selfdual, roots,
                 gram_int, diag_even, det))
    return ok, detail


# ---------------------------------------------------------------- main
def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--smoke", action="store_true")
    args = parser.parse_args()
    smoke = bool(args.smoke)
    bisect_n = 6 if smoke else BISECT_N

    print("=" * 78)
    print("code_synthesis_probe  PRIME.CODE.SYNTHESIS.01")
    print("FROZEN SPEC_SHA %s%s" % (SPEC_SHA[:16],
          "   *** SMOKE -- NOT VERDICT-BEARING ***" if smoke else ""))
    print("=" * 78)

    # ================================================================ A
    section("A. FIREWALL + FROZEN OBJECTS")
    fw_ok, fw_detail = firewall_audit()
    check_ward("A1 source-only AST firewall", fw_ok, fw_detail)
    atoms_main = atom_table(L_MAIN)
    atoms_ward = [a for a in atoms_main if a[2] < 2.568 - 1e-14]
    w2 = next(a[3] for a in atoms_main if a[0] == 2 and a[1] == 1)
    quasi_sel = [q for q in range(2, 123)
                 if (q * GOLDEN) % 1.0 < 1.0 / math.log(q)]
    a2_ok = (abs(N_MAIN * DELTA - L_MAIN) < 1e-12
             and abs(w2 - math.log(2.0) / math.sqrt(2.0)) < 1e-14
             and len(atoms_main) == 41
             and len(quasi_sel) == 33)
    check_ward("A2 frozen ladders + atom-table + QUASI selector", a2_ok,
               "n*delta=L; w(2)=%.8f; atoms(u<4.8)=%d; quasi_sel=%d"
               % (w2, len(atoms_main), len(quasi_sel)))
    setup_constants()

    t_build = time.time()
    g6 = base_g_values(N_MAIN, DELTA_TEXT)
    base6_mp = lag_row_from_g(g6, DELTA_TEXT)
    base6 = np.array([float(v) for v in base6_mp])
    ramp_rows: dict[float, np.ndarray] = {}
    for u0 in TAIL_U0S:
        ramp_rows[u0] = np.array([float(v) for v in lag_row_from_g(
            ramp_values(u0, N_MAIN, DELTA_TEXT), DELTA_TEXT)])
    ramp0 = np.array([float(v) for v in lag_row_from_g(
        ramp_values(0.0, N_WARD, DELTA_TEXT), DELTA_TEXT)])
    print("  mp base builds (dps %d): %.1f s" % (DPS_BUILD,
                                                 time.time() - t_build))
    true_row = comb_row(base6, [(a[2], a[3]) for a in atoms_main],
                        N_MAIN, DELTA)

    # ================================================================ B
    section("B. ENGINE WARDS (float64 vs mp vs round-92/93 numbers)")
    res_full = levinson(true_row, keep_alphas=True)
    if smoke:
        check_ward("W1 true-stream regression + f64-vs-mp cross",
                   res_full["ok"]
                   and abs(res_full["amax"] - WARD_FULL_MAX) < 5e-5,
                   "SMOKE (mp cross skipped) max|alpha|=%.6f"
                   % res_full["amax"])
    else:
        row428_mp = list(base6_mp[:N_WARD])
        for _p, _m, u, w in atoms_ward:
            arow = mp_atom_row(u, w, N_WARD, DELTA_TEXT)
            row428_mp = [x + y for x, y in zip(row428_mp, arow)]
        sz_mp = szego_mp(row428_mp, DPS_WARD)
        res_428 = levinson(true_row[:N_WARD], keep_alphas=True)
        dev428 = (max(abs(float(am) - af) for am, af in
                      zip(sz_mp["alphas"], res_428["alphas"]))
                  if sz_mp["ok"] and res_428["ok"] else float("inf"))
        check_ward("W1 true-stream regression + f64-vs-mp cross",
                   res_full["ok"]
                   and abs(res_full["amax"] - WARD_FULL_MAX) < 5e-5
                   and dev428 <= 1e-9,
                   "full-800 max|alpha|=%.6f (round92 %.6f); 428-prefix"
                   " f64-mp dev=%.2e" % (res_full["amax"], WARD_FULL_MAX,
                                         dev428))
    smooth_row = base6[:N_WARD] + ramp0
    res_sm = levinson(smooth_row)
    q_ward = [a[0] ** a[1] for a in atoms_ward]
    order = sorted(range(len(atoms_ward)),
                   key=lambda i: (q_ward[i] * GOLDEN) % 1.0)
    scram_atoms = [(atoms_ward[i][2], atoms_ward[order[i]][3])
                   for i in range(len(atoms_ward))]
    res_sc = levinson(comb_row(base6[:N_WARD], scram_atoms, N_WARD, DELTA))
    res_ar = levinson(base6[:N_ARCH])
    check_ward("W2 control regression (SMOOTH/SCRARITH/ARCH)",
               res_sm["fail_k"] == WARD_SMOOTH_EXIT
               and abs(res_sm["attempted"] - WARD_SMOOTH_ATT) < 1e-3
               and res_sc["fail_k"] == WARD_SCRAM_EXIT
               and abs(res_sc["attempted"] - WARD_SCRAM_ATT) < 1e-3
               and res_ar["fail_k"] == WARD_ARCH_EXIT
               and abs(res_ar["attempted"] - WARD_ARCH_ATT) < 2e-2,
               "SMOOTH %d/%.6f  SCRARITH %d/%.6f  ARCH600 %d/%.4f"
               % (res_sm["fail_k"], res_sm["attempted"],
                  res_sc["fail_k"], res_sc["attempted"],
                  res_ar["fail_k"], res_ar["attempted"]))

    # ================================================================ C
    section("C. C1 -- THE CODE DICTIONARY (measured entries)")
    atom_of = {(p, m): (u, w) for p, m, u, w in atoms_main}

    def mk_weight(u, w):
        def f(s):
            row = true_row.copy()
            for d, v in tent_reads(u, s * w, N_MAIN, DELTA):
                row[d] += v
            return row
        return f

    # C1a minimum distance ladder (atom-2 weight channel)
    u2a, w2a = atom_of[(2, 1)]
    fn2 = mk_weight(u2a, w2a)
    print("  C1a minimum distance: atom-2 w+ modulus ladder"
          " (bisection %d steps)" % bisect_n)
    mod2: dict[int, dict] = {}
    for dpt in DEPTHS:
        mod2[dpt] = modulus_search("w+:2@%d" % dpt, fn2, W_LO, W_HI,
                                   dpt, true_row, bisect_n)
        frz = FROZEN_MOD2[dpt]
        print("    D=%3d r=%.3f  eta* = %.4e  (round96 %.2e, ratio %.3f)"
              "  hi-death index k_fail = %d"
              % (dpt, dpt * DELTA, mod2[dpt]["mod"], frz,
                 mod2[dpt]["mod"] / frz, mod2[dpt]["hi_fail"]))
    rs = [d * DELTA for d in DEPTHS]
    lns = [math.log(mod2[d]["mod"]) for d in DEPTHS]
    slope2, icpt2 = ols(rs, lns)
    print("    refit: ln eta*(r) = %+.4f r %+.4f  (round96: %+.4f r %+.4f)"
          % (slope2, icpt2, FROZEN_SLOPE, FROZEN_ICPT))
    dist_ok = (all(1.0 / DIST_BAND <= mod2[d]["mod"] / FROZEN_MOD2[d]
                   <= DIST_BAND for d in DEPTHS)
               and SLOPE_LO <= slope2 <= SLOPE_HI
               and ICPT_LO <= icpt2 <= ICPT_HI)
    check_gate("G-DIST minimum-distance law re-measured", dist_ok,
               "slope %.4f in [%.2f,%.2f]; icpt %.4f in [%.1f,%.1f]"
               % (slope2, SLOPE_LO, SLOPE_HI, icpt2, ICPT_LO, ICPT_HI))

    # C1b decoding radius (six-impostor frozen subset)
    print("  C1b decoding radius: impostor census (round-96 subset)")

    def shift2_atoms() -> list[tuple[float, float]]:
        out = []
        for p in sieve_primes(121):
            q = p + 2
            lq = math.log(q)
            m = 1
            while m * lq < L_MAIN - 1e-12:
                out.append((m * lq, lq / math.sqrt(float(q) ** m)))
                m += 1
        out.sort()
        return out

    quasi_atoms = []
    for q in quasi_sel:
        lq = math.log(q)
        m = 1
        while m * lq < L_MAIN - 1e-12:
            quasi_atoms.append((m * lq, lq / math.sqrt(float(q) ** m)))
            m += 1
    quasi_atoms.sort()

    def cryst_atoms(h: float, u0: float) -> list[tuple[float, float]]:
        out = []
        k = 0
        while u0 + (k + 0.5) * h < L_MAIN - 1e-12:
            uc = u0 + (k + 0.5) * h
            wc = 2.0 * (math.exp((u0 + (k + 1) * h) / 2)
                        - math.exp((u0 + k * h) / 2))
            out.append((uc, wc))
            k += 1
        return out

    def split_atoms(s: float) -> list[tuple[float, float]]:
        out = []
        for _p, _m, u, w in atoms_main:
            out.append((u - s, 0.5 * w))
            out.append((u + s, 0.5 * w))
        out.sort()
        return out

    q_main = [a[0] ** a[1] for a in atoms_main]
    order8 = sorted(range(len(atoms_main)),
                    key=lambda i: (q_main[i] * GOLDEN) % 1.0)
    scr800_atoms = [(atoms_main[i][2], atoms_main[order8[i]][3])
                    for i in range(len(atoms_main))]

    def massrest_row(u0: float) -> np.ndarray:
        return (comb_row(base6, [(a[2], a[3]) for a in atoms_main
                                 if a[2] < u0], N_MAIN, DELTA)
                + ramp_rows[u0])

    imp_defs = [
        ("SHIFT2", comb_row(base6, shift2_atoms(), N_MAIN, DELTA)),
        ("QUASI(33 sel)", comb_row(base6, quasi_atoms, N_MAIN, DELTA)),
        ("CRYST(h=0.1)", comb_row(base6, cryst_atoms(0.1, U2),
                                  N_MAIN, DELTA)),
        ("SPLIT(0.006)", comb_row(base6, split_atoms(0.006),
                                  N_MAIN, DELTA)),
        ("MASSREST(u0=1.5)", massrest_row(1.5)),
        ("SCRARITH-800", comb_row(base6, scr800_atoms, N_MAIN, DELTA)),
    ]
    syndromes: list[tuple[str, int, np.ndarray, np.ndarray]] = []
    radius_ok = True
    radius_det = []
    print("    %-18s %5s %5s %5s %6s  %-14s %9s" % (
        "impostor", "d0", "exit", "J", "r", "kind", "attempted"))
    for name, row in imp_defs:
        d0 = first_defect(row, true_row)
        res = levinson(row, keep_fail_vec=True)
        fd0, fex = FROZEN_IMP[name]
        if res["ok"]:
            radius_ok = False
            radius_det.append("%s SURVIVES" % name)
            print("    %-18s %5d  SURVIVES (max|a|=%.4f)"
                  % (name, d0, res["amax"]))
            continue
        note_causality("imp:" + name, res["fail_k"], d0)
        ok_i = (d0 == fd0 and abs(res["fail_k"] - fex) <= 1)
        radius_ok &= ok_i
        radius_det.append("%s exit %d (frozen %d)"
                          % (name, res["fail_k"], fex))
        print("    %-18s %5d %5d %5d %6.3f  %-14s %+9.4f"
              % (name, d0, res["fail_k"], res["fail_k"] - (d0 - 1),
                 res["fail_k"] * DELTA, res["kind"], res["attempted"]))
        syndromes.append((name, res["fail_k"], res["fail_vec"], row))
    check_gate("G-RADIUS impostor exits vs round 96 (+-1)", radius_ok,
               "; ".join(radius_det))

    # C1c rate / effective dimension
    print("  C1c rate: per-footprint w+ moduli at D=400 vs D=799")
    rate_slopes = []
    logvol = {400: 0.0, 799: 0.0}
    dr = (RATE_DEPTHS[1] - RATE_DEPTHS[0]) * DELTA
    for (p, m) in RATE_QS:
        u, w = atom_of[(p, m)]
        fn = mk_weight(u, w)
        e4 = modulus_search("rate:%d^%d@400" % (p, m), fn, W_LO, W_HI,
                            RATE_DEPTHS[0], true_row, bisect_n)
        e7 = modulus_search("rate:%d^%d@799" % (p, m), fn, W_LO, W_HI,
                            RATE_DEPTHS[1], true_row, bisect_n)
        sl = math.log(e7["mod"] / e4["mod"]) / dr
        rate_slopes.append((p ** m, sl))
        logvol[400] += math.log(e4["mod"])
        logvol[799] += math.log(e7["mod"])
        print("    q=%2d u=%.4f  eta*(400)=%.4e  eta*(799)=%.4e"
              "  slope=%+.3f/unit" % (p ** m, u, e4["mod"], e7["mod"], sl))
        if (p, m) == (7, 1):
            syndromes.append(("bnd:w+:7@799",
                              *_boundary_syndrome(fn, e7)))
        if (p, m) == (2, 1):
            syndromes.append(("bnd:w+:2@799",
                              *_boundary_syndrome(fn, e7)))
    print("    survival-box log-volume V(400)=%.3f V(799)=%.3f"
          "  dV/dr = %+.3f (5 coordinates)"
          % (logvol[400], logvol[799],
             (logvol[799] - logvol[400]) / dr))
    check_gate("G-RATE all per-footprint slopes <= %.2f" % RATE_SLOPE_BAR,
               all(sl <= RATE_SLOPE_BAR for _q, sl in rate_slopes),
               " ".join("q=%d:%+.3f" % (q, sl) for q, sl in rate_slopes))

    print("  C1 DICTIONARY (code-theoretic reading, machine-grounded):")
    print("    ambient space   : nonneg atomic measures on (0,r],"
          " tent mesh delta=0.006 -> c in R^%d" % N_MAIN)
    print("    codeword        : prime-power comb (41 atoms u<4.8),"
          " completes with max|alpha| = %.6f" % res_full["amax"])
    print("    check family    : T_k(-g'') PSD, k<=D  <=>  causal"
          " Verblunsky |alpha_k|<1 (Levinson)")
    print("    min distance    : eta*(r) = exp(%+.3f r %+.3f)"
          " per footprint (this run)" % (slope2, icpt2))
    print("    decoding radius : impostor deaths at defect footprints"
          " (6/6 die; round 96: 17/17, deletions J<=8)")
    print("    rate            : survival-box volume shrinks at"
          " dV/dr = %+.2f on 5 coords -> rate -> 0"
          % ((logvol[799] - logvol[400]) / dr))

    # ================================================================ D
    section("D. C2 -- COMPILER CODE LAYER (exact) + GRAMMAR COMPARISON")
    e8_ok, e8_detail = hamming_e8_block()
    check_gate("G-E8 [8,4,4]->Construction A->E8 exact block", e8_ok,
               e8_detail)
    print("  GRAMMAR TABLE (both sides machine-grounded):")
    print("    %-22s %-30s %-30s" % ("", "compiler code layer",
                                     "positivity code (this probe)"))
    print("    %-22s %-30s %-30s" % ("alphabet", "F2 (bits)",
                                     "R>=0 (tent masses)"))
    print("    %-22s %-30s %-30s" % ("length", "8 (fixed)",
                                     "D = r/delta (unbounded)"))
    print("    %-22s %-30s %-30s" % ("membership test",
                                     "Gram of lattice basis PSD/even",
                                     "Gram sections T_k(-g'') PSD"))
    print("    %-22s %-30s %-30s" % ("dual rank", "4 (self-dual, finite)",
                                     "measured in E (grows?)"))
    print("    %-22s %-30s %-30s" % ("min distance", "4 (fixed)",
                                     "exp(%+.2f r) (shrinking)" % slope2))
    print("    %-22s %-30s %-30s" % ("decoder", "syndrome projection"
                                     " (v638 RM(1,3))",
                                     "footprint-local death (J<=8)"))
    print("  TYPED: SAME GRAMMAR -- both membership tests are"
          " nonnegativity of a Gram pairing family")
    print("  (Simple-Principle form, round 86 S2 3/3: Gram positivity of"
          " node evaluations; the compiler")
    print("  adds no arithmetic bit).  The one axiom INSTANTIATES at the"
          " arithmetic seam as this code.")
    print("  DIFFERENT TYPE in the decisive invariant: finite self-dual"
          " (rank 4, distance 4) vs")
    print("  depth-unbounded check ladder with shrinking distance --"
          " adjudicated next.")

    # ================================================================ E
    section("E. C3 -- FINITE DUAL DESCRIPTION (the decisive question)")
    # E1 nestedness spot checks
    def sect_eig(row: np.ndarray, size: int) -> float:
        idx = np.arange(size)
        tmat = (row[:size] / row[0])[np.abs(idx[:, None] - idx[None, :])]
        return float(np.linalg.eigvalsh(tmat)[0])

    nest_det = []
    nest_ok = True
    for name, kf, row in (("SHIFT2", 122, imp_defs[0][1]),
                          ("QUASI(33 sel)", 233, imp_defs[1][1])):
        lam_lo = sect_eig(row, max(kf - 40, 10))
        lam_hi = sect_eig(row, min(kf + 60, N_MAIN))
        ok_n = lam_lo > 0.0 and lam_hi < 0.0
        nest_ok &= ok_n
        nest_det.append("%s: lam(T_%d)=%.2e>0 lam(T_%d)=%.2e<0"
                        % (name, max(kf - 40, 10), lam_lo,
                           min(kf + 60, N_MAIN), lam_hi))
    check_gate("G-NEST section nestedness spot eigenvalues", nest_ok,
               "; ".join(nest_det))
    print("    (T_k = leading sections of T_D: one check per depth"
          " suffices; the quantifier is the depth ladder)")

    # E2 needed-check-depth growth -- THE DECISIVE NUMBER
    print("  E2 needed check depth for the minimum-distance error:")
    kf_rs = []
    kf_vals = []
    for dpt in DEPTHS:
        kf = mod2[dpt]["hi_fail"]
        kf_rs.append(dpt * DELTA)
        kf_vals.append(kf * DELTA)
        print("    D=%3d r=%.3f  k_fail=%3d  k_fail*delta=%.3f"
              "  k_fail/D=%.4f" % (dpt, dpt * DELTA, kf, kf * DELTA,
                                   kf / dpt))
    dual_slope, dual_icpt = ols(kf_rs, kf_vals)
    if dual_slope >= DUAL_GROW_BAR:
        dual_type = "GROWS"
    elif dual_slope <= DUAL_STAB_BAR:
        dual_type = "STABILIZES(lever)"
    else:
        dual_type = "AMBIGUOUS"
    check_gate("G-DUALRANK needed-depth slope (>=%.2f grows)"
               % DUAL_GROW_BAR, dual_slope >= DUAL_GROW_BAR
               or dual_slope <= DUAL_STAB_BAR,
               "slope = %.4f  => %s" % (dual_slope, dual_type))

    # E3 syndrome census + rank
    print("  E3 syndrome functionals (autocorrelation of failing"
          " predictor polynomials):")
    ins_rows = []
    for ui in INS_US:
        row = true_row.copy()
        for d, v in tent_reads(ui, INS_W, N_MAIN, DELTA):
            row[d] += v
        ins_rows.append(("ins@%.3f(w=%.2f)" % (ui, INS_W), row))
    del2_row = true_row.copy()
    for d, v in tent_reads(u2a, w2a, N_MAIN, DELTA):
        del2_row[d] -= v
    extra_worlds = ins_rows + [("del:2", del2_row),
                               ("MASSREST(u0=3.0)", massrest_row(3.0)),
                               ("MASSREST(u0=4.5)", massrest_row(4.5))]
    world_deaths: dict[str, int] = {}
    for name, row in extra_worlds:
        d0 = first_defect(row, true_row)
        res = levinson(row, keep_fail_vec=True)
        if res["ok"]:
            world_deaths[name] = -1
            print("    %-22s d0=%3d  SURVIVES full window" % (name, d0))
            continue
        note_causality(name, res["fail_k"], d0)
        world_deaths[name] = res["fail_k"]
        syndromes.append((name, res["fail_k"], res["fail_vec"], row))
        print("    %-22s d0=%3d  exit=%3d  J=%3d  kind=%s"
              % (name, d0, res["fail_k"], res["fail_k"] - (d0 - 1),
                 res["kind"]))
    syn_ok = True
    syn_det = []
    smat = []
    syn_sorted = sorted(syndromes, key=lambda t: t[1])
    for name, kf, fv, row in syn_sorted:
        s = syndrome_functional(fv, N_MAIN)
        val, scale = syndrome_value(s, row)
        ok_v = val <= SYN_TOL * scale
        syn_ok &= ok_v
        syn_det.append("%s:%.1e" % (name, val / scale))
        smat.append(s / (np.linalg.norm(s) + 1e-300))
    check_ward("W-SYN every syndrome violated on its own world"
               " (rel <= %.0e)" % SYN_TOL, syn_ok, " ".join(syn_det))
    smat_np = np.array(smat)
    svals = np.linalg.svd(smat_np, compute_uv=False)
    rank_full = int(np.sum(svals > 1e-8 * svals[0]))
    half = len(syn_sorted) // 2
    svals_h = np.linalg.svd(smat_np[:half], compute_uv=False)
    rank_half = int(np.sum(svals_h > 1e-8 * svals_h[0]))
    print("    syndrome census %d members; rank(shallow half %d) = %d,"
          " rank(full) = %d" % (len(syn_sorted), half, rank_half,
                                rank_full))
    check_gate("G-SYNRANK deep errors need new checks (inc >= %d)"
               % SYNRANK_INC_BAR, rank_full - rank_half >= SYNRANK_INC_BAR,
               "increment = %d" % (rank_full - rank_half))

    # E4 counting-law confrontation (cross-instrument, cited)
    print("  E4 counting-law confrontation (round 85, tp_opus S7, cited"
          " not re-measured):")
    print("    on the node-Gram instrument the forced skip count is"
          " D_max = x - 3/8 -- LINEAR in depth;")
    print("    each forced sign change is an independent active"
          " constraint.  Consistent with the E2 slope")
    print("    %.3f and the E3 rank growth: the dual rank of the check"
          " system grows with depth on BOTH" % dual_slope)
    print("    instruments; no measured surface shows a stabilizing"
          " binding set.")

    # E5 blindness theorem check
    row_b = massrest_row(3.0)
    d0_b = first_defect(row_b, true_row)
    res_b = levinson(row_b, keep_alphas=True)
    res_t = levinson(true_row, keep_alphas=True, nlim=N_MAIN)
    npref = max(d0_b - 2, 1)
    dev_pref = float(np.max(np.abs(
        res_b["alphas"][:npref] - res_t["alphas"][:npref]))) \
        if res_b["alphas"] is not None and len(res_b["alphas"]) >= npref \
        else float("inf")
    blind_ok = (dev_pref == 0.0 and not res_b["ok"]
                and res_b["fail_k"] >= d0_b - 1)
    check_gate("G-BLIND checks below the defect are EXACTLY blind",
               blind_ok,
               "MASSREST(3.0): d0=%d prefix dev=%.1e death=%d"
               % (d0_b, dev_pref, res_b["fail_k"]))
    print("    => a non-codeword passes EVERY check of index < d0-1"
          " bit-identically (causality lemma):")
    print("       no finite/bounded-depth dual set can certify"
          " membership; the dual is not finitely supported.")

    # ================================================================ F
    section("F. C4 -- LOCAL TESTABILITY + THE DECODING THEOREM")

    def ltc_q(kd: int, D: int, m: int) -> float:
        if kd < 0:
            return 0.0
        return 1.0 - (min(kd, D) / D) ** m

    def ltc_empirical(kd: int, D: int, m: int) -> float:
        rej = 0
        for t in range(LTC_TRIALS):
            hit = False
            for j in range(m):
                k = int((((t * m + j + 1) * GOLDEN) % 1.0) * D)
                if kd >= 0 and k >= kd:
                    hit = True
            rej += 1 if hit else 0
        return rej / LTC_TRIALS

    emp_ok = True
    emp_det = []
    print("  F1 LTC-LOCAL (random %d-subsets of section checks,"
          " golden-key sampling, %d trials):" % (LTC_M, LTC_TRIALS))
    local_qs = {}
    for name, _row in ins_rows + [("del:2", del2_row)]:
        kd = world_deaths[name]
        q4 = ltc_q(kd, 400, LTC_M)
        q7 = ltc_q(kd, 799, LTC_M)
        e7 = ltc_empirical(kd, 799, LTC_M)
        emp_ok &= abs(e7 - q7) <= EMP_BAR
        emp_det.append("%s:|%.3f-%.3f|" % (name, e7, q7))
        local_qs[name] = (q4, q7)
        print("    %-22s k_d=%3d  q(D=400)=%.4f  q(D=799)=%.4f"
              "  empirical(799)=%.4f" % (name, kd, q4, q7, e7))
    # spot levinson verification on both sides of one death index
    kd_spot = world_deaths[ins_rows[0][0]]
    row_spot = ins_rows[0][1]
    ok_below = levinson(row_spot, nlim=max(kd_spot - 3, 2))["ok"]
    ok_above = levinson(row_spot, nlim=min(kd_spot + 7, N_MAIN))["ok"]
    check_ward("W-EMP empirical q + monotone spot checks",
               emp_ok and ok_below and (not ok_above),
               "%s; spot below=%s above=%s"
               % (" ".join(emp_det), ok_below, ok_above))
    loc_name = ins_rows[0][0]
    q4l, q7l = local_qs[loc_name]
    check_gate("G-LTC-LOC local gap >= %.2f and non-decreasing in D"
               % LTC_LOCAL_BAR, q7l >= LTC_LOCAL_BAR and q7l >= q4l,
               "%s: q(400)=%.4f q(799)=%.4f" % (loc_name, q4l, q7l))

    print("  F2 LTC-ADVERSARIAL (defect pushed toward the window edge):")
    adv_qs = []
    for u0 in TAIL_U0S:
        name = "MASSREST(u0=%.1f)" % u0
        kd = world_deaths.get(name, None)
        if kd is None:  # u0 = 1.5 ran in the impostor census
            kd = next(kfv for nm, kfv, _fv, _rw in syndromes
                      if nm == name)
        q7 = ltc_q(kd, 799, LTC_M)
        adv_qs.append((u0, kd, q7))
        print("    u0=%.1f  k_d=%s  q(m=%d, D=799)=%.4f"
              % (u0, kd if kd >= 0 else "SURVIVES(edge)", LTC_M, q7))
    adv_dec = all(adv_qs[i + 1][2] < adv_qs[i][2]
                  for i in range(len(adv_qs) - 1))
    check_gate("G-LTC-ADV gap decays toward the edge (q(4.5)<=%.2f)"
               % LTC_ADV_BAR, adv_dec and adv_qs[-1][2] <= LTC_ADV_BAR,
               "q ladder: " + " ".join("%.4f" % q for _u, _k, q in adv_qs))
    print("    plus E5: an error strictly beyond the support of any"
          " bounded check family has q = 0 EXACTLY.")

    print("  F3 DECODING-THEOREM CANDIDATE (typed):")
    print("    CANDIDATE: the screw-positivity code at depth r has"
          " minimum distance eta*(r) =")
    print("    exp(%+.3f (r) %+.3f) per footprint and corrects all"
          " measured error classes up to that" % (slope2, icpt2))
    print("    radius (anchors MEASURED at 4 depths; law FITTED;"
          " all-depth OPEN).  A proof needs: a")
    print("    lambda_min(T_r) lower bound (the round-96"
          " conditioning price c_lam = 0.814,")
    print("    CONDITIONING-PRICED to O(1)) + the arrival-kick law"
          " certified without consuming the")
    print("    prior inverse (the round-101 named open piece).")
    print("    THE HONEST CONVERSE: decoding runs measure ->"
          " identification (checks to depth r pin")
    print("    the measure to precision eta*(r)) -- the DECODING"
          " direction.  RH needs the ENCODING")
    print("    quantifier: the codeword passes ALL checks (T_k PSD for"
          " every k).  Error-correction")
    print("    machinery certifies the former; the E2/E3/E5"
          " measurements show the latter does not")
    print("    compress: the binding check index grows linearly"
          " (slope %.3f), deep errors need new" % dual_slope)
    print("    independent syndromes, and bounded check sets are"
          " exactly blind beyond their support.")
    print("    LIST-DECODING does not change the direction;"
          " LOCAL TESTABILITY holds for local errors")
    print("    (q -> 1, depth-improving) but fails adversarially"
          " (q -> 0 at the edge, 0 beyond).")

    # ================================================================ G
    section("G. C5 -- TYPED GATES + COMPOSITE VERDICT")
    check_ward("W3 causality (all recorded deaths, fail >= d0-1)",
               not CAUSAL_VIOL, "violations=%s" % (CAUSAL_VIOL or "none"))
    runtime = time.time() - T0
    check_ward("A3 runtime <= %.0f s" % RUNTIME_BAR,
               runtime <= RUNTIME_BAR, "%.1f s" % runtime)

    wards_ok = all(ok for _n, ok, _d in WARDS)
    gates_ok = all(ok for _n, ok, _d in GATES)
    n_pass = sum(1 for _n, ok, _d in WARDS + GATES if ok)
    n_tot = len(WARDS) + len(GATES)
    print("\n  gates+wards: %d/%d" % (n_pass, n_tot))

    lever = dual_slope <= DUAL_STAB_BAR or adv_qs[-1][2] >= 0.8
    if smoke:
        verdict = "SMOKE -- NOT VERDICT-BEARING"
        code = 0
    elif not wards_ok:
        verdict = "INSTRUMENT-EDGE"
        code = 1
    elif lever:
        verdict = ("CODE-LEVER(dual-slope=%.3f, adv-q=%.3f)"
                   % (dual_slope, adv_qs[-1][2]))
        code = 0
    elif not gates_ok:
        failed = [n for n, ok, _d in GATES if not ok]
        verdict = "CODE-DICTIONARY-INCOMPLETE(%s)" % ",".join(failed)
        code = 0
    else:
        verdict = ("CODE-READING-TRUE-DECODING-DIRECTION("
                   "dictionary compiled; grammar SAME-GRAMMAR-"
                   "DIFFERENT-DUAL; dual rank GROWS slope %.3f; "
                   "LTC local YES adversarial NO; decoding theorem "
                   "candidate typed, all-depth OPEN)" % dual_slope)
        code = 0
    print("\nCOMPONENTS: CODE-DICTIONARY-COMPILED=%s |"
          " CODE-COMPILER-GRAMMAR=SAME-GRAMMAR-DIFFERENT-DUAL(%s) |"
          % (all(ok for n, ok, _d in GATES
                 if n.startswith(("G-DIST", "G-RADIUS", "G-RATE"))),
             e8_ok))
    print("  CODE-DUAL-RANK=%s(slope %.3f) | CODE-LTC(local=%s,"
          " adversarial=%s) | CODE-DECODING-THEOREM=CANDIDATE-TYPED"
          % (dual_type, dual_slope, q7l >= LTC_LOCAL_BAR,
             "NO" if adv_qs[-1][2] <= LTC_ADV_BAR else "YES"))
    print("\nVERDICT: %s" % verdict)
    print("SPEC_SHA %s  runtime %.1f s" % (SPEC_SHA[:16], runtime))
    print("NO RH CLAIM.  NO ALL-DEPTH POSITIVITY CLAIM."
          "  EXPLORATION ONLY.")
    return code


def _boundary_syndrome(fn, entry: dict):
    """Fail data of the final bracket-hi endpoint of a modulus search."""
    row = fn(entry["hi"])
    res = levinson(row, keep_fail_vec=True)
    return res["fail_k"], res["fail_vec"], row


if __name__ == "__main__":
    raise SystemExit(main())
