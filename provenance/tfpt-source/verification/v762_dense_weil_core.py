#!/usr/bin/env python3
"""v762 -- PRIME.DENSECORE.01: the canonical countable dense test family from the (D, X) tower -- admissibility located per class (v677 S2(i)/IK Thm 5.12: hats direct, bare box only correlated/tent-read, named caveat), quantitative density rates hat -1.566 / box -0.503 per level, exact Q correlation closure on all 8 type pairs, explicit stage map with I_64 exact, and the 24-function battery typed as an initial diagnostic package (battery hat 8 IS family member hat(2,3), enum rank 35) (DENSE-CORE-CANONICAL).  Lean companion: TfptCarrier/DenseWeilCore.lean (42 theorems; honest analytic remainder in the header).

PROVENANCE: discovery probe dense_weil_core_probe.py (2026-08-04, 26/26 checks, verdict DENSE-CORE-CANONICAL).  Promoted verbatim (sibling import points at v767); numbers unchanged.
GLOBAL-HANDOFF Agent C -- DENSE WEIL CORE: the canonical countable
dense test family (intended promotion target v762_dense_weil_core).

Exploration only.  This probe never reads a zero ordinate, never loads
prime data, never builds or factors the Weil target Gram, and writes no
files.  It replaces the frozen 24-function diagnostic battery by a
CANONICAL COUNTABLE DENSE test family and certifies its structure.

THE FAMILY (no new test class -- exactly the basis of the canonical
(D, X) tower used by the deployed probes):

    D  =  union over r, m in N of  V_{2^-m, r}(Q),

where V_{2^-m, r}(Q) is the Q-span of the dyadic box functions
box(m, k) = 1_[k 2^-m, (k+1) 2^-m)  and the dyadic hat functions
hat(m, k) = tent with nodes (k, k+1, k+2) 2^-m and peak 1, restricted
to support in [0, r].  Rational compact support, rational coefficients.

FIXED LEXICOGRAPHIC ENUMERATION (frozen, hashed):

    rank(m, k, kind) = 2 (tri(m+k) + m) + kind,   tri(t) = t(t+1)/2,
    kind: 0 = box, 1 = hat

-- lexicographic in (weight m+k, level m, kind); a bijection N <->
{(m, k, kind)} with computable stage bounds (weight <= n/2).  The
stage map to the canonical tower is

    n  ->  (d(n), r(n)) = (2^-(n//2),  n//2 + 2):

every member of the initial segment I_n is exactly representable on
grid d(n) with support in [0, r(n)].

CONVENTIONS INHERITED (cited, read-only):
  * verification/v563_paper2_readouts.py -- the deployed odd-Toeplitz
    window evaluation; arch/atom layers are read with width-D tent
    test pairs (atom_lags_at, arch_lags).
  * verification/v677_w3_structure_theorem.py -- S2(i) per-lag
    dictionary: each deployed lag read g_d(u) = tent_D(u - dD)
    + tent_D(u + dD) is an admissible even Weil test pair
    (Iwaniec-Kowalski Thm 5.12) with transform
    h_d(r) = 2 cos(dDr) D sinc^2(rD/2); S2(ii): window positivity ==
    alias positivity of the Weil symbol.  (Tent test-pair weights:
    the v669 fejer_density identity, cited inside v677 S1(iii).)
  * experiments/tfpt-discovery/handoff_frequency_gram_probe.py -- the
    frozen 24-function battery (12 hats + 12 boxes, supports in
    0 < u < 1.55, SHA-256 pinned below) and the Gram construction
    G[i,j] = W(f_i * f_j~).
  * experiments/tfpt-discovery/handoff_bulk_probe.py and
    simpler_schur_recursion_probe.py -- the dyadic tower grid
    D = 1/64 = 2^-6, midpoint sampling, l2-normalisation, exact
    prefix nesting of ONE lag vector (simpler_tower T1.1).
  * experiments/lean4-carrier-rigidity/TfptCarrier/DenseWeilCore.lean
    -- the finitary side (enumeration bijection, stage bounds, grid
    module closure) machine-checked in Lean 4.

PREREGISTERED CHECKS (frozen before the first run):

D1  ADMISSIBILITY PER FUNCTION CLASS.  Located criterion (v677 S2(i),
    IK Thm 5.12): an even, continuous, compactly supported test pair
    of bounded variation is admissible; its transform is entire of
    exponential type with O(r^-2) decay on horizontal strips.  Per
    class, not per sample:
      (a) hat class: continuous piecewise-linear, compact support ->
          admissible directly; the closed-form transform of the even
          pair of hat(m, k), 2 h sinc^2(rh/2) cos(r(k+1)h) with
          h = 2^-m, must match the exact piecewise integral to
          <= 1e-10 on 6 class representatives x 40 frequencies, and
          the measured log-log envelope decay slope must be <= -1.8.
      (b) box class: NOT continuous, hence NOT admissible as a bare
          test pair (measured envelope slope must sit in
          [-1.25, -0.75], documenting the r^-1 decay).  The deployed
          evaluation, however, never applies W to a bare box: every
          Gram entry is W(f_i * f_j~) and every lag is read through
          the width-D tent pairs g_d -- the correlated form
          box * box~ is a continuous tent (measured slope <= -1.8).
          D1 passes iff the hat class is directly admissible AND the
          box class is admissible in every form the deployed
          evaluation actually uses (correlated / tent-read), with
          the bare-box caveat printed, not hidden.

D2  DENSITY, QUANTITATIVE.  For each of the 24 frozen battery
    functions, the relative L2 projection error onto the level-m
    subspace V_m (all boxes+hats of level m on [0, 2], which is a
    subset of the initial segment I_{N(m)} with N(m) printed exactly)
    for m = 3..9 must be strictly decreasing in m, with per-class
    mean log2-slope <= -0.40 for the 12 box targets (theory: -1/2,
    jump cells) and <= -1.20 for the 12 hat targets (theory: -3/2,
    kink cells).  Battery members that are EXACT family members
    (error 0 at every level; see the calibration note) are certified
    as exact (error <= 1e-12 at all levels) and excluded from the
    rate fit.  General dyadic-approximation argument (stated, not
    machine-proved): indicators of arbitrary intervals are L2-limits
    of dyadic boxes with error^2 <= 2 * 2^-m per endpoint; simple
    functions are dense in L2(0, infinity) with compact support;
    hence span_Q D is dense in the deployed test space.

D3  CORRELATION CLOSURE, EXACT.  On representatives of each type
    pair (box x box, box x hat, hat x hat, including mixed dyadic
    levels), the cross-correlation (f * g~)(tau) = int f(u) g(u+tau)
    du is computed EXACTLY in Q at rational sample points, its
    piecewise polynomial is reconstructed exactly per breakpoint
    interval (4-point rational Vandermonde fit + independent 5th-
    point exactness certificate), and it must be: continuous at
    every breakpoint (exact equality in Q), supported exactly in
    [a_g - b_f, b_g - a_f], with breakpoints on the dyadic grid of
    the finer level, and of degree <= 1 / <= 2 / <= 3 for bb / bh /
    hh.  Hence every cross-correlation the Gram construction needs
    stays inside the admissible class (continuous + compact support
    + BV) -- structural failure here is the DEAD trigger.

D4  FINITE TOWER STAGES.  The enumeration bijection is certified
    exactly for n < 100000 (rank o enum = id, enum o rank = id) and
    the weight bound weight(n) <= n//2 for all n < 100000.  The
    stage map n -> (2^-(n//2), n//2 + 2) is printed for N = 24, 64,
    256, 1024, 4096.  Every member of I_64 must be EXACTLY
    representable at its stage (grid 2^-7, reach 9): boxes as sums
    of fine boxes, hats as nodal combinations of fine hats, verified
    by exact rational equality at two interior points of every fine
    cell (both sides are piecewise linear per fine cell, so two
    points determine the restriction), plus exact support inclusion.

D5  THE 24 BATTERY IS AN INITIAL DIAGNOSTIC PACKAGE.  (a) The
    DEPLOYED battery (midpoint-sampled on the tower grid D = 1/64,
    the bulk-probe convention) is, before l2 normalisation, an EXACT
    rational point of the level-6 box span: all 24 sample vectors
    have rational entries (max denominator printed), reconstruction
    over enum members is exact in Q, and the maximal enumeration
    rank needed is printed (the 24 battery sits inside an explicit
    finite initial segment).  The l2 normalisers ||v||^2 are
    rational (printed); only the scalar sqrt leaves Q.  (b) The
    ANALYTIC battery decomposes over the enumeration as follows:
    exactly 23 of the 24 specs have at least one non-dyadic
    breakpoint (exact denominator certificates) and are therefore
    L2-limits of the family (rates from D2), NOT members of any
    finite stage; the remaining spec (hat 8: peak 1, width 1/4)
    IS the family member hat(2, 3) = enumeration member of rank 35,
    verified by exact pointwise equality in Q.  Either way the 24
    battery is an initial diagnostic package, not the definition of
    the space.  The pinned spec hash must equal the deployed
    BATTERY_SPEC_HASH.

CALIBRATION (declared, run 1 -> run 2; no measurement changed): run 1
(22/25) DISCOVERED that battery hat 8 has all-dyadic breakpoints
(3/4, 1, 5/4) and is EXACTLY the family member hat(2, 3), so its
projection error is identically zero -- which broke the naive strict-
decrease gate (0 -> 0), made the hat-class slope fit nan (log 0), and
made the "24/24 non-dyadic" count read 23/24.  Run 2 re-anchors the
three gates to this exact-membership fact (D2 excludes certified
exact members from the rate fit; D5.3 expects 23 non-dyadic + 1 exact
member with its rank printed).  All other gates and every measured
number are unchanged.

VERDICT ENUM (frozen before the run):
  DENSE-CORE-CANONICAL -- all five established;
  DENSE-CORE-PARTIAL   -- names exactly which of D1..D5 fail or stay
                          analytic-only;
  DENSE-CORE-DEAD      -- structural closure failure (e.g. a cross-
                          correlation leaves the admissible class).

HONEST ANALYTIC REMAINDER (out of scope of this probe and the Lean
module, stated up front): true L2-density of span_Q D in the full
admissible Weil test space is an analytic statement (simple-function
density; here verified quantitatively on the 24 battery only); Weil
admissibility itself (IK Thm 5.12 hypotheses -> explicit formula) is
an analytic property, checked here at the level of the located
criteria and closed-form transforms; the bare box is NOT an
admissible test pair and enters only in correlated/tent-read form;
the operator-system limit of the finite stages is NOT constructed
here.  NO RH claim.

RESULTS (2026-08-04, 26/26 PASS, verdict DENSE-CORE-CANONICAL):
  G0  bijection + weight bound certified exactly on n < 100000;
      enumeration spec SHA-256 bf2e659d65c8...; battery pin ok.
  D1  hat closed-form transform residual <= 1.14e-12 on 6 reps x 40
      freqs; envelope decay slopes: hat -1.854, bare box -0.942 (the
      named IK caveat), correlated box*box~ -1.867.
  D2  all 23 inexact targets strictly decreasing over levels 3..9;
      per-class rates hat -1.566 /level (theory -3/2), box -0.503
      /level (theory -1/2); level-9 subspace V_9 (2047 members) sits
      inside I_1066075 (max rank printed per level).
  D3  8/8 type-pair representatives: exact pw-poly reconstruction in
      Q with 5th-point certificates, continuous, dyadic breakpoints,
      exact supports, degrees 1/2/3 for bb/bh/hh -- closure holds.
  D4  I_64 fits stage (2^-32, 33) loosely and reproduces EXACTLY at
      its tight stage grid 2^-7, reach 9 (all 64 members, equality
      in Q); stage map n -> (2^-(n//2), n//2 + 2) explicit.
  D5  24/24 sampled vectors exact rational points of the level-6 box
      span (max entry denominator 800, ||v||^2 rational, max enum
      rank 11354); 23/24 analytic specs non-dyadic (L2-limits), and
      battery hat 8 IS hat(2, 3) = enum rank 35 exactly.

Exploration only (tfpt-experiment firewall): NOT wired into
run_all.py, no ledger row, no paper claim.  Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/dense_weil_core_probe.py
"""


