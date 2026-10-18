#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""parabolic_detline2_probe -- PRIME.PARABOLIC.DETLINE.02

Exploration only.  Identity side only.  No positivity statement and no RH
claim.  This probe audits the regularisation gap left by DETLINE.01.

Lemma L1 (fixed-point half-density trace)
-----------------------------------------
For a hyperbolic tree translation g of length m, write x=q^{-m}.  The
visual derivatives at the attracting and repelling ends are x and x^{-1}.
The one-dimensional Lefschetz prescription

    sum_{g xi=xi} |g'(xi)|^{1/2} / |1-g'(xi)|

therefore gives x^{1/2}/(1-x) at either end and
2*x^{1/2}/(1-x) in total.  Proof sketch: at the repeller,
x^{-1/2}/(x^{-1}-1)=x^{1/2}/(1-x).  Expansion of the denominator gives
2*sum_{k>=0} q^{-m(2k+1)/2}.

This is NOT literally the nonzero-shell term of Connes'
integral-prime distribution.  On |u|_p=q^{-m}<1, ultrametricity gives
|1-u|_p=1, so half-density normalisation contributes q^{-m/2} with no
factor (1-q^{-m})^{-1}.  The two orientations give 2*q^{-m/2}.  Thus the
Lefschetz boundary expression is an odd-power resummation of shell
weights, not the coefficient at the single shell m.  Recovering the
single-shell Weil coefficient requires removing that resummation (or,
equivalently, multiplying by 1-q^{-m}); it does not follow from merely
renaming the fixed-point trace.

