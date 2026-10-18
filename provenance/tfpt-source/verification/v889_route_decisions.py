#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""v889 -- PRIME.PORT.DIAGSEP.01 + PRIME.CASE.ZONESPLIT.01 + PRIME.CASE.PNTGAMMA.01 + PRIME.CASE.SIGNEDHOMOTOPY.01: THE FOUR ROUTE-DECIDING MEASUREMENTS OF THE SUM-RULE PROGRAM, ONE module from four probes (8/8 + 12/12 + 10/10 + 12/12 checks, zero fails, verdicts DIAGSEP-MEASURED (DIAG-INTERMEDIATE) + ZONESPLIT-MEASURED (ZONE-FROZEN(theta*=0.700) / OUTLIERS-DANGEROUS / INSIDE-LAW=c/log^2) + PNTGAMMA-MEASURED (PNT-INSUFFICIENT / DOMINANT=INT(+)) + HOMOTOPY-MEASURED (HOMOTOPY-INDEFINITE-ARITHMETIC / KERNEL-NSD on both M4 rungs); discovery probes diagonal_separation_probe.py, christoffel_zone_envelope_probe.py (SPEC v2), christoffel_pnt_gamma_probe.py (SPEC v2), signed_homotopy_probe.py (SPEC v2), rounds 42-44, 2026-08-09, re-run identically at promotion, embedded BYTE-EXACT and executed verbatim, ~6.5 min).  (1) THE WALL DIES OFF-DIAGONALLY (diagsep, the strategy memo's decisive logic test): under the frozen off-critical injection Delta c = A cos(gamma0 tau)(cosh(delta tau) - 1) (generic frozen frequency, NO zeros; built-in null at delta = 0 warded EXACTLY at 0), the wall ALWAYS dies first -- separation ratio rho_sep = A*_diag/A*_wall in [1.99, INF] over the 10 (rung, delta) cells: rho ~ 2.0-2.7 on the shallow heavy rungs and NO diagonal crossing AT ALL up to 10 x A*_wall on the deep rungs kz 26/40 (rho >= 10, four INFINITY cells) -- typed DIAG-INTERMEDIATE per the frozen bars (DIAG-SEPARATED needed rho >= 3 on every cell, DIAG-INHERITS needed rho <= 1.5 somewhere; neither fires), with the separation GROWING with depth, i.e. the deep direction where the analytic theorem must live is the separated one; at the wall's death point EVERY diagonal testing entry stays below 1 (max T_m 0.94-0.99, coherence share lam_max - max_m T_m = 1.1e-2..6.3e-2): 100 percent of the wall's death is coherent off-diagonal accumulation, never a diagonal violation, so the pointwise Carleson testing theorem does not inherit the wall's kill scale at depth and stays a candidate for analytic investment (it does NOT make the wall unconditional -- typed in the frozen spec).  (2) THE CRITICAL ZONE FREEZES AT theta* = 0.700 (zone envelope): on all 42 reachable rungs the outside testing margin eta_out(h, theta) = min over deployed neg nodes with a > h^(2 theta) of (1 - T_m) is uniformly positive at the frozen grid theta* = 0.700 with deep-half infimum +0.0214 (>= the 0.02 bar), cut-stable under one-alias moves, and sharp (0.667 fails); typed sublabels honest: OUTLIERS-DANGEROUS (the bulk density-oscillation defects can coincide with margin minimizers -- the H1-style tools carry margin risk) and INSIDE-LAW=c/log^2 (the inside envelope the arithmetic input must beat).  (3) PNT IS INSUFFICIENT (pnt gamma, the decider): the four matched worlds (truth / PNT-smooth closed-form reference / mask-actual / mass-actual, identical pipeline, partition identity self-tested at 1e-12) show the smooth reference gap min gamma^(2) NEGATIVE on every rung (-0.96 at kz 9 to -7.8e-3 at the deepest kz 116, h = 1433) -- the smooth PNT world VIOLATES the port testing margin everywhere, so no classical zero-free-region-strength input can close H5 by smooth comparison; the decomposition types the dominant rescue piece INT(+) -- the MASK-MASS INTERACTION, neither the support pattern nor the mass fluctuation alone -- and the frozen decision branch fires PNT-INSUFFICIENT (envelope fit typed UNRESOLVED per freeze on the nonpositive gap).  (4) THE HOMOTOPY KERNEL IS INDEFINITE-ARITHMETIC (signed homotopy, the route-decider): along the exact PNT-to-truth interpolation d_t = d_PNT + t r the signed homotopy identity (lambda_1 - nu_1) - (lambda_0 - nu_0) = Int_0^1 J dt is exact calculus (heavy rungs warded at rel <= 1e-8 across ALL exact rational mask-crossing times; deep rungs piecewise + pointwise-FD warded per the v2 amendment); the classification comes out HOMOTOPY-INDEFINITE-ARITHMETIC: some endpoint gaps Delta_m <= 0, the fixed-chamber quadratic kernel is KERNEL-NSD on both frozen M4 rungs kz 9 and kz 40 (exactly the concavity-predicted outcome), and the fixed-mask first variation is not positive everywhere -- the positivity of the truth endpoint is carried by the SIGNED FIRST-ORDER alignment of the arithmetic residual with the extremal-polynomial weights, i.e. the diagonal route's required input is PAIR-CORRELATION CLASS, not any PSD kernel positivity.  NET ROUTE DECISION (the module's content): invest in the separated diagonal theorem inside the frozen zone, with an arithmetic (pair-correlation-class) input replacing the dead smooth comparison; the off-diagonal coherence half stays with the port/positivity contracts.  NO RH claim; no marker moves; nothing here proves a bound, a rate, or uniformity in h.  Float64 on the deployed v563 machinery (READ-ONLY); no zeros, no prime oracles (AST firewalls inside the probes); RNG only in declared scramble controls.  Python-only per GATE.WOLFRAM.02.

PROVENANCE: discovery probes diagonal_separation_probe.py (8/8,
DIAGSEP-MEASURED (DIAG-INTERMEDIATE)), christoffel_zone_envelope_
probe.py (12/12, ZONESPLIT-MEASURED, SPEC v2: two transparency
fixes on record, no number or bar moved, theta* = 0.700 unchanged),
christoffel_pnt_gamma_probe.py (10/10, PNTGAMMA-MEASURED, SPEC v2:
alias-cap disclosure, n/a display on nonpositive reference gaps,
descriptive addendum -- every typed first-run outcome unchanged),
signed_homotopy_probe.py (12/12, HOMOTOPY-MEASURED, SPEC v2:
endpoint evaluation scale added to the deep ward denominator plus
the strengthened pointwise FD ward, fail-first diagnosis on
record), all 2026-08-09, re-run identically at promotion.
ROUND-31 EMBEDDING CONVENTION: frozen sources embedded BYTE-EXACT,
executed verbatim in isolated namespaces; printed spec SHAs
reproduce; byte-equality ward vs experiments/tfpt-discovery/
inside the pattern gates.  All probes consume the READ-ONLY
deployed core v563_paper2_readouts.py.

FIREWALL: no zeros, no prime-table oracles; heavy/deep rungs and
all bars declared in the frozen headers; all fail-first spec
amendments preserved.  NO RH claim.
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

# ------------- frozen probe source diagonal_separation_probe (embedded BYTE-EXACT, raw string)
_SRC_0 = r'''
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
'''

