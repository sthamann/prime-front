#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""conductor_functoriality_probe -- PRIME.POSITIVE_DESCENT.01,
third module (strand E): the CONDUCTOR-FUNCTORIALITY GATE -- the next
falsifier named by f8_sector_continuum_probe (F8SECTOR-PSD): show the
continuum assignment chi -> (c0, p_e, q_e, pole flag, conductor) is
ONE closed structure map (not a case table), and decide a SECOND
independent cuspidal sector -- the register-internal twist
f8 (x) chi_{-4} -- with the RULE-DERIVED continuum.

INPUT STATE (sibling probe, 2026-08-05, F8SECTOR-PSD, 15/15): the f8
and chi4 sectors are PSD on the full frozen ladder with their own
explicit-formula continua (f8: +1.52e-4 -> +3.20e-5; chi4: +9.14e-5
-> +7.18e-6; GL1 anchor +5.29e-5 -> +1.18e-5); the wrong (GL1)
continuum reproduces the parent breakage at -140.8; the mirror-type
register sectors are typed structurally non-automorphic.  The sibling
verdict named gate (1b): exhibit chi -> continuum as a functorial
assignment and test a second cuspidal sector from the same rule.

THE CLOSED RULE (frozen -- the standard completed-L recipe, stated as
ONE map and verified on all four sectors as instances):
    An automorphic sector chi of the register carries
        Lambda_chi(s) = q^{s/2} PROD_j Gamma_R(s + mu_j) L_an(chi, s),
        Gamma_R(z) = pi^{-z/2} Gamma(z/2),
    in the ANALYTIC normalization (functional equation s -> 1 - s),
    with (mu-list, q, pole) determined by (degree, parity/weight,
    ramified-register content):
        GL1 character, parity a:  mu = {a},                q = cond(chi),
                                  pole iff chi trivial;
        GL2 hol. newform, wt k :  mu = {(k-1)/2, (k+1)/2}, q = cond,
                                  no pole (cuspidal).
    The tent-lag continuum follows by ONE kernel lemma per Gamma_R
    factor (no per-sector choice):
        arch_chi(g) = ln(q) g(0) + SUM_j K_{mu_j}(g),
        K_mu(g) = -(ln pi + EULER) g(0)
                  + int_0^oo [2 e^{-2u} g(0)
                    - e^{-(mu + 1/2) u} (g(u) + g(-u))] / (1 - e^{-2u}) du,
    i.e. per factor p_e = mu + 1/2, q_e = 2, c0 = -(ln pi + EULER),
    plus the single conductor constant ln q at lag 0.  INSTANCES:
      zeta       : mu = {0}          , q = 1  (pole)   -> the deployed
                   GL1 kernel (gate R1a: == v563.arch_lags bit-level);
      chi_{-4}   : mu = {1}          , q = 4  (no pole) -> the sibling
                   chi4 kernel (gate R1b, <= 1e-12);
      f8         : mu = {3/2, 5/2}   , q = 8  (no pole) -> the sibling
                   weight-4 Gamma_C kernel via the DUPLICATION identity
                   Gamma_R(z) Gamma_R(z+1) = Gamma_C(z) (gate R1c,
                   <= 1e-9: two independent quadrature structures --
                   the strongest one-rule Ward);
      f8 (x) chi4: mu = {3/2, 5/2}   , q = 16 (no pole) -- NOTHING
                   hand-tuned: same mu-list as f8 (weight unchanged by
                   twisting), conductor from the twist bound + the
                   Fricke ward below.
THE TWIST (the second cuspidal sector, register-internal):
    g = f8 (x) chi_{-4}: a_g(n) = chi_{-4}(n) a_f8(n) (zero on even n;
    a_2(f8) = 0 already), weight 4, trivial nebentypus (chi^2 = 1),
    real coefficients.  CONDUCTOR: Atkin-Li (1978), "Twists of
    newforms and pseudo-eigenvalues of W-operators", Thm 3.1: for a
    newform of level N and a primitive twist chi mod m, cond(f x chi)
    divides lcm(N, m^2, m cond(chi_f)) = lcm(8, 16, 4) = 16 here; the
    EXACT conductor is decided numerically by the Fricke ward (T2):
    on the imaginary axis the weight-4 eigenform property reads
        f(1/(N t)) = eps N^2 t^4 f(t),   f(t) = SUM a(n) e^{-2 pi n t},
    which must hold to <= 1e-8 over the frozen t-grid for the TRUE N
    (and must FAIL for wrong N -- sub-control).  Anchor: f8 itself at
    N = 8 (its own Fricke eigenvalue reported).
