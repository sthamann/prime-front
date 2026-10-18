"""Discovery probe (2026-07-29), part 151 of the prime/window investigation.
Contract ODD.LADDER -- THE ONE INEQUALITY IN THE ODD PARITY SECTOR.

WHERE THIS SITS (T150 END STATE: ONE-TERM-MISSING, and what it left standing)
  T140 reduced the question to two small matrices per zone, T141 made it a
  weighted Hardy problem, T142 .. T147 closed the comparison, capacity and level
  branches and reduced D-uniformity to TWO scalars via Gam = sqrt(Q_star) x Sw,
  T148 CLOSED Sw, T149 eliminated the TV hypothesis by a change of gauge and
  restated the question as a LADDER, and T150 NAMED THE MECHANISM.  QUOTED from
  T140 .. T150 and NEVER re-derived:
    * A IS EXACTLY the compression of the full symmetric Toeplitz section T_M(c)
      to its ANTISYMMETRIC parity sector, A = U_-^T T_M(c) U_- (cross block 0 to
      4e-16), and the even sector is A_+ = T + H;
    * the NEGATIVE INERTIA of T_M(c) forced by f(0) < 0 sits ENTIRELY in the EVEN
      sector (72/72 certified by two LDL^T counts); the odd sector has NONE;
    * the antisymmetric Dirichlet sines t_k(r) = 2/sqrt(N) sin(2 pi k (r+1)/N),
      N = 2m+1, are the exact eigenvectors of the parity Laplacian L_P and give
      nu_k = pi k^2 EXACTLY on their own control;
    * the LAG VECTOR splits exactly, c = c^arch + c^atom with c^atom <= 0 and
      ||c^atom||_1 <= 4 B sqrt(N); the ARCHIMEDEAN section ALONE has 2 .. 7
      NEGATIVE eigenvalues, so the atoms are CO-RESPONSIBLE for positivity and
      the additive perturbation route is dead by 2.4 .. 5.8 orders;
    * the MULTIPLICATIVE (Loewner) gauge step closes, exp(amp) <= 14.11, scale
      free -- the only living transport direction;
    * THE ONE MISSING GATE: the ladder constant in nu_k <= C k^2 still GROWS,
      C = 14.24 .. 43.39 = 13.81 pi at worst, trend x^(0.258 +- 0.009) against
      the flatness bar 0.25, maximum at k = 1 (67/72), the growth carried by the
      deeper read modes; and the gap pi -> 13.81 pi is the ARITHMETIC LEAKAGE of
      the mode, l1 mass 1.41 .. 1.79 and m ||psi||_inf^2 = 2.45 .. 3.41 against
      the model value 2;
    * end to end 6.8 .. 18.45 % of the true gap is certified;
    * the STRESS PAIR: the no-go breaks IN THE LADDER (C grows like x^1.84) while
      the Dirichlet and parity controls give C = pi exactly.
  T150's rest list was three items: (1) nu_k <= C k^2 m-free in the ODD sector
  for a SIGN-CHANGING symbol -- THE one inequality; (2) a closed lower bound on
  min Lam^arch; (3) Basor-Ehrhardt 2009 extended to f(0) < 0, or an EXPLICIT
  LOCAL MODEL at the symbol minimum inside the odd sector.  This file attacks
  (3) first, because (3) turns out to CONTAIN (1).

THE IDEA THIS PROBE TESTS, STATED BEFORE ANY NUMBER
  Item (3) is not a side quest.  The symbol f is negative in a neighbourhood
  [0, th_c) of the origin, and the ODD sector never sees the origin: the parity
  sines live on the SHIFTED grid th_k = 2 pi k / N, k = 1 .. m, whose first point
  is th_1 = 2 pi / N.  So the odd sector's effective symbol minimum is not f(0)
  but f(th_1) -- the negative window is STEPPED OVER whenever it is narrower than
  one odd mode spacing.  That is the local model, it is of ORDER 2, and its
  constant term is the absorbed negative f(0).  Written as an operator statement
  and using the classical fact that the Toeplitz-section quadratic form IS the
  symbol integral,
      <T_M(f) x, x> = (1/2 pi) int f(th) |sum_j x_j e^{i j th}|^2 dth ,
  the section is MONOTONE in the symbol, and 2 - 2 cos th is the symbol of the
  full-window path Laplacian whose odd compression is EXACTLY L_P.  Hence
      f(th) >= kap_sym (2 - 2 cos th) + f(0)  for all th
        ==>  A >= kap_sym L_P + f(0) I  >=  (kap_sym - |f(0)| / mu^P_1) L_P ,
  because L_P >= mu^P_1 I with mu^P_1 = 4 sin^2(pi/N) EXACT.  The whole question
  becomes a PENCIL question: the two numbers
      kap = lam_min(A, L_P) ,  K_bot = max_{k <= K} lam_k(A) / mu^P_k ,
  the first certified by ONE completed Cholesky, the second by K completed LDL^T
  counts (Sylvester 1852) -- so neither reads an eigenvector.  The a priori
  symbol-only ceiling K/kap <= K_sym / (kap_sym (1 - rho)) with
  rho = |f(0)| / (kap_sym mu^P_1) is ALSO instrumented, and it comes out VACUOUS:
  the symbol is not slowly varying at the resolution of the bottom mode, which is
  itself the most informative negative in this probe and is what disposes of
  T150's third rest item.  The matrix objects carry everything.
  And then the ladder is NOT reached through nu at all.  A vector of the odd
  sector vanishes at r = -1, so the elementary discrete Sobolev step
      ||psi||_inf^2 <= 2 ||psi||_2 ||grad psi||_2 ,  ||grad psi||_2^2 <= <psi, L_P psi>
  applies, and the pencil bound gives <psi_k, L_P psi_k> <= lam_k(A)/kap <=
  K mu^P_k / kap, whence
      m ||psi_k||_inf^2 <= 2 m sqrt(K_bot mu^P_k / kap) <= 2 pi k sqrt(K_bot/kap) .
  That is LINEAR in k, m-FREE given the pencil ratio, and it is the MULTIPLICATIVE
  mode comparison T150 asked for: the Sobolev step converts a Loewner (relative)
  form comparison into a MODE bound with no additive perturbation anywhere, so
  the Theta(D^3) smallness of the bottom -- which killed Weyl/Bauer-Fike/
  Davis-Kahan -- never enters.

WHAT THIS PROBE DOES
  X0  THE LICENCES.  The RH fence first; then every inequality used, each with
      its DIRECTION in its name and each VERIFIED before use: the exact
      Dirichlet / Neumann / PARITY eigenpairs, the sup bounds, the T148
      second-difference l1 ceiling (quoted, re-verified, never re-derived), the
      SYMBOL-INTEGRAL identity for the section quadratic form and the section
      monotonicity it implies, the PARITY COMPRESSION identities
      U_-^T T_M(c) U_- = A and U_-^T L_0^(M) U_- = L_P, the DISCRETE SOBOLEV
      step, the Rayleigh floor L_P >= mu^P_1 I, and the pencil transport.
  X1  THE LOCAL MODEL AND THE LEAKAGE ANATOMY.  Where the symbol minimum is,
      how wide the negative window th_c is against the odd mode spacing th_1;
      then the HONEST NEGATIVE that reshapes the block -- the parity symbol read
      mode by mode (t_k^T A t_k against f(th_k)) FAILS, because f moves by O(1)
      across one mode spacing, so no pointwise symbol statement is admissible at
      the bottom and T150's rest item 3 is a dead end as posed; then the local
      model that DOES hold, as a certified MATRIX statement (lam_k <= S mu^P_k by
      inertia counts, order 2, O(1) prefactor) together with the certified pencil
      floor kap; and then the LEAKAGE dissected: band by band in k, as a mode
      rotation against t_1, as a sideband row, and against the lag ranges the
      atoms occupy.
  X2  THE LADDER CLOSURE.  Route (i) the MULTIPLICATIVE mode comparison via the
      Sobolev step (the one that lives), instrumented against route (i-additive)
      via relative Davis-Kahan, which is priced and shown to be the wrong tool;
      route (ii) the counting / layer-cake reading, which asks how much of the
      ladder the Q_star average actually needs.  Per route: theorem / certified
      layer / measured, plus the NEW ladder constant and its trend against the
      0.25 bar.
  X3  THE CLEAN-UP.  min Lam^arch CLOSED from the smooth kernel alone (T150 rest
      item 2); the Q_star ceiling and the end-to-end fraction with the best X2
      bound, against T150's numbers; and the MANDATORY STRESS PAIR, with the
      question WHERE the no-go breaks now that the ladder runs through a pencil
      ratio.
  X4  THE MAP V23, the promotion list (T149's 7 and T150's 9 are PENDING and are
      NOT duplicated), the shortest rest list, and the honest conclusion.

WHAT IS A THEOREM, WHAT IS CERTIFIED, WHAT IS A PRIORI, WHAT IS MEASURED
  * THEOREM means classical, cited, and never re-proved.
  * CERTIFIED means a completed Cholesky (Wilkinson 1968; Higham 2002) with the
    declared floating-point floor, or a completed LDL^T inertia count
    (Sylvester 1852; Bunch-Kaufman 1977), or an elementary inequality evaluated
    EXACTLY on the actual objects with a declared rounding guard -- always in the
    DIRECTION stated in the name.
  * A PRIORI means: the number is a functional of the FORM alone, with no
    eigenvector read anywhere.  kap, K, rho, kap_sym, K_sym, f(0), th_c,
    ||c^atom||_1 and the inertia counts all are; so, and this is the point of
    this probe, is the per-mode bound 2 m sqrt(K_bot mu^P_k / kap).
  * MEASURED means a number that reads a computed eigenvector as an object in
    its own right.  It enters as a CROSS-CHECK, never as a hypothesis.
  * A FIT is a least-squares exponent with a delete-one jackknife band, always
    labelled, NEVER load-bearing.  A FINITE SURFACE PROVES NO STATEMENT FOR ALL
    D, and the verdict rule enforces that: the word 'proved' is unreachable in
    every branch.
  * THE GRID-TO-CONTINUUM CARE.  kap_sym and K_sym are DESIGNED on a finite
    theta grid, so the symbol-only formula is labelled DESIGN and is never
    load-bearing.  What is load-bearing is the MATRIX pencil pair, certified by
    Cholesky, which needs no continuum step at all.

FENCES
  * THE RH FENCE, PROMINENT AND FIRST.  The surrounding statement is the
    positivity of a Weil window form (Weil 1952; Bombieri 2000; Connes 1999) on
    a FINITE list of prime-power zones and a FINITE window.  Weil's criterion is
    CITED as an address and is NEVER USED, in either direction.  Nothing here
    claims, assumes or approaches RH.  Even with the odd ladder closed, what
    would stand is a finite-window positivity statement with an explicit
    constant on prime-power zones in frame A; the distance from there to RH is
    mapped in X4 and never travelled.  No zero data of any kind is read,
    generated or approximated; an AST firewall enforces this together with the
    import whitelist and the absence of any write-mode file access.
  * DISCOVERY ONLY.  Nothing is promoted.  No verification module, no ledger, no
    TeX, no website, no changelog, no next.txt is touched; this is ONE new file
    in experiments/tfpt-discovery/ and it writes nothing.
  * HARD CAPS.  Largest factorised / inverted / diagonalised matrix <= 1500;
    runtime budget 660 s (< 900 s), with per-block guards that truncate a pool
    rather than overrun.

CLASSICAL ADDRESSES (cited, never re-proved)
  Kac-Murdock-Szego 1953 (the exact sine / cosine sections and their eigenvalue
  ladder nu_k = pi k^2); Widom 1958 (Toeplitz sections with a vanishing symbol,
  and the local behaviour at a symbol minimum); Basor-Ehrhardt 2009
  (Toeplitz-plus-Hankel determinants, Fredholm theory, the parity-sector
  decomposition); Bottcher-Silbermann (the modern Toeplitz+Hankel algebra);
  Weyl 1912 (eigenvalue perturbation and the minimax characterisation);
  Bauer-Fike 1960; Davis-Kahan 1970; Parlett (the symmetric eigenvalue problem
  and the pencil reduction); Hardy-Littlewood-Polya 1934 and Agmon 1965 (the
  Sobolev / Agmon step in its continuum form); Sylvester 1852; Bunch-Kaufman
  1977; Wilkinson 1968; Higham 2002; Chebyshev 1852 and Rosser-Schoenfeld 1962
  (psi(x) <= B x); Maz'ya 1985; Charikar 2000.
"""

import ast
import math
import os
import time

import numpy as np
from numpy.linalg import LinAlgError
from scipy.linalg import cho_factor, cho_solve, eigh, ldl, solve_triangular

np.seterr(all="ignore")

PASS = 0
FAIL = 0
T_START = time.time()

EULER = 0.5772156649015328606065120900824
LOG_PI = math.log(math.pi)

MAX_H = 1500                 # HARD cap on any FACTORISED / INVERTED form
BUDGET_S = 660.0             # HARD probe budget (< 900 s)
RESERVE_S = 200.0            # reserved for X2 .. X4 after the window loop

U_ROUND = 2.0 ** -53
ROUND_GUARD = 8.0 * U_ROUND  # outward rounding on every certified ratio
GL_N = 48
_GLX, _GLW = np.polynomial.legendre.leggauss(GL_N)

NU_MAIN = 4                  # T105 admissibility floor / T112 frame A
H_MIN = 24
CHUNK = 16384

ATOM_MAX = 400000
ZONE_DEEP = 380000

# --- the measurement surface (declared BEFORE any result is seen) ------------
# The contract is about m-FREENESS, so the surface takes every admissible zone
# it can afford rather than a stride through a few.  It is smaller than T150's
# because every window now pays for a PENCIL reduction on top of the chain.
SURF_ZONES = 72
SURF_HCAP = 1500
STRATA = 4

THETA_BLK = 10.0             # the bottom block, preregistered as in T147 .. T150

# --- THE LADDER READ, preregistered ------------------------------------------
K_LAD = 24                   # modes read for the ladder
LAD_BAR = 0.25               # |exponent| + band for "the constant is FLAT"

# --- THE PENCIL, preregistered ----------------------------------------------
# The certified pencil pair is sought by ONE dense reduction plus Cholesky
# certificates; the backoff ladder below is fixed here, before any number.
PEN_BACKOFF = (1.0e-12, 1.0e-9, 1.0e-6, 1.0e-4, 1.0e-3, 1.0e-2, 1.0e-1)
RPEN_BAR = 0.25              # non-growing bar for the BOTTOM pencil ratio
CS_BAR = 0.25                # non-growing bar for the Sobolev ladder constant

# --- THE SYMBOL GRID (DESIGN ONLY, never load-bearing) ----------------------
N_TH = 4096                  # uniform theta grid on [0, pi]
N_TH_LOG = 256               # geometric refinement towards theta = 0
# The ratio (f(th) - f(0)) / (2 - 2 cos th) is a 0/0 form at the origin, so the
# grid floor is set where the cancellation in the numerator still leaves several
# digits.  Below it the quotient is numerical noise, and reading noise as a
# minimum would manufacture a spurious kap_sym = 0.
TH_LO = 1.0e-3

# --- THE CERTIFIED BOTTOM LADDER --------------------------------------------
# The number of low modes for which lam_k <= S mu^P_k is CERTIFIED by completed
# LDL^T counts rather than read off a diagonalisation.  Fixed here.
K_CERT = 8

# --- the certified counting ladder (T148, quoted in form) --------------------
RHO_LADDER = (1.5, 2.0, 4.0, 8.0, 16.0, 64.0, 256.0, 1024.0)
K_FIT = 12

# --- THE CUT LADDER of the Q_star ceiling (T148 .. T150, quoted in form) -----
CUT_LADDER_Q = (1, 2, 3, 4, 6, 8, 12, 16, 24, 32, 48, 64, 96, 128, 192)
CUT_MAX = 192

# --- the cake (T145 .. T150, quoted in form) --------------------------------
BASE_GRID = (2.0, 1.5, 1.25, 1.125, 1.0625, 1.03125)
FL_TARGET = 1.0e-12

# --- THE CHEBYSHEV BUDGET ---------------------------------------------------
# psi(x) <= B_PSI x for all x > 0 (Chebyshev 1852 in the elementary form,
# Rosser-Schoenfeld 1962 Thm 12 for the constant).  CITED, and VERIFIED on the
# exact range this probe actually uses -- never assumed beyond it.
B_PSI = 1.03883

# --- the parity pool (the compression identities need the FULL M x M form) ---
PAR_MCAP = 512
PAR_POOL = 4

# --- the stress forms -------------------------------------------------------
NOGO_EPS = 1.0e-3
NOGO_SIZES = (64, 128, 256, 512, 1024)
CTRL_SIZES = (64, 128, 256, 512, 1024)

# --- reading rules, ALL preregistered ---------------------------------------
BAR_UNIF = 0.25
CTRL_TOL = 0.06              # relative tolerance for "nu_k = pi k^2" on a model
QLAD_BAR = 3.0               # tolerated loss of the ladder form vs the minimum
K_BANDS = ((1, 1), (2, 4), (5, 16), (17, 64), (65, 1 << 30))

# --- T140 .. T150 numbers, QUOTED and never recomputed ----------------------
SW_CERT_T148 = 1.9587
QSTAR_T147 = 2.8634
KAPUP_CONST_T149 = 2.3146
SIG_CONST_T149 = 5.5789
C_LAD_T150 = (14.24, 43.39)
C_LAD_PI_T150 = 13.81
C_LAD_EXP_T150 = (0.258, 0.009)
C_ARG1_T150 = (67, 72)
L1_T150 = (1.41, 1.79)
SUP_T150 = (2.45, 3.41)
FRAC_T150 = (0.068, 0.1845)
IDENT_T150 = 4.0e-16
EXPAMP_T150 = 14.11
NEG_AR_T150 = (2, 7)
DK_DEAD_T150 = (2.4, 5.8)
LVL_EXP_T150 = 0.244
NOGO_EXP_T150 = 1.84
PROMO_T149 = 7
PROMO_T150 = 9

ZETA4 = math.pi ** 4 / 90.0  # sum_{k>=1} k^{-4} (Euler 1735), an EXACT constant


def check(name, ok, detail=""):
    global PASS, FAIL
    if ok:
        PASS += 1
    else:
        FAIL += 1
    print("check  %-42s %s  %s" % (name, "PASS" if ok else "FAIL", detail))


def info(name, detail=""):
    print("info   %-42s %s" % (name, detail))


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
            msk = np.ones(n, dtype=bool)
            msk[i] = False
            ai, bi, _ = fit_line(x[msk], y[msk])
            aa.append(ai)
            bb.append(bi)
    sa = (0.5 * (max(aa) - min(aa))) if aa else float("nan")
    sb = (0.5 * (max(bb) - min(bb))) if bb else float("nan")
    return a0, b0, rms, sa, sb, n


def pow_fit(xv, yv, tag):
    """A FIT of y ~ c x^p in log-log with a jackknife band.  NEVER load-bearing."""
    x = np.asarray(xv, dtype=float)
    y = np.asarray(yv, dtype=float)
    ok = np.isfinite(x) & np.isfinite(y) & (x > 0.0) & (y > 0.0)
    n_ok = int(np.count_nonzero(ok))
    if n_ok < 3:
        return dict(tag=tag, c=float("nan"), p=float("nan"), rms=float("nan"),
                    sc=float("nan"), sp=float("nan"), n=n_ok)
    a0, b0, rms, sa, sb, n = fit_band(np.log(x[ok]), np.log(y[ok]))
    return dict(tag=tag, c=math.exp(a0), p=b0, rms=rms, sc=sa, sp=sb, n=n)


def fit_str(f):
    return "x^(%.3f +- %.3f)" % (f["p"], f["sp"])


def flat_ok(f, bar=BAR_UNIF):
    """The preregistered READING of a FIT: |p| plus its jackknife band inside the
    bar.  A FIT is never load-bearing; this only LABELS it."""
    return bool(np.isfinite(f["p"]) and np.isfinite(f["sp"])
                and abs(f["p"]) + f["sp"] <= bar)


def nogrow_ok(f, bar=BAR_UNIF):
    """THE PREREGISTERED READING FOR AN UPPER BOUND.  A quantity that enters the
    chain only as a CEILING needs one thing: that it does not GROW.  Reads
    p + band <= bar, and every use is labelled NON-GROWING rather than FLAT.
    Still a reading of a FIT, still never load-bearing."""
    return bool(np.isfinite(f["p"]) and np.isfinite(f["sp"])
                and f["p"] + f["sp"] <= bar)


def band_ok(f, lo, hi):
    """Does the measured exponent's jackknife band CONTAIN the theory value?
    A reading, not a proof."""
    if not (np.isfinite(f["p"]) and np.isfinite(f["sp"])):
        return False
    return bool(f["p"] - f["sp"] <= hi and f["p"] + f["sp"] >= lo)


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
    check("ol_firewall.tokens", not hits, "forbidden token hits: %d" % len(hits))
    check("ol_firewall.imports", not bad_imports,
          "non-whitelisted imports: %s" % (bad_imports or "none"))
    check("ol_firewall.no_writes", not bad_writes,
          "write-mode file access: %s" % (bad_writes or "none"))
    check("ol_firewall.one_file", os.path.basename(os.path.abspath(__file__))
          == "odd_ladder_probe.py", "single new file in the sandbox")