# ------------- frozen probe source christoffel_zone_envelope_probe (embedded BYTE-EXACT, raw string)
_SRC_1 = r'''
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""christoffel_zone_envelope_probe -- PRIME.CASE.ZONESPLIT.01
(EXPLORATION ONLY, experiments/; round 43: freeze the smallest valid
critical-zone exponent theta for the repaired Christoffel domination
theorem, 2026-08-09).

CONTEXT (machinery verbatim from christoffel_hypotheses_probe /
freetail_case_bridge_probe): the deployed tilde-measures carry atoms
nu~_m at neg nodes y_m; T_m = nu~_m K_h(y_m, y_m); the port scale is
a_m = 2 h^2 (1 - y_m).  The repaired theorem splits the band into a
critical zone C_h = {a <= h^(2 theta)} -- inside which all measured
criticality lives -- and its complement, on which the testing margin
1 - T_m must stay uniformly positive.  Measured margin minimizers
sit at a = 89..3754 (kz 26 at a = 3754 ~ h^1.40, i.e. theta ~ 0.70
there); the strategy memo proposes theta = 3/4 as the frozen safety
split.  This probe measures the outside envelope on ALL 42 reachable
rungs and freezes the smallest grid theta that confines the
difficulty.

THE LADDER (frozen, verbatim from certified_ladder_probe):
core.frame_a_zones() restricted to h <= 900 -- the 42 reachable
rungs (h 142..878), sorted by (h, kz); the deep half = the 21
highest-h rungs.

FROZEN PROTOCOL (2026-08-09; constants frozen before the first run:
theta grid {0.50, 0.60, 2/3, 0.70, 0.75, 0.80}; deep-half margin
bar 0.02; cut-stability tolerance 30 %; materiality factor 1/2;
alias index = rank inward from x = +1 in a-ascending order; H1
oscillation constants verbatim A_h = 20 two-sided, C = 2, 33
samples, top-3; heavy rungs kz {9, 12, 13, 26, 40}; Z4 fit split
leave-last-third-out 28/14 by ascending h; control kz 9 scramble
seed 1 at the memo cut theta = 3/4):

 Z1  ENVELOPE TABLE: eta_out(h, theta) = min over deployed neg
     nodes with a_m > h^(2 theta) of (1 - T_m), plus the minimizing
     alias m*(h, theta); the full 42 x 6 table (compact), and per
     theta the inf over the deep half and the inf over all rungs.

 Z2  FREEZE DECISION (typed): theta* = the smallest grid theta with
     (i)   inf over the deep half of eta_out(theta) >= 0.02,
     (ii)  cut stability: moving the cut by ONE alias in both
           directions (the outside set starts one node earlier /
           later in a-order, per rung) keeps the deep-half inf the
           same sign and within 30 % of the base value,
     (iii) sharpness: the next-smaller grid theta FAILS (i) or has
           materially less deep-half margin (< 1/2 of the
           candidate's); vacuously true at the grid minimum 0.50.
     Typed ZONE-FROZEN(theta*) with the numbers.  ZONE-OPEN iff no
     grid theta (even 0.80) passes (i), or none passes (i)+(ii)
     (the difficulty is not confinable STABLY at any tested
     exponent -- honest).  If the three-criteria set is empty while
     (i)+(ii) holds somewhere, freeze the smallest theta passing
     (i)+(ii) and print the (iii) plateau flag honestly (the grid
     does not resolve sharpness).

 Z3  OUTLIER SEPARATION (the H1/H2 question): per heavy rung the
     top-3 bulk oscillation nodes (oscillation of log w_h over
     I_h(x), verbatim H1: two-sided bulk min(1 -+ x) >= A_h/h^2,
     C = 2, 33 samples) vs the margin minimizer m*(h, theta_Z3);
     typed OUTLIERS-HARMLESS iff the two node sets are disjoint on
     EVERY heavy rung (the density defects are measure-zero for the
     margin -- the H1/H2 failures are the wrong tool, not theorem
     killers), else OUTLIERS-DANGEROUS (they coincide somewhere --
     the defects DO carry margin risk).  theta_Z3 = theta* if
     frozen, else the memo 3/4 (for the record).

 Z4  MARGIN LAW INSIDE (report): inside C_h(theta_Z3) the min
     margin per rung eta^C_h = min_{a <= h^(2 theta)} (1 - T_m);
     the h-trend (shallow/deep pair medians), and envelope fits
     eta^C_h ~ c, c/log h, c/log^2 h, c h^-p -- trained on the 28
     lowest-h rungs, scored by held-out RMSE on the 14 deepest
     (leave-last-third-out); the power law needs positive train
     margins (else typed n/a).  This eta^C_h is the quantity the
     arithmetic input must beat; report which envelope fits best.

 C   CONTROLS (kz 9, scramble seed 1): the scrambled window must
     drive eta_out(theta = 3/4) NEGATIVE (value control) while the
     pipeline persists (chain completes).

FROZEN CONCRETIZATIONS (pre-registered with the protocol, before
the first run):
  (i)   alias index m = 1, 2, ... = neg nodes ranked by a ascending
        (m = 1 closest to x = +1), extending the port-alias
        numbering of christoffel_hypotheses_probe to all nodes.
  (ii)  an empty outside set (cut above max a) would print n/a and
        be excluded from the infs; it cannot occur on this ladder
        (max a ~ 4 h^2 >> h^1.6 for all h <= 900).
  (iii) Z2 (iii) is vacuous at the grid minimum 0.50 (no smaller
        grid point exists).
  (iv)  Z3/Z4 run at the memo theta = 3/4 when Z2 types ZONE-OPEN,
        purely for the record; the typed labels stand either way.
  (v)   all Z1/Z2 infs are over the FULL deployed neg node set
        (bulk AND the -1 edge); no bulk restriction -- the envelope
        is the honest two-edge quantity the theorem needs.

KILLS: pipeline breaks (wrong rung count, chain short on any rung,
non-finite T or margins, heavy rung missing from the ladder) ->
PIPELINE-BROKEN; control silent -> CONTROL-DEAD.  The Z2/Z3/Z4
labels are MEASUREMENTS, never kills: ZONE-OPEN or
OUTLIERS-DANGEROUS is a finding.

VERDICT (frozen enum): ZONESPLIT-MEASURED (+ typed sublabels
ZONE-FROZEN(theta*) / ZONE-OPEN, OUTLIERS-HARMLESS /
OUTLIERS-DANGEROUS, INSIDE-LAW=<c | c/log | c/log^2 | c*h^-p |
n/a>) / PIPELINE-BROKEN / CONTROL-DEAD.

SPEC AMENDMENTS (fail-first history preserved):
  v1 (2026-08-09): initial freeze, everything above.
  v2 (2026-08-09, after the first run -- which already returned
     ZONE-FROZEN(0.700) + OUTLIERS-DANGEROUS + INSIDE-LAW=c/log^2
     with all checks green): two transparency fixes, neither moves
     a number or a bar: (a) a dead pre-assignment in the Z1 table
     loop removed (the global minimum was always read from the
     suffix structure); (b) Z2 criterion (ii) is now EVALUATED
     independently of (i) so the per-theta table prints the honest
     stability status of every grid point (v1 gated (ii) on (i),
     printing "fail" for thetas whose cut was in fact stable).  The
     freeze rule itself is unchanged (theta* still needs all three
     criteria), and theta* = 0.700 is unchanged.

NO RH claim: eta_out and eta^C_h are measured finite-h envelopes of
the deployed v563 window family; a frozen theta* is a zone split
for the finite ladder, not a proof of the domination theorem, and
no marker moves.

FIREWALL: no zeros, no prime oracles (AST scan: zetazero, nzeros,
primerange, isprime, primepi, nextprime, prevprime); v563
READ-ONLY; RNG only in the scramble control; stdout only.

Sources (read-only): v563_paper2_readouts; christoffel_hypotheses_
probe (chain + free-tail density machinery, verbatim), declared
inputs.

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/christoffel_zone_envelope_probe.py
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

H_LADDER_MAX = 900             # reachable-rung cap (the 42 rungs)
N_RUNGS_EXP = 42               # frozen expected rung count
HEAVY = (9, 12, 13, 26, 40)    # heavy rungs (Z3 + context)
THETAS = (0.50, 0.60, 2.0 / 3.0, 0.70, 0.75, 0.80)
MARGIN_BAR = 0.02              # Z2 (i): deep-half inf bar
STAB_REL = 0.30                # Z2 (ii): 30 % cut-shift tolerance
HALF_FACTOR = 0.5              # Z2 (iii): materiality factor
THETA_MEMO = 0.75              # the memo split (control + fallback)
A_H = 20.0                     # H1 bulk cut (two-sided), verbatim
C_OSC = 2.0                    # H1 interval half-width factor
N_OSC = 33                     # H1 samples per interval
TOP_K = 3                      # Z3 top oscillation nodes per rung
N_TRAIN = 28                   # Z4 leave-last-third-out split
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


# ------------------------------------------------------------------ pipeline
# (grid density, folded arm measures, Lanczos chain, CD kernel, free-tail
#  m-function: verbatim from christoffel_hypotheses_probe)

def grid_density(c):
    c = np.asarray(c, float)
    a = np.concatenate([c, c[-2:0:-1]])
    d = np.fft.fft(a)
    assert float(np.max(np.abs(d.imag))) <= 1e-9 * max(
        1.0, float(np.max(np.abs(d.real))))
    return d.real


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


def build_rung(kz, scramble_seed=None):
    """Window -> pos/neg folded measures -> chain -> CD diagonal + T."""
    rr = core.build_window(kz, scramble_seed=scramble_seed)
    h, M, D, alpha = rr["h"], rr["M"], rr["D"], rr["alpha"]
    uu = np.asarray(rr["uu"], float)
    mm = 2.0 * np.asarray(rr["lam"], float)
    c_at, _ = core.atom_lags_at(alpha, M, uu, mm)
    c_ar = np.asarray(core.arch_lags(M, D), float)
    d = grid_density(c_ar + np.asarray(c_at, float))
    L = 2 * M - 2
    xs, ws, _ = folded_measure(d, L, +1.0)
    ys, vs, _ = folded_measure(d, L, -1.0)
    al, be, m0, steps = lanczos_chain(xs, ws, h + 1)
    if steps < h + 1:
        return None
    Pn = eval_chain(al, be, m0, ys, h)
    Kdiag = np.sum(Pn ** 2, axis=1)
    T = vs * Kdiag
    return dict(kz=kz, h=h, L=L, xs=xs, ws=ws, ys=ys, vs=vs,
                m0=m0, Kdiag=Kdiag, T=T,
                A2=2.0 * be[:h], B2=2.0 * al[:h])


def m_strip(A2, B2v, E):
    """Exact m-function of J_h^ft on the essential spectrum: free
    boundary value + coefficient stripping (Herglotz-preserving)."""
    m = 0.5 * (-E + 1j * np.sqrt(4.0 - E * E))
    for k in range(len(A2) - 1, -1, -1):
        m = 1.0 / (B2v[k] - E - (A2[k] ** 2) * m)
    return m


def w_ft(r, x):
    """The exact free-tail ac density w_h at x (any shape)."""
    E = np.clip(2.0 * np.asarray(x, float), -2.0 + 1e-15, 2.0 - 1e-15)
    return 2.0 * r["m0"] * m_strip(r["A2"], r["B2"], E).imag / math.pi


# ------------------------------------------------------- zone machinery
def ladder_zones():
    """The 42 reachable rungs: frame_a_zones with h <= H_LADDER_MAX
    (h from the same closed formula frame_a_zones uses)."""
    out = []
    for kz in core.frame_a_zones():
        D_k = 0.5 * float(core.G_ALL[kz]) / float(core.NU_MAIN)
        M_k = int(math.ceil(float(core.U_ALL[kz]) / D_k - 1.0e-9)) + 1
        if M_k % 2:
            M_k += 1
        if M_k // 2 <= H_LADDER_MAX:
            out.append(kz)
    return out


def zone_scan(r):
    """a-ascending order + suffix/prefix minima of the margin, so
    every cut position is answered in O(1)."""
    h = r["h"]
    a = 2.0 * h * h * (1.0 - r["ys"])
    o = np.argsort(a, kind="stable")
    a_s = a[o]
    marg = 1.0 - r["T"][o]
    n = len(a_s)
    suf = np.empty(n + 1)
    sufi = np.empty(n + 1, dtype=int)
    suf[n] = np.inf
    sufi[n] = -1
    for j in range(n - 1, -1, -1):
        if marg[j] <= suf[j + 1]:
            suf[j], sufi[j] = marg[j], j
        else:
            suf[j], sufi[j] = suf[j + 1], sufi[j + 1]
    pre = np.empty(n)
    prei = np.empty(n, dtype=int)
    best, bi = np.inf, -1
    for j in range(n):
        if marg[j] < best:
            best, bi = marg[j], j
        pre[j], prei[j] = best, bi
    r.update(a_s=a_s, marg_s=marg, order=o, suf=suf, sufi=sufi,
             pre=pre, prei=prei, n_neg=n)


def cut_index(r, theta):
    """First a-ascending index OUTSIDE the zone {a <= h^(2 theta)}."""
    return int(np.searchsorted(r["a_s"], r["h"] ** (2.0 * theta),
                               side="right"))


def eta_out(r, theta, shift=0):
    """(eta_out, alias m*, global neg index) at the (shifted) cut."""
    j = min(max(cut_index(r, theta) + shift, 0), r["n_neg"])
    if j >= r["n_neg"]:
        return float("inf"), -1, -1
    ji = int(r["sufi"][j])
    return float(r["suf"][j]), ji + 1, int(r["order"][ji])


def eta_in(r, theta):
    """(eta^C_h, alias, a at the minimizer) inside the zone."""
    j = cut_index(r, theta)
    if j == 0:
        return None
    ji = int(r["prei"][j - 1])
    return float(r["pre"][j - 1]), ji + 1, float(r["a_s"][ji])


def top_osc_nodes(r):
    """Verbatim H1: top-K bulk oscillation nodes of log w_h over
    I_h(x) (two-sided bulk, C = C_OSC, N_OSC samples)."""
    h = r["h"]
    bulk = np.minimum(1.0 - r["ys"], 1.0 + r["ys"]) >= A_H / h ** 2
    bi = np.nonzero(bulk)[0]
    yb = r["ys"][bi]
    dx = C_OSC * (np.sqrt(1.0 - yb ** 2) / h + 1.0 / h ** 2)
    tt = np.linspace(-1.0, 1.0, N_OSC)
    pts = np.clip(yb[:, None] + dx[:, None] * tt[None, :],
                  -1.0 + 1e-15, 1.0 - 1e-15)
    lw = np.log(np.maximum(w_ft(r, pts.ravel()), 1e-300))
    lw = lw.reshape(pts.shape)
    osc = lw.max(axis=1) - lw.min(axis=1)
    top = bi[np.argsort(-osc)[:TOP_K]]
    return top, osc[np.argsort(-osc)[:TOP_K]]


def fit_envelopes(hs, ys):
    """Z4: four candidate envelopes, leave-last-third-out."""
    hs = np.asarray(hs, float)
    ys = np.asarray(ys, float)
    out = {}
    regs = (("c", np.ones_like(hs)),
            ("c/log", 1.0 / np.log(hs)),
            ("c/log^2", 1.0 / np.log(hs) ** 2))
    for name, reg in regs:
        c = float(np.sum(ys[:N_TRAIN] * reg[:N_TRAIN])
                  / np.sum(reg[:N_TRAIN] ** 2))
        rmse = float(np.sqrt(np.mean(
            (ys[N_TRAIN:] - c * reg[N_TRAIN:]) ** 2)))
        out[name] = ("c=%.5f" % c, rmse)
    if np.all(ys[:N_TRAIN] > 0.0):
        A = np.vstack([np.ones(N_TRAIN), -np.log(hs[:N_TRAIN])]).T
        sol, *_ = np.linalg.lstsq(A, np.log(ys[:N_TRAIN]),
                                  rcond=None)
        c, p = math.exp(float(sol[0])), float(sol[1])
        rmse = float(np.sqrt(np.mean(
            (ys[N_TRAIN:] - c * hs[N_TRAIN:] ** (-p)) ** 2)))
        out["c*h^-p"] = ("c=%.5f p=%.3f" % (c, p), rmse)
    else:
        out["c*h^-p"] = ("n/a (nonpositive train margin)", None)
    return out


def main():
    section("PRIME.CASE.ZONESPLIT.01 -- critical-zone envelope + "
            "freeze of theta (EXPLORATION ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s"
          % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
    print("    NO RH claim; no marker moves.")
    print("\nS0 -- firewall")
    check("S0.1 AST firewall clean", not ast_scan(BANNED_IDS))

    section("B0 -- the ladder (all reachable rungs, h <= %d)"
            % H_LADDER_MAX)
    zones = ladder_zones()
    check("B0.1 frozen rung count: %d reachable rungs" % N_RUNGS_EXP,
          len(zones) == N_RUNGS_EXP, "found %d" % len(zones),
          kill="PIPELINE")
    check("B0.2 heavy rungs on the ladder",
          all(kz in zones for kz in HEAVY), kill="PIPELINE")
    if "PIPELINE" in KILLS:
        return finish(None, None, None, None)
    R = []
    ok = True
    fin = True
    for kz in zones:
        r = build_rung(kz)
        ok &= r is not None
        if r is None:
            print("    kz %-3d: CHAIN SHORT" % kz, flush=True)
            continue
        fin &= bool(np.all(np.isfinite(r["T"])))
        zone_scan(r)
        R.append(r)
    R.sort(key=lambda r: (r["h"], r["kz"]))
    check("B0.3 all %d chains complete" % len(zones), ok,
          kill="PIPELINE")
    check("B0.4 all T finite", fin, kill="PIPELINE")
    if "PIPELINE" in KILLS:
        return finish(None, None, None, None)
    deep = R[N_RUNGS_EXP // 2:]
    print("    h range %d..%d; deep half = %d rungs (h >= %d); "
          "[%.1f s]" % (R[0]["h"], R[-1]["h"], len(deep),
                        deep[0]["h"], time.time() - T0))

    # ---------------------------------------------------------- Z1
    section("Z1 -- THE ENVELOPE TABLE eta_out(h, theta) = min over "
            "{a > h^(2 theta)} of (1 - T), with minimizing alias")
    th_lab = ["%.3f" % th for th in THETAS]
    print("\n    kz   h    glob-min(1-T)@a      "
          + " ".join("th=%s      " % s for s in th_lab))
    table = {th: [] for th in THETAS}
    for r in R:
        # global min = suffix min at j = 0 (all nodes outside)
        g_eta = float(r["suf"][0])
        g_a = float(r["a_s"][int(r["sufi"][0])])
        cells = []
        for th in THETAS:
            e, m_star, _gi = eta_out(r, th)
            table[th].append(e)
            cells.append("%+.3f/%-5d" % (e, m_star))
        print("    %-4d %-4d %+.4f@%-10.1f " % (r["kz"], r["h"],
                                                g_eta, g_a)
              + " ".join(cells), flush=True)
    print("\n    per theta:  inf(all 42)   inf(deep half)")
    inf_all = {}
    inf_deep = {}
    for th in THETAS:
        inf_all[th] = min(table[th])
        inf_deep[th] = min(table[th][N_RUNGS_EXP // 2:])
        print("      theta=%.3f  %+.4f       %+.4f"
              % (th, inf_all[th], inf_deep[th]))
    check("Z1.1 envelope table complete (finite where the outside "
          "set is nonempty)",
          all(np.isfinite(v) for v in inf_all.values()),
          kill="PIPELINE")

    # ---------------------------------------------------------- Z2
    section("Z2 -- FREEZE DECISION: smallest theta with (i) deep "
            "inf >= %.2f, (ii) cut-stable 30%%, (iii) sharp"
            % MARGIN_BAR)
    rows = {}
    for idx, th in enumerate(THETAS):
        base = inf_deep[th]
        e_min = min(eta_out(r, th, shift=-1)[0] for r in deep)
        e_plu = min(eta_out(r, th, shift=+1)[0] for r in deep)
        c1 = base >= MARGIN_BAR
        same_sign = ((base > 0.0) == (e_min > 0.0)
                     and (base > 0.0) == (e_plu > 0.0))
        c2 = (same_sign
              and abs(e_min - base) <= STAB_REL * abs(base)
              and abs(e_plu - base) <= STAB_REL * abs(base))
        if idx == 0:
            c3 = True                       # vacuous at grid minimum
        else:
            prev = inf_deep[THETAS[idx - 1]]
            c3 = (prev < MARGIN_BAR) or (prev < HALF_FACTOR * base)
        rows[th] = (base, e_min, e_plu, c1, c2, c3)
        print("    theta=%.3f: deep inf %+.4f | cut-1 %+.4f cut+1 "
              "%+.4f | (i)%s (ii)%s (iii)%s"
              % (th, base, e_min, e_plu,
                 "PASS" if c1 else "fail",
                 "PASS" if c2 else "fail",
                 "PASS" if c3 else "fail"), flush=True)
    full = [th for th in THETAS if all(rows[th][3:6])]
    stab = [th for th in THETAS if rows[th][3] and rows[th][4]]
    plateau = False
    if full:
        theta_star = full[0]
    elif stab:
        theta_star = stab[0]
        plateau = True
        print("    (iii) PLATEAU: no grid theta is sharp; frozen at "
              "the smallest theta passing (i)+(ii) -- the grid does "
              "not resolve sharpness (concretization, honest).")
    else:
        theta_star = None
    if theta_star is not None:
        b, em, ep, *_ = rows[theta_star]
        zone_label = "ZONE-FROZEN(theta*=%.3f)" % theta_star
        print("\n    FROZEN: theta* = %.3f  (deep inf %+.4f >= "
              "%.2f; cut shifts %+.4f/%+.4f within %.0f%%; %s)"
              % (theta_star, b, MARGIN_BAR, em, ep,
                 100 * STAB_REL,
                 "(iii) plateau-flagged" if plateau else
                 "next-smaller theta fails/half"))
    else:
        zone_label = "ZONE-OPEN"
        print("\n    ZONE-OPEN: no grid theta (even 0.80) passes "
              "(i)+(ii) -- the difficulty is not confinable at any "
              "tested exponent (honest).")
    check("Z2.1 typed: %s" % zone_label, True)
    theta_z3 = theta_star if theta_star is not None else THETA_MEMO

    # ---------------------------------------------------------- Z3
    section("Z3 -- OUTLIER SEPARATION: H1 top-%d oscillation nodes "
            "vs the margin minimizer at theta=%.3f (heavy rungs)"
            % (TOP_K, theta_z3))
    harmless = True
    for r in R:
        if r["kz"] not in HEAVY:
            continue
        top, oscv = top_osc_nodes(r)
        h = r["h"]
        _e, m_star, gi = eta_out(r, theta_z3)
        a_min = 2.0 * h * h * (1.0 - r["ys"][gi])
        a_top = 2.0 * h * h * (1.0 - r["ys"][top])
        clash = gi in set(int(t) for t in top)
        harmless &= not clash
        print("    kz %-3d h %4d: osc top-%d nodes a = %s (osc %s)"
              % (r["kz"], h, TOP_K,
                 " ".join("%.1f" % v for v in a_top),
                 " ".join("%.2f" % v for v in oscv)))
        print("                 margin minimizer m*=%d at a = %.1f "
              "(1-y = %.3e) -> %s"
              % (m_star, a_min, 1.0 - r["ys"][gi],
                 "CLASH" if clash else "disjoint"), flush=True)
    out_label = ("OUTLIERS-HARMLESS" if harmless
                 else "OUTLIERS-DANGEROUS")
    check("Z3.1 typed: %s (oscillation sups vs margin minimizers)"
          % out_label, True)

    # ---------------------------------------------------------- Z4
    section("Z4 -- MARGIN LAW INSIDE C_h(theta=%.3f): eta^C_h = "
            "min_{a <= h^(2 theta)} (1 - T)" % theta_z3)
    hs, es = [], []
    ok_z4 = True
    for r in R:
        v = eta_in(r, theta_z3)
        ok_z4 &= v is not None
        if v is None:
            print("    kz %-3d h %4d: EMPTY ZONE" % (r["kz"], r["h"]))
            continue
        e, m_star, a_at = v
        hs.append(r["h"])
        es.append(e)
        print("    kz %-3d h %4d: eta^C_h %+.5f at alias %-4d "
              "(a = %.1f)" % (r["kz"], r["h"], e, m_star, a_at),
              flush=True)
    check("Z4.0 inside zone nonempty on every rung", ok_z4,
          kill="PIPELINE")
    law_label = "n/a"
    if ok_z4:
        sh = float(np.median(es[:2]))
        dp = float(np.median(es[-2:]))
        print("\n    h-trend: shallow-pair median %+.5f -> deep-pair "
              "median %+.5f (%s)"
              % (sh, dp, "shrinking" if dp < sh else
                 "non-shrinking"))
        fits = fit_envelopes(hs, es)
        best, best_rmse = None, None
        for name in ("c", "c/log", "c/log^2", "c*h^-p"):
            par, rmse = fits[name]
            print("    fit %-8s: %-22s held-out RMSE %s"
                  % (name, par,
                     "%.5f" % rmse if rmse is not None else "n/a"))
            if rmse is not None and (best_rmse is None
                                     or rmse < best_rmse):
                best, best_rmse = name, rmse
        law_label = best if best is not None else "n/a"
        print("    best envelope (leave-last-third-out): %s"
              % law_label)
    check("Z4.1 typed: INSIDE-LAW=%s (the quantity the arithmetic "
          "input must beat)" % law_label, True)

    # ------------------------------------------------------------ C
    section("C -- controls (kz 9, scramble seed 1): eta_out at the "
            "memo cut theta = %.2f must flip negative" % THETA_MEMO)
    rs = build_rung(9, scramble_seed=1)
    if not check("C0 scramble chain completes (pipeline persists)",
                 rs is not None, kill="PIPELINE"):
        return finish(zone_label, out_label, law_label, None)
    zone_scan(rs)
    e_s, m_s, _ = eta_out(rs, THETA_MEMO)
    r9 = next(r for r in R if r["kz"] == 9)
    e_r, _m, _ = eta_out(r9, THETA_MEMO)
    print("    scramble eta_out(%.2f) = %+.4f at alias %d "
          "(real kz 9: %+.4f) -> %s"
          % (THETA_MEMO, e_s, m_s, e_r,
             "FIRES" if e_s < 0.0 else "silent"), flush=True)
    ctrl = "eta_out<0" if e_s < 0.0 else None
    check("C1 CONTROL FIRES: scrambled eta_out negative",
          e_s < 0.0, kill="CONTROL")
    return finish(zone_label, out_label, law_label, ctrl)


def finish(zone_label, out_label, law_label, ctrl):
    section("V -- FROZEN VERDICT")
    n_pass = sum(1 for _n, okk in CHECKS if okk)
    n_tot = len(CHECKS)
    if "PIPELINE" in KILLS:
        VERDICT = "PIPELINE-BROKEN"
    elif "CONTROL" in KILLS:
        VERDICT = "CONTROL-DEAD"
    else:
        VERDICT = "ZONESPLIT-MEASURED"
    sub = []
    if zone_label:
        sub.append(zone_label)
    if out_label:
        sub.append(out_label)
    if law_label:
        sub.append("INSIDE-LAW=%s" % law_label)
    if ctrl:
        sub.append("CONTROL=%s" % ctrl)
    print("\n  VERDICT: %s%s" % (VERDICT,
                                 (" (%s)" % " + ".join(sub))
                                 if sub else ""))
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed"
          % (time.time() - T0, n_tot, n_tot - n_pass))
    return 0 if n_pass == n_tot else 1


if __name__ == "__main__":
    raise SystemExit(main())
'''

