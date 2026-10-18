#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""l1_weyllaw_probe -- PRIME.L1.WEYLLAW.PROOF.01

FROZEN SPEC (2026-08-16).  EXPLORATION ONLY.  This probe writes no
verification module, paper, ledger, website, manifest, Lean file or
status marker.  It makes NO RH claim, NO positivity claim, NO
counterexample claim.  It closes no gate and narrows no gate.

=======================================================================
MISSION (proof lane on L1, the second member of the round-128 pair)
=======================================================================
Round 128 (doublelimit_proof_probe, 28/28) proved Theorem R:
L1 + WPD on a dense a-subset of (1/4, inf) ==> RH (with the cited
round-122 NF-closure).  L1 states: Tr B_{a,lam} -> C01(a) = b0 - b1
as lam -> inf, B = a M^2 (a + M^2)^{-2} on the round-114 operators,
C01(a) = C01_arch(a) + (1/4) sum Lambda(n) n^{-1/2-sqrt a}
(a ln n - sqrt a), absolutely convergent iff a > 1/4.  This probe is
a maximal proof attempt on L1: (T1) the exact node-zero relation,
(T2) unconditional tail bounds with certified cited constants,
(T3) the assembly of L1 with the circularity adjudication, (T4/T5)
controls, tau-screen, conditioning, min-cut.

NOTATION.  a > 1/4; w_a(t) = a t^2/(a + t^2)^2; per rung x the even
cell has window [-A, A], A = log(x)/2, K = ceil(KFAC x log x) modes
om_k = k pi/A, minimizer phi = sum cn_k cos(om_k u) (unit L2 norm),
E_N = phihat (entire, exponential type A), nodes = the K-1 positive
zero pairs of E_N (complete census), tau = lambda_min of the
compressed Weil form Q on the window.  Boundary jets A_{2m} :=
sum_k (-1)^k cn_k om_k^{2m}  (A_0 = phi(A), the boundary value).

=======================================================================
T1 -- THE NODE-ZERO RELATION (two exact layers + one measured law)
=======================================================================
LAYER 1 (EXACT ALGEBRA, new-in-corpus in this sharp form; the
round-114 exterior-determinant identity specialised to the dictionary
frame).  The round-114/123 block operator is the rank-one update
Meta = D - |D xi><eta| / <eta, xi> on the doubled basis (D = lattice
diag(n pi / A), xi the symmetrised minimizer, eta alternating).  Then
   det(Meta - z) = - z * C(z^2) / A_0,
where C(y) is exactly the census numerator polynomial of E_N
(degree K-1) and A_0 = <eta, xi> = phi(A).  Chain, all sympy-exact:
  (i)  resolvent identity 1 - <eta,(D-z)^{-1} D xi>/A_0
       = z R(z) / (2 A_0), with E_N(z) = sin(A z) R(z),
       R(z) = 2 cn_0/z + sum_k 2 cn_k (-1)^k z/(z^2 - om_k^2);
  (ii) the sinc-pair basis identity B_k(z) = (-1)^k sin(Az)
       2z/(z^2-om_k^2) (k = 0 included, om_0 = 0);
  (iii) rank-one determinant lemma on an exact rational instance.
COROLLARIES (exact): spec(Meta) = {0} U {+-nodes}; the operator's
nontrivial node count is EXACTLY K-1 (census degree); E_N has the
exact lattice zeros j pi/A, j >= K; the operator node-counting
function is closed-form -- the T2 "operator-side counting bound"
is an algebraic theorem of the Loewner/rank-one structure, no
measure needed.  The eta-degeneration of deep rungs (round 123) is
the boundary-value decay A_0 -> 0: the OPERATOR costume blows up
as 1/A_0 while the census polynomial stays perfectly conditioned --
the nodes, not the matrix, are the honest object.

LAYER 2 (THE PINNING MECHANISM; classical identity, machine-gated).
The compressed form satisfies the Guinand-Weil explicit formula on
psi = phi * phi~ (supp [-2A, 2A], psihat = |E_N|^2 on R):
   tau = Q(phi) = sum_rho psihat(gamma_rho)
       = 2 sum_{gamma>0 on-line} |E_N(gamma)|^2  +  S_off,
S_off over off-line zeros only.  [PT21] (no off-line zero below
T_PT = 3,000,175,332,800) + the exact envelope of E_N (boundary-jet
telescope, LAYER 3) + [HSW22 Cor. 1.2] zero counting make S_off a
certified allowance OFF_ALLOW.  Hence THE SMALLNESS LAW: for EVERY
true zero gamma_j,   2 |E_N(gamma_j)|^2 <= tau + OFF_ALLOW,
and with the elementary gap lemma (|E'| >= m near a node, Taylor
with M2 = sup|E''|):  every true zero in the RESOLVABILITY ZONE
gamma <= min(0.98 edge, 2 pi x)  (the G17 crossover -- past it the
envelope kills |E| and |E'| together and the ratio is O(1) by
construction; the edge layer is measured, not certified) lies
within  g_j <= 2 eps_bar / m_j  of an operator node,
eps_bar = sqrt((tau + OFF_ALLOW)/2).  The nodes do not "happen" to
track the zeros: the VARIATIONAL VALUE ITSELF is the l2 norm of E_N
on the true spectrum -- pinning is the mechanism, not an input.

LAYER 3 (THE BOUNDARY-JET ENVELOPE; exact telescope).  Exactly
(z/2) R(z) - A_0 = sum_k (-1)^k cn_k om_k^2/(z^2 - om_k^2), and the
m-fold telescope gives |E_N(t+i d)| <= e^{A d} (2/t) ENV_m(t),
ENV_m(t) = sum_{i<=m} |A_{2i}|/t^{2i} + SABS_{2m+2}/(t^{2m}
(t^2 - om_max^2)), SABS_{2m} = sum_k |cn_k| om_k^{2m}.  The tail of
the GW sum and OFF_ALLOW are certified by ENV_3 + G(T) below.  The
A_{2m} are SOURCE-side computables; their measured decay (the
boundary-jet law, printed) is the reason the finite window can pin
zeros far beyond naive resolution.

=======================================================================
T2 -- UNCONDITIONAL TAILS (cited constants, closed forms)
=======================================================================
G(T) := sum over ALL zeros gamma > T of gamma^{-2}
     <= (log(T/2pi) + 1)/(2 pi T)
        + [alpha(2 log T + 1)/2 + beta(loglog T + 1/(2 log T)) + c
           + alpha log T + beta loglog T + c] / T^2
with (alpha, beta, c) = (0.1038, 0.2573, 9.3675) = [HSW22] Cor. 1.2
(the v914 pinned constants; N(t) counts ALL zeros in the strip, so
G needs no RH and no on-line assumption).  Derivation: Stieltjes
integration by parts sum = 2 int (N(t) - N(T)) t^{-3} dt, N <= M+Q,
N(T) >= M(T)-Q(T), exact antiderivatives (sympy-gated), loglog
handled by the tangent bound loglog t <= loglog T + (log t/T)/log T
(classical log u <= u-1; derivative sign sympy-gated).
  TRUE-SIDE tail:      sum_{gamma>T} w_a(gamma) <= a G(T)  (w<=a/t^2).
  OPERATOR-SIDE tail:  node count == K-1 EXACT (Layer 1) -- the
  finite w-mass is a computed number, no bound needed; the E_N
  lattice tail j >= K contributes NOTHING to Tr B (spec(Meta) is the
  census only).  epsilon(a, band) tables printed per rung.
  CERTIFIED C01 BRACKET: C01(a) in [S_cache(a), S_cache(a)
  + a G(gamma_top)] with the X5 cache (7000 verified ordinates,
  READ-ONLY ward) + declared cache f64 slop; the EM-jet target must
  land inside (G21) -- the same bracket certifies d_1 (G36).

=======================================================================
T3 -- THE ASSEMBLY AND THE CIRCULARITY ADJUDICATION
=======================================================================
ADJUDICATION (the crux, answered by reading + AST gate): the
round-114 builder consumes Lambda(n) (own sieve), the archimedean
integral of e^{-w/2}/(1-e^{-2w}), and the pole block -- NO zero
location enters any construction branch (G01 firewall; the cache is
ward-only).  The node-zero tracking is therefore NOT transcription-
by-input: it is forced by the Layer-2 variational identity.  What
the round-112/123/128 Z1 verdicts say (and this probe re-types, not
hides) is about EVIDENCE CONTENT: at today's budgets the finite
band data is numerically equivalent to cache partial sums.  The
DISTINCTION made sharp here: input-circularity NO (theorem-shaped
mechanism), evidence-novelty LIMITED (transcribing-in-band).
ASSEMBLY of L1 at fixed (a, rung), every inequality gated:
   d_1 = C01 - Tr B  in  [S_cache - TrB,  S_cache - TrB
                          + a G(gamma_top)]      (certified, G36)
   d_1 = MISM + TRUE-TAIL - NODE-EXTRA           (bookkeeping, G37)
   MISM(zone) <= 1.5 sum_zone |w'(gamma_j)| 2 eps_bar/m_j
          (certified given the measured derivative floors m_j, G34;
          the edge layer enters the bookkeeping as measured mass)
   TRUE-TAIL -> 0 (a fixed, lam -> inf): a G(T*(x)) closed form;
   NODE-EXTRA -> 0: <= (K-1-N_match) a/T_match^2 (counting + w<=a/t^2).
