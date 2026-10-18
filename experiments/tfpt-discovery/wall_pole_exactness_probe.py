#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""wall_pole_exactness_probe -- PRIME.PORT.CHEB.EXACT.02
(EXPLORATION ONLY, experiments/; round 64 follow-up to
oddtoeplitz_pole_branch_probe.py (SPEC_SHA b27539e6cd7c235d).  Asks
whether the one-pole Bochner certificate is EXACT, i.e. whether
sup over the two certificate parameters reproduces lam_min(K) itself.
2026-08-11.)

NO RH CLAIM ANYWHERE.  RH is unsolved.  S6 types every result.

--------------------------------------------------------------------
PART 0 -- WHAT CAME BEFORE (one paragraph)
--------------------------------------------------------------------
The predecessor probe proved (elementary, machine-checked) the
three-branch representation theorem for the odd-Toeplitz operator
    A[c]_{ij} = c_{|i-j|} - c_{M-1-i-j},   0 <= i, j < h,  M = 2h,
namely  A[c] >= 0  <=>  c in cl cone{ eps(x) T_.(x) : x in R } + R*1
with eps(x) = -1 for x > 1 and +1 otherwise, together with the
certificate (L5)
    Psi(m, be) := lam_min( Pi Tz(c + m cosh(be .)) Pi )  <=  lam_min A[c]
for every m >= 0, be > 0, Pi the orthoprojector onto 1^perp and
Tz the plain M x M Toeplitz matrix.  With be FROZEN at the value
derived from the zeta pole term 2 cosh(x/2) dx of the Weil explicit
formula (be = D/2 in lag coordinates x = dD) it measured, over the 42
deployed rungs h in [142, 878],
    Psi*/tau  min 0.4081  med 0.7113  max 0.9995,
i.e. the single derived pole atom recovers a median 71% of the wall's
own floor tau = lam_min A[c].  This probe asks where the missing 29%
lives, and it has a sharp a-priori answer to test.

--------------------------------------------------------------------
PART 1 -- THE PREDICTION (proved here; the probe tests it)
--------------------------------------------------------------------
Notation.  W_n = Chebyshev polynomial of the fourth kind,
q_v(x) = sum_{j<h} v_j W_{h-1-j}(x), and (predecessor L3, machine-
checked there and re-checked in S1 here)
    v^T A[c] v = <c, w(v)>,   sum_{d<M} w_d(v) T_d(x) = (1-x) q_v(x)^2.
Continuations of q_v off the segment (all exact, S1):
    q_v(cos th)  = (l_th . v)/sin(th/2),  l_th(i) = sin((h-i-1/2) th),
    q_v(cosh be) = (k_be . v)/sinh(be/2), k_be(i) = sinh((h-i-1/2) be),
    q_v(-cosh be)= (-1)^{h-1} (a_be . v)/cosh(be/2),
                   a_be(i) = (-1)^i cosh((h-i-1/2) be).

P1 (COMPLEMENTARY SLACKNESS).  Let tau = lam_min A[c] and let v be a
    bottom eigenvector.  Every representation
        c - tau delta_0 = gam*1 + int g^{(x)} dmu(x),   mu >= 0
    (one exists, by L4 applied to A[c] - tau I >= 0; the generator set
    is compact after adding the two limit rays -+delta_{M-1}, so the
    cone is closed and the representation exists) satisfies
        supp mu  subset  {x : q_v(x) = 0}  union  {1}  union  {limit rays}.
    PROOF.  0 = v^T (A[c] - tau I) v = int |1-x| q_v(x)^2 dmu(x), an
    integral of a nonnegative function against a nonnegative measure;
    |1-x| q_v(x)^2 = 0 forces x = 1 or q_v(x) = 0.  For the limit rays
    -delta_{M-1} the generator is e_0 e_0^T, contributing (v_0)^2, so
    those carry mass only if v_0 = 0.  QED.

P2 (EXACTNESS CRITERION).  Define the two-parameter certificate
        Psi** := sup_{m >= 0, be > 0} Psi(m, be).
    Then Psi** <= tau always (L5), and
        Psi** = tau
    as soon as SOME optimal mu has at most ONE atom in (1, infty), no
    atom in (-infty, -1), and no mass on the limit rays.
    PROOF.  Write mu = mu_seg + m delta_{x+} with mu_seg supported in
    [-1, 1] and x+ = cosh(be+).  Then
        c - tau delta_0 - gam*1 + m cosh(be+ .) = int_{[-1,1]} g^{(x)} dmu_seg,
    and the right-hand side is the cosine-moment sequence of the
    push-forward of mu_seg under x = cos th, a NONNEGATIVE measure;
    hence its Toeplitz matrix is PSD (Caratheodory-Toeplitz), i.e.
    Psi(m, be+) >= tau.  QED.
    By P1, be+ must be a zero of be |-> k_be . v.  So the prediction is
    twofold and falsifiable:
        (A)  q_v has EXACTLY ONE zero in (1, infty) and NONE below -1;
        (B)  the certificate-optimal be equals that zero, and then
             Psi**/tau = 1 to numerical precision.
    If instead Psi**/tau stays < 1, then by P2 the wall genuinely needs
    two or more exterior atoms (or limit-ray mass) -- also a clean,
    reportable structural fact.

P3 (A KILL, PROVED, NO RUN NEEDED -- recorded so nobody re-walks it).
    One is tempted to strengthen L5 by a Szego envelope: if
    r := c + m cosh(be.) - t delta_0 - gam*1 has Tz(r) > 0, take the
    maximum-entropy (AR) density f_r >= 0 with the same M cosine
    moments; since A[r] = int 2 l_th l_th^T dsig and the sine system
    {sin((h-i-1/2) th)} is orthogonal on [0, 2pi) with norm^2 = pi,
        A[r] >= 2 pi (min_th f_r) I,   hence  tau >= t + 2 pi min f_r,
    which looks strictly better than L5's  tau >= t.  It is not.
    Tz(r) is the compression of multiplication by f_r in the
    exponential system (norm^2 = 2pi), so  2 pi min f_r <= lam_min Tz(r)
    = Psi(m, be) - t  (the last equality because subtracting t delta_0
    shifts Tz by exactly t I).  Therefore
        t + 2 pi min f_r  <=  Psi(m, be)  <=  Psi**
    for EVERY admissible t.  The envelope refinement is dominated by
    Psi** identically.  DEAD BY ALGEBRA.

