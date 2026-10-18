"""Discovery probe (2026-07-25), part 67 of the zeta/prime investigation.
AMPLITUDE.DIRAC.SQRT — map the amplitude plane of the half-integral bridge
(the direct entry to the thinking-pause question: metaplectic square-root
of the square object; Review §7).

Context (sandbox chain):
  T50 / half_integral_selfconvolution: Shimura relation
      b(d m²) = b(d)·α_d^♯(m),   α exact with 2-support correction.
  T51 / waldspurger_family_kernel: Gram K = VᵀV with
      V[d,m] = √w_d · b(d) · χ_d(m)  (signed amplitudes).
  T62 / core_isolation: fibre decomposition by σ = (χ_d(p))_p.
  T63–T64 / weil_core + rtf_stabilization: the SQUARE plane
      (ζ-kernel, Minus = ♭-term, det₂).  Thinking pause: which
      halving removes the square (metaplectic root of the family)?
  v537 / v538 / v539: load-bearing half-integral bridge + Weil family.

Classical background (named as such — not new mathematics):
  Shimura correspondence / half-integral weight; Waldspurger /
  Baruch–Mao (central values encode b(d)², not signs); metaplectic
  group and half-integral forms; Dirac square-root idea for a positive
  kernel K = VᵀV; Krein polarisation; Kohnen sign results for
  half-integral coefficients; Clebsch–Gordan / Sato–Tate on SU(2)
  (χ₁×χ₁ = χ₀+χ₂).

FENCE (load-bearing typing): this probe is a MAPPING of the amplitude
plane — NOT a Weil-positivity claim and NOT RH evidence.  The open
problem remains the canonical polarisation with positivity.

S0  ZERO-FIREWALL (AST): no Riemann-zero loader; ζ/Γ as mpmath OK.
A1  DIRAC: D = [[0,V],[Vᵀ,0]], D² = diag(VVᵀ, VᵀV), VᵀV = K;
    spectrum ± svals(V); Hecke intertwining (modal T51 + Shimura T50).
A2  AMPLITUDE TOWERS = DEGREE-2 EULER: T_d^amp = Σ α_d^♯(m) m^{-w};
    exact local form; Λ_amp vs square [1,0,2,0]; no ♭/doubling.
A3  METAPLECTIC DATUM = sgn(b(d)): distribution, fibre constancy,
    correlations vs root-number proxies / |d|; honest typing.
A4  CATEGORICAL SEESAW: amplitude has E_ST[χ₁]=0 (no ζ-kernel);
    square gets ζ via χ₁×χ₁; polarisation V=V₊−V₋ / K vs K_abs.
A5  SYNTHESIS + thinking-pause map; promotion typing only (no promote).

PREREGISTERED CRITERIA
  A1: D=Dᵀ; D² block-exact; VᵀV=K exact; spectrum ±svals;
      m-side V A = Â V (p-free) AND modal d-side exact — else KILL
      (naive Dirac not canonical).
  A2: algebraic + coefficientwise Grad-2 Euler on ≥8 towers, m≤200;
      no (1−p³X) ratio; Λ_amp Chebyshev without even-power kill.
  A3: report sign shares, mixed-fibre fraction, H(sgn|σ), correlations.
  A4: quantify seesaw (no Minus/ζ on amp vs ζ+Minus on square);
      polarisation cross-term / K vs K_abs ζ-proxy.
  Verdicts: DIRAC-SQRT-EXACT / PARTIAL / OBSTRUCTED.

Firewall: discovery sandbox only — no promotion, no ledger / paper /
website / next.txt / README edits; classical theorems named classical;
no RH-evidence or “Weil positivity achieved” language.
"""
from __future__ import annotations

import ast
import inspect
import math
import time
from collections import defaultdict

import numpy as np
import sympy as sp

PASS = 0
FAIL = 0
T0 = time.time()

# ---------------------------------------------------------------- config
QMAX = 8_000                      # g-series / live d window
N_F8 = 20_000
D_DIRAC = 5_000                   # live fundamental d ≤ this
M_MAX = 2001                      # odd m-window
M_EULER = 200                     # amplitude tower check
N_TOWERS = 10                     # ≥8 towers
WITNESS_KEY = (0, 2, 0, 1, 1, 1)
HEAD_AP = {3: -4, 5: -2, 7: 24, 11: -44, 13: 22}
HECKE_PS = (3, 5, 7)
PATTERN_PRIMES = (3, 5, 7, 11, 13)
K_HALF = 2
W_NAME = "inv"                    # w_d = |d|^{-1} RTF-native (T55/T62)
TOL = 1e-10
TOL_SPEC = 1e-8


def check(name, ok):
    global PASS, FAIL
    tag = "PASS" if ok else "FAIL"
    print(f"  [{tag}] {name}", flush=True)
    if ok:
        PASS += 1
    else:
        FAIL += 1
    return ok


def info(msg):
    print(f"        {msg}", flush=True)


# ================================================================ helpers
def eta_pass(d, e, order):
    s = np.zeros(order + 1, dtype=np.int64)
    s[0] = 1
    for k in range(d, order + 1, d):
        for _ in range(e):
            s[k:] = s[k:] - s[:-k]
    return s


def conv_i64(a, b, order):
    return np.convolve(a, b)[: order + 1].astype(np.int64)


def kronecker(d: int, n: int) -> int:
    return int(sp.kronecker_symbol(d, n))


def is_fundamental_discriminant(d: int) -> bool:
    if d == 0:
        return False
    if d % 4 == 1:
        return abs(sp.mobius(abs(d))) == 1
    if d % 4 != 0:
        return False
    m = d // 4
    if m % 4 not in (2, 3):
        return False
    return abs(sp.mobius(abs(m))) == 1


def theta2_t(order_t, scale_q=1):
    s = np.zeros(order_t + 1, dtype=np.int64)
    o = 1
    while True:
        exp = scale_q * o * o
        if exp > order_t:
            break
        s[exp] = 2
        o += 2
    return s


def theta3_t(order_t, scale_q=1):
    s = np.zeros(order_t + 1, dtype=np.int64)
    s[0] = 1
    n = 1
    while True:
        exp = 4 * scale_q * n * n
        if exp > order_t:
            break
        s[exp] = 2
        n += 1
    return s


def theta4_t(order_t, scale_q=1):
    s = np.zeros(order_t + 1, dtype=np.int64)
    s[0] = 1
    n = 1
    while True:
        exp = 4 * scale_q * n * n
        if exp > order_t:
            break
        s[exp] = 2 * ((-1) ** n)
        n += 1
    return s


def fft_mul_i64(a: np.ndarray, b: np.ndarray, order: int) -> np.ndarray:
    nneed = order + 1
    N = 1
    while N < 2 * nneed:
        N *= 2
    out = np.fft.irfft(
        np.fft.rfft(a.astype(np.float64), N)
        * np.fft.rfft(b.astype(np.float64), N),
        N,
    )[:nneed]
    return np.rint(out).astype(np.int64)


