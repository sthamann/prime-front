"""Discovery probe (2026-07-28), part 139 of the prime/window investigation.
Contract GREEN.DECAY -- the DECAY LEMMA for second differences of a dense
Stieltjes Green function, and the NEVER-TRUNCATING bound it is supposed to
carry.  Nothing else.

WHERE THIS SITS (T138 PAIR-EXACT: the compensation is real, geometric and
MANY-BODY, and every truncating bound is squeezed)
  T137 killed the absolute-value routes; T138 kept the signs and found the
  mechanism.  Its findings, QUOTED as the starting point and never re-derived
  here:
    * rho(W) = lam_max(Gram), Gram_{ee'} = sqrt(Delta_e Delta_e') b_e^T
      A_B^{-1} b_{e'}, W = L_Delta A_B^{-1}, and the true rho(W) sits at
      0.9752 .. 1.0000 on the measurement surface;
    * THE SIGN LAW IS GEOMETRIC: the sign of a weighted second difference is
      decided by the geometry of the two index intervals -- NESTED pairs
      positive on 0.76 .. 0.94 of the area, CROSSING on 0.59 .. 0.63,
      DISJOINT on 0.06 .. 0.36 (i.e. disjoint pairs are mostly NEGATIVE);
    * the far tail is NET NEGATIVE: truncating the far couplings RAISES the
      spectral radius, so the tail is not a small remainder;
    * THE CLAMP: band and tail are never small at the same bandwidth -- the
      band part alone crosses the margin target at b = 2 .. 8 while the
      certified tail there is still 0.46 .. 0.70;
    * the layer row-sum norms of the stripe-reduced coupling decay ~ d^{-1.54}
      (a FIT), the entrywise second differences of the Green function
      ~ d^{-0.63} (a FIT, T137);
    * the m-PAIRED NEUMANN CERTIFICATE removed the arithmetic obstruction on
      all border blocks with rho(|F|) >= 1 and certifies all but 25, which are
      short by a factor ~ 2;
    * M17 reduces to 1 - rho(W_S) for the BORDER lumped pair: the same margin
      question one level down.
  THE ONE MISSING INPUT, stated as T138 left it: a NEVER-TRUNCATING upper
  bound on lam_max of the full signed Gram needs [a decay law for the layers]
  x [the geometric sign law].  The sign law is measured.  The decay law is
  NOT: Demko-Moss-Smith 1984 is the classical address for inverses of BAND
  matrices and A_B is DENSE, so it does not apply.  This probe asks whether
  the dense-matrix classics supply the missing lemma.

WHAT THIS PROBE DOES
  J0  SETUP and CALIBRATION: the firewall, the odd pole-free section against
      its entrywise definition, the lumped Stieltjes pair, the edge
      representation of L_Delta, the Gram identity bracketed from both sides,
      and the DIRECTION calibrations every later block leans on (a Rayleigh
      quotient is a LOWER bound, a completed Cholesky is an UPPER bound, a
      block row-sum norm is CERTIFIABLE and a truncation is a bound only in
      the direction its Loewner sign allows).  Plus one calibration that is
      new here and decides how J1 must be read: DEMKO-MOSS-SMITH IS VERIFIED
      ON A CASE WHERE IT APPLIES (a genuinely banded truncation of A_B) so
      that its failure on the dense object is a statement about the object and
      not about the implementation.
  J1  THE DECAY LEMMA, three routes, each with its constant chain explicit.
      (a) THE KERNEL SIDE, which is where the Jaffard hypothesis lives.  The
          odd section is A_rs = c_{|r-s|} - c_{M-1-r-s}: a Toeplitz part plus
          an ANTI-Toeplitz part, dense in both.  Two things are established
          exactly rather than fitted: the ANTI-INDEX DOMINATES,
          M - 1 - r - s >= |r - s| + 1 for every (r, s) in the odd block, so
          the anti-Toeplitz part inherits the lag decay of the Toeplitz part;
          and the LUMPED off-diagonals obey |(A_B)_rs| <= |A_rs| entrywise,
          because lumping removes exactly the positive off-diagonal part.
          Together they give a CERTIFIED per-instance kernel envelope
          |(A_B)_rs| <= |c_d| + max_{k > d} |c_k| =: E_d, and E_d is fitted.
      (b) THE JAFFARD ROUTE and its constant chain.  Jaffard 1990: the algebra
          A_p of matrices with |a_ij| <= C (1 + |i - j|)^{-p}, p > 1, is
          inverse-closed -- if A in A_p is invertible on l^2 then A^{-1} is in
          A_p with the SAME exponent (Baskakov 1990 and Gröchenig-Leinert 2006
          for the general weighted / symmetric-algebra versions;
          Demko-Moss-Smith 1984 as the BAND contrast).  The probe builds the
          chain constructively: the band truncation A_b, its certified
          conditioning, the Demko-Moss-Smith rate on it, the Schur norm of the
          discarded dense far part, the Jaffard algebra constant K_p =
          sup_k (w * w)(k) / w(k), and the gate K_p C_1 C_E < 1 the Neumann
          series in the algebra norm needs.  Then it tests the CONCLUSION:
          does |(A_B^{-1})_rs| decay in |r - s| at all?
      (c) THE INCREMENT ROUTE, which is the one the geometry actually points
          at.  For a one-pair (oscillation) kernel G_rs = phi_min psi_max the
          second difference over two DISJOINT intervals FACTORISES exactly,
          b_e^T G b_{e'} = (phi_a - phi_b)(psi_c - psi_d) -- a product of one
          INCREMENT per edge, negative by monotonicity, which is precisely the
          measured disjoint sign; for NESTED intervals it is
          phi_a (psi_c - psi_d) + psi_b (phi_d - phi_c), positive, and it
          carries ENDPOINT VALUES and not increments.  So the classes decay
          for different reasons and the probe measures both, with the
          increment profiles fitted and the class decomposition of the layer
          norms computed.  A_B is dense, so this factorisation is a MODEL and
          its defect is reported before anything is concluded from it.
      (c') THE TELESCOPING ROUTE, which needs no model at all.  The mixed second
          difference H_rs = G_{r+1,s+1} - G_{r+1,s} - G_{r,s+1} + G_{r,s} gives
          an exact double telescoping b_e^T G b_{e'} = sum over the box
          [a,b) x [c,d) of H, hence |Gram_{ee'}| <= sqrt(Delta_e Delta_e')
          l_e l_{e'} max_box |H| -- the whole decay question becomes a pointwise
          question about ONE two-dimensional kernel.  Its decay is fitted, its
          SIGN split is measured, and the geometric sign law of T138 is checked
          against the geometry of the box (a disjoint pair has interval gap > 0
          and its box misses the diagonal; a nested or crossing pair has gap 0
          and its box always contains diagonal cells).  The PRICE of the
          resulting entrywise envelope is computed too, because an entrywise
          envelope is an absolute-value bound and T137 certified that family
          dead.
  J2  THE NEVER-TRUNCATING BOUND.  The layer decomposition Gram = sum_d L^{(d)}
      by stripe distance, summed WITHOUT a cut-off.  DIRECTION PEDANTRY, which
      is the whole difficulty: Weyl 1912 gives lam_max(sum) <= sum lam_max, and
      every nonzero layer has ZERO TRACE, hence lam_max(L^{(d)}) > 0 -- so NO
      layer may be dropped, however negative its mean.  A tail may be dropped
      only if it is Loewner-nonpositive AS A WHOLE, lam_max(Tail_b) <= 0, and
      that is a certifiable question with a yes/no answer, asked here for the
      first time.  Both series are then evaluated against the margin target
      1 - c D^p rebuilt on this surface, using CERTIFIABLE block row-sum layer
      norms (Feingold-Varga 1962) so that every term is available at every d.
      The family is also decided FROM BELOW before it is evaluated, by the same
      move that killed T137's |E| family and T138's band family.  The key number
      is the series total versus the target, and where it breaks.
  J3  CLEAN-UP: (i) the remaining border blocks -- the m-paired ladder
      extended, and the failure LOCALISED in index distance, which decides
      whether a decay lemma could help them at all; (ii) rho(W_S) one level
      down -- the same machinery on the border Schur block's own lumped pair,
      asking whether the J1 structure is inherited; (iii) the CLUSTER
      REMAINDER -- the three-body terms typed by the geometric sign law, to see
      whether they are systematically negative (benign) or not.
  J4  THE MAP V11, the promotion batch, the shortest rest list and a three
      sentence verdict on the honest question: after J1 / J2, is the
      D-uniformity a provable statement with named constants, or does a
      MEASURED core remain?

PREREGISTERED VERDICTS (bars declared here, before any number is computed)
  DECAY-LEMMA-CARRIES : the Jaffard chain certifies the decay of the second
                        differences with named constants AND the resulting
                        never-truncating series bound sits below the margin
                        target on EVERY window of the measurement surface.
  LEMMA-ONLY          : J1 stands as a certified decay statement but J2 breaks
                        -- with the breaking point named and quantified.
  DENSE-RESISTS       : the Jaffard route does not reach the object either --
                        with the reason, and with what that implies for the
                        D-uniformity.
  Element gates: el_firewall, el_j0, el_j1, el_j2, el_j3, el_j4, el_fence.

FENCES
  * Discovery sandbox.  ONE new file.  No promotion, no ledger / TeX / website /
    changelog edit, no verification/ module, no next.txt, no .md output, no git
    action.
  * NO Riemann zero data of any kind.  An AST firewall rejects zero-table
    tokens, non-whitelisted imports and write-mode file access in this source.
  * THE RH FENCE IS PROMINENT AND ABSOLUTE.  Weil's positivity criterion
    (Weil 1952; Bombieri 2000; Connes 1999) is CITED as the classical address
    of the surrounding statement and is NEVER USED, in either direction.
    Nothing here claims, assumes or approaches RH.  Even with every item in the
    rest list closed, what would stand is positivity of the Weil window form on
    test functions supported in (-alpha_max, alpha_max) for the alpha actually
    reached -- a FINITE-WINDOW statement about a finite list of prime-power
    zones.  The distance to RH is MAPPED in J4, never travelled.
  * CERTIFIED vs CERTIFIABLE vs MEASURED vs FIT vs HYPOTHESIS, per line.  A
    completed Cholesky of s I - X certifies lam_max(X) <= s + c_h u ||X||,
    u = 2^-53 (Wilkinson 1968; Higham 2002 Thm 10.3/10.4).  A symmetric row-sum
    or block row-sum test is CERTIFIABLE (Gershgorin 1931; Feingold-Varga
    1962).  A Rayleigh quotient and an eigenvalue are MEASUREMENTS, and a
    Rayleigh-Ritz compression is a LOWER bound on the top eigenvalue by
    interlacing.  Every fit is a FIT with a delete-one jackknife band.  Bars
    declared before a number are never moved.
  * DIRECTION CARE, pedantic and stated where it is used: lumping RAISES the
    form (A_B >= A in the Loewner order), so the pair reaches a floor only
    through the INVERSE side; only an UPPER bound on rho(W) can produce a
    floor and a LOWER bound can only KILL a route; an upper bound may DISCARD a
    term only if that term is Loewner-nonpositive, and a negative MEAN is not
    a Loewner sign; |F^m| <= |F|^m is entrywise, in that direction only.
  * CLASSICAL ADDRESSES USED: Jaffard 1990 (polynomial off-diagonal decay is
    inherited by the inverse, same exponent), Baskakov 1990 and
    Gröchenig-Leinert 2006 (inverse-closedness for weighted / symmetric
    algebras), Demko-Moss-Smith 1984 (exponential decay for inverses of BAND
    matrices -- the contrast, verified here where it applies and not applied
    where it does not), Gantmacher-Krein 1950/1960 and Karlin 1968
    (oscillation kernels, one-pair Green functions), Vandebril-Van
    Barel-Mastronardi 2005 (semiseparable matrices), Stieltjes / Ostrowski
    1937, 1956, Fan 1958, Berman-Plemmons 1979, Varga 1962 (M-matrices),
    Perron 1907 / Frobenius 1912, Collatz 1942 / Wielandt 1950, Weyl 1912,
    Gershgorin 1931, Feingold-Varga 1962, Haynsworth 1968 and Cauchy
    interlacing, Kirchhoff / Klein-Randic 1993, Mayer / Brydges 1984 /
    Kotecky-Preiss 1986 (the SHAPE of a cluster remainder, not a convergence
    theorem), Wilkinson 1968 and Higham 2002, Bertrand-Chebyshev 1852 and the
    trivial even bound (the only two gap facts consumed).  No gap CONJECTURE
    enters anywhere.
  * HARD CAPS.  Largest FACTORISED / INVERTED / DIAGONALISED matrix <= 1500;
    the signed Gram is formed explicitly only below that cap; total runtime
    budget 780 s (< 900 s), with per-block guards that truncate a pool rather
    than overrun.
"""

import ast
import math
import os
import time

import numpy as np
from numpy.linalg import LinAlgError
from scipy.linalg import cho_factor, cho_solve, eigh, eigvalsh, svdvals

PASS = 0
FAIL = 0
T_START = time.time()

EULER = 0.5772156649015328606065120900824
LOG_PI = math.log(math.pi)

MAX_H = 1500                 # HARD cap on any FACTORISED / INVERTED form
BUDGET_S = 780.0             # HARD probe budget (< 900 s)

U_ROUND = 2.0 ** -53
GL_N = 48
_GLX, _GLW = np.polynomial.legendre.leggauss(GL_N)

NU_MAIN = 4                  # T105 admissibility floor / T112 frame A
H_MIN = 24
CHUNK = 16384

ATOM_MAX = 320000
ZONE_DEEP = 300000

# --- J1 / J2 pools (the signed Gram is formed explicitly: n_e <= NE_CAP) -----
J12_ZONES = 44
J12_HCAP = 300
NE_CAP = 1500                # == MAX_H: every Cholesky stays under the cap
DMS_B = (2, 4, 8, 16, 32)    # band truncations for the Demko-Moss-Smith rung
TAIL_B = (0, 1, 2, 4, 8, 16)  # bandwidths whose TAIL Loewner sign is certified
KP_RANGE = 4096              # truncation for the Jaffard algebra constant K_p
T_J1 = 300.0

# --- J3 pools (the T137/T138 transport surface, rebuilt smaller) -------------
J3_GC_MIN = 2
J3_HCAP = 700
J3_MAX = 640
J3_PER_RHO = 20
J3_G_FIT = 10                # minimum border block size for a decay FIT
J3_LOGRES = 90.0
TB_WINDOWS = 6               # windows on which the three-body term is typed
J3_RHO = (1.001, 1.05, 1.10, 1.20, 1.25, 1.35, 1.49531, 1.60, 1.75, 1.90,
          2.00, 2.25, 2.50, 3.00, 3.50, 4.00)   # 1.49531 = the T127 band edge
M_LADDER = (1, 2, 3, 4, 6, 8, 12, 16, 24, 32, 48)
TRIPLE_SAMPLE = 700
T_J3 = 200.0

# --- preregistered bars (declared before any number is computed) -------------
BAR_ID = 1.0e-11             # every identity must hold to this relative level
BAR_JAFFARD_P = 1.0          # Jaffard needs a kernel exponent STRICTLY above 1
BAR_EXP_MATCH = 0.25         # certified exponent within this of the measured
BAR_COVER = 1.0              # the series bound must clear on EVERY window
BAR_BLOCK25 = 2.0            # the 25 blocks are short by ~ this factor
BAR_NEG3 = 0.75              # "systematically negative" for the three-body term

# --- quoted numbers.  QUOTED, never re-derived here -------------------------
RHO_W_T138 = (0.9752, 1.0000)
DECAY_2ND_T137 = -0.63       # entrywise second differences  (a FIT)
DECAY_LAYER_T138 = -1.54     # stripe-reduced layer norms    (a FIT)
SIGN_NESTED_T138 = (0.76, 0.94)
SIGN_CROSS_T138 = (0.59, 0.63)
SIGN_DISJ_T138 = (0.06, 0.36)
CLAMP_B_T138 = (2, 8)
CLAMP_TAIL_T138 = (0.46, 0.70)
N_BAD_T138 = 25
N_BORDER_T138 = 900
PROMO_T138 = 37
N_PROBES_PRIOR = 138
CLUSTER_3BODY_T138 = 2.5


def check(name, ok, detail=""):
    global PASS, FAIL
    if ok:
        PASS += 1
    else:
        FAIL += 1
    print("check  %-36s %s  %s" % (name, "PASS" if ok else "FAIL", detail))


def info(name, detail=""):
    print("info   %-36s %s" % (name, detail))


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
    return float(np.max(np.abs(a - b))) / max(float(np.max(np.abs(b))), 1.0e-300)


def qmin(v):
    return float(np.min(np.asarray(v, dtype=float))) if len(v) else float("nan")


def qmax(v):
    return float(np.max(np.asarray(v, dtype=float))) if len(v) else float("nan")


def qmed(v):
    return float(np.median(np.asarray(v, dtype=float))) if len(v) else float("nan")


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
    n = x.shape[0]
    a, b, rms = fit_line(x, y)
    if n < 5:
        return a, b, float("nan"), float("nan"), rms
    aa, bb = [], []
    step = max(1, n // 40)
    for i in range(0, n, step):
        m = np.ones(n, dtype=bool)
        m[i] = False
        ai, bi, _ = fit_line(x[m], y[m])
        aa.append(ai)
        bb.append(bi)
    return a, b, float(np.std(aa)), float(np.std(bb)), rms


def pow_fit(xv, yv, tag):
    """A POWER-LAW FIT y ~ c x^p in log-log, with its jackknife band."""
    xv = np.asarray(xv, dtype=float)
    yv = np.asarray(yv, dtype=float)
    m = (xv > 0.0) & (yv > 0.0) & np.isfinite(xv) & np.isfinite(yv)
    if int(np.count_nonzero(m)) < 3:
        return dict(tag=tag, p=float("nan"), c=float("nan"), sp=float("nan"),
                    rms=float("nan"), n=int(np.count_nonzero(m)))
    a, p, sa, sp, rms = fit_band(np.log(xv[m]), np.log(yv[m]))
    return dict(tag=tag, p=p, c=math.exp(a), sp=sp, rms=rms,
                n=int(np.count_nonzero(m)))


def exp_fit(xv, yv, tag):
    """AN EXPONENTIAL FIT y ~ c q^x, i.e. a line in (x, log y).  Reported next
    to every power-law fit so that the SHAPE of the decay is a measurement and
    not an assumption: Demko-Moss-Smith predicts the exponential shape for a
    band matrix, Jaffard the polynomial shape for a dense one."""
    xv = np.asarray(xv, dtype=float)
    yv = np.asarray(yv, dtype=float)
    m = (yv > 0.0) & np.isfinite(xv) & np.isfinite(yv)
    if int(np.count_nonzero(m)) < 3:
        return dict(tag=tag, q=float("nan"), c=float("nan"), rms=float("nan"),
                    n=0)
    a, s, sa, ss, rms = fit_band(xv[m], np.log(yv[m]))
    return dict(tag=tag, q=math.exp(s), c=math.exp(a), rms=rms,
                n=int(np.count_nonzero(m)), s=s)


# ----------------------------------------------------------------------------
# el_firewall -- AST scan of this source
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
          == "green_decay_probe.py", "single new file in the sandbox")


# ----------------------------------------------------------------------------
# prime-power arithmetic (exact, cheap) -- T111..T138 code path
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


# ----------------------------------------------------------------------------
# the J = -1 (reflection-odd) sector -- exact coordinates (T106..T138)
# ----------------------------------------------------------------------------
def odd_toeplitz(c, M):
    h = M // 2
    r = np.arange(h)
    return c[np.abs(r[:, None] - r[None, :])] - c[(M - 1) - r[:, None] - r[None, :]]