--------------------------------------------------------------------
PART 2 -- GATES, DECLARED BEFORE THE RUN
--------------------------------------------------------------------
ANTI-CIRCULARITY, and the one place it is deliberately relaxed:
  * the CERTIFICATE Psi**(c) = sup_{m, be} Psi(m, be) is SOURCE-ONLY.
    Its inputs are the source lag vector c and two scalar certificate
    parameters located by concave/unimodal search.  Optimising a
    certificate parameter is not target eigendata (the predecessor
    already optimised m; this probe also optimises be).  No sigma_h,
    no tau, no wall eigenvector enters Psi**.  tau is computed only to
    report the RATIO Psi**/tau.
  * the DUAL-ROOT ANATOMY of S1 deliberately uses the bottom
    eigenvector v of A[c].  That is target eigendata and it is typed
    DIAGNOSTIC, never certificate.  Its role is to predict, and then
    to explain, the source-only number Psi**/tau.  The two are computed
    by disjoint code paths and cross-checked against each other.
WALL-BLINDNESS: S5 runs the prime-free (arch-only) and scrambled-comb
  worlds.  Psi** <= tau holds by L5 in every world, so a control that
  merely fails to certify is a weak control; the SHARP control here is
  the LOCATION of the optimal be and the exterior-root count -- if the
  smooth/scrambled worlds also produce a single exterior root at
  be = D/2 the mechanism is not arithmetic.  Declared kill:
  CONTROLS-SILENT if any control world certifies (Psi** > 0).
TAU-SCREEN: S3 regresses log(Psi**/tau) on log h.  Since Psi** <= tau
  by construction, a slope of 0 with ratio ~ 1 is EXACTNESS, not a
  gain in the h-decay.  The h-decay of the wall is NOT touched by this
  probe and the report says so.
ANTHROPIC NO-GO: unchanged from the predecessor -- the certificate
  consumes the full comb through c and is therefore outside the
  two-moment budget; it is a reformulation and is typed as one.
NO POINTWISE PRIME STATEMENT, NO ENDPOINT ENVELOPE, NO TRANSITION-ONLY
  CERTIFICATE: the certificate is one global matrix positivity per rung.

--------------------------------------------------------------------
FROZEN SPEC
--------------------------------------------------------------------
Ladder: every kz in v563.frame_a_zones() with h in [142, 878].
DIAG_KZ = (9, 12, 22, 25, 26, 29, 32, 44, 46, 55, 64, 82)  (the 12
rungs diagnosed in the predecessor's amendment A1; 6 of them are the
rungs where the frozen-be certificate missed (1/2) mu1).
be bracket for the golden search: BE_LO_S/BE_HI_S = 0.46, 0.58 in
units of be/D; GOLD_EVALS = 26 function evaluations; inner mass m by
M_ITERS = 22 bisections of the concave derivative on an adaptively
doubled bracket (start 8/cosh(be(M-1)), at most MAX_DOUBLE = 24
doublings).  Root search: RG_N = 6000 geometric nodes in
be in [1e-5, 2.0], sign changes refined by 90 bisections; cos-branch
roots counted on 8h uniform nodes in (0, pi).  Unimodality screen:
UNI_KZ = (9, 26, 44) on UNI_N = 21 uniform be/D nodes in the bracket.
Tolerances: ID_TOL = 1e-9 (identity battery), MATCH_TOL = 1e-4
(relative agreement be_opt vs be_root), EXACT_MED = 0.999 and
EXACT_MIN = 0.99 (bars for POLE-CERT-EXACT).
Controls: CTRL_KZ = (9, 26, 44), SCRAMBLE_SEED = 777.

SMOKE-RUN DISCLOSURE.  None.  This file was written from the
predecessor's output plus the proofs P1-P3 above; no scan preceded
it.  The bars were fixed before the first execution.  Any later
change is disclosed as a numbered amendment below.

AMENDMENT A1 (disclosed; added AFTER the first frozen run of this
file, SPEC_SHA c296b2fd5adddca0, 12/14 checks, no kills, verdicts
POLE-CERT-PARTIAL(med 0.9696, min -0.0221) / HALF-TARGET-MET(41/42) /
SINGLE-EXTERIOR-ROOT / BETA-OPT-EQUALS-DUAL-ROOT / CONTROLS-FIRE).
A1 ADDS section S7 only.  It moves NO bar, changes NO enum, adds no
constant and no eigendata; S0-S6 are byte-identical to that run.
REASON.  The first run located be with a SINGLE golden pass over a
bracket of width 0.12, whose terminal resolution is
0.12 * 0.618^24 = 1.4e-6 in be/D.  S4 shows that is not enough on the
deep rungs: at kz = 64 the search stopped at be/D = 0.5000003 while
the dual root sits at 0.5000001 -- a relative misplacement of 4e-7 --
and that already turned Psi** negative.  The first-pass census
therefore measures the SEARCH, not the certificate.  S7 re-runs the
same source-only certificate with two nested golden passes
(half-widths 5e-5 then 5e-9, terminal resolution ~1e-13 in be/D) on
every rung whose first-pass ratio fell below EXACT_MIN, keeps
max(refined, first-pass) (both are valid lower bounds by L5), and in
addition measures the SHARPNESS of the peak: the relative be-window
on which Psi >= tau/2.  Nested refinement of a parameter search is
not new information.

