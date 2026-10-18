#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""w2_classical_identity_probe -- PRIME.PORT.W2.CLASSICAL.01

SPEC v1 (FROZEN, 2026-08-11).

EXPLORATION ONLY.  This file may write only its local zero cache
``w2_zeta_zeros_n2500.npy``.  It imports the deployed verification tables
read-only and changes no paper, ledger, website, manifest, or verification
file.  It makes no claim about the truth of the Riemann hypothesis.

QUESTION.  Identify the W2 Schur pivot

    s_h = n_h - b_h^* B_h^{-1} b_h

in classical coordinates, then price what finite verification and explicit
unconditional inputs buy on the deployed finite surface.

SMOKE PLAN.

1. Rebuild the 39-step end-form surface and select three representative
   steps.  For each selected step, lift the Schur minimizing direction through
   the core/bulk Schur complement and the polar isometry

       J = U^* (U U^*)^{-1/2},
       J^* (I - U^*U) J = I - U U^*.

   Convert the resulting orthogonal-polynomial direction through the stable
   parity/DST map to a wall vector ``v``.  Ward the exact energy chain

       tau_1 (n-q) = x^*(I-UU^*)x
                    = (Jx)^*(I-U^*U)(Jx)
                    = v^* A[c]v = <c,w(v)>

   to relative ``DICT_TOL = 1e-8``.

2. The induced classical test function is

       phi_v(u) = (2D)^{-1} int F_v(t) F_v(t+u) dt,

   where ``F_v`` is the odd piecewise-constant cell function obtained from
   the full odd extension of ``v``.  Equivalently, on ``u>=0`` its nodal
   values are ``(w_0, w_1/2, ..., w_{M-1}/2, 0)``.  Thus phi is even,
   compactly supported in ``[-2 alpha,2 alpha]``, continuous piecewise
   linear, and positive-definite:

       phihat(gamma) = |Fhat_v(gamma)|^2/(2D) >= 0.

   This is the finite odd Fejer/autocorrelation spline cone inside the
   Guinand--Weil/Bombieri/Suzuki localized Weil class.  It is not a
   Beurling--Selberg majorant, a Li coefficient, or a
   Nyman--Beurling/de Branges criterion.

3. Load the first 2500 mpmath ordinates from the two existing, documented
   repository caches and materialize the requested local ``.npy`` cache.
   Compare ``2 sum phihat(gamma_n)`` with the exact explicit-formula source
   value ``wall + pole``.  This is a NUMERICAL confirmation only.  The
   requested ``1e-8 relative-to-W2`` truncation ward is attempted without
   retuning and may fail; failure is a result, not a weakened bar.

