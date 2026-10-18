#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""v883 -- PRIME.PORT.TAU.01 (finite-h determinant chain, executed) + PRIME.PORT.LATTICE.PARAMETRIX.01 (DECIDED: FLUCTUATIONS-REQUIRED) + PRIME.PORT.LATTICE.PARAMETRIX.02 (zone refinement DECIDED: BOTH-REQUIRED): the determinant/sign chain to the tau function and the GLOBAL RIGIDITY of the Euler-product comb, ONE module from three probes (5/5 + 3/3 + 3/3 checks, zero fails, verdicts TAU-CHAIN-EXACT + PARAMETRIX-MEASURED (FLUCTUATIONS-REQUIRED) + ZONES-MEASURED (BOTH-REQUIRED); discovery probes port_tau_determinant_probe.py, lattice_parametrix_probe.py, edge_bulk_smoothing_probe.py, 2026-08-09, re-run identically at promotion, embedded BYTE-EXACT and executed verbatim).  (1) THE TAU CHAIN (round-40 work package 1, finite-h level): the Schur determinant identities sigma_h = det(I-E)/det(B) and det(I-E) = det(I-R) det(I-D_P) are MACHINE-EXACT (rel <= 4.8e-13 in log space) with positive bulk factors on all heavy rungs, hence sign(tau_h) = sign(sigma_h) = the sign of the wall with tau_h := det(I - D_{P,h}); the Jacobi variational identity d/ds log det(I - s D_P) = -tr[(I - s D_P)^{-1} D_P] holds on the true family (s = 0.5/0.9, rel <= 1e-6) -- the differential identity every RH-problem tau function must satisfy; controls: the determinant wall indicator (bulk positive AND tau > 0) is FALSE on both Epstein and scramble; the kappa/rho readout (first LEADING.SIGN step): slope(log sigma) = -2.93 vs twice the Mellin fluctuation slope -2.53 -- the arithmetic energy reading sigma ~ fluctuation^2 within 16 percent.  THE SYMBOLIC CONTRACT stays registered (PRIME.PORT.TAU.01 [O]): tau_h = the tau function of the discrete 2x2 IIKS Riemann-Hilbert problem of the v881 generators, for arbitrary h without numerics.  (2) THE PARAMETRIX DECISION (round-40 work package 2): four worlds through the IDENTICAL pencil pipeline on every heavy rung -- A (true comb: masses 2 Lambda(n)/sqrt(n) at u = log n): tau_A = +1.7e-4 .. +6.7e-7 warded positive; B1 (prime-power lattice, fully smooth quadrature masses 2 e^{u/2} du): tau_B1 = -78 .. -1706; B2 (lattice, LOCAL +-1/2-log-unit mass sums preserved EXACTLY, in-window fluctuations killed): tau_B2 = -78 .. -5537; C (fine continuum): tau_C = -0.11 .. -1.26 warded negative -- LATTICE-WITH-SMOOTH-MASSES IS ORDERS OF MAGNITUDE WORSE THAN FULL SMOOTHING; even exact local PNT mass on the true lattice breaks the floor violently: not the positions alone but the EXACT Lambda-mass-position pairing (the multiplicative Euler-product structure) carries the positivity -- the naive parametrix design (Mellin-Cauchy + lattice, Lambda perturbative) is DEAD; the main parametrix of any RH analysis must carry the full von Mangoldt comb.  (3) THE ZONE REFINEMENT (both zones load-bearing): B2-style local-average smoothing ONLY in the edge zone (u > U - 1, ~40-44 percent of the mass) kills the floor (tau_Z1 = -3.7 .. -22.1), ONLY in the interior kills harder (tau_Z2 = -77 .. -7551), globally kills (ward), truth positive (ward) on all five heavy rungs: THE EULER-PRODUCT PAIRING IS GLOBALLY RIGID -- there is no 'only the last log unit is non-perturbative' shortcut; together with (2) every smoothing-based parametrix construction is dead, and the small parameters live exclusively in the flow/deformation direction (ladder with a better order; isomonodromy/tau; s-deformation) -- the design constraint that routes v885.  CONTROLS fire on the value throughout (Epstein/scramble negative floors; smooth worlds warded negative); the identities persist (algebra).  NO RH claim; no marker moves.  Float64 on the deployed v563 machinery; no zeros, no prime-table oracles (AST firewalls inside the probes); no RNG outside declared controls.  Python-only per GATE.WOLFRAM.02.

