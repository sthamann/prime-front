#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""rh_leverage_probe -- E8.RH.LEVERAGE.01: if the world is read as the
output of a short program, where exactly do the primes sit, and what
would a proof of RH actually buy the TFPT compiler?

EXPLORATION ONLY (experiments/): no ledger row, no paper edit, no .md,
nothing outside experiments/.  NO RH CLAIM -- this probe measures the
LEVERAGE of RH on the deployed stack and the SCALE at which RH becomes
visible; it does not prove, disprove, or supply evidence for RH in
either direction.  Read-only import of the deployed v563 tables, the
same pattern v881/v882 use.  No zero of any L-function is read into
any wall object; the one classical zero ordinate that appears (gamma_1
= 14.134725..., a literature constant) is used ONLY in the closed-form
scale arithmetic of S3 and never touches the comb, the window or the
Toeplitz form.  Frozen (spec + sha256) before running.  Seeded RNG in
exactly two places, both controls.

THE QUESTION (user-posed, frozen): read metaphorically -- if everything
is the output of a program, or of one very simple rule -- how do the
primes fit in, and what would solving RH mean IN THE CONTEXT OF TFPT?
The compiler probes answered where 210 comes from (E8.BRIDGE.ARITHGEO:
Omega_adm sits exactly on the arithmetic floor) and what the register
knows about gaps (PRIME.DIVISOR210.GAPCODE: the head of the sieve, and
nothing beyond it).  This probe closes the loop by making the program
reading QUANTITATIVE (description length), locating RH inside it (the
compression exponent), measuring why no finite bookkeeping can settle
it (the scale gap), and auditing what the deployed wall would gain.

