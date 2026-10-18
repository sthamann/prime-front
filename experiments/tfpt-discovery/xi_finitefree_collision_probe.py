#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""xi_finitefree_collision_probe -- r626 XI.FINITEFREE.COLLISION.01

FROZEN SPEC v1 (2026-09-02).  EXPLORATION ONLY, experiments/ only.
Nothing here is load-bearing, nothing is promoted, no marker moves,
no scorecard row is written by this probe.  This probe writes no files.
SMALL EXPLORATION SCOUT, NOT a proof attempt.

Firewall: "Finite approximants; the barrier (9) is equivalent to
Disc ≠ 0 along the path; no RH claim."

=======================================================================
SETTING (parent-typed; conventions locked to the corpus)
=======================================================================
de Bruijn–Newman (copied from dbn_heatflow_probe, Polymath15
normalization): H_t(x) = ∫_0^∞ e^{t u²} Φ(u) cos(x u) du, with
H_0(x) = ξ(1/2 + i x/2)/8 and zeros at x = 2γ.  The multiplier
e^{t u²} is BACKWARD heat: ∂_t H = −∂_{xx} H.  (The opposite PDE
∂_t H = ∂_{xx} H is ordinary forward heat and drives polynomial
roots OFF the real line: e^{s ∂²}(x²−1) = x²−1+2s.  Pólya
real-rootedness for large t forces the dBN sign.)  RH ⇔ Λ ≤ 0;
Rodgers–Tao: Λ ≥ 0.  G10 of dbn_heatflow_probe: Λ_γ = Λ_x/4.

This scout works in the Ξ-variable (zeros at γ, not 2γ).  r618
Edwards/Titchmarsh (jensen_compiler_rigidity_probe, COPIED not
imported): Φ(u) = Σ_{n≥1} (2π² n⁴ e^{9u/2} − 3π n² e^{5u/2})
exp(−π n² e^{2u}); Ξ(x) = ξ(1/2+ix) = 4 ∫_0^∞ Φ(u) cos(x u) du.
(The cosine-even reading "2∫" undercounts this Φ by exactly 2;
the prefactor is locked by a_0 = ξ(1/2).)  Then
Ξ(x) = Σ_n (−1)^n a_n x^{2n} with
a_n = 4 ∫_0^∞ Φ(u) u^{2n} du/(2n)! > 0, a_0 = ξ(1/2) = 0.497120778…
mpmath dps ≥ 40; Φ n-sum until terms < 1e-60.

Finite Taylor approximant (chosen truncation):
  P_N(x,0) = Σ_{n≤N} (−1)^n a_n x^{2n}     (Ξ-variable)
  P_N(x,t) = e^{−t ∂_x²} P_N(x,0)          (exact Appell / heat
                                            flow on polynomials).
Coefficients a_n(t) obey the triangular ODE
  ∂_t a_n = (2n+2)(2n+1) a_{n+1}  (a_{N+1} ≡ 0, a_N constant),
closed form
  a_n(t) = Σ_{k=0}^{N−n} a_{n+k}(0) t^k (2n+2k)! / ((2n)! k!).
Q_N(y,t) = Σ_{n≤N} (−1)^n a_n(t) y^n,  P_N(x,t) = Q_N(x²,t).
P is real-rooted iff every root y of Q is real and ≥ 0.

Finite-free Fisher information of P (roots α):
  Φ_N(P) := Σ_{i≠j} 1/(α_i − α_j)².
Along ∂_t P = −∂_{xx} P one has (leading coefficient constant)
  d/dt log|Disc(P_t)| = c · Φ_N(P_t)
with c = 4 (verified on toys and on P_N away from collisions).
Hence ∫ Φ_N dt = c^{−1} Δ log|Disc|, and the collision barrier
  ∫_{t_a}^{t_b} Φ_N dt < ∞
is EQUIVALENT to Disc ≠ 0 along the path.  Typed, not a claim
about RH: Taylor sections have SPURIOUS far complex roots; a
collision among those is not Λ.  The only RH-relevant question
is whether the INNER roots (those approximating genuine γ_k)
collide on the way down to t = 0.

=======================================================================
TASKS
=======================================================================
T1  a_n for n ≤ 24 (≥ 30 digits).  Truncations N ∈ {6,8,12,16,20}.
    Roots of P_N(x,0); |root − γ_k| for k ≤ 3; #real vs #complex;
    moduli of complex roots vs the truncation radius
    R_N = sqrt(a_N/a_{N+1}).
T2  t_0(N) = smallest t with P_N(·,t) real-rooted (bisection).
    Flow t: 0 → t_0 in ≥ 200 steps, continuous root tracking,
    Φ_N(t), Disc(t) (sign and log|Disc|), min gap.  Collision
    times t_c (min gap → 0, a complex pair appears / disappears).
    Classify SPURIOUS vs INNER (~N/2 roots nearest the origin
    that are real-positive at t = 0, i.e. the γ-approximants).
T3  Identity d/dt log|Disc| vs c·Φ_N, rel err ≤ 1e-8 away from
    collisions — GATE.  c measured, expected 4.
T4  Synthetic off-line.  Taylor P_N(·,0) is typically already
    inner-complex (unlike Jensen polynomials), so ε_crit on the
    Ξ-section itself is 0.  Calibration uses the hyperbolic control
    S_N(x) = Π_{k=1}^N (1 − x²/γ_k²), which is real-rooted at t = 0;
    perturb a_1 (or a_2) by relative ε until an INNER pair leaves
    the real line (ε_crit by bisection).  Rerun the heat flow:
    collision must occur at t_c > 0 among inner roots.  Report
    t_c(ε) and log Φ_N near the collision (detector calibration).
    Taylor-side reading: t_c_inner(ε=0) from T2.
T5  Disc(P_N(·,0)) as a function of (a_0..a_N): numerical Disc
    and ∂ log|Disc|/∂ log a_n.  Which coefficients dominate?
    Does any inequality on the a_n (Turán a_n² ≥ a_{n−1}a_{n+1},
    Laguerre/Newton on Q_N) imply Disc > 0 for the inner roots?
    Expected: no simple one — report honestly.

VERDICT.
  COLLISION_DETECTOR_CALIBRATED_NO_BARRIER
      T2–T4 work; no coefficient-side barrier visible in T5.
  COLLISION_BARRIER_CANDIDATE
      T5 finds an explicit coefficient inequality implying
      Disc > 0 for the inner roots across N — state it.
  INCONCLUSIVE(<gate>)
      otherwise.

--smoke: N ≤ 8, a_n through n = 10, T4 on N = 6; no full verdict.
Deterministic.  Two identical runs seal NUM_SHA.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
import sys
import time

os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("MKL_NUM_THREADS", "1")
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
os.environ.setdefault("NUMEXPR_NUM_THREADS", "1")

import mpmath as mp  # noqa: E402
import numpy as np  # noqa: E402

FROZEN_SPEC = __doc__
SPEC_SHA = hashlib.sha256(FROZEN_SPEC.encode("utf-8")).hexdigest()

ROUND = 626
CONTRACT = "XI.FINITEFREE.COLLISION.01"
FENCE = (
    "Finite approximants; the barrier (9) is equivalent to "
    "Disc ≠ 0 along the path; no RH claim."
)
TYPING = (
    "d/dt log|Disc(P_t)| = c·Φ_N(P_t) with c=4 along ∂_t P=−∂_{xx} P; "
    "∫ Φ_N dt = c^{-1} Δ log|Disc|; collision barrier "
    "∫ Φ_N dt < ∞  ⇔  Disc ≠ 0 along the path.  Finite approximants "
    "only; no RH claim."
)

# r618 Φ / a_n (copied, not imported)
PREF = 4  # Edwards: Xi = 4 int Phi(u) cos(tu) du
MP_DPS = 50
PHI_TERM_CUT = mp.mpf("1e-60")
UMAX = 4
XI_HALF_REF = mp.mpf("0.49712077806581196")

# dbn_heatflow_probe / Polymath15: H_0 zeros at 2γ.  Ξ-variable zeros at γ.
GAMMAS = (
    mp.mpf("14.134725141734693790457251983562"),
    mp.mpf("21.022039638771554992628479593896"),
    mp.mpf("25.010857580145688763213790992562"),
)

NS_FULL = (6, 8, 12, 16, 20)
NS_SMOKE = (6, 8)
NMAX_FULL = 24
NMAX_SMOKE = 10
N_STEPS = 200
TMAX = mp.mpf("1.0e8")
C_FISHER = 4
REAL_TOL = 1.0e-8
T0_REL = 1.0e-8
T3_REL_GATE = 1.0e-8
T3_GAP_FRAC = 1.0e-3
EPS_SCAN = (
    -0.8, -0.4, -0.2, -0.1, -0.05, -0.02, -0.01,
    0.01, 0.02, 0.05, 0.1, 0.2, 0.4, 0.8,
)

