#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""export_wall_certificates -- Lean exporter for the v897 certified
interval ladder (PRIME.PORT.BALLLADDER.01).

WHAT THIS DOES (read-only on the verification suite): for each of the
42 reachable rungs h = 142..878 of the deployed v563 window ladder it
re-runs the FROZEN v897 machinery (the byte-exact embedded
ball_arithmetic_ladder_probe source, SHA-warded) to rebuild

  * the exact dyadic interval-lag midpoints  mid_i = num_i / 2^k
    (mpmath mpf values are exact binary rationals -- the export is
    EXACT, no rounding),
  * the rigorous interval shift  shift_int = h + ceil(2 h rad_max Q)
    on the integer grid  Q = 10^20  (v897 E4, verbatim),
  * the exact integer grid matrix
        N[i][j] = floor(Q * (mid_|i-j| - mid_{2h-1-(i+j)}))
    (v897 grid_matrix_exact, cross-checked entry-by-entry against a
    pure-integer reconstruction of the same formula -- the SAME
    formula the Lean checker evaluates),

and then constructs a POSITIVITY WITNESS for the shifted certificate
matrix  M = N - shift_int * I:

  * an integer floor  c = floorC > 0  (grid units; sigma floor c/Q),
  * an integer matrix L ~ round(cholesky(M - 2c*I))  such that the
    residual  R = M - c*I - L*L^T  is (weakly) diagonally dominant
    with nonnegative diagonal -- verified EXACTLY in integers here,
    and re-verified by the Lean kernel (TfptCarrier/WallLadderChecker
    .lean, `rungOk`).  Diagonal dominance of the symmetric residual
    plus the Gram term gives  M >= c*I  -- i.e. the same
    sigma_h > 0 content as the v897 tier-1 certificate, as a
    kernel-checkable decomposition.

WHAT THIS DOES NOT DO: it proves nothing about the asymptotic tail
(h -> infinity), and it does NOT touch verification/v897_*.py (the
module is imported read-only; its embedded frozen source is SHA-warded
before use).  The interval-arithmetic error accounting that connects
M/Q to the TRUE wall matrix (v897 E1-E4) stays on the Python side and
enters the Lean composition as the NAMED EnclosureBridge hypothesis.
NO RH claim.

Emits: TfptCarrier/WallLadder/RungKz<kz>.lean  (data + kernel theorem).

Run (from experiments/lean4-carrier-rigidity/):
    ../tfpt-discovery/.venv/bin/python scripts/export_wall_certificates.py \
        --kz 18 23 12          # specific rungs, or --all
