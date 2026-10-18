#!/usr/bin/env python3
"""v716 -- PRIME.MOONSHOT.02: MOONSHOT stage 2 -- the shared arch-sector
test (kill (c) head-on).

QUESTION: does the archimedean place of the SAME commensurability groupoid
(stage 1: the Z[i]-E8 Hecke tower, moonshot_hecke_groupoid_probe, 19/19
MOONSHOT-GO) deliver the rho-arch tower of the L1 montage?  If yes, the
WHOLE Weil measure -- pole 2cosh(t/2) MINUS arch rho(t) MINUS atom orbits
Lambda -- comes out of one geometric object and the strategy-council kill
(c) ("arch glues only as a direct sum") falls at measurement level.

STRUCTURE HYPOTHESIS (tested link by link):
  the archimedean incarnation is the 48-site NS cover lift (S-C /
  chain_deck_sector_probe): clock L = S^4 of order 12 (spin-doubled,
  L^12 = -1) with the plane Z/12 = mu4 x mu3:
    *  mu4  = the half-turn H = L^6 = S^24 (true order 4, eigenvalue i^m)
       <-> the unit group Z[i]^x = <i> of the finite tower;
    *  mu3  = the deck Dk = L^4 = S^16 (Dk^3 = -1), charges
       nu(m) = m/6 mod 1 in {1/6, 1/2, 5/6} == the v628 deck-class twists;
    *  NS boundary (S^48 = -1) <-> the half-integer spectrum {2k + 1/2}
       of the L1 background operator;
    *  the arch tower = the +i eigenspace of H == {m == 1 mod 4} (the
       v695-S2 half-tower), whose heat trace IS rho(t) =
       e^{-t/2}/(1 - e^{-2t}) (S-C exact channel identity).

SECTIONS:
  A1  the unit map: exact character bookkeeping (matrices, mode census,
      CRT bijection m mod 12 <-> (m mod 4, m mod 3), deck labels, the
      finite-side mu4 witnesses: unit freeness r2 == 0 mod 4 and the
      i-stability locks of stage 1 -- the Z[i] tower IS the mu4-fixed
      part of the Z-commensurability groupoid).  No fit anywhere.
  A2  the trace identity: EXACT closed identity (machine-verified)
          Re psi(1/4 + i tau/2)          = int_0^inf [e^{-2u}/u
                                            - 2 rho(u) cos(tau u)] du
          Re psi(1/4 + i tau/2) - log pi = int_0^inf [e^{-2 pi u}/u
                                            - 2 rho(u) cos(tau u)] du
      -- the deployed arch density (v695 S3.4 Omega identity) is the
      cosine transform of the LIFT HEAT TRACE rho: the 1/4 is the mu4
      offset (modes m == 1 mod 4 => spectrum 2(k + 1/4)), DERIVED; the
      log pi is the Frullani comparison of the UV reference scale
      (2 -> 2 pi), i.e. the self-dual (Tate) normalization of the arch
      place -- DECLARED, the exact arch mirror of the declared sqrt(n)
      half-density at the finite places.  Machine-pinned: log pi enters
      the deployed window ONLY through the d = 0 UV cell.  The pole term
      2cosh(t/2) = e^{t/2} + e^{-t/2} is the two boundary exponents
      (s = 1, 0; the trivial-mode slot of v695 S3.4) and its deployed
      lag read is EXACTLY the tent integral of that density.
  A3  the gluing test (kill (c) direct): the unified trace functional
          T(t) = 2cosh(t/2) dt  -  rho(t) dt  -  sum Lambda-orbit atoms
      built with NO per-sector scalar: atoms from the stage-1 groupoid
      comb (Gaussian-class sieve to X = 262144, full window-4 reach),
      arch from the lift trace, pole from the boundary exponents.
      (i) atom sector: kappa_at == 1 on all 5 windows [<= 1e-12];
      (ii) arch operator ladder: finite-N lift traces on the deep-lag
      battery (dD >= 0.5), ONE joint scalar over all 5 windows,
      s*(N) -> 1 at rate ~N^-2; (iii) THE NAIL: single global kappa on
      the full unified window vectors vs the deployed windows (v643 W1
      Weil-measure reference), then a FREE 3-scalar LSQ
      (kappa_at, kappa_ar, kappa_p) must return all three == 1 -- if two
      independent scalars were needed, kill (c) stands; (iv) must-fail
      counterfactuals: the mu2 tower (Z carrier, all odd modes) and the
      wrong mu4 class (m == 3 mod 4) must NOT glue (>= 10% residual);
      the wrong deck-twist channel set misses rho by >= 30% (D5 mirror).
  A4  verdict + honesty: E8 enters through the arch side (clock 12 =
      mu4 x mu3, NS doubling, 48 = 16 x 3, v628 twists); the finite
      counts alone are carrier-generic (stage-1 honesty note).  The
      rank-4 hermitian unimodular Z[i]-carrier == Gaussian E8 is the
      v634/v689 identification (cited, not re-proven here).

FIREWALL (machine-enforced, G0): banned identifiers (no prime table, no
zeta charge) anywhere; the verification counting tables (core.U_ALL /
MU_ALL / LAM_TAB / arch_lags / atom_lags_at / atoms_in / frame_a_zones)
ONLY inside declared_* functions (AST-checked).  Windows are measurement
frames (declared); every geometric ingredient is defined BEFORE the
comparison.

CALIBRATION (interactive, this session):
  *  Gaussian-class sieve to 262144: 22996 irreducibles (11472 split
     norms, ram (1+1i), 11527 inert bases), comb slots 23150 == ka_4,
     missing/extra none, mass rel dev 0.0 (after fixing the unit-class
     bug: the norm-1 class must not seed the sieve).
  *  psi identities: dev <= 1.2e-11 for tau <= 3.7 with quad splitting
     [0, 1, 10, inf]; tau = 10 needs finer oscillation splitting
     (unit intervals to 30) -- bar 1e-9.
  *  lift ladder on the deep-lag battery (60 lags, 5 windows, one joint
     scalar): s* = 0.99078720 / 0.99796426 / 0.99950387 / 0.99987668 /
     0.99996921 at N = 48..768, rates 2.2/2.0/2.0, geometric extrapolant
     |s*_inf - 1| = 2.4e-7; rho-quadrature vs deployed 4.4e-16.
  *  counterfactuals: mu2 best scalar 0.6743 residual 0.326; wrong mu4
     class best scalar 1.93 residual 1.000.

RESULTS (this run, 18/18 PASS -- MOONSHOT-STAGE2-GLUED):
  *  A1: lift algebra exact (dev 0.0); census 24/24, 16/16/16, 8/8/8;
     Z/12 CRT labels arch (1,5,9) = mu4-charge 1 x mu3 (1,2,0) with
     nu = {1/6, 5/6, 1/2}; finite mu4 witnesses (r2 mod 4, i-stability
     locks) all pass -- ONE consistent character-plane identification.
  *  A2: Re psi(1/4 + i tau/2) = int [e^{-2u}/u - 2 rho cos(tau u)]
     verified to 1.4e-10 over tau in {0, .5, 1, 3.7, 10}: the 1/4 IS
     the mu4 offset (derived); log pi = Frullani 2 -> 2 pi (dev 0.0,
     declared self-dual scale, pinned to the d = 0 UV cell at 2.2e-16);
     gamma identity 8.3e-30 (after the Bernoulli-stable integrand fix);
     pole = 2cosh tent read, dev 1.9e-10 (second-difference float
     cancellation, typed).
  *  A3: comb at full reach 23150 slots dev 0.0; kappa_at - 1 = 0.0 on
     all 5 windows; lift ladder joint s* = 0.99078720 .. 0.99996921
     (rates 2.22/2.05/2.01, |s*_inf - 1| = 2.4e-7); unified object ==
     deployed windows at 2.2e-16 over ALL lags of all 5 windows; free
     3-scalar LSQ returns (1.0, 1.0, 1.0) to < 1e-12 -- ONE
     normalization; must-fails: mu2 residual 0.326, wrong mu4 class
     1.000, wrong deck twists 0.474.

PROVENANCE: discovery probe moonshot_arch_glue_probe.py (2026-08-03,
18/18 PASS, verdict MOONSHOT-STAGE2-GLUED: one object, ONE
normalization -- the free 3-scalar LSQ returns kappa = (1, 1, 1) to
< 1e-12 on all 5 windows; the 1/4 in the psi identity is the DERIVED
mu4 fixed-sector offset; log pi enters only through the declared
self-dual UV cell; lift ladder s* -> 1 at rate ~N^-2
(|s*_inf - 1| = 2.4e-7); must-fail counterfactuals: mu2 tower
residual 0.326, wrong mu4 class 1.000, wrong deck twists 0.474 --
E8 becomes forced AT THE GLUING).  Promoted verbatim (the stage-1
import now points at the promoted v714 module); numbers unchanged.
"""

