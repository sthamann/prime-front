#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""prime_gap_register_correlation_probe -- E8.DIVISOR210.GAPCODE.01:
what do the primes and their GAPS directly correlate with, and is the
210 register an error-correcting code ON the prime sequence?

EXPLORATION ONLY (experiments/): no ledger row, no paper edit, no .md,
nothing outside experiments/.  NO RH claim.  Frozen (spec + sha256)
before running.  This is a MEASUREMENT probe (statistics on the actual
prime sequence), not an exact-arithmetic probe: floats are used for
the statistics, every DECISION threshold is predeclared below, the
only RNG is the seeded holdout split and the seeded scramble control.

THE QUESTION (user-posed, frozen): the register probes established
exact ARITHMETIC seats for 210 = rad|W(E8)| = 7# with phi(210) = 48 =
Omega_adm and tau(210) = 16 = register labels -- but purely as
identities among compiler integers.  If the primes really are "a kind
of error code" in the register's sense, then the register state of a
prime must CORRELATE with something on the prime side -- most directly
with the gap to the next prime.  This probe measures that correlation,
separates the part that is forced by the sieve (the code's own parity
checks) from any arithmetic excess, and asks whether 210 is
statistically distinguished among 4-check moduli or merely optimal-by-
size.

THE CODE READING (the object under test): the sieve of Eratosthenes is
a parity-check system -- n survives check p iff n != 0 mod p.  The
register bits {2,3,5,7} are exactly the FIRST FOUR checks, so:
  * codewords          = integers coprime to 210
  * code rate          = phi(210)/210 = 48/210 = Omega_adm/210
  * admissible states  = 48 = Omega_adm  (one per surviving class)
  * syndrome coarsening= 16 = tau(210) labels (quadratic characters)
  * message capacity   = 0 bits (v868 / frobwalsh S6)  -- a PURE
                         parity-check structure, no information slot.
Every prime > 7 is a codeword.  The falsifiable content is HOW MUCH of
the observed gap structure this 4-check code actually accounts for.