"""

import argparse
import hashlib
import os
import sys
import time
import types

import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
_LEANROOT = os.path.abspath(os.path.join(_HERE, os.pardir))
_REPO = os.path.abspath(os.path.join(_LEANROOT, os.pardir, os.pardir))
_VERIFY = os.path.join(_REPO, "verification")
_DISC = os.path.join(_REPO, "experiments", "tfpt-discovery")
sys.path.insert(0, _VERIFY)
sys.path.insert(0, _DISC)

import v897_certified_interval_ladder as v897  # noqa: E402  (READ-ONLY)

Q = 10 ** 20
OUT_DIR = os.path.join(_LEANROOT, "TfptCarrier", "WallLadder")
FLOOR_FRAC = 0.25          # exported integer floor c = this * lam_f * Q


def load_probe():
    """Exec the frozen embedded probe source (v897 S0 convention:
    byte-exact, SHA-warded, entry point not run)."""
    src = v897._SRC_0
    if src[:1] == "\n":
        src = src[1:]
    sha = hashlib.sha256(src.encode("utf-8")).hexdigest()
    assert sha == v897.LADDER_FILE_SHA, "frozen probe SHA mismatch"
    path = os.path.join(_DISC, "ball_arithmetic_ladder_probe.py")
    mod = types.ModuleType("ball_arithmetic_ladder_probe")
    mod.__file__ = path if os.path.isfile(path) else v897.__file__
    sys.modules["ball_arithmetic_ladder_probe"] = mod
    exec(compile(src, mod.__file__, "exec"), mod.__dict__)
    return mod


def dyadic(x, mp):
    """Exact (num, exp) with x = num * 2^exp (mpmath mpf)."""
    sign, man, exp, _bc = x._mpf_
    if man == 0:
        return (0, 0)
    return (-man if sign else man, exp)


def export_rung(mod, r, check_exact=True):
    mp = mod.mp
    h, M = r["h"], r["M"]
    spec = dict(kind="prime", M=M, n_zone=r["n_zone"], ka=r["ka"])
    t0 = time.time()
    mids, rads, range_ok = mod.lags_iv(spec)
    assert range_ok, "tent-range rigour failed"
    rad_max = rads[0]
    for r_ in rads[1:]:
        if r_ > rad_max:
            rad_max = r_
    # cross-implementation ward (probe L1.1, rel <= 1e-9)
    with mp.workdps(80):
        ward = float(max(abs(a - mp.mpf(b))
                         for a, b in zip(mids, r["c_f"]))
                     / max(abs(mp.mpf(b)) for b in r["c_f"]))
    assert ward <= 1.0e-9, "cross-implementation ward failed"
    with mp.workdps(40):
        QM = mp.mpf(Q)
    shift_int = mod.rigorous_shift_int(h, rad_max, QM)
    N = mod.grid_matrix_exact(mids, M, QM)
    t_grid = time.time() - t0

    # ---- exact dyadic export at a common exponent
    dys = [dyadic(x, mp) for x in mids]
    E = min((e for n_, e in dys if n_ != 0), default=0)
    assert E < 0, "unexpected nonnegative exponent"
    nums = [n_ << (e - E) if n_ != 0 else 0 for n_, e in dys]
    den = 1 << (-E)

    # ---- pure-integer reconstruction ward: the Lean formula
    #      floor(Q*(mids[d]-mids[e])/den) must reproduce N exactly
    if check_exact:
        for i in range(h):
            for j in range(i, h):
                d_, e_ = abs(i - j), (2 * h - 1) - (i + j)
                v = (Q * (nums[d_] - nums[e_])) // den
                assert v == N[i][j], "grid reconstruction mismatch"

    # ---- the witness: c > 0 and L with R = M - cI - LL^T diag-dominant
    c = max(1, int(FLOOR_FRAC * max(r["lam_f"], 0.0) * Q))
    Mz = [[N[i][j] - (shift_int if i == j else 0) for j in range(h)]
          for i in range(h)]
    A64 = np.array([[float(Mz[i][j]) - (2.0 * c if i == j else 0.0)
                     for j in range(h)] for i in range(h)])
    Lf = np.linalg.cholesky(A64)
    Lint = np.rint(Lf).astype(np.int64)
    assert int(np.abs(Lint).max()) < (1 << 40), "witness entry too large"

    # exact Gram via 15-bit split (all int64 partial products safe)
    hi = Lint >> 15
    lo = Lint - (hi << 15)
    assert int(np.abs(hi).max()) ** 2 * h < (1 << 62)
    G = ((hi @ hi.T).astype(object) << 30) \
        + ((hi @ lo.T + lo @ hi.T).astype(object) << 15) \
        + (lo @ lo.T).astype(object)
    Mo = np.array(Mz, dtype=object)
    R = Mo - np.diag([c] * h).astype(object) - G
    absR = abs(R)
    offsum = absR.sum(axis=1) - absR.diagonal()
    margin = R.diagonal() - offsum
    min_margin = int(min(margin))
    assert min_margin >= 0, "residual not diagonally dominant"
    assert all(int(x) >= 0 for x in R.diagonal()), "negative residual diag"

    rows = [[int(Lint[i][t]) for t in range(i + 1)] for i in range(h)]
    return dict(kz=r["kz"], h=h, den=den, shift=shift_int, floorC=c,
                mids=nums, rows=rows, rad_max=mp.nstr(rad_max, 3),
                ward=ward, min_margin=min_margin, t_grid=t_grid,
                floor_sigma=c / Q, lam_f=r["lam_f"])


def pack_signed(xs, bits):
    """Pack signed ints as offset-binary limbs, the exact inverse of
    Lean's tail-recursive `decodeSigned bits count blob` (which
    prepends, so the LAST vector entry sits in the lowest limb)."""
    off = 1 << (bits - 1)
    blob = 0
    for k, x in enumerate(reversed(xs)):
        v = x + off
        assert 0 <= v < (1 << bits), "limb out of range"
        blob |= v << (k * bits)
    # simulate the Lean decoder exactly (round-trip ward)
    acc, b = [], blob
    for _ in range(len(xs)):
        acc.insert(0, (b % (1 << bits)) - off)
        b //= 1 << bits
    assert acc == list(xs), "decodeSigned round-trip failed"
    return blob


def wrap_hex(blob, indent="    ", width=100):
    s = "0x%x" % blob
    return s  # single token; Lean parses hex numerals linearly


def emit_lean(d):
    name = "RungKz%d" % d["kz"]
    flat = [x for row in d["rows"] for x in row]
    wbits = max(x.bit_length() for x in flat) + 2
    # one packed blob per witness row (bounds the decode recursion
    # depth by h; simulate Lean's decodeRows for the round-trip ward)
    row_blobs = [pack_signed(row, wbits) for row in d["rows"]]
    sim, ln = [], 1
    for b in row_blobs:
        acc, bb = [], b
        for _ in range(ln):
            acc.insert(0, (bb % (1 << wbits)) - (1 << (wbits - 1)))
            bb //= 1 << wbits
        sim.append(acc)
        ln += 1
    assert sim == d["rows"], "decodeRows round-trip failed"
    mbits = max(x.bit_length() for x in d["mids"]) + 2
    mblob = pack_signed(d["mids"], mbits)
    rows_txt = ",\n".join("    0x%x" % b for b in row_blobs)
    body = """/-
  %s -- GENERATED wall-ladder certificate data (kz = %d, h = %d).
  =================================================================
  Exported by scripts/export_wall_certificates.py from the FROZEN
  v897 machinery (verification/v897_certified_interval_ladder.py,
  embedded probe SHA 48fda8c39afa074f...).  DO NOT HAND-EDIT.

  Content: exact dyadic interval-lag midpoints (mids[i]/den), the
  rigorous interval shift shift_int = h + ceil(2 h rad_max Q) on the
  grid Q = 10^20 (v897 E4), and an integer Cholesky witness for
    N - shift*I  >=  floorC * I   (grid units; sigma floor %.3e).
  rad_max %s | cross-implementation ward rel %.1e | exact residual
  dominance margin %d (integer grid units).

  The theorem below is checked by the Lean KERNEL (decide): the
  residual  M - floorC*I - L*L^T  is diagonally dominant with
  nonnegative diagonal, hence M is positive definite
  (TfptCarrier/WallLadderChecker.lean).  NO RH claim; the h -> infty
  tail is untouched.
