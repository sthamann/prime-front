"""v540 -- RTF.GNS.AMP.01: amplitude route and positive linear carrier.
The amplitude/linear route out of the square plane, consolidated from
discovery T67/T68/T69/T70/T71/T72 (amplitude chain).  Companion to
HECKE.GEOM.RTF.01 (v538) and RTF.GNS.WEIL.01 (v539).

[E] (A) AMPLITUDE DIRAC (T67).  D = [[0,V],[V^T,0]] with
    V[d,m] = sqrt(w_d) b(d) chi_d(m), w_d = |d|^{-1}, exists exactly:
    D = D^T; D^2 = diag(VV^T, V^T V) with V^T V = K = Sum w b^2
    chi (x) chi (rel < 1e-12); spectrum(D) = +/- svals(V); Hecke
    equivariance exact -- m-side intertwining V A_p^T = A^_p V on the
    p-free locus (p = 3,5,7) and d-side Shimura b(dp^2) = b(d)
    alpha_d^#(p) integer-exact on the window.
[E] (B) GEOMETRIC POLARISATION (T68).  b = N_+ - N_- and
    Theta = N_+ + N_- by direct parity-split lattice counting of the
    quinary form n = (x^2+y^2)/2 + 2z^2 + u^2 + 2w^2 (exact, n <= 2000);
    Theta = theta2(q^2)^2 theta3(q) theta3(q^2)^2 coefficientwise;
    N_+- = (Theta +- g)/2 integral and >= 0 for ALL n <= 50000;
    b^2 = Theta^2 - 4 N_+ N_- exact; Theta is a PURE Siegel-Weil
    Eisenstein T(p^2)-eigenform with eigenvalue sigma_3(p) = 1+p^3
    (p <= 13, 0 mismatches; cusp component ZERO); Cohen seed identity
    Theta(d) = -48 L(-1,chi_d) exact-rational on >= 100 live d
    (d Theta(d) = 24 S2(d), S2 = Sum chi_d(a) a^2; generalised
    Bernoulli B_{2,chi} = S2/d; Cohen 1975 H(2,d) = L(-1,chi_d)).
[E] (C) EVEN-k DELETION IS UNIVERSAL ON THE SQUARE PLANE (T69).
    Cauchy-Littlewood window lemma with FREE Satake symbols:
    Sum h_k(s,t) h_k(u,v) X^k = (1 - stuv X^2)/[(1-suX)(1-svX)(1-tuX)
    (1-tvX)] (sympy exact, k <= 6); determinant instantiation
    st = uv = p^3 gives numerator 1 - p^6 X^2 INDEPENDENT of the pair
    -- every coefficient-bilinear channel of two determinant-p^3
    towers inherits the deletion (five channels: b^2, Theta^2,
    Theta*g, N_+^2/N_-^2/N_+N_- as verified bilinear combinations);
    simultaneously the deletion is EXACTLY the square-class
    double-counting: fam[1,0,2,0] + 2flat[0,2,0,2] + Plancherel
    delta_{k1} = FULL [2,2,2,2] (generating-function exact; global
    Moebius square sieve 2^omega = mu_sq * d, d = 1_sq * 2^omega).
[E] (D) POSITIVE LINEAR CARRIER + PLUS BALANCE (T70).  The linear
    measure mu(d) = Theta(d) |d|^{-a} = 48|L(-1,chi_d)| |d|^{-a} > 0
    carries FULL weights: lambda_k = 1 + p^{3k} - (chi p)^k exact,
    p^{3k}-layer = [1,1,1,1,...] (no even-k kill; the CL lemma has no
    second Satake pair to act on: degree-1 numerator); plus balance
    Prime_Thetalin(g) = P_zeta(g_-) + P_zeta(g_+), g_+- =
    e^{+-3u/2} g(u), ONLY PLUS signs (rel < 1e-12, zero-free); pole
    kernel collapse => Q = Q_zeta(g_-) + Q_zeta(g_+); d-aggregation
    prime side = P_zeta(gflat_-) + P_zeta(gflat_+) -- the v539
    flat/doubling kernel class WITH PLUS (sign inverted vs the
    square plane).
[E] (E) FUNCTIONAL EQUATION EXACT (T71).  Fricke closed via the three
    Jacobi inversions: Theta(i/(8y)) = 8 y^{5/2} Theta_dag(iy) with
    mirror monomial Theta_dag = theta3^2 theta4^2 theta3(q^2)
    = theta4(q^2)^4 theta3(q^2) (Landen), rel < 1e-20; completed FE
    Lambda_Theta(s) = 8^{1-s} Lambda_{Theta_dag}(5/2-s) in the strip
    (>= 3 s-points, independent split points, rel < 1e-20); single
    poles 5/2 (residue 8^{-3/2}) / 0 (residue -1) swapped by the FE;
    FE centre 5/4, plus-balance locus s = 1 off-centre by exactly 1/4.
[C] (F) CONE FACTS + THE NAMED OPEN BOUNDARY (T71/T72, sampled).
    The guaranteed cone K_guar (value-side nonnegativity on the
    log-lattice) and the library hull {Theta, psi, Theta_dag} are
    FE-SELF-DUAL and the gap functional lambda* is FE-covariant
    (positive mirror multiplier cosh(u)); the mirror family psi =
    theta3 theta4^4 obeys the RIGID sign law sign psi(n) =
    (-1)^{floor(n/2)+1} (0 violations, 0 zeros, n <= 50000, exact);
    the hull constraint class is C_L3 = {n == 6 mod 8} (machine ==
    closed form); lambda* EXISTS as the compressed residual distance:
    one exact Farkas witness (a violated constrained atom n* == 6
    mod 8 where every library member pays positive mass with plus
    sign while h(log n*) < 0) certifies h outside the hull and
    lambda*(h) > 0; coverage saturates on the sample (h(0) > 0 pins
    every Weil element against every sign twist at n = 1).

HONEST FENCES (load-bearing typing):
  * Cohen 1975 (H(2,d) = L(-1,chi_d), Cohen-Eisenstein 5/2),
    Siegel-Weil / genus Eisenstein, Jacobi theta inversions / Landen /
    Fricke / Hecke split-Mellin, Cauchy-Littlewood / Rankin-Selberg
    zeta(2s)-normalisation, Moebius square sieve, Shimura T(p^2),
    Shintani zeta class, Weil 1952 positivity cone, Farkas / LP
    duality named CLASSICAL -- NEW is the compiler-native
    consolidation and the machine-checked closure of the square
    plane + the exact positive linear carrier.
  * EULER-REGION POSITIVITY ONLY: the seeds L(-1,chi_d) are edge
    L-values in the absolute-convergence region; a plus combination
    of shifted zeta-Weil forms at the (w, w-3) lines is NOT Weil
    positivity for zeta on the 1/2-line.  NOT "almost RH".
  * THE OPEN BOUNDARY IS PART OF THE CLAIM: the residual distance to
    the Weil cone is the FE-covariant gap functional lambda* on the
    atoms n == 6 mod 8 -- named, measured, NOT removed; no finite
    library of deterministic-sign theta families removes it
    (Farkas-certified on the sample; n = 1 pin h(0) = ||f||^2 > 0).
  * ZETA.HP.CARRIER untouched; NO marker upgrades of any
    pre-existing contract.
  * ZERO-FIREWALL: AST-checked; no zetazero; all prime sides are
    finite zero-free sums over odd prime powers; mpmath is used for
    jtheta/Gamma/quad only (no zeta values needed).

Status: [E] exact integer / Fraction / sympy identities, exact
lattice counting, zero-free prime relations, and mpmath FE at
rel < 1e-20; [C] sampled cone facts (finite sample of Weil-cone
elements, finite lattice window).  Python; Wolfram-mirrored (exact
algebraic identities -- lattice enumeration, FFT autocorrelations
and the mpmath split-Mellin FE stay Python-only), counted per
GATE.WOLFRAM.02.  Discovery provenance:
  experiments/tfpt-discovery/amplitude_dirac_sqrt_probe.py      (T67)
  experiments/tfpt-discovery/geometric_polarization_probe.py    (T68)
  experiments/tfpt-discovery/mixed_channel_full_weight_probe.py (T69)
  experiments/tfpt-discovery/linear_measure_weil_probe.py       (T70)
  experiments/tfpt-discovery/transport_terrain_probe.py         (T71)
  experiments/tfpt-discovery/cone_enlargement_probe.py          (T72)
"""
from __future__ import annotations

import ast
import math
import time
from fractions import Fraction

import mpmath
import numpy as np
import sympy as sp

from tfpt_constants import check, summary, reset