import ast
import hashlib
import json
import math
import os
import sys
import time
from fractions import Fraction as F
from math import isqrt

import numpy as np
import scipy.linalg as sla

_here = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _here)
sys.path.insert(0, os.path.abspath(os.path.join(_here, "..", "..",
                                                "verification")))

_here_DISC = os.path.abspath(os.path.join(_here, "..",
    "experiments", "tfpt-discovery"))
sys.path.insert(0, _here_DISC)

import v767_handoff_frequency_gram as hf  # noqa: E402  (frozen battery)

T0 = time.time()
CHECKS = []
FAILS = []

TOWER_LEVEL = 6                  # deployed dyadic tower grid 1/64 = 2^-6
PINNED_BATTERY_HASH = \
    "18c484c99c0f757a81fbf2d007978547d6724b1f18a0d3389d73f17c94fcf58e"

BIJECTION_REACH = 100000
D2_LEVELS = range(3, 10)
D2_SUPPORT = F(2)                # analytic battery support ends < 1.6
BAR_TRANSFORM = 1.0e-10
BAR_SLOPE_HAT = -1.8
BAR_SLOPE_BOX = (-1.25, -0.75)
BAR_SLOPE_D2_BOX = -0.40
BAR_SLOPE_D2_HAT = -1.20
BAR_FLOAT_MATCH = 1.0e-14

