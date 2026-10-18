#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""euler_scattering_source_probe -- PRIME.EULER.SCATTER.01
(EXPLORATION ONLY, experiments/; round 45, probe 2 of the review's
category shift: do local Euler Blaschke factors plus the Gamma
phase generate the deployed window lags EXACTLY -- making the von
Mangoldt comb the phase derivative of a cascade of lossless
one-state scatterers?  2026-08-09).

THE EXACT IDENTITY (frozen): for a_p = p^{-1/2} and
z_p(t) = e^{i t log p}, the Blaschke factor
    b_a(z) = (z - a)/(1 - a z)
satisfies on the unit circle
    d/dt arg b_{a_p}(z_p(t))
      = log p * (1 - a_p^2)/(1 - 2 a_p cos(t log p) + a_p^2)
      = log p + 2 sum_{k>=1} (log p / p^{k/2}) cos(t log p^k),
i.e. the nonconstant part is EXACTLY this prime's full von
Mangoldt comb 2 sum_k Lambda(p^k)/p^{k/2} cos(t log p^k),
including ALL prime powers.  Archimedean side: with
    Theta_Gamma(t) = pi^{-i t} Gamma(1/4 + i t/2)
                              / Gamma(1/4 - i t/2),
    (1/i) d/dt log Theta_Gamma(t) = Re psi(1/4 + i t/2) - log pi,
and the DEPLOYED archimedean lag layer (v563 arch_lags, read
verbatim) is the tent-tested Weil kernel of exactly this density:
its window cosine transform equals Re psi(1/4 + i tau_j/2) -
log pi up to the computable e^{-u/2} window-truncation tail
(verified with the tail added back; the raw gap IS the truncation
share, printed).

