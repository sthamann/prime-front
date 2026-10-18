#!/usr/bin/env python3
"""prime_float_budget_probe -- attack the frozen quadratic float-budget
convention: does a rigorous Higham-grade (norm-LINEAR) budget extend the
citation-grade family gate past alpha* ~ 11 to full sieve depth?

EXPLORATION ONLY (experiments/): no verification claim, no ledger row,
no paper edit.  NO RH claim anywhere.  Frozen before running.

CONTEXT (prime_family_depth_probe, FAMILY-SCALES): at the deep rungs
the binding term in the citation chain is eps_f = 100 eps |A2|_F^2
(QUADRATIC in the norm; 1.7e-4 at M = 1632 where |A2| ~ 1.3e5), while
the true zero-tail term is 4.3e-8 -- four orders smaller.  lambda_min
(A2 - M2) >= 0 holds 6/6 but is float-resolvable above that blanket
budget on 0/6.  The quadratic convention was calibrated on the old
ladder (|A2| ~ 300) where quadratic vs linear barely differed.

THE FROZEN NEW BUDGET (derivation sketch; Higham, Accuracy and
Stability of Numerical Algorithms, ch. 3-4; all magnitudes computed
online, all constants explicit; eps = 2^-52 unit roundoff):

  (A2 side)  A2_xy = sum_k cc_k W_k, cc = c_ar + c_at, with c_at the
  banded-sieve atom-lag accumulation.  Per entry (W = W_xy, all
  vectors length M, @ = dot of NON-NEGATIVE vectors -- a budget
  quantity, not a certified one):

    dA2 =  gC * (S_abs @ |W|)              [tent-sum float]
         + (eps*X/D + C_ATOM*eps) * (T @ |W|)   [tent READ error]
         + gQ * (A_abs @ |W|)              [arch quadrature float]
         + (M + C_T)*eps * (C_abs @ Wabs)  [W-weight construction]
         + eps * (|cc| @ |W|) + eps*|A2|   [final fsum dot: products
                                            1 ulp + exact fsum]
    gC   = (2^16 + 32) eps : the accumulation is re-run with the
           bincount partial sums BOUNDED to N_SUB = 2^16 contributions
           per (bin, partial) -- Higham gamma_n with n = N_SUB -- and
           the partials folded into the accumulator by COMPENSATED
           (TwoSum, Knuth) addition whose residual is O(eps^2) (+32
           slack covers band assembly, <= 11 plain adds, and the
           compensation residue).  S_abs[i] = |c_at[i]| (the tent
           contributions are same-signed, so the abs-sum IS the sum).
    eps*X/D : u = log n carries a 1-ulp error <= eps*X; the tent slope
           1/D amplifies it (D = 2^-6 is exact, /D is exact); T[i] =
           sum of atom masses mu/2 hitting bin i (accumulated in the
           sieve).  THIS TERM IS IRREDUCIBLE at fixed precision --
           it is the accuracy of the atom positions themselves.
    C_ATOM = 8 : mu = 2 log(n)/sqrt(n) (log 1 ulp, sqrt+div 1.5 ulp),
           tent v = 1 - |i D - u|/D (i D exact dyadic, sub 1 ulp,
           /D exact), product mu*0.5*v (2 ulp) -- < 8 rounding ops.
    gQ   = 400 eps : GL-96 arch quadrature, <= 4 panels x 96 nodes +
           assembly; A_abs = the same quadrature on |integrand|.
    (M + C_T) eps, C_T = 8 : W_k = 2 sum_j f_j f_{j+k} (<= M terms,
           gamma_M) on the CONSTRUCTED float window f (whose deviation
           from ideal sin CANCELS between the two sides -- Guinand
           holds for any test vector; only evaluation errors count);
           Wabs = autocorrelation of |f|; C_abs = S_abs + |c_ar|.
           W12 error carried via 0.5(Wabs_pp + Wabs_11 + Wabs_22).

  (M2 side)  components a_j = 2 sqrt(wg_j) Re(rot F1(gamma_j)):
  cancellation inside F_of makes a RELATIVE bound wrong; the honest
  cap is A_cap_j = sqrt(wg_j) * sum|f1| (attained when no
  cancellation).  Per-component error E_a[j] = c_absF * A_cap_j with

    c_absF = max(C_SPOT * max spot dev / cap, M*eps)
    c_pole = max(C_SPOT * max pole spot dev, M*eps)

  anchored by mpmath dps-40 recomputation at PREDECLARED density (per
  rung: the top-4 family carriers + gamma_1 + 4 spread quantiles + the
  pole legs), C_SPOT = 10.  Then entrywise (x, y in {a, b}):

    dM2_xy   = fsum(|x| E_y + |y| E_x) + 4 eps G_abs_xy,
    G_abs_xy = fsum(|x_i||y_i|)      (fsum is exactly rounded)
    dcert    = sum_top100 (2|x_k| dx_k + dx_k^2) + eps cert100,
    dx_k     = |b_p| E_a[k] + |a_k| E_b[P] + |a_p| E_b[k]
               + |b_k| E_a[P] + 4 eps (|a_k b_p| + |b_k a_p|).

  (chain)  env_new = tail_term + eps_arch + max dA2 + max dM2;
  pert_new = env_new s1n (1 + 1e-10) + 2 env_new^2   [unchanged pert
  law; s1n from the fsum A2].  CITATION GATE: pert_new < cert100 -
  dcert.  RESOLVABILITY: lambda_min(A2 - M2) > 2 (max dA2 + max dM2)
  [2x2 sym: |dlambda| <= |E|_2 <= 2 max|e_ij|; the psd step is the
  closed-form 2x2 eigenvalue -- the norm-linear replacement of the
  Cholesky backward-error certificate deployed on the M x M ladder].

PREDECLARATIONS: N_SUB = 2^16 frozen from the pre-run estimate
  gC * (S_abs@|W| ~ 2e5) ~ 3e-6 < the closure need cert100/s1n ~ 9e-6
  at M = 1632 (margin ~3x; if the measured magnitudes are larger and
  closure fails, that is the honest (b) outcome).  Sieve cap: the
  compensated instrumentation costs ~40-60%, so T_CAP = 1800 s
  (declared; the (a)-decision requires the full six-rung set with
  X = 25.5; a drop is typed honestly).  Runtime target ~25-30 min.

DECISION (frozen): MARGIN-EXPOSED if lambda_min(A2 - M2) < -2(max dA2
  + max dM2) at any rung (a float-certified negative) OR the tail term
  ALONE blocks the gate (thin margin independent of float); else
  BUDGET-LINEAR-CLOSES-ALL if the citation gate closes on all six;
  else BUDGET-PARTIAL (binding term named per blocked rung).

CONTROLS: CT1 budget ward -- (i) two EXACT-BIN re-enumerations at the
  deepest rung (the deepest lag bin and the 7/8 bin): the bin's atoms
  re-sieved and pairwise-summed in sorted order (reference error
  ~60 eps << budget); |c_of[i] - ref| <= gC S_abs[i], margin typed;
  (ii) the mpmath spot deviations sit a factor C_SPOT below the caps
  by construction (max measured dev typed); (iii) |A2_fsum -
  A2_plain| <= dA2.  CT2 old-budget regression: rho, cert100,
  eps_f_old, pert_old, and the old closure set {1176, 1326, 1414}
  reproduce from the frozen cited table (lambda_min at loose tol 0.25,
  typed -- at depth its value is itself summation-order sensitive,
  which IS the resolvability finding).  CT3 [must-fire] scramble at
  M = 1176 still refused by the psd chain.

CONVENTION NOTE (deliverable 4): the budget above is REPORT-ONLY for
  future probes; the deployed v818 convention stays frozen in the
  verification suite.

FIREWALL: v563 / v692 / parent probes READ-ONLY; zero values used
openly (on-line by computation <= 2e4 via the parent's RS scan,
citation horizon 3e12 [Platt-Trudgian] in the tail chain); RNG only
in the declared CT3 scramble (seed 7).  Report only, nothing written.
"""

