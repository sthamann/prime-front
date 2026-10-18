#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""arith_healthcode12_probe -- PRIME.ARITH.HEALTHCODE12.01
(EXPLORATION ONLY, experiments/; round 58, the cheap diagnostic:
the 12-bit pivot sign word of the wall window, verified against
the deployed modules, plus a seeded adversarial syndrome table.
A DIAGNOSTIC tool -- zero RH content, typed as such.  2026-08-10.)

THE OBJECT (frozen).  The 12-window compression A_12 = I - C_J(h)
of the wall (JWIN = {2, 4, ..., 24}; v899 machinery) carries 12
sequential LDL pivots d_{k,h} = det A^(k) / det A^(k-1); with
mu_{k,h} := 1/d_{k,h} - 1 the pivot factors are Q_{k,h} = 1 +
mu_{k,h} = 1/d_{k,h}, and for k = 12 the v899 exact identity
1/d_12 = 1 + m_def makes mu_12 the deflated-Christoffel mass
(warded below).  THE HEALTH CODE: the 12-bit sign word w_h =
(sign d_{1,h}, ..., sign d_{12,h}); by Sylvester the all-(+) word
is EQUIVALENT to PD of A_12 -- a repackaging of known content, no
new positivity.

PLAN-CLAIM AUDIT (frozen; the incoming plan summary attributed
four facts to "v897's actual machinery" -- each is verified
against the module where it ACTUALLY lives, and the attribution
errors are reported as first-class discrepancies):
  CLAIM-1 "v897's ladder transitions carry 12 pivot factors":
     ATTRIBUTION ERROR expected -- v897's certificates are
     h-dimensional integer-Bareiss/Cholesky pivot chains with NO
     12-structure; the 12 pivots live in the v899 12-window
     compression (per RUNG, not per transition -- second
     nuance).  Verified by reading both modules.
  CLAIM-2 "all-(+) word on every true transition": verified on
     every full-window truth RUNG (37 of the 42-census).
  CLAIM-3 "Epstein rejected at pivot 10": a v897 fact about the
     h-dimensional certificate (NOT a 12-word flag).  Verified
     by RE-RUNNING v897's actual embedded machinery READ-ONLY
     (exec of the byte-exact _SRC_0 after its file-SHA ward, no
     edit): run_control_ball() must return status 'refused' with
     first bad pivot index 10; a float LDL shadow of the same
     Epstein K prints its first bad index next to it.
  CLAIM-4 "smooth control fails first at flags 1 and 3" and "the
     soft wall pivot is k = 12": both MEASURED -- the smooth
     first-flip census over the 12-word, and the argmin_k d_k
     census on truth rungs; agreement or refutation reported.

FROZEN PROTOCOL (machinery verbatim from
case_edge_christoffel_probe round 57 = christoffel_ratio_probe
round 55; anatomy EXTENDED by one hook: an additive lag
injection lag_add (the deployed off-line-zero signature of
errorterm_demand_curve_probe: Delta c(t) = A cos(gamma0 t)
(cosh(delta t) - 1), t = j D) -- bit-identical physics when
lag_add = 0):

 W   PIPELINE + REPRODUCTION WARDS (kill -> PIPELINE-BROKEN /
     WARD-BROKEN): W0 truth ladder == 42 rungs; W0c full-window
     census == 37; W-C1f c-quartile reproduction 1163/2117/2930
     + c(kz21) = 50667 at h = 371 (rtol 2e-2).

 D   THE WORD IS WELL-DEFINED (kill -> WARD-BROKEN):
       D1 d_12 from the sequential LDL == d_12 from the
          independent slogdet minor-quotient route, rel <=
          D12_WARD = 1e-8, on every full truth rung;
       D2 SYLVESTER CONSISTENCY: all-(+) word <=> A_12 PD
          (eigvalsh), exact boolean agreement on every evaluated
          word (truth + smooth + battery);
       D3 mu_12 == m_def (the v899 deflation identity),
          conditioning-aware bar max(CHR_WARD_FLOOR = 1e-8,
          CHR_COND_FAC = 1e3 x EPS / tau_full) per rung.

 A1  THE TRUE WORD (typed): all-(+) on 37/37 (CLAIM-2; kill if
     not -- identity-grade, A_12 PD is the known census);
     SOFTEST-PIVOT census: argmin_k d_{k,h} per rung, count of
     rungs with argmin == 12 (CLAIM-4b), plus the mu_k ladder
     summary (min/med/max per k).

 A2  THE v897 RE-RUN (CLAIM-3; kill -> WARD-BROKEN): S1 the
     embedded source SHA-256 reproduces LADDER_FILE_SHA (v897
     module constant, READ-ONLY import); S2 the node-enclosure
     lemma holds; S3 run_control_ball() returns status 'refused'
     AND npiv == 10; S4 the float LDL shadow of the Epstein K at
     kz 9 prints its first nonpositive pivot index (0-based)
     next to the interval result (agreement reported, not
     barred: the interval certificate is the authority).

 A3  THE SMOOTH FIRST-FLIP CENSUS (CLAIM-4a; measured, typed):
     per smooth full-window rung the word, the set of negative
     flags, and the FIRST (lowest-index) negative flag; the
     census of first-flip indices vs the claim {1, 3}; typed
     SMOOTHCLAIM-CONFIRMED iff the set of observed first-flip
     indices == {1, 3}, else SMOOTHCLAIM-REFUTED(census).

 B   THE SEEDED ADVERSARIAL BATTERY (the syndrome table;
     measured): on the N_BAT = 3 shallowest full-window truth
     rungs:
       B1 INJ-COSH lag injection (errorterm verbatim; delta =
          0.05, gamma0 = 10.0, both signs): amplitude ladder
          A in (1e-4, 1e-3, 1e-2, 1e-1, 0.5, 1.0, 2.0)
          ascending; per rung the smallest flipping amplitude
          A*, its sign, and the flag set at first flip;
       B2 SCRAMBLE (seeds 1, 2, 3; binary strength): word or
          frame death per seed;
       B3 SMOOTH (binary): word per battery rung;
       B4 MASS-RESCALE mm -> f mm, f in (0.5, 0.9, 0.99, 1.01,
          1.1, 2.0): word per factor, first flipping |log f|.
     Frame death / window loss are recorded as their own
     syndrome states (CHAIN-DEATH / WINDOW-LOST).

 C   CONTROLS (kill -> WARD-BROKEN if silent): C0 truth wall
     neg(A) = 0 on every rung; C-S the smooth world flips >= 1
     flag on >= 1 full-window rung (the diagnostic must detect
     the wall-violating world); C-E Epstein + scramble (seed 1)
     at kz 9 fire (chain death or neg(A) > 0 or a flipped flag).

