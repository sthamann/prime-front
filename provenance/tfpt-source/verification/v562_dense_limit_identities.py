"""v562 -- PRIME.DENSE.LIMIT.01: the dense-limit identities (T176).

THE ENDGAME OF THE PHASE-2 MEASUREMENT PROGRAMME, ITS EXACT CORES AS ALGEBRA.
T176 (contract DENSE.LIMIT, probe dense_limit_probe.py, 24/24, 118.7 s,
verdict SITS-AT-ZERO) raised the von-Mangoldt sieve by a factor 20.8 (ATOM_MAX
1.2e6 -> 2.5e7, density ceiling 361 -> 6120) and extended the deficit(dens)
curve by two preregistered ratio-4 bins; both new bins are CONSISTENT WITH
ZERO (pooled +0.0496 +- 0.0372, 1.3 sigma), the plateau window narrows by a
factor 3.6 (0.264 -> 0.074 at 2 sigma), and the phase-2 measurement programme
CLOSES AS PLANNED.  THIS module is the load-bearing version of the exact,
theorem-shaped cores of that endgame -- per instance, machine-checkable, each
with a mutation control, on a SMALL declared surface (the big sieve is NOT
rebuilt here: the identities are sieve-size-free, which is their point):

[E] (1) R1 CLOSED -- THE FEYNMAN-HELLMANN IDENTITY (T176 P2, the strongest).
    R = (lam_min/lam_max)/DEL with DEL = 1 - r_12^2, so
        dlog R/ddelta = v^T dA~ v / lam_min - w^T dA~ w / lam_max - dDEL/DEL,
    where dA~ is the odd-Toeplitz image of the EXACT lag derivative dc/ddelta
    (the assembly moves 0.5 mu_p per unit phase between two adjacent lag
    cells and NOTHING else, so dc/ddelta is exact and piecewise constant --
    THEOREM T3 of T176) and v, w are the extreme eigenvectors of the
    normalised low block (Hellmann 1937, Feynman 1939: dlambda = v^T dA v
    for a simple eigenvalue of a symmetric matrix).  Verified per instance
    against the full nonlinear rebuild on a DECLARED central-difference step
    ladder whose U-SHAPE is exhibited: the residual has an interior minimum
    (truncation error above, round-off amplification below), which a wrong
    formula cannot have -- a wrong formula has a floor.  T175's intervention
    regression (dlog R/ddelta = 879, measured) is thereby retired as a
    separate claim: it is an identity about the assembly, not a fit.
[E] (2) THE PHASE POLE (T176 P3; replaces the 300x harmonic anomaly).  On
    the same instances the full phase period is swept on a declared grid:
    positive definiteness of the low block survives only a small fraction of
    the period, so lam_min changes sign INSIDE the period and log R has a
    POLE there; the bisected loss point delta_PD satisfies
    delta_PD x |dlog R/ddelta| = O(1) (a pole at the natural scale), and the
    two lowest modes of the normalised low block are ALREADY nearly
    degenerate at delta = 0 -- the intervention does not create a crossing,
    it walks along one.  CONSEQUENCE, wired as the reading: a first-harmonic
    regression of log R over the period estimates a Fourier coefficient of a
    function with a pole in the interval, which is why T175's harmonic came
    out ~300x below the local derivative -- NOTHING is wrong with either
    number; they measure different things.
[E] (3) SIEVE CONSISTENCY (T176 P4).  A bigger sieve adds atoms ABOVE the
    old cap and nothing else, so every cell whose comb was already complete
    under the old cap is UNCHANGED BY CONSTRUCTION: the lag vectors agree
    bit for bit, R agrees exactly, and the bin deficit computed under the
    old and the new table is IDENTICAL on the shared anchors -- the audit
    that lets any later probe raise ATOM_MAX without re-deriving the chain
    (T176 re-measured all six T175 bins at 0.0 sigma; here the same
    statement is checked at construction level).  Must-break: an anchor
    whose zone runs past the old cap has a truncated comb there, and its
    cell CHANGES under the bigger sieve -- the no-op is a theorem about
    complete combs, not about sieves.
[E] (4) THE CURVE ESTIMATOR AS A PROCEDURE + THE LADDER CAVEAT AS CONTENT
    (T176 P1 + the anti-promotion).  The cluster-robust bin statistic of
    T175/T176 -- one OLS slope of log|R| on log h per anchor from its cells
    inside a declared density bin, then the unweighted mean of the anchor
    slopes with the cluster-robust s.e. of that mean -- is DETERMINISTIC and
    exactly reproducible (two independent evaluation orders agree to
    round-off).  AND THE ANTI-PROMOTION IS WIRED AS A CHECK: the SAME bin
    deficit computed on the fine 2^(1/4) rung ladder and on its coarse
    sqrt(2) sub-ladder DIFFERS (log R is curved in log h -- T176 measured
    a2 = -0.0842 +- 0.0085 -- so a ratio-4 bin with ~12 rungs samples the
    curvature differently from one with ~6), i.e. THE ESTIMATOR IS
    LADDER-DEPENDENT: any ledger row quoting a bin deficit must quote the
    rung ladder with it, or the number is not reproducible.  T176 measured
    the shift at up to 0.20 on its surface; the module exhibits the
    mechanism per instance.

NAMED LIMITS AS LOAD-BEARING CONTENT (the claim INCLUDES them):
  (i)   THE VERDICT IS A MEASUREMENT, NOT A CLAIM OF THIS MODULE.  T176's
        SITS-AT-ZERO -- the extended curve +0.8886 -> +0.5148 -> +0.1948 ->
        +0.3922 -> +0.1520 -> +0.0579 -> +0.0376 +- 0.0410 -> +0.1046 +-
        0.0881 over 4.0 decades of comb density, pooled +0.0496 +- 0.0372
        over the two new bins, density slope 8.0 sigma, plateau window
        0.264 -> 0.074 (2 sigma) -- is a sandbox MEASURED number on T176's
        2.5e7 surface WITH ITS RUNG LADDER (the 2^(1/4) ladder containing
        T175's seven rungs), and it is NOT consumed here.  THE LADDER
        CAVEAT IS PART OF THE QUOTE.
  (ii)  THE LIMIT STAYS OPEN AND TYPED OPEN.  A true zero at finite
        density, a power-law approach to zero and a plateau below 0.074
        remain INDISTINGUISHABLE under any finite sieve reachable by
        resources (the window narrows like the square root of the anchor
        cap: one more decade would cost ATOM_MAX ~ 2.5e9).  No limit is
        claimed, the open quantifier at link 16 is untouched, and the
        phase-2 CLOSURE is a closure of the MEASUREMENT PROGRAMME (the
        planned instrument is exhausted), not of the question.
  (iii) The curvature map stays sandbox: both channels (log h +0.1529 +-
        0.0258, log dens -0.0434 +- 0.0060) and the failure of all six
        preregistered reparametrisations (the data wants dens^{+0.284} h --
        no candidate) are T176 MEASURED/FIT items on its surface, not
        consumed here.
HONEST FENCES: NO RH statement anywhere -- RH_DELTA = 0.5 is a yardstick in
exactly one role; the arithmetic input is a FINITE von Mangoldt table below a
declared cap (Chebyshev 1852 / Rosser-Schoenfeld 1962, verified on the
table), a bigger sieve is a bigger finite table and nothing else; no zero of
any L-function is read and no L-function is evaluated (AST firewall); the
Weil fence is hard (positivity of a finite A_h is never routed through the
Weil criterion; Weil 1952 cited, never used); Feynman-Hellmann (Hellmann
1937, Feynman 1939), Schur 1917, Kac-Murdock-Szego 1953, Dirichlet 1829,
Chebyshev 1852 named CLASSICAL.  Status: [E] per-instance identities and
certified inequalities with mutation controls; deterministic (fixed seeds,
no wall-clock dependence); Python-only, counted per GATE.WOLFRAM.02.
Discovery provenance:
  experiments/tfpt-discovery/dense_limit_probe.py   (T176, 24/24,
  SITS-AT-ZERO; the phase-2 measurement programme closes as planned)
"""
from __future__ import annotations

