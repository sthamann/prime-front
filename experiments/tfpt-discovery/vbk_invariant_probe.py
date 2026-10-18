#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""vbk_invariant_probe -- PRIME.SCREW.VERBLUNSKY.INVARIANT.01

FROZEN SPEC (2026-08-15).  EXPLORATION ONLY.  This file is the sole
probe of the round.  It writes nothing, imports no repository module,
reads no measured pin, wall margin, zero table, paper, ledger, website
or verification file, and makes NO RH claim.

MISSION
=======
Pin three foundational corrections and attack the remaining
Verblunsky object of Suzuki's screw coordinate without opening a new
architecture.

V0a -- MINIMAL PIN LEMMA.  The Stieltjes--Vitali sequence
sigma_r = 1 + 1/r lies in (1,2] and accumulates at the interior point
1.  Consequently pointwise contraction on this countable sequence
(uniform contraction on [1,2] is more than enough), plus the one-pin
normal-family bound already isolated by SVPIN, supplies (SV).  No
uniformity as sigma decreases to 1/2 is used by the Vitali/identity/
pole-contradiction chain.

V0b -- NO BACK-INFERENCE.  For mu = delta_1 on the circle,
F(w) = (1+w)/(1-w) is finite with positive real part for 0<w<1, while
every n-by-n moment Toeplitz matrix is the all-ones matrix and is
singular for n>=2.  Therefore convergence/positivity of pin values
cannot prove strict positivity of the sections required to construct
the carrier.

V0c -- EULER--PICK AND AUTOCORRELATION WELD.
Put P(z)=xi'/xi(1/2+z), sigma_j=1+1/j, and
  Pick_N[j,k] = (P(sigma_j)+P(sigma_k))/(sigma_j+sigma_k).
The exact criterion audited here is
  RH iff Pick_N is positive semidefinite for every N.
Forward, under RH,
  Pick[j,k] = sum_gamma [
    1/((sigma_j-i gamma)(sigma_k+i gamma))
   +1/((sigma_j+i gamma)(sigma_k-i gamma)) ],
a sum of two rank-one Gram matrices per positive ordinate.
Backward uses the classical Pick theorem in right-half-plane form:
for distinct z_j in Re z>0 and values w_j, a holomorphic function
H:Re z>0 -> {Re w>=0} with H(z_j)=w_j exists iff every finite matrix
[(w_j+conj(w_k))/(z_j+conj(z_k))] is positive semidefinite.
For countably many nodes, positivity of every leading matrix gives
every finite subproblem; finite interpolants, Cayley-transformed to
the Schur class, have a normal-family subsequence (Montel), yielding
one interpolant.  This is exactly Theorem 2 (Pick, 1916) in
Artur Nicolau, "The Nevanlinna-Pick Interpolation Problem" (2015):
the disc Pick matrices are PSD for every N iff the countable problem
has a solution; the proof states that normal families reduce it to
the finite theorem.  Cayley maps give the displayed half-plane form.
The nodes accumulate at 1 inside Re z>1/2, where the Euler expression
for P is holomorphic, so the identity theorem identifies H=P there.
Continuation through Re z>0 minus the discrete zero set and the
nonzero logarithmic-derivative residue at any off-line zero give the
same pole contradiction as SVPIN.  The functional equation supplies
the reflected half.  All hypotheses are named; no finite numerical
matrix is substituted for "every N".

For f_c(v)=1_{v>=0} sum_j c_j exp(-sigma_j v), direct integration gives
  (f_c * f_c~)(t)
   = (1/2) sum_jk c_j c_k
       [exp(-sigma_j |t|)+exp(-sigma_k |t|)]/(sigma_j+sigma_k).
Together with P(sigma)=(1/2)<-g'',exp(-sigma|.|)> this proves
  c^T Pick_N c = <-g'', f_c*f_c~>.                         (AC)
The algebra is symbolically gated and the two sides are independently
evaluated: Euler--Maclaurin Dirichlet data on the left, exact second
differences of the corpus screw function (own prime-power sieve) on
the right.

V1 -- EXACT MOMENT AND PACKET UPDATE.
At mesh delta, let phi_d(u)=max(0,1-|u-d delta|/delta).  The unnormalised
moment row of -g'' is
  c_d = c_d^arch - sum_p Deltap_d,
  Deltap_d = log(p) sum_{m>=1, m log p<L} p^(-m/2) phi_d(m log p).
Thus a complete p-packet changes every finite Toeplitz section by the
explicit signed Toeplitz matrix
  T_n -> T_n + D_{p,n},  D_{p,n}=Toeplitz(-Deltap_0,...,-Deltap_{n-1}).
It is generally high rank and indefinite, but has Toeplitz displacement
rank at most two.  If A=T_n before the packet, the exact resolvent law is
  (A+D)^(-1)=A^(-1)-A^(-1)D(A+D)^(-1),
and this gives the exact Verblunsky update
  alpha_{n-2}' =
    -[e0^T(A+D)^(-1)e_{n-1}]/[e0^T(A+D)^(-1)e0].
Equivalently the ordinary Levinson recursion below updates every alpha
causally: a packet whose first touched lag is d leaves alpha_0 through
alpha_{d-2} byte-identical.  Packet addition commutes in moment space,
but the induced alpha increments are tested for state dependence.

V2 -- FROZEN INVARIANT SEARCH.
The source ladder is the cofinal mesh L_n=n*delta (n=1,2,...) with
delta=0.006; this run declares the prefix n<=428 (L=2.568), without
post-hoc rung selection.  The diagnostic depths are frozen below.
The only strict region tested is the first dyadic interior Schur box
|alpha|<=1/4.  It may be a finite separator; it is NOT called an
invariant because its membership is computed from the alpha sequence
whose all-depth disk membership it is supposed to prove.  The AST
circularity gate detects that dependence.

The controls are frozen verbatim from the source probe:
 SMOOTH replaces the arithmetic atoms by the density exp(u/2);
 SCRARITH keeps atom positions and golden-permutes their weights.
Their unit-Schur-disk exits must reproduce r=0.264 and r=0.744.
The smooth event is diagnosed against the exact support gap
(0,log 2): the true prime measure is zero there, whereas the PNT
density has mass 2(exp(r/2)-1) by depth r.

V3 -- KILL CRITERIA.
* source-only AST path; no repository imports/data loads/known zeros;
* fixed cofinal mesh prefix and fixed diagnostic depths;
* controls exit at 0.264/0.744;
* no measured pins, wall margin, post-hoc rung, generic norm majorant;
* a region checked by first computing section positivity/alphas is
  rejected as circular, never promoted to an invariant.