def build_g_fft(qmax: int) -> np.ndarray:
    order_t = 4 * qmax
    s = np.zeros(order_t + 1, dtype=np.int64)
    s[0] = 1
    a0, a2, b0, b2, c0, c2 = WITNESS_KEY
    assert (a0, a2, b0, b2, c0, c2) == (0, 2, 0, 1, 1, 1)
    for _ in range(a2):
        s = fft_mul_i64(s, theta2_t(order_t, 2), order_t)
    for _ in range(b2):
        s = fft_mul_i64(s, theta3_t(order_t, 2), order_t)
    for _ in range(c0):
        s = fft_mul_i64(s, theta4_t(order_t, 1), order_t)
    for _ in range(c2):
        s = fft_mul_i64(s, theta4_t(order_t, 2), order_t)
    return s[0::4][: qmax + 1].astype(np.int64)


def odd_indices(m_max: int):
    return list(range(1, m_max + 1, 2))


def weight_d(d: int) -> float:
    return 1.0 / float(abs(d))


def alpha_naive(d: int, m: int, a_f8) -> int:
    tot = 0
    for j in sp.divisors(m):
        j = int(j)
        mj = m // j
        tot += (int(sp.mobius(j)) * kronecker(d, j)
                * (j ** (K_HALF - 1)) * a_f8[mj])
    return int(tot)


def alpha_sharp(d: int, m: int, a_f8) -> int:
    if m % 2 == 0:
        return 0
    return alpha_naive(d, m, a_f8)


def alpha_pk(ap: int, p: int, chi: int, k: int) -> int:
    """Local α(p^k) via T50/T61 recurrence (exact)."""
    if k == 0:
        return 1
    if k == 1:
        return int(ap - chi * p)
    a_prev2, a_prev1 = 1, int(ap - chi * p)
    for _ in range(2, k + 1):
        a_prev2, a_prev1 = a_prev1, int(ap * a_prev1 - (p ** 3) * a_prev2)
    return int(a_prev1)


def lambda_square_arith(ap, p, chi, kmax=4):
    """Square-plane von Mangoldt from α² (T61) — for contrast only."""
    u = [1]
    for k in range(1, kmax + 1):
        ak = alpha_pk(ap, p, chi, k)
        u.append(ak * ak)
    lam = [0] * (kmax + 1)
    for k in range(1, kmax + 1):
        acc = k * u[k]
        for j in range(1, k):
            acc -= lam[j] * u[k - j]
        lam[k] = acc
    return lam


def lambda_amp_local(ap, p, chi, kmax=4):
    """Amplitude-plane Λ(p^k)/log p from Dirichlet -L'/L.

    G(X)=Σ α(p^k) X^k, X=p^{-w}.  Since dX/dw=-log(p)·X,
    -L'/L gives Σ (Λ(p^k)/log p) X^k = X G'/G
    (plus sign).  Exact: G=(1−χ p X)/(1−a_p X+p³ X²).
    """
    alphas = [alpha_pk(ap, p, chi, k) for k in range(0, kmax + 1)]
    inv = [0.0] * (kmax + 1)
    inv[0] = 1.0 / alphas[0]
    for n in range(1, kmax + 1):
        s = 0.0
        for j in range(n):
            s += alphas[n - j] * inv[j]
        inv[n] = -s / alphas[0]
    # X G' coeffs m_n = n α_n; λ = (X G')*(1/G)
    lam = [0.0] * (kmax + 1)
    for n in range(1, kmax + 1):
        s = 0.0
        for j in range(1, n + 1):
            s += (j * alphas[j]) * inv[n - j]
        lam[n] = s
    return lam, alphas


# ================================================================ S0
print("=" * 72)
print("S0 -- ZERO-FIREWALL (AST) + rebuild g, f8")
print("=" * 72)

_SRC = inspect.getsource(inspect.getmodule(check))
_FORBIDDEN_AST = {
    "zeta" + "zero",
    "zeta" + "_zero",
    "zeta" + "_zeros",
    "siegel" + "z",
    "riemann" + "zeros",
    "riemann" + "_zero",
}
_tree = ast.parse(_SRC)
_call_names = set()
for node in ast.walk(_tree):
    if isinstance(node, ast.Call):
        f = node.func
        if isinstance(f, ast.Name):
            _call_names.add(f.id)
        elif isinstance(f, ast.Attribute):
            _call_names.add(f.attr)
_zero_calls = _call_names & _FORBIDDEN_AST
_attr_chain_hits = [
    node.attr for node in ast.walk(_tree)
    if isinstance(node, ast.Attribute) and node.attr in _FORBIDDEN_AST
]
_imported_names = set()
for node in ast.walk(_tree):
    if isinstance(node, ast.ImportFrom):
        for alias in node.names:
            _imported_names.add(alias.name)
    elif isinstance(node, ast.Import):
        for alias in node.names:
            _imported_names.add(alias.name)
_bad_imports = _imported_names & _FORBIDDEN_AST
check(
    "S0a ZERO-FIREWALL: AST has no Riemann-zero loader "
    f"(calls∩={sorted(_zero_calls)}; attrs={_attr_chain_hits}; "
    f"imports={sorted(_bad_imports)})",
    len(_zero_calls) == 0 and len(_attr_chain_hits) == 0
    and len(_bad_imports) == 0,
)
_exec_hits = [
    node.id for node in ast.walk(_tree)
    if isinstance(node, ast.Name) and node.id in _FORBIDDEN_AST
]
check(
    "S0b ZERO-FIREWALL: no forbidden zero-loader Name nodes "
    f"(hits={_exec_hits})",
    len(_exec_hits) == 0,
)
info("FENCE: amplitude-plane mapping only — no Weil-positivity / RH claim.")

t_f8 = time.time()
f8 = np.roll(conv_i64(eta_pass(2, 4, N_F8),
                      eta_pass(4, 4, N_F8), N_F8), 1)
f8[0] = 0
a_f8 = [int(f8[n]) for n in range(N_F8 + 1)]
info(f"f8 eta-product O(q^{N_F8}) in {time.time() - t_f8:.2f}s")
check(
    "S0.f8: a_1=1; HEAD_AP; a_even=0 on n≤200",
    a_f8[1] == 1
    and all(a_f8[p] == v for p, v in HEAD_AP.items())
    and all(a_f8[n] == 0 for n in range(2, 201, 2)),
)

t_g = time.time()
g = build_g_fft(QMAX)
info(f"g FFT rebuild O(q^{QMAX}) in {time.time() - t_g:.2f}s; head={list(g[:12])}")
mass_mod4 = {
    r: int(sum(abs(int(g[n])) for n in range(1, min(QMAX, 800) + 1)
               if n % 4 == r))
    for r in range(4)
}
info(f"|g| mass by n mod 4 (n≤800): {mass_mod4}")
check(
    "S0.g: T38/v537 witness; U4 fence (mass only n≡1,2 mod 4)",
    int(g[0]) == 0 and mass_mod4[0] == 0 and mass_mod4[3] == 0
    and mass_mod4[1] > 0 and mass_mod4[2] > 0,
)

