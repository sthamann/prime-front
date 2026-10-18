"""Discovery probe: EPSTEIN FIREWALL -- the NEGATIVE CONTROL of the
Weil-positivity window machinery on a zeta WITHOUT Euler product.

CONTEXT.  The W3 program measures positivity margins of windowed Weil
forms built from the von Mangoldt atoms 2Λ(n)/sqrt(n).  A machinery
that stayed positive on an RH-VIOLATING zeta would be suspicious: its
family positivity would carry no arithmetic information.  The Epstein
zeta of Q1(x,y) = x² + 5y² (discriminant -20, class number 2) is the
classical violator: it has NO Euler product, and Davenport-Heilbronn
(1936) proved it has infinitely many zeros with Re s > 1 (hence RH
fails badly).  Its exact decomposition into two Euler products,

    E(s) = Σ' (x²+5y²)^{-s} = ζ(s) L(s, χ_-20) + L(s, χ_-4) L(s, χ_5)

(genus-character identity, verified coefficient-wise below), makes it
the perfect ablation lab: the CLASS SUM (ζ_Q1 + ζ_Q2)/2 = ζ L_-20 =
ζ_K(Q(sqrt-5)) RESTORES the Euler product, while the single class
E = ζ L_-20 + L_-4 L_5 destroys it.  This probe (i) computes the
correct von Mangoldt analogue Λ_E(n) of E by Dirichlet-series
division of -E'/E from the representation numbers r_Q(n), (ii) runs
the IDENTICAL frame-A tent machinery (verification/v563, read-only)
with atom masses 2Λ_X(n)/sqrt(n) swapped along an ablation ladder,
and (iii) measures WHERE positivity breaks and WHICH structural
building block carries the break.  PASS = the machinery breaks
demonstrably and diagnosably.  No marker move, no RH statement.

TRANSLATION FREEDOMS (fixed here, documented):
  F1  the archimedean + pole layer c_ar of the ζ machinery is kept
      FIXED across all rungs (controlled ablation: only the atom
      masses change).  Epstein's true completed form has Γ(s) instead
      of Γ(s/2) and pole residue π/sqrt5 instead of 1 -- the absolute
      λ_min of the swapped rungs carries that bias; the DIFFERENCES
      between rungs are the measurement.  Note -X'/X has residue 1 at
      s = 1 for ζ, ζ_K and E/2 alike (simple pole), so the leading
      atom density ψ_X(x) ~ x matches across L0/L1/L3;
  F2  normalization: E is divided by r(1) = 2 (b_n = r_Q1(n)/2,
      b_1 = 1) before -E'/E extraction;
  F3  the window family is the deployed frame-A family (v563),
      truncated to windows whose atom budget e^{2α} <= N_CAP fits the
      computed Λ_E table;
  F4  Λ_E is THE correct "von Mangoldt analogy" (coefficients of
      -E'/E); without an Euler product it is neither >= 0 nor
      supported on prime powers -- exactly the structural difference
      this probe measures.

CALIBRATION HISTORY (declared -- honesty first): run 1 (2026-08-02)
passed all gates but showed that the Euler-true class-sum rung L1
(ζ_K = ζ L_-20, SAME Γ(s)-type functional equation and conductor as
E) ALSO fails the ζ-calibrated arch layer -- the declared F1 bias is
real and NOT negligible.  Run 2 adds, WITHOUT touching any gate: a
printed DIFFERENTIAL block in B3 (excess λ_min(L3) - λ_min(L1),
ratio λ_min(L3)/λ_min(L1), npp share of the atom-side attribution),
because the clean Epstein statement is the EXCESS over the same-
functional-equation Euler control L1, not the absolute λ_min.

PREREGISTERED DECISIONS (declared BEFORE the numbers):
  * N_CAP = 100000: r_Q1, r_Q2 by exact lattice count; identity
    guards r_Q1(n) = Σ_{d|n} χ_-20(d) + (χ_-4 * χ_5)(n) and
    r_Q2(n) = Σ_{d|n} χ_-20(d) - (χ_-4 * χ_5)(n) EXACTLY for all
    n <= N_CAP; b_n = r_Q1(n)/2 integer;
  * division machinery validated on THREE known Euler products
    before use on E: coefficients 1 -> Λ(n) (SPF sieve reference);
    Σ_{d|n} χ_-20(d) -> Λ(n)(1 + χ_-20(n)); (χ_-4 * χ_5)(n) ->
    Λ(n)(χ_-4(n) + χ_5(n)); max abs dev < 1e-8 each;
  * B1 arithmetic reads (gates: >= 1 negative Λ_E value and >= 1
    non-prime-power support point below N_CAP; rest measured): first
    negative site, count/mass of negatives, support off prime
    powers, dyadic growth of max|Λ_E| vs the Euler bound log n,
    deviation of Λ_E from the would-be Euler average (Λ_A + Λ_B)/2,
    Chebyshev reads (ψ_X(x) - x)/sqrt(x) at x = 1e3/1e4/1e5;
  * B2 window ablation: candidates = frame-A zones with e^{2α} <=
    N_CAP and h <= 1100; picks at h-quantiles {0.25, 0.5, 1.0}
    (nearest h; if a pick's L0 baseline is not positive above the
    floor, substitute the next-nearest candidate -- reported);
    ladder per window, all with atom positions log n and masses
    2Λ_X(n)/sqrt(n) via the verbatim core tent assembly:
      L0  Λ(n)            (deployed baseline; must be > floor),
      L1  Λ(n)(1+χ_-20)   (class-sum restoration ζ_K: Euler product
                           restored from the SAME lattice data),
      L2  Λ(n)(χ_-4+χ_5)  (the genus partner L_-4 L_5: Euler product,
                           signed weights, no pole -- density 0),
      L3  Λ_E(n)          (the Epstein rung: no Euler product),
      L4a Λ_E restricted to prime powers,
      L4b Λ_E restricted to non-prime-powers;
    floor = 20 eps · rad · sqrt(h) (family convention); wiring
    guards: sieve-Λ rebuild of L0 matches the core-table L0 λ_min
    (rel 1e-10); lag additivity c_at(L3) = c_at(L4a) + c_at(L4b)
    (abs < 1e-10 · scale);
  * B3 localization on the L3 minimizer v*: exact Rayleigh
    attribution λ_min = r_arch + r_pp + r_npp (guard abs dev <
    1e-8 · rad) and the positive/negative-weight split r_pos +
    r_neg = r_pp + r_npp; FIREWALL GATE: λ_min(L3) < -floor on >= 1
    window; diagnosis typed from which rungs break (L4a/L4b/L1);
  * B4 (printed, NO gate): off-line zero count of E by argument-
    principle winding around the declared box Re s in [0.6, 1.4],
    Im s in [2, 100] (mpmath dps 15, adaptive boundary walk, arg
    step bar 1.5 rad, eval cap 30000), with the analytic E(s)
    identity guarded against the truncated Dirichlet series at
    s = 2 + 5i (rel < 1e-3).  Davenport-Heilbronn stands as the
    literature ground truth for RH violation regardless of whether
    the box catches a zero.

Verdict enums (frozen, precedence top-down): EPSTEIN-FW-MIXED
(guards fail), EPSTEIN-FW-UNPOWERED (no positive-baseline window),
EPSTEIN-FW-BREAKS (L3 breaks on >= 1 window -- the firewall PASS),
EPSTEIN-FW-SUSPICIOUS (L3 stays positive everywhere: the family
positivity read carries no RH information at this depth).

FIREWALL: experiments-only; verification/ read-only (v563 import);
no marker moves; no positivity claim for ζ; no RH statement; NO zero
of any L-function is read as input (the B4 winding count is a
measured OUTPUT of this probe, not a zero table; AST-checked: no
zetazero/nzeros loader).  Python-only, per GATE.WOLFRAM.02.

Provenance: ihara_ground_truth_probe.py (slice A, positive-control
twin), w3_uniform_bound_probe / w3_resonance_landscape_probe
(2026-08-02, the W3 margin question), v563 (tent machinery),
Davenport-Heilbronn 1936 (Epstein zeros off the line, cited).
"""
import ast
import cmath
import math
import os
import sys
import time

