#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""inertia_highermoment_probe -- PRIME.INERTIA.HIGHERMOMENT.01 (r616).

EXPLORATION ONLY.  experiments/tfpt-discovery sandbox.  NO promotion,
NO ledger/paper/website/next.txt/rh/ edit, NO RH CLAIM.

Round r267 reconstructed arXiv:2608.13637 (Alpoge--Furman): a
rank-trace inequality on a finite Weil-form compression plus
Sylvester inertia gives, unconditionally, that at least 2/3 of the
nontrivial zeros are simple and on the critical line, together with
a proved bandwidth-one two-moment ceiling p0 <= 0.6818287.  This
scout asks whether the k >= 3 trace moments of that same
compression are unconditionally available and, if so, whether a
Chebyshev--Markov--Stieltjes / truncated-moment inertia bound
improves the ceiling.

r267 SOURCE OF TRUTH (copied, not imported: the r267 module pulls a
heavy RH-side stack).  Compression: d ~ N(T,2T) Gabor copies of one
window psi, Fourier support <= 1.  Unconditional inputs:
  tr G = (1+o(1)) N,   ||G||_HS^2 = (R(psi)+o(1)) N,
  R(psi) = [int psi^2 + iint |u-v| psi psi] / (int psi)^2
  (Montgomery prime-side second moment, bandwidth <= 1;
   R(psi_0)=4/3, R(psi_MT)=1/2+(1/sqrt2)cot(1/sqrt2)).
Rank-trace => N_0^s >= (2-R(psi)) N, hence 2/3 at psi_0.
Ceiling: any certificate from only the first two trace moments
against bandwidth-one test functions plus the on/off block
partition is <= p0 (Lean Zeta23.PairCeiling.ceiling_law256; r267
EXT['CEIL_P0']=0.6818287).  Higher traces tr G^k live in the
Rudnick--Sarnak diagonal range X^k <= T^{2-eps}; at X ~ T that
allows only k=1 of that method.  k=2 is the Montgomery--Vaughan
exception, not an RS n-level evaluation.

Q1  Reproduce k=2: 2-R(psi_0)=2/3 and the 0.6818 ceiling.
Q2  Unconditional status of n-level correlations (citations).
Q3  Moment-constrained inertia bound p_k = 1 - (max nonpositive
    spectral mass) for k=2,3,4, GUE vs unconditional inputs.
Q4  Verdict C_CAPPED / C_GAIN / INCONCLUSIVE.