live_all = [
    d for d in range(1, QMAX + 1, 2)
    if d % 8 == 1 and is_fundamental_discriminant(d) and int(g[d]) != 0
]
live = [d for d in live_all if d <= D_DIRAC]
bs = {d: int(g[d]) for d in live_all}
info(f"live fund d≡1 mod 8, b≠0: ≤{QMAX}: {len(live_all)}; "
     f"≤{D_DIRAC}: {len(live)}")
check(
    f"S0.family: #{len(live)} live fundamental d≤{D_DIRAC} (need ≥80)",
    len(live) >= 80,
)


# ================================================================ A1
print("=" * 72)
print("A1 -- DIRAC CONSTRUCTION D² = K (exact)")
print("=" * 72)
info("V[d,m] = √w_d · b(d) · χ_d(m),  w_d = |d|^{-1} (RTF-native)")
info("D = [[0, V],[Vᵀ, 0]]  on ℓ²(d) ⊕ ℓ²(odd m)")

ms = odd_indices(M_MAX)
nd, nm = len(live), len(ms)
info(f"window: #d={nd}, #m={nm} (odd m≤{M_MAX})")

# build V, K
Vraw = np.zeros((nd, nm), dtype=np.float64)
for j, d in enumerate(live):
    for i, m in enumerate(ms):
        Vraw[j, i] = float(kronecker(d, m))
ws = np.array([weight_d(d) for d in live], dtype=np.float64)
bvec = np.array([float(bs[d]) for d in live], dtype=np.float64)
scales = np.sqrt(np.maximum(ws, 0.0)) * bvec
V = Vraw * scales[:, None]
K = V.T @ V
Ghat = V @ V.T

# Dirac operator
D = np.zeros((nd + nm, nd + nm), dtype=np.float64)
D[:nd, nd:] = V
D[nd:, :nd] = V.T

# (i) self-adjoint
sym_err = float(np.linalg.norm(D - D.T, "fro")
                / (np.linalg.norm(D, "fro") + 1e-30))
info(f"D−Dᵀ relFrobenius = {sym_err:.3e}")
check(
    "A1.i: D = Dᵀ self-adjoint by construction "
    f"(relFrobenius {sym_err:.2e} < 1e-14)",
    sym_err < 1e-14,
)

# (ii) D² = diag(VVᵀ, VᵀV) and VᵀV = K
D2 = D @ D
block_dd = D2[:nd, :nd]
block_mm = D2[nd:, nd:]
block_off_1 = D2[:nd, nd:]
block_off_2 = D2[nd:, :nd]
err_dd = float(np.linalg.norm(block_dd - Ghat, "fro")
               / (np.linalg.norm(Ghat, "fro") + 1e-30))
err_mm = float(np.linalg.norm(block_mm - K, "fro")
               / (np.linalg.norm(K, "fro") + 1e-30))
err_off = float(np.linalg.norm(block_off_1, "fro")
                + np.linalg.norm(block_off_2, "fro"))
info(f"D² block: dd↔VVᵀ rel={err_dd:.3e}, mm↔VᵀV=K rel={err_mm:.3e}, "
     f"off Frobenius={err_off:.3e}")
# also rebuild K_T51 style from b²
K_b2 = np.zeros((nm, nm), dtype=np.float64)
for j, d in enumerate(live):
    chi = Vraw[j]
    K_b2 += ws[j] * (bvec[j] ** 2) * np.outer(chi, chi)
err_k = float(np.linalg.norm(K - K_b2, "fro")
              / (np.linalg.norm(K_b2, "fro") + 1e-30))
info(f"VᵀV vs Σ w b² χ⊗χ rel={err_k:.3e}")
check(
    "A1.ii: D² = diag(VVᵀ, VᵀV) exact and VᵀV = K = Σ w b² χ⊗χ "
    f"(rels dd={err_dd:.2e}, mm={err_mm:.2e}, K={err_k:.2e}; off={err_off:.2e})",
    err_dd < TOL and err_mm < TOL and err_k < TOL and err_off < 1e-8,
)

# (iii) spectrum of D = ± singular values of V
svals = np.linalg.svd(V, compute_uv=False)
# D is (nd+nm); nonzero eigs ±σ
eigs_D = np.linalg.eigvalsh(D)
eigs_D_sorted = np.sort(eigs_D)
# positive eigs of D should match svals (padded with zeros)
pos = eigs_D_sorted[eigs_D_sorted > TOL_SPEC]
neg = eigs_D_sorted[eigs_D_sorted < -TOL_SPEC]
pos = pos[::-1]  # descending
neg_abs = (-neg)  # ascending of |neg| → match ascending? use sort
pos_s = np.sort(pos)[::-1]
neg_s = np.sort(-neg)[::-1]
n_match = min(len(svals), len(pos_s), len(neg_s))
s_use = np.sort(svals)[::-1][:n_match]
if n_match > 0:
    rel_pos = float(np.linalg.norm(pos_s[:n_match] - s_use)
                    / (np.linalg.norm(s_use) + 1e-30))
    rel_neg = float(np.linalg.norm(neg_s[:n_match] - s_use)
                    / (np.linalg.norm(s_use) + 1e-30))
else:
    rel_pos = rel_neg = 0.0
# symmetry about 0
sym_spec = float(np.linalg.norm(np.sort(eigs_D) + np.sort(eigs_D)[::-1])
                 / (np.linalg.norm(eigs_D) + 1e-30))
info(f"spectrum: #pos={len(pos)}, #neg={len(neg)}, #svals>tol="
     f"{int(np.sum(svals > TOL_SPEC))}; rel± vs σ: "
     f"{rel_pos:.3e}/{rel_neg:.3e}; 0-symmetry rel={sym_spec:.3e}")
info(f"top σ: {s_use[:5]}")
check(
    "A1.iii: spectrum(D) = ± singular values of V (indefinite-symmetric "
    f"Dirac character); rel±={rel_pos:.2e}/{rel_neg:.2e}, "
    f"0-sym={sym_spec:.2e}",
    rel_pos < 1e-8 and rel_neg < 1e-8 and sym_spec < 1e-8
    and len(pos) == len(neg),
)

# (iv) Hecke equivariance
info("Hecke: m-side A_p (T51); modal Â_p=diag(χ_d(p)); "
     "d-side Shimura b(dp²)=b(d)·α_d^♯(p)")


def hecke_matrix(ms_list, p: int):
    idx = {m: i for i, m in enumerate(ms_list)}
    A = np.zeros((len(ms_list), len(ms_list)), dtype=np.float64)
    for m in ms_list:
        i = idx[m]
        pm = p * m
        if pm in idx:
            A[i, idx[pm]] += 1.0
        if m % p == 0:
            mp = m // p
            if mp in idx:
                A[i, idx[mp]] += 1.0  # κ=0
    return A


def interior_free_mask(ms_list, p: int):
    mset = set(ms_list)
    return np.array([
        (m % p != 0) and (p * m in mset)
        for m in ms_list
    ], dtype=bool)


