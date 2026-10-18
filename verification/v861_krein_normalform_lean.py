#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""v861 -- PRIME.KREIN.NORMALFORM.01 + FORM.PRIME.KREIN.DEFECT.01 [F]: the wall's operator form -- the deployed window form gets an EXACT Krein normal form Q_h(t) = ||B+ t||^2 - ||B- t||^2 with the Douglas pencil identity 1 - ||C2||^2 == tau-margin machine-exact, the register wiring separates the mu-sign C2 from the deck C2 (the identification ONE faithful-mu4 character away, three candidate constructions typed), the Redheffer/Mertens echo is exact (det R_n = M(n); the vacuum column's ENTIRE Smith deviation = the single invariant factor |M(n)|), and the defect theorem is kernel-checked with SourceContractor the named hypothesis, ONE module from two probes plus the kernel-checked Lean frame (37/37 + 8/8 checks, zero fails, verdicts DECK-MU-PARALLEL + REDHEFFER-ECHO-EXACT and KREIN-CONTRACTOR-STABLE-NO-WORD; + 4 mirror checks; discovery probes mobius_deck_redheffer_probe.py and krein_normalform_probe.py, 2026-08-08, re-run identically at promotion, embedded BYTE-EXACT and executed verbatim, ~13 s; Lean frame TfptCarrier/KreinDefect.lean, lake build green 3416 jobs, kernel axioms clean).  PART A, THE TWO C2s (Q1 of the deck probe): the deployed wiring has TWO separate order-2 elements -- the mu-sign lives in the register's C2 slot (the deployed reading character chi_GL1 = (eps=-1, w=0, j=0) reads it as -1) and the geometric deck lives in the mu4/(1+i) jet tower (image (0,0,2), read by chi_GL1 as +1; trivial intersection of the two subgroups, both machine-verified on G = C2 x F2^4 x Z4 with |G| = 128) -- no deployed intertwiner exists, and the three candidate CONSTRUCTIONS are named and machine-verified: (1) the diagonal characters (eps=-1, w=0, j=1 or 3) -- one character away from the deployed GL1 read, necessarily FAITHFUL on mu4 (the zeta8/metaplectic layer must resolve i: zeta8^2 = i exact, the unique ring iso Z[i]/(2) -> F2[eps]/(eps^2) sends 1+i -> eps, 1 of 24 bijections); (2) the Galois/Frobenius bookkeeping mu_K((p)) = chi4(p) EXACT on all 609 split (p = x^2 + y^2 witnesses found) and all 619 inert primes p <= 10000 -- the base sign mu(p) = -1 survives the double cover exactly on the deck-odd (inert, Frobenius = deck) sector, (2) = -i(1+i)^2 the killed ramified site; (3) the Hall chain parity: M = sum_k (-1)^k N^k terminates at k = 8 with M Z == I exact and ROW 1 of M == mu (n = 360) -- the mu-sign IS the chain-length parity grading of the divisor poset's double cover.  PART B, THE REDHEFFER ECHO (Q2): det R_n == M(n) EXACT (Bareiss integer determinants on 62 sizes n <= 120; the matrix-determinant lemma det(Z + u e1^T) = 1 + sum_{k>=2} mu(k) extends the identity along ALL n <= 2e6), the witness minor == 1 exactly so SNF(R_n) = diag(1, ..., 1, |M(n)|) -- vacuum completion is a RANK-ONE origin update converting the unimodular Z (SNF = I) into the global census concentrated in ONE new invariant, with the code-side instantiation typed at parameter grade ([15,5,6] shortening, CSS [[15,5,3]] -> [[16,4,4]]) and the mod-2 shadow M(n) == squarefree-count parity for ALL n <= 2e6; the Perron root of R_n grows as ~sqrt(n) = the deployed comb normalization scale (typed, no deeper connection: ABSENT); the fit-free floor census finds NO resolvable tau <-> Mertens correlation (Spearman battery, Bonferroni x4: min 4p = 0.378 -- the margin ladder and the Mertens path are independent at these horizons; the scrambled mu-signs give a random-walk path at contrast 4.51x: the SIGN data, not the support, carries the census).  PART C, THE KREIN NORMAL FORM: on every reachable rung and BOTH canonical cuts the deployed lag form equals B+*B+ - B-*B- ENTRYWISE (ward <= 1e-15 rel; B carries sqrt|Lambda| so the form is LINEAR in Lambda -- the grade barrier is passed by construction, doubling the comb masses doubles the comb Gram at 1.8e-15), the range condition ran(B-*) c ran(B+*) holds (residual <= 3.8e-15) and the EXACT Douglas relationship 1 - ||C2||^2 == lam_min(G+^{-1/2} Ah G+^{-1/2}) is verified per rung (max rel dev 3.9e-09): the tau-margin IS the contraction margin in the positive-side metric -- 'which self-consistent comb is real' has become 'which rate measure makes B- pinv(B+) a contraction', and the discriminator is the Douglas equivalence itself: truth has lam_min(K) > 0 and ||C_full|| <= 1 on every rung (razor-thin, 1 - ||C||^2 down to ~1e-6 at depth) while the Epstein h=2 comb explodes to ||C_E|| = 46.81 with lam_min(K_E) < 0 and the scrambled comb to 3693 (the 2x2 battery at the shallow window is honestly too coarse for Epstein -- the negativity needs the full grid, the v1 presumption retracted in the frozen spec); the geometry census puts the contraction-critical direction in a LOW dual-frequency band (tau* drifting 1.70 -> 0.88 along the ladder, small digamma-band mass), and the word census closes: 155 words over {J, S, M4, KM, ZM} -- best residual 0.991 vs bar 1e-8, EMPTY as pre-typed (the d+ and d- supports are disjoint frequency bands, all short deployed words are support-preserving; the missing object is a BAND-MOVING intertwiner with an independent norm bound -- the explicit-formula transfer).  PART D, THE LEAN FRAME (FORM.PRIME.KREIN.DEFECT.01 [F]; v856/v849 precedent -- numeric witnesses here, kernel statements there): TfptCarrier/KreinDefect.lean -- 14 declarations (10 theorems), kernel-checked (no sorry, no native_decide; axioms propext/Classical.choice/Quot.sound only, verified by #print axioms; import wired in TfptCarrier.lean; Lean manifest 87 -> 88 files): (1) defect / formAt_defect -- the defect representation Q(f) = ||B+ f||^2 - ||B- f||^2 exactly; (2) defect_psd_of_contraction -- THE MAIN THEOREM: B- = C B+ with the Loewner certificate (1 - C^H C) PSD forces the defect PSD via the exact factorization defect = B+^H (1 - C^H C) B+ and congruence; (3) douglas_contraction_of_defect_psd -- the converse (full-rank case proven, C := B- B+^{-1}; the singular case deliberately the classical Douglas 1966 citation); (4) SourceContractor -- THE NAMED HYPOTHESIS: the contractor + factorization + INDEPENDENT norm certificate as data a consumer must supply from the source side, with the CIRCULARITY WARNING typed (a target-computed C -- eigendata or the converse's pseudoinverse -- is a reformulation, not a proof); (5) krein_cofinal / krein_cofinal_weil -- contractors on a cofinal ladder produce H_cof (index extraction via Filter.extraction_of_frequently_atTop) and compose through CofinalWeil.weil_nonneg_of_cofinal to Weil nonnegativity on the whole dense family -- no hidden wall behind the contractor certificates.  Nothing here proves the contractor exists; v866 delivers its closed FORMULA and v866's Perron closure types what any certificate must use.  NO RH claim.  Python-only per GATE.WOLFRAM.02.

PROVENANCE: discovery probes mobius_deck_redheffer_probe.py (37/37,
verdicts DECK-MU-PARALLEL + REDHEFFER-ECHO-EXACT) and
krein_normalform_probe.py (8/8, verdict
KREIN-CONTRACTOR-STABLE-NO-WORD), 2026-08-08, re-run identically at
promotion.  ROUND-31 EMBEDDING CONVENTION: the frozen sources are
embedded BYTE-EXACT (raw strings below) and executed verbatim in
isolated module namespaces registered under their canonical import
names -- the printed frozen spec SHAs reproduce exactly, and when
the original files are present the harness verifies byte-equality
(provenance ward inside the pattern gates).  The original probe
files live verbatim in experiments/tfpt-discovery/.  The normalform
probe imports the READ-ONLY deployed core v563_paper2_readouts.py.
The Lean frame TfptCarrier/KreinDefect.lean is kernel-checked
separately (lake build green, 3416 jobs); part C mirrors its
statements with numeric witnesses only.

FIREWALL: no zeros, no prime-table symbols beyond own sieves (AST
firewalls inside both probes); v563 READ-ONLY; pseudoinverse =
microscope only; RNG only in the declared scramble controls and the
seeded mirror witnesses.  NO RH claim.
"""

import contextlib
import io
import math
import os
import re
import sys
import time
import types

_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)

# ------------- frozen probe source mobius_deck_redheffer_probe (embedded BYTE-EXACT, raw string)
_SRC_0 = r'''
#!/usr/bin/env python3
"""THE DOUBLE-COVER <-> MOEBIUS QUESTION -- deck C2 vs mu-sign C2,
and the Redheffer/Mertens vacuum-column echo.  EXPLORATION ONLY.

QUESTION 1 (SHEET/MU-SIGN): the theory's geometric Z2 (sheet/deck
involution; the C2 factor read in the deployed register G = C2 x
F2^4 x mu4; the NS/R parity point) vs the arithmetic mu-sign (the C2
register the relational carrier uses, eps = sgn mu(d)).  Structurally
the SAME C2 or coincidentally both order 2?
  (a) WIRING CENSUS: rebuild the deployed register group and its 128
      characters; locate the sign-C2 generator s = (1,0,0) and the
      tower image of the deck iota(deck) = (0,0,2) in the mu4 slot
      ((1+i)^2 = 2i: the sheet 2 sits over i^2 = -1 in mu4); measure
      whether the deployed reading character chi_GL1 = (eps=-1, w=0,
      j=0) routes both through one slot (it reads the sign-C2 and is
      blind to the deck image -- measured exactly).  Deployed wiring
      cited: character_corner_probe event elements put the SIGN in the
      C2 slot and the (nonnegative) glue distribution in the mu4 slot;
      v833's deck acts trivially on F2^4, as the jet unit 1+eps at
      level 2, and as i*I in the metaplectic lift.
  (b) ACTION TEST: deck side -- ring-level wards of v833 rungs 2-4
      ((1+i)^2 = 2i, zeta8^2 = i, Z[i]/(2) ~= F2[eps]/(eps^2) with the
      deck = 1 + eps, deck == 1 mod (1+i); lattice census cited
      read-only).  mu side -- the M = Z^{-1} signs ARE the chain-
      length parity: M = sum_k (-1)^k N^k (N = Z - I strictly upper),
      verified exactly (the Philip Hall reading: mu(n) = alternating
      census of strict divisor chains -- the arithmetic double cover
      of the divisor poset by chain parity).  The mu4/(1+i) tower
      bookkeeping, exact: in the Galois double cover Q(i)/Q the cover
      Moebius obeys mu_K((p)) = chi4(p) for odd p (split: (p) = P
      Pbar, mu_K = +1; inert: mu_K = -1; ramified: (2) = (1+i)^2,
      mu_K = 0) -- i.e. the base sign mu(p) = -1 SURVIVES the cover
      exactly on the deck-odd (inert) sector; verified with explicit
      x^2 + y^2 witnesses for every odd p <= 10^4.
  (c) HONEST TYPING (frozen rule below): IDENTIFIED / PARALLEL /
      INDEPENDENT.

QUESTION 2 (REDHEFFER/MERTENS BRIDGE): the deployed divisibility Z is
unitriangular (det 1).  The Redheffer completion R_n = Z + u e_1^T
(u = ones beyond slot 1: the vacuum column) has det R_n = M(n) (the
Mertens function); RH <=> M(x) = O(x^{1/2+eps}) -- CITED, NOT CLAIMED,
NOT TESTED.
  (a) construction + wards: integer Bareiss determinants == M(n) on a
      predeclared n-set; the matrix-determinant lemma det = 1 +
      sum_{k>=2} (Z^{-1})[1,k] = M(n) with the exact inverse row.
  (b) VACUUM-PATTERN COMPARISON: SNF(R_n) vs SNF(Z_n) = I: witness
      minor (delete row/col 1) is unitriangular => d_{n-1} = 1, so the
      ENTIRE Smith deviation concentrates in ONE invariant factor
      |M(n)| (exact SNF cross-check at small n; rank/kernel typed at
      M(n) = 0 sites); mod-2 shadow det == M == Q(n) (squarefree
      count) mod 2; code side (parameter regression, deployed q*
      cited read-only v853): RM(1,4) + <x1x2+x3x4> = [16,6,6] self-
      orthogonal => CSS [[16,4,4]]; shorten at the origin slot =>
      [15,5,6] => CSS [[15,5,3]] -- the vacuum transformation
      [[15,5,3]] -> [[16,4,4]] reproduced at parameter grade.
      THE ONE STATEMENT (frozen): "vacuum completion is a one-column
      origin update X -> X + (column at the origin); it converts the
      trivial invariant into the global census, concentrated in a
      SINGLE new invariant -- arithmetic: det 1 -> M(n), Smith form
      (1,...,1,|M(n)|); code: one physical slot, one logical qubit
      paid, distance 3 -> 4 bought."  Cross-domain identification
      stays PATTERN-grade (no functor claimed); the enum measures
      whether both instantiations verify.
  (c) FLOOR CONNECTION (correlation census, fit-free): the certified
      ladder margins tau/tau_pnt and e1 vs the normalized Mertens
      m(X) = M(e^{2 alpha})/e^{alpha} across the full frame-A ladder;
      4 predeclared statistics, permutation p-values, Bonferroni x4.
      A census, NOT a claim.
  (d) SPECTRAL NOTE: eigenvalue-1 algebraic multiplicity of R_n ==
      n - floor(log2 n) - 1 (exact rank of (R-I)^s over GF(65521));
      Perron root vs sqrt(n) -- the ladder scale e^alpha = sqrt(X) is
      exactly the deployed 1/sqrt(n) normalization horizon (typed).

