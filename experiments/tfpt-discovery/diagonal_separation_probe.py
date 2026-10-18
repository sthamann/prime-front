#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""diagonal_separation_probe -- PRIME.PORT.DIAGSEP.01
(EXPLORATION ONLY, experiments/; round 42, executing the strategy
memo's DECISIVE LOGIC TEST: is the diagonal (testing) half of the
wall genuinely SEPARATED from RH hardness, or does it inherit the
full difficulty?, 2026-08-09).

THE QUESTION: the wall is lam_max(E_h) <= 1; the diagonal half is
the Carleson TESTING condition max_m T_m = max_m E_mm <= 1
(measured 0.93-0.99 across the ladder, attained at the port).  A
positive matrix can have every diagonal entry < 1 while
lam_max > 1 (coherent off-diagonal accumulation), so T <= 1 is
logically WEAKER than the wall.  The decision: inject the frozen
off-critical-zero signature (the demand-curve family) and measure
whether the deployed diagonal margin dies on the SAME amplitude
scale as the wall (then the pointwise sum-rule theorem inherits
RH-scale hardness) or whether the wall dies while every diagonal
stays below 1 (then the diagonal theorem is genuinely separated
from the hard core and is a candidate for an unconditional proof).
This probe types the LOGICAL relation of two FINITE statements
under a frozen perturbation family -- nothing more.

THE INJECTION (verbatim from errorterm_demand_curve_probe, frozen;
no zeta zeros anywhere -- gamma0 is a GENERIC frozen frequency,
not a zero ordinate): a zero quadruple moved off the critical line
to 1/2 +- delta +- i gamma0 changes the zero-side lag by EXACTLY
    Delta c(tau) = A cos(gamma0 tau) (cosh(delta tau) - 1),
added to the deployed lag vector with sign s.  Built-in NULL: at
delta = 0 the injection vanishes IDENTICALLY.

THE OPERATOR (verbatim round-38/round-41 chain route, READ-ONLY on
v563): perturbed lags -> grid density -> folded positive/negative
measures -> Lanczos chain (h+1 steps, twice-reorthogonalized) ->
E-spectrum via the SIGNED Carleson-Gram identity
E = S D_nu^{1/2} K_CD D_nu^{1/2} S (carleson_testing_law_probe S1,
rel <= 1e-9): lam_max(E) = lam_max(Pn_h^T D_nu Pn_h) and
E_mm = nu~_m K_h(y_m, y_m), both from ONE chain evaluation.  Gate
below re-verifies 1 - lam_max(E) == the pencil Krein floor tau.