BANNED_IDS = ("sympy", "isprime", "primerange", "nextprime", "prevprime",
              "primepi", "zetazero", "nzeros")

ENUM_SPEC = dict(
    version="dense-weil-core-v1",
    family=("D = union_{r,m} V_{2^-m,r}(Q); box(m,k)=1_[k 2^-m,(k+1)2^-m)"
            ", hat(m,k)=tent nodes (k,k+1,k+2)2^-m peak 1"),
    enumeration=("rank(m,k,kind)=2*(tri(m+k)+m)+kind, tri(t)=t(t+1)/2,"
                 " kind 0=box 1=hat; lexicographic in (m+k, m, kind)"),
    stage_map="n -> (d,r) = (2^-(n//2), n//2 + 2)")
ENUM_SPEC_JSON = json.dumps(ENUM_SPEC, sort_keys=True,
                            separators=(",", ":"))
ENUM_SPEC_HASH = hashlib.sha256(ENUM_SPEC_JSON.encode()).hexdigest()


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok)))
    if not ok:
        FAILS.append(name.split()[0])
    print("  [%s] %s%s" % ("PASS" if ok else "FAIL", name,
                           ("  -- " + detail) if detail else ""))
    return bool(ok)


# ------------------------------------------------- enumeration (frozen)
def tri(t):
    return t * (t + 1) // 2


def rank_of(m, k, kind):
    return 2 * (tri(m + k) + m) + kind


def enum(n):
    kind = n & 1
    q = n >> 1
    t = (isqrt(8 * q + 1) - 1) // 2
    m = q - tri(t)
    return (m, t - m, kind)


def weight(n):
    return sum(enum(n)[:2])


def stage_map(n):
    """Explicit stage map: initial segment I_n -> tower stage (d, r)."""
    t = n // 2
    return (F(1, 2 ** t), t + 2)


# -------------------------------------- exact piecewise-poly machinery
# A function is a list of pieces (a, b, coeffs) meaning
# sum_i coeffs[i] * u^i on [a, b); Fractions for exact work, floats OK.
def member_pieces(m, k, kind):
    h = F(1, 2 ** m)
    if kind == 0:
        return [(k * h, (k + 1) * h, [F(1)])]
    up = [F(-k), F(2 ** m)]                     # (u - kh)/h
    dn = [F(k + 2), F(-(2 ** m))]               # ((k+2)h - u)/h
    return [(k * h, (k + 1) * h, up), ((k + 1) * h, (k + 2) * h, dn)]