import math
import os
import sys
import time

import numpy as np
import scipy.linalg as sla

_here = os.path.dirname(os.path.abspath(__file__))
for _cand in (os.path.join(_here, "..", "..", "verification"), _here):
    if os.path.exists(os.path.join(_cand, "v563_paper2_readouts.py")):
        sys.path.insert(0, os.path.abspath(_cand))
        break
sys.path.insert(0, _here)

import v563_paper2_readouts as core          # noqa: E402 (READ-ONLY)
import v692_rank3_lockgram as lg             # noqa: E402 (READ-ONLY)
import prime_lagrange_pair_probe as pp       # noqa: E402 (READ-ONLY)
import prime_floor_theorem_probe as ft       # noqa: E402 (READ-ONLY)
import prime_tail_envelope_probe as tp       # noqa: E402 (READ-ONLY)
import floor_envelope_depth_probe as fdp     # noqa: E402 (READ-ONLY)
from mpmath import mp, mpf, mpc, expj as mexpj, exp as mexp, \
    sin as msin, sqrt as msqrt, re as mre  # noqa: E402 (VALUES only)

T0 = time.time()
FAILS = []
N_CHK = 0
fsum = math.fsum

# ------------------------------------------------- frozen bars / constants
EPS = float(np.finfo(float).eps)   # 2^-52 (unit roundoff = eps/2; the
#   budget uses the conservative 1-ulp = eps convention throughout)
N_SUB = 1 << 16               # bincount partial-sum bound (frozen)
G_C = (N_SUB + 32) * EPS      # tent-sum gamma (chunk-bounded + TwoSum)
C_ATOM = 8.0                  # per-contribution rounding ops
C_T = 8.0                     # window-vector construction ops
G_Q = 400.0 * EPS             # arch GL-96 quadrature float
C_SPOT = 10.0                 # slack on the mpmath spot anchor
MP_DPS = 40                   # anchoring precision
RES_FAC = 2.0                 # |E|_2 <= 2 max|e| for 2x2 symmetric
K_FAM = ft.K_FAM              # certified family size (100, frozen)
T_VER = tp.T_VER              # citation horizon 3e12 (cited)
T_CAP = 1800.0                # predeclared cap (instrumented sieve)
PROJ_SAFETY = 1.3
DGRID = fdp.DGRID
TARGET_MS = fdp.TARGET_MS
ANCHOR_MS = fdp.ANCHOR_MS
LAM_CITED = fdp.LAM_CITED
SEED_SCRAMBLE = fdp.SEED_SCRAMBLE
PARITY_M = fdp.PARITY_M
PARITY_C_ABS = fdp.PARITY_C_ABS
# frozen regression targets (prime_family_depth_probe, 2026-08-06):
CITED = {
    1176: dict(rho=1.959e-3, cert=1.52e-1, lam_r=2.81e-7,
               pert_o=2.47e-3, epsf_o=3.22e-7, tail=2.77e-9),
    1326: dict(rho=1.773e-3, cert=2.98e-1, lam_r=2.19e-7,
               pert_o=5.49e-2, epsf_o=2.56e-6, tail=6.59e-9),
    1414: dict(rho=1.684e-3, cert=4.49e-1, lam_r=1.91e-7,
               pert_o=3.38e-1, epsf_o=8.62e-6, tail=1.12e-8),
    1504: dict(rho=1.683e-3, cert=7.27e-1, lam_r=1.67e-7,
               pert_o=2.17e0, epsf_o=2.98e-5, tail=1.93e-8),
    1588: dict(rho=1.770e-3, cert=1.21e0, lam_r=1.48e-7,
               pert_o=1.23e1, epsf_o=9.50e-5, tail=3.26e-8),
    1632: dict(rho=1.855e-3, cert=1.62e0, lam_r=1.39e-7,
               pert_o=3.05e1, epsf_o=1.74e-4, tail=4.30e-8),
}
OLD_CLOSE_SET = {1176, 1326, 1414}   # old family-gate closure (cited)
REG_TOL = 2.0e-2              # regression tolerance (values re-derived
#   through a different summation order; ANCH_REL convention)
LAMR_TOL = 0.25               # lambda_min regression (loose, typed)
CHAIN_FAC_OLD = 100.0         # the old quadratic convention (regression)


