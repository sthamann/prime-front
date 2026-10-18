#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""port_seated_pivot_probe -- PRIME.PORT.SEATEDPIVOT.01
(EXPLORATION ONLY, experiments/; round 42, seat-repair half of the
leading-sign contract, 2026-08-09).

THE CONTRACT (frozen): re-test the leading-sign law
    sigma = kappa * rho + o(rho)
with the 1-D Schur pivot SEATED AT THE PORT instead of at the
global argmax.  The round-42 diagnosis (PRIME.PORT.KZ19.01) typed
the single kappa outlier kz 19 (h = 313) as SIGMA-ARITHMETIC with
the mechanism: its raw pivot atom m* = argmax T_m sits at a
near-degenerate BULK node (tau = 13.56, top-2 gap 2.7e-3) while
every ladder neighbor pivots at the port (tau ~ 0.85); the
shallow cancellation sigma/a = 691 x ladder median follows from
the decoupled seat.  QUESTION: does the law become LAWFUL
(R^2 >= 0.90, slope ~ 1) once every rung pivots at the port?

INPUTS (measured, reused VERBATIM, not re-derived):
  sigma machinery = the exact 1-D Schur pivot of
    PRIME.PORT.SCALAR.01 (sigma = a - beta warded against
    1/[(I-E)^{-1}]_{mm} at 1e-9), only the PIVOT NODE changes;
  rho = (1/8) sum_{j=1..8} [(d_at(theta_j) - pred_j)/pred_j]^2,
    the FIT-FREE Mellin-Cauchy relative-L2 port fluctuation of
    PRIME.PORT.LEADING.SIGN.01 / PRIME.PORT.MELLIN.01, VERBATIM;
  port set = negative-side nodes with tau_m <= tau_max/10 (the
    lowest-tau-decile cut of PRIME.PORT.SCHUR.01, VERBATIM);
  raw-law priors (round 41, declared): slope +1.022, R^2 0.743.
All consume the READ-ONLY deployed core v563_paper2_readouts.

FROZEN PROTOCOL (2026-08-09; all 42 reachable rungs h <= 900;
controls kz 9):

 P1  SEAT CENSUS (full table): per rung the raw argmax seat
     m*_raw (index, tau_m value, port membership under the decile
     cut) and the PORT-SEATED pivot m*_port = the port atom with
     maximal testing value T_m = E_mm.  Census printed: on how
     many rungs do the two seats differ?  (If m*_raw is a port
     atom the seats coincide by construction.)

 P2  THE PORT-SEATED SCALAR: sigma_port :=
     1/[(I-E)^{-1}]_{m*_port, m*_port}, EXACT by the same 1-D
     Schur identity (a_p - b_p^T B_p^{-1} b_p, no approximation,
     just a different pivot node).  HONEST ONE-DIRECTIONAL
     CAVEAT (stated once, binding): I - E > 0 IMPLIES every 1-D
     diagonal Schur complement is positive (ANY pivot), so on
     truth rungs tau_wall > 0 FORCES sigma_port > 0 -- that
     NECESSITY direction is the ward here.  The CONVERSE FAILS:
     a single positive scalar at one pivot does NOT certify the
     wall (only the split at a pivot together with B > 0 restores
     the equivalence, which is what the raw-argmax contract
     PRIME.PORT.SCALAR.01 uses).  sigma_port is therefore a
     WITNESS COORDINATE of the wall, not a certificate.  WARDS:
     exactness a_p - beta_p == 1/[(I-E)^{-1}]_{pp} at rel <=
     1e-9 on all truth rungs; sigma_port > 0 whenever
     tau_wall > 0 (necessity).  On the two controls the
     port-node INDICATOR may or may not fire through this node
     -- which one fires is REPORTED, never killed.

 P3  THE LAW RE-TEST (the deliverable): kappa_port =
     sigma_port / rho with the SAME frozen rho; log-log
     regression of sigma_port on rho over all 42 rungs: slope,
     R^2, sd(log kappa_port), drift d log kappa_port / d alpha.
     The raw-seat regression is recomputed in-run as the
     baseline.  Typed: SEATED-LAWFUL iff R^2 >= 0.90 AND slope
     in [0.8, 1.2]; SEATED-IMPROVED iff 0.743 < R^2 < 0.90;
     SEATED-FLAT otherwise.  All honest, never kill.

 P4  KZ 19 READOUT: the kz {16, 18, 19, 20, 21} ledger with BOTH
     seats (a, beta, sigma = a - beta, cancellation depth
     sigma/a) -- does kz 19 rejoin the family when seated at the
     port?

 P5  DEGENERACY GUARD (report): per rung the top-2 testing gap
     AT THE PORT SEAT (max T_m minus second max T_m over the
     port atoms); rungs with gap < 5e-3 flagged as
     near-degenerate seats (candidates for residual scatter).

 C   CONTROLS (kz 9, must fire): Epstein x^2+5y^2 and scramble
     combs fire ON THE VALUE via the raw-seat channel of
     PRIME.PORT.SCALAR.01 (sigma_raw < 0 OR the rest block goes
     indefinite) while the pipeline itself persists; the
     port-seated scalar at the same combs is printed (fires /
     silent -- the P2 caveat in action).