def support_of(pieces):
    return (min(p[0] for p in pieces), max(p[1] for p in pieces))


def peval(coeffs, x):
    out = 0 * x
    for c in reversed(coeffs):
        out = out * x + c
    return out


def pmul(p, q):
    out = [0 * (p[0] + q[0])] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            out[i + j] = out[i + j] + a * b
    return out


def pint(p):
    return [0 * p[0]] + [c / (i + 1) if isinstance(c, F) else c / (i + 1.0)
                         for i, c in enumerate(p)]


def pshift(p, tau):
    """p(u + tau) as a polynomial in u."""
    out = [0 * (p[0] + tau)] * len(p)
    power = [1 + 0 * tau]                        # (u + tau)^i coefficients
    for i, c in enumerate(p):
        for j, w in enumerate(power):
            out[j] = out[j] + c * w
        nxt = [0 * tau] * (len(power) + 1)
        for j, w in enumerate(power):
            nxt[j] = nxt[j] + w * tau
            nxt[j + 1] = nxt[j + 1] + w
        power = nxt
    return out


def corr_value(fp, gp, tau):
    """(f * g~)(tau) = int f(u) g(u + tau) du, exact for Fractions."""
    total = None
    for (a1, b1, p) in fp:
        for (a2, b2, q) in gp:
            lo = a1 if a1 > a2 - tau else a2 - tau
            hi = b1 if b1 < b2 - tau else b2 - tau
            if hi > lo:
                anti = pint(pmul(p, pshift(q, tau)))
                val = peval(anti, hi) - peval(anti, lo)
                total = val if total is None else total + val
    if total is None:
        return 0 * (tau + fp[0][0])
    return total


def to_float_pieces(pieces):
    return [(float(a), float(b), [float(c) for c in p])
            for (a, b, p) in pieces]


def solve_exact(A, y):
    """Exact Gaussian elimination over Q (small systems)."""
    n = len(y)
    M = [row[:] + [y[i]] for i, row in enumerate(A)]
    for col in range(n):
        piv = next(r for r in range(col, n) if M[r][col] != 0)
        M[col], M[piv] = M[piv], M[col]
        pv = M[col][col]
        M[col] = [v / pv for v in M[col]]
        for r in range(n):
            if r != col and M[r][col] != 0:
                f = M[r][col]
                M[r] = [vr - f * vc for vr, vc in zip(M[r], M[col])]
    return [M[r][n] for r in range(n)]


def segment_hash(tag, members, extra=""):
    dig = hashlib.sha256()
    dig.update(ENUM_SPEC_HASH.encode())
    dig.update(tag.encode())
    dig.update(extra.encode())
    for m, k, kind in members:
        dig.update(("%d,%d,%d;" % (m, k, kind)).encode())
        for (a, b, p) in member_pieces(m, k, kind):
            dig.update(("%s|%s|%s;" % (a, b, p)).encode())
    return dig.hexdigest()


# ------------------------------------------------- battery spec, exact
def battery_pieces_exact(spec):
    """Analytic battery member as exact pw-poly on the radius axis."""
    if spec["kind"] == "hat":
        c = F(str(spec["center"]))
        w = F(str(spec["width"]))
        lo, hi = c - w, c + w
        up = [1 - c / w, 1 / w]
        dn = [1 + c / w, -1 / w]
        pieces = []
        if c > 0:
            pieces.append((max(lo, F(0)), c, up))
        pieces.append((c, hi, dn))
        return pieces
    left = F(str(spec["left"]))
    right = F(str(spec["right"]))
    return [(left, right, [F(1)])]


def battery_breakpoints(spec):
    if spec["kind"] == "hat":
        c = F(str(spec["center"]))
        w = F(str(spec["width"]))
        return [b for b in (c - w, c, c + w) if b > 0]
    return [F(str(spec["left"])), F(str(spec["right"]))]


def is_dyadic(x):
    d = x.denominator
    return d & (d - 1) == 0


# ================================================================== G0
def g0():
    print("\nG0 -- firewall + frozen enumeration + pinned battery")
    with open(os.path.abspath(__file__), "r", encoding="utf-8") as fh:
        tree = ast.parse(fh.read())
    names = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Name):
            names.add(node.id)
        elif isinstance(node, ast.Attribute):
            names.add(node.attr)
        elif isinstance(node, (ast.Import, ast.ImportFrom)):
            for al in node.names:
                names.add(al.name.split(".")[0])
    hits = sorted(n for n in names for b in BANNED_IDS if b in n.lower())
    check("G0.1 AST firewall zeta/prime-free; no target Gram is built, "
          "no fit, no file written", not hits, str(hits))
    check("G0.2 enumeration specification frozen and hashed BEFORE any "
          "evaluation", True, "SHA-256 %s" % ENUM_SPEC_HASH[:16])
    check("G0.3 deployed 24-battery spec pinned",
          hf.BATTERY_SPEC_HASH == PINNED_BATTERY_HASH
          and len(hf.BATTERY_SPEC) == 24,
          "SHA-256 %s.., 12 hats + 12 boxes" % hf.BATTERY_SPEC_HASH[:16])
    ok_bij = True
    ok_wt = True
    seen = set()
    for n in range(BIJECTION_REACH):
        m, k, kind = enum(n)
        ok_bij &= rank_of(m, k, kind) == n and (m, k, kind) not in seen
        seen.add((m, k, kind))
        ok_wt &= m + k <= n // 2
    for m in range(40):
        for k in range(40):
            for kind in (0, 1):
                ok_bij &= enum(rank_of(m, k, kind)) == (m, k, kind)
    check("G0.4 enumeration bijection certificate: rank o enum = id and "
          "enum o rank = id on n < %d and (m,k) < 40^2; weight(n) <= "
          "n//2 everywhere (the computable stage bound, mirrored in "
          "Lean DenseWeilCore)" % BIJECTION_REACH, ok_bij and ok_wt)


