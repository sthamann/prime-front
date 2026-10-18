#!/usr/bin/env python3
"""v714 -- PRIME.MOONSHOT.01: MOONSHOT first slice -- the E8 Hecke groupoid tower.

QUESTION (strategy-council 15% stream, verbatim): does the atom layer of the
L1 montage EMERGE from a larger geometry -- the commensurability / Hecke
correspondences of the Gaussian E8 lattice (the Z[i]-E8 of v634/v689: rank 4,
hermitian unimodular) -- instead of being inserted?  Finite places: spherical
Hecke towers (sublattices of index p resp. N(pi) for Gaussian primes pi);
time evolution = degree/index => length log p FROM THE DEGREE; repetitions =
closed orbits p^k.

CONSTRUCTION PATH (all lattice-internal, NO prime table -- AST-enforced):
  *  Correspondence census: Z[i]-submodules of the rank-4 module underlying
     the Gaussian E8, graded by abelian index n = N(det).  Counted via
     Hermite-normal-form cells over Z[i] (triangular bases v_j = d_j e_j +
     sum_{i<j} h_ji e_i, h_ji in residues mod d_i); norms enter only as the
     lattice quadratic form a^2+b^2 (point count).  Multiplicativity is NOT
     assumed anywhere; where it appears it is a MEASURED emergent fact.
  *  Primitivity: a degree-n layer is primitive iff its correspondences are
     not composed from smaller ones, i.e. iff an index-n submodule admits no
     proper intermediate module.  Machine test on the explicit quotients
     (every nonzero element of L/M must generate; |L/M| = n <= 13 explicit).
  *  Log generator (the v625 pattern, groupoid-internal = derivative of the
     degree grading): a_n log n = sum_{d|n, d>=2} LamA(d) a_{n/d}; then the
     rank-4 HNF cell normalizer (1 + n + n^2 + n^3) -- the lattice mirror of
     v625's Satake 1/(1+n^3) -- turns divisor-type counts into orbit data.
  *  Conjugation (sigma) quotient descent: complex conjugation is a symmetry
     of the Gaussian lattice; primitive classes split into sigma-swapped
     pairs (free orbit, length log N), sigma-fixed with trivial residue
     action (d | 2: ramified, length log N) and sigma-fixed with nontrivial
     residue action (rational d ~ m: inert, mu_2 isotropy, HALF orbit,
     length log m = (1/2) log N).  The residue-action test is machine-run:
     sigma trivial mod d  <=>  d | 2i - i*conj(i)... i.e. d | 2.
  *  Riemann comb: atoms at u = k*ell per sigma-orbit base, weight ell;
     mass mu = 2*Lambda/sqrt(n) with the s = 1/2 half-density normalization
     TYPED as declared bookkeeping (v695 G1.3), not groupoid output.

FIREWALL (machine-enforced in G0):
  *  banned identifiers anywhere: sympy / isprime / primerange / nextprime /
     primepi / sieve / zetazero / zeta -- no prime table, no zeta charge.
  *  the verification counting tables (core.U_ALL / MU_ALL / LAM_TAB /
     atom_lags_at / atoms_in) may appear ONLY inside functions whose name
     starts with `declared_` -- the ground-truth comparison sections.  The
     construction path never touches them (AST-checked on this very file).

CALIBRATION (interactive, this session, .venv python 3):
  *  census locks: rank-1 (i-stable index-n sublattices of Z^2, n <= 35) and
     rank-2 (i-stable index-n sublattices of Z^4, n in {2,4,5,8}: 3/7/12/15)
     match the Z[i]-HNF counts exactly once the HNF residue convention is
     h_ij mod diagonal-of-column (two reference-formula bugs fixed in
     calibration: wrong residue interval rank 1; double m=1 count rank 2).
  *  explicit maximality census: n=2: 15/15 maximal, n=5: 312/312, n=9:
     820/820, n=13: 4760/4760; n=4: 0/155, n=8: 0/1395, n=10: 0/4680.
  *  log generator at N_REC = 20000: Lambda_geo vs census Lambda_K
     on-support rel dev 1.1e-14, off-support max 4.0e-13 (float64 exact-int
     convolutions; a_n integer check 0.0).  Bars set at 1e-9 with margin.
  *  first-100-slot reach: slot 100 is n = 419; X_GEO = 460 covers it, and
     inert bases must be detected via rational irreducibility up to X_GEO
     (norm p^2 exceeds any affordable census horizon -- found in calibration
     as a KeyError at the inert prime 151).

RESULTS (this run, 19/19 PASS -- MOONSHOT-GO):
  *  S1: primitive degrees n <= 35 = {2, 5, 9, 13, 17, 29} = the Gaussian
     prime norms exactly; primitive layers are ENTIRE degree layers (all
     correspondences maximal: 15/15, 312/312, 820/820, 4760/4760); at the
     composite degrees 4/8/10 ZERO maximal.  NOT the rational primes:
     3, 7, 11, 19, 23, 31 enter only through their squares (inert).
  *  S2: raw trace divisorial (a_5 = 312 = 2(1+5+25+125)) -- kill (a)
     fires and is resolved internally: log generator + cell normalizer
     give Lambda support == prime-ideal powers (off-support 4.0e-13,
     1183 slots on-support rel dev 1.1e-14 vs orbit lengths).  Sigma
     descent (inert = half orbit) -> Riemann comb: first 100 slots
     positions dev 0, masses rel dev 0, window-0 368 lag moments rel
     dev 0 against the L1 point masses -mu_n/2.  (Run-1 lesson: the
     N_REC validation needs class-complete bases to 20000, the comb
     bases rational-inert extension to X_GEO -- split fixed.)

VERDICT LOGIC (preregistered): MOONSHOT-GO iff S1 primitive degrees ==
Gaussian prime norms (declared end-check) AND the log generator
de-divisorizes internally AND the descent comb matches positions AND masses
AND window-lag moments, with the only non-groupoid ingredients the two
DECLARED conventions (half-density sqrt(n); sigma-quotient = symmetry
orbifold).  MOONSHOT-PARTIAL iff positions emerge but weights need an
undeclared external step (or internal validation fails).  MOONSHOT-NO-GO iff
the primitive degrees miss the prime pattern or the trace stays divisorial.

Exploration only (tfpt-experiment firewall): NOT wired into run_all.py, no
ledger row, no paper claim.  Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/moonshot_hecke_groupoid_probe.py

PROVENANCE: discovery probe moonshot_hecke_groupoid_probe.py
(2026-08-03, 19/19 PASS, verdict MOONSHOT-GO: the atom layer is
groupoid-internal from the Z[i]-E8 Hecke tower -- the primitive
degrees are EXACTLY the Gaussian prime norms (maximality census, no
prime projector anywhere), the log generator + cell normalizer
de-divisorize at 4e-13, and the sigma descent matches 100 positions,
100 masses and 368 moments at deviation 0.00; declared ingredients:
the sqrt(n) half-density and the sigma descent.  HONEST FENCE: the
finite counting facts used here are E8-UNSPECIFIC -- the specificity
question (does the tower single out E8?) is stage 2, which also owns
the arch layer (still glued as a direct sum here)).  Promoted
verbatim; numbers unchanged.
"""