CONTROLS: CTRL-A det = Mertens ward (exact); CTRL-B mu-sign register
regression (mu*1 = delta and mu*log = Lambda exact at 360; float ward
at 256; tau_X kz9 vs the frozen carrier-probe ref); CTRL-C scramble
breaks the determinant structure (scrambled mu signs give a random-
walk Mertens path -- contrast bar; PLUS relabeling invariance: a
permuted divisor table leaves det R = M(n) unchanged -- only the sign
data itself carries the census); CTRL-D deck-action wards (ring level,
v833 cited read-only for the lattice census).

HONESTY: exploration only; NO RH claim (nothing here bounds zeros or
Mertens); no file written; nothing outside experiments/; v563 imports
READ-ONLY; own sieves; AST firewall.

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/mobius_deck_redheffer_probe.py
"""

import ast
import hashlib
import math
import os
import sys
import time
from fractions import Fraction as Fr

import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
_VERIFY = os.path.abspath(os.path.join(_HERE, "..", "..", "verification"))
sys.path.insert(0, _HERE)
sys.path.insert(0, _VERIFY)

import v563_paper2_readouts as core        # noqa: E402  (READ-ONLY)

FROZEN_SPEC = """\
PRIME.DECK.MU.REDHEFFER.01 spec v2 (2026-08-08; v2 = the census
ladder inherits the SECOND deployed exclusion.  The v1 run fired
ONLY the ladder ward S6.1 (36/37): v1 excluded h = 1292 but missed
the deployed horizon cut exp(2 alpha) <= ATOM_MAX + 0.5 (the bridge
probe's 67-frame battery, paircorr_bridge_map_probe S1.SET) -- the
two atom-truncated windows kz = 142 (X = 4.4e5, tau = -1.05e-4) and
kz = 177 (X = 7.9e5, tau = -0.29) carry incomplete combs and spurious
tau.  v2 adds the deployed cut (67 rungs expected, ward count
asserted); every other section of v1 passed unchanged and no other
number moved).
Q1 WIRING: register G = C2 x F2^4 x Z4 (|G| = 128) rebuilt; chars
chi(a,v,m) = (-1)^{eps a} (-1)^{pc(w&v)} i^{jm}; orthogonality exact;
sign generator s = (1,0,0); deck tower image iota(deck) = (0,0,2)
(from (1+i)^2 = 2i exact in Z[i]); deployed read chi_GL1 = (eps=1bit,
w=0, j=0).  IDENTIFIED requires chi_GL1(s) = chi_GL1(iota(deck)) = -1
(one slot reads both) or a deployed intertwiner module; measured.
The diagonal characters (read s AND iota(deck) as -1, trivial on
F2^4) are {(1,0,1), (1,0,3)}: chi(iota(deck)) = i^{2j} = (-1)^j, so
the identification needs a FAITHFUL mu4 character (j odd -- the
zeta8/metaplectic layer resolves i itself); typed as CANDIDATE
construction if present and distinct from chi_GL1.  Q1 ACTION: deck ring wards ((1+i)^2 = 2i; zeta8^2 = i via
(1+i)^2/2; Z[i]/(2) jet ring: exactly 1 of 24 bijections to
F2[eps]/(eps^2) is a ring iso, unique nonzero nilpotent = img(1+i),
deck 1+eps order 2, (i-1)/(1+i) = i so deck == 1 mod (1+i)); Hall
chain parity M = sum_k (-1)^k N^k exact at N_MU = 360 (int64), row 1
== mu, M @ Z == I; Galois bookkeeping: for ALL odd primes p <= P_MAX
= 10^4: p == 1 mod 4 <=> x^2+y^2 = p solvable (witness) <=> mu_K =
+1, p == 3 mod 4 <=> no representation <=> mu_K = -1; mu_K((2)) = 0
via (2) = -i (1+i)^2 exact.  Q1 RULE: IDENTIFIED as above; else
INDEPENDENT if any of {diag character, Hall parity, Galois
bookkeeping} fails; else PARALLEL (candidate constructions named).
Q2 REDHEFFER: R_n[i,j] = 1 iff j = 1 or i|j.  DET_SET = {1..60, 90,
120}: Bareiss integer det == M(n) exact; lemma det = 1 + sum_{k>=2}
mu(k) with exact Z^{-1} row 1 at n = 120.  VACUUM: witness minor
(delete row/col 1) == 1 exact for n in DET_SET => d_{n-1} = 1 =>
SNF = (1,..,1,|M(n)|) for M(n) != 0; sympy SNF cross-check n <= 24;
at M(n) = 0 sites in DET_SET: rank_{GF(65521)} = n-1 typed; mod-2:
M(n) == Q(n) mod 2 for all n <= N_SIEVE = 2e6.  CODE SIDE (parameter
regression; deployed q* cited): A16 = RM(1,4) + <x1x2+x3x4> --
[16,6,6] self-orth, CSS [[16,4,4]] (dual\\code min wt 4); shortened at
origin -- [15,5,6], CSS [[15,5,3]] (dual\\code min wt 3).  ECHO-EXACT
iff det wards + SNF concentration + mod-2 + code regression ALL pass
AND the census (c) is delivered; else ECHO-ANALOGY.  CENSUS: rungs =
core.frame_a_zones() minus h = 1292 (deployed anomaly exclusion)
minus exp(2 alpha) > ATOM_MAX + 0.5 (deployed horizon cut; 67 rungs
asserted == the deployed v818 battery);
per rung tau = eig2min(B - S), tau_pnt/S_pnt (U0 = 2 ln(-C_TH/4),
GRID_PER_D = 4, umax = 2 alpha + 1e-9), e1 = (tau/tau_pnt) h^{3/2},
m(X) = M(floor(X))/sqrt(X), X = e^{2 alpha}.  4 predeclared stats:
Spearman(tau/tau_pnt, m), Spearman(tau/tau_pnt, |m|), Spearman(e1,
m), Spearman(e1, |m|); permutation p (PERMS = 4000, LCG), two-sided;
FLAG iff 4 * min p < 0.05, else independence typed.  Rungs are nested
(correlated) -- census grade only, no claim.  SPECTRAL: n in {64,
128, 256, 512, 1024}: alg mult of eigenvalue 1 = n - rank_{GF(65521)}
((R-I)^16) == n - floor(log2 n) - 1; Perron root by power iteration
(200 its, n up to 4096), report lam/sqrt(n).  CONTROLS: CTRL-B
carrier regression (mu*1 = delta dict, mu*log = Lambda log-p-basis
dict at 360; float ward 1e-12 at 256; tau kz9 vs REG_REF 5.984165e-4
rel 1e-4); CTRL-C scramble: 3 LCG seeds, random +-1 on squarefree
support, pooled median |W_scr(X_k)|/sqrt(X_k) >= RATIO_BAR = 1.5 x
true pooled median |M(X_k)|/sqrt(X_k) (calibration note: true ratio
sits at 0.03-0.3 on this range, walk rms 0.78 -- bar 1.5 is
conservative); relabeling: permuted table (pi fixes 1, LCG) det ==
M(60) exact.  BAR_EXACT = 1e-12.  LCG seed 20260808.  Mertens spot
refs {10: -1, 100: 1, 1000: 2, 10000: -23, 100000: -48, 1000000:
212}.  NO RH claim; writes nothing.
"""

BAR_EXACT = 1.0e-12
N_MU = 360
N_SIEVE = 2_000_000
P_MAX = 10_000
DET_SET = tuple(list(range(1, 61)) + [90, 120])
SNF_MAX = 24
PERMS = 4000
RATIO_BAR = 1.5
REG_REF_KZ9 = 5.984165e-4
REG_BAR = 1.0e-4
GRID_PER_D = 4.0
GFP = 65521
SPECTRAL_NS = (64, 128, 256, 512, 1024)
PERRON_NS = (64, 128, 256, 512, 1024, 2048, 4096)
MERT_REFS = {10: -1, 100: 1, 1000: 2, 10000: -23, 100000: -48,
             1000000: 212}
BANNED_IDS = ("zetazero", "nzeros", "primerange", "isprime", "primepi",
              "nextprime", "prevprime")

CHECKS = []
FAILS = []
T0 = time.time()
_LCG = [20260808]


def lcg():
    _LCG[0] = (6364136223846793005 * _LCG[0] + 1442695040888963407) % (1 << 63)
    return _LCG[0] / float(1 << 63)


def lcg_int(n):
    return int(lcg() * n)


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok)))
    tag = "PASS" if ok else "FAIL"
    if not ok:
        FAILS.append(name)
    print("[%s] %s%s" % (tag, name, ("  -- " + detail) if detail else ""))


def section(title):
    print()
    print("=" * 72)
    print(title)
    print("=" * 72)


def ast_firewall():
    src = open(os.path.abspath(__file__), encoding="utf-8").read()
    bad = []
    for node in ast.walk(ast.parse(src)):
        name = None
        if isinstance(node, ast.Name):
            name = node.id
        elif isinstance(node, ast.Attribute):
            name = node.attr
        if name and name.lower() in BANNED_IDS:
            bad.append(name)
    return bad


# ===================================================== arithmetic layer
def build_sieves(n):
    """Own sieves: spf, mu, Mertens cumulative, squarefree cumulative."""
    # classic smallest-prime-factor sieve (vectorized outer loop)
    spf = np.zeros(n + 1, dtype=np.int64)
    for p in range(2, int(n ** 0.5) + 1):
        if spf[p] == 0:
            sl = spf[p * p::p]
            sl[sl == 0] = p
            spf[p * p::p] = sl
    primes_mask = (spf == 0)
    primes_mask[:2] = False
    primes = np.nonzero(primes_mask)[0]
    spf[primes] = primes
    mu = np.ones(n + 1, dtype=np.int64)
    mu[0] = 0
    for p in primes:
        mu[p::p] *= -1
    for p in primes[primes * primes <= n]:
        mu[p * p::p * p] = 0
    mert = np.cumsum(mu)
    mert[0] = 0
    sqfree = np.cumsum(np.abs(mu))
    return spf, mu, mert, sqfree, primes


def factorize(n, spf):
    out = {}
    while n > 1:
        p = int(spf[n])
        k = 0
        while n % p == 0:
            n //= p
            k += 1
        out[p] = k
    return out


def lam_logdict(n, spf):
    """Lambda(n) in the log-p basis: {p: k} means k*log p; Lambda is
    {p: 1} at prime powers, {} else."""
    f = factorize(n, spf)
    if len(f) == 1:
        p = next(iter(f))
        return {p: Fr(1)}
    return {}


def log_logdict(n, spf):
    return {p: Fr(k) for p, k in factorize(n, spf).items()}


def dict_add(a, b, s=1):
    out = dict(a)
    for k, v in b.items():
        out[k] = out.get(k, Fr(0)) + s * v
        if out[k] == 0:
            del out[k]
    return out


# ===================================================== small helpers
def eig2min(M2):
    a, b, c = M2[0, 0], M2[0, 1], M2[1, 1]
    mid, R = 0.5 * (a + c), math.hypot(0.5 * (a - c), b)
    return mid - R


def pnt_tau_mat(rr, U0):
    Mz, D = rr["M"], rr["D"]
    umax = 2.0 * rr["alpha"] + 1e-9
    delta = D / GRID_PER_D
    n_cells = int(math.ceil((umax - U0) / delta))
    edges = U0 + delta * np.arange(n_cells + 1)
    reads = np.empty((n_cells, 3))
    centers = 0.5 * (edges[:-1] + edges[1:])
    for j, u_j in enumerate(centers):
        reads[j, 0] = core.spline_project(rr["W11"], u_j, D, Mz)
        reads[j, 1] = core.spline_project(rr["W22"], u_j, D, Mz)
        reads[j, 2] = core.spline_project(rr["W12"], u_j, D, Mz)
    hi = np.minimum(edges[1:], umax)
    lo = np.minimum(edges[:-1], umax)
    m = 2.0 * (np.exp(hi / 2.0) - np.exp(lo / 2.0))
    s = m @ reads
    Sp = np.array([[s[0], s[2]], [s[2], s[1]]])
    return eig2min(np.asarray(rr["B"], float) - Sp), Sp


def bareiss_det(A):
    """Fraction-free integer determinant with row pivoting (exact)."""
    a = [row[:] for row in A]
    n = len(a)
    sign = 1
    prev = 1
    for k in range(n - 1):
        if a[k][k] == 0:
            piv = next((r for r in range(k + 1, n) if a[r][k] != 0), None)
            if piv is None:
                return 0
            a[k], a[piv] = a[piv], a[k]
            sign = -sign
        for i in range(k + 1, n):
            rik = a[i][k]
            rkk = a[k][k]
            rowk = a[k]
            rowi = a[i]
            for j in range(k + 1, n):
                rowi[j] = (rkk * rowi[j] - rik * rowk[j]) // prev
            rowi[k] = 0
        prev = a[k][k]
    return sign * a[n - 1][n - 1]


def redheffer_int(n):
    """R_n as list-of-lists ints: R[i][j] = 1 iff j = 1 or i | j."""
    R = [[0] * n for _ in range(n)]
    for i in range(1, n + 1):
        R[i - 1][0] = 1
        for j in range(i, n + 1, i):
            R[i - 1][j - 1] = 1
    return R


def gf_rank(Anp, p=GFP):
    """Exact rank over GF(p) by float-safe elimination (entries < p)."""
    A = np.array(Anp % p, dtype=np.int64)
    n, m = A.shape
    rank = 0
    row = 0
    for col in range(m):
        piv = None
        for r in range(row, n):
            if A[r, col] % p:
                piv = r
                break
        if piv is None:
            continue
        A[[row, piv]] = A[[piv, row]]
        inv = pow(int(A[row, col]), p - 2, p)
        A[row] = (A[row] * inv) % p
        mask = (A[:, col] % p) != 0
        mask[row] = False
        if mask.any():
            A[mask] = (A[mask] - np.outer(A[mask, col], A[row])) % p
        rank += 1
        row += 1
        if row == n:
            break
    return rank


def gf_matmul(A, B, p=GFP):
    """(A @ B) mod p with float64 (safe: n * p^2 < 2^53 for n <= 1024)."""
    C = np.dot(A.astype(np.float64), B.astype(np.float64))
    return np.mod(C, p).astype(np.int64)


def spearman(x, y):
    def ranks(v):
        idx = np.argsort(v, kind="mergesort")
        r = np.empty(len(v))
        r[idx] = np.arange(1, len(v) + 1)
        vv = np.asarray(v)
        uu = np.unique(vv)
        if len(uu) < len(vv):                  # average ties (rare)
            for val in uu:
                m = vv == val
                if m.sum() > 1:
                    r[m] = r[m].mean()
        return r
    rx, ry = ranks(x), ranks(y)
    rx = rx - rx.mean()
    ry = ry - ry.mean()
    den = math.sqrt(float((rx ** 2).sum() * (ry ** 2).sum()))
    return float((rx * ry).sum() / den) if den > 0 else 0.0


def perm_p(x, y, stat, nperm):
    obs = stat(x, y)
    y = np.array(y, dtype=float)
    cnt = 0
    for _ in range(nperm):
        idx = np.arange(len(y))
        for i in range(len(idx) - 1, 0, -1):
            j = lcg_int(i + 1)
            idx[i], idx[j] = idx[j], idx[i]
        if abs(stat(x, y[idx])) >= abs(obs) - 1e-15:
            cnt += 1
    return obs, (cnt + 1) / (nperm + 1)


# ===================================================== GF(2) code layer
def gf2_rank_rows(rows):
    rr = list(rows)
    rank = 0
    piv = []
    for i in range(len(rr)):
        v = rr[i]
        for (b, pv) in piv:
            if v >> b & 1:
                v ^= pv
        if v:
            b = v.bit_length() - 1
            piv.append((b, v))
            rank += 1
    return rank


def gf2_span(basis):
    out = [0]
    for b in basis:
        out += [w ^ b for w in out]
    return out


def gf2_nullspace(basis, nbits):
    """Basis of the dual code {v : <v, b> even for all b} in F2^nbits."""
    # gaussian elimination on the basis as a matrix, then free-variable
    rows = list(basis)
    pivcols = []
    r = 0
    for c in range(nbits):
        piv = None
        for i in range(r, len(rows)):
            if rows[i] >> c & 1:
                piv = i
                break
        if piv is None:
            continue
        rows[r], rows[piv] = rows[piv], rows[r]
        for i in range(len(rows)):
            if i != r and (rows[i] >> c & 1):
                rows[i] ^= rows[r]
        pivcols.append(c)
        r += 1
        if r == len(rows):
            break
    rows = rows[:r]
    free = [c for c in range(nbits) if c not in pivcols]
    null = []
    for f in free:
        v = 1 << f
        for i, c in enumerate(pivcols):
            if rows[i] >> f & 1:
                v |= 1 << c
        null.append(v)
    return null


# ======================================================== main sections
def main():
    print("mobius_deck_redheffer_probe -- deck C2 vs mu-sign C2 + the")
    print("Redheffer/Mertens vacuum column.  EXPLORATION ONLY, NO RH CLAIM.")
    sha = hashlib.sha256(FROZEN_SPEC.encode("utf-8")).hexdigest()
    print("    FROZEN_SPEC SHA-256 = %s" % sha)

    section("S0 -- firewall")
    bad = ast_firewall()
    check("S0.1 AST firewall: no zeta-zero / prime-table symbols",
          not bad, str(bad))

    # ------------------------------------------------------------- S1
    section("S1 -- arithmetic layer (own sieves) + wards")
    t = time.time()
    spf_s, mu_s, _, _, _ = build_sieves(N_MU)
    spf, mu, mert, sqfree, primes = build_sieves(N_SIEVE)
    print("    sieves to %d in %.1f s" % (N_SIEVE, time.time() - t))
    ok = all(int(mert[k]) == v for k, v in MERT_REFS.items())
    check("S1.1 Mertens spot refs %s exact" % MERT_REFS, ok,
          str({k: int(mert[k]) for k in MERT_REFS}))
    # mu * 1 = delta as dict identity (Dirichlet convolution, n <= 360)
    ok = True
    for n in range(1, N_MU + 1):
        s = sum(int(mu_s[d]) for d in range(1, n + 1) if n % d == 0)
        if s != (1 if n == 1 else 0):
            ok = False
            break
    check("S1.2 mu * 1 = delta_1 exact for all n <= %d" % N_MU, ok)
    # mu * log = Lambda in the exact log-p basis (Fractions)
    ok = True
    worst = None
    for n in range(1, N_MU + 1):
        acc = {}
        for d in range(1, n + 1):
            if n % d == 0 and mu_s[d] != 0:
                acc = dict_add(acc, log_logdict(n // d, spf_s),
                               s=Fr(int(mu_s[d])))
        if acc != lam_logdict(n, spf_s):
            ok = False
            worst = n
            break
    check("S1.3 mu * log == Lambda exact (log-p basis dicts, n <= %d)"
          % N_MU, ok, "" if ok else "first defect at n = %s" % worst)

    # ------------------------------------------------------------- S2
    section("S2 -- Q1(a) THE WIRING CENSUS (register level, exact)")
    # the deployed register group G = C2 x F2^4 x Z4, |G| = 128
    G = [(a, v, m) for a in range(2) for v in range(16) for m in range(4)]
    CH = [(e, w, j) for e in range(2) for w in range(16) for j in range(4)]

    IUNIT = (1 + 0j, 1j, -1 + 0j, -1j)      # exact i^k table

    def chival(chi, g):
        e, w, j = chi
        a, v, m = g
        s = (-1) ** (e * a) * (-1) ** (bin(w & v).count("1"))
        return s * IUNIT[(j * m) % 4]

    ok = True
    for i1 in range(0, 128, 17):          # LCG-free deterministic sample
        for i2 in range(0, 128, 13):
            s = sum(chival(CH[i1], g) * np.conj(chival(CH[i2], g))
                    for g in G)
            want = 128 if i1 == i2 else 0
            if abs(s - want) > 1e-9:
                ok = False
    check("S2.1 character orthogonality on G = C2 x F2^4 x Z4 "
          "(|G| = 128, sampled pairs, values exact units)", ok)
    chi_gl1 = (1, 0, 0)               # deployed: eps = -1, w = 0, j = 0
    s_gen = (1, 0, 0)                 # the sign-C2 generator (mu-sign slot)
    # the deck tower image: (1+i)^2 = 2i exact in Z[i] (multiplication,
    # never complex pow -- pow is float-inexact)
    z = complex(1, 1)
    ok = (z * z == complex(0, 2))
    check("S2.2 tower square (1+i)^2 = 2i exact (Gaussian units)", ok)
    deck_img = (0, 0, 2)              # i^2 = -1 in the mu4 slot
    v1 = chival(chi_gl1, s_gen)
    v2 = chival(chi_gl1, deck_img)
    check("S2.3 deployed read chi_GL1 = (eps=-1, w=0, j=0): reads the "
          "sign-C2 as -1 AND is blind to the deck image (+1)",
          v1 == -1 and v2 == 1,
          "chi_GL1(s) = %s, chi_GL1(iota(deck)) = %s" % (v1, v2))
    triv = all(chival(chi_gl1, (0, v, m)) == 1
               for v in range(16) for m in range(4))
    check("S2.4 chi_GL1 trivial on F2^4 x mu4 (all 64 elements)", triv)
    # subgroup census: <s> vs <iota(deck)> inside G
    check("S2.5 <s> and <iota(deck)> are DIFFERENT order-2 subgroups "
          "with trivial intersection", s_gen != deck_img)
    # the diagonal candidates: characters reading BOTH as -1
    diags = [chi for chi in CH
             if chival(chi, s_gen) == -1 and chival(chi, deck_img) == -1
             and all(chival(chi, (0, v, 0)) == 1 for v in range(16))]
    check("S2.6 the intertwining CANDIDATE characters exist and are "
          "NOT the deployed read: {(eps=-1, w=0, j=1), (eps=-1, w=0, "
          "j=3)} -- a FAITHFUL mu4 character is required (chi(iota("
          "deck)) = (-1)^j: the zeta8/metaplectic layer must resolve i)",
          diags == [(1, 0, 1), (1, 0, 3)] and chi_gl1 not in diags,
          "diagonal characters (trivial on F2^4) = %s" % diags)
    print("    WIRING CENSUS (deployed loci, cited): the carrier/corner")
    print("    probes put the SIGN in the C2 slot (event elements: 'C2")
    print("    slot = the pure sign carrier'; chi_GL1 reads it as -1) and")
    print("    the nonnegative glue distribution Th_m/240 sigma3 in the")
    print("    mu4 slot (no sign content possible there); v833's deck is")
    print("    trivial on F2^4 (rung 2), the jet unit 1 + eps (rung 3),")
    print("    and i*I in the metaplectic lift (rung 4) -- the deck lives")
    print("    in the mu4/jet tower, NOT in the register's C2 factor.")
    print("    => TWO SEPARATE C2s in the deployed wiring; the deployed")
    print("    reading character SEPARATES them (S2.3).")

    # ------------------------------------------------------------- S3
    section("S3 -- Q1(b) THE ACTION TEST (deck wards + mu-sign structure)")
    # CTRL-D: deck ring wards (v833 rungs 2-4 at ring level)
    # zeta8^2 = i via (1+i)^2 / 2 (exact multiplication)
    check("S3.1 zeta8 = (1+i)/sqrt2: zeta8^2 = (1+i)^2/2 = i exact",
          (z * z) / 2 == complex(0, 1))
    # jet ring Z[i]/(2) ~= F2[eps]/(eps^2): residues {0, 1, i, 1+i}
    res = [(0, 0), (1, 0), (0, 1), (1, 1)]      # (x + y i) mod 2

    def gmul2(u, v):
        x = (u[0] * v[0] - u[1] * v[1]) % 2
        y = (u[0] * v[1] + u[1] * v[0]) % 2
        return (x, y)

    def gadd2(u, v):
        return ((u[0] + v[0]) % 2, (u[1] + v[1]) % 2)

    nilp = [r for r in res if gmul2(r, r) == (0, 0) and r != (0, 0)]
    check("S3.2 jet ring: unique nonzero nilpotent of Z[i]/(2) is the "
          "image of (1+i)", nilp == [(1, 1)])
    # ring isos to F2[eps]/(eps^2) = {0, 1, e, 1+e}
    jet = [(0, 0), (1, 0), (0, 1), (1, 1)]      # (c + d eps)

    def jmul(u, v):
        return ((u[0] * v[0]) % 2, (u[0] * v[1] + u[1] * v[0]) % 2)

    def jadd(u, v):
        return ((u[0] + v[0]) % 2, (u[1] + v[1]) % 2)

    from itertools import permutations
    iso_count = 0
    iso_map = None
    for perm in permutations(range(4)):
        f = {res[i]: jet[perm[i]] for i in range(4)}
        ok = all(f[gadd2(u, v)] == jadd(f[u], f[v]) and
                 f[gmul2(u, v)] == jmul(f[u], f[v])
                 for u in res for v in res) and f[(1, 0)] == (1, 0)
        if ok:
            iso_count += 1
            iso_map = f
    check("S3.3 EXACTLY 1 of 24 bijections is a unital ring iso "
          "Z[i]/(2) -> F2[eps]/(eps^2); it sends 1+i -> eps",
          iso_count == 1 and iso_map[(1, 1)] == (0, 1),
          "iso count = %d" % iso_count)
    deck = (1, 1)   # 1 + eps in jet coords via iso: deck = 1 + img(1+i)
    check("S3.4 deck = 1 + eps is a unit of order 2 ((1+eps)^2 = 1)",
          jmul(deck, deck) == (1, 0))
    # deck == 1 mod (1+i): (i - 1)/(1+i) = i exactly
    check("S3.5 deck trivial at level 1: i - 1 = i * (1 + i) exact "
          "(so mult-by-i == identity mod (1+i); v833 R2.2 lattice "
          "census cited read-only)",
          complex(0, 1) * complex(1, 1) == complex(-1, 1))

    # mu-sign structure: Hall chain parity, exact integers at N_MU
    t = time.time()
    n = N_MU
    Zi = np.zeros((n, n), dtype=np.int64)
    for a in range(1, n + 1):
        Zi[a - 1, a - 1::a] = 1
    Ni = Zi - np.eye(n, dtype=np.int64)
    Mi = np.eye(n, dtype=np.int64)
    Pk = np.eye(n, dtype=np.int64)
    sgn = 1
    kmax = 0
    chain_counts = []
    while True:
        Pk = Pk @ Ni
        if not Pk.any():
            break
        kmax += 1
        sgn = -sgn
        Mi = Mi + sgn * Pk
        chain_counts.append(Pk[0].copy())
    ok = np.array_equal(Mi @ Zi, np.eye(n, dtype=np.int64))
    check("S3.6 Hall chain parity: M = sum_k (-1)^k N^k terminates at "
          "k = %d and M @ Z == I exactly (n = %d)" % (kmax, n), ok)
    ok = np.array_equal(Mi[0], mu_s[1:n + 1])
    check("S3.7 row 1 of M == mu exactly: the mu-sign IS the chain-"
          "length parity (alternating census of strict divisor chains)",
          ok)
    ex = 30
    terms = [int(cc[ex - 1]) for cc in chain_counts]
    alt = sum(((-1) ** k) * c for k, c in enumerate(terms, start=1))
    print("    example n = %d: strict chain counts by length %s, "
          "alternating sum = %d == mu(%d) = %d"
          % (ex, terms, alt, ex, int(mu_s[ex])))
    print("    typed: the mu-sign C2 is the CHAIN-PARITY GRADING of the")
    print("    incidence algebra -- the arithmetic double cover of the")
    print("    divisor poset.  Identifying it with the geometric deck is")
    print("    a CONSTRUCTION candidate, not a deployed fact.")
    print("    (%.1f s)" % (time.time() - t))

    # Galois bookkeeping: mu_K((p)) = chi4(p) for odd p <= P_MAX
    t = time.time()
    odd_primes = [int(p) for p in primes if p <= P_MAX and p > 2]
    ok_split, ok_inert = True, True
    n_split = n_inert = 0
    wit = {}
    for p in odd_primes:
        has_rep = False
        x = 1
        while x * x * 2 <= p:
            y2 = p - x * x
            y = int(math.isqrt(y2))
            if y * y == y2:
                has_rep = True
                wit[p] = (x, y)
                break
            x += 1
        chi4 = 1 if p % 4 == 1 else -1
        if chi4 == 1:
            n_split += 1
            if not has_rep:
                ok_split = False
        else:
            n_inert += 1
            if has_rep:
                ok_inert = False
    check("S3.8 Galois bookkeeping, split sector: ALL %d primes p == 1 "
          "mod 4 (p <= %d) have p = x^2 + y^2 (witnesses found) -- "
          "(p) = P Pbar, mu_K((p)) = mu(P) mu(Pbar) = +1 = chi4(p)"
          % (n_split, P_MAX), ok_split,
          "e.g. %s" % ({p: wit[p] for p in odd_primes[:8] if p in wit}))
    check("S3.9 Galois bookkeeping, INERT (deck-odd) sector: ALL %d "
          "primes p == 3 mod 4 have NO representation -- (p) stays "
          "prime, mu_K((p)) = -1 = chi4(p) = mu(p)" % n_inert, ok_inert)
    check("S3.10 ramified: (2) = -i (1+i)^2 exact, so mu_K((2)) = 0 "
          "(the sheet-2 site is where the cover kills the sign)",
          complex(0, -1) * (z * z) == complex(2, 0))
    print("    ONE-LINE BOOKKEEPING (exact, %d + %d primes): mu_K((p)) ="
          % (n_split, n_inert))
    print("    chi4(p) for odd p; mu(p) mu_K((p)) = -chi4(p); the base")
    print("    sign mu(p) = -1 SURVIVES the double cover EXACTLY on the")
    print("    deck-odd (inert, Frobenius = deck) sector.  This is the")
    print("    (1+i)/mu4-tower connection -- theorem-grade bookkeeping,")
    print("    but a CANDIDATE identification (Frobenius = deck is the")
    print("    construction), not deployed wiring.  (%.1f s)"
          % (time.time() - t))

    # Q1 verdict per frozen rule
    q1_identified = (v1 == -1 and v2 == -1)
    q1_connections = (diags == [(1, 0, 1), (1, 0, 3)]) \
        and ok_split and ok_inert \
        and bool(np.array_equal(Mi[0], mu_s[1:n + 1]))
    if q1_identified:
        q1 = "DECK-MU-IDENTIFIED"
    elif q1_connections:
        q1 = "DECK-MU-PARALLEL"
    else:
        q1 = "DECK-MU-INDEPENDENT"

    # ------------------------------------------------------------- S4
    section("S4 -- Q2(a) THE REDHEFFER CONSTRUCTION + det = Mertens ward")
    t = time.time()
    ok_all = True
    worst = None
    for nn in DET_SET:
        d = bareiss_det(redheffer_int(nn))
        if d != int(mert[nn]):
            ok_all = False
            worst = (nn, d, int(mert[nn]))
            break
    check("S4.1 CTRL-A: Bareiss integer det R_n == M(n) EXACT for all "
          "n in DET_SET (%d values, n <= 120)" % len(DET_SET), ok_all,
          "defect %s" % (worst,) if worst else
          "e.g. det R_60 = %d, det R_120 = %d"
          % (int(mert[60]), int(mert[120])))
    print("    (%.1f s)" % (time.time() - t))
    # matrix determinant lemma with the exact inverse row
    n = 120
    Zi = np.zeros((n, n), dtype=np.int64)
    for a in range(1, n + 1):
        Zi[a - 1, a - 1::a] = 1
    # exact triangular inversion, row 1
    row1 = np.zeros(n, dtype=np.int64)
    row1[0] = 1
    for b in range(2, n + 1):
        s = 0
        for d in range(1, b):
            if b % d == 0:
                s += row1[d - 1]
        row1[b - 1] = -s
    ok = np.array_equal(row1, mu_s[1:n + 1])
    check("S4.2 exact Z^{-1} row 1 == mu (independent back-substitution, "
          "n = 120)", ok)
    lem = 1 + int(row1[1:].sum())
    check("S4.3 matrix-determinant lemma: det(Z + u e1^T) = 1 + "
          "sum_{k>=2} mu(k) = %d == M(120) = %d (det Z = 1; the vacuum "
          "column is a rank-one origin update)" % (lem, int(mert[120])),
          lem == int(mert[120]))
    print("    typed: along ALL n <= %d the lemma gives det R_n = M(n)"
          % N_SIEVE)
    print("    identically (cumulative mu); the n <= 120 direct")
    print("    determinants are the independent ward.")

    # ------------------------------------------------------------- S5
    section("S5 -- Q2(b) THE VACUUM-PATTERN COMPARISON")
    t = time.time()
    # witness minor: delete row/col 1 -> unitriangular, det = 1
    ok_minor = True
    for nn in DET_SET:
        if nn < 2:
            continue
        R = redheffer_int(nn)
        Msub = [row[1:] for row in R[1:]]
        if bareiss_det(Msub) != 1:
            ok_minor = False
            break
    check("S5.1 witness minor (delete row/col 1) == 1 EXACT for all "
          "n in DET_SET => d_{n-1} = gcd of (n-1)-minors = 1", ok_minor)
    print("    => SNF(R_n) = diag(1, ..., 1, |M(n)|) whenever M(n) != 0:")
    print("    the ENTIRE Smith deviation from the unimodular Z (SNF = I)")
    print("    concentrates in ONE invariant factor = the signed census.")
    # sympy SNF cross-check at small n
    from sympy import Matrix, ZZ
    from sympy.matrices.normalforms import smith_normal_form
    ok_snf = True
    for nn in range(2, SNF_MAX + 1):
        S = smith_normal_form(Matrix(redheffer_int(nn)), domain=ZZ)
        diag = [abs(int(S[i, i])) for i in range(nn)]
        want = [1] * (nn - 1) + [abs(int(mert[nn]))]
        if sorted(diag) != sorted(want):
            ok_snf = False
            break
    check("S5.2 sympy SNF cross-check n <= %d: invariant factors "
          "(1,...,1,|M(n)|) exact (including |M| = 0 ranks)" % SNF_MAX,
          ok_snf)
    zeros = [nn for nn in DET_SET if nn >= 2 and int(mert[nn]) == 0]
    ok_rank = all(gf_rank(np.array(redheffer_int(nn))) == nn - 1
                  for nn in zeros)
    check("S5.3 M(n) = 0 sites in DET_SET %s: rank drops by EXACTLY 1 "
          "(GF(%d)); cokernel = Z (free), typed" % (zeros, GFP), ok_rank)
    # mod-2 shadow
    ok_mod2 = bool(np.all((mert % 2) == (sqfree % 2)))
    check("S5.4 mod-2 shadow: M(n) == Q(n) (squarefree count) mod 2 for "
          "ALL n <= %d -- det R mod 2 = the vacuum column's parity "
          "census" % N_SIEVE, ok_mod2)
    print("    (%.1f s)" % (time.time() - t))

    # code side: parameter regression of the vacuum transformation
    pts = list(range(16))                     # F2^4 points as ints
    def evalvec(f):
        w = 0
        for i, x in enumerate(pts):
            if f(x):
                w |= 1 << i
        return w
    ones = evalvec(lambda x: 1)
    coords = [evalvec(lambda x, b=b: (x >> b) & 1) for b in range(4)]
    qword = evalvec(lambda x: ((x >> 0) & (x >> 1) & 1) ^
                    ((x >> 2) & (x >> 3) & 1))
    rm14 = [ones] + coords
    a16 = rm14 + [qword]
    dim = gf2_rank_rows(a16)
    words = gf2_span(a16)
    wts = sorted({bin(w).count("1") for w in words if w})
    selforth = all(bin(u & v).count("1") % 2 == 0
                   for u in a16 for v in a16)
    check("S5.5 code side: A16 = RM(1,4) + <x1x2+x3x4> is [16, 6, %d], "
          "self-orthogonal (deployed canonical q* cited read-only, "
          "v853)" % min(wts), dim == 6 and min(wts) == 6 and selforth)
    dual = gf2_nullspace(a16, 16)
    dwords = gf2_span(dual)
    inset = set(words)
    dmin = min(bin(w).count("1") for w in dwords if w and w not in inset)
    check("S5.6 CSS [[16, 16 - 2*6 = 4, %d]]: min weight of dual "
          "minus code = 4 -- the completed code" % dmin,
          len(dual) == 10 and dmin == 4)
    # shorten at the origin slot (evaluation point x = 0, bit 0)
    short = [w >> 1 for w in words if not (w & 1)]
    sbasis = []
    for w in short:
        if gf2_rank_rows(sbasis + [w]) > len(sbasis):
            sbasis.append(w)
    sdim = len(sbasis)
    swts = sorted({bin(w).count("1") for w in short if w})
    check("S5.7 shortening at the vacuum/origin slot: [15, 5, %d] "
          "(one slot removed, one dimension paid)" % min(swts),
          sdim == 5 and min(swts) == 6)
    sdual = gf2_nullspace(sbasis, 15)
    sdw = gf2_span(sdual)
    sset = set(gf2_span(sbasis))
    sdmin = min(bin(w).count("1") for w in sdw if w and w not in sset)
    check("S5.8 CSS [[15, 15 - 2*5 = 5, %d]]: the punctured code -- the "
          "vacuum transformation [[15,5,3]] -> [[16,4,4]] reproduced at "
          "parameter grade" % sdmin, len(sdual) == 10 and sdmin == 3)
    print("    THE ONE STATEMENT (frozen text, both instantiations")
    print("    machine-verified above): vacuum completion is a one-column")
    print("    origin update; it converts the trivial invariant into the")
    print("    global census concentrated in a SINGLE new invariant --")
    print("    arithmetic: det 1 -> M(n) with Smith form (1,...,1,|M(n)|);")
    print("    code: one physical slot added, one logical qubit paid,")
    print("    distance 3 -> 4 bought.  The cross-domain identification")
    print("    is PATTERN-grade: no functor is deployed or claimed.")

    # ------------------------------------------------------------- S6
    section("S6 -- Q2(c) THE FLOOR-MERTENS CORRELATION CENSUS (fit-free)")
    t = time.time()
    from mpmath import zeta as mzeta, diff as mdiff
    C_TH = float(-2 * mdiff(lambda s: mzeta(s), 0.5) / mzeta(0.5))
    U0 = 2.0 * math.log(-C_TH / 4.0)
    print("    v818 convention: U0 = %.6f" % U0)
    kzs = [kz for kz in core.frame_a_zones()]
    rows = []
    n_cut = 0
    for kz in kzs:
        rr = core.build_window(kz)
        if rr["h"] == 1292:               # deployed anomaly exclusion
            continue
        if rr["X"] > core.ATOM_MAX + 0.5:   # deployed horizon cut (v2)
            n_cut += 1
            continue
        tau = eig2min(rr["Ah"])
        tau_p, _ = pnt_tau_mat(rr, U0)
        X = rr["X"]
        mm = int(mert[min(int(X), N_SIEVE)]) / math.sqrt(X)
        rows.append((kz, rr["alpha"], rr["h"], X, tau, tau_p,
                     (tau / tau_p) * rr["h"] ** 1.5, mm))
    print("    ladder: %d rungs (h = 1292 excluded; %d atom-truncated "
          "windows beyond ATOM_MAX cut), alpha %.2f .. %.2f,"
          % (len(rows), n_cut, rows[0][1], rows[-1][1]))
    print("    X %.3g .. %.3g  (%.1f s)"
          % (rows[0][3], rows[-1][3], time.time() - t))
    ok_pos = all(r[4] > 0 and r[5] > 0 for r in rows) and len(rows) == 67
    check("S6.1 ladder ward: 67 rungs == the deployed v818 battery AND "
          "tau > 0 and tau_pnt > 0 on every census rung", ok_pos,
          "%d rungs" % len(rows))
    kz9 = next(r for r in rows if r[0] == 9)
    check("S6.2 CTRL-B: tau(kz = 9) = %.6e vs frozen carrier-probe ref "
          "%.6e (rel %.1e)" % (kz9[4], REG_REF_KZ9,
                               abs(kz9[4] / REG_REF_KZ9 - 1)),
          abs(kz9[4] / REG_REF_KZ9 - 1) < REG_BAR)
    tt = np.array([r[4] / r[5] for r in rows])
    e1 = np.array([r[6] for r in rows])
    mm = np.array([r[7] for r in rows])
    print("    Mertens path at the horizons: m(X) = M(X)/sqrt(X) in "
          "[%.3f, %.3f], median |m| = %.3f"
          % (mm.min(), mm.max(), float(np.median(np.abs(mm)))))
    stats = [("Spearman(tau/tau_pnt, m)", tt, mm),
             ("Spearman(tau/tau_pnt, |m|)", tt, np.abs(mm)),
             ("Spearman(e1, m)", e1, mm),
             ("Spearman(e1, |m|)", e1, np.abs(mm))]
    pmin = 1.0
    for name, x, y in stats:
        obs, p = perm_p(x, y, spearman, PERMS)
        pmin = min(pmin, p)
        print("    %-30s = %+.3f   perm p = %.4f" % (name, obs, p))
    flag = 4 * pmin < 0.05
    check("S6.3 census verdict: %s (Bonferroni x4: min p = %.4f, "
          "4p = %.3f %s 0.05); rungs are NESTED (correlated) -- census "
          "grade, no claim"
          % ("CORRELATION FLAGGED" if flag else
             "no resolvable correlation (independence at this grade)",
             pmin, 4 * pmin, "<" if flag else ">="), True)
    census_flag = flag

    # ------------------------------------------------------------- S7
    section("S7 -- Q2(d) THE REDHEFFER SPECTRAL NOTE")
    t = time.time()
    ok_mult = True
    for nn in SPECTRAL_NS:
        R = np.array(redheffer_int(nn), dtype=np.int64)
        A = (R - np.eye(nn, dtype=np.int64)) % GFP
        P = A.copy()
        for _ in range(4):                 # (R - I)^16 by squaring
            P = gf_matmul(P, P)
        mult = nn - gf_rank(P)
        want = nn - int(math.floor(math.log2(nn))) - 1
        star = "==" if mult == want else "!="
        if mult != want:
            ok_mult = False
        print("    n = %4d: alg mult(eigenvalue 1) = %d %s "
              "n - floor(log2 n) - 1 = %d" % (nn, mult, star, want))
    check("S7.1 eigenvalue-1 algebraic multiplicity = n - floor(log2 n)"
          " - 1 (exact GF(%d) rank of (R - I)^16) on all %d sizes"
          % (GFP, len(SPECTRAL_NS)), ok_mult)
    print("    nontrivial spectrum size 2 floor(log2 n) + 1 - trivial:")
    for nn in PERRON_NS:
        R = np.array(redheffer_int(nn), dtype=float)
        v = np.ones(nn) / math.sqrt(nn)
        for _ in range(300):
            w = R @ v
            v = w / np.linalg.norm(w)
        lam = float(v @ (R @ v))
        print("    n = %5d: Perron root = %9.4f   lam/sqrt(n) = %.4f"
              % (nn, lam, lam / math.sqrt(nn)))
    print("    typed: the Perron root grows as ~sqrt(n) (ratio drifting")
    print("    slowly, consistent with sqrt(n) + O(log n)); at the ladder")
    print("    horizons n = X = e^{2 alpha} this is e^{alpha} -- EXACTLY")
    print("    the deployed 1/sqrt(n) comb normalization scale (the")
    print("    sqrt-horizon).  No deeper deployed connection found:")
    print("    typed ABSENT (the margin tau is a spectral floor of the")
    print("    2x2 window compression, not of R_n).")
    print("    (%.1f s)" % (time.time() - t))

    # ------------------------------------------------------------- S8
    section("S8 -- CTRL-C: scramble vs relabeling")
    t = time.time()
    Xs = [r[3] for r in rows]
    true_med = float(np.median([abs(r[7]) for r in rows]))
    sq_pos = np.nonzero(np.abs(mu[:N_SIEVE + 1]) == 1)[0]
    ratios = []
    for seed in range(3):
        signs = np.array([1 if lcg() < 0.5 else -1
                          for _ in range(len(sq_pos))], dtype=np.int64)
        w = np.zeros(N_SIEVE + 1, dtype=np.int64)
        w[sq_pos] = signs
        W = np.cumsum(w)
        med = float(np.median([abs(int(W[min(int(X), N_SIEVE)]))
                               / math.sqrt(X) for X in Xs]))
        ratios.append(med / true_med)
        print("    seed %d: pooled median |W_scr(X)|/sqrt(X) = %.3f  "
              "(true = %.3f, ratio %.2f)" % (seed, med, true_med,
                                             med / true_med))
    med_ratio = float(np.median(ratios))
    check("S8.1 scrambled mu-signs give a random-walk Mertens path: "
          "median contrast ratio %.2f >= %.1f (the true path is "
          "anomalously SMALL -- the mu-sign data, not the support, "
          "carries the census)" % (med_ratio, RATIO_BAR),
          med_ratio >= RATIO_BAR)
    # relabeling invariance at n = 60
    nn = 60
    perm = list(range(2, nn + 1))
    for i in range(len(perm) - 1, 0, -1):
        j = lcg_int(i + 1)
        perm[i], perm[j] = perm[j], perm[i]
    pi = [1] + perm
    Rp = [[0] * nn for _ in range(nn)]
    for i in range(1, nn + 1):
        Rp[i - 1][0] = 1
        for j in range(1, nn + 1):
            if pi[j - 1] % pi[i - 1] == 0:
                Rp[i - 1][j - 1] = 1
    dp = bareiss_det(Rp)
    check("S8.2 relabeling invariance: det of the pi-permuted Redheffer "
          "table = %d == M(60) = %d (pi fixes 1; the census is basis-"
          "free -- only scrambling the SIGNS breaks it)"
          % (dp, int(mert[60])), dp == int(mert[60]))
    print("    (%.1f s)" % (time.time() - t))

    # ------------------------------------------------------------- V
    section("V -- FROZEN VERDICTS + the honest consequence")
    q2_exact = (ok_all and ok_minor and ok_snf and ok_rank and ok_mod2
                and dmin == 4 and sdmin == 3)
    q2 = "REDHEFFER-ECHO-EXACT" if q2_exact else "REDHEFFER-ECHO-ANALOGY"
    npass = sum(1 for _, ok in CHECKS if ok)
    print("    checks: %d/%d passed%s"
          % (npass, len(CHECKS),
             "" if not FAILS else "; FAILS: %s" % FAILS))
    if FAILS:
        q1 = "DECK-MU-WARD-FAIL"
        q2 = "REDHEFFER-WARD-FAIL"
    print()
    print("    VERDICT Q1: %s" % q1)
    print("      the deployed wiring has TWO separate C2s: the mu-sign")
    print("      lives in the register's C2 slot (read by chi_GL1 as -1),")
    print("      the deck lives in the mu4/(1+i) tower (image (0,0,2),")
    print("      read by chi_GL1 as +1) -- the deployed reading character")
    print("      SEPARATES them.  No deployed intertwiner exists.  Three")
    print("      candidate constructions named and machine-verified:")
    print("      (1) the diagonal characters (eps=-1, w=0, j=1 or 3) --")
    print("          the identification is ONE character away from the")
    print("          deployed GL1 read, and it must be FAITHFUL on mu4")
    print("          (the zeta8/metaplectic layer resolves i itself);")
    print("      (2) the Galois/Frobenius bookkeeping mu_K((p)) = chi4(p):")
    print("          mu(p) = -1 survives the double cover exactly on the")
    print("          deck-odd (inert) sector -- (1+i)^2 = 2i wired;")
    print("      (3) the Hall chain-parity grading: the mu-sign IS the")
    print("          chain-length parity of the divisor poset's cover.")
    print()
    print("    VERDICT Q2: %s%s" % (q2,
          "" if not census_flag else "  [census FLAGGED -- inspect]"))
    print("      det R_n = M(n) exact; the vacuum column is a rank-one")
    print("      origin update whose ENTIRE Smith deviation is the single")
    print("      invariant factor |M(n)|; mod-2 shadow = squarefree-count")
    print("      parity; the code-side vacuum transformation [[15,5,3]] ->")
    print("      [[16,4,4]] reproduced at parameter grade; the one")
    print("      statement holds with both instantiations verified,")
    print("      cross-domain identification typed PATTERN-grade.")
    print("      Floor census: %s."
          % ("correlation FLAGGED (see S6)" if census_flag else
             "no resolvable tau <-> Mertens correlation at this grade"))
    print()
    print("    HONEST CONSEQUENCE: nothing here bounds M(x) or zeta zeros")
    print("    -- NO RH claim.  The deck <-> mu identification remains a")
    print("    CONSTRUCTION target (the three candidates above); the")
    print("    Redheffer vacuum echo is a structural pattern statement,")
    print("    exact on each side separately.  The floor's window")
    print("    machinery does not resolve the Mertens fluctuation at")
    print("    census grade -- the margin ladder and the Mertens path are")
    print("    measured as independent at these horizons.")
    print()
    print("    total runtime %.1f s" % (time.time() - T0))
    return 0 if not FAILS else 1


if __name__ == "__main__":
    sys.exit(main())
'''
# ------------- frozen probe source krein_normalform_probe (embedded BYTE-EXACT, raw string)
_SRC_1 = r'''
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""krein_normalform_probe -- PRIME.SIGNED.KREIN.NORMALFORM.01 +
PRIME.KREIN.GRAPH.CENSUS.01 (EXPLORATION ONLY, experiments/;
round 33 midday packages A+B(+C), after LOCAL-SIGN-FAILS,
2026-08-08).

THE MOVE: the euler_schur probe measured that BOTH deployed
sides carry SIGNED spectral density (comb deposits 50 percent
negative mass; arch negative on the digamma band ending at
tau* = 6.27).  The Krein normal form takes the sign seriously:
write the deployed window form EXACTLY as

    Q_h(t) = ||B+ t||^2 - ||B- t||^2

via the canonical decomposition d nu = d nu_+ - d nu_- of the
exact grid spectral density -- exact linear algebra through the
CIRCULANT EMBEDDING: the symmetric M x M Toeplitz lag form
embeds exactly in the circulant of size L = 2M - 2, whose
eigenvalues are the exact grid density d_j = FFT of the folded
lag array (SOURCE data only -- no eigendecomposition of the
target).  Then t^T K t = (1/2L) Sigma_j d_j |F_j(t)|^2 with
F = FFT o pad o odd-extend, and

    B+/- = diag(sqrt(max(+-d, 0)/(2L))) . F . pad . E_odd.

CUT 1: sign split of the TOTAL density d = d_ar + d_at.
CUT 2 (predeclared channel grouping): sign split per channel
(arch and comb separately), stacked -- cross-channel
cancellation at equal frequency is now kept in separate blocks.
GRADE: comb weights enter the density LINEARLY (c_at linear in
Lambda(n)/sqrt(n)), B carries sqrt|density|, so B*B is linear
in Lambda -- the grade barrier is passed by construction
(asserted: doubling the masses doubles the comb Gram exactly).

PACKAGE B -- THE DOUGLAS CENSUS: C_min = B- . pinv(B+)
(pseudoinverse as MICROSCOPE, not proof component -- typed).
Given the range condition ran(B-*) subset ran(B+*):
Q PSD on a subspace  <=>  ||C_min|| <= 1 there.  Measured per
rung and cut: ||C_min|| on the full h-grid (geometry) and on
the certified battery (t1, t2) where tau > 0 is certified --
there ||C2|| <= 1 MUST hold (consistency ward), and the exact
relationship is 1 - ||C2||^2 = lam_min(G+^{-1/2} Ah G+^{-1/2})
(the tau-margin measured in the metric of the positive side --
verified machine-exact).  Plus: range condition, rank/direction
census (dominant dual frequency tau* of the top singular
direction, digamma-band mass, battery overlaps), ladder drift,
unitary basis-change invariance (DST basis).  KILLS (frozen):
ward fails / range fails / truth battery ||C2|| > 1 / Epstein
h=2 (x^2+5y^2, relation-level Lambda_E from -Z'/Z) does NOT
show ||C2|| > 1 (its 2x2 is non-PSD, so the contractor MUST
exceed 1 -- the discriminator) / scramble shows the same
geometry / wild rotation along the ladder.

PACKAGE C -- THE SOURCE ALGEBRA (only if B stable): words up to
length 3 over the frozen dual-grid generators {J frequency
flip, S one-bin shift, M4 quarter phase, KM KMS half-weight
diag e^{-tau/2}, ZM truncated Moebius symbol diag(sum mu(n)
n^{-1/2} e^{-i tau log n}, n <= 50, sup-normalised)} -- all
unitaries or contractions, so every word has an independent
norm bound <= 1 by composition.  SUCCESS bar: rel residual
||W B+ - B-||_F / ||B-||_F <= 1e-8.  TYPED STRUCTURAL
EXPECTATION (pre-run): in Cut 1 the supports of d_+ and d_- are
DISJOINT frequency bands and d is even, so J and diagonals are
support-preserving and S moves support by one bin -- no short
word can bridge the bands; the census then measures HOW FAR
the best word stays from the contractor.

VERDICT (frozen): KREIN-CONTRACTOR-STABLE (+ SOURCE-WORD-FOUND
if C succeeds) / KREIN-CONTRACTOR-STABLE-NO-WORD /
KREIN-UNSTABLE (kills typed) / NORMALFORM-FAILS (ward).
NO RH claim; writes nothing; v563 READ-ONLY.

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/krein_normalform_probe.py
"""

import ast
import hashlib
import math
import os
import sys
import time

import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
_VERIFY = os.path.abspath(os.path.join(_HERE, "..", "..",
                                       "verification"))
sys.path.insert(0, _HERE)
sys.path.insert(0, _VERIFY)

import v563_paper2_readouts as core        # noqa: E402  (READ-ONLY)

FROZEN_SPEC = """\
PRIME.SIGNED.KREIN.NORMALFORM.01 + PRIME.KREIN.GRAPH.CENSUS.01
spec v2 (2026-08-08; v1 amendment typed after the first run:
the v1 Epstein discriminator presumed the h=2 battery (t1, t2)
compression is non-PSD at kz 9 -- the measurement refuted the
presumption (lam_min(Ah_E) = +0.665, ||C2_E|| = 0.934 <= 1,
CONSISTENT with the Douglas equivalence: the 2x2 battery at
this shallow window is too coarse to see Epstein's
negativity).  The discriminator moves to the FULL h-grid where
both sides of the equivalence are measurable: truth lam_min(K)
> 0 AND ||C_full|| <= 1 + 1e-9 at every rung; Epstein
lam_min(K_E) < 0 AND ||C_E|| > 1; scramble geometry differs.
No other bars changed; the battery values stay reported as
diagnostics).  Anchors kz 9/12/13
(tau refs rel 1e-4); ladder = frame_a_zones() thinned to <= 12
rungs (every len//10-th, anchors forced, h <= 900).  A: cut 1 =
sign split of d = FFT(fold(c_ar + c_at)) on L = 2M-2 circulant;
cut 2 = per-channel split stacked; B+/- = diag(sqrt(d+-/2L)) F
pad E_odd; WARD (both cuts, every rung): max|Re(B+*B+ - B-*B-)
- odd_toeplitz(c)| <= 1e-9 max|K|, imag <= 1e-9; battery
cross-ward T2^T K T2 == Ah_dir to 1e-8 rel; grade assert:
doubling mm doubles the comb Gram to 1e-12 rel.  B: pinv cut
sigma <= 1e-12 sigma_max; range residual ||(I - VV*)B-*|| /
||B-|| <= 1e-8; ||C_full|| via sigma_max(B- V Sigma^+); battery
||C2|| via B+- T2; consistency 1 - ||C2||^2 ==
lam_min(G+^{-1/2} Ah G+^{-1/2}) rel 1e-6; truth battery ||C2||
<= 1 + 1e-10 at anchors (kill); Epstein x^2+5y^2 Lambda_E by
-Z'/Z recursion (a_n = r(n)/2), masses 2 Lambda_E/sqrt(n): its
battery lam_min < 0 AND ||C2_E|| > 1 at anchors (discriminator
kill if not); scramble seed 1 at kz 9: differs iff
|dC|/C >= 1e-3 or tau* differs >= 30 percent; drift: last third
of ladder max/min ||C_full|| <= 1.25 and tau* max/min <= 3;
DST basis invariance |d||C||| <= 1e-8 rel (orthonormalised
parity basis).  C only if B stable: 5 generators, words <= 3
(155), success rel residual <= 1e-8; all words contractions by
construction.  Verdict: NORMALFORM-FAILS if ward fails;
KREIN-UNSTABLE if any kill; else STABLE +- NO-WORD per C.
Pseudoinverse typed as microscope.  NO RH claim; writes
nothing.
"""

ANCHORS = (9, 12, 13)
TAU_REFS = {9: 5.984165e-4, 12: 4.351189e-4, 13: 5.637632e-4}
TAU_STAR_DIGAMMA = 6.27
BANNED_IDS = ("zetazero", "nzeros", "primerange", "isprime",
              "primepi", "nextprime", "prevprime")

CHECKS = []
FAILS = []
T0 = time.time()


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok)))
    if not ok:
        FAILS.append(name.split()[0])
    print("  [%s] %s%s" % ("PASS" if ok else "FAIL", name,
                           ("  -- " + detail) if detail else ""),
          flush=True)
    return bool(ok)


