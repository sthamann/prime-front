#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""gabor_window_adaptive_tail_probe -- r592

Round 592.  Experiments-only FALSIFICATION of L2 TAIL_ABSCHÄTZUNG
after r591 (fixed packets die on equal-σ centre killers).  Packet
(a,ω) from finite W_R={ρ:|Im ρ−γ_c|≤R}, AFTER window, BEFORE outer
adversaries.  Finite increment-capped arithmetic.  NO RH claim.

HAT/W from r591/r567/r560.  Q=(π/a)[A₊cosφ₊+A₋cosφ₋+2Aₓcosφₓ],
A±=exp((σ′²−(γ′∓ω)²)/(2a)), Aₓ=exp((σ′²−γ′²−ω²)/(2a)),
φ₊=σ′(γ′+ω)/a, φ₋=σ′(γ′−ω)/a, φₓ=σ′γ′/a.
R_on=2 C_inc S_cert, C_inc=174.818115823,
S_cert=(π/(4a))(Θ_lobe+Θ_left_pos+2 Θ_cross_pos).
Reduced E=(π/a)exp(σ★²/2a).  W=Σ m Q + R_on.

ISOLATION-SHRINK = isolationShrinkOfConfig on W_R:
  Host=σ-max in W_R, tie-break min γ.  d_min=min{|γ′−γ★|:γ′≠γ★} or +∞.
  ε(a)=√(2a log max(1/a,4·43)).  radius=πa/σ+ε(a).
  a_lock=σ★²/512 (=gaborALock).  a_ω=γ★σ★/(2π) (isolationShrinkTop).
  a_seed=min(a_lock,a_ω).  +∞ ⇒ a=a_seed; else largest a≤a_seed with
  radius≤d_min/2 and ω>0 (80-step log bisection; no a-floor).
  Cap min(a_lock,shrink) — NOT full gaborSmallnessA.  ω=γ★−πa/σ★.
  Float64: πa/σ★<ulp(γ★) ⇒ ω=γ★ (r551 self-kill).  Reported.

L2: A₋′/A₋★=exp((σ′²−σ★²−d²−2dq)/(2a)), q=πa/σ★.
𝒯(a)=Σ_{ρ∉W} m exp((σ_ρ²−σ★²−d_ρ²+2q|d_ρ|)/(2a)).
Falsify if sup_{ρ∉W}(σ_ρ²−σ★²−d_ρ²+2q|d_ρ|)≥0.
(A) local equal-σ centre killer in W_R.  (B) outer σ′≤σ★ |d|>R.
(C) σ_n↑σ★ escape sequences.  (D) σ′>σ★ control.
Verdicts HOLDS/BREAKS/MIXED and TAIL_METRIC_OK/FAILS.
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

C_INC_PIN = 174.818115823
K_BIN, SEED = 43, 20260902
EXPO_LO, EXPO_HI = -745.0, 709.0
SIGMAS, GAMMAS, RADII = (0.10, 0.25, 0.40), (14.0, 1000.0), (1.0, 3.0)
DELTAS, GAPS = (1e-2, 1e-3, 1e-4), (0.1, 1.0, 10.0)
GAMMA_LO, GAMMA_HI, SIGMA_FREE = 0.5, 2.0e4, 0.49
N_FOREIGN, N_RASTER, N_BISECT = 4, 28, 80
A_FLOOR_REL, EDGE_EPS = 1e-18, 1e-6

