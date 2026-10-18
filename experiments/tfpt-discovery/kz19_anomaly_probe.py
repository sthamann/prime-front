#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""kz19_anomaly_probe -- PRIME.PORT.KZ19.01
(EXPLORATION ONLY, experiments/; round 42, anatomy of the single
leading-sign outlier, 2026-08-09).

THE CONTRACT (frozen): rung kz 19 (h = 313) breaks the round-41
leading-sign law sigma = kappa rho + o(rho)
(PRIME.PORT.LEADING.SIGN.01): its kappa = sigma/rho = 0.293 sits
two orders of magnitude above the ladder median 1.9e-3, the ONE
outlier that pins R^2(log sigma vs log rho) at 0.743 < 0.90
(LAW-BROKEN typing).  This probe DISSECTS WHY, with frozen
decision rules, and re-fits the law conditioned on the diagnosis
(reported as SENSITIVITY, never as cherry-pick).

INPUTS (measured, reused VERBATIM, not re-derived):
  sigma = a - beta, the 1-D Schur pivot at the testing atom m*:
    a = 1 - T_{m*} = 1 - nu~_{m*} K_h(y*, y*)  (testing margin),
    beta = b^T (I - E_rest)^{-1} b  (coherent backreaction)
    (PRIME.PORT.SCALAR.01, computation verbatim);
  rho = (1/8) sum_{j=1..8} [(d_at(theta_j) - pred_j)/pred_j]^2,
    pred_j the FIT-FREE Mellin-Cauchy continuum prediction
    (PRIME.PORT.MELLIN.01 / LEADING.SIGN.01, verbatim);
  port set = negative-side nodes with tau <= tau_max/10
    (PRIME.PORT.LIMIT.01 decile cut, verbatim convention).
All consume the READ-ONLY deployed core v563_paper2_readouts.

FROZEN TREND (stated once, used everywhere): trend_q(alpha) for
q in {sigma, rho} = the LEAVE-KZ19-OUT log-linear fit of log q
on alpha over the other 41 rungs, evaluated at alpha(kz 19).

FROZEN PROTOCOL (2026-08-09; all 42 reachable rungs h <= 900;
neighborhood = the two reachable ladder rungs on each side of
kz 19 in ladder order, i.e. kz {16, 18, 19, 20, 21} (SPEC v2,
see AMENDMENTS); controls kz 9):

 A1  REPRODUCE: recompute (sigma, rho, kappa) on all 42 rungs;
     WARD sigma == 1/[(I-E)^{-1}]_{m*m*} at rel <= 1e-9 with
     sign(sigma) == sign(tau) on truth; WARD the round-41
     kappa-probe values: kappa(kz19) within 5 percent of 0.293,
     ladder median kappa within 10 percent of 1.9e-3, R^2 within
     0.010 of 0.743.  Print the kz 17..21 neighborhood table.

 A2  DECOMPOSE sigma AT kz 19 vs neighbors: the pivot ledger
     (a, beta, sigma = a - beta, cancellation depth sigma/a) for
     the neighborhood + the ladder quartiles of sigma/a -- is
     sigma
     large because a is large (GEOMETRY: weak testing criticality
     at the pivot) or because the cancellation a ~ beta is
     anomalously shallow (ARITHMETIC)?

 A3  PIVOT/PORT ANATOMY (neighborhood): port-set size, pivot
     index
     m*, node position y* = cos(2 pi f*/L) and tau_{m*}, testing
     value T_{m*}, the gap T_{m*} - T_second (pivot degeneracy?),
     and the port-decile boundary tau_max/10 (is kz 19's port
     set anomalous in size or boundary?).

 A4  WINDOW COMMENSURABILITY (neighborhood): alpha, D, h, the
     tent-taper edge u_max = (M-1) D, the distance from u_max to
     the nearest prime-power log n (heavy atom AT the taper
     edge?), and the largest single-atom mass in the last half
     log-unit [u_max - 0.5, u_max] vs neighbors.

 A5  RHO SIDE (neighborhood): the SIGNED per-mode deviations
     (d_at(theta_j) - pred_j)/pred_j, j = 1..8, their mean and
     rho -- is rho anomalously SMALL at kz 19 (prediction
     accidentally near-exact / alternating signs summing small)
     rather than sigma large?

 A6  TYPED DIAGNOSIS (the deliverable; rules frozen, evaluated
     in this order):
       RHO-ACCIDENT     iff rho(kz19) < 0.2 x trend_rho(alpha19)
                        AND sigma(kz19) within 3x of
                        trend_sigma(alpha19);
       SIGMA-GEOMETRY   iff a(kz19) > 3 x median a over the
                        neighbors kz {16, 18, 20, 21};
       SIGMA-ARITHMETIC iff (sigma/a)(kz19) > 10 x ladder median
                        of sigma/a AND a(kz19) within 3x of the
                        neighbor median;
       MIXED            otherwise.
     RE-FIT: if RHO-ACCIDENT, refit log sigma vs log rho on all
     42 rungs with rho(kz19) FLOORED at trend_rho(alpha19); else
     refit on the 41 rungs excluding kz 19 (SENSITIVITY, not a
     cherry-pick).  Print new slope/R^2 vs the round-41 0.743.

 C   CONTROLS (kz 9, must fire): Epstein x^2+5y^2 and scramble
     combs -- sigma < 0 OR the rest-block goes indefinite, while
     the pipeline itself persists.