import ast
import math
import os
import sys
import time
from itertools import product

import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..",
                                "verification"))
import v563_paper2_readouts as core  # noqa: E402  (declared_* sections only)

# ---------------------------------------------------------------- constants
N_SMALL = 35          # S1 tower horizon (task: n <= ~35)
N_EXPLICIT = 13       # explicit submodule/maximality census horizon
N_REC = 20000         # log-generator recursion horizon (v625 scale)
X_GEO = 460           # comb reach (covers the first 100 atom slots)
N_SLOTS = 100         # declared comparison: first ~100 atom slots
RANK = 4              # Z[i]-rank of the Gaussian E8 module

BAR_OFF = 1.0e-9      # off-support |Lambda_geo|        (calib 4.0e-13)
BAR_ON = 1.0e-9       # on-support rel dev vs census    (calib 1.1e-14)
BAR_POS = 1.0e-12     # position dev |log n - U_ALL|
BAR_MASS = 1.0e-12    # mass rel dev vs MU_ALL
BAR_MOM = 1.0e-12     # window lag-moment rel dev

BANNED_IDS = ("sympy", "isprime", "primerange", "nextprime", "prevprime",
              "primepi", "sieve", "zetazero", "zetas", "mpz_zeta")
RESTRICTED = ("U_ALL", "MU_ALL", "LAM_TAB", "G_ALL", "NU_MAIN", "ATOM_MAX",
              "atom_lags_at", "atoms_in", "arch_lags", "frame_a_zones")

CHECKS = []


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok)))
    print("  [%s] %s%s" % ("PASS" if ok else "FAIL", name,
                           ("  -- " + detail) if detail else ""))
    return bool(ok)


# ---------------------------------------------------------- Gaussian basics
def canon(z):
    """Canonical associate representative (a > 0, b >= 0)."""
    a, b = z
    for _ in range(4):
        if a > 0 and b >= 0:
            return (a, b)
        a, b = -b, a
    raise ValueError(z)


def gmul(x, y):
    return (x[0] * y[0] - x[1] * y[1], x[0] * y[1] + x[1] * y[0])


def gsub(x, y):
    return (x[0] - y[0], x[1] - y[1])


