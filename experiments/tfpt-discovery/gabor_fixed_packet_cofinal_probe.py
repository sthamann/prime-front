#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""gabor_fixed_packet_cofinal_probe -- r591

Round 591.  Experiments-only RETRY of r590 `GaborFixedPacketCofinalNegAt`
(prior attempts rate-limited; no leftover files).

  r549 ADVERSARIAL: σ′>σ flips via exp((σ′²−σ²)/2a).
  r551: equal-σ centre killer Q★/|Q_sel|≈1.08.
  r567: CANONICAL_DOMINANCE_HOLDS only with Z-dependent packet.
  r590 Lean: ∃ a ω δ>0, ∃ T0, ∀ T≥T0:
        gaborHonestWeil(a,ω, weighted FD trunc T) ≤ −δ
        (all strip zeros of height ≤T, host AND foreigners).

THIS ROUND.  Packet first (sees only host s=(σ,γ)); adversary then
places 1–4 compliance-capped foreigners; watch W(Z_T) as T grows.

CLAIM BOUNDARY.  Finite closed-form / deterministic-grid arithmetic
on increment-capped catalogs.  NO RH claim, NO anti-RH claim, NO
ledger/paper/Lean/verification/website edit.

HAT CONVENTION (byte-inherited from r567/r561/r560).  Weil-shifted
ĥ_W, Q = 4 Re ĥ_W
  Q(σ′,γ′) = (π/a)[A₊ cos φ₊ + A₋ cos φ₋ + 2 Aₓ cos φₓ],
  A± = exp((σ′²−(γ′∓ω)²)/(2a)),  Aₓ = exp((σ′²−γ′²−ω²)/(2a)),
  φ₊ = σ′(γ′+ω)/a,  φ₋ = σ′(γ′−ω)/a,  φₓ = σ′ γ′/a.
R_on = 2 C_inc S_cert, C_inc pin 174.818115823.
S_cert = (π/(4a))(Θ_lobe + Θ_left_pos + 2 Θ_cross_pos)  (r560).
Reduced units E = (π/a) exp(σ★²/2a).  Never form e^{σ²/2a} raw.
Amplitude-0 terms skip cos.

COMPLIANCE.  Per unit window at most
  K(γ′) = 2·(1+ln(|γ′|+3)) quadrupoles.  C=1 (documented; Lean
  log-kappe uses 2 C_inner(1+log); this probe uses C=1).

Scenarios:
  (a) strict  — foreign σ′ ≤ σ−0.02
  (b) weak    — foreign σ′ ≤ σ  (tie at packet centre allowed)
  (c) free    — foreign σ′ ≤ 0.49  (control, expected BREAK)

Verdicts per scenario:
  COFINAL_NEG_HOLDS / COFINAL_NEG_BREAKS(breaker) / MIXED
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
from pathlib import Path

os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("MKL_NUM_THREADS", "1")
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
os.environ.setdefault("NUMEXPR_NUM_THREADS", "1")

import numpy as np  # noqa: E402

# ---------------------------------------------------------------------------
# Frozen design.  SPEC_SHA is sha256 of the canonical JSON of SPEC.
# ---------------------------------------------------------------------------
C_INC_PIN = 174.818115823
SEED = 20260902
EXPO_LO = -745.0
EXPO_HI = 709.0
EPS_STRICT = 0.02
SIGMAS = (0.10, 0.25, 0.40)
GAMMAS = (14.0, 100.0, 1000.0)
A_KINDS = ("512", "1024", "64")
OMEGA_KINDS = ("phase", "center")
T_EXTRA = (100.0, 1000.0, 20000.0)
N_FOREIGN = 4
N_RASTER = 28
GAMMA_LO = 0.5
GAMMA_HI = 2.0e4
EPS_SCAN = (0.02, 0.01, 0.005, 0.001)
SCENARIOS = ("strict", "weak", "free")