KILLS: KW A1 wards fail (exactness OR round-41 reproduction) ->
WARD-BROKEN; KP pipeline breaks (ladder incomplete / kz 19 or
its 2+2 ladder neighbors missing / Lanczos breakdown) ->
PIPELINE-BROKEN; KC controls silent -> CONTROL-DEAD.  A2..A6
typed, never kill.

VERDICT (frozen enum): KZ19-DIAGNOSED (+ typed cause
SIGMA-GEOMETRY / SIGMA-ARITHMETIC / RHO-ACCIDENT / MIXED) /
PIPELINE-BROKEN / WARD-BROKEN / CONTROL-DEAD.

SPEC v2 AMENDMENTS (mechanical repair, no bar loosened): the v1
neighborhood "kz 17..21" is unreachable AS WRITTEN -- kz 17 is
not a frame-A zone (frame_a_zones() skips it; the ladder runs
..., 16, 18, 19, 20, 21, ...).  v2 fixes the neighborhood to the
two reachable ladder rungs on each side of kz 19 IN LADDER ORDER
(kz {16, 18, 19, 20, 21}) and the SIGMA-GEOMETRY neighbor median
to kz {16, 18, 20, 21}.  All numeric bars, decision rules, wards
and controls are UNCHANGED from v1.

HONEST FRAME: this is single-rung forensics on a measured
42-rung ladder; the re-fit is a SENSITIVITY statement about the
finite ladder, NOT a repair of the law and NOT an asymptotic
claim.  NO RH claim.  No marker moves.

FIREWALL: no zeros, no prime oracles (AST scan; banned:
zetazero/nzeros/primerange/isprime/primepi/nextprime/prevprime);
v563 READ-ONLY; RNG only in the declared scramble control;
stdout only.

Sources (read-only): v563_paper2_readouts;
leading_sign_kappa_probe (sigma/rho/kappa + priors, VERBATIM);
port_scalar_schur_probe (Schur pivot, VERBATIM);
port_mellin_cauchy_probe (pred_j, VERBATIM);
port_limit_operator_probe (port decile cut, convention).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/kz19_anomaly_probe.py
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
KZ_STAR = 19
NEIGH_HALF = 2          # SPEC v2: 2 ladder rungs on each side
WARD_TOL = 1e-9
PORT_CUT = 1.0 / 10.0
# round-41 kappa-probe priors (declared, warded in A1)
PRIOR_KAPPA19 = 0.293
PRIOR_KAPPA_MED = 1.9e-3
PRIOR_R2 = 0.743
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


# ---- sigma machinery, VERBATIM (port_scalar_schur_probe /
# ---- leading_sign_kappa_probe); carleson_E extended only to
# ---- RETURN the negative-side node data (ys, vs, uf) for A3/A4.

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
                alpha=alpha, h=h, uu=uu, mm=mm)


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
    ys, vs, uf = folded_measure(b["d"], L, -1.0)
    al, be, m0, steps = lanczos_chain(xs, ws, h + 1)
    if steps < h + 1 or np.any(be <= 0):
        return None
    Pn = eval_chain(al, be, m0, ys, h)
    E = np.sqrt(vs)[:, None] * (Pn @ Pn.T) * np.sqrt(vs)[None, :]
    E = 0.5 * (E + E.T)
    return dict(E=E, ys=ys, vs=vs, uf=uf)


def scalar_split(E):
    n = E.shape[0]
    dg = np.diag(E).copy()
    mstar = int(np.argmax(dg))
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
    T1 = float(dg[mstar])
    dg[mstar] = -np.inf
    T2 = float(np.max(dg))
    return dict(a=a, beta=beta, sigma=sigma, tau=tau,
                lamR=lamR, sig_ward=sig_ward, mstar=mstar,
                T1=T1, T2=T2)