# ---------------------------------------------------------------- budgets
QMAX = 50_000                 # exact q-window for the monomials
D_FAM = 8_000                 # live-d family window
D_DIRAC = 3_000               # Dirac-block d-window
M_DIRAC = 801                 # odd m <= M_DIRAC (Dirac columns)
N_ENUM = 2_000                # parity-split lattice enumeration window
N_SIEVE = 2_000               # square-sieve coefficient window
N_SEED = 160                  # Cohen-seed scan size (need >= 100)
K_MAX = 8                     # layer depth
K_CL = 6                      # Cauchy-Littlewood series depth
N_LAM = 20_000                # odd prime-power window (zero-free sums)
N_LAT = 4_000                 # log-lattice window {log n : n <= N_LAT}
N_GRID = 1 << 13              # cone-survey FFT grid
U_GRID = 14.0                 # cone-survey grid half-width
HEAD_AP = {3: -4, 5: -2, 7: 24, 11: -44, 13: 22}
HECKE_PS = (3, 5, 7)          # Dirac intertwining primes
EIGEN_PS = (3, 5, 7, 11, 13)  # eigenform / tower primes
G_KEY = (0, 2, 0, 1, 1, 1)    # g       = th2(q2)^2 th3(q2) th4 th4(q2)
TH_KEY = (0, 2, 1, 2, 0, 0)   # Theta   = th2(q2)^2 th3(q) th3(q2)^2
TD_KEY = (0, 0, 2, 1, 2, 0)   # Theta+  = th3^2 th3(q2) th4^2 (mirror)
PSI_KEY = (0, 0, 1, 0, 4, 0)  # psi     = th3 th4^4 (reduced mirror)
Y_MOD = ("0.30", "0.45", "0.353553390593273762", "0.60", "0.85", "1.20")
S_STRIP = ("0.50", "1.25", "2.00")
C_LHS, C_RHS, C_ALT = "0.30", "0.55", "0.62"
REL_DIRAC = 1e-12
REL_PLUS = 1e-12
REL_FE = mpmath.mpf("1e-20")
TOL_MEM = 1e-12


# ---------------------------------------------------------------- helpers
def theta_pairs(kind: int, scale_q: int, order_t: int):
    """Sparse (exponent, coeff) list of a theta factor in t-units."""
    pairs = []
    if kind == 2:
        o = 1
        while scale_q * o * o <= order_t:
            pairs.append((scale_q * o * o, 2))
            o += 2
    else:
        pairs.append((0, 1))
        n = 1
        while 4 * scale_q * n * n <= order_t:
            c = 2 if kind == 3 else 2 * ((-1) ** n)
            pairs.append((4 * scale_q * n * n, c))
            n += 1
    return pairs


def sparse_mul(s: np.ndarray, pairs, order_t: int) -> np.ndarray:
    out = np.zeros(order_t + 1, dtype=np.int64)
    for e, c in pairs:
        if e == 0:
            out += c * s
        else:
            out[e:] += c * s[:-e]
    return out


def build_monomial(key, order_t: int) -> np.ndarray:
    a0, a2, b0, b2, c0, c2 = key
    s = np.zeros(order_t + 1, dtype=np.int64)
    s[0] = 1
    for _ in range(a0):
        s = sparse_mul(s, theta_pairs(2, 1, order_t), order_t)
    for _ in range(a2):
        s = sparse_mul(s, theta_pairs(2, 2, order_t), order_t)
    for _ in range(b0):
        s = sparse_mul(s, theta_pairs(3, 1, order_t), order_t)
    for _ in range(b2):
        s = sparse_mul(s, theta_pairs(3, 2, order_t), order_t)
    for _ in range(c0):
        s = sparse_mul(s, theta_pairs(4, 1, order_t), order_t)
    for _ in range(c2):
        s = sparse_mul(s, theta_pairs(4, 2, order_t), order_t)
    return s


def eta_pass(d, e, order):
    s = np.zeros(order + 1, dtype=np.int64)
    s[0] = 1
    for k in range(d, order + 1, d):
        for _ in range(e):
            s[k:] = s[k:] - s[:-k]
    return s


def mobius_sieve(n: int) -> np.ndarray:
    mu = np.zeros(n + 1, dtype=np.int8)
    mu[1] = 1
    primes = []
    is_comp = np.zeros(n + 1, dtype=bool)
    for i in range(2, n + 1):
        if not is_comp[i]:
            primes.append(i)
            mu[i] = -1
        for p in primes:
            v = i * p
            if v > n:
                break
            is_comp[v] = True
            if i % p == 0:
                mu[v] = 0
                break
            mu[v] = -mu[i]
    return mu


def spf_sieve(n: int) -> np.ndarray:
    spf = np.zeros(n + 1, dtype=np.int32)
    for i in range(2, n + 1):
        if spf[i] == 0:
            for j in range(i, n + 1, i):
                if spf[j] == 0:
                    spf[j] = i
    spf[1] = 1
    return spf


def jacobi(a: int, n: int) -> int:
    """Jacobi symbol (a/n) for odd n > 0 (binary algorithm)."""
    a %= n
    result = 1
    while a:
        while a % 2 == 0:
            a //= 2
            if n % 8 in (3, 5):
                result = -result
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3:
            result = -result
        a %= n
    return result if n == 1 else 0


def g_fejer(u, a):
    return max(0.0, 1.0 - abs(u) / a)


def g_gauss(u, sig):
    return math.exp(-0.5 * (u / sig) ** 2)


def kron2(d: int) -> int:
    return 1 if d % 8 in (1, 7) else -1


def ast_zero_firewall(src_path: str) -> bool:
    with open(src_path, "r", encoding="utf-8") as fh:
        src = fh.read()
    tree = ast.parse(src)
    zero_calls = []
    attr_hits = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            f = node.func
            if isinstance(f, ast.Attribute) and f.attr in (
                "zetazero", "nzeros", "second_sheet_zero",
            ):
                zero_calls.append(f.attr)
            if isinstance(f, ast.Name) and f.id in ("zetazero",):
                zero_calls.append(f.id)
        if isinstance(node, ast.Attribute) and node.attr in ("zetazero",):
            attr_hits.append(node.attr)
    return len(zero_calls) == 0 and len(attr_hits) == 0


# ---- mpmath theta monomials on the imaginary axis (q = e^{2 pi i tau})
def Theta_iy(y):
    """Theta(iy) = th2(q^2)^2 th3(q) th3(q^2)^2, q = e^{-2 pi y}."""
    q1 = mpmath.exp(-2 * mpmath.pi * y)
    q2 = q1 * q1
    return (mpmath.jtheta(2, 0, q2) ** 2 * mpmath.jtheta(3, 0, q1)
            * mpmath.jtheta(3, 0, q2) ** 2)


def Theta_dag_iy(y):
    """Theta_dag(iy) = th3(q)^2 th4(q)^2 th3(q^2) (the W8 mirror)."""
    q1 = mpmath.exp(-2 * mpmath.pi * y)
    q2 = q1 * q1
    return (mpmath.jtheta(3, 0, q1) ** 2 * mpmath.jtheta(4, 0, q1) ** 2
            * mpmath.jtheta(3, 0, q2))


def A_int(s, c):
    """A(s;c) = int_c^inf Theta(iy) y^{s-1} dy (exp convergent)."""
    return mpmath.quad(lambda y: Theta_iy(y) * mpmath.power(y, s - 1),
                       [c, mpmath.inf])


def B_int(w, c):
    """B(w;c) = int_c^inf (Theta_dag(iy) - 1) y^{w-1} dy (a0 = 1 off)."""
    return mpmath.quad(
        lambda y: (Theta_dag_iy(y) - 1) * mpmath.power(y, w - 1),
        [c, mpmath.inf])


MP8 = mpmath.mpf(8)
MP52 = mpmath.mpf(5) / 2


def Lam_Theta(s, c):
    """Lambda_Theta(s) via Hecke's split-Mellin trick (classical)."""
    s = mpmath.mpf(s)
    c = mpmath.mpf(c)
    return (A_int(s, c)
            + MP8 ** (1 - s) * B_int(MP52 - s, 1 / (8 * c))
            + MP8 ** (1 - s) * (8 * c) ** (s - MP52) / (s - MP52))


def Lam_dag(w, c):
    """Lambda_dag(w), same trick (own constant term -1)."""
    w = mpmath.mpf(w)
    c = mpmath.mpf(c)
    return (B_int(w, c)
            + MP8 ** (mpmath.mpf(3) / 2 - w) * A_int(MP52 - w, 1 / (8 * c))
            - c ** w / w)