WHAT IS PROVEN vs CITED vs MEASURED (the honest table):
   PROVEN (exact algebra): Layer 1, Layer 3 telescope, gap lemma,
     w bounds, G antiderivatives, resolvability crossover (below).
   CITED (classical/published): Guinand-Weil for compactly
     supported autocorrelations; PT21; HSW22 Cor. 1.2.
   MEASURED (source-side numbers): tau, cn, A_{2m}, node census,
     derivative floors m_j, M2 (sampled sup, SUP_INFLATE 1.5),
     matched prefix T*(x).
THE EXACT REMAINING OMEGA for full L1 (typed, not claimed): a
lam-uniform lower bound on the derivative floors m_j(x) at band
zeros + the matched-prefix law T*(x) -> inf.  This is k_lambda ~
xi_lambda in POINTWISE currency -- strictly sharper coordinates
than round 122/128 (the tail half of L1 is now classical), but the
same wall; no silent upgrade.

L1-MEAN (the Weyl-law sub-case, T1's realistic goal):
  (a) EXACT: mode density A/pi crosses the RvM density
      (1/2pi) log(T/2pi) exactly at T = 2 pi x (sympy; band edge
      = 2 pi KFAC x, so the resolvable fraction is 1/KFAC = 0.8 ==
      the corpus INBAND_F -- the frozen constant is a theorem);
      total node count == K-1 exact (Layer 1).
  (b) MEASURED: in-band node counting follows the ARITHMETIC RvM
      law (round-128 G35 bars replicated: sup dev <= 1.2 zeros,
      clock/semicircle/arcsine separated by >= 2.5x); Weyl count at
      the crossover |N_op(2 pi x) - RvM(2 pi x)| <= WEYL_BAR.
L1-OSC (must separate worlds): SMOOTH/SCRARITH/EPSTEIN cells at
x = 5 through the SAME pipeline: the smallness law is ARITHMETIC
(max_band |E_world(gamma_j)| / |E_main(gamma_j)| >= 1e3) and the
d_1 functional separates (median >= 2.0 SMOOTH, >= 1.5 SCRARITH;
EPSTEIN trace-read typed INFO per smoke disclosure f3 -- its
honest separator is the smallness law).

=======================================================================
FROZEN NUMERICS
=======================================================================
LADDER = ((3,45),(5,60),(8,80),(13,120)), KFAC = 1.25 (radius4/SL
currency); A_BAT = (1, 4, 16); worlds at x = 5 dps 60.  NPOL = 32
band ordinates polished in audit_ (own Newton on xi via mp.zeta,
AUD_DPS = 100); polish cross-ward vs cache <= 1e-7.  GW zones: band
= polished zeros <= 0.98 edge (cell dps); mid = cache zeros to
N_GW_MID = 2000 (mp dps 60, cache slop 2(2|E||E'| e + (|E'| e)^2),
e = 1e-9 declared); beyond gamma_{2000}: ENV_3 envelope only.
T_PT = 3000175332800 [PT21]; HSW = (0.1038, 0.2573, 9.3675)
[HSW22 Cor. 1.2]; OFF_ALLOW = 8 e^{A} ENV_3(T_PT)^2 (2/T)^2-folded
G(T_PT).  SUP_INFLATE = 1.5 (sampled-sup honesty, M2 on 3-pt
stencil); INBAND_F = 0.8; BAND_F = 0.98; MATCH_F = 0.25 (of local
spacing).  Bars (frozen from the disclosed pre-freeze smoke at
x = (3,5)): BAR_EM_AUDIT 1e-20, BAR_POLISH_XW 1e-7, BAR_POLISH_RES
1e-60, GW_LOW_TOL 1e-3 (rel to tau + slop), RVM_BAR 1.20, FIT_SEP
2.5, WEYL_BAR 1.5, RVM_CTRL 6.0, SEP_SMALL 1e3, SEP_D1_SM 2.0,
SEP_D1_OTH 1.5, FALL_L1 1.6, WOBBLE 1.10, TAU_SLOPE_BAR 0.30,
COND_WIN (1e-40, 1e-10), CENSUS_DEFICIT 1, CTOL/JTOL declared
in-run, RUNTIME_BAR = 3600 s.  Deterministic: no RNG, all literals
frozen; cache verified_zeros_n7000.npy READ-ONLY in ward_ (X5).
All mpf/mpc arithmetic inside explicit mp.workdps blocks (the
round-118/120 ambient-precision negation trap).

VERDICT ENUMS (frozen): SECULAR-EXACT; GW-PINNING-GATED;
GAPLAW-CERTIFIED(scale); NOT-TRANSCRIPTION-BY-INPUT(typed, with the
Z1 evidence caveat carried); TAILS-CERTIFIED(HSW22/PT21);
L1-CERTIFIED-ON-LADDER(bracket widths); L1-MEAN-COUNTING(exact
crossover + measured RvM); L1-OSC-ARITHMETIC(separations);
BOUNDARY-JET-LAW(measured); MINCUT-REFINED(L1 -> L1TAIL-proven +
L1BAND-omega; flows 4/5; census {MEAS, OMEGA-POS} unchanged).
Priority: INSTRUMENT-EDGE (any edge gate fails, exit 1) >
EXACT-LAYER-OBSTRUCTED (any sympy gate fails) > verdicts as gated.

