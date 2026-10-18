#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""port_signfree_normalization_probe -- PRIME.PORT.SIGNFREE.NORMALIZATION.01
(EXPLORATION ONLY, experiments/; round 57: de-circularize the v900
normalization -- the exact core update in a SIGN-FREE normalization
whose update coefficients never read tau_{h+1} or any wall sign.
2026-08-10.)

THE QUESTION (frozen).  v900 (PRIME.PORT.NORMALIZED.CORE.01,
promoted from normalized_core_update_probe round 55) proved the
EXACT update X_{h+1} = c_h (X_h + U_h) for the normalized 8x8 core
X_h = S_h / tau_h, with c_h = tau_h / tau_{h+1}.  That coordinate
is CIRCULAR for any propagation theorem: tau_{h+1} = lambda_min(
A_{h+1}) is the wall scale whose SIGN is the very thing to be
propagated -- the update coefficient reads the unknown.  This
probe transcribes the SAME exact update into sign-free coordinates
    Y_h := S_h / ell(S_h),
    Y_{h+1} = g_h (Y_h + V_h),   g_h := ell(S_h)/ell(S_{h+1}),
    V_h := (S_{h+1} - S_h)/ell(S_h),
where ell is a SOURCE-ONLY functional: computable from the comb
linear algebra (Gram + block solve) WITHOUT any lambda_min / sign
query of the wall, so that g_h contains NO forward-sign input.
The algebraic transcription is an identity for ANY nonzero ell;
the CONTENT is measured: which candidate ell (i) stays positive on
the whole ladder, (ii) keeps the family {Y_h} bounded, (iii) keeps
the coefficients g_h tame -- the de-circularization criterion is
(i) + exactness + (ii), the winner is the tamest.

HONEST FRAME (frozen, said up front): the one-step positivity
margin is SCALING-INVARIANT -- Y_h = (tau_h/ell_h) X_h and V_h =
(tau_h/ell_h) U_h, so lambda_min(Y^{-1/2} V Y^{-1/2}) ==
lambda_min(X^{-1/2} U X^{-1/2}) EXACTLY (warded below).  The
sign-free coordinates change NOTHING about the measured margins;
what changes is the BOOKKEEPING: every coefficient of the update
becomes a source-side functional, so a future invariant-region /
propagation theorem needs no forward tau-sign input in its
dynamics.  Also honest: S_h = B_h - Xc_h R_h^{-1} Xc_h^T needs the
EXTERIOR block R_h invertible -- the already-certified-safe outer
block (v893: lambda_min(R) >= c_R tau with trendless c_R = 210;
negR = 0 on every truth rung, reproduced here); and positivity of
a trace/determinant functional of S is a MEASURED fact, far weaker
than PD -- it does not presuppose the wall.

THE FOUR FROZEN CANDIDATES (all source-only; chosen from what the
v900 objects actually expose):
  ELL-A  TRACE-CORE       ell = tr(S_h)/8       (Schur-core trace)
  ELL-B  DET-CORE         ell = det(S_h)^{1/8}  (slogdet route;
         DEAD on a rung if the determinant sign is not +1 -- the
         sign is RECORDED, never presumed)
  ELL-C  TRACE-OUTER      ell = tr(R_h)/(n-8)   (trace of the
         certified-safe exterior block)
  ELL-D  QUAD-MASS        ell = sum_j v_j       (total mass of the
         folded NEG-node quadrature that carries A = I - E; a
         positive readout of the constructional measure, >= 0 by
         construction)