hecke_m_ok = True
hecke_rows = []
for p in HECKE_PS:
    A = hecke_matrix(ms, p)
    free = interior_free_mask(ms, p)
    Ah = np.diag(np.array([float(kronecker(d, p)) for d in live]))
    # T51: A χ = χ(p) χ on p-free ⇒ V @ A.T = Â @ V on free columns.
    max_res = 0.0
    for j, d in enumerate(live):
        chi = Vraw[j]
        lam = float(kronecker(d, p))
        if lam == 0.0:
            continue
        Ach = A @ chi
        res = float(np.linalg.norm((Ach - lam * chi)[free])
                    / (np.linalg.norm(chi[free]) + 1e-30))
        max_res = max(max_res, res)
    # matrix form with signed V: (V @ A.T - Ah @ V) on free cols
    # Since A may not equal A.T, use column-eigen test above + 
    # V_free intertwining via Ah @ V[:,free] vs action
    VA = V @ A.T
    AhV = Ah @ V
    res_mat = float(np.linalg.norm((VA - AhV)[:, free], "fro")
                    / (np.linalg.norm(V[:, free], "fro") + 1e-30))
    hecke_rows.append((p, max_res, res_mat, int(free.sum())))
    info(f"  p={p}: χ-eigen p-free maxres={max_res:.3e}; "
         f"V Aᵀ=Â V free rel={res_mat:.3e} (#free={int(free.sum())})")
    hecke_m_ok = hecke_m_ok and (max_res < 1e-12) and (res_mat < 1e-10)

check(
    "A1.iv.m: modal m-side intertwining V Aᵀ = Â V on p-free locus "
    f"exact for p={HECKE_PS} (T51 reading)",
    hecke_m_ok,
)

# d-side Shimura: b(d p²) = b(d) α_d^♯(p) for live d with d p² ≤ QMAX
shimura_ok = True
shimura_n = 0
shimura_fail = 0
for d in live:
    bd = bs[d]
    for p in HECKE_PS:
        n = d * p * p
        if n > QMAX:
            continue
        ash = alpha_sharp(d, p, a_f8)
        pred = bd * ash
        got = int(g[n])
        shimura_n += 1
        if got != pred:
            shimura_fail += 1
            shimura_ok = False
            if shimura_fail <= 3:
                info(f"  FAIL Shimura d={d} p={p}: g[n]={got} pred={pred}")
info(f"Shimura d↦dp² checks: {shimura_n}, fails={shimura_fail}")

# d-side modal: [Ĝ, Â] = Ĝ ⊙ (λ_j − λ_i) exact (T51)
modal_d_ok = True
for p in HECKE_PS:
    lam = np.array([float(kronecker(d, p)) for d in live])
    Ah = np.diag(lam)
    comm = Ghat @ Ah - Ah @ Ghat
    pred = Ghat * (lam[None, :] - lam[:, None])
    match = float(np.linalg.norm(comm - pred, "fro")
                  / (np.linalg.norm(pred, "fro") + 1e-30 + 1.0))
    # when pred≈0 use absolute
    abs_err = float(np.linalg.norm(comm - pred, "fro"))
    info(f"  modal [Ĝ,Â_p] p={p}: match_rel={match:.3e}, abs={abs_err:.3e}")
    modal_d_ok = modal_d_ok and (abs_err < 1e-8 * (np.linalg.norm(Ghat) + 1))

check(
    "A1.iv.d: Shimura b(dp²)=b(d)·α_d^♯(p) exact on window + "
    "modal [Ĝ,Â_p]=Ĝ⊙(λ_j−λ_i) exact (T50/T51 d-side)",
    shimura_ok and shimura_n >= 100 and modal_d_ok,
)

A1_hecke_ok = hecke_m_ok and shimura_ok and modal_d_ok
A1_exact = (sym_err < 1e-14 and err_dd < TOL and err_mm < TOL
            and err_k < TOL and rel_pos < 1e-8 and A1_hecke_ok)
info(f"A1 aggregate exact={A1_exact}; Hecke-equivariant={A1_hecke_ok}")


# ================================================================ A2
print("=" * 72)
print("A2 -- AMPLITUDE TOWERS = DEGREE-2 EULER (structural heart)")
print("=" * 72)
info("T_d^amp(w) = Σ_m α_d^♯(m) m^{-w}  (LINEAR — not squared)")
info("Local derivation: α(p^k) = a_p α(p^{k-1}) − p³ α(p^{k-2}),")
info("  α(1)=1, α(p)=a_p − χ_d(p)·p")
info("  ⇒ G_p(X) = Σ α(p^k) X^k = (1 − χ p X)/(1 − a_p X + p³ X²)")
info("  = L(f₈,w)_p / L(χ_d, w−1)_p   (odd part; classical Dirichlet)")
info("NOTE vs preregistered expectation L(f₈×χ_d): the twist sits in")
info("  the linear numerator (Dirichlet L), NOT in the a_p-coefficient.")
info("  Pure twisted Hecke 1/(1−χ a_p X+χ² p³ X²) is a DIFFERENT series.")

# Algebraic identity via sympy
X, a_s, p_s, chi_s = sp.symbols("X a p chi")
A0, A1 = 1, a_s - chi_s * p_s
A2 = sp.expand(a_s * A1 - p_s ** 3 * A0)
A3 = sp.expand(a_s * A2 - p_s ** 3 * A1)
A4 = sp.expand(a_s * A3 - p_s ** 3 * A2)
G_closed = (1 - chi_s * p_s * X) / (1 - a_s * X + p_s ** 3 * X ** 2)
# series of closed form to X^4
G_series = G_closed.series(X, 0, 5).removeO()
coeffs_closed = [sp.expand(G_series.coeff(X, k)) for k in range(5)]
coeffs_rec = [A0, A1, A2, A3, A4]
alg_ok = all(sp.expand(coeffs_closed[k] - coeffs_rec[k]) == 0
             for k in range(5))
info(f"algebraic G vs recurrence coeffs: {[sp.simplify(c) for c in coeffs_rec]}")
check(
    "A2.algebraic: G_p=(1−χ p X)/(1−a_p X+p³ X²) matches α-recurrence "
    "coeffs k=0..4 (sympy exact)",
    alg_ok,
)

# No (1-p³X) factor: denominator of G is Hecke poly of UN-twisted f₈;
# the square-plane tower has extra (1-p³X) in D (T57/T61).
den_amp = 1 - a_s * X + p_s ** 3 * X ** 2
den_at = sp.expand(den_amp.subs(X, 1 / p_s ** 3))
# den(p^{-3}) = 1 - a/p³ + 1/p³ = (p³ - a + 1)/p³ ≢ 0 as a polynomial in a,p
no_flat = sp.simplify(den_at * p_s ** 3) != 0
info(f"den(X=p^{{-3}})·p³ = {sp.simplify(den_at * p_s ** 3)} "
     "(≢0 ⇒ no universal (1−p³X) factor)")
check(
    "A2.no-flat: amplitude Euler has NO universal (1−p³X)=ζ(w−3)_p "
    "factor (the square-plane ♭/doubling seed is absent)",
    no_flat,
)

# Coefficientwise check on ≥8 towers, m≤200
towers = live[:max(N_TOWERS, 8)]
# ensure diverse χ patterns
extra = []
for d in live:
    if d in towers:
        continue
    if len(towers) + len(extra) >= N_TOWERS:
        break
    extra.append(d)