KILLS: KP pipeline (W) -> PIPELINE-BROKEN; KW D1-D3, A1
all-(+), A2, C0/C-S/C-E -> WARD-BROKEN.  A3/B typed outcomes
are measurements, never kills.

VERDICT (frozen enum): HEALTHCODE12-MEASURED / DIAGNOSTIC-ONLY
with typed sublabels TRUEWORD-ALLPLUS, SOFTPIVOT-12(count),
V897-PIVOT10-REPRODUCED, SMOOTHCLAIM-CONFIRMED /
SMOOTHCLAIM-REFUTED(census), and the printed DISCREPANCY list;
else PIPELINE-BROKEN / WARD-BROKEN.

FROZEN BARS: H_DEEP_MAX = 900; JWIN = (2,...,24); NW = 12;
N_RUNGS_EXP = 42; N_FULLWIN_FROZEN = 37; KZ_STAR = 21; H_STAR =
371; REF_C21 = 50667, REF_Q25/MED/Q75 = 1163/2117/2930 (rtol
2e-2); D12_WARD = 1e-8; CHR_WARD_FLOOR = 1e-8; CHR_COND_FAC =
1e3; EPS = 2.220446049250313e-16; N_BAT = 3; INJ_DELTA = 0.05;
INJ_GAMMA0 = 10.0; INJ_LADDER = (1e-4, 1e-3, 1e-2, 1e-1, 0.5,
1.0, 2.0); SCR_SEEDS = (1, 2, 3); RSC_FACTORS = (0.5, 0.9,
0.99, 1.01, 1.1, 2.0); V897_NPIV_REF = 10; CTRL_KZ = 9.

SMOKE-RUN DISCLOSURE (2026-08-10, before freezing): one smoke run
of this script (18/18 with the identical bars; no bar or enum
was tuned to it; ONE wording fix in the A1.2 typed detail --
'PARTIAL' -> 'REFUTED' for a 0/37 census -- no rule moved)
measured the picture frozen here as context: CLAIM-1 is an
ATTRIBUTION ERROR as expected (v897 exposes h-dimensional pivot
chains only; the 12-word lives in the v899 window compression,
per rung); the true word is all-(+) on 37/37, but CLAIM-4b is
REFUTED in the raw-argmin reading: the softest RAW pivot is k =
2 on ALL 37 rungs (census [2]; mu_2 median 3.8e5 dominates) --
the special role of k = 12 is the deflation-identity seat
(mu_12 == m_def, warded in D3), not raw softness; v897's control
re-run reproduces REFUSED at pivot index 10 byte-exactly in
1.1 s (CLAIM-3 confirmed where it actually lives) and the float
LDL shadow agrees (first bad index 10); the smooth first-flip
census REFUTES CLAIM-4a: first-flipped flags are {2: 25, 1: 9}
over 34 flagged smooth full-window rungs -- flag 3 is never
first; the syndrome table SEPARATES the manipulations: the
coherent cosh injection flips the HIGH flags first (flags [11] /
[12] at A* = 0.01 on the two shallowest rungs; window loss at
0.1 on the third), scramble kills the 12-window frame outright
(WINDOW-LOST, all seeds), mass rescale is asymmetric (f < 1
flips the LOW block {2, 3, 4, ...}, f > 1 flips {1} + the HIGH
block; f = 1.01 clean everywhere).  No census count, no enum,
no typed rule was changed after the smoke run.