SPEC = {
    "round": 591,
    "lean_target": "GaborFixedPacketCofinalNegAt",
    "parent_r567_sha_prefix": "c0781a08",
    "c_inc_pin": C_INC_PIN,
    "compliance": "K=2*(1+ln(|g|+3)); C=1",
    "seed": SEED,
    "sigmas": list(SIGMAS),
    "gammas": list(GAMMAS),
    "a_kinds": list(A_KINDS),
    "omega_kinds": list(OMEGA_KINDS),
    "t_extra": list(T_EXTRA),
    "n_foreign": N_FOREIGN,
    "eps_strict": EPS_STRICT,
    "scenarios": list(SCENARIOS),
    "form": "W = sum m Q + R_on; Q,R_on r567/r560 sealed",
    "quantifiers": "packet sees host only; adversary after; cofinal T",
}
SPEC_SHA = hashlib.sha256(
    json.dumps(SPEC, sort_keys=True, separators=(",", ":")).encode()
).hexdigest()

CHECKS: list[tuple[str, bool]] = []


def check(name: str, ok: bool, detail: str = "") -> bool:
    CHECKS.append((name, bool(ok)))
    print("  [%s] %-44s %s" % ("PASS" if ok else "FAIL", name, detail))
    return bool(ok)


def file_sha256() -> str:
    return hashlib.sha256(Path(__file__).resolve().read_bytes()).hexdigest()


def nstr(value: float, digits: int = 12) -> str:
    if not math.isfinite(value):
        return "inf" if value > 0 else ("-inf" if value < 0 else "nan")
    return "%.*e" % (digits, value)


def exp_clip(value: float) -> float:
    if value <= EXPO_LO:
        return 0.0
    if value >= EXPO_HI:
        return math.inf
    return math.exp(value)


def a_of(sigma: float, kind: str) -> float:
    return (sigma * sigma) / float(kind)


def omega_of(sigma: float, gamma: float, a_val: float, kind: str) -> float:
    if kind == "phase":
        return gamma - math.pi * a_val / sigma
    return gamma


def k_cap(gamma_p: float) -> int:
    """C=1 quadrupole cap per unit window: 2*(1+ln(|γ′|+3))."""
    return max(1, int(math.floor(2.0 * (1.0 + math.log(abs(gamma_p) + 3.0)))))


def theta3_q(a_val: float) -> float:
    q_log = -1.0 / (2.0 * a_val)
    total = 1.0
    m_val = 1
    while True:
        term = exp_clip((m_val * m_val) * q_log)
        if not math.isfinite(term):
            break
        total += 2.0 * term
        if term < 1e-80 or m_val > 200:
            m_next = m_val + 1
            gap = exp_clip(-(2.0 * m_val + 1.0) / (2.0 * a_val))
            if gap < 0.5:
                rem = 2.0 * exp_clip(-(m_next * m_next) / (2.0 * a_val))
                if gap < 1.0 and math.isfinite(rem):
                    rem = rem / (1.0 - gap) if (1.0 - gap) > 0.0 else 0.0
                    total += rem
            break
        m_val += 1
    return total


def theta_lobe(a_val: float) -> float:
    return 2.0 + theta3_q(a_val)


def theta_left_pos(a_val: float, omega: float) -> float:
    if omega <= 0.0:
        return theta_lobe(a_val)
    geom = exp_clip(-omega / a_val)
    if geom >= 0.5:
        return theta_lobe(a_val)
    return exp_clip(-(omega * omega) / (2.0 * a_val)) / (1.0 - geom)


def theta_cross_pos(a_val: float, omega: float) -> float:
    return exp_clip(-(omega * omega) / (2.0 * a_val)) * (1.0 + theta3_q(a_val)) / 2.0


def s_cert(a_val: float, omega: float) -> float:
    pref = math.pi / (4.0 * a_val)
    return pref * (
        theta_lobe(a_val)
        + theta_left_pos(a_val, omega)
        + 2.0 * theta_cross_pos(a_val, omega)
    )


