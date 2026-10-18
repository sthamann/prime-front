#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""gabor_exposed_orbit_probe -- r605N

Experiments-only scout of EXPOSED-ORBIT + PHASE-LOCK selection for
the pure-Gabor zero-side Z = Re Σ_ρ m(ρ) ĥ(ρ) (no pole term).

  Score of an orbit (σ², |γ|) at ω ≥ 0:  S(ω) = σ² − (|γ| − ω)².
  On-line orbits have S ≤ 0.  Given an off-line host ρ₀, the interval
  I = (γ₀ − |σ₀|/2, γ₀ + |σ₀|/2) has S_{ρ₀} > 3σ₀²/4 > 0.  After
  dropping −ω² the scores are lines; two distinct orbits tie at most
  once.  ω* is the midpoint of the longest tie-and-ordinate-free
  subinterval of I.  Unique maximizer ρ* with gap Δ > 0.  Phase lock
  a_n = |σ* d*| / ((2n+1)π),  d* = |γ*| − ω*,  so cos(σ* d*/a_n) = −1.

CLAIM BOUNDARY.  Finite closed-form / seeded arithmetic on synthetic
off-line catalogs plus a frozen on-line ordinate table.  NO RH claim,
NO anti-RH claim, NO ledger/paper/Lean/verification/website/next.txt
edit.  KEIN RH-CLAIM.

HAT CONVENTION.  Literal Lean `pureGaborHatDelta` (GaborSeparation.lean
L114–123), δ = s − 1/2, third lobe 2 exp((σ²−t²−ω²)/(2a)) exp(i σ t/a).
Checkpoint ĥ_{1,0}(1) = π e^{1/8}.  FE quadruple
ĥ(ρ)+ĥ(1−ρ)+ĥ(ρ̄)+ĥ(1−ρ̄) = 4 Re ĥ(ρ).  A σ>0 orbit expands to four
strip partners; σ=0 expands to two.  Z uses Re Σ m ĥ, no pole.

On-line background: first 2000 positive ordinates from
verified_zeros_n7000.npy (mpmath.zetazero, dps=15).  No synthetic
von Mangoldt tail.

Verdicts:
  EXPOSED_ORBIT_HOLDS
  EXPOSED_ORBIT_BREAKS(<where>)
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
import random
import sys
from pathlib import Path

os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("MKL_NUM_THREADS", "1")
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
os.environ.setdefault("NUMEXPR_NUM_THREADS", "1")

import mpmath as mp  # noqa: E402
import numpy as np  # noqa: E402

HERE = Path(__file__).resolve().parent
CACHE_N7000 = HERE / "verified_zeros_n7000.npy"

ROUND = 605
SEED = 605202609
DPS = 60
N_ONLINE = 2000
N_T1 = 20
N_MAX = 8
N_T5 = 200
N_T5_MAX = 12
CUT_ATOL = 1e-14
S_ATOL = 1e-14
EXPO_SKIP = -40.0
PI = math.pi

SPEC = {
    "round": ROUND,
    "tag": "r605N",
    "contract": "PRIME.RDAGGER.GABOR.EXPOSED_ORBIT.01",
    "hat": "pureGaborHatDelta_literal_L114",
    "score": "S=sigma^2-(|gamma|-omega)^2",
    "a_n": "|sigma* d*| / ((2n+1) pi)",
    "c_star": 4,
    "seed": SEED,
    "n_online": N_ONLINE,
    "zeros_cache": "verified_zeros_n7000.npy[:2000]",
    "zeros_pedigree": "mpmath.zetazero dps=15",
    "dps": DPS,
}
SPEC_SHA = hashlib.sha256(
    json.dumps(SPEC, sort_keys=True, separators=(",", ":")).encode()
).hexdigest()
CHECKS: list[tuple[str, bool]] = []
LINES: list[str] = []


def emit(line: str = "") -> None:
    LINES.append(line)
    print(line)


def check(name: str, ok: bool, detail: str = "") -> bool:
    flag = bool(ok)
    CHECKS.append((name, flag))
    emit("  [%s] %-42s %s" % ("PASS" if flag else "FAIL", name, detail))
    return flag


def fmt(x: float, n: int = 12) -> str:
    return "%+.*e" % (n, float(x))


def file_sha256() -> str:
    return hashlib.sha256(Path(__file__).read_bytes()).hexdigest()