# ---- rho machinery, VERBATIM (port_mellin_cauchy_probe /
# ---- leading_sign_kappa_probe); rel vector kept for A5.

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


def rho_and_rel(b):
    """(rho, signed rel deviations j=1..8) per the frozen norm."""
    rel = []
    for j in PORTSET:
        act = float(b["d_at"][j])
        pf = pred_port(b, j)
        rel.append((act - pf) / pf)
    rel = np.asarray(rel)
    return float(np.mean(rel ** 2)), rel


def loglog_fit(x, y):
    """slope, R^2 of log y on log x."""
    lx = np.log(np.asarray(x, float))
    ly = np.log(np.asarray(y, float))
    sl, ic = np.polyfit(lx, ly, 1)
    fit = sl * lx + ic
    ss_res = float(np.sum((ly - fit) ** 2))
    ss_tot = float(np.sum((ly - np.mean(ly)) ** 2))
    return float(sl), 1.0 - ss_res / max(ss_tot, 1e-300)


def lin_trend_at(av, logq, a_star):
    """log-linear trend log q ~ alpha, evaluated at a_star."""
    sl, ic = np.polyfit(np.asarray(av, float),
                        np.asarray(logq, float), 1)
    return math.exp(sl * a_star + ic)


def main():
    section("PRIME.PORT.KZ19.01 -- anatomy of the kz 19 "
            "leading-sign outlier (EXPLORATION ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s"
          % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
    print("    NO RH claim; single-rung forensics on the finite "
          "ladder; no marker moves.")
    print("\nS0 -- firewall")
    check("S0.1 AST firewall clean", not ast_scan(BANNED_IDS))

    section("A1 -- reproduce the ladder (sigma, rho, kappa) + "
            "wards")
    rows = {}
    ward_max = 0.0
    sign_ok = True
    for kz in core.frame_a_zones():
        b = build_rung(kz)
        r = carleson_E(b)
        if r is None or (isinstance(r, str) and r == "TOO-DEEP"):
            continue
        s = scalar_split(r["E"])
        rho, rel = rho_and_rel(b)
        rows[kz] = dict(kz=kz, b=b, s=s, rho=rho, rel=rel,
                        kappa=s["sigma"] / rho,
                        ys=r["ys"], vs=r["vs"], uf=r["uf"])
        ward_max = max(ward_max, abs(s["sigma"] - s["sig_ward"])
                       / max(abs(s["sig_ward"]), 1e-300))
        sign_ok &= (s["sigma"] > 0) == (s["tau"] > 0)
    kzs = sorted(rows)
    neigh_ok = (KZ_STAR in rows
                and NEIGH_HALF <= kzs.index(KZ_STAR)
                < len(kzs) - NEIGH_HALF)
    if neigh_ok:
        i_star = kzs.index(KZ_STAR)
        NEIGH = tuple(kzs[i_star - NEIGH_HALF:
                          i_star + NEIGH_HALF + 1])
    else:
        NEIGH = ()
    check("A1.1 PIPELINE: %d reachable rungs h <= 900 (frozen "
          "%d); ladder neighborhood of kz 19 = %s (SPEC v2)"
          % (len(kzs), N_RUNGS_FROZEN, list(NEIGH)),
          len(kzs) == N_RUNGS_FROZEN and neigh_ok, kill="KP")
    check("A1.2 WARD exactness: sigma == 1/[(I-E)^{-1}]_{m*m*} "
          "(max rel %.1e <= %.0e); sign(sigma) == sign(tau)"
          % (ward_max, WARD_TOL),
          ward_max <= WARD_TOL and sign_ok, kill="KW")
    kap_all = np.array([rows[k]["kappa"] for k in kzs])
    kap19 = rows[KZ_STAR]["kappa"]
    kap_med = float(np.median(kap_all))
    sl0, r20 = loglog_fit([rows[k]["rho"] for k in kzs],
                          [rows[k]["s"]["sigma"] for k in kzs])
    check("A1.3 WARD round-41 reproduction: kappa(kz19) %.4f "
          "(prior %.3f, bar 5%%) | median kappa %.3e (prior "
          "%.1e, bar 10%%) | R^2 %.4f (prior %.3f, bar 0.010)"
          % (kap19, PRIOR_KAPPA19, kap_med, PRIOR_KAPPA_MED,
             r20, PRIOR_R2),
          abs(kap19 / PRIOR_KAPPA19 - 1.0) <= 0.05
          and abs(kap_med / PRIOR_KAPPA_MED - 1.0) <= 0.10
          and abs(r20 - PRIOR_R2) <= 0.010, kill="KW")
    print("\n    ladder neighborhood of kz 19 (SPEC v2):")
    print("    %-4s %-5s %-8s %-12s %-12s %-12s"
          % ("kz", "h", "alpha", "sigma", "rho", "kappa"))
    for k in NEIGH:
        r = rows[k]
        print("    %-4d %-5d %-8.3f %-12.4e %-12.4e %-12.4e%s"
              % (k, r["b"]["h"], r["b"]["alpha"], r["s"]["sigma"],
                 r["rho"], r["kappa"],
                 "   <-- OUTLIER" if k == KZ_STAR else ""))

    section("A2 -- the pivot ledger: a, beta, sigma, "
            "cancellation depth sigma/a")
    print("    %-4s %-12s %-12s %-12s %-12s"
          % ("kz", "a=1-T*", "beta", "sigma=a-beta", "sigma/a"))
    for k in NEIGH:
        s = rows[k]["s"]
        print("    %-4d %-12.4e %-12.4e %-12.4e %-12.4e%s"
              % (k, s["a"], s["beta"], s["sigma"],
                 s["sigma"] / s["a"],
                 "   <-- OUTLIER" if k == KZ_STAR else ""))
    depth_all = np.array([rows[k]["s"]["sigma"]
                          / rows[k]["s"]["a"] for k in kzs])
    q1, q2, q3 = np.percentile(depth_all, (25, 50, 75))
    a19 = rows[KZ_STAR]["s"]["a"]
    a_nb = float(np.median([rows[k]["s"]["a"] for k in NEIGH
                            if k != KZ_STAR]))
    d19 = rows[KZ_STAR]["s"]["sigma"] / a19
    print("    ladder sigma/a quartiles: q1 %.3e | median %.3e "
          "| q3 %.3e" % (q1, q2, q3))
    print("    kz19: a/median(neighbor a) = %.2f | (sigma/a) / "
          "ladder-median = %.1f" % (a19 / a_nb, d19 / q2))
    check("A2.1 ledger recorded (report): kz19 sigma/a %.3e vs "
          "ladder median %.3e -- cancellation %s"
          % (d19, q2, "SHALLOW" if d19 > 10.0 * q2 else
             "in family"), True)

    section("A3 -- pivot/port anatomy (port cut tau <= "
            "tau_max/10, PRIME.PORT.LIMIT.01 convention)")
    print("    %-4s %-6s %-6s %-9s %-9s %-10s %-10s %-10s"
          % ("kz", "nport", "m*", "y*", "tau_m*", "T_m*",
             "gap T1-T2", "tau_bnd"))
    for k in NEIGH:
        r = rows[k]
        b, s = r["b"], r["s"]
        tau_m = (2.0 * math.pi * r["uf"] / b["L"]) / b["D"]
        bnd = float(np.max(tau_m)) * PORT_CUT
        nport = int(np.sum(tau_m <= bnd))
        ms = s["mstar"]
        print("    %-4d %-6d %-6d %+-9.5f %-9.4f %-10.6f "
              "%-10.2e %-10.4f%s"
              % (k, nport, ms, float(r["ys"][ms]),
                 float(tau_m[ms]), s["T1"], s["T1"] - s["T2"],
                 bnd, "   <-- OUTLIER" if k == KZ_STAR else ""))
    check("A3.1 anatomy recorded (report): pivot degeneracy gap "
          "kz19 %.2e vs neighbor min %.2e"
          % (rows[KZ_STAR]["s"]["T1"] - rows[KZ_STAR]["s"]["T2"],
             min(rows[k]["s"]["T1"] - rows[k]["s"]["T2"]
                 for k in NEIGH if k != KZ_STAR)), True)

    section("A4 -- window commensurability (taper edge vs the "
            "prime-power comb)")
    print("    %-4s %-8s %-9s %-9s %-10s %-12s %-8s"
          % ("kz", "alpha", "D", "u_max", "d(edge,n)",
             "max-mass@.5", "n@.5"))
    for k in NEIGH:
        b = rows[k]["b"]
        u_edge = (b["M"] - 1) * b["D"]
        dist = float(np.min(np.abs(u_edge - b["uu"])))
        last = b["uu"] >= u_edge - 0.5
        mmax = float(np.max(b["mm"][last])) if np.any(last) \
            else 0.0
        print("    %-4d %-8.3f %-9.5f %-9.3f %-10.4f %-12.4e "
              "%-8d%s"
              % (k, b["alpha"], b["D"], u_edge, dist, mmax,
                 int(np.sum(last)),
                 "   <-- OUTLIER" if k == KZ_STAR else ""))
    check("A4.1 commensurability recorded (report)", True)

    section("A5 -- the rho side: signed per-mode deviations "
            "(d_at - pred)/pred, j = 1..8")
    for k in NEIGH:
        rel = rows[k]["rel"]
        print("    kz %-3d: %s | mean %+.4f | rho %.4e%s"
              % (k, " ".join("%+.4f" % v for v in rel),
                 float(np.mean(rel)), rows[k]["rho"],
                 "   <-- OUTLIER" if k == KZ_STAR else ""))
    check("A5.1 rho anatomy recorded (report)", True)

    section("A6 -- TYPED DIAGNOSIS + diagnosis-conditioned "
            "re-fit")
    a_star = rows[KZ_STAR]["b"]["alpha"]
    oth = [k for k in kzs if k != KZ_STAR]
    av_o = [rows[k]["b"]["alpha"] for k in oth]
    tr_rho = lin_trend_at(av_o, [math.log(rows[k]["rho"])
                                 for k in oth], a_star)
    tr_sig = lin_trend_at(av_o, [math.log(rows[k]["s"]["sigma"])
                                 for k in oth], a_star)
    rho19 = rows[KZ_STAR]["rho"]
    sig19 = rows[KZ_STAR]["s"]["sigma"]
    r_rho = rho19 / tr_rho
    r_sig = sig19 / tr_sig
    r_a = a19 / a_nb
    print("    leave-kz19-out trends at alpha %.3f: rho %.3e "
          "(measured %.3e, ratio %.3f) | sigma %.3e (measured "
          "%.3e, ratio %.3f)"
          % (a_star, tr_rho, rho19, r_rho, tr_sig, sig19, r_sig))
    print("    a(kz19)/neighbor-median a = %.2f | (sigma/a)19 / "
          "ladder-median = %.1f" % (r_a, d19 / q2))
    if r_rho < 0.2 and (1.0 / 3.0) <= r_sig <= 3.0:
        cause = "RHO-ACCIDENT"
    elif r_a > 3.0:
        cause = "SIGMA-GEOMETRY"
    elif d19 > 10.0 * q2 and max(r_a, 1.0 / r_a) <= 3.0:
        cause = "SIGMA-ARITHMETIC"
    else:
        cause = "MIXED"
    check("A6.1 typed cause: %s (frozen rules: rho<0.2x trend & "
          "sigma within 3x -> RHO-ACCIDENT; a>3x neighbors -> "
          "SIGMA-GEOMETRY; sigma/a>10x ladder median & a within "
          "3x -> SIGMA-ARITHMETIC; else MIXED)" % cause, True)
    if cause == "RHO-ACCIDENT":
        rr = [rows[k]["rho"] if k != KZ_STAR else tr_rho
              for k in kzs]
        ss = [rows[k]["s"]["sigma"] for k in kzs]
        mode = "rho(kz19) floored at trend, 42 rungs"
    else:
        rr = [rows[k]["rho"] for k in oth]
        ss = [rows[k]["s"]["sigma"] for k in oth]
        mode = "kz19 excluded, 41 rungs (SENSITIVITY)"
    sl1, r21 = loglog_fit(rr, ss)
    check("A6.2 RE-FIT (%s): slope %+.3f, R^2 %.4f (round-41 "
          "full ladder: slope %+.3f, R^2 %.4f) -- %s"
          % (mode, sl1, r21, sl0, r20,
             "law restored R^2 >= 0.90" if r21 >= 0.90
             else "law still below 0.90"), True)

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
        r_c = carleson_E(b_c)
        s_c = scalar_split(r_c["E"])
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
        print("\n  VERDICT: %s" % VERDICT)
    else:
        VERDICT = "KZ19-DIAGNOSED"
        print("\n  VERDICT: %s (%s)" % (VERDICT, cause))
    print("""
  THE CONTRACT STATEMENT (PRIME.PORT.KZ19.01): the single
  leading-sign outlier kz 19 (h = 313) is dissected into the
  frozen alternatives geometry / arithmetic / rho-accident with
  a diagnosis-conditioned re-fit reported as SENSITIVITY on the
  finite ladder.  The law itself and its derivation half stay
  exactly where round 41 left them.  NO RH claim.""")
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed"
          % (time.time() - T0, n_tot, n_tot - n_pass))
    return 0 if n_pass == n_tot else 1


if __name__ == "__main__":
    raise SystemExit(main())