def r_on(a_val: float, omega: float) -> float:
    return 2.0 * C_INC_PIN * s_cert(a_val, omega)


def q_reduced(
    sigma_p: float, t_value: float, a_val: float, omega: float, sigma_ref: float,
) -> float:
    """Q/E with E=(π/a) exp(σ_ref²/2a).  Sealed r567 phases."""
    scale = (sigma_p * sigma_p - sigma_ref * sigma_ref) / (2.0 * a_val)

    def lobe(dist_sq: float, phase: float, weight: float) -> float:
        amp = exp_clip(scale - dist_sq / (2.0 * a_val))
        if amp == 0.0:
            return 0.0
        if not math.isfinite(amp):
            return math.inf
        return weight * amp * math.cos(phase)

    plus = lobe((t_value + omega) ** 2, sigma_p * (t_value + omega) / a_val, 1.0)
    minus = lobe((t_value - omega) ** 2, sigma_p * (t_value - omega) / a_val, 1.0)
    cross = lobe(t_value ** 2 + omega ** 2, sigma_p * t_value / a_val, 2.0)
    return plus + minus + cross


def r_on_reduced(a_val: float, omega: float, sigma_ref: float) -> float:
    raw = r_on(a_val, omega)
    scale = - (sigma_ref * sigma_ref) / (2.0 * a_val)
    factor = (a_val / math.pi) * exp_clip(scale)
    if factor == 0.0:
        return 0.0
    if not math.isfinite(factor) or not math.isfinite(raw):
        return 0.0 if factor == 0.0 else math.inf
    return raw * factor


def log_raster(n_pts: int) -> np.ndarray:
    return np.geomspace(GAMMA_LO, GAMMA_HI, n_pts)


def targeted(omega: float, a_val: float, sigma: float) -> list[float]:
    width = a_val / sigma
    out = [omega, omega - width, omega + width, omega - 1.0, omega + 1.0]
    return [g for g in out if g >= GAMMA_LO]


def sigma_grid(scenario: str, sigma: float, eps: float) -> list[float]:
    if scenario == "strict":
        cap = sigma - eps
        if cap <= 1e-4:
            return [max(cap, 1e-4)]
        pts = [1e-2, 0.5 * cap, cap]
        if sigma - 0.05 > 1e-4:
            pts.append(min(sigma - 0.05, cap))
    elif scenario == "weak":
        cap = sigma
        pts = [1e-2, 0.5 * sigma, max(sigma - 0.01, 1e-2), cap]
    else:
        cap = 0.49
        pts = [1e-2, sigma, 0.5 * (sigma + cap), cap]
    uniq: list[float] = []
    for p in pts:
        q = min(max(p, 1e-4), cap)
        if all(abs(q - u) > 1e-12 for u in uniq):
            uniq.append(q)
    uniq.sort()
    return uniq


def t_grid(gamma: float, smoke: bool) -> list[float]:
    raw = [gamma + 10.0, *T_EXTRA]
    if smoke:
        raw = [gamma + 10.0, 20000.0]
    vals = sorted({t for t in raw if t > 0.0})
    return vals


def window_key(gamma_p: float) -> int:
    return int(math.floor(gamma_p))


def build_pool(
    sigma: float,
    a_val: float,
    omega: float,
    scenario: str,
    eps: float,
    n_pts: int,
) -> list[tuple[float, float, int, float]]:
    """(σ′, γ′, m_max, Q_red) foreigners, host excluded by (σ,γ) later."""
    heights = set(float(x) for x in log_raster(n_pts))
    heights.update(targeted(omega, a_val, sigma))
    sigs = sigma_grid(scenario, sigma, eps)
    pool: list[tuple[float, float, int, float]] = []
    for gp in sorted(heights):
        if not (GAMMA_LO <= gp <= GAMMA_HI):
            continue
        m_max = k_cap(gp)
        for sp in sigs:
            qv = q_reduced(sp, gp, a_val, omega, sigma)
            if qv > 0.0:
                pool.append((sp, gp, m_max, qv))
    pool.sort(key=lambda row: (-row[3], row[1], row[0]))
    return pool