AMENDMENT A2 (disclosed; added after the A1 run, SPEC_SHA
360be3a5b952b181).  A2 ADDS section S8 only; S0-S7 are unchanged and
still print their search-limited numbers, because the failure of the
search is itself the finding.  REASON, and it is a correction of the
PROBE, not of the theory: A1's nested golden passes still plateaued
below tau on many rungs (e.g. kz 40 did not move at all), which read
as a contradiction with S4's SINGLE-EXTERIOR-ROOT and would have
falsified P2.  Two throwaway diagnostics settled it and are disclosed
here in full: (i) a LINEAR rescan of the exterior dual root at 5e-8
resolution over be/D in [0.4990, 0.5010] and a 200k-node log rescan
over [1e-4, 50] confirm there is exactly ONE exterior root, no
cluster; (ii) evaluating Psi at that root with a careful mass
optimisation gives Psi/tau = 1.000000 with m/2D = 0.999999 on kz 44,
40 and 9 -- P2 is EXACT and the deficit was pure search error.  The
mechanism: the peak is about 1e-7 wide in be/D at h ~ 600 while the
golden bracket is 0.12 wide, so value comparisons in the far field
are made between numbers that differ in the eleventh digit and the
contraction walks away from the peak.  S8 therefore replaces the
VALUE search by a SIGN search: bisection on the envelope derivative
dPsi/dbe = m* v^T comp1(Tz(d sinh(be d))) v, which is a single
quadratic form and whose sign is reliable far from the peak.  This
changes no bar, no constant and no enum, uses no eigendata (the
derivative is taken at the certificate's own bottom eigenvector, not
at the wall's), and can only raise Psi**, which is a lower bound for
lam_min A[c] whatever the search returns.
"""
import ast
import hashlib
import math
import os
import sys
import time

import numpy as np
from scipy.linalg import eigh

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)
sys.path.insert(0, os.path.abspath(os.path.join(_HERE, "..", "..",
                                                "verification")))
import v563_paper2_readouts as core  # noqa: E402  READ-ONLY

# ------------------------------------------------------------ frozen spec
H_LO, H_HI = 142, 878
BE_LO_S, BE_HI_S = 0.46, 0.58
GOLD_EVALS = 26
M_ITERS = 22
MAX_DOUBLE = 24
RG_LO, RG_HI, RG_N = 1.0e-5, 2.0, 6000
ROOT_BISECT = 90
COS_NODES_PER_H = 8
DIAG_KZ = (9, 12, 22, 25, 26, 29, 32, 44, 46, 55, 64, 82)
UNI_KZ = (9, 26, 44)
UNI_N = 21
CTRL_KZ = (9, 26, 44)
SCRAMBLE_SEED = 777
ID_TOL = 1.0e-9
MATCH_TOL = 1.0e-4
EXACT_MED, EXACT_MIN = 0.999, 0.99
RNG = np.random.default_rng(20260811)

CHECKS, KILLS, VERDICTS = [], [], []


def check(name, ok, detail="", kill=None):
    CHECKS.append((name, bool(ok)))
    if kill and not ok:
        KILLS.append(kill)
    print("  [%s] %s%s" % ("PASS" if ok else "FAIL", name,
                           ("  -- " + detail) if detail else ""), flush=True)
    return bool(ok)


def section(t):
    print("\n" + "=" * 74)
    print(t)
    print("=" * 74, flush=True)


def spec_sha():
    src = open(os.path.abspath(__file__), encoding="utf-8").read()
    return hashlib.sha256(src.encode("utf-8")).hexdigest()[:16]


def ast_scan(banned):
    src = open(os.path.abspath(__file__), encoding="utf-8").read()
    bad = []
    for node in ast.walk(ast.parse(src)):
        nm = None
        if isinstance(node, ast.Attribute):
            nm = node.attr
        elif isinstance(node, ast.Name):
            nm = node.id
        if nm in banned:
            bad.append(nm)
    return sorted(set(bad))


# --------------------------------------------------------------- machinery
def tz(c):
    i = np.arange(len(c))
    return c[np.abs(i[:, None] - i[None, :])]


def comp1(X):
    """compression of X to 1^perp (exact Householder congruence)."""
    M = X.shape[0]
    u = np.zeros(M)
    u[0] = 1.0
    u -= np.ones(M) / math.sqrt(M)
    u /= np.linalg.norm(u)
    Y = X - 2.0 * np.outer(u, u @ X)
    Y = Y - 2.0 * np.outer(Y @ u, u)
    return Y[1:, 1:]


def lam1(A):
    w, v = eigh(A, subset_by_index=[0, 0])
    return float(w[0]), v[:, 0]


def wall_c(kz, scramble_seed=None, arch_only=False):
    r = core.build_window(kz, scramble_seed=scramble_seed)
    alpha, M, D = r["alpha"], r["M"], r["D"]
    c_at = np.asarray(core.atom_lags_at(alpha, M, np.asarray(r["uu"], float),
                                        2.0 * np.asarray(r["lam"], float))[0],
                      float)
    c_ar = np.asarray(core.arch_lags(M, D), float)
    return (c_ar if arch_only else c_ar + c_at), r


def psi_at(C0, M, be, iters=M_ITERS):
    """sup_{m>=0} lam_min(C0 + m C1(be)).  Concave in m; the derivative
    is v^T C1 v at the bottom eigenvector.  Adaptive upper bracket."""
    C1 = comp1(tz(np.cosh(be * np.arange(M, dtype=float))))
    w0, v = lam1(C0)
    if float(v @ C1 @ v) <= 0.0:
        return w0, 0.0, False
    hi = 8.0 / math.cosh(be * (M - 1))
    grew = 0
    while grew < MAX_DOUBLE:
        _, v = lam1(C0 + hi * C1)
        if float(v @ C1 @ v) <= 0.0:
            break
        hi *= 2.0
        grew += 1
    lo = 0.0
    for _ in range(iters):
        mid = 0.5 * (lo + hi)
        _, v = lam1(C0 + mid * C1)
        if float(v @ C1 @ v) > 0.0:
            lo = mid
        else:
            hi = mid
    m = 0.5 * (lo + hi)
    w, _ = lam1(C0 + m * C1)
    return w, m, grew >= MAX_DOUBLE


def golden_max(f, lo, hi, evals):
    """maximise a unimodal f on [lo, hi] with `evals` evaluations."""
    gr = (math.sqrt(5.0) - 1.0) / 2.0
    x1, x2 = hi - gr * (hi - lo), lo + gr * (hi - lo)
    f1, f2 = f(x1), f(x2)
    n = 2
    while n < evals:
        if f1 < f2:
            lo, x1, f1 = x1, x2, f2
            x2 = lo + gr * (hi - lo)
            f2 = f(x2)
        else:
            hi, x2, f2 = x2, x1, f1
            x1 = hi - gr * (hi - lo)
            f1 = f(x1)
        n += 1
    return (x1, f1) if f1 > f2 else (x2, f2)


def sup_psi_2p(c, D, lo_s=BE_LO_S, hi_s=BE_HI_S, evals=GOLD_EVALS,
               iters=M_ITERS):
    """Psi** = sup_{m, be} Psi(m, be), be/D searched in [lo_s, hi_s]."""
    M = len(c)
    C0 = comp1(tz(c))
    best = {}

    def f(s):
        w, m, cap = psi_at(C0, M, s * D, iters=iters)
        if (not best) or w > best["w"]:
            best.update(w=w, m=m, s=s, cap=cap)
        return w

    s_opt, w_opt = golden_max(f, lo_s, hi_s, evals)
    if w_opt < best["w"]:
        s_opt, w_opt = best["s"], best["w"]
    edge = min(abs(s_opt - lo_s), abs(s_opt - hi_s)) < 1e-6
    return w_opt, s_opt, best["m"], edge


# ------------------------------------------------- dual polynomial off-seg
def dual_hyp(v, betas):
    """e^{-(h-1/2)be} * sum_j v_j sinh((h-j-1/2) be)   (overflow-free);
    same zeros as be |-> q_v(cosh be) on be > 0."""
    h = len(v)
    j = np.arange(h, dtype=float)
    b = np.atleast_1d(np.asarray(betas, float))
    out = np.empty(b.shape[0])
    for s in range(0, b.shape[0], 256):
        bb = b[s:s + 256][None, :]
        t1 = np.exp(-j[:, None] * bb)
        t2 = np.exp(-(2.0 * h - 1.0 - j)[:, None] * bb)
        out[s:s + 256] = 0.5 * (v[:, None] * (t1 - t2)).sum(axis=0)
    return out


def dual_alt(v, betas):
    """e^{-(h-1/2)be} * sum_j v_j (-1)^j cosh((h-j-1/2) be); same zeros
    as be |-> q_v(-cosh be) on be > 0."""
    h = len(v)
    j = np.arange(h, dtype=float)
    sg = v * ((-1.0) ** j)
    b = np.atleast_1d(np.asarray(betas, float))
    out = np.empty(b.shape[0])
    for s in range(0, b.shape[0], 256):
        bb = b[s:s + 256][None, :]
        t1 = np.exp(-j[:, None] * bb)
        t2 = np.exp(-(2.0 * h - 1.0 - j)[:, None] * bb)
        out[s:s + 256] = 0.5 * (sg[:, None] * (t1 + t2)).sum(axis=0)
    return out


def dual_cos(v, ths):
    """sum_j v_j sin((h-j-1/2) th); same zeros as th |-> q_v(cos th)."""
    h = len(v)
    a = h - np.arange(h, dtype=float) - 0.5
    t = np.atleast_1d(np.asarray(ths, float))
    out = np.empty(t.shape[0])
    for s in range(0, t.shape[0], 4096):
        out[s:s + 4096] = np.sin(np.outer(t[s:s + 4096], a)) @ v
    return out


def sign_change_roots(fn, xs, nb=ROOT_BISECT):
    """all sign changes of fn on the ordered grid xs, bisected."""
    y = fn(xs)
    idx = np.nonzero(np.sign(y[:-1]) * np.sign(y[1:]) < 0.0)[0]
    roots = []
    for i in idx:
        a, b = float(xs[i]), float(xs[i + 1])
        fa = float(y[i])
        for _ in range(nb):
            mid = 0.5 * (a + b)
            fm = float(fn(np.array([mid]))[0])
            if fa * fm <= 0.0:
                b = mid
            else:
                a, fa = mid, fm
        roots.append(0.5 * (a + b))
    return roots


# =========================================================== S0
section("S0 -- FRAME, SPEC AND STATIC WARDS")
SHA = spec_sha()
print("  SPEC_SHA (sha256/16 of this file) = %s" % SHA)
print("  frozen: be/D bracket [%.2f, %.2f]  GOLD=%d  M_ITERS=%d  "
      "RG_N=%d" % (BE_LO_S, BE_HI_S, GOLD_EVALS, M_ITERS, RG_N))
BANNED = ("sigma_h", "shat", "s_h", "mu1_target", "frame_b_zones")
bad = ast_scan(BANNED)
check("S0.1 no banned target symbols in source", not bad,
      "scanned %d names" % len(BANNED))
LADDER = [kz for kz in core.frame_a_zones()
          if H_LO <= core.build_window(kz)["h"] <= H_HI]
check("S0.2 deployed ladder recovered", len(LADDER) == 42,
      "%d rungs" % len(LADDER))


# =========================================================== S1
section("S1 -- IDENTITY WARDS for the off-segment continuations of q_v")
worst = {"cos": 0.0, "hyp": 0.0, "alt": 0.0, "pair": 0.0}
for h in (5, 9, 23):
    M = 2 * h
    v = RNG.standard_normal(h)
    j = np.arange(h, dtype=float)

    def qW(x):
        wm1, w0 = 0.0, 1.0
        acc = v[h - 1] * w0
        for n in range(1, h):
            w1 = (2.0 * x + 1.0) if n == 1 else (2.0 * x * w0 - wm1)
            wm1, w0 = w0, w1
            acc += v[h - 1 - n] * w0
        return acc

    for th in (0.31, 1.17, 2.55):
        lhs = qW(math.cos(th))
        rhs = float(np.sin((h - j - 0.5) * th) @ v) / math.sin(th / 2.0)
        worst["cos"] = max(worst["cos"], abs(lhs - rhs) / max(1.0, abs(rhs)))
    for be in (0.07, 0.4, 1.1):
        lhs = qW(math.cosh(be))
        rhs = float(np.sinh((h - j - 0.5) * be) @ v) / math.sinh(be / 2.0)
        worst["hyp"] = max(worst["hyp"], abs(lhs - rhs) / max(1.0, abs(rhs)))
        lhs = qW(-math.cosh(be))
        rhs = ((-1.0) ** (h - 1)
               * float((((-1.0) ** j) * np.cosh((h - j - 0.5) * be)) @ v)
               / math.cosh(be / 2.0))
        worst["alt"] = max(worst["alt"], abs(lhs - rhs) / max(1.0, abs(rhs)))
    c = RNG.standard_normal(M)
    lhs = float(v @ core.odd_toeplitz(c, M) @ v)
    rhs = float(np.asarray(core.lag_weights_from_v(v, h), float) @ c)
    worst["pair"] = max(worst["pair"], abs(lhs - rhs) / max(1.0, abs(rhs)))
for k in ("cos", "hyp", "alt", "pair"):
    check("S1 q_v continuation exact (%s)" % k, worst[k] < ID_TOL,
          "max rel dev %.2e" % worst[k])
# the scaled kernels used for root hunting have the same zeros
h = 17
v = RNG.standard_normal(h)
bs = np.array([0.05, 0.3, 0.9])
sc = np.exp(-(h - 0.5) * bs)
d1 = np.abs(dual_hyp(v, bs)
            - sc * np.array([float(np.sinh((h - np.arange(h) - 0.5) * b) @ v)
                             for b in bs])).max()
d2 = np.abs(dual_alt(v, bs)
            - sc * np.array([float((((-1.0) ** np.arange(h))
                                    * np.cosh((h - np.arange(h) - 0.5) * b))
                                   @ v) for b in bs])).max()
check("S1 scaled root kernels agree with the raw ones",
      max(d1, d2) < 1e-11, "max abs dev %.2e" % max(d1, d2))


# =========================================================== S2
section("S2 -- UNIMODALITY SCREEN for be |-> sup_m Psi(m, be)")
uni_ok = True
for kz in UNI_KZ:
    c, r = wall_c(kz)
    M, D = r["M"], r["D"]
    C0 = comp1(tz(c))
    ss = np.linspace(BE_LO_S, BE_HI_S, UNI_N)
    vals = [psi_at(C0, M, s * D, iters=14)[0] for s in ss]
    va = np.array(vals)
    i = int(np.argmax(va))
    mono = (bool(np.all(np.diff(va[:i + 1]) > 0.0))
            and bool(np.all(np.diff(va[i:]) < 0.0)))
    uni_ok = uni_ok and mono
    print("  kz=%-3d h=%-4d argmax be/D=%.4f  %s  [%s]"
          % (kz, r["h"], ss[i], "unimodal" if mono else "NOT unimodal",
             " ".join("%+.1e" % x for x in va[::4])))
check("S2 be-profile unimodal on the frozen bracket", uni_ok,
      "%d rungs x %d nodes" % (len(UNI_KZ), UNI_N))


# =========================================================== S3
section("S3 -- THE TWO-PARAMETER CERTIFICATE ON THE DEPLOYED LADDER")
print("   kz     h     M   tau          Psi**        Psi**/tau  Psi**/mu1"
      "  be_opt/D    m*/2D-1   edge")
rows = []
t00 = time.time()
for kz in LADDER:
    c, r = wall_c(kz)
    h, M, D = r["h"], r["M"], r["D"]
    tau = float(np.linalg.eigvalsh(core.odd_toeplitz(c, M))[0])
    mu1 = 4.0 * math.sin(math.pi / (2.0 * h + 1.0)) ** 2
    w, s_opt, m, edge = sup_psi_2p(c, D)
    rows.append((kz, h, M, D, tau, w, mu1, s_opt, m))
    print("  %4d %5d %5d  %+.4e  %+.4e  %.6f   %+.4f   %.7f  %+.3e  %s"
          % (kz, h, M, tau, w, w / tau, w / mu1, s_opt,
             m / (2.0 * D) - 1.0, "EDGE" if edge else ""), flush=True)
print("  [%.1fs]" % (time.time() - t00))

ps = np.array([x[5] for x in rows])
tt = np.array([x[4] for x in rows])
mu = np.array([x[6] for x in rows])
hs = np.array([float(x[1]) for x in rows])
Ds = np.array([x[3] for x in rows])
so = np.array([x[7] for x in rows])
rat = ps / tt
npos = int((ps > 0).sum())
nhalf = int((ps >= 0.5 * mu).sum())
print("\n  Psi** > 0 on %d/%d ; Psi** >= (1/2) mu1 on %d/%d"
      % (npos, len(rows), nhalf, len(rows)))
print("  Psi**/tau  min %.6f  med %.6f  max %.6f"
      % (rat.min(), float(np.median(rat)), rat.max()))
print("  Psi**/mu1  min %.4f  med %.4f  max %.4f"
      % ((ps / mu).min(), float(np.median(ps / mu)), (ps / mu).max()))
print("  be_opt/D   min %.7f  med %.7f  max %.7f  (derived value 0.5)"
      % (so.min(), float(np.median(so)), so.max()))
A = np.vstack([np.log(hs), np.ones_like(hs)]).T
sr = np.linalg.lstsq(A, np.log(np.maximum(rat, 1e-300)), rcond=None)[0][0]
sp = np.linalg.lstsq(A, np.log(np.maximum(ps, 1e-300)), rcond=None)[0][0]
st = np.linalg.lstsq(A, np.log(tt), rcond=None)[0][0]
print("  TAU-SCREEN: log Psi** ~ %.4f log h ; log tau ~ %.4f log h ; "
      "log(Psi**/tau) ~ %+.4f log h" % (sp, st, sr))
exact = (float(np.median(rat)) >= EXACT_MED) and (rat.min() >= EXACT_MIN)
check("S3 two-parameter certificate positive on the whole ladder",
      npos == len(rows), "%d/%d" % (npos, len(rows)))
check("S3 certificate never exceeds tau (L5 must hold)",
      bool((rat <= 1.0 + 1e-9).all()), "max ratio %.9f" % rat.max())
check("S3 POLE-CERT-EXACT (med >= %.3f and min >= %.2f)"
      % (EXACT_MED, EXACT_MIN), exact,
      "med %.6f  min %.6f" % (float(np.median(rat)), rat.min()))
VERDICTS.append(("CERT2", "POLE-CERT-EXACT(med %.5f)" % float(np.median(rat))
                 if exact else
                 "POLE-CERT-PARTIAL(med %.4f, min %.4f)"
                 % (float(np.median(rat)), rat.min())))
VERDICTS.append(("HALF2", "HALF-TARGET-MET(%d/%d)" % (nhalf, len(rows))))


# =========================================================== S4
section("S4 -- DUAL-ROOT ANATOMY  (DIAGNOSTIC: uses the bottom "
        "eigenvector; never a certificate)")
print("   kz     h   #roots x>1  be_root/D    be_opt/D     rel dev     "
      "#roots x<-1  #roots in (-1,1)  q_v(cosh be_opt) scaled")
diag = []
t01 = time.time()
for kz in DIAG_KZ:
    c, r = wall_c(kz)
    h, M, D = r["h"], r["M"], r["D"]
    K = core.odd_toeplitz(c, M)
    _, vv = eigh(K, subset_by_index=[0, 0])
    v = vv[:, 0]
    gr = np.geomspace(RG_LO, RG_HI, RG_N)
    rp = sign_change_roots(lambda b: dual_hyp(v, b), gr)
    rn = sign_change_roots(lambda b: dual_alt(v, b), gr)
    th = np.linspace(1e-9, math.pi - 1e-9, COS_NODES_PER_H * h)
    yc = dual_cos(v, th)
    rc = int(np.count_nonzero(np.sign(yc[:-1]) * np.sign(yc[1:]) < 0.0))
    row = [x for x in rows if x[0] == kz][0]
    s_opt = row[7]
    br = (rp[0] / D) if rp else float("nan")
    dev = abs(br / s_opt - 1.0) if rp else float("nan")
    resid = abs(float(dual_hyp(v, np.array([s_opt * D]))[0]))
    scale = float(np.abs(dual_hyp(v, gr)).max())
    diag.append((kz, h, len(rp), br, s_opt, dev, len(rn), rc,
                 resid / max(scale, 1e-300)))
    print("  %4d %5d      %2d     %.7f   %.7f   %.3e       %2d          "
          "%4d          %.3e"
          % (kz, h, len(rp), br, s_opt, dev, len(rn), rc,
             resid / max(scale, 1e-300)), flush=True)
print("  [%.1fs]" % (time.time() - t01))
one_ext = all(d[2] == 1 and d[6] == 0 for d in diag)
devs = [d[5] for d in diag if d[2] == 1]
match = bool(devs) and max(devs) <= MATCH_TOL
check("S4 SINGLE-EXTERIOR-ROOT (exactly one x>1 root, none below -1)",
      one_ext, "%d rungs" % len(diag))
check("S4 BETA-OPT-EQUALS-DUAL-ROOT (rel dev <= %.0e)" % MATCH_TOL,
      match, "max rel dev %.2e" % (max(devs) if devs else float("nan")))
VERDICTS.append(("ROOTS", "SINGLE-EXTERIOR-ROOT" if one_ext
                 else "MULTI-EXTERIOR-ROOT"))
VERDICTS.append(("MATCH", "BETA-OPT-EQUALS-DUAL-ROOT" if match
                 else "BETA-OPT-OFF-DUAL-ROOT"))

print("\n  the law for the optimal branch point (be_opt/D - 1/2):")
dv = so - 0.5
print("    min %+.3e  med %+.3e  max %+.3e" % (dv.min(), float(np.median(dv)),
                                               dv.max()))
for nm, xx in (("D", Ds), ("h", hs), ("alpha", Ds * hs)):
    yy = np.abs(dv)
    good = yy > 0.0
    if int(good.sum()) >= 6:
        sl = np.linalg.lstsq(np.vstack([np.log(xx[good]),
                                        np.ones(int(good.sum()))]).T,
                             np.log(yy[good]), rcond=None)[0]
        pred = sl[0] * np.log(xx[good]) + sl[1]
        ss_res = float(((np.log(yy[good]) - pred) ** 2).sum())
        ss_tot = float(((np.log(yy[good])
                         - np.log(yy[good]).mean()) ** 2).sum())
        print("    log|dev| ~ %+.4f log %s %+.3f   R^2 = %.3f"
              % (sl[0], nm, sl[1], 1.0 - ss_res / max(ss_tot, 1e-300)))


# =========================================================== S5
section("S5 -- CONTROLS (must fire)")
ctrl_ok = True
for kz in CTRL_KZ:
    for nm, cc, rr in (("ARCH-ONLY",) + wall_c(kz, arch_only=True),
                       ("SCRAMBLE",)
                       + wall_c(kz, scramble_seed=SCRAMBLE_SEED + kz)):
        K2 = core.odd_toeplitz(cc, rr["M"])
        tc = float(np.linalg.eigvalsh(K2)[0])
        w, s_opt, m, edge = sup_psi_2p(cc, rr["D"], evals=16, iters=16)
        _, vv = eigh(K2, subset_by_index=[0, 0])
        gr = np.geomspace(RG_LO, RG_HI, RG_N)
        rp = sign_change_roots(lambda b: dual_hyp(vv[:, 0], b), gr)
        ctrl_ok = ctrl_ok and (w <= 0.0)
        print("  kz=%-3d %-10s tau=%+.4e  Psi**=%+.4e  be_opt/D=%.5f  "
              "#roots x>1 = %d %s"
              % (kz, nm, tc, w, s_opt, len(rp),
                 ("(at %s)" % " ".join("%.4f" % (x / rr["D"]) for x in rp[:4]))
                 if rp else ""), flush=True)
check("S5 CONTROLS-FIRE (no control world certifies)", ctrl_ok,
      kill="CONTROLS-SILENT")
VERDICTS.append(("CONTROLS", "CONTROLS-FIRE" if ctrl_ok
                 else "CONTROLS-SILENT"))


# =========================================================== S7 (A1)
section("S7 -- AMENDMENT A1: nested be-refinement of the SAME "
        "source-only certificate")
REF_HALF1, REF_HALF2 = 5.0e-5, 5.0e-9
REF_EVALS, REF_IT1, REF_IT2 = 20, 22, 26
SHARP_KZ = (9, 26, 52, 64)
SHARP_DELTAS = (1e-9, 1e-8, 1e-7, 1e-6, 1e-5, 1e-4, 1e-3)
bad_rows = [x for x in rows if x[5] / x[4] < EXACT_MIN]
print("  refining %d/%d rungs (first-pass ratio < %.2f); two nested "
      "golden passes" % (len(bad_rows), len(rows), EXACT_MIN))
print("    kz     h   ratio 1-pass  ratio refined  be_opt/D refined")
ref = {}
t02 = time.time()
for (kz, h, M, D, tau, w1, mu1, s1, m1) in bad_rows:
    c, _ = wall_c(kz)
    w, s, _, _ = sup_psi_2p(c, D, lo_s=s1 - REF_HALF1, hi_s=s1 + REF_HALF1,
                            evals=REF_EVALS, iters=REF_IT1)
    w, s, _, _ = sup_psi_2p(c, D, lo_s=s - REF_HALF2, hi_s=s + REF_HALF2,
                            evals=REF_EVALS, iters=REF_IT2)
    w = max(w, w1)
    ref[kz] = w
    print("  %4d %5d    %+.6f      %+.6f      %.11f"
          % (kz, h, w1 / tau, w / tau, s), flush=True)
print("  [%.1fs]" % (time.time() - t02))

ps2 = np.array([ref.get(x[0], x[5]) for x in rows])
rat2 = ps2 / tt
npos2 = int((ps2 > 0).sum())
nhalf2 = int((ps2 >= 0.5 * mu).sum())
print("\n  REFINED census:  Psi** > 0 on %d/%d ; Psi** >= (1/2) mu1 on "
      "%d/%d" % (npos2, len(rows), nhalf2, len(rows)))
print("  Psi**/tau  min %.6f  med %.6f  max %.6f"
      % (rat2.min(), float(np.median(rat2)), rat2.max()))
print("  Psi**/mu1  min %.4f  med %.4f  max %.4f"
      % ((ps2 / mu).min(), float(np.median(ps2 / mu)), (ps2 / mu).max()))
if bool((ps2 > 0).all()):
    sr2 = np.linalg.lstsq(A, np.log(rat2), rcond=None)[0][0]
    sp2 = np.linalg.lstsq(A, np.log(ps2), rcond=None)[0][0]
    print("  TAU-SCREEN (refined): log Psi** ~ %.4f log h ; log tau ~ "
          "%.4f log h ; log(Psi**/tau) ~ %+.4f log h" % (sp2, st, sr2))
exact2 = (float(np.median(rat2)) >= EXACT_MED) and (rat2.min() >= EXACT_MIN)
check("S7 A1 refined certificate positive on the whole ladder",
      npos2 == len(rows), "%d/%d" % (npos2, len(rows)))
check("S7 A1 POLE-CERT-EXACT after refinement (med >= %.3f, min >= %.2f)"
      % (EXACT_MED, EXACT_MIN), exact2,
      "med %.6f  min %.6f" % (float(np.median(rat2)), rat2.min()))
VERDICTS.append(("CERT2-A1", "POLE-CERT-EXACT(med %.5f, min %.5f)"
                 % (float(np.median(rat2)), rat2.min()) if exact2 else
                 "POLE-CERT-PARTIAL(med %.4f, min %.4f)"
                 % (float(np.median(rat2)), rat2.min())))
VERDICTS.append(("HALF2-A1", "HALF-TARGET-MET(%d/%d)" % (nhalf2, len(rows))))

print("\n  SHARPNESS of the peak: relative be-window with Psi >= tau/2")
print("    kz     h   alpha    widest delta with Psi(be*(1+delta)) >= tau/2")
for kz in SHARP_KZ:
    row = [x for x in rows if x[0] == kz][0]
    c, r = wall_c(kz)
    D, M, tau = row[3], row[2], row[4]
    s = row[7]
    C0 = comp1(tz(c))
    best_d = 0.0
    for dd in SHARP_DELTAS:
        w, _, _ = psi_at(C0, M, (s * (1.0 + dd)) * D, iters=REF_IT1)
        if w >= 0.5 * tau:
            best_d = dd
    print("  %4d %5d  %6.3f   %.1e" % (kz, r["h"], r["alpha"], best_d),
          flush=True)

# =========================================================== S8 (A2)
section("S8 -- AMENDMENT A2: the same certificate with a SIGN search "
        "(bisection on dPsi/dbe)")
SIGN_ITERS = 34
SIGN_M_ITERS = 24


def psi_grad(C0, M, D, s, iters=SIGN_M_ITERS):
    """(Psi, m*, dPsi/dbe sign carrier) at be = s*D.  Danskin: the
    envelope derivative is m* v^T dC1/dbe v at the bottom eigenvector."""
    be = s * D
    dd = np.arange(M, dtype=float)
    C1 = comp1(tz(np.cosh(be * dd)))
    Cp = comp1(tz(dd * np.sinh(be * dd)))
    w0, v = lam1(C0)
    if float(v @ C1 @ v) <= 0.0:
        return w0, 0.0, float(v @ Cp @ v)
    hi = 8.0 / math.cosh(be * (M - 1))
    for _ in range(MAX_DOUBLE):
        _, v = lam1(C0 + hi * C1)
        if float(v @ C1 @ v) <= 0.0:
            break
        hi *= 2.0
    lo = 0.0
    for _ in range(iters):
        mid = 0.5 * (lo + hi)
        _, v = lam1(C0 + mid * C1)
        if float(v @ C1 @ v) > 0.0:
            lo = mid
        else:
            hi = mid
    m = 0.5 * (lo + hi)
    w, v = lam1(C0 + m * C1)
    return w, m, float(v @ Cp @ v)


def sup_psi_sign(c, D, lo_s=BE_LO_S, hi_s=BE_HI_S, iters=SIGN_ITERS):
    M = len(c)
    C0 = comp1(tz(c))
    a, b = lo_s, hi_s
    wa, ma, ga = psi_grad(C0, M, D, a)
    wb, mb, gb = psi_grad(C0, M, D, b)
    best = max((wa, a, ma), (wb, b, mb))
    if not (ga > 0.0 > gb):
        return best[0], best[1], best[2], True
    for _ in range(iters):
        mid = 0.5 * (a + b)
        w, m, g = psi_grad(C0, M, D, mid)
        if w > best[0]:
            best = (w, mid, m)
        if g > 0.0:
            a = mid
        else:
            b = mid
    w, m, _ = psi_grad(C0, M, D, 0.5 * (a + b), iters=SIGN_M_ITERS + 8)
    if w > best[0]:
        best = (w, 0.5 * (a + b), m)
    return best[0], best[1], best[2], False


SHARP_KZ2 = (9, 18, 26, 44, 52, 64)
print("   kz     h     M   tau          Psi**(sign)  Psi/tau    Psi/mu1"
      "   be_opt/D          m*/2D-1     brk")
rows8 = []
t03 = time.time()
for (kz, h, M, D, tau, w1, mu1, s1, m1) in rows:
    c, _ = wall_c(kz)
    w, s, m, brk = sup_psi_sign(c, D)
    w = max(w, w1, ref.get(kz, -np.inf))
    rows8.append((kz, h, D, tau, w, mu1, s, m))
    print("  %4d %5d %5d  %+.4e  %+.4e  %.7f  %+.5f   %.12f  %+.3e  %s"
          % (kz, h, M, tau, w, w / tau, w / mu1, s, m / (2.0 * D) - 1.0,
             "NOBRACKET" if brk else ""), flush=True)
print("  [%.1fs]" % (time.time() - t03))

ps8 = np.array([x[4] for x in rows8])
rat8 = ps8 / tt
npos8 = int((ps8 > 0).sum())
nhalf8 = int((ps8 >= 0.5 * mu).sum())
print("\n  SIGN-SEARCH census:  Psi** > 0 on %d/%d ; Psi** >= (1/2) mu1 "
      "on %d/%d" % (npos8, len(rows8), nhalf8, len(rows8)))
print("  Psi**/tau  min %.6f  med %.6f  max %.6f"
      % (rat8.min(), float(np.median(rat8)), rat8.max()))
print("  Psi**/mu1  min %.4f  med %.4f  max %.4f"
      % ((ps8 / mu).min(), float(np.median(ps8 / mu)), (ps8 / mu).max()))
mdev8 = np.array([x[7] / (2.0 * x[2]) - 1.0 for x in rows8])
print("  m*/2D - 1  min %+.3e  med %+.3e  max %+.3e  (the Weil pole mass)"
      % (mdev8.min(), float(np.median(mdev8)), mdev8.max()))
if bool((ps8 > 0).all()):
    sr8 = np.linalg.lstsq(A, np.log(rat8), rcond=None)[0][0]
    sp8 = np.linalg.lstsq(A, np.log(ps8), rcond=None)[0][0]
    print("  TAU-SCREEN (sign search): log Psi** ~ %.4f log h ; log tau ~ "
          "%.4f log h ; log(Psi**/tau) ~ %+.4f log h" % (sp8, st, sr8))
exact8 = (float(np.median(rat8)) >= EXACT_MED) and (rat8.min() >= EXACT_MIN)
check("S8 A2 sign-search certificate positive on the whole ladder",
      npos8 == len(rows8), "%d/%d" % (npos8, len(rows8)))
check("S8 A2 certificate still never exceeds tau (L5)",
      bool((rat8 <= 1.0 + 1e-9).all()), "max ratio %.9f" % rat8.max())
check("S8 A2 POLE-CERT-EXACT (med >= %.3f, min >= %.2f)"
      % (EXACT_MED, EXACT_MIN), exact8,
      "med %.6f  min %.6f" % (float(np.median(rat8)), rat8.min()))
VERDICTS.append(("CERT2-A2", "POLE-CERT-EXACT(med %.6f, min %.6f)"
                 % (float(np.median(rat8)), rat8.min()) if exact8 else
                 "POLE-CERT-PARTIAL(med %.4f, min %.4f)"
                 % (float(np.median(rat8)), rat8.min())))
VERDICTS.append(("HALF2-A2", "HALF-TARGET-MET(%d/%d)" % (nhalf8, len(rows8))))

print("\n  cross-check against the S4 dual roots (DIAGNOSTIC vs "
      "SOURCE-ONLY, disjoint code paths):")
dev8 = []
for d in diag:
    kz = d[0]
    s8 = [x[6] for x in rows8 if x[0] == kz][0]
    dev8.append(abs(d[3] / s8 - 1.0))
    print("    kz=%-4d be_root/D=%.12f  be_opt/D=%.12f  rel dev %.2e"
          % (kz, d[3], s8, dev8[-1]))
check("S8 A2 sign search lands on the dual root (rel dev <= %.0e)"
      % MATCH_TOL, max(dev8) <= MATCH_TOL, "max rel dev %.2e" % max(dev8))

print("\n  SHARPNESS: how precisely must the branch point be known?")
print("    kz     h   alpha   widest |delta| with Psi(be*(1+delta)) "
      ">= tau/2")
sh_h, sh_d, sh_a = [], [], []
for kz in SHARP_KZ2:
    row = [x for x in rows8 if x[0] == kz][0]
    c, r = wall_c(kz)
    M, D = r["M"], r["D"]
    tau, s = row[3], row[6]
    C0 = comp1(tz(c))
    best_d = 0.0
    for dd_ in SHARP_DELTAS:
        w, _, _ = psi_grad(C0, M, D, s * (1.0 + dd_))
        wm, _, _ = psi_grad(C0, M, D, s * (1.0 - dd_))
        if min(w, wm) >= 0.5 * tau:
            best_d = dd_
    sh_h.append(float(r["h"]))
    sh_a.append(r["alpha"])
    sh_d.append(max(best_d, 1e-12))
    print("  %4d %5d  %6.3f   %.1e" % (kz, r["h"], r["alpha"], best_d),
          flush=True)
if len(sh_d) >= 4:
    Ash = np.vstack([np.array(sh_a), np.ones(len(sh_a))]).T
    sl = np.linalg.lstsq(Ash, np.log(np.array(sh_d)), rcond=None)[0]
    print("    log(tolerance) ~ %+.3f alpha %+.2f   -> the admissible "
          "relative error in the branch point shrinks like "
          "exp(%.2f alpha)" % (sl[0], sl[1], sl[0]))

# =========================================================== S6
section("S6 -- LOGICAL STATUS, TYPED")
print("""  PROVED HERE (elementary; S1 checks the identities used):
    P1  supp of any optimal cone measure is inside the zero set of the
        dual polynomial q_v (complementary slackness).
    P2  if some optimal measure has at most one atom outside [-1, 1]
        and none on the limit rays, then sup_{m, be} Psi(m, be) equals
        lam_min A[c] EXACTLY.
    P3  the Szego/maximum-entropy envelope refinement of the L5
        certificate is dominated by sup_{m, be} Psi identically --
        dead by algebra, no run needed.
  MACHINE-MEASURED (this run):
    the exterior-root census of q_v, the source-only value
    sup_{m, be} Psi and its ratio to lam_min A[c], the location of the
    optimal branch point relative to the derived pole value D/2, and
    the behaviour of both in the prime-free and scrambled worlds.
  NOT PROVED, GAP NAMED (unchanged from the predecessor):
    nothing here shows the certificate's HYPOTHESIS -- that the
    pole-restored lag sequence is a nonnegative-measure cosine-moment
    sequence.  By the explicit formula that hypothesis is the window's
    share of the zero-side positivity, so this remains a
    REFORMULATION, not a reduction.  Exactness (if measured) upgrades
    the reformulation from lossy to LOSSLESS: it would say the wall's
    floor IS a Caratheodory-Toeplitz positivity plus one explicit
    rank-one pole, with the pole location the unique exterior zero of
    the dual polynomial.  The h-decay of the floor is untouched.
  NO RH CLAIM IS MADE OR IMPLIED BY THIS FILE.""")

section("VERDICTS")
for k, v_ in VERDICTS:
    print("  %-10s %s" % (k, v_))
npass = sum(1 for _, ok in CHECKS if ok)
print("\n  checks %d/%d passed ; kills: %s"
      % (npass, len(CHECKS), ", ".join(KILLS) if KILLS else "none"))
print("  SPEC_SHA %s" % SHA)