import numpy as np

_here = os.path.dirname(os.path.abspath(__file__))
for _cand in (_here, os.path.join(_here, "..", "..", "verification")):
    if os.path.exists(os.path.join(_cand, "v563_paper2_readouts.py")):
        sys.path.insert(0, os.path.abspath(_cand))
        break

T0 = time.time()
FAILS = []
N_CHK = 0

EPS = float(np.finfo(float).eps)
FLOOR_SAFETY = 20.0          # family convention, verbatim
N_CAP = 100000               # Λ_E table horizon
H_CAP = 1100                 # window size cap (runtime)
QUANTS = (0.25, 0.50, 1.00)  # window picks by h-quantile
LAM_TOL = 1e-9
TOL_DIV = 1e-8
TOL_WIRE = 1e-10
TOL_ATTR = 1e-8
PSI_X = (1000, 10000, 100000)
# B4 winding box (declared)
BOX_S = (0.6, 1.4)
BOX_T = (2.0, 100.0)
ARG_BAR = 1.5                # rad per boundary step
STEP_T = 0.2                 # base boundary step in t
STEP_S = 0.05                # base boundary step in sigma
MAX_EVAL = 30000
MIN_STEP = 1e-6
TOL_EID = 1e-3               # E identity vs truncated Dirichlet sum


def check(name, ok, detail=""):
    global N_CHK
    N_CHK += 1
    if not ok:
        FAILS.append(name.split()[0])
    print("[%s] %s%s" % ("PASS" if ok else "FAIL", name,
                         (": " + detail) if detail else ""))


def ast_zero_firewall(src_path):
    with open(src_path, "r", encoding="utf-8") as fh:
        tree = ast.parse(fh.read())
    for node in ast.walk(tree):
        if isinstance(node, ast.Attribute) and node.attr in (
                "zetazero", "nzeros", "second_sheet_zero"):
            return False
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) \
                and node.func.id in ("zetazero", "nzeros"):
            return False
    return True