KILLS: KW exactness ward or the truth necessity sign ward fails
-> WARD-BROKEN; KP pipeline breaks (ladder incomplete / port set
empty on a truth rung / Lanczos breakdown) -> PIPELINE-BROKEN;
KC controls silent on the raw channel -> CONTROL-DEAD.
P1/P3/P4/P5 typed or report, never kill.

VERDICT (frozen enum): SEATEDPIVOT-MEASURED (+ typed sublabel
SEATED-LAWFUL / SEATED-IMPROVED / SEATED-FLAT) /
PIPELINE-BROKEN / WARD-BROKEN / CONTROL-DEAD.

HONEST FRAME: a lawful seated regression on 42 rungs is a FINITE
statement about the measured ladder and about WHERE the law-
carrying scalar lives (the port seat); it does not certify the
wall (P2 caveat) and carries no asymptotic content.  NO RH
claim.  No marker moves.

FIREWALL: no zeros, no prime oracles (AST scan; banned:
zetazero/nzeros/primerange/isprime/primepi/nextprime/prevprime);
v563 READ-ONLY; RNG only in the declared scramble control;
stdout only.

Sources (read-only): v563_paper2_readouts;
port_scalar_schur_probe (Schur pivot, VERBATIM);
leading_sign_kappa_probe (rho + raw-law priors, VERBATIM);
port_schur_reduction_probe (port decile cut, VERBATIM);
kz19_anomaly_probe (diagnosis, declared input).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/port_seated_pivot_probe.py
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
NEIGH = (16, 18, 19, 20, 21)
WARD_TOL = 1e-9
PORT_CUT = 1.0 / 10.0
GAP_FLAG = 5e-3
# round-41 raw-law priors (declared, baseline for P3)
PRIOR_SLOPE_RAW = 1.022
PRIOR_R2_RAW = 0.743
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
# ---- kz19_anomaly_probe); carleson_E returns the negative-side
# ---- node data (ys, vs, uf) for the seat census.

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
    ys, vs, uf = folded_measure(b["d"], L, -1.0)
    al, be, m0, steps = lanczos_chain(xs, ws, h + 1)
    if steps < h + 1 or np.any(be <= 0):
        return None
    Pn = eval_chain(al, be, m0, ys, h)
    E = np.sqrt(vs)[:, None] * (Pn @ Pn.T) * np.sqrt(vs)[None, :]
    E = 0.5 * (E + E.T)
    return dict(E=E, ys=ys, vs=vs, uf=uf)


def pivot_split(E, m, want_rest_eig=False):
    """Exact 1-D Schur split of I - E at pivot node m (VERBATIM
    scalar_split of port_scalar_schur_probe with a free pivot)."""
    n = E.shape[0]
    rest = [i for i in range(n) if i != m]
    a = 1.0 - float(E[m, m])
    bvec = E[m, rest]
    B = np.eye(n - 1) - E[np.ix_(rest, rest)]
    beta = float(bvec @ np.linalg.solve(B, bvec))
    sigma = a - beta
    lamR = (float(np.linalg.eigvalsh(
        E[np.ix_(rest, rest)])[-1]) if want_rest_eig else None)
    return dict(a=a, beta=beta, sigma=sigma, lamR=lamR)


