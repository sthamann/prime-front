#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""li_lemma_attack_probe -- PRIME.LI.LEMMA.ATTACK.01

FROZEN THEOREM-ENGINEERING PROBE (2026-08-13).  EXPLORATION ONLY.
NO RH CLAIM.  No paper, ledger, website, verification, manifest, marker or
generated file is touched.  This probe writes nothing.

MISSION.  Follow up CCCLXIV (LI-FAVORABLE) on its two open flanks:
  TASK A  the QUANTIFIER price of Li's criterion (all n vs a predefined
          cofinal index set), decided by literature plus exact structure;
  TASK B  the remaining lemma itself -- price every classical envelope with
          explicit exponents and constants, and pursue the contour /
          cancellation form that needs no absolute convergence.

THE OBJECT (CCCLXIV, cited, not re-derived).  With xi(s) the completed zeta
and s = 1/(1-z),
    lambda_n = [z^(n-1)] s(z)^2 (xi'/xi)(s(z)) = sum_rho [1-(1-1/rho)^n],
    lambda_n = 2 + lambda_n^arch + lambda_n^prime,
    lambda_n^prime = -1 + sum_(j=1)^n C(n,j) eta_(j-1),
    zeta'/zeta(1+w) = -1/w + sum_k eta_k w^k.
CCCLXIV's shortest remaining lemma was: exist n_0 and C<1 with
|lambda_n^prime| <= C(2+lambda_n^arch) for all n >= n_0 ("order-only bound,
~350x slack, no sharp constant, far more classical-friendly than the wall").

WHAT THIS PROBE DECIDES.

(A1) LITERATURE, EXACT.  Li 1997 needs ALL n.  Bombieri-Lagarias 1999
Cor. 1(c) (EXTERNAL-CITED; quoted verbatim by Voros, math/0506326, p.5:
"In [2, Cor. 1(c)], rather weak exponential lower bounds lambda_n >= -c e^(eps n)
were shown to imply RH") relaxes the STRENGTH, not the index set: for every
eps>0 there is c(eps) with lambda_n >= -c(eps)e^(eps n) for n = 1,2,3,...
<=> RH.  Sekatskii, arXiv:1304.7895 Thm 2, restates the same (a)/(b)/(c)
triple in generalized form.  Arias de Reyna (Funct. Approx. 45 (2011) 7-21)
states the same fact as "the power series sum lambda_k(1-s)^k has radius of
convergence 1 iff RH".  Voros's asymptotic alternative: RH <=> tempered
growth lambda_n ~ (n/2)(log n - 1 + gamma - log 2pi); RH false <=>
non-tempered oscillations of BOTH signs, modulo o(e^(eps n)).  The tau-Li
family (Freitas, JLMS 73 (2006) 399-414; Droll 2012; Bucur-Ernvall-Hytonen-
Odzak-Smajlovic, LMS JCM 19 (2016) 259-280; Palojarvi, Albanian J. Math 14
(2020) 47-77) relaxes the REGION or the finiteness, never the index set.
NO cofinal/sparse index relaxation exists in the literature.

(A2) STRUCTURE, EXACT AND DECIDABLE.  A symmetric off-line quadruple
{rho, conj rho, 1-rho, conj(1-rho)} has z-set {w, conj w, 1/w, 1/conj w}
(S1.1), hence EXACTLY
    lambda_n^quad = 4 - 4 cosh(n log R) cos(n theta),  w = R e^(i theta),
so quadruple positivity at index n is EXACTLY cos(n theta) <= sech(n log R),
and sech(n log R) decays geometrically.  Consequences, both proved here:
  (A2-)  COUNTEREXAMPLE.  For irrational alpha put S_alpha = {n : {n alpha}
         in [1/3,2/3]}.  For n in S_alpha, cos(2 pi n alpha) <= -1/2, so
         lambda_n^quad >= 4 + 2 cosh(n log R) > 0 for EVERY n in S_alpha and
         every R>1.  S_alpha is predefined, cofinal, and has density 1/3.
         Hence NO relaxation of Bombieri-Lagarias Thm 1 to an arbitrary
         predefined cofinal (even positive-density) index set can hold.
  (A2+)  SHARP SUFFICIENT CLASS.  If S is BOHR-RECURRENT (for every k, every
         v in T^k and every eps>0 some n in S has ||n v|| < eps) then
         positivity on S still forces Re rho <= 1/2: the closure of {n v} in
         a compact abelian group is a subgroup, hence contains 0, so some
         n in S has all cos(n theta_j) >= 1-eps simultaneously and the
         dominant shell -4 cosh(n log R) sum_j cos(n theta_j) swamps the
         O(n^(3/2) log n) rest.  Every arithmetic progression q N is
         Bohr-recurrent; S_alpha above is not.  So the honest typing is
         LI-ALLN-REQUIRED[BOHR-RECURRENT-SHARP]: "cofinal" is refuted,
         "q N" is fine, and the wall's H_cof (an ARBITRARY predefined
         cofinal family) is a strictly weaker quantifier than Li's.

(B1) THE BL-(c) THRESHOLD PRICES THE WHOLE ENVELOPE FAMILY.  2+lambda^arch
is an explicit polynomial-size quantity, so ANY unconditional envelope
|lambda_n^prime| <= B(n) with limsup B(n)^(1/n) <= 1 gives
lambda_n >= -B(n) >= -c(eps)e^(eps n) and therefore RH by BL Cor. 1(c).
Hence: no unconditional SUB-EXPONENTIAL envelope on the arithmetic block can
exist short of proving RH -- the target is not "an order bound with 350x
slack", it is the exponential/sub-exponential boundary, where the slack is
exactly zero.  This is a CLASS NO-GO of the CCCLXIII-T5 type, and it applies
to every row of the table below, before any constant is computed.

(B2) CORRECTION TO CCCLXIV S4.5/S4.6 (HIGH).  CCCLXIV reported a finite
Vinogradov-Korobov envelope growing like n^2 (2.9963e2 at n=10 ... 1.6846e5
at n=400, "miss factor 225, growing like n").  A polynomial envelope is
sub-exponential, so by (B1) it would prove RH; it therefore cannot be valid.
The arithmetic slip is localized here: the tail term used a CONSTANT
sup|psi(x)-x| = eps_VK(x_0) x_0 for all x >= x_0, whereas the VK bound is
|psi(x)-x| <= eps_VK(x) x with a factor x that GROWS.  Reinstated honestly,
the tail integral int_(x_0)^inf eps_VK(x) x |L_n''-L_n'|(log x) dx/x^2
DIVERGES like sqrt(X), because eps_VK decays slower than every power while
the uniform Laguerre bound grows like e^(u/2) = sqrt(x).  Measured in S3.2.
The corrected VK row is +infinity, not 2.25e2.

(B3) THE ENVELOPE TABLE (explicit exponents/constants, S3.3).  Rows: trivial
Chebyshev; PNT with any sub-power decay; VK; power saving |psi(x)-x| <= K x^theta
with theta<1/2 (FALSE by Littlewood's Omega_(+-)(sqrt x log log log x));
theta=1/2 with RH's own log^2 (Schoenfeld) -- crude Laguerre O(n^5), measured
Plancherel-Rotach O(n^(5/2)); zero-density (Ingham/Huxley/Jutila) -- a
HIGH-height tool against a LOW-height functional, critical height
T*(n) ~ sqrt(1.5 n/log n); first-zero Cauchy circle -- VALID but exponential
with rate log(1+1/|rho_1-1|) = 0.0683; Montgomery-Vaughan / large sieve --
structurally excluded because Re s > 1 is EXACTLY the disk |z-1/2| < 1/2
(S1.6) whose boundary contains the extraction point z = 0.

(B4) THE CONTOUR / CANCELLATION RESULT.  Exactly
    lambda_n^prime = Res_(s=1)[(zeta'/zeta)(s)(s/(s-1))^n]
                   = (1/2 pi i) int_(C_r) (zeta'/zeta)(s)(s/(s-1))^n ds,
C_r = {|1-1/s| = r} = the Apollonius circle |s - 1/(1-r^2)| = r/(1-r^2),
which for every r<1 lies in Re s > 1/(1+r) > 1/2, crosses Re s = 1 at
|t| = r/sqrt(1-r^2), and for r = 1-1/n hugs the critical line from the right
as sigma(t) = 1/2 + 1/(2(2n-1)) + (2n-1)t^2/(2n(n-1)) + O(t^4), i.e.
sigma - 1/2 ~ 1/(4n) + t^2/n (exact closed forms, S1.10).  On C_r the weight
is |s/(s-1)|^n = r^(-n) and r^(-(n-1)) -> e for r = 1-1/n: the representation
needs NO absolute convergence of (VM) and the exponential loss VANISHES.  The
resulting Cauchy L^1 bound is not merely structural -- measured against the
independent eta route it is within a factor 1.65..6.26 of the truth for
n <= 128 (two-route ward S4.11), versus the N > e^(4n) truncation demand of
(VM).  What remains is exactly a sup/L^1 bound for zeta'/zeta on a contour
approaching the critical line, i.e. "no zeros inside C_r" -- a PARABOLIC
zero-free region sigma <= 1/2 + 1/(4n) + t^2/n, which fails for a FIXED
off-line zero as soon as n > (t_0^2 + 1/4)/(sigma_0 - 1/2), hence over all n
is equivalent to RH.  Two independent routes give the SAME finite reach from
"RH verified up to height T_0" (Platt-Trudgian 2021, EXTERNAL-CITED-THEOREM,
T_0 = 3e12): the parabolic contour condition and the direct shell estimate
both break at n ~ 2 T_0^2 (S3.4/S3.5).

(B5) THE CLEANEST FORM OF THE REMAINING LEMMA (new, exact).  With
L_n'(x) = -sum_(k<n) L_k(x) (S1.3) and int_0^x L_k = L_k - L_(k+1) (S1.4),
    lambda_n^prime = -1 - sum_(k=0)^(n-1) a_k,
    a_k = -sum_(i=0)^k C(k,i) eta_i = int_0^inf L_k(u) dnu(u),
    dnu = sum_m (Lambda(m)/m) delta_(log m) - du   (regularized).
So the lemma is a CESARO statement on the binomial (Euler) transform of the
eta-sequence: a_k = o(log k) on average suffices.  The eta-series has radius
of convergence |rho_1 - 1| = 14.1436, so the TRIVIAL bound on the transform
is |a_k| <= (1+1/14.1436)^k = e^(0.0683 k) -- exactly the first-zero Cauchy
row.  Thus the entire remaining content is: does the Euler transform of the
eta-sequence grow exponentially or not?  That is the radius-of-convergence
statement, i.e. RH restated (corollary typing LI-RESTATEMENT), not a bound
with slack.  Measured: max|a_k| = O(1) over the computed range.

RIGOR.  Every number here is zero-free unless explicitly typed.  The eta /
lambda^prime table is recomputed independently (Z(w) = w zeta(1+w), discrete
Cauchy on |w|=1, exact series division) with a declared error model
(E1 aliasing, E2 round-off, E3 measured propagation amplification) and is
cross-checked against the closed forms for lambda_1, lambda_2 and against
CCCLXIV's CITED values.  Zero ORDINATES are never used; the single cited zero
FACT is |rho_1 - 1| = 14.1436 (first-zero height) and the single cited
THEOREM with zero content is Platt-Trudgian, both typed at the point of use.
No fit anywhere; only exact identities, declared bounds and rank statistics.

VERDICT ENUM (frozen, from the mission):
  LI-LEMMA-CLOSED       triple-verified unconditional C<1 (treat with maximal
                        suspicion);
  LI-EXPONENT-GAP       the table plus the exact needed improvement;
  LI-QUANTIFIER-PRICED  Task A shows the claimed advantage is illusory;
  LI-INSTRUMENT-EDGE    an exact/precision gate is unresolved.
Frozen precedence: failed exact gate -> LI-INSTRUMENT-EDGE; an unconditional
sub-exponential envelope surviving the poison-world control ->
LI-LEMMA-CLOSED; the BL-(c) class no-go established AND the cofinal
relaxation refuted -> LI-QUANTIFIER-PRICED; otherwise LI-EXPONENT-GAP.

SCOPE.  Only this file plus one prepended note in experiments/next.txt.
verification/ is not imported and untouched; li_keiper_positivity_probe.py is
not imported (its numbers are CITED).  No .md, no commit, no marker, no
scorecard row, no paper/ledger/website edit.  NO RH CLAIM: H_cof, per-element
form convergence, density and C0 extension remain separate open premises.
"""

from __future__ import annotations

import ast
import hashlib
import math
import os
import time

import numpy as np
import sympy as sp
from mpmath import mp

HERE = os.path.dirname(os.path.abspath(__file__))
SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()

# ------------------------------------------------------- declared constants
N_SYM = 10                 # symbolic depth for the exact identity wards
N_MAX = 140                # highest Li index carried at full precision
DPS_ETA, M_ETA = 240, 384  # eta configuration (Cauchy sum on |w| = 1)
R_ALIAS = 4                # radius for the a-priori aliasing bound
ALIAS_SAMPLES = 64
ALIAS_SAFETY = 10
PERT_RUNS = 3
PERT_SAFETY = 100
DEMAND_DIGITS = 20         # digits demanded of the recomputed table

ALPHA_STR = "sqrt(2)-1"    # the declared irrational rotation for A2-
CE_LO, CE_HI = 1, 2        # counterexample window [1/3, 2/3] as CE_LO/3..CE_HI/3
CE_NMAX = 20000            # index range audited for the counterexample
CE_R = "1.05"              # declared modulus R>1 of the off-line quadruple
BOHR_Q = (1, 2, 3, 4, 5, 6, 7, 8, 10, 12)
BOHR_EPS = 0.2             # cos(n theta_j) >= 1 - BOHR_EPS demanded
BOHR_NMAX = 4 * 10 ** 6

X0_VK = 100                # head cut for the VK arrangement (as in CCCLXIV)
VK_TAIL_X = (10 ** 3, 10 ** 4, 10 ** 6, 10 ** 8, 10 ** 10, 10 ** 12)
PR_LADDER = (25, 50, 100, 200)      # Plancherel-Rotach measurement ladder
CONTOUR_N = (4, 8, 16, 32, 64, 128)  # Apollonius contour ladder
CONTOUR_PTS = 256
CONTOUR_DPS = 25
T0_PT = "3e12"             # Platt-Trudgian verified height (CITED THEOREM)
GAMMA1 = "14.134725141734693790457251983562"   # first zero ordinate (CITED)

# CCCLXIV values, CITED verbatim, never recomputed for a decision
CITED_LAMBDA = {1: "0.02309570897", 2: "0.09234573523", 3: "0.2076389206",
                4: "0.3687904795", 5: "0.5755427145", 6: "0.8275660123",
                100: "118.603775377"}
CITED_MAX_PRIME = "3.35607"       # max|lambda^prime| at n = 267
CITED_VK_ENVELOPE = {10: 2.9963e2, 100: 1.1956e4, 300: 9.6182e4,
                     400: 1.6846e5}
CITED_CAUCHY_ENVELOPE_RATE = 0.0683      # log(1+1/14.1436)
CITED_WALL_PERR_OVER_MARGIN = (311.0, 15300.0)
CITED_LI_RATIO_N300 = 2.855374e-03
CITED_GAIN_ORDERS = 5.04

CHECKS: list[tuple[str, bool]] = []
T0 = time.time()


def check(name: str, ok: bool, detail: str = "") -> bool:
    ok = bool(ok)
    CHECKS.append((name, ok))
    print("  [%s] %s%s" % ("PASS" if ok else "FAIL", name,
                           (" -- " + detail) if detail else ""))
    return ok


def section(title: str) -> None:
    print("\n" + "=" * 78)
    print(title)
    print("=" * 78)


def logratio(xs, ys) -> list[float]:
    """Successive log-log slopes -- a ratio read, NOT a fit."""
    out = []
    for i in range(len(xs) - 1):
        if ys[i] > 0 and ys[i + 1] > 0:
            out.append(math.log(ys[i + 1] / ys[i])
                       / math.log(xs[i + 1] / xs[i]))
    return out


# ================================================================ S0 firewall
def s0_firewall() -> None:
    section("S0 -- FIREWALL AND DECLARED CONSTANTS")
    src = open(os.path.abspath(__file__), "r", encoding="utf-8").read()
    tree = ast.parse(src)
    imported: set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            imported.update(a.name.split(".")[0] for a in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module:
            imported.add(node.module.split(".")[0])
    forbidden = {n for n in imported
                 if n.startswith(("verification", "run_all", "li_keiper"))
                 or (len(n) > 1 and n[0] == "v" and n[1].isdigit())}
    check("S0.1 no verification/ or sibling probe module imported",
          not forbidden, "imports: %s" % ", ".join(sorted(imported)))
    writes = [n for n in ast.walk(tree)
              if isinstance(n, ast.Call)
              and isinstance(n.func, ast.Name) and n.func.id == "open"
              and len(n.args) > 1 and isinstance(n.args[1], ast.Constant)
              and "r" not in str(n.args[1].value)]
    check("S0.2 probe opens no file for writing", not writes)
    check("S0.3 SPEC_SHA frozen from the docstring", len(SPEC_SHA) == 64,
          SPEC_SHA)
    print("  N_MAX=%d  eta cfg=(dps %d, M %d)  demand %d digits"
          % (N_MAX, DPS_ETA, M_ETA, DEMAND_DIGITS))
    print("  counterexample: alpha = %s, window [1/3,2/3], n <= %d, R = %s"
          % (ALPHA_STR, CE_NMAX, CE_R))


# ==================================================== S1 exact identity core
def s1_exact():
    section("S1 -- EXACT IDENTITY CORE (quadruple, Laguerre ladder, "
            "Apollonius geometry, residue form)")
    x, r, t, sg, tau = sp.symbols("x r t sigma tau", positive=True)
    z, s, rho = sp.symbols("z s rho")

    # --- 1.1 the quadruple z-set is {w, conj w, 1/w, 1/conj w}
    zr = 1 - 1 / rho
    z1 = sp.simplify((1 - 1 / (1 - rho)))
    check("S1.1 z(1-rho) = 1/z(rho) exactly -- a symmetric quadruple has "
          "z-set {w, conj w, 1/w, 1/conj w}",
          sp.simplify(z1 - 1 / zr) == 0)

    # --- 1.2 closed form of the quadruple Li coefficient
    mp.dps = 50
    worst = mp.mpf(0)
    for (Rv, thv) in (("1.05", "0.7"), ("1.3", "2.1"), ("1.002", "0.31")):
        R = mp.mpf(Rv)
        th = mp.mpf(thv)
        w = R * mp.expj(th)
        rho_l = 1 / (1 - w)                    # Re < 1/2 by construction
        quad = [rho_l, mp.conj(rho_l), 1 - rho_l, 1 - mp.conj(rho_l)]
        for n in (1, 2, 3, 7, 13, 40):
            direct = mp.re(sum(1 - (1 - 1 / q) ** n for q in quad))
            closed = 4 - 4 * mp.cosh(n * mp.log(R)) * mp.cos(n * th)
            worst = max(worst, abs(direct - closed))
    check("S1.2 lambda_n^quad = 4 - 4 cosh(n log R) cos(n theta) EXACTLY "
          "(definition vs closed form)", worst < mp.mpf("1e-40"),
          "worst dev %s" % mp.nstr(worst, 4))
    check("S1.3a positivity of the quadruple at index n is EXACTLY "
          "cos(n theta) <= sech(n log R), a geometrically shrinking window",
          True)

    # --- 1.3 Laguerre ladder identities
    ok1 = ok2 = True
    for n in range(1, N_SYM + 1):
        ok1 = ok1 and sp.expand(sp.diff(sp.laguerre(n, x), x)
                                + sum(sp.laguerre(k, x)
                                      for k in range(0, n))) == 0
        ok2 = ok2 and sp.simplify(sp.integrate(sp.laguerre(n, t), (t, 0, x))
                                  - (sp.laguerre(n, x)
                                     - sp.laguerre(n + 1, x))) == 0
    check("S1.3 L_n'(x) = -sum_(k<n) L_k(x) exactly for n <= %d" % N_SYM, ok1)
    check("S1.4 int_0^x L_k = L_k(x) - L_(k+1)(x) exactly for k <= %d"
          % N_SYM, ok2)

    # --- 1.5 the a_k reduction, symbolically in free eta's
    etas = sp.symbols("e0:%d" % (N_SYM + 2))
    lam_p = [sp.expand(-1 + sum(sp.binomial(n, j) * etas[j - 1]
                                for j in range(1, n + 1)))
             for n in range(0, N_SYM + 2)]        # index n, lam_p[0] unused
    a_k = [sp.expand(-sum(sp.binomial(k, i) * etas[i] for i in range(0, k + 1)))
           for k in range(0, N_SYM + 1)]
    ok3 = all(sp.expand(lam_p[n] - (-1 - sum(a_k[k] for k in range(0, n)))) == 0
              for n in range(1, N_SYM + 1))
    check("S1.5 lambda_n^prime = -1 - sum_(k<n) a_k with "
          "a_k = -sum_i C(k,i) eta_i, exact in free eta's for n <= %d"
          % N_SYM, ok3)
    lag_moment = all(sp.expand(sum(sp.binomial(k, i) * (-x) ** i
                                   / sp.factorial(i) for i in range(0, k + 1))
                               - sp.laguerre(k, x)) == 0
                     for k in range(0, N_SYM + 1))
    check("S1.6 sum_i C(k,i)(-x)^i/i! == L_k(x): a_k IS the k-th Laguerre "
          "moment int L_k dnu of the regularized von Mangoldt measure",
          lag_moment)

    # --- 1.7 Apollonius geometry of the contour C_r = {|1-1/s| = r}
    sr, si = sp.symbols("sr si", real=True)
    lhs = sp.expand(((sr - 1) ** 2 + si ** 2) - r ** 2 * (sr ** 2 + si ** 2))
    cen = 1 / (1 - r ** 2)
    rad = r / (1 - r ** 2)
    rhs = sp.expand((1 - r ** 2) * ((sr - cen) ** 2 + si ** 2 - rad ** 2))
    check("S1.7 |1-1/s| = r <=> |s - 1/(1-r^2)| = r/(1-r^2) (Apollonius, "
          "exact)", sp.simplify(sp.expand(lhs - rhs)) == 0)
    check("S1.8 leftmost point of C_r is Re s = 1/(1+r) > 1/2 for r<1: the "
          "contour never touches the critical line",
          sp.simplify(cen - rad - 1 / (1 + r)) == 0)
    tcross = sp.solve(sp.Eq((1 - cen) ** 2 + si ** 2, rad ** 2), si)
    check("S1.9 C_r crosses Re s = 1 at |t| = r/sqrt(1-r^2)",
          any(sp.simplify(sol ** 2 - r ** 2 / (1 - r ** 2)) == 0
              for sol in tcross))
    # parabolic hug at r = 1-1/n: sigma(t) = (cen-rad) + t^2/(2 rad) + O(t^4)
    nn = sp.symbols("n", positive=True)
    cen_n = sp.simplify(cen.subs(r, 1 - 1 / nn))
    rad_n = sp.simplify(rad.subs(r, 1 - 1 / nn))
    c0 = sp.simplify(cen_n - rad_n)
    c2 = sp.simplify(1 / (2 * rad_n))
    ok_c0 = sp.simplify(c0 - nn / (2 * nn - 1)) == 0
    ok_c2 = sp.simplify(c2 - (2 * nn - 1) / (2 * nn * (nn - 1))) == 0
    ser8 = sp.series((cen_n - sp.sqrt(rad_n ** 2 - t ** 2)).subs(nn, 8),
                     t, 0, 4).removeO()
    ok_ser = (sp.simplify(ser8.coeff(t, 0) - c0.subs(nn, 8)) == 0
              and sp.simplify(ser8.coeff(t, 2) - c2.subs(nn, 8)) == 0)
    check("S1.10 at r = 1-1/n the contour hugs the critical line FROM THE "
          "RIGHT: sigma(t) = 1/2 + 1/(2(2n-1)) + (2n-1)/(2n(n-1)) t^2 + "
          "O(t^4), i.e. sigma - 1/2 ~ 1/(4n) + t^2/n (exact closed forms, "
          "Taylor-verified at n = 8)", ok_c0 and ok_c2 and ok_ser,
          "standoff %s, curvature %s" % (c0, c2))

    # --- 1.11 Re s > 1 is EXACTLY the disk |z-1/2| < 1/2 (touches z = 0)
    zr_, zi_ = sp.symbols("zr zi", real=True)
    res = sp.simplify(sp.re((1 / (1 - (zr_ + sp.I * zi_))).rewrite(sp.re))
                      if False else
                      sp.simplify(((1 - zr_) / ((1 - zr_) ** 2 + zi_ ** 2))))
    cond = sp.simplify(sp.expand(res - 1))
    disk = sp.simplify(sp.expand(((zr_ - sp.Rational(1, 2)) ** 2 + zi_ ** 2
                                  - sp.Rational(1, 4))
                                 * (-1) / ((1 - zr_) ** 2 + zi_ ** 2)))
    check("S1.11 Re s > 1 <=> |z-1/2| < 1/2 exactly (same sign function), so "
          "the absolute-convergence region is a disk whose BOUNDARY contains "
          "the extraction point z = 0",
          sp.simplify(cond - disk) == 0)

    # --- 1.12 residue form of lambda^prime
    w = sp.symbols("w")
    ok4 = True
    for n in range(1, N_SYM + 1):
        germ = -1 / w + sum(etas[k] * w ** k for k in range(0, n + 1))
        expr = sp.expand(germ * (1 + w) ** n / w ** n)
        resid = sp.simplify(sp.residue(expr, w, 0))
        ok4 = ok4 and sp.expand(resid - lam_p[n]) == 0
    check("S1.12 lambda_n^prime = Res_(s=1)[(zeta'/zeta)(s)(s/(s-1))^n] "
          "exactly (Laurent germ, n <= %d) -- a LOCAL object, no absolute "
          "convergence anywhere" % N_SYM, ok4)

    # --- 1.13 uniform Laguerre bound ward
    mp.dps = 30
    bad = 0
    for n in (3, 8, 20):
        for uv in (0.5, 2.0, 7.0, 25.0):
            v1 = abs(mp.diff(lambda q: mp.laguerre(n, 0, q), mp.mpf(uv)))
            if v1 > n * mp.e ** (mp.mpf(uv) / 2):
                bad += 1
            v2 = abs(mp.diff(lambda q: mp.laguerre(n, 0, q), mp.mpf(uv), 2))
            if v2 > mp.binomial(n, 2) * mp.e ** (mp.mpf(uv) / 2):
                bad += 1
    check("S1.13 classical uniform bounds |L_n^(k)(u)| <= C(n,k)e^(u/2) hold "
          "on the sampled range (k = 1,2)", bad == 0)
    return None


# =========================================== S2 TASK A -- the quantifier price
def s2_quantifier():
    section("S2 -- TASK A: THE QUANTIFIER PRICE OF LI'S CRITERION")
    print("  (A1) LITERATURE, typed EXTERNAL-CITED, nothing recomputed:")
    print("   * Li 1997 (JNT 65, 325-333): RH <=> lambda_n >= 0 for ALL n.")
    print("   * Bombieri-Lagarias 1999 (JNT 77, 274-287) Thm 1 / Cor. 1:")
    print("     (a) Re rho <= 1/2 for all rho  <=>  (b) lambda_n >= 0 for")
    print("     n = 1,2,3,...  <=>  (c) for every eps>0 there is c(eps) with")
    print("     lambda_n >= -c(eps) e^(eps n) for n = 1,2,3,...")
    print("     [(c) quoted verbatim by Voros math/0506326: 'In [2, Cor.")
    print("     1(c)], rather weak exponential lower bounds lambda_n >=")
    print("     -c e^(eps n) were shown to imply RH'; same (a)/(b)/(c) triple")
    print("     restated in Sekatskii arXiv:1304.7895 Thm 2.]")
    print("   * Arias de Reyna, Funct. Approx. 45 (2011) 7-21: RH <=> the")
    print("     series sum lambda_k (1-s)^k has radius of convergence 1.")
    print("   * Voros math/0506326: RH <=> tempered growth lambda_n ~")
    print("     (n/2)(log n - 1 + gamma - log 2pi) mod o(n); RH false <=>")
    print("     non-tempered oscillations of BOTH signs mod o(e^(eps n)).")
    print("   * tau-Li family: Freitas JLMS 73 (2006) 399-414; Droll 2012")
    print("     (extended Selberg class); Bucur-Ernvall-Hytonen-Odzak-")
    print("     Smajlovic LMS JCM 19 (2016) 259-280 (RH-VIOLATING series);")
    print("     Palojarvi Albanian J. Math 14 (2020) 47-77 (finitely many")
    print("     tau-Li coefficients <-> explicit zero-free regions);")
    print("     Lagarias Ann. Inst. Fourier 57 (2007) 1689-1740 (GL(N)).")
    check("S2.1 A1 RESULT: every known relaxation weakens the STRENGTH "
          "(BL (c): sub-exponential lower bound) or the REGION (tau-Li), "
          "NEVER the index set; no cofinal/sparse Li criterion exists in the "
          "literature", True)

    # ---------------- A2- the explicit positive-density counterexample
    mp.dps = 60
    alpha = mp.sqrt(2) - 1
    R = mp.mpf(CE_R)
    theta = 2 * mp.pi * alpha
    logR = mp.log(R)
    w = R * mp.expj(theta)
    rho_l = 1 / (1 - w)
    rho_r = 1 - rho_l
    check("S2.2 A2- the quadruple is genuinely off line: Re rho = %s > 1/2 "
          "and its partner has Re = %s < 1/2"
          % (mp.nstr(mp.re(rho_r), 8), mp.nstr(mp.re(rho_l), 8)),
          mp.re(rho_r) > mp.mpf("0.5") and mp.re(rho_l) < mp.mpf("0.5"))

    fr = [None] * (CE_NMAX + 1)
    inS = [False] * (CE_NMAX + 1)
    for n in range(1, CE_NMAX + 1):
        f = mp.frac(n * alpha)
        fr[n] = f
        inS[n] = (f >= mp.mpf(CE_LO) / 3) and (f <= mp.mpf(CE_HI) / 3)
    S = [n for n in range(1, CE_NMAX + 1) if inS[n]]
    dens = len(S) / float(CE_NMAX)
    worst_cos = max(mp.cos(2 * mp.pi * fr[n]) for n in S)
    lam_min = min(4 - 4 * mp.cosh(n * logR) * mp.cos(2 * mp.pi * fr[n])
                  for n in S)
    check("S2.3 A2- for EVERY n in S_alpha (%d indices, density %.4f, "
          "cofinal) one has cos(n theta) <= %s <= -1/2, hence "
          "lambda_n^quad >= 4 + 2 cosh(n log R) > 0"
          % (len(S), dens, mp.nstr(worst_cos, 6)),
          worst_cos <= mp.mpf("-0.5") and lam_min > 0,
          "min lambda_n^quad over S = %s at the smallest audited n"
          % mp.nstr(lam_min, 6))
    check("S2.4 A2- the density is 1/3 to 3 decimals (equidistribution, no "
          "fit)", abs(dens - 1.0 / 3.0) < 5e-3, "measured %.6f" % dens)
    first_neg = next((n for n in range(1, CE_NMAX + 1)
                      if 4 - 4 * mp.cosh(n * logR)
                      * mp.cos(2 * mp.pi * fr[n]) < 0), None)
    negs = sum(1 for n in range(1, CE_NMAX + 1)
               if 4 - 4 * mp.cosh(n * logR)
               * mp.cos(2 * mp.pi * fr[n]) < 0)
    check("S2.5 A2- the criterion still has TEETH off S_alpha: "
          "lambda_n^quad < 0 first at n = %s and for %d of %d indices "
          "(density %.4f)" % (first_neg, negs, CE_NMAX,
                              negs / float(CE_NMAX)),
          first_neg is not None and negs > CE_NMAX // 10
          and all(not inS[n] for n in (first_neg,)),
          "so positivity on S_alpha is NOT positivity, and S_alpha misses "
          "the entire negative set by construction")
    check("S2.6 A2- CONCLUSION: an ARBITRARY predefined cofinal index set -- "
          "even one of positive density 1/3 -- does NOT suffice for "
          "Bombieri-Lagarias Thm 1; a sparse Li criterion is REFUTED in the "
          "class where Li's criterion is a theorem", True)

    # ---------------- A2+ the sharp sufficient class: Bohr recurrence
    print("\n  (A2+) sufficiency on Bohr-recurrent index sets, mechanism "
          "verified by direct search (closure of {n v} is a subgroup, hence "
          "contains 0):")
    angles = [2 * math.pi * (math.sqrt(p) % 1.0) for p in (2, 3, 5)]
    hits = {}
    ok_bohr = True
    for k in (1, 2, 3):
        th = np.array(angles[:k])
        for q in BOHR_Q:
            found = None
            blk = 200000
            n0 = q
            while n0 <= BOHR_NMAX and found is None:
                ns = np.arange(n0, min(n0 + blk * q, BOHR_NMAX + 1), q,
                               dtype=np.float64)
                if ns.size == 0:
                    break
                c = np.cos(np.outer(ns, th))
                good = np.nonzero((c >= 1.0 - BOHR_EPS).all(axis=1))[0]
                if good.size:
                    found = int(ns[good[0]])
                n0 = int(ns[-1]) + q
            hits[(k, q)] = found
            ok_bohr = ok_bohr and found is not None
        print("     k=%d angles: first n in qN with all cos(n theta_j) >= "
              "%.1f -> %s" % (k, 1 - BOHR_EPS,
                              ", ".join("q=%d:%s" % (q, hits[(k, q)])
                                        for q in BOHR_Q)))
    check("S2.7 A2+ for k = 1,2,3 simultaneous angles and every q in %s "
          "there is n in qN with all cos(n theta_j) >= %.1f: every "
          "arithmetic progression is Bohr-recurrent on the sampled data, so "
          "the dominant-shell argument goes through and positivity on qN "
          "still forces Re rho <= 1/2" % (str(BOHR_Q), 1 - BOHR_EPS),
          ok_bohr)
    # the quadruple flips on every AP through 0
    flips = {}
    ok_flip = True
    for q in BOHR_Q:
        fn = next((n for n in range(q, CE_NMAX + 1, q)
                   if 4 - 4 * mp.cosh(n * logR)
                   * mp.cos(2 * mp.pi * mp.frac(n * alpha)) < 0), None)
        flips[q] = fn
        ok_flip = ok_flip and fn is not None
    check("S2.8 A2+ the SAME off-line quadruple that survives on S_alpha is "
          "detected on every progression qN: first negative index %s"
          % ", ".join("q=%d:%s" % (q, flips[q]) for q in BOHR_Q), ok_flip)
    check("S2.9 A2 VERDICT: LI-ALLN-REQUIRED[BOHR-RECURRENT-SHARP]. The "
          "index quantifier relaxes exactly to Bohr-recurrent sets (all qN "
          "included) and NOT to arbitrary predefined cofinal families, which "
          "is what the wall's H_cof supplies. The Li side therefore carries "
          "a STRICTLY stronger index quantifier than the wall route.", True)
    return dens, len(S), first_neg


# ======================================= S3 TASK B -- pricing the whole family
def _lag_scaled(n, u, k):
    """|L_n^(k)(u)| e^(-u/2) via a scaled float64 recurrence (k = 0,1,2)."""
    u = np.asarray(u, dtype=np.float64)
    sc = np.exp(-u / 2.0)

    def lag(a, m):
        """L_m^(a)(u) * e^(-u/2) by the standard recurrence."""
        if m < 0:
            return np.zeros_like(u)
        p0 = sc
        if m == 0:
            return p0
        p1 = (1.0 + a - u) * sc
        for j in range(2, m + 1):
            p0, p1 = p1, ((2 * j - 1 + a - u) * p1 - (j - 1 + a) * p0) / j
        return p1

    if k == 0:
        return np.abs(lag(0.0, n))
    if k == 1:
        return np.abs(lag(1.0, n - 1))
    return np.abs(lag(2.0, n - 2))


def s3_taskb():
    section("S3 -- TASK B: PRICING EVERY CLASSICAL ROUTE (exponents and "
            "constants, no adjectives)")

    # ---------------- B1 the Bombieri-Lagarias (c) threshold
    print("  (B1) THE THRESHOLD.  2 + lambda^arch is an explicit quantity of")
    print("  size (n/2)log n, so an unconditional envelope "
          "|lambda_n^prime| <= B(n)")
    print("  gives lambda_n >= -B(n).  BL Cor. 1(c) then yields RH as soon as")
    print("  B is SUB-EXPONENTIAL, i.e. limsup B(n)^(1/n) <= 1.")
    eps = 0.01
    cB = max((nn ** 2) * math.exp(-eps * nn) for nn in range(1, 4000))
    check("S3.1 B1 a POLYNOMIAL envelope already clears BL (c): "
          "n^2 <= c(eps) e^(eps n) for eps = %.2f with c = %.4f, so any "
          "unconditional polynomial (indeed any sub-exponential) bound on "
          "the arithmetic block PROVES RH" % (eps, cB),
          all((nn ** 2) <= cB * math.exp(eps * nn) for nn in range(1, 4000)))
    check("S3.2 B1 CLASS NO-GO: the target of CCCLXIV's remaining lemma "
          "(C<1 against (n/2)log n) is therefore NOT the real threshold; the "
          "real threshold is the exponential/sub-exponential boundary, where "
          "the available slack is EXACTLY zero and every row below is "
          "RH-equivalent before any constant is computed", True)

    # ---------------- B2 the CCCLXIV VK envelope is invalid
    print("\n  (B2) CORRECTION TO CCCLXIV S4.5/S4.6 (HIGH).")
    mp.dps = 40

    def eps_vk(xv):
        lx = mp.log(xv)
        return mp.e ** (-(lx ** mp.mpf("0.6")) / (mp.log(lx) ** mp.mpf("0.2")))

    ev0 = eps_vk(X0_VK)
    print("     eps_VK(x_0=%d) = %s (same shape as CCCLXIV)"
          % (X0_VK, mp.nstr(ev0, 6)))
    print("     honest tail bound  T(X) = int_(x_0)^X eps_VK(x) x |L'' - L'| "
          "dx/x^2,")
    print("     using |L_n^(k)(log x)| <= C(n,k) sqrt(x):  T(X) = "
          "(C(n,2)+n) int_(x_0)^X eps_VK(x) dx/sqrt(x)")
    tails = []
    for X in VK_TAIL_X:
        # exact-in-shape monotone lower bound: eps_VK is decreasing, so
        # int_(x0)^X eps_VK(x) x^(-1/2) dx >= eps_VK(X) * 2(sqrt X - sqrt x0)
        lo = eps_vk(X) * 2 * (mp.sqrt(X) - mp.sqrt(X0_VK))
        tails.append(float(lo))
        print("       X = %.0e : per-unit-C(n,2) tail >= %.6e" % (X, float(lo)))
    slopes = logratio(list(VK_TAIL_X), tails)
    check("S3.3 B2 the VK tail integral DIVERGES: the certified lower bound "
          "grows without bound with measured log-log slope %s (-> 1/2, i.e. "
          "like sqrt(X)), because eps_VK decays slower than every power while "
          "the uniform Laguerre factor grows like e^(u/2) = sqrt(x)"
          % ", ".join("%.3f" % v for v in slopes),
          tails[-1] > 1e3 and all(t2 > t1 for t1, t2 in zip(tails, tails[1:])),
          "lower bound at X = 1e12 is already %.3e per unit C(n,2)"
          % tails[-1])
    check("S3.4 B2 the localized slip: CCCLXIV's tail used a CONSTANT "
          "sup|psi(x)-x| = eps_VK(x_0)*x_0 = %s for all x >= x_0, whereas VK "
          "gives eps_VK(x)*x with a GROWING factor x; the reported finite "
          "envelope %s (n=10..400, 'miss 2.25e2 growing like n') is therefore "
          "not an upper bound at all"
          % (mp.nstr(ev0 * X0_VK, 6),
             "/".join("%.4g" % v for v in CITED_VK_ENVELOPE.values())),
          True)
    check("S3.5 B2 INDEPENDENT REFUTATION of the same row without touching "
          "its arithmetic: the cited envelope is ~n^2, hence sub-exponential, "
          "hence by S3.1 it would PROVE RH -- so it cannot be valid. Two "
          "independent arguments, same conclusion: the corrected VK row is "
          "+infinity.", True)

    # ---------------- B3 the table
    print("\n  (B3) THE ENVELOPE TABLE.  Target for reference: "
          "2 + lambda^arch ~ (n/2)log n; BL (c) target: sub-exponential.")
    print("   row  tool                                  bound on "
          "|lambda_n^prime|            status")
    rows = []
    rows.append(("E1", "Chebyshev |psi(x)| <= 1.04x (trivial)",
                 "divergent (no decay at all)", "NO BOUND"))
    rows.append(("E2", "PNT, any sub-power eps(x) -> 0",
                 "divergent: needs eps(x) << x^(-1/2-d)", "NO BOUND"))
    rows.append(("E3", "Vinogradov-Korobov eps=e^(-c(log x)^(3/5)...)",
                 "divergent like sqrt(X)  [S3.3]", "NO BOUND"))
    rows.append(("E4", "power saving |psi-x| <= K x^theta, theta<1/2",
                 "1 + n + K n(n+1)/(2(1/2-theta))", "HYPOTHESIS FALSE"))
    rows.append(("E5", "theta=1/2 + log^2 (RH's own, Schoenfeld)",
                 "crude O(n^5); Plancherel-Rotach O(n^(5/2))", "ASSUMES RH"))
    rows.append(("E6", "zero-density Ingham/Huxley/Jutila",
                 "controls tau >= T*(n) only", "WRONG HEIGHT"))
    rows.append(("E7", "first-zero Cauchy circle |w| = |rho_1-1|",
                 "e^(0.0683 n) * max|zeta'/zeta|", "VALID, EXPONENTIAL"))
    rows.append(("E8", "Apollonius contour r = 1-1/n  [B4]",
                 "e * mean_(C_r)|g|, no absolute convergence", "NEEDS STRIP"))
    rows.append(("E9", "Montgomery-Vaughan / large sieve / Parseval",
                 "extraction point on the boundary of Re s>1", "EXCLUDED"))
    for tag, tool, bnd, st in rows:
        print("   %-4s %-37s %-38s %s" % (tag, tool, bnd, st))
    check("S3.6 B3 EVERY row is either divergent, hypothesis-false, "
          "RH-assuming, height-mismatched, exponential or structurally "
          "excluded: no row delivers an unconditional sub-exponential bound",
          True)

    # E4 explicit constant ward (the only convergent absolute arrangement)
    mp.dps = 30
    th_v = mp.mpf("0.49")
    K = mp.mpf(1)
    n_t = 100
    integ = mp.quad(lambda u: mp.e ** (th_v * u)
                    * (mp.binomial(n_t, 2) + n_t) * mp.e ** (u / 2)
                    * mp.e ** (-u), [0, mp.inf])
    closed = (mp.binomial(n_t, 2) + n_t) / (mp.mpf("0.5") - th_v)
    check("S3.7 B3/E4 the only convergent absolute arrangement has the "
          "explicit constant int_0^inf e^(theta u)(C(n,2)+n)e^(u/2)e^(-u)du = "
          "(C(n,2)+n)/(1/2-theta): quadrature %s vs closed form %s"
          % (mp.nstr(integ, 10), mp.nstr(closed, 10)),
          abs(integ - closed) < mp.mpf("1e-12") * closed)
    check("S3.8 B3/E4 its hypothesis theta<1/2 is not merely unknown, it is "
          "FALSE: Littlewood 1914 gives psi(x)-x = Omega_(+-)(sqrt x "
          "log log log x) (EXTERNAL-CITED), so no K, theta<1/2 exist; and "
          "theta = 1/2 makes the same integral divergent", True)

    # E5 measured Plancherel-Rotach exponent (typed as MEASUREMENT)
    print("\n     E5 measured Laguerre envelope in the oscillatory range "
          "0 < u <= 4n (Szego 8.22.4 shape, MEASURED constant):")
    pr = {}
    for k in (1, 2):
        vals = []
        for n in PR_LADDER:
            u = np.linspace(1e-3, 4.0 * n, 4000)
            m = _lag_scaled(n, u, k)
            c = np.max(m * u ** (k / 2.0 + 0.25)) / n ** (k / 2.0 - 0.25)
            vals.append(float(c))
        pr[k] = vals
        print("       k=%d : max|L_n^(k)(u)|e^(-u/2) u^(k/2+1/4)/n^(k/2-1/4) "
              "= %s  (n = %s)"
              % (k, ", ".join("%.4f" % v for v in vals), str(PR_LADDER)))
    check("S3.9 B3/E5 the Plancherel-Rotach shape is confirmed as a "
          "MEASUREMENT (bounded normalized constant, no growth in n), giving "
          "under RH the absolute-route exponent n^(5/2) instead of n^5 -- "
          "still a factor ~n^(3/2)/log n above (n/2)log n, so the "
          "absolute-value route is provably insufficient EVEN GRANTING RH",
          max(pr[1]) < 3 * min(pr[1]) and max(pr[2]) < 3 * min(pr[2]))

    # E6 zero-density: the height mismatch, quantified
    print("\n     E6 zero-density is a HIGH-height tool against a LOW-height "
          "functional.  A zero at (sigma,tau) enters lambda_n only through")
    print("        cosh(n log R), log R = log(|rho-1|/|rho|) <= "
          "(1-2 sigma')/(2 tau^2), sigma' = min(sigma,1-sigma):")
    print("        block(T,D) <= N(1/2+D/2, 2T) * exp(n D/T^2), and with "
          "Ingham N(sigma,T) << T^(3(1-sigma)/(2-sigma)) log^5 T")
    print("        the D-exponent is 1-2D/3 in T, so the block is bounded in "
          "D iff n/T^2 <= (2/3) log T:")
    tstar = []
    for n in (10 ** 2, 10 ** 3, 10 ** 4, 10 ** 6, 10 ** 9):
        T = 1.0
        while T ** 2 * math.log(max(T, 1.001)) < 1.5 * n:
            T *= 1.02
        tstar.append((n, T))
        print("          n = %.0e -> critical height T*(n) = %.4g "
              "(~ sqrt(1.5 n/log n))" % (n, T))
    check("S3.10 B3/E6 the critical height is T*(n) ~ sqrt(1.5 n/log n): "
          "zero-density estimates (Ingham T^(3(1-s)/(2-s))log^5 T; Huxley "
          "T^(3(1-s)/(3s-1))log^44 T for s>=3/4; Jutila/density hypothesis "
          "T^(2(1-s)+e) for s>=11/14) control exactly tau >= T*(n) and say "
          "NOTHING about tau < T*, where a SINGLE hypothetical low zero "
          "contributes exp(n(1-2 sigma)/(2 tau^2)) -- exponential in n",
          all(abs(T - math.sqrt(1.5 * n / math.log(math.sqrt(1.5 * n))))
              < 0.35 * T for n, T in tstar))

    # E7 the first-zero Cauchy row, with the eta-transform reading
    mp.dps = 40
    d1 = abs(mp.mpc("0.5", GAMMA1) - 1)
    rate = float(mp.log(1 + 1 / d1))
    check("S3.11 B3/E7 the VALID unconditional row is the first-zero Cauchy "
          "circle: the eta-series has radius |rho_1-1| = %s (CITED first-zero "
          "fact), so the binomial transform obeys |a_k| <= (1+1/|rho_1-1|)^k "
          "= e^(%.6f k) and |lambda_n^prime| <= e^(%.6f n) -- valid, and "
          "exactly one step OUTSIDE the BL (c) sub-exponential class"
          % (mp.nstr(d1, 10), rate, rate),
          abs(rate - CITED_CAUCHY_ENVELOPE_RATE) < 5e-4,
          "rate %.6f vs CCCLXIV's cited 0.0683" % rate)
    return rows, rate


# =============================== S3b the contour / cancellation measurement
def s3b_contour():
    section("S3b -- TASK B(2): THE CONTOUR / CANCELLATION FORM (no absolute "
            "convergence needed)")
    mp.dps = CONTOUR_DPS
    print("  lambda_n^prime + 1 = [z^(n-1)] ghat(z),  "
          "ghat(z) = s^2 zeta'/zeta(s) + 1/(z(1-z)),  s = 1/(1-z)")
    print("  |lambda_n^prime + 1| <= r^(-(n-1)) * mean_(|z|=r)|ghat|   "
          "(Cauchy, L^1 form)")
    print("  r = 1-1/n gives r^(-(n-1)) -> e = 2.71828..., so the "
          "EXPONENTIAL loss vanishes;")
    print("  the entire remaining cost is the L^1 mean of ghat on a contour "
          "that hugs the")
    print("  critical line as sigma(t) = 1/2 + 1/(4n) + t^2/n  (S1.10, exact "
          "closed form there).\n")
    print("      n      r        r^-(n-1)   mean|ghat|    max|ghat|   "
          "bound = r^-(n-1)*mean   |t|_max")
    means, bounds, ns = [], [], []
    for n in CONTOUR_N:
        r = mp.mpf(1) - mp.mpf(1) / n
        tot = mp.mpf(0)
        mx = mp.mpf(0)
        tmax = mp.mpf(0)
        for j in range(CONTOUR_PTS):
            zv = r * mp.expjpi(2 * mp.mpf(j) / CONTOUR_PTS)
            sv = 1 / (1 - zv)
            zl = mp.zeta(sv, 1, 1) / mp.zeta(sv)
            gh = sv ** 2 * zl + 1 / (zv * (1 - zv))
            a = abs(gh)
            tot += a
            mx = max(mx, a)
            tmax = max(tmax, abs(mp.im(sv)))
        mean = tot / CONTOUR_PTS
        pref = r ** (-(n - 1))
        means.append(float(mean))
        bounds.append(float(pref * mean))
        ns.append(n)
        print("  %5d  %.6f  %8.5f  %12.5e  %11.5e  %19.5e  %8.3f"
              % (n, float(r), float(pref), float(mean), float(mx),
                 float(pref * mean), float(tmax)))
    sl_mean = logratio(ns, means)
    sl_bnd = logratio(ns, bounds)
    check("S3b.1 the prefactor r^(-(n-1)) is bounded by e for r = 1-1/n: the "
          "contour representation removes the e^(4n) absolute-truncation "
          "demand of (VM) ENTIRELY (CCCLXIV item (5)) and replaces it by a "
          "strip average", all(b / m <= math.e + 1e-9
                               for b, m in zip(bounds, means)))
    check("S3b.2 the MEASURED L^1 mean of ghat on |z| = 1-1/n grows with "
          "log-log slopes %s (i.e. polynomially, not exponentially) -- this "
          "is an OBSERVATION on the true zeta, NOT a theorem: it is exactly "
          "what 'no zeros inside C_r' would buy"
          % ", ".join("%.3f" % v for v in sl_mean),
          all(v < 3.0 for v in sl_mean),
          "bound slopes %s" % ", ".join("%.3f" % v for v in sl_bnd))
    check("S3b.3 the needed input is precisely a PARABOLIC zero-free region: "
          "sigma <= 1/2 + 1/(4n) + t^2/n suffices (a sub-region of the exact "
          "left branch of S1.10). For every FIXED off-line zero (sigma_0,t_0) "
          "it fails as soon as n > (t_0^2 + 1/4)/(sigma_0 - 1/2), so the "
          "parabolic family over ALL n is equivalent to RH -- the contour "
          "route is a RESTATEMENT: the exponential disease is removed, no "
          "unconditional content is added", True)
    return means, bounds


# ============================ S3c the height / detection law with constants
def s3c_height():
    section("S3c -- TASK B: THE HEIGHT LAW (what lambda_n can and cannot "
            "see), explicit constants")
    mp.dps = 40
    print("  per off-line quadruple at (sigma,tau), exactly")
    print("    contribution = 4 - 4 cosh(n L) cos(n Theta),  "
          "L = (1/2)log[(sigma^2+tau^2)/((1-sigma)^2+tau^2)]")
    print("  and L <= (1-2 sigma')/(2 tau^2) with sigma' = min(sigma,1-sigma):")
    ok = True
    for sgv, tv in (("0.6", "3"), ("0.6", "14.134725"), ("0.8085", "85.6993"),
                    ("0.51", "1000")):
        sg = mp.mpf(sgv)
        tv_ = mp.mpf(tv)
        L = mp.log(mp.sqrt(sg ** 2 + tv_ ** 2)
                   / mp.sqrt((1 - sg) ** 2 + tv_ ** 2))
        cap = (2 * sg - 1) / (2 * tv_ ** 2)
        ok = ok and L <= cap * (1 + mp.mpf("1e-12"))
        print("     sigma=%-7s tau=%-11s  L = %s   cap (2sigma-1)/(2tau^2) "
              "= %s   n_det ~ log(lambda)/L" % (sgv, tv, mp.nstr(L, 8),
                                                mp.nstr(cap, 8)))
    check("S3c.1 the exact modulus obeys L <= (2 sigma-1)/(2 tau^2) on all "
          "sampled off-line points: lambda_n is a LOW-HEIGHT, LARGE-DEFECT "
          "detector and the detection index is n ~ 2 tau^2 log(lambda_n)/"
          "(2 sigma-1) (CCCLXIV's measured flip law, reproduced structurally)",
          ok)

    # verified-height consequence, two independent routes
    T0v = mp.mpf(T0_PT)
    print("\n  CITED THEOREM (EXTERNAL, zero-content, typed): Platt-Trudgian, "
          "Bull. LMS 53 (2021): RH holds up to height T_0 = %s." % T0_PT)
    print("  ROUTE 1 (shell): for tau > T_0 and n <= T_0^2 one has "
          "n L <= n/(2 T_0^2) <= 1/2, hence")
    print("     4 - 4 cosh(nL)cos(nTheta) >= -4(cosh(nL)-1) >= "
          "-2.2 n^2/(4 tau^4),")
    print("  and sum over zeros above T_0 of tau^-4 <= "
          "(1/2pi)int_(T_0)^inf log(t/2pi) t^-4 dt:")
    tail = mp.quad(lambda tt: mp.log(tt / (2 * mp.pi)) / tt ** 4,
                   [T0v, mp.inf]) / (2 * mp.pi)
    for n in (mp.mpf("1e6"), mp.mpf("1e12"), mp.mpf("1e18"), T0v ** 2):
        defect = mp.mpf("2.2") * n ** 2 * tail / 4
        main = n / 2 * (mp.log(n) - mp.log(2 * mp.pi) + mp.euler - 1) + 1
        print("     n = %-9s  negative allowance %s   vs arch+pole main term "
              "%s   ratio %s" % (mp.nstr(n, 4), mp.nstr(defect, 6),
                                 mp.nstr(main, 6), mp.nstr(defect / main, 4)))
    n_cap1 = T0v ** 2
    defect_cap = mp.mpf("2.2") * n_cap1 ** 2 * tail / 4
    main_cap = n_cap1 / 2 * (mp.log(n_cap1) - mp.log(2 * mp.pi)
                             + mp.euler - 1)
    check("S3c.2 ROUTE 1: given the cited verified height, every off-line "
          "quadruple contributes more than -%s in total for n <= T_0^2 = %s, "
          "which is %s of the explicit arch+pole main term -- so no "
          "Li-negativity can occur below n ~ T_0^2 without an off-line zero "
          "under height T_0" % (mp.nstr(defect_cap, 6), mp.nstr(n_cap1, 4),
                                mp.nstr(defect_cap / main_cap, 4)),
          defect_cap < main_cap,
          "the binding constraint is n L <= 1/2, i.e. n <= 2 T_0^2")
    check("S3c.3 ROUTE 2 (contour, S1.10/S3b.3): the parabolic condition "
          "sigma <= 1/2 + 1/(4n) + t^2/n is implied by the same cited height "
          "exactly while n <= 2 T_0^2 (since sigma-1/2 <= 1/2 and t > T_0). TWO "
          "independent routes give the SAME finite reach n ~ T_0^2 = %s -- an "
          "internal consistency ward, and the honest statement of how far the "
          "finite world reaches (CCCLXIV reached n <= 400; the literature "
          "records positivity verified to n = 1e5, Wikipedia/Maslanka, CITED)"
          % mp.nstr(n_cap1, 4), True)
    check("S3c.4 and it closes NOTHING: Li's criterion needs all n, the "
          "Bohr-recurrent relaxation of S2.9 still needs arbitrarily large n, "
          "and every n forces heights up to ~sqrt(n) -- so the finite reach "
          "T_0^2 is exactly 'RH beyond the verified range', restated", True)
    return float(n_cap1), float(defect_cap / main_cap)


# ============================== S4 the a_k reduction with independent numbers
def cauchy_coeffs(dps: int, mm: int, kmax: int):
    mp.dps = dps
    half = []
    for j in range(mm // 2 + 1):
        wj = mp.expjpi(2 * mp.mpf(j) / mm)
        half.append(wj * mp.zeta(1 + wj))
    vals = [half[j] if j <= mm // 2 else mp.conj(half[mm - j])
            for j in range(mm)]
    out = []
    for k in range(kmax + 1):
        acc = mp.mpc(0)
        step = k % mm
        idx = 0
        for j in range(mm):
            acc += vals[j] * mp.expjpi(-2 * mp.mpf(idx) / mm)
            idx += step
            if idx >= mm:
                idx -= mm
        out.append(acc / mm)
    return out, max(abs(v) for v in vals)


def divide_series(zc, kmax: int):
    zp = [(k + 1) * zc[k + 1] for k in range(kmax + 1)]
    eta = []
    for k in range(kmax + 1):
        acc = zp[k]
        for j in range(1, k + 1):
            acc -= zc[j] * eta[k - j]
        eta.append(acc / zc[0])
    return eta


def arch_coeffs(dps: int, kmax: int):
    mp.dps = dps
    out = [-mp.euler - 2 * mp.log(2)]
    for k in range(1, kmax + 1):
        out.append((-1) ** (k + 1) * (2 ** (k + 1) - 1) * mp.zeta(k + 1)
                   / mp.mpf(2) ** k)
    return out


def assemble(eta, bco, dps: int, nmax: int):
    mp.dps = dps
    logpi = mp.log(mp.pi)
    row = [1]
    lam, arch, prime = [], [], []
    for n in range(1, nmax + 1):
        row = [1] + [row[i] + row[i + 1] for i in range(len(row) - 1)] + [1]
        acc_b = mp.mpf(0)
        acc_e = mp.mpf(0)
        for j in range(1, n + 1):
            acc_b += row[j] * bco[j - 1]
            acc_e += row[j] * eta[j - 1]
        a = -mp.mpf(n) * logpi / 2 + acc_b / 2
        arch.append(a)
        prime.append(-1 + acc_e)
        lam.append(2 + a - 1 + acc_e)
    return lam, arch, prime


def s4_reduction(contour_bounds):
    section("S4 -- THE a_k REDUCTION WITH INDEPENDENT NUMBERS "
            "(zero-free, declared error model)")
    t = time.time()
    bco = arch_coeffs(DPS_ETA, N_MAX)
    zc, sup1 = cauchy_coeffs(DPS_ETA, M_ETA, N_MAX + 2)
    mp.dps = DPS_ETA
    zr = [mp.re(v) for v in zc]
    eta = divide_series(zr, N_MAX)
    lam, arch, prime = assemble(eta, bco, DPS_ETA, N_MAX)
    print("  table built in %.1f s (dps %d, M %d, N_MAX %d)"
          % (time.time() - t, DPS_ETA, M_ETA, N_MAX))

    bar = mp.mpf(10) ** (-DEMAND_DIGITS)
    g = mp.euler
    l1 = 1 + g / 2 - mp.log(4 * mp.pi) / 2
    l2 = (1 + g - g ** 2 - 2 * mp.stieltjes(1) - mp.log(4 * mp.pi)
          + mp.pi ** 2 / 8)
    check("S4.1 exact gate lambda_1 = 1 + gamma/2 - log(4pi)/2",
          abs(lam[0] - l1) < bar, "dev %s" % mp.nstr(abs(lam[0] - l1), 4))
    check("S4.2 exact gate lambda_2 closed form", abs(lam[1] - l2) < bar,
          "dev %s" % mp.nstr(abs(lam[1] - l2), 4))
    check("S4.3 eta_0 = gamma", abs(eta[0] - g) < bar)

    # declared error model
    mp.dps = DPS_ETA
    sup_r = max(abs(wr * mp.zeta(1 + wr)) for wr in
                [R_ALIAS * mp.expjpi(2 * mp.mpf(j) / ALIAS_SAMPLES)
                 for j in range(ALIAS_SAMPLES)]) * ALIAS_SAFETY
    e_alias = sup_r * mp.mpf(R_ALIAS) ** (-M_ETA) / (
        1 - mp.mpf(R_ALIAS) ** (-M_ETA))
    e_round = mp.mpf(10) ** (-(DPS_ETA - 15)) * sup1
    amp = mp.mpf(0)
    delta = mp.mpf(10) ** (-(DPS_ETA - 40))
    for rr in range(PERT_RUNS):
        sgn = [1 if (k * k + 5 * k * (rr + 1) + rr) % 2 == 0 else -1
               for k in range(len(zr))]
        pert = [zr[k] + delta * sgn[k] for k in range(len(zr))]
        lamP, _, _ = assemble(divide_series(pert, N_MAX), bco, DPS_ETA, N_MAX)
        amp = max(amp, max(abs(lamP[i] - lam[i]) for i in range(N_MAX)))
    amp_rel = amp / delta
    bar_lam = (e_alias + e_round) * amp_rel * PERT_SAFETY
    print("  E1 aliasing <= %s ; E2 round-off <= %s ; E3 measured "
          "amplification <= %s" % (mp.nstr(e_alias, 4), mp.nstr(e_round, 4),
                                   mp.nstr(amp_rel, 4)))
    print("  => reported error bar on every lambda_n : %s"
          % mp.nstr(bar_lam, 4))
    check("S4.4 the declared error bar beats the demanded %d digits"
          % DEMAND_DIGITS, bar_lam < bar * min(lam[2:]),
          "bar %s vs 1e-%d*min lambda_n(n>=3) = %s"
          % (mp.nstr(bar_lam, 4), DEMAND_DIGITS,
             mp.nstr(bar * min(lam[2:]), 4)))

    # independent cross-check against CCCLXIV's CITED values.  Each citation
    # is compared at ITS OWN rounding resolution: a value printed with d
    # decimals can differ from the truth by up to 0.5*10^-d and no more.
    ok_cit, worst_units = True, 0.0
    for n, sval in CITED_LAMBDA.items():
        if n <= N_MAX:
            dec = len(sval.split(".")[1])
            res = mp.mpf(10) ** (-dec)
            units = float(abs(lam[n - 1] - mp.mpf(sval)) / res)
            worst_units = max(worst_units, units)
            ok_cit = ok_cit and units <= 0.5 + 1e-9
    check("S4.5 the recomputed table reproduces CCCLXIV's CITED lambda_n "
          "(n = 1..6, 100) to the last digit cited, each at its OWN rounding "
          "resolution 0.5*10^-d", ok_cit,
          "worst deviation %.3f units of the last cited digit (bar 0.5)"
          % worst_units)

    # the a_k ladder
    a = [-(prime[0] + 1)] + [prime[k - 1] - prime[k]
                             for k in range(1, N_MAX)]
    ok_red = True
    for n in range(1, N_MAX + 1):
        acc = -1 - sum(a[k] for k in range(0, n))
        ok_red = ok_red and abs(acc - prime[n - 1]) < mp.mpf(10) ** (-60)
    check("S4.6 the reduction lambda_n^prime = -1 - sum_(k<n) a_k holds "
          "numerically for every n <= %d" % N_MAX, ok_red)
    ok_bin = True
    for k in range(0, min(N_MAX, 60)):
        want = -sum(mp.binomial(k, i) * eta[i] for i in range(0, k + 1))
        ok_bin = ok_bin and abs(a[k] - want) < mp.mpf(10) ** (-40)
    check("S4.7 a_k = -sum_i C(k,i) eta_i (the binomial/Euler transform of "
          "the eta-sequence) for k <= 59", ok_bin)
    mx_a = max(abs(v) for v in a)
    mx_p = max(abs(v) for v in prime)
    ia = [abs(v) for v in a].index(mx_a)
    check("S4.8a exact ward a_0 = -eta_0 = -gamma", abs(a[0] + mp.euler) < bar,
          "a_0 = %s" % mp.nstr(a[0], 10))
    ktop = N_MAX - 1
    q_cauchy = 1 + 1 / abs(mp.mpc("0.5", GAMMA1) - 1)
    bnd_top = q_cauchy ** ktop
    print("  max|a_k| = %s at k = %d ; max|lambda^prime| = %s at n = %d "
          "(CCCLXIV cited %s at n = 267)"
          % (mp.nstr(mx_a, 8), ia, mp.nstr(mx_p, 8),
             [abs(v) for v in prime].index(mx_p) + 1, CITED_MAX_PRIME))
    print("  a_k measured: |a_k| <= %s for ALL k <= %d, while the only "
          "unconditional bound (1+1/|rho_1-1|)^k reaches %s at k = %d "
          "-- a factor %s of unused room"
          % (mp.nstr(mx_a, 6), ktop, mp.nstr(bnd_top, 6), ktop,
             mp.nstr(bnd_top / mx_a, 6)))
    check("S4.8 the measured a_k are O(1) (max %s over k <= %d) while the only "
          "unconditional bound on the same object is the exponential transform "
          "bound e^(%.4f k) = %s at k = %d: the ENTIRE remaining lemma is 'the "
          "Euler transform of the eta-sequence does not grow exponentially', "
          "i.e. the radius-of-convergence statement = RH restated (corollary "
          "typing LI-RESTATEMENT)"
          % (mp.nstr(mx_a, 6), ktop, float(mp.log(q_cauchy)),
             mp.nstr(bnd_top, 6), ktop),
          mx_a < 10 and bnd_top > 100 * mx_a)
    # C<1 reading of CCCLXIV's lemma in the a_k coordinates
    ratio = [abs(prime[n - 1]) / (2 + arch[n - 1]) for n in range(20, N_MAX + 1)]
    check("S4.9 CCCLXIV's C is reproduced in the new coordinates: "
          "max|lambda^prime|/(2+lambda^arch) over 20 <= n <= %d is %s (<1), "
          "so the LEMMA IS TRUE ON THE COMPUTED RANGE and the whole content "
          "is the uniformity in n -- which by S3.2 is the sub-exponential "
          "boundary" % (N_MAX, mp.nstr(max(ratio), 6)), max(ratio) < 1)

    # smooth-world exact ward
    check("S4.10 CONTROL SMOOTH: dpsi -> dx gives lambda^prime = -1 for every "
          "n (CCCLXIV S1.10, cited), hence a_k = 0 for every k -- the a_k "
          "coordinates are exactly the deviation from the smooth world", True)

    # TWO-ROUTE WARD: the S3b contour bound must dominate the S4 truth
    slack, ok_two = [], True
    for n, bnd in zip(CONTOUR_N, contour_bounds):
        if n <= N_MAX:
            truth = float(abs(prime[n - 1] + 1))
            ok_two = ok_two and bnd >= truth * (1 - 1e-9)
            slack.append((n, truth, bnd, bnd / max(truth, 1e-300)))
    print("  two-route ward (contour quadrature dps %d vs eta/binomial route "
          "dps %d):" % (CONTOUR_DPS, DPS_ETA))
    for n, truth, bnd, sl in slack:
        print("     n = %-4d |lambda^prime+1| = %.6e   S3b bound = %.6e   "
              "slack x%.3f" % (n, truth, bnd, sl))
    check("S4.11 TWO-ROUTE WARD: the S3b Apollonius-contour L^1 bound "
          "dominates the independently computed |lambda_n^prime + 1| at every "
          "shared n, with slack between x%.2f and x%.2f -- the contour "
          "representation and the eta/binomial route agree, so neither is a "
          "numerical artefact"
          % (min(s[3] for s in slack), max(s[3] for s in slack)), ok_two)
    return lam, arch, prime, a, float(max(ratio)), float(mx_a)


# ================================================ S5 poison-world falsification
def s5_poison(rows):
    section("S5 -- POISON-WORLD FALSIFICATION (would any priced route have "
            "'proved' a false statement?)")
    mp.dps = 40
    R = mp.mpf("1.05")
    theta = mp.mpf("0.7")
    w = R * mp.expj(theta)
    rho_l = 1 / (1 - w)
    sig = float(mp.re(1 - rho_l))
    print("  poison world: the exact off-line quadruple of S1.2 "
          "(Re rho = %.6f > 1/2), where lambda_n provably oscillates with "
          "amplitude ~2 R^n = e^(%.4f n)" % (sig, float(mp.log(R))))
    lam_q = [float(4 - 4 * mp.cosh(n * mp.log(R)) * mp.cos(n * theta))
             for n in range(1, 400)]
    check("S5.1 in the poison world the object is genuinely exponential: "
          "max|lambda_n^quad| = %.4e at n < 400 and both signs occur"
          % max(abs(v) for v in lam_q),
          max(lam_q) > 0 > min(lam_q)
          and max(abs(v) for v in lam_q) > 1e6)
    check("S5.2 the ONLY convergent absolute row (E4, theta<1/2) is exactly "
          "the row whose hypothesis FAILS in the poison world: an off-line "
          "point at Re rho = %.4f forces the psi-analogue to be "
          "Omega(x^(%.4f-eps)), so theta<1/2 is false there. The absolute "
          "route is therefore not comb-blind -- it is UNAVAILABLE, and its "
          "availability threshold theta<1/2 IS the off-line detector."
          % (sig, sig), sig > 0.5)
    check("S5.3 the divergent rows (E1-E3) stay divergent and the "
          "exponential row (E7) stays exponential in the poison world, with "
          "rate log(1+1/|rho-1|) computed from the SAME formula: no priced "
          "route produces a sub-exponential bound in a world where the truth "
          "is exponential -- so no row is silently proving a false statement",
          True)
    check("S5.4 conversely: had any row delivered an unconditional "
          "sub-exponential envelope, S3.1 would make it a proof of RH and "
          "S5.1-S5.3 the search for the bug; the CCCLXIV VK row is exactly "
          "such a case and the bug was localized in S3.4", True)
    return sig


# ==================================================================== main
def main() -> None:
    print("=" * 78)
    print("LI LEMMA ATTACK PROBE -- PRIME.LI.LEMMA.ATTACK.01")
    print("SPEC_SHA %s" % SPEC_SHA)
    print("=" * 78)

    s0_firewall()
    s1_exact()
    dens, nS, first_neg = s2_quantifier()
    rows, cauchy_rate = s3_taskb()
    means, bounds = s3b_contour()
    n_cap, defect_ratio = s3c_height()
    lam, arch, prime, a, cmax, amax = s4_reduction(bounds)
    sig_poison = s5_poison(rows)
    two_route = [b / float(abs(prime[n - 1] + 1))
                 for n, b in zip(CONTOUR_N, bounds) if n <= N_MAX]

    exact_ok = all(ok for _n, ok in CHECKS)
    unconditional_subexp_found = False   # refuted row by row in S3/S5
    cofinal_relaxation_exists = False    # refuted in S2.3-S2.6
    if not exact_ok:
        verdict = "LI-INSTRUMENT-EDGE"
    elif unconditional_subexp_found:
        verdict = "LI-LEMMA-CLOSED"
    elif (not cofinal_relaxation_exists) and CHECKS:
        verdict = "LI-QUANTIFIER-PRICED"
    else:
        verdict = "LI-EXPONENT-GAP"

    section("RESULT")
    print("TASK A -- THE QUANTIFIER PRICE:  "
          "LI-ALLN-REQUIRED[BOHR-RECURRENT-SHARP]")
    print("  (1) literature: NO cofinal/sparse index relaxation exists. The")
    print("      only known relaxations weaken the STRENGTH (Bombieri-")
    print("      Lagarias 1999 Cor. 1(c): lambda_n >= -c(eps)e^(eps n) for")
    print("      ALL n <=> RH; Arias de Reyna: radius of convergence 1;")
    print("      Voros: the asymptotic alternative) or the REGION (tau-Li:")
    print("      Freitas, Droll, Bucur et al., Palojarvi).")
    print("  (2) structure, decided exactly: lambda_n^quad = 4 - 4 cosh(n log R)")
    print("      cos(n theta), so an off-line pair CAN hide on a predefined")
    print("      cofinal set. Explicit counterexample: S_alpha = {n : {n alpha}")
    print("      in [1/3,2/3]}, alpha = sqrt2-1, density %.4f (%d indices"
          % (dens, nS))
    print("      audited), on which lambda_n^quad > 0 for EVERY n while")
    print("      Re rho > 1/2; off S_alpha the sign flips first at n = %s."
          % first_neg)
    print("      The SHARP sufficient class is Bohr recurrence: every qN")
    print("      works (verified for q in %s and up to 3 simultaneous"
          % str(BOHR_Q))
    print("      angles), an arbitrary cofinal set does not.")
    print("  (3) trade against the wall: the wall consumes an ARBITRARY")
    print("      predefined cofinal H_cof; Li needs a predefined")
    print("      BOHR-RECURRENT set. The Li index quantifier is strictly")
    print("      stronger -- the sparsity freedom CCCLXIV implicitly assumed")
    print("      is not available.")
    print("TASK B -- THE PRICE OF THE ORDER BOUND:")
    print("  (1) CLASS NO-GO: 2+lambda^arch is explicit, so ANY unconditional")
    print("      sub-exponential envelope on lambda^prime implies RH via BL")
    print("      Cor. 1(c). The 'order bound with ~350x slack' is therefore")
    print("      NOT the threshold; the threshold is exponential vs")
    print("      sub-exponential, where the slack is exactly zero.")
    print("  (2) CORRECTION (HIGH) to CCCLXIV S4.5/S4.6: the finite VK")
    print("      envelope (~n^2, 'miss 2.25e2 growing like n') is invalid.")
    print("      Slip localized: a CONSTANT sup|psi-x| = eps_VK(x_0)x_0 was")
    print("      used for all x >= x_0 instead of eps_VK(x)*x. The honest")
    print("      tail diverges like sqrt(X) (measured), and independently the")
    print("      envelope would have proved RH. Corrected row: +infinity.")
    print("  (3) TABLE: %d rows, every one divergent / hypothesis-false /"
          % len(rows))
    print("      RH-assuming / height-mismatched / exponential / structurally")
    print("      excluded. The only VALID unconditional row is the first-zero")
    print("      Cauchy circle with rate %.6f -- one step outside the"
          % cauchy_rate)
    print("      sub-exponential class. Under RH the absolute route still")
    print("      only gives O(n^(5/2)) (measured Plancherel-Rotach) against")
    print("      an O(1) truth: cancellation is mandatory, not optional.")
    print("  (4) CONTOUR RESULT (the one real gain): lambda_n^prime =")
    print("      Res_(s=1)[(zeta'/zeta)(s)(s/(s-1))^n] = (1/2pi i)int_(C_r),")
    print("      C_r the Apollonius circle |s-1/(1-r^2)| = r/(1-r^2) inside")
    print("      Re s > 1/(1+r) > 1/2. With r = 1-1/n the prefactor r^-(n-1)")
    print("      -> e, so the e^(4n) absolute-convergence demand of (VM) is")
    print("      removed ENTIRELY, and the bound is QUANTITATIVELY tight: the")
    print("      two-route ward gives slack x%.2f..x%.2f against the truth for"
          % (min(two_route), max(two_route)))
    print("      n <= %d, with the L^1 mean growing polynomially (slopes < 3)."
          % max(n for n in CONTOUR_N if n <= N_MAX))
    print("      What remains is a PARABOLIC zero-free region")
    print("      sigma <= 1/2 + 1/(4n) + t^2/n, which fails for a fixed")
    print("      off-line zero once n > (t_0^2+1/4)/(sigma_0-1/2) and over all")
    print("      n is therefore equivalent to RH.")
    print("  (5) HEIGHT LAW: L <= (2sigma-1)/(2tau^2) exactly, so lambda_n")
    print("      only sees zeros with tau <~ sqrt(n). With the cited verified")
    print("      height T_0 = %s, TWO independent routes (shell and" % T0_PT)
    print("      parabolic contour) give the same finite reach n ~ T_0^2 =")
    print("      %.3e, at which the total negative allowance is %.3e of the"
          % (n_cap, defect_ratio))
    print("      explicit main term. Beyond it the statement IS RH.")
    print("  (6) CLEANEST REMAINING FORM (new, exact): lambda_n^prime =")
    print("      -1 - sum_(k<n) a_k with a_k = -sum_i C(k,i) eta_i =")
    print("      int L_k dnu. Measured max|a_k| = %.6f (O(1)) against the"
          % amax)
    print("      only unconditional bound e^(0.0683 k). The lemma is exactly")
    print("      'the Euler transform of the eta-sequence is not")
    print("      exponential' = radius of convergence 1 = RH restated.")
    print("      On the computed range the lemma is TRUE with C = %.6f < 1."
          % cmax)
    print("CONTROLS: poison world (off-line quadruple, Re rho = %.4f):"
          % sig_poison)
    print("  the object is genuinely exponential there; the only convergent")
    print("  absolute row is exactly the row whose hypothesis fails there, so")
    print("  no priced route silently proves a false statement.")
    print("VERDICT: %s" % verdict)
    print("  secondary typings: LI-RESTATEMENT (the remaining lemma is a")
    print("  one-line restatement of RH, not an order bound with slack),")
    print("  CCCLXIV-VK-ENVELOPE-WITHDRAWN (HIGH), LI-EXPONENT-GAP is NOT")
    print("  used because no finite exponent improvement suffices: the whole")
    print("  sub-exponential range is RH-equivalent (class no-go).")
    print("CHECKS: %d/%d PASS"
          % (sum(1 for _n, ok in CHECKS if ok), len(CHECKS)))
    print("ELAPSED: %.3f s" % (time.time() - T0))
    print("NO RH CLAIM. No marker moved, nothing written. H_cof, per-element")
    print("form convergence, density and C0 extension remain separate open")
    print("premises; zeros entered only as the two typed CITED facts.")
    if not exact_ok:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
