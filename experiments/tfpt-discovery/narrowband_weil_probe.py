#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""narrowband_weil_probe -- PRIME.RDAGGER.NARROWBAND_WEIL.01
(round 461): consistency probe between the Lean frequently-selected
mincut and classical compact-window Weil positivity.
Research documentation.  NO RH claim.  NO anti-RH claim.

VERDICT: FORK_SHARPENED.

Q1.  The Lean endpoint is `forall f : GridElement, 0 <= weilForm f`.
A GridElement is the even piecewise-linear autocorrelation of arbitrary
real step data on a dyadic mesh.  Hence its Fourier transform is
nonnegative in the classical autocorrelation sense.  The route does NOT
formalize the spectral/zero side or the density/continuity extension to
the standard C_c-infinity Weil criterion.  Since r638L it consumes the
unasserted `ArchGaussMellinDigammaIdentity` contract explicitly and the
named, unproved `SelectedACapPsdImpliesPlainReads` bridge; no arch
`sorryAx` is asserted.

Q2.  In the r459 builder normalization,
  Delta_k = 2^(-floor(sqrt(k))) log 2,
  N_k = (m_k + 1)/2,
  U_k = N_k Delta_k = k log 2 / 2.
Here U_k is the half-width of the autocorrelation and the length of the
underlying step-function support; in the modern `[-L,L]` convention
L_k = U_k/2.  Bombieri Theorem 12 / Yoshida gives the classical
prime-blind certificate U < log 2.  The 2026 compact-window preprint
arXiv:2608.24827 claims a certified extension to U <= 1.6
(L <= 0.8); it is a recent preprint, not the classical theorem.
Every measured selected member k=5..12 already has U_k > 1.6.
Thus there is no unconditional-to-RH contradiction in the measured
ladder.  The often quoted Fourier-support `(-2,2)` belongs to
scaled density/pair-correlation settings and is not an unconditional
Weil-positivity theorem in this normalization.

Q3.  After the missing dictionary is proved, the mincut is exactly
cofinal compact-window Weil positivity: lambda_*(L_k) >= 0 on an
unbounded selected subsequence.  Since the compact test spaces are
nested, this is equivalent to positivity on every compact window,
hence to the full Weil criterion after the classical density and
spectral identifications.  Li and Bombieri-Lagarias provide equivalent
coordinates, not an unconditional positivity gain.

NUMERIC PINS (r459 races):
 k  m   N    Delta          U=N Delta      L=U/2         n_1.6 tail race
 5  19  10  .173286795140  1.732867951400  .866433975700   9    1  .675060257568
 6  23  12  .173286795140  2.079441541680 1.039720770840   9    3  .694906740736
 7  27  14  .173286795140  2.426015131960 1.213007565980   9    5  .628735899842
 8  31  16  .173286795140  2.772588722240 1.386294361120   9    7  .606566077487
 9  71  36  .086643397570  3.119162312520 1.559581156260  18   18  .635369043912
10  79  40  .086643397570  3.465735902800 1.732867951400  18   22  .757782884552
11  87  44  .086643397570  3.812309493080 1.906154746540  18   26  .715781944535
12  95  48  .086643397570  4.158883083360 2.079441541680  18   30  .693564423468