def pick_foreigners(
    pool: list[tuple[float, float, int, float]],
    t_cut: float,
    host_gamma: float,
    host_in: bool,
    k_max: int,
) -> list[tuple[float, float, int, float]]:
    used: dict[int, int] = {}
    if host_in:
        used[window_key(host_gamma)] = 1
    picked: list[tuple[float, float, int, float]] = []
    for sp, gp, m_max, qv in pool:
        if gp > t_cut:
            continue
        if len(picked) >= k_max:
            break
        wk = window_key(gp)
        cap = k_cap(float(wk) + 0.5)
        already = used.get(wk, 0)
        room = cap - already
        if room <= 0:
            continue
        m_use = min(m_max, room)
        if m_use <= 0:
            continue
        picked.append((sp, gp, m_use, qv))
        used[wk] = already + m_use
    return picked


def w_reduced_at(
    sigma: float,
    gamma: float,
    a_val: float,
    omega: float,
    t_cut: float,
    foreigners: list[tuple[float, float, int, float]],
) -> float:
    total = r_on_reduced(a_val, omega, sigma)
    if gamma <= t_cut:
        total += q_reduced(sigma, gamma, a_val, omega, sigma)
    for _sp, gp, m_use, qv in foreigners:
        if gp <= t_cut:
            total += m_use * qv
            if not math.isfinite(total):
                return total
    return total


def eval_cell(
    sigma: float,
    gamma: float,
    a_kind: str,
    o_kind: str,
    scenario: str,
    eps: float,
    smoke: bool,
) -> dict:
    a_val = a_of(sigma, a_kind)
    omega = omega_of(sigma, gamma, a_val, o_kind)
    n_pts = 8 if smoke else N_RASTER
    pool = build_pool(sigma, a_val, omega, scenario, eps, n_pts)
    ts = t_grid(gamma, smoke)
    t0 = gamma
    seq: list[tuple[float, float, list]] = []
    for t_cut in ts:
        host_in = gamma <= t_cut
        fr = pick_foreigners(pool, t_cut, gamma, host_in, N_FOREIGN)
        wv = w_reduced_at(sigma, gamma, a_val, omega, t_cut, fr)
        seq.append((t_cut, wv, fr))
    cofinal = [(t, w, fr) for t, w, fr in seq if t >= t0]
    if not cofinal:
        cofinal = seq[-1:]
    worst_t, worst_w, worst_fr = max(
        cofinal, key=lambda row: (
            math.inf if not math.isfinite(row[1]) and row[1] > 0 else row[1],
            row[0],
        )
    )
    holds = math.isfinite(worst_w) and worst_w < 0.0
    if not holds and worst_fr:
        sp, gp, m_use, qv = worst_fr[0]
        breaker = (
            "sig=%.4f/gam=%.4f/a=%s/om=%s/T=%.4g/"
            "f0=(s=%.6g,g=%.10g,m=%d,Qred=%s)"
            % (sigma, gamma, a_kind, o_kind, worst_t, sp, gp, m_use, nstr(qv, 6))
        )
    elif not holds:
        breaker = "sig=%.4f/gam=%.4f/a=%s/om=%s/T=%.4g/Wred=%s" % (
            sigma, gamma, a_kind, o_kind, worst_t, nstr(worst_w, 6),
        )
    else:
        breaker = ""
    return {
        "sigma": sigma, "gamma": gamma, "a_kind": a_kind, "o_kind": o_kind,
        "holds": holds, "worst_w": worst_w, "worst_t": worst_t,
        "breaker": breaker, "n_fr": len(worst_fr),
    }


def _wkey(row: dict) -> float:
    w = row["worst_w"]
    return math.inf if (not math.isfinite(w) and w > 0) else w