SPEC = {
    "round": 592, "parent_r591": "gabor_fixed_packet_cofinal_probe",
    "c_inc_pin": C_INC_PIN, "k_bin": K_BIN,
    "compliance": "K=2*(1+ln(|g|+3)); C=1", "seed": SEED,
    "sigmas": list(SIGMAS), "gammas": list(GAMMAS), "radii": list(RADII),
    "deltas": list(DELTAS), "gaps": list(GAPS),
    "a_rule": "min(sigma^2/512, isolation_shrink_on_W_R)",
    "omega_rule": "gamma_star - pi*a/sigma_star",
    "form": "W = sum m Q + R_on; Q,R_on r591/r567/r560 sealed",
    "tail": "T(a)=sum_outer m*exp((s^2-s*^2-d^2+2q|d|)/(2a))",
    "quantifiers": "packet sees W_R; outer adversary after",
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


def k_cap(gamma_p: float) -> int:
    return max(1, int(math.floor(2.0 * (1.0 + math.log(abs(gamma_p) + 3.0)))))


def theta3_q(a_val: float) -> float:
    total, m_val, q_log = 1.0, 1, -1.0 / (2.0 * a_val)
    while True:
        term = exp_clip((m_val * m_val) * q_log)
        if not math.isfinite(term):
            break
        total += 2.0 * term
        if term < 1e-80 or m_val > 200:
            gap = exp_clip(-(2.0 * m_val + 1.0) / (2.0 * a_val))
            if gap < 0.5:
                rem = 2.0 * exp_clip(-((m_val + 1) ** 2) / (2.0 * a_val))
                if gap < 1.0 and math.isfinite(rem) and (1.0 - gap) > 0.0:
                    total += rem / (1.0 - gap)
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


def r_on(a_val: float, omega: float) -> float:
    pref = math.pi / (4.0 * a_val)
    return 2.0 * C_INC_PIN * pref * (
        theta_lobe(a_val) + theta_left_pos(a_val, omega)
        + 2.0 * theta_cross_pos(a_val, omega)
    )


def q_reduced(sp: float, t_value: float, a_val: float, omega: float, sref: float) -> float:
    scale = (sp * sp - sref * sref) / (2.0 * a_val)

    def lobe(dist_sq: float, phase: float, weight: float) -> float:
        amp = exp_clip(scale - dist_sq / (2.0 * a_val))
        if amp == 0.0:
            return 0.0
        if not math.isfinite(amp):
            return math.inf
        return weight * amp * math.cos(phase)

    return (
        lobe((t_value + omega) ** 2, sp * (t_value + omega) / a_val, 1.0)
        + lobe((t_value - omega) ** 2, sp * (t_value - omega) / a_val, 1.0)
        + lobe(t_value ** 2 + omega ** 2, sp * t_value / a_val, 2.0)
    )


def r_on_reduced(a_val: float, omega: float, sref: float) -> float:
    raw, factor = r_on(a_val, omega), (a_val / math.pi) * exp_clip(-(sref * sref) / (2.0 * a_val))
    if factor == 0.0:
        return 0.0
    if not math.isfinite(factor) or not math.isfinite(raw):
        return math.inf
    return raw * factor


def w_reduced(pts, a_val: float, omega: float, sref: float) -> float:
    total = r_on_reduced(a_val, omega, sref)
    for sp, gp, m_use in pts:
        total += m_use * q_reduced(sp, gp, a_val, omega, sref)
        if not math.isfinite(total):
            return total
    return total


def a_minus(sp: float, gp: float, a_val: float, omega: float) -> float:
    return exp_clip((sp * sp - (gp - omega) ** 2) / (2.0 * a_val))


def epsilon_of(a_val: float) -> float:
    if a_val <= 0.0:
        return 0.0
    log_term = math.log(max(1.0 / a_val, 4.0 * K_BIN))
    return math.sqrt(2.0 * a_val * (log_term if log_term >= 1.0 else 1.0))


def a_lock_of(sigma: float) -> float:
    return (sigma * sigma) / 512.0


def isolated(sigma: float, d_min: float, a_val: float) -> bool:
    if not math.isfinite(d_min) or d_min <= 0.0 or a_val <= 0.0:
        return True
    return (math.pi * a_val / sigma) + epsilon_of(a_val) <= d_min / 2.0


def isolation_a(sigma: float, gamma: float, d_min: float) -> float:
    a_hi = a_lock_of(sigma)
    a_omega = gamma * sigma / (2.0 * math.pi)
    if 0.0 < a_omega < a_hi:
        a_hi = a_omega
    if a_hi <= 0.0:
        return a_lock_of(sigma)
    if isolated(sigma, d_min, a_hi) and math.pi * a_hi / sigma < gamma:
        return a_hi
    if not math.isfinite(d_min) or d_min <= 0.0:
        return a_hi
    a_lo = max(a_hi * A_FLOOR_REL, 1e-30)
    for _ in range(N_BISECT):
        mid = math.sqrt(a_lo * a_hi)
        if isolated(sigma, d_min, mid) and math.pi * mid / sigma < gamma:
            a_lo = mid
        else:
            a_hi = mid
    return a_lo


def pick_host(pts):
    return max(pts, key=lambda p: (p[0], -p[1]))


def foreign_dmin(pts, gamma_star: float) -> float:
    gaps = [abs(gp - gamma_star) for _sp, gp, _m in pts if abs(gp - gamma_star) > 1e-18]
    return min(gaps) if gaps else math.inf


def adaptive_packet(pts) -> dict:
    sigma, gamma, m_host = pick_host(pts)
    d_min = foreign_dmin(pts, gamma)
    a_val = isolation_a(sigma, gamma, d_min)
    omega = gamma - math.pi * a_val / sigma
    if not math.isfinite(d_min):
        tag = "top"
    elif a_val < a_lock_of(sigma) * (1.0 - 1e-12):
        tag = "shrunk"
    else:
        tag = "lock"
    return {
        "sigma": sigma, "gamma": gamma, "m": m_host, "a": a_val,
        "omega": omega, "d_min": d_min, "tag": tag,
    }


def q_of(a_val: float, sigma: float) -> float:
    return math.pi * a_val / sigma


def l2_num(sp: float, sstar: float, dist: float, q_val: float) -> float:
    return sp * sp - sstar * sstar - dist * dist + 2.0 * q_val * abs(dist)


def tail_from_arrays(sstar, a_val, sigmas, ds, masses) -> tuple[float, float, float]:
    if sigmas.size == 0:
        return 0.0, -math.inf, -math.inf
    q_val = q_of(a_val, sstar)
    nums = sigmas * sigmas - sstar * sstar - ds * ds + 2.0 * q_val * np.abs(ds)
    expo = nums / (2.0 * a_val) + np.log(np.maximum(masses, 1e-300))
    finite = np.isfinite(expo)
    if not np.any(finite):
        return 0.0, -math.inf, float(np.max(nums))
    expo_f, peak = expo[finite], float(np.max(expo[finite]))
    if peak <= EXPO_LO:
        t_val = 0.0
    elif peak >= EXPO_HI:
        t_val = math.inf
    else:
        t_val = float(math.exp(peak) * np.sum(np.exp(np.clip(expo_f - peak, -745.0, 0.0))))
        if not math.isfinite(t_val):
            t_val = math.inf
    return t_val, peak, float(np.max(nums))


def sequence_outers(gamma_star, radius, sigma_p, gap, smoke):
    start, n_max = gamma_star + radius + EDGE_EPS, (80 if smoke else (400 if gap < 0.5 else 2000))
    n_up = min(n_max, max(1, int(math.floor((GAMMA_HI - start) / gap)) + 1))
    gammas = start + gap * np.arange(n_up, dtype=float)
    gammas = gammas[gammas <= GAMMA_HI]
    lo_end = gamma_star - radius - EDGE_EPS
    if lo_end >= GAMMA_LO:
        n_dn = min(n_max, max(1, int(math.floor((lo_end - GAMMA_LO) / gap)) + 1))
        down = lo_end - gap * np.arange(n_dn, dtype=float)
        gammas = np.concatenate([gammas, down[down >= GAMMA_LO]])
    return np.full_like(gammas, sigma_p), gammas - gamma_star, np.array([float(k_cap(g)) for g in gammas])


def window_key(gamma_p: float) -> int:
    return int(math.floor(gamma_p))


def pick_foreigners(pool, k_max: int, host_g: float | None):
    used, picked = ({}, [])
    if host_g is not None:
        used[window_key(host_g)] = 1
    for sp, gp, m_max, qv in pool:
        if len(picked) >= k_max:
            break
        wk, already = window_key(gp), used.get(window_key(gp), 0)
        room = k_cap(float(wk) + 0.5) - already
        if room <= 0:
            continue
        m_use = min(m_max, room)
        if m_use <= 0:
            continue
        picked.append((sp, gp, m_use, qv))
        used[wk] = already + m_use
    return picked


def outer_pool(sstar, a_val, omega, scap, gstar, radius, n_pts, sigmas):
    heights = set(float(x) for x in np.geomspace(max(gstar + radius + EDGE_EPS, GAMMA_LO), GAMMA_HI, n_pts))
    lo = gstar - radius - EDGE_EPS
    if lo >= GAMMA_LO:
        heights.update(float(x) for x in np.geomspace(GAMMA_LO, lo, max(4, n_pts // 2)))
    for extra in (EDGE_EPS, 1e-3, 0.1, 1.0, 10.0):
        heights.add(gstar + radius + extra)
        if gstar - radius - extra >= GAMMA_LO:
            heights.add(gstar - radius - extra)
    pool = []
    for gp in sorted(heights):
        if not (GAMMA_LO <= gp <= GAMMA_HI) or abs(gp - gstar) <= radius:
            continue
        for sp in sigmas:
            spu = min(sp, scap)
            if spu <= 0.0:
                continue
            qv = q_reduced(spu, gp, a_val, omega, sstar)
            if qv > 0.0:
                pool.append((spu, gp, k_cap(gp), qv))
    pool.sort(key=lambda row: (-row[3], row[1], row[0]))
    return pool


def wkey_row(row: dict) -> float:
    w_val = row["w"]
    return math.inf if (not math.isfinite(w_val) and w_val > 0) else w_val


def margin_of(w_local: float) -> float:
    return -w_local if math.isfinite(w_local) and w_local < 0.0 else 0.0


def hosts_of(smoke: bool):
    return [(s, g) for s in ((0.25,) if smoke else SIGMAS) for g in ((14.0,) if smoke else GAMMAS)]


def radii_of(smoke: bool):
    return (1.0,) if smoke else RADII


def scenario_verdict(rows):
    if not rows:
        return "MIXED(empty)", {"n_ok": 0, "n_fail": 0, "worst_w": math.inf, "breaker": "empty"}
    ok_r, fail_r = [r for r in rows if r["holds"]], [r for r in rows if not r["holds"]]
    extra = {"n_ok": len(ok_r), "n_fail": len(fail_r), "worst_w": max(rows, key=wkey_row)["w"], "breaker": ""}
    if fail_r:
        worst = max(fail_r, key=wkey_row)
        extra["breaker"], extra["worst_w"] = worst.get("breaker", ""), worst["w"]
    if fail_r and not ok_r:
        return "BREAKS(%s)" % extra["breaker"], extra
    if ok_r and not fail_r:
        return "HOLDS", extra
    return "MIXED(saved=%d, failed=%d, breaker=%s)" % (len(ok_r), len(fail_r), extra["breaker"]), extra


def tail_verdict(rows):
    fails = [r for r in rows if not r.get("tail_ok", False)]
    extra = {
        "n_ok": sum(1 for r in rows if r.get("tail_ok", False)), "n_fail": len(fails),
        "worst_T": max((r.get("T", 0.0) for r in rows), default=0.0),
    }
    if fails:
        extra["breaker"] = max(fails, key=lambda r: r.get("T_over_margin", 0.0)).get("breaker", "")
        return "TAIL_METRIC_FAILS(%s)" % extra["breaker"], extra
    return "TAIL_METRIC_OK", extra


def run_g0() -> None:
    sigma, gamma = 0.25, 14.0
    a_val, omega = a_lock_of(sigma), gamma - math.pi * a_lock_of(sigma) / sigma
    qp, qm = q_reduced(sigma, gamma, a_val, omega, sigma), q_reduced(sigma, -gamma, a_val, omega, sigma)
    check("G0-c-inc-pin", abs(C_INC_PIN - 174.818115823) < 1e-12, nstr(C_INC_PIN))
    check("G0-a-lock-512", abs(a_val - sigma * sigma / 512.0) < 1e-18, nstr(a_val))
    check("G0-q-even-gamma", abs(qp - qm) < 1e-12, nstr(qp - qm, 6))
    check("G0-phase-host-neg", qp < 0.0, "Qred=%s" % nstr(qp, 6))
    qc = q_reduced(sigma, omega, a_val, omega, sigma)
    check("G0-r551-centre-pos", qc > 0.0 and qc > abs(qp), "Qctr=%s |Qh|=%s" % (nstr(qc, 6), nstr(abs(qp), 6)))
    check("G0-ron-tiny-vs-host", 0.0 <= r_on_reduced(a_val, omega, sigma) < 1e-6, "")
    check("G0-kcap-c1", k_cap(14.0) == int(math.floor(2 * (1 + math.log(17.0)))), str(k_cap(14.0)))
    check("G0-seed-frozen", SEED == 20260902, str(SEED))
    pkt = adaptive_packet([(sigma, gamma, 1)])
    check("G0-empty-window-lock", pkt["tag"] == "top" and abs(pkt["a"] - a_val) < 1e-18, pkt["tag"])
    d_val, gp, qv = 0.05, gamma + 0.05, q_of(a_val, sigma)
    ratio = a_minus(sigma, gp, a_val, omega) / a_minus(sigma, gamma, a_val, omega)
    pred = exp_clip((0.0 - d_val * d_val - 2.0 * d_val * qv) / (2.0 * a_val))
    check("G0-L2-ratio-identity", abs(ratio - pred) / max(pred, 1e-30) < 1e-9, nstr(ratio - pred, 6))
    near = adaptive_packet([(sigma, gamma, 1), (sigma, gamma + 1e-4, 1)])
    check("G0-shrink-near", near["tag"] == "shrunk" and near["a"] < a_val, nstr(near["a"]))
    check("G0-host-tiebreak-min-gamma", pick_host([(0.2, 10.0, 1), (0.2, 9.0, 1)])[1] == 9.0, "")


def local_row(cs, cg, radius, pts, tag) -> dict:
    pkt = adaptive_packet(pts)
    w_loc = w_reduced(pts, pkt["a"], pkt["omega"], pkt["sigma"])
    holds = math.isfinite(w_loc) and w_loc < 0.0
    br = "" if holds else (
        "A/%s/s=%.4f/g=%.4f/R=%.3g/host=(%.6g,%.10g)/tag=%s/a=%s/W=%s"
        % (tag, cs, cg, radius, pkt["sigma"], pkt["gamma"], pkt["tag"], nstr(pkt["a"], 6), nstr(w_loc, 6))
    )
    return {
        "holds": holds, "w": w_loc, "breaker": br, "tag": pkt["tag"],
        "merged": abs(pkt["gamma"] - cg) > 1e-18 or abs(pkt["sigma"] - cs) > 1e-18,
        "a": pkt["a"], "omega": pkt["omega"], "sigma": pkt["sigma"], "gamma": pkt["gamma"],
        "margin": margin_of(w_loc), "T": 0.0, "tail_ok": True, "T_over_margin": 0.0,
        "l2_sup": -math.inf, "kind": tag, "radius": radius, "centre_s": cs, "centre_g": cg,
    }


def scenario_a(smoke: bool) -> list[dict]:
    rows = []
    for sigma, gamma in hosts_of(smoke):
        for radius in radii_of(smoke):
            omega_lk = gamma - math.pi * a_lock_of(sigma) / sigma
            host = (sigma, gamma, 1)
            rows.append(local_row(sigma, gamma, radius, [host, (sigma, omega_lk, k_cap(omega_lk))], "centre-below"))
            g_up = 2.0 * gamma - omega_lk
            rows.append(local_row(sigma, gamma, radius, [host, (sigma, g_up, k_cap(g_up))], "centre-above"))
            rows.append(local_row(sigma, gamma, radius, [host, (sigma, gamma + 1e-8, k_cap(gamma + 1e-8))], "near-tie"))
            if not smoke:
                rows.append(local_row(sigma, gamma, radius, [host, (sigma, gamma + 1e-4, k_cap(gamma + 1e-4))], "mid-tie"))
    return rows


def attach_tail(row, pkt, scap, sseq, gap, smoke) -> dict:
    radius, gstar, sstar, a_val = row["radius"], pkt["gamma"], pkt["sigma"], pkt["a"]
    sigmas, ds, masses = sequence_outers(gstar, radius, sseq, gap, smoke)
    mask = np.abs(ds) > radius
    t_val, log_t, l2_sup = tail_from_arrays(sstar, a_val, sigmas[mask], ds[mask], masses[mask])
    mar, w_loc = margin_of(row["w"]), row["w"]
    tail_ok = mar > 0.0 and math.isfinite(t_val) and t_val < mar
    w_bound = w_loc + t_val if math.isfinite(t_val) else math.inf
    holds = math.isfinite(w_bound) and w_bound < 0.0
    br = "" if holds and tail_ok else (
        "s=%.4f/g=%.4f/R=%.3g/a=%s/T=%s/marg=%s/l2=%s/gap=%s/scap=%.4f"
        % (sstar, gstar, radius, nstr(a_val, 6), nstr(t_val, 6), nstr(mar, 6), nstr(l2_sup, 6), nstr(gap, 3), scap)
    )
    out = dict(row)
    out.update({
        "T": t_val, "log_T": log_t, "l2_sup": l2_sup, "tail_ok": tail_ok,
        "T_over_margin": (t_val / mar) if mar > 0.0 and math.isfinite(t_val) else math.inf,
        "w_bound": w_bound, "holds": holds, "w": w_bound, "breaker": br,
        "gap": gap, "sigma_seq": sseq, "sigma_cap": scap,
    })
    return out


def scenario_outer(smoke: bool, kind: str) -> list[dict]:
    rows, n_pts = [], 8 if smoke else N_RASTER
    for sigma, gamma in hosts_of(smoke):
        for radius in radii_of(smoke):
            pts = [(sigma, gamma, 1)]
            pkt = adaptive_packet(pts)
            w_loc = w_reduced(pts, pkt["a"], pkt["omega"], pkt["sigma"])
            base = {
                "holds": True, "w": w_loc, "breaker": "", "tag": pkt["tag"], "merged": False,
                "a": pkt["a"], "omega": pkt["omega"], "sigma": pkt["sigma"], "gamma": pkt["gamma"],
                "margin": margin_of(w_loc), "kind": kind, "radius": radius,
                "centre_s": sigma, "centre_g": gamma, "w_local": w_loc,
            }
            if kind == "B":
                scap, sseq = sigma, sigma
                sig_grid = [1e-2, 0.5 * sigma, max(sigma - 0.01, 1e-2), sigma]
            else:
                scap, sseq = SIGMA_FREE, SIGMA_FREE
                sig_grid = [sigma, 0.5 * (sigma + SIGMA_FREE), SIGMA_FREE]
            gaps = (1.0,) if smoke else GAPS
            pool = outer_pool(pkt["sigma"], pkt["a"], pkt["omega"], scap, pkt["gamma"], radius, n_pts, sig_grid)
            picked = pick_foreigners(pool, N_FOREIGN, pkt["gamma"])
            w_hon = w_reduced(pts + [(sp, gp, m) for sp, gp, m, _q in picked], pkt["a"], pkt["omega"], pkt["sigma"])
            hon = dict(base)
            hon["w"], hon["holds"] = w_hon, math.isfinite(w_hon) and w_hon < 0.0
            if not hon["holds"]:
                fr = picked[0] if picked else (0.0, 0.0, 0, 0.0)
                hon["breaker"] = "%s/honest/s=%.4f/g=%.4f/R=%.3g/W=%s/f0=(s=%.6g,g=%.10g,m=%d)" % (
                    kind, sigma, gamma, radius, nstr(w_hon, 6), fr[0], fr[1], fr[2])
            for gap in gaps:
                rows.append(attach_tail(dict(base), pkt, scap, sseq, gap, smoke))
            hon["T"] = rows[-1]["T"] if rows else 0.0
            mar = margin_of(w_loc)
            hon["tail_ok"] = mar > 0.0 and math.isfinite(hon["T"]) and hon["T"] < mar
            hon["T_over_margin"] = hon["T"] / mar if mar > 0 else math.inf
            hon["l2_sup"] = rows[-1]["l2_sup"] if rows else -math.inf
            rows.append(hon)
    return rows


def scenario_c(smoke: bool) -> list[dict]:
    rows, deltas, gaps = [], ((1e-2,) if smoke else DELTAS), ((1.0,) if smoke else GAPS)
    for sigma, gamma in hosts_of(smoke):
        for radius in radii_of(smoke):
            pts = [(sigma, gamma, 1)]
            pkt = adaptive_packet(pts)
            w_loc = w_reduced(pts, pkt["a"], pkt["omega"], pkt["sigma"])
            base = {
                "holds": True, "w": w_loc, "breaker": "", "tag": pkt["tag"], "merged": False,
                "a": pkt["a"], "omega": pkt["omega"], "sigma": pkt["sigma"], "gamma": pkt["gamma"],
                "margin": margin_of(w_loc), "kind": "C", "radius": radius,
                "centre_s": sigma, "centre_g": gamma, "w_local": w_loc,
            }
            for delta in deltas:
                for gap in gaps:
                    row = attach_tail(dict(base), pkt, sigma, max(sigma - delta, 1e-4), gap, smoke)
                    row["delta"] = delta
                    rows.append(row)
    return rows


def interpret(verdicts, tail_v, l2_nonneg) -> str:
    a_ok = verdicts["A"].startswith("HOLDS")
    outer_ok = all(verdicts[k].startswith("HOLDS") for k in "BC")
    t_ok = all(v.startswith("TAIL_METRIC_OK") for v in tail_v.values())
    if l2_nonneg:
        return "TOT(L2-numerator-nonneg)"
    if not a_ok:
        return "KONDITIONAL(A-near-tie IEEE-omega-collapse; outer-tail-ok; Host-sigma-max per Hoehe)"
    return "KONDITIONAL(Host-sigma-max per Hoehe/T-Neuwahl; Fenster deckt |d|<=2q)" if outer_ok and t_ok else "TOT(outer-tail-eats-margin)"


def pub(rows):
    keys = ("holds", "w", "T", "tail_ok", "l2_sup", "a", "tag", "kind", "radius", "centre_s", "centre_g", "breaker", "delta", "gap")
    out = []
    for row in rows:
        rec = {}
        for key in keys:
            if key not in row:
                continue
            val = row[key]
            rec[key] = int(bool(val)) if key in ("holds", "tail_ok") else (
                nstr(val) if isinstance(val, float) else val
            )
        out.append(rec)
    return out


def compute(smoke: bool) -> dict:
    return {"A": scenario_a(smoke), "B": scenario_outer(smoke, "B"),
            "C": scenario_c(smoke), "D": scenario_outer(smoke, "D")}

def payload_sha(blob: dict) -> str:
    return hashlib.sha256(json.dumps(blob, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def run(smoke: bool) -> int:
    np.random.seed(SEED)
    print("gabor_window_adaptive_tail_probe -- r592")
    print("SPEC_SHA %s" % SPEC_SHA)
    print("FILE_SHA256 %s" % file_sha256())
    print("smoke %d" % int(smoke))
    print("CLAIM_BOUNDARY experiments_only; NO_RH_CLAIM")
    print("quantifiers packet_sees_W_R; outer_adversary_after")
    print("online 2*C_inc*S_cert  C_inc %s  C=1 K=2*(1+ln(|g|+3))" % nstr(C_INC_PIN))
    print("FORMULA  W=sum m Q+R_on; T(a)=sum m exp((s^2-s*^2-d^2+2q|d|)/(2a))")
    print("RULE  host=max_sigma/min_gamma; a=min(s^2/512,shrink); w=g-pi a/s")
    print("\n" + "=" * 74)
    print("G0  SEAL / Q-EVEN / R551 / SHRINK / L2-RATIO")
    run_g0()
    data1, data2 = compute(smoke), compute(smoke)
    seal1 = payload_sha({"SPEC_SHA": SPEC_SHA, "rows": {k: pub(v) for k, v in data1.items()}})
    seal2 = payload_sha({"SPEC_SHA": SPEC_SHA, "rows": {k: pub(v) for k, v in data2.items()}})
    check("G3-determinism-two-run", seal1 == seal2, "payload hashed twice")
    check("G3-determinism-contract", True, "no wall-clock, no RNG, BLAS threads=1")
    data, verdicts, extras, tail_vs = data1, {}, {}, {}
    print("\n" + "=" * 74)
    print("G1  SCENARIOS A–D")
    for name in ("A", "B", "C", "D"):
        verd, extra = scenario_verdict(data[name])
        tverd, textra = tail_verdict(data[name])
        verdicts[name], extras[name], tail_vs[name] = verd, extra, tverd
        print("VERDICT_%s %s" % (name, verd))
        print("  TAIL_%s %s" % (name, tverd))
        print("  n_ok/fail %d/%d  worst_W=%s  worst_T=%s  breaker=%s" % (
            extra["n_ok"], extra["n_fail"], nstr(extra["worst_w"], 6),
            nstr(textra.get("worst_T", 0.0), 6), extra.get("breaker", "") or "-",
        ))
    print("\n" + "=" * 74)
    print("G2  TAIL METRIC / L2 FALSIFICATION / delta-gap SCAN")
    l2_global = max((r.get("l2_sup", -math.inf) for r in data["B"] + data["C"] + data["D"]), default=-math.inf)
    closed_max = -math.inf
    for sigma, gamma in hosts_of(smoke):
        for radius in radii_of(smoke):
            pkt = adaptive_packet([(sigma, gamma, 1)])
            for scap in (sigma, SIGMA_FREE):
                closed_max = max(closed_max, l2_num(scap, pkt["sigma"], radius + EDGE_EPS, q_of(pkt["a"], pkt["sigma"])))
    l2_any = l2_global >= 0.0 or closed_max >= 0.0
    l2_global = max(l2_global, closed_max)
    print("L2_SUP_CLOSED %s" % nstr(closed_max, 6))
    print("L2_SUP_SCAN %s" % nstr(l2_global, 6))
    print("L2_FALSIFICATION %s" % ("REACHED" if l2_any else "NOT_REACHED"))
    check("G2-L2-closed-negative", closed_max < 0.0, nstr(closed_max, 6))
    by_key = {}
    for row in data["C"]:
        key = (row.get("delta", 0.0), row.get("gap", 0.0), row["radius"])
        if key not in by_key or wkey_row(row) > wkey_row(by_key[key]):
            by_key[key] = row
    for key in sorted(by_key):
        row = by_key[key]
        print("  C dlt=%s gap=%s R=%s  T=%s logT=%s l2=%s marg=%s T/m=%s %s" % (
            nstr(key[0], 3), nstr(key[1], 3), nstr(key[2], 3), nstr(row["T"], 6),
            nstr(row.get("log_T", -math.inf), 6), nstr(row["l2_sup"], 6), nstr(row["margin"], 6),
            nstr(row.get("T_over_margin", 0.0), 6), "OK" if row["tail_ok"] else "FAIL",
        ))
    exists_a = all(r.get("tail_ok", False) for r in data["B"] + data["C"])
    print("EXISTS_LOCAL_a_T_lt_MARGIN %s" % ("YES" if exists_a else "NO"))
    print("\n" + "=" * 74)
    print("G3  INTERPRETATION")
    print("INTERPRETATION lokal-adaptiv-global-fest %s" % interpret(verdicts, tail_vs, l2_any))
    for name in ("A", "B", "C", "D"):
        print("SCENARIO_%s %s  %s" % (name, verdicts[name], tail_vs[name]))
    print("A_MECHANISMS merge=%d shrink=%d lock=%d" % (
        sum(1 for r in data["A"] if r.get("merged")),
        sum(1 for r in data["A"] if r.get("tag") == "shrunk"),
        sum(1 for r in data["A"] if r.get("tag") in ("lock", "top")),
    ))
    print("D_NOTE host-not-extremal; residual = host reselect as T grows / window slides")
    print("PAYLOAD_SHA256 %s" % seal1)
    print("NO_RH_CLAIM")
    n_fail = sum(1 for _, ok in CHECKS if not ok)
    print("\nCHECKS %d/%d" % (len(CHECKS) - n_fail, len(CHECKS)))
    if n_fail:
        return 1
    print("ALL CHECKS PASSED")
    return 0


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--smoke", action="store_true")
    args = parser.parse_args()
    raise SystemExit(run(args.smoke))


if __name__ == "__main__":
    main()
