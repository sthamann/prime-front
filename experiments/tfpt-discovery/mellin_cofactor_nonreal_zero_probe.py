#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""mellin_cofactor_nonreal_zero_probe -- MELLIN.COFACTOR.NONREAL-ZERO.01

FROZEN SPEC v1 (2026-09-03).  EXPLORATION ONLY.

Certifies non-real zeros of the Mellin transform of the Riemann kernel,

    M(s) = integral_0^infinity Phi(u) u^s du,      F(z) = 2 M(2z-1),
    H(z) = F(z) / Gamma(z)   (entire Mellin cofactor),

with Phi normalised as in mellin_pick_zero_residue2_probe (half of Polya's
Phi; zeros are unaffected).  Off the non-positive integers 1/Gamma is
zero-free, so every non-real zero of F is a non-real zero of H.

WHY THIS MATTERS (mechanism, not a claim about RH)
    Xi(2 sqrt(x)) / 2 = sqrt(pi) * sum_k H(k+1/2) (-x)^k / k!.
By Polya--Schur, RH is equivalent to {H(k+1/2)}_k being a multiplier
sequence.  Laguerre's theorem (and de Bruijn 1950 in the form quoted as
KPS Theorem 3.11) gives the SUFFICIENT condition "the interpolant H has
only negative real zeros".  A single certified non-real zero of H shows
that this sufficient condition is not available for the Riemann kernel.

CERTIFICATE
    Interval Newton for the analytic function F on a complex box X:
    F(z0) evaluated at the midpoint, F'(X) enclosed over the whole box
    (ball-parametric rigorous integration + explicit pole sum).  If
    0 not in F'(X) and N(X) = z0 - F(z0)/F'(X) is contained in X, then F
    has exactly one zero in X.  Convexity of the ball F'(X) makes the
    mean-value argument valid for complex analytic F.

NON-CLAIMS
    Nothing here is load-bearing: no ledger, paper, Lean, website or
    verification claim.  This does not bear on the truth of RH.  It only
    closes one sufficient criterion for the specific kernel Phi.
"""
from __future__ import annotations

import importlib.util
import json
import sys
import time
from pathlib import Path

from flint import acb, arb

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "mellin_pick_zero_residue2_probe.py"
RESULT = HERE / "mellin_cofactor_nonreal_zero_result.json"

# Frozen inputs -------------------------------------------------------------
TAYLOR_MARGIN = 40          # tightens the analytic [0,DELTA_LOW] remainder box
NEWTON_STEPS = 6
BOX_RADIUS = "1e-13"
CANDIDATES = (               # scouted by quadtree winding numbers + Newton
    ("-7.994182256992558", "2.937767068567584"),
    ("-11.625061166698821", "6.838174857484421"),
    ("-20.353775220110890", "4.583241657454611"),
)


def load_source():
    spec = importlib.util.spec_from_file_location("mellin_zr2_source", SOURCE)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    module.configure(smoke=False)
    module.TAYLOR_MARGIN = TAYLOR_MARGIN
    return module


def F_ball(g, z: acb, derivative: int) -> acb:
    """Enclosure of F^(derivative)(z) for every point of the ball z."""
    parts = g.eval_R(z, derivative)
    if not parts.ok:
        return acb("nan")
    coeffs = g.taylor_even_coeffs(parts.n_terms)
    pole = acb(0)
    for j in range(parts.n_terms):
        den = z + acb(j)
        if den.contains(0):
            return acb("nan")
        pole += coeffs[j] / den if derivative == 0 else -coeffs[j] / (den * den)
    return parts.total + pole


def midpoint(z: acb) -> acb:
    return acb(arb(z.real.mid()), arb(z.imag.mid()))


def certify(g, re: str, im: str) -> dict:
    t0 = time.time()
    z0 = acb(re, im)
    for _ in range(NEWTON_STEPS):
        f0 = F_ball(g, z0, 0)
        f1 = F_ball(g, z0, 1)
        if not (f0.is_finite() and f1.is_finite()) or f1.contains(0):
            return {"input": [re, im], "verdict": "INCONCLUSIVE(newton_failed)"}
        z0 = midpoint(z0 - f0 / f1)
    f0 = F_ball(g, z0, 0)
    radius = arb(BOX_RADIUS)
    box = acb(arb(z0.real.mid(), radius), arb(z0.imag.mid(), radius))
    f1_box = F_ball(g, box, 1)
    record = {
        "input": [re, im],
        "zero_midpoint": [z0.real.mid().str(20, radius=False), z0.imag.mid().str(20, radius=False)],
        "box_radius": BOX_RADIUS,
        "abs_F_at_midpoint_upper": f0.abs_upper().str(3),
        "seconds": round(time.time() - t0, 2),
    }
    if not f1_box.is_finite() or f1_box.contains(0):
        record["verdict"] = "INCONCLUSIVE(derivative_box_contains_zero)"
        return record
    newton_image = z0 - f0 / f1_box
    contained = box.real.contains(newton_image.real) and box.imag.contains(newton_image.imag)
    im_positive = box.imag.lower() > 0
    record.update({
        "abs_Fprime_box_lower": f1_box.abs_lower().str(3),
        "newton_image_radius": "%.2e" % max(float(newton_image.real.rad()), float(newton_image.imag.rad())),
        "newton_image_in_box": bool(contained),
        "imaginary_part_certainly_positive": bool(im_positive),
    })
    if contained and im_positive:
        record["verdict"] = "NONREAL_ZERO_CERTIFIED"
        s = acb(2) * z0 - acb(1)
        record["mellin_variable_s_midpoint"] = [s.real.mid().str(20, radius=False), s.imag.mid().str(20, radius=False)]
    else:
        record["verdict"] = "INCONCLUSIVE(newton_image_not_contained)"
    return record


def main() -> int:
    g = load_source()
    records = [certify(g, re, im) for re, im in CANDIDATES]
    certified = [r for r in records if r["verdict"] == "NONREAL_ZERO_CERTIFIED"]
    verdict = "NONREAL_ZEROS_CERTIFIED(%d)" % len(certified) if certified else "INCONCLUSIVE"
    out = {
        "contract": "MELLIN.COFACTOR.NONREAL-ZERO.01",
        "spec": "FROZEN SPEC v1 (2026-09-03)",
        "status": "exploration_only",
        "source_module": SOURCE.name,
        "taylor_margin": TAYLOR_MARGIN,
        "verdict": verdict,
        "zeros": records,
        "consequence": (
            "H(z)=2M(2z-1)/Gamma(z) has non-real zeros, hence H is not in the "
            "Laguerre-Polya class with negative zeros; the Laguerre/de Bruijn "
            "sufficient multiplier-sequence criterion (KPS Thm 3.11) does not "
            "apply to the Riemann kernel.  No statement about RH itself."
        ),
    }
    RESULT.write_text(json.dumps(out, indent=2) + "\n")
    for r in records:
        print("%-38s %s" % (r["verdict"], r.get("zero_midpoint", r["input"])))
    print("VERDICT", verdict)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