towers = (towers + extra)[:N_TOWERS]
info(f"towers d={towers}")

euler_ok = True
euler_max_rel = 0.0
for d in towers:
    chi_cache = {}
    # build α^♯(m) for odd m≤M_EULER two ways: Shimura sum vs Euler product
    odd_ms = list(range(1, M_EULER + 1, 2))
    alpha_direct = []
    alpha_euler = []
    for m in odd_ms:
        ad = alpha_sharp(d, m, a_f8)
        alpha_direct.append(ad)
        # multiplicative from local α_pk
        fac = sp.factorint(m)
        val = 1
        good = True
        for p, e in fac.items():
            p = int(p)
            e = int(e)
            if p == 2:
                good = False
                break
            if p not in chi_cache:
                chi_cache[p] = kronecker(d, p)
            if p >= len(a_f8):
                good = False
                break
            val *= alpha_pk(a_f8[p], p, chi_cache[p], e)
        alpha_euler.append(val if good else None)
    mismatches = 0
    compared = 0
    for m, ad, ae in zip(odd_ms, alpha_direct, alpha_euler):
        if ae is None:
            continue
        compared += 1
        if ad != ae:
            mismatches += 1
            if mismatches <= 2:
                info(f"  mismatch d={d} m={m}: direct={ad} euler={ae}")
    # Dirichlet partial sums vs Euler product at a test w
    w_test = 4.0
    S_dir = 0.0
    for m, ad in zip(odd_ms, alpha_direct):
        S_dir += ad / (m ** w_test)
    # Euler product over odd p≤M_EULER
    S_eul = 1.0
    for p in sp.primerange(3, M_EULER + 1):
        p = int(p)
        ap = a_f8[p]
        chi = kronecker(d, p)
        X = p ** (-w_test)
        Gp = (1.0 - chi * p * X) / (1.0 - ap * X + (p ** 3) * X * X)
        S_eul *= Gp
    # truncate error: both miss m with large prime factors similarly;
    # compare ratio of partial Euler (expand to m≤M) vs direct
    # Better: expand local factors multiplicatively up to M_EULER
    coeff = np.zeros(M_EULER + 1, dtype=np.float64)
    coeff[1] = 1.0
    for p in sp.primerange(3, M_EULER + 1):
        p = int(p)
        ap = a_f8[p]
        chi = kronecker(d, p)
        # local α(p^k)
        lok = [alpha_pk(ap, p, chi, k) for k in range(0, 8)]
        new = np.zeros_like(coeff)
        for n in range(1, M_EULER + 1):
            if coeff[n] == 0.0:
                continue
            pk = 1
            for k in range(0, 8):
                if n * pk > M_EULER:
                    break
                new[n * pk] += coeff[n] * lok[k]
                pk *= p
        coeff = new
    S_eul_trunc = 0.0
    for m in odd_ms:
        S_eul_trunc += coeff[m] / (m ** w_test)
    rel = abs(S_dir - S_eul_trunc) / max(abs(S_dir), 1e-30)
    euler_max_rel = max(euler_max_rel, rel)
    info(f"  d={d}: α-mult mismatches={mismatches}/{compared}; "
         f"Dirichlet vs Euler-trunc at w=4 rel={rel:.3e}; "
         f"T_dir={S_dir:.6g}")
    if mismatches > 0 or rel > 1e-10:
        euler_ok = False

check(
    f"A2.coeff: Grad-2 Euler G_p=(1−χp X)/(1−a_p X+p³ X²) exact on "
    f"{len(towers)} towers, odd m≤{M_EULER} "
    f"(max Dirichlet-rel {euler_max_rel:.2e})",
    euler_ok and len(towers) >= 8,
)

# Twisted-L expectation is FALSE for α — document kill of that reading
twist_mismatch = 0
twist_checked = 0
d0 = towers[0]
for p in (3, 5, 7, 11, 13):
    ap = a_f8[p]
    chi = kronecker(d0, p)
    # α(p) from T50 vs χ a_p from L(f×χ)
    a_sh = alpha_pk(ap, p, chi, 1)
    a_twist = chi * ap
    twist_checked += 1
    if a_sh != a_twist:
        twist_mismatch += 1
info(f"α(p)=a_p−χp vs χ a_p (twisted): mismatches "
     f"{twist_mismatch}/{twist_checked} on d={d0}")
check(
    "A2.not-twisted-L: α-series is L(f)/L(χ,w−1), NOT L(f×χ) "
    f"(α(p)=a_p−χp ≠ χ a_p for sample; mismatches={twist_mismatch})",
    twist_mismatch == twist_checked and twist_checked >= 3,
)

# Λ_amp vs Λ_square contrast
info("Λ_amp(p^k)/log p from X ∂_X log G (Dirichlet −L'/L, LINEAR α);")
info("Λ_sq from α²-recurrence (T61); ST-targets:")
info("  amp: E_ST[χ_1]=0 ⇒ NO ζ-kernel; E_ST[2cos]=(0,−1,0,0)")
info("  sq:  E_ST[Φ]=(1,0,2,0) ⇒ ζ-kernel + even-power doubling")

AHAT = sp.symbols("ahat")
# ST: E_ST[χ_n]=δ_{n0} with χ_n=U_n(cos θ) (classical).
# 2cos(kθ) = χ_1 (k=1); = χ_k − χ_{k−2} (k≥2).
# ⇒ E_ST[2cos(kθ)] = [0, −1, 0, 0] for k=1..4
# Leading amplitude channel is χ_1 with E_ST=0 ⇒ NO ζ-kernel.
# (k=2 has E_ST=−1 from −χ_0 — NOT the square-plane ζ-seed;
#  square Φ_1=χ_0+χ_2 has E_ST=+1.)


def two_cos_k_in_chi(k):
    if k == 0:
        return {0: 1}
    if k == 1:
        return {1: 1}
    return {k: 1, k - 2: -1}


st_amp = []
for k in range(1, 5):
    cf = two_cos_k_in_chi(k)
    st_amp.append(int(cf.get(0, 0)))
est_chi1 = int(two_cos_k_in_chi(1).get(0, 0))
info(f"E_ST[2cos(kθ)] k=1..4 = {st_amp}; E_ST[χ_1]={est_chi1} "
     "(χ_1-channel has no ζ-core; k=2 weight −1 ≠ square Φ)")

# numeric Λ_amp and Λ_sq at sample p, χ=±1,0
lam_amp_samples = {}
lam_sq_samples = {}
for p, chi in ((3, 1), (5, -1), (7, 0), (11, 1)):
    ap = a_f8[p]
    lam_a, _ = lambda_amp_local(ap, p, chi, 4)
    lam_s = lambda_square_arith(ap, p, chi, 4)
    lam_amp_samples[(p, chi)] = [lam_a[k] for k in range(1, 5)]
    lam_sq_samples[(p, chi)] = [lam_s[k] for k in range(1, 5)]
    info(f"  p={p} χ={chi:+d}: Λ_amp/log={['%.4g' % lam_a[k] for k in range(1,5)]}")
    info(f"           Λ_sq /p^{{3k}} proxy raw={lam_s[1:5]}")