PROVENANCE: discovery probes port_tau_determinant_probe.py (5/5,
TAU-CHAIN-EXACT), lattice_parametrix_probe.py (3/3,
PARAMETRIX-MEASURED (FLUCTUATIONS-REQUIRED)),
edge_bulk_smoothing_probe.py (3/3, ZONES-MEASURED (BOTH-REQUIRED)),
all 2026-08-09, re-run identically at promotion.  ROUND-31 EMBEDDING
CONVENTION: frozen sources embedded BYTE-EXACT, executed verbatim in
isolated namespaces; printed spec SHAs reproduce; byte-equality ward
vs experiments/tfpt-discovery/ inside the pattern gates.  All probes
consume the READ-ONLY deployed core v563_paper2_readouts.py.

FIREWALL: no zeros, no prime-table oracles; heavy rungs declared in
the frozen headers; NO RH claim.
"""

import contextlib
import io
import os
import re
import sys
import time
import types

_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)

# ------------- frozen probe source port_tau_determinant_probe (embedded BYTE-EXACT, raw string)
_SRC_0 = r'''
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
'''

# ------------- frozen probe source lattice_parametrix_probe (embedded BYTE-EXACT, raw string)
_SRC_1 = r'''
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""lattice_parametrix_probe -- PRIME.PORT.LATTICE.PARAMETRIX.01
(EXPLORATION ONLY, experiments/; round 40, work package 2 of the
closing-cylinder plan: WHICH part of the prime discreteness must
live in the Riemann-Hilbert main parametrix?, 2026-08-09).

CONTEXT: the smooth continuum dr-model VIOLATES the floor
(MODEL-SUPERCRITICAL, tau_model = -1.26 -> -0.11): the prime
discreteness rescues positivity.  But 'discreteness' has two
separable parts: (P) the POSITIONS (the prime-power lattice
{log n}) and (M) the MASSES (the actual Lambda(n) values with
their fluctuations).  The parametrix design question: does the
main problem need only the lattice with SMOOTH masses (then the
Lambda-fluctuations are the perturbative remainder -- the ideal
case), or the actual masses too?

THE THREE-PLUS-ONE WORLDS (frozen; identical pipeline, pencil
floor tau for each):
  A   TRUE:      masses 2 Lambda(n)/sqrt(n) at u_n = log n
                 (tau_A > 0, known);
  B1  LATTICE-SMOOTH: prime-power positions, fully smooth
                 quadrature masses m_n = 2 e^{u_n/2} du_n
                 (midpoint cells) -- NO Lambda information at all;
  B2  LOCAL-AVERAGE: B1 masses rescaled per +-1/2 log-unit window
                 to preserve the TRUE local mass sums -- kills
                 in-window Lambda fluctuations, keeps local PNT
                 mass exactly;
  C   CONTINUUM: fine D/8 grid (tau_C < 0, known -- re-warded).

TYPED OUTCOMES (the deliverable):
  LATTICE-SUFFICIENT      iff tau_B1 > 0 on every heavy rung
    (the parametrix = Mellin-Cauchy + bare prime-power lattice;
    Lambda entirely perturbative -- the ideal case);
  LOCAL-MASS-REQUIRED     iff tau_B1 < 0 somewhere but tau_B2 > 0
    everywhere (the parametrix needs the local PNT mass on the
    lattice; only in-window fluctuations perturbative);
  FLUCTUATIONS-REQUIRED   iff tau_B2 < 0 somewhere (the actual
    Lambda values are load-bearing -- the parametrix must carry
    them; the remainder split must be finer).

 C1  CONTROLS/WARDS: tau_A > 0 and tau_C < 0 re-warded on every
     heavy rung (the two known anchors of the dichotomy).

KILLS: K1 pipeline breaks -> PIPELINE-BROKEN; K2 an anchor ward
fails -> ANCHOR-BROKEN.

VERDICT (frozen enum): PARAMETRIX-MEASURED (+ typed outcome) /
PIPELINE-BROKEN / ANCHOR-BROKEN.

NO RH claim.  Firewall: no zeros, no prime oracles (AST scan; the
worlds are built from the deployed tables and deterministic
transforms); v563 READ-ONLY; no RNG; stdout only.

Sources (read-only): v563_paper2_readouts; mellin_model_operator
probe (round 39, the continuum anchor), v882 (source law).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/lattice_parametrix_probe.py
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


def floor_of(c, M):
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


def cell_widths(uu):
    du = np.zeros(len(uu))
    du[1:-1] = 0.5 * (uu[2:] - uu[:-2])
    du[0] = uu[1] - uu[0]
    du[-1] = uu[-1] - uu[-2]
    return du


def main():
    section("PRIME.PORT.LATTICE.PARAMETRIX.01 -- which "
            "discreteness must the parametrix carry? "
            "(EXPLORATION ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s"
          % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
    print("    NO RH claim; deterministic worlds; no marker "
          "moves.")
    print("\nS0 -- firewall")
    check("S0.1 AST firewall clean", not ast_scan(BANNED_IDS))

    section("W -- the four worlds (heavy rungs)")
    okA = okC = True
    b1_signs, b2_signs = [], []
    for kz in HEAVY:
        rr = core.build_window(kz)
        h, M, D, alpha = rr["h"], rr["M"], rr["D"], rr["alpha"]
        uu = np.asarray(rr["uu"], float)
        mm = 2.0 * np.asarray(rr["lam"], float)
        c_ar = np.asarray(core.arch_lags(M, D), float)

        def tau_of(pos, mass):
            c_at, _ = core.atom_lags_at(alpha, M, pos, mass)
            return floor_of(c_ar + np.asarray(c_at, float), M)

        tau_A = tau_of(uu, mm)
        du = cell_widths(uu)
        m_b1 = 2.0 * np.exp(uu / 2.0) * du
        tau_B1 = tau_of(uu, m_b1)
        # B2: rescale B1 masses to preserve true local sums
        m_b2 = m_b1.copy()
        for i in range(len(uu)):
            w = np.abs(uu - uu[i]) <= 0.5
            s_true = float(np.sum(mm[w]))
            s_b1 = float(np.sum(m_b1[w]))
            m_b2[i] = m_b1[i] * (s_true / s_b1 if s_b1 > 0
                                 else 1.0)
        tau_B2 = tau_of(uu, m_b2)
        U = float(np.max(uu))
        dug = D / 8.0
        ug = np.arange(dug / 2.0, U, dug)
        tau_C = tau_of(ug, 2.0 * np.exp(ug / 2.0) * dug)
        okA &= (tau_A is not None and tau_A > 0)
        okC &= (tau_C is not None and tau_C < 0)
        b1_signs.append(tau_B1)
        b2_signs.append(tau_B2)
        print("    kz %-3d h %4d: tau_A %+0.3e | tau_B1(lattice-"
              "smooth) %+0.3e | tau_B2(local-avg) %+0.3e | tau_C"
              "(continuum) %+0.3e"
              % (kz, h, tau_A, tau_B1, tau_B2, tau_C))
    check("C1 ANCHOR WARDS: tau_A > 0 and tau_C < 0 on every "
          "heavy rung", okA and okC, kill="K2")
    if all(t is not None and t > 0 for t in b1_signs):
        outcome = "LATTICE-SUFFICIENT"
    elif all(t is not None and t > 0 for t in b2_signs):
        outcome = "LOCAL-MASS-REQUIRED"
    else:
        outcome = "FLUCTUATIONS-REQUIRED"
    check("W.1 typed: %s -- %s"
          % (outcome,
             "the parametrix = Mellin-Cauchy + bare prime-power "
             "lattice; Lambda entirely perturbative (ideal case)"
             if outcome == "LATTICE-SUFFICIENT" else
             "the parametrix needs the local PNT mass on the "
             "lattice; in-window fluctuations perturbative"
             if outcome == "LOCAL-MASS-REQUIRED" else
             "the actual Lambda values are load-bearing; the "
             "remainder split must be finer than mass-smoothing"),
          True)

    section("V -- FROZEN VERDICT")
    n_pass = sum(1 for _n, okk in CHECKS if okk)
    n_tot = len(CHECKS)
    VERDICT = ("ANCHOR-BROKEN" if KILLS else
               "PARAMETRIX-MEASURED")
    print("\n  VERDICT: %s (%s)" % (VERDICT, outcome))
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed"
          % (time.time() - T0, n_tot, n_tot - n_pass))
    return 0 if n_pass == n_tot else 1


if __name__ == "__main__":
    raise SystemExit(main())
'''

# ------------- frozen probe source edge_bulk_smoothing_probe (embedded BYTE-EXACT, raw string)
_SRC_2 = r'''
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""edge_bulk_smoothing_probe -- PRIME.PORT.LATTICE.PARAMETRIX.02
(EXPLORATION ONLY, experiments/; round 40, work package 4: WHERE
are the Lambda fluctuations load-bearing -- the edge zone (last
log unit, 39 percent of the mass) or the interior?, 2026-08-09).

CONTEXT: lattice_parametrix_probe (XCVI) decided FLUCTUATIONS-
REQUIRED with GLOBAL mass smoothing.  This refinement smooths
ZONE-WISE (B2-style local-average masses preserving +-1/2
log-unit sums, the mildest smoothing that kills fluctuations):
  A    TRUE comb                          (tau_A > 0, ward);
  Z1   edge-only smoothing  (u > U - 1)   -- interior exact;
  Z2   interior-only smoothing (u <= U-1) -- edge exact;
  Z3   GLOBAL smoothing                   (= XCVI B2, ward < 0).

TYPED OUTCOMES: EDGE-CARRIES iff Z1 breaks (tau < 0) while Z2
survives on every heavy rung (the non-perturbative core is the
last log unit -- a massive simplification of the parametrix);
INTERIOR-CARRIES iff the reverse; BOTH-REQUIRED iff both break;
NEITHER (both survive) would contradict XCVI and fire a kill.

KILLS: K1 pipeline breaks -> PIPELINE-BROKEN; K2 ward fails
(tau_A <= 0 or Z3 >= 0 somewhere) -> ANCHOR-BROKEN; K3 both
zones survive -> XCVI-CONTRADICTION.

VERDICT (frozen enum): ZONES-MEASURED (+ typed outcome) /
PIPELINE-BROKEN / ANCHOR-BROKEN / XCVI-CONTRADICTION.

NO RH claim.  Firewall: no zeros, no prime oracles (AST scan);
deterministic transforms of the deployed tables; v563 READ-ONLY;
no RNG; stdout only.

Sources (read-only): v563_paper2_readouts;
lattice_parametrix_probe (XCVI, declared input).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/edge_bulk_smoothing_probe.py
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


def floor_of(c, M):
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


def cell_widths(uu):
    du = np.zeros(len(uu))
    du[1:-1] = 0.5 * (uu[2:] - uu[:-2])
    du[0] = uu[1] - uu[0]
    du[-1] = uu[-1] - uu[-2]
    return du


def smoothed_masses(uu, mm, zone_mask):
    """B2-style local-average masses inside the zone, exact
    outside: quadrature shape rescaled to preserve +-1/2 log-unit
    TRUE mass sums, applied only where zone_mask holds."""
    du = cell_widths(uu)
    m_shape = 2.0 * np.exp(uu / 2.0) * du
    out = mm.copy()
    for i in np.where(zone_mask)[0]:
        w = (np.abs(uu - uu[i]) <= 0.5) & zone_mask
        s_true = float(np.sum(mm[w]))
        s_shape = float(np.sum(m_shape[w]))
        out[i] = m_shape[i] * (s_true / s_shape
                               if s_shape > 0 else 1.0)
    return out


def main():
    section("PRIME.PORT.LATTICE.PARAMETRIX.02 -- edge vs bulk "
            "smoothing (EXPLORATION ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s"
          % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
    print("    NO RH claim; deterministic; no marker moves.")
    print("\nS0 -- firewall")
    check("S0.1 AST firewall clean", not ast_scan(BANNED_IDS))

    section("Z -- the zone worlds (heavy rungs)")
    okA = okZ3 = True
    z1_all, z2_all = [], []
    for kz in HEAVY:
        rr = core.build_window(kz)
        h, M, D, alpha = rr["h"], rr["M"], rr["D"], rr["alpha"]
        uu = np.asarray(rr["uu"], float)
        mm = 2.0 * np.asarray(rr["lam"], float)
        c_ar = np.asarray(core.arch_lags(M, D), float)
        U = float(np.max(uu))

        def tau_of(mass):
            c_at, _ = core.atom_lags_at(alpha, M, uu, mass)
            return floor_of(c_ar + np.asarray(c_at, float), M)

        edge = uu > U - 1.0
        tau_A = tau_of(mm)
        tau_Z1 = tau_of(smoothed_masses(uu, mm, edge))
        tau_Z2 = tau_of(smoothed_masses(uu, mm, ~edge))
        tau_Z3 = tau_of(smoothed_masses(
            uu, mm, np.ones(len(uu), bool)))
        okA &= (tau_A is not None and tau_A > 0)
        okZ3 &= (tau_Z3 is not None and tau_Z3 < 0)
        z1_all.append(tau_Z1)
        z2_all.append(tau_Z2)
        print("    kz %-3d h %4d (edge mass %.2f): tau_A %+0.3e "
              "| Z1 edge-smoothed %+0.3e | Z2 interior-smoothed "
              "%+0.3e | Z3 global %+0.3e"
              % (kz, h, float(np.sum(mm[edge]) / np.sum(mm)),
                 tau_A, tau_Z1, tau_Z2, tau_Z3))
    check("C1 ANCHOR WARDS: tau_A > 0 and tau_Z3 < 0 on every "
          "heavy rung", okA and okZ3, kill="K2")
    z1_pos = all(t is not None and t > 0 for t in z1_all)
    z2_pos = all(t is not None and t > 0 for t in z2_all)
    if z1_pos and z2_pos:
        outcome = "XCVI-CONTRADICTION"
    elif (not z1_pos) and z2_pos:
        outcome = "EDGE-CARRIES"
    elif z1_pos and (not z2_pos):
        outcome = "INTERIOR-CARRIES"
    else:
        outcome = "BOTH-REQUIRED"
    check("Z.1 typed: %s -- %s"
          % (outcome,
             "the non-perturbative core is the LAST LOG UNIT; "
             "interior Lambda fluctuations are perturbative (a "
             "massive parametrix simplification)"
             if outcome == "EDGE-CARRIES" else
             "the interior carries; the edge is perturbative"
             if outcome == "INTERIOR-CARRIES" else
             "both zones' fluctuations are load-bearing -- the "
             "Euler-product pairing is globally rigid"
             if outcome == "BOTH-REQUIRED" else
             "inspect: contradicts XCVI"),
          outcome != "XCVI-CONTRADICTION", kill="K3")

    section("V -- FROZEN VERDICT")
    n_pass = sum(1 for _n, okk in CHECKS if okk)
    n_tot = len(CHECKS)
    if KILLS:
        VERDICT = {"K1": "PIPELINE-BROKEN", "K2": "ANCHOR-BROKEN",
                   "K3": "XCVI-CONTRADICTION"}[KILLS[0]]
    else:
        VERDICT = "ZONES-MEASURED"
    print("\n  VERDICT: %s (%s)" % (VERDICT, outcome))
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed"
          % (time.time() - T0, n_tot, n_tot - n_pass))
    return 0 if n_pass == n_tot else 1


if __name__ == "__main__":
    raise SystemExit(main())
'''

# --------------------------------------------------------------- harness
_PF_RE = re.compile(r"^\s*\[(PASS|FAIL)\]\s+(\S+)", re.M)
_VD_RE = re.compile(r"VERDICT[:\]]")


def _probe_file(name):
    cand = os.path.abspath(os.path.join(
        _HERE, os.pardir, "experiments", "tfpt-discovery", name + ".py"))
    return cand if os.path.isfile(cand) else None


def _census(out):
    marks = _PF_RE.findall(out)
    fails = sorted({tok for st, tok in marks if st == "FAIL"})
    verdict = ""
    for line in out.splitlines():
        if _VD_RE.search(line):
            verdict = line.strip()
    return len(marks), fails, verdict


def _exec_probe(name, src, run_entry=True):
    """Execute one embedded frozen probe source BYTE-EXACT in its own
    module namespace (round-31 convention); capture and re-emit
    stdout; return (stdout, exit_code, byte_equal_or_None)."""
    if src[:1] == "\n":
        src = src[1:]
    path = _probe_file(name)
    same = None
    if path is not None:
        with open(path, encoding="utf-8") as fh:
            same = (fh.read() == src)
    fname = path or os.path.abspath(__file__)
    mod = types.ModuleType(name)
    mod.__file__ = fname
    sys.modules[name] = mod
    buf = io.StringIO()
    code = 0
    with contextlib.redirect_stdout(buf):
        try:
            exec(compile(src, fname, "exec"), mod.__dict__)
            entry = mod.__dict__.get("main") or mod.__dict__.get("run")
            if run_entry and callable(entry):
                rc = entry()
                code = 0 if rc is None else int(rc)
        except SystemExit as exc:
            code = 0 if exc.code is None else int(exc.code)
        except Exception:                            # regression guard
            import traceback
            traceback.print_exc(file=sys.stdout)
            code = 99
    out = buf.getvalue()
    sys.stdout.write(out)
    sys.stdout.flush()
    return out, code, same


def _gate(name, out, code, same, exp_n, exp_fails, exp_verdict,
          exp_code, gates):
    n, fails, verdict = _census(out)
    ok = (n == exp_n and fails == list(exp_fails)
          and exp_verdict in verdict and code == exp_code
          and same is not False)
    gates.append(ok)
    prov = ("byte-exact vs experiments source" if same is True else
            "embedded copy (source file not present)" if same is None
            else "SOURCE MISMATCH")
    print("\n[%s] PATTERN GATE %s: %d checks (exp %d) | FAILs %s "
          "(exp %s) | exit %d (exp %d) | %s\n      verdict line: %s"
          % ("PASS" if ok else "FAIL", name, n, exp_n,
             ",".join(fails) if fails else "none",
             ",".join(exp_fails) if exp_fails else "none",
             code, exp_code, prov, verdict), flush=True)
    return ok


_PLAN = (
    ('port_tau_determinant_probe', _SRC_0, 5, (), 'TAU-CHAIN-EXACT', 0),
    ('lattice_parametrix_probe', _SRC_1, 3, (), 'PARAMETRIX-MEASURED', 0),
    ('edge_bulk_smoothing_probe', _SRC_2, 3, (), 'ZONES-MEASURED', 0),
)


def run():
    t0 = time.time()
    print("=" * 74)
    print('v883 -- PRIME.PORT.TAU.01 (finite-h chain executed) + PRIME.PORT.LATTICE.PARAMETRIX.01/.02 (DECIDED): the determinant chain to the tau function and the global rigidity of the Euler-product comb')
    print("(frozen probes embedded byte-exact and executed verbatim; NO RH claim)")
    print("=" * 74, flush=True)
    gates = []
    for name, src, exp_n, exp_fails, exp_verdict, exp_code in _PLAN:
        print("\n" + "-" * 74)
        print("EMBEDDED FROZEN PROBE: %s" % name)
        print("-" * 74, flush=True)
        out, code, same = _exec_probe(name, src)
        _gate(name, out, code, same, exp_n, exp_fails,
              exp_verdict, exp_code, gates)
    ok = all(gates)
    print("\n" + "=" * 74)
    print("v883: %d/%d pattern gates passed | runtime %.1f s"
          % (sum(gates), len(gates), time.time() - t0))
    print('the sign chain sign(tau_h) = sign(sigma_h) = the wall is machine-exact; every smoothing-based parametrix is dead')
    print("[%s] v883 VERDICT GATE" % ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(run())
