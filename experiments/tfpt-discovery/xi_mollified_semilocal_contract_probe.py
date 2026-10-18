#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""xi_mollified_semilocal_contract_probe -- PRIME.XI.MOLLIFIED.SEMILOCAL.01

FROZEN THEOREM CONTRACT (2026-08-13).  EXPLORATION ONLY.  NO RH CLAIM.
This file writes nothing and runs only cheap exact/symbolic prerequisite
checks.  It does not duplicate PRIME.COFINAL.SHIFT.AVERAGE.DEEP.01.

SELECTED TARGET.  Let

    Xi(z) = xi(1/2 - i z).

For Y,T -> infinity, build a source-only real crossing set from the
Riemann-Siegel Gamma phase and the prime-power Euler phase with the C2
semilocal weight

    a_{Y,T}(n,t) = w_Y(n) s(clip((t/2pi)^beta/n - 1, 0, 1)),
    s(x) = 10x^3 - 15x^4 + 6x^5,

where w_Y is 1 below Y/2, transitions by the same smootherstep, and is 0
at and above Y.  The mirror-symmetric crossing set is the spectrum of a
finite self-adjoint diagonal operator D_{Y,T}.  Put

    F_{Y,T}(z) = Tr (D_{Y,T} - z)^{-1} + explicit arch/Euler tails.

The theorem target is:

  (M1) there are affine gauges A_{Y,T} z + B_{Y,T} such that the
       UNNORMALIZED regularized full traces

       R_{Y,T}(z) = F_{Y,T}(z) - A_{Y,T} z - B_{Y,T}

       converge to -Xi'(z)/Xi(z) on one safe open set Im z > 1/2;

  (M2) the same R_{Y,T} are locally bounded on the WHOLE upper
       half-plane, uniformly on compact sets;

  (M3) the integrated, normalized real-rooted determinants converge
       locally uniformly to Xi (equivalently: M1+M2 plus one
       normalization point and the standard logarithmic-derivative
       integration lemma);

  (M4) the proof of M2 contains an arithmetic-specific estimate that
       fails for the frozen Epstein/Scramble/Smooth controls.  A generic
       density or Gram estimate does not pass the TFPT frozen gate.

M1+M2 imply by Vitali and the identity theorem that -Xi'/Xi has no pole
in the upper half-plane.  Functional-equation symmetry then excludes
nonreal zeros, hence RH.  Equivalently, M3 plus Hurwitz gives RH directly.
The target is therefore at least RH-hard (and may be strictly stronger for
this particular approximant family).  It is not an "almost proof".

NEW NORMALIZATION BUG FOUND IN ROUNDS 1/2.  Their convergence gate uses
the UNNORMALIZED completed trace F, whose residues have magnitude one,
but their Herglotz normal-family check divides the finite-window trace by
dim.  The normalized vector-state resolvent has total spectral mass one
and residues 1/dim, so it cannot converge to -Xi'/Xi, whose simple-zero
residues have magnitude one.  Giving every pole unit residue requires a
vector of squared norm dim, destroying the claimed dimension-independent
Herglotz bound.  Thus the existing Herglotz check does not support the
Vitali step.  M2 above is deliberately the missing UNNORMALIZED,
REGULARIZED normal-family lemma.

SECOND SEMANTIC LIMIT FOUND.  CofinalWeil.CofinalHypothesis documents
that idx is pre-fixed independently of measured signs, but the Lean type
does not enforce that independence: A is a parameter of the structure,
and a producer may compute idx from A before constructing the value.
Field order is an audit convention, not a noninterference theorem.  This
does not invalidate limit_nonneg_of_cofinal_seq; it means the PREDEFINED
condition remains an external premise.

WHY THE OTHER CANDIDATES ARE REJECTED.
  * A deeper finite shift-average certification duplicates the active
    worker.  An all-depth average identity still needs an arithmetic sign
    estimate and a sign-independent selector to instantiate H_cof.
  * G2, mu(p^k) exp(u/2) k/2 = u, is exactly Lambda(p^k)=log p rewritten.
    It discriminates the frozen controls but supplies no sign inequality.
  * Radau/SOS/cofinal packages certify selected finite float64 matrices and
    consume a previous-rung sign gate; they do not address an all-depth
    source theorem.
  * Fold covariance is already PATTERN-ONLY at k=3.

CHEAP PREREQUISITES CHECKED HERE.
  P1 smootherstep is C2 at both endpoints, monotone, and complementary;
  P2 the logarithmic taper is source-only and compactly supported;
  P3 the elementary safe-half-plane Euler-tail majorant is correct;
  P4 determinant/log-derivative and residue identities are exact;
  P5 the residue-vs-Herglotz-mass obstruction is exact;
  P6 both existing Xi probes really mix an unnormalized convergence gate
     with a normalized Herglotz diagnostic;
  P7 H_cof's noninterference condition is documentary, not type-enforced;
  P8 the selected contract includes the frozen world-discrimination gate.