GATES (frozen before the run):
  R1a/b/c  the rule instances (above).
  T1   twist layer exact: a_g multiplicative on 25 sampled coprime
       pairs (integer arithmetic); a_g(even) = 0; |t_k| <= 2 on every
       reachable (p, k) (Deligne survives twisting, |chi| = 1).
  T2   conductor: Fricke ward passes for exactly one N in {8, 16, 32}
       and it is N = 16, |eps| = 1; f8 anchor passes at N = 8.
  D1   THE DECIDER: the twist sector with the RULE-derived continuum
       (mu = {3/2, 5/2}, q = 16) is PSD on all rungs X = 4..10
       (bar -1e-10 ||T||_2).
  D2   FOUR-SECTOR COHERENCE: GL1 + chi4 + f8 + twist simultaneously
       PSD on every rung, same battery/window machinery (battery
       Grams PSD through all four).
  P0   conductor pinning (readout, gated as consistency): lambda_min
       is EXACTLY linear in ln q (identity shift), so PSD pins
       ln q >= ln 16 - lambda_min(top); with the Atkin-Li bound
       q | 16 from above, q = 16 is the unique admissible conductor;
       relative pinning width = lambda_min(top) ~ 1e-5.
CONTROLS (must fire):
  C1   THE DISCRIMINATING CONTROL: the twist sector under the
       UNTWISTED f8 continuum (q = 8, everything else identical) must
       break: the diagonal drops by exactly ln 2, so lambda_min ~
       margin - 0.693 < -0.5.  The conductor datum is load-bearing.
  C2   scrambled twisted a_p (frozen LCG permutation) explodes on the
       correct continuum (bar < 0).
  C3   wrong-N Fricke (N = 8 on the twist) fails by > 1e-2
       (sub-control inside T2).
NAMED (never gated): the register mirror (+,0,0) stays typed
non-automorphic (re-asserted; no positivity demand); sign-flipped
twist comb readout.
VERDICT ENUM (frozen):
  CONDUCTOR-FUNCTORIAL = R1 + T1/T2 + D1 + D2 + P0 pass, C1-C3 fire:
      the assignment is ONE map; demand (1) of
      PRIME.POSITIVE_DESCENT.01 upgrades to a functorial statement;
      what remains is the infinite-level CP extension (named in the
      contract update).
  CONDUCTOR-PARTIAL    = rule + twist PSD but a named gate fails.
  CONDUCTOR-AD-HOC     = the twist needs hand-tuning (D1 fails with
      the rule continuum): the assignment is a case table -- typed.

RESULTS (2026-08-05, first run after freeze, 16/16 checks, controls
3/3, 0.9 s; verdict CONDUCTOR-FUNCTORIAL; no repairs):
  *  R1a zeta == deployed and R1b chi4 == sibling: max dev 0.0
     (bit-level); R1c DUPLICATION WARD: the two-Gamma_R build equals
     the sibling Gamma_C weight-4 kernel to 2.66e-15 -- the rule is
     one map, verified across two independent quadrature structures.
  *  T1: twist coefficients exact and multiplicative; 2518 Satake
     atoms, |t_k| <= 2 (max 1.999631).
  *  T2 FRICKE: f8 anchor eps = +1 (4.4e-16); the twist passes at
     N = 16 ONLY (6.7e-16, eps = +1); N = 8 fails at 5.2e-1, N = 32
     at 6.8e-1: conductor(f8 x chi4) = 16, decided numerically at
     machine precision inside the Atkin-Li bound.
  *  D1: twist sector PSD on ALL rungs with the rule continuum,
     lambda_min = +1.97e-4 -> +2.75e-5 (X = 4..10).
  *  D2: FOUR-SECTOR COHERENCE holds (GL1 +5.29e-5 -> +1.18e-5, chi4
     +9.14e-5 -> +7.18e-6, f8 +1.52e-4 -> +3.20e-5, twist as above);
     battery Grams PSD through all four sectors.
  *  P0: lambda_min exactly linear in ln q (shift ward -6.931e-1 ==
     margin - ln 2); PSD pins q >= 15.999561, Atkin-Li pins q | 16:
     unique conductor 16, relative pinning width 2.7e-5.
  *  Controls: C1 untwisted (q = 8) continuum on the twist:
     lambda_min = -0.693120 = margin - ln 2 EXACTLY (deterministic
     identity shift -- the conductor datum is load-bearing at 4
     orders of magnitude above the margins); C2 scrambled a_p:
     -2.3e+39; C3 wrong-N Fricke fails at 5.2e-1.  Named: sign-
     flipped twist comb -6.73 (non-automorphic, breaks as typed).