import ast
import math
import time

import numpy as np

from tfpt_constants import check, summary, reset

# ---------------------------------------------------------------- budgets
ATOM_MAX = 320000            # the NEW (small) table cap of this module
ATOM_MAX_OLD = 120000        # the OLD cap of the consistency check (S3)
GL_N = 48
CHUNK = 16384
EULER = 0.5772156649015328606065120900824
LOG_PI = math.log(math.pi)

KB_MAX = 32                  # parity modes carried
SCHUR_KB = 16                # the low block of the T152..T176 chain
EPSM = float(np.finfo(float).eps)

# --- the declared surface (fixed BEFORE any number) ---------------------------
ANCHOR_LO = 40               # every anchor n has a COMPLETE comb: n^2 <= cap
H_FINE = (128, 152, 181, 215, 256, 304)   # the 2^(1/4) ladder (T176's ratio)
H_COARSE = (128, 181, 256)                # the sqrt(2) sub-ladder (T175's)
DENS_BIN = (6.4, 102.4)      # ONE declared T175/T176 ratio-4x2 bin (S4)
N_FH_CELLS = 6               # declared FH instances (mid-rung, spread anchors)
N_POLE_CELLS = 4             # declared pole instances (densest anchors)
FD_GRID = (1.0e-8, 1.0e-7, 1.0e-6, 1.0e-5, 1.0e-4)   # DECLARED step ladder
PHASE_FAM = (2, 3, 5, 7, 11, 13)          # T175/T176's PRIMARY family
N_PER = 64                   # declared period grid (no harmonic hunting)
N_BIS = 40                   # declared bisection depth

# --- the Chebyshev input, preregistered (T162..T176) --------------------------
KAPPA_X0 = 100.0
KAPPA_REF = 0.038821
TOL_KAPPA = 1.0e-6
B_PSI = 1.03883              # psi(x) <= B_PSI x (Chebyshev 1852; RS 1962)

# --- the ledger exponents / T176 numbers (YARDSTICKS + quotes, not claims) ----
RH_DELTA = 0.5               # RH-equivalent strength, a YARDSTICK only
T176_POOLED = 0.0496         # T176 pooled new-bin deficit -- sandbox MEASURED,
T176_POOLED_SE = 0.0372      # quoted for documentation, NOT consumed
T176_PLATEAU = 0.0744        # T176 2-sigma plateau window -- quoted only
T175_DLOGR = 879.0           # T175's measured intervention slope -- quoted

# --- preregistered tolerances / bars (declared BEFORE any number) --------------
TOL_EXACT = 1.0e-12          # small-matrix / assembly identities
ROUND_BAR = 1.0e-9           # the probe's declared round-off horizon of the
#                              full h x h forms (T176) -- used where a small
#                              increment is read off an O(1) assembly
TOL_FH = 1.0e-5              # FH vs rebuild at the U minimum (T176: 3.4e-6)
U_SHAPE_FAC = 3.0            # both ladder ends must sit >= this over the min
BAR_MUT_FH = 1.0e-2          # a mutated formula must miss by >= this (rel.)
BAR_POLE_FRAC = 0.90         # PD must fail on > 10% of the period grid
POLE_PROD_LO, POLE_PROD_HI = 0.02, 50.0   # declared O(1) band for the product
BAR_NEAR = 0.35              # (lam2-lam1)/lam2 at delta = 0 must sit below
BAR_LADDER = 1.0e-3          # fine vs coarse ladder must differ by >= this
BAR_TRUNC = 1.0e-3           # a truncated-comb cell must MOVE under the sieve
COND_BAR = 1.0e12            # the T159 numerical horizon on cond(B_LL)
SEED = 562


def sym(A):
    return 0.5 * (A + A.T)


def ast_zero_firewall(src_path: str) -> bool:
    with open(src_path, "r", encoding="utf-8") as fh:
        tree = ast.parse(fh.read())
    hits = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            f = node.func
            if isinstance(f, ast.Attribute) and f.attr in (
                "zetazero", "nzeros", "second_sheet_zero",
            ):
                hits.append(f.attr)
            if isinstance(f, ast.Name) and f.id in ("zetazero", "nzeros"):
                hits.append(f.id)
        if isinstance(node, ast.Attribute) and node.attr in ("zetazero",):
            hits.append(node.attr)
    return not hits


# ---------------------------------------------------------------- atoms
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


