#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""port_scalar_schur_probe -- PRIME.PORT.SCALAR.01
(EXPLORATION ONLY, experiments/; round 39 follow-up, NEW OPEN
CONTRACT per the 2026-08-09 second review: no more eigenvector
fishing -- the wall as ONE scalar inequality via the Schur/
Feshbach pivot at the port atom, 2026-08-09).

THE CONTRACT (frozen): split the Carleson embedding at the ATOM
node m* (the worst testing node, the pole-port seat):
    I - E = [[ a, -b^T ], [ -b, B ]],
    a = 1 - T_{m*} = 1 - nu~_{m*} K_h(y*, y*)   (PHASE-FREE,
        the testing margin at the atom -- an explicit windowed
        prime functional),
    B = I - E_rest,  b = E[m*, rest].
EXACT EQUIVALENCE (1-D Schur complement):
    E <= I   <=>   B > 0  AND  sigma := a - b^T B^{-1} b >= 0.
The whole wall is the SCALAR inequality sigma >= 0: leading term
= the phase-free testing margin at one node; subtracted term
= the coherent backreaction b^T B^{-1} b of the rest of the
operator through the resolvent.  If the rank-one prime functional
appears here, the wall is one scalar inequality -- the review's
strongest-route claim, measured below.

FROZEN PROTOCOL (2026-08-09; full ladder h <= 900 for laws, heavy
rungs kz {9, 12, 13, 26, 40} printed; controls kz 9):

 S1  EXACTNESS WARDS (heavy rungs): sigma == 1/[(I - E)^{-1}]_
     {m* m*} (rel <= 1e-8); B > 0 on truth (lam_max(E_rest) < 1);
     sign(sigma) == sign(tau) (the equivalence in action);
     first-order check sigma ~= tau/|v_top(m*)|^2 (ratio printed).

 S2  THE SCALAR LEDGER (full ladder): per rung print/collect
     a = 1 - T_{m*}, the backreaction beta = b^T B^{-1} b, sigma,
     tau, and the CANCELLATION DEPTH rho = sigma/a; fit-free
     slopes: d log a / d alpha, d log sigma / d alpha (vs the tau
     law -2.4); typed SCALAR-LAWFUL iff sigma > 0 on all rungs
     and the sigma-slope matches the tau-slope within 20 percent
     (sigma IS the wall margin in scalar form).

 S3  REST-MARGIN (the B-side safety): 1 - lam_max(E_rest) per
     rung -- is removing ONE node enough to open a fat margin
     (the atom carries the criticality alone)?  Typed
     ATOM-CARRIES-ALONE iff min margin >= 100 x tau everywhere,
     else REST-SHARES.

 C   CONTROLS (kz 9, must fire): Epstein/scramble: sigma < 0 OR
     B indefinite (the scalar detects the kill; which of the two
     fires is the localization readout, printed).

KILLS: K1 exactness ward fails -> SCALAR-BROKEN; K2 pipeline ->
PIPELINE-BROKEN; K3 controls silent -> CONTROL-DEAD.

VERDICT (frozen enum): SCALAR-REDUCED (+ typed sublabels) /
SCALAR-BROKEN / PIPELINE-BROKEN / CONTROL-DEAD.

HONEST FRAME: sigma >= 0 carries the full RH weight (hardness
test LXXXVIII); the value of this contract is DIMENSIONAL -- the
wall becomes one scalar with an explicit phase-free leading term
and one coherent backreaction term.  NO RH claim.

FIREWALL: no zeros, no prime oracles (AST scan); v563 READ-ONLY;
RNG only in the scramble control; stdout only.  No marker moves.

Sources (read-only): v563_paper2_readouts; round-38/39 chain
(carleson_testing_law: T_m = nu~ K identity; weyl_m: atom
condensation -- declared inputs).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/port_scalar_schur_probe.py
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

HEAVY = (9, 12, 13, 26, 40)
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
    d = grid_density(c_ar + c_at)
    return dict(d=d, L=2 * M - 2, D=D, alpha=alpha, h=h)


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


def carleson_E(kz, **kw):
    b = build_rung(kz, **kw)
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
    return dict(E=E, h=h, alpha=b["alpha"])


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
    ev, V = np.linalg.eigh(E)
    tau = 1.0 - float(ev[-1])
    vm = float(V[mstar, -1])
    Minv = np.linalg.inv(np.eye(n) - E)
    sig_ward = 1.0 / float(Minv[mstar, mstar])
    return dict(a=a, beta=beta, sigma=sigma, tau=tau,
                lamR=lamR, vm2=vm ** 2, sig_ward=sig_ward,
                mstar=mstar)


