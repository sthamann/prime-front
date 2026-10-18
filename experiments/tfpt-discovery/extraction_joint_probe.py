#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""extraction_joint_probe -- PRIME.RDAGGER.EXTRACTION_JOINT_REDESIGN.01 (r473).

Diagnoses the r470 k=5 signed native read against the classical
Guinand--Weil functional Q(g_f) and seals the redesigned extraction
joint: polynomial-class A_cap reads (proved) plus a named
fixed-support approximation carrying the arch tent error.

SCRAMBLE GATE (r469 anti-list item 3).  This probe proposes no
bound on q^dagger.  It is a finite comparison of one native
fullRead against one classical Q at the unscrambled selected
window k=5.  A source scramble would change both numbers; the
round does not claim scramble-invariance of either.

VERDICT: ARTEFACT + POLY_BRIDGE_PROVED.
Research documentation.  NO RH claim.
"""
from __future__ import annotations

import argparse
import hashlib
import math
import os
import sys

import numpy as np
from mpmath import mp

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", ".."))
PROB = os.path.join(REPO, "rh", "problem")
for p in (HERE, PROB):
    if p not in sys.path:
        sys.path.insert(0, p)

import cofinal_family_probe as R458  # noqa: E402
import quadrep_probe as Q  # noqa: E402
import verify_lstar_instance as V  # noqa: E402

SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
CHECKS: list[tuple[str, bool]] = []

mp.dps = 50

PIN_Q = 0.0769078530458283
PIN_FULLREAD = -0.0428854252772195
PIN_ERR = 0.1197932783230478
PIN_ARCH_CL = 0.2131977998658999
PIN_ARCH_WIN = 0.0934045215428521
PIN_COMB = 0.1364027472150502
PIN_POLE = 0.0001128003949786
PIN_FEJER_Q = 0.0880146104737050


def check(name: str, ok: bool, detail: str = "") -> None:
    CHECKS.append((name, bool(ok)))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name:38s} {detail}")


def read(relative: str) -> str:
    with open(os.path.join(REPO, relative), encoding="utf-8") as handle:
        return handle.read()


def von_mangoldt(n_max: int) -> np.ndarray:
    sieve = np.ones(n_max + 1, dtype=bool)
    sieve[:2] = False
    for i in range(2, int(math.isqrt(n_max)) + 1):
        if sieve[i]:
            sieve[i * i::i] = False
    lam = np.zeros(n_max + 1)
    for p in np.nonzero(sieve)[0]:
        p = int(p)
        lp = math.log(p)
        q = p
        while q <= n_max:
            lam[q] = lp
            q *= p
    return lam


def g_pl(acf: np.ndarray, d0: float, u) -> float:
    u = abs(float(u))
    knots = np.arange(len(acf), dtype=float) * d0
    return float(np.interp(u, knots, acf, right=0.0))


def arch_classical(g, b: float):
    """A_arch via the u-space digamma identity, mpmath dps 50."""
    b = mp.mpf(b)
    cb = -mp.euler - mp.log(mp.pi) - mp.log(1 - mp.e ** (-2 * b))
    g0 = mp.mpf(g(0.0))

    def integrand(u):
        uu = mp.mpf(u)
        wgt = 2 * mp.e ** (-uu / 2) / (1 - mp.e ** (-2 * uu))
        return wgt * (mp.e ** (-mp.mpf("1.5") * uu) * g0 - mp.mpf(g(float(uu))))

    return cb * g0 + mp.quad(integrand, [0, b])


def comb_exact(g, b: float) -> float:
    nmax = int(math.floor(math.exp(b) + 2))
    lam = von_mangoldt(nmax)
    acc = 0.0
    for n in range(2, lam.size):
        if lam[n] == 0.0:
            continue
        u = math.log(n)
        if u > b + 1e-15:
            continue
        acc += (2.0 * lam[n] / math.sqrt(n)) * g(u)
    return acc


def text_gates() -> None:
    inner = read("rh/lean/RH/InnerBridges.lean")
    frequent = read("rh/lean/RH/FrequentlySelected.lean")
    check("poly-bridge-proved",
          "theorem selectedACapPsdImpliesPolynomialReads" in inner
          and "theorem hankel_quadform" in inner
          and "\n  sorry" not in inner)
    check("arch-gap-identity-proved",
          "theorem fullRead_weilForm_gap_eq_arch" in inner
          and "comb_elementwise_stabilization" in inner)
    check("named-approx-bridge",
          "def SelectedPolynomialApproximatesGrid" in inner
          and "∃ᶠ" not in inner.split(
              "def SelectedPolynomialApproximatesGrid")[1].split(
              "theorem selected_reads_ge_neg_archError_of_approx")[0])
    check("redesigned-joint",
          "def FrequentlySelectedPolynomialJoint" in frequent
          and "theorem weilForm_ge_neg_two_archError_of_joint" in frequent
          and "theorem selected_polynomial_nonneg_of_cone" in frequent)
    check("old-channel-retained",
          "def SelectedReadQuadraticRepresentation" in inner
          and "def FrequentlySelectedInternalMincut" in frequent)


def numerical_gates() -> None:
    shp = R458.lean_shape(5)
    a, m, M, Delta = shp["a"], shp["m"], shp["M"], shp["D"]
    car = V.arch_lags(M, Delta)
    mask = V.PP <= a * a
    U_atoms, MU_atoms = V.U[mask], V.W_VM[mask]
    steps, mesh = Q.PIN_STEPS_COVER, Q.PIN_MESHEXP_COVER
    d0 = 2.0 ** (-mesh)
    support = steps * d0
    T = Q.hess_full(steps, mesh, m, car, Delta, U_atoms, MU_atoms)
    ev, evec = np.linalg.eigh(T)
    x = evec[:, 0] / np.linalg.norm(evec[:, 0])
    fr = float(Q.full_read(x, mesh, m, car, Delta, U_atoms, MU_atoms))
    acf = Q.acf_of(x, d0)

    def gpl(u, acf=acf, d0=d0):
        return g_pl(acf, d0, u)

    F = lambda u: Q.to_fun(acf, d0, u)
    arch_win = float(car[0] * F(0.0))
    for i in range(1, m + 1):
        arch_win += 2.0 * float(car[i] * F(i * Delta))
    comb_win = float(np.dot(MU_atoms, F(U_atoms)))
    nmax = len(x) + 3
    pole_win = 0.0
    for k in range(-nmax, nmax + 1):
        pole_win += float(F(k * d0) * Q.pole_delta(d0, k))
    pole_win = -pole_win / d0

    arch_cl = arch_classical(gpl, support)
    comb_cl = comb_exact(gpl, support)
    q_val = float(arch_cl) + pole_win - comb_cl
    err = float(arch_cl) - arch_win

    check("k5-fullRead-negative",
          abs(fr - PIN_FULLREAD) < 2e-15 and fr < 0,
          f"fullRead={fr:.16f}")
    check("k5-Q-positive",
          abs(q_val - PIN_Q) < 2e-15 and q_val > 0,
          f"Q={q_val:.16f}")
    check("k5-arch-error",
          abs(err - PIN_ERR) < 2e-15
          and abs(float(arch_cl) - PIN_ARCH_CL) < 2e-13
          and abs(arch_win - PIN_ARCH_WIN) < 2e-15,
          f"err={err:.16f}")
    check("k5-comb-exact",
          abs(comb_win - PIN_COMB) < 2e-15
          and abs(comb_cl - comb_win) < 1e-14,
          f"comb={comb_win:.16f}")
    check("k5-pole-native",
          abs(pole_win - PIN_POLE) < 2e-15,
          f"pole={pole_win:.16f}")
    check("artefact-split",
          q_val > 0 > fr and abs((q_val - fr) - err) < 1e-14,
          "Q>0>fullRead; gap = arch tent error")

    uu = np.linspace(0.0, support, 2000)
    du = uu[1] - uu[0]
    gv = np.array([gpl(u) for u in uu])
    ghats = np.array([
        2.0 * np.trapezoid(gv * np.cos(t * uu), dx=du)
        for t in np.linspace(0.0, 30.0, 120)
    ])
    check("g-positive-type",
          float(ghats.min()) > 0.0,
          f"ghat_min={float(ghats.min()):.6e}")

    def gtri(u):
        return max(0.0, 1.0 - abs(float(u)))

    q_fejer = float(arch_classical(gtri, 1.0)
                    + 4 * mp.quad(
                        lambda u: mp.mpf(gtri(float(u))) * mp.cosh(mp.mpf(u) / 2),
                        [0, 1])
                    - comb_exact(gtri, 1.0))
    check("fejer-ward",
          q_fejer > 0 and abs(q_fejer - PIN_FEJER_Q) < 2e-13,
          f"Q_Fejer={q_fejer:.16f}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--smoke", action="store_true")
    parser.parse_args()
    print("extraction_joint_probe -- r473")
    print(f"SPEC_SHA {SPEC_SHA[:16]}")
    text_gates()
    numerical_gates()
    failed = [name for name, ok in CHECKS if not ok]
    print(f"RESULT: {len(CHECKS)-len(failed)}/{len(CHECKS)} gates PASS")
    if failed:
        print("FAILED:", ", ".join(failed))
        return 1
    print("EXTRACTION JOINT PROBE VERIFIED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