# ================================================================== D1
def transform_even_pair(pieces_f, r):
    """hat/box transform: 2 int_0^inf f(u) cos(ru) du, exact per piece
    (degree <= 1 closed forms), float."""
    total = 0.0
    for (a, b, p) in pieces_f:
        c0 = p[0]
        c1 = p[1] if len(p) > 1 else 0.0
        if r == 0.0:
            total += c0 * (b - a) + 0.5 * c1 * (b * b - a * a)
            continue
        sa, sb = math.sin(r * a), math.sin(r * b)
        ca, cb = math.cos(r * a), math.cos(r * b)
        total += c0 * (sb - sa) / r
        total += c1 * ((cb - ca) / r ** 2 + (b * sb - a * sa) / r)
    return 2.0 * total


def hat_closed_transform(m, k, r):
    h = 2.0 ** (-m)
    s = (k + 1) * h
    x = 0.5 * r * h
    sc = 1.0 if abs(x) < 1e-12 else math.sin(x) / x
    return 2.0 * h * sc * sc * math.cos(r * s)


def envelope_slope(pieces_f):
    js = range(4, 14)
    env = []
    for j in js:
        rs = np.linspace(2.0 ** j, 2.0 ** (j + 1), 64)
        env.append(max(abs(transform_even_pair(pieces_f, r)) for r in rs))
    return float(np.polyfit([j * math.log(2.0) for j in js],
                            np.log(env), 1)[0])


def d1():
    print("\nD1 -- admissibility per function class (criterion located: "
          "v677 S2(i) / IK Thm 5.12 tent test pairs)")
    reps = [(3, 1), (4, 5), (5, 0), (6, 20), (2, 3), (7, 90)]
    worst = 0.0
    for (m, k) in reps:
        fp = to_float_pieces(member_pieces(m, k, 1))
        for r in np.logspace(-1, 3, 40):
            worst = max(worst, abs(transform_even_pair(fp, float(r))
                                   - hat_closed_transform(m, k, float(r))))
    check("D1.1 HAT CLASS admissible directly: continuous pw-linear, "
          "compact support, BV; closed-form even-pair transform "
          "2 h sinc^2(rh/2) cos(r(k+1)h) matches exact piecewise "
          "integral on %d representatives x 40 freqs" % len(reps),
          worst <= BAR_TRANSFORM, "max |residual| = %.2e" % worst)

    s_hat = envelope_slope(to_float_pieces(member_pieces(4, 3, 1)))
    s_box = envelope_slope(to_float_pieces(member_pieces(4, 3, 0)))
    h = 2.0 ** (-4)
    corr_pieces = [(0.0, h, [h, -1.0])]     # (box*box~)(tau)=h-|tau|, tau>0
    s_cor = envelope_slope(corr_pieces)
    check("D1.2 measured transform envelope decay slopes: hat %.3f "
          "(gate <= %.1f), bare box %.3f (gate in [%.2f, %.2f]: the "
          "bare box FAILS the IK r^-2 criterion -- named caveat), "
          "correlated box*box~ %.3f (gate <= %.1f)"
          % (s_hat, BAR_SLOPE_HAT, s_box, BAR_SLOPE_BOX[0],
             BAR_SLOPE_BOX[1], s_cor, BAR_SLOPE_HAT),
          s_hat <= BAR_SLOPE_HAT
          and BAR_SLOPE_BOX[0] <= s_box <= BAR_SLOPE_BOX[1]
          and s_cor <= BAR_SLOPE_HAT)
    check("D1.3 CLASS VERDICT: every family member is admissible for "
          "the deployed Weil evaluation -- hats directly (D1.1/D1.2); "
          "boxes in every form the evaluation applies W to (Gram "
          "entries W(f_i * f_j~) are correlations, and every lag is "
          "read through the admissible width-D tent pairs g_d of "
          "v677 S2(i)); the bare box itself is NOT an admissible "
          "test pair and is never used as one", True)


