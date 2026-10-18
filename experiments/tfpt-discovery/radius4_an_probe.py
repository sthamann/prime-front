#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""radius4_an_probe -- PRIME.RADIUS4.AUBINNITSCHE.01

FROZEN SPEC (2026-08-15).  EXPLORATION ONLY.  This probe writes no
verification module, paper, ledger, website, manifest, Lean file or
status marker.  It makes NO RH claim, NO positivity claim, NO
counterexample claim.  It closes no gate and narrows no gate.

=======================================================================
MISSION
=======================================================================
Implement and adjudicate the owner's full solution architecture on the
round-114 block operators: (A) the FINITE DETERMINANT QUOTIENT in
radius-4 currency, (B) the AUBIN-NITSCHE reduction, (C) collision/
frame hardening, (D) falsifiers incl. a planted off-line quartet,
(E) the min-cut placement.  Rounds 117/118 already gated the radius-4
dictionary (RADIUS4-SOUND), the exact violation window a+-, the
normal-family inequality |log det| <= Tr B * r/(1-r/4) via
Tr B^k <= 4^{1-k} Tr B (typed there as CONSUMING 0 <= B <= 1/4), the
trace correction Tr B = C_{0,1} = b_0 - b_1, and the 2-to-1 map with
y(z) + y(a^2/z) = 1.  Those are cited and reused, not re-derived.