SPEC v1 (2026-08-10, frozen + SHA-hashed before the frozen run):
everything above.  Mechanical concretizations frozen with v1:
(i) window memoization per (kz, seed); (ii) ONE Gram per rung;
(iii) the LDL is the standard no-pivoting elimination, pivots in
window order 1..12; a zero pivot terminates the elimination and
the remaining bits are typed dead; (iv) N_BAT = the 3 shallowest
full-window truth rungs in (h, kz) order; (v) the injection time
grid is t = j D, j = 0..M-1 (errorterm verbatim); (vi) the v897
re-run consumes the module's OWN embedded byte-exact source
(_SRC_0) after the SHA ward -- v897 itself is never edited.

NO RH claim -- and beyond that, typed DIAGNOSTIC-ONLY: the
12-bit word is a CLASSIFIER for manipulated combs /
L-function-like inputs on the deployed finite windows; its
all-(+) state on truth rungs is the known certified census
repackaged (Sylvester), and nothing here bears on tau_h > 0
beyond v897.  No marker moves.

FIREWALL: no zeros, no prime oracles (AST scan; banned ids
zetazero / nzeros / primerange / isprime / primepi / nextprime /
prevprime; the only factorisation in the v897 re-run is its own
trial-division spf on the READ-ONLY v563 atom list); v563 and
v897 READ-ONLY; RNG only inside the declared scramble
manipulations; stdout only.

