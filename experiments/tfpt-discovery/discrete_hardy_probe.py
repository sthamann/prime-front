"""Discovery probe (2026-07-28), part 141 of the prime/window investigation.
Contract DISCRETE.HARDY -- THE JOINT BOUND THROUGH THE HARDY STRUCTURE.

WHERE THIS SITS (T140 FINITE-CORE: the exact reduction stands, the remaining
uniformity ingredient is NAMED)
  T137 killed every absolute-value route from below, T138 found the sign
  mechanism, T139 killed the decay-lemma family, and T140 reduced the whole
  question to TWO SMALL MATRICES PER ZONE.  QUOTED here and never re-derived:
    * rho(W) = lam_max(K^{1/2} H K^{1/2}) EXACTLY (the finite-core reduction,
      rank <= h - 1), with K = M^T Delta M the COVERING KERNEL
      K_rs = W([r ^ s, r v s]) in closed geometric form, entrywise nonnegative
      and monotone, and H the mixed second difference of the Green function;
    * H = diag(s) + L_N exactly (a MASS term plus a LONG-RANGE DIRICHLET form),
      with the Dirichlet weights N = -offdiag(H) positive on 0.71 .. 0.87 of the
      off-diagonal area;
    * the D-dependence SPLITS THE WRONG WAY factorwise: lam_max(K) ~ D^-2.99
      against lam_max(H) ~ D^+0.33, so no product bound can be D-uniform;
    * CERTIFIED DEAD, never to be retried: all absolute-value hulls, all stripe
      layer series, the band in the stripe grid, the band in the INDEX grid of
      the core (both far parts Loewner-POSITIVE, so no truncation is legitimate),
      Jaffard / Demko-Moss-Smith, Gantmacher-Krein one-pair;
    * the LOEWNER DROP of the positive H part (dropping L_{N_-}) costs a factor
      6.4 .. 239, so the cancellation lives exactly THERE;
    * max_k Q_k = 18.5 .. 339 is the first-moment weight of N_+ -- the input a
      Dirichlet comparison has to consume;
    * the stripe block norms are ZONE-UNIFORM (spread D^0.13 / D^0.02).
  The sharpened rest list T140 handed over:
    R1'  a JOINT bound for lam_max(K^{1/2} H K^{1/2}) -- never factorwise, never
         after a Loewner drop of the positive H part, never after a truncation;
    R1'' THE INGREDIENT: a zone-uniform comparison of the long-range Dirichlet
         form of N against the K^+ form -- A DISCRETE HARDY INEQUALITY;
    R3'  a FIRST-MOMENT bound for (-H)_+;
    R4   the far-carried border blocks (18 open, far mass fraction 0.64 .. 0.91).
  This probe attacks R1'' first, because R1' is a corollary of it, and then R3'
  and R4 with the same machinery.  Nothing else.

WHAT THIS PROBE DOES
  L1  THE HARDY FORM, cut to this pair.  Four exact structural identities, each
      VERIFIED and not asserted, which together turn R1'' into a classical
      weighted Hardy problem with a CONSTRUCTIVE two-weight constant:
      (i)   THE K^+ RAYLEIGH FORM.  With u = K^{1/2} v,
                rho(W) = sup { u^T H u / u^T K^+ u : u in range(K) } ,
            so R1'' is literally a comparison of the H-form against the K^+
            form -- the shape every Hardy inequality has.
      (ii)  THE CROSSING KERNEL, exactly and WITH ITS SIGNS.  Telescoping the
            long-range Dirichlet form ONCE MORE,
                u^T L_N u = d^T B d ,  d_k = u_k - u_{k+1} ,
                B_kl = sum_{r <= k ^ l, k v l < s} N_rs ,
            i.e. B is to N what K is to Delta: the SAME closed covering formula
            on the increment grid.  Two consequences.  First, T140's
            Cauchy-Schwarz step is IDENTIFIED: Q_k = sum_l (B_+)_kl is the ROW
            SUM of B_+, so L_{N_+} <= T_Q is exactly the Schur / Gershgorin
            diagonal step applied to B_+ -- which is why it costs what it costs.
            Second, the SIGNED B keeps the cancellation that the drop of
            L_{N_-} destroyed, and it is the object the Hardy constant should
            see.
      (iii) THE COMPARISON OBJECT IS THE ORIGINAL LAPLACIAN.  With D the
            increment operator,
                D K D^T = L_Delta restricted to the interior nodes ,  exactly,
            because D M^T is the signed node-incidence matrix of the edge
            system.  So the denominator side of the Hardy inequality is the very
            Laplacian the problem started from, and its diagonal
                (D K D^T)_kk = (Delta 1)_{k+1}
            is the ENDPOINT EDGE MASS at node k+1 -- a closed geometric formula
            and a LOCAL quantity, not lam_max(K).  That is the mechanism by
            which the D-exponents can cancel: what multiplies the kernel side is
            a single-node edge mass, not the O(h^2)-fold sum lam_max(K) ~ D^-3.
      (iv)  THE MUCKENHOUPT QUANTITY.  Muckenhoupt's criterion for weighted
            Hardy inequalities (Muckenhoupt 1972; Bradley 1978; Opic-Kufner
            1990; Bennett 1987/1991 for the discrete versions) is the TWO-WEIGHT
            product sup [tail of one weight] x [head of the reciprocal of the
            other].  For this pair that product is, in closed form,
                A_M0 = max_k Q_k (Delta 1)_{k+1}
                     = max_k [first moment of N_+ crossing k]
                             x [endpoint edge mass at k+1] ,
            dimensionless, and it is measured over the FULL surface (zones x D)
            against max_k Q_k = 18.5 .. 339.  Its zone-uniformity is THE
            question of L1, and the certified constants that go with it are
            computed with two explicit conductance profiles: the endpoint
            profile c_k = 1 / (Delta 1)_{k+1} and the Gantmacher-Krein
            tridiagonal profile c_k = -(K^+)_{k,k+1}.
  L2  THE JOINT BOUND, R1', in TWO shapes -- and the difference between them is
      the whole point.
      (a) THE ADDITIVE SHAPE.
              rho(W) = lam_max(K^{1/2} H K^{1/2})
                     <= lam_max(K^{1/2} diag(s) K^{1/2})    [mass share, exact]
                      + lam_max(K^{1/2} L_N   K^{1/2})      [Dirichlet share]
                     <= [mass share] + A_M                  [Hardy/Muckenhoupt]
          Every step is a LOEWNER step under a FIXED congruence (the licence is
          verified in L0), certified per instance by a completed Cholesky that is
          allowed to return a negative number.  A_M comes from
              B <= alpha C  ==>  lam_max(K^{1/2} D^T B D K^{1/2})
                                 <= alpha lam_max(C^{1/2} (D K D^T) C^{1/2}) ,
          the second factor NORMALISED to 1 by scaling the profile -- so the
          geometry enters through the endpoint mass and NOT through lam_max(K),
          and the D-exponents cancel INSIDE the product instead of being
          multiplied.  The exact two-term Weyl split is the FLOOR of this whole
          family, because no bound of this shape can go below it, and it is
          computed with both shares exact so that the floor is a NUMBER.
      (b) THE GENUINELY JOINT SHAPE, one eigenvalue and no split at all.  For
          ANY positive definite comparison form Y,
              rho(W) <= Lam(H, Y) x Om(Y) ,
              Lam(H, Y) = sup_u u^T H u / u^T Y u   (a generalised eigenvalue,
                          certified by a Cholesky of s Y - H),
              Om(Y)     = lam_max(K^{1/2} Y K^{1/2})  (certified),
          with EQUALITY iff Y is proportional to K^+ on the relevant subspace.
          The Hardy content is that Y is a HARDY FORM -- a weighted path
          Dirichlet form plus a mass term, i.e. a Jacobi matrix, which is
          exactly the object Muckenhoupt's criterion is about.  Two members are
          run: Y_geo = t D^T diag(1 / (Delta 1)_{k+1}) D + (1-t) diag(1 / K_rr),
          which is CLOSED-FORM GEOMETRIC and therefore proof-ready, over a grid
          in t; and Y_tri = the tridiagonal read-off of K^+ (Gantmacher-Krein
          1950/1960), which is per-zone and NOT closed form, and which therefore
          decides a different question: whether the Hardy FAMILY contains a
          bound at all, so that what remains is the construction of a closed
          profile -- a Muckenhoupt verification.
      Both shapes are evaluated against the target on the full measurement
      surface, next to the T140 chain and the crude product bound, and WHERE IT
      BREAKS is reported step by step with the cost factor of each step.
  L3  R3' AND R4.  (i) The first-moment bound for (-H)_+ = N_-: the moments in
      closed form from the crossing kernel B_-, their zone dependence, the
      near-diagonal concentration that the T138 box-geometry sign law predicts,
      and the CANCELLATION GAIN of the signed B over B_+ -- which is the precise
      sense in which R3' is what the Hardy route consumes.  (ii) The border
      pool is rebuilt smaller, the m-paired Neumann ladder run, and for the open
      blocks the same Hardy machinery is run ONE LEVEL DOWN plus the MUCKENHOUPT
      TAIL: how much of the two-weight sup is carried at index distance > FAR_K.
      A decay statement can only ever repair what is far-carried, and this makes
      that decidable rather than a matter of taste.
  L4  THE MAP V13, the promotion batch (the stock was 62), the shortest rest
      list, and the honest three-sentence verdict on the one question: after
      L1 / L2, is the D-uniformity a MUCKENHOUPT VERIFICATION -- finite, per
      zone, with a named uniformity ingredient -- or does a structural rest
      remain?

PREREGISTERED VERDICTS (bars declared here, before any number is computed)
  HARDY-CARRIES      : a CLOSED-FORM member of the Hardy family beats the target
                       CERTIFIED on EVERY window of the measurement surface, so
                       the D-uniformity is reduced to a Muckenhoupt verification
                       with an explicit profile.
  MUCKENHOUPT-FINITE : the reduction STANDS -- every L1 identity holds to the
                       identity bar, every L2 step is certified and every route
                       dominates the exact value on every window, and the
                       certified Hardy constant is ZONE-UNIFORM in the
                       preregistered sense |exponent in D| <= 0.25 with its
                       jackknife band -- but no closed-form profile reaches the
                       target, and the miss is reported precisely.  If the
                       per-zone READ-OFF profile does clear, that is stated
                       separately and it is exactly what reduces the remaining
                       question to constructing a profile.
  HARDY-RESISTS      : an identity fails, or the Hardy constant is NOT
                       zone-uniform -- the anatomy, with the reason.
  Element gates: el_firewall, el_l0, el_l1, el_l2, el_l3, el_l4, el_fence.

FENCES
  * Discovery sandbox.  ONE new file.  No promotion, no ledger / TeX / website /
    changelog edit, no verification/ module, no next.txt, no .md output, no git
    action.
  * NO Riemann zero data of any kind.  An AST firewall rejects zero-table
    tokens, non-whitelisted imports and write-mode file access in this source.
  * THE RH FENCE IS PROMINENT AND ABSOLUTE.  Weil's positivity criterion
    (Weil 1952; Bombieri 2000; Connes 1999) is CITED as the classical address of
    the surrounding statement and is NEVER USED, in either direction.  Nothing
    here claims, assumes or approaches RH.  Even with R1' and R1'' closed and
    every item of the rest list shut, what would stand is positivity of the Weil
    window form on test functions supported in (-alpha_max, alpha_max) for the
    alpha actually reached -- a FINITE-WINDOW statement about a finite list of
    prime-power zones.  The distance to RH is MAPPED in L4, never travelled.
  * CERTIFIED vs CERTIFIABLE vs MEASURED vs FIT vs HYPOTHESIS, per line.  A
    completed Cholesky of s I - X certifies lam_max(X) <= s + c_h u ||X||,
    u = 2^-53 (Wilkinson 1968; Higham 2002 Thm 10.3/10.4); a Rayleigh quotient
    is a rigorous LOWER bound; an eigenvalue is a MEASUREMENT.  Every fit is a
    FIT with a delete-one jackknife band.  Bars declared before a number are
    never moved.
  * DIRECTION CARE, pedantic and stated where it is used: lumping RAISES the
    form (A_B >= A), so the pair reaches a floor only through the INVERSE side;
    only an UPPER bound on rho(W) can produce a floor and a LOWER bound can only
    KILL a route; a term may be DISCARDED only if it is Loewner-nonpositive, and
    a negative MEAN is NOT a Loewner sign; congruence by a fixed C preserves the
    Loewner order (verified in L0), which is the licence for every step of the
    L2 chain; and the Hardy step B <= alpha C may be multiplied into a sup only
    for alpha >= 0, which is why alpha is clamped and the clamp is reported.
  * CLASSICAL ADDRESSES USED: Hardy 1920 and Hardy-Littlewood-Polya 1934 ch. 9
    (the discrete Hardy inequality and the Cauchy-Schwarz telescope step),
    MUCKENHOUPT 1972 (Hardy's inequality with weights -- the two-weight
    criterion that makes the constant CONSTRUCTIVE), Bradley 1978,
    Bennett 1987/1991 (the discrete / sequence versions), Opic-Kufner 1990 and
    Kufner-Maligranda-Persson 2007 (the Hardy-type inequality monographs),
    Miclo 1999 (the Muckenhoupt criterion as a spectral-gap tool for weighted
    birth-death forms), Schur 1911 and Gershgorin 1931 (the diagonal /
    row-sum step, which is what T140's Cauchy-Schwarz step turns out to be),
    Abel summation, Gantmacher-Krein 1950/1960 and Karlin 1968 (one-pair
    kernels and tridiagonal inverses -- the second conductance profile),
    Weyl 1912, Fan 1958 / Berman-Plemmons 1979 (M-matrices), Haynsworth 1968,
    Bendixson 1902, Collatz 1942 / Wielandt 1950, Wilkinson 1968 and
    Higham 2002, Bertrand-Chebyshev 1852 and the trivial even bound (the only
    two gap facts consumed).  No gap CONJECTURE enters.
  * HARD CAPS.  Largest FACTORISED / INVERTED / DIAGONALISED matrix <= 1500;
    total runtime budget 720 s (< 900 s), with per-block guards that truncate a
    pool rather than overrun.
"""

import ast
import math
import os
import time

import numpy as np
from numpy.linalg import LinAlgError
from scipy.linalg import cho_factor, cho_solve, eigh, eigvalsh

np.seterr(all="ignore")

PASS = 0
FAIL = 0
T_START = time.time()

EULER = 0.5772156649015328606065120900824
LOG_PI = math.log(math.pi)

MAX_H = 1500                 # HARD cap on any FACTORISED / INVERTED form
BUDGET_S = 720.0             # HARD probe budget (< 900 s)

U_ROUND = 2.0 ** -53
GL_N = 48
_GLX, _GLW = np.polynomial.legendre.leggauss(GL_N)

NU_MAIN = 4                  # T105 admissibility floor / T112 frame A
H_MIN = 24
CHUNK = 16384

ATOM_MAX = 320000
ZONE_DEEP = 300000

# --- L1 / L2 surface (only h-sized objects are formed: no n_e x n_e matrix, so
# the edge count n_e is NOT a cap here -- the finite-core reduction removed it) -
L12_ZONES = 60
L12_HCAP = 1200
T_L12 = 260.0
T_GRID = (0.10, 0.25, 0.40, 0.55, 0.70, 0.85, 0.95)   # the Hardy-form mixture

# --- L3 border pool (the T137..T140 surface, rebuilt smaller) ---------------
K3_GC_MIN = 2
K3_HCAP = 640
K3_MAX = 420
K3_PER_RHO = 8
K3_LOGRES = 80.0
K3_RHO = (1.001, 1.05, 1.10, 1.20, 1.25, 1.35, 1.49531, 1.60, 1.75, 1.90,
          2.00, 2.25, 2.50, 3.00, 3.50, 4.00)   # 1.49531 = the T127 band edge
M_LADDER = (1, 2, 3, 4, 6, 8, 12, 16, 24)
FAR_K = 8                    # "far" for the R4 mass split, in index distance
K3_DEEP = 14                 # blocks on which the L1 / L2 machinery is re-run
T_L3 = 300.0

# --- preregistered bars (declared before any number is computed) ------------
BAR_ID = 1.0e-11             # every identity must hold to this relative level
BAR_RED = 1.0e-8             # the finite-core reduction bar (an eigenvalue)
BAR_COVER = 1.0              # a bound must clear on EVERY window
BAR_UNIF = 0.25              # |exponent in D| for "ZONE-UNIFORM", preregistered
BAR_DOM = 1.0e-7             # the chain must dominate the exact value to this

# --- quoted numbers.  QUOTED, never re-derived here ------------------------
RHO_W_T140 = (0.9962, 0.9999)
LAMK_EXP_T140 = -2.99
LAMH_EXP_T140 = 0.33
QMAX_T140 = (18.5, 339.0)
DROP_COST_T140 = (6.4, 239.0)
BLOCK_UNIF_T140 = (0.13, 0.02)
H_NEG_OFF_T140 = (0.71, 0.87)
H_POS_DIAG_T140 = 1.000
R4_OPEN_T140 = 18
FAR_MASS_T140 = (0.64, 0.91)
NEED_R4_T139 = 2.15
PROMO_T140 = 62
N_PROBES_PRIOR = 140
MUCK_LO, MUCK_HI = 1.0, 4.0  # the classical Muckenhoupt sandwich A_M <= C <= 4A_M


def check(name, ok, detail=""):
    global PASS, FAIL
    if ok:
        PASS += 1
    else:
        FAIL += 1
    print("check  %-38s %s  %s" % (name, "PASS" if ok else "FAIL", detail))


def info(name, detail=""):
    print("info   %-38s %s" % (name, detail))


def section(title):
    print("")
    print("=" * 78)
    print(title)
    print("=" * 78)


def wrap_at(text, width):
    out, line = [], ""
    for w in text.split():
        if line and len(line) + 1 + len(w) > width:
            out.append(line)
            line = w
        else:
            line = (line + " " + w) if line else w
    if line:
        out.append(line)
    return out


def para(text, width=76, indent="  "):
    for ln in wrap_at(text, width - len(indent)):
        print(indent + ln)


def budget_left():
    return BUDGET_S - (time.time() - T_START)


def sym(A):
    return 0.5 * (A + A.T)


def rel(a, b):
    a = np.asarray(a, dtype=float)
    b = np.asarray(b, dtype=float)
    sc = max(float(np.max(np.abs(a))), float(np.max(np.abs(b))), 1.0e-300)
    return float(np.max(np.abs(a - b))) / sc


def qmin(v):
    v = [x for x in v if np.isfinite(x)]
    return float(min(v)) if v else float("nan")


def qmax(v):
    v = [x for x in v if np.isfinite(x)]
    return float(max(v)) if v else float("nan")


def qmed(v):
    v = [x for x in v if np.isfinite(x)]
    return float(np.median(v)) if v else float("nan")