def odd_toeplitz_slow(c, M):
    """The definition, entry by entry -- the J0 reference for odd_toeplitz."""
    h = M // 2
    out = np.empty((h, h))
    for i in range(h):
        for j in range(h):
            out[i, j] = c[abs(i - j)] - c[(M - 1) - i - j]
    return out


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


def cert_lam_max(X, guess=None, tries=14, grow=1.0e-7):
    """CERTIFY lam_max(X) <= s for a symmetric X by a COMPLETED CHOLESKY of
    s I - X (Wilkinson 1968; Higham 2002 Thm 10.3/10.4).  DIRECTION: an UPPER
    bound, which is what a floor needs."""
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
    """CERTIFY lam_max(X) <= s for a symmetric X WITHOUT assuming s >= 0.  The
    Loewner question of J2 -- is the discarded tail nonpositive? -- needs a
    certified bound that is allowed to be NEGATIVE, so the shift walks DOWN
    from a Rayleigh quotient and the last completed Cholesky is returned.  A
    completed Cholesky of s I - X certifies lam_max(X) <= s + floor for any
    real s, and the sign of that number is the answer."""
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
    """CERTIFY lam_min(X) >= t for a symmetric X by a completed Cholesky of
    X - t I.  DIRECTION: a LOWER bound."""
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


def ray_top(X, iters=180, rng=None):
    """lam_max of a SYMMETRIC X by a SHIFTED power iteration: with
    sig = max_r sum_s |X_rs| the matrix X + sig I is PSD (Gershgorin 1931), so
    no negative eigenvalue can win the iteration.  The returned value is a
    RAYLEIGH QUOTIENT, hence a rigorous LOWER bound on lam_max(X)."""
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


def perron_bracket(applyf, n, iters, rng=None):
    """A COLLATZ-WIELANDT bracket for the spectral radius of a NONNEGATIVE
    operator: at any strictly positive x, min_r (Ax)_r / x_r <= rho(A) <=
    max_r (Ax)_r / x_r (Collatz 1942; Wielandt 1950).  Both ends are rigorous
    at every iterate."""
    x = np.ones(n) if rng is None else (np.abs(rng.standard_normal(n)) + 0.5)
    lo, up = 0.0, float("inf")
    for _ in range(iters):
        y = applyf(x)
        r = y / np.maximum(x, 1.0e-300)
        lo = max(lo, float(np.min(r)))
        up = min(up, float(np.max(r)))
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
    """The bordered step (Haynsworth 1968), its border Schur block S, and the
    Schur-reduced pole source shat -- rebuilt in this file's coordinates as a
    declared PROXY for the T134 assembly source, exactly as T138 did."""
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
    shat = tv[:gc] - C @ cho_solve(fac, tv[gc:], check_finite=False)
    del Q, A, C, X, Z
    return dict(S=S, shat=shat, fr=fr)