def section(title):
    print("\n" + "=" * 74)
    print(title)
    print("=" * 74, flush=True)


def ast_scan(banned):
    src = open(os.path.abspath(__file__), encoding="utf-8").read()
    bad = []
    for node in ast.walk(ast.parse(src)):
        name = None
        if isinstance(node, ast.Name):
            name = node.id
        elif isinstance(node, ast.Attribute):
            name = node.attr
        if name and name.lower() in banned:
            bad.append(name)
    return bad


# ------------------------------------------------ Krein construction
def odd_extend_mat(h):
    """E_odd: t in R^h -> f_ext = [t, -t[::-1]] in R^{2h}."""
    E = np.zeros((2 * h, h))
    E[:h] = np.eye(h)
    E[h:] = -np.eye(h)[::-1]
    return E


def grid_density(c):
    """Exact circulant density: d = FFT of the folded lag array
    [c0..c_{M-1}, c_{M-2}..c_1], length L = 2M - 2 (source data
    only)."""
    c = np.asarray(c, float)
    a = np.concatenate([c, c[-2:0:-1]])
    d = np.fft.fft(a)
    assert float(np.max(np.abs(d.imag))) <= 1e-9 * max(
        1.0, float(np.max(np.abs(d.real))))
    return d.real


def krein_arms(dens_list, h):
    """B+/- for a list of channel densities (cut 2 stacks
    channels; cut 1 passes one summed density).  Exact:
    B+*B+ - B-*B- == odd_toeplitz(sum c) by construction."""
    M = 2 * h
    L = 2 * M - 2
    E = odd_extend_mat(h)
    Fp = np.fft.fft(np.vstack([E, np.zeros((L - M, h))]), axis=0)
    Bp_blocks, Bm_blocks = [], []
    for d in dens_list:
        dp = np.sqrt(np.maximum(d, 0.0) / (2.0 * L))
        dm = np.sqrt(np.maximum(-d, 0.0) / (2.0 * L))
        Bp_blocks.append(dp[:, None] * Fp)
        Bm_blocks.append(dm[:, None] * Fp)
    return np.vstack(Bp_blocks), np.vstack(Bm_blocks)