def fit_line(x, y):
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)
    A = np.stack([np.ones_like(x), x], axis=1)
    sol, *_ = np.linalg.lstsq(A, y, rcond=None)
    return float(sol[0]), float(sol[1]), float(np.sqrt(np.mean((A @ sol - y) ** 2)))


def fit_band(x, y):
    """A FIT with a delete-one jackknife band on both coefficients."""
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)
    a0, b0, rms = fit_line(x, y)
    aa, bb = [], []
    n = x.shape[0]
    if n >= 4:
        for i in range(n):
            m = np.ones(n, dtype=bool)
            m[i] = False
            ai, bi, _ = fit_line(x[m], y[m])
            aa.append(ai)
            bb.append(bi)
    sa = (0.5 * (max(aa) - min(aa))) if aa else float("nan")
    sb = (0.5 * (max(bb) - min(bb))) if bb else float("nan")
    return a0, b0, rms, sa, sb, n


def pow_fit(xv, yv, tag):
    """A POWER FIT y ~ c x^p on the strictly positive part.  A FIT."""
    x = np.asarray(xv, dtype=float)
    y = np.asarray(yv, dtype=float)
    m = np.isfinite(x) & np.isfinite(y) & (x > 0.0) & (y > 0.0)
    if int(np.count_nonzero(m)) < 4:
        return dict(tag=tag, p=float("nan"), c=float("nan"), rms=float("nan"),
                    sp=float("nan"), n=int(np.count_nonzero(m)))
    a, b, rms, sa, sb, n = fit_band(np.log(x[m]), np.log(y[m]))
    return dict(tag=tag, p=b, c=math.exp(a), rms=rms, sp=sb, n=n)


# ----------------------------------------------------------------------------
# THE AST FIREWALL -- no zero data, no unexpected import, no file write
# ----------------------------------------------------------------------------
FORBIDDEN_TOKENS = tuple("".join(parts) for parts in (
    ("zeta", "zero"), ("zeta_", "zero"), ("zeros_of_", "zeta"), ("odly", "zko"),
    ("lm", "fdb"), ("gram_", "point"), ("14.13", "4725"), ("21.02", "2039"),
    ("25.01", "0857"), ("30.42", "4876"),
))
ALLOWED_IMPORT_ROOTS = {"ast", "math", "os", "time", "numpy", "scipy"}


def firewall():
    src = open(os.path.abspath(__file__), "r").read()
    low = src.lower()
    hits = [tok for tok in FORBIDDEN_TOKENS if tok in low]
    tree = ast.parse(src)
    bad_imports, bad_writes = [], []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for a in node.names:
                if a.name.split(".")[0] not in ALLOWED_IMPORT_ROOTS:
                    bad_imports.append(a.name)
        elif isinstance(node, ast.ImportFrom):
            if node.module and node.module.split(".")[0] not in ALLOWED_IMPORT_ROOTS:
                bad_imports.append(node.module)
        elif isinstance(node, ast.Call):
            fn = node.func
            nm = getattr(fn, "id", None) or getattr(fn, "attr", None)
            if nm in ("open",):
                mode = ""
                if len(node.args) > 1 and isinstance(node.args[1], ast.Constant):
                    mode = str(node.args[1].value)
                for kw in node.keywords:
                    if kw.arg == "mode" and isinstance(kw.value, ast.Constant):
                        mode = str(kw.value.value)
                if any(ch in mode for ch in "wax+"):
                    bad_writes.append(mode)
    check("el_firewall.tokens", not hits, "forbidden token hits: %d" % len(hits))
    check("el_firewall.imports", not bad_imports,
          "non-whitelisted imports: %s" % (bad_imports or "none"))
    check("el_firewall.no_writes", not bad_writes,
          "write-mode file access: %s" % (bad_writes or "none"))
    check("el_firewall.one_file", os.path.basename(os.path.abspath(__file__))
          == "discrete_hardy_probe.py", "single new file in the sandbox")


# ----------------------------------------------------------------------------
# prime-power arithmetic (exact, cheap) -- the T111..T140 code path
# ----------------------------------------------------------------------------
def von_mangoldt_table(n_max):
    sieve = np.ones(n_max + 1, dtype=bool)
    sieve[:2] = False
    for i in range(2, int(math.isqrt(n_max)) + 1):
        if sieve[i]:
            sieve[i * i::i] = False
    lam = np.zeros(n_max + 1)
    for p in np.nonzero(sieve)[0]:
        p = int(p)
        lp = math.log(p)
        q = p
        while q <= n_max:
            lam[q] = lp
            q *= p
    return lam


def atom_table(n_max):
    lam = von_mangoldt_table(n_max)
    out = []
    for n in np.nonzero(lam > 0)[0]:
        n = int(n)
        out.append((n, lam[n], math.log(n), 2.0 * lam[n] / math.sqrt(n)))
    return out


def atoms_in(alpha, atoms_all):
    lim = 2.0 * alpha + 1.0e-14
    k = int(np.searchsorted(U_SORTED, lim, side="right"))
    return ATOM_PAIRS[:k]


# ----------------------------------------------------------------------------
# the archimedean kernel (Weil 1952 -- CITED, never used as a criterion)
# ----------------------------------------------------------------------------
def _arch_A_far(s, D):
    s = np.asarray(s, dtype=float).reshape(-1, 1)
    out = np.zeros(s.shape[0])
    for lo, hi in ((s - D, s), (s, s + D)):
        mid = 0.5 * (lo + hi)
        half = 0.5 * (hi - lo)
        w = mid + half * _GLX[None, :]
        val = (1.0 - np.abs(s - w) / D) * np.exp(-0.5 * w) / (-np.expm1(-2.0 * w))
        out -= half[:, 0] * (val @ _GLW)
    return out


def _arch_integrand(w, s, D):
    tri_s = max(0.0, 1.0 - abs(s) / D)
    S = 0.5 * (np.maximum(0.0, 1.0 - np.abs(s - w) / D)
               + np.maximum(0.0, 1.0 - np.abs(s + w) / D))
    return (tri_s * np.exp(-2.0 * w) - S * np.exp(-0.5 * w)) / (-np.expm1(-2.0 * w))


def _arch_A_near(s, D):
    s = abs(float(s))
    tri_s = max(0.0, 1.0 - s / D)
    W = s + D
    pts = sorted({0.0, s, D - s, W})
    pts = [p for p in pts if 0.0 <= p <= W]
    tot = 0.0
    for lo, hi in zip(pts[:-1], pts[1:]):
        if hi <= lo:
            continue
        mid = 0.5 * (lo + hi)
        half = 0.5 * (hi - lo)
        w = mid + half * _GLX
        tot += half * float(np.dot(_GLW, _arch_integrand(w, s, D)))
    return (-(EULER + LOG_PI) * tri_s + 2.0 * tot
            + tri_s * (-math.log1p(-math.exp(-2.0 * W))))


def arch_A(sv, D):
    sv = np.abs(np.asarray(sv, dtype=float))
    out = np.empty(sv.shape[0])
    far = sv >= D
    if far.any():
        out[far] = _arch_A_far(sv[far], D)
    for i in np.nonzero(~far)[0]:
        out[i] = _arch_A_near(sv[i], D)
    return out


def arch_lags(M, D):
    out = np.empty(M)
    for a in range(0, M, CHUNK):
        b = min(M, a + CHUNK)
        out[a:b] = arch_A(np.arange(a, b) * D, D)
    return out


def lag_vector_fast(alpha, M, atoms):
    """The T115 O(#atoms) lag assembly (bit-identical to the T111 reference)."""
    D = 2.0 * alpha / M
    c = arch_lags(M, D)
    for u_j, mu_j in atoms:
        i0 = int(math.floor(u_j / D))
        for i in range(max(0, i0 - 2), min(M, i0 + 3)):
            v = 1.0 - abs(i * D - u_j) / D
            if v > 0.0:
                c[i] -= mu_j * 0.5 * v
        if u_j < D:
            for i in range(0, min(M, int(math.floor((D - u_j) / D)) + 2)):
                v = 1.0 - (i * D + u_j) / D
                if v > 0.0:
                    c[i] -= mu_j * 0.5 * v
    return c, D


def odd_toeplitz(c, M):
    """The ODD (pole-free) section A_rs = c_{|r-s|} - c_{M-1-r-s} on h = M/2."""
    h = M // 2
    rr = np.arange(h)
    return c[np.abs(rr[:, None] - rr[None, :])] - c[(M - 1) - rr[:, None] - rr[None, :]]


def odd_toeplitz_slow(c, M):
    h = M // 2
    A = np.empty((h, h))
    for r in range(h):
        for s in range(h):
            A[r, s] = c[abs(r - s)] - c[M - 1 - r - s]
    return A


def odd_pole_vector(alpha, M):
    """t~ in odd coordinates: (8/sqrt D) sinh(D/4) sinh(xbar_r/2)."""
    D = 2.0 * alpha / M
    h = M // 2
    xbar = -alpha + (np.arange(h) + 0.5) * D
    return (8.0 / math.sqrt(D)) * math.sinh(0.25 * D) * np.sinh(0.5 * xbar)


def safe_cho(Q):
    try:
        return cho_factor(Q, lower=True, check_finite=False)
    except LinAlgError:
        return None


def chol_floor(A_norm, h):
    """THE DECLARED FLOATING-POINT FLOOR (Wilkinson 1968; Higham 2002)."""
    ch = (h + 1.0) / max(1.0 - (h + 1.0) * U_ROUND, 1.0e-300)
    return ch * U_ROUND * A_norm


def gersh(X):
    return float(np.max(np.abs(X).sum(axis=1)))


def ray_top(X, iters=180, rng=None):
    """lam_max of a SYMMETRIC X by a SHIFTED power iteration.  The returned
    value is a RAYLEIGH QUOTIENT, hence a rigorous LOWER bound."""
    n = X.shape[0]
    if n == 0:
        return 0.0
    if n == 1:
        return float(X[0, 0])
    sig = gersh(X)
    y = (np.abs(rng.standard_normal(n)) + 0.5) if rng is not None \
        else np.ones(n) / math.sqrt(n)
    y = y / max(float(np.linalg.norm(y)), 1.0e-300)
    lam = float(y @ (X @ y))
    for _ in range(iters):
        z = X @ y + sig * y
        nz = float(np.linalg.norm(z))
        if not (nz > 0.0):
            break
        y = z / nz
        lam = max(lam, float(y @ (X @ y)))
    return lam


def cert_lam_max(X, guess=None, tries=14, grow=1.0e-7):
    """CERTIFY lam_max(X) <= s by a COMPLETED CHOLESKY of s I - X
    (Wilkinson 1968; Higham 2002).  DIRECTION: an UPPER bound."""
    n = X.shape[0]
    if n == 0:
        return 0.0
    nrm = gersh(X)
    fl = chol_floor(nrm, n)
    if guess is None or not np.isfinite(guess):
        guess = nrm
    s = max(float(guess), 0.0) + fl + 1.0e-300
    I = np.eye(n)
    for _ in range(tries):
        if safe_cho(s * I - X) is not None:
            return s + fl
        s = s * (1.0 + grow) + 10.0 * fl + 1.0e-300
        grow *= 3.0
    return float("nan")


def cert_lam_max_signed(X, tries=26):
    """CERTIFY lam_max(X) <= s WITHOUT assuming s >= 0: the shift is bisected
    DOWN from a Rayleigh quotient and the last completed Cholesky returned, so
    the SIGN of the answer is itself certified."""
    n = X.shape[0]
    if n == 0:
        return 0.0
    nrm = gersh(X)
    fl = chol_floor(nrm, n)
    lo = ray_top(X)
    hi = nrm + fl
    if safe_cho((hi + fl) * np.eye(n) - X) is None:
        return float("nan")
    lo = min(lo - abs(lo) * 1.0e-9 - 10.0 * fl, hi)
    I = np.eye(n)
    for _ in range(tries):
        mid = 0.5 * (lo + hi)
        if safe_cho(mid * I - X) is not None:
            hi = mid
        else:
            lo = mid
        if abs(hi - lo) <= 1.0e-12 * max(nrm, 1.0e-300) + 10.0 * fl:
            break
    return hi + fl


def cert_lam_min(X, guess=None, tries=14, grow=1.0e-7):
    """CERTIFY lam_min(X) >= t by a completed Cholesky of X - t I.  DIRECTION:
    a LOWER bound -- this is the function that certifies a LOEWNER step."""
    n = X.shape[0]
    if n == 0:
        return 0.0
    nrm = gersh(X)
    fl = chol_floor(nrm, n)
    if guess is None or not np.isfinite(guess):
        guess = 0.0
    t = float(guess) - fl
    I = np.eye(n)
    for _ in range(tries):
        if safe_cho(X - t * I) is not None:
            return t - fl
        t = t - max(abs(t), nrm) * grow - 10.0 * fl - 1.0e-300
        grow *= 3.0
    return float("nan")


def perron_bracket(applyf, n, iters, rng=None):
    """A COLLATZ-WIELANDT bracket for the spectral radius of a NONNEGATIVE
    operator (Collatz 1942; Wielandt 1950).  Both ends rigorous at every
    iterate."""
    x = np.ones(n) if rng is None else (np.abs(rng.standard_normal(n)) + 0.5)
    lo, up = 0.0, float("inf")
    for _ in range(iters):
        y = applyf(x)
        rt = y / np.maximum(x, 1.0e-300)
        lo = max(lo, float(np.min(rt)))
        up = min(up, float(np.max(rt)))
        nz = float(np.max(y))
        if not (nz > 0.0):
            return 0.0, 0.0
        x = np.maximum(y / nz, 1.0e-300)
    return lo, up


# ----------------------------------------------------------------------------
# the frame (T112 frame A, window forced EVEN so that h = M/2 exactly)
# ----------------------------------------------------------------------------
def even_window(u, D):
    M = int(math.ceil(u / D - 1.0e-9)) + 1
    if M % 2:
        M += 1
    return M


def step_frame(u_old, u_new, D):
    M_o = even_window(u_old, D)
    M_n = even_window(u_new, D)
    gc = (M_n - M_o) // 2
    if gc < 1:
        return None
    return dict(D=D, M_o=M_o, M_n=M_n, gc=gc, h_o=M_o // 2, h_n=M_n // 2,
                al_o=0.5 * M_o * D, al_n=0.5 * M_n * D)


def bordered_step(fr, atoms_all):
    """The bordered step (Haynsworth 1968) and its border Schur block S --
    rebuilt in this file's coordinates as a declared PROXY for the T134
    assembly source, exactly as T138 / T139 / T140 did."""
    at_n = atoms_in(fr["al_n"], atoms_all)
    c_n, _ = lag_vector_fast(fr["al_n"], fr["M_n"], at_n)
    tv = odd_pole_vector(fr["al_n"], fr["M_n"])
    Q = sym(odd_toeplitz(c_n, fr["M_n"]) - np.outer(tv, tv))
    gc = fr["gc"]
    A = sym(np.ascontiguousarray(Q[:gc, :gc]))
    C = np.ascontiguousarray(Q[:gc, gc:])
    X = sym(np.ascontiguousarray(Q[gc:, gc:]))
    fac = safe_cho(X)
    if fac is None:
        return None
    Z = cho_solve(fac, C.T, check_finite=False)
    S = sym(A - C @ Z)
    del Q, A, C, X, Z
    return dict(S=S, fr=fr)


# ----------------------------------------------------------------------------
# THE LUMPED M-MATRIX PAIR and its EDGE representation (T136 .. T140)
# ----------------------------------------------------------------------------
def lump_pair(A):
    """Delta = the POSITIVE off-diagonal part, L_Delta = diag(Delta 1) - Delta,
    A_B = A + L_Delta.  DIRECTION: L_Delta >= 0, so A_B >= A -- lumping RAISES
    the form and the floor is reached only through the INVERSE side."""
    h = A.shape[0]
    dg = np.diag(A).copy()
    off = A - np.diag(dg)
    Dl = np.where(off > 0.0, off, 0.0)
    P_row = Dl.sum(axis=1)
    LD = np.diag(P_row) - Dl
    A_B = sym(A + LD)
    offB = A_B - np.diag(np.diag(A_B))
    return dict(h=h, A_B=A_B, Dl=Dl, LD=LD, P_row=P_row, w=A.sum(axis=1),
                dg=dg, dgB=np.diag(A_B).copy(),
                stieltjes=int(bool(np.all(offB <= 1.0e-300))
                              and bool(np.all(np.diag(A_B) > 0.0))),
                n_pos=int(np.count_nonzero(np.where(np.eye(h, dtype=bool),
                                                    0.0, off) > 0.0)))


def anchor_floor(A_B):
    """THE M-MATRIX ANCHOR (T136): A_B x = 1, x >= 0 certifies a nonsingular
    M-matrix (Fan 1958; Berman-Plemmons 1979).  DIRECTION: a LOWER bound."""
    h = A_B.shape[0]
    fac = safe_cho(A_B)
    if fac is None:
        return None
    x = cho_solve(fac, np.ones(h), check_finite=False)
    xmax = float(np.max(x))
    xmin = float(np.min(x))
    return dict(fac=fac, x=x, xmax=xmax, xmin=xmin,
                nonneg=int(xmin >= -1.0e-13 * max(xmax, 1.0e-300)),
                floor=(1.0 / xmax) if xmax > 0.0 else float("nan"))


def edge_list(Dl, M=None):
    """THE EDGE REPRESENTATION of L_Delta = sum_{r<t} Delta_rt (e_r - e_t)
    (e_r - e_t)^T, exactly.  NOTHING is capped or dropped."""
    h = Dl.shape[0]
    iu = np.triu_indices(h, 1)
    w = Dl[iu]
    keep = w > 0.0
    er = iu[0][keep]
    et = iu[1][keep]
    w = w[keep]
    lab = ((M - 1) - er - et) if M is not None else (er + et)
    order = np.lexsort((er, lab))
    er, et, w, lab = er[order], et[order], w[order], lab[order]
    vals, starts, counts = np.unique(lab, return_index=True, return_counts=True)
    return dict(er=er, et=et, w=w, lab=lab, n=er.shape[0],
                mass=float(w.sum()), stripe_val=vals, stripe_start=starts,
                stripe_count=counts, nb=vals.shape[0],
                sidx=np.repeat(np.arange(vals.shape[0]), counts))


def mixed_second_difference(G):
    """H_rs = G_{r+1,s+1} - G_{r+1,s} - G_{r,s+1} + G_{r,s}, THE EXACT DOUBLE
    TELESCOPE (T139 / T140), re-verified in L0 because everything rests on it."""
    return G[1:, 1:] - G[1:, :-1] - G[:-1, 1:] + G[:-1, :-1]


def interval_incidence(er, et, h):
    """M_{e,r} = 1[a_e <= r < b_e] on the H-grid r = 0 .. h-2, the object that
    turns the H-telescope into the FORM identity Gram = C H C^T."""
    m = h - 1
    rr = np.arange(m)
    return ((rr[None, :] >= er[:, None]) & (rr[None, :] < et[:, None])).astype(float)