# unitary amp weights: Λ_amp(p^k)/(log p)/ p^{3k/2} ≈ 2cos(kθ) for χ=0
# (when χ=0, G=1/D pure)
p_u, chi_u = 5, 0
ap_u = a_f8[p_u]
lam_u, _ = lambda_amp_local(ap_u, p_u, chi_u, 4)
ahat = ap_u / (p_u ** 1.5)
theta = math.acos(max(-1.0, min(1.0, ahat / 2.0)))
cheb = [2 * math.cos(k * theta) for k in range(1, 5)]
unit = [lam_u[k] / (p_u ** (1.5 * k)) for k in range(1, 5)]
cheb_rel = float(np.linalg.norm(np.array(unit) - np.array(cheb))
                 / (np.linalg.norm(cheb) + 1e-30))
info(f"χ=0 unitary: Λ_amp/p^{{3k/2}}={['%.6f' % u for u in unit]}")
info(f"             2cos(kθ)     ={['%.6f' % c for c in cheb]} rel={cheb_rel:.2e}")

# Square ST target [1,0,2,0] from T61 Φ-expansion (classical CG)
st_sq = [1, 0, 2, 0]
# Square ST kills k=2 (Φ-weight 0); amplitude Chebyshev k=2 is nonzero
even_amp_nonzero = abs(cheb[1]) > 1e-6 and abs(unit[1]) > 1e-6
check(
    "A2.Lambda: Λ_amp = Chebyshev 2cos(kθ) (χ=0 exact, rel"
    f"={cheb_rel:.2e}); E_ST[χ_1]=0 (no ζ); E_ST[2cos]= {st_amp} "
    f"(k=2 weight {unit[1]:.4f}≠0 — no square-style even kill); "
    f"contrast Λ_sq ST={st_sq}",
    cheb_rel < 1e-10 and est_chi1 == 0 and st_amp == [0, -1, 0, 0]
    and even_amp_nonzero and st_sq == [1, 0, 2, 0],
)

A2_exact = (alg_ok and no_flat and euler_ok and cheb_rel < 1e-10
            and est_chi1 == 0)


# ================================================================ A3
print("=" * 72)
print("A3 -- METAPLECTIC DATUM: signs of b(d)")
print("=" * 72)
info("CLASSICAL: Waldspurger determines b²; sign of half-integral")
info("  coefficients is a deep datum (Kohnen — named as classical).")

signs = np.array([1 if bs[d] > 0 else -1 for d in live])
n_pos = int(np.sum(signs > 0))
n_neg = int(np.sum(signs < 0))
frac_pos = n_pos / len(live)
frac_neg = n_neg / len(live)
info(f"sgn(b): +={n_pos} ({frac_pos:.4f}), −={n_neg} ({frac_neg:.4f}), "
     f"N={len(live)}")

# fluctuation with D
sign_ladder = []
for Dcut in (500, 1000, 2000, 5000):
    sub = [d for d in live if d <= Dcut]
    if not sub:
        continue
    fp = sum(1 for d in sub if bs[d] > 0) / len(sub)
    sign_ladder.append((Dcut, len(sub), fp, 1 - fp))
    info(f"  D≤{Dcut}: N={len(sub)}, frac+={fp:.4f}, frac−={1-fp:.4f}")
check(
    "A3.i: sign distribution recorded; both signs present "
    f"(frac+={frac_pos:.3f}, frac−={frac_neg:.3f}; ladder={len(sign_ladder)})",
    n_pos > 0 and n_neg > 0 and abs(frac_pos - 0.5) < 0.25
    and len(sign_ladder) >= 3,
)

# Fibre test (T62 σ-patterns)
fibres = defaultdict(list)
for d in live:
    sig = tuple(kronecker(d, p) for p in PATTERN_PRIMES)
    fibres[sig].append(d)

n_fibres = len(fibres)
mixed = 0
pure_pos = 0
pure_neg = 0
fibre_entropy_num = 0.0  # Σ μ_f H(sgn|f)
fibre_mass_tot = 0.0
mixed_mass = 0.0
for sig, ds in fibres.items():
    sgs = [1 if bs[d] > 0 else -1 for d in ds]
    n_p = sum(1 for s in sgs if s > 0)
    n_m = len(sgs) - n_p
    mass = float(sum(weight_d(d) * abs(bs[d]) for d in ds))  # amp mass
    # use count-mass for entropy
    cnt = float(len(ds))
    fibre_mass_tot += cnt
    if n_p > 0 and n_m > 0:
        mixed += 1
        mixed_mass += cnt
        p_plus = n_p / cnt
        # binary entropy
        H = 0.0
        for pr in (p_plus, 1 - p_plus):
            if pr > 0:
                H -= pr * math.log(pr, 2)
        fibre_entropy_num += cnt * H
    elif n_p > 0:
        pure_pos += 1
    else:
        pure_neg += 1

H_cond = fibre_entropy_num / max(fibre_mass_tot, 1.0)
frac_mixed = mixed / max(n_fibres, 1)
frac_mixed_mass = mixed_mass / max(fibre_mass_tot, 1.0)
info(f"fibres nonempty: {n_fibres}; pure+: {pure_pos}, pure−: {pure_neg}, "
     f"mixed: {mixed} ({frac_mixed:.3f})")
info(f"mass-weighted mixed fraction: {frac_mixed_mass:.4f}; "
     f"H(sgn|σ)={H_cond:.4f} bits (0=character-determined)")
# If signs were character-determined, H=0 and mixed=0
genuine_phase = (mixed > 0 and H_cond > 0.1)
check(
    "A3.ii: fibre test — signs VARY inside σ-fibres "
    f"(mixed={mixed}/{n_fibres}={frac_mixed:.3f}, H(sgn|σ)={H_cond:.3f}) "
    "⇒ metaplectic residual beyond characters"
    if genuine_phase else
    "A3.ii: fibre test — signs CONSTANT on σ-fibres "
    f"(mixed={mixed}, H={H_cond:.3f}) ⇒ character-determined phase",
    True,  # both outcomes valid; assert bookkeeping
)
check(
    "A3.ii.data: fibre census consistent "
    f"(pure++pure−+mixed={pure_pos + pure_neg + mixed} == {n_fibres})",
    pure_pos + pure_neg + mixed == n_fibres and n_fibres >= 8,
)

# Correlations vs proxies
# Classical twist root number ε(d)=χ_d(8) is CONSTANT +1 on the live
# d≡1 mod 8 class (T45) — cannot explain signs (documented degeneracy).
rn8 = np.array([kronecker(d, 8) for d in live], dtype=float)
rn8_const = bool(np.std(rn8) < 1e-12)
info(f"  twist root-number proxy χ_d(8): unique values="
     f"{sorted(set(int(x) for x in rn8))}; constant_on_live={rn8_const}")

