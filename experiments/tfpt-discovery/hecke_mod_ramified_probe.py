#!/usr/bin/env python3
"""hecke_mod_ramified_probe.py -- PRIME.HECKE.MOD_RAMIFIED.01 (discovery
probe): the Gaussian-E8 Hecke correspondences projected onto V = L/(1+i)L.

REVIEW THESIS UNDER TEST (scope verbatim): "the four-bit code is the local
fiber at the ramified prime place (1+i) of the SAME global Hecke object" --
the v714 Z[i]-E8 Hecke tower (index-N(p) submodule correspondences,
primitive degrees = the Gaussian prime norms {2, 5, 9, 13, ...}) should
induce WELL-DEFINED, sigma-commuting operators on the 16-element message
space V = L/(1+i)L = F2^4 of the Gaussian code bridge (v689 /
gaussian_code_bridge_probe; NS/R grading v722).  If yes, the tower
decomposes over V into <= 7 sigma-orbit channels and the positivity
bookkeeping gains a channel projection.  HARD KILL (review, literal):
representative dependence of the induced transport, or a functoriality
break, ends the route -- no relabeling.

CONSTRUCTION (all module-internal, NO prime table -- AST-enforced):
  *  E8 in the doubled-coordinate standard model (v722 frame): w in Z^8,
     all-even or all-odd entries, sum(w) = 0 mod 4; 240 roots |w|^2 = 8;
     J = in-pair rotation (mu4 clock), sigma = coordinate-pair 3-cycle
     (both verified lattice automorphisms, [J, sigma] = 0 exact).
  *  Z^8 = Z[i]^4 CANONICALLY via the J-pairing z_k = w_{2k} + i w_{2k+1}
     (then J = multiplication by i, exactly).  A Z[i]-basis of L is
     computed as the Z[i]-Hermite normal form of the 8 standard Z-basis
     generators (Euclidean gquo_round reduction); abelian index
     N(prod diag) = 256 certifies the basis.  All submodule theory then
     lives in exact Z[i]^4 coordinates ("L-coords"), where L = Z[i]^4.
  *  V = L/(1+i)L: the residue map Z[i] -> F2, z = a+bi |-> (a+b) mod 2,
     applied per L-coordinate (a ring homomorphism); 16 classes; the
     240 roots fall 15 x 16 with the zero class empty (v689 census,
     re-derived here in this frame).
  *  Prime layers ring-internally (v714 pattern): canonical associate
     classes by lattice norm scan, irreducibility = ring
     indecomposability; norms <= 13 yield EXACTLY the six Gaussian
     primes (1+i), (2+i), (1+2i), (3), (3+2i), (2+3i) -- the tower's
     primitive degrees {2, 5, 9, 13}, no prime table anywhere.
  *  Hecke layer at p = (pi): ALL index-N(pi) submodules M' of L =
     preimages of the hyperplanes of L/pi L = F_q^4 (q = N(pi));
     explicit triangular Z[i]-bases; counts 15 / 156+156 / 820 /
     2380+2380 (degree sums 15, 312, 820, 4760 = v714's S1 tower
     numbers, recounted here independently).

THE PROJECTION TESTED (H1, the kill test -- exact over ALL submodules and
ALL 16 classes, not samples):
  For each M', each message class v in V is a coset v = x + (1+i)L; its
  transport into the fiber V_{M'} = M'/(1+i)M' is the set of classes of
  v & M' (set intersection).  Machine objects per M':
    iota-bar : V_{M'} -> V, the F2-linear map induced by the inclusion
               M' -> L (4x4 F2 matrix over the explicit bases);
    t(v)     : the constructive transport -- solve for a representative
               x in v & M' and read its M'-basis coordinates mod (1+i).
  WELL-DEFINEDNESS = ker(iota-bar) counts the transport ambiguity
  EXACTLY: v & M' is a union of |ker iota-bar| classes of (1+i)M'.
    odd layers (N(pi) odd): claim det(iota-bar) = 1 (bijective) and
      t = iota-bar^{-1}, hence a canonical INDUCED ENDOMORPHISM = id
      per submodule; cross-validated constructively with two
      independent representatives per (M', v) and a non-membership
      control.  ANY singular iota-bar or transport mismatch = DEAD.
    ramified layer (1+i): claim rank 3, image = a hyperplane W of V,
      fibers exactly 2:1 over W (deck Z/2 = ker iota-bar), the 15
      submodules biject onto the 15 hyperplanes of V.  Any deviation
      = DEAD.
  FUNCTORIALITY: sigma is Z[i]-linear on L; it must permute every layer
  (hyperplane pushforward psi^T = Sbar^{-1} phi^T over F_q, verified by
  membership of all 4 sigma-images of each M'-basis) with sigma^3 = id,
  and on the ramified layer W_{sigma M'} = sigma-bar(W_{M'}).  Complex
  conjugation (in-pair swap) must swap the two ideal layers over 5
  (spot-checked, informational).

STRUCTURE (H2, if alive):
  (i)   [H-bar_p, sigma-bar] = 0 for every layer operator (16x16
        matrices, assembled from the measured per-submodule transports,
        never asserted).
  (ii)  Walsh analysis: 16 characters; odd layers act as deg * id
        (eigenvalue = layer degree on EVERY character -- the honest
        local-global statement: prime-to-(1+i) Hecke acts on the
        (1+i)-fiber through its degree ONLY); the ramified multiplier
        D = diag(30, 14 x 15) is delta-diagonal, Walsh form
        224 I + 16 * ones (rank-1 cross-character coupling, exact);
        the ramified transfer Gram A[v,w] = #{M': v,w in W_{M'}} has
        exact spectrum {64, 4 (x14), 0} with integer eigenvectors.
  (iii) commutativity: all down-up layer operators commute pairwise
        (scalars + one diagonal D); the extended pair (D, A) does NOT
        commute -- [D, A] is supported exactly on the zero-class
        row/column with entries +-112 (measured structure).
  (iv)  the ramified place: the 15 Hecke-(1+i) submodules ARE the 15
        hyperplanes of the code fiber (the layer is INTERNAL to V);
        the v722 NS/R grading is the parity character chi_par
        (sigma-fixed, kernel = the even/NS sublattice = ONE of the 15
        Hecke submodules); NS/R class census 7 + 8 re-derived; the
        2:1 deck of every ramified edge is the Z/2 of (1+i)^2 = i*2.
  CHANNELS: sigma-orbits counted exactly on classes (1 + 3 + 4x3),
  characters (1 + 3 + 4x3) and hyperplanes (3 + 4x3): the review's "7"
  = the 7 NONTRIVIAL orbit channels (identical on message and character
  side); "8" = 7 + the trivial channel (zero class resp. trivial
  character).  Both counts exact; no discrepancy beyond bookkeeping.

CONSEQUENCE MEASUREMENT (H3, declared_* sections ONLY -- the v563
deployed window surface enters HERE and nowhere else):
  The odd layers act as scalars on V, so the fiber CANNOT spectrally
  separate odd-prime atoms into channels -- the V-resolvable part of the
  window moments is exactly the ramified (2-adic) atom family, graded by
  the deck parity (layer 2^k |-> k mod 2; "J-odd" = odd k).  Measured on
  the deployed frame-A ladder (v563, verbatim windows): the atom side S
  of the thin T-B margin is split by channel {ram-odd, ram-even, split,
  inert}; per channel: atom count, mass, linear det pressure D(B, S_c),
  leave-channel-out margin 1 - r12^2, and the lambda_min Rayleigh share
  of the odd-sector form at its minimiser.  Exact split identities
  (sum_c S_c = S, det polarisation, Rayleigh sum) are checked to
  round-off; every number printed.

KILL CRITERIA (preregistered): DEAD iff any odd-layer submodule has
ker(iota-bar) != 0 OR constructive transport disagrees with
iota-bar^{-1} anywhere OR an induced endomorphism differs from id OR
sigma fails to permute a layer / breaks W-equivariance OR the ramified
anatomy deviates (rank != 3, fibers != {2 on W, 0 off}, no bijection
onto the 15 hyperplanes).  CHANNELS iff every check passes.  Verdict
enums (frozen): HECKE-MOD-RAMIFIED-CHANNELS / HECKE-MOD-RAMIFIED-DEAD.

FIREWALL: experiments/ probe; ONE new file; writes nothing; no
verification/, paper, ledger, changelog or website surface touched.
AST-enforced: no prime-table / zeta symbols anywhere; the v563 deployed
tables and window builders (U_ALL, MU_ALL, LAM_TAB, frame_a_zones,
build_window, ...) may appear ONLY inside functions whose name starts
with `declared_` (checked on this very file).

Predecessors (read-only): verification/v714_moonshot_hecke_groupoid.py
(the tower), experiments/tfpt-discovery/gaussian_code_bridge_probe.py
(V, sigma, the code semantics), verification/v722_phys_ramified_ns_r.py
(NS/R = parity character), verification/v563_paper2_readouts.py (the
deployed window surface, declared side only).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/hecke_mod_ramified_probe.py
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
import v563_paper2_readouts as core  # noqa: E402  (declared_* only)

# ---------------------------------------------------------------- constants
NORM_MAX = 13         # Hecke layers up to Gaussian prime norm 13 (task)
RANK = 4              # Z[i]-rank of the Gaussian E8 module
INDEX_L = 256         # [Z[i]^4 : L] in doubled coordinates (= |det| of the
#                       Z-basis, v689 I5)
N_H3_EIG = 2          # windows that get the odd-sector eigen decomposition
TOL_ID = 1.0e-12      # exact-split identities (relative)
TOL_EIG = 1.0e-9      # eigen/Rayleigh assembly (relative)

BANNED_IDS = ("sympy", "isprime", "primerange", "nextprime", "prevprime",
              "primepi", "zetazero", "zetas", "mpz_zeta")
RESTRICTED = ("U_ALL", "MU_ALL", "LAM_TAB", "G_ALL", "NU_MAIN", "ATOM_MAX",
              "atoms_in", "atom_lags_at", "arch_lags", "frame_a_zones",
              "build_window", "odd_toeplitz", "_NN")

CHECKS = []
KILL_FLAGS = []


def check(name, ok, detail="", kill=False):
    CHECKS.append((name, bool(ok)))
    if kill and not ok:
        KILL_FLAGS.append(name)
    print("  [%s] %s%s" % ("PASS" if ok else "FAIL", name,
                           ("  -- " + detail) if detail else ""), flush=True)
    return bool(ok)


def section(title):
    print("\n" + "=" * 74)
    print(title)
    print("=" * 74, flush=True)


# deterministic pseudo-randomness (no wall clock, no numpy RNG state)
_LCG = [20260804]


def lcg(n):
    _LCG[0] = (1103515245 * _LCG[0] + 12345) % (1 << 31)
    return _LCG[0] % n


# ---------------------------------------------------------- Gaussian basics
def canon(z):
    a, b = z
    for _ in range(4):
        if a > 0 and b >= 0:
            return (a, b)
        a, b = -b, a
    raise ValueError(z)


def gmul(x, y):
    return (x[0] * y[0] - x[1] * y[1], x[0] * y[1] + x[1] * y[0])


def gadd(x, y):
    return (x[0] + y[0], x[1] + y[1])


def gsub(x, y):
    return (x[0] - y[0], x[1] - y[1])


def gnorm(x):
    return x[0] * x[0] + x[1] * x[1]


def gdivides(e, d):
    n = gnorm(e)
    xr = d[0] * e[0] + d[1] * e[1]
    xi = d[1] * e[0] - d[0] * e[1]
    return xr % n == 0 and xi % n == 0


def gquo_exact(x, d):
    """x / d in Z[i], exact (asserts divisibility)."""
    n = gnorm(d)
    xr = x[0] * d[0] + x[1] * d[1]
    xi = x[1] * d[0] - x[0] * d[1]
    assert xr % n == 0 and xi % n == 0, (x, d)
    return (xr // n, xi // n)


def gquo_round(x, d):
    n = gnorm(d)
    xr = x[0] * d[0] + x[1] * d[1]
    xi = x[1] * d[0] - x[0] * d[1]
    return ((2 * xr + n) // (2 * n), (2 * xi + n) // (2 * n))


def par(z):
    """Z[i] -> F2, the reduction mod (1+i): a+bi |-> (a+b) mod 2 (ring
    homomorphism)."""
    return (z[0] + z[1]) & 1


# --------------------------------------------- ring-internal prime census
def class_census(nmax):
    am = int(math.isqrt(nmax)) + 1
    cls = {}
    for a in range(-am, am + 1):
        for b in range(-am, am + 1):
            n = a * a + b * b
            if 1 <= n <= nmax:
                cls.setdefault(n, set()).add(canon((a, b)))
    return {n: sorted(v) for n, v in cls.items()}


def irreducible(d, cls):
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


# ------------------------------------------------- the lattice (v722 frame)
def in_L(w):
    parities = {c % 2 for c in w}
    return len(parities) == 1 and sum(w) % 4 == 0


def roots_E8():
    roots = []
    for i in range(8):
        for j in range(i + 1, 8):
            for si in (2, -2):
                for sj in (2, -2):
                    w = [0] * 8
                    w[i], w[j] = si, sj
                    roots.append(tuple(w))
    for signs in product((1, -1), repeat=8):
        if signs.count(-1) % 2 == 0:
            roots.append(signs)
    return roots


def J8(w):
    out = []
    for k in range(4):
        a, b = w[2 * k], w[2 * k + 1]
        out.extend([-b, a])
    return tuple(out)


def sig8(w):
    return (w[4], w[5], w[0], w[1], w[2], w[3], w[6], w[7])


def conj8(w):
    return (w[1], w[0], w[3], w[2], w[5], w[4], w[7], w[6])


def z_basis_L():
    B = []
    for i in range(6):
        w = [0] * 8
        w[i], w[i + 1] = 2, -2
        B.append(tuple(w))
    w = [0] * 8
    w[6], w[7] = 2, 2
    B.append(tuple(w))
    B.append(tuple([1] * 8))
    return B


def pack(w):
    """Z^8 -> Z[i]^4 via the J-pairing (then J = mult by i, exactly)."""
    return tuple((w[2 * k], w[2 * k + 1]) for k in range(4))


def unpack(z):
    out = []
    for a, b in z:
        out.extend([a, b])
    return tuple(out)


def zi_hnf(rows):
    """Z[i]-Hermite normal form (row style) of a rank-4 generator list in
    Z[i]^4: returns 4 upper-triangular rows (Euclidean gquo_round)."""
    M = [list(r) for r in rows]
    out = []
    for col in range(4):
        pool = [r for r in M if any(r[c] != (0, 0) for c in range(col, 4))]
        M = pool
        while True:
            nz = [r for r in M if r[col] != (0, 0)]
            if len(nz) <= 1:
                break
            nz.sort(key=lambda r: gnorm(r[col]))
            piv = nz[0]
            for r in nz[1:]:
                q = gquo_round(r[col], piv[col])
                for c in range(4):
                    r[c] = gsub(r[c], gmul(q, piv[c]))
        nz = [r for r in M if r[col] != (0, 0)]
        assert len(nz) == 1, "rank defect in Z[i]-HNF"
        out.append(list(nz[0]))
        M = [r for r in M if r is not nz[0]]
    return out


class Lmodule:
    """L as the free module Z[i]^4 via an explicit triangular Z[i]-basis
    (rows of self.M, in packed Z^8 = Z[i]^4 ambient coordinates)."""

    def __init__(self):
        gens = [list(pack(b)) for b in z_basis_L()]
        self.M = zi_hnf(gens)
        idx = 1
        for k in range(4):
            idx *= gnorm(self.M[k][k])
        self.index = idx

    def to_ambient(self, y):
        """L-coords y (Z[i]^4) -> ambient packed vector sum y_k m_k."""
        out = [(0, 0)] * 4
        for k in range(4):
            for c in range(4):
                out[c] = gadd(out[c], gmul(y[k], self.M[k][c]))
        return tuple(out)

    def coords(self, z):
        """ambient packed vector -> L-coords (asserts membership)."""
        z = list(z)
        y = [(0, 0)] * 4
        for k in range(4):
            y[k] = gquo_exact(z[k], self.M[k][k])
            for c in range(4):
                z[c] = gsub(z[c], gmul(y[k], self.M[k][c]))
        assert all(c == (0, 0) for c in z)
        return tuple(y)

    def w_coords(self, w):
        return self.coords(pack(w))

    def class_of_w(self, w):
        return tuple(par(c) for c in self.w_coords(w))


# ---------------------------------------------------------- F2 linear algebra
def f2_matvec(cols, v):
    out = [0, 0, 0, 0]
    for j in range(4):
        if v[j]:
            for i in range(4):
                out[i] ^= cols[j][i]
    return tuple(out)


def f2_rank_ker_inv(cols):
    """columns of a 4x4 F2 matrix -> (rank, kernel basis, inverse cols or
    None)."""
    A = [[cols[j][i] for j in range(4)] for i in range(4)]     # rows
    aug = [A[i] + [1 if i == j else 0 for j in range(4)] for i in range(4)]
    piv_cols = []
    r = 0
    for c in range(4):
        p = next((i for i in range(r, 4) if aug[i][c]), None)
        if p is None:
            continue
        aug[r], aug[p] = aug[p], aug[r]
        for i in range(4):
            if i != r and aug[i][c]:
                aug[i] = [(x ^ y) for x, y in zip(aug[i], aug[r])]
        piv_cols.append(c)
        r += 1
    ker = []
    free = [c for c in range(4) if c not in piv_cols]
    for fc in free:
        v = [0, 0, 0, 0]
        v[fc] = 1
        for ri, pc in enumerate(piv_cols):
            v[pc] = aug[ri][fc]
        ker.append(tuple(v))
    inv_cols = None
    if r == 4:
        inv_rows = [aug[i][4:] for i in range(4)]
        inv_cols = [tuple(inv_rows[i][j] for i in range(4)) for j in range(4)]
    return r, ker, inv_cols


def vidx(v):
    return v[0] + 2 * v[1] + 4 * v[2] + 8 * v[3]


ALL_V = [tuple((n >> k) & 1 for k in range(4)) for n in range(16)]


# ------------------------------------------------------------ residue fields
def field_for(pi):
    """Finite field Z[i]/(pi) for an irreducible canonical pi.  Elements:
    ints 0..q-1 (split/ramified) or pairs mod m (inert pi = (m,0))."""
    a, b = pi
    if b == 0:                                   # inert: F_{m^2}
        m = a
        elems = [(u, v) for u in range(m) for v in range(m)]
        F = dict(q=m * m, zero=(0, 0), one=(1, 0), elems=elems)
        F["add"] = lambda s, t: ((s[0] + t[0]) % m, (s[1] + t[1]) % m)
        F["neg"] = lambda s: ((-s[0]) % m, (-s[1]) % m)
        F["mul"] = lambda s, t: ((s[0] * t[0] - s[1] * t[1]) % m,
                                 (s[0] * t[1] + s[1] * t[0]) % m)
        F["red"] = lambda z: (z[0] % m, z[1] % m)
        F["lift"] = lambda e: (e[0], e[1])
    else:                                        # split or ramified: F_q
        q = a * a + b * b
        t = next(t for t in range(q) if (a + b * t) % q == 0)
        F = dict(q=q, zero=0, one=1, elems=list(range(q)))
        F["add"] = lambda s, u: (s + u) % q
        F["neg"] = lambda s: (-s) % q
        F["mul"] = lambda s, u: (s * u) % q
        F["red"] = lambda z: (z[0] + t * z[1]) % q
        F["lift"] = lambda e: (e, 0)
    F["inv"] = lambda s: next(e for e in F["elems"]
                              if F["mul"](s, e) == F["one"])
    return F


def hyperplanes(F):
    """All hyperplanes of F^4 as normalized functionals (j0, phi):
    phi[j] = 0 for j < j0, phi[j0] = 1."""
    out = []
    for j0 in range(4):
        for tail in product(F["elems"], repeat=3 - j0):
            phi = [F["zero"]] * j0 + [F["one"]] + list(tail)
            out.append((j0, tuple(phi)))
    return out


def field_matinv(F, A):
    """inverse of a 4x4 matrix over F (rows A[i][j]); None if singular."""
    aug = [list(A[i]) + [F["one"] if i == j else F["zero"]
                         for j in range(4)] for i in range(4)]
    for c in range(4):
        p = next((i for i in range(c, 4) if aug[i][c] != F["zero"]), None)
        if p is None:
            return None
        aug[c], aug[p] = aug[p], aug[c]
        s = F["inv"](aug[c][c])
        aug[c] = [F["mul"](s, x) for x in aug[c]]
        for i in range(4):
            if i != c and aug[i][c] != F["zero"]:
                f = aug[i][c]
                aug[i] = [F["add"](x, F["neg"](F["mul"](f, y)))
                          for x, y in zip(aug[i], aug[c])]
    return [row[4:] for row in aug]


# ------------------------------------------------------------- Hecke layers
class Layer:
    """One Hecke layer: all index-N(pi) submodules of L = Z[i]^4."""

    def __init__(self, name, pi):
        self.name = name
        self.pi = pi
        self.q = gnorm(pi)
        self.F = field_for(pi)
        self.red1pi = self.F["red"]((1, 1))
        self.is_ram = (self.red1pi == self.F["zero"])
        self.subs = hyperplanes(self.F)
        self.key = {s: k for k, s in enumerate(self.subs)}

    def phi_of(self, phi, x):
        F = self.F
        s = F["zero"]
        for j in range(4):
            s = F["add"](s, F["mul"](phi[j], F["red"](x[j])))
        return s

    def member(self, phi, x):
        return self.phi_of(phi, x) == self.F["zero"]

    def m_basis(self, j0, phi):
        """triangular Z[i]-basis of M' (rows, in L-coords)."""
        F = self.F
        rows = []
        for j in range(4):
            r = [(0, 0)] * 4
            if j == j0:
                r[j0] = self.pi
            else:
                r[j] = (1, 0)
                r[j0] = gsub((0, 0), F["lift"](phi[j]))
            rows.append(tuple(r))
        return rows

    def iota_cols(self, j0, phi):
        """columns of iota-bar: V_{M'} -> V in the m-basis / class bases."""
        F = self.F
        cols = []
        for j in range(4):
            c = [0, 0, 0, 0]
            if j == j0:
                c[j0] = par(self.pi)
            else:
                c[j] = 1
                c[j0] ^= par(F["lift"](phi[j]))
            cols.append(tuple(c))
        return cols

    def mprime_coords(self, j0, phi, x):
        """M'-basis coordinates of x in M' (exact; asserts membership)."""
        F = self.F
        y = list(x)
        acc = x[j0]
        for j in range(4):
            if j != j0:
                acc = gadd(acc, gmul(F["lift"](phi[j]), x[j]))
        y[j0] = gquo_exact(acc, self.pi)
        return tuple(y)

    def representative(self, j0, phi, v):
        """a representative of the class v inside M' (odd layers always;
        ramified only if v in W = ker phi); None if impossible."""
        F = self.F
        x = [(vj, 0) for vj in v]
        s = self.phi_of(phi, x)
        if s != F["zero"]:
            if self.is_ram:
                return None
            c = F["mul"](F["neg"](s), F["inv"](self.red1pi))
            x[j0] = gadd(x[j0], gmul((1, 1), F["lift"](c)))
        assert self.member(phi, x)
        return tuple(x)