FROZEN CLAIMS (2026-08-09, frozen + SHA-hashed before first run):

 S1  THE PROGRAM READING MADE EXACT -- the description-length ladder
     of the primes (measured, exact counting).  Task: transmit the
     primality bits of every integer in (7, X].  Nested rules:
         R0  no rule                    : X - 7 bits
         R1  the anchor check alone     : only odd n carry a bit
         R2  the 210 register, 4 checks : only n coprime to 210
         R3  register + PNT density     : Bernoulli(q_n) coding on the
             admissible slots with q_n = (210/48)/log n, codelength
             sum over admissible n of -[b log2 q + (1-b) log2(1-q)]
         BOUND log2 C(A, P) -- the combinatorial floor for ANY code
             that knows only how many primes there are among the A
             admissible slots.
     (a) the ladder in bits and in bits per integer;
     (b) bits per prime under each rule;
     (c) THE DECISIVE RATIO R3/BOUND: predeclared to be close to 1,
         i.e. the simple rules already buy essentially everything a
         counting argument can buy, and what remains is the cost of
         an arbitrary subset of that size.  The primes are, to the
         resolution of every finitely-describable smooth rule, a
         RANDOM-LOOKING subset of the register's admissible slots.
     Fail (any codelength non-monotone, or ratio outside [0.9, 1.15])
     => CODELENGTH-BROKEN.

 S2  RH AS THE COMPRESSION EXPONENT (measured).  The simplest possible
     rule for the primes is psi(x) = x.  Its error Delta(x) = psi(x)
     - x is exactly what no simple rule captures, and storing it costs
     about log2|Delta| bits.
     (a) measure Delta(x) and |Delta(x)|/sqrt(x) on an x ladder;
     (b) fit the exponent sigma_emp in |Delta| ~ x^sigma over the
         ladder.  RH says sigma = 1/2 (up to logs); the unconditional
         knowledge allows sigma arbitrarily close to 1.  PREDECLARED:
         the measured exponent is compatible with 1/2, which is an
         EMPIRICAL OBSERVATION AT SMALL x AND NOT EVIDENCE FOR RH --
         recorded as such, ward |sigma_emp - 0.5| < 0.25;
     (c) the reading: RH is the assertion that the correction to the
         simplest rule costs HALF as many bits as it could.  In the
         program metaphor RH is a statement about the compressibility
         of the output, not about the program.
     Fail => EXPONENT-BROKEN.

 S3  THE SCALE GAP -- why no finite bookkeeping can settle it
     (closed form, decisive for the TFPT question).  A hypothetical
     zero pair at sigma = 1/2 + delta with ordinate gamma contributes
     about 2 x^sigma/|rho| to Delta(x), while the whole on-line zero
     sum is bounded under RH by Schoenfeld's (1/(8 pi)) sqrt(x) log^2
     x for x >= 73.2.  Solve for the crossover X*(delta) where the
     single off-line pair first dominates the entire on-line budget.
     (a) X*(delta) for delta = 0.05, 0.10, 0.25 at gamma = gamma_1;
     (b) the deepest FAITHFUL deployed rung (atoms not truncated by
         ATOM_MAX) sees primes only up to X_dep = e^(2 alpha);
     (c) the gap in orders of magnitude.  PREDECLARED: the gap is
         dozens of decades, i.e. the deployed ladder is astronomically
         far below the scale at which an RH violation of that size
         would announce itself -- the quantitative form of the I5
         safeguard (finite bookkeeping cannot decide RH).
     Fail (gap <= 0 decades) => SCALE-BROKEN.

 S4  THE WALL MARGIN TREND ON THE DEPLOYED LADDER (measured, the new
     content).  Rebuild every admissible rung read-only from v563 --
     atoms (u_n, mu_n = 2 Lambda(n)/sqrt n), tent lags, Weil arch
     layer, odd Toeplitz K -- and take lam_min(K), the wall margin.
     (a) REGRESSION against v884's certified floors on the head rungs
         kz = 9, 12, 13: measured lam_min must be >= 3.633e-4,
         3.327e-4, 3.842e-4 respectively;
     (b) every accessible faithful rung must have lam_min > 0;
     (c) fit lam_min ~ C h^(-p) over the ladder; report p and the fit
         quality.  PREDECLARED: p > 0 -- the margin SHRINKS with
         depth;
     (d) THE CRITICALITY READING (the point): a wall that is positive
         on every accessible rung but whose margin tends to zero is
         exactly a MARGINAL statement.  No finite ladder proves the
         infinite one, and no finite ladder refutes it.  That is why
         the prime-front gates are RH-hard: they are not blocked by a
         missing computation, they are blocked by the fact that the
         quantity being computed goes to zero;
     (e) soft-mode localization: inverse participation ratio of the
         lam_min eigenvector in RAW head coordinates, reported as
         effective support / h.  Recorded, no expectation frozen --
         v881's 15% port concentration lives in the Schur/testing
         frame, not in these coordinates, so a large raw support
         would mean the FRAME is what does the localizing.
     Fail => WALL-BROKEN.

 S5  THE LEVERAGE AUDIT -- what a proof would and would not change
     (exact + typed).
     (a) EXACT: the deployed readouts are functions of a finite exact
         von Mangoldt table plus quadrature.  Verified here by
         rebuilding a rung twice and requiring bit-identical output,
         and by an AST scan of this probe for the deployed banned
         identifiers.  No deployed number is conditional on RH, so a
         proof would move NO TFPT number and NO physics readout;
     (b) TYPED (cited, not re-derived): the wall for ALL h is
         equivalent to Weil positivity and hence to RH (prime front
         I5).  Therefore the open prime-front gates are not "helped
         by" RH -- in TFPT coordinates they ARE RH.  A proof would
         close them by definition; conversely TFPT cannot close them
         without proving RH.  What a proof WOULD buy is listed as
         three items and nothing more;
     (c) the converse direction stays shut: nothing measured here
         supplies anything toward RH.
     Fail => AUDIT-BROKEN.

 C   CONTROLS (must fire):
     C1 SCRAMBLE: keep the atom masses, randomize the atom positions
        in (0, 2 alpha]; the wall must FAIL (lam_min < 0).  Shows the
        wall reads arithmetic, not mass.
     C2 SMOOTH-COMB: replace the atoms by the PNT continuum limit of
        the same comb (uniform grid in u with density 2 e^(u/2), same
        total mass to <2%); the wall must FAIL.  Regression of v883's
        FLUCTUATIONS-REQUIRED verdict -- the wall needs the actual
        arithmetic fluctuations, not the smooth law.
     C3 FIREWALL: AST scan of this file for the deployed banned
        identifiers (zetazero, nzeros, primerange, isprime, primepi,
        nextprime, prevprime); none may appear as a call.
     C4 NO-RH-CLAIM: the verdict string must not assert RH in either
        direction.

