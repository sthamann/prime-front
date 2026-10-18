#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""moebius_source_step_probe -- PRIME.PORT.MOEBIUS.SOURCE.01
(EXPLORATION ONLY, experiments/; round 46, the new front-runner
after the round-45 route decisions: can the measured per-rung
Moebius step of the port carrier be DERIVED from source/window
data alone?  2026-08-09).

THE QUESTION (frozen): port_schur_cocycle_probe CONFIRMED that
the PSL(2,R)-normalized carrier m_h = g/f moves by a SINGLE
Moebius map per rung (median chordal residual 0.0015 over 41
steps; all fitted steps upper-half-plane J-contractions,
|alpha| < 1 on 100%, median |alpha| ~ 0.002).  The rung step
h -> h' changes the window by KNOWN source data: the atoms
entering (or leaving) the window, the window geometry (alpha, D,
M), and the archimedean layer.  Is the measured step T_h
COMPUTABLE from the source increment -- with NO per-rung fitting
against the measurement?

THE LADDER (frozen, port_schur_cocycle verbatim): all frame-A
zones (core.frame_a_zones()) with h <= 900, sorted by (h, kz);
consecutive rung pairs with >= 8 common port alias indices.

FROZEN PROTOCOL (2026-08-09, frozen + SHA-hashed before first
run; bars frozen before the run):

 S1  REPRODUCE THE FITTED STEPS: machinery verbatim from
     port_schur_cocycle_probe (fused heavy build, SPEC v2 IIKS
     extraction, three-deepest-common-node PSL(2,R)
     normalization, TLS Moebius fit, median chordal residual on
     non-reference nodes).  REPRODUCTION WARD (kill ->
     WARD-BROKEN): 41 steps; every per-step residual matches the
     predecessor's printed table within the print rounding
     5.001e-5; median residual matches 0.0015 within 5.001e-5;
     |alpha| < 1 on 100% of steps.  (The predecessor persists
     its numbers only at print precision; the machinery is
     verbatim, so the reproduction is bit-level in fact and the
     ward bar is the rounding radius -- documented amendment of
     the requested 1e-9 machinery ward.)

 S2  THE IDENTITY QUESTION FIRST (candidate C3, the trivial
     baseline): per step, dist(T_h, Id) = median chordal
     displacement of the fitted map on the non-reference common
     nodes, printed next to the fit residual and the raw
     identity-candidate residual median chordal(N_a, N_b).
     TYPED: CARRIER-INVARIANT iff median_h dist(T_h, Id) <= 3 x
     median_h fit-residual; else STEP-NONTRIVIAL.  DIRECT
     INVARIANCE TEST (printed regardless): the ladder-wide
     common node set J* (port alias indices present on a >= 0.90
     fraction of rungs; if |J*| < 6 the threshold steps down
     0.90 -> 0.80 -> 0.70, deterministic availability rule,
     reported); per rung, normalize the carrier by the three
     smallest indices of J* -> (0, 1, inf); m_* = the pointwise
     chordal median over rungs; print the per-rung deviation
     profile median chordal(m_h, m_*) -- if the normalized
     carrier is rung-invariant this is the stronger statement
     (a single fixed function).

 S3  SOURCE CANDIDATES (both tables are computed and printed on
     every run; each is SCORED only in its branch --
     fail-first preserved, all bars frozen):
     C1 EULER INCREMENT: the deployed atom lists are exact
        prefixes of one global table (uu = U_ALL[:ka], warded
        1e-15 per pair), so the increment is a suffix: entering
        atoms (ka_a < ka_b) or leaving atoms (ka_b < ka_a).
        Each atom u_n is one lossless one-state stage with
        a_n = e^{-u_n/2}, z_n = e^{i tau_ref u_n} (atom-level
        concretization of the entering primes' b_{a_p};
        documented amendment), stage matrix [[z, a], [a z, 1]]
        acting on the disk reflection, composed in entering
        order (ascending u_n); a leaving suffix contributes the
        inverse composition; tau_ref = (max tau of rung a)/20,
        the port center (frozen, source side).  The composed
        map is Cayley-conjugated to the upper half plane,
        real-projected by the phase-minimizing projection
        R = Re(e^{i phi} A), 2 phi = -arg(sum A_ij^2) (defect
        printed), and transported into the measured gauge as
        C = T_b R T_a^{-1}.  Compared to the fitted T_h by the
        median chordal candidate residual on the non-reference
        nodes and by the Cayley |alpha|.
     C2 CHRISTOFFEL-UVAROV: the source Weyl function of the
        tilde atom measure, m_w(z) = sum_n mu_n / (u_n - z),
        evaluated at the four FROZEN test points z = 1.0+0.7i,
        2.3+1.1i, 3.7+0.9i, 5.1+1.3i (off the real axis, source
        side only).  The unique complex Moebius map S carrying
        m_w^{(h)}(z_1..3) -> m_w^{(h')}(z_1..3) is built from
        the two three-point normalizers; THE WARD: the chordal
        deviation at z_4 must be <= 0.02, else the source Weyl
        functions are NOT Moebius-related at this step and C2
        types NOT-MOEBIUS there (honest death channel).  Where
        the ward passes, S is real-projected and transported as
        in C1 (frozen transport hypothesis: the carrier
        coordinate is the source Weyl coordinate).  Note: S is
        fitted from SOURCE data only -- never from the measured
        step.
     SCORING: in the STEP-NONTRIVIAL branch a candidate types
     SOURCE-DERIVED(Ck) iff its median candidate residual <= 3 x
     the median fit residual (one frozen construction, all
     rungs); SOURCE-PARTIAL iff <= 0.05; else SOURCE-OPEN.  C2
     additionally requires the z_4 ward to pass on > 0.50 of
     the steps, else C2-NOT-MOEBIUS.
     INVARIANT-FUNCTION IDENTIFICATION (scored in the
     CARRIER-INVARIANT branch; printed regardless): compare m_*
     against three source candidates at the deepest rung that
     carries the J* reference triple, each candidate normalized
     by the SAME three reference nodes (Moebius-invariant
     cross-ratio comparison):
       (A) the source Weyl carrier: the Cauchy transform of the
           positive-arm folded measure at the port nodes,
           sum_i w_i / (x_i - y_j);
       (B) the Euler cascade reflection angle (euler_scattering
           E4, frozen KAPPA = 1/2): theta_j = arg r_X(tau_j)/2,
           carrier pair (sin theta_j, cos theta_j), primes from
           the own sieve up to X = e^{2 alpha};
       (C) the Cauchy transform of the limit measure: the
           deepest rung's negative-arm folded measure at the
           same nodes, self-atom excluded (|x - y| <= 1e-12).
     TYPED per candidate: INVARIANT-MATCH iff median chordal
     <= 0.05; INVARIANT-PARTIAL iff <= 0.20; else open; the
     branch label is INVARIANT-MATCH(...) / INVARIANT-
     PARTIAL(...) / INVARIANT-OPEN.

 C   CONTROLS (kz 9, must fire): Epstein (lambda_eps recursion
     comb) + scramble (seed 1).  Fire channels, reported per
     control: FRAME (window unavailable or I - E_out indefinite
     or lam(C_J) > 1, as in the predecessor) or INVARIANCE-
     BREAK (frame survives but the control carrier's deviation
     from m_* exceeds 10 x the truth ladder's median deviation).
     Silent on both channels -> CONTROL-DEAD.

 W   PIPELINE WARDS (predecessor verbatim): W1 >= 30 rungs; W2
     [Y, D_P] rank 2 on every rung (s3/s1 <= 1e-10); W4 >= 30
     measured steps.

KILLS: K1 pipeline ward breaks -> PIPELINE-BROKEN; KW the S1
reproduction ward breaks -> WARD-BROKEN; K3 controls silent ->
CONTROL-DEAD.

VERDICT (frozen enum): MOEBIUSSOURCE-MEASURED with typed
sublabels CARRIER-INVARIANT / STEP-NONTRIVIAL (S2) and, per
branch, SOURCE-DERIVED(C1/C2) / SOURCE-PARTIAL / SOURCE-OPEN /
C2-NOT-MOEBIUS or INVARIANT-MATCH(...) / INVARIANT-PARTIAL(...)
/ INVARIANT-OPEN (S3); else PIPELINE-BROKEN / WARD-BROKEN /
CONTROL-DEAD.

SPEC v2 AMENDMENTS (documented before the run; fail-first
preserved): (i) the S1 reproduction ward is the full 41-entry
printed-table match at rounding radius 5.001e-5 (the
predecessor's full-precision values are not persisted); (ii) the
C1 stages are per-ATOM (each entering prime power p^k is its own
one-state stage with a = p^{-k/2} = e^{-u/2}) -- the prompt's
"entering primes" concretized at the atom level, which handles
new powers of old primes uniformly; (iii) rung_all is extended
with source bookkeeping fields (uu, mm, xs, ws, ys, vs, taup,
tau_max) -- bookkeeping only, physics verbatim; (iv) both
candidate tables print on every run and are scored only in their
branch.

NO RH claim -- a source-derived (or rung-invariant) normalized
carrier is a numerical measurement on compressed truncations,
not a theorem about zeros.

FIREWALL: no zeros, no prime oracles (AST scan; banned ids
zetazero / nzeros / primerange / isprime / primepi / nextprime /
prevprime); own boolean Eratosthenes sieve for candidate (B)
only (allowed, v882 precedent); v563 READ-ONLY; RNG only inside
the declared scramble control; stdout only.  No marker moves.

Sources (read-only): v563_paper2_readouts; measured-step
machinery verbatim from port_schur_cocycle_probe.py
(PRIME.PORT.SCHURSTEP.01); cascade reflection + KAPPA = 1/2 from
euler_scattering_source_probe.py (PRIME.EULER.SCATTER.01);
port_loewner_identity_probe (static identification dead,
context).  IIKS = Its-Izergin-Korepin-Slavnov.

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/moebius_source_step_probe.py
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

H_DEEP_MAX = 900
JWIN = tuple(range(2, 25, 2))
MIN_RUNGS = 30
MIN_PAIRS = 30
MIN_COMMON_J = 8
RANK_BAR = 1e-10
REF_SEP_MIN = 1e-6
CTRL_KZ = 9

# S1 reproduction ward: the predecessor's printed per-step residual
# table (41 steps, print precision 1e-4) and headline stats.
REF_RES = (0.0011, 0.0024, 0.0150, 0.0035, 0.0097, 0.0102, 0.0015,
           0.0028, 0.0022, 0.0012, 0.0008, 0.0007, 0.0011, 0.0016,
           0.0006, 0.0005, 0.0003, 0.0001, 0.0013, 0.0005, 0.0002,
           0.0036, 0.0122, 0.0010, 0.0002, 0.0001, 0.0012, 0.0005,
           0.0017, 0.0032, 0.0019, 0.0005, 0.0077, 0.0015, 0.0024,
           0.0215, 0.0118, 0.0063, 0.0011, 0.0043, 0.0005)
REF_N_STEPS = 41
REF_MED_RES = 0.0015
ROUND_TOL = 5.001e-5

INV_FACTOR = 3.0            # S2: CARRIER-INVARIANT bar (x med fit res)
SRC_FACTOR = 3.0            # S3: SOURCE-DERIVED bar   (x med fit res)
SRC_PART_BAR = 0.05
Z_TEST = (1.0 + 0.7j, 2.3 + 1.1j, 3.7 + 0.9j, 5.1 + 1.3j)
C2_WARD_BAR = 0.02
C2_MIN_PASS_FRAC = 0.50
JSTAR_FRACS = (0.90, 0.80, 0.70)
MIN_JSTAR = 6
INV_MATCH_BAR = 0.05
INV_PART_BAR = 0.20
KAPPA = 0.5                 # euler_scattering E4, frozen
CTRL_INV_FACTOR = 10.0
PREFIX_WARD = 1e-15
BANNED_IDS = ("zetazero", "nzeros", "primerange", "isprime",
              "primepi", "nextprime", "prevprime")

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


# --------- pipeline, verbatim from port_schur_cocycle_probe
def grid_density(c):
    c = np.asarray(c, float)
    a = np.concatenate([c, c[-2:0:-1]])
    d = np.fft.fft(a)
    assert float(np.max(np.abs(d.imag))) <= 1e-9 * max(
        1.0, float(np.max(np.abs(d.real))))
    return d.real


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
    return dict(d=d, L=2 * M - 2, D=D, alpha=alpha, h=h,
                uu=uu, mm=mm, M=M)


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


def antisym_generators(C):
    """Canonical (f, g) with C = f g^T - g f^T (SPEC v2 extraction,
    verbatim)."""
    U, sv, _Vh = np.linalg.svd(C)
    s1 = sv[0]
    f = math.sqrt(s1) * U[:, 0]
    g = math.sqrt(s1) * U[:, 1]
    Ct = np.outer(f, g) - np.outer(g, f)
    if np.linalg.norm(Ct + C) < np.linalg.norm(Ct - C):
        g = -g
    return f, g, sv


def gauge_fix(f, g, jp):
    """FROZEN GAUGE (lax2 verbatim; the normalization quotients it
    out exactly)."""
    m0 = int(np.argmin(jp))
    r = math.hypot(f[m0], g[m0])
    c, s = f[m0] / r, g[m0] / r
    return c * f + s * g, -s * f + c * g


def rung_all(kz, **kw):
    """One heavy build per rung (port_schur_cocycle verbatim), plus
    source bookkeeping fields (amendment iii)."""
    b = build_rung(kz, **kw)
    h, L, D = b["h"], b["L"], b["D"]
    if h > H_DEEP_MAX:
        return "TOO-DEEP"
    xs, ws, _ = folded_measure(b["d"], L, +1.0)
    ys, vs, uf_n = folded_measure(b["d"], L, -1.0)
    al, be, m0, steps = lanczos_chain(xs, ws, h + 1)
    if steps < h + 1 or np.any(be <= 0):
        return None
    Pn = eval_chain(al, be, m0, ys, h)
    E = np.sqrt(vs)[:, None] * (Pn @ Pn.T) * np.sqrt(vs)[None, :]
    E = 0.5 * (E + E.T)
    out = dict(kz=kz, h=h, alpha=b["alpha"], M=b["M"], D=D,
               uu=b["uu"], mm=b["mm"], xs=xs, ws=ws, ys=ys, vs=vs,
               lamE=float(np.linalg.eigvalsh(E)[-1]))
    # ---- window compression (controls' frame channel, verbatim)
    idx = {int(j): k for k, j in enumerate(uf_n)}
    jav = [j for j in JWIN if j in idx]
    if len(jav) >= MIN_COMMON_J:
        iw = [idx[j] for j in jav]
        io = [k for k in range(E.shape[0]) if k not in set(iw)]
        Eo = E[np.ix_(io, io)]
        IO = np.eye(len(io)) - Eo
        CJ = (E[np.ix_(iw, iw)]
              + E[np.ix_(iw, io)] @ np.linalg.solve(
                  IO, E[np.ix_(io, iw)]))
        CJ = 0.5 * (CJ + CJ.T)
        out["lamO"] = float(np.linalg.eigvalsh(Eo)[-1])
        out["lamC"] = float(np.linalg.eigvalsh(CJ)[-1])
    # ---- dressed port + IIKS generators (verbatim)
    tau_m = (2.0 * math.pi * uf_n / L) / D
    port = tau_m <= float(np.max(tau_m)) / 10.0
    ip, ib = np.where(port)[0], np.where(~port)[0]
    if len(ip) >= 4 and len(ib) >= 1:
        P = E[np.ix_(ip, ip)]
        X = E[np.ix_(ip, ib)]
        R = E[np.ix_(ib, ib)]
        IR = np.eye(len(ib)) - R
        DP = P + X @ np.linalg.solve(IR, X.T)
        DP = 0.5 * (DP + DP.T)
        Y = np.diag(ys[ip])
        C = Y @ DP - DP @ Y
        f, g, sv = antisym_generators(C)
        f, g = gauge_fix(f, g, uf_n[ip])
        out["f"], out["g"] = f, g
        out["jp"], out["yp"] = uf_n[ip], ys[ip]
        out["taup"] = tau_m[ip]
        out["tau_max"] = float(np.max(tau_m))
        out["rk"] = float(sv[2] / sv[0]) if len(sv) > 2 else 0.0
    return out


# ------------------------------------------- homogeneous RP^1 machinery
def unit_pairs(g, f):
    P = np.stack([np.asarray(g, float), np.asarray(f, float)],
                 axis=1)
    return P / np.linalg.norm(P, axis=1)[:, None]


def chordal(P, Q):
    """Chordal distance on RP^1 (or CP^1) between unit pair rows."""
    return np.abs(P[:, 0] * Q[:, 1] - P[:, 1] * Q[:, 0])


def norm_map(p0, p1, p2):
    """The unique PSL(2, R) map sending p0 -> 0, p1 -> 1,
    p2 -> infinity (homogeneous); None if degenerate (verbatim)."""
    M = np.stack([p2, p0], axis=1)
    if abs(float(np.linalg.det(M))) < 1e-12:
        return None
    T0 = np.linalg.inv(M)
    s, t = T0 @ p1
    if abs(s) < 1e-10 or abs(t) < 1e-10:
        return None
    return np.diag([1.0 / s, 1.0 / t]) @ T0


def norm_map_c(p0, p1, p2):
    """Complex three-point normalizer (CP^1), for the C2 source
    Weyl points only."""
    M = np.stack([p2, p0], axis=1).astype(complex)
    if abs(np.linalg.det(M)) < 1e-12:
        return None
    T0 = np.linalg.inv(M)
    s, t = T0 @ p1
    if abs(s) < 1e-10 or abs(t) < 1e-10:
        return None
    return np.diag([1.0 / s, 1.0 / t]) @ T0


def apply_hom(T, P):
    Q = (T @ P.T).T
    n = np.linalg.norm(Q, axis=1)
    n[n < 1e-300] = 1.0
    return Q / n[:, None]


def moebius_fit(P, Q):
    """TLS Moebius fit (verbatim)."""
    rows = np.stack([P[:, 0] * Q[:, 1], P[:, 1] * Q[:, 1],
                     -P[:, 0] * Q[:, 0], -P[:, 1] * Q[:, 0]],
                    axis=1)
    _u, _s, Vh = np.linalg.svd(rows)
    a, b, c, d = Vh[-1]
    T = np.array([[a, b], [c, d]])
    return T, chordal(apply_hom(T, P), Q)


def cayley_alpha(T):
    den = T[1, 0] * 1j + T[1, 1]
    if abs(den) < 1e-300:
        return float("inf")
    z = (T[0, 0] * 1j + T[0, 1]) / den
    return abs((z - 1j) / (z + 1j))


def quart(v):
    q = np.percentile(np.asarray(v, float), [25, 50, 75])
    return "q25 %.4f  med %.4f  q75 %.4f" % tuple(q)


def eps_comb(kz):
    rr = core.build_window(kz)
    N_E = int(math.floor(math.exp(2.0 * rr["alpha"]))) + 1
    lamE_ = lambda_eps(N_E)
    nn = np.nonzero(np.abs(lamE_) > 1e-12)[0]
    return (np.log(nn.astype(float)),
            2.0 * lamE_[nn] / np.sqrt(nn.astype(float)))


# ------------------------------------------- source-candidate machinery
def sieve_primes(N):
    """Own boolean Eratosthenes sieve, no oracle imports (allowed,
    v882 precedent; candidate (B) only)."""
    if N < 2:
        return []
    s = np.ones(N + 1, dtype=bool)
    s[:2] = False
    for i in range(2, int(math.isqrt(N)) + 1):
        if s[i]:
            s[i * i::i] = False
    return [int(p) for p in np.nonzero(s)[0]]


def cascade_reflection(tau, primes_desc):
    """Moebius composition of the U_p stages, load 0, smallest prime
    outermost (euler_scattering E4, verbatim)."""
    tau = np.asarray(tau, float)
    rho = np.zeros(len(tau), dtype=complex)
    for p in primes_desc:
        a = 1.0 / math.sqrt(p)
        z = np.exp(1j * tau * math.log(p))
        rho = (a + z * rho) / (1.0 + a * z * rho)
    return rho


def stage_matrix(u, tau_ref):
    """One entering atom = one lossless one-state stage on the disk
    reflection: rho -> (a + z rho)/(1 + a z rho), a = e^{-u/2},
    z = e^{i tau_ref u}."""
    a = math.exp(-0.5 * u)
    z = np.exp(1j * tau_ref * u)
    return np.array([[z, a], [a * z, 1.0]], dtype=complex)


K_HD = np.array([[-1.0, 1j], [1.0, 1j]], dtype=complex)  # H -> D
K_DH = np.linalg.inv(K_HD)                               # D -> H


def real_project(A):
    """Phase-minimizing real projection of a complex 2x2 Moebius
    representative: R = Re(e^{i phi} A), 2 phi = -arg(sum A_ij^2);
    returns (R, defect)."""
    s = complex(np.sum(A * A))
    phi = -0.5 * np.angle(s) if abs(s) > 1e-300 else 0.0
    B = A * np.exp(1j * phi)
    nA = float(np.linalg.norm(A))
    if nA < 1e-300:
        return None, 1.0
    defect = float(np.linalg.norm(B.imag)) / nA
    R = np.asarray(B.real, float)
    if np.linalg.norm(R) < 1e-12 * nA:
        return None, 1.0
    return R, defect


def euler_increment_map(ra, rb, tau_ref):
    """C1: the suffix increment as a composed one-state cascade
    (entering ascending u; leaving suffix -> inverse composition).
    Returns (W_complex, n_signed) or (None, reason)."""
    ka, kb = len(ra["uu"]), len(rb["uu"])
    n = min(ka, kb)
    if (ka and kb and float(np.max(np.abs(
            ra["uu"][:n] - rb["uu"][:n]))) > PREFIX_WARD):
        return None, "PREFIX-BROKEN"
    W = np.eye(2, dtype=complex)
    if kb > ka:
        for u in rb["uu"][ka:]:
            W = stage_matrix(float(u), tau_ref) @ W
        return W, kb - ka
    if ka > kb:
        for u in ra["uu"][kb:]:
            W = stage_matrix(float(u), tau_ref) @ W
        return np.linalg.inv(W), kb - ka
    return W, 0


def weyl_source(uu, mm, z):
    """The source Weyl function of the tilde atom measure at complex
    z: sum_n mu_n / (u_n - z)."""
    return complex(np.sum(np.asarray(mm) / (np.asarray(uu) - z)))


def unit_pairs_c(vals):
    P = np.stack([np.asarray(vals, complex),
                  np.ones(len(vals), complex)], axis=1)
    return P / np.linalg.norm(P, axis=1)[:, None]


def chordal_median(pairs_list):
    """The chordal median on RP^1 of a list of unit pairs: the
    sample minimizing the summed chordal distance to all others."""
    P = np.stack(pairs_list)
    D = np.abs(P[:, None, 0] * P[None, :, 1]
               - P[:, None, 1] * P[None, :, 0])
    return P[int(np.argmin(np.sum(D, axis=1)))]


def main():
    section("PRIME.PORT.MOEBIUS.SOURCE.01 -- is the per-rung Moebius "
            "step source-derivable? (EXPLORATION ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s"
          % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
    print("    NO RH claim; own sieve (candidate B only); no marker "
          "moves.")
    print("\nS0 -- firewall")
    check("S0.1 AST firewall clean", not ast_scan(BANNED_IDS))

    # ------------------------------------------------------------ W
    section("W -- build the ladder (all frame-A zones, h <= %d; "
            "machinery verbatim)" % H_DEEP_MAX)
    rungs = []
    rk_max = 0.0
    for kz in core.frame_a_zones():
        r = rung_all(kz)
        if not isinstance(r, dict):
            continue
        rk_max = max(rk_max, r.get("rk", 1.0))
        rungs.append(r)
    rungs.sort(key=lambda r: (r["h"], r["kz"]))
    print("    %d rungs, h %d .. %d; worst [Y,D_P] s3/s1 %.1e"
          % (len(rungs), rungs[0]["h"], rungs[-1]["h"], rk_max))
    check("W1 >= %d rungs built" % MIN_RUNGS,
          len(rungs) >= MIN_RUNGS, "%d rungs" % len(rungs),
          kill="K1")
    check("W2 rank-2 exact on every rung (max s3/s1 %.1e <= %.0e)"
          % (rk_max, RANK_BAR), rk_max <= RANK_BAR, kill="K1")

    # ------------------------------------------------------------ S1
    section("S1 -- reproduce the fitted steps (port_schur_cocycle "
            "verbatim; reproduction ward %.1e)" % ROUND_TOL)
    steps = []
    n_skip_j = n_skip_ref = 0
    for ra, rb in zip(rungs[:-1], rungs[1:]):
        com, ia, ib = np.intersect1d(ra.get("jp", []),
                                     rb.get("jp", []),
                                     return_indices=True)
        if len(com) < MIN_COMMON_J:
            n_skip_j += 1
            continue
        Pa = unit_pairs(ra["g"][ia], ra["f"][ia])
        Pb = unit_pairs(rb["g"][ib], rb["f"][ib])
        order = np.argsort(com)
        i0, i1, i2 = order[0], order[1], order[2]
        seps = [chordal(Pa[[u]], Pa[[v]])[0]
                for u, v in ((i0, i1), (i0, i2), (i1, i2))] \
            + [chordal(Pb[[u]], Pb[[v]])[0]
               for u, v in ((i0, i1), (i0, i2), (i1, i2))]
        Ta = norm_map(Pa[i0], Pa[i1], Pa[i2])
        Tb = norm_map(Pb[i0], Pb[i1], Pb[i2])
        if min(seps) <= REF_SEP_MIN or Ta is None or Tb is None:
            n_skip_ref += 1
            continue
        Na, Nb = apply_hom(Ta, Pa), apply_hom(Tb, Pb)
        T, res = moebius_fit(Na, Nb)
        keep = np.ones(len(com), dtype=bool)
        keep[[i0, i1, i2]] = False
        steps.append(dict(ra=ra, rb=rb, Ta=Ta, Tb=Tb, T=T,
                          Na=Na, Nb=Nb, keep=keep,
                          res=float(np.median(res[keep])),
                          alpha=cayley_alpha(T)))
    check("W4 >= %d steps measured (typed skips: %d common-j, %d "
          "degenerate-reference)" % (MIN_PAIRS, n_skip_j,
                                     n_skip_ref),
          len(steps) >= MIN_PAIRS, "%d steps" % len(steps),
          kill="K1")
    res_v = np.array([s["res"] for s in steps])
    al_v = np.array([s["alpha"] for s in steps])
    med_res = float(np.median(res_v)) if len(res_v) else 1.0
    frac_al = float(np.mean(al_v < 1.0)) if len(al_v) else 0.0
    tab_ok = (len(steps) == REF_N_STEPS
              and float(np.max(np.abs(
                  res_v - np.array(REF_RES)))) <= ROUND_TOL)
    tab_dev = (float(np.max(np.abs(res_v - np.array(REF_RES))))
               if len(res_v) == REF_N_STEPS else float("inf"))
    print("    %d steps; residual ladder: %s" % (len(steps),
                                                 quart(res_v)))
    check("S1.1 REPRODUCTION WARD: %d steps == %d; per-step "
          "residual table max dev %.1e <= %.1e; |median - %.4f| "
          "<= %.1e; |alpha| < 1 on %.2f == 1.00"
          % (len(steps), REF_N_STEPS, tab_dev, ROUND_TOL,
             REF_MED_RES, ROUND_TOL, frac_al),
          tab_ok and abs(med_res - REF_MED_RES) <= ROUND_TOL
          and frac_al == 1.0, kill="KW")

    # ------------------------------------------------------------ S2
    section("S2 -- THE IDENTITY QUESTION (candidate C3 first)")
    print("    per step: dist(T, Id) = median chordal displacement "
          "of the fitted map on")
    print("    non-reference nodes; id-res = median chordal(N_a, "
          "N_b) (identity as candidate).")
    for s in steps:
        disp = chordal(apply_hom(s["T"], s["Na"]), s["Na"])
        s["dist_id"] = float(np.median(disp[s["keep"]]))
        s["id_res"] = float(np.median(
            chordal(s["Na"], s["Nb"])[s["keep"]]))
        print("    h %3d->%3d  fit res %.4f  dist(T,Id) %.4f  "
              "id-res %.4f  |alpha| %.3f"
              % (s["ra"]["h"], s["rb"]["h"], s["res"],
                 s["dist_id"], s["id_res"], s["alpha"]))
    did_v = np.array([s["dist_id"] for s in steps])
    idr_v = np.array([s["id_res"] for s in steps])
    med_did = float(np.median(did_v))
    inv_bar = INV_FACTOR * med_res
    s2_label = ("CARRIER-INVARIANT" if med_did <= inv_bar
                else "STEP-NONTRIVIAL")
    print("    dist(T,Id) ladder: %s" % quart(did_v))
    print("    id-res     ladder: %s" % quart(idr_v))
    print("    TYPED: median dist(T,Id) %.4f vs bar %.4f "
          "(= %.0f x median fit res %.4f) -> %s"
          % (med_did, inv_bar, INV_FACTOR, med_res, s2_label))
    check("S2.1 typed: %s (the identity question, answered first)"
          % s2_label, True)

    # ---- direct invariance test: J*, m_*, per-rung deviation
    print("\n    DIRECT INVARIANCE TEST (printed regardless):")
    all_jp = [set(int(j) for j in r.get("jp", [])) for r in rungs]
    jstar, used_frac = [], None
    for fr in JSTAR_FRACS:
        cand = sorted(j for j in set().union(*all_jp)
                      if sum(j in s for s in all_jp)
                      >= fr * len(rungs))
        if len(cand) >= MIN_JSTAR:
            jstar, used_frac = cand, fr
            break
    check("S2.2 ladder-wide node set J* built (|J*| %d >= %d at "
          "presence >= %.2f)" % (len(jstar), MIN_JSTAR,
                                 used_frac or 0.0),
          len(jstar) >= MIN_JSTAR, kill="K1")
    if len(jstar) < MIN_JSTAR:
        return finish(None, None, None)
    refs = jstar[:3]
    print("    J* = %s (presence >= %.2f); reference triple %s "
          "-> (0, 1, inf)" % (jstar, used_frac, refs))
    norm_carriers = {}          # rung index -> {j: unit pair}
    n_skip_inv = 0
    for irx, r in enumerate(rungs):
        jp = list(r.get("jp", []))
        if not all(j in jp for j in refs):
            n_skip_inv += 1
            continue
        pos = {int(j): k for k, j in enumerate(jp)}
        P = unit_pairs(r["g"], r["f"])
        Tn = norm_map(P[pos[refs[0]]], P[pos[refs[1]]],
                      P[pos[refs[2]]])
        if Tn is None:
            n_skip_inv += 1
            continue
        N = apply_hom(Tn, P)
        norm_carriers[irx] = {int(j): N[pos[j]] for j in jstar
                              if j in pos}
    mstar = {}
    for j in jstar:
        vals = [nc[j] for nc in norm_carriers.values() if j in nc]
        if len(vals) >= 3:
            mstar[j] = chordal_median(vals)
    devs = []
    print("    per-rung deviation from m_* (median chordal on "
          "J* minus refs; %d typed skips):" % n_skip_inv)
    for irx in sorted(norm_carriers):
        nc = norm_carriers[irx]
        dd = [float(chordal(nc[j][None, :], mstar[j][None, :])[0])
              for j in jstar[3:] if j in nc and j in mstar]
        if not dd:
            continue
        d = float(np.median(dd))
        devs.append(d)
        print("      h %4d kz %3d  dev %.4f  (%d nodes)"
              % (rungs[irx]["h"], rungs[irx]["kz"], d, len(dd)))
    med_dev = float(np.median(devs)) if devs else float("inf")
    print("    ladder deviation profile: %s" % quart(devs))
    check("S2.3 direct invariance profile computed (median rung "
          "deviation from m_* = %.4f)" % med_dev, bool(devs),
          kill="K1")

    # ------------------------------------------------------------ S3
    section("S3 -- source candidates C1 (Euler increment) and C2 "
            "(Christoffel-Uvarov)")
    print("    both tables computed on every run; SCORED only in "
          "their branch (S2 typed %s)." % s2_label)
    print("    step            dn    C1 res  (dfct)   C2 res  "
          "(dfct)   fit res  C2-ward")
    c1_res, c2_res = [], []
    c1_al, c2_al = [], []
    n_c2_pass = n_c2_fail = n_c2_deg = 0
    n_prefix_broken = 0
    for s in steps:
        ra, rb = s["ra"], s["rb"]
        # ---- C1
        tau_ref = ra["tau_max"] / 20.0
        W, ninc = euler_increment_map(ra, rb, tau_ref)
        c1_txt = "      -    "
        if W is None:
            n_prefix_broken += 1
            ninc_txt = "PFX!"
        else:
            ninc_txt = "%+5d" % ninc
            AH = K_DH @ W @ K_HD
            R, dfct1 = real_project(AH)
            if R is not None:
                Cn = s["Tb"] @ R @ np.linalg.inv(s["Ta"])
                rc = float(np.median(chordal(
                    apply_hom(Cn, s["Na"]),
                    s["Nb"])[s["keep"]]))
                c1_res.append(rc)
                c1_al.append(cayley_alpha(Cn))
                c1_txt = "%.4f (%.2f)" % (rc, dfct1)
        # ---- C2
        c2_txt = "      -    "
        ward_txt = "-"
        ma = [weyl_source(ra["uu"], ra["mm"], z) for z in Z_TEST]
        mb = [weyl_source(rb["uu"], rb["mm"], z) for z in Z_TEST]
        pa = unit_pairs_c(ma)
        pb = unit_pairs_c(mb)
        Ga = norm_map_c(pa[0], pa[1], pa[2])
        Gb = norm_map_c(pb[0], pb[1], pb[2])
        if Ga is None or Gb is None:
            n_c2_deg += 1
            ward_txt = "DEG"
        else:
            S = np.linalg.inv(Gb) @ Ga
            w4 = float(chordal(apply_hom(S, pa[[3]]), pb[[3]])[0])
            if w4 > C2_WARD_BAR:
                n_c2_fail += 1
                ward_txt = "FIRE %.3f" % w4
            else:
                n_c2_pass += 1
                ward_txt = "ok %.4f" % w4
                R2, dfct2 = real_project(S)
                if R2 is not None:
                    Cn2 = s["Tb"] @ R2 @ np.linalg.inv(s["Ta"])
                    rc2 = float(np.median(chordal(
                        apply_hom(Cn2, s["Na"]),
                        s["Nb"])[s["keep"]]))
                    c2_res.append(rc2)
                    c2_al.append(cayley_alpha(Cn2))
                    c2_txt = "%.4f (%.2f)" % (rc2, dfct2)
        print("    h %3d->%3d  %s  %s  %s  %.4f   %s"
              % (ra["h"], rb["h"], ninc_txt, c1_txt, c2_txt,
                 s["res"], ward_txt))
    check("S3.0 prefix ward: deployed atom lists are exact prefixes "
          "on every pair (%d broken)" % n_prefix_broken,
          n_prefix_broken == 0, kill="K1")
    src_bar = SRC_FACTOR * med_res
    med_c1 = float(np.median(c1_res)) if c1_res else float("inf")
    med_c2 = float(np.median(c2_res)) if c2_res else float("inf")
    c2_frac = n_c2_pass / max(n_c2_pass + n_c2_fail + n_c2_deg, 1)
    print("\n    C1 candidate residual ladder: %s"
          % (quart(c1_res) if c1_res else "none"))
    print("    C2 z4-ward: pass %d / fire %d / degenerate %d "
          "(pass frac %.2f vs %.2f); residual ladder: %s"
          % (n_c2_pass, n_c2_fail, n_c2_deg, c2_frac,
             C2_MIN_PASS_FRAC,
             quart(c2_res) if c2_res else "none"))
    print("    scalar Schur compare: measured |alpha| med %.4f | "
          "C1 med %s | C2 med %s"
          % (float(np.median(al_v)),
             "%.4f" % float(np.median(c1_al)) if c1_al else "-",
             "%.4f" % float(np.median(c2_al)) if c2_al else "-"))

    labels = []
    if med_c1 <= src_bar:
        labels.append("SOURCE-DERIVED(C1)")
    if c2_frac > C2_MIN_PASS_FRAC and med_c2 <= src_bar:
        labels.append("SOURCE-DERIVED(C2)")
    if c2_frac <= C2_MIN_PASS_FRAC:
        labels.append("C2-NOT-MOEBIUS")
    if not any(x.startswith("SOURCE-DERIVED") for x in labels):
        best = min(med_c1, med_c2)
        labels.append("SOURCE-PARTIAL" if best <= SRC_PART_BAR
                      else "SOURCE-OPEN")
    nontriv_label = " + ".join(labels)
    print("    NONTRIVIAL-branch typing (bars: derived <= %.4f = "
          "%.0f x med fit res; partial <= %.2f): %s"
          % (src_bar, SRC_FACTOR, SRC_PART_BAR, nontriv_label))

    # ---- invariant-function identification (candidates A / B / C)
    print("\n    INVARIANT-FUNCTION IDENTIFICATION (scored in the "
          "CARRIER-INVARIANT branch):")
    ref_irx = max((irx for irx in norm_carriers),
                  key=lambda irx: rungs[irx]["h"], default=None)
    inv_meds = {}
    if ref_irx is not None:
        rr = rungs[ref_irx]
        jp = list(rr["jp"])
        pos = {int(j): k for k, j in enumerate(jp)}
        nodes = [j for j in jstar if j in pos and j in mstar]
        print("    reference rung h %d kz %d; %d J* nodes"
              % (rr["h"], rr["kz"], len(nodes)))
        yv = np.array([rr["yp"][pos[j]] for j in nodes])
        tv = np.array([rr["taup"][pos[j]] for j in nodes])
        # (A) source Weyl carrier: Cauchy transform of positive arm
        vA = np.array([float(np.sum(rr["ws"] / (rr["xs"] - y)))
                       for y in yv])
        # (B) Euler cascade reflection angle (KAPPA = 1/2 frozen)
        X = math.exp(2.0 * rr["alpha"])
        prim = sorted(sieve_primes(int(math.floor(X)) + 1),
                      reverse=True)
        th = KAPPA * np.angle(cascade_reflection(tv, prim))
        PB = np.stack([np.sin(th), np.cos(th)], axis=1)
        # (C) Cauchy transform of the limit (deepest) measure
        deep = rungs[max(range(len(rungs)),
                         key=lambda i: rungs[i]["h"])]
        vC = []
        for y in yv:
            d = deep["ys"] - y
            m = np.abs(d) > 1e-12
            vC.append(float(np.sum(deep["vs"][m] / d[m])))
        vC = np.array(vC)
        cand_pairs = {"A source-Weyl-carrier": unit_pairs(
                          vA, np.ones(len(vA))),
                      "B euler-cascade-angle": PB,
                      "C limit-measure-Cauchy": unit_pairs(
                          vC, np.ones(len(vC)))}
        i0, i1, i2 = (nodes.index(refs[0]), nodes.index(refs[1]),
                      nodes.index(refs[2]))
        Mstar = np.stack([mstar[j] for j in nodes])
        for nm, P in cand_pairs.items():
            Tn = norm_map(P[i0].astype(float),
                          P[i1].astype(float),
                          P[i2].astype(float))
            if Tn is None:
                print("      %-24s: reference triple degenerate "
                      "-> open" % nm)
                inv_meds[nm] = float("inf")
                continue
            N = apply_hom(Tn, P)
            dd = [float(chordal(N[[k]], Mstar[[k]])[0])
                  for k in range(len(nodes))
                  if nodes[k] not in refs]
            inv_meds[nm] = float(np.median(dd))
            print("      %-24s: median chordal vs m_* = %.4f "
                  "(match <= %.2f, partial <= %.2f)"
                  % (nm, inv_meds[nm], INV_MATCH_BAR,
                     INV_PART_BAR))
    matches = [n.split()[0] for n, v in inv_meds.items()
               if v <= INV_MATCH_BAR]
    partials = [n.split()[0] for n, v in inv_meds.items()
                if INV_MATCH_BAR < v <= INV_PART_BAR]
    if matches:
        inv_label = "INVARIANT-MATCH(%s)" % ",".join(matches)
    elif partials:
        inv_label = "INVARIANT-PARTIAL(%s)" % ",".join(partials)
    else:
        inv_label = "INVARIANT-OPEN"
    print("    INVARIANT-branch typing: %s" % inv_label)
    s3_label = (inv_label if s2_label == "CARRIER-INVARIANT"
                else nontriv_label)
    check("S3.1 typed (%s branch scored): %s"
          % (s2_label, s3_label), True)

    # ------------------------------------------------------------ C
    section("C -- controls (kz %d, must fire; channels reported)"
            % CTRL_KZ)
    ok = True
    for nmc, kw in (("Epstein", dict(comb=eps_comb(CTRL_KZ))),
                    ("scramble", dict(scramble_seed=1))):
        rc = rung_all(CTRL_KZ, **kw)
        if not isinstance(rc, dict):
            print("    %-8s: rung not built (%r) -> fires via "
                  "FRAME" % (nmc, rc))
            continue
        frame_dead = ("lamC" not in rc or rc["lamO"] > 1.0
                      or rc["lamC"] > 1.0)
        if frame_dead:
            why = ("window unavailable" if "lamC" not in rc else
                   "lam(out) %.3e" % rc["lamO"]
                   if rc["lamO"] > 1.0 else
                   "lam(C_J) %.3e" % rc["lamC"])
            print("    %-8s: fires via FRAME (%s)" % (nmc, why))
            continue
        # frame survived: the invariance channel must fire instead
        fired = False
        if "jp" in rc and all(j in list(rc["jp"]) for j in refs):
            pos = {int(j): k for k, j in enumerate(rc["jp"])}
            P = unit_pairs(rc["g"], rc["f"])
            Tn = norm_map(P[pos[refs[0]]], P[pos[refs[1]]],
                          P[pos[refs[2]]])
            if Tn is not None:
                N = apply_hom(Tn, P)
                dd = [float(chordal(N[[pos[j]]],
                                    mstar[j][None, :])[0])
                      for j in jstar[3:]
                      if j in pos and j in mstar]
                if dd:
                    dev_c = float(np.median(dd))
                    fired = dev_c > CTRL_INV_FACTOR * med_dev
                    print("    %-8s: frame ALIVE; carrier dev vs "
                          "m_* %.4f vs bar %.4f -> %s via "
                          "INVARIANCE-BREAK"
                          % (nmc, dev_c,
                             CTRL_INV_FACTOR * med_dev,
                             "fires" if fired else "SILENT"))
        if not fired and "jp" not in rc:
            print("    %-8s: frame alive but carrier unavailable "
                  "-> fires via FRAME" % nmc)
            fired = True
        ok &= fired
    check("C1 CONTROLS FIRE (frame death or invariance break on "
          "both controls)", ok, kill="K3")

    return finish(s2_label, s3_label,
                  dict(med_res=med_res, med_did=med_did,
                       med_dev=med_dev, med_c1=med_c1,
                       med_c2=med_c2, inv_meds=inv_meds))


def finish(s2_label, s3_label, stats):
    section("V -- FROZEN VERDICT")
    n_pass = sum(1 for _n, okk in CHECKS if okk)
    n_tot = len(CHECKS)
    if KILLS:
        VERDICT = {"K1": "PIPELINE-BROKEN",
                   "KW": "WARD-BROKEN",
                   "K3": "CONTROL-DEAD"}[KILLS[0]]
        print("\n  VERDICT: %s" % VERDICT)
    else:
        VERDICT = "MOEBIUSSOURCE-MEASURED / %s / %s" % (s2_label,
                                                        s3_label)
        print("\n  VERDICT: %s" % VERDICT)
        print("  (med fit res %.4f; med dist(T,Id) %.4f; med "
              "invariance dev %.4f; C1 med %.4f; C2 med %s)"
              % (stats["med_res"], stats["med_did"],
                 stats["med_dev"], stats["med_c1"],
                 ("%.4f" % stats["med_c2"])
                 if stats["med_c2"] < float("inf") else "n/a"))
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed"
          % (time.time() - T0, n_tot, n_tot - n_pass))
    return 0 if n_pass == n_tot else 1


if __name__ == "__main__":
    raise SystemExit(main())