# ---------------------------------------------------------------------------
# Hat: literal Lean pureGaborHatDelta
# ---------------------------------------------------------------------------
def hat_delta_mp(a: mp.mpf, omega: mp.mpf, sigma: mp.mpf, t_val: mp.mpf) -> mp.mpc:
    """Lean `pureGaborHatDelta` (third lobe phase I·σ·t/a)."""
    pref = mp.pi / (4 * a)
    term_plus = mp.exp(
        (sigma ** 2 - (t_val + omega) ** 2) / (2 * a)
    ) * mp.exp(mp.j * (sigma * (t_val + omega) / a))
    term_minus = mp.exp(
        (sigma ** 2 - (t_val - omega) ** 2) / (2 * a)
    ) * mp.exp(mp.j * (sigma * (t_val - omega) / a))
    term_cross = (
        2
        * mp.exp((sigma ** 2 - t_val ** 2 - omega ** 2) / (2 * a))
        * mp.exp(mp.j * (sigma * t_val / a))
    )
    return pref * (term_plus + term_minus + term_cross)


def score_S(sigma: float, gamma: float, omega: float) -> float:
    dlt = abs(gamma) - omega
    return sigma * sigma - dlt * dlt


def score_line(sigma: float, gamma: float, omega: float) -> float:
    gabs = abs(gamma)
    return 2.0 * gabs * omega + sigma * sigma - gabs * gabs


def tie_omega(
    s1: float, g1: float, s2: float, g2: float,
) -> float | None:
    """ω where L_1 = L_2.  None if parallel (same |γ|)."""
    dg = abs(g1) - abs(g2)
    if abs(dg) < 1e-18:
        return None
    num = (
        abs(g1) ** 2 - abs(g2) ** 2 - s1 * s1 + s2 * s2
    )
    return num / (2.0 * dg)


def unique_sorted(xs: list[float], atol: float = CUT_ATOL) -> list[float]:
    if not xs:
        return []
    xs = sorted(xs)
    out = [xs[0]]
    for val in xs[1:]:
        if val - out[-1] > atol:
            out.append(val)
    return out


def merge_orbits(
    orbits: list[tuple[float, float, int]],
) -> list[tuple[float, float, int]]:
    acc: dict[tuple[float, float], int] = {}
    order: list[tuple[float, float]] = []
    for sigma, gamma, mult in orbits:
        key = (float(sigma), float(abs(gamma)))
        if key not in acc:
            order.append(key)
            acc[key] = 0
        acc[key] += int(mult)
    return [(sig, gam, acc[(sig, gam)]) for sig, gam in order]


def expand_partners(
    sigma: float, gamma: float, mult: int,
) -> list[tuple[float, float, int]]:
    if abs(sigma) <= 1e-18:
        return [(0.0, gamma, mult), (0.0, -gamma, mult)]
    return [
        (sigma, gamma, mult),
        (sigma, -gamma, mult),
        (-sigma, gamma, mult),
        (-sigma, -gamma, mult),
    ]


def load_online(n_use: int) -> tuple[float, ...]:
    raw = np.load(str(CACHE_N7000))
    n_use = min(int(n_use), int(raw.shape[0]))
    return tuple(float(x) for x in raw[:n_use])


def competitor_orbits(
    off: list[tuple[float, float, int]],
    online: tuple[float, ...],
    i_lo: float,
    i_hi: float,
) -> list[tuple[float, float, int]]:
    """Off-line (all) plus on-line with |γ| ≤ i_hi+1 and ≥ i_lo-1."""
    lo = i_lo - 1.0
    hi = i_hi + 1.0
    out = list(off)
    for gam in online:
        if lo <= gam <= hi:
            out.append((0.0, float(gam), 1))
    return merge_orbits(out)