FENCES: NO RH / GRH claim (B1 of the sibling probe carries over: PSD
here is finite-level EVIDENCE, zeros of L(g) on the line as far as
they influence the windows, nothing proven).  Stop-list of the closed
Gram route binding; deployed machinery reused READ-ONLY; exploration
only; ONE new file; writes nothing.  AST firewall: no prime tables /
zeta symbols (own sieve, own eta recurrence, sibling helpers
imported).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/conductor_functoriality_probe.py
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

import v563_paper2_readouts as core            # noqa: E402
import v755_simpler_schur_recursion as srp     # noqa: E402
import v766_handoff_bulk as hbp                # noqa: E402
import f8_sector_continuum_probe as fsc        # noqa: E402  (sibling,
#                                          import-safe: main() guarded)

FROZEN_SPEC = """\
CONDUCTOR-FUNCTORIALITY spec v1 (frozen 2026-08-05, before the first
run).  Grid D = 1/64, M_TOP = 640, rungs 256..640 step 64; N cap
22050.  THE RULE: Lambda_chi = q^{s/2} prod_j Gamma_R(s + mu_j) L_an;
kernel = ln(q) at lag 0 + sum_j GammaR-factor kernels
(p_e = mu_j + 1/2, q_e = 2, c0 = -(ln pi + EULER)); pole iff trivial.
Instances: zeta {0},1; chi4 {1},4; f8 {3/2,5/2},8; twist {3/2,5/2},16.
Gates R1a (bit/1e-12 vs deployed), R1b (1e-12), R1c duplication
(1e-9), T1 (25 coprime pairs, Deligne), T2 Fricke (1e-8 pass at one N
= 16, anchor f8@8; wrong-N > 1e-2), D1/D2 (PSD bar -1e-10 ||T||_2),
P0 pinning.  Controls C1 (< -0.5), C2 (< 0), C3 (> 1e-2).  Fricke
t-grid {0.19, 0.22, 0.28, 0.33, 0.40} (kept away from the W_N fixed
points 1/sqrt(N) = 0.177 / 0.25 / 0.354 where R is trivial or 0/0;
NaN ratios count as ward failure), series cap n <= 3000.  LCG
seed 20260805.  Verdict enum CONDUCTOR-FUNCTORIAL / -PARTIAL /
-AD-HOC.  NO RH/GRH claim; stop-list binding; writes nothing.
"""

DGRID = 1.0 / 64.0
M_TOP = 640
ALPHA_TOP = 0.5 * M_TOP * DGRID
RUNGS = (256, 320, 384, 448, 512, 576, 640)
N_CAP = 22050
PSD_BAR = 1.0e-10
EULER = 0.5772156649015328606
LOG_PI = math.log(math.pi)
FRICKE_T = (0.19, 0.22, 0.28, 0.33, 0.40)
FRICKE_NCAP = 3000

BANNED_IDS = ("sympy", "isprime", "primerange", "nextprime", "prevprime",
              "primepi", "zetazero", "nzeros", "mpz_zeta")

CHECKS = []
CONTROL_FIRED = {}
T0 = time.time()
_LCG = [20260805]


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
    bad = []
    for node in ast.walk(ast.parse(src)):
        name = None
        if isinstance(node, ast.Name):
            name = node.id
        elif isinstance(node, ast.Attribute):
            name = node.attr
        elif isinstance(node, (ast.Import, ast.ImportFrom)):
            mods = [al.name for al in node.names]
            if isinstance(node, ast.ImportFrom) and node.module:
                mods.append(node.module)
            bad += [m for m in mods if any(b in m for b in BANNED_IDS)]
            continue
        if name and name.lower() in BANNED_IDS:
            bad.append(name)
    check("G0.1 no prime-table / zeta symbols in this file", not bad,
          "found %s" % bad if bad else "clean")
    print("    python %s, numpy %s, scipy %s"
          % (sys.version.split()[0], np.__version__,
             __import__("scipy").__version__))


# ==================================================== S1 THE CLOSED RULE
def rule_arch_lags(mus, q):
    """THE structure map: mu-list + conductor -> tent-lag continuum.
    One universal Gamma_R-factor kernel per mu, one ln(q) at lag 0.
    Nothing else is free."""
    out = np.zeros(M_TOP)
    for mu in mus:
        out += fsc.arch_lags_general(M_TOP, DGRID, mu + 0.5, 2.0,
                                     -(LOG_PI + EULER))
    out[0] += math.log(q)
    return out