FROZEN PROTOCOL (2026-08-09, frozen + SHA-hashed before first
run; heavy rungs kz {9, 12, 13, 26, 40}; deltas {0.05, 0.10}
(the demand-curve grid), gamma0 = 10.0; both signs for the wall
bisection, the diagonal ramped along the wall's WORST sign --
the comparison lives on the identical perturbation ray):

 G   PIPELINE GATE: baseline (A = 0) m_wall = 1 - lam_max(E) > 0
     and m_diag = 1 - max_m E_mm > 0 on every heavy rung, and the
     chain wall margin equals the pencil Krein floor (floor_of)
     to rel 1e-6 -- the E route IS the wall.

 D2  THE CROSSING CENSUS (the deliverable, computed first; D1
     needs A*_wall): per (rung, delta): A*_wall = smallest A
     where m_wall crosses 0 (bisection over both signs, worst
     sign kept, rel tol 1e-3, chain-break counted as crossed --
     fail-first); A*_diag = where m_diag crosses 0 along the SAME
     sign, bracket [0, 10 A*_wall] (if m_diag > 0 still at
     10 A*_wall: record INFINITY and say so).  Separation ratio
     rho_sep = A*_diag / A*_wall.  TYPED (all honest):
       DIAG-SEPARATED   iff rho_sep >= 3   on EVERY cell (the
         wall dies at least 3x earlier -- the diagonal is
         materially insensitive at the wall's kill scale);
       DIAG-INHERITS    iff rho_sep <= 1.5 on SOME cell (the
         first diagonal crosses at essentially the wall scale);
       DIAG-INTERMEDIATE otherwise.

 D1  THE TWO MARGINS ALONG THE RAMP: amplitude ladder A =
     {0.01, 0.03, 0.1, 0.3, 1, 3, 10} x A*_wall (worst sign);
     at each A record m_wall(A), m_diag(A), and the
     port-restricted diagonal margin 1 - max_{m in port} E_mm
     (port = nodes with tau_m <= max(tau_m)/10, the round-38
     port definition).  Two-margin table printed per cell.

 D3  THE MECHANISM READOUT (report, delta = 0.10 per rung): at
     A = A*_wall (the wall's death point) print lam_max, the full
     diagonal profile vs the port (max global / max in-port /
     argmax location), which diagonal entries moved (>= 10 pct
     relative, matched by folded node index; top movers printed;
     appearing/vanishing nodes counted) and the COHERENCE SHARE
     lam_max - max_m E_mm at that A -- the memo's 'coherent
     off-diagonal accumulation' quantified at the kill point.

 D4  NULL WARD: delta = 0 gives Delta c == 0 EXACTLY; both
     margins unchanged at 1e-14 (expected exactly 0).

 C   CONTROLS (kz 9, value controls, must fire): Epstein
     x^2+5y^2 comb and scramble seed 1 -- BOTH margins already
     negative at A = 0 (wall channel AND diagonal channel
     reported; the arithmetic break is a testing violation
     before any injection).

KILLS: K1 pipeline breaks (gate G, bracket failure, chain break
at baseline) -> PIPELINE-BROKEN; K2 null ward fails ->
NULL-BROKEN; K3 a control does not fire on both channels ->
CONTROL-DEAD.

VERDICT (frozen enum): DIAGSEP-MEASURED (+ typed DIAG-SEPARATED /
DIAG-INHERITS / DIAG-INTERMEDIATE) / PIPELINE-BROKEN /
NULL-BROKEN / CONTROL-DEAD.

NO RH claim.  Neither m_wall > 0 nor m_diag > 0 is claimed proved
for any h; the probe measures the RESPONSE of two finite margins
to a frozen off-critical perturbation family and types their
logical relation.  A DIAG-SEPARATED reading licenses analytic
investment in the pointwise sum-rule (testing) theorem; it does
NOT make the wall unconditional.

FIREWALL: no zeros, no prime-table oracles (AST scan; banned:
zetazero/nzeros/primerange/isprime/primepi/nextprime/prevprime);
v563 READ-ONLY; RNG only inside the declared scramble control
(seed 1, verbatim carleson control); writes nothing but stdout.
No marker moves.

Sources (read-only): v563_paper2_readouts;
errorterm_demand_curve_probe (SPEC v3: injection, bisection,
energy law); carleson_testing_law_probe (SPEC v2: signed
identity, testing diagonal, port anatomy); v866/v876 Carleson
chain.

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/diagonal_separation_probe.py
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

RUNGS = (9, 12, 13, 26, 40)
DELTAS = (0.05, 0.10)
GAMMA0 = 10.0
RAMP = (0.01, 0.03, 0.1, 0.3, 1.0, 3.0, 10.0)
DIAG_CEIL = 10.0          # diagonal search ceiling, x A*_wall
BAR_SEP = 3.0             # DIAG-SEPARATED iff rho >= 3 everywhere
BAR_INH = 1.5             # DIAG-INHERITS  iff rho <= 1.5 somewhere
REL_TOL = 1e-3            # bisection relative tolerance
SEED_SCRAMBLE = 1         # verbatim carleson control seed
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


# ---- machinery, verbatim from the two source probes ----------------

def grid_density(c):
    c = np.asarray(c, float)
    a = np.concatenate([c, c[-2:0:-1]])
    d = np.fft.fft(a)
    assert float(np.max(np.abs(d.imag))) <= 1e-9 * max(
        1.0, float(np.max(np.abs(d.real))))
    return d.real


def build_lags(kz, scramble_seed=None, comb=None):
    rr = core.build_window(kz, scramble_seed=scramble_seed)
    h, M, D, alpha = rr["h"], rr["M"], rr["D"], rr["alpha"]
    uu = np.asarray(rr["uu"], float)
    mm = 2.0 * np.asarray(rr["lam"], float)
    if comb is not None:
        uu, mm = comb
    c_at, _ = core.atom_lags_at(alpha, M, uu, mm)
    c_ar = np.asarray(core.arch_lags(M, D), float)
    return dict(c=c_ar + np.asarray(c_at, float), M=M, D=D,
                alpha=alpha, h=h, L=2 * M - 2)


def floor_of(c, M):
    """Pencil Krein floor (verbatim demand-curve probe; gate only)."""
    K = core.odd_toeplitz(c, M)
    d = grid_density(c)
    c_abs = np.real(np.fft.ifft(np.abs(d)))[:M]
    Tabs = core.odd_toeplitz(c_abs, M)
    Gp = 0.5 * (Tabs + K)
    Gm = 0.5 * (Tabs - K)
    ev, V = np.linalg.eigh(Gp)
    if float(ev[0]) <= 0.0:
        return None
    R = V @ np.diag(ev ** -0.5) @ V.T
    A = R @ Gm @ R
    lam = np.linalg.eigvalsh(0.5 * (A + A.T))
    return 1.0 - float(lam[-1])


def zero_signature(M, D, delta, gamma0):
    tt = np.arange(M) * D
    return np.cos(gamma0 * tt) * (np.cosh(delta * tt) - 1.0)


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


# ---- the two margins from one chain evaluation ---------------------

def margins(b, c):
    """Both wall and diagonal margins of E on the lag vector c.
    Returns None on chain break (counted as crossed -- fail-first)."""
    h, L, D = b["h"], b["L"], b["D"]
    d = grid_density(c)
    xs, ws, _ = folded_measure(d, L, +1.0)
    ys, vs, uf_n = folded_measure(d, L, -1.0)
    if len(xs) < h + 1 or len(ys) == 0:
        return None
    al, be, m0, steps = lanczos_chain(xs, ws, h + 1)
    if steps < h + 1 or np.any(be <= 0):
        return None
    Pn = eval_chain(al, be, m0, ys, h + 1)
    B = np.sqrt(vs)[:, None] * Pn[:, :h]
    lam = float(np.linalg.eigvalsh(B.T @ B)[-1])
    Tdiag = vs * np.sum(Pn[:, :h] ** 2, axis=1)
    tau_m = (2.0 * math.pi * uf_n / L) / D
    port = tau_m <= float(np.max(tau_m)) / 10.0
    Tp = float(np.max(Tdiag[port])) if np.any(port) else float("nan")
    return dict(lam=lam, m_wall=1.0 - lam,
                m_diag=1.0 - float(np.max(Tdiag)),
                m_port=1.0 - Tp, Tdiag=Tdiag, uf_n=uf_n,
                port=port, mstar=int(np.argmax(Tdiag)))


def margins_at(b, sig, s, A):
    return margins(b, b["c"] + s * A * sig)


def wall_crossed(r):
    return r is None or r["m_wall"] < 0.0


def diag_crossed(r):
    return r is None or r["m_diag"] < 0.0


def bisect(f_crossed, b, sig, s, lo, hi, steps=40):
    """First-crossing bisection on the ray A -> c + s A sig;
    requires f_crossed at hi; returns hi endpoint (crossed side)."""
    for _ in range(steps):
        if (hi - lo) <= REL_TOL * hi:
            break
        mid = 0.5 * (lo + hi)
        if f_crossed(margins_at(b, sig, s, mid)):
            hi = mid
        else:
            lo = mid
    return hi


def wall_crit(b, sig):
    """Smallest |A| flipping the wall, worst sign (demand-curve
    convention); returns (A*, sign) or (inf, 0)."""
    best = (float("inf"), 0)
    for s in (+1.0, -1.0):
        hi = 4.0
        grow = 0
        while not wall_crossed(margins_at(b, sig, s, hi)) and grow < 8:
            hi *= 4.0
            grow += 1
        if not wall_crossed(margins_at(b, sig, s, hi)):
            continue
        Ast = bisect(wall_crossed, b, sig, s, 0.0, hi)
        if Ast < best[0]:
            best = (Ast, int(s))
    return best


def diag_crit(b, sig, s, A_wall):
    """Diagonal crossing along the SAME ray, ceiling 10 x A*_wall;
    returns A*_diag or inf if the diagonal never crosses."""
    Amax = DIAG_CEIL * A_wall
    if not diag_crossed(margins_at(b, sig, s, Amax)):
        return float("inf")
    return bisect(diag_crossed, b, sig, s, 0.0, Amax)


def main():
    section("PRIME.PORT.DIAGSEP.01 -- is the diagonal (testing) "
            "half separated from RH hardness? (EXPLORATION ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s"
          % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
    print("    NO RH claim; gamma0 = %.1f is a GENERIC frozen "
          "frequency (not a zero ordinate); this probe types the "
          "LOGICAL relation of two finite statements under a "
          "frozen perturbation family; no marker moves." % GAMMA0)
    print("\nS0 -- firewall")
    check("S0.1 AST firewall clean (no zero/prime oracles)",
          not ast_scan(BANNED_IDS))

    section("G -- pipeline gate: baseline margins + chain == pencil")
    bases = {}
    ok_gate = True
    for kz in RUNGS:
        b = build_lags(kz)
        r0 = margins(b, b["c"])
        if r0 is None:
            ok_gate = False
            print("    kz %-3d: CHAIN BREAK at baseline" % kz)
            continue
        tau_p = floor_of(b["c"], b["M"])
        rel = abs(r0["m_wall"] - tau_p) / max(abs(tau_p), 1e-300)
        ok_gate &= (r0["m_wall"] > 0.0 and r0["m_diag"] > 0.0
                    and rel <= 1e-6)
        bases[kz] = (b, r0)
        print("    kz %-3d (h %3d, alpha %.2f): m_wall %.3e "
              "(pencil rel %.1e) | m_diag %.3e | m_port %.3e | "
              "argmax-T in port: %s"
              % (kz, b["h"], b["alpha"], r0["m_wall"], rel,
                 r0["m_diag"], r0["m_port"],
                 bool(r0["port"][r0["mstar"]])), flush=True)
    check("G.1 baseline m_wall > 0, m_diag > 0 on every heavy rung "
          "and chain wall margin == pencil Krein floor (rel <= "
          "1e-6): the E route IS the wall", ok_gate, kill="K1")

    section("D2 -- the crossing census (bisection, rel 1e-3)")
    census = {}
    ok_pipe = True
    for kz in RUNGS:
        b, r0 = bases[kz]
        for de in DELTAS:
            sig = zero_signature(b["M"], b["D"], de, GAMMA0)
            Aw, sgn = wall_crit(b, sig)
            if not math.isfinite(Aw):
                ok_pipe = False
                print("    kz %-3d delta %.2f: WALL NEVER CROSSES "
                      "(bracket failure)" % (kz, de))
                continue
            Ad = diag_crit(b, sig, float(sgn), Aw)
            rho = Ad / Aw
            census[(kz, de)] = dict(Aw=Aw, Ad=Ad, sgn=sgn, rho=rho,
                                    sig=sig)
            print("    kz %-3d delta %.2f: A*_wall %.4e (sign %+d) "
                  "| A*_diag %s | rho_sep %s"
                  % (kz, de, Aw, sgn,
                     ("%.4e" % Ad) if math.isfinite(Ad)
                     else "INFINITY (no crossing up to 10 A*_wall)",
                     ("%.2f" % rho) if math.isfinite(rho)
                     else ">= %.0f (INF)" % DIAG_CEIL), flush=True)
    check("D2.0 bisection brackets found on every (rung, delta) "
          "cell", ok_pipe and len(census) == len(RUNGS) * len(DELTAS),
          kill="K1")
    rhos = [census[k]["rho"] for k in census]
    if any(r <= BAR_INH for r in rhos):
        sub = "DIAG-INHERITS"
    elif all(r >= BAR_SEP for r in rhos):
        sub = "DIAG-SEPARATED"
    else:
        sub = "DIAG-INTERMEDIATE"
    n_inf = sum(1 for r in rhos if not math.isfinite(r))
    check("D2.1 TYPED: rho_sep = A*_diag / A*_wall in [%s, %s] "
          "over %d cells (%d cells with NO diagonal crossing at "
          "all) -> %s (bars: separated >= %.1f everywhere, "
          "inherits <= %.1f somewhere)"
          % (("%.2f" % min(rhos)) if math.isfinite(min(rhos))
             else "INF",
             ("%.2f" % max(rhos)) if math.isfinite(max(rhos))
             else "INF", len(rhos), n_inf, sub, BAR_SEP, BAR_INH),
          True)

    section("D1 -- the two margins along the ramp (worst sign)")
    for kz in RUNGS:
        b, r0 = bases[kz]
        for de in DELTAS:
            cell = census[(kz, de)]
            Aw, sgn, sig = cell["Aw"], cell["sgn"], cell["sig"]
            print("    kz %-3d delta %.2f (A*_wall %.4e, sign %+d):"
                  % (kz, de, Aw, sgn))
            print("      %10s  %11s  %11s  %11s"
                  % ("A/A*_wall", "m_wall", "m_diag", "m_port"))
            for f in RAMP:
                r = margins_at(b, sig, float(sgn), f * Aw)
                if r is None:
                    print("      %10.2f  %11s  %11s  %11s"
                          % (f, "CHAIN-BRK", "CHAIN-BRK",
                             "CHAIN-BRK"))
                    continue
                print("      %10.2f  %+11.3e  %+11.3e  %+11.3e"
                      % (f, r["m_wall"], r["m_diag"], r["m_port"]))
    check("D1.1 two-margin ramp tables printed (report)", True)

    section("D3 -- mechanism at the wall's death point "
            "(A = A*_wall, delta = %.2f)" % DELTAS[1])
    for kz in RUNGS:
        b, r0 = bases[kz]
        cell = census[(kz, DELTAS[1])]
        Aw, sgn, sig = cell["Aw"], cell["sgn"], cell["sig"]
        rk = margins_at(b, sig, float(sgn), Aw)
        if rk is None:
            print("    kz %-3d: chain break AT the kill point "
                  "(reported)" % kz)
            continue
        T0d = dict(zip(r0["uf_n"].tolist(), r0["Tdiag"].tolist()))
        Tkd = dict(zip(rk["uf_n"].tolist(), rk["Tdiag"].tolist()))
        common = sorted(set(T0d) & set(Tkd))
        dT = {j: Tkd[j] - T0d[j] for j in common}
        moved = [j for j in common
                 if abs(dT[j]) >= 0.10 * max(T0d[j], 1e-300)]
        top = sorted(common, key=lambda j: -abs(dT[j]))[:3]
        pset = set(rk["uf_n"][rk["port"]].tolist())
        top_s = "; ".join(
            "j %d%s: %.4f -> %.4f (%+.1e)"
            % (j, " [PORT]" if j in pset else "", T0d[j], Tkd[j],
               dT[j]) for j in top)
        print("    kz %-3d: lam_max %.6f | max T %.6f (port max "
              "%.6f, argmax in port: %s) | COHERENCE SHARE "
              "lam_max - max T = %.3e | moved >= 10 pct: %d of %d "
              "common nodes (%d appear, %d vanish)"
              % (kz, rk["lam"], 1.0 - rk["m_diag"],
                 1.0 - rk["m_port"], bool(rk["port"][rk["mstar"]]),
                 rk["m_diag"] - rk["m_wall"], len(moved),
                 len(common), len(set(Tkd) - set(T0d)),
                 len(set(T0d) - set(Tkd))))
        print("      top movers: %s" % top_s, flush=True)
    check("D3.1 mechanism readout printed (report): the coherence "
          "share quantifies the off-diagonal accumulation at the "
          "kill point", True)

    section("D4 -- null ward (delta = 0)")
    b9, r9 = bases[9]
    sig0 = zero_signature(b9["M"], b9["D"], 0.0, GAMMA0)
    rn = margins_at(b9, sig0, +1.0, 1.0)
    dmax = float(np.max(np.abs(sig0)))
    dw = abs(rn["m_wall"] - r9["m_wall"]) if rn else float("inf")
    dd = abs(rn["m_diag"] - r9["m_diag"]) if rn else float("inf")
    check("D4.1 NULL WARD: delta = 0 gives max |Delta c| = %.1e "
          "== 0 EXACTLY; both margins unchanged (|d m_wall| = "
          "%.1e, |d m_diag| = %.1e, bar 1e-14)"
          % (dmax, dw, dd),
          dmax == 0.0 and dw <= 1e-14 and dd <= 1e-14, kill="K2")

    section("C -- value controls (kz 9, A = 0, both channels)")
    rr9 = core.build_window(9)
    N_E = int(math.floor(math.exp(2.0 * rr9["alpha"]))) + 1
    lamE = lambda_eps(N_E)
    nn = np.nonzero(np.abs(lamE) > 1e-12)[0]
    ctl = {"Epstein": build_lags(9, comb=(np.log(nn.astype(float)),
                                          2.0 * lamE[nn]
                                          / np.sqrt(nn.astype(float)))),
           "scramble": build_lags(9, scramble_seed=SEED_SCRAMBLE)}
    ok_ctl = True
    for nm, bc in ctl.items():
        rc = margins(bc, bc["c"])
        fired = rc is None or (rc["m_wall"] < 0.0
                               and rc["m_diag"] < 0.0)
        ok_ctl &= fired
        if rc is None:
            print("    %-8s: chain break at A = 0 (counted fired)"
                  % nm)
        else:
            print("    %-8s: m_wall %+.3e | m_diag %+.3e -- both "
                  "channels %s at A = 0"
                  % (nm, rc["m_wall"], rc["m_diag"],
                     "NEGATIVE" if fired else "NOT fired"))
    check("C.1 CONTROLS: Epstein and scramble fire on BOTH "
          "channels before any injection (the arithmetic break "
          "is already a testing violation)", ok_ctl, kill="K3")

    section("V -- FROZEN VERDICT")
    n_pass = sum(1 for _n, ok in CHECKS if ok)
    n_tot = len(CHECKS)
    if KILLS:
        VERDICT = {"K1": "PIPELINE-BROKEN",
                   "K2": "NULL-BROKEN",
                   "K3": "CONTROL-DEAD"}[KILLS[0]]
    else:
        VERDICT = "DIAGSEP-MEASURED"
    print("\n  VERDICT: %s (%s)" % (VERDICT, sub))
    print("""
  HONEST READING: rho_sep types the logical relation of two FINITE
  statements -- the wall lam_max(E_h) <= 1 and its diagonal
  (Carleson testing) half max_m E_mm <= 1 -- under the frozen
  off-critical-zero signature.  DIAG-SEPARATED: the wall dies while
  every diagonal stays below 1 -- the off-critical energy enters
  through COHERENT OFF-DIAGONAL accumulation, the testing theorem
  does not see it at the wall's kill scale, and the pointwise
  sum-rule target is a candidate for an unconditional proof.
  DIAG-INHERITS: the deployed diagonal margin is exhausted at the
  same amplitude -- the sum-rule theorem carries the same hardness
  as the wall.  NO RH claim either way; neither statement is
  claimed proved for any h.""")
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed"
          % (time.time() - T0, n_tot, n_tot - n_pass))
    return 0 if n_pass == n_tot else 1


if __name__ == "__main__":
    raise SystemExit(main())