import ast
import bisect
import math
import os
import sys
import time

import mpmath as mp
import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..",
                                "verification"))
import v563_paper2_readouts as core  # noqa: E402  (declared_* only)
import v714_moonshot_hecke_groupoid as stage1  # noqa: E402

# ---------------------------------------------------------------- constants
X_GEO = 262144            # window-4 atom reach e^{2 alpha_4}
N0 = 48                   # lift sites
N_LADDER = (48, 96, 192, 384, 768)
GL_N = 48                 # match the deployed quadrature density
T_GRID = np.linspace(0.5, 3.0, 51)
TAU_BATT = (0.0, 0.5, 1.0, 3.7, 10.0)
BATT_PER_WIN = 12         # deep-lag battery points per window
W_BATT_MIN = 0.5          # battery lags dD >= 0.5 (lift truncation window)

BAR_EXACT = 1.0e-12       # matrix identities / channel identities
BAR_PSI = 1.0e-9          # psi trace identities        (calib 1.2e-11)
BAR_QUAD = 1.0e-12        # own quadrature vs deployed  (calib 4.4e-16)
BAR_POLE = 1.0e-8         # pole tent-read vs closed second difference
                          # (float cancellation at deep lags, run 1.9e-10)
BAR_ATOM = 1.0e-12        # atom sector kappa/lags      (calib 0.0)
BAR_SSTAR = 1.0e-5        # |s*_inf - 1|                (calib 2.4e-7)
BAR_DEV768 = 1.0e-4       # ladder dev at N = 768       (calib 2.9e-5)
RATE_LO, RATE_HI = 1.8, 2.3
BAR_UNI = 1.0e-12         # unified window rel dev (to max |p|)
BAR_KAPPA = 1.0e-9        # 3-scalar LSQ deviation from 1
MUSTFAIL_RES = 0.10       # counterfactual residual floor
BAR_WRONGTWIST = 0.30     # D5 mirror

BANNED_IDS = ("sympy", "isprime", "primerange", "nextprime", "prevprime",
              "primepi", "zetazero", "zetas", "nzeros")