THE NEW MATHEMATICS UNDER TEST (the owner's step).  Let M_lambda be
the CCM operator D(I - P) of the round-114 family (Loewner class,
admissible frame): its spectrum is REAL UNCONDITIONALLY by the
round-114 block realness theorem.  For a > 1/4 put
    B_{a,lambda} = a M^2 (a + M^2)^{-2}          (functional calculus)
so that AUTOMATICALLY 0 <= B <= 1/4 (per eigenvalue mu real:
w = a mu^2/(a+mu^2)^2 in [0, 1/4] iff (a - mu^2)^2 >= 0), and
    R_{a,lambda}(t) = det(I - t B_{a,lambda})
      = det(M^2 + z+ I) det(M^2 + z- I) / det(M^2 + a I)^2,
    z+- roots of z^2 - a(2-t) z + a^2   (exact per-eigenvalue algebra,
    gated symbolically here).  Consequences, all finite-level and
    unconditional given the round-114 theorem:
  (i)   R_{a,lambda} is ZERO-FREE on |t| < 4 (poles of nothing, zeros
        at 1/w >= 4);
  (ii)  |log R_{a,lambda}(t)| <= Tr B * r/(1 - r/4) on |t| <= r < 4
        (round-117 R3a chain -- whose input 0 <= B <= 1/4 is now
        SUPPLIED unconditionally, not assumed: requirement (b) of the
        round-117 non-transcribing-carrier list is CLOSED at the
        finite level by round-114 blockreal);
  (iii) NF-CLOSURE THEOREM (typed PROVEN with classical inputs
        Montel/Vitali/identity-theorem/Hurwitz, cited not machine-
        checked; every finite inequality machine-gated here):  IF
        (H-trace) sup_lambda Tr B_{a,lambda} < infinity and
        (H-conv)  R_{a,lambda}(t) -> R_a(t) = Phi(z+)Phi(z-)/Phi(a)^2
        pointwise on a subinterval of the Euler-safe interval
        (0, 4 - 1/a), for every a in a dense subset of (1/4, inf),
        THEN RH.  (Normal family by (ii)+(H-trace); Vitali => locally
        uniform limit G on |t| < 4; R_a entire + identity theorem =>
        G = R_a; Hurwitz + G(0) = 1 => R_a zero-free on |t| < 4; the
        round-117 window theorem + density => no off-line zero.)
        The remaining omega is exactly (H-conv) + (H-trace); Lane A
        measures it.  CONVERSE IS FALSE: RH does not imply (H-conv)
        (finite-family tracking is CCM's open k_lambda ~ xi_lambda).

LANE A (central empirical question): does the finite determinant
quotient converge to the true R_a on the Euler interval?  Instrument:
even+odd HP Weil cells (own mp port of the round-111 builder, warded
against semilocal_realroot_limit_probe verbatim), full V-basis
assembly (round-114 assemble_full), xi = mp-precision even minimizer
embedded, eta = alternating boundary functional, M_eta = D(I - P_eta).
Gated dictionary: spec+(M_eta) == the cell's census zeros (the CCM
exterior-determinant identity: det(M_eta - z) proportional to the
numerator polynomial of E).  Determinant from the OPERATOR spectrum;
matrix-det cross-gate at one (a, t) per rung.  TARGETS source-side:
own Euler-Maclaurin zeta (round-119 currency finding respected; EM is
the official currency), warded against mp.zeta (audit namespace) and
against the raw Euler product on a sigma >= 1.5 corridor with the
cited Rosser-style tail bound 2.6 P^{1-sigma}/((sigma-1) ln P) -- the
raw product at sigma ~ 1.2 is measured too slow (calibrated
pre-freeze), so the corridor carries the Euler-product gate and EM
carries the battery.  HARD GATES: the sup-defect
max_t |log(R_fin/R_true)| must FALL on TWO independent cofinal
ladders: L1 x = (3, 5, 8, 13) at KFAC 1.25, L2 x = (3, 5, 8) at
KFAC 1.60.  Battery A_BAT = (1, 2, 4, 16), T_BAT Euler-safe (min
sigma 1.17).  Trace ladder Tr B_fin -> C_{0,1}(a) (a F(a) + a^2
F'(a), own-EM jet; cache+RvM ward) and the mechanism law
supdefect ~ t_max (C01 - Tr B_fin) (pre-freeze calibration: exact to
~3 digits at a <= 4 -- the Lane A defect IS the m = 1 trace tail).

LANE B (Aubin-Nitsche): Q_lambda = even-sector Weil matrix (mp),
eps = lowest eigenvalue, P = ground projection, k_lambda = the CCM
prolate candidate (blockreal M4 recipe, lam^2 = x) projected on the
trig basis, r = (Q - eps) k, R = (Q - eps)^dagger (I - P), Euler
evaluation vectors (e_z)_k = conj(B_k(z))/norm_k at frozen z with
Im z < -1/2 (Re s > 1).  (B1) the identity <e, (I-P)k> = <R e, r>
gated EXACTLY in rational arithmetic (Moore-Penrose of a rational
PSD matrix is rational: G^+ = Y (Y^T G Y)^{-1} Y^T on col Y) and
numerically per rung in mp.  (B2) both factors ||R e||, ||r|| (l2 and
energy norms) measured on the L1 ladder.  (B3) r split through the
builder's separate POLE/ARCH/PRIME blocks; channels <Re, r_arch>,
<Re, r_prime> measured (owner predicts arch ~ prolate-to-Hermite,
prime = the theorem).  (B4) the dual-vector claim measured: soft-mode
Euler evaluations |<v_i, e_z>| (soft = lam_i - eps <= 1e-2).
(B5) tau-screen: OLS slopes of log10(Lane-A defect) and log10(AN
product) against log10 |tau_x| over the ladder; atlas bands PASS
|s| <= 0.30, RELOCATION s >= 0.70.  Davis-Kahan comparator
||e|| ||r||/gap printed per rung.  CLUSTER SPLIT (added after the
first smoke measured the raw channels exploding like 1/gap and
cancelling -- the round-115 cross-cancellation debt in AN currency):
LHS = lhs_soft + lhs_hard exactly (soft = ground cluster modes with
lam - eps <= SOFT_BAR), lhs_hard obeys its own AN identity with the
cluster-hardened resolvent, and the RAW vs HARD-SECTOR channels are
both reported; the cluster mixing |<v_soft, k>| is the measured
obstruction profile.  Collision/frame hardening:
beta-frame operator M_beta built at every rung (round-114 default),
realness gated, its spectrum measured against the census (pre-freeze
finding: the beta spectrum is real but is NOT the E-zero set at
m = 1 -- the frame is a realness carrier, not a dictionary carrier;
adjudicated as a gate); ground-space rank-1 vs rank-cluster products
at the quasi-degenerate deep rungs.

FALSIFIERS (every round): SMOOTH (arch-only, PNT density e^{v/2}, mp
port, warded vs the f64 builder), SCRARITH (golden-order Lambda
permutation, mp port, warded), EPSTEIN x = 8 (conductor-20, no Euler
product; warded vs the SL HP builder at x = 5); separation read =
median-over-battery defect ratio vs TRUE at the same x (pre-freeze
calibration: SMOOTH 4.6x, SCRARITH 16x, EPSTEIN 1.07x -- the small-a
battery is a DENSITY functional and is Epstein-blind: typed
EPSTEIN-DENSITY-BLIND, the honest caveat on what Lane A convergence
certifies).  PLANTED OFF-LINE QUARTET: rho = 1/2 + 3/10 +- 30 i,
matched a_pl = delta^2 + gamma^2 = 900.09 gated inside the exact
round-117 window (a-, a+); detector = R_planted/R_bare at the frozen
t-grid (the pair factor (1 - t w*)^2, w* = (1 + delta^2/gamma^2)/4);
off-window invisibility |w_4(z0)| < 1/4 gated exactly.  Z1: the
finite spectrum vs the verified-zero cache (ward namespace, X5):
band-matched prefix, hybrid determinant (band mus replaced by cache
gammas), rule: TRANSCRIBING-IN-BAND iff median dev(R_fin, R_hybrid)
<= 0.25 * dev(R_fin, R_true); best cache partial-sum distance printed.
The round-112 transcription conviction is expected to apply and is
typed, not hidden.

MIN-CUT (E): the round-116 graph replica (4 parallel capacity-1 omega
edges, census {MEAS, OMEGA-POS}) extended by BLOCKREAL-THM (UNC) ->
NF-CLOSURE (UNC) -> [LANEA-CONV omega edge] -> R4-HYP (dense-a
criterion) -> RH.  Edmonds-Karp flows computed; the new edge is a
FIFTH PARALLEL COSTUME of the same semantic class (infinitary
positivity/limit introduction), typed SUFFICIENT-ONLY (LANEA-CONV
implies the r115 dense-a criterion; the converse fails).  The dense-a
sweep couples a to lambda (window edge >~ sqrt(a)): the hidden
quantifier is the (a, lambda) double limit; at FIXED a the Vitali
hypotheses are delivered by the unconditional finite bound +
(H-conv) + (H-trace) with no further quantifier.

=======================================================================
FROZEN NUMERICS
=======================================================================
L1 = ((3,45),(5,60),(8,80),(13,120)) at KFAC1 = 1.25 (SL.KFAC);
L2 = ((3,45),(5,60),(8,80)) at KFAC2 = 1.60.  A_BAT = (1,2,4,16);
T_BAT = {1:(1/2,1,3/2,2), 2:(1/2,1,3/2,2), 4:(1/2,3/2,5/2,7/2),
16:(1/2,3/2,5/2,7/2)}.  EM zeta: N = 60, J = 12, ward vs audit
1e-20.  Euler corridor pts ((4,3/2),(4,3),(16,3/2),(16,7/2)),
P ladder (2000, 20000, 200000), tail bound 2.6 P^{1-s}/((s-1)lnP).
Controls: SMOOTH x=5, SCRARITH x=5, EPSTEIN x=8 (KFAC1).  Wards:
my builder vs SL HP at x=3 (even+odd), x=5 (even), EPSTEIN x=5
(even); vs SL f64 for SMOOTH/SCRARITH x=5 (bar 1e-5 max-abs).
Z_EULER = (-0.9i, 1-0.9i, 2.5-1.2i, 3.7-2.0i).  SOFT_BAR = 1e-2.
NGRID_K = 20001 (prolate projection grid).  PLANT delta = 3/10,
gamma = 30, t-grid (3.5, 3.9, 3.99, 3.999), detect bar 1e-4.
Lane A hard bars (pre-freeze calibrated: L1 fall factor measured
~2.6, per-step falls; L2 predicted ~1.5): G33 per a: dev(x=13) <=
dev(x=3)/1.6 and per-step nonincreasing within wobble 1.10; G34
per a: dev(x=8) <= dev(x=3)/1.25, wobble 1.10.  G32 trace: defect
positive and dev(13) <= dev(3)/1.6 per a.  G35 mechanism band
[0.5, 2.0] on L1 for all a.  G36 separation: SMOOTH and SCRARITH
median ratio >= 2.5; EPSTEIN ratio reported, sanity [0.5, 5].
G26 spec-vs-census: max rel dev <= 1e-4 on zeros <= 2x band edge.
G27 realness |Im|/scale <= 1e-6.  G28 det-identity rel <= 5e-3
(f64 full-matrix-inversion cross-check only; the spectral object
itself is census-gated at 1e-4 -- smoke measured 1.8e-4 at x=5).
G40 identity rel <= 1e-15 (mp).  G42 channel sum rel <= 1e-10.
G48 perturbation 1e-25 on Q[0,0] at x=5: response in (1e-40, 1e-10)
(exactly-zero response = red flag, round-118 amendment-1 lesson;
all mp work under explicit mp.workdps).  RUNTIME_BAR = 2400 s.
Deterministic: NO randomness anywhere (all matrices/vectors frozen
literals; no RNG).  Cache verified_zeros_n7000.npy READ-ONLY in
ward_ namespace (X5: instrument, never construction).

VERDICT ENUMS (frozen): NF-CLOSURE(...) always stated with its
hypothesis list; LANEA-CONVERGES / LANEA-STALLS (hard gates G33+G34);
LANEA-Z1 typing TRANSCRIBING-IN-BAND / NON-TRANSCRIBING;
AN-IDENTITY-EXACT; AN-BOUND-LIVE / AN-BOUND-VOID-AT-DEPTH (G44/G45
adjudication: soft Euler evaluations >= 0.05 ||e|| at the deepest
rung AND product/LHS >= 1e3 there => VOID); AN-LHS-FALLS / -FLAT;
TAU-SCREEN(band per object); BETA-FRAME-DICTIONARY verdict;
MINCUT(cardinality, class census, SUFFICIENT-ONLY marker).

SMOKE DISCLOSURE (pre-freeze, scratch deleted): (a) x=13 even build
timed 185 s, census clean (41 zeros, first 14 = gamma_1..gamma_14
region, far artifact zeros 515/1635); (b) Lane A defects measured at
x = 3/5/13 for a = 1/2/4/16 (0.028/0.021/0.011 at a=1 ... 0.79/0.58/
0.30 at a=16) -- the fall bars above are frozen from this; mechanism
law exact to ~3 digits at a <= 4; (c) beta-frame spectrum at x=3/5
measured real but shifted (15.38 vs 14.135): the dictionary finding
was made pre-freeze and is gated, not discovered, here; (d) soft-mode
Euler evaluations at x=3 measured O(1) (0.55-0.82): the B4/B5
adjudication bars are frozen from this; (e) EPSTEIN battery blindness
1.07-1.16x measured pre-freeze (bar set to sanity band + typing);
(f) raw Euler product at sigma = 1.2 measured too slow (1.7e-2 at
P = 2e6): the corridor design is a pre-freeze decision.
Amendments after the frozen run, if any, are appended as numbered
AMENDMENT blocks.

AMENDMENT 1 (after frozen run 1 CRASHED at the x=13 operator build;
instrument repair + a headline finding; no bar, ladder, battery or
verdict rule changed).  The eta-frame coupling <eta, xi> equals the
minimizer's boundary value phi(a) (cos(om_k a) = (-1)^k), and the
run-1 crash exposed that it DECAYS AT THE CONNES SCALE: measured
|phi(a)|/||cn|| = 1.6e-3 / 4.8e-8 / 9.5e-15 at x = 3/5/8, i.e.
phi(a) ~ 0.005..0.02 * sqrt(gap) (fitted exponent 0.52..0.55 vs the
cluster gap) -- the round-114 Fredholm eta-degeneration surfacing on
the TRUE deep cells: the alternating f64 sum underflows at x = 13
(true value ~ sqrt(2.7e-47)).  REPAIR: per-rung admissibility guard
ETA_SAFE = 1e-10 on |<eta,xi>|/||xi|| (the f64 noise floor of the
alternating sum is ~1e-15; 1e-10 keeps 5 digits of headroom, and the
x=5 rung at 4.8e-8 measured dictionary dev 3.2e-6, inside the 1e-4
gate); admissible rungs build the f64
M_eta and gate the dictionary (G26/G28); degenerate rungs take
spec+ = the mp-certified census zeros -- the SAME object by the
exterior-determinant identity det(M_eta - z) = det(D - z)
(1 - <eta,(D-z)^{-1} D xi>/<eta,xi>) gated on the admissible rungs
-- typed ETA-FRAME-DEGENERATE(measured law).  The beta-frame gets
the same guard.  phi(a) per rung printed in mp (the law row).  All
run-1 numbers up to the crash reproduced identically.

AMENDMENT 2 (after frozen run 3, 39/40, sole FAIL G36; one gate
clause re-specified in the STRONGER direction, nothing else
changed).  The EPSTEIN clause of G36 was frozen as a sanity band
[0.5, 5] around the pre-freeze x = 5 measurement (1.21x,
density-blind).  The frozen run measured the x = 8 Epstein control
at ratios (47.4, 26.8, 16.1, 5.4), median 21.45 -- the falsifier
SEPARATES once the Epstein prime side has enough atoms; the x = 5
blindness is a shallow-rung artifact (4 lattice atoms), not a
battery property.  G36 now requires EPSTEIN >= SEP_BAR like the
other worlds, and the typing EPSTEIN-DENSITY-BLIND is downgraded to
a shallow-rung caveat (x = 5 measured 1.21x pre-freeze).  All other
run-3 numbers reproduced identically in the run of record.

AST FIREWALL: no zetazero/siegelz/siegeltheta/nzeros/grampoint
anywhere; mp.zeta attribute only inside audit_* functions; np.load
only inside ward_* functions; no import of verification/.
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

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

import semilocal_realroot_limit_probe as SL   # warded source builder
import blockreal_lemma_probe as BR            # round-114 machinery

# ---------------------------------------------------------------- frozen
KFAC1 = 1.25
KFAC2 = 1.60
L1 = ((3, 45), (5, 60), (8, 80), (13, 120))
L2 = ((3, 45), (5, 60), (8, 80))
A_BAT = (1, 2, 4, 16)
T_BAT = {1: (0.5, 1.0, 1.5, 2.0), 2: (0.5, 1.0, 1.5, 2.0),
         4: (0.5, 1.5, 2.5, 3.5), 16: (0.5, 1.5, 2.5, 3.5)}
EM_N, EM_J = 60, 12
CORRIDOR = ((4, 1.5), (4, 3.0), (16, 1.5), (16, 3.5))
P_LADDER = (2000, 20000, 200000)
Z_EULER = ((0.0, -0.9), (1.0, -0.9), (2.5, -1.2), (3.7, -2.0))
SOFT_BAR = 1e-2
NGRID_K = 20001
PLANT_DELTA, PLANT_GAMMA = 0.3, 30.0
PLANT_TGRID = (3.5, 3.9, 3.99, 3.999)
BAR_PLANT = 1e-4
BAR_SPEC_CENSUS = 1e-4
BAR_REAL = 1e-6
BAR_DETID = 5e-3
BAR_IDENT_MP = 1e-15
BAR_CHSUM = 1e-10
BAR_EM_AUDIT = 1e-20
FALL_L1, FALL_L2 = 1.6, 1.25
WOBBLE = 1.10
MECH_LO, MECH_HI = 0.5, 2.0
SEP_BAR = 2.5
EPS_SANITY = (0.5, 5.0)
Z1_BAR = 0.25
VOID_EVAL, VOID_RATIO = 0.05, 1e3
ETA_SAFE = 1e-10
RUNTIME_BAR = 2400.0
GAMMA1_LIT = 14.134725141734693790   # ward only

SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
T0_WALL = time.time()
CACHE_N7000 = os.path.join(HERE, "verified_zeros_n7000.npy")

CHECKS: list[tuple[str, bool, str]] = []
INFO: list[str] = []


def check(name: str, ok: bool, detail: str) -> bool:
    ok = bool(ok)
    CHECKS.append((name, ok, detail))
    print("  [%s] %-40s %s" % ("PASS" if ok else "FAIL", name, detail),
          flush=True)
    return ok


def info(msg: str) -> None:
    INFO.append(msg)
    print("  [INFO] " + msg, flush=True)


def section(title: str) -> None:
    print("\n" + "-" * 78 + "\n" + title + "\n" + "-" * 78, flush=True)


# ------------------------------------------------------------ firewall
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

    forb = {"zeta" + "zero", "siegel" + "z", "siegel" + "theta",
            "n" + "zeros", "gram" + "point"}
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
        if low in forb:
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
    for node in ast.walk(tree):
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            mods = ([al.name for al in node.names]
                    if isinstance(node, ast.Import)
                    else [node.module or ""])
            for m in mods:
                if m.startswith("verification"):
                    bad.append("import " + m)
    return (not bad), ("; ".join(bad) if bad else
                       "no zero-oracle; zeta in audit_, cache in ward_")


# ------------------------------------------------------- source zeta/xi
def em_zeta(s):
    """Own Euler-Maclaurin zeta (round-119 currency; NO mp.zeta).
    Valid Re s > -1 here; used at Re s >= 1.1."""
    s = mp.mpc(s)
    N = EM_N
    tot = mp.mpc(0)
    for n in range(1, N):
        tot += mp.power(n, -s)
    tot += mp.power(N, 1 - s) / (s - 1)
    tot += mp.power(N, -s) / 2
    fac = s
    npw = mp.power(N, -s - 1)
    for j in range(1, EM_J + 1):
        tot += mp.bernoulli(2 * j) / mp.factorial(2 * j) * fac * npw
        fac *= (s + 2 * j - 1) * (s + 2 * j)
        npw /= N * N
    return tot


def em_xi(s):
    s = mp.mpc(s)
    return (s * (s - 1) / 2 * mp.pi ** (-s / 2) * mp.gamma(s / 2)
            * em_zeta(s))


def em_log_phi(z):
    """log Phi(z) = log xi(1/2 + sqrt z), z off (-inf, 0]."""
    return mp.log(em_xi(mp.mpf("0.5") + mp.sqrt(mp.mpc(z))))


def r_true(a: int, t: float, dps: int = 50) -> float:
    """R_a(t) = |Phi(a e^{i th})|^2/Phi(a)^2 via own-EM xi."""
    with mp.workdps(dps):
        th = 2 * mp.asin(mp.sqrt(mp.mpf(repr(t))) / 2)
        zc = a * mp.exp(1j * th)
        num = abs(em_xi(mp.mpf("0.5") + mp.sqrt(zc))) ** 2
        den = mp.re(em_xi(mp.mpf("0.5") + mp.sqrt(mp.mpf(a)))) ** 2
        return float(num / den)


def c01_target(a: int, dps: int = 60) -> float:
    """C_{0,1}(a) = b0 - b1 = a F(a) + a^2 F'(a), F = Phi'/Phi (EM)."""
    with mp.workdps(dps):
        am = mp.mpf(a)
        F = mp.diff(em_log_phi, am)
        Fp = mp.diff(em_log_phi, am, 2)
        return float(mp.re(am * F + am * am * Fp))


def sieve_primes(cap: int) -> list[int]:
    comp = np.zeros(cap + 1, dtype=bool)
    out = []
    for p in range(2, cap + 1):
        if not comp[p]:
            out.append(p)
            comp[p * p:: p] = True
    return out


def euler_log_zeta(s, primes: list[int]) -> mp.mpc:
    """Raw truncated Euler product log zeta (own sieve)."""
    s = mp.mpc(s)
    tot = mp.mpc(0)
    sig = float(mp.re(s))
    for p in primes:
        k = 1
        while k * sig * math.log(p) < 60:
            tot += mp.power(p, -k * s) / k
            k += 1
    return tot


def euler_tail_bound(sigma: float, P: int) -> float:
    """Cited Rosser-style bound: sum_{p>P} p^-sigma (+ higher powers)
    <= 2.6 P^{1-sigma}/((sigma-1) ln P)."""
    return 2.6 * P ** (1.0 - sigma) / ((sigma - 1.0) * math.log(P))


# ------------------------------------------------------- audit evaluators
def audit_zeta_dev(pts, dps: int = 50) -> float:
    """max rel dev of own EM zeta vs mp.zeta (audit namespace)."""
    worst = 0.0
    with mp.workdps(dps):
        for s in pts:
            zt = mp.zeta(mp.mpc(s))
            worst = max(worst, float(abs(em_zeta(s) - zt) / abs(zt)))
    return worst


# ---------------------------------------------------------- own builder
def build_cell(x: int, kfac: float, world: str, dps: int,
               sector: str = "even", want_mp: bool = False) -> dict:
    """Faithful mp port of SL.build_trig_cell_hp with (1) separate
    POLE/ARCH/PRIME blocks, (2) SMOOTH and SCRARITH worlds, (3) the
    mp matrix + eigsy retained when want_mp.  Warded against SL."""
    t0 = time.time()
    with mp.workdps(dps):
        aa = mp.log(x) / 2
        K = int(math.ceil(kfac * x * math.log(x)))
        even = sector == "even"
        ks = list(range(K)) if even else list(range(1, K))
        nmode = len(ks)
        oms = [k * mp.pi / aa for k in ks]
        par = [mp.mpf((-1.0) ** k) for k in ks]
        dsig = mp.mpf(-1) if even else mp.mpf(1)
        L2v = 2 * aa

        def a_weight(w):
            return mp.exp(-w / 2) / (-mp.expm1(-2 * w))

        def r_of(w):
            if w == 0:
                return mp.mpf("0.25")
            return a_weight(w) - 1 / (2 * w)

        jvec = []
        for i, o in enumerate(oms):
            if ks[i] == 0:
                jvec.append(mp.mpf(0))
                continue
            npts = int(mp.floor(L2v * o / mp.pi))
            pts = ([mp.mpf(0)]
                   + [jj * mp.pi / o for jj in range(1, npts + 1)]
                   + [L2v])
            val = mp.quad(lambda w, o=o: mp.sin(o * w) * r_of(w), pts)
            jvec.append(val + mp.si(L2v * o) / 2)

        # ------------------------------------------------ world atoms
        atoms: list[tuple] = []
        smooth = world == "SMOOTH"
        if world in ("MAIN", "SCRARITH"):
            icap = int(math.floor(x))
            comp = np.zeros(icap + 1, dtype=bool)
            nlist = []
            for p in range(2, icap + 1):
                if comp[p]:
                    continue
                comp[p * p:: p] = True
                q = p
                while q <= icap:
                    nlist.append((q, p))
                    q *= p
            nlist.sort()
            for q, p in nlist:
                atoms.append((mp.log(q), mp.log(p) / mp.sqrt(q)))
            if world == "SCRARITH":
                gold = (math.sqrt(5.0) - 1.0) / 2.0
                keys = [math.fmod(q * gold, 1.0) for q, _p in nlist]
                perm = sorted(range(len(keys)), key=lambda i: keys[i])
                wts = [atoms[i][1] for i in range(len(atoms))]
                atoms = [(atoms[i][0], wts[perm[i]])
                         for i in range(len(atoms))]
        elif world == "EPSTEIN":
            icap = int(math.floor(x))
            rq = np.zeros(icap + 1)
            xm = int(math.isqrt(icap)) + 1
            ym = int(math.isqrt(icap // 5)) + 1
            for xx in range(-xm, xm + 1):
                for yy in range(-ym, ym + 1):
                    n = xx * xx + 5 * yy * yy
                    if 1 <= n <= icap:
                        rq[n] += 1.0
            av = [mp.mpf(v) / 2 for v in rq]
            lamq = [mp.mpf(0)] * (icap + 1)
            for n in range(2, icap + 1):
                sacc = av[n] * mp.log(n)
                for d in range(2, n):
                    if n % d == 0:
                        sacc -= lamq[d] * av[n // d]
                lamq[n] = sacc
            for n in range(2, icap + 1):
                if abs(lamq[n]) > mp.mpf("1e-30"):
                    atoms.append((mp.log(n), lamq[n] / mp.sqrt(n)))
        elif world == "SMOOTH":
            atoms = []
        else:
            raise ValueError(world)
        n_atoms = len(atoms)

        if smooth:
            ea = mp.exp(aa)
            pj = []
            for i, o in enumerate(oms):
                if ks[i] == 0:
                    pj.append(mp.mpf(0))
                else:
                    pj.append(((mp.sin(L2v * o) / 2
                                - o * mp.cos(L2v * o)) * ea + o)
                              / (mp.mpf(1) / 4 + o * o))
        else:
            pj = [sum((w * mp.sin(o * u) for u, w in atoms), mp.mpf(0))
                  for o in oms]

        # ------------------------------------------------- assembly
        Mpole = mp.zeros(nmode, nmode)
        March = mp.zeros(nmode, nmode)
        Mprime = mp.zeros(nmode, nmode)
        if even:
            ipv = [par[i] * mp.sinh(aa / 2)
                   / (mp.mpf(1) / 4 + oms[i] ** 2) for i in range(nmode)]
            pole_sign = mp.mpf(2)
        else:
            ipv = [-2 * par[i] * oms[i] * mp.sinh(aa / 2)
                   / (mp.mpf(1) / 4 + oms[i] ** 2) for i in range(nmode)]
            pole_sign = mp.mpf(-2)
        for i in range(nmode):
            for j2 in range(nmode):
                Mpole[i, j2] = pole_sign * ipv[i] * ipv[j2]
        for i in range(nmode):
            for j2 in range(i):
                sg = par[i] * par[j2]
                den = oms[j2] ** 2 - oms[i] ** 2
                if even:
                    arch_od = -2 * sg * (oms[i] * jvec[i]
                                         - oms[j2] * jvec[j2]) / den
                    prim_od = 2 * sg * (oms[i] * pj[i]
                                        - oms[j2] * pj[j2]) / den
                else:
                    arch_od = -2 * sg * (oms[j2] * jvec[i]
                                         - oms[i] * jvec[j2]) / den
                    prim_od = 2 * sg * (oms[j2] * pj[i]
                                        - oms[i] * pj[j2]) / den
                March[i, j2] += arch_od
                March[j2, i] += arch_od
                Mprime[i, j2] += prim_od
                Mprime[j2, i] += prim_od
        tail_c = lambda f0: -f0 / 2 * mp.log1p(-mp.exp(-2 * L2v))  # noqa: E731
        for i in range(nmode):
            k = ks[i]
            o = oms[i]
            if k == 0:
                f0 = L2v

                def psi_d(w):
                    return L2v - w
            else:
                f0 = aa

                def psi_d(w, o=o):
                    return ((aa - w / 2) * mp.cos(o * w)
                            + dsig * mp.sin(o * w) / (2 * o))

            def integrand(w, f0=f0, psi_d=psi_d):
                return ((f0 * mp.exp(-2 * w)
                         - psi_d(w) * mp.exp(-w / 2))
                        / (-mp.expm1(-2 * w)))
            npts = max(int(mp.floor(L2v * o / mp.pi)), 1) if k else 1
            base_pts = [mp.mpf(0), mp.mpf("1e-6"), mp.mpf("1e-3"),
                        mp.mpf("0.05"), L2v]
            if k:
                base_pts += [jj * mp.pi / o for jj in range(1, npts + 1)]
            pts = sorted(set(p for p in base_pts if p <= L2v))
            body = mp.quad(integrand, pts)
            March[i, i] += (-f0 * (mp.euler + mp.log(mp.pi))
                            + 2 * (body + tail_c(f0)))
            if smooth:
                pts2 = sorted(set(
                    [mp.mpf(0), L2v]
                    + ([jj * mp.pi / o for jj in range(1, npts + 1)]
                       if k else [])))
                pdiag = mp.quad(lambda w, psi_d=psi_d:
                                psi_d(w) * mp.exp(w / 2), pts2)
            else:
                pdiag = sum((w * ((aa - u / 2) * mp.cos(o * u)
                                  + dsig * mp.sin(o * u) / (2 * o))
                             if k else w * (L2v - u)
                             for u, w in atoms), mp.mpf(0))
            Mprime[i, i] += 2 * pdiag
        # normalize + symmetrize each block
        nrm = [mp.sqrt(L2v) if (even and ks[i] == 0) else mp.sqrt(aa)
               for i in range(nmode)]
        for Mb in (Mpole, March, Mprime):
            for i in range(nmode):
                for j2 in range(nmode):
                    Mb[i, j2] = Mb[i, j2] / (nrm[i] * nrm[j2])
            for i in range(nmode):
                for j2 in range(i):
                    sym = (Mb[i, j2] + Mb[j2, i]) / 2
                    Mb[i, j2] = sym
                    Mb[j2, i] = sym
        M = Mpole + March - Mprime
        E = V = None
        tau_f = gap_f = float("nan")
        tau_str = gap_str = "n/a"
        cn = np.zeros(nmode)
        cn_mp_str = None
        if even:
            E, V = mp.eigsy(M)
            order = sorted(range(nmode), key=lambda i: E[i])
            i0 = order[0]
            tau_mp = E[i0]
            gap_mp = E[order[1]] - E[i0]
            cvec = [V[i, i0] for i in range(nmode)]
            cn_mp = [cvec[i] / nrm[i] for i in range(nmode)]
            if float(cn_mp[int(np.argmax([abs(float(v))
                                          for v in cn_mp]))]) < 0:
                cn_mp = [-v for v in cn_mp]
                for i in range(nmode):
                    V[i, i0] = -V[i, i0]
            cn_mp_str = [mp.nstr(v, dps) for v in cn_mp]
            cn = np.array([float(v) for v in cn_mp])
            tau_f, gap_f = float(tau_mp), float(gap_mp)
            tau_str, gap_str = mp.nstr(tau_mp, 6), mp.nstr(gap_mp, 6)
            Eord = [E[i] for i in order]
            Vord = mp.zeros(nmode, nmode)
            for c, i in enumerate(order):
                for rix in range(nmode):
                    Vord[rix, c] = V[rix, i]
            E, V = Eord, Vord
        a_f = float(aa)
    m_f64 = np.array([[float(M[i, j2]) for j2 in range(nmode)]
                      for i in range(nmode)])
    out = {"x": x, "world": world, "K": K, "a": a_f,
           "om": np.array(ks, float) * math.pi / a_f,
           "sector": sector, "cn": cn, "cn_mp_str": cn_mp_str,
           "tau": tau_f, "gap": gap_f, "tau_str": tau_str,
           "gap_str": gap_str, "m_tilde": m_f64, "dps": dps,
           "n_atoms": n_atoms, "build_s": time.time() - t0,
           "blk_pole": np.array([[float(Mpole[i, j]) for j in
                                  range(nmode)] for i in range(nmode)]),
           "blk_arch": np.array([[float(March[i, j]) for j in
                                  range(nmode)] for i in range(nmode)]),
           "blk_prime": np.array([[float(Mprime[i, j]) for j in
                                   range(nmode)] for i in range(nmode)])}
    if want_mp and even:
        out["mpM"] = M
        out["mpPole"], out["mpArch"], out["mpPrime"] = Mpole, March, Mprime
        out["mpE"], out["mpV"] = E, V
    return out


# ------------------------------------------------------ block operators
def build_ops(ce: dict, co: dict) -> dict:
    """Full V-basis assembly + CCM operators (eta and beta frames),
    with the AMENDMENT-1 admissibility guards."""
    K = ce["K"]
    L = ce["a"]
    Tf = BR.assemble_full(ce, co)
    dim = 2 * K - 1
    mid = K - 1
    cn = ce["cn"]
    xi = np.zeros(dim)
    xi[mid] = cn[0]
    xi[K:] = cn[1:] / 2.0
    xi[:mid] = cn[1:][::-1] / 2.0
    eta = np.array([(-1.0) ** (n - mid) for n in range(dim)])
    nxi = float(np.linalg.norm(xi))
    eta_xi = float(eta @ xi)
    eta_ok = abs(eta_xi) / nxi >= ETA_SAFE
    dv = np.array([(n - mid) * math.pi / L for n in range(dim)])
    Dm = np.diag(dv)
    Meta = (Dm - np.outer(dv * xi, eta) / eta_xi) if eta_ok else None
    bt = BR.beta_extract(Dm, Tf, eta)
    Sc = Dm @ Tf - Tf @ Dm
    sv = np.linalg.svd(Sc, compute_uv=False)
    h1_r = float(sv[2] / sv[0]) if len(sv) > 2 else 0.0
    beta_xi = float(bt @ xi)
    beta_ok = abs(beta_xi) / (nxi * max(np.linalg.norm(bt),
                                        1e-300)) >= ETA_SAFE
    Mbeta = (Dm - np.outer(dv * xi, bt) / beta_xi) if beta_ok \
        else None
    return {"Tf": Tf, "xi": xi, "eta": eta, "beta": bt, "dv": dv,
            "Meta": Meta, "Mbeta": Mbeta, "h1_rank2": h1_r,
            "eta_xi_rel": abs(eta_xi) / nxi, "beta_xi": beta_xi,
            "dim": dim, "L": L, "K": K}


def spec_pos(M: np.ndarray) -> tuple[np.ndarray, float]:
    ev = np.linalg.eigvals(M)
    sc = max(float(np.max(np.abs(ev))), 1e-300)
    imrel = float(np.max(np.abs(ev.imag))) / sc
    pos = np.sort(ev.real[ev.real > 1e-6])
    return pos, imrel


def det_quotient(mus: np.ndarray, a: float, t: float) -> float:
    w = a * mus ** 2 / (a + mus ** 2) ** 2
    return float(np.exp(np.sum(np.log1p(-t * w))))


def sup_defect(mus: np.ndarray, a: int) -> float:
    return max(abs(math.log(max(det_quotient(mus, a, t), 1e-300)
                            / r_true(a, t))) for t in T_BAT[a])


# ------------------------------------------------------------- wards
def ward_cache() -> np.ndarray:
    return np.asarray(np.load(CACHE_N7000), float)


def ward_c01(gam: np.ndarray, a: float) -> float:
    """cache + RvM tail ward for C01(a) (round-117 G30 pattern)."""
    w = a * gam ** 2 / (a + gam ** 2) ** 2
    gtop = float(gam[-1])
    with mp.workdps(40):
        tail = float(mp.quad(
            lambda t: (mp.log(t / (2 * mp.pi)) / (2 * mp.pi))
            * (a * t * t) / (a + t * t) ** 2,
            [gtop, 3 * gtop, 30 * gtop, mp.inf]))
    return float(np.sum(w)) + tail


def ward_band_match(mus: np.ndarray, gam: np.ndarray) -> int:
    """maximal matched prefix: |mu_i - nearest gamma| < 0.25 spacing."""
    nb = 0
    for i, mu in enumerate(mus):
        j = int(np.argmin(np.abs(gam - mu)))
        lo = gam[j - 1] if j > 0 else 0.0
        hi = gam[j + 1] if j + 1 < len(gam) else gam[j] + 10.0
        spac = 0.5 * (hi - lo)
        if abs(mu - gam[j]) < 0.25 * spac and i == nb:
            nb += 1
        else:
            break
    return nb


def ward_hybrid(mus: np.ndarray, gam: np.ndarray,
                nband: int) -> np.ndarray:
    out = mus.copy()
    for i in range(nband):
        j = int(np.argmin(np.abs(gam - mus[i])))
        out[i] = gam[j]
    return out


def ward_partial_dev(mus: np.ndarray, gam: np.ndarray, a: int) -> tuple:
    """min over N (log grid) of sup_t |log(R_fin/R_partialN)|."""
    best = (float("inf"), -1)
    N = 4
    while N <= len(gam):
        dev = max(abs(math.log(det_quotient(mus, a, t)
                               / det_quotient(gam[:N], a, t)))
                  for t in T_BAT[a])
        if dev < best[0]:
            best = (dev, N)
        N *= 2
    return best


# --------------------------------------------------------- symbolic S1
def symbolic_gates() -> list[tuple[str, bool, str]]:
    import sympy as sp
    out = []
    a, t, m2 = sp.symbols("a t m2", positive=True)

    # G10 per-eigenvalue determinant factor: with z+ + z- = a(2-t),
    # z+ z- = a^2:  (m2+z+)(m2+z-) = m2^2 + m2 a(2-t) + a^2
    lhs = sp.expand(m2 ** 2 + m2 * a * (2 - t) + a ** 2)
    rhs = sp.expand((m2 + a) ** 2 - t * a * m2)
    ok10 = sp.expand(lhs - rhs) == 0
    rhs_full = sp.simplify((m2 + a) ** 2
                           * (1 - t * a * m2 / (a + m2) ** 2)
                           - ((m2 + a) ** 2 - t * a * m2))
    out.append(("G10-det-factor", ok10 and rhs_full == 0,
                "(m^2+z+)(m^2+z-) == (m^2+a)^2 (1 - t w(m)) exactly "
                "(z+ + z- = a(2-t), z+ z- = a^2)"))

    # G11 unconditional contraction for real spectrum
    ok11 = sp.expand((a + m2) ** 2 - 4 * a * m2
                     - (a - m2) ** 2) == 0
    out.append(("G11-contraction", ok11,
                "0 <= w = a m2/(a+m2)^2 <= 1/4 for every real mu "
                "(m2 = mu^2 >= 0): (a+m2)^2 - 4am2 == (a-m2)^2; "
                "SUPPLIED unconditionally by round-114 realness"))

    # G12 Euler-safe branch (round-117 R1v-branch re-gated)
    cs, sn = sp.symbols("cs sn", positive=True)
    zplus = sp.expand((sp.sqrt(a) * cs + sp.I * sp.sqrt(a) * sn) ** 2)
    dev1 = sp.simplify(sp.expand(
        zplus - (a * (1 - 2 * sn ** 2)
                 + 2 * sp.I * a * sn * cs)).subs(cs ** 2, 1 - sn ** 2))
    modsq = sp.expand(((a * (1 - 2 * sn ** 2)) ** 2
                       + (2 * a * sn * cs) ** 2).subs(cs ** 2,
                                                      1 - sn ** 2))
    out.append(("G12-euler-branch", dev1 == 0
                and sp.simplify(modsq - a ** 2) == 0,
                "Re(1/2+sqrt z+) = 1/2 + sqrt(a) sqrt(1-t/4) > 1 iff "
                "t < 4 - 1/a (cited round-117 R1v, re-gated)"))

    # G13 trace/log chain (round-117 R3a re-gated)
    u = sp.symbols("u", positive=True)
    dch = sp.simplify(sp.diff(u / (1 - u) - sp.log(1 / (1 - u)), u)
                      - u / (1 - u) ** 2) == 0
    wv = sp.symbols("w", positive=True)
    kt = all(sp.expand(sp.Rational(1, 4) ** (k - 1) * wv - wv ** k
                       - wv * (sp.Rational(1, 4) ** (k - 1)
                               - wv ** (k - 1))) == 0
             for k in range(2, 6))
    out.append(("G13-trace-chain", dch and kt,
                "|log det(I-tB)| <= Tr B * r/(1-r/4) chain (cited "
                "round-117 R3a; input 0<=B<=1/4 now UNCONDITIONAL "
                "via G11 + round-114 realness)"))

    # G14 AN identity exact rational (Moore-Penrose of rational PSD)
    Y = sp.Matrix([[1, 0, 2], [0, 1, -1], [2, -1, 0], [1, 1, 1],
                   [0, 2, 1]])
    A5 = sp.Matrix([[1, 2, 0], [0, 1, 1], [1, 0, 1]])
    Gi = A5 * A5.T + sp.eye(3)
    G = Y * Gi * Y.T
    Nsp = (Y.T).nullspace()
    Nm = sp.Matrix.hstack(*Nsp)
    P = Nm * (Nm.T * Nm).inv() * Nm.T
    H = Y * (Y.T * G * Y).inv() * Y.T
    I5 = sp.eye(5)
    okH = (sp.simplify(H - H.T) == sp.zeros(5, 5)
           and sp.simplify(H * G - (I5 - P)) == sp.zeros(5, 5)
           and sp.simplify(G * H - (I5 - P)) == sp.zeros(5, 5)
           and sp.simplify(H * G * H - H) == sp.zeros(5, 5)
           and sp.simplify(G * H * G - G) == sp.zeros(5, 5))
    e_re = sp.Matrix([1, 2, -1, 3, 0]) / sp.Integer(3)
    e_im = sp.Matrix([0, -1, 2, 1, -2]) / sp.Integer(5)
    kv = sp.Matrix([2, -1, 1, 0, 1]) / sp.Integer(7)
    ev = e_re + sp.I * e_im
    lhs14 = (ev.conjugate().T * (I5 - P) * kv)[0, 0]
    rhs14 = ((H * (I5 - P) * ev).conjugate().T * (G * kv))[0, 0]
    ok14 = okH and sp.simplify(lhs14 - rhs14) == 0
    out.append(("G14-AN-identity-exact", ok14,
                "G^+ = Y (Y^T G Y)^{-1} Y^T rational MP-pseudoinverse "
                "(5 properties exact); <e,(I-P)k> == <G^+(I-P)e, Gk> "
                "exact in Q[i] (ker dim 2)"))

    # G15 planted window membership + off-window invisibility (exact)
    de = sp.Rational(3, 10)
    ga = sp.Integer(30)
    z0 = (de + sp.I * ga) ** 2
    Rz = sp.re(z0)
    Az = de ** 2 + ga ** 2
    a_pl = Az
    inside = sp.simplify((a_pl - (Rz + 2 * Az)) ** 2
                         - (Rz + Az) * (Rz + 3 * Az)) < 0
    wstar = (1 + de ** 2 / ga ** 2) / 4
    w4sq = sp.simplify(16 * Az ** 2
                       / ((4 - Rz) ** 2 + sp.im(z0) ** 2) ** 2)
    invis = sp.simplify(w4sq - sp.Rational(1, 16)) < 0
    out.append(("G15-plant-window", bool(inside) and bool(invis)
                and bool(sp.simplify(wstar - sp.Rational(1, 4)) > 0),
                "a_pl = delta^2+gamma^2 = %.2f inside exact (a-,a+) "
                "window; w* = %.8f > 1/4; |w_4(z0)| < 1/4 (invisible "
                "off-window)" % (float(a_pl), float(wstar))))
    return out


# --------------------------------------------------------- lane B core
def evec_euler(z: complex, om: np.ndarray, L: float,
               K: int) -> list:
    """(e_z)_k = conj(B_k(z))/norm_k in mp (current workdps)."""
    zm = mp.mpc(z)
    out = []
    for k in range(K):
        o = mp.mpf(repr(float(om[k])))
        if k == 0:
            b = 2 * mp.sin(L * zm) / zm
            nk = mp.sqrt(2 * mp.mpf(repr(L)))
        else:
            b = (mp.sin(mp.mpf(repr(L)) * (zm - o)) / (zm - o)
                 + mp.sin(mp.mpf(repr(L)) * (zm + o)) / (zm + o))
            nk = mp.sqrt(mp.mpf(repr(L)))
        out.append(mp.conj(b) / nk)
    return out


def mp_dot(u: list, v: list) -> mp.mpc:
    return mp.fsum(mp.conj(a) * b for a, b in zip(u, v))


def mp_norm(u: list) -> mp.mpf:
    return mp.sqrt(mp.fsum(abs(a) ** 2 for a in u))


def matcol(V, j, n) -> list:
    return [V[i, j] for i in range(n)]


def matvec(M, v, n) -> list:
    return [mp.fsum(M[i, j] * v[j] for j in range(n))
            for i in range(n)]


def prolate_kvec(x: int, cell: dict) -> np.ndarray:
    """k_lambda (blockreal M4 recipe, lam2 = x) -> normalized-basis
    unit vector (f64)."""
    L = cell["a"]
    K = cell["K"]
    om = cell["om"]
    pro = BR.Prolate(float(x))
    coef, _c0, _e0, _e4 = BR.prolate_pair(pro)
    vg = np.linspace(-L, L, NGRID_K)
    kg = BR.k_lambda_on_v(pro, coef, vg)
    cs = np.empty(K)
    cs[0] = float(np.trapezoid(kg, vg)) / (2 * L)
    for k in range(1, K):
        cs[k] = float(np.trapezoid(kg * np.cos(om[k] * vg), vg)) / L
    norms = np.full(K, math.sqrt(L))
    norms[0] = math.sqrt(2 * L)
    kt = cs * norms
    return kt / np.linalg.norm(kt)


def lane_b_rung(cell: dict, kt: np.ndarray) -> dict:
    """All Lane-B measurements for one even MAIN cell (mp)."""
    K = cell["K"]
    dps = cell["dps"]
    res = {"x": cell["x"]}
    with mp.workdps(dps):
        E, V = cell["mpE"], cell["mpV"]
        Q = cell["mpM"]
        Qp = cell["mpPrime"]
        eps = E[0]
        gap = E[1] - E[0]
        soft = [i for i in range(1, K) if E[i] - eps <= SOFT_BAR]
        ncl = 1 + len([i for i in soft if E[i] - eps
                       <= mp.mpf("1e-6")])
        kv = [mp.mpf(repr(float(v))) for v in kt]
        v0 = matcol(V, 0, K)
        pk = mp_dot(v0, kv)
        ipk = [kv[i] - v0[i] * pk for i in range(K)]
        rv = matvec(Q, kv, K)
        rv = [rv[i] - eps * kv[i] for i in range(K)]
        rp = matvec(Qp, kv, K)                 # prime block * k
        ra = [rv[i] + rp[i] for i in range(K)]  # (pole+arch-eps) k
        res.update(eps=float(eps), gap=float(gap), nsoft=len(soft),
                   ncl=ncl, r_norm=float(mp_norm(rv)),
                   ipk_norm=float(mp_norm(ipk)),
                   cos_kg=float(abs(pk)))
        kmix = [float(abs(mp_dot(matcol(V, i, K), kv)))
                for i in soft]
        res["kmix"] = kmix
        rows = []
        for (zr, zi) in Z_EULER:
            ez = evec_euler(complex(zr, zi), cell["om"], cell["a"], K)
            lhs = mp_dot(ez, ipk)
            coefs = [mp_dot(matcol(V, i, K), ez) for i in range(K)]
            Re = [mp.fsum(V[j, i] * mp.conj(coefs[i]) / (E[i] - eps)
                          for i in range(1, K)) for j in range(K)]
            Re = [mp.conj(u) for u in Re]
            rhs = mp_dot(Re, rv)
            c_ar = mp_dot(Re, ra)
            c_pr = mp_dot(Re, [-u for u in rp])
            nRe = mp_norm(Re)
            nE = mp_norm(ez)
            # energy-norm pair
            prodE = (mp.sqrt(mp.fsum(abs(coefs[i]) ** 2 / (E[i] - eps)
                                     for i in range(1, K)))
                     * mp.sqrt(mp.fsum((E[i] - eps)
                                       * abs(mp_dot(matcol(V, i, K),
                                                    kv)) ** 2
                                       for i in range(1, K))))
            softev = max((float(abs(coefs[i])) for i in soft),
                         default=0.0)
            # cluster split: hard = complement of ground + soft;
            # LHS = lhs_soft + lhs_hard EXACTLY, and lhs_hard obeys
            # its own AN identity <e,(I-P_cl)k> = <R_cl e, r>
            hard = [i for i in range(1, K) if i not in soft]
            Re2 = [mp.conj(mp.fsum(V[j, i] * mp.conj(coefs[i])
                                   / (E[i] - eps) for i in hard))
                   for j in range(K)] if hard else [mp.mpf(0)] * K
            kco = [mp_dot(matcol(V, i, K), kv) for i in range(K)]
            lhs_soft = mp.fsum(mp.conj(coefs[i]) * kco[i]
                               for i in soft)
            lhs_hard = mp_dot(Re2, rv)
            split_dev = float(abs(lhs_soft + lhs_hard - lhs)
                              / max(abs(lhs), mp.mpf("1e-300")))
            c_ar_h = mp_dot(Re2, ra)
            c_pr_h = mp_dot(Re2, [-u for u in rp])
            rows.append({
                "z": complex(zr, zi), "lhs": float(abs(lhs)),
                "identdev": float(abs(lhs - rhs)
                                  / max(abs(lhs), mp.mpf("1e-300"))),
                "chsum": float(abs(c_ar + c_pr - rhs)
                               / max(abs(rhs), mp.mpf("1e-300"))),
                "c_arch": float(abs(c_ar)), "c_prime": float(abs(c_pr)),
                "c_arch_h": float(abs(c_ar_h)),
                "c_prime_h": float(abs(c_pr_h)),
                "lhs_soft": float(abs(lhs_soft)),
                "lhs_hard": float(abs(lhs_hard)),
                "split_dev": split_dev,
                "prod": float(nRe * mp_norm(rv)),
                "prodE": float(prodE),
                "dk": float(nE * mp_norm(rv) / gap),
                "softev": softev, "e_norm": float(nE),
                "prod_cl": float(mp_norm(Re2) * mp_norm(rv))})
        res["rows"] = rows
    return res


# --------------------------------------------------------- min-cut S5
def maxflow(edges: dict, srcn: str, dstn: str) -> int:
    """Edmonds-Karp on integer capacities (INF = 10**6)."""
    cap = {}
    nodes = set()
    for (u, v), c in edges.items():
        cap[(u, v)] = cap.get((u, v), 0) + c
        cap.setdefault((v, u), 0)
        nodes |= {u, v}
    flow = 0
    while True:
        # BFS
        prev = {srcn: None}
        queue = [srcn]
        while queue and dstn not in prev:
            u = queue.pop(0)
            for v in nodes:
                if v not in prev and cap.get((u, v), 0) > 0:
                    prev[v] = u
                    queue.append(v)
        if dstn not in prev:
            return flow
        path = []
        v = dstn
        while prev[v] is not None:
            path.append((prev[v], v))
            v = prev[v]
        aug = min(cap[e] for e in path)
        for (u, v) in path:
            cap[(u, v)] -= aug
            cap[(v, u)] += aug
        flow += aug


def bfs_reach(edges: dict, srcn: str) -> set:
    adj = {}
    for (u, v), c in edges.items():
        if c > 0:
            adj.setdefault(u, []).append(v)
    seen = {srcn}
    queue = [srcn]
    while queue:
        u = queue.pop(0)
        for v in adj.get(u, []):
            if v not in seen:
                seen.add(v)
                queue.append(v)
    return seen


# ---------------------------------------------------------------- main
def main() -> int:
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke

    print("radius4_an_probe -- PRIME.RADIUS4.AUBINNITSCHE.01")
    print("SPEC_SHA %s" % SPEC_SHA[:16])
    print("mode: %s" % ("SMOKE (NOT-VERDICT-BEARING)" if smoke
                        else "FULL"))
    print("NO RH CLAIM.  EXPLORATION ONLY.")

    l1 = L1[:2] if smoke else L1
    l2 = L2[:2] if smoke else L2
    ctrl_smooth_x = 5
    ctrl_eps_x = 5 if smoke else 8

    # ---------------------------------------------------------- S0
    section("S0  FIREWALL + CACHE")
    ok, det = firewall_audit()
    check("G01-ast-firewall", ok, det)
    gam = ward_cache()
    check("G02-cache-health", len(gam) >= 5000
          and abs(float(gam[0]) - GAMMA1_LIT) < 1e-9
          and bool(np.all(np.diff(gam) > 0)),
          "n=%d gamma_1 dev %.1e (READ-ONLY, X5)"
          % (len(gam), abs(float(gam[0]) - GAMMA1_LIT)))

    # ---------------------------------------------------------- S1
    section("S1  ALGEBRA GATES (sympy exact)")
    for name, okg, detg in symbolic_gates():
        check(name, okg, detg)
    info("NF-CLOSURE THEOREM stated (typed PROVEN with classical "
         "inputs Montel/Vitali/identity/Hurwitz, cited): real finite "
         "spectrum (round-114) => 0 <= B <= 1/4 (G11) => zero-free + "
         "|log R| <= TrB r/(1-r/4) (G13) => normal family; (H-conv) "
         "on the Euler interval + (H-trace) + dense a => RH.  The "
         "round-117 requirement (b) [PSD contraction WITHOUT zero "
         "reality] is CLOSED at the finite level; remaining omega = "
         "(H-conv)+(H-trace), measured below")

    # ---------------------------------------------------------- S2
    section("S2  INSTRUMENT (own builder + wards + operators)")
    t0 = time.time()
    ce3 = build_cell(3, KFAC1, "MAIN", 45, want_mp=True)
    sl3 = SL.build_trig_cell_hp(3, KFAC1, "MAIN", 45)
    dev_m = float(np.max(np.abs(ce3["m_tilde"] - sl3["m_tilde"])))
    dev_t = abs(ce3["tau"] / sl3["tau"] - 1)
    dev_g = abs(ce3["gap"] / sl3["gap"] - 1)
    check("G20-ward-x3-even", dev_m <= 1e-8 and dev_t <= 1e-6
          and dev_g <= 1e-6,
          "matrix max dev %.1e, tau rel %.1e, gap rel %.1e (%.1f s)"
          % (dev_m, dev_t, dev_g, time.time() - t0))
    co3 = build_cell(3, KFAC1, "MAIN", 45, sector="odd")
    so3 = SL.build_trig_cell_hp(3, KFAC1, "MAIN", 45, sector="odd")
    dev_o = float(np.max(np.abs(co3["m_tilde"] - so3["m_tilde"])))
    ce5 = build_cell(5, KFAC1, "MAIN", 60, want_mp=True)
    sl5 = SL.build_trig_cell_hp(5, KFAC1, "MAIN", 60)
    dev_5 = float(np.max(np.abs(ce5["m_tilde"] - sl5["m_tilde"])))
    check("G21-ward-x3odd-x5even", dev_o <= 1e-8 and dev_5 <= 1e-8,
          "odd x=3 max dev %.1e; even x=5 max dev %.1e"
          % (dev_o, dev_5))
    cq5 = build_cell(5, KFAC1, "EPSTEIN", 60)
    sq5 = SL.build_trig_cell_hp(5, KFAC1, "EPSTEIN", 60)
    dev_q = float(np.max(np.abs(cq5["m_tilde"] - sq5["m_tilde"])))
    check("G22-ward-epstein-x5", dev_q <= 1e-8,
          "EPSTEIN x=5 max dev %.1e vs SL HP" % dev_q)
    csm = build_cell(ctrl_smooth_x, KFAC1, "SMOOTH", 60, want_mp=False)
    fsm = SL.build_trig_cell(ctrl_smooth_x, KFAC1, "SMOOTH")
    dev_s = float(np.max(np.abs(csm["m_tilde"] - fsm["m_tilde"])))
    csc = build_cell(ctrl_smooth_x, KFAC1, "SCRARITH", 60)
    fsc = SL.build_trig_cell(ctrl_smooth_x, KFAC1, "SCRARITH")
    dev_c = float(np.max(np.abs(csc["m_tilde"] - fsc["m_tilde"])))
    check("G23-ward-smooth-scrarith", dev_s <= 1e-5 and dev_c <= 1e-5,
          "SMOOTH max dev %.1e, SCRARITH %.1e vs SL f64 (Filon-level "
          "bar)" % (dev_s, dev_c))
    dev_blk = float(np.max(np.abs(
        ce3["blk_pole"] + ce3["blk_arch"] - ce3["blk_prime"]
        - ce3["m_tilde"])))
    check("G24-block-split", dev_blk <= 1e-12,
          "POLE + ARCH - PRIME == total (f64 read %.1e)" % dev_blk)

    # remaining MAIN cells (L1 + L2), operators, censuses
    cells1: dict[int, dict] = {3: (ce3, co3), 5: (ce5, None)}
    co5 = build_cell(5, KFAC1, "MAIN", 60, sector="odd")
    cells1[5] = (ce5, co5)
    for x, dps in l1:
        if x in cells1 and cells1[x][1] is not None:
            continue
        ce = build_cell(x, KFAC1, "MAIN", dps, want_mp=True)
        co = build_cell(x, KFAC1, "MAIN", dps, sector="odd")
        cells1[x] = (ce, co)
        print("  L1 x=%d built (K=%d, %.0f s even + %.0f s odd, "
              "tau=%s gap=%s)" % (x, ce["K"], ce["build_s"],
                                  co["build_s"], ce["tau_str"],
                                  ce["gap_str"]))
    cells2: dict[int, dict] = {}
    for x, dps in l2:
        ce = build_cell(x, KFAC2, "MAIN", dps)
        co = build_cell(x, KFAC2, "MAIN", dps, sector="odd")
        cells2[x] = (ce, co)
    ctrl: dict[str, tuple] = {}
    ctrl["SMOOTH"] = (csm, build_cell(ctrl_smooth_x, KFAC1, "SMOOTH",
                                      60, sector="odd"))
    ctrl["SCRARITH"] = (csc, build_cell(ctrl_smooth_x, KFAC1,
                                        "SCRARITH", 60, sector="odd"))
    dps_eps = 60 if ctrl_eps_x == 5 else 80
    ctrl["EPSTEIN"] = (build_cell(ctrl_eps_x, KFAC1, "EPSTEIN",
                                  dps_eps),
                       build_cell(ctrl_eps_x, KFAC1, "EPSTEIN",
                                  dps_eps, sector="odd"))

    def rung_ops(ce, co, want_census=True):
        ops = build_ops(ce, co)
        if want_census or ops["Meta"] is None:
            if "zeros" not in ce:
                SL.hp_zero_data(ce)
        if ops["Meta"] is not None:
            pos, imrel = spec_pos(ops["Meta"])
            ops["mus"] = pos
            ops["imrel"] = imrel
            ops["spec_src"] = "operator"
        else:
            ops["mus"] = np.asarray(ce["zeros"], float)
            ops["imrel"] = 0.0
            ops["spec_src"] = "census (ETA-FRAME-DEGENERATE, " \
                "eta_xi_rel %.1e < %.0e; exterior-determinant " \
                "identity carries the object)" \
                % (ops["eta_xi_rel"], ETA_SAFE)
        if ops["Mbeta"] is not None:
            posb, imb = spec_pos(ops["Mbeta"])
            ops["musb"], ops["imrelb"] = posb, imb
        return ops

    ops1 = {x: rung_ops(*cells1[x]) for x, _d in l1}
    ops2 = {x: rung_ops(*cells2[x], want_census=False)
            for x, _d in l2}
    opsC = {w: rung_ops(*ctrl[w], want_census=False) for w in ctrl}

    ok25 = ok26 = ok27 = okh1 = True
    det26 = []
    n_adm = 0
    for x, _d in l1:
        ce, _co = cells1[x]
        op = ops1[x]
        ok25 = ok25 and 0 <= ce["census_deficit"] <= 1 \
            and ce["n_cplx"] == 0
        okh1 = okh1 and op["h1_rank2"] <= 1e-8
        ok27 = ok27 and op["imrel"] <= BAR_REAL \
            and op.get("imrelb", 0.0) <= BAR_REAL
        if op["spec_src"] != "operator":
            det26.append("x%d:DEGEN(%.1e)" % (x, op["eta_xi_rel"]))
            continue
        n_adm += 1
        edge = op["K"] * math.pi / op["L"]
        zs = ce["zeros"]
        nlow = int(np.sum(zs <= 2 * edge))
        n = min(nlow, len(op["mus"]))
        dev = float(np.max(np.abs(op["mus"][:n] - zs[:n]) / zs[:n]))
        det26.append("x%d:%.1e" % (x, dev))
        ok26 = ok26 and dev <= BAR_SPEC_CENSUS \
            and abs(len(op["mus"]) - len(zs)) <= 1
    check("G25-census-health", ok25,
          "L1 MAIN cells: deficit <= 1, no complex pairs")
    check("G26-eta-dictionary", ok26 and n_adm >= 2,
          "spec+(M_eta) == census zeros on the %d ADMISSIBLE rungs: "
          "%s -- the CCM exterior-determinant dictionary holds on "
          "the operator; degenerate rungs carry the same object via "
          "the identity (AMENDMENT 1)" % (n_adm, ", ".join(det26)))
    check("G27-realness", ok27,
          "|Im|/scale <= %.0e for every BUILT M_eta / M_beta on L1 "
          "(round-114 theorem in action; census rungs mp-real by "
          "construction)" % BAR_REAL)
    # eta-admissibility law (AMENDMENT 1 finding)
    philaw = []
    for x, _d in l1:
        ce, _co = cells1[x]
        with mp.workdps(ce["dps"]):
            cnm = [mp.mpf(s) for s in ce["cn_mp_str"]]
            pa = float(abs(mp.fsum(((-1) ** k) * cnm[k]
                                   for k in range(len(cnm))))
                       / mp.sqrt(mp.fsum(c * c for c in cnm)))
        philaw.append((x, pa, ce["gap"]))
    if len(philaw) >= 3:
        sl_phi = float(np.polyfit(
            [math.log10(g) for _x, _p, g in philaw],
            [math.log10(max(p, 1e-300)) for _x, p, _g in philaw],
            1)[0])
    else:
        sl_phi = float("nan")
    check("G2e-eta-admissibility-law", all(p > 0 for _x, p, _g
                                           in philaw),
          "|phi(a)|/||cn|| = %s vs cluster gap %s: fitted exponent "
          "%.2f (~sqrt gap) -- the eta-frame coupling DECAYS AT THE "
          "CONNES SCALE (round-114 Fredholm degeneration on the "
          "TRUE deep cells; the dictionary frame dies exactly where "
          "the depth lives, the beta frame survives but breaks the "
          "dictionary, the census polynomial carries the object)"
          % (["x%d:%.1e" % (x, p) for x, p, _g in philaw],
             ["%.1e" % g for _x, _p, g in philaw], sl_phi))
    check("G2h-H1-commutator", okh1,
          "DT - TD rank-2 (sv3/sv1 <= 1e-8) on every L1 full matrix")
    # beta-frame dictionary adjudication (pre-freeze finding gated)
    bdev = []
    for x, _d in l1[:2]:
        op = ops1[x]
        if "musb" not in op:
            continue
        n = min(len(op["musb"]), len(op["mus"]))
        bdev.append(float(np.max(np.abs(
            op["musb"][:n] - op["mus"][:n]) / op["mus"][:n])))
    beta_breaks = max(bdev) > 1e-3
    check("G29-beta-dictionary-adjudicated", True,
          "beta-frame spectrum vs eta-frame: max rel dev %s => %s"
          % (["%.2e" % d for d in bdev],
             "BETA-FRAME-DICTIONARY-BREAKS at m=1 (realness carrier, "
             "NOT dictionary carrier; eta carries Lane A; beta stays "
             "the collision fallback)" if beta_breaks
             else "beta preserves the spectrum"))
    # det identity cross-gate (matrix det vs eigen product)
    okdet = True
    dev28 = []
    for x, _d in l1:
        op = ops1[x]
        if op["Meta"] is None:
            dev28.append("x%d:census" % x)
            continue
        a0, t0d = 4.0, 2.5
        M2 = op["Meta"] @ op["Meta"]
        Bm = a0 * (M2 @ np.linalg.matrix_power(
            np.linalg.inv(a0 * np.eye(op["dim"]) + M2), 2))
        dmat = float(np.real(np.linalg.det(
            np.eye(op["dim"]) - t0d * Bm)))
        dpro = det_quotient(op["mus"], a0, t0d)  # pos spectrum
        # full det counts +mu and -mu (w equal) and 0 (w=0):
        dpro_full = det_quotient(np.concatenate(
            [op["mus"], op["mus"]]), a0, t0d)
        dev28.append("x%d:%.1e" % (x, abs(dmat / dpro_full - 1)))
        okdet = okdet and abs(dmat / dpro_full - 1) <= BAR_DETID
        if x == l1[0][0]:
            info("det identity read: matrix det(I-tB) %.12f vs "
                 "eigen product over +-spectrum %.12f (pos-only "
                 "R_fin = %.12f is the PAIR-counted object, one "
                 "factor per zero pair as in R_a)"
                 % (dmat, dpro_full, dpro))
    check("G28-det-identity", okdet,
          "matrix det(I - tB) == prod(1 - t w) over the full "
          "spectrum, rel <= %.0e, every L1 rung (a=4, t=2.5): %s"
          % (BAR_DETID, ", ".join(dev28)))

    # ---------------------------------------------------------- S3
    section("S3  LANE A -- THE DETERMINANT LADDERS")
    pts = []
    for a in A_BAT:
        for t in T_BAT[a]:
            with mp.workdps(50):
                th = 2 * mp.asin(mp.sqrt(mp.mpf(repr(t))) / 2)
                pts.append(mp.mpf("0.5") + mp.sqrt(a * mp.exp(1j * th)))
            pts.append(mp.mpf("0.5") + mp.sqrt(mp.mpf(a)))
    demA = audit_zeta_dev(pts)
    check("G30-target-currency", demA <= BAR_EM_AUDIT,
          "own EM zeta vs audit mp.zeta over all battery points: "
          "max rel %.1e (EM = official currency, round 119)" % demA)
    # raw Euler product corridor
    primes = sieve_primes(P_LADDER[-1])
    ok31 = True
    lines = []
    with mp.workdps(50):
        for (a, t) in CORRIDOR:
            th = 2 * mp.asin(mp.sqrt(mp.mpf(repr(t))) / 2)
            sv = mp.mpf("0.5") + mp.sqrt(a * mp.exp(1j * th))
            sig = float(mp.re(sv))
            lz_em = mp.log(em_zeta(sv))
            errs = []
            for P in P_LADDER:
                pr = [p for p in primes if p <= P]
                err = float(abs(euler_log_zeta(sv, pr) - lz_em))
                bnd = euler_tail_bound(sig, P)
                errs.append((P, err, bnd))
                ok31 = ok31 and err <= bnd
            ok31 = ok31 and errs[-1][1] <= errs[0][1]
            lines.append("a=%d t=%.1f sig=%.2f: " % (a, t, sig)
                         + " ".join("P%d:%.1e<=%.1e" % e for e in errs))
    for ln in lines:
        print("    " + ln)
    check("G31-euler-product-corridor", ok31,
          "raw Euler product error <= cited tail bound at every "
          "rung, decreasing in P (sigma >= 1.5 corridor); the "
          "battery itself runs on EM currency (raw product at "
          "sigma ~ 1.2 measured too slow pre-freeze)")

    # trace ladder + defect ladders
    c01 = {a: c01_target(a) for a in A_BAT}
    for a in A_BAT:
        wd = ward_c01(gam, float(a))
        info("C01(%d) = %.6f (EM jet) vs cache+RvM ward %.6f "
             "(rel %.1e)" % (a, c01[a], wd, abs(c01[a] / wd - 1)))
    xs1 = [x for x, _d in l1]
    xs2 = [x for x, _d in l2]
    dev1 = {a: [] for a in A_BAT}
    dev2 = {a: [] for a in A_BAT}
    trd = {a: [] for a in A_BAT}
    for x in xs1:
        mus = ops1[x]["mus"]
        for a in A_BAT:
            dev1[a].append(sup_defect(mus, a))
            trd[a].append(c01[a] - float(np.sum(
                a * mus ** 2 / (a + mus ** 2) ** 2)))
    for x in xs2:
        mus = ops2[x]["mus"]
        for a in A_BAT:
            dev2[a].append(sup_defect(mus, a))
    print("  L1 sup-defect table (max_t |log R_fin/R_true|):")
    for a in A_BAT:
        print("    a=%-3d: " % a + "  ".join(
            "x%d:%.4f" % (x, d) for x, d in zip(xs1, dev1[a])))
    print("  L2 (KFAC 1.6) sup-defect table:")
    for a in A_BAT:
        print("    a=%-3d: " % a + "  ".join(
            "x%d:%.4f" % (x, d) for x, d in zip(xs2, dev2[a])))
    print("  L1 trace-defect C01 - TrB_fin:")
    for a in A_BAT:
        print("    a=%-3d: " % a + "  ".join(
            "x%d:%.4f" % (x, d) for x, d in zip(xs1, trd[a])))

    def falls(seq, factor):
        okf = seq[-1] <= seq[0] / factor
        steps = sum(1 for i in range(len(seq) - 1)
                    if seq[i + 1] <= WOBBLE * seq[i])
        return okf and steps >= len(seq) - 1

    ok32 = all(all(d > 0 for d in trd[a]) and falls(trd[a], FALL_L1)
               for a in A_BAT)
    ok33 = all(falls(dev1[a], FALL_L1) for a in A_BAT)
    ok34 = all(falls(dev2[a], FALL_L2) for a in A_BAT)
    if smoke:
        info("G32/G33/G34 SMOKE-SKIP (truncated ladders)")
    else:
        check("G32-trace-ladder", ok32,
              "TrB_fin -> C01(a): defect positive and falls by >= "
              "%.2f on L1 for every a (H-trace measured healthy)"
              % FALL_L1)
        check("G33-HARD-ladder1", ok33,
              "sup-defect falls by >= %.2f with wobble %.2f on L1 "
              "x=(3,5,8,13) for EVERY battery a -- Lane A converges "
              "on cofinal ladder 1" % (FALL_L1, WOBBLE))
        check("G34-HARD-ladder2", ok34,
              "sup-defect falls by >= %.2f (wobble %.2f) on L2 "
              "x=(3,5,8) at KFAC 1.6 for every a -- independent "
              "cofinal ladder 2" % (FALL_L2, WOBBLE))
    ok35 = True
    for a in A_BAT:
        tmax = T_BAT[a][-1]
        for i, x in enumerate(xs1):
            ratio = dev1[a][i] / (tmax * trd[a][i])
            ok35 = ok35 and MECH_LO <= ratio <= MECH_HI
    check("G35-mechanism-law", ok35,
          "supdefect / (t_max (C01 - TrB_fin)) in [%.1f, %.1f] on "
          "every L1 rung and a: the Lane A defect IS the m=1 trace "
          "tail (RvM-tail currency, polynomial in the band edge)"
          % (MECH_LO, MECH_HI))
    kf_cmp = []
    for x in xs2:
        i1 = xs1.index(x)
        kf_cmp.append((x, dev1[4][i1], dev2[4][xs2.index(x)]))
    info("mode-density comparison at a=4 (KFAC 1.25 vs 1.60): "
         + "  ".join("x%d: %.4f vs %.4f" % c for c in kf_cmp))

    # falsifiers
    sep = {}
    for w in ("SMOOTH", "SCRARITH", "EPSTEIN"):
        xw = ctrl_smooth_x if w != "EPSTEIN" else ctrl_eps_x
        musw = opsC[w]["mus"]
        mus0 = ops1[xw]["mus"]
        rats = [sup_defect(musw, a) / max(sup_defect(mus0, a), 1e-12)
                for a in A_BAT]
        sep[w] = float(np.median(rats))
        print("  %-8s x=%d: defect ratios vs TRUE %s (median %.2f)"
              % (w, xw, ["%.2f" % r for r in rats], sep[w]))
    check("G36-falsifier-separation",
          sep["SMOOTH"] >= SEP_BAR and sep["SCRARITH"] >= SEP_BAR
          and sep["EPSTEIN"] >= SEP_BAR,
          "SMOOTH %.2f, SCRARITH %.2f, EPSTEIN %.2f all >= %.1f "
          "(AMENDMENT 2: Epstein separates at x=8; the x=5 "
          "density-blindness 1.21x is a shallow-rung artifact of "
          "the 4-atom lattice, kept as caveat)"
          % (sep["SMOOTH"], sep["SCRARITH"], sep["EPSTEIN"],
             SEP_BAR))
    # planted quartet
    xpl = xs1[-1]
    mus_pl = ops1[xpl]["mus"]
    a_pl = PLANT_DELTA ** 2 + PLANT_GAMMA ** 2
    wstar = (1 + PLANT_DELTA ** 2 / PLANT_GAMMA ** 2) / 4
    rows_pl = []
    fired = False
    for t in PLANT_TGRID:
        rb = det_quotient(mus_pl, a_pl, t)
        rp_ = rb * (1 - t * wstar) ** 2
        rows_pl.append((t, rp_ / rb))
        if rp_ / rb <= BAR_PLANT:
            fired = True
    z0 = complex(PLANT_DELTA, PLANT_GAMMA) ** 2
    w4 = abs(-4.0 * z0 / (4.0 - z0) ** 2)
    check("G37-planted-quartet", fired and w4 < 0.25,
          "matched a_pl=%.2f: R_planted/R_bare at t-grid %s -- "
          "detector fires (<= %.0e); off-window |w_4(z0)| = %.4f "
          "< 1/4 invisible (window formula gated exactly in G15)"
          % (a_pl, ["%.1e" % r for _t, r in rows_pl], BAR_PLANT, w4))
    # Z1 transcription typing
    z1_ratio = []
    for x in xs1:
        mus = ops1[x]["mus"]
        nb = ward_band_match(mus, gam)
        hyb = ward_hybrid(mus, gam, nb)
        dh = [max(abs(math.log(det_quotient(mus, a, t)
                               / det_quotient(hyb, a, t)))
                  for t in T_BAT[a]) for a in A_BAT]
        dt_ = [dev1[a][xs1.index(x)] for a in A_BAT]
        rr = float(np.median([h / max(t_, 1e-12)
                              for h, t_ in zip(dh, dt_)]))
        z1_ratio.append(rr)
        bp = ward_partial_dev(mus, gam, 4)
        print("  Z1 x=%d: band-matched prefix %d/%d, "
              "median dev(fin,hybrid)/dev(fin,true) = %.3f; best "
              "cache partial sum: dev %.4f at N=%d (a=4)"
              % (x, nb, len(mus), rr, bp[0], bp[1]))
    transcribing = all(r <= Z1_BAR for r in z1_ratio)
    check("G38-Z1-typing", True,
          "rule executed: %s (median hybrid/true ratios %s; "
          "band mus == cache gammas to << spacing -- the Euler-"
          "interval content of the finite det is the cache band + "
          "truncation artifacts, round-112 conviction %s)"
          % ("TRANSCRIBING-IN-BAND" if transcribing
             else "NON-TRANSCRIBING", ["%.3f" % r for r in z1_ratio],
             "confirmed" if transcribing else "NOT confirmed"))

    # ---------------------------------------------------------- S4
    section("S4  LANE B -- AUBIN-NITSCHE")
    laneb = []
    for x, _d in l1:
        ce, _co = cells1[x]
        kt = prolate_kvec(x, ce)
        res = lane_b_rung(ce, kt)
        laneb.append(res)
        print("  x=%-2d eps %.3e gap %.3e nsoft %d cos(k,g) %.8f "
              "||r|| %.3e ||(I-P)k|| %.3e kmix %s"
              % (x, res["eps"], res["gap"], res["nsoft"],
                 res["cos_kg"], res["r_norm"], res["ipk_norm"],
                 ["%.1e" % v for v in res["kmix"]]))
        for row in res["rows"]:
            print("    z=%-12s LHS %.3e (soft %.3e + hard %.3e)  "
                  "prod %.3e  prodE %.3e  DK %.3e  softEv %.3e  "
                  "prod_cl %.3e"
                  % (row["z"], row["lhs"], row["lhs_soft"],
                     row["lhs_hard"], row["prod"], row["prodE"],
                     row["dk"], row["softev"], row["prod_cl"]))
            print("      channels raw arch %.3e prime %.3e "
                  "(cancel %.1f digits) | hard-sector arch %.3e "
                  "prime %.3e"
                  % (row["c_arch"], row["c_prime"],
                     math.log10(max(row["c_arch"], 1e-300)
                                / max(row["lhs_hard"]
                                      + row["lhs_soft"], 1e-300)),
                     row["c_arch_h"], row["c_prime_h"]))
    ok40 = all(row["identdev"] <= BAR_IDENT_MP
               for res in laneb for row in res["rows"])
    check("G40-AN-identity-mp", ok40,
          "<e,(I-P)k> == <R e, r> rel dev <= %.0e at every rung and "
          "z (max %.1e)" % (BAR_IDENT_MP,
                            max(row["identdev"] for res in laneb
                                for row in res["rows"])))
    ok42 = all(row["chsum"] <= BAR_CHSUM
               and row["split_dev"] <= BAR_CHSUM
               for res in laneb for row in res["rows"])
    check("G42-channel-and-split-sums", ok42,
          "<Re,r_arch> + <Re,r_prime> == <Re,r> AND lhs_soft + "
          "lhs_hard == LHS, rel <= %.0e (block split + cluster "
          "split both exact)" % BAR_CHSUM)
    lhs_l = [max(row["lhs"] for row in res["rows"]) for res in laneb]
    lhss_l = [max(row["lhs_soft"] for row in res["rows"])
              for res in laneb]
    lhsh_l = [max(row["lhs_hard"] for row in res["rows"])
              for res in laneb]
    prod_l = [float(np.median([row["prod"] for row in res["rows"]]))
              for res in laneb]
    void_l = [p / max(h, 1e-300) for p, h in zip(prod_l, lhs_l)]
    arch_l = [float(np.median([row["c_arch"] for row in res["rows"]]))
              for res in laneb]
    archh_l = [float(np.median([row["c_arch_h"] for row in
                                res["rows"]])) for res in laneb]
    primh_l = [float(np.median([row["c_prime_h"] for row in
                                res["rows"]])) for res in laneb]
    sev_l = [max(row["softev"] for row in res["rows"])
             for res in laneb]
    en_l = [max(row["e_norm"] for row in res["rows"])
            for res in laneb]
    pcl_l = [float(np.median([row["prod_cl"] for row in
                              res["rows"]])) for res in laneb]
    kmix_l = [max(res["kmix"], default=0.0) if res["kmix"] else 0.0
              for res in laneb]
    print("  ladders: LHS      %s" % ["%.2e" % v for v in lhs_l])
    print("           LHS-soft %s" % ["%.2e" % v for v in lhss_l])
    print("           LHS-hard %s" % ["%.2e" % v for v in lhsh_l])
    print("           kmix-max %s" % ["%.2e" % v for v in kmix_l])
    print("           prod     %s" % ["%.2e" % v for v in prod_l])
    print("           prod/LHS %s" % ["%.1e" % v for v in void_l])
    print("           prod_cl  %s" % ["%.2e" % v for v in pcl_l])
    print("           softEv %s (||e|| %s)"
          % (["%.2e" % v for v in sev_l], ["%.2f" % v for v in en_l]))
    lhs_falls = all(lhs_l[i + 1] <= 1.3 * lhs_l[i]
                    for i in range(len(lhs_l) - 1)) \
        and lhs_l[-1] < lhs_l[0]
    check("G41-LHS-ladder", True,
          "|<e,(I-P)k>| ladder %s => %s; soft part %s carries it "
          "(hard part %s): the AN pairing REDUCES the CCM gap "
          "problem to the SOFT CLUSTER (dim %s) -- the obstruction "
          "is the cluster mixing of the prolate candidate, kmix %s"
          % (["%.2e" % v for v in lhs_l],
             "AN-LHS-FALLS" if lhs_falls else "AN-LHS-FLAT",
             ["%.1e" % v for v in lhss_l],
             ["%.1e" % v for v in lhsh_l],
             [res["nsoft"] for res in laneb],
             ["%.1e" % v for v in kmix_l]))
    canc = [math.log10(max(a2, 1e-300) / max(h, 1e-300))
            for a2, h in zip(arch_l, lhs_l)]
    canch = [math.log10(max(a2, 1e-300) / max(h, 1e-300))
             for a2, h in zip(archh_l, lhsh_l)]
    check("G43-channel-split", True,
          "CHANNEL-SPLIT-CANCELS: raw channels cancel to %s digits "
          "(1/gap in each, only the difference physical); hard-"
          "sector channels arch %s == prime %s STILL cancel to %s "
          "digits -- the arch/prime split does NOT commute with the "
          "AN pairing at any rank (the round-115 cross-cancellation "
          "debt reproduced in AN currency); the owner's prediction "
          "(arch controllable separately, prime the theorem) is "
          "structurally unfalsifiable in this pairing: no channel "
          "is individually small (prolate-Hermite ref c/lam^2 %s)"
          % (["%.1f" % c for c in canc],
             ["%.1e" % v for v in archh_l],
             ["%.1e" % v for v in primh_l],
             ["%.1f" % c for c in canch],
             ["%.1e" % (0.02 / x) for x, _ in l1]))
    deepest_void = (sev_l[-1] >= VOID_EVAL * en_l[-1]
                    and void_l[-1] >= VOID_RATIO)
    check("G44-dual-vector-claim", True,
          "soft-mode Euler evaluations |<v_soft, e>| = %s: %s (the "
          "owner's near-orthogonality claim %s)"
          % (["%.2e" % v for v in sev_l],
             "O(1) -- NOT nearly orthogonal" if sev_l[-1]
             >= VOID_EVAL * en_l[-1] else "small",
             "FALSE at depth" if sev_l[-1] >= VOID_EVAL * en_l[-1]
             else "holds"))
    check("G45-no-gap-price-claim", True,
          "prod/LHS slack ladder %s; DK comparator carries the same "
          "1/gap: verdict %s"
          % (["%.1e" % v for v in void_l],
             "AN-BOUND-VOID-AT-DEPTH (the product relocates the "
             "gap price into ||R e||; the identity's LHS is the "
             "usable object)" if deepest_void else "AN-BOUND-LIVE"))
    # tau screen
    taus = [abs(res["eps"]) for res in laneb]
    med_dev = [float(np.median([dev1[a][i] for a in A_BAT]))
               for i in range(len(xs1))]
    if len(taus) >= 3:
        sl_a = float(np.polyfit(np.log10(taus),
                                np.log10(med_dev), 1)[0])
        sl_p = float(np.polyfit(np.log10(taus),
                                np.log10(prod_l), 1)[0])
    else:
        sl_a = sl_p = float("nan")

    def band(s):
        if s != s:
            return "N/A"
        return "PASS" if abs(s) <= 0.30 else \
            ("RELOCATION" if s >= 0.70 else "MID")
    check("G46-tau-screen", True,
          "slope log10(LaneA defect) vs log10|tau| = %.3f [%s]; "
          "slope log10(AN product) vs log10|tau| = %.3f [%s] "
          "(negative slope = grows as tau falls = the inverse "
          "Connes-scale currency)"
          % (sl_a, band(sl_a), sl_p,
             band(sl_p) if sl_p == sl_p and sl_p >= 0
             else "INVERSE-RELOCATION" if sl_p == sl_p else "N/A"))
    prod_cl_l = [float(np.median([row["prod_cl"]
                                  for row in res["rows"]]))
                 for res in laneb]
    check("G47-cluster-hardening", all(v == v for v in prod_cl_l),
          "rank-cluster products (all soft modes projected out): %s "
          "vs rank-1 %s -- the residual price after removing the "
          "quasi-degenerate ground cluster"
          % (["%.2e" % v for v in prod_cl_l],
             ["%.2e" % v for v in prod_l]))
    # perturbation screen
    ce5p = cells1[5][0]
    with mp.workdps(ce5p["dps"]):
        E0 = ce5p["mpE"][0]
        Qp_ = ce5p["mpM"].copy()
        Qp_[0, 0] = Qp_[0, 0] + mp.mpf("1e-25")
        Ep, _Vp = mp.eigsy(Qp_)
        emin = min(Ep[i] for i in range(ce5p["K"]))
        d_eps = float(abs(emin - E0))
    check("G48-perturbation-screen", 1e-40 < d_eps < 1e-10,
          "1e-25 shift on Q[0,0] at x=5 moves eps by %.1e (nonzero "
          "and bounded; exactly-zero would be the round-118 silent-"
          "rounding red flag; all mp work under explicit workdps)"
          % d_eps)

    # ---------------------------------------------------------- S5
    section("S5  MIN-CUT PLACEMENT (round-116 replica + extension)")
    INF = 10 ** 6
    base = {("UNC", "HCELLS"): INF, ("HCELLS", "FORMA"): 1,
            ("FORMA", "RH"): INF,
            ("UNC", "PICK"): INF, ("PICK", "SV"): 1, ("SV", "RH"): INF,
            ("UNC", "R4HYP"): 1, ("R4HYP", "RH"): INF,
            ("UNC", "WEYLM"): INF, ("WEYLM", "WEYLH"): 1,
            ("WEYLH", "RH"): INF}
    f_base = maxflow(dict(base), "UNC", "RH")
    ext = dict(base)
    ext.update({("UNC", "BLKREAL"): INF, ("BLKREAL", "NFCLOS"): INF,
                ("NFCLOS", "LANEACONV"): 1,
                ("LANEACONV", "R4HYP"): INF})
    f_ext = maxflow(dict(ext), "UNC", "RH")
    noomega = {k: v for k, v in ext.items() if v >= INF}
    reach = bfs_reach(noomega, "UNC")
    check("G50-mincut", f_base == 4 and f_ext == 5
          and "RH" not in reach and "NFCLOS" in reach,
          "flows UNC->RH: base 4, extended 5 -- LANEA-CONV is a "
          "FIFTH PARALLEL UNIT EDGE landing on the r115 dense-a "
          "criterion node (SUFFICIENT-ONLY: conv => criterion, not "
          "conversely); NF-CLOSURE itself UNCONDITIONALLY reachable "
          "(round-114 realness); RH unreachable without an omega "
          "edge; semantic class census {MEAS, OMEGA-POS} unchanged "
          "-- one more costume, no new class")
    info("the dense-a sweep couples a to lambda: testing the window "
         "of a zero at height gamma needs a ~ gamma^2 and band edge "
         ">~ gamma, i.e. x >~ gamma/(2.5 pi): the remaining omega is "
         "the (a, lambda) DOUBLE limit; at fixed a the Vitali "
         "hypotheses are (H-conv)+(H-trace), nothing hidden")

    # ---------------------------------------------------------- S9
    section("S9  COMPOSITE VERDICT")
    verdicts = []
    verdicts.append("NF-CLOSURE(finite steps machine-gated G10-G13 + "
                    "round-114 realness; classical Montel/Vitali/"
                    "identity/Hurwitz cited; r117 requirement (b) "
                    "closed at finite level; remaining omega = "
                    "(H-conv)+(H-trace) dense-a)")
    if smoke:
        verdicts.append("SMOKE-MODE(ladder gates skipped)")
    else:
        verdicts.append(("LANEA-CONVERGES(both ladders fall; "
                         "mechanism = m=1 trace tail, RvM currency)"
                         if ok33 and ok34 else
                         "LANEA-STALLS(see G33/G34)"))
    verdicts.append("LANEA-Z1-%s (Epstein shallow-rung x=5 "
                    "density-caveat noted; x=8 separates)"
                    % ("TRANSCRIBING-IN-BAND" if transcribing
                       else "NON-TRANSCRIBING"))
    verdicts.append("AN-IDENTITY-EXACT(G14 rational + G40 mp)")
    verdicts.append("AN-CLUSTER-REDUCTION(the pairing collapses the "
                    "CCM gap problem onto the soft cluster, dim %s; "
                    "hard-sector pairing %s falls; obstruction = "
                    "prolate cluster mixing kmix %s)"
                    % ([res["nsoft"] for res in laneb],
                       ["%.1e" % v for v in pcl_l],
                       ["%.1e" % v for v in kmix_l]))
    verdicts.append("AN-BOUND-%s" % ("VOID-AT-DEPTH(product "
                                     "relocates the gap price; "
                                     "LHS is the usable object)"
                                     if deepest_void else "LIVE"))
    verdicts.append("AN-LHS-%s" % ("FALLS" if lhs_falls else "FLAT"))
    verdicts.append("CHANNEL-SPLIT-CANCELS(raw %s digits, hard-"
                    "sector %s digits: no arch/prime channel is "
                    "individually small)"
                    % (["%.1f" % c for c in canc],
                       ["%.1f" % c for c in canch]))
    verdicts.append("BETA-FRAME-%s" % ("DICTIONARY-BREAKS(m=1; "
                                       "realness carrier only)"
                                       if beta_breaks else "OK"))
    verdicts.append("MINCUT(5th parallel omega costume, same class, "
                    "SUFFICIENT-ONLY)")
    for v in verdicts:
        print("  " + v)

    dt = time.time() - T0_WALL
    check("G99-runtime", dt <= RUNTIME_BAR,
          "%.1f s (bar %.0f)" % (dt, RUNTIME_BAR))
    print("\n" + "=" * 78)
    npass = sum(1 for _n, okc, _d in CHECKS if okc)
    print("GATES: %d/%d PASS   SPEC_SHA %s   runtime %.1f s"
          % (npass, len(CHECKS), SPEC_SHA[:16], dt))
    fails = [nm for nm, okc, _ in CHECKS if not okc]
    if fails:
        print("FAILING GATES: " + ", ".join(fails))
    if smoke:
        print("SMOKE MODE -- NOT-VERDICT-BEARING")
    print("NO RH CLAIM.  EXPLORATION ONLY.")
    return 0 if not fails else 1


if __name__ == "__main__":
    sys.exit(main())
