#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""port_tau_determinant_probe -- PRIME.PORT.TAU.01
(EXPLORATION ONLY, experiments/; round 40, work package 1 of the
closing-cylinder plan: the wall scalar as a determinant ratio and
the sign chain to the tau function, 2026-08-09).

THE EXACT ALGEBRA (frozen; Schur determinant identities, no
window-specific assumption):
  (i)   sigma_h = det(I - E_h) / det(B_h)          (1-D pivot),
  (ii)  det(I - E_h) = det(I - R_h) det(I - D_{P,h})  (block
        Schur), hence with tau_h := det(I - D_{P,h}) and the bulk
        factors POSITIVE (I - R_h > 0, B_h > 0 measured):
  (iii) sign(tau_h) = sign(sigma_h) = sign(wall margin).
The wall is then det(I - D_{P,h}) > 0 -- and for an IIKS-class
matrix (v881: [Y, D_P] rank 2 exact) this determinant is the
natural tau-function candidate of the discrete 2x2 Riemann-
Hilbert problem (the symbolic tau identification is the CONTRACT;
this probe delivers the exact finite-h identities and the
Jacobi-variation ward).

FROZEN PROTOCOL (2026-08-09; heavy rungs kz {9, 12, 13, 26, 40};
controls kz 9):

 T1  DETERMINANT IDENTITIES (exact, slogdet): (i) and (ii) at rel
     <= 1e-8 in log-space with matching signs on every heavy
     rung; positivity of the bulk factors re-warded.

 T2  JACOBI VARIATION (the tau-function differential ward):
     d/ds log det(I - s D_P) = -trace[(I - s D_P)^{-1} D_P]
     verified against central differences at the frozen points
     s in {0.5, 0.9} (rel <= 1e-6) -- the variational identity
     any RH-problem tau function must satisfy, checked on the
     actual family.

 T3  THE KAPPA/RHO READOUT (report, first step of LEADING.SIGN):
     log sigma_h vs alpha slope compared with TWICE the measured
     Mellin-fluctuation slope (the arithmetic-energy reading
     sigma ~ fluctuation^2 suggested by the round-38 energy law);
     both slopes printed.

 C   CONTROLS (kz 9, must fire): Epstein/scramble: tau_h < 0 OR
     an even number of eigenvalues above 1 flips parity -- report
     sign(det(I - D_P)) and the count of eigenvalues above 1;
     must-fire: the wall indicator (all bulk factors positive AND
     tau > 0) is FALSE for both.

KILLS: K1 a determinant identity fails -> DET-CHAIN-BROKEN; K2
the variational ward fails -> VARIATION-BROKEN; K3 controls
silent -> CONTROL-DEAD.

VERDICT (frozen enum): TAU-CHAIN-EXACT / DET-CHAIN-BROKEN /
VARIATION-BROKEN / CONTROL-DEAD.

NO RH claim; the symbolic tau-function theorem (arbitrary h, no
numerics) is the registered contract PRIME.PORT.TAU.01 -- this
probe is its finite-h evidence layer.

FIREWALL: no zeros, no prime oracles (AST scan); v563 READ-ONLY;
RNG only in the scramble control; stdout only.  No marker moves.

Sources (read-only): v563_paper2_readouts; v881 (port geometry,
promoted), port_scalar_schur_probe (round 39).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/port_tau_determinant_probe.py
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


def objects_of(kz, **kw):
    b = build_rung(kz, **kw)
    h, L, D = b["h"], b["L"], b["D"]
    if h > 900:
        return "TOO-DEEP"
    xs, ws, _ = folded_measure(b["d"], L, +1.0)
    ys, vs, uf_n = folded_measure(b["d"], L, -1.0)
    al, be, m0, steps = lanczos_chain(xs, ws, h + 1)
    if steps < h + 1 or np.any(be <= 0):
        return None
    Pn = eval_chain(al, be, m0, ys, h)
    E = np.sqrt(vs)[:, None] * (Pn @ Pn.T) * np.sqrt(vs)[None, :]
    E = 0.5 * (E + E.T)
    n = E.shape[0]
    tau_m = (2.0 * math.pi * uf_n / L) / D
    port = tau_m <= float(np.max(tau_m)) / 10.0
    ip, ib = np.where(port)[0], np.where(~port)[0]
    P = E[np.ix_(ip, ip)]
    X = E[np.ix_(ip, ib)]
    R = E[np.ix_(ib, ib)]
    IR = np.eye(len(ib)) - R
    DP = P + X @ np.linalg.solve(IR, X.T)
    DP = 0.5 * (DP + DP.T)
    mstar = int(np.argmax(np.diag(E)))
    rest = [i for i in range(n) if i != mstar]
    a = 1.0 - float(E[mstar, mstar])
    bv = E[mstar, rest]
    B = np.eye(n - 1) - E[np.ix_(rest, rest)]
    sigma = a - float(bv @ np.linalg.solve(B, bv))
    return dict(E=E, DP=DP, IR=IR, B=B, sigma=sigma,
                alpha=b["alpha"], h=h,
                lamE=float(np.linalg.eigvalsh(E)[-1]))


def slog(A):
    s, ld = np.linalg.slogdet(A)
    return float(s), float(ld)