RESTRICTED = ("U_ALL", "MU_ALL", "LAM_TAB", "G_ALL", "NU_MAIN", "ATOM_MAX",
              "atom_lags_at", "atoms_in", "arch_lags", "frame_a_zones",
              "arch_A")

GLX, GLW = np.polynomial.legendre.leggauss(GL_N)
EULER = 0.57721566490153286060651209008240243104215933593992
LOG_PI = math.log(math.pi)

CHECKS = []


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok)))
    print("  [%s] %s%s" % ("PASS" if ok else "FAIL", name,
                           ("  -- " + detail) if detail else ""))
    return bool(ok)


# ------------------------------------------------------- densities (closed)
def rho(w):
    """The lift heat trace (S-C): sum_{m==1 mod 4} e^{-w m/2}."""
    w = np.asarray(w, float)
    return np.exp(-0.5 * w) / (-np.expm1(-2.0 * w))


def rho_mu2(w):
    """Counterfactual: Z carrier (mu2 units), ALL odd modes."""
    w = np.asarray(w, float)
    return np.exp(-0.5 * w) / (-np.expm1(-1.0 * w))


def rho_mu4_wrong(w):
    """Counterfactual: the OTHER mu4 class m == 3 mod 4 (D2)."""
    w = np.asarray(w, float)
    return np.exp(-1.5 * w) / (-np.expm1(-2.0 * w))


def rho_lat(w, N):
    """Finite-N lift trace on the selected (+i) sector, sin dispersion."""
    ms = np.arange(1, N, 2)
    ms = ms[ms % 4 == 1]
    eps = (N / math.pi) * np.sin(ms * math.pi / (2.0 * N))
    return np.exp(-np.outer(np.asarray(w, float).ravel(), eps)).sum(axis=1)


def pole_density(w):
    """2cosh(w/2): the two boundary exponents e^{(s-1/2)t}, s = 1, 0
    (the trivial-mode slot, v695 S3.4)."""
    w = np.asarray(w, float)
    return 2.0 * np.cosh(0.5 * w)


def g_pole(tv):
    tv = abs(tv)
    return -4.0 * (math.exp(tv / 2) + math.exp(-tv / 2) - 2.0)


def pole_lags_closed(M, D):
    return np.array([-(g_pole((d - 1) * D) - 2.0 * g_pole(d * D)
                       + g_pole((d + 1) * D)) / D for d in range(M)])


# --------------------------------------------------------- tent quadrature
def tent_read(density, d, D):
    """int tent_d(w) density(w) dw, GL-48 per half cell (far cells)."""
    s = d * D
    tot = 0.0
    for lo, hi in ((s - D, s), (s, s + D)):
        mid, half = 0.5 * (lo + hi), 0.5 * (hi - lo)
        w = mid + half * GLX
        tot += half * float(np.dot(GLW, (1.0 - np.abs(s - w) / D)
                                   * density(w)))
    return tot


def arch_lags_far_geo(M, D):
    """-int tent_d rho for d = 1..M-1, vectorized (deployed convention)."""
    s = (np.arange(1, M) * D).reshape(-1, 1)
    out = np.zeros(M - 1)
    for lo, hi in ((s - D, s), (s, s + D)):
        mid = 0.5 * (lo + hi)
        half = 0.5 * (hi - lo)
        w = mid + half * GLX[None, :]
        val = (1.0 - np.abs(s - w) / D) * rho(w)
        out -= half[:, 0] * (val @ GLW)
    return out


def arch_lag0_geo(D, with_logpi=True):
    """The d = 0 UV cell of the arch read, own reimplementation of the
    deployed near-cell (Weil regularized kernel): the ONLY place the
    constant log pi enters; the gamma is the psi-offset regularizer."""
    W = D
    mid, half = 0.5 * W, 0.5 * W
    w = mid + half * GLX
    integrand = (np.exp(-2.0 * w) - (1.0 - w / D) * np.exp(-0.5 * w)) \
        / (-np.expm1(-2.0 * w))
    tot = half * float(np.dot(GLW, integrand))
    c = -EULER + 2.0 * tot - math.log1p(-math.exp(-2.0 * W))
    if with_logpi:
        c -= LOG_PI
    return c


def atom_tent_geo(alpha, M, positions, masses):
    """Own tent assembly (deployed T115 semantics) at geo atoms."""
    D = 2.0 * alpha / M
    c = np.zeros(M)
    for u_j, mu_j in zip(positions, masses):
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
    return c


# ------------------------------------------------- stage-1 comb via sieve
def gaussian_sieve(x):
    """Ring-internal irreducibility sieve on associate classes of Z[i]
    with norm <= x (norms = lattice form, no prime input): process
    classes by ascending norm; an unmarked class is irreducible and
    marks all its multiples."""
    am = int(math.isqrt(x)) + 1
    by_norm = {}
    for a in range(1, am + 1):
        for b in range(0, am + 1):
            n = a * a + b * b
            if 2 <= n <= x:
                by_norm.setdefault(n, []).append((a, b))
    norms = sorted(by_norm)
    flat = [(n, d) for n in norms for d in by_norm[n]]
    flat_norms = [n for n, _d in flat]
    composite = set()
    irred = []
    for n in norms:
        for d in by_norm[n]:
            if d in composite:
                continue
            irred.append(d)
            top = x // n
            if top >= 2:
                hi = bisect.bisect_right(flat_norms, top)
                da, db = d
                for k in range(hi):
                    _gn, (ga, gb) = flat[k]
                    composite.add(stage1.canon((da * ga - db * gb,
                                                da * gb + db * ga)))
    return irred