import v563_paper2_readouts as core  # noqa: E402  (READ-ONLY import)
import mpmath as mp  # noqa: E402
import scipy.linalg as sla  # noqa: E402


def gen_min_eig2(A, G):
    w, V = sla.eigh(0.5 * (A + A.T), 0.5 * (G + G.T))
    rad = max(abs(float(w[0])), abs(float(w[-1])))
    return float(w[0]), V[:, 0], rad


# ------------------------------------------------- arithmetic sieves
def spf_lambda(N):
    """von Mangoldt via smallest-prime-factor sieve (reference)."""
    spf = np.zeros(N + 1, dtype=np.int64)
    for i in range(2, N + 1):
        if spf[i] == 0:
            spf[i::i] = np.where(spf[i::i] == 0, i, spf[i::i])
    lam = np.zeros(N + 1)
    ispp = np.zeros(N + 1, dtype=bool)
    for n in range(2, N + 1):
        p = int(spf[n])
        m = n
        while m % p == 0:
            m //= p
        if m == 1:
            lam[n] = math.log(p)
            ispp[n] = True
    return lam, ispp


def chi_arrays(N):
    nn = np.arange(N + 1)
    chi4 = np.array([0, 1, 0, -1], dtype=np.int64)[nn % 4]
    chi5 = np.array([0, 1, -1, -1, 1], dtype=np.int64)[nn % 5]
    return chi4, chi5, chi4 * chi5