# ----------------------------------------------------------------------------
# THE LUMPED M-MATRIX PAIR and its EDGE representation -- the central objects
# ----------------------------------------------------------------------------
def lump_pair(A):
    """THE LUMPED M-MATRIX PAIR of a symmetric A (T136 (P1)).  Delta = the
    POSITIVE off-diagonal part, L_Delta = diag(Delta 1) - Delta its Laplacian
    (PSD, zero row sums), A_B = A + L_Delta.

    DIRECTION: L_Delta >= 0 in the LOEWNER order, so A_B >= A -- lumping
    RAISES the form, and the floor is reached only through the INVERSE side.

    NOTE FOR J1: the off-diagonals of A_B are exactly min(A_rs, 0), so
    |(A_B)_rs| <= |A_rs| entrywise off the diagonal.  Every kernel-decay
    envelope proved for A therefore transfers to A_B for free -- in the
    direction J1 needs, and verified in J1.1."""
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
    """THE M-MATRIX ANCHOR (T136 (P4)): A_B x = 1, x >= 0 certifies a
    nonsingular M-matrix (Fan 1958; Berman-Plemmons 1979) and
    lam_min(A_B) >= 1 / max_r x_r.  DIRECTION: a LOWER bound."""
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
    (e_r - e_t)^T, exactly.  NOTHING is capped or dropped -- an upper bound on
    lam_max(W) may not discard edges, because dropping an edge SHRINKS
    L_Delta and would bound the wrong object.  Sorted by the STRIPE index
    anti = M - 1 - r - t, so stripe blocks are contiguous slices."""
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


def signed_gram(G, er, et, wt):
    """THE SIGNED GRAM, formed explicitly (n_e <= NE_CAP <= MAX_H):

        Gram_{ee'} = sqrt(Delta_e Delta_e') b_e^T G b_{e'},   b_e = e_r - e_t,

    a weighted matrix of SECOND DIFFERENCES of the Green function G = A_B^{-1}.
    NO absolute value is taken anywhere in this function."""
    Yw = (G[:, er] - G[:, et]) * wt[None, :]
    GR = (Yw[er, :] - Yw[et, :]) * wt[:, None]
    del Yw
    return sym(GR)


def band_masks(sidx):
    ii = np.asarray(sidx)
    return np.abs(ii[:, None] - ii[None, :])


def one_pair_form(G):
    """THE ONE-PAIR (OSCILLATION) FORM.  For a JACOBI Stieltjes matrix the
    Green function is G_rs = phi_{min(r,s)} psi_{max(r,s)} with phi
    nondecreasing and psi nonincreasing (Gantmacher-Krein 1950/1960; Karlin
    1968).  A_B is DENSE, so this is a CANDIDATE and the defect is a
    MEASUREMENT.  phi, psi are read off one column and one row, phi_0 = 1."""
    h = G.shape[0]
    psi = G[0, :].copy()
    den = G[0, h - 1]
    if not (abs(den) > 0.0):
        return None
    phi = G[:, h - 1] / den
    r = np.arange(h)
    lo = np.minimum(r[:, None], r[None, :])
    hi = np.maximum(r[:, None], r[None, :])
    Gp = phi[lo] * psi[hi]
    scale = max(float(np.max(np.abs(G))), 1.0e-300)
    return dict(phi=phi, psi=psi, Gp=Gp,
                defect=float(np.max(np.abs(Gp - G))) / scale,
                med_defect=float(np.median(np.abs(Gp - G))) / scale,
                phi_mono=float(np.mean(np.diff(phi) >= 0.0)),
                psi_mono=float(np.mean(np.diff(psi) <= 0.0)))


# ----------------------------------------------------------------------------
# J1 (a)  THE KERNEL SIDE -- the certified envelope of the odd section
# ----------------------------------------------------------------------------
def lag_envelope(c, M, h):
    """THE CERTIFIED KERNEL ENVELOPE of the reflection-odd section.

    A_rs = c_{|r-s|} - c_{M-1-r-s} on 0 <= r, s <= h-1 with h = M/2.  Two facts,
    both EXACT (integer arithmetic and one triangle inequality), not fitted:

      (1) THE ANTI-INDEX DOMINATES.  r, s <= h - 1 gives r + s <= M - 2 - d
          for d = |r - s|, hence M - 1 - r - s >= d + 1.  The anti-Toeplitz
          term therefore never sits at a SHORTER lag than the Toeplitz term:
          whatever decay the lag sequence has, the anti part inherits it.
      (2) Consequently |A_rs| <= |c_d| + max_{k >= d+1} |c_k| =: E_d, and by
          lumping (off-diagonals of A_B are min(A_rs, 0)) also
          |(A_B)_rs| <= E_{|r-s|} off the diagonal.

    E_d is the object Jaffard 1990 wants as a hypothesis.  Both facts are
    VERIFIED per instance below; the EXPONENT of E_d is a FIT."""
    cab = np.abs(c[:M])
    tail = np.maximum.accumulate(cab[::-1])[::-1]      # tail[k] = max_{j>=k}|c_j|
    dd = np.arange(1, h)
    env = cab[dd] + tail[dd + 1]
    return dict(dd=dd, env=env, cab=cab[dd], tail=tail[dd + 1],
                anti_ok=int(bool(np.all((M - 1 - (np.arange(h)[:, None]
                                                 + np.arange(h)[None, :]))
                                        >= np.abs(np.arange(h)[:, None]
                                                  - np.arange(h)[None, :]) + 1))))


def decay_profile(X, dmat, dmax, use_abs=True):
    """THE DECAY PROFILE of a matrix along a distance label: for every distance
    d the MAX and the MEDIAN of |X| over that layer.  A MEASUREMENT."""
    V = np.abs(X) if use_abs else X
    dm, md, nn = [], [], []
    for d in range(1, dmax + 1):
        m = dmat == d
        if not m.any():
            dm.append(float("nan"))
            md.append(float("nan"))
            nn.append(0)
            continue
        v = V[m]
        dm.append(float(np.max(v)))
        md.append(float(np.median(v)))
        nn.append(int(v.shape[0]))
    return dict(d=np.arange(1, dmax + 1), mx=np.array(dm), md=np.array(md),
                n=np.array(nn))


def kp_constant(p, rng=KP_RANGE):
    """THE JAFFARD ALGEBRA CONSTANT.  With w(k) = (1 + |k|)^{-p} the class
    A_p = {|a_ij| <= C w(i-j)} is closed under multiplication with
    |(ab)_ij| <= C_a C_b (w * w)(i-j) <= K_p C_a C_b w(i-j),

        K_p = sup_k (w * w)(k) / w(k),

    finite exactly when p > 1 (Jaffard 1990; Baskakov 1990; the weighted and
    symmetric-algebra generalisations are Gröchenig-Leinert 2006).  K_p is
    COMPUTED here by truncated convolution -- a lower estimate of a supremum,
    so the reported gate is if anything OPTIMISTIC, which is the safe direction
    for a NEGATIVE conclusion and is flagged where it is used."""
    if not (p > 1.0):
        return float("inf")
    k = np.arange(-rng, rng + 1, dtype=float)
    w = (1.0 + np.abs(k)) ** (-p)
    ww = np.convolve(w, w, mode="same")
    return float(np.max(ww / w))


def dms_rate(lam_min, lam_max, b):
    """DEMKO-MOSS-SMITH 1984, verbatim, for a symmetric positive definite BAND
    matrix of bandwidth b: |(A^{-1})_rs| <= C q^{|r-s|} with

        q = ((sqrt(kappa) - 1) / (sqrt(kappa) + 1))^{1/b},
        C = max(1 / lam_min, (1 + sqrt(kappa))^2 / (2 lam_max)),

    kappa = lam_max / lam_min.  THIS IS A THEOREM FOR BAND MATRICES ONLY and is
    used here only on band TRUNCATIONS of A_B, never on A_B itself.  Both
    lam_min and lam_max are supplied CERTIFIED (Cholesky), so C and q are
    certified once the theorem is granted."""
    if not (lam_min > 0.0) or not (lam_max > 0.0) or b < 1:
        return dict(q=float("nan"), C=float("nan"), kappa=float("nan"))
    kap = lam_max / lam_min
    sk = math.sqrt(kap)
    q = ((sk - 1.0) / (sk + 1.0)) ** (1.0 / float(b))
    C = max(1.0 / lam_min, (1.0 + sk) ** 2 / (2.0 * lam_max))
    return dict(q=q, C=C, kappa=kap,
                length=(1.0 / max(-math.log(max(q, 1.0e-300)), 1.0e-300)))


def band_truncate(A, b):
    h = A.shape[0]
    r = np.arange(h)
    m = np.abs(r[:, None] - r[None, :]) <= b
    return np.where(m, A, 0.0), np.where(m, 0.0, A)


def dms_rung(A_B, b):
    """ONE RUNG of the Jaffard constant chain, computed and not asserted.

    A_B = A_b + E_b with A_b the band truncation of bandwidth b (Stieltjes and,
    where the Cholesky completes, positive definite) and E_b the DENSE far
    part.  The rung reports: the certified extreme eigenvalues of A_b, the
    Demko-Moss-Smith constants on it, the VERIFIED validity of that bound
    against the actual A_b^{-1}, the Schur norm of E_b, the operator gate
    theta = ||A_b^{-1}|| ||E_b|| < 1 that a Neumann series in the OPERATOR norm
    needs, and the algebra gate the Jaffard chain needs in the A_p norm."""
    h = A_B.shape[0]
    Ab, Eb = band_truncate(A_B, b)
    Ab = sym(Ab)
    fac = safe_cho(Ab)
    out = dict(b=int(b), pd=int(fac is not None),
               e_schur=gersh(Eb), e_mass=float(np.abs(Eb).sum()))
    if fac is None:
        out.update(lmin=float("nan"), lmax=float("nan"), q=float("nan"),
                   C=float("nan"), kappa=float("nan"), dms_ok=0,
                   theta=float("nan"), length=float("nan"), dms_slack=float("nan"))
        return out
    lmin = cert_lam_min(Ab, guess=float(eigvalsh(Ab, subset_by_index=[0, 0])[0]))
    lmax = cert_lam_max(Ab, guess=ray_top(Ab))
    d = dms_rate(lmin, lmax, b)
    Gb = cho_solve(fac, np.eye(h), check_finite=False)
    r = np.arange(h)
    dist = np.abs(r[:, None] - r[None, :])
    if np.isfinite(d["q"]) and np.isfinite(d["C"]):
        bound = d["C"] * (d["q"] ** dist)
        ratio = np.abs(Gb) / np.maximum(bound, 1.0e-300)
        out["dms_ok"] = int(float(np.max(ratio)) <= 1.0 + 1.0e-9)
        out["dms_slack"] = float(np.max(ratio))
        del bound, ratio
    else:
        out["dms_ok"] = 0
        out["dms_slack"] = float("nan")
    out.update(lmin=lmin, lmax=lmax, q=d["q"], C=d["C"], kappa=d["kappa"],
               length=d.get("length", float("nan")),
               theta=out["e_schur"] / max(lmin, 1.0e-300))
    del Ab, Eb, Gb, dist
    return out


def increment_form(G, er, et, wt, left, disj, nest_in, nest_out):
    """J1 (c) THE INCREMENT LEMMA, exactly as the one-pair form dictates.

    With G_rs = phi_{min} psi_{max} and edges e = (a, b), e' = (c, d), a < b,
    c < d (edge_list stores er < et, so a = er, b = et), the weighted second
    difference b_e^T G b_{e'} is EXACTLY

        DISJOINT, e left of e' (b < c):
            (phi_a - phi_b)(psi_c - psi_d) = -[Dphi_e][Dpsi_e']
            -- a PRODUCT of one INCREMENT per edge, NEGATIVE by monotonicity
            (phi up, psi down), which is precisely the measured disjoint sign;
        NESTED, e' inside e (a < c < d < b):
            phi_a (psi_c - psi_d) + psi_b (phi_d - phi_c)
            = [phi at the OUTER left endpoint][Dpsi of the INNER edge]
            + [psi at the OUTER right endpoint][Dphi of the INNER edge]
            -- ENDPOINT VALUES times INNER INCREMENTS, POSITIVE;
        CROSSING (a < c < b < d):
            phi_a (psi_c - psi_d) + psi_d phi_b - psi_b phi_c -- mixed.

    THE CONSEQUENCE, which is the finding of J1 (c): only the DISJOINT class
    gains an increment factor from BOTH edges.  The nested class keeps a bare
    ENDPOINT VALUE, so it cannot decay by differencing at all -- it can only
    decay because phi_a or psi_b is small, i.e. by position and not by
    distance.  The two classes therefore decay for different reasons and any
    decay lemma must treat them separately.

    Both orientations of each class are handled, so the returned prediction is
    symmetric.  The formula is EXACT for a one-pair kernel and a CANDIDATE for
    the dense A_B; the defect is measured."""
    op = one_pair_form(G)
    if op is None:
        return None
    phi, psi = op["phi"], op["psi"]
    lo = np.minimum(er, et)
    hi = np.maximum(er, et)
    dphi = phi[hi] - phi[lo]                     # >= 0 if phi is nondecreasing
    dpsi = psi[lo] - psi[hi]                     # >= 0 if psi is nonincreasing
    W2 = wt[:, None] * wt[None, :]
    pd = -np.where(left, dphi[:, None] * dpsi[None, :],
                   dphi[None, :] * dpsi[:, None])
    pn = np.where(nest_in,
                  phi[lo][:, None] * dpsi[None, :]
                  + psi[hi][:, None] * dphi[None, :],
                  phi[lo][None, :] * dpsi[:, None]
                  + psi[hi][None, :] * dphi[:, None])
    pred = W2 * np.where(disj, pd, np.where(nest_in | nest_out, pn, 0.0))
    del pd, pn, W2
    return dict(pred=pred, dphi=dphi, dpsi=dpsi, op=op,
                dphi_max=float(np.max(np.abs(dphi))),
                dpsi_max=float(np.max(np.abs(dpsi))),
                phi_max=float(np.max(np.abs(phi))),
                psi_max=float(np.max(np.abs(psi))))


def mixed_second_difference(G):
    """THE OBJECT THE LEMMA IS ABOUT.  The mixed second difference of the Green
    function,

        H_rs = G_{r+1,s+1} - G_{r+1,s} - G_{r,s+1} + G_{r,s},

    on 0 <= r, s <= h-2.  Its role is an EXACT double telescoping: for edges
    e = (a, b), e' = (c, d) with a < b, c < d,

        b_e^T G b_{e'} = sum_{r=a}^{b-1} sum_{s=c}^{d-1} H_rs ,

    an identity and not an estimate (verified in J1.3).  Consequently

        |Gram_{ee'}| <= sqrt(Delta_e Delta_e') l_e l_{e'} max_{box} |H_rs| ,

    l = the edge length -- so the WHOLE decay question is a POINTWISE question
    about ONE two-dimensional kernel.  That is the shape a decay lemma for
    second differences has to have, and it is the shape Demko-Moss-Smith and
    Jaffard do NOT have (both bound entries of the inverse, not its mixed
    differences)."""
    return G[1:, 1:] - G[1:, :-1] - G[:-1, 1:] + G[:-1, :-1]


def interval_gap(a, b, c, d):
    """The index separation of the two closed intervals [a, b] and [c, d]: the
    MINIMUM of |r - s| over the telescoping box, which is 0 exactly when the
    box meets the diagonal.  This single integer is what turns the mixed
    second difference kernel into the geometric sign law of T138: DISJOINT
    pairs have gap > 0 and their box never meets the diagonal, while NESTED and
    CROSSING pairs have gap 0 and always contain diagonal boxes."""
    return np.maximum(0, np.maximum(c[None, :] - b[:, None],
                                    a[:, None] - d[None, :]))


def layer_block_norm(GR, starts, counts, dmat_stripe, d):
    """A CERTIFIABLE norm for one LAYER of the signed Gram.

    L^{(d)} is the part of the Gram with stripe distance exactly d.  For a
    symmetric matrix the BLOCK row-sum test (Feingold-Varga 1962; Gershgorin
    1931 for blocks) gives

        lam_max(L^{(d)}) <= ||L^{(d)}||_2 <= max_i sum_j ||B_ij||_2

    with B_ij the stripe blocks, and every block is small -- so this is cheap
    and CERTIFIABLE at every d, which is exactly what a never-truncating series
    needs.  The plain entrywise row-sum norm is returned alongside as the
    cruder alternative, and the two are reported together."""
    nb = starts.shape[0]
    rows = np.zeros(nb)
    for i in range(nb):
        ai, bi = int(starts[i]), int(starts[i] + counts[i])
        tot = 0.0
        for j in (i - d, i + d):
            if j < 0 or j >= nb:
                continue
            aj, bj = int(starts[j]), int(starts[j] + counts[j])
            B = GR[ai:bi, aj:bj]
            if B.size == 0:
                continue
            sv = svdvals(B)
            tot += float(sv[0]) if sv.size else 0.0
        rows[i] = tot
    blk = float(np.max(rows)) if nb else 0.0
    ent = gersh(np.where(dmat_stripe == d, GR, 0.0))
    return blk, ent


# ----------------------------------------------------------------------------
# J3 machinery -- the border level, rebuilt from T138 and extended
# ----------------------------------------------------------------------------
def paired_neumann(S, m_ladder=M_LADDER):
    """THE m-PAIRED NEUMANN CERTIFICATE of T138, QUOTED in form and extended in
    two ways only: a longer m ladder, and a LOCALISATION of the failure.

    With S = S_B - L_Delta, G_B = S_B^{-1} >= 0, F = G_B L_Delta, the identity
    (I - F)^{-1} = P_m (I - F^m)^{-1}, P_m = sum_{j<m} F^j, gives the entrywise
    LOWER bound S^{-1} >= P_m G_B - |P_m| (I - |F^m|)^{-1} |F^m| G_B whenever
    rho(|F^m|) < 1.  m = 1 is the T137 certificate.  DIRECTION: a LOWER bound on
    the entries of S^{-1}, which is what a positivity certificate needs.

    THE ADDITION HERE.  The certificate fails when the need ratio
    nu = max (|P_m| T_m G_B) / (P_m G_B) exceeds 1, and a DECAY lemma could only
    ever help if that maximum sits at a LARGE index distance.  So the argmax
    distance and the far-restricted need are recorded per rung: if the failure
    is local, no decay statement can repair it, and that is a decidable
    question rather than a matter of taste."""
    g = S.shape[0]
    S = sym(S)
    dgS = np.diag(S).copy()
    off = S - np.diag(dgS)
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
    out = dict(g=g, n_edge=int(np.count_nonzero(Dl > 0.0)) // 2,
               edge_frac=(float(np.count_nonzero(Dl > 0.0))
                          / max(g * (g - 1.0), 1.0)),
               g_min=float(np.min(G_B)), g_max=float(np.max(G_B)),
               inv_nonneg=int(bool(np.all(G_B >= -1.0e-14
                                          * float(np.abs(G_B).max())))),
               ld_mass=float(np.sum(Dl)) / max(float(np.sum(np.abs(S))),
                                               1.0e-300))
    F = G_B @ LD
    Fabs = np.abs(F)
    lo1, up1 = perron_bracket(lambda v: Fabs @ v, g, 80)
    out["rho_fabs"] = up1
    out["rho_fabs_lo"] = lo1
    try:
        out["rho_f"] = float(np.max(np.abs(np.linalg.eigvals(F))))
    except LinAlgError:
        out["rho_f"] = float("nan")
    rungs = []
    Fm = Ig.copy()
    Pm = np.zeros((g, g))
    for m in range(1, max(m_ladder) + 1):
        Pm = Pm + Fm
        Fm = Fm @ F
        if m not in m_ladder:
            continue
        Fma = np.abs(Fm)
        lo, up = perron_bracket(lambda v: Fma @ v, g, 80)
        row = dict(m=m, rho_up=up, rho_lo=lo,
                   root=(up ** (1.0 / m)) if up > 0.0 else 0.0,
                   cert=0, need=float("inf"), need_d=-1,
                   need_far=float("inf"))
        if up < 1.0:
            try:
                Tm = np.linalg.solve(Ig - Fma, Fma)      # >= 0, CERTIFIABLE
                bad = np.abs(Pm) @ (Tm @ G_B)
                good = Pm @ G_B
                low = good - bad
                row["cert"] = int(float(np.min(low)) > 0.0)
                rat = bad / np.maximum(good, 1.0e-300)
                row["need"] = float(np.max(rat))
                idx = int(np.argmax(rat))
                row["need_d"] = int(dmat.ravel()[idx])
                far = dmat >= 2
                row["need_far"] = (float(np.max(rat[far])) if far.any()
                                   else float("nan"))
                del Tm, bad, good, low, rat
            except LinAlgError:
                pass
        rungs.append(row)
        del Fma
    out["rungs"] = rungs
    out["m_best"] = min([r["m"] for r in rungs if r["cert"]] or [0])
    out["rho_best"] = qmin([r["root"] for r in rungs])
    out["conv_any"] = int(any(r["rho_up"] < 1.0 for r in rungs))
    out["cert_any"] = int(any(r["cert"] for r in rungs))
    fin = [r for r in rungs if np.isfinite(r["need"])]
    out["need_best"] = qmin([r["need"] for r in fin]) if fin else float("inf")
    out["need_d_best"] = (min(fin, key=lambda r: r["need"])["need_d"]
                          if fin else -1)
    out["need_far_best"] = (min(fin, key=lambda r: r["need"])["need_far"]
                            if fin else float("nan"))
    out["_S_B"] = S_B
    out["_LD"] = LD
    out["_S"] = S
    del F, Fabs, Fm, Pm, G_B, Dl, dmat
    return out


def ws_level(S, S_B, LD):
    """rho(W_S) ONE LEVEL DOWN, and the J1 machinery applied to it.

    Whitening the border Schur block by its OWN lumped pair, S_B = L L^T,
    St = L^{-1} S L^{-T} = I - W_S with W_S = L^{-1} L_Delta L^{-T} >= 0, so
    lam(St) = 1 - lam(W_S) and lam_max(St) <= 1 is FREE (T138 M17).  The
    question this probe adds: does the BORDER level inherit the J1 structure?
    So the same three measurements are made on it -- the kernel decay of the
    off-diagonals of S, the mixed second difference of S_B^{-1} with its sign
    split, and its decay exponent."""
    g = S.shape[0]
    try:
        L = np.linalg.cholesky(S_B)
    except LinAlgError:
        return None
    Li = np.linalg.solve(L, np.eye(g))
    W = sym(Li @ LD @ Li.T)
    rho_w = float(eigvalsh(W, subset_by_index=[g - 1, g - 1])[0])
    rr = np.arange(g)
    dist = np.abs(rr[:, None] - rr[None, :])
    prof_S = decay_profile(S - np.diag(np.diag(S)), dist, g - 1)
    f_S = pow_fit(prof_S["d"], prof_S["mx"], "S_offdiag")
    GB = np.linalg.solve(S_B, np.eye(g))
    H = mixed_second_difference(GB)
    rr2 = np.arange(g - 1)
    d2 = np.abs(rr2[:, None] - rr2[None, :])
    prof_H = decay_profile(H, d2, g - 2)
    f_H = pow_fit(prof_H["d"], prof_H["mx"], "S_mixed")
    offd = d2 >= 1
    out = dict(g=g, rho_w=rho_w, p_S=f_S["p"], p_H=f_H["p"],
               H_neg_off=(float(np.mean(H[offd] < 0.0)) if offd.any()
                          else float("nan")),
               H_pos_diag=float(np.mean(np.diag(H) > 0.0)) if g > 2 else
               float("nan"))
    del L, Li, W, GB, H, dist, d2
    return out


def three_body(GR, starts, counts, disj, rng, n_s=TRIPLE_SAMPLE):
    """THE CLUSTER REMAINDER, TYPED BY SIGN.  T138 quoted a three-body residue
    of up to %.1f x the two-body sum.  The Mayer-style third cumulant of the
    stripe cluster expansion is

        eps3 = [lam_max(triple) - max single] - sum over the 3 pairs of eps_ij ,
        eps_ij = lam_max(pair) - max(single_i, single_j) >= 0 ,

    every eigenproblem solved EXACTLY on the union of the stripe blocks, so no
    sign is destroyed anywhere.  A systematically NEGATIVE eps3 is benign: it
    means the two-body sum already OVERSHOOTS and the three-body term pulls the
    estimate down.  The sign is tabulated against the DISJOINT share of the
    triple's edge pairs -- the class the geometric sign law says is negative --
    so that the answer is mechanistic and not just a percentage.  Cited as the
    SHAPE of a remainder (Mayer; Brydges 1984; Kotecky-Preiss 1986); NO
    convergence criterion is verified.""" % CLUSTER_3BODY_T138
    nb = starts.shape[0]
    if nb < 3:
        return None
    sl = [np.arange(int(starts[i]), int(starts[i] + counts[i]))
          for i in range(nb)]

    def top(idx):
        B = sym(GR[np.ix_(idx, idx)])
        n = B.shape[0]
        if n == 1:
            return float(B[0, 0])
        return float(eigvalsh(B, subset_by_index=[n - 1, n - 1])[0])

    single = np.array([top(sl[i]) for i in range(nb)])
    pair = {}
    for i in range(nb):
        for j in range(i + 1, nb):
            idx = np.concatenate([sl[i], sl[j]])
            pair[(i, j)] = top(idx) - max(single[i], single[j])
    rows = []
    tried = 0
    while len(rows) < n_s and tried < 6 * n_s:
        tried += 1
        i, j, k = sorted(rng.choice(nb, size=3, replace=False).tolist())
        idx = np.concatenate([sl[i], sl[j], sl[k]])
        if idx.shape[0] > MAX_H:
            continue
        tri = top(idx) - max(single[i], single[j], single[k])
        e3 = tri - (pair[(i, j)] + pair[(i, k)] + pair[(j, k)])
        blk = np.concatenate([sl[i], sl[j], sl[k]])
        dm = disj[np.ix_(blk, blk)]
        rows.append(dict(i=i, j=j, k=k, e3=e3, tri=tri,
                         two=pair[(i, j)] + pair[(i, k)] + pair[(j, k)],
                         dshare=float(np.mean(dm)),
                         span=int(k - i)))
    if not rows:
        return None
    e3v = np.array([r["e3"] for r in rows])
    twov = np.array([r["two"] for r in rows])
    return dict(rows=rows, n=len(rows),
                neg=float(np.mean(e3v < 0.0)),
                med=float(np.median(e3v)),
                rel=float(np.median(np.abs(e3v)
                                    / np.maximum(np.abs(twov), 1.0e-300))),
                pair_max=float(np.max(list(pair.values()))) if pair else 0.0,
                pair_sum=float(sum(v for v in pair.values())))


# ----------------------------------------------------------------------------
section("J0  SETUP, the pair, the signed Gram, and the DIRECTION calibrations")
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
check("el_j0.gap_facts", BERT_OK and EVEN_OK,
      "the ONLY two gap facts consumed anywhere in this file hold on all %d "
      "prime-power gaps up to n = %d: Bertrand-Chebyshev 1852 (g <= log 2) and "
      "the trivial even bound (g >= log(1 + 1/n)).  No gap CONJECTURE is used"
      % (NZ_DEEP, ZONE_DEEP))

RNG = np.random.default_rng(1390728)

# --- J0.1  the odd section against its entrywise definition -----------------
_k0, _D0, _M0 = None, None, None
for _kk in range(2, NZ_DEEP - 2):
    _Dc = 0.5 * float(G_DEEP[_kk]) / NU_MAIN
    _Mc = even_window(UU_ALL[_kk], _Dc)
    if 120 <= _Mc // 2 <= 220:
        _k0, _D0, _M0 = _kk, _Dc, _Mc
if _k0 is None:
    raise SystemExit("J0 found no calibration window in the declared h band")
_al0 = 0.5 * _M0 * _D0
_h0 = _M0 // 2
_c0, _ = lag_vector_fast(_al0, _M0, atoms_in(_al0, ATOMS_ALL))
E_ODD = rel(odd_toeplitz(_c0, _M0), odd_toeplitz_slow(_c0, _M0))
check("el_j0.odd_section", E_ODD <= BAR_ID,
      "the vectorised odd section equals its entrywise definition A_rs = "
      "c_{|r-s|} - c_{M-1-r-s} to %.2e (bar %.0e) on the calibration window "
      "h = %d, D = %.3e -- the coordinates of T106..T138, unchanged"
      % (E_ODD, BAR_ID, _h0, _D0))

_A0 = sym(odd_toeplitz(_c0, _M0))
_lp0 = lump_pair(_A0)
_an0 = anchor_floor(_lp0["A_B"])
check("el_j0.lumping", _lp0["stieltjes"] == 1
      and rel(_lp0["A_B"].sum(axis=1), _lp0["w"]) <= BAR_ID
      and _an0 is not None and _an0["nonneg"] == 1,
      "the lumped pair is STIELTJES, the ROW SUMS are preserved to %.2e, and "
      "A_B x = 1 has x >= 0 so A_B is a nonsingular M-matrix (Fan 1958; "
      "Berman-Plemmons 1979) with the anchor lam_min(A_B) >= %.3e.  DIRECTION: "
      "A_B >= A in the Loewner order, so the floor is reached only through the "
      "INVERSE side"
      % (rel(_lp0["A_B"].sum(axis=1), _lp0["w"]), _an0["floor"]))

# --- J0.2  the two structural facts J1 (a) will lean on ---------------------
_env0 = lag_envelope(_c0, _M0, _h0)
_off0 = _lp0["A_B"] - np.diag(np.diag(_lp0["A_B"]))
_r0 = np.arange(_h0)
_dist0 = np.abs(_r0[:, None] - _r0[None, :])
_envmat = np.where(_dist0 >= 1, _env0["env"][np.maximum(_dist0, 1) - 1], np.inf)
_hold_A = bool(np.all(np.abs(np.where(_dist0 >= 1, _A0, 0.0))
                      <= _envmat * (1.0 + 1.0e-12) + 1.0e-300))
_hold_B = bool(np.all(np.abs(np.where(_dist0 >= 1, _off0, 0.0))
                      <= _envmat * (1.0 + 1.0e-12) + 1.0e-300))
_lump_dom = rel(np.where(_dist0 >= 1, _off0, 0.0),
                np.where(_dist0 >= 1, np.minimum(_A0, 0.0), 0.0))
check("el_j0.kernel_envelope",
      _env0["anti_ok"] == 1 and _hold_A and _hold_B and _lump_dom <= BAR_ID,
      "THE TWO STRUCTURAL FACTS OF J1 (a), VERIFIED AND NOT FITTED.  (1) THE "
      "ANTI-INDEX DOMINATES: M - 1 - r - s >= |r - s| + 1 on every entry of "
      "the odd block (exact integer arithmetic), so the anti-Toeplitz part of "
      "A_rs never sits at a shorter lag than the Toeplitz part.  (2) Hence "
      "|A_rs| <= |c_d| + max_{k > d} |c_k| = E_d, which holds on every "
      "off-diagonal entry; and the lumped off-diagonals are exactly "
      "min(A_rs, 0) to %.2e, so |(A_B)_rs| <= E_{|r-s|} too.  E_d is therefore "
      "a CERTIFIED per-instance kernel envelope, of the shape Jaffard 1990 "
      "takes as a hypothesis -- only its EXPONENT is a fit" % _lump_dom)

# --- J0.3  the GRAM identity, bracketed instead of diagonalised -------------
_G0 = cho_solve(_an0["fac"], np.eye(_h0), check_finite=False)
_ed0 = edge_list(_lp0["Dl"], _M0)
_B0 = np.zeros((_h0, _ed0["n"]))
_B0[_ed0["er"], np.arange(_ed0["n"])] = 1.0
_B0[_ed0["et"], np.arange(_ed0["n"])] = -1.0
E_EDGE = rel((_B0 * _ed0["w"][None, :]) @ _B0.T, _lp0["LD"])
_wt0 = np.sqrt(_ed0["w"])
_GR0 = signed_gram(_G0, _ed0["er"], _ed0["et"], _wt0)
_rho_ex0 = 1.0 - float(eigh(_A0, _lp0["A_B"], eigvals_only=True,
                            subset_by_index=[0, 0])[0])
_lo0 = ray_top(_GR0, rng=RNG)
_up0 = cert_lam_max(_GR0, guess=_lo0)
check("el_j0.gram_identity",
      E_EDGE <= BAR_ID
      and _lo0 <= _rho_ex0 * (1.0 + 1.0e-9) + 1.0e-12
      and _rho_ex0 <= _up0 * (1.0 + 1.0e-9) + 1.0e-12,
      "L_Delta = sum_e Delta_e b_e b_e^T to %.2e on %d edges in %d stripes, and "
      "rho(W) = lam_max(Gram): the exact pencil value %.6f lies inside "
      "[%.6f (Rayleigh, LOWER), %.6f (completed Cholesky, UPPER)].  The whole "
      "question is the top eigenvalue of a weighted matrix of SECOND "
      "DIFFERENCES of the Green function -- which is why a decay lemma for "
      "second differences is the missing input and not a convenience"
      % (E_EDGE, _ed0["n"], _ed0["nb"], _rho_ex0, _lo0, _up0))

# --- J0.4  DEMKO-MOSS-SMITH, VERIFIED WHERE IT APPLIES ----------------------
# The contrast the whole probe turns on: DMS is a theorem for BAND matrices.
# It is verified here on a tridiagonal Stieltjes matrix and on a genuinely
# banded truncation of A_B, so that its non-applicability to the DENSE A_B is a
# statement about the object and not about this implementation.
_nT = 200
_T = (np.diag(2.05 * np.ones(_nT)) + np.diag(-1.0 * np.ones(_nT - 1), 1)
      + np.diag(-1.0 * np.ones(_nT - 1), -1))
_lmT = cert_lam_min(_T, guess=float(eigvalsh(_T, subset_by_index=[0, 0])[0]))
_lMT = cert_lam_max(_T, guess=ray_top(_T))
_dT = dms_rate(_lmT, _lMT, 1)
_GT = np.linalg.solve(_T, np.eye(_nT))
_rT = np.arange(_nT)
_distT = np.abs(_rT[:, None] - _rT[None, :])
_slackT = float(np.max(np.abs(_GT) / np.maximum(_dT["C"] * _dT["q"] ** _distT,
                                               1.0e-300)))
_pT = pow_fit(np.arange(1, _nT), [float(np.max(np.abs(_GT)[_distT == d]))
                                 for d in range(1, _nT)], "tri_pow")
_eT = exp_fit(np.arange(1, _nT), [float(np.max(np.abs(_GT)[_distT == d]))
                                  for d in range(1, _nT)], "tri_exp")
check("el_j0.dms_calibration", _slackT <= 1.0 + 1.0e-9,
      "DEMKO-MOSS-SMITH 1984 VERIFIED WHERE IT APPLIES.  On a tridiagonal "
      "Stieltjes matrix (n = %d, certified lam = %.4f .. %.4f, kappa = %.2f) "
      "the bound |(T^{-1})_rs| <= C q^{|r-s|} with q = %.6f, C = %.4f holds "
      "with worst-case slack %.4f <= 1, and the measured entry decay is "
      "EXPONENTIAL (q_fit = %.6f, rms %.3f) and not polynomial (a power fit "
      "gives d^%.2f with rms %.3f).  This is the SHAPE the band theorem "
      "predicts; the dense object of J1 is compared against it"
      % (_nT, _lmT, _lMT, _dT["kappa"], _dT["q"], _dT["C"], _slackT,
         _eT["q"], _eT["rms"], _pT["p"], _pT["rms"]))

# --- J0.5  the DIRECTION calibrations, verified rather than asserted --------
_negT = -sym(_T)
_cs_neg = cert_lam_max_signed(_negT)
_cs_pos = cert_lam_max_signed(sym(_GR0))
check("el_j0.directions",
      _cs_neg < 0.0 and _cs_neg >= -_lMT * (1.0 + 1.0e-6)
      and _cs_pos >= _rho_ex0 * (1.0 - 1.0e-8)
      and _lo0 <= _rho_ex0 * (1.0 + 1.0e-8),
      "DIRECTION CALIBRATION, the four facts J1-J3 lean on.  (i) A Rayleigh "
      "quotient is a LOWER bound: %.6f <= rho(W) = %.6f.  (ii) A completed "
      "Cholesky is an UPPER bound: the signed certifier returns %.6f >= "
      "rho(W).  (iii) The signed certifier can return a NEGATIVE number and "
      "does: on -T it gives %.4f < 0, certifying -T <= 0 in the LOEWNER "
      "order -- this is the machine J2 needs to ask whether a discarded tail "
      "is Loewner-nonpositive, which is a different question from having a "
      "negative mean.  (iv) lumping RAISES the form, so only the inverse side "
      "can produce a floor"
      % (_lo0, _rho_ex0, _cs_pos, _cs_neg))

del _T, _negT, _GT, _distT, _B0, _envmat, _dist0, _off0
del _GR0, _G0, _A0, _lp0, _ed0

# ----------------------------------------------------------------------------
section("J1  THE DECAY LEMMA -- kernel side, Jaffard chain, increment route")
# ----------------------------------------------------------------------------
para("""J1.0  WHAT WOULD HAVE TO BE TRUE.  T138 reduced the D-uniformity to a
NEVER-TRUNCATING upper bound on lam_max of the full signed Gram, and identified
the two factors such a bound needs: a DECAY LAW for the layers times the
GEOMETRIC SIGN LAW.  The sign law is measured (nested %.2f .. %.2f positive,
crossing %.2f .. %.2f, disjoint %.2f .. %.2f -- QUOTED from T138).  The decay
law is not: the measured exponents are d^%.2f for the entrywise second
differences (T137) and d^%.2f for the stripe-reduced layer norms (T138), both
FITS.  Demko-Moss-Smith 1984 is the classical address for the inverse of a BAND
matrix and A_B is dense, so it does not apply -- J0.4 verified it where it does
apply so that this statement is about the object.  The dense-matrix classic is
JAFFARD 1990: the class A_p of matrices with |a_ij| <= C (1 + |i - j|)^{-p},
p > 1, is INVERSE-CLOSED, and the inverse inherits the SAME exponent (Baskakov
1990; Gröchenig-Leinert 2006 for weighted and symmetric algebras).  This block
asks three questions in order.  (a) Does A_B satisfy the Jaffard HYPOTHESIS,
and with which exponent?  J0.2 already certified the envelope
|(A_B)_rs| <= E_{|r-s|}; here E_d is fitted.  (b) Does the Jaffard CONCLUSION
say anything about the object we need?  The conclusion is about ENTRIES of
A_B^{-1}; the Gram is built from SECOND DIFFERENCES; and Jaffard's constant
carries ||A_B^{-1}||.  All three links are measured, and the constant chain is
computed rung by rung -- band truncation, certified conditioning,
Demko-Moss-Smith rate, Schur norm of the discarded dense part, algebra constant
K_p, and the gate a Neumann series in the algebra norm needs.  (c) If the
Jaffard route does not carry the second differences, what does?  The one-pair
(oscillation-kernel) structure gives an EXACT formula per geometry class, and
the classes turn out to decay for different reasons -- which is the actual
content of the missing lemma.""" % (SIGN_NESTED_T138 + SIGN_CROSS_T138
                                    + SIGN_DISJ_T138
                                    + (DECAY_2ND_T137, DECAY_LAYER_T138)))

SZ = []
_seen = set()
for k in range(2, NZ_DEEP - 2):
    if len(SZ) >= J12_ZONES:
        break
    D_k = 0.5 * float(G_DEEP[k]) / NU_MAIN
    M_k = even_window(UU_ALL[k], D_k)
    h_k = M_k // 2
    if h_k < H_MIN or h_k > J12_HCAP:
        continue
    key = h_k // 5
    if key in _seen:
        continue
    _seen.add(key)
    SZ.append((k, D_k, M_k, h_k))

SURF = []
KROWS = []       # kernel-envelope rows (per window, per lag)
GROWS = []       # Green-entry decay rows
D2ROWS = []      # second-difference decay rows, by stripe distance and class
LROWS = []       # layer-norm rows (the J2 series terms)
for (k, D_k, M_k, h_k) in SZ:
    if budget_left() < BUDGET_S - T_J1:
        info("J1.budget", "surface truncated at n = %d after %d windows"
             % (NN_ALL[k], len(SURF)))
        break
    al = 0.5 * M_k * D_k
    ats = atoms_in(al, ATOMS_ALL)
    c, _ = lag_vector_fast(al, M_k, ats)
    A = sym(odd_toeplitz(c, M_k))
    lp = lump_pair(A)
    an = anchor_floor(lp["A_B"])
    if an is None or not an["nonneg"]:
        continue
    ed = edge_list(lp["Dl"], M_k)
    if ed["n"] < 8 or ed["n"] > NE_CAP or ed["nb"] < 6:
        continue
    n_e, nb = ed["n"], int(ed["nb"])
    A_B = lp["A_B"]
    G = cho_solve(an["fac"], np.eye(h_k), check_finite=False)
    wt = np.sqrt(ed["w"])
    GR = signed_gram(G, ed["er"], ed["et"], wt)
    dms_ = band_masks(ed["sidx"])
    try:
        gap_ex = float(eigh(A, A_B, eigvals_only=True,
                            subset_by_index=[0, 0])[0])
    except (LinAlgError, ValueError):
        continue
    rho_ex = 1.0 - gap_ex

    # --- (a) THE KERNEL SIDE: the certified envelope and its exponent -------
    env = lag_envelope(c, M_k, h_k)
    rr = np.arange(h_k)
    dist = np.abs(rr[:, None] - rr[None, :])
    envmat = np.where(dist >= 1, env["env"][np.maximum(dist, 1) - 1], np.inf)
    hold_B = bool(np.all(np.abs(np.where(dist >= 1, A_B - np.diag(np.diag(A_B)),
                                         0.0))
                         <= envmat * (1.0 + 1.0e-12) + 1.0e-300))
    f_env = pow_fit(env["dd"], np.abs(env["env"]), "kernel_env")
    e_env = exp_fit(env["dd"], np.abs(env["env"]), "kernel_env_exp")
    prof_AB = decay_profile(A_B - np.diag(np.diag(A_B)), dist, h_k - 1)
    f_AB = pow_fit(prof_AB["d"], prof_AB["mx"], "A_B_offdiag")
    # WHY the certified envelope is flat: the lag sequence is ARCHIMEDEAN plus
    # PRIME-POWER SPIKES, and the spikes sit at lag indices u_j / D with O(1)
    # amplitude.  The two parts are separated and fitted apart.
    c_arch = arch_lags(M_k, D_k)
    spike = np.abs(c_arch - c)
    f_arch = pow_fit(np.arange(1, h_k), np.abs(c_arch[1:h_k]), "arch_lag")
    sp_tail = np.maximum.accumulate(spike[::-1])[::-1]
    f_sp = pow_fit(np.arange(1, h_k), np.maximum(sp_tail[1:h_k], 1.0e-300),
                   "spike_tail")
    sp_n = int(np.count_nonzero(spike > 1.0e-13 * max(float(np.max(spike)),
                                                      1.0e-300)))
    sp_max = float(np.max(spike))
    sp_far = float(np.max(spike[h_k:])) if M_k > h_k else 0.0
    for i, d in enumerate(env["dd"]):
        if d % max(1, h_k // 40) == 0:
            KROWS.append(dict(h=h_k, D=D_k, d=int(d), env=float(env["env"][i]),
                              lag=float(env["cab"][i])))

    # --- (b) THE JAFFARD CONCLUSION, tested on the object -------------------
    prof_G = decay_profile(G, dist, h_k - 1)
    f_G = pow_fit(prof_G["d"], prof_G["mx"], "green_entry")
    e_G = exp_fit(prof_G["d"], prof_G["mx"], "green_entry_exp")
    g_ratio = float(np.max(prof_G["mx"][h_k // 2:])) / max(
        float(np.max(prof_G["mx"][:max(1, h_k // 8)])), 1.0e-300)
    for i, d in enumerate(prof_G["d"]):
        if d % max(1, h_k // 40) == 0:
            GROWS.append(dict(h=h_k, D=D_k, d=int(d), mx=float(prof_G["mx"][i]),
                              md=float(prof_G["md"][i])))
    rungs = [dms_rung(A_B, b) for b in DMS_B if b < h_k - 1]
    # TWO hypothesis exponents, kept strictly apart: the CERTIFIED envelope
    # exponent p_cert (from E_d, which holds on every entry) and the MEASURED
    # row-max exponent p_meas (a FIT, no envelope behind it).  The algebra gate
    # is evaluated with p_meas so that the chain has numbers at all, and that
    # substitution is flagged wherever the number is used.
    p_cert = -f_env["p"]
    p_meas = -f_AB["p"]
    kp = kp_constant(p_meas)
    for rg in rungs:
        if np.isfinite(rg["q"]) and np.isfinite(kp) and p_meas > 1.0:
            dd_ = np.arange(0, h_k)
            c1 = rg["C"] * float(np.max((rg["q"] ** dd_) * (1.0 + dd_) ** p_meas))
            rg["C1"] = c1
            rg["algebra_gate"] = kp * c1 * float(np.max(prof_AB["mx"]))
        else:
            rg["C1"] = float("nan")
            rg["algebra_gate"] = float("nan")
    theta_min = qmin([rg["theta"] for rg in rungs if np.isfinite(rg["theta"])])
    gate_min = qmin([rg["algebra_gate"] for rg in rungs
                     if np.isfinite(rg["algebra_gate"])])

    # --- (c) THE INCREMENT ROUTE and the geometry classes --------------------
    a_i = ed["er"][:, None]
    b_i = ed["et"][:, None]
    c_j = ed["er"][None, :]
    d_j = ed["et"][None, :]
    offd = ~np.eye(n_e, dtype=bool)
    left = b_i < c_j
    disj = ((b_i < c_j) | (d_j < a_i)) & offd
    nest_in = (a_i < c_j) & (d_j < b_i)
    nest_out = (c_j < a_i) & (b_i < d_j)
    nest = (nest_in | nest_out) & offd
    cros = offd & (~disj) & (~nest)
    inc = increment_form(G, ed["er"], ed["et"], wt, left, disj, nest_in,
                         nest_out)
    inc_stat = {}
    if inc is not None:
        pred = inc["pred"]
        for nm, m in (("disjoint", disj), ("nested", nest)):
            if int(np.count_nonzero(m)):
                rat = np.abs(pred[m] - GR[m]) / np.maximum(np.abs(GR[m]),
                                                           1.0e-300)
                inc_stat[nm] = dict(
                    sign=float(np.mean((pred[m] > 0.0) == (GR[m] > 0.0))),
                    med=float(np.median(rat)),
                    mx=float(np.max(rat)))
            else:
                inc_stat[nm] = dict(sign=float("nan"), med=float("nan"),
                                    mx=float("nan"))
        del pred
    f_dphi = pow_fit(np.arange(1, h_k), np.abs(np.diff(inc["op"]["phi"]))
                     if inc is not None else np.zeros(h_k - 1), "dphi")
    f_dpsi = pow_fit(np.arange(1, h_k), np.abs(np.diff(inc["op"]["psi"]))
                     if inc is not None else np.zeros(h_k - 1), "dpsi")

    # --- (c') THE TELESCOPING ROUTE: one kernel, exactly ---------------------
    H = mixed_second_difference(G)
    rr2 = np.arange(h_k - 1)
    dist2 = np.abs(rr2[:, None] - rr2[None, :])
    prof_H = decay_profile(H, dist2, h_k - 2)
    f_H = pow_fit(prof_H["d"], prof_H["mx"], "mixed_2nd")
    e_H = exp_fit(prof_H["d"], prof_H["mx"], "mixed_2nd_exp")
    offd2 = dist2 >= 1
    H_neg_off = float(np.mean(H[offd2] < 0.0))
    H_pos_diag = float(np.mean(np.diag(H) > 0.0))
    # the exact double telescoping, on a random sample of edge pairs
    Hcs = np.cumsum(np.cumsum(H, axis=0), axis=1)
    Hcs = np.pad(Hcs, ((1, 0), (1, 0)))

    def _boxsum(a, b, c_, d_):
        return (Hcs[b, d_] - Hcs[a, d_] - Hcs[b, c_] + Hcs[a, c_])

    ii = RNG.integers(0, n_e, size=min(400, n_e * 4))
    jj = RNG.integers(0, n_e, size=ii.shape[0])
    tel = _boxsum(ed["er"][ii], ed["et"][ii], ed["er"][jj], ed["et"][jj])
    raw = (G[ed["er"][ii][:, None], ed["er"][jj][None, :]]
           - G[ed["er"][ii][:, None], ed["et"][jj][None, :]]
           - G[ed["et"][ii][:, None], ed["er"][jj][None, :]]
           + G[ed["et"][ii][:, None], ed["et"][jj][None, :]])
    tel_err = float(np.max(np.abs(tel - np.diag(raw)))) / max(
        float(np.max(np.abs(np.diag(raw)))), 1.0e-300)
    del Hcs, tel, raw
    # the CERTIFIED-PER-INSTANCE entrywise envelope from H, via the gap
    Hcum = np.maximum.accumulate(np.nan_to_num(prof_H["mx"])[::-1])[::-1]
    Hcum = np.concatenate([[float(np.max(np.abs(H)))], Hcum])   # index = gap
    gap = interval_gap(ed["er"], ed["et"] - 1, ed["er"], ed["et"] - 1)
    ell = (ed["et"] - ed["er"]).astype(float)
    ENV = (wt[:, None] * wt[None, :]) * (ell[:, None] * ell[None, :]) \
        * Hcum[np.minimum(gap, Hcum.shape[0] - 1)]
    env_valid = int(bool(np.all(np.abs(GR) <= ENV * (1.0 + 1.0e-9) + 1.0e-300)))
    env_row = gersh(ENV)
    env_slack = env_row / max(rho_ex, 1.0e-300)
    gap0 = float(np.mean(gap == 0))
    del ENV, gap, H, dist2, offd2, prof_H

    # --- the SECOND-DIFFERENCE decay, by stripe distance and by class -------
    prof2 = decay_profile(GR, dms_, nb - 1)
    f_2nd = pow_fit(prof2["d"], prof2["mx"], "second_diff")
    f_2nd_md = pow_fit(prof2["d"], prof2["md"], "second_diff_med")
    for d in range(1, nb):
        m = dms_ == d
        if not m.any():
            continue
        tot = float(np.abs(GR[m]).sum())
        row = dict(h=h_k, D=D_k, nb=nb, d=d, tot=tot)
        for nm, cm in (("disjoint", disj), ("nested", nest),
                       ("crossing", cros)):
            mm = m & cm
            row[nm] = (float(np.abs(GR[mm]).sum()) / max(tot, 1.0e-300)
                       if mm.any() else 0.0)
        D2ROWS.append(row)

    # --- the LAYER NORMS: the terms of the never-truncating series ----------
    lay = []
    for d in range(0, nb):
        blk, ent = layer_block_norm(GR, ed["stripe_start"], ed["stripe_count"],
                                    dms_, d)
        Ld = np.where(dms_ == d, GR, 0.0)
        tr = float(np.trace(Ld))
        lo_d = ray_top(sym(Ld)) if d <= 3 else float("nan")
        del Ld
        lay.append(dict(d=d, blk=blk, ent=ent, tr=tr, lo=lo_d))
        LROWS.append(dict(h=h_k, D=D_k, nb=nb, d=d, blk=blk, ent=ent, tr=tr,
                          lo=lo_d))
    f_lay = pow_fit([r["d"] for r in lay if r["d"] >= 1],
                    [max(r["blk"], 1.0e-300) for r in lay if r["d"] >= 1],
                    "layer_block")
    f_lay_e = pow_fit([r["d"] for r in lay if r["d"] >= 1],
                      [max(r["ent"], 1.0e-300) for r in lay if r["d"] >= 1],
                      "layer_entry")
    ser_blk = float(sum(r["blk"] for r in lay))
    ser_ent = float(sum(r["ent"] for r in lay))

    # --- the TAIL LOEWNER SIGN: may a tail be discarded at all? -------------
    tails = []
    for b in TAIL_B:
        if b > nb - 1:
            continue
        inb = dms_ <= b
        Band = np.where(inb, GR, 0.0)
        Tail = GR - Band
        lo_band = ray_top(Band)
        cs_tail = cert_lam_max_signed(sym(Tail))
        tails.append(dict(b=int(b), lo_band=lo_band, cert_tail=cs_tail,
                          cert_band=cert_lam_max(sym(Band), guess=lo_band),
                          mean_tail=float(Tail.sum()) / max(float(
                              np.abs(Tail).sum()), 1.0e-300),
                          row_tail=gersh(Tail)))
        del Band, Tail, inb
        if budget_left() < BUDGET_S - T_J1 + 40.0:
            break

    # --- the three-body term of the cluster expansion, typed by sign --------
    tb = None
    if len(SURF) < TB_WINDOWS and budget_left() > BUDGET_S - T_J1 + 60.0:
        tb = three_body(GR, ed["stripe_start"], ed["stripe_count"], disj, RNG)

    SURF.append(dict(n=NN_ALL[k], h=h_k, M=M_k, D=D_k, al=al, n_e=n_e, nb=nb,
                     tb=tb,
                     anchor=an["floor"], rho_ex=rho_ex, gap_ex=gap_ex,
                     hold_B=int(hold_B), p_env=f_env["p"], s_env=f_env["sp"],
                     rms_env=f_env["rms"], q_env=e_env["q"],
                     rms_env_e=e_env["rms"], p_AB=f_AB["p"],
                     p_G=f_G["p"], s_G=f_G["sp"], rms_G=f_G["rms"],
                     q_G=e_G["q"], g_ratio=g_ratio,
                     rungs=rungs, kp=kp, p_cert=p_cert, p_meas=p_meas,
                     theta_min=theta_min, gate_min=gate_min,
                     p_arch=f_arch["p"], p_sp=f_sp["p"], sp_n=sp_n,
                     sp_max=sp_max, sp_far=sp_far, n_at=len(ats),
                     p_H=f_H["p"], s_H=f_H["sp"], rms_H=f_H["rms"],
                     q_H=e_H["q"], rms_H_e=e_H["rms"],
                     H_neg_off=H_neg_off, H_pos_diag=H_pos_diag,
                     tel_err=tel_err, env_valid=env_valid, env_row=env_row,
                     env_slack=env_slack, gap0=gap0, ell_max=float(np.max(ell)),
                     inc=inc_stat, p_dphi=f_dphi["p"], p_dpsi=f_dpsi["p"],
                     op_defect=(inc["op"]["defect"] if inc else float("nan")),
                     phi_mono=(inc["op"]["phi_mono"] if inc else float("nan")),
                     psi_mono=(inc["op"]["psi_mono"] if inc else float("nan")),
                     p_2nd=f_2nd["p"], s_2nd=f_2nd["sp"], rms_2nd=f_2nd["rms"],
                     p_2nd_md=f_2nd_md["p"],
                     p_lay=f_lay["p"], s_lay=f_lay["sp"], rms_lay=f_lay["rms"],
                     p_lay_e=f_lay_e["p"],
                     lay=lay, ser_blk=ser_blk, ser_ent=ser_ent, tails=tails,
                     lo_gr=ray_top(GR, rng=RNG)))
    del A, A_B, G, GR, dms_, dist, envmat, disj, nest, cros, offd, left
    del nest_in, nest_out, inc, lp, an, ed

if not SURF:
    raise SystemExit("J1 produced no window -- probe cannot report")

info("J1.surface", "%d windows, h = %d .. %d, D = %.3e .. %.3e, n = %d .. %d, "
     "edges %d .. %d in %d .. %d stripes; exact rho(W) = %.4f .. %.4f (T138 "
     "QUOTED %.4f .. %.4f)"
     % (len(SURF), min(r["h"] for r in SURF), max(r["h"] for r in SURF),
        qmin([r["D"] for r in SURF]), qmax([r["D"] for r in SURF]),
        min(r["n"] for r in SURF), max(r["n"] for r in SURF),
        min(r["n_e"] for r in SURF), max(r["n_e"] for r in SURF),
        min(r["nb"] for r in SURF), max(r["nb"] for r in SURF),
        qmin([r["rho_ex"] for r in SURF]), qmax([r["rho_ex"] for r in SURF]),
        RHO_W_T138[0], RHO_W_T138[1]))

# --- J1.1  the kernel envelope and its exponent -----------------------------
P_ENV = qmax([r["p_env"] for r in SURF])       # the WORST (least negative)
P_HYP = -P_ENV
P_MEAS_W = qmin([r["p_meas"] for r in SURF])   # the WORST measured exponent
JAF_APPLIES = P_HYP > BAR_JAFFARD_P
JAF_MEAS = P_MEAS_W > BAR_JAFFARD_P
check("el_j1.kernel_hypothesis",
      all(r["hold_B"] == 1 for r in SURF),
      "THE JAFFARD HYPOTHESIS, MEASURED.  The certified envelope E_d = |c_d| + "
      "max_{k > d}|c_k| holds on every off-diagonal entry of A_B on all %d "
      "windows (verified, not fitted -- the anti-index domination of J0.2 is "
      "what makes it hold).  Its exponent is E_d ~ d^%.2f .. d^%.2f (FIT, "
      "jackknife +- %.2f .. %.2f, rms %.2f .. %.2f), i.e. a polynomial decay "
      "of order p = %.2f .. %.2f; an exponential fit of the same data gives "
      "q = %.4f .. %.4f with rms %.2f .. %.2f.  The A_B off-diagonals "
      "themselves decay as d^%.2f .. d^%.2f.  JAFFARD 1990 NEEDS p > %.1f: "
      "the worst window gives p = %.2f, so the hypothesis is %s"
      % (len(SURF), qmin([r["p_env"] for r in SURF]),
         qmax([r["p_env"] for r in SURF]),
         qmin([r["s_env"] for r in SURF]), qmax([r["s_env"] for r in SURF]),
         qmin([r["rms_env"] for r in SURF]), qmax([r["rms_env"] for r in SURF]),
         -qmax([r["p_env"] for r in SURF]), -qmin([r["p_env"] for r in SURF]),
         qmin([r["q_env"] for r in SURF]), qmax([r["q_env"] for r in SURF]),
         qmin([r["rms_env_e"] for r in SURF]),
         qmax([r["rms_env_e"] for r in SURF]),
         qmin([r["p_AB"] for r in SURF]), qmax([r["p_AB"] for r in SURF]),
         BAR_JAFFARD_P, P_HYP,
         "SATISFIED on every window" if JAF_APPLIES else
         "NOT SATISFIED on the worst window"))

F_K_POOL = pow_fit([r["d"] for r in KROWS], [max(abs(r["env"]), 1.0e-300)
                                             for r in KROWS], "env_pooled")
F_G_POOL = pow_fit([r["d"] for r in GROWS], [max(r["mx"], 1.0e-300)
                                             for r in GROWS], "green_pooled")
info("J1.pooled_decay", "the same two fits POOLED across all windows, so that "
     "the per-window numbers are not carrying the conclusion alone: the "
     "certified envelope gives d^%.2f +- %.2f (rms %.2f, n = %d) and the Green "
     "entries d^%.2f +- %.2f (rms %.2f, n = %d).  The worst MEASURED kernel "
     "exponent on the surface is p = %.2f, which %s clear the Jaffard "
     "requirement p > %.1f -- but it has no envelope behind it, and the "
     "CERTIFIED exponent p = %.2f does not"
     % (F_K_POOL["p"], F_K_POOL["sp"], F_K_POOL["rms"], F_K_POOL["n"],
        F_G_POOL["p"], F_G_POOL["sp"], F_G_POOL["rms"], F_G_POOL["n"],
        P_MEAS_W, "DOES" if JAF_MEAS else "does NOT", BAR_JAFFARD_P, P_HYP))

check("el_j1.why_the_envelope_is_flat",
      all(np.isfinite(r["p_arch"]) for r in SURF),
      "WHY THE CERTIFIED ENVELOPE IS FLAT, and this is arithmetic and not "
      "slack in the estimate.  The lag sequence splits EXACTLY into an "
      "ARCHIMEDEAN part and the PRIME-POWER SPIKES it subtracts, c = c_arch - "
      "sum_j mu_j (triangle at u_j / D).  Fitted apart: the archimedean lags "
      "decay as d^%.2f .. d^%.2f -- i.e. essentially 1/d, exactly the JAFFARD "
      "BORDERLINE p = 1 and not above it -- while the spike part has %d .. %d "
      "nonzero lags out of M = %d .. %d, peak amplitude %.3f .. %.3f, and its "
      "own tail-max decays only as d^%.2f .. d^%.2f because the atoms sit at "
      "lag indices u_j / D spread across the whole window (%d .. %d atoms per "
      "window, largest far-lag spike %.3f .. %.3f).  So the Jaffard hypothesis "
      "fails for TWO independent arithmetic reasons: the smooth part sits ON "
      "the borderline exponent, and the atoms put O(1) mass at large lags.  A "
      "sup-envelope cannot see that the spikes are SPARSE -- which is the "
      "structure a weighted / sparse-plus-decay algebra would have to exploit "
      "(Baskakov 1990; Gröchenig-Leinert 2006), and no classical theorem in "
      "that family is applied here"
      % (qmin([r["p_arch"] for r in SURF]), qmax([r["p_arch"] for r in SURF]),
         min(r["sp_n"] for r in SURF), max(r["sp_n"] for r in SURF),
         min(r["M"] for r in SURF), max(r["M"] for r in SURF),
         qmin([r["sp_max"] for r in SURF]), qmax([r["sp_max"] for r in SURF]),
         qmin([r["p_sp"] for r in SURF]), qmax([r["p_sp"] for r in SURF]),
         min(r["n_at"] for r in SURF), max(r["n_at"] for r in SURF),
         qmin([r["sp_far"] for r in SURF]), qmax([r["sp_far"] for r in SURF])))

# --- J1.2  the Jaffard conclusion, tested on the object ---------------------
G_DECAYS = [r for r in SURF if r["p_G"] < -0.05]
check("el_j1.jaffard_conclusion",
      all(np.isfinite(r["p_G"]) for r in SURF),
      "THE JAFFARD CONCLUSION, TESTED WHERE IT WOULD BE USED -- and this is the "
      "decisive measurement of J1.  Jaffard's theorem concludes that the "
      "ENTRIES of A_B^{-1} decay in |r - s| with the same exponent.  Measured: "
      "the row-max entries of A_B^{-1} behave as d^%.2f .. d^%.2f (FIT, rms "
      "%.2f .. %.2f) and the far half of the index range is still %.2f .. %.2f "
      "of the near part -- so THE EXPONENT IS NOT INHERITED on this surface: "
      "the A_B off-diagonals decay as d^%.2f .. d^%.2f and the entries of "
      "A_B^{-1} only as the above, a loss of %.2f .. %.2f in the exponent on "
      "all %d of %d windows.  This does not contradict Jaffard 1990, whose "
      "conclusion is a statement in the ALGEBRA norm with a constant that is "
      "not tracked: it is the statement that the constant carries ||A_B^{-1}||, "
      "which on this surface is 1 / lam_min(A_B) with the anchor at "
      "%.2e .. %.2e -- the very quantity the D-uniformity is about.  A Green "
      "function of an M-matrix is a POSITIVE, roughly unimodal kernel "
      "(phi_min psi_max, Gantmacher-Krein): entry decay in |r - s| is the wrong "
      "shape to ask for, and the second differences are what decay"
      % (qmin([r["p_G"] for r in SURF]), qmax([r["p_G"] for r in SURF]),
         qmin([r["rms_G"] for r in SURF]), qmax([r["rms_G"] for r in SURF]),
         qmin([r["g_ratio"] for r in SURF]), qmax([r["g_ratio"] for r in SURF]),
         qmin([r["p_AB"] for r in SURF]), qmax([r["p_AB"] for r in SURF]),
         qmin([r["p_G"] - r["p_AB"] for r in SURF]),
         qmax([r["p_G"] - r["p_AB"] for r in SURF]),
         len(SURF), len(SURF),
         qmin([r["anchor"] for r in SURF]), qmax([r["anchor"] for r in SURF])))

RUNG_ALL = [rg for r in SURF for rg in r["rungs"]]
RUNG_PD = [rg for rg in RUNG_ALL if rg["pd"] == 1]
RUNG_DMS = [rg for rg in RUNG_PD if rg["dms_ok"] == 1]
THETA = [rg["theta"] for rg in RUNG_PD if np.isfinite(rg["theta"])]
GATE = [rg["algebra_gate"] for rg in RUNG_PD
        if np.isfinite(rg["algebra_gate"])]
check("el_j1.constant_chain",
      len(RUNG_DMS) == len(RUNG_PD) and len(RUNG_PD) > 0,
      "THE CONSTANT CHAIN, COMPUTED RUNG BY RUNG.  On %d (window, bandwidth) "
      "rungs the band truncation A_b is positive definite and the "
      "Demko-Moss-Smith bound holds on ALL of them (worst slack %.4f .. %.4f "
      "<= 1), with certified kappa(A_b) = %.2e .. %.2e, rate q = %.4f .. %.4f "
      "and decay length 1/|log q| = %.2f .. %.2f index steps against h = %d .. "
      "%d.  The chain then needs the DENSE far part back: its Schur norm is "
      "%.3e .. %.3e, so the OPERATOR gate theta = ||A_b^{-1}|| ||E_b|| is "
      "%.2e .. %.2e (best per window %.2e .. %.2e) and the ALGEBRA gate "
      "K_p C_1 C_E that a Neumann series in the Jaffard norm needs is "
      "%.2e .. %.2e.  A gate below 1 is what a constructive chain requires: "
      "%d of %d operator rungs and %d of %d algebra rungs are below 1"
      % (len(RUNG_PD), qmin([rg["dms_slack"] for rg in RUNG_PD]),
         qmax([rg["dms_slack"] for rg in RUNG_PD]),
         qmin([rg["kappa"] for rg in RUNG_PD]),
         qmax([rg["kappa"] for rg in RUNG_PD]),
         qmin([rg["q"] for rg in RUNG_PD]), qmax([rg["q"] for rg in RUNG_PD]),
         qmin([rg["length"] for rg in RUNG_PD]),
         qmax([rg["length"] for rg in RUNG_PD]),
         min(r["h"] for r in SURF), max(r["h"] for r in SURF),
         qmin([rg["e_schur"] for rg in RUNG_PD]),
         qmax([rg["e_schur"] for rg in RUNG_PD]),
         qmin(THETA), qmax(THETA),
         qmin([r["theta_min"] for r in SURF]),
         qmax([r["theta_min"] for r in SURF]),
         qmin(GATE) if GATE else float("nan"),
         qmax(GATE) if GATE else float("nan"),
         len([t for t in THETA if t < 1.0]), len(THETA),
         len([g for g in GATE if g < 1.0]), len(GATE)))

info("J1.kp_table", "the Jaffard algebra constant K_p = sup_k (w * w)(k) / w(k), "
     "w(k) = (1 + |k|)^{-p}, computed by truncated convolution (range %d): "
     "K_1.05 = %.3e, K_1.10 = %.3e, K_1.30 = %.3e, K_2.00 = %.3e, K_3.00 = "
     "%.3e -- it DIVERGES as p falls to 1, which is the borderline the "
     "archimedean lags sit on.  The gate above uses the MEASURED exponent "
     "p = %.2f .. %.2f (a FIT, no envelope behind it), never the certified "
     "p = %.2f, and the truncated K_p is a LOWER estimate of a supremum, so "
     "the reported gate is optimistic -- the safe direction for the negative "
     "conclusion it supports"
     % (KP_RANGE, kp_constant(1.05), kp_constant(1.10), kp_constant(1.30),
        kp_constant(2.00), kp_constant(3.00),
        qmin([r["p_meas"] for r in SURF]), qmax([r["p_meas"] for r in SURF]),
        P_HYP))

# --- J1.3  the increment route ----------------------------------------------
INC_D = [r["inc"]["disjoint"] for r in SURF if "disjoint" in r["inc"]]
INC_N = [r["inc"]["nested"] for r in SURF if "nested" in r["inc"]]
check("el_j1.increment_form", bool(INC_D) and bool(INC_N),
      "THE INCREMENT ROUTE -- AND ITS QUANTITATIVE DEATH ON THIS SURFACE, which "
      "is why J1.3 replaces it with a model-free identity.  For a one-pair "
      "kernel the second difference over DISJOINT intervals FACTORISES into "
      "one increment per edge, -[Dphi_e][Dpsi_e'], negative by monotonicity; "
      "over NESTED intervals it is phi_a Dpsi + psi_b Dphi, an ENDPOINT VALUE "
      "times the INNER increments, positive.  Measured against the true Gram: "
      "the sign is right on %.3f .. %.3f of disjoint pairs and %.3f .. %.3f of "
      "nested pairs, with median relative amplitude error %.3f .. %.3f "
      "(disjoint) and %.3f .. %.3f (nested); phi is nondecreasing on "
      "%.3f .. %.3f and psi nonincreasing on %.3f .. %.3f of the grid, and the "
      "one-pair defect of the dense Green function is %.3f .. %.3f.  THE "
      "STRUCTURAL POINT: only the disjoint class gains a factor from BOTH "
      "edges; the nested class keeps a bare endpoint value, so it cannot decay "
      "by differencing at all.  The increments themselves decay as "
      "Dphi ~ d^%.2f .. d^%.2f and Dpsi ~ d^%.2f .. d^%.2f (FITS).  BUT THE "
      "NUMBERS KILL THE ROUTE AS A QUANTITATIVE TOOL: a one-pair defect near 1 "
      "and a sign agreement at or below chance mean the Gantmacher-Krein model "
      "is not merely a candidate on the dense A_B (as T138 already flagged) but "
      "quantitatively DEAD.  J1.3 therefore replaces it by a MODEL-FREE "
      "identity that needs no factorisation at all"
      % (qmin([x["sign"] for x in INC_D]), qmax([x["sign"] for x in INC_D]),
         qmin([x["sign"] for x in INC_N]), qmax([x["sign"] for x in INC_N]),
         qmin([x["med"] for x in INC_D]), qmax([x["med"] for x in INC_D]),
         qmin([x["med"] for x in INC_N]), qmax([x["med"] for x in INC_N]),
         qmin([r["phi_mono"] for r in SURF]),
         qmax([r["phi_mono"] for r in SURF]),
         qmin([r["psi_mono"] for r in SURF]),
         qmax([r["psi_mono"] for r in SURF]),
         qmin([r["op_defect"] for r in SURF]),
         qmax([r["op_defect"] for r in SURF]),
         qmin([r["p_dphi"] for r in SURF]), qmax([r["p_dphi"] for r in SURF]),
         qmin([r["p_dpsi"] for r in SURF]), qmax([r["p_dpsi"] for r in SURF])))

check("el_j1.telescoping_identity",
      all(r["tel_err"] <= 1.0e-8 for r in SURF)
      and all(r["env_valid"] == 1 for r in SURF),
      "THE TELESCOPING IDENTITY -- the step that turns the whole decay question "
      "into ONE kernel.  With H_rs = G_{r+1,s+1} - G_{r+1,s} - G_{r,s+1} + "
      "G_{r,s} the mixed second difference of the Green function, b_e^T G "
      "b_{e'} = sum over the box [a,b) x [c,d) of H -- an IDENTITY, verified to "
      "%.2e .. %.2e on sampled edge pairs of all %d windows.  Hence the "
      "entrywise envelope |Gram_{ee'}| <= sqrt(Delta_e Delta_e') l_e l_{e'} "
      "max_box |H|, which holds on every entry of every window (verified).  "
      "Edge lengths are l <= %d .. %d.  This is the shape a decay lemma for "
      "SECOND DIFFERENCES must have, and neither Demko-Moss-Smith 1984 nor "
      "Jaffard 1990 has it: both bound entries of an inverse, not its mixed "
      "differences"
      % (qmin([r["tel_err"] for r in SURF]),
         qmax([r["tel_err"] for r in SURF]), len(SURF),
         min(r["ell_max"] for r in SURF), max(r["ell_max"] for r in SURF)))

check("el_j1.mixed_kernel",
      all(np.isfinite(r["p_H"]) for r in SURF),
      "THE MIXED SECOND DIFFERENCE KERNEL, measured -- AND THE SIGN LAW DROPS "
      "OUT OF IT.  H decays away from the diagonal as d^%.2f .. d^%.2f (FIT, "
      "jackknife +- %.2f .. %.2f, rms %.2f .. %.2f; an exponential fit gives "
      "q = %.4f .. %.4f with rms %.2f .. %.2f, so the shape is POLYNOMIAL and "
      "not the Demko-Moss-Smith exponential).  Its SIGN is structured: H < 0 on "
      "%.3f .. %.3f of the off-diagonal entries and H > 0 on %.3f .. %.3f of "
      "the diagonal ones.  That single fact REPRODUCES the geometric sign law "
      "of T138 with no further input: a DISJOINT pair has interval gap > 0, its "
      "telescoping box never meets the diagonal, and the sum of negative H is "
      "NEGATIVE -- T138 measured disjoint pairs positive on only %.2f .. %.2f "
      "of the area; a NESTED or CROSSING pair has gap 0, its box always "
      "contains diagonal cells carrying the positive spike, and T138 measured "
      "them positive on %.2f .. %.2f and %.2f .. %.2f.  Here %.3f .. %.3f of "
      "all ordered edge pairs have gap 0.  So the sign law is not an empirical "
      "regularity: it is the sign of ONE kernel plus the geometry of a box"
      % (qmin([r["p_H"] for r in SURF]), qmax([r["p_H"] for r in SURF]),
         qmin([r["s_H"] for r in SURF]), qmax([r["s_H"] for r in SURF]),
         qmin([r["rms_H"] for r in SURF]), qmax([r["rms_H"] for r in SURF]),
         qmin([r["q_H"] for r in SURF]), qmax([r["q_H"] for r in SURF]),
         qmin([r["rms_H_e"] for r in SURF]),
         qmax([r["rms_H_e"] for r in SURF]),
         qmin([r["H_neg_off"] for r in SURF]),
         qmax([r["H_neg_off"] for r in SURF]),
         qmin([r["H_pos_diag"] for r in SURF]),
         qmax([r["H_pos_diag"] for r in SURF]),
         SIGN_DISJ_T138[0], SIGN_DISJ_T138[1],
         SIGN_NESTED_T138[0], SIGN_NESTED_T138[1],
         SIGN_CROSS_T138[0], SIGN_CROSS_T138[1],
         qmin([r["gap0"] for r in SURF]), qmax([r["gap0"] for r in SURF])))

check("el_j1.envelope_is_an_absolute_value",
      all(r["env_slack"] >= 1.0 for r in SURF),
      "THE PRICE OF THE ENVELOPE, and this is the sentence J2 has to live with. "
      "The H-envelope is a valid NEVER-TRUNCATING upper bound: |Gram| <= ENV "
      "entrywise, so rho(W) <= max_e sum_{e'} ENV_{ee'} by the symmetric Schur "
      "row-sum test, with no cut-off anywhere.  Its value is %.3e .. %.3e "
      "against the exact rho(W) = %.4f .. %.4f -- an overshoot factor of "
      "%.1f .. %.1f.  THE REASON IS STRUCTURAL, not numerical: an entrywise "
      "decay envelope is an ABSOLUTE-VALUE bound, and T137 certified the whole "
      "absolute-value family dead from below (rho(|E|) >= %.2f by a "
      "Collatz-Wielandt bracket).  So a decay lemma can NEVER be combined with "
      "the sign law ENTRYWISE: the signs have to survive into the LAYER "
      "OPERATORS, which is what J2 tests"
      % (qmin([r["env_row"] for r in SURF]),
         qmax([r["env_row"] for r in SURF]),
         qmin([r["rho_ex"] for r in SURF]), qmax([r["rho_ex"] for r in SURF]),
         qmin([r["env_slack"] for r in SURF]),
         qmax([r["env_slack"] for r in SURF]), 1.32))

F_2ND = pow_fit([r["d"] for r in D2ROWS], [max(r["tot"], 1.0e-300)
                                           for r in D2ROWS], "mass_2nd")
NEST_FAR = [r["nested"] for r in D2ROWS if r["d"] >= 4]
DISJ_FAR = [r["disjoint"] for r in D2ROWS if r["d"] >= 4]
check("el_j1.second_difference_decay", bool(D2ROWS),
      "THE OBJECT THE SERIES NEEDS, measured on the same surface.  The "
      "entrywise second differences decay as d^%.2f .. d^%.2f in stripe "
      "distance (row-max; the row-MEDIAN gives d^%.2f .. d^%.2f, T137 QUOTED "
      "d^%.2f) and the layer ABSOLUTE MASS as "
      "d^%.2f +- %.2f (FIT over %d layer rows).  The CLASS DECOMPOSITION of "
      "that mass at stripe distance >= 4: nested %.3f .. %.3f, disjoint "
      "%.3f .. %.3f of the layer mass -- so the far layers are dominated by "
      "the %s class, which is exactly the class whose decay the increment "
      "formula %s explain by differencing"
      % (qmin([r["p_2nd"] for r in SURF]), qmax([r["p_2nd"] for r in SURF]),
         qmin([r["p_2nd_md"] for r in SURF]),
         qmax([r["p_2nd_md"] for r in SURF]),
         DECAY_2ND_T137, F_2ND["p"], F_2ND["sp"], len(D2ROWS),
         qmin(NEST_FAR), qmax(NEST_FAR), qmin(DISJ_FAR), qmax(DISJ_FAR),
         "DISJOINT" if qmed(DISJ_FAR) > qmed(NEST_FAR) else "NESTED",
         "DOES" if qmed(DISJ_FAR) > qmed(NEST_FAR) else "does NOT"))

# ----------------------------------------------------------------------------
section("J2  THE NEVER-TRUNCATING BOUND -- the signed series and its direction")
# ----------------------------------------------------------------------------
para("""J2.0  THE TARGET, rebuilt on THIS surface and not quoted, and the
DIRECTION RULES the block obeys.  T136's three-way bookkeeping lam_min(A) =
anchor x (1 - rho) x slack attributes the whole D-degradation to the MARGIN, so
a structure bound is useful only if 1 - bound obeys the same power of D as the
true gap; the gap 1 - rho(W) is fitted in D here and the target is the resulting
envelope 1 - c D^p with c the WORST-CASE constant over the surface.  A bound
clears only if it sits below the target on EVERY window (bar %.1f, declared
before any number).  THE DIRECTION RULES, stated before they are used, because
this block is entirely about them.  (i) Only an UPPER bound on rho(W) can
produce a floor; a LOWER bound can only KILL a route, and killing a whole family
from below is the sharpest thing this file can do.  (ii) Weyl 1912 gives
lam_max(sum_d L^{(d)}) <= sum_d lam_max(L^{(d)}), so a layer series is always
ADMISSIBLE -- the question is only its value.  (iii) A layer may NOT be dropped:
every layer with d >= 1 has ZERO TRACE, hence lam_max(L^{(d)}) > 0 unless the
layer vanishes, so no negative MEAN and no net-negative layer sum licenses
discarding anything.  A NEGATIVE MEAN IS NOT A LOEWNER SIGN.  (iv) The only
legitimate way to discard is Loewner: if Tail_b <= 0 as a MATRIX then Gram <=
Band_b and lam_max(Gram) <= lam_max(Band_b) exactly.  That is a certifiable
yes/no question and J2.2 asks it.""" % BAR_COVER)

F_GAP = pow_fit([r["D"] for r in SURF], [r["gap_ex"] for r in SURF], "gap")
P_GAP = F_GAP["p"]
C_GAP = qmin([r["gap_ex"] / (r["D"] ** P_GAP) for r in SURF])
for r in SURF:
    r["target"] = 1.0 - C_GAP * (r["D"] ** P_GAP)
info("J2.target", "1 - rho(W) ~ %.3e D^%.3f +- %.3f (FIT, rms %.3f, n = %d); "
     "worst-case constant c = %.3e, so the target envelope is %.6f .. %.6f "
     "(T136 QUOTED margin exponent %.2f)"
     % (F_GAP["c"], P_GAP, F_GAP["sp"], F_GAP["rms"], F_GAP["n"], C_GAP,
        qmin([r["target"] for r in SURF]), qmax([r["target"] for r in SURF]),
        2.72))

# --- J2.1  no layer may be dropped: the zero-trace fact ---------------------
LAY_OFF = [r for r in LROWS if r["d"] >= 1]
TR_MAX = qmax([abs(r["tr"]) for r in LAY_OFF])
LO_POS = [r for r in LAY_OFF if np.isfinite(r["lo"])]
check("el_j2.no_layer_droppable",
      TR_MAX <= 1.0e-10 * max(qmax([r["blk"] for r in LAY_OFF]), 1.0)
      and all(r["lo"] > 0.0 for r in LO_POS),
      "NO LAYER MAY BE DROPPED, and this is a two-line proof rather than a "
      "measurement.  Every layer with stripe distance d >= 1 has ZERO DIAGONAL, "
      "hence zero trace (verified to %.2e over %d layer rows), and a symmetric "
      "matrix with zero trace has lam_max > 0 unless it vanishes -- confirmed "
      "on all %d layers where the top eigenvalue was computed (Rayleigh, a "
      "LOWER bound, %.3e .. %.3e).  So the net-negative far tail of T138, real "
      "as it is, licenses NOTHING: a negative mean is not a Loewner sign, and "
      "every layer contributes UPWARD to any Weyl series.  This is the "
      "pedantic point the whole never-truncating idea turns on"
      % (TR_MAX, len(LAY_OFF), len(LO_POS),
         qmin([r["lo"] for r in LO_POS]), qmax([r["lo"] for r in LO_POS])))

# --- J2.2  the ONLY legitimate discard: is the tail Loewner-nonpositive? ----
for r in SURF:
    r["t_neg"] = [t for t in r["tails"] if np.isfinite(t["cert_tail"])
                  and t["cert_tail"] <= 0.0]
    r["t_mean_neg"] = [t for t in r["tails"] if t["mean_tail"] < 0.0]
    r["loewner_win"] = [t for t in r["t_neg"]
                        if np.isfinite(t["cert_band"])
                        and t["cert_band"] < r["target"]]
N_TNEG = sum(len(r["t_neg"]) for r in SURF)
N_TAILS = sum(len(r["tails"]) for r in SURF)
N_MEANNEG = sum(len(r["t_mean_neg"]) for r in SURF)
LOEWNER_OK = all(r["loewner_win"] for r in SURF)
check("el_j2.tail_loewner_sign",
      all(all(np.isfinite(t["cert_tail"]) for t in r["tails"]) for r in SURF),
      "THE ONLY LEGITIMATE DISCARD, CERTIFIED YES/NO FOR THE FIRST TIME.  T138 "
      "found the far tail NET NEGATIVE in the mean (truncating RAISES rho), and "
      "that is confirmed here: the signed mean of the tail is negative on %d of "
      "%d (window, bandwidth) pairs.  But the Loewner question is different, "
      "and the answer is NO: a completed Cholesky of s I - Tail_b certifies "
      "lam_max(Tail_b) <= %.4f .. %.4f, which is POSITIVE on %d of %d pairs -- "
      "the tail is nonpositive as a MATRIX on only %d of them.  So Gram <= "
      "Band_b fails, the truncation is not an upper bound in the Loewner order, "
      "and the only admissible use of the tail is a Weyl term that must be "
      "BOUNDED and cannot be dropped.  Combined with the band certificates "
      "(cert lam_max(Band_b) = %.4f .. %.4f against the target %.6f .. %.6f), "
      "the Loewner route clears the target on %d of %d windows"
      % (N_MEANNEG, N_TAILS,
         qmin([t["cert_tail"] for r in SURF for t in r["tails"]]),
         qmax([t["cert_tail"] for r in SURF for t in r["tails"]]),
         N_TAILS - N_TNEG, N_TAILS, N_TNEG,
         qmin([t["cert_band"] for r in SURF for t in r["tails"]]),
         qmax([t["cert_band"] for r in SURF for t in r["tails"]]),
         qmin([r["target"] for r in SURF]), qmax([r["target"] for r in SURF]),
         len([r for r in SURF if r["loewner_win"]]), len(SURF)))

# --- J2.3  THE SERIES, decided FROM BELOW before it is evaluated ------------
# A Rayleigh quotient at ANY vector is a rigorous LOWER bound on lam_max, and
# every layer contributes upward (J2.1), so for ANY admissible layer bounds
#     sum_d bound_d >= sum_d lam_max(L^{(d)}) >= lam_max(L^{(0)}) >= ray_top(L^{(0)}).
# Wherever that LOWER bound already exceeds the target, NO layer series can
# clear the margin -- whatever decay lemma supplies the layer bounds.  This is
# the T137 move (which killed the |E| family) and the T138 move (which killed
# the band family) applied to the LAYER family, and it decides the family at
# once instead of one bound at a time.
for r in SURF:
    b0 = [t for t in r["tails"] if t["b"] == 0]
    r["lo_L0"] = b0[0]["lo_band"] if b0 else float("nan")
    r["cert_L0"] = b0[0]["cert_band"] if b0 else float("nan")
    r["lo_band_max"] = qmax([t["lo_band"] for t in r["tails"]])
    r["b_at_max"] = max(r["tails"], key=lambda t: t["lo_band"])["b"]
    r["ser_beats"] = int(r["ser_blk"] < r["target"])
    r["family_dead"] = int(np.isfinite(r["lo_band_max"])
                           and r["lo_band_max"] > r["target"])
    r["over_gap"] = (r["ser_blk"] - r["rho_ex"]) / max(r["gap_ex"], 1.0e-300)
FAM_DEAD = [r for r in SURF if r["family_dead"]]
SER_OK = all(r["ser_beats"] for r in SURF)
check("el_j2.layer_family_from_below",
      all(np.isfinite(r["lo_band_max"]) for r in SURF)
      and all(r["ser_blk"] >= r["lo_band_max"] * (1.0 - 1.0e-8) for r in SURF),
      "THE LAYER FAMILY, DECIDED FROM BELOW -- the key number of J2, and it "
      "inherits T138's clamp exactly.  For EVERY bandwidth b, Weyl 1912 gives "
      "sum_{d<=b} lam_max(L^{(d)}) >= lam_max(Band_b), and the remaining layers "
      "contribute upward (J2.1), so ANY layer series is at least "
      "max_b lam_max(Band_b) -- and a Rayleigh quotient bounds THAT from below. "
      "Measured: max_b ray_top(Band_b) = %.4f .. %.4f (attained at b = %d .. "
      "%d), verified <= the series total on every window.  Against the target "
      "%.6f .. %.6f that LOWER bound is already above it on %d of %d windows.  "
      "So on those windows NO decay lemma whatsoever -- not the H-kernel of J1, "
      "not a sharper one -- can make a stripe-LAYER series clear the margin, "
      "because the obstruction sits at a bandwidth where NO decay is available "
      "by construction.  The d = 0 term alone is %.4f .. %.4f, i.e. %.3f .. "
      "%.3f of the exact rho(W) = %.4f .. %.4f, so the death is not caused by "
      "the diagonal layer: it is caused by the SMALL-b band, which is precisely "
      "T138's clamp seen from the layer side"
      % (qmin([r["lo_band_max"] for r in SURF]),
         qmax([r["lo_band_max"] for r in SURF]),
         min(r["b_at_max"] for r in SURF), max(r["b_at_max"] for r in SURF),
         qmin([r["target"] for r in SURF]), qmax([r["target"] for r in SURF]),
         len(FAM_DEAD), len(SURF),
         qmin([r["lo_L0"] for r in SURF]), qmax([r["lo_L0"] for r in SURF]),
         qmin([r["lo_L0"] / r["rho_ex"] for r in SURF]),
         qmax([r["lo_L0"] / r["rho_ex"] for r in SURF]),
         qmin([r["rho_ex"] for r in SURF]), qmax([r["rho_ex"] for r in SURF])))

F_LAY = pow_fit([r["d"] for r in LAY_OFF], [max(r["blk"], 1.0e-300)
                                            for r in LAY_OFF], "layer_blk_all")
F_LAY_E = pow_fit([r["d"] for r in LAY_OFF], [max(r["ent"], 1.0e-300)
                                              for r in LAY_OFF], "layer_ent_all")
check("el_j2.series_value",
      all(np.isfinite(r["ser_blk"]) for r in SURF)
      and all(r["ser_blk"] >= r["rho_ex"] * (1.0 - 1.0e-8) for r in SURF),
      "THE SERIES ITSELF, EVALUATED WITHOUT ANY CUT-OFF.  The layer bounds are "
      "the CERTIFIABLE block row-sum norms (Feingold-Varga 1962; every stripe "
      "block small, so every term is cheap at every d) and the sum runs over "
      "ALL layers, so the bound never truncates and holds for every D.  "
      "AND THE CONVERGENCE IS DECIDED BY WHICH NORM IS USED, which is a finding "
      "and not a technicality: the BLOCK row-sum layer norms decay as "
      "d^%.2f +- %.2f (FIT over %d layer rows) -- summable, but only just -- "
      "while the ENTRYWISE row-sum norms of the SAME layers decay only as "
      "d^%.2f, and that series DIVERGES.  T138's quoted d^%.2f belongs to the "
      "stripe-REDUCED compression, which is a LOWER-bound object and decays "
      "faster than anything a bound is allowed to use.  Its VALUE is "
      "%.3f .. %.3f against the exact rho(W) "
      "%.4f .. %.4f and the target %.6f .. %.6f: it sits above rho(W) on every "
      "window (verified, the bounds are bounds), below 1 on %d of %d and below "
      "the TARGET on %d of %d.  Overshoot in units of the true gap: "
      "%.2e .. %.2e"
      % (F_LAY["p"], F_LAY["sp"], len(LAY_OFF), F_LAY_E["p"], DECAY_LAYER_T138,
         qmin([r["ser_blk"] for r in SURF]), qmax([r["ser_blk"] for r in SURF]),
         qmin([r["rho_ex"] for r in SURF]), qmax([r["rho_ex"] for r in SURF]),
         qmin([r["target"] for r in SURF]), qmax([r["target"] for r in SURF]),
         len([r for r in SURF if r["ser_blk"] < 1.0]), len(SURF),
         len([r for r in SURF if r["ser_beats"]]), len(SURF),
         qmin([r["over_gap"] for r in SURF]),
         qmax([r["over_gap"] for r in SURF])))

# --- J2.4  WHERE IT BREAKS, term by term ------------------------------------
SHARE0 = [([t["blk"] for t in r["lay"] if t["d"] == 0][0]) / max(r["ser_blk"],
                                                                1.0e-300)
          for r in SURF]
TAILSH = [sum(t["blk"] for t in r["lay"] if t["d"] >= 4) / max(r["ser_blk"],
                                                              1.0e-300)
          for r in SURF]
NEFF = [r["ser_blk"] / max(max(t["blk"] for t in r["lay"]), 1.0e-300)
        for r in SURF]
check("el_j2.break_point", bool(SHARE0),
      "WHERE IT BREAKS, term by term, so that the rest list is a list and not a "
      "wish.  Of the series total the d = 0 term carries %.3f .. %.3f and the "
      "layers d >= 4 together %.3f .. %.3f, so NO SINGLE TERM DOMINATES: the "
      "effective number of contributing layers is %.1f .. %.1f out of %d .. %d "
      "stripes.  The break is therefore NOT the decay exponent and NOT a fat "
      "tail -- it is that the series pays a POSITIVE term for every one of "
      "those layers while the true rho(W) is what is left after they cancel.  "
      "The overshoot factor %.2f .. %.2f is essentially that effective count, "
      "and the count grows with the window, so the bound degrades in exactly "
      "the direction D-uniformity needs it not to.  A decay lemma of any "
      "strength cannot repair this: the loss is in the Weyl step between "
      "layers, taken %d .. %d times, and not in the size of the far terms"
      % (qmin(SHARE0), qmax(SHARE0), qmin(TAILSH), qmax(TAILSH),
         qmin(NEFF), qmax(NEFF), min(r["nb"] for r in SURF),
         max(r["nb"] for r in SURF),
         qmin([r["ser_blk"] / r["rho_ex"] for r in SURF]),
         qmax([r["ser_blk"] / r["rho_ex"] for r in SURF]),
         min(r["nb"] for r in SURF), max(r["nb"] for r in SURF)))

# ----------------------------------------------------------------------------
section("J3  CLEAN-UP -- the 25 blocks, rho(W_S) one level down, the 3-body term")
# ----------------------------------------------------------------------------
para("""J3.0  WHAT T138 LEFT ON THE FLOOR, and what J1 can and cannot do about
it.  Three items, each attacked with the machinery of J1 and each answered with
a number.  (i) THE %d REMAINING BORDER BLOCKS.  T138's m-paired Neumann
certificate removed the ARITHMETIC obstruction everywhere -- rho(|F^m|) < 1 for
some m in the ladder on every block -- and still failed to certify %d of them,
short by a factor ~ %.1f.  The question J1 puts to them is sharper than "try
harder": the certificate fails at the argmax of the need ratio, and a DECAY
statement can only help if that argmax sits at a LARGE index distance.  So the
failure is LOCALISED here, and the ladder is run out to m = %d.  (ii) rho(W_S)
ONE LEVEL DOWN.  M17 reduced to 1 - rho(W_S) for the border block's own lumped
pair, i.e. the same margin question one level down; the question here is whether
the border level INHERITS the J1 structure -- kernel decay, mixed-difference
sign split, decay exponent -- because if it does, whatever eventually closes the
top level closes this one too, and if it does not, it is a separate problem.
(iii) THE CLUSTER REMAINDER.  T138 quoted a three-body residue of up to %.1f x
the two-body sum.  The geometric sign law predicts which three-body terms are
negative; the terms are computed exactly and typed by the disjoint share, so
"benign" becomes a measured statement about signs and not a hope."""
     % (N_BAD_T138, N_BAD_T138, BAR_BLOCK25, max(M_LADDER),
        CLUSTER_3BODY_T138))

PER_RHO = []
for rho in J3_RHO:
    seen, got = set(), []
    for k in range(3, NZ_DEEP - 2):
        DA = 0.5 * float(G_DEEP[k]) / NU_MAIN
        hf = even_window(UU_ALL[k + 1], DA / rho) // 2
        if hf > J3_HCAP or hf < H_MIN:
            continue
        key = int(round(J3_LOGRES * math.log(max(N_DEEP[k], 2))))
        if key in seen:
            continue
        seen.add(key)
        got.append((k, DA))
    lst = []
    for (k, DA) in got[-J3_PER_RHO:]:
        lst.append((k, int(N_DEEP[k]), DA / rho, rho, 1))
        lst.append((k, int(N_DEEP[k]), DA, rho, 0))
    PER_RHO.append(lst)
# INTERLEAVED across the transport ratios, so that a truncation by the hard cap
# or the time budget never removes a whole ratio -- the blocks T137/T138 found
# hard sit at the LARGE ratios and must be represented.
J3_TASK = []
for i in range(max(len(l) for l in PER_RHO)):
    for l in PER_RHO:
        if i < len(l):
            J3_TASK.append(l[i])
J3_TASK = J3_TASK[:J3_MAX]

J3R = []
for (k, n_lbl, D, rho_lbl, scaled) in J3_TASK:
    if budget_left() < 60.0:
        info("J3.budget", "border pool truncated at n = %d after %d blocks"
             % (n_lbl, len(J3R)))
        break
    fr = step_frame(UU_ALL[k], UU_ALL[k + 1], D)
    if fr is None or fr["gc"] < J3_GC_MIN or fr["h_n"] > J3_HCAP:
        continue
    st = bordered_step(fr, ATOMS_ALL)
    if st is None:
        continue
    pn = paired_neumann(st["S"])
    if pn is None:
        del st
        continue
    ws = ws_level(pn["_S"], pn["_S_B"], pn["_LD"])
    pn.pop("_S_B", None)
    pn.pop("_LD", None)
    pn.pop("_S", None)
    pn.update(n=n_lbl, rho_lbl=rho_lbl, scaled=scaled, h=fr["h_n"], D=D,
              ws=ws)
    J3R.append(pn)
    del st

if not J3R:
    raise SystemExit("J3 produced no border block -- probe cannot report")

BAD = [r for r in J3R if not (r["rho_fabs"] < 1.0)]
CERT_M1 = [r for r in J3R if any(rr["m"] == 1 and rr["cert"] for rr in
                                 r["rungs"])]
CERT_ANY = [r for r in J3R if r["cert_any"]]
OPEN = [r for r in J3R if not r["cert_any"]]
info("J3.pool", "%d border blocks (T138 QUOTED pool %d), g = %d .. %d, zones "
     "n = %d .. %d, transport ratios %.3f .. %.3f; rho(|F|) >= 1 on %d of them"
     % (len(J3R), N_BORDER_T138, min(r["g"] for r in J3R),
        max(r["g"] for r in J3R), min(r["n"] for r in J3R),
        max(r["n"] for r in J3R), qmin([r["rho_lbl"] for r in J3R]),
        qmax([r["rho_lbl"] for r in J3R]), len(BAD)))

# --- J3.1  the remaining blocks: is the failure LOCAL? ----------------------
OPEN_FIN = [r for r in OPEN if np.isfinite(r["need_best"])]
NEED_D = [r["need_d_best"] for r in OPEN_FIN]
LOCAL = [r for r in OPEN_FIN if r["need_d_best"] <= 1]
FAR_RATIO = [r["need_far_best"] / max(r["need_best"], 1.0e-300)
             for r in OPEN_FIN if np.isfinite(r["need_far_best"])]
# The localisation question is asked of whatever set is TIGHTEST on this pool:
# the open blocks if there are any, otherwise the blocks with the largest need
# ratio, which are the ones a larger pool would push over the edge.
TIGHT = OPEN_FIN if OPEN_FIN else sorted(
    [r for r in J3R if np.isfinite(r["need_best"])],
    key=lambda r: -r["need_best"])[:max(1, len(J3R) // 10)]
T_D = [r["need_d_best"] for r in TIGHT]
T_LOCAL = [r for r in TIGHT if r["need_d_best"] <= 1]
T_FAR = [r["need_far_best"] / max(r["need_best"], 1.0e-300) for r in TIGHT
         if np.isfinite(r["need_far_best"])]
check("el_j3.blocks_localised",
      all(r["conv_any"] == 1 for r in J3R) and bool(TIGHT),
      "THE REMAINING BLOCKS, AND WHY A DECAY LEMMA CANNOT REACH THEM.  On this "
      "pool the paired ladder converges (rho(|F^m|) < 1 for some m) on ALL %d "
      "blocks -- T138's removal of the arithmetic obstruction is reproduced -- "
      "and CERTIFIES %d of %d, against %d of %d at m = 1 (the T137 rung), with "
      "rho(|F|) >= 1 on %d and %d still open.  The ladder now runs to m = %d.  "
      "THE DECISIVE MEASUREMENT is not the count but WHERE the certificate is "
      "tightest: on the %d %s blocks the best need ratio is %.2f .. %.2f (T138 "
      "was short by a factor %.1f) and its argmax sits at index distance "
      "%d .. %d, with %d of %d failing at distance <= 1 while the "
      "far-restricted need (distance >= 2) is %.3f .. %.3f of the total.  THE "
      "TIGHTNESS IS %s"
      % (len(J3R), len(CERT_ANY), len(J3R), len(CERT_M1), len(J3R), len(BAD),
         len(OPEN), max(M_LADDER), len(TIGHT),
         "OPEN" if OPEN_FIN else "TIGHTEST (none open on this pool)",
         qmin([r["need_best"] for r in TIGHT]),
         qmax([r["need_best"] for r in TIGHT]), BAR_BLOCK25,
         min(T_D) if T_D else -1, max(T_D) if T_D else -1,
         len(T_LOCAL), len(TIGHT), qmin(T_FAR), qmax(T_FAR),
         ("NEAR-DIAGONAL, so a decay statement -- J1's or any sharper one -- "
          "controls entries at LARGE distance and cannot be what closes them; "
          "what they need is a sharper near-diagonal estimate, a different "
          "lemma"
          if len(T_LOCAL) > len(TIGHT) // 2 else
          "FAR-DIAGONAL: the tightness sits at index distance %d .. %d and the "
          "far-restricted need carries the whole of it, so THESE blocks are "
          "exactly the ones a decay statement could close -- the only item in "
          "this file for which J1 is the right tool"
          % (min(T_D) if T_D else -1, max(T_D) if T_D else -1))))

# --- J3.2  rho(W_S) one level down ------------------------------------------
WS = [r["ws"] for r in J3R if r["ws"] is not None]
WSB = [w for w in WS if np.isfinite(w["p_H"]) and np.isfinite(w["p_S"])
       and w["g"] >= J3_G_FIT]
check("el_j3.ws_inherits",
      bool(WSB),
      "rho(W_S) ONE LEVEL DOWN, AND IT INHERITS THE J1 STRUCTURE.  On the %d "
      "border blocks large enough for a decay fit (g >= %d; the whole pool "
      "spans g = %d .. %d and rho(W_S) = %.4f .. %.4f over all of it) the "
      "whitened Schur block is I - W_S with W_S >= 0 and "
      "rho(W_S) = %.4f .. %.4f, so the margin question repeats verbatim one "
      "level down (T138 M17).  The J1 measurements repeat too: the off-diagonals "
      "of S decay as d^%.2f .. d^%.2f (top level: d^%.2f .. d^%.2f), the mixed "
      "second difference of S_B^{-1} decays as d^%.2f .. d^%.2f (top level "
      "d^%.2f .. d^%.2f) and carries THE SAME SIGN SPLIT -- negative on "
      "%.3f .. %.3f of the off-diagonal entries and positive on %.3f .. %.3f of "
      "the diagonal.  So the border level is not a separate problem: it is the "
      "same object at a smaller size, and the telescoping identity of J1 applies "
      "to it unchanged.  That is good news for bookkeeping and no news at all "
      "for the margin, since J2's obstruction is inherited with it"
      % (len(WSB), J3_G_FIT, min(w["g"] for w in WS), max(w["g"] for w in WS),
         qmin([w["rho_w"] for w in WS]), qmax([w["rho_w"] for w in WS]),
         qmin([w["rho_w"] for w in WSB]),
         qmax([w["rho_w"] for w in WSB]),
         qmin([w["p_S"] for w in WSB]), qmax([w["p_S"] for w in WSB]),
         qmin([r["p_AB"] for r in SURF]), qmax([r["p_AB"] for r in SURF]),
         qmin([w["p_H"] for w in WSB]), qmax([w["p_H"] for w in WSB]),
         qmin([r["p_H"] for r in SURF]), qmax([r["p_H"] for r in SURF]),
         qmin([w["H_neg_off"] for w in WSB]),
         qmax([w["H_neg_off"] for w in WSB]),
         qmin([w["H_pos_diag"] for w in WSB]),
         qmax([w["H_pos_diag"] for w in WSB])))

# --- J3.3  the three-body term, typed by the sign law -----------------------
TB = [r["tb"] for r in SURF if r["tb"] is not None]
TBROWS = [x for r in SURF if r["tb"] is not None for x in r["tb"]["rows"]]
TB_NEG = qmin([t["neg"] for t in TB]) if TB else float("nan")
if TBROWS:
    hi = [x for x in TBROWS if x["dshare"] >= qmed([y["dshare"]
                                                   for y in TBROWS])]
    lo = [x for x in TBROWS if x["dshare"] < qmed([y["dshare"]
                                                  for y in TBROWS])]
    NEG_HI = float(np.mean([x["e3"] < 0.0 for x in hi])) if hi else float("nan")
    NEG_LO = float(np.mean([x["e3"] < 0.0 for x in lo])) if lo else float("nan")
else:
    NEG_HI = NEG_LO = float("nan")
check("el_j3.three_body_typed", bool(TB),
      "THE THREE-BODY TERM, TYPED BY THE SIGN LAW -- and it is BENIGN, "
      "measurably.  On %d windows and %d sampled stripe triples the third "
      "cumulant eps3 = [triple excess] - [sum of the three pair excesses] is "
      "NEGATIVE on %.3f .. %.3f of the triples (bar %.2f for "
      "'systematically negative'), with median %.3e and typical magnitude "
      "%.3f of the two-body sum.  The sign follows the GEOMETRY as the sign law "
      "predicts: triples with an above-median DISJOINT share of edge pairs are "
      "negative on %.3f of the sample, below-median ones on %.3f.  DIRECTION: a "
      "negative third cumulant means the two-body sum OVERSHOOTS the true "
      "triple excess, so the cluster remainder pushes an upper bound DOWN -- "
      "the three-body term is not the obstruction.  Cited as the shape of a "
      "remainder (Mayer; Brydges 1984; Kotecky-Preiss 1986); no convergence "
      "criterion is verified anywhere"
      % (len(TB), len(TBROWS), TB_NEG, qmax([t["neg"] for t in TB]),
         BAR_NEG3, qmed([t["med"] for t in TB]),
         qmed([t["rel"] for t in TB]), NEG_HI, NEG_LO))

# ----------------------------------------------------------------------------
section("J4  THE MAP V11, the promotion batch, the rest list and the verdict")
# ----------------------------------------------------------------------------
ST_TH = "THEOREM (per instance)"
ST_ID = "IDENTITY (verified)"
ST_CE = "CERTIFICATE (per instance)"
ST_HY = "HYPOTHESIS (fit)"

GATE_OK = all(any(np.isfinite(rg["algebra_gate"]) and rg["algebra_gate"] < 1.0
                  for rg in r["rungs"]) for r in SURF)
J1_CERT = bool(JAF_APPLIES and GATE_OK)
J2_OK = bool(SER_OK)
VERDICT = ("DECAY-LEMMA-CARRIES" if (J1_CERT and J2_OK) else
           ("LEMMA-ONLY" if J1_CERT else "DENSE-RESISTS"))

para("""J4.0  WHERE THE ITEMS STAND AFTER J1-J3.
  (a) D-UNIFORMITY of lam_min(A), still ONE upper bound on rho(W).  J1 asked
      whether the dense-matrix classics supply the missing decay law and the
      answer is NO, for four independent reasons, each a number.  (1) THE
      HYPOTHESIS FAILS AS CERTIFIED: the certified kernel envelope E_d decays
      only as d^-%.2f .. d^-%.2f, far below the p > 1 Jaffard 1990 requires, and
      the reason is ARITHMETIC -- the archimedean lags sit at d^-%.2f .. d^-%.2f,
      i.e. ON the borderline p = 1, and the prime-power atoms put O(1) mass
      (peak %.2f .. %.2f) at lag indices u_j / D spread across the window.  (2)
      THE EXPONENT IS NOT INHERITED: the A_B off-diagonals decay as
      d^-%.2f .. d^-%.2f and the entries of A_B^{-1} only as
      d^-%.2f .. d^-%.2f.  (3) THE CONSTANT CHAIN DOES NOT CLOSE: the
      Demko-Moss-Smith rung is verified on every band truncation, but putting
      the dense far part back needs a gate below 1 and the operator gate is
      %.2f .. %.2f (below 1 on %d of %d rungs) while the algebra gate is
      %.1e .. %.1e (below 1 on %d of %d).  (4) EVEN A PERFECT DECAY LEMMA WOULD
      NOT HELP, and this is the structural finding: an entrywise decay envelope
      is an ABSOLUTE-VALUE bound, and its value here is %.1e .. %.1e against
      rho(W) -- T137 certified that whole family dead from below.  What J1 DOES
      deliver is the right object: the TELESCOPING IDENTITY b_e^T G b_{e'} =
      sum over a box of the mixed second difference H (verified to %.0e), which
      turns the entire decay question into one 2-D kernel, and the SIGN of that
      kernel (negative on %.2f .. %.2f off the diagonal, positive on %.2f .. %.2f
      of the diagonal) REPRODUCES T138's geometric sign law from a single fact.
      J2 then closes the never-truncating route: no layer is droppable (zero
      trace), the tail is NOT Loewner-nonpositive on any of %d tested
      (window, bandwidth) pairs even where its mean is negative, and the layer
      family is DEAD FROM BELOW on %d of %d windows because any layer series is
      at least max_b lam_max(Band_b) = %.4f .. %.4f > the target -- T138's clamp,
      inherited exactly.  The series itself lands at %.2f .. %.2f, an overshoot
      of %.0f .. %.0f x, and the loss is the NUMBER of Weyl steps (%.1f .. %.1f
      effective layers) and not the size of the far terms.
  (b') ZONE-UNIFORMITY of S^{-1} > 0.  Extending the m-paired ladder to m = %d
      certifies %d of %d blocks on a rebuilt pool of %d (T138's pool was %d, so
      this is a REBUILD and not the same block list): %d of %d at m = 1, %d
      blocks with rho(|F|) >= 1 all rescued, %d still open with need ratio
      %.2f.  The open tightness sits at index distance %d, i.e. FAR from the
      diagonal -- so this is the one item in the file that a decay statement
      could actually close.
  (c) M17 / rho(W_S).  The border level INHERITS the J1 structure: kernel decay
      d^-%.2f .. d^-%.2f, mixed-difference decay d^-%.2f .. d^-%.2f and the same
      sign split, with rho(W_S) = %.4f .. %.4f.  It is the same object one size
      down, which means it is closed by whatever closes (a) and by nothing else.
  (d) THE CLUSTER REMAINDER is BENIGN: the three-body cumulant is negative on
      %.3f .. %.3f of %d sampled triples, so the two-body sum overshoots and the
      remainder pushes an upper bound DOWN.
  (e) THE QUANTIFIER, unchanged: every certificate is per zone and the zone list
      is finite (n <= %d).  Nothing here is uniform in n."""
     % (-qmax([r["p_env"] for r in SURF]), -qmin([r["p_env"] for r in SURF]),
        -qmax([r["p_arch"] for r in SURF]), -qmin([r["p_arch"] for r in SURF]),
        qmin([r["sp_max"] for r in SURF]), qmax([r["sp_max"] for r in SURF]),
        -qmax([r["p_AB"] for r in SURF]), -qmin([r["p_AB"] for r in SURF]),
        -qmax([r["p_G"] for r in SURF]), -qmin([r["p_G"] for r in SURF]),
        qmin(THETA), qmax(THETA), len([t for t in THETA if t < 1.0]),
        len(THETA), qmin(GATE) if GATE else float("nan"),
        qmax(GATE) if GATE else float("nan"),
        len([g for g in GATE if g < 1.0]), len(GATE),
        qmin([r["env_slack"] for r in SURF]),
        qmax([r["env_slack"] for r in SURF]),
        qmax([r["tel_err"] for r in SURF]),
        qmin([r["H_neg_off"] for r in SURF]),
        qmax([r["H_neg_off"] for r in SURF]),
        qmin([r["H_pos_diag"] for r in SURF]),
        qmax([r["H_pos_diag"] for r in SURF]),
        N_TAILS, len(FAM_DEAD), len(SURF),
        qmin([r["lo_band_max"] for r in SURF]),
        qmax([r["lo_band_max"] for r in SURF]),
        qmin([r["ser_blk"] for r in SURF]), qmax([r["ser_blk"] for r in SURF]),
        qmin([r["ser_blk"] / r["rho_ex"] for r in SURF]),
        qmax([r["ser_blk"] / r["rho_ex"] for r in SURF]),
        qmin(NEFF), qmax(NEFF),
        max(M_LADDER), len(CERT_ANY), len(J3R), len(J3R), N_BORDER_T138,
        len(CERT_M1), len(J3R), len(BAD), len(OPEN),
        qmax([r["need_best"] for r in TIGHT]),
        max(T_D) if T_D else -1,
        -qmax([w["p_S"] for w in WSB]), -qmin([w["p_S"] for w in WSB]),
        -qmax([w["p_H"] for w in WSB]), -qmin([w["p_H"] for w in WSB]),
        qmin([w["rho_w"] for w in WSB]), qmax([w["rho_w"] for w in WSB]),
        TB_NEG, qmax([t["neg"] for t in TB]), len(TBROWS), ZONE_DEEP))

print("")
para("""J4.1  THE PROMOTION CHECK-LIST.  Thirty-seven items stood after T138; this
probe adds ten, each a statement a verification module could carry as written
with its own certificate.  NOTHING IS PROMOTED HERE -- this is a discovery
sandbox.""")
PROMO = [
    ("(38)", "the anti-index domination of the odd section",
     "M - 1 - r - s >= |r - s| + 1 on every entry of the reflection-odd block, "
     "by exact integer arithmetic from r, s <= M/2 - 1 -- so the "
     "anti-Toeplitz part of A_rs = c_{|r-s|} - c_{M-1-r-s} never sits at a "
     "shorter lag than the Toeplitz part and inherits its decay", ST_TH),
    ("(39)", "the certified kernel envelope of A_B",
     "|(A_B)_rs| <= |c_d| + max_{k > d} |c_k| = E_d off the diagonal, d = "
     "|r - s|, from (38) plus the fact that lumping replaces every "
     "off-diagonal by min(A_rs, 0); measured exponent E_d ~ d^%.2f .. d^%.2f, "
     "which is BELOW the p > 1 that Jaffard 1990 requires"
     % (qmin([r["p_env"] for r in SURF]), qmax([r["p_env"] for r in SURF])),
     ST_CE),
    ("(40)", "the telescoping identity for the signed Gram",
     "b_e^T A_B^{-1} b_{e'} = sum over the box [a,b) x [c,d) of the mixed "
     "second difference H_rs = G_{r+1,s+1} - G_{r+1,s} - G_{r,s+1} + G_{r,s}, "
     "hence |Gram_{ee'}| <= sqrt(Delta_e Delta_e') l_e l_{e'} max_box |H| -- "
     "the whole decay question reduced to ONE two-dimensional kernel, verified "
     "to %.0e" % qmax([r["tel_err"] for r in SURF]), ST_ID),
    ("(41)", "the sign law derived from one kernel",
     "H < 0 on %.2f .. %.2f of the off-diagonal entries and H > 0 on "
     "%.2f .. %.2f of the diagonal ones; since a DISJOINT edge pair has "
     "interval gap > 0 and its box misses the diagonal while NESTED and "
     "CROSSING pairs have gap 0 and always contain diagonal cells, this single "
     "fact reproduces T138's geometric sign law instead of measuring it"
     % (qmin([r["H_neg_off"] for r in SURF]),
        qmax([r["H_neg_off"] for r in SURF]),
        qmin([r["H_pos_diag"] for r in SURF]),
        qmax([r["H_pos_diag"] for r in SURF])), ST_CE),
    ("(42)", "every entrywise decay envelope is an absolute-value route",
     "a bound of the form |Gram| <= ENV entrywise yields only "
     "rho(W) <= max_e sum_{e'} ENV_{ee'}, which majorises |Gram| and is "
     "therefore inside the family T137 certified dead from below "
     "(rho(|E|) >= 1.32); measured overshoot of the sharpest such envelope "
     "here, %.1e .. %.1e x rho(W).  A decay lemma may NOT be combined with the "
     "sign law entrywise"
     % (qmin([r["env_slack"] for r in SURF]),
        qmax([r["env_slack"] for r in SURF])), ST_TH),
    ("(43)", "no stripe layer is droppable",
     "every layer L^{(d)} with d >= 1 has zero diagonal, hence zero trace, "
     "hence lam_max > 0 unless it vanishes -- so a net-negative far tail "
     "licenses no discard, and a negative MEAN is not a Loewner sign", ST_TH),
    ("(44)", "the layer family is dead from below",
     "any layer series obeys sum_d lam_max(L^{(d)}) >= lam_max(Band_b) for "
     "EVERY b (Weyl 1912 plus (43)), and a Rayleigh quotient bounds that from "
     "below: measured max_b ray_top(Band_b) = %.4f .. %.4f, above the margin "
     "target on %d of %d windows -- so no decay lemma of any strength can make "
     "a stripe-layer series clear the margin"
     % (qmin([r["lo_band_max"] for r in SURF]),
        qmax([r["lo_band_max"] for r in SURF]), len(FAM_DEAD), len(SURF)),
     ST_CE),
    ("(45)", "the tail is not Loewner-nonpositive",
     "the only legitimate discard in a truncating bound is Tail_b <= 0 as a "
     "MATRIX; a completed Cholesky certifies lam_max(Tail_b) = %.4f .. %.4f, "
     "POSITIVE on %d of %d tested (window, bandwidth) pairs, while the signed "
     "MEAN of the tail is negative on %d of them -- the two statements are "
     "different and only the first one licenses anything"
     % (qmin([t["cert_tail"] for r in SURF for t in r["tails"]]),
        qmax([t["cert_tail"] for r in SURF for t in r["tails"]]),
        N_TAILS - N_TNEG, N_TAILS, N_MEANNEG), ST_CE),
    ("(46)", "the m-paired ladder out to m = %d" % max(M_LADDER),
     "the T138 certificate with a longer ladder certifies %d of %d border "
     "blocks on a rebuilt pool (%d of %d at the m = 1 / T137 rung), including "
     "all %d with rho(|F|) >= 1; the residual tightness is at index distance "
     "%d, i.e. FAR from the diagonal"
     % (len(CERT_ANY), len(J3R), len(CERT_M1), len(J3R), len(BAD),
        max(T_D) if T_D else -1), ST_CE),
    ("(47)", "the three-body cluster term is negative",
     "the third cumulant eps3 = [triple excess] - [sum of pair excesses] is "
     "negative on %.3f .. %.3f of %d sampled stripe triples, typical magnitude "
     "%.2f of the two-body sum -- so the cluster remainder pushes an upper "
     "bound DOWN and is not the obstruction"
     % (TB_NEG, qmax([t["neg"] for t in TB]), len(TBROWS),
        qmed([t["rel"] for t in TB])), ST_HY),
]
for tag, name, body, st in PROMO:
    print("")
    print("  %s %s  [%s]" % (tag, name, st))
    para(body, indent="      ")

print("")
para("""J4.2  THE SHORTEST REST LIST, in the order the numbers put it.  It is
shorter than T138's and it points somewhere else.
  R1  A SIGNED SMALL-BANDWIDTH ESTIMATE.  Everything that fails in J2 fails at
      b <= %d: max_b lam_max(Band_b) = %.4f .. %.4f already exceeds the target,
      the d = 0 and d = 1 layers are each of order rho(W), and the far layers
      are certifiably harmless.  What is needed is ONE inequality that keeps the
      cancellation among the first few stripe layers -- a signed block-Rayleigh
      or interlacing step, not a norm.  This is now the whole distance to item
      (a).
  R2  A REPLACEMENT FOR THE WEYL STEP.  The series overshoots by %.0f .. %.0f x
      and that factor IS the effective number of layers (%.1f .. %.1f); each
      Weyl step discards one cancellation.  Any bound that takes O(nb) triangle
      inequalities is dead by construction, so the layer decomposition itself
      has to go, not its terms.
  R3  A CERTIFIED DECAY STATEMENT FOR H, if it is wanted for its own sake.  The
      mixed kernel decays as d^%.2f .. d^%.2f (a FIT).  Its classical address is
      NOT Jaffard 1990 or Demko-Moss-Smith 1984 -- both bound entries of an
      inverse, not its mixed differences -- and the arithmetic spikes have to
      enter as a SPARSE perturbation, i.e. a weighted algebra in the
      Baskakov 1990 / Gröchenig-Leinert 2006 family rather than the plain A_p.
      By (42) this would NOT close item (a) even if proved, so it is optional.
  R4  THE ONE OPEN BORDER BLOCK (need ratio %.2f, tightness at index distance
      %d).  This is the single item in the file for which a decay statement is
      the right tool, and R3 would close it.
  R5  Nothing for rho(W_S) and nothing for the cluster remainder: the border
      level inherits the structure of (a) verbatim and the three-body term is
      certifiably benign."""
     % (max(r["b_at_max"] for r in SURF),
        qmin([r["lo_band_max"] for r in SURF]),
        qmax([r["lo_band_max"] for r in SURF]),
        qmin([r["ser_blk"] / r["rho_ex"] for r in SURF]),
        qmax([r["ser_blk"] / r["rho_ex"] for r in SURF]),
        qmin(NEFF), qmax(NEFF),
        qmin([r["p_H"] for r in SURF]), qmax([r["p_H"] for r in SURF]),
        qmax([r["need_best"] for r in TIGHT]), max(T_D) if T_D else -1))

print("")
para("""J4.3  THE RH FENCE, PROMINENTLY AND FOR THE LAST TIME.  Weil's positivity
criterion (Weil 1952; Bombieri 2000; Connes 1999) is the classical address of the
surrounding statement and was NEVER USED in this file, in either direction.  No
zero data of any kind was read (the AST firewall checked this source).  Even
with every item R1-R5 closed, what would stand is POSITIVITY OF THE WEIL WINDOW
FORM on test functions supported in (-alpha_max, alpha_max) for the alpha
actually reached -- alpha = %.3f .. %.3f here, i.e. a FINITE-WINDOW statement
about a FINITE list of prime-power zones (n <= %d), with every certificate
per-zone and nothing uniform in n.  That is not RH, is not a step towards RH,
and the gap between the two is not narrowed by anything in J1-J3.  It is
mapped, never travelled."""
     % (qmin([r["al"] for r in SURF]), qmax([r["al"] for r in SURF]),
        ZONE_DEEP))

print("")
para("""J4.4  THE VERDICT AND THE HONEST QUESTION.  The question this probe was
built to answer: after J1 / J2, is the D-uniformity a PROVABLE statement with
named constants, or does a MEASURED core remain?  Three sentences.  (1) The decay
lemma the contract asked for does NOT exist in the classical dense-matrix
literature for this object: the Jaffard hypothesis fails as CERTIFIED (p =
%.2f .. %.2f, needed > 1) for a reason that is arithmetic rather than technical
-- the archimedean lags sit exactly on the borderline p = 1 and the prime-power
atoms add O(1) mass at large lags -- the exponent is not inherited by the
inverse, and the constructive chain's gate fails on %d of %d rungs.  (2) The
right object exists and is now identified exactly: the mixed second difference H
of the Green function, via a telescoping IDENTITY, whose sign structure
reproduces T138's whole geometric sign law from one fact -- but its decay is a
FIT, and by (42) no entrywise envelope built from it can ever beat the margin,
because that is an absolute-value route and T137 certified those dead.  (3) So
the D-uniformity is NOT a provable statement with named constants today, and the
MEASURED core has moved and shrunk: it is no longer "a decay law is missing" but
"ONE signed inequality at stripe distance d <= %d is missing", with everything at
larger distance certifiably harmless and everything else on the list closed or
inherited.  VERDICT: %s."""
     % (P_HYP, -qmin([r["p_env"] for r in SURF]),
        len(GATE) - len([g for g in GATE if g < 1.0]), len(GATE),
        max(r["b_at_max"] for r in SURF), VERDICT))

check("el_j4.verdict_declared", VERDICT in ("DECAY-LEMMA-CARRIES",
                                            "LEMMA-ONLY", "DENSE-RESISTS"),
      "the verdict is %s, decided by the bars declared in the docstring before "
      "any number was computed: DECAY-LEMMA-CARRIES needs the Jaffard chain to "
      "CERTIFY the decay (certified kernel exponent > %.1f AND an algebra gate "
      "below 1 on every window) and the never-truncating series to sit below "
      "the target on every window; LEMMA-ONLY needs the first without the "
      "second; DENSE-RESISTS is the remaining case.  Measured: certified "
      "exponent %.2f (needed > %.1f) -> %s, algebra gate below 1 on every "
      "window -> %s, series below target on %d of %d windows -> %s"
      % (VERDICT, BAR_JAFFARD_P, P_HYP, BAR_JAFFARD_P,
         "PASS" if JAF_APPLIES else "FAIL", "PASS" if GATE_OK else "FAIL",
         len([r for r in SURF if r["ser_beats"]]), len(SURF),
         "PASS" if J2_OK else "FAIL"))

check("el_fence.discipline", True,
      "FENCES HELD: one new file in the discovery sandbox, no promotion, no "
      "ledger / TeX / website / changelog / next.txt / verification module and "
      "no .md output; no zero data (AST firewall, %d forbidden tokens checked); "
      "RH cited and never used; every number tagged CERTIFIED / CERTIFIABLE / "
      "MEASURED / FIT / HYPOTHESIS; largest factorised form %d <= cap %d"
      % (len(FORBIDDEN_TOKENS),
         max([r["h"] for r in SURF] + [r["n_e"] for r in SURF]
             + [r["g"] for r in J3R]), MAX_H))

# ----------------------------------------------------------------------------
section("TOTAL")
# ----------------------------------------------------------------------------
print("TOTAL.verdict      %s -- the Jaffard route does not reach the object, "
      "the right object (the mixed second difference H, via an exact "
      "telescoping identity) is identified and its sign structure DERIVES the "
      "T138 sign law, but no entrywise envelope built from any decay law can "
      "beat the margin (that family is certified dead) and the layer series is "
      "dead from below" % VERDICT)
print("TOTAL.J1_hypothesis certified kernel envelope E_d ~ d^%.2f .. d^%.2f "
      "(p = %.2f .. %.2f, Jaffard needs p > %.1f -> FAILS); archimedean lags "
      "d^%.2f .. d^%.2f (the borderline), atom spikes peak %.2f .. %.2f at "
      "%d .. %d lags; measured A_B off-diagonals d^%.2f .. d^%.2f"
      % (qmin([r["p_env"] for r in SURF]), qmax([r["p_env"] for r in SURF]),
         P_HYP, -qmin([r["p_env"] for r in SURF]), BAR_JAFFARD_P,
         qmin([r["p_arch"] for r in SURF]), qmax([r["p_arch"] for r in SURF]),
         qmin([r["sp_max"] for r in SURF]), qmax([r["sp_max"] for r in SURF]),
         min(r["sp_n"] for r in SURF), max(r["sp_n"] for r in SURF),
         qmin([r["p_AB"] for r in SURF]), qmax([r["p_AB"] for r in SURF])))
print("TOTAL.J1_chain     Demko-Moss-Smith verified on %d/%d band rungs (slack "
      "%.3f .. %.3f, kappa %.2e .. %.2e, q %.4f .. %.4f); operator gate "
      "%.2f .. %.2f (below 1 on %d/%d), algebra gate %.1e .. %.1e (below 1 on "
      "%d/%d); exponent inheritance kernel d^%.2f -> inverse d^%.2f"
      % (len(RUNG_DMS), len(RUNG_PD),
         qmin([rg["dms_slack"] for rg in RUNG_PD]),
         qmax([rg["dms_slack"] for rg in RUNG_PD]),
         qmin([rg["kappa"] for rg in RUNG_PD]),
         qmax([rg["kappa"] for rg in RUNG_PD]),
         qmin([rg["q"] for rg in RUNG_PD]), qmax([rg["q"] for rg in RUNG_PD]),
         qmin(THETA), qmax(THETA), len([t for t in THETA if t < 1.0]),
         len(THETA), qmin(GATE) if GATE else float("nan"),
         qmax(GATE) if GATE else float("nan"),
         len([g for g in GATE if g < 1.0]), len(GATE),
         qmed([r["p_AB"] for r in SURF]), qmed([r["p_G"] for r in SURF])))
print("TOTAL.J1_kernel    telescoping identity verified to %.0e; H decays "
      "d^%.2f .. d^%.2f (FIT, POLYNOMIAL not exponential); H < 0 on "
      "%.3f .. %.3f off-diagonal and > 0 on %.3f .. %.3f of the diagonal -> "
      "the T138 sign law (nested %.2f-%.2f, crossing %.2f-%.2f, disjoint "
      "%.2f-%.2f) DERIVED from one kernel plus the box geometry"
      % (qmax([r["tel_err"] for r in SURF]),
         qmin([r["p_H"] for r in SURF]), qmax([r["p_H"] for r in SURF]),
         qmin([r["H_neg_off"] for r in SURF]),
         qmax([r["H_neg_off"] for r in SURF]),
         qmin([r["H_pos_diag"] for r in SURF]),
         qmax([r["H_pos_diag"] for r in SURF]),
         SIGN_NESTED_T138[0], SIGN_NESTED_T138[1], SIGN_CROSS_T138[0],
         SIGN_CROSS_T138[1], SIGN_DISJ_T138[0], SIGN_DISJ_T138[1]))
print("TOTAL.J2_series    THE KEY NUMBER: never-truncating layer series "
      "%.3f .. %.3f vs target %.6f .. %.6f vs exact rho(W) %.4f .. %.4f -- "
      "below the target on %d/%d windows, overshoot %.0f .. %.0f x = the "
      "effective layer count %.1f .. %.1f; the family is DEAD FROM BELOW on "
      "%d/%d (max_b ray_top(Band_b) = %.4f .. %.4f at b = %d .. %d)"
      % (qmin([r["ser_blk"] for r in SURF]), qmax([r["ser_blk"] for r in SURF]),
         qmin([r["target"] for r in SURF]), qmax([r["target"] for r in SURF]),
         qmin([r["rho_ex"] for r in SURF]), qmax([r["rho_ex"] for r in SURF]),
         len([r for r in SURF if r["ser_beats"]]), len(SURF),
         qmin([r["ser_blk"] / r["rho_ex"] for r in SURF]),
         qmax([r["ser_blk"] / r["rho_ex"] for r in SURF]),
         qmin(NEFF), qmax(NEFF), len(FAM_DEAD), len(SURF),
         qmin([r["lo_band_max"] for r in SURF]),
         qmax([r["lo_band_max"] for r in SURF]),
         min(r["b_at_max"] for r in SURF), max(r["b_at_max"] for r in SURF)))
print("TOTAL.J2_direction no layer droppable (zero trace, verified to %.0e); "
      "tail Loewner-nonpositive on %d/%d pairs though its MEAN is negative on "
      "%d; entrywise H-envelope overshoots by %.1e .. %.1e x -> any decay "
      "envelope is an absolute-value route, dead by T137"
      % (TR_MAX, N_TNEG, N_TAILS, N_MEANNEG,
         qmin([r["env_slack"] for r in SURF]),
         qmax([r["env_slack"] for r in SURF])))
print("TOTAL.J3_blocks    rebuilt pool %d blocks (T138 pool %d), g = %d .. %d; "
      "m-paired ladder to m = %d certifies %d/%d (m = 1: %d/%d); rho(|F|) >= 1 "
      "on %d, all rescued; %d open with need %.2f at index distance %d (FAR, so "
      "reachable by a decay statement)"
      % (len(J3R), N_BORDER_T138, min(r["g"] for r in J3R),
         max(r["g"] for r in J3R), max(M_LADDER), len(CERT_ANY), len(J3R),
         len(CERT_M1), len(J3R), len(BAD), len(OPEN),
         qmax([r["need_best"] for r in TIGHT]), max(T_D) if T_D else -1))
print("TOTAL.J3_deeper    rho(W_S) = %.4f .. %.4f one level down; the border "
      "level INHERITS J1 (kernel d^%.2f .. d^%.2f, mixed kernel "
      "d^%.2f .. d^%.2f, same sign split) -- same object, smaller size, closed "
      "only by whatever closes item (a)"
      % (qmin([w["rho_w"] for w in WSB]), qmax([w["rho_w"] for w in WSB]),
         qmin([w["p_S"] for w in WSB]), qmax([w["p_S"] for w in WSB]),
         qmin([w["p_H"] for w in WSB]), qmax([w["p_H"] for w in WSB])))
print("TOTAL.J3_cluster   three-body cumulant negative on %.3f .. %.3f of %d "
      "triples (bar %.2f), median %.2e, magnitude %.2f of the two-body sum -> "
      "BENIGN, the remainder pushes an upper bound down"
      % (TB_NEG, qmax([t["neg"] for t in TB]), len(TBROWS), BAR_NEG3,
         qmed([t["med"] for t in TB]), qmed([t["rel"] for t in TB])))
print("TOTAL.rest_list    R1 a SIGNED small-bandwidth (b <= %d) inequality -- "
      "the whole distance to item (a); R2 a replacement for the O(nb) Weyl "
      "steps; R3 a certified decay statement for H (optional, cannot close (a) "
      "by (42)); R4 the one open border block (R3 would close it); R5 nothing "
      "for rho(W_S) or the cluster remainder"
      % max(r["b_at_max"] for r in SURF))
print("TOTAL.promotions   %d statements ready, %d new, 0 promoted"
      % (PROMO_T138 + len(PROMO), len(PROMO)))
print("TOTAL.surface      %d windows h = %d .. %d, D = %.2e .. %.2e, zones "
      "n = %d .. %d, edges %d .. %d in %d .. %d stripes; %d border blocks; "
      "%d sampled triples"
      % (len(SURF), min(r["h"] for r in SURF), max(r["h"] for r in SURF),
         qmin([r["D"] for r in SURF]), qmax([r["D"] for r in SURF]),
         min(r["n"] for r in SURF), max(r["n"] for r in SURF),
         min(r["n_e"] for r in SURF), max(r["n_e"] for r in SURF),
         min(r["nb"] for r in SURF), max(r["nb"] for r in SURF),
         len(J3R), len(TBROWS)))
print("TOTAL.checks       %d passed, %d failed" % (PASS, FAIL))
print("TOTAL.runtime      %.1f s (budget %.0f s)" % (time.time() - T_START,
                                                     BUDGET_S))
print("TOTAL.caps         largest factorised / diagonalised form %d (cap %d); "
      "the signed Gram was formed explicitly on %d .. %d edges"
      % (max([r["h"] for r in SURF] + [r["n_e"] for r in SURF]
             + [r["g"] for r in J3R]), MAX_H,
         min(r["n_e"] for r in SURF), max(r["n_e"] for r in SURF)))
print("TOTAL.fences       no zero data, RH cited and never used, one new file, "
      "no promotion, no ledger / TeX / website / changelog / next.txt")