def geo_comb(x):
    """Stage-1 sigma-quotient comb to x: split pairs (norm p), ram
    (1+i, base 2), inert rationals (half orbit) via the double sieve."""
    irred = gaussian_sieve(x)
    split_norms = sorted({a * a + b * b for (a, b) in irred
                          if b != 0 and a != b})
    ram_ok = [(a, b) for (a, b) in irred if a == b] == [(1, 1)]
    census_rationals = sorted(a for (a, b) in irred if b == 0)
    mark = np.zeros(x + 1, dtype=bool)
    for p in split_norms:
        mark[p::p] = True
    inert = []
    for m in range(3, x + 1, 2):
        if not mark[m]:
            inert.append(m)
            mark[2 * m::m] = True
    comb = {}
    for p in split_norms:
        pk = p
        while pk <= x:
            comb[pk] = math.log(p)
            pk *= p
    pk = 2
    while pk <= x:
        comb[pk] = math.log(2.0)
        pk *= 2
    for m in inert:
        pk = m
        while pk <= x:
            comb[pk] = math.log(m)
            pk *= m
    meta = dict(n_irred=len(irred), n_split=len(split_norms),
                n_inert=len(inert), ram_ok=ram_ok,
                census_rationals=census_rationals)
    return comb, meta


# ------------------------------------------------------------ G0 firewall
def g0_firewall():
    print("\nG0 -- AST firewall + environment")
    src = open(os.path.abspath(__file__), encoding="utf-8").read()
    tree = ast.parse(src)
    bad = []
    for node in ast.walk(tree):
        name = None
        if isinstance(node, ast.Name):
            name = node.id
        elif isinstance(node, ast.Attribute):
            name = node.attr
        elif isinstance(node, (ast.Import, ast.ImportFrom)):
            mods = [al.name for al in node.names]
            if isinstance(node, ast.ImportFrom) and node.module:
                mods.append(node.module)
            for m in mods:
                if any(b in m for b in BANNED_IDS):
                    bad.append(m)
            continue
        if name and name.lower() in BANNED_IDS:
            bad.append(name)
    check("G0.1 banned symbols absent (no prime table / no zeta charge)",
          not bad, "found %s" % bad if bad else "clean")

    allowed = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and \
                node.name.startswith("declared_"):
            for sub in ast.walk(node):
                allowed.add(id(sub))
    leaks = [node.attr for node in ast.walk(tree)
             if isinstance(node, ast.Attribute) and node.attr in RESTRICTED
             and id(node) not in allowed]
    check("G0.2 counting tables only inside declared_* sections",
          not leaks, "leaks: %s" % leaks if leaks else "clean")
    print("    python %s, numpy %s, mpmath %s"
          % (sys.version.split()[0], np.__version__, mp.__version__))