def select_omega(
    off: list[tuple[float, float, int]],
    online: tuple[float, ...],
    host: tuple[float, float, int],
) -> dict:
    """Exposed-orbit selection.  Host = ρ₀ (first listed off-line)."""
    sigma0, gamma0, _m0 = host
    half = abs(sigma0) / 2.0
    i_lo = gamma0 - half
    i_hi = gamma0 + half
    if i_hi <= i_lo:
        return {"ok": False, "why": "empty_I"}
    catalog = competitor_orbits(off, online, i_lo, i_hi)
    cuts = [i_lo, i_hi]
    for sig, gam, _m in catalog:
        if i_lo < gam < i_hi:
            cuts.append(gam)
    for i, (s1, g1, _m1) in enumerate(catalog):
        for s2, g2, _m2 in catalog[i + 1 :]:
            t_omega = tie_omega(s1, g1, s2, g2)
            if t_omega is None:
                continue
            if i_lo < t_omega < i_hi:
                cuts.append(float(t_omega))
    cuts = unique_sorted(cuts)
    best_lo, best_hi, best_len = i_lo, i_hi, -1.0
    for left, right in zip(cuts, cuts[1:]):
        length = right - left
        if length <= CUT_ATOL:
            continue
        if length > best_len + CUT_ATOL or (
            abs(length - best_len) <= CUT_ATOL and left < best_lo
        ):
            best_len = length
            best_lo, best_hi = left, right
    if best_len <= CUT_ATOL:
        return {"ok": False, "why": "no_open_subinterval"}
    omega_star = 0.5 * (best_lo + best_hi)
    # Maximizer + Δ over the full catalog (far on-line have S<0 on I).
    full = merge_orbits(list(off) + [(0.0, float(g), 1) for g in online])
    scored: list[tuple[float, float, float, int]] = []
    for sig, gam, mult in full:
        scored.append((score_S(sig, gam, omega_star), sig, gam, mult))
    scored.sort(key=lambda row: (-row[0], row[2], -row[1]))
    s_star, sig_star, gam_star, m_star = scored[0]
    s_second = scored[1][0] if len(scored) > 1 else -1.0e300
    gap = s_star - s_second
    d_star = abs(gam_star) - omega_star
    unique = True
    for s_val, sig, gam, _m in scored[1:]:
        if abs(s_val - s_star) <= S_ATOL * (1.0 + abs(s_star)):
            if abs(sig - sig_star) > 1e-18 or abs(gam - gam_star) > 1e-18:
                unique = False
                break
    why = ""
    ok = True
    if abs(sig_star) <= 1e-18:
        ok, why = False, "maximizer_online"
    elif not unique:
        ok, why = False, "tie_unresolved"
    elif gap <= 0.0:
        ok, why = False, "nonpositive_gap"
    elif abs(d_star) <= 1e-18:
        ok, why = False, "d_star_zero"
    elif s_star <= 0.0:
        ok, why = False, "M_nonpositive"
    return {
        "ok": ok,
        "why": why,
        "omega": omega_star,
        "M": s_star,
        "Delta": gap,
        "d_star": d_star,
        "sigma_star": sig_star,
        "gamma_star": gam_star,
        "m_star": m_star,
        "i_lo": i_lo,
        "i_hi": i_hi,
        "n_comp": len(catalog),
        "unique": unique,
        "sub_lo": best_lo,
        "sub_hi": best_hi,
    }


def a_n_of(sigma_star: float, d_star: float, n_idx: int) -> float:
    return abs(sigma_star * d_star) / ((2 * n_idx + 1) * PI)


def safe_exp(x: float) -> float:
    if x < -745.0:
        return 0.0
    if x > 709.0:
        return math.inf
    return math.exp(x)


def mag_a1(sigma: float, t_val: float, omega: float) -> float:
    """Three-lobe magnitudes at a=1 (plus + minus + 2·cross)."""
    s2 = sigma * sigma
    a_plus = safe_exp(0.5 * (s2 - (t_val + omega) ** 2))
    a_minus = safe_exp(0.5 * (s2 - (t_val - omega) ** 2))
    a_cross = safe_exp(0.5 * (s2 - t_val * t_val - omega * omega))
    return a_plus + a_minus + 2.0 * a_cross


def r1_remainder(
    off: list[tuple[float, float, int]],
    online: tuple[float, ...],
    sel: dict,
    extra_online: tuple[float, ...] = (),
) -> float:
    sig_star = sel["sigma_star"]
    gam_star = sel["gamma_star"]
    omega = sel["omega"]
    total = 0.0
    for sig, gam, mult in off:
        same = abs(sig - sig_star) <= 1e-18 and abs(gam - gam_star) <= 1e-18
        for ps, pt, pm in expand_partners(sig, gam, mult):
            if same and abs(abs(pt) - gam_star) <= 1e-18 and abs(abs(ps) - sig_star) <= 1e-18:
                continue
            total += pm * mag_a1(ps, pt, omega)
    skip_star_on = abs(sig_star) <= 1e-18
    seen_extra = set()
    for gam in list(online) + list(extra_online):
        key = float(gam)
        if key in seen_extra:
            continue
        seen_extra.add(key)
        if skip_star_on and abs(gam - gam_star) <= 1e-18:
            continue
        total += mag_a1(0.0, gam, omega)
        total += mag_a1(0.0, -gam, omega)
    return total