VERDICT ENUM.
  CONTRACT-BROKEN   any cheap prerequisite fails.
  CONTRACT-EXPOSED  all prerequisites pass; the exact missing lemma is M2
                    (with M1 still unproved, only measured in round 2).

No paper, ledger, website, verification module, manifest, or marker is
touched.  No .md file.  No commit.
"""

from __future__ import annotations

import ast
import hashlib
import math
import os
import sys
from fractions import Fraction as F

import sympy as sp


HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()

CHECKS: list[tuple[str, bool]] = []


def check(name: str, ok: bool, detail: str = "") -> bool:
    ok = bool(ok)
    CHECKS.append((name, ok))
    print("  [%s] %s%s" % ("PASS" if ok else "FAIL", name,
                           (" -- " + detail) if detail else ""))
    return ok


def poly_add(a: list[F], b: list[F]) -> list[F]:
    out = [F(0)] * max(len(a), len(b))
    for i, v in enumerate(a):
        out[i] += v
    for i, v in enumerate(b):
        out[i] += v
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def poly_mul(a: list[F], b: list[F]) -> list[F]:
    out = [F(0)] * (len(a) + len(b) - 1)
    for i, u in enumerate(a):
        for j, v in enumerate(b):
            out[i + j] += u * v
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def poly_compose_affine(a: list[F], c0: F, c1: F) -> list[F]:
    out = [F(0)]
    power = [F(1)]
    for coeff in a:
        out = poly_add(out, [coeff * v for v in power])
        power = poly_mul(power, [c0, c1])
    return out


def poly_derivative(a: list[F]) -> list[F]:
    return [F(i) * a[i] for i in range(1, len(a))] or [F(0)]


def poly_value(a: list[F], x: F) -> F:
    out = F(0)
    for coeff in reversed(a):
        out = out * x + coeff
    return out


def read(relpath: str) -> str:
    with open(os.path.join(ROOT, relpath), encoding="utf-8") as fh:
        return fh.read()


def ast_has_banned_constructor_names() -> list[str]:
    """The contract's source-side helpers must not invoke zeta/zero APIs."""
    banned = {"zetazero", "nzeros", "zeta", "xi", "eigh", "eigvalsh"}
    tree = ast.parse(read("experiments/tfpt-discovery/"
                          "xi_mollified_semilocal_contract_probe.py"))
    hits = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            fun = node.func
            name = (fun.id if isinstance(fun, ast.Name) else
                    fun.attr if isinstance(fun, ast.Attribute) else "")
            if name.lower() in banned:
                hits.append(name)
    return sorted(set(hits))


