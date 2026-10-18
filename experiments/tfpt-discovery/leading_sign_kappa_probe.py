#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""leading_sign_kappa_probe -- PRIME.PORT.LEADING.SIGN.01
(EXPLORATION ONLY, experiments/; round 41, MEASUREMENT HALF of the
leading-sign contract, 2026-08-09).

THE CONTRACT (frozen): test the leading-sign law
    sigma_h = kappa * rho_h + o(rho_h)
with a MEASURED fluctuation-squared candidate for rho_h and a
stability test for kappa.  Inputs (measured, declared, NOT
re-derived here): sigma_h = the 1-D Schur pivot at the testing
atom (PRIME.PORT.SCALAR.01, computation reused VERBATIM); the
fluctuation = the per-rung deviation of the deployed port
numerators d_at(theta_j) from the FIT-FREE Mellin-Cauchy continuum
prediction pred_j (PRIME.PORT.MELLIN.01, prediction reused
VERBATIM; rel 0.375 -> 0.029 along the ladder).  Prior slopes
(v883 chain): slope(log sigma) = -2.93 vs 2x Mellin fluctuation
slope -2.53 (sigma ~ fluctuation^2 within 16 percent).

THE FROZEN RHO (stated once, used everywhere): over the port set
P = {j = 1..8} (the port modes of PRIME.PORT.MELLIN.01),
    rho_h := (1/8) * sum_{j in P} [ (d_at(theta_j) - pred_j)
                                    / pred_j ]^2,
i.e. the SQUARE of the RMS relative fluctuation of the port
numerators, each mode entering with the SAME per-mode 1/|pred_j|
relative weight used in port_mellin_cauchy_probe (its M2 ledger),
aggregated in L2.  No free scale, no fit.