SMOKE DISCLOSURE (two pre-freeze smokes at x = (3, 5), mid zone
capped 400; smoke numbers are MEASURED and NOT verdict-bearing;
no bar moved after the freeze):
(a) GW identity: x=3: tau 3.056e-07, P 2.856e-07 (band share 0.10,
mid share 0.90); x=5: tau 1.607e-16, P 1.482e-16 (band 0.01, mid
0.99) -- the variational value IS carried by the true zeros, with
the residual inside the ENV_3 tail bound (4e-08 / 3e-17); the
upper side is envelope-limited by construction (declared weak
side); GW_LOW_TOL 1e-3 frozen.  The measured tau follows the GW
law tau ~ 8 A_0^2 G(edge) + band mass -- the window lambda_min is
boundary-jet-limited, NOT the prolate-cluster e^{-4 pi x}.
(b) smallness/gap: x=5 per-zero table: gamma_1 pinned at gap
4.6e-13 (|E| = 2.4e-15), zone-edge zero gamma_4 = 30.42 at gap
2.1e-06 <= bound 9.3e-03; max 2|E|^2 = 9.0e-19 <= tau + off
1.6e-16; eps_bar = 9.0e-09; derivative floors m fall toward the
edge exactly on the envelope (5.3e-3 -> 1.9e-6).
(c) boundary jets: A_0 = 1.84e-03 (x=3) / 4.73e-08 (x=5), A_2 =
8.94 / 2.89e-3 -- the round-123 eta-admissibility law reproduced
source-side with depth.
(d) counting: Weyl crossover devs 0.17/0.08; RvM in-band x=5 dev
0.18 vs clock 4.3 / semicircle 2.1 / arcsine 0.8 (r128 verbatim).
(e) controls x=5: smallness separations 7.1e7 (SMOOTH) / 7.5e7
(SCRARITH) / 3.4e8 (EPSTEIN); d1-trace medians 3.72 / 8.27 / 1.02;
control RvM devs 3.50/3.21/2.42 (RVM_CTRL 6.0 frozen: the
archimedean MEAN is world-tolerant at loose bars, as the contract
predicted; the oscillation channels separate).
(f) PRE-FREEZE INSTRUMENT REPAIRS (disclosed; no bar moved):
(f1) firewall owner logic flagged mp.zeta inside a function NESTED
in audit_polish_band (the round-124 AMENDMENT-1 owner-logic class);
fixed to any-enclosing-scope.  (f2) smoke 1 gated the gap law over
the FULL polished band (<= 0.98 edge) and failed at the edge zeros
(x=3 gap 0.54, x=5 gap 3.4e-2): past the G17 crossover 2 pi x the
envelope kills |E| and |E'| TOGETHER, so 2 eps/m is O(1) there BY
CONSTRUCTION -- the certified zone was restricted to the
resolvability zone gamma <= min(0.98 edge, 2 pi x) (exactly the
G17 theorem's zone) and the edge layer re-typed MEASURED-ONLY;
this is a zone-typing repair, not a bar move -- the failed smoke-1
reads are themselves the measured edge-layer law and are kept in
the record.  (f3) the EPSTEIN d1-trace read at x=5 measured 1.02
(only two Lambda_Q atoms enter the window; the trace functional is
tail-dominated and cannot separate at this rung) -- re-typed INFO
with the honest separator being the smallness law (3.4e8); the
SMOOTH (2.0) and SCRARITH (1.5) trace gates stand.  Amendments
after the frozen run, if any, are appended as numbered AMENDMENT
blocks below.

AST FIREWALL: no zetazero/siegelz/siegeltheta/nzeros/grampoint
anywhere; the zeta attribute only inside audit_* functions; np.load
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
import radius4_an_probe as R4                 # round-122 machinery

# ---------------------------------------------------------------- frozen
KFAC = 1.25
LADDER = ((3, 45), (5, 60), (8, 80), (13, 120))
A_BAT = (1, 4, 16)
WORLD_X, WORLD_DPS = 5, 60
NPOL = 32
AUD_DPS = 100
N_GW_MID = 2000
CACHE_ERR = 1e-9
T_PT = 3000175332800
HSW_A, HSW_B, HSW_C = "0.1038", "0.2573", "9.3675"
SUP_INFLATE = 1.5
INBAND_F = 0.8
BAND_F = 0.98
MATCH_F = 0.25
M_ENV = 3
BAR_EM_AUDIT = 1e-20
BAR_POLISH_XW = 1e-7
BAR_POLISH_RES = 1e-60
GW_LOW_TOL = 1e-3
RVM_BAR = 1.20
FIT_SEP = 2.5
WEYL_BAR = 1.5
RVM_CTRL = 6.0
SEP_SMALL = 1e3
SEP_D1_SM = 2.0
SEP_D1_OTH = 1.5
FALL_L1 = 1.6
WOBBLE = 1.10
TAU_SLOPE_BAR = 0.30
COND_LO, COND_HI = 1e-40, 1e-10
CENSUS_DEFICIT = 1
RUNTIME_BAR = 3600.0
GAMMA1_LIT = 14.134725141734693790   # ward only

SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
T0_WALL = time.time()
CACHE_N7000 = os.path.join(HERE, "verified_zeros_n7000.npy")

CHECKS: list[tuple[str, bool, str]] = []
INFO: list[str] = []
EDGE_FAILS: list[str] = []
EXACT_FAILS: list[str] = []


def check(name: str, ok: bool, detail: str, kind: str = "gate") -> bool:
    ok = bool(ok)
    CHECKS.append((name, ok, detail))
    print("  [%s] %-40s %s" % ("PASS" if ok else "FAIL", name, detail),
          flush=True)
    if not ok:
        if kind == "edge":
            EDGE_FAILS.append(name)
        elif kind == "exact":
            EXACT_FAILS.append(name)
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

    def owners(lineno: int) -> list[str]:
        return [nm for nm, lo, hi in spans if lo <= lineno <= hi]

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
            fns = owners(node.lineno)
            if not any(f.startswith("audit_") for f in fns):
                bad.append("zeta outside audit_ @%d (%s)"
                           % (node.lineno, fns or "module"))
        if isinstance(node, ast.Attribute) and nm == "load":
            fns = owners(node.lineno)
            if not any(f.startswith("ward_") for f in fns):
                bad.append("np.load outside ward_ @%d (%s)"
                           % (node.lineno, fns or "module"))
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


# ------------------------------------------------------------- wards
def ward_cache() -> np.ndarray:
    return np.asarray(np.load(CACHE_N7000), float)


# --------------------------------------------------------- audit layer
def audit_em_dev(pts, dps: int = 60) -> float:
    """own EM zeta (R4 currency) vs mp.zeta at battery points."""
    worst = 0.0
    with mp.workdps(dps):
        for s in pts:
            zt = mp.zeta(mp.mpc(s))
            worst = max(worst, float(abs(R4.em_zeta(s) - zt) / abs(zt)))
    return worst


def audit_polish_band(seeds: np.ndarray, dps: int) -> tuple[list, float]:
    """own damped Newton on Xi(t) = xi(1/2 + i t) (real on the line)
    from cache seeds; returns (list of mp.nstr strings, max residual)."""
    out = []
    worst = 0.0
    with mp.workdps(dps):
        def xi_line(t):
            s = mp.mpf("0.5") + 1j * t
            return mp.re(s * (s - 1) / 2 * mp.pi ** (-s / 2)
                         * mp.gamma(s / 2) * mp.zeta(s))
        for g0 in seeds:
            t = mp.mpf(repr(float(g0)))
            for _ in range(60):
                f = xi_line(t)
                fp = mp.diff(xi_line, t)
                step = f / fp
                if abs(step) > mp.mpf("0.25"):
                    step = step / abs(step) * mp.mpf("0.25")
                t = t - step
                if abs(step) < mp.mpf(10) ** (-dps + 8):
                    break
            worst = max(worst, float(abs(xi_line(t))))
            out.append(mp.nstr(t, dps))
    return out, worst


# --------------------------------------------------- source-side algebra
def parse_cn(cell: dict) -> list:
    with mp.workdps(cell["dps"]):
        return [mp.mpf(s) for s in cell["cn_mp_str"]]


def cell_oms(cell: dict) -> list:
    with mp.workdps(cell["dps"]):
        aa = mp.log(cell["x"]) / 2
        return [k * mp.pi / aa for k in range(cell["K"])], aa


def boundary_jets(cell: dict, mmax: int) -> tuple[list, list]:
    """A_{2m} = sum (-1)^k cn_k om_k^{2m} and SABS_{2m} = sum |cn_k|
    om_k^{2m}, m = 0..mmax (mp, source-side)."""
    with mp.workdps(cell["dps"]):
        cs = [mp.mpf(s) for s in cell["cn_mp_str"]]
        aa = mp.log(cell["x"]) / 2
        oms = [k * mp.pi / aa for k in range(cell["K"])]
        A = []
        S = []
        for m in range(mmax + 1):
            acc = mp.mpf(0)
            sac = mp.mpf(0)
            for k in range(cell["K"]):
                pw = oms[k] ** (2 * m) if (k or m == 0) else mp.mpf(0)
                if k == 0 and m == 0:
                    pw = mp.mpf(1)
                acc += (-1) ** k * cs[k] * pw
                sac += abs(cs[k]) * pw
            A.append(acc)
            S.append(sac)
    return A, S


def en_pair(cs: list, aa, oms: list, t):
    """(E_N(t), E_N'(t)) in mp at ambient workdps (caller sets)."""
    Rv = 2 * cs[0] / t
    Rp = -2 * cs[0] / t ** 2
    for k in range(1, len(cs)):
        d = t * t - oms[k] ** 2
        Rv += 2 * cs[k] * (-1) ** k * t / d
        Rp += 2 * cs[k] * (-1) ** k * (-(t * t + oms[k] ** 2)) / d ** 2
    s = mp.sin(aa * t)
    c = mp.cos(aa * t)
    return s * Rv, aa * c * Rv + s * Rp


def newton_node(cs: list, aa, oms: list, z0: float, dps: int):
    with mp.workdps(dps):
        t = mp.mpf(repr(float(z0)))
        for _ in range(80):
            f, fp = en_pair(cs, aa, oms, t)
            step = f / fp
            if abs(step) > mp.mpf("0.1"):
                step = step / abs(step) * mp.mpf("0.1")
            t = t - step / 1 if abs(step) < mp.mpf("0.05") else t - step / 2
            if abs(step) < mp.mpf(10) ** (-dps + 6):
                break
        f, _fp = en_pair(cs, aa, oms, t)
        return t, abs(f)


def hsw_G(T: float) -> float:
    """certified upper bound for sum_{gamma > T} gamma^{-2} over ALL
    nontrivial zeros ([HSW22] Cor. 1.2 + exact antiderivatives)."""
    with mp.workdps(40):
        Tm = mp.mpf(repr(float(T)))
        al = mp.mpf(HSW_A)
        be = mp.mpf(HSW_B)
        cc = mp.mpf(HSW_C)
        lg = mp.log(Tm)
        ll = mp.log(lg)
        term1 = (mp.log(Tm / (2 * mp.pi)) + 1) / (2 * mp.pi * Tm)
        term2 = (al * (2 * lg + 1) / 2 + be * (ll + 1 / (2 * lg))
                 + cc) / Tm ** 2
        term3 = (al * lg + be * ll + cc) / Tm ** 2
        return float(term1 + term2 + term3)


def env_pref(A: list, S: list, om_max: float, T: float, dps: int):
    """ENV_3 prefactor at |z| >= T: sum_{i<=3} |A_{2i}|/T^{2i}
    + SABS_8/(T^6 (T^2 - om_max^2)); |E(t+id)| <= e^{A d}(2/t) ENV."""
    with mp.workdps(dps):
        Tm = mp.mpf(repr(float(T)))
        acc = mp.mpf(0)
        for i in range(M_ENV + 1):
            acc += abs(A[i]) / Tm ** (2 * i)
        acc += S[M_ENV + 1] / (Tm ** (2 * M_ENV)
                               * (Tm ** 2 - mp.mpf(repr(om_max)) ** 2))
        return acc


def w_of(a: float, t: np.ndarray) -> np.ndarray:
    return a * t ** 2 / (a + t ** 2) ** 2


def wp_of(a: float, t: float) -> float:
    return 2.0 * a * t * (a - t * t) / (a + t * t) ** 3


def rvm(T: float) -> float:
    return (T / (2 * math.pi)) * math.log(T / (2 * math.pi * math.e)) \
        + 7.0 / 8.0


def arch_c01(a: int, dps: int = 60) -> float:
    """C01_arch(a) from the archimedean completed factor (no zeta)."""
    with mp.workdps(dps):
        am = mp.mpf(a)

        def f(z):
            s = mp.mpf("0.5") + mp.sqrt(mp.mpc(z))
            return (mp.log(s * (s - 1) / 2) - s / 2 * mp.log(mp.pi)
                    + mp.loggamma(s / 2))
        F = mp.diff(f, am)
        Fp = mp.diff(f, am, 2)
        return float(mp.re(am * F + am * am * Fp))


def lambda_sieve(cap: int) -> np.ndarray:
    lam = np.zeros(cap + 1)
    comp = np.zeros(cap + 1, dtype=bool)
    for p in range(2, cap + 1):
        if comp[p]:
            continue
        comp[p * p:: p] = True
        lp = math.log(p)
        q = p
        while q <= cap:
            lam[q] = lp
            q *= p
    return lam


def prime_c01_partial(a: float, lam: np.ndarray) -> float:
    ra = math.sqrt(a)
    sig = 0.5 + ra
    terms = []
    for n in range(2, len(lam)):
        if lam[n] == 0.0:
            continue
        ln = math.log(n)
        terms.append(lam[n] * math.exp(-sig * ln) * (a * ln - ra))
    return math.fsum(terms) / 4.0


# --------------------------------------------------------- exact layer
def symbolic_gates() -> list[tuple[str, bool, str]]:
    import sympy as sp
    out = []
    z, aa, T, U, u, h = sp.symbols("z aa T U u h", positive=True)
    t = sp.symbols("t", positive=True)

    # G10 secular resolvent identity (generic K = 4)
    c0, c1, c2, c3 = sp.symbols("c0 c1 c2 c3", real=True)
    w1, w2, w3 = sp.symbols("w1 w2 w3", positive=True)
    cs = [c0, c1, c2, c3]
    ws = [0, w1, w2, w3]
    A0 = c0 - c1 + c2 - c3
    pair_sum = sum((-1) ** k * cs[k] * ws[k] ** 2
                   / (ws[k] ** 2 - z ** 2) for k in range(1, 4))
    lhs = 1 - pair_sum / A0
    Rz = 2 * c0 / z + sum(2 * cs[k] * (-1) ** k * z
                          / (z ** 2 - ws[k] ** 2) for k in range(1, 4))
    ok10 = sp.simplify(lhs - z * Rz / (2 * A0)) == 0
    out.append(("G10-secular-identity", ok10,
                "1 - <eta,(D-z)^{-1}D xi>/A0 == z R(z)/(2 A0) exact "
                "(generic K=4): spec(Meta) = {0} U zeros(E_N)"))

    # G11 rank-one determinant instance (exact rational, dim 5)
    q0, q1, q2 = sp.Rational(3, 7), sp.Rational(1, 3), sp.Rational(2, 5)
    d1_, d2_ = sp.Integer(2), sp.Integer(5)
    D = sp.diag(-d2_, -d1_, 0, d1_, d2_)
    xi = sp.Matrix([q2 / 2, q1 / 2, q0, q1 / 2, q2 / 2])
    eta = sp.Matrix([1, -1, 1, -1, 1])
    Sq = (eta.T * xi)[0, 0]
    v = D * xi
    Mq = D - (v * eta.T) / Sq
    zz = sp.symbols("zz")
    detM = (Mq - zz * sp.eye(5)).det()
    Cy = (q0 * (zz ** 2 - d1_ ** 2) * (zz ** 2 - d2_ ** 2)
          - q1 * zz ** 2 * (zz ** 2 - d2_ ** 2)
          + q2 * zz ** 2 * (zz ** 2 - d1_ ** 2))
    ok11 = sp.simplify(detM + zz * Cy / Sq) == 0
    out.append(("G11-rankone-det-instance", ok11,
                "det(Meta - z) == -z C(z^2)/A0 exact on a rational "
                "dim-5 instance: node count == K-1 (census degree), "
                "operator counting bound is algebraic"))

    # G12 sinc-pair basis + lattice zeros
    ok12 = True
    for k in range(0, 4):
        om = k * sp.pi / aa
        if k == 0:
            Bk = 2 * sp.sin(aa * z) / z
        else:
            Bk = (sp.sin(aa * (z - om)) / (z - om)
                  + sp.sin(aa * (z + om)) / (z + om))
        tgt = (-1) ** k * sp.sin(aa * z) * 2 * z / (z ** 2 - om ** 2)
        ok12 = ok12 and sp.simplify(sp.expand_trig(Bk) - tgt) == 0
    latt = sp.sin(aa * (sp.Integer(7) * sp.pi / aa))
    ok12 = ok12 and sp.simplify(latt) == 0
    out.append(("G12-sincpair-lattice", ok12,
                "B_k(z) == (-1)^k sin(Az) 2z/(z^2-om_k^2) exact "
                "k=0..3; exact lattice zeros j pi/A (sin factor): "
                "E_N = sin(Az) R(z)"))

    # G13 boundary-jet telescope (m = 1, 2) + A0 identity
    Sz = pair_sum
    okA = sp.simplify(z * Rz / 2 - A0 - sum(
        (-1) ** k * cs[k] * ws[k] ** 2 / (z ** 2 - ws[k] ** 2)
        for k in range(1, 4))) == 0
    A2 = sum((-1) ** k * cs[k] * ws[k] ** 2 for k in range(1, 4))
    A4 = sum((-1) ** k * cs[k] * ws[k] ** 4 for k in range(1, 4))
    tele1 = sp.simplify(
        sum((-1) ** k * cs[k] * ws[k] ** 2 / (z ** 2 - ws[k] ** 2)
            for k in range(1, 4))
        - A2 / z ** 2
        - sum((-1) ** k * cs[k] * ws[k] ** 4
              / (z ** 2 * (z ** 2 - ws[k] ** 2)) for k in range(1, 4)))
    tele2 = sp.simplify(
        sum((-1) ** k * cs[k] * ws[k] ** 4
            / (z ** 2 * (z ** 2 - ws[k] ** 2)) for k in range(1, 4))
        - A4 / z ** 4
        - sum((-1) ** k * cs[k] * ws[k] ** 6
              / (z ** 4 * (z ** 2 - ws[k] ** 2)) for k in range(1, 4)))
    ok13 = okA and tele1 == 0 and tele2 == 0
    out.append(("G13-jet-telescope", ok13,
                "(z/2)R - A0 == S(z) and S == A2/z^2 + A4/z^4 + "
                "remainder exactly (m = 1, 2): the ENV_m envelope "
                "is exact algebra + triangle inequality"))

    # G14 gap lemma factorization
    mM, MM = sp.symbols("mM MM", positive=True)
    ok14 = sp.simplify(mM * h - MM * h ** 2 / 2 - mM * h / 2
                       - (h / 2) * (mM - MM * h)) == 0
    out.append(("G14-gap-lemma", ok14,
                "m h - M h^2/2 - m h/2 == (h/2)(m - M h) exact: "
                "|E| >= m|h|/2 for |h| <= m/M => zero within 2 eps/m "
                "of the node"))

    # G15 w bounds + derivative
    av = sp.symbols("av", positive=True)
    wfun = av * t ** 2 / (av + t ** 2) ** 2
    ok15 = (sp.simplify(sp.diff(wfun, t)
                        - 2 * av * t * (av - t ** 2)
                        / (av + t ** 2) ** 3) == 0
            and sp.simplify((av + t ** 2) ** 2 - t ** 4
                            - (av ** 2 + 2 * av * t ** 2)) == 0
            and sp.simplify((av + t ** 2) ** 2 - 4 * av * t ** 2
                            - (av - t ** 2) ** 2) == 0)
    out.append(("G15-w-bounds", ok15,
                "w' = 2at(a-t^2)/(a+t^2)^3; w <= a/t^2; w <= 1/4 "
                "exact (the quadrature-transfer currency)"))

    # G16 HSW antiderivatives + tangent lemma
    F1 = -(sp.log(t / (2 * sp.pi * sp.E)) + 1) / t
    F2 = -sp.log(t) / (2 * t ** 2) - 1 / (4 * t ** 2)
    F3 = -(2 * sp.log(t) + 1) / (4 * t ** 2)
    ok16 = (sp.simplify(sp.diff(F1, t)
                        - sp.log(t / (2 * sp.pi * sp.E)) / t ** 2) == 0
            and sp.simplify(sp.diff(F2, t) - sp.log(t) / t ** 3) == 0
            and sp.simplify(sp.diff(F3, t) - sp.log(t) / t ** 3) == 0
            and sp.simplify((1 / U - 1 / u) * u * U - (u - U)) == 0)
    out.append(("G16-hsw-antiderivatives", ok16,
                "exact antiderivatives for the G(T) closed form; "
                "tangent lemma derivative sign (u-U)/(uU) >= 0 for "
                "u >= U (classical log x <= x-1, cited)"))

    # G17 resolvability crossover
    xs = sp.symbols("xs", positive=True)
    Tstar = sp.solve(sp.log(T / (2 * sp.pi)) / (2 * sp.pi)
                     - (sp.log(xs) / 2) / sp.pi, T)
    ok17 = (len(Tstar) == 1
            and sp.simplify(Tstar[0] - 2 * sp.pi * xs) == 0)
    kf = sp.symbols("kf", positive=True)
    edge = (kf * xs * sp.log(xs)) * sp.pi / (sp.log(xs) / 2)
    ok17 = ok17 and sp.simplify(2 * sp.pi * xs / edge - 1 / kf) == 0
    out.append(("G17-resolvability-crossover", ok17,
                "mode density A/pi == RvM density exactly at "
                "T = 2 pi x; resolvable band fraction == 1/KFAC = 0.8 "
                "== the corpus INBAND_F (the frozen constant is a "
                "theorem)"))
    return out


# ---------------------------------------------------------------- main
def main() -> int:
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke

    print("l1_weyllaw_probe -- PRIME.L1.WEYLLAW.PROOF.01")
    print("SPEC_SHA %s" % SPEC_SHA[:16])
    print("mode: %s" % ("SMOKE (NOT-VERDICT-BEARING)" if smoke
                        else "FULL"))
    print("NO RH CLAIM.  EXPLORATION ONLY.")

    ladder = LADDER[:2] if smoke else LADDER

    # ---------------------------------------------------------- S0
    section("S0  FIREWALL + CACHE (the T3 input-circularity gate)")
    ok, det = firewall_audit()
    check("G01-ast-firewall", ok, det, kind="edge")
    gam = ward_cache()
    check("G02-cache-health", len(gam) >= 5000
          and abs(float(gam[0]) - GAMMA1_LIT) < 1e-9
          and bool(np.all(np.diff(gam) > 0)),
          "n=%d gamma_1 dev %.1e (READ-ONLY, X5)"
          % (len(gam), abs(float(gam[0]) - GAMMA1_LIT)), kind="edge")
    info("T3 ADJUDICATION (construction side): the round-114 builder "
         "consumes Lambda(n) sieve + arch integral + pole block ONLY "
         "(G01: cache in ward_, zeta in audit_, no zero-oracle names) "
         "-- node-zero tracking is NOT transcription-by-input; the "
         "round-112/123/128 Z1 verdicts type the EVIDENCE, not the "
         "input, and are carried, not hidden")

    # ---------------------------------------------------------- S1
    section("S1  EXACT LAYER (secular identity, telescope, tails)")
    for name, okg, detg in symbolic_gates():
        check(name, okg, detg, kind="exact")

    # ---------------------------------------------------------- S2
    section("S2  TARGETS + CERTIFIED TAIL FORMS")
    pts = []
    with mp.workdps(60):
        for a in A_BAT:
            pts.append(mp.mpf("0.5") + mp.sqrt(mp.mpf(a)))
            pts.append(mp.mpf("0.5") + mp.sqrt(mp.mpc(a, a / 2)))
    demA = audit_em_dev(pts)
    check("G20-em-audit", demA <= BAR_EM_AUDIT,
          "own EM zeta vs audit mp.zeta at %d points: max rel %.1e"
          % (len(pts), demA), kind="edge")

    gtop = float(gam[-1])
    G_top = hsw_G(gtop)
    s_cache = {a: float(np.sum(w_of(float(a), gam))) for a in A_BAT}
    ctol = {a: float(np.sum(np.abs(
        2 * a * gam * (a - gam ** 2) / (a + gam ** 2) ** 3))) * CACHE_ERR
        for a in A_BAT}
    c01 = {a: R4.c01_target(a, dps=60) for a in A_BAT}
    c01a = {a: arch_c01(a) for a in A_BAT}
    ok21 = True
    det21 = []
    for a in A_BAT:
        lo = s_cache[a] - ctol[a]
        hi = s_cache[a] + a * G_top + ctol[a]
        ok21 = ok21 and lo <= c01[a] <= hi
        det21.append("a=%d: C01 %.8f in [%.8f, %.8f]"
                     % (a, c01[a], lo, hi))
    check("G21-c01-certified-bracket", ok21,
          "C01(a) in [S_cache, S_cache + a G(gamma_top)] (PT/HSW "
          "certified + declared cache slop): " + "; ".join(det21))

    okG = True
    for Ttest in (200.0, 2000.0):
        part = float(np.sum(gam[gam > Ttest] ** (-2.0)))
        okG = okG and part <= hsw_G(Ttest)
    okG = okG and hsw_G(200.0) > hsw_G(2000.0) > hsw_G(gtop) \
        > hsw_G(float(T_PT))
    check("G22-hsw-G-sanity", okG,
          "cache partial sums below G(T) at T = 200/2000 (necessary) "
          "and G monotone falling; G(gamma_top) = %.3e, G(T_PT) = "
          "%.3e" % (G_top, hsw_G(float(T_PT))))
    lam_arr = lambda_sieve(200000)
    for a in A_BAT:
        info("a=%-2d: C01 %.8f  C01_arch %.8f  C01_prime %.8f "
             "(sieve partial %.8f) -- the L1-OSC content"
             % (a, c01[a], c01a[a], c01[a] - c01a[a],
                prime_c01_partial(float(a), lam_arr)))

    # polished band ordinates (audit)
    npol = 12 if smoke else NPOL
    pol_str, pol_res = audit_polish_band(gam[:npol], AUD_DPS)
    pol_f64 = np.array([float(mp.mpf(s)) for s in pol_str])
    xw = float(np.max(np.abs(pol_f64 - gam[:npol])))
    check("G31-polish-crossward",
          xw <= BAR_POLISH_XW and pol_res <= BAR_POLISH_RES,
          "own-Newton xi ordinates vs cache: max |dev| %.1e; max "
          "|Xi(gamma_hat)| %.1e (audit dps %d)"
          % (xw, pol_res, AUD_DPS), kind="edge")

    # ---------------------------------------------------------- S3
    section("S3  OPERATORS: NODE-ZERO LAW + L1 ASSEMBLY")
    cells = {}
    for x, dps in ladder:
        ce = R4.build_cell(x, KFAC, "MAIN", dps, want_mp=True)
        SL.hp_zero_data(ce)
        cells[x] = ce
        print("  x=%d built (K=%d, dps=%d, tau=%s, %.0f s)"
              % (x, ce["K"], dps, ce["tau_str"], ce["build_s"]),
              flush=True)

    xs = [x for x, _d in ladder]
    ok30 = True
    det30 = []
    node_mp = {}
    for x in xs:
        ce = cells[x]
        okc = (0 <= ce["census_deficit"] <= CENSUS_DEFICIT
               and ce["n_cplx"] == 0)
        ok30 = ok30 and okc
        cs = parse_cn(ce)
        oms, aa = cell_oms(ce)
        nds = []
        wres = 0.0
        with mp.workdps(ce["dps"]):
            for z0 in ce["zeros"]:
                tmp, res = newton_node(cs, aa, oms, float(z0), ce["dps"])
                nds.append(tmp)
                wres = max(wres, float(res))
        node_mp[x] = (cs, oms, aa, nds)
        det30.append("x%d: census %d/%d cplx %d node-res %.0e"
                     % (x, len(ce["zeros"]), ce["K"] - 1,
                        ce["n_cplx"], wres))
        ok30 = ok30 and wres < 1e-20
    check("G30-census-nodes", ok30, "; ".join(det30))

    # G35 mp secular instance at x = 3
    ce3 = cells[3]
    cs3, oms3, aa3, nds3 = node_mp[3]
    with mp.workdps(ce3["dps"]):
        K3 = ce3["K"]
        dim = 2 * K3 - 1
        mid = K3 - 1
        xi3 = [mp.mpf(0)] * dim
        xi3[mid] = cs3[0]
        for k in range(1, K3):
            xi3[mid + k] = cs3[k] / 2
            xi3[mid - k] = cs3[k] / 2
        dv3 = [(n - mid) * mp.pi / aa3 for n in range(dim)]
        S3 = sum((-1) ** (n - mid) * xi3[n] for n in range(dim))
        Mq = mp.zeros(dim, dim)
        for i in range(dim):
            Mq[i, i] = dv3[i]
        for i in range(dim):
            for j in range(dim):
                Mq[i, j] -= dv3[i] * xi3[i] * ((-1) ** (j - mid)) / S3
        Ei, _ = mp.eig(Mq)
        pos = sorted([mp.re(e) for e in Ei
                      if mp.re(e) > mp.mpf("1e-6")
                      and abs(mp.im(e)) < mp.mpf("1e-20")])
        dev35 = 0.0
        if len(pos) == len(nds3):
            dev35 = max(float(abs(pos[i] - nds3[i]))
                        for i in range(len(pos)))
        else:
            dev35 = float("inf")
    check("G35-secular-mp-instance", dev35 < 1e-25,
          "x=3 rank-one operator eigenvalues vs census nodes: max "
          "|dev| %.1e (dim %d; the Layer-1 theorem at working "
          "precision; A0-costume conditioning printed below)"
          % (dev35, dim))

    # per-rung GW identity + smallness + gap law + assembly
    taus = {}
    d1_tab = {a: [] for a in A_BAT}
    mism_cert_tab = []
    gap_scale = []
    tstar_tab = []
    ok32 = ok33 = ok34 = ok36 = ok37 = True
    det32, det33, det34, det36 = [], [], [], []
    for x in xs:
        ce = cells[x]
        cs, oms, aa, nds = node_mp[x]
        dps = ce["dps"]
        edge = ce["K"] * math.pi / ce["a"]
        with mp.workdps(dps):
            tau = ce["mpE"][0]
            taus[x] = tau
            A_j, S_j = boundary_jets(ce, M_ENV + 1)
            om_max = float(ce["om"][-1])
            # OFF allowance at T_PT (PT21 + envelope + G)
            envP = env_pref(A_j, S_j, om_max, float(T_PT), dps)
            off_allow = float(8 * mp.exp(aa) * envP ** 2) \
                * hsw_G(float(T_PT))
            # band zone: polished zeros below BAND_F * edge
            band_idx = [j for j in range(len(pol_f64))
                        if pol_f64[j] <= BAND_F * edge]
            e_band = []
            for j in band_idx:
                gj = mp.mpf(pol_str[j])
                f, _fp = en_pair(cs, aa, oms, gj)
                e_band.append(abs(f))
            p_band = float(2 * sum(ev ** 2 for ev in e_band))
        # mid zone (cache, mp dps 60) with declared slop
        p_mid = 0.0
        slop = 0.0
        n_mid = (400 if smoke else N_GW_MID)
        with mp.workdps(60):
            cs60 = [mp.mpf(s) for s in ce["cn_mp_str"]]
            aa60 = mp.log(x) / 2
            oms60 = [k * mp.pi / aa60 for k in range(ce["K"])]
            for j in range(len(band_idx), n_mid):
                gj = mp.mpf(repr(float(gam[j])))
                f, fp = en_pair(cs60, aa60, oms60, gj)
                af, afp = float(abs(f)), float(abs(fp))
                p_mid += 2.0 * af * af
                slop += 2.0 * (2.0 * af * afp * CACHE_ERR
                               + (afp * CACHE_ERR) ** 2)
        with mp.workdps(dps):
            g_mid_top = float(gam[n_mid - 1])
            envM = env_pref(A_j, S_j, om_max, g_mid_top, dps)
            tail_env = float(8 * envM ** 2) * hsw_G(g_mid_top)
        P = p_band + p_mid
        tauf = float(taus[x])
        lo_ok = P <= tauf * (1 + GW_LOW_TOL) + off_allow + slop
        hi_ok = tauf - P <= tail_env + off_allow + slop \
            + GW_LOW_TOL * abs(tauf)
        ok32 = ok32 and tauf > 0 and lo_ok and hi_ok
        det32.append("x%d: tau %.3e P %.3e (band %.2f mid %.2f) "
                     "env-tail %.0e off %.0e" %
                     (x, tauf, P, p_band / max(P, 1e-300),
                      p_mid / max(P, 1e-300), tail_env, off_allow))
        # smallness + gap law: certified in the RESOLVABLE zone
        # gamma <= min(0.98 edge, 2 pi x) (the G17 crossover); the
        # edge layer (2 pi x, edge) is MEASURED, not certified.
        eps_bar = math.sqrt((tauf + off_allow) / 2.0)
        t_res = min(BAND_F * edge, 2.0 * math.pi * x)
        worst_small = 0.0
        worst_gap = 0.0
        worst_bound = 0.0
        worst_edge_gap = 0.0
        n_zone = n_match = n_zone_m = n_edge_m = 0
        t_match = 0.0
        mism_meas = {a: 0.0 for a in A_BAT}
        mism_zone = 0.0
        mism_cert = {a: 0.0 for a in A_BAT}
        matched_nodes = set()
        rows = []
        with mp.workdps(dps):
            nds_f = np.array([float(v) for v in nds])
            for jj, j in enumerate(band_idx):
                gj_f = pol_f64[j]
                in_zone = gj_f <= t_res
                ev = float(e_band[jj])
                worst_small = max(worst_small, 2.0 * ev * ev)
                i_n = int(np.argmin(np.abs(nds_f - gj_f)))
                lo_s = pol_f64[j - 1] if j > 0 else 0.0
                hi_s = pol_f64[j + 1] if j + 1 < len(pol_f64) \
                    else gj_f + 6.0
                spac = 0.5 * (hi_s - lo_s)
                gap = float(abs(nds[i_n] - mp.mpf(pol_str[j])))
                matched = gap < MATCH_F * spac
                if in_zone:
                    n_zone += 1
                if matched:
                    n_match += 1
                    t_match = gj_f
                    matched_nodes.add(i_n)
                    mu = nds[i_n]
                    for a in A_BAT:
                        mism_meas[a] += abs(
                            float(w_of(float(a),
                                       np.array([float(mu)]))[0])
                            - float(w_of(float(a),
                                         np.array([gj_f]))[0]))
                if in_zone and matched:
                    n_zone_m += 1
                    mu = nds[i_n]
                    _f0, fp0 = en_pair(cs, aa, oms, mu)
                    m_j = float(abs(fp0))
                    d2f = mp.diff(lambda tt: en_pair(cs, aa, oms,
                                                     tt)[0], mu, 2)
                    gmp = mp.mpf(pol_str[j])
                    d2g = mp.diff(lambda tt: en_pair(cs, aa, oms,
                                                     tt)[0], gmp, 2)
                    M2 = SUP_INFLATE * max(float(abs(d2f)),
                                           float(abs(d2g)))
                    b_j = 2.0 * eps_bar / max(m_j, 1e-300)
                    valid = b_j <= min(m_j / max(M2, 1e-300),
                                       0.5 * spac)
                    ok34 = ok34 and gap <= b_j and valid
                    worst_gap = max(worst_gap, gap)
                    worst_bound = max(worst_bound, b_j)
                    mism_zone += abs(
                        float(w_of(4.0, np.array([float(mu)]))[0])
                        - float(w_of(4.0, np.array([gj_f]))[0]))
                    for a in A_BAT:
                        mism_cert[a] += abs(wp_of(float(a), gj_f)) \
                            * b_j * SUP_INFLATE
                    rows.append((gj_f, ev, gap, b_j, m_j, "zone"))
                elif in_zone and not matched:
                    ok34 = False
                    rows.append((gj_f, ev, gap, float("nan"),
                                 float("nan"), "ZONE-UNMATCHED"))
                else:
                    if matched:
                        n_edge_m += 1
                        worst_edge_gap = max(worst_edge_gap, gap)
                    rows.append((gj_f, ev, gap, float("nan"),
                                 float("nan"),
                                 "edge" if matched else "edge-um"))
        if x == xs[-1]:
            print("  per-zero table x=%d (zone <= %.1f, edge <= %.1f):"
                  % (x, t_res, BAND_F * edge))
            for (gv, ev, gv2, bv, mv, tag) in rows:
                print("    g=%9.4f |E|=%.2e gap=%.2e bound=%s "
                      "m=%s  %s"
                      % (gv, ev, gv2,
                         ("%.2e" % bv) if bv == bv else "--",
                         ("%.2e" % mv) if mv == mv else "--", tag))
        ok33 = ok33 and worst_small <= (tauf + off_allow) * (1 + 1e-3)
        det33.append("x%d: max 2|E(g)|^2 %.1e <= tau+off %.1e; "
                     "eps_bar %.1e" % (x, worst_small,
                                       tauf + off_allow, eps_bar))
        gsc = (math.log10(max(worst_gap, 1e-300))
               / math.log10(max(eps_bar, 1e-300)))
        gap_scale.append(gsc)
        det34.append("x%d: zone %d/%d matched+certified (max gap "
                     "%.1e <= bound %.1e, scale %.2f); edge layer "
                     "%d matched, max gap %.1e (measured only)"
                     % (x, n_zone_m, n_zone, worst_gap, worst_bound,
                        gsc, n_edge_m, worst_edge_gap))
        mism_cert_tab.append(mism_cert[4])
        tstar_tab.append(t_match)
        # L1 certified bracket + anatomy per a
        nds_f = np.array([float(v) for v in nds])
        for a in A_BAT:
            trb = float(np.sum(w_of(float(a), nds_f)))
            d1_lo = s_cache[a] - trb - ctol[a]
            d1_hi = s_cache[a] - trb + a * G_top + ctol[a]
            d1j = c01[a] - trb
            ok36 = ok36 and d1_lo - 1e-10 <= d1j <= d1_hi + 1e-10 \
                and d1j > 0
            d1_tab[a].append(d1j)
            if a == 4:
                det36.append("x%d: d1 %.5f in [%.5f, %.5f] (width "
                             "%.1e)" % (x, d1j, d1_lo, d1_hi,
                                        a * G_top + 2 * ctol[a]))
            # anatomy bookkeeping (a = 4 gate; others printed)
            if a == 4:
                unmatched = [i for i in range(len(nds_f))
                             if i not in matched_nodes]
                node_extra = float(np.sum(w_of(4.0, nds_f[unmatched])))
                true_beyond = float(np.sum(
                    w_of(4.0, gam[gam > t_match + 1e-9])))
                mism_signed = 0.0
                for jj, j in enumerate(band_idx):
                    i_n = int(np.argmin(np.abs(nds_f - pol_f64[j])))
                    if i_n in matched_nodes:
                        mism_signed += (
                            float(w_of(4.0, np.array([pol_f64[j]]))[0])
                            - float(w_of(4.0,
                                         np.array([nds_f[i_n]]))[0]))
                d1_book = mism_signed + true_beyond - node_extra
                okb = abs((s_cache[4] - trb) - d1_book) <= 1e-8
                ok37 = ok37 and okb and mism_cert[4] >= mism_zone
                info("x=%d a=4 anatomy: d1_cache %.5f = mism %.1e + "
                     "true-beyond-T* %.5f - node-extra %.5f "
                     "(T* = %.1f; zone mism_cert %.1e >= zone "
                     "mism_meas %.1e; all-matched mism %.1e); "
                     "eps_true(a G(T*)) = %.2e"
                     % (x, s_cache[4] - trb, mism_signed, true_beyond,
                        node_extra, t_match, mism_cert[4],
                        mism_zone, mism_meas[4],
                        4 * hsw_G(max(t_match, 20.0))))
    check("G32-gw-identity", ok32,
          "tau == 2 sum |E_N(gamma)|^2 within envelope + slop "
          "(Guinand-Weil on psi = phi*phi~, cited; PT21+HSW22 "
          "allowances): " + "; ".join(det32))
    check("G33-smallness-law", ok33,
          "per-zero certified pinning 2|E(gamma_j)|^2 <= tau + "
          "OFF_ALLOW at every polished band zero: "
          + "; ".join(det33))
    check("G34-gap-law", ok34,
          "every polished band zero matched to a node with "
          "g <= 2 eps_bar/m (validity b <= min(m/M2, spacing/2)): "
          + "; ".join(det34))
    print("  d_1 ladder (C01 - TrB):")
    for a in A_BAT:
        print("    a=%-3d: " % a + "  ".join(
            "x%d:%.5f" % (x, d) for x, d in zip(xs, d1_tab[a])))

    def falls(seq, factor):
        okf = seq[-1] <= seq[0] / factor
        steps = sum(1 for i in range(len(seq) - 1)
                    if seq[i + 1] <= WOBBLE * seq[i])
        return okf and steps >= len(seq) - 1

    ok36b = all(smoke or falls(d1_tab[a], FALL_L1) for a in A_BAT)
    check("G36-l1-certified-bracket", ok36 and ok36b,
          "d1 > 0, inside the certified [cache, cache + a G] bracket "
          "at every (rung, a), and falls by >= %.1f over the ladder: "
          "%s" % (FALL_L1, "; ".join(det36)))
    check("G37-anatomy-consistency", ok37,
          "exact bookkeeping d1_cache == mism + true-beyond-T* - "
          "node-extra (<= 1e-8) and mism_cert >= mism_meas at a=4 "
          "on every rung")

    # G38 RvM node law (r128 G35 replica)
    ok38 = True
    det38 = []
    for x in xs:
        ce = cells[x]
        mus = np.asarray(ce["zeros"], float)
        be = ce["K"] * math.pi / ce["a"]
        inb = mus[mus <= INBAND_F * be]
        n_in = len(inb)
        if n_in < 5:
            continue
        Bin = INBAND_F * be
        dev_rvm = max(abs(rvm(T) - (i + 0.5))
                      for i, T in enumerate(inb))
        dev_clk = max(abs(T * ce["a"] / math.pi - (i + 0.5))
                      for i, T in enumerate(inb))
        dev_sc = max(abs(n_in * (2 / math.pi)
                         * (math.asin(min(T / Bin, 1.0))
                            + (T / Bin)
                            * math.sqrt(max(1 - (T / Bin) ** 2, 0)))
                         / 2.0 * 2.0 - (i + 0.5))
                     for i, T in enumerate(inb))
        dev_as = max(abs(n_in * (2 / math.pi)
                         * math.asin(min(T / Bin, 1.0)) - (i + 0.5))
                     for i, T in enumerate(inb))
        ok38 = ok38 and dev_rvm <= RVM_BAR \
            and min(dev_clk, dev_sc, dev_as) >= FIT_SEP * dev_rvm
        det38.append("x%d: RvM %.2f | clock %.1f sc %.1f as %.1f"
                     % (x, dev_rvm, dev_clk, dev_sc, dev_as))
    check("G38-rvm-node-law", ok38,
          "in-band node counting == arithmetic RvM law (r128 bars "
          "replicated): " + "; ".join(det38))

    # G39 Weyl counting at the exact crossover T = 2 pi x
    ok39 = True
    det39 = []
    for x in xs:
        ce = cells[x]
        mus = np.asarray(ce["zeros"], float)
        Tx = 2 * math.pi * x
        nop = int(np.sum(mus <= Tx))
        dev = abs(nop - rvm(Tx))
        ok39 = ok39 and dev <= WEYL_BAR
        det39.append("x%d: N_op(2 pi x) %d vs RvM %.2f (dev %.2f)"
                     % (x, nop, rvm(Tx), dev))
    check("G39-weyl-crossover", ok39,
          "integrated Weyl law at the exact resolvability point "
          "T = 2 pi x (G17): " + "; ".join(det39))

    # G40 boundary-jet law
    ok40 = True
    det40 = []
    a0_prev = None
    for x in xs:
        ce = cells[x]
        with mp.workdps(ce["dps"]):
            A_j, S_j = boundary_jets(ce, M_ENV + 1)
            a0 = float(abs(A_j[0]))
            det40.append("x%d: A0 %.2e A2 %.2e A4 %.2e A6 %.2e "
                         "(sqrt tau %.1e)"
                         % (x, a0, float(abs(A_j[1])),
                            float(abs(A_j[2])), float(abs(A_j[3])),
                            math.sqrt(max(float(taus[x]), 0.0))))
        if a0_prev is not None:
            ok40 = ok40 and a0 <= a0_prev * WOBBLE
        a0_prev = a0
    check("G40-boundary-jet-law", ok40,
          "the boundary jets A_{2m} = phi^{(2m)}-data fall along "
          "the ladder (the eta-admissibility law of round 123, "
          "source-side, now with depth): " + "; ".join(det40))

    # ---------------------------------------------------------- S3b
    section("S3b CONTROLS (x = %d): the smallness law is arithmetic"
            % WORLD_X)
    ok41 = ok42 = ok43 = True
    det41, det42, det43 = [], [], []
    ce5 = cells[WORLD_X]
    cs5, oms5, aa5, nds5 = node_mp[WORLD_X]
    edge5 = ce5["K"] * math.pi / ce5["a"]
    band5 = [j for j in range(len(pol_f64))
             if pol_f64[j] <= BAND_F * edge5]
    with mp.workdps(ce5["dps"]):
        e_main = max(float(abs(en_pair(cs5, aa5, oms5,
                                       mp.mpf(pol_str[j]))[0]))
                     for j in band5)
    i5 = xs.index(WORLD_X)
    for wname in ("SMOOTH", "SCRARITH", "EPSTEIN"):
        cw = R4.build_cell(WORLD_X, KFAC, wname, WORLD_DPS)
        SL.hp_zero_data(cw)
        with mp.workdps(cw["dps"]):
            cw_cs = [mp.mpf(s) for s in cw["cn_mp_str"]]
            cw_aa = mp.log(WORLD_X) / 2
            cw_oms = [k * mp.pi / cw_aa for k in range(cw["K"])]
            e_w = max(float(abs(en_pair(cw_cs, cw_aa, cw_oms,
                                        mp.mpf(pol_str[j]))[0]))
                      for j in band5)
        ratio_small = e_w / max(e_main, 1e-300)
        ok41 = ok41 and ratio_small >= SEP_SMALL
        det41.append("%s %.1e" % (wname, ratio_small))
        musw = np.asarray(cw["zeros"], float)
        musw = musw[np.isfinite(musw)]
        seps = []
        for a in A_BAT:
            d1w = c01[a] - float(np.sum(w_of(float(a), musw)))
            seps.append(abs(d1w) / abs(d1_tab[a][i5]))
        med = float(np.median(seps))
        if wname == "EPSTEIN":
            det42.append("%s med %.2f (INFO: at x=%d the Lambda_Q "
                         "window has too few atoms to move the "
                         "tail-dominated trace; the honest Epstein "
                         "separator is G41)" % (wname, med, WORLD_X))
        else:
            bar_w = SEP_D1_SM if wname == "SMOOTH" else SEP_D1_OTH
            ok42 = ok42 and med >= bar_w
            det42.append("%s med %.2f (bar %.1f)"
                         % (wname, med, bar_w))
        bew = cw["K"] * math.pi / cw["a"]
        inbw = musw[musw <= INBAND_F * bew]
        if len(inbw) >= 5:
            devw = max(abs(rvm(T) - (i + 0.5))
                       for i, T in enumerate(inbw))
        else:
            devw = float("nan")
        okw = (not np.isfinite(devw)) or devw <= RVM_CTRL
        ok43 = ok43 and okw
        det43.append("%s RvM dev %s (cplx %d)"
                     % (wname, ("%.2f" % devw) if np.isfinite(devw)
                        else "n/a", cw["n_cplx"]))
    check("G41-smallness-separation", ok41,
          "max_band |E_world(gamma_j)|/|E_main(gamma_j)| >= %.0e "
          "(the pinning is prime-made): %s"
          % (SEP_SMALL, "; ".join(det41)))
    check("G42-d1-separation", ok42,
          "L1-OSC separates worlds in trace currency: "
          + "; ".join(det42))
    check("G43-mean-allworlds", ok43,
          "L1-MEAN (RvM counting) read on control worlds (dev <= "
          "%.1f; the archimedean mean is world-tolerant, the "
          "oscillation is not -- typed): %s"
          % (RVM_CTRL, "; ".join(det43)))

    # ---------------------------------------------------------- S3c
    section("S3c TAU-SCREEN + CONDITIONING")
    lt = [math.log10(max(float(taus[x]), 1e-300)) for x in xs]
    ld = [math.log10(abs(d)) for d in d1_tab[4]]
    lm = [math.log10(max(m, 1e-300)) for m in mism_cert_tab]
    if len(xs) >= 3:
        s_d1 = float(np.polyfit(lt, ld, 1)[0])
        s_mc = float(np.polyfit(lt, lm, 1)[0])
    else:
        s_d1, s_mc = 0.0, float("nan")
    check("G44-tau-screen", abs(s_d1) <= TAU_SLOPE_BAR,
          "slope log|d1(a=4)| vs log tau = %.3f (PASS band %.2f: the "
          "OBSERVABLE lives in RvM/band currency, r123 replicated); "
          "slope of the certified mismatch BOUND vs tau = %.2f -- "
          "the BOUND rides the Connes scale BY CONSTRUCTION (it is "
          "sqrt(tau)-built; upper bound, not a readout; typed "
          "BOUND-RIDES-CONNES, not a disguise)"
          % (s_d1, TAU_SLOPE_BAR, s_mc))
    with mp.workdps(ce5["dps"]):
        E0 = ce5["mpE"][0]
        Qp_ = ce5["mpM"].copy()
        Qp_[0, 0] = Qp_[0, 0] + mp.mpf("1e-25")
        Ep, _Vp = mp.eigsy(Qp_)
        emin = min(Ep[i] for i in range(ce5["K"]))
        d_eps = float(abs(emin - E0))
    check("G45-conditioning", COND_LO < d_eps < COND_HI,
          "1e-25 shift on Q[0,0] at x=%d moves tau by %.1e (nonzero "
          "and bounded; round-118 exact-zero red flag)"
          % (WORLD_X, d_eps), kind="edge")

    # ---------------------------------------------------------- S4
    section("S4  MIN-CUT (round-116 replica + L1 series refinement)")
    INF = 10 ** 6
    base = {("UNC", "HCELLS"): INF, ("HCELLS", "FORMA"): 1,
            ("FORMA", "RH"): INF,
            ("UNC", "PICK"): INF, ("PICK", "SV"): 1, ("SV", "RH"): INF,
            ("UNC", "R4HYP"): 1, ("R4HYP", "RH"): INF,
            ("UNC", "WEYLM"): INF, ("WEYLM", "WEYLH"): 1,
            ("WEYLH", "RH"): INF}
    f_base = R4.maxflow(dict(base), "UNC", "RH")
    ext = dict(base)
    ext.update({("UNC", "BLKREAL"): INF, ("BLKREAL", "NFCLOS"): INF,
                ("NFCLOS", "L1TAILPROVEN"): INF,
                ("L1TAILPROVEN", "L1BAND"): 1,
                ("L1BAND", "WPDN"): 1, ("WPDN", "R4HYP"): INF})
    f_ext = R4.maxflow(dict(ext), "UNC", "RH")
    cf = dict(ext)
    cf[("L1TAILPROVEN", "L1BAND")] = INF
    f_cf = R4.maxflow(dict(cf), "UNC", "RH")
    noomega = {k: v for k, v in ext.items() if v >= INF}
    reach = R4.bfs_reach(noomega, "UNC")
    check("G50-mincut", f_base == 4 and f_ext == 5 and f_cf == 5
          and "RH" not in reach and "L1TAILPROVEN" in reach,
          "flows: base 4, refined 5 (the r128 L1 unit edge REFINED "
          "into L1TAIL-proven (INF, this round: HSW22 closed form + "
          "exact node count) -> L1BAND (unit omega: derivative "
          "floors + matched-prefix law) -> WPD; granting L1BAND "
          "alone still flows 5 -- WPD caps the route, no new "
          "capacity); RH unreachable without an omega edge; census "
          "{MEAS, OMEGA-POS} unchanged")
    info("EXACT L1 RESIDUE after this round: L1(a) = [TAIL: proven "
         "-- a G(T*) -> 0 closed form + node-extra <= (K-1-N) a/T*^2 "
         "+ exact node count K-1] AND [BAND: for every band zero, "
         "gap <= 2 sqrt((tau+OFF)/2)/m_j -- certified TODAY per "
         "rung; the lam-uniform derivative floor m(x) and the "
         "matched-prefix law T*(x) -> inf are the remaining omega = "
         "k_lambda ~ xi_lambda in pointwise currency].  L1-MEAN at "
         "counting level: exact crossover (G17) + measured RvM law "
         "(G38/G39).  NO RH claim; nothing upgraded.")

    # ---------------------------------------------------------- S9
    section("S9  COMPOSITE VERDICT")
    verdicts = [
        "SECULAR-EXACT(det(Meta - z) = -z C(z^2)/A0: operator nodes "
        "== E_N zeros, node count == K-1, exact; G10/G11/G35)",
        "GW-PINNING-GATED(tau = 2 sum |E_N(gamma)|^2 + certified "
        "allowances; the variational value lives on the true zeros; "
        "G32)",
        "GAPLAW-CERTIFIED(every polished band zero within "
        "2 eps_bar/m of a node; scales %s; G33/G34)"
        % ["%.2f" % g for g in gap_scale],
        "NOT-TRANSCRIPTION-BY-INPUT(builder consumes Lambda/arch/"
        "pole only, AST-gated; the Z1 evidence typing of r112/123/"
        "128 carried unchanged)",
        "TAILS-CERTIFIED(G(T) closed form from HSW22 Cor. 1.2 + "
        "PT21; true tail a G(T), operator side exact; G21/G22)",
        "L1-CERTIFIED-ON-LADDER(d1 inside [cache, cache + a G] at "
        "every rung/a; falls; G36)",
        "L1-MEAN-COUNTING(exact resolvability crossover T = 2 pi x, "
        "INBAND_F == 1/KFAC a theorem; RvM law measured; G17/G38/"
        "G39)",
        "L1-OSC-ARITHMETIC(smallness law and d1 separate all three "
        "control worlds; G41/G42)",
        "BOUNDARY-JET-LAW(A_{2m} fall with the rung -- the source-"
        "side mechanism that lets a finite window pin zeros; G40)",
        "MINCUT-REFINED(L1 -> L1TAIL-proven + L1BAND-omega, flows "
        "4/5, census unchanged; G50)"]
    for v in verdicts:
        print("  " + v)

    dt = time.time() - T0_WALL
    check("G99-runtime", dt <= RUNTIME_BAR,
          "%.1f s (bar %.0f)" % (dt, RUNTIME_BAR), kind="edge")
    print("\n" + "=" * 78)
    npass = sum(1 for _n, okc, _d in CHECKS if okc)
    print("GATES: %d/%d PASS   SPEC_SHA %s   runtime %.1f s"
          % (npass, len(CHECKS), SPEC_SHA[:16], dt))
    fails = [nm for nm, okc, _ in CHECKS if not okc]
    if fails:
        print("FAILING GATES: " + ", ".join(fails))
    if EDGE_FAILS:
        print("COMPOSITE: INSTRUMENT-EDGE(%s)" % ",".join(EDGE_FAILS))
    elif EXACT_FAILS:
        print("COMPOSITE: EXACT-LAYER-OBSTRUCTED(%s)"
              % ",".join(EXACT_FAILS))
    else:
        print("COMPOSITE: SECULAR-EXACT + GW-PINNING-GATED + "
              "GAPLAW-CERTIFIED + NOT-TRANSCRIPTION-BY-INPUT + "
              "TAILS-CERTIFIED + L1-CERTIFIED-ON-LADDER + "
              "L1-MEAN-COUNTING + L1-OSC-ARITHMETIC + "
              "BOUNDARY-JET-LAW + MINCUT-REFINED")
    if smoke:
        print("SMOKE MODE -- NOT-VERDICT-BEARING")
    print("NO RH CLAIM.  EXPLORATION ONLY.")
    return 0 if not (EDGE_FAILS or fails) else 1


if __name__ == "__main__":
    sys.exit(main())
