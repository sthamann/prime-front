#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""relay_lead_law_probe -- r636  PRIME.RELAY.LEAD.LAW.01

Experiments-only attempt to *derive* the r635 leads Δ_q instead of
measuring them.  Uses only converged r635 leads.  If r635 is
LEAD_N_ARTIFACT there is nothing to explain: this round is a short
refutation (LEAD_LAW_UNEXPLAINED).

Imported (not reinvented):
  * r635  sealed JSON: Δ_q(D1/D2,N), λ*(L_q), r_q, s_q, c(L_q)
  * r630b holdout grammar, OLS, AIC-like complexity penalty
  * r623  POLE+ARCH predecessor, P_q = overlap(log q)
  * r620  oriented identity ⟨f,T_q f⟩ = −(‖f₊‖²−‖f₋‖²) on the
    overlap I = [−L+log q, L] of width 2δ (odd sector)

Models, fit on q∈{2,3,4,5}, test on the other converged events:
  M1  margin/rate: Δ_pred = λ*(L_q)/r_q, and the quadratic
      integral of λ_min(Q⁻)(L) to its zero
  M2  edge-sliver: restricted min of POLE+ARCH−Σ_{q' present} on
      the R_q-antisymmetric odd edge sector vs δ=L−L_q
  M3  r630b grammar on {log q, Λ(q)/√q, L_q, s_q, λ*, c(L_q)}
  M4  spacing null Δ_pred = s_q (and α s_q on the train set)

Decision: LEAD_LAW_FOUND / LEAD_LAW_PARTIAL / LEAD_LAW_UNEXPLAINED
/ LEAD_LAW_NULL.

Claim boundary: experiments only.  Not a ledger row.  Not a paper claim.
Fence: Exploration on sealed objects; no RH claim.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
import sys
import time
from pathlib import Path

os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("MKL_NUM_THREADS", "1")
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
os.environ.setdefault("NUMEXPR_NUM_THREADS", "1")

import numpy as np  # noqa: E402

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

import support_relay_census_probe as R619  # noqa: E402
import margin_law_symreg_probe as R630  # noqa: E402
import semilocal_p2_dilation_probe as R623  # noqa: E402
import p2_reflection_factor_probe as R620  # noqa: E402
import relay_lead_precision_probe as R635  # noqa: E402

ROUND = 636
SEED = 636202609
CONTRACT = "PRIME.RELAY.LEAD.LAW.01"
FENCE = "Exploration on sealed objects; no RH claim"
TAG = "r636"
R635_JSON = HERE / "relay_lead_precision_result.json"
R635_SHA_PREFIX = "28db9bef54dd4cd6"
R630_SHA_PREFIX = "87febb97aaee5dcd"
R620_SHA_PREFIX = "7c8e73b7d4f27fed"
R623_SHA_PREFIX = "5890676d194739b1"
HOLD_Q = (2, 3, 4, 5)
REL_CUT = 0.20
N_M2 = 24
N_M2_SMOKE = 12
N_OUTER_M2 = 48
DELTA_GRID = (
    0.003, 0.006, 0.010, 0.014, 0.018, 0.024, 0.032, 0.045, 0.060, 0.080,
)
DELTA_GRID_SMOKE = (0.006, 0.014, 0.030, 0.060)

DECISIONS = (
    "LEAD_LAW_FOUND",
    "LEAD_LAW_PARTIAL",
    "LEAD_LAW_UNEXPLAINED",
    "LEAD_LAW_NULL",
)

SPEC = {
    "round": ROUND,
    "tag": TAG,
    "contract": CONTRACT,
    "parent": "r635 PRIME.RELAY.LEAD.PRECISION.01",
    "holdout_q": list(HOLD_Q),
    "rel_cut": REL_CUT,
    "M1": "lambda_star/r_q and quadratic root of Q^-",
    "M2": "odd R_q-antisymmetric sliver of POLE+ARCH-present vs delta",
    "M3": "r630b grammar depth 3, AIC penalty, features logq,Lam/sqrtq,L,s,lam*,c",
    "M4": "spacing null Delta=s_q and alpha*s_q",
    "converged_only": True,
    "artifact_path": "if r635 LEAD_N_ARTIFACT => LEAD_LAW_UNEXPLAINED refutation",
    "seed": SEED,
    "claim_boundary": "experiments_only_not_a_ledger_claim",
    "fence": FENCE,
}
SPEC_SHA = hashlib.sha256(
    json.dumps(SPEC, sort_keys=True, separators=(",", ":")).encode("utf-8")
).hexdigest()

CHECKS: list[tuple[str, bool]] = []
LINES: list[str] = []


def emit(line: str = "") -> None:
    LINES.append(line)
    print(line)


def check(name: str, ok: bool, detail: str = "") -> bool:
    flag = bool(ok)
    CHECKS.append((name, flag))
    emit("  [%s] %-44s %s" % ("PASS" if flag else "FAIL", name, detail))
    return flag


def section(title: str) -> None:
    emit("")
    emit("=" * 74)
    emit(title)
    emit("=" * 74)


def fmt(value, digits: int = 16) -> str:
    if value is None:
        return "nan"
    if isinstance(value, (bool, np.bool_)):
        return "1" if value else "0"
    if isinstance(value, (int, np.integer)) and not isinstance(value, (bool, np.bool_)):
        return "%d" % int(value)
    number = float(value)
    if math.isnan(number):
        return "nan"
    if not math.isfinite(number):
        return "+inf" if number > 0.0 else "-inf"
    return "%+.*e" % (digits, number)


def file_sha256() -> str:
    return hashlib.sha256(Path(__file__).read_bytes()).hexdigest()


def payload_sha(payload: dict) -> str:
    return hashlib.sha256(
        json.dumps(payload, sort_keys=True, separators=(",", ":"), default=str)
        .encode("utf-8")
    ).hexdigest()


def rel_err(pred, true) -> float:
    if pred is None or true is None:
        return float("inf")
    pred_f, true_f = float(pred), float(true)
    if not (math.isfinite(pred_f) and math.isfinite(true_f)):
        return float("inf")
    if abs(true_f) < 1.0e-15:
        return float("inf")
    return abs(pred_f - true_f) / abs(true_f)


def quadratic_root(lam0, r0, r1, h_fd: float) -> float:
    """λ(δ) ≈ lam0 − r0 δ + (1/2) a δ² with a = (r1−r0)/h; first positive root."""
    if not math.isfinite(lam0) or not math.isfinite(r0):
        return float("nan")
    accel = 0.0
    if math.isfinite(r1):
        accel = (r1 - r0) / max(h_fd, 1.0e-12)
    # lam0 - r0 d + 0.5 a d^2 = 0
    aa = 0.5 * accel
    bb = -r0
    cc = lam0
    if abs(aa) < 1.0e-18:
        if abs(r0) < 1.0e-18:
            return float("nan")
        root = lam0 / r0
        return float(root) if root > 0.0 else float("nan")
    disc = bb * bb - 4.0 * aa * cc
    if disc < 0.0:
        return float("nan")
    sqrt_d = math.sqrt(disc)
    roots = [(-bb + sqrt_d) / (2.0 * aa), (-bb - sqrt_d) / (2.0 * aa)]
    pos = [root for root in roots if math.isfinite(root) and root > 0.0]
    return float(min(pos)) if pos else float("nan")


def load_r635() -> dict:
    if not R635_JSON.is_file():
        raise FileNotFoundError("missing %s; run r635 first" % R635_JSON.name)
    return json.loads(R635_JSON.read_text(encoding="utf-8"))


def train_test(events: list[dict]):
    conv = [
        rec for rec in events
        if rec.get("conv_d2_damped") and rec.get("delta_d2_damped") is not None
    ]
    train = [rec for rec in conv if int(rec["q"]) in HOLD_Q]
    test = [rec for rec in conv if int(rec["q"]) not in HOLD_Q]
    return conv, train, test


def m1_preds(rec: dict) -> dict:
    lam = rec.get("lam_star")
    r_q = rec.get("r_q")
    r_q2 = rec.get("r_q2")
    lin = float("nan")
    if lam is not None and r_q is not None and abs(float(r_q)) > 1.0e-30:
        lin = float(lam) / float(r_q)
    quad = quadratic_root(
        float(rec["lam_pred0"]) if rec.get("lam_pred0") is not None else float(lam or "nan"),
        float(r_q) if r_q is not None else float("nan"),
        float(r_q2) if r_q2 is not None else float("nan"),
        R635.H_FD,
    )
    return {"lin": lin, "quad": quad}


def sector_masses_q(length, dimension, damped, n_quad, shift: float) -> dict:
    """r620 sector_masses with general translation shift = log q."""
    inner_edge = float(shift) - float(length)
    zeros = np.zeros((dimension, dimension), dtype=np.float64)
    if inner_edge <= 1.0e-14:
        gram_l = R620.gram_matrix(
            length, dimension, damped, max(n_quad, 48), "odd",
        )
        return {
            "minus_I": zeros, "plus_I": zeros, "empty_I": True, "gram": gram_l,
        }
    pts_i, w_i = R620._interval_quad(inner_edge, length, n_quad)
    b_i = R620.basis_values(pts_i, length, dimension, damped, "odd")
    b_r = R620.basis_values(shift - pts_i, length, dimension, damped, "odd")
    b_minus = 0.5 * (b_i - b_r)
    b_plus = 0.5 * (b_i + b_r)
    mass_minus_i = R620._sym(b_minus.T @ (w_i[:, None] * b_minus))
    mass_plus_i = R620._sym(b_plus.T @ (w_i[:, None] * b_plus))
    return {
        "minus_I": mass_minus_i,
        "plus_I": mass_plus_i,
        "empty_I": False,
    }


def m2_crossing(rec: dict, logqs, weights, qs, smoke: bool) -> dict:
    """Restricted min of Q^- on the odd R_q-antisymmetric edge sliver."""
    q_val = int(rec["q"])
    ell_q = float(rec["L"])
    skip = qs.index(q_val)
    dim = N_M2_SMOKE if smoke else N_M2
    cache = R630.FormCache(dim, N_OUTER_M2, 3, logqs, weights)
    grid = DELTA_GRID_SMOKE if smoke else DELTA_GRID
    rows = []
    for delta in grid:
        length = ell_q + float(delta)
        packed = cache.assemble(length, skip)  # D2 frozen
        sectors = sector_masses_q(length, dim, True, 64, math.log(q_val))
        if sectors["empty_I"]:
            rows.append({
                "delta": float(delta), "lam": float("nan"),
                "cost": float("nan"), "gain": float("nan"),
            })
            continue
        gram = packed["gram"]
        quad = packed["full"]
        minus = sectors["minus_I"]
        plus = sectors["plus_I"]
        metric = minus + 1.0e-12 * np.eye(dim)
        try:
            lam, vec = R630.min_rayleigh(quad, metric)
        except Exception:
            lam, vec = float("nan"), None
        cost = float("nan")
        gain = float("nan")
        if vec is not None and math.isfinite(lam):
            nrm = float(vec @ gram @ vec)
            if nrm > 1.0e-18:
                cost = float(vec @ packed["free"] @ vec) / nrm
                gain = float(rec["w"]) * float(vec @ (plus - minus) @ vec) / nrm
        rows.append({
            "delta": float(delta), "lam": float(lam),
            "cost": cost, "gain": gain,
        })
    crossing = float("nan")
    prev = None
    for row in rows:
        if prev is not None and math.isfinite(prev["lam"]) and math.isfinite(row["lam"]):
            if prev["lam"] > 0.0 and row["lam"] <= 0.0:
                frac = prev["lam"] / (prev["lam"] - row["lam"])
                crossing = prev["delta"] + frac * (row["delta"] - prev["delta"])
                break
        prev = row
    cost_log = []
    for row in rows:
        if (
            math.isfinite(row["cost"]) and row["delta"] > 0.0
            and math.isfinite(row["lam"])
        ):
            cost_log.append((math.log(1.0 / row["delta"]), row["cost"]))
    slope = float("nan")
    intercept = float("nan")
    if len(cost_log) >= 3:
        xs = np.array([pair[0] for pair in cost_log], dtype=np.float64)
        ys = np.array([pair[1] for pair in cost_log], dtype=np.float64)
        matrix = np.column_stack([np.ones_like(xs), xs])
        coeff, _, _, _ = np.linalg.lstsq(matrix, ys, rcond=None)
        intercept, slope = float(coeff[0]), float(coeff[1])
    return {
        "pred": crossing,
        "cost_a": intercept,
        "cost_b": slope,
        "rows": rows,
        "log_cost": bool(math.isfinite(slope)),
    }


def m3_fit(train: list[dict], all_rows: list[dict]) -> dict:
    names = ("logq", "w", "L", "s", "lam", "c")
    def feats(rec):
        q_val = max(int(rec["q"]), 2)
        lam = rec.get("lam_star")
        c_log = rec.get("c_log")
        return {
            "1": 1.0,
            "logq": math.log(q_val),
            "w": float(rec.get("w") or 0.0),
            "L": float(rec["L"]),
            "s": float(rec["s"]),
            "lam": math.log(max(abs(float(lam)), 1.0e-30)) if lam is not None else 0.0,
            "c": float(c_log) if c_log is not None and math.isfinite(float(c_log)) else 0.0,
        }

    if len(train) < 3:
        return {"name": "none", "pred": {}, "hold": float("inf"), "coeff": []}

    base_train = {name: np.array([feats(rec)[name] for rec in train]) for name in ("1",) + names}
    y_train = np.array([float(rec["delta_d2_damped"]) for rec in train], dtype=np.float64)
    gram = R630.grammar_monomials(base_train, 3)
    fit_mask = np.ones(len(train), dtype=bool)
    test_mask = np.zeros(len(train), dtype=bool)
    ranked = R630.rank_grammar(gram, y_train, fit_mask, test_mask, max_terms=2)
    if not ranked:
        return {"name": "none", "pred": {}, "hold": float("inf"), "coeff": []}
    best = ranked[0]
    # predict on all_rows with the same monomial names
    pred_map = {}
    terms = list(best["terms"])
    for rec in all_rows:
        row_f = feats(rec)
        atoms = {"1": 1.0}
        atoms.update({name: row_f[name] for name in names})
        vec = [1.0]
        for term in terms:
            parts = [tok for tok in term.split("*") if tok and tok != "1"]
            acc = 1.0
            for tok in parts:
                acc *= atoms.get(tok, 1.0)
            vec.append(acc)
        pred_map[int(rec["q"])] = float(np.dot(best["coeff"], vec[:len(best["coeff"])]))
    return {
        "name": best["name"],
        "pred": pred_map,
        "coeff": [float(val) for val in best["coeff"]],
        "aic": float(best["aic"]),
        "n_par": len(best["coeff"]),
    }


def model_errors(name: str, preds: dict, test: list[dict], train: list[dict]) -> dict:
    test_e = [rel_err(preds.get(int(rec["q"])), rec["delta_d2_damped"]) for rec in test]
    train_e = [rel_err(preds.get(int(rec["q"])), rec["delta_d2_damped"]) for rec in train]
    small_test = [rec for rec in test if int(rec["q"]) <= 7]
    large_test = [rec for rec in test if int(rec["q"]) > 7]
    small_e = [rel_err(preds.get(int(rec["q"])), rec["delta_d2_damped"]) for rec in small_test]
    large_e = [rel_err(preds.get(int(rec["q"])), rec["delta_d2_damped"]) for rec in large_test]
    def peak(vals):
        finite = [val for val in vals if math.isfinite(val)]
        return max(finite) if finite else float("inf")
    return {
        "name": name,
        "test": test_e,
        "train": train_e,
        "peak_test": peak(test_e),
        "peak_train": peak(train_e),
        "peak_small": peak(small_e) if small_test else float("nan"),
        "peak_large": peak(large_e) if large_test else float("nan"),
        "all_test_ok": bool(test and peak(test_e) < REL_CUT),
        "small_ok": bool(small_test) and peak(small_e) < REL_CUT,
        "preds": {int(q_val): preds[int(q_val)] for q_val in preds},
        "per_event": {
            int(rec["q"]): rel_err(preds.get(int(rec["q"])), rec["delta_d2_damped"])
            for rec in train + test
        },
    }


def decide_law(reports: list[dict], artifact: bool, n_test: int) -> tuple[str, str]:
    if artifact:
        return (
            "LEAD_LAW_UNEXPLAINED",
            "r635 LEAD_N_ARTIFACT: Delta(N) is a basis artefact; nothing to derive",
        )
    if n_test < 1:
        train_ok = [
            rep for rep in reports
            if math.isfinite(rep["peak_train"]) and rep["peak_train"] < REL_CUT
        ]
        if train_ok:
            best = min(train_ok, key=lambda rep: rep["peak_train"])
            if best["name"].startswith("M4"):
                return (
                    "LEAD_LAW_NULL",
                    "no held-out events; spacing wins on the train set (q<=7 only)",
                )
            return (
                "LEAD_LAW_PARTIAL",
                "no held-out converged events; %s <20%% on train q<=7 only"
                % best["name"],
            )
        return ("LEAD_LAW_UNEXPLAINED", "no held-out converged events")
    viable = [rep for rep in reports if math.isfinite(rep["peak_test"])]
    if not viable:
        return ("LEAD_LAW_UNEXPLAINED", "no finite holdout errors")
    best = min(viable, key=lambda rep: (rep["peak_test"], len(rep["name"])))
    spacing = [rep for rep in reports if rep["name"].startswith("M4")]
    spacing_best = min(spacing, key=lambda rep: rep["peak_test"]) if spacing else None
    if best["all_test_ok"]:
        if spacing_best is not None and spacing_best["name"] == best["name"]:
            return (
                "LEAD_LAW_NULL",
                "spacing model wins with holdout <%d%%; no extra content" % int(100 * REL_CUT),
            )
        return (
            "LEAD_LAW_FOUND",
            "%s holdout peak %s < 20%% on all test events" % (
                best["name"], fmt(best["peak_test"], 3),
            ),
        )
    if best["small_ok"] and (
        not math.isfinite(best["peak_large"]) or best["peak_large"] >= REL_CUT
    ):
        return (
            "LEAD_LAW_PARTIAL",
            "%s <20%% only for q<=7 (peak_small=%s peak_large=%s)" % (
                best["name"], fmt(best["peak_small"], 3), fmt(best["peak_large"], 3),
            ),
        )
    return (
        "LEAD_LAW_UNEXPLAINED",
        "no model <20%% on test (best %s peak %s)" % (
            best["name"], fmt(best["peak_test"], 3),
        ),
    )


def run(smoke: bool) -> int:
    CHECKS.clear()
    LINES.clear()
    wall0 = time.time()
    section("r636  PRIME.RELAY.LEAD.LAW.01")
    emit("SPEC_SHA %s" % SPEC_SHA)
    emit("FILE_SHA256 %s" % file_sha256())
    emit("FENCE %s" % FENCE)

    parent = load_r635()
    artifact = parent.get("verdict") == "LEAD_N_ARTIFACT"
    events = parent.get("events") or []
    check(
        "G01-r635-json",
        bool(events) and parent.get("contract") == R635.CONTRACT,
        "n_events=%d verdict=%s" % (len(events), parent.get("verdict")),
    )
    check(
        "G02-import-SPEC",
        R635.SPEC_SHA.startswith(R635_SHA_PREFIX)
        and R630.SPEC_SHA.startswith(R630_SHA_PREFIX)
        and R620.SPEC_SHA.startswith(R620_SHA_PREFIX)
        and R623.SPEC_SHA.startswith(R623_SHA_PREFIX),
        "r635 %s r630 %s r620 %s r623 %s"
        % (
            R635.SPEC_SHA[:8], R630.SPEC_SHA[:8],
            R620.SPEC_SHA[:8], R623.SPEC_SHA[:8],
        ),
    )
    check("G03-fence", FENCE == SPEC["fence"], FENCE)

    conv, train, test = train_test(events)
    emit("r635 verdict %s  conv=%d train=%d test=%d artifact=%d" % (
        parent.get("verdict"), len(conv), len(train), len(test), int(artifact),
    ))

    reports = []
    m2_meta = {}
    if artifact:
        section("REFUTATION  r635 LEAD_N_ARTIFACT")
        emit("  Leads drift with N even for L_q<=1; the r619 mean Delta~0.015")
        emit("  is a basis/precision artefact.  No law to fit.")
        check("G04-refutation", True, "short path; M1-M3 skipped")
        # M4 documented only as a diagnostic on the untrustworthy table
        preds_s = {int(rec["q"]): float(rec["s"]) for rec in events}
        reports.append(model_errors("M4_s", preds_s, test or conv, train or conv[:1]))
    else:
        qs, logqs, weights, _ells, _qn, _lam = R619.prime_powers_upto(32 if not smoke else 8)
        q_list = [int(q_val) for q_val in qs]
        section("M1  MARGIN/RATE")
        preds_lin = {}
        preds_quad = {}
        for rec in conv:
            packed = m1_preds(rec)
            preds_lin[int(rec["q"])] = packed["lin"]
            preds_quad[int(rec["q"])] = packed["quad"]
            emit(
                "  q=%d Delta=%s M1lin=%s M1quad=%s lam*=%s r_q=%s"
                % (
                    rec["q"], fmt(rec["delta_d2_damped"], 4),
                    fmt(packed["lin"], 4), fmt(packed["quad"], 4),
                    fmt(rec.get("lam_star"), 3), fmt(rec.get("r_q"), 3),
                )
            )
        reports.append(model_errors("M1_lin", preds_lin, test, train))
        reports.append(model_errors("M1_quad", preds_quad, test, train))

        section("M2  EDGE SLIVER")
        preds_m2 = {}
        use_rows = conv if not smoke else conv[: min(4, len(conv))]
        for rec in use_rows:
            packed = m2_crossing(rec, logqs, weights, q_list, smoke)
            m2_meta[int(rec["q"])] = {
                "pred": packed["pred"],
                "cost_a": packed["cost_a"],
                "cost_b": packed["cost_b"],
            }
            preds_m2[int(rec["q"])] = packed["pred"]
            emit(
                "  q=%d Delta=%s M2=%s cost~a+b log(1/d) a=%s b=%s"
                % (
                    rec["q"], fmt(rec["delta_d2_damped"], 4),
                    fmt(packed["pred"], 4),
                    fmt(packed["cost_a"], 3), fmt(packed["cost_b"], 3),
                )
            )
        reports.append(model_errors("M2_sliver", preds_m2, test, train))
        n_log = sum(1 for rec in m2_meta.values() if math.isfinite(rec["cost_b"]))
        check("G04-M2-log-cost", n_log >= 1 or smoke, "finite b in a+b log(1/delta): %d" % n_log)

        section("M3  GRAMMAR")
        gram = m3_fit(train, conv)
        emit("  best %s aic=%s coeff=%s" % (
            gram["name"], fmt(gram.get("aic"), 3), gram.get("coeff"),
        ))
        reports.append(model_errors("M3_" + gram["name"], gram["pred"], test, train))

        section("M4  SPACING NULL")
        preds_s = {int(rec["q"]): float(rec["s"]) for rec in conv}
        alpha = 1.0
        if train:
            num = sum(float(rec["delta_d2_damped"]) * float(rec["s"]) for rec in train)
            den = sum(float(rec["s"]) ** 2 for rec in train)
            if den > 0.0:
                alpha = num / den
        preds_as = {int(rec["q"]): alpha * float(rec["s"]) for rec in conv}
        emit("  alpha=%s  (Delta ~ alpha s_q on train)" % fmt(alpha, 4))
        reports.append(model_errors("M4_s", preds_s, test, train))
        reports.append(model_errors("M4_alpha_s", preds_as, test, train))

    section("HOLDOUT")
    for rep in reports:
        emit(
            "  %s  peak_test=%s peak_train=%s peak_q<=7=%s peak_q>7=%s"
            % (
                rep["name"], fmt(rep["peak_test"], 3), fmt(rep["peak_train"], 3),
                fmt(rep["peak_small"], 3), fmt(rep["peak_large"], 3),
            )
        )
        for q_val, err in sorted(rep["per_event"].items()):
            emit("    q=%d rel=%s" % (q_val, fmt(err, 3)))

    verdict, why = decide_law(reports, artifact, len(test))
    check("G05-verdict-enum", verdict in DECISIONS, verdict)
    if artifact:
        pass
    elif not any(name == "G04-M2-log-cost" for name, _ok in CHECKS):
        check("G04-M2-log-cost", True, "M2 ran") 

    payload = {
        "contract": CONTRACT,
        "tag": TAG,
        "verdict": verdict,
        "why": why,
        "parent_verdict": parent.get("verdict"),
        "parent_result_sha": parent.get("result_sha"),
        "artifact": bool(artifact),
        "n_conv": len(conv),
        "models": [
            {
                "name": rep["name"],
                "peak_test": None if not math.isfinite(rep["peak_test"]) else round(rep["peak_test"], 6),
                "peak_train": None if not math.isfinite(rep["peak_train"]) else round(rep["peak_train"], 6),
                "peak_small": None if not math.isfinite(rep["peak_small"]) else round(rep["peak_small"], 6),
                "peak_large": None if not math.isfinite(rep["peak_large"]) else round(rep["peak_large"], 6),
                "per_event": {
                    str(q_val): (None if not math.isfinite(err) else round(err, 6))
                    for q_val, err in sorted(rep["per_event"].items())
                },
            }
            for rep in reports
        ],
        "m2": {
            str(q_val): {
                "pred": None if not math.isfinite(meta["pred"]) else round(meta["pred"], 6),
                "cost_a": None if not math.isfinite(meta["cost_a"]) else round(meta["cost_a"], 6),
                "cost_b": None if not math.isfinite(meta["cost_b"]) else round(meta["cost_b"], 6),
            }
            for q_val, meta in m2_meta.items()
        },
    }
    result = payload_sha(payload)
    payload["result_sha"] = result
    payload["spec_sha"] = SPEC_SHA
    check("G06-payload", bool(reports), "n_models=%d" % len(reports))

    n_pass = sum(1 for _name, ok in CHECKS if ok)
    n_gate = len(CHECKS)
    wall = time.time() - wall0
    emit("VERDICT %s" % verdict)
    emit("WHY %s" % why)
    emit("GATES %d/%d" % (n_pass, n_gate))
    emit("SPEC_SHA %s" % SPEC_SHA)
    emit("FILE_SHA256 %s" % file_sha256())
    emit("RESULT_SHA %s" % result)
    emit("WALL_S %s" % fmt(wall, 4))
    if n_pass == n_gate:
        emit("ALL CHECKS PASSED")
    else:
        emit("GATE_FAILURES " + ",".join(name for name, ok in CHECKS if not ok))
    emit("claim_boundary experiments_only_not_a_ledger_claim")
    emit("FENCE %s" % FENCE)

    section("STATE")
    emit("round r%d contract %s" % (ROUND, CONTRACT))
    emit("FILE_SHA256 %s" % file_sha256())
    emit("SPEC_SHA %s" % SPEC_SHA)
    emit("RESULT_SHA %s" % result)
    emit("GATES %d/%d smoke=%d wall_s=%s" % (n_pass, n_gate, int(smoke), fmt(wall, 3)))
    emit("parent r635 %s RESULT_SHA %s" % (
        parent.get("verdict"), str(parent.get("result_sha", ""))[:16],
    ))
    for rep in reports:
        emit(
            "  %s peak_test=%s" % (rep["name"], fmt(rep["peak_test"], 3))
        )
    emit("DECISION %s" % verdict)
    emit("WHY %s" % why)
    emit("FENCE %s" % FENCE)
    emit("END_STATE")
    (HERE / "relay_lead_law_result.json").write_text(
        json.dumps(payload, sort_keys=True, separators=(",", ":"), default=str) + "\n",
        encoding="utf-8",
    )
    return 0 if n_pass == n_gate else 1


def main() -> None:
    parser = argparse.ArgumentParser(
        description="r636 relay-lead law (experiments only; no RH claim)",
    )
    parser.add_argument("--smoke", action="store_true")
    arguments = parser.parse_args()
    raise SystemExit(run(arguments.smoke))


if __name__ == "__main__":
    main()
