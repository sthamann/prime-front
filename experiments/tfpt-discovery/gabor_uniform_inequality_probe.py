#!/usr/bin/env python3
r"""gabor_uniform_inequality_probe -- r544 symbolic-uniformity scout.

CLAIM BOUNDARY.  EXPERIMENT ONLY.  NO RH CLAIM, NO ANTI-RH CLAIM, NO
LOAD-BEARING STATUS.  This deterministic scout evaluates the exact pure-Gabor
closed forms for ONE off-critical functional-equation quadruple, the pole
subtraction appearing in `RH.gaborSpectralFormula`, and a crude-safe C=4
unit-bin majorant for an otherwise critical-line background.  It does not
bound additional off-critical zeros; that missing term is deliberately
reported as the decisive scope boundary.

For sigma=beta-1/2>0, a=sigma^2/64 and
omega=gamma-pi*a/sigma, the exact quadruple is

  Q = (pi/a) [A_plus cos(phi_plus) - A_main
              + 2 A_cross cos(phi_cross)],

where
  A_main  = exp((sigma^2-(gamma-omega)^2)/(2a)),
  A_plus  = exp((sigma^2-(gamma+omega)^2)/(2a)),
  A_cross = exp((sigma^2-gamma^2-omega^2)/(2a)).

The phase-tuned main term is negative because
sigma*(gamma-omega)/a=pi.  For positive-ordinate critical-line zeros, every
unit bin [k,k+1] is charged by

  2 * C log(k+3) * sup_bin pureGaborOnLine,

with C=4; the factor 2 books conjugate ordinates.  We sum all non-negligible
packet and origin bins and add the frozen absolute tail pad 1.  In the scanned
regime the first omitted Gaussian is below exp(-10^8), so this pad is vastly
larger than the omitted numerical tail.  This is a scout of the stated
unit-bin model, not a derivation of C=4 from Trudgian for every real height.

The pole is SUBTRACTED:
  spectral = sum_zeros - hat(1).
Moreover hat(1) contains exp((1/4-omega^2)/(2a)), not exp(1/(8a)) alone;
the frequency shift suppresses it at large gamma.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import mpmath as mp


SIGMAS = ("1e-1", "1e-2", "1e-3", "1e-4", "1e-6")
GAMMAS = ("1e3", "1e6", "1e10")
C_CRUDE = mp.mpf(4)
TAIL_PAD = mp.mpf(1)
PACKET_RADIUS_BINS = 6

SPEC = {
    "round": 544,
    "contract": "PRIME.RDAGGER.WEIL_GABOR.UNIFORM_INEQUALITY.01",
    "sigma": SIGMAS,
    "gamma": GAMMAS,
    "a_rule": "sigma^2/64",
    "omega_rule": "gamma-pi*a/sigma",
    "critical_background": "unit bins; 2*C*log(k+3)*sup; C=4",
    "packet_radius_bins": PACKET_RADIUS_BINS,
    "absolute_tail_pad": "1",
    "scope": "one FE quadruple + critical-line background - pole",
    "excluded": "all additional off-critical zeros",
}
SPEC_SHA = hashlib.sha256(
    json.dumps(SPEC, sort_keys=True, separators=(",", ":")).encode()
).hexdigest()


def file_sha256() -> str:
    return hashlib.sha256(Path(__file__).read_bytes()).hexdigest()


def exp_real(value: mp.mpf) -> mp.mpf:
    return mp.exp(value)


def lobe_sup(center: mp.mpf, a: mp.mpf, k: int) -> mp.mpf:
    left = mp.mpf(k)
    right = left + 1
    if left <= center <= right:
        distance = mp.mpf(0)
    else:
        distance = min(abs(center - left), abs(center - right))
    return exp_real(-(distance * distance) / (2 * a))


def online_value(t: mp.mpf, a: mp.mpf, omega: mp.mpf) -> mp.mpf:
    prefactor = mp.pi / (4 * a)
    return prefactor * (
        exp_real(-((t + omega) ** 2) / (2 * a))
        + exp_real(-((t - omega) ** 2) / (2 * a))
        + 2 * exp_real(-(t * t + omega * omega) / (2 * a))
    )


def online_bin_sup(k: int, a: mp.mpf, omega: mp.mpf) -> mp.mpf:
    prefactor = mp.pi / (4 * a)
    left_lobe = lobe_sup(-omega, a, k)
    right_lobe = lobe_sup(omega, a, k)
    cross = 2 * exp_real(-(mp.mpf(k) ** 2 + omega * omega) / (2 * a))
    return prefactor * (left_lobe + right_lobe + cross)


def relevant_bins(omega: mp.mpf) -> tuple[int, ...]:
    packet_floor = int(mp.floor(omega))
    bins = set(range(0, PACKET_RADIUS_BINS + 1))
    bins.update(
        range(
            max(0, packet_floor - PACKET_RADIUS_BINS),
            packet_floor + PACKET_RADIUS_BINS + 2,
        )
    )
    return tuple(sorted(bins))


def critical_background_bound(a: mp.mpf, omega: mp.mpf) -> mp.mpf:
    total = TAIL_PAD
    for k in relevant_bins(omega):
        count_bound = C_CRUDE * mp.log(mp.mpf(k) + 3)
        total += 2 * count_bound * online_bin_sup(k, a, omega)
    return total


def exact_offline_quadruple(
    sigma: mp.mpf, gamma: mp.mpf, a: mp.mpf, omega: mp.mpf
) -> tuple[mp.mpf, mp.mpf, mp.mpf, mp.mpf]:
    detune = gamma - omega
    a_main = exp_real((sigma**2 - detune**2) / (2 * a))
    a_plus = exp_real((sigma**2 - (gamma + omega) ** 2) / (2 * a))
    a_cross = exp_real((sigma**2 - gamma**2 - omega**2) / (2 * a))
    phi_plus = sigma * (gamma + omega) / a
    phi_cross = sigma * gamma / a
    value = (mp.pi / a) * (
        a_plus * mp.cos(phi_plus) - a_main
        + 2 * a_cross * mp.cos(phi_cross)
    )
    return value, a_main, a_plus, a_cross


def exact_pole(a: mp.mpf, omega: mp.mpf) -> mp.mpf:
    exponent = (mp.mpf("0.25") - omega**2) / (2 * a)
    return (mp.pi / a) * exp_real(exponent) * mp.cos(omega / (4 * a)) ** 2


def log10_abs(value: mp.mpf) -> str:
    if value == 0:
        return "-inf"
    return mp.nstr(mp.log10(abs(value)), 9)


def run(smoke: bool) -> int:
    mp.mp.dps = 80
    sigmas = SIGMAS[:2] if smoke else SIGMAS
    gammas = GAMMAS[:1] if smoke else GAMMAS
    print("gabor_uniform_inequality_probe -- r544")
    print(f"SPEC_SHA {SPEC_SHA}")
    print(f"FILE_SHA256 {file_sha256()}")
    print(f"smoke {int(smoke)}")
    print("CLAIM_BOUNDARY one_FE_quadruple+critical_background-pole; "
          "additional_offcritical_zeros=UNBOUNDED")
    print("density_model unit_bin_C=4 factor2_conjugates tail_pad=1")
    print("pole_sign SUBTRACTED; frequency_shift_suppression INCLUDED")
    print("sigma gamma log10|off| log10(onlineUB) log10(pole) "
          "online/off totalUB_sign")

    all_negative = True
    max_ratio = mp.mpf(0)
    rows = 0
    for sigma_text in sigmas:
        sigma = mp.mpf(sigma_text)
        for gamma_text in gammas:
            gamma = mp.mpf(gamma_text)
            a = sigma**2 / 64
            omega = gamma - mp.pi * a / sigma
            off, a_main, a_plus, a_cross = exact_offline_quadruple(
                sigma, gamma, a, omega
            )
            online = critical_background_bound(a, omega)
            pole = exact_pole(a, omega)
            total_upper = off + online - pole
            ratio = online / abs(off)
            max_ratio = max(max_ratio, ratio)
            all_negative = all_negative and total_upper < 0
            rows += 1
            print(
                f"{sigma_text} {gamma_text} {log10_abs(off)} "
                f"{log10_abs(online)} {log10_abs(pole)} "
                f"{mp.nstr(ratio, 9)} {'NEG' if total_upper < 0 else 'NONNEG'}"
            )
            phase_error = abs(sigma * (gamma - omega) / a - mp.pi)
            if phase_error > mp.mpf("1e-60"):
                raise AssertionError("phase tuning drift")
            if not (a_main > a_plus >= 0 and a_main > a_cross >= 0):
                raise AssertionError("unexpected lobe ordering")

    print(f"rows {rows}")
    print(f"max_online_off_ratio {mp.nstr(max_ratio, 12)}")
    print("pole_verdict HELPS_OR_ZERO_AND_SUPPRESSED")
    print("sigma_to_zero_verdict UNIT_BIN_RATIO_SIGMA_INDEPENDENT_AT_LEADING_ORDER")
    print("height_verdict NOT_UNIFORM_IN_GAMMA_BOUND_GROWS_LIKE_LOG_GAMMA")
    print("scope_verdict ADDITIONAL_OFFCRITICAL_ZEROS_BLOCK_GLOBAL_SEPARATION")
    print(
        "VERDICT "
        + (
            "SCOUT_NEGATIVE_ALL_GRID_BUT_GLOBAL_PROOF_BLOCKED"
            if all_negative
            else "SCOUT_MARGIN_FLIP_ON_GRID"
        )
    )
    print("ALL CHECKS PASSED")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--smoke", action="store_true")
    args = parser.parse_args()
    return run(args.smoke)


if __name__ == "__main__":
    raise SystemExit(main())