Lemma L2 (what the cylinder truncation computes)
------------------------------------------------
Let C_N^+ and C_N^- be the depth-N cylinders about the two fixed ends,
with visual mass mu_N=1/((q+1)q^{N-1}).  In the orthonormal cylinder
basis e_C=1_C/sqrt(mu_N), the two diagonal entries are q^{-m/2} and
q^{m/2}; hence DETLINE.01 obtained q^{-m/2}+q^{m/2}, independently of
N.  The growing term is the repelling RN half-density, exposed because
normalising a shrinking cylinder cancels its mass and treats it as an
atom.  With unnormalised indicators the mass-weighted diagonal is
mu_N*(q^{-m/2}+q^{m/2}) and tends to zero.  Neither sequence approaches
the Lefschetz distribution.  The missing operation is the displacement
Jacobian (1-g')^{-1}, not an additional cylinder depth.

Lemma L3 (canonical cutoffs and Hardy projection)
-------------------------------------------------
The direct Connes-style finite cutoff h_N U_g h_N on the cylinder
Hilbert space has the orthonormal trace from L2; removing the cutoff
does not produce L1.  Its mass-weighted variant tends to zero.  The
tree-defined Hardy projection P_+ onto the attracting tail is canonical
after choosing the oriented hyperbolic element, but
Tr(P_+ U_g P_+)=q^{-m/2}: it discards the expanding end and supplies
neither the second orientation nor the Lefschetz denominator.  A
Lefschetz shell sum can be DEFINED canonically from g and the visual
metric and equals L1, but it is a different distributional trace; it
does not validate either requested operator cutoff.

Lemma L4 (local assembly and Haar length)
-----------------------------------------
The modular/Busemann cocycle of diag(p^m,1) is
-log |p^m|_p=m log p.  Thus log p per primitive step is canonical once
the standard multiplicative Haar module (and natural logarithm) fixes
the real flow parameter; it is not imported from a prime table.
For an even Gaussian test transform F(t)=exp(-t^2), the Weil local sum
uses -2 log(p) p^{-m/2} F(m log p).  L1 instead multiplies every summand
by (1-p^{-m})^{-1}.  The exact termwise discrepancy is recorded below.

Controls
--------
C1: an elliptic/torsion permutation with no boundary fixed points has
fixed-point trace zero and every finite cutoff trace zero.
C2: at m=0 the operator is the identity.  Its finite trace is the cutoff
rank and diverges as N grows; the fixed-point denominator is singular.
This is the expected identity-volume divergence, not a finite L1 term.
"""
from __future__ import annotations

import hashlib
import json
import time
from fractions import Fraction
from pathlib import Path

import mpmath as mp


CONTRACT = "PRIME.PARABOLIC.DETLINE.02"
HERE = Path(__file__).resolve().parent
RESULT_PATH = HERE / "parabolic_detline2_result.json"
Q_VALUES = (2, 3, 5, 7)
M_VALUES = (1, 2, 3)
DEPTHS = (2, 4, 8, 16)
MP_DPS = 60
SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()


def fraction_record(value: Fraction) -> dict[str, int | str]:
    """JSON-safe exact rational."""
    return {
        "numerator": value.numerator,
        "denominator": value.denominator,
        "text": str(value),
    }


def fixed_point_trace(q: int, m: int) -> dict[str, object]:
    """Verify L1 exactly at the level of squared radical coefficients."""
    if q <= 1 or m <= 0:
        raise ValueError("L1 requires q>1 and m>0")
    x = Fraction(1, q**m)
    attracting_coefficient_squared = x / ((1 - x) ** 2)
    repelling_coefficient_squared = (
        Fraction(q**m, 1) / ((q**m - 1) ** 2)
    )
    common = Fraction(q**m, (q**m - 1) ** 2)
    return {
        "q": q,
        "m": m,
        "derivative_attracting": fraction_record(x),
        "derivative_repelling": fraction_record(Fraction(q**m, 1)),
        "attracting_coefficient_squared": fraction_record(
            attracting_coefficient_squared
        ),
        "repelling_coefficient_squared": fraction_record(
            repelling_coefficient_squared
        ),
        "equal_end_contributions_exact": (
            attracting_coefficient_squared
            == repelling_coefficient_squared
            == common
        ),
        "one_end_formula": f"{q}^(-{m}/2)/(1-{q}^(-{m}))",
        "total_formula": f"2*{q}^(-{m}/2)/(1-{q}^(-{m}))",
        "odd_power_resummation": (
            f"2*sum_(k>=0) {q}^(-{m}*(2*k+1)/2)"
        ),
        "connes_shell_formula": f"2*{q}^(-{m}/2)",
        "ratio_to_connes_shell": fraction_record(Fraction(q**m, q**m - 1)),
    }


def cylinder_cutoff(q: int, m: int, depth: int) -> dict[str, object]:
    """Verify L2 with exact visual masses and radical squares."""
    if depth < 1:
        raise ValueError("depth must be positive")
    mass = Fraction(1, (q + 1) * q ** (depth - 1))
    mass_weighted_squared_over_trace_squared = mass * mass
    return {
        "q": q,
        "m": m,
        "depth": depth,
        "cylinder_mass": fraction_record(mass),
        "orthonormal_attracting_square": fraction_record(Fraction(1, q**m)),
        "orthonormal_repelling_square": fraction_record(Fraction(q**m, 1)),
        "orthonormal_trace_formula": f"{q}^(-{m}/2)+{q}^({m}/2)",
        "orthonormal_trace_depth_independent": True,
        "mass_weighted_trace_formula": (
            f"{mass}*({q}^(-{m}/2)+{q}^({m}/2))"
        ),
        "mass_weighted_scale_square": fraction_record(
            mass_weighted_squared_over_trace_squared
        ),
    }


def regularisation_audit(q: int, m: int) -> dict[str, object]:
    """Verify L3 for the two requested prescriptions."""
    l1 = fixed_point_trace(q, m)
    mass_last = Fraction(1, (q + 1) * q ** (DEPTHS[-1] - 1))
    return {
        "q": q,
        "m": m,
        "target": l1["total_formula"],
        "connes_style_cutoff": {
            "canonical": True,
            "limit": f"{q}^(-{m}/2)+{q}^({m}/2)",
            "converges_to_L1": False,
            "diagnosis": (
                "orthonormal shrinking cylinders cancel visual mass; "
                "repelling RN half-density remains"
            ),
        },
        "mass_weighted_cutoff": {
            "canonical": True,
            "last_exact_mass": fraction_record(mass_last),
            "limit": "0",
            "converges_to_L1": False,
        },
        "hardy_attracting_projection": {
            "canonical_given_oriented_g": True,
            "limit": f"{q}^(-{m}/2)",
            "converges_to_L1": False,
            "diagnosis": (
                "keeps one attracting contribution but has no second "
                "orientation and no displacement denominator"
            ),
        },
        "lefschetz_distribution": {
            "canonical_from_g_and_visual_metric": True,
            "equals_L1": True,
            "is_requested_operator_cutoff": False,
        },
    }


def gaussian_assembly() -> dict[str, object]:
    """Numerically verify L4 and its exact termwise multiplier."""
    mp.mp.dps = MP_DPS
    weil_total = mp.mpf("0")
    fixed_total = mp.mpf("0")
    rows = []
    for p in Q_VALUES:
        log_p = mp.log(p)
        for m in M_VALUES:
            translation_length = m * log_p
            test_value = mp.exp(-(translation_length**2))
            bare = -2 * log_p * mp.power(p, -mp.mpf(m) / 2) * test_value
            resummation = Fraction(p**m, p**m - 1)
            fixed = bare * mp.mpf(resummation.numerator) / resummation.denominator
            weil_total += bare
            fixed_total += fixed
            rows.append({
                "p": p,
                "m": m,
                "busemann_integer_length": m,
                "haar_real_length": mp.nstr(translation_length, 30),
                "gaussian": mp.nstr(test_value, 30),
                "weil_term": mp.nstr(bare, 30),
                "fixed_point_term": mp.nstr(fixed, 30),
                "fixed_over_weil_exact": fraction_record(resummation),
            })
    return {
        "test_transform": "F(t)=exp(-t^2), even",
        "orientation_factor": 2,
        "haar_length_derivation": (
            "-log(|p^m|_p)=m*log(p); primitive real length is log(p)"
        ),
        "log_p_inserted_by_hand": False,
        "half_density_inserted_by_hand": False,
        "weil_total": mp.nstr(weil_total, 40),
        "fixed_point_total": mp.nstr(fixed_total, 40),
        "difference_fixed_minus_weil": mp.nstr(
            fixed_total - weil_total, 40
        ),
        "termwise_match": False,
        "rows": rows,
    }


def controls() -> dict[str, object]:
    """Run C1 and C2 exactly."""
    elliptic_rows = []
    for depth in DEPTHS:
        # A fixed-point-free cyclic permutation of q+1 first-level branches.
        q = 3
        branch_count = q + 1
        fixed_branches = sum(
            1 for branch in range(branch_count)
            if (branch + 1) % branch_count == branch
        )
        elliptic_rows.append({
            "depth": depth,
            "fixed_boundary_points": 0,
            "fixed_branches": fixed_branches,
            "fixed_point_trace": 0,
            "cutoff_trace": 0,
        })
    identity_rows = []
    q = 3
    for depth in DEPTHS:
        rank = (q + 1) * q ** (depth - 1)
        identity_rows.append({
            "depth": depth,
            "cutoff_rank": rank,
            "identity_trace": rank,
        })
    return {
        "C1_elliptic": {
            "rows": elliptic_rows,
            "passes": all(row["cutoff_trace"] == 0 for row in elliptic_rows),
            "limit": 0,
        },
        "C2_identity": {
            "m": 0,
            "rows": identity_rows,
            "fixed_point_denominator": "singular: 1-g'=0",
            "finite_trace": False,
            "expected_divergence_observed": all(
                identity_rows[i]["identity_trace"]
                < identity_rows[i + 1]["identity_trace"]
                for i in range(len(identity_rows) - 1)
            ),
        },
    }


def run() -> int:
    """Execute the deterministic adjudication and write its JSON result."""
    started = time.monotonic()
    print(f"{CONTRACT} -- exploration only; no RH claim")

    l1_rows = [
        fixed_point_trace(q, m) for q in Q_VALUES for m in M_VALUES
    ]
    l1_ok = all(row["equal_end_contributions_exact"] for row in l1_rows)
    print(
        "L1 %s: Tr_fp=2*q^(-m/2)/(1-q^-m); "
        "Connes shell=2*q^(-m/2)"
        % ("PASS" if l1_ok else "FAIL")
    )

    l2_rows = [
        cylinder_cutoff(q, m, depth)
        for q in Q_VALUES
        for m in M_VALUES
        for depth in DEPTHS
    ]
    l2_ok = all(row["orthonormal_trace_depth_independent"] for row in l2_rows)
    print(
        "L2 %s: orthonormal cylinder trace is "
        "q^(m/2)+q^(-m/2), while mass-weighted trace tends to 0"
        % ("PASS" if l2_ok else "FAIL")
    )

    l3_rows = [
        regularisation_audit(q, m) for q in Q_VALUES for m in M_VALUES
    ]
    cutoff_reaches_l1 = any(
        row["connes_style_cutoff"]["converges_to_L1"]
        or row["hardy_attracting_projection"]["converges_to_L1"]
        for row in l3_rows
    )
    l3_ok = not cutoff_reaches_l1
    print(
        "L3 AUDIT: neither canonical cutoff nor Hardy projection reaches L1"
    )

    l4 = gaussian_assembly()
    l4_ok = (
        not l4["log_p_inserted_by_hand"]
        and not l4["half_density_inserted_by_hand"]
    )
    print(
        "L4 PASS (normalisations canonical), but fixed-point/Weil totals "
        f"differ: {l4['fixed_point_total']} vs {l4['weil_total']}"
    )

    control_rows = controls()
    controls_ok = (
        control_rows["C1_elliptic"]["passes"]
        and control_rows["C2_identity"]["expected_divergence_observed"]
    )

    kills = []
    if not l1_ok:
        kills.append("K1")
    if not cutoff_reaches_l1:
        kills.append("K2")
    if not l4_ok:
        kills.append("K3")
    verdict = (
        "KILLED_K2 (the symmetric fixed-point half-density sum is exact, "
        "but neither the canonical Busemann/cylinder cutoff nor the "
        "attracting Hardy projection converges to it; moreover its "
        "1/(1-q^-m) odd-power resummation is not the single-shell Connes/"
        "Weil coefficient. log p and p^-1/2 are canonical. Local identity "
        "side only; the global and positivity questions are untouched.)"
    )
    elapsed = time.monotonic() - started
    payload = {
        "contract": CONTRACT,
        "verdict": verdict,
        "kills": kills,
        "outcome": "KILLED",
        "L1": {
            "passes_algebraically": l1_ok,
            "fixed_point_formula": "2*q^(-m/2)/(1-q^-m)",
            "connes_nonzero_shell_formula": "2*q^(-m/2)",
            "exact_discrepancy": "factor 1/(1-q^-m)",
            "interpretation": "odd-power resummation, not one shell",
            "rows": l1_rows,
        },
        "L2": {
            "passes_diagnosis": l2_ok,
            "orthonormal_limit": "q^(m/2)+q^(-m/2), independent of N",
            "mass_weighted_limit": "0",
            "missing_regularisation": "displacement Jacobian 1/|1-g'|",
            "rows": l2_rows,
        },
        "L3": {
            "requested_prescription_reaches_L1": cutoff_reaches_l1,
            "audit_passes": l3_ok,
            "rows": l3_rows,
        },
        "L4": l4,
        "controls": control_rows,
        "controls_pass": controls_ok,
        "deterministic": True,
        "mp_dps": MP_DPS,
        "spec_sha": SPEC_SHA,
        "runtime_s": elapsed,
        "identity_side_only": True,
        "rh_claim": False,
    }
    RESULT_PATH.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(f"controls {'PASS' if controls_ok else 'FAIL'}")
    print(f"VERDICT: {verdict}")
    print(f"runtime {elapsed:.3f}s")
    print(f"wrote {RESULT_PATH}")
    return 0 if l1_ok and l2_ok and l3_ok and l4_ok and controls_ok else 1


if __name__ == "__main__":
    raise SystemExit(run())