SECTOR_DATA = {
    #  name          mu-list         q   pole
    "zeta":  (( 0.0,),        1,  True),
    "chi4":  (( 1.0,),        4,  False),
    "f8":    ((1.5, 2.5),     8,  False),
    "twist": ((1.5, 2.5),    16,  False),
}


def s1_rule():
    section("S1 -- THE CLOSED RULE (one structure map) + instance gates")
    print("    RULE: Lambda_chi(s) = q^{s/2} prod_j Gamma_R(s + mu_j) "
          "L_an(chi, s);   kernel = ln(q) e_0 + sum_j K_{mu_j},")
    print("          K_mu: p_e = mu + 1/2, q_e = 2, c0 = -(ln pi + "
          "EULER);   pole iff chi trivial.  Instances:")
    for nm, (mus, q, pole) in SECTOR_DATA.items():
        print("      %-5s: mu = %-12s q = %-3d pole = %s"
              % (nm, str(list(mus)), q, pole))
    lag = {nm: rule_arch_lags(mus, q)
           for nm, (mus, q, _p) in SECTOR_DATA.items()}

    dev_a = float(np.max(np.abs(lag["zeta"] - core.arch_lags(M_TOP,
                                                             DGRID))))
    check("R1a rule instance zeta {mu=0, q=1} == DEPLOYED "
          "v563.arch_lags (max abs dev %.2e <= 1e-12)" % dev_a,
          dev_a <= 1.0e-12)
    sib_c4 = fsc.arch_lags_general(M_TOP, DGRID, 1.5, 2.0,
                                   math.log(4.0 / math.pi) - EULER)
    dev_b = float(np.max(np.abs(lag["chi4"] - sib_c4)))
    check("R1b rule instance chi4 {mu=1, q=4} == sibling chi4 kernel "
          "(max abs dev %.2e <= 1e-12)" % dev_b, dev_b <= 1.0e-12)
    sib_f8 = fsc.arch_lags_general(
        M_TOP, DGRID, 2.0, 1.0,
        math.log(8.0) - 2.0 * math.log(2.0 * math.pi) - 2.0 * EULER)
    dev_c = float(np.max(np.abs(lag["f8"] - sib_f8)))
    check("R1c DUPLICATION WARD: rule instance f8 {mu=3/2,5/2, q=8} "
          "(two Gamma_R kernels) == sibling Gamma_C kernel "
          "(independent quadrature structure; max abs dev %.2e <= "
          "1e-9) -- Gamma_R(z) Gamma_R(z+1) = Gamma_C(z)" % dev_c,
          dev_c <= 1.0e-9)
    print("    (the -2 ln 2 constant offset between the two forms is "
          "absorbed by the counterterm integral, as the duplication\n"
          "     identity demands -- verified numerically above, not "
          "assumed)")
    return lag


# ==================================================== S2 the twist layer
def eta_f8(ncap):
    """a_n of f8 = eta(2t)^4 eta(4t)^4 by the log-derivative
    recurrence (int64, exact; sibling-validated construction)."""
    tk = np.zeros(ncap + 1, dtype=np.int64)
    for d in range(2, ncap + 1, 2):
        tk[d::d] += d * (4 + (4 if d % 4 == 0 else 0))
    g = np.zeros(ncap, dtype=np.int64)
    g[0] = 1
    for n in range(1, ncap):
        s = int(np.dot(tk[1:n + 1], g[n - 1::-1]))
        q, r = divmod(-s, n)
        assert r == 0
        g[n] = q
    a = np.zeros(ncap + 1, dtype=np.int64)
    a[1:] = g
    return a


def chi4(n):
    if n % 2 == 0:
        return 0
    return 1 if n % 4 == 1 else -1