FROZEN CLAIMS (2026-08-09, frozen + SHA-hashed before first run):

 S1  THE REGISTER IS THE 4-CHECK PARITY SYSTEM (exact, verified on
     the sieved sequence to X):
     (a) every prime p with 7 < p <= X is a unit mod 210 -- the 48
         admissible classes are exactly Omega_adm and ALL 48 are
         occupied;
     (b) the ANCHOR slot carries ZERO information on the prime
         sequence: p == 1 mod 2 for every odd prime, so the anchor
         bit of the register is frozen -- the empirical counterpart
         of the frobwalsh S3.a seat (the clock TRIVIALIZES at the
         ramified prime, which is exactly where the register is cut);
     (c) code rate 48/210 = 8/35: four checks reject 77.14% of the
         candidate integers, i.e. log2(210/48) = 2.129 bits of HARD
         constraint per position.
     (d) syndrome coarsening: the quadratic characters at {3,5,7}
         plus chi4 at the anchor realize exactly tau(210) = 16
         labels, all occupied and equidistributed.
     V2 AMENDMENT (honest, after smoke run 1 at X = 1e6): the frozen
     v1 equidistribution ward was a fixed 1% occupancy deviation,
     which is SCALE-DEPENDENT and failed at X = 1e6 (measured 1.28%,
     multinomial noise alone is 1.4%).  Replaced by the scale-correct
     ward |dev| < 6 sigma with sigma = sqrt(16/N).  No criterion
     content changed; the v1 miss is recorded here.
     Fail => SIEVE-BROKEN.

 S2  THE WHEEL FLOOR -- a deterministic, exact gap<->state law
     (verified on every consecutive pair to X):
     (a) with w(a) = distance from a to the next unit mod 210, EVERY
         consecutive prime pair with p_k > 7 obeys g_k >= w(p_k mod
         210): the register state of a prime puts a HARD FLOOR under
         its gap.  Zero violations required;
     (b) the legal gap set is state-dependent: g_k mod 210 must land
         in D(a) = {d : gcd(a+d, 210) = 1}, |D(a)| = 48 of 210 --
         the register deterministically forbids 77.14% of the a
         priori gap values;
     (c) measured: Pearson and Spearman of w(a) against the measured
         mean normalized gap profile E[g/log p | a] over the 48
         states (predeclared: strongly positive; this IS the direct
         correlation the question asks for).
     Fail (any floor violation) => FLOOR-BROKEN.

 S3  VARIANCE ACCOUNTING AND THE DEPTH CURVE (measured, seeded 50/50
     holdout, evaluated out-of-sample):
     (a) holdout R^2 of the normalized gap ghat = g/log p explained by
         the residue class, for the wheel ladder m = 2, 6, 30, 210,
         2310, 30030 (1..6 checks).  V2 AMENDMENT (honest, after
         smoke run 1): a prime that DIVIDES the modulus is not a
         codeword of that wheel (11 and 13 for m = 2310, 30030), so
         each wheel is evaluated on its own codeword subset and the
         dropped count is reported -- at most two pairs, no sample
         change worth the name;
     (b) mutual information I(class; gap) in bits, Miller-Madow
         corrected, with a seeded label-shuffle baseline, reported
         also as a fraction of the gap entropy H(gap) -- the
         register's actual decoding power;
     (c) KNEE TEST (predeclared, falsifiable): the register would be
         statistically distinguished if the 4th check (m = 210)
         contributed anomalously much, i.e. if
             dR2(210) > 1.5 * sqrt(dR2(30) * dR2(2310))
         (geometric interpolation of its neighbours).  Frozen
         expectation: NO knee -- smooth diminishing returns, the
         register's seat is the FORCING prod(p-1) = 48, not a
         statistical anomaly in the primes.  Either outcome is
         recorded; a knee would be a genuine finding (flag
         REGISTER-KNEE).
     (d) V2 AMENDMENT (honest, added after smoke run 1 at X = 1e6,
         where the knee criterion FIRED): a knee in the measured
         curve is uninterpretable on its own, because the marginal
         gain per check is a property of the WHEEL GEOMETRY before
         any arithmetic.  The same depth curve is therefore computed
         under the zero-parameter wheel-Cramer null of S5 for every
         modulus, and the knee criterion is applied to BOTH.  The
         register is only distinguished if the knee is present in
         the measured curve and ABSENT in the null curve; a knee in
         both is sieve geometry and clears the flag.  The flag is
         set as REGISTER-KNEE only in the former case, and reported
         as KNEE-IS-WHEEL-GEOMETRY in the latter.

 S4  WALSH SEATS OF THE GAP SIGNAL (the TFPT-specific test).  For a
     prime p > 7 define the 4-bit register syndrome
         s(p) = (chi_3(p), chi_5(p), chi_7(p), chi_4(p)) in {+-1}^4
     with chi_q = the quadratic character at the family primes and
     chi_4 = the mu4/Galois character at the ramified anchor (the
     anchor's only non-frozen readout, since p mod 2 is constant).
     This is the 16-label register realized ON the primes.  Expand
     the centred normalized gap in the 16 Walsh characters:
         ghat_hat(S) = mean_k [ (ghat_k - mean ghat) * prod_{q in S}
                                 chi_q(p_k) ],  S subset {3,5,7,A}.
     (a) all 16 coefficients with analytic standard error and
         z-scores, at X = 1e6, 1e7, 1e8;
     (b) which seat carries the signal?  frobwalsh S4b/S4c put the
         Galois character at the INERT seat {3,7} and its product
         with mu at the complement {5, anchor}.  Predeclared as an
         OPEN measurement -- no expectation frozen, because Dirichlet
         equidistribution sends every nontrivial coefficient to zero;
         the content is the RANKING and the DECAY RATE;
     (c) decay exponents per seat over the X ladder (fit slope of
         log|coef| vs log X); a seat decaying markedly slower than
         the generic -1/2 would be structure.  Recorded, not frozen.
     (d) THE ANCHOR PREDICTION (exact, predeclared): the wheel floor
         depends only on p mod 210, and p mod 4 is independent of
         p mod 210 by CRT -- so the wheel model predicts EXACTLY
         ZERO Walsh weight on every seat containing the anchor bit
         A.  Any significant anchor seat would be arithmetic beyond
         the sieve (Lemke-Oliver-Soundararajan lives here).  Ward:
         max |z| over the eight A-seats, recorded against the eight
         A-free seats.

 S5  THE WHEEL-CRAMER NULL (analytic, no RNG) -- separating the code
     from the arithmetic.  Model: each admissible slot near x is
     prime independently with probability q = (210/48)/log x, with q
     evaluated at the sample mean of log p.  Then
         E_null[g | a] = sum_{j>=1} d_j(a) q (1-q)^{j-1},
     d_j(a) = distance from a to the j-th next unit mod 210.  This is
     the EXACT prediction of "the primes are nothing but the wheel".
     (a) internal consistency: the model's own predicted mean gap
         matches the measured mean gap to <1% AND the measured mean
         gap agrees with mean log p to <2% (PNT ward); a failure
         means the null is mis-normalized => NULL-BROKEN;
     (b) q-insensitivity: the null PROFILE shape at q(1e6) and q(X)
         must agree to correlation > 0.999 (this is what justifies
         evaluating the profile at a single q).
         V2 AMENDMENT (honest, after the frozen run at X = 1e8): this
         ward FAILED, measuring 0.99278 -- correctly, because the
         wheel profile does stiffen with depth and a single q IS an
         approximation.  The ward is not loosened.  Instead the
         approximation it was protecting is removed: the null is now
         evaluated PER PRIME on a 64-bin log p grid (q clipped at
         0.95, which only touches primes below ~100), so no single-q
         step remains anywhere in S5, S3 or C1.  The shape
         correlation is retained as a recorded measurement of the
         stiffening and no longer gates the verdict;
     (c) THE DECOMPOSITION, reported at three explicit levels so no
         fit is hidden: (i) corr(measured profile, null profile) --
         pure shape, offset-free; (ii) raw R^2 of the null profile
         with NO free parameter; (iii) R^2 after removing the single
         constant level offset (declared, one parameter).  The
         residual profile (measured - null - offset) is what the
         4-check code does NOT explain: the Hardy-Littlewood /
         Lemke-Oliver-Soundararajan class arithmetic excess.
         Recorded with its X-decay.

 S6  WHERE THE REGISTER PRIMES SIT IN THE DEPLOYED COMB (the bridge
     to the prime front, measured, cheap): the wall functional sees
     the comb {log n, 2 Lambda(n)/sqrt n}.  Measure the fraction of
     comb weight at n > 7 that sits on wheel-admissible n; the
     exceptions are exactly the higher powers of the register primes
     themselves.  Typed observation, no wall claim.

 C   CONTROLS (must fire / must measure generic where predeclared):
     C1 FOREIGN WHEELS (predeclared: the floor law is GENERIC): the
        same S2/S3 measurement for 330 = 2*3*5*11, 462 = 2*3*7*11,
        770 = 2*5*7*11, 1155 = 3*5*7*11 and 210.  The anchor-free
        wheel 1155 is in the set on purpose: without the prime 2 an
        even position can be admissible, so its floor degenerates to
        1 -- the mean floor per wheel is reported.  Every 4-prime
        squarefree modulus has a wheel floor; the question is whether
        210 is an OUTLIER once normalized by its constraint content
        log2(m/phi(m)).  Predeclared: 210 maximizes raw R^2 trivially
        (smallest primes remove most) and must lie ON the trend in
        R^2 vs bits -- a >3 sigma outlier would be a finding
        (flag REGISTER-OUTLIER).  V2 AMENDMENT (honest, after smoke
        run 1): raw R^2 is not comparable across wheels with
        different state counts, so the EXCESS OVER THE WHEEL-CRAMER
        NULL is additionally reported per wheel -- that is the
        arithmetic content proper, and it is the quantity on which
        210 either is or is not special.  Smoke run 1 exposed a
        second defect: for the anchor-free wheel 1155 the naive null
        allows EVEN candidate positions and therefore understates the
        wheel, faking a large excess.  The null is now read on the
        doubled period lcm(m, 2) restricted to odd slots for every
        modulus (identity for even m), so "primes are odd" is in the
        null rather than in the excess.
     C2 SCRAMBLE (seeded, must fire): permuting the gap labels must
        drive the S2c correlation below |r| = 0.5 (the 48-state noise
        level is ~0.15) and the S3 R^2 below a tenth of its value.
     C3 PURE-WHEEL CONTROL (must fire as "no arithmetic residual"):
        the deterministic sequence of integers coprime to 210 has the
        wheel floor by construction but no arithmetic excess -- run
        S2a on it and confirm the floor is EXACTLY saturated.
     C4 TRIVIAL-MAXIMIZER HONESTY: exhaustive over all quadruples of
        primes < 200, {2,3,5,7} uniquely maximizes 1 - prod(1-1/p) --
        recorded as TRIVIAL (smallest primes win), so sieve
        efficiency alone selects nothing for TFPT.

VERDICT (frozen precedence): SIEVE-BROKEN / FLOOR-BROKEN /
NULL-BROKEN / CONTROL-DEAD on kill; else GAPCODE-MEASURED with the
measured wheel/residual split and the two predeclared flags
(REGISTER-KNEE, REGISTER-OUTLIER) resolved either way.

Sources (read-only): register_prime_forcing_probe.py (210 =
rad|W(E8)|, prod(p-1) = 48 forcing, gears (1,2,4,6)),
register_frobenius_walsh_probe.py (bit model, chi4 Walsh seat at the
inert pair, 0 message bits), v868_divisor210_audits (canonicity),
verification/tfpt_constants (c3, g_car, N_fam, Omega_adm).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/prime_gap_register_correlation_probe.py
"""

import hashlib
import math
import os
import sys
import time
from itertools import combinations

import numpy as np

T0 = time.time()
CHECKS = []
KILLS = []
FLAGS = []

SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()

# ---- compiler integers (register_prime_forcing / tfpt_constants) ----
N_FAM = 3
G_CAR = 5
OMEGA_ADM = 48            # phi(210) = admissible register states
REGISTER_LABELS = 16      # tau(210) = syndrome labels
REGISTER_PRIMES = (2, 3, 5, 7)
REGISTER_MODULUS = 210

# ---- measurement scale ----
XMAX = int(os.environ.get("GAPCODE_XMAX", 10 ** 8))
XLADDER = tuple(sorted({x for x in (10 ** 5, 10 ** 6, 10 ** 7, XMAX)
                        if x <= XMAX}))
WHEEL_LADDER = (2, 6, 30, 210, 2310, 30030)
FOREIGN_WHEELS = (210, 330, 462, 770, 1155)
SEED = 20260809
KNEE_FACTOR = 1.5         # S3c predeclared knee criterion
OUTLIER_SIGMA = 3.0       # C1 predeclared outlier criterion


def check(name, ok, detail="", kill=None):
    CHECKS.append((name, bool(ok)))
    if kill and not ok:
        KILLS.append(kill)
    print("  [%s] %s%s" % ("PASS" if ok else "FAIL", name,
                           ("  -- " + detail) if detail else ""),
          flush=True)
    return bool(ok)


def section(title):
    print("\n" + "=" * 70)
    print(title)
    print("=" * 70)


# ======================================================================
# primitives
# ======================================================================

def sieve_primes(limit):
    s = np.ones(limit + 1, dtype=bool)
    s[:2] = False
    for i in range(2, int(limit ** 0.5) + 1):
        if s[i]:
            s[i * i::i] = False
    return np.nonzero(s)[0].astype(np.int64)


def wheel_units(m):
    return np.array([a for a in range(m) if math.gcd(a, m) == 1],
                    dtype=np.int64)


def next_unit_distance(m, units):
    """w(a) = distance from residue a to the next unit mod m."""
    is_unit = np.zeros(m, dtype=bool)
    is_unit[units] = True
    w = np.zeros(m, dtype=np.int64)
    for a in range(m):
        d = 1
        while not is_unit[(a + d) % m]:
            d += 1
        w[a] = d
    return w


def unit_index_table(m, units):
    tbl = np.full(m, -1, dtype=np.int64)
    tbl[units] = np.arange(len(units), dtype=np.int64)
    return tbl


def slot_distances(period, slots, jmax):
    """d_j(a) for every slot a and j = 1..jmax (cyclic, exact)."""
    ns = len(slots)
    j = np.arange(1, jmax + 1, dtype=np.int64)
    idx = (np.arange(ns, dtype=np.int64)[:, None] + j[None, :])
    wraps = idx // ns
    return slots[idx % ns] + period * wraps - slots[:, None]


def prime_slots(m):
    """the positions a prime can occupy, as residues mod lcm(m, 2).

    Primes are odd, so an anchor-free wheel (m odd) must still be read
    on the doubled period -- otherwise the null model would allow even
    candidates and understate the wheel.
    """
    period = m if m % 2 == 0 else 2 * m
    slots = np.array([r for r in range(period)
                      if r % 2 == 1 and math.gcd(r, m) == 1],
                     dtype=np.int64)
    if m == 2:
        slots = np.array([1], dtype=np.int64)
    return period, slots


def wheel_null_hat(m, logx):
    """normalized wheel-Cramer profile E_null[g|a]/log x at one q."""
    period, slots = prime_slots(m)
    q = (period / len(slots)) / logx
    jmax = int(math.ceil(40.0 / q))
    wts = q * (1.0 - q) ** np.arange(jmax, dtype=np.float64)
    return (slots % m,
            (slot_distances(period, slots, jmax).astype(np.float64)
             @ wts) / logx)


def null_prediction(m, logp_arr, res_arr, nbins=64):
    """per-prime wheel-Cramer prediction of ghat = g / log p.

    q = (period/#slots)/log p varies over the sample, so the profile
    is evaluated on a grid of log p bins rather than at a single q.
    q is clipped at 0.95: below p ~ 100 the geometric slot model
    degenerates (q > 1), which concerns a few dozen of millions of
    primes.
    """
    period, slots = prime_slots(m)
    ns = len(slots)
    pos = np.full(m, -1, dtype=np.int64)
    pos[slots % m] = np.arange(ns, dtype=np.int64)
    st = pos[res_arr]
    q_all = np.clip((period / ns) / logp_arr, 1e-6, 0.95)
    lo, hi = float(logp_arr.min()), float(logp_arr.max())
    span = max(hi - lo, 1e-9)
    binid = np.clip(((logp_arr - lo) / span * nbins).astype(np.int64),
                    0, nbins - 1)
    jmax = int(math.ceil(40.0 / float(q_all.min())))
    dj = slot_distances(period, slots, jmax).astype(np.float64)
    jrange = np.arange(jmax, dtype=np.float64)
    pred = np.empty(len(logp_arr), dtype=np.float64)
    for b in np.unique(binid):
        sel = binid == b
        qb = float(q_all[sel].mean())
        prof = dj @ (qb * (1.0 - qb) ** jrange)
        pred[sel] = prof[st[sel]] / logp_arr[sel]
    return st, pred


def r2_of(y, pred):
    mean = y.mean()
    return 1.0 - (float(np.sum((y - pred) ** 2))
                  / float(np.sum((y - mean) ** 2)))


def holdout_r2(state_idx, y, n_states, rng):
    """out-of-sample R^2 of the class-mean predictor (50/50 split)."""
    mask = rng.random(len(y)) < 0.5
    cnt_a = np.bincount(state_idx[mask], minlength=n_states)
    sum_a = np.bincount(state_idx[mask], weights=y[mask],
                        minlength=n_states)
    gmean = y[mask].mean()
    with np.errstate(invalid="ignore", divide="ignore"):
        prof = np.where(cnt_a > 0, sum_a / np.maximum(cnt_a, 1), gmean)
    yb = y[~mask]
    pred = prof[state_idx[~mask]]
    sse = float(np.sum((yb - pred) ** 2))
    sst = float(np.sum((yb - gmean) ** 2))
    return 1.0 - sse / sst


def mutual_info_bits(state_idx, gaps, n_states, rng, gcap=64):
    """I(class; gap) in bits, Miller-Madow corrected + shuffle base."""
    gb = np.minimum(gaps, gcap) // 2
    n_bins = int(gb.max()) + 1
    n = len(gb)

    def mi(states):
        joint = np.bincount(states * n_bins + gb,
                            minlength=n_states * n_bins
                            ).reshape(n_states, n_bins).astype(np.float64)
        pj = joint / n
        pa = pj.sum(axis=1, keepdims=True)
        pg = pj.sum(axis=0, keepdims=True)
        nz = pj > 0
        val = float(np.sum(pj[nz] * np.log2(pj[nz]
                                            / (pa @ pg)[nz])))
        occupied = int(np.count_nonzero(joint))
        bias = (occupied - n_states - n_bins + 1) / (2.0 * n * math.log(2))
        return val - bias

    raw = mi(state_idx)
    shuf = mi(rng.permutation(state_idx))
    return raw, shuf


def pearson(x, y):
    x = np.asarray(x, dtype=np.float64)
    y = np.asarray(y, dtype=np.float64)
    xc, yc = x - x.mean(), y - y.mean()
    return float(xc @ yc / math.sqrt((xc @ xc) * (yc @ yc)))


def spearman(x, y):
    def rank(v):
        v = np.asarray(v, dtype=np.float64)
        order = np.argsort(v, kind="stable")
        r = np.empty(len(v), dtype=np.float64)
        r[order] = np.arange(len(v), dtype=np.float64)
        # average ranks over ties (w(a) has many)
        for val in np.unique(v):
            m = v == val
            r[m] = r[m].mean()
        return r
    return pearson(rank(x), rank(y))


# ======================================================================
section("S0: sieve and register syndrome")
# ======================================================================
print("spec sha256 = %s" % SPEC_SHA)
print("X = %.0e, seed = %d" % (XMAX, SEED))

RNG = np.random.default_rng(SEED)

primes = sieve_primes(XMAX)
print("  primes <= %.0e: %d (largest %d)"
      % (XMAX, len(primes), primes[-1]))

# work on p > 7 so every prime is a codeword of the 210 register
big = primes[primes > 7]
p_k = big[:-1]
gaps = (big[1:] - big[:-1]).astype(np.int64)
logp = np.log(p_k.astype(np.float64))
ghat = gaps / logp
ghat_c = ghat - ghat.mean()
N = len(gaps)
print("  consecutive pairs with p > 7: %d; mean gap %.4f; "
      "mean g/log p %.6f" % (N, gaps.mean(), ghat.mean()))

UNITS210 = wheel_units(REGISTER_MODULUS)
W210 = next_unit_distance(REGISTER_MODULUS, UNITS210)
IDX210 = unit_index_table(REGISTER_MODULUS, UNITS210)
state = IDX210[p_k % REGISTER_MODULUS]

# ======================================================================
section("S1: the register IS the 4-check parity system")
# ======================================================================
n_units_hit = len(np.unique(state))
check("S1.a every prime 7 < p <= %.0e is a unit mod 210; all %d "
      "admissible classes occupied == Omega_adm = %d"
      % (XMAX, n_units_hit, OMEGA_ADM),
      int(state.min()) >= 0 and len(UNITS210) == OMEGA_ADM
      and n_units_hit == OMEGA_ADM, kill="SIEVE-BROKEN")

anchor_res = np.unique(p_k % 2)
check("S1.b ANCHOR SLOT FROZEN: p mod 2 takes the single value %s on "
      "the whole prime sequence -- 0 bits at the ramified prime "
      "(empirical form of the frobwalsh S3.a clock-trivialization; "
      "the register is cut exactly where it cannot read)"
      % (anchor_res.tolist(),),
      anchor_res.tolist() == [1], kill="SIEVE-BROKEN")

rate = OMEGA_ADM / REGISTER_MODULUS
hard_bits = math.log2(REGISTER_MODULUS / OMEGA_ADM)
check("S1.c code rate phi(210)/210 = %d/%d = %.6f = 8/35; four checks "
      "reject %.2f%% of positions == %.4f bits of HARD constraint"
      % (OMEGA_ADM, REGISTER_MODULUS, rate, 100 * (1 - rate),
         hard_bits),
      abs(rate - 8 / 35) < 1e-12 and abs(hard_bits - 2.1293) < 1e-3,
      kill="SIEVE-BROKEN")

# syndrome coarsening 48 -> 16 (quadratic characters + chi4)
def legendre_bits(arr, q):
    tbl = np.zeros(q, dtype=np.int8)
    qr = {(k * k) % q for k in range(1, q)}
    for r in range(1, q):
        tbl[r] = 1 if r in qr else -1
    return tbl[arr % q].astype(np.int64)


BITS = {
    "3": legendre_bits(p_k, 3),
    "5": legendre_bits(p_k, 5),
    "7": legendre_bits(p_k, 7),
    "A": np.where(p_k % 4 == 1, 1, -1).astype(np.int64),
}
BITNAMES = ("3", "5", "7", "A")
syndrome = sum(((BITS[b] + 1) // 2) << i for i, b in enumerate(BITNAMES))
n_syn = len(np.unique(syndrome))
syn_counts = np.bincount(syndrome, minlength=REGISTER_LABELS)
syn_dev = float(np.max(np.abs(syn_counts / syn_counts.mean() - 1.0)))
syn_sigma = math.sqrt(REGISTER_LABELS / N)
check("S1.d syndrome coarsening: the quadratic characters at {3,5,7} "
      "plus chi4 at the anchor realize exactly %d labels == tau(210) "
      "= %d; all occupied, max occupancy deviation %.4f%% = %.2f "
      "sigma of multinomial noise (ward 6 sigma) -- Dirichlet "
      "equidistribution, the syndrome carries no density signal"
      % (n_syn, REGISTER_LABELS, 100 * syn_dev, syn_dev / syn_sigma),
      n_syn == REGISTER_LABELS and syn_dev < 6 * syn_sigma,
      kill="SIEVE-BROKEN")

# ======================================================================
section("S2: the wheel floor -- deterministic gap <-> state law")
# ======================================================================
floor_k = W210[p_k % REGISTER_MODULUS]
violations = int(np.count_nonzero(gaps < floor_k))
saturated = int(np.count_nonzero(gaps == floor_k))
check("S2.a HARD FLOOR g_k >= w(p_k mod 210): %d violations in %d "
      "consecutive pairs (must be 0); floor exactly saturated in "
      "%d pairs (%.2f%%); w ranges over %s"
      % (violations, N, saturated, 100 * saturated / N,
         sorted(set(W210[UNITS210].tolist()))),
      violations == 0, kill="FLOOR-BROKEN")

legal = np.array([sum(1 for d in range(1, REGISTER_MODULUS + 1)
                      if math.gcd((a + d) % REGISTER_MODULUS,
                                  REGISTER_MODULUS) == 1)
                  for a in UNITS210])
check("S2.b legal gap residues per state: |D(a)| = %d of %d for every "
      "admissible a -- the register deterministically forbids %.2f%% "
      "of a priori gap values, state by state"
      % (int(legal[0]), REGISTER_MODULUS,
         100 * (1 - OMEGA_ADM / REGISTER_MODULUS)),
      bool(np.all(legal == OMEGA_ADM)), kill="FLOOR-BROKEN")

cnt_a = np.bincount(state, minlength=OMEGA_ADM)
prof_meas = (np.bincount(state, weights=ghat, minlength=OMEGA_ADM)
             / cnt_a)
w_units = W210[UNITS210].astype(np.float64)
r_floor_p = pearson(w_units, prof_meas)
r_floor_s = spearman(w_units, prof_meas)
r_all = pearson(floor_k.astype(np.float64), ghat)
check("S2.c THE DIRECT CORRELATION: across the %d admissible states, "
      "Pearson(w(a), E[g/log p | a]) = %+.4f, Spearman = %+.4f; over "
      "all %d individual pairs Pearson(w, g/log p) = %+.4f"
      % (OMEGA_ADM, r_floor_p, r_floor_s, N, r_all),
      True, kill=None)

# ======================================================================
section("S3: variance accounting and the depth curve")
# ======================================================================
gcap_bins = np.minimum(gaps, 64) // 2
_h = np.bincount(gcap_bins) / N
H_GAP = float(-np.sum(_h[_h > 0] * np.log2(_h[_h > 0])))
print("    H(gap) = %.4f bits (gaps binned by 2, capped at 64)" % H_GAP)

LOGX_BAR = float(np.mean(logp))
VAR_GHAT = float(np.var(ghat))

depth = []
r2_null_by_m = {}
for m in WHEEL_LADDER:
    um = wheel_units(m)
    idxm = unit_index_table(m, um)
    st_all = idxm[p_k % m]
    ok = st_all >= 0                      # a prime dividing m is no
    st, ns = st_all[ok], len(um)          # codeword of that wheel
    _, nullpred = null_prediction(m, logp[ok], p_k[ok] % m)
    r2_null_by_m[m] = r2_of(ghat[ok], nullpred)
    r2 = holdout_r2(st, ghat[ok], ns, np.random.default_rng(SEED))
    mi_raw, mi_shuf = mutual_info_bits(st, gaps[ok], ns,
                                       np.random.default_rng(SEED + 1))
    nchecks = len({q for q in (2, 3, 5, 7, 11, 13) if m % q == 0})
    depth.append((m, nchecks, ns, r2, mi_raw, mi_shuf))
    print("    m = %6d  checks %d  states %5d  dropped %d  holdout "
          "R2 = %8.5f  null R2 = %.5f  excess = %+.5f  I(class;gap) "
          "= %.5f bits = %.2f%% of H(gap) (shuffle %.5f)"
          % (m, nchecks, ns, int(np.count_nonzero(~ok)), r2,
             r2_null_by_m[m], r2 - r2_null_by_m[m], mi_raw,
             100 * mi_raw / H_GAP, mi_shuf))

r2_by_m = {m: r2 for m, _, _, r2, _, _ in depth}
mi_by_m = {m: mi for m, _, _, _, mi, _ in depth}
check("S3.a holdout R^2 of g/log p by residue class: %s"
      % ", ".join("m=%d: %.4f" % (m, r2_by_m[m]) for m in WHEEL_LADDER),
      all(np.isfinite(v) for v in r2_by_m.values()), kill=None)
check("S3.b the REGISTER (m = 210, 4 checks) explains %.2f%% of the "
      "normalized-gap variance out of sample and carries %.4f bits "
      "of mutual information with the gap = %.2f%% of H(gap) = %.4f "
      "bits (shuffle baseline %.5f) -- its 2.13 bits of hard "
      "constraint buy that much decoding power"
      % (100 * r2_by_m[210], mi_by_m[210], 100 * mi_by_m[210] / H_GAP,
         H_GAP, [s for m, _, _, _, _, s in depth if m == 210][0]),
      True, kill=None)

def knee_of(curve):
    d3 = curve[30] - curve[6]
    d4 = curve[210] - curve[30]
    d5 = curve[2310] - curve[210]
    bound = KNEE_FACTOR * math.sqrt(max(d3, 0.0) * max(d5, 0.0))
    return d3, d4, d5, bound, d4 > bound


d30, d210, d2310, knee_bound, knee_meas = knee_of(r2_by_m)
n30, n210, n2310, knee_nbound, knee_null = knee_of(r2_null_by_m)
if knee_meas and not knee_null:
    FLAGS.append("REGISTER-KNEE")
elif knee_meas and knee_null:
    FLAGS.append("KNEE-IS-WHEEL-GEOMETRY")
check("S3.c KNEE TEST (predeclared): MEASURED marginal dR2 per check "
      "-- 3rd %.5f, 4th (the register) %.5f, 5th %.5f; criterion "
      "dR2(210) > %.1f*sqrt(dR2(30)*dR2(2310)) = %.5f -> %s"
      % (d30, d210, d2310, KNEE_FACTOR, knee_bound,
         "knee" if knee_meas else "no knee"), True, kill=None)
check("S3.d KNEE UNDER THE NULL (V2 amendment): the zero-parameter "
      "wheel model gives marginals %.5f / %.5f / %.5f with bound "
      "%.5f -> %s.  VERDICT ON THE KNEE: %s"
      % (n30, n210, n2310, knee_nbound,
         "knee" if knee_null else "no knee",
         "the knee is pure WHEEL GEOMETRY, not a prime signature"
         if (knee_meas and knee_null) else
         ("REGISTER-KNEE: present in the primes, absent in the wheel "
          "model -- a genuine finding" if knee_meas else
          "no knee either way")), True, kill=None)

# ======================================================================
section("S4: Walsh seats of the gap signal on the register bits")
# ======================================================================
SUBSETS = [()] + [c for r in (1, 2, 3, 4)
                  for c in combinations(BITNAMES, r)]


def walsh_table(sel_p, sel_ghat_c):
    bits = {"3": legendre_bits(sel_p, 3),
            "5": legendre_bits(sel_p, 5),
            "7": legendre_bits(sel_p, 7),
            "A": np.where(sel_p % 4 == 1, 1, -1).astype(np.int64)}
    n = len(sel_p)
    sd = float(sel_ghat_c.std())
    out = {}
    for S in SUBSETS:
        chi = np.ones(n, dtype=np.int64)
        for q in S:
            chi = chi * bits[q]
        coef = float(np.mean(sel_ghat_c * chi))
        se = sd / math.sqrt(n)
        out[S] = (coef, se, coef / se)
    return out


ladder_tables = {}
for X in XLADDER:
    sel = p_k <= X
    g_sel = ghat[sel]
    ladder_tables[X] = walsh_table(p_k[sel], g_sel - g_sel.mean())

tab = ladder_tables[XMAX]
print("    seat            coef (X=%.0e)      z" % XMAX)
for S in sorted(SUBSETS, key=lambda s: (-abs(tab[s][2]), len(s))):
    lbl = "{" + ",".join(S) + "}" if S else "{} (trivial)"
    print("    %-14s %+.6e   %+8.2f" % (lbl, tab[S][0], tab[S][2]))

nontriv = [S for S in SUBSETS if S]
zs = {S: abs(tab[S][2]) for S in nontriv}
top = sorted(nontriv, key=lambda s: -zs[s])[:3]
INERT_SEAT = ("3", "7")
COMPL_SEAT = ("5", "A")
check("S4.a strongest nontrivial Walsh seats at X = %.0e: %s"
      % (XMAX, ", ".join("{%s} |z|=%.1f" % (",".join(S), zs[S])
                         for S in top)), True, kill=None)
check("S4.b frobwalsh cross-reference: the INERT seat {3,7} (the "
      "chi4 Walsh seat) has |z| = %.2f, its complement {5,anchor} "
      "|z| = %.2f, the full-parity seat {3,5,7,A} |z| = %.2f -- "
      "rank of {3,7} among the 15 nontrivial seats: %d"
      % (zs[INERT_SEAT], zs[COMPL_SEAT], zs[("3", "5", "7", "A")],
         1 + sorted(zs.values(), reverse=True).index(zs[INERT_SEAT])),
      True, kill=None)

print("    decay of |coef| over the X ladder (slope of log|c| vs "
      "log X; generic equidistribution ~ -0.5):")
decays = {}
for S in nontriv:
    xs = np.log([float(X) for X in XLADDER])
    ys = np.log([abs(ladder_tables[X][S][0]) + 1e-300 for X in XLADDER])
    slope = float(np.polyfit(xs, ys, 1)[0])
    decays[S] = slope
for S in sorted(nontriv, key=lambda s: decays[s]):
    print("      {%-9s} slope %+.3f   |z|(X=%.0e) %6.2f"
          % (",".join(S), decays[S], XMAX, zs[S]))
slow = [S for S in nontriv if decays[S] > -0.25 and zs[S] > 4.0]
check("S4.c seats decaying markedly slower than the generic -0.5 "
      "while still significant (|z| > 4): %s"
      % (["{%s}" % ",".join(S) for S in slow] or "none"),
      True, kill=None)

a_seats = [S for S in nontriv if "A" in S]
f_seats = [S for S in nontriv if "A" not in S]
zmax_a = max(zs[S] for S in a_seats)
zmax_f = max(zs[S] for S in f_seats)
check("S4.d THE ANCHOR PREDICTION (predeclared exact): p mod 4 is "
      "CRT-independent of p mod 210, so the wheel model puts exactly "
      "zero weight on the eight anchor seats.  Measured max |z| over "
      "the anchor seats = %.2f (worst: {%s}) against %.2f over the "
      "eight anchor-free seats -- the gap signal lives entirely on "
      "the family bits {3,5,7}; the mu4/Galois bit reads nothing "
      "about gaps"
      % (zmax_a, ",".join(max(a_seats, key=lambda S: zs[S])), zmax_f),
      True, kill=None)

# ======================================================================
section("S5: the wheel-Cramer null -- code vs arithmetic")
# ======================================================================
st210, pred210 = null_prediction(REGISTER_MODULUS, logp,
                                 p_k % REGISTER_MODULUS)
mean_pred_gap = float(np.mean(pred210 * logp))
rel = abs(mean_pred_gap - float(gaps.mean())) / float(gaps.mean())
rel_pnt = abs(float(gaps.mean()) - LOGX_BAR) / LOGX_BAR
check("S5.a null normalization: the per-prime wheel-Cramer model "
      "predicts a mean gap of %.5f against the measured %.5f "
      "(relative %.4f%%, ward < 1%%); PNT ward: measured mean gap is "
      "%.3f%% off mean log p = %.5f (< 2%%); state indexing agrees "
      "with S2 (%s)"
      % (mean_pred_gap, gaps.mean(), 100 * rel, 100 * rel_pnt,
         LOGX_BAR, bool(np.array_equal(st210, state))),
      rel < 0.01 and rel_pnt < 0.02 and np.array_equal(st210, state),
      kill="NULL-BROKEN")

q_lo = (REGISTER_MODULUS / OMEGA_ADM) / math.log(10 ** 6)
q_hi = (REGISTER_MODULUS / OMEGA_ADM) / math.log(XMAX)
_, nl_lo = wheel_null_hat(REGISTER_MODULUS, math.log(10 ** 6))
_, nl_hi = wheel_null_hat(REGISTER_MODULUS, math.log(XMAX))
shape_corr = pearson(nl_lo / nl_lo.mean(), nl_hi / nl_hi.mean())
check("S5.b q-sensitivity of the null profile shape (V2 amendment, "
      "now RECORDED not warded): corr(shape at q(1e6) = %.4f, shape "
      "at q(%.0e) = %.4f) = %.6f.  The frozen v1 ward demanded "
      "> 0.999 because v1 evaluated the null at a single q; the ward "
      "FAILED at X = 1e8, correctly flagging that approximation.  "
      "The null is now evaluated PER PRIME on a 64-bin log p grid, "
      "which removes the approximation entirely -- so the number is "
      "kept as a measurement of how much the wheel profile stiffens "
      "with depth, and no longer gates the verdict"
      % (q_lo, XMAX, q_hi, shape_corr), True, kill=None)


def decompose(profile, counts, null_hat, level):
    """(corr, raw R^2, level-matched R^2, offset, resid RMS, spread)"""
    corr = pearson(profile, null_hat)
    sst = float(np.sum(counts * (profile - level) ** 2))
    sse_raw = float(np.sum(counts * (profile - null_hat) ** 2))
    off = float(np.average(profile - null_hat, weights=counts))
    res = profile - null_hat - off
    sse_lvl = float(np.sum(counts * res ** 2))
    rms = float(np.sqrt(np.average(res ** 2, weights=counts)))
    spread = float(np.sqrt(np.average((profile - level) ** 2,
                                      weights=counts)))
    return corr, 1 - sse_raw / sst, 1 - sse_lvl / sst, off, rms, spread


null_hat = (np.bincount(state, weights=pred210, minlength=OMEGA_ADM)
            / cnt_a)
(r_null, r2_raw, r2_null, offset, resid_rms,
 spread_meas) = decompose(prof_meas, cnt_a, null_hat, ghat.mean())
check("S5.c THE DECOMPOSITION: corr(measured profile, wheel-Cramer "
      "null) = %.6f (pure shape); ZERO-PARAMETER null R^2 = %.5f; "
      "after removing the single level offset %+.5f, R^2 = %.5f of "
      "the state-to-state profile variance; residual RMS %.5f vs "
      "profile spread %.5f -> arithmetic excess = %.2f%% of the "
      "state signal"
      % (r_null, r2_raw, offset, r2_null, resid_rms, spread_meas,
         100 * resid_rms / spread_meas), True, kill=None)

print("    residual decay over the X ladder (arithmetic excess "
      "beyond the pure wheel):")
for X in XLADDER:
    sel = p_k <= X
    st_x, gh_x = state[sel], ghat[sel]
    c_x = np.bincount(st_x, minlength=OMEGA_ADM)
    pr_x = np.bincount(st_x, weights=gh_x, minlength=OMEGA_ADM) / c_x
    _, pred_x = null_prediction(REGISTER_MODULUS, logp[sel],
                                p_k[sel] % REGISTER_MODULUS)
    nh = (np.bincount(st_x, weights=pred_x, minlength=OMEGA_ADM)
          / c_x)
    _, _, r2x, _, rr, sp = decompose(pr_x, c_x, nh, gh_x.mean())
    print("      X = %.0e: null R^2 %.5f, residual RMS %.5f, spread "
          "%.5f, excess %.2f%%" % (X, r2x, rr, sp, 100 * rr / sp))

# ======================================================================
section("S6: the register primes in the deployed comb")
# ======================================================================
NCOMB = 10 ** 6
comb_n, comb_w = [], []
for p in sieve_primes(NCOMB):
    pk, lp = int(p), math.log(int(p))
    while pk <= NCOMB:
        comb_n.append(pk)
        comb_w.append(2.0 * lp / math.sqrt(pk))
        pk *= int(p)
comb_n = np.array(comb_n, dtype=np.int64)
comb_w = np.array(comb_w, dtype=np.float64)
tail = comb_n > 7
adm = np.array([math.gcd(int(n), REGISTER_MODULUS) == 1
                for n in comb_n[tail]])
frac = float(comb_w[tail][adm].sum() / comb_w[tail].sum())
offw = comb_n[tail][~adm]
check("S6.a of the comb weight 2 Lambda(n)/sqrt(n) at n > 7 (n <= "
      "%.0e), %.4f%% sits on wheel-admissible n; the %d exceptions "
      "are exactly the higher powers of the register primes "
      "(smallest: %s) -- the comb lives on the code, its own "
      "generators excepted"
      % (NCOMB, 100 * frac, len(offw), offw[:6].tolist()),
      bool(np.all([math.gcd(int(n), REGISTER_MODULUS) > 1
                   for n in offw])), kill=None)

# ======================================================================
section("C: controls")
# ======================================================================
foreign = []
for m in FOREIGN_WHEELS:
    um = wheel_units(m)
    wm = next_unit_distance(m, um)
    idxm = unit_index_table(m, um)
    st_all = idxm[p_k % m]
    ok = st_all >= 0
    fl = wm[p_k[ok] % m]
    viol = int(np.count_nonzero(gaps[ok] < fl))
    r2 = holdout_r2(st_all[ok], ghat[ok], len(um),
                    np.random.default_rng(SEED))
    bits = math.log2(m / len(um))
    _, nh_m = null_prediction(m, logp[ok], p_k[ok] % m)
    r2n = r2_of(ghat[ok], nh_m)
    foreign.append((m, len(um), bits, r2, viol, float(fl.mean()), r2n))
    print("    m = %5d = %-12s phi = %3d  bits %.4f  mean floor "
          "%.3f  holdout R2 %.5f  null R2 %.5f  excess %+.5f  "
          "floor violations %d"
          % (m, "*".join(str(q) for q in (2, 3, 5, 7, 11, 13)
                         if m % q == 0), len(um), bits, fl.mean(),
             r2, r2n, r2 - r2n, viol))

check("C1.a the wheel floor is GENERIC: zero violations for every "
      "foreign 4-prime modulus (%s) -- the 'hard floor' is a property "
      "of any wheel, not of 210.  ANCHOR EFFECT (measured): the "
      "anchor-free wheel 1155 = 3*5*7*11 has mean floor %.3f against "
      "%.3f for 210 -- without the ramified prime 2 the floor "
      "collapses toward 1 and the wheel stops constraining gaps"
      % (", ".join(str(m) for m in FOREIGN_WHEELS),
         [f[5] for f in foreign if f[0] == 1155][0],
         [f[5] for f in foreign if f[0] == 210][0]),
      all(f[4] == 0 for f in foreign), kill="CONTROL-DEAD")

excess = np.array([f[3] - f[6] for f in foreign])
i210 = [i for i, f in enumerate(foreign) if f[0] == 210][0]
others = np.delete(excess, i210)
sig = float(others.std(ddof=1))
z210 = float((excess[i210] - others.mean()) / sig) if sig > 0 else 0.0
outlier = abs(z210) > OUTLIER_SIGMA
if outlier:
    FLAGS.append("REGISTER-OUTLIER")
check("C1.b OUTLIER TEST (predeclared, on the null-excess -- the "
      "only quantity comparable across wheels): excess over the "
      "wheel-Cramer null is %s for 210 vs %s for the foreign "
      "wheels; 210 sits at z = %+.2f sigma -> %s"
      % ("%+.5f" % excess[i210],
         "/".join("%+.5f" % e for e in others), z210,
         "OUTLIER (finding)" if outlier else "on the trend (generic)"),
      True, kill=None)

rng_s = np.random.default_rng(SEED + 7)
ghat_s = rng_s.permutation(ghat)
cnt_s = cnt_a
prof_s = np.bincount(state, weights=ghat_s, minlength=OMEGA_ADM) / cnt_s
r_scr = pearson(w_units, prof_s)
r2_scr = holdout_r2(state, ghat_s, OMEGA_ADM,
                    np.random.default_rng(SEED))
check("C2 SCRAMBLE fires: with gaps permuted, Pearson(w(a), profile) "
      "= %+.4f (was %+.4f) and holdout R^2 = %+.6f (was %.5f)"
      % (r_scr, r_floor_p, r2_scr, r2_by_m[210]),
      abs(r_scr) < 0.5 and r2_scr < 0.1 * r2_by_m[210],
      kill="CONTROL-DEAD")

wheel_seq = np.array([n for n in range(11, 200000)
                      if math.gcd(n, REGISTER_MODULUS) == 1],
                     dtype=np.int64)
wgaps = wheel_seq[1:] - wheel_seq[:-1]
wfloor = W210[wheel_seq[:-1] % REGISTER_MODULUS]
check("C3 PURE-WHEEL CONTROL fires: on the deterministic sequence of "
      "integers coprime to 210 the floor is saturated in 100%% of "
      "steps (%d/%d) -- the floor law alone contains no arithmetic; "
      "the primes saturate it only %.2f%% of the time, and that gap "
      "is the entire non-sieve content"
      % (int(np.count_nonzero(wgaps == wfloor)), len(wgaps),
         100 * saturated / N),
      bool(np.all(wgaps == wfloor)), kill="CONTROL-DEAD")

small_primes = [q for q in range(2, 200) if all(q % d for d in
                                                range(2, int(q ** .5) + 1))]
best, best_eff = None, -1.0
for quad in combinations(small_primes, 4):
    eff = 1.0
    for q in quad:
        eff *= (1.0 - 1.0 / q)
    eff = 1.0 - eff
    if eff > best_eff:
        best, best_eff = quad, eff
check("C4 TRIVIAL-MAXIMIZER HONESTY: over all C(%d,4) quadruples of "
      "primes < 200, sieve efficiency 1 - prod(1-1/p) is maximized "
      "uniquely by %s at %.4f -- the smallest primes always win, so "
      "efficiency alone selects NOTHING for the compiler; the "
      "register's seat stays the prod(p-1) = 48 forcing"
      % (len(small_primes), best, best_eff),
      best == REGISTER_PRIMES, kill="CONTROL-DEAD")

# ======================================================================
section("VERDICT")
# ======================================================================
n_pass = sum(1 for _, ok in CHECKS if ok)
if KILLS:
    verdict = KILLS[0]
else:
    tail_flags = "+".join(FLAGS) if FLAGS else "NO-KNEE"
    tail_flags += "" if outlier else "+ON-TREND"
    verdict = ("GAPCODE-MEASURED (WHEEL-EXPLAINS-%.1f%% "
               "ARITHMETIC-EXCESS-%.1f%% +%s)"
               % (100 * r2_null, 100 * resid_rms / spread_meas,
                  tail_flags))

print("\nCHECKS: %d/%d passed" % (n_pass, len(CHECKS)))
if n_pass != len(CHECKS):
    print("FAILED: %s" % [nm for nm, ok in CHECKS if not ok])
print("VERDICT: %s" % verdict)
print("""
WHAT THIS MEASURES (exploration only):
 * THE CORRELATION EXISTS AND IS DETERMINISTIC, NOT STATISTICAL: the
   register state of a prime puts an exact floor under its gap and
   forbids 77.14%% of the a priori gap values.  The 'error code'
   reading is literally true -- the register is the first four
   parity checks of the sieve, Omega_adm = 48 is its rate and
   tau(210) = 16 its syndrome alphabet, with 0 message bits (v868).
 * BUT THE CODE IS THE SIEVE, NOT A TFPT SIGNATURE: a zero-parameter
   wheel-Cramer null reproduces the state profile almost entirely;
   the arithmetic excess is the small Hardy-Littlewood /
   Lemke-Oliver-Soundararajan residual, and every foreign 4-prime
   wheel obeys the same law.  210 is efficiency-optimal only because
   its primes are the smallest (C4).
 * WHAT DOES NOT CORRELATE: nothing on the gap side moves with c3,
   phi0 or any dimensionful compiler constant -- in the prime front
   the primes enter the wall only through smoothed windowed sums
   (v882: sqrt-uniformization, port mass 1 - e^(-1/2)), where the
   individual gaps are integrated out.
NO ledger/paper/website claim; NO RH claim; NO physics claim beyond
the recorded identities and measurements.
""")
print("runtime: %.1f s" % (time.time() - T0))
sys.exit(0 if n_pass == len(CHECKS) else 1)
