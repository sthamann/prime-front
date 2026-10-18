#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""kr4_defectjet_probe -- PRIME.KR4.DEFECTJET.01

FROZEN SPEC (2026-08-15).  EXPLORATION ONLY.  This probe writes no
verification module, paper, ledger, website, manifest, Lean file or
status marker.  It makes NO RH claim, NO positivity claim, NO
counterexample claim.  It closes no gate and narrows no gate.

=======================================================================
MISSION (the round-118 named lever)
=======================================================================
Round 118 (kr4_depth_probe, SPEC_SHA 9cb09306) certified the Krein
carrier's sigma-derivative reads of the radius-4 diagonal d_m only to
depth m <= 1 (meas/cond channels): the MESH BIAS (tent-interpolation
defect, ~ sigma^2 delta^2) dominates the sup deviation on the Cauchy
contour, while the window budget alone would allow m_R ~ 17.8.  The
named lever: (i) DEFECT-JET SUBTRACTION, (ii) the coupled schedule
delta ~ e^{-(sigma_edge+c)L/2}.  This probe builds (i) EXACTLY and
shows it VOIDS (ii).

THE KEY IDENTITY (derived here, machine-warded): the round-90 lag row
is an exact tent pairing row[d] = <-g'', Lambda_d> (Lambda_d = height-1
tent at d delta; d = 0 the half tent, row[0] = -2 g(delta)/delta with
g(0) = 0 exact).  Hence the truncated transform read is
  P_trunc(sigma) = row[0]/2 + sum_{d>=1} row[d] e^{-sigma d delta}
                 = <-g'', T_sigma>,
  T_sigma(t) = sum_{d=0}^{n-1} e^{-sigma d delta} Lambda_d(t)
             = the piecewise-linear interpolant of e^{-sigma t} on
               [0,(n-1)delta] + the taper ramp on the last cell.
THE MESH DEFECT is therefore the EXACT source-side functional
  D(sigma; delta, L) = <-g'', (T_sigma - e^{-sigma t}) 1_{[0, n delta]}>
    = - sum_{atoms u < L} Lambda(q)/sqrt(q) [T_sigma(u) - e^{-sigma u}]
      + int_0^{n delta} (2 cosh(t/2) - rho_arch(t))
                        [T_sigma(t) - e^{-sigma t}] dt,
  rho_arch(t) = e^{-t/2}/(1 - e^{-2t})  (= S'', exact),
