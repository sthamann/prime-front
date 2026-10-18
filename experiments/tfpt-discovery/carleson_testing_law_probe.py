#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""carleson_testing_law_probe -- PRIME.CARLESON.TESTING.01
(EXPLORATION ONLY, experiments/; round 38 continuation, executing
the LXXXV named object (a): the port-quotient law made ANALYTIC,
2026-08-09).

THE NEW EXACT IDENTITY, DERIVED ON PAPER BEFORE THE RUN (one line
from the confluent Christoffel-Darboux formula): in the round-38
scalarization the entire p_h machinery CANCELS,
    E_mm'  =  sqrt(nu~_m nu~_m') K_h(y_m, y_m'),
    E_mm   =  nu~_m K_h(y_m, y_m),
with K_h(y, y') = sum_{k<h} p_k(y) p_k(y') the CD kernel of the
positive tilde measure.  (Proof: phi_i^2 = p_{h-1}(x_i)/(b_h
p_h'(x_i)) by confluent CD at the zeros, so g = p_{h-1}/(b_h p_h)
and the partial-fraction sums collapse; omega_m = nu~_m p_h(y_m)^2
cancels the p_h(y)^2 denominators.)  CONSEQUENCES: (i) the diagonal
of the wall operator is PHASE-FREE -- it is the classical CARLESON
TESTING quotient T_m = nu~_m K_h(y_m, y_m) = nu~_m / lambda_h(y_m)
(mass over Christoffel function); (ii) the DIAG-DOMINANT finding of
the omega run says the wall norm is carried to 93-99 percent by the
TESTING CONDITION sup_m T_m <= 1 -- the reproducing-kernel-thesis
gap rho_h = lam_max/T_max is only 1.006-1.07; (iii) the controls
break because their mass concentration violates TESTING directly.

FROZEN PROTOCOL (2026-08-09, frozen + SHA-hashed before first run):

 S1  THE IDENTITY (heavy rungs kz {9, 12, 13} + holdouts {26, 40}):
     ||E - D_nu^{1/2} K_CD D_nu^{1/2}||_F / ||E||_F <= 1e-9 with
     E built by the round-38 Cauchy-Gram route and K_CD by direct
     chain evaluation -- two independent float paths; and
     maxdiag(E) == max_m nu~_m K_h(y_m, y_m) rel <= 1e-10.

 S2  THE TESTING LAWS (full ladder, all 42 rungs h <= 900, cheap
     diagonal route: no n^2 objects):
       T_h := max_m nu~_m K_h(y_m, y_m)  (the testing constant),
       rho_h := (1 - tau_h)/T_h          (the RK-thesis gap),
     report 1 - T_h and rho_h - 1 series with fit-free log-log
     slopes vs h and vs alpha; typed dichotomies (all honest):
       TESTING-MARGIN-UNIFORM iff min(1 - T_h) >= 5e-3 and the
         log-log slope of (1 - T_h) vs h >= -0.10, else
         TESTING-MARGIN-FALLING (slope printed);
       RKTHESIS-TIGHTENING iff the log-log slope of (rho_h - 1)
         vs h <= -0.10 (the testing condition asymptotically
         carries everything), else RKTHESIS-STABLE.

 S3  THE PORT SOURCE ANATOMY (heavy rungs; the analytic half of
     the law): at the worst node m*:
       (a) ARCH SHARE: rebuild the density with the atom layer
           REMOVED (arch lags only); report share_arch =
           |d_arch(theta_m*)| / |d(theta_m*)| -- typed ARCH-CARRIED
           iff share >= 0.8 on all heavy rungs (then the testing
           numerator nu~ at the port is the analytic two-pole
           layer, and the h-law of T_h is an ARCHIMEDEAN question
           with an atom correction), else ATOM-CARRIED/MIXED;
       (b) the plateau: |d| at the first 5 negative nodes vs the
           arch-only value (the sin^2 tilde weight cancels the
           double pole -- the port mass is FINITE, report);
       (c) the kernel growth: K_h(y_m*, y_m*) values and the
           log-log slope vs h (the Christoffel side of the law).

 S4  CONTROLS (kz 9, must fire): Epstein x^2+5y^2 and scramble
     seed 1: the identity PERSISTS (algebra) while the testing
     constant fires T > 1 -- the arithmetic break is a TESTING
     violation (mass over Christoffel), now a named classical
     object.

KILLS: K1 identity breaks -> TESTING-IDENTITY-BROKEN; K2 ladder
pipeline breaks -> PIPELINE-BROKEN; K3 a control does not fire
-> CONTROL-DEAD.

VERDICT (frozen enum): TESTING-IDENTIFIED (+ typed sublabels from
S2/S3) / TESTING-IDENTITY-BROKEN / PIPELINE-BROKEN / CONTROL-DEAD.

NO RH claim.  The testing condition sup_m T_m <= 1 is NECESSARY
for the wall; DIAG-DOMINANT makes it nearly sufficient in measure;
neither is claimed proved.

SPEC v2 (honest amendment, LXXX precedent; run 1 = 3/5): the v1
frozen identity omitted the SIGN bookkeeping of the p_h
cancellation: sqrt(omega_m) = sqrt(nu~_m) |p_h(y_m)| carries the
ABSOLUTE VALUE, so the exact statement is the SIGNED congruence
    E = S (D_nu^{1/2} K_CD D_nu^{1/2}) S,   S = diag(sign p_h(y_m))
(run 1 measured: diagonal identity EXACT at 2.4e-12, full identity
off by O(1) -- precisely the missing +-1 conjugation).  S is a
source-only diagonal gauge: E and the PLAIN Carleson Gram
D_nu^{1/2} K_CD D_nu^{1/2} are orthogonally equivalent -- SAME
spectrum, same diagonal -- i.e. the off-diagonal phases of the wall
operator are PURE GAUGE at this level.  v2 checks the signed
identity; intent, kills and verdict rule UNCHANGED; the corrected
statement is STRONGER (it also identifies where the sign pattern
lives).

FIREWALL: no zeros, no prime-table oracles (AST scan); v563
READ-ONLY; RNG only inside the declared scramble control; writes
nothing but stdout.  No marker moves.

Sources (read-only): v563_paper2_readouts, the round-38 chain
(cd_pick_scalarization/omega_source_law/loewner_interlace probes),
v866/v876 (Carleson chain, heavy set), v870/v879 (tilde
convention).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/carleson_testing_law_probe.py
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
    c = c_ar + c_at
    K = core.odd_toeplitz(c, M)
    d = grid_density(c)
    d_arch = grid_density(c_ar)
    L = 2 * M - 2
    c_abs = np.real(np.fft.ifft(np.abs(d)))[:M]
    Tabs = core.odd_toeplitz(c_abs, M)
    return dict(d=d, d_arch=d_arch, K=K, Tabs=Tabs, L=L, D=D,
                alpha=alpha, h=h)


def tau_frame(b):
    Gp = 0.5 * (b["Tabs"] + b["K"])
    Gm = 0.5 * (b["Tabs"] - b["K"])
    ev, V = np.linalg.eigh(Gp)
    R = V @ np.diag(ev ** -0.5) @ V.T
    A = R @ Gm @ R
    lam = np.linalg.eigvalsh(0.5 * (A + A.T))
    return 1.0 - float(lam[-1])


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


def rung_core(kz, need_E=False, **kw):
    """Chain + testing diagnostics; E matrices only when needed."""
    b = build_rung(kz, **kw)
    h, L, D = b["h"], b["L"], b["D"]
    if h > 900:
        return "TOO-DEEP"
    xs, ws, _ = folded_measure(b["d"], L, +1.0)
    ys, vs, uf_n = folded_measure(b["d"], L, -1.0)
    al, be, m0, steps = lanczos_chain(xs, ws, h + 1)
    if steps < h + 1 or np.any(be <= 0):
        return None
    Pn = eval_chain(al, be, m0, ys, h + 1)
    Kdiag = np.sum(Pn[:, :h] ** 2, axis=1)
    T = vs * Kdiag
    mstar = int(np.argmax(T))
    tau = tau_frame(b)
    out = dict(kz=kz, h=h, alpha=b["alpha"], tau=tau,
               T=float(T[mstar]), mstar=mstar,
               Kstar=float(Kdiag[mstar]),
               rho=(1.0 - tau) / float(T[mstar]),
               theta_star=2.0 * math.pi * uf_n[mstar] / L,
               b=b, ys=ys, vs=vs, uf_n=uf_n)
    if need_E:
        J = np.diag(al[:h]) + np.diag(be[:h - 1], 1) \
            + np.diag(be[:h - 1], -1)
        bh = float(be[h - 1])
        om = vs * Pn[:, h] ** 2
        xg, Q = np.linalg.eigh(J)
        phi = Q[h - 1, :]
        Cmat = np.sqrt(om)[None, :] / (ys[None, :] - xg[:, None])
        E = (bh ** 2) * (Cmat.T @ ((phi ** 2)[:, None] * Cmat))
        E = 0.5 * (E + E.T)
        KCD = Pn[:, :h] @ Pn[:, :h].T
        S = np.sign(Pn[:, h])
        Etest = (S * np.sqrt(vs))[:, None] * KCD \
            * (S * np.sqrt(vs))[None, :]
        out["rel_id"] = float(np.linalg.norm(E - Etest)
                              / np.linalg.norm(E))
        out["rel_diag"] = float(
            abs(np.max(np.diag(E)) - out["T"])
            / max(out["T"], 1e-30))
    return out


def slope(xv, yv):
    return float(np.polyfit(xv, yv, 1)[0])


def main():
    section("PRIME.CARLESON.TESTING.01 -- the wall diagonal IS the "
            "Carleson testing condition (EXPLORATION ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s"
          % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
    print("    NO RH claim; no marker moves.")
    print("\nS0 -- firewall")
    check("S0.1 AST firewall clean (no zero/prime oracles)",
          not ast_scan(BANNED_IDS))

    section("S1 -- the identity E = D_nu^{1/2} K_CD D_nu^{1/2} "
            "(heavy rungs)")
    heavy = {}
    for kz in HEAVY:
        r = rung_core(kz, need_E=True)
        heavy[kz] = r
        print("    kz %-3d h %4d  rel_id %.1e  rel_diag %.1e  "
              "T %.6f  rho-1 %.2e"
              % (kz, r["h"], r["rel_id"], r["rel_diag"], r["T"],
                 r["rho"] - 1.0))
    check("S1.1 IDENTITY (SPEC v2, signed): E == S D_nu^{1/2} K_CD "
          "D_nu^{1/2} S with S = diag(sign p_h) on all heavy rungs "
          "(max rel %.1e <= 1e-9); maxdiag == the TESTING quotient "
          "max nu~_m K_h(y_m,y_m) (max rel %.1e <= 1e-10) -- the "
          "wall is GAUGE-EQUIVALENT to the plain Carleson Gram; "
          "diagonal PHASE-FREE and classical"
          % (max(r["rel_id"] for r in heavy.values()),
             max(r["rel_diag"] for r in heavy.values())),
          max(r["rel_id"] for r in heavy.values()) <= 1e-9
          and max(r["rel_diag"] for r in heavy.values()) <= 1e-10,
          kill="K1")

    section("S2 -- the testing laws (full ladder)")
    rows = []
    for kz in core.frame_a_zones():
        r = rung_core(kz)
        if r in (None, "TOO-DEEP"):
            if r is None:
                check("S2.0 chain short at kz %d" % kz, False,
                      kill="K2")
            continue
        rows.append(r)
    hh = np.array([r["h"] for r in rows], float)
    av = np.array([r["alpha"] for r in rows])
    Tm = np.array([r["T"] for r in rows])
    rho = np.array([r["rho"] for r in rows])
    tt = np.array([r["tau"] for r in rows])
    sl_T_h = slope(np.log(hh), np.log(1.0 - Tm))
    sl_T_a = slope(av, np.log(1.0 - Tm))
    sl_r_h = slope(np.log(hh), np.log(rho - 1.0))
    print("    1 - T_h in [%.2e, %.2e]; log-log slope vs h %+.3f; "
          "vs alpha %+.3f" % (float(np.min(1 - Tm)),
                              float(np.max(1 - Tm)), sl_T_h,
                              sl_T_a))
    print("    rho_h - 1 in [%.2e, %.2e]; log-log slope vs h %+.3f"
          % (float(np.min(rho - 1)), float(np.max(rho - 1)),
             sl_r_h))
    print("    comparison: log tau vs alpha slope %+.3f (the v866 "
          "defect law)" % slope(av, np.log(tt)))
    t_type = ("TESTING-MARGIN-UNIFORM"
              if float(np.min(1 - Tm)) >= 5e-3 and sl_T_h >= -0.10
              else "TESTING-MARGIN-FALLING")
    r_type = ("RKTHESIS-TIGHTENING" if sl_r_h <= -0.10
              else "RKTHESIS-STABLE")
    check("S2.1 typed: %s (min margin %.2e, slope %+.3f) + %s "
          "(slope %+.3f); %d rungs"
          % (t_type, float(np.min(1 - Tm)), sl_T_h, r_type,
             sl_r_h, len(rows)), len(rows) == 42, kill="K2")

    section("S3 -- the port source anatomy (heavy rungs)")
    shares = []
    for kz in HEAVY:
        r = heavy[kz]
        b, ys, vs, uf_n = r["b"], r["ys"], r["vs"], r["uf_n"]
        L = b["L"]
        j_star = int(uf_n[r["mstar"]])
        sh = abs(b["d_arch"][j_star]) / abs(b["d"][j_star])
        shares.append(sh)
        first5 = uf_n[np.argsort(uf_n)[:5]]
        dvals = "/".join("%.1f" % b["d"][int(j)] for j in first5)
        avals = "/".join("%.1f" % b["d_arch"][int(j)]
                         for j in first5)
        print("    kz %-3d worst node j %5d (theta %.4f): "
              "arch share %.3f | K* %.3e | first-5 |d| %s vs "
              "arch %s"
              % (kz, j_star, r["theta_star"], sh, r["Kstar"],
                 dvals, avals))
    hhh = np.array([heavy[kz]["h"] for kz in HEAVY], float)
    Ks = np.array([heavy[kz]["Kstar"] for kz in HEAVY])
    sl_K = slope(np.log(hhh), np.log(Ks))
    arch_type = ("ARCH-CARRIED" if min(shares) >= 0.8
                 else ("MIXED" if min(shares) >= 0.4
                       else "ATOM-CARRIED"))
    check("S3.1 typed: arch share at the worst node in [%.3f, "
          "%.3f] -> %s; Christoffel growth K_h(y*, y*) ~ h^%.2f"
          % (min(shares), max(shares), arch_type, sl_K), True)

    section("S4 -- controls (kz 9; identity persists, value fires)")
    rr9 = core.build_window(9)
    N_E = int(math.floor(math.exp(2.0 * rr9["alpha"]))) + 1
    lamE = lambda_eps(N_E)
    nn = np.nonzero(np.abs(lamE) > 1e-12)[0]
    ctl = {}
    ctl["Epstein"] = rung_core(9, need_E=True,
                               comb=(np.log(nn.astype(float)),
                                     2.0 * lamE[nn]
                                     / np.sqrt(nn.astype(float))))
    ctl["scramble"] = rung_core(9, need_E=True, scramble_seed=1)
    for nm, c in ctl.items():
        print("    %-8s: T %.3e (rel_id %.1e) -- the break IS a "
              "testing violation" % (nm, c["T"], c["rel_id"]))
    check("S4.1 CONTROLS: identity persists (max rel %.1e <= "
          "1e-6) and the testing constant fires T > 1 on both"
          % max(c["rel_id"] for c in ctl.values()),
          max(c["rel_id"] for c in ctl.values()) <= 1e-6
          and all(c["T"] > 1.0 for c in ctl.values()), kill="K3")

    section("V -- FROZEN VERDICT")
    n_pass = sum(1 for _n, ok in CHECKS if ok)
    n_tot = len(CHECKS)
    if KILLS:
        VERDICT = {"K1": "TESTING-IDENTITY-BROKEN",
                   "K2": "PIPELINE-BROKEN",
                   "K3": "CONTROL-DEAD"}[KILLS[0]]
    else:
        VERDICT = "TESTING-IDENTIFIED"
    print("\n  VERDICT: %s (%s + %s + %s)"
          % (VERDICT, t_type, r_type, arch_type))
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed"
          % (time.time() - T0, n_tot, n_tot - n_pass))
    return 0 if n_pass == n_tot else 1


if __name__ == "__main__":
    raise SystemExit(main())