# ------------------------------------------------------------ A1 unit map
def a1_unit_map():
    print("\nA1 -- the unit map (exact character bookkeeping, no fit)")
    S = np.zeros((N0, N0))
    for i in range(N0 - 1):
        S[i, i + 1] = 1.0
    S[N0 - 1, 0] = -1.0
    L = np.linalg.matrix_power(S, 4)
    Dk = np.linalg.matrix_power(S, 16)
    H = np.linalg.matrix_power(S, 24)
    Q = np.linalg.matrix_power(L, 3)
    eye = np.eye(N0)
    dev = max(
        float(np.max(np.abs(np.linalg.matrix_power(L, 12) + eye))),
        float(np.max(np.abs(np.linalg.matrix_power(Dk, 3) + eye))),
        float(np.max(np.abs(np.linalg.matrix_power(H, 4) - eye))),
        float(np.max(np.abs(np.linalg.matrix_power(Q, 2) - H))),
        float(np.max(np.abs(np.linalg.matrix_power(Q, 4) + eye))))
    check("A1.1 lift algebra: L^12=-1, Dk^3=-1, H=S^24 with H^4=+1 "
          "(the TRUE mu4), (L^3)^2=H, (L^3)^4=-1", dev <= BAR_EXACT,
          "max dev %.1e" % dev)

    ms = np.arange(1, 2 * N0, 2)
    i_pow = np.mod(ms, 4)                       # H eigenvalue i^m
    nus = np.mod(ms / 6.0, 1.0)                 # deck charge m/6 mod 1
    cnt4 = {1: int(np.sum(i_pow == 1)), 3: int(np.sum(i_pow == 3))}
    cnt_nu = {v: int(np.sum(np.isclose(nus, v)))
              for v in (1.0 / 6.0, 0.5, 5.0 / 6.0)}
    arch = ms[ms % 4 == 1]
    cnt_arch = {r: int(np.sum(arch % 12 == r)) for r in (1, 5, 9)}
    ok_census = (cnt4 == {1: 24, 3: 24}
                 and cnt_nu == {1.0 / 6.0: 16, 0.5: 16, 5.0 / 6.0: 16}
                 and cnt_arch == {1: 8, 5: 8, 9: 8})
    check("A1.2 mode census: mu4 classes 24/24 (i^m = +i/-i); deck "
          "nu = m/6 mod 1 in {1/6,1/2,5/6} counts 16/16/16 (== v628 "
          "twists, cited); arch (+i) sector deck-split 8/8/8",
          ok_census, "%s %s %s" % (cnt4, cnt_nu, cnt_arch))

    # CRT: m mod 12 <-> (m mod 4, m mod 3) bijection on odd residues
    tab = {}
    ok_crt = True
    for r in (1, 3, 5, 7, 9, 11):
        pair = (r % 4, r % 3)
        ok_crt &= pair not in tab.values()
        tab[r] = pair
    sec = {r: (tab[r], r / 6.0 % 1.0) for r in (1, 5, 9)}
    check("A1.3 the Z/12 plane: CRT bijection m mod 12 <-> "
          "(mu4, mu3) on odd residues; arch sectors (1,5,9) = "
          "mu4-charge 1 x mu3-charges (1,2,0)",
          ok_crt and all(tab[r][0] == 1 for r in (1, 5, 9)),
          "labels %s" % {r: "mu4=%d mu3=%d nu=%s" % (tab[r][0], tab[r][1],
                         mp.nstr(mp.mpf(r) / 6 % 1, 3)) for r in (1, 5, 9)})

    # exact channel identities (selection + deck split == rho)
    dev_sel = 0.0
    dev_deck = 0.0
    for t in T_GRID:
        sel = sum(math.exp(-t * m / 2.0) for m in range(1, 400, 4))
        deck = sum(math.exp(-(r / 2.0) * t) / (1.0 - math.exp(-6.0 * t))
                   for r in (1, 5, 9))
        r0 = float(rho(t))
        dev_sel = max(dev_sel, abs(sel - r0) / r0)
        dev_deck = max(dev_deck, abs(deck - r0) / r0)
    check("A1.4 selection identity: the +i (m==1 mod 4) tower trace == "
          "rho, and the three deck channels {1/2,5/2,9/2} sum to rho "
          "(S-C, exact)", max(dev_sel, dev_deck) <= BAR_EXACT,
          "sel %.1e deck %.1e" % (dev_sel, dev_deck))

    # finite-side mu4 witnesses (stage-1 machinery)
    r2 = stage1.r2_counts(20000)
    ok_free = bool(np.all(r2[1:] % 4 == 0))
    cls35 = stage1.class_census(35)
    ok1, _n1, _c1 = stage1.lock_rank1(35, cls35)
    ok2, _n2, _c2 = stage1.lock_rank2((2, 4, 5, 8), cls35)
    check("A1.5 finite side: mu4 = Z[i]^x acts freely (r2 == 0 mod 4, "
          "n <= 20000); i-STABILITY locks (rank 1 n<=35; rank 2 "
          "{2,4,5,8}: 3/7/12/15) -- the Z[i] tower IS the mu4-fixed "
          "part of the Z-commensurability groupoid",
          ok_free and ok1 and ok2)
    print("    identification: <i> (units) <-> <H = S^24> (half turn), "
          "both cyclic order 4;\n    the arch tower carries chi(H) = +i "
          "(mode fields, fundamental character),\n    the finite tower "
          "is the chi = 0 (invariant/module) incarnation -- one Z/12\n"
          "    plane, sector labels consistent.  The finite-side mu3 "
          "(triality of the\n    Gaussian E8, v633/orbit60) stays a "
          "CITED carrier structure, typed open.")