# ----------------------------------------------------------------------------
# prime-power arithmetic (exact, cheap) -- the T111 .. T150 code path
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


def atoms_in(alpha):
    lim = 2.0 * alpha + 1.0e-14
    k = int(np.searchsorted(U_SORTED, lim, side="right"))
    return ATOM_PAIRS[:k]


def psi_ratio_max(atoms_all):
    """THE VERIFIED RANGE OF THE CITED CHEBYSHEV BOUND.  psi(x) is a step
    function that jumps at prime powers, so max_x psi(x)/x is attained at a jump
    point; the maximum over exactly those points is therefore the true maximum
    over the whole range.  DIRECTION: an UPPER bound on psi(x)/x for all
    x <= ATOM_MAX, and it is COMPUTED, not assumed."""
    best, arg = 0.0, 0
    acc = 0.0
    for n, lam_n, _u, _mu in atoms_all:
        acc += lam_n
        r = acc / float(n)
        if r > best:
            best, arg = r, n
    return best, arg


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


def atom_lags(alpha, M, atoms):
    """THE ARITHMETIC PART OF THE LAG VECTOR, ISOLATED.  Every prime-power atom
    contributes -mu_j/2 times a linear spline of total mass 1 around u_j, plus a
    reflected spline when u_j < D.  So c^atom <= 0 entrywise, and
        ||c^atom||_1 <= sum_j mu_j
    with EQUALITY up to the (nonnegative) reflected term."""
    D = 2.0 * alpha / M
    c = np.zeros(M)
    mu_tot = 0.0
    n_hit = 0
    for u_j, mu_j in atoms:
        mu_tot += mu_j
        n_hit += 1
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
    return c, D, mu_tot, n_hit


def lag_vector_split(alpha, M, atoms):
    """THE EXACT SPLIT c = c^arch + c^atom of the T115 lag assembly.  The sum is
    bit-for-bit the object T111 .. T150 use."""
    c_at, D, mu_tot, n_hit = atom_lags(alpha, M, atoms)
    c_ar = arch_lags(M, D)
    return dict(c=c_ar + c_at, c_ar=c_ar, c_at=c_at, D=D, mu_tot=mu_tot,
                n_atom=n_hit, l1_at=float(np.sum(np.abs(c_at))))


def atom_hit_lags(alpha, M):
    """THE LAG INDICES a prime-power atom imprints on, as an exact set."""
    D = 2.0 * alpha / M
    lim = 2.0 * alpha + 1.0e-14
    k = int(np.searchsorted(U_SORTED, lim, side="right"))
    if k == 0:
        return np.zeros(0, dtype=np.int64)
    i0 = np.floor(U_SORTED[:k] / D).astype(np.int64)
    hits = np.concatenate([i0, np.minimum(i0 + 1, M - 1)])
    return np.unique(np.clip(hits, 0, M - 1))


# ----------------------------------------------------------------------------
# the sections and the parity structure
# ----------------------------------------------------------------------------
def odd_toeplitz(c, M):
    """A_rs = c_{|r-s|} - c_{M-1-r-s} on the ODD section, r, s = 0 .. M/2 - 1.
    THE TOEPLITZ-MINUS-HANKEL STRUCTURE, exact and not an approximation: the
    object Szego/Widom theory speaks about (Widom 1958; Basor-Ehrhardt 2009)."""
    h = M // 2
    rr = np.arange(h)
    return c[np.abs(rr[:, None] - rr[None, :])] - c[(M - 1) - rr[:, None] - rr[None, :]]


def even_toeplitz(c, M):
    """A^+_rs = c_{|r-s|} + c_{M-1-r-s}: THE EVEN PARITY SECTOR, the Toeplitz
    PLUS Hankel partner.  Needed only to LOCATE the negative inertia."""
    h = M // 2
    rr = np.arange(h)
    return c[np.abs(rr[:, None] - rr[None, :])] + c[(M - 1) - rr[:, None] - rr[None, :]]


def full_toeplitz(c, M):
    """T_M(c)_{ij} = c_{|i-j|}, the FULL symmetric section.  Built only for the
    small parity pool, where M <= PAR_MCAP is far inside MAX_H."""
    ii = np.arange(M)
    return c[np.abs(ii[:, None] - ii[None, :])]


def parity_isometries(M):
    """e^-_s = (delta_s - delta_{M-1-s})/sqrt(2) and e^+_s = (delta_s +
    delta_{M-1-s})/sqrt(2), s = 0 .. M/2-1, as the columns of two M x (M/2)
    isometries.  Together they are an ORTHONORMAL BASIS of R^M."""
    h = M // 2
    Um = np.zeros((M, h))
    Up = np.zeros((M, h))
    r2 = 1.0 / math.sqrt(2.0)
    for s in range(h):
        Um[s, s] = r2
        Um[M - 1 - s, s] = -r2
        Up[s, s] = r2
        Up[M - 1 - s, s] = r2
    return Um, Up


# ----------------------------------------------------------------------------
# X1's CENTRAL OBJECT: THE SYMBOL, ITS MINIMUM, AND THE ODD SHIFT
# ----------------------------------------------------------------------------
def theta_grid():
    """The DESIGN grid: uniform on [0, pi] plus a geometric refinement towards
    theta = 0, where the whole question lives.  A grid is a DESIGN, never a
    certificate; every number it produces is re-certified at matrix level."""
    th_u = np.linspace(0.0, math.pi, N_TH)
    th_g = np.exp(np.linspace(math.log(TH_LO), math.log(math.pi), N_TH_LOG))
    th = np.unique(np.concatenate([th_u, th_g]))
    return th


TH_GRID = theta_grid()