proxies = {
    "mod16_1": np.array([1 if d % 16 == 1 else -1 for d in live]),
    "mod32_odd": np.array([1 if (d % 32) in (1, 17) else -1 for d in live]),
    "chi_m1": np.array([kronecker(d, -1) for d in live]),
}
corr_rows = {}
for name, prox in proxies.items():
    prox_f = prox.astype(float)
    if float(np.std(prox_f)) < 1e-12:
        info(f"  corr sgn vs {name}: DEGENERATE (constant on live class)")
        corr_rows[name] = (0.0, None)
        continue
    agree = float(np.mean(signs == prox))
    c = float(np.corrcoef(signs.astype(float), prox_f)[0, 1])
    info(f"  corr sgn vs {name}: Pearson={c:.4f}, agree={agree:.4f}")
    corr_rows[name] = (c, agree)

abs_corr = float(np.corrcoef(signs.astype(float),
                             np.log([float(d) for d in live]))[0, 1])
info(f"  corr sgn vs log|d|: Pearson={abs_corr:.4f}")
corr_rows["log_abs_d"] = (abs_corr, None)

max_abs_corr = max(abs(v[0]) for v in corr_rows.values()
                   if v[0] == v[0])  # skip nan
if genuine_phase and max_abs_corr < 0.35 and rn8_const:
    sign_typing = ("GENUINE-METAPLECTIC-RESIDUAL: signs vary inside "
                   "σ-fibres; twist root number χ_d(8) constant on live "
                   "class; tested mod16/32/|d| proxies weak "
                   f"(max |ρ|={max_abs_corr:.3f}) — classical Kohnen-depth "
                   "datum; Waldspurger blind to sign")
elif genuine_phase:
    sign_typing = ("MIXED: fibre-variable signs with partial proxy "
                   f"correlation (max |ρ|={max_abs_corr:.3f})")
else:
    sign_typing = ("CHARACTER-DETERMINED: signs constant on σ-fibres "
                   "(trivial phase)")
info(f"TYPING: {sign_typing}")
check(
    "A3.iii: correlation battery recorded "
    f"(χ_d(8) constant={rn8_const}; "
    f"mod16 ρ={corr_rows['mod16_1'][0]:.3f}, "
    f"mod32 ρ={corr_rows['mod32_odd'][0]:.3f}, "
    f"log|d| ρ={abs_corr:.3f}); max|ρ|={max_abs_corr:.3f}",
    rn8_const and "mod16_1" in corr_rows and max_abs_corr < 0.5,
)
check(
    f"A3.iv: honest typing issued ({sign_typing[:40]}…)",
    len(sign_typing) > 20,
)

A3_characterized = genuine_phase  # expected: genuine residual


# ================================================================ A4
print("=" * 72)
print("A4 -- CATEGORICAL SEESAW (amplitude ↔ square)")
print("=" * 72)
info("Clebsch–Gordan (classical): χ₁ × χ₁ = χ₀ + χ₂")
info("  Amplitude Λ_amp ~ χ₁ weights ⇒ E_ST[χ₁]=0 ⇒ NO ζ-kernel")
info("  Square: χ₁×χ₁ projects onto χ₀ ⇒ ζ-kernel + Minus/♭ (T63/T64)")

# Quantitative: ST moments already in A2
seesaw_amp_no_zeta = (est_chi1 == 0)  # χ₁-channel: no ζ
seesaw_sq_has_zeta = (st_sq == [1, 0, 2, 0])
info(f"amp E_ST[χ_1]={est_chi1}, E_ST[2cos]={st_amp}; "
     f"sq E_ST[Φ]={st_sq} (ζ at k=1,3)")
check(
    "A4.seesaw: amplitude E_ST[χ₁]=0 (no ζ-kernel / no Minus seed) vs "
    "square E_ST[Φ]=(1,0,2,0) (ζ-kernel + even doubling) — exact CG "
    f"(amp 2cos ST={st_amp} ≠ sq)",
    seesaw_amp_no_zeta and seesaw_sq_has_zeta
    and st_amp != st_sq,
)

# Polarisation: V = V₊ − V₋ with |b|
pos_idx = [j for j, d in enumerate(live) if bs[d] > 0]
neg_idx = [j for j, d in enumerate(live) if bs[d] < 0]
Vplus = np.zeros_like(V)
Vminus = np.zeros_like(V)
for j in pos_idx:
    Vplus[j] = np.sqrt(ws[j]) * abs(bvec[j]) * Vraw[j]
for j in neg_idx:
    Vminus[j] = np.sqrt(ws[j]) * abs(bvec[j]) * Vraw[j]

V_signed = Vplus - Vminus
V_abs = Vplus + Vminus
err_vs = float(np.linalg.norm(V_signed - V, "fro")
               / (np.linalg.norm(V, "fro") + 1e-30))
info(f"V = V₊ − V₋ reconstruction rel={err_vs:.3e} "
     f"(#+= {len(pos_idx)}, #−={len(neg_idx)})")
check(
    "A4.polarisation: V = V₊ − V₋ exact with (V±)_{d}=√w |b| χ · 1_{±} "
    f"(rel {err_vs:.2e})",
    err_vs < 1e-14,
)

K_pp = Vplus.T @ Vplus
K_mm = Vminus.T @ Vminus
K_pm = Vplus.T @ Vminus
K_mp = Vminus.T @ Vplus
# row-partition ⇒ K_pm = 0 (orthogonal d-supports)
pm_fro = float(np.linalg.norm(K_pm, "fro"))
mp_fro = float(np.linalg.norm(K_mp, "fro"))
K_from_pol = K_pp + K_mm - K_pm - K_mp
K_abs = V_abs.T @ V_abs
K_abs_from = K_pp + K_mm + K_pm + K_mp
err_Kpol = float(np.linalg.norm(K_from_pol - K, "fro")
                 / (np.linalg.norm(K, "fro") + 1e-30))
err_Kabs = float(np.linalg.norm(K_abs - K_abs_from, "fro")
                 / (np.linalg.norm(K_abs, "fro") + 1e-30))
# Key: K vs K_abs — with row partition K_pm=0 ⇒ K = K_abs = K_pp+K_mm
K_vs_abs = float(np.linalg.norm(K - K_abs, "fro")
                 / (np.linalg.norm(K, "fro") + 1e-30))
info(f"K_pm Frobenius={pm_fro:.3e} (row-partition ⇒ 0)")
info(f"K=(V₊−V₋)ᵀ(V₊−V₋) rel err={err_Kpol:.3e}")
info(f"K_abs=(V₊+V₋)ᵀ(V₊+V₋) rel err={err_Kabs:.3e}")
info(f"K vs K_abs rel={K_vs_abs:.3e}  "
     "(Waldspurger: K sees only b² — signs cancel)")

# d-space Gram DOES feel signs
G_signed = V @ V.T
G_abs = V_abs @ V_abs.T
# block structure
def block_fro(G, I, J):
    if not I or not J:
        return 0.0
    return float(np.linalg.norm(G[np.ix_(I, J)], "fro"))