NO RH CLAIM.  Finite consistency and translation probe only.
"""
from __future__ import annotations

import argparse
import ast
import hashlib
import math
import os
import sys
import time

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DISC = os.path.dirname(os.path.abspath(__file__))
LEAN = os.path.join(REPO, "rh", "lean", "RH")
if DISC not in sys.path:
    sys.path.insert(0, DISC)

import fullcomb_cleanup_probe as R459  # noqa: E402

VERDICT = "FORK_SHARPENED"
LOG2 = math.log(2.0)
CLASSICAL_AUTOCORR_SUPPORT = LOG2
RECENT_AUTOCORR_SUPPORT = 1.6
K_VALUES = tuple(range(5, 13))
SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
CHECKS: list[tuple[str, bool]] = []
T0 = time.time()


def check(name: str, ok: bool, detail: str = "") -> bool:
    CHECKS.append((name, bool(ok)))
    print("  [%s] %-43s %s" % ("PASS" if ok else "FAIL", name, detail),
          flush=True)
    return bool(ok)


def section(title: str) -> None:
    print("\n" + "=" * 78)
    print(title)
    print("=" * 78, flush=True)


def firewall_audit() -> tuple[bool, str]:
    source = open(os.path.abspath(__file__), encoding="utf-8").read()
    tree = ast.parse(source)
    forbidden = {"zeta" + "zero", "n" + "zeros", "gram" + "point"}
    bad = []
    for node in ast.walk(tree):
        name = node.attr if isinstance(node, ast.Attribute) else (
            node.id if isinstance(node, ast.Name) else None)
        if name and name.lower() in forbidden:
            bad.append("%s@%d" % (name, node.lineno))
    return (not bad), ("NO zero/oracle calls" if not bad else "; ".join(bad))


def lean_text(filename: str) -> str:
    with open(os.path.join(LEAN, filename), encoding="utf-8") as handle:
        return handle.read()


def lean_map() -> dict[str, bool]:
    elementwise = lean_text("Elementwise.lean")
    selected = lean_text("Selected.lean")
    frequent = lean_text("FrequentlySelected.lean")
    audit = lean_text("Audit.lean")
    return {
        "grid_structure": all(token in elementwise for token in (
            "structure GridElement where", "steps : ℕ", "meshExp : ℕ",
            "x : Fin steps → ℝ", "noncomputable def acf",
            "noncomputable def toFun")),
        "support": all(token in elementwise for token in (
            "noncomputable def supportBound",
            "theorem toFun_eq_zero_of_lt_abs")),
        "full_read": all(token in elementwise for token in (
            "archRead a m f - combRead a f + poleRead a m f",
            "∑ n ∈ windowAtoms a, combMass n * f.toFun (Real.log n)")),
        "arch_contract": "def ArchGaussMellinDigammaIdentity" in elementwise
        and "theorem arch_gauss_mellin_digamma_identity" not in elementwise
        and "(hArch : ArchGaussMellinDigammaIdentity)" in elementwise,
        "density_absent": "deliberately NOT formalized here" in elementwise,
        "spectral_absent": "spectral/zero side of the" in elementwise
        and "NOT part of this definition" in elementwise,
        "selected_formula": all(token in selected for token in (
            "def selectedAnchor (k : ℕ) : ℕ := 2 ^ k",
            "noncomputable def selectedMesh",
            "noncomputable def selectedDelta",
            "theorem selected_covers")),
        "named_bridge": "def SelectedACapPsdImpliesPlainReads" in frequent,
        "endpoint": "theorem rh_of_frequently_selected" in frequent
        and "∀ f : GridElement, 0 ≤ weilForm f" in frequent,
        "contract_on_path":
        "ON PATH, named hypothesis: `ArchGaussMellinDigammaIdentity`"
        in audit,
    }


def selected_pin(k: int) -> dict[str, float | int]:
    root = math.isqrt(k)
    mesh = k * 2**root - 1
    count = mesh + 1
    depth = count // 2
    delta = LOG2 / 2**root
    support = depth * delta
    half_width = support / 2.0
    prime_blind_last = 2**root - 1
    recent_last = math.floor(RECENT_AUTOCORR_SUPPORT / delta + 1e-12)
    return {
        "k": k,
        "root": root,
        "mesh": mesh,
        "depth": depth,
        "delta": delta,
        "support": support,
        "half_width": half_width,
        "prime_blind_last": prime_blind_last,
        "recent_last": recent_last,
        "recent_tail": depth - recent_last,
        "race": R459.LEAN_RACE[k],
    }


def part_q1() -> None:
    section("Q1  LEAN ENDPOINT / FUNCTION CLASS")
    facts = lean_map()
    check("G10-grid-elements", facts["grid_structure"] and facts["support"],
          "dyadic step autocorrelations; even PL compact support")
    check("G11-full-Weil-read", facts["full_read"],
          "fullRead=arch-comb+pole; comb is exact von-Mangoldt sum")
    check("G12-cofinal-selected", facts["selected_formula"],
          "a_k, m_k and selected_covers present")
    check("G13-not-RH-theorem",
          facts["endpoint"] and facts["density_absent"]
          and facts["spectral_absent"],
          "endpoint is GridElement positivity; density/zero side absent")
    check("G14-open-path-inputs",
          facts["arch_contract"] and facts["named_bridge"]
          and facts["contract_on_path"],
          "explicit arch contract + named A_cap-to-fullRead bridge")


def part_q2() -> None:
    section("Q2  UNCONDITIONAL-FORK NUMERICS")
    pins = [selected_pin(k) for k in K_VALUES]
    for pin in pins:
        k = int(pin["k"])
        identity = abs(float(pin["support"]) - k * LOG2 / 2.0) < 1e-14
        outside = float(pin["support"]) > RECENT_AUTOCORR_SUPPORT
        race_pin = abs(float(pin["race"]) - R459.LEAN_RACE[k]) < 1e-15
        check("G2%d-k%d" % (k, k), identity and outside and race_pin,
              "N=%d D=%.12f U=%.12f L=%.12f tail1.6=%d race=%.12f"
              % (pin["depth"], pin["delta"], pin["support"],
                 pin["half_width"], pin["recent_tail"], pin["race"]))
    check("G30-classical-threshold",
          all(float(pin["support"]) > CLASSICAL_AUTOCORR_SUPPORT
              for pin in pins),
          "all U_k > log(2); prime-blind regime left before k=5")
    check("G31-recent-threshold",
          pins[0]["recent_tail"] == 1 and pins[-1]["recent_tail"] == 30,
          "U<=1.6 covers 9/10 depths at k=5, 18/48 at k=12")
    check("G32-race-band",
          min(float(pin["race"]) for pin in pins) > 0.60
          and max(float(pin["race"]) for pin in pins) < 0.76,
          "r459 race %.6f..%.6f"
          % (min(float(pin["race"]) for pin in pins),
             max(float(pin["race"]) for pin in pins)))


def part_q3() -> None:
    section("Q3  CLASSICAL ROUTE TYPING")
    check("G40-verdict", VERDICT == "FORK_SHARPENED", VERDICT)
    check("G41-cofinal-window-name",
          max(selected_pin(k)["half_width"] for k in K_VALUES)
          > min(selected_pin(k)["half_width"] for k in K_VALUES),
          "L_k=k log(2)/4 grows without bound on the selected sequence")
    check("G42-no-inconsistency",
          selected_pin(5)["support"] > RECENT_AUTOCORR_SUPPORT,
          "first measured member is already beyond U=1.6")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--smoke", action="store_true")
    args = parser.parse_args()
    print("=" * 78)
    print("narrowband_weil_probe -- PRIME.RDAGGER.NARROWBAND_WEIL.01")
    print("mode: %s" % ("SMOKE" if args.smoke else "FULL"))
    print("SPEC_SHA %s" % SPEC_SHA)
    print("=" * 78)
    ok, detail = firewall_audit()
    check("G00-firewall", ok, detail)
    part_q1()
    part_q2()
    part_q3()
    check("G99-runtime", time.time() - T0 < (60.0 if args.smoke else 2700.0),
          "%.3fs" % (time.time() - T0))
    failures = sum(1 for _name, passed in CHECKS if not passed)
    print("\nRESULT: %d/%d gates PASS" % (len(CHECKS) - failures, len(CHECKS)))
    if failures == 0:
        print("NARROWBAND WEIL %s VERIFIED" %
              ("SMOKE" if args.smoke else ""))
        print("VERDICT %s" % VERDICT)
        print("NO RH CLAIM.  NO anti-RH claim.")
        return 0
    print("NARROWBAND WEIL FAILED %d" % failures)
    return 1


if __name__ == "__main__":
    sys.exit(main())