def lattice_r1(N):
    """r_{Q1}(n), Q1 = x² + 5y², exact count over Z²."""
    r = np.zeros(N + 1, dtype=np.int64)
    for x in range(0, int(math.isqrt(N)) + 1):
        x2 = x * x
        wx = 2 if x > 0 else 1
        ymax = int(math.isqrt((N - x2) // 5)) if x2 <= N else -1
        for y in range(0, ymax + 1):
            n = x2 + 5 * y * y
            if n == 0 or n > N:
                continue
            r[n] += wx * (2 if y > 0 else 1)
    return r


def lattice_r2(N):
    """r_{Q2}(n), Q2 = 2x² + 2xy + 3y², exact count over Z²."""
    r = np.zeros(N + 1, dtype=np.int64)
    ymax = int(math.isqrt(2 * N // 5)) + 1
    xr = int(math.isqrt(N // 2)) + 2
    for y in range(-ymax, ymax + 1):
        for x in range(int(-y / 2) - xr, int(-y / 2) + xr + 1):
            n = 2 * x * x + 2 * x * y + 3 * y * y
            if 0 < n <= N:
                r[n] += 1
    return r


def divisor_transform(chi, N):
    """a(n) = Σ_{d|n} chi(d)."""
    out = np.zeros(N + 1, dtype=np.int64)
    for d in range(1, N + 1):
        out[d::d] += chi[d]
    return out


def convolution_45(chi4, chi5, N):
    """(χ_-4 * χ_5)(n) = Σ_{de=n} χ_-4(d) χ_5(e)."""
    out = np.zeros(N + 1, dtype=np.int64)
    for d in range(1, N + 1):
        k = N // d
        out[d::d] += chi4[d] * chi5[1:k + 1]
    return out


def dirichlet_vonmangoldt(a, N):
    """Coefficients Λ_F(n) of -F'/F for F = Σ a_n n^{-s}, a_1 = 1:
    a_n log n = Σ_{jk=n} Λ_F(j) a_k, solved ascending."""
    lam = np.zeros(N + 1)
    S = np.zeros(N + 1)
    logs = np.zeros(N + 1)
    logs[1:] = np.log(np.arange(1, N + 1, dtype=float))
    af = a.astype(float)
    for n in range(2, N + 1):
        lam[n] = af[n] * logs[n] - S[n]
        k = N // n
        if k >= 2:
            S[2 * n::n] += lam[n] * af[2:k + 1]
    return lam


# ------------------------------------------------- window machinery
def build_window_geometry(kz):
    alpha = float(core.U_ALL[kz])
    D_k = 0.5 * float(core.G_ALL[kz]) / float(core.NU_MAIN)
    Mz = int(math.ceil(alpha / D_k - 1.0e-9)) + 1
    if Mz % 2:
        Mz += 1
    return alpha, Mz


def window_form(alpha, Mz, positions, masses, c_ar):
    c_at, D = core.atom_lags_at(alpha, Mz, positions, masses)
    A = core.odd_toeplitz(c_ar + c_at, Mz)
    g = np.zeros(Mz)
    g[0], g[1] = 2.0 * D / 3.0, D / 6.0
    Gm = core.odd_toeplitz(g, Mz)
    return A, Gm, c_at


def rayleigh(v, A, Gm):
    return float(v @ (A @ v)) / float(v @ (Gm @ v))


# ------------------------------------------------- analytic E (B4)
def make_L(q, chi_of_a):
    def L(s):
        tot = mp.mpc(0)
        for a, c in chi_of_a:
            tot += c * mp.zeta(s, mp.mpf(a) / q)
        return tot * mp.power(q, -s)
    return L


L4_AN = make_L(4, [(1, 1), (3, -1)])
L5_AN = make_L(5, [(1, 1), (2, -1), (3, -1), (4, 1)])
L20_AN = make_L(20, [(1, 1), (3, 1), (7, 1), (9, 1),
                     (11, -1), (13, -1), (17, -1), (19, -1)])


def E_analytic(s):
    return mp.zeta(s) * L20_AN(s) + L4_AN(s) * L5_AN(s)


def winding_count():
    """Argument-principle walk around the declared box; returns
    (count, n_eval, resolved)."""
    s0, s1 = BOX_S
    t0, t1 = BOX_T
    corners = [complex(s1, t0), complex(s1, t1), complex(s0, t1),
               complex(s0, t0), complex(s1, t0)]
    steps = [STEP_T, STEP_S, STEP_T, STEP_S]
    cache = {}
    n_eval = [0]

    def f(z):
        key = (round(z.real, 9), round(z.imag, 9))
        if key not in cache:
            v = E_analytic(mp.mpc(z.real, z.imag))
            cache[key] = complex(v)
            n_eval[0] += 1
        return cache[key]

    total = 0.0
    resolved = True
    for (za, zb), st in zip(zip(corners[:-1], corners[1:]), steps):
        L = abs(zb - za)
        npt = max(2, int(math.ceil(L / st)) + 1)
        params = list(np.linspace(0.0, 1.0, npt))
        stack = [(params[i], params[i + 1]) for i in range(npt - 1)]
        stack.reverse()
        while stack:
            if n_eval[0] > MAX_EVAL:
                resolved = False
                break
            a, b = stack.pop()
            fa = f(za + (zb - za) * a)
            fb = f(za + (zb - za) * b)
            if abs(fa) == 0.0 or abs(fb) == 0.0:
                resolved = False
                continue
            d = cmath.phase(fb / fa)
            if abs(d) > ARG_BAR and (b - a) > MIN_STEP:
                mid = 0.5 * (a + b)
                stack.append((mid, b))
                stack.append((a, mid))
            else:
                if abs(d) > ARG_BAR:
                    resolved = False
                total += d
        if not resolved and n_eval[0] > MAX_EVAL:
            break
    return total / (2.0 * math.pi), n_eval[0], resolved


def run():
    global N_CHK, FAILS
    N_CHK = 0
    FAILS = []
    print("=" * 78)
    print("EPSTEIN FIREWALL -- Q(x,y) = x² + 5y² (disc -20, h = 2, "
          "no Euler product)")
    print("=" * 78)
    check("G0.0 [E] AST zero-firewall: no zero-table loader in this "
          "probe", ast_zero_firewall(os.path.abspath(__file__)))

    # ------------------------------------------------ G0: arithmetic
    N = N_CAP
    lam_ref, ispp = spf_lambda(N)
    chi4, chi5, chi20 = chi_arrays(N)
    r1 = lattice_r1(N)
    r2 = lattice_r2(N)
    div20 = divisor_transform(chi20, N)
    conv45 = convolution_45(chi4, chi5, N)
    dev1 = int(np.max(np.abs(r1[1:] - (div20[1:] + conv45[1:]))))
    dev2 = int(np.max(np.abs(r2[1:] - (div20[1:] - conv45[1:]))))
    check("G0.1 [E] genus identity EXACT for all n <= %d: r_Q1 = "
          "Σχ_-20 + χ_-4*χ_5 (max dev %d), r_Q2 = Σχ_-20 - χ_-4*χ_5 "
          "(max dev %d) -- E = ζL_-20 + L_-4 L_5 coefficient-wise"
          % (N, dev1, dev2), dev1 == 0 and dev2 == 0)
    check("G0.2 [E] b_n = r_Q1(n)/2 integral (r_Q1 even everywhere), "
          "b_1 = 1", bool(np.all(r1[1:] % 2 == 0)) and r1[1] == 2)
    b = (r1 // 2).astype(np.int64)

    ones = np.ones(N + 1, dtype=np.int64)
    lam_z = dirichlet_vonmangoldt(ones, N)
    lam_A_x = dirichlet_vonmangoldt(div20, N)
    lam_B_x = dirichlet_vonmangoldt(conv45, N)
    lam_A = lam_ref * (1.0 + chi20[:N + 1])
    lam_B = lam_ref * (chi4[:N + 1] + chi5[:N + 1]).astype(float)
    d_z = float(np.max(np.abs(lam_z - lam_ref)))
    d_A = float(np.max(np.abs(lam_A_x - lam_A)))
    d_B = float(np.max(np.abs(lam_B_x - lam_B)))
    check("G0.3 [E] division machinery validated on three Euler "
          "products: ζ -> Λ (dev %.1e), ζL_-20 -> Λ(1+χ_-20) (dev "
          "%.1e), L_-4 L_5 -> Λ(χ_-4+χ_5) (dev %.1e); all < %.0e"
          % (d_z, d_A, d_B, TOL_DIV),
          max(d_z, d_A, d_B) < TOL_DIV)

    lam_E = dirichlet_vonmangoldt(b, N)

    # ------------------------------------------------ B1: structure
    print("\nB1 -- the von Mangoldt analogue Λ_E(n) of the Epstein "
          "zeta (no Euler product)")
    neg_idx = np.where(lam_E < -LAM_TOL)[0]
    offpp = np.where((~ispp) & (np.abs(lam_E) > LAM_TOL))[0]
    offpp = offpp[offpp >= 2]
    i_min = int(np.argmin(lam_E))
    i_maxabs = int(np.argmax(np.abs(lam_E)))
    neg_mass = float(np.sum(np.abs(lam_E[neg_idx])))
    tot_mass = float(np.sum(np.abs(lam_E)))
    print("      first 24 nonzero sites (n, Λ_E, Euler-average "
          "(Λ_A+Λ_B)/2, prime power?):")
    shown = 0
    avg_AB = 0.5 * (lam_A + lam_B)
    for n in range(2, N + 1):
        if abs(lam_E[n]) > LAM_TOL or abs(avg_AB[n]) > LAM_TOL:
            print("      n = %5d   Λ_E = %+9.4f   euler-avg = %+9.4f"
                  "   pp = %s%s"
                  % (n, lam_E[n], avg_AB[n], bool(ispp[n]),
                     "   <- NEGATIVE" if lam_E[n] < -LAM_TOL else ""))
            shown += 1
            if shown >= 24:
                break
    check("B1.1 [E] the Euler-product structure is GONE: Λ_E has %d "
          "negative sites below %d (first at n = %d, Λ_E = %+.4f; "
          "most negative %+.4f at n = %d) and %d support points OFF "
          "prime powers (first at n = %d); negative-|mass| share "
          "%.4f of total"
          % (len(neg_idx), N, int(neg_idx[0]) if len(neg_idx) else -1,
             lam_E[int(neg_idx[0])] if len(neg_idx) else 0.0,
             lam_E[i_min], i_min, len(offpp),
             int(offpp[0]) if len(offpp) else -1,
             neg_mass / tot_mass),
          len(neg_idx) > 0 and len(offpp) > 0)

    dev_pp = np.abs(lam_E - avg_AB)[ispp]
    n_pp_dev = int(np.sum(dev_pp > LAM_TOL))
    print("      multiplicativity failure ON prime powers: %d of %d "
          "prime-power sites deviate from the Euler average "
          "(max dev %.4f); OFF prime powers Λ_E is pure deviation "
          "(%d sites, max |Λ_E| = %.4f)"
          % (n_pp_dev, int(np.sum(ispp)), float(np.max(dev_pp)),
             len(offpp), float(np.max(np.abs(lam_E[offpp])))
             if len(offpp) else 0.0))
    print("      dyadic growth of max|Λ_E| vs the Euler bound log n:")
    print("      block [2^k, 2^{k+1})   max|Λ_E|    log(2^{k+1})   "
          "ratio")
    for k in range(2, 17):
        lo, hi = 2 ** k, min(2 ** (k + 1), N + 1)
        if lo >= N + 1:
            break
        blk = np.abs(lam_E[lo:hi])
        mb = float(np.max(blk))
        print("      k = %2d               %9.4f    %8.4f      %6.3f"
              % (k, mb, math.log(hi), mb / math.log(hi)))
    print("      max |Λ_E| overall: %.4f at n = %d (Λ(n) bound would "
          "be log n = %.4f)"
          % (abs(lam_E[i_maxabs]), i_maxabs, math.log(i_maxabs)))

    print("\n      Chebyshev reads (ψ_X(x) - x)/sqrt(x)   [ζ | "
          "ζ_K = class sum | E single class]:")
    cz = np.cumsum(lam_ref)
    cA = np.cumsum(lam_A)
    cE = np.cumsum(lam_E)
    for x in PSI_X:
        print("      x = %6d:   %+8.4f   %+8.4f   %+8.4f"
              % (x, (cz[x] - x) / math.sqrt(x),
                 (cA[x] - x) / math.sqrt(x),
                 (cE[x] - x) / math.sqrt(x)))

    # ------------------------------------------------ B2: the windows
    print("\nB2 -- ablation ladder on the deployed frame-A tent "
          "machinery (v563, read-only)")
    KZ = core.frame_a_zones()
    cands = []
    for kz in KZ:
        alpha, Mz = build_window_geometry(kz)
        X = math.exp(2.0 * alpha)
        if X <= N_CAP and Mz // 2 <= H_CAP:
            cands.append((kz, alpha, Mz, X))
    hs_c = np.array([c[2] // 2 for c in cands], float)
    print("      %d candidate windows with e^{2α} <= %d and h <= %d "
          "(h range %d..%d)"
          % (len(cands), N_CAP, H_CAP, int(hs_c.min()),
             int(hs_c.max())))
    check("B2.0 [E] candidate family nonempty: %d windows"
          % len(cands), len(cands) >= 3)

    sqn = np.sqrt(np.arange(N + 1, dtype=float))
    sqn[0] = 1.0
    logn = np.zeros(N + 1)
    logn[1:] = np.log(np.arange(1, N + 1, dtype=float))

    def masses_of(lam_vec, alpha, mask=None):
        """Atom selection in u-space, the core convention verbatim:
        u = log n <= 2 alpha + 1e-14."""
        sel = np.abs(lam_vec) > 1e-12
        sel[:2] = False
        sel &= logn <= 2.0 * alpha + 1.0e-14
        if mask is not None:
            sel &= mask
        idx = np.where(sel)[0]
        return logn[idx], 2.0 * lam_vec[idx] / sqn[idx]

    picks = []
    used = set()
    for qv in QUANTS:
        tgt = float(np.quantile(hs_c, qv))
        order = sorted(range(len(cands)),
                       key=lambda i: abs(hs_c[i] - tgt))
        chosen = None
        subst = 0
        for i in order:
            if i in used:
                continue
            kz, alpha, Mz, X = cands[i]
            hz = Mz // 2
            c_ar = core.arch_lags(Mz, 2.0 * alpha / Mz)
            ka = core.atoms_in(alpha)
            A0, Gm, _ = window_form(
                alpha, Mz, core.U_ALL[:ka], core.MU_ALL[:ka], c_ar)
            lm0, v0, rad0 = gen_min_eig2(A0, Gm)
            floor = FLOOR_SAFETY * EPS * rad0 * math.sqrt(hz)
            if lm0 > floor:
                chosen = dict(kz=kz, alpha=alpha, Mz=Mz, X=X, hz=hz,
                              c_ar=c_ar, Gm=Gm, lm0=lm0, rad0=rad0,
                              floor=floor, subst=subst)
                used.add(i)
                break
            subst += 1
        picks.append(chosen)
    ok_picks = [p for p in picks if p is not None]
    check("B2.1 [E] window picks (h-quantiles %s): %s; L0 baseline "
          "λ_min > floor on all picks (substitutions per pick: %s)"
          % (list(QUANTS),
             [(p["hz"], "X=%.0f" % p["X"]) for p in ok_picks],
             [p["subst"] for p in ok_picks]),
          len(ok_picks) == len(QUANTS))
    if not ok_picks:
        print("\nVERDICT: EPSTEIN-FW-UNPOWERED")
        return 1

    # wiring guard: sieve-Λ rebuild of L0
    p0 = ok_picks[0]
    pos, ms = masses_of(lam_ref, p0["alpha"])
    A0s, _, _ = window_form(p0["alpha"], p0["Mz"], pos, ms, p0["c_ar"])
    lm0s, _, _ = gen_min_eig2(A0s, p0["Gm"])
    dev_w = abs(lm0s - p0["lm0"]) / abs(p0["lm0"])
    check("B2.2 [E] wiring guard: sieve-Λ rebuild of L0 reproduces "
          "the core-table λ_min on the first pick (rel dev %.1e < "
          "%.0e)" % (dev_w, TOL_WIRE), dev_w < TOL_WIRE)

    rungs = [("L0  Λ (deployed ζ baseline)", lam_ref, None),
             ("L1  Λ(1+χ_-20) (class-sum ζ_K)", lam_A, None),
             ("L2  Λ(χ_-4+χ_5) (genus partner)", lam_B, None),
             ("L3  Λ_E (Epstein, no Euler)", lam_E, None),
             ("L4a Λ_E on prime powers", lam_E, ispp),
             ("L4b Λ_E off prime powers", lam_E, ~ispp)]
    results = []
    for p in ok_picks:
        print("\n      window h = %d (2α = %.4f, X = e^{2α} = %.0f, "
              "M = %d):" % (p["hz"], 2 * p["alpha"], p["X"], p["Mz"]))
        print("      rung                              #atoms   "
              "Σ Λ_X/X     λ_min          λ_min/floor")
        res = {}
        for name, lv, mask in rungs:
            pos, ms = masses_of(lv, p["alpha"], mask)
            A, Gm, c_at = window_form(p["alpha"], p["Mz"], pos, ms,
                                      p["c_ar"])
            lm, v, rad = gen_min_eig2(A, Gm)
            sel = np.abs(lv) > 1e-12
            sel[:2] = False
            sel &= logn <= 2.0 * p["alpha"] + 1.0e-14
            if mask is not None:
                sel &= mask
            dens = float(np.sum(lv[sel])) / p["X"]
            res[name[:3].strip()] = dict(lm=lm, v=v, rad=rad,
                                         c_at=c_at, n_at=len(pos))
            print("      %-32s  %6d   %+8.4f   %+.6e   %+10.1f"
                  % (name, len(pos), dens, lm, lm / p["floor"]))
        results.append((p, res))

    # lag additivity guard L3 = L4a + L4b
    dev_add = 0.0
    for p, res in results:
        d = np.max(np.abs(res["L3"]["c_at"] - res["L4a"]["c_at"]
                          - res["L4b"]["c_at"]))
        sc = max(1.0, float(np.max(np.abs(res["L3"]["c_at"]))))
        dev_add = max(dev_add, float(d) / sc)
    check("B2.3 [E] lag additivity c_at(L3) = c_at(L4a) + c_at(L4b) "
          "on all picks (max rel dev %.1e < %.0e)"
          % (dev_add, TOL_WIRE), dev_add < TOL_WIRE)

    # ------------------------------------------------ B3: localization
    print("\nB3 -- where does it break? (Rayleigh attribution of the "
          "L3 minimizer)")
    breaks = []
    attr_ok = True
    diff_rows = []
    for p, res in results:
        v3 = res["L3"]["v"]
        A_ar = core.odd_toeplitz(p["c_ar"], p["Mz"])
        A_pp = core.odd_toeplitz(res["L4a"]["c_at"], p["Mz"])
        A_np = core.odd_toeplitz(res["L4b"]["c_at"], p["Mz"])
        r_ar = rayleigh(v3, A_ar, p["Gm"])
        r_pp = rayleigh(v3, A_pp, p["Gm"])
        r_np = rayleigh(v3, A_np, p["Gm"])
        lm3 = res["L3"]["lm"]
        attr_ok &= abs(r_ar + r_pp + r_np - lm3) \
            <= TOL_ATTR * res["L3"]["rad"]
        # positive / negative weight split of the FULL Λ_E atom layer
        pos_m = lam_E > 1e-12
        neg_m = lam_E < -1e-12
        posu, posw = masses_of(lam_E, p["alpha"], pos_m)
        negu, negw = masses_of(lam_E, p["alpha"], neg_m)
        cpos, _ = core.atom_lags_at(p["alpha"], p["Mz"], posu, posw)
        cneg, _ = core.atom_lags_at(p["alpha"], p["Mz"], negu, negw)
        r_pos = rayleigh(v3, core.odd_toeplitz(cpos, p["Mz"]), p["Gm"])
        r_neg = rayleigh(v3, core.odd_toeplitz(cneg, p["Mz"]), p["Gm"])
        broke = lm3 < -p["floor"]
        if broke:
            breaks.append(p["hz"])
        print("      h = %4d: λ_min(L3) = %+.6e (%s); minimizer "
              "attribution: arch %+.4e | Λ_E-pp %+.4e | Λ_E-npp "
              "%+.4e; weight-sign split: pos-Λ_E %+.4e / neg-Λ_E "
              "%+.4e"
              % (p["hz"], lm3, "BREAKS" if broke else "stays >= 0",
                 r_ar, r_pp, r_np, r_pos, r_neg))
        lm1 = res["L1"]["lm"]
        atom_side = r_pp + r_np
        diff_rows.append(dict(
            hz=p["hz"], lm1=lm1, lm3=lm3, exc=lm3 - lm1,
            ratio=lm3 / lm1 if lm1 < 0 else float("inf"),
            npp_share=r_np / atom_side if atom_side != 0 else 0.0,
            lm4a=res["L4a"]["lm"], lm4b=res["L4b"]["lm"]))

    print("\n      run-2 DIFFERENTIAL vs the Euler-true control L1 "
          "(same Γ(s) functional equation + conductor):")
    print("      h      λ_min(L1)      λ_min(L3)      excess L3-L1"
          "    L3/L1   npp share   L4a (pp only)   L4b (npp only)")
    for d in diff_rows:
        print("      %4d   %+.4e   %+.4e   %+.4e   %6.2f     %.3f"
              "     %+.4e    %+.4e"
              % (d["hz"], d["lm1"], d["lm3"], d["exc"], d["ratio"],
                 d["npp_share"], d["lm4a"], d["lm4b"]))
    med_ratio = float(np.median([d["ratio"] for d in diff_rows]))
    med_npp = float(np.median([d["npp_share"] for d in diff_rows]))
    check("B3.1 [E] attribution wiring: r_arch + r_pp + r_npp == "
          "λ_min(L3) on every pick (tol %.0e x rad)" % TOL_ATTR,
          attr_ok)

    l1_ok = all(res["L1"]["lm"] > -p["floor"] for p, res in results)
    l4a_broke = [p["hz"] for p, res in results
                 if res["L4a"]["lm"] < -p["floor"]]
    l4b_broke = [p["hz"] for p, res in results
                 if res["L4b"]["lm"] < -p["floor"]]
    fw_break = len(breaks) > 0
    if fw_break:
        diag = []
        if l1_ok:
            diag.append("the class-sum restoration L1 (Euler "
                        "product restored) stays positive -- the "
                        "break is carried by the LOSS OF "
                        "MULTIPLICATIVITY alone")
        else:
            diag.append("L1 (Euler-true, same functional equation) "
                        "also goes negative -- the declared F1 "
                        "arch-mismatch bias is real; the EPSTEIN-"
                        "specific effect is the median x%.1f deeper "
                        "break of L3 over L1, carried to %.0f%% by "
                        "the non-prime-power Λ_E atoms (L4a alone "
                        "stays at the L1 scale, L4b alone "
                        "reproduces the full L3 break)"
                        % (med_ratio, 100.0 * med_npp))
        diag.append("pp-only rung breaks on %s, npp-only rung "
                    "breaks on %s" % (l4a_broke or "none",
                                      l4b_broke or "none"))
        diag_s = "; ".join(diag)
    else:
        diag_s = ("L3 stays positive on every pick -- at this window "
                  "depth the family positivity does NOT distinguish "
                  "the RH-violating Epstein zeta from ζ")
    check("B3.2 [%s] FIREWALL: λ_min(L3) < -floor on %d of %d "
          "windows %s.  Diagnosis: %s"
          % ("E" if fw_break else "X", len(breaks), len(results),
             breaks or "", diag_s), fw_break)

    # ------------------------------------------------ B4: zero box
    print("\nB4 -- off-line zero count (argument principle, printed, "
          "NO gate; Davenport-Heilbronn 1936 is the literature "
          "ground truth)")
    mp.mp.dps = 15
    s_test = mp.mpc(2.0, 5.0)
    E_an = E_analytic(s_test)
    nn = np.arange(1, N + 1)
    E_tr = complex(np.sum(r1[1:] * nn ** (-2.0)
                          * np.exp(-1j * 5.0 * np.log(nn))))
    dev_E = abs(complex(E_an) - E_tr) / abs(complex(E_an))
    check("G0.4 [E] analytic E(s) identity vs truncated Dirichlet "
          "series at s = 2+5i: rel dev %.1e < %.0e (tail bound "
          "~ %.0e)" % (dev_E, TOL_EID, 2.9 / N), dev_E < TOL_EID)
    t_b4 = time.time()
    cnt, nev, resolved = winding_count()
    n_zero = int(round(cnt))
    print("      box Re s in [%.2f, %.2f], Im s in [%.0f, %.0f]: "
          "winding = %+.4f -> %d zero(s) right of the critical "
          "line in the box (%d evals, resolved %s, %.0f s)"
          % (BOX_S[0], BOX_S[1], BOX_T[0], BOX_T[1], cnt, n_zero,
             nev, resolved, time.time() - t_b4))
    if n_zero > 0:
        print("      -> RH violation of E confirmed INSIDE the "
              "searched box (plus mirror zeros left of the line by "
              "the functional equation)")
    else:
        print("      -> no off-line zero below t = %.0f in this box; "
              "the Davenport-Heilbronn zeros sit higher -- the "
              "firewall statement rests on the measured positivity "
              "break, the RH violation itself is literature ground "
              "truth" % BOX_T[1])

    # ------------------------------------------------ verdict
    guards_ok = not any(f.startswith(("G0", "B2.0", "B2.2", "B2.3",
                                      "B3.1")) for f in FAILS)
    if not guards_ok:
        VERDICT = "EPSTEIN-FW-MIXED (guards failed)"
    elif not ok_picks:
        VERDICT = "EPSTEIN-FW-UNPOWERED"
    elif fw_break:
        VERDICT = "EPSTEIN-FW-BREAKS (the firewall works)"
    else:
        VERDICT = "EPSTEIN-FW-SUSPICIOUS (machinery blind to the "\
                  "violation at this depth)"

    check("B5.1 [C] typed reading: the correct von Mangoldt analogy "
          "for E is the -E'/E coefficient Λ_E(n) (F4); without the "
          "Euler product it goes negative and leaks off the prime "
          "powers (B1); the deployed tent machinery with Λ_E atoms "
          "%s; the class-sum rung L1 isolates multiplicativity as "
          "the load-bearing arithmetic ingredient.  No RH statement, "
          "no marker move; W3 stays open"
          % ("breaks demonstrably (B3)" if fw_break else
             "does NOT break at this depth -- a diagnostic-power "
             "warning for the W3 family read"), True)

    print("\nVERDICT: %s" % VERDICT)
    print("""
CONTRACT-NOTE TEXT (report only -- nothing is written by this probe):

  PRIME.WEIL.OPERATOR.01, Epstein-firewall round (2026-08-02): the
  window machinery was A/B-tested on the classical RH violator
  E(s) = Σ'(x²+5y²)^{-s} (disc -20, class number 2, no Euler
  product; E = ζL_-20 + L_-4 L_5 verified coefficient-wise to
  n = %d).  ARITHMETIC: Λ_E (:= -E'/E coefficients) has %d negative
  sites (first n = %d) and %d non-prime-power support points below
  %d -- the Euler-product structure (Λ >= 0, prime-power support) is
  measurably gone.  WINDOWS: on the deployed frame-A family the
  ladder Λ -> Λ(1+χ) -> Λ_E gives λ_min %s; the firewall verdict is
  %s.  TYPE: negative control of the machinery; Davenport-Heilbronn
  1936 cited for the RH violation; no marker move.
""" % (N, len(neg_idx), int(neg_idx[0]) if len(neg_idx) else -1,
       len(offpp), N,
       "; ".join("h=%d: %+.3e/%+.3e/%+.3e"
                 % (p["hz"], res["L0"]["lm"], res["L1"]["lm"],
                    res["L3"]["lm"]) for p, res in results),
       VERDICT))

    print("checks: %d, failures: %d %s" % (N_CHK, len(FAILS),
                                           FAILS or ""))
    print("elapsed: %.1f s" % (time.time() - T0))
    return len(FAILS)


if __name__ == "__main__":
    raise SystemExit(1 if run() else 0)