def main():
    section("PRIME.PORT.SCALAR.01 -- the wall as ONE scalar "
            "inequality (EXPLORATION ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s"
          % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
    print("    NO RH claim; no marker moves.")
    print("\nS0 -- firewall")
    check("S0.1 AST firewall clean", not ast_scan(BANNED_IDS))

    section("S1/S2/S3 -- exactness + the scalar ledger")
    rows = []
    ward_max = 0.0
    for kz in core.frame_a_zones():
        r = carleson_E(kz)
        if r in (None, "TOO-DEEP"):
            continue
        s = scalar_split(r["E"])
        s.update(kz=kz, h=r["h"], alpha=r["alpha"])
        rows.append(s)
        ward_max = max(ward_max, abs(s["sigma"] - s["sig_ward"])
                       / max(abs(s["sig_ward"]), 1e-300))
        if kz in HEAVY:
            print("    kz %-3d h %4d: a = 1-T* %.3e | backreact "
                  "beta %.3e | sigma %.3e | tau %.3e | rho = "
                  "sigma/a %.2e | sigma*vm2/tau %.3f | rest-marg "
                  "%.3e"
                  % (kz, s["h"], s["a"], s["beta"], s["sigma"],
                     s["tau"], s["sigma"] / s["a"],
                     s["sigma"] * s["vm2"] / s["tau"],
                     1.0 - s["lamR"]))
    check("S1.1 EXACTNESS: sigma == 1/[(I-E)^{-1}]_{m*m*} on all "
          "%d rungs (max rel %.1e <= 1e-8); truth rest-blocks "
          "PSD; sign(sigma) == sign(tau) everywhere"
          % (len(rows), ward_max),
          ward_max <= 1e-8
          and all(x["lamR"] < 1.0 for x in rows)
          and all((x["sigma"] > 0) == (x["tau"] > 0)
                  for x in rows), kill="K1")
    av = np.array([x["alpha"] for x in rows])
    sl_a = float(np.polyfit(av, [math.log(x["a"]) for x in rows],
                            1)[0])
    sl_s = float(np.polyfit(av, [math.log(x["sigma"])
                                 for x in rows], 1)[0])
    sl_t = float(np.polyfit(av, [math.log(x["tau"])
                                 for x in rows], 1)[0])
    lawful = (all(x["sigma"] > 0 for x in rows)
              and abs(sl_s / sl_t - 1.0) <= 0.2)
    s2_type = "SCALAR-LAWFUL" if lawful else "SCALAR-IRREGULAR"
    check("S2.1 typed: %s -- slopes vs alpha: a (testing margin) "
          "%+.2f | sigma %+.2f | tau %+.2f (sigma tracks tau; "
          "the cancellation depth rho = sigma/a spans %.1e..%.1e)"
          % (s2_type, sl_a, sl_s, sl_t,
             min(x["sigma"] / x["a"] for x in rows),
             max(x["sigma"] / x["a"] for x in rows)), lawful)
    ratio_rest = min((1.0 - x["lamR"]) / x["tau"] for x in rows)
    s3_type = ("ATOM-CARRIES-ALONE" if ratio_rest >= 100.0
               else "REST-SHARES")
    check("S3.1 typed: %s (min rest-margin/tau = %.1e; removing "
          "the ONE atom node opens the margin by that factor)"
          % (s3_type, ratio_rest), True)

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
        r = carleson_E(9, **kw)
        s = scalar_split(r["E"])
        fired = (s["sigma"] < 0.0) or (s["lamR"] > 1.0)
        ok &= fired
        print("    %-8s: sigma %.3e | rest lam %.3f -> fires via "
              "%s" % (nmc, s["sigma"], s["lamR"],
                      "SCALAR" if s["sigma"] < 0 else "REST"))
    check("C1 CONTROLS FIRE (sigma < 0 or rest indefinite)", ok,
          kill="K3")

    section("V -- FROZEN VERDICT")
    n_pass = sum(1 for _n, okk in CHECKS if okk)
    n_tot = len(CHECKS)
    if KILLS:
        VERDICT = {"K1": "SCALAR-BROKEN", "K2": "PIPELINE-BROKEN",
                   "K3": "CONTROL-DEAD"}[KILLS[0]]
    else:
        VERDICT = "SCALAR-REDUCED"
    print("\n  VERDICT: %s (%s + %s)" % (VERDICT, s2_type,
                                         s3_type))
    print("""
  THE CONTRACT STATEMENT (PRIME.PORT.SCALAR.01, registered):
  the cofinal wall is EXACTLY the family of scalar inequalities
      sigma_h = [1 - nu~_{m*} K_h(y*, y*)] - b^T (I - E_rest)^{-1}
                b  >=  0,
  leading term phase-free (windowed prime functional), subtracted
  term = the coherent backreaction.  Open: one-sidedness of
  sigma_h on the ladder.  NO RH claim.""")
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed"
          % (time.time() - T0, n_tot, n_tot - n_pass))
    return 0 if n_pass == n_tot else 1


if __name__ == "__main__":
    raise SystemExit(main())