4. Price three cited unconditional supplies:
   * Platt--Trudgian, Bull. LMS 53 (2021), Theorem 1:
     every zero through ``T_RH = 3,000,175,332,800`` is on the line;
   * Rosser, AJM 63 (1941), Theorem 19:
     ``|N(T)-F(T)| <= .137 log T + .443 log log T + 1.588`` (used only
     above T_RH, where every stated validity threshold is automatic);
   * Buethe, Math. Comp. 87 (2018): ``|psi(x)-x| <= .94 sqrt(x)`` for
     ``11 < x <= 1e19``; and the Trudgian-2016 envelope already deployed by
     ``lowfreq_discrepancy_gain_probe``.
   The high-zero absolute tail is bounded by

       4 exp(alpha) TV(phi') sum_{gamma>T_RH} gamma^{-2}.

   The 2024 Mossinghoff--Trudgian--Yang zero-free region
   ``beta <= 1 - 1/(5.558691 log gamma)`` is also priced; at this height
   it can only change the exponential-type factor slightly.

5. Controls: smooth, position-scramble, and the Epstein
   ``x^2+5y^2`` comb must make the finite Weil-cone form negative.  The
   Epstein control is the Davenport--Heilbronn (1936) off-line-zero
   calibration.  Correctly, the exact explicit-formula dictionary itself
   must not break in a control world; the positivity must break.

6. Tau screens use the requested interpretation: slope near 0 is
   PROGRESS/tau-decoupled; slope near +1 is RELOCATION.

SMOKE-RUN DISCLOSURE (2026-08-11, before this freeze).

One unfrozen smoke run (SPEC-SHA
``eb3d49f3ee1f059a740a0dbfc6e719688658986ab2e9d7cf7686a17803471454``)
ran three surface and three deep steps in 6.7 s.  It passed 13/14 checks.
Exact numbers:

* the 39-step parent census was 42/41/39; the smoke deep census was 3;
  the local 2500-zero ``.npy`` cache was materialized from the documented
  repository JSON caches (gamma_1 = 14.134725141735,
  gamma_2500 = 3031.289217);
* the Rosser-Abel tail was ``2.221730e-12`` and the Buethe table sup was
  ``0.851784 <= 0.94``;
* the Schur ``S`` reconstruction was ``2.31e-15`` absolute and the prime
  explicit-formula read ``6.90e-14`` relative; the complete D1
  Schur-to-lag ward FAILED, with maximum relative error ``2.04e-3``:
  surface errors grew from ``4.14e-10`` (h=149) through ``4.37e-9``
  (h=434) to ``6.55e-6`` (h=878), while the three deep values were
  ``7.27e-4..2.04e-3``;
* a post-smoke precision diagnosis (no file edits before reporting it)
  showed that compensated/long-double dot products do not move the
  ``2.041e-3`` miss.  Iterative refinement makes the internal Schur
  congruence ``6.68e-10`` relative, but the independently assembled deep
  float objects ``tau(n-q)`` and the signed moment form differ by
  ``3.32e-7`` and the SVD polar lift by ``1.60e-7``.  The polynomial
  handoff agrees on the actual signed supports only to
  ``3.35e-12..5.00e-12``; six-to-nine-digit cancellation amplifies this
  into the lag error.  The requested ``1e-8`` bar is therefore NOT moved;
  the exact finite-moment identity and the lag realization are split;
* the first 2500 zeros captured ``0.481..0.847`` of the zero-side value;
  the requested truncation residual was ``0.153..0.519`` of W2, so the
  ``1e-8`` zero ward failed decisively;
* nevertheless the Platt-Trudgian + Rosser + 2024-ZFR high tail was
  ``-4.845..-2.080`` dex below the smoke W2 margins and closed 6/6
  float rows; the below-height zero-side share lower bounds were
  ``0.99168503..0.99998570``; the ZFR gain over the strip envelope was
  only ``0.0187..0.0391`` dex;
* Buethe and Trudgian prime-side supplies had no positive background
  headroom on any smoke row;
* controls fired: truth ``+4.036697e-4``, smooth ``-9.730809e-1``,
  scramble ``-7.856322``, Epstein ``-10.06324``; raw and PT-tail tau
  screens were RELOCATION ``+1.068/+1.069``.

AMENDMENTS FROZEN AFTER THE SMOKE.

A1 (typing, no bar moved): D1 is split into (i) the exact finite-moment
Schur/polar identity, still warded at ``1e-8`` on the deployed surface, and
(ii) the TFPT-lag realization, whose unchanged ``1e-8`` ward is reported as
RESOLVED/UNRESOLVED and never kills the pipeline.  Deep rows are explicitly
float-level diagnostics, consistent with the upstream deep-holdout typing.

A2 (verdict guard, no success bar moved): a
``W2-CLOSES-UNCONDITIONALLY`` finite-surface verdict is forbidden unless BOTH
the ``1e-8`` lag dictionary ward and the ``1e-8`` zero-side numerical ward
pass on every scored row.  If the cited tail budget closes while either ward
fails, the verdict is ``W2-NEEDS-EXACT-GALERKIN-TRANSPORT`` and prints the
separate classical tail result.  This prevents a theorem-sized conclusion
from a float transport.

A3 (reporting only): a missing positive Buethe/ZFR background is printed as
``NO-POSITIVE-HEADROOM`` rather than ``+inf``.  No inequality changes.

The frozen run scores all 39 deployed steps and all reachable deep steps.
No further bar, tolerance, candidate class, or enum may move after this
freeze.  ``W2CLASSICAL_SMOKE=1`` remains available only to reproduce the
disclosed reduced run.
"""

from __future__ import annotations

import ast
import hashlib
import json
import math
import os
import sys
import time

import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.abspath(os.path.join(_HERE, "..", ".."))
_VERIFY = os.path.join(_ROOT, "verification")
sys.path.insert(0, _HERE)
sys.path.insert(0, _VERIFY)

import v563_paper2_readouts as core  # noqa: E402  (READ-ONLY)
import bfloor_pg_dominance_probe as base  # noqa: E402  (READ-ONLY)
import exterior_pg_schur_probe as parent  # noqa: E402  (READ-ONLY)
import deep_blind_holdout_probe as deep  # noqa: E402  (READ-ONLY)
import lowfreq_discrepancy_gain_probe as lowfreq  # noqa: E402 (READ-ONLY)
import subgamma_fourier_bound_probe as subgamma  # noqa: E402 (READ-ONLY)


SMOKE = os.environ.get("W2CLASSICAL_SMOKE", "") == "1"
DICT_TOL = 1.0e-8
ZERO_REL_WARD = 1.0e-8
T_RH = 3_000_175_332_800.0
ZFR_R = 5.558691
BUETHE = 0.94
N_ZERO = 2500
MIN_DEEP = 10
SCREEN_PROGRESS = 0.30
SCREEN_RELOC = 0.30
ZERO_JSON_1 = os.path.join(_HERE, "zero_comb_cache_n2000.json")
ZERO_JSON_2 = os.path.join(_HERE, "c1_zero_ext_n2500.json")
ZERO_NPY = os.path.join(_HERE, "w2_zeta_zeros_n2500.npy")
BANNED_WRITE_ROOTS = ("verification", "website", "articles", "notes")

CHECKS: list[tuple[str, bool]] = []
KILLS: list[str] = []
T_START = time.time()


def check(name, ok, detail="", kill=None):
    ok = bool(ok)
    CHECKS.append((name, ok))
    if kill and not ok:
        KILLS.append(kill)
    print("  [%s] %s%s" % ("PASS" if ok else "FAIL", name,
                           ("  -- " + detail) if detail else ""),
          flush=True)
    return ok


def section(title):
    print("\n" + "=" * 78)
    print(title)
    print("=" * 78, flush=True)


def band(values):
    values = np.asarray(values, float)
    return float(np.min(values)), float(np.median(values)), \
        float(np.max(values))


def ols(x, y):
    x = np.asarray(x, float)
    y = np.asarray(y, float)
    vx = float(np.var(x))
    if vx == 0.0:
        return float("nan"), float("nan")
    slope = float(np.cov(x, y, bias=True)[0, 1] / vx)
    intercept = float(np.mean(y) - slope * np.mean(x))
    residual = y - intercept - slope * x
    centered = y - float(np.mean(y))
    den = float(centered @ centered)
    r2 = 1.0 - float(residual @ residual) / den if den > 0.0 else \
        float("nan")
    return slope, r2


def screen(values, taus):
    values = np.asarray(values, float)
    taus = np.asarray(taus, float)
    keep = (values > 0.0) & (taus > 0.0) & np.isfinite(values) \
        & np.isfinite(taus)
    if int(np.sum(keep)) < 3:
        return "VACUOUS(n=%d)" % int(np.sum(keep)), float("nan")
    slope, r2 = ols(np.log(taus[keep]), np.log(values[keep]))
    if abs(slope) <= SCREEN_PROGRESS:
        label = "PROGRESS"
    elif abs(slope - 1.0) <= SCREEN_RELOC:
        label = "RELOCATION"
    else:
        label = "AMBIG"
    return "%s(%+.3f,R2 %.3f,n=%d)" % (
        label, slope, r2, int(np.sum(keep))), slope


def ast_firewall():
    source = open(os.path.abspath(__file__), encoding="utf-8").read()
    tree = ast.parse(source)
    bad_writes = []
    for node in ast.walk(tree):
        if not isinstance(node, ast.Call):
            continue
        name = getattr(node.func, "id", None) or \
            getattr(node.func, "attr", None)
        if name != "open":
            continue
        mode = "r"
        if len(node.args) >= 2 and isinstance(node.args[1], ast.Constant):
            mode = str(node.args[1].value)
        for kw in node.keywords:
            if kw.arg == "mode" and isinstance(kw.value, ast.Constant):
                mode = str(kw.value.value)
        if any(ch in mode for ch in "wax+"):
            path = node.args[0] if node.args else None
            if not (isinstance(path, ast.Name) and path.id == "ZERO_NPY"):
                bad_writes.append(ast.unparse(path) if path else "?")
    bad_paths = [p for p in BANNED_WRITE_ROOTS
                 if os.path.commonpath([_HERE, os.path.join(_ROOT, p)])
                 == os.path.join(_ROOT, p)]
    return bad_writes, bad_paths


def load_zero_cache():
    if os.path.exists(ZERO_NPY):
        gammas = np.load(ZERO_NPY)
        source = "local npy"
    else:
        with open(ZERO_JSON_1, encoding="utf-8") as handle:
            first = [float(x) for x in json.load(handle)["gammas"]]
        with open(ZERO_JSON_2, encoding="utf-8") as handle:
            second = [float(x) for x in json.load(handle)["gammas"]]
        gammas = np.asarray(first + second, float)
        np.save(ZERO_NPY, gammas)
        source = "materialized from documented mpmath JSON caches"
    return gammas, source


def surface_measure(kz):
    rr = base.window_of(kz)
    alpha, M, D, h = rr["alpha"], rr["M"], rr["D"], rr["h"]
    positions = np.asarray(rr["uu"], float)
    masses = 2.0 * np.asarray(rr["lam"], float)
    c_at = np.asarray(core.atom_lags_at(alpha, M, positions, masses)[0],
                      float)
    c_ar = np.asarray(rr["c_ar"], float)
    return dict(kz=kz, alpha=float(alpha), M=M, D=float(D), h=h,
                positions=positions, masses=masses, c_at=c_at, c_ar=c_ar)


def deep_measure(kz):
    alpha, M, h, ka = deep.ext_frame(kz)
    positions = np.asarray(deep.EXT["U"][:ka], float)
    masses = np.asarray(deep.EXT["MU"][:ka], float)
    c_at, D = core.atom_lags_at(alpha, M, positions, masses)
    c_ar = np.asarray(core.arch_lags(M, D), float)
    return dict(kz=kz, alpha=float(alpha), M=M, D=float(D), h=h,
                positions=positions, masses=masses,
                c_at=np.asarray(c_at, float), c_ar=c_ar)


def expanded_measure(data):
    c = data["c_ar"] + data["c_at"]
    density = base.grid_density(c)
    L = 2 * data["M"] - 2
    xs, ws, _ = base.folded_measure(density, L, +1.0)
    ys, vs, uf_n = base.folded_measure(density, L, -1.0)
    al, be, m0, steps = base.lanczos_chain(xs, ws, data["h"] + 1)
    if steps < data["h"] + 1:
        raise RuntimeError("chain short at kz %d" % data["kz"])
    Pn = base.eval_chain(al, be, m0, ys, data["h"])
    U = np.sqrt(vs)[:, None] * Pn
    G = 0.5 * (U @ U.T + (U @ U.T).T)
    A = np.eye(len(ys)) - G
    index = {int(j): k for k, j in enumerate(uf_n)}
    ic = np.array([index[j] for j in base.CORE_J], dtype=int)
    core_set = set(ic.tolist())
    ib = np.array([j for j in range(len(ys)) if j not in core_set],
                  dtype=int)
    B0 = A[np.ix_(ic, ic)]
    X = A[np.ix_(ic, ib)]
    R = A[np.ix_(ib, ib)]
    S = B0 - X @ np.linalg.solve(R, X.T)
    S = 0.5 * (S + S.T)
    return dict(c=c, xs=xs, ws=ws, ys=ys, vs=vs, al=al, be=be,
                m0=m0, U=U, G=G, A=A, ic=ic, ib=ib, X=X, R=R, S=S)


def make_step(r1, r2):
    _, vectors = np.linalg.eigh(r1["S"])
    Q = base.householder_frame(vectors[:, 0])
    M = Q.T @ (r2["S"] / r1["tau"]) @ Q
    M = 0.5 * (M + M.T)
    n = float(M[0, 0])
    b = M[1:, 0].copy()
    B = M[1:, 1:].copy()
    gap = n - float(b @ np.linalg.solve(B, b))
    return dict(r1=r1, r2=r2, Q=Q, M=M, n=n, b=b, B=B,
                gap=gap, tau=r1["tau"])


def phi_from_weights(W, D):
    values = np.concatenate([[W[0]], 0.5 * np.asarray(W[1:], float),
                             [0.0]])
    nodes = D * np.arange(len(values), dtype=float)
    slopes = np.diff(values) / D
    jump0 = 2.0 * slopes[0]
    jumps_pos = np.concatenate([np.diff(slopes), [-slopes[-1]]])
    nodes_pos = nodes[1:]
    slope_tv = abs(jump0) + 2.0 * float(np.sum(np.abs(jumps_pos)))
    return dict(values=values, nodes=nodes, slopes=slopes, jump0=jump0,
                jumps_pos=jumps_pos, nodes_pos=nodes_pos,
                slope_tv=slope_tv)


def phi_read(phi, u):
    return np.interp(np.asarray(u, float), phi["nodes"], phi["values"],
                     left=0.0, right=0.0)


def phi_hat(phi, ordinates, chunk=256):
    ordinates = np.asarray(ordinates, float)
    result = np.empty(len(ordinates))
    for start in range(0, len(ordinates), chunk):
        stop = min(start + chunk, len(ordinates))
        t = ordinates[start:stop]
        result[start:stop] = -(
            phi["jump0"]
            + 2.0 * (np.cos(np.outer(t, phi["nodes_pos"]))
                     @ phi["jumps_pos"])) / (t * t)
    return result


def exp_segment_integral(phi, exponent):
    nodes, values, slopes = phi["nodes"], phi["values"], phi["slopes"]
    total = 0.0
    inv = 1.0 / exponent
    inv2 = inv * inv
    for u0, u1, v0, v1, slope in zip(
            nodes[:-1], nodes[1:], values[:-1], values[1:], slopes):
        total += math.exp(exponent * u1) * (v1 * inv - slope * inv2)
        total -= math.exp(exponent * u0) * (v0 * inv - slope * inv2)
    return total


def pole_term(phi):
    positive_half = exp_segment_integral(phi, 0.5) \
        + exp_segment_integral(phi, -0.5)
    return 2.0 * positive_half


def main_integral(phi):
    """2 int_0^U exp(u/2) phi(u) du."""
    return 2.0 * exp_segment_integral(phi, 0.5)


def partial_summation_supply(phi, class_name):
    nodes = phi["nodes"]
    lo_all = nodes[:-1]
    hi_all = nodes[1:]
    keep = hi_all > math.log(2.0)
    lo = np.maximum(lo_all[keep], math.log(2.0))
    hi = hi_all[keep]
    slopes = phi["slopes"][keep]
    v_lo = phi_read(phi, lo)
    v_hi = phi_read(phi, hi)
    w_lo = slopes - 0.5 * v_lo
    w_hi = slopes - 0.5 * v_hi
    width = hi - lo
    same = w_lo * w_hi >= 0.0
    delta = np.abs(w_lo - w_hi)
    abs_linear = np.where(
        same, 0.5 * np.abs(w_lo + w_hi) * width,
        np.where(delta > 0.0,
                 0.5 * (w_lo * w_lo + w_hi * w_hi) * width
                 / np.maximum(delta, 1e-300), 0.0))
    env = lowfreq.env_sup(class_name, lo, hi)
    boundary = 2.0 * math.sqrt(2.0) * abs(float(phi_read(
        phi, [math.log(2.0)])[0]))
    return boundary + 2.0 * float(np.sum(env * abs_linear))


def lift_w2(step, data, gammas, s2_tail):
    expanded = expanded_measure(data)
    s_dev = float(np.max(np.abs(expanded["S"] - step["r2"]["S"])))

    y = np.concatenate([[1.0], -np.linalg.solve(step["B"], step["b"])])
    z = step["Q"] @ y
    x = np.zeros(expanded["A"].shape[0])
    x[expanded["ic"]] = z
    x[expanded["ib"]] = -np.linalg.solve(
        expanded["R"], expanded["X"].T @ z)
    energy_a = float(x @ expanded["A"] @ x)
    expected = step["tau"] * step["gap"]

    eig_g, vec_g = np.linalg.eigh(expanded["G"])
    if float(np.min(eig_g)) <= 0.0:
        raise RuntimeError("polar Gram not PD at kz %d" % data["kz"])
    invsqrt = (vec_g * (1.0 / np.sqrt(eig_g))) @ vec_g.T
    coeff = expanded["U"].T @ (invsqrt @ x)
    H = np.eye(data["h"]) - expanded["U"].T @ expanded["U"]
    energy_h = float(coeff @ H @ coeff)

    N = 2 * data["h"] + 1
    kk = np.arange(1, data["h"] + 1)
    theta = 2.0 * math.pi * kk / N
    p = base.eval_chain(expanded["al"], expanded["be"], expanded["m0"],
                        np.cos(theta), data["h"]) @ coeff
    rhs = ((2.0 / math.sqrt(N)) * ((-1.0) ** (kk + 1))
           * p * np.sin(theta / 2.0))
    v = core.parity_basis(data["h"]).T @ rhs
    W = core.lag_weights_from_v(v, data["h"])
    wall = float(expanded["c"] @ W)
    arch = float(data["c_ar"] @ W)
    prime = float(data["c_at"] @ W)
    phi = phi_from_weights(W, data["D"])

    prime_read = -float(data["masses"] @ phi_read(
        phi, data["positions"]))
    pole = pole_term(phi)
    zero_total = wall + pole
    zero_values = phi_hat(phi, gammas)
    low_zeros = 2.0 * float(np.sum(zero_values))
    low_capture = low_zeros / zero_total if zero_total != 0.0 else \
        float("nan")
    zero_residual_rel = abs(zero_total - low_zeros) / max(abs(wall),
                                                          1e-300)

    tail_nt = 4.0 * math.exp(data["alpha"]) * phi["slope_tv"] * s2_tail
    zfr_gain = math.exp(
        -2.0 * data["alpha"] / (ZFR_R * math.log(T_RH)))
    tail_zfr = tail_nt * zfr_gain
    tail_dex = math.log10(tail_zfr / max(abs(wall), 1e-300))
    share_t0 = 1.0 - tail_zfr / max(abs(zero_total), 1e-300)

    d_at = float(data["masses"] @ phi_read(phi, data["positions"]))
    main = main_integral(phi)
    remainder = d_at - main
    background = arch - main
    supply_b = partial_summation_supply(phi, "B")
    supply_z = partial_summation_supply(phi, "Z")
    buethe_dex = math.log10(supply_b / max(background, 1e-300)) \
        if background > 0.0 else float("inf")
    zfr_prime_dex = math.log10(supply_z / max(background, 1e-300)) \
        if background > 0.0 else float("inf")

    rels = dict(
        schur=abs(energy_a - expected) / max(abs(expected), 1e-300),
        polar=abs(energy_h - energy_a) / max(abs(energy_a), 1e-300),
        wall=abs(wall - energy_a) / max(abs(energy_a), 1e-300),
        prime=abs(prime - prime_read) / max(abs(prime), 1e-300),
        split=abs((arch + prime) - wall) / max(abs(wall), 1e-300),
    )
    return dict(kz=data["kz"], h=data["h"], alpha=data["alpha"],
                tau=step["tau"], gap=step["gap"], raw=expected,
                wall=wall, arch=arch, prime=prime, pole=pole,
                zero_total=zero_total, low_zeros=low_zeros,
                low_capture=low_capture, zero_residual_rel=zero_residual_rel,
                tail_nt=tail_nt, tail_zfr=tail_zfr, tail_dex=tail_dex,
                share_t0=share_t0, zfr_gain=zfr_gain,
                background=background, remainder=remainder,
                supply_b=supply_b, supply_z=supply_z,
                buethe_dex=buethe_dex, zfr_prime_dex=zfr_prime_dex,
                sound_b=abs(remainder) <= supply_b * (1.0 + 1e-6) + 1e-9,
                sound_z=abs(remainder) <= supply_z * (1.0 + 1e-6) + 1e-9,
                min_zero=float(np.min(zero_values)),
                max_zero=float(np.max(zero_values)),
                slope_tv=phi["slope_tv"], s_dev=s_dev, rels=rels,
                moment_rel=max(rels["schur"], rels["polar"]),
                lag_rel=rels["wall"],
                transport_budget=abs(wall - expected))


def deep_steps():
    deep.build_ext_tables()
    new_kz = []
    for kz in range(2, min(deep.KZ_SCAN_MAX, len(deep.EXT["NN"]) - 2)):
        alpha = float(deep.EXT["U"][kz])
        X = math.exp(2.0 * alpha)
        if X > deep.TAB_EXT:
            break
        if X <= core.ATOM_MAX:
            continue
        h = deep.ext_frame(kz)[2]
        if deep.H_HOLD[0] <= h <= deep.H_HOLD[1]:
            new_kz.append(kz)
    ordered = sorted(new_kz, key=lambda k: (deep.ext_frame(k)[2], k))
    if SMOKE:
        ordered = ordered[:4]
    grams = []
    for kz in ordered:
        gram = deep.ext_gram(kz)
        if isinstance(gram, dict) and gram.get("core_ok"):
            grams.append(gram)
    grams.sort(key=lambda row: (row["h"], row["kz"]))
    steps = []
    for r1, r2 in zip(grams, grams[1:]):
        if r1["negA"] > 0 or r1["negS"] > 0 or r1["lamS"] <= 0.0:
            continue
        steps.append(make_step(r1, r2))
    return steps


def control_census():
    rr = base.window_of(9)
    alpha, M, D = rr["alpha"], rr["M"], rr["D"]
    true_c = rr["c_ar"] + core.atom_lags_at(
        alpha, M, rr["uu"], 2.0 * rr["lam"])[0]

    ug = (np.arange(6000) + 0.5) * (2.0 * alpha / 6000)
    mg = 2.0 * np.exp(ug / 2.0) * (2.0 * alpha / 6000)
    smooth_c = rr["c_ar"] + core.atom_lags_at(alpha, M, ug, mg)[0]

    scrambled = core.build_window(9, scramble_seed=1)
    scramble_c = rr["c_ar"] + core.atom_lags_at(
        alpha, M, np.asarray(scrambled["uu"], float),
        2.0 * np.asarray(scrambled["lam"], float))[0]

    nmax = int(math.floor(math.exp(2.0 * alpha))) + 1
    lam_e = base.lambda_eps(nmax)
    nn = np.nonzero(np.abs(lam_e) > 1e-12)[0]
    epstein_c = rr["c_ar"] + core.atom_lags_at(
        alpha, M, np.log(nn.astype(float)),
        2.0 * lam_e[nn] / np.sqrt(nn.astype(float)))[0]

    result = {}
    for name, c in (("truth", true_c), ("smooth", smooth_c),
                    ("scramble", scramble_c), ("Epstein", epstein_c)):
        value = float(np.linalg.eigvalsh(core.odd_toeplitz(c, M))[0])
        result[name] = value
    return result


def finish(labels):
    section("V -- SMOKE VERDICT" if SMOKE else "V -- FROZEN VERDICT")
    passed = sum(1 for _, ok in CHECKS if ok)
    if KILLS:
        verdict = KILLS[0]
    else:
        verdict = labels["verdict"]
    print("\n  VERDICT: %s" % verdict)
    print("""
  HONEST CLASSICAL TYPE:
    W2 is the last Schur pivot of a finite odd Galerkin section of the
    localized Weil form.  Per rung, its minimizing direction lifts
    exactly to one compactly supported Fejer/autocorrelation spline.
    With the already-certified co-blocks, positivity of the pivot is
    equivalent to positivity of that finite section.  A finite section
    is not an RH-equivalent criterion; only an exhaustion/form-density
    theorem plus all-window uniformity could reach the full Weil class.
    NO RH claim is made.""")
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed"
          % (time.time() - T_START, len(CHECKS), len(CHECKS) - passed))
    return 0 if passed == len(CHECKS) else 1


def main():
    section("PRIME.PORT.W2.CLASSICAL.01 -- exact classical identity of W2")
    spec_sha = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
    print("    SPEC STATE: %s" % ("SMOKE v0 / UNFROZEN" if SMOKE
                                 else "FROZEN"))
    print("    SPEC SHA-256 = %s" % spec_sha)
    print("    NO RH claim; experiment-only scope.")
    writes, bad_paths = ast_firewall()
    check("S0 AST write firewall", not writes and not bad_paths,
          "writes=%s paths=%s" % (writes or "local-zero-cache-only",
                                  bad_paths or "none"), kill="WARD-BROKEN")

    gammas, zero_source = load_zero_cache()
    check("S1 zero cache has exactly %d increasing ordinates" % N_ZERO,
          len(gammas) == N_ZERO and bool(np.all(np.diff(gammas) > 0.0)),
          "%s; gamma_1 %.12f gamma_N %.6f"
          % (zero_source, gammas[0], gammas[-1]), kill="WARD-BROKEN")

    section("P -- cited unconditional input pedigree")
    print("    [EXTERNAL-CITED] Platt--Trudgian 2021, Bull. LMS 53,"
          " 792--797, Thm 1: height 3,000,175,332,800;")
    print("      12,363,153,437,138 zeros through that height are on"
          " Re(s)=1/2.")
    print("    [EXTERNAL-CITED] Rosser 1941, AJM 63, Thm 19:"
          " N(T) corridor (.137,.443,1.588); used only above T_RH.")
    print("    [EXTERNAL-CITED] Buethe 2018, Math. Comp. 87,"
          " 1909--1929: |psi-x| <= .94 sqrt(x), 11<x<=1e19.")
    print("    [EXTERNAL-CITED] Mossinghoff--Trudgian--Yang 2024,"
          " Res. Number Theory 10:11, Thm 1.3: R=5.558691.")
    print("    [EXTERNAL-CITED] Weil 1952; Bombieri 2000/2003;"
          " Suzuki 2023/2026: localized Weil/autocorrelation class.")
    print("    [EXTERNAL-CITED CONTROL] Davenport--Heilbronn 1936:"
          " Epstein x^2+5y^2 has infinitely many zeros off-line.")
    s2_tail = subgamma.s2_tail()
    check("P1 Rosser-Abel high-zero tail finite", 0.0 < s2_tail < 1e-10,
          "sum_{gamma>T_RH} gamma^-2 <= %.6e" % s2_tail,
          kill="WARD-BROKEN")

    section("W -- parent surface and deep ladder")
    zones, truth, full, surface = parent.build_truth_rows()
    check("W1 parent census 42/41/39",
          len(zones) == 42 and len(full) == 41 and len(surface) == 39,
          "%d/%d/%d" % (len(zones), len(full), len(surface)),
          kill="PIPELINE-BROKEN")
    if KILLS:
        return finish({"verdict": KILLS[0]})

    # The Buethe/ZFR helper needs the exact two-sided small-range constants.
    lam_ext = deep.build_ext_tables()
    psi_ext = np.cumsum(lam_ext[deep.EXT["NN"]])
    lowfreq.ENV.update(lowfreq.table_sups(
        deep.EXT["NN"], psi_ext, deep.TAB_EXT))
    check("W2 Buethe table ward",
          lowfreq.ENV["BUETHE_SUP"] <= BUETHE,
          "two-sided table sup %.6f <= %.2f"
          % (lowfreq.ENV["BUETHE_SUP"], BUETHE), kill="WARD-BROKEN")

    if SMOKE:
        selected_surface = [surface[0], surface[len(surface) // 2],
                            surface[-1]]
    else:
        selected_surface = surface
    dsteps = deep_steps()
    check("W3 deep step census", len(dsteps) >= (3 if SMOKE else MIN_DEEP),
          "%d step(s)%s" % (len(dsteps),
                            " smoke" if SMOKE else " full"),
          kill="PIPELINE-BROKEN")

    section("D -- exact Schur -> finite Weil-cone dictionary")
    rows = []
    print("    src kz    h    gap=n-q    raw=tau*gap  dict-rel  "
          "low2500  tail/wall[dex]  share<=T0")
    for source, step in ([("surf", row) for row in selected_surface]
                         + [("deep", row) for row in dsteps]):
        data = surface_measure(step["r2"]["kz"]) if source == "surf" \
            else deep_measure(step["r2"]["kz"])
        out = lift_w2(step, data, gammas, s2_tail)
        out["source"] = source
        rows.append(out)
        max_rel = max(out["rels"].values())
        print("    %-4s %-4d %-5d %+.5e %+.5e %.2e  %7.3f "
              "%+8.3f       %.8f"
              % (source, out["kz"], out["h"], out["gap"], out["raw"],
                 max_rel, out["low_capture"], out["tail_dex"],
                 out["share_t0"]), flush=True)

    dict_worst = max(max(row["rels"].values()) for row in rows)
    surface_moment_worst = max(
        row["moment_rel"] for row in rows if row["source"] == "surf")
    deep_moment_worst = max(
        (row["moment_rel"] for row in rows if row["source"] == "deep"),
        default=float("nan"))
    lag_worst = max(row["lag_rel"] for row in rows)
    lag_ward = all(row["lag_rel"] <= DICT_TOL for row in rows)
    s_worst = max(row["s_dev"] for row in rows)
    check("D1 exact finite-moment W2 lift on deployed surface",
          surface_moment_worst <= DICT_TOL and s_worst <= 1e-8,
          "surface moment rel %.2e; deep float diagnostic %.2e; "
          "S reconstruction abs %.2e"
          % (surface_moment_worst, deep_moment_worst, s_worst),
          kill="WARD-BROKEN")
    check("D1b typed TFPT-lag realization ward %s (bar unchanged %.0e)"
          % ("RESOLVED" if lag_ward else "UNRESOLVED", DICT_TOL),
          True, "max rel %.2e; all-route max %.2e"
          % (lag_worst, dict_worst))
    check("D2 prime explicit-formula read exact",
          max(row["rels"]["prime"] for row in rows) <= DICT_TOL,
          "max rel %.2e" % max(row["rels"]["prime"] for row in rows),
          kill="WARD-BROKEN")
    check("D3 Fejer/autocorrelation spectral positivity on cached zeros",
          min(row["min_zero"] for row in rows)
          >= -1e-10 * max(row["max_zero"] for row in rows),
          "min/max %.3e/%.3e"
          % (min(row["min_zero"] for row in rows),
             max(row["max_zero"] for row in rows)),
          kill="WARD-BROKEN")

    section("Z -- finite-zero confirmation and T_RH leverage")
    zero_rel = np.array([row["zero_residual_rel"] for row in rows])
    zero_ward = bool(np.all(zero_rel <= ZERO_REL_WARD))
    print("    requested zero-truncation ward: |Z_2500-Z_total|/"
          "|tau(n-q)| band %.3e/%.3e/%.3e vs %.0e"
          % (band(zero_rel) + (ZERO_REL_WARD,)))
    print("    This is a truncation diagnostic, not an identity proof;"
          " failure does not weaken the exact D1/D2 dictionary.")
    check("Z1 typed zero-side numerical ward %s"
          % ("RESOLVED" if zero_ward else "UNRESOLVED"),
          True)
    tail_dex = np.array([row["tail_dex"] for row in rows])
    total_budget = np.array([
        (row["tail_zfr"] + row["transport_budget"])
        / max(abs(row["raw"]), 1e-300) for row in rows])
    total_budget_dex = np.log10(total_budget)
    n_close = int(np.sum(total_budget < 1.0))
    print("    PT+Rosser+ZFR tail demand/supply log10(tail/|W2|): "
          "band %+.3f/%+.3f/%+.3f dex"
          % band(tail_dex))
    print("    including measured Galerkin-transport defect: "
          "%+.3f/%+.3f/%+.3f dex; float-level closes %d/%d"
          % (band(total_budget_dex) + (n_close, len(rows))))
    shares = np.array([row["share_t0"] for row in rows])
    print("    zeros below 3,000,175,332,800 carry at least "
          "%.8f/%.8f/%.8f of the exact zero-side total per rung"
          % band(shares))
    zfr_gain = -np.log10(np.array([row["zfr_gain"] for row in rows]))
    print("    zero-free-region gain over strip-only high-tail envelope: "
          "%.4f/%.4f/%.4f dex (small at T_RH)" % band(zfr_gain))

    section("B -- prime-side Buethe/ZFR supplies")
    sound_b = all(row["sound_b"] for row in rows)
    sound_z = all(row["sound_z"] for row in rows)
    check("B1 measured remainders lie inside Buethe and ZFR envelopes",
          sound_b and sound_z, "Buethe %s; ZFR %s"
          % (sound_b, sound_z), kill="WARD-BROKEN")
    bdex = np.array([row["buethe_dex"] for row in rows])
    zdex = np.array([row["zfr_prime_dex"] for row in rows])
    bfinite = bdex[np.isfinite(bdex)]
    zfinite = zdex[np.isfinite(zdex)]
    print("    Buethe supply/headroom: %s"
          % (("%+.2f/%+.2f/%+.2f dex on %d/%d positive-headroom rows"
              % (band(bfinite) + (len(bfinite), len(rows))))
             if len(bfinite) else
             "NO-POSITIVE-HEADROOM (0/%d)" % len(rows)))
    print("    Trudgian-ZFR supply/headroom: %s"
          % (("%+.2f/%+.2f/%+.2f dex on %d/%d positive-headroom rows"
              % (band(zfinite) + (len(zfinite), len(rows))))
             if len(zfinite) else
             "NO-POSITIVE-HEADROOM (0/%d)" % len(rows)))

    section("C -- controls + anti-circularity")
    controls = control_census()
    for name, value in controls.items():
        print("    %-9s lambda_min finite Weil-cone form = %+.6e"
              % (name, value))
    check("C1 truth positive and smooth/scramble/Epstein negative",
          controls["truth"] > 0.0
          and all(controls[name] < 0.0
                  for name in ("smooth", "scramble", "Epstein")),
          "Epstein %.3e (off-line-zero calibration breaks positivity,"
          " not the dictionary)" % controls["Epstein"],
          kill="CONTROL-DEAD")
    check("C2 anti-circularity: target data enter only the comparandum/lift;"
          " supplies use cited constants + source geometry", True)

    section("T -- mandatory tau screens")
    taus = np.array([row["tau"] for row in rows])
    raw = np.abs(np.array([row["raw"] for row in rows]))
    pt_margin = np.array([abs(row["wall"]) - row["tail_zfr"]
                          for row in rows])
    b_margin = np.array([row["background"] - row["supply_b"]
                         for row in rows])
    for name, values in (("raw W2 margin", raw),
                         ("PT-tail margin", pt_margin),
                         ("Buethe margin", b_margin)):
        label, _ = screen(values, taus)
        print("    %-18s %s" % (name, label))
    check("T1 screens recorded with 0=PROGRESS, +1=RELOCATION", True)

    if n_close == len(rows) and lag_ward and zero_ward:
        verdict = ("W2-CLOSES-UNCONDITIONALLY (FINITE %d-STEP "
                   "DEPLOYED+DEEP SURFACE ONLY; exact odd Fejer-spline "
                   "Weil section; PT+Rosser+ZFR tail below every W2 margin)"
                   % len(rows))
    elif n_close == len(rows):
        verdict = (
            "W2-NEEDS-EXACT-GALERKIN-TRANSPORT "
            "(classical PT+Rosser+ZFR weighted-tail budget closes the "
            "finite float surface %d/%d, even after the measured transport "
            "defect; but the unchanged 1e-8 wards are lag=%s and "
            "zero-truncation=%s, max lag rel %.2e, zero residual med %.2e; "
            "therefore no unconditional finite-surface theorem is issued)"
            % (n_close, len(rows),
               "PASS" if lag_ward else "FAIL",
               "PASS" if zero_ward else "FAIL",
               lag_worst, float(np.median(zero_rel))))
    else:
        short = float(np.median(total_budget_dex[total_budget_dex >= 0.0])) \
            if np.any(total_budget_dex >= 0.0) \
            else float(np.median(total_budget_dex))
        verdict = ("W2-NEEDS-WEIGHTED-ZERO-TAIL (finite odd Fejer-spline "
                   "Guinand--Weil cone; PT locates zeros but N(T)/ZFR "
                   "absolute tail misses %d/%d rungs, median open shortfall "
                   "%+.2f dex; not Li/NB/pair-correlation and not an "
                   "RH-equivalent finite cone)" % (
                       len(rows) - n_close, len(rows), short))
    if not zero_ward:
        verdict += (" / ZERO-NUMERIC-WARD-UNRESOLVED(2500-zero residual "
                    "med %.2e of W2)" % float(np.median(zero_rel)))
    return finish({"verdict": verdict})


if __name__ == "__main__":
    raise SystemExit(main())