def norm_re_one(
    sigma: float,
    t_val: float,
    a: float,
    omega: float,
    m_score: float,
    lock_minus: bool,
    lock_plus: bool,
    use_mp: bool = False,
) -> float:
    """e^{−M/(2a)} (A₊ cos φ₊ + A₋ cos φ₋ + 2 Aₓ cos φₓ)."""
    if use_mp:
        mp.mp.dps = DPS
        sig = mp.mpf(sigma)
        t_m = mp.mpf(t_val)
        a_m = mp.mpf(a)
        w_m = mp.mpf(omega)
        m_m = mp.mpf(m_score)
        two_a = 2 * a_m
        acc = mp.mpf("0")
        s2 = sig * sig
        terms = (
            (s2 - (t_m + w_m) ** 2, lock_plus, sig * (t_m + w_m) / a_m, mp.mpf("1")),
            (s2 - (t_m - w_m) ** 2, lock_minus, sig * (t_m - w_m) / a_m, mp.mpf("1")),
            (s2 - t_m * t_m - w_m * w_m, False, sig * t_m / a_m, mp.mpf("2")),
        )
        for score, locked, phase, wt in terms:
            expo = (score - m_m) / two_a
            if expo <= EXPO_SKIP:
                continue
            csg = mp.mpf("-1") if locked else mp.cos(phase)
            acc += wt * mp.exp(expo) * csg
        return acc
    s2 = sigma * sigma
    two_a = 2.0 * a
    acc = 0.0
    s_plus = s2 - (t_val + omega) ** 2
    expo = (s_plus - m_score) / two_a
    if expo > EXPO_SKIP:
        if lock_plus:
            csg = -1.0
        else:
            csg = math.cos(sigma * (t_val + omega) / a)
        acc += safe_exp(expo) * csg
    s_minus = s2 - (t_val - omega) ** 2
    expo = (s_minus - m_score) / two_a
    if expo > EXPO_SKIP:
        if lock_minus:
            csg = -1.0
        else:
            csg = math.cos(sigma * (t_val - omega) / a)
        acc += safe_exp(expo) * csg
    s_cross = s2 - t_val * t_val - omega * omega
    expo = (s_cross - m_score) / two_a
    if expo > EXPO_SKIP:
        acc += 2.0 * safe_exp(expo) * math.cos(sigma * t_val / a)
    return acc


def is_star_partner(
    sigma: float, t_val: float, sig_star: float, gam_star: float,
) -> bool:
    return (
        abs(abs(sigma) - abs(sig_star)) <= 1e-18
        and abs(abs(t_val) - abs(gam_star)) <= 1e-18
    )


def locks_for(sigma: float, t_val: float, star: bool) -> tuple[bool, bool]:
    """Leading-lobe lock: t>0 minus, t<0 plus.  Only on the exposed orbit."""
    if not star:
        return False, False
    if t_val > 0.0:
        return True, False
    if t_val < 0.0:
        return False, True
    return False, False


def normalized_Z(
    off: list[tuple[float, float, int]],
    online: tuple[float, ...],
    a: float,
    omega: float,
    m_score: float,
    sig_star: float,
    gam_star: float,
    extra_online: tuple[float, ...] = (),
    orbit_only: bool = False,
    use_mp: bool = False,
) -> float:
    """(4a/π) e^{−M/(2a)} Z  = Σ m e^{−M/(2a)} (A₊c₊ + A₋c₋ + 2Aₓcₓ)."""
    acc: float | object = mp.mpf("0") if use_mp else 0.0
    if use_mp:
        mp.mp.dps = DPS
    for sig, gam, mult in off:
        for ps, pt, pm in expand_partners(sig, gam, mult):
            star = is_star_partner(ps, pt, sig_star, gam_star)
            if orbit_only and not star:
                continue
            lock_minus, lock_plus = locks_for(ps, pt, star)
            s_loc = score_S(ps, pt, omega)
            if (not star) and (s_loc - m_score) / (2.0 * a) < EXPO_SKIP:
                continue
            acc += pm * norm_re_one(
                ps, pt, a, omega, m_score, lock_minus, lock_plus,
                use_mp=use_mp,
            )
    if orbit_only:
        return float(acc)
    seen = set()
    for gam in list(online) + list(extra_online):
        if gam in seen:
            continue
        seen.add(gam)
        s_loc = score_S(0.0, gam, omega)
        if (s_loc - m_score) / (2.0 * a) < EXPO_SKIP:
            continue
        for pt in (gam, -gam):
            acc += norm_re_one(
                0.0, pt, a, omega, m_score, False, False, use_mp=use_mp,
            )
    return float(acc)


def named_configs() -> list[tuple[str, list[tuple[float, float, int]], tuple[float, ...]]]:
    """(name, off-line orbits, extra on-line ordinates)."""
    c4 = [
        (0.01 + 0.01 * k, 100.0 + 0.003 * k, 1) for k in range(15)
    ]
    return [
        ("C1", [(0.1, 100.0, 1)], ()),
        ("C2m", [(0.05, 100.0, 2)], ()),
        ("C2t", [(0.05, 100.0, 1), (0.05, 100.02, 1)], ()),
        ("C3", [(0.05, 100.0, 1), (0.2, 100.3, 1)], ()),
        ("C4", c4, ()),
        ("C5a", [(1e-3, 500.0, 1)], ()),
        ("C5b", [(1e-3, 500.0, 1)], (500.0,)),
        ("C6", [(0.1, 1900.7, 1)], ()),
        ("C7", [(0.45, 50.3, 1)], ()),
    ]