LAM_TAB = von_mangoldt_table(ATOM_MAX)
_NN = np.nonzero(LAM_TAB > 0.0)[0]
U_ALL = np.log(_NN.astype(float))
MU_ALL = 2.0 * LAM_TAB[_NN] / np.sqrt(_NN.astype(float))
# the OLD table is a PREFIX of the new one: same atoms below the old cap
_OLD_CUT = int(np.searchsorted(_NN, ATOM_MAX_OLD, side="right"))
_GLX, _GLW = np.polynomial.legendre.leggauss(GL_N)


def chebyshev_kappa():
    nn = _NN.astype(float)
    psi = np.cumsum(LAM_TAB[_NN])
    keep = nn >= KAPPA_X0
    return float(np.max(np.abs(psi[keep] - nn[keep]) / nn[keep]))


def atoms_in(alpha, cut=None):
    n = int(np.searchsorted(U_ALL, 2.0 * alpha + 1.0e-14, side="right"))
    return min(n, cut) if cut is not None else n


# --------------------------------- the archimedean kernel (Weil 1952, cited)
def _arch_A_far(s, D):
    s = np.asarray(s, dtype=float).reshape(-1, 1)
    out = np.zeros(s.shape[0])
    for lo, hi in ((s - D, s), (s, s + D)):
        mid = 0.5 * (lo + hi)
        half = 0.5 * (hi - lo)
        w = mid + half * _GLX[None, :]
        val = ((1.0 - np.abs(s - w) / D) * np.exp(-0.5 * w)
               / (-np.expm1(-2.0 * w)))
        out -= half[:, 0] * (val @ _GLW)
    return out


def _arch_integrand(w, s, D):
    tri_s = max(0.0, 1.0 - abs(s) / D)
    S = 0.5 * (np.maximum(0.0, 1.0 - np.abs(s - w) / D)
               + np.maximum(0.0, 1.0 - np.abs(s + w) / D))
    return ((tri_s * np.exp(-2.0 * w) - S * np.exp(-0.5 * w))
            / (-np.expm1(-2.0 * w)))


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


# --------------------------------- parity geometry (KMS 1953; Dirichlet 1829)
def parity_mu(m):
    N = 2 * m + 1
    kk = np.arange(1, m + 1, dtype=float)
    return 4.0 * np.sin(math.pi * kk / N) ** 2


def parity_basis(m, kb=None):
    N = 2 * m + 1
    jj = np.arange(m)
    kk = np.arange(1, (kb or m) + 1)
    return (2.0 / math.sqrt(N)) * np.sin(
        2.0 * math.pi * np.outer(kk, jj + 1.0) / N)


def apply_LP(V, m):
    out = 2.0 * np.asarray(V, dtype=float).copy()
    out[:, 1:] -= V[:, :-1]
    out[:, :-1] -= V[:, 1:]
    out[:, -1] += V[:, -1]
    return out


_IDX = {}


def toeplitz_index(M):
    if M not in _IDX:
        h = M // 2
        rr = np.arange(h)
        _IDX[M] = (np.abs(rr[:, None] - rr[None, :]),
                   (M - 1) - rr[:, None] - rr[None, :])
    return _IDX[M]


def odd_toeplitz(c, M):
    it, ih = toeplitz_index(M)
    return np.asarray(c)[it] - np.asarray(c)[ih]


_TB = {}


def basis_of(hz):
    if hz not in _TB:
        _TB[hz] = (parity_basis(hz, KB_MAX), parity_mu(hz)[:KB_MAX])
    return _TB[hz]


# --------------------------------- THE T176 ASSEMBLY, verbatim (bincount)
def atom_lags(alpha, M, u, mu):
    """T176's production assembly: a linear spline of total mass one around
    u_n = log n, split between cells i0 and i0 + 1 with weights 1 - f and f,
    f = frac(u/D) the PLACEMENT PHASE, plus the reflected arm below D."""
    D = 2.0 * alpha / M
    q = u / D
    i0 = np.floor(q).astype(np.int64)
    f = q - i0
    c = np.bincount(i0, weights=-mu * 0.5 * (1.0 - f), minlength=M)[:M].copy()
    idx = i0 + 1
    ok = idx < M
    c += np.bincount(idx[ok], weights=-mu[ok] * 0.5 * f[ok], minlength=M)[:M]
    refl = u < D
    if refl.any():
        c[0] -= 0.5 * float(np.sum(mu[refl] * (1.0 - u[refl] / D)))
    return c, D


def gap_of(Ahat, prof, kb=SCHUR_KB):
    isq = 1.0 / np.sqrt(np.asarray(prof, dtype=float)[:kb])
    ev = np.linalg.eigvalsh(sym(Ahat[:kb, :kb] * np.outer(isq, isq)))
    return float(ev[0]), float(ev[-1])


def del_of(Ahat):
    a11, a12, a22 = float(Ahat[0, 0]), float(Ahat[0, 1]), float(Ahat[1, 1])
    det = a11 * a22 - a12 * a12
    return det / (a11 * a22)


def build_cell(n_zone, h, cut=None):
    """ONE window; the builder sees (n_zone, alpha, M) and nothing else
    (T174 P12).  `cut` truncates the atom table at the OLD cap (S3 only)."""
    alpha = math.log(float(n_zone))
    M = 2 * h
    ka = atoms_in(alpha, cut)
    c_at, D = atom_lags(alpha, M, U_ALL[:ka], MU_ALL[:ka])
    c = arch_lags(M, D) + c_at
    Tb, mu = basis_of(h)
    Ah = sym(Tb @ (odd_toeplitz(c, M) @ Tb.T))
    lmin, lmax = gap_of(Ah, mu)
    dl = del_of(Ah)
    return dict(n=n_zone, alpha=alpha, h=h, M=M, D=D, n_atom=ka,
                lmin=lmin, lmax=lmax, GAP=lmin / lmax, DEL=dl,
                R=(lmin / lmax) / max(abs(dl), 1.0e-300),
                pd=bool(lmin > 0.0),
                cond=abs(lmax / max(abs(lmin), 1.0e-300)),
                dens=float(ka) / float(M),
                complete=float(n_zone) ** 2 <= float(ATOM_MAX) + 0.5)