def s2_twist():
    section("S2 -- the twist g = f8 (x) chi_{-4}: coefficients, "
            "Deligne, conductor (Fricke ward)")
    t0 = time.time()
    a = eta_f8(N_CAP)
    ag = np.array([chi4(n) * int(a[n]) for n in range(N_CAP + 1)],
                  dtype=np.int64)
    ok_anchor = ((int(a[3]), int(a[5]), int(a[7])) == (-4, -2, 24)
                 and (int(ag[3]), int(ag[5]), int(ag[7]))
                 == (4, -2, -24) and int(ag[2]) == 0)
    ok_mult = True
    for _ in range(25):
        m = 3 + 2 * lcg(60)
        n = 3 + 2 * lcg(60)
        if math.gcd(m, n) != 1 or m * n > N_CAP:
            continue
        ok_mult &= int(ag[m * n]) == int(ag[m]) * int(ag[n])
    check("T1.1 twist coefficients exact: a_g(3,5,7) = (+4,-2,-24) = "
          "chi4 * (-4,-2,24); a_g(even) = 0; multiplicative on "
          "sampled coprime odd pairs (integer arithmetic)",
          ok_anchor and ok_mult
          and not np.any(ag[2::2]), "%.1f s" % (time.time() - t0))

    # Satake masses for the twist (and Deligne)
    spf = np.zeros(N_CAP + 1, dtype=np.int64)
    for p in range(2, N_CAP + 1):
        if spf[p] == 0:
            spf[p::p] = np.where(spf[p::p] == 0, p, spf[p::p])
    primes = [p for p in range(3, N_CAP + 1, 2) if spf[p] == p]

    def satake_comb(ap_of_p):
        pos, mas = [], []
        tmax = 0.0
        for p in primes:
            u1 = math.log(p)
            if u1 >= 2.0 * ALPHA_TOP:
                break
            t1 = float(ap_of_p(p)) / p ** 1.5
            tkm1, tkk = 2.0, t1
            k, u = 1, u1
            while u < 2.0 * ALPHA_TOP:
                pos.append(u)
                mas.append(2.0 * tkk * math.log(p) / p ** (0.5 * k))
                tmax = max(tmax, abs(tkk))
                tkm1, tkk = tkk, t1 * tkk - tkm1
                k += 1
                u = k * u1
        return np.array(pos), np.array(mas), tmax

    pos_g, mas_g, tmax_g = satake_comb(lambda p: ag[p])
    pos_f, mas_f, _tf = satake_comb(lambda p: a[p])
    check("T1.2 twist Satake layer: %d atoms; |t_k| <= 2 everywhere "
          "(max %.6f) -- Deligne survives twisting (|chi| = 1)"
          % (len(pos_g), tmax_g), tmax_g <= 2.0 + 1e-12)

    # T2 -- Fricke ward: f(1/(N t)) = eps N^2 t^4 f(t), weight 4
    print("    T2 conductor: Atkin-Li (1978, Thm 3.1) bound "
          "cond(f8 x chi4) | lcm(8, 4^2, 4) = 16; exact value by the "
          "Fricke ward:")
    nv = np.arange(1, FRICKE_NCAP + 1, dtype=float)

    def f_series(coeff, t):
        return float(np.dot(coeff[1:FRICKE_NCAP + 1],
                            np.exp(-2.0 * math.pi * nv * t)))

    def fricke_dev(coeff, N):
        R = [f_series(coeff, 1.0 / (N * t))
             / (N ** 2 * t ** 4 * f_series(coeff, t)) for t in FRICKE_T]
        if any(math.isnan(r) or math.isinf(r) for r in R):
            return float("inf"), 0
        eps = round(sum(R) / len(R))
        return max(abs(r - eps) for r in R), eps

    afl = a.astype(float)
    agl = ag.astype(float)
    dev_f8, eps_f8 = fricke_dev(afl, 8)
    check("T2.1 anchor: f8 itself is a W_8 eigenform, eps = %+d "
          "(max |R - eps| = %.1e <= 1e-8)" % (eps_f8, dev_f8),
          dev_f8 <= 1.0e-8 and abs(eps_f8) == 1)
    devs = {N: fricke_dev(agl, N) for N in (8, 16, 32)}
    for N, (d, e) in devs.items():
        print("      twist @ N = %-2d : max |R - eps| = %.3e "
              "(nearest eps = %+d)" % (N, d, e))
    ok_16 = devs[16][0] <= 1.0e-8 and abs(devs[16][1]) == 1
    ok_unique = all(devs[N][0] > 1.0e-2 for N in (8, 32))
    check("T2.2 the twist passes the Fricke ward at N = 16 ONLY "
          "(eps = %+d); wrong N in {8, 32} fail by > 1e-2 -- "
          "conductor(f8 x chi4) = 16" % devs[16][1],
          ok_16 and ok_unique)
    CONTROL_FIRED["C3"] = devs[8][0] > 1.0e-2
    check("C3 wrong-N Fricke control (N = 8 on the twist) FAILS as "
          "it must (dev %.2e > 1e-2)" % devs[8][0],
          CONTROL_FIRED["C3"])
    return dict(pos_g=pos_g, mas_g=mas_g, pos_f=pos_f, mas_f=mas_f,
                primes=primes, ag=ag)


# ============================================ S3 four-sector coherence
def lam_min(lagv, M):
    T = sla.toeplitz(lagv[:M])
    lam = float(sla.eigvalsh(T, subset_by_index=[0, 0])[0])
    return lam, float(sla.norm(T, 2))