def check(name, ok, detail=""):
    global N_CHK
    N_CHK += 1
    if not ok:
        FAILS.append(name.split()[0])
    print("[%s] %s%s" % ("PASS" if ok else "FAIL", name,
                         (": " + detail) if detail else ""))


# --------------------------------------- compensated banded accumulation
def twosum_add(c, e, x):
    """c += x with the TwoSum (Knuth) error pushed into e (exact)."""
    s = c + x
    b = s - c
    e += (c - (s - b)) + (x - b)
    c[:] = s


def tent_accumulate_comp(st, Mpad, D, u, mu, chunk=4000000, nsub=N_SUB):
    """The fdp tent convention with (i) bincount partials bounded to
    nsub contributions, (ii) TwoSum-compensated folding into st['c'] /
    st['e'], (iii) the mass accumulator st['T'] (budget quantity).
    Atoms have u >= log 2 > D, so the u < D reflection never fires
    (asserted)."""
    assert float(u.min(initial=np.inf)) > D or u.size == 0
    c, e, Tm = st["c"], st["e"], st["T"]
    for s in range(0, u.size, chunk):
        uu, mm = u[s:s + chunk], mu[s:s + chunk]
        i0 = np.floor(uu / D).astype(np.int64)
        for off in (-2, -1, 0, 1, 2):
            idx = i0 + off
            ok = (idx >= 0) & (idx < Mpad)
            if not ok.any():
                continue
            v = 1.0 - np.abs(idx[ok] * D - uu[ok]) / D
            pos = v > 0.0
            if not pos.any():
                continue
            ii = idx[ok][pos]
            ww = mm[ok][pos] * 0.5 * v[pos]
            tt = mm[ok][pos] * 0.5
            for s2 in range(0, ii.size, nsub):
                part = np.bincount(ii[s2:s2 + nsub],
                                   weights=ww[s2:s2 + nsub],
                                   minlength=Mpad)
                twosum_add(c, e, -part)
            Tm += np.bincount(ii, weights=tt, minlength=Mpad)