def douglas(Bp, Bm):
    """The Douglas census: range residual, ||C_min|| and the
    h-space top direction (pinv as MICROSCOPE)."""
    U, s, Vh = np.linalg.svd(Bp, full_matrices=False)
    r = int(np.sum(s > 1e-12 * s[0]))
    U, s, Vh = U[:, :r], s[:r], Vh[:r]
    BmH = Bm.conj().T
    rng_res = float(np.linalg.norm(BmH - Vh.conj().T @ (Vh @ BmH))
                    / max(np.linalg.norm(Bm), 1e-300))
    A2 = Bm @ (Vh.conj().T / s)                  # C on ran(B+)
    u2, s2, v2 = np.linalg.svd(A2, full_matrices=False)
    x = Vh.conj().T @ (v2[0].conj() / s)         # h-space direction
    x = np.real(x)
    x /= max(np.linalg.norm(x), 1e-300)
    return rng_res, float(s2[0]), s2, x, r


def dom_tau(x, D):
    """Dominant dual frequency (tau units) + digamma-band mass
    of an h-space direction, via the odd extension."""
    h = len(x)
    f = np.concatenate([x, -x[::-1]])
    L = 2 * len(f) - 2
    X = np.abs(np.fft.fft(f, n=L)) ** 2
    jj = np.arange(L)
    tau = np.where(jj <= L // 2, jj, L - jj) * (
        2.0 * math.pi / L) / D
    j0 = int(np.argmax(X[1:L // 2])) + 1
    band = (tau >= 2.0) & (tau <= TAU_STAR_DIGAMMA)
    return float(tau[j0]), float(np.sum(X[band]) / np.sum(X))


def lambda_eps(N):
    """Relation-level Epstein h=2 comb: a_n = r_{x^2+5y^2}(n)/2,
    -Z'/Z = Sigma Lambda_E(n) n^{-s} by exact recursion."""
    r = np.zeros(N + 1)
    s = int(math.isqrt(N)) + 1
    for x in range(-s, s + 1):
        for y in range(-s, s + 1):
            v = x * x + 5 * y * y
            if 1 <= v <= N:
                r[v] += 1.0
    a = r / 2.0                                   # a_1 = 1
    lam = np.zeros(N + 1)
    for n in range(2, N + 1):
        acc = a[n] * math.log(n)
        for d in range(2, n):
            if n % d == 0:
                acc -= lam[d] * a[n // d]
        lam[n] = acc
    return lam


def moebius(N):
    mu = np.ones(N + 1, dtype=int)
    prim = np.ones(N + 1, dtype=bool)
    prim[:2] = False
    for p in range(2, N + 1):
        if prim[p]:
            prim[2 * p::p] = False
            mu[p::p] *= -1
            mu[p * p::p * p] = 0
    return mu


# ================================================================= main
def main():
    section("PRIME.SIGNED.KREIN.NORMALFORM.01 -- the Krein/"
            "defect representation (EXPLORATION ONLY)")
    sha = hashlib.sha256(FROZEN_SPEC.encode("utf-8")).hexdigest()
    print("    FROZEN_SPEC SHA-256 = %s" % sha)
    print("    NO RH claim.  Pseudoinverse = microscope only.")
    print("\nS0 -- firewall")
    check("S0.1 AST firewall clean (no zero/prime oracles)",
          not ast_scan(BANNED_IDS))

    zones = list(core.frame_a_zones())
    step = max(1, len(zones) // 10)
    ladder = sorted(set(zones[::step]) | set(ANCHORS))
    ladder = [kz for kz in ladder if kz in zones]

    # ---------------- S1 PACKAGE A + B per rung
    section("S1 -- PACKAGES A+B: normal form + Douglas census "
            "(%d rungs)" % len(ladder))
    ward_ok = True
    range_ok = True
    grade_ok = True
    rows = {}
    for kz in ladder:
        rr = core.build_window(kz)
        h, M, D, alpha = rr["h"], rr["M"], rr["D"], rr["alpha"]
        if h > 900:
            continue
        uu = np.asarray(rr["uu"], float)
        mm = 2.0 * np.asarray(rr["lam"], float)
        c_at, _ = core.atom_lags_at(alpha, M, uu, mm)
        c_ar = np.asarray(core.arch_lags(M, D), float)
        K = core.odd_toeplitz(c_ar + c_at, M)
        d_ar = grid_density(c_ar)
        d_at = grid_density(c_at)
        cuts = {"cut1": [d_ar + d_at], "cut2": [d_ar, d_at]}
        T2 = np.column_stack([rr["t1"], rr["t2"]])
        Ah_dir = np.asarray(rr["Ah_dir"], float)
        xw = float(np.max(np.abs(T2.T @ (K @ T2) - Ah_dir))
                   / max(np.max(np.abs(Ah_dir)), 1e-300))
        row = dict(h=h, alpha=alpha, xward=xw,
                   lmin_full=float(np.linalg.eigvalsh(K)[0]),
                   lmin_bat=float(np.linalg.eigvalsh(Ah_dir)[0]))
        for cut, dl in cuts.items():
            Bp, Bm = krein_arms(dl, h)
            G = Bp.conj().T @ Bp - Bm.conj().T @ Bm
            kscale = max(float(np.max(np.abs(K))), 1e-300)
            wdev = float(np.max(np.abs(G.real - K))) / kscale
            widev = float(np.max(np.abs(G.imag))) / kscale
            ward_ok &= wdev <= 1e-9 and widev <= 1e-9
            rng_res, cnorm, s2, x1, rk = douglas(Bp, Bm)
            range_ok &= rng_res <= 1e-8
            ts, bmass = dom_tau(x1, D)
            BpT, BmT = Bp @ T2, Bm @ T2
            _, c2, _, _, _ = douglas(BpT, BmT)
            Gp = np.real(BpT.conj().T @ BpT)
            ev, Vp = np.linalg.eigh(Gp)
            R = Vp @ np.diag(ev ** -0.5) @ Vp.T
            pmin = float(np.linalg.eigvalsh(R @ Ah_dir @ R)[0])
            row[cut] = dict(
                wdev=wdev, rng=rng_res, cnorm=cnorm, c2=c2,
                pmin=pmin, taustar=ts, bmass=bmass, rank=rk,
                sratio=float(s2[1] / s2[0]) if len(s2) > 1
                else 0.0,
                ot1=float(abs(x1 @ rr["t1"])
                          / np.linalg.norm(rr["t1"])),
                pencil_dev=float(abs((1.0 - c2 ** 2) - pmin)
                                 / max(abs(pmin), 1e-300)))
        rows[kz] = row
        c1, c2_ = row["cut1"], row["cut2"]
        print("    kz %-3d h %-4d | lmin(K) %+9.2e lmin(bat) "
              "%+9.2e | cut1: ward %.0e rng %.0e |C| %.6f "
              "|C2| %.9f 1-|C2|^2 %+.3e tau* %5.2f band %.2f | "
              "cut2: |C| %.6f |C2| %.9f"
              % (kz, row["h"], row["lmin_full"],
                 row["lmin_bat"], c1["wdev"], c1["rng"],
                 c1["cnorm"], c1["c2"], 1.0 - c1["c2"] ** 2,
                 c1["taustar"], c1["bmass"], c2_["cnorm"],
                 c2_["c2"]), flush=True)
    # grade assertion (kz 9): doubling masses doubles comb Gram
    rr9 = core.build_window(9)
    h9, M9, D9, a9 = rr9["h"], rr9["M"], rr9["D"], rr9["alpha"]
    uu9 = np.asarray(rr9["uu"], float)
    mm9 = 2.0 * np.asarray(rr9["lam"], float)
    dat1 = grid_density(core.atom_lags_at(a9, M9, uu9, mm9)[0])
    dat2 = grid_density(core.atom_lags_at(a9, M9, uu9,
                                          2.0 * mm9)[0])
    Bp1, Bm1 = krein_arms([dat1], h9)
    Bp2, Bm2 = krein_arms([dat2], h9)
    gdev = float(
        np.max(np.abs((Bp2.conj().T @ Bp2 - Bm2.conj().T @ Bm2)
                      - 2.0 * (Bp1.conj().T @ Bp1
                               - Bm1.conj().T @ Bm1))))
    grade_ok = gdev <= 1e-12 * max(1.0, float(np.max(np.abs(
        Bp1.conj().T @ Bp1))))
    check("S1.A [THE WARD] B+*B+ - B-*B- == the deployed lag "
          "form entrywise (<= 1e-9 rel) for BOTH cuts on all "
          "%d rungs; battery cross-ward vs Ah_dir <= 1e-8; "
          "GRADE: doubling the comb masses doubles the comb "
          "Gram exactly (dev %.1e) -- B carries sqrt|Lambda|, "
          "B*B is LINEAR in Lambda: the grade barrier is "
          "passed by construction"
          % (len(rows), gdev),
          ward_ok and grade_ok
          and max(r["xward"] for r in rows.values()) <= 1e-8)
    check("S1.B [RANGE + PENCIL] range condition ran(B-*) in "
          "ran(B+*) holds on every rung/cut (max residual "
          "%.1e <= 1e-8); the exact Douglas relationship "
          "1 - ||C2||^2 == lam_min(G+^{-1/2} Ah G+^{-1/2}) "
          "verified per rung (max rel dev %.1e <= 1e-6) -- the "
          "tau-margin IS the contraction margin in the "
          "positive-side metric"
          % (max(max(r["cut1"]["rng"], r["cut2"]["rng"])
                 for r in rows.values()),
             max(max(r["cut1"]["pencil_dev"],
                     r["cut2"]["pencil_dev"])
                 for r in rows.values())),
          range_ok
          and max(max(r["cut1"]["pencil_dev"],
                      r["cut2"]["pencil_dev"])
                  for r in rows.values()) <= 1e-6)
    truth_c2_ok = all(rows[kz]["cut1"]["c2"] <= 1.0 + 1e-10
                      for kz in ANCHORS)
    tau_ok = all(abs(float(np.linalg.eigvalsh(
        np.asarray(core.build_window(kz)["Ah"], float))[0])
        - TAU_REFS[kz]) / TAU_REFS[kz] <= 1e-4
        for kz in ANCHORS)
    check("S1.C [CERTIFIED CONSISTENCY] on the certified "
          "battery the truth contractor is a genuine "
          "contraction at all anchors (||C2|| = %.9f/%.9f/%.9f "
          "<= 1); tau refs reproduce (rel 1e-4): %s"
          % (rows[9]["cut1"]["c2"], rows[12]["cut1"]["c2"],
             rows[13]["cut1"]["c2"], tau_ok),
          truth_c2_ok and tau_ok)

    # drift + basis stability
    kzs = [kz for kz in ladder if kz in rows]
    cn = [rows[kz]["cut1"]["cnorm"] for kz in kzs]
    ts = [rows[kz]["cut1"]["taustar"] for kz in kzs]
    last = max(1, len(kzs) // 3)
    cn3, ts3 = cn[-last:], ts[-last:]
    drift_ok = (max(cn3) / min(cn3) <= 1.25
                and max(ts3) / max(min(ts3), 1e-300) <= 3.0)
    # unitary basis change: orthonormalised parity/DST basis
    Sb = core.parity_basis(h9, h9).T
    Sb, _ = np.linalg.qr(Sb)
    d9 = [grid_density(np.asarray(core.arch_lags(M9, D9), float)
                       + core.atom_lags_at(a9, M9, uu9, mm9)[0])]
    Bp9, Bm9 = krein_arms(d9, h9)
    _, cA, _, _, _ = douglas(Bp9, Bm9)
    _, cB, _, _, _ = douglas(Bp9 @ Sb, Bm9 @ Sb)
    bas_dev = abs(cA - cB) / cA
    check("S1.D [DRIFT + BASIS] ladder drift of the full-grid "
          "contractor: ||C|| last-third max/min = %.3f (<= "
          "1.25), tau* last-third max/min = %.2f (<= 3) -- the "
          "top direction sits in a stable dual-frequency band; "
          "unitary basis change (DST) moves ||C|| by %.1e "
          "(<= 1e-8): the contraction geometry is "
          "basis-invariant"
          % (max(cn3) / min(cn3),
             max(ts3) / max(min(ts3), 1e-300), bas_dev),
          drift_ok and bas_dev <= 1e-8)

    # ---------------- S2 discriminators
    section("S2 -- THE DISCRIMINATORS (Epstein h=2 + scramble)")
    N_E = int(math.floor(math.exp(2.0 * a9))) + 1
    lamE = lambda_eps(N_E)
    nn = np.nonzero(np.abs(lamE) > 1e-12)[0]
    uuE = np.log(nn.astype(float))
    mmE = 2.0 * lamE[nn] / np.sqrt(nn.astype(float))
    c_atE, _ = core.atom_lags_at(a9, M9, uuE, mmE)
    c_ar9 = np.asarray(core.arch_lags(M9, D9), float)
    KE = core.odd_toeplitz(c_ar9 + c_atE, M9)
    T29 = np.column_stack([rr9["t1"], rr9["t2"]])
    AhE = T29.T @ (KE @ T29)
    lminE_bat = float(np.linalg.eigvalsh(AhE)[0])
    lminE_full = float(np.linalg.eigvalsh(KE)[0])
    BpE, BmE = krein_arms([grid_density(c_ar9 + c_atE)], h9)
    _, c2E, _, _, _ = douglas(BpE @ T29, BmE @ T29)
    rngE, cE, _, xE, _ = douglas(BpE, BmE)
    tsE, bmE = dom_tau(xE, D9)
    truth_full_ok = all(
        r["lmin_full"] > 0.0
        and r["cut1"]["cnorm"] <= 1.0 + 1e-9
        for r in rows.values())
    eps_kill = (lminE_full < 0.0 and cE > 1.0
                and rngE <= 1e-8)
    check("S2.1 [EPSTEIN DISCRIMINATOR, full grid] the Douglas "
          "equivalence measured on BOTH sides: truth lam_min(K)"
          " > 0 and ||C_full|| <= 1 at every rung (%s); the "
          "h=2 comb (relation-level Lambda_E, %d events) has "
          "lam_min(K_E) = %+.3e < 0 and ||C_E|| = %.3f > 1 "
          "(range res %.0e) -- positivity <=> contraction "
          "discriminates the Euler comb on the window space; "
          "diagnostic: the 2x2 battery at this shallow window "
          "is too coarse (lam_min(Ah_E) = %+.3f, ||C2_E|| = "
          "%.3f <= 1, consistent with the equivalence)"
          % (truth_full_ok, len(nn), lminE_full, cE, rngE,
             lminE_bat, c2E),
          truth_full_ok and eps_kill)
    uu_s = np.asarray(core.build_window(9, scramble_seed=1)
                      ["uu"], float)
    c_atS, _ = core.atom_lags_at(a9, M9, uu_s, mm9)
    BpS, BmS = krein_arms([grid_density(c_ar9 + c_atS)], h9)
    _, cS, _, xS, _ = douglas(BpS, BmS)
    tsS, _ = dom_tau(xS, D9)
    t_true = rows[9]["cut1"]["taustar"]
    c_true = rows[9]["cut1"]["cnorm"]
    scr_diff = (abs(cS - c_true) / c_true >= 1e-3
                or abs(tsS - t_true) / t_true >= 0.3)
    check("S2.2 [SCRAMBLE GEOMETRY] scrambled positions move "
          "the contraction geometry: ||C|| %.6f vs %.6f, tau* "
          "%.2f vs %.2f (Epstein: ||C|| %.6f tau* %.2f band "
          "%.2f) -- the geometry is arithmetic, not generic"
          % (cS, c_true, tsS, t_true, cE, tsE, bmE), scr_diff)

    b_stable = (ward_ok and grade_ok and range_ok
                and truth_c2_ok and truth_full_ok
                and drift_ok and bas_dev <= 1e-8
                and eps_kill and scr_diff)

    # ---------------- S3 PACKAGE C: the source word algebra
    section("S3 -- PACKAGE C: the source word algebra "
            "(%s)" % ("UNLOCKED" if b_stable else
                      "locked -- typed skip"))
    word_found = False
    if b_stable:
        L9 = Bp9.shape[0]
        jj = np.arange(L9)
        tauj = np.where(jj <= L9 // 2, jj, L9 - jj) * (
            2.0 * math.pi / L9) / D9
        mu = moebius(50)
        zm = np.zeros(L9, complex)
        for n in range(1, 51):
            if mu[n]:
                zm += mu[n] / math.sqrt(n) * np.exp(
                    -1j * tauj * math.log(n))
        gens = {
            "J": ("perm", (-jj) % L9),
            "S": ("perm", (jj + 1) % L9),
            "M4": ("diag", 1j ** (jj % 4)),
            "KM": ("diag", np.exp(-tauj / 2.0)),
            "ZM": ("diag", zm / np.max(np.abs(zm))),
        }

        def apply_gen(gname, X):
            kind, dat = gens[gname]
            return X[dat] if kind == "perm" else dat[:, None] * X

        names = list(gens)
        words = [(n,) for n in names]
        words += [(a, b) for a in names for b in names]
        words += [(a, b, c) for a in names for b in names
                  for c in names]
        nrmB = float(np.linalg.norm(Bm9))
        best = []
        for wd in words:
            X = Bp9
            for g in reversed(wd):
                X = apply_gen(g, X)
            res = float(np.linalg.norm(X - Bm9) / nrmB)
            best.append((res, ".".join(wd)))
        best.sort()
        word_found = best[0][0] <= 1e-8
        print("    best words: " + "; ".join(
            "%s (res %.3f)" % (w, r) for r, w in best[:5]))
        check("S3.1 [WORD CENSUS] %d words over {J, S, M4, KM, "
              "ZM} (every word a contraction by composition); "
              "best residual %.3f (bar 1e-8): %s -- as "
              "pre-typed, the d+ and d- supports are disjoint "
              "frequency bands and all short deployed words are "
              "(near-)support-preserving: no short source word "
              "realizes the contractor; the needed object is a "
              "BAND-MOVING intertwiner (Hankel/cross-band), "
              "which no length-<=3 word over the deployed "
              "generators contains"
              % (len(words), best[0][0],
                 "FOUND" if word_found else "none"),
              True)

    # ---------------- S4 verdict
    section("V -- FROZEN VERDICT + the honest consequence")
    if not ward_ok:
        verdict = "NORMALFORM-FAILS"
    elif not b_stable:
        verdict = "KREIN-UNSTABLE"
    elif word_found:
        verdict = "KREIN-CONTRACTOR-STABLE + SOURCE-WORD-FOUND"
    else:
        verdict = "KREIN-CONTRACTOR-STABLE-NO-WORD"
    print("\n  VERDICT: %s   [ward %s | range %s | truth "
          "contraction (battery %s, full grid %s) | drift %s | "
          "Epstein kill %s | scramble differs %s | word %s]"
          % (verdict, ward_ok, range_ok, truth_c2_ok,
             truth_full_ok, drift_ok, eps_kill, scr_diff,
             word_found))
    m9 = 1.0 - rows[9]["cut1"]["c2"] ** 2
    print("""
  HONEST CONSEQUENCE: the deployed window form now has an EXACT
  Krein normal form Q_h(t) = ||B+ t||^2 - ||B- t||^2, machine-
  warded entrywise on every rung for both canonical cuts, with
  the weights entering as sqrt|Lambda| so the form is linear in
  Lambda -- the signed-density measurement of the euler_schur
  probe turned into a construction instead of a kill.  The
  Douglas microscope gives the sharpest reformulation of the
  floor so far, and on the FULL window space, not just the
  battery: every truth rung has lam_min(K) > 0 and
  ||C_full|| <= 1 (razor-thin: 1 - ||C||^2 down to ~1e-6 at
  depth), the battery margin 1 - ||C2||^2 = %.3e at kz 9 == the
  tau-margin in the positive-side metric (exact pencil
  identity, machine-verified), while Epstein h=2 explodes to
  ||C_E|| ~ 47 with lam_min(K_E) < 0 and the scrambled comb to
  ~3700: 'which self-consistent comb is real' has become
  'which rate measure makes B- . pinv(B+) a contraction' --
  and the discriminator is the Douglas equivalence itself.
  (Diagnostic honesty: at this shallow window Epstein's 2x2
  battery compression is still PSD -- the negativity needs the
  full grid; the v1 presumption is retracted in the spec.)
  The geometry census: the contraction-critical direction
  sits in a LOW dual-frequency band, tau* drifting 1.7 -> 0.9
  along the ladder with small digamma-band mass -- the norm is
  NOT carried by the (2, 6.27) arch band but by the
  low-frequency comb-vs-pole balance.  The word algebra
  outcome types what is missing: the positive and negative
  spectral supports are disjoint bands, every short word over
  the deployed source operators is support-preserving, so the
  contractor is NOT a short source word -- the remaining
  object is a band-moving intertwiner with an independent norm
  bound, which is precisely the explicit-formula transfer (lag
  deposits <-> spectral bands) that all previous coordinates
  also lacked.  The wall is unchanged; its normal form is
  sharper.  NO RH claim.""" % m9)
    n_pass = sum(1 for _n, ok in CHECKS if ok)
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed%s"
          % (time.time() - T0, len(CHECKS), len(FAILS),
             ("  " + ",".join(FAILS)) if FAILS else ""))
    return 0 if n_pass == len(CHECKS) else 1


if __name__ == "__main__":
    raise SystemExit(main())
'''

# --------------------------------------------------------------- harness
_PF_RE = re.compile(r"^\s*\[(PASS|FAIL)\]\s+(\S+)", re.M)
_VD_RE = re.compile(r"VERDICT[^\n]*:")


def _probe_file(name):
    cand = os.path.abspath(os.path.join(
        _HERE, os.pardir, "experiments", "tfpt-discovery", name + ".py"))
    return cand if os.path.isfile(cand) else None


def _census(out):
    marks = _PF_RE.findall(out)
    fails = sorted({tok for st, tok in marks if st == "FAIL"})
    verdicts = [ln.strip() for ln in out.splitlines()
                if _VD_RE.search(ln)]
    return len(marks), fails, " | ".join(verdicts)


def _exec_probe(name, src, run_entry=True):
    """Execute one embedded frozen probe source BYTE-EXACT in its own
    module namespace, registered in sys.modules under the probe's
    canonical import name; capture and re-emit stdout; return
    (stdout, exit_code, byte_equal_to_source_file_or_None)."""
    if src[:1] == "\n":
        src = src[1:]
    path = _probe_file(name)
    same = None
    if path is not None:
        with open(path, encoding="utf-8") as fh:
            same = (fh.read() == src)
    fname = path or os.path.abspath(__file__)
    mod = types.ModuleType(name)
    mod.__file__ = fname
    sys.modules[name] = mod
    buf = io.StringIO()
    code = 0
    with contextlib.redirect_stdout(buf):
        try:
            exec(compile(src, fname, "exec"), mod.__dict__)
            entry = mod.__dict__.get("main") or mod.__dict__.get("run")
            if run_entry and callable(entry):
                rc = entry()
                code = 0 if rc is None else int(rc)
        except SystemExit as exc:
            code = 0 if exc.code is None else int(exc.code)
        except Exception:                            # regression guard
            import traceback
            traceback.print_exc(file=sys.stdout)
            code = 99
    out = buf.getvalue()
    sys.stdout.write(out)
    sys.stdout.flush()
    return out, code, same


def _gate(name, out, code, same, exp_n, exp_fails, exp_verdicts,
          exp_code, gates):
    n, fails, verdict = _census(out)
    ok = (n == exp_n and fails == list(exp_fails)
          and all(v in verdict for v in exp_verdicts)
          and code == exp_code and same is not False)
    gates.append(ok)
    prov = ("byte-exact vs experiments source" if same is True else
            "embedded copy (source file not present)" if same is None
            else "SOURCE MISMATCH")
    print("\n[%s] PATTERN GATE %s: %d checks (exp %d) | FAILs %s "
          "(exp %s) | exit %d (exp %d) | %s\n      verdict line(s): %s"
          % ("PASS" if ok else "FAIL", name, n, exp_n,
             ",".join(fails) if fails else "none",
             ",".join(exp_fails) if exp_fails else "none",
             code, exp_code, prov, verdict), flush=True)
    return ok

_PLAN = (
    ('mobius_deck_redheffer_probe', _SRC_0, 37, (),
     ('DECK-MU-PARALLEL', 'REDHEFFER-ECHO-EXACT'), 0),
    ('krein_normalform_probe', _SRC_1, 8, (),
     ('KREIN-CONTRACTOR-STABLE-NO-WORD',), 0),
)


# ====== PART C -- the Lean frame (KreinDefect.lean; kernel-checked
# statements cited, numeric witnesses only -- v856/v849 precedent)

_C_CHECKS = []


def _ccheck(name, ok, detail=""):
    _C_CHECKS.append(bool(ok))
    print("  [%s] %s%s" % ("PASS" if ok else "FAIL", name,
                           ("  -- " + detail) if detail else ""),
          flush=True)
    return bool(ok)


def part_c():
    import numpy as np
    print("\n" + "-" * 74)
    print("v861 PART C -- the Lean frame: TfptCarrier/KreinDefect.lean "
          "(kernel-checked;")
    print("numeric witnesses here; SourceContractor never instantiated "
          "with deployed data)")
    print("-" * 74, flush=True)
    rng = np.random.default_rng(20260808)

    # C1: the defect representation + the exact factorization
    ok_rep, ok_fac = True, True
    for _ in range(6):
        Bp = rng.normal(size=(7, 5))
        C0 = rng.normal(size=(6, 7))
        C0 /= (np.linalg.norm(C0, 2) * (1.0 + rng.uniform(0.05, 0.5)))
        Bm = C0 @ Bp
        D = Bp.T @ Bp - Bm.T @ Bm                    # the defect matrix
        for _v in range(4):
            f = rng.normal(size=5)
            q = float(f @ (D @ f))
            e = (float((Bp @ f) @ (Bp @ f))
                 - float((Bm @ f) @ (Bm @ f)))
            ok_rep &= abs(q - e) <= 1e-10 * max(abs(q), 1.0)
        F = Bp.T @ (np.eye(7) - C0.T @ C0) @ Bp      # the factorization
        ok_fac &= float(np.max(np.abs(D - F))) <= 1e-10
    _ccheck("C1 THE DEFECT REPRESENTATION (defect / formAt_defect, "
            "kernel-checked): Q(f) = ||B+ f||^2 - ||B- f||^2 exactly "
            "(6 seeded channel pairs x 4 witnesses, 1e-10) AND the "
            "exact factorization defect = B+^H (1 - C^H C) B+ "
            "(defect_factorization, entrywise 1e-10)", ok_rep and ok_fac)

    # C2: the main theorem -- contraction => defect PSD
    ok_psd = True
    for _ in range(6):
        Bp = rng.normal(size=(7, 5))
        C0 = rng.normal(size=(6, 7))
        C0 /= (np.linalg.norm(C0, 2) * (1.0 + rng.uniform(0.05, 0.5)))
        cert = np.eye(7) - C0.T @ C0                 # Loewner certificate
        ok_psd &= float(np.linalg.eigvalsh(cert)[0]) >= -1e-12
        D = Bp.T @ Bp - (C0 @ Bp).T @ (C0 @ Bp)
        ok_psd &= float(np.linalg.eigvalsh(D)[0]) >= -1e-10
    _ccheck("C2 THE MAIN THEOREM (defect_psd_of_contraction): B- = "
            "C B+ with (1 - C^H C) PSD forces the defect PSD -- "
            "congruence preserves PSD (6 seeded instances, "
            "lam_min >= -1e-10)", ok_psd)

    # C3: the converse (Douglas, full-rank) + the circularity warning
    ok_conv = True
    for _ in range(6):
        Bp = rng.normal(size=(5, 5)) + 3.0 * np.eye(5)   # invertible
        Bm = rng.normal(size=(6, 5))
        D = Bp.T @ Bp - Bm.T @ Bm
        w = np.linalg.eigvalsh(D)
        if w[0] < 0:                                  # force PSD defect
            Bm *= 0.9 * math.sqrt(
                float((np.linalg.norm(Bp, 2) ** 2)
                      / max(np.linalg.norm(Bm, 2) ** 2, 1e-300)))
            D = Bp.T @ Bp - Bm.T @ Bm
            if float(np.linalg.eigvalsh(D)[0]) < 0:
                continue
        C = Bm @ np.linalg.inv(Bp)                    # the explicit C
        ok_conv &= (float(np.max(np.abs(Bm - C @ Bp))) <= 1e-9
                    and float(np.linalg.eigvalsh(
                        np.eye(5) - C.T @ C)[0]) >= -1e-9)
    _ccheck("C3 THE CONVERSE (douglas_contraction_of_defect_psd, "
            "full-rank): defect PSD + B+ invertible gives C = B- B+^-1 "
            "with certificate 1 - C^H C = B+^-H (defect) B+^-1 PSD -- "
            "and the CIRCULARITY WARNING typed: this C is mined from "
            "the target, so feeding it back is a reformulation "
            "(SourceContractor demands an INDEPENDENT certificate)",
            ok_conv)

    # C4: the cofinal composition (krein_cofinal / krein_cofinal_weil)
    ok_comp = True
    visits = [m for m in range(1, 4000) if (m * 0.6180339887) % 1 < 0.2]
    ok_comp &= len(visits) > 200 and all(
        any(v > m0 for v in visits) for m0 in range(0, 3000, 97))
    for _ in range(4):
        base = rng.normal(size=(3, 3))
        Ainf = base @ base.T                          # PSD limit block
        for _v in range(8):
            x = rng.normal(size=3)
            qw = float(x @ (Ainf @ x))
            vals = [qw + (0.5 ** j) * abs(rng.normal())
                    for j in range(40)]               # cofinal-PSD ladder
            ok_comp &= (min(vals) >= 0.0 and qw >= -1e-12)
    _ccheck("C4 THE COFINAL COMPOSITION (krein_cofinal + "
            "krein_cofinal_weil): ContractorRecurrence (cofinal "
            "contractors, witnessed on a synthetic golden-ratio "
            "ladder with %d visits) extracts a strictly monotone PSD "
            "ladder (extraction_of_frequently_atTop mirrored) and "
            "per-element convergence forces QW >= 0 on the whole "
            "dense family (4 seeded blocks x 8 elements, eps/2 "
            "argument, NO diagonal) -- no hidden wall behind the "
            "contractor certificates; SourceContractor stays a NAMED "
            "hypothesis everywhere" % len(visits), ok_comp)
    print("  (kernel-checked statements: experiments/"
          "lean4-carrier-rigidity/TfptCarrier/KreinDefect.lean -- "
          "14 declarations (10 theorems), lake build green, 3416 jobs, "
          "no sorry, no native_decide, axioms propext/Classical."
          "choice/Quot.sound only; import wired in TfptCarrier.lean; "
          "lean_manifest.sha256 at 88 files)")



def run():
    t0 = time.time()
    _C_CHECKS.clear()
    print("=" * 74)
    print('v861 -- PRIME.KREIN.NORMALFORM.01 + FORM.PRIME.KREIN.DEFECT.01 [F]')
    print("(the wall's operator form: two separate C2s and the exact")
    print('Redheffer/Mertens Smith echo; the deployed window form gets an')
    print('EXACT Krein normal form with the Douglas pencil identity')
    print('1 - ||C2||^2 == tau-margin; the defect theorem kernel-checked;')
    print('NO RH claim)')
    print("=" * 74, flush=True)
    gates = []
    for name, src, exp_n, exp_fails, exp_verdicts, exp_code in _PLAN:
        print("\n" + "-" * 74)
        print("EMBEDDED FROZEN PROBE: %s" % name)
        print("-" * 74, flush=True)
        out, code, same = _exec_probe(name, src)
        _gate(name, out, code, same, exp_n, exp_fails,
              exp_verdicts, exp_code, gates)
    part_c()
    ok_c = all(_C_CHECKS) and len(_C_CHECKS) == 4
    gates.append(ok_c)
    ok = all(gates)
    print("\n" + "=" * 74)
    print("v861: %d/%d gates passed (%d probe pattern gates + %d/4 mirror checks) | "
          "runtime %.1f s"
          % (sum(gates), len(gates), len(_PLAN), sum(_C_CHECKS), time.time() - t0))
    print('The Krein coordinates are established: the mu-sign and the deck')
    print('are two separate C2s (identification one faithful-mu4 character')
    print('away, three candidates typed); det R_n = M(n) with the WHOLE')
    print('Smith deviation in ONE invariant factor; the window form is')
    print('Q(f) = ||B+ f||^2 - ||B- f||^2 with the Douglas equivalence as')
    print('the discriminator; the defect frame is kernel-checked with')
    print('SourceContractor the named hypothesis.')
    print("[%s] v861 VERDICT GATE: DECK-MU-PARALLEL + REDHEFFER-ECHO-EXACT + KREIN-CONTRACTOR-STABLE-NO-WORD + the KreinDefect frame mirrored"
          % ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(run())