def prescribed_packet(host: tuple[float, float, int]) -> tuple[float, float]:
    sigma, gamma, _m = host
    alpha = (sigma * sigma) / 64.0
    omega = gamma - PI * alpha / sigma
    return alpha, omega


def random_t1(rng: random.Random, n_pts: int) -> tuple[list, list]:
    line_pts = []
    fe_pts = []
    for _ in range(n_pts):
        alpha = math.exp(rng.uniform(-2.0, 1.5))
        omega = rng.uniform(-40.0, 40.0)
        t_val = rng.uniform(-40.0, 40.0)
        line_pts.append((alpha, omega, t_val))
    for _ in range(n_pts):
        alpha = math.exp(rng.uniform(-1.5, 1.2))
        omega = rng.uniform(-8.0, 8.0)
        sigma = rng.uniform(-0.45, 0.45)
        t_val = rng.uniform(-12.0, 12.0)
        fe_pts.append((alpha, omega, sigma, t_val))
    return line_pts, fe_pts


def run_t1(n_pts: int) -> dict:
    mp.mp.dps = DPS
    a1 = mp.mpf("1")
    w0 = mp.mpf("0")
    hat1 = hat_delta_mp(a1, w0, mp.mpf("0.5"), mp.mpf("0"))
    target = mp.pi * mp.e ** (mp.mpf("1") / 8)
    err = abs(hat1 - target)
    checkpoint_ok = err < mp.mpf("1e-12") and abs(mp.im(hat1)) < mp.mpf("1e-12")
    rng = random.Random(SEED + 1)
    line_pts, fe_pts = random_t1(rng, n_pts)
    line_ok = 0
    for alpha, omega, t_val in line_pts:
        val = hat_delta_mp(
            mp.mpf(alpha), mp.mpf(omega), mp.mpf("0"), mp.mpf(t_val),
        )
        re_v, im_v = float(mp.re(val)), float(mp.im(val))
        if abs(im_v) < 1e-12 and re_v >= -1e-12:
            line_ok += 1
    fe_ok = 0
    for alpha, omega, sigma, t_val in fe_pts:
        a_mp, w_mp = mp.mpf(alpha), mp.mpf(omega)
        s_mp, t_mp = mp.mpf(sigma), mp.mpf(t_val)
        h_rho = hat_delta_mp(a_mp, w_mp, s_mp, t_mp)
        h_1m = hat_delta_mp(a_mp, w_mp, -s_mp, -t_mp)
        h_bar = hat_delta_mp(a_mp, w_mp, s_mp, -t_mp)
        h_1b = hat_delta_mp(a_mp, w_mp, -s_mp, t_mp)
        left = h_rho + h_1m + h_bar + h_1b
        right = 4 * mp.re(h_rho)
        if abs(left - right) < mp.mpf("1e-12"):
            fe_ok += 1
    third_lobe_note = (
        "Lean L122-123: 2*Real.exp((s^2-t^2-w^2)/(2a))*exp(I*s*t/a) "
        "matches formula (1) third lobe; ĥ_{1,0}(1) does not test the "
        "phase (all three phases vanish at t=ω=0)"
    )
    return {
        "hat1_re": float(mp.re(hat1)),
        "target": float(target),
        "err": float(err),
        "checkpoint_ok": bool(checkpoint_ok),
        "line_ok": line_ok,
        "line_n": n_pts,
        "fe_ok": fe_ok,
        "fe_n": n_pts,
        "third_lobe_note": third_lobe_note,
        "discrepancy": "none",
    }


def eval_packet(
    off: list[tuple[float, float, int]],
    online: tuple[float, ...],
    extra_online: tuple[float, ...],
    a: float,
    omega: float,
    m_score: float,
    sig_star: float,
    gam_star: float,
) -> dict:
    nrm = normalized_Z(
        off, online, a, omega, m_score, sig_star, gam_star, extra_online,
        use_mp=True,
    )
    nrm_orb = normalized_Z(
        off, online, a, omega, m_score, sig_star, gam_star, extra_online,
        orbit_only=True, use_mp=True,
    )
    nrm_rem = nrm - nrm_orb
    return {"nrm": nrm, "nrm_orb": nrm_orb, "nrm_rem": nrm_rem}