def scenario_verdict(rows: list[dict]) -> tuple[str, dict]:
    hosts = sorted({(r["sigma"], r["gamma"]) for r in rows})
    saved, failed, best_by_host = [], [], {}
    worst_fail: dict | None = None
    for host in hosts:
        cells = [r for r in rows if (r["sigma"], r["gamma"]) == host]
        winners = [r for r in cells if r["holds"]]
        if winners:
            saved.append(host)
            best_by_host[host] = min(winners, key=_wkey)
            continue
        failed.append(host)
        # best-effort packet still flipped: tightest (least positive) W
        flop = min(cells, key=_wkey)
        if worst_fail is None or _wkey(flop) > _wkey(worst_fail):
            worst_fail = flop
    extra = {
        "n_host": len(hosts), "n_saved": len(saved), "n_failed": len(failed),
        "worst_w": None, "breaker": "", "best_delta": None,
    }
    if saved and not failed:
        worst_saved = max(best_by_host.values(), key=_wkey)
        extra["worst_w"] = worst_saved["worst_w"]
        extra["best_delta"] = -worst_saved["worst_w"]
        return (
            "COFINAL_NEG_HOLDS(hosts=%d, worst_Wred=%s, delta=%s)"
            % (len(saved), nstr(worst_saved["worst_w"], 6), nstr(extra["best_delta"], 6)),
            extra,
        )
    br = worst_fail["breaker"] if worst_fail else "unknown"
    extra["breaker"] = br
    extra["worst_w"] = worst_fail["worst_w"] if worst_fail else math.inf
    if failed and not saved:
        return "COFINAL_NEG_BREAKS(%s)" % br, extra
    return "MIXED(saved=%d, failed=%d, breaker=%s)" % (len(saved), len(failed), br), extra


def run_g0() -> None:
    sigma, gamma = 0.25, 14.0
    a_val = a_of(sigma, "64")
    omega = omega_of(sigma, gamma, a_val, "phase")
    q_plus = q_reduced(sigma, gamma, a_val, omega, sigma)
    q_minus = q_reduced(sigma, -gamma, a_val, omega, sigma)
    check("G0-c-inc-pin", abs(C_INC_PIN - 174.818115823) < 1e-12, nstr(C_INC_PIN))
    check("G0-q-even-gamma", abs(q_plus - q_minus) < 1e-12, nstr(q_plus - q_minus, 6))
    check("G0-phase-host-neg", q_plus < 0.0, "Qred=%s" % nstr(q_plus, 6))
    q_ctr = q_reduced(sigma, omega, a_val, omega, sigma)
    check(
        "G0-r551-centre-pos",
        q_ctr > 0.0 and q_ctr > abs(q_plus),
        "Qctr=%s |Qhost|=%s" % (nstr(q_ctr, 6), nstr(abs(q_plus), 6)),
    )
    ron = r_on_reduced(a_val, omega, sigma)
    check("G0-ron-tiny-vs-host", 0.0 <= ron < 1e-6, "Ron/E=%s" % nstr(ron, 6))
    check("G0-kcap-c1", k_cap(14.0) == int(math.floor(2 * (1 + math.log(17.0)))), str(k_cap(14.0)))
    check("G0-seed-frozen", SEED == 20260902, str(SEED))


def interpret(verdicts: dict[str, str]) -> str:
    a_ok = verdicts["strict"].startswith("COFINAL_NEG_HOLDS")
    b_ok = verdicts["weak"].startswith("COFINAL_NEG_HOLDS")
    c_ok = verdicts["free"].startswith("COFINAL_NEG_HOLDS")
    if a_ok and b_ok and c_ok:
        return "beweisbar-plausibel"
    if a_ok and (not b_ok) and (not c_ok):
        return "nur-mit-Extremalitaet"
    if not a_ok:
        return "tot"
    return "nur-mit-Extremalitaet"