def seats_of(E, uf, L, D):
    """(m_raw, m_port, tau_m array, port mask, port top-2 gap,
    decile boundary tau_max/10)."""
    dg = np.diag(E)
    tau_m = (2.0 * math.pi * uf / L) / D
    bnd = float(np.max(tau_m)) * PORT_CUT
    port = tau_m <= bnd
    m_raw = int(np.argmax(dg))
    ip = np.where(port)[0]
    if len(ip) == 0:
        return m_raw, None, tau_m, port, None, bnd
    m_port = int(ip[np.argmax(dg[ip])])
    if len(ip) >= 2:
        dgp = np.sort(dg[ip])[::-1]
        gap = float(dgp[0] - dgp[1])
    else:
        gap = float("inf")
    return m_raw, m_port, tau_m, port, gap, bnd


# ---- rho machinery, VERBATIM (port_mellin_cauchy_probe /
# ---- leading_sign_kappa_probe).

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


def rho_named(b):
    """The frozen named rho (relative L2 over the 8 port modes)."""
    rel = []
    for j in PORTSET:
        act = float(b["d_at"][j])
        pf = pred_port(b, j)
        rel.append((act - pf) / pf)
    rel = np.asarray(rel)
    return float(np.mean(rel ** 2))


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
    section("PRIME.PORT.SEATEDPIVOT.01 -- the leading-sign law "
            "with the Schur pivot seated AT THE PORT "
            "(EXPLORATION ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s"
          % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
    print("    NO RH claim; sigma_port is a witness coordinate, "
          "not a certificate (P2 caveat); no marker moves.")
    print("\nS0 -- firewall")
    check("S0.1 AST firewall clean", not ast_scan(BANNED_IDS))

    section("P1/P2 -- seat census + the port-seated scalar "
            "(full ladder)")
    print("    port cut: tau_m <= tau_max/10 (PRIME.PORT.SCHUR.01"
          " decile, VERBATIM); T_m = E_mm")
    print("    %-4s %-5s %-6s %-8s %-8s %-5s %-6s %-8s %-10s "
          "%-5s"
          % ("kz", "h", "m*raw", "tau_raw", "tau_bnd", "port",
             "m*prt", "tau_prt", "gap@port", "seat"))
    rows = []
    ward_max = 0.0
    sign_ok = True
    port_empty = False
    for kz in core.frame_a_zones():
        b = build_rung(kz)
        r = carleson_E(b)
        if r is None or (isinstance(r, str) and r == "TOO-DEEP"):
            continue
        E = r["E"]
        m_raw, m_port, tau_m, port, gap, bnd = seats_of(
            E, r["uf"], b["L"], b["D"])
        if m_port is None:
            port_empty = True
            continue
        ev = np.linalg.eigvalsh(E)
        tau = 1.0 - float(ev[-1])
        Minv = np.linalg.inv(np.eye(E.shape[0]) - E)
        s_raw = pivot_split(E, m_raw)
        s_prt = (s_raw if m_port == m_raw
                 else pivot_split(E, m_port))
        for m, s in ((m_raw, s_raw), (m_port, s_prt)):
            ward_max = max(
                ward_max,
                abs(s["sigma"] - 1.0 / float(Minv[m, m]))
                / max(abs(1.0 / float(Minv[m, m])), 1e-300))
        sign_ok &= (not tau > 0.0) or (s_prt["sigma"] > 0.0)
        rho = rho_named(b)
        rows.append(dict(kz=kz, h=b["h"], alpha=b["alpha"],
                         tau=tau, rho=rho, gap=gap, bnd=bnd,
                         tau_raw=float(tau_m[m_raw]),
                         m_raw=m_raw, m_port=m_port,
                         raw=s_raw, prt=s_prt,
                         in_port=bool(port[m_raw])))
        print("    %-4d %-5d %-6d %-8.3f %-8.3f %-5s %-6d "
              "%-8.3f %-10.2e %-5s"
              % (kz, b["h"], m_raw, float(tau_m[m_raw]), bnd,
                 "Y" if port[m_raw] else "N", m_port,
                 float(tau_m[m_port]), gap,
                 "SAME" if m_raw == m_port else "DIFF"))
    n_diff = sum(1 for r in rows if r["m_raw"] != r["m_port"])
    check("P1.1 PIPELINE: %d reachable rungs h <= 900 (frozen "
          "%d); port set nonempty on every rung (%s)"
          % (len(rows), N_RUNGS_FROZEN, not port_empty),
          len(rows) == N_RUNGS_FROZEN and not port_empty,
          kill="KP")
    diff_kz = [r["kz"] for r in rows if r["m_raw"] != r["m_port"]]
    r19c = next(r for r in rows if r["kz"] == KZ_STAR)
    check("P1.2 SEAT CENSUS (report): raw and port seats differ "
          "on %d of %d rungs: kz %s (raw seat off-port exactly "
          "there); NOTE the decile boundary scales as tau_max/10 "
          "= pi/(10 D), so at kz 19 (D small) bnd = %.1f and the "
          "tau = %.2f anomalous seat is %s the frozen port "
          "decile" % (n_diff, len(rows), diff_kz, r19c["bnd"],
                      r19c["tau_raw"],
                      "INSIDE" if r19c["in_port"]
                      else "OUTSIDE"), True)
    check("P2.1 WARD exactness: sigma == 1/[(I-E)^{-1}]_{mm} at "
          "BOTH seats on all rungs (max rel %.1e <= %.0e)"
          % (ward_max, WARD_TOL), ward_max <= WARD_TOL,
          kill="KW")
    check("P2.2 WARD necessity: tau_wall > 0 -> sigma_port > 0 "
          "on every truth rung (one-directional: the wall FORCES "
          "the positive scalar, not conversely)", sign_ok,
          kill="KW")

    section("P3 -- the law re-test (the deliverable)")
    rr = [r["rho"] for r in rows]
    sl_raw, r2_raw = loglog_fit(rr, [r["raw"]["sigma"]
                                     for r in rows])
    sl_prt, r2_prt = loglog_fit(rr, [r["prt"]["sigma"]
                                     for r in rows])
    av = np.array([r["alpha"] for r in rows])
    lk = np.log(np.array([r["prt"]["sigma"] / r["rho"]
                          for r in rows]))
    sd_lk = float(np.std(lk))
    drift = float(np.polyfit(av, lk, 1)[0])
    print("    raw seat   (baseline): slope %+.3f, R^2 %.4f "
          "(round-41 prior: %+.3f / %.3f)"
          % (sl_raw, r2_raw, PRIOR_SLOPE_RAW, PRIOR_R2_RAW))
    print("    port seat (this run) : slope %+.3f, R^2 %.4f | "
          "sd(log kappa_port) %.3f | drift d log kappa_port / "
          "d alpha %+.3f" % (sl_prt, r2_prt, sd_lk, drift))
    if r2_prt >= 0.90 and 0.8 <= sl_prt <= 1.2:
        p3_type = "SEATED-LAWFUL"
    elif r2_prt > PRIOR_R2_RAW:
        p3_type = "SEATED-IMPROVED"
    else:
        p3_type = "SEATED-FLAT"
    check("P3.1 typed: %s (bars: R^2 >= 0.90 and slope in "
          "[0.8, 1.2] -> LAWFUL; R^2 > %.3f -> IMPROVED; else "
          "FLAT)" % (p3_type, PRIOR_R2_RAW), True)

    section("P4 -- kz 19 readout: both seats on kz %s"
            % (list(NEIGH),))
    print("    %-4s %-4s %-12s %-12s %-12s %-12s"
          % ("kz", "seat", "a=1-T*", "beta", "sigma", "sigma/a"))
    for r in rows:
        if r["kz"] not in NEIGH:
            continue
        for tag, s in (("raw", r["raw"]), ("port", r["prt"])):
            print("    %-4d %-4s %-12.4e %-12.4e %-12.4e "
                  "%-12.4e%s"
                  % (r["kz"], tag, s["a"], s["beta"], s["sigma"],
                     s["sigma"] / s["a"],
                     "   <-- OUTLIER" if r["kz"] == KZ_STAR
                     else ""))
    d_prt = np.array([r["prt"]["sigma"] / r["prt"]["a"]
                      for r in rows])
    med_d = float(np.median(d_prt))
    r19 = next(r for r in rows if r["kz"] == KZ_STAR)
    d19 = r19["prt"]["sigma"] / r19["prt"]["a"]
    check("P4.1 readout (report): port-seated kz19 sigma/a "
          "%.3e = %.1f x ladder median %.3e (raw seat was "
          "691 x) -- kz 19 %s the family at the port seat"
          % (d19, d19 / med_d, med_d,
             "REJOINS" if d19 / med_d <= 10.0 else
             "still outside"), True)

    section("P5 -- degeneracy guard: top-2 testing gap at the "
            "port seat")
    flagged = [(r["kz"], r["gap"]) for r in rows
               if r["gap"] < GAP_FLAG]
    gaps = np.array([r["gap"] for r in rows
                     if math.isfinite(r["gap"])])
    print("    gap range over the ladder: min %.2e | median "
          "%.2e | max %.2e"
          % (gaps.min(), float(np.median(gaps)), gaps.max()))
    check("P5.1 guard (report): %d rung(s) with port-seat gap < "
          "%.0e: %s (near-degenerate seats -- candidates for "
          "residual scatter)"
          % (len(flagged), GAP_FLAG,
             ["kz %d (%.1e)" % f for f in flagged] or "none"),
          True)

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
        E_c = r_c["E"]
        m_raw, m_port, _tau_m, _port, _gap, _bnd = seats_of(
            E_c, r_c["uf"], b_c["L"], b_c["D"])
        s_raw = pivot_split(E_c, m_raw, want_rest_eig=True)
        fired = (s_raw["sigma"] < 0.0) or (s_raw["lamR"] > 1.0)
        ok &= fired
        if m_port is not None:
            sp = (s_raw["sigma"] if m_port == m_raw
                  else pivot_split(E_c, m_port)["sigma"])
            prt_txt = ("sigma_port %.3e -> %s"
                       % (sp, "fires" if sp < 0.0
                          else "SILENT (P2 caveat in action)"))
        else:
            prt_txt = "port set empty"
        print("    %-8s: raw sigma %.3e | rest lam %.3f -> %s | "
              "%s" % (nmc, s_raw["sigma"], s_raw["lamR"],
                      "FIRES" if fired else "silent", prt_txt))
    check("C1 CONTROLS FIRE on the raw channel (sigma < 0 or "
          "rest indefinite; pipeline persists); port-node "
          "indicator behavior reported above", ok, kill="KC")

    section("V -- FROZEN VERDICT")
    n_pass = sum(1 for _n, okk in CHECKS if okk)
    n_tot = len(CHECKS)
    if KILLS:
        VERDICT = {"KW": "WARD-BROKEN", "KP": "PIPELINE-BROKEN",
                   "KC": "CONTROL-DEAD"}[KILLS[0]]
        print("\n  VERDICT: %s" % VERDICT)
    else:
        VERDICT = "SEATEDPIVOT-MEASURED"
        print("\n  VERDICT: %s (%s)" % (VERDICT, p3_type))
    print("""
  THE CONTRACT STATEMENT (PRIME.PORT.SEATEDPIVOT.01): the
  leading-sign law is re-tested with the exact 1-D Schur scalar
  seated at the port atom instead of the global argmax; on truth
  the wall FORCES sigma_port > 0 (necessity), but a positive
  sigma_port certifies nothing (the P2 one-directional caveat).
  Whether the seated law is lawful is a finite statement about
  the measured 42-rung ladder.  NO RH claim.""")
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed"
          % (time.time() - T0, n_tot, n_tot - n_pass))
    return 0 if n_pass == n_tot else 1


if __name__ == "__main__":
    raise SystemExit(main())