FROZEN PROTOCOL (2026-08-09, frozen + SHA-hashed before first
run; heavy rungs kz {9, 12, 13, 26, 40}; controls kz 9):

 E1  FACTOR IDENTITY: (i) SYMBOLIC (sympy, rational in (a, z) on
     the circle where cos phi = (z + 1/z)/2): z d/dz log b_a(z)
     == z/(z-a) + a z/(1 - a z) == (1 - a^2)/(1 - a (z + 1/z)
     + a^2) == 1 + a z/(1 - a z) + (a/z)/(1 - a/z) (the
     geometric resummation of 1 + sum_k a^k (z^k + z^-k)) --
     all by exact cancellation; hence d/dt arg b_{a_p}(z_p(t)) =
     log p * Poisson = log p + 2 sum_k Lambda(p^k) p^{-k/2}
     cos(t log p^k).  (ii) the lossless one-state realization
     U_p = [[a_p, s_p], [s_p, -a_p]], s_p = sqrt(1 - a_p^2):
     U_p^T U_p == I and the feedback transfer U22 + U21 z
     (1 - U11 z)^{-1} U12 == b_{a_p}(z), symbolic + exact
     radicals at p = 2, 3.  (iii) NUMERIC: per-prime truncated
     comb + EXACT geometric remainder == closed Poisson form,
     pointwise rel <= 1e-12 on a 257-point t-grid, p in
     {2, 3, 5, 101}.

 A   ARCH LAYER: (i) Theta_Gamma phase derivative == Re psi(1/4
     + i t/2) - log pi (mpmath central difference, dps 40,
     <= 1e-8).  (ii) the pairing identity Re psi(1/4 + i tau/2)
     - log pi == -(gamma + log pi) + 2 int_0^inf (e^{-2w}
     - cos(tau w) e^{-w/2})/(1 - e^{-2w}) dw by quadrature
     (<= 1e-6) -- this is the u-space kernel the deployed
     arch_lags tent-tests (v563 _arch_integrand, read verbatim).
     (iii) DEPLOYED: d_ar(theta_j) == [Re psi(1/4 + i tau_j/2)
     - log pi] + tail_j, tail_j = 2 int_{u_edge}^inf cos(tau_j w)
     e^{-w/2}/(1 - e^{-2w}) dw, u_edge = (M-1) D, rel <= 2e-2 at
     j = 1..8 on the heavy rungs (bar covers the tent second
     order + the half-weighted edge cell, O(e^{-u_edge/2} D));
     TYPED check, no kill -- the raw no-tail gap printed is the
     exact relation's truncation share.

 E2  WINDOW ASSEMBLY (exact rebracketing, Ward 1e-12): own
     boolean sieve (allowed, v882 precedent: "own SPF sieves
     inside the probes") enumerates primes p and prime powers
     p^k with log p^k <= 2 alpha + 1e-14 (the deployed atoms_in
     cutoff, verbatim); the grouped atom set {(log p^k,
     2 log p / p^{k/2})} must equal the deployed table (census
     match; max |du|, |dmu| <= 1e-12) and the per-prime tent
     assembly sum_p atom_lags_at(alpha, M, uu_p, mm_p) must
     equal the deployed c_atoms, rel <= 1e-12 -- the deployed
     prime-power sum IS the Euler grouping by p, exactly
     rebracketed; primes vs prime powers counted per rung.

 E3  CASCADE READING (typed, stated honestly): B(t) =
     prod_{p <= X} b_{a_p}(e^{i t log p}) is a QUASI-PERIODIC
     product (Bohr lift: one factor per circle z_p = e^{i t
     log p}; NOT a single Blaschke product in one disk variable)
     -- each factor is unimodular on its own circle (max
     ||b_p| - 1| <= 1e-13 per factor, product <= 1e-11 on the
     t-grid) and the total phase derivative == theta(X) +
     the deployed arch-free comb + the EXACT per-prime k > K_p
     geometric tails, rel <= 1e-10 (kz 9 prime set); the k-tail
     share beyond the deployed p^k <= X cutoff printed.  Typed
     EULER-CASCADE-EXACT iff E1 + E2 ward.

 E4  GENERATOR MATCH (the decisive test, typed): cascade
     reflection r_X(tau) by Moebius composition of the U_p
     stages (load 0, primes composed in descending order --
     smallest prime outermost), stage map rho -> (a_p + z_p rho)
     / (1 + a_p z_p rho), z_p = e^{i tau log p}, evaluated at
     the port frequencies tau_j; IIKS generators (f, g) of
     [Y, D_P] extracted as in port_riemann_hilbert_setup_probe
     SPEC v2 (copied verbatim).  GAUGE (documented): the
     antisymmetric SVD frame carries a per-rung rotation gauge
     under which atan(m_j), m_j = g_j/f_j, shifts by a constant
     mod pi -- so the frozen comparison is ANCHORED at the
     lowest port node: dphi_j = wrap_pi(atan2(g_j, f_j) -
     atan2(g_0, f_0)) vs Theta_j = wrap_pi(KAPPA * wrap_2pi(
     arg r_X(tau_j) - arg r_X(tau_0))) with the ONE global
     source-determined normalization KAPPA = 1/2 (the Cayley
     half-angle of the Moebius rotation action; frozen, same
     for ALL rungs, no fit).  Report Pearson correlation +
     median rel deviation per rung; typed SOURCE-MATCH iff
     median rel <= 0.1 on ALL heavy rungs, SOURCE-O1-MISMATCH
     otherwise (the review's kill: displacement right, source
     wrong).

 C   CONTROLS (kz 9, must fire): (i) EPSTEIN comb (x^2 + 5 y^2,
     its own lambda by the deployed recursion): NOT a prime
     Euler cascade -- the per-prime regrouping must FAIL:
     non-prime-power |mass| share >= 0.1 AND the prime-power-
     only rebuild misses c_at^E by rel >= 0.1 (the geometric-
     in-k losslessness ratio lambda_E(p^2)/lambda_E(p) is
     REPORTED; inside this window only p = 5 is testable and is
     ramified-multiplicative -- typed, not the fire).
     (ii) SCRAMBLE (log-uniform positions, deployed convention
     seed 1): structurally off the prime-power grid (hit
     fraction <= 0.01 at atol 1e-9) -- the regrouping does not
     even parse; the c_at sensitivity printed.

KILLS: K1 an exact identity breaks (E1 / A(i)(ii) / E2 / E3
algebra) -> IDENTITY-BROKEN; K2 pipeline breaks (census, ports,
chain) -> PIPELINE-BROKEN; K3 controls silent -> CONTROL-DEAD.
A(iii) and E4 are TYPED (honest fail possible, no kill).

VERDICT (frozen enum): EULERSCATTER-MEASURED (+ typed sublabels
EULER-CASCADE-EXACT and SOURCE-MATCH / SOURCE-O1-MISMATCH) /
PIPELINE-BROKEN / IDENTITY-BROKEN / CONTROL-DEAD.

NO RH claim: the cascade names the SOURCE of the deployed comb
(lossless local scatterers + the Gamma phase); it does not bound
any error term.

FIREWALL: no zeros, no prime oracles (AST scan; banned ids
zetazero / nzeros / primerange / isprime / primepi / nextprime /
prevprime); the per-prime regrouping REQUIRES an own prime
enumeration -- an own boolean Eratosthenes sieve is used
(allowed, v882 precedent), documented here; v563 READ-ONLY; RNG
only inside the declared scramble control; stdout only.  No
marker moves.

Sources (read-only): v563_paper2_readouts (arch_lags +
atom_lags_at + atoms_in cutoff, read verbatim);
port_atom_numerator_probe (windowed prime-sum identity, declared
input); port_riemann_hilbert_setup_probe SPEC v2 (IIKS generator
extraction, copied verbatim); v882_port_source_mellin (own-sieve
precedent); carleson_testing_law_probe (ATOM-CARRIED, context).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/euler_scattering_source_probe.py
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

HEAVY = (9, 12, 13, 26, 40)
E1_PRIMES = (2, 3, 5, 101)
KAPPA = 0.5                    # the frozen Cayley half-angle (E4)
BANNED_IDS = ("zetazero", "nzeros", "primerange", "isprime",
              "primepi", "nextprime", "prevprime")
LOG_PI = math.log(math.pi)
EULER_GAMMA = float(np.euler_gamma)

CHECKS = []
KILLS = []
T0 = time.time()


def check(name, ok, detail="", kill=None):
    CHECKS.append((name, bool(ok)))
    if kill and not ok:
        KILLS.append(kill)
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


# ---------------------------------------------------------------- window
def grid_density(c):
    c = np.asarray(c, float)
    a = np.concatenate([c, c[-2:0:-1]])
    d = np.fft.fft(a)
    assert float(np.max(np.abs(d.imag))) <= 1e-9 * max(
        1.0, float(np.max(np.abs(d.real))))
    return d.real


def cos_transform(cvec, M, L, jlist):
    out = []
    kk = np.arange(1, M - 1)
    for j in jlist:
        th = 2.0 * math.pi * j / L
        out.append(float(cvec[0] + 2.0 * np.sum(
            cvec[1:M - 1] * np.cos(kk * th))
            + cvec[M - 1] * math.cos((M - 1) * th)))
    return np.array(out)


def build_rung(kz, scramble_seed=None, comb=None):
    rr = core.build_window(kz, scramble_seed=scramble_seed)
    h, M, D, alpha = rr["h"], rr["M"], rr["D"], rr["alpha"]
    uu = np.asarray(rr["uu"], float)
    mm = 2.0 * np.asarray(rr["lam"], float)
    if comb is not None:
        uu, mm = comb
    c_at, _ = core.atom_lags_at(alpha, M, uu, mm)
    c_ar = np.asarray(core.arch_lags(M, D), float)
    d = grid_density(c_ar + c_at)
    return dict(d=d, c_at=np.asarray(c_at, float), c_ar=c_ar,
                L=2 * M - 2, M=M, D=D, alpha=alpha, h=h,
                uu=uu, mm=mm)


# ------------------------------------------------- own sieve (documented)
def sieve_primes(N):
    """Own boolean Eratosthenes sieve, no oracle imports (allowed,
    v882 precedent)."""
    if N < 2:
        return []
    s = np.ones(N + 1, dtype=bool)
    s[:2] = False
    for i in range(2, int(math.isqrt(N)) + 1):
        if s[i]:
            s[i * i::i] = False
    return [int(p) for p in np.nonzero(s)[0]]


def euler_grouped_atoms(alpha):
    """The deployed atom law regrouped by prime: for each prime p,
    the atoms (u = log p^k, mu = 2 log p / p^{k/2}) with the
    deployed cutoff log p^k <= 2 alpha + 1e-14 (atoms_in,
    verbatim).  Returns {p: (u_array, mu_array)}."""
    ucut = 2.0 * alpha + 1.0e-14
    Nint = int(math.floor(math.exp(ucut))) + 1
    groups = {}
    for p in sieve_primes(Nint):
        lp = math.log(p)
        if lp > ucut:
            break
        us, mus = [], []
        n = p
        while math.log(n) <= ucut:
            us.append(math.log(n))
            mus.append(2.0 * lp / math.sqrt(n))
            n *= p
        if us:
            groups[p] = (np.array(us), np.array(mus))
    return groups


# ------------------------------------------------- quadrature helpers
_GLX32, _GLW32 = np.polynomial.legendre.leggauss(32)


def gl_int(fun, a, b, width):
    tot = 0.0
    x0 = a
    while x0 < b - 1e-12:
        x1 = min(x0 + width, b)
        mid, half = 0.5 * (x0 + x1), 0.5 * (x1 - x0)
        w = mid + half * _GLX32
        tot += half * float(np.dot(_GLW32, fun(w)))
        x0 = x1
    return tot


def weil_F(w):
    """The u-space arch kernel factor e^{-w/2}/(1 - e^{-2w})."""
    return np.exp(-0.5 * w) / (-np.expm1(-2.0 * w))


def psi_quarter(tau):
    """Re psi(1/4 + i tau/2) - log pi via mpmath."""
    import mpmath as mp
    return float(mp.re(mp.digamma(mp.mpc(0.25, 0.5 * tau)))) - LOG_PI


# ------------------------------------------------- IIKS port (verbatim)
def lambda_eps(N):
    r = np.zeros(N + 1)
    s = int(math.isqrt(N)) + 1
    for x in range(-s, s + 1):
        for y in range(-s, s + 1):
            v = x * x + 5 * y * y
            if 1 <= v <= N:
                r[v] += 1.0
    a = r / 2.0
    lam = np.zeros(N + 1)
    for n in range(2, N + 1):
        acc = a[n] * math.log(n)
        for dd in range(2, n):
            if n % dd == 0:
                acc -= lam[dd] * a[n // dd]
        lam[n] = acc
    return lam


def folded_measure(d_arm, L, sign=+1.0):
    jj = np.arange(L)
    keep = (sign * d_arm) > 0.0
    jj = jj[keep]
    th = 2.0 * math.pi * jj / L
    wt = (np.abs(d_arm[keep]) / (2.0 * L)) * 4.0 * np.sin(
        th / 2.0) ** 2
    fold = np.minimum(jj, L - jj)
    uf, inv = np.unique(fold, return_inverse=True)
    wagg = np.zeros(len(uf))
    np.add.at(wagg, inv, wt)
    xs = np.cos(2.0 * math.pi * uf / L)
    m = wagg > 1e-300
    return xs[m], wagg[m], uf[m]


def lanczos_chain(x, w, n):
    m0 = float(np.sum(w))
    m = len(x)
    Q = np.zeros((m, n))
    Q[:, 0] = np.sqrt(w) / math.sqrt(m0)
    al = np.zeros(n)
    be = np.zeros(max(n - 1, 0))
    steps = n
    for k in range(n):
        z = x * Q[:, k]
        al[k] = float(Q[:, k] @ z)
        z = z - al[k] * Q[:, k]
        if k > 0:
            z = z - be[k - 1] * Q[:, k - 1]
        for _ in range(2):
            z = z - Q[:, :k + 1] @ (Q[:, :k + 1].T @ z)
        if k == n - 1:
            break
        bnorm = float(np.linalg.norm(z))
        if bnorm <= 1e-14:
            steps = k + 1
            break
        be[k] = bnorm
        Q[:, k + 1] = z / bnorm
    return al[:steps], be[:max(steps - 1, 0)], m0, steps


def eval_chain(al, be, m0, y, n):
    P = np.zeros((len(y), n))
    P[:, 0] = 1.0 / math.sqrt(m0)
    if n > 1:
        P[:, 1] = (y - al[0]) * P[:, 0] / be[0]
    for k in range(1, n - 1):
        P[:, k + 1] = ((y - al[k]) * P[:, k]
                       - be[k - 1] * P[:, k - 1]) / be[k]
    return P


def dressed_port(kz, **kw):
    b = build_rung(kz, **kw)
    h, L, D = b["h"], b["L"], b["D"]
    if h > 900:
        return None
    xs, ws, _ = folded_measure(b["d"], L, +1.0)
    ys, vs, uf_n = folded_measure(b["d"], L, -1.0)
    al, be, m0, steps = lanczos_chain(xs, ws, h + 1)
    if steps < h + 1 or np.any(be <= 0):
        return None
    Pn = eval_chain(al, be, m0, ys, h)
    G = np.sqrt(vs)[:, None] * (Pn @ Pn.T) * np.sqrt(vs)[None, :]
    G = 0.5 * (G + G.T)
    tau_m = (2.0 * math.pi * uf_n / L) / D
    port = tau_m <= float(np.max(tau_m)) / 10.0
    ip, ib = np.where(port)[0], np.where(~port)[0]
    P = G[np.ix_(ip, ip)]
    X = G[np.ix_(ip, ib)]
    R = G[np.ix_(ib, ib)]
    IR = np.eye(len(ib)) - R
    DP = P + X @ np.linalg.solve(IR, X.T)
    DP = 0.5 * (DP + DP.T)
    return dict(DP=DP, yp=ys[ip], tau=tau_m[ip], h=h,
                alpha=b["alpha"])


def antisym_generators(C):
    """Canonical (f, g) with C = f g^T - g f^T (RH-setup SPEC v2,
    verbatim)."""
    U, sv, _Vh = np.linalg.svd(C)
    s1 = sv[0]
    f = math.sqrt(s1) * U[:, 0]
    g = math.sqrt(s1) * U[:, 1]
    Ct = np.outer(f, g) - np.outer(g, f)
    if np.linalg.norm(Ct + C) < np.linalg.norm(Ct - C):
        g = -g
    return f, g, sv


# ------------------------------------------------- cascade (E3 / E4)
def cascade_reflection(tau, primes_desc):
    """Moebius composition of the U_p stages, load 0, smallest
    prime outermost: rho -> (a_p + z_p rho)/(1 + a_p z_p rho)."""
    tau = np.asarray(tau, float)
    rho = np.zeros(len(tau), dtype=complex)
    for p in primes_desc:
        a = 1.0 / math.sqrt(p)
        z = np.exp(1j * tau * math.log(p))
        rho = (a + z * rho) / (1.0 + a * z * rho)
    return rho


def wrap_pi(x):
    return x - math.pi * np.round(x / math.pi)


def wrap_2pi(x):
    return x - 2.0 * math.pi * np.round(x / (2.0 * math.pi))


# ------------------------------------------------------------------ main
def main():
    section("PRIME.EULER.SCATTER.01 -- Euler Blaschke cascade as "
            "the source of the window comb (EXPLORATION ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s"
          % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
    print("    NO RH claim; own sieve; no marker moves.")
    print("\nS0 -- firewall")
    check("S0.1 AST firewall clean (own sieve, no oracles)",
          not ast_scan(BANNED_IDS))

    # ------------------------------------------------------------ E1
    section("E1 -- the factor identity (symbolic + numeric)")
    import sympy as sp
    a, z, w = sp.symbols("a z w", positive=True)
    b_az = (z - a) / (1 - a * z)
    lhs = sp.cancel(z * sp.diff(sp.log(b_az), z))       # z b'/b
    circle = z / (z - a) + a * z / (1 - a * z)
    poisson = (1 - a ** 2) / (1 - a * (z + 1 / z) + a ** 2)
    resum = 1 + a * z / (1 - a * z) + (a / z) / (1 - a / z)
    ok_s = (sp.cancel(lhs - circle) == 0
            and sp.cancel(sp.together(circle - poisson)) == 0
            and sp.cancel(sp.together(circle - resum)) == 0)
    check("E1.1 SYMBOLIC: z d/dz log b == z/(z-a) + az/(1-az) == "
          "Poisson closed form == geometric comb resummation "
          "1 + sum_k a^k (z^k + z^-k) (exact cancellation)",
          ok_s, kill="K1")

    s_ = sp.sqrt(1 - a ** 2)
    U = sp.Matrix([[a, s_], [s_, -a]])
    ok_u = sp.simplify(U.T * U - sp.eye(2)) == sp.zeros(2)
    transfer = U[1, 1] + U[1, 0] * w * U[0, 1] / (1 - U[0, 0] * w)
    ok_t = sp.cancel(sp.together(transfer - (w - a) / (1 - a * w))
                     ) == 0
    ok_ex = True
    for p in (2, 3):
        ap = 1 / sp.sqrt(p)
        Up = sp.Matrix([[ap, sp.sqrt(1 - sp.Rational(1, p))],
                        [sp.sqrt(1 - sp.Rational(1, p)), -ap]])
        ok_ex &= sp.simplify(Up.T * Up - sp.eye(2)) == sp.zeros(2)
    check("E1.2 REALIZATION: U_p unitary (symbolic + exact "
          "radicals p = 2, 3) and feedback transfer == b_{a_p}",
          ok_u and ok_t and ok_ex, kill="K1")

    tg = np.linspace(0.31, 23.7, 257)
    rel1max = 0.0
    for p in E1_PRIMES:
        L_ = math.log(p)
        ap = p ** -0.5
        closed = L_ * (1.0 - ap * ap) / (
            1.0 - 2.0 * ap * np.cos(tg * L_) + ap * ap)
        K = int(math.ceil(120.0 / L_))
        kk = np.arange(1, K + 1)
        series = L_ * (1.0 + 2.0 * np.sum(
            (ap ** kk)[:, None] * np.cos(np.outer(kk * L_, tg)),
            axis=0))
        zz = ap * np.exp(1j * tg * L_)
        rem = 2.0 * L_ * np.real(zz ** (K + 1) / (1.0 - zz))
        rel = float(np.max(np.abs(closed - series - rem)
                           / np.abs(closed)))
        rel1max = max(rel1max, rel)
        print("    p = %-4d: K = %3d terms, comb + exact "
              "remainder vs closed Poisson rel %.2e" % (p, K, rel))
    check("E1.3 NUMERIC comb identity: per-prime full von "
          "Mangoldt comb == Blaschke phase derivative on the "
          "t-grid (max rel %.1e <= 1e-12)" % rel1max,
          rel1max <= 1e-12, kill="K1")

    # ------------------------------------------------------------ A
    section("A -- the Gamma phase and the deployed arch layer")
    import mpmath as mp
    mp.mp.dps = 40
    h_fd = mp.mpf("1e-6")
    devA = 0.0
    for t in (0.7, 2.3, 7.9, 19.1):
        tt = mp.mpf(t)

        def argTheta(x):
            return mp.im(-1j * x * mp.log(mp.pi)
                         + mp.loggamma(0.25 + 0.5j * x)
                         - mp.loggamma(0.25 - 0.5j * x))

        fd = float((argTheta(tt + h_fd) - argTheta(tt - h_fd))
                   / (2 * h_fd))
        ref = psi_quarter(t)
        devA = max(devA, abs(fd - ref))
    check("A1 Theta_Gamma: (1/i) d/dt log Theta == Re psi(1/4 + "
          "i t/2) - log pi (central diff, max dev %.1e <= 1e-8)"
          % devA, devA <= 1e-8, kill="K1")

    devP = 0.0
    for tau in (0.5, 1.5, 5.0, 12.0):
        quad = -(EULER_GAMMA + LOG_PI) + 2.0 * gl_int(
            lambda x: (np.exp(-2.0 * x)
                       - np.cos(tau * x) * np.exp(-0.5 * x))
            / (-np.expm1(-2.0 * x)), 0.0, 80.0, 0.5)
        devP = max(devP, abs(quad - psi_quarter(tau)))
    check("A2 PAIRING identity: -(gamma + log pi) + 2 int (e^-2w "
          "- cos e^-w/2)/(1 - e^-2w) == Re psi - log pi (max dev "
          "%.1e <= 1e-6)" % devP, devP <= 1e-6, kill="K1")

    relAmax = rawAmax = 0.0
    rungs = {}
    for kz in HEAVY:
        b = build_rung(kz)
        rungs[kz] = b
        M, L, D = b["M"], b["L"], b["D"]
        u_edge = (M - 1) * D
        jl = list(range(1, 9))
        d_ar = cos_transform(b["c_ar"], M, L, jl)
        relA = rawA = 0.0
        for jx, j in enumerate(jl):
            tau_j = (2.0 * math.pi * j / L) / D
            ref = psi_quarter(tau_j)
            tail = 2.0 * gl_int(
                lambda x: np.cos(tau_j * x) * weil_F(x),
                u_edge, u_edge + 80.0, 0.25)
            relA = max(relA, abs(d_ar[jx] - (ref + tail))
                       / abs(ref))
            rawA = max(rawA, abs(d_ar[jx] - ref) / abs(ref))
        relAmax = max(relAmax, relA)
        rawAmax = max(rawAmax, rawA)
        print("    kz %-3d (M %4d, u_edge %.2f): |d_ar - (Re psi "
              "- log pi + tail)| rel %.2e | raw no-tail gap "
              "%.2e (the truncation share)"
              % (kz, M, u_edge, relA, rawA))
    check("A3 DEPLOYED arch layer (typed): the window cosine "
          "transform of arch_lags == the Theta_Gamma phase-"
          "derivative density + the computable e^{-u/2} "
          "truncation tail (max rel %.1e <= 2e-2; raw gap max "
          "%.1e printed)" % (relAmax, rawAmax), relAmax <= 2e-2)

    # ------------------------------------------------------------ E2
    section("E2 -- the window assembly as an exact Euler "
            "rebracketing (heavy rungs)")
    census_ok = True
    duMax = dmuMax = relWmax = 0.0
    groups_by_kz = {}
    for kz in HEAVY:
        b = rungs[kz]
        g = euler_grouped_atoms(b["alpha"])
        groups_by_kz[kz] = g
        us = np.concatenate([g[p][0] for p in g])
        mus = np.concatenate([g[p][1] for p in g])
        o = np.argsort(us)
        us, mus = us[o], mus[o]
        n_pp = len(b["uu"])
        if len(us) != n_pp:
            census_ok = False
            print("    kz %-3d CENSUS MISMATCH: %d grouped vs %d "
                  "deployed" % (kz, len(us), n_pp))
            continue
        du = float(np.max(np.abs(us - b["uu"])))
        dmu = float(np.max(np.abs(mus - b["mm"])))
        duMax, dmuMax = max(duMax, du), max(dmuMax, dmu)
        c_reb = np.zeros(b["M"])
        for p in g:
            c_reb += core.atom_lags_at(b["alpha"], b["M"],
                                       g[p][0], g[p][1])[0]
        relW = float(np.linalg.norm(c_reb - b["c_at"])
                     / np.linalg.norm(b["c_at"]))
        relWmax = max(relWmax, relW)
        print("    kz %-3d: %4d primes -> %4d prime powers "
              "(X = e^%.2f) | set match du %.1e dmu %.1e | "
              "per-prime tent rebuild rel %.1e"
              % (kz, len(g), n_pp, 2.0 * b["alpha"], du, dmu,
                 relW))
    check("E2.1 CENSUS + SET: the Euler grouping by p enumerates "
          "EXACTLY the deployed prime-power table (max |du| "
          "%.1e, |dmu| %.1e <= 1e-12)" % (duMax, dmuMax),
          census_ok and duMax <= 1e-12 and dmuMax <= 1e-12,
          kill="K1")
    check("E2.2 REBRACKETING WARD: sum_p atom_lags_at(p-group) == "
          "deployed c_atoms (max rel %.1e <= 1e-12) -- the "
          "deployed window comb IS the tent-weighted sum of "
          "per-prime Blaschke combs" % relWmax,
          relWmax <= 1e-12, kill="K1")
    e2_ok = CHECKS[-1][1] and CHECKS[-2][1]

    # ------------------------------------------------------------ E3
    section("E3 -- the quasi-periodic cascade trace (kz 9 prime "
            "set)")
    b9 = rungs[9]
    g9 = groups_by_kz[9]
    plist = sorted(g9)
    tg3 = np.linspace(0.31, 23.7, 257)
    facdev = 0.0
    Bt = np.ones(len(tg3), dtype=complex)
    dsum = np.zeros(len(tg3))
    tails = np.zeros(len(tg3))
    theta_X = 0.0
    for p in plist:
        L_ = math.log(p)
        ap = p ** -0.5
        zt = np.exp(1j * tg3 * L_)
        bf = (zt - ap) / (1.0 - ap * zt)
        facdev = max(facdev, float(np.max(np.abs(np.abs(bf)
                                                 - 1.0))))
        Bt *= bf
        dsum += L_ * (1.0 - ap * ap) / (
            1.0 - 2.0 * ap * np.cos(tg3 * L_) + ap * ap)
        Kp = len(g9[p][0])
        zz = ap * zt
        tails += 2.0 * L_ * np.real(zz ** (Kp + 1) / (1.0 - zz))
        theta_X += L_
    comb = np.array([float(np.sum(b9["mm"] * np.cos(t * b9["uu"])))
                     for t in tg3])
    moddev = float(np.max(np.abs(np.abs(Bt) - 1.0)))
    rel3 = float(np.max(np.abs(dsum - (theta_X + comb + tails)))
                 / np.max(np.abs(dsum)))
    print("    %d primes (X = %.0f): per-factor max ||b|-1| = "
          "%.1e | product max ||B|-1| = %.1e" %
          (len(plist), math.exp(2.0 * b9["alpha"]), facdev,
           moddev))
    print("    total phase derivative vs theta(X) + deployed comb "
          "+ exact k-tails: rel %.1e | max |k-tail| %.3f vs max "
          "|comb| %.3f (share %.4f)"
          % (rel3, float(np.max(np.abs(tails))),
             float(np.max(np.abs(comb))),
             float(np.max(np.abs(tails)) / np.max(np.abs(comb)))))
    print("    HONEST TYPE: B(t) is a Bohr-lift QUASI-PERIODIC "
          "product (one circle per prime), lossless in each "
          "factor; it is NOT a single-disk Blaschke product.")
    check("E3.1 CASCADE: every factor unimodular (%.1e <= 1e-13; "
          "product %.1e <= 1e-11) and total phase derivative == "
          "theta(X) + arch-free comb + exact geometric k-tails "
          "(rel %.1e <= 1e-10)" % (facdev, moddev, rel3),
          facdev <= 1e-13 and moddev <= 1e-11 and rel3 <= 1e-10,
          kill="K1")
    e3_ok = CHECKS[-1][1]

    # ------------------------------------------------------------ E4
    section("E4 -- the generator match (cascade reflection vs "
            "IIKS generators; KAPPA = 1/2 frozen)")
    medians = []
    pipe_ok = True
    for kz in HEAVY:
        r = dressed_port(kz)
        if r is None or len(r["tau"]) < 4:
            pipe_ok = False
            print("    kz %-3d: PORT PIPELINE FAILED" % kz)
            continue
        Y = np.diag(r["yp"])
        C = Y @ r["DP"] - r["DP"] @ Y
        f, g, sv = antisym_generators(C)
        rk = float(sv[2] / sv[0]) if len(sv) > 2 else 0.0
        phi = np.arctan2(g, f)
        dphi = wrap_pi(phi - phi[0])
        prim = sorted(groups_by_kz[kz], reverse=True)
        rX = cascade_reflection(r["tau"], prim)
        Theta = wrap_pi(KAPPA * wrap_2pi(np.angle(rX)
                                         - np.angle(rX[0])))
        dv, tv = dphi[1:], Theta[1:]
        med = float(np.median(np.abs(dv - tv)
                              / np.maximum(np.abs(dv), 1e-300)))
        corr = float(np.corrcoef(dv, tv)[0, 1]) if len(dv) > 2 \
            else float("nan")
        medians.append(med)
        print("    kz %-3d: %2d ports, rank ward s3/s1 %.1e | "
              "corr(dphi, Theta) %+.3f | median rel dev %.3f"
              % (kz, len(r["tau"]), rk, corr, med))
        print("            dphi[1:5]  = %s"
              % np.array2string(dv[:4], precision=4))
        print("            Theta[1:5] = %s"
              % np.array2string(tv[:4], precision=4))
    check("E4.0 pipeline: all heavy-rung ports extracted",
          pipe_ok and len(medians) == len(HEAVY), kill="K2")
    src_label = ("SOURCE-MATCH"
                 if medians and max(medians) <= 0.1
                 else "SOURCE-O1-MISMATCH")
    check("E4.1 typed: %s -- median rel deviation per rung %s "
          "(bar 0.1 on ALL rungs, ONE frozen normalization "
          "KAPPA = 1/2)" % (src_label,
                            ["%.3f" % m for m in medians]), True)

    # ------------------------------------------------------------ C
    section("C -- controls (kz 9)")
    alpha9, M9 = b9["alpha"], b9["M"]
    N_E = int(math.floor(math.exp(2.0 * alpha9))) + 1
    lamE = lambda_eps(N_E)
    nn = np.nonzero(np.abs(lamE) > 1e-12)[0]
    uu_E = np.log(nn.astype(float))
    mm_E = 2.0 * lamE[nn] / np.sqrt(nn.astype(float))
    pp_set = set()
    for p in sieve_primes(N_E):
        n = p
        while n <= N_E:
            pp_set.add(n)
            n *= p
    is_pp = np.array([int(n) in pp_set for n in nn])
    share_npp = float(np.sum(np.abs(mm_E[~is_pp]))
                      / np.sum(np.abs(mm_E)))
    c_E = core.atom_lags_at(alpha9, M9, uu_E, mm_E)[0]
    c_Epp = core.atom_lags_at(alpha9, M9, uu_E[is_pp],
                              mm_E[is_pp])[0]
    rel_E = float(np.linalg.norm(c_E - c_Epp)
                  / np.linalg.norm(c_E))
    ratio_txt = "none testable"
    if lamE[5] != 0.0 and N_E >= 25 and lamE[25] != 0.0:
        ratio_txt = ("lambda_E(25)/lambda_E(5) = %.3f "
                     "(ramified p = 5; typed, not the fire)"
                     % (lamE[25] / lamE[5]))
    print("    Epstein : non-prime-power |mass| share %.3f | "
          "prime-power-only rebuild misses c_at^E by rel %.3f | "
          "losslessness ratio: %s"
          % (share_npp, rel_E, ratio_txt))
    ok_E = share_npp >= 0.1 and rel_E >= 0.1

    rr9s = core.build_window(9, scramble_seed=1)
    uu_s = np.asarray(rr9s["uu"], float)
    grid = np.sort(np.concatenate([g9[p][0] for p in g9]))
    idx = np.searchsorted(grid, uu_s)
    idx = np.clip(idx, 1, len(grid) - 1)
    dmin = np.minimum(np.abs(uu_s - grid[idx - 1]),
                      np.abs(uu_s - grid[idx]))
    hit = float(np.mean(dmin <= 1e-9))
    c_s, _ = core.atom_lags_at(alpha9, M9, uu_s, b9["mm"])
    sens = float(np.linalg.norm(np.asarray(c_s) - b9["c_at"])
                 / np.linalg.norm(b9["c_at"]))
    print("    scramble: prime-power-grid hit fraction %.4f "
          "(atol 1e-9) -- regrouping does not parse | c_at "
          "sensitivity %.2f" % (hit, sens))
    ok_S = hit <= 0.01
    check("C1 CONTROLS FIRE: Epstein is NOT a prime Euler "
          "cascade (non-pp share %.3f >= 0.1, rebuild miss %.3f "
          ">= 0.1) and scramble is structurally off the grid "
          "(hit %.4f <= 0.01)" % (share_npp, rel_E, hit),
          ok_E and ok_S, kill="K3")

    # ------------------------------------------------------------ V
    section("V -- FROZEN VERDICT")
    n_pass = sum(1 for _n, okk in CHECKS if okk)
    n_tot = len(CHECKS)
    if KILLS:
        VERDICT = {"K1": "IDENTITY-BROKEN",
                   "K2": "PIPELINE-BROKEN",
                   "K3": "CONTROL-DEAD"}[KILLS[0]]
        print("\n  VERDICT: %s" % VERDICT)
    else:
        casc = ("EULER-CASCADE-EXACT" if (e2_ok and e3_ok)
                else "EULER-CASCADE-BROKEN")
        print("\n  VERDICT: EULERSCATTER-MEASURED (%s, %s)"
              % (casc, src_label))
    print("""
  NAMED READING (printed, not claimed): each prime is a lossless
  one-state scatterer U_p; its Blaschke phase derivative is that
  prime's FULL von Mangoldt comb (all powers, exactly); the
  deployed window comb is the tent-weighted Euler regrouping of
  these factors, and the deployed arch layer is the Gamma-factor
  phase derivative Re psi(1/4 + i tau/2) - log pi up to the
  computable window tail.  The one-variable trace B(t) is a
  Bohr-lift quasi-periodic product, NOT a single Blaschke
  product.  Whether the cascade reflection also generates the
  extracted IIKS generators is the E4 typing above.  NO RH
  claim.""")
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed"
          % (time.time() - T0, n_tot, n_tot - n_pass))
    return 0 if n_pass == n_tot else 1


if __name__ == "__main__":
    raise SystemExit(main())