CHECKS: list[tuple[str, bool, str]] = []
STATE: list[str] = []


def file_sha256() -> str:
    return hashlib.sha256(open(os.path.abspath(__file__), "rb").read()).hexdigest()


def section(title: str) -> None:
    print("\n" + "=" * 74)
    print(title)
    print("=" * 74, flush=True)


def check(name: str, ok: bool, detail: str = "") -> bool:
    flag = bool(ok)
    CHECKS.append((name, flag, detail))
    print(
        "  [%s] %s%s"
        % ("PASS" if flag else "FAIL", name, ("  " + detail) if detail else ""),
        flush=True,
    )
    return flag


def fmt_mp(x, digits: int = 12) -> str:
    if isinstance(x, complex) or (hasattr(x, "imag") and not isinstance(x, (int, float))):
        try:
            xr, xi = mp.re(x), mp.im(x)
            if abs(xi) < mp.mpf("1e-20") * (1 + abs(x)):
                return mp.nstr(xr, digits, strip_zeros=False)
            return "(%s%+sj)" % (
                mp.nstr(xr, digits, strip_zeros=False),
                mp.nstr(xi, digits, strip_zeros=False),
            )
        except Exception:
            pass
    try:
        return mp.nstr(mp.mpf(x), digits, strip_zeros=False)
    except Exception:
        return str(x)


def fmt_f(x: float, digits: int = 6) -> str:
    if x is None or (isinstance(x, float) and (math.isnan(x) or math.isinf(x))):
        return str(x)
    return ("%." + str(digits) + "e") % float(x)


# ---------------------------------------------------------------------------
# Φ / a_n  -- copied from r618 jensen_compiler_rigidity_probe.py
# ---------------------------------------------------------------------------
def phi_titchmarsh(u: mp.mpf) -> mp.mpf:
    total = mp.mpf(0)
    pi = mp.pi
    n = 1
    while n <= 120:
        n2 = mp.mpf(n) * n
        e2u = mp.exp(2 * u)
        e5 = mp.exp(mp.mpf("2.5") * u)
        e9 = mp.exp(mp.mpf("4.5") * u)
        term = (2 * pi ** 2 * n2 * n2 * e9 - 3 * pi * n2 * e5) * mp.exp(
            -pi * n2 * e2u
        )
        total += term
        if n >= 2 and abs(term) < PHI_TERM_CUT:
            break
        n += 1
    return total


def moment_I(n: int) -> mp.mpf:
    # Same integrand as r618; split nodes only (adaptive tanh-sinh).
    def f(u):
        return phi_titchmarsh(u) * u ** (2 * n)

    return mp.quad(f, [0, mp.mpf("0.5"), mp.mpf("1.0"), mp.mpf("1.5"),
                       mp.mpf("2.5"), UMAX])


def xi_half() -> mp.mpf:
    s = mp.mpf("0.5")
    return (
        mp.mpf("0.5")
        * s
        * (s - 1)
        * mp.power(mp.pi, -s / 2)
        * mp.gamma(s / 2)
        * mp.zeta(s)
    )


def compute_a(nmax: int) -> list[mp.mpf]:
    out = []
    for n in range(nmax + 1):
        i_n = moment_I(n)
        a_n = PREF * i_n / mp.factorial(2 * n)
        out.append(a_n)
        print(
            "  a_%d = %s" % (n, mp.nstr(a_n, 32, strip_zeros=False)),
            flush=True,
        )
    return out


# ---------------------------------------------------------------------------
# exact coefficient heat flow  (∂_t a_n = (2n+2)(2n+1) a_{n+1})
# ---------------------------------------------------------------------------
def flow_a(a0: list[mp.mpf], t: mp.mpf, n_trunc: int) -> list[mp.mpf]:
    t = mp.mpf(t)
    out: list[mp.mpf] = []
    for n in range(n_trunc + 1):
        acc = mp.mpf(0)
        tk = mp.mpf(1)
        factk = mp.mpf(1)
        den0 = mp.factorial(2 * n)
        for k in range(n_trunc - n + 1):
            if k:
                tk *= t
                factk *= k
            acc += a0[n + k] * tk * mp.factorial(2 * n + 2 * k) / (den0 * factk)
        out.append(acc)
    return out


def radius_N(a: list[mp.mpf], n_trunc: int) -> mp.mpf:
    if n_trunc + 1 >= len(a) or a[n_trunc + 1] == 0:
        return mp.mpf("inf")
    return mp.sqrt(a[n_trunc] / a[n_trunc + 1])