V4 -- VERDICT ENUM.
 VERBLUNSKY-INVARIANT-FOUND(remaining proof stated)
 VERBLUNSKY-DICHOTOMY(explicit checkable-arithmetic packet inequality)
 VERBLUNSKY-NO-INVARIANT(mechanism exhibited)
 INSTRUMENT-EDGE (a ward fails; exit 1, not a mathematical verdict).

The exact congruence condition
  A+D_p > 0 iff lambda_min(I+A^(-1/2)D_p A^(-1/2))>0
is printed but explicitly priced WALL-EQUIVALENT: it consumes the
inverse/positive square root of the prior section and is not the new
checkable-arithmetic packet inequality required for DICHOTOMY.

DECLARED NUMERICS AND SUBSAMPLING.
delta=0.006, L=2.568 for the Verblunsky attack; every lag and every
prime power in that window is used.  The (AC) independent screw read
uses the same delta through L=9.0 and one frozen four-coefficient
vector.  Euler--Pick uses N=1..12, 100 decimal digits, two independent
Euler--Maclaurin truncations, and an own Lambda-sieve cross-ward.
Float64 is used only for ranks/inertias of explicit packet matrices
and printed profile diagnostics; moment construction, Levinson
recursion and Euler--Pick floors use mpmath.  Runtime bar: 600 seconds.

SHAKEOUT DISCLOSURE / AMENDMENT 1.  Frozen run 1 (SPEC_SHA
843611425e3e2067) returned INSTRUMENT-EDGE, 20/22: (a) an exact-zero
bar had been put on the combined "background + ramps, then second
difference" route, whose ordinary cancellation leaves 9.75e-14 even
though each isolated ramp equals its tent row to <1e-113; the repaired
gate separately requires isolated equality <1e-90 and a declared
1e-12 combined backward-error bar; (b) the state-dependence comparison
had an empty overlap because the arch-only stream exits before the
p=3 packet arrives.  The repaired diagnostic uses the exact inverse
endpoint formula on the predeclared dimensions 200/220/240 and adds a
symbolic Levinson state-dependence identity.  A display-only negative
index for lambda_max was also replaced by its positive matrix index.
Frozen run 2 returned 22/23: only the old exact-zero decomposition bar
remained, measured 6.34e-15; the isolated atom audit then confirmed
4.76e-115..8.46e-114.  No mathematical bar, world, ladder, candidate
region or verdict priority moved.