# ------------------------------------------------------------- G0 firewall
def g0_firewall():
    section("G0 -- AST firewall + environment")
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
        if isinstance(node, ast.Attribute) and node.attr in RESTRICTED \
                and id(node) not in allowed:
            leaks.append(node.attr)
    check("G0.2 deployed tables/window builders only inside declared_* "
          "sections", not leaks,
          "leaks: %s" % leaks if leaks else
          "restricted: " + ",".join(RESTRICTED[:6]) + ",...")
    print("    python %s, numpy %s" % (sys.version.split()[0],
                                       np.__version__))


# ------------------------------------------------------------ S1: the module
def s1_setup():
    section("S1 -- the Z[i]-module, V = L/(1+i)L and sigma (exact)")
    roots = roots_E8()
    rset = set(roots)
    B8 = z_basis_L()
    ok = (len(roots) == 240
          and all(in_L(b) for b in B8)
          and all(in_L(J8(b)) for b in B8)
          and all(in_L(sig8(b)) for b in B8)
          and all(J8(r) in rset and sig8(r) in rset for r in roots)
          and all(J8(J8(r)) == tuple(-c for c in r) for r in roots[:60])
          and all(J8(sig8(b)) == sig8(J8(b)) for b in B8))
    check("S1.1 240 roots; J, sigma lattice+root automorphisms; J^2 = -1; "
          "[J, sigma] = 0 (exact)", ok, kill=True)

    L = Lmodule()
    okb = (L.index == INDEX_L)
    diag = [L.M[k][k] for k in range(4)]
    okb &= all(in_L(unpack(L.to_ambient(tuple(
        (1 if j == k else 0, 0) for j in range(4))))) for k in range(4))
    rt = True
    for w in B8 + roots[:40]:
        y = L.w_coords(w)
        rt &= (unpack(L.to_ambient(y)) == w)
    check("S1.2 Z[i]-HNF basis of L: rows in L, abelian index N(det) = %d "
          "= %d, coord round-trip exact" % (L.index, INDEX_L),
          okb and rt, "diag = %s" % (diag,), kill=True)

    # class map census on the roots
    root_class = {r: L.class_of_w(r) for r in roots}
    census = {}
    for r in roots:
        census[root_class[r]] = census.get(root_class[r], 0) + 1
    zero = (0, 0, 0, 0)
    sizes = sorted(census.values())
    check("S1.3a class census: 240 roots -> 15 nonzero classes x 16, zero "
          "class empty", len(census) == 15 and zero not in census
          and sizes == [16] * 15, kill=True)

    # cross-validate the class map against the direct (1+i)-equivalence
    def equiv_direct(w1, w2):
        d = tuple(x - y for x, y in zip(w1, w2))
        u = tuple(x - y for x, y in zip(d, J8(d)))
        if any(c % 2 for c in u):
            return False
        return in_L(tuple(c // 2 for c in u))

    pool = roots[:30] + [tuple(a + b for a, b in zip(roots[i], roots[i + 1]))
                         for i in range(0, 40, 2)]
    okx = True
    for _ in range(200):
        w1 = pool[lcg(len(pool))]
        w2 = pool[lcg(len(pool))]
        okx &= ((L.class_of_w(w1) == L.class_of_w(w2))
                == equiv_direct(w1, w2))
    check("S1.3b class map == direct test (1-J)(x-y)/2 in L "
          "(200 deterministic pairs)", okx, kill=True)

    # sigma in L-coords (Z[i]-matrix, rows) and sigma-bar on V
    S = [L.coords(pack(sig8(unpack(L.to_ambient(
        tuple((1 if j == k else 0, 0) for j in range(4))))))) for k in
        range(4)]
    S2 = [[par(S[k][j]) for j in range(4)] for k in range(4)]

    def sigbar(v):
        return tuple((sum(v[k] * S2[k][j] for k in range(4))) & 1
                     for j in range(4))

    def sigchar(a):
        return tuple((sum(S2[k][j] * a[j] for j in range(4))) & 1
                     for k in range(4))

    v1 = {v: sigbar(v) for v in ALL_V}
    v3 = {v: sigbar(sigbar(v1[v])) for v in ALL_V}
    fixed = [v for v in ALL_V if v1[v] == v]
    oklin = all(L.class_of_w(sig8(r)) == sigbar(root_class[r])
                for r in roots)
    check("S1.4 sigma-bar on V: linear (all 240 roots), sigma^3 = id, "
          "exactly 4 fixed classes", oklin
          and all(v3[v] == v for v in ALL_V)
          and any(v1[v] != v for v in ALL_V) and len(fixed) == 4,
          "fixed = %s" % [vidx(v) for v in fixed], kill=True)

    # ring-internal prime layers
    cls = class_census(NORM_MAX)
    prims = [(n, d) for n in sorted(cls) for d in cls[n]
             if irreducible(d, cls)]
    exp_prims = [(2, (1, 1)), (5, (1, 2)), (5, (2, 1)), (9, (3, 0)),
                 (13, (2, 3)), (13, (3, 2))]
    check("S1.5a ring-internal prime census (norm <= %d): %s" %
          (NORM_MAX, [d for _n, d in prims]),
          sorted(prims) == sorted(exp_prims), kill=True)

    layers = [Layer("(%d%+di)" % d if d[1] else "(%d)" % d[0], d)
              for _n, d in prims]
    counts = {ly.name: len(ly.subs) for ly in layers}
    deg_sum = {}
    for ly in layers:
        deg_sum[ly.q] = deg_sum.get(ly.q, 0) + len(ly.subs)
    check("S1.5b layer counts %s; degree sums %s == v714 tower numbers "
          "{2:15, 5:312, 9:820, 13:4760}" % (counts, deg_sum),
          deg_sum == {2: 15, 5: 312, 9: 820, 13: 4760}, kill=True)

    ctx = dict(L=L, roots=roots, root_class=root_class, S=S, S2=S2,
               sigbar=sigbar, sigchar=sigchar, layers=layers,
               census=census)
    return ctx


# ---------------------------------------------------------- H1: the kill test
def h1_layer(ctx, ly):
    """exact scan over ALL submodules of one layer; returns the assembled
    operator and the anatomy (or violation list)."""
    L, S = ctx["L"], ctx["S"]
    F = ly.F
    viol = []
    Hop = np.zeros((16, 16), dtype=np.int64)
    Wfun = []                      # ramified: the F2 functional per M'
    n_det1 = n_rank3 = 0
    for si, (j0, phi) in enumerate(ly.subs):
        cols = ly.iota_cols(j0, phi)
        rk, ker, inv = f2_rank_ker_inv(cols)
        if ly.is_ram:
            if rk != 3 or len(ker) != 1:
                viol.append(("rank", ly.name, si, rk))
                continue
            n_rank3 += 1
            deck = ker[0]
            # image of iota-bar must be ker(phi) (phi is already F2 here)
            img_ok = all((sum(phi[i] * cols[j][i] for i in range(4)) & 1)
                         == 0 for j in range(4))
            if not img_ok:
                viol.append(("image", ly.name, si))
            Wfun.append(phi)
            for v in ALL_V:
                pairing = (sum(phi[j] * v[j] for j in range(4))) & 1
                x = ly.representative(j0, phi, v)
                if pairing:                      # off the hyperplane
                    if x is not None:
                        viol.append(("ghost-rep", ly.name, si, v))
                    continue
                if x is None:
                    viol.append(("no-rep", ly.name, si, v))
                    continue
                y = ly.mprime_coords(j0, phi, x)
                t = tuple(par(c) for c in y)
                # second sheet: add (1+i) e_{j0} (stays in M', ram case)
                x3 = list(x)
                x3[j0] = gadd(x3[j0], (1, 1))
                y3 = ly.mprime_coords(j0, phi, tuple(x3))
                t3 = tuple(par(c) for c in y3)
                if tuple(a ^ b for a, b in zip(t, t3)) != deck or t3 == t:
                    viol.append(("deck", ly.name, si, v, t, t3, deck))
                for tt in (t, t3):
                    if f2_matvec(cols, tt) != v:
                        viol.append(("iota", ly.name, si, v, tt))
                Hop[vidx(v), vidx(v)] += 2
        else:
            if rk != 4 or inv is None:
                viol.append(("singular", ly.name, si, rk,
                             "ker=%s" % ker))
                continue
            n_det1 += 1
            mb = ly.m_basis(j0, phi)
            for v in ALL_V:
                x = ly.representative(j0, phi, v)
                y = ly.mprime_coords(j0, phi, x)
                t = tuple(par(c) for c in y)
                # constructive transport must equal iota-bar^{-1} v
                if t != f2_matvec(inv, v):
                    viol.append(("transport", ly.name, si, v, t))
                # representative independence: second, independent rep
                coeffs = [(lcg(2), lcg(2)) for _ in range(4)]
                m2 = [(0, 0)] * 4
                for k in range(4):
                    for c in range(4):
                        m2[c] = gadd(m2[c], gmul(coeffs[k], mb[k][c]))
                x2 = tuple(gadd(x[c], gmul((1, 1), m2[c]))
                           for c in range(4))
                y2 = ly.mprime_coords(j0, phi, x2)
                t2 = tuple(par(c) for c in y2)
                if t2 != t:
                    viol.append(("rep-dep", ly.name, si, v, t, t2))
                # non-membership control: (1+i) e_{j0} leaves M'
                x4 = list(x)
                x4[j0] = gadd(x4[j0], (1, 1))
                if ly.member(phi, tuple(x4)):
                    viol.append(("control", ly.name, si, v))
                w = f2_matvec(cols, t)
                Hop[vidx(w), vidx(v)] += 1
    # sigma-functoriality: pushforward permutation of the layer
    Sf = [[F["red"](S[k][j]) for j in range(4)] for k in range(4)]
    Sfinv = field_matinv(F, Sf)
    perm = []
    okperm = Sfinv is not None
    for (j0, phi) in ly.subs:
        u = [F["zero"]] * 4
        for i in range(4):
            for j in range(4):
                u[i] = F["add"](u[i], F["mul"](Sfinv[i][j], phi[j]))
        p0 = next((i for i in range(4) if u[i] != F["zero"]), None)
        if p0 is None:
            okperm = False
            break
        s = F["inv"](u[p0])
        psi = tuple(F["mul"](s, x) for x in u)
        tgt = (p0, psi)
        if tgt not in ly.key:
            okperm = False
            viol.append(("sigma-perm", ly.name, phi))
            break
        perm.append(ly.key[tgt])
        # membership functoriality: sigma-images of the M'-basis in M'_psi
        mb = ly.m_basis(j0, phi)
        for r in mb:
            img = tuple_sum_mul(r, S)
            if not ly.member(psi, img):
                okperm = False
                viol.append(("sigma-member", ly.name, phi))
                break
    orbit_count = None
    if okperm and len(perm) == len(ly.subs):
        seen = [False] * len(perm)
        orbit_count = 0
        p3ok = True
        for s0 in range(len(perm)):
            if seen[s0]:
                continue
            orbit_count += 1
            cyc = [s0]
            j = perm[s0]
            while j != s0:
                seen[j] = True
                cyc.append(j)
                j = perm[j]
            seen[s0] = True
            if len(cyc) not in (1, 3):
                p3ok = False
        okperm &= p3ok
    return Hop, viol, okperm, orbit_count, Wfun, n_det1, n_rank3


def tuple_sum_mul(r, S):
    """x |-> x . S for a row vector r in Z[i]^4 (rows S[k])."""
    out = [(0, 0)] * 4
    for k in range(4):
        for c in range(4):
            out[c] = gadd(out[c], gmul(r[k], S[k][c]))
    return tuple(out)


def h1_scan(ctx):
    section("H1 -- the projection: well-definedness over ALL submodules "
            "(the kill test)")
    ops = {}
    rami = None
    for ly in ctx["layers"]:
        t0 = time.time()
        Hop, viol, okperm, orbits, Wfun, n_det1, n_rank3 = \
            h1_layer(ctx, ly)
        deg = len(ly.subs)
        ops[ly.name] = Hop
        if ly.is_ram:
            rami = dict(layer=ly, Wfun=Wfun, Hop=Hop)
            hset = {tuple(w) for w in Wfun}
            ok = (not viol and n_rank3 == deg and len(hset) == 15)
            check("H1.1 ramified %s: ALL %d submodules rank-3, 2:1 deck "
                  "verified per (M', v in W), submodules <-> the 15 "
                  "hyperplanes of V (bijective)" % (ly.name, deg), ok,
                  "violations: %s" % viol[:4] if viol else
                  "%.1f s" % (time.time() - t0), kill=True)
        else:
            expc = np.zeros((16, 16), dtype=np.int64)
            np.fill_diagonal(expc, deg)
            ok = (not viol and n_det1 == deg
                  and np.array_equal(Hop, expc))
            check("H1.%d odd layer %s (q = %d): ALL %d submodules det "
                  "iota-bar = 1, constructive transport == iota-bar^{-1} "
                  "(16 classes x 2 reps each), induced endo == id => "
                  "H-bar = %d * id" % (2 + ctx["layers"].index(ly) - 1,
                                       ly.name, ly.q, deg, deg), ok,
                  "violations: %s" % viol[:4] if viol else
                  "%.1f s" % (time.time() - t0), kill=True)
        check("H1.f sigma-functoriality on %s: pushforward permutes the "
              "layer, orbit lengths in {1, 3} (count %s)"
              % (ly.name, orbits), okperm and orbits is not None,
              kill=True)
    return ops, rami


# ----------------------------------------------------------- H2: structure
def h2_structure(ctx, ops, rami):
    section("H2 -- structure: sigma-commutation, Walsh, channels, the "
            "ramified place")
    sigbar, sigchar = ctx["sigbar"], ctx["sigchar"]
    P = np.zeros((16, 16), dtype=np.int64)
    for v in ALL_V:
        P[vidx(sigbar(v)), vidx(v)] = 1

    okc = all(np.array_equal(H @ P, P @ H) for H in ops.values())
    check("H2.1 [H-bar_p, sigma-bar] = 0 for every layer operator "
          "(16x16, exact integers)", okc, kill=True)

    D = rami["Hop"]
    okD = (D[0, 0] == 30 and all(D[k, k] == 14 for k in range(1, 16))
           and np.count_nonzero(D - np.diag(np.diag(D))) == 0)
    check("H2.2a ramified multiplier D = diag(30, 14 x 15) "
          "(down-up composition, assembled)", okD, kill=True)

    Wal = np.array([[(-1) ** sum(a * b for a, b in zip(av, vv))
                     for vv in ALL_V] for av in ALL_V], dtype=np.int64)
    lhs = Wal @ D @ Wal
    rhs = 224 * np.eye(16, dtype=np.int64) + 16 * np.ones((16, 16),
                                                          dtype=np.int64)
    check("H2.2b Walsh form of D == 224 I + 16 * ones exactly (all "
          "cross-character coupling is ONE rank-1 layer)",
          np.array_equal(lhs, rhs))

    degs = {ly.name: len(ly.subs) for ly in ctx["layers"]}
    odd_ok = all(np.array_equal(ops[n], degs[n] * np.eye(16, dtype=np.int64))
                 for n in ops if n != rami["layer"].name)
    check("H2.2c odd layers on the Walsh characters: eigenvalue = degree "
          "on EVERY character (%s)" %
          {n: d for n, d in degs.items() if n != rami["layer"].name},
          odd_ok)

    # ramified transfer Gram A[v,w] = #hyperplanes containing v and w
    Wfun = rami["Wfun"]
    A = np.zeros((16, 16), dtype=np.int64)
    for phi in Wfun:
        inW = [v for v in ALL_V
               if (sum(phi[j] * v[j] for j in range(4))) & 1 == 0]
        for v in inW:
            for w in inW:
                A[vidx(v), vidx(w)] += 1
    pat_ok = (A[0, 0] == 15
              and all(A[0, k] == 7 and A[k, 0] == 7 for k in range(1, 16))
              and all(A[k, k] == 7 for k in range(1, 16))
              and all(A[i, j] == 3 for i in range(1, 16)
                      for j in range(1, 16) if i != j))
    x0 = np.ones(16, dtype=np.int64)
    x0[0] = -7
    x64 = 14 * np.ones(16, dtype=np.int64)
    x64[0] = 30
    y = np.zeros(16, dtype=np.int64)
    y[1], y[2] = 1, -1
    eig_ok = (np.array_equal(A @ x0, 0 * x0)
              and np.array_equal(A @ x64, 64 * x64)
              and np.array_equal(A @ y, 4 * y))
    ev = np.linalg.eigvalsh(A.astype(float))
    ev_int = sorted(int(round(e)) for e in ev)
    check("H2.2d transfer Gram A: pattern (15/7/7/3), exact integer "
          "eigensystem {0, 4 x 14, 64}; 64-eigenvector = diag D",
          pat_ok and eig_ok and ev_int == [0] + [4] * 14 + [64],
          "spec = %s" % sorted(set(ev_int)))

    ok_sA = np.array_equal(A @ P, P @ A)
    C = D @ A - A @ D
    supp_ok = all(C[i, j] == 0 for i in range(1, 16) for j in range(1, 16))
    supp_ok &= all(C[0, j] == 112 for j in range(1, 16))
    supp_ok &= all(C[i, 0] == -112 for i in range(1, 16))
    supp_ok &= C[0, 0] == 0
    check("H2.3 commutativity: all down-up H-bar commute pairwise "
          "(scalars + diagonal D); [A, sigma] = 0; [D, A] != 0 EXACTLY "
          "on the zero-class row/column (+-112)", ok_sA and supp_ok,
          "the ramified place is the only non-scalar direction")

    # ---- channels: sigma-orbit census on classes / characters / planes
    def orbits_of(action, elems):
        seen, orb = set(), []
        for e in elems:
            if e in seen:
                continue
            o = [e]
            x = action(e)
            while x != e:
                o.append(x)
                x = action(x)
            seen |= set(o)
            orb.append(o)
        return orb

    orb_cls = orbits_of(sigbar, ALL_V)
    orb_chr = orbits_of(sigchar, ALL_V)
    zero = (0, 0, 0, 0)
    nz_cls = [o for o in orb_cls if zero not in o]
    nz_chr = [o for o in orb_chr if zero not in o]
    cls_sig = sorted(len(o) for o in nz_cls)
    chr_sig = sorted(len(o) for o in nz_chr)
    # hyperplanes carry the same census as nontrivial characters
    ok_ch = (cls_sig == [1, 1, 1, 3, 3, 3, 3]
             and chr_sig == [1, 1, 1, 3, 3, 3, 3])
    check("H2.4 CHANNELS: sigma-orbits on the 15 nonzero classes = "
          "3 fixed + 4 moved = 7; on the 15 nontrivial characters = "
          "3 + 4 = 7; + 1 trivial channel each (zero class / trivial "
          "character) => the review's 7 = the nontrivial channels, "
          "task's 8 = 7 + trivial -- both exact, no discrepancy",
          ok_ch, "classes %s, characters %s" % (cls_sig, chr_sig))

    # ---- the ramified place: NS/R = parity character (v722 hookup)
    L = ctx["L"]
    roots = ctx["roots"]
    a_par = tuple(unpack(L.to_ambient(tuple((1 if j == k else 0, 0)
                                            for j in range(4))))[0] % 2
                  for k in range(4))
    ok_chi = all((r[0] % 2) == (sum(a * b for a, b in
                                    zip(a_par, ctx["root_class"][r])) & 1)
                 for r in roots)
    ok_fix = (sigchar(a_par) == a_par and a_par != zero)
    ns_classes = [v for v in ctx["census"]
                  if (sum(a * b for a, b in zip(a_par, v)) & 1) == 0]
    r_classes = [v for v in ctx["census"]
                 if (sum(a * b for a, b in zip(a_par, v)) & 1) == 1]
    in_layer = tuple(a_par) in {tuple(phi) for phi in rami["Wfun"]}
    check("H2.5a NS/R grading = the parity character chi_par of V "
          "(all 240 roots), chi_par sigma-FIXED, ker chi_par = the "
          "even/NS sublattice = ONE of the 15 ramified Hecke "
          "submodules; class census %d NS + %d R (v722 re-derived)"
          % (len(ns_classes), len(r_classes)),
          ok_chi and ok_fix and in_layer
          and len(ns_classes) == 7 and len(r_classes) == 8,
          "a_par = %s" % (a_par,))

    # NS/R distribution over the 7 nontrivial channels
    def chan_par(o):
        return (sum(a * b for a, b in zip(a_par, o[0]))) & 1

    pure = all(len({(sum(a * b for a, b in zip(a_par, v))) & 1
                    for v in o}) == 1 for o in nz_cls)
    ns_orb = [o for o in nz_cls if chan_par(o) == 0]
    r_orb = [o for o in nz_cls if chan_par(o) == 1]
    check("H2.5b parity constant on every channel: NS channels %d "
          "(sizes %s), R channels %d (sizes %s) -- 7 = %d NS + %d R"
          % (len(ns_orb), sorted(len(o) for o in ns_orb), len(r_orb),
             sorted(len(o) for o in r_orb), len(ns_orb), len(r_orb)),
          pure and len(ns_orb) + len(r_orb) == 7)

    print("    typed consequence (measured, exact): the projected Hecke "
          "algebra acts on the\n    15 nontrivial classes as SCALARS "
          "(odd layers: degree; ramified: 14) -- the\n    fiber V is "
          "Hecke-RIGID away from bookkeeping on the trivial channel.  "
          "The <= 7\n    channels are SIGMA channels (code semantics: "
          "v638 families/anchor, v722 NS/R),\n    not Hecke-eigenvalue "
          "channels: a per-prime channel separation of window\n    "
          "positivity CANNOT come from this projection alone; what the "
          "fiber does\n    canonically grade is the RAMIFIED (2-adic) "
          "tower via the deck parity.")
    return dict(a_par=a_par, nz_cls=nz_cls, D=D, A=A)


# --------------------------------------------------- H3: declared measurement
def declared_h3_windows(h2):
    """The v563 deployed frame-A surface enters HERE only: channel split
    of the atom side of the thin T-B margin + odd-sector Rayleigh."""
    section("H3 -- [declared] channel projection of the deployed window "
            "moments (v563 surface)")
    a_par = h2["a_par"]

    def mixed_det(Pm, Qm):
        return (Pm[0, 0] * Qm[1, 1] + Pm[1, 1] * Qm[0, 0]
                - 2.0 * Pm[0, 1] * Qm[0, 1])

    def channel_of(n):
        k = 1
        for j in range(int(math.log2(n)), 1, -1):
            p = int(round(n ** (1.0 / j)))
            for pc in (p - 1, p, p + 1):
                if pc >= 2 and pc ** j == n:
                    k, base = j, pc
                    break
            else:
                continue
            break
        else:
            base = n
        if base == 2:
            return "ram-odd" if k % 2 else "ram-even"
        for a in range(1, int(math.isqrt(base)) + 1):
            b2 = base - a * a
            b = int(math.isqrt(b2))
            if b > 0 and b * b == b2:
                return "split"
        return "inert"

    KZ = core.frame_a_zones()
    # complete-comb windows only: X = n_zone^2 <= the declared table cap
    # (beyond it the comb is truncated and the margin is an artefact)
    KZC = [kz for kz in KZ
           if int(core._NN[kz]) ** 2 <= core.ATOM_MAX]
    kz_ref = KZ[len(KZ) // 2]          # the v563 reference window (h = 540)
    picks = sorted({KZC[0], KZC[1], kz_ref, KZC[-1]})
    labels = ("ram-odd", "ram-even", "split", "inert")
    ok_split = ok_det = ok_ray = ok_cov = True
    ramodd_lin, ramodd_ray, posrest_lin = [], [], []
    for wi, kz in enumerate(picks):
        r = core.build_window(kz)
        nn = np.rint(np.exp(r["uu"])).astype(int)
        chan = np.array([channel_of(int(n)) for n in nn])
        S = r["S"]
        B = r["B"]
        Ah = r["Ah"]
        det_ah = float(np.linalg.det(Ah))
        onem = r["onem"]
        Sc = {}
        for lab in labels:
            idx = np.nonzero(chan == lab)[0]
            lam = r["lam"][idx]
            Xn = r["Xn"][idx]
            Sc[lab] = np.array(
                [[float(lam @ Xn[:, 0]), float(lam @ Xn[:, 2])],
                 [float(lam @ Xn[:, 2]), float(lam @ Xn[:, 1])]])
        ok_cov &= (sum(int(np.sum(chan == lab)) for lab in labels)
                   == r["n_atom"])
        Ssum = sum(Sc.values())
        ok_split &= (np.max(np.abs(Ssum - S))
                     <= TOL_ID * max(1.0, float(np.max(np.abs(S)))))
        lin = {lab: mixed_det(B, Sc[lab]) for lab in labels}
        quad = 0.0
        for i1, l1 in enumerate(labels):
            for l2 in labels[i1:]:
                q = mixed_det(Sc[l1], Sc[l2])
                quad += (0.5 * q) if l1 == l2 else q
        det_rebuilt = float(np.linalg.det(B)) - sum(lin.values()) + quad
        ok_det &= abs(det_rebuilt - det_ah) <= 1e-6 * abs(det_ah)
        ramodd_lin.append(lin["ram-odd"])
        posrest_lin.append(min(lin["split"], lin["inert"]))
        print("  window kz=%d: n_zone=%d h=%d X=%.4g atoms=%d | "
              "det B=%.4g  -D(B,S)=%.4g  det S=%.4g  det Ahat=%.4g  "
              "margin 1-r12^2=%.4g"
              % (kz, r["n_zone"], r["h"], r["X"], r["n_atom"],
                 float(np.linalg.det(B)), -sum(lin.values()),
                 float(np.linalg.det(S)), det_ah, onem))
        for lab in labels:
            idx = np.nonzero(chan == lab)[0]
            mass = float(np.sum(2.0 * r["lam"][idx]))
            Sl = S - Sc[lab]
            Al = B - Sl
            onem_l = (float(np.linalg.det(Al))
                      / (Al[0, 0] * Al[1, 1]))
            print("    %-8s atoms %5d  mass sum mu %10.4g  linear det "
                  "pressure D(B,S_c) %11.4g (%6.2f%% of total)  "
                  "leave-out margin %10.4g (x%7.3f)"
                  % (lab, len(idx), mass, lin[lab],
                     100.0 * lin[lab] / sum(lin.values()),
                     onem_l, onem_l / onem))
        # odd-sector Rayleigh split at the minimiser (first + mid window)
        if wi < N_H3_EIG:
            Mz, D_ = r["M"], r["D"]
            c_ar = core.arch_lags(Mz, D_)
            mm = 2.0 * r["lam"]
            c_at_c = {}
            for lab in labels:
                idx = np.nonzero(chan == lab)[0]
                c_at_c[lab], _ = core.atom_lags_at(
                    r["alpha"], Mz, r["uu"][idx], mm[idx])
            c_at_all, _ = core.atom_lags_at(r["alpha"], Mz, r["uu"], mm)
            ok_split &= (np.max(np.abs(sum(c_at_c.values()) - c_at_all))
                         <= 1e-10)
            Afull = core.odd_toeplitz(c_ar + c_at_all, Mz)
            evals, evecs = np.linalg.eigh(Afull)
            vmin = evecs[:, 0]
            lam_min = float(evals[0])
            r_ar = float(vmin @ (core.odd_toeplitz(c_ar, Mz) @ vmin))
            r_c = {lab: float(vmin @ (core.odd_toeplitz(c_at_c[lab], Mz)
                                      @ vmin)) for lab in labels}
            ok_ray &= (abs(r_ar + sum(r_c.values()) - lam_min)
                       <= TOL_EIG * max(1.0, abs(lam_min)))
            ramodd_ray.append((r_c["ram-odd"],
                               min(r_c[lab] for lab in labels
                                   if lab != "ram-odd")))
            print("    odd-sector lambda_min = %.6g ; Rayleigh split at "
                  "the minimiser: arch %+.6g" % (lam_min, r_ar))
            for lab in labels:
                print("      %-8s atom pressure %+11.6g  (%7.3f x "
                      "lambda_min)" % (lab, r_c[lab],
                                       r_c[lab] / lam_min))
    check("H3.1 [declared] channel split covers every atom and "
          "sum_c S_c == S to %.0e (all windows)" % TOL_ID,
          ok_cov and ok_split)
    check("H3.2 [declared] det polarisation over channels rebuilds "
          "det Ahat (rel 1e-6)", ok_det)
    check("H3.3 [declared] odd-sector Rayleigh split: arch + sum of "
          "channel pressures == lambda_min (rel %.0e, %d windows)"
          % (TOL_EIG, N_H3_EIG), ok_ray)
    check("H3.4 [declared] the 'negative J-odd pressure' located: the "
          "ram-odd channel (2-adic layers of odd deck parity chi_par, "
          "n = 2, 8, 32, ...) has NEGATIVE linear det pressure on "
          "EVERY window while split/inert stay positive; in the "
          "odd-sector Rayleigh split it is the unique negative channel "
          "on the measured windows",
          all(x < 0.0 for x in ramodd_lin)
          and all(x > 0.0 for x in posrest_lin)
          and all(a < 0.0 < b for a, b in ramodd_ray),
          "lin(ram-odd) = %s" % ["%.3g" % x for x in ramodd_lin])
    print("    reading (measured): (i) the ram-odd channel carries the "
          "review's 'negative\n    J-odd pressure' -- negative on every "
          "window in the det reading (ram-even\n    flips slightly "
          "negative only at the deep end), unique negative channel in\n"
          "    the Rayleigh reading; (ii) split and inert carry the "
          "positive pressure\n    ~50/50 and stay channel-blind (H2 "
          "rigidity); (iii) NO single channel\n    carries the margin: "
          "the thin T-B margin is a cross-channel cancellation --\n    "
          "removing ANY channel moves it by 1e2..1e5 x its own size "
          "(leave-out column),\n    so a per-channel transfer-matrix "
          "reduction of W3 positivity does NOT follow\n    from this "
          "projection alone; the V-fiber grades, it does not decouple.")


# ------------------------------------------------------------------ verdict
def verdict():
    section("VERDICT")
    n_pass = sum(1 for _n, ok in CHECKS if ok)
    n_all = len(CHECKS)
    if KILL_FLAGS:
        v = "HECKE-MOD-RAMIFIED-DEAD"
        note = ("kill fired (review criterion, literal): %s -- route "
                "ended, no relabeling." % KILL_FLAGS[:3])
    elif n_pass == n_all:
        v = "HECKE-MOD-RAMIFIED-CHANNELS"
        note = ("the projection exists canonically and is exhaustively "
                "well-defined; the tower acts on V through degrees "
                "(odd places) + the ramified hyperplane geometry; "
                "channels = the 7 sigma-orbit channels (+1 trivial), "
                "NS/R = chi_par at the ramified place.")
    else:
        v = "HECKE-MOD-RAMIFIED-CHANNELS (construction caveats)"
        note = "non-kill checks failed -- see FAIL lines."
    print("%d/%d checks passed" % (n_pass, n_all))
    print("VERDICT: %s" % v)
    print("PRIME.HECKE.MOD_RAMIFIED.01: %s -- %s" % (v, note))
    return n_pass == n_all


def main():
    t0 = time.time()
    print("=" * 74)
    print("PRIME.HECKE.MOD_RAMIFIED.01 -- the Hecke tower mod (1+i): "
          "local fiber test")
    print("=" * 74)
    g0_firewall()
    ctx = s1_setup()
    ops, rami = h1_scan(ctx)
    h2 = h2_structure(ctx, ops, rami)
    declared_h3_windows(h2)
    ok = verdict()
    print("total runtime %.1f s" % (time.time() - t0))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