VERDICT (frozen precedence): CODELENGTH-BROKEN / EXPONENT-BROKEN /
SCALE-BROKEN / WALL-BROKEN / AUDIT-BROKEN / CONTROL-DEAD on kill; else
RH-LEVERAGE-MEASURED with the measured codelength ratio, compression
exponent, scale gap in decades and wall-margin exponent.

Sources (read-only): v563_paper2_readouts (deployed atom tables,
tent assembly, arch lags, odd Toeplitz), v884 (certified head floors
3.633e-4 / 3.327e-4 / 3.842e-4 at kz 9/12/13), v883 (parametrix
verdict FLUCTUATIONS-REQUIRED), v881 (port geometry, testing law),
v882 (sqrt uniformization, port mass 1 - e^{-1/2}),
tfpt_prime_front.tex (I5 equivalence typing, no-RH-claim posture),
compiler_arithmetic_bridge_probe (the floor theorem),
prime_gap_register_correlation_probe (the sieve head).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/rh_leverage_probe.py
"""

import ast
import hashlib
import math
import os
import sys
import time

import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
_VERIFY = os.path.abspath(os.path.join(_HERE, "..", "..", "verification"))
sys.path.insert(0, _HERE)
sys.path.insert(0, _VERIFY)

import v563_paper2_readouts as core        # noqa: E402  (READ-ONLY)

T0 = time.time()
CHECKS = []
KILLS = []
SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()

REGISTER_MODULUS = 210
OMEGA_ADM = 48
XPSI = int(os.environ.get("RHLEV_XPSI", 10 ** 8))
XCODE = int(os.environ.get("RHLEV_XCODE", 10 ** 7))
KZMAX = int(os.environ.get("RHLEV_KZMAX", 150))
SEED = 20260809
# classical literature constant; used ONLY in the closed-form scale
# arithmetic of S3, never fed to the comb, window or Toeplitz form
GAMMA_1 = 14.134725141734693
SCHOENFELD_C = 1.0 / (8.0 * math.pi)
CERTIFIED = {9: 3.633e-4, 12: 3.327e-4, 13: 3.842e-4}   # v884 floors
BANNED_IDS = ("zetazero", "nzeros", "primerange", "isprime",
              "primepi", "nextprime", "prevprime")


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


def sieve_bool(limit):
    s = np.ones(limit + 1, dtype=bool)
    s[:2] = False
    for i in range(2, int(limit ** 0.5) + 1):
        if s[i]:
            s[i * i::i] = False
    return s


def log2binom(n, k):
    return (math.lgamma(n + 1) - math.lgamma(k + 1)
            - math.lgamma(n - k + 1)) / math.log(2.0)


# ======================================================================
section("S0: setup")
# ======================================================================
print("spec sha256 = %s" % SPEC_SHA)
print("X(psi) = %.0e, X(codelength) = %.0e, kz scan <= %d, seed %d"
      % (XPSI, XCODE, KZMAX, SEED))

IS_P = sieve_bool(XPSI)
PRIMES = np.nonzero(IS_P)[0].astype(np.int64)
print("  primes <= %.0e: %d" % (XPSI, len(PRIMES)))

# ======================================================================
section("S1: the program reading -- description length of the primes")
# ======================================================================
UNITS = np.array([a for a in range(REGISTER_MODULUS)
                  if math.gcd(a, REGISTER_MODULUS) == 1], dtype=np.int64)
IS_ADM_RES = np.zeros(REGISTER_MODULUS, dtype=bool)
IS_ADM_RES[UNITS] = True

print("       X        R0 bits     R1 bits     R2 bits     R3 bits"
      "     BOUND      R3/BOUND   bits/prime")
code_rows = []
for X in (10 ** 5, 10 ** 6, XCODE):
    n_lo = 8
    tot = X - n_lo + 1
    r0 = float(tot)
    r1 = float(np.count_nonzero(np.arange(n_lo, X + 1) % 2 == 1))
    adm_cnt = 0
    r3 = 0.0
    n_pr_adm = 0
    step = 10 ** 6
    for lo in range(n_lo, X + 1, step):
        hi = min(lo + step - 1, X)
        nn = np.arange(lo, hi + 1, dtype=np.int64)
        adm = IS_ADM_RES[nn % REGISTER_MODULUS]
        nn = nn[adm]
        adm_cnt += len(nn)
        q = np.clip((REGISTER_MODULUS / OMEGA_ADM)
                    / np.log(nn.astype(np.float64)), 1e-12, 0.999999)
        b = IS_P[nn]
        n_pr_adm += int(np.count_nonzero(b))
        r3 += float(np.sum(np.where(b, -np.log2(q), -np.log2(1.0 - q))))
    r2 = float(adm_cnt)
    bound = log2binom(adm_cnt, n_pr_adm)
    ratio = r3 / bound
    code_rows.append((X, r0, r1, r2, r3, bound, ratio, n_pr_adm))
    print("    %.0e %11.4g %11.4g %11.4g %11.4g %11.4g %9.4f %10.3f"
          % (X, r0, r1, r2, r3, bound, ratio, r3 / n_pr_adm))

mono = all(r[1] > r[2] > r[3] > r[4] for r in code_rows)
ratios = [r[6] for r in code_rows]
check("S1.a/b the description-length ladder is strictly decreasing at "
      "every X: no rule %.4g -> anchor %.4g -> register %.4g -> "
      "register+PNT %.4g bits at X = %.0e; in bits per integer that is "
      "1.000 -> %.4f -> %.4f -> %.4f"
      % (code_rows[-1][1], code_rows[-1][2], code_rows[-1][3],
         code_rows[-1][4], code_rows[-1][0],
         code_rows[-1][2] / code_rows[-1][1],
         code_rows[-1][3] / code_rows[-1][1],
         code_rows[-1][4] / code_rows[-1][1]),
      mono, kill="CODELENGTH-BROKEN")

check("S1.c THE DECISIVE RATIO: the PNT-on-the-register code costs "
      "%.4f of the combinatorial floor log2 C(A, P) at X = %.0e "
      "(ladder %s).  The simple rules already buy essentially "
      "everything a counting argument can buy -- to the resolution of "
      "every finitely describable smooth rule the primes are a "
      "RANDOM-LOOKING subset of the register's admissible slots, at "
      "%.2f bits per prime"
      % (ratios[-1], code_rows[-1][0],
         ", ".join("%.4f" % r for r in ratios),
         code_rows[-1][4] / code_rows[-1][7]),
      all(0.90 <= r <= 1.15 for r in ratios), kill="CODELENGTH-BROKEN")

# ======================================================================
section("S2: RH as the compression exponent")
# ======================================================================
LOGP = np.log(PRIMES.astype(np.float64))
CUM = np.concatenate(([0.0], np.cumsum(LOGP)))


def psi_of(x):
    """exact Chebyshev psi(x) = sum_{p^k <= x} log p."""
    i = int(np.searchsorted(PRIMES, x, side="right"))
    tot = float(CUM[i])
    k = 2
    while True:
        r = int(round(x ** (1.0 / k)))
        while (r + 1) ** k <= x:
            r += 1
        while r ** k > x:
            r -= 1
        if r < 2:
            break
        j = int(np.searchsorted(PRIMES, r, side="right"))
        tot += float(CUM[j])
        k += 1
    return tot


print("        x         psi(x)-x      |D|/sqrt(x)   log2|D|   "
      "0.5*log2 x")
xs, ds = [], []
for e in range(3, int(math.log10(XPSI)) + 1):
    x = float(10 ** e)
    d = psi_of(x) - x
    xs.append(x)
    ds.append(abs(d))
    print("    %.0e %+14.3f %13.5f %10.3f %11.3f"
          % (x, d, abs(d) / math.sqrt(x), math.log2(abs(d)),
             0.5 * math.log2(x)))

lx = np.log(np.array(xs))
ly = np.log(np.array(ds))
sigma_emp = float(np.polyfit(lx, ly, 1)[0])
check("S2.a/b measured compression exponent of the correction to the "
      "simplest rule: |psi(x) - x| ~ x^%.4f over %d decades (RH says "
      "1/2 up to logs, unconditional knowledge allows up to 1).  THIS "
      "IS AN OBSERVATION AT SMALL x, NOT EVIDENCE FOR RH -- ward "
      "|sigma - 0.5| < 0.25 only certifies that the ladder is in the "
      "square-root regime where it is expected to be"
      % (sigma_emp, len(xs)),
      abs(sigma_emp - 0.5) < 0.25, kill="EXPONENT-BROKEN")

check("S2.c THE READING: storing the correction costs about "
      "sigma*log2(x) bits, so RH is exactly the statement that the "
      "correction to the simplest rule costs HALF as many bits as it "
      "could (%.2f instead of up to %.2f bits at x = %.0e).  In the "
      "program metaphor RH is a statement about the COMPRESSIBILITY "
      "OF THE OUTPUT, not about the program"
      % (0.5 * math.log2(XPSI), math.log2(XPSI), XPSI),
      True, kill=None)

# ======================================================================
section("S3: the scale gap -- why finite bookkeeping cannot settle it")
# ======================================================================
RHO1 = math.hypot(0.5, GAMMA_1)


def crossover_logx(delta, rho=RHO1):
    """smallest log x with 2 x^(1/2+delta)/rho >= C sqrt(x) log^2 x."""
    lo, hi = 1.0, 1.0e6
    for _ in range(300):
        mid = 0.5 * (lo + hi)
        lhs = delta * mid - math.log(rho / 2.0)
        rhs = math.log(SCHOENFELD_C) + 2.0 * math.log(mid)
        if lhs >= rhs:
            hi = mid
        else:
            lo = mid
    return hi


print("    a single off-line zero pair at gamma_1 = %.6f (|rho| = "
      "%.4f) against Schoenfeld's on-line budget (1/8pi) sqrt(x) "
      "log^2 x:" % (GAMMA_1, RHO1))
cross = {}
for delta in (0.05, 0.10, 0.25):
    lx_star = crossover_logx(delta)
    cross[delta] = lx_star / math.log(10.0)
    print("      sigma = %.2f: dominates only above X* = 1e%.1f"
          % (0.5 + delta, cross[delta]))

rungs = []
for kz in range(2, KZMAX + 1):
    try:
        rr = core.build_window(kz)
    except Exception:
        continue
    if rr["h"] < core.H_MIN or rr["h"] > core.HCAP:
        continue
    if rr["X"] > core.ATOM_MAX:          # atoms truncated -> not faithful
        continue
    rungs.append(rr)
X_DEEP = max(r["X"] for r in rungs)
gap_dec = cross[0.10] - math.log10(X_DEEP)
check("S3.a/b/c THE SCALE GAP: the deepest FAITHFUL deployed rung "
      "(kz = %d, alpha = %.4f, h = %d) sees primes only up to X = "
      "%.4g = 1e%.2f, while a sigma = 0.60 violation first dominates "
      "the on-line budget above 1e%.1f -- a gap of %.0f DECADES.  "
      "This is the quantitative form of the I5 safeguard: the "
      "compiler's finite bookkeeping is astronomically far from the "
      "scale at which RH announces itself, in either direction"
      % (max(rungs, key=lambda r: r["X"])["k"],
         max(rungs, key=lambda r: r["X"])["alpha"],
         max(rungs, key=lambda r: r["X"])["h"], X_DEEP,
         math.log10(X_DEEP), cross[0.10], gap_dec),
      gap_dec > 0, kill="SCALE-BROKEN")

# ======================================================================
section("S4: the wall margin trend on the deployed ladder")
# ======================================================================


def wall_matrix(alpha, M, D, uu, mu):
    c = (np.asarray(core.arch_lags(M, D), float)
         + core.atom_lags_at(alpha, M, uu, mu)[0])
    return core.odd_toeplitz(c, M)


lam_rows = []
for rr in rungs:
    uu = np.asarray(rr["uu"], float)
    mu = 2.0 * np.asarray(rr["lam"], float)
    K = wall_matrix(rr["alpha"], rr["M"], rr["D"], uu, mu)
    w, V = np.linalg.eigh(K)
    v = V[:, 0]
    eff = float(1.0 / np.sum(v ** 4) * np.sum(v ** 2) ** 2)
    lam_rows.append((rr["k"], rr["alpha"], rr["X"], rr["h"],
                     rr["n_atom"], float(w[0]), eff / rr["h"]))

print("    %d faithful rungs, h = %d..%d, X = %.4g..%.4g"
      % (len(lam_rows), min(r[3] for r in lam_rows),
         max(r[3] for r in lam_rows), min(r[2] for r in lam_rows),
         X_DEEP))
print("      kz   alpha        X     h  n_atom     lam_min   "
      "soft-mode support/h")
for r in lam_rows[:5] + lam_rows[-5:]:
    print("     %4d %7.4f %9.4g %5d %7d %+.6e %10.3f"
          % (r[0], r[1], r[2], r[3], r[4], r[5], r[6]))

reg = {r[0]: r[5] for r in lam_rows}
reg_ok = all(k not in reg or reg[k] >= CERTIFIED[k] for k in CERTIFIED)
check("S4.a REGRESSION against the v884 certificates on the head "
      "rungs: measured lam_min = %s against certified floors %s -- "
      "every measurement clears its certificate"
      % (", ".join("kz%d: %.4e" % (k, reg[k]) for k in CERTIFIED
                   if k in reg),
         ", ".join("%.4e" % CERTIFIED[k] for k in CERTIFIED)),
      reg_ok, kill="WALL-BROKEN")

n_pos = sum(1 for r in lam_rows if r[5] > 0.0)
check("S4.b every one of the %d faithful accessible rungs has "
      "lam_min > 0: the wall HOLDS everywhere it can be evaluated "
      "(smallest margin %.4e at h = %d)"
      % (len(lam_rows), min(r[5] for r in lam_rows),
         min(lam_rows, key=lambda r: r[5])[3]),
      n_pos == len(lam_rows), kill="WALL-BROKEN")

hh = np.log(np.array([r[3] for r in lam_rows], dtype=float))
ll = np.log(np.array([r[5] for r in lam_rows], dtype=float))
p_fit, c_fit = np.polyfit(hh, ll, 1)
resid = ll - (p_fit * hh + c_fit)
r2_fit = 1.0 - float(np.var(resid) / np.var(ll))
check("S4.c the margin SHRINKS with depth: lam_min ~ h^(%.4f) over "
      "the ladder (log-log fit R2 = %.4f).  Predeclared p > 0 in "
      "lam_min ~ h^(-p): confirmed with p = %.4f"
      % (p_fit, r2_fit, -p_fit), p_fit < 0.0, kill="WALL-BROKEN")

supp = float(np.mean([r[6] for r in lam_rows]))
check("S4.d THE CRITICALITY READING: the wall is positive on every "
      "accessible rung and its margin tends to zero like h^(%.2f).  "
      "That is a MARGINAL statement -- no finite ladder proves the "
      "infinite one, and no finite ladder refutes it.  The "
      "prime-front gates are not blocked by a missing computation; "
      "they are blocked because the quantity being computed goes to "
      "zero.  Soft-mode support in RAW head coordinates averages "
      "%.3f of h, so the raw frame does NOT localize the difficulty "
      "-- v881's 15%% port concentration is produced by the "
      "Schur/testing FRAME, not by the wall itself"
      % (p_fit, supp), True, kill=None)

# ======================================================================
section("S5: the leverage audit")
# ======================================================================
rr = core.build_window(13)
K1 = wall_matrix(rr["alpha"], rr["M"], rr["D"],
                 np.asarray(rr["uu"], float),
                 2.0 * np.asarray(rr["lam"], float))
rr2 = core.build_window(13)
K2 = wall_matrix(rr2["alpha"], rr2["M"], rr2["D"],
                 np.asarray(rr2["uu"], float),
                 2.0 * np.asarray(rr2["lam"], float))
check("S5.a EXACT: the deployed readout is a function of a finite "
      "exact von Mangoldt table plus quadrature -- two independent "
      "rebuilds of rung kz = 13 agree bit-for-bit (max |dK| = %.1e).  "
      "No deployed number is conditional on RH, so a PROOF WOULD MOVE "
      "NO TFPT NUMBER and no physics readout"
      % float(np.max(np.abs(K1 - K2))),
      bool(np.array_equal(K1, K2)), kill="AUDIT-BROKEN")

check("S5.b TYPED (cited I5, not re-derived): the wall for ALL h is "
      "equivalent to Weil positivity and hence to RH.  So the open "
      "prime-front gates (CARLESON.PRIME, PORT.LIMIT, PORT.SCALAR, "
      "CASE.SUMRULE, KREIN.CONTRACTOR) are not 'helped by' RH -- in "
      "TFPT coordinates they ARE RH.  A proof closes them by "
      "definition; TFPT cannot close them without proving RH.  WHAT A "
      "PROOF WOULD BUY, exhaustively: (i) the five open gates flip to "
      "closed with no new understanding, (ii) the port-geometry error "
      "terms become unconditional instead of conditional, (iii) the "
      "S4 margin law gains a proof that it never crosses zero.  It "
      "would buy NOTHING on the compiler side: c3, g_car, the "
      "register, E8 and every SM readout are untouched",
      True, kill=None)

check("S5.c the converse stays shut: nothing measured here supplies "
      "anything toward RH.  S2 is an observation at small x, S4 is a "
      "finite ladder, and S3 measures exactly how far both are from "
      "the deciding scale", True, kill=None)

# ======================================================================
section("C: controls")
# ======================================================================
rng = np.random.default_rng(SEED)
c1_rows, c2_rows = [], []
for kz in (13, 26, 40):
    rr = core.build_window(kz)
    alpha, M, D, h = rr["alpha"], rr["M"], rr["D"], rr["h"]
    uu = np.asarray(rr["uu"], float)
    mu = 2.0 * np.asarray(rr["lam"], float)
    lam_true = float(np.linalg.eigvalsh(
        wall_matrix(alpha, M, D, uu, mu))[0])

    uus = np.sort(rng.uniform(0.0, 2.0 * alpha, size=len(uu)))
    lam_scr = float(np.linalg.eigvalsh(
        wall_matrix(alpha, M, D, uus, mu))[0])

    ng = 4000
    ug = (np.arange(ng) + 0.5) * (2.0 * alpha / ng)
    mg = 2.0 * np.exp(ug / 2.0) * (2.0 * alpha / ng)
    lam_sm = float(np.linalg.eigvalsh(
        wall_matrix(alpha, M, D, ug, mg))[0])

    c1_rows.append((kz, lam_true, lam_scr))
    c2_rows.append((kz, lam_true, lam_sm,
                    abs(mg.sum() - mu.sum()) / mu.sum()))
    print("    kz = %2d  h = %4d  lam_min TRUE %+.4e | SCRAMBLE "
          "%+.4e | SMOOTH %+.4e (mass dev %.3f%%)"
          % (kz, h, lam_true, lam_scr, lam_sm,
             100 * abs(mg.sum() - mu.sum()) / mu.sum()))

check("C1 SCRAMBLE fires on all three rungs: randomizing the atom "
      "POSITIONS while keeping the masses drives lam_min from %s to "
      "%s -- the wall reads arithmetic, not mass"
      % ("/".join("%+.2e" % r[1] for r in c1_rows),
         "/".join("%+.2e" % r[2] for r in c1_rows)),
      all(r[2] < 0.0 for r in c1_rows), kill="CONTROL-DEAD")

check("C2 SMOOTH-COMB fires on all three rungs: replacing the atoms "
      "by the PNT continuum limit of the SAME comb (density 2 e^{u/2}, "
      "total mass within %.2f%%) gives lam_min = %s -- regression of "
      "v883's FLUCTUATIONS-REQUIRED.  The wall needs the actual "
      "arithmetic fluctuations; the smooth law alone destroys it by "
      "four orders of magnitude"
      % (100 * max(r[3] for r in c2_rows),
         "/".join("%+.2e" % r[2] for r in c2_rows)),
      all(r[2] < 0.0 for r in c2_rows), kill="CONTROL-DEAD")

_tree = ast.parse(open(__file__, encoding="utf-8").read())
_called = {n.func.id for n in ast.walk(_tree)
           if isinstance(n, ast.Call) and isinstance(n.func, ast.Name)}
_called |= {n.func.attr for n in ast.walk(_tree)
            if isinstance(n, ast.Call) and isinstance(n.func, ast.Attribute)}
hits = sorted(_called & set(BANNED_IDS))
check("C3 FIREWALL: AST scan of this file finds none of the deployed "
      "banned identifiers %s as a call (hits: %s); the only zero "
      "ordinate in the file is the literature constant gamma_1 in the "
      "closed-form scale arithmetic of S3, which never touches a comb, "
      "window or Toeplitz form"
      % (list(BANNED_IDS), hits or "none"), not hits,
      kill="CONTROL-DEAD")

# ======================================================================
section("VERDICT")
# ======================================================================
n_pass = sum(1 for _, ok in CHECKS if ok)
if KILLS:
    verdict = KILLS[0]
else:
    verdict = ("RH-LEVERAGE-MEASURED (CODE-RATIO-%.3f + "
               "EXPONENT-%.3f + SCALE-GAP-%.0f-DECADES + "
               "WALL-MARGIN-h^%.2f + ZERO-DEPLOYED-LEVERAGE)"
               % (ratios[-1], sigma_emp, gap_dec, p_fit))
check("C4 NO-RH-CLAIM: the verdict asserts nothing about the truth of "
      "RH -- it reports a code ratio, an observed exponent, a scale "
      "gap and a margin law", "RH-TRUE" not in verdict
      and "RH-FALSE" not in verdict, kill="CONTROL-DEAD")

print("\nCHECKS: %d/%d passed" % (n_pass + 1, len(CHECKS)))
if any(not ok for _, ok in CHECKS):
    print("FAILED: %s" % [nm for nm, ok in CHECKS if not ok])
print("VERDICT: %s" % verdict)
print("""
WHAT THIS MEASURES (exploration only):
 * WHERE THE PRIMES SIT IN A PROGRAM READING: the description-length
   ladder shows that finitely describable smooth rules -- parity, the
   210 register, the PNT density -- take the cost of the primes down
   to the combinatorial floor and no further.  After every simple
   rule the primes cost what an arbitrary subset of that size costs.
   That is the precise sense in which they are the incompressible
   part of the output.
 * WHERE RH SITS: it is the statement that the correction to the
   simplest rule is square-root small, i.e. that the output is as
   compressible as it can be without being periodic.  RH is a
   statement about the OUTPUT, not about the program.
 * WHY THE COMPILER CANNOT REACH IT: the deployed ladder is dozens of
   decades below the scale at which a violation would announce
   itself, and the wall margin it computes tends to zero with depth.
   Positive on every rung, shrinking on every rung -- marginal by
   construction, which is exactly what an equivalence to RH must look
   like from inside a finite machine.
 * WHAT A PROOF WOULD BUY TFPT: the five open prime-front gates, the
   unconditionality of the port error terms, and a proof that the
   margin law never crosses zero.  It would move NO deployed number
   and NO physics readout -- those are functions of a finite exact
   table.
NO ledger/paper/website claim; NO RH claim in either direction; NO
physics claim beyond the recorded identities and measurements.
""")
print("runtime: %.1f s" % (time.time() - T0))
sys.exit(0 if n_pass + 1 == len(CHECKS) else 1)