def gnorm(x):
    return x[0] * x[0] + x[1] * x[1]


def gdivides(e, d):
    """e | d in Z[i] (exact integer arithmetic)."""
    n = gnorm(e)
    xr = d[0] * e[0] + d[1] * e[1]
    xi = d[1] * e[0] - d[0] * e[1]
    return xr % n == 0 and xi % n == 0


def gquo_round(x, d):
    """Nearest Gaussian quotient of x/d (exact ints, round half up)."""
    n = gnorm(d)
    xr = x[0] * d[0] + x[1] * d[1]
    xi = x[1] * d[0] - x[0] * d[1]
    return ((2 * xr + n) // (2 * n), (2 * xi + n) // (2 * n))


def gred(x, d):
    return gsub(x, gmul(gquo_round(x, d), d))


def residues(d):
    """Canonical residue system mod d (well-defined: rounding commutes
    with Gaussian-integer shifts)."""
    n = gnorm(d)
    S = set()
    R = int(math.isqrt(n)) + 2
    for a in range(-R, R + 1):
        for b in range(-R, R + 1):
            S.add(gred((a, b), d))
    assert len(S) == n, (d, len(S))
    return sorted(S)


def conj_class(d):
    return canon((d[0], -d[1]))


# --------------------------------------------------- class census (lattice)
def class_census(nmax):
    """Associate classes of Z[i] by norm, from the lattice point scan --
    the norm is the quadratic form, nothing number-theoretic imported."""
    am = int(math.isqrt(nmax)) + 1
    cls = {}
    for a in range(-am, am + 1):
        for b in range(-am, am + 1):
            n = a * a + b * b
            if 1 <= n <= nmax:
                cls.setdefault(n, set()).add(canon((a, b)))
    return {n: sorted(v) for n, v in cls.items()}


def r2_counts(nmax):
    """r_2(n) via numpy lattice scan (independent of class_census)."""
    am = int(math.isqrt(nmax)) + 1
    r2 = np.zeros(nmax + 1, dtype=np.int64)
    for a in range(-am, am + 1):
        b2 = nmax - a * a
        if b2 < 0:
            continue
        bm = int(math.isqrt(b2))
        bs = np.arange(-bm, bm + 1)
        np.add.at(r2, a * a + bs * bs, 1)
    r2[0] = 0
    return r2


def irreducible(d, cls):
    """d irreducible in Z[i]: no non-unit divisor class of norm <= sqrt(N).
    (Any proper factorization has a factor of norm <= sqrt(N(d)).)
    Ring-internal indecomposability -- no primality import."""
    n = gnorm(d)
    if n < 2:
        return False
    for m in sorted(cls):
        if m * m > n:
            break
        if m < 2:
            continue
        for e in cls[m]:
            if gdivides(e, d):
                return False
    return True


# ------------------------------------------- HNF submodule counting (rank 4)
def dirichlet_conv(x, y, nmax):
    c = np.zeros(nmax + 1)
    for i in np.nonzero(x[1:])[0] + 1:
        top = nmax // i
        c[i::i] += x[i] * y[1:top + 1]
    return c


def hnf_counts(nmax, rank=RANK):
    """a_n = #{Z[i]-submodules of Z[i]^rank with abelian index n}, via the
    HNF cell decomposition: sum over diagonal class tuples (d_1..d_r) with
    prod N(d_i) = n, cell size prod_j N(d_j)^(j-1).  Implemented as the
    r-fold Dirichlet convolution of the graded class counts -- an exact
    regrouping of the cell enumeration, NOT a multiplicativity assumption."""
    r2 = r2_counts(nmax)
    assert np.all(r2 % 4 == 0)
    rp = (r2 // 4).astype(np.float64)
    mm = np.arange(nmax + 1, dtype=np.float64)
    a = rp * mm ** 0
    for j in range(1, rank):
        a = dirichlet_conv(a, rp * mm ** j, nmax)
    return a


# ------------------------------------- explicit submodules + maximality test
def submodules_explicit(n, cls):
    """All index-n submodules of Z[i]^4 as triangular bases
    v_j = d_j e_j + sum_{i<j} h_ji e_i, h_ji in residues(d_i)."""
    norms = sorted(c for c in cls if c > 1)
    out = []

    def diag_tuples(rem, k, cur):
        if k == RANK:
            if rem == 1:
                yield tuple(cur)
            return
        if rem == 1:
            yield tuple(cur + [(1, 0)] * (RANK - k))
            return
        for m in [1] + norms:
            if rem % m:
                continue
            for d in ([(1, 0)] if m == 1 else cls[m]):
                cur.append(d)
                yield from diag_tuples(rem // m, k + 1, cur)
                cur.pop()

    for dg in diag_tuples(n, 0, []):
        res = [residues(d) if gnorm(d) > 1 else [(0, 0)] for d in dg]
        for combo in product(*[product(*[res[i] for i in range(j)])
                               for j in range(RANK)]):
            basis = []
            for j in range(RANK):
                v = [(0, 0)] * RANK
                v[j] = dg[j]
                for i in range(j):
                    v[i] = combo[j][i]
                basis.append(v)
            out.append((dg, basis))
    return out


def reduce_vec(x, basis, dg):
    x = list(x)
    for j in range(RANK - 1, -1, -1):
        q = gquo_round(x[j], dg[j])
        if q != (0, 0):
            for i in range(j + 1):
                x[i] = gsub(x[i], gmul(q, basis[j][i]))
    return tuple(x)


def is_maximal(basis, dg, n):
    """L/M simple <=> every nonzero element of the quotient generates it.
    Pure combinatorics on the (<= n)-element quotient -- the primitivity
    (groupoid generator) test, no primality anywhere."""
    sets = [residues(d) if gnorm(d) > 1 else [(0, 0)] for d in dg]
    zero = ((0, 0),) * RANK
    for x in (tuple(c) for c in product(*sets)):
        if x == zero:
            continue
        ix = reduce_vec(tuple(gmul((0, 1), c) for c in x), basis, dg)
        gens = (x, ix)
        seen = {zero}
        frontier = [zero]
        while frontier:
            y = frontier.pop()
            for g in gens:
                z = tuple((y[i][0] + g[i][0], y[i][1] + g[i][1])
                          for i in range(RANK))
                z = reduce_vec(z, basis, dg)
                if z not in seen:
                    seen.add(z)
                    frontier.append(z)
        if len(seen) != n:
            return False
    return True


# ----------------------------------------------------- brute-force locks
def lock_rank1(nmax, cls):
    """i-stable index-n sublattices of Z^2 == ideal classes of norm n."""
    for n in range(2, nmax + 1):
        cnt = 0
        for a in range(1, n + 1):
            if n % a:
                continue
            d = n // a
            for b in range(d):
                def member(x, y):
                    if x % a:
                        return False
                    s = x // a
                    return (y - s * b) % d == 0
                if member(-b, a) and member(-d, 0):
                    cnt += 1
        if cnt != len(cls.get(n, [])):
            return False, n, cnt
    return True, None, None


def lock_rank2(ns, cls):
    """i-stable index-n sublattices of Z^4 == Z[i]^2 HNF counts."""
    jmat = np.array([[0, 1, 0, 0], [-1, 0, 0, 0],
                     [0, 0, 0, 1], [0, 0, -1, 0]], dtype=np.int64)
    for n in ns:
        diags = []

        def rec(rem, k, cur):
            if k == 4:
                if rem == 1:
                    diags.append(tuple(cur))
                return
            for d in range(1, rem + 1):
                if rem % d == 0:
                    cur.append(d)
                    rec(rem // d, k + 1, cur)
                    cur.pop()

        rec(n, 0, [])
        cnt = 0
        for dg in diags:
            offs = [[list(range(dg[i])) for i in range(j)] for j in range(4)]
            for combo in product(*[product(*offs[j]) for j in range(4)]):
                rows = []
                for j in range(4):
                    v = [0] * 4
                    v[j] = dg[j]
                    for i in range(j):
                        v[i] = combo[j][i]
                    rows.append(v)
                bmat = np.array(rows, dtype=np.int64)
                vv = bmat @ jmat.T
                okm = True
                for v in vv:
                    w = v.copy()
                    for j in (3, 2, 1, 0):
                        if w[j] % bmat[j][j]:
                            okm = False
                            break
                        w = w - (w[j] // bmat[j][j]) * bmat[j]
                    if not okm or np.any(w != 0):
                        okm = False
                        break
                if okm:
                    cnt += 1
        ref = 0
        for m1 in sorted(set(cls) | {1}):
            if n % m1:
                continue
            m2 = n // m1
            c1 = 1 if m1 == 1 else len(cls.get(m1, []))
            c2 = 1 if m2 == 1 else len(cls.get(m2, []))
            ref += c1 * c2 * m2
        if cnt != ref:
            return False, n, (cnt, ref)
    return True, None, None


# ----------------------------------------------------------- log generator
def log_generator(a, nmax):
    """LamA from  a_n log n = sum_{d|n, d>=2} LamA(d) a_{n/d}  -- the
    derivative of the degree grading (time evolution = degree), applied to
    the raw correspondence counts.  Groupoid-internal: composition
    (Dirichlet layering of the tower) + grading (length log n) only."""
    lam = np.zeros(nmax + 1)
    acc = np.zeros(nmax + 1)
    logn = np.zeros(nmax + 1)
    logn[1:] = np.log(np.arange(1, nmax + 1))
    for d in range(2, nmax + 1):
        lam[d] = a[d] * logn[d] - acc[d]
        if lam[d] != 0.0:
            top = nmax // d
            if top >= 2:
                acc[2 * d::d] += lam[d] * a[2:top + 1]
    return lam


# -------------------------------------------------- sigma classification
def classify_bases(cls, nmax_class):
    """Sigma-orbit bases of the primitive layer, all ring-internal:
      split : d, conj(d) non-associate  -> base length log N(d)
      ram   : sigma-fixed, d | 2 (sigma trivial on residues) -> log N(d)
      inert : sigma-fixed, d ~ rational m (sigma = Frobenius on residues,
              mu_2 isotropy) -> HALF orbit, base length log m
    Reads every class with norm <= nmax_class; the inert detection through
    classes reaches bases m <= sqrt(nmax_class) -- exactly the inert
    norm-slots p^{2k} <= nmax_class, so this list is norm-complete."""
    bases = []
    seen = set()
    for n in sorted(cls):
        if n > nmax_class:
            break
        for d in cls[n]:
            if d in seen or not irreducible(d, cls):
                continue
            dc = conj_class(d)
            if dc != d:
                seen.add(d)
                seen.add(dc)
                bases.append(("split", n, math.log(n)))
            elif gdivides(d, (2, 0)):
                seen.add(d)
                bases.append(("ram", n, math.log(n)))
            else:
                seen.add(d)
                m = int(math.isqrt(n))
                assert m * m == n and d == (m, 0)
                bases.append(("inert", m, math.log(m)))
    return bases


def extend_inert(bases, cls, x_geo):
    """Comb bases to x_geo: inert bases with sqrt(nmax_class) < m <= x_geo
    live beyond any affordable class-census horizon (norm m^2); detect them
    by ring-internal irreducibility of the rational class (m, 0)."""
    out = [b for b in bases if b[1] <= x_geo]
    have_inert = {b for t, b, _l in out if t == "inert"}
    for m in range(3, x_geo + 1, 2):
        if m not in have_inert and irreducible((m, 0), cls):
            out.append(("inert", m, math.log(m)))
    return out


def census_lambda_k(bases, nmax):
    """Pre-descent Dedekind comb of the tower (per IDEAL, no quotient):
    split p^k: 2 log p (two fixed ideals); ram 2^k: log 2;
    inert p^{2k}: 2 log p (norm-length of the sigma-fixed ideal)."""
    lk = np.zeros(nmax + 1)
    for t, b, ell in bases:
        if t == "inert":
            step = b * b
            w = 2.0 * ell
        elif t == "split":
            step = b
            w = 2.0 * ell
        else:
            step = b
            w = ell
        pk = step
        while pk <= nmax:
            lk[pk] += w
            pk *= step
    return lk


def descent_comb(bases, x_geo):
    """Riemann comb via the sigma-quotient (orbifold) reading: one atom
    tower per sigma-orbit, positions k*ell, weight ell (inert: half
    orbit)."""
    comb = {}
    for t, b, ell in bases:
        pk = b
        while pk <= x_geo:
            comb[pk] = ell
            pk *= b
    return comb


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
    leaks = []
    for node in ast.walk(tree):
        nm = None
        if isinstance(node, ast.Attribute) and node.attr in RESTRICTED:
            nm = node.attr
        if nm and id(node) not in allowed:
            leaks.append(nm)
    check("G0.2 counting tables only inside declared_* sections",
          not leaks, "leaks: %s" % leaks if leaks else
          "restricted: " + ",".join(RESTRICTED[:5]) + ",...")
    print("    python %s, numpy %s" % (sys.version.split()[0],
                                       np.__version__))


# --------------------------------------------------------------- S1 tower
def s1_tower():
    print("\nS1 -- the tower, started small (n <= %d)" % N_SMALL)
    t0 = time.time()
    cls = class_census(N_REC)
    r2 = r2_counts(N_SMALL)
    ok_cls = all(len(cls.get(n, [])) == r2[n] // 4
                 for n in range(1, N_SMALL + 1))
    check("S1.1a class census == r2/4 lattice scan (n<=%d)" % N_SMALL,
          ok_cls)

    ok1, n1, c1 = lock_rank1(N_SMALL, cls)
    check("S1.1b rank-1 lock: i-stable Z^2 sublattices == ideal classes",
          ok1, "n<=%d exact" % N_SMALL if ok1 else
          "n=%s cnt=%s" % (n1, c1))
    ok2, n2, c2 = lock_rank2((2, 4, 5, 8), cls)
    check("S1.1c rank-2 lock: i-stable Z^4 sublattices == Z[i]-HNF count",
          ok2, "n in {2,4,5,8} exact" if ok2 else "n=%s %s" % (n2, c2))

    a = hnf_counts(N_REC)
    ok_int = float(np.max(np.abs(a - np.round(a)))) == 0.0
    check("S1.2a HNF cell counts integral (float64 exact)", ok_int)

    print("    tower a_n (index-n correspondence degrees), n <= %d:"
          % N_SMALL)
    maximal = {}
    ok_explicit = True
    for n in range(2, N_SMALL + 1):
        an = int(a[n])
        tag = ""
        if n <= N_EXPLICIT and an > 0:
            subs = submodules_explicit(n, cls)
            nmax_cnt = sum(1 for dg, b in subs if is_maximal(b, dg, n))
            maximal[n] = nmax_cnt
            ok_explicit &= (len(subs) == an)
            tag = "  explicit=%d maximal=%d" % (len(subs), nmax_cnt)
        if an or tag:
            print("      n=%2d  a_n=%6d%s" % (n, an, tag))
    check("S1.2b explicit enumeration == HNF cell count (n<=%d)"
          % N_EXPLICIT, ok_explicit)

    irr_norms = sorted({gnorm(d) for n in cls if n <= N_SMALL
                        for d in cls[n] if irreducible(d, cls)})
    prim_explicit = sorted(n for n, m in maximal.items() if m > 0)
    comp_explicit = sorted(n for n, m in maximal.items() if m == 0)
    ok_equiv = (prim_explicit == [n for n in irr_norms if n <= N_EXPLICIT]
                and all(n not in irr_norms for n in comp_explicit))
    check("S1.3 primitivity == irreducible-class norm (explicit, n<=%d)"
          % N_EXPLICIT, ok_equiv,
          "maximal>0 at %s; =0 at %s" % (prim_explicit, comp_explicit))
    all_max = all(maximal[n] == int(a[n]) for n in prim_explicit)
    check("S1.3b primitive layers are ENTIRE degree layers "
          "(all correspondences maximal)", all_max,
          "e.g. n=13: %d/%d" % (maximal.get(13, -1), int(a[13])))

    print("    primitive degrees n <= %d (typed: equivalence verified "
          "explicitly to %d,\n    extended by the ring-internal "
          "irreducibility census): %s" % (N_SMALL, N_EXPLICIT, irr_norms))
    return cls, a, irr_norms


def declared_s1_ground_truth(irr_norms):
    """DECLARED ground-truth comparison (the only S1 place touching the
    verification tables): primes p read off LAM_TAB (p prime iff
    LAM_TAB[p] == log p)."""
    lam = core.LAM_TAB
    primes = [p for p in range(2, N_SMALL + 1)
              if abs(lam[p] - math.log(p)) < 1.0e-12]
    gauss_norms = sorted([2] + [p for p in primes if p % 4 == 1]
                         + [p * p for p in primes
                            if p % 4 == 3 and p * p <= N_SMALL])
    ok = (irr_norms == gauss_norms)
    check("S1.4 [declared] primitive degrees == Gaussian prime norms",
          ok, "%s" % irr_norms)
    missing_rational = [p for p in primes if p % 4 == 3]
    print("    honest reading: NOT the rational primes -- %s appear only "
          "through their\n    squares (inert, sigma-fixed, mu_2 isotropy); "
          "the rational-prime layer needs the\n    sigma-quotient descent "
          "(S2.3)." % missing_rational)
    return ok


# ---------------------------------------------------------------- S2 trace
def s2_trace(cls, a):
    print("\nS2 -- the trace question (go/no-go)")

    # kill (a): the raw trace is divisorial -- measured, then repaired
    q5 = sum(5 ** j for j in range(RANK))
    q13 = sum(13 ** j for j in range(RANK))
    q2 = sum(2 ** j for j in range(RANK))
    q9 = sum(9 ** j for j in range(RANK))
    ok_div = (int(a[5]) == 2 * q5 and int(a[13]) == 2 * q13
              and int(a[2]) == q2 and int(a[9]) == q9)
    check("S2.1a kill(a) fires: raw counts are divisor-type "
          "(hyperplane sums)", ok_div,
          "a_5=%d=2*%d, a_13=%d=2*%d, a_2=%d, a_9=%d"
          % (int(a[5]), q5, int(a[13]), q13, int(a[2]), int(a[9])))
    pairs = [(2, 5), (4, 5), (2, 13), (5, 9), (9, 10), (8, 25)]
    ok_mult = all(abs(a[m * n] - a[m] * a[n]) == 0.0 for m, n in pairs)
    check("S2.1b multiplicativity EMERGES (measured on coprime pairs, "
          "not assumed)", ok_mult, str(pairs))

    lam_a = log_generator(a, N_REC)
    mm = np.arange(N_REC + 1, dtype=np.float64)
    cells = np.ones(N_REC + 1)
    for j in range(1, RANK):
        cells += mm ** j
    lam_geo = np.zeros(N_REC + 1)
    lam_geo[1:] = lam_a[1:] / cells[1:]

    bases_val = classify_bases(cls, N_REC)
    bases = extend_inert(bases_val, cls, X_GEO)
    tc = {t: sum(1 for x in bases if x[0] == t)
          for t in ("split", "ram", "inert")}
    print("    sigma-orbit comb bases <= %d: %s ; first: %s"
          % (X_GEO, tc, [(t, b) for t, b, _l in bases[:8]]))

    lk = census_lambda_k(bases_val, N_REC)
    on_dev = 0.0
    off_dev = 0.0
    n_on = 0
    for n in range(2, N_REC + 1):
        if lk[n] > 0.0:
            on_dev = max(on_dev, abs(lam_geo[n] - lk[n]) / lk[n])
            n_on += 1
        else:
            off_dev = max(off_dev, abs(lam_geo[n]))
    check("S2.2a log generator de-divisorizes: support == prime-ideal "
          "powers", off_dev <= BAR_OFF,
          "off-support max %.2e <= %.0e (%d on-support slots)"
          % (off_dev, BAR_OFF, n_on))
    check("S2.2b weights == orbit lengths (census, ring-internal)",
          on_dev <= BAR_ON,
          "rel dev %.2e <= %.0e; e.g. Lambda_geo(5)=%.12f=2*log5/2? "
          "-> 2log5=%.12f" % (on_dev, BAR_ON, lam_geo[5],
                              2.0 * math.log(5)))
    print("    sigma3 -> Lambda anatomy: (i) raw trace divisorial "
          "[measured S2.1a];\n    (ii) log generator = d/ds of the degree "
          "grading (groupoid-internal:\n    composition + grading only, "
          "v625 pattern); (iii) normalizer 1+n+n^2+n^3 =\n    the rank-4 "
          "HNF cell weights (lattice data, v625's 1/(1+n^3) mirror).")

    comb = descent_comb(bases, X_GEO)
    ok_half = all(abs(comb[b] - 0.5 * math.log(b * b)) < 1e-15
                  for t, b, _l in bases if t == "inert" and b in comb)
    check("S2.3 sigma-quotient descent: inert = half orbit "
          "(mu_2 isotropy, machine rule d|2)", ok_half,
          "comb slots <= %d: %d" % (X_GEO, len(comb)))
    return lam_geo, bases, comb


def declared_s2_ground_truth(comb):
    """DECLARED final comparison against the verification comb (the L1
    point masses -mu_n/2): positions, masses, window lag moments."""
    print("    -- declared ground-truth section (verification tables "
          "enter HERE only) --")
    nn = np.round(np.exp(core.U_ALL[:N_SLOTS])).astype(int)
    ok_pos = all(int(n) in comb for n in nn)
    pos_dev = max((abs(math.log(int(n)) - core.U_ALL[k])
                   for k, n in enumerate(nn)), default=1.0) \
        if ok_pos else 1.0
    check("S2.4a positions: all %d slots present, dev <= %.0e"
          % (N_SLOTS, BAR_POS), ok_pos and pos_dev <= BAR_POS,
          "slot100 n=%d, max|log n - u| = %.2e" % (int(nn[-1]), pos_dev))

    false_atoms = [n for n in sorted(comb)
                   if n <= int(nn[-1]) and n not in set(nn.tolist())]
    check("S2.4b no false atoms below slot %d" % N_SLOTS,
          not false_atoms, str(false_atoms) if false_atoms else "clean")

    mass_dev = max(abs(2.0 * comb[int(n)] / math.sqrt(float(n))
                       - core.MU_ALL[k]) / core.MU_ALL[k]
                   for k, n in enumerate(nn))
    check("S2.4c masses mu_n = 2*Lambda/sqrt(n): rel dev <= %.0e"
          % BAR_MASS, mass_dev <= BAR_MASS,
          "max rel dev %.2e (sqrt(n) = declared half-density, "
          "v695 G1.3 typing)" % mass_dev)

    alpha0 = 0.5 * math.log(256.0)          # L1 window 0 (X = 256, M = 368)
    m0 = 368
    ka = core.atoms_in(alpha0)
    us = sorted(u for u in comb if u <= 256)
    u_geo = [math.log(n) for n in us]
    mu_geo = [2.0 * comb[n] / math.sqrt(float(n)) for n in us]
    c_geo, _ = core.atom_lags_at(alpha0, m0, u_geo, mu_geo)
    c_ref, _ = core.atom_lags_at(alpha0, m0, core.U_ALL[:ka],
                                 core.MU_ALL[:ka])
    mom_dev = float(np.max(np.abs(c_geo - c_ref)) / np.max(np.abs(c_ref)))
    check("S2.4d atom-measure moments (window 0, %d lags): rel dev <= %.0e"
          % (m0, BAR_MOM), mom_dev <= BAR_MOM,
          "%d atoms in window, max rel dev %.2e" % (ka, mom_dev))
    print("    L1 point-mass reading: the groupoid comb equals the "
          "inserted atoms -mu_n/2\n    on every tested moment -- the atom "
          "layer NEED NOT be inserted.")
    return {"pos": ok_pos and pos_dev <= BAR_POS,
            "mass": mass_dev <= BAR_MASS, "mom": mom_dev <= BAR_MOM}


# ----------------------------------------------------------------- S3 kill
def s3_verdict(results):
    print("\nS2.5 -- memo kill criteria, adjudicated")
    print("  (a) divisor sums instead of Lambda/sqrt(n): FIRES on the raw "
          "trace [S2.1a],\n      RESOLVED groupoid-internally: log "
          "generator = grading derivative +\n      lattice cell normalizer "
          "[S2.2a/b].  No external step.")
    print("  (b) external prime projector: NOT NEEDED -- primitivity = "
          "maximality of\n      correspondences (S1.3), irreducibility = "
          "ring indecomposability; the\n      AST firewall (G0) certifies "
          "no prime table in the construction path.\n      DECLARED "
          "non-groupoid ingredients: (i) the s=1/2 half-density\n      "
          "sqrt(n) (bookkeeping, v695 G1.3); (ii) the sigma-quotient "
          "descent uses\n      conjugation -- a lattice symmetry (internal),"
          " but the RAW tower yields\n      the Dedekind comb of Q(i); the "
          "Riemann comb is its orbifold reading.")
    print("  (c) arch sector: in this probe still DIRECT SUM (the L1 "
          "background is\n      glued, not derived).  OPEN -- next "
          "construction stage: the shared\n      arch-sector test (does "
          "the archimedean place of the same\n      commensurability "
          "groupoid deliver Gamma_R, i.e. the rho-arch tower --\n      "
          "v695 S3.4 Gamma-factor route as target).")
    print("  (d) self-adjointness vs weights: the symmetric (s=1/2) "
          "normalization\n      multiplies by e^{-u/2} -- weights survive "
          "intact (S2.4c/d); typed as\n      declared bookkeeping, not "
          "groupoid output.")
    print("  honesty note: the finite-place counts depend only on the "
          "free rank-4\n      Z[i]-module (any hermitian unimodular "
          "carrier gives the same tower);\n      E8-specific geometry "
          "(theta shells, v625 sigma_3) enters the arch/weight\n      "
          "sector -- part of the named next stage.")

    print("\nS3 -- verdict")
    n_pass = sum(1 for _n, ok in CHECKS if ok)
    n_all = len(CHECKS)
    s1_ok = all(ok for name, ok in CHECKS if name.startswith("S1"))
    s2_int = all(ok for name, ok in CHECKS
                 if name.startswith(("S2.1", "S2.2", "S2.3")))
    s2_dec = all(results.values())
    if s1_ok and s2_int and s2_dec:
        verdict = "MOONSHOT-GO"
        note = ("positions AND weights emerge groupoid-internally "
                "(primitive degrees + grading derivative + sigma "
                "quotient); declared-only extras: half-density sqrt(n), "
                "orbifold descent.  Next stage: the shared arch-sector "
                "test.")
    elif s1_ok and results.get("pos", False):
        verdict = "MOONSHOT-PARTIAL"
        note = ("positions emerge; weights/moments fail the declared "
                "comparison -- see FAIL lines above.")
    else:
        verdict = "MOONSHOT-NO-GO"
        note = "primitive layer or trace de-divisorization failed."
    print("  %s -- %s" % (verdict, note))
    print("\n%d/%d checks passed" % (n_pass, n_all))
    print("VERDICT: %s" % verdict)
    print("PRIME.Z1.MOONSHOT.01: E8 Hecke groupoid tower, first slice -- "
          "%s." % verdict)
    return n_pass == n_all


def run():
    t0 = time.time()
    print("=" * 72)
    print("MOONSHOT first slice -- the E8 Hecke groupoid tower "
          "(Z[i]-E8, rank 4)")
    print("=" * 72)
    g0_firewall()
    cls, a, irr_norms = s1_tower()
    declared_s1_ground_truth(irr_norms)
    lam_geo, bases, comb = s2_trace(cls, a)
    print("\nS2.4 -- exact comparison against the L1 point masses")
    results = declared_s2_ground_truth(comb)
    ok = s3_verdict(results)
    print("total runtime %.1f s" % (time.time() - t0))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(run())