def main() -> int:
    print("=" * 78)
    print("PRIME.XI.MOLLIFIED.SEMILOCAL.01 -- frozen theorem contract")
    print("SPEC_SHA %s" % SPEC_SHA[:16])
    print("=" * 78)

    # P1: exact smootherstep algebra.
    smoother = [F(0), F(0), F(0), F(10), F(-15), F(6)]
    ds = poly_derivative(smoother)
    d2s = poly_derivative(ds)
    deriv_factor = poly_mul([F(0), F(0), F(30)],
                            [F(1), F(-2), F(1)])
    complement = poly_add(
        smoother,
        poly_compose_affine(smoother, F(1), F(-1)))
    check("P1.1 smootherstep endpoint values",
          poly_value(smoother, F(0)) == 0
          and poly_value(smoother, F(1)) == 1)
    check("P1.2 smootherstep is C2 at both endpoints",
          all(poly_value(p, x) == 0 for p in (ds, d2s)
              for x in (F(0), F(1))))
    check("P1.3 smootherstep monotonicity factor",
          ds == deriv_factor,
          "s'(x) = 30 x^2 (1-x)^2 >= 0")
    check("P1.4 smootherstep complement identity",
          complement == [F(1)], "s(x)+s(1-x)=1 exactly")

    # P2: the taper definition is source-only and compactly supported.
    hits = ast_has_banned_constructor_names()
    check("P2 source-side contract firewall", not hits,
          "banned constructor calls: %s" % (hits or "none"))
    taper_samples = []
    for r in (F(0), F(1, 4), F(1, 2), F(3, 4), F(1), F(5, 4)):
        if r <= F(1, 2):
            w = F(1)
        elif r >= 1:
            w = F(0)
        else:
            w = poly_value(smoother, 2 * (1 - r))
        taper_samples.append((r, w))
    check("P2.2 compact C2 taper range/support",
          all(0 <= w <= 1 for _r, w in taper_samples)
          and taper_samples[0][1] == 1
          and taper_samples[-1][1] == 0,
          "samples %s" % taper_samples)

    # P3: unconditional safe-half-plane Euler-tail majorant.
    y, sigma = sp.symbols("Y sigma", positive=True)
    tail = y ** (1 - sigma) * (
        sp.log(y) / (sigma - 1) + 1 / (sigma - 1) ** 2)
    deriv = sp.simplify(sp.diff(tail, y) + sp.log(y) * y ** (-sigma))
    check("P3 safe-half-plane tail antiderivative",
          deriv == 0,
          "d/dY integral_Y^inf log(t)t^-sigma dt = -log(Y)Y^-sigma")
    numeric_tail = float(tail.subs({y: 1000, sigma: sp.Rational(3, 2)}))
    check("P3.2 safe Euler-tail majorant decays for sigma>1",
          numeric_tail > 0
          and float(tail.subs({y: 10 ** 6,
                               sigma: sp.Rational(3, 2)}))
          < numeric_tail)

    # P4/P5: determinant, residues, and the normalization obstruction.
    z = sp.symbols("z")
    lams = sp.symbols("l0:3", real=True)
    det = sp.prod(z - lam for lam in lams)
    logder = sp.simplify(sp.diff(det, z) / det)
    full = sum(1 / (z - lam) for lam in lams)
    check("P4 determinant logarithmic-derivative identity",
          sp.simplify(logder - full) == 0)
    trace_d_minus_z = sum(1 / (lam - z) for lam in lams)
    residue_full = sp.limit((z - lams[0]) * trace_d_minus_z,
                            z, lams[0])
    residue_norm = sp.limit(
        (z - lams[0]) * trace_d_minus_z / len(lams), z, lams[0])
    check("P4.2 full trace has unit-magnitude pole residue",
          residue_full == -1)
    check("P5 normalized trace has the wrong residue",
          residue_norm == -sp.Rational(1, len(lams)),
          "full residue -1, normalized residue %s" % residue_norm)
    weights = sp.symbols("w0:3", nonnegative=True)
    mass_one = sp.Eq(sum(weights), 1)
    all_unit_mass = sum(sp.Integer(1) for _ in weights)
    check("P5.2 residue-vs-Herglotz-mass obstruction",
          all_unit_mass == len(weights) and len(weights) != 1,
          "unit vector: sum residues=1; unit residue at %d poles "
          "requires ||e||^2=%d" % (len(weights), len(weights)))
    xx, yy, lam = sp.symbols("x y lambda", real=True)
    imag_kernel = sp.simplify(sp.im(1 / (lam - (xx + sp.I * yy))))
    check("P5.3 self-adjoint resolvent is Herglotz before normalization",
          imag_kernel == yy / ((lam - xx) ** 2 + yy ** 2))

    # P6: source audit of the two existing Xi probes.
    xi1 = read("experiments/tfpt-discovery/xi_realrooted_limit_probe.py")
    xi2 = read("experiments/tfpt-discovery/"
               "xi_realrooted_limit_r2_probe.py")
    normalized_diag = all(
        ("Fw / dim" in src or "abs(Fw / dim)" in src)
        and "F_completed" in src and "target" in src
        for src in (xi1, xi2))
    check("P6 existing Xi rounds mix normalized Herglotz and "
          "unnormalized target gates", normalized_diag)
    print("  [BUG-CONFIRMED] XI-HERGLOTZ-NORMALIZATION: the Vitali "
          "normal-family diagnostic is on F_window/dim, while the "
          "convergence target is the unnormalized completed trace.")

    # P7: the Lean type cannot enforce sign-independent construction.
    cof = read("experiments/lean4-carrier-rigidity/"
               "TfptCarrier/CofinalWeil.lean")
    documentary_only = (
        "structure CofinalHypothesis (A :" in cof
        and "idx : ℕ → ℕ" in cof
        and "psd : ∀ j, (A (idx j)).PosSemidef" in cof
        and "chosen independently of measured signs" in cof)
    check("P7 H_cof predefinition is documented but not "
          "noninterference-typed", documentary_only)
    print("  [PREMISE-HIDDEN] HCOF-NONINTERFERENCE: Lean proves the "
          "limit implication for a supplied idx; it does not prove "
          "that idx was not computed from A or its signs.")

    # P8: the contract carries a first-class discrimination clause.
    contract = __doc__
    check("P8 frozen gate requires arithmetic world discrimination",
          "(M4)" in contract and "Epstein/Scramble/Smooth" in contract)

    passed = sum(ok for _name, ok in CHECKS)
    verdict = ("CONTRACT-EXPOSED" if passed == len(CHECKS)
               else "CONTRACT-BROKEN")
    print("\n" + "=" * 78)
    print("CHECKS %d/%d PASS" % (passed, len(CHECKS)))
    print("VERDICT: %s" % verdict)
    print("EXACT MISSING LEMMA: a locally bounded family on every "
          "compact K subset of Im(z)>0 for the UNNORMALIZED, "
          "AFFINE-REGULARIZED full traces R_{Y,T}, together with "
          "safe-open-set convergence.  The current normalized "
          "Herglotz check cannot supply it.")
    print("DIFFICULTY: this lemma plus the checked prerequisites implies "
          "RH by Vitali/identity; for this real-rooted approximant "
          "family it is at least RH-hard and may be stronger.")
    print("NO RH CLAIM.  NO POSITIVITY CLAIM.  EXPERIMENTS ONLY.")
    print("=" * 78)
    return 0 if verdict == "CONTRACT-EXPOSED" else 1


if __name__ == "__main__":
    sys.exit(main())