FROZEN PROTOCOL (2026-08-09; all 42 reachable rungs h <= 900;
controls kz 9):

 K1  THE TWO SERIES (full table printed): per rung sigma_h exact,
     WARDED against 1/[(I - E)^{-1}]_{m* m*} at rel <= 1e-9, with
     sign(sigma) == sign(tau) everywhere on truth; and rho_h per
     the frozen norm above.  Table: kz, h, alpha, sigma, rho,
     kappa_h = sigma_h / rho_h.

 K2  THE LAW (typed): regress log sigma on log rho over the 42
     rungs: slope (target 1.0 for the pure law), R^2; and the
     kappa ladder kappa_h = sigma_h/rho_h -- sd(log kappa) and the
     drift slope d log kappa / d alpha.  Typed KAPPA-STABLE iff
     |drift slope| <= 0.15 AND R^2(log-log) >= 0.90;
     KAPPA-DRIFTS iff R^2 >= 0.90 but |drift| > 0.15;
     LAW-BROKEN iff R^2 < 0.90.  All honest, no kill.

 K3  POSITIVITY READING (report): if kappa_h > 0 on every rung,
     print min/median/max and the honest statement: one-sidedness
     on the measured ladder = kappa > 0 THERE; NO asymptotic
     claim.

 K4  CROSS-CANDIDATE (control of the rho choice): repeat the K2
     log-log regression with
       (a) rho'  = [ max_{j in P} |d_at(theta_j) - pred_j| /
                     |pred_j| ]^2   (worst port node only);
       (b) rho'' = tau_h itself (tautological calibration
           reference: sigma-vs-tau slope, prior ~ -2.59/-2.40
           ~ 1.08 -- printed, NOT a law test).
     Typed RHO-NAMED-WINS iff R^2(named rho) > R^2(rho') else
     RHO-WORSTNODE-WINS (honest).

 C   CONTROLS (kz 9, must fire): Epstein and scramble combs --
     sigma < 0 OR the rest-block goes indefinite (the sign/value
     control fires) while the pipeline itself persists.

KILLS: KW exactness ward fails -> WARD-BROKEN; KP pipeline breaks
(ladder incomplete / Lanczos breakdown) -> PIPELINE-BROKEN; KC
controls silent -> CONTROL-DEAD.  K2/K3/K4 typed, never kill.

VERDICT (frozen enum): LEADINGSIGN-MEASURED (+ typed sublabels
KAPPA-STABLE / KAPPA-DRIFTS / LAW-BROKEN and RHO-NAMED-WINS /
RHO-WORSTNODE-WINS) / PIPELINE-BROKEN / WARD-BROKEN /
CONTROL-DEAD.

HONEST FRAME: kappa_h > 0 on 42 rungs is a FINITE statement about
the measured ladder; the leading-sign law with kappa > 0 in the
limit would carry the full RH weight and is NOT claimed.  NO RH
claim.  No marker moves.

FIREWALL: no zeros, no prime oracles (AST scan; banned:
zetazero/nzeros/primerange/isprime/primepi/nextprime/prevprime);
v563 READ-ONLY; RNG only in the declared scramble control; stdout
only.

Sources (read-only): v563_paper2_readouts; port_scalar_schur_probe
(sigma, VERBATIM); port_mellin_cauchy_probe (pred_j and the
per-mode relative weights, VERBATIM); v883 slope chain (declared
prior).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/leading_sign_kappa_probe.py
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

PORTSET = tuple(range(1, 9))
N_RUNGS_FROZEN = 42
WARD_TOL = 1e-9
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


# ---- sigma machinery, VERBATIM from port_scalar_schur_probe ----

def grid_density(c):
    c = np.asarray(c, float)
    a = np.concatenate([c, c[-2:0:-1]])
    d = np.fft.fft(a)
    assert float(np.max(np.abs(d.imag))) <= 1e-9 * max(
        1.0, float(np.max(np.abs(d.real))))
    return d.real


def lambda_eps(N):
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


def build_rung(kz, scramble_seed=None, comb=None):
    rr = core.build_window(kz, scramble_seed=scramble_seed)
    h, M, D, alpha = rr["h"], rr["M"], rr["D"], rr["alpha"]
    uu = np.asarray(rr["uu"], float)
    mm = 2.0 * np.asarray(rr["lam"], float)
    if comb is not None:
        uu, mm = comb
    c_at, _ = core.atom_lags_at(alpha, M, uu, mm)
    c_ar = np.asarray(core.arch_lags(M, D), float)
    d = grid_density(c_ar + np.asarray(c_at, float))
    d_at = grid_density(np.asarray(c_at, float))
    return dict(d=d, d_at=d_at, M=M, D=D, L=2 * M - 2,
                alpha=alpha, h=h, uu=uu)


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


def carleson_E(b):
    h, L = b["h"], b["L"]
    if h > 900:
        return "TOO-DEEP"
    xs, ws, _ = folded_measure(b["d"], L, +1.0)
    ys, vs, _uf = folded_measure(b["d"], L, -1.0)
    al, be, m0, steps = lanczos_chain(xs, ws, h + 1)
    if steps < h + 1 or np.any(be <= 0):
        return None
    Pn = eval_chain(al, be, m0, ys, h)
    E = np.sqrt(vs)[:, None] * (Pn @ Pn.T) * np.sqrt(vs)[None, :]
    E = 0.5 * (E + E.T)
    return E


def scalar_split(E):
    n = E.shape[0]
    mstar = int(np.argmax(np.diag(E)))
    rest = [i for i in range(n) if i != mstar]
    a = 1.0 - float(E[mstar, mstar])
    bvec = E[mstar, rest]
    B = np.eye(n - 1) - E[np.ix_(rest, rest)]
    lamR = float(np.linalg.eigvalsh(
        E[np.ix_(rest, rest)])[-1])
    beta = float(bvec @ np.linalg.solve(B, bvec))
    sigma = a - beta
    ev, _V = np.linalg.eigh(E)
    tau = 1.0 - float(ev[-1])
    Minv = np.linalg.inv(np.eye(n) - E)
    sig_ward = 1.0 / float(Minv[mstar, mstar])
    return dict(a=a, beta=beta, sigma=sigma, tau=tau,
                lamR=lamR, sig_ward=sig_ward, mstar=mstar)


# ---- rho machinery, VERBATIM from port_mellin_cauchy_probe ----

def w_exact(u_arr, M, D, L, j):
    """The exact deployed transform weight per unit mass at
    positions u (LXXXVII convention): 0.5 * sum_i tent_i(u) w_i
    cos(i theta_j)."""
    th = 2.0 * math.pi * j / L
    i0 = np.floor(u_arr / D).astype(int)
    f = u_arr / D - i0

    def w_of(i):
        return np.where((i == 0) | (i == M - 1), 1.0, 2.0)

    tot = np.zeros(len(u_arr))
    for i_at, v_at in ((i0, 1.0 - f), (i0 + 1, f)):
        ok = (i_at >= 0) & (i_at <= M - 1) & (v_at > 0.0)
        tot += np.where(ok, v_at * w_of(i_at)
                        * np.cos(i_at * th), 0.0)
    return 0.5 * tot


def pred_port(b, j):
    """Continuum prediction: -4 sqrt(X) int_0^1 w_j(u(r)) dr."""
    U = float(np.max(b["uu"]))
    rg = np.linspace(1e-6, 1.0, 20000)
    ug = U + 2.0 * np.log(rg)
    keep = ug >= 0.0
    w = w_exact(ug[keep], b["M"], b["D"], b["L"], j)
    return -4.0 * math.exp(U / 2.0) * float(
        np.trapezoid(w, rg[keep]))


def rho_pair(b):
    """(named rho, worst-node rho') per the frozen norms."""
    rel = []
    for j in PORTSET:
        act = float(b["d_at"][j])
        pf = pred_port(b, j)
        rel.append((act - pf) / pf)
    rel = np.asarray(rel)
    rho = float(np.mean(rel ** 2))
    rho_worst = float(np.max(np.abs(rel)) ** 2)
    return rho, rho_worst


def loglog_fit(x, y):
    """slope, R^2 of log y on log x."""
    lx = np.log(np.asarray(x, float))
    ly = np.log(np.asarray(y, float))
    sl, ic = np.polyfit(lx, ly, 1)
    fit = sl * lx + ic
    ss_res = float(np.sum((ly - fit) ** 2))
    ss_tot = float(np.sum((ly - np.mean(ly)) ** 2))
    return float(sl), 1.0 - ss_res / max(ss_tot, 1e-300)


def main():
    section("PRIME.PORT.LEADING.SIGN.01 -- leading-sign law "
            "sigma = kappa rho + o(rho), MEASUREMENT HALF "
            "(EXPLORATION ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s"
          % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
    print("    NO RH claim (finite-ladder statement only); no "
          "marker moves.")
    print("\nS0 -- firewall")
    check("S0.1 AST firewall clean", not ast_scan(BANNED_IDS))

    section("K1 -- the two series (full ladder, table)")
    print("    frozen rho: rho_h = (1/8) sum_{j=1..8} "
          "[(d_at(theta_j) - pred_j)/pred_j]^2  (relative L2 "
          "over the port modes, per-mode 1/|pred_j| weights of "
          "port_mellin_cauchy_probe)")
    print("    %-4s %-5s %-8s %-12s %-12s %-12s"
          % ("kz", "h", "alpha", "sigma", "rho", "kappa"))
    rows = []
    ward_max = 0.0
    sign_ok = True
    for kz in core.frame_a_zones():
        b = build_rung(kz)
        E = carleson_E(b)
        if E is None or (isinstance(E, str) and E == "TOO-DEEP"):
            continue
        s = scalar_split(E)
        rho, rho_w = rho_pair(b)
        kap = s["sigma"] / rho
        rows.append(dict(kz=kz, h=b["h"], alpha=b["alpha"],
                         sigma=s["sigma"], tau=s["tau"], rho=rho,
                         rho_w=rho_w, kappa=kap))
        ward_max = max(ward_max, abs(s["sigma"] - s["sig_ward"])
                       / max(abs(s["sig_ward"]), 1e-300))
        sign_ok &= (s["sigma"] > 0) == (s["tau"] > 0)
        print("    %-4d %-5d %-8.3f %-12.4e %-12.4e %-12.4e"
              % (kz, b["h"], b["alpha"], s["sigma"], rho, kap))
    check("K1.1 PIPELINE: %d reachable rungs h <= 900 (frozen: "
          "%d)" % (len(rows), N_RUNGS_FROZEN),
          len(rows) == N_RUNGS_FROZEN, kill="KP")
    check("K1.2 WARD: sigma == 1/[(I-E)^{-1}]_{m*m*} on all "
          "rungs (max rel %.1e <= %.0e); sign(sigma) == "
          "sign(tau) on truth" % (ward_max, WARD_TOL),
          ward_max <= WARD_TOL and sign_ok, kill="KW")

    section("K2 -- the law (typed)")
    av = np.array([r["alpha"] for r in rows])
    sl, r2 = loglog_fit([r["rho"] for r in rows],
                        [r["sigma"] for r in rows])
    lk = np.log(np.array([r["kappa"] for r in rows]))
    drift = float(np.polyfit(av, lk, 1)[0])
    sd_lk = float(np.std(lk))
    if r2 < 0.90:
        k2_type = "LAW-BROKEN"
    elif abs(drift) <= 0.15:
        k2_type = "KAPPA-STABLE"
    else:
        k2_type = "KAPPA-DRIFTS"
    check("K2.1 typed: %s -- log sigma vs log rho: slope %+.3f "
          "(target 1.0), R^2 %.4f; kappa ladder: sd(log kappa) "
          "%.3f, drift d log kappa / d alpha %+.3f (bars: R^2 >= "
          "0.90, |drift| <= 0.15)"
          % (k2_type, sl, r2, sd_lk, drift), True)

    section("K3 -- positivity reading (report)")
    kaps = np.array([r["kappa"] for r in rows])
    if np.all(kaps > 0):
        print("    kappa_h > 0 on all %d rungs: min %.3e | "
              "median %.3e | max %.3e"
              % (len(rows), kaps.min(), float(np.median(kaps)),
                 kaps.max()))
        print("    HONEST: one-sidedness on the measured ladder "
              "= kappa > 0 THERE; NO asymptotic claim.")
    else:
        print("    kappa_h changes sign on the ladder (%d of %d "
              "rungs negative) -- no one-sidedness reading."
              % (int(np.sum(kaps <= 0)), len(rows)))
    check("K3.1 positivity reading recorded (report)", True)

    section("K4 -- cross-candidates (control of the rho choice)")
    sl_w, r2_w = loglog_fit([r["rho_w"] for r in rows],
                            [r["sigma"] for r in rows])
    sl_t, r2_t = loglog_fit([r["tau"] for r in rows],
                            [r["sigma"] for r in rows])
    print("    (a) worst-node rho': slope %+.3f, R^2 %.4f"
          % (sl_w, r2_w))
    print("    (b) tau calibration:  slope %+.3f, R^2 %.4f "
          "(tautological reference, prior ~ 1.08 -- NOT a law "
          "test)" % (sl_t, r2_t))
    k4_type = ("RHO-NAMED-WINS" if r2 > r2_w
               else "RHO-WORSTNODE-WINS")
    check("K4.1 typed: %s (named R^2 %.4f vs worst-node R^2 "
          "%.4f)" % (k4_type, r2, r2_w), True)

    section("C -- controls (kz 9)")
    rr9 = core.build_window(9)
    N_E = int(math.floor(math.exp(2.0 * rr9["alpha"]))) + 1
    lamE_ = lambda_eps(N_E)
    nn = np.nonzero(np.abs(lamE_) > 1e-12)[0]
    ok = True
    for nmc, kw in (("Epstein", dict(comb=(
            np.log(nn.astype(float)),
            2.0 * lamE_[nn] / np.sqrt(nn.astype(float))))),
            ("scramble", dict(scramble_seed=1))):
        b_c = build_rung(9, **kw)
        E_c = carleson_E(b_c)
        s_c = scalar_split(E_c)
        fired = (s_c["sigma"] < 0.0) or (s_c["lamR"] > 1.0)
        ok &= fired
        print("    %-8s: sigma %.3e | rest lam %.3f -> %s"
              % (nmc, s_c["sigma"], s_c["lamR"],
                 "FIRES" if fired else "silent"))
    check("C1 CONTROLS FIRE (sigma < 0 or rest indefinite; "
          "pipeline persists)", ok, kill="KC")

    section("V -- FROZEN VERDICT")
    n_pass = sum(1 for _n, okk in CHECKS if okk)
    n_tot = len(CHECKS)
    if KILLS:
        VERDICT = {"KW": "WARD-BROKEN", "KP": "PIPELINE-BROKEN",
                   "KC": "CONTROL-DEAD"}[KILLS[0]]
    else:
        VERDICT = "LEADINGSIGN-MEASURED"
    print("\n  VERDICT: %s (%s + %s)" % (VERDICT, k2_type,
                                         k4_type))
    print("""
  THE CONTRACT STATEMENT (PRIME.PORT.LEADING.SIGN.01, measurement
  half): on the measured ladder the scalar wall sigma_h and the
  squared port fluctuation rho_h (fit-free Mellin-Cauchy
  deviation) are compared as sigma = kappa rho + o(rho).  kappa >
  0 on 42 rungs is a FINITE statement; the derivation half (WHY
  kappa > 0) stays open.  NO RH claim.""")
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed"
          % (time.time() - T0, n_tot, n_tot - n_pass))
    return 0 if n_pass == n_tot else 1


if __name__ == "__main__":
    raise SystemExit(main())