FROZEN PROTOCOL (2026-08-10; machinery verbatim from
normalized_core_update_probe (round 55) with gram_anatomy EXTENDED
by two scalars: tr(R) and sum(v); pipeline physics bit-identical):

 W   PIPELINE + REPRODUCTION WARDS (kill -> PIPELINE-BROKEN /
     WARD-BROKEN): W1 42 reachable rungs, all chains complete, all
     tau finite; W2 >= 30 full-core rungs; W3 truth all-PSD +
     >= 20 consecutive full-core steps; W4 deepcore product law
     max |lamS*wcore/tau - 1| <= 1e-6; W5 inheritance floor min
     eta_core = 0.0315 (tol 5.001e-5); W6 the v900 exact update
     reproduced: max rel ||X' - c(X+U)|| <= 1e-10, and the c-range
     [0.051, 19.50] reproduced at rtol 2e-2.

 N1  THE CIRCULARITY STATEMENT + THE TRANSCRIPTION (per candidate,
     per consecutive full-core step): WARDS (kill -> WARD-BROKEN):
       N1.a TRANSCRIPTION: ||Y' - g (Y + V)||_F / ||Y'||_F <=
            TRANS_WARD = 1e-10 on every step (candidates with
            ell > 0 on both rungs of the step);
       N1.b SCALING CONSISTENCY: ||Y - (tau/ell) X||_F /
            ||Y||_F <= SCAL_WARD = 1e-12 per rung (tau is used
            ONLY inside this crosscheck ward, never in the
            construction);
       N1.c MARGIN INVARIANCE: |lambda_min(Y^{-1/2} V Y^{-1/2}) -
            lambda_min(X^{-1/2} U X^{-1/2})| <= INV_WARD = 1e-8
            per step (the honest-frame identity, warded).

 N2  THE MEASUREMENTS (per candidate; all typed, never kill):
     (i)  POSITIVITY OF ell: count of full-core truth rungs with
          ell <= 0 (DET-CORE: sign != +1) -> ELL-DEAD(count) if
          any;
     (ii) BOUNDEDNESS of {Y_h}: log-log slope of lambda_max(Y_h)
          vs h, band |slope| <= SLOPE_BND = 0.15 (v900's frozen
          band); Frobenius diameter printed ->
          BOUNDED(diam) / UNBOUNDED(slope);
     (iii) SOURCE-ONLY EXPOSURE: kappa_h = ell_h / tau_h printed
          (min/max/ratio).  With tau = ell/kappa the circular
          coefficient factors EXACTLY as
              c_h = tau_h/tau_{h+1} = g_h x (kappa_{h+1}/kappa_h)
          -- a source-only coefficient times a coordinate factor;
          boundedness of kappa (and of its step ratio) is the
          de-circularization content, printed per candidate;
          corr(log g, log c) printed;
     (iv) TAMENESS: the coefficient range [min g, max g] and the
          spread ratio max(g)/min(g) (requires all g > 0, else
          candidate is coefficient-signed -> recorded).
     TYPED WINNER (frozen rule): among candidates with zero
     ELL-DEAD rungs, exact transcription, and BOUNDED family, the
     winner is argmin of the g-spread ratio -> DECIRC-ACHIEVED(
     winner) with TAMEST(winner, ratio); if no candidate passes ->
     DECIRC-OPEN.

 C   CONTROLS (kill -> WARD-BROKEN if silent): C0 truth wall
     neg(A) = 0 on every rung.  C1 SMOOTH world (masses
     2 e^{u/2} du, verbatim): neg(A) > 0 on >= 1 rung AND the
     winner's Y-machinery must EXIT on the smooth family: on >= 1
     smooth full-core rung, S not PSD or ell <= 0 or the rung is
     rung-level violated (the sign-free normalization must NOT
     hide the smooth failure).  C2 Epstein x^2+5y^2 comb and
     scramble (seed 1) at kz 9: neg(A) > 0 or chain death on
     BOTH; the winner ell status there is printed.

KILLS: K1 a W1-W3 pipeline ward breaks -> PIPELINE-BROKEN; K2 a
reproduction/identity/control ward (W4-W6, N1.a-c, C0-C2) breaks
-> WARD-BROKEN.  N2 outcomes are measurements, never kills.

VERDICT (frozen enum): SIGNFREE-MEASURED with typed sublabels
DECIRC-ACHIEVED(ell) / DECIRC-OPEN, TAMEST(ell, ratio), and the
four per-candidate labels; else PIPELINE-BROKEN / WARD-BROKEN.

FROZEN BARS: CORE_J = (2,4,...,16); H_LADDER_MAX = 900;
N_RUNGS_EXP = 42; MIN_CORE_RUNGS = 30; MIN_STEPS = 20;
REPRO_PROD_BAR = 1e-6; REPRO_ETA_MIN = 0.0315; ROUND_TOL =
5.001e-5; XUPD_WARD = 1e-10; C_RANGE_REF = [0.051, 19.50] (rtol
2e-2); TRANS_WARD = 1e-10; SCAL_WARD = 1e-12; INV_WARD = 1e-8;
SLOPE_BND = 0.15; CTRL_KZ = 9; scramble seed 1.