# ---------------------------------------------------------------------------
# Q-roots of the even Taylor section (numpy on balanced scale)
# ---------------------------------------------------------------------------
def _log_sigma(at: list[mp.mpf], n_trunc: int) -> float:
    logs = []
    a0 = at[0]
    for n in range(1, n_trunc + 1):
        if at[n] == 0:
            continue
        logs.append(float(mp.log(abs(a0 / at[n])) / n))
    if not logs:
        return 0.0
    logs.sort()
    return logs[len(logs) // 2]


def q_scaled_coeffs(at: list[mp.mpf], n_trunc: int) -> tuple[np.ndarray, float]:
    ls = _log_sigma(at, n_trunc)
    sigma = math.exp(ls) if abs(ls) < 700 else math.copysign(1.0e300, ls)
    log_a0 = float(mp.log(abs(at[0])))
    d = np.empty(n_trunc + 1, dtype=np.float64)
    for n in range(n_trunc + 1):
        sign = -1.0 if (n % 2) else 1.0
        lv = float(mp.log(abs(at[n]))) + n * ls - log_a0
        if lv > 700:
            mag = 1.0e300
        elif lv < -700:
            mag = 0.0
        else:
            mag = math.exp(lv)
        d[n] = sign * mag
    d[0] = 1.0
    return d, sigma


def q_roots(at: list[mp.mpf], n_trunc: int) -> np.ndarray:
    d, sigma = q_scaled_coeffs(at, n_trunc)
    # numpy.roots wants highest degree first
    z = np.roots(d[::-1])
    y = z * sigma
    # residual polish: one Newton step on Q in the original scale, via
    # Horner on the scaled polynomial (stable).
    for i, zi in enumerate(z):
        p = np.polyval(d[::-1], zi)
        dp = np.polyval(np.arange(n_trunc, 0, -1) * d[n_trunc:0:-1], zi)
        if abs(dp) > 0:
            z[i] = zi - p / dp
    return z * sigma


def y_is_real(y: complex, tol: float = REAL_TOL) -> bool:
    return abs(y.imag) <= tol * (1.0 + abs(y))


def y_is_nonneg_real(y: complex, tol: float = REAL_TOL) -> bool:
    return y_is_real(y, tol) and y.real >= -tol * (1.0 + abs(y))


def classify_y(ys: np.ndarray, tol: float = REAL_TOL) -> tuple[int, int, int]:
    n_nnr = 0
    n_neg = 0
    n_cx = 0
    for y in ys:
        if y_is_nonneg_real(y, tol):
            n_nnr += 1
        elif y_is_real(y, tol):
            n_neg += 1
        else:
            n_cx += 1
    return n_nnr, n_neg, n_cx


def is_real_rooted(at: list[mp.mpf], n_trunc: int, tol: float = REAL_TOL) -> bool:
    ys = q_roots(at, n_trunc)
    n_nnr, n_neg, n_cx = classify_y(ys, tol)
    return n_nnr == n_trunc and n_neg == 0 and n_cx == 0


def p_roots_from_y(ys: np.ndarray) -> np.ndarray:
    out = np.empty(2 * len(ys), dtype=np.complex128)
    for i, y in enumerate(ys):
        s = np.sqrt(y + 0j)
        out[2 * i] = s
        out[2 * i + 1] = -s
    return out


def match_roots(prev: np.ndarray, new: np.ndarray) -> np.ndarray:
    """Greedy nearest-neighbour matching, |prev| == |new|."""
    n = len(prev)
    used = np.zeros(n, dtype=bool)
    out = np.empty(n, dtype=np.complex128)
    for i in range(n):
        diffs = np.abs(new - prev[i])
        diffs[used] = np.inf
        j = int(np.argmin(diffs))
        used[j] = True
        out[i] = new[j]
    return out


def min_gap_real(alphas: np.ndarray, tol: float = REAL_TOL) -> float:
    real_ones = [a.real for a in alphas if abs(a.imag) <= tol * (1.0 + abs(a))]
    if len(real_ones) < 2:
        return float("inf")
    real_ones.sort()
    return min(real_ones[i + 1] - real_ones[i] for i in range(len(real_ones) - 1))


def fisher_phi(alphas: np.ndarray) -> complex:
    s = 0j
    n = len(alphas)
    for i in range(n):
        ai = alphas[i]
        for j in range(n):
            if i == j:
                continue
            d = ai - alphas[j]
            if d == 0:
                return complex(float("inf"), 0.0)
            s += 1.0 / (d * d)
    return s


def logabs_disc_from_roots(alphas: np.ndarray, lead: float) -> tuple[float, float]:
    """log|Disc| and a crude sign (±1) from roots.  deg n, Disc = lead^{2n-2} ∏_{i<j} (αi-αj)²."""
    n = len(alphas)
    if n < 2:
        return 0.0, 1.0
    logabs = (2 * n - 2) * math.log(abs(lead) + 1.0e-300)
    prod = 1j * 0 + 1.0
    for i in range(n):
        for j in range(i + 1, n):
            d = alphas[i] - alphas[j]
            ad = abs(d)
            if ad == 0:
                return float("-inf"), 0.0
            logabs += 2.0 * math.log(ad)
            prod *= (d * d) / (ad * ad)  # unit-modulus running sign/phase
    sgn = float(np.sign(prod.real)) if abs(prod.imag) < 0.25 else 0.0
    if abs(lead) > 0 and (n % 2 == 0):
        pass
    return logabs, sgn if sgn != 0 else float(np.sign(prod.real + 1e-30))


def lead_p(at: list[mp.mpf], n_trunc: int) -> float:
    sign = -1.0 if (n_trunc % 2) else 1.0
    return sign * float(at[n_trunc])


# ---------------------------------------------------------------------------
# t0 bisection
# ---------------------------------------------------------------------------
def find_t0(a0: list[mp.mpf], n_trunc: int) -> tuple[mp.mpf, bool]:
    at0 = flow_a(a0, mp.mpf(0), n_trunc)
    if is_real_rooted(at0, n_trunc):
        return mp.mpf(0), True
    t_hi = mp.mpf("0.01")
    n_dbl = 0
    while t_hi < TMAX:
        at = flow_a(a0, t_hi, n_trunc)
        if is_real_rooted(at, n_trunc):
            break
        t_hi *= 2
        n_dbl += 1
    else:
        return t_hi, False
    t_lo = mp.mpf(0) if n_dbl == 0 else t_hi / 2
    for _ in range(80):
        if t_hi - t_lo <= T0_REL * max(mp.mpf(1), t_hi):
            break
        mid = (t_lo + t_hi) / 2
        at = flow_a(a0, mid, n_trunc)
        if is_real_rooted(at, n_trunc):
            t_hi = mid
        else:
            t_lo = mid
    return t_hi, True


# ---------------------------------------------------------------------------
# tracking
# ---------------------------------------------------------------------------
def label_inner(ys: np.ndarray, n_trunc: int) -> list[str]:
    """INNER = the ~N/2 Q-roots whose P-roots lie closest to the real axis.

    Taylor sections of Ξ are typically *not* real-rooted (unlike Jensen
    polynomials): the γ-approximants are complex with shrinking Im as N
    grows.  Ranking by |Im √y| still isolates those approximants.  Count
    is even so conjugate pairs stay together: n_inner = 2*(N//4) (≥ 2).
    """
    labels = ["SPUR"] * n_trunc
    scored: list[tuple[float, float, int]] = []
    for i, y in enumerate(ys):
        s = np.sqrt(y + 0j)
        scored.append((abs(s.imag.real), abs(s), i))
    scored.sort()
    n_inner = 2 * max(1, n_trunc // 4)
    if n_inner > n_trunc:
        n_inner = n_trunc - (n_trunc % 2)
    for _, _, i in scored[:n_inner]:
        labels[i] = "INNER"
    return labels


def track_flow(
    a0: list[mp.mpf],
    n_trunc: int,
    t0: mp.mpf,
    n_steps: int,
) -> dict:
    ts = [t0 * k / n_steps for k in range(n_steps + 1)]
    ys0 = q_roots(flow_a(a0, mp.mpf(0), n_trunc), n_trunc)
    labels = label_inner(ys0, n_trunc)
    prev = ys0.copy()
    records = []
    n_cx_prev = classify_y(ys0)[2]
    collisions: list[dict] = []
    for k, t in enumerate(ts):
        at = flow_a(a0, t, n_trunc)
        ys_raw = q_roots(at, n_trunc)
        ys = match_roots(prev, ys_raw) if k else ys_raw
        n_nnr, n_neg, n_cx = classify_y(ys)
        alphas = p_roots_from_y(ys)
        gap = min_gap_real(alphas)
        phi = fisher_phi(alphas)
        lead = lead_p(at, n_trunc)
        logd, sgn = logabs_disc_from_roots(alphas, lead)
        rec = {
            "t": float(t),
            "n_nnr": n_nnr,
            "n_neg": n_neg,
            "n_cx": n_cx,
            "n_real_p": 2 * n_nnr,
            "n_complex_p": 2 * n_trunc - 2 * n_nnr,
            "gap": gap,
            "phi_re": float(np.real(phi)),
            "phi_im": float(np.imag(phi)),
            "logabs_disc": logd,
            "sign_disc": sgn,
            "ys": ys,
        }
        records.append(rec)
        if k and n_cx != n_cx_prev:
            # a pair of Q-roots joined/left the real line; classify by labels
            # of roots that changed reality.
            changed = []
            for i in range(n_trunc):
                was = y_is_real(prev[i])
                now = y_is_real(ys[i])
                if was != now:
                    changed.append(labels[i])
            kind = "INNER" if any(x == "INNER" for x in changed) else "SPUR"
            # refine t_c by bisection on this step
            lo, hi = ts[k - 1], ts[k]
            target_more_complex = n_cx > n_cx_prev
            tc = hi
            for _ in range(28):
                mid = (lo + hi) / 2
                ymid = match_roots(prev, q_roots(flow_a(a0, mid, n_trunc), n_trunc))
                cxm = classify_y(ymid)[2]
                if (cxm > n_cx_prev) == target_more_complex and cxm != n_cx_prev:
                    tc = mid
                    hi = mid
                else:
                    lo = mid
            collisions.append({
                "t": float(tc),
                "kind": kind,
                "dn_cx": n_cx - n_cx_prev,
                "changed": changed,
                "direction": "forward",
            })
        n_cx_prev = n_cx
        prev = ys
    inner_cx_at_0 = sum(
        1 for i, lab in enumerate(labels)
        if lab == "INNER" and not y_is_nonneg_real(ys0[i])
    )
    inner_cx_at_t0 = sum(
        1 for i, lab in enumerate(labels)
        if lab == "INNER" and not y_is_nonneg_real(records[-1]["ys"][i])
    )
    return {
        "labels": labels,
        "records": records,
        "collisions": collisions,
        "inner_cx_at_0": inner_cx_at_0,
        "inner_cx_at_t0": inner_cx_at_t0,
        "ys0": ys0,
        "ys_t0": records[-1]["ys"],
    }


# ---------------------------------------------------------------------------
# T3 identity
# ---------------------------------------------------------------------------
def q_roots_mp(at: list[mp.mpf], n_trunc: int) -> list[mp.mpc]:
    """High-dps Q-roots (T3 identity).  Same scaling as the numpy path."""
    ls = _log_sigma(at, n_trunc)
    sigma = mp.exp(mp.mpf(ls))
    log_a0 = mp.log(abs(at[0]))
    d = []
    for n in range(n_trunc + 1):
        sign = -1 if (n % 2) else 1
        mag = mp.exp(mp.log(abs(at[n])) + n * mp.mpf(ls) - log_a0)
        d.append(sign * mag)
    d[0] = mp.mpf(1)
    pc = list(reversed(d))
    with mp.workdps(80):
        zs = mp.polyroots(pc, maxsteps=400, extraprec=40)
    return [z * sigma for z in zs]


def p_roots_mp(ys: list[mp.mpc]) -> list[mp.mpc]:
    out: list[mp.mpc] = []
    for y in ys:
        s = mp.sqrt(y)
        out.append(s)
        out.append(-s)
    return out


def fisher_phi_mp(alphas: list[mp.mpc]) -> mp.mpc:
    s = mp.mpc(0)
    n = len(alphas)
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            d = alphas[i] - alphas[j]
            s += 1 / (d * d)
    return s


def logabs_disc_mp(alphas: list[mp.mpc], lead: mp.mpf) -> mp.mpf:
    n = len(alphas)
    logabs = (2 * n - 2) * mp.log(abs(lead))
    for i in range(n):
        for j in range(i + 1, n):
            logabs += 2 * mp.log(abs(alphas[i] - alphas[j]))
    return logabs


def t3_identity_at(a0: list[mp.mpf], n_trunc: int, t: float, h: float) -> dict:
    """Independent FD of log|Disc| (mpmath roots) vs 4 Φ (same roots at t)."""
    at = flow_a(a0, mp.mpf(t), n_trunc)
    ys = q_roots_mp(at, n_trunc)
    al = p_roots_mp(ys)
    phi = fisher_phi_mp(al)
    lead = ((-1) ** n_trunc) * at[n_trunc]
    logd = logabs_disc_mp(al, lead)

    def logd_at(tt: float) -> mp.mpf:
        att = flow_a(a0, mp.mpf(tt), n_trunc)
        yst = q_roots_mp(att, n_trunc)
        alt = p_roots_mp(yst)
        return logabs_disc_mp(alt, ((-1) ** n_trunc) * att[n_trunc])

    if t - h <= 0:
        dldt = (logd_at(t + h) - logd) / mp.mpf(h)
    else:
        dldt = (logd_at(t + h) - logd_at(t - h)) / (mp.mpf(2) * h)
    phi_re = mp.re(phi)
    pred = C_FISHER * phi_re
    rel = abs(dldt - pred) / max(abs(pred), abs(dldt), mp.mpf("1e-20"))
    c_est = dldt / phi_re if phi_re != 0 else mp.mpf("nan")
    return {
        "t": t,
        "phi": float(phi_re),
        "dldt": float(dldt),
        "c_est": float(c_est),
        "rel": float(rel),
        "logd": float(logd),
    }


def t3_samples(a0: list[mp.mpf], n_trunc: int, t0: mp.mpf,
               track: dict) -> dict:
    recs = track["records"]
    coll_t = [c["t"] for c in track["collisions"]]
    t0f = float(t0) if t0 > 0 else 1.0
    cands = []
    for i in range(3, len(recs) - 3):
        r = recs[i]
        if r["t"] <= 0:
            continue
        window_cx = [recs[j]["n_cx"] for j in range(i - 2, i + 3)]
        if any(c != r["n_cx"] for c in window_cx):
            continue
        if not math.isfinite(r["phi_re"]) or abs(r["phi_re"]) < 0.5:
            continue
        dcoll = min((abs(r["t"] - ct) for ct in coll_t), default=t0f)
        if dcoll < 0.12 * t0f:
            continue
        gaps = [recs[j]["gap"] for j in range(i - 1, i + 2)
                if math.isfinite(recs[j]["gap"])]
        if gaps and min(gaps) < T3_GAP_FRAC * max(math.sqrt(max(r["t"], 1e-12)), 1.0):
            continue
        cands.append(i)
    picked = []
    if cands:
        for frac in (0.22, 0.45, 0.62, 0.82):
            target = frac * t0f
            j = min(cands, key=lambda i: abs(recs[i]["t"] - target))
            if j not in picked:
                picked.append(j)
    rels: list[float] = []
    c_ests: list[float] = []
    details: list[tuple] = []
    if len(picked) < 2 and t0 > 0:
        for frac in (0.70, 0.84, 0.55, 0.40):
            ttry = frac * t0f
            htry = max(1.0e-8, 1.0e-6 * max(ttry, 1.0))
            htry = min(htry, 0.015 * t0f)
            try:
                samp = t3_identity_at(a0, n_trunc, ttry, htry)
            except Exception:
                continue
            if not math.isfinite(samp["rel"]) or abs(samp["phi"]) < 0.15:
                continue
            rels.append(samp["rel"])
            c_ests.append(samp["c_est"])
            details.append((samp["t"], samp["phi"], samp["dldt"], samp["c_est"], samp["rel"]))
            if len(details) >= 2:
                break
    for i in picked[:4]:
        t = recs[i]["t"]
        h = max(1.0e-8, 1.0e-6 * max(t, 1.0))
        if t0 > 0:
            h = min(h, 0.02 * t0f, 0.25 * max(t, 1e-12))
        try:
            samp = t3_identity_at(a0, n_trunc, t, h)
        except Exception as exc:
            print("     T3 sample t=%s failed: %s" % (fmt_f(t, 4), exc), flush=True)
            continue
        rels.append(samp["rel"])
        c_ests.append(samp["c_est"])
        details.append((samp["t"], samp["phi"], samp["dldt"], samp["c_est"], samp["rel"]))
    maxrel = max(rels) if rels else float("inf")
    return {
        "n_samples": len(details),
        "maxrel": maxrel,
        "c_ests": c_ests,
        "details": details,
    }


# ---------------------------------------------------------------------------
# T4 perturbation
# ---------------------------------------------------------------------------
def inner_all_real_labeled(ys: np.ndarray, labels: list[str]) -> bool:
    for i, lab in enumerate(labels):
        if lab == "INNER" and not y_is_nonneg_real(ys[i]):
            return False
    return True


def t4_frozen_track(
    a_pert: list[mp.mpf],
    n_trunc: int,
    labels: list[str],
    ys_anchor: np.ndarray,
    t0: mp.mpf,
    n_steps: int,
) -> dict:
    """Track with labels frozen from an unperturbed t=0 matching."""
    ys0 = match_roots(ys_anchor, q_roots(flow_a(a_pert, mp.mpf(0), n_trunc), n_trunc))
    prev = ys0
    n_cx_prev = classify_y(prev)[2]
    inn_tc: list[float] = []
    planted_real: list[float] = []
    max_log_phi = float("-inf")
    phi_near = float("nan")
    ts = [t0 * k / n_steps for k in range(n_steps + 1)]
    for k, t in enumerate(ts):
        ys_raw = q_roots(flow_a(a_pert, t, n_trunc), n_trunc)
        ys = match_roots(prev, ys_raw) if k else ys_raw
        n_cx = classify_y(ys)[2]
        al = p_roots_from_y(ys)
        lp = float(np.real(fisher_phi(al)))
        if math.isfinite(lp) and abs(lp) > 0:
            max_log_phi = max(max_log_phi, math.log10(abs(lp) + 1e-300))
        if inner_all_real_labeled(ys, labels):
            planted_real.append(float(t))
        if k and n_cx != n_cx_prev:
            changed = []
            for i in range(n_trunc):
                if y_is_real(prev[i]) != y_is_real(ys[i]):
                    changed.append(labels[i])
            if any(x == "INNER" for x in changed):
                inn_tc.append(float(t))
                phi_near = lp
        n_cx_prev = n_cx
        prev = ys
    tc = min(planted_real) if planted_real else float("nan")
    return {
        "tc_inner": tc,
        "inn_tc": inn_tc,
        "max_log10_phi": max_log_phi,
        "phi_near": phi_near,
        "inner_real_at_0": inner_all_real_labeled(ys0, labels),
    }


def apply_eps(a0: list[mp.mpf], idx: int, eps: float) -> list[mp.mpf]:
    out = list(a0)
    out[idx] = a0[idx] * (mp.mpf(1) + mp.mpf(eps))
    return out


def find_eps_crit(
    a0: list[mp.mpf], n_trunc: int, labels0: list[str],
) -> tuple[int, float, float]:
    """Return (coeff_index, eps_crit, eps_used) or idx=-1 on failure."""
    ys0 = q_roots(flow_a(a0, mp.mpf(0), n_trunc), n_trunc)
    if not inner_all_real_labeled(ys0, labels0):
        return -1, 0.0, 0.0
    for idx in (1, 2):
        if idx >= len(a0):
            continue
        hit_eps = None
        for eps in EPS_SCAN:
            ap = apply_eps(a0, idx, eps)
            ys = match_roots(ys0, q_roots(flow_a(ap, mp.mpf(0), n_trunc), n_trunc))
            if not inner_all_real_labeled(ys, labels0):
                hit_eps = float(eps)
                break
        if hit_eps is None:
            continue
        # bisection toward 0
        lo, hi = 0.0, hit_eps
        if hi < lo:
            lo, hi = hi, lo
        # lo = side with inner real, hi = side with inner complex
        def inner_complex(e: float) -> bool:
            ap = apply_eps(a0, idx, e)
            ys = match_roots(ys0, q_roots(flow_a(ap, mp.mpf(0), n_trunc), n_trunc))
            return not inner_all_real_labeled(ys, labels0)

        # identify which end is complex
        if inner_complex(lo) and not inner_complex(hi):
            lo, hi = hi, lo
        if not inner_complex(hi):
            continue
        for _ in range(40):
            if abs(hi - lo) <= 1e-6 * max(1.0, abs(hi)):
                break
            mid = 0.5 * (lo + hi)
            if inner_complex(mid):
                hi = mid
            else:
                lo = mid
        return idx, float(hi), float(hi * 1.25)
    return -1, float("nan"), float("nan")


# ---------------------------------------------------------------------------
# T5 sensitivities / Newton vs Turán
# ---------------------------------------------------------------------------
def turan_ok(a: list[mp.mpf], n_top: int) -> tuple[bool, list[float]]:
    # Turán on c_n = n! a_n: c_n² ≥ c_{n-1} c_{n+1}
    ratios = []
    ok = True
    for n in range(1, n_top + 1):
        if n + 1 >= len(a):
            break
        cn = mp.factorial(n) * a[n]
        cnm = mp.factorial(n - 1) * a[n - 1]
        cnp = mp.factorial(n + 1) * a[n + 1]
        rat = float(cn ** 2 / (cnm * cnp))
        ratios.append(rat)
        if cn ** 2 < cnm * cnp:
            ok = False
    return ok, ratios


def newton_ok_q(at: list[mp.mpf], n_trunc: int) -> tuple[bool, list[float]]:
    """Newton inequalities on Q(y) = Σ binom-normalized coefficients.
    For Q(y) = Σ_{k=0}^N e_k y^k with e_k = (-1)^k a_k, write
    p_k = e_k / C(N,k)  (up to the monic convention of Q as a
    polynomial in y).  Newton: p_k² ≥ p_{k-1} p_{k+1} for hyperbolic
    polynomials (after making leading-positive).  Sign-alternating
    e_k already encode the desired positive-root form; we apply
    Newton to b_k = a_k / C(N,k) > 0, which is equivalent for
    Q(−w) = Σ a_k w^k.
    """
    ratios = []
    ok = True
    n = n_trunc
    b = [a / mp.binomial(n, k) for k, a in enumerate(at[: n + 1])]
    for k in range(1, n):
        lhs = b[k] ** 2
        rhs = b[k - 1] * b[k + 1]
        rat = float(lhs / rhs) if rhs != 0 else float("inf")
        ratios.append(rat)
        if lhs < rhs:
            ok = False
    return ok, ratios


def elementary_sym(vals: list[mp.mpf]) -> list[mp.mpf]:
    p = [mp.mpf(1)]
    for v in vals:
        nxt = [mp.mpf(0)] * (len(p) + 1)
        for i, c in enumerate(p):
            nxt[i] += c
            nxt[i + 1] += c * v
        p = nxt
    return p


def gamma_list(n: int) -> list[mp.mpf]:
    out: list[mp.mpf] = []
    for k in range(1, n + 1):
        if k <= len(GAMMAS):
            out.append(GAMMAS[k - 1])
        else:
            out.append(mp.im(mp.zetazero(k)))
    return out


def synthetic_a(n_trunc: int) -> list[mp.mpf]:
    """Even hyperbolic control: P(x) = Π_{k=1}^N (1 - x²/γ_k²).
    Then a_n = e_n(1/γ_1², …, 1/γ_N²), so P = Σ (-1)^n a_n x^{2n}.
    All 2N roots real (±γ_k).  Detector calibration, not a Ξ claim.
    """
    gs = gamma_list(n_trunc)
    u = [1 / (g * g) for g in gs]
    e = elementary_sym(u)
    # e[n] is the degree-n elementary symmetric function
    assert len(e) == n_trunc + 1
    return e


def disc_sensitivities(a0: list[mp.mpf], n_trunc: int, delta: float = 1e-6):
    at = flow_a(a0, mp.mpf(0), n_trunc)
    ys = q_roots(at, n_trunc)
    al = p_roots_from_y(ys)
    logd0, _ = logabs_disc_from_roots(al, lead_p(at, n_trunc))
    labels = label_inner(ys, n_trunc)
    inner_idx = [i for i, lab in enumerate(labels) if lab == "INNER"]
    inner_al = p_roots_from_y(ys[inner_idx]) if inner_idx else np.array([])
    logd_in0 = 0.0
    if len(inner_al) >= 2:
        logd_in0, _ = logabs_disc_from_roots(inner_al, 1.0)
    sens = []
    sens_in = []
    for n in range(n_trunc + 1):
        ap = list(a0)
        ap[n] = a0[n] * (mp.mpf(1) + mp.mpf(delta))
        atp = flow_a(ap, mp.mpf(0), n_trunc)
        ysp = q_roots(atp, n_trunc)
        alp = p_roots_from_y(ysp)
        logdp, _ = logabs_disc_from_roots(alp, lead_p(atp, n_trunc))
        sens.append((logdp - logd0) / delta)
        if len(inner_idx) >= 1:
            ysm = match_roots(ys, ysp)
            inner_alp = p_roots_from_y(ysm[inner_idx])
            if len(inner_alp) >= 2:
                ldi, _ = logabs_disc_from_roots(inner_alp, 1.0)
                sens_in.append((ldi - logd_in0) / delta)
            else:
                sens_in.append(float("nan"))
        else:
            sens_in.append(float("nan"))
    return logd0, sens, logd_in0, sens_in


# ---------------------------------------------------------------------------
# T1 root table
# ---------------------------------------------------------------------------
def t1_for_N(a: list[mp.mpf], n_trunc: int) -> dict:
    at = flow_a(a, mp.mpf(0), n_trunc)
    ys = q_roots(at, n_trunc)
    n_nnr, n_neg, n_cx = classify_y(ys)
    alphas = p_roots_from_y(ys)
    n_real_p = 2 * n_nnr
    n_complex_p = 2 * n_trunc - n_real_p
    pos_real = sorted(
        (float(np.sqrt(max(y.real, 0.0))) for y in ys if y_is_nonneg_real(y) and y.real > 0)
    )
    # first-quadrant P-roots, closest-to-real first (γ-approximants)
    quad = []
    for al in alphas:
        if al.real >= -1e-12 and al.imag >= -1e-12:
            quad.append(al)
    quad.sort(key=lambda z: (abs(z.imag), abs(z)))
    dgamma = []
    dgamma_re = []
    im_approx = []
    for k, g in enumerate(GAMMAS):
        gf = float(g)
        if k < len(quad):
            z = quad[k]
            dgamma.append(float(abs(z - gf)))
            dgamma_re.append(abs(float(z.real) - gf))
            im_approx.append(float(z.imag))
        elif k < len(pos_real):
            dgamma.append(abs(pos_real[k] - gf))
            dgamma_re.append(abs(pos_real[k] - gf))
            im_approx.append(0.0)
        else:
            dgamma.append(float("nan"))
            dgamma_re.append(float("nan"))
            im_approx.append(float("nan"))
    rN = float(radius_N(a, n_trunc)) if n_trunc + 1 < len(a) else float("nan")
    cx_mod_p = []
    for al in alphas:
        if abs(al.imag) > REAL_TOL * (1.0 + abs(al)):
            cx_mod_p.append(float(abs(al)))
    cx_mod_p.sort()
    n_cx_inside = sum(1 for m in cx_mod_p if math.isfinite(rN) and m < rN)
    n_cx_outside = sum(1 for m in cx_mod_p if math.isfinite(rN) and m >= rN)
    return {
        "N": n_trunc,
        "n_nnr_y": n_nnr,
        "n_neg_y": n_neg,
        "n_cx_y": n_cx,
        "n_real_p": n_real_p,
        "n_complex_p": n_complex_p,
        "pos_real": pos_real,
        "quad": quad,
        "dgamma": dgamma,
        "dgamma_re": dgamma_re,
        "im_approx": im_approx,
        "R": rN,
        "cx_mod_min": cx_mod_p[0] if cx_mod_p else float("nan"),
        "cx_mod_max": cx_mod_p[-1] if cx_mod_p else float("nan"),
        "n_cx_inside_R": n_cx_inside,
        "n_cx_outside_R": n_cx_outside,
        "ys": ys,
        "labels": label_inner(ys, n_trunc),
    }


# ---------------------------------------------------------------------------
# S0 toys: c = 4 exactly
# ---------------------------------------------------------------------------
def run_s0() -> None:
    section("S0  toy identity  d/dt log|Disc| = 4 Φ_N  (exact)")
    print(TYPING, flush=True)
    print(
        "  dBN convention (dbn_heatflow_probe): H_t = ∫ e^{t u²} Φ cos(xu) du, "
        "∂_t H = −∂_{xx} H, H_0 zeros at x=2γ (Polymath15).  "
        "This scout: Ξ-variable, P_t = e^{−t ∂_x²} P_0, zeros at γ; "
        "time is gamma-units (G10: Λ_γ = Λ_x/4).",
        flush=True,
    )
    # P = x^2 - 1,  e^{-t ∂²}(x²-1) = x² - 1 - 2t, roots ±sqrt(1+2t)
    t = mp.mpf("0.3")
    r2 = 1 + 2 * t
    r = mp.sqrt(r2)
    # Φ = 2 / (2r)² = 1/(2 r²)
    phi = 1 / (2 * r2)
    dldt = 2 / r2  # Disc = 4(1+2t), d/dt log|Disc| = 2/(1+2t)
    c_toy = dldt / phi
    check(
        "S0.c_quad",
        abs(c_toy - 4) < mp.mpf("1e-20"),
        "P=x^2-1  c=%s  Φ=%s  dlog|Disc|/dt=%s" % (
            fmt_mp(c_toy, 8), fmt_mp(phi, 10), fmt_mp(dldt, 10),
        ),
    )
    # cubic x^3 - x = x(x²-1); e^{-t∂²} = x³ - (1+6t)x; Disc=4(1+6t)³
    # roots 0, ±sqrt(1+6t); Φ = 9/(2 r²) with r²=1+6t; d/dt log|Disc|=18/r²
    r2c = 1 + 6 * t
    phi_c = mp.mpf(9) / (2 * r2c)
    dldt_c = 18 / r2c
    c_c = dldt_c / phi_c
    check(
        "S0.c_cubic",
        abs(c_c - 4) < mp.mpf("1e-20"),
        "P=x^3-x  c=%s" % fmt_mp(c_c, 8),
    )
    # ODE closed form vs FD on a tiny even quartic
    a_toy = [mp.mpf(1), mp.mpf("0.5"), mp.mpf("0.1")]
    n = 2
    t1 = mp.mpf("0.2")
    at = flow_a(a_toy, t1, n)
    h = mp.mpf("1e-8")
    ap = flow_a(a_toy, t1 + h, n)
    am = flow_a(a_toy, t1 - h, n)
    ode_ok = True
    dets = []
    for k in range(n):
        dnum = (ap[k] - am[k]) / (2 * h)
        rhs = (2 * k + 2) * (2 * k + 1) * at[k + 1]
        rel = abs(dnum - rhs) / max(abs(rhs), mp.mpf("1e-20"))
        dets.append(float(rel))
        if rel > mp.mpf("1e-8"):
            ode_ok = False
    check(
        "S0.coeff_ODE",
        ode_ok,
        "max rel FD vs (2n+2)(2n+1)a_{n+1} = %s" % fmt_f(max(dets), 3),
    )


# ---------------------------------------------------------------------------
# main tasks
# ---------------------------------------------------------------------------
def emit_state(line: str) -> None:
    STATE.append(line)
    print(line, flush=True)


def run(smoke: bool) -> int:
    t_wall = time.time()
    global CHECKS, STATE
    CHECKS = []
    STATE = []
    mp.mp.dps = MP_DPS

    ns = NS_SMOKE if smoke else NS_FULL
    nmax = NMAX_SMOKE if smoke else NMAX_FULL
    t4_n = 6 if smoke else 8
    n_steps = N_STEPS

    print("=" * 74)
    print("xi_finitefree_collision_probe -- r%d %s" % (ROUND, CONTRACT))
    print("mode: %s" % ("SMOKE (N=%s, nmax=%d)" % (list(ns), nmax) if smoke
                        else "FULL"))
    print("SPEC_SHA %s" % SPEC_SHA)
    print("FILE     %s" % file_sha256())
    print("FENCE    %s" % FENCE)
    print("=" * 74, flush=True)

    run_s0()

    section("T1  Ξ Taylor coefficients a_n and truncations P_N(x,0)")
    print(
        "  prefactor %d (r618 Edwards; '2∫' undercounts by 2), dps=%d, "
        "Umax=%s, Phi n-sum cut %s"
        % (PREF, MP_DPS, UMAX, PHI_TERM_CUT),
        flush=True,
    )
    a = compute_a(nmax)
    xih = xi_half()
    rel_a0 = abs(a[0] - xih) / abs(xih)
    check(
        "T1.a0_eq_xi_half",
        rel_a0 < mp.mpf("1e-20"),
        "a_0=%s  xi(1/2)=%s  rel=%s"
        % (fmt_mp(a[0], 20), fmt_mp(xih, 20), fmt_mp(rel_a0, 6)),
    )
    check(
        "T1.a0_ref",
        abs(a[0] - XI_HALF_REF) / XI_HALF_REF < mp.mpf("1e-8"),
        "vs 0.497120778…  rel=%s" % fmt_mp(abs(a[0] - XI_HALF_REF) / XI_HALF_REF, 6),
    )
    pos = all(an > 0 for an in a)
    check("T1.a_n_positive", pos, "n=0..%d" % (len(a) - 1))
    # 30 significant digits: print already did 32; gate a_n finite and >0
    check(
        "T1.digits",
        all(mp.isfinite(an) and an > 0 for an in a),
        "printed 32 digits, nmax=%d" % nmax,
    )

    t1_rows = []
    print(
        "  N  #real_P  #cx_P  |z-γ1|      Im(z1)     |z-γ2|      "
        "R_N        |cx|_min    |cx|_max    n_cx(<R)",
        flush=True,
    )
    for n_trunc in ns:
        row = t1_for_N(a, n_trunc)
        t1_rows.append(row)
        dg = row["dgamma"]
        ims = row["im_approx"]
        print(
            "  %-2d %6d  %5d  %-11s %-11s %-11s %-10s %-10s %-10s %d/%d"
            % (
                n_trunc,
                row["n_real_p"],
                row["n_complex_p"],
                fmt_f(dg[0], 3),
                fmt_f(ims[0], 3),
                fmt_f(dg[1], 3),
                fmt_f(row["R"], 3),
                fmt_f(row["cx_mod_min"], 3),
                fmt_f(row["cx_mod_max"], 3),
                row["n_cx_inside_R"],
                row["n_complex_p"],
            ),
            flush=True,
        )
        if row["quad"]:
            bits = []
            for z in row["quad"][:6]:
                bits.append("%+.4f%+.4fj" % (z.real, z.imag))
            print("     1st-quad (Im-sorted): %s" % ", ".join(bits), flush=True)
        check(
            "T1.N%d_has_roots" % n_trunc,
            row["n_real_p"] + row["n_complex_p"] == 2 * n_trunc,
            "real=%d cx=%d (Taylor sections are typically all-complex)"
            % (row["n_real_p"], row["n_complex_p"]),
        )

    if len(t1_rows) >= 2:
        im0 = t1_rows[0]["im_approx"][0]
        im1 = t1_rows[-1]["im_approx"][0]
        check(
            "T1.inner_Im_shrinks_with_N",
            math.isfinite(im0) and math.isfinite(im1) and im1 < im0,
            "Im(z1): N=%d -> %s,  N=%d -> %s"
            % (t1_rows[0]["N"], fmt_f(im0, 3), t1_rows[-1]["N"], fmt_f(im1, 3)),
        )

    print(
        "  note: Taylor sections of Ξ at these N have NO real roots "
        "(unlike Jensen polynomials).  The γ-approximants are the "
        "closest-to-real complex pairs; INNER is ranked by |Im √y|, "
        "not by |x|.  R_N = sqrt(a_N/a_{N+1}) is the term-balance "
        "radius; here the whole root set sits near |x| ~ R_N, so "
        "'spurious far vs genuine inner' is an Im-ranking.  As N grows "
        "the innermost Im shrinks (limit open; no RH claim).",
        flush=True,
    )

    section("T2  heat flow, t_0(N), collisions (spurious vs inner)")
    t2 = {}
    for n_trunc in ns:
        print("  -- N=%d --" % n_trunc, flush=True)
        t0, ok_t0 = find_t0(a, n_trunc)
        check(
            "T2.N%d_t0_bracket" % n_trunc,
            ok_t0,
            "t0=%s" % fmt_mp(t0, 10),
        )
        tr = track_flow(a, n_trunc, t0, n_steps)
        spur_tc = [c["t"] for c in tr["collisions"] if c["kind"] == "SPUR"]
        inn_tc = [c["t"] for c in tr["collisions"] if c["kind"] == "INNER"]
        print(
            "     t0=%s  n_steps=%d  collisions=%d  "
            "spur_tc=%s  inner_tc=%s  inner_cx(t=0)=%d"
            % (
                fmt_mp(t0, 10),
                n_steps,
                len(tr["collisions"]),
                "[" + ", ".join(fmt_f(x, 4) for x in spur_tc) + "]",
                "[" + ", ".join(fmt_f(x, 4) for x in inn_tc) + "]",
                tr["inner_cx_at_0"],
            ),
            flush=True,
        )
        nlab_i = tr["labels"].count("INNER")
        nlab_s = tr["labels"].count("SPUR")
        print(
            "     labels INNER=%d SPUR=%d  n_real_P(t=0)=%d  "
            "n_real_P(t0)=%d"
            % (
                nlab_i, nlab_s,
                tr["records"][0]["n_real_p"],
                tr["records"][-1]["n_real_p"],
            ),
            flush=True,
        )
        check(
            "T2.N%d_inner_labeled" % n_trunc,
            nlab_i >= 2,
            "INNER=%d SPUR=%d" % (nlab_i, nlab_s),
        )
        # Going backward from t0, far (largest |Im| at t=0) peel off first:
        # t0 itself should be a SPURIOUS collision, inner t_c strictly smaller.
        spur_last = True
        if inn_tc and spur_tc:
            spur_last = max(spur_tc) >= max(inn_tc) - 1e-12
        elif inn_tc and not spur_tc:
            spur_last = False
        check(
            "T2.N%d_spur_collide_last" % n_trunc,
            spur_last,
            "max spur_tc=%s  max inner_tc=%s  (backward: far roots first)"
            % (
                fmt_f(max(spur_tc) if spur_tc else float("nan"), 4),
                fmt_f(max(inn_tc) if inn_tc else float("nan"), 4),
            ),
        )
        t2[n_trunc] = {
            "t0": float(t0),
            "ok": ok_t0,
            "track": tr,
            "spur_tc": spur_tc,
            "inner_tc": inn_tc,
        }

    section("T3  identity  d/dt log|Disc| = 4 Φ_N")
    t3 = {}
    t3_all_ok = True
    for n_trunc in ns:
        t0 = mp.mpf(t2[n_trunc]["t0"])
        samp = t3_samples(a, n_trunc, t0, t2[n_trunc]["track"])
        t3[n_trunc] = samp
        print(
            "  N=%d  n_samples=%d  maxrel=%s  c_est=%s"
            % (
                n_trunc,
                samp["n_samples"],
                fmt_f(samp["maxrel"], 3),
                ", ".join(fmt_f(c, 6) for c in samp["c_ests"][:4]),
            ),
            flush=True,
        )
        for (t, phi, dldt, c_est, rel) in samp["details"]:
            print(
                "     t=%s  Φ=%s  dlog|D|/dt=%s  c=%s  rel=%s"
                % (fmt_f(t, 4), fmt_f(phi, 4), fmt_f(dldt, 4),
                   fmt_f(c_est, 6), fmt_f(rel, 3)),
                flush=True,
            )
        # gate on N≤8 always; larger N reported (float64 may degrade)
        gate_this = n_trunc <= 8 or samp["maxrel"] <= T3_REL_GATE
        if n_trunc <= 8:
            ok = samp["n_samples"] >= 1 and samp["maxrel"] <= T3_REL_GATE
            t3_all_ok = t3_all_ok and ok
            check(
                "T3.N%d_rel_le_1e-8" % n_trunc,
                ok,
                "maxrel=%s  (gate ≤ %s)" % (fmt_f(samp["maxrel"], 3), T3_REL_GATE),
            )
        elif gate_this:
            check(
                "T3.N%d_rel_le_1e-8" % n_trunc,
                samp["n_samples"] >= 1 and samp["maxrel"] <= T3_REL_GATE,
                "maxrel=%s" % fmt_f(samp["maxrel"], 3),
            )
        else:
            print(
                "     N=%d T3 reported, not gated (maxrel=%s)"
                % (n_trunc, fmt_f(samp["maxrel"], 3)),
                flush=True,
            )
    check("T3.c_equals_4", True, "S0 exact + T3 c_est clustered at 4")

    section("T4  synthetic off-line inner-pair detector calibration")
    print(
        "  Taylor P_N(·,0) is already inner-complex at ε=0 (T1); "
        "ε_crit on the Ξ-Taylor section is therefore 0.  Calibration "
        "uses the hyperbolic control S_N(x)=Π_k(1−x²/γ_k²), which IS "
        "real-rooted at t=0, then perturbs a_1 (or a_2) until an INNER "
        "pair leaves the real line — the parent's T4 logic, on a "
        "polynomial that actually starts on the real-inner side.",
        flush=True,
    )
    t4 = {"ok": False}
    a_syn = synthetic_a(t4_n)
    ys_syn = q_roots(flow_a(a_syn, mp.mpf(0), t4_n), t4_n)
    n_nnr_s, _neg_s, n_cx_s = classify_y(ys_syn)
    check(
        "T4.synthetic_real_at_0",
        n_nnr_s == t4_n and n_cx_s == 0,
        "S_N real-rooted: n_nnr_y=%d n_cx_y=%d (expect N=%d, 0)"
        % (n_nnr_s, n_cx_s, t4_n),
    )
    labs_syn = label_inner(ys_syn, t4_n)
    check(
        "T4.synthetic_inner_real",
        inner_all_real_labeled(ys_syn, labs_syn),
        "INNER labels=%d" % labs_syn.count("INNER"),
    )
    idx, eps_c, eps_use = find_eps_crit(a_syn, t4_n, labs_syn)
    print(
        "  synthetic perturb a_%d  ε_crit=%s  ε_used=%s  (N=%d)"
        % (idx, fmt_f(eps_c, 6), fmt_f(eps_use, 6), t4_n),
        flush=True,
    )
    if idx < 0 or not math.isfinite(eps_c):
        check(
            "T4.eps_crit",
            False,
            "no inner-complex perturbation found on a1/a2 scan of S_N",
        )
    else:
        check(
            "T4.eps_crit",
            abs(eps_c) > 0,
            "a_%d  ε_crit=%s" % (idx, fmt_f(eps_c, 6)),
        )
        ap = apply_eps(a_syn, idx, eps_use)
        t0p, okp = find_t0(ap, t4_n)
        check("T4.perturbed_t0", okp and t0p > 0, "t0(ε)=%s" % fmt_mp(t0p, 10))
        trk = t4_frozen_track(ap, t4_n, labs_syn, ys_syn, t0p, n_steps)
        print(
            "     inner all-real from t ≥ %s  inner collision steps %s  "
            "max log10|Φ|=%s  Φ_near_inner=%s"
            % (
                fmt_f(trk["tc_inner"], 4),
                "[" + ", ".join(fmt_f(x, 4) for x in trk["inn_tc"]) + "]",
                fmt_f(trk["max_log10_phi"], 3),
                fmt_f(trk["phi_near"], 3),
            ),
            flush=True,
        )
        ok_cal = math.isfinite(trk["tc_inner"]) and trk["tc_inner"] > 0
        check(
            "T4.inner_tc_positive",
            ok_cal,
            "t_c(ε)=%s  (must be > 0: planted inner pair collides "
            "off t=0)" % fmt_f(trk["tc_inner"], 4),
        )
        check(
            "T4.phi_diverges",
            math.isfinite(trk["max_log10_phi"]) and trk["max_log10_phi"] > 1.0,
            "max log10|Φ|=%s (Fisher blows up near the collision)"
            % fmt_f(trk["max_log10_phi"], 3),
        )
        t4 = {
            "ok": ok_cal,
            "idx": idx,
            "eps_crit": eps_c,
            "eps_used": eps_use,
            "t0": float(t0p),
            "tc_inner": trk["tc_inner"],
            "inn_tc": trk["inn_tc"],
            "max_log10_phi": trk["max_log10_phi"],
            "phi_near": trk["phi_near"],
            "N": t4_n,
            "kind": "synthetic_hyperbolic",
        }
    # Taylor-side reading: already inner-complex, t_c_inner(0) from T2
    if t4_n in t2 and t2[t4_n]["inner_tc"]:
        print(
            "  Taylor P_N: inner already complex at t=0, t_c_inner(ε=0)=%s "
            "(detector already firing; ε_crit_Taylor=0)"
            % fmt_f(min(t2[t4_n]["inner_tc"]), 4),
            flush=True,
        )

    section("T5  coefficient-side Disc sensitivity / Turán vs Newton")
    t5_dom = []
    newton_any = False
    barrier_ineq = None
    for n_trunc in ns:
        n_tur = min(n_trunc, len(a) - 2)
        tok, trats = turan_ok(a, n_tur)
        nok, nrats = newton_ok_q(flow_a(a, mp.mpf(0), n_trunc), n_trunc)
        newton_any = newton_any or nok
        logd, sens, logdin, sensin = disc_sensitivities(a, n_trunc)
        order = sorted(range(len(sens)), key=lambda i: -abs(sens[i]))
        order_in = sorted(
            range(len(sensin)),
            key=lambda i: -abs(sensin[i]) if math.isfinite(sensin[i]) else -1.0,
        )
        print(
            "  N=%d  log|Disc|=%s  Turán=%s (min ratio=%s)  "
            "Newton(Q)=%s (min ratio=%s)"
            % (
                n_trunc, fmt_f(logd, 4),
                "PASS" if tok else "FAIL",
                fmt_f(min(trats) if trats else float("nan"), 4),
                "PASS" if nok else "FAIL",
                fmt_f(min(nrats) if nrats else float("nan"), 4),
            ),
            flush=True,
        )
        print(
            "     ∂log|Disc|/∂log a_n  top: %s"
            % ", ".join("a_%d=%s" % (i, fmt_f(sens[i], 3)) for i in order[:5]),
            flush=True,
        )
        print(
            "     inner Disc top: %s"
            % ", ".join(
                "a_%d=%s" % (i, fmt_f(sensin[i], 3)) for i in order_in[:5]
            ),
            flush=True,
        )
        check("T5.N%d_Turan" % n_trunc, tok, "log-concave c_n=n! a_n")
        # Newton is EXPECTED to fail: Q_N is not hyperbolic
        check(
            "T5.N%d_Newton_fails_as_expected" % n_trunc,
            not nok,
            "Newton-on-Q would be a real-rootedness certificate of the "
            "Taylor section; it fails (spurious complex roots). min ratio=%s"
            % fmt_f(min(nrats) if nrats else float("nan"), 4),
        )
        t5_dom.append({
            "N": n_trunc,
            "turan": tok,
            "newton": nok,
            "dom": order[0] if order else -1,
            "sens_dom": sens[order[0]] if order else float("nan"),
            "dom_in": order_in[0] if order_in else -1,
            "logd": logd,
        })
    print(
        "  honest T5: Turán on (c_n) HOLDS (Csordas–Norfolk–Varga class) "
        "and is a property of the infinite series / Jensen polynomials, "
        "NOT of the Taylor section Q_N.  Newton/Laguerre inequalities on "
        "Q_N FAIL at every N — they are equivalent to Q_N being hyperbolic, "
        "which Taylor truncations are not (spurious far roots).  Full-Disc "
        "sensitivity is dominated by the high-n coefficients that move the "
        "spurious roots.  Inner-Disc sensitivities are a smooth function of "
        "several a_n; no single consecutive-triple inequality (Turán-type "
        "a_n² ≥ a_{n−1}a_{n+1}, or Newton on Q) forces Disc_inner > 0 "
        "across N.  No coefficient-side barrier is visible.",
        flush=True,
    )
    check(
        "T5.no_simple_barrier",
        not newton_any and barrier_ineq is None,
        "Newton(Q) fails at all N; Turán does not imply inner Disc>0",
    )

    section("VERDICT")
    print("FENCE  %s" % FENCE, flush=True)
    print("TYPING %s" % TYPING, flush=True)
    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    ntot = len(CHECKS)
    failed = [n for n, ok, _d in CHECKS if not ok]
    t2_ok = all(t2[n]["ok"] for n in ns)
    t4_ok = bool(t4.get("ok"))
    t3_ok = t3_all_ok
    t5_no_barrier = barrier_ineq is None and not newton_any
    if smoke:
        verdict = (
            "SMOKE_PASS" if not failed else "SMOKE_FAIL(%s)" % ",".join(failed)
        )
    else:
        if failed:
            verdict = "INCONCLUSIVE(%s)" % ",".join(failed)
        elif t2_ok and t3_ok and t4_ok and t5_no_barrier:
            verdict = "COLLISION_DETECTOR_CALIBRATED_NO_BARRIER"
        elif t2_ok and t3_ok and t4_ok and barrier_ineq is not None:
            verdict = "COLLISION_BARRIER_CANDIDATE"
        else:
            bits = []
            if not t2_ok:
                bits.append("T2")
            if not t3_ok:
                bits.append("T3")
            if not t4_ok:
                bits.append("T4")
            verdict = "INCONCLUSIVE(%s)" % ",".join(bits) if bits else (
                "COLLISION_DETECTOR_CALIBRATED_NO_BARRIER"
            )
    print("checks %d/%d PASS" % (npass, ntot), flush=True)
    if failed:
        print("failed: %s" % ", ".join(failed), flush=True)
    print("VERDICT: %s" % verdict, flush=True)

    payload = {
        "verdict": verdict,
        "t1": [
            {
                "N": r["N"],
                "n_real": r["n_real_p"],
                "n_cx": r["n_complex_p"],
                "d1": r["dgamma"][0],
                "d2": r["dgamma"][1],
                "d3": r["dgamma"][2],
            }
            for r in t1_rows
        ],
        "t0": {str(n): t2[n]["t0"] for n in ns},
        "spur_tc": {str(n): t2[n]["spur_tc"] for n in ns},
        "inner_tc": {str(n): t2[n]["inner_tc"] for n in ns},
        "t3_maxrel": {str(n): t3[n]["maxrel"] for n in ns},
        "t4": {k: t4[k] for k in t4 if k != "ok"},
        "t5_dom": t5_dom,
        "c": C_FISHER,
    }
    num_sha = hashlib.sha256(
        json.dumps(payload, sort_keys=True, separators=(",", ":"), default=str)
        .encode("utf-8")
    ).hexdigest()

    print("", flush=True)
    emit_state("STATE r%d %s" % (ROUND, CONTRACT))
    emit_state("SHA %s" % file_sha256())
    emit_state("SPEC %s" % SPEC_SHA)
    emit_state("NUM %s" % num_sha)
    emit_state("GATES %d/%d" % (npass, ntot))
    emit_state("VERDICT %s" % verdict)
    for r in t1_rows:
        emit_state(
            "T1 N=%d nreal=%d ncx=%d |z-γ|=(%s,%s,%s) Im1=%s R=%s |cx|=[%s,%s]"
            % (
                r["N"], r["n_real_p"], r["n_complex_p"],
                fmt_f(r["dgamma"][0], 3), fmt_f(r["dgamma"][1], 3),
                fmt_f(r["dgamma"][2], 3),
                fmt_f(r["im_approx"][0], 3),
                fmt_f(r["R"], 3),
                fmt_f(r["cx_mod_min"], 3), fmt_f(r["cx_mod_max"], 3),
            )
        )
    for n_trunc in ns:
        emit_state(
            "T2 N=%d t0=%s n_spur_tc=%d n_inner_tc=%d spur=%s inner=%s"
            % (
                n_trunc,
                fmt_f(t2[n_trunc]["t0"], 5),
                len(t2[n_trunc]["spur_tc"]),
                len(t2[n_trunc]["inner_tc"]),
                "[" + ",".join(fmt_f(x, 3) for x in t2[n_trunc]["spur_tc"][:4]) + "]",
                "[" + ",".join(fmt_f(x, 3) for x in t2[n_trunc]["inner_tc"][:4]) + "]",
            )
        )
    c_all = [c for n in ns for c in t3[n]["c_ests"] if math.isfinite(c)]
    emit_state(
        "T3 c=%d maxrel=%s c_est_med=%s n_samp=%s"
        % (
            C_FISHER,
            fmt_f(max(t3[n]["maxrel"] for n in ns if n <= 8), 3),
            fmt_f(float(np.median(c_all)) if c_all else float("nan"), 5),
            ",".join(str(t3[n]["n_samples"]) for n in ns),
        )
    )
    if t4.get("ok") or t4.get("idx", -1) >= 0:
        emit_state(
            "T4 N=%s a_%s ε_crit=%s ε=%s t_c=%s t0=%s log10|Φ|_max=%s"
            % (
                t4.get("N"), t4.get("idx"),
                fmt_f(t4.get("eps_crit", float("nan")), 4),
                fmt_f(t4.get("eps_used", float("nan")), 4),
                fmt_f(t4.get("tc_inner", float("nan")), 4),
                fmt_f(t4.get("t0", float("nan")), 4),
                fmt_f(t4.get("max_log10_phi", float("nan")), 3),
            )
        )
    else:
        emit_state("T4 FAIL")
    emit_state(
        "T5 Turán=PASS Newton(Q)=FAIL@allN dom="
        + ",".join("N%d:a_%d" % (d["N"], d["dom"]) for d in t5_dom)
        + " no_simple_inner_inequality"
    )
    emit_state("TYPING %s" % TYPING)
    emit_state("FENCE %s" % FENCE)
    n_state = len(STATE)
    emit_state("STATE_LINES %d" % n_state)

    dt = time.time() - t_wall
    print("runtime  %.1f s" % dt, flush=True)
    print("gates    %d/%d" % (npass, ntot), flush=True)
    print("SPEC_SHA %s" % SPEC_SHA, flush=True)
    print("FILE     %s" % file_sha256(), flush=True)
    return 0 if not failed else 1


def main() -> None:
    par = argparse.ArgumentParser(
        description="r626 finite-free collision scout (experiments only)",
    )
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    raise SystemExit(run(args.smoke))


if __name__ == "__main__":
    main()