-/
import TfptCarrier.WallLadderChecker

namespace TfptCarrier
namespace WallLadder

/-- Packed lag-midpoint numerators (%d signed limbs, %d bits each). -/
def rungKz%dMids : ℕ := %s

/-- Packed Cholesky witness, one blob per triangular row
(%d signed limbs total, %d bits each). -/
def rungKz%dWitness : List ℕ := [
%s]

/-- Exported certificate data for rung kz = %d (h = %d). -/
def rungKz%d : RungData where
  kz := %d
  h := %d
  den := %d
  shift := %d
  floorC := %d
  mids := decodeSigned %d %d rungKz%dMids
  rows := decodeRows %d 1 rungKz%dWitness

set_option maxHeartbeats 0 in
set_option maxRecDepth 100000 in
/-- KERNEL-CHECKED: the exported integer wall-certificate matrix at
kz = %d (h = %d) is positive definite with integer floor `floorC`
(sigma floor %.3e on the Q = 10^20 grid).  The `decide` runs in the
Lean kernel on the exported integers (no `native_decide`). -/
theorem rungKz%d_posDef : (MmatR rungKz%d).PosDef :=
  posDef_of_rungOk rungKz%d (by decide +kernel)

end WallLadder
end TfptCarrier
""" % (name, d["kz"], d["h"], d["floor_sigma"], d["rad_max"], d["ward"],
       d["min_margin"],
       len(d["mids"]), mbits, d["kz"], wrap_hex(mblob),
       len(flat), wbits, d["kz"], rows_txt,
       d["kz"], d["h"], d["kz"], d["kz"], d["h"],
       d["den"], d["shift"], d["floorC"],
       mbits, len(d["mids"]), d["kz"],
       wbits, d["kz"],
       d["kz"], d["h"], d["floor_sigma"], d["kz"], d["kz"],
       d["kz"])
    os.makedirs(OUT_DIR, exist_ok=True)
    path = os.path.join(OUT_DIR, name + ".lean")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(body)
    return path


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--kz", type=int, nargs="*", default=None)
    ap.add_argument("--all", action="store_true")
    args = ap.parse_args()

    t0 = time.time()
    mod = load_probe()
    mp = mod.mp
    print("[%.1fs] frozen probe loaded (SHA ok)" % (time.time() - t0),
          flush=True)
    glx, glw, lemma = mod.gl_nodes_enclosed(mod.GL_N)
    assert lemma["sign_ok"] and lemma["disjoint"] and lemma["contains2"]
    mod._GLX, mod._GLW = glx, glw
    print("[%.1fs] node-enclosure lemma ok" % (time.time() - t0),
          flush=True)

    rungs = []
    for kz in mod.core.frame_a_zones():
        r = mod.rung_survey(kz)
        if r["h"] <= mod.H_LADDER_MAX:
            rungs.append(r)
    rungs.sort(key=lambda r: (r["h"], r["kz"]))
    assert len(rungs) == 42
    targets = rungs if args.all else \
        [r for r in rungs if r["kz"] in set(args.kz or [])]
    assert targets, "no rungs selected (--kz ... or --all)"

    for r in targets:
        t1 = time.time()
        d = export_rung(mod, r)
        path = emit_lean(d)
        print("[%.1fs] kz %-3d h %-4d shift %-8d floorC %.3e "
              "margin %.2e ward %.1e -> %s (%.1fs)"
              % (time.time() - t0, d["kz"], d["h"], d["shift"],
                 d["floor_sigma"], float(d["min_margin"]), d["ward"],
                 os.path.relpath(path, _LEANROOT), time.time() - t1),
              flush=True)
    print("[%.1fs] done (%d rungs)" % (time.time() - t0, len(targets)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