Sources (read-only): v563_paper2_readouts; window/deflation
machinery verbatim from case_edge_christoffel_probe.py (round
57) = christoffel_ratio_probe.py (round 55, promoted v899); the
off-line-zero cosh signature verbatim from
errorterm_demand_curve_probe.py (PRIME.ERRORTERM.SCALE row);
v897_certified_interval_ladder.py (embedded probe source,
SHA-warded, exec'd verbatim without entry point); certified base
v884/v887/v897 -- declared inputs.

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/arith_healthcode12_probe.py
"""

import ast
import hashlib
import math
import os
import sys
import time
import types

import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
_VERIFY = os.path.abspath(os.path.join(_HERE, "..", "..",
                                       "verification"))
sys.path.insert(0, _HERE)
sys.path.insert(0, _VERIFY)

import v563_paper2_readouts as core        # noqa: E402  (READ-ONLY)

H_DEEP_MAX = 900
JWIN = tuple(range(2, 25, 2))
NW = 12
N_RUNGS_EXP = 42
N_FULLWIN_FROZEN = 37
KZ_STAR = 21
H_STAR = 371
REF_C21 = 50667.0
REF_Q25, REF_MED, REF_Q75 = 1163.0, 2117.0, 2930.0
REF_RTOL = 2e-2
D12_WARD = 1e-8
CHR_WARD_FLOOR = 1e-8
CHR_COND_FAC = 1e3
EPS = 2.220446049250313e-16
N_BAT = 3
INJ_DELTA = 0.05
INJ_GAMMA0 = 10.0
INJ_LADDER = (1e-4, 1e-3, 1e-2, 1e-1, 0.5, 1.0, 2.0)
SCR_SEEDS = (1, 2, 3)
RSC_FACTORS = (0.5, 0.9, 0.99, 1.01, 1.1, 2.0)
V897_NPIV_REF = 10
CTRL_KZ = 9
BANNED_IDS = ("zetazero", "nzeros", "primerange", "isprime",
              "primepi", "nextprime", "prevprime")

CHECKS = []
KILLS = []
T0 = time.time()


def check(name, ok, detail="", kill=None):
    CHECKS.append((name, bool(ok)))
    if kill and not ok:
        KILLS.append(kill)
    print("  [%s] %s%s" % ("PASS" if ok else "FAIL", name,
                           ("  -- " + detail) if detail else ""),
          flush=True)
    return bool(ok)


def section(title):
    print("\n" + "=" * 74)
    print(title)
    print("=" * 74, flush=True)


def ast_scan(banned):
    src = open(os.path.abspath(__file__), encoding="utf-8").read()
    bad = []
    for node in ast.walk(ast.parse(src)):
        name = None
        if isinstance(node, ast.Name):
            name = node.id
        elif isinstance(node, ast.Attribute):
            name = node.attr
        if name and name.lower() in banned:
            bad.append(name)
    return bad


# --------- pipeline, verbatim (christoffel_ratio / case_edge chain)
def grid_density(c):
    c = np.asarray(c, float)
    a = np.concatenate([c, c[-2:0:-1]])
    d = np.fft.fft(a)
    assert float(np.max(np.abs(d.imag))) <= 1e-9 * max(
        1.0, float(np.max(np.abs(d.real))))
    return d.real


def cell_widths(uu):
    du = np.zeros(len(uu))
    du[1:-1] = 0.5 * (uu[2:] - uu[:-2])
    du[0] = uu[1] - uu[0]
    du[-1] = uu[-1] - uu[-2]
    return du


def smooth_masses(uu):
    return 2.0 * np.exp(np.asarray(uu, float) / 2.0) \
        * cell_widths(np.asarray(uu, float))


def folded_measure(d_arm, L, sign=+1.0):
    jj = np.arange(L)
    keep = (sign * d_arm) > 0.0
    jj = jj[keep]
    th = 2.0 * math.pi * jj / L
    wt = (np.abs(d_arm[keep]) / (2.0 * L)) * 4.0 * np.sin(
        th / 2.0) ** 2
    fold = np.minimum(jj, L - jj)
    uf, inv = np.unique(fold, return_inverse=True)
    wagg = np.zeros(len(uf))
    np.add.at(wagg, inv, wt)
    xs = np.cos(2.0 * math.pi * uf / L)
    m = wagg > 1e-300
    return xs[m], wagg[m], uf[m]


def lanczos_chain(x, w, n):
    m0 = float(np.sum(w))
    m = len(x)
    Q = np.zeros((m, n))
    Q[:, 0] = np.sqrt(w) / math.sqrt(m0)
    al = np.zeros(n)
    be = np.zeros(max(n - 1, 0))
    steps = n
    for k in range(n):
        z = x * Q[:, k]
        al[k] = float(Q[:, k] @ z)
        z = z - al[k] * Q[:, k]
        if k > 0:
            z = z - be[k - 1] * Q[:, k - 1]
        for _ in range(2):
            z = z - Q[:, :k + 1] @ (Q[:, :k + 1].T @ z)
        if k == n - 1:
            break
        bnorm = float(np.linalg.norm(z))
        if bnorm <= 1e-14:
            steps = k + 1
            break
        be[k] = bnorm
        Q[:, k + 1] = z / bnorm
    return al[:steps], be[:max(steps - 1, 0)], m0, steps


def eval_chain(al, be, m0, y, n):
    P = np.zeros((len(y), n))
    P[:, 0] = 1.0 / math.sqrt(m0)
    if n > 1:
        P[:, 1] = (y - al[0]) * P[:, 0] / be[0]
    for k in range(1, n - 1):
        P[:, k + 1] = ((y - al[k]) * P[:, k]
                       - be[k - 1] * P[:, k - 1]) / be[k]
    return P


def lambda_eps(N):
    """Epstein x^2+5y^2 comb (port_schur_reduction verbatim)."""
    r = np.zeros(N + 1)
    s = int(math.isqrt(N)) + 1
    for x in range(-s, s + 1):
        for y in range(-s, s + 1):
            v = x * x + 5 * y * y
            if 1 <= v <= N:
                r[v] += 1.0
    a = r / 2.0
    lam = np.zeros(N + 1)
    for n in range(2, N + 1):
        acc = a[n] * math.log(n)
        for dd in range(2, n):
            if n % dd == 0:
                acc -= lam[dd] * a[n // dd]
        lam[n] = acc
    return lam


_WIN_CACHE = {}


def window_of(kz, scramble_seed=None):
    key = (kz, scramble_seed)
    if key not in _WIN_CACHE:
        rr = core.build_window(kz, scramble_seed=scramble_seed)
        _WIN_CACHE[key] = dict(
            h=rr["h"], M=rr["M"], D=rr["D"], alpha=rr["alpha"],
            n_atom=rr["n_atom"],
            uu=np.asarray(rr["uu"], float).copy(),
            lam=np.asarray(rr["lam"], float).copy(),
            c_ar=np.asarray(core.arch_lags(rr["M"], rr["D"]),
                            float))
    return _WIN_CACHE[key]


def anatomy(kz, scramble_seed=None, comb=None, lag_add=None):
    """One rung -> Gram, 12-window compression, deflated mass
    (christoffel_ratio verbatim), EXTENDED by the additive lag
    injection hook lag_add (bit-identical when None)."""
    rr = window_of(kz, scramble_seed=scramble_seed)
    h, M, D, alpha = rr["h"], rr["M"], rr["D"], rr["alpha"]
    if h > H_DEEP_MAX:
        return "TOO-DEEP"
    uu = rr["uu"]
    mm = 2.0 * rr["lam"]
    if comb is not None:
        uu, mm = comb
    c_at, _ = core.atom_lags_at(alpha, M, uu, mm)
    lags = rr["c_ar"] + np.asarray(c_at, float)
    if lag_add is not None:
        lags = lags + np.asarray(lag_add, float)
    d = grid_density(lags)
    L = 2 * M - 2
    xs, ws, uf_p = folded_measure(d, L, +1.0)
    ys, vs, uf_n = folded_measure(d, L, -1.0)
    al, be, m0, steps = lanczos_chain(xs, ws, h + 1)
    if steps < h + 1 or np.any(be <= 0):
        return None
    Pn = eval_chain(al, be, m0, ys, h)
    B = np.sqrt(vs)[:, None] * Pn
    E = B @ B.T
    E = 0.5 * (E + E.T)
    n = E.shape[0]
    out = dict(kz=kz, h=h, n=n, M=M, L=L, D=D,
               alpha=float(alpha))
    G = B.T @ B
    G = 0.5 * (G + G.T)
    egG = np.linalg.eigvalsh(G)
    out["tau_full"] = float(1.0 - egG[-1])
    out["negA"] = int(np.sum(egG > 1.0))
    idx = {int(j): k for k, j in enumerate(uf_n)}
    jav = [j for j in JWIN if j in idx]
    out["full"] = (len(jav) == len(JWIN))
    if out["full"]:
        iw = [idx[j] for j in jav]
        io = [k for k in range(n) if k not in set(iw)]
        IO = np.eye(len(io)) - E[np.ix_(io, io)]
        try:
            CJ = (E[np.ix_(iw, iw)]
                  + E[np.ix_(iw, io)] @ np.linalg.solve(
                      IO, E[np.ix_(io, iw)]))
            out["CJ"] = 0.5 * (CJ + CJ.T)
        except np.linalg.LinAlgError:
            out["full"] = False
    if out["full"]:
        jstar = idx[JWIN[-1]]
        p = Pn[jstar]
        qvec = np.linalg.solve(np.eye(h) - G, p)
        out["m_def"] = float(vs[jstar] * (p @ qvec))
    return out


def win_attrs(r):
    """12-window objects (christoffel_ratio verbatim, trimmed)."""
    A = np.eye(NW) - r["CJ"]
    sg12, ld12 = np.linalg.slogdet(A)
    sg11, ld11 = np.linalg.slogdet(A[:11, :11])
    r["sg_ok"] = (sg12 == 1.0 and sg11 == 1.0)
    r["d12"] = math.exp(ld12 - ld11) * sg12 * sg11
    ew = np.linalg.eigvalsh(A)
    r["tau12"] = float(ew[0])
    r["c"] = r["d12"] / r["tau12"] if r["tau12"] != 0.0 \
        else float("inf")
    return r


def ldl_pivots(A):
    """Sequential no-pivoting LDL pivots d_1..d_n (SPEC iii); a
    zero pivot terminates, remaining pivots typed dead (nan)."""
    A = np.array(A, dtype=float)
    n = A.shape[0]
    piv = []
    for k in range(n):
        p = float(A[k, k])
        piv.append(p)
        if p == 0.0:
            piv.extend([float("nan")] * (n - k - 1))
            break
        if k + 1 < n:
            v = A[k + 1:, k].copy()
            A[k + 1:, k + 1:] -= np.outer(v, v) / p
    return piv


def word_of(r):
    """(pivots, bits, flipped-set) of one rung's 12-window; r must
    be full."""
    A = np.eye(NW) - r["CJ"]
    piv = ldl_pivots(A)
    bits = [bool(p > 0.0) if np.isfinite(p) else False
            for p in piv]
    neg = [k + 1 for k, b in enumerate(bits) if not b]
    return piv, bits, neg


def word_str(bits):
    return "".join("+" if b else "-" for b in bits)


def quartiles(v):
    q = np.percentile(np.asarray(v, float), [25, 50, 75])
    return float(q[0]), float(q[1]), float(q[2])


def probe_word(kz, **kw):
    """One manipulated build -> syndrome state."""
    try:
        r = anatomy(kz, **kw)
    except (np.linalg.LinAlgError, AssertionError):
        return ("CHAIN-DEATH", None, None)
    if not isinstance(r, dict):
        return ("CHAIN-DEATH", None, None)
    if not (r.get("full") and "CJ" in r):
        return ("WINDOW-LOST", None, r)
    piv, bits, neg = word_of(r)
    return ("WORD", (piv, bits, neg), r)


def inj_signature(kz, A, s):
    """errorterm_demand_curve verbatim: Delta c(t) = A cos(gamma0
    t)(cosh(delta t) - 1), t = j D."""
    w = window_of(kz)
    tt = np.arange(w["M"]) * w["D"]
    return (s * A * np.cos(INJ_GAMMA0 * tt)
            * (np.cosh(INJ_DELTA * tt) - 1.0))


def main():
    section("PRIME.ARITH.HEALTHCODE12.01 -- the 12-bit pivot sign "
            "word: verified + syndrome table (EXPLORATION ONLY; "
            "DIAGNOSTIC, zero RH content)")
    print("    FROZEN_SPEC SHA-256 = %s"
          % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
    print("    NO RH claim; no marker moves.")
    print("\nS0 -- firewall")
    check("S0.1 AST firewall clean", not ast_scan(BANNED_IDS))

    # ------------------------------------------------------------ W
    section("W -- ladders + reproduction wards")
    truth, smooth = [], []
    n_toodeep, n_dead_t, n_dead_s = 0, 0, 0
    for kz in core.frame_a_zones():
        r = anatomy(kz)
        if r == "TOO-DEEP":
            n_toodeep += 1
            continue
        if r is None:
            n_dead_t += 1
            continue
        truth.append(r)
        uu = window_of(kz)["uu"]
        rs = anatomy(kz, comb=(uu, smooth_masses(uu)))
        if isinstance(rs, dict):
            smooth.append(rs)
        else:
            n_dead_s += 1
    truth.sort(key=lambda r: (r["h"], r["kz"]))
    smooth.sort(key=lambda r: (r["h"], r["kz"]))
    print("    truth %d rungs (h %d..%d) | smooth %d rungs (%d "
          "dead)  [%.1f s]"
          % (len(truth), truth[0]["h"], truth[-1]["h"],
             len(smooth), n_dead_s, time.time() - T0))
    check("W0 truth ladder == %d rungs" % N_RUNGS_EXP,
          len(truth) == N_RUNGS_EXP, "%d" % len(truth), kill="KP")
    fullw = [r for r in truth if r.get("full") and "CJ" in r]
    check("W0c full-window census %d == %d"
          % (len(fullw), N_FULLWIN_FROZEN),
          len(fullw) == N_FULLWIN_FROZEN, kill="KP")
    if KILLS:
        return finish({})
    for r in fullw:
        win_attrs(r)
    cs = np.array([r["c"] for r in fullw])
    q1, q2, q3 = quartiles(cs)
    star = [r for r in fullw if r["kz"] == KZ_STAR]
    c21 = star[0]["c"] if star else float("nan")
    h21 = star[0]["h"] if star else -1
    check("W-C1f REPRODUCTION c-quartiles %.0f/%.0f/%.0f == "
          "%.0f/%.0f/%.0f, c(kz%d) %.0f == %.0f at h %d"
          % (q1, q2, q3, REF_Q25, REF_MED, REF_Q75, KZ_STAR, c21,
             REF_C21, h21),
          abs(q1 / REF_Q25 - 1.0) <= REF_RTOL
          and abs(q2 / REF_MED - 1.0) <= REF_RTOL
          and abs(q3 / REF_Q75 - 1.0) <= REF_RTOL
          and abs(c21 / REF_C21 - 1.0) <= REF_RTOL
          and h21 == H_STAR, kill="KW")

    # ------------------------------------------------------------ D
    section("D -- the word is well-defined (LDL vs slogdet vs "
            "deflation identity)")
    dev_d12 = 0.0
    dev_chr = 0.0
    sylv_ok = True
    for r in fullw:
        piv, bits, neg = word_of(r)
        r["piv"], r["bits"], r["negflags"] = piv, bits, neg
        dev_d12 = max(dev_d12, abs(piv[-1] - r["d12"])
                      / max(abs(r["d12"]), 1e-300))
        A = np.eye(NW) - r["CJ"]
        pd = bool(float(np.linalg.eigvalsh(A)[0]) > 0.0)
        sylv_ok &= (all(bits) == pd)
        mu12 = 1.0 / piv[-1] - 1.0
        bar = max(CHR_WARD_FLOOR,
                  CHR_COND_FAC * EPS / max(r["tau_full"], 1e-300))
        dev_chr = max(dev_chr, (abs(mu12 - r["m_def"])
                                / max(abs(r["m_def"]), 1e-300))
                      / bar)
    check("D1 WARD d_12 LDL == slogdet minor quotient: max rel "
          "%.1e <= %.0e" % (dev_d12, D12_WARD),
          dev_d12 <= D12_WARD, kill="KW")
    check("D2 WARD Sylvester consistency all-(+) <=> A_12 PD on "
          "every truth rung", sylv_ok, kill="KW")
    check("D3 WARD mu_12 == m_def (v899 deflation identity): "
          "worst dev/bar %.3f <= 1 (conditioning-aware)"
          % dev_chr, dev_chr <= 1.0, kill="KW")

    # ------------------------------------------------------------ A1
    section("A1 -- THE TRUE WORD (CLAIM-2 + CLAIM-4b)")
    n_allplus = sum(1 for r in fullw if all(r["bits"]))
    softmins = [int(np.argmin(r["piv"])) + 1 for r in fullw]
    n_soft12 = sum(1 for k in softmins if k == 12)
    print("    kz   h    word          softest-k  d_12       "
          "mu_12")
    for r, sk in zip(fullw, softmins):
        print("    %-4d %-4d %s  %2d         %.3e  %.3e"
              % (r["kz"], r["h"], word_str(r["bits"]), sk,
                 r["piv"][-1], 1.0 / r["piv"][-1] - 1.0),
              flush=True)
    check("A1.1 WARD all-(+) word on %d/%d truth full-window "
          "rungs (CLAIM-2, per RUNG not per transition -- "
          "nuance recorded)" % (n_allplus, len(fullw)),
          n_allplus == len(fullw), kill="KW")
    a1 = "SOFTPIVOT-12(%d/%d)" % (n_soft12, len(fullw))
    check("A1.2 typed: %s -- CLAIM-4b (raw-argmin reading) %s"
          % (a1, "CONFIRMED" if n_soft12 == len(fullw)
             else "REFUTED: softest-k census %s; the k = 12 "
             "role is the deflation-identity seat (D3), not raw "
             "softness" % sorted(set(softmins))), True)
    mus = np.array([[1.0 / p - 1.0 for p in r["piv"]]
                    for r in fullw])
    print("    the 12 pivot factors Q_k = 1 + mu_k: mu_k median "
          "per k: %s"
          % " ".join("%.1e" % float(np.median(mus[:, k]))
                     for k in range(NW)))

    # ------------------------------------------------------------ A2
    section("A2 -- CLAIM-3: v897's Epstein control RE-RUN "
            "(read-only exec of the embedded byte-exact source)")
    import v897_certified_interval_ladder as v897mod  # READ-ONLY
    src = v897mod._SRC_0
    if src[:1] == "\n":
        src = src[1:]
    sha_src = hashlib.sha256(src.encode("utf-8")).hexdigest()
    check("A2.1 WARD embedded source SHA-256 == v897 "
          "LADDER_FILE_SHA (%s...)" % v897mod.LADDER_FILE_SHA[:16],
          sha_src == v897mod.LADDER_FILE_SHA, kill="KW")
    mod = types.ModuleType("ball_arithmetic_ladder_probe_ro")
    mod.__file__ = os.path.abspath(__file__)
    exec(compile(src, mod.__file__, "exec"), mod.__dict__)
    t0 = time.time()
    glx, glw, lemma = mod.gl_nodes_enclosed(mod.GL_N)
    mod._GLX, mod._GLW = glx, glw
    check("A2.2 WARD node-enclosure lemma (GL-%d, r = %s)"
          % (mod.GL_N, mod.NODE_R),
          lemma["sign_ok"] and lemma["disjoint"]
          and lemma["contains2"],
          "%.1f s" % (time.time() - t0), kill="KW")
    t0 = time.time()
    res_e = mod.run_control_ball()
    print("    v897 control: h %d | status %s | pivots done %d | "
          "ward rel %.2e | %.1f s"
          % (res_e["h"], res_e["status"].upper(), res_e["npiv"],
             res_e["ward"], time.time() - t0), flush=True)
    check("A2.3 WARD CLAIM-3 where it lives: v897 machinery "
          "REFUSES the Epstein comb at pivot index %d == %d "
          "(h-dimensional certificate pivot, NOT a 12-word flag "
          "-- type distinction recorded)"
          % (res_e["npiv"], V897_NPIV_REF),
          res_e["status"] == "refused"
          and res_e["npiv"] == V897_NPIV_REF, kill="KW")
    # float LDL shadow of the same Epstein K (reported)
    r9w = window_of(CTRL_KZ)
    N_E = int(math.floor(math.exp(2.0 * r9w["alpha"]))) + 1
    lamE_ = lambda_eps(N_E)
    nn = np.nonzero(np.abs(lamE_) > 1e-12)[0]
    uuE = np.log(nn.astype(float))
    mmE = 2.0 * lamE_[nn] / np.sqrt(nn.astype(float))
    c_atE, _ = core.atom_lags_at(r9w["alpha"], r9w["M"], uuE, mmE)
    KE = core.odd_toeplitz(r9w["c_ar"] + np.asarray(c_atE, float),
                           r9w["M"])
    pivE = ldl_pivots(KE)
    firstbad = next((k for k, p in enumerate(pivE)
                     if not (np.isfinite(p) and p > 0.0)), None)
    check("A2.4 float LDL shadow of the Epstein K: first "
          "nonpositive pivot index %s (0-based) vs interval "
          "refusal at %d -- %s (reported)"
          % (firstbad, V897_NPIV_REF,
             "AGREES" if firstbad == V897_NPIV_REF
             else "DIFFERS"), True)

    # ------------------------------------------------------------ A3
    section("A3 -- CLAIM-4a: the smooth first-flip census")
    smfull = [r for r in smooth if r.get("full") and "CJ" in r]
    firstflips = []
    n_flagged = 0
    for r in smfull:
        piv, bits, neg = word_of(r)
        r["bits"], r["negflags"] = bits, neg
        if neg:
            n_flagged += 1
            firstflips.append(neg[0])
    census = sorted(set(firstflips))
    hist = {k: firstflips.count(k) for k in census}
    print("    smooth full-window rungs: %d; words with >= 1 "
          "negative flag: %d; first-flip index census: %s "
          "(claim: {1, 3})" % (len(smfull), n_flagged, hist))
    for r in smfull[:6]:
        print("    e.g. kz %-4d h %-4d word %s neg flags %s"
              % (r["kz"], r["h"], word_str(r["bits"]),
                 r["negflags"]), flush=True)
    a3 = ("SMOOTHCLAIM-CONFIRMED" if census == [1, 3]
          else "SMOOTHCLAIM-REFUTED(first-flip=%s)" % census)
    check("A3.1 typed: %s" % a3, True)

    # ------------------------------------------------------------ B
    section("B -- THE SYNDROME TABLE (seeded battery on the %d "
            "shallowest full-window rungs)" % N_BAT)
    bat = fullw[:N_BAT]
    print("    battery rungs: %s"
          % ", ".join("kz %d (h %d)" % (r["kz"], r["h"])
                      for r in bat))
    print("\n  B1 -- INJ-COSH (delta %.2f, gamma0 %.1f, both "
          "signs, ladder %s):" % (INJ_DELTA, INJ_GAMMA0,
                                  list(INJ_LADDER)))
    for r in bat:
        found = None
        for A in INJ_LADDER:
            for s in (+1.0, -1.0):
                st, wd, _rr = probe_word(
                    r["kz"], lag_add=inj_signature(r["kz"], A, s))
                if st != "WORD":
                    found = (A, s, st, None)
                    break
                if wd[2]:
                    found = (A, s, "WORD", wd[2])
                    break
            if found:
                break
        if found:
            A, s, st, neg = found
            print("    kz %-4d h %-4d: first flip at A* = %g "
                  "(sign %+d) -> %s"
                  % (r["kz"], r["h"], A, int(s),
                     ("flags %s" % neg) if st == "WORD" else st),
                  flush=True)
        else:
            print("    kz %-4d h %-4d: NO flip up to A = %g"
                  % (r["kz"], r["h"], INJ_LADDER[-1]), flush=True)
    print("\n  B2 -- SCRAMBLE (seeds %s):" % (SCR_SEEDS,))
    for r in bat:
        outs = []
        for sd in SCR_SEEDS:
            st, wd, _rr = probe_word(r["kz"], scramble_seed=sd)
            outs.append("seed %d: %s" % (sd,
                        ("flags %s" % wd[2]) if st == "WORD"
                        else st))
        print("    kz %-4d h %-4d: %s"
              % (r["kz"], r["h"], " | ".join(outs)), flush=True)
    print("\n  B3 -- SMOOTH (binary):")
    for r in bat:
        uu = window_of(r["kz"])["uu"]
        st, wd, _rr = probe_word(r["kz"],
                                 comb=(uu, smooth_masses(uu)))
        print("    kz %-4d h %-4d: %s"
              % (r["kz"], r["h"],
                 ("word %s flags %s" % (word_str(wd[1]), wd[2]))
                 if st == "WORD" else st), flush=True)
    print("\n  B4 -- MASS-RESCALE (factors %s):"
          % (RSC_FACTORS,))
    for r in bat:
        uu = window_of(r["kz"])["uu"]
        mm = 2.0 * window_of(r["kz"])["lam"]
        outs = []
        for f in RSC_FACTORS:
            st, wd, _rr = probe_word(r["kz"], comb=(uu, f * mm))
            if st != "WORD":
                outs.append("f=%.2f: %s" % (f, st))
            elif wd[2]:
                outs.append("f=%.2f: flags %s" % (f, wd[2]))
            else:
                outs.append("f=%.2f: clean" % f)
        print("    kz %-4d h %-4d: %s"
              % (r["kz"], r["h"], " | ".join(outs)), flush=True)
    check("B.1 syndrome table recorded (measurement; the word is "
          "a DIAGNOSTIC classifier of manipulated combs -- zero "
          "RH content)", True)

    # ------------------------------------------------------------ C
    section("C -- controls")
    check("C0 WARD truth wall holds (neg(A) = 0 on all rungs)",
          all(r["negA"] == 0 for r in truth), kill="KW")
    check("C-S WARD the smooth world flips >= 1 flag on >= 1 "
          "full-window rung (%d flagged of %d)"
          % (n_flagged, len(smfull)), n_flagged >= 1, kill="KW")
    ok_c = True
    for nmc, kw in (("Epstein",
                     dict(comb=(uuE, mmE))),
                    ("scramble", dict(scramble_seed=1))):
        st, wd, rr = probe_word(CTRL_KZ, **kw)
        if st == "CHAIN-DEATH":
            print("    %-8s: chain dies -> FIRES" % nmc)
            continue
        fired = (rr["negA"] > 0
                 or (st == "WORD" and bool(wd[2])))
        ok_c &= fired
        print("    %-8s: neg(A) %d | %s -> %s"
              % (nmc, rr["negA"],
                 ("flags %s" % wd[2]) if st == "WORD" else st,
                 "FIRES" if fired else "SILENT"), flush=True)
    check("C-E controls fire", ok_c, kill="KW")

    # ------------------------------------------------------------
    section("DISCREPANCY LIST vs the incoming plan summary")
    print("""    DISC-1 (ATTRIBUTION): the '12 pivot factors' do NOT live in
           v897 -- v897's certificates are h-dimensional integer-
           Bareiss / validated-Cholesky pivot chains with no
           12-structure; the 12-word lives in the v899 12-window
           compression (this probe).  CLAIM-3 is the only genuine
           v897 fact and holds there (A2).
    DISC-2 (GRANULARITY): the word is per RUNG (37 full-window
           rungs), not per ladder TRANSITION.
    DISC-3 (SMOOTH FLAGS): see A3 -- the measured first-flip
           census replaces the claimed 'flags 1 and 3'.""")

    return finish(dict(a1=a1, a3=a3))


def finish(labels):
    section("V -- FROZEN VERDICT")
    n_pass = sum(1 for _n, okk in CHECKS if okk)
    n_tot = len(CHECKS)
    if KILLS:
        VERDICT = {"KP": "PIPELINE-BROKEN",
                   "KW": "WARD-BROKEN"}[KILLS[0]]
        print("\n  VERDICT: %s" % VERDICT)
    else:
        VERDICT = ("HEALTHCODE12-MEASURED / DIAGNOSTIC-ONLY / "
                   "TRUEWORD-ALLPLUS / %(a1)s / "
                   "V897-PIVOT10-REPRODUCED / %(a3)s" % labels)
        print("\n  VERDICT: %s" % VERDICT)
    print("""
  HONEST FRAME (as frozen): the 12-bit word is a DIAGNOSTIC
  classifier for manipulated combs on the deployed finite
  windows.  Its all-(+) truth state is the certified census
  repackaged through Sylvester -- no new positivity, no RH
  content in either direction.  The plan-claim audit corrections
  (attribution, granularity, smooth flags) are recorded above.
  No marker moves.""")
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed"
          % (time.time() - T0, n_tot, n_tot - n_pass))
    return 0 if n_pass == n_tot else 1


if __name__ == "__main__":
    raise SystemExit(main())