def s3_sectors(lag, tw):
    section("S3 -- the four-sector PSD ladder (rule-derived continua "
            "only)")
    # GL1: deployed build (anchor, read-only)
    ka, masks, dev = srp.channel_masks(ALPHA_TOP)
    check("S3.0 tower comb consistency (deployed masses ward)",
          dev <= 1.0e-12, "rel dev %.1e, ka = %d" % (dev, ka))
    c_gl1 = srp.continuum_lags(M_TOP)
    for cnl in ("ro", "re", "sp", "in"):
        c_gl1 = c_gl1 + srp.atom_channel_lags(ALPHA_TOP, M_TOP,
                                              masks[cnl])
    nvals = np.array([int(round(math.exp(float(core.U_ALL[i]))))
                      for i in range(ka)], dtype=np.int64)
    odd = nvals % 2 == 1
    sgn = np.where(nvals % 4 == 1, 1.0, -1.0)
    cat4, _d = core.atom_lags_at(ALPHA_TOP, M_TOP,
                                 core.U_ALL[:ka][odd],
                                 (core.MU_ALL[:ka] * sgn)[odd])
    catf, _d = core.atom_lags_at(ALPHA_TOP, M_TOP, tw["pos_f"],
                                 tw["mas_f"])
    catg, _d = core.atom_lags_at(ALPHA_TOP, M_TOP, tw["pos_g"],
                                 tw["mas_g"])
    combs = {
        "GL1 (deployed anchor)": c_gl1,
        "chi4 (rule continuum)": lag["chi4"] + cat4,
        "f8 (rule continuum)": lag["f8"] + catf,
        "f8xchi4 (rule continuum)": lag["twist"] + catg,
    }
    print("    PSD table (lambda_min per rung, X = M/64):")
    print("      sector                    | " +
          " | ".join("X=%-2d" % int(M * DGRID) for M in RUNGS))
    psd, top = {}, {}
    for name, cv in combs.items():
        row = [lam_min(cv, M) for M in RUNGS]
        psd[name] = all(l >= -PSD_BAR * n for l, n in row)
        top[name] = row[-1][0]
        print("      %-25s | %s  [%s]"
              % (name, " | ".join("%+.2e" % l for l, _n in row),
                 "PSD" if psd[name] else "NEG"))
    ok1 = check("D1 THE DECIDER: the twist sector f8 x chi4 with the "
                "RULE-derived continuum {mu = 3/2, 5/2; q = 16} -- "
                "nothing hand-tuned -- is PSD on ALL %d rungs"
                % len(RUNGS), psd["f8xchi4 (rule continuum)"])
    ok2 = check("D2 FOUR-SECTOR COHERENCE: GL1 + chi4 + f8 + twist "
                "simultaneously PSD on every rung, same machinery",
                all(psd.values()))

    # battery Grams through all four sectors
    bat = hbp.battery(1.0)
    Fm = np.stack([v for _n, v in bat], axis=1)
    F = np.zeros((M_TOP, Fm.shape[1]))
    F[:Fm.shape[0]] = Fm
    gmin = {}
    for name, cv in combs.items():
        T = sla.toeplitz(cv[:M_TOP])
        Gm = F.T @ T @ F
        gmin[name] = float(np.linalg.eigvalsh(0.5 * (Gm + Gm.T))[0])
    check("S3.5 frozen-battery Grams PSD through all FOUR sectors "
          "(min eigs %s)" % ", ".join("%.0e" % v for v in
                                      gmin.values()),
          all(v >= -1.0e-12 for v in gmin.values()))

    # P0 conductor pinning: lambda_min is exactly linear in ln q
    lm = top["f8xchi4 (rule continuum)"]
    qmin = 16.0 * math.exp(-lm)
    shift = lam_min((lag["twist"] + catg
                     - np.eye(1, M_TOP, 0)[0] * math.log(2.0)), M_TOP)[0]
    ok_lin = abs(shift - (lm - math.log(2.0))) <= 1.0e-8
    check("P0 CONDUCTOR PINNING: lambda_min is exactly linear in "
          "ln q (identity shift verified: %.3e == %.3e - ln 2); PSD "
          "pins q >= 16 exp(-%.2e) = %.6f, Atkin-Li pins q | 16: the "
          "unique admissible conductor is 16 (relative width %.1e)"
          % (shift, lm, lm, qmin, lm), ok_lin)
    print("    B1 (carried over, typed): the twist-sector PSD is "
          "finite-level EVIDENCE (zeros of L(f8 x chi4) on the line "
          "as far\n       as they influence these windows); GRH-type "
          "statements unproven; NO RH/GRH claim.")
    return dict(combs=combs, psd=psd, top=top, catg=catg)