def run(smoke: bool) -> int:
    np.random.seed(SEED)
    print("gabor_fixed_packet_cofinal_probe -- r591")
    print("SPEC_SHA %s" % SPEC_SHA)
    print("FILE_SHA256 %s" % file_sha256())
    print("smoke %d" % int(smoke))
    print("CLAIM_BOUNDARY experiments_only; NO_RH_CLAIM")
    print("hat_convention weil_shifted")
    print("lean_target GaborFixedPacketCofinalNegAt")
    print("quantifiers packet_sees_host_only; adversary_after; cofinal_T")
    print("online 2*C_inc*S_cert  C_inc %s  C=1 K=2*(1+ln(|g|+3))" % nstr(C_INC_PIN))
    print("FORMULA  W_honest = sum m Q + R_on   (no R_ref, no -3.56)")
    print("FORMULA  reduced E=(pi/a)exp(sigma*^2/2a); never raw e^{s^2/2a}")

    print("\n" + "=" * 74)
    print("G0  SEAL / Q-EVEN / R551 CENTRE / R_ON")
    run_g0()

    sigmas = (0.25,) if smoke else SIGMAS
    gammas = (14.0,) if smoke else GAMMAS
    a_kinds = ("512", "64") if smoke else A_KINDS
    o_kinds = OMEGA_KINDS

    by_scen: dict[str, list[dict]] = {name: [] for name in SCENARIOS}
    print("\n" + "=" * 74)
    print("G1  FIXED PACKET vs POST-CHOICE ADVERSARY")
    for scenario in SCENARIOS:
        eps = EPS_STRICT if scenario == "strict" else 0.0
        for sigma in sigmas:
            for gamma in gammas:
                for a_kind in a_kinds:
                    for o_kind in o_kinds:
                        row = eval_cell(
                            sigma, gamma, a_kind, o_kind, scenario, eps, smoke,
                        )
                        by_scen[scenario].append(row)

    verdicts: dict[str, str] = {}
    extras: dict[str, dict] = {}
    for scenario in SCENARIOS:
        verd, extra = scenario_verdict(by_scen[scenario])
        verdicts[scenario] = verd
        extras[scenario] = extra
        tag = {"strict": "A", "weak": "B", "free": "C"}[scenario]
        print("VERDICT_%s %s  %s" % (tag, scenario, verd))
        ww = extra.get("worst_w")
        print(
            "  hosts saved/fail %d/%d  worst_Wred=%s  breaker=%s"
            % (
                extra["n_saved"], extra["n_failed"],
                nstr(ww) if ww is not None else "na",
                extra.get("breaker", "") or "-",
            )
        )

    print("\n" + "=" * 74)
    print("G2  STRICT eps-DEPENDENCE (phase packets only)")
    for eps in EPS_SCAN:
        rows = [
            eval_cell(sigma, gamma, a_kind, "phase", "strict", eps, smoke)
            for sigma in sigmas for gamma in gammas for a_kind in a_kinds
        ]
        verd, extra = scenario_verdict(rows)
        print("  eps=%s  %s  worst_Wred=%s" % (
            nstr(eps, 3), verd,
            nstr(extra["worst_w"]) if extra.get("worst_w") is not None else "na",
        ))

    print("\n" + "=" * 74)
    print("G3  INTERPRETATION")
    meaning = interpret(verdicts)
    print("INTERPRETATION GaborFixedPacketCofinalNegAt %s" % meaning)
    print("STRICT  %s" % verdicts["strict"])
    print("WEAK    %s" % verdicts["weak"])
    print("FREE    %s" % verdicts["free"])
    print("NO_RH_CLAIM")

    n_fail = sum(1 for _, ok in CHECKS if not ok)
    print("\nCHECKS %d/%d" % (len(CHECKS) - n_fail, len(CHECKS)))
    return 0 if n_fail == 0 else 1


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--smoke", action="store_true")
    args = parser.parse_args()
    raise SystemExit(run(args.smoke))


if __name__ == "__main__":
    main()