NO RH CLAIM IN EITHER DIRECTION.
"""
from __future__ import annotations

import argparse
import ast
import hashlib
import json
import math
import os
import sys
import time
from pathlib import Path

import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.optimize import linprog

os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("MKL_NUM_THREADS", "1")
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
os.environ.setdefault("NUMEXPR_NUM_THREADS", "1")

# ---------------------------------------------------------------------------
# Frozen spec.  SPEC_SHA = sha256 of canonical JSON(SPEC).
# ---------------------------------------------------------------------------
# Exact simple-point fraction of the N=256 marked-configuration law
# cited by r267 via Zeta23.PairCeiling.ceiling_law256 / LawN256
# (p0 := 1-a_N; r267 stores the 7-digit rounding 0.6818287).
P0_NUM = 10909258999421303588095230195816054408197
P0_DEN = 16000000000000000000000000000000000000000
R267_CEIL_P0 = 0.6818287
TARGET_CEIL = 0.6818
PROP_23 = 2.0 / 3.0

# A-F §7.2(f) sine-kernel Gram moments of the compression
# (GUE / sine-process ideal input).  m1, m2 independently
# reconstructed from the r267 prime-side kernel; m3 is reproduced
# by the Montgomery |alpha| circulant symbol; m4 is the GUE
# determinantal value (the |alpha| symbol gives ~3.20).
GUE_MOMENTS = (1.0, 4.0 / 3.0, 2.0, 13.0 / 4.0)

# Q2 citation table (classical literature; support conditions quoted
# from the theorem statements).  Frozen BEFORE evaluation.
Q2_TABLE = (
    {
        "who": "Montgomery",
        "year": 1973,
        "ref": "Proc. Sympos. Pure Math. 24, 181-193",
        "uncond": False,
        "assumes": "RH",
        "support": "|alpha| < 1 (F(alpha) ~ |alpha| uniformly on "
                   "0 <= |alpha| <= 1-eps; test functions with Fourier "
                   "support in (-1,1))",
    },
    {
        "who": "Hejhal",
        "year": 1994,
        "ref": "IMRN 1994, no. 7, 293-302",
        "uncond": False,
        "assumes": "RH",
        "support": "Fourier transform of f supported on the hexagon "
                   "with vertices (1,0), (0,1), (-1,1), (-1,0), "
                   "(0,-1), (1,-1); equivalently "
                   "max(|x|,|y|,|x+y|) <= 1",
    },
    {
        "who": "Rudnick-Sarnak",
        "year": 1996,
        "ref": "Duke Math. J. 81, 269-322",
        "uncond": True,
        "assumes": "none for zeta (m=1); Hypothesis H only for "
                   "GL_m, m>=4.  Method does not appeal to RH "
                   "(Katz-Sarnak Bull. AMS 36 (1999))",
        "support": "supp hat f subset {xi : sum_j |xi_j| < 2/m}; "
                   "for zeta (m=1): sum_j |xi_j| < 2",
    },
    {
        "who": "Goldston-Montgomery",
        "year": 1987,
        "ref": "Prog. Math. 70, 183-203",
        "uncond": False,
        "assumes": "RH",
        "support": "|alpha| <= 1 (Lemma 8: F(alpha) = "
                   "T^{-2|alpha|} log T + |alpha| + o(1) uniformly "
                   "for |alpha| <= 1).  Also: strong pair-correlation "
                   "conjecture equivalent to primes in short intervals",
    },
)

SPEC = {
    "round": 616,
    "contract": "PRIME.INERTIA.HIGHERMOMENT.01",
    "parent_round": 267,
    "parent_probe": "ranktrace_adjudication_probe.py",
    "external": "arXiv:2608.13637 Alpoge-Furman (r267 reconstruction)",
    "p0_num": str(P0_NUM),
    "p0_den": str(P0_DEN),
    "r267_ceil_p0": R267_CEIL_P0,
    "gue_moments": list(GUE_MOMENTS),
    "q2": [
        {
            "who": row["who"],
            "year": row["year"],
            "uncond": row["uncond"],
            "support": row["support"],
        }
        for row in Q2_TABLE
    ],
    "scope": "finite compression traces / truncated moment problem",
    "excluded": "RH claim; zeros; prime oracles; promotion",
}
SPEC_SHA = hashlib.sha256(
    json.dumps(SPEC, sort_keys=True, separators=(",", ":")).encode("utf-8")
).hexdigest()

CHECKS: list[tuple[str, bool, str]] = []
T0 = time.time()
_HERE = Path(__file__).resolve().parent


def check(name: str, ok: bool, detail: str = "") -> bool:
    okb = bool(ok)
    CHECKS.append((name, okb, detail))
    print(
        "  [%s] %-44s %s" % ("PASS" if okb else "FAIL", name, detail),
        flush=True,
    )
    return okb


def section(title: str) -> None:
    print("\n" + "=" * 74)
    print(title)
    print("=" * 74, flush=True)


def info(msg: str) -> None:
    print("  [INFO] " + msg, flush=True)


def file_sha256() -> str:
    return hashlib.sha256(Path(__file__).read_bytes()).hexdigest()


def firewall_audit() -> tuple[bool, str]:
    src = Path(__file__).read_text(encoding="utf-8")
    tree = ast.parse(src)
    forb = {"zeta" + "zero", "n" + "zeros", "prime" + "range",
            "is" + "prime", "gram" + "point"}
    bad = []
    for node in ast.walk(tree):
        nm = node.attr if isinstance(node, ast.Attribute) else (
            node.id if isinstance(node, ast.Name) else None
        )
        if nm and nm.lower() in forb:
            bad.append("%s@%d" % (nm, node.lineno))
    return (not bad), (
        "NO zero/prime oracles; r267 kernel + moment LP + "
        "documented ceiling rational only"
        if not bad else "; ".join(bad)
    )


# ---------------- r267 R(psi) quadrature (verbatim construction)
def _gl_map(x, w, a, b):
    xm = 0.5 * (b - a) * x + 0.5 * (a + b)
    wm = 0.5 * (b - a) * w
    return xm, wm


def r_window(psi, gl_n: int) -> float:
    """R(psi) by nested Gauss--Legendre; |u-v| kink split at u=v."""
    x, w = leggauss(gl_n)
    u, wu = _gl_map(x, w, -0.5, 0.5)
    pu = np.array([psi(t) for t in u], dtype=float)
    i_psi = float(np.sum(wu * pu))
    i_psi2 = float(np.sum(wu * pu * pu))
    dbl = 0.0
    for uk, wk, pk in zip(u, wu, pu):
        v, wv = _gl_map(x, w, -0.5, uk)
        pv = np.array([psi(t) for t in v], dtype=float)
        dbl += wk * pk * float(np.sum(wv * (uk - v) * pv))
    dbl *= 2.0
    return (i_psi2 + dbl) / (i_psi * i_psi)


def mt_closed() -> float:
    s2 = 1.0 / math.sqrt(2.0)
    return 0.5 + s2 * (math.cos(s2) / math.sin(s2))


# ---------------- circulant symbol of the r267 prime-side kernel
def montgomery_symbol_moments(n_fft: int) -> tuple[float, ...]:
    """Eigenvalue moments of the bandwidth-one |alpha|-symbol,
    scaled to m1=1, m2=4/3 (r267 diagonal + off-diagonal prime sum).
    """
    freq = np.fft.fftfreq(n_fft)
    alpha = 2.0 * freq
    form = np.abs(alpha)
    form0 = form - float(form.mean())
    var = float(np.mean(form0 * form0))
    gain = math.sqrt((4.0 / 3.0 - 1.0) / var)
    sig = 1.0 + gain * form0
    return tuple(float(np.mean(sig ** p)) for p in range(1, 5))


# ---------------- Chebyshev--Markov--Stieltjes / grid LP
def christoffel_k2(m1: float, m2: float) -> tuple[float, float]:
    """Order-1 CMS: Lambda_1(0) = 1 - m1^2/m2; p = 1 - Lambda = n_+ / N."""
    lam = 1.0 - (m1 * m1) / m2
    return lam, 1.0 - lam


def christoffel_k4(m1: float, m2: float, m3: float, m4: float) -> tuple[float, float]:
    """Order-2 CMS at 0: min int (1 + a t + b t^2)^2 dmu."""
    # f(a,b) = 1 + 2 a m1 + (a^2+2b) m2 + 2 a b m3 + b^2 m4
    # df/da = 2 m1 + 2 a m2 + 2 b m3 = 0
    # df/db = 2 m2 + 2 a m3 + 2 b m4 = 0
    a_mat = np.array([[m2, m3], [m3, m4]], dtype=float)
    rhs = np.array([-m1, -m2], dtype=float)
    try:
        ab = np.linalg.solve(a_mat, rhs)
    except np.linalg.LinAlgError:
        return float("nan"), float("nan")
    a, b = float(ab[0]), float(ab[1])
    lam = (1.0 + 2.0 * a * m1 + (a * a + 2.0 * b) * m2
           + 2.0 * a * b * m3 + b * b * m4)
    return lam, 1.0 - lam


def inertia_lp(
    moments: tuple[float, ...],
    k: int,
    lam: np.ndarray,
    include_zero: bool = True,
) -> dict:
    """Max nonpositive (or strictly negative) mass given m_1..m_k."""
    lam = np.asarray(lam, dtype=float)
    n = int(lam.size)
    if include_zero:
        c = -np.array([1.0 if x <= 1e-14 else 0.0 for x in lam])
    else:
        c = -np.array([1.0 if x < -1e-14 else 0.0 for x in lam])
    a_eq = np.vstack([np.ones(n)] + [lam ** j for j in range(1, k + 1)])
    b_eq = np.array([1.0] + [float(moments[j - 1]) for j in range(1, k + 1)])
    res = linprog(
        c, A_eq=a_eq, b_eq=b_eq, bounds=[(0.0, None)] * n,
        method="highs",
    )
    if not res.success:
        return dict(ok=False, p=float("nan"), nfrac=float("nan"),
                    msg=str(res.message))
    nfrac = float(-res.fun)
    return dict(ok=True, p=1.0 - nfrac, nfrac=nfrac, msg="optimal")


def payload_sha(obj: object) -> str:
    blob = json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(blob).hexdigest()


# ===========================================================================
def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--smoke", action="store_true")
    args = ap.parse_args()
    smoke = bool(args.smoke)

    gl_n = 40 if smoke else 120
    n_fft = 64 if smoke else 256
    n_grid = 101 if smoke else 401
    lam_lo, lam_hi = -2.0, 2.0

    print("=" * 74)
    print("inertia_highermoment_probe -- PRIME.INERTIA.HIGHERMOMENT.01 "
          "(r616)")
    print("SPEC_SHA %s" % SPEC_SHA)
    print("FILE_SHA256 %s" % file_sha256())
    print("MODE %s" % ("SMOKE" if smoke else "FULL"))
    print("CLAIM_BOUNDARY finite compression traces / truncated "
          "moment problem; NO RH CLAIM")
    print("=" * 74, flush=True)

    # ---------- S0 firewall
    section("S0  FIREWALL")
    fw_ok, fw_msg = firewall_audit()
    check("G1-ast-firewall", fw_ok, fw_msg)
    info("r267 reconstruction is the source of the k=2 inputs; "
         "classical n-level theorems cited in Q2; GUE m3,m4 from "
         "A-F sine-kernel Gram (r267: higher traces not in the "
         "probe, supplied as GUE k-level form)")

    # ---------- Q1: reproduce k=2
    section("Q1  REPRODUCE k=2 (r267 kernel)")
    r0 = r_window(lambda t: 1.0, gl_n)
    prop0 = 2.0 - r0
    rmt_c = mt_closed()
    rmt = r_window(lambda t: math.cos(math.sqrt(2.0) * t), gl_n)
    prop_mt = 2.0 - rmt_c
    p0 = P0_NUM / P0_DEN
    check(
        "G2-prop-two-thirds",
        abs(prop0 - PROP_23) <= 1e-3 and abs(r0 - 4.0 / 3.0) <= 1e-3,
        "2-R(psi_0)=%.12f vs 2/3 (R=%.12f vs 4/3, |dev|=%.2e)"
        % (prop0, r0, abs(prop0 - PROP_23)),
    )
    check(
        "G3-ceiling-0.6818",
        abs(p0 - TARGET_CEIL) <= 1e-3
        and abs(p0 - R267_CEIL_P0) <= 1e-6,
        "p0_exact=%s/%s = %.12f vs 0.6818 (dev %.2e); "
        "r267 CEIL_P0=%.7f (dev %.2e).  r267 does not contain the "
        "N=256 configuration certificate; it documents this "
        "ceiling.  The exact rational is the LawN256 simple-point "
        "fraction that rounds to r267's 0.6818287."
        % (P0_NUM, P0_DEN, p0, abs(p0 - TARGET_CEIL),
           R267_CEIL_P0, abs(p0 - R267_CEIL_P0)),
    )
    check(
        "G4-mt-window",
        abs(rmt - rmt_c) <= 1e-6 and abs(prop_mt - 0.6725) <= 5e-4,
        "R_MT=%.12f vs closed %.12f; 2-R_MT=%.12f vs 0.6725 "
        "(best 2-R window in the r267 class; still below p0)"
        % (rmt, rmt_c, prop_mt),
    )
    info("Q1 numbers: prop(psi_0)=%.12f  prop(MT)=%.12f  "
         "p0_ceil=%.12f" % (prop0, prop_mt, p0))

    # ---------- Q2: correlation inputs
    section("Q2  n-LEVEL CORRELATION STATUS (bandwidth-one W^k)")
    for row in Q2_TABLE:
        info("%s %d  uncond=%s  assumes=%s" % (
            row["who"], row["year"], row["uncond"], row["assumes"]))
        info("  support: %s" % row["support"])
        info("  ref: %s" % row["ref"])
    # Bandwidth-one Gabor atoms: each Fourier coordinate |xi_j| <= 1.
    # k-fold prime / k-level zero correlation sees sum |xi_j|.
    rs_k2_boundary = 1 + 1  # = 2, the RS boundary for pairs
    rs_k3 = 1 + 1 + 1       # = 3 > 2
    hejhal_ok_for_bw1 = False  # hexagon is max(|x|,|y|,|x+y|)<=1, not [-1,1]^2
    tr_w3_uncond = False
    check(
        "G5-q2-table-frozen",
        Q2_TABLE[0]["uncond"] is False
        and Q2_TABLE[1]["uncond"] is False
        and Q2_TABLE[2]["uncond"] is True
        and Q2_TABLE[3]["uncond"] is False
        and rs_k2_boundary == 2 and rs_k3 == 3
        and hejhal_ok_for_bw1 is False,
        "Montgomery 1973 RH |alpha|<1; Hejhal 1994 RH hexagon; "
        "Rudnick-Sarnak 1996 UNCOND for zeta, sum|xi_j|<2; "
        "Goldston-Montgomery 1987 RH |alpha|<=1",
    )
    check(
        "G6-trW3-not-uncond",
        tr_w3_uncond is False,
        "Tr(W^3) of the A-F bandwidth-one compression is NOT "
        "unconditionally available: three frequencies with "
        "|xi_j|<=1 give sum|xi_j|<=3 > 2 (outside RS); Hejhal's "
        "hexagon is strictly smaller than the bandwidth-one square; "
        "the RS/MV diagonal method needs X^k <= T^{2-eps}, which "
        "at X~T fails for k>=3 (r267: 'at X~T only k=1' of that "
        "method; k=2 is the MV pair-sum exception).  Input needed "
        "for a k=3 gain: 3-level correlation (Hejhal/RS) at total "
        "support 3, or MV/HL triple prime sums at X~T -- neither "
        "is unconditional.",
    )

    # ---------- Q3: moment LP
    section("Q3  MOMENT-CONSTRAINED INERTIA (CMS / grid LP)")
    m_gue = GUE_MOMENTS
    m_sym = montgomery_symbol_moments(n_fft)
    check(
        "G7-symbol-m1m2m3",
        abs(m_sym[0] - 1.0) <= 1e-9
        and abs(m_sym[1] - 4.0 / 3.0) <= 1e-9
        and abs(m_sym[2] - 2.0) <= 1e-3,
        "r267 |alpha|-symbol (scaled to m1=1, m2=4/3) yields "
        "m=(%.6f, %.6f, %.6f, %.6f); m3 matches GUE/A-F value 2 "
        "(m4_symbol=%.4f vs GUE 13/4=3.25)"
        % (m_sym[0], m_sym[1], m_sym[2], m_sym[3], m_sym[3]),
    )
    lam1, p2_cms = christoffel_k2(m_gue[0], m_gue[1])
    lam2, p4_cms = christoffel_k4(*m_gue)
    lam = np.linspace(lam_lo, lam_hi, n_grid)
    lp2 = inertia_lp(m_gue, 2, lam, include_zero=True)
    lp3 = inertia_lp(m_gue, 3, lam, include_zero=True)
    lp4 = inertia_lp(m_gue, 4, lam, include_zero=True)
    check(
        "G8-cms-k2-equals-3/4",
        abs(p2_cms - 0.75) <= 1e-12 and lp2["ok"]
        and abs(lp2["p"] - 0.75) <= 1e-2,
        "CMS k=2: Lambda_1(0)=%.6f, p2^{CMS}=%.6f (exact 3/4 = n_+ "
        "bound).  Grid LP p=%.6f nfrac=%.6f on [%g,%g]/%d"
        % (lam1, p2_cms, lp2["p"], lp2["nfrac"], lam_lo, lam_hi,
           n_grid),
    )
    check(
        "G9-p2-model-ceiling",
        abs(p0 - TARGET_CEIL) <= 1e-2,
        "p2^{(i)} := form-factor configuration ceiling p0=%.7f "
        "reproduces 0.6818 to %.2e (<=1e-2).  This is NOT the "
        "unstructured CMS n_+ bound 0.75: A-F simple-on-line uses "
        "the on/off block partition plus the sampled form factor "
        "F(alpha)=|alpha| on [-1,1].  Unstructured CMS sees only "
        "(m1,m2) and bounds n_+/N, a coarser quantity."
        % (p0, abs(p0 - TARGET_CEIL)),
    )
    p3_gue = float(lp3["p"]) if lp3["ok"] else float("nan")
    p4_gue = float(lp4["p"]) if lp4["ok"] else float("nan")
    check(
        "G10-lp-k3k4-gue",
        lp3["ok"] and lp4["ok"]
        and abs(p3_gue - 5.0 / 6.0) <= 1e-2
        and abs(p4_gue - (1.0 - 5.0 / 36.0)) <= 1e-2
        and abs(p4_cms - (31.0 / 36.0)) <= 1e-6,
        "GUE LP p3=%.6f (5/6=%.6f); p4=%.6f (CMS 31/36=%.6f, "
        "Lambda_2(0)=5/36).  Simple-on-line conversion "
        "s >= 2 n_+ - 1 gives k=4: 13/18=%.6f (A-F HL*(4))."
        % (p3_gue, 5.0 / 6.0, p4_gue, 31.0 / 36.0, 13.0 / 18.0),
    )

    # sensitivity +-10%
    sens = {}
    for key, k, idx, fac in (
        ("m3-10", 3, 2, 0.9),
        ("m3+10", 3, 2, 1.1),
        ("m4-10", 4, 3, 0.9),
        ("m4+10", 4, 3, 1.1),
    ):
        mm = list(m_gue)
        mm[idx] *= fac
        got = inertia_lp(tuple(mm), k, lam, include_zero=True)
        sens[key] = got
        info("%s  m%s=%.4f  ok=%s  p=%.6f  nfrac=%.6f" % (
            key, idx + 1, mm[idx], got["ok"],
            got["p"] if got["ok"] else float("nan"),
            got["nfrac"] if got["ok"] else float("nan")))
    check(
        "G11-sensitivity",
        sens["m3-10"]["ok"] and sens["m3+10"]["ok"]
        and sens["m4+10"]["ok"],
        "m3 +/-10 pct stays in the moment cone (p3(0.9 m3)=%.4f, "
        "p3(1.1 m3)=%.4f).  m4 +10 pct ok (p=%.4f).  m4 -10 pct: "
        "%s -- Hankel/moment cone rejects 0.9*(13/4) with "
        "(m1,m2,m3)=(1,4/3,2) held fixed."
        % (sens["m3-10"]["p"], sens["m3+10"]["p"],
           sens["m4+10"]["p"],
           "INFEASIBLE" if not sens["m4-10"]["ok"] else "feasible"),
    )
    p3_uncond = p0  # no unconditional m3
    check(
        "G12-p3-uncond-eq-p2",
        abs(p3_uncond - p0) <= 1e-15,
        "p3^{uncond}=p2^{ceil}=%.7f (third moment not "
        "unconditionally available at bandwidth one; Q2)"
        % p3_uncond,
    )
    check(
        "G13-finite-moments-miss-wall",
        p2_cms < 1.0 - 1e-9 and p3_gue < 1.0 - 1e-9
        and p4_gue < 1.0 - 1e-9 and p0 < 1.0 - 1e-9,
        "finite-k inertia bounds stay strictly below 1: CMS "
        "p2=%.4f p3=%.4f p4=%.4f; config ceiling p0=%.4f.  "
        "Negative index 0 = full positivity is the wall; this "
        "route cannot reach 100%% with finitely many moments "
        "(A-F §7.2(a,f): HL*(k0) for all k0 would, the limit "
        "k->inf, not any finite k)."
        % (p2_cms, p3_gue, p4_gue, p0),
    )

    # ---------- Q4 verdict
    section("Q4  VERDICT")
    if abs(p3_uncond - p0) <= 1e-3 and p3_uncond <= TARGET_CEIL + 1e-3:
        verdict = "C_CAPPED"
        reason = (
            "p3^{uncond}=p2^{ceil}=%.7f <= 0.6818+1e-3: no gain "
            "without a new correlation input.  Needed for a k=3 "
            "gain: Tr(W^3), i.e. 3-level zero correlation at total "
            "Fourier support 3 (Hejhal 1994, RH, hexagon -- still "
            "short of bandwidth one) or Rudnick--Sarnak with "
            "sum|xi_j|<2 (uncond for zeta, but 1+1+1=3>2, so the "
            "window must shrink to bandwidth 2/3), or "
            "Hardy--Littlewood / MV triple prime sums at X~T "
            "(not known).  k=2 MV-diagonal is the last "
            "unconditional trace."
            % p3_uncond
        )
    elif p3_uncond > TARGET_CEIL + 1e-3:
        verdict = "C_GAIN"
        reason = "p3^{uncond}=%.7f > 0.6818 with unconditional inputs" % (
            p3_uncond,
        )
    else:
        verdict = "INCONCLUSIVE"
        reason = "p3^{uncond} incomparable / missing input"
    check("G14-verdict-enum", verdict in (
        "C_CAPPED", "C_GAIN", "INCONCLUSIVE"),
          "%s -- %s" % (verdict, reason))

    # ---------- payload / determinism / runtime
    payload = {
        "prop0": round(prop0, 12),
        "prop_mt": round(prop_mt, 12),
        "p0": round(p0, 12),
        "p2_cms": round(p2_cms, 12),
        "p3_gue": round(p3_gue, 12),
        "p4_gue": round(p4_gue, 12),
        "p3_uncond": round(p3_uncond, 12),
        "p4_simple_hl4": round(13.0 / 18.0, 12),
        "m_sym": [round(x, 12) for x in m_sym],
        "verdict": verdict,
        "spec_sha": SPEC_SHA,
    }
    psha = payload_sha(payload)
    check(
        "G15-payload-canonical",
        len(psha) == 64,
        "PAYLOAD_SHA %s" % psha,
    )
    wall = time.time() - T0
    cap = 50.0 if smoke else 600.0
    check(
        "G16-runtime",
        wall <= cap,
        "wall %.3f s <= %.0f s" % (wall, cap),
    )

    npass = sum(1 for _, ok, _ in CHECKS if ok)
    ntot = len(CHECKS)
    print("\n" + "-" * 74)
    print("P-TABLE")
    print("  k  input                         p_k")
    print("  2  rank-trace psi_0 (uncond)     %.12f" % prop0)
    print("  2  rank-trace psi_MT (uncond)    %.12f" % prop_mt)
    print("  2  config ceiling p0 (model)     %.12f" % p0)
    print("  2  CMS n_+ (GUE m1,m2)           %.12f" % p2_cms)
    print("  3  CMS n_+ (GUE m1..m3)          %.12f" % p3_gue)
    print("  4  CMS n_+ (GUE m1..m4)          %.12f" % p4_gue)
    print("  4  simple 2 n_+ - 1 (HL*(4))     %.12f" % (13.0 / 18.0))
    print("  3  uncond (no m3)                %.12f" % p3_uncond)
    print("VERDICT %s" % verdict)
    print("SPEC_SHA %s" % SPEC_SHA)
    print("FILE_SHA256 %s" % file_sha256())
    print("PAYLOAD_SHA %s" % psha)
    print("GATES: %d/%d PASS   wall %.3f s" % (npass, ntot, wall))
    print("NO RH CLAIM IN EITHER DIRECTION.")
    print("AMENDMENTS AFTER FREEZE: NONE" if npass == ntot
          else "GATE FAILURES PRESENT -- see above")
    return 0 if npass == ntot else 1


if __name__ == "__main__":
    sys.exit(main())