# ================================================ S4 remaining controls
def s4_controls(lag, tw, ss3):
    section("S4 -- controls + named readouts")
    catg = ss3["catg"]
    # C1 discriminating control: untwisted f8 continuum (q = 8) on the
    # twist sector -- ONLY the conductor constant differs (-ln 2 on
    # the diagonal)
    lam, _n = lam_min(lag["f8"] + catg, M_TOP)
    CONTROL_FIRED["C1"] = lam < -0.5
    check("C1 DISCRIMINATING CONTROL: the twist sector under the "
          "UNTWISTED f8 continuum (q = 8): lambda_min(top) = %+.6f "
          "< -0.5 (= margin - ln 2 = %+.6f; the conductor datum is "
          "load-bearing at 4 orders of magnitude above the margins)"
          % (lam, ss3["top"]["f8xchi4 (rule continuum)"]
             - math.log(2.0)), CONTROL_FIRED["C1"])

    # C2 scrambled twisted a_p on the correct rule continuum
    primes = tw["primes"]
    avals = [int(tw["ag"][p]) for p in primes]
    perm = list(range(len(avals)))
    for i in range(len(perm) - 1, 0, -1):
        j = lcg(i + 1)
        perm[i], perm[j] = perm[j], perm[i]
    pos_s, mas_s = [], []
    for pi, p in enumerate(primes):
        u1 = math.log(p)
        if u1 >= 2.0 * ALPHA_TOP:
            break
        t1 = float(avals[perm[pi]]) / p ** 1.5
        tkm1, tkk = 2.0, t1
        k, u = 1, u1
        while u < 2.0 * ALPHA_TOP:
            pos_s.append(u)
            mas_s.append(2.0 * tkk * math.log(p) / p ** (0.5 * k))
            tkm1, tkk = tkk, t1 * tkk - tkm1
            k += 1
            u = k * u1
    cat_s, _d = core.atom_lags_at(ALPHA_TOP, M_TOP, np.array(pos_s),
                                  np.array(mas_s))
    lam_s, _n = lam_min(lag["twist"] + cat_s, M_TOP)
    CONTROL_FIRED["C2"] = lam_s < 0.0
    check("C2 scrambled twisted a_p (LCG permutation, correct rule "
          "continuum): lambda_min(top) = %+.3e < 0" % lam_s,
          CONTROL_FIRED["C2"])

    # named readouts
    catm, _d = core.atom_lags_at(ALPHA_TOP, M_TOP, tw["pos_g"],
                                 -tw["mas_g"])
    lam_m, _n = lam_min(lag["twist"] + catm, M_TOP)
    print("    NAMED READOUT (not gated): sign-flipped twist comb on "
          "the rule continuum: lambda_min(top) = %+.3e" % lam_m)
    print("    NAMED (re-asserted, typed): the register mirror sector "
          "(+,0,0) remains NON-AUTOMORPHIC -- no completed L-function "
          "has\n      +Lambda(n)/sqrt(n) atoms uniformly (1/zeta-type "
          "channel, zeros <-> poles swapped); it carries NO "
          "positivity demand\n      and is OUTSIDE the domain of the "
          "rule map.  The rule's domain is the automorphic register "
          "characters; this probe\n      extends the verified domain "
          "to their twists (closure under the register group law "
          "chi4 (x) f8-channel).")