SMOKE-RUN DISCLOSURE (2026-08-10, before freezing): one smoke run
of this script (18/18 with the identical bars; no bar, rule or
enum was tuned to it -- the winner rule above predates the run)
measured the picture that is frozen here as context: ELL-A/ELL-B
(core trace/determinant-root) TRACK tau -- kappa = ell/tau
bounded within ratio ~3.1/~2.8, families BOUNDED (slopes -0.020 /
-0.035) -- but their coefficients inherit the full c-spread
(g-spread ~421/~250, corr(log g, log c) ~ +0.96); ELL-C/ELL-D
are O(1) source functionals with TAME coefficients (spread
~1.3/~2.1) that do NOT track tau, so their Y-families inherit
tau's decay (slopes ~ -3.1/-3.4, UNBOUNDED).  The TRADE-OFF
(bounded family <-> tame coefficients) is the honest first-class
finding of this probe; the de-circularization itself (kappa and
its step ratio bounded for the core functionals) holds for BOTH
tau-tracking candidates.  All wards are identities,
deployed-ledger reproductions (v900 printed numbers) or controls
frozen a priori.

SPEC v1 (2026-08-10, frozen + SHA-hashed before the frozen run):
everything above.  Mechanical concretizations frozen with v1:
(i) window memoization per (kz, seed) (v900 verbatim); (ii)
candidate ELL-B uses np.linalg.slogdet(S) and is DEAD on a rung
iff sign != +1.0; (iii) slopes/OLS as in v900 (population
statistics); (iv) the winner ladder table prints Y-diagnostics
for the winner only, summaries for the rest; (v) g-spread uses
only steps where both rung ells are positive.

NO RH claim: the sign-free transcription is exact bookkeeping on
the deployed v563 window ladder; nothing here proves tau_h > 0
beyond the certified census (v897), and the propagation theorem
(bounded g + margin > -1 for all h) remains open.  No marker
moves.

FIREWALL: no zeros, no prime oracles (AST scan; banned ids
zetazero / nzeros / primerange / isprime / primepi / nextprime /
prevprime); v563 READ-ONLY; RNG only inside the declared scramble
control; stdout only.