# ------------- frozen probe source christoffel_pnt_gamma_probe (embedded BYTE-EXACT, raw string)
_SRC_2 = r'''
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""christoffel_pnt_gamma_probe -- PRIME.CASE.PNTGAMMA.01
(EXPLORATION ONLY, experiments/; round 43: THE DECIDER for the
repaired sum-rule theorem -- is the one-sided Christoffel correction
gamma PNT-LEVEL (H5 closes on classical zero-free-region strength,
strictly weaker than RH) or not?  2026-08-09.)

CONTEXT (machinery verbatim from christoffel_hypotheses_probe /
freetail_case_bridge_probe): the deployed window kz carries atoms at
u_n = log n (prime powers, deployed von Mangoldt table), masses
mu_n = 2 Lambda(n)/sqrt(n), entering through tent-tapered window lags
(T115 assembly) -> grid density -> folded pos/neg measures -> Lanczos
chain -> CD kernel K_h; lambda_h(y) = 1/K_h(y, y); the neg atoms are
the tilde-masses nu~_m.  H7 (round 42) measured gamma_{h,m} =
(lambda_h - nu~_m)/Lambda^ref > 0 on all port aliases but shrinking
(min 5.9e-2 -> 1.07e-2 at kz 40).  THIS probe decides where that
correction lives: in the smooth PNT world, in the prime-power MASK
(support pattern), in the arithmetic MASS fluctuation (Lambda - 1),
or in their interaction.

FROZEN PROTOCOL (2026-08-09; constants frozen before the first
measurement run):

 THE FOUR MATCHED WORLDS (identical pipeline through lags ->
 measures -> CD kernel -> Christoffel; only the atom lag block c_at
 changes; the archimedean lags, the grid (M, D, L), the fold and the
 chain length h+1 are identical per rung):
   W1 TRUTH   : atoms (u_n, mu_n) via the deployed tent assembly.
   W2 PNT-SMOOTH (the full reference rho^0): the continuum PNT
      density 2 e^{u/2} du on u in [0, 2 alpha] (the smooth image of
      sum 2 Lambda(n) n^{-1/2} f(log n) under psi(x) ~ x, x in
      [1, X = e^{2 alpha}]) deposited on the SAME tent-tapered lag
      grid by the CLOSED-FORM integrals c^0[i] =
      -(1/2) Int tent_i(u) 2 e^{u/2} du, tent_i(u) =
      max(0, 1 - |iD - u|/D), plus the i = 0 reflection (the u < D
      mirror term of the deployed assembly, integrated exactly);
      primitive Int (A + B u) 2 e^{u/2} du = 4 e^{u/2} (A + B(u-2)).
   CELLS: b_0 = 0, b_j = (u_j + u_{j+1})/2 (j = 1..ka-1), b_ka =
      2 alpha; smooth cell mass m0_j = 4 (e^{b_j/2} - e^{b_{j-1}/2})
      (the exact rho^0 mass of atom j's Voronoi cell).
   W3 MASK ACTUAL, MASS SMOOTH: atoms at the ACTUAL positions u_n
      carrying the SMOOTH cell masses m0_n (tent assembly verbatim).
   W4 MASS ACTUAL, MASK SMOOTH: the piecewise density
      (mu_j / m0_j) 2 e^{u/2} du on cell j (actual cell masses,
      smooth profile; closed form per cell x tent piece).  With
      mu_j = m0_j for all j, W4 == W2 EXACTLY (partition identity,
      self-tested to 1e-12) and W3 == W1 by construction.

 RUNGS: heavy kz {9, 12, 13, 26, 40} + the deepest 3 REACHABLE =
   the frame-A zones with COMPLETE deployed atom table on the window
   (X = e^{2 alpha} <= ATOM_MAX = 4e5; the zones kz 142/177/243
   violate this -- their truth world is table-truncated and the
   comparison would be contaminated), sorted by (h desc, kz asc),
   top 3 not already heavy: kz 116 (h 1433), kz 90 (h 1430), kz 88
   (h 1393; tied with kz 121 at h 1393, tie broken by smaller kz).
   Pre-sizing (zone table + one chain timing) disclosed below.

 G1 PER WORLD r AND PORT ALIAS m <= h^{3/4}/pi (N_al =
   floor(h^{3/4}/pi); aliases = that world's N_al neg nodes closest
   to x = +1, RANK-PAIRED across worlds by closeness order; alias
   positions printed so misalignment is visible): the exact discrete
   Christoffel lambda^{(r)}_m = 1/K_h^{(r)}(y_m, y_m), the target
   mass nu^{(r)}_m (that world's neg atom), and gamma^{(r)}_{h,m} =
   (lambda^{(r)}_m - nu^{(r)}_m) / Lambda^0_m with Lambda^0_m =
   lambda^{(2)}_m (the W2 Christoffel at ITS m-th alias -- the
   common reference; so gamma^{(2)}_m = 1 - T^{(2)}_m exactly).
   Print the four gamma profiles per rung (first 8 aliases + min +
   median over all N_al).

 G2 THE DECOMPOSITION: gamma^{(1)} - gamma^{(2)} = (MASK:
   gamma^{(3)} - gamma^{(2)}) + (MASS: gamma^{(4)} - gamma^{(2)})
   + (INTERACTION: remainder), evaluated per rung at m* =
   argmin_m gamma^{(1)}_m and as medians over aliases.  Dominant
   piece = largest |.| at m*; the cross-rung answer = the majority
   dominant over the deep half (the 4 largest-h rungs) + its sign.

 G3 THE ENVELOPE FIT (typed): y(h) = min_m gamma^{(2)} against the
   candidates c / c/log X / c/(log X)^2 / c h^{-p} (log X = 2 alpha
   per rung), least squares in log space; TRAIN on the 5 smallest-h
   rungs, PREDICT the 3 largest (leave-last-third-out); winner =
   min test RMSE; DISCRIMINATION honest: RESOLVED only if the
   runner-up test RMSE >= 1.25x the winner's, else UNRESOLVED
   (eight points); any y <= 0 -> UNRESOLVED (reason printed).

 G4 THE VK PROPAGATION (the rigorous half, measured): per W2 port
   alias the Christoffel MINIMIZER p*_m(x) = K^{(2)}(x, y_m) /
   K^{(2)}(y_m, y_m) (coefficients P^{(2)}_k(y_m)/K^{(2)}(y_m,y_m)
   in the W2 orthonormal chain); eps_m = |Int p*^2 d(mu^{(1)} -
   rho^0)| / Int p*^2 d rho^0 with Int p*^2 d rho^0 = lambda^{(2)}_m
   EXACTLY (orthonormality; recomputed numerically as a pipeline
   check <= 1e-8) and Int p*^2 d mu^{(1)} = the W1 pos-measure
   quadratic form; eps_A^exact(h) = max_m eps_m.  TYPED against
   min gamma^{(2)} on the deep half (4 largest-h rungs), ratio_r =
   eps_A(r) / min gamma^{(2)}(r):
     PNT-CLOSES       iff every deep ratio <= 0.5 AND the deep
                      ratio trend does not cross (last <= first);
     PNT-INSUFFICIENT iff any deep ratio >= 1.0 OR any deep
                      min gamma^{(2)} <= 0;
     UNRESOLVED       otherwise.
   HONEST FENCE: this replaces the analytic Vinogradov-Korobov
   bound by the MEASURED arithmetic deviation on the deployed
   window; the analytic closure additionally needs the VK-to-eps_A
   lemma (an unconditional |psi(x) - x| bound propagated through
   the same finite Gram comparison) -- NOT proved here, and the
   textbook explicit bounds do not apply at our tiny X.

 C  CONTROLS (kz 9, scramble seed 1, mirroring the deployed
   scramble: positions uniform on (0, 2 alpha), SAME masses):
   (value control) the scrambled-truth gamma at the port must flip
   sign (min_m gamma^{scr} <= 0 against the real W2 reference);
   (persistence) the four-world pipeline + the scramble chain all
   complete with finite outputs.  Value control silent ->
   CONTROL-DEAD.

 SELF-TESTS (S0, kill PIPELINE on failure): (i) closed-form W2
   lags vs 64-pt Gauss-Legendre quadrature per tent piece on kz 9
   (rel sup <= 1e-10); (ii) W4 with unit scales == W2 (partition
   identity, rel sup <= 1e-12); (iii) AST firewall clean.

KILLS: chain short / non-finite Christoffels / self-test failure /
alias sets empty -> PIPELINE-BROKEN; value control silent ->
CONTROL-DEAD.  G1..G4 outcomes are MEASUREMENTS, never kills.

VERDICT (frozen enum): PNTGAMMA-MEASURED (+ typed decision
PNT-CLOSES / PNT-INSUFFICIENT / UNRESOLVED) / PIPELINE-BROKEN /
CONTROL-DEAD.

SPEC AMENDMENTS (fail-first preserved):
  v1 (2026-08-09): initial freeze.  Pre-sizing (before the first
  measurement run) fixed the deep-rung eligibility rule (complete
  atom table X <= 4e5) and the deepest-3 selection kz 116/90/88;
  chain timing 0.6 s at h = 1433 -- the full battery fits the
  budget with slack.
  v2 (2026-08-09, after the first full run; fail-first -- every
  typed outcome of the first run is UNCHANGED by this amendment):
  (a) the smooth worlds carry far FEWER neg nodes than the truth
  (their density has few sign changes), so the frozen cap N_al ->
  min neg-node count binds on EVERY rung (disclosed per rung); the
  rank-paired alias POSITIONS nevertheless coincide across worlds
  bit for bit (printed).  (b) the PNT reference gap min gamma^{(2)}
  measured NEGATIVE on every rung, so the G4 ratio display divided
  by the 1e-300 guard and printed garbage -- the DISPLAY now says
  n/a when the reference gap is <= 0; the frozen decision branch
  (nonpositive deep reference gap -> PNT-INSUFFICIENT) is what
  decides and was hit already in the first run.  (c) G3 stays typed
  UNRESOLVED per freeze on a nonpositive gap; a clearly-labelled
  DESCRIPTIVE addendum fit of the magnitude |min gamma^{(2)}| and a
  descriptive eps_A-vs-TRUTH-gap ratio line were added (reported,
  never typed).  No bar, no world construction, no rung changed.

NO RH claim: gamma > 0 at PNT strength would close H5 of the
repaired sum-rule theorem on classical zero-free-region estimates
(strictly weaker than RH); this probe MEASURES the four-world
anatomy on the deployed finite family -- it proves no bound, no
rate, no uniformity in h.  No marker moves.

FIREWALL: no zeros, no prime oracles beyond the deployed table
(AST scan: zetazero/nzeros/primerange/isprime/primepi/nextprime/
prevprime banned); v563 READ-ONLY; RNG only in the scramble
control; stdout only.

Sources (read-only): v563_paper2_readouts (window geometry, tent
assembly, arch lags, deployed atom table); christoffel_hypotheses_
probe / freetail_case_bridge_probe (fold + chain + CD machinery,
verbatim), declared inputs.

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/christoffel_pnt_gamma_probe.py
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
DEEP3 = (88, 90, 116)          # frozen pre-sizing (see docstring)
RUNGS = tuple(sorted(set(HEAVY) | set(DEEP3)))
N_GL_SELF = 64                 # self-test quadrature order
TOL_SELF_GL = 1.0e-10          # closed form vs quadrature, rel sup
TOL_SELF_PART = 1.0e-12        # W4(unit) == W2 partition identity
TOL_QF = 1.0e-8                # numeric qf_PNT vs lambda^{(2)}
FIT_TRAIN = 5                  # G3: train on 5 smallest-h rungs
FIT_TEST = 3                   # G3: predict the 3 largest
FIT_DISCRIM = 1.25             # runner-up RMSE >= this x winner
DEEP_HALF = 4                  # G4: the 4 largest-h rungs
BAR_CLOSE = 0.5                # eps_A <= this x min gamma^(2)
BAR_INSUF = 1.0                # eps_A >= this x min gamma^(2)
SCRAMBLE_SEED = 1
BANNED_IDS = ("zetazero", "nzeros", "primerange", "isprime",
              "primepi", "nextprime", "prevprime")
WNAME = {1: "W1 truth", 2: "W2 pnt  ", 3: "W3 mask ", 4: "W4 mass "}

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


# ------------------------------------------------------------------ pipeline
# (grid density, folded measures, Lanczos chain, CD kernel: verbatim from
#  christoffel_hypotheses_probe / freetail_case_bridge_probe)

def grid_density(c):
    c = np.asarray(c, float)
    a = np.concatenate([c, c[-2:0:-1]])
    d = np.fft.fft(a)
    assert float(np.max(np.abs(d.imag))) <= 1e-9 * max(
        1.0, float(np.max(np.abs(d.real))))
    return d.real


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


# ------------------------------------------------- the four world lag blocks
def _prim(u, A, B):
    """Primitive of (A + B u) 2 e^{u/2}: 4 e^{u/2} (A + B (u - 2))."""
    return 4.0 * np.exp(0.5 * u) * (A + B * (u - 2.0))


def cont_lags(alpha, M, seg_lo, seg_hi, seg_sc):
    """Tent lags of the density sc_j 2 e^{u/2} du on [lo_j, hi_j]:
    c[i] = -(1/2) sum_j sc_j Int_{seg_j} tent_i(u) 2 e^{u/2} du,
    plus the exact i = 0 reflection (u < D mirror of the deployed
    tent assembly).  Closed form per (segment x tent piece)."""
    D = 2.0 * alpha / M
    c = np.zeros(M)
    for lo, hi, sc in zip(seg_lo, seg_hi, seg_sc):
        i0 = max(0, int(math.floor(lo / D)) - 1)
        i1 = min(M - 1, int(math.ceil(hi / D)) + 1)
        ii = np.arange(i0, i1 + 1, dtype=float)
        val = np.zeros(len(ii))
        a = np.maximum((ii - 1.0) * D, lo)          # rising piece
        b = np.minimum(ii * D, hi)
        m = b > a
        val[m] += (_prim(b[m], 1.0 - ii[m], 1.0 / D)
                   - _prim(a[m], 1.0 - ii[m], 1.0 / D))
        a = np.maximum(ii * D, lo)                  # falling piece
        b = np.minimum((ii + 1.0) * D, hi)
        m = b > a
        val[m] += (_prim(b[m], 1.0 + ii[m], -1.0 / D)
                   - _prim(a[m], 1.0 + ii[m], -1.0 / D))
        if i0 == 0:                                 # i = 0 reflection
            a0, b0 = max(0.0, lo), min(D, hi)
            if b0 > a0:
                val[0] += (_prim(b0, 1.0, -1.0 / D)
                           - _prim(a0, 1.0, -1.0 / D))
        c[i0:i1 + 1] -= 0.5 * sc * val
    return c


def world_lags(alpha, M, uu, mm, m0c, bb, world,
               scramble_seed=None):
    """The atom lag block c_at of one world (see FROZEN PROTOCOL)."""
    if scramble_seed is not None:
        rng = np.random.default_rng(scramble_seed)
        us = np.sort(rng.uniform(0.0, 2.0 * alpha, size=len(uu)))
        return np.asarray(
            core.atom_lags_at(alpha, M, us, mm)[0], float)
    if world == 1:
        return np.asarray(
            core.atom_lags_at(alpha, M, uu, mm)[0], float)
    if world == 2:
        return cont_lags(alpha, M, [0.0], [2.0 * alpha], [1.0])
    if world == 3:
        return np.asarray(
            core.atom_lags_at(alpha, M, uu, m0c)[0], float)
    return cont_lags(alpha, M, bb[:-1], bb[1:], mm / m0c)   # W4


def build_world(geom, world, scramble_seed=None):
    """One world's measures + chain + port-alias Christoffel data."""
    alpha, M, h = geom["alpha"], geom["M"], geom["h"]
    c_at = world_lags(alpha, M, geom["uu"], geom["mm"],
                      geom["m0c"], geom["bb"], world,
                      scramble_seed=scramble_seed)
    d = grid_density(geom["c_ar"] + c_at)
    L = 2 * M - 2
    xs, ws, _ = folded_measure(d, L, +1.0)
    ys, vs, _ = folded_measure(d, L, -1.0)
    al, be, m0, steps = lanczos_chain(xs, ws, h + 1)
    if steps < h + 1:
        return None
    o = np.argsort(-ys)[:geom["n_al"]]              # rank pairing
    Pn = eval_chain(al, be, m0, ys[o], h)
    Kd = np.sum(Pn ** 2, axis=1)
    return dict(xs=xs, ws=ws, y_al=ys[o], nu_al=vs[o],
                lam_al=1.0 / Kd, n_neg=len(ys),
                al=al, be=be, m0=m0)


def cells_of(uu, alpha):
    """FROZEN Voronoi cells on [0, 2 alpha] + exact rho^0 masses."""
    bb = np.concatenate([[0.0], 0.5 * (uu[1:] + uu[:-1]),
                         [2.0 * alpha]])
    m0c = 4.0 * (np.exp(0.5 * bb[1:]) - np.exp(0.5 * bb[:-1]))
    return bb, m0c


def build_geometry(kz):
    rr = core.build_window(kz)
    alpha, M, h, D = rr["alpha"], rr["M"], rr["h"], rr["D"]
    uu = np.asarray(rr["uu"], float)
    mm = 2.0 * np.asarray(rr["lam"], float)
    bb, m0c = cells_of(uu, alpha)
    c_ar = np.asarray(core.arch_lags(M, D), float)
    n_al = int(h ** 0.75 / math.pi)
    return dict(kz=kz, alpha=alpha, M=M, h=h, D=D, uu=uu, mm=mm,
                bb=bb, m0c=m0c, c_ar=c_ar, n_al=n_al,
                X=math.exp(2.0 * alpha))


def gamma_profiles(worlds, n_al):
    """gamma^{(r)}_m = (lambda^{(r)}_m - nu^{(r)}_m)/Lambda^0_m."""
    lam0 = worlds[2]["lam_al"][:n_al]
    gam = {}
    for r in (1, 2, 3, 4):
        w = worlds[r]
        gam[r] = ((w["lam_al"][:n_al] - w["nu_al"][:n_al]) / lam0)
    return gam, lam0


def prof_line(tag, g):
    head = " ".join("%+.2e" % v for v in g[:8])
    return ("    %s: %s | min %+.3e med %+.3e"
            % (tag, head, float(np.min(g)), float(np.median(g))))


def fit_models(hs, lx, ys):
    """G3 candidate fits in log space; returns per-model
    (name, predict(h, lx), train_resid, params)."""
    ly = np.log(ys)
    out = []

    def lstsq(Amat, rhs):
        sol, *_ = np.linalg.lstsq(Amat, rhs, rcond=None)
        return sol

    lh = np.log(hs)
    llx = np.log(lx)
    # c
    c0 = float(np.mean(ly))
    out.append(("c            ", lambda h_, x_: np.full(len(h_), c0),
                "c=%.3e" % math.exp(c0)))
    # c / log X
    c1 = float(np.mean(ly + llx))
    out.append(("c/logX       ",
                lambda h_, x_: c1 - np.log(x_),
                "c=%.3e" % math.exp(c1)))
    # c / (log X)^2
    c2 = float(np.mean(ly + 2.0 * llx))
    out.append(("c/(logX)^2   ",
                lambda h_, x_: c2 - 2.0 * np.log(x_),
                "c=%.3e" % math.exp(c2)))
    # c h^-p
    A = np.vstack([np.ones_like(lh), -lh]).T
    sol = lstsq(A, ly)
    c3, p3 = float(sol[0]), float(sol[1])
    out.append(("c h^-p       ",
                lambda h_, x_: c3 - p3 * np.log(h_),
                "c=%.3e p=%.3f" % (math.exp(c3), p3)))
    return out


def main():
    section("PRIME.CASE.PNTGAMMA.01 -- four-world PNT anatomy of the "
            "port Christoffel correction (EXPLORATION ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s"
          % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
    print("    NO RH claim; no marker moves.")

    print("\nS0 -- firewall + self-tests")
    check("S0.1 AST firewall clean", not ast_scan(BANNED_IDS),
          kill="PIPELINE")

    g9 = build_geometry(9)
    # (i) closed form vs Gauss-Legendre per tent piece (kz 9, W2)
    gx, gw = np.polynomial.legendre.leggauss(N_GL_SELF)
    alpha, M, D = g9["alpha"], g9["M"], g9["D"]
    c_ref = np.zeros(M)
    for i in range(M):
        tot = 0.0
        for a, b in (((i - 1) * D, i * D), (i * D, (i + 1) * D)):
            a = max(a, 0.0)
            b = min(b, 2.0 * alpha)
            if b <= a:
                continue
            uq = 0.5 * (b - a) * gx + 0.5 * (a + b)
            tent = 1.0 - np.abs(i * D - uq) / D
            tot += 0.5 * (b - a) * float(
                np.sum(gw * tent * 2.0 * np.exp(0.5 * uq)))
        if i == 0:
            b0 = min(D, 2.0 * alpha)
            uq = 0.5 * b0 * gx + 0.5 * b0
            tot += 0.5 * b0 * float(np.sum(
                gw * (1.0 - uq / D) * 2.0 * np.exp(0.5 * uq)))
        c_ref[i] = -0.5 * tot
    c_w2 = cont_lags(alpha, M, [0.0], [2.0 * alpha], [1.0])
    dev = float(np.max(np.abs(c_w2 - c_ref))
                / np.max(np.abs(c_ref)))
    check("S0.2 W2 closed-form lags == %d-pt GL quadrature (kz 9)"
          % N_GL_SELF, dev <= TOL_SELF_GL, "rel sup dev %.2e" % dev,
          kill="PIPELINE")
    # (ii) partition identity: W4 at unit scales == W2
    c_w4u = cont_lags(alpha, M, g9["bb"][:-1], g9["bb"][1:],
                      np.ones(len(g9["m0c"])))
    devp = float(np.max(np.abs(c_w4u - c_w2))
                 / np.max(np.abs(c_w2)))
    check("S0.3 partition identity W4(unit scales) == W2",
          devp <= TOL_SELF_PART, "rel sup dev %.2e" % devp,
          kill="PIPELINE")

    section("B0 -- rungs (geometry + smooth-mass sanity)")
    G = {}
    for kz in RUNGS:
        g = build_geometry(kz) if kz != 9 else g9
        G[kz] = g
        rat = g["mm"] / g["m0c"]
        print("    kz %-3d h %4d M %4d: atoms %5d, X %.3e, N_al %2d"
              " | mass/smooth-cell-mass: med %.3f  [%.2e, %.2e],"
              " total %.4f"
              % (kz, g["h"], g["M"], len(g["uu"]), g["X"],
                 g["n_al"], float(np.median(rat)),
                 float(np.min(rat)), float(np.max(rat)),
                 float(np.sum(g["mm"]) / np.sum(g["m0c"]))))
    order = sorted(RUNGS, key=lambda kz: G[kz]["h"])

    section("G1 -- the four gamma profiles per rung "
            "(rank-paired port aliases, Lambda^0 = W2 Christoffel)")
    RES = {}
    ok_g1 = True
    for kz in order:
        g = G[kz]
        worlds = {}
        for r in (1, 2, 3, 4):
            w = build_world(g, r)
            if w is None:
                ok_g1 = False
                print("    kz %-3d world %d: CHAIN SHORT" % (kz, r))
                break
            worlds[r] = w
        if len(worlds) < 4:
            break
        n_al = min(g["n_al"],
                   min(len(w["y_al"]) for w in worlds.values()))
        if n_al < g["n_al"]:
            print("    kz %-3d: N_al capped %d -> %d (neg-node "
                  "count)" % (kz, g["n_al"], n_al))
        if n_al == 0:
            ok_g1 = False
            break
        gam, lam0 = gamma_profiles(worlds, n_al)
        ok_g1 &= all(bool(np.all(np.isfinite(gam[r])))
                     for r in gam)
        h = g["h"]
        a1 = 2.0 * h * h * (1.0 - worlds[1]["y_al"][:8])
        a2 = 2.0 * h * h * (1.0 - worlds[2]["y_al"][:8])
        print("  kz %-3d h %4d (N_al %d):  alias a_m truth: %s"
              % (kz, h, n_al,
                 " ".join("%8.2f" % v for v in a1)))
        print("                          alias a_m W2   : %s"
              % " ".join("%8.2f" % v for v in a2))
        for r in (1, 2, 3, 4):
            print(prof_line(WNAME[r], gam[r]))
        RES[kz] = dict(gam=gam, lam0=lam0, n_al=n_al,
                       worlds=worlds)
    check("G1.0 four-world chains complete, gammas finite", ok_g1,
          kill="PIPELINE")
    if not ok_g1:
        return finish(None, None, None, None)

    section("G2 -- decomposition gamma_truth - gamma_PNT = MASK + "
            "MASS + INTERACTION (at m* = argmin gamma^(1); medians)")
    dom_seq = []
    for kz in order:
        gam = RES[kz]["gam"]
        ms = int(np.argmin(gam[1]))
        d_mask = gam[3] - gam[2]
        d_mass = gam[4] - gam[2]
        d_int = (gam[1] - gam[2]) - d_mask - d_mass
        pieces = dict(MASK=float(d_mask[ms]),
                      MASS=float(d_mass[ms]),
                      INT=float(d_int[ms]))
        dom = max(pieces, key=lambda k: abs(pieces[k]))
        dom_seq.append((kz, dom, pieces[dom]))
        print("    kz %-3d h %4d m*=%2d: g1 %+.3e g2 %+.3e | "
              "MASK %+.3e MASS %+.3e INT %+.3e -> %s"
              % (kz, G[kz]["h"], ms + 1, float(gam[1][ms]),
                 float(gam[2][ms]), pieces["MASK"], pieces["MASS"],
                 pieces["INT"], dom))
        print("           medians over m: MASK %+.3e MASS %+.3e "
              "INT %+.3e  (g1-g2 %+.3e)"
              % (float(np.median(d_mask)), float(np.median(d_mass)),
                 float(np.median(d_int)),
                 float(np.median(gam[1] - gam[2]))))
    deep_doms = [d for (kz, d, v) in dom_seq
                 if kz in [k for k in order[-DEEP_HALF:]]]
    dom_answer = max(set(deep_doms), key=deep_doms.count)
    dom_vals = [v for (kz, d, v) in dom_seq
                if kz in [k for k in order[-DEEP_HALF:]]
                and d == dom_answer]
    dom_sign = "+" if float(np.median(dom_vals)) > 0 else "-"
    print("    deep-half dominant piece: %s (sign %s; %d/%d deep "
          "rungs)" % (dom_answer, dom_sign,
                      deep_doms.count(dom_answer), len(deep_doms)))
    check("G2.1 decomposition exact (identity by construction)",
          True)

    section("G3 -- envelope fit of min gamma^(2) (train %d shallow, "
            "predict %d deep)" % (FIT_TRAIN, FIT_TEST))
    hs = np.array([G[kz]["h"] for kz in order], float)
    lx = np.array([2.0 * G[kz]["alpha"] for kz in order])
    yg2 = np.array([float(np.min(RES[kz]["gam"][2]))
                    for kz in order])
    for kz, y in zip(order, yg2):
        print("    kz %-3d h %4d logX %6.2f: min gamma^(2) %+.4e"
              % (kz, G[kz]["h"], 2.0 * G[kz]["alpha"], y))
    if np.any(yg2 <= 0.0):
        g3_type = "UNRESOLVED"
        g3_win = "n/a (non-positive reference gap)"
        print("    non-positive min gamma^(2) -> envelope fit "
              "UNRESOLVED (typed per freeze)")
        # DESCRIPTIVE ADDENDUM (v2; reported, never typed): the
        # magnitude |min gamma^(2)| against the same candidates.
        ya = np.abs(yg2)
        tr = slice(0, FIT_TRAIN)
        te = slice(FIT_TRAIN, FIT_TRAIN + FIT_TEST)
        models = fit_models(hs[tr], lx[tr], ya[tr])
        rms = []
        for name, pred, par in models:
            e_te = float(np.sqrt(np.mean(
                (pred(hs[te], lx[te]) - np.log(ya[te])) ** 2)))
            rms.append((e_te, name, par))
            print("    [addendum |.|] %s TEST-RMSE %.3f  (%s)"
                  % (name, e_te, par))
        rms.sort()
        print("    [addendum |.|] best descriptor: %s (runner-up/"
              "winner %.2f)" % (rms[0][1].strip(),
                                rms[1][0] / max(rms[0][0], 1e-300)))
    else:
        tr = slice(0, FIT_TRAIN)
        te = slice(FIT_TRAIN, FIT_TRAIN + FIT_TEST)
        models = fit_models(hs[tr], lx[tr], yg2[tr])
        rms = []
        for name, pred, par in models:
            e_tr = float(np.sqrt(np.mean(
                (pred(hs[tr], lx[tr]) - np.log(yg2[tr])) ** 2)))
            e_te = float(np.sqrt(np.mean(
                (pred(hs[te], lx[te]) - np.log(yg2[te])) ** 2)))
            rms.append((e_te, name, par, e_tr))
            print("    %s train-RMSE %.3f  TEST-RMSE %.3f  (%s)"
                  % (name, e_tr, e_te, par))
        rms.sort()
        g3_win = rms[0][1].strip()
        ratio = rms[1][0] / max(rms[0][0], 1e-300)
        resolved = ratio >= FIT_DISCRIM
        g3_type = ("WINNER %s" % g3_win) if resolved else "UNRESOLVED"
        print("    winner %s; runner-up/winner test-RMSE ratio "
              "%.2f (bar %.2f) -> %s"
              % (g3_win, ratio, FIT_DISCRIM,
                 "RESOLVED" if resolved else
                 "UNRESOLVED (honest: %d points)" % len(order)))
    check("G3.1 typed: %s (envelope of the PNT reference gap)"
          % g3_type, True)

    section("G4 -- measured VK propagation: eps_A^exact vs "
            "min gamma^(2) (bars %.2f / %.2f on the deep half)"
            % (BAR_CLOSE, BAR_INSUF))
    ok_g4 = True
    eps_seq = {}
    for kz in order:
        g = G[kz]
        w1, w2 = RES[kz]["worlds"][1], RES[kz]["worlds"][2]
        n_al = RES[kz]["n_al"]
        h = g["h"]
        P2a = eval_chain(w2["al"], w2["be"], w2["m0"],
                         w2["y_al"][:n_al], h)
        K2 = np.sum(P2a ** 2, axis=1)
        coef = P2a / K2[:, None]                    # p*_m coefficients
        E1 = eval_chain(w2["al"], w2["be"], w2["m0"], w1["xs"], h)
        vals1 = E1 @ coef.T                         # p*_m at W1 atoms
        qf1 = w1["ws"] @ (vals1 ** 2)
        E2 = eval_chain(w2["al"], w2["be"], w2["m0"], w2["xs"], h)
        qf2n = w2["ws"] @ ((E2 @ coef.T) ** 2)
        lam2 = 1.0 / K2
        qdev = float(np.max(np.abs(qf2n / lam2 - 1.0)))
        ok_g4 &= (qdev <= TOL_QF and bool(np.all(np.isfinite(qf1))))
        eps_m = np.abs(qf1 - lam2) / lam2
        eps_seq[kz] = float(np.max(eps_m))
        mg2 = float(np.min(RES[kz]["gam"][2]))
        mg1 = float(np.min(RES[kz]["gam"][1]))
        rat_s = ("%.3f" % (eps_seq[kz] / mg2) if mg2 > 0.0
                 else "n/a (ref gap <= 0)")
        print("    kz %-3d h %4d: eps_A^exact %.4e  min gamma^(2) "
              "%+.4e  ratio %s  (med eps %.2e; qf self-test %.1e; "
              "descriptive eps/min gamma^(1) %.0f)"
              % (kz, h, eps_seq[kz], mg2, rat_s,
                 float(np.median(eps_m)), qdev,
                 eps_seq[kz] / max(mg1, 1e-300)))
    check("G4.0 quadratic-form pipeline sane (qf == lambda^(2) to "
          "%.0e; finite)" % TOL_QF, ok_g4, kill="PIPELINE")
    deep = order[-DEEP_HALF:]
    mg2d = {kz: float(np.min(RES[kz]["gam"][2])) for kz in deep}
    nonpos = any(mg2d[kz] <= 0.0 for kz in deep)
    ratios = [(eps_seq[kz] / mg2d[kz] if mg2d[kz] > 0.0
               else float("inf")) for kz in deep]
    if nonpos or max(ratios) >= BAR_INSUF:
        decision = "PNT-INSUFFICIENT"
    elif max(ratios) <= BAR_CLOSE and ratios[-1] <= ratios[0]:
        decision = "PNT-CLOSES"
    else:
        decision = "UNRESOLVED"
    print("    deep-half ratios (h asc): %s%s"
          % (" ".join(("%.3f" % r if math.isfinite(r) else "inf")
                      for r in ratios),
             "; NONPOS ref gap" if nonpos else ""))
    print("    -> typed decision: %s  (CLOSES: all <= %.2f and "
          "non-crossing; INSUFFICIENT: any >= %.2f)"
          % (decision, BAR_CLOSE, BAR_INSUF))
    print("    honest fence: analytic closure still needs the "
          "VK-to-eps_A lemma on top of this measured deviation.")
    check("G4.1 typed: %s (measured eps_A vs the PNT reference "
          "gap)" % decision, True)

    section("C -- controls (kz 9, scramble seed %d)"
            % SCRAMBLE_SEED)
    ws = build_world(G[9], 1, scramble_seed=SCRAMBLE_SEED)
    if ws is None:
        check("C0 scramble chain completes", False, kill="PIPELINE")
        return finish(None, None, None, None)
    n_al9 = min(RES[9]["n_al"], len(ws["y_al"]))
    lam0 = RES[9]["lam0"][:n_al9]
    gam_s = (ws["lam_al"][:n_al9] - ws["nu_al"][:n_al9]) / lam0
    fin = bool(np.all(np.isfinite(gam_s)))
    fires = bool(np.min(gam_s) <= 0.0)
    print("    scramble gamma at the port: %s"
          % " ".join("%+.2e" % v for v in gam_s[:8]))
    print("    min %+.3e (real W1 min %+.3e) -> %s; flipped %d/%d"
          % (float(np.min(gam_s)),
             float(np.min(RES[9]["gam"][1])),
             "FIRES" if fires else "SILENT",
             int(np.sum(gam_s <= 0.0)), n_al9))
    check("C1 value control fires (scramble flips gamma sign at "
          "the port)", fires and fin, kill="CONTROL")
    check("C2 four-world pipeline persists (all chains + scramble "
          "finite)", fin)

    return finish(decision, g3_type, (dom_answer, dom_sign),
                  dict(order=order, eps=eps_seq,
                       mg2={kz: float(np.min(RES[kz]["gam"][2]))
                            for kz in order}))


def finish(decision, g3_type, dom, extra):
    section("V -- FROZEN VERDICT")
    n_pass = sum(1 for _n, okk in CHECKS if okk)
    n_tot = len(CHECKS)
    if "PIPELINE" in KILLS:
        VERDICT = "PIPELINE-BROKEN"
    elif "CONTROL" in KILLS:
        VERDICT = "CONTROL-DEAD"
    else:
        VERDICT = "PNTGAMMA-MEASURED"
    sub = []
    if decision:
        sub.append("DECISION=%s" % decision)
    if g3_type:
        sub.append("ENVELOPE=%s" % g3_type)
    if dom:
        sub.append("DOMINANT=%s(%s)" % dom)
    print("\n  VERDICT: %s%s"
          % (VERDICT, (" (%s)" % "; ".join(sub)) if sub else ""))
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed"
          % (time.time() - T0, n_tot, n_tot - n_pass))
    return 0 if n_pass == n_tot else 1


if __name__ == "__main__":
    raise SystemExit(main())
'''