# -------------------------------------------------------- A2 trace identity
def a2_trace_identity():
    print("\nA2 -- the trace identity (the 1/4 derived, log pi declared)")
    mp.mp.dps = 30

    def rho_m(u):
        return mp.e ** (-u / 2) / (1 - mp.e ** (-2 * u))

    pts = [0] + list(range(1, 31)) + [mp.inf]
    dev1 = mp.mpf(0)
    dev2 = mp.mpf(0)
    for tau in TAU_BATT:
        lhs = mp.re(mp.digamma(mp.mpf(1) / 4 + mp.mpf(tau) / 2 * 1j))
        rhs = mp.quad(lambda u: mp.e ** (-2 * u) / u
                      - 2 * rho_m(u) * mp.cos(tau * u), pts)
        dev1 = max(dev1, abs(lhs - rhs))
        rhs2 = mp.quad(lambda u: mp.e ** (-2 * mp.pi * u) / u
                       - 2 * rho_m(u) * mp.cos(tau * u), pts)
        dev2 = max(dev2, abs(lhs - mp.log(mp.pi) - rhs2))
    check("A2.1 EXACT: Re psi(1/4 + i tau/2) = int [e^{-2u}/u - "
          "2 rho(u) cos(tau u)] -- the deployed arch density IS the "
          "cosine transform of the lift heat trace; the 1/4 = mu4 "
          "offset (spectrum 2(k + 1/4) from m == 1 mod 4), DERIVED",
          dev1 <= BAR_PSI, "max dev %s over tau %s"
          % (mp.nstr(dev1, 3), TAU_BATT))
    fr = mp.quad(lambda u: (mp.e ** (-2 * u) - mp.e ** (-2 * mp.pi * u))
                 / u, [0, 1, mp.inf])
    check("A2.2 log pi = Frullani scale comparison 2 -> 2 pi (dev %s); "
          "psi - log pi identity holds with reference e^{-2 pi u}/u "
          "(max dev %s) -- the self-dual (Tate) normalization of the "
          "arch place, DECLARED (mirror of the finite-place sqrt(n))"
          % (mp.nstr(abs(fr - mp.log(mp.pi)), 3), mp.nstr(dev2, 3)),
          abs(fr - mp.log(mp.pi)) <= BAR_PSI and dev2 <= BAR_PSI)

    # gamma = the psi-offset regularizer (same family as e^{-2u}/u);
    # cancellation-stable form near w = 0 (Bernoulli series)
    def gam_integrand(w):
        if w < mp.mpf("1e-4"):
            g = mp.mpf(1) / 2 + w / 12 - w ** 3 / 720
        else:
            g = 1 / (1 - mp.e ** (-w)) - 1 / w
        return mp.e ** (-w) * g

    gam = mp.quad(gam_integrand, [0, 1, mp.inf])
    check("A2.3 gamma-regularizer identity: gamma = -psi(1) = int "
          "[e^{-w}/(1-e^{-w}) - e^{-w}/w] (dev %s) -- the constant "
          "pair (gamma, log pi) of the deployed UV cell is (spectral "
          "offset, declared scale)" % mp.nstr(abs(gam - mp.euler), 3),
          abs(gam - mp.euler) <= BAR_PSI)

    # pole = boundary exponents; deployed pole lag == tent(2cosh) exact
    devp = 0.0
    for (M, D) in ((368, 0.015068), (2866, 0.004353)):
        cp = pole_lags_closed(M, D)
        for d in (1, 5, M // 2, M - 2):
            q = tent_read(pole_density, d, D)
            devp = max(devp, abs(cp[d] - q) / abs(q))
    check("A2.4 pole term: deployed pole lag == tent integral of "
          "2cosh(w/2) (second difference = tent read of g'', exact "
          "identity; residual = float cancellation of the second "
          "difference at deep lags, ~|g| eps / D^2 g''); 2cosh(w/2) = "
          "e^{w/2} + e^{-w/2} = the s = 1, 0 boundary exponents "
          "(trivial-mode slot, v695 S3.4)",
          devp <= BAR_POLE, "max rel dev %.1e <= %.0e" % (devp, BAR_POLE))


# --------------------------------------------------------- declared frames
def declared_family():
    """DECLARED measurement frames: the identical L1/5b window family and
    the deployed lag vectors (v563 build == the v643 W1 Weil-measure
    reference).  The verification tables enter HERE (and in the other
    declared_* sections) only."""
    zones = core.frame_a_zones()
    fam = []
    for kz in zones:
        alpha = float(core.U_ALL[kz])
        D_k = 0.5 * float(core.G_ALL[kz]) / float(core.NU_MAIN)
        M = int(math.ceil(alpha / D_k - 1.0e-9)) + 1
        if M % 2:
            M += 1
        if math.exp(2.0 * alpha) <= core.ATOM_MAX + 0.5:
            fam.append((kz, alpha, M))
    hs = np.array([t[2] // 2 for t in fam], float)
    picks = [fam[0]]
    for qq in (0.25, 0.5, 0.75, 1.0):
        tgt = float(np.quantile(hs, qq))
        cand = min(fam, key=lambda t_: abs(t_[2] // 2 - tgt))
        if all(cand[0] != p_[0] for p_ in picks):
            picks.append(cand)
    picks = sorted(picks, key=lambda t_: t_[2])
    wins = []
    for (kz, alpha, M) in picks:
        D = 2.0 * alpha / M
        ka = core.atoms_in(alpha)
        car = core.arch_lags(M, D)
        cat, _ = core.atom_lags_at(alpha, M, core.U_ALL[:ka],
                                   core.MU_ALL[:ka])
        cp = pole_lags_closed(M, D)
        wins.append(dict(kz=kz, alpha=alpha, M=M, D=D, ka=ka,
                         car=car, cat=cat, cp=cp, p=car + cat + cp))
    return wins


def declared_atom_reference(comb, wins):
    """DECLARED: geo comb vs the deployed atom layer on all 5 windows."""
    dev_pos = 0.0
    dev_mass = 0.0
    ok_slots = True
    ka4 = wins[-1]["ka"]
    nn = np.round(np.exp(core.U_ALL[:ka4])).astype(int)
    ok_slots = all(int(n) in comb for n in nn) and \
        len(comb) == ka4
    dev_pos = max(abs(math.log(int(n)) - core.U_ALL[k])
                  for k, n in enumerate(nn))
    dev_mass = max(abs(2.0 * comb[int(n)] / math.sqrt(float(n))
                       - core.MU_ALL[k]) / core.MU_ALL[k]
                   for k, n in enumerate(nn))
    return ok_slots, dev_pos, dev_mass, nn


# --------------------------------------------------------------- A3 gluing
def a3_gluing(comb):
    print("\nA3 -- the gluing test (kill (c) direct)")
    wins = declared_family()
    print("    family: " + ", ".join("h=%d (X=%.0f)" % (w["M"] // 2,
          math.exp(2 * w["alpha"])) for w in wins))

    # ---- A3.1 atom sector from the groupoid comb, full window-4 reach
    ok_slots, dev_pos, dev_mass, _nn = declared_atom_reference(comb, wins)
    check("A3.1a groupoid comb at full reach X = %d: all %d slots, "
          "positions dev %.1e, masses rel dev %.1e"
          % (X_GEO, wins[-1]["ka"], dev_pos, dev_mass),
          ok_slots and dev_pos <= BAR_ATOM and dev_mass <= BAR_ATOM)
    us = sorted(comb)
    u_geo = [math.log(n) for n in us]
    mu_geo = [2.0 * comb[n] / math.sqrt(float(n)) for n in us]
    kappa_at = []
    dev_at = 0.0
    for w in wins:
        cat_geo = atom_tent_geo(w["alpha"], w["M"], u_geo, mu_geo)
        w["cat_geo"] = cat_geo
        num = float(cat_geo @ w["cat"])
        den = float(cat_geo @ cat_geo)
        kappa_at.append(num / den)
        dev_at = max(dev_at, float(np.max(np.abs(cat_geo - w["cat"]))
                                   / np.max(np.abs(w["cat"]))))
    check("A3.1b atom sector: kappa_at == 1 on all 5 windows (max "
          "|kappa-1| %.1e), lag dev %.1e -- NO atom-sector scalar"
          % (max(abs(k - 1) for k in kappa_at), dev_at),
          max(abs(k - 1) for k in kappa_at) <= BAR_ATOM
          and dev_at <= BAR_ATOM)

    # ---- A3.2 arch operator ladder (deep-lag battery, ONE joint scalar)
    dep_b = []
    lat_b = {N: [] for N in N_LADDER}
    rho_b = []
    mu2_b = []
    mu4w_b = []
    for w in wins:
        M, D = w["M"], w["D"]
        ds = np.unique(np.round(np.geomspace(
            W_BATT_MIN / D, 2 * w["alpha"] / D - 1,
            BATT_PER_WIN)).astype(int))
        for d in ds:
            dep_b.append(-w["car"][d])
            rho_b.append(tent_read(rho, d, D))
            mu2_b.append(tent_read(rho_mu2, d, D))
            mu4w_b.append(tent_read(rho_mu4_wrong, d, D))
            for N in N_LADDER:
                lat_b[N].append(tent_read(lambda x: rho_lat(x, N), d, D))
    dep_b = np.array(dep_b)
    rho_b = np.array(rho_b)
    dev_q = float(np.max(np.abs(rho_b - dep_b) / np.abs(dep_b)))
    check("A3.2a own rho quadrature == deployed arch lags on the "
          "battery (%d lags, 5 windows)" % len(dep_b),
          dev_q <= BAR_QUAD, "max rel dev %.1e" % dev_q)
    svals, devs = [], []
    for N in N_LADDER:
        la = np.array(lat_b[N])
        s = float(la @ dep_b) / float(la @ la)
        svals.append(s)
        devs.append(float(np.max(np.abs(s * la - dep_b) / np.abs(dep_b))))
    r_s = [math.log(abs(svals[i] - svals[i + 1])
                    / abs(svals[i + 1] - svals[i + 2])) / math.log(2.0)
           for i in range(len(svals) - 2)]
    r_d = [math.log(devs[i] / devs[i + 1]) / math.log(2.0)
           for i in range(len(devs) - 1)]
    s_inf = svals[-1] + (svals[-1] - svals[-2]) / (2.0 ** r_s[-1] - 1.0)
    print("    ladder: " + "  ".join("N=%d s*=%.8f dev=%.1e"
          % (N, svals[i], devs[i]) for i, N in enumerate(N_LADDER)))
    check("A3.2b the LIFT OPERATOR delivers the arch sector: one joint "
          "scalar over all 5 windows, s*(N) -> 1 at ~N^-2 (rates %s), "
          "|s*_inf - 1| = %.1e <= %.0e, dev(768) = %.1e <= %.0e"
          % (["%.2f" % r for r in r_s], abs(s_inf - 1), BAR_SSTAR,
             devs[-1], BAR_DEV768),
          all(RATE_LO <= r <= RATE_HI for r in r_s + r_d)
          and abs(s_inf - 1) <= BAR_SSTAR and devs[-1] <= BAR_DEV768)

    # ---- A3.3 THE NAIL: one normalization for the unified object
    uni_dev = 0.0
    logpi_pin = 0.0
    rows_geo = []
    rows_dep = []
    for w in wins:
        M, D = w["M"], w["D"]
        car_geo = np.empty(M)
        car_geo[1:] = arch_lags_far_geo(M, D)
        car_geo[0] = arch_lag0_geo(D)
        logpi_pin = max(logpi_pin, abs(
            (arch_lag0_geo(D, with_logpi=False) - arch_lag0_geo(D))
            - LOG_PI))
        dev0 = abs(car_geo[0] - w["car"][0]) / abs(w["car"][0])
        c_uni = car_geo + w["cat_geo"] + w["cp"]
        uni_dev = max(uni_dev, float(np.max(np.abs(c_uni - w["p"]))
                                     / np.max(np.abs(w["p"]))),
                      float(np.max(np.abs(car_geo - w["car"]))
                            / np.max(np.abs(w["car"]))), dev0)
        rows_geo.append(np.stack([w["cat_geo"][1:], car_geo[1:],
                                  w["cp"][1:]], axis=1))
        rows_dep.append(w["p"][1:])
    check("A3.3a unified object (atoms + arch + pole, ALL coefficients "
          "1) == deployed windows (v643 W1 Weil reference), all lags "
          "all 5 windows incl. the UV cell", uni_dev <= BAR_UNI,
          "max rel dev %.1e; log pi pinned in d=0 cell (dev %.1e)"
          % (uni_dev, logpi_pin))
    A = np.vstack(rows_geo)
    y = np.concatenate(rows_dep)
    kap, *_ = np.linalg.lstsq(A, y, rcond=None)
    uni = A.sum(axis=1)
    kap_1 = float(uni @ y) / float(uni @ uni)
    check("A3.3b THE NAIL: free 3-scalar LSQ (kappa_at, kappa_ar, "
          "kappa_p) over all windows returns (%.12f, %.12f, %.12f); "
          "single global kappa = %.12f -- ONE normalization, no "
          "per-sector scalar, kill (c) falls"
          % (kap[0], kap[1], kap[2], kap_1),
          max(abs(k - 1.0) for k in kap) <= BAR_KAPPA
          and abs(kap_1 - 1.0) <= BAR_KAPPA)

    # ---- A3.4 must-fail counterfactuals (E8 specificity of the arch side)
    res = {}
    for tag, v in (("mu2 (Z carrier, all odd modes)", np.array(mu2_b)),
                   ("wrong mu4 class (m==3 mod 4)", np.array(mu4w_b))):
        s = float(v @ dep_b) / float(v @ v)
        res[tag] = (s, float(np.max(np.abs(s * v - dep_b)
                                    / np.abs(dep_b))))
    dev_tw = 0.0
    for t in T_GRID:
        wrong = sum(math.exp(-b * t) / (1.0 - math.exp(-6.0 * t))
                    for b in (0.75, 1.5, 2.25))
        dev_tw = max(dev_tw, abs(wrong - float(rho(t))) / float(rho(t)))
    check("A3.4 MUST-FAIL: mu2 tower best scalar %.4f residual %.3f; "
          "wrong mu4 class best scalar %.4f residual %.3f (both >= "
          "%.2f); wrong deck twists {3/4,3/2,9/4} miss rho by %.3f "
          "(>= %.2f, D5 mirror) -- the mu4 x mu3 clock is load-bearing"
          % (res[list(res)[0]][0], res[list(res)[0]][1],
             res[list(res)[1]][0], res[list(res)[1]][1], MUSTFAIL_RES,
             dev_tw, BAR_WRONGTWIST),
          all(r[1] >= MUSTFAIL_RES for r in res.values())
          and dev_tw >= BAR_WRONGTWIST)
    return wins


# ---------------------------------------------------------------- verdict
def a4_verdict():
    print("\nA4 -- verdict")
    n_pass = sum(1 for _n, ok in CHECKS if ok)
    n_all = len(CHECKS)
    a1 = all(ok for n, ok in CHECKS if n.startswith("A1"))
    a2 = all(ok for n, ok in CHECKS if n.startswith("A2"))
    a3_core = all(ok for n, ok in CHECKS
                  if n.startswith(("A3.1", "A3.2", "A3.3")))
    a3_mf = all(ok for n, ok in CHECKS if n.startswith("A3.4"))
    if a1 and a2 and a3_core and a3_mf:
        verdict = "MOONSHOT-STAGE2-GLUED"
    elif a1 and a2:
        verdict = "MOONSHOT-STAGE2-PARTIAL"
    else:
        verdict = "MOONSHOT-STAGE2-DIRECT-SUM" if not a3_core else \
            "MOONSHOT-STAGE2-PARTIAL"
    print("  %s" % verdict)
    if verdict == "MOONSHOT-STAGE2-GLUED":
        print("  one object, one normalization: T(t) = 2cosh(t/2) "
              "- rho(t) - Lambda-orbits,\n  finite places = the Z[i] "
              "Hecke tower (stage 1), arch place = the 48-site\n  NS "
              "lift flow, glued on the Z/12 = mu4 x mu3 character "
              "plane.  DECLARED-only\n  extras: sqrt(n) half-density "
              "(finite) and log pi self-dual scale (arch) --\n  the "
              "same s = 1/2 unitary normalization at every place.")
        print("  MISSING THEOREMS (named, measurement -> statement): "
              "(1) a Selberg/Lefschetz\n  trace formula for the "
              "commensurability groupoid with archimedean place =\n  "
              "the NS-lift flow (one statement producing 2cosh - rho "
              "- Lambda); (2) the\n  product formula / self-dual "
              "measure deriving log pi and the gamma\n  regularizer "
              "instead of declaring them; (3) the sigma-orbifold "
              "descent as a\n  quotient-groupoid theorem (stage 1); "
              "(4) the L1 continuum convergence\n  (Mosco / "
              "norm-resolvent, v679 template); (5) positivity (the "
              "Weil\n  criterion) -- untouched, the RH-level step.")
        print("  E8 honesty (stage-1 note continued): the finite "
              "counts are carrier-generic,\n  but the ARCH side is "
              "not: the mu4 selection (offset 1/4 -> Gamma_R) and "
              "the\n  mu3 deck (48 = 16 x 3, v628 twists) are "
              "load-bearing (A3.4 must-fails);\n  gluing forces a "
              "carrier with mu4 units and triality deck -- a "
              "rank-4\n  hermitian unimodular Z[i] lattice, which IS "
              "the Gaussian E8 by the cited\n  v634/v689 "
              "identification.  E8 becomes forced AT THE GLUING, not "
              "at the\n  finite places.")
    print("\n%d/%d checks passed" % (n_pass, n_all))
    print("VERDICT: %s" % verdict)
    print("PRIME.Z1.MOONSHOT.02: shared arch sector -- %s." % verdict)
    return n_pass == n_all


def run():
    t0 = time.time()
    print("=" * 72)
    print("MOONSHOT stage 2 -- the shared arch-sector test "
          "(one groupoid, one Weil measure)")
    print("=" * 72)
    g0_firewall()
    a1_unit_map()
    a2_trace_identity()
    print("\n    building the stage-1 groupoid comb to X = %d "
          "(Gaussian-class sieve) ..." % X_GEO)
    comb, meta = geo_comb(X_GEO)
    print("    sieve: %d irreducibles (%d split norms, ram ok=%s, "
          "%d inert bases), %d comb slots"
          % (meta["n_irred"], meta["n_split"], meta["ram_ok"],
             meta["n_inert"], len(comb)))
    a3_gluing(comb)
    ok = a4_verdict()
    print("total runtime %.1f s" % (time.time() - t0))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(run())