Sources (read-only): v563_paper2_readouts; full wall operator +
fixed-core split + exact update machinery verbatim from
normalized_core_update_probe.py (PRIME.PORT.NORMALIZED.CORE.01,
round 55; promoted as v900); exterior-reserve reading from v893
(PRIME.PORT.RELFLAG.01, c_R = 210); certified base v884/v887/v897
-- declared inputs, not re-run.

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/port_signfree_normalization_probe.py
"""

import ast
import hashlib
import math
import os
import sys
import time

import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
_VERIFY = os.path.abspath(os.path.join(_HERE, "..", "..",
                                       "verification"))
sys.path.insert(0, _HERE)
sys.path.insert(0, _VERIFY)

import v563_paper2_readouts as core        # noqa: E402  (READ-ONLY)

CORE_J = (2, 4, 6, 8, 10, 12, 14, 16)
H_LADDER_MAX = 900
N_RUNGS_EXP = 42
MIN_CORE_RUNGS = 30
MIN_STEPS = 20
REPRO_PROD_BAR = 1e-6          # W4 deepcore product law
REPRO_ETA_MIN = 0.0315         # W5 deepcore eta_core floor
ROUND_TOL = 5.001e-5
XUPD_WARD = 1e-10              # W6 v900 exact update
C_MIN_REF, C_MAX_REF = 0.051, 19.50    # v900 printed c range
C_RANGE_RTOL = 2e-2
TRANS_WARD = 1e-10             # N1.a transcription
SCAL_WARD = 1e-12              # N1.b scaling consistency
INV_WARD = 1e-8                # N1.c margin invariance
SLOPE_BND = 0.15               # N2 boundedness band (v900)
CTRL_KZ = 9
R_SING_TOL_REL = 1e-10
BANNED_IDS = ("zetazero", "nzeros", "primerange", "isprime",
              "primepi", "nextprime", "prevprime")
CAND_NAMES = ("ELL-A(tr-core)", "ELL-B(det-core)",
              "ELL-C(tr-outer)", "ELL-D(quad-mass)")

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


# --------------- pipeline, verbatim (normalized_core_update_probe)
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
    """SPEC concretization (i): pure memoization of the
    deterministic core.build_window (v900 verbatim)."""
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


def ladder_zones():
    """The 42 reachable rungs (christoffel_zone_envelope verbatim)."""
    out = []
    for kz in core.frame_a_zones():
        D_k = 0.5 * float(core.G_ALL[kz]) / float(core.NU_MAIN)
        M_k = int(math.ceil(float(core.U_ALL[kz]) / D_k - 1.0e-9)) + 1
        if M_k % 2:
            M_k += 1
        if M_k // 2 <= H_LADDER_MAX:
            out.append(kz)
    return out


def smooth_masses(uu):
    """PNT-mean masses 2 e^{u/2} du (lattice_parametrix B1)."""
    return 2.0 * np.exp(uu / 2.0) * cell_widths(uu)


def world_smooth(uu, mm, rr):
    return uu, smooth_masses(uu)


def gram_anatomy(kz, world_fn=None, scramble_seed=None, comb=None,
                 want_vec=False):
    """v900 verbatim wall + fixed-core split, EXTENDED with two
    source-only scalars: tr(R) and the total NEG-quadrature mass
    sum(v) (bit-identical physics otherwise)."""
    rr = window_of(kz, scramble_seed=scramble_seed)
    M, D, alpha, h = rr["M"], rr["D"], rr["alpha"], rr["h"]
    uu = rr["uu"]
    mm = 2.0 * rr["lam"]
    if world_fn is not None:
        uu, mm = world_fn(uu, mm, rr)
    if comb is not None:
        uu, mm = comb
    c_at, _ = core.atom_lags_at(alpha, M, uu, mm)
    d = grid_density(rr["c_ar"] + np.asarray(c_at, float))
    L = 2 * M - 2
    xs, ws, _ = folded_measure(d, L, +1.0)
    ys, vs, uf_n = folded_measure(d, L, -1.0)
    al, be, m0, steps = lanczos_chain(xs, ws, h + 1)
    if steps < h + 1 or np.any(be <= 0):
        return None
    Pn = eval_chain(al, be, m0, ys, h)
    G = np.sqrt(vs)[:, None] * (Pn @ Pn.T) * np.sqrt(vs)[None, :]
    G = 0.5 * (G + G.T)
    n = G.shape[0]
    A = np.eye(n) - G
    out = dict(kz=kz, h=h, n=n, alpha=float(alpha))
    out["mneg"] = float(np.sum(vs))            # EXTENSION (ELL-D)
    if want_vec:
        evA, VA = np.linalg.eigh(A)
    else:
        evA = np.linalg.eigvalsh(A)
        VA = None
    out["tau"] = float(evA[0])
    out["negA"] = int(np.sum(evA < 0.0))
    idx = {int(j): k for k, j in enumerate(uf_n)}
    out["core_ok"] = all(j in idx for j in CORE_J)
    if not out["core_ok"]:
        return out
    ic = np.array([idx[j] for j in CORE_J], dtype=int)
    icset = set(ic.tolist())
    ib = np.array([k for k in range(n) if k not in icset],
                  dtype=int)
    B = A[np.ix_(ic, ic)]
    Xc = A[np.ix_(ic, ib)]
    R = A[np.ix_(ib, ib)]
    evR = np.linalg.eigvalsh(R)
    out["lamR"] = float(evR[0])
    out["negR"] = int(np.sum(evR < 0.0))
    out["trR"] = float(np.trace(R))            # EXTENSION (ELL-C)
    out["Rsing"] = bool(float(np.min(np.abs(evR)))
                        < R_SING_TOL_REL
                        * float(np.max(np.abs(evR))))
    Z = np.linalg.solve(R, Xc.T)
    Y = Xc @ Z
    Y = 0.5 * (Y + Y.T)
    S = B - Y
    S = 0.5 * (S + S.T)
    evS = np.linalg.eigvalsh(S)
    out["S"] = S
    out["lamS"] = float(evS[0])
    out["lamSmax"] = float(evS[-1])
    out["negS"] = int(np.sum(evS < 0.0))
    if want_vec:
        v = VA[:, 0]
        out["wcore"] = float(np.sum(v[ic] ** 2))
    return out


def inv_sqrt(M):
    w, V = np.linalg.eigh(M)
    return V @ np.diag(w ** -0.5) @ V.T


def ols_line(x, y):
    """OLS y = a + b x; returns (a, b, R^2)."""
    x = np.asarray(x, float)
    y = np.asarray(y, float)
    vx = float(np.var(x))
    if vx == 0.0:
        return float(np.mean(y)), 0.0, float("nan")
    b = float(np.cov(x, y, bias=True)[0, 1] / vx)
    a = float(np.mean(y) - b * np.mean(x))
    ss = float(np.sum((y - a - b * x) ** 2))
    st = float(np.sum((y - np.mean(y)) ** 2))
    return a, b, (1.0 - ss / st if st > 0 else float("nan"))


def corr(x, y):
    return float(np.corrcoef(np.asarray(x, float),
                             np.asarray(y, float))[0, 1])


def ell_values(r):
    """The four frozen source-only candidates on one rung.
    Returns list of (value or None); None = ELL-DEAD channel
    (ELL-B determinant sign != +1)."""
    S = r["S"]
    out = []
    out.append(float(np.trace(S)) / 8.0)                 # ELL-A
    sg, ld = np.linalg.slogdet(S)
    out.append(math.exp(ld / 8.0) if sg == 1.0 else None)  # ELL-B
    out.append(r["trR"] / float(r["n"] - 8))             # ELL-C
    out.append(r["mneg"])                                # ELL-D
    return out


def main():
    section("PRIME.PORT.SIGNFREE.NORMALIZATION.01 -- the exact "
            "core update in sign-free coordinates (EXPLORATION "
            "ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s"
          % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
    print("    NO RH claim; no marker moves.")
    print("\nS0 -- firewall")
    check("S0.1 AST firewall clean", not ast_scan(BANNED_IDS))

    # ------------------------------------------------------------ W
    section("W -- the truth ladder + v900 reproduction wards")
    zones = ladder_zones()
    check("W1 frozen rung count %d" % N_RUNGS_EXP,
          len(zones) == N_RUNGS_EXP, "found %d" % len(zones),
          kill="K1")
    truth = []
    for kz in zones:
        r = gram_anatomy(kz, want_vec=True)
        if r is None:
            print("    kz %-3d: CHAIN SHORT" % kz, flush=True)
        truth.append(r)
    ok_chain = all(r is not None for r in truth)
    check("W1b all chains complete", ok_chain, kill="K1")
    if not ok_chain:
        return finish({})
    truth.sort(key=lambda r: (r["h"], r["kz"]))
    check("W1c all tau finite",
          all(np.isfinite(r["tau"]) for r in truth), kill="K1")
    full = [r for r in truth if r["core_ok"]]
    check("W2 >= %d full-core rungs" % MIN_CORE_RUNGS,
          len(full) >= MIN_CORE_RUNGS,
          "%d full-core rungs" % len(full), kill="K1")
    ok_psd = all(r["negA"] == 0 and r["negR"] == 0
                 and r["negS"] == 0 for r in full)
    check("W3a WARD truth all-PSD (A, R, S) on every full-core "
          "rung", ok_psd, kill="K1")
    print("    h range %d..%d  [%.1f s]"
          % (truth[0]["h"], truth[-1]["h"], time.time() - T0))
    if KILLS:
        return finish({})
    prods = np.array([r["lamS"] * r["wcore"] / r["tau"]
                      for r in full])
    prod_dev = float(np.max(np.abs(prods - 1.0)))
    check("W4 REPRODUCTION deepcore product law: max "
          "|lamS*wcore/tau - 1| = %.3e <= %.0e"
          % (prod_dev, REPRO_PROD_BAR), prod_dev <= REPRO_PROD_BAR,
          kill="K2")
    steps = []
    for r1, r2 in zip(truth, truth[1:]):
        if (r1 is None or r2 is None or not r1.get("core_ok")
                or not r2.get("core_ok")):
            continue
        if r1["lamS"] <= 0.0 or r1["negA"] > 0:
            continue
        steps.append((r1, r2))
    check("W3b >= %d consecutive full-core steps" % MIN_STEPS,
          len(steps) >= MIN_STEPS, "%d steps" % len(steps),
          kill="K1")
    etas_core = []
    for r1, r2 in steps:
        Wi = inv_sqrt(r1["S"])
        etas_core.append(float(np.linalg.eigvalsh(
            Wi @ r2["S"] @ Wi)[0]))
    eta_min = float(np.min(etas_core))
    check("W5 REPRODUCTION deepcore inheritance floor: min "
          "eta_core %.4f == %.4f (tol %.1e)"
          % (eta_min, REPRO_ETA_MIN, ROUND_TOL),
          abs(eta_min - REPRO_ETA_MIN) <= ROUND_TOL, kill="K2")
    # W6: the v900 exact update in the circular coordinates
    for r in full:
        r["X"] = r["S"] / r["tau"]
    xrec_dev = 0.0
    u_list = []
    for r1, r2 in steps:
        c = r1["tau"] / r2["tau"]
        U = (r2["S"] - r1["S"]) / r1["tau"]
        Xn = c * (r1["X"] + U)
        xr = (float(np.linalg.norm(Xn - r2["X"]))
              / max(float(np.linalg.norm(r2["X"])), 1e-300))
        xrec_dev = max(xrec_dev, xr)
        u_list.append((c, U))
    cs = np.array([c for (c, _U) in u_list])
    ok_crange = (abs(float(np.min(cs)) / C_MIN_REF - 1.0)
                 <= C_RANGE_RTOL
                 and abs(float(np.max(cs)) / C_MAX_REF - 1.0)
                 <= C_RANGE_RTOL)
    check("W6 REPRODUCTION v900 exact update: max rel ||X' - "
          "c(X+U)|| %.2e <= %.0e; c range [%.5f, %.5f] == "
          "[%.3f, %.2f] (rtol %.0e)"
          % (xrec_dev, XUPD_WARD, float(np.min(cs)),
             float(np.max(cs)), C_MIN_REF, C_MAX_REF,
             C_RANGE_RTOL),
          xrec_dev <= XUPD_WARD and ok_crange, kill="K2")
    if KILLS:
        return finish({})

    # ------------------------------------------------------------ N1
    section("N1 -- THE CIRCULARITY + THE SIGN-FREE TRANSCRIPTION")
    print("    v900 coefficient c_h = tau_h/tau_{h+1}: READS the "
          "sign of tau_{h+1} -- the unknown to be propagated.")
    print("    sign-free: Y = S/ell(S), Y' = g (Y + V), g = "
          "ell_h/ell_{h+1}, V = DS/ell_h -- NO forward-sign "
          "input.")
    ncand = len(CAND_NAMES)
    ELL = np.full((len(full), ncand), np.nan)
    dead = np.zeros(ncand, dtype=int)
    for i, r in enumerate(full):
        for k, v in enumerate(ell_values(r)):
            if v is None:
                dead[k] += 1
            else:
                ELL[i, k] = v
    idx_of = {id(r): i for i, r in enumerate(full)}
    print("\n    the candidate ladder (full-core rungs):")
    print("    kz   h     tau        " + "  ".join(
        "%-11s" % nm for nm in CAND_NAMES))
    for i, r in enumerate(full):
        print("    %-4d %-4d %.3e  " % (r["kz"], r["h"], r["tau"])
              + "  ".join(("%11.4e" % ELL[i, k])
                          if np.isfinite(ELL[i, k]) else
                          "%11s" % "DEAD"
                          for k in range(ncand)), flush=True)

    trans_dev = np.zeros(ncand)
    scal_dev = np.zeros(ncand)
    inv_dev = np.zeros(ncand)
    gco = [[] for _ in range(ncand)]
    mX_list = []
    for (c, U), (r1, r2) in zip(u_list, steps):
        Wi = inv_sqrt(r1["X"])
        mX = float(np.linalg.eigvalsh(Wi @ U @ Wi)[0])
        mX_list.append(mX)
        i1, i2 = idx_of[id(r1)], idx_of[id(r2)]
        DS = r2["S"] - r1["S"]
        for k in range(ncand):
            e1, e2 = ELL[i1, k], ELL[i2, k]
            if not (np.isfinite(e1) and np.isfinite(e2)
                    and e1 > 0.0 and e2 > 0.0):
                continue
            g = e1 / e2
            gco[k].append(g)
            Y1 = r1["S"] / e1
            Y2 = r2["S"] / e2
            V = DS / e1
            tr = (float(np.linalg.norm(Y2 - g * (Y1 + V)))
                  / max(float(np.linalg.norm(Y2)), 1e-300))
            trans_dev[k] = max(trans_dev[k], tr)
            sc = (float(np.linalg.norm(
                Y1 - (r1["tau"] / e1) * r1["X"]))
                / max(float(np.linalg.norm(Y1)), 1e-300))
            scal_dev[k] = max(scal_dev[k], sc)
            Wy = inv_sqrt(Y1)
            mY = float(np.linalg.eigvalsh(Wy @ V @ Wy)[0])
            inv_dev[k] = max(inv_dev[k], abs(mY - mX))
    check("N1.a TRANSCRIPTION WARD: max rel ||Y' - g(Y+V)|| = "
          "%.2e <= %.0e (all candidates, all live steps)"
          % (float(np.max(trans_dev)), TRANS_WARD),
          float(np.max(trans_dev)) <= TRANS_WARD, kill="K2")
    check("N1.b SCALING WARD: max rel ||Y - (tau/ell) X|| = %.2e "
          "<= %.0e (tau used ONLY in this crosscheck)"
          % (float(np.max(scal_dev)), SCAL_WARD),
          float(np.max(scal_dev)) <= SCAL_WARD, kill="K2")
    check("N1.c MARGIN-INVARIANCE WARD: max |lam_min(Y-rel V) - "
          "lam_min(X-rel U)| = %.2e <= %.0e (the margin is "
          "coordinate-invariant, said honestly)"
          % (float(np.max(inv_dev)), INV_WARD),
          float(np.max(inv_dev)) <= INV_WARD, kill="K2")

    # ------------------------------------------------------------ N2
    section("N2 -- MEASUREMENTS: positivity, boundedness, "
            "source-only exposure, tameness (per candidate)")
    hh = np.array([r["h"] for r in full], float)
    labels = []
    passing = []
    for k, nm in enumerate(CAND_NAMES):
        col = ELL[:, k]
        livemask = np.isfinite(col)
        n_nonpos = int(dead[k] + np.sum(col[livemask] <= 0.0))
        if n_nonpos > 0:
            lab = "%s: ELL-DEAD(%d)" % (nm, n_nonpos)
            labels.append(lab)
            print("    %s -- %d rungs with ell <= 0 or dead "
                  "determinant sign" % (lab, n_nonpos))
            continue
        lamYmax = np.array([r["lamSmax"] / col[i]
                            for i, r in enumerate(full)])
        _, slope, _ = ols_line(np.log(hh), np.log(lamYmax))
        vecs = [r["S"].flatten() / col[i]
                for i, r in enumerate(full)]
        diam = 0.0
        for i in range(len(vecs)):
            for j in range(i + 1, len(vecs)):
                diam = max(diam, float(np.linalg.norm(
                    vecs[i] - vecs[j])))
        kap = np.array([col[i] / r["tau"]
                        for i, r in enumerate(full)])
        g = np.array(gco[k])
        gpos = bool(np.all(g > 0.0))
        gratio = (float(np.max(g)) / float(np.min(g))
                  if gpos else float("inf"))
        cg = corr(np.log(g), np.log(cs)) if gpos else float("nan")
        bounded = abs(slope) <= SLOPE_BND
        lab = ("%s: %s" % (nm,
               "BOUNDED(diam=%.3g, slope=%+.3f)" % (diam, slope)
               if bounded else "UNBOUNDED(slope=%+.3f)" % slope))
        labels.append(lab)
        print("    %s" % lab)
        print("      ell range [%.3e, %.3e]; kappa = ell/tau in "
              "[%.3e, %.3e] (ratio %.3g)"
              % (float(np.min(col)), float(np.max(col)),
                 float(np.min(kap)), float(np.max(kap)),
                 float(np.max(kap)) / float(np.min(kap))))
        print("      g = ell/ell' range [%.4f, %.4f], spread "
              "ratio %.3g, all g > 0: %s; corr(log g, log c) = "
              "%+.4f"
              % (float(np.min(g)), float(np.max(g)), gratio,
                 gpos, cg))
        print("      EXACT factorization: c_h = g_h x "
              "(kappa_{h+1}/kappa_h); kappa-ratio range "
              "[%.4f, %.4f]"
              % (float(np.min(kap[1:] / kap[:-1])),
                 float(np.max(kap[1:] / kap[:-1]))))
        if (bounded and gpos
                and trans_dev[k] <= TRANS_WARD):
            passing.append((k, gratio))
    if passing:
        kwin, ratio_win = min(passing, key=lambda t: t[1])
        winner = CAND_NAMES[kwin]
        decirc = "DECIRC-ACHIEVED(%s)" % winner
        tamest = "TAMEST(%s, spread=%.3g)" % (winner, ratio_win)
    else:
        kwin = None
        winner = None
        decirc = "DECIRC-OPEN"
        tamest = "TAMEST(n/a)"
    check("N2.1 typed: %s / %s" % (decirc, tamest), True)
    if kwin is not None:
        print("\n    the WINNER ladder (Y = S/ell, %s):" % winner)
        print("    kz   h     ell        lamin(Y)   lamax(Y)   "
              "kappa=ell/tau")
        for i, r in enumerate(full):
            e = ELL[i, kwin]
            print("    %-4d %-4d %.4e %10.6f %10.4f  %.4e"
                  % (r["kz"], r["h"], e, r["lamS"] / e,
                     r["lamSmax"] / e, e / r["tau"]), flush=True)
        print("\n    the sign-free update statement (measured "
              "constants): Y' = g (Y + V) with g source-only in "
              "[%.4f, %.4f];"
          % (float(np.min(gco[kwin])), float(np.max(gco[kwin]))))
        print("    PD propagates along the ladder iff 1 + "
              "lam_min(Y^{-1/2} V Y^{-1/2}) > 0 at every step "
              "(min measured %.4f) -- IDENTICAL margins to v900 "
              "(N1.c), but NO coefficient reads tau_{h+1}."
              % (1.0 + float(np.min(mX_list))))

    # ------------------------------------------------------------ C
    section("C -- controls: smooth world + Epstein/scramble")
    check("C0.1 WARD truth wall holds on every rung (neg(A) = 0)",
          all(r["negA"] == 0 for r in truth), kill="K2")
    print("  C1 -- the smooth-mass world (2 e^{u/2} du):")
    sm = []
    for kz in zones:
        r = gram_anatomy(kz, world_fn=world_smooth)
        if r is not None:
            sm.append(r)
    n_viol = sum(1 for r in sm if r["negA"] > 0)
    n_exit = 0
    n_smfull = 0
    for r in sm:
        if not r.get("core_ok"):
            continue
        n_smfull += 1
        vals = ell_values(r)
        ew = (vals[kwin] if kwin is not None else vals[0])
        s_bad = r["negS"] > 0
        e_bad = (ew is None) or (ew <= 0.0)
        if s_bad or e_bad or r["negA"] > 0:
            n_exit += 1
    print("    %d rungs built; neg(A) > 0 on %d; winner "
          "Y-machinery exits (S not PSD / ell <= 0 / rung "
          "violated) on %d of %d full-core smooth rungs"
          % (len(sm), n_viol, n_exit, n_smfull))
    check("C1.1 WARD smooth violates at rung level (neg(A) > 0 "
          "somewhere)", n_viol > 0, kill="K2")
    check("C1.2 WARD winner Y-machinery exits on >= 1 smooth "
          "full-core rung (the sign-free normalization must not "
          "hide the failure)", n_exit >= 1, kill="K2")
    print("  C2 -- Epstein + scramble at kz %d:" % CTRL_KZ)
    rr9 = window_of(CTRL_KZ)
    N_E = int(math.floor(math.exp(2.0 * rr9["alpha"]))) + 1
    lamE_ = lambda_eps(N_E)
    nn = np.nonzero(np.abs(lamE_) > 1e-12)[0]
    ctl = {"Epstein": gram_anatomy(
               CTRL_KZ, comb=(np.log(nn.astype(float)),
                              2.0 * lamE_[nn]
                              / np.sqrt(nn.astype(float)))),
           "scramble": gram_anatomy(CTRL_KZ, scramble_seed=1)}
    fired_all = True
    for name, r in ctl.items():
        if r is None:
            print("    %-9s: chain dies -> fires (frame death)"
                  % name)
            continue
        f = r["negA"] > 0
        fired_all &= f
        stat = "n/a"
        if r.get("core_ok"):
            vals = ell_values(r)
            ew = (vals[kwin] if kwin is not None else vals[0])
            stat = ("ell=%.3e negS=%d"
                    % (ew if ew is not None else float("nan"),
                       r["negS"]))
        print("    %-9s: tau %+.3e  neg(A) %d  [winner status: "
              "%s] -> %s"
              % (name, r["tau"], r["negA"], stat,
                 "FIRES" if f else "SILENT"), flush=True)
    check("C2.1 WARD both controls fire (neg(A) > 0 or chain "
          "death)", fired_all, kill="K2")

    return finish(dict(decirc=decirc, tamest=tamest,
                       labels=labels))


def finish(labels):
    section("V -- FROZEN VERDICT")
    n_pass = sum(1 for _n, okk in CHECKS if okk)
    n_tot = len(CHECKS)
    if KILLS:
        VERDICT = {"K1": "PIPELINE-BROKEN",
                   "K2": "WARD-BROKEN"}[KILLS[0]]
        print("\n  VERDICT: %s" % VERDICT)
    else:
        VERDICT = ("SIGNFREE-MEASURED / %(decirc)s / %(tamest)s"
                   % labels)
        print("\n  VERDICT: %s" % VERDICT)
        for lab in labels.get("labels", []):
            print("    " + lab)
    print("""
  HONEST FRAME (as frozen): the sign-free transcription is exact
  bookkeeping; the positivity margins are coordinate-invariant
  (N1.c) and NOTHING here proves tau_h > 0 beyond the certified
  census (v897).  The content is the measured de-circularization:
  which source-only ell keeps ell > 0, the family bounded and the
  coefficients tame -- so that a propagation theorem needs no
  forward tau-sign input in its dynamics.  NO RH claim.  No
  marker moves.""")
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed"
          % (time.time() - T0, n_tot, n_tot - n_pass))
    return 0 if n_pass == n_tot else 1


if __name__ == "__main__":
    raise SystemExit(main())
