#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""f8_sector_continuum_probe -- PRIME.POSITIVE_DESCENT.01 follow-up
(strand E, second module): the F8-SECTOR CONTINUUM -- the concrete
finite-level falsifier/promoter named by positive_descent_probe
(DESCENT-PARTIAL): does the f8 character sector become PSD when the
CP functor transports its OWN continuum (the twisted-channel explicit
formula: weight-4 archimedean factor, conductor 8, NO pole) with the
character, instead of the register-trivial GL1 arch+pole?

INPUT STATE (parent probe, 2026-08-05, DESCENT-PARTIAL, 30/30): the
GL1 sector of the packet correspondence operator is bit-identical to
the deployed Weil window and is its UNIQUE PSD sector (margins
+5.29e-5 -> +1.18e-5 over X = 4 -> 10); all 23 other sectors break at
O(1)-O(100) because the register-trivial continuum cannot follow the
damped/twisted atom leg (localization: the negativity is carried by
the POLE layer; arch alone stays near-PSD at -3.6..-4.7).  The parent
verdict named the missing CP-functor data: SECTOR-ADAPTED CONTINUA.
This probe builds the first two and decides them.

THE EXACT CONVENTIONS (frozen; derived so that the ZETA case
reproduces the deployed v563 kernel bit-for-bit -- gated Ward A1):
For a completed L-function Lambda(s) = q^{s/2} gamma_oo(s) L_an(s) in
the ANALYTIC normalization (functional equation s -> 1 - s, critical
line Re s = 1/2, the same normalization as the deployed GL1 window),
the explicit formula pairs an even test g (here: the tent-basis
autocorrelations of the dyadic window, D = 1/64) against
    W(g) = arch(g) [+ pole(g) if L has a pole] - sum_n (c(n)/sqrt(n))
                                                  (g(ln n) + g(-ln n)),
and W(g) = sum_rho h(gamma_rho) >= 0 whenever all zeros are on the
line (h = |phi-hat|^2 for g = phi * phi~).  The archimedean term, in
the tent-lag form the deployed machinery uses, is
    arch(g) = c0 g(0) + int_0^oo [2 e^{-q_e u} g(0)
              - e^{-p_e u} (g(u) + g(-u))] / (1 - e^{-q_e u}) du,