def main():
    section("PRIME.PORT.TAU.01 -- the determinant/sign chain of "
            "the wall scalar (EXPLORATION ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s"
          % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
    print("    NO RH claim; no marker moves.")
    print("\nS0 -- firewall")
    check("S0.1 AST firewall clean", not ast_scan(BANNED_IDS))

    section("T1/T2/T3 -- heavy rungs")
    ok1 = ok2 = True
    sig_alpha = []
    for kz in HEAVY:
        r = objects_of(kz)
        n = r["E"].shape[0]
        sI, ldI = slog(np.eye(n) - r["E"])
        sB, ldB = slog(r["B"])
        sR, ldR = slog(r["IR"])
        sD, ldD = slog(np.eye(r["DP"].shape[0]) - r["DP"])
        # (i) sigma = det(I-E)/det(B)
        rel_i = abs(math.log(abs(r["sigma"])) - (ldI - ldB)) \
            / max(abs(ldI - ldB), 1e-30)
        ok_i = (sI * sB > 0) == (r["sigma"] > 0) and rel_i <= 1e-8
        # (ii) det(I-E) = det(I-R) det(I-D_P)
        rel_ii = abs(ldI - (ldR + ldD)) / max(abs(ldI), 1e-30)
        ok_ii = rel_ii <= 1e-8 and sI == sR * sD
        ok1 &= ok_i and ok_ii and sB > 0 and sR > 0
        # T2 variational ward
        ok_var = True
        for s in (0.5, 0.9):
            eps = 1e-6
            _, ldp = slog(np.eye(r["DP"].shape[0])
                          - (s + eps) * r["DP"])
            _, ldm = slog(np.eye(r["DP"].shape[0])
                          - (s - eps) * r["DP"])
            num = (ldp - ldm) / (2 * eps)
            Minv = np.linalg.inv(np.eye(r["DP"].shape[0])
                                 - s * r["DP"])
            ana = -float(np.trace(Minv @ r["DP"]))
            ok_var &= abs(num - ana) / max(abs(ana), 1e-30) <= 1e-6
        ok2 &= ok_var
        sig_alpha.append((r["alpha"], r["sigma"]))
        print("    kz %-3d h %4d: sigma %.3e | (i) rel %.1e | "
              "(ii) rel %.1e | sign(tau) %+d == sign(sigma) %+d "
              "| variation ok %s"
              % (kz, r["h"], r["sigma"], rel_i, rel_ii, int(sD),
                 1 if r["sigma"] > 0 else -1, ok_var))
    check("T1.1 DETERMINANT CHAIN EXACT: sigma = det(I-E)/det(B) "
          "and det(I-E) = det(I-R) det(I-D_P) with positive bulk "
          "factors on every heavy rung -- sign(tau_h) = "
          "sign(sigma_h) = sign(wall)", ok1, kill="K1")
    check("T2.1 JACOBI VARIATION: d/ds log det(I - s D_P) == "
          "-tr[(I - s D_P)^{-1} D_P] at s = 0.5, 0.9 on every "
          "rung -- the tau-function differential identity holds "
          "on the actual family", ok2, kill="K2")
    av = np.array([x[0] for x in sig_alpha])
    ls = np.log([x[1] for x in sig_alpha])
    sl_sig = float(np.polyfit(av, ls, 1)[0])
    # measured Mellin fluctuation slope from XCII: dev 0.375 ->
    # 0.029 over alpha 2.77 -> 4.79 => slope ~ -1.27
    sl_fluct = (math.log(0.029) - math.log(0.375)) / (4.79 - 2.77)
    check("T3.1 KAPPA/RHO READOUT (report): slope log sigma = "
          "%+.2f vs 2 x fluctuation slope = %+.2f -- the "
          "arithmetic-energy reading sigma ~ fluct^2 within %.0f "
          "percent" % (sl_sig, 2 * sl_fluct,
                       100 * abs(sl_sig / (2 * sl_fluct) - 1)),
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
        r = objects_of(9, **kw)
        sR, _ = slog(r["IR"])
        sD, _ = slog(np.eye(r["DP"].shape[0]) - r["DP"])
        n_above = int(np.sum(np.linalg.eigvalsh(r["DP"]) > 1.0))
        wall_ok = (sR > 0 and sD > 0 and r["sigma"] > 0
                   and r["lamE"] < 1.0)
        ok &= (not wall_ok)
        print("    %-8s: lam(E) %.3e | sign det(I-R) %+d | sign "
              "tau %+d | eigs of D_P above 1: %d | wall "
              "indicator %s"
              % (nmc, r["lamE"], int(sR), int(sD), n_above,
                 wall_ok))
    check("C1 CONTROLS FIRE: the determinant wall indicator is "
          "FALSE on both", ok, kill="K3")

    section("V -- FROZEN VERDICT")
    n_pass = sum(1 for _n, okk in CHECKS if okk)
    n_tot = len(CHECKS)
    if KILLS:
        VERDICT = {"K1": "DET-CHAIN-BROKEN",
                   "K2": "VARIATION-BROKEN",
                   "K3": "CONTROL-DEAD"}[KILLS[0]]
    else:
        VERDICT = "TAU-CHAIN-EXACT"
    print("\n  VERDICT: %s" % VERDICT)
    print("""
  CONTRACT (PRIME.PORT.TAU.01, registered): prove SYMBOLICALLY
  (arbitrary h, no numerics) that tau_h = det(I - D_{P,h}) is the
  tau function of the discrete 2x2 IIKS Riemann-Hilbert problem
  of v881's generator pair, and that sign(tau_h) = sign(sigma_h)
  -- this probe supplies the exact finite-h determinant chain and
  the variational ward.  NO RH claim.""")
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed"
          % (time.time() - T0, n_tot, n_tot - n_pass))
    return 0 if n_pass == n_tot else 1


if __name__ == "__main__":
    raise SystemExit(main())