Gpp = block_fro(G_signed, pos_idx, pos_idx)
Gmm = block_fro(G_signed, neg_idx, neg_idx)
Gpm_s = block_fro(G_signed, pos_idx, neg_idx)
Gpm_a = block_fro(G_abs, pos_idx, neg_idx)
# Entry-sum (not Frobenius): signed cross mass vs abs cross mass
# Ĝ_ij ∝ b_i b_j ⟨χ_i,χ_j⟩ — opposite signs flip the entry
cross_sum_s = float(np.sum(G_signed[np.ix_(pos_idx, neg_idx)]))
cross_sum_a = float(np.sum(G_abs[np.ix_(pos_idx, neg_idx)]))
info(f"Ĝ_signed blocks Frobenius: ++={Gpp:.6g}, −−={Gmm:.6g}, "
     f"+−={Gpm_s:.6g}")
info(f"Ĝ +− ENTRY-SUM: signed={cross_sum_s:.6g}, abs={cross_sum_a:.6g} "
     f"(ratio signed/abs={cross_sum_s / max(abs(cross_sum_a), 1):.4f})")
cross_ratio_s = Gpm_s / max(Gpp + Gmm, 1e-30)
info(f"cross/diag Frobenius: {cross_ratio_s:.4f}")

tr_K = float(np.trace(K))
tr_Kabs = float(np.trace(K_abs))
info(f"tr K={tr_K:.6g}, tr K_abs={tr_Kabs:.6g}, "
     f"relΔ={abs(tr_K - tr_Kabs) / max(tr_K, 1):.3e}")

# Ĝ signed ≠ Ĝ abs (entrywise) even when Frobenius of blocks match
G_diff = float(np.linalg.norm(G_signed - G_abs, "fro")
               / (np.linalg.norm(G_abs, "fro") + 1e-30))
info(f"Ĝ_signed vs Ĝ_abs relFrobenius={G_diff:.4f}")

if K_vs_abs < 1e-10 and G_diff > 1e-6:
    pol_finding = (
        "SIGNS-BLIND-ON-K / SIGNS-LIVE-IN-Ĝ: K ≡ K_abs exactly "
        "(row-partition K₊₋=0; Waldspurger b² — signs do NOT steer "
        "m-side ζ-kernel of K).  But Ĝ_signed ≠ Ĝ_abs "
        f"(rel {G_diff:.4f}; +− entry-sum signed={cross_sum_s:.4g} vs "
        f"abs={cross_sum_a:.4g}): phase lives in the indefinite "
        "Dirac/d-space Gram.  Canonical positivity polarisation OPEN."
    )
elif K_vs_abs < 1e-10:
    pol_finding = (
        "SIGNS-BLIND-ON-K: K ≡ K_abs (Waldspurger b²).  "
        "Canonical positivity polarisation remains OPEN."
    )
else:
    pol_finding = (
        f"SIGNS-STEER-K: K and K_abs differ (rel {K_vs_abs:.3e}) — "
        "metaplectic phase feeds the square kernel."
    )
info(f"POLARISATION FINDING: {pol_finding}")
check(
    "A4.K-structure: K=(V₊−V₋)ᵀ(V₊−V₋)=K₊₊+K₋₋−2K₊₋ with "
    f"K₊₋=0 by d-partition; K vs K_abs rel={K_vs_abs:.2e}",
    err_Kpol < TOL and pm_fro < 1e-8 and K_vs_abs < 1e-10,
)
check(
    "A4.zeta-steering: m-side K sign-blind (Waldspurger); "
    f"Ĝ feels signs (Ĝ_signed≠Ĝ_abs rel={G_diff:.4f}; "
    f"+− sum signed/abs={cross_sum_s:.4g}/{cross_sum_a:.4g})",
    K_vs_abs < 1e-10 and G_diff > 0.01
    and abs(cross_sum_s - cross_sum_a) > 1.0,
)

A4_quantified = (seesaw_amp_no_zeta and seesaw_sq_has_zeta
                 and err_vs < 1e-14 and K_vs_abs < 1e-10)


# ================================================================ A5
print("=" * 72)
print("A5 -- SYNTHESIS + THINKING-PAUSE MAP")
print("=" * 72)

struct_eq = (
    "AMPLITUDE: T_d^amp = L(f₈)/L(χ_d,·−1) = Grad-2 Euler "
    "(1−χpX)/(1−a_p X+p³X²);  D=[[0,V],[Vᵀ,0]], D²=diag(VVᵀ,K);  "
    "Λ_amp ~ χ₁ (E_ST=0).  SQUARE: sym²/α² Euler with (1−p³X) "
    "⇒ ζ-kernel + Minus/♭; K=VᵀV sees only b²."
)
info(f"STRUCTURE: {struct_eq}")

props = {
    "Hecke-equivariant": A1_hecke_ok,
    "Grad-2-Euler": A2_exact,
    "genuine-phase-datum": bool(A3_characterized),
    "polarisation-mapped": A4_quantified,
}
for k, v in props.items():
    info(f"  half-object must have {k}: {'YES ✓' if v else 'NO ✗'}")

boundary = (
    "MAPPED: Dirac D, Grad-2 amplitude Euler, sign statistics / "
    "fibre residual, categorical seesaw (CG), polarisation algebra "
    "K=K_abs (sign-blind).  OPEN (theory step, not this probe): "
    "canonical Krein/metaplectic polarisation that produces the "
    "ζ-kernel WITH positive sign upon squaring — the actual "
    "positivity problem.  Fence: no Weil-positivity claim."
)
info(f"BOUNDARY: {boundary}")

# Verdict
if A1_exact and A2_exact and A3_characterized and A4_quantified:
    verdict = "DIRAC-SQRT-EXACT"
elif (not A1_hecke_ok) or (not A2_exact):
    verdict = "OBSTRUCTED"
    if not A1_hecke_ok:
        info("OBSTRUCTION: Hecke intertwining of naive Dirac failed")
    if not A2_exact:
        info("OBSTRUCTION: Grad-2 Euler of amplitude towers failed")
else:
    verdict = "PARTIAL"

info(f"VERDICT: {verdict}")
check(
    f"A5.verdict: {verdict} "
    f"(A1_exact={A1_exact}, A2_exact={A2_exact}, "
    f"A3_phase={A3_characterized}, A4={A4_quantified})",
    verdict in ("DIRAC-SQRT-EXACT", "PARTIAL", "OBSTRUCTED"),
)

promo = (
    "PROMOTION TYPING (no promotion executed): if A1+A2 exact — "
    "candidate module would be a structural amplitude/Dirac companion "
    "to v537–v539 (mapping certificate, NOT a positivity / RH claim). "
    "Decision reserved for project lead.  This probe does NOT promote."
)
info(promo)
check(
    "A5.no-promotion: sandbox mapping only; promotion typed not executed",
    True,
)
check(
    "A5.structure-equation: one-line amplitude-plane equation issued",
    "Grad-2" in struct_eq and "D=" in struct_eq.replace(" ", ""),
)


# ================================================================ end
print("=" * 72)
elapsed = time.time() - T0
print(f"TOTAL: {PASS} passed, {FAIL} failed  ({elapsed:.1f}s)")
print(f"VERDICT: {verdict}")
print(f"A3 typing: {sign_typing}")
print(f"A4 polarisation: {pol_finding}")
print("=" * 72)
raise SystemExit(0 if FAIL == 0 else 1)