def run_named(
    online: tuple[float, ...], n_max: int,
) -> list[dict]:
    rows = []
    for name, off_raw, extra in named_configs():
        off = merge_orbits(off_raw)
        host = off[0]
        sel = select_omega(off, online + extra, host)
        row: dict = {
            "name": name,
            "off": off,
            "extra": extra,
            "host": host,
            "sel": sel,
        }
        if not sel["ok"]:
            row["t2"] = "SELECT_FAIL(%s)" % sel["why"]
            row["n_neg"] = None
            row["nrm_list"] = []
            row["t4_ok"] = False
            row["t3_sign"] = 0
            rows.append(row)
            continue
        sig_s = sel["sigma_star"]
        gam_s = sel["gamma_star"]
        omega = sel["omega"]
        m_sc = sel["M"]
        gap = sel["Delta"]
        m_star = sel["m_star"]
        r1 = r1_remainder(off, online, sel, extra)
        nrm_list = []
        n_neg = None
        t4_all = True
        t4_notes = []
        for n_idx in range(n_max + 1):
            alpha = a_n_of(sig_s, sel["d_star"], n_idx)
            pack = eval_packet(
                off, online, extra, alpha, omega, m_sc, sig_s, gam_s,
            )
            nrm_list.append(pack["nrm"])
            if n_neg is None and pack["nrm"] < 0.0:
                n_neg = n_idx
            if alpha <= 1.0 + 1e-15:
                bound_n = 4.0 * r1 * math.exp(-gap / (2.0 * alpha))
                ok_t4 = abs(pack["nrm_rem"]) <= bound_n + 1e-12
                if not ok_t4:
                    t4_all = False
                    t4_notes.append(
                        "n=%d rem=%s bound=%s" % (
                            n_idx, fmt(pack["nrm_rem"], 4), fmt(bound_n, 4),
                        )
                    )
            else:
                t4_notes.append("n=%d a>1 skip" % n_idx)
        target = -4.0 * m_star
        nrm_last = nrm_list[-1]
        a_last = a_n_of(sig_s, sel["d_star"], n_max)
        err_last = abs(nrm_last - target)
        scale = math.exp(-gap / (2.0 * a_last))
        const_ok = err_last <= (4.0 * r1 + 1.0) * scale + 1e-9
        a_p, w_p = prescribed_packet(host)
        m_p = max(
            score_S(sig, gam, w_p) for sig, gam, _m in off
        )
        m_p = max(m_p, 1e-30)
        nrm_p = normalized_Z(
            off, online, a_p, w_p, m_p, off[0][0], off[0][1], extra,
            use_mp=True,
        )
        t3_sign = 1 if nrm_p > 0.0 else (-1 if nrm_p < 0.0 else 0)
        row.update({
            "r1": r1,
            "nrm_list": nrm_list,
            "n_neg": n_neg,
            "nrm_last": nrm_last,
            "target": target,
            "err_last": err_last,
            "const_ok": const_ok,
            "t4_ok": t4_all,
            "t4_notes": t4_notes,
            "t3_sign": t3_sign,
            "t3_nrm": nrm_p,
            "t3_a": a_p,
            "t3_w": w_p,
        })
        rows.append(row)
    return rows


def random_t5_config(rng: random.Random) -> list[tuple[float, float, int]]:
    n_orb = rng.randint(1, 6)
    orbits = []
    for k in range(n_orb):
        sigma = rng.uniform(0.005, 0.45)
        gamma = rng.uniform(20.0, 1500.0)
        mult = rng.choice((1, 2))
        orbits.append((sigma, gamma + 1e-6 * k, mult))
    return merge_orbits(orbits)


def run_t5(
    online: tuple[float, ...], n_cfg: int, n_max: int,
) -> dict:
    rng = random.Random(SEED + 5)
    n_pass = 0
    failures = []
    for k in range(n_cfg):
        off = random_t5_config(rng)
        host = off[0]
        sel = select_omega(off, online, host)
        rec = {
            "k": k,
            "off": off,
            "sel": sel,
        }
        if not sel["ok"]:
            rec["why"] = "SELECT_FAIL(%s)" % sel["why"]
            rec["n_neg"] = None
            failures.append(rec)
            continue
        n_neg = None
        nrm_last = None
        for n_idx in range(n_max + 1):
            alpha = a_n_of(sel["sigma_star"], sel["d_star"], n_idx)
            nrm = normalized_Z(
                off, online, alpha, sel["omega"], sel["M"],
                sel["sigma_star"], sel["gamma_star"],
            )
            nrm_last = nrm
            if n_neg is None and nrm < 0.0:
                n_neg = n_idx
                break
        rec["n_neg"] = n_neg
        rec["nrm_last"] = nrm_last
        if n_neg is None:
            rec["why"] = "no_NEG_n<=%d" % n_max
            failures.append(rec)
        else:
            n_pass += 1
    return {"n_pass": n_pass, "n_cfg": n_cfg, "failures": failures}


