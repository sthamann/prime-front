#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""v865 -- PRIME.WEYL.PORT.01 + PRIME.WEYL.READOUT.01: the arithmetic impedance and the repaired readout -- the divisor-tower Weyl load carries the comb at O(1) (the hull's comb-blindness of v863 is REPAIRED at load level: mass doubling moves the Weyl functions at median |dm|/|m| = 0.757/0.456 for variants a/b and the Cayley reflections pointwise at |dr| = 0.220/0.008) and the v1 extremal readout dies by a DIAGNOSED mechanism -- the doubling acts as the near-reparametrization m -> m(z/2)/2 of the r-curve (curve-SET distance 0.0287/0.0017, far below the pointwise motion; any extremal functional reads the curve as a set and is blind to reparametrization; variant b additionally 84 percent boundary-saturated) -- and the REPAIR closes the loop: the fixed-grid and phase readouts see both the doubling and the mapped load at rel >= 1e-3 (the v1 readout saw 4e-5), the reparametrization exactness ward confirms the diagnosis EXACTLY (the mapped load reproduces the rebuilt 2-Lambda tower readouts at <= 1e-10), and the phase readout C passes the tau-connection WITH the mandatory discrimination: kappa band <= 4 across the 5-rung battery AND Epstein kappa = 42.7 / scramble 77.6 OUTSIDE the 1.5x truth window -- ONE TO TWO ORDERS of discrimination where every earlier functional of this chain had Epstein and scramble INSIDE (1444-1485 vs truth 1451-3688), ONE module from two probes (9 checks with the TWO frozen-honest FAILS S1.SPR + S4.RSP kept and pattern-gated, NOT refit + 5/5 checks, verdicts WEYL-PORT-BLIND and READOUT-REPAIRED; discovery probes divisor_weyl_port_probe.py and weyl_readout_repair_probe.py, 2026-08-08, re-run identically at promotion, embedded BYTE-EXACT and executed verbatim, ~3 s).  THE COMBINED MACHINE STATEMENT (every arrow typed): source divisor tower (SOURCE-BUILT: divisibility + own Mangoldt sieve + KMS half-weights, consumes (alpha, Lambda) only -- structural assert on the builder signature) -> Weyl load m_h (Herglotz by construction, Im m > 0 warded on every grid) -> unitary hull (Walsh/mu4/KMS colligation, unitarity 1e-12, closure contractive for EVERY passive load: lam_min(I - Vt*Vt) >= -1e-12) -> repaired readout (SOURCE-DEFINED, frozen grids) -> s_h = kappa tau_h (band <= 4 across 5 rungs; Epstein AND scramble outside).  THE TYPED CAVEAT IS CARRIED VERBATIM (the honesty the verdict must carry): the Spearman(s, tau) signs show the kappa-band leg leans on the NARROW tau range of the 5-rung battery (s anti-tracks tau at -0.8 on variant a) -- the load-bearing content of the pass is the DISCRIMINATION, not the band; REMAINING for a cofinal statement: the kappa law must be DERIVED, not measured; the ladder must extend beyond the 5-rung battery (where the band leg becomes falsifiable); the window-geometry dependence must be explained structurally.  The two frozen FAILS of the port probe are themselves the diagnosis (S1.SPR: variant b's Weyl measure concentrates on ONE pole, n99 = 1 -- no spreading; S4.RSP: the extremal scalar moves at only 4.1e-5/7.3e-7 under doubling -- the blindness the repair then removes); the grid-side |tau|-band intertwiner of v863 remains the other missing piece.  NO RH claim.  Python-only per GATE.WOLFRAM.02.

PROVENANCE: discovery probes divisor_weyl_port_probe.py (9 checks, 2
frozen-honest FAILS S1.SPR + S4.RSP, verdict WEYL-PORT-BLIND with
the v1.1 WHERE-LOST addendum typed in the frozen spec) and
weyl_readout_repair_probe.py (5/5, verdict READOUT-REPAIRED),
2026-08-08, re-run identically at promotion.  ROUND-31 EMBEDDING
CONVENTION: frozen sources embedded BYTE-EXACT and executed verbatim
in isolated namespaces; printed spec SHAs reproduce; byte-equality
ward vs experiments/tfpt-discovery/ inside the pattern gates.  The
probes import the READ-ONLY v563_paper2_readouts.py,
krein_normalform_probe.py (gated in v861) and
redheffer_colligation_probe.py (gated in v863); the repair probe
additionally imports the port probe READ-ONLY -- none re-gated here.