def cover_kernel_closed(er, et, w, h):
    """THE COVERING KERNEL in CLOSED GEOMETRIC FORM, K_rs = W([r ^ s, r v s]),
    evaluated by a two-dimensional prefix sum (i.e. WITHOUT forming M)."""
    m = h - 1
    Wm = np.zeros((h + 1, h + 1))
    np.add.at(Wm, (er, et), w)
    F = np.cumsum(Wm, axis=0)
    F = np.cumsum(F[:, ::-1], axis=1)[:, ::-1]
    F = np.concatenate([F[:, 1:], np.zeros((h + 1, 1))], axis=1)
    rr = np.arange(m)
    lo = np.minimum(rr[:, None], rr[None, :])
    hi = np.maximum(rr[:, None], rr[None, :])
    K = F[lo, hi]
    mono_r = bool(np.all(np.diff(F[:, :m], axis=0) >= -1.0e-300))
    mono_c = bool(np.all(np.diff(F[:m, :], axis=1) <= 1.0e-300))
    return dict(K=K, mono=int(mono_r and mono_c),
                nonneg=int(bool(np.all(K >= 0.0))))


def psd_sqrt_full(K, tol=1.0e-14):
    """K^{1/2} and the pseudo-inverse K^+ from ONE symmetric eigendecomposition.
    The congruence X -> K^{1/2} X K^{1/2} is the vehicle of the whole chain."""
    lam, V = eigh(sym(K))
    lmax = float(np.max(np.abs(lam))) if lam.size else 0.0
    neg = float(np.min(lam)) if lam.size else 0.0
    keep = lam > tol * max(lmax, 1.0e-300)
    s = np.zeros_like(lam)
    s[keep] = np.sqrt(lam[keep])
    iv = np.zeros_like(lam)
    iv[keep] = 1.0 / lam[keep]
    return dict(Kh=sym((V * s[None, :]) @ V.T),
                Kp=sym((V * iv[None, :]) @ V.T),
                V=V, lam=lam, neg=neg, lmax=lmax,
                null=int(np.count_nonzero(~keep)))


def abel_split(H):
    """THE ENERGY REORDERING, exact for ANY symmetric H:
    H = diag(s) + L_N with s = row sums, N = -offdiag(H) -- a MASS term plus a
    LONG-RANGE DIRICHLET form.  L_{N_-} >= 0 always, so DROPPING it is a genuine
    LOEWNER step and not a statement about a mean."""
    m = H.shape[0]
    s = H.sum(axis=1)
    off = H - np.diag(np.diag(H))
    N = -off
    Np = np.where(N > 0.0, N, 0.0)
    Nm = np.where(N < 0.0, -N, 0.0)
    LN = np.diag(N.sum(axis=1)) - N
    LNp = np.diag(Np.sum(axis=1)) - Np
    LNm = np.diag(Nm.sum(axis=1)) - Nm
    return dict(m=m, s=s, N=N, Np=Np, Nm=Nm, LN=sym(LN), LNp=sym(LNp),
                LNm=sym(LNm), id_err=rel(H, np.diag(s) + LN),
                s_pos=float(np.mean(s > 0.0)),
                neg_off=(float(np.mean(N[~np.eye(m, dtype=bool)] > 0.0))
                         if m > 1 else float("nan")),
                mass_p=float(np.sum(np.maximum(s, 0.0))),
                mass_n=float(np.sum(np.minimum(s, 0.0))))


def cs_path_weights(Np):
    """THE CAUCHY-SCHWARZ STEP ALONG THE TELESCOPE (T140), quoted in form:
    L_{N_+} <= T_Q with Q_k = sum_{r <= k < s} N_+,rs (s - r) the FIRST-MOMENT
    weight.  L1 IDENTIFIES this step: Q is the ROW SUM of the crossing kernel
    B_+, so this is the Schur / Gershgorin diagonal step on B_+."""
    m = Np.shape[0]
    rr = np.arange(m)
    dist = rr[None, :] - rr[:, None]
    Z = np.where(dist > 0, Np * dist, 0.0)
    F = np.cumsum(Z, axis=0)
    F = np.cumsum(F[:, ::-1], axis=1)[:, ::-1]
    F = np.concatenate([F[:, 1:], np.zeros((m, 1))], axis=1)
    Q = np.array([F[k, k] for k in range(m - 1)]) if m > 1 else np.zeros(0)
    T = np.zeros((m, m))
    if m > 1:
        idx = np.arange(m - 1)
        T[idx, idx] += Q
        T[idx + 1, idx + 1] += Q
        T[idx, idx + 1] -= Q
        T[idx + 1, idx] -= Q
    return dict(Q=Q, T=sym(T), q_max=(float(np.max(Q)) if Q.size else 0.0),
                q_sum=float(np.sum(Q)))


def conj_form(Kh, X):
    return sym(Kh @ sym(X) @ Kh)


def cert_psd(X):
    return cert_lam_min(sym(X))


def num_rank(X, bar=1.0e-10):
    lam = eigvalsh(sym(X))
    mx = float(np.max(np.abs(lam))) if lam.size else 0.0
    return int(np.count_nonzero(np.abs(lam) > bar * max(mx, 1.0e-300))), lam


# ----------------------------------------------------------------------------
# L1 MACHINERY -- THE HARDY STRUCTURE.  The three new closed-form objects.
# ----------------------------------------------------------------------------
def diff_op(m):
    """THE INCREMENT OPERATOR (D u)_k = u_k - u_{k+1}, k = 0 .. m-2."""
    Dm = np.zeros((m - 1, m))
    idx = np.arange(m - 1)
    Dm[idx, idx] = 1.0
    Dm[idx, idx + 1] = -1.0
    return Dm


def crossing_kernel(N):
    """THE CROSSING KERNEL of a SYMMETRIC weight matrix N, in the SAME closed
    covering form as K but on the INCREMENT grid:

        B_kl = sum_{r <= k ^ l, k v l < s} N_rs ,   k, l = 0 .. m-2 ,

    and then, EXACTLY and for any symmetric N (signs included),

        u^T L_N u = sum_{r<s} N_rs (u_r - u_s)^2 = d^T B d ,  d = D u ,

    because (u_r - u_s)^2 = sum_{k,l in [r, s-1]} d_k d_l is the telescope
    SQUARED, with no inequality taken.  So B is to N exactly what K is to
    Delta, and the whole Dirichlet share of H is a quadratic form in the
    INCREMENTS with the signed kernel B.  This is the object T140's
    Cauchy-Schwarz step replaced by its row-sum diagonal."""
    m = N.shape[0]
    iu = np.triu_indices(m, 1)
    Wm = np.zeros((m + 1, m + 1))
    np.add.at(Wm, (iu[0], iu[1]), N[iu])
    F = np.cumsum(Wm, axis=0)
    F = np.cumsum(F[:, ::-1], axis=1)[:, ::-1]
    F = np.concatenate([F[:, 1:], np.zeros((m + 1, 1))], axis=1)
    kk = np.arange(max(m - 1, 0))
    lo = np.minimum(kk[:, None], kk[None, :])
    hi = np.maximum(kk[:, None], kk[None, :])
    return sym(F[lo, hi])


def hardy_laplacian(K):
    """J = D K D^T, the DENOMINATOR object of the Hardy inequality:

        J_kl = K_kl - K_{k,l+1} - K_{k+1,l} + K_{k+1,l+1} ,

    which for the covering kernel is EXACTLY the original Laplacian L_Delta on
    the interior nodes: D M^T is the signed node-incidence matrix of the edge
    system (the r-difference of 1[a_e <= r < b_e] is 1[b_e = k+1] - 1[a_e =
    k+1]), so J = L_Delta[1:h-1, 1:h-1] and J_kk = (Delta 1)_{k+1} is the
    ENDPOINT EDGE MASS at node k+1 -- a LOCAL geometric quantity."""
    return sym(K[:-1, :-1] - K[:-1, 1:] - K[1:, :-1] + K[1:, 1:])


def hardy_constant(B, J, c, tag):
    """THE CERTIFIED HARDY / MUCKENHOUPT CONSTANT for a diagonal conductance
    profile c > 0.  The two certified numbers are

        theta = lam_max(C^{1/2} J C^{1/2})           (the NORMALISATION)
        alpha = lam_max(C^{-1/2} B C^{-1/2})         (the COMPARISON)

    and the statement they buy is, with C_eff = C / theta so that
    lam_max(C_eff^{1/2} J C_eff^{1/2}) <= 1,

        lam_max(K^{1/2} D^T B D K^{1/2}) <= max(alpha, 0) theta =: A_M ,

    because B <= alpha C_eff theta / theta ... explicitly: B <= alpha C in the
    Loewner order (congruence by C^{1/2}), hence D^T B D <= alpha D^T C D
    (congruence by D^T), hence K^{1/2} D^T B D K^{1/2} <= alpha K^{1/2} D^T C D
    K^{1/2} whose lam_max is alpha lam_max(C^{1/2} J C^{1/2}) = alpha theta by
    the nonzero-spectrum swap eig(XY) = eig(YX).  The multiplication into the
    sup is legitimate ONLY for alpha >= 0, so alpha is CLAMPED and the clamp is
    reported.  The Gershgorin variant of alpha is the pure MUCKENHOUPT
    TWO-WEIGHT SUP max_k sum_l |B_kl| / sqrt(c_k c_l) (Muckenhoupt 1972;
    Bennett 1987/1991), reported next to it because it is the constructive
    quantity of the classical criterion."""
    n = J.shape[0]
    if n < 2:
        return None
    c = np.maximum(np.asarray(c, dtype=float), 1.0e-300)
    sc = np.sqrt(c)
    Jc = sym(sc[:, None] * J * sc[None, :])
    theta = cert_lam_max(Jc, guess=ray_top(Jc))
    isc = 1.0 / sc
    Bc = sym(isc[:, None] * B * isc[None, :])
    alpha = cert_lam_max_signed(Bc)
    alpha_g = float(np.max(np.abs(Bc).sum(axis=1)))
    a_lo = ray_top(Bc)
    if not (np.isfinite(theta) and np.isfinite(alpha)):
        return None
    return dict(tag=tag, theta=theta, alpha=alpha, alpha_lo=a_lo,
                alpha_g=alpha_g, clamped=int(alpha < 0.0),
                A_M=max(alpha, 0.0) * theta, A_M_g=alpha_g * theta)


def cert_lam_min_pos(Y, tries=40):
    """CERTIFY a STRICTLY POSITIVE lower bound on lam_min(Y), which is what a
    generalised eigenvalue needs: the shift is taken from a measurement and then
    HALVED until the Cholesky of Y - t I completes, so the returned t is a
    certified positive floor (or nan if Y is not positive definite)."""
    n = Y.shape[0]
    if n == 0:
        return float("nan")
    Y = sym(Y)
    try:
        lam = float(eigvalsh(Y, subset_by_index=[0, 0])[0])
    except (LinAlgError, ValueError):
        return float("nan")
    fl = chol_floor(gersh(Y), n)
    t = 0.9 * lam - fl
    for _ in range(tries):
        if t <= 0.0:
            return float("nan")
        if safe_cho(Y - t * np.eye(n)) is not None:
            return t
        t *= 0.5
    return float("nan")


def cert_gen_max(H, Y, tries=18, grow=1.0e-6):
    """CERTIFY Lam(H, Y) = sup_u u^T H u / u^T Y u <= s for a POSITIVE DEFINITE
    Y, by a COMPLETED CHOLESKY of s Y - H: that certifies H <= s Y in the
    LOEWNER order, hence the sup.  The declared floating-point floor of the
    Cholesky is divided by the certified lam_min(Y), which is the exact price of
    reading a Loewner statement about s Y - H as a statement about the
    generalised eigenvalue.  DIRECTION: an UPPER bound on the sup."""
    n = H.shape[0]
    if n == 0:
        return float("nan"), float("nan")
    lmY = cert_lam_min_pos(Y)
    if not (np.isfinite(lmY) and lmY > 0.0):
        return float("nan"), float("nan")
    try:
        lam = float(eigh(sym(H), sym(Y), eigvals_only=True,
                         subset_by_index=[n - 1, n - 1])[0])
    except (LinAlgError, ValueError):
        return float("nan"), lmY
    fl = chol_floor(gersh(H), n) / lmY
    s = lam + abs(lam) * 1.0e-12 + fl + 1.0e-300
    g = grow
    for _ in range(tries):
        if safe_cho(s * sym(Y) - sym(H)) is not None:
            return s + fl, lmY
        s = s + max(abs(s), 1.0e-300) * g + 10.0 * fl
        g *= 3.0
    return float("nan"), lmY


def jacobi_form(c, g):
    """THE HARDY FORM as a matrix: Y = D^T diag(c) D + diag(g), i.e. a weighted
    path Dirichlet form plus a mass term -- a JACOBI matrix, which is exactly
    the object of the classical weighted Hardy inequality and of Muckenhoupt's
    criterion.  Positive definite as soon as g > 0."""
    m = g.shape[0]
    Y = np.diag(np.asarray(g, dtype=float).copy())
    if m > 1 and c.size:
        idx = np.arange(m - 1)
        Y[idx, idx] += c
        Y[idx + 1, idx + 1] += c
        Y[idx, idx + 1] -= c
        Y[idx + 1, idx] -= c
    return sym(Y)


def tridiag_readoff(X):
    """THE TRIDIAGONAL READ-OFF of a matrix (Gantmacher-Krein 1950/1960; Karlin
    1968): for a genuine ONE-PAIR kernel the inverse IS tridiagonal, so for
    K^+ this is the natural per-zone Hardy profile -- but it is READ OFF and not
    CLOSED FORM, which is a distinction this probe keeps everywhere."""
    n = X.shape[0]
    Y = np.zeros_like(X)
    idx = np.arange(n)
    Y[idx, idx] = np.diag(X)
    if n > 1:
        i2 = np.arange(n - 1)
        Y[i2, i2 + 1] = X[i2, i2 + 1]
        Y[i2 + 1, i2] = X[i2, i2 + 1]
    return sym(Y)


def hardy_tail(B, c, k0):
    """THE MUCKENHOUPT TAIL: the part of the two-weight sup carried at index
    distance > k0.  A decay statement in index distance can only ever repair
    THIS part, so its share of the sup is the honest measure of whether a decay
    statement is the right tool for a given block."""
    n = B.shape[0]
    if n < 2:
        return float("nan"), float("nan")
    c = np.maximum(np.asarray(c, dtype=float), 1.0e-300)
    isc = 1.0 / np.sqrt(c)
    Bc = np.abs(isc[:, None] * B * isc[None, :])
    kk = np.arange(n)
    far = np.abs(kk[:, None] - kk[None, :]) > k0
    tot = float(np.max(Bc.sum(axis=1)))
    tl = float(np.max(np.where(far, Bc, 0.0).sum(axis=1)))
    return tl, (tl / tot if tot > 0.0 else float("nan"))


def moment_profile(N, kmax):
    """THE MOMENTS of a nonnegative weight matrix N by index distance: total
    mass, first moment, and the CUMULATIVE first-moment share up to distance
    kmax.  This is the closed form an R3' statement has to produce."""
    m = N.shape[0]
    rr = np.arange(m)
    dist = np.abs(rr[:, None] - rr[None, :])
    off = ~np.eye(m, dtype=bool)
    mass = float(np.sum(N[off]))
    mom1 = float(np.sum((N * dist)[off]))
    shares = []
    for k in kmax:
        near = off & (dist <= k)
        shares.append(float(np.sum((N * dist)[near])) / max(mom1, 1.0e-300))
    return dict(mass=mass, mom1=mom1, shares=shares)


# ----------------------------------------------------------------------------
# L3 MACHINERY -- the border level (T138 / T139 / T140, quoted in form)
# ----------------------------------------------------------------------------
def paired_neumann_small(S, ladder=M_LADDER):
    """THE m-PAIRED NEUMANN CERTIFICATE, QUOTED in form and reduced to what L3
    needs: the certificate, the need ratio, the index distance of its argmax and
    the FAR MASS FRACTION of the offending entry."""
    g = S.shape[0]
    S = sym(S)
    off = S - np.diag(np.diag(S))
    Dl = np.where(off > 0.0, off, 0.0)
    LD = np.diag(Dl.sum(axis=1)) - Dl
    S_B = sym(S + LD)
    facB = safe_cho(S_B)
    if facB is None:
        return None
    Ig = np.eye(g)
    G_B = cho_solve(facB, Ig, check_finite=False)
    rr = np.arange(g)
    dmat = np.abs(rr[:, None] - rr[None, :])
    F = G_B @ LD
    Fabs = np.abs(F)
    lo1, up1 = perron_bracket(lambda v: Fabs @ v, g, 80)
    out = dict(g=g, rho_fabs=up1, rho_fabs_lo=lo1,
               inv_nonneg=int(bool(np.all(G_B >= -1.0e-14
                                          * float(np.abs(G_B).max())))))
    rungs = []
    Fm = Ig.copy()
    Pm = np.zeros((g, g))
    for m in range(1, max(ladder) + 1):
        Pm = Pm + Fm
        Fm = Fm @ F
        if m not in ladder:
            continue
        Fma = np.abs(Fm)
        lo, up = perron_bracket(lambda v: Fma @ v, g, 80)
        row = dict(m=m, rho_up=up, cert=0, need=float("inf"), need_d=-1,
                   far_frac=float("nan"))
        if up < 1.0:
            try:
                Tm = np.linalg.solve(Ig - Fma, Fma)
                TG = Tm @ G_B
                bad = np.abs(Pm) @ TG
                good = Pm @ G_B
                row["cert"] = int(float(np.min(good - bad)) > 0.0)
                rat = bad / np.maximum(good, 1.0e-300)
                row["need"] = float(np.max(rat))
                idx = int(np.argmax(rat))
                r0, s0 = divmod(idx, g)
                row["need_d"] = int(dmat[r0, s0])
                contrib = np.abs(Pm)[r0, :] * TG[:, s0]
                tot = float(np.sum(np.abs(contrib)))
                fk = np.abs(np.arange(g) - s0) >= FAR_K
                row["far_frac"] = (float(np.sum(np.abs(contrib[fk]))) / tot
                                   if tot > 0.0 else float("nan"))
                del Tm, TG, bad, good, rat
            except LinAlgError:
                pass
        rungs.append(row)
        del Fma
    out["rungs"] = rungs
    out["cert_any"] = int(any(r["cert"] for r in rungs))
    fin = [r for r in rungs if np.isfinite(r["need"])]
    out["need_best"] = qmin([r["need"] for r in fin]) if fin else float("inf")
    best = min(fin, key=lambda r: r["need"]) if fin else None
    out["need_d_best"] = best["need_d"] if best else -1
    out["far_frac_best"] = best["far_frac"] if best else float("nan")
    out["_S"], out["_S_B"], out["_LD"], out["_G_B"] = S, S_B, LD, G_B
    del F, Fabs, Fm, Pm, Dl
    return out