# --------------------------------- the T176 phase machinery, verbatim
def dc_dphase(cell):
    """THE EXACT LAG DERIVATIVE (T176 THEOREM T3): shifting the placement
    phase f -> f + delta of a family atom moves 0.5 mu_p delta from cell
    i0 + 1 to cell i0 and NOTHING else; dc/ddelta is exact and piecewise
    constant in delta between wraps."""
    dc = np.zeros(cell["M"])
    used = 0
    for p in PHASE_FAM:
        q = math.log(float(p)) / cell["D"]
        i0 = int(math.floor(q))
        if i0 + 1 >= cell["M"]:
            continue
        mp = 2.0 * math.log(float(p)) / math.sqrt(float(p))
        dc[i0] += 0.5 * mp
        dc[i0 + 1] -= 0.5 * mp
        used += 1
    return dc, used


def comb_with_family_shift(cell, delta):
    """The lag vector with the six family atoms displaced by delta (exact
    rebuild; T175's intervention, T176's E3 control)."""
    cat, _ = atom_lags(cell["alpha"], cell["M"], U_ALL[:cell["n_atom"]],
                       MU_ALL[:cell["n_atom"]])
    if delta != 0.0:
        for p in PHASE_FAM:
            q = math.log(float(p)) / cell["D"]
            i0, f = int(math.floor(q)), math.fmod(q, 1.0)
            if i0 + 1 >= cell["M"]:
                continue
            f2 = math.fmod(f + delta, 1.0)
            mp = 2.0 * math.log(float(p)) / math.sqrt(float(p))
            cat[i0] += 0.5 * mp * (f2 - f)
            cat[i0 + 1] -= 0.5 * mp * (f2 - f)
    return cat


def logR_at(cell, delta):
    cat = comb_with_family_shift(cell, delta)
    Tb, mm = basis_of(cell["h"])
    Ah = sym(Tb @ (odd_toeplitz(arch_lags(cell["M"], cell["D"]) + cat,
                                cell["M"]) @ Tb.T))
    lmin, lmax = gap_of(Ah, mm)
    if lmin <= 0.0:
        return None
    return math.log((lmin / lmax) / max(abs(del_of(Ah)), 1.0e-300))


def fh_closed(cell, swap_vectors=False, drop_del=False):
    """dlog R/ddelta IN CLOSED FORM (Feynman-Hellmann).  The two mutation
    knobs build the WRONG formula on purpose (S1.MUT)."""
    cat = comb_with_family_shift(cell, 0.0)
    Tb, mm = basis_of(cell["h"])
    Ah = sym(Tb @ (odd_toeplitz(arch_lags(cell["M"], cell["D"]) + cat,
                                cell["M"]) @ Tb.T))
    dc, used = dc_dphase(cell)
    dAh = sym(Tb @ (odd_toeplitz(dc, cell["M"]) @ Tb.T))
    isq = 1.0 / np.sqrt(np.asarray(mm, dtype=float)[:SCHUR_KB])
    S = np.outer(isq, isq)
    At = sym(Ah[:SCHUR_KB, :SCHUR_KB] * S)
    dAt = sym(dAh[:SCHUR_KB, :SCHUR_KB] * S)
    ev, V = np.linalg.eigh(At)
    v, w = V[:, 0], V[:, -1]
    if swap_vectors:
        v, w = w, v
    dlmin = float(v @ (dAt @ v))
    dlmax = float(w @ (dAt @ w))
    a11, a12, a22 = float(Ah[0, 0]), float(Ah[0, 1]), float(Ah[1, 1])
    d11, d12, d22 = float(dAh[0, 0]), float(dAh[0, 1]), float(dAh[1, 1])
    DEL = 1.0 - a12 * a12 / (a11 * a22)
    dDEL = (-2.0 * a12 * d12 / (a11 * a22)
            + a12 * a12 / (a11 * a22) * (d11 / a11 + d22 / a22))
    t_del = 0.0 if drop_del else (-dDEL / DEL)
    return dict(dlogR=dlmin / ev[0] - dlmax / ev[-1] + t_del,
                t_min=dlmin / ev[0], t_max=-dlmax / ev[-1],
                t_del=-dDEL / DEL,
                lmin=float(ev[0]), lam2=float(ev[1]), used=used)


def sweeper(cell):
    """delta -> spectrum of the normalised low block, arithmetic that does
    not depend on delta computed ONCE (T176 E3.ii, verbatim logic)."""
    cat = comb_with_family_shift(cell, 0.0)
    base = arch_lags(cell["M"], cell["D"]) + cat
    Tb, mm = basis_of(cell["h"])
    isq = 1.0 / np.sqrt(np.asarray(mm, dtype=float)[:SCHUR_KB])
    S = np.outer(isq, isq)
    fam = []
    for p in PHASE_FAM:
        q = math.log(float(p)) / cell["D"]
        i0, f = int(math.floor(q)), math.fmod(q, 1.0)
        if i0 + 1 < cell["M"]:
            fam.append((i0, f, 2.0 * math.log(float(p)) / math.sqrt(float(p))))

    def at(delta):
        c = base.copy()
        for i0, f, mp in fam:
            df = math.fmod(f + delta, 1.0) - f
            c[i0] += 0.5 * mp * df
            c[i0 + 1] -= 0.5 * mp * df
        Ah = sym(Tb @ (odd_toeplitz(c, cell["M"]) @ Tb.T))
        At = sym(Ah[:SCHUR_KB, :SCHUR_KB] * S)
        return np.linalg.eigvalsh(At)
    return at


# --------------------------------- the T175/T176 curve estimator, verbatim
def ols_slope(lx, ly):
    lx = np.asarray(lx, dtype=float)
    ly = np.asarray(ly, dtype=float)
    xc = lx - lx.mean()
    return float(np.sum(xc * ly) / np.sum(xc * xc))


def bin_deficit(cells, lo, hi, min_rung=3):
    """T175/T176's estimator, VERBATIM: one OLS slope of log|R| on log h per
    anchor from its cells INSIDE the bin, then the unweighted mean of the
    anchor slopes with the CLUSTER-ROBUST s.e. of that mean."""
    byn = {}
    for r in cells:
        if lo <= r["dens"] < hi:
            byn.setdefault(r["n"], []).append(r)
    es = []
    for n in sorted(byn):
        row = sorted(byn[n], key=lambda r: r["h"])
        if len(row) < min_rung:
            continue
        es.append(-ols_slope([math.log(float(r["h"])) for r in row],
                             [math.log(abs(r["R"])) for r in row]))
    if len(es) < 2:
        return None
    e = np.array(es)
    return (float(np.mean(e)),
            float(np.std(e, ddof=1) / math.sqrt(len(e))), len(e))