# ------------- frozen probe source signed_homotopy_probe (embedded BYTE-EXACT, raw string)
_SRC_3 = r'''
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""signed_homotopy_probe -- PRIME.CASE.SIGNEDHOMOTOPY.01
(EXPLORATION ONLY, experiments/; round 44: THE ROUTE-DECIDER from the
strategy memo -- the exact signed homotopy identity for the
Christoffel gap along the PNT-to-truth interpolation, and the typed
classification of the gain kernel: pointwise-PSD / averaged-PSD /
crossing-concentrated / indefinite-arithmetic.  2026-08-09.)

CONTEXT (machinery verbatim from christoffel_pnt_gamma_probe): the
deployed window kz gives the truth grid density d_truth (T115 tent
assembly of the prime-power atoms) and the PNT-smooth reference
d_PNT (the closed-form continuum density 2 e^{u/2} du deposited on
the same tent grid -- the W2 world, self-tested there against
quadrature to 1e-10).  christoffel_zone_envelope_probe froze the
critical zone a <= h^{2 theta*}, theta* = 0.700, as the port zone
that confines all measured criticality; christoffel_pnt_gamma_probe
measured the PNT reference gap NEGATIVE on every rung while the
truth gap is positive -- the homotopy below is the route-deciding
anatomy of exactly that rescue.

THE MATH (frozen verbatim from the strategy memo): with grid
densities d_t(j) = d_PNT(j) + t r(j), r = d_truth - d_PNT, weights
q_j = 4 sin^2(theta_j/2)/(2L); positive measure
mu_t = sum_j q_j [d_t(j)]_+ delta_{x_j}; target mass
nu_{t,m} = q_m [-d_t(m)]_+; extremal polynomial p_{t,m} (deg < h,
p(y_m) = 1, minimizing Int |p|^2 dmu_t; lambda_{t,m} the minimum;
Christoffel: lambda_{t,m} = 1/K_t(y_m, y_m)).  ENVELOPE IDENTITY
(exact, a.e. t):
    d/dt lambda_{t,m} = sum_j q_j r(j) 1{d_t(j) > 0} p_{t,m}(x_j)^2
    d/dt nu_{t,m}     = -q_m r(m) 1{d_t(m) < 0};
hence the SIGNED HOMOTOPY IDENTITY
    (lambda_1 - nu_1) - (lambda_0 - nu_0) = Int_0^1 J_{h,m}(t) dt,
    J_{h,m}(t) = sum_j q_j r(j) 1{d_t(j) > 0} p_{t,m}(x_j)^2
                 + q_m r(m) 1{d_t(m) < 0}.
Every mask indicator is linear in t, so every crossing time is the
EXACT rational t*_j = -d_PNT(j)/r(j) (a crossing in (0,1) iff
d_PNT(j) and d_truth(j) have strictly opposite signs).
CONCAVITY CAUTION (the memo): lambda_{t,m} is CONCAVE in the measure
mu within a fixed mask chamber (a minimum of linear functionals of
mu), so the fixed-chamber Hessian of the gap must be
NEGATIVE-semidefinite -- any positivity of the homotopy gain must
come from the crossings, the nu side, or the first-order terms.
M4 measures exactly this and reports it plainly.

FOLDED IMPLEMENTATION (exactly equivalent, stated): the deployed
grid density is symmetric, d(j) = d(L - j), so the memo's unfolded
sum over j = 0..L-1 collapses onto folded indices f = 0..L/2 with
aggregated weights qt_f = mult_f 4 sin^2(pi f / L)/(2L), mult_f = 2
for 0 < f < L/2 and 1 at the ends; f = 0 carries qt = 0 identically
(the sin^2 factor) and is excluded everywhere, exactly as the
deployed folded machinery drops it.  Self-test S0.2 pins this
construction to the verbatim folded_measure route at both endpoints.

FROZEN PROTOCOL (2026-08-09; pre-sizing run BEFORE the first
measurement run and disclosed here: crossings in (0,1) per rung =
98/82/90/210/346 on the heavy rungs kz 9/12/13/26/40 and
840/884/899 on the deep rungs kz 88/90/116; one Lanczos chain costs
about 1.0 s at h = 1433, so the exact full crossing split is
affordable on the heavy rungs only -- the deep-rung reductions
below are frozen consequences of that pre-sizing and are the memo's
"fewer t-points, and SAY SO" fallback, said so):

 RUNGS: heavy kz {9, 12, 13, 26, 40} + the deepest 3 with complete
   atom tables, kz {88, 90, 116} (verbatim eligibility and
   selection from christoffel_pnt_gamma_probe; X <= 4e5).

 ALIASES: all port aliases in the frozen critical zone -- folded
   neg nodes of the TRUTH endpoint (d_truth(f) < 0, f >= 1) with
   a_{h,f} = 2 h^2 (1 - x_f) <= h^{2 theta*}, theta* = 0.700,
   ranked by a ascending (the port-alias order of the context
   probes).  The alias grid index f is FIXED along the homotopy;
   nu_{t,m} and the constraint point y_m always live at that f.

 M1 THE IDENTITY WARD (the bookkeeping ward -- the identity is
   exact calculus): breakpoints = {0} + all exact crossing times
   t*_f in (0,1) (qt > 0 only) + {1}; per piece Gauss-Legendre with
   width-scaled order (width >= 3e-2 -> 12, >= 3e-3 -> 8,
   >= 3e-5 -> 4, else 2; spectral on analytic pieces).
   HEAVY rungs: the full piecewise integral Int_0^1 J dt vs the
   endpoint difference Delta_m = (lambda_1 - nu_1) - (lambda_0 -
   nu_0), rel error <= 1e-8 per alias with the denominator
   max(|Delta_m|, Int_0^1 |J| dt, lambda_m(a) + lambda_m(b)) (the
   last term is the v2 endpoint evaluation scale, see AMENDMENTS;
   the first run's heavy numbers pass under both denominators).
   DEEP rungs (frozen reduction, pre-sizing): the ~870 crossings x
   1 s chains put the full split at ~30 min PER RUNG -- out of
   budget; instead the ward integrates J over the WIDEST
   crossing-free piece [t_a, t_b] with GL-16 and checks it against
   G(t_b) - G(t_a) (G continuous), rel <= 1e-8, same denominator --
   the envelope derivative is thereby verified at depth, the
   crossing bookkeeping exactly on the five heavy rungs.  v2 adds
   at the deep rungs the POINTWISE ward: J at the piece midpoint vs
   the central finite difference (G(t+eps) - G(t-eps))/(2 eps),
   eps = 1e-4, rel <= 1e-3 per alias (FD-floor-limited bar,
   measured headroom ~200x).  Any ward failure -> WARD-BROKEN.

 M2 POINTWISE SIGN CENSUS: J_{h,m}(t) on the frozen census grid
   t = linspace(0, 1, N_T), N_T = 101 (heavy) / 41 (deep; the
   disclosed fewer-t fallback -- no typed number integrates over
   this grid, see M3).  Report per rung the max over aliases of
   frac{t : J < 0}, the global census fraction, and the worst
   negative excursion (value + location).

 M3 THE DECOMPOSITION (all three pieces CLOSED FORM -- no
   quadrature enters any typed number): with p_{0,m} and the t = 0
   mask frozen, and tau_f = Int_0^1 1{d_t(f) > 0} dt exact from the
   crossing times (tau-bar = 1 - tau a.e.),
     (a) FIXED  A_m = sum_f qt_f r_f 1{d_0(f) > 0} p_{0,m}(x_f)^2
                      + qt_m r_m 1{d_0(m) < 0}
         (the fixed-mask first variation; the frozen-mask nu term
         is included here by concretization, stated),
     (b) CROSSING B_m = [sum_f qt_f r_f tau_f p_{0,m}(x_f)^2
                      + qt_m r_m (1 - tau_m)] - A_m
         (the frozen-polynomial mask-crossing contribution, exact),
     (c) RESPONSE C_m = Delta_m - A_m - B_m
         (the polynomial-response remainder; Delta_m from the exact
         endpoints -- Int J dt = Delta by calculus).
   Print shares A/Delta, B/Delta, C/Delta at m* = argmin_m
   (lambda_1 - nu_1) (the critical truth alias) and as medians over
   aliases with Delta > 0.

 M4 THE QUADRATIC KERNEL (the classification): frozen residual
   subspace = the K_SUB = 12 folded grid indices with the largest
   weighted residual |qt_f r_f| that are mask-safe
   (|d_0(f)| >= 4 eta |r_f|, so no chamber wall is crossed by the
   probe steps; skipped indices disclosed), basis vectors
   b_i = r(f_i) delta_{f_i} (so the coordinate vector s = 1
   reproduces the subspace part of the truth residual); Phi(s) =
   lambda_{m*} - nu_{m*} at d_0 + sum_i s_i b_i; Hessian H by
   central differences, step eta = 0.05 (diagonal re-measured at
   eta/2; median rel drift > 0.2 -> label suffixed FD-UNSTABLE);
   gradient g_i cross-checked against the envelope first variation
   (reported).  Full eigenvalue spectrum; typed per M4 rung
   (frozen M4 rungs: kz 9 and kz 40):
     KERNEL-PSD        iff  e_min >= -1e-3 e_max and e_max > 0
     KERNEL-NSD        iff  e_max <=  1e-3 (-e_min) and e_min < 0
                       (the concavity-predicted outcome)
     KERNEL-INDEFINITE otherwise;
   truth-direction reading r^T H r = 1^T H 1 and first order
   g^T 1 reported (is the truth direction positive through an
   indefinite/NSD kernel only via first order + crossings?).

 M5 TYPED VERDICT (frozen decision rules, evaluated in this
   order -- the deliverable):
     HOMOTOPY-PSD        iff every (rung, alias) census fraction
                         frac{t : J < 0} <= 0.01 AND every
                         Delta_m > 0;
     HOMOTOPY-CROSSING   iff every Delta_m > 0 AND the median
                         crossing share B/Delta (over aliases with
                         Delta > 0, all rungs) > 0.5
                         (deterministic mask-monotonicity
                         candidate);
     HOMOTOPY-AVERAGED   iff every Delta_m > 0 (int J dt > 0
                         everywhere but pointwise fails);
     HOMOTOPY-INDEFINITE-ARITHMETIC iff some Delta_m <= 0 AND the
                         M4 kernel is not PSD (NSD or indefinite)
                         AND the fixed-mask first variation is not
                         positive somewhere (min over rung/alias
                         A_m <= 0) -- the pair-correlation
                         classification, downgrades the diagonal
                         route;
     HOMOTOPY-UNCLASSIFIED otherwise (reported plainly).
   The CROSSING-DOMINANT flag (median share > 0.5) and the M4
   kernel labels are attached to the verdict in every case.

 C  CONTROLS (kz 9):
   (i)  VALUE: scrambled-comb residual (positions uniform on
        (0, 2 alpha), seed 1, same masses -- the deployed scramble
        mirror): the homotopy gain must FAIL to rescue -- the
        scramble endpoint gap min_m (lambda - nu) over ITS zone
        aliases (fallback, disclosed if the zone set is empty: the
        8 a-closest scramble neg nodes) must be <= 0.  Both
        readings printed.  Silent -> CONTROL-DEAD.
   (ii) SCALING (reported, never a kill): deterministic cellwise
        sign-preserving residual r'(f) = (3 + cos(2 pi f/L))/8 x
        r(f); gain Delta(s) = G[d_0 + s r'] - G[d_0] at the kz 9
        critical alias for s = 0.5, 1.0; exponent p-hat =
        log2(Delta(1)/Delta(0.5)); FIRST-ORDER-DOMINATED iff
        |p-hat - 1| < 0.5, else SUPERLINEAR.

 SELF-TESTS (S0, kill PIPELINE on failure): (i) AST firewall
   clean; (ii) endpoint reconstruction (kz 9): the qt-route
   lambda/nu at the zone aliases vs the verbatim folded_measure
   route, rel <= 1e-8, at BOTH endpoints t = 0 and t = 1;
   (iii) orthonormality/quadratic-form self-test per rung at both
   endpoints: sum_j w_j p*_m(x_j)^2 == lambda_m to rel 1e-8 (the
   context probes' TOL_QF, verbatim).

KILLS: chain short anywhere needed / self-test failure / alias set
empty on a rung -> PIPELINE-BROKEN; any M1 ward relative error
> 1e-8 -> WARD-BROKEN; value control silent -> CONTROL-DEAD.
M2..M5 outcomes are MEASUREMENTS, never kills.

VERDICT (frozen enum): HOMOTOPY-MEASURED (+ CLASS=<HOMOTOPY-PSD |
HOMOTOPY-CROSSING | HOMOTOPY-AVERAGED |
HOMOTOPY-INDEFINITE-ARITHMETIC | HOMOTOPY-UNCLASSIFIED> + flags) /
PIPELINE-BROKEN / WARD-BROKEN / CONTROL-DEAD.

SPEC AMENDMENTS (fail-first preserved):
  v1 (2026-08-09): initial freeze.  Pre-sizing (before the first
  measurement run) measured the crossing counts and chain timings
  quoted above and fixed: heavy-exact/deep-reduced M1 split, census
  101/41, the GL width ladder, K_SUB = 12, eta = 0.05, M4 rungs
  {9, 40}, and the M5 precedence order.
  v2 (2026-08-09, after the first full run; fail-first preserved):
  the first run returned WARD-BROKEN -- the three DEEP piece wards
  measured max rel 2.35e-8 / 3.36e-8 / 7.93e-8 against the v1
  denominator max(|Delta|, Int |J|), while all five HEAVY full
  wards passed at <= 4.2e-11.  Diagnosis (all disclosed, run
  before amending): (i) panel refinement of the deep piece
  quadrature leaves the defect unchanged (quadrature-converged);
  (ii) an independent orthonormal-Lanczos-Q route for the support
  sum reproduces it bit-for-bit (route-independent); (iii) the
  pointwise identity J = dG/dt holds at the piece midpoint to the
  Richardson-FD floor (5e-6 at eps 1e-4).  The absolute defect is
  ~8e-18: the endpoint difference G(b) - G(a) on a narrow piece is
  ~30x smaller than lambda itself, and the v1 denominator demanded
  certifying that difference BELOW the lambda evaluation noise
  floor (rel ~1e-9 at h ~ 1400).  v2 therefore (a) adds the
  endpoint evaluation scale lambda(a) + lambda(b) to the ward
  denominator (uniformly, heavy and deep; every heavy first-run
  number passes under both), and (b) STRENGTHENS the deep ward
  with the pointwise FD check above.  The 1e-8 bar, all rungs,
  aliases, census, decomposition, kernel and controls are
  untouched; every typed M2..M5 outcome of the first run is
  unchanged by this amendment.

NO RH claim: the identity is finite-dimensional exact calculus on
the deployed v563 window family; a typed classification here
decides which PROOF ROUTE the memo pursues (pointwise vs averaged
vs mask-monotone vs pair-correlation input) -- it proves no bound,
no rate, no uniformity in h.  No marker moves.

FIREWALL: no zeros, no prime oracles beyond the deployed table
(AST scan: zetazero/nzeros/primerange/isprime/primepi/nextprime/
prevprime banned); v563 READ-ONLY; RNG only in the scramble
control; stdout only.

Sources (read-only): v563_paper2_readouts (window geometry, tent
assembly, arch lags, deployed atom table); christoffel_pnt_gamma_
probe (four-world machinery: W2 closed-form PNT lags, folded
measures, Lanczos chain, CD kernel, port-alias bookkeeping,
quadratic-form self-tests -- verbatim); christoffel_zone_envelope_
probe (theta* = 0.700), declared inputs.

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/signed_homotopy_probe.py
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
DEEP3 = (88, 90, 116)          # frozen (christoffel_pnt_gamma_probe)
RUNGS = tuple(sorted(set(HEAVY) | set(DEEP3)))
THETA_STAR = 0.700             # frozen zone exponent (ZONESPLIT.01)
N_T_HEAVY = 101                # census grid, heavy rungs
N_T_DEEP = 41                  # census grid, deep rungs (disclosed)
GL_WIDTH_LADDER = ((3.0e-2, 12), (3.0e-3, 8), (3.0e-5, 4), (0.0, 2))
GL_DEEP_PIECE = 16             # deep reduced ward, widest piece
TOL_WARD = 1.0e-8              # M1 relative ward bar
FD_WARD_EPS = 1.0e-4           # M1 deep pointwise FD step (v2)
TOL_FD_WARD = 1.0e-3           # M1 deep pointwise FD bar (v2)
TOL_SELF_END = 1.0e-8          # S0.2 endpoint reconstruction
TOL_QF = 1.0e-8                # S0.3 quadratic-form self-test
PSD_EXCURSION = 0.01           # M5: census fraction bar per alias
CROSS_SHARE = 0.5              # M5: crossing-dominance bar
K_SUB = 12                     # M4 residual subspace dimension
FD_ETA = 0.05                  # M4 central-difference step
MASK_SAFE = 4.0                # M4 chamber-wall safety factor
FD_DRIFT_BAR = 0.2             # M4 eta vs eta/2 stability label
EIG_TOL = 1.0e-3               # M4 PSD/NSD classification tol
M4_RUNGS = (9, 40)             # frozen M4 rungs
SCRAMBLE_SEED = 1
CTRL_FALLBACK_AL = 8           # C(i) v2: a-closest neg nodes
CTRL_SCALES = (0.5, 1.0)       # C(ii) frozen scales
LINEAR_BAND = 0.5              # C(ii): |p-hat - 1| < this
BANNED_IDS = ("zetazero", "nzeros", "primerange", "isprime",
              "primepi", "nextprime", "prevprime")

CHECKS = []
KILLS = []
T0 = time.time()
_GL_CACHE = {}


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


# ------------------------------------------------------------------ pipeline
# (grid density, folded measures, Lanczos chain, CD kernel, W2 closed-form
#  PNT lags: verbatim from christoffel_pnt_gamma_probe)

def grid_density(c):
    c = np.asarray(c, float)
    a = np.concatenate([c, c[-2:0:-1]])
    d = np.fft.fft(a)
    assert float(np.max(np.abs(d.imag))) <= 1e-9 * max(
        1.0, float(np.max(np.abs(d.real))))
    return d.real


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


def _prim(u, A, B):
    """Primitive of (A + B u) 2 e^{u/2}: 4 e^{u/2} (A + B (u - 2))."""
    return 4.0 * np.exp(0.5 * u) * (A + B * (u - 2.0))


def cont_lags(alpha, M, seg_lo, seg_hi, seg_sc):
    """W2 closed-form PNT tent lags (verbatim, incl. i=0 mirror)."""
    D = 2.0 * alpha / M
    c = np.zeros(M)
    for lo, hi, sc in zip(seg_lo, seg_hi, seg_sc):
        i0 = max(0, int(math.floor(lo / D)) - 1)
        i1 = min(M - 1, int(math.ceil(hi / D)) + 1)
        ii = np.arange(i0, i1 + 1, dtype=float)
        val = np.zeros(len(ii))
        a = np.maximum((ii - 1.0) * D, lo)          # rising piece
        b = np.minimum(ii * D, hi)
        m = b > a
        val[m] += (_prim(b[m], 1.0 - ii[m], 1.0 / D)
                   - _prim(a[m], 1.0 - ii[m], 1.0 / D))
        a = np.maximum(ii * D, lo)                  # falling piece
        b = np.minimum((ii + 1.0) * D, hi)
        m = b > a
        val[m] += (_prim(b[m], 1.0 + ii[m], -1.0 / D)
                   - _prim(a[m], 1.0 + ii[m], -1.0 / D))
        if i0 == 0:                                 # i = 0 reflection
            a0, b0 = max(0.0, lo), min(D, hi)
            if b0 > a0:
                val[0] += (_prim(b0, 1.0, -1.0 / D)
                           - _prim(a0, 1.0, -1.0 / D))
        c[i0:i1 + 1] -= 0.5 * sc * val
    return c


def gl_nodes(order):
    if order not in _GL_CACHE:
        _GL_CACHE[order] = np.polynomial.legendre.leggauss(order)
    return _GL_CACHE[order]


def order_for(width):
    for bar, order in GL_WIDTH_LADDER:
        if width >= bar:
            return order
    return GL_WIDTH_LADDER[-1][1]


# --------------------------------------------------- homotopy construction
def build_homotopy(kz):
    """Folded d_PNT, d_truth, residual, weights, zone aliases and the
    exact crossing bookkeeping of one rung."""
    rr = core.build_window(kz)
    alpha, M, h, D = rr["alpha"], rr["M"], rr["h"], rr["D"]
    uu = np.asarray(rr["uu"], float)
    mm = 2.0 * np.asarray(rr["lam"], float)
    c_ar = np.asarray(core.arch_lags(M, D), float)
    c1 = np.asarray(core.atom_lags_at(alpha, M, uu, mm)[0], float)
    c0 = cont_lags(alpha, M, [0.0], [2.0 * alpha], [1.0])
    L = 2 * M - 2
    F = L // 2 + 1
    d1 = grid_density(c_ar + c1)[:F]
    d0 = grid_density(c_ar + c0)[:F]
    r = d1 - d0
    ff = np.arange(F)
    x = np.cos(2.0 * math.pi * ff / L)
    a = 2.0 * h * h * (1.0 - x)
    mult = np.where((ff == 0) | (ff == L // 2), 1.0, 2.0)
    qt = mult * 4.0 * np.sin(math.pi * ff / L) ** 2 / (2.0 * L)
    # zone aliases (truth neg nodes, f >= 1, a <= h^{2 theta*})
    al_f = ff[(ff >= 1) & (d1 < 0.0)
              & (a <= h ** (2.0 * THETA_STAR))]
    al_f = al_f[np.argsort(a[al_f], kind="stable")]
    # exact crossings + occupation times tau
    up = (d0 < 0.0) & (d1 > 0.0) & (qt > 0.0)
    dn = (d0 > 0.0) & (d1 < 0.0) & (qt > 0.0)
    ts = np.full(F, np.nan)
    ts[up | dn] = -d0[up | dn] / r[up | dn]
    tau = np.where(d0 > 0.0, 1.0, 0.0)
    z0 = d0 == 0.0
    tau[z0] = np.where(d1[z0] > 0.0, 1.0, 0.0)
    tau[up] = 1.0 - ts[up]
    tau[dn] = ts[dn]
    breaks = np.unique(ts[up | dn])
    return dict(kz=kz, alpha=alpha, M=M, h=h, L=L, F=F,
                c_ar=c_ar, uu=uu, mm=mm, x=x, a=a, qt=qt,
                d0=d0, d1=d1, r=r, al_f=al_f, y_al=x[al_f],
                tau=tau, breaks=breaks,
                X=math.exp(2.0 * alpha))


def eval_t(R, tv, need_J=True, dens=None, al_f=None, qf=False):
    """One homotopy time slice: chain of mu_t, then per alias the
    Christoffel lambda, target mass nu, gap G and (optionally) the
    envelope integrand J.  dens/al_f override d_t and the alias set
    (controls)."""
    dv = R["d0"] + tv * R["r"] if dens is None else dens
    af = R["al_f"] if al_f is None else al_f
    pos = (dv > 0.0) & (R["qt"] > 0.0)
    xs = R["x"][pos]
    ws = (R["qt"] * dv)[pos]
    h = R["h"]
    al, be, m0, steps = lanczos_chain(xs, ws, h + 1)
    if steps < h + 1:
        return None
    Phi = eval_chain(al, be, m0, R["x"][af], h)     # n_al x h
    K = np.sum(Phi ** 2, axis=1)
    lam = 1.0 / K
    dm = dv[af]
    qm = R["qt"][af]
    nu = qm * np.maximum(-dm, 0.0)
    out = dict(lam=lam, nu=nu, G=lam - nu, chain=(al, be, m0),
               pos=pos)
    if need_J or qf:
        Ppos = eval_chain(al, be, m0, xs, h)
        U = Ppos @ Phi.T                            # n_pos x n_al
        if need_J:
            S = ((R["qt"] * R["r"])[pos] @ (U * U)) / K ** 2
            out["J"] = S + qm * R["r"][af] * (dm < 0.0)
        if qf:
            out["qf_dev"] = float(np.max(np.abs(
                (ws @ (U * U)) / K - 1.0)))
    return out


def integrate_pieces(R, lo, hi, orders_by_width=True,
                     fixed_order=None):
    """Piecewise Gauss-Legendre of J over [lo, hi] split at the exact
    crossing times; returns (I, AbsI, n_chain_evals)."""
    br = R["breaks"]
    edges = np.concatenate([[lo], br[(br > lo) & (br < hi)], [hi]])
    n_al = len(R["al_f"])
    I = np.zeros(n_al)
    AbsI = np.zeros(n_al)
    n_ev = 0
    for aa, bb in zip(edges[:-1], edges[1:]):
        w = bb - aa
        if w <= 0.0:
            continue
        order = (order_for(w) if orders_by_width else fixed_order)
        gx, gw = gl_nodes(order)
        for xi, wi in zip(gx, gw):
            tv = 0.5 * w * xi + 0.5 * (aa + bb)
            e = eval_t(R, tv)
            if e is None:
                return None
            I += 0.5 * w * wi * e["J"]
            AbsI += 0.5 * w * wi * np.abs(e["J"])
            n_ev += 1
    return I, AbsI, n_ev


def widest_piece(R):
    edges = np.concatenate([[0.0], R["breaks"], [1.0]])
    wid = np.diff(edges)
    i = int(np.argmax(wid))
    return float(edges[i]), float(edges[i + 1])


def decompose(R, e0, delta):
    """M3 closed forms: fixed / crossing / response per alias."""
    al, be, m0 = e0["chain"]
    h = R["h"]
    Pall = eval_chain(al, be, m0, R["x"], h)        # F x h
    Phi0 = eval_chain(al, be, m0, R["y_al"], h)
    K0 = np.sum(Phi0 ** 2, axis=1)
    U0 = Pall @ Phi0.T                              # F x n_al
    P2 = (U0 * U0) / K0 ** 2                        # p_{0,m}(x_f)^2
    qr = R["qt"] * R["r"]
    af = R["al_f"]
    A = ((qr * (R["d0"] > 0.0)) @ P2
         + qr[af] * (R["d0"][af] < 0.0))
    FP = ((qr * R["tau"]) @ P2
          + qr[af] * (1.0 - R["tau"][af]))
    B = FP - A
    C = delta - FP
    return A, B, C, P2


def m4_kernel(R, e0, e1, P2):
    """M4: FD Hessian of the gap at the PNT point in the frozen
    K_SUB-dimensional residual subspace, at the critical alias."""
    ms = int(np.argmin(e1["G"]))
    m_f = int(R["al_f"][ms])
    y_m = np.array([R["x"][m_f]])
    qt, r, d0, h = R["qt"], R["r"], R["d0"], R["h"]
    cand = np.argsort(-np.abs(qt * r), kind="stable")
    safe = (np.abs(d0) >= MASK_SAFE * FD_ETA * np.abs(r)) \
        & (qt > 0.0)
    idx, skipped = [], 0
    for f in cand:
        if len(idx) == K_SUB:
            break
        if safe[f]:
            idx.append(int(f))
        else:
            skipped += 1
    idx = np.array(idx)

    def phi(svec):
        dv = d0.copy()
        dv[idx] += svec * r[idx]
        pos = (dv > 0.0) & (qt > 0.0)
        al, be, m0, steps = lanczos_chain(
            R["x"][pos], (qt * dv)[pos], h + 1)
        if steps < h + 1:
            return None
        P = eval_chain(al, be, m0, y_m, h)
        lam = 1.0 / float(np.sum(P ** 2))
        return lam - qt[m_f] * max(-dv[m_f], 0.0)

    K = len(idx)
    base = phi(np.zeros(K))
    if base is None:
        return None
    H = np.zeros((K, K))
    g = np.zeros(K)
    diag2 = np.zeros(K)
    for i in range(K):
        for eta, tgt in ((FD_ETA, H), (0.5 * FD_ETA, diag2)):
            sp = np.zeros(K)
            sp[i] = eta
            fp, fm = phi(sp), phi(-sp)
            if fp is None or fm is None:
                return None
            if eta == FD_ETA:
                g[i] = (fp - fm) / (2.0 * eta)
                H[i, i] = (fp - 2.0 * base + fm) / eta ** 2
            else:
                diag2[i] = (fp - 2.0 * base + fm) / eta ** 2
    for i in range(K):
        for k in range(i + 1, K):
            s = np.zeros(K)
            vals = {}
            for si in (+1.0, -1.0):
                for sk in (+1.0, -1.0):
                    s[:] = 0.0
                    s[i] = si * FD_ETA
                    s[k] = sk * FD_ETA
                    v = phi(s)
                    if v is None:
                        return None
                    vals[(si, sk)] = v
            H[i, k] = H[k, i] = (
                vals[(1, 1)] - vals[(1, -1)] - vals[(-1, 1)]
                + vals[(-1, -1)]) / (4.0 * FD_ETA ** 2)
    drift = np.abs(diag2 - np.diag(H)) / np.maximum(
        np.abs(np.diag(H)), 1e-300)
    eig = np.linalg.eigvalsh(0.5 * (H + H.T))
    emin, emax = float(eig[0]), float(eig[-1])
    if emin >= -EIG_TOL * max(emax, 0.0) and emax > 0.0:
        lab = "KERNEL-PSD"
    elif emax <= EIG_TOL * max(-emin, 0.0) and emin < 0.0:
        lab = "KERNEL-NSD"
    else:
        lab = "KERNEL-INDEFINITE"
    fd_unstable = float(np.median(drift)) > FD_DRIFT_BAR
    if fd_unstable:
        lab += "(FD-UNSTABLE)"
    # envelope first-variation cross-check (fixed mask, exact)
    env = (qt[idx] * r[idx] * (d0[idx] > 0.0) * P2[idx, ms]
           + np.where(idx == m_f,
                      qt[m_f] * r[m_f] * (d0[m_f] < 0.0), 0.0))
    env_dev = np.abs(g - env) / np.maximum(np.abs(env), 1e-300)
    return dict(idx=idx, skipped=skipped, ms=ms, H=H, g=g, eig=eig,
                emin=emin, emax=emax, label=lab,
                drift_med=float(np.median(drift)),
                rHr=float(np.ones(len(idx)) @ H @ np.ones(len(idx))),
                gT1=float(np.sum(g)),
                env_dev_med=float(np.median(env_dev)),
                env_dev_max=float(np.max(env_dev)))


def main():
    section("PRIME.CASE.SIGNEDHOMOTOPY.01 -- signed homotopy "
            "identity + gain-kernel classification (EXPLORATION "
            "ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s"
          % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
    print("    NO RH claim; no marker moves.")

    print("\nS0 -- firewall + self-tests")
    check("S0.1 AST firewall clean", not ast_scan(BANNED_IDS),
          kill="PIPELINE")

    section("B0 -- rungs (homotopy geometry; crossings are exact "
            "rationals t* = -d_PNT/r)")
    RG = {}
    for kz in RUNGS:
        R = build_homotopy(kz)
        RG[kz] = R
        wp = widest_piece(R)
        print("    kz %-3d h %4d F %5d: crossings %4d  zone aliases "
              "%3d (a <= h^1.4 = %8.0f)  widest piece [%.4f, %.4f]"
              % (kz, R["h"], R["F"], len(R["breaks"]),
                 len(R["al_f"]), R["h"] ** 1.4, wp[0], wp[1]),
              flush=True)
    order = sorted(RUNGS, key=lambda kz: RG[kz]["h"])
    ok_al = all(len(RG[kz]["al_f"]) > 0 for kz in RUNGS)
    check("B0.1 zone alias sets nonempty on every rung", ok_al,
          kill="PIPELINE")
    if not ok_al:
        return finish(None, None, None)

    # S0.2 endpoint reconstruction vs verbatim folded_measure (kz 9)
    R9 = RG[9]
    dev_end = 0.0
    for tv, c_at in ((1.0, None), (0.0, None)):
        dv = R9["d1"] if tv == 1.0 else R9["d0"]
        # rebuild the FULL arm density for the verbatim route
        L = R9["L"]
        d_full = np.concatenate([dv, dv[-2:0:-1]])
        xs, ws, _uf = folded_measure(d_full, L, +1.0)
        ys, vs, uf_n = folded_measure(d_full, L, -1.0)
        al, be, m0, steps = lanczos_chain(xs, ws, R9["h"] + 1)
        if steps < R9["h"] + 1:
            check("S0.2 endpoint chain (verbatim route)", False,
                  kill="PIPELINE")
            return finish(None, None, None)
        Pn = eval_chain(al, be, m0, R9["y_al"], R9["h"])
        lam_ref = 1.0 / np.sum(Pn ** 2, axis=1)
        pos_map = {int(f): float(v) for f, v in zip(uf_n, vs)}
        nu_ref = np.array([pos_map.get(int(f), 0.0)
                           for f in R9["al_f"]])
        e = eval_t(R9, tv, need_J=False)
        if e is None:
            check("S0.2 endpoint chain (qt route)", False,
                  kill="PIPELINE")
            return finish(None, None, None)
        dev_end = max(dev_end, float(np.max(
            np.abs(e["lam"] / lam_ref - 1.0))))
        dev_end = max(dev_end, float(np.max(
            np.abs(e["nu"] - nu_ref)
            / np.maximum(np.abs(nu_ref), 1e-300))))
    check("S0.2 endpoint reconstruction == verbatim folded route "
          "(kz 9, t = 0 and 1)", dev_end <= TOL_SELF_END,
          "rel sup dev %.2e" % dev_end, kill="PIPELINE")

    section("E -- exact endpoints per rung: G_m(t) = lambda_{t,m} - "
            "nu_{t,m}, gain Delta_m = G_m(1) - G_m(0)")
    RES = {}
    ok_e = True
    qf_worst = 0.0
    for kz in order:
        R = RG[kz]
        e0 = eval_t(R, 0.0, need_J=False, qf=True)
        e1 = eval_t(R, 1.0, need_J=False, qf=True)
        if e0 is None or e1 is None:
            ok_e = False
            print("    kz %-3d: CHAIN SHORT at an endpoint" % kz)
            break
        qf_worst = max(qf_worst, e0["qf_dev"], e1["qf_dev"])
        delta = e1["G"] - e0["G"]
        RES[kz] = dict(e0=e0, e1=e1, delta=delta,
                       ms=int(np.argmin(e1["G"])))
        ms = RES[kz]["ms"]
        print("    kz %-3d h %4d (n_al %2d): G0 min %+.3e med %+.3e"
              " | G1 min %+.3e med %+.3e | Delta min %+.3e med "
              "%+.3e | m* %d: G0 %+.3e -> G1 %+.3e"
              % (kz, R["h"], len(R["al_f"]),
                 float(np.min(e0["G"])), float(np.median(e0["G"])),
                 float(np.min(e1["G"])), float(np.median(e1["G"])),
                 float(np.min(delta)), float(np.median(delta)),
                 ms + 1, float(e0["G"][ms]), float(e1["G"][ms])),
              flush=True)
    check("E0 endpoint chains complete on all rungs", ok_e,
          kill="PIPELINE")
    check("S0.3 quadratic-form self-test (sum w p*^2 == lambda, "
          "both endpoints, all rungs)", ok_e
          and qf_worst <= TOL_QF, "worst rel dev %.2e" % qf_worst,
          kill="PIPELINE")
    if not ok_e:
        return finish(None, None, None)

    section("M1 -- THE IDENTITY WARD (heavy: full crossing split; "
            "deep: widest-piece GL-%d, disclosed)" % GL_DEEP_PIECE)
    ward_ok = True
    for kz in order:
        R = RG[kz]
        t_a = time.time()
        fd_txt = ""
        if kz in HEAVY:
            out = integrate_pieces(R, 0.0, 1.0)
            if out is None:
                check("M1 chains complete (kz %d)" % kz, False,
                      kill="PIPELINE")
                return finish(None, None, None)
            I, AbsI, n_ev = out
            tgt = RES[kz]["delta"]
            lam_ab = RES[kz]["e0"]["lam"] + RES[kz]["e1"]["lam"]
            mode = "FULL  (%4d pieces, %5d chains)" % (
                len(R["breaks"]) + 1, n_ev)
        else:
            lo, hi = widest_piece(R)
            out = integrate_pieces(R, lo, hi, orders_by_width=False,
                                   fixed_order=GL_DEEP_PIECE)
            ea = eval_t(R, lo, need_J=False)
            eb = eval_t(R, hi, need_J=False)
            if out is None or ea is None or eb is None:
                check("M1 chains complete (kz %d)" % kz, False,
                      kill="PIPELINE")
                return finish(None, None, None)
            I, AbsI, n_ev = out
            tgt = eb["G"] - ea["G"]
            lam_ab = ea["lam"] + eb["lam"]
            mode = "PIECE [%.4f, %.4f] (%d chains)" % (lo, hi,
                                                       n_ev + 2)
            # v2 pointwise ward: J vs central FD at the midpoint
            tm = 0.5 * (lo + hi)
            em = eval_t(R, tm)
            ep = eval_t(R, tm + FD_WARD_EPS, need_J=False)
            en = eval_t(R, tm - FD_WARD_EPS, need_J=False)
            if em is None or ep is None or en is None:
                check("M1 chains complete (kz %d)" % kz, False,
                      kill="PIPELINE")
                return finish(None, None, None)
            fd = (ep["G"] - en["G"]) / (2.0 * FD_WARD_EPS)
            fd_rel = float(np.max(np.abs(fd - em["J"])
                                  / np.maximum(np.abs(em["J"]),
                                               1e-300)))
            ward_ok &= fd_rel <= TOL_FD_WARD
            fd_txt = "  FD ward %.2e" % fd_rel
        rel = np.abs(I - tgt) / np.maximum(np.maximum(
            np.maximum(np.abs(tgt), AbsI), lam_ab), 1e-300)
        wmax = float(np.max(rel))
        RES[kz]["ward"] = wmax
        ward_ok &= wmax <= TOL_WARD
        print("    kz %-3d h %4d: %s  max rel err %.2e%s  [%.1f s]"
              % (kz, R["h"], mode, wmax, fd_txt,
                 time.time() - t_a), flush=True)
    check("M1.1 identity ward: max rel err <= %.0e (deep pointwise"
          " FD <= %.0e) on every rung/alias"
          % (TOL_WARD, TOL_FD_WARD), ward_ok, kill="WARD")

    section("M2 -- POINTWISE SIGN CENSUS of J on the frozen t-grid "
            "(%d heavy / %d deep points)" % (N_T_HEAVY, N_T_DEEP))
    worst = (0.0, None, None, None)          # (J, kz, alias, t)
    n_neg_tot = 0
    n_tot = 0
    census_ok = True
    for kz in order:
        R = RG[kz]
        t_a = time.time()
        n_t = N_T_HEAVY if kz in HEAVY else N_T_DEEP
        tt = np.linspace(0.0, 1.0, n_t)
        JJ = np.zeros((n_t, len(R["al_f"])))
        for i, tv in enumerate(tt):
            e = eval_t(R, tv)
            if e is None:
                check("M2 chains complete (kz %d)" % kz, False,
                      kill="PIPELINE")
                return finish(None, None, None)
            JJ[i] = e["J"]
        frac = np.mean(JJ < 0.0, axis=0)
        RES[kz]["frac_neg"] = frac
        census_ok &= bool(np.max(frac) <= PSD_EXCURSION)
        n_neg_tot += int(np.sum(JJ < 0.0))
        n_tot += JJ.size
        i0, m0i = np.unravel_index(int(np.argmin(JJ)), JJ.shape)
        if float(JJ[i0, m0i]) < worst[0]:
            worst = (float(JJ[i0, m0i]), kz, m0i + 1,
                     float(tt[i0]))
        print("    kz %-3d h %4d: frac(J<0) max %.3f med %.3f | "
              "min J %+.3e at (m %d, t %.2f) | med |J| %.2e  "
              "[%.1f s]"
              % (kz, R["h"], float(np.max(frac)),
                 float(np.median(frac)), float(JJ[i0, m0i]),
                 m0i + 1, float(tt[i0]),
                 float(np.median(np.abs(JJ))), time.time() - t_a),
              flush=True)
    print("    global census: %d / %d samples negative (%.2f%%); "
          "worst J %+.3e at (kz %s, alias %s, t %s)"
          % (n_neg_tot, n_tot, 100.0 * n_neg_tot / max(n_tot, 1),
             worst[0], worst[1], worst[2], worst[3]))
    check("M2.1 census recorded (measurement; PSD bar %.0f%% per "
          "rung/alias: %s)" % (100 * PSD_EXCURSION,
                               "met" if census_ok else "NOT met"),
          True)

    section("M3 -- DECOMPOSITION (closed form): Delta = FIXED(A) + "
            "CROSSING(B) + RESPONSE(C)")
    sh_cross_all = []
    A_min_all = float("inf")
    for kz in order:
        R = RG[kz]
        e0, delta = RES[kz]["e0"], RES[kz]["delta"]
        A, B, C, P2 = decompose(R, e0, delta)
        RES[kz].update(A=A, B=B, C=C, P2=P2)
        A_min_all = min(A_min_all, float(np.min(A)))
        ms = RES[kz]["ms"]
        pos = delta > 0.0
        shB = B[pos] / delta[pos]
        sh_cross_all.extend(shB.tolist())
        print("    kz %-3d h %4d m*=%2d: Delta %+.3e = A %+.3e "
              "(%.0f%%) + B %+.3e (%.0f%%) + C %+.3e (%.0f%%)"
              % (kz, R["h"], ms + 1, float(delta[ms]),
                 float(A[ms]), 100 * A[ms] / delta[ms],
                 float(B[ms]), 100 * B[ms] / delta[ms],
                 float(C[ms]), 100 * C[ms] / delta[ms]))
        print("           medians over m (Delta>0: %d/%d): A/D "
              "%+.3f  B/D %+.3f  C/D %+.3f | min A %+.3e"
              % (int(np.sum(pos)), len(delta),
                 float(np.median(A[pos] / delta[pos])),
                 float(np.median(shB)),
                 float(np.median(C[pos] / delta[pos])),
                 float(np.min(A))), flush=True)
    med_cross = (float(np.median(sh_cross_all)) if sh_cross_all
                 else float("nan"))
    print("    all-rung median crossing share B/Delta = %+.3f "
          "(dominance bar %.2f); min fixed first variation A = "
          "%+.3e" % (med_cross, CROSS_SHARE, A_min_all))
    check("M3.1 decomposition exact (A + B + C == Delta by "
          "construction)", True)

    section("M4 -- QUADRATIC KERNEL at the PNT point (K_SUB = %d "
            "top-|qt r| mask-safe grid modes, eta = %.2f, central "
            "FD; concavity caution: fixed-chamber part must be "
            "NSD)" % (K_SUB, FD_ETA))
    kernel_labels = {}
    kernel_not_psd = False
    for kz in M4_RUNGS:
        t_a = time.time()
        R = RG[kz]
        out = m4_kernel(R, RES[kz]["e0"], RES[kz]["e1"],
                        RES[kz]["P2"])
        if out is None:
            check("M4 chains complete (kz %d)" % kz, False,
                  kill="PIPELINE")
            return finish(None, None, None)
        kernel_labels[kz] = out["label"]
        kernel_not_psd |= not out["label"].startswith("KERNEL-PSD")
        eig = out["eig"]
        print("    kz %-3d (m* %d; subspace f = %s ...; %d skipped "
              "mask-unsafe):" % (kz, out["ms"] + 1,
                                 [int(f) for f in out["idx"][:6]],
                                 out["skipped"]))
        print("      spectrum: %s" % " ".join("%+.2e" % v
                                              for v in eig))
        print("      e_min %+.3e  e_max %+.3e  -> %s | FD eta/2 "
              "med drift %.3f | envelope-vs-FD gradient dev med "
              "%.2e max %.2e"
              % (out["emin"], out["emax"], out["label"],
                 out["drift_med"], out["env_dev_med"],
                 out["env_dev_max"]))
        print("      truth direction: r^T H r %+.3e (second "
              "order), g^T 1 %+.3e (first order)  [%.1f s]"
              % (out["rHr"], out["gT1"], time.time() - t_a),
              flush=True)
    concave_seen = all(lab.startswith("KERNEL-NSD")
                       for lab in kernel_labels.values())
    print("    concavity caution check: fixed-chamber kernel NSD "
          "on all M4 rungs -> %s"
          % ("YES (as the memo predicts: positivity must come "
             "from first order / crossings / nu side)"
             if concave_seen else "NO (see labels above)"))
    check("M4.1 kernel typed: %s"
          % ", ".join("kz %d %s" % (kz, kernel_labels[kz])
                      for kz in M4_RUNGS), True)

    section("M5 -- TYPED CLASSIFICATION (frozen precedence)")
    all_pos = all(bool(np.all(RES[kz]["delta"] > 0.0))
                  for kz in order)
    cross_dom = med_cross > CROSS_SHARE
    if census_ok and all_pos:
        klass = "HOMOTOPY-PSD"
    elif all_pos and cross_dom:
        klass = "HOMOTOPY-CROSSING"
    elif all_pos:
        klass = "HOMOTOPY-AVERAGED"
    elif kernel_not_psd and A_min_all <= 0.0:
        klass = "HOMOTOPY-INDEFINITE-ARITHMETIC"
    else:
        klass = "HOMOTOPY-UNCLASSIFIED"
    flags = []
    if cross_dom:
        flags.append("CROSSING-DOMINANT")
    flags.append("KERNEL={%s}" % ",".join(
        "kz%d:%s" % (kz, kernel_labels[kz]) for kz in M4_RUNGS))
    print("    pointwise PSD (census <= %.0f%% per rung/alias): %s"
          % (100 * PSD_EXCURSION, census_ok))
    print("    all gains Delta > 0 on every rung/alias: %s"
          % all_pos)
    print("    crossing-dominant (median share %.3f > %.2f): %s"
          % (med_cross, CROSS_SHARE, cross_dom))
    print("    kernel not PSD: %s; min fixed first variation "
          "%+.3e" % (kernel_not_psd, A_min_all))
    print("    -> CLASS = %s  [%s]" % (klass, "; ".join(flags)))
    check("M5.1 typed: %s" % klass, True)

    section("C -- controls (kz 9)")
    # (i) scrambled comb: the homotopy must fail to rescue
    rng = np.random.default_rng(SCRAMBLE_SEED)
    us = np.sort(rng.uniform(0.0, 2.0 * R9["alpha"],
                             size=len(R9["uu"])))
    c_s = np.asarray(core.atom_lags_at(R9["alpha"], R9["M"], us,
                                       R9["mm"])[0], float)
    d_s = grid_density(R9["c_ar"] + c_s)[:R9["F"]]
    ff9 = np.arange(R9["F"])
    neg_s = ff9[(ff9 >= 1) & (d_s < 0.0)]
    neg_s = neg_s[np.argsort(R9["a"][neg_s], kind="stable")]
    al_zone = neg_s[R9["a"][neg_s]
                    <= R9["h"] ** (2.0 * THETA_STAR)]
    al_port = neg_s[:CTRL_FALLBACK_AL]     # disclosed fallback
    es_z = (eval_t(R9, 1.0, need_J=False, dens=d_s, al_f=al_zone)
            if len(al_zone) else None)
    es_p = eval_t(R9, 1.0, need_J=False, dens=d_s, al_f=al_port)
    if es_p is None:
        check("C0 scramble chain completes", False,
              kill="PIPELINE")
        return finish(klass, flags, kernel_labels)
    gz = (float(np.min(es_z["G"])) if es_z is not None
          else float("nan"))
    gp = float(np.min(es_p["G"]))
    fires = (gz <= 0.0) if es_z is not None else (gp <= 0.0)
    print("    scramble endpoint gap: zone aliases (%d) min %s%s | "
          "first-%d neg nodes min %+.3e (real kz 9 truth min "
          "%+.3e) -> %s"
          % (len(al_zone),
             ("%+.3e" % gz) if es_z is not None else "n/a (empty",
             "" if es_z is not None else " -> frozen fallback)",
             CTRL_FALLBACK_AL, gp,
             float(np.min(RES[9]["e1"]["G"])),
             "FIRES" if fires else "SILENT"), flush=True)
    check("C1 value control fires (scrambled comb: homotopy fails "
          "to rescue, min gap <= 0)", fires, kill="CONTROL")
    # (ii) sign-preserving cellwise scaling (reported)
    mod = (3.0 + np.cos(2.0 * math.pi * ff9 / R9["L"])) / 8.0
    rp = mod * R9["r"]
    ms9 = RES[9]["ms"]
    g0 = float(RES[9]["e0"]["G"][ms9])
    dd = []
    for s in CTRL_SCALES:
        ep = eval_t(R9, 0.0, need_J=False, dens=R9["d0"] + s * rp)
        if ep is None:
            check("C2 perturbation chain completes", False,
                  kill="PIPELINE")
            return finish(klass, flags, kernel_labels)
        dd.append(float(ep["G"][ms9]) - g0)
    if dd[0] != 0.0 and dd[0] * dd[1] > 0.0:
        phat = math.log2(dd[1] / dd[0])
        lab = ("FIRST-ORDER-DOMINATED"
               if abs(phat - 1.0) < LINEAR_BAND else "SUPERLINEAR")
        det = "Delta(0.5)=%+.3e Delta(1)=%+.3e p-hat=%.3f" % (
            dd[0], dd[1], phat)
    else:
        lab = "SIGN-CHANGE (no clean exponent)"
        det = "Delta(0.5)=%+.3e Delta(1)=%+.3e" % (dd[0], dd[1])
    print("    sign-preserving cellwise gain scaling at m*: %s -> "
          "%s" % (det, lab))
    check("C2 scaling control reported: %s" % lab, True)

    return finish(klass, flags, kernel_labels)


def finish(klass, flags, kernel_labels):
    section("V -- FROZEN VERDICT")
    n_pass = sum(1 for _n, okk in CHECKS if okk)
    n_tot = len(CHECKS)
    if "PIPELINE" in KILLS:
        VERDICT = "PIPELINE-BROKEN"
    elif "WARD" in KILLS:
        VERDICT = "WARD-BROKEN"
    elif "CONTROL" in KILLS:
        VERDICT = "CONTROL-DEAD"
    else:
        VERDICT = "HOMOTOPY-MEASURED"
    sub = []
    if klass:
        sub.append("CLASS=%s" % klass)
    if flags:
        sub.extend(flags)
    print("\n  VERDICT: %s%s"
          % (VERDICT, (" (%s)" % "; ".join(sub)) if sub else ""))
    if VERDICT == "HOMOTOPY-MEASURED" and klass:
        if klass in ("HOMOTOPY-PSD", "HOMOTOPY-CROSSING"):
            print("  PLAIN ANSWER: the diagonal route stays "
                  "unconditional-shaped (%s)."
                  % ("pointwise-positive gain" if klass ==
                     "HOMOTOPY-PSD" else
                     "deterministic mask-monotonicity candidate"))
        elif klass == "HOMOTOPY-AVERAGED":
            print("  PLAIN ANSWER: positivity only in the "
                  "t-average -- the diagonal route survives but "
                  "needs the integrated gain, not a pointwise "
                  "kernel.")
        elif klass == "HOMOTOPY-INDEFINITE-ARITHMETIC":
            print("  PLAIN ANSWER: the input is pair-correlation "
                  "class -- the fixed-mask kernel cannot carry "
                  "the positivity; the diagonal route is "
                  "downgraded.")
        else:
            print("  PLAIN ANSWER: no frozen class fits -- "
                  "reported plainly above.")
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
    ('diagonal_separation_probe', _SRC_0, 8, (), 'DIAGSEP-MEASURED', 0),
    ('christoffel_zone_envelope_probe', _SRC_1, 12, (), 'ZONESPLIT-MEASURED', 0),
    ('christoffel_pnt_gamma_probe', _SRC_2, 10, (), 'PNTGAMMA-MEASURED', 0),
    ('signed_homotopy_probe', _SRC_3, 12, (), 'HOMOTOPY-MEASURED', 0),
)


def run():
    t0 = time.time()
    print("=" * 74)
    print('v889 -- PRIME.PORT.DIAGSEP.01 + PRIME.CASE.ZONESPLIT.01 + PRIME.CASE.PNTGAMMA.01 + PRIME.CASE.SIGNEDHOMOTOPY.01: the four route-deciding measurements -- off-diagonal death of the wall, the theta* = 0.700 zone freeze, PNT-INSUFFICIENT, and the indefinite-arithmetic homotopy kernel')
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
    print("v889: %d/%d pattern gates passed | runtime %.1f s"
          % (sum(gates), len(gates), time.time() - t0))
    print('the routes are decided: the wall dies off-diagonally, the zone freezes at theta* = 0.700, the smooth PNT reference is insufficient, and the required input is pair-correlation class')
    print("[%s] v889 VERDICT GATE" % ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(run())