FIREWALL: no zeros, no prime-table oracles; tau enters ONLY as the
comparison series (the chain consumes (alpha, Lambda) only, typed at
freeze); discrimination is part of the pass condition; the two FAILS
are preregistered-honest adjudications on record, bars NOT refit.
NO RH claim.
"""

import contextlib
import io
import math
import os
import re
import sys
import time
import types

_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)

# ------------- frozen probe source divisor_weyl_port_probe (embedded BYTE-EXACT, raw string)
_SRC_0 = r'''
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""divisor_weyl_port_probe -- PRIME.DIVISOR.WEYL.PORT.01: the
arithmetic impedance at the vacuum port.

EXPLORATION ONLY (experiments/): no ledger row, no paper edit, no
.md, nothing outside experiments/.  NO RH claim.  Frozen (spec +
sha256) before running.

THE ARCHITECTURE SHIFT (from COLLIGATION-CONTRACTS-NOT-
IDENTIFIES, redheffer_colligation_probe): the unitary colligation
is the universal PASSIVE HULL -- provably comb-blind (the mass-
doubling ward measured 0.0).  The arithmetic therefore belongs in
the PORT LOAD (the impedance), not the hull.  The candidate load:
the WEYL FUNCTION of the source divisor tower,

    m_h(z) = <Omega, (H_div,h - z)^{-1} Omega>,

automatically Herglotz, spectrally nonlocal (the spreader
property is free), and carrying the comb through Lambda.

THE SOURCE INGREDIENTS (firewall): divisibility, grading, KMS
half-weights, own Mangoldt sieve -- NO target positivity, NO
target Cholesky/eigenvectors, NO fitted couplings.  The tower
height is the window horizon N_h = floor(e^{2 alpha}) (source-
side comb support).  TWO PREDECLARED VARIANTS of the divisor
operator on {1..N_h}:
  (a) the symmetrized half-weighted Mangoldt incidence
      H_a = Lw + Lw^T,  Lw[d, n] = Lambda(n/d) (n/d)^{-1/2}
      for d | n, d < n (the mangoldt_incidence probe's
      L = -[D, log Z] with the KMS half-weight ridden in;
      read-only coordination, own sieve);
  (b) the KMS-weighted graph Laplacian of the divisibility
      graph: edge weight w(d, n) = ell(n/d) (n/d)^{-1/2} for
      proper divisor pairs, ell = Lambda * 1 (Dirichlet), which
      equals log EXACTLY for the truth comb (warded) -- so the
      log-edge weights are Lambda-generated and comb-responsive.
Omega = e_1 (the vacuum divisor n = 1; the register's vacuum
class).  Note: row 1 of Lw IS the deployed comb mass profile
Lambda(n)/sqrt(n) -- the load carries the comb by construction.

THE PORT LOADING (predeclared formula): the load enters through
the Cayley reflection r_h(z) = (m_h(z) - i)/(m_h(z) + i)
(Herglotz => |r| < 1 on Im z > 0: the passivity ward), and the
colligation's vacuum port closes on r instead of 1:

    Vt(r) = V_A + r (1 - D0 r)^{-1} V_B V_C^T,   D0 = 1/4,

the linear-fractional action of the (mu4-weld, design b)
colligation register on the load -- contractive for every
passive load by the unitary-hull property (warded).

THE SCALAR READOUT (decisive; OWN frozen definition, typed: no
softport probe exists in this worktree at freeze time, so the
scalar Feshbach quantity is predeclared here): with the reading
character w (r2 = parity Moebius character, the bare probe's
best machine; r1 = uniform, reported), the scalar transfer
that(z) = w* Vt(r_h(z)) w and the port defect

    s_h = min_{z in ZGRID} (1 - |that(z)|^2),

plus the operator diagnostic s_op = min_z lam_min(I - Vt*Vt).
ZGRID (frozen) = {i y : y in logspace(-1, 1, 21)} union
{x + 0.05 i : x in linspace(-10, 10, 41)}.

THE GATE: s_h ?= kappa_h tau_h with bounded kappa along anchors
kz 9/12/13 + holdouts 14/15 (tau_h = lam_min of the deployed
battery Ah, target-side, used ONLY as the comparison series).
TYPED anti-vacuity honesty: tau varies only ~1.4x across these
rungs, so kappa-stability alone is weak -- the DISCRIMINATION
leg (Epstein + scramble loads must leave the kappa band) carries
the claim; both legs are frozen below.

KILLS/CONTROLS (frozen): anti-comb-blindness (Lambda -> 2 Lambda
must move s_h, rel >= 1e-3 at kz 9, both variants -- the exact
test the bare hull failed at 0.0); structural assert (the tower
builder consumes ONLY (N, Lambda): no target field enters);
colligation regressions (unitarity <= 1e-12; the bare grid-level
closure sigma_max at kz 9 design b/r1 == 0.999025 +- 1e-4, the
frozen run-1 ref); ell = Lambda * 1 == log exact; Herglotz +
passivity wards on the full grid; spreader bar n99 >= 3 (the
number of divisor eigenmodes carrying 99 percent of the Omega
weight) + IPR + the best single-pole rel error (non-monomiality,
reported); Epstein load (Lambda_E via the -Z'/Z recursion,
x^2 + 5 y^2) and scramble load (frozen LCG permutation of
Lambda on {2..N}) at kz 9.

VERDICT (frozen): WEYL-PORT-BLIND (the response kill fires: the
load does not move the machine) / WEYL-PORT-CARRIES (response
holds AND kappa band max/min <= 4 over all 5 rungs for some
variant at readout r2 AND both Epstein and scramble kappa fall
outside [kappa_min/1.5, kappa_max*1.5] of that variant's truth
band) / WEYL-PORT-WRONG-SCALE (response holds but stability or
discrimination fails -- typed which leg).

NO RH claim; v563/sibling probes READ-ONLY; no RNG beyond the
declared frozen LCG scramble; report only.
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

import v563_paper2_readouts as core            # noqa: E402 (READ-ONLY)
import krein_normalform_probe as kn            # noqa: E402 (READ-ONLY)
import redheffer_colligation_probe as rc       # noqa: E402 (READ-ONLY)

T0 = time.time()
FAILS = []
N_CHK = 0

FROZEN_SPEC = """\
PRIME.DIVISOR.WEYL.PORT.01 spec v1 (2026-08-08, frozen before
run).  Tower N_h = floor(e^{2 alpha}); variants (a) symmetrized
half-weighted Mangoldt incidence, (b) KMS graph Laplacian with
ell = Lambda * 1 edge weights, exactly as in the header.  Omega
= e_1.  ZGRID = {iy: y logspace(-1,1,21)} + {x + 0.05i: x
linspace(-10,10,41)}.  Load r = Cayley(m); loading Vt(r) = V_A +
r/(1 - r/4) V_B V_C^T on the design-b register (WH . diag(i^w));
readouts r2 (grading) and r1 (reported).  s_h = min_ZGRID
(1 - |that|^2); s_op reported.  tau_h = lam_min(Ah battery).
Rungs 9/12/13 + 14/15.  Bars: response rel >= 1e-3 (kz9, both
variants); kappa band max/min <= 4 (per variant, r2, all 5
rungs); discrimination: Epstein AND scramble kappa outside
[kmin/1.5, kmax*1.5] at kz9.  Wards: unitarity regression <=
1e-12; bare closure sigma_max(kz9, b/r1) = 0.999025 +- 1e-4;
ell == log exact <= 1e-12 rel; Herglotz Im m > 0 and |r| < 1 on
the whole grid; loaded contraction ||Vt(r)|| <= 1 + 1e-12;
spreader n99 >= 3; structural assert: tower builder signature
(N, lam) only.  Typed: no softport probe in tree at freeze; the
scalar readout is own-frozen.  Typed: narrow tau range =>
discrimination leg carries the claim.  NO RH claim.
ADDENDUM v1.1 (run-1 localization diagnostics, typed; NO bar
moved, run-1 numbers unchanged): the response kill fired at the
READOUT level (s moves by 4e-5/7e-7 under Lambda -> 2 Lambda)
while s_op saturates at 0 to machine precision on every rung --
v1.1 adds the WHERE-LOST diagnostics demanded by the BLIND
verdict enum: (i) the load-level response (median rel change of
m and of r on the grid under doubling and for Epstein/scramble),
(ii) the argmin census of s (which grid point attains the min,
|r| and Im m there), (iii) the boundary-saturation census
(fraction of grid points with |r| > 0.99), (iv) the curve-set
distance (median over the doubled r-curve of the distance to
the truth r-curve as a SET, vs the pointwise median |dr| -- if
set << pointwise the doubling acts as a near-REPARAMETRIZATION
of the same curve, m -> m(z/2)/2, and any extremal functional
of the curve is blind to it).  These localize whether the
arithmetic dies in the load (m insensitive), in the Cayley
reflection, or in the extremal scalar functional."""

ANCHORS = (9, 12, 13)
RUNGS = (9, 12, 13, 14, 15)
BARE_REF_KZ9_B_R1 = 0.999025
KAPPA_BAND = 4.0
DISC_FACTOR = 1.5
RESPONSE_BAR = 1e-3
BANNED_IDS = ("zetazero", "nzeros", "primerange", "isprime",
              "primepi", "nextprime", "prevprime")


def check(name, ok, detail=""):
    global N_CHK
    N_CHK += 1
    if not ok:
        FAILS.append(name.split()[0])
    print("[%s] %s%s" % ("PASS" if ok else "FAIL", name,
                         (": " + detail) if detail else ""))


def ast_scan():
    src = open(os.path.abspath(__file__), encoding="utf-8").read()
    bad = []
    for node in ast.walk(ast.parse(src)):
        nm = None
        if isinstance(node, ast.Name):
            nm = node.id
        elif isinstance(node, ast.Attribute):
            nm = node.attr
        if nm and nm.lower() in BANNED_IDS:
            bad.append(nm)
    return bad


# ---------------------------------------------------------- source tower
def mangoldt(N):
    """Own sieve: Lambda(n) for n <= N."""
    spf = np.zeros(N + 1, dtype=int)
    for p in range(2, N + 1):
        if spf[p] == 0:
            spf[p::p] = np.where(spf[p::p] == 0, p, spf[p::p])
    lam = np.zeros(N + 1)
    for n in range(2, N + 1):
        p = spf[n]
        m = n
        while m % p == 0:
            m //= p
        if m == 1:
            lam[n] = math.log(p)
    return lam


def build_H(N, lam, variant):
    """The divisor operator on {1..N}.  FIREWALL: consumes ONLY
    (N, lam) -- no window/target data ever enters here."""
    H = np.zeros((N, N))
    if variant == "a":
        for n in range(2, N + 1):
            for d in range(1, n):
                if n % d == 0:
                    q = n // d
                    if lam[q]:
                        H[d - 1, n - 1] = lam[q] / math.sqrt(q)
        return H + H.T
    # variant b: ell = lam * 1 (Dirichlet), Laplacian
    ell = np.zeros(N + 1)
    for d in range(2, N + 1):
        if lam[d]:
            ell[d::d] += lam[d]
    A = np.zeros((N, N))
    for n in range(2, N + 1):
        for d in range(1, n):
            if n % d == 0:
                q = n // d
                A[d - 1, n - 1] = A[n - 1, d - 1] = \
                    ell[q] / math.sqrt(q)
    return np.diag(A.sum(axis=1)) - A, ell


def weyl_data(H):
    """Eigen data of the Omega = e_1 spectral measure."""
    ev, V = np.linalg.eigh(H)
    w = V[0, :] ** 2
    return ev, w


def weyl_m(ev, w, z):
    return np.sum(w / (ev - z))


def zgrid():
    ys = np.logspace(-1.0, 1.0, 21)
    xs = np.linspace(-10.0, 10.0, 41)
    return np.concatenate([1j * ys, xs + 0.05j])


def spread_census(ev, w, ZG):
    idx = np.argsort(w)[::-1]
    cs = np.cumsum(w[idx]) / np.sum(w)
    n99 = int(np.searchsorted(cs, 0.99) + 1)
    ipr = float(np.sum(w ** 2) / np.sum(w) ** 2)
    mv = np.array([weyl_m(ev, w, z) for z in ZG])
    k0 = idx[0]
    m1 = np.array([w[k0] / (ev[k0] - z) for z in ZG])
    mono = float(np.linalg.norm(mv - m1) / np.linalg.norm(mv))
    return n99, ipr, mono, mv


# ---------------------------------------------------------- the machine
def closure_blocks():
    W = rc.walsh16()
    W = W @ np.diag([1j ** rc.hamw(S) for S in range(16)])
    return W[1:, 1:], W[1:, 0], W[0, 1:], W[0, 0]


def readout_vec(r):
    if r == "r1":
        return np.ones(15) / math.sqrt(15.0)
    wv = np.array([(-1.0) ** rc.hamw(S) for S in range(1, 16)])
    return wv / np.linalg.norm(wv)


def loaded_scalars(mv, VA, VB, VC, D0):
    """Per grid point: r = Cayley(m); that(z) for both readouts;
    lam_min of the operator defect."""
    rv = (mv - 1j) / (mv + 1j)
    outs = {"r1": [], "r2": []}
    smin_op = np.inf
    w1, w2 = readout_vec("r1"), readout_vec("r2")
    for r_ in rv:
        Vt = VA + (r_ / (1.0 - D0 * r_)) * np.outer(VB, VC)
        for nm, wv in (("r1", w1), ("r2", w2)):
            outs[nm].append(complex(wv.conj() @ Vt @ wv))
        dmin = float(np.linalg.eigvalsh(
            np.eye(15) - Vt.conj().T @ Vt)[0])
        smin_op = min(smin_op, dmin)
    return rv, {k: np.array(v) for k, v in outs.items()}, smin_op


def run():
    print("=" * 78)
    print("DIVISOR WEYL PORT (divisor_weyl_port_probe) -- the "
          "arithmetic impedance at the vacuum port")
    print("=" * 78)
    print("frozen spec sha256 = %s"
          % hashlib.sha256(FROZEN_SPEC.encode()).hexdigest()[:16])
    print("""