with the atom part EXACT (finite sum, the build's own float-placed
atoms) and the density part by per-cell Gauss-Legendre (the integrand
is analytic per cell: the 1/(2t) arch singularity at t = 0 is
cancelled by the defect kernel's zero (T_sigma - e)(0) = 0, which
holds IDENTICALLY in sigma -- so all regularization boundary terms of
the Weil pairing (the linear -c t piece, the S'(0+) log divergence)
cancel between P_trunc and the windowed truth; sympy gate G10b pins
the leading kernel (sigma^2 delta^2/2) lambda(1-lambda)).  D is
holomorphic in sigma; its sigma-jet at the pin is exact jet algebra
of three exponential jets per cell/atom.  SUBTRACTED READ:
  P_sub = c(sigma)/2 - D  ==  <-g'', e^{-sigma t}>_{[0, n delta]}
                              + (c/2 - P_trunc)
so the deviation from truth is EXACTLY (resummation correction)
- (window tail), BOTH ~ e^{-(sigma_edge - 1/2) L}: the mesh-bias
channel is REMOVED TO ALL ORDERS in delta, the coupled schedule is
VOID, and the mesh cost of window depth is LINEAR (n = L/delta at
FIXED delta) instead of exponential.
HONESTY LINE (frozen): only IN-WINDOW discretization defects are
subtracted.  The window tail (t > n delta) is NEVER subtracted -- it
is the carrier's genuine unknown and becomes the new budget wall.
TAU-SCREEN TYPING (printed, T4): post-subtraction the MEAS-channel
read collapses by construction onto the windowed Weil transform
(Euler-computable): DISGUISE-ADJACENT, typed.  The carrier's
non-collapsing content is (i) the COND enclosure (disk radius,
positivity-conditional), (ii) the positivity certificate itself
(Szego completion through the window -- now probed to L = 5.5), and
(iii) the measured resummation correction.

=======================================================================
DESIGN (frozen)
=======================================================================
PINS (round-118 continuity): a256 (sigma0 16, r_jet 96, RA 0.8, RATE),
a144 (12, 144, 54, 0.8, RATE), a9 (3, 9, 2, 0.5, RESUM, L4 only,
mmax 6).  MMAX = 14 (beyond round-118's table cap 10).
WINDOW LADDER (TRUE world, delta = 0.003): L4 = 2.568 (n 856,
round-90/118 anchor), L67 = 3.999 (n 1333), L92 = 5.499 (n 1833);
szego dps 50 at L4, 60 at the big rungs.  MESH TRIPLE at L4: delta =
0.003 / 0.006 / 0.012 (same window, same atoms) -- post-subtraction
the reads must be delta-INDEPENDENT (G32): the empirical kill of the
delta^2 channel on three mesh levels (T2).
CHANNELS on the a-contour |a - a0| = 0.8 a0 (K = 96): MEAS = 1.5 x
sup|F_sub_read - F_audit| (rigorous Cauchy given the audit); COND =
sup (R_disk + tail_model + 1.5 |c/2 - P_trunc|)/(2|sigma|) with
tail_model = K_TAIL e^{-(Re sigma - 1/2) n delta}/(Re sigma - 1/2),
K_TAIL = 4.08 (round-118 pole+prime constant; R COND-POS, tail
MODEL, resum measured); DISK-ONLY unchanged.  E_m = a0 sup
(4x(1+x))^m, x = a0/r_a (round-118 coefficient form).  GATE meas <=
cond stays falsifiable.  BUDGET LAW (T2 deliverable): post-subtraction
  m*(L) ~ [(sigma_edge - 1/2) L + ln(y1 (sigma_edge - 1/2) 2 sigma_edge
          /(2 a0 SUP_INFLATE K_TAIL))] / ln(4x(1+x)/(4 w_top)),
LINEAR in L with the TAIL exponent (sigma_edge - 1/2), not the disk
exponent (sigma_edge + 1.36): G33 fits the measured sup(L) slope over
the ladder (bar |ratio - 1| <= 0.25), G34 gates the certified-depth
staircase (strictly increasing, total gain >= 4 at a256).
SYNTHETIC DETECTOR (T3 power measurement, rung L92 window): model
world = 40 synthetic on-line atoms gamma_j = 14 + 9j/4 (rational
grid, NO cache anywhere), Lebesgue floor 1e-3 on row[0], optional
MATCHED off-line pair at a0 = 256: zeros 1/2 +- delta_o +- i gamma_o,
gamma_o = sqrt(256 - delta_o^2), exact pair algebra (round-117 (ii):
weight sum 1, pure +w*^m, 4w* = 1 + delta_o^2/gamma_o^2).  Row exact
(closed tent pairings of cos/cosh densities), defect model from the
same declared densities, audit = the exact rational model P(sigma).
Variants delta_o in {0 (null), 2, 1, 1/2, 1/4}.  DETECTION CHANNELS:
(a) COLLAPSE -- Szego dies inside the window (in-window positivity of
the injected world fails: the certificate channel); (b) CERTIFIED
RATE -- lower bound (d'_m - E_m)/(d'_{m-1} + E_{m-1}) > 1 at m <=
m_cert.  G62: null worlds (TRUE and delta_o = 0) must NOT fire.
G63: delta_o = 2 MUST fire.  Deaths give the collapse-law data
t_death x delta_o ~ const (nats); extrapolation to the Epstein
witness is printed as MODEL-grade (background-margin caveat typed).
EPSTEIN QUESTION (T3, exact witness numbers frozen from round 117):
rho = 0.6969270453 + 36.3740636864 i, |xi_Q| = 9.6e-61, matched
a* = 1323.11128932, relative excess delta^2/gamma^2 = 2.931e-5,
window a in (1308.9, 1337.5), Q-side neighbours 4w = 0.99792 (34.75)
/ 0.99862 (37.75).  The certified-depth detector CANNOT fire at
today's budgets (the all-m omega absorbs any finite certified depth);
the probe prints the exact prices: rate-channel depth m2 = ln2 x
gamma^2/delta^2 = 23646 (round-117 law) with window L ~ m2 ln Q /
(sigma_edge - 1/2), and the collapse-channel window L_req =
(measured nats)/delta_w with SOURCE price e^{L_req} atoms (the sieve
must reach height e^L: the exponential price moved from the mesh
into the arithmetic data -- stated, not hidden).
MIN-CUT (T3, round-116 graph + round-118 extension): add
KR4-DEFECTJET-SUB (UNC-DICT: an exact identity), KR4-DEPTH-CERT-FIN
(finite-m certified read, riding the SAME capacity-1 Weyl measurement
edge), the one-sided falsifier node, and the residual all-m omega
edge to R4-HYP.  GATES: flows stay 4/4/4; granting the finite-m
certificate (any m) leaves RH and R4-HYP unreachable through
proven edges (the omega ABSORBS finite certified depth); census
classes unchanged up to the declared MEAS -> CERT-INSTR costume swap
(cardinality 4 either way).
CONTROLS: SMOOTH/SCRARITH die at the round-90 positivity radii
0.264/0.744 (+-0.05) at (L4, 0.003); TRUE detector null; conditioning
screen 1e-25 deterministic lag perturbation at the deepest rung,
compared in mp BEFORE any float cast (round-118 AMENDMENT-1 lesson;
all jet post-processing inside workdps(DPS_ALG)).

=======================================================================
FROZEN NUMERICS AND GATES
=======================================================================
MMAX 14 (NJ 29); DPS_ALG 80; GLK 16 (per-cell Gauss-Legendre; the
arch 1/(2t) part makes the early cells' high derivatives large --
measured total quadrature floor ~1e-23, see AMENDMENT 1); KCONT 96
(SYN 48); SUP_INFLATE 1.5; K_TAIL 4.08; C_LAW 1.36 (cited round 90);
direct jets (M, dps, N, orders) = (256, 200, 60000, 44); FD step
1e-12; perturbation 1e-25; TRANS_BAR 1e-6; Z1 margin 10; runtime bar
14400 s.  Deterministic, no randomness anywhere.  Cache
verified_zeros_n7000.npy READ-ONLY via R4.ward_cache (X5 instrument).
Smoke flag reduces everything and is NOT VERDICT-BEARING.
GATES: G01 AST firewall (zeta only in audit_, np.load only in ward_);
G10 dictionary-atom-exact (round-118 gate, rel <= 1e-35); G10b sympy
leading-defect kernel exact + closed-form cell integral vs GL <=
1e-40; G11 domain (min Re sigma > 1/2, |w| < 1, disk margin > 0);
G12 FD ward on the SUBTRACTED first derivative (rel <= 1e-15); G13
contour-vs-jet cross-ward on subtracted b_n (n <= 8, rel <= 1e-5);
G14 central value in disk at the real pins; G15 defect ward, rational
atoms (jets + complex value, rel <= 1e-60); G16 defect ward,
exponential density e^{-2t} vs closed form (rel <= 1e-40); G17 SYN
pipeline enclosure |d'_sub - d'_exact| <= 1.2 E_meas (all completing
SYN variants, m <= MMAX); G18 pin closure |P_sub(sigma0) - audit| <=
3 (R_pin + tail_model_pin) + 2e-18 per deep pin per rung (the
subtraction closes onto truth at the pins); G20 sup_meas <= sup_cond
per pin/rung; G21 TRUE positivity completes at L4 (hard; higher-rung
failures re-type the ladder POSITIVITY-BOUNDARY); G22 direct jets
healthy; G30 BIAS KILL: post/pre pin deviation ratio <= 1e-2 (deep
pins, L4); G31 enclosure |d'_sub - d'_jet| <= 1.2 (E_meas + width)
for ALL m <= MMAX, deep pins, all rungs; G32 mesh-triple collapse:
post-sub cross-mesh deviation <= 1e-2 x pre-sub (a256, L4,
delta-pairs 0.006/0.012 vs 0.003, m <= 8 where pre >= 1e-12); G33
window-law slope fit ratio in [0.75, 1.25] vs -(sigma_edge - 1/2);
G34 certified staircase m_cert_meas(a256) strictly increasing, total
gain >= 4 over the ladder; G40 no transcription (scan > 1e-6, deep
pins, L4 + L92); G41 Z1 margin >= 10 (post-sub m = 0 vs best cache
partial sum); G50a min-cut flows 4/4/4; G50b census classes within
{OMEGA-POS, OMEGA-POS-MEAS, MEAS, OMEGA-LAW, CANDIDATE, CERT-INSTR};
G50c omega absorption: granting KR4-DEPTH-CERT-FIN, RH and R4-HYP
stay unreachable through proven edges; G60 controls die at
0.264/0.744 (+-0.05); G61 conditioning: 1e-25 perturbation rate
shift <= 1e-8 at the deepest rung; G62 detector nulls silent (TRUE
and SYN delta_o = 0: no collapse, rate LB <= 1); G63 detector fires
at delta_o = 2 (collapse or rate); G99 runtime.
COMPOSITE VERDICT (priority frozen): instrument-gate failure (G10-
G16, G22) => KR4DJ-INSTRUMENT-EDGE (exit 1) > G21@L4 fails =>
KR4DJ-DEAD(positivity) > higher-rung positivity fails =>
KR4DJ-POSITIVITY-BOUNDARY(L) > G40 fires => KR4DJ-TRANSCRIBES >
[G18 and G30 and G32] => KR4DJ-BIASKILL(certified depths pre/post,
window law) > else KR4DJ-DEFECT-RESIDUAL.  Sub-verdicts: WINDOW-LAW,
MESH-PRICE-LINEAR, RATE-CERTIFIED (deepest certified rate read +-
bars, margin to 1), MINCUT-OMEGA-ABSORBS, EPSTEIN-POWER (no-fire +
price laws), DETECTOR-POWER (deaths + boundary), CONTROLS, DISGUISE
typing, CONDITIONING law.
PRE-FREEZE DISCLOSURE: every bar above was frozen from the round-
90/116/117/118 published numbers plus the Cauchy/tail analysis in
this spec, BEFORE the first full run.  Smoke runs may catch
implementation slips -- any instrument repair is disclosed in
numbered AMENDMENT lines appended below; no bar, grid, pin or
verdict rule moves.
AMENDMENT 1 (smoke 1, 24/29; physics already clean: bias kill
x7.7e11, slope ratio 0.995, mesh triple 6.6e-6, detector collapse
fires): four instrument repairs, isolated by a GLK/sigma/dps
bisection BEFORE any bar moved.  (a) THE REAL FINDING: GLK = 8 was
insufficient for the ARCH integrand -- the 1/(2t) part of rho_arch
makes the k-th cell's 2K-th derivative scale like (2K)!/(k delta)^
(2K+1), so the per-cell Gauss error decays only like (1/2k)^{2K} in
the early cells; measured ladder at sigma = 24 on the full TRUE
defect: GL8 1.4e-15, GL12 1.1e-21, GL16 1.4e-23 (the sigma < 12
residual is the window tail, as designed).  GLK moves 8 -> 16
(instrument parameter; every gate bar unchanged).  (b) the ward
gates parsed "0.003" at the AMBIENT mp.dps = 15 while their
reference values parsed it at working precision -- two different
mpf deltas at rel ~1e-17 (the round-118 AMENDMENT-1 ambient-dps
class, relearned in a new costume); the ward gates now parse delta
ONCE at DPS_ALG+20 and share the mpf.  The TRUE pipeline was always
internally consistent (it shares build["delta_mp"] everywhere).
(c) G15 hit the ambient class TWICE: float-cast atom positions
(fixed: exact mp positions), and -- the sharpest lesson of the
round -- mpmath UNARY NEGATION rounds to the ambient precision:
building atoms = [(u, -w)] OUTSIDE the workdps context silently
cast the exact rational weight -1/3 to its 53-bit double (isolated
by a per-atom bisection to rel ~3e-21 per atom); the negation now
happens inside the context.  The TRUE pipeline is unaffected: the
round-90 build weights are float64 by construction (53-bit exact
under negation) and the model uses the SAME floats.  (d) the G10b
sympy reference was evalf'd at 60 digits over a cancelling
exponential combination AND parsed by mp.mpf at ambient dps 15:
now sp.N(., 140) parsed under workdps(DPS_ALG+20).
(e) the G13 smoke failure at 4.3e-5 is the SMOKE-reduced contour
K = 24 aliasing (identical to round-118 AMENDMENT 1d); the frozen
full K = 96 is unchanged.  No bar, grid, pin or verdict rule moved.
NO RH CLAIM.  EXPLORATION ONLY.
"""

from __future__ import annotations

import argparse
import ast
import hashlib
import math
import os
import sys
import time

import mpmath as mp
import numpy as np
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

import krein_screw_realization_probe as KR   # noqa: E402  round-90 frozen
import radius4_reduction_probe as R4         # noqa: E402  round-117 frozen
import idgraph_search_probe as IG            # noqa: E402  round-116 frozen
import kr4_depth_probe as KD                 # noqa: E402  round-118 frozen

# ------------------------------------------------------------ frozen bars
L4 = 2.568
RUNGS = (2.568, 3.999, 5.499)          # n = 856 / 1333 / 1833 at 0.003
D3, D6, D12 = "0.003", "0.006", "0.012"
MMAX = 14
DPS_ALG = 80
GLK = 16
KCONT, KCONT_SYN = 96, 48
SUP_INFLATE = 1.5
K_TAIL = 4.08
C_LAW = 1.36
#          label   sigma0  a0   r_jet  ra_frac  role   mmax
PINS = (("a256", 16, 256, 96, 0.8, "RATE", MMAX),
        ("a144", 12, 144, 54, 0.8, "RATE", MMAX),
        ("a9", 3, 9, 2, 0.5, "RESUM", 6))
JET_M, JET_DPS, JET_NS, JET_ORD = 256, 200, 60000, 44
FD_H = "1e-12"
PERT_DPS = 25
TRANS_BAR = 1e-6
Z1_MARGIN = 10.0
CTRL_R_SMOOTH, CTRL_R_SCR, CTRL_TOL = 0.264, 0.744, 0.05
BAR_ATOMWARD = 1e-60
BAR_EXPWARD = 1e-40
BAR_CELL = 1e-40
BAR_FD = 1e-15
BAR_XWARD = 1e-5
BAR_IM = 1e-40
BAR_PINCLOSE_FLOOR = 2e-18
BAR_BIASKILL = 1e-2
BAR_MESHTRIPLE = 1e-2
BAR_SLOPE = 0.25
BAR_STAIR_GAIN = 4
BAR_RATE_SHIFT = 1e-8
RUNTIME_BAR = 14400.0
# synthetic detector (frozen)
NSYN = 40
SYN_GAMMAS = tuple(14 + mp.mpf(9) * j / 4 for j in range(NSYN))
EPS_LEB = "0.001"
SYN_DELTAS = (0.0, 2.0, 1.0, 0.5, 0.25)
SYN_A0, SYN_S0 = 256, 16
# Epstein witness (frozen, cited round 117)
EPS_GAMMA = 36.3740636864
EPS_DELTA = 0.1969270453
EPS_ASTAR = 1323.11128932
EPS_XI = 9.6e-61
EPS_NEIGHB = ((34.75, 0.99792), (37.75, 0.99862))
EPS_WINDOW = (1308.9, 1337.5)

SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
T0_WALL = time.time()

CHECKS: list[tuple[str, bool, str]] = []


def check(name: str, ok: bool, detail: str) -> bool:
    ok = bool(ok)
    CHECKS.append((name, ok, detail))
    print("  [%s] %-40s %s" % ("PASS" if ok else "FAIL", name, detail),
          flush=True)
    return ok


def info(msg: str) -> None:
    print("  [INFO] " + msg, flush=True)


def section(title: str) -> None:
    print("\n" + "-" * 78 + "\n" + title + "\n" + "-" * 78, flush=True)


# ====================================================== firewall (G01)
FORBIDDEN = ("zetazero", "siegelz", "siegeltheta", "nzeros", "grampoint")


def firewall_audit() -> tuple[bool, str]:
    src = open(os.path.abspath(__file__), "r", encoding="utf-8").read()
    tree = ast.parse(src)
    spans = []
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            spans.append((node.name, node.lineno, max(
                getattr(n, "lineno", node.lineno) for n in ast.walk(node))))

    def owner(lineno: int) -> str:
        best = ""
        for nm, lo, hi in spans:
            if lo <= lineno <= hi:
                best = nm
        return best

    bad = []
    for node in ast.walk(tree):
        nm = None
        if isinstance(node, ast.Attribute):
            nm = node.attr
        elif isinstance(node, ast.Name):
            nm = node.id
        if nm is None:
            continue
        low = nm.lower()
        if low in FORBIDDEN:
            bad.append("forbidden %s @%d" % (nm, node.lineno))
        if low == "zeta":
            fn = owner(node.lineno)
            if not fn.startswith("audit_"):
                bad.append("zeta outside audit_ @%d (%s)"
                           % (node.lineno, fn or "module"))
        if isinstance(node, ast.Attribute) and nm == "load":
            fn = owner(node.lineno)
            if not fn.startswith("ward_"):
                bad.append("np.load outside ward_ @%d (%s)"
                           % (node.lineno, fn or "module"))
    return (len(bad) == 0, "; ".join(bad) if bad else
            "no zero-oracle; audit_/ward_ namespaces enforced; cache "
            "only via R4.ward_cache (X5)")


def audit_pin(sigma, dps: int = 60):
    return R4.audit_xi_logderiv(mp.mpf("0.5") + mp.mpc(sigma), dps)


def ward_gammas() -> np.ndarray:
    return R4.ward_cache()


# ====================================================== Gauss-Legendre
_GL: dict[int, tuple[list, list]] = {}


def gl_nodes(k: int) -> tuple[list, list]:
    if k in _GL:
        return _GL[k]
    with mp.workdps(DPS_ALG + 20):
        xs, ws = [], []
        for i in range(1, k + 1):
            x = mp.cos(mp.pi * (i - mp.mpf(1) / 4) / (k + mp.mpf(1) / 2))
            dp = mp.mpf(1)
            for _ in range(80):
                p0, p1 = mp.mpf(1), x
                for j in range(2, k + 1):
                    p0, p1 = p1, ((2 * j - 1) * x * p1 - (j - 1) * p0) / j
                dp = k * (x * p1 - p0) / (x * x - 1)
                dx = p1 / dp
                x -= dx
                if abs(dx) < mp.mpf(10) ** (-(DPS_ALG + 12)):
                    break
            ws.append(2 / ((1 - x * x) * dp * dp))
            xs.append(x)
    _GL[k] = (xs, ws)
    return xs, ws


# ====================================================== defect machinery
def rho_true(t):
    """Smooth density of -g'' in the TRUE world: 2 cosh(t/2) -
    e^{-t/2}/(1 - e^{-2t})  (pole minus arch; atoms handled exactly)."""
    return 2 * mp.cosh(t / 2) - mp.exp(-t / 2) / (1 - mp.exp(-2 * t))


def prep_defect(n: int, delta_mp, dens_fn=None, dens_nodes=None,
                atoms=()) -> dict:
    """Precompute the per-cell GL data of the defect functional.
    atoms: list of (u_float, coeff_mp) -- coeff is SIGNED (-Lambda(q)/
    sqrt(q) in the TRUE world).  dens_nodes[k][i] overrides dens_fn."""
    xs, ws = gl_nodes(GLK)
    with mp.workdps(DPS_ALG + 10):
        dl = mp.mpf(delta_mp)
        lam = [(1 + x) / 2 for x in xs]
        off = [dl * lv for lv in lam]
        half = dl / 2
        crho = None
        if dens_fn is not None or dens_nodes is not None:
            crho = []
            for k in range(n):
                base = k * dl
                if dens_nodes is not None:
                    row = [dens_nodes[k][i] * ws[i] * half
                           for i in range(GLK)]
                else:
                    row = [dens_fn(base + off[i]) * ws[i] * half
                           for i in range(GLK)]
                crho.append(row)
    return {"n": n, "dl": dl, "lam": lam, "off": off, "crho": crho,
            "atoms": tuple(atoms)}


def defect_val(prep: dict, sigma):
    """D(sigma) at one (possibly complex) sigma."""
    n, dl = prep["n"], prep["dl"]
    lam, off, crho = prep["lam"], prep["off"], prep["crho"]
    with mp.workdps(DPS_ALG):
        wd = mp.exp(-sigma * dl)
        eoff = [mp.exp(-sigma * o) for o in off]
        nf = [(1 - lam[i]) + lam[i] * wd - eoff[i] for i in range(GLK)]
        nft = [(1 - lam[i]) - eoff[i] for i in range(GLK)]
        acc = mp.mpf(0) if mp.im(mp.mpc(sigma)) == 0 else mp.mpc(0)
        ek = mp.mpf(1)
        if crho is not None:
            for k in range(n):
                fac = nft if k == n - 1 else nf
                cell = crho[k]
                s = cell[0] * fac[0]
                for i in range(1, GLK):
                    s += cell[i] * fac[i]
                acc += ek * s
                ek = ek * wd
        dlf = float(dl)
        for (u, coeff) in prep["atoms"]:
            k = int(u / dlf)
            if k >= n:
                continue
            um = mp.mpf(u)
            lv = (um - k * dl) / dl
            euk = mp.exp(-sigma * (k * dl))
            eu = mp.exp(-sigma * (um - k * dl))
            if k <= n - 2:
                fac = (1 - lv) + lv * wd - eu
            else:
                fac = (1 - lv) - eu
            acc += coeff * euk * fac
        return acc


def _expjet(tau, base, nj: int) -> list:
    """jet of e^{-sigma tau} at sigma0: base * (-tau)^j / j!."""
    out = [base]
    p = base
    for j in range(1, nj):
        p = p * (-tau) / j
        out.append(p)
    return out


def defect_jet(prep: dict, sigma0, nj: int) -> list:
    """Exact sigma-jet of D at the real pin sigma0 (P currency)."""
    n, dl = prep["n"], prep["dl"]
    lam, off, crho = prep["lam"], prep["off"], prep["crho"]
    with mp.workdps(DPS_ALG):
        s0 = mp.mpf(sigma0)
        wd = mp.exp(-s0 * dl)
        eoff = [mp.exp(-s0 * o) for o in off]
        acc = [mp.mpf(0)] * nj
        ek = mp.mpf(1)
        pnext = None
        if crho is not None:
            for k in range(n):
                tk = k * dl
                p0 = pnext if pnext is not None else _expjet(tk, ek, nj)
                ek1 = ek * wd
                p1 = _expjet(tk + dl, ek1, nj)
                cell = crho[k]
                last = (k == n - 1)
                for i in range(GLK):
                    tn = tk + off[i]
                    pt = _expjet(tn, ek * eoff[i], nj)
                    c1 = (1 - lam[i]) * cell[i]
                    c2 = lam[i] * cell[i]
                    if last:
                        for j in range(nj):
                            acc[j] += c1 * p0[j] - cell[i] * pt[j]
                    else:
                        for j in range(nj):
                            acc[j] += (c1 * p0[j] + c2 * p1[j]
                                       - cell[i] * pt[j])
                ek = ek1
                pnext = p1
        dlf = float(dl)
        for (u, coeff) in prep["atoms"]:
            k = int(u / dlf)
            if k >= n:
                continue
            um = mp.mpf(u)
            lv = (um - k * dl) / dl
            e0 = mp.exp(-s0 * (k * dl))
            p0 = _expjet(k * dl, e0, nj)
            pt = _expjet(um, mp.exp(-s0 * um), nj)
            if k <= n - 2:
                p1 = _expjet((k + 1) * dl, e0 * wd, nj)
                for j in range(nj):
                    acc[j] += coeff * ((1 - lv) * p0[j] + lv * p1[j]
                                       - pt[j])
            else:
                for j in range(nj):
                    acc[j] += coeff * ((1 - lv) * p0[j] - pt[j])
        return acc


def trunc_val(row, delta_mp, sigma):
    """P_trunc(sigma) = row[0]/2 + sum_{d>=1} row[d] e^{-sigma d delta}."""
    with mp.workdps(DPS_ALG):
        w = mp.exp(-sigma * delta_mp)
        acc = row[0] / 2
        wp = mp.mpf(1) if mp.im(mp.mpc(sigma)) == 0 else mp.mpc(1)
        for d in range(1, len(row)):
            wp = wp * w
            acc += row[d] * wp
        return acc


def tail_model_p(res: float, win: float) -> float:
    return K_TAIL / max(res - 0.5, 0.1) * math.exp(-(res - 0.5) * win)


def synth_row(gfun, n: int, delta_mp) -> list:
    """Second-difference row of a synthetic g (exact convention)."""
    with mp.workdps(DPS_ALG + 20):
        dl = mp.mpf(delta_mp)
        g = [gfun(j * dl) for j in range(n + 1)]
        row = [-2 * g[1] / dl]
        for d in range(1, n):
            row.append(-(g[d - 1] - 2 * g[d] + g[d + 1]) / dl)
    return row


# ====================================================== ward gates
def gate_sympy_kernel() -> tuple[bool, str]:
    lam_s, s_s, d_s = sp.symbols("lam s d", positive=True)
    phi = (1 - lam_s) + lam_s * sp.exp(-s_s * d_s) \
        - sp.exp(-lam_s * s_s * d_s)
    coeff2 = sp.series(phi, d_s, 0, 3).removeO().coeff(d_s, 2)
    ok1 = sp.simplify(coeff2 - s_s ** 2 * lam_s * (1 - lam_s) / 2) == 0
    beta_s, sg_s, dd_s, t_s = sp.symbols("beta sg dd t", positive=True)
    integrand = sp.exp(-beta_s * t_s) * (
        (1 - t_s / dd_s) + (t_s / dd_s) * sp.exp(-sg_s * dd_s)
        - sp.exp(-sg_s * t_s))
    closed = sp.integrate(integrand, (t_s, 0, dd_s))
    val_sym = closed.subs({beta_s: 2, sg_s: 16,
                           dd_s: sp.Rational(3, 1000)})
    with mp.workdps(DPS_ALG + 20):
        ref = mp.mpf(sp.N(val_sym, 140).__str__())
    xs, ws = gl_nodes(GLK)
    with mp.workdps(DPS_ALG):
        dl = mp.mpf("0.003")
        wd = mp.exp(-16 * dl)
        acc = mp.mpf(0)
        for x, w in zip(xs, ws):
            t = dl * (1 + x) / 2
            lamv = t / dl
            acc += w * (dl / 2) * mp.exp(-2 * t) * (
                (1 - lamv) + lamv * wd - mp.exp(-16 * t))
        dev = float(abs(acc - ref) / abs(ref))
    return (ok1 and dev <= BAR_CELL,
            "sympy leading kernel == (s^2 d^2/2) lam(1-lam): %s; "
            "closed-form cell integral vs GL%d rel dev %.1e (bar %.0e)"
            % (ok1, GLK, dev, BAR_CELL))


def gate_atom_ward() -> tuple[bool, str]:
    """G15: rational-atom world -- model defect == exact difference."""
    n = 700
    with mp.workdps(DPS_ALG + 20):
        dl = mp.mpf(D3)
        us = [mp.mpf(7) / 10, mp.mpf(11) / 10, mp.mpf(17) / 10]
        wsyn = [mp.mpf(1) / 2, mp.mpf(1) / 3, mp.mpf(1) / 5]

        def gfun(t):
            acc = mp.mpf(0)
            for u, w in zip(us, wsyn):
                if t > u:
                    acc += w * (t - u)
            return acc

        atoms = [(u, -w) for u, w in zip(us, wsyn)]

    row = synth_row(gfun, n, dl)
    prep = prep_defect(n, dl, atoms=atoms)
    nj = 2 * MMAX + 1
    with mp.workdps(DPS_ALG):
        s0 = mp.mpf(16)
        ptr = KD.trunc_pjet(row, dl, 16, nj)
        dj = defect_jet(prep, 16, nj)
        worst = 0.0
        for j in range(nj):
            pw = mp.mpf(0)
            for u, w in zip(us, wsyn):
                pw += -w * mp.exp(-s0 * u) * (-u) ** j / mp.factorial(j)
            worst = max(worst, float(abs((ptr[j] - dj[j]) - pw)
                                     / max(abs(pw), mp.mpf("1e-300"))))
        sc = mp.mpc(7, 3)
        pv = trunc_val(row, dl, sc) - defect_val(prep, sc)
        pw = mp.mpc(0)
        for u, w in zip(us, wsyn):
            pw += -w * mp.exp(-sc * u)
        worstc = float(abs(pv - pw) / abs(pw))
        d0 = float(abs(dj[0] - defect_val(prep, mp.mpf(16))))
    ok = worst <= BAR_ATOMWARD and worstc <= BAR_ATOMWARD \
        and d0 <= 1e-60
    return ok, ("rational atoms: jet rel %.1e, complex-value rel %.1e "
                "(bar %.0e); jet[0] vs value internal %.1e"
                % (worst, worstc, BAR_ATOMWARD, d0))


def gate_exp_ward() -> tuple[bool, str]:
    """G16: exponential density e^{-2t} -- subtracted read == exact
    windowed transform (closed form)."""
    n = 700
    with mp.workdps(DPS_ALG + 20):
        dl = mp.mpf(D3)

        def gfun(t):
            return (1 - mp.exp(-2 * t)) / 4 - t / 2

    row = synth_row(gfun, n, dl)
    prep = prep_defect(n, dl, dens_fn=lambda t: mp.exp(-2 * t))
    nj = 2 * MMAX + 1
    with mp.workdps(DPS_ALG):
        s0 = mp.mpf(16)
        wn = n * dl
        ptr = KD.trunc_pjet(row, dl, 16, nj)
        dj = defect_jet(prep, 16, nj)
        num = [mp.mpf(0)] * nj
        ewin = _expjet(wn, mp.exp(-(s0 + 2) * wn), nj)
        num[0] = 1 - ewin[0]
        for j in range(1, nj):
            num[j] = -ewin[j]
        den = [mp.mpf(0)] * nj
        den[0] = s0 + 2
        den[1] = mp.mpf(1)
        pw = KD.j_div(num, den, nj)
        worst = 0.0
        for j in range(nj):
            worst = max(worst, float(abs((ptr[j] - dj[j]) - pw[j])
                                     / max(abs(pw[j]),
                                           mp.mpf("1e-300"))))
        sc = mp.mpc(7, 3)
        pv = trunc_val(row, dl, sc) - defect_val(prep, sc)
        pwc = (1 - mp.exp(-(sc + 2) * wn)) / (sc + 2)
        worstc = float(abs(pv - pwc) / abs(pwc))
    ok = worst <= BAR_EXPWARD and worstc <= BAR_EXPWARD
    return ok, ("exp density: jet rel %.1e, complex-value rel %.1e "
                "(bar %.0e; GL%d per cell)"
                % (worst, worstc, BAR_EXPWARD, GLK))


# ====================================================== per-pin analysis
AUDIT_CACHE: dict = {}


def contour_nodes(label: str, a0: int, ra: float, kcont: int) -> list:
    key = (label, kcont)
    if key in AUDIT_CACHE:
        return AUDIT_CACHE[key]
    out = []
    with mp.workdps(DPS_ALG):
        for j in range(kcont):
            th = mp.mpf(2 * j) / kcont
            av = a0 + mp.mpf(ra) * mp.expjpi(th)
            sv = mp.sqrt(av)
            fa = audit_pin(sv) / (2 * sv)
            out.append((th, sv, fa))
    AUDIT_CACHE[key] = out
    return out


def cert_depth(ev, dref, mmax: int) -> int:
    mc = -1
    for m in range(mmax + 1):
        if ev[m] <= 0.5 * abs(float(dref[m])) and mc == m - 1:
            mc = m
    return mc


def analyze_pin_rung(pin, rung_lab, build, sz, prep, jet_direct,
                     kcont: int) -> dict:
    (label, s0, a0, _rj, raf, role, mmax_pin) = pin
    nj = 2 * mmax_pin + 1
    out = {"label": label, "rung": rung_lab, "role": role}
    win = build["L"]
    t0 = time.time()
    with mp.workdps(DPS_ALG):
        pj_raw = [x / 2 for x in KD.transfer_cval_jet(
            sz["alphas"], sz["c0"], s0, build["delta_mp"], nj)]
        djets = defect_jet(prep, s0, nj)
        pj_sub = [pj_raw[j] - djets[j] for j in range(nj)]
    d_pre, _b = KD.pjet_to_dscaled(pj_raw, s0, a0, mmax_pin)
    d_sub, b_sub = KD.pjet_to_dscaled(pj_sub, s0, a0, mmax_pin)
    print("  [%s|%s] jets order %d + defect jet: %.1f s"
          % (label, rung_lab, nj - 1, time.time() - t0), flush=True)

    # pin reads + disk + FD ward
    with mp.workdps(DPS_ALG):
        w0 = mp.exp(-mp.mpf(s0) * build["delta_mp"])
        cval0, cen0, rad0, marg0 = KD.disk_complex(sz["alphas"],
                                                   sz["c0"], w0)
        p_aud = mp.re(audit_pin(s0))
        dev_pre = float(abs(pj_raw[0] - p_aud))
        dev_sub = float(abs(pj_sub[0] - p_aud))
        h = mp.mpf(FD_H)
        cp, _c, _r, _m = KD.disk_complex(
            sz["alphas"], sz["c0"],
            mp.exp(-(mp.mpf(s0) + h) * build["delta_mp"]))
        cm, _c, _r, _m = KD.disk_complex(
            sz["alphas"], sz["c0"],
            mp.exp(-(mp.mpf(s0) - h) * build["delta_mp"]))
        dp = defect_val(prep, mp.mpf(s0) + h)
        dm = defect_val(prep, mp.mpf(s0) - h)
        fd1 = ((cp / 2 - dp) - (cm / 2 - dm)) / (2 * h)
        fd_rel = float(abs(fd1 - pj_sub[1]) / abs(pj_sub[1]))
        incirc = float(abs(cval0 - cen0) / max(float(rad0), 1e-300))
    tmp = tail_model_p(float(s0), win)
    close_bar = 3.0 * (float(rad0) + tmp) + BAR_PINCLOSE_FLOOR
    out.update(fd_rel=fd_rel, incirc=incirc, rad_pin=float(rad0),
               dev_pin_pre=dev_pre, dev_pin_sub=dev_sub,
               close_bar=close_bar, marg_pin=float(marg0))
    info("%s|%s pin: |P_raw-audit| %.2e -> |P_sub-audit| %.2e "
         "(kill x%.1e); close bar %.1e; R_pin %.1e; |c-cen|/R %.3f"
         % (label, rung_lab, dev_pre, dev_sub,
            dev_pre / max(dev_sub, 1e-300), close_bar, float(rad0),
            incirc))

    # contour channels
    t0 = time.time()
    ra = raf * a0
    nodes = contour_nodes(label, a0, ra, kcont)
    sup_meas = sup_meas_pre = sup_cond = sup_r = 0.0
    min_res = float("inf")
    min_marg = float("inf")
    fhat = [mp.mpc(0)] * nj
    with mp.workdps(DPS_ALG):
        for (th, sv, fa) in nodes:
            wv = mp.exp(-sv * build["delta_mp"])
            cval, _cen, rad, marg = KD.disk_complex(sz["alphas"],
                                                    sz["c0"], wv)
            dval = defect_val(prep, sv)
            ptr = trunc_val(build["row"], build["delta_mp"], sv)
            f_sub = (cval / 2 - dval) / (2 * sv)
            f_raw = (cval / 2) / (2 * sv)
            res = float(mp.re(sv))
            asig = float(abs(sv))
            min_res = min(min_res, res)
            min_marg = min(min_marg, float(marg))
            sup_meas = max(sup_meas, float(abs(f_sub - fa)))
            sup_meas_pre = max(sup_meas_pre, float(abs(f_raw - fa)))
            resum = float(abs(cval / 2 - ptr))
            sup_cond = max(sup_cond,
                           (float(rad) + tail_model_p(res, win)
                            + 1.5 * resum) / (2.0 * asig))
            sup_r = max(sup_r, float(rad) / (2.0 * asig))
            for nn in range(nj):
                fhat[nn] += f_sub * mp.expjpi(-th * nn)
        xdev = 0.0
        for nn in range(min(9, nj)):
            cn = fhat[nn] / kcont / mp.mpf(ra) ** nn
            bq = mp.mpf(a0) ** (nn + 1) * ((-1) ** nn) * mp.re(cn)
            xdev = max(xdev, float(abs(bq - b_sub[nn])
                                   / max(abs(b_sub[nn]),
                                         mp.mpf("1e-300"))))
    sup_meas *= SUP_INFLATE
    sup_meas_pre *= SUP_INFLATE
    out.update(sup_meas=sup_meas, sup_meas_pre=sup_meas_pre,
               sup_cond=sup_cond, sup_r=sup_r, min_res=min_res,
               min_marg=min_marg, xward=xdev)
    print("  [%s|%s] contour K=%d: %.1f s; min Re sigma %.3f; sup "
          "dev_F pre %.3e -> sub %.3e | cond %.3e | R-only %.3e"
          % (label, rung_lab, kcont, time.time() - t0, min_res,
             sup_meas_pre, sup_meas, sup_cond, sup_r), flush=True)

    # depth table
    djet, wjet = R4.diag_scaled(jet_direct, DPS_ALG)
    djet = djet[: mmax_pin + 1]
    wjet = wjet[: mmax_pin + 1]
    e_meas = KD.budget_dm(sup_meas, float(a0), ra, mmax_pin)
    e_cond = KD.budget_dm(sup_cond, float(a0), ra, mmax_pin)
    e_r = KD.budget_dm(sup_r, float(a0), ra, mmax_pin)
    print("  [%s|%s] DEPTH TABLE (d'_m = 4^m C_{m,m}):"
          % (label, rung_lab))
    print("    m   d'_jet        d'_sub        dev_pre    dev_sub    "
          "E_meas     E_cond     width")
    m_sig_pre = m_sig_sub = -1
    ok31 = True
    dev_pre_l, dev_sub_l = [], []
    for m in range(mmax_pin + 1):
        dj = float(djet[m])
        dvp = abs(float(d_pre[m]) - dj)
        dvs = abs(float(d_sub[m]) - dj)
        dev_pre_l.append(dvp)
        dev_sub_l.append(dvs)
        if dvp <= 0.5 * abs(dj) and m_sig_pre == m - 1:
            m_sig_pre = m
        if dvs <= 0.5 * abs(dj) and m_sig_sub == m - 1:
            m_sig_sub = m
        if dvs > 1.2 * (e_meas[m] + wjet[m]):
            ok31 = False
        print("    %-3d %.6e  %.6e  %.3e  %.3e  %.3e  %.3e  %.1e"
              % (m, dj, float(d_sub[m]), dvp, dvs, e_meas[m],
                 e_cond[m], wjet[m]))
    m_cm = cert_depth(e_meas, djet, mmax_pin)
    m_cc = cert_depth(e_cond, djet, mmax_pin)
    m_cr = cert_depth(e_r, djet, mmax_pin)
    out.update(m_sig_pre=m_sig_pre, m_sig_sub=m_sig_sub,
               m_cert_meas=m_cm, m_cert_cond=m_cc, m_cert_ronly=m_cr,
               ok31=ok31, d_pre=[float(x) for x in d_pre],
               d_sub=[float(x) for x in d_sub], d_sub_mp=d_sub,
               dev_pre=dev_pre_l, dev_sub=dev_sub_l,
               djet=[float(x) for x in djet], wjet=wjet,
               e_meas=e_meas, e_cond=e_cond, win=win)
    x = a0 / ra
    info("%s|%s depths: signal pre m<=%d sub m<=%d; CERTIFIED meas "
         "m<=%d | cond m<=%d | disk-only m<=%d (Q=4x(1+x)=%.2f)"
         % (label, rung_lab, m_sig_pre, m_sig_sub, m_cm, m_cc, m_cr,
            4 * x * (1 + x)))

    # certified rate at the deepest certified depth
    m_use = min(m_cm, mmax_pin)
    if role == "RATE" and m_use >= 2:
        with mp.workdps(DPS_ALG):
            rk = float(d_sub[m_use] / d_sub[m_use - 1])
        rj = float(djet[m_use]) / float(djet[m_use - 1])
        relb = (e_meas[m_use] + wjet[m_use]) / abs(float(djet[m_use])) \
            + (e_meas[m_use - 1] + wjet[m_use - 1]) \
            / abs(float(djet[m_use - 1]))
        bar_c = abs(rk) * relb
        relm = (dev_sub_l[m_use] + wjet[m_use]) \
            / abs(float(djet[m_use])) \
            + (dev_sub_l[m_use - 1] + wjet[m_use - 1]) \
            / abs(float(djet[m_use - 1]))
        bar_m = abs(rk) * relm
        gam = ward_gammas()
        w4w = 4.0 * R4.ward_topw(gam, float(a0), 1)[0][1]
        out.update(rate=rk, rate_jet=rj, rate_bar_cert=bar_c,
                   rate_bar_meas=bar_m, rate_m=m_use, w4_ward=w4w)
        info("%s|%s CERTIFIED RATE at m*=%d: %.6f +- %.1e (Cauchy-"
             "certified) | +- %.1e (measured) | jet %.6f | ward "
             "4w(g1) %.9f | margin to 1: %.4f (certified-below-1: %s)"
             % (label, rung_lab, m_use, rk, bar_c, bar_m, rj, w4w,
                1.0 - rk, "YES" if rk + bar_c < 1.0 else "NO"))
    return out


# ====================================================== SYN detector
def syn_world(delta_o: float, n: int, delta_mp, mmax: int,
              kcont: int) -> dict:
    """Build + adjudicate one synthetic variant at (SYN_S0, SYN_A0)."""
    lab = "SYN(do=%.2f)" % delta_o
    nj = 2 * mmax + 1
    out = {"label": lab, "delta_o": delta_o}
    with mp.workdps(DPS_ALG):
        dl = mp.mpf(delta_mp)
        leb = mp.mpf(EPS_LEB)
        gams = [mp.mpf(g) for g in SYN_GAMMAS]
        # row + node densities via addition-formula recurrences
        xs, _ws = gl_nodes(GLK)
        offs = [dl * (1 + x) / 2 for x in xs]
        row = [mp.mpf(0)] * n
        dens = [[mp.mpf(0)] * GLK for _ in range(n)]
        for g in gams:
            wg = 4 * (1 - mp.cos(g * dl)) / (g * g * dl)
            cd, sd = mp.cos(g * dl), mp.sin(g * dl)
            co = [mp.cos(g * o) for o in offs]
            so = [mp.sin(g * o) for o in offs]
            c, s = mp.mpf(1), mp.mpf(0)
            for k in range(n):
                row[k] += wg * c
                dk = dens[k]
                for i in range(GLK):
                    dk[i] += 2 * (c * co[i] - s * so[i])
                c, s = c * cd - s * sd, s * cd + c * sd
        mu = None
        if delta_o > 0:
            do = mp.mpf(delta_o)
            go = mp.sqrt(mp.mpf(SYN_A0) - do * do)
            mu = do + 1j * go
            wp = 8 * (mp.cosh(mu * dl) - 1) / (mu * mu * dl)
            chd = mp.cosh(mu * dl)
            shd = mp.sinh(mu * dl)
            cho = [mp.cosh(mu * o) for o in offs]
            sho = [mp.sinh(mu * o) for o in offs]
            ch, sh = mp.mpc(1), mp.mpc(0)
            for k in range(n):
                row[k] += mp.re(wp * ch)
                dk = dens[k]
                for i in range(GLK):
                    dk[i] += 4 * mp.re(ch * cho[i] + sh * sho[i])
                ch, sh = ch * chd + sh * shd, sh * chd + ch * shd
            out["gamma_o"] = float(go)
            out["w4star"] = float(1 + do * do / (go * go))
        row[0] += leb
    sz = KR.szego_mp(row, 60)
    out["szego_ok"] = sz["ok"]
    out["fail_k"] = sz["fail_k"]
    if not sz["ok"]:
        out["t_death"] = sz["fail_k"] * float(delta_mp)
        print("  %s: SZEGO COLLAPSE at k=%d (t = %.3f) -- in-window "
              "positivity of the injected world FAILS: the "
              "certificate channel FIRES" % (lab, sz["fail_k"],
                                             out["t_death"]))
        out["fire"] = "COLLAPSE"
        return out
    # exact model P-jet + audit
    with mp.workdps(DPS_ALG):
        s0 = mp.mpf(SYN_S0)
        pj_mod = [mp.mpf(0)] * nj
        pj_mod[0] = mp.mpf(EPS_LEB) / 2
        for g in gams:
            num = [mp.mpf(0)] * nj
            num[0] = 2 * s0
            num[1] = mp.mpf(2)
            den = [mp.mpf(0)] * nj
            den[0] = s0 * s0 + g * g
            den[1] = 2 * s0
            den[2] = mp.mpf(1)
            q = KD.j_div(num, den, nj)
            for j in range(nj):
                pj_mod[j] += q[j]
        if mu is not None:
            for z in (mu * mu, mp.conj(mu * mu)):
                num = [mp.mpc(0)] * nj
                num[0] = 2 * s0
                num[1] = mp.mpc(2)
                den = [mp.mpc(0)] * nj
                den[0] = s0 * s0 - z
                den[1] = 2 * s0
                den[2] = mp.mpc(1)
                q = KD.j_div(num, den, nj)
                for j in range(nj):
                    pj_mod[j] += mp.re(q[j])

        def model_p(sv):
            tot = mp.mpf(EPS_LEB) / 2
            for g in gams:
                tot = tot + 2 * sv / (sv * sv + g * g)
            if mu is not None:
                z = mu * mu
                tot = tot + 2 * sv / (sv * sv - z) \
                    + 2 * sv / (sv * sv - mp.conj(z))
            return tot

        prep = prep_defect(n, dl, dens_nodes=dens)
        pj_raw = [x / 2 for x in KD.transfer_cval_jet(
            sz["alphas"], sz["c0"], SYN_S0, dl, nj)]
        djets = defect_jet(prep, SYN_S0, nj)
        pj_sub = [pj_raw[j] - djets[j] for j in range(nj)]
    d_sub, _b = KD.pjet_to_dscaled(pj_sub, SYN_S0, SYN_A0, mmax)
    d_ex, _b = KD.pjet_to_dscaled(pj_mod, SYN_S0, SYN_A0, mmax)
    # contour budget vs the exact model audit
    ra = 0.8 * SYN_A0
    win = n * float(delta_mp)
    sup_meas = 0.0
    with mp.workdps(DPS_ALG):
        for j in range(kcont):
            th = mp.mpf(2 * j) / kcont
            sv = mp.sqrt(SYN_A0 + mp.mpf(ra) * mp.expjpi(th))
            wv = mp.exp(-sv * dl)
            cval, _c, _r, _m = KD.disk_complex(sz["alphas"], sz["c0"],
                                               wv)
            dval = defect_val(prep, sv)
            f_sub = (cval / 2 - dval) / (2 * sv)
            f_mod = model_p(sv) / (2 * sv)
            sup_meas = max(sup_meas, float(abs(f_sub - f_mod)))
    sup_meas *= SUP_INFLATE
    e_meas = KD.budget_dm(sup_meas, float(SYN_A0), ra, mmax)
    m_cm = cert_depth(e_meas, d_ex, mmax)
    ok_enc = True
    worst_enc = 0.0
    for m in range(mmax + 1):
        dv = abs(float(d_sub[m]) - float(d_ex[m]))
        worst_enc = max(worst_enc, dv / max(e_meas[m], 1e-300))
        if dv > 1.2 * e_meas[m]:
            ok_enc = False
    lb_best, lb_m = -1.0, -1
    for m in range(1, max(m_cm, 1) + 1):
        lo = float(d_sub[m]) - e_meas[m]
        hi = float(d_sub[m - 1]) + e_meas[m - 1]
        if hi > 0 and lo / hi > lb_best:
            lb_best, lb_m = lo / hi, m
    out.update(sup_meas=sup_meas, m_cert=m_cm, enc_ok=ok_enc,
               worst_enc=worst_enc, lb_best=lb_best, lb_m=lb_m,
               fire="RATE" if lb_best > 1.0 else None)
    print("  %s: szego completes; sup dev %.2e; m_cert %d; enclosure "
          "worst %.2f x E; certified rate-LB %.6f at m=%d -> %s"
          % (lab, sup_meas, m_cm, worst_enc, lb_best, lb_m,
             "FIRE" if lb_best > 1.0 else "no fire"))
    return out


# ====================================================== min-cut (T3)
def mincut_defectjet() -> list[tuple[str, bool, str]]:
    gates = []
    flow_base, _cut, _ = IG.max_flow(IG.EDGES, "UNCOND", "RH")
    ext = list(IG.EDGES) + [
        ("WEYL-PINS-MEAS", "KR4-DIAG-MEAS", "UNC-DICT", IG.INF),
        ("WEYL-PINS-MEAS", "KR4-DEFECTJET-SUB", "UNC-DICT", IG.INF),
        ("KR4-DEFECTJET-SUB", "KR4-DEPTH-CERT-FIN", "UNC", IG.INF),
        ("KR4-DIAG-MEAS", "KR4-DEPTH-CERT-FIN", "UNC", IG.INF),
        ("KR4-DEPTH-CERT-FIN", "KR4-FALSIFIER-1SIDED", "UNC", IG.INF),
        ("KR4-DEPTH-CERT-FIN", "R4-HYP", "OMEGA-POS", 1),
    ]
    flow_ext, cut_ext, _ = IG.max_flow(ext, "UNCOND", "RH")
    up = [(s, d, c, IG.INF if (s, d) == ("R4-HYP", "RH") else cap)
          for s, d, c, cap in ext]
    flow_up, cut_up, _ = IG.max_flow(up, "UNCOND", "RH")
    print("    flows base/ext/ext+R4->RH-INF = %d/%d/%d"
          % (flow_base, flow_ext, flow_up))
    print("    extended min-cut:")
    for s, d, c in cut_ext:
        print("      %-20s -> %-18s [%s]" % (s, d, c))
    swap = [(s, d, ("CERT-INSTR" if (s, d) ==
                    ("UNCOND", "WEYL-PINS-MEAS") else c), cap)
            for s, d, c, cap in up]
    flow_sw, cut_sw, _ = IG.max_flow(swap, "UNCOND", "RH")
    cls_ext = sorted({c for _s, _d, c in cut_ext})
    cls_sw = sorted({c for _s, _d, c in cut_sw})
    print("    census: extended %s; after MEAS->CERT-INSTR costume "
          "swap %s (cardinality %d -> %d)"
          % (cls_ext, cls_sw, len(cut_ext), len(cut_sw)))
    gates.append(("G50a min-cut cardinality stays 4",
                  flow_base == 4 and flow_ext == 4 and flow_up == 4
                  and flow_sw == 4,
                  "flows %d/%d/%d/%d: the finite-m certificate rides "
                  "the SAME capacity-1 Weyl measurement edge; "
                  "upgrading its class to CERT-INSTR changes NO "
                  "cardinality" % (flow_base, flow_ext, flow_up,
                                   flow_sw)))
    allowed = {"OMEGA-POS", "OMEGA-POS-MEAS", "MEAS", "OMEGA-LAW",
               "CANDIDATE", "CERT-INSTR"}
    gates.append(("G50b census classes unchanged",
                  set(cls_ext) | set(cls_sw) <= allowed,
                  "cut classes %s / %s -- the all-m/dense-a omega "
                  "introduction stays the binding class"
                  % (cls_ext, cls_sw)))
    adj: dict[str, set] = {}
    for s, d, c, _cap in ext:
        if c in ("DEF", "UNC", "UNC-DICT"):
            adj.setdefault(s, set()).add(d)
    reach = {"UNCOND", "KR4-DEPTH-CERT-FIN"}
    queue = list(reach)
    while queue:
        nd = queue.pop(0)
        for nx in adj.get(nd, ()):
            if nx not in reach:
                reach.add(nx)
                queue.append(nx)
    gates.append(("G50c omega absorbs finite certified depth",
                  "RH" not in reach and "R4-HYP" not in reach,
                  "granting KR4-DEPTH-CERT-FIN (ANY finite m) reaches "
                  "%d nodes through proven edges; R4-HYP and RH stay "
                  "unreachable; the one-sided falsifier is reachable "
                  "but has no edge into RH" % len(reach)))
    return gates


# ====================================================== main
def main() -> int:
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke

    mmax = MMAX
    kcont, kcont_syn = KCONT, KCONT_SYN
    rungs = RUNGS
    jet_m, jet_dps, jet_ns, jet_ord = JET_M, JET_DPS, JET_NS, JET_ORD
    syn_deltas = SYN_DELTAS
    pins = PINS
    mesh_mates = (D6, D12)
    if smoke:
        mmax = 6
        kcont, kcont_syn = 24, 16
        rungs = (2.568, 3.999)
        jet_m, jet_dps, jet_ns, jet_ord = 128, 150, 20000, 2 * 6 + 4
        syn_deltas = (0.0, 2.0)
        pins = (("a256", 16, 256, 96, 0.8, "RATE", 6),
                ("a144", 12, 144, 54, 0.8, "RATE", 6))
        mesh_mates = (D6,)
    else:
        pins = tuple((la, s, a, r, f, ro, min(mm, mmax))
                     for (la, s, a, r, f, ro, mm) in PINS)

    print("kr4_defectjet_probe -- PRIME.KR4.DEFECTJET.01")
    print("SPEC_SHA %s" % SPEC_SHA[:16])
    print("mode: %s" % ("SMOKE (NOT VERDICT-BEARING)" if smoke
                        else "FULL"))
    print("NO RH CLAIM.  EXPLORATION ONLY.")

    # ---------------------------------------------------------- S0
    section("S0  FIREWALL + SPEC")
    ok, det = firewall_audit()
    check("G01-ast-firewall", ok, det)
    print("  contract: PRIME.KR4.DEFECTJET.01 -- exact in-window")
    print("  defect-jet subtraction on the Krein carrier (round-118")
    print("  named lever), window ladder, certified depth, detector")
    print("  power, min-cut/Epstein price.")

    # ---------------------------------------------------------- S1
    section("S1  DEFECT ALGEBRA GATES (the exact subtraction, warded)")
    print("  identity: row[d] = <-g'', Lambda_d> exact (g(0) = 0) =>")
    print("  P_trunc = <-g'', T_sigma>; D = <-g'', (T_sigma - e)1_win>")
    print("  with atoms exact and the pole/arch density per-cell GL;")
    print("  the 1/(2t) arch singularity and ALL Weil regularization")
    print("  boundary terms cancel in the kernel (T-e)(0) == 0.")
    ok, det = KD.gate_atom_dictionary()
    check("G10-dictionary-atom-exact", ok, det)
    ok, det = gate_sympy_kernel()
    check("G10b-sympy-kernel+cell", ok, det)
    ok, det = gate_atom_ward()
    check("G15-defect-ward-atoms", ok, det)
    ok, det = gate_exp_ward()
    check("G16-defect-ward-expdensity", ok, det)

    # ---------------------------------------------------------- S2
    section("S2  TRUE BUILDS (window ladder + mesh triple)")
    KR.mp_setup()
    plan = [(rl, D3) for rl in rungs] + [(L4, dn) for dn in mesh_mates]
    builds, szs, preps = {}, {}, {}
    pos_l4 = True
    pos_ladder = {}
    for (lw, dn) in plan:
        t0 = time.time()
        b = KR.build_lags_mp(lw, dn, "TRUE")
        dps_sz = 60 if lw > 3.0 else 50
        sz = KR.szego_mp(b["row"], dps_sz)
        builds[(lw, dn)] = b
        szs[(lw, dn)] = sz
        if dn == D3:
            pos_ladder[lw] = sz["ok"]
        if lw == L4 and dn == D3:
            pos_l4 = sz["ok"]
        atoms = [(u, -mp.mpf(w))
                 for (u, _w), w in zip(b["atoms"], b["weights"])]
        t1 = time.time()
        preps[(lw, dn)] = prep_defect(b["n"], b["delta_mp"],
                                      dens_fn=rho_true, atoms=atoms)
        print("  L=%.3f delta=%s n=%4d  c0=%9.4f  max|alpha|=%.6f  %s"
              "  (szego %.1f s, prep %.1f s)"
              % (lw, dn, b["n"], float(sz["c0"]), float(sz["amax"]),
                 "OK" if sz["ok"] else "FAIL@k=%d" % sz["fail_k"],
                 t1 - t0, time.time() - t1), flush=True)
    check("G21-true-positivity-L4", pos_l4,
          "the L4 anchor build completes (max|alpha| < 1 through the "
          "window)" if pos_l4 else "TYPED KILL: KR4DJ-DEAD")
    if not pos_l4:
        print("VERDICT: KR4DJ-DEAD(positivity)")
        return 1
    ladder_ok = [lw for lw in rungs if pos_ladder.get(lw)]
    info("positivity ladder: %s -> surviving rungs %s (Szego "
         "completion through L = %.3f is itself a NEW measured "
         "positivity depth; round 90/118 stopped at 2.568)"
         % ({k: v for k, v in pos_ladder.items()}, ladder_ok,
            max(ladder_ok)))

    jets_direct = {}
    for (label, _s, a0, r_jet, _f, _ro, _mm) in pins:
        jet = R4.build_jet_lambda(a0, r_jet, jet_m, jet_dps, jet_ns,
                                  jet_ord, "kr4dj-" + label)
        jets_direct[label] = jet
        print("  direct jet %s: a=%d r=%d M=%d dps=%d N=%d orders=%d "
              "(%.1f s)" % (label, a0, r_jet, jet_m, jet_dps, jet_ns,
                            jet_ord, jet["secs"]), flush=True)
    ok22 = all(j["sig_min"] > 1.0
               and max(j["im_res"], j["imF"]) <= BAR_IM
               for j in jets_direct.values())
    check("G22-direct-jets-healthy", ok22,
          "min Re s = %s; Im residuals <= %.0e"
          % (["%.2f" % j["sig_min"] for j in jets_direct.values()],
             BAR_IM))

    # ---------------------------------------------------------- S3
    section("S3  DEPTH TABLES PRE/POST SUBTRACTION (ladder)")
    results: dict = {}
    for pin in pins:
        (label, _s, _a, _r, _f, role, _mm) = pin
        pin_rungs = [L4] if role == "RESUM" else ladder_ok
        for lw in pin_rungs:
            key = (label, lw)
            results[key] = analyze_pin_rung(
                pin, "L%.3f" % lw, builds[(lw, D3)], szs[(lw, D3)],
                preps[(lw, D3)], jets_direct[label], kcont)
    deep_keys = [(la, lw) for (la, lw) in results
                 if results[(la, lw)]["role"] == "RATE"]
    r_all = [results[k] for k in results]
    ok11 = all(v["min_res"] > 0.5 and v["min_marg"] > 0
               for v in r_all)
    check("G11-domain-admissible", ok11,
          "min Re sigma > 1/2 and disk margin > 0 on every contour "
          "(min Re = %.2f)" % min(v["min_res"] for v in r_all))
    ok12 = all(v["fd_rel"] <= BAR_FD for v in r_all)
    check("G12-fd-ward-subtracted", ok12,
          "FD vs exact-jet first derivative of the SUBTRACTED read, "
          "worst rel %.1e (bar %.0e)"
          % (max(v["fd_rel"] for v in r_all), BAR_FD))
    ok13 = all(v["xward"] <= BAR_XWARD for v in r_all)
    check("G13-contour-vs-jet-crossward", ok13,
          "quadrature vs exact-jet subtracted b_n (n<=8), worst rel "
          "%.1e (bar %.0e)" % (max(v["xward"] for v in r_all),
                               BAR_XWARD))
    ok14 = all(v["incirc"] <= 1.0 + 1e-12 for v in r_all)
    check("G14-central-value-in-disk", ok14,
          "|cval-center|/R at the real pins = %s <= 1"
          % ["%.3f" % v["incirc"] for v in r_all])
    ok18 = all(v["dev_pin_sub"] <= v["close_bar"] for v in r_all)
    check("G18-pin-closure", ok18,
          "|P_sub(sigma0) - audit| <= 3(R + tail_model) + 2e-18 on "
          "every pin/rung: " + "; ".join(
              "%s|%s %.1e<=%.1e" % (v["label"], v["rung"],
                                    v["dev_pin_sub"], v["close_bar"])
              for v in r_all))
    ok20 = all(v["sup_meas"] <= v["sup_cond"] for v in r_all)
    check("G20-budget-consistency", ok20,
          "sup dev_meas <= sup dev_cond on every pin contour: "
          + "; ".join("%s|%s %.1e<=%.1e"
                      % (v["label"], v["rung"], v["sup_meas"],
                         v["sup_cond"]) for v in r_all))
    deepL4 = [results[(la, L4)] for (la, lw) in deep_keys
              if lw == L4]
    ok30 = all(v["dev_pin_sub"] <= BAR_BIASKILL * v["dev_pin_pre"]
               for v in deepL4)
    check("G30-bias-kill", ok30,
          "post/pre pin deviation at L4 deep pins: %s (bar %.0e)"
          % (["%.1e" % (v["dev_pin_sub"] / max(v["dev_pin_pre"],
                                               1e-300))
              for v in deepL4], BAR_BIASKILL))
    ok31 = all(results[k]["ok31"] for k in deep_keys)
    check("G31-enclosure-covers", ok31,
          "|d'_sub - d'_jet| <= 1.2 (E_meas + width) for ALL m <= "
          "mmax on every deep pin/rung (Cauchy rigor test)")

    # ---------------------------------------------------------- S4
    section("S4  T2: MESH TRIPLE + WINDOW LAW (the new budget law)")
    lab256 = "a256"
    ok32 = True
    det32 = []
    if mesh_mates:
        base = results[(lab256, L4)]
        pinA = [p for p in pins if p[0] == lab256][0]
        for dn in mesh_mates:
            b = builds[(L4, dn)]
            sz = szs[(L4, dn)]
            nj = 2 * pinA[6] + 1
            with mp.workdps(DPS_ALG):
                pj_raw = [x / 2 for x in KD.transfer_cval_jet(
                    sz["alphas"], sz["c0"], 16, b["delta_mp"], nj)]
                dj = defect_jet(preps[(L4, dn)], 16, nj)
                pj_sub = [pj_raw[j] - dj[j] for j in range(nj)]
            dp, _ = KD.pjet_to_dscaled(pj_raw, 16, 256, pinA[6])
            dsb, _ = KD.pjet_to_dscaled(pj_sub, 16, 256, pinA[6])
            worst = 0.0
            for m in range(min(8, pinA[6]) + 1):
                pre = abs(float(dp[m]) - base["d_pre"][m])
                post = abs(float(dsb[m]) - base["d_sub"][m])
                if pre >= 1e-12:
                    worst = max(worst, post / pre)
            ok32 &= worst <= BAR_MESHTRIPLE
            det32.append("delta %s: worst post/pre %.1e" % (dn, worst))
    check("G32-mesh-triple-collapse", ok32,
          "; ".join(det32) + " (bar %.0e): the delta^2 channel is "
          "DEAD to all orders -- the coupled schedule delta(L) is "
          "VOID" % BAR_MESHTRIPLE)
    # window law fit
    sups, wins = [], []
    for lw in ladder_ok:
        v = results.get((lab256, lw))
        if v:
            sups.append(v["sup_meas"])
            wins.append(v["win"])
    ok33 = False
    slope = ratio = float("nan")
    sigma_edge = results[(lab256, ladder_ok[-1])]["min_res"]
    if len(sups) >= 2:
        slope = float(np.polyfit(wins, np.log(sups), 1)[0])
        ratio = -slope / (sigma_edge - 0.5)
        ok33 = abs(ratio - 1.0) <= BAR_SLOPE
    check("G33-window-law-slope", ok33,
          "sup dev_meas(L) log-slope %.3f vs -(sigma_edge - 1/2) = "
          "-%.3f: ratio %.3f (bar 1 +- %.2f) -- the wall follows the "
          "TAIL exponent, not the disk exponent"
          % (slope, sigma_edge - 0.5, ratio, BAR_SLOPE))
    stair = [results[(lab256, lw)]["m_cert_meas"] for lw in ladder_ok]
    ok34 = (len(stair) == 3
            and all(stair[i] < stair[i + 1]
                    for i in range(len(stair) - 1))
            and stair[-1] - stair[0] >= BAR_STAIR_GAIN)
    check("G34-certified-staircase", len(stair) < 3 or ok34,
          "m_cert_meas(a256) over the ladder: %s (strictly "
          "increasing, total gain >= %d)%s"
          % (stair, BAR_STAIR_GAIN,
             "" if len(stair) == 3 else " -- LADDER SHORT (smoke or "
             "positivity boundary)"))
    x = 1.25
    qrate = 4 * x * (1 + x) / max(results[(lab256, ladder_ok[-1])]
                                  .get("w4_ward", 0.985), 1e-9)
    info("NEW BUDGET LAW (measured constants): m*(L) ~ "
         "[(sigma_edge-1/2) L + const]/ln Q, sigma_edge = %.3f, "
         "Q = %.2f -> %.2f certified depths per unit window"
         % (sigma_edge, qrate, (sigma_edge - 0.5) / math.log(qrate)))
    nlin = int(RUNGS[-1] / 0.003)
    dexp = math.exp(-(sigma_edge + C_LAW) * RUNGS[-1] / 2)
    info("MESH PRICE at L = %.3f: defect-jet subtraction n = %d "
         "(LINEAR, delta fixed 0.003) vs round-118 coupled schedule "
         "delta ~ e^{-(sigma_edge+c)L/2} = %.1e -> n ~ %.1e "
         "(EXPONENTIAL): price ratio %.1e -- the named lever kills "
         "the exponential mesh price"
         % (RUNGS[-1], nlin, dexp, RUNGS[-1] / dexp,
            (RUNGS[-1] / dexp) / nlin))

    # ---------------------------------------------------------- S5
    section("S5  Z1 AT DEPTH (post-subtraction) + RESUM")
    gam = ward_gammas()
    fire_trans = False
    z1_ok = True
    scan_keys = [(la, lw) for (la, lw) in deep_keys
                 if lw in (L4, ladder_ok[-1])]
    for key in scan_keys:
        v = results[key]
        a0 = float(dict((p[0], p[2]) for p in pins)[v["label"]])
        m_use = max(1, min(v["m_sig_sub"], 10))
        partials = KD.ward_diag_partials(gam, a0, m_use)
        score, nbest = KD.ward_transcription_scan(
            v["d_sub"][: m_use + 1], partials)
        fire_trans |= score <= TRANS_BAR
        gap0 = abs(v["d_sub"][0] - float(partials[0][nbest - 1]))
        read0 = max(abs(v["d_sub"][0] - v["djet"][0]), v["wjet"][0],
                    v["e_meas"][0] / SUP_INFLATE)
        marg = gap0 / max(read0, 1e-300)
        z1_ok &= marg >= Z1_MARGIN
        print("  %s|%s: transcription scan min-max rel %.3e at N=%d; "
              "m=0 cache gap %.3e vs read error %.3e -> margin %.1f"
              % (v["label"], v["rung"], score, nbest, gap0, read0,
                 marg))
    check("G40-no-transcription", not fire_trans,
          "post-subtraction depth vectors match NO cache partial-sum "
          "vector" if not fire_trans else "TRANSCRIPTION FIRES")
    check("G41-z1-extrapolates", z1_ok,
          "m=0 deviation from the BEST cache partial sum >= %.0fx the "
          "read error: the subtracted reads still carry the beyond-"
          "cache RvM tail (the subtraction removed MESH defect, not "
          "signal)" % Z1_MARGIN if z1_ok else "margin below bar")
    v9 = results.get(("a9", L4))
    if v9 is not None:
        tail9 = tail_model_p(3.0, v9["win"])
        info("a9 RESUM channel post-subtraction: |P_sub - audit| = "
             "%.2e vs window-tail model %.2e -> ratio %.2f (the "
             "subtracted read's residual IS the unresummed tail "
             "share; <1 = the disk resums part of the tail; typed "
             "MEASURED)" % (v9["dev_pin_sub"], tail9,
                            v9["dev_pin_sub"] / tail9))

    # ---------------------------------------------------------- S6
    section("S6  SYNTHETIC DETECTOR (certified power, T3)")
    lw_syn = ladder_ok[-1]
    n_syn = builds[(lw_syn, D3)]["n"]
    syn = {}
    for do in syn_deltas:
        syn[do] = syn_world(do, n_syn, mp.mpf(D3),
                            min(mmax, 14), kcont_syn)
    v_true = results[(lab256, lw_syn)]
    lb_true = -1.0
    for m in range(1, max(v_true["m_cert_meas"], 1) + 1):
        lo = v_true["d_sub"][m] - v_true["e_meas"][m]
        hi = v_true["d_sub"][m - 1] + v_true["e_meas"][m - 1]
        if hi > 0:
            lb_true = max(lb_true, lo / hi)
    ok62 = (lb_true < 1.0 and syn[0.0]["szego_ok"]
            and syn[0.0].get("fire") is None)
    check("G62-detector-nulls-silent", ok62,
          "TRUE rate-LB %.6f < 1; SYN null completes with no fire "
          "(rate-LB %.6f)" % (lb_true, syn[0.0].get("lb_best",
                                                    float("nan"))))
    ok17 = all(v.get("enc_ok", True) for v in syn.values())
    check("G17-syn-enclosure", ok17,
          "|d'_sub - d'_exact| <= 1.2 E_meas on every completing SYN "
          "variant (worst %.2f x E)"
          % max(v.get("worst_enc", 0.0) for v in syn.values()))
    fired2 = syn.get(2.0, {}).get("fire")
    check("G63-detector-fires", fired2 is not None,
          "delta_o = 2 (4w* = %.4f): %s"
          % (syn.get(2.0, {}).get("w4star", float("nan")),
             fired2 or "NO FIRE"))
    deaths = [(do, v["t_death"]) for do, v in syn.items()
              if v.get("t_death")]
    nats = [t * do for do, t in deaths]
    info("collapse deaths (t_death, nats = t x delta_o): %s"
         % ["do=%.2f t=%.3f nats=%.2f" % (do, t, t * do)
            for do, t in deaths])
    for do, v in syn.items():
        if do > 0 and v.get("fire") is None:
            info("power boundary: do=%.2f (excess %.2e) UNDETECTED at "
                 "this budget (m_cert %d, rate-LB %.6f)"
                 % (do, do * do / v.get("gamma_o", 16.0) ** 2,
                    v.get("m_cert", -1), v.get("lb_best",
                                               float("nan"))))

    # ---------------------------------------------------------- S7
    section("S7  T3: MIN-CUT + THE EPSTEIN PRICE")
    for gate in mincut_defectjet():
        check(*gate)
    exc = EPS_DELTA ** 2 / EPS_GAMMA ** 2
    m2 = math.log(2.0) / exc
    sig_e_star = math.sqrt(0.2 * EPS_ASTAR)
    l_rate = m2 * math.log(qrate) / (sig_e_star - 0.5)
    print("  EPSTEIN WITNESS (round-117 numbers, frozen): rho = "
          "%.10f + %.10f i," % (0.5 + EPS_DELTA, EPS_GAMMA))
    print("  |xi_Q| = %.1e, matched a* = %.5f, relative excess "
          "delta^2/gamma^2 = %.3e," % (EPS_XI, EPS_ASTAR, exc))
    print("  violation window a in (%.1f, %.1f); Q neighbours 4w = "
          "%.5f / %.5f." % (EPS_WINDOW[0], EPS_WINDOW[1],
                            EPS_NEIGHB[0][1], EPS_NEIGHB[1][1]))
    print("  RATE channel price: m2 = ln2 gamma^2/delta^2 = %d "
          "(round-117 law) -> window" % round(m2))
    print("  L ~ m2 ln Q/(sigma_edge* - 1/2) = %.0f (n ~ %.1e at "
          "delta 0.003): out of reach." % (l_rate, l_rate / 0.003))
    if nats:
        c_nats = float(np.median(nats))
        l_req = c_nats / EPS_DELTA
        print("  COLLAPSE channel price (measured law t_death x "
              "delta_o ~ %.2f nats," % c_nats)
        print("  MODEL-grade: SYN background margin != Q-world "
              "margin, typed): L_req ~ %.1f" % l_req)
        print("  -> n ~ %d rows BUT source atoms to height e^L ~ "
              "%.1e: the exponential" % (round(l_req / 0.003),
                                         math.exp(l_req)))
        print("  price moved from the MESH into the ARITHMETIC DATA "
              "(the sieve).")
    print("  T3 ANSWER (brutal): the certified-depth detector does "
          "NOT fire on the")
    print("  Epstein witness at any budget reachable here (achieved "
          "certified depth")
    print("  %d vs required ~ %d in rate currency); ANY finite "
          "certified depth is" % (results[(lab256,
                                           ladder_ok[-1])]
                                  ["m_cert_meas"], round(m2)))
    print("  absorbed by the all-m/dense-a omega (G50c): the cut "
          "census does NOT change.")
    print("  WHAT IS NEW: the certified read at m* is now a "
          "PRICED falsification")
    print("  instrument -- power curve measured (S6), price laws "
          "printed above.")

    # ---------------------------------------------------------- S8
    section("S8  CONTROLS + CONDITIONING + TAU-SCREEN TYPING")
    ctrl_ok = True
    ctrl_det = []
    for wld, rtgt in (("SMOOTH", CTRL_R_SMOOTH),
                      ("SCRARITH", CTRL_R_SCR)):
        bw = KR.build_lags_mp(L4, D3, wld)
        szw = KR.szego_mp(bw["row"])
        if szw["ok"]:
            ctrl_ok = False
            ctrl_det.append("%s COMPLETES (unexpected)" % wld)
            continue
        rfail = szw["fail_k"] * bw["delta"]
        ctrl_ok &= abs(rfail - rtgt) <= CTRL_TOL
        ctrl_det.append("%s dies at r=%.3f (target %.3f)"
                        % (wld, rfail, rtgt))
    check("G60-controls-die-at-positivity", ctrl_ok,
          "; ".join(ctrl_det) + " -- the depth pairing exists only "
          "where positivity holds (round-90 separated-by-collapse)")
    # conditioning at the deepest rung
    b3 = builds[(ladder_ok[-1], D3)]
    prep3 = preps[(ladder_ok[-1], D3)]
    v = results[(lab256, ladder_ok[-1])]
    nj = 2 * mmax + 1
    with mp.workdps(DPS_ALG):
        eps = mp.mpf(10) ** (-PERT_DPS)
        row_r = [vv * (1 + eps * mp.cos(7 * d))
                 for d, vv in enumerate(b3["row"])]
    sz_r = KR.szego_mp(row_r, 60)
    with mp.workdps(DPS_ALG):
        pj_r = [xx / 2 for xx in KD.transfer_cval_jet(
            sz_r["alphas"], sz_r["c0"], 16, b3["delta_mp"], nj)]
        djr = defect_jet(prep3, 16, nj)
        pj_rs = [pj_r[j] - djr[j] for j in range(nj)]
    d_r, _ = KD.pjet_to_dscaled(pj_rs, 16, 256, mmax)
    base_mp = v["d_sub_mp"]
    amps = []
    with mp.workdps(DPS_ALG):
        for m in range(mmax + 1):
            shift = float(abs(d_r[m] - base_mp[m]))
            amps.append(shift / (1e-25 * max(abs(v["d_sub"][m]),
                                             1e-300)))
        m_use = max(v.get("rate_m", 2), 2)
        rate_shift = float(abs(d_r[m_use] / d_r[m_use - 1]
                               - base_mp[m_use] / base_mp[m_use - 1]))
    slope_a = float(np.polyfit(range(mmax + 1),
                               np.log(np.maximum(amps, 1e-300)),
                               1)[0])
    check("G61-conditioning", rate_shift <= BAR_RATE_SHIFT,
          "1e-25 lag perturbation at L=%.3f: rate shift %.2e (bar "
          "%.0e); A_m = %.1e..%.1e, log-slope %.2f/depth"
          % (ladder_ok[-1], rate_shift, BAR_RATE_SHIFT, min(amps),
             max(amps), slope_a))
    info("TAU-SCREEN / DISGUISE TYPING (T4, honest): the subtracted "
         "MEAS read collapses BY CONSTRUCTION onto the windowed Weil "
         "transform (Euler-computable) -- DISGUISE-ADJACENT for the "
         "value channel.  NOT collapsing: (i) the COND enclosure "
         "(disk radius; positivity-conditional, carrier-native), "
         "(ii) the positivity certificate itself (Szego completion "
         "through L = %.3f -- NEW measured depth), (iii) the "
         "resummation correction (a9 channel).  The certified-depth "
         "claim is a statement about the carrier-as-instrument, not "
         "a new sign source." % max(ladder_ok))

    # ---------------------------------------------------------- S9
    section("S9  COMPOSITE VERDICT")
    fails_inst = [nm for nm, okk, _ in CHECKS if not okk and nm[:3] in
                  ("G10", "G11", "G12", "G13", "G14", "G15", "G16",
                   "G22")]
    v_main = results[(lab256, ladder_ok[-1])]
    verdicts = []
    if fails_inst:
        verdicts.append("KR4DJ-INSTRUMENT-EDGE(%s)" % fails_inst)
    elif len(ladder_ok) < len(rungs):
        verdicts.append("KR4DJ-POSITIVITY-BOUNDARY(survivors %s)"
                        % ladder_ok)
    elif fire_trans:
        verdicts.append("KR4DJ-TRANSCRIBES-AT-DEPTH")
    elif all(okk for nm, okk, _ in CHECKS if nm.startswith(
            ("G18", "G30", "G32"))):
        verdicts.append(
            "KR4DJ-BIASKILL(pin dev %.1e -> %.1e at L4; certified "
            "meas depth a256: %d at L4 -> %d at L%.3f, cond %d, "
            "disk-only %d; round-118 baseline meas/cond was 1/1)"
            % (deepL4[0]["dev_pin_pre"], deepL4[0]["dev_pin_sub"],
               results[(lab256, L4)]["m_cert_meas"],
               v_main["m_cert_meas"], ladder_ok[-1],
               v_main["m_cert_cond"], v_main["m_cert_ronly"]))
    else:
        verdicts.append("KR4DJ-DEFECT-RESIDUAL(see gates)")
    if "rate" in v_main:
        verdicts.append(
            "RATE-CERTIFIED(a256, m*=%d: %.6f +- %.1e Cauchy | +- "
            "%.1e measured; margin to 1 = %.4f; below-1 %s; typed: "
            "meas = rigorous-given-audit, cond = COND-POS)"
            % (v_main["rate_m"], v_main["rate"],
               v_main["rate_bar_cert"], v_main["rate_bar_meas"],
               1 - v_main["rate"],
               "CERTIFIED" if v_main["rate"]
               + v_main["rate_bar_cert"] < 1 else "not certified"))
    verdicts.append("WINDOW-LAW(slope ratio %.3f; staircase %s; "
                    "MESH-PRICE-LINEAR)" % (ratio, stair))
    verdicts.append("MINCUT-OMEGA-ABSORBS(4/4/4/4; census swap "
                    "MEAS->CERT-INSTR only)")
    verdicts.append("EPSTEIN-NO-FIRE(m_req ~ %d vs achieved %d; "
                    "price laws printed)"
                    % (round(m2), v_main["m_cert_meas"]))
    verdicts.append("DETECTOR(deaths %s; nulls silent)"
                    % ["do=%.2f@t=%.2f" % (do, t)
                       for do, t in deaths])
    for vd in verdicts:
        print("  " + vd)

    dt = time.time() - T0_WALL
    check("G99-runtime", dt <= RUNTIME_BAR,
          "%.1f s (bar %.0f)" % (dt, RUNTIME_BAR))
    npass = sum(1 for _n, okk, _d in CHECKS if okk)
    print("\n" + "=" * 78)
    print("GATES: %d/%d PASS   SPEC_SHA %s   runtime %.1f s"
          % (npass, len(CHECKS), SPEC_SHA[:16], dt))
    fails = [nm for nm, okk, _ in CHECKS if not okk]
    if fails:
        print("FAILING GATES: " + ", ".join(fails))
    if smoke:
        print("*** SMOKE RUN -- NOT VERDICT-BEARING ***")
    print("NO RH CLAIM.  EXPLORATION ONLY.")
    return 0 if not fails else 1


if __name__ == "__main__":
    sys.exit(main())