with the closed tail int_W^oo 2 e^{-q_e u}/(1 - e^{-q_e u}) du
= -(2/q_e) ln(1 - e^{-q_e W}).  The three channels decided here:
  ZETA (deployed GL1, validation Ward only):
      gamma_oo = pi^{-s/2} Gamma(s/2):
      c0 = -EULER - ln pi, p_e = 1/2, q_e = 2, PLUS the pole term
      (v716 pole_lags_closed, read-only).  Gate A1: this reproduces
      v563.arch_lags to <= 1e-12 -- the convention lock.
  CHI4 (the odd Dirichlet character mod 4; a genuine mu4-register
      sector of the parent packet -- sp/in = p mod 4):
      Lambda(s, chi) = (pi/4)^{-(s+1)/2} Gamma((s+1)/2) L(s, chi):
      c0 = ln(4/pi) - EULER, p_e = 3/2, q_e = 2, NO pole; atoms
      chi4(n) 2 Lambda(n)/sqrt(n) at ln n, odd n only (conductor 4
      kills the 2-adic channel); chi4(n) = +1/-1 for n = 1/3 mod 4.
  F8 (the weight-4 level-8 newform f8 = eta(2t)^4 eta(4t)^4 -- the C2
      sign channel of the packet, Th0 - Th2 = -8 f8 on odd n):
      Lambda(s) = 8^{s/2} (2 pi)^{-(s+3/2)} Gamma(s+3/2) L_an(s),
      L_an(s) = sum a_n n^{-(s+3/2)} ... i.e. a_n^an = a_n / n^{3/2}:
      gamma'/gamma(1/2 + ir) = (1/2) ln 8 - ln 2pi + psi(2 + ir):
      c0 = ln 8 - 2 ln 2pi - 2 EULER, p_e = 2, q_e = 1, NO pole
      (cuspidal); atoms at u = k ln p with the SATAKE masses
      mu(p^k) = 2 t_k(p) ln p / p^{k/2},
      t_0 = 2, t_1 = a_p / p^{3/2}, t_{k+1} = t_1 t_k - t_{k-1}
      (alpha_p beta_p = 1 for p odd; |t_k| <= 2 by Deligne), and NO
      2-adic atoms (a_2 = 0, conductor 8 -- the ramified channel is
      empty, exactly the parent's register honesty point).

GATES (frozen before the run):
  A1  convention lock: the general arch builder at the ZETA parameters
      reproduces v563.arch_lags(640, 1/64) to max abs <= 1e-12.
  A2  twisted kernels well-formed: d = 0 lags finite; far lags
      negative and decaying; closed tails match a brute cross-check.
  P1  f8 atom layer exact: a_p from the independent eta recurrence
      (int64 + python-int ward), a_p = (-4, -2, 24) at p = 3, 5, 7,
      a_2 = 0; |t_k| <= 2 on every reachable (p, k); t_k ==
      (a_{p^k} - p^3 a_{p^{k-2}})/p^{3k/2} exact-rationally for p = 3,
      k <= 8 (Satake == Hecke bookkeeping).
  D1  THE DECIDER: the f8-sector window (weight-4 arch, no pole, f8
      Satake atoms) is PSD on ALL rungs M = 256..640 (lambda_min >=
      -1e-10 ||T||_2); margins and trend reported.
  D2  the chi4 sector with ITS adapted continuum is PSD on all rungs.
  D3  the GL1 anchor (deployed c_full, read-only) is PSD on all rungs
      (the parent margins reproduced).
  D4  TWO-SECTOR COHERENCE (the structural gate): the SAME battery /
      window machinery with sector-adapted continua is PSD in the GL1
      AND f8 (AND chi4) sectors SIMULTANEOUSLY on every rung -- the
      coherence the CP functor needs.
  B1  honest baseline (typed, always printed): f8-sector PSD at finite
      level is EVIDENCE for the functor architecture (zeros of L(f8)
      lie on the line as far as computed; GRH(f8) is unproven), NOT a
      theorem.  No RH claim, no GRH claim.
CONTROLS (must fire):
  C1  WRONG continuum: the GL1 arch+pole under the f8 Satake atoms
      must break PSD massively (the parent's breakage reproduced from
      the other side); bar: lambda_min(top) < -10.
  C2  scrambled a_p (frozen LCG permutation of the a_p values across
      the odd primes, masses rebuilt): breaks PSD on the CORRECT f8
      continuum; bar: lambda_min(top) < 0.
  C3  Epstein x^2 + 5y^2 comb (epstein_firewall_probe read-only,
      Lambda_E via lattice count + Dirichlet division) on the f8
      continuum: breaks PSD; bar: lambda_min(top) < 0.
NAMED READOUTS (reported, never gated): the sign-flipped f8 comb on
the f8 continuum (the "mirror of f8" -- no L-function behind it); the
typed statement that the register MIRROR sector (+,0,0) admits NO
adapted continuum in the automorphic category (its atom side is
+Lambda(n)/sqrt(n) uniformly = a 1/zeta-type channel with zeros and
poles swapped -- there is no positivity target to adapt to), so the
CP functor's sector set is the AUTOMORPHIC characters, not all 128
register characters.

VERDICT ENUM (frozen):
  F8SECTOR-PSD     = A1/A2/P1 pass, D1-D4 pass, C1-C3 fire: the
      sector-adapted-continua demand of PRIME.POSITIVE_DESCENT.01 is
      finite-level VIABLE; the functor now needs the sector continua
      as functorial data (contract update in the report).
  F8SECTOR-PARTIAL = wards + controls ok, f8 PSD on >= 4 rungs but a
      gate among D1-D4 fails (name it).
  F8SECTOR-DEAD    = the f8 sector stays broken with its OWN continuum
      (D1 fails on > 3 rungs), or a convention ward fails, or a
      control is void: the functor architecture fails its first
      falsifier -- typed plainly.

RESULTS (2026-08-05, 15/15 checks, controls 3/3, 0.7 s; verdict
F8SECTOR-PSD).  Declared repair between run 1 and run 2: the A2 tail
cross-check used a trapezoid rule whose ~1.5e-5 endpoint error at the
1/u singularity failed its own bar; replaced by GL-48 on geometric
cells (dev 3.6e-15).  No gate, kernel, or bar was changed.
  *  A1 convention lock: general builder == v563.arch_lags, max abs
     dev 0.0 (bit-identical).  A2: d = 0 lags finite (f8 +7.590372,
     chi4 +4.133993), far lags negative/decaying, tail closed form ==
     brute (3.6e-15).
  *  P1: a_p = (-4, -2, 24), a_2 = 0 (ramified channel empty); 2518
     Satake atoms, |t_k| <= 2 everywhere (max 1.999631); Satake ==
     Hecke bookkeeping exact (p = 3, k <= 8, Fractions).
  *  D1 THE DECIDER: the f8 sector with its OWN continuum is PSD on
     ALL rungs, lambda_min = +1.52e-4 / +8.64e-5 / +6.14e-5 /
     +4.96e-5 / +4.15e-5 / +3.71e-5 / +3.20e-5 (X = 4..10, log-slope
     -0.241 per X unit).  The parent's f8-twist breakage (-132..-151)
     was ENTIRELY the wrong continuum.
  *  D2 chi4: PSD on all rungs, +9.14e-5 -> +7.18e-6 (slope -0.413).
     D3 GL1 anchor reproduced: +5.29e-5 -> +1.18e-5 (slope -0.239).
     D4 three-sector coherence PASSES: GL1 + chi4 + f8 simultaneously
     PSD on every rung; battery Grams PSD through all three sectors.
     Measured shape: all sectors live in the SAME thin-margin class
     with slow depth decay -- the pole is NOT the sole margin driver.
  *  Controls: C1 wrong continuum -1.408e+2 (parent band reproduced);
     C2 scrambled a_p -1.9e+36; C3 Epstein -1.560e+2.  Named readout:
     sign-flipped f8 comb -6.912 (the mirror-type non-automorphic
     channel indeed carries no positivity).
  *  B1 typed: evidence for the functor architecture, NOT a theorem.

FENCES: NO RH claim, NO GRH(f8) claim.  Stop-list of the closed
diagonal-Gram route binding: windows/battery/pole machinery reused
READ-ONLY, nothing re-gated, no fixed-d variants.  [C neu] semantics;
exploration only; ONE new file; writes nothing.  AST firewall: no
prime tables / zeta symbols (own sieve, own eta recurrence).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/f8_sector_continuum_probe.py
"""

import ast
import hashlib
import math
import os
import sys
import time

import numpy as np
import scipy.linalg as sla

_HERE = os.path.dirname(os.path.abspath(__file__))
_VERIFY = os.path.abspath(os.path.join(_HERE, "..", "..", "verification"))
sys.path.insert(0, _HERE)
sys.path.insert(0, _VERIFY)

import v563_paper2_readouts as core          # noqa: E402  (deployed atoms)
import v716_moonshot_arch_glue as glue       # noqa: E402  (pole lags)
import v755_simpler_schur_recursion as srp   # noqa: E402  (tower channels)
import v766_handoff_bulk as hbp              # noqa: E402  (frozen battery)
import epstein_firewall_probe as epx         # noqa: E402  (control comb)

FROZEN_SPEC = """\
F8-SECTOR-CONTINUUM spec v1 (frozen 2026-08-05, before the first run).
Grid D = 1/64, M_TOP = 640, alpha_top = 5, rungs 256..640 step 64
(X = 4..10); N cap 22050 (reach e^10 = 22026).
Kernels (analytic normalization, tent-lag form, ZETA convention lock):
  zeta: c0 = -EULER - ln pi, p_e = 1/2, q_e = 2, pole = v716 closed;
  chi4: c0 = ln(4/pi) - EULER, p_e = 3/2, q_e = 2, no pole,
        atoms chi4(n) 2 Lambda(n)/sqrt(n), odd n;
  f8  : c0 = ln 8 - 2 ln 2pi - 2 EULER, p_e = 2, q_e = 1, no pole,
        atoms 2 t_k(p) ln p / p^{k/2} at k ln p, odd p only
        (t_1 = a_p p^{-3/2}, t_{k+1} = t_1 t_k - t_{k-1}; a from the
        independent eta recurrence).
Gates A1 (<= 1e-12), A2, P1, D1-D4 (PSD bar -1e-10 ||T||_2), B1 typed;
controls C1 (< -10), C2 (< 0), C3 (< 0); named readouts sign-flip f8,
mirror-sector statement.  Verdict enum F8SECTOR-PSD / -PARTIAL / -DEAD.
LCG seed 20260805.  Runtime cap ~20 min.  NO RH / GRH claim; stop-list
binding; writes nothing.
"""

DGRID = 1.0 / 64.0
M_TOP = 640
ALPHA_TOP = 0.5 * M_TOP * DGRID
RUNGS = (256, 320, 384, 448, 512, 576, 640)
N_CAP = 22050
PSD_BAR = 1.0e-10
EULER = 0.5772156649015328606
EP_NCAP = 34000

BANNED_IDS = ("sympy", "isprime", "primerange", "nextprime", "prevprime",
              "primepi", "zetazero", "nzeros", "mpz_zeta")

CHECKS = []
CONTROL_FIRED = {}
T0 = time.time()
_LCG = [20260805]

_GLX, _GLW = np.polynomial.legendre.leggauss(48)


def lcg(n):
    _LCG[0] = (1103515245 * _LCG[0] + 12345) % (1 << 31)
    return _LCG[0] % n


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok)))
    print("  [%s] %s%s" % ("PASS" if ok else "FAIL", name,
                           ("  -- " + detail) if detail else ""), flush=True)
    return bool(ok)


def section(title):
    print("\n" + "=" * 74)
    print(title)
    print("=" * 74, flush=True)


# ==================================================================== G0
def g0_firewall():
    section("G0 -- SHA-frozen spec + AST firewall + environment")
    sha = hashlib.sha256(FROZEN_SPEC.encode("utf-8")).hexdigest()
    print("    FROZEN_SPEC SHA-256 = %s" % sha)
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
    check("G0.1 no prime-table / zeta symbols in this file", not bad,
          "found %s" % bad if bad else "clean")
    print("    python %s, numpy %s, scipy %s"
          % (sys.version.split()[0], np.__version__,
             __import__("scipy").__version__))


# =============================================== S1 general arch builder
def arch_lag_far(s, D, p_e, q_e):
    """-int tent_s(u) e^{-p u} / (1 - e^{-q u}) du, s >= D (GL-48 per
    half cell) -- the v563 far-cell structure with general exponents."""
    s = np.asarray(s, dtype=float).reshape(-1, 1)
    out = np.zeros(s.shape[0])
    for lo, hi in ((s - D, s), (s, s + D)):
        mid = 0.5 * (lo + hi)
        half = 0.5 * (hi - lo)
        w = mid + half * _GLX[None, :]
        val = ((1.0 - np.abs(s - w) / D) * np.exp(-p_e * w)
               / (-np.expm1(-q_e * w)))
        out -= half[:, 0] * (val @ _GLW)
    return out


def arch_lag_near(s, D, p_e, q_e, c0):
    """d = 0 (and any |s| < D) lag: constants + combined singular cell
    + closed counterterm tail -- the v563 near-cell structure with
    general exponents and constant."""
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
        S = 0.5 * (np.maximum(0.0, 1.0 - np.abs(s - w) / D)
                   + np.maximum(0.0, 1.0 - np.abs(s + w) / D))
        val = ((tri_s * np.exp(-q_e * w) - S * np.exp(-p_e * w))
               / (-np.expm1(-q_e * w)))
        tot += half * float(np.dot(_GLW, val))
    tail = tri_s * (-(2.0 / q_e) * math.log1p(-math.exp(-q_e * W)))
    return c0 * tri_s + 2.0 * tot + tail


def arch_lags_general(M, D, p_e, q_e, c0):
    sv = np.arange(M) * D
    out = np.empty(M)
    far = sv >= D
    out[far] = arch_lag_far(sv[far], D, p_e, q_e)
    for i in np.nonzero(~far)[0]:
        out[i] = arch_lag_near(sv[i], D, p_e, q_e, c0)
    return out


KERNELS = {
    "zeta": dict(p_e=0.5, q_e=2.0, c0=-EULER - math.log(math.pi),
                 pole=True,
                 label="pi^{-s/2} Gamma(s/2)          (GL1, deployed)"),
    "chi4": dict(p_e=1.5, q_e=2.0,
                 c0=math.log(4.0 / math.pi) - EULER, pole=False,
                 label="(pi/4)^{-(s+1)/2} Gamma((s+1)/2)  (odd Dirichlet"
                       " mod 4)"),
    "f8": dict(p_e=2.0, q_e=1.0,
               c0=math.log(8.0) - 2.0 * math.log(2.0 * math.pi)
               - 2.0 * EULER, pole=False,
               label="8^{s/2} (2pi)^{-(s+3/2)} Gamma(s+3/2)  (weight-4"
                     " newform, level 8)"),
}


def s1_kernels():
    section("S1 -- the twisted archimedean kernels (exact conventions) "
            "+ the ZETA convention lock")
    print("    tent-lag form: arch(g) = c0 g(0) + int [2 e^{-q u} g(0) "
          "- e^{-p u}(g(u)+g(-u))]/(1-e^{-q u}) du")
    for name, K in KERNELS.items():
        print("      %-4s: gamma_oo = %s" % (name, K["label"]))
        print("            p_e = %.1f, q_e = %.1f, c0 = %+.12f, pole = %s"
              % (K["p_e"], K["q_e"], K["c0"], K["pole"]))
    t0 = time.time()
    mine = arch_lags_general(M_TOP, DGRID, KERNELS["zeta"]["p_e"],
                             KERNELS["zeta"]["q_e"],
                             KERNELS["zeta"]["c0"])
    depl = core.arch_lags(M_TOP, DGRID)
    dev = float(np.max(np.abs(mine - depl)))
    check("A1 CONVENTION LOCK: general builder at zeta parameters == "
          "v563.arch_lags (max abs dev %.2e <= 1e-12)" % dev,
          dev <= 1.0e-12, "%.1f s" % (time.time() - t0))

    arch_c4 = arch_lags_general(M_TOP, DGRID, KERNELS["chi4"]["p_e"],
                                KERNELS["chi4"]["q_e"],
                                KERNELS["chi4"]["c0"])
    arch_f8 = arch_lags_general(M_TOP, DGRID, KERNELS["f8"]["p_e"],
                                KERNELS["f8"]["q_e"],
                                KERNELS["f8"]["c0"])
    # brute cross-check of the closed counterterm tail (A2): GL-48 on
    # geometric cells [W 2^k, W 2^{k+1}] (the integrand is ~2/(q u)
    # at the left endpoint -- geometric cells resolve it exactly)
    q = KERNELS["f8"]["q_e"]
    W = DGRID
    brute = 0.0
    for k in range(48):
        lo, hi = W * 2.0 ** k, W * 2.0 ** (k + 1)
        mid, half = 0.5 * (lo + hi), 0.5 * (hi - lo)
        u = mid + half * _GLX
        brute += half * float(np.dot(
            _GLW, 2.0 * np.exp(-q * u) / (-np.expm1(-q * u))))
    closed = -(2.0 / q) * math.log1p(-math.exp(-q * W))
    okA2 = (np.isfinite(arch_f8).all() and np.isfinite(arch_c4).all()
            and abs(brute - closed) <= 1.0e-9
            and np.all(arch_f8[1:] < 0) and np.all(arch_c4[1:] < 0)
            and arch_f8[10] > arch_f8[5] and arch_c4[10] > arch_c4[5])
    check("A2 twisted kernels well-formed: d = 0 finite (f8 %+.6f, "
          "chi4 %+.6f); far lags negative and decaying; closed tail == "
          "brute quadrature (dev %.1e)"
          % (arch_f8[0], arch_c4[0], abs(brute - closed)), okA2)
    return dict(arch_zeta=depl, arch_c4=arch_c4, arch_f8=arch_f8)


# =============================================== S2 f8 atom layer
def s2_f8_atoms():
    section("S2 -- the f8 Satake atom layer (independent eta recurrence)")
    t0 = time.time()
    # f8 = q prod (1-q^{2m})^4 (1-q^{4m})^4 via log-derivative recurrence
    tk = np.zeros(N_CAP + 1, dtype=np.int64)
    for d in range(2, N_CAP + 1, 2):
        e_d = 4 + (4 if d % 4 == 0 else 0)
        tk[d::d] += d * e_d
    g = np.zeros(N_CAP, dtype=np.int64)
    g[0] = 1
    for n in range(1, N_CAP):
        s = int(np.dot(tk[1:n + 1], g[n - 1::-1]))
        q, r = divmod(-s, n)
        assert r == 0
        g[n] = q
    a = np.zeros(N_CAP + 1, dtype=np.int64)
    a[1:] = g
    ok_ward = True
    for _ in range(20):
        n = 1 + lcg(N_CAP - 1)
        s = sum(int(tk[k]) * int(g[n - k]) for k in range(1, n + 1)
                if tk[k])
        ok_ward &= (-s == n * int(g[n]))
    check("P1.1 eta recurrence exact (int64 + python-int ward on 20 "
          "sampled steps); a_p = (%d, %d, %d) == (-4, -2, 24); a_2 = %d "
          "== 0 (conductor 8: the ramified channel is EMPTY)"
          % (a[3], a[5], a[7], a[2]),
          ok_ward and (a[3], a[5], a[7]) == (-4, -2, 24) and a[2] == 0,
          "%.1f s" % (time.time() - t0))

    # own smallest-factor sieve for the prime/prime-power structure
    spf = np.zeros(N_CAP + 1, dtype=np.int64)
    for p in range(2, N_CAP + 1):
        if spf[p] == 0:
            spf[p::p] = np.where(spf[p::p] == 0, p, spf[p::p])
    primes = [p for p in range(3, N_CAP + 1, 2) if spf[p] == p]

    # Satake masses on all reachable (p, k)
    pos, mas = [], []
    tmax = 0.0
    npk = 0
    for p in primes:
        if math.log(p) >= 2.0 * ALPHA_TOP:
            break
        t1 = float(a[p]) / p ** 1.5
        tkm1, tkk = 2.0, t1
        k = 1
        u = math.log(p)
        while u < 2.0 * ALPHA_TOP:
            mass = 2.0 * tkk * math.log(p) / p ** (0.5 * k)
            pos.append(u)
            mas.append(mass)
            tmax = max(tmax, abs(tkk))
            npk += 1
            tkm1, tkk = tkk, t1 * tkk - tkm1
            k += 1
            u = k * math.log(p)
    order = np.argsort(np.array(pos))
    pos = np.array(pos)[order]
    mas = np.array(mas)[order]
    check("P1.2 Satake layer: %d atoms (p odd, k >= 1, u < 10); "
          "|t_k| <= 2 everywhere (max %.6f) -- Deligne bound realized"
          % (npk, tmax), tmax <= 2.0 + 1e-12)

    # Satake == Hecke bookkeeping: t_k = (a_{p^k} - p^3 a_{p^{k-2}})
    #                                    / p^{3k/2}, exact rationals p=3
    from fractions import Fraction as Fr
    ok_hecke = True
    tprev, tcur = Fr(2), Fr(int(a[3]))          # scaled: T_k = t_k p^{3k/2}
    # use the integer-scaled recursion T_{k+1} = a_p T_k - p^3 T_{k-1}
    for k in range(1, 9):
        pk = 3 ** k
        ref = Fr(int(a[pk]) - (27 * int(a[pk // 9]) if k >= 2 else 0))
        if tcur != ref:
            ok_hecke = False
        tprev, tcur = tcur, Fr(int(a[3])) * tcur - 27 * tprev
    check("P1.3 Satake == Hecke bookkeeping: p^{3k/2} t_k == a_{p^k} - "
          "p^3 a_{p^{k-2}} EXACT (p = 3, k = 1..8, Fractions)", ok_hecke)
    return dict(a=a, pos=pos, mas=mas, spf=spf)


# =============================================== S3 sector windows
def ladder(lag):
    out = []
    for M in RUNGS:
        T = sla.toeplitz(lag[:M])
        lam = float(sla.eigvalsh(T, subset_by_index=[0, 0])[0])
        nrm = float(sla.norm(T, 2))
        out.append((M, lam, nrm))
    return out


def log_slope(vals):
    if any(v <= 0 for v in vals):
        return None
    Xs = np.array([M * DGRID for M in RUNGS])
    y = np.log(np.array(vals))
    A = np.vstack([np.ones(len(Xs)), Xs]).T
    cf, *_ = np.linalg.lstsq(A, y, rcond=None)
    return float(cf[1])


def s3_sectors(kern, f8):
    section("S3 -- the sector windows with their ADAPTED continua "
            "(the decider)")
    # GL1 anchor: deployed build (read-only)
    ka, masks, dev = srp.channel_masks(ALPHA_TOP)
    check("S3.0 tower comb consistency (deployed masses ward)",
          dev <= 1.0e-12, "rel dev %.1e, ka = %d" % (dev, ka))
    c_gl1 = srp.continuum_lags(M_TOP)
    for cnl in ("ro", "re", "sp", "in"):
        c_gl1 = c_gl1 + srp.atom_channel_lags(ALPHA_TOP, M_TOP,
                                              masks[cnl])
    # chi4 sector: odd deployed atoms, signed by n mod 4, own continuum
    nvals = np.array([int(round(math.exp(float(core.U_ALL[i]))))
                      for i in range(ka)], dtype=np.int64)
    odd = nvals % 2 == 1
    sgn = np.where(nvals % 4 == 1, 1.0, -1.0)
    pos4 = core.U_ALL[:ka][odd]
    mas4 = (core.MU_ALL[:ka] * sgn)[odd]
    cat4, _d = core.atom_lags_at(ALPHA_TOP, M_TOP, pos4, mas4)
    c_c4 = kern["arch_c4"] + cat4
    # f8 sector: Satake atoms, own continuum
    catf, _d = core.atom_lags_at(ALPHA_TOP, M_TOP, f8["pos"], f8["mas"])
    c_f8 = kern["arch_f8"] + catf

    lads = {"GL1 (deployed anchor)": ladder(c_gl1),
            "chi4 (adapted continuum)": ladder(c_c4),
            "f8 (adapted continuum)": ladder(c_f8)}
    print("    PSD table (lambda_min per rung, X = M/64):")
    print("      sector                    | " +
          " | ".join("X=%-2d" % int(M * DGRID) for M in RUNGS))
    psd = {}
    for name, lad in lads.items():
        psd[name] = all(lam >= -PSD_BAR * nrm for _M, lam, nrm in lad)
        print("      %-25s | %s  [%s]"
              % (name, " | ".join("%+.2e" % lam for _M, lam, _n in lad),
                 "PSD" if psd[name] else "NEG"))
        sl = log_slope([lam for _M, lam, _n in lad])
        print("        margin trend: factor %.2f over X = 4 -> 10, "
              "log-slope %s per X unit"
              % (lad[0][1] / lad[-1][1] if lad[-1][1] > 0 else
                 float("nan"),
                 "%.3f" % sl if sl is not None else "n/a"))
    ok1 = check("D1 THE DECIDER: the f8 sector with its OWN continuum "
                "(weight-4 arch, no pole, Satake atoms) is PSD on ALL "
                "%d rungs -- the parent's f8-twist breakage "
                "(-132..-151) was the WRONG continuum"
                % len(RUNGS), psd["f8 (adapted continuum)"])
    ok2 = check("D2 the chi4 sector with its adapted continuum is PSD "
                "on all rungs", psd["chi4 (adapted continuum)"])
    ok3 = check("D3 the GL1 anchor (deployed) is PSD on all rungs "
                "(parent margins reproduced)",
                psd["GL1 (deployed anchor)"])
    ok4 = check("D4 MULTI-SECTOR COHERENCE: GL1 + chi4 + f8 "
                "simultaneously PSD on every rung with the same "
                "battery/window machinery -- the coherence the CP "
                "functor needs", ok1 and ok2 and ok3)

    # battery Grams through the sectors (v766 battery R = 1, read-only)
    bat = hbp.battery(1.0)
    Fm = np.stack([v for _n, v in bat], axis=1)
    nR = Fm.shape[0]
    gmin = {}
    for name, lag in (("GL1", c_gl1), ("chi4", c_c4), ("f8", c_f8)):
        F = np.zeros((M_TOP, Fm.shape[1]))
        F[:nR] = Fm
        T = sla.toeplitz(lag[:M_TOP])
        Gm = F.T @ T @ F
        gmin[name] = float(np.linalg.eigvalsh(0.5 * (Gm + Gm.T))[0])
    check("S3.5 frozen-battery Grams PSD through all three sectors at "
          "the top rung (min eig GL1/chi4/f8 = %.1e / %.1e / %.1e)"
          % (gmin["GL1"], gmin["chi4"], gmin["f8"]),
          all(v >= -1.0e-12 for v in gmin.values()))
    print("    B1 HONEST BASELINE (typed): the f8/chi4 sector PSD at "
          "finite level is EVIDENCE for the functor architecture --\n"
          "       it reflects the zeros of L(f8)/L(chi4) lying on the "
          "critical line as far as they influence these windows.\n"
          "       GRH(f8) is UNPROVEN: this is a consistency "
          "measurement, NOT a theorem, and no GRH/RH claim is made.")
    return dict(c_gl1=c_gl1, c_c4=c_c4, c_f8=c_f8, lads=lads, psd=psd)


# =============================================== S4 controls + readouts
def s4_controls(kern, f8, ss3):
    section("S4 -- must-fail controls + named readouts")
    # C1 wrong continuum: GL1 arch + pole under the f8 Satake atoms
    catf, _d = core.atom_lags_at(ALPHA_TOP, M_TOP, f8["pos"], f8["mas"])
    c_wrong = srp.continuum_lags(M_TOP) + catf
    lam = float(sla.eigvalsh(sla.toeplitz(c_wrong[:M_TOP]),
                             subset_by_index=[0, 0])[0])
    CONTROL_FIRED["C1"] = lam < -10.0
    check("C1 WRONG continuum (GL1 arch+pole under f8 atoms): "
          "lambda_min(top) = %+.3e < -10 (the parent's sector breakage "
          "reproduced from the other side)" % lam, CONTROL_FIRED["C1"])

    # C2 scrambled a_p on the CORRECT f8 continuum
    spf = f8["spf"]
    primes = [p for p in range(3, N_CAP + 1, 2) if spf[p] == p]
    avals = [int(f8["a"][p]) for p in primes]
    perm = list(range(len(avals)))
    for i in range(len(perm) - 1, 0, -1):
        j = lcg(i + 1)
        perm[i], perm[j] = perm[j], perm[i]
    pos_s, mas_s = [], []
    for pi, p in enumerate(primes):
        if math.log(p) >= 2.0 * ALPHA_TOP:
            break
        t1 = float(avals[perm[pi]]) / p ** 1.5
        tkm1, tkk = 2.0, t1
        k = 1
        u = math.log(p)
        while u < 2.0 * ALPHA_TOP:
            pos_s.append(u)
            mas_s.append(2.0 * tkk * math.log(p) / p ** (0.5 * k))
            tkm1, tkk = tkk, t1 * tkk - tkm1
            k += 1
            u = k * math.log(p)
    cat_s, _d = core.atom_lags_at(ALPHA_TOP, M_TOP,
                                  np.array(pos_s), np.array(mas_s))
    lam_s = float(sla.eigvalsh(sla.toeplitz(
        (kern["arch_f8"] + cat_s)[:M_TOP]),
        subset_by_index=[0, 0])[0])
    CONTROL_FIRED["C2"] = lam_s < 0.0
    check("C2 scrambled a_p (LCG permutation across the odd primes, "
          "correct f8 continuum): lambda_min(top) = %+.3e < 0"
          % lam_s, CONTROL_FIRED["C2"])

    # C3 Epstein x^2 + 5y^2 comb on the f8 continuum
    r1 = epx.lattice_r1(EP_NCAP)
    b = np.asarray(r1, float) / 2.0
    lamE = epx.dirichlet_vonmangoldt(b, EP_NCAP)
    supp = np.nonzero(np.abs(lamE) > 1.0e-9)[0]
    supp = supp[(supp >= 2)]
    posE = np.log(supp.astype(float))
    keep = posE < 2.0 * ALPHA_TOP
    posE = posE[keep]
    masE = 2.0 * lamE[supp[keep]] / np.sqrt(supp[keep].astype(float))
    catE, _d = core.atom_lags_at(ALPHA_TOP, M_TOP, posE, masE)
    lam_e = float(sla.eigvalsh(sla.toeplitz(
        (kern["arch_f8"] + catE)[:M_TOP]),
        subset_by_index=[0, 0])[0])
    CONTROL_FIRED["C3"] = lam_e < 0.0
    check("C3 Epstein x^2+5y^2 comb (%d negative Lambda_E sites) on "
          "the f8 continuum: lambda_min(top) = %+.3e < 0"
          % (int(np.sum(lamE[2:] < -1.0e-9)), lam_e),
          CONTROL_FIRED["C3"])

    # named readouts (never gated)
    catm, _d = core.atom_lags_at(ALPHA_TOP, M_TOP, f8["pos"],
                                 -f8["mas"])
    lam_m = float(sla.eigvalsh(sla.toeplitz(
        (kern["arch_f8"] + catm)[:M_TOP]),
        subset_by_index=[0, 0])[0])
    print("    NAMED READOUT (not gated): sign-flipped f8 comb on the "
          "f8 continuum: lambda_min(top) = %+.3e" % lam_m)
    print("    NAMED STATEMENT (typed): the register MIRROR sector "
          "(+,0,0) admits NO adapted continuum in the automorphic\n"
          "      category -- its atom side (+Lambda(n)/sqrt(n) "
          "uniformly) is a 1/zeta-type channel (zeros <-> poles "
          "swapped),\n      so there is no positivity target to adapt "
          "to.  CONSEQUENCE for the functor: the CP sector set is the "
          "set of\n      AUTOMORPHIC characters of the register (GL1, "
          "chi4-type Dirichlet sectors, the f8 channel), not all 128 "
          "register\n      characters.  The parent's 23 broken sectors "
          "split into: repairable-by-adapted-continuum (automorphic) "
          "and\n      structurally-non-automorphic (mirror-type)."
          )
    return lam, lam_s, lam_e, lam_m


# ================================================================ verdict
def verdict(ss3):
    section("VERDICT")
    n_pass = sum(1 for _n, ok in CHECKS if ok)
    n_all = len(CHECKS)
    print("%d/%d checks passed" % (n_pass, n_all))
    controls_ok = all(CONTROL_FIRED.get(c, False)
                      for c in ("C1", "C2", "C3"))
    wards_ok = all(ok for n, ok in CHECKS
                   if n.startswith(("A1", "A2", "P1", "S3.0")))
    f8_lad = ss3["lads"]["f8 (adapted continuum)"]
    f8_psd_rungs = sum(1 for _M, lam, nrm in f8_lad
                       if lam >= -PSD_BAR * nrm)
    d_ok = ss3["psd"]["f8 (adapted continuum)"] \
        and ss3["psd"]["chi4 (adapted continuum)"] \
        and ss3["psd"]["GL1 (deployed anchor)"]
    if not wards_ok or not controls_ok or f8_psd_rungs <= 3:
        v = "F8SECTOR-DEAD (%s)" % (
            "convention ward failed" if not wards_ok else
            "control void: %s" % [c for c in ("C1", "C2", "C3")
                                  if not CONTROL_FIRED.get(c, False)]
            if not controls_ok else
            "the f8 sector stays broken with its OWN continuum "
            "(%d/7 rungs PSD): the functor architecture fails its "
            "first falsifier" % f8_psd_rungs)
    elif d_ok and n_pass == n_all:
        v = "F8SECTOR-PSD"
    else:
        fails = [n for n, ok in CHECKS if not ok]
        v = "F8SECTOR-PARTIAL (%s)" % ("; ".join(fails[:3])
                                       if fails else "gate detail")
    print("VERDICT: %s" % v)
    if v == "F8SECTOR-PSD":
        print("""
F8-SECTOR CONTINUUM -- F8SECTOR-PSD.  The first falsifier of the
sector-adapted-continua demand PASSES:
  * The f8 sector, broken at -132..-151 under the register-trivial
    GL1 continuum (parent probe), is PSD on the ENTIRE frozen ladder
    once the CP functor transports its OWN continuum (weight-4 arch
    kernel, conductor 8, no pole, Satake atom masses) -- with margins
    in the same thin-margin class as the GL1 anchor (~3x fatter).
  * The chi4 (odd Dirichlet mod 4) sector -- a genuine mu4-register
    sector -- is likewise PSD with its adapted continuum.
  * MULTI-SECTOR COHERENCE holds: GL1 + chi4 + f8 are simultaneously
    PSD on every rung with the SAME battery/window machinery -- the
    finite-level shape of the CP functor's naturality square.
  * Controls: the wrong continuum reproduces the parent breakage; a_p
    scramble and Epstein break the correct continuum.  The mirror
    sector is typed as structurally non-automorphic (no adapted
    continuum exists) -- the functor's sector set is the automorphic
    characters, not all 128.
  * B1: evidence for the functor architecture, NOT a theorem
    (GRH(f8)/GRH(chi4)/RH all unproven).  NO claim beyond the frozen
    windows.""")
    print("total runtime %.1f s" % (time.time() - T0))
    return v


def contract_update(ss3):
    section("RECOMMENDED CONTRACT UPDATE -- PRIME.POSITIVE_DESCENT.01 "
            "(report only; nothing written)")
    print("""\
    UPDATE to the three-object demand of PRIME.POSITIVE_DESCENT.01
    (parent report), after the first falsifier PASSED:
      (1) SECTOR-ADAPTED CONTINUA -- status upgrade [finite-level
          VIABLE]: the f8 and chi4 sectors are PSD on the full frozen
          ladder with their own explicit-formula continua (f8:
          +1.52e-4 -> +3.20e-5; chi4: +9.14e-5 -> +7.18e-6; GL1
          anchor: +5.29e-5 -> +1.18e-5).  The demand sharpens to:
          (1a) the functor's sector set is the AUTOMORPHIC register
          characters (GL1, the Dirichlet mu4 sectors, the f8/C2
          channel); the mirror-type sectors are structurally
          non-automorphic (sign-flipped f8 comb: lambda_min = -6.9)
          and carry no positivity demand; (1b) the continuum
          assignment chi -> (c0, p_e, q_e, pole flag, conductor) must
          be shown FUNCTORIAL (compatible with the register
          composition measured in the parent: sigma3/f8 channel
          arithmetic, conductor = ramified-register content:
          1 / 4 / 8 here).
      (2) SECTOR-PSD PERSISTENCE now reads: for EVERY automorphic
          sector, the sector window with its adapted continuum stays
          PSD as X -> infinity (GL1 = Weil positivity; f8/chi4 = the
          GRH-type statements for the twisted channels).  The
          measured finite-level shape: ALL THREE sectors sit in the
          same thin-margin PSD class with slow depth decay (log-slope
          per X unit: GL1 -0.239, f8 -0.241, chi4 -0.413) -- the
          moving-edge phenomenon of the closed route persists in mild
          form in every sector, pole or no pole, so the pole is NOT
          the sole thin-margin driver; the persistence demand is a
          genuinely infinite-level statement in each sector.
      (3) THE CARRIER INTERTWINER is unchanged (the population ->
          unit-modulus sign step), but gains a target: the intertwined
          carrier evaluation must land, sector by sector, on EXACTLY
          these adapted explicit formulas (the Satake mass recursion
          t_{k+1} = t_1 t_k - t_{k-1} IS the analytic image of the
          parent's p^3-corrected packet recursion -- the bookkeeping
          identity p^{3k/2} t_k = a_{p^k} - p^3 a_{p^{k-2}} was
          verified exactly here).
    STOP CONDITIONS unchanged: no RH/GRH claim, stop-list of the
    closed Gram route binding, closed-route objects reused read-only.
    NEXT FALSIFIER (named): the conductor-functoriality gate (1b) --
    exhibit the continuum assignment as a monoid map from the
    ramified-register content to (conductor, gamma shift), and test a
    SECOND cuspidal sector (e.g. the weight-4 level-16 channel of the
    mu4 register) with the same machinery.""")


def main():
    print("=" * 74)
    print("F8-SECTOR CONTINUUM -- the first falsifier of the "
          "sector-adapted-continua")
    print("demand of PRIME.POSITIVE_DESCENT.01 (parent: DESCENT-PARTIAL)")
    print("=" * 74)
    g0_firewall()
    kern = s1_kernels()
    f8 = s2_f8_atoms()
    ss3 = s3_sectors(kern, f8)
    s4_controls(kern, f8, ss3)
    v = verdict(ss3)
    contract_update(ss3)
    n_pass = sum(1 for _n, ok in CHECKS if ok)
    return 0 if (n_pass == len(CHECKS)
                 and not v.startswith("F8SECTOR-DEAD")) else 1


if __name__ == "__main__":
    sys.exit(main())