def run():
    reset()
    t0 = time.time()
    rng = np.random.default_rng(SEED)
    print("=" * 72)
    print("v562  PRIME.DENSE.LIMIT.01 -- the dense-limit identities (T176)")
    print("=" * 72)

    # ================================================================ S0
    print("\nS0 -- firewall, the one arithmetic input, the declared surface")
    check("S0.AST: no Riemann-zero / zetazero loader in this module",
          ast_zero_firewall(__file__))
    kappa = chebyshev_kappa()
    zone_max = int(math.isqrt(ATOM_MAX))
    anchors = [int(n) for n in _NN
               if ANCHOR_LO <= n <= zone_max and n * n <= ATOM_MAX]
    # the declared sub-selection: every 6th prime-power anchor (cost only)
    anchors = anchors[::6]
    CELLS = [build_cell(n, h) for n in anchors for h in H_FINE]
    n_pd = sum(r["pd"] for r in CELLS)
    check(f"S0.SURFACE: kappa = {kappa:.6f} reproduced to "
          f"{abs(kappa - KAPPA_REF):.1e} <= {TOL_KAPPA:.0e} at every jump "
          f"point of psi(x)/x on the table in [{KAPPA_X0:.0f}, {ATOM_MAX}] "
          f"(Chebyshev 1852 / Rosser-Schoenfeld 1962 -- the ONE "
          f"unconditional arithmetic input; psi(x)/x <= {B_PSI} holds), and "
          f"the declared surface is {len(anchors)} prime-power anchors in "
          f"[{ANCHOR_LO}, {zone_max}] (every 6th, declared; comb COMPLETE "
          f"on every cell, X = n^2 <= {ATOM_MAX}) x the declared 2^(1/4) "
          f"ladder h = {H_FINE} = {len(CELLS)} cells, {n_pd}/{len(CELLS)} "
          f"positive definite with cond(B_LL) <= "
          f"{max(r['cond'] for r in CELLS):.1e} <= {COND_BAR:.0e} (the "
          f"declared T159 horizon), dens spanning "
          f"{min(r['dens'] for r in CELLS):.2f}.."
          f"{max(r['dens'] for r in CELLS):.1f} atoms per lag cell",
          abs(kappa - KAPPA_REF) <= TOL_KAPPA
          and all(r["pd"] and r["complete"] for r in CELLS)
          and max(r["cond"] for r in CELLS) <= COND_BAR)

    # ================================================================ S1
    print("\nS1 -- R1 CLOSED: the Feynman-Hellmann identity (T176 P2)")
    byn = {}
    for r in CELLS:
        byn.setdefault(r["n"], []).append(r)
    rows = [sorted(v, key=lambda r: r["h"]) for _, v in sorted(byn.items())]
    mids = [row[len(row) // 2] for row in rows if len(row) >= 4]
    fh_cells = mids[:: max(1, len(mids) // N_FH_CELLS)][:N_FH_CELLS]
    # (a) the exact lag derivative: c(delta) = c(0) + delta dc between wraps
    c0 = comb_with_family_shift(fh_cells[0], 0.0)
    dtest = 1.0e-5
    c1 = comb_with_family_shift(fh_cells[0], dtest)
    dc0, used0 = dc_dphase(fh_cells[0])
    e_lin = (float(np.max(np.abs(c1 - c0 - dtest * dc0)))
             / max(float(np.max(np.abs(dtest * dc0))), 1.0e-300))
    check(f"S1.DCEXACT [THEOREM] T176 T3, the exactness that makes first "
          f"order an identity: the assembly is PIECEWISE LINEAR in the "
          f"placement phase -- c(delta) = c(0) + delta dc/ddelta EXACTLY "
          f"between wraps (checked at delta = {dtest:.0e} on the declared "
          f"cell n = {fh_cells[0]['n']}, h = {fh_cells[0]['h']}: residual "
          f"{e_lin:.1e} <= {ROUND_BAR:.0e} relative to the increment, "
          f"{used0} family atoms in window; the increment is {dtest:.0e} "
          f"of an O(1) lag vector, so the honest bar is the probe's "
          f"declared round-off horizon of the full assembly, not "
          f"double-precision exactness) -- the assembly moves 0.5 mu_p "
          f"per unit phase between two adjacent lag cells and NOTHING "
          f"else",
          e_lin <= ROUND_BAR and used0 == len(PHASE_FAM))
    # (b) the identity, against the rebuild, with the U-shape exhibited
    med_by_step = {d: [] for d in FD_GRID}
    n_ok = 0
    for cell in fh_cells:
        f = fh_closed(cell)
        if abs(f["dlogR"]) < 1.0e-30:
            continue
        got = {}
        for d in FD_GRID:
            p, m2 = logR_at(cell, +d), logR_at(cell, -d)
            if p is None or m2 is None:
                continue
            got[d] = (p - m2) / (2.0 * d)
        if len(got) < len(FD_GRID):
            continue
        n_ok += 1
        for d, qd in got.items():
            med_by_step[d].append(abs(qd - f["dlogR"]) / abs(f["dlogR"]))
    med = [(d, float(np.median(med_by_step[d]))) for d in FD_GRID]
    best = min(med, key=lambda t: t[1])
    print("    FD ladder (median |quotient - closed| / |closed|): "
          + ", ".join(f"{d:.0e} -> {m:.2e}" for d, m in med))
    check(f"S1.FH [THEOREM, per instance] R1 CLOSED: dlog R/ddelta = "
          f"v^T dA~ v/lam_min - w^T dA~ w/lam_max - dDEL/DEL "
          f"(Feynman-Hellmann; Hellmann 1937, Feynman 1939) reproduces the "
          f"full nonlinear rebuild on {n_ok}/{len(fh_cells)} declared "
          f"instances at the minimum of the declared step ladder: best "
          f"median residual {best[1]:.2e} <= {TOL_FH:.0e} at delta = "
          f"{best[0]:.0e}, WITH THE U-SHAPE EXHIBITED (round-off limited "
          f"at {FD_GRID[0]:.0e}: {med[0][1]:.2e}; truncation limited at "
          f"{FD_GRID[-1]:.0e}: {med[-1][1]:.2e}; both >= {U_SHAPE_FAC:.0f}x "
          f"the minimum) -- the residual is the DIFFERENCE QUOTIENT, not "
          f"the identity; a wrong formula has a floor, not a minimum.  "
          f"T175's measured intervention slope ({T175_DLOGR:.0f}) is "
          f"retired as a separate claim: it is an identity about the "
          f"assembly (T176 C1)",
          n_ok == len(fh_cells) and best[1] <= TOL_FH
          and med[0][1] >= U_SHAPE_FAC * best[1]
          and med[-1][1] >= U_SHAPE_FAC * best[1])
    # (c) the decomposition, reported (T176: dDEL/DEL carries the bulk)
    shares = []
    for cell in fh_cells:
        f = fh_closed(cell)
        tot = abs(f["t_min"]) + abs(f["t_max"]) + abs(f["t_del"])
        shares.append(abs(f["t_del"]) / max(tot, 1.0e-300))
    check(f"S1.DECOMP [E] the decomposition that corrected the expected "
          f"story: of the three closed terms the near-degeneracy channel "
          f"dDEL/DEL carries the LARGEST share on every declared instance "
          f"(shares {min(shares):.2f}..{max(shares):.2f}, all > 1/3; T176 "
          f"measured 84% median on its surface) -- the phase response of R "
          f"lives in the 2x2 near-degeneracy channel, which is exactly the "
          f"channel T174 proved does NOT cancel",
          min(shares) > 1.0 / 3.0)
    # (d) mutations: the wrong formula has a floor, not a U
    worst_mut = 0.0
    cell = fh_cells[0]
    f_true = fh_closed(cell)
    d_ref = best[0]
    p, m2 = logR_at(cell, +d_ref), logR_at(cell, -d_ref)
    quot = (p - m2) / (2.0 * d_ref)
    for kw in (dict(swap_vectors=True), dict(drop_del=True)):
        f_bad = fh_closed(cell, **kw)
        worst_mut = max(worst_mut,
                        0.0 if abs(quot) < 1e-300
                        else abs(f_bad["dlogR"] - quot) / abs(quot))
    e_true = abs(f_true["dlogR"] - quot) / abs(quot)
    check(f"S1.MUT [must-break] two mutated formulas miss the measured "
          f"quotient at the optimal step by >= {BAR_MUT_FH:.0e} relative "
          f"(swapped eigenvectors and dropped dDEL/DEL term: worst miss "
          f"{worst_mut:.2e}) while the true closed form sits at "
          f"{e_true:.2e}: the identity is a statement about THE formula, "
          f"not about any first-order expression",
          worst_mut >= BAR_MUT_FH and e_true <= TOL_FH * 10.0)

    # ================================================================ S2
    print("\nS2 -- the phase pole (T176 P3): the 300x anomaly explained")
    dense_mids = sorted(mids, key=lambda r: -r["dens"])[:N_POLE_CELLS]
    frac_pd, prods, nears, dpds = [], [], [], []
    for cell in dense_mids:
        at = sweeper(cell)
        f = fh_closed(cell)
        dd = np.arange(N_PER) / float(N_PER)
        lm = np.array([at(float(d))[0] for d in dd])
        frac_pd.append(float(np.mean(lm > 0.0)))
        nears.append((f["lam2"] - f["lmin"]) / f["lam2"])
        lo, hi = 0.0, None
        for s in (1.0e-6, 1.0e-5, 1.0e-4, 1.0e-3, 1.0e-2, 0.1, 0.5):
            if at(s)[0] <= 0.0:
                hi = s
                break
            lo = s
        if hi is None:
            continue
        for _ in range(N_BIS):
            mid = 0.5 * (lo + hi)
            if at(mid)[0] > 0.0:
                lo = mid
            else:
                hi = mid
        dpd = 0.5 * (lo + hi)
        dpds.append(dpd)
        prods.append(dpd * abs(f["dlogR"]))
    med_frac = float(np.median(frac_pd))
    med_prod = float(np.median(prods))
    check(f"S2.POLE [E, per instance] THE POLE: on the {len(dense_mids)} "
          f"densest declared instances the full phase period is swept on "
          f"the declared {N_PER}-point grid (no harmonic hunting) and "
          f"positive definiteness survives only a fraction "
          f"{min(frac_pd):.2f}..{max(frac_pd):.2f} of the period (median "
          f"{med_frac:.2f} < {BAR_POLE_FRAC}) -- lam_min CHANGES SIGN "
          f"inside the period, so log R has a POLE there and is NOT "
          f"defined on the full period; bisected to {N_BIS} levels the "
          f"loss point sits at delta_PD = {min(dpds):.1e}..{max(dpds):.1e} "
          f"with delta_PD x |dlog R/ddelta| = {med_prod:.2f} median, "
          f"inside the declared O(1) band [{POLE_PROD_LO}, {POLE_PROD_HI}] "
          f"-- a pole at the natural scale.  THE READING (T176): a "
          f"first-harmonic regression over the period estimates a Fourier "
          f"coefficient of a function with a pole in the interval, which "
          f"is why T175's harmonic came out ~300x below the local "
          f"derivative -- neither number is wrong; they measure different "
          f"things.  The 300x anomaly is RETIRED, replaced by this pole",
          len(dpds) == len(dense_mids) and med_frac < BAR_POLE_FRAC
          and POLE_PROD_LO <= med_prod <= POLE_PROD_HI)
    check(f"S2.NEAR [E, per instance] THE CROSSING IS ALREADY THERE: the "
          f"two lowest modes of the normalised low block sit within "
          f"{min(nears):.3f}..{max(nears):.3f} of each other at delta = 0 "
          f"(relative spacing (lam_2 - lam_1)/lam_2 < {BAR_NEAR} on every "
          f"instance; T176 measured 13.4% median) -- the intervention does "
          f"not CREATE a near-degeneracy, it walks along one, which closes "
          f"the loop with S1.DECOMP: the response lives in dDEL/DEL, and "
          f"DEL = 1 - r_12^2 IS the near-degeneracy of the bottom two "
          f"directions", max(nears) < BAR_NEAR)
    # control: the bisection brackets a true sign change
    at0 = sweeper(dense_mids[0])
    d0 = dpds[0]
    e_base = (abs(at0(0.0)[0] - dense_mids[0]["lmin"])
              / abs(dense_mids[0]["lmin"]))
    check(f"S2.CTRL: the bisected loss point is a genuine sign change -- "
          f"lam_min(0.98 delta_PD) = {at0(0.98 * d0)[0]:+.2e} > 0 and "
          f"lam_min(1.02 delta_PD) = {at0(1.02 * d0)[0]:+.2e} < 0 on the "
          f"first declared instance, and the sweeper's delta = 0 spectrum "
          f"reproduces the cell's lam_min to {e_base:.1e} <= "
          f"{ROUND_BAR:.0e} relative (same assembly, same block)",
          at0(0.98 * d0)[0] > 0.0 and at0(1.02 * d0)[0] < 0.0
          and e_base <= ROUND_BAR)

    # ================================================================ S3
    print("\nS3 -- sieve consistency (T176 P4): the audit at construction "
          "level")
    old_ok = [n for n in anchors if n * n <= ATOM_MAX_OLD]
    worst_c, worst_R = 0.0, 0.0
    for n in old_ok:
        for h in H_COARSE:
            alpha = math.log(float(n))
            ka_new = atoms_in(alpha)
            ka_old = atoms_in(alpha, _OLD_CUT)
            c_new, _ = atom_lags(alpha, 2 * h, U_ALL[:ka_new],
                                 MU_ALL[:ka_new])
            c_old, _ = atom_lags(alpha, 2 * h, U_ALL[:ka_old],
                                 MU_ALL[:ka_old])
            worst_c = max(worst_c, float(np.max(np.abs(c_new - c_old))))
            if ka_new != ka_old:
                worst_c = np.inf
    cells_old = [build_cell(n, h, cut=_OLD_CUT)
                 for n in old_ok for h in H_FINE]
    cells_new = [build_cell(n, h) for n in old_ok for h in H_FINE]
    for a, b in zip(cells_old, cells_new):
        worst_R = max(worst_R, abs(a["R"] / b["R"] - 1.0))
    lo_b = min(r["dens"] for r in cells_new)
    hi_b = max(r["dens"] for r in cells_new) + 1.0e-9
    b_old = bin_deficit(cells_old, lo_b, hi_b)
    b_new = bin_deficit(cells_new, lo_b, hi_b)
    check(f"S3.UNCHANGED [THEOREM] SIEVE CONSISTENCY AT CONSTRUCTION "
          f"LEVEL: a bigger sieve adds atoms ABOVE the old cap and nothing "
          f"else, so on the {len(old_ok)} anchors whose comb is complete "
          f"under the OLD cap {ATOM_MAX_OLD} the lag vectors under old and "
          f"new table agree BIT FOR BIT (worst |dc| = {worst_c:.1e} == 0), "
          f"R agrees to {worst_R:.1e} on {len(cells_new)} cells, and the "
          f"cluster-robust bin deficit is IDENTICAL: {b_old[0]:+.6f} +- "
          f"{b_old[1]:.6f} (old, {b_old[2]} anchors) vs {b_new[0]:+.6f} +- "
          f"{b_new[1]:.6f} (new) -- T176's cell-by-cell audit (all six "
          f"T175 bins at 0.0 sigma under the 20.8x sieve) is this "
          f"construction fact plus statistics, and it is what lets any "
          f"later probe raise ATOM_MAX without re-deriving the chain",
          worst_c == 0.0 and worst_R == 0.0
          and b_old[0] == b_new[0] and b_old[1] == b_new[1])
    n_tr = max(n for n in anchors if n * n > ATOM_MAX_OLD)
    r_tr_old = build_cell(int(n_tr), H_COARSE[0], cut=_OLD_CUT)
    r_tr_new = build_cell(int(n_tr), H_COARSE[0])
    move_tr = abs(r_tr_old["R"] / r_tr_new["R"] - 1.0)
    check(f"S3.MUT [must-break] the no-op is a theorem about COMPLETE "
          f"combs, not about sieves: the deepest declared anchor n = "
          f"{int(n_tr)} (X = {int(n_tr) ** 2} > {ATOM_MAX_OLD} = old cap) "
          f"has a TRUNCATED comb under the old table ({r_tr_old['n_atom']} "
          f"atoms vs {r_tr_new['n_atom']}) and its R moves by "
          f"{move_tr:.2e} >= {BAR_TRUNC:.0e} under the bigger sieve -- "
          f"exactly where the construction says it must",
          move_tr >= BAR_TRUNC)

    # ================================================================ S4
    print("\nS4 -- the curve estimator as a procedure + the ladder caveat "
          "(T176 P1 + the anti-promotion)")
    b_fine = bin_deficit(CELLS, DENS_BIN[0], DENS_BIN[1])
    order = rng.permutation(len(CELLS))
    b_perm = bin_deficit([CELLS[i] for i in order], DENS_BIN[0], DENS_BIN[1])
    coarse_cells = [r for r in CELLS if r["h"] in H_COARSE]
    b_coarse = bin_deficit(coarse_cells, DENS_BIN[0], DENS_BIN[1])
    d_ladder = abs(b_fine[0] - b_coarse[0])
    check(f"S4.ESTIMATOR [E] THE PROCEDURE IS DETERMINISTIC AND "
          f"REPRODUCIBLE: the cluster-robust bin statistic of T175/T176 "
          f"(one OLS slope of log|R| on log h per anchor inside the "
          f"declared bin dens in [{DENS_BIN[0]}, {DENS_BIN[1]}), then the "
          f"unweighted anchor mean with the cluster-robust s.e.) gives "
          f"{b_fine[0]:+.6f} +- {b_fine[1]:.6f} on {b_fine[2]} anchor "
          f"clusters, and recomputing under a permuted cell order "
          f"reproduces it EXACTLY ({abs(b_fine[0] - b_perm[0]):.1e} == 0): "
          f"no Monte Carlo, no tuning, no wall clock -- the T176 curve is "
          f"this procedure applied to its declared bins",
          b_fine is not None and b_fine[0] == b_perm[0]
          and b_fine[1] == b_perm[1])
    check(f"S4.LADDER [E, THE ANTI-PROMOTION WIRED AS A CHECK] the "
          f"estimator is LADDER-DEPENDENT, exhibited per instance: the "
          f"SAME declared bin on the fine 2^(1/4) ladder gives "
          f"{b_fine[0]:+.4f} +- {b_fine[1]:.4f} and on the coarse sqrt(2) "
          f"sub-ladder {b_coarse[0]:+.4f} +- {b_coarse[1]:.4f} -- a shift "
          f"of {d_ladder:.4f} >= {BAR_LADDER:.0e} (log R is CURVED in "
          f"log h: T176 measured a2 = -0.0842 +- 0.0085, so ladders with "
          f"different rung counts sample the curvature differently; T176 "
          f"saw shifts up to 0.20).  CONSEQUENCE, load-bearing: any ledger "
          f"row quoting a bin deficit MUST quote the rung ladder with it, "
          f"or the number is not reproducible -- the PRIME.DENSE.LIMIT.01 "
          f"row does exactly that", d_ladder >= BAR_LADDER)
    # the scramble control at the densest cells (T176 E3.iii, 194/194)
    n_kill, n_draw = 0, 0
    for cell in dense_mids[:2]:
        for _ in range(3):
            ka = cell["n_atom"]
            D, M = cell["D"], cell["M"]
            q = U_ALL[:ka] / D
            i0 = np.floor(q).astype(np.int64)
            f = rng.random(ka)
            mu = MU_ALL[:ka]
            c = np.bincount(i0, weights=-mu * 0.5 * (1.0 - f),
                            minlength=M)[:M].copy()
            ok = i0 + 1 < M
            c += np.bincount(i0[ok] + 1, weights=-mu[ok] * 0.5 * f[ok],
                             minlength=M)[:M]
            refl = U_ALL[:ka] < D
            if refl.any():
                c[0] -= 0.5 * float(np.sum(mu[refl]
                                           * (1.0 - U_ALL[:ka][refl] / D)))
            Tb, mm = basis_of(cell["h"])
            Ah = sym(Tb @ (odd_toeplitz(arch_lags(M, D) + c, M) @ Tb.T))
            lmin, _ = gap_of(Ah, mm)
            n_draw += 1
            if lmin <= 0.0:
                n_kill += 1
    check(f"S4.SCRAMBLE [must-break] the phase scramble at the densest "
          f"declared cells (every atom keeps its lag CELL, occupancy "
          f"preserved exactly, only the sub-cell placement is drawn "
          f"uniform): positive definiteness is destroyed on {n_kill}/"
          f"{n_draw} draws (T176: 194/194 at its density) -- the "
          f"dense-limit deficit is a property of WHERE the atoms sit, not "
          f"of how many there are; a one-sided destruction control, never "
          f"a calibrated null", n_kill == n_draw)
    # KMS exactness control at a ladder rung (T176 stress 2)
    m2 = H_FINE[3]
    Tb2, mu2 = basis_of(m2)
    e_ort = float(np.max(np.abs(Tb2 @ Tb2.T - np.eye(Tb2.shape[0]))))
    e_lp = float(np.max(np.abs(apply_LP(Tb2, m2) - mu2[:, None] * Tb2)))
    check(f"S4.CTRL: the KMS sine modes at the ladder rung m = {m2} are "
          f"orthonormal to {e_ort:.1e} and satisfy L_P t_k = mu^P_k t_k to "
          f"{e_lp:.1e} <= {TOL_EXACT:.0e} with the Dirichlet end x(-1) = 0 "
          f"and the parity end x(m) = -x(m-1) (Kac-Murdock-Szego 1953; "
          f"T176 stress 2 measured 1.9e-15) -- the classical spine the "
          f"identities stand on", e_ort <= TOL_EXACT and e_lp <= TOL_EXACT)

    # ================================================================ S5
    print("\nS5 -- the fences, restated as a check")
    check("S5.FENCE: per-instance identities and certified inequalities on "
          "a SMALL declared surface only -- the big sieve is NOT rebuilt "
          "here because the identities are sieve-size-free, which is their "
          "point; THE VERDICT IS A MEASUREMENT AND NOT A CLAIM OF THIS "
          f"MODULE -- T176's SITS-AT-ZERO (pooled {T176_POOLED:+.4f} +- "
          f"{T176_POOLED_SE:.4f} over the two new bins, plateau window "
          f"{T176_PLATEAU:.4f} at 2 sigma, factor 3.6 narrower than T175) "
          "stays a sandbox MEASURED number on T176's 2.5e7 surface WITH "
          "ITS RUNG LADDER -- the ladder caveat is part of the quote "
          "(S4.LADDER); THE LIMIT STAYS OPEN AND TYPED OPEN: true zero at "
          "finite density, power-law approach and low plateau remain "
          "indistinguishable under any resource-reachable sieve (the "
          "window narrows like the square root of the anchor cap -- one "
          "more decade costs ATOM_MAX ~ 2.5e9), no limit is claimed, and "
          "the open quantifier at link 16 is untouched; THE PHASE-2 "
          "CLOSURE IS A CLOSURE OF THE MEASUREMENT PROGRAMME (the planned "
          "instrument is exhausted), NOT OF THE QUESTION -- the work "
          "continues in the classification papers and the backflow lines; "
          "NO RH statement is made, assumed, approached or weakened, no "
          "zero of any L-function is read, no L-function is evaluated "
          "(AST firewall), RH_DELTA = 0.5 is a YARDSTICK in exactly one "
          "role; THE WEIL FENCE: positivity of a finite A_h is never "
          "routed through the Weil criterion, the audited chain is the "
          "R4-free R1 form; no marker of any pre-existing contract moves; "
          "Feynman-Hellmann (Hellmann 1937, Feynman 1939), Schur 1917, "
          "KMS 1953, Dirichlet 1829, Chebyshev 1852 / Rosser-Schoenfeld "
          "1962 named CLASSICAL; Weil 1952 CITED, never used as a "
          "criterion; zero-firewall AST-checked",
          True)

    elapsed = time.time() - t0
    print(f"\nv562 runtime: {elapsed:.1f}s")
    print(f"  FH identity: best median residual {best[1]:.2e} at delta = "
          f"{best[0]:.0e} (U-shape exhibited); dDEL/DEL shares "
          f"{min(shares):.2f}..{max(shares):.2f}")
    print(f"  pole: PD survives {med_frac:.2f} of the period median, "
          f"delta_PD x slope = {med_prod:.2f}; near-degeneracy at delta=0: "
          f"{min(nears):.3f}..{max(nears):.3f}")
    print(f"  sieve consistency: bit-for-bit on {len(old_ok)} shared "
          f"anchors; ladder shift {d_ladder:.4f} (the anti-promotion); "
          f"scramble kills {n_kill}/{n_draw}")
    return summary("PRIME.DENSE.LIMIT.01 dense-limit identities")


if __name__ == "__main__":
    raise SystemExit(run())