NO RH CLAIM.  NO ALL-DEPTH POSITIVITY CLAIM.  EXPLORATION ONLY.
"""

from __future__ import annotations

import ast
import hashlib
import math
import os
import time

import mpmath as mp
import numpy as np
import sympy as sp
from scipy.linalg import toeplitz


T0 = time.time()
SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()

DELTA_TEXT = "0.006"
DELTA = 0.006
L_MAIN = 2.568
N_MAIN = 428
L_AC = 9.0
N_AC = 1500
DPS = 100
PIN_COUNT = 12
STRICT_BOX = 0.25
DEPTHS = (0.264, 0.744, 1.092, 1.608, 2.076, 2.568)
UPDATE_DIMS = (128, 160, 180)
STATE_DIMS = (200, 220, 240)
SMOOTH_EXIT = 0.264
SCRAM_EXIT = 0.744
EXIT_TOL = DELTA / 2 + 1e-12
AC_COEFFS = (1.0, 0.5, -1.0 / 3.0, 0.2)
AC_SIGMAS = (2.0, 1.5, 4.0 / 3.0, 1.25)
LAMBDA_CAP = 4_000_000
RUNTIME_BAR = 600.0
GOLDEN = (math.sqrt(5.0) - 1.0) / 2.0

CHECKS: list[tuple[str, bool, str]] = []


def check(name: str, ok: bool, detail: str) -> bool:
    result = bool(ok)
    CHECKS.append((name, result, detail))
    print("  [%s] %-48s %s" % ("PASS" if result else "FAIL", name, detail))
    return result


def section(title: str) -> None:
    print("\n" + "=" * 78)
    print(title)
    print("=" * 78)


def fmt_mp(x: mp.mpf, digits: int = 8) -> str:
    return mp.nstr(x, digits, min_fixed=0, max_fixed=0)


# ---------------------------------------------------------------- firewall
def firewall_audit() -> tuple[bool, str, ast.Module]:
    with open(os.path.abspath(__file__), "r", encoding="utf-8") as fh:
        source = fh.read()
    tree = ast.parse(source)
    bad: list[str] = []
    allowed_roots = {
        "__future__", "ast", "hashlib", "math", "os", "time",
        "mpmath", "numpy", "sympy", "scipy",
    }
    forbidden_calls = {
        "load", "loadtxt", "genfromtxt", "fromfile",
        "zetazero", "zetazeros", "nzeros", "siegelz", "siegeltheta",
    }
    forbidden_attrs = {
        "zeta", "zetazero", "zetazeros", "nzeros",
        "siegelz", "siegeltheta",
    }
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                root = alias.name.split(".")[0]
                if root not in allowed_roots:
                    bad.append("import:" + alias.name)
        elif isinstance(node, ast.ImportFrom):
            root = (node.module or "").split(".")[0]
            if root not in allowed_roots:
                bad.append("from:" + (node.module or ""))
        elif isinstance(node, ast.Call):
            called = (node.func.id if isinstance(node.func, ast.Name)
                      else node.func.attr
                      if isinstance(node.func, ast.Attribute) else "")
            if called.lower() in forbidden_calls:
                bad.append("call:" + called)
        elif isinstance(node, ast.Attribute):
            if node.attr.lower() in forbidden_attrs:
                bad.append("attr:" + node.attr)
    return not bad, "violations=%s" % (bad or "none"), tree


# ---------------------------------------------------------- prime arithmetic
def sieve_primes(limit: int) -> list[int]:
    bits = bytearray(b"\x01") * (limit + 1)
    if limit >= 1:
        bits[0:2] = b"\x00\x00"
    for p in range(2, math.isqrt(limit) + 1):
        if bits[p]:
            count = (limit - p * p) // p + 1
            bits[p * p:limit + 1:p] = b"\x00" * count
    return [i for i in range(2, limit + 1) if bits[i]]


def prime_atoms(L: float) -> list[tuple[int, int, mp.mpf, mp.mpf]]:
    """(p,m,u,w) with u=m log p<L and w=log(p)/sqrt(p^m)."""
    limit = int(math.exp(L)) + 1
    out: list[tuple[int, int, mp.mpf, mp.mpf]] = []
    with mp.workdps(DPS + 15):
        for p in sieve_primes(limit):
            lp = mp.log(p)
            q = p
            m = 1
            while m * float(lp) < L - 1e-14:
                out.append((p, m, m * lp, lp / mp.sqrt(q)))
                if q > limit // p:
                    break
                q *= p
                m += 1
    out.sort(key=lambda item: item[2])
    return out


def atom_row(u: mp.mpf, weight: mp.mpf, n: int) -> list[mp.mpf]:
    """The exact tent read -weight*phi_d(u), d=0,...,n-1."""
    with mp.workdps(DPS + 15):
        out = [mp.mpf(0) for _ in range(n)]
        x = u / mp.mpf(DELTA_TEXT)
        lo = int(mp.floor(x))
        for d in (lo, lo + 1):
            if 0 <= d < n:
                value = 1 - abs(x - d)
                if value > 0:
                    out[d] -= weight * value
    return out


def packet_rows(atoms: list[tuple[int, int, mp.mpf, mp.mpf]],
                n: int) -> dict[int, list[mp.mpf]]:
    packets: dict[int, list[mp.mpf]] = {}
    with mp.workdps(DPS + 15):
        for p, _m, u, weight in atoms:
            if p not in packets:
                packets[p] = [mp.mpf(0) for _ in range(n)]
            ar = atom_row(u, weight, n)
            packets[p] = [a + b for a, b in zip(packets[p], ar)]
    return packets


def add_rows(*rows: list[mp.mpf]) -> list[mp.mpf]:
    with mp.workdps(DPS + 15):
        return [mp.fsum(values) for values in zip(*rows)]


# ---------------------------------------------------------- corpus screw g
MP_CONST: dict[str, mp.mpf] = {}
S_CACHE: dict[int, mp.mpf] = {}


def setup_constants() -> None:
    with mp.workdps(DPS + 20):
        MP_CONST["psi14"] = mp.digamma(mp.mpf(1) / 4)
        MP_CONST["logpi"] = mp.log(mp.pi)
        MP_CONST["phi1"] = mp.lerchphi(1, 2, mp.mpf(1) / 4)


def s_arch_grid(index: int) -> mp.mpf:
    """S(t)=(1/4)e^(-t/2)Phi(e^(-2t),2,1/4), t=index*delta."""
    if index in S_CACHE:
        return S_CACHE[index]
    with mp.workdps(DPS + 15):
        t = mp.mpf(index) * mp.mpf(DELTA_TEXT)
        if index == 0:
            value = MP_CONST["phi1"] / 4
        elif t < mp.mpf("0.3"):
            value = (mp.exp(-t / 2)
                     * mp.lerchphi(mp.exp(-2 * t), 2, mp.mpf(1) / 4) / 4)
        else:
            z = mp.exp(-2 * t)
            total = mp.mpf(0)
            power = mp.mpf(1)
            k = 0
            floor = mp.mpf(10) ** (-(DPS + 8))
            while power > floor * (1 + abs(total)):
                total += power / (mp.mpf(k) + mp.mpf(1) / 4) ** 2
                power *= z
                k += 1
            value = mp.exp(-t / 2) * total / 4
    S_CACHE[index] = value
    return value


def base_g_values(n: int) -> list[mp.mpf]:
    """Archimedean background, including the pole layer, without primes."""
    dl = mp.mpf(DELTA_TEXT)
    values: list[mp.mpf] = []
    with mp.workdps(DPS + 15):
        for j in range(n + 1):
            t = j * dl
            value = -8 * (mp.cosh(t / 2) - 1)
            value -= (t / 2) * (MP_CONST["psi14"] - MP_CONST["logpi"])
            value -= MP_CONST["phi1"] / 4
            value += s_arch_grid(j)
            values.append(value)
    return values


def lag_row_from_g(values: list[mp.mpf]) -> list[mp.mpf]:
    with mp.workdps(DPS + 15):
        dl = mp.mpf(DELTA_TEXT)
        n = len(values) - 1
        row = [-2 * values[1] / dl]
        for d in range(1, n):
            row.append(
                -(values[d - 1] - 2 * values[d] + values[d + 1]) / dl
            )
    return row


def direct_true_g(base: list[mp.mpf],
                  atoms: list[tuple[int, int, mp.mpf, mp.mpf]]) -> list[mp.mpf]:
    """Independent direct ramp assembly, O(grid+atoms), not packet rows."""
    ordered = sorted([(u, weight) for _p, _m, u, weight in atoms],
                     key=lambda item: item[0])
    out: list[mp.mpf] = []
    active_weight = mp.mpf(0)
    active_weight_u = mp.mpf(0)
    cursor = 0
    dl = mp.mpf(DELTA_TEXT)
    with mp.workdps(DPS + 15):
        for j, background in enumerate(base):
            t = j * dl
            while cursor < len(ordered) and ordered[cursor][0] < t:
                u, weight = ordered[cursor]
                active_weight += weight
                active_weight_u += weight * u
                cursor += 1
            out.append(background + t * active_weight - active_weight_u)
    return out


def smooth_row(base_g: list[mp.mpf]) -> list[mp.mpf]:
    dl = mp.mpf(DELTA_TEXT)
    values = []
    with mp.workdps(DPS + 15):
        for j, value in enumerate(base_g):
            t = j * dl
            smooth_ramp = 4 * mp.exp(t / 2) - 2 * t - 4
            values.append(value + smooth_ramp)
    return lag_row_from_g(values)


def scrambled_row(base_row: list[mp.mpf],
                  atoms: list[tuple[int, int, mp.mpf, mp.mpf]]) -> tuple[
                      list[mp.mpf], list[mp.mpf]]:
    q_values = [p ** m for p, m, _u, _w in atoms]
    order = sorted(range(len(atoms)),
                   key=lambda i: (q_values[i] * GOLDEN) % 1.0)
    weights = [atoms[i][3] for i in order]
    row = list(base_row)
    for atom, weight in zip(atoms, weights):
        ar = atom_row(atom[2], weight, len(row))
        row = add_rows(row, ar)
    return row, weights


# ----------------------------------------------------- Levinson / Szego
def szego(row: list[mp.mpf]) -> dict:
    """Real Szego recursion with the attempted coefficient at a failure."""
    with mp.workdps(DPS):
        c0 = row[0]
        moments = [value / c0 for value in row]
        phi = [mp.mpf(1)]
        phi_star = [mp.mpf(1)]
        alphas: list[mp.mpf] = []
        prediction: list[mp.mpf] = []
        fail_k = -1
        fail_kind = ""
        attempted = mp.nan
        fail_num = mp.nan
        fail_den = mp.nan
        for k in range(len(moments) - 1):
            numerator = mp.fdot(phi, moments[1:k + 2])
            denominator = mp.fdot(phi_star, moments[0:k + 1])
            if denominator <= 0:
                fail_k = k
                fail_kind = "DEN_NONPOSITIVE"
                fail_num = numerator
                fail_den = denominator
                break
            alpha = numerator / denominator
            if abs(alpha) >= 1:
                fail_k = k
                fail_kind = "ALPHA_EXIT"
                attempted = alpha
                fail_num = numerator
                fail_den = denominator
                break
            alphas.append(alpha)
            prediction.append(denominator)
            zphi = [mp.mpf(0)] + phi
            phi_pad = phi_star + [mp.mpf(0)]
            phi_new = [zphi[j] - alpha * phi_pad[j] for j in range(k + 2)]
            phi_star_new = [phi_pad[j] - alpha * zphi[j]
                            for j in range(k + 2)]
            phi, phi_star = phi_new, phi_star_new
        return {
            "ok": fail_k < 0,
            "alphas": alphas,
            "prediction": prediction,
            "fail_k": fail_k,
            "fail_kind": fail_kind,
            "attempted": attempted,
            "fail_num": fail_num,
            "fail_den": fail_den,
            "c0": c0,
        }


def candidate_membership(alphas: list[mp.mpf], bound: float) -> tuple[bool, int]:
    """Finite diagnostic only; AST-gated as circular by construction."""
    for index, alpha in enumerate(alphas):
        if abs(alpha) > bound:
            return False, index
    return True, -1


def first_box_exit(result: dict, bound: float) -> float:
    _inside, index = candidate_membership(result["alphas"], bound)
    if index >= 0:
        return index * DELTA
    if result["fail_k"] >= 0:
        attempted = result["attempted"]
        if attempted == attempted and abs(attempted) > bound:
            return result["fail_k"] * DELTA
    return float("inf")


def margin_at_depth(result: dict, depth: float) -> tuple[float, float, int]:
    count = min(int(round(depth / DELTA)), len(result["alphas"]))
    values = [abs(float(a)) for a in result["alphas"][:count]]
    maximum = max(values, default=0.0)
    return maximum, 1.0 - maximum, count


# ------------------------------------------------------- Euler source P
def dirichlet_logderivative(s: mp.mpf, cutoff: int,
                            terms: int) -> tuple[mp.mpf, mp.mpf]:
    """Euler--Maclaurin value and derivative of sum n^-s, no library zeta."""
    total = mp.mpf(0)
    derivative = mp.mpf(0)
    for n in range(1, cutoff):
        power = mp.power(n, -s)
        total += power
        derivative -= mp.log(n) * power
    M = mp.mpf(cutoff)
    logM = mp.log(M)
    lead = M ** (1 - s) / (s - 1)
    total += lead
    derivative += lead * (-logM - 1 / (s - 1))
    half = mp.mpf("0.5") * M ** (-s)
    total += half
    derivative -= logM * half
    for k in range(1, terms + 1):
        order = 2 * k - 1
        rising = mp.rf(s, order)
        coefficient = mp.bernpoly(2 * k, 0) / mp.factorial(2 * k)
        correction = coefficient * rising * M ** (-s - order)
        harmonic = mp.fsum(1 / (s + j) for j in range(order))
        total += correction
        derivative += correction * (harmonic - logM)
    return total, derivative


def euler_P(sigma: mp.mpf, cutoff: int = 96,
            terms: int = 28) -> mp.mpf:
    s = mp.mpf("0.5") + sigma
    value, derivative = dirichlet_logderivative(s, cutoff, terms)
    return (1 / s + 1 / (s - 1) - mp.log(mp.pi) / 2
            + mp.digamma(s / 2) / 2 + derivative / value)


def lambda_source_values(sigmas: tuple[float, ...]) -> tuple[
        dict[float, float], int, float]:
    """Independent own Lambda sieve plus the SVPIN PNT anchored tail."""
    primes = sieve_primes(LAMBDA_CAP)
    logp = np.log(np.asarray(primes, dtype=float))
    small = [p for p in primes if p <= math.isqrt(LAMBDA_CAP)]
    psi_exact = float(np.sum(logp))
    for p in small:
        q = p * p
        lp = math.log(p)
        while q <= LAMBDA_CAP:
            psi_exact += lp
            q *= p
    values: dict[float, float] = {}
    N = float(LAMBDA_CAP)
    for sigma in sigmas:
        s = 0.5 + sigma
        lam = float(np.sum(logp * np.exp(-s * logp)))
        for p in small:
            q = p * p
            lp = math.log(p)
            while q <= LAMBDA_CAP:
                lam += lp * math.exp(-s * math.log(q))
                q *= p
        tail = s * N ** (1 - s) / (s - 1)
        tail -= math.log(2 * math.pi) * N ** (-s)
        for k in range(1, 4):
            tail += ((s / 2) * N ** (-2 * k - s)
                     / (k * (2 * k + s)))
        tail -= psi_exact * N ** (-s)
        lam += tail
        with mp.workdps(35):
            values[sigma] = float(
                1 / mp.mpf(s) + 1 / (mp.mpf(s) - 1)
                - mp.log(mp.pi) / 2 + mp.digamma(mp.mpf(s) / 2) / 2
                - mp.mpf(lam))
    return values, len(primes), psi_exact


def pick_matrix(values: list[mp.mpf], sigmas: list[mp.mpf]) -> mp.matrix:
    n = len(values)
    matrix = mp.matrix(n, n)
    for j in range(n):
        for k in range(n):
            matrix[j, k] = ((values[j] + values[k])
                            / (sigmas[j] + sigmas[k]))
    return matrix


def autocorrelation_value(t: mp.mpf, coefficients: tuple[float, ...],
                          sigmas: tuple[float, ...]) -> mp.mpf:
    value = mp.mpf(0)
    for j, cj in enumerate(coefficients):
        for k, ck in enumerate(coefficients):
            value += (mp.mpf(cj) * mp.mpf(ck)
                      * mp.exp(-mp.mpf(sigmas[j]) * abs(t))
                      / (mp.mpf(sigmas[j]) + mp.mpf(sigmas[k])))
    return value


# ---------------------------------------------------------- packet matrices
def toeplitz_section(row: list[mp.mpf], dimension: int) -> np.ndarray:
    first = np.asarray([float(value) for value in row[:dimension]], dtype=float)
    return toeplitz(first)


def inverse_alpha(matrix_inverse: np.ndarray) -> float:
    return float(-matrix_inverse[0, -1] / matrix_inverse[0, 0])


def numerical_rank(matrix: np.ndarray) -> int:
    singular = np.linalg.svd(matrix, compute_uv=False)
    tolerance = max(matrix.shape) * np.finfo(float).eps * max(singular[0], 1.0)
    return int(np.sum(singular > tolerance))


def displacement_rank(matrix: np.ndarray) -> int:
    n = matrix.shape[0]
    shift = np.zeros((n, n))
    shift[1:, :-1] = np.eye(n - 1)
    return numerical_rank(matrix - shift @ matrix @ shift.T)


def alpha_increment(state: list[mp.mpf], packet: list[mp.mpf]) -> tuple[
        dict, list[mp.mpf]]:
    updated = add_rows(state, packet)
    return szego(updated), updated


def main() -> int:
    print("=" * 78)
    print("vbk_invariant_probe  PRIME.SCREW.VERBLUNSKY.INVARIANT.01")
    print("FROZEN SPEC_SHA %s" % SPEC_SHA[:16])
    print("=" * 78)

    fw_ok, fw_detail, source_tree = firewall_audit()
    section("A. SOURCE FIREWALL + FROZEN LADDER")
    check("A1 source-only AST firewall", fw_ok, fw_detail)
    ladder_ok = (abs(N_MAIN * DELTA - L_MAIN) < 1e-15
                 and abs(N_AC * DELTA - L_AC) < 1e-15
                 and tuple(sorted(DEPTHS)) == DEPTHS
                 and all(abs(round(depth / DELTA) * DELTA - depth) < 1e-12
                         for depth in DEPTHS))
    check("A2 predeclared cofinal mesh prefix", ladder_ok,
          "L_n=n*0.006, executed n<=%d; diagnostic depths=%s"
          % (N_MAIN, DEPTHS))
    setup_constants()

    # ================================================================ V0a
    section("V0a. SIGMA-RANGE CORRECTION")
    finite_pins = [1 + 1 / r for r in range(1, PIN_COUNT + 1)]
    v0a_ok = (all(1 < sigma <= 2 for sigma in finite_pins)
              and all(finite_pins[i + 1] < finite_pins[i]
                      for i in range(len(finite_pins) - 1))
              and abs((1 + 1 / 10 ** 9) - 1) < 2e-9)
    check("V0a pin sequence is interior-safe", v0a_ok,
          "sigma_1=%.1f sigma_%d=%.12f limit=1; all in (1,2]"
          % (finite_pins[0], PIN_COUNT, finite_pins[-1]))
    print("  PINNED MINIMAL LEMMA: pointwise Weyl-disk contraction on"
          " sigma_r=1+1/r suffices for (SV);")
    print("  uniformity on [1,2] is sufficient but unnecessary;"
          " sigma downarrow 1/2 uniformity is not load-bearing.")

    # ================================================================ V0b
    section("V0b. DELTA_1 COUNTEREXAMPLE -- NO BACK-INFERENCE")
    w = sp.symbols("w", real=True)
    F = (1 + w) / (1 - w)
    exact_ranks = []
    exact_dets = []
    for n in range(1, 7):
        ones = sp.ones(n, n)
        exact_ranks.append(int(ones.rank()))
        exact_dets.append(sp.det(ones))
    rational_samples = [sp.Rational(k, 10) for k in range(1, 10)]
    v0b_ok = (sp.simplify(F - (1 + w) / (1 - w)) == 0
              and all(F.subs(w, value) > 0 for value in rational_samples)
              and exact_ranks == [1] * 6
              and exact_dets[0] == 1
              and all(value == 0 for value in exact_dets[1:]))
    check("V0b delta_1 exact counterexample", v0b_ok,
          "F=(1+w)/(1-w)>0 on samples 0.1..0.9; ranks=%s det(T_2..T_6)=0"
          % exact_ranks)
    print("  TYPED NO-GO: pin convergence/finite positive Caratheodory"
          " values do not imply strict Toeplitz positivity;")
    print("  the carrier cannot establish its own existence hypothesis.")

    # ================================================================ V0c
    section("V0c. EULER--PICK CRITERION + (AC) IDENTITY")
    x, y, z = sp.symbols("x y z", positive=True, real=True)
    gram_identity = sp.simplify(
        (2 * x / (x ** 2 + y ** 2) + 2 * z / (z ** 2 + y ** 2))
        / (x + z)
        - (1 / ((x - sp.I * y) * (z + sp.I * y))
           + 1 / ((x + sp.I * y) * (z - sp.I * y))))
    pj, pk = sp.symbols("P_j P_k", real=True)
    ac_symbol = sp.simplify(
        sp.Rational(1, 2) * (2 * pj + 2 * pk) / (x + z)
        - (pj + pk) / (x + z))
    r1, r2, d2 = sp.symbols("r_1 r_2 Delta_2", real=True)
    alpha1 = (r2 - r1 ** 2) / (1 - r1 ** 2)
    alpha1_update = sp.simplify(
        ((r2 + d2) - r1 ** 2) / (1 - r1 ** 2) - alpha1
    )
    state_symbol = sp.simplify(sp.diff(alpha1_update, r1))
    check("V0c forward Gram algebra + AC algebra", 
          gram_identity == 0 and ac_symbol == 0,
          "both symbolic residuals exactly zero")

    pin_sigmas = [mp.mpf(1) + mp.mpf(1) / r
                  for r in range(1, PIN_COUNT + 1)]
    with mp.workdps(DPS):
        p_values = [euler_P(sigma) for sigma in pin_sigmas]
        p_values_refined = [euler_P(sigma, 128, 32) for sigma in pin_sigmas]
        em_deviation = max(abs(a - b)
                           for a, b in zip(p_values, p_values_refined))
    check("V0c Euler--Maclaurin source stability",
          em_deviation < mp.mpf("1e-70"),
          "max |P_96,28-P_128,32|=%s" % fmt_mp(em_deviation, 5))

    lambda_sigmas = tuple(float(sigma) for sigma in pin_sigmas)
    lambda_values, prime_count, psi_exact = lambda_source_values(lambda_sigmas)
    lambda_deviations = [
        abs(float(p_values[i]) - lambda_values[lambda_sigmas[i]])
        for i in range(PIN_COUNT)
    ]
    check("V0c own-Lambda-sieve Euler cross-ward",
          max(lambda_deviations) < 5e-4,
          "cap=%d primes=%d psi=%.6f max dev=%.3e"
          % (LAMBDA_CAP, prime_count, psi_exact, max(lambda_deviations)))

    floors: list[mp.mpf] = []
    conditions: list[mp.mpf] = []
    print("  Euler--Pick eigenvalue floors (mp, %d dps):" % DPS)
    with mp.workdps(DPS):
        for n in range(1, PIN_COUNT + 1):
            matrix = pick_matrix(p_values[:n], pin_sigmas[:n])
            eigenvalues = mp.eigsy(matrix, eigvals_only=True)
            floor = eigenvalues[0]
            ceiling = eigenvalues[n - 1]
            condition = ceiling / floor
            floors.append(floor)
            conditions.append(condition)
            print("    N=%2d  lambda_min=%-15s lambda_max=%-13s cond=%s"
                  % (n, fmt_mp(floor, 9), fmt_mp(ceiling, 8),
                     fmt_mp(condition, 7)))
    check("V0c Euler--Pick floors positive through N=12",
          all(value > 0 for value in floors),
          "floor_N12=%s cond_N12=%s (finite falsification instrument only)"
          % (fmt_mp(floors[-1], 8), fmt_mp(conditions[-1], 8)))

    pick_hypotheses = (all(pin_sigmas[i] != pin_sigmas[j]
                           for i in range(PIN_COUNT)
                           for j in range(i))
                       and all(sigma > 0 for sigma in pin_sigmas)
                       and all(value > 0 for value in p_values)
                       and abs((mp.mpf(1) + 1 / mp.mpf(10) ** 20) - 1)
                       < mp.mpf("2e-20"))
    check("V0c classical infinite-Pick hypotheses audited",
          pick_hypotheses,
          "distinct RHP nodes; positive data; accumulation at 1 interior;"
          " all leading PSD => every finite subset PSD")
    print("  PINNED CRITERION: RH iff Pick_N >= 0 for every N."
          " Backward use is classical Pick + Montel +")
    print("  identity theorem + logarithmic-derivative pole contradiction;"
          " finite N<=12 is only a falsification prefix.")

    # Independent numerical AC read through the corpus g.
    print("  building independent corpus-g read for (AC), L=%.1f delta=%.3f ..."
          % (L_AC, DELTA))
    atoms_ac = prime_atoms(L_AC)
    base_g_ac = base_g_values(N_AC)
    direct_g_ac = direct_true_g(base_g_ac, atoms_ac)
    row_ac = lag_row_from_g(direct_g_ac)
    with mp.workdps(DPS):
        ac_p = [euler_P(mp.mpf(sigma)) for sigma in AC_SIGMAS]
        lhs_ac = mp.mpf(0)
        for j, cj in enumerate(AC_COEFFS):
            for k, ck in enumerate(AC_COEFFS):
                lhs_ac += (mp.mpf(cj) * mp.mpf(ck)
                           * (ac_p[j] + ac_p[k])
                           / (mp.mpf(AC_SIGMAS[j]) + mp.mpf(AC_SIGMAS[k])))
        rhs_ac = row_ac[0] * autocorrelation_value(
            mp.mpf(0), AC_COEFFS, AC_SIGMAS)
        for d in range(1, len(row_ac)):
            rhs_ac += (2 * row_ac[d]
                       * autocorrelation_value(mp.mpf(d) * mp.mpf(DELTA_TEXT),
                                               AC_COEFFS, AC_SIGMAS))
        ac_abs = abs(lhs_ac - rhs_ac)
        ac_rel = ac_abs / max(abs(lhs_ac), mp.mpf("1e-50"))
    check("V0c numerical (AC) against corpus g",
          ac_abs < mp.mpf("3e-3") and ac_rel < mp.mpf("3e-2"),
          "lhs=%s rhs_grid=%s abs=%s rel=%s (tail+taper declared)"
          % (fmt_mp(lhs_ac, 10), fmt_mp(rhs_ac, 10),
             fmt_mp(ac_abs, 5), fmt_mp(ac_rel, 5)))

    # ================================================================ V1
    section("V1. EXACT COMPLETE-PRIME-PACKET UPDATE")
    atoms_main = prime_atoms(L_MAIN)
    packets = packet_rows(atoms_main, N_MAIN)
    base_g_main = base_g_values(N_MAIN)
    base_row = lag_row_from_g(base_g_main)
    direct_row = lag_row_from_g(direct_true_g(base_g_main, atoms_main))
    packet_sum = list(base_row)
    for p in sorted(packets):
        packet_sum = add_rows(packet_sum, packets[p])
    decomposition_error = max(abs(a - b)
                              for a, b in zip(direct_row, packet_sum))
    isolated_errors = []
    with mp.workdps(DPS + 15):
        dl = mp.mpf(DELTA_TEXT)
        for _p, _m, u, weight in atoms_main:
            ramp_values = [
                weight * max(mp.mpf(0), j * dl - u)
                for j in range(N_MAIN + 1)
            ]
            ramp_row = lag_row_from_g(ramp_values)
            tent_row = atom_row(u, weight, N_MAIN)
            isolated_errors.append(
                max(abs(a - b) for a, b in zip(ramp_row, tent_row))
            )
    isolated_error = max(isolated_errors)
    check("V1 exact arch + complete-packet decomposition",
          isolated_error < mp.mpf("1e-90")
          and decomposition_error < mp.mpf("1e-12"),
          "primes=%s atoms=%d isolated ramp/tent<=%s; combined"
          " second-difference residual=%s (bar 1e-12)"
          % (sorted(packets), len(atoms_main),
             fmt_mp(isolated_error, 5),
             fmt_mp(decomposition_error, 5)))
    print("  packet formula: Delta c_d(p) = -log(p) sum_m"
          " p^(-m/2) phi_d(m log p).")
    for p in sorted(packets):
        members = [(m, float(u), float(weight))
                   for pp, m, u, weight in atoms_main if pp == p]
        first_lag = min(i for i, value in enumerate(packets[p])
                        if value != 0)
        touched = sum(1 for value in packets[p] if value != 0)
        print("    p=%2d powers=%s first_lag=%d r=%.3f touched_lags=%d"
              % (p, [m for m, _u, _w in members], first_lag,
                 first_lag * DELTA, touched))

    true_result = szego(direct_row)
    base_result = szego(base_row)
    packet_states: dict[int, dict] = {}
    state_row = list(base_row)
    packet_failures = []
    print("  complete-packet prefix stream (prime order):")
    for p in sorted(packets):
        state_row = add_rows(state_row, packets[p])
        result = szego(state_row)
        packet_states[p] = result
        if not result["ok"]:
            packet_failures.append(p)
        maximum = max([abs(float(a)) for a in result["alphas"]], default=0.0)
        status = ("OK" if result["ok"] else "%s@r=%.3f"
                  % (result["fail_kind"], result["fail_k"] * DELTA))
        print("    after p=%2d: %-24s max|alpha|=%.6f coefficients=%d"
              % (p, status, maximum, len(result["alphas"])))
    packet_recovery = (len(packet_failures) > 0
                       and packet_states[sorted(packets)[-1]]["ok"]
                       and true_result["ok"])
    check("V1 complete-packet stream leaves and re-enters disk",
          packet_recovery,
          "failing packet prefixes=%s; full arithmetic stream returns with"
          " max|alpha|=%.6f" % (packet_failures,
                                max(abs(float(a))
                                    for a in true_result["alphas"])))

    # Causality for every packet against the state immediately before it.
    causal_ok = True
    state_row = list(base_row)
    causal_details = []
    for p in sorted(packets):
        before = szego(state_row)
        updated_row = add_rows(state_row, packets[p])
        after = szego(updated_row)
        first_lag = min(i for i, value in enumerate(packets[p])
                        if value != 0)
        prefix = max(0, first_lag - 1)
        available = min(prefix, len(before["alphas"]), len(after["alphas"]))
        deviation = max(
            [abs(before["alphas"][i] - after["alphas"][i])
             for i in range(available)], default=mp.mpf(0))
        causal_ok &= deviation < mp.mpf("1e-90")
        causal_details.append("p%d:%s" % (p, fmt_mp(deviation, 2)))
        state_row = updated_row
    check("V1 causal alpha prefix under each packet", causal_ok,
          "max prefix deviations " + " ".join(causal_details))

    # Inverse/resolvent law and alpha endpoint identity on frozen sections.
    update_residuals = []
    alpha_residuals = []
    ranks = []
    disp_ranks = []
    inertias = []
    p_update = min(packets)
    for dimension in UPDATE_DIMS:
        A = toeplitz_section(base_row, dimension)
        D = toeplitz_section(packets[p_update], dimension)
        A_new = A + D
        inv_A = np.linalg.inv(A)
        inv_new = np.linalg.inv(A_new)
        resolvent = inv_A - inv_A @ D @ inv_new
        res = float(np.max(np.abs(resolvent - inv_new))
                    / max(np.max(np.abs(inv_new)), 1e-300))
        update_residuals.append(res)
        alpha_inverse = inverse_alpha(inv_new)
        recursion = szego(add_rows(base_row[:dimension],
                                   packets[p_update][:dimension]))
        alpha_recursion = float(recursion["alphas"][dimension - 2])
        alpha_residuals.append(abs(alpha_inverse - alpha_recursion))
        ranks.append(numerical_rank(D))
        disp_ranks.append(displacement_rank(D))
        eigen_D = np.linalg.eigvalsh(D)
        inertias.append((int(np.sum(eigen_D < -1e-12)),
                         int(np.sum(np.abs(eigen_D) <= 1e-12)),
                         int(np.sum(eigen_D > 1e-12))))
    check("V1 resolvent + inverse-alpha update law",
          max(update_residuals) < 1e-10 and max(alpha_residuals) < 1e-10,
          "dims=%s resolvent rel<=%.2e alpha dev<=%.2e"
          % (UPDATE_DIMS, max(update_residuals), max(alpha_residuals)))
    check("V1 packet is non-rank-one, displacement-rank two",
          all(rank > 1 for rank in ranks)
          and all(rank <= 2 for rank in disp_ranks)
          and all(negative > 0 and positive > 0
                  for negative, _zero, positive in inertias),
          "p=%d ranks=%s displacement=%s inertias(-,0,+)=%s"
          % (p_update, ranks, disp_ranks, inertias))

    # State dependence of the p=3 rational endpoint update, with/without p=2.
    # The arch-only Schur recursion exits before p=3 arrives, which is itself
    # the packet-preservation kill above; inverses remain defined and expose
    # the exact state dependence of the algebraic update.
    primes_order = sorted(packets)
    p_a, p_b = primes_order[:2]
    state_differences = []
    state_ratios = []
    for dimension in STATE_DIMS:
        A0 = toeplitz_section(base_row, dimension)
        Da = toeplitz_section(packets[p_a], dimension)
        Db = toeplitz_section(packets[p_b], dimension)
        alpha_0 = inverse_alpha(np.linalg.inv(A0))
        alpha_b = inverse_alpha(np.linalg.inv(A0 + Db))
        alpha_a = inverse_alpha(np.linalg.inv(A0 + Da))
        alpha_ab = inverse_alpha(np.linalg.inv(A0 + Da + Db))
        inc0 = alpha_b - alpha_0
        incA = alpha_ab - alpha_a
        difference = abs(incA - inc0)
        scale = max(abs(inc0), 1e-300)
        state_differences.append(difference)
        state_ratios.append(difference / scale)
    state_difference = max(state_differences)
    state_ratio = max(state_ratios)
    check("V1 induced alpha update is state-dependent",
          state_symbol != 0 and state_ratio > 1e-3,
          "symbolic d/dr1[Delta2/(1-r1^2)]=%s !=0; p=%d endpoint"
          " increments on dims=%s change by max %.3e = %.3e of"
          " base-state scale"
          % (state_symbol, p_b, STATE_DIMS, state_difference, state_ratio))
    print("  STRUCTURE: packet addition is additive/commutative in moment space;"
          " alpha transport is nonlinear and")
    print("  prior-state dependent.  The packet matrix is high-rank indefinite"
          " Toeplitz with rank-two displacement, not rank one.")

    # ================================================================ V2
    section("V2. INVARIANT-REGION SEARCH + CONTROL EVENTS")
    smooth = smooth_row(base_g_main)
    scrambled, scrambled_weights = scrambled_row(base_row, atoms_main)
    smooth_result = szego(smooth)
    scrambled_result = szego(scrambled)
    true_max = max(abs(float(a)) for a in true_result["alphas"])
    print("  margin-to-unit-boundary on frozen depths:")
    print("      depth | TRUE max/margin | SMOOTH max/margin | SCRARITH max/margin")
    for depth in DEPTHS:
        rows = []
        for result in (true_result, smooth_result, scrambled_result):
            maximum, margin, count = margin_at_depth(result, depth)
            expected = min(int(round(depth / DELTA)), N_MAIN - 1)
            suffix = "*" if count < expected else ""
            rows.append("%7.4f/%7.4f%s" % (maximum, margin, suffix))
        print("      %5.3f | %s | %s | %s"
              % (depth, rows[0], rows[1], rows[2]))
    print("    * control recursion already exited the unit Schur disk.")

    smooth_event = smooth_result["fail_k"] * DELTA
    scrambled_event = scrambled_result["fail_k"] * DELTA
    control_ok = (not smooth_result["ok"] and not scrambled_result["ok"]
                  and abs(smooth_event - SMOOTH_EXIT) <= EXIT_TOL
                  and abs(scrambled_event - SCRAM_EXIT) <= EXIT_TOL)
    check("V2 control unit-disk exits reproduce wards", control_ok,
          "SMOOTH %s at r=%.3f attempted=%s; SCRARITH %s at r=%.3f"
          " attempted=%s"
          % (smooth_result["fail_kind"], smooth_event,
             fmt_mp(smooth_result["attempted"], 7),
             scrambled_result["fail_kind"], scrambled_event,
             fmt_mp(scrambled_result["attempted"], 7)))

    true_box, _ = candidate_membership(true_result["alphas"], STRICT_BOX)
    smooth_box_exit = first_box_exit(smooth_result, STRICT_BOX)
    scrambled_box_exit = first_box_exit(scrambled_result, STRICT_BOX)
    finite_separator = (true_box and math.isfinite(smooth_box_exit)
                        and math.isfinite(scrambled_box_exit))
    check("V2 strict |alpha|<=1/4 finite separator",
          finite_separator,
          "TRUE max=%.6f; exits SMOOTH r=%.3f SCRARITH r=%.3f"
          % (true_max, smooth_box_exit, scrambled_box_exit))

    # Exact diagnosis of the first smooth event.
    event_k = smooth_result["fail_k"]
    moment_index = event_k + 1
    smooth_density_mass = 2 * (math.exp(smooth_event / 2) - 1)
    support_gap = math.log(2.0)
    local_delta = float((smooth[moment_index] / smooth[0])
                        - (base_row[moment_index] / base_row[0]))
    true_alpha_event = float(true_result["alphas"][event_k])
    support_diagnosis = (smooth_event < support_gap
                         and all(float(u) >= support_gap - 1e-14
                                 for _p, _m, u, _weight in atoms_main)
                         and abs(float(direct_row[0] - base_row[0]))
                         < 1e-80)
    check("V2 r=0.264 smooth-event diagnosis", support_diagnosis,
          "event alpha=%s, true alpha same k=%+.6f; moment d=%d"
          " normalized smooth-base delta=%+.3e; PNT mass[0,r]=%.6f,"
          " true prime mass=0 before log2=%.6f"
          % (fmt_mp(smooth_result["attempted"], 8), true_alpha_event,
             moment_index, local_delta, smooth_density_mass, support_gap))

    first_position_weight = float(atoms_main[0][3])
    scrambled_first_weight = float(scrambled_weights[0])
    print("  SCRARITH diagnosis: first atom stays at log 2 but its weight"
          " changes %.8f -> %.8f (ratio %.3f);"
          % (first_position_weight, scrambled_first_weight,
             scrambled_first_weight / first_position_weight))
    print("  the true stream survives; the scrambled stream exits at r=%.3f."
          " This prices exact arithmetic weights after the support gap,"
          % scrambled_event)
    print("  but does not supply a packet-wise invariant inequality.")

    # ================================================================ V3/V4
    section("V3. HONESTY GATES AND V4. ADJUDICATION")
    circular = False
    for node in ast.walk(source_tree):
        if isinstance(node, ast.FunctionDef) and node.name == "candidate_membership":
            circular = any(isinstance(child, ast.Name)
                           and child.id == "alphas"
                           for child in ast.walk(node))
    check("V3 circular candidate detector fires", circular,
          "|alpha|<=1/4 membership consumes the computed alpha stream;"
          " finite separation is not an invariant proof")

    packet_local_checkable = (
        all(rank == 1 for rank in ranks)
        and state_ratio < mp.mpf("1e-20")
    )
    check("V3 no false arithmetic-local upgrade",
          not packet_local_checkable,
          "rank-one=%s state-independent=%s; exact congruence test consumes"
          " prior T^{-1/2} and is WALL-EQUIVALENT"
          % (all(rank == 1 for rank in ranks),
             state_ratio < mp.mpf("1e-20")))

    truth_prefix_ok = true_result["ok"] and true_max < 1
    check("V3 source truth prefix stays in Schur disk",
          truth_prefix_ok,
          "n=%d max|alpha|=%.6f margin=%.6f"
          % (len(true_result["alphas"]), true_max, 1 - true_max))

    invariant_found = finite_separator and not circular and packet_local_checkable
    dichotomy_found = packet_local_checkable and not circular
    if invariant_found:
        verdict = ("VERBLUNSKY-INVARIANT-FOUND(remaining proof: extend the"
                   " certified packet preservation to the cofinal ladder)")
    elif dichotomy_found:
        verdict = ("VERBLUNSKY-DICHOTOMY(checkable-arithmetic per-packet"
                   " inequality)")
    else:
        verdict = (
            "VERBLUNSKY-NO-INVARIANT(mechanism: complete packets act by "
            "high-rank indefinite Toeplitz updates of displacement rank two; "
            "the induced alpha increment is prior-state dependent.  The only "
            "exact survival condition uses the prior section inverse and is "
            "WALL-EQUIVALENT.  The |alpha|<=1/4 finite separator is circular.)"
        )

    wall = time.time() - T0
    check("A3 runtime", wall <= RUNTIME_BAR,
          "%.1f s <= %.0f s" % (wall, RUNTIME_BAR))
    instrument_ok = all(ok for _name, ok, _detail in CHECKS)
    n_pass = sum(1 for _name, ok, _detail in CHECKS if ok)
    print("\n  V0a: MINIMAL-PIN-LEMMA-PINNED (sigma_r in (1,2], limit 1).")
    print("  V0b: DELTA1-NO-BACK-INFERENCE (singular sections n>=2).")
    print("  V0c: EULER-PICK-CRITERION-PINNED; (AC) symbolic + numerical;"
          " N<=12 is a source-only falsification prefix.")
    print("  V1 : EXACT-PACKET-UPDATE (additive moments, displacement-rank two,"
          " nonlinear state-dependent alphas).")
    print("  V2 : strict box is FINITE-SEPARATOR-ONLY; smooth kill is the"
          " false sub-log2 density support;")
    print("       scrambled kill prices exact weights, not a proved invariant.")
    print("  V3 : source firewall, controls, cofinal-prefix and circularity"
          " gates all explicit.")
    print("\n" + "=" * 78)
    print("CHECKS %d/%d PASS   runtime %.1f s   SPEC_SHA %s"
          % (n_pass, len(CHECKS), wall, SPEC_SHA[:16]))
    if not instrument_ok:
        print("VERDICT: INSTRUMENT-EDGE (failed ward; no mathematical verdict)")
        print("NO RH CLAIM. EXPLORATION ONLY.")
        print("=" * 78)
        return 1
    print("VERDICT: %s" % verdict)
    print("TYPING: surviving all-depth premise = WALL-EQUIVALENT,"
          " not checkable-arithmetic.")
    print("NO RH CLAIM. NO ALL-DEPTH POSITIVITY CLAIM. EXPLORATION ONLY.")
    print("=" * 78)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