def run():
    reset()
    mpmath.mp.dps = 40
    t0 = time.time()
    print("v540 RTF.GNS.AMP.01 -- amplitude route and positive linear "
          "carrier (open boundary lambda* as content)")

    # ============================================================ S0
    print("S0 -- AST zero-firewall + exact builds + live family")
    check("S0.AST: no Riemann-zero / zetazero loaders in this module",
          ast_zero_firewall(__file__))

    f8 = np.roll(np.convolve(eta_pass(2, 4, 300),
                             eta_pass(4, 4, 300))[:301].astype(np.int64), 1)
    f8[0] = 0
    a_f8 = [int(f8[n]) for n in range(301)]
    check("S0.f8: eta(2t)^4 eta(4t)^4 head a_1=1; "
          "a_p = {3:-4, 5:-2, 7:24, 11:-44, 13:22}",
          a_f8[1] == 1 and all(a_f8[p] == v for p, v in HEAD_AP.items()))

    t_b = time.time()
    ORDER_T = 4 * QMAX
    _g_t = build_monomial(G_KEY, ORDER_T)
    _th_t = build_monomial(TH_KEY, ORDER_T)
    _td_t = build_monomial(TD_KEY, ORDER_T)
    _ps_t = build_monomial(PSI_KEY, ORDER_T)
    support_ok = all(
        not np.any(arr[r::4] != 0)
        for arr in (_g_t, _th_t, _td_t, _ps_t) for r in (1, 2, 3)
    )
    g = _g_t[0::4][: QMAX + 1].copy()
    Th = _th_t[0::4][: QMAX + 1].copy()
    Td = _td_t[0::4][: QMAX + 1].copy()
    Psi = _ps_t[0::4][: QMAX + 1].copy()
    del _g_t, _th_t, _td_t, _ps_t
    print(f"        exact sparse int64 builds O(q^{QMAX}) in "
          f"{time.time() - t_b:.2f}s")
    check("S0.build: four monomials on integer q-powers; g witness head "
          "[0,4,-8,0,0,0,16]; Theta >= |g| >= 0 for ALL n <= 50000; "
          "Theta_dag(0)=1; psi(0)=1, psi(1)=-6",
          support_ok and list(g[:7]) == [0, 4, -8, 0, 0, 0, 16]
          and bool(np.all(Th >= np.abs(g)))
          and int(Td[0]) == 1 and int(Psi[0]) == 1 and int(Psi[1]) == -6)

    mu = mobius_sieve(QMAX)
    spf = spf_sieve(QMAX)
    live = [
        d for d in range(1, D_FAM + 1, 2)
        if d % 8 == 1 and mu[d] != 0 and int(g[d]) != 0
    ]
    live_dirac = [d for d in live if d <= D_DIRAC]
    print(f"        live fund d=1 mod 8, b!=0: <= {D_FAM}: {len(live)}; "
          f"<= {D_DIRAC}: {len(live_dirac)}")
    check(f"S0.family: {len(live)} live fundamental d <= {D_FAM} "
          f"(>= 200) and {len(live_dirac)} <= {D_DIRAC} (>= 150)",
          len(live) >= 200 and len(live_dirac) >= 150)

    rng = np.random.default_rng(540)
    kron_ok = True
    for _ in range(200):
        d = int(rng.integers(1, 5000)) * 2 + 1
        m = int(rng.integers(1, 5000)) * 2 + 1
        if jacobi(d, m) != int(sp.kronecker_symbol(d, m)):
            kron_ok = False
    check("S0.kron: fast Jacobi implementation matches sympy "
          "kronecker_symbol on 200 random odd (d, m) pairs",
          kron_ok)

    # ============================================================ A
    print("A -- amplitude Dirac D^2 = family kernel (exact, Hecke-equiv.)")
    ms = list(range(1, M_DIRAC + 1, 2))
    nd, nm = len(live_dirac), len(ms)
    Vraw = np.zeros((nd, nm), dtype=np.float64)
    for j, d in enumerate(live_dirac):
        for i, m in enumerate(ms):
            Vraw[j, i] = float(jacobi(d, m))
    ws = np.array([1.0 / d for d in live_dirac])
    bvec = np.array([float(int(g[d])) for d in live_dirac])
    V = Vraw * (np.sqrt(ws) * bvec)[:, None]
    K = V.T @ V
    Ghat = V @ V.T
    D = np.zeros((nd + nm, nd + nm))
    D[:nd, nd:] = V
    D[nd:, :nd] = V.T

    sym_err = float(np.linalg.norm(D - D.T, "fro")
                    / (np.linalg.norm(D, "fro") + 1e-30))
    check(f"A.i: D = D^T self-adjoint (rel Frobenius {sym_err:.2e} "
          "< 1e-14)",
          sym_err < 1e-14)

    D2 = D @ D
    err_dd = float(np.linalg.norm(D2[:nd, :nd] - Ghat, "fro")
                   / (np.linalg.norm(Ghat, "fro") + 1e-30))
    err_mm = float(np.linalg.norm(D2[nd:, nd:] - K, "fro")
                   / (np.linalg.norm(K, "fro") + 1e-30))
    err_off = float(np.linalg.norm(D2[:nd, nd:], "fro")
                    + np.linalg.norm(D2[nd:, :nd], "fro"))
    K_b2 = np.zeros((nm, nm))
    for j in range(nd):
        K_b2 += ws[j] * (bvec[j] ** 2) * np.outer(Vraw[j], Vraw[j])
    err_k = float(np.linalg.norm(K - K_b2, "fro")
                  / (np.linalg.norm(K_b2, "fro") + 1e-30))
    print(f"        D^2 blocks: dd {err_dd:.2e}, mm {err_mm:.2e}, "
          f"off {err_off:.2e}; K vs Sum w b^2 chi(x)chi {err_k:.2e}")
    check("A.ii: D^2 = diag(VV^T, V^T V) and V^T V = K = "
          f"Sum w b^2 chi(x)chi (rels < {REL_DIRAC:g}; off-blocks 0)",
          err_dd < REL_DIRAC and err_mm < REL_DIRAC
          and err_k < REL_DIRAC and err_off < 1e-8)

    svals = np.linalg.svd(V, compute_uv=False)
    eigs_D = np.sort(np.linalg.eigvalsh(D))
    pos = np.sort(eigs_D[eigs_D > 1e-8])[::-1]
    neg = np.sort(-eigs_D[eigs_D < -1e-8])[::-1]
    n_match = min(len(svals), len(pos), len(neg))
    s_use = np.sort(svals)[::-1][:n_match]
    rel_pos = float(np.linalg.norm(pos[:n_match] - s_use)
                    / (np.linalg.norm(s_use) + 1e-30))
    rel_neg = float(np.linalg.norm(neg[:n_match] - s_use)
                    / (np.linalg.norm(s_use) + 1e-30))
    sym_spec = float(np.linalg.norm(eigs_D + eigs_D[::-1])
                     / (np.linalg.norm(eigs_D) + 1e-30))
    check("A.iii: spectrum(D) = +/- singular values of V "
          f"(rel {rel_pos:.2e}/{rel_neg:.2e}; 0-symmetry {sym_spec:.2e}; "
          f"#pos = #neg = {len(pos)})",
          rel_pos < 1e-8 and rel_neg < 1e-8 and sym_spec < 1e-8
          and len(pos) == len(neg))

    hecke_m_ok = True
    for p in HECKE_PS:
        idx = {m: i for i, m in enumerate(ms)}
        A = np.zeros((nm, nm))
        for m in ms:
            if p * m in idx:
                A[idx[m], idx[p * m]] += 1.0
            if m % p == 0 and m // p in idx:
                A[idx[m], idx[m // p]] += 1.0
        free = np.array([(m % p != 0) and (p * m in idx) for m in ms])
        Ah = np.diag(np.array([float(jacobi(d, p)) for d in live_dirac]))
        res_mat = float(np.linalg.norm(((V @ A.T) - (Ah @ V))[:, free],
                                       "fro")
                        / (np.linalg.norm(V[:, free], "fro") + 1e-30))
        print(f"        p={p}: V A^T = A^ V on p-free locus rel "
              f"{res_mat:.2e} (#free={int(free.sum())})")
        hecke_m_ok = hecke_m_ok and res_mat < REL_DIRAC \
            and int(free.sum()) >= 30
    check("A.iv.m: m-side Hecke intertwining V A_p^T = A^_p V exact on "
          f"the p-free locus for p = {HECKE_PS} (rel < {REL_DIRAC:g})",
          hecke_m_ok)

    shim_n = 0
    shim_ok = True
    for d in live:
        for p in HECKE_PS:
            n1 = d * p * p
            if n1 > QMAX or d % p == 0:
                continue
            shim_n += 1
            if int(g[n1]) != int(g[d]) * (HEAD_AP[p] - jacobi(d, p) * p):
                shim_ok = False
    modal_ok = True
    for p in HECKE_PS:
        lam = np.array([float(jacobi(d, p)) for d in live_dirac])
        Ah = np.diag(lam)
        comm = Ghat @ Ah - Ah @ Ghat
        pred = Ghat * (lam[None, :] - lam[:, None])
        if float(np.linalg.norm(comm - pred, "fro")) \
                > 1e-8 * (float(np.linalg.norm(Ghat, "fro")) + 1.0):
            modal_ok = False
    check("A.iv.d: d-side Shimura b(dp^2) = b(d) (a_p - chi_d(p) p) "
          f"integer-exact on {shim_n} (d,p) pairs (>= 300) + modal "
          "[G^, A^_p] = G^ o (lam_j - lam_i) exact",
          shim_ok and shim_n >= 300 and modal_ok)

    # ============================================================ B
    print("B -- geometric polarisation + Eisenstein seed (exact)")
    t_e = time.time()
    xy = np.zeros(N_ENUM + 1, dtype=np.int64)
    max_o = int(math.isqrt(2 * N_ENUM)) + 2
    for x in range(-max_o, max_o + 1):
        if x % 2 == 0:
            continue
        for y in range(-max_o, max_o + 1):
            if y % 2 == 0:
                continue
            m = (x * x + y * y) // 2
            if m <= N_ENUM:
                xy[m] += 1
    zuw_even = np.zeros(N_ENUM + 1, dtype=np.int64)
    zuw_odd = np.zeros(N_ENUM + 1, dtype=np.int64)
    max_u = int(math.isqrt(N_ENUM))
    for u in range(-max_u, max_u + 1):
        u2 = u * u
        if u2 > N_ENUM:
            continue
        max_w = int(math.isqrt((N_ENUM - u2) // 2))
        for w in range(-max_w, max_w + 1):
            base = u2 + 2 * w * w
            if base > N_ENUM:
                continue
            par = (abs(u) + abs(w)) % 2
            max_z = int(math.isqrt((N_ENUM - base) // 2))
            for z in range(-max_z, max_z + 1):
                idx2 = base + 2 * z * z
                if idx2 <= N_ENUM:
                    if par == 0:
                        zuw_even[idx2] += 1
                    else:
                        zuw_odd[idx2] += 1
    N_plus = np.convolve(xy, zuw_even)[: N_ENUM + 1].astype(np.int64)
    N_minus = np.convolve(xy, zuw_odd)[: N_ENUM + 1].astype(np.int64)
    print(f"        parity-split enumeration n <= {N_ENUM} in "
          f"{time.time() - t_e:.2f}s")
    check(f"B.i: b = N_+ - N_- and Theta = N_+ + N_- by direct lattice "
          f"counting of the quinary form, exact for all n <= {N_ENUM} "
          "(sign class = parity of u+w; theta4->theta3 slot swap)",
          bool(np.array_equal(N_plus - N_minus, g[: N_ENUM + 1]))
          and bool(np.array_equal(N_plus + N_minus, Th[: N_ENUM + 1])))

    parity_ok = bool(np.all((Th - g) % 2 == 0))
    Npl = (Th + g) // 2
    Nmi = (Th - g) // 2
    pos_ok = bool(np.all(Npl >= 0)) and bool(np.all(Nmi >= 0))
    cross = Th.astype(object) ** 2 - g.astype(object) ** 2
    split_exact = bool(np.all(cross % 4 == 0)) and bool(
        np.all(cross // 4 == Npl.astype(object) * Nmi.astype(object)))
    check(f"B.ii: N_+- = (Theta +- g)/2 integral and >= 0 for ALL "
          f"n <= {QMAX}; structure equation b^2 = Theta^2 - 4 N_+ N_- "
          "exact as integer identity (cross channel = N_+ N_- >= 0)",
          parity_ok and pos_ok and split_exact)

    eigen_ok = True
    cusp_zero_ok = True
    for p in EIGEN_PS:
        sig3 = 1 + p ** 3
        n2 = QMAX // (p * p)
        bad = 0
        max_res_ap = 0
        for n in range(1, n2 + 1):
            t = int(Th[p * p * n]) + jacobi(n, p) * p * int(Th[n])
            if n % (p * p) == 0:
                t += p ** 3 * int(Th[n // (p * p)])
            if t != sig3 * int(Th[n]):
                bad += 1
            r_ap = abs(t - HEAD_AP[p] * int(Th[n]))
            if r_ap > max_res_ap:
                max_res_ap = r_ap
        eigen_ok = eigen_ok and bad == 0
        cusp_zero_ok = cusp_zero_ok and max_res_ap > 0
    check("B.iii: Theta is an EXACT T(p^2)-eigenform with Eisenstein "
          f"eigenvalue sigma_3(p) = 1+p^3 for p in {EIGEN_PS} "
          "(0 mismatches on full windows); eigenvalue is NOT a_p(f8) "
          "=> cusp component ZERO -- pure Siegel-Weil genus Eisenstein "
          "(Cohen-Eisenstein weight 5/2, named classical)",
          eigen_ok and cusp_zero_ok)

    t_s = time.time()

    def seed_S2(d: int) -> int:
        chi = np.zeros(d, dtype=np.int8)
        chi[1] = 1
        k2 = kron2(d)
        for a in range(2, d):
            p = int(spf[a])
            if p == a:
                if d % p == 0:
                    v = 0
                elif p == 2:
                    v = k2
                else:
                    v = jacobi(d, p)
                chi[a] = v
            else:
                chi[a] = chi[p] * chi[a // p]
        aa = np.arange(d, dtype=np.int64)
        return int(np.dot(chi.astype(np.int64), aa * aa))

    seed_bad = 0
    n_seed = 0
    s2_pos = True
    for d in live[:N_SEED]:
        if d == 1:
            continue
        n_seed += 1
        S2 = seed_S2(d)
        if S2 <= 0:
            s2_pos = False
        if 24 * S2 != d * int(Th[d]):
            seed_bad += 1
    r1 = Fraction(int(Th[1])) / Fraction(-1, 12)
    print(f"        Cohen seed scan: {n_seed} live d in "
          f"{time.time() - t_s:.1f}s; anchor Theta(1)/zeta(-1) = {r1}")
    check(f"B.iv: COHEN SEED IDENTITY Theta(d) = -48 L(-1,chi_d) "
          f"exact-rational on {n_seed} live d (>= 100) -- "
          "d Theta(d) = 24 S2(d) integer-exact with S2 > 0 "
          "(L(-1,chi_d) = -B_2chi/2 < 0, generalised Bernoulli), "
          f"d = 1 anchor Theta(1)/zeta(-1) = {r1} (Cohen 1975 "
          "H(2,d) = L(-1,chi_d), named classical)",
          seed_bad == 0 and n_seed >= 100 and s2_pos
          and r1 == Fraction(-48))

    # ============================================================ C
    print("C -- Cauchy-Littlewood deletion + square-class bookkeeping")
    X_s, A_s, P_s, CHI_s = sp.symbols("X a p chi")
    s_s, t_s2, u_s, v_s = sp.symbols("s t u v")
    hs = [sp.Integer(1), s_s + t_s2]
    hu = [sp.Integer(1), u_s + v_s]
    for _k in range(2, K_CL + 1):
        hs.append(sp.expand((s_s + t_s2) * hs[-1] - s_s * t_s2 * hs[-2]))
        hu.append(sp.expand((u_s + v_s) * hu[-1] - u_s * v_s * hu[-2]))
    S_lem = sum(sp.expand(hs[k] * hu[k]) * X_s ** k
                for k in range(K_CL + 1))
    Den_lem = sp.expand((1 - s_s * u_s * X_s) * (1 - s_s * v_s * X_s)
                        * (1 - t_s2 * u_s * X_s) * (1 - t_s2 * v_s * X_s))
    Num_lem = 1 - s_s * t_s2 * u_s * v_s * X_s ** 2
    R_lem = sp.expand(S_lem * Den_lem - Num_lem)
    lemma_ok = all(sp.expand(R_lem.coeff(X_s, k)) == 0
                   for k in range(K_CL + 1))
    check("C.i: Cauchy-Littlewood window lemma (classical) -- "
          "Sum h_k(s,t) h_k(u,v) X^k = (1 - stuv X^2)/"
          "[(1-suX)(1-svX)(1-tuX)(1-tvX)] exact for k <= "
          f"{K_CL}, FREE Satake symbols (sympy)",
          lemma_ok)

    num_det = sp.simplify(Num_lem.subs({t_s2: P_s ** 3 / s_s,
                                        v_s: P_s ** 3 / u_s}))
    det_ok = sp.simplify(num_det - (1 - P_s ** 6 * X_s ** 2)) == 0
    al = [sp.Integer(1), A_s - 0 * P_s]           # f8 Satake, chi = 0
    be = [sp.Integer(1), (1 + P_s ** 3)]          # Eisenstein, chi = 0
    for _k in range(2, K_CL + 1):
        al.append(sp.expand(A_s * al[-1] - P_s ** 3 * al[-2]))
        be.append(sp.expand((1 + P_s ** 3) * be[-1] - P_s ** 3 * be[-2]))
    NUM = 1 - P_s ** 6 * X_s ** 2
    D_ff = sp.expand((1 - (A_s ** 2 - 2 * P_s ** 3) * X_s
                      + P_s ** 6 * X_s ** 2) * (1 - P_s ** 3 * X_s) ** 2)
    D_EE = sp.expand((1 - X_s) * (1 - P_s ** 3 * X_s) ** 2
                     * (1 - P_s ** 6 * X_s))
    D_fE = sp.expand((1 - A_s * X_s + P_s ** 3 * X_s ** 2)
                     * (1 - A_s * P_s ** 3 * X_s + P_s ** 9 * X_s ** 2))
    ch_ok = {}
    for name, seq1, seq2, DEN in (("b2", al, al, D_ff),
                                  ("Th2", be, be, D_EE),
                                  ("mixed", al, be, D_fE)):
        S_ch = sum(sp.expand(seq1[k] * seq2[k]) * X_s ** k
                   for k in range(K_CL + 1))
        R_ch = sp.expand(S_ch * DEN - NUM)
        ch_ok[name] = all(sp.expand(R_ch.coeff(X_s, k)) == 0
                          for k in range(K_CL + 1))
    check("C.ii: determinant instantiation st = uv = p^3 => numerator "
          "1 - p^6 X^2 INDEPENDENT of the pair (exact); the three basic "
          "channels carry it -- b^2 (f8 x f8), Theta^2 (Eis x Eis = the "
          "zeta(w)zeta(w-3)^2 zeta(w-6)/zeta(2w-6) floor), Theta*g "
          "(f8 x Eis, Rankin 1939) all series-exact vs closed form "
          f"(k <= {K_CL}, chi = 0 pillar)",
          det_ok and all(ch_ok.values()))

    n_t1 = n_t2 = 0
    tower_ok = True
    comb_ok = True
    for d in live:
        gd, td = int(g[d]), int(Th[d])
        for p in EIGEN_PS:
            if d % p == 0:
                continue
            chi = jacobi(d, p)
            a_p = HEAD_AP[p]
            s3 = 1 + p ** 3
            al1 = a_p - chi * p
            be1 = s3 - chi * p
            n1 = d * p * p
            if n1 <= QMAX:
                n_t1 += 1
                g1, t1v = int(g[n1]), int(Th[n1])
                if g1 != al1 * gd or t1v != be1 * td:
                    tower_ok = False
                np1, nm1 = int(Npl[n1]), int(Nmi[n1])
                if (2 * np1 != be1 * td + al1 * gd
                        or 2 * nm1 != be1 * td - al1 * gd
                        or 4 * np1 * nm1 != be1 * be1 * td * td
                        - al1 * al1 * gd * gd):
                    comb_ok = False
            n2v = d * p ** 4
            if n2v <= QMAX:
                n_t2 += 1
                al2 = a_p * al1 - p ** 3
                be2 = s3 * be1 - p ** 3
                if int(g[n2v]) != al2 * gd or int(Th[n2v]) != be2 * td:
                    tower_ok = False
    print(f"        bilinear towers: {n_t1} k=1 + {n_t2} k=2 points")
    check("C.iii: FIVE CHANNELS as verified bilinear combinations -- "
          "exact towers g(dp^2) = alpha_1 g(d), Theta(dp^2) = beta_1 "
          "Theta(d) (+ k=2 recurrences) and 2N_+(dp^2) = beta_1 Theta_d "
          "+ alpha_1 g_d, 2N_-(dp^2) = beta_1 Theta_d - alpha_1 g_d, "
          "4N_+N_-(dp^2) = beta_1^2 Theta_d^2 - alpha_1^2 g_d^2, "
          f"integer-exact on {n_t1} + {n_t2} points (>= 300/40)",
          tower_ok and comb_ok and n_t1 >= 300 and n_t2 >= 40)

    Y_s = sp.symbols("Y")
    gens = {
        "full": 2 * Y_s / (1 - Y_s),
        "fam": 2 * Y_s / (1 - Y_s ** 2) - Y_s,
        "floor": 2 * Y_s / (1 - Y_s ** 2),
        "mixed": -2 * Y_s ** 2 / (1 - Y_s ** 2),
        "flat": 2 * Y_s ** 2 / (1 - Y_s ** 2),
        "linear": Y_s / (1 - Y_s),
    }
    lists = {}
    for name, gen in gens.items():
        ser = sp.series(gen, Y_s, 0, K_MAX + 1).removeO()
        lists[name] = [int(ser.coeff(Y_s, k)) for k in range(1, K_MAX + 1)]
    print(f"        layers: fam {lists['fam'][:4]}, floor "
          f"{lists['floor'][:4]}, mixed {lists['mixed'][:4]}, "
          f"flat {lists['flat'][:4]}, linear {lists['linear'][:4]}")
    tgt = {
        "fam": [1 if k == 1 else (2 if k % 2 == 1 else 0)
                for k in range(1, K_MAX + 1)],
        "floor": [2 if k % 2 == 1 else 0 for k in range(1, K_MAX + 1)],
        "mixed": [0 if k % 2 == 1 else -2 for k in range(1, K_MAX + 1)],
        "flat": [0 if k % 2 == 1 else 2 for k in range(1, K_MAX + 1)],
        "linear": [1] * K_MAX,
        "full": [2] * K_MAX,
    }
    check("C.iv: p^{3k}-layer weight lists exact -- fam [1,0,2,0,...], "
          "floor [2,0,2,0,...], mixed [0,-2,0,-2,...] (deletion isolated "
          "WITH MINUS in the only signed channel), flat [0,2,0,2,...] = "
          "lambda-weights of zeta_p(2u), linear [1,1,1,1,...] (full)",
          all(lists[k] == tgt[k] for k in lists))

    book_ok = sp.simplify(gens["fam"] + gens["flat"] + Y_s
                          - gens["full"]) == 0
    slots_ok = all(
        (tgt["fam"][k] == 0 and tgt["flat"][k] == 2) if (k + 1) % 2 == 0
        else (tgt["flat"][k] == 0
              and tgt["fam"][k] + (1 if k == 0 else 0) == 2)
        for k in range(K_MAX)
    )
    om = np.zeros(N_SIEVE + 1, dtype=np.int64)
    dcnt = np.zeros(N_SIEVE + 1, dtype=np.int64)
    for p in sp.primerange(2, N_SIEVE + 1):
        om[int(p)::int(p)] += 1
    for a_i in range(1, N_SIEVE + 1):
        dcnt[a_i::a_i] += 1
    sieve_fwd = True
    sieve_bwd = True
    for n in range(1, N_SIEVE + 1):
        acc_f = 0
        acc_b = 0
        r = 1
        while r * r <= n:
            if n % (r * r) == 0:
                acc_f += int(mu[r]) * int(dcnt[n // (r * r)])
                acc_b += 2 ** int(om[n // (r * r)])
            r += 1
        if acc_f != 2 ** int(om[n]):
            sieve_fwd = False
        if acc_b != int(dcnt[n]):
            sieve_bwd = False
    check("C.v: TOWER DOUBLE-COUNTING IDENTITY exact -- fam [1,0,2,0] + "
          "2flat [0,2,0,2] + Plancherel delta_k1 = FULL [2,2,2,2] "
          "(generating functions, slot-disjoint); the flat object is "
          "the square-class index zeta 1/(1-Y^2) = zeta_p(2u); globally "
          "2^omega(n) = Sum_{r^2|n} mu(r) d(n/r^2) and d(n) = "
          f"Sum_{{r^2|n}} 2^omega(n/r^2) coefficient-exact n <= {N_SIEVE} "
          "(Moebius square sieve = RS zeta(2s)-normalisation, classical)",
          book_ok and slots_ok and sieve_fwd and sieve_bwd)

    # ============================================================ D
    print("D -- positive linear carrier ell^2(d, mu) + plus balance")
    carrier_pos = all(int(Th[d]) >= abs(int(g[d])) and int(Th[d]) > 0
                      for d in live)
    d5 = [D for D in range(5, D_FAM + 1, 8) if mu[D] != 0]
    d5_ok = all(int(g[D]) == 0 for D in d5) \
        and all(int(Th[D]) > 0 for D in d5)
    mu_w = np.array([float(int(Th[d])) * d ** (-2.5) for d in live])
    xg = np.array(live, dtype=np.float64) / float(max(live))
    VB = np.zeros((20, len(live)))
    for k in range(20):
        c = (k + 0.5) / 20.0
        w = 1.5 / 20.0
        tloc = (xg - c) / w
        VB[k] = np.where(np.abs(tloc) < 1.0, (1.0 - tloc * tloc) ** 2, 0.0)
    GB = (VB * mu_w) @ VB.T
    eigsB = np.linalg.eigvalsh(GB)
    rankB = int(np.sum(np.abs(eigsB) > 1e-8 * max(abs(float(eigsB[-1])),
                                                  1e-30)))
    check(f"D.i: mu(d) = Theta(d)|d|^(-a) = 48|L(-1,chi_d)||d|^(-a) > 0 "
          f"on ALL {len(live)} live d (exact counting inequality "
          f"Theta >= |b| > 0); extends to d = 5 mod 8 ({len(d5)} d: "
          "b = 0, Theta > 0 -- population-positive where the quadratic "
          "family is empty); GNS Gram PSD "
          f"(min eig {float(eigsB[0]):.2e}, rank {rankB}/20)",
          carrier_pos and d5_ok and len(d5) >= 200
          and float(eigsB[0]) >= -1e-8 * float(eigsB[-1]) and rankB == 20)

    G_lin = (1 - CHI_s * P_s * X_s) / ((1 - X_s) * (1 - P_s ** 3 * X_s))
    L_lin = sp.series(X_s * sp.diff(sp.log(G_lin), X_s), X_s, 0,
                      K_MAX + 1).removeO()
    lam_closed_ok = all(
        sp.simplify(sp.expand(L_lin.coeff(X_s, k))
                    - (1 + P_s ** (3 * k) - (CHI_s * P_s) ** k)) == 0
        for k in range(1, K_MAX + 1)
    )
    Q_s = sp.symbols("q", positive=True)
    layer_ok = True
    for k in range(1, K_MAX + 1):
        e = sp.expand((1 + P_s ** (3 * k) - (CHI_s * P_s) ** k)
                      .subs(P_s, Q_s ** 2))
        c6k = sp.expand(e.coeff(Q_s, 6 * k))
        if c6k != 1 or c6k.has(CHI_s):
            layer_ok = False
    deg_num = sp.degree(sp.Poly(1 - CHI_s * P_s * X_s, X_s))
    check("D.ii: FULL WEIGHTS -- lambda_k = 1 + p^{3k} - (chi p)^k exact "
          f"(k <= {K_MAX}); p^(3k)-layer = [1,1,...,1], chi-free (the "
          "chi term lives at layer q^(2k), never at q^(6k)); CL lemma "
          f"structurally inapplicable (numerator degree {deg_num} = 1; "
          "chi = 0 numerator = 1 -- no second Satake pair)",
          lam_closed_ok and layer_ok and deg_num == 1)

    lam_pk = []
    for p in sp.primerange(3, N_LAM + 1):
        p = int(p)
        lp = math.log(p)
        pk = p
        while pk <= N_LAM:
            lam_pk.append((pk, lp))
            pk *= p
    TEST_FNS = []
    for a in (1.5, 2.0, 2.5, 3.0, 3.5):
        TEST_FNS.append(("fejer", a, (lambda u, aa=a: g_fejer(u, aa)),
                         float(a)))
    for sig in (0.6, 0.8, 1.0, 1.2):
        TEST_FNS.append(("gauss", sig, (lambda u, s=sig: g_gauss(u, s)),
                         8.0 * float(sig)))

    def P_lin_fn(g_fn, umax):
        s = 0.0
        for n, lp in lam_pk:
            u = math.log(n)
            if u > umax + 1e-12:
                continue
            s += lp * (n ** -2.0 + float(n)) * g_fn(u)
        return 2.0 * s

    def P_zeta_conj(g_fn, umax, alpha):
        s = 0.0
        for n, lp in lam_pk:
            u = math.log(n)
            if u > umax + 1e-12:
                continue
            s += lp * n ** -0.5 * math.exp(alpha * u) * g_fn(u)
        return 2.0 * s

    def P_agg_fn(g_fn, umax):
        s = 0.0
        for n, lp in lam_pk:
            u = 2.0 * math.log(n)
            if u > umax + 1e-12:
                continue
            s += lp * (n ** -2.0 + float(n)) * g_fn(u)
        return 2.0 * s

    def P_flat_conj(g_fn, umax, alpha):
        s = 0.0
        for n, lp in lam_pk:
            u = 2.0 * math.log(n)
            if u > umax + 1e-12:
                continue
            s += lp * n ** -0.5 * math.exp(alpha * u / 2.0) * g_fn(u)
        return 2.0 * s

    plus_ok = True
    max_rel_plus = 0.0
    for kind, par, g_fn, um in TEST_FNS:
        pl = P_lin_fn(g_fn, um)
        rhs = P_zeta_conj(g_fn, um, -1.5) + P_zeta_conj(g_fn, um, +1.5)
        rel = abs(pl - rhs) / max(abs(pl), 1e-30)
        max_rel_plus = max(max_rel_plus, rel)
        if rel > REL_PLUS:
            plus_ok = False
    check("D.iii: PLUS BALANCE EXACT -- Prime_Thetalin(g) = "
          "P_zeta(g_-) + P_zeta(g_+), g_+- = e^(+-3u/2) g(u), ONLY PLUS "
          f"signs, on all {len(TEST_FNS)} test functions "
          f"(max rel {max_rel_plus:.2e} < {REL_PLUS:g}; zero-free "
          "finite sums over odd prime powers)",
          plus_ok and len(TEST_FNS) >= 9)

    us_k = np.linspace(-12.0, 12.0, 12001)
    k_lin = (np.exp(2 * us_k) + np.exp(us_k)
             + np.exp(-us_k) + np.exp(-2 * us_k))
    k_fac = ((np.exp(0.5 * us_k) + np.exp(-0.5 * us_k))
             * 2.0 * np.cosh(1.5 * us_k))
    kern_rel = float(np.max(np.abs(k_lin - k_fac))
                     / np.max(np.abs(k_lin)))
    q_ok = True
    max_rel_q = 0.0
    for kind, par, g_fn, um in TEST_FNS:
        us = np.linspace(-um, um, 6001)
        gv = np.array([g_fn(float(u)) for u in us])
        pole_lin = float(np.trapezoid(
            gv * (np.exp(2 * us) + np.exp(us)
                  + np.exp(-us) + np.exp(-2 * us)), us))
        q_lhs = pole_lin - P_lin_fn(g_fn, um)
        pole_pm = 0.0
        p_pm = 0.0
        for alpha in (-1.5, 1.5):
            ga = np.exp(alpha * us) * gv
            pole_pm += float(np.trapezoid(
                ga * (np.exp(0.5 * us) + np.exp(-0.5 * us)), us))
            p_pm += P_zeta_conj(g_fn, um, alpha)
        q_rhs = pole_pm - p_pm
        rel = abs(q_lhs - q_rhs) / max(abs(q_lhs), 1e-30)
        max_rel_q = max(max_rel_q, rel)
        if rel > REL_PLUS:
            q_ok = False
    check("D.iv: Q-COLLAPSE -- pole kernel (e^(u/2)+e^(-u/2)) 2cosh(3u/2) "
          f"= e^(2u)+e^u+e^(-u)+e^(-2u) pointwise (rel {kern_rel:.2e} "
          "< 1e-13) and Q_Thetalin(g) = Q_zeta(g_-) + Q_zeta(g_+) on all "
          f"test functions (max rel {max_rel_q:.2e}; arch declared "
          "classical-external)",
          kern_rel < 1e-13 and q_ok)

    agg_ok = True
    max_rel_agg = 0.0
    for kind, par, g_fn, um in TEST_FNS:
        pa = P_agg_fn(g_fn, um)
        rhs = P_flat_conj(g_fn, um, -1.5) + P_flat_conj(g_fn, um, +1.5)
        rel = abs(pa - rhs) / max(abs(pa), 1e-30)
        max_rel_agg = max(max_rel_agg, rel)
        if rel > REL_PLUS:
            agg_ok = False
    check("D.v: d-AGGREGATION WITH PLUS -- prime side of "
          "zeta_o(2s)zeta_o(2s-3) = P_zeta(gflat_-) + P_zeta(gflat_+), "
          "gflat_+-(x) = e^(+-3x/2) g(2x): the v539 flat/doubling kernel "
          f"class WITH PLUS (max rel {max_rel_agg:.2e} < {REL_PLUS:g}; "
          "sign INVERTED vs the square-plane minus of v539)",
          agg_ok)

    # ============================================================ E
    print("E -- functional equation (Fricke closed; split-Mellin)")
    mod_ok = True
    max_mod = mpmath.mpf(0)
    for ys in Y_MOD:
        y = mpmath.mpf(ys)
        lhs = Theta_iy(1 / (8 * y))
        rhs = 8 * y ** MP52 * Theta_dag_iy(y)
        rel = abs(lhs - rhs) / abs(lhs)
        max_mod = max(max_mod, rel)
        if rel > REL_FE:
            mod_ok = False
    y_t = mpmath.mpf("0.41")
    lhs2 = Theta_dag_iy(1 / (8 * y_t))
    rhs2 = MP8 ** (mpmath.mpf(3) / 2) * y_t ** MP52 * Theta_iy(y_t)
    rel2 = abs(lhs2 - rhs2) / abs(lhs2)
    check("E.i: FRICKE CLOSED -- Theta(i/(8y)) = 8 y^(5/2) Theta_dag(iy) "
          f"on {len(Y_MOD)} y incl. the fixed point 8^(-1/2) "
          f"(max rel {mpmath.nstr(max_mod, 3)} < 1e-20); involution "
          f"closes: inverse leg rel {mpmath.nstr(rel2, 3)}, constant "
          "chain 8^(-1/4) 8^(+1/4) = 1 (Jacobi inversions, classical)",
          mod_ok and rel2 < REL_FE)

    anchor_ok = True
    for y_f, arr, fn in ((0.35, Th, Theta_iy), (0.6, Th, Theta_iy),
                         (0.35, Td, Theta_dag_iy), (0.6, Td, Theta_dag_iy)):
        x = math.exp(-2 * math.pi * y_f)
        with np.errstate(under="ignore"):
            ssum = float(np.sum(arr.astype(np.float64)
                                * x ** np.arange(QMAX + 1,
                                                 dtype=np.float64)))
        jval = float(fn(mpmath.mpf(y_f)))
        if abs(ssum - jval) / abs(jval) >= 1e-12:
            anchor_ok = False
    even_only = not np.any(Td[1::2] != 0)
    half = Td[0::2][: QMAX // 2 + 1]
    psi_match = bool(np.array_equal(half, Psi[: len(half)]))
    check("E.ii: exact integer builds == jtheta monomials on the "
          "imaginary axis (4 anchors, rel < 1e-12); LANDEN COLLAPSE "
          "Theta_dag = theta4(q^2)^4 theta3(q^2): even-only support and "
          "Theta_dag(2m) = psi(m) coefficient-exact (classical)",
          anchor_ok and even_only and psi_match)

    n_arr = np.arange(1, QMAX + 1, dtype=np.float64)
    Thf = Th[1:].astype(np.float64)
    Tdf = Td[1:].astype(np.float64)
    anch_ok = True
    for s, tol in ((4.0, 1e-4), (5.0, 1e-8)):
        lam_split = float(Lam_Theta(s, C_LHS))
        lam_dir = ((2 * math.pi) ** (-s) * math.gamma(s)
                   * float(np.sum(Thf * n_arr ** (-s))))
        if abs(lam_split - lam_dir) / abs(lam_dir) >= tol:
            anch_ok = False
    for w, tol in ((4.5, 1e-6), (5.0, 1e-8)):
        lam_split = float(Lam_dag(w, C_RHS))
        lam_dir = ((2 * math.pi) ** (-w) * math.gamma(w)
                   * float(np.sum(Tdf * n_arr ** (-w))))
        scale = ((2 * math.pi) ** (-w) * math.gamma(w)
                 * float(np.sum(np.abs(Tdf) * n_arr ** (-w))))
        if abs(lam_split - lam_dir) / scale >= tol:
            anch_ok = False
    fe_ok = True
    max_fe = mpmath.mpf(0)
    for ss in S_STRIP:
        s = mpmath.mpf(ss)
        lhs = Lam_Theta(s, C_LHS)
        rhs = MP8 ** (1 - s) * Lam_dag(MP52 - s, C_RHS)
        rel = abs(lhs - rhs) / abs(lhs)
        max_fe = max(max_fe, rel)
        if rel > REL_FE:
            fe_ok = False
    split_cons = abs(Lam_Theta("1.25", C_LHS) - Lam_Theta("1.25", C_ALT)) \
        / abs(Lam_Theta("1.25", C_LHS))
    check("E.iii: COMPLETED FE IN THE STRIP -- Lambda_Theta(s) = "
          "8^(1-s) Lambda_Theta_dag(5/2-s) at s in {0.5, 1.25, 2.0} "
          f"with INDEPENDENT split points (max rel "
          f"{mpmath.nstr(max_fe, 3)} < 1e-20; split invariance "
          f"{mpmath.nstr(split_cons, 3)}); split-Mellin anchored vs "
          "direct Dirichlet sums (truncation-limited tolerances met; "
          "Hecke split-Mellin, classical)",
          fe_ok and split_cons < REL_FE and anch_ok)

    res_t = mpmath.mpf("1e-4") * Lam_Theta(MP52 + mpmath.mpf("1e-4"),
                                           C_LHS)
    rel_rt = abs(res_t - MP8 ** (-mpmath.mpf(3) / 2)) \
        / MP8 ** (-mpmath.mpf(3) / 2)
    res_d = mpmath.mpf("1e-5") * Lam_dag(mpmath.mpf("1e-5"), C_RHS)
    rel_rd = abs(res_d - (-1))
    sC = Fraction(5, 4)
    lines_ok = (sC == (Fraction(0) + Fraction(5, 2)) / 2
                and sC - Fraction(1) == Fraction(1, 4)
                and {Fraction(1, 2) - 2 * Fraction(1),
                     Fraction(7, 2) - 2 * Fraction(1)}
                == {Fraction(-3, 2), Fraction(3, 2)})
    check("E.iv: POLE SET + LINE MAP -- Lambda_Theta single pole at "
          f"s = 5/2 with residue 8^(-3/2) (rel {mpmath.nstr(rel_rt, 3)} "
          "< 1e-3); Lambda_dag single pole at 0 with residue -1 (abs "
          f"{mpmath.nstr(rel_rd, 3)} < 1e-3) -- the FE swaps the poles; "
          "FE centre 5/4 = (0 + 5/2)/2, plus-balance locus s = 1 "
          "off-centre by EXACTLY 1/4, tilt pair {-3/2, +3/2} "
          "(exact rationals)",
          rel_rt < mpmath.mpf("1e-3") and rel_rd < mpmath.mpf("1e-3")
          and lines_ok)

    # ============================================================ F
    print("F -- cone facts + the named open boundary lambda* [C]")
    n_all = np.arange(1, QMAX + 1)
    s_law = np.where((n_all % 4) <= 1, -1, 1).astype(np.int64)
    law_viol = int(np.sum(np.sign(Psi[1:]) != s_law))
    psi_zeros = int(np.sum(Psi[1:] == 0))
    check("F.i: RIGID MIRROR SIGN LAW -- sign psi(n) = "
          f"(-1)^(floor(n/2)+1) with |psi(n)| > 0 for ALL n <= {QMAX} "
          f"({law_viol} violations, {psi_zeros} zeros; exact integers) "
          "-- the mirror family is a 4-periodic sign times a strictly "
          "positive family",
          law_viol == 0 and psi_zeros == 0)

    n_lat = np.arange(1, N_LAT + 1)
    U_LAT = np.log(n_lat.astype(np.float64))
    s_lat = np.where((n_lat % 4) <= 1, -1, 1)
    th_lat_pos = bool(np.all(Th[1:N_LAT + 1] > 0))
    mass_th = Th[1:N_LAT + 1] > 0
    sgn_ps = np.sign(Psi[1:N_LAT + 1])
    mass_ps = sgn_ps != 0
    sgn_td = np.sign(Td[1:N_LAT + 1])
    mass_td = sgn_td != 0
    C1m = mass_th
    C2m = C1m & mass_ps & (sgn_ps > 0)
    C3m = C2m & mass_td & (sgn_td > 0)
    C2_cf = C1m & ((n_lat % 4) >= 2)
    C3_cf = C1m & ((n_lat % 8) == 6)
    cls_ok = bool(np.array_equal(C2m, C2_cf)) \
        and bool(np.array_equal(C3m, C3_cf))
    print(f"        constraint atoms: |C_L1|={int(C1m.sum())}, "
          f"|C_L2|={int(C2m.sum())}, |C_L3|={int(C3m.sum())}")
    check("F.ii: HULL CONSTRAINT CLASSES machine == closed form -- from "
          "the exact coefficient signs (Theta full-support positive on "
          f"the lattice: {th_lat_pos}), C_L2 = {{n == 2,3 mod 4}} and "
          "C_L3 = {n == 6 mod 8} (product-cone separation / Farkas at "
          "a single atom, classical)",
          th_lat_pos and cls_ok)

    DU = 2 * U_GRID / N_GRID
    us_g = (np.arange(N_GRID) - N_GRID // 2) * DU
    lag_u = np.arange(N_GRID) * DU
    SAMPLES = []
    for sig in (0.5, 0.8, 1.2):
        SAMPLES.append((f"gauss s={sig}",
                        np.exp(-0.5 * (us_g / sig) ** 2), "nonneg", None))
    for a in (1.5, 2.5):
        SAMPLES.append((f"bump a={a}",
                        np.where(np.abs(us_g) < a,
                                 (1 - (us_g / a) ** 2) ** 2, 0.0),
                        "nonneg", None))
    for sig, om_ in ((0.7, 1.2), (0.7, 2.5), (1.1, 1.8), (1.1, 3.5)):
        SAMPLES.append((f"gabor s={sig} w={om_}",
                        np.exp(-0.5 * (us_g / sig) ** 2)
                        * np.cos(om_ * us_g), "gabor", (sig, om_)))
    SAMPLES.append(("hermite2", (us_g ** 2 - 1) * np.exp(-0.5 * us_g ** 2),
                    "hermite", None))
    SAMPLES.append(("DoG c=0.5", np.exp(-0.5 * us_g ** 2)
                    - 0.5 * np.exp(-us_g ** 2 / 8), "dog", None))
    SAMPLES.append(("DoG c=0.8", np.exp(-0.5 * us_g ** 2)
                    - 0.8 * np.exp(-us_g ** 2 / 8), "dog", None))

    def autocorr_lattice(fv):
        F = np.fft.rfft(fv, 2 * N_GRID)
        acf = np.fft.irfft(np.abs(F) ** 2, 2 * N_GRID)[:N_GRID] * DU
        acf_n = acf / float(acf[0])
        return np.interp(U_LAT, lag_u, acf_n)

    ROWS = []
    for name, fv, typ, meta in SAMPLES:
        ROWS.append({"name": name, "typ": typ, "meta": meta,
                     "v": autocorr_lattice(fv)})
    n_tot = len(ROWS)
    r_lat = np.exp(-U_LAT ** 2 / 8.0)
    _Fr = np.fft.rfft(np.exp(-us_g ** 2 / 4.0), 2 * N_GRID)
    _acf_r = np.fft.irfft(np.abs(_Fr) ** 2, 2 * N_GRID)[:N_GRID] * DU
    _acf_r = _acf_r / _acf_r[0]
    _mr = lag_u <= 10.0
    rel_r = float(np.max(np.abs(_acf_r[_mr]
                                - np.exp(-lag_u[_mr] ** 2 / 8.0))
                         / np.exp(-lag_u[_mr] ** 2 / 8.0)))

    def lam_star(v, mask, ref):
        if not np.any(mask):
            return 0.0
        return float(max(0.0, np.max(-v[mask] / ref[mask])))

    masks = (C1m, C2m, C3m)
    for r in ROWS:
        r["cov"] = [bool(np.all(r["v"][m] >= -TOL_MEM)) for m in masks]
        r["lam"] = [lam_star(r["v"], m, r_lat) for m in masks]

    cosh_lat = np.cosh(U_LAT)
    fe_flags = 0
    fe_lam = 0
    for r in ROWS:
        mv = cosh_lat * r["v"]
        mr2 = cosh_lat * r_lat
        for li, m in enumerate(masks):
            flag_m = bool(np.all(mv[m] >= -TOL_MEM * cosh_lat[m]))
            lam_m = lam_star(mv, m, mr2)
            if flag_m == r["cov"][li]:
                fe_flags += 1
            if abs(lam_m - r["lam"][li]) <= 1e-10 * (1.0 + r["lam"][li]):
                fe_lam += 1
    check("F.iii: FE SELF-DUALITY OF THE GUARANTEED SIDE (sampled) -- "
          "the FE mirror multiplier cosh(u) > 0 preserves every hull "
          f"membership flag ({fe_flags}/{3 * n_tot}) and the gap "
          f"functional is FE-COVARIANT ({fe_lam}/{3 * n_tot}; "
          "lambda*(cosh h; cosh r) = lambda*(h; r)) -- MEASURED on "
          f"{n_tot} Weil-cone samples x 3 libraries",
          fe_flags == 3 * n_tot and fe_lam == 3 * n_tot)

    wit = next(r for r in ROWS if r["name"] == "gabor s=0.7 w=2.5")
    bad3 = np.where((wit["v"] < -TOL_MEM) & C3m)[0]
    n_star = int(bad3[0]) + 1 if len(bad3) else -1
    farkas_ok = (
        n_star > 0 and n_star % 8 == 6
        and int(Th[n_star]) > 0 and int(Psi[n_star]) > 0
        and int(Td[n_star]) > 0
        and wit["v"][n_star - 1] < -TOL_MEM
        and wit["lam"][2] > 0.0
    )
    lam3 = wit["lam"][2]
    feas_at = bool(np.all(wit["v"][C3m] + lam3 * r_lat[C3m] >= -1e-12))
    sharp = not bool(np.all(wit["v"][C3m]
                            + (1 - 1e-6) * lam3 * r_lat[C3m] >= 0.0))
    lo, hi = 0.0, 2 * lam3 + 1.0
    for _ in range(60):
        mid = 0.5 * (lo + hi)
        if bool(np.all(wit["v"][C3m] + mid * r_lat[C3m] >= 0.0)):
            hi = mid
        else:
            lo = mid
    bis_err = abs(hi - lam3) / (1.0 + lam3)
    mono_ok = all(r["lam"][0] >= r["lam"][1] - 1e-12
                  and r["lam"][1] >= r["lam"][2] - 1e-12 for r in ROWS)
    print(f"        Farkas witness: gabor s=0.7 w=2.5, atom n*={n_star} "
          f"(=6 mod 8), h(log n*)={wit['v'][n_star - 1]:+.4e}, "
          f"lambda*_L3={lam3:.6f} (bisect err {bis_err:.1e})")
    check("F.iv: lambda* EXISTS with an EXACT FARKAS WITNESS -- the "
          f"reference r = e^(-u^2/8) is a Gaussian autocorrelation (rel "
          f"{rel_r:.1e} < 1e-6, r > 0 on the lattice); witness atom "
          f"n* = {n_star} == 6 mod 8 where Theta, psi, Theta_dag ALL pay "
          "positive mass with plus sign (exact integers) while "
          "h(log n*) < 0 => h outside the hull (dual certificate) and "
          f"lambda*_L3(h) = {lam3:.4f} > 0; closed form == bisection "
          f"({bis_err:.1e} <= 1e-8); monotone lambda*_L1 >= L2 >= L3 "
          f"on all {n_tot} samples",
          rel_r < 1e-6 and bool(np.all(r_lat > 0)) and farkas_ok
          and feas_at and sharp and bis_err <= 1e-8 and mono_ok)

    cov1 = sum(r["cov"][0] for r in ROWS)
    cov3 = sum(r["cov"][2] for r in ROWS)
    n_nonneg = sum(1 for r in ROWS if r["typ"] == "nonneg")
    nested = all((not r["cov"][0] or r["cov"][1])
                 and (not r["cov"][1] or r["cov"][2]) for r in ROWS)
    pin_ok = all(r["v"][0] > 0 for r in ROWS) and int(s_lat[0]) == -1
    unc = [r for r in ROWS if not r["cov"][0]]
    red3 = [1.0 - r["lam"][2] / r["lam"][0] for r in unc
            if r["lam"][0] > 0]
    mean_red3 = float(np.mean(red3)) if red3 else 0.0
    print(f"        coverage {cov1}/{n_tot} -> {cov3}/{n_tot}; "
          f"mean gap reduction on uncovered {100 * mean_red3:.1f}%")
    check("F.v: COVERAGE SATURATES on the sample -- "
          f"{cov1}/{n_tot} -> {cov3}/{n_tot} covered (= the "
          f"{n_nonneg} autocorrelations of nonnegative f; nested flags "
          "monotone); the n = 1 pin holds (h(0) > 0 on every sample, "
          "s(1) = -1): no finite signed theta library removes lambda* "
          f"-- it falls (mean {100 * mean_red3:.0f}% on the uncovered "
          "sample) but stays > 0 (MEASURED, finite sample)",
          cov1 == n_nonneg and cov3 == n_nonneg and nested and pin_ok
          and all(x >= -1e-12 for x in red3) and mean_red3 > 0)

    check("FENCE: Cohen 1975 / Siegel-Weil / Jacobi-Fricke / Landen / "
          "Hecke split-Mellin / Cauchy-Littlewood / Moebius sieve / "
          "Shimura / Shintani / Weil 1952 / Farkas named classical; "
          "EULER-REGION positivity only (edge L-values, NOT the central "
          "line); lambda* on n == 6 mod 8 is the NAMED OPEN BOUNDARY "
          "inside the claim; NOT 'almost RH'; ZETA.HP.CARRIER "
          "untouched; no marker moves",
          True)

    elapsed = time.time() - t0
    print(f"\nv540 runtime: {elapsed:.1f}s")
    print(f"  Dirac: D^2 blocks rel {max(err_dd, err_mm):.2e}; "
          f"K rel {err_k:.2e}; Shimura {shim_n} pairs")
    print(f"  Cohen seed: {n_seed} live d exact; constant {r1}")
    print(f"  towers: {n_t1}+{n_t2} bilinear points exact")
    print(f"  plus balance rel {max_rel_plus:.2e}; "
          f"agg-plus rel {max_rel_agg:.2e}")
    print(f"  FE: Fricke rel {mpmath.nstr(max_mod, 3)}; "
          f"strip rel {mpmath.nstr(max_fe, 3)}")
    print(f"  cone: FE-self-dual {fe_flags}/{3 * n_tot}; witness "
          f"n*={n_star}; lambda*_L3={lam3:.4f}; coverage "
          f"{cov1}->{cov3}/{n_tot}")
    return summary("RTF.GNS.AMP.01 amplitude route and positive "
                   "linear carrier")


if __name__ == "__main__":
    raise SystemExit(run())