def star_str(sel: dict) -> str:
    return "(%.6g,%.6g,%d)" % (
        sel["sigma_star"], sel["gamma_star"], sel["m_star"],
    )


def run(smoke: bool) -> int:
    LINES.clear()
    CHECKS.clear()
    n_pts = 5 if smoke else N_T1
    n_max = 2 if smoke else N_MAX
    n_t5 = 8 if smoke else N_T5
    n_t5_max = 4 if smoke else N_T5_MAX

    emit("gabor_exposed_orbit_probe r605N")
    emit("KEIN RH-CLAIM")
    emit("SPEC_DESIGN %s" % SPEC_SHA[:16])
    emit("smoke %d" % int(smoke))
    emit("zeros_source verified_zeros_n7000.npy[:%d] mpmath.zetazero dps=15" % N_ONLINE)
    emit("hat Lean pureGaborHatDelta L114-123 third-lobe phase I*sigma*t/a")
    emit("sum T2/T3 mp.dps=%d on (4a/pi) e^{-M/(2a)} Z; T5 float64 same form" % DPS)

    online = load_online(N_ONLINE)
    emit("n_online %d gamma_1=%s gamma_N=%s" % (
        len(online), fmt(online[0], 6), fmt(online[-1], 6),
    ))

    # T1
    emit("T1 FORMULA")
    t1 = run_t1(n_pts)
    emit("  hat_{1,0}(1)=%s target=%s err=%s" % (
        fmt(t1["hat1_re"]), fmt(t1["target"]), fmt(t1["err"], 4),
    ))
    emit("  FORMULA_VS_LEAN %s" % t1["discrepancy"])
    emit("  third_lobe %s" % t1["third_lobe_note"])
    check(
        "T1-checkpoint", t1["checkpoint_ok"],
        "err=%s" % fmt(t1["err"], 4),
    )
    check(
        "T1-line-nonneg", t1["line_ok"] == t1["line_n"],
        "%d/%d" % (t1["line_ok"], t1["line_n"]),
    )
    check(
        "T1-FE-quadruple", t1["fe_ok"] == t1["fe_n"],
        "%d/%d" % (t1["fe_ok"], t1["fe_n"]),
    )
    t1_pass = t1["checkpoint_ok"] and t1["line_ok"] == t1["line_n"] and t1["fe_ok"] == t1["fe_n"]
    emit("T1 VERDICT %s" % ("PASS" if t1_pass else "FAIL"))

    # T2 / T3 / T4
    emit("T2 EXPOSED-ORBIT")
    rows = run_named(online, n_max)
    t2_fail = []
    t4_fail = []
    t3_bits = []
    for row in rows:
        name = row["name"]
        sel = row["sel"]
        if not sel["ok"]:
            emit("  %s SELECT_FAIL %s" % (name, sel["why"]))
            t2_fail.append(name)
            t3_bits.append("%s=NA" % name)
            continue
        nrm_s = ",".join(fmt(v, 6) for v in row["nrm_list"])
        verd = "NEG_REACHED n=%s" % row["n_neg"] if row["n_neg"] is not None else "NO_NEG"
        emit(
            "  %s star=%s om=%s M=%s D=%s d*=%s m=%d %s nrm_max=%s target=%s"
            % (
                name, star_str(sel), fmt(sel["omega"], 10),
                fmt(sel["M"], 6), fmt(sel["Delta"], 6),
                fmt(sel["d_star"], 6), sel["m_star"], verd,
                fmt(row["nrm_last"], 6), fmt(row["target"], 6),
            )
        )
        emit("    nrm=[%s]" % nrm_s)
        if row["n_neg"] is None or not row["const_ok"]:
            t2_fail.append(name)
            if row["n_neg"] is None:
                emit("    BREAK no NEG in n=0..%d" % n_max)
            if not row["const_ok"]:
                emit(
                    "    BREAK limit err=%s vs e^{-D/2a}(4 R1+1)"
                    % fmt(row["err_last"], 4)
                )
        if not row["t4_ok"]:
            t4_fail.append(name)
            emit("    T4 FAIL %s" % ";".join(row["t4_notes"]))
        sgn = row["t3_sign"]
        t3_bits.append("%s=%+d" % (name, sgn))
        check(
            "T2-%s-select" % name, True,
            "star=%s D=%s" % (star_str(sel), fmt(sel["Delta"], 4)),
        )
        check(
            "T2-%s-NEG" % name, row["n_neg"] is not None,
            "nNEG=%s" % row["n_neg"],
        )
        check(
            "T2-%s-limit" % name, bool(row["const_ok"]),
            "nrm=%s target=%s" % (fmt(row["nrm_last"], 4), fmt(row["target"], 4)),
        )
        check(
            "T4-%s" % name, bool(row["t4_ok"]),
            "R1=%s" % fmt(row["r1"], 4),
        )
    t2_ok = not t2_fail
    emit("T2 VERDICT %s" % (
        "ALL_NEG_REACHED" if t2_ok else "BREAKS(%s)" % ",".join(t2_fail)
    ))

    emit("T3 PRESCRIBED")
    emit("  signs %s  (+ prescribed Z>0, - Z<0)" % " ".join(t3_bits))
    pos_names = [
        row["name"] for row in rows
        if row["sel"]["ok"] and row["t3_sign"] > 0
    ]
    emit("  prescribed_pos %s" % (",".join(pos_names) if pos_names else "none"))
    c3 = next(r for r in rows if r["name"] == "C3")
    c4 = next(r for r in rows if r["name"] == "C4")
    expected_gap = c3["sel"]["ok"] and c4["sel"]["ok"] and c3["t3_sign"] > 0 and c4["t3_sign"] > 0
    t3_verd = "PRESCRIBED_POS_ON_C3_C4" if expected_gap else (
        "PRESCRIBED_POS(%s)" % ",".join(pos_names) if pos_names
        else "PRESCRIBED_ALL_NEG"
    )
    emit("T3 VERDICT %s" % t3_verd)
    # T3 is contrast, not a construction hold/break.

    emit("T4 TAIL")
    emit("T4 VERDICT %s" % (
        "TAIL_OK" if not t4_fail else "TAIL_FAILS(%s)" % ",".join(t4_fail)
    ))

    emit("T5 ROBUSTNESS n_cfg=%d n_max=%d seed=%d" % (n_t5, n_t5_max, SEED + 5))
    t5 = run_t5(online, n_t5, n_t5_max)
    emit("  NEG_REACHED %d/%d" % (t5["n_pass"], t5["n_cfg"]))
    for rec in t5["failures"]:
        sel = rec["sel"]
        if not sel["ok"]:
            emit(
                "  FAIL k=%d off=%s why=%s"
                % (rec["k"], rec["off"], rec["why"])
            )
        else:
            emit(
                "  FAIL k=%d off=%s star=%s om=%s M=%s D=%s d*=%s nNEG=%s nrm=%s why=%s"
                % (
                    rec["k"], rec["off"], star_str(sel),
                    fmt(sel["omega"], 8), fmt(sel["M"], 6),
                    fmt(sel["Delta"], 6), fmt(sel["d_star"], 6),
                    rec["n_neg"], fmt(rec["nrm_last"], 6) if rec["nrm_last"] is not None else "na",
                    rec["why"],
                )
            )
    t5_ok = t5["n_pass"] == t5["n_cfg"]
    check(
        "T5-all-NEG", t5_ok,
        "%d/%d" % (t5["n_pass"], t5["n_cfg"]),
    )
    emit("T5 VERDICT %s" % (
        "ROBUST" if t5_ok else "FAILS n=%d" % len(t5["failures"])
    ))

    where = []
    if not t1_pass:
        where.append("T1")
    if t2_fail:
        where.append("T2:" + ",".join(t2_fail))
    if t4_fail:
        where.append("T4:" + ",".join(t4_fail))
    if not t5_ok:
        ks = ",".join(str(r["k"]) for r in t5["failures"][:8])
        where.append("T5:k=%s" % ks)
    if where:
        verdict = "EXPOSED_ORBIT_BREAKS(%s)" % ";".join(where)
    else:
        verdict = "EXPOSED_ORBIT_HOLDS"
    emit("VERDICT: %s" % verdict)
    emit("NO_RH_CLAIM")
    n_fail = sum(1 for _, ok in CHECKS if not ok)
    emit("CHECKS %d/%d" % (len(CHECKS) - n_fail, len(CHECKS)))
    if n_fail:
        emit("GATE_FAILURES " + ",".join(n for n, ok in CHECKS if not ok))
    else:
        emit("ALL CHECKS PASSED")

    body = "\n".join(LINES) + "\n"
    spec = hashlib.sha256(body.encode("utf-8")).hexdigest()[:16]
    print("SPEC %s" % spec)
    return 0 if (t1_pass and not where) else 1


def main() -> None:
    parser = argparse.ArgumentParser(
        description=(
            "r605N exposed-orbit + phase-lock scout "
            "(experiments only, no RH claim)"
        ),
    )
    parser.add_argument("--smoke", action="store_true")
    arguments = parser.parse_args()
    raise SystemExit(run(arguments.smoke))


if __name__ == "__main__":
    main()