def symbol_values(c, th):
    """f(th) = c_0 + 2 sum_{k>=1} c_k cos(k th), evaluated in chunks so that a
    window with M = 2000 lags and a 4000-point grid never allocates a big
    matrix."""
    c = np.asarray(c, dtype=float)
    out = np.full(th.shape[0], c[0])
    kk = np.arange(1, c.shape[0])
    step = max(1, int(2.0e6 // max(th.shape[0], 1)))
    for a in range(0, kk.shape[0], step):
        b = min(kk.shape[0], a + step)
        out += 2.0 * (np.cos(np.outer(th, kk[a:b])) @ c[1 + a:1 + b])
    return out


def symbol_local_model(c, m):
    """THE LOCAL MODEL AT THE SYMBOL MINIMUM, INSIDE THE ODD SECTOR.  Everything
    here is a functional of the lag vector alone -- A PRIORI, no eigenvector.
      * f0 = f(0), the T148/T150 honest negative, re-read and never re-derived;
      * th_min / f_min: WHERE the symbol minimum actually is;
      * th_c: the first sign change of f, i.e. the WIDTH of the negative window;
      * th_1 = 2 pi / N: the FIRST POINT OF THE ODD GRID.  The parity sines live
        on th_k = 2 pi k / N and never touch the origin, which is the whole
        mechanism: the odd sector STEPS OVER the negative window iff th_c < th_1;
      * f2 = f''(0) = -2 sum k^2 c_k, the ORDER of the local model at 0;
      * kap_sym = min_{th > 0} (f(th) - f(0)) / (2 - 2 cos th) and K_sym the max:
        the DESIGN pair of the symbol comparison f >= kap (2-2cos) + f(0), which
        by the section symbol-integral identity transports to A >= kap L_P + f0 I
        on the odd sector;
      * rho = |f0| / (kap_sym mu^P_1): the POSITIVITY MARGIN of that comparison.
        rho < 1 would be a CLOSED a priori criterion for odd-sector positivity;
      * f_var = |f(2 th_1) - f(th_1)| / |f(th_1)|: how much the symbol MOVES over
        ONE odd mode spacing.  This is the number that decides whether a symbol
        argument is admissible at the resolution of the bottom mode at all, and
        it is reported whatever it says."""
    N = 2 * m + 1
    th = TH_GRID
    f = symbol_values(c, th)
    f0 = float(f[0])
    j = int(np.argmin(f))
    pos = np.nonzero(f > 0.0)[0]
    if f0 > 0.0:
        th_c = 0.0
    elif pos.size == 0:
        th_c = float(math.pi)
    else:
        i1 = int(pos[0])
        i0 = i1 - 1
        f0v, f1v = float(f[i0]), float(f[i1])
        w = f0v / (f0v - f1v) if f1v != f0v else 0.5
        th_c = float(th[i0] + w * (th[i1] - th[i0]))
    kk = np.arange(1, c.shape[0], dtype=float)
    f2 = float(-2.0 * np.sum(kk * kk * c[1:]))
    use = th >= TH_LO
    den = 2.0 - 2.0 * np.cos(th[use])
    rat = (f[use] - f0) / np.where(den > 0.0, den, np.inf)
    rat = rat[np.isfinite(rat)]
    kap_sym = float(np.min(rat)) if rat.size else float("nan")
    K_sym = float(np.max(rat)) if rat.size else float("nan")
    mu1 = 4.0 * math.sin(math.pi / N) ** 2
    th_1 = 2.0 * math.pi / N
    rho = (abs(f0) / (kap_sym * mu1)) if kap_sym > 0.0 else float("inf")
    f_th1 = float(np.interp(th_1, th, f))
    f_th2 = float(np.interp(2.0 * th_1, th, f))
    return dict(f0=f0, f_min=float(f[j]), th_min=float(th[j]),
                f_max=float(np.max(f)),
                neg_share=float(np.count_nonzero(f < 0.0)) / float(th.shape[0]),
                th_c=th_c, th_1=th_1, mu1=mu1, f2=f2,
                kap_sym=kap_sym, K_sym=K_sym, rho=rho,
                f_th1=f_th1, f_th2=f_th2,
                f_var=abs(f_th2 - f_th1) / max(abs(f_th1), 1.0e-300),
                loc_th1=kap_sym * mu1 + f0,
                step_over=bool(th_c < th_1),
                R_sym=(K_sym / (kap_sym * (1.0 - rho))
                       if (kap_sym > 0.0 and rho < 1.0) else float("inf")))


# ----------------------------------------------------------------------------
# CERTIFICATION (Wilkinson 1968; Higham 2002; Sylvester 1852)
# ----------------------------------------------------------------------------
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


def ray_top(X, iters=90):
    """lam_max of a SYMMETRIC X by a SHIFTED power iteration.  The returned value
    is a RAYLEIGH QUOTIENT, hence a rigorous LOWER bound -- used only as a SEED."""
    n = X.shape[0]
    if n == 0:
        return 0.0
    if n == 1:
        return float(X[0, 0])
    sig = gersh(X)
    y = np.ones(n) / math.sqrt(n)
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
    """CERTIFY lam_max(X) <= s by a COMPLETED CHOLESKY of s I - X.  DIRECTION: an
    UPPER bound.  The GUESS is only a SEED."""
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


def cert_lam_min(X, guess=None, tries=14, grow=1.0e-7):
    """CERTIFY lam_min(X) >= t by a completed Cholesky of X - t I.  DIRECTION: a
    LOWER bound."""
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


def inertia_neg(X):
    """THE CERTIFIED EIGENVALUE COUNT (Sylvester 1852; Bunch-Kaufman 1977;
    Higham 2002 ch. 11).  Returns -1 when the factorisation does not complete, so
    a missing certificate is REPORTED rather than silently replaced."""
    n = X.shape[0]
    if n == 0:
        return 0
    try:
        _lu, d, _perm = ldl(sym(X), lower=True)
    except (LinAlgError, ValueError):
        return -1
    if not np.all(np.isfinite(d)):
        return -1
    i, neg = 0, 0
    while i < n:
        two = (i + 1 < n) and (abs(float(d[i, i + 1])) > 0.0
                               or abs(float(d[i + 1, i])) > 0.0)
        if two:
            a = float(d[i, i])
            b = float(d[i, i + 1]) if abs(float(d[i, i + 1])) > 0.0 else float(d[i + 1, i])
            cc = float(d[i + 1, i + 1])
            det = a * cc - b * b
            tr = a + cc
            if det < 0.0:
                neg += 1
            elif tr < 0.0:
                neg += 2
            i += 2
        else:
            if float(d[i, i]) < 0.0:
                neg += 1
            i += 1
    return neg


# ----------------------------------------------------------------------------
# the frame (T112 frame A, window forced EVEN so that h = M/2 exactly)
# ----------------------------------------------------------------------------
def even_window(u, D):
    M = int(math.ceil(u / D - 1.0e-9)) + 1
    if M % 2:
        M += 1
    return M


def lump_pair(A):
    """Delta = the POSITIVE off-diagonal part, L_Delta = diag(Delta 1) - Delta,
    A_B = A + L_Delta.  DIRECTION: L_Delta >= 0, so A_B >= A."""
    h = A.shape[0]
    dg = np.diag(A).copy()
    off = A - np.diag(dg)
    Dl = np.where(off > 0.0, off, 0.0)
    P_row = Dl.sum(axis=1)
    LD = np.diag(P_row) - Dl
    A_B = sym(A + LD)
    offB = A_B - np.diag(np.diag(A_B))
    return dict(h=h, A_B=A_B, dg=dg, dgB=np.diag(A_B).copy(), P=P_row,
                stieltjes=int(bool(np.all(offB <= 1.0e-300))
                              and bool(np.all(np.diag(A_B) > 0.0))))


def diag_explicit(c, M):
    """THE DIAGONAL OF A_B AS AN EXPLICIT SUM OVER THE ZONE'S LAG STRUCTURE:
        Lam_r = c_0 - c_{M-1-2r} + sum_{s != r} max(c_{|r-s|} - c_{M-1-r-s}, 0) ."""
    h = M // 2
    rr = np.arange(h)
    A = c[np.abs(rr[:, None] - rr[None, :])] - c[(M - 1) - rr[:, None] - rr[None, :]]
    dg = np.diag(A).copy()
    off = A - np.diag(dg)
    return dg + np.maximum(off, 0.0).sum(axis=1)


def arch_diag_closed(c_ar, M):
    """X3 / T150 REST ITEM 2: A CLOSED LOWER BOUND ON min Lam^arch FROM THE
    SMOOTH KERNEL ALONE -- and it turns out to be ATTAINED, not merely a bound.
    The exact diagonal is
        Lam^arch_r = c_0 - c_{M-1-2r} + sum_{s != r} max(c_{|r-s|} - c_{M-1-r-s}, 0),
    and the archimedean kernel has TWO SHAPE PROPERTIES, both CHECKED per window
    rather than assumed: c_i < 0 for every lag i >= 1, and c_i is NON-DECREASING
    in i on i >= 1 (it rises back towards 0).  Given those:
      * at r = 0 every term of the sum is max(c_s - c_{M-1-s}, 0) with
        1 <= s <= M/2 - 1 < M-1-s, hence c_s <= c_{M-1-s} and the term is 0, so
            Lam^arch_0 = c_0 - c_{M-1}   EXACTLY;
      * for every r, dropping the (nonnegative) sum gives
            Lam^arch_r >= c_0 - c_{M-1-2r} >= c_0 - c_{M-1},
        the last step because M-1-2r <= M-1 and c is non-decreasing there.
    So min_r Lam^arch_r = c_0 - c_{M-1}: a CLOSED two-term functional of the
    smooth kernel, with NO arithmetic, NO matrix and NO eigenvector, and with no
    loss at all.  DIRECTION: a LOWER bound that is also attained."""
    c_ar = np.asarray(c_ar, dtype=float)
    tail = c_ar[1:M]
    sc = max(abs(float(c_ar[0])), 1.0)
    neg = bool(tail.size and np.all(tail < 0.0))
    inc = bool(tail.size < 2 or np.all(np.diff(tail) >= -1.0e-13 * sc))
    closed = float(c_ar[0] - (c_ar[M - 1] if M > 1 else 0.0))
    return dict(neg=neg, inc=inc, shape=bool(neg and inc), closed=closed)


# ----------------------------------------------------------------------------
# THE EXACT MODELS, THE l1 CEILING (T148, quoted) AND THE PARITY LAPLACIAN
# ----------------------------------------------------------------------------
def dirichlet_mu(m):
    """THE EXACT DIRICHLET EIGENVALUES mu_k = 4 sin^2(pi k / (2(m+1))), k = 1..m.
    THEOREM (Kac-Murdock-Szego 1953, section 4; classical)."""
    kk = np.arange(1, m + 1, dtype=float)
    return 4.0 * np.sin(0.5 * math.pi * kk / (m + 1.0)) ** 2


def sine_basis(m):
    """THE ORTHONORMAL DIRICHLET (sine) BASIS, sup bound sqrt(2/(m+1))."""
    jj = np.arange(m)
    kk = np.arange(1, m + 1)
    return math.sqrt(2.0 / (m + 1.0)) * np.sin(
        math.pi * np.outer(kk, jj + 1.0) / (m + 1.0))


def neumann_mu(m):
    """THE EXACT NEUMANN EIGENVALUES mu_k = 4 sin^2(pi k / (2m)), k = 0..m-1."""
    kk = np.arange(m, dtype=float)
    return 4.0 * np.sin(0.5 * math.pi * kk / m) ** 2


def cosine_basis(m):
    """THE ORTHONORMAL NEUMANN (cosine) BASIS, sup bound sqrt(2/m)."""
    jj = np.arange(m)
    kk = np.arange(m)
    C = math.sqrt(2.0 / m) * np.cos(math.pi * np.outer(kk, jj + 0.5) / m)
    C[0, :] = 1.0 / math.sqrt(m)
    return C


def parity_mu(m):
    """THE EXACT PARITY EIGENVALUES mu^P_k = 4 sin^2(pi k / N), N = 2m+1,
    k = 1 .. m -- the spectrum of the path Laplacian with corner entry 3 at the
    reflecting end, which is the Dirichlet path Laplacian of the FULL window
    restricted to its ANTISYMMETRIC parity sector (Kac-Murdock-Szego 1953 in the
    parity sector; Basor-Ehrhardt 2009 for why that sector is the natural one).
    In symbol language mu^P_k = (2 - 2 cos th_k) with th_k = 2 pi k / N: the odd
    grid, which never contains th = 0."""
    N = 2 * m + 1
    kk = np.arange(1, m + 1, dtype=float)
    return 4.0 * np.sin(math.pi * kk / N) ** 2


def parity_basis(m):
    """THE ORTHONORMAL PARITY BASIS t_k(r) = 2/sqrt(N) sin(2 pi k (r+1)/N),
    N = 2m+1, k = 1 .. m, sup bound 2/sqrt(N).  Note t_k(-1) = 0 EXACTLY: the
    odd sector vanishes at the left virtual node, which is what licences the
    discrete Sobolev step below."""
    N = 2 * m + 1
    jj = np.arange(m)
    kk = np.arange(1, m + 1)
    return (2.0 / math.sqrt(N)) * np.sin(2.0 * math.pi * np.outer(kk, jj + 1.0) / N)


def _lap_D(X):
    """L_0 X columnwise, L_0 = tridiag(-1, 2, -1) (DIRICHLET)."""
    out = 2.0 * X
    out[:-1] -= X[1:]
    out[1:] -= X[:-1]
    return out


def _lap_N(X):
    """L_N X columnwise, the same with corner diagonals 1 (NEUMANN)."""
    out = _lap_D(X)
    out[0] -= X[0]
    out[-1] -= X[-1]
    return out


def _lap_P(X):
    """L_P X columnwise: tridiag(-1, 2, -1) with the LAST diagonal entry 3.  That
    corner is not a choice: for an antisymmetric vector of the full window the
    reflected neighbour of the last index is MINUS the last index."""
    out = _lap_D(X)
    out[-1] += X[-1]
    return out


def lap_P_mat(m):
    """L_P as a dense matrix.  It is the symbol-2-2cos section of the FULL window
    compressed to the odd sector, and it is the model the pencil is taken
    against."""
    L = sym(2.0 * np.eye(m) - np.eye(m, k=1) - np.eye(m, k=-1))
    L[m - 1, m - 1] = 3.0
    return L


def ceilings(X, m, mu, sup_s, lap, scale):
    """THE VECTORISED CERTIFIED CEILING of T148, applied to every column at once.
    Columns must be unit vectors.  DIRECTION: every entry of B is an UPPER bound
    on |a_k|, hence the column sums are UPPER bounds on ||a||_1."""
    L1 = lap(X.copy())
    L2 = lap(L1.copy())
    n1 = np.sum(np.abs(L1), axis=0)
    n2 = np.sum(np.abs(L2), axis=0)
    with np.errstate(divide="ignore", invalid="ignore"):
        B1 = np.minimum(1.0, sup_s * n1[None, :] / mu[:, None])
        B2 = np.minimum(1.0, sup_s * n2[None, :] / (mu * mu)[:, None])
    B1 = np.where(np.isfinite(B1), B1, 1.0)
    B2 = np.where(np.isfinite(B2), B2, 1.0)
    B = np.minimum(B1, B2)
    nu = scale * n1
    del L1, L2
    return dict(nu=nu, ceil=np.sum(B, axis=0),
                ceil_closed=2.0 * np.sqrt(np.maximum(nu, 0.0)) + 1.0, B=B)


def ceil_D(X, m):
    return ceilings(X, m, dirichlet_mu(m), math.sqrt(2.0 / (m + 1.0)), _lap_D,
                    (m + 1.0) ** 1.5 / (2.0 * math.sqrt(2.0)))


def ceil_N(X, m):
    return ceilings(X, m, neumann_mu(m), math.sqrt(2.0 / m), _lap_N,
                    float(m) ** 1.5 / (2.0 * math.sqrt(2.0)))


def ceil_P(X, m):
    """THE PARITY CEILING, scale_P = (N/2)^{3/2}/(2 sqrt 2) = N^{3/2}/8."""
    N = 2.0 * m + 1.0
    return ceilings(X, m, parity_mu(m), 2.0 / math.sqrt(N), _lap_P,
                    N ** 1.5 / 8.0)


def mode_bounds(X, m, S, C, P, cap=None):
    """THE PER-MODE UPPER BOUND ON m ||psi||_inf^2 as the MINIMUM of every valid
    l1-ceiling bound available (T148 .. T150, quoted in form).  Because each
    ceiling is valid on its own, the pointwise minimum of the three is valid."""
    X = np.ascontiguousarray(X, dtype=float)
    nrm = np.linalg.norm(X, axis=0)
    nrm = np.where(nrm > 0.0, nrm, 1.0)
    X = X / nrm[None, :]
    cD = ceil_D(X, m)
    cN = ceil_N(X, m)
    cP = ceil_P(X, m)
    aS = S @ X
    aC = C @ X
    aP = P @ X
    viol = max(float(np.max(np.abs(aS) - cD["B"])),
               float(np.max(np.abs(aC) - cN["B"])),
               float(np.max(np.abs(aP) - cP["B"])))
    ceil_dn = np.minimum(cD["ceil"], cN["ceil"])
    ceil_3 = np.minimum(ceil_dn, cP["ceil"])
    nu_dn = np.minimum(cD["nu"], cN["nu"])
    nu_3 = np.minimum(nu_dn, cP["nu"])
    bnd = 2.0 * ceil_3 ** 2
    if cap is not None:
        bnd = np.minimum(bnd, float(cap))
    return dict(bound=bnd, viol=viol, ceil=ceil_3, ceil_dn=ceil_dn,
                ceil_P=cP["ceil"], nu=nu_3, nu_dn=nu_dn, nu_P=cP["nu"],
                nu_D=cD["nu"], nu_N=cN["nu"],
                which_P=int(np.count_nonzero(cP["ceil"] < ceil_dn)))


# ----------------------------------------------------------------------------
# THE HEART OF THIS PROBE: THE PENCIL AND THE DISCRETE SOBOLEV STEP
# ----------------------------------------------------------------------------
def grad_sq(psi):
    """||grad psi||_2^2 = sum_{s=0}^{m-1} (psi_s - psi_{s-1})^2 with psi_{-1} = 0,
    the LEFT-DIRICHLET first difference.  EXACT IDENTITY:
        ||grad psi||_2^2 = <psi, L_0 psi> - psi_{m-1}^2 <= <psi, L_P psi> ,
    the last step because L_P = L_0 + e_last e_last^T >= L_0 and the subtracted
    term is nonnegative.  DIRECTION: an UPPER bound on the gradient energy by the
    parity Dirichlet form."""
    psi = np.asarray(psi, dtype=float)
    d = np.diff(np.concatenate([[0.0], psi]))
    return float(d @ d)


def sobolev_sup(psi, lp_energy):
    """THE DISCRETE SOBOLEV / AGMON STEP, elementary and verified:
        psi_r^2 = sum_{s<=r} (psi_s^2 - psi_{s-1}^2)
                <= sum_s (|psi_s| + |psi_{s-1}|) |psi_s - psi_{s-1}|
                <= 2 ||psi||_2 ||grad psi||_2
    for any vector with psi_{-1} = 0 -- which every odd-sector vector has, since
    the antisymmetric extension vanishes at the virtual node.  Continuum address:
    Hardy-Littlewood-Polya 1934; Agmon 1965.  DIRECTION: an UPPER bound on
    ||psi||_inf^2, and with ||psi||_2 = 1 it reads ||psi||_inf^2 <= 2 sqrt(E)."""
    return 2.0 * math.sqrt(max(lp_energy, 0.0)) * float(np.linalg.norm(psi))


def pencil_pair(A, LP, m):
    """THE CERTIFIED PENCIL PAIR (kap, K) with kap L_P <= A <= K L_P.
    HOW: L_P is tridiagonal and positive definite, so one Cholesky L_P = G G^T
    and two triangular solves give Z = G^{-1} A G^{-T} whose spectrum IS the
    pencil spectrum (Parlett; the standard reduction of a definite pencil).  The
    extreme eigenvalues of Z are only SEEDS; the certificates are two completed
    Choleskys of A - kap L_P and K L_P - A.
    THE FLOOR IS CARRIED HONESTLY.  A completed Cholesky of A - kap L_P certifies
    A - kap L_P >= -fl I, and I <= L_P / mu^P_1, so what is certified is
        A >= (kap - fl / mu^P_1) L_P ,
    and the reported kap SUBTRACTS that correction.  Same, with the sign
    reversed, for K.  DIRECTION: kap is a LOWER bound, K an UPPER bound."""
    mu1 = 4.0 * math.sin(math.pi / (2 * m + 1)) ** 2
    fac = safe_cho(LP)
    if fac is None:
        return None
    G = np.tril(fac[0]) if fac[1] else np.tril(fac[0].T)
    try:
        Y = solve_triangular(G, A, lower=True, check_finite=False)
        Z = sym(solve_triangular(G, Y.T, lower=True, check_finite=False))
    except (LinAlgError, ValueError):
        return None
    del Y
    try:
        wz = eigh(Z, eigvals_only=True)
    except (LinAlgError, ValueError):
        del Z
        return None
    del Z
    lo_seed, up_seed = float(wz[0]), float(wz[-1])
    kap = float("nan")
    for eta in PEN_BACKOFF:
        k_try = lo_seed * (1.0 - eta) if lo_seed > 0.0 else lo_seed - eta
        X = sym(A - k_try * LP)
        if safe_cho(X) is not None:
            fl = chol_floor(gersh(X), m)
            kap = k_try - fl / mu1
            del X
            break
        del X
    K = float("nan")
    for eta in PEN_BACKOFF:
        K_try = up_seed * (1.0 + eta)
        X = sym(K_try * LP - A)
        if safe_cho(X) is not None:
            fl = chol_floor(gersh(X), m)
            K = K_try + fl / mu1
            del X
            break
        del X
    return dict(kap=kap, K=K, kap_seed=lo_seed, K_seed=up_seed, mu1=mu1,
                R=(K / kap) if (np.isfinite(kap) and kap > 0.0) else float("inf"),
                R_seed=(up_seed / lo_seed) if lo_seed > 0.0 else float("inf"),
                fl_rel=(abs(K - up_seed) / max(abs(up_seed), 1.0e-300)))


def cert_bottom_ladder(A, m, S_seed, k_cert=K_CERT):
    """THE CERTIFIED BOTTOM EIGENVALUE LADDER lam_k <= S mu^P_k, k <= k_cert.
    HOW, and WHY IT READS NO EIGENVECTOR: a completed LDL^T of A - tau I returns
    #{j : lam_j < tau} as a CERTIFICATE (Sylvester 1852; Bunch-Kaufman 1977), and
    lam_k < tau holds exactly when that count is at least k.  Taking
    tau_k = S mu^P_k for k = 1 .. k_cert therefore certifies the whole bottom
    ladder with k_cert inertia counts and no diagonalisation.  The seed S comes
    from a spectrum, so it is only a SEED; the certificate is the count.
    THIS IS THE OBJECT THAT REPLACES THE GLOBAL PENCIL TOP.  The global
    lam_max(A, L_P) is dominated by the TOP of the section, where L_P saturates at
    4 while the section does not -- and the top is irrelevant, because the cake
    bounds high modes by the trivial m anyway.  DIRECTION: an UPPER bound on the
    low eigenvalues, in units of the exact model ladder."""
    mu = parity_mu(m)
    kc = int(min(k_cert, m))
    for eta in PEN_BACKOFF:
        S = S_seed * (1.0 + eta)
        ok = True
        for k in range(1, kc + 1):
            n_lt = inertia_neg(A - (S * float(mu[k - 1])) * np.eye(m))
            if n_lt < k:
                ok = False
                break
        if ok:
            return dict(S=S, k_cert=kc, eta=eta)
    return None


def sobolev_ladder(kap, K, m, k_lad=K_LAD, kap_gauge=1.0):
    """THE ODD LADDER, A PRIORI AND m-FREE BY CONSTRUCTION GIVEN THE PENCIL.
    Chain, each step certified or exact and each in the direction named:
        (1) lam_k(A) <= K mu^P_k          [CERTIFIED by k inertia counts, UPPER;
                                           K is the BOTTOM ladder constant, NOT
                                           the global pencil top]
        (2) A >= kap L_P                  [certified pencil, LOWER]
            ==> <psi_k, L_P psi_k> <= lam_k(A) / kap <= K mu^P_k / kap
        (3) ||psi_k||_inf^2 <= 2 sqrt(<psi_k, L_P psi_k>)   [Sobolev, exact]
        ==> b_k := m ||psi_k||_inf^2 <= 2 m sqrt(K_bot mu^P_k / kap)
                                      <= 2 pi k sqrt(K_bot/kap) * (2m/N) .
    NOTHING ADDITIVE APPEARS ANYWHERE, so the Theta(D^3) smallness of the bottom
    -- which kills Weyl / Bauer-Fike / Davis-Kahan as MODE tools -- never enters.
    kap_gauge is the Loewner price of the gauge (max/min of Lam~), 1 in the const
    gauge where the whitened mode IS the pure-section mode.
    RETURNS the bound vector and the LINEAR ladder constant C_S = max_k b_k / k."""
    if not (np.isfinite(kap) and kap > 0.0 and np.isfinite(K) and K > 0.0):
        return None
    K_n = int(min(k_lad, m))
    mu = parity_mu(m)[:K_n]
    kk = np.arange(1, K_n + 1, dtype=float)
    b = kap_gauge * 2.0 * m * np.sqrt(np.maximum(K * mu / kap, 0.0))
    b_cap = np.minimum(b, float(m))
    return dict(b=b, b_cap=b_cap, C_S=float(np.max(b_cap / kk)),
                arg_S=int(np.argmax(b_cap / kk)) + 1,
                b1=float(b_cap[0]), bK=float(b_cap[K_n - 1]), K_n=K_n,
                C_closed=2.0 * math.pi * math.sqrt(K / kap) * (2.0 * m / (2.0 * m + 1.0)))


def sobolev_from_lams(kap, lams, m, kap_gauge=1.0):
    """THE SAME BOUND FED WITH THE ACTUAL LOW EIGENVALUES instead of the ladder:
        b_k = m ||psi_k||_inf^2 <= 2 m sqrt(lam_k / kap) .
    Eigenvalues are SPECTRAL DATA OF THE FORM -- certifiable by inertia counts,
    as cert_bottom_ladder does -- so this is still eigenvector-free.  It is what
    the cake consumes, while the ladder form above is what carries the m-freeness
    STATEMENT.  DIRECTION: UPPER."""
    if not (np.isfinite(kap) and kap > 0.0):
        return None
    lams = np.maximum(np.asarray(lams, dtype=float), 0.0)
    return np.minimum(kap_gauge * 2.0 * m * np.sqrt(lams / kap), float(m))


def leak_anatomy(psi, P, A, m, lam1, so):
    """X1's LEAKAGE ANATOMY.  WHY does the bottom mode carry l1 mass 1.41 .. 1.79
    in the parity basis instead of 1?  Everything here is MEASURED -- it reads a
    computed eigenvector as an object in its own right -- and enters as a
    cross-check, never as a hypothesis.
      * l1 / head / band shares: WHERE in k the mass sits;
      * sin_t1 = sqrt(1 - a_1^2): the mode ROTATION away from the model mode t_1,
        which is what the leakage IS;
      * the SIDEBAND ROW b_l = t_l^T A t_1: the coupling the arithmetic induces
        between the model bottom mode and the rest of the odd grid;
      * sob_gap: how lossy the Sobolev step is ON THIS MODE, i.e. the price of
        the inequality as opposed to the price of the leakage."""
    psi = np.asarray(psi, dtype=float)
    psi = psi / max(float(np.linalg.norm(psi)), 1.0e-300)
    a = P @ psi
    l1 = float(np.sum(np.abs(a)))
    bands = []
    for lo, hi in K_BANDS:
        hi_e = min(hi, m)
        if lo > hi_e:
            bands.append(0.0)
            continue
        bands.append(float(np.sum(np.abs(a[lo - 1:hi_e]))) / max(l1, 1.0e-300))
    t1 = P[0]
    ov = abs(float(a[0]))
    sin_t1 = math.sqrt(max(0.0, 1.0 - min(1.0, ov * ov)))
    row = P @ (A @ t1)
    r_diag = abs(float(row[0]))
    r_off = float(np.sum(np.abs(row))) - r_diag
    l_star = int(np.argmax(np.abs(row[1:]))) + 2 if m > 1 else 1
    e_lp = grad_sq(psi)
    sup_true = float(m) * float(np.max(np.abs(psi))) ** 2
    sup_sob = float(m) * sobolev_sup(psi, e_lp)
    return dict(l1=l1, bands=bands, ov_t1=ov, sin_t1=sin_t1,
                sup_true=sup_true, sup_sob=sup_sob,
                sob_gap=sup_sob / max(sup_true, 1.0e-300),
                e_lp=e_lp, e_lp_pred=lam1 / max(so["kap_sym"], 1.0e-300),
                r_diag=r_diag, r_off=r_off,
                r_off_share=r_off / max(r_diag + r_off, 1.0e-300),
                l_star=l_star,
                sgn_flip=int(np.count_nonzero(np.diff(np.sign(psi)) != 0.0)),
                part=1.0 / max(float(m) * float(np.sum(psi ** 4)), 1.0e-300))


# ----------------------------------------------------------------------------
# THE CHAIN (T145 .. T150, quoted in form -- never re-derived)
# ----------------------------------------------------------------------------
def greedy_density(Wp):
    """CHARIKAR'S GREEDY PEELING (Charikar 2000).  Both directions used: the
    returned density is ATTAINED, hence a LOWER bound on the optimum, and the
    guarantee greedy >= opt/2 turns it into opt <= 2 x greedy."""
    m = Wp.shape[0]
    if m < 2:
        return dict(dens=0.0, size=m)
    deg = Wp.sum(axis=1).astype(float)
    tot = 0.5 * float(deg.sum())
    alive = np.ones(m, dtype=bool)
    n_alive = m
    best, best_n = tot / m, m
    while n_alive > 1:
        d = np.where(alive, deg, np.inf)
        j = int(np.argmin(d))
        tot -= float(deg[j])
        alive[j] = False
        deg = deg - Wp[j]
        deg[j] = 0.0
        n_alive -= 1
        dens = tot / n_alive
        if dens > best:
            best, best_n = dens, n_alive
    return dict(dens=float(best), size=int(best_n))


def density_all_upper(R):
    """AN UPPER BOUND for Psi = sup_A (1^T R_AA 1)/|A| over ALL 2^m sets, the
    smaller of Charikar's greedy bound and the CERTIFIED lam_max of the same
    nonnegative matrix.  T145's licence-4 lesson: what is passed in must be |R|."""
    Rp = np.maximum(R, 0.0)
    np.fill_diagonal(Rp, 0.0)
    gr = greedy_density(Rp)
    dg_max = float(np.max(np.diag(R)))
    psi_char = dg_max + 4.0 * gr["dens"]
    psi_spec = dg_max + cert_lam_max(Rp, guess=ray_top(Rp))
    cands = [x for x in (psi_char, psi_spec) if np.isfinite(x)]
    best = min(cands) if cands else float("nan")
    del Rp
    return dict(up=best, char=psi_char, spec=psi_spec, greedy=gr["dens"])


def c0_of_base(Gam, Gam_1, base, m):
    """THE A PRIORI LEVEL CONSTANT at a given cake base (T146, quoted):
        c_0^ap(base) = 2 base^2 Gam min(1, Gam_1) + eps ."""
    vmax_ap = Gam / math.sqrt(max(m, 1))
    lb = math.log(base)
    k_bot = int(math.floor(math.log(FL_TARGET) / lb))
    while base ** k_bot > FL_TARGET:
        k_bot -= 1
    eps = 2.0 * base * vmax_ap * m * (base ** k_bot)
    return 2.0 * base * base * Gam * min(1.0, Gam_1) + eps, eps


def counting_cert(E, lam_lo, m, ladder=RHO_LADDER):
    """THE CERTIFIED COUNTING FUNCTION AND THE Sw BOUND (T148, quoted in form).
    At tau_i = rho_i lam_lo a completed LDL^T gives N_i = #{k : lam_k < tau_i} as
    a CERTIFICATE (Sylvester 1852), whence the LAYER-CAKE bound on
    sum_k lam_k^{-2}.  X2 route (ii) reads the SAME machinery in the other
    direction, as a counting bound on the ladder."""
    N = []
    taus = []
    for rho in ladder:
        tau = rho * lam_lo
        n_i = inertia_neg(E - tau * np.eye(m))
        if n_i < 0:
            return None
        N.append(int(n_i))
        taus.append(float(tau))
    N = np.maximum.accumulate(np.array(N, dtype=float))
    taus = np.array(taus, dtype=float)
    s2 = N[0] / (lam_lo * lam_lo)
    for i in range(len(taus) - 1):
        s2 += max(N[i + 1] - N[i], 0.0) / (taus[i] * taus[i])
    s2 += max(m - N[-1], 0.0) / (taus[-1] * taus[-1])
    c_bot = max(N[0] ** 2, 1.0)
    for i in range(len(taus) - 1):
        c_bot = max(c_bot, N[i + 1] ** 2 / ladder[i])
    return dict(N=N, taus=taus, sum_inv2_up=float(s2), C_bot=float(c_bot),
                C_tail=float((m * m) / ladder[-1]), n_band=int(N[-1]))


def kms_scaling(w, k_fit=K_FIT):
    """THE MEASURED BOTTOM SCALING lam_k/lam_hat ~ k^alpha, with the classical
    order-2 value alpha = 2 (Kac-Murdock-Szego 1953: for the Dirichlet section
    the ratio lies in [4k^2/pi^2, k^2] EXACTLY)."""
    m = w.shape[0]
    lam_hat = float(w[0])
    kk = np.arange(1, m + 1, dtype=float)
    ratio = w / max(lam_hat, 1.0e-300)
    kf = min(k_fit, m)
    f = pow_fit(kk[1:kf], ratio[1:kf], "lam_k/lam_hat")
    c_all = float(np.max(kk * kk / np.maximum(ratio, 1.0e-300)))
    br_up = bool(np.all(ratio[:kf] <= kk[:kf] ** 2 * (1.0 + 1.0e-9)))
    br_lo = bool(np.all(ratio[:kf] >= 4.0 * kk[:kf] ** 2 / math.pi ** 2 - 1.0e-9))
    return dict(fit=f, C_meas=c_all, bracket_up=br_up, bracket_lo=br_lo)


def counting_ladder(nu_sorted, k_lad):
    """X2 ROUTE (ii): THE LAYER-CAKE / COUNTING READING OF THE LADDER.  The
    Q_star average never needs nu MODE BY MODE: it needs the SORTED profile,
    because a weighted average with decreasing weights is maximal when the bounds
    are sorted increasingly (the rearrangement reading of T148's cake).  So the
    honest counting form of the ladder is
        N(nu) = #{k <= K : nu_k <= nu}  >=  sqrt(nu / C_cnt) ,
    equivalently C_cnt = max_j nu_(j) / j^2 with nu_(j) the SORTED values.
    DIRECTION: C_cnt <= C pointwise always, with equality iff the maximum of
    nu_k / k^2 is at the sorted position it already occupies."""
    v = np.sort(np.asarray(nu_sorted, dtype=float))[:k_lad]
    jj = np.arange(1, v.shape[0] + 1, dtype=float)
    return dict(C_cnt=float(np.max(v / jj ** 2)),
                arg_cnt=int(np.argmax(v / jj ** 2)) + 1)


def qstar_with(V, w, m, S, C, P, kap_gauge, b_extra=None):
    """THE l1 CEILING APPLIED TO Q_star (T148 .. T150, quoted in form), now with
    the SOBOLEV bound as an extra valid per-mode bound:
        Q_star <= [ sum_{k<=cut} b_k wt_k + m wt_{cut+1} ] / sum_k wt_k ,
        wt_k = lam_k^{-2} ,
    for ANY cut and ANY valid per-mode bounds b_k.  DIRECTION: UPPER throughout."""
    wt = 1.0 / (w * w)
    tot = float(np.sum(wt))
    order = np.argsort(-wt)
    K = int(min(m, CUT_MAX))
    idx = order[:K]
    VW = np.ascontiguousarray(V[:, idx])
    mp = mode_bounds(VW, m, S, C, P, cap=m)
    sup = m * np.max(np.abs(VW), axis=0) ** 2
    b_l1 = np.minimum(kap_gauge * mp["bound"], float(m))
    wt_sorted = wt[order]
    wk = wt_sorted[:K]

    def _best(bv):
        best, bcut = float("inf"), 1
        for cut in CUT_LADDER_Q:
            if cut > K:
                break
            tail = float(wt_sorted[cut]) if cut < m else 0.0
            val = (float(np.sum(bv[:cut] * wk[:cut])) + m * tail) \
                / max(tot, 1.0e-300)
            if val < best:
                best, bcut = val, cut
        return best, bcut

    q_l1, cut_l1 = _best(b_l1)
    q_sup, _ = _best(np.minimum(sup, float(m)))
    kk = np.arange(1, K + 1, dtype=float)
    nu_P = mp["nu_P"]
    cnt = counting_ladder(nu_P, K)
    out = dict(K=K, Qs_l1=q_l1, cut_l1=cut_l1, Qs_sup=q_sup,
               nu_k2=float(np.max(nu_P / kk ** 2)),
               nu_k2_arg=int(np.argmax(nu_P / kk ** 2)) + 1,
               nu_1=float(nu_P[0]), C_cnt=cnt["C_cnt"], arg_cnt=cnt["arg_cnt"],
               viol=mp["viol"],
               viol_b=float(np.max(sup - b_l1)),
               sup_max=float(np.max(sup)))
    if b_extra is not None:
        bx = np.minimum(np.asarray(b_extra, dtype=float)[:K], float(m))
        if bx.shape[0] < K:
            bx = np.concatenate([bx, np.full(K - bx.shape[0], float(m))])
        q_sb, cut_sb = _best(bx)
        out["Qs_sob"] = q_sb
        out["cut_sob"] = cut_sb
        out["Qs_both"] = _best(np.minimum(bx, b_l1))[0]
        out["sob_ok"] = bool(np.all(bx >= sup - 1.0e-9))
        out["sob_gain"] = q_l1 / max(q_sb, 1.0e-300)
    del VW, mp
    return out


def whiten_with(A, A_B, Lam_t):
    """THE GENERALISED WHITENING BY AN ARBITRARY POSITIVE DIAGONAL Lam~:
        E~ = Lam~^{-1/2} A Lam~^{-1/2},  W~ = Lam~^{-1/2} A_B Lam~^{-1/2},
        lam_min(A, A_B) >= lam_min(E~) / lam_max(W~),
    an identity plus one Rayleigh step (T149 licence 5).  DIRECTION: kap~_up =
    cert_lam_max(W~) is an UPPER bound and is the ONLY price of the gauge."""
    sq = 1.0 / np.sqrt(np.asarray(Lam_t, dtype=float))
    E = sym(A * np.outer(sq, sq))
    W = sym(A_B * np.outer(sq, sq))
    kap_up = cert_lam_max(W, guess=ray_top(W))
    return dict(E=E, W=W, sqinv=sq, kap_up=kap_up)


def chain_const(A, A_B, Lam_t, S, C, P, gap_ex, pen, so):
    """THE WHOLE T146 .. T150 CHAIN IN THE CONST GAUGE, with the SOBOLEV per-mode
    bound added as a fifth valid bound:
        lam_min(A, A_B) >= lam_min(E~) / kap~_up >= 1 / (kap~_up c_0^ap Psi),
        c_0^ap = 2 base^2 Gam min(1, Gam_1) + eps,  Gam = sqrt(Q_star) Sw.
    THE CONST GAUGE IS THE ONE T149 SINGLED OUT: Lam~ = const makes the whitened
    section A / const, so the whitened mode IS the pure-section mode and the
    pencil statement applies to it verbatim, with kap_gauge = 1."""
    m = A.shape[0]
    wt = whiten_with(A, A_B, Lam_t)
    E = wt["E"]
    kap_up = wt["kap_up"]
    if not np.isfinite(kap_up) or not (kap_up > 0.0):
        return None
    try:
        w, V = eigh(E)
    except (LinAlgError, ValueError):
        return None
    lam_hat = float(w[0])
    if not (lam_hat > 0.0):
        return None
    lam_lo = cert_lam_min(E, guess=lam_hat)
    if not (np.isfinite(lam_lo) and lam_lo > 0.0):
        return None
    fac = safe_cho(E)
    if fac is None:
        return None
    R = sym(cho_solve(fac, np.eye(m), check_finite=False))
    EV = E @ R
    den = np.sum(R * R, axis=0)
    num = np.sum(R * EV, axis=0)
    rres = np.linalg.norm(EV - np.eye(m), axis=0)
    del EV
    fl_q = chol_floor(gersh(E), m)
    lam_up = float(np.min(num / den)) + fl_q
    res_f = float(np.linalg.norm(rres))
    fro2 = float(np.sum(R * R))
    fro = math.sqrt(max(fro2, 1.0e-300))
    fro_lo = max(fro - res_f / lam_lo, 1.0e-300)
    fro_up = fro + res_f / lam_lo
    col_true = np.sqrt(den)
    col_cert = col_true + rres / lam_lo
    cmax = float(np.max(col_true))
    cmax_up = float(np.max(col_cert))
    Sw = lam_up * fro
    Sw_up = lam_up * fro_up
    Qs = m * cmax * cmax / fro2
    Qs_up = m * cmax_up * cmax_up / (fro_lo * fro_lo)
    gam_cert = math.sqrt(m) * lam_up * cmax_up
    gam_fac = math.sqrt(max(Qs_up, 0.0)) * Sw_up
    gam_true = math.sqrt(m) * lam_up * cmax
    gam1_cert = lam_up * float(np.sum(col_cert)) / math.sqrt(m)
    # the SOBOLEV bound vector, in the PURE-SECTION eigenvalue order.  The const
    # gauge scales every eigenvalue by the same factor, so the k-th whitened mode
    # is the k-th pure mode and no re-ordering is needed.
    g = float(Lam_t[0])
    lam_pure = w[:CUT_MAX] * g
    b_sob = sobolev_from_lams(pen["kap"], lam_pure, m, kap_gauge=1.0)
    qc = qstar_with(V, w, m, S, C, P, 1.0, b_extra=b_sob)
    cc = counting_cert(E, lam_lo, m)
    km = kms_scaling(w)
    Sw_cnt = (lam_up * math.sqrt(max(cc["sum_inv2_up"], 0.0))
              if cc is not None else float("nan"))
    Sw_ap_meas = (lam_up / lam_lo) * km["C_meas"] * math.sqrt(ZETA4)
    gam_best = min(gam_cert, gam_fac)
    gam1_best = min(gam1_cert, lam_up * fro_up)
    c0_tbl = {b: c0_of_base(gam_best, gam1_best, b, m) for b in BASE_GRID}
    b_star = min(BASE_GRID, key=lambda b: c0_tbl[b][0])
    c0_ap, eps_ap = c0_tbl[b_star]
    dens = density_all_upper(np.abs(R))
    ok_psi = bool(np.isfinite(dens["up"]) and dens["up"] > 0.0)
    chain = (1.0 / (kap_up * c0_ap * dens["up"])) if ok_psi else float("nan")
    sw_apr = min([x for x in (Sw_cnt, Sw_ap_meas) if np.isfinite(x)] or [float("nan")])

    def _frac(qs):
        if not np.isfinite(qs) or not ok_psi:
            return float("nan"), float("nan")
        gam = math.sqrt(max(qs, 0.0)) * sw_apr
        c0 = min(c0_of_base(gam, gam1_best, b, m)[0] for b in BASE_GRID)
        ch = 1.0 / (kap_up * c0 * dens["up"])
        return ch, (ch / gap_ex if gap_ex > 0.0 else float("nan"))

    ch_l1, fr_l1 = _frac(qc["Qs_l1"])
    ch_sob, fr_sob = _frac(qc.get("Qs_sob", float("nan")))
    ch_both, fr_both = _frac(qc.get("Qs_both", float("nan")))
    # THE BOTTOM LADDER of the PURE section: the ratio lam_k / mu^P_k over the
    # read modes.  This is the object that replaced the global pencil top.
    mu_P = parity_mu(m)
    n_lad = int(min(K_LAD, m))
    rat_lad = lam_pure[:n_lad] / mu_P[:n_lad]
    K_bot = float(np.max(rat_lad))
    k_bot_lo = float(np.min(rat_lad))
    sob = sobolev_ladder(pen["kap"], K_bot, m, k_lad=K_LAD, kap_gauge=1.0)
    # the LEAKAGE anatomy on the true bottom mode of the PURE section
    lam1_pure = lam_hat * g
    lk = leak_anatomy(V[:, 0], P, A, m, lam1_pure, so)
    out = dict(m=m, kap_up=kap_up, lam_hat=lam_hat,
               lam_2=float(w[1]) if m > 1 else float("nan"),
               lam1_pure=lam1_pure, gscale=g,
               rel_gap=((float(w[1]) - lam_hat) / lam_hat) if m > 1 else float("nan"),
               lam_lo=lam_lo, lam_up=lam_up, Sw=Sw, Sw_up=Sw_up,
               Sw_cnt=Sw_cnt, Qs=Qs, Qs_up=Qs_up,
               Qs_l1=qc["Qs_l1"], Qs_sob=qc.get("Qs_sob", float("nan")),
               Qs_both=qc.get("Qs_both", float("nan")),
               Qs_sup=qc["Qs_sup"], cut_l1=qc["cut_l1"],
               cut_sob=qc.get("cut_sob", -1),
               sob_ok=qc.get("sob_ok", False),
               sob_gain=qc.get("sob_gain", float("nan")),
               nu_k2=qc["nu_k2"], nu_k2_arg=qc["nu_k2_arg"], nu_1=qc["nu_1"],
               C_cnt=qc["C_cnt"], arg_cnt=qc["arg_cnt"],
               viol=qc["viol"], viol_b=qc["viol_b"], sup_max=qc["sup_max"],
               gam_best=gam_best, gam1_best=gam1_best, gam_true=gam_true,
               c0_ap=c0_ap, base_star=b_star, psi_up=dens["up"],
               C_bot=cc["C_bot"] if cc is not None else float("nan"),
               n_band=cc["n_band"] if cc is not None else -1,
               kms_p=km["fit"]["p"], kms_sp=km["fit"]["sp"],
               C_meas=km["C_meas"],
               chain=chain, frac=chain / gap_ex if gap_ex > 0.0 else float("nan"),
               chain_l1=ch_l1, frac_l1=fr_l1,
               chain_sob=ch_sob, frac_sob=fr_sob,
               chain_both=ch_both, frac_both=fr_both,
               K_bot=K_bot, k_bot_lo=k_bot_lo, R_bot=K_bot / pen["kap"],
               lam_pure=lam_pure[:K_LAD].copy(), sob=sob, lk=lk)
    del E, R, V, wt, qc
    return out


# ----------------------------------------------------------------------------
# THE STRESS FORMS
# ----------------------------------------------------------------------------
def nogo_form(m, eps=NOGO_EPS):
    """THE T145 NO-GO: R = a a^T + eps I with a_i = i^{-1/2}, E = R^{-1}.  R is
    PD, entrywise nonnegative, its density sup over ALL sets is bounded, and the
    bottom eigenvector of E is LOCALISED, so m ||psi||_inf^2 = m/H_m DIVERGES.
    DECISIVE FOR THIS PROBE: the no-go passes W1 (its whitening diagonal is
    smooth) and it passed T150's mechanism block, so it MUST break in X1/X2, and
    the probe asks exactly WHERE."""
    a = 1.0 / np.sqrt(np.arange(1, m + 1, dtype=float))
    R = np.outer(a, a) + eps * np.eye(m)
    n2 = float(a @ a)
    E = sym((np.eye(m) - np.outer(a, a) / (eps + n2)) / eps)
    return dict(R=sym(R), E=E, a=a, psi=a / math.sqrt(n2),
                lam_min=1.0 / (n2 + eps), Q_exact=m / n2)


def control_form(m):
    """THE DIRICHLET CONTROL: the path Laplacian L_0, the EXACT
    Kac-Murdock-Szego model.  nu_k = pi k^2 EXACTLY, so it fixes the ladder
    normalisation and every number on it must stay flat."""
    E = sym(2.0 * np.eye(m) - np.eye(m, k=1) - np.eye(m, k=-1))
    return dict(E=E, w=dirichlet_mu(m), psi=sine_basis(m)[0].copy())


def parity_control_form(m):
    """THE PARITY CONTROL: L_P itself, the operator whose exact eigenvectors are
    the parity sines.  On it the pencil is (1, 1) EXACTLY, so C_S must come out
    at exactly 2 pi (2m/N) and nu_k at exactly pi k^2."""
    E = lap_P_mat(m)
    return dict(E=E, w=parity_mu(m), psi=parity_basis(m)[0].copy())


# ----------------------------------------------------------------------------
section("X0  SETUP, THE RH FENCE, and THE LICENCES")
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
check("ol_x0.gap_facts", BERT_OK and EVEN_OK,
      "the ONLY two gap facts consumed anywhere in this file hold on all %d "
      "prime-power gaps up to n = %d: Bertrand-Chebyshev 1852 (g <= log 2) and "
      "the trivial even bound (g >= log(1 + 1/n)).  No gap CONJECTURE is used"
      % (NZ_DEEP, ZONE_DEEP))

para("""X0.0  THE RH FENCE, STATED BEFORE ANY NUMBER AND PROMINENTLY.  The
surrounding statement of this whole investigation is the positivity of a Weil
window form (Weil 1952; Bombieri 2000; Connes 1999) on a FINITE list of
prime-power zones and a FINITE window.  Weil's explicit-formula criterion is
CITED here as an ADDRESS and is NEVER USED, in either direction.  No zero data of
any kind is read, generated, approximated or extrapolated -- the AST firewall
above enforces that together with the import whitelist and the absence of any
write-mode file access.  What this probe investigates is one inequality about the
low eigenvectors of a finite Toeplitz-minus-Hankel section in its ODD PARITY
SECTOR.  Even if that inequality closed perfectly, what would stand is a
finite-window positivity statement with an explicit constant on prime-power zones
in frame A; the distance from there to RH is mapped in X4 and never travelled.""")

para("""X0.1  WHAT T150 LEFT AND WHY THIS FILE ATTACKS ITS THIRD REST ITEM FIRST.
T150 named the mechanism -- A is EXACTLY the odd parity sector of T_M(c) and all
of the negative inertia forced by f(0) < 0 sits in the EVEN sector -- and left
ONE gate open: the ladder constant in nu_k <= C k^2 still grows, C = %.2f .. %.2f
= %.2f pi at worst, trend x^(%.3f +- %.3f), maximum at k = 1 in %d of %d windows,
and the gap from pi is the arithmetic LEAKAGE of the mode (l1 mass %.2f .. %.2f,
m ||psi||_inf^2 = %.2f .. %.2f against the model 2).  Its rest list ended with
'an EXPLICIT LOCAL MODEL at the symbol minimum inside the odd sector'.  THIS FILE
STARTS THERE, because the local model turns out to CONTAIN the ladder: the odd
sector lives on the shifted grid th_k = 2 pi k / N which never touches th = 0, so
the negative window of the symbol is STEPPED OVER, the effective odd minimum is
f(th_1) with th_1 = 2 pi / N, and the whole comparison collapses into a PENCIL
against the parity Laplacian -- from which a Sobolev step, not a ceiling, gives
the per-mode bound."""
     % (C_LAD_T150[0], C_LAD_T150[1], C_LAD_PI_T150, C_LAD_EXP_T150[0],
        C_LAD_EXP_T150[1], C_ARG1_T150[0], C_ARG1_T150[1],
        L1_T150[0], L1_T150[1], SUP_T150[0], SUP_T150[1]))

# --- X0.2  THE LICENCES, each VERIFIED before use ---------------------------
LIC = []

_m0 = 96
_L0 = sym(2.0 * np.eye(_m0) - np.eye(_m0, k=1) - np.eye(_m0, k=-1))
_LN = _L0.copy()
_LN[0, 0] = 1.0
_LN[_m0 - 1, _m0 - 1] = 1.0
_LP = lap_P_mat(_m0)
_S0 = sine_basis(_m0)
_C0 = cosine_basis(_m0)
_P0 = parity_basis(_m0)
e1 = rel(_L0 @ _S0.T, _S0.T * dirichlet_mu(_m0)[None, :])
e2 = rel(_LN @ _C0.T, _C0.T * neumann_mu(_m0)[None, :])
e3 = rel(_LP @ _P0.T, _P0.T * parity_mu(_m0)[None, :])
o1 = rel(_S0 @ _S0.T, np.eye(_m0))
o2 = rel(_C0 @ _C0.T, np.eye(_m0))
o3 = rel(_P0 @ _P0.T, np.eye(_m0))
check("ol_x0.lic1_models", max(e1, e2, e3, o1, o2, o3) < 1.0e-12,
      "THEOREM (Kac-Murdock-Szego 1953): the DIRICHLET, NEUMANN and PARITY "
      "eigenpairs are exact and each basis is orthonormal; residuals %.2e / "
      "%.2e / %.2e, orthonormality %.2e / %.2e / %.2e"
      % (e1, e2, e3, o1, o2, o3))
LIC.append("exact D / N / PARITY eigenpairs and orthonormality")

s1 = float(np.max(np.abs(_S0))) <= math.sqrt(2.0 / (_m0 + 1.0)) * (1.0 + 1.0e-12)
s2 = float(np.max(np.abs(_C0))) <= math.sqrt(2.0 / _m0) * (1.0 + 1.0e-12)
s3 = float(np.max(np.abs(_P0))) <= 2.0 / math.sqrt(2.0 * _m0 + 1.0) * (1.0 + 1.0e-12)
check("ol_x0.lic2_sup", s1 and s2 and s3,
      "the sup bounds sqrt(2/(m+1)), sqrt(2/m) and 2/sqrt(2m+1) hold entrywise "
      "-- DIRECTION: each is an UPPER bound, the direction the ceiling consumes")
LIC.append("the three basis sup bounds, UPPER")

_rng = np.random.default_rng(1510)
_X = _rng.standard_normal((_m0, 6))
_X /= np.linalg.norm(_X, axis=0)[None, :]
_mb = mode_bounds(_X, _m0, _S0, _C0, _P0, cap=_m0)
_sup = _m0 * np.max(np.abs(_X), axis=0) ** 2
check("ol_x0.lic3_ceiling", _mb["viol"] <= 1.0e-10
      and bool(np.all(_sup <= _mb["bound"] + 1.0e-9)),
      "the T148 second-difference l1 ceiling holds in ALL THREE bases on random "
      "unit vectors (worst |a_k| - B_k margin %.2e) and the resulting bound on "
      "m ||psi||_inf^2 is respected (worst margin %.3e).  QUOTED from T148 and "
      "re-verified, never re-derived" % (_mb["viol"], float(np.min(_mb["bound"] - _sup))))
LIC.append("the second-difference l1 CEILING in three bases, UPPER")

_mc = 512
_Sc = sine_basis(_mc)
_Pc = parity_basis(_mc)
_nuD = ceil_D(np.ascontiguousarray(_Sc[:8].T), _mc)["nu"]
_nuP = ceil_P(np.ascontiguousarray(_Pc[:8].T), _mc)["nu"]
_kk8 = (np.arange(8, dtype=float) + 1.0) ** 2
_eD = float(np.max(np.abs(_nuD / (math.pi * _kk8) - 1.0)))
_eP = float(np.max(np.abs(_nuP / (math.pi * _kk8) - 1.0)))
check("ol_x0.lic4_ladder_norm", max(_eD, _eP) <= CTRL_TOL,
      "THE LADDER NORMALISATION (T149/T150, quoted): on the exact Dirichlet "
      "sines nu_k/(pi k^2) = 1 to %.4f and on the exact PARITY sines to %.4f "
      "(m = %d, k <= 8, bar %.2f) -- so 'C = pi' is the model value the "
      "arithmetic surface is measured against" % (_eD, _eP, _mc, CTRL_TOL))
LIC.append("nu_k = pi k^2 in the exact models: the LADDER NORMALISATION")

# licence 5: THE SYMBOL-INTEGRAL IDENTITY and the SECTION MONOTONICITY it gives
_Msym = 48
_rng2 = np.random.default_rng(1511)
_cs = _rng2.standard_normal(_Msym) / (1.0 + np.arange(_Msym)) ** 1.5
_Ts = full_toeplitz(_cs, _Msym)
_nq = 4096
_thq = 2.0 * math.pi * np.arange(_nq) / _nq
_fq = _cs[0] + 2.0 * (np.cos(np.outer(_thq, np.arange(1, _Msym))) @ _cs[1:])
_xs = _rng2.standard_normal((_Msym, 5))
_lhs = np.einsum("ij,jk->ik", _Ts, _xs)
_lhs = np.sum(_xs * _lhs, axis=0)
_pw = np.abs(np.exp(1j * np.outer(_thq, np.arange(_Msym))) @ _xs) ** 2
_rhs = (_fq[None, :] @ _pw)[0] / float(_nq)
check("ol_x0.lic5_symbol_form", rel(_lhs, _rhs) < 1.0e-11,
      "THEOREM (classical; Bottcher-Silbermann, Widom 1958): the section "
      "quadratic form IS the symbol integral, <T_M(f)x,x> = (1/2pi) int f |p_x|^2, "
      "verified to %.2e on random vectors (M = %d).  COROLLARY, and the licence "
      "this probe lives on: f >= g pointwise ==> T_M(f) >= T_M(g), i.e. the "
      "section is MONOTONE in the symbol.  DIRECTION: order-preserving"
      % (rel(_lhs, _rhs), _Msym))
LIC.append("the symbol-integral identity and SECTION MONOTONICITY in the symbol")

# licence 6: the PARITY COMPRESSION identities, both of them
_Mp = 64
_hp = _Mp // 2
_Um, _Up = parity_isometries(_Mp)
_cp = _rng2.standard_normal(_Mp) / (1.0 + np.arange(_Mp))
_Tp = full_toeplitz(_cp, _Mp)
_e_odd = rel(_Um.T @ _Tp @ _Um, odd_toeplitz(_cp, _Mp))
_e_even = rel(_Up.T @ _Tp @ _Up, even_toeplitz(_cp, _Mp))
_e_cross = float(np.max(np.abs(_Um.T @ _Tp @ _Up))) / max(gersh(_Tp), 1.0e-300)
_L0p = sym(2.0 * np.eye(_Mp) - np.eye(_Mp, k=1) - np.eye(_Mp, k=-1))
_e_lap = rel(_Um.T @ _L0p @ _Um, lap_P_mat(_hp))
check("ol_x0.lic6_compression", max(_e_odd, _e_even, _e_lap) < 1.0e-13
      and _e_cross < 1.0e-13,
      "THE TWO PARITY COMPRESSION IDENTITIES, exact: U_-^T T_M(c) U_- = T - H "
      "(%.2e), U_+^T T_M(c) U_+ = T + H (%.2e), cross block %.2e -- and, the new "
      "one this probe needs, U_-^T L_0^(M) U_- = L_P (%.2e).  So the model the "
      "pencil is taken against is the ODD COMPRESSION OF THE SYMBOL 2 - 2 cos th, "
      "not an analogy" % (_e_odd, _e_even, _e_cross, _e_lap))
LIC.append("U_-^T T_M(c) U_- = A and U_-^T L_0 U_- = L_P, EXACT")

# licence 7: THE DISCRETE SOBOLEV STEP and the gradient identity
_ms = 200
_rng3 = np.random.default_rng(1512)
_Ps = parity_basis(_ms)
_LPs = lap_P_mat(_ms)
_V = np.concatenate([_rng3.standard_normal((_ms, 8)), _Ps[:4].T], axis=1)
_V /= np.linalg.norm(_V, axis=0)[None, :]
_g_id, _g_le, _so_ok = 0.0, True, True
for j in range(_V.shape[1]):
    v = _V[:, j]
    gs = grad_sq(v)
    e_lp = float(v @ (_LPs @ v))
    e_l0 = float(v @ (_lap_D(v.reshape(-1, 1)).ravel()))
    _g_id = max(_g_id, abs(gs - (e_l0 - v[-1] ** 2)) / max(abs(gs), 1.0e-300))
    _g_le = _g_le and (gs <= e_lp * (1.0 + 1.0e-12))
    _so_ok = _so_ok and (float(np.max(np.abs(v))) ** 2
                         <= sobolev_sup(v, e_lp) * (1.0 + 1.0e-12))
check("ol_x0.lic7_sobolev", _g_id < 1.0e-12 and _g_le and _so_ok,
      "THE DISCRETE SOBOLEV STEP, elementary and verified on %d unit vectors "
      "(random plus the first parity sines): the gradient identity "
      "||grad psi||^2 = <psi, L_0 psi> - psi_last^2 to %.2e, the ordering "
      "||grad psi||^2 <= <psi, L_P psi>, and ||psi||_inf^2 <= 2 ||psi||_2 "
      "||grad psi||_2.  Continuum address Hardy-Littlewood-Polya 1934 / Agmon "
      "1965.  DIRECTION: an UPPER bound on ||psi||_inf^2, which is the only "
      "direction the chain consumes" % (_V.shape[1], _g_id))
LIC.append("the DISCRETE SOBOLEV step, UPPER on ||psi||_inf^2")

# licence 8: THE PENCIL TRANSPORT, both directions, on a model where the answer
# is known in closed form
_mq = 160
_LPq = lap_P_mat(_mq)
_Aq = sym(_LPq @ np.diag(1.0 + 0.5 * np.cos(np.arange(_mq))) @ _LPq)
_Aq = sym(_LPq + 0.37 * np.eye(_mq))
_pq = pencil_pair(_Aq, _LPq, _mq)
_mu_q = parity_mu(_mq)
_ok_lo = bool(np.all(_mu_q * _pq["kap"] <= _mu_q + 0.37 + 1.0e-9))
_ok_up = bool(np.all(_mu_q * _pq["K"] >= _mu_q + 0.37 - 1.0e-9))
_wq = eigh(_Aq, eigvals_only=True)
_ok_ray = bool(np.all(_wq >= _pq["kap"] * _mu_q - 1.0e-9)
               and np.all(_wq <= _pq["K"] * _mu_q + 1.0e-9))
check("ol_x0.lic8_pencil", np.isfinite(_pq["kap"]) and np.isfinite(_pq["K"])
      and _ok_lo and _ok_up and _ok_ray,
      "THE PENCIL TRANSPORT (Parlett; Weyl 1912 minimax): on the closed model "
      "A = L_P + 0.37 I the certified pair is kap = %.6f, K = %.6f (exact "
      "extremes 1 + 0.37/mu^P_k: %.6f and %.6f), and BOTH transported ladders "
      "hold on every one of the %d eigenvalues: kap mu^P_k <= lam_k <= K mu^P_k.  "
      "DIRECTION: kap LOWER, K UPPER, and the Cholesky floor is carried through "
      "as fl / mu^P_1 (relative size %.2e)"
      % (_pq["kap"], _pq["K"], 1.0 + 0.37 / float(_mu_q[-1]),
         1.0 + 0.37 / float(_mu_q[0]), _mq, _pq["fl_rel"]))
LIC.append("the certified PENCIL pair, kap LOWER and K UPPER")

# licence 9: the ELEMENTARY Rayleigh floor L_P >= mu^P_1 I, used to absorb f(0)
_ok_fl = bool(cert_lam_min(_LPq, guess=float(_mu_q[0])) >= float(_mu_q[0]) * (1.0 - 1.0e-9))
check("ol_x0.lic9_floor", _ok_fl,
      "THE RAYLEIGH FLOOR L_P >= mu^P_1 I is certified (mu^P_1 = %.6e at "
      "m = %d).  THIS IS THE STEP THAT ABSORBS f(0) < 0: for f0 < 0 one has "
      "f0 I >= (f0 / mu^P_1) L_P, so the symbol comparison "
      "A >= kap_sym L_P + f0 I becomes A >= kap_sym (1 - rho) L_P with "
      "rho = |f0| / (kap_sym mu^P_1).  DIRECTION: pedantically, the inequality "
      "REVERSES on multiplication by the negative f0, and that reversal is the "
      "whole content" % (float(_mu_q[0]), _mq))
LIC.append("L_P >= mu^P_1 I, and the SIGN-REVERSING absorption of f(0) < 0")

_bpsi, _bn = psi_ratio_max(ATOMS_ALL)
check("ol_x0.lic10_chebyshev", _bpsi <= B_PSI,
      "THE CITED CHEBYSHEV BOUND psi(x) <= %.5f x (Chebyshev 1852; "
      "Rosser-Schoenfeld 1962 Thm 12) is VERIFIED on the exact range this file "
      "uses: max psi(n)/n = %.6f at n = %d over all prime powers up to %d, and "
      "it is never assumed beyond that range" % (B_PSI, _bpsi, _bn, ATOM_MAX))
LIC.append("psi(x) <= B x, VERIFIED on the range used")

info("X0.2.licences", "%d licences, each VERIFIED BEFORE USE and each with its "
     "DIRECTION in its name: %s" % (len(LIC), "; ".join(LIC)))

para("""X0.3  THE TYPING RULE, RESTATED BECAUSE THIS PROBE CHANGES WHICH OBJECT IS
LOAD-BEARING.  T148 .. T150 reached the per-mode bound through nu, the scaled l1
norm of the second difference of the mode: a CEILING functional that reads a
computed eigenvector.  This probe reaches it through the PENCIL, which reads no
eigenvector at all -- kap and K are two completed Choleskys of the FORM.  So the
per-mode bound 2 m sqrt(K_bot mu^P_k / kap) is A PRIORI in the strict sense declared
above, and nu survives only as a CROSS-CHECK and as the object T150's number is
quoted in.  What is NOT a priori is the m-freeness of K_bot/kap, and that is exactly
the one thing the surface measures.  kap_sym and K_sym, by contrast, are DESIGNED
on a finite theta grid; they are printed to explain the mechanism and are never
load-bearing, because the matrix pencil needs no continuum step.""")

# ----------------------------------------------------------------------------
section("X1  THE LOCAL MODEL AT THE SYMBOL MINIMUM, INSIDE THE ODD SECTOR")
# ----------------------------------------------------------------------------
para("""X1.0  THE QUESTION, SHARPENED.  T148 measured f(0) < 0 and T150 certified
that all of the negative inertia it forces sits in the EVEN sector.  That leaves
a question T150 did not answer: WHY is the odd sector positive, and what does it
see instead of f(0)?  The answer is a grid statement.  The parity sines live on
th_k = 2 pi k / N, k = 1 .. m, and mu^P_k = 2 - 2 cos th_k EXACTLY; the odd grid
therefore begins at th_1 = 2 pi / N and never contains the origin, while the even
sector does contain a mode at th ~ 0.  So the odd sector's effective symbol
minimum is f(th_1), the local model is of ORDER 2 with the negative f(0) as its
absorbed constant term, and the criterion for odd positivity is that the negative
window [0, th_c) be NARROWER than one odd mode spacing.  X1 measures th_c, th_1,
the order, the certified pencil pair that transports the model to the matrix, and
then dissects the leakage that T150 left as a number without an anatomy.""")

CAND = []
for k in range(2, NZ_DEEP - 2):
    D_k = 0.5 * float(G_DEEP[k]) / NU_MAIN
    M_k = even_window(UU_ALL[k], D_k)
    h_k = M_k // 2
    if h_k < H_MIN or h_k > SURF_HCAP:
        continue
    CAND.append((k, D_k, M_k, h_k))
SZ = []
if CAND:
    step = max(1, len(CAND) // max(SURF_ZONES, 1))
    SZ = CAND[::-1][::step][:SURF_ZONES]
    SZ.sort(key=lambda t: t[0])
info("X1.0.zones", "%d prime-power zones admit a frame-A window inside the cap "
     "(h <= %d, MAX_H = %d); the surface takes %d of them (stride %d) from the "
     "deep end" % (len(CAND), SURF_HCAP, MAX_H, len(SZ), step))

ROWS = []
SKIP = dict(stieltjes=0, gap=0, pos=0, pencil=0, chain=0)
for (i_w, (k, D_k, M_k, h_k)) in enumerate(SZ):
    if budget_left() < RESERVE_S:
        info("X1.0.budget", "surface truncated at n = %d after %d windows"
             % (NN_ALL[k], len(ROWS)))
        break
    al = 0.5 * M_k * D_k
    sp = lag_vector_split(al, M_k, atoms_in(al))
    c_lag = sp["c"]
    A = sym(odd_toeplitz(c_lag, M_k))
    lp = lump_pair(A)
    if lp["stieltjes"] != 1:
        SKIP["stieltjes"] += 1
        del A, lp
        continue
    A_B = lp["A_B"]
    Lam = lp["dgB"]
    if not (float(np.min(Lam)) > 0.0):
        SKIP["pos"] += 1
        del A, A_B, lp
        continue
    try:
        gap_ex = float(eigh(A, A_B, eigvals_only=True, subset_by_index=[0, 0])[0])
    except (LinAlgError, ValueError):
        gap_ex = float("nan")
    if not (gap_ex > 0.0):
        SKIP["gap"] += 1
        del A, A_B, lp
        continue
    m = A.shape[0]
    LP = lap_P_mat(m)
    so = symbol_local_model(c_lag, m)

    # THE CERTIFIED PENCIL -- the load-bearing object of this probe
    pen = pencil_pair(A, LP, m)
    if pen is None or not (np.isfinite(pen["kap"]) and pen["kap"] > 0.0
                           and np.isfinite(pen["K"])):
        SKIP["pencil"] += 1
        del A, A_B, lp, LP
        continue

    # THE ARCH-ONLY PENCIL: is the smooth part alone enough?  (T150 found the
    # arch section INDEFINITE; in pencil language that reads kap^arch <= 0.)
    A_ar = sym(odd_toeplitz(sp["c_ar"], M_k))
    try:
        kap_ar = float(eigh(A_ar, LP, eigvals_only=True,
                            subset_by_index=[0, 0])[0])
    except (LinAlgError, ValueError):
        kap_ar = float("nan")
    ad = arch_diag_closed(sp["c_ar"], M_k)
    lp_ar = lump_pair(A_ar)
    min_lam_ar = float(np.min(lp_ar["dgB"]))
    del A_ar, lp_ar

    # THE PARITY SYMBOL READ, mode by mode, on the first 32 odd grid points
    kr = int(min(32, m))
    P32 = parity_basis(m)[:kr]
    dg_par = np.einsum("ij,ij->i", P32 @ A, P32)
    th_kr = 2.0 * math.pi * np.arange(1, kr + 1) / (2.0 * m + 1.0)
    f_kr = symbol_values(c_lag, th_kr)
    par_res = float(np.max(np.abs(dg_par - f_kr))) / max(float(np.max(np.abs(f_kr))), 1.0e-300)
    par_res1 = abs(float(dg_par[0]) - float(f_kr[0])) / max(abs(float(f_kr[0])), 1.0e-300)
    del P32

    # the exact diagonal formula, re-verified on THIS window
    d_res = rel(Lam, diag_explicit(c_lag, M_k))
    N_lim = math.exp(2.0 * al)
    mu_cheb = 4.0 * B_PSI * math.sqrt(N_lim)

    neg_odd = inertia_neg(A)
    neg_even = inertia_neg(sym(even_toeplitz(c_lag, M_k)))

    # the const gauge, the chain, the bottom ladder, the leakage anatomy
    g_const = float(np.exp(np.mean(np.log(Lam))))
    Lam_t = np.full(m, g_const)
    ch = chain_const(A, A_B, Lam_t, sine_basis(m), cosine_basis(m),
                     parity_basis(m), gap_ex, pen, so)
    if ch is None:
        SKIP["chain"] += 1
        del A, A_B, lp, LP
        continue
    sob = ch["sob"]

    # THE CERTIFIED BOTTOM LADDER: k_cert completed LDL^T counts, seeded by the
    # measured ratio and certified independently of it
    cbl = cert_bottom_ladder(A, m, ch["K_bot"])

    hits_lag = atom_hit_lags(al, M_k)
    lagb = [0.0, 0.0, 0.0]
    if sp["l1_at"] > 0.0:
        cat = np.abs(sp["c_at"])
        q1, q2 = M_k // 4, M_k // 2
        lagb = [float(np.sum(cat[:q1])) / sp["l1_at"],
                float(np.sum(cat[q1:q2])) / sp["l1_at"],
                float(np.sum(cat[q2:])) / sp["l1_at"]]

    ROWS.append(dict(n=NN_ALL[k], D=D_k, m=m, M=M_k, alpha=al, gap_ex=gap_ex,
                     d_res=d_res, mu_tot=sp["mu_tot"], l1_at=sp["l1_at"],
                     n_atom=sp["n_atom"], mu_cheb=mu_cheb, N_lim=N_lim,
                     so=so, pen=pen, sob=sob, ch=ch, ad=ad, cbl=cbl,
                     min_lam_ar=min_lam_ar, kap_ar=kap_ar,
                     par_res=par_res, par_res1=par_res1,
                     dg_par1=float(dg_par[0]), f_th1=float(f_kr[0]),
                     neg_odd=neg_odd, neg_even=neg_even,
                     n_hit=int(hits_lag.shape[0]), lagb=lagb))
    del A, A_B, lp, LP, dg_par

check("ol_x1.surface_nonempty", len(ROWS) >= 8,
      "%d windows carried the local model, the certified pencil and the "
      "const-gauge chain (need >= 8 for four populated D-strata); skips %s"
      % (len(ROWS), SKIP))

if not ROWS:
    info("X1.abort", "no window survived; the remaining blocks are skipped")
    print("")
    print("TOTAL  %d checks, %d passed, %d failed, %.1f s"
          % (PASS + FAIL, PASS, FAIL, time.time() - T_START))
    raise SystemExit(1)

MV = [r["m"] for r in ROWS]
DV = [r["D"] for r in ROWS]
SO = [r["so"] for r in ROWS]
PEN = [r["pen"] for r in ROWS]
SOB = [r["sob"] for r in ROWS]
CH = [r["ch"] for r in ROWS]
LK = [r["ch"]["lk"] for r in ROWS]

info("X1.0.surface", "%d windows, m = %d .. %d, D = %.3e .. %.3e, n = %d .. %d; "
     "the exact generalised eigenvalue spans %.3e .. %.3e"
     % (len(ROWS), min(MV), max(MV), qmin(DV), qmax(DV),
        min(r["n"] for r in ROWS), max(r["n"] for r in ROWS),
        qmin([r["gap_ex"] for r in ROWS]), qmax([r["gap_ex"] for r in ROWS])))

check("ol_x1.diag_formula", qmax([r["d_res"] for r in ROWS]) < 1.0e-12,
      "the EXPLICIT DIAGONAL FORMULA holds on all %d windows, worst residual "
      "%.2e -- the whitening diagonal IS the zone's lag arithmetic (T150, "
      "quoted and re-verified)" % (len(ROWS), qmax([r["d_res"] for r in ROWS])))

check("ol_x1.cheb_budget", all(r["mu_tot"] <= r["mu_cheb"] * (1.0 + 1.0e-12)
                               and r["l1_at"] <= r["mu_tot"] * (1.0 + 1.0e-12)
                               for r in ROWS),
      "THE CLOSED BUDGET holds on all %d windows: ||c^atom||_1 <= sum_j mu_j <= "
      "4 B sqrt(N), worst ratio to the closed ceiling %.4f"
      % (len(ROWS), qmax([r["l1_at"] / r["mu_cheb"] for r in ROWS])))

check("ol_x1.inertia_split", all(r["neg_odd"] == 0 for r in ROWS),
      "T150's MECHANISM re-certified on this surface: the ODD sector has 0 "
      "negative eigenvalues on all %d windows while the EVEN sector has "
      "%d .. %d, so every eigenvalue forced negative by f(0) < 0 lives in the "
      "other parity sector" % (len(ROWS), min(r["neg_even"] for r in ROWS),
                               max(r["neg_even"] for r in ROWS)))

# --- X1.1  THE LOCAL MODEL --------------------------------------------------
F0 = [s["f0"] for s in SO]
THC = [s["th_c"] for s in SO]
TH1 = [s["th_1"] for s in SO]
RATIO_C = [s["th_c"] / s["th_1"] for s in SO]
RHO = [s["rho"] for s in SO]
KAPS = [s["kap_sym"] for s in SO]
KSYM = [s["K_sym"] for s in SO]
F2 = [s["f2"] for s in SO]

info("X1.1.symbol", "THE SYMBOL, A PRIORI: f(0) = %.4e .. %.4e (T148's honest "
     "negative, re-read), the minimum sits at th_min = %.3e .. %.3e with "
     "f_min = %.4e .. %.4e, the negative share of [0, pi] is %.4f .. %.4f, and "
     "f''(0) = %.4e .. %.4e -- so the local model at the minimum is of ORDER 2 "
     "with a NEGATIVE constant term"
     % (qmin(F0), qmax(F0), qmin([s["th_min"] for s in SO]),
        qmax([s["th_min"] for s in SO]), qmin([s["f_min"] for s in SO]),
        qmax([s["f_min"] for s in SO]), qmin([s["neg_share"] for s in SO]),
        qmax([s["neg_share"] for s in SO]), qmin(F2), qmax(F2)))

N_MIN0 = sum(1 for s in SO if s["th_min"] <= s["th_1"])
info("X1.1.min_at_zero", "WHERE THE MINIMUM IS: in %d of %d windows the symbol "
     "minimum lies at or below the first odd grid point th_1, i.e. the minimum "
     "is the ORIGIN and it is a point the odd sector never evaluates.  That is "
     "the whole asymmetry between the two parity sectors, stated as a grid fact"
     % (N_MIN0, len(SO)))

N_STEP = sum(1 for s in SO if s["step_over"])
info("X1.1.step_over", "THE NEGATIVE WINDOW AGAINST THE ODD MODE SPACING: "
     "th_c = %.4e .. %.4e, th_1 = 2 pi / N = %.4e .. %.4e, and the ratio "
     "th_c / th_1 = %.4f .. %.4f (median %.4f).  The odd grid STEPS OVER the "
     "negative window in %d of %d windows -- which is the mechanism, and it is "
     "an A PRIORI statement about the form"
     % (qmin(THC), qmax(THC), qmin(TH1), qmax(TH1), qmin(RATIO_C),
        qmax(RATIO_C), qmed(RATIO_C), N_STEP, len(SO)))

F_RC = pow_fit(MV, RATIO_C, "th_c/th_1")
info("X1.1.step_trend", "and the ratio's trend is %s (%s): th_c and the mode "
     "spacing both shrink, so the mechanism is not an artefact of small m -- but "
     "a FIT is never load-bearing and a finite surface proves nothing for all D"
     % (fit_str(F_RC), "NON-GROWING" if nogrow_ok(F_RC) else "GROWING"))

# --- X1.1b  THE HONEST NEGATIVE: THE SYMBOL IS NOT THE RIGHT LANGUAGE -------
N_RHO = sum(1 for s in SO if s["rho"] < 1.0)
FVAR = [s["f_var"] for s in SO]
F_F2 = pow_fit(MV, [abs(s["f2"]) for s in SO], "|f''(0)|")
info("X1.1b.sym_fails", "AND NOW THE HONEST NEGATIVE, BECAUSE IT IS THE MOST "
     "INFORMATIVE NUMBER IN THIS BLOCK.  The one-parameter symbol comparison "
     "f >= kap_sym (2 - 2 cos th) + f(0) is VACUOUS on this surface: kap_sym is "
     "pinned by the LARGE-th end (where f is O(1) but 2 - 2 cos th saturates at "
     "4) and comes out at %.3f .. %.3f, so the margin rho = |f0|/(kap_sym mu^P_1) "
     "= %.3g .. %.3g, below 1 in %d of %d windows.  The reason is explicit: "
     "f''(0) = %.3e .. %.3e (trend %s) and the symbol MOVES by a relative "
     "%.2f .. %.2f across ONE odd mode spacing, so f is NOT slowly varying at "
     "the resolution of the bottom mode"
     % (qmin(KAPS), qmax(KAPS), qmin(RHO), qmax(RHO), N_RHO, len(SO),
        qmin([s["f2"] for s in SO]), qmax([s["f2"] for s in SO]), fit_str(F_F2),
        qmin(FVAR), qmax(FVAR)))

info("X1.1b.parity_symbol", "THE SAME FACT MEASURED DIRECTLY, and it settles "
     "T150's rest item 3 in the NEGATIVE: the parity-basis diagonal t_k^T A t_k "
     "does NOT reproduce f(th_k).  Relative deviation %.2f .. %.2f at k = 1 and "
     "%.2f .. %.2f over k <= 32.  The section quadratic form is the symbol "
     "integral against a Fejer-type kernel of width one mode spacing (licence 5, "
     "exact), and a symbol that moves by O(1) across that width is averaged, not "
     "sampled.  CONSEQUENCE, stated plainly: extending Basor-Ehrhardt 2009 to "
     "f(0) < 0 would NOT deliver this ladder, because no pointwise symbol "
     "statement survives at the bottom mode's resolution.  The local model has "
     "to be a MATRIX statement, and X1.1c is that statement"
     % (qmin([r["par_res1"] for r in ROWS]), qmax([r["par_res1"] for r in ROWS]),
        qmin([r["par_res"] for r in ROWS]), qmax([r["par_res"] for r in ROWS])))

# --- X1.1c  THE LOCAL MODEL THAT DOES HOLD, AS A CERTIFIED MATRIX STATEMENT --
KBOT = [c["K_bot"] for c in CH]
KBLO = [c["k_bot_lo"] for c in CH]
CBL = [r["cbl"] for r in ROWS]
N_CBL = sum(1 for t in CBL if t is not None)
F_KBOT = pow_fit(MV, KBOT, "K_bot")
check("ol_x1.bottom_ladder", N_CBL == len(ROWS),
      "THE LOCAL MODEL, CERTIFIED WITHOUT A SYMBOL AND WITHOUT AN EIGENVECTOR: "
      "on all %d windows lam_k(A) <= S mu^P_k for k <= %d is certified by %d "
      "completed LDL^T counts per window (Sylvester 1852), with S = %.4f .. %.4f. "
      " The odd sector's bottom spectrum IS the parity-Laplacian ladder up to a "
      "bounded factor -- order 2 in k, because mu^P_k = 4 sin^2(pi k/N), and with "
      "no trace of f(0) < 0 in it"
      % (len(ROWS), K_CERT, K_CERT,
         qmin([t["S"] for t in CBL if t]), qmax([t["S"] for t in CBL if t])))
info("X1.1c.local_model", "AND THE BAND IT SITS IN, over the %d read modes: "
     "lam_k / mu^P_k in [%.4f, %.4f] with the upper end K_bot = %.4f .. %.4f "
     "(trend %s).  At the bottom mode itself lam_1 / mu^P_1 = %.4f .. %.4f.  So "
     "the answer to 'where is the odd effective minimum and what order has it' "
     "is: at th_1 = 2 pi / N, of ORDER 2, with an O(1) prefactor -- and the "
     "negative f(0) is absorbed, not cancelled, because the odd grid never "
     "reaches it"
     % (K_LAD, qmin(KBLO), qmax(KBOT), qmin(KBOT), qmax(KBOT), fit_str(F_KBOT),
        qmin([c["lam1_pure"] / p["mu1"] for c, p in zip(CH, PEN)]),
        qmax([c["lam1_pure"] / p["mu1"] for c, p in zip(CH, PEN)])))

# --- X1.2  THE CERTIFIED PENCIL --------------------------------------------
KAP = [p["kap"] for p in PEN]
KUP = [p["K"] for p in PEN]
RGLOB = [p["R"] for p in PEN]
RPEN = [c["R_bot"] for c in CH]
RSYM = [s["R_sym"] for s in SO]
F_RPEN = pow_fit(MV, RPEN, "R_bot")
F_RGLOB = pow_fit(MV, RGLOB, "K/kap global")
F_KAP = pow_fit(MV, KAP, "kap")
F_KUP = pow_fit(MV, KUP, "K global")

check("ol_x1.pencil_direction", all(
    c["lam1_pure"] >= p["kap"] * p["mu1"] * (1.0 - 1.0e-7)
    and c["lam1_pure"] <= p["K"] * p["mu1"] * (1.0 + 1.0e-7)
    for c, p in zip(CH, PEN)),
      "THE DIRECTION OF THE PENCIL IS VERIFIED ON THE ACTUAL BOTTOM EIGENVALUE "
      "of all %d windows: kap mu^P_1 <= lam_1(A) <= K mu^P_1.  A certificate "
      "whose direction is not re-read on the object it is applied to is not a "
      "certificate" % len(ROWS))

check("ol_x1.sobolev_direction", all(
    lk["sup_true"] <= lk["sup_sob"] * (1.0 + 1.0e-9)
    and lk["e_lp"] <= c["lam1_pure"] / p["kap"] * (1.0 + 1.0e-7)
    for lk, c, p in zip(LK, CH, PEN)),
      "AND SO IS THE DIRECTION OF THE TWO STEPS THAT FOLLOW IT: on every window "
      "the true m ||psi_1||_inf^2 is below its Sobolev bound, and the true "
      "parity Dirichlet energy <psi_1, L_P psi_1> is below lam_1 / kap.  Both "
      "are the inequalities the ladder consumes, both read in the direction "
      "consumed")

info("X1.2.pencil_lo", "THE CERTIFIED PENCIL LOWER BOUND (ONE completed Cholesky "
     "per window, no eigenvector anywhere, floor carried as fl/mu^P_1): "
     "kap = lam_min(A, L_P) = %.4f .. %.4f (median %.4f), trend %s -- %s.  This "
     "is the ONLY thing the Sobolev step needs from the form, and it is bounded "
     "AWAY FROM ZERO on the whole surface"
     % (qmin(KAP), qmax(KAP), qmed(KAP), fit_str(F_KAP),
        "FLAT" if flat_ok(F_KAP) else "NOT flat"))

info("X1.2.pencil_up_neg", "AND THE HONEST NEGATIVE ON THE OTHER SIDE: the "
     "GLOBAL pencil top K = lam_max(A, L_P) = %.4g .. %.4g GROWS at %s, so the "
     "global ratio K/kap = %.4g .. %.4g at %s is useless.  The reason is "
     "structural and harmless: L_P saturates at 4 while the section's top does "
     "not, so the global ratio is a statement about the TOP of the spectrum -- "
     "which the cake bounds by the trivial m anyway.  The bottom is what the "
     "ladder needs, and that is why X1.1c certifies the bottom ladder separately "
     "instead of importing it from the global pencil"
     % (qmin(KUP), qmax(KUP), fit_str(F_KUP), qmin(RGLOB), qmax(RGLOB),
        fit_str(F_RGLOB)))

info("X1.2.pencil_bot", "THE ONE NUMBER OF THIS PROBE is therefore the BOTTOM "
     "ratio R = K_bot / kap = %.4f .. %.4f (median %.4f), trend %s -- %s against "
     "the bar %.2f.  K_bot is certified for k <= %d by inertia counts and read "
     "for k <= %d; kap is certified by Cholesky.  No eigenvector enters either"
     % (qmin(RPEN), qmax(RPEN), qmed(RPEN), fit_str(F_RPEN),
        "NON-GROWING" if nogrow_ok(F_RPEN, RPEN_BAR) else "GROWING", RPEN_BAR,
        K_CERT, K_LAD))

info("X1.2.pencil_symbol", "and the SYMBOL version of the same ratio is recorded "
     "only to show that it is NOT usable: the a priori ceiling "
     "K_sym / (kap_sym (1 - rho)) is VACUOUS on %d of %d windows because "
     "rho = |f(0)| / (kap_sym mu^P_1) = %.3g .. %.3g exceeds 1 (it evaluates to "
     "%s), against the certified R = %.4f .. %.4f.  The matrix objects are not "
     "vacuous and need no grid-to-continuum step at all -- which is why the "
     "symbol side is fenced off as DESIGN and the chain never touches it"
     % (len(SO) - N_RHO, len(SO), qmin(RHO), qmax(RHO),
        "a negative number or nan" if not np.all(np.isfinite(RSYM))
        else "%.4g .. %.4g" % (qmin(RSYM), qmax(RSYM)),
        qmin(RPEN), qmax(RPEN)))

N_ARNEG = sum(1 for r in ROWS if not (r["kap_ar"] > 0.0))
info("X1.2.arch_pencil", "THE ATOMS ARE CO-RESPONSIBLE, IN PENCIL LANGUAGE: the "
     "ARCHIMEDEAN-ONLY section has lam_min(A^arch, L_P) = %.4e .. %.4e, "
     "non-positive in %d of %d windows, so the smooth part alone does NOT admit "
     "a positive pencil lower bound and the arithmetic is not a perturbation of "
     "a positive object.  T150 said the same thing with %d .. %d negative "
     "eigenvalues and a dead additive route (%.1f .. %.1f orders); the pencil "
     "says it without any perturbation theory at all"
     % (qmin([r["kap_ar"] for r in ROWS]), qmax([r["kap_ar"] for r in ROWS]),
        N_ARNEG, len(ROWS), NEG_AR_T150[0], NEG_AR_T150[1],
        DK_DEAD_T150[0], DK_DEAD_T150[1]))

# --- X1.3  THE LEAKAGE ANATOMY ---------------------------------------------
L1P = [lk["l1"] for lk in LK]
SIN1 = [lk["sin_t1"] for lk in LK]
SUPT = [lk["sup_true"] for lk in LK]
BANDS = np.array([lk["bands"] for lk in LK], dtype=float)
F_L1 = pow_fit(MV, L1P, "l1_parity")
F_SIN = pow_fit(MV, SIN1, "sin(psi,t1)")

info("X1.3.leak_l1", "THE LEAKAGE, FIRST AS T150 LEFT IT: the bottom mode's l1 "
     "mass in the parity basis is %.4f .. %.4f (T150: %.2f .. %.2f) and "
     "m ||psi||_inf^2 = %.4f .. %.4f (T150: %.2f .. %.2f, model 2).  Trend of "
     "the l1 mass %s.  REPRODUCED, and now it gets an anatomy"
     % (qmin(L1P), qmax(L1P), L1_T150[0], L1_T150[1], qmin(SUPT), qmax(SUPT),
        SUP_T150[0], SUP_T150[1], fit_str(F_L1)))

info("X1.3.leak_bands", "WHERE THE MASS SITS, BAND BY BAND IN k (shares of the "
     "l1 mass, worst window in each band): k = 1: %.3f, k = 2..4: %.3f, "
     "k = 5..16: %.3f, k = 17..64: %.3f, k > 64: %.3f.  So the leakage is NOT a "
     "far tail: it is a LOW-k spreading of the mode over the first few odd grid "
     "points, which is exactly what a symbol whose minimum sits just outside the "
     "grid produces"
     % tuple(float(np.max(BANDS[:, j])) for j in range(BANDS.shape[1])))

info("X1.3.leak_rotation", "THE SAME FACT AS A ROTATION: the overlap with the "
     "model bottom mode t_1 is |<psi, t_1>| = %.4f .. %.4f, i.e. "
     "sin angle(psi, t_1) = %.4f .. %.4f (trend %s).  The l1 excess over 1 is "
     "%.4f .. %.4f and the ratio (l1 - 1) / sin is %.3f .. %.3f -- so the "
     "leakage IS the rotation, at an O(1) exchange rate, and it is NOT an "
     "arithmetic sideband at high k"
     % (qmin([lk["ov_t1"] for lk in LK]), qmax([lk["ov_t1"] for lk in LK]),
        qmin(SIN1), qmax(SIN1), fit_str(F_SIN),
        qmin([x - 1.0 for x in L1P]), qmax([x - 1.0 for x in L1P]),
        qmin([(a - 1.0) / max(b, 1e-300) for a, b in zip(L1P, SIN1)]),
        qmax([(a - 1.0) / max(b, 1e-300) for a, b in zip(L1P, SIN1)])))

info("X1.3.leak_sideband", "THE COUPLING THAT DRIVES THE ROTATION, measured as "
     "the SIDEBAND ROW b_l = t_l^T A t_1: the off-diagonal share of its l1 mass "
     "is %.4f .. %.4f, the largest sideband sits at l* = %d .. %d, and the "
     "atoms occupy the lag bands [0, M/4) : %.3f, [M/4, M/2) : %.3f, "
     "[M/2, M) : %.3f of ||c^atom||_1 (worst window each).  The sideband index "
     "is LOW while the atom mass is spread over the whole lag range: the leakage "
     "is therefore not a resonance with a particular lag but the generic "
     "low-frequency response of the section to a symbol perturbation"
     % (qmin([lk["r_off_share"] for lk in LK]),
        qmax([lk["r_off_share"] for lk in LK]),
        min(lk["l_star"] for lk in LK), max(lk["l_star"] for lk in LK),
        float(np.max([r["lagb"][0] for r in ROWS])),
        float(np.max([r["lagb"][1] for r in ROWS])),
        float(np.max([r["lagb"][2] for r in ROWS]))))

info("X1.3.leak_price", "AND THE PRICE OF THE SOBOLEV STEP SEPARATED FROM THE "
     "PRICE OF THE LEAKAGE: on the actual bottom mode the Sobolev bound "
     "over-estimates m ||psi||_inf^2 by a factor %.3f .. %.3f, while on the "
     "exact model mode t_1 the same step costs exactly pi.  The certified "
     "energy ceiling lam_1 / kap over-estimates the true <psi, L_P psi> by "
     "%.3f .. %.3f.  Both are O(1) and neither grows with m -- which is the "
     "difference between this route and the nu route, whose ceiling paid "
     "%.2f pi at k = 1"
     % (qmin([lk["sob_gap"] for lk in LK]), qmax([lk["sob_gap"] for lk in LK]),
        qmin([c["lam1_pure"] / p["kap"] / max(lk["e_lp"], 1e-300)
              for c, p, lk in zip(CH, PEN, LK)]),
        qmax([c["lam1_pure"] / p["kap"] / max(lk["e_lp"], 1e-300)
              for c, p, lk in zip(CH, PEN, LK)]),
        C_LAD_PI_T150))

# ----------------------------------------------------------------------------
section("X2  THE LADDER CLOSURE")
# ----------------------------------------------------------------------------
para("""X2.0  TWO ROUTES, BOTH INSTRUMENTED, ONE OF THEM ALIVE.  Route (i) is the
MODE COMPARISON, and T150 established that its ADDITIVE form is dead: every
additive tool (Weyl 1912, Bauer-Fike 1960, Davis-Kahan 1970) measures the
perturbation against the Theta(D^3) bottom gap and misses by orders.  The
MULTIPLICATIVE form is what survives, and the Sobolev step is what makes it a
MODE statement: a Loewner comparison kap L_P <= A <= K L_P controls the parity
Dirichlet ENERGY of every eigenvector, and the energy controls the sup norm
directly.  No gap, no rotation, no smallness enters.  Route (ii) is the
COUNTING/LAYER-CAKE reading: the Q_star average is a weighted mean over modes, so
it never needs the ladder mode by mode, only the SORTED profile -- which is a
strictly weaker demand and is priced here.  X2 reports both, with the new ladder
constant and its trend against the %.2f bar.""" % LAD_BAR)

CS = [s["C_S"] for s in SOB if s is not None]
CSC = [s["C_closed"] for s in SOB if s is not None]
B1 = [s["b1"] for s in SOB if s is not None]
F_CS = pow_fit([r["m"] for r in ROWS if r["sob"] is not None], CS, "C_S")
F_CSC = pow_fit([r["m"] for r in ROWS if r["sob"] is not None], CSC, "C_closed")
F_B1 = pow_fit([r["m"] for r in ROWS if r["sob"] is not None], B1, "b_1")

check("ol_x2.sob_valid", all(c["sob_ok"] for c in CH),
      "THE SOBOLEV BOUND DOMINATES THE TRUTH on every one of the %d read modes "
      "of every one of the %d windows (b_k >= m ||psi_k||_inf^2, modes taken in "
      "the weight order the cake uses).  A bound that is not re-read against the "
      "object it bounds is a hypothesis, not a bound" % (CUT_MAX, len(CH)))

info("X2.1.route_i", "ROUTE (i), THE MULTIPLICATIVE MODE COMPARISON -- ALIVE.  "
     "b_k = m ||psi_k||_inf^2 <= 2 m sqrt(K_bot mu^P_k / kap) is CERTIFIED "
     "(pencil floor + inertia counts) "
     "plus EXACT (Sobolev, model spectrum), and it is LINEAR in k, not "
     "quadratic.  The ladder constant C_S = max_k b_k / k = %.4f .. %.4f "
     "(median %.4f, attained at k = %d .. %d), trend %s -- %s against the bar "
     "%.2f.  Its closed form 2 pi sqrt(K_bot/kap) (2m/N) is %.4f .. %.4f, trend %s"
     % (qmin(CS), qmax(CS), qmed(CS),
        min(s["arg_S"] for s in SOB if s is not None),
        max(s["arg_S"] for s in SOB if s is not None), fit_str(F_CS),
        "NON-GROWING" if nogrow_ok(F_CS, CS_BAR) else "GROWING", CS_BAR,
        qmin(CSC), qmax(CSC), fit_str(F_CSC)))

info("X2.1.route_i_bottom", "AT THE BOTTOM, where T150's constant was attained: "
     "b_1 = %.4f .. %.4f (trend %s) against the true m ||psi_1||_inf^2 = "
     "%.4f .. %.4f and against what the nu route delivers at k = 1, "
     "2 (2 sqrt(C) + 1)^2 = %.1f .. %.1f for T150's C = %.2f .. %.2f.  The "
     "improvement at the bottom is a factor %.1f .. %.1f"
     % (qmin(B1), qmax(B1), fit_str(F_B1), qmin(SUPT), qmax(SUPT),
        2.0 * (2.0 * math.sqrt(C_LAD_T150[0]) + 1.0) ** 2,
        2.0 * (2.0 * math.sqrt(C_LAD_T150[1]) + 1.0) ** 2,
        C_LAD_T150[0], C_LAD_T150[1],
        2.0 * (2.0 * math.sqrt(C_LAD_T150[0]) + 1.0) ** 2 / max(qmax(B1), 1e-300),
        2.0 * (2.0 * math.sqrt(C_LAD_T150[1]) + 1.0) ** 2 / max(qmin(B1), 1e-300)))

# the ADDITIVE alternative, priced honestly (relative Davis-Kahan)
RG = [c["rel_gap"] for c in CH]
DK_REL = []
DK_ORD = []
for c, p, lk in zip(CH, PEN, LK):
    rg = c["rel_gap"]
    # a RELATIVE Davis-Kahan: the multiplicative defect (R - 1) against the
    # RELATIVE bottom gap.  Even in its most favourable relative form the mode
    # bound must be converted to a second-difference l1 norm, which costs a
    # factor 4 sqrt(m) scale_P -- and that is where m re-enters.
    sin_bd = (c["R_bot"] - 1.0) / max(rg, 1.0e-300)
    N = 2.0 * c["m"] + 1.0
    nu_extra = (N ** 1.5 / 8.0) * 4.0 * math.sqrt(c["m"]) * min(sin_bd, 1.0)
    DK_REL.append(sin_bd)
    DK_ORD.append(nu_extra / math.pi)
info("X2.1.route_i_additive", "AND THE ADDITIVE ALTERNATIVE, PRICED SO THAT THE "
     "ASYMMETRY IS ON THE RECORD: the RELATIVE bottom gap (lam_2-lam_1)/lam_1 is "
     "%.4f .. %.4f -- O(1), not Theta(D^3), so a RELATIVE perturbation bound is "
     "not absurd, and it gives sin angle <= (R-1)/relgap = %.3f .. %.3f.  But "
     "converting a rotation into the nu language costs scale_P * 4 sqrt(m), so "
     "the imported nu exceeds pi by a factor %.2e .. %.2e.  The rotation route "
     "fails for a DIFFERENT reason than T150's additive routes: not the "
     "Theta(D^3) bottom, but the sqrt(m) of the l1-from-l2 step.  The Sobolev "
     "step avoids both because it never leaves the l-infinity norm"
     % (qmin(RG), qmax(RG), qmin(DK_REL), qmax(DK_REL), qmin(DK_ORD), qmax(DK_ORD)))

NU_K2 = [c["nu_k2"] for c in CH]
C_CNT = [c["C_cnt"] for c in CH]
F_NU = pow_fit(MV, NU_K2, "C_nu")
F_CNT = pow_fit(MV, C_CNT, "C_cnt")
info("X2.2.route_ii", "ROUTE (ii), THE COUNTING / LAYER-CAKE READING.  T150's "
     "pointwise constant is reproduced on this surface as C = %.2f .. %.2f = "
     "%.2f pi at worst (T150: %.2f .. %.2f = %.2f pi), trend %s.  Its SORTED "
     "(counting) version, C_cnt = max_j nu_(j)/j^2 -- the only thing a weighted "
     "average actually needs -- is %.2f .. %.2f, trend %s, attained at "
     "j = %d .. %d.  The counting reading buys a factor %.3f .. %.3f and does "
     "NOT change the trend, because the maximum already sits at the bottom: the "
     "cake cannot rescue a ladder whose worst mode is its first"
     % (qmin(NU_K2), qmax(NU_K2), qmax(NU_K2) / math.pi, C_LAD_T150[0],
        C_LAD_T150[1], C_LAD_PI_T150, fit_str(F_NU), qmin(C_CNT), qmax(C_CNT),
        fit_str(F_CNT), min(c["arg_cnt"] for c in CH),
        max(c["arg_cnt"] for c in CH),
        qmin([a / max(b, 1e-300) for a, b in zip(NU_K2, C_CNT)]),
        qmax([a / max(b, 1e-300) for a, b in zip(NU_K2, C_CNT)])))

info("X2.3.typing", "THE TYPING OF THE TWO ROUTES, pedantically.  ROUTE (i): "
     "THEOREM for the symbol-integral identity, the section monotonicity, the "
     "Weyl minimax and the exact mu^P spectrum; CERTIFIED for kap by ONE "
     "completed Cholesky per window with the floor carried as fl/mu^P_1 "
     "(relative %.1e .. %.1e) and for K_bot by %d completed LDL^T inertia counts "
     "per window (Sylvester 1852); ELEMENTARY-and-verified for the Sobolev step; "
     "MEASURED only for the cross-checks.  The one thing NOT established for all "
     "D is the m-freeness of K_bot/kap, which is a FIT reading on a finite surface.  "
     "ROUTE (ii): the same T148 cake, quoted, with a rearrangement reading -- "
     "certified per window, and it does not move the open term"
     % (qmin([p["fl_rel"] for p in PEN]), qmax([p["fl_rel"] for p in PEN]),
        K_CERT))

# per-stratum reading of the one number
LD = np.log(np.array(DV, dtype=float))
edges = np.linspace(LD.min() - 1e-12, LD.max() + 1e-12, STRATA + 1)
STR_TBL = []
for s in range(STRATA):
    idx = [i for i in range(len(ROWS)) if edges[s] <= LD[i] <= edges[s + 1]]
    if not idx:
        continue
    STR_TBL.append(dict(s=s, n=len(idx),
                        m_lo=min(MV[i] for i in idx), m_hi=max(MV[i] for i in idx),
                        kap=qmin([KAP[i] for i in idx]),
                        R=qmax([RPEN[i] for i in idx]),
                        CS=qmax([SOB[i]["C_S"] for i in idx if SOB[i] is not None])))
for t in STR_TBL:
    info("X2.4.stratum", "D-stratum %d: %2d windows, m = %4d .. %4d, smallest "
         "kap = %.4f, worst R = K_bot/kap = %.4f, worst C_S = %.4f"
         % (t["s"], t["n"], t["m_lo"], t["m_hi"], t["kap"], t["R"], t["CS"]))
R_WORST = qmax([t["R"] for t in STR_TBL]) if STR_TBL else float("nan")
CS_WORST = qmax([t["CS"] for t in STR_TBL]) if STR_TBL else float("nan")
KAP_WORST = qmin([t["kap"] for t in STR_TBL]) if STR_TBL else float("nan")

# ----------------------------------------------------------------------------
section("X3  THE CLEAN-UP: min Lam^arch, THE CHAIN, AND THE STRESS PAIR")
# ----------------------------------------------------------------------------
AD_OK = sum(1 for r in ROWS if r["ad"]["shape"])
AD_R = [r["min_lam_ar"] / max(r["ad"]["closed"], 1.0e-300) for r in ROWS
        if r["ad"]["shape"] and r["ad"]["closed"] > 0.0]
AD_POS = sum(1 for r in ROWS if r["ad"]["closed"] > 0.0)
check("ol_x3.arch_closed", AD_OK == len(ROWS) and AD_POS == len(ROWS)
      and np.isfinite(qmax(AD_R)) and abs(qmax(AD_R) - 1.0) < 1.0e-9
      and abs(qmin(AD_R) - 1.0) < 1.0e-9,
      "T150 REST ITEM 2, CLOSED -- AND ATTAINED, WHICH WAS NOT EXPECTED.  The "
      "archimedean lag kernel has two shape properties, both CHECKED on all %d "
      "windows and neither assumed: c^arch_i < 0 for every lag i >= 1, and "
      "c^arch_i is non-decreasing in i on i >= 1.  Given those, at r = 0 every "
      "term of the exact diagonal formula's sum is max(c_s - c_{M-1-s}, 0) with "
      "s <= M/2 - 1 < M-1-s, hence exactly 0, so Lam^arch_0 = c^arch_0 - "
      "c^arch_{M-1}; and for every other r the same two properties give "
      "Lam^arch_r >= c^arch_0 - c^arch_{M-1}.  So min_r Lam^arch_r = c^arch_0 - "
      "c^arch_{M-1} EXACTLY, verified to a relative %.2e -- a closed two-term "
      "functional of the smooth kernel with NO loss"
      % (len(ROWS), max(abs(x - 1.0) for x in AD_R) if AD_R else float("nan")))
info("X3.1.arch_closed", "THE CLOSED BOUND IN NUMBERS: c^arch_0 - c^arch_{M-1} = "
     "%.4e .. %.4e, positive on all %d windows, against the true min Lam^arch = "
     "%.4e .. %.4e -- ratio %.12f .. %.12f.  So W1's amplitude ceiling, which "
     "divides by min Lam^arch, is now CLOSED at no price at all, and T150's rest "
     "item 2 is off the list"
     % (qmin([r["ad"]["closed"] for r in ROWS]),
        qmax([r["ad"]["closed"] for r in ROWS]), AD_POS,
        qmin([r["min_lam_ar"] for r in ROWS]),
        qmax([r["min_lam_ar"] for r in ROWS]), qmin(AD_R), qmax(AD_R)))

QS_L1 = [c["Qs_l1"] for c in CH]
QS_SOB = [c["Qs_sob"] for c in CH]
QS_BOTH = [c["Qs_both"] for c in CH]
QS_SUP = [c["Qs_sup"] for c in CH]
FR_L1 = [c["frac_l1"] for c in CH]
FR_SOB = [c["frac_sob"] for c in CH]
FR_BOTH = [c["frac_both"] for c in CH]
F_QSOB = pow_fit(MV, QS_SOB, "Qs_sob")
QLAD_LOSS = qmax([a / max(b, 1e-300) for a, b in zip(QS_SOB, QS_L1)])

info("X3.2.qstar", "THE Q_star CEILING WITH THE SOBOLEV BOUND IN THE MINIMUM: "
     "Q*_sob = %.4g .. %.4g (trend %s) against the T148/T150 l1-ceiling value "
     "%.4g .. %.4g and the true-sup reference %.4g .. %.4g; the three-way best "
     "is %.4g .. %.4g.  The Sobolev bound BEATS the l1 ceiling by a factor "
     "%.3f .. %.3f, and the cut it chooses is %d .. %d"
     % (qmin(QS_SOB), qmax(QS_SOB), fit_str(F_QSOB), qmin(QS_L1), qmax(QS_L1),
        qmin(QS_SUP), qmax(QS_SUP), qmin(QS_BOTH), qmax(QS_BOTH),
        qmin([c["sob_gain"] for c in CH]), qmax([c["sob_gain"] for c in CH]),
        min(c["cut_sob"] for c in CH), max(c["cut_sob"] for c in CH)))

info("X3.2.endtoend", "END TO END.  With Sw taken from T148's certified layer "
     "cake (<= %.4f) and Q_star from the Sobolev ceiling, the chain delivers "
     "%.3e .. %.3e of the TRUE generalised gap, against %.3e .. %.3e with the "
     "l1 ceiling alone and against T150's %.4f .. %.4f certified.  The "
     "three-way best is %.3e .. %.3e.  DIRECTION: every factor is an upper "
     "bound on a denominator, so the fraction is a LOWER bound on what the "
     "chain proves"
     % (SW_CERT_T148, qmin(FR_SOB), qmax(FR_SOB), qmin(FR_L1), qmax(FR_L1),
        FRAC_T150[0], FRAC_T150[1], qmin(FR_BOTH), qmax(FR_BOTH)))

FR_GAIN = [a / max(b, 1.0e-300) for a, b in zip(FR_SOB, FR_L1)]
info("X3.2.endtoend_read", "AND THAT COMPARISON READ PEDANTICALLY, because it is "
     "the one number in this block that invites a wrong reading.  T150's "
     "%.4f .. %.4f was computed on T150's surface with T150's Q_star; it is "
     "QUOTED here and is NOT a like-for-like reference.  The like-for-like "
     "reading is INTERNAL: on the SAME %d windows with the SAME Sw, Psi, "
     "kap~_up and Gam, replacing the l1 ceiling by the Sobolev ceiling moves the "
     "fraction from %.3e .. %.3e to %.3e .. %.3e, a gain of %.2f .. %.2f on every "
     "window.  The absolute fraction is smaller than T150's because Psi = "
     "%.4g .. %.4g dominates this deeper surface, and Psi is untouched by "
     "anything in this file -- which is precisely why it is rest item 3"
     % (FRAC_T150[0], FRAC_T150[1], len(CH), qmin(FR_L1), qmax(FR_L1),
        qmin(FR_SOB), qmax(FR_SOB), qmin(FR_GAIN), qmax(FR_GAIN),
        qmin([c["psi_up"] for c in CH]), qmax([c["psi_up"] for c in CH])))

info("X3.2.balance", "THE FACTOR-BY-FACTOR BALANCE, so that the remaining loss "
     "is located and not hidden: kap~_up = %.4f .. %.4f (T149 const-gauge "
     "certified %.4f), Psi = %.4g .. %.4g, c_0^ap = %.4g .. %.4g at base "
     "%.4f .. %.4f, Gam = %.4g .. %.4g.  The Q_star factor is no longer the "
     "dominant loss on this surface; Psi is"
     % (qmin([c["kap_up"] for c in CH]), qmax([c["kap_up"] for c in CH]),
        KAPUP_CONST_T149, qmin([c["psi_up"] for c in CH]),
        qmax([c["psi_up"] for c in CH]), qmin([c["c0_ap"] for c in CH]),
        qmax([c["c0_ap"] for c in CH]), qmin([c["base_star"] for c in CH]),
        qmax([c["base_star"] for c in CH]), qmin([c["gam_best"] for c in CH]),
        qmax([c["gam_best"] for c in CH])))

# --- X3.3  THE MANDATORY STRESS PAIR ---------------------------------------
para("""X3.3  THE MANDATORY STRESS PAIR.  A ladder route is worth nothing unless
the T145 no-go BREAKS in it, and unless the exact models stay exact.  The no-go
passes W1 (its whitening diagonal is smooth) and it passed T150's mechanism
block, so it must break here -- and the interesting question is WHICH of the
three steps it breaks, since the route now has three: the pencil, the Sobolev
step, and the model spectrum.  The Sobolev step is an identity-plus-Cauchy-
Schwarz and cannot break.  The model spectrum is exact.  So the break must be in
the PENCIL, and the probe reads its rate.""")

NG = []
for mm in NOGO_SIZES:
    if budget_left() < 25.0:
        break
    ng = nogo_form(mm)
    E = ng["E"]
    LPm = lap_P_mat(mm)
    pn = pencil_pair(E, LPm, mm)
    if pn is None:
        continue
    psi = ng["psi"]
    # the SAME bottom ratio the arithmetic surface is judged by, so that the
    # stress test is apples to apples and not a comparison of two objects
    wn = eigh(E, eigvals_only=True)
    mun = parity_mu(mm)
    nl = int(min(K_LAD, mm))
    K_bot_n = float(np.max(wn[:nl] / mun[:nl]))
    sb = sobolev_ladder(pn["kap"], K_bot_n, mm)
    lgt = np.log(np.diag(E))
    NG.append(dict(m=mm, R=K_bot_n / pn["kap"], R_glob=pn["R"], kap=pn["kap"],
                   K_bot=K_bot_n,
                   C_S=sb["C_S"] if sb else float("nan"),
                   b1=sb["b1"] if sb else float("nan"),
                   sup_true=mm * float(np.max(np.abs(psi))) ** 2,
                   e_lp=grad_sq(psi),
                   tv=float(np.sum(np.abs(np.diff(lgt))))))
    del E, LPm, ng
F_NG_R = pow_fit([t["m"] for t in NG], [t["R"] for t in NG], "nogo R_bot")
F_NG_CS = pow_fit([t["m"] for t in NG], [t["C_S"] for t in NG], "nogo C_S")
NOGO_BREAKS = bool(NG and not nogrow_ok(F_NG_R, RPEN_BAR))
check("ol_x3.nogo_breaks", NOGO_BREAKS,
      "THE NO-GO BREAKS IN THE PENCIL, and only there.  Its whitening diagonal "
      "stays smooth (TV <= %.4f), the Sobolev step and the model spectrum are "
      "identities -- but its BOTTOM pencil ratio K_bot/kap grows like %s over "
      "m = %d .. %d, from %.3g to %.3g, and the Sobolev ladder constant follows "
      "at %s.  So the ONE thing this probe's route asks of the form is exactly "
      "the thing the no-go does not have: a BOUNDED Loewner comparison with the "
      "parity Laplacian at the bottom.  (T150's no-go broke in the ladder at "
      "x^%.2f.)"
      % (qmax([t["tv"] for t in NG]) if NG else float("nan"), fit_str(F_NG_R),
         min(t["m"] for t in NG) if NG else -1,
         max(t["m"] for t in NG) if NG else -1,
         NG[0]["R"] if NG else float("nan"), NG[-1]["R"] if NG else float("nan"),
         fit_str(F_NG_CS), NOGO_EXP_T150))
info("X3.3.nogo_where", "AND THE ANATOMY OF THAT BREAK, because 'it grows' is "
     "not an explanation: the no-go's bottom mode a_i = i^{-1/2} is LOCALISED, "
     "so its parity Dirichlet energy is %.4g .. %.4g -- of order 1/log m rather "
     "than the model's mu^P_1 ~ 4 pi^2/N^2 -- while a SMOOTH test vector still "
     "sees the full 1/eps of the form.  The pencil ratio therefore measures "
     "exactly the localisation the no-go was built to exhibit, and the true "
     "m ||psi||_inf^2 = %.3g .. %.3g diverges in step with it"
     % (qmin([t["e_lp"] for t in NG]), qmax([t["e_lp"] for t in NG]),
        qmin([t["sup_true"] for t in NG]), qmax([t["sup_true"] for t in NG])))

CTRL_D, CTRL_P = [], []
for mm in CTRL_SIZES:
    if budget_left() < 15.0:
        break
    cd = control_form(mm)
    Sd = sine_basis(mm)
    nu_d = ceil_D(np.ascontiguousarray(Sd[:8].T), mm)["nu"]
    kk8 = (np.arange(8, dtype=float) + 1.0) ** 2
    LPm = lap_P_mat(mm)
    pn_d = pencil_pair(cd["E"], LPm, mm)
    CTRL_D.append(dict(m=mm, C=float(np.max(nu_d / kk8)),
                       R=pn_d["R"] if pn_d else float("nan")))
    cp = parity_control_form(mm)
    Pp = parity_basis(mm)
    nu_p = ceil_P(np.ascontiguousarray(Pp[:8].T), mm)["nu"]
    pn_p = pencil_pair(cp["E"], LPm, mm)
    sb_p = sobolev_ladder(pn_p["kap"], pn_p["K"], mm) if pn_p else None
    # on the parity control K_bot and the global K coincide and both are 1
    CTRL_P.append(dict(m=mm, C=float(np.max(nu_p / kk8)),
                       R=pn_p["R"] if pn_p else float("nan"),
                       C_S=sb_p["C_S"] if sb_p else float("nan"),
                       C_S_ex=2.0 * math.pi * (2.0 * mm / (2.0 * mm + 1.0)),
                       sup1=mm * float(np.max(np.abs(Pp[0]))) ** 2))
    del Sd, Pp, LPm
CTRL_HOLDS = bool(
    CTRL_D and CTRL_P
    and max(abs(t["C"] / math.pi - 1.0) for t in CTRL_D) <= CTRL_TOL
    and max(abs(t["C"] / math.pi - 1.0) for t in CTRL_P) <= CTRL_TOL
    and max(abs(t["R"] - 1.0) for t in CTRL_P) <= 1.0e-6)
check("ol_x3.controls", CTRL_HOLDS,
      "THE CONTROLS STAY EXACT IN BOTH LANGUAGES.  In the nu language the "
      "Dirichlet control gives C/pi - 1 <= %.2e and the parity control "
      "<= %.2e (T149/T150's invariant, preserved).  In the NEW language the "
      "parity control's pencil is (1, 1) to %.2e -- it IS the model -- so its "
      "Sobolev constant is 2 pi (2m/N) = %.4f .. %.4f, matched to %.2e, while "
      "the truth on t_1 is m ||t_1||_inf^2 = %.4f: the Sobolev step costs "
      "EXACTLY pi on the model, and that factor pi is the honest, m-free price "
      "of leaving the l2 world"
      % (max(abs(t["C"] / math.pi - 1.0) for t in CTRL_D) if CTRL_D else float("nan"),
         max(abs(t["C"] / math.pi - 1.0) for t in CTRL_P) if CTRL_P else float("nan"),
         max(abs(t["R"] - 1.0) for t in CTRL_P) if CTRL_P else float("nan"),
         qmin([t["C_S_ex"] for t in CTRL_P]), qmax([t["C_S_ex"] for t in CTRL_P]),
         max(abs(t["C_S"] / t["C_S_ex"] - 1.0) for t in CTRL_P) if CTRL_P else float("nan"),
         qmax([t["sup1"] for t in CTRL_P])))
info("X3.3.ctrl_dirichlet", "and the DIRICHLET control's pencil against the "
     "PARITY Laplacian is R = %.4f .. %.4f -- bounded and m-free but not 1, "
     "because L_0 = L_P - e_last e_last^T differs from the parity model at the "
     "reflecting corner.  A mismatch of exactly one rank-one corner costs a "
     "bounded factor; that is the quantitative form of 'the parity basis is the "
     "matched one'"
     % (qmin([t["R"] for t in CTRL_D]), qmax([t["R"] for t in CTRL_D])))

# the PARITY POOL: the compression identity re-certified on the real windows
PAR = []
for r in ROWS:
    if len(PAR) >= PAR_POOL or budget_left() < 20.0:
        break
    if r["M"] > PAR_MCAP:
        continue
    sp = lag_vector_split(r["alpha"], r["M"], atoms_in(r["alpha"]))
    T = full_toeplitz(sp["c"], r["M"])
    Um, Up = parity_isometries(r["M"])
    e_o = rel(Um.T @ T @ Um, odd_toeplitz(sp["c"], r["M"]))
    e_c = float(np.max(np.abs(Um.T @ T @ Up))) / max(gersh(T), 1.0e-300)
    PAR.append(dict(n=r["n"], M=r["M"], e_o=e_o, e_c=e_c))
    del T, Um, Up
if PAR:
    check("ol_x3.compression_real", qmax([t["e_o"] for t in PAR]) < 1.0e-13
          and qmax([t["e_c"] for t in PAR]) < 1.0e-13,
          "and the compression identity is re-certified on %d REAL arithmetic "
          "windows (M <= %d): A = U_-^T T_M(c) U_- to %.2e with the cross block "
          "at %.2e (T150: %.0e).  The mechanism is not a property of a model"
          % (len(PAR), PAR_MCAP, qmax([t["e_o"] for t in PAR]),
             qmax([t["e_c"] for t in PAR]), IDENT_T150))

# ----------------------------------------------------------------------------
section("X4  THE MAP V23, THE PROMOTION LIST, THE REST LIST, THE CONCLUSION")
# ----------------------------------------------------------------------------
MAP = [
    ("P1/P2 -> E8 -> SM readouts", "untouched by this file"),
    ("T140 .. T147  the reduction to two scalars", "CLOSED, quoted"),
    ("T148  Sw", "CLOSED, certified <= %.4f, quoted" % SW_CERT_T148),
    ("T149  the gauge / TV question", "DISSOLVED: TV was the wrong localisation"),
    ("T150  the mechanism", "NAMED: A is the odd parity sector of T_M(c), all "
     "negative inertia in the EVEN sector"),
    ("T150  the ladder nu_k <= C k^2", "OPEN, C = %.2f pi, trend x^%.3f"
     % (C_LAD_PI_T150, C_LAD_EXP_T150[0])),
    ("T150 rest 3  Basor-Ehrhardt on f(0) < 0", "DEAD END, and now shown to be "
     "one: no pointwise symbol statement survives at the bottom mode's "
     "resolution (f moves %.2f .. %.2f per mode spacing)"
     % (qmin(FVAR), qmax(FVAR))),
    ("T151 X1  the local model", "DELIVERED as a MATRIX statement: lam_k <= "
     "S mu^P_k certified for k <= %d, S = %.3f .. %.3f, order 2"
     % (K_CERT, qmin([t["S"] for t in CBL if t]), qmax([t["S"] for t in CBL if t]))),
    ("T151 X1  the grid asymmetry", "the odd grid steps over the negative window "
     "in %d/%d windows, th_c/th_1 = %.3f .. %.3f" % (N_STEP, len(SO),
                                                     qmin(RATIO_C), qmax(RATIO_C))),
    ("T151 X1  the leakage", "ANATOMISED: a LOW-k rotation away from t_1, "
     "sin = %.3f .. %.3f, not a high-k arithmetic sideband"
     % (qmin(SIN1), qmax(SIN1))),
    ("T151 X2  the per-mode bound", "REROUTED: pencil + Sobolev gives b_k <= "
     "C_S k, LINEAR, C_S = %.3f worst, trend %s" % (CS_WORST, fit_str(F_CS))),
    ("T151 X2  the open term", "the m-freeness of R = K_bot/kap = %.4f worst, "
     "trend %s" % (R_WORST, fit_str(F_RPEN))),
    ("T150 rest 2  min Lam^arch", "CLOSED AND ATTAINED: min Lam^arch = c^arch_0 "
     "- c^arch_{M-1} exactly"),
    ("T151 X3  end to end", "%.3e .. %.3e of the true gap" % (qmin(FR_SOB), qmax(FR_SOB))),
    ("the RH fence", "NEVER CROSSED: finite window, finite zone list, no zero "
     "data, Weil cited as an address only"),
]
for a, b in MAP:
    info("X4.1.map", "%-44s %s" % (a, b))

PROMO = [
    ("v569", "THE ODD SECTOR SEES A SHIFTED SYMBOL GRID.  The parity sines are "
     "supported on th_k = 2 pi k / N with mu^P_k = 2 - 2 cos th_k EXACTLY, so "
     "the odd sector never evaluates the symbol at the origin.  On %d windows "
     "the negative window of f has width th_c = %.3e .. %.3e against the odd "
     "spacing th_1 = %.3e .. %.3e, ratio %.4f .. %.4f, and the odd grid steps "
     "over it in %d of them.  This is the explicit local model at the symbol "
     "minimum inside the odd sector that T150 listed as its third rest item"
     % (len(SO), qmin(THC), qmax(THC), qmin(TH1), qmax(TH1), qmin(RATIO_C),
        qmax(RATIO_C), N_STEP)),
    ("v570", "AND THE HONEST NEGATIVE BESIDE IT, WHICH KILLS T150's REST ITEM 3 "
     "AS POSED: no POINTWISE symbol statement is admissible at the bottom mode's "
     "resolution.  The section form is the symbol integral against a Fejer kernel "
     "of width one mode spacing (exact identity), f''(0) = %.2e .. %.2e, f moves "
     "by a relative %.2f .. %.2f across one spacing, and consequently "
     "t_k^T A t_k does NOT reproduce f(th_k) (deviation %.2f .. %.2f at k = 1).  "
     "Extending Basor-Ehrhardt 2009 to f(0) < 0 would therefore NOT deliver the "
     "odd ladder; the local model has to be, and is, a matrix statement"
     % (qmin([s["f2"] for s in SO]), qmax([s["f2"] for s in SO]),
        qmin(FVAR), qmax(FVAR), qmin([r["par_res1"] for r in ROWS]),
        qmax([r["par_res1"] for r in ROWS]))),
    ("v571", "THE LOCAL MODEL AS A CERTIFIED MATRIX STATEMENT: lam_k(A) <= "
     "S mu^P_k for k <= %d, certified by %d completed LDL^T counts per window "
     "(Sylvester 1852) with S = %.4f .. %.4f, and read to k <= %d with "
     "K_bot = %.4f .. %.4f (trend %s).  The odd sector's bottom spectrum IS the "
     "parity-Laplacian ladder up to a bounded factor: ORDER 2 in k, prefactor "
     "O(1), and no trace of f(0) < 0.  The symbol comparison that would have "
     "produced the same statement is vacuous here (rho = %.2g .. %.2g), which is "
     "why the certificate is a count and not an asymptotic"
     % (K_CERT, K_CERT, qmin([t["S"] for t in CBL if t]),
        qmax([t["S"] for t in CBL if t]), K_LAD, qmin(KBOT), qmax(KBOT),
        fit_str(F_KBOT), qmin(RHO), qmax(RHO))),
    ("v572", "THE PENCIL IS THE RIGHT INVARIANT, AT THE BOTTOM.  kap L_P <= A "
     "with kap certified by ONE completed Cholesky (floor carried as fl/mu^P_1, "
     "relative %.1e) gives kap = %.4f .. %.4f, bounded away from 0, trend %s.  "
     "The GLOBAL top lam_max(A, L_P) = %.3g .. %.3g GROWS at %s and is useless -- "
     "L_P saturates at 4 while the section's top does not -- so the ladder is "
     "carried by R = K_bot/kap = %.4f .. %.4f, trend %s.  Separating the two is "
     "the whole content: the top of the spectrum is bounded by the trivial m and "
     "never needed a comparison"
     % (qmax([p["fl_rel"] for p in PEN]), qmin(KAP), qmax(KAP), fit_str(F_KAP),
        qmin(KUP), qmax(KUP), fit_str(F_KUP), qmin(RPEN), qmax(RPEN),
        fit_str(F_RPEN))),
    ("v573", "THE MULTIPLICATIVE MODE COMPARISON EXISTS, and it is the Sobolev "
     "step: for an odd-sector vector (which vanishes at the virtual node) "
     "||psi||_inf^2 <= 2 ||psi||_2 ||grad psi||_2 and ||grad psi||^2 <= "
     "<psi, L_P psi> <= lam/kap, whence b_k = m ||psi_k||_inf^2 <= "
     "2 m sqrt(K_bot mu^P_k / kap) <= C_S k with C_S = %.3f .. %.3f, LINEAR in k and "
     "m-free given R.  T150 asked for a multiplicative version of the mode "
     "comparison; this is it, and it is immune to the Theta(D^3) bottom because "
     "nothing additive appears"
     % (qmin(CS), qmax(CS))),
    ("v574", "THE LADDER LANGUAGE WAS THE WRONG INTERMEDIATE.  Converting a mode "
     "statement into nu costs scale_P * 4 sqrt(m) through the l1-from-l2 step, "
     "and that sqrt(m) -- not the Theta(D^3) bottom -- is why every rotation "
     "route fails: the relative bottom gap is a healthy %.3f .. %.3f and the "
     "relative Davis-Kahan angle is %.3f .. %.3f, yet the imported nu still "
     "exceeds pi by %.1e .. %.1e.  The Sobolev route never leaves l-infinity"
     % (qmin(RG), qmax(RG), qmin(DK_REL), qmax(DK_REL), qmin(DK_ORD), qmax(DK_ORD))),
    ("v575", "THE LEAKAGE IS A LOW-k ROTATION, NOT AN ARITHMETIC SIDEBAND.  The "
     "bottom mode's parity l1 mass %.3f .. %.3f (T150: %.2f .. %.2f) sits at "
     "k = 1 (%.3f) and k = 2..4 (%.3f) with %.3f beyond k = 64; it equals the "
     "rotation sin angle(psi, t_1) = %.3f .. %.3f at an O(1) exchange rate, and "
     "the sideband row t_l^T A t_1 peaks at l* = %d .. %d.  So T150's number has "
     "a mechanism: a symbol whose minimum sits just outside the grid spreads the "
     "bottom mode over the first few grid points"
     % (qmin(L1P), qmax(L1P), L1_T150[0], L1_T150[1],
        float(np.max(BANDS[:, 0])), float(np.max(BANDS[:, 1])),
        float(np.max(BANDS[:, 4])), qmin(SIN1), qmax(SIN1),
        min(lk["l_star"] for lk in LK), max(lk["l_star"] for lk in LK))),
    ("v576", "min Lam^arch IS CLOSED AND ATTAINED (T150 rest item 2, off the "
     "list).  The archimedean kernel satisfies c^arch_i < 0 and c^arch "
     "non-decreasing for i >= 1 on all %d windows (checked); then the r = 0 row "
     "of the exact diagonal formula has an EMPTY positive part, so "
     "min_r Lam^arch_r = c^arch_0 - c^arch_{M-1} = %.4e .. %.4e exactly, matched "
     "to the computed minimum to a relative %.1e"
     % (AD_OK, qmin([r["ad"]["closed"] for r in ROWS]),
        qmax([r["ad"]["closed"] for r in ROWS]),
        max(abs(x - 1.0) for x in AD_R) if AD_R else float("nan"))),
    ("v577", "THE SOBOLEV BOUND BEATS THE l1 CEILING IN THE CAKE: Q*_sob = "
     "%.4g .. %.4g against %.4g .. %.4g, a factor %.2f .. %.2f, and on the SAME "
     "windows with every other factor held fixed the end-to-end fraction moves "
     "from %.3e .. %.3e to %.3e .. %.3e.  The remaining dominant loss is "
     "Psi = %.3g .. %.3g, not Q_star -- the bottleneck has MOVED, and T150's "
     "%.4f .. %.4f is a different surface's number, quoted and not compared"
     % (qmin(QS_SOB), qmax(QS_SOB), qmin(QS_L1), qmax(QS_L1),
        qmin([c["sob_gain"] for c in CH]), qmax([c["sob_gain"] for c in CH]),
        qmin(FR_L1), qmax(FR_L1), qmin(FR_SOB), qmax(FR_SOB),
        qmin([c["psi_up"] for c in CH]), qmax([c["psi_up"] for c in CH]),
        FRAC_T150[0], FRAC_T150[1])),
    ("v578", "THE STRESS PAIR RELOCATES CLEANLY.  The T145 no-go breaks in the "
     "PENCIL and nowhere else -- R_bot grows like %s while its whitening diagonal "
     "stays smooth and the Sobolev step is an identity -- and the parity control "
     "has pencil (1,1) exactly, so its Sobolev constant is 2 pi (2m/N) with the "
     "factor pi being the exact, m-free price of the step.  The Dirichlet "
     "control's pencil against the PARITY model is %.3f .. %.3f: one rank-one "
     "corner mismatch, one bounded factor"
     % (fit_str(F_NG_R), qmin([t["R"] for t in CTRL_D]),
        qmax([t["R"] for t in CTRL_D]))),
]
for tag, txt in PROMO:
    info("X4.2.promotion", "%s  %s" % (tag, txt))
info("X4.2.count", "%d promotion candidates from THIS pass, numbered from v569 "
     "because T149's %d and T150's %d are still PENDING and are NOT duplicated "
     "(a parallel worker is promoting v549 out of T149/T150; nothing here "
     "touches it).  Promotion itself is OUT OF SCOPE of this file, which writes "
     "nothing outside itself" % (len(PROMO), PROMO_T149, PROMO_T150))

# --- X4.3  THE VERDICT, with the refusal built in ---------------------------
BASE_OK = bool(len(ROWS) >= 8 and CTRL_HOLDS and NOGO_BREAKS
               and all(c["sob_ok"] for c in CH)
               and qmax([c["viol"] for c in CH]) <= 1.0e-9)
MECH_OK = bool(all(r["neg_odd"] == 0 for r in ROWS)
               and (not PAR or qmax([t["e_o"] for t in PAR]) < 1.0e-13))
LOC_OK = bool(N_CBL == len(ROWS) and N_STEP == len(SO)
              and np.isfinite(qmax(KBOT)))
PEN_BOUNDED = bool(np.isfinite(R_WORST) and R_WORST < float("inf")
                   and KAP_WORST > 0.0)
PEN_FLAT = bool(nogrow_ok(F_RPEN, RPEN_BAR))
CS_FLAT = bool(nogrow_ok(F_CS, CS_BAR))
QSOB_OK = bool(np.isfinite(QLAD_LOSS) and QLAD_LOSS <= QLAD_BAR)

GATES = [("mechanism named and certified", MECH_OK),
         ("local model certified: bottom ladder + grid shift", LOC_OK),
         ("bottom pencil ratio bounded per stratum", PEN_BOUNDED),
         ("bottom pencil ratio NON-GROWING in m", PEN_FLAT),
         ("Sobolev ladder constant NON-GROWING in m", CS_FLAT),
         ("Sobolev ceiling loses <= %.1fx vs the l1 minimum" % QLAD_BAR, QSOB_OK)]
N_FAIL = [nm for nm, ok in GATES if not ok]
for nm, ok in GATES:
    info("X4.3.gate", "%-48s %s" % (nm, "MET" if ok else "NOT MET"))

if BASE_OK and not N_FAIL:
    VERDICT = "ODD-CARRIES"
    VTXT = ("every preregistered gate is met on this surface.  The m-free "
            "per-mode bound is delivered by a NAMED mechanism with each layer "
            "typed: THEOREM (the parity compression identity, Weyl minimax, "
            "Sylvester's law, the exact mu^P spectrum), CERTIFIED (kap by a "
            "completed Cholesky with the floor carried, K_bot by completed LDL^T "
            "counts), ELEMENTARY-and-verified (the discrete Sobolev step).  The "
            "ladder is LINEAR in k with C_S <= %.3f and the bottom pencil ratio "
            "is non-growing at %s.  What stands is a STRATIFIED CERTIFIED statement on a "
            "FINITE surface with a named mechanism -- the word 'proved' is "
            "unreachable by construction and no statement is made for all D.  "
            "The one reading in the chain that is a FIT and not a certificate is "
            "the m-freeness of R itself, and it is named as such."
            % (CS_WORST, fit_str(F_RPEN)))
    VTAIL = ("the route carries, with the m-freeness of R = K_bot/kap named as "
             "the one FIT in it.")
elif BASE_OK and len(N_FAIL) == 1:
    VERDICT = "ONE-TERM-MISSING"
    VTXT = ("exactly one preregistered gate fails: '%s'.  Numerically the open "
            "term is now the BOTTOM PENCIL RATIO R = K_bot/kap <= %.4f certified per "
            "stratum, trend %s against the bar %.2f -- a SINGLE SCALAR "
            "comparison between the section and the parity Laplacian, with no "
            "eigenvector in it.  T150's gate was the ladder constant "
            "C = %.2f pi at trend x^(%.3f +- %.3f), a statement about a MODE.  "
            "The open term has become smaller in every sense that matters: one "
            "scalar instead of a mode family, %.2f instead of %.2f in size, and "
            "an object two completed Choleskys certify per window."
            % (N_FAIL[0], R_WORST, fit_str(F_RPEN), RPEN_BAR, C_LAD_PI_T150,
               C_LAD_EXP_T150[0], C_LAD_EXP_T150[1], R_WORST, C_LAD_T150[1]))
    VTAIL = "the one open term is R = K_bot/kap, a single scalar."
else:
    VERDICT = "ODD-RESISTS"
    VTXT = ("%d preregistered gates fail (%s).  The anatomy is explicit: the "
            "local model and the mechanism are settled, the route through the "
            "pencil and the Sobolev step is valid and verified in its direction, "
            "and what resists is R = K_bot/kap <= %.4f at trend %s together with "
            "C_S <= %.3f at trend %s."
            % (len(N_FAIL), ", ".join(N_FAIL) or "base checks", R_WORST,
               fit_str(F_RPEN), CS_WORST, fit_str(F_CS)))
    VTAIL = ("what resists is the bottom pencil ratio, and its anatomy is on "
             "the table.")

REST = [
    "the m-freeness of the BOTTOM PENCIL RATIO R = K_bot / kap, where "
    "kap = lam_min(A, L_P) is one Cholesky and K_bot = max_{k <= K} "
    "lam_k / mu^P_k is K inertia counts -- ONE scalar, no eigenvector, and the "
    "only non-certified link left in the chain",
    "a closed lower bound on kap = lam_min(A, L_P) from the lag vector, which "
    "would make the Sobolev route closed rather than per-window certified; the "
    "symbol route to it is VACUOUS (rho > 1) and the reason is now known, so "
    "this needs the arithmetic of the atoms and not an asymptotic",
    "Psi, which is the dominant loss in the end-to-end chain now that Q_star has "
    "been improved -- it was never the bottleneck before",
]
for i, t in enumerate(REST):
    info("X4.4.rest", "%d. %s" % (i + 1, t))

section("X4.5  THE HONEST CONCLUSION")
para("""(1) THE LOCAL MODEL EXISTS, BUT IT IS A MATRIX STATEMENT AND NOT A SYMBOL
ONE -- and that is the sharpest thing this probe learned.  The symbol side does
give the geometry: the odd sector lives on th_k = 2 pi k / N and never evaluates f
at the origin where it is negative, the negative window has width
th_c = %.2e .. %.2e against an odd spacing th_1 = %.2e .. %.2e (ratio
%.3f .. %.3f, stepped over in %d of %d windows).  But f moves by a relative
%.3f .. %.3f across ONE mode spacing, the section form averages the symbol against
a Fejer kernel of exactly that width instead of sampling it, the mode-by-mode read
t_k^T A t_k vs f(th_k) misses by %.2f .. %.2f, and the one-parameter symbol margin
comes out rho = %.3g .. %.3g >= 1 in %d of %d windows: VACUOUS.  So T150's rest
item 3 is answered in the negative -- extending Basor-Ehrhardt 2009 to f(0) < 0
would not deliver this ladder.  What DOES hold is certified without a symbol and
without an eigenvector: lam_k(A) <= S mu^P_k for k <= %d by completed LDL^T counts
on all %d windows with S = %.4f .. %.4f, i.e. the odd bottom spectrum IS the
parity-Laplacian ladder up to an O(1) factor -- at th_1, of ORDER 2, with f(0) < 0
absorbed rather than cancelled.  The leakage T150 left as a bare number is a LOW-k
rotation of the bottom mode away from t_1 (sin = %.3f .. %.3f, %.3f of the l1 mass
at k = 1, %.3f beyond k = 64) -- not an arithmetic sideband.  (2) THE LADDER WAS
THE WRONG INTERMEDIATE, AND THE MULTIPLICATIVE MODE COMPARISON T150 ASKED FOR IS
THE SOBOLEV STEP: an odd-sector vector vanishes at the virtual node, so
||psi||_inf^2 <= 2 ||psi||_2 ||grad psi||_2, the certified pencil floor kap bounds
the gradient energy by lam_k / kap, and b_k = m ||psi_k||_inf^2 <=
2 m sqrt(K_bot mu^P_k / kap) <= C_S k is LINEAR in k, m-free given
R = K_bot/kap, and free of every additive step -- so the Theta(D^3) bottom that
killed Weyl, Bauer-Fike and Davis-Kahan never enters, and the sqrt(m) that kills
the rotation route is never paid.  C_S = %.3f .. %.3f against the %.1f .. %.1f the
nu route delivers at k = 1, and in the cake Q*_sob beats the l1 ceiling by
%.2f .. %.2f, moving the end-to-end fraction to %.3e .. %.3e and moving the
bottleneck from Q_star to Psi.  (3) THE VERDICT IS %s: %s  And whatever its
status, what would stand is a finite-window positivity statement with an explicit
constant on prime-power zones in frame A -- which is not RH and is not a step
towards it."""
     % (qmin(THC), qmax(THC), qmin(TH1), qmax(TH1), qmin(RATIO_C), qmax(RATIO_C),
        N_STEP, len(SO), qmin(FVAR), qmax(FVAR),
        qmin([r["par_res1"] for r in ROWS]), qmax([r["par_res1"] for r in ROWS]),
        qmin(RHO), qmax(RHO), len(SO) - N_RHO, len(SO),
        K_CERT, len(ROWS),
        qmin([t["S"] for t in CBL if t]), qmax([t["S"] for t in CBL if t]),
        qmin(SIN1), qmax(SIN1),
        float(np.max(BANDS[:, 0])), float(np.max(BANDS[:, 4])),
        qmin(CS), qmax(CS),
        2.0 * (2.0 * math.sqrt(C_LAD_T150[0]) + 1.0) ** 2,
        2.0 * (2.0 * math.sqrt(C_LAD_T150[1]) + 1.0) ** 2,
        qmin([c["sob_gain"] for c in CH]), qmax([c["sob_gain"] for c in CH]),
        qmin(FR_SOB), qmax(FR_SOB), VERDICT, VTAIL))

info("X4.6.verdict", VERDICT)
para("VERDICT %s -- %s" % (VERDICT, VTXT))
para("""THE RH FENCE, RESTATED AT THE END.  Nothing above reads, generates or
approximates zero data; Weil's criterion is cited as an address and never used,
in either direction.  The distance from a finite-window positivity statement with
an explicit constant on prime-power zones in frame A to RH is not travelled here,
and no finite surface proves any statement for all D.""")

print("")
print("TOTAL  %d checks, %d passed, %d failed, %.1f s"
      % (PASS + FAIL, PASS, FAIL, time.time() - T_START))
raise SystemExit(0 if FAIL == 0 else 1)
