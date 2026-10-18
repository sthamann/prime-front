#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""quadrep_probe -- PRIME.RDAGGER.QUADREP.01 (r470).

Seals the exact finite obstruction to
SelectedReadQuadraticRepresentation.  The original r464 Prop
quantifies over every mesh-compatible GridElement with unbounded
steps.  At the selected window k=5 the native Hessian of fullRead
on an onset-compatible covering element is indefinite of rank
24 > cap+1 = 11, while A_cap is positive definite, so a negative
native read cannot be a quadratic value of A_cap.

SCRAMBLE GATE (r469 anti-list item 3).  This probe proposes no
bound on q^dagger and is not scramble-classified as a bound: it
is a finite linear-algebra witness on the unscrambled selected
window k=5.  A source scramble would change the Hessian; the
round does not claim scramble-invariance.

VERDICT: OBSTRUCTION_SEALED.
Research documentation.  NO RH claim.
"""
from __future__ import annotations

import argparse
import hashlib
import math
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", ".."))
PROB = os.path.join(REPO, "rh", "problem")
for p in (HERE, PROB):
    if p not in sys.path:
        sys.path.insert(0, p)

import cofinal_family_probe as R458  # noqa: E402
import verify_lstar_instance as V  # noqa: E402

SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
CHECKS: list[tuple[str, bool]] = []

# Frozen pins (k=5 selected window; Hessian of fullRead at
# meshExp=3, steps=24).  First computed in /tmp/quadrep_explore.py
# then sealed here.
PIN_TMIN = -0.042885425277
PIN_QDAG = 0.8778980273211964
PIN_AMIN = 6.61841958078e-08
PIN_RANK = 24
PIN_NNEG = 2
PIN_CAP = 10
PIN_STEPS_COVER = 24
PIN_MESHEXP_COVER = 3
PIN_ANCHOR = 21


def check(name: str, ok: bool, detail: str = "") -> None:
    CHECKS.append((name, bool(ok)))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name:38s} {detail}")


def read(relative: str) -> str:
    with open(os.path.join(REPO, relative), encoding="utf-8") as handle:
        return handle.read()


def pole_potential(t: float) -> float:
    return -8.0 * (math.cosh(abs(t) / 2.0) - 1.0)


def pole_delta(D: float, k: int) -> float:
    return (pole_potential((k - 1) * D) - 2.0 * pole_potential(k * D)
            + pole_potential((k + 1) * D))


def to_fun(acf: np.ndarray, D0: float, u) -> np.ndarray:
    u = np.abs(np.asarray(u, dtype=float))
    knots = np.arange(len(acf), dtype=float) * D0
    return np.interp(u, knots, acf, right=0.0)


def acf_of(x: np.ndarray, D0: float) -> np.ndarray:
    ng = len(x)
    a = np.correlate(x, x, "full")[ng - 1:] * D0
    return np.append(a, 0.0)


def full_read(x, mesh_exp, m, car, Delta, U_atoms, MU_atoms):
    D0 = 2.0 ** (-mesh_exp)
    acf = acf_of(np.asarray(x, float), D0)
    F = lambda u: to_fun(acf, D0, u)
    arch = float(car[0] * F(0.0))
    for i in range(1, m + 1):
        arch += 2.0 * float(car[i] * F(i * Delta))
    comb = float(np.dot(MU_atoms, F(U_atoms)))
    nmax = len(x) + 3
    pole = 0.0
    for k in range(-nmax, nmax + 1):
        pole += float(F(k * D0) * pole_delta(D0, k))
    pole = -pole / D0
    return arch - comb + pole


def hess_full(steps, mesh_exp, m, car, Delta, U_atoms, MU_atoms):
    T = np.zeros((steps, steps))
    for i in range(steps):
        e = np.zeros(steps)
        e[i] = 1.0
        T[i, i] = full_read(e, mesh_exp, m, car, Delta, U_atoms, MU_atoms)
        for j in range(i + 1, steps):
            ep = np.zeros(steps)
            ep[i] = 1.0
            ep[j] = 1.0
            em = np.zeros(steps)
            em[i] = 1.0
            em[j] = -1.0
            vp = full_read(ep, mesh_exp, m, car, Delta, U_atoms, MU_atoms)
            vm = full_read(em, mesh_exp, m, car, Delta, U_atoms, MU_atoms)
            T[i, j] = T[j, i] = 0.25 * (vp - vm)
    return T


def text_gates() -> None:
    inner = read("rh/lean/RH/InnerBridges.lean")
    check("channel-remainder-retained",
          "def SelectedReadQuadraticRepresentation" in inner
          and "f.meshExp ≤ selectedMesh k" in inner
          and "steps ≤" not in inner.split(
              "def SelectedReadQuadraticRepresentation")[1].split(
              "def SelectedACapPsdImpliesPlainReads")[0])
    check("quantifier-witness-proved",
          "theorem exists_mesh_compatible_steps_gt_cap" in inner
          and "selectedCapStepsWitness" in inner
          and "\n  sorry" not in inner)
    check("signed-obstruction-named",
          "def SelectedOnsetCompatibleNegativeRead" in inner
          and "theorem quadraticRepresentation_refuted_of_negative_read"
          in inner)
    check("no-new-sorry-in-inner", "\n  sorry" not in inner)


def numerical_gates() -> None:
    shp = R458.lean_shape(5)
    a, m, M, Delta = shp["a"], shp["m"], shp["M"], shp["D"]
    cap = (m + 1) // 2
    check("k5-arithmetic-witness",
          m == 19 and cap == PIN_CAP and (PIN_CAP + 1) > cap
          and 19 <= m,
          f"m={m} cap={cap} steps_gt={PIN_CAP + 1}")

    car = V.arch_lags(M, Delta)
    mask = V.PP <= a * a
    U_atoms = V.U[mask]
    MU_atoms = V.W_VM[mask]
    T = hess_full(PIN_STEPS_COVER, PIN_MESHEXP_COVER, m, car, Delta,
                  U_atoms, MU_atoms)
    ev = np.linalg.eigvalsh(T)
    scale = max(1.0, float(np.max(np.abs(ev))))
    rank = int(np.sum(np.abs(ev) > 1e-10 * scale))
    n_neg = int(np.sum(ev < -1e-10 * scale))
    tmin = float(ev[0])
    support = PIN_STEPS_COVER * 2.0 ** (-PIN_MESHEXP_COVER)
    a0 = max(1, math.ceil(math.exp(support)))
    check("k5-onset-compatible",
          PIN_MESHEXP_COVER <= m and a0 == PIN_ANCHOR and a0 <= a,
          f"meshExp={PIN_MESHEXP_COVER} a0={a0} a={a} support={support}")
    check("k5-rank-gap",
          rank == PIN_RANK and rank > cap + 1,
          f"rank={rank} cap+1={cap + 1}")
    check("k5-hessian-indefinite",
          n_neg == PIN_NNEG and abs(tmin - PIN_TMIN) < 2e-12,
          f"n_neg={n_neg} tmin={tmin:.12f}")

    mz = R458.mz_from_shape(shp)
    pk, _ = R458.lean_pack(5)
    n = cap
    xs = np.concatenate([mz["xp"], mz["yn"]])
    ws = np.concatenate([mz["wp"], -mz["vn"]])
    H = np.array([[np.sum(ws * xs ** (i + j)) for j in range(n)]
                  for i in range(n)])
    bxs, bws, bys, bvs = R458.border_from_shape(shp)
    bx = np.concatenate([np.asarray(bxs, float), np.asarray(bys, float)])
    bw = np.concatenate([np.asarray(bws, float), -np.asarray(bvs, float)])
    u = np.array([np.sum(bw * bx ** i) for i in range(n)])
    B = float(pk["Bw"])
    A = np.zeros((n + 1, n + 1))
    A[:n, :n] = H
    A[:n, n] = u
    A[n, :n] = u
    A[n, n] = B
    evA = np.linalg.eigvalsh(A)
    amin = float(evA[0])
    qdag = float(pk["qdag"])
    check("k5-A-cap-posdef",
          amin > 0 and abs(amin - PIN_AMIN) < 1e-12 and qdag < 1.0
          and abs(qdag - PIN_QDAG) < 1e-12,
          f"amin={amin:.6e} qdag={qdag:.12f}")
    check("k5-sign-obstruction",
          tmin < 0 < amin,
          "T indefinite, A_cap PD: existential channel fails")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--smoke", action="store_true")
    parser.parse_args()
    print("quadrep_probe -- r470")
    print(f"SPEC_SHA {SPEC_SHA[:16]}")
    text_gates()
    numerical_gates()
    failed = [name for name, ok in CHECKS if not ok]
    print(f"RESULT: {len(CHECKS)-len(failed)}/{len(CHECKS)} gates PASS")
    if failed:
        print("FAILED:", ", ".join(failed))
        return 1
    print("QUADREP PROBE VERIFIED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