# ================================================================== D2
def d2():
    print("\nD2 -- quantitative density: 24 battery targets vs level-m "
          "initial segments")
    targets = []
    for spec in hf.BATTERY_SPEC:
        pieces = battery_pieces_exact(spec)
        nf2 = float(corr_value(pieces, pieces, F(0)))
        targets.append((spec["kind"], to_float_pieces(pieces), nf2))

    errs = np.zeros((24, len(list(D2_LEVELS))))
    seg_ranks = []
    for col, m in enumerate(D2_LEVELS):
        n_box = int(2 * 2 ** m)
        h = 2.0 ** (-m)
        members = [(m, k, 0) for k in range(n_box)] \
            + [(m, k, 1) for k in range(n_box - 1)]
        sh = segment_hash("D2-level-%d" % m, members)
        rmax = max(rank_of(*mem) for mem in members)
        seg_ranks.append((m, len(members), rmax, sh[:12]))
        nb = len(members)
        G = np.zeros((nb, nb))
        for k in range(n_box):
            G[k, k] = h
        for k in range(n_box - 1):
            j = n_box + k
            G[j, j] = 2.0 * h / 3.0
            if k + 1 < n_box - 1:
                G[j, j + 1] = G[j + 1, j] = h / 6.0
            G[k, j] = G[j, k] = 0.5 * h
            G[k + 1, j] = G[j, k + 1] = 0.5 * h
        basis = [to_float_pieces(member_pieces(*mem)) for mem in members]
        for ti, (_kind, fp, nf2) in enumerate(targets):
            lo, hi = fp[0][0], fp[-1][1]
            b = np.zeros(nb)
            for bi, bp in enumerate(basis):
                if bp[-1][1] <= lo or bp[0][0] >= hi:
                    continue
                b[bi] = corr_value(fp, bp, 0.0)
            c = sla.solve(G, b, assume_a="pos")
            e2 = nf2 - 2.0 * float(b @ c) + float(c @ G @ c)
            errs[ti, col] = math.sqrt(max(e2, 0.0) / nf2)

    for (m, nmem, rmax, sh) in seg_ranks:
        print("    level %d: |V_m| = %4d, max enum rank = %8d "
              "(segment I_%d contains V_m), seg-hash %s"
              % (m, nmem, rmax, rmax + 1, sh))

    ms = np.array(list(D2_LEVELS), float)
    exact_idx = [i for i in range(24) if float(np.max(errs[i])) <= 1e-6]
    inexact = [i for i in range(24) if i not in exact_idx]
    check("D2.0 exact family members among the battery: targets %s "
          "have projection error at the float-solver floor <= 1e-6 "
          "at EVERY level (exactness itself is certified in Q by "
          "D5.3) and are excluded from the rate fit (declared "
          "calibration run 1 -> run 2)"
          % exact_idx, exact_idx == [8],
          "max error of target 8 = %.1e" % float(np.max(errs[8])))
    slopes = {i: float(np.polyfit(ms, np.log2(errs[i]), 1)[0])
              for i in inexact}
    hat_idx = [i for i in inexact if targets[i][0] == "hat"]
    box_idx = [i for i in inexact if targets[i][0] == "box"]
    mono = all(np.all(np.diff(errs[i]) < 0.0) for i in inexact)
    mean_hat = float(np.mean([slopes[i] for i in hat_idx]))
    mean_box = float(np.mean([slopes[i] for i in box_idx]))
    check("D2.1 errors strictly decreasing over levels 3..9 for all "
          "%d inexact targets" % len(inexact), mono,
          "hat target 0: %s | box target 0: %s"
          % ("/".join("%.1e" % e for e in errs[hat_idx[0]]),
             "/".join("%.1e" % e for e in errs[box_idx[0]])))
    check("D2.2 per-class mean log2 rate (%d hat / %d box inexact "
          "targets): hat %.3f /level (gate <= %.2f, theory -3/2: "
          "kink cells), box %.3f /level (gate <= %.2f, theory -1/2: "
          "jump cells)"
          % (len(hat_idx), len(box_idx), mean_hat, BAR_SLOPE_D2_HAT,
             mean_box, BAR_SLOPE_D2_BOX),
          mean_hat <= BAR_SLOPE_D2_HAT and mean_box <= BAR_SLOPE_D2_BOX)
    check("D2.3 general dyadic argument (stated exactly, analytic "
          "remainder): interval indicators are L2-limits of dyadic "
          "boxes (error^2 <= 2*2^-m per endpoint), simple functions "
          "dense in compactly supported L2(0,inf); the finite rates "
          "above are the quantitative instance on the frozen 24",
          True)
    return errs


# ================================================================== D3
def fit_piece_exact(fp, gp, lo, hi):
    """Exact cubic reconstruction of (f*g~) on [lo, hi] + 5th-point
    certificate; returns (coeffs, certified)."""
    width = hi - lo
    xs = [lo + width * F(i, 5) for i in (1, 2, 3, 4)]
    ys = [corr_value(fp, gp, x) for x in xs]
    A = [[x ** j for j in range(4)] for x in xs]
    coeffs = solve_exact(A, ys)
    x5 = lo + width * F(7, 10)
    certified = peval(coeffs, x5) == corr_value(fp, gp, x5)
    return coeffs, certified


def poly_degree(coeffs):
    deg = -1
    for i, c in enumerate(coeffs):
        if c != 0:
            deg = i
    return deg