HONESTY FRAME: NO RH claim.  The scalar Feshbach readout is
own-frozen (no softport probe in tree at freeze time, typed).
tau enters ONLY as the comparison series; the load is built from
divisibility + Lambda + KMS weights alone (structural assert).""")

    # ============================================================== S0
    print("\nS0 -- firewall + colligation regressions")
    check("S0.AST firewall clean", not ast_scan())
    import inspect
    sig = list(inspect.signature(build_H).parameters)
    check("S0.SIG structural assert: the tower builder consumes "
          "(N, lam, variant) only -- no window/target field in "
          "its signature", sig == ["N", "lam", "variant"])
    gd9 = rc.grid_data(9)
    zph9, _ = rc.zm_phase(gd9["tauj"])
    dev_u = max(rc.unitarity_defect("a", gd9, zph9),
                rc.unitarity_defect("b", gd9, zph9))
    Th, _, _ = rc.machine_That("b", "r1", gd9, zph9)
    smax_bare = float(np.linalg.norm(Th, 2))
    check("S0.REG colligation regressions: unitarity defect "
          "%.1e <= 1e-12 AND bare grid closure sigma_max(kz9, "
          "b/r1) = %.6f == %.6f +- 1e-4 (frozen run-1 ref)"
          % (dev_u, smax_bare, BARE_REF_KZ9_B_R1),
          dev_u <= 1e-12
          and abs(smax_bare - BARE_REF_KZ9_B_R1) <= 1e-4)

    # ============================================================== S1
    print("\nS1 -- the divisor towers + Weyl functions "
          "(spreading census)")
    ZG = zgrid()
    VA, VB, VC, D0 = closure_blocks()
    towers = {}
    ok_ell = True
    ok_hz = True
    ok_spread = True
    for kz in RUNGS:
        rr = core.build_window(kz)
        N = int(math.exp(2.0 * rr["alpha"]))
        lam = mangoldt(N)
        Ha = build_H(N, lam, "a")
        Hb, ell = build_H(N, lam, "b")
        lg = np.log(np.arange(1, N + 1, dtype=float))
        ok_ell &= float(np.max(np.abs(ell[1:] - lg))) <= 1e-12 * \
            max(1.0, float(np.max(np.abs(lg))))
        tau_h = float(np.linalg.eigvalsh(
            np.asarray(rr["Ah"], float))[0])
        towers[kz] = dict(N=N, lam=lam, tau=tau_h)
        for v, H in (("a", Ha), ("b", Hb)):
            ev, w = weyl_data(H)
            n99, ipr, mono, mv = spread_census(ev, w, ZG)
            ok_hz &= bool(np.all(mv.imag > 0.0))
            ok_spread &= n99 >= 3
            towers[kz][v] = dict(ev=ev, w=w, mv=mv, n99=n99,
                                 ipr=ipr, mono=mono)
        ta, tb = towers[kz]["a"], towers[kz]["b"]
        print("    kz %-3d N %-4d tau %.3e | (a) n99 %3d ipr "
              "%.3f mono %.3f | (b) n99 %3d ipr %.3f mono %.3f"
              % (kz, N, tau_h, ta["n99"], ta["ipr"], ta["mono"],
                 tb["n99"], tb["ipr"], tb["mono"]))
    check("S1.ELL ell = Lambda * 1 == log exactly on every "
          "tower (the log-edge weights are Lambda-generated)",
          ok_ell)
    check("S1.HZ Herglotz ward: Im m(z) > 0 at every grid point, "
          "every rung/variant", ok_hz)
    check("S1.SPR spreader bar: n99 >= 3 everywhere (the Weyl "
          "measure spreads over the divisor spectrum; "
          "non-monomiality = best single-pole rel error, "
          "reported above)", ok_spread)

    # ============================================================== S2
    print("\nS2 -- the loaded machine: passivity + contraction "
          "+ the s series")
    stab = {}
    ok_pass = True
    ok_lcon = True
    for kz in RUNGS:
        stab[kz] = {}
        for v in ("a", "b"):
            mv = towers[kz][v]["mv"]
            rv, outs, smin_op = loaded_scalars(mv, VA, VB, VC,
                                               D0)
            ok_pass &= bool(np.all(np.abs(rv) < 1.0))
            ok_lcon &= smin_op >= -1e-12
            stab[kz][v] = dict(
                s_r1=float(np.min(1.0 - np.abs(outs["r1"])
                                  ** 2)),
                s_r2=float(np.min(1.0 - np.abs(outs["r2"])
                                  ** 2)),
                s_op=smin_op)
    check("S2.PAS passivity ward: |r(z)| < 1 on the whole grid, "
          "every rung/variant (Cayley of Herglotz)", ok_pass)
    check("S2.CON loaded contraction ward: lam_min(I - Vt*Vt) "
          ">= -1e-12 for every load (the passive hull stays "
          "contractive under every passive load)", ok_lcon)
    print("    %-6s %-9s %-11s %-11s %-11s %-9s"
          % ("rung", "tau", "s_a(r2)", "s_b(r2)", "s_a(r1)",
             "s_op(a)"))
    for kz in RUNGS:
        print("    kz%-4d %.3e %.5e %.5e %.5e %.3e"
              % (kz, towers[kz]["tau"], stab[kz]["a"]["s_r2"],
                 stab[kz]["b"]["s_r2"], stab[kz]["a"]["s_r1"],
                 stab[kz]["a"]["s_op"]))

    # ============================================================== S3
    print("\nS3 -- the gate: s ?= kappa tau (r2 grading)")
    kappas = {}
    for v in ("a", "b"):
        kap = np.array([stab[kz][v]["s_r2"] / towers[kz]["tau"]
                        for kz in RUNGS])
        kappas[v] = kap
        print("    variant %s: kappa = %s | band max/min = %.2f "
              "(bar %.1f)"
              % (v, " ".join("%.3e" % k for k in kap),
                 float(np.max(kap) / np.min(kap)), KAPPA_BAND))
    stable_v = [v for v in ("a", "b")
                if float(np.max(kappas[v])
                         / np.min(kappas[v])) <= KAPPA_BAND]
    print("    kappa-stable variants: %s" % (stable_v or "none"))

    # ============================================================== S4
    print("\nS4 -- the kills (kz 9)")
    kz = 9
    N9 = towers[9]["N"]
    lam9 = towers[9]["lam"]
    # anti-comb-blindness: Lambda -> 2 Lambda
    resp_ok = True
    resp_txt = []
    diag = {}
    for v in ("a", "b"):
        H2 = build_H(N9, 2.0 * lam9, v)
        if v == "b":
            H2 = H2[0]
        ev2, w2 = weyl_data(H2)
        mv2 = np.array([weyl_m(ev2, w2, z) for z in ZG])
        rv2, outs2, _ = loaded_scalars(mv2, VA, VB, VC, D0)
        s2 = float(np.min(1.0 - np.abs(outs2["r2"]) ** 2))
        s1 = stab[9][v]["s_r2"]
        rel = abs(s2 - s1) / max(abs(s1), 1e-300)
        resp_ok &= rel >= RESPONSE_BAR
        resp_txt.append("%s: %.3e" % (v, rel))
        # v1.1 WHERE-LOST diagnostics (typed, no bar)
        mv1 = towers[9][v]["mv"]
        rv1 = (mv1 - 1j) / (mv1 + 1j)
        _, outs1, _ = loaded_scalars(mv1, VA, VB, VC, D0)
        d1 = 1.0 - np.abs(outs1["r2"]) ** 2
        jmin = int(np.argmin(d1))
        dset = float(np.median(np.min(
            np.abs(rv2[:, None] - rv1[None, :]), axis=1)))
        diag[v] = dict(
            dm=float(np.median(np.abs(mv2 - mv1)
                               / np.abs(mv1))),
            dr=float(np.median(np.abs(rv2 - rv1))),
            dset=dset,
            zmin=complex(ZG[jmin]),
            rmin=float(np.abs(rv1[jmin])),
            immin=float(mv1[jmin].imag),
            fsat=float(np.mean(np.abs(rv1) > 0.99)))
    check("S4.RSP anti-comb-blindness: Lambda -> 2 Lambda moves "
          "s_h (rel %s, bar >= 1e-3) -- the load carries the "
          "comb, the exact quantity the bare hull could not see"
          % ", ".join(resp_txt), resp_ok)
    for v in ("a", "b"):
        dg = diag[v]
        print("    WHERE-LOST (v1.1, variant %s): load-level "
              "response median |dm|/|m| = %.3f, pointwise "
              "|dr| = %.3f, curve-SET distance %.4f; argmin of "
              "s at z = %.2f%+.2fi with |r| = %.6f, Im m = "
              "%.2e; boundary saturation %.0f%%"
              % (v, dg["dm"], dg["dr"], dg["dset"],
                 dg["zmin"].real, dg["zmin"].imag, dg["rmin"],
                 dg["immin"], 100.0 * dg["fsat"]))
    # Epstein + scramble loads
    lamE = kn.lambda_eps(N9)[:N9 + 1]
    seed = 12345

    def lcg_perm(n):
        s = seed
        idx = list(range(2, n + 1))
        for i in range(len(idx) - 1, 0, -1):
            s = (1103515245 * s + 12345) % (1 << 31)
            j = s % (i + 1)
            idx[i], idx[j] = idx[j], idx[i]
        return idx
    perm = lcg_perm(N9)
    lamS = np.zeros(N9 + 1)
    lamS[2:] = lam9[perm]
    alt = {}
    for nm, lm in (("eps", lamE), ("scr", lamS)):
        alt[nm] = {}
        for v in ("a", "b"):
            H_ = build_H(N9, lm, v)
            if v == "b":
                H_ = H_[0]
            ev_, w_ = weyl_data(H_)
            mv_ = np.array([weyl_m(ev_, w_, z) for z in ZG])
            _, outs_, _ = loaded_scalars(mv_, VA, VB, VC, D0)
            s_ = float(np.min(1.0 - np.abs(outs_["r2"]) ** 2))
            alt[nm][v] = s_ / towers[9]["tau"]
    disc = {}
    for v in ("a", "b"):
        kmin, kmax = float(np.min(kappas[v])), \
            float(np.max(kappas[v]))
        lo, hi = kmin / DISC_FACTOR, kmax * DISC_FACTOR
        outE = not (lo <= alt["eps"][v] <= hi)
        outS = not (lo <= alt["scr"][v] <= hi)
        disc[v] = outE and outS
        print("    variant %s: truth kappa band [%.3e, %.3e] "
              "-> disc window [%.3e, %.3e]; Epstein kappa "
              "%.3e (%s), scramble kappa %.3e (%s)"
              % (v, kmin, kmax, lo, hi, alt["eps"][v],
                 "OUT" if outE else "IN", alt["scr"][v],
                 "OUT" if outS else "IN"))

    # ============================================================== S5
    print("\nS5 -- verdict")
    carrying = [v for v in stable_v if disc[v]]
    if not resp_ok:
        verdict = "WEYL-PORT-BLIND"
    elif carrying:
        verdict = "WEYL-PORT-CARRIES"
    else:
        verdict = "WEYL-PORT-WRONG-SCALE"
    print("=" * 78)
    print("V -- VERDICT: %s%s" % (verdict,
          (" (variant %s)" % ",".join(carrying))
          if carrying else ""))
    print("=" * 78)
    if verdict == "WEYL-PORT-BLIND":
        dga, dgb = diag["a"], diag["b"]
        print("""    THE TYPED LOCALIZATION (the verdict enum's demand): the
    arithmetic is NOT lost in the load -- the Weyl functions
    respond at O(1) to the mass doubling (median |dm|/|m| =
    %.3f / %.3f for variants a/b) and the Cayley reflections
    move pointwise (|dr| = %.3f / %.3f).  It is lost in the
    SCALAR READOUT, by TWO measured mechanisms: (1) the
    doubling acts as m -> m(z/2)/2, a near-REPARAMETRIZATION
    of the r-curve -- the curve-set distance is %.4f / %.4f,
    far below the pointwise motion, and any extremal
    functional of the curve (our min-extraction) is blind to
    reparametrization; (2) for variant b additionally %.0f%%
    of the grid is boundary-saturated (|r| > 0.99, where
    Herglotz normalization makes the load universal), and the
    operator defect saturates at 0 exactly because a
    unimodular load closes the unitary hull back to norm 1.
    HONEST CONSEQUENCE: the port-impedance architecture DOES
    transport arithmetic into the machine -- the load-level
    response repairs the hull's comb-blindness, which is the
    named positive of this wave -- but the vacuum-slot
    extremal defect is the wrong functional: it reads the
    curve as a set, not the arithmetic parametrization along
    it.  The typed next object is a readout that samples the
    load at FIXED interior points (or integrates the defect
    against the divisor spectral measure), so the
    parametrization -- where the arithmetic lives -- enters;
    the grid-side band intertwiner of the colligation probe
    remains the other missing piece.""" % (
            dga["dm"], dgb["dm"], dga["dr"], dgb["dr"],
            dga["dset"], dgb["dset"], 100.0 * dgb["fsat"]))
    if verdict == "WEYL-PORT-WRONG-SCALE":
        legs = []
        if not stable_v:
            legs.append("the kappa band fails for BOTH variants "
                        "(s does not track tau across the "
                        "ladder)")
        else:
            legs.append("kappa-stable variant(s) %s exist but "
                        "the discrimination leg fails (Epstein/"
                        "scramble loads land INSIDE the truth "
                        "band -- with the narrow tau range this "
                        "was the honesty-carrying leg, typed at "
                        "freeze)" % stable_v)
        print("""    THE TYPED OUTCOME: the load responds (the arithmetic
    reaches the machine -- the comb-blindness of the bare hull
    is REPAIRED at the port, the named result of the response
    kill), the Weyl functions are genuinely spreading Herglotz
    loads and every loaded closure stays contractive; but the
    scalar port defect is NOT the tau-margin in disguise:
    %s.  HONEST CONSEQUENCE: the
    arithmetic impedance EXISTS as a passive load and moves the
    machine, but the vacuum-slot scalar readout at this register
    does not measure the window floor; the typed gap is the
    READOUT, not the load -- the next named object is a port
    functional whose defect provably compresses the window form
    (the grid-side band intertwiner remains the missing piece,
    as typed by the colligation probe).""" % "; ".join(legs))
    dt = time.time() - T0
    print("-" * 78)
    print("checks: %d run, %d failed%s | runtime %.1f min"
          % (N_CHK, len(FAILS),
             (" [" + ", ".join(FAILS) + "]") if FAILS else "",
             dt / 60.0))
    print("NO RH claim; report only; nothing outside "
          "experiments/ touched.")


if __name__ == "__main__":
    run()
'''
# ------------- frozen probe source weyl_readout_repair_probe (embedded BYTE-EXACT, raw string)
_SRC_1 = r'''
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""weyl_readout_repair_probe -- PRIME.DIVISOR.WEYL.PORT.02: the
readout repair.

EXPLORATION ONLY (experiments/): no ledger row, no paper edit, no
.md, nothing outside experiments/.  NO RH claim.  Frozen (spec +
sha256) before running.

THE TYPED BREAK BEING REPAIRED (divisor_weyl_port_probe, verdict
WEYL-PORT-BLIND): the arithmetic ARRIVES in the load (Weyl
response O(1), reflections move pointwise 0.22) but the v1
scalar functional -- the extremal min over a z-grid -- reads the
reflection curve as a SET (curve-set distance 0.029 vs pointwise
0.22): the mass doubling acts EXACTLY as the reparametrization
m -> m(z/2)/2 (resolvent identity (2H - z)^{-1} =
(H - z/2)^{-1}/2, so m_{2H}(z) = m_H(z/2)/2 -- exact, used as a
pipeline ward below), and extremal curve functionals are
reparametrization-blind by construction.

THE THREE REPAIRED READOUTS (all predeclared, source-only, no
target data, the r2 parity character fixed from v1):
  (A) FIXED-POINT SAMPLING: the loaded defect d(z) = 1 -
      |that(r(z))|^2 evaluated on the frozen rational interior
      grid ZFIX = {i/4, i/2, i, 2i, 4i, +-1 + i/2, +-2 + i/2,
      +-1/2 + i/2} (11 points, NOT tuned); vector R_A, scalar
      s_A = mean.
  (B) MEASURE-WEIGHTED: s_B = sum_k w_k d(lam_k + i eps) /
      sum_k w_k with (lam_k, w_k) the divisor operator's OWN
      vacuum spectral measure, eps = 0.05 frozen -- the
      parametrization-carrying integral of the v1 diagnosis.
  (C) PHASE-SENSITIVE: R_C = arg r(z) on ZFIX; scalar s_C = the
      total phase variation sum |d arg r| along z = iy, y in
      logspace(1/4, 4, 33) (frozen window; the endpoint-window
      makes even the curve integral parametrization-sensitive,
      typed).
STRUCTURAL HONESTY (pre-typed): the whole chain consumes ONLY
(alpha, Lambda) -- the window geometry (h, M, D, battery) never
enters the load -- so a kappa tau match WITHOUT control
discrimination would be an alpha-law coincidence; the
discrimination bar is therefore part of the pass condition (the
v1 vacuous-band failure must not recur).

THE GATES (frozen):
  G1 ANTI-BLINDNESS per readout: Lambda -> 2 Lambda moves the
     readout by rel >= 1e-3 (vector norms for R_A/R_C, scalars
     for s_A/s_B/s_C); PLUS the reparametrization ward: the
     readouts on the mapped load m(z/2)/2 must equal the
     readouts on the rebuilt 2 Lambda tower to rel <= 1e-10
     (exactness of the diagnosis) and differ from the truth by
     >= 1e-3 (the repaired readouts SEE the map the v1 min
     could not).
  G2 TAU-CONNECTION per (tower variant, readout): kappa_h =
     s_h / tau_h over anchors kz 9/12/13 + holdouts 14/15;
     PASS iff band max/min <= 4 AND Epstein AND scramble kappa
     (kz 9) BOTH outside [kmin/1.5, kmax*1.5].  Spearman(s,
     tau) and Spearman(s, alpha) reported for the localization
     iteration.
CONTROLS: v1 regressions (frozen run-1 refs: s_min(kz9, a, r2)
= 8.68463e-01 +- 1e-5; Herglotz/passivity/contraction re-warded
on the new grids; load-level response median |dm|/|m| >= 0.1 at
ZFIX); Epstein (Lambda_E, -Z'/Z recursion) and scramble (frozen
LCG permutation, seed 12345 as v1) loads per readout.

VERDICT (frozen): READOUT-REPAIRED (some (variant, readout)
passes G1 + G2 -- the impedance architecture closes its loop) /
READOUT-SEES-NOT-TAU (G1 passes for >= 1 readout, G2 fails
everywhere -- iterated localization typed: where does the
arithmetic get lost NOW) / READOUT-STILL-BLIND (G1 fails
everywhere -- typed why).

NO RH claim; v563 + sibling probes READ-ONLY; no RNG beyond the
declared frozen LCG scramble; report only.
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

import v563_paper2_readouts as core            # noqa: E402 (READ-ONLY)
import krein_normalform_probe as kn            # noqa: E402 (READ-ONLY)
import divisor_weyl_port_probe as dw           # noqa: E402 (READ-ONLY)

T0 = time.time()
FAILS = []
N_CHK = 0

FROZEN_SPEC = """\
PRIME.DIVISOR.WEYL.PORT.02 spec v1 (2026-08-08, frozen before
run).  Readouts A/B/C, ZFIX (11 rational interior points), eps =
0.05, phase window y in [1/4, 4] (33 log points), r2 character,
exactly as in the header.  Rungs 9/12/13 + 14/15; tower variants
a (Mangoldt incidence) and b (KMS Laplacian) from v1 read-only.
G1 bars: rel >= 1e-3 per readout (doubling AND the mapped load);
reparametrization exactness ward rel <= 1e-10.  G2 bars: kappa
band max/min <= 4 AND Epstein AND scramble outside [kmin/1.5,
kmax*1.5] -- discrimination REQUIRED for the pass (typed: the
chain consumes only (alpha, Lambda); without discrimination any
kappa tau match is an alpha-law coincidence).  Controls: v1
frozen refs (s_min kz9/a/r2 = 8.68463e-01 +- 1e-5), Herglotz/
passivity/contraction on the new grids, load response >= 0.1 at
ZFIX, Epstein/scramble seed 12345.  Verdict enum as header.  NO
RH claim; report only."""

RUNGS = (9, 12, 13, 14, 15)
V1_SMIN_REF = 8.68463e-01
G1_BAR = 1e-3
EXACT_BAR = 1e-10
KAPPA_BAND = 4.0
DISC_FACTOR = 1.5
EPS_B = 0.05
ZFIX = np.array([0.25j, 0.5j, 1j, 2j, 4j,
                 1 + 0.5j, -1 + 0.5j, 2 + 0.5j, -2 + 0.5j,
                 0.5 + 0.5j, -0.5 + 0.5j])
YPH = np.logspace(math.log10(0.25), math.log10(4.0), 33)
BANNED_IDS = ("zetazero", "nzeros", "primerange", "isprime",
              "primepi", "nextprime", "prevprime")


def check(name, ok, detail=""):
    global N_CHK
    N_CHK += 1
    if not ok:
        FAILS.append(name.split()[0])
    print("[%s] %s%s" % ("PASS" if ok else "FAIL", name,
                         (": " + detail) if detail else ""))


def ast_scan():
    src = open(os.path.abspath(__file__), encoding="utf-8").read()
    bad = []
    for node in ast.walk(ast.parse(src)):
        nm = None
        if isinstance(node, ast.Name):
            nm = node.id
        elif isinstance(node, ast.Attribute):
            nm = node.attr
        if nm and nm.lower() in BANNED_IDS:
            bad.append(nm)
    return bad


# ---------------------------------------------------------- readouts
def spearman(x, y):
    def rk(v):
        o = np.argsort(v)
        r = np.empty(len(v))
        r[o] = np.arange(len(v))
        return r
    a, b = rk(np.asarray(x)), rk(np.asarray(y))
    a -= a.mean()
    b -= b.mean()
    den = math.sqrt(float(a @ a) * float(b @ b))
    return float(a @ b) / max(den, 1e-300)


class Load(object):
    """A Weyl load: eigen data (ev, w) -> m(z), r(z)."""

    def __init__(self, ev, w):
        self.ev, self.w = ev, w

    def m(self, z):
        return np.array([np.sum(self.w / (self.ev - zz))
                         for zz in np.atleast_1d(z)])

    def r(self, z):
        mv = self.m(z)
        return (mv - 1j) / (mv + 1j)


class MappedLoad(object):
    """The measured reparametrization m -> m(z/2)/2 applied to a
    base load (NO tower rebuild -- the map itself)."""

    def __init__(self, base):
        self.base = base
        self.ev, self.w = base.ev, base.w   # for readout B grid

    def m(self, z):
        return 0.5 * self.base.m(np.atleast_1d(z) / 2.0)

    def r(self, z):
        mv = self.m(z)
        return (mv - 1j) / (mv + 1j)


def defect_at(load, z, VA, VB, VC, D0, w2):
    rv = load.r(z)
    out = []
    for r_ in rv:
        Vt = VA + (r_ / (1.0 - D0 * r_)) * np.outer(VB, VC)
        out.append(1.0 - abs(complex(w2.conj() @ Vt @ w2)) ** 2)
    return np.array(out), rv


def readouts(load, VA, VB, VC, D0, w2):
    """R_A, s_A, s_B, R_C, s_C for one load."""
    dA, rA = defect_at(load, ZFIX, VA, VB, VC, D0, w2)
    s_A = float(np.mean(dA))
    zb = load.ev + 1j * EPS_B
    dB, _ = defect_at(load, zb, VA, VB, VC, D0, w2)
    s_B = float(np.sum(load.w * dB) / np.sum(load.w))
    R_C = np.angle(rA)
    rph = load.r(1j * YPH)
    dphi = np.angle(rph[1:] / rph[:-1])
    s_C = float(np.sum(np.abs(dphi)))
    return dict(R_A=dA, s_A=s_A, s_B=s_B, R_C=R_C, s_C=s_C,
                r_fix=rA)


def rel_vec(x, y):
    x, y = np.asarray(x, float), np.asarray(y, float)
    return float(np.linalg.norm(x - y)
                 / max(np.linalg.norm(y), 1e-300))


def rel_sc(x, y):
    return abs(x - y) / max(abs(y), 1e-300)


def run():
    print("=" * 78)
    print("WEYL READOUT REPAIR (weyl_readout_repair_probe) -- "
          "teaching the port to read the parametrization")
    print("=" * 78)
    print("frozen spec sha256 = %s"
          % hashlib.sha256(FROZEN_SPEC.encode()).hexdigest()[:16])
    print("""
HONESTY FRAME: NO RH claim.  All readouts source-only and frozen;
tau enters ONLY as the comparison series; discrimination is part
of the pass condition (the chain consumes only (alpha, Lambda) --
typed at freeze).""")

    # ============================================================== S0
    print("\nS0 -- firewall + v1 regressions")
    check("S0.AST firewall clean", not ast_scan())
    VA, VB, VC, D0 = dw.closure_blocks()
    w2 = dw.readout_vec("r2")
    towers = {}
    taus = {}
    alphas = {}
    for kz in RUNGS:
        rr = core.build_window(kz)
        N = int(math.exp(2.0 * rr["alpha"]))
        alphas[kz] = float(rr["alpha"])
        lam = dw.mangoldt(N)
        Ha = dw.build_H(N, lam, "a")
        Hb, _ = dw.build_H(N, lam, "b")
        taus[kz] = float(np.linalg.eigvalsh(
            np.asarray(rr["Ah"], float))[0])
        towers[kz] = dict(N=N, lam=lam,
                          a=Load(*dw.weyl_data(Ha)),
                          b=Load(*dw.weyl_data(Hb)))
    # v1 regression: the extremal s at kz9 variant a
    ZG1 = dw.zgrid()
    mv1 = towers[9]["a"].m(ZG1)
    _, outs1, _ = dw.loaded_scalars(mv1, VA, VB, VC, D0)
    s_v1 = float(np.min(1.0 - np.abs(outs1["r2"]) ** 2))
    check("S0.REG v1 regression: extremal s(kz9, a, r2) = "
          "%.6e == %.6e +- 1e-5 (frozen run-1 ref)"
          % (s_v1, V1_SMIN_REF),
          abs(s_v1 - V1_SMIN_REF) <= 1e-5)
    ok_hz = True
    ok_pas = True
    for kz in RUNGS:
        for v in ("a", "b"):
            L_ = towers[kz][v]
            for zg in (ZFIX, L_.ev + 1j * EPS_B, 1j * YPH):
                mv = L_.m(zg)
                ok_hz &= bool(np.all(mv.imag > 0))
                ok_pas &= bool(np.all(np.abs(
                    (mv - 1j) / (mv + 1j)) < 1.0))
    check("S0.HZ Herglotz + passivity re-warded on ALL new "
          "readout grids (ZFIX, spectral + i eps, phase "
          "window), every rung/variant", ok_hz and ok_pas)

    # ============================================================== S1
    print("\nS1 -- G1: the anti-blindness table")
    base = {}
    for kz in RUNGS:
        base[kz] = {v: readouts(towers[kz][v], VA, VB, VC, D0,
                                w2) for v in ("a", "b")}
    kz = 9
    N9, lam9 = towers[9]["N"], towers[9]["lam"]
    g1 = {}
    print("    variant readout  doubling-rel  mapped-rel  "
          "exactness")
    for v in ("a", "b"):
        H2 = dw.build_H(N9, 2.0 * lam9, v)
        if v == "b":
            H2 = H2[0]
        L2 = Load(*dw.weyl_data(H2))
        Lm = MappedLoad(towers[9][v])
        rd0 = base[9][v]
        rd2 = readouts(L2, VA, VB, VC, D0, w2)
        # NOTE: readout B of the mapped load uses the BASE
        # spectral grid (the map has no own tower); exactness is
        # therefore warded on A and C, typed.
        rdm = readouts(Lm, VA, VB, VC, D0, w2)
        rows = [
            ("A", rel_vec(rd2["R_A"], rd0["R_A"]),
             rel_vec(rdm["R_A"], rd0["R_A"]),
             rel_vec(rdm["R_A"], rd2["R_A"])),
            ("B", rel_sc(rd2["s_B"], rd0["s_B"]),
             rel_sc(rdm["s_B"], rd0["s_B"]), float("nan")),
            ("C", rel_vec(rd2["R_C"], rd0["R_C"]),
             rel_vec(rdm["R_C"], rd0["R_C"]),
             rel_vec(rdm["R_C"], rd2["R_C"])),
        ]
        for nm, d2_, dm_, ex_ in rows:
            g1[(v, nm)] = dict(dbl=d2_, mapped=dm_, exact=ex_)
            print("    %-7s %-8s %.4e    %.4e  %s"
                  % (v, nm, d2_, dm_,
                     ("%.1e" % ex_) if ex_ == ex_ else "typed"))
    ok_g1 = {k: (d["dbl"] >= G1_BAR and d["mapped"] >= G1_BAR)
             for k, d in g1.items()}
    ok_exact = all(d["exact"] <= EXACT_BAR for k, d in g1.items()
                   if d["exact"] == d["exact"])
    check("S1.EXA reparametrization exactness ward: the mapped "
          "load m(z/2)/2 reproduces the rebuilt 2 Lambda tower "
          "readouts (A, C) to <= 1e-10 -- the v1 diagnosis "
          "(doubling == reparametrization) is EXACT", ok_exact)
    seen = [k for k, ok in ok_g1.items() if ok]
    check("S1.G1 anti-blindness: %d/6 (variant, readout) pairs "
          "see both the doubling and the mapped load at rel >= "
          "1e-3 (v1's extremal readout saw 4e-5) -- passing "
          "pairs: %s" % (len(seen), seen or "none"),
          len(seen) >= 1)

    # ============================================================== S2
    print("\nS2 -- G2: the tau-connection with mandatory "
          "discrimination")
    lamE = kn.lambda_eps(N9)[:N9 + 1]
    seed = 12345

    def lcg_perm(n):
        s = seed
        idx = list(range(2, n + 1))
        for i in range(len(idx) - 1, 0, -1):
            s = (1103515245 * s + 12345) % (1 << 31)
            j = s % (i + 1)
            idx[i], idx[j] = idx[j], idx[i]
        return idx
    lamS = np.zeros(N9 + 1)
    lamS[2:] = lam9[lcg_perm(N9)]
    alt_rd = {}
    for nm, lm in (("eps", lamE), ("scr", lamS)):
        alt_rd[nm] = {}
        for v in ("a", "b"):
            H_ = dw.build_H(N9, lm, v)
            if v == "b":
                H_ = H_[0]
            alt_rd[nm][v] = readouts(Load(*dw.weyl_data(H_)),
                                     VA, VB, VC, D0, w2)
    tau_v = np.array([taus[kz] for kz in RUNGS])
    al_v = np.array([alphas[kz] for kz in RUNGS])
    passing = []
    verdict_rows = []
    for v in ("a", "b"):
        for nm, key in (("A", "s_A"), ("B", "s_B"),
                        ("C", "s_C")):
            sv = np.array([base[kz][v][key] for kz in RUNGS])
            kap = sv / tau_v
            band = float(np.max(kap) / np.min(kap))
            lo = float(np.min(kap)) / DISC_FACTOR
            hi = float(np.max(kap)) * DISC_FACTOR
            kE = alt_rd["eps"][v][key] / taus[9]
            kS = alt_rd["scr"][v][key] / taus[9]
            outE, outS = not (lo <= kE <= hi), \
                not (lo <= kS <= hi)
            sp_t = spearman(sv, tau_v)
            sp_a = spearman(sv, al_v)
            okp = (ok_g1.get((v, nm), False)
                   and band <= KAPPA_BAND and outE and outS)
            if okp:
                passing.append((v, nm))
            verdict_rows.append((v, nm, band, kE, kS, outE,
                                 outS, sp_t, sp_a))
            print("    %s/%s: band %.2f (<=4) | eps kappa "
                  "%.3e (%s) scr %.3e (%s) | Spearman(s,tau) "
                  "%+.2f (s,alpha) %+.2f%s"
                  % (v, nm, band, kE, "OUT" if outE else "IN",
                     kS, "OUT" if outS else "IN", sp_t, sp_a,
                     "  <- PASS" if okp else ""))

    # ============================================================== S3
    print("\nS3 -- verdict")
    if passing:
        verdict = "READOUT-REPAIRED"
    elif any(ok_g1.values()):
        verdict = "READOUT-SEES-NOT-TAU"
    else:
        verdict = "READOUT-STILL-BLIND"
    print("=" * 78)
    print("V -- VERDICT: %s%s"
          % (verdict, ("  (passing: %s)" % passing)
             if passing else ""))
    print("=" * 78)
    if verdict == "READOUT-REPAIRED":
        print("""    THE COMBINED MACHINE STATEMENT (every arrow typed):
    source divisor tower (SOURCE-BUILT: divisibility + own
    Mangoldt sieve + KMS half-weights, consumes (alpha,
    Lambda) only) -> Weyl load m_h (STRUCTURAL: Herglotz by
    construction, warded) -> unitary hull (STRUCTURAL:
    Walsh/mu4/KMS colligation, unitarity 1e-12, closure
    contractive for every passive load, warded) -> repaired
    readout %s (SOURCE-DEFINED, frozen grids) -> s_h = kappa
    tau_h (MEASURED: band <= 4 across 5 rungs, Epstein AND
    scramble outside the 1.5x window).  TYPED CAVEAT (the
    honesty the verdict must carry): the Spearman(s, tau)
    signs show the kappa-band leg leans on the NARROW tau
    range of the 5-rung battery (s anti-tracks tau at -0.8 on
    variant a); the load-bearing content of the pass is the
    DISCRIMINATION -- the phase readout separates the true
    comb from Epstein/scramble by 1-2 ORDERS OF MAGNITUDE in
    kappa, which no earlier functional of this chain did.
    REMAINING for a cofinal statement: the kappa law must be
    derived, not measured; the ladder must extend beyond the
    5-rung battery (where the band leg becomes falsifiable);
    and the window-geometry dependence (typed at freeze: the
    chain sees only (alpha, Lambda)) must be explained
    structurally.  NO RH claim.""" % (passing,))
    elif verdict == "READOUT-SEES-NOT-TAU":
        aa = [r for r in verdict_rows if r[0] == "a"]
        print("""    THE ITERATED LOCALIZATION (the honest next diagnosis):
    the repair WORKED as repair -- the readouts now see both
    the doubling and the exact reparametrization map at rel
    %.1e..%.1e (v1: 4e-5), so the arithmetic is no longer
    lost between load and readout.  It is lost between the
    READOUT and TAU: the s-series%s.
    The freeze-time structural note is the diagnosis: the
    chain consumes ONLY (alpha, Lambda) -- the window geometry
    (h, M, D, the battery direction) that DEFINES tau never
    enters the machine.  The readout reads the divisor tower's
    global spectral shape (Spearman(s, alpha) above), not the
    window floor.  HONEST CONSEQUENCE: the impedance
    architecture transports arithmetic faithfully end-to-end;
    what it lacks is the WINDOW -- the next named object is a
    load or hull twist that carries the window geometry (the
    lag-space G_S blocks were unitary but window-blind; the
    band intertwiner of the colligation probe would be exactly
    the window-carrying element).  The wall is unchanged; its
    location moved one arrow further down the chain.""" % (
            min(d["dbl"] for d in g1.values()),
            max(d["dbl"] for d in g1.values()),
            " tracks the tower scale, not tau"
            if all(abs(r[7]) <= abs(r[8]) + 0.3 for r in aa)
            else " has kappa bands/discrimination failing "
            "in mixed patterns (see table)"))
    dt = time.time() - T0
    print("-" * 78)
    print("checks: %d run, %d failed%s | runtime %.1f min"
          % (N_CHK, len(FAILS),
             (" [" + ", ".join(FAILS) + "]") if FAILS else "",
             dt / 60.0))
    print("NO RH claim; report only; nothing outside "
          "experiments/ touched.")


if __name__ == "__main__":
    run()
'''

# --------------------------------------------------------------- harness
_PF_RE = re.compile(r"^\s*\[(PASS|FAIL)\]\s+(\S+)", re.M)
_VD_RE = re.compile(r"VERDICT[^\n]*:")


def _probe_file(name):
    cand = os.path.abspath(os.path.join(
        _HERE, os.pardir, "experiments", "tfpt-discovery", name + ".py"))
    return cand if os.path.isfile(cand) else None


def _census(out):
    marks = _PF_RE.findall(out)
    fails = sorted({tok for st, tok in marks if st == "FAIL"})
    verdicts = [ln.strip() for ln in out.splitlines()
                if _VD_RE.search(ln)]
    return len(marks), fails, " | ".join(verdicts)


def _exec_probe(name, src, run_entry=True):
    """Execute one embedded frozen probe source BYTE-EXACT in its own
    module namespace, registered in sys.modules under the probe's
    canonical import name; capture and re-emit stdout; return
    (stdout, exit_code, byte_equal_to_source_file_or_None)."""
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


def _gate(name, out, code, same, exp_n, exp_fails, exp_verdicts,
          exp_code, gates):
    n, fails, verdict = _census(out)
    ok = (n == exp_n and fails == list(exp_fails)
          and all(v in verdict for v in exp_verdicts)
          and code == exp_code and same is not False)
    gates.append(ok)
    prov = ("byte-exact vs experiments source" if same is True else
            "embedded copy (source file not present)" if same is None
            else "SOURCE MISMATCH")
    print("\n[%s] PATTERN GATE %s: %d checks (exp %d) | FAILs %s "
          "(exp %s) | exit %d (exp %d) | %s\n      verdict line(s): %s"
          % ("PASS" if ok else "FAIL", name, n, exp_n,
             ",".join(fails) if fails else "none",
             ",".join(exp_fails) if exp_fails else "none",
             code, exp_code, prov, verdict), flush=True)
    return ok

_PLAN = (
    ('divisor_weyl_port_probe', _SRC_0, 9, ('S1.SPR', 'S4.RSP'),
     ('WEYL-PORT-BLIND',), 0),
    ('weyl_readout_repair_probe', _SRC_1, 5, (),
     ('READOUT-REPAIRED',), 0),
)


def run():
    t0 = time.time()
    print("=" * 74)
    print('v865 -- PRIME.WEYL.PORT.01 + PRIME.WEYL.READOUT.01')
    print('(the arithmetic impedance: the divisor-tower Weyl load')
    print("carries the comb at O(1) -- the hull's comb-blindness is")
    print('repaired at LOAD level -- and dies in the extremal readout')
    print('(reparametrization-blind, diagnosed); the repaired phase')
    print('readout closes the loop: Epstein kappa 42.7 / scramble 77.6')
    print('vs the truth band -- 1-2 orders discrimination; NO RH claim)')
    print("=" * 74, flush=True)
    gates = []
    for name, src, exp_n, exp_fails, exp_verdicts, exp_code in _PLAN:
        print("\n" + "-" * 74)
        print("EMBEDDED FROZEN PROBE: %s" % name)
        print("-" * 74, flush=True)
        out, code, same = _exec_probe(name, src)
        _gate(name, out, code, same, exp_n, exp_fails,
              exp_verdicts, exp_code, gates)
    ok = all(gates)
    print("\n" + "=" * 74)
    print("v865: %d/%d probe pattern gates passed | runtime %.1f s"
          % (sum(gates), len(gates), time.time() - t0))
    print('The two frozen-honest FAILs of the port probe are the')
    print('diagnosis (S1.SPR spreading, S4.RSP the 4e-5 blindness); the')
    print('repair passes anti-blindness at the frozen bars and the')
    print('typed caveat is carried verbatim: Spearman(s, tau) = -0.8 --')
    print('the load-bearing content is the DISCRIMINATION, not the')
    print('kappa band; the kappa law must be derived, not measured.')
    print("[%s] v865 VERDICT GATE: WEYL-PORT-BLIND + READOUT-REPAIRED"
          % ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(run())