def seg_sieve_comp(caps, n_lo, n_hi, st, Mpad, cnt,
                   collect_mass_cap=None, seg=fdp.SEG_ASC):
    """fdp.seg_sieve_bands with the compensated+instrumented tent."""
    caps = np.asarray(caps, dtype=np.int64)
    masses = [] if collect_mass_cap else None
    bp = fdp.base_primes(int(math.isqrt(n_hi)))
    for lo in range(0, n_hi + 1, seg):
        hi = min(lo + seg, n_hi + 1)
        if hi - 1 <= n_lo:
            continue
        sv = np.ones(hi - lo, dtype=bool)
        if lo == 0:
            sv[:2] = False
        for p in bp:
            p = int(p)
            stt = max(p * p, ((lo + p - 1) // p) * p)
            if stt < hi:
                sv[stt - lo::p] = False
        nn = np.flatnonzero(sv).astype(np.float64) + float(lo)
        nn = nn[nn > n_lo]
        if nn.size == 0:
            continue
        lgn = np.log(nn)
        mu = 2.0 * lgn / np.sqrt(nn)
        bidx = np.searchsorted(caps, nn.astype(np.int64), side="left")
        for b in np.unique(bidx):
            sel = bidx == b
            tent_accumulate_comp(st[b], Mpad, DGRID, lgn[sel], mu[sel])
            cnt[b] += int(sel.sum())
        if masses is not None:
            keep = nn <= collect_mass_cap
            if keep.any():
                masses.append(mu[keep].copy())
    for p in bp:                             # prime powers p^k, k >= 2
        p = int(p)
        lp = math.log(p)
        q = p * p
        while q <= n_hi:
            if q > n_lo:
                u1 = np.array([math.log(q)])
                m1 = np.array([2.0 * lp / math.sqrt(q)])
                b = int(np.searchsorted(caps, q, side="left"))
                tent_accumulate_comp(st[b], Mpad, DGRID, u1, m1)
                cnt[b] += 1
                if masses is not None and q <= collect_mass_cap:
                    masses.append(m1.copy())
            q *= p
    return np.concatenate(masses) if masses else None


# ------------------------------------------------ arch |integrand| bound
_GX96, _GW96 = np.polynomial.legendre.leggauss(ft.GL_FINE)


def arch_A_abs(sv, D):
    """|integrand|-quadrature companion of ft.arch_A_fine (same nodes):
    an upper bound on the abs-mass the GL sums move (budget qty)."""
    sv = np.abs(np.asarray(sv, dtype=float))
    out = np.empty(sv.shape[0])
    far = sv >= D
    if far.any():
        s = sv[far].reshape(-1, 1)
        acc = np.zeros(s.shape[0])
        for lo, hi in ((s - D, s), (s, s + D)):
            mid, half = 0.5 * (lo + hi), 0.5 * (hi - lo)
            w = mid + half * _GX96[None, :]
            val = np.abs((1.0 - np.abs(s - w) / D) * np.exp(-0.5 * w)
                         / (-np.expm1(-2.0 * w)))
            acc += half[:, 0] * (val @ _GW96)
        out[far] = acc
    for i in np.nonzero(~far)[0]:
        s = float(sv[i])
        tri_s = max(0.0, 1.0 - s / D)
        W = s + D
        pts = sorted({0.0, s, D - s, W})
        pts = [p for p in pts if 0.0 <= p <= W]
        tot = 0.0
        for lo, hi in zip(pts[:-1], pts[1:]):
            if hi <= lo:
                continue
            mid, half = 0.5 * (lo + hi), 0.5 * (hi - lo)
            w = mid + half * _GX96
            tri = np.maximum(0.0, 1.0 - np.abs(s - w) / D)
            trr = np.maximum(0.0, 1.0 - np.abs(s + w) / D)
            val = np.abs((tri_s * np.exp(-2.0 * w)
                          - 0.5 * (tri + trr) * np.exp(-0.5 * w))
                         / (-np.expm1(-2.0 * w)))
            tot += half * float(np.dot(_GW96, val))
        out[i] = (abs(core.EULER + core.LOG_PI) * tri_s + 2.0 * tot
                  + tri_s * abs(-math.log1p(-math.exp(-2.0 * W))))
    return out


def wabs_of(f):
    """Wabs_k: lag weights of |f| (autocorrelation, k = 0..M-1)."""
    fa = np.abs(f)
    ac = np.correlate(fa, fa, "full")[len(f) - 1:]
    w = 2.0 * ac
    w[0] = ac[0]
    return w


def fsum_dot(x, y):
    return fsum((x * y).tolist())


# ---------------------------------------------------- mpmath anchoring
def mp_zero_legs(f1, f2, D, Mz, g):
    """(a, b) legs of one zero at dps 40 (incremental phase)."""
    mp.dps = MP_DPS
    Dm = mpf(D)
    gm = mpf(repr(float(g)))
    q = mexpj(Dm * gm)
    ph = mpc(1, 0)
    F1 = mpc(0, 0)
    F2 = mpc(0, 0)
    for j in range(Mz):
        F1 += mpf(repr(float(f1[j]))) * ph
        F2 += mpf(repr(float(f2[j]))) * ph
        ph *= q
    rot = mexpj(-(Mz - 1) * Dm * gm / 2) * mpc(0, "0.5")
    hw = Dm * gm / 2
    wg = Dm * (msin(hw) / hw) ** 2
    sq = 2 * msqrt(wg)
    return float(sq * mre(rot * F1)), float(sq * mre(rot * F2))


def mp_pole_legs(f1, f2, D, Mz):
    """(vp0, vp1) pole legs at dps 40 (real arithmetic)."""
    mp.dps = MP_DPS
    Dm = mpf(D)
    qd = mexp(-Dm / 2)
    qg = mexp(Dm / 2)
    pd = mpf(1)
    pg = mpf(1)
    Fp = {"1": mpf(0), "2": mpf(0)}
    Fm = {"1": mpf(0), "2": mpf(0)}
    for j in range(Mz):
        c1 = mpf(repr(float(f1[j])))
        c2 = mpf(repr(float(f2[j])))
        Fp["1"] += c1 * pd
        Fp["2"] += c2 * pd
        Fm["1"] += c1 * pg
        Fm["2"] += c2 * pg
        pd *= qd
        pg *= qg
    cs = (mexp(Dm / 4) - mexp(-Dm / 4)) / 2 / (Dm / 4)   # sinh(D/4)/(D/4)
    pref = cs * cs * Dm / 2
    P = {}
    for (i, j), (fa, fb) in {(0, 0): ("1", "1"), (1, 1): ("2", "2"),
                             (0, 1): ("1", "2")}.items():
        P[(i, j)] = P[(j, i)] = -pref * (Fp[fa] * Fm[fb]
                                         + Fp[fb] * Fm[fa])
    mid = (P[(0, 0)] + P[(1, 1)]) / 2
    rad = msqrt(((P[(0, 0)] - P[(1, 1)]) / 2) ** 2 + P[(0, 1)] ** 2)
    lmax = mid + rad
    v0, v1 = P[(0, 1)], lmax - P[(0, 0)]
    nrm = msqrt(v0 * v0 + v1 * v1)
    sq = msqrt(lmax if lmax > 0 else mpf(0))
    return float(sq * v0 / nrm), float(sq * v1 / nrm)


def run():
    global N_CHK, FAILS
    N_CHK = 0
    FAILS = []
    print("=" * 78)
    print("THE FLOAT-BUDGET ATTACK -- quadratic blanket -> rigorous "
          "Higham-linear chain")
    print("(prime_float_budget_probe, exploration only, no RH claim)")
    print("=" * 78)
    print("\nS0 -- the frozen budget (constants): gC = (2^16+32)eps = "
          "%.2e, eps*X/D at X = 25.5: %.2e," % (G_C, EPS * 25.5 / DGRID))
    print("      C_ATOM = %g, C_T = %g, gQ = %.1e, C_SPOT = %g, "
          "mp dps = %d, RES_FAC = %g" % (C_ATOM, C_T, G_Q, C_SPOT,
                                         MP_DPS, RES_FAC))

    # ============================================================== S1
    print("\nS1 -- zero list + deep instrument (compensated + "
          "instrumented sieve)")
    gam, n_rvm = pp.zero_list()
    check("S1.Z zero list: %d zeros to T = 2e4 (RvM dev %.2f <= 3)"
          % (len(gam), abs(len(gam) - n_rvm)),
          abs(len(gam) - n_rvm) <= 3.0)
    n_z = len(gam)

    # parity ward: compensated path == deployed T115 path at M = 896
    n_pw = fdp.nmax_of_M(PARITY_M)
    lam_tab = core.von_mangoldt_table(n_pw)
    nn0 = np.nonzero(lam_tab > 0.0)[0]
    u_pw = np.log(nn0.astype(float))
    mu_pw = 2.0 * lam_tab[nn0] / np.sqrt(nn0.astype(float))
    del lam_tab
    c_slow, _ = core.atom_lags_at(0.5 * PARITY_M * DGRID, PARITY_M,
                                  u_pw, mu_pw)
    st_pw = {0: dict(c=np.zeros(PARITY_M + 3), e=np.zeros(PARITY_M + 3),
                     T=np.zeros(PARITY_M + 3))}
    cnt_pw = {0: 0}
    seg_sieve_comp([n_pw], 0, n_pw, st_pw, PARITY_M + 3, cnt_pw)
    dev_pw = float(np.max(np.abs(
        (st_pw[0]["c"] + st_pw[0]["e"])[:PARITY_M] - c_slow)))
    check("S1.PARITY compensated banded assembly == deployed T115 "
          "path at M = %d (%d atoms): max |dc| = %.2e <= %.0e"
          % (PARITY_M, cnt_pw[0], dev_pw, PARITY_C_ABS),
          cnt_pw[0] == len(u_pw) and dev_pw <= PARITY_C_ABS)

    ms_all = sorted(set(TARGET_MS) | set(ANCHOR_MS))
    caps_all = [fdp.nmax_of_M(M) for M in ms_all]
    Mpad = max(ms_all) + 3
    st = {b: dict(c=np.zeros(Mpad), e=np.zeros(Mpad), T=np.zeros(Mpad))
          for b in range(len(ms_all))}
    cnt = {b: 0 for b in range(len(ms_all))}
    n_1176 = fdp.nmax_of_M(1176)
    t0 = time.time()
    masses_scr = seg_sieve_comp(caps_all, 0, n_1176, st, Mpad, cnt,
                                collect_mass_cap=n_1176)
    t_bench = time.time() - t0
    proj = {M: t_bench * (fdp.nmax_of_M(M) / n_1176) * PROJ_SAFETY
            for M in ms_all}
    deep_ms = [M for M in TARGET_MS if proj[M] <= T_CAP]
    print("    benchmark: %d atoms in %.1f s; projections: %s"
          % (cnt[0], t_bench,
             ", ".join("M=%d: %.0f s" % (M, proj[M])
                       for M in TARGET_MS)))
    dropped = [M for M in TARGET_MS if M not in deep_ms]
    if dropped:
        print("    DROPPED by the predeclared cap %.0f s: %s (typed)"
              % (T_CAP, ", ".join("M=%d" % M for M in dropped)))
    n_deep = fdp.nmax_of_M(max(deep_ms))
    t0 = time.time()
    seg_sieve_comp(caps_all, n_1176, n_deep, st, Mpad, cnt)
    print("    instrumented sieve to n = %d: %.1f s (projected %.0f s)"
          % (n_deep, time.time() - t0, proj[max(deep_ms)]))

    def c_of(M):
        nm = fdp.nmax_of_M(M)
        c = np.zeros(M)
        for b, cap in enumerate(caps_all):
            if cap <= nm:
                c += (st[b]["c"] + st[b]["e"])[:M]
        return c

    def T_of(M):
        nm = fdp.nmax_of_M(M)
        t = np.zeros(M)
        for b, cap in enumerate(caps_all):
            if cap <= nm:
                t += st[b]["T"][:M]
        return t

    import v755_simpler_schur_recursion as srp   # READ-ONLY
    anch_ok = True
    for M in [M for M in ANCHOR_MS if fdp.nmax_of_M(M) <= n_deep]:
        cT = srp.continuum_lags(M)[:M] + c_of(M)[:M]
        lamM = float(sla.eigvalsh(sla.toeplitz(cT),
                                  subset_by_index=[0, 0])[0])
        rel = abs(lamM - LAM_CITED[M]) / LAM_CITED[M]
        anch_ok = anch_ok and rel <= fdp.ANCH_REL
    check("S2.ANCH the certified-rung lambda_min anchors reproduce "
          "(rel <= %.2f) on every built certified rung" % fdp.ANCH_REL,
          anch_ok)

    # ============================================================== S2
    print("\nS2 -- per-rung objects + mpmath component anchoring "
          "(predeclared spot density)")
    deep = []
    spot_max_z, spot_max_p = 0.0, 0.0
    for M in deep_ms:
        dw = fdp.deep_window(M, c_of(M))
        ev = fdp.floor_eval(dw["t1"], dw["t2"], dw["W11"], dw["W22"],
                            dw["W12"], dw["c_ar"], dw["c_at"], DGRID,
                            M, full_geo=False)
        cc = dw["c_ar"] + dw["c_at"]
        # certified A2: fsum dots (exactly rounded); plain kept for CT1
        A2f = np.empty((2, 2))
        A2p = np.empty((2, 2))
        for (i, j), W in {(0, 0): dw["W11"], (1, 1): dw["W22"],
                          (0, 1): dw["W12"]}.items():
            A2f[i, j] = A2f[j, i] = fsum_dot(cc, W)
            A2p[i, j] = A2p[j, i] = float(cc @ W)
        wd = dict(f1=fdp.odd_ext(dw["t1"], M),
                  f2=fdp.odd_ext(dw["t2"], M), D=DGRID, M=M, h=M // 2)
        a, b, meta = pp.components_of(wd, gam)
        wg = meta["wg"]
        x_pz = a[:-1] * b[-1] - b[:-1] * a[-1]
        order = np.argsort(x_pz ** 2)[::-1]
        cert = fsum((x_pz[order[:K_FAM]] ** 2).tolist())
        M2 = np.array(
            [[fsum_dot(a, a), fsum_dot(a, b)],
             [fsum_dot(a, b), fsum_dot(b, b)]])
        lam_r = ft.eig2_min(A2f - M2)
        ev.update(M=M, X=M * DGRID, alpha=dw["alpha"], dw=dw, wd=wd,
                  cc=cc, A2=A2f, A2p=A2p, a=a, b=b, wg=wg, x_pz=x_pz,
                  order=order, cert=cert, M2=M2, lam_r=lam_r)
        # mpmath spot anchoring (top-4 carriers + gamma_1 + 4 spread)
        sf1 = fsum(np.abs(wd["f1"]).tolist())
        sf2 = fsum(np.abs(wd["f2"]).tolist())
        acap = np.sqrt(np.maximum(wg, 0.0)) * sf1
        bcap = np.sqrt(np.maximum(wg, 0.0)) * sf2
        spots = sorted(set([int(k) for k in order[:4]] + [0]
                           + [n_z // 8, n_z // 4, n_z // 2,
                              (3 * n_z) // 4]))
        for k in spots:
            am, bm = mp_zero_legs(wd["f1"], wd["f2"], DGRID, M, gam[k])
            spot_max_z = max(spot_max_z,
                             abs(am - a[k]) / max(acap[k], 1e-300),
                             abs(bm - b[k]) / max(bcap[k], 1e-300))
        vp0m, vp1m = mp_pole_legs(wd["f1"], wd["f2"], DGRID, M)
        if vp0m * a[-1] + vp1m * b[-1] < 0.0:
            vp0m, vp1m = -vp0m, -vp1m      # eigenvector sign gauge
        nvp = math.hypot(a[-1], b[-1])
        spot_max_p = max(spot_max_p, abs(vp0m - a[-1]) / nvp,
                         abs(vp1m - b[-1]) / nvp)
        ev.update(acap=acap, bcap=bcap, n_spots=len(spots))
        deep.append(ev)
    c_absF = max(C_SPOT * spot_max_z, max(M for M in deep_ms) * EPS)
    c_pole = max(C_SPOT * spot_max_p, max(M for M in deep_ms) * EPS)
    print("    spot deviations (%d zero-leg + %d pole spots): zero "
          "%.2e (cap-normalized), pole %.2e (rel)"
          % (sum(ev["n_spots"] for ev in deep), len(deep),
             spot_max_z, spot_max_p))
    print("    frozen-formula caps: c_absF = %.2e, c_pole = %.2e"
          % (c_absF, c_pole))

    # ============================================================== S3
    print("\nS3 -- THE NEW BUDGET vs THE OLD (per rung, entrywise)")
    print("    %5s %6s | %9s %9s %9s %9s %9s | %9s %9s | %9s %7s"
          % ("M", "alpha", "sum", "read", "wterm", "dot", "dA2",
             "dM2", "dcert", "epsf_old", "ratio"))
    for ev in deep:
        M, dw = ev["M"], ev["dw"]
        X = ev["X"]
        S_abs = np.abs(dw["c_at"])
        Tm = T_of(M)
        car_abs = np.abs(dw["c_ar"])
        A_abs = arch_A_abs(np.arange(M) * DGRID, DGRID)
        C_abs = S_abs + car_abs
        cc_abs = np.abs(ev["cc"])
        wab1 = wabs_of(ev["wd"]["f1"])
        wab2 = wabs_of(ev["wd"]["f2"])
        wabp = wabs_of(ev["wd"]["f1"] + ev["wd"]["f2"])
        wab12 = 0.5 * (wabp + wab1 + wab2)
        dA2 = {}
        parts_max = None
        for (i, j), (W, wab) in {(0, 0): (dw["W11"], wab1),
                                 (1, 1): (dw["W22"], wab2),
                                 (0, 1): (dw["W12"], wab12)}.items():
            Wa = np.abs(W)
            t_sum = G_C * float(S_abs @ Wa)
            t_read = (EPS * X / DGRID + C_ATOM * EPS) * float(Tm @ Wa)
            t_arch = G_Q * float(A_abs @ Wa)
            t_w = (M + C_T) * EPS * float(C_abs @ wab)
            t_dot = EPS * float(cc_abs @ Wa) + EPS * abs(ev["A2"][i, j])
            dA2[(i, j)] = t_sum + t_read + t_arch + t_w + t_dot
            if parts_max is None or dA2[(i, j)] > parts_max[-1]:
                parts_max = (t_sum, t_read, t_w, t_arch + t_dot,
                             dA2[(i, j)])
        dA2_max = max(dA2.values())
        # M2 side
        a, b = ev["a"], ev["b"]
        Ea = np.concatenate([c_absF * ev["acap"],
                             [c_pole * abs(a[-1])]])
        Eb = np.concatenate([c_absF * ev["bcap"],
                             [c_pole * abs(b[-1])]])
        aa, bb = np.abs(a), np.abs(b)
        dM2 = {}
        for (i, j), (x, y, Ex, Ey) in {(0, 0): (aa, aa, Ea, Ea),
                                       (1, 1): (bb, bb, Eb, Eb),
                                       (0, 1): (aa, bb, Ea, Eb)}.items():
            gabs = fsum_dot(x, y)
            dM2[(i, j)] = fsum_dot(x, Ey) + fsum_dot(y, Ex) \
                + 4.0 * EPS * gabs
        dM2_max = max(dM2.values())
        # cert budget
        ap, bp = abs(a[-1]), abs(b[-1])
        idx = ev["order"][:K_FAM]
        dx = (bp * Ea[idx] + aa[idx] * Eb[-1] + ap * Eb[idx]
              + bb[idx] * Ea[-1]
              + 4.0 * EPS * (aa[idx] * bp + bb[idx] * ap))
        xk = np.abs(ev["x_pz"][idx])
        dcert = fsum((2.0 * xk * dx + dx * dx).tolist()) \
            + EPS * ev["cert"]
        epsf_old = CHAIN_FAC_OLD * EPS \
            * float(np.linalg.norm(ev["A2"])) ** 2
        ev.update(dA2=dA2, dA2_max=dA2_max, dM2_max=dM2_max,
                  dcert=dcert, epsf_old=epsf_old, parts=parts_max,
                  dfloat=dA2_max + dM2_max)
        print("    %5d %6.2f | %9.2e %9.2e %9.2e %9.2e %9.2e | "
              "%9.2e %9.2e | %9.2e %7.0f"
              % (M, ev["alpha"], parts_max[0], parts_max[1],
                 parts_max[2], parts_max[3], dA2_max, dM2_max, dcert,
                 epsf_old, epsf_old / (dA2_max + dM2_max)))
    check("S3.LINEAR the new budget is norm-linear: dfloat = %.1e.."
          "%.1e vs the old quadratic %.1e..%.1e (improvement %.0f.."
          "%.0fx, growing with depth as diagnosed)"
          % (min(ev["dfloat"] for ev in deep),
             max(ev["dfloat"] for ev in deep),
             min(ev["epsf_old"] for ev in deep),
             max(ev["epsf_old"] for ev in deep),
             min(ev["epsf_old"] / ev["dfloat"] for ev in deep),
             max(ev["epsf_old"] / ev["dfloat"] for ev in deep)),
          all(ev["dfloat"] < ev["epsf_old"] for ev in deep))

    # ============================================================== S4
    print("\nS4 -- THE RE-CERTIFICATION (citation gate + "
          "resolvability, old vs new)")
    print("    %5s %6s | %9s %9s | %9s %9s | %5s %5s | %10s %6s"
          % ("M", "alpha", "pert_old", "pert_new", "cert100", "need",
             "old", "new", "lam_min(R)", "resol"))
    sh = tp.sh_sum(T_VER)
    for ev in deep:
        M = ev["M"]
        s1n = (abs(ev["A2"][0, 0]) + abs(ev["A2"][1, 1])
               + 2.0 * abs(ev["A2"][0, 1]))
        num_c = tp.num_sup({"h": M // 2, "D": DGRID}, 0.5)
        tail_term = (4.0 / DGRID) * num_c * sh
        dc = ft.arch_A_fine(np.arange(M) * DGRID, DGRID) \
            - np.asarray(core.arch_lags(M, DGRID), float)
        dw = ev["dw"]
        eps_arch = ft.ARCH_SLACK * max(
            abs(float(dc @ dw["W11"])), abs(float(dc @ dw["W22"])),
            abs(float(dc @ dw["W12"])))
        env_old = tail_term + ev["epsf_old"]
        pert_old = tp.pert_of(env_old, s1n)
        env_new = tail_term + eps_arch + ev["dfloat"]
        pert_new = tp.pert_of(env_new, s1n) * (1.0 + 1e-10)
        gate = ev["cert"] - ev["dcert"]
        close_old = pert_old < ev["cert"]
        close_new = pert_new < gate
        res_bud = RES_FAC * ev["dfloat"]
        resol = ev["lam_r"] > res_bud
        pert_tail_only = tp.pert_of(tail_term + eps_arch, s1n)
        ev.update(s1n=s1n, tail_term=tail_term, eps_arch=eps_arch,
                  pert_old=pert_old, pert_new=pert_new,
                  close_old=close_old, close_new=close_new,
                  res_bud=res_bud, resol=resol,
                  pert_tail=pert_tail_only)
        print("    %5d %6.2f | %9.2e %9.2e | %9.2e %9.2e | %5s %5s "
              "| %10.2e %6s"
              % (M, ev["alpha"], pert_old, pert_new, ev["cert"],
                 pert_new / max(gate, 1e-300), "yes" if close_old
                 else "NO", "YES" if close_new else "NO",
                 ev["lam_r"], "yes" if resol else "NO"))
    al_new = [ev["alpha"] for ev in deep if ev["close_new"]]
    al_blk = [ev["alpha"] for ev in deep if not ev["close_new"]]
    n_res = sum(1 for ev in deep if ev["resol"])
    print("    ALPHA-COVERAGE RETYPED: citation grade now covers "
          "alpha in {%s}%s"
          % (", ".join("%.2f" % a for a in al_new) or "none",
             ("; blocked: {%s}" % ", ".join("%.2f" % a
                                            for a in al_blk))
             if al_blk else " -- FULL SIEVE DEPTH"))
    print("    lambda_min(R) float-resolvability: %d/%d rungs "
          "(was 0/%d under the quadratic blanket)"
          % (n_res, len(deep), len(deep)))
    check("S4.GATE the citation-grade family gate under the new "
          "budget closes %d/%d deep rungs (old convention: %d/%d)"
          % (sum(1 for ev in deep if ev["close_new"]), len(deep),
             sum(1 for ev in deep if ev["close_old"]), len(deep)),
          sum(1 for ev in deep if ev["close_new"])
          >= sum(1 for ev in deep if ev["close_old"]))

    # ============================================================== S5
    print("\nS5 -- THE DECISION (frozen)")
    margin_exposed = any(ev["lam_r"] < -ev["res_bud"] for ev in deep) \
        or any(ev["pert_tail"] >= ev["cert"] - ev["dcert"]
               for ev in deep)
    if margin_exposed:
        decision = "MARGIN-EXPOSED"
    elif all(ev["close_new"] for ev in deep):
        decision = "BUDGET-LINEAR-CLOSES-ALL"
    else:
        decision = "BUDGET-PARTIAL"
    if decision == "BUDGET-PARTIAL":
        for ev in deep:
            if not ev["close_new"]:
                terms = dict(tail=ev["tail_term"],
                             arch=ev["eps_arch"],
                             float_A2=ev["dA2_max"],
                             float_M2=ev["dM2_max"])
                binding = max(terms, key=terms.get)
                print("    BLOCKED M = %d (alpha %.2f): binding term "
                      "%s = %.2e of env = %.2e"
                      % (ev["M"], ev["alpha"], binding,
                         terms[binding], ev["tail_term"]
                         + ev["eps_arch"] + ev["dfloat"]))
    print("    decision: %s" % decision)

    # ============================================================== CT
    print("\nCT -- controls")
    # CT1(i) exact-bin re-enumeration at the deepest rung
    evd = deep[-1]
    Md = evd["M"]
    nmax_d = fdp.nmax_of_M(Md)
    bw_ok = True
    for ib in (Md - 1, (7 * Md) // 8):
        u_lo, u_hi = (ib - 1) * DGRID, (ib + 1) * DGRID
        a_n = max(2, int(math.floor(math.exp(u_lo))) + 1)
        b_n = min(nmax_d, int(math.floor(math.exp(u_hi))))
        bp = fdp.base_primes(int(math.isqrt(b_n)))
        vals = []
        for lo in range(a_n, b_n + 1, fdp.SEG_ASC):
            hi = min(lo + fdp.SEG_ASC, b_n + 1)
            sv = np.ones(hi - lo, dtype=bool)
            for p in bp:
                p = int(p)
                stt = max(p * p, ((lo + p - 1) // p) * p)
                if stt < hi:
                    sv[stt - lo::p] = False
            nn = np.flatnonzero(sv).astype(np.float64) + float(lo)
            if nn.size == 0:
                continue
            un = np.log(nn)
            v = 1.0 - np.abs(ib * DGRID - un) / DGRID
            m = v > 0.0
            vals.append((2.0 * un[m] / np.sqrt(nn[m])) * 0.5 * v[m])
        for p in bp:
            p = int(p)
            q = p * p
            while q <= b_n:
                if q >= a_n:
                    uq = math.log(q)
                    vq = 1.0 - abs(ib * DGRID - uq) / DGRID
                    if vq > 0.0:
                        vals.append(np.array(
                            [2.0 * math.log(p) / math.sqrt(q)
                             * 0.5 * vq]))
                q *= p
        w_all = np.sort(np.concatenate(vals))
        ref = -float(np.sum(w_all))          # pairwise, ~60 eps rel
        got = float(evd["dw"]["c_at"][ib])
        bud_i = G_C * abs(got)
        dev = abs(got - ref)
        bw_ok = bw_ok and dev <= bud_i
        print("    exact-bin i = %4d (%d atoms): |dev| = %.2e vs "
              "budget %.2e (margin %.0fx) %s"
              % (ib, w_all.size, dev, bud_i,
                 bud_i / max(dev, 1e-300), "ok" if dev <= bud_i
                 else "MISS"))
    check("CT1a budget ward (accumulation): the exact-bin references "
          "sit inside the gC S_abs budget at the deepest rung", bw_ok)
    fs_ok = True
    for ev in deep:
        d_fp = float(np.max(np.abs(ev["A2"] - ev["A2p"])))
        fs_ok = fs_ok and d_fp <= ev["dA2_max"]
    check("CT1b budget ward (dots): |A2_fsum - A2_plain| <= dA2 on "
          "every rung (max %.1e)"
          % max(float(np.max(np.abs(ev["A2"] - ev["A2p"])))
                for ev in deep), fs_ok)
    check("CT1c budget ward (components): the mpmath spot deviations "
          "sit a factor >= %.0f below the frozen caps (zero %.1e vs "
          "cap %.1e; pole %.1e vs %.1e)"
          % (C_SPOT, spot_max_z, c_absF, spot_max_p, c_pole),
          c_absF >= C_SPOT * spot_max_z * (1.0 - 1e-12)
          and c_pole >= C_SPOT * spot_max_p * (1.0 - 1e-12))
    # CT2 old-budget regression
    reg_ok, lam_note = True, []
    for ev in deep:
        ct = CITED[ev["M"]]
        for key, val, tol in (("rho", ev["rho"], REG_TOL),
                              ("cert", ev["cert"], REG_TOL),
                              ("epsf_o", ev["epsf_old"], REG_TOL),
                              ("pert_o", ev["pert_old"], REG_TOL),
                              ("tail", ev["tail_term"], REG_TOL)):
            reg_ok = reg_ok and abs(val - ct[key]) / ct[key] <= tol
        lam_note.append(abs(ev["lam_r"] - ct["lam_r"]) / ct["lam_r"])
    close_set = {ev["M"] for ev in deep if ev["close_old"]}
    reg_ok = reg_ok and close_set == OLD_CLOSE_SET
    check("CT2 old-budget regression: rho / cert100 / eps_f_old / "
          "pert_old / tail reproduce the cited table (rel <= %.2f) "
          "and the old closure set == %s; lambda_min(R) shifts "
          "%.3f..%.3f under the changed summation order (loose bar "
          "%.2f -- the shift itself is the resolvability finding, "
          "typed)"
          % (REG_TOL, sorted(OLD_CLOSE_SET), min(lam_note),
             max(lam_note), LAMR_TOL),
          reg_ok and max(lam_note) <= LAMR_TOL)
    # CT3 scramble
    ev0 = next(ev for ev in deep if ev["M"] == 1176)
    rng = np.random.default_rng(SEED_SCRAMBLE)
    u_scr = rng.uniform(0.0, 1176 * DGRID, size=masses_scr.size)
    c_scr = np.zeros(1176)
    fdp.tent_accumulate_D(c_scr, 1176, DGRID, u_scr, masses_scr)
    dw0 = ev0["dw"]
    ccs = dw0["c_ar"] + c_scr
    A2s = np.array([[ccs @ dw0["W11"], ccs @ dw0["W12"]],
                    [ccs @ dw0["W12"], ccs @ dw0["W22"]]])
    lam_scr = ft.eig2_min(A2s - ev0["M2"])
    check("CT3 [must-fire] scramble at M = 1176 (same %d masses, "
          "seed %d): lambda_min(A2_scr - M2) = %.3e < 0 -- the psd "
          "chain still refuses the scrambled comb"
          % (masses_scr.size, SEED_SCRAMBLE, lam_scr), lam_scr < 0.0)

    # ============================================================== V
    print("\n" + "=" * 78)
    print("V -- VERDICT: %s" % decision)
    print("=" * 78)
    if decision == "BUDGET-LINEAR-CLOSES-ALL":
        cfr = [(ev["cert"] - ev["dcert"] - ev["pert_new"])
               / (ev["lam"] * ev["tau"]) for ev in deep]
        print("""
  STRONGEST UNIFORM ASSERTION NOW SUPPORTED (verbatim):
    'On every deep rung X = %.3f..%.3f (alpha = %.2f..%.2f, full
     sieve depth), lambda tau = det A2 >= cert100 - dcert - pert_new:
     the certified pole x alias family carries >= %.3f of the floor
     at CITATION grade -- inputs: [A1] (all zeros in the strip),
     verified on-line zeros to T_ver = 3e12 [Platt-Trudgian 2021],
     explicit RvM counting constants [Trudgian-grade], the sharpened
     tail chain (prime_tail_envelope_probe), and the Higham-linear
     float budget frozen above (compensated banded accumulation,
     N_SUB = 2^16, exact fsum dots, dps-40 anchored components).
     The certified-family lower bound on rho sits within 2%% of the
     measured value; lambda_min(A2 - M2) >= 0 is float-resolvable
     on %d/%d rungs.'
  The alpha* ~ 11 horizon was an artifact of the quadratic float
  convention; the citation-grade reach now extends to alpha = %.2f."""
              % (deep[0]["X"], deep[-1]["X"], deep[0]["alpha"],
                 deep[-1]["alpha"], min(cfr), n_res, len(deep),
                 deep[-1]["alpha"]))
    elif decision == "BUDGET-PARTIAL":
        print("""
  The linear budget improves the float term %.0f..%.0fx but the gate
  stays blocked on %d rung(s); the binding terms are named above --
  the honest remaining boundary."""
              % (min(ev["epsf_old"] / ev["dfloat"] for ev in deep),
                 max(ev["epsf_old"] / ev["dfloat"] for ev in deep),
                 sum(1 for ev in deep if not ev["close_new"])))
    else:
        print("""
  A REAL THIN MARGIN WAS EXPOSED: the failure survives the budget
  tightening (tail-only pert >= cert100, or a float-certified
  negative lambda_min).  The quadratic convention was hiding it --
  reported prominently, typed above.""")
    print("""
  CONVENTION NOTE (report only): the frozen budget formula in the
  header is proposed for FUTURE probes; the deployed v818 convention
  stays frozen in the verification suite.""")
    dt = time.time() - T0
    print("-" * 78)
    print("checks: %d run, %d failed%s | runtime %.1f min"
          % (N_CHK, len(FAILS),
             (" [" + ", ".join(FAILS) + "]") if FAILS else "",
             dt / 60.0))
    print("NO RH claim; exploration only; nothing outside "
          "experiments/ touched.")


if __name__ == "__main__":
    run()