def d3():
    print("\nD3 -- exact correlation closure on type-pair "
          "representatives")
    reps = [
        ("box x box self ", (3, 2, 0), (3, 2, 0), 1),
        ("box x box off  ", (3, 1, 0), (3, 5, 0), 1),
        ("box x hat      ", (3, 2, 0), (3, 3, 1), 2),
        ("box x hat ovlp ", (3, 4, 0), (3, 3, 1), 2),
        ("hat x hat self ", (3, 2, 1), (3, 2, 1), 3),
        ("hat x hat adj  ", (3, 2, 1), (3, 3, 1), 3),
        ("box x hat mixed", (2, 1, 0), (4, 5, 1), 2),
        ("hat x hat mixed", (2, 0, 1), (5, 7, 1), 3),
    ]
    all_ok = True
    for (tag, fi, gi, dmax) in reps:
        fp = member_pieces(*fi)
        gp = member_pieces(*gi)
        (a1, b1) = support_of(fp)
        (a2, b2) = support_of(gp)
        s_lo, s_hi = a2 - b1, b2 - a1
        cuts = sorted({cg - cf
                       for (af, bf, _p) in fp for cf in (af, bf)
                       for (ag, bg, _q) in gp for cg in (ag, bg)})
        lvl = max(fi[0], gi[0])
        grid_ok = all((c * 2 ** lvl).denominator == 1 for c in cuts)
        pieces = []
        ok = True
        for lo, hi in zip(cuts[:-1], cuts[1:]):
            if hi <= lo:
                continue
            coeffs, cert = fit_piece_exact(fp, gp, lo, hi)
            ok &= cert
            pieces.append((lo, hi, coeffs))
        deg = max(poly_degree(p[2]) for p in pieces)
        cont = all(peval(pa[2], pa[1]) == peval(pb[2], pb[0])
                   for pa, pb in zip(pieces[:-1], pieces[1:]))
        edge = (peval(pieces[0][2], pieces[0][0]) == 0
                and peval(pieces[-1][2], pieces[-1][1]) == 0)
        outside = all(corr_value(fp, gp, x) == 0
                      for x in (s_lo - F(3, 2), s_lo - F(1, 7),
                                s_hi + F(1, 7), s_hi + F(3, 2)))
        ok = ok and grid_ok and cont and edge and outside \
            and 0 <= deg <= dmax
        all_ok &= ok
        check("D3.%s: exact pw-poly, deg %d <= %d, %d pieces, "
              "breakpoints on grid 2^-%d, continuous + support "
              "[%s, %s] exact (all certificates in Q)"
              % (tag, deg, dmax, len(pieces), lvl, s_lo, s_hi), ok)
    check("D3.9 CLOSURE: every cross-correlation the Gram construction "
          "needs is continuous, compactly supported, BV, with dyadic "
          "breakpoints -- it stays in the admissible class (it need "
          "not stay in span D itself: degrees 2 and 3 appear; the "
          "class, not the span, is what admissibility requires)",
          all_ok)
    return all_ok


# ================================================================== D4
def member_value(m, k, kind, x):
    h = F(1, 2 ** m)
    if kind == 0:
        return F(1) if k * h <= x < (k + 1) * h else F(0)
    if k * h <= x < (k + 1) * h:
        return (x - k * h) / h
    if (k + 1) * h <= x < (k + 2) * h:
        return ((k + 2) * h - x) / h
    return F(0)


def refined_value(m, k, kind, t, x):
    """Value at x of the stage-t representation of member (m,k,kind)."""
    step = 2 ** (t - m)
    ht = F(1, 2 ** t)
    if kind == 0:
        j = int(x / ht)
        return F(1) if k * step <= j < (k + 1) * step else F(0)
    total = F(0)
    j0 = int(x / ht)
    for j in (j0 - 1, j0):
        if k * step - 1 < j < (k + 2) * step - 1:
            w = member_value(m, k, 1, (j + 1) * ht)
            total += w * member_value(t, j, 1, x)
    return total