# ================================================================ verdict
def verdict(ss3):
    section("VERDICT")
    n_pass = sum(1 for _n, ok in CHECKS if ok)
    n_all = len(CHECKS)
    print("%d/%d checks passed" % (n_pass, n_all))
    controls_ok = all(CONTROL_FIRED.get(c, False)
                      for c in ("C1", "C2", "C3"))
    rule_ok = all(ok for n, ok in CHECKS if n.startswith("R1"))
    twist_ok = ss3["psd"]["f8xchi4 (rule continuum)"]
    coher_ok = all(ss3["psd"].values())
    if not twist_ok:
        v = ("CONDUCTOR-AD-HOC (the twist sector FAILS with the "
             "rule-derived continuum -- the assignment is a case "
             "table after all)")
    elif not (rule_ok and controls_ok):
        v = "CONDUCTOR-PARTIAL (%s)" % (
            "rule instance gate failed" if not rule_ok else
            "control void: %s" % [c for c in ("C1", "C2", "C3")
                                  if not CONTROL_FIRED.get(c, False)])
    elif coher_ok and n_pass == n_all:
        v = "CONDUCTOR-FUNCTORIAL"
    else:
        fails = [n for n, ok in CHECKS if not ok]
        v = "CONDUCTOR-PARTIAL (%s)" % ("; ".join(fails[:3]))
    print("VERDICT: %s" % v)
    if v == "CONDUCTOR-FUNCTORIAL":
        print("""
CONDUCTOR-FUNCTORIALITY -- CONDUCTOR-FUNCTORIAL.  The assignment
chi -> continuum is ONE closed structure map, not a case table:
  * THE RULE (q^{s/2} prod Gamma_R(s + mu_j), universal per-factor
    kernel, ln q at lag 0, pole iff trivial) reproduces all deployed
    and sibling kernels as instances -- including the weight-4 kernel
    through the DUPLICATION identity, two independent quadrature
    structures agreeing to 1e-12.
  * THE SECOND CUSPIDAL SECTOR f8 (x) chi_{-4} (register-internal,
    conductor 16 by Atkin-Li + the Fricke ward, nothing hand-tuned)
    is PSD on the entire ladder with the rule-derived continuum.
  * FOUR-SECTOR COHERENCE holds (GL1 + chi4 + f8 + twist, same
    machinery), and the conductor datum is LOAD-BEARING: swapping in
    the q = 8 constant breaks the twist sector by ln 2 -- four orders
    of magnitude above the margins -- while the PSD margins pin the
    conductor from below to relative width ~1e-5.
  * WHAT REMAINS for PRIME.POSITIVE_DESCENT.01: the INFINITE-LEVEL CP
    EXTENSION -- (i) sector-PSD persistence X -> infinity per
    automorphic sector (GRH-type, unproven, the honest open core);
    (ii) the register-group closure of the rule map (all twists of
    the verified sectors -- finite-level machinery now exists);
    (iii) the carrier intertwiner landing on these explicit formulas
    exactly (Satake == packet recursion, verified in the sibling).""")
    print("total runtime %.1f s" % (time.time() - T0))
    return v


def contract_update():
    section("RECOMMENDED CONTRACT UPDATE -- PRIME.POSITIVE_DESCENT.01 "
            "(report only; nothing written)")
    print("""\
    Demand (1) upgrades from 'sector-adapted continua exist
    finite-level' (sibling) to a FUNCTORIAL statement:
      (1-F) THE CONTINUUM FUNCTOR: on the automorphic register
            characters, chi -> Lambda_chi = q(chi)^{s/2}
            prod_j Gamma_R(s + mu_j(chi)) with (mu, q, pole) given by
            the closed rule (degree, weight/parity, ramified-register
            content); verified instances: GL1 (q=1, pole), chi4
            (q=4), f8 (q=8), f8 x chi4 (q=16).  The register group
            law is respected: the twist sector receives its continuum
            from the SAME rule with the Atkin-Li/Fricke conductor --
            no hand-tuning (gate C1 shows the conductor constant is
            load-bearing at ln 2 against ~1e-5 margins, and P0 shows
            the finite-level margins PIN the conductor from below).
      (2)   SECTOR-PSD PERSISTENCE (unchanged, now four sectors): the
            windows with rule-derived continua stay PSD as X -> oo in
            every automorphic sector -- the honest infinite-level
            core (GRH-type, unproven; finite-level margins all in the
            same thin-margin class with slow depth decay).
      (3)   THE CARRIER INTERTWINER (unchanged): must land sector by
            sector on EXACTLY these rule-derived explicit formulas.
    NEXT FALSIFIER (named): the INFINITE-LEVEL CP EXTENSION gate --
    formalize the finite-level windows as a net of CP maps on the
    packet algebra and identify the exact limit object whose
    positivity is demanded (the Weil/GRH positivity per sector); on
    the measurement side, the depth-trend decomposition (does the
    margin decay -0.24/X saturate or cross zero -- oscillation-aware,
    higher rungs).  STOP CONDITIONS unchanged: no RH/GRH claim,
    stop-list binding, deployed objects read-only.""")


def main():
    print("=" * 74)
    print("CONDUCTOR-FUNCTORIALITY -- the rule map + the second "
          "cuspidal sector")
    print("(follow-up to F8SECTOR-PSD; parent chain: DESCENT-PARTIAL)")
    print("=" * 74)
    g0_firewall()
    lag = s1_rule()
    tw = s2_twist()
    ss3 = s3_sectors(lag, tw)
    s4_controls(lag, tw, ss3)
    v = verdict(ss3)
    contract_update()
    n_pass = sum(1 for _n, ok in CHECKS if ok)
    return 0 if (n_pass == len(CHECKS)
                 and not v.startswith("CONDUCTOR-AD-HOC")) else 1


if __name__ == "__main__":
    sys.exit(main())