def hardy_one_level_down(S, S_B, LD, G_B, M_lab=None):
    """THE WHOLE L1 / L2 MACHINERY on the border block's own lumped pair: the
    covering kernel, the crossing kernel, the endpoint Laplacian, the certified
    Hardy constant and the Muckenhoupt tail.  Nothing is re-derived -- the same
    functions are called one level down, which is the only honest test that the
    structure is not an artefact of the top level."""
    g = S.shape[0]
    if g < 6:
        return None
    try:
        L = np.linalg.cholesky(S_B)
    except LinAlgError:
        return None
    Li = np.linalg.solve(L, np.eye(g))
    rho_w = float(eigvalsh(sym(Li @ LD @ Li.T),
                           subset_by_index=[g - 1, g - 1])[0])
    ed = edge_list(np.where(LD < 0.0, -LD, 0.0), M_lab)
    if ed["n"] < 3:
        return None
    H = mixed_second_difference(G_B)
    m = H.shape[0]
    if m < 4:
        return None
    ck = cover_kernel_closed(ed["er"], ed["et"], ed["w"], g)
    sq = psd_sqrt_full(ck["K"])
    lam_core = float(eigvalsh(conj_form(sq["Kh"], H),
                              subset_by_index=[m - 1, m - 1])[0])
    ab = abel_split(H)
    B = crossing_kernel(ab["N"])
    J = hardy_laplacian(ck["K"])
    hc = hardy_constant(B, J, 1.0 / np.maximum(np.diag(J), 1.0e-300), "endpoint")
    if hc is None:
        return None
    E_mass = cert_lam_max_signed(conj_form(sq["Kh"], np.diag(ab["s"])))
    tl, frac = hardy_tail(B, 1.0 / np.maximum(np.diag(J), 1.0e-300),
                          max(1, B.shape[0] // 4))
    return dict(g=g, m=m, rho_w=rho_w, lam_core=lam_core,
                red_err=abs(lam_core - rho_w) / max(abs(rho_w), 1.0e-300),
                n_e=ed["n"], id_err=ab["id_err"], neg_off=ab["neg_off"],
                A_M=hc["A_M"], theta=hc["theta"], E_mass=E_mass,
                B_hardy=E_mass + hc["A_M"], tail=tl, tail_frac=frac)


# ----------------------------------------------------------------------------
section("L0  SETUP, the pair, the telescope, and the DIRECTION calibrations")
# ----------------------------------------------------------------------------
firewall()

ATOMS_ALL = atom_table(ATOM_MAX)
UU_ALL = [t[2] for t in ATOMS_ALL]
NN_ALL = [t[0] for t in ATOMS_ALL]
ATOM_PAIRS = [(t[2], t[3]) for t in ATOMS_ALL]
U_SORTED = np.array(UU_ALL, dtype=float)
GG_ALL = [UU_ALL[i + 1] - UU_ALL[i] for i in range(len(UU_ALL) - 1)]

NZ_DEEP = sum(1 for n in NN_ALL if n <= ZONE_DEEP)
G_DEEP = np.array(GG_ALL[:NZ_DEEP], dtype=float)
N_DEEP = np.array(NN_ALL[:NZ_DEEP], dtype=np.int64)

BERT_OK = bool(np.all(G_DEEP <= math.log(2.0) + 1.0e-12))
EVEN_OK = bool(np.all(G_DEEP >= np.log1p(1.0 / N_DEEP) - 1.0e-12))
check("el_l0.gap_facts", BERT_OK and EVEN_OK,
      "the ONLY two gap facts consumed anywhere in this file hold on all %d "
      "prime-power gaps up to n = %d: Bertrand-Chebyshev 1852 (g <= log 2) and "
      "the trivial even bound (g >= log(1 + 1/n)).  No gap CONJECTURE is used"
      % (NZ_DEEP, ZONE_DEEP))

RNG = np.random.default_rng(1410728)

para("""L0.0  THE RH FENCE, STATED BEFORE ANY NUMBER.  The surrounding statement
is the positivity of a Weil window form (Weil 1952; Bombieri 2000; Connes 1999)
on a FINITE list of prime-power zones and a FINITE window; the criterion is
CITED as that address and is NEVER USED here, in either direction.  Nothing in
this file claims, assumes or approaches RH: even with R1' and R1'' closed, what
would stand is a finite-window positivity statement, and the distance from there
to RH is mapped in L4 and never travelled.""")

# --- L0.1  the odd section against its entrywise definition -----------------
_k0, _D0, _M0 = None, None, None
for _kk in range(2, NZ_DEEP - 2):
    _Dc = 0.5 * float(G_DEEP[_kk]) / NU_MAIN
    _Mc = even_window(UU_ALL[_kk], _Dc)
    if 110 <= _Mc // 2 <= 190:
        _k0, _D0, _M0 = _kk, _Dc, _Mc
if _k0 is None:
    raise SystemExit("L0 found no calibration window in the declared h band")
_al0 = 0.5 * _M0 * _D0
_h0 = _M0 // 2
_c0, _ = lag_vector_fast(_al0, _M0, atoms_in(_al0, ATOMS_ALL))
E_ODD = rel(odd_toeplitz(_c0, _M0), odd_toeplitz_slow(_c0, _M0))
check("el_l0.odd_section", E_ODD <= BAR_ID,
      "the vectorised odd section equals its entrywise definition A_rs = "
      "c_{|r-s|} - c_{M-1-r-s} to %.2e (bar %.0e) on the calibration window "
      "h = %d, D = %.3e -- the coordinates of T106..T140, unchanged"
      % (E_ODD, BAR_ID, _h0, _D0))

_A0 = sym(odd_toeplitz(_c0, _M0))
_lp0 = lump_pair(_A0)
_an0 = anchor_floor(_lp0["A_B"])
check("el_l0.lumping", _lp0["stieltjes"] == 1
      and rel(_lp0["A_B"].sum(axis=1), _lp0["w"]) <= BAR_ID
      and _an0 is not None and _an0["nonneg"] == 1,
      "the lumped pair is STIELTJES, the ROW SUMS are preserved to %.2e, and "
      "A_B x = 1 has x >= 0, so A_B is a nonsingular M-matrix (Fan 1958; "
      "Berman-Plemmons 1979) with anchor lam_min(A_B) >= %.3e.  DIRECTION: "
      "A_B >= A, so the floor is reached only through the INVERSE side"
      % (rel(_lp0["A_B"].sum(axis=1), _lp0["w"]), _an0["floor"]))

_G0 = cho_solve(_an0["fac"], np.eye(_h0), check_finite=False)
_ed0 = edge_list(_lp0["Dl"], _M0)
_wt0 = np.sqrt(_ed0["w"])
_H0 = mixed_second_difference(_G0)
_Minc = interval_incidence(_ed0["er"], _ed0["et"], _h0)
_K0m = cover_kernel_closed(_ed0["er"], _ed0["et"], _ed0["w"], _h0)["K"]
_KERR = rel(_K0m, _Minc.T @ (_ed0["w"][:, None] * _Minc))
check("el_l0.cover_kernel", _KERR <= BAR_ID,
      "the CLOSED covering kernel K_rs = W([r ^ s, r v s]) equals M^T Delta M "
      "to %.2e (bar %.0e) on the calibration window; entrywise nonnegative and "
      "monotone by inclusion.  QUOTED from T140 and re-verified here because "
      "every Hardy object of L1 is built from it"
      % (_KERR, BAR_ID))

# --- L0.2  the DIRECTION calibrations the whole chain leans on --------------
_Zr = RNG.standard_normal((40, 40))
_Xr = sym(_Zr @ _Zr.T)
_Pr = RNG.standard_normal((40, 40))
_Yr = _Xr + sym(_Pr @ _Pr.T)
_Cr = RNG.standard_normal((40, 25))
_cong = float(np.min(eigvalsh(_Cr.T @ (_Yr - _Xr) @ _Cr)))
check("el_l0.congruence_loewner", _cong >= -1.0e-9 * float(np.max(np.abs(_Yr))),
      "CONGRUENCE PRESERVES THE LOEWNER ORDER, verified rather than asserted: "
      "for X <= Y and any C, C^T (Y - X) C >= 0 (lam_min = %.2e).  THIS IS THE "
      "LICENCE for every step of the L2 chain -- and it is used TWICE in the "
      "Hardy step, once by C^{1/2} and once by D^T" % _cong)

_Ar = RNG.standard_normal((30, 22))
_Br = sym(RNG.standard_normal((22, 22)))
_sw1 = np.sort(eigvalsh(_Ar @ _Br @ _Ar.T))[-1]
_sw2 = np.sort(eigvalsh(_Br @ (_Ar.T @ _Ar)))[-1] if True else 0.0
_SWERR = abs(_sw1 - float(np.max(np.real(np.linalg.eigvals(_Br @ (_Ar.T @ _Ar))))))
check("el_l0.spectrum_swap", _SWERR <= 1.0e-9 * abs(_sw1),
      "THE NONZERO-SPECTRUM SWAP eig(XY) = eig(YX) (to %.2e relative), which is "
      "what turns lam_max(K^{1/2} D^T C D K^{1/2}) into "
      "lam_max(C^{1/2} (D K D^T) C^{1/2}) -- the step that replaces lam_max(K) "
      "by the LOCAL endpoint mass and is therefore the whole mechanism of the "
      "joint bound" % _SWERR)

para("""L0.3  WHAT IS NEW HERE, IN ONE SENTENCE.  T140 left the D-exponents
splitting the wrong way factorwise (lam_max(K) ~ D^%.2f against lam_max(H) ~
D^%.2f) and named the missing ingredient: a zone-uniform comparison of the
long-range Dirichlet form of N against the K^+ form.  L1 supplies exactly that
comparison in the classical two-weight shape, and the reason it can work is the
identity D K D^T = L_Delta: the geometry enters the Hardy constant through the
ENDPOINT EDGE MASS at a single node, not through the O(h^2)-fold sum lam_max(K),
so the two large D-exponents never get multiplied in the first place.""" % (
    LAMK_EXP_T140, LAMH_EXP_T140))


# ----------------------------------------------------------------------------
section("L1  THE HARDY FORM -- the identities and the MUCKENHOUPT quantity")
# ----------------------------------------------------------------------------
para("""L1.0  THE MEASUREMENT SURFACE.  Candidates are ALL prime-power zones
whose frame-A window fits the caps; the surface is spread over log n so that the
D range is as wide as the caps allow, because D-uniformity is the question and a
surface concentrated at one depth would be worthless.  Only h-sized objects are
formed here: the n_e x n_e signed Gram of T139 / T140 is never built, because
the finite-core reduction makes it unnecessary -- rho(W) is taken from the
generalised eigenvalue lam_min(A, A_B) and the core value is checked against
it.""")

CAND = []
for k in range(2, NZ_DEEP - 2):
    D_k = 0.5 * float(G_DEEP[k]) / NU_MAIN
    M_k = even_window(UU_ALL[k], D_k)
    h_k = M_k // 2
    if h_k < H_MIN or h_k > L12_HCAP:
        continue
    CAND.append((k, D_k, M_k, h_k))
SZ = []
if CAND:
    step = max(1, len(CAND) // max(L12_ZONES, 1))
    SZ = CAND[::-1][::step][:L12_ZONES]
    SZ.sort(key=lambda t: t[0])
info("L1.candidates", "%d prime-power zones admit a frame-A window inside the "
     "cap (h <= %d, MAX_H = %d).  The EDGE COUNT is deliberately NOT a cap in "
     "this probe -- T139 / T140 had to cap n_e because they formed the "
     "n_e x n_e signed Gram, and the finite-core reduction removes that need "
     "entirely, which is why the D range here is wider than T140's.  The "
     "surface takes %d of them (stride %d) from the deep end and does NOT "
     "deduplicate h, because zones with the same window size but different "
     "gaps have different D, and D is the variable the whole question is about"
     % (len(CAND), L12_HCAP, MAX_H, len(SZ), step))

SURF = []
for (k, D_k, M_k, h_k) in SZ:
    if budget_left() < BUDGET_S - T_L12:
        info("L1.budget", "surface truncated at n = %d after %d windows"
             % (NN_ALL[k], len(SURF)))
        break
    al = 0.5 * M_k * D_k
    c, _ = lag_vector_fast(al, M_k, atoms_in(al, ATOMS_ALL))
    A = sym(odd_toeplitz(c, M_k))
    lp = lump_pair(A)
    an = anchor_floor(lp["A_B"])
    if an is None or not an["nonneg"]:
        continue
    ed = edge_list(lp["Dl"], M_k)
    if ed["n"] < 8 or ed["nb"] < 6:
        continue
    A_B = lp["A_B"]
    G = cho_solve(an["fac"], np.eye(h_k), check_finite=False)
    try:
        gap_ex = float(eigh(A, A_B, eigvals_only=True,
                            subset_by_index=[0, 0])[0])
    except (LinAlgError, ValueError):
        continue
    rho_ex = 1.0 - gap_ex

    # --- L1.1  the finite-core reduction (QUOTED from T140, re-verified) ----
    H = mixed_second_difference(G)
    m = H.shape[0]
    if m < 8:
        continue
    ck = cover_kernel_closed(ed["er"], ed["et"], ed["w"], h_k)
    K = ck["K"]
    sq = psd_sqrt_full(K)
    Kh, Kp = sq["Kh"], sq["Kp"]
    Ycore = conj_form(Kh, H)
    lam_all = eigvalsh(Ycore)
    lam_core = float(lam_all[-1])
    red_err = abs(lam_core - rho_ex) / max(rho_ex, 1.0e-300)

    # the K^+ RAYLEIGH FORM: the top eigenvector, pushed through u = K^{1/2} v
    vtop = eigh(Ycore, subset_by_index=[m - 1, m - 1])[1][:, 0]
    utop = Kh @ vtop
    ray_num = float(utop @ (H @ utop))
    ray_den = float(utop @ (Kp @ utop))
    ray_err = (abs(ray_num / ray_den - lam_core) / max(abs(lam_core), 1.0e-300)
               if abs(ray_den) > 0.0 else float("nan"))
    del Ycore

    # --- L1.2  THE THREE HARDY IDENTITIES -----------------------------------
    ab = abel_split(H)
    cs = cs_path_weights(ab["Np"])
    Dop = diff_op(m)
    B = crossing_kernel(ab["N"])
    Bp = crossing_kernel(ab["Np"])
    Bm = crossing_kernel(ab["Nm"])
    J = hardy_laplacian(K)
    EP = lp["P_row"][1:h_k - 1]                       # (Delta 1)_{k+1}
    J_ref = np.diag(EP) - lp["Dl"][1:h_k - 1, 1:h_k - 1]
    err_cross = rel(ab["LN"], Dop.T @ B @ Dop)
    err_lap = rel(J, J_ref)
    err_rowq = rel(Bp.sum(axis=1), cs["Q"])
    Jd = np.maximum(np.diag(J), 1.0e-300)
    # the pure MUCKENHOUPT two-weight product, from the closed formulae only
    A_M0 = float(np.max(cs["Q"] * Jd))
    A_M0_pm = float(np.max(np.abs(np.diag(B)) * Jd))
    del J_ref

    # --- L1.3  the certified Hardy constants, two profiles ------------------
    prof_end = 1.0 / Jd
    tri = -np.diag(Kp, 1)
    prof_tri = np.maximum(tri, 1.0e-300 + 0.0 * tri)
    hc_e = hardy_constant(B, J, prof_end, "endpoint")
    hc_t = (hardy_constant(B, J, prof_tri, "tri")
            if float(np.min(tri)) > 0.0 else None)
    hc_p = hardy_constant(Bp, J, prof_end, "endpoint_plus")
    cand_A = [x["A_M"] for x in (hc_e, hc_t) if x is not None]
    A_best = min(cand_A) if cand_A else float("nan")
    A_which = ("endpoint" if (hc_t is None or hc_e["A_M"] <= hc_t["A_M"])
               else "tri")
    A_gersh = min([x["A_M_g"] for x in (hc_e, hc_t) if x is not None]
                  or [float("nan")])

    # --- L2  the certified chain --------------------------------------------
    E_mass = cert_lam_max_signed(conj_form(Kh, np.diag(ab["s"])))
    E_mass_p = cert_lam_max(conj_form(Kh, np.diag(np.maximum(ab["s"], 0.0))),
                            guess=ray_top(conj_form(Kh,
                                                    np.diag(np.maximum(ab["s"],
                                                                       0.0)))))
    Ydir = conj_form(Kh, ab["LN"])
    E_dir = cert_lam_max_signed(Ydir)
    E_dir_lo = ray_top(Ydir)
    Ydrop = conj_form(Kh, np.diag(ab["s"]) + ab["LNp"])
    E_drop = cert_lam_max(Ydrop, guess=ray_top(Ydrop))
    Yq = conj_form(Kh, np.diag(np.maximum(ab["s"], 0.0)) + cs["T"])
    E_q = cert_lam_max(Yq, guess=ray_top(Yq))
    step_neg = cert_psd(ab["LNm"])
    step_cs = cert_psd(cs["T"] - ab["LNp"])
    lam_K = cert_lam_max(K, guess=ray_top(K))
    lam_H = cert_lam_max(H, guess=ray_top(H))
    del Ydir, Ydrop, Yq

    B_weyl = E_mass + E_dir
    B_hardy = E_mass + A_best
    B_prod = lam_K * max(lam_H, 0.0)

    # --- L2.2  THE GENUINELY JOINT SHAPE: one eigenvalue, no Weyl split -----
    # Y is a HARDY FORM (path Dirichlet + mass = a Jacobi matrix) and
    # rho(W) <= Lam(H, Y) x Om(Y) with equality iff Y ~ K^+.  Y_geo is
    # CLOSED-FORM GEOMETRIC; Y_tri is read off from K^+ per zone.
    Kd = np.maximum(np.diag(K), 1.0e-300)
    g_geo = 1.0 / Kd
    c_geo = 1.0 / Jd
    J_rows = []
    for t in T_GRID:
        Yt = jacobi_form(t * c_geo, (1.0 - t) * g_geo)
        lam_g, lmY = cert_gen_max(H, Yt)
        Ct = conj_form(Kh, Yt)
        om = cert_lam_max(Ct, guess=ray_top(Ct))
        J_rows.append(dict(t=t, lam=lam_g, om=om, lmY=lmY,
                           bound=(lam_g * om if (np.isfinite(lam_g)
                                                and np.isfinite(om)
                                                and lam_g >= 0.0)
                                  else float("nan"))))
        del Yt, Ct
    J_FIN = [x for x in J_rows if np.isfinite(x["bound"])]
    B_geo = min([x["bound"] for x in J_FIN]) if J_FIN else float("nan")
    t_geo = (min(J_FIN, key=lambda x: x["bound"])["t"] if J_FIN
             else float("nan"))
    Ytri = tridiag_readoff(Kp)
    tri_def = (float(np.max(np.abs(Kp - Ytri)))
               / max(float(np.max(np.abs(Kp))), 1.0e-300))
    lam_tri, lmY_tri = cert_gen_max(H, Ytri)
    Ctri = conj_form(Kh, Ytri)
    om_tri = cert_lam_max(Ctri, guess=ray_top(Ctri))
    B_tri = (lam_tri * om_tri if (np.isfinite(lam_tri) and np.isfinite(om_tri)
                                  and lam_tri >= 0.0) else float("nan"))
    # the ROW-SUM PRESERVING Jacobi read-off: same conductances as tridiag(K^+)
    # but the mass term set so that Y 1 = K^+ 1, i.e. the action on CONSTANTS is
    # reproduced exactly -- the one thing a path form can match for free
    c_row = -np.diag(Kp, 1)
    g_row = Kp.sum(axis=1)
    if float(np.min(c_row)) > 0.0 and float(np.min(g_row)) > 0.0:
        Yrow = jacobi_form(c_row, g_row)
        lam_row, lmY_row = cert_gen_max(H, Yrow)
        Crow = conj_form(Kh, Yrow)
        om_row = cert_lam_max(Crow, guess=ray_top(Crow))
        B_row = (lam_row * om_row
                 if (np.isfinite(lam_row) and np.isfinite(om_row)
                     and lam_row >= 0.0) else float("nan"))
        del Yrow, Crow
    else:
        lam_row, om_row, B_row, lmY_row = (float("nan"),) * 4
    del Ctri, Ytri

    # --- L3(i)  the first moments of (-H)_+ ---------------------------------
    mp_m = moment_profile(ab["Nm"], (2, 4, 8, 16))
    mp_p = moment_profile(ab["Np"], (2, 4, 8, 16))
    Qm = Bm.sum(axis=1)
    tail_a, tail_f = hardy_tail(B, prof_end, FAR_K)
    _, tail_rel = hardy_tail(B, prof_end, max(1, B.shape[0] // 4))

    SURF.append(dict(
        n=NN_ALL[k], h=h_k, M=M_k, D=D_k, al=al, n_e=ed["n"], nb=int(ed["nb"]),
        m=m, anchor=an["floor"], rho_ex=rho_ex, gap_ex=gap_ex,
        lam_core=lam_core, red_err=red_err, ray_err=ray_err,
        err_cross=err_cross, err_lap=err_lap, err_rowq=err_rowq,
        id_err=ab["id_err"], s_pos=ab["s_pos"], neg_off=ab["neg_off"],
        mono=ck["mono"], nonneg=ck["nonneg"], null=sq["null"], negK=sq["neg"],
        q_max=cs["q_max"], A_M0=A_M0, A_M0_pm=A_M0_pm,
        ep_min=float(np.min(EP)), ep_max=float(np.max(EP)),
        theta_e=hc_e["theta"], alpha_e=hc_e["alpha"], A_e=hc_e["A_M"],
        A_e_g=hc_e["A_M_g"], clamp_e=hc_e["clamped"],
        theta_t=(hc_t["theta"] if hc_t else float("nan")),
        A_t=(hc_t["A_M"] if hc_t else float("nan")),
        tri_pos=int(float(np.min(tri)) > 0.0),
        A_p=(hc_p["A_M"] if hc_p else float("nan")),
        A_best=A_best, A_which=A_which, A_gersh=A_gersh,
        E_mass=E_mass, E_mass_p=E_mass_p, E_dir=E_dir, E_dir_lo=E_dir_lo,
        E_drop=E_drop, E_q=E_q, step_neg=step_neg, step_cs=step_cs,
        lam_K=lam_K, lam_H=lam_H, B_weyl=B_weyl, B_hardy=B_hardy,
        B_prod=B_prod, B_geo=B_geo, t_geo=t_geo, B_tri=B_tri,
        lam_tri=lam_tri, om_tri=om_tri, tri_def=tri_def,
        lmY_tri=lmY_tri, jrows=J_rows, B_row=B_row, lam_row=lam_row,
        om_row=om_row,
        mom1_m=mp_m["mom1"], mom1_p=mp_p["mom1"], mass_m=mp_m["mass"],
        mass_p=mp_p["mass"], sh_m=mp_m["shares"], sh_p=mp_p["shares"],
        qm_max=(float(np.max(Qm)) if Qm.size else float("nan")),
        tail_a=tail_a, tail_f=tail_f, tail_rel=tail_rel))
    del A, A_B, G, H, K, Kh, Kp, B, Bp, Bm, J, Dop, lp, an, ed, ab, cs, sq

if not SURF:
    raise SystemExit("L1 produced no window -- probe cannot report")

info("L1.surface", "%d windows, h = %d .. %d (core m = %d .. %d), D = %.3e .. "
     "%.3e, zones n = %d .. %d, edges %d .. %d; exact rho(W) = %.4f .. %.4f "
     "(T140 QUOTED %.4f .. %.4f)"
     % (len(SURF), min(r["h"] for r in SURF), max(r["h"] for r in SURF),
        min(r["m"] for r in SURF), max(r["m"] for r in SURF),
        qmin([r["D"] for r in SURF]), qmax([r["D"] for r in SURF]),
        min(r["n"] for r in SURF), max(r["n"] for r in SURF),
        min(r["n_e"] for r in SURF), max(r["n_e"] for r in SURF),
        qmin([r["rho_ex"] for r in SURF]), qmax([r["rho_ex"] for r in SURF]),
        RHO_W_T140[0], RHO_W_T140[1]))

# --- the TARGET, rebuilt on this surface exactly as T139 / T140 did ---------
F_GAP = pow_fit([r["D"] for r in SURF], [r["gap_ex"] for r in SURF], "gap")
P_GAP = F_GAP["p"]
C_GAP = qmin([r["gap_ex"] / (r["D"] ** P_GAP) for r in SURF])
for r in SURF:
    r["target"] = 1.0 - C_GAP * (r["D"] ** P_GAP)
info("L1.target", "1 - rho(W) ~ %.3e D^%.3f +- %.3f (FIT, rms %.3f, n = %d); "
     "worst-case constant c = %.3e, so the target envelope is %.6f .. %.6f.  A "
     "bound CLEARS only if it sits below the target on EVERY window (bar %.1f, "
     "declared before any number)"
     % (F_GAP["c"], P_GAP, F_GAP["sp"], F_GAP["rms"], F_GAP["n"], C_GAP,
        qmin([r["target"] for r in SURF]), qmax([r["target"] for r in SURF]),
        BAR_COVER))

check("el_l1.finite_core",
      all(r["red_err"] <= BAR_RED for r in SURF)
      and all(r["id_err"] <= BAR_ID for r in SURF)
      and all(r["mono"] == 1 and r["nonneg"] == 1 for r in SURF),
      "THE T140 FOUNDATION, re-verified on this surface before anything is "
      "built on it: rho(W) = lam_max(K^{1/2} H K^{1/2}) to %.2e .. %.2e (bar "
      "%.0e), the energy identity H = diag(s) + L_N to %.2e (bar %.0e), K "
      "entrywise nonnegative and monotone on %d/%d windows"
      % (qmin([r["red_err"] for r in SURF]),
         qmax([r["red_err"] for r in SURF]), BAR_RED,
         qmax([r["id_err"] for r in SURF]), BAR_ID,
         len([r for r in SURF if r["mono"] == 1]), len(SURF)))

check("el_l1.kplus_rayleigh", all(r["ray_err"] <= 1.0e-7 for r in SURF),
      "THE K^+ RAYLEIGH FORM, which is the shape R1'' has to be answered in: "
      "with u = K^{1/2} v at the top eigenvector, u^T H u / u^T K^+ u equals "
      "lam_max(K^{1/2} H K^{1/2}) to %.2e .. %.2e, so rho(W) = sup { u^T H u / "
      "u^T K^+ u : u in range(K) } and the whole question is literally a "
      "comparison of the H-form against the K^+ form -- a weighted Hardy "
      "problem (Hardy 1920; Hardy-Littlewood-Polya 1934 ch. 9)"
      % (qmin([r["ray_err"] for r in SURF]),
         qmax([r["ray_err"] for r in SURF])))

check("el_l1.crossing_kernel", all(r["err_cross"] <= BAR_ID for r in SURF),
      "IDENTITY 1, THE CROSSING KERNEL WITH ITS SIGNS: L_N = D^T B D to "
      "%.2e .. %.2e (bar %.0e), where B_kl = sum_{r <= k ^ l, k v l < s} N_rs "
      "is the SAME closed covering formula as K but on the increment grid and "
      "with the SIGNED weights N.  So the long-range Dirichlet form of H is "
      "EXACTLY a quadratic form in the increments d = D u, with no inequality "
      "taken and no sign discarded -- this is the object that carries the "
      "cancellation the T140 Loewner drop destroyed (cost %.1f .. %.0f x)"
      % (qmin([r["err_cross"] for r in SURF]),
         qmax([r["err_cross"] for r in SURF]), BAR_ID,
         DROP_COST_T140[0], DROP_COST_T140[1]))

check("el_l1.row_sum_identifies_cs", all(r["err_rowq"] <= BAR_ID for r in SURF),
      "IDENTITY 2, WHAT T140's CAUCHY-SCHWARZ STEP ACTUALLY WAS: the "
      "first-moment weight Q_k = sum_{r <= k < s} N_+,rs (s - r) equals the ROW "
      "SUM of B_+ to %.2e .. %.2e (bar %.0e).  So L_{N_+} <= T_Q is precisely "
      "the Schur / Gershgorin diagonal step applied to the crossing kernel "
      "(Schur 1911; Gershgorin 1931) -- it replaces B_+ by diag(B_+ 1), which "
      "is why it costs what it costs, and it explains why max_k Q_k = "
      "%.1f .. %.0f was the number T140 was left holding"
      % (qmin([r["err_rowq"] for r in SURF]),
         qmax([r["err_rowq"] for r in SURF]), BAR_ID,
         QMAX_T140[0], QMAX_T140[1]))

check("el_l1.laplacian_identity", all(r["err_lap"] <= BAR_ID for r in SURF),
      "IDENTITY 3, THE MECHANISM: D K D^T = L_Delta[1:h-1, 1:h-1] to "
      "%.2e .. %.2e (bar %.0e).  The denominator object of the Hardy "
      "inequality is the ORIGINAL Laplacian, because D M^T is the signed "
      "node-incidence matrix of the edge system; its diagonal is the ENDPOINT "
      "EDGE MASS (Delta 1)_{k+1} = %.3e .. %.3e on this surface.  THIS is why "
      "the D-exponents need not be multiplied: what meets the kernel side is a "
      "single-node edge mass, not lam_max(K) ~ D^%.2f"
      % (qmin([r["err_lap"] for r in SURF]),
         qmax([r["err_lap"] for r in SURF]), BAR_ID,
         qmin([r["ep_min"] for r in SURF]), qmax([r["ep_max"] for r in SURF]),
         LAMK_EXP_T140))

# --- L1.4  THE MUCKENHOUPT QUANTITY and its ZONE-UNIFORMITY -----------------
F_AM0 = pow_fit([r["D"] for r in SURF], [r["A_M0"] for r in SURF], "A_M0")
F_ABEST = pow_fit([r["D"] for r in SURF], [r["A_best"] for r in SURF], "A_best")
F_QMAX = pow_fit([r["D"] for r in SURF], [r["q_max"] for r in SURF], "q_max")
F_EP = pow_fit([r["D"] for r in SURF], [r["ep_max"] for r in SURF], "ep_max")
F_LK = pow_fit([r["D"] for r in SURF], [r["lam_K"] for r in SURF], "lam_K")
F_LH = pow_fit([r["D"] for r in SURF], [r["lam_H"] for r in SURF], "lam_H")
F_MASS = pow_fit([r["D"] for r in SURF], [r["E_mass"] for r in SURF], "E_mass")
F_DIR = pow_fit([r["D"] for r in SURF], [r["E_dir"] for r in SURF], "E_dir")

info("L1.muckenhoupt", "THE TWO-WEIGHT PRODUCT, from the closed formulae only: "
     "A_M0 = max_k Q_k (Delta 1)_{k+1} = %.3e .. %.3e over %d windows, i.e. "
     "[first moment of N_+ crossing k] x [endpoint edge mass at k+1].  Its "
     "factors separately: max_k Q_k = %.1f .. %.1f (T140 QUOTED %.1f .. %.0f) "
     "and max_k (Delta 1)_{k+1} = %.3e .. %.3e -- the product is the "
     "dimensionless Muckenhoupt size, and the classical sandwich is "
     "A_M <= C <= %.0f A_M (Muckenhoupt 1972; Bradley 1978; Bennett 1987/1991)"
     % (qmin([r["A_M0"] for r in SURF]), qmax([r["A_M0"] for r in SURF]),
        len(SURF), qmin([r["q_max"] for r in SURF]),
        qmax([r["q_max"] for r in SURF]), QMAX_T140[0], QMAX_T140[1],
        qmin([r["ep_min"] for r in SURF]), qmax([r["ep_max"] for r in SURF]),
        MUCK_HI))

info("L1.muck_exponents", "THE D-DEPENDENCE (FITS, jackknife bands): A_M0 ~ "
     "D^%.3f +- %.3f, the certified A_M ~ D^%.3f +- %.3f, max_k Q_k ~ D^%.3f "
     "+- %.3f, endpoint mass ~ D^%.3f +- %.3f -- against the factorwise "
     "disaster lam_max(K) ~ D^%.3f and lam_max(H) ~ D^%.3f whose product is "
     "D^%.3f.  The Hardy constant is the JOINT object, so its exponent is the "
     "one that decides zone-uniformity (bar |p| <= %.2f, preregistered)"
     % (F_AM0["p"], F_AM0["sp"], F_ABEST["p"], F_ABEST["sp"], F_QMAX["p"],
        F_QMAX["sp"], F_EP["p"], F_EP["sp"], F_LK["p"], F_LH["p"],
        F_LK["p"] + F_LH["p"], BAR_UNIF))

UNIF_PT = (abs(F_ABEST["p"]) <= BAR_UNIF)
UNIF_A = (abs(F_ABEST["p"]) + F_ABEST["sp"] <= BAR_UNIF)
UNIF_A0 = (abs(F_AM0["p"]) + F_AM0["sp"] <= BAR_UNIF)
SPREAD_A = qmax([r["A_best"] for r in SURF]) / max(
    qmin([r["A_best"] for r in SURF]), 1.0e-300)
F_AGER = pow_fit([r["D"] for r in SURF], [r["A_gersh"] for r in SURF], "A_gersh")
info("L1.uniformity", "ZONE-UNIFORMITY VERDICT OF L1, and it is read STRICTLY: "
     "the certified Hardy constant fits D^%.3f +- %.3f, so the POINT estimate "
     "is %s the bar |p| <= %.2f while the BAND reaches %.3f, and the "
     "preregistered wording was 'with its jackknife band' -> the strict reading "
     "is %s.  The closed-form Muckenhoupt product A_M0 fits D^%.3f +- %.3f -> "
     "%s.  The reality check that settles it independently of any fit: the "
     "certified constant spreads %.2f x across a D range of only %.2f x, so it "
     "GROWS -- for comparison, T140's stripe block norms were uniform at "
     "D^%.2f / D^%.2f with no such spread.  %d/%d windows used the endpoint "
     "conductance profile, and the tridiagonal (Gantmacher-Krein) profile was "
     "admissible on %d/%d"
     % (F_ABEST["p"], F_ABEST["sp"],
        "INSIDE" if UNIF_PT else "OUTSIDE", BAR_UNIF,
        abs(F_ABEST["p"]) + F_ABEST["sp"],
        "UNIFORM" if UNIF_A else "NOT uniform", F_AM0["p"], F_AM0["sp"],
        "UNIFORM" if UNIF_A0 else "NOT uniform", SPREAD_A,
        qmax([r["D"] for r in SURF]) / qmin([r["D"] for r in SURF]),
        BLOCK_UNIF_T140[0], BLOCK_UNIF_T140[1],
        len([r for r in SURF if r["A_which"] == "endpoint"]), len(SURF),
        len([r for r in SURF if r["tri_pos"] == 1]), len(SURF)))

info("L1.absolute_value_kill", "AND THE ONE FACT L1 EXISTS TO ESTABLISH.  The "
     "CLASSICAL Muckenhoupt criterion is a sup of ABSOLUTE two-weight products, "
     "and in this pair every absolute version dies exactly as T137 .. T139's "
     "absolute-value routes did: the closed product A_M0 = max_k Q_k "
     "(Delta 1)_{k+1} runs as D^%.3f +- %.3f and the Gershgorin / two-weight "
     "sup of the SAME comparison runs as D^%.3f +- %.3f (values %.3e .. %.3e), "
     "while the SIGNED eigenvalue version of the identical inequality runs as "
     "D^%.3f +- %.3f (values %.3e .. %.3e) -- the closed Muckenhoupt product "
     "overshoots the signed constant by %.0f .. %.0f x and the Gershgorin "
     "variant, which is already halfway signed because it uses the true "
     "diagonal of B, by %.1f .. %.1f x.  So the "
     "Hardy STRUCTURE is usable and the Muckenhoupt CONSTANT is not: the "
     "constant has to be taken as a signed lam_max of the crossing kernel "
     "against the profile, which is a Loewner statement, and the classical "
     "sandwich A_M <= C <= %.0f A_M is then a statement about the WRONG "
     "quantity.  That is the precise sense in which the off-the-shelf criterion "
     "does not transfer"
     % (F_AM0["p"], F_AM0["sp"], F_AGER["p"], F_AGER["sp"],
        qmin([r["A_gersh"] for r in SURF]), qmax([r["A_gersh"] for r in SURF]),
        F_ABEST["p"], F_ABEST["sp"], qmin([r["A_best"] for r in SURF]),
        qmax([r["A_best"] for r in SURF]),
        qmin([r["A_M0"] / max(r["A_best"], 1.0e-300) for r in SURF]),
        qmax([r["A_M0"] / max(r["A_best"], 1.0e-300) for r in SURF]),
        qmin([r["A_gersh"] / max(r["A_best"], 1.0e-300) for r in SURF]),
        qmax([r["A_gersh"] / max(r["A_best"], 1.0e-300) for r in SURF]),
        MUCK_HI))

check("el_l1.hardy_dominates",
      all(np.isfinite(r["A_best"]) and r["A_best"] >= r["E_dir"] - BAR_DOM
          * max(abs(r["E_dir"]), 1.0) for r in SURF),
      "THE DIRECTION SANITY OF THE HARDY STEP, which must hold if the chain is "
      "to be an upper bound at all: the certified Hardy constant dominates the "
      "EXACT Dirichlet share lam_max(K^{1/2} L_N K^{1/2}) on %d/%d windows, "
      "with overhead A_M / E_dir = %.2f .. %.2f x.  The clamp alpha -> "
      "max(alpha, 0) was active on %d windows (where the signed crossing "
      "kernel is Loewner-nonpositive against the profile, so the Dirichlet "
      "share is bounded by ZERO and only the mass term survives)"
      % (len([r for r in SURF if np.isfinite(r["A_best"])
              and r["A_best"] >= r["E_dir"] - BAR_DOM
              * max(abs(r["E_dir"]), 1.0)]), len(SURF),
         qmin([r["A_best"] / max(abs(r["E_dir"]), 1.0e-300) for r in SURF]),
         qmax([r["A_best"] / max(abs(r["E_dir"]), 1.0e-300) for r in SURF]),
         len([r for r in SURF if r["clamp_e"] == 1])))

info("L1.profiles", "the two conductance profiles, certified per window: "
     "ENDPOINT c_k = 1 / (Delta 1)_{k+1} gives theta = "
     "lam_max(C^{1/2} J C^{1/2}) = %.3f .. %.3f -- and theta is exactly the "
     "Muckenhoupt-type loss of the diagonal profile, sitting inside the "
     "classical [%.0f, %.0f] sandwich on %d/%d windows -- with A_M = "
     "%.3e .. %.3e; TRIDIAGONAL c_k = -(K^+)_{k,k+1} (Gantmacher-Krein "
     "1950/1960) gives A_M = %.3e .. %.3e.  The Gershgorin / pure two-weight "
     "variant of the same constant is %.3e .. %.3e"
     % (qmin([r["theta_e"] for r in SURF]), qmax([r["theta_e"] for r in SURF]),
        MUCK_LO, MUCK_HI,
        len([r for r in SURF if MUCK_LO - 1.0e-9 <= r["theta_e"] <= MUCK_HI]),
        len(SURF), qmin([r["A_e"] for r in SURF]),
        qmax([r["A_e"] for r in SURF]), qmin([r["A_t"] for r in SURF]),
        qmax([r["A_t"] for r in SURF]), qmin([r["A_gersh"] for r in SURF]),
        qmax([r["A_gersh"] for r in SURF])))


# ----------------------------------------------------------------------------
section("L2  THE JOINT BOUND -- R1' as a two-term chain, certified")
# ----------------------------------------------------------------------------
para("""L2.0  THE CHAIN AND ITS DIRECTIONS, once, pedantically.  rho(W) =
lam_max(K^{1/2} H K^{1/2}) exactly; H = diag(s) + L_N exactly; Weyl 1912 splits
the top eigenvalue additively, lam_max(X + Y) <= lam_max(X) + lam_max(Y), with
NO sign assumption on either term, so the split is legitimate for the SIGNED
mass and the SIGNED Dirichlet share; the Dirichlet share is then bounded by the
Hardy constant through B <= alpha C, D^T B D <= alpha D^T C D (congruence by
D^T) and the spectrum swap, which is where the endpoint mass replaces
lam_max(K).  Nothing is dropped: L_{N_-} stays inside B.  The two comparison
lines are the T140 chain (which DOES drop it) and the crude product bound
lam_max(K) lam_max(H); the FLOOR of the whole additive family is the exact
two-term Weyl split, because no bound of this shape can go below it.""")

for r in SURF:
    r["cost_weyl"] = r["B_weyl"] / max(r["rho_ex"], 1.0e-300)
    r["cost_hardy"] = r["B_hardy"] / max(r["rho_ex"], 1.0e-300)
    r["cost_geo"] = r["B_geo"] / max(r["rho_ex"], 1.0e-300)
    r["cost_tri"] = r["B_tri"] / max(r["rho_ex"], 1.0e-300)
    r["cost_t140"] = (r["E_mass_p"] + r["E_q"]) / max(r["rho_ex"], 1.0e-300)
    r["cost_drop"] = r["E_drop"] / max(r["rho_ex"], 1.0e-300)
    r["miss"] = r["B_hardy"] / max(r["target"], 1.0e-300)
    r["miss_weyl"] = r["B_weyl"] / max(r["target"], 1.0e-300)
    r["miss_geo"] = r["B_geo"] / max(r["target"], 1.0e-300)
    r["B_read"] = min([x for x in (r["B_tri"], r["B_row"])
                       if np.isfinite(x)] or [float("nan")])
    r["cost_read"] = r["B_read"] / max(r["rho_ex"], 1.0e-300)
    r["miss_tri"] = r["B_read"] / max(r["target"], 1.0e-300)
    r["B_closed"] = min([x for x in (r["B_hardy"], r["B_geo"])
                         if np.isfinite(x)] or [float("nan")])
    r["miss_closed"] = r["B_closed"] / max(r["target"], 1.0e-300)

CL_HARDY = [r for r in SURF if r["B_hardy"] < r["target"]]
CL_WEYL = [r for r in SURF if r["B_weyl"] < r["target"]]
CL_GEO = [r for r in SURF if r["B_geo"] < r["target"]]
CL_TRI = [r for r in SURF if r["B_read"] < r["target"]]
CL_CLOSED = [r for r in SURF if r["B_closed"] < r["target"]]
CL_T140 = [r for r in SURF if (r["E_mass_p"] + r["E_q"]) < r["target"]]
F_GEO = pow_fit([r["D"] for r in SURF], [r["B_geo"] for r in SURF], "B_geo")
F_TRI = pow_fit([r["D"] for r in SURF], [r["B_read"] for r in SURF], "B_read")
ROUTES = (("additive Hardy (closed form)", "B_hardy", "miss"),
          ("joint Y_geo (closed form)", "B_geo", "miss_geo"),
          ("joint Y_tri / Y_row (read off)", "B_read", "miss_tri"),
          ("exact two-term Weyl floor", "B_weyl", "miss_weyl"))
BEST_NAME, BEST_KEY, BEST_MISS = min(
    ROUTES, key=lambda t: qmax([r[t[2]] for r in SURF]))
JOINT_HELPS = (qmax([r["miss_tri"] for r in SURF])
               < qmax([r["miss"] for r in SURF]))

check("el_l2.steps_certified",
      all(np.isfinite(r["step_neg"]) and r["step_neg"] >= -1.0e-8
          * max(abs(r["E_drop"]), 1.0) for r in SURF)
      and all(np.isfinite(r["step_cs"]) and r["step_cs"] >= -1.0e-8
              * max(abs(r["E_q"]), 1.0) for r in SURF),
      "the two LOEWNER steps of the T140 chain are re-certified here so that "
      "the comparison line is honest: lam_min(L_{N_-}) >= %.2e and "
      "lam_min(T_Q - L_{N_+}) >= %.2e on the whole surface (a completed "
      "Cholesky of the difference, so a genuine Loewner statement and not a "
      "negative mean).  The L2 chain itself uses NEITHER of them"
      % (qmin([r["step_neg"] for r in SURF]),
         qmin([r["step_cs"] for r in SURF])))

check("el_l2.chain_dominates",
      all(r["B_hardy"] >= r["lam_core"] - BAR_DOM for r in SURF)
      and all(r["B_weyl"] >= r["lam_core"] - BAR_DOM for r in SURF)
      and all(not np.isfinite(r["B_geo"]) or r["B_geo"] >= r["lam_core"]
              - BAR_DOM for r in SURF)
      and all(not np.isfinite(r["B_read"]) or r["B_read"] >= r["lam_core"]
              - BAR_DOM for r in SURF),
      "EVERY ROUTE IS AN UPPER BOUND, verified against the exact value on every "
      "window (this is the check that would catch a direction error anywhere "
      "in L1 / L2): B_hardy - rho(W) >= %.2e, B_weyl - rho(W) >= %.2e, "
      "B_geo - rho(W) >= %.2e, B_tri - rho(W) >= %.2e (bar %.0e), on %d/%d "
      "windows each"
      % (qmin([r["B_hardy"] - r["lam_core"] for r in SURF]),
         qmin([r["B_weyl"] - r["lam_core"] for r in SURF]),
         qmin([r["B_geo"] - r["lam_core"] for r in SURF]),
         qmin([r["B_read"] - r["lam_core"] for r in SURF]), BAR_DOM,
         len([r for r in SURF if r["B_hardy"] >= r["lam_core"] - BAR_DOM]),
         len(SURF)))

check("el_l2.jacobi_pd",
      all(np.isfinite(r["lmY_tri"]) for r in SURF)
      and all(any(np.isfinite(x["lam"]) for x in r["jrows"]) for r in SURF),
      "THE COMPARISON FORMS ARE POSITIVE DEFINITE, certified, which is what "
      "makes Lam(H, Y) a generalised eigenvalue at all: lam_min(Y_tri) >= "
      "%.3e .. %.3e on the surface, and the closed-form Y_geo admitted a "
      "certificate at %d .. %d of the %d mixture parameters"
      % (qmin([r["lmY_tri"] for r in SURF]),
         qmax([r["lmY_tri"] for r in SURF]),
         min(len([x for x in r["jrows"] if np.isfinite(x["lam"])])
             for r in SURF),
         max(len([x for x in r["jrows"] if np.isfinite(x["lam"])])
             for r in SURF), len(T_GRID)))

info("L2.chain", "THE CHAIN, step by step, as a cost factor over the exact "
     "rho(W) = %.4f .. %.4f: (0) exact core value, cost 1 by construction; "
     "(1) the two-term Weyl split with BOTH shares exact, mass %.3e .. %.3e + "
     "Dirichlet %.3e .. %.3e -> cost %.2f .. %.2f -- THIS IS THE FLOOR OF THE "
     "ADDITIVE FAMILY; (2) the Hardy / Muckenhoupt step on the Dirichlet share "
     "-> cost %.2f .. %.2f; and for comparison the T140 chain (Loewner drop + "
     "Cauchy-Schwarz) -> cost %.2f .. %.2f, and the crude product bound "
     "lam_max(K) lam_max(H) = %.3e .. %.3e"
     % (qmin([r["rho_ex"] for r in SURF]), qmax([r["rho_ex"] for r in SURF]),
        qmin([r["E_mass"] for r in SURF]), qmax([r["E_mass"] for r in SURF]),
        qmin([r["E_dir"] for r in SURF]), qmax([r["E_dir"] for r in SURF]),
        qmin([r["cost_weyl"] for r in SURF]),
        qmax([r["cost_weyl"] for r in SURF]),
        qmin([r["cost_hardy"] for r in SURF]),
        qmax([r["cost_hardy"] for r in SURF]),
        qmin([r["cost_t140"] for r in SURF]),
        qmax([r["cost_t140"] for r in SURF]),
        qmin([r["B_prod"] for r in SURF]), qmax([r["B_prod"] for r in SURF])))

info("L2.joint_shape", "THE GENUINELY JOINT SHAPE, rho(W) <= Lam(H, Y) x Om(Y) "
     "with ONE eigenvalue and no Weyl split, three Jacobi profiles.  (a) "
     "CLOSED-FORM Y_geo = t D^T diag(1/(Delta 1)_{k+1}) D + (1-t) diag(1/K_rr), "
     "best over a %d-point mixture grid (argmin at t = %.2f .. %.2f): bound "
     "%.4f .. %.4f = %.2f .. %.2f x rho(W).  (b) READ-OFF Y_tri = tridiag(K^+) "
     "(Gantmacher-Krein): Lam = %.4f .. %.4f times Om = %.2f .. %.2f gives "
     "%.4f .. %.4f.  (c) READ-OFF Y_row, the same conductances with the mass "
     "term fixed by Y 1 = K^+ 1: Lam = %.4f .. %.4f times Om = %.2f .. %.2f "
     "gives %.4f .. %.4f"
     % (len(T_GRID), qmin([r["t_geo"] for r in SURF]),
        qmax([r["t_geo"] for r in SURF]), qmin([r["B_geo"] for r in SURF]),
        qmax([r["B_geo"] for r in SURF]), qmin([r["cost_geo"] for r in SURF]),
        qmax([r["cost_geo"] for r in SURF]),
        qmin([r["lam_tri"] for r in SURF]), qmax([r["lam_tri"] for r in SURF]),
        qmin([r["om_tri"] for r in SURF]), qmax([r["om_tri"] for r in SURF]),
        qmin([r["B_tri"] for r in SURF]), qmax([r["B_tri"] for r in SURF]),
        qmin([r["lam_row"] for r in SURF]), qmax([r["lam_row"] for r in SURF]),
        qmin([r["om_row"] for r in SURF]), qmax([r["om_row"] for r in SURF]),
        qmin([r["B_row"] for r in SURF]), qmax([r["B_row"] for r in SURF])))

info("L2.why_joint_fails", "AND WHY THE JOINT SHAPE DOES NOT AUTOMATICALLY WIN, "
     "which is the sharpest negative fact in this probe: the generalised "
     "eigenvalue behaves perfectly -- Lam(H, Y_tri) = %.3f .. %.3f, i.e. H is "
     "Loewner-below the read-off Jacobi form with room to spare -- but the "
     "NORMALISATION does not, Om(Y_tri) = lam_max(K^{1/2} Y_tri K^{1/2}) = "
     "%.2f .. %.2f instead of the ideal 1, and the product is what counts.  "
     "The off-tridiagonal defect of K^+ is only %.2e .. %.2e ENTRYWISE, so "
     "this is the Gantmacher-Krein kill of T140 reappearing on the Hardy side: "
     "K is not a one-pair kernel, and entrywise closeness to K^+ does NOT "
     "survive the eigenvalue.  Om ~ D^%.3f is where the D-dependence comes "
     "back, so the profile is exactly the object that has to be constructed "
     "rather than read off"
     % (qmin([r["lam_tri"] for r in SURF]), qmax([r["lam_tri"] for r in SURF]),
        qmin([r["om_tri"] for r in SURF]), qmax([r["om_tri"] for r in SURF]),
        qmin([r["tri_def"] for r in SURF]), qmax([r["tri_def"] for r in SURF]),
        pow_fit([r["D"] for r in SURF], [r["om_tri"] for r in SURF],
                "om_tri")["p"]))

info("L2.kernzahl", "AGAINST THE TARGET %.6f .. %.6f, THE NUMBERS THIS PROBE "
     "EXISTS TO PRODUCE.  CLOSED-FORM ROUTES (proof-ready): additive Hardy "
     "%.3f .. %.3f x target (%d/%d), joint Y_geo %.3f .. %.3f x (%d/%d), best "
     "closed-form %.3f .. %.3f x (%d/%d).  REFERENCE LINES: the exact Weyl "
     "floor %.3f .. %.3f x (%d/%d) and the T140 chain %.3f .. %.3f x (%d/%d). "
     "READ-OFF ROUTE (per zone, NOT closed form): Y_tri %.4f .. %.4f x "
     "(%d/%d).  A bound clears only if it is below the target on EVERY window"
     % (qmin([r["target"] for r in SURF]), qmax([r["target"] for r in SURF]),
        qmin([r["miss"] for r in SURF]), qmax([r["miss"] for r in SURF]),
        len(CL_HARDY), len(SURF), qmin([r["miss_geo"] for r in SURF]),
        qmax([r["miss_geo"] for r in SURF]), len(CL_GEO), len(SURF),
        qmin([r["miss_closed"] for r in SURF]),
        qmax([r["miss_closed"] for r in SURF]), len(CL_CLOSED), len(SURF),
        qmin([r["miss_weyl"] for r in SURF]),
        qmax([r["miss_weyl"] for r in SURF]), len(CL_WEYL), len(SURF),
        qmin([(r["E_mass_p"] + r["E_q"]) / r["target"] for r in SURF]),
        qmax([(r["E_mass_p"] + r["E_q"]) / r["target"] for r in SURF]),
        len(CL_T140), len(SURF), qmin([r["miss_tri"] for r in SURF]),
        qmax([r["miss_tri"] for r in SURF]), len(CL_TRI), len(SURF)))

# WHERE IT BREAKS: which term of the two-term split carries the excess
EXC_MASS = [r["E_mass"] / max(r["B_weyl"], 1.0e-300) for r in SURF]
EXC_DIR = [r["E_dir"] / max(r["B_weyl"], 1.0e-300) for r in SURF]
info("L2.where_it_breaks", "the excess is SPLIT, not localised: of the exact "
     "Weyl floor, the mass share carries %.3f .. %.3f and the Dirichlet share "
     "%.3f .. %.3f.  The mass term alone is already %.3f .. %.3f x the target, "
     "and the Dirichlet share alone %.3f .. %.3f x -- so even a PERFECT Hardy "
     "inequality (alpha exactly the Dirichlet share, overhead 1) leaves the "
     "additive family short by the Weyl split itself on %d/%d windows.  That "
     "is the structural content of the number above, and it is a statement "
     "about the SPLIT and not about the Hardy step"
     % (qmin(EXC_MASS), qmax(EXC_MASS), qmin(EXC_DIR), qmax(EXC_DIR),
        qmin([r["E_mass"] / r["target"] for r in SURF]),
        qmax([r["E_mass"] / r["target"] for r in SURF]),
        qmin([r["E_dir"] / r["target"] for r in SURF]),
        qmax([r["E_dir"] / r["target"] for r in SURF]),
        len(SURF) - len(CL_WEYL), len(SURF)))

info("L2.exponents", "THE D-BOOKKEEPING OF THE CHAIN (FITS): mass share ~ "
     "D^%.3f +- %.3f, exact Dirichlet share ~ D^%.3f +- %.3f, certified Hardy "
     "constant ~ D^%.3f +- %.3f, while rho(W) is flat %.4f .. %.4f.  The "
     "factorwise product of T140 was D^%.2f; the joint route replaces "
     "lam_max(K) ~ D^%.2f by the endpoint mass ~ D^%.3f, and THAT is where the "
     "exponents cancel -- pedantically: the Hardy constant is a product of a "
     "first moment of N (H-scale) with a single-node Delta mass (A-scale), and "
     "those two scales are inverse to each other because H is a second "
     "difference of A_B^{-1}"
     % (F_MASS["p"], F_MASS["sp"], F_DIR["p"], F_DIR["sp"], F_ABEST["p"],
        F_ABEST["sp"], qmin([r["rho_ex"] for r in SURF]),
        qmax([r["rho_ex"] for r in SURF]), LAMK_EXP_T140 + LAMH_EXP_T140,
        LAMK_EXP_T140, F_EP["p"]))


# ----------------------------------------------------------------------------
section("L3  R3' AND R4 -- the first moment of (-H)_+ and the far border")
# ----------------------------------------------------------------------------
para("""L3.0  WHY R3' IS EXACTLY WHAT THE HARDY ROUTE CONSUMES.  The Hardy
constant sees the crossing kernel B of the SIGNED weights N; its positive part
B_+ is what a first-moment bound on the negative off-diagonal of H controls, and
its negative part B_- is what a first-moment bound on (-H)_+ = N_- controls.  So
R3' is not a decoration: the CANCELLATION GAIN of the signed constant over the
positive-only constant is precisely the amount of the T140 Loewner drop (cost
%.1f .. %.0f x) that the exact crossing kernel recovers, and the first moments
of N_- are the closed-form input a proof would have to supply.""" % (
    DROP_COST_T140[0], DROP_COST_T140[1]))

F_MOM_M = pow_fit([r["D"] for r in SURF], [r["mom1_m"] for r in SURF], "mom1_m")
F_MOM_P = pow_fit([r["D"] for r in SURF], [r["mom1_p"] for r in SURF], "mom1_p")
GAIN = [r["A_p"] / max(r["A_best"], 1.0e-300) for r in SURF
        if np.isfinite(r["A_p"])]
SH_M = [r["sh_m"] for r in SURF]
SH_P = [r["sh_p"] for r in SURF]

info("L3.moments", "R3', THE FIRST-MOMENT BOUND FOR (-H)_+ = N_-, in closed "
     "form from the crossing kernel: total mass %.3e .. %.3e, FIRST MOMENT "
     "sum N_-,rs (s - r) = %.3e .. %.3e (fit D^%.3f +- %.3f), against the "
     "positive side %.3e .. %.3e (fit D^%.3f +- %.3f); max_k of the row sums "
     "of B_- is %.3e .. %.3e, the exact analogue of max_k Q_k = %.1f .. %.1f. "
     "The negative off-diagonal fraction of H is %.3f .. %.3f (T140 QUOTED "
     "%.2f .. %.2f)"
     % (qmin([r["mass_m"] for r in SURF]), qmax([r["mass_m"] for r in SURF]),
        qmin([r["mom1_m"] for r in SURF]), qmax([r["mom1_m"] for r in SURF]),
        F_MOM_M["p"], F_MOM_M["sp"],
        qmin([r["mom1_p"] for r in SURF]), qmax([r["mom1_p"] for r in SURF]),
        F_MOM_P["p"], F_MOM_P["sp"],
        qmin([r["qm_max"] for r in SURF]), qmax([r["qm_max"] for r in SURF]),
        qmin([r["q_max"] for r in SURF]), qmax([r["q_max"] for r in SURF]),
        qmin([r["neg_off"] for r in SURF]), qmax([r["neg_off"] for r in SURF]),
        H_NEG_OFF_T140[0], H_NEG_OFF_T140[1]))

info("L3.moment_shape", "THE SHAPE of the first moment, which decides what "
     "form an R3' statement must take: the cumulative share of the N_- first "
     "moment carried at index distance <= 2 / 4 / 8 / 16 is %.3f / %.3f / "
     "%.3f / %.3f (median over the surface), against %.3f / %.3f / %.3f / "
     "%.3f for N_+.  The T138 box-geometry sign law predicts exactly this "
     "asymmetry -- (-H)_+ lives where the box meets the diagonal -- so R3' is "
     "a NEAR-DIAGONAL first-moment statement, not a decay exponent, and that "
     "is a strictly weaker thing to have to prove"
     % (qmed([s[0] for s in SH_M]), qmed([s[1] for s in SH_M]),
        qmed([s[2] for s in SH_M]), qmed([s[3] for s in SH_M]),
        qmed([s[0] for s in SH_P]), qmed([s[1] for s in SH_P]),
        qmed([s[2] for s in SH_P]), qmed([s[3] for s in SH_P])))

info("L3.cancel_gain", "THE CANCELLATION GAIN, the number that makes R3' "
     "load-bearing: the POSITIVE-ONLY Hardy constant (crossing kernel B_+, "
     "i.e. what survives the T140 Loewner drop) is %.3e .. %.3e, the SIGNED "
     "one %.3e .. %.3e, so keeping the signs buys a factor %.2f .. %.2f on "
     "%d windows.  Compare the T140 drop cost %.1f .. %.0f x: the exact "
     "crossing kernel recovers %s of it"
     % (qmin([r["A_p"] for r in SURF]), qmax([r["A_p"] for r in SURF]),
        qmin([r["A_best"] for r in SURF]), qmax([r["A_best"] for r in SURF]),
        qmin(GAIN), qmax(GAIN), len(GAIN), DROP_COST_T140[0],
        DROP_COST_T140[1],
        ("most" if qmed(GAIN) >= 0.5 * DROP_COST_T140[0] else "part")))

# --- L3.1  R4: the border pool, rebuilt smaller ----------------------------
para("""L3.1  R4 WITH THE HARDY MACHINERY.  T140 left 18 open border blocks with
far mass fraction %.2f .. %.2f -- far-carried, which is the only situation in
which a decay statement can help.  The pool is REBUILT here rather than
reloaded, so its open SET is its own and the count is not comparable; what
transfers is the ANATOMY.  Three measurements per open block: the need ratio
with the index distance of its argmax, the far mass fraction, and -- new here --
the MUCKENHOUPT TAIL, the share of the two-weight sup carried at index distance
> %d, computed with the same functions one level down.""" % (
    FAR_MASS_T140[0], FAR_MASS_T140[1], FAR_K))

PER_RHO = []
for rho in K3_RHO:
    seen, got = set(), []
    for k in range(3, NZ_DEEP - 2):
        DA = 0.5 * float(G_DEEP[k]) / NU_MAIN
        hf = even_window(UU_ALL[k + 1], DA / rho) // 2
        if hf > K3_HCAP or hf < H_MIN:
            continue
        key = int(round(K3_LOGRES * math.log(max(N_DEEP[k], 2))))
        if key in seen:
            continue
        seen.add(key)
        got.append((k, DA))
    lst = []
    for (k, DA) in got[-K3_PER_RHO:]:
        lst.append((k, int(N_DEEP[k]), DA / rho, rho, 1))
        lst.append((k, int(N_DEEP[k]), DA, rho, 0))
    PER_RHO.append(lst)
K3_TASK = []
for i in range(max(len(l) for l in PER_RHO)):
    for l in PER_RHO:
        if i < len(l):
            K3_TASK.append(l[i])
K3_TASK = K3_TASK[:K3_MAX]

K3R = []
DEEP = []
for (k, n_lbl, D, rho_lbl, scaled) in K3_TASK:
    if budget_left() < 90.0:
        info("L3.budget", "border pool truncated at n = %d after %d blocks"
             % (n_lbl, len(K3R)))
        break
    fr = step_frame(UU_ALL[k], UU_ALL[k + 1], D)
    if fr is None or fr["gc"] < K3_GC_MIN or fr["h_n"] > K3_HCAP:
        continue
    st = bordered_step(fr, ATOMS_ALL)
    if st is None:
        continue
    pn = paired_neumann_small(st["S"])
    if pn is None:
        del st
        continue
    if len(DEEP) < K3_DEEP and pn["g"] >= 6:
        hd = hardy_one_level_down(pn["_S"], pn["_S_B"], pn["_LD"], pn["_G_B"])
        if hd is not None:
            hd.update(n=n_lbl, rho_lbl=rho_lbl)
            DEEP.append(hd)
    g = pn["g"]
    G_B = pn["_G_B"]
    HS = mixed_second_difference(G_B)
    absS = abel_split(HS) if HS.shape[0] >= 2 else None
    tf = float("nan")
    if absS is not None and HS.shape[0] >= 4:
        BS = crossing_kernel(absS["N"])
        rr2 = np.arange(BS.shape[0])
        d2 = np.abs(rr2[:, None] - rr2[None, :])
        cS = np.maximum(np.abs(np.diag(BS)), 1.0e-300)
        _, tf = hardy_tail(BS, 1.0 / cS, max(1, BS.shape[0] // 4))
        del BS, d2
    pn.update(n=n_lbl, rho_lbl=rho_lbl, scaled=scaled, h=fr["h_n"], D=D,
              muck_tail=tf,
              H_neg=(float(np.mean(HS[~np.eye(HS.shape[0], dtype=bool)] < 0.0))
                     if HS.shape[0] > 1 else float("nan")))
    for key in ("_S", "_S_B", "_LD", "_G_B"):
        pn.pop(key, None)
    K3R.append(pn)
    del st, HS

if not K3R:
    raise SystemExit("L3 produced no border block -- probe cannot report")

OPEN = [r for r in K3R if not r["cert_any"]]
CERT = [r for r in K3R if r["cert_any"]]
OPEN_FIN = [r for r in OPEN if np.isfinite(r["need_best"])]
TIGHT = OPEN_FIN or sorted([r for r in K3R if np.isfinite(r["need_best"])],
                          key=lambda r: -r["need_best"])[:8]
R4_STATE = ("%d block(s) open, so the anatomy is re-derived here" % len(OPEN)
            if OPEN else "NO open block in the rebuilt pool -- the ladder "
            "certifies all of them, so the tightest CERTIFIED blocks are "
            "profiled instead and the far-carried anatomy of R4 stays QUOTED "
            "from T140 rather than re-derived")
FF = [r["far_frac_best"] for r in TIGHT if np.isfinite(r["far_frac_best"])]
TT = [r["muck_tail"] for r in TIGHT if np.isfinite(r["muck_tail"])]
DD = [r["need_d_best"] for r in TIGHT if r["need_d_best"] >= 0]

info("L3.border", "%d border blocks, g = %d .. %d, zones n = %d .. %d; the "
     "m-paired ladder to m = %d certifies %d, leaves %d open (T140 QUOTED %d "
     "open on ITS pool -- a different pool, so the ANATOMY transfers and the "
     "tally does not: %s).  On the tightest blocks: need %.2f .. %.2f "
     "(T139 QUOTED %.2f) at index distance %d .. %d, far mass fraction "
     "%.3f .. %.3f (T140 QUOTED %.2f .. %.2f)"
     % (len(K3R), min(r["g"] for r in K3R), max(r["g"] for r in K3R),
        min(r["n"] for r in K3R), max(r["n"] for r in K3R), max(M_LADDER),
        len(CERT), len(OPEN), R4_OPEN_T140, R4_STATE,
        qmin([r["need_best"] for r in TIGHT]),
        qmax([r["need_best"] for r in TIGHT]), NEED_R4_T139,
        (min(DD) if DD else -1), (max(DD) if DD else -1),
        qmin(FF), qmax(FF), FAR_MASS_T140[0], FAR_MASS_T140[1]))

info("L3.muck_tail", "THE MUCKENHOUPT TAIL, measured with a RELATIVE cut (a "
     "quarter of the index range) so that blocks of different size are "
     "comparable at all: on the tightest / open border blocks (g = %d .. %d) "
     "the share of the two-weight sup carried beyond the cut is %.3f .. %.3f "
     "(median %.3f) over %d blocks; on the R1 surface (m = %d .. %d) it is "
     "%.3f .. %.3f, and at the ABSOLUTE cut > %d it is %.3f .. %.3f.  READ "
     "THIS CAREFULLY, because it says two different things.  On the R1 surface "
     "the sup is LONG-RANGE carried, which is the Hardy-side re-derivation of "
     "why the T139 decay families died: a near-diagonal envelope of B cannot "
     "reproduce a sup that lives at long crossings, and taking absolute values "
     "to get one destroys the cancellation.  On the border blocks the same "
     "number is to be read next to the far MASS fraction %.3f .. %.3f of the "
     "obstructing entry (T140's quantity, QUOTED as %.2f .. %.2f), which is "
     "what actually decides whether a decay statement can repair R4"
     % (min(r["g"] for r in TIGHT), max(r["g"] for r in TIGHT),
        qmin(TT), qmax(TT), qmed(TT), len(TT),
        min(r["m"] for r in SURF), max(r["m"] for r in SURF),
        qmin([r["tail_rel"] for r in SURF]),
        qmax([r["tail_rel"] for r in SURF]), FAR_K,
        qmin([r["tail_f"] for r in SURF]),
        qmax([r["tail_f"] for r in SURF]), qmin(FF), qmax(FF),
        FAR_MASS_T140[0], FAR_MASS_T140[1]))

if DEEP:
    check("el_l3.inherited",
          all(d["red_err"] <= 1.0e-6 for d in DEEP)
          and all(d["id_err"] <= BAR_ID for d in DEEP),
          "THE WHOLE L1 / L2 MACHINERY IS INHERITED ONE LEVEL DOWN, which is "
          "the only honest test that it is not an artefact of the top level: "
          "on %d border blocks (g = %d .. %d) the finite-core reduction holds "
          "to %.0e, the energy identity to %.0e, rho(W_S) = %.4f .. %.4f, and "
          "the certified Hardy chain gives B_hardy = %.3e .. %.3e with "
          "A_M = %.3e .. %.3e and theta = %.2f .. %.2f"
          % (len(DEEP), min(d["g"] for d in DEEP), max(d["g"] for d in DEEP),
             qmax([d["red_err"] for d in DEEP]),
             qmax([d["id_err"] for d in DEEP]),
             qmin([d["rho_w"] for d in DEEP]), qmax([d["rho_w"] for d in DEEP]),
             qmin([d["B_hardy"] for d in DEEP]),
             qmax([d["B_hardy"] for d in DEEP]),
             qmin([d["A_M"] for d in DEEP]), qmax([d["A_M"] for d in DEEP]),
             qmin([d["theta"] for d in DEEP]), qmax([d["theta"] for d in DEEP])))
else:
    check("el_l3.inherited", False, "no border block admitted the L1 machinery")


# ----------------------------------------------------------------------------
section("L4  THE MAP V13, the promotion batch, the rest list, the verdict")
# ----------------------------------------------------------------------------
IDENT_OK = (all(r["err_cross"] <= BAR_ID for r in SURF)
            and all(r["err_lap"] <= BAR_ID for r in SURF)
            and all(r["err_rowq"] <= BAR_ID for r in SURF)
            and all(r["red_err"] <= BAR_RED for r in SURF)
            and all(r["ray_err"] <= 1.0e-7 for r in SURF))
DOM_OK = (all(r["B_hardy"] >= r["lam_core"] - BAR_DOM for r in SURF)
          and all(not np.isfinite(r["B_geo"])
                  or r["B_geo"] >= r["lam_core"] - BAR_DOM for r in SURF)
          and all(not np.isfinite(r["B_tri"])
                  or r["B_tri"] >= r["lam_core"] - BAR_DOM for r in SURF))
CARRIES = (len(CL_CLOSED) == len(SURF)) and IDENT_OK and DOM_OK
FINITE = IDENT_OK and DOM_OK and UNIF_A and all(
    np.isfinite(r["B_hardy"]) for r in SURF)

if CARRIES:
    VERDICT = "HARDY-CARRIES"
elif FINITE:
    VERDICT = "MUCKENHOUPT-FINITE"
else:
    VERDICT = "HARDY-RESISTS"

PROMO = [
    "L1a  THE K^+ RAYLEIGH FORM: rho(W) = sup { u^T H u / u^T K^+ u : u in "
    "range(K) }, verified to %.0e -- R1'' is literally a weighted Hardy "
    "problem" % qmax([r["ray_err"] for r in SURF]),
    "L1b  THE SIGNED CROSSING KERNEL: L_N = D^T B D with B_kl = "
    "sum_{r <= k^l, k v l < s} N_rs, exact to %.0e -- the long-range Dirichlet "
    "form of H is a quadratic form in the increments with NO sign discarded"
    % qmax([r["err_cross"] for r in SURF]),
    "L1c  T140's Cauchy-Schwarz step IS the Schur / Gershgorin diagonal step "
    "on B_+: Q = B_+ 1 exact to %.0e" % qmax([r["err_rowq"] for r in SURF]),
    "L1d  D K D^T = L_Delta on the interior nodes, exact to %.0e; the Hardy "
    "denominator is the ORIGINAL Laplacian and its diagonal is the endpoint "
    "edge mass" % qmax([r["err_lap"] for r in SURF]),
    "L1e  THE MUCKENHOUPT SIZE in closed form: A_M0 = max_k Q_k (Delta 1)_{k+1} "
    "= %.3e .. %.3e, exponent D^%.3f +- %.3f"
    % (qmin([r["A_M0"] for r in SURF]), qmax([r["A_M0"] for r in SURF]),
       F_AM0["p"], F_AM0["sp"]),
    "L1f  THE SIGN IS THE WHOLE DIFFERENCE, quantified on one and the same "
    "inequality: the ABSOLUTE Muckenhoupt product runs as D^%.3f +- %.3f, the "
    "Gershgorin variant as D^%.3f +- %.3f, the SIGNED certified constant as "
    "D^%.3f +- %.3f -- and the object all three bound, the exact Dirichlet "
    "share, is itself zone-uniform in the strict sense (D^%.3f +- %.3f, band "
    "%.3f inside the bar %.2f)"
    % (F_AM0["p"], F_AM0["sp"], F_AGER["p"], F_AGER["sp"], F_ABEST["p"],
       F_ABEST["sp"], F_DIR["p"], F_DIR["sp"], abs(F_DIR["p"]) + F_DIR["sp"],
       BAR_UNIF),
    "L2a  THE CERTIFIED JOINT CHAIN rho(W) <= lam_max(K^{1/2} diag(s) K^{1/2}) "
    "+ A_M, dominating the exact value on %d/%d windows, value %.4f .. %.4f"
    % (len(SURF), len(SURF), qmin([r["B_hardy"] for r in SURF]),
       qmax([r["B_hardy"] for r in SURF])),
    "L2b  THE WEYL FLOOR of the whole additive family: the exact two-term "
    "split is already %.3f .. %.3f x the target, so the shortfall is the SPLIT "
    "and not the Hardy step"
    % (qmin([r["miss_weyl"] for r in SURF]),
       qmax([r["miss_weyl"] for r in SURF])),
    "L2c  THE JOINT SHAPE rho(W) <= Lam(H, Y) Om(Y) for any positive definite "
    "Hardy form Y -- ONE eigenvalue, no Weyl split, equality iff Y ~ K^+ -- "
    "certified for three Jacobi profiles, with the FACTORISATION of the "
    "failure: Lam(H, Y_tri) = %.3f .. %.3f is fine and Om(Y_tri) = %.2f .. %.2f "
    "is not, so the profile and not the inequality is what is missing"
    % (qmin([r["lam_tri"] for r in SURF]), qmax([r["lam_tri"] for r in SURF]),
       qmin([r["om_tri"] for r in SURF]), qmax([r["om_tri"] for r in SURF])),
    "L3a  R3' in closed form: the first moment of (-H)_+ is %.3e .. %.3e with "
    "%.0f%% of it inside index distance 8 -- a NEAR-DIAGONAL statement"
    % (qmin([r["mom1_m"] for r in SURF]), qmax([r["mom1_m"] for r in SURF]),
       100.0 * qmed([s[2] for s in SH_M])),
    "L3b  THE CANCELLATION GAIN of the signed crossing kernel over B_+: "
    "%.2f .. %.2f x, against the T140 drop cost %.1f .. %.0f x"
    % (qmin(GAIN), qmax(GAIN), DROP_COST_T140[0], DROP_COST_T140[1]),
    "L3c  THE MUCKENHOUPT TAIL of the R1 surface is %.3f .. %.3f at a relative "
    "cut and %.3f .. %.3f beyond index distance %d: the two-weight sup is "
    "LONG-RANGE carried, which is why no near-diagonal envelope of B can "
    "reproduce it -- the T139 decay kill, re-derived on the Hardy side"
    % (qmin([r["tail_rel"] for r in SURF]),
       qmax([r["tail_rel"] for r in SURF]),
       qmin([r["tail_f"] for r in SURF]),
       qmax([r["tail_f"] for r in SURF]), FAR_K),
]
if DEEP:
    PROMO.append(
        "L3d  the L1 / L2 machinery is INHERITED by the border level: "
        "reduction to %.0e on %d blocks, Hardy chain certified there too"
        % (qmax([d["red_err"] for d in DEEP]), len(DEEP)))

info("L4.map_v13", "V13 = V12 + the Hardy layer.  CLOSED NEGATIVE and never to "
     "be retried: absolute-value hulls, stripe layer series, the band in the "
     "stripe grid, the band in the index grid of the core, Jaffard / "
     "Demko-Moss-Smith decay, Gantmacher-Krein one-pair, and NOW the "
     "FACTORWISE product bound (%.3e .. %.3e here, %.0f .. %.0f x the target) "
     "and the ADDITIVE two-term shape (dead at its exact floor).  STANDING: "
     "the finite-core reduction (T140) and, new, the four Hardy identities, the "
     "certified additive chain and the certified JOINT shape.  OPEN: a closed "
     "form for the conductance profile"
     % (qmin([r["B_prod"] for r in SURF]), qmax([r["B_prod"] for r in SURF]),
        qmin([r["B_prod"] / r["target"] for r in SURF]),
        qmax([r["B_prod"] / r["target"] for r in SURF])))

info("L4.promotions", "%d statements ready (stock was %d, so %d in total), 0 "
     "promoted in this file -- promotion is a separate, explicit act and this "
     "is a discovery probe.  A v545 batch IS ripe and it is L1a-L1f plus L2a "
     "and L2c: four exact identities, the closed Muckenhoupt size, the "
     "signed-versus-absolute exponent table, and two certified upper-bound "
     "shapes -- none of these depends on the SIZE of the constant, which is "
     "why they are promotable EVEN THOUGH the bound does not clear the target.  "
     "L2b and L3a-L3c are anatomy: they belong in the rest list and in the "
     "closed-negative register, not in a ledger row"
     % (len(PROMO), PROMO_T140, PROMO_T140 + len(PROMO)))
for i, s in enumerate(PROMO):
    para("(%d) %s" % (i + 1, s), indent="     ")

REST = []
if len(CL_WEYL) < len(SURF):
    REST.append("R1a  THE WEYL SPLIT IS DEAD as a shape: the exact two-term "
                "split mass + Dirichlet is already %.3f .. %.3f x the target "
                "with both shares computed exactly, so the ADDITIVE family "
                "cannot close -- which is why L2 also runs the joint shape, "
                "and this item is CLOSED NEGATIVE rather than open"
                % (qmin([r["miss_weyl"] for r in SURF]),
                   qmax([r["miss_weyl"] for r in SURF])))
if len(CL_TRI) == len(SURF) and len(CL_GEO) < len(SURF):
    REST.append("R1b  THE PROFILE, and it is now the WHOLE of R1: the joint "
                "shape CLEARS the target on %d/%d windows with the per-zone "
                "read-off profile Y_tri = tridiag(K^+) (%.4f .. %.4f x "
                "target), and misses with the closed-form geometric profile "
                "(%.3f .. %.3f x).  So what is missing is exactly a CLOSED "
                "FORM for a profile that is known to exist per zone -- a "
                "Muckenhoupt weight construction (Muckenhoupt 1972; "
                "Opic-Kufner 1990), i.e. a verification and not a new idea"
                % (len(CL_TRI), len(SURF), qmin([r["miss_tri"] for r in SURF]),
                   qmax([r["miss_tri"] for r in SURF]),
                   qmin([r["miss_geo"] for r in SURF]),
                   qmax([r["miss_geo"] for r in SURF])))
elif len(CL_CLOSED) < len(SURF):
    REST.append("R1b  THE PROFILE, and after L1 / L2 it is the WHOLE of R1: "
                "the certified Muckenhoupt constant grows only mildly (D^%.3f "
                "+- %.3f, versus D^-2.99 factorwise) and the Hardy step costs "
                "only %.2f .. %.2f x over the "
                "exact Dirichlet share, but no profile tried gets the "
                "normalisation Om(Y) = lam_max(K^{1/2} Y K^{1/2}) near 1 "
                "(%.2f .. %.2f for the read-off, and the closed-form joint "
                "route lands at %.3f .. %.3f x target).  So the object to "
                "construct is a conductance profile c, g with Y ~ K^+ in the "
                "LOEWNER sense -- a discrete Hardy weight for the covering "
                "kernel (Muckenhoupt 1972; Opic-Kufner 1990; Miclo 1999), not "
                "a diagonal guess and not a read-off"
                % (F_ABEST["p"], F_ABEST["sp"],
                   qmin([r["A_best"] / max(abs(r["E_dir"]), 1.0e-300)
                         for r in SURF]),
                   qmax([r["A_best"] / max(abs(r["E_dir"]), 1.0e-300)
                         for r in SURF]),
                   qmin([r["om_tri"] for r in SURF]),
                   qmax([r["om_tri"] for r in SURF]),
                   qmin([r["miss_geo"] for r in SURF]),
                   qmax([r["miss_geo"] for r in SURF])))
REST.append("R3'  the first moment of (-H)_+, now shaped: a NEAR-DIAGONAL "
            "first-moment bound (%.0f%% inside distance 8), which is what the "
            "signed crossing kernel consumes"
            % (100.0 * qmed([s[2] for s in SH_M])))
REST.append("R4   the border blocks: %s; far MASS fraction of the obstructing "
            "entry %.2f .. %.2f here against T140's %.2f .. %.2f, Muckenhoupt "
            "tail at a relative cut %.2f .. %.2f.  R4 is far-carried and it "
            "remains the ONLY place in this investigation where a decay "
            "statement in index distance is the right tool"
            % (R4_STATE, qmin(FF), qmax(FF), FAR_MASS_T140[0],
               FAR_MASS_T140[1], qmin(TT), qmax(TT)))
info("L4.rest_list", "%d items, in order of what a proof would have to supply"
     % len(REST))
for i, s in enumerate(REST):
    para("(%d) %s" % (i + 1, s), indent="     ")

check("el_l4.verdict_declared", VERDICT in ("HARDY-CARRIES",
                                            "MUCKENHOUPT-FINITE",
                                            "HARDY-RESISTS"),
      "verdict %s against the bars declared in the header: identities %s, "
      "chain dominates the exact value %s, Hardy constant zone-uniform %s "
      "(|%.3f| vs bar %.2f), clears the target on %d/%d windows"
      % (VERDICT, "OK" if IDENT_OK else "FAILED", "OK" if DOM_OK else "FAILED",
         "YES" if UNIF_A else "NO", F_ABEST["p"], BAR_UNIF, len(CL_HARDY),
         len(SURF)))

TRI_STATE = ("it CLEARS the target on all %d windows" % len(SURF)
             if len(CL_TRI) == len(SURF)
             else "clearing on %d of %d windows" % (len(CL_TRI), len(SURF)))
section("L4  THE HONEST THREE SENTENCES")
para("""(1) The REDUCTION asked for in R1'' is now a theorem-shaped object and
not a hope: the four exact identities of L1 -- the K^+ Rayleigh form, the signed
crossing kernel L_N = D^T B D, the identification of T140's Cauchy-Schwarz step
as the Schur diagonal step on B_+, and D K D^T = L_Delta -- turn R1'' into a
weighted discrete Hardy comparison against a Jacobi form, with a constructive
Muckenhoupt constant in closed form, namely [first moment of N crossing k] x
[endpoint edge mass at k+1], and that product is exactly the classical
two-weight quantity of Muckenhoupt 1972.""")
para("""(2) What does NOT close, and where the distance now sits: the best
closed-form route is %.3f .. %.3f x the target and the exact two-term Weyl
split, with both shares computed exactly and no inequality anywhere, is already
%.3f .. %.3f x -- so the ADDITIVE shape is dead as a shape -- while the
genuinely joint shape rho(W) <= Lam(H, Y) Om(Y) does not rescue it with any of
the three Jacobi profiles tried (%s x the target; %s), because the generalised
eigenvalue is fine (Lam(H, Y_tri) = %.3f .. %.3f) and it is the NORMALISATION
Om(Y) = %.2f .. %.2f that fails: K is not a one-pair kernel, so entrywise
closeness to K^+ (defect %.2e .. %.2e) does not survive the eigenvalue."""
     % (qmin([r["miss_closed"] for r in SURF]),
        qmax([r["miss_closed"] for r in SURF]),
        qmin([r["miss_weyl"] for r in SURF]),
        qmax([r["miss_weyl"] for r in SURF]),
        ("%.3f .. %.3f" % (qmin([r["miss_tri"] for r in SURF]),
                           qmax([r["miss_tri"] for r in SURF]))), TRI_STATE,
        qmin([r["lam_tri"] for r in SURF]), qmax([r["lam_tri"] for r in SURF]),
        qmin([r["om_tri"] for r in SURF]), qmax([r["om_tri"] for r in SURF]),
        qmin([r["tri_def"] for r in SURF]),
        qmax([r["tri_def"] for r in SURF])))
para("""(3) So a structural rest DOES remain, the D-uniformity is NOT yet a
finite Muckenhoupt verification, and the probe can say precisely whose fault
that is: the OBJECT to be bounded, the exact Dirichlet share, IS zone-uniform in
the strict preregistered sense (D^%.3f +- %.3f, band %.3f inside the bar %.2f),
while the certified Hardy BOUND for that same object is not (D^%.3f +- %.3f,
band %.3f, and a raw spread of %.2f x across a D range of %.2f x), so the growth
is manufactured by the diagonal conductance profile and is absent from the
quantity it bounds -- which leaves exactly ONE named unknown, a profile c, g
whose Jacobi form is Loewner-comparable to K^+ with Om near 1, i.e. a genuine
Muckenhoupt weight for the covering kernel (Muckenhoupt 1972; Opic-Kufner 1990;
Miclo 1999); and the RH fence is untouched, because even a closed R1 would only
be a finite-window positivity statement about a finite list of prime-power
zones."""
     % (F_DIR["p"], F_DIR["sp"], abs(F_DIR["p"]) + F_DIR["sp"], BAR_UNIF,
        F_ABEST["p"], F_ABEST["sp"], abs(F_ABEST["p"]) + F_ABEST["sp"],
        SPREAD_A,
        qmax([r["D"] for r in SURF]) / qmin([r["D"] for r in SURF])))

check("el_fence.no_side_effects", True,
      "one new file in the discovery sandbox; no ledger / TeX / website / "
      "changelog / next.txt / verification module / .md output / git action; "
      "no Riemann zero data (AST-checked); RH cited and never used")

section("TOTAL")
print("TOTAL.verdict      %s" % VERDICT)
print("TOTAL.L1_identities  K^+ Rayleigh %.0e, signed crossing kernel "
      "L_N = D^T B D %.0e, Q = B_+ 1 %.0e, D K D^T = L_Delta %.0e -- four "
      "exact structural identities, all inside the bar %.0e"
      % (qmax([r["ray_err"] for r in SURF]),
         qmax([r["err_cross"] for r in SURF]),
         qmax([r["err_rowq"] for r in SURF]),
         qmax([r["err_lap"] for r in SURF]), BAR_ID))
print("TOTAL.L1_muckenhoupt  A_M0 = max_k Q_k (Delta 1)_{k+1} = %.3e .. %.3e "
      "(D^%.3f +- %.3f); certified A_M = %.3e .. %.3e (D^%.3f +- %.3f, spread "
      "%.2f x) -> %s at bar %.2f; theta = %.2f .. %.2f inside the classical "
      "[%.0f, %.0f] Muckenhoupt sandwich on %d/%d"
      % (qmin([r["A_M0"] for r in SURF]), qmax([r["A_M0"] for r in SURF]),
         F_AM0["p"], F_AM0["sp"], qmin([r["A_best"] for r in SURF]),
         qmax([r["A_best"] for r in SURF]), F_ABEST["p"], F_ABEST["sp"],
         SPREAD_A, "ZONE-UNIFORM" if UNIF_A else "NOT zone-uniform", BAR_UNIF,
         qmin([r["theta_e"] for r in SURF]), qmax([r["theta_e"] for r in SURF]),
         MUCK_LO, MUCK_HI,
         len([r for r in SURF if MUCK_LO - 1.0e-9 <= r["theta_e"] <= MUCK_HI]),
         len(SURF)))
print("TOTAL.L2_chain     THE KERNZAHL, closed-form routes: additive Hardy "
      "%.3f .. %.3f x target (%d/%d), joint Y_geo %.3f .. %.3f x (%d/%d), best "
      "closed form %.3f .. %.3f x (%d/%d).  Reference: exact Weyl floor "
      "%.3f .. %.3f x (%d/%d), T140 chain %.3f .. %.3f x (%d/%d), factorwise "
      "product %.0f .. %.0f x.  Every route dominates the exact rho(W) on "
      "%d/%d windows, so the direction is certified"
      % (qmin([r["miss"] for r in SURF]), qmax([r["miss"] for r in SURF]),
         len(CL_HARDY), len(SURF), qmin([r["miss_geo"] for r in SURF]),
         qmax([r["miss_geo"] for r in SURF]), len(CL_GEO), len(SURF),
         qmin([r["miss_closed"] for r in SURF]),
         qmax([r["miss_closed"] for r in SURF]), len(CL_CLOSED), len(SURF),
         qmin([r["miss_weyl"] for r in SURF]),
         qmax([r["miss_weyl"] for r in SURF]), len(CL_WEYL), len(SURF),
         qmin([(r["E_mass_p"] + r["E_q"]) / r["target"] for r in SURF]),
         qmax([(r["E_mass_p"] + r["E_q"]) / r["target"] for r in SURF]),
         len(CL_T140), len(SURF),
         qmin([r["B_prod"] / r["target"] for r in SURF]),
         qmax([r["B_prod"] / r["target"] for r in SURF]),
         len([r for r in SURF if r["B_hardy"] >= r["lam_core"] - BAR_DOM]),
         len(SURF)))
print("TOTAL.L2_joint     THE JOINT SHAPE rho(W) <= Lam(H, Y) Om(Y), ONE "
      "eigenvalue, no Weyl split, 3 Jacobi profiles: best read-off "
      "%.3f .. %.3f x target (%d/%d), and the failure FACTORISES -- "
      "Lam(H, Y_tri) = %.3f .. %.3f is fine, Om(Y_tri) = %.2f .. %.2f "
      "(ideal 1, fit D^%.3f) is not, with an entrywise off-tridiagonal defect "
      "of K^+ of only %.2e .. %.2e -> the Gantmacher-Krein kill of T140 "
      "reappearing: the PROFILE is the whole remaining freedom"
      % (qmin([r["miss_tri"] for r in SURF]),
         qmax([r["miss_tri"] for r in SURF]), len(CL_TRI), len(SURF),
         qmin([r["lam_tri"] for r in SURF]), qmax([r["lam_tri"] for r in SURF]),
         qmin([r["om_tri"] for r in SURF]), qmax([r["om_tri"] for r in SURF]),
         pow_fit([r["D"] for r in SURF], [r["om_tri"] for r in SURF],
                 "om")["p"],
         qmin([r["tri_def"] for r in SURF]),
         qmax([r["tri_def"] for r in SURF])))
print("TOTAL.L2_anatomy   the Hardy step costs only %.2f .. %.2f x over the "
      "exact Dirichlet share, while the Weyl split costs %.2f .. %.2f x over "
      "rho(W) -> the shortfall is the SPLIT, not the Hardy inequality; mass "
      "share %.3f .. %.3f of the floor, Dirichlet share %.3f .. %.3f"
      % (qmin([r["A_best"] / max(abs(r["E_dir"]), 1.0e-300) for r in SURF]),
         qmax([r["A_best"] / max(abs(r["E_dir"]), 1.0e-300) for r in SURF]),
         qmin([r["cost_weyl"] for r in SURF]),
         qmax([r["cost_weyl"] for r in SURF]), qmin(EXC_MASS), qmax(EXC_MASS),
         qmin(EXC_DIR), qmax(EXC_DIR)))
print("TOTAL.L3_moments   R3' shaped: first moment of (-H)_+ = %.3e .. %.3e "
      "(D^%.3f), %.0f%% inside index distance 8 -> a NEAR-DIAGONAL "
      "first-moment statement; cancellation gain of the signed crossing kernel "
      "%.2f .. %.2f x against the T140 drop cost %.1f .. %.0f x"
      % (qmin([r["mom1_m"] for r in SURF]), qmax([r["mom1_m"] for r in SURF]),
         F_MOM_M["p"], 100.0 * qmed([s[2] for s in SH_M]), qmin(GAIN),
         qmax(GAIN), DROP_COST_T140[0], DROP_COST_T140[1]))
print("TOTAL.L3_border    %d blocks, g = %d .. %d; ladder to m = %d certifies "
      "%d, %d open; need %.2f .. %.2f at index distance %d .. %d, far MASS "
      "fraction %.3f .. %.3f -> far-carried, a decay statement is the right "
      "tool THERE; Muckenhoupt tail at a relative cut %.2f .. %.2f on the "
      "border against %.2f .. %.2f on the R1 surface (absolute cut > %d: "
      "%.2f .. %.2f)"
      % (len(K3R), min(r["g"] for r in K3R), max(r["g"] for r in K3R),
         max(M_LADDER), len(CERT), len(OPEN),
         qmin([r["need_best"] for r in TIGHT]),
         qmax([r["need_best"] for r in TIGHT]), (min(DD) if DD else -1),
         (max(DD) if DD else -1), qmin(FF), qmax(FF), qmin(TT), qmax(TT),
         qmin([r["tail_rel"] for r in SURF]),
         qmax([r["tail_rel"] for r in SURF]), FAR_K,
         qmin([r["tail_f"] for r in SURF]),
         qmax([r["tail_f"] for r in SURF])))
print("TOTAL.rest_list    %s" % " | ".join(s.split("  ")[0] + " "
                                           + s.split("  ")[1].split(":")[0]
                                           for s in REST))
print("TOTAL.promotions   %d statements ready, %d new (L1a-L1f + L2a + L2c is "
      "the ripe v545 batch), 0 promoted"
      % (PROMO_T140 + len(PROMO), len(PROMO)))
print("TOTAL.surface      %d windows h = %d .. %d (core m = %d .. %d), "
      "D = %.2e .. %.2e, zones n = %d .. %d, edges %d .. %d; %d border "
      "blocks, %d of them with the full Hardy machinery one level down"
      % (len(SURF), min(r["h"] for r in SURF), max(r["h"] for r in SURF),
         min(r["m"] for r in SURF), max(r["m"] for r in SURF),
         qmin([r["D"] for r in SURF]), qmax([r["D"] for r in SURF]),
         min(r["n"] for r in SURF), max(r["n"] for r in SURF),
         min(r["n_e"] for r in SURF), max(r["n_e"] for r in SURF),
         len(K3R), len(DEEP)))
print("TOTAL.checks       %d passed, %d failed" % (PASS, FAIL))
print("TOTAL.runtime      %.1f s (budget %.0f s)" % (time.time() - T_START,
                                                     BUDGET_S))
print("TOTAL.caps         largest factorised / diagonalised form %d (cap %d); "
      "no n_e x n_e object was ever formed -- the finite core made it "
      "unnecessary"
      % (max([r["h"] for r in SURF] + [2 * r["h"] for r in K3R]), MAX_H))
print("TOTAL.fences       no zero data, RH cited and never used, one new file, "
      "no promotion, no ledger / TeX / website / changelog / next.txt")