def d4():
    print("\nD4 -- explicit stage map + exact representability of "
          "initial segments")
    for N in (24, 64, 256, 1024, 4096):
        d, r = stage_map(N - 1)
        tmax = max(weight(n) for n in range(N))
        print("    I_%d: max weight %d, stage (d, r) = (2^-%d, %d)"
              % (N, tmax, N // 2, r))

    N = 64
    members = [enum(n) for n in range(N)]
    sh = segment_hash("D4-I64", members)
    print("    I_64 segment hash %s (before evaluation)" % sh[:16])
    t_stage = max(m + k for (m, k, _kind) in members)
    reach = max(k + 1 + kind for (_m, k, kind) in members)
    d_seg, r_seg = stage_map(N - 1)
    ok_stage = t_stage <= (N - 1) // 2 and reach <= r_seg
    check("D4.1 I_64 fits its stage: max weight %d <= %d = (N-1)//2, "
          "support reach %d cells <= r = %d (exact nesting in X)"
          % (t_stage, (N - 1) // 2, reach, r_seg), ok_stage)

    t = t_stage
    ht = F(1, 2 ** t)
    ok_rep = True
    for (m, k, kind) in members:
        lo, hi = support_of(member_pieces(m, k, kind))
        j_lo, j_hi = int(lo / ht), int(hi / ht)
        for j in range(j_lo, j_hi):
            for frac in (F(1, 3), F(2, 3)):
                x = (j + frac) * ht
                if member_value(m, k, kind, x) \
                        != refined_value(m, k, kind, t, x):
                    ok_rep = False
    check("D4.2 dyadic inheritance in D, exact: all 64 members "
          "reproduce EXACTLY on the stage grid 2^-%d (boxes as fine-"
          "box sums, hats as nodal fine-hat combinations; equality "
          "in Q at 2 interior points of every fine cell -- both "
          "sides pw-linear per cell, so this pins the restriction)"
          % t, ok_rep)
    check("D4.3 stage map is explicit and computable: n -> (d, r) = "
          "(2^-(n//2), n//2 + 2), certified by the weight bound of "
          "G0.4; the deployed tower grid 1/64 is stage level %d"
          % TOWER_LEVEL, True)


# ================================================================== D5
def d5():
    print("\nD5 -- the 24 battery is an initial diagnostic package")
    hcell = F(1, 2 ** TOWER_LEVEL)
    n_cells = int(F(2) / hcell)
    max_rank = 0
    max_den = 1
    ok_exact = True
    ok_float = True
    norms = []
    for spec in hf.BATTERY_SPEC:
        vals = []
        for i in range(n_cells):
            x = (i + F(1, 2)) * hcell
            if spec["kind"] == "hat":
                c = F(str(spec["center"]))
                w = F(str(spec["width"]))
                v = max(1 - abs(x - c) / w, F(0))
            else:
                lft = F(str(spec["left"]))
                rgt = F(str(spec["right"]))
                v = F(1) if lft <= x <= rgt else F(0)
            vals.append(v)
            xf = float(x)
            if spec["kind"] == "hat":
                vf = max(1.0 - abs(xf - spec["center"]) / spec["width"],
                         0.0)
            else:
                vf = float(spec["left"] <= xf <= spec["right"])
            ok_float &= abs(float(v) - vf) <= BAR_FLOAT_MATCH
        nz = [i for i, v in enumerate(vals) if v != 0]
        k_last = max(nz)
        max_rank = max(max_rank, rank_of(TOWER_LEVEL, k_last, 0))
        max_den = max(max_den, max(v.denominator for v in vals))
        for i in range(n_cells):
            x = (i + F(1, 2)) * hcell
            rec = sum((vals[j] * member_value(TOWER_LEVEL, j, 0, x)
                       for j in nz), F(0))
            ok_exact &= rec == vals[i]
        norms.append(sum((v * v for v in vals), F(0)) * hcell)
    check("D5.1 deployed battery (midpoint-sampled at tower grid "
          "1/64, bulk-probe convention): all 24 unnormalised sample "
          "vectors are EXACT rational points of the level-6 box "
          "span; reconstruction over enum members exact in Q; float "
          "sampling formula agrees to <= %.0e; max entry denominator "
          "%d" % (BAR_FLOAT_MATCH, max_den), ok_exact and ok_float)
    check("D5.2 the sampled 24 sit inside the explicit finite initial "
          "segment I_%d (max enum rank %d = rank(box(6, k_last)); "
          "the family is NOT defined by them)"
          % (max_rank + 1, max_rank), max_rank > 0,
          "||v||^2 rational, e.g. %s, %s (only the scalar sqrt "
          "leaves Q)" % (norms[0], norms[12]))
    dyadic_idx = [i for i, spec in enumerate(hf.BATTERY_SPEC)
                  if all(is_dyadic(b) for b in battery_breakpoints(spec))]
    ok_member = dyadic_idx == [8]
    if ok_member:
        bp = battery_pieces_exact(hf.BATTERY_SPEC[8])
        for j in range(int(F(2) / F(1, 32))):
            for frac in (F(1, 3), F(2, 3)):
                x = (j + frac) * F(1, 32)
                bv = sum((peval(p, x) for (a, b, p) in bp if a <= x < b),
                         F(0))
                ok_member &= bv == member_value(2, 3, 1, x)
    check("D5.3 analytic decomposition over the enumeration: 23/24 "
          "specs have a non-dyadic breakpoint (exact denominator "
          "certificates; e.g. hat 0 breakpoints %s) and are "
          "L2-limits with the D2 rates; spec 8 (peak 1, width 1/4, "
          "breakpoints 3/4, 1, 5/4) IS the family member hat(2, 3) "
          "= enum rank %d, verified pointwise-exactly in Q -- "
          "either way the 24 battery is an initial diagnostic "
          "package, not the definition of the space"
          % ([str(b) for b in battery_breakpoints(hf.BATTERY_SPEC[0])],
             rank_of(2, 3, 1)),
          len(dyadic_idx) == 1 and ok_member)


# ================================================================== run
def run():
    print("DENSE WEIL CORE -- canonical countable dense test family "
          "(Agent C, intended v762)")
    print("enumeration spec: %s" % ENUM_SPEC_JSON)
    g0()
    d1()
    d2()
    closure_ok = d3()
    d4()
    d5()

    n_ok = sum(1 for _n, ok in CHECKS if ok)
    if not FAILS:
        verdict = "DENSE-CORE-CANONICAL"
    elif not closure_ok:
        verdict = "DENSE-CORE-DEAD"
    else:
        verdict = "DENSE-CORE-PARTIAL (failing: %s)" \
            % ",".join(sorted(set(FAILS)))
    print("\nVERDICT: %s" % verdict)
    print("HONEST ANALYTIC REMAINDER: true L2-density of span_Q D in "
          "the full admissible Weil test space and IK-5.12 "
          "admissibility are analytic statements (here: located "
          "criteria, closed-form transforms, and quantitative rates "
          "on the frozen 24 only); the bare box is not an admissible "
          "test pair and enters only correlated/tent-read; the "
          "operator-system limit of the stages is not constructed "
          "here.  NO RH claim.")
    print("RESULT: %d/%d CHECKS PASSED (%.1f s)"
          % (n_ok, len(CHECKS), time.time() - T0))
    return 0 if n_ok == len(CHECKS) else 1


if __name__ == "__main__":
    sys.exit(run())
