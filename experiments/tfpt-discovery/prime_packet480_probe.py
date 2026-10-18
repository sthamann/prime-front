#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""prime_packet480_probe -- PRIME.PACKET480.01 (module 2 of the prime-channel
message round): is the pair Header(p) = (p mod 30, a_p mod 32) a canonical
7-bit packet header that ACTS on the E8 spinor block, or address arithmetic?

THE HYPOTHESIS (frozen before running, see FROZEN_SPEC below, SHA-256 printed
before any computation):
  *  Header(p) = (p mod 30, a_p mod 32) with a_p the eta-product coefficient
     of f_8 = eta(2 tau)^4 eta(4 tau)^4 (weight-4 level-8 newform,
     tfpt_prime_front.tex; a_3 = -4, a_5 = -2).  Via the check32 decoder
     p mod 32 = (a_p - 1)^3 mod 32 (recomputed HERE, independent of the
     parallel check32 worker) and CRT (480 = lcm(30, 32)) the header is
     equivalent to p mod 480.  phi(480) = 128 admissible classes
     = 8 x 16 = 3 + 4 bits.
  *  SHARP QUESTION: does (Z/480)^x (abelian, order 128) act CANONICALLY on
     the 128-root E8 spinor block (248 = 120 + 128, D8 half-spinor;
     v775 standard doubled model), intertwining the deployed structures
     (deck sigma, mu4 = J, chi_NSR)?
  *  KILL (frozen, the user's own bar): if no canonical intertwiner exists,
     the header stays address arithmetic and the 128 is a fingerprint,
     not a theorem.

VERDICT ENUM (frozen):
  PACKET480-INTERTWINED  = a canonical action exists with the predeclared
                           dictionary; the header is structural.
  PACKET480-ADDRESS-ONLY = no canonical intertwiner; the header is exact
                           address arithmetic, the 128 stays a fingerprint
                           (the honest expected outcome; kill fires).
  PACKET480-ILLDEFINED   = the CRT/decoder layer itself breaks.
  TEST-VOID              = a must-fire control does not fire.

FENCES (binding): NO semantic/message claims; the spinor block is used as a
ROOT SET only -- every matter-adjacent reading is killed at root level by
v775 (ARF.ROOTCLASS.01, verdict ROOTCLASS-MIXED) and stays fenced here.
Information accounting (P4) is a typed measurement [M], never a gate.

FIREWALL: exploration only (experiments/tfpt-discovery/); ONE new file;
writes nothing; touches no verification/, paper, ledger, changelog or
website surface.  Exact integer/F2 arithmetic in every load-bearing step
(numpy int64 with explicit mod, no floats in any decision); floats appear
only in the chi-square MEASUREMENT (P1.6) which is context, not a gate.
No RNG in any decision path (the scrambled control uses a FIXED seed).

Corpus sources (read-only):
  tfpt_prime_front.tex        f_8 = eta(2 tau)^4 eta(4 tau)^4, a_3=-4, a_5=-2
  verification/v223_...py     (Z/30)^x = E8 exponents, mu4 clock = <7 mod 30>
  verification/v775_...py     standard doubled E8 model: 128 spinor roots
                              (+-1)^8 with sum = 0 mod 4; J = pair rotation;
                              sigma = pair 3-cycle; ROOTCLASS-MIXED fence
  verification/v774_...py     chi_NSR = anchor bit; NS/R purity of classes
  verification/v702_...py     per-slot information demand g ~ 5-12 bits
                              (PRIME.Z1LOOKAHEAD.01, parameter-robust)

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/prime_packet480_probe.py
"""

import hashlib
import itertools
import math
import random
import time
from math import gcd

import numpy as np

T0 = time.time()

# ======================================================================
# frozen spec -- hashed BEFORE any root/prime data is computed
# ======================================================================
FROZEN_SPEC = """PRIME.PACKET480.01 FROZEN SPEC (2026-08-05, module 2)
HYPOTHESIS: Header(p) = (p mod 30, a_p mod 32) is a canonical 7-bit packet
header: CRT-equivalent to p mod 480 (480 = lcm(30,32), phi(480) = 128 =
8 x 16 = 3 + 4 bits); decoder p mod 32 = (a_p - 1)^3 mod 32 with a_p from
f_8 = eta(2 tau)^4 eta(4 tau)^4 (recomputed independently here).
SHARP QUESTION: does (Z/480)^x act canonically on the 128 E8 spinor roots
(248 = 120 + 128, v775 standard doubled model), intertwining deck sigma,
mu4 = J and chi_NSR?
CANDIDATE DICTIONARY (predeclared BEFORE the search; CRT generators of
(Z/480)^x = U32 x U3 x U5):
  D1  chi_{-4} direction (the square of the order-4 Coxeter part)
      -> J^2 = -1 on spinor roots (the Gaussian split/inert involution;
         subsumed by D2 if D2 holds)
  D2  mod-30 Coxeter order-4 part <7 mod 30> = CRT(2 mod 5) (v223: the mu4
      clock on the E8 exponents) -> mu4 = J (pair rotation, order 4)
  D3  mod-3 part CRT(2 mod 3) (order 2) -> the deck cycle sigma (order 3)
  D4  mod-32 Galois part CRT(3 mod 32) (order 8) -> a candidate of order 8
      from the mu4/level structure inside the deployed symmetry group
  D5  CRT(-1 mod 32) (order 2) -> the anchor-pair flip eps_{67} (the
      sigma-fixed pair (6,7) of the canonical sigma-stable split, v775)
A forced or arbitrary assignment counts as NO.
KILL (frozen): no canonical intertwiner => the header is address
arithmetic; the 128 is a fingerprint, not a theorem.
CONTROLS (must fire): (C1) the RIGHT group F2^7 must be detected as a
canonical torsor (harness positive control); (C2) a fixed-seed random
abelian group of order 128 with scrambled sub-characters must FAIL the
dictionary census; (C3) wrong moduli (28 or 36 instead of 30) must break
the CRT header (collision census), the true header has zero collisions.
VERDICTS: PACKET480-INTERTWINED / PACKET480-ADDRESS-ONLY /
PACKET480-ILLDEFINED / TEST-VOID."""

P_MAX = 100_000          # prime range 5 < p < P_MAX
MOD30, MOD32, MOD480 = 30, 32, 480
N_CLASSES = 128          # phi(480)
EXACT_XCHECK_N = 2000    # pure-python full-integer eta cross-check range

CHECKS = []
KILLS = []


def check(name, ok, detail="", kill=None):
    CHECKS.append((name, bool(ok)))
    if kill and not ok:
        KILLS.append(kill)
    print("[%s] %s%s" % ("PASS" if ok else "FAIL", name,
                         (" -- " + detail) if detail else ""), flush=True)
    return bool(ok)


def section(title):
    print("=" * 78)
    print(title)
    print("=" * 78, flush=True)


# ======================================================================
# small exact helpers
# ======================================================================
def sieve(n):
    bs = bytearray([1]) * (n + 1)
    bs[0:2] = b"\x00\x00"
    for i in range(2, int(n ** 0.5) + 1):
        if bs[i]:
            bs[i * i::i] = bytearray(len(bs[i * i::i]))
    return [i for i in range(2, n + 1) if bs[i]]


def pent_terms(scale, n_max):
    """sparse terms (exponent, sign) of prod_{m>=1}(1 - q^{scale*m}),
    generalized pentagonal number theorem, exponents <= n_max."""
    terms = [(0, 1)]
    k = 1
    while True:
        e1 = scale * (k * (3 * k - 1) // 2)
        e2 = scale * (k * (3 * k + 1) // 2)
        s = -1 if k % 2 else 1
        added = False
        for e in (e1, e2):
            if e <= n_max:
                terms.append((e, s))
                added = True
        if not added:
            break
        k += 1
    return terms


def eta_product_mod32(n_max):
    """a_n mod 32 of f_8 = q prod (1-q^{2m})^4 (1-q^{4m})^4, exact int64."""
    c = np.zeros(n_max + 1, dtype=np.int64)
    c[0] = 1
    for scale, power in ((2, 4), (4, 4)):
        terms = pent_terms(scale, n_max)
        for _ in range(power):
            out = np.zeros(n_max + 1, dtype=np.int64)
            for e, s in terms:
                if s == 1:
                    out[e:] += c[:n_max + 1 - e]
                else:
                    out[e:] -= c[:n_max + 1 - e]
            c = out % 32
    a = np.zeros(n_max + 1, dtype=np.int64)
    a[1:] = c[:n_max]          # prefactor q
    return a


def eta_product_exact(n_max):
    """full-integer a_n for n <= n_max (pure python, independent route)."""
    c = [0] * (n_max + 1)
    c[0] = 1
    for scale, power in ((2, 4), (4, 4)):
        terms = pent_terms(scale, n_max)
        for _ in range(power):
            out = [0] * (n_max + 1)
            for e, s in terms:
                if s == 1:
                    for i in range(e, n_max + 1):
                        out[i] += c[i - e]
                else:
                    for i in range(e, n_max + 1):
                        out[i] -= c[i - e]
            c = out
    a = [0] * (n_max + 1)
    a[1:] = c[:n_max]
    return a


def crt_pair(r30, r32):
    """unique x mod 480 with x = r30 (30), x = r32 (32), or None if
    inconsistent (gcd(30,32) = 2: needs equal parity)."""
    if r30 % 2 != r32 % 2:
        return None
    # 480 = lcm(30,32); solve by stepping through the 32-residue class
    for x in range(r32 % 32, MOD480, 32):
        if x % 30 == r30:
            return x
    return None


def perm_order(p):
    n = len(p)
    seen = [False] * n
    o = 1
    for i in range(n):
        if not seen[i]:
            ln, j = 0, i
            while not seen[j]:
                seen[j] = True
                j = p[j]
                ln += 1
            o = o * ln // gcd(o, ln)
    return o


def compose(p, q):
    """(p o q)(i) = p[q[i]]"""
    return tuple(p[i2] for i2 in q)


def subgroup_closure(gens, identity):
    G = {identity}
    frontier = [identity]
    while frontier:
        g = frontier.pop()
        for h in gens:
            ng = compose(h, g)
            if ng not in G:
                G.add(ng)
                frontier.append(ng)
    return G


def norm_cdf(z):
    return 0.5 * math.erfc(-z / math.sqrt(2.0))


def chi2_sf_wh(x, k):
    """Wilson-Hilferty survival approximation (measurement only)."""
    t = (x / k) ** (1.0 / 3.0)
    mu = 1.0 - 2.0 / (9.0 * k)
    sd = math.sqrt(2.0 / (9.0 * k))
    return 1.0 - norm_cdf((t - mu) / sd)


# ======================================================================
# P1 -- header well-definedness (CRT + check32 decoder + census)
# ======================================================================
def p1_header():
    section("P1: HEADER WELL-DEFINEDNESS -- CRT, check32 decoder, census")
    primes = [p for p in sieve(P_MAX - 1) if p > 5]
    n_pr = len(primes)
    print("    primes 5 < p < %d: %d" % (P_MAX, n_pr))

    # P1.1 structural CRT: (x mod 30, x mod 32) is injective on Z/480
    images = {(x % 30, x % 32) for x in range(MOD480)}
    ok_crt_struct = len(images) == MOD480
    recon_all = all(crt_pair(x % 30, x % 32) == x for x in range(MOD480))
    check("P1.1 CRT structural: x -> (x mod 30, x mod 32) injective on "
          "Z/480 and crt_pair inverts it (all 480 residues)",
          ok_crt_struct and recon_all, kill="ILLDEFINED")

    # P1.2 admissible pairs = phi(480) = 128 = 8 x 16 = 3 + 4 bits
    adm = [(r30, r32) for r30 in range(30) if gcd(r30, 30) == 1
           for r32 in range(32) if r32 % 2 == 1]
    ok_adm = (len(adm) == N_CLASSES
              and all(crt_pair(a, b) is not None
                      and gcd(crt_pair(a, b), MOD480) == 1 for a, b in adm))
    check("P1.2 admissible pairs: 8 x 16 = 128 = phi(480) = 2^(3+4); every "
          "pair CRT-consistent (both odd) and lands on a unit mod 480",
          ok_adm and math.log2(N_CLASSES) == 7.0, kill="ILLDEFINED")

    # P1.3 independent eta product a_p mod 32 + exact cross-check
    t = time.time()
    a32 = eta_product_mod32(P_MAX)
    a_exact = eta_product_exact(EXACT_XCHECK_N)
    ok_anchor = (a_exact[3] == -4 and a_exact[5] == -2)
    ok_xchk = all(a_exact[n] % 32 == int(a32[n])
                  for n in range(1, EXACT_XCHECK_N + 1))
    check("P1.3 a_p recomputed independently: exact route gives corpus "
          "anchors a_3 = -4, a_5 = -2 (tfpt_prime_front.tex); mod-32 route "
          "agrees with the exact route on all n <= %d" % EXACT_XCHECK_N,
          ok_anchor and ok_xchk,
          "eta pipeline %.1f s" % (time.time() - t), kill="ILLDEFINED")

    # P1.4 Hecke consistency mod 32 (newform structure, internal guard)
    odd_small = [p for p in primes if p * p <= P_MAX]
    ok_pp = all(int(a32[p * p]) == (int(a32[p]) ** 2 - p ** 3) % 32
                for p in odd_small)
    prs = [p for p in primes if p < 50]
    ok_mult = all(int(a32[p * q]) == (int(a32[p]) * int(a32[q])) % 32
                  for i, p in enumerate(prs) for q in prs[i + 1:]
                  if p * q <= P_MAX)
    check("P1.4 Hecke guard mod 32: a_{p^2} = a_p^2 - p^3 (all %d primes "
          "with p^2 < 1e5) and a_{pq} = a_p a_q (all pairs p < q < 50)"
          % len(odd_small), ok_pp and ok_mult, kill="ILLDEFINED")

    # P1.5 check32 decoder + full header pipeline on every prime
    ok_cong = all(int(a32[p]) == (1 + p ** 3) % 32 for p in primes)
    ok_dec = all(pow((int(a32[p]) - 1) % 32, 3, 32) == p % 32
                 for p in primes)
    ok_head = all(crt_pair(p % 30, pow((int(a32[p]) - 1) % 32, 3, 32))
                  == p % MOD480 for p in primes)
    check("P1.5 check32 decoder on ALL %d primes: a_p = 1 + p^3 (mod 32) "
          "(Eisenstein congruence), (a_p - 1)^3 = p (mod 32) (exponent of "
          "(Z/32)^x is 8: p^9 = p), and Header(p) -> CRT -> p mod 480 "
          "exact" % n_pr, ok_cong and ok_dec and ok_head, kill="ILLDEFINED")

    # P1.6 census of the 128 classes (measurement, not a gate)
    counts = {}
    for p in primes:
        counts[p % MOD480] = counts.get(p % MOD480, 0) + 1
    hit = len(counts)
    exp = n_pr / N_CLASSES
    chi2 = sum((counts.get(crt_pair(a, b), 0) - exp) ** 2 / exp
               for a, b in adm)
    pval = chi2_sf_wh(chi2, N_CLASSES - 1)
    cmin, cmax = min(counts.values()), max(counts.values())
    check("P1.6 [M] census: all 128 classes hit (%d/128); chi-square vs "
          "uniform Dirichlet expectation = %.1f (df = 127, WH p ~ %.3f); "
          "counts %d..%d around E = %.1f -- MEASUREMENT, not a gate"
          % (hit, chi2, pval, cmin, cmax, exp), hit == N_CLASSES)
    return primes, a32


# ======================================================================
# P2 -- exact group structure of (Z/480)^x
# ======================================================================
def crt480(r32, r3, r5):
    for x in range(MOD480):
        if x % 32 == r32 and x % 3 == r3 and x % 5 == r5:
            return x
    raise AssertionError("CRT lift failed")


def mult_order(g, mod):
    x, k = g % mod, 1
    while x != 1:
        x = (x * g) % mod
        k += 1
    return k


def p2_group():
    section("P2: (Z/480)^x EXACT -- invariant factors, exponent, "
            "sub-characters")
    units = [u for u in range(MOD480) if gcd(u, MOD480) == 1]
    orders = {u: mult_order(u, MOD480) for u in units}
    expo = max(orders.values())
    check("P2.1 |(Z/480)^x| = %d = 2^7, exponent = %d" % (len(units), expo),
          len(units) == 128 and expo == 8)

    # explicit CRT generators (frozen in the spec)
    g32a = crt480(31, 1, 1)   # -1 mod 32
    g32b = crt480(3, 1, 1)    # 3 mod 32, order 8 (Galois/mod-32 part)
    g3 = crt480(1, 2, 1)      # 2 mod 3
    g5 = crt480(1, 1, 2)      # 2 mod 5 -> reduces to 7 mod 30 (v223 clock)
    gens = (g32a, g32b, g3, g5)
    gen_orders = tuple(orders[g] for g in gens)
    prods = {(pow(g32a, i, MOD480) * pow(g32b, j, MOD480)
              * pow(g3, k, MOD480) * pow(g5, l, MOD480)) % MOD480
             for i in range(2) for j in range(8)
             for k in range(2) for l in range(4)}
    check("P2.2 direct product: <-1 mod 32> x <3 mod 32> x <2 mod 3> x "
          "<2 mod 5> with orders %s = (2, 8, 2, 4) hits all 128 units "
          "bijectively => elementary divisors {2, 8, 2, 4}, INVARIANT "
          "FACTORS Z2 x Z2 x Z4 x Z8" % (gen_orders,),
          gen_orders == (2, 8, 2, 4) and prods == set(units))

    # order-counting cross-check of the abelian type
    n2 = sum(1 for u in units if pow(u, 2, MOD480) == 1)
    n4 = sum(1 for u in units if pow(u, 4, MOD480) == 1)
    check("P2.3 order counting confirms the type: #\\{x^2=1\\} = %d = 16 "
          "(2-rank 4), #\\{x^4=1\\} = %d = 64, #\\{x^8=1\\} = 128 -- "
          "unique abelian type Z2^2 x Z4 x Z8" % (n2, n4),
          n2 == 16 and n4 == 64)

    # natural sub-characters
    chi_m4 = {u: 1 if u % 4 == 1 else -1 for u in units}
    chi_8 = {u: 1 if u % 8 in (1, 7) else -1 for u in units}
    chi_3 = {u: 1 if u % 3 == 1 else -1 for u in units}
    chi_5 = {u: 1 if u % 5 in (1, 4) else -1 for u in units}
    quads = [chi_m4, chi_8, chi_3, chi_5]
    ok_hom = all(all(ch[(u * v) % MOD480] == ch[u] * ch[v]
                     for u in units[:16] for v in units[:16])
                 for ch in quads)
    # independence: the 4 quadratic characters generate F2^4 (16 sign rows)
    sigrows = {tuple(ch[u] for ch in quads) for u in units}
    check("P2.4 natural sub-characters: chi_-4, chi_8 (mod-32 part), chi_3, "
          "chi_5 (mod-30 Coxeter part) are multiplicative and independent: "
          "%d distinct sign patterns = 16 = |(Z/480)^x / squares| = 2^4"
          % len(sigrows), ok_hom and len(sigrows) == 16)

    ok_cox = (g5 % 30 == 7 and mult_order(7, 30) == 4)
    check("P2.5 the mod-30 Coxeter part: CRT(2 mod 5) reduces to 7 mod 30, "
          "the order-4 mu4 clock on the E8 exponents (v223); "
          "(Z/30)^x = {1,7,11,13,17,19,23,29} = E8 exponents",
          ok_cox and [u for u in range(30) if gcd(u, 30) == 1]
          == [1, 7, 11, 13, 17, 19, 23, 29])
    print("    NOTE [M]: |(Z/480)^x / squares| = 16 = |V| (the Gaussian "
          "quotient F2^4 of v752/v774) -- cardinality observation only, "
          "typed as numerology unless an intertwiner exists (P3).")
    return dict(units=units, orders=orders, gens=gens,
                gen_orders=gen_orders)


# ======================================================================
# P3 -- the intertwiner search on the 128 E8 spinor roots (THE DECIDER)
# ======================================================================
def p3_intertwiner():
    section("P3: INTERTWINER SEARCH -- (Z/480)^x vs the E8 spinor block "
            "(v775 standard doubled model)")
    # 128 spinor roots: (+-1)^8 with sum = 0 mod 4  <=>  even # of -1
    SP = [v for v in itertools.product((1, -1), repeat=8)
          if sum(v) % 4 == 0]
    IDX = {v: i for i, v in enumerate(SP)}
    check("P3.1 spinor block: %d roots (+-1)^8 with sum = 0 mod 4 "
          "(248 = 120 + 128: adjoint side 112 integer roots + 8 Cartan, "
          "spinor side 128 = D8 half-spinor; v775 model)" % len(SP),
          len(SP) == 128 and all(v.count(-1) % 2 == 0 for v in SP))

    # deployed generators
    def J_act(v):
        return (-v[1], v[0], -v[3], v[2], -v[5], v[4], -v[7], v[6])

    def sig_act(v):
        return (v[4], v[5], v[0], v[1], v[2], v[3], v[6], v[7])

    PJ = tuple(IDX[J_act(v)] for v in SP)
    PS = tuple(IDX[sig_act(v)] for v in SP)
    ID = tuple(range(128))
    MINUS1 = tuple(IDX[tuple(-x for x in v)] for v in SP)
    EPS67 = tuple(IDX[v[:6] + (-v[6], -v[7])] for v in SP)
    EPS05 = tuple(IDX[tuple(-x for x in v[:6]) + v[6:]] for v in SP)
    ok_orders = (perm_order(PJ) == 4 and perm_order(PS) == 3
                 and compose(PJ, PJ) == MINUS1
                 and compose(MINUS1, EPS67) == EPS05)
    check("P3.2 deployed structures on the block: mu4 = J (pair rotation) "
          "has order 4 with J^2 = -1; deck sigma (pair 3-cycle) order 3; "
          "chi_NSR is constant on the spinor block (preservation is "
          "automatic); named involutions -1, eps_67 (anchor-pair flip, "
          "sigma-fixed pair), eps_05 = -eps_67", ok_orders)

    # Gamma = even sign-flip group, the canonical torsor
    def translation(eps):
        return tuple(IDX[tuple(e * x for e, x in zip(eps, v))] for v in SP)

    GAMMA = {}
    for eps in itertools.product((1, -1), repeat=8):
        if eps.count(-1) % 2 == 0:
            GAMMA[eps] = translation(eps)
    gamma_set = set(GAMMA.values())
    free = all(all(t[i] != i for i in range(128))
               for eps, t in GAMMA.items() if eps != (1,) * 8)
    orbit0 = {t[0] for t in GAMMA.values()}
    exp2 = all(compose(t, t) == ID for t in GAMMA.values())
    check("P3.3 CANONICAL TORSOR: the even sign-flip group Gamma ~ F2^7 "
          "(order 128, exponent 2) acts freely and transitively on the "
          "128 spinor roots -- the block IS a torsor, but under F2^7",
          len(gamma_set) == 128 and free and len(orbit0) == 128 and exp2)

    # Gamma is self-centralizing: every Gamma-equivariant bijection is a
    # translation (orbit map bijective + abelian translations commute)
    ok_comm = all(compose(GAMMA[e1], t) == compose(t, GAMMA[e1])
                  for e1 in list(GAMMA)[:8] for t in GAMMA.values())
    check("P3.4 Gamma is self-centralizing in Sym(128): the orbit map "
          "gamma -> gamma.x0 is bijective (P3.3), so a Gamma-equivariant "
          "map is fixed by its value at x0 and IS a translation; "
          "translations commute (spot-checked 8 x 128 pairs) => "
          "Centralizer(Gamma) = Gamma, exponent 2", ok_comm)
    print("    => any (Z/480)^x-action commuting with the torsor structure "
          "factors through (Z/480)^x / squares (order 16): never faithful "
          "(exponent 8 vs 2).")

    # the deployed symmetry group G = <Gamma, J, sigma>
    gamma_gens = [GAMMA[eps] for eps in
                  [tuple(-1 if k in (0, i) else 1 for k in range(8))
                   for i in range(1, 8)]]
    G = subgroup_closure([PJ, PS] + gamma_gens, ID)
    ordhist = {}
    for g in G:
        o = perm_order(g)
        ordhist[o] = ordhist.get(o, 0) + 1
    check("P3.5 deployed symmetry group G = <Gamma, J, sigma>: |G| = %d "
          "= 128 x 6 (G/Gamma ~ Z6 = <perm_J> x <perm_sigma>); element "
          "order histogram %s" % (len(G), dict(sorted(ordhist.items()))),
          len(G) == 768 and gamma_set <= G)
    no8 = all(o % 8 != 0 for o in ordhist)
    check("P3.6 THE EXACT OBSTRUCTION: G contains NO element of order 8 "
          "(orders %s) -- but (Z/480)^x has invariant factor Z8, so "
          "(Z/480)^x embeds in NO subgroup of G: no faithful canonical "
          "action exists, a fortiori no simply-transitive one (torsor "
          "form DEAD)" % sorted(ordhist), no8)

    # centralizer of {J, sigma} in G
    C = [g for g in G if compose(g, PJ) == compose(PJ, g)
         and compose(g, PS) == compose(PS, g)]
    c_orders = sorted(perm_order(g) for g in C)
    c_ab = all(compose(a, b) == compose(b, a) for a in C for b in C)
    c_named = (MINUS1 in C and EPS67 in C and EPS05 in C
               and PJ in C and PS in C)
    invols = [g for g in C if perm_order(g) <= 2]
    check("P3.7 centralizer C = C_G(sigma, J) = <J> x <eps_67> x <sigma> "
          "~ Z4 x Z2 x Z3 (order %d, abelian %s, element orders %s); "
          "involutions in C: exactly {1, -1, eps_67, eps_05} ~ F2^2 -- "
          "only TWO independent named involutions for FOUR quadratic "
          "sub-characters" % (len(C), c_ab, sorted(set(c_orders))),
          len(C) == 24 and c_ab and c_named and len(invols) == 4
          and set(invols) == {ID, MINUS1, EPS67, EPS05})

    # exhaustive hom census (Z/480)^x -> C  (gens orders 2, 8, 2, 4)
    c_ord = {g: perm_order(g) for g in C}
    hom_images = []
    dict_ok_d2d5 = 0
    for a in C:            # image of -1 mod 32   (order | 2)
        if c_ord[a] > 2:
            continue
        for b in C:        # image of 3 mod 32    (order | 8)
            if 8 % c_ord[b] != 0:
                continue
            for c in C:    # image of 2 mod 3     (order | 2)
                if c_ord[c] > 2:
                    continue
                for d in C:  # image of 2 mod 5   (order | 4)
                    if 4 % c_ord[d] != 0:
                        continue
                    img = subgroup_closure([a, b, c, d], ID)
                    hom_images.append(len(img))
                    if d == PJ and a == EPS67:
                        dict_ok_d2d5 += 1
    max_img = max(hom_images)
    check("P3.8 EXHAUSTIVE HOM CENSUS: %d homomorphisms (Z/480)^x -> C; "
          "max image order = %d (never 128: NEVER faithful, kernel index "
          "<= 8 means >= 4 of the 7 header bits are always lost); "
          "faithful homs: 0" % (len(hom_images), max_img),
          max_img <= 8 and 128 not in hom_images)

    # predeclared dictionary, entry by entry
    d1 = compose(PJ, PJ) == MINUS1
    check("P3.9 DICT D1 (chi_-4 -> Gaussian split/inert involution): "
          "REALIZABLE -- J^2 = -1 exactly (subsumed by D2)", d1)
    d2 = 4 % c_ord[PJ] == 0 and c_ord[PJ] == 4
    check("P3.10 DICT D2 (mod-30 Coxeter order-4 part <7 mod 30> -> "
          "mu4 = J): REALIZABLE -- orders match (4 -> 4), J in C; "
          "%d homs realize D2+D5 simultaneously" % dict_ok_d2d5,
          d2 and dict_ok_d2d5 > 0)
    # realizable iff ord(sigma) divides the generator order 2
    d3_realizable = (2 % c_ord[PS] == 0)
    check("P3.11 DICT D3 (mod-3 part, order 2 -> deck sigma, order 3): "
          "STRUCTURALLY IMPOSSIBLE -- a homomorphism must kill the "
          "order-2 generator into <sigma> ~ Z3 (gcd(2,3) = 1); sigma "
          "can never lie in the image of the 2-group (Z/480)^x",
          (not d3_realizable) and c_ord[PS] == 3)
    d4_candidates = [g for g in G if perm_order(g) == 8]
    check("P3.12 DICT D4 (mod-32 Galois part, order 8 -> order-8 "
          "candidate from the mu4/level structure): CANDIDATE SET EMPTY "
          "-- %d elements of order 8 in ALL of G (exhaustive census); "
          "the 3-bit Galois part <3 mod 32> is never represented"
          % len(d4_candidates), len(d4_candidates) == 0)
    d5 = EPS67 in C and c_ord[EPS67] == 2
    check("P3.13 DICT D5 (CRT(-1 mod 32) -> anchor-pair flip eps_67): "
          "REALIZABLE -- eps_67 in C, order 2", d5)

    graded_max = max(n for n in hom_images)
    print("    GRADED RESULT: the maximal canonical action is the "
          "order-%d image <J, eps_67> ~ Z4 x Z2 (D2 + D5 + derived D1): "
          "3 of the 7 header bits (the mod-5 Coxeter 2 bits + one mod-32 "
          "sign bit) act; the mod-3 bit (D3) and the 3-bit mod-32 Galois "
          "part (D4) are STRUCTURALLY unrepresentable." % graded_max)

    intertwined = (max_img == 128 and len(d4_candidates) > 0)
    return dict(intertwined=intertwined, max_img=max_img, no8=no8,
                SP=SP, GAMMA=GAMMA, gamma_set=gamma_set, ID=ID,
                C=C, c_ord=c_ord, ordhist=ordhist)


# ======================================================================
# CONTROLS (must fire)
# ======================================================================
def controls(primes, ctx3):
    section("C: CONTROLS (must fire)")
    # C1 positive control: the RIGHT group F2^7 IS detected as a torsor
    ok_c1 = (len(ctx3["gamma_set"]) == 128
             and all(compose(t, t) == ctx3["ID"]
                     for t in list(ctx3["gamma_set"])[:16]))
    check("C1 FIRES (positive): the harness finds the canonical torsor "
          "for the RIGHT group -- F2^7 = Gamma acts simply transitively "
          "(P3.3); the failure for (Z/480)^x is a property of the GROUP "
          "(exponent 8, Z8 factor), not of the harness", ok_c1)

    # C2 scrambled control: fixed-seed random abelian order-128 group
    rng = random.Random(480)
    types = [(128,), (2, 64), (4, 32), (8, 16), (2, 2, 32), (2, 4, 16),
             (2, 8, 8), (4, 4, 8), (2, 2, 2, 16), (2, 4, 4, 4),
             (2, 2, 2, 4, 4), (2, 2, 2, 2, 8)]
    typ = rng.choice(types)
    targets = [ctx3["ID"], ctx3["C"][0]] + ctx3["C"][:6]
    scram = [(o, rng.choice(ctx3["C"])) for o in typ]
    viol = [(o, ctx3["c_ord"][t]) for o, t in scram
            if o % ctx3["c_ord"][t] != 0]
    needs8 = any(o >= 8 for o in typ)
    no8_in_c = all(ctx3["c_ord"][g] != 8 for g in ctx3["C"])
    fired = (len(viol) > 0) or (needs8 and no8_in_c)
    check("C2 FIRES: scrambled control -- random abelian type %s (seed "
          "480) with scrambled generator->target dictionary %s has %d "
          "order-violating entries%s => the dictionary census REJECTS it"
          % (typ, [(o, ctx3["c_ord"][t]) for o, t in scram], len(viol),
             "; needs an order-8 image which C lacks" if needs8 else ""),
          fired)

    # C3 wrong moduli break the CRT header (collision census)
    def collisions(m1, m2):
        seen = {}
        n_coll = 0
        for p in primes:
            key = (p % m1, p % m2)
            r = p % MOD480
            if key in seen and seen[key] != r:
                n_coll += 1
            else:
                seen[key] = r
        return n_coll

    c28 = collisions(28, 32)
    c36 = collisions(36, 32)
    c30 = collisions(30, 32)
    check("C3 FIRES: wrong moduli break the header -- (mod 28, mod 32): "
          "%d collisions (lcm 224 < 480), (mod 36, mod 32): %d collisions "
          "(lcm 288 < 480); the TRUE header (mod 30, mod 32): %d "
          "collisions (exact)" % (c28, c36, c30),
          c28 > 0 and c36 > 0 and c30 == 0)
    return ok_c1 and fired and (c28 > 0 and c36 > 0 and c30 == 0)


# ======================================================================
# P4 -- information accounting (typed measurement, never a gate)
# ======================================================================
def p4_information():
    section("P4: INFORMATION ACCOUNTING [M] -- 7 header bits vs the "
            "corpus reconstruction window")
    bits = math.log2(N_CLASSES)
    lo, hi = 5.0, 12.0
    inside = lo <= bits <= hi
    check("P4.1 [M] the 7-bit header (log2 128 = %.0f) sits INSIDE the "
          "corpus-measured per-slot information demand g ~ 5-12 bits of "
          "the autonomous prime-front reconstruction (v702, "
          "PRIME.Z1LOOKAHEAD.01: 'the per-slot information demand "
          "g ~ 5-12 bits is information-theoretic and parameter-robust'; "
          "verdict Z1-RECURSION-SEMI / FLOW-VERIFIER-NOT-GENERATOR)"
          % bits, inside)
    print("    CONTEXT ONLY: the header is per-PRIME address information "
          "(exact, zero noise), the v702 window is per-SLOT generative "
          "demand of the Gamma-flow reconstruction -- same order of "
          "magnitude, different registers; typed [M], never a gate.")


# ======================================================================
def main():
    print("=" * 78)
    print("PRIME.PACKET480.01 -- the 7-bit packet header (p mod 30, "
          "a_p mod 32) vs the E8 spinor block")
    print("=" * 78)
    print("FROZEN_SPEC SHA-256: %s"
          % hashlib.sha256(FROZEN_SPEC.encode()).hexdigest())
    print(flush=True)

    primes, _a32 = p1_header()
    p2_group()
    ctx3 = p3_intertwiner()
    controls_fired = controls(primes, ctx3)
    p4_information()

    section("SUMMARY / VERDICT")
    n_pass = sum(1 for _, ok in CHECKS if ok)
    n_all = len(CHECKS)
    illdefined = "ILLDEFINED" in KILLS
    print("%d/%d checks passed" % (n_pass, n_all))
    if illdefined:
        verdict = "PACKET480-ILLDEFINED"
    elif not controls_fired:
        verdict = "TEST-VOID"
    elif ctx3["intertwined"]:
        verdict = "PACKET480-INTERTWINED"
    else:
        verdict = "PACKET480-ADDRESS-ONLY"
    print("VERDICT: %s" % verdict)
    if verdict == "PACKET480-ADDRESS-ONLY":
        print("""
ADJUDICATION -- PACKET480-ADDRESS-ONLY (kill criterion FIRED, typed plainly):
  * The header LAYER is exact: (p mod 30, a_p mod 32) <-> p mod 480 via CRT
    (structural bijection on Z/480) and the check32 decoder
    p mod 32 = (a_p - 1)^3 mod 32 holds on every prime 5 < p < 1e5, backed
    by the Eisenstein congruence a_p = 1 + p^3 (mod 32) (a_p recomputed
    independently from the eta product; Hecke-guarded).
  * (Z/480)^x = Z2 x Z2 x Z4 x Z8 (exponent 8).  The spinor block IS a
    canonical torsor -- but under Gamma ~ F2^7 (exponent 2).  The deployed
    symmetry group G = <Gamma, J, sigma> (|G| = 768) contains NO element of
    order 8, so (Z/480)^x embeds in no subgroup of G: no faithful canonical
    action of ANY form exists; the exhaustive hom census into
    C_G(sigma, J) ~ Z4 x Z2 x Z3 tops out at image order 8.
  * The predeclared dictionary splits exactly: D1, D2, D5 REALIZABLE
    (Coxeter mu4 part -> J, its square -> the Gaussian split/inert -1,
    CRT(-1 mod 32) -> eps_67); D3 (mod-3 -> deck sigma) and D4 (mod-32
    Galois Z8 part) STRUCTURALLY IMPOSSIBLE.  3 of 7 header bits act;
    4 are address-only.
  * The 128 = phi(480) = |spinor block| coincidence is CARDINALITY ONLY
    (the two groups of order 128 are non-isomorphic): a fingerprint, not
    a theorem.  The header stays ADDRESS ARITHMETIC.
RECOMMENDED CONTRACT TEXT (report only, no surface touched):
  'PRIME.PACKET480.01 (exploration): the prime packet header
   (p mod 30, a_p mod 32) is exact 7-bit address arithmetic
   (CRT + check32, Eisenstein congruence a_p = 1 + p^3 mod 32); the sharp
   intertwiner question is settled NEGATIVELY -- (Z/480)^x (type
   2.2.4.8, exponent 8) admits no faithful canonical action on the 128
   E8 spinor roots (canonical torsor group F2^7, exponent 2; deployed
   symmetry group has no order-8 element).  Maximal canonical action:
   the order-8 graded image <mu4, eps_67> (Coxeter/mod-5 part + one
   mod-32 sign bit).  The 128 stays a fingerprint.  Kill criterion
   fired as preregistered; matter-adjacent readings stay fenced by
   v775 ROOTCLASS-MIXED.'
FENCES: no semantic/message claims anywhere in this probe; the spinor
block is a root set; ROOTCLASS-MIXED (v775) binds every matter-adjacent
reading.  P1.6 and P4 are typed measurements [M], not gates.""")
    print("Runtime: %.1f min" % ((time.time() - T0) / 60.0))
    print("ALL CHECKS PASSED" if n_pass == n_all else "CHECKS FAILED")
    return 0 if n_pass == n_all else 1


if __name__ == "__main__":
    raise SystemExit(main())
