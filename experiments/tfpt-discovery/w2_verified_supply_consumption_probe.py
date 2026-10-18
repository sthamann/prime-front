#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""w2_verified_supply_consumption_probe -- PRIME.PORT.W2.CONSUME.01
(EXPLORATION ONLY, experiments/; round 65 iteration, 2026-08-11).

WHY THIS PROBE EXISTS -- FEED THE CLXXXIX SUPPLY INTO THE CLXXXV
DEMAND.  CLXXXV (w2_pairing_structure_probe, SPEC-SHA 8db29e6e..)
split the wall margin EXACTLY into m = HEAD(n_c) + TCONT(n_c) +
PARITH(n_c) and measured the demand: the Buethe-only certificate
closes 67/67 + 8/8 but needs a head of 95.3% of the atoms; at a
FIXED head of A = 9 atoms the demand is c_req med +1.330 dex, and
the fixed-head demand grows +0.191 dex per log h.  CLXXXVI showed
the per-carrier route dead with ABSOLUTE envelopes (0/16 and 0/17
carriers pass, split-free aggregate +2.14/+1.76 dex, TRIDEF med
1.6e3) and named what each carrier needs: a PHASE-SENSITIVE
Fourier-localised bound on Phi_j at omega_j <= 5.25, +0.9..+1.9
dex sharper than the envelope.  CLXXXIX built exactly that supply
for W1: the first N_Z = 7000 verified zeros (cache
verified_zeros_n7000.npy, Rosser-corridor warded, Platt-Trudgian
T0 = 3e12 EXTERNAL-CITED so every summed zero is ON the line)
summed EXACTLY, with the tail gamma > T_c = 7264.75 paid by an
unconditional Abel envelope.  This probe consumes that supply on
the W2 pairing split: the CLXXXV demand currency (PARITH and the
carriers Phi_j) is evaluated by the verified-zero explicit
formula, phase-sensitively -- the signed read replaces the
absolute envelope.

THE EXACT TRANSLATION (the currency match, warded).  Fix a rung
and a cut n_c; write w for the deployed pw-linear weight of the
critical direction, u0 = log(n_c + 1), uL = log N_g, and let
u_end = M D be the true support end of w (q_read vanishes there;
on the surface u_end ~ uL, on the deep table u_end ~ uL/2).
Build the CONTINUOUS compactly supported pw-linear test function

    phi_cont = left ramp [u0 - eps, u0] (0 -> w(u0), eps =
               min(2, u0 - U0), U0 = ln2/2)  +  w on [u0, uL]
               +  w on [uL, u_end]           (surface only; the
                  extension kills the O(1e-5) truncation jump at
                  uL whose 1/gamma transform tail the 1/gamma^2
                  budget could NOT cover -- found in scouting,
                  repaired exactly: no integer atom lives in
                  (N_g, e^{u_end}], warded),

correct its finitely many ramp atoms (prime powers in the ramp
interval, exact from the deployed tables) and its ramp/extension
continuum (closed form).  Then EXACTLY (ward, no zeros):

    PARITH(n_c) = Phi[phi_cont] - RAMP_AT + RAMP_CONT + EXT_CONT,
    Phi[phi]    = Sum_k (2 Lambda(k)/sqrt k) phi(log k)
                  - 2 Int e^{u/2} phi(u) du,

and the explicit formula prices Phi[phi_cont] by the zeros:

    Phi[phi]  = - Sum_gamma 4 Re phihat(gamma) - TRIV[phi],
    phihat(g) = -(1/g^2) Sum_m J_m e^{i g v_m}   (slope jumps J),

so with the verified zeros summed exactly to T_c and the tail
paid unconditionally:

    PARITH_hat = -4 Sum_{gamma <= T_c} Re phihat(gamma)
                 - TRIV_exact - RAMP_AT + RAMP_CONT + EXT_CONT,
    |PARITH - PARITH_hat| <= TAILB,
    TAILB = 4 S_Delta Abel[1/gamma^2; T_c -> T0, N(T_c) = N_Z]
            + 4 e^{vmax/2} S_Delta S2TAIL      (beyond T0, beta
              in [0,1] NOT assumed on-line)
            + DPS_PAD + TRIV_PAD               (declared),

S_Delta = Sum |J_m| (the constant transform envelope; the
CLXXXIX interval refinement is NOT used -- declared, sound).
The same construction with psi_j(u) = n_j cos(omega_j (u - u0))
on [u0, uL] plus ramps at BOTH ends (the cosine does not vanish
at uL; right-ramp atoms from the 4e6 table) prices every CARRIER
Phi_j at its frequency omega_j <= 5.25: the transform of the
cosine piece is elementary closed form (never singular: gamma_1
= 14.13 > 5.25), the tail envelope is TV(phi_j') = 2 n_j/eps_L +
n_j omega_j^2 Int|cos| + seam terms.  THE SUPPLY IS SIGNED: the
certified lower bound of the wall margin is

    m_cert(n_c) = FC(n_c) + PARITH_hat(n_c) - TAILB(n_c),

which needs NO FC > 0 gate and NO absolute bound on PARITH --
the head size enters only through the tail budget.

WHAT IS MEASURED.
 (a) CURRENCY MATCH (wards): the exact split reproduces (X1/X3
     <= 1e-10, CLXXXV saw 2.1e-13); the bookkeeping identity
     PARITH == recon(phi_cont) to 1e-9 scaled on every read
     (float-exact, no zeros); phi_cont continuity at the support
     end; transform jump form == per-segment closed form; THE
     HEART on every rung x cut and every carrier: |PARITH -
     PARITH_hat| <= TAILB and |Phi_j - Phihat_j| <= TAILB_j --
     zeros against primes at the W2 seat.  Per-carrier
     SHARPENING delivered: log10(|c_j| SUP_psi(omega_j) /
     (|c_j|(|Phihat_j| + TAILB_j))) vs the CLXXXVI demand band
     +0.9..+1.9 dex.
 (b) PER-CARRIER LEMMAS RETRY: the CLXXXVI censuses (0/16 at cB,
     0/17 at the A = 9 head) re-run with the verified-zero reads
     (equal-split budgets, LEM_FRAC = 0.8 verbatim); the
     SPLIT-FREE aggregates log10(Sum_j s_j / FC) old (+2.14 /
     +1.76 reproduced) vs new; the SIGNED aggregate
     log10((|Sum_j c_j Phihat_j| + Sum_j |c_j| TAILB_j)/FC) --
     the phase-sensitive carrier route.  The FIXED-HEAD ladder
     re-run: c_req_new = (|PARITH_hat| + TAILB)/FC at A in
     (9, 12, 20, 50, 100, 200, 400), vs the CLXXXV ladder
     (+1.330/+1.146/+1.049/+0.796 dex reproduced as wards).
 (c) THE W2 CERTIFICATE RECOMPOSED: m_cert > 0 census per rung
     and cut on the 67 surface + 8 deep rungs; minimal
     certifying head per rung on the frozen ladder; the honest
     blocker quantified: log10(TAILB/m) per rung, and the
     ZEROS-NEEDED anatomy (main-term N(T) inversion, declared
     approximation): the T_c and zero count at which TAILB < m
     -- the residual W2 demand priced in verified zeros instead
     of dex of unknown constants.
 (d) THE HEAD-SIZE LAW RETEST: the joint surface+deep jackknife
     slope of the fixed-head demand vs log h -- OLD (envelope)
     reproduced +0.191, NEW (exact supply) refit; typed
     COLLAPSED / PERSISTS / REVERSED at TREND_FLAT = 0.05.  The
     residual hardness law: slope of log10(TAILB/m) vs log h --
     the tail-price law that replaces it.  The CLXXXV L2/
     UNIF-PATH tier re-read: the L1 -> L2 Cauchy-Schwarz cost
     (med 1.0518) reproduced; the exact route is DIRECTION-
     CONDITIONAL data, the Loewner/uniformity step untouched.
 (e) GATES: tau screens (CLXXXV jackknife definitions verbatim,
     PASS |s| <= 0.30 / RELOC >= 0.70) on the new margins;
     controls MUST fire -- smooth world breaks the wall 67/67
     and Epstein + scramble combs break lam_min at kz 9 (CLXXXV
     verbatim), the scrambled comb breaks the exact prime-side
     heart ward |PARITH_scr - PARITH_hat| <= TAILB at BOTH
     control cuts, the CLXXXIX off-line impostor (gamma_1 ->
     beta = 0.75, FE-symmetrised quadruple) shifts PARITH_hat by
     >= 10x the genuine residual.  ANTI-CIRCULARITY: no wall
     output is an input to any bound; the verified ordinates are
     the CLXXXIX-sanctioned input class (pedigree + cache wards
     Z1-Z4 verbatim: census, Rosser corridor both sides,
     gamma_1, independent |zeta| spots at dps 20, T_c < T0) and
     enter ONLY the supply side, tested AGAINST the independent
     prime side; measured m appears only as truth column,
     soundness ward and denominator.  RNG: none except the
     declared scramble control (seed 1, CLXXXV verbatim).

VERDICT (frozen enums, decided by these rules and nothing else):
  V1 translation: CURRENCY-MATCHED(recon max; heart worst
     excess; slack med dex) -- kill wards decide.
  V2 sharpening: SHARPENING-DELIVERED(med dex at the A = 9 cut
     >= 0.90, the CLXXXVI band floor; lemma retry censuses;
     aggregates old -> new) / SHARPENING-SHORT(med dex).
  V3 certificate: W2VZ-CLOSES(n/67 surface + n/8 deep, minimal
     head fraction) iff any rung closes; else
     W2VZ-TAIL-PRICED(0 closed; log10(TAILB/m) min/med/max; the
     zeros-needed ladder med/max + census at N <= 1e5/1e6/1e7)
     -- the honest headline either way.
  V4 law: HEADLAW-COLLAPSED(new slope, |b| <= 0.05, was +0.191)
     / HEADLAW-PERSISTS(b) / HEADLAW-REVERSED(b), plus
     TAILLAW(slope of log10(TAILB/m) per log h).
  V5 gates: DISCRIMINATION-FIRES(scramble 2/2 cuts, impostor
     ratio >= 10, smooth 67/67, Epstein+scramble lam < 0) /
     DISCRIMINATION-UNRESOLVED(census); screens appended.
DEAD overrides: K1 PIPELINE-BROKEN / K2 WARD-BROKEN / K3
ALGEBRA-BROKEN as tagged.

FROZEN BARS: N_Z = 7000 (cache verified_zeros_n7000.npy, reused
from CLXXXIX, NOT rebuilt); ZETA_TOL = 1e-6 at NS = 24 spots
(dps 20); CORR_EPS = 1e-6; DPS_ERR = 1e-9/ordinate; RAMP_EPS =
min(2.0, u0 - U0); CARRIER_ER = 1.0; CUT ladder = HEAD_A =
(9, 12, 20, 50, 100, 200, 400) head atoms (CLXXXV verbatim) +
the deployed covering cut cB; OMEGA_C = 5.25, OMEGA_MAX = 240,
LEM_FRAC = 0.8, frame verbatim CLXXXV; RECON_TOL = 1e-9 scaled;
CONT_TOL = 1e-12 scaled; TRANS_TOL = 1e-10; CTRANS_TOL = 1e-8;
TRIV2_TOL = 1e-9; SOUND_TOL = 1e-9; ABEL_BAND = (1e-4, 4e-4);
reproduction refs (CLXXXV/CLXXXVI frozen run): N_SURF = 67,
N_DEEP = 8, DEX_OLD_REF = {9: +1.330, 12: +1.146, 200: +1.049,
400: +0.796} atol 0.05, HAFR_REF = 0.9534 / HAFR_DEEP_REF =
0.971 atol 0.005, ARITH_REF = 0.302 atol 0.010, TRIDEF_REF =
1.61e3 rtol 0.15, KCAR_REF = 12, JSTAR_REF = 2, LEMMA_REF = 0/16
at cB + 0/17 at A = 9 exact, AGG_REF = (+2.14, +1.76) atol 0.05,
SLOPE_OLD_REF = +0.191 atol 0.02, CS_REF = 1.0518 atol 0.005;
SHARP_FLOOR = 0.90 dex; TREND_FLAT = 0.05; IMP_BETA = 0.75,
IMP_RATIO_MIN = 10; SCR both control cuts must fire; NEED_LEVELS
= (1e5, 1e6, 1e7); SPEC prefixes: w2 8db29e6e, subgamma
c7d8810c, j16 supply deea4e1c (docstring SHA, source parsed, not
executed).  Runtime cap declared: 25 min.  Smoke mode
W2VZC_SMOKE=1 restricts the surface to kz <= 30 and DEEP_MAX =
2 and defers the full-only reproduction wards (disclosed
prints); controls always full.

SCOUTING DISCLOSURE (2026-08-11, pre-spec, before any probe
run): ONE throwaway scratch script (deleted) sized the
translation on kz 9/60/121 at the cuts A = 9 and cB, and the
following numbers were SEEN before this spec was frozen:
(i) the bookkeeping recon is float-exact (dev <= 2e-15) and the
    heart holds with slack: |PARITH - PARITH_hat| = 2e-9..2.4e-7
    against TAILB = 1.5e-3..3.7e-3 (slack +3.9..+6.0 dex);
(ii) S_Delta = 1.8..4.5, Abel base 2.06e-4, so TAILB ~ 2e-3
    sits ABOVE the wall margin m = 4.0e-4/7.4e-5/7.3e-6 by
    +0.69/+1.45..1.47/+2.31..2.36 dex: m_cert < 0 on all six
    scout reads -- the certificate is NOT expected to close at
    N_Z = 7000, and V3 is expected to type W2VZ-TAIL-PRICED;
(iii) the envelope sharpening delivered is log10(SUP_B/SUP_VZ)
    ~ +1.1..+1.5 dex and c_req_new collapses to 1.007..1.023
    (dex +0.003..+0.010) where FC > 0 -- the +1.33 dex fixed-
    head demand is envelope looseness, the residue is the tail
    price;
(iv) six carrier reads on kz 60 (j = 0..5 at cB and A = 9):
    residuals ~6e-7, all inside TAILB_j = 1.2e-3..1.0e-2;
(v) the uL truncation jump (~1e-5) was found UNSOUND against
    the 1/gamma^2 tail budget and the support extension repair
    was designed BEFORE the freeze (it is exact, not a bar).
NO bar, band, tolerance, enum or success criterion was chosen
to fit those numbers: the kill wards are identities and
soundness statements, the reproduction refs are the CLXXXV/
CLXXXVI frozen-run numbers, SHARP_FLOOR is the CLXXXVI demand
band floor, TREND_FLAT is the CLXXXIX class bar, and V3 types
BOTH outcomes symmetrically.

SMOKE-RUN DISCLOSURE (2026-08-11, before freezing): TWO smoke
runs (both W2VZC_SMOKE=1: 19 surface rungs kz <= 30, DEEP_MAX =
2, controls full), full fail-first history, nothing omitted.
SMOKE 1 (10.1 s, 44 checks, exit 1): 43/44 -- the single failure
was B4, the carrier ward's OWN independent quadrature: its grid
np.linspace(aa, bb) straddled the slope kinks of the carrier
test function at u0 and uL, so the GL24 comparison converged
only to 6.4e-7/1.6e-7 against bars 1e-8/1e-9.  The closed forms
themselves were verified correct (the carrier HEART B3 passed on
all 342 reads with worst scaled excess -1.0e-3).  Amendment A1.
SMOKE 2 (9.9 s, 44/44, exit 0): measured content the frozen run
must be consistent with (19 shallow rungs): heart worst scaled
excess -4.9e-06 on 134 direct reads, slack +2.12/+3.49/+5.37
dex, recon worst 2.6e-15; carrier heart worst -1.0e-3 on 342
reads, transform/trivial wards 7.2e-16/6.9e-18; per-carrier
sharpening delivered med +1.66 dex at A = 9 (band +0.9..+1.9);
lemma retry 5/11 at cB and 6/11 at A = 9 (subset indices; was
0/16, 0/17), split-free aggregate cB +2.52 -> +1.03 dex, A = 9
+1.62 -> +0.11 dex, SIGNED aggregate +0.068/-0.046 dex;
fixed-head c_req_new dex med +0.004 (A = 9) / +0.004 (A = 12) /
+0.001 (A = 200) / +0.000 (A = 400) vs old +1.259/+1.169/
+1.045/+0.763 on the subset; THE SURPRISE against the scouting
expectation (which predicted TAIL-PRICED): the SIGNED
certificate closes 14/19 shallow rungs at deeper fixed heads
(A = 50..400; TAILB falls with the cut while m is fixed),
minimal head fraction med 0.522 vs the Buethe route's 0.953;
deep 0/2 (TAILB/m +2.8 dex); blocker log10(TAILB/m) at cB
+0.79/+1.18/+1.85 dex, zeros-needed med 1.8e5 / max 1.2e6;
laws on the subset: old +0.376 (subset artefact of the deferred
D1 ward), new +0.037, tail law +0.667 dex/log h (R^2 0.97);
screens A=9 PASS(-0.001), A=12 PASS(+0.024), TAILB/m
AMBIG(-0.389); controls fire (smooth 19/19, Epstein -1.0e+01,
scramble -7.9e+00, heart-break 2/2 at 1.5e2/3.8e2 x TAILB,
impostor 8.2e4 x).
AMENDMENTS (two, both disclosed):
 A1  THE B4 WARD QUADRATURE GRID WAS MIS-SPECIFIED.  The
     carrier test function is smooth only piecewise (kinks at
     u0 and uL); the ward's independent GL24 grid must be built
     per smooth piece.  v1 subdivides [aa,u0]/[u0,uL]/[uL,bb]
     separately (transform ward at frequency max(om, 25)).
     The bars (1e-8, 1e-9) did NOT move; the metric's grid was
     repaired.  No measured supply/demand number changed.
 A2  ONE MEASUREMENT ADDED, none removed, no bar moved: the
     MINIMAL CERTIFYING HEAD FRACTION (A*/natom on closing
     rungs) and the certified margin log10(m_cert/m) -- the
     mission's own headline contrast against the CLXXXV 95.3%
     head; printed in C and typed into V3.
No bar, band, count, rule or enum was moved after any smoke
run beyond A1/A2 above; the frozen run repeats everything on
the full 67 + 8 ladder and the enums move only as the full
data says.

HONEST SCOPE (stated once, repeated in the verdict): every
certified or measured statement here is per-rung and along the
MEASURED critical direction v (DIRECTION-CONDITIONAL, CLXXXV
d1 verbatim); the head grows or shrinks only inside the frozen
ladder; nothing here is uniform in h or in direction; the deep
block is FLOAT-LEVEL as in CLXXXV.  The verified-zero data is a
FINITE input class: a finite zero sum can never prove RH, and a
TAIL-PRICED verdict prices the residual W2 demand in verified
zeros -- a computation-size statement, not a theorem.  W2 as an
all-h, all-direction object (the Weil-positivity face) remains
RH-hard and untouched in EVERY branch.  NO RH claim in either
direction.  No marker moves, no promotion, no ledger row;
stdout only; nothing written outside experiments/.

Sources (read-only): v563_paper2_readouts (core);
w2_pairing_structure_probe (CLXXXV/CLXXXVI demand machinery
verbatim: rungs, split, frame, censuses, controls);
subgamma_fourier_bound_probe (CLXXXI: Rosser corridor, Abel,
s2_tail, U0, T0); the CLXXXIX cache + tail-grid/pad conventions
(j16_verified_zero_supply_probe, SPEC prefix warded, source
parsed not executed).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/w2_verified_supply_consumption_probe.py
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

import v563_paper2_readouts as core  # noqa: E402  (READ-ONLY)
import w2_pairing_structure_probe as w2  # noqa: E402  (READ-ONLY)
import subgamma_fourier_bound_probe as subg  # noqa: E402 (READ-ONLY)

SMOKE = os.environ.get("W2VZC_SMOKE", "") == "1"

ZC_NPY = os.path.join(_HERE, "verified_zeros_n7000.npy")
SUPPLY_SRC = os.path.join(_HERE, "j16_verified_zero_supply_probe.py")
N_Z = 7000
ZETA_TOL = 1.0e-6
NS_ZETA = 24
CORR_EPS = 1.0e-6
DPS_ERR = 1.0e-9
RAMP_EPS_MAX = 2.0
CARRIER_ER = 1.0
CUT_A = w2.HEAD_A                     # (9, 12, 20, 50, 100, 200, 400)
A_STR = 9
RECON_TOL = 1.0e-9
CONT_TOL = 1.0e-12
TRANS_TOL = 1.0e-10
CTRANS_TOL = 1.0e-8
TRIV2_TOL = 1.0e-9
SOUND_TOL = 1.0e-9
ABEL_BAND = (1.0e-4, 4.0e-4)
N_SURF = 67
N_DEEP = 8
DEX_OLD_REF = {9: 1.330, 12: 1.146, 200: 1.049, 400: 0.796}
DEX_ATOL = 0.05
HAFR_REF = 0.9534
HAFR_DEEP_REF = 0.971
HAFR_ATOL = 0.005
ARITH_REF = 0.302
ARITH_ATOL = 0.010
TRIDEF_REF = 1.61e3
TRIDEF_RTOL = 0.15
KCAR_REF = 12
JSTAR_REF = 2
LEMMA_REF = (0, 16, 0, 17)
AGG_REF = (2.14, 1.76)
AGG_ATOL = 0.05
SLOPE_OLD_REF = 0.191
SLOPE_ATOL = 0.02
CS_REF = 1.0518
CS_ATOL = 0.005
SHARP_FLOOR = 0.90
SHARP_TOP = 1.90
TREND_FLAT = 0.05
IMP_BETA = 0.75
IMP_RATIO_MIN = 10.0
NEED_LEVELS = (1.0e5, 1.0e6, 1.0e7)
CTRL_KZ = w2.CTRL_KZ
KZ_TOP = 30 if SMOKE else w2.KZMAX
DEEP_MAX = 2 if SMOKE else N_DEEP
PREFIXES = dict(w2="8db29e6e", subgamma="c7d8810c",
                supply="deea4e1c")
LN2 = math.log(2.0)

CHECKS = []
KILLS = []
T0 = time.time()
_GLX, _GLW = np.polynomial.legendre.leggauss(24)


def check(name, ok, detail="", kill=None):
    CHECKS.append((name, bool(ok)))
    if kill and not ok:
        KILLS.append(kill)
    print("  [%s] %s%s" % ("PASS" if ok else "FAIL", name,
                           ("  -- " + detail) if detail else ""),
          flush=True)
    return bool(ok)


def section(title):
    print("\n" + "=" * 76)
    print(title)
    print("=" * 76, flush=True)


def ast_scan():
    src = open(os.path.abspath(__file__), encoding="utf-8").read()
    bad = []
    for node in ast.walk(ast.parse(src)):
        name = None
        if isinstance(node, ast.Name):
            name = node.id
        elif isinstance(node, ast.Attribute):
            name = node.attr
        if name and name.lower() in w2.BANNED_IDS:
            bad.append(name)
    return bad


def spec_sha_of_source(path):
    """Docstring SHA of a probe source WITHOUT executing it."""
    tree = ast.parse(open(path, encoding="utf-8").read())
    doc = ast.get_docstring(tree, clean=False)
    return hashlib.sha256(doc.encode("utf-8")).hexdigest()


def band(v):
    v = np.asarray(v, float)
    return float(np.min(v)), float(np.median(v)), float(np.max(v))


# ------------------------------------------------ supply machinery
def tail_grid(D, tc):
    """CLXXXIX tail grid: linear (phase step 0.25 in gamma D) from
    T_c, then geometric *1.3 to T0."""
    dt = max(0.25 / D, 0.5)
    tsw = max(300.0, 10.0 * math.pi / D, 2.0 * tc)
    nlin = max(int(math.ceil((tsw - tc) / dt)), 1)
    lin = tc + dt * np.arange(nlin + 1)
    geo = [lin[-1]]
    while geo[-1] < subg.T0_RH:
        geo.append(min(geo[-1] * 1.3, subg.T0_RH))
    return np.concatenate([lin, np.asarray(geo[1:], float)])


def zsum4re(v, J, gam):
    """4 Sum_k Re phihat(gamma_k), phihat = -(1/g^2) Sum J e^{igv},
    chunked over the ordinates."""
    tot = 0.0
    for i0 in range(0, len(gam), 1000):
        g = gam[i0:i0 + 1000]
        E = np.exp(1j * np.outer(g, v))
        tot += float(np.sum((-(E @ J) / g ** 2).real))
    return 4.0 * tot


def triv_pl(edges, fvals, slopes):
    """TRIV = Int 2 phi(u) e^{-u/2}/(e^{2u} - 1) du, GL24/piece."""
    tot = 0.0
    for a, b, fa, sl in zip(edges[:-1], edges[1:], fvals[:-1],
                            slopes):
        mid, half = 0.5 * (a + b), 0.5 * (b - a)
        u = mid + half * _GLX
        phi = fa + sl * (u - a)
        tot += half * float(np.dot(_GLW, 2.0 * phi
                                   * np.exp(-0.5 * u)
                                   / np.expm1(2.0 * u)))
    return tot


def triv_env_pl(edges, fvals):
    """CLXXXI trivial-zero envelope for a pw-linear phi."""
    f = np.asarray(fvals, float)
    v = np.asarray(edges, float)
    supg = 2.0 * np.maximum(np.abs(f[:-1]), np.abs(f[1:])) \
        * np.exp(-0.5 * v[:-1])
    wseg = 0.5 * (np.log(1.0 - np.exp(-2.0 * v[1:]))
                  - np.log(1.0 - np.exp(-2.0 * v[:-1])))
    return float(np.sum(supg * wseg))


def hat_seg_c(edges, fvals, slopes, z):
    """Exact transform Int phi(u) e^{z u} du at complex z, per-
    segment closed form (impostor + transform ward)."""
    iz = 1.0 / z
    e0 = np.exp(z * edges[:-1])
    e1 = np.exp(z * edges[1:])
    val = e1 * (fvals[1:] * iz - slopes * iz ** 2) \
        - e0 * (fvals[:-1] * iz - slopes * iz ** 2)
    return complex(np.sum(val))


def phi_cont_of(row, sp):
    """The continuous compactly supported pw-linear phi_cont of the
    direct PARITH read, with exact ramp/extension corrections."""
    Wv, D, M = row["Wv"], row["D"], row["M"]
    u0, uL = sp["u0"], sp["uL"]
    a_p, b_p, wa, wb, s_p = w2.weight_pieces(Wv, u0, uL, D, M)
    w0 = float(wa[0])
    eps = min(RAMP_EPS_MAX, u0 - subg.U0)
    aL = u0 - eps
    edges = [aL]
    fvals = [0.0]
    slopes = [w0 / eps]
    edges.extend(a_p.tolist())
    fvals.extend(wa.tolist())
    slopes.extend(s_p.tolist())
    edges.append(float(b_p[-1]))
    fvals.append(float(wb[-1]))
    # support extension [uL, u_end = M D]: kills the truncation
    # jump at uL exactly; no integer atom lives in (N_g, e^{MD}]
    # on the surface, and on the deep table u_end < uL (skipped).
    u_end = M * D
    ext_cont = 0.0
    ext_at = 0.0
    if u_end > uL + 1e-12 and abs(fvals[-1]) > 0.0:
        e_p = w2.weight_pieces(Wv, uL, u_end, D, M)
        ext_cont = w2.tcont_of(e_p)
        edges.extend(e_p[1].tolist())
        fvals.extend(e_p[3].tolist())
        slopes.extend(e_p[4].tolist())
        k_lo = row["Ng"] + 1
        k_hi = int(math.floor(math.exp(u_end)))
        if k_hi >= k_lo:
            kk = np.arange(k_lo, min(k_hi,
                                     len(row["lam_tab"]) - 1) + 1)
            lv = row["lam_tab"][kk]
            nz = lv > 0.0
            if bool(np.any(nz)):
                kk = kk[nz].astype(float)
                ext_at = float(np.sum(
                    2.0 * lv[nz] / np.sqrt(kk)
                    * w2.q_read(Wv, np.log(kk), D, M)))
    edges = np.asarray(edges, float)
    fvals = np.asarray(fvals, float)
    slopes = np.asarray(slopes, float)
    J = np.empty(len(edges))
    J[0] = slopes[0]
    J[1:-1] = slopes[1:] - slopes[:-1]
    J[-1] = -slopes[-1]
    keep = np.abs(J) > 1e-15
    # ramp continuum 2 Int_{aL}^{u0} e^{u/2} (w0/eps)(u - aL) du
    s = w0 / eps
    ramp_cont = 2.0 * (math.exp(u0 / 2.0) * (2.0 * w0 - 4.0 * s)
                       - math.exp(aL / 2.0) * (-4.0 * s))
    # ramp atoms: prime powers in (e^{aL}, n_c]
    lo = int(math.floor(math.exp(aL))) + 1
    kk = np.arange(max(lo, 2), sp["nc"] + 1)
    ramp_at = 0.0
    if len(kk):
        lv = row["lam_tab"][kk]
        nz = lv > 0.0
        kk = kk[nz].astype(float)
        if len(kk):
            ramp_at = float(np.sum(2.0 * lv[nz] / np.sqrt(kk)
                                   * s * (np.log(kk) - aL)))
    return dict(v=edges[keep], J=J[keep],
                sd=float(np.sum(np.abs(J[keep]))),
                vmax=float(edges[-1]), edges=edges, fvals=fvals,
                slopes=slopes, w0=w0, eps=eps,
                ramp_cont=ramp_cont, ramp_at=ramp_at,
                ext_cont=ext_cont, ext_at=ext_at,
                fend=float(fvals[-1]),
                fmax=float(np.max(np.abs(fvals))),
                triv=triv_pl(edges, fvals, slopes))


def direct_read(row, sp, pc, gam, abel, s2t, inv2, inv3):
    """PARITH_hat + TAILB of one (rung, cut)."""
    zs = zsum4re(pc["v"], pc["J"], gam)
    par_hat = (-zs - pc["triv"] - pc["ramp_at"] + pc["ramp_cont"]
               + pc["ext_cont"] - pc["ext_at"])
    dps = 4.0 * pc["sd"] * (pc["vmax"] * inv2 + 2.0 * inv3) \
        * DPS_ERR
    tailb = (4.0 * pc["sd"] * abel
             + 4.0 * math.exp(0.5 * pc["vmax"]) * pc["sd"] * s2t
             + dps + 1e-12 * (1.0 + abs(pc["triv"])))
    return par_hat, tailb


def recon_of(row, sp, pc):
    """Bookkeeping ward (no zeros): PARITH reconstructed from the
    phi_cont atom/continuum sides must equal sp['par'] exactly."""
    uu = row["uu"]
    idx = np.searchsorted(pc["edges"], uu, side="right") - 1
    ok = (idx >= 0) & (idx < len(pc["slopes"]))
    phi = np.zeros(len(uu))
    phi[ok] = pc["fvals"][idx[ok]] + pc["slopes"][idx[ok]] \
        * (uu[ok] - pc["edges"][idx[ok]])
    atom_side = float(np.dot(row["mu"], phi))
    cont_side = sp["tcont"] + pc["ramp_cont"] + pc["ext_cont"]
    par_recon = (atom_side - cont_side) - pc["ramp_at"] \
        - pc["ext_at"] + pc["ramp_cont"] + pc["ext_cont"]
    return abs(par_recon - sp["par"]) \
        / max(1.0, abs(sp["t_int"]))


def abs_cos_int(om, L):
    """Int_0^L |cos(om x)| dx, exact via the |sin| primitive."""
    if om == 0.0:
        return L
    y = om * L
    return (w2._abs_sin_int(y + 0.5 * math.pi)
            - w2._abs_sin_int(0.5 * math.pi)) / om


def carrier_hat(om, nj, u0, uL, eL, eR, g):
    """Closed-form transform of the carrier test function ramp +
    nj cos(om (u - u0)) + ramp, at i*g for an ordinate array g
    (never singular: g >= gamma_1 > OMEGA_C >= om)."""
    ig = 1.0 / (1j * g)
    sL = nj / eL
    aa = u0 - eL
    tL = (np.exp(1j * g * u0) * (nj * ig - sL * ig ** 2)
          - np.exp(1j * g * aa) * (-sL * ig ** 2))
    L = uL - u0
    if om == 0.0:
        tc = nj * np.exp(1j * g * u0) \
            * (np.exp(1j * g * L) - 1.0) / (1j * g)
    else:
        num = (np.exp(1j * g * L) * (1j * g * math.cos(om * L)
                                     + om * math.sin(om * L))
               - 1j * g)
        tc = nj * np.exp(1j * g * u0) * num / (om ** 2 - g ** 2)
    fR = nj * math.cos(om * L)
    sR = -fR / eR
    bb = uL + eR
    tR = (np.exp(1j * g * bb) * (-sR * ig ** 2)
          - np.exp(1j * g * uL) * (fR * ig - sR * ig ** 2))
    return tL + tc + tR


def carrier_phi_eval(om, nj, u0, uL, eL, eR, u):
    """The carrier test function evaluated at u (quadratures)."""
    L = uL - u0
    fR = nj * math.cos(om * L)
    return np.where(
        u < u0, (nj / eL) * (u - (u0 - eL)),
        np.where(u <= uL, nj * np.cos(om * (u - u0)),
                 fR * (1.0 - (u - uL) / eR)))


def carrier_supply(row, sp, om, nj, gam, abel, s2t, inv2, inv3,
                   lam_ramp, want_ward=False):
    """Phihat_j + TAILB_j of one carrier at one cut."""
    u0, uL = sp["u0"], sp["uL"]
    eL = min(RAMP_EPS_MAX, u0 - subg.U0)
    eR = CARRIER_ER
    L = uL - u0
    zs = 0.0
    for i0 in range(0, len(gam), 2000):
        g = gam[i0:i0 + 2000]
        zs += float(np.sum(carrier_hat(om, nj, u0, uL, eL, eR,
                                       g).real))
    zs *= 4.0
    # ramp atoms (left from the rung table, right from lam_ramp)
    ra = 0.0
    lo = int(math.floor(math.exp(u0 - eL))) + 1
    kk = np.arange(max(lo, 2), sp["nc"] + 1)
    if len(kk):
        lv = row["lam_tab"][kk]
        nz = lv > 0.0
        kk = kk[nz].astype(float)
        if len(kk):
            ra += float(np.sum(2.0 * lv[nz] / np.sqrt(kk)
                               * (nj / eL) * (np.log(kk)
                                              - (u0 - eL))))
    hi = int(math.floor(math.exp(uL + eR)))
    kk = np.arange(row["Ng"] + 1, min(hi, len(lam_ramp) - 1) + 1)
    if len(kk):
        lv = lam_ramp[kk]
        nz = lv > 0.0
        kk = kk[nz].astype(float)
        if len(kk):
            fR = nj * math.cos(om * L)
            ra += float(np.sum(2.0 * lv[nz] / np.sqrt(kk) * fR
                               * (1.0 - (np.log(kk) - uL) / eR)))
    # ramp continuum, closed form on the two linear ramps
    sL = nj / eL
    aa = u0 - eL
    rc = 2.0 * (math.exp(u0 / 2.0) * (2.0 * nj - 4.0 * sL)
                - math.exp(aa / 2.0) * (-4.0 * sL))
    fR = nj * math.cos(om * L)
    sR = -fR / eR
    bb = uL + eR
    rc += 2.0 * (math.exp(bb / 2.0) * (-4.0 * sR)
                 - math.exp(uL / 2.0) * (2.0 * fR - 4.0 * sR))
    # trivial-zero term, GL24 on a KINK-RESPECTING subdivided grid
    # (amendment A1: the pieces meet with slope kinks at u0 and uL,
    # so the quadrature grid must not straddle them); the ward
    # doubles the resolution.
    def _qgrid(freq, mult):
        ed = []
        for a2, b2 in ((aa, u0), (u0, uL), (uL, bb)):
            ns2 = max(4, int(math.ceil((b2 - a2) * freq / 0.4))
                      * mult)
            seg = np.linspace(a2, b2, ns2 + 1)
            ed.append(seg if b2 == bb else seg[:-1])
        return np.concatenate(ed)

    def triv_at(mult):
        ed = _qgrid(max(om, 1.0), mult)
        mid = 0.5 * (ed[:-1] + ed[1:])
        half = 0.5 * (ed[1:] - ed[:-1])
        tot = 0.0
        for xg, wg in zip(_GLX, _GLW):
            u = mid + half * xg
            phi = carrier_phi_eval(om, nj, u0, uL, eL, eR, u)
            tot += wg * float(np.sum(half * 2.0 * phi
                                     * np.exp(-0.5 * u)
                                     / np.expm1(2.0 * u)))
        return tot
    triv = triv_at(1)
    triv_dev = abs(triv - triv_at(2)) / max(1.0, abs(triv)) \
        if want_ward else 0.0
    # TV(phi_j') envelope: ramps + cosine curvature + seams
    tv = (2.0 * abs(sL) + nj * om * om * abs_cos_int(om, L)
          + abs(-nj * om * math.sin(om * L) - sR) + abs(sR))
    tailb = (4.0 * tv * abel
             + 4.0 * math.exp(0.5 * bb) * tv * s2t
             + 4.0 * tv * (bb * inv2 + 2.0 * inv3) * DPS_ERR
             + 1e-12 * (1.0 + abs(triv)))
    phi_hat = -zs - triv - ra + rc
    tw = 0.0
    if want_ward:
        gg = np.array([25.0])
        cf = complex(carrier_hat(om, nj, u0, uL, eL, eR, gg)[0])
        ed = _qgrid(max(om, 25.0), 2)
        mid = 0.5 * (ed[:-1] + ed[1:])
        half = 0.5 * (ed[1:] - ed[:-1])
        qd = 0.0 + 0.0j
        for xg, wg in zip(_GLX, _GLW):
            u = mid + half * xg
            phi = carrier_phi_eval(om, nj, u0, uL, eL, eR, u)
            qd += wg * complex(np.sum(half * phi
                                      * np.exp(1j * 25.0 * u)))
        tw = abs(cf - qd) / max(1.0, abs(cf))
    return phi_hat, tailb, tv, triv_dev, tw


def zeros_needed(m, sd):
    """ANATOMY (main-term N(T), declared approximation): the T at
    which 4 sd (log(T/2pi) + 1)/(2 pi T) = m, and N_main(T)."""
    tgt = m / (4.0 * sd)

    def f(t):
        return (math.log(t / (2.0 * math.pi)) + 1.0) \
            / (2.0 * math.pi * t)
    lo, hi = 15.0, 1.0e16
    if f(lo) < tgt:
        return lo, 0.0
    for _ in range(200):
        mid = math.sqrt(lo * hi)
        if f(mid) > tgt:
            lo = mid
        else:
            hi = mid
        if hi / lo < 1.0 + 1e-9:
            break
    t = hi
    return t, float(subg.n_main(np.array([t]))[0])


def lemma_census(rungs, cut_of, sup_of, tag):
    """The CLXXXVI per-carrier lemma census at a cut rule, with a
    pluggable per-carrier supply; returns (n_pass, n_idx,
    med_aggregate, worst deficits)."""
    pas, dfc, agg = {}, {}, []
    for r in rungs:
        item = cut_of(r)
        if item is None:
            continue
        spf, cr = item
        if spf["fc"] <= 0.0:
            continue
        idx = np.nonzero(cr["sel_om"])[0]
        if len(idx) == 0:
            continue
        s_j = sup_of(r, spf, cr, idx)
        if s_j is None:
            continue
        budget = spf["fc"] / len(idx)
        agg.append(math.log10(max(float(np.sum(s_j)), 1e-300)
                              / spf["fc"]))
        for jj, j in enumerate(idx):
            k = int(j)
            pas.setdefault(k, [0, 0])
            pas[k][1] += 1
            if s_j[jj] <= budget:
                pas[k][0] += 1
            dfc.setdefault(k, []).append(
                math.log10(max(s_j[jj], 1e-300) / budget))
    nl = sum(1 for k, v in pas.items()
             if v[1] > 0 and v[0] / v[1] >= w2.LEM_FRAC)
    med_agg = float(np.median(agg)) if agg else float("nan")
    worst = sorted(((float(np.median(v)), k)
                    for k, v in dfc.items()), reverse=True)[:5]
    print("      %s: %d of %d carrier indices pass their equal "
          "split; split-free aggregate med %+.2f dex"
          % (tag, nl, len(pas), med_agg))
    if worst:
        print("        worst (median log10(supply/budget)): %s"
              % ", ".join("j=%d: %+.2f" % (k, d)
                          for d, k in worst))
    return nl, len(pas), med_agg


def finish(labels):
    section("V -- FROZEN VERDICT")
    passed = sum(1 for _n, ok in CHECKS if ok)
    if KILLS:
        verdict = {"K1": "PIPELINE-BROKEN", "K2": "WARD-BROKEN",
                   "K3": "ALGEBRA-BROKEN"}[KILLS[0]]
    else:
        verdict = " / ".join(labels.get(k, "-")
                             for k in ("v1", "v2", "v3", "v4",
                                       "v5"))
    print("\n  VERDICT: %s" % verdict)
    print("""
  HONEST SCOPE: every statement is per-rung and along the MEASURED
  critical direction v (DIRECTION-CONDITIONAL); nothing is uniform
  in h or direction; the deep block is FLOAT-LEVEL.  The verified
  ordinates are the CLXXXIX-sanctioned finite input class; a finite
  zero sum can never prove RH, and a TAIL-PRICED verdict prices the
  residual W2 demand as a computation size, not a theorem.  The
  all-h all-direction W2 (Weil-positivity face) remains RH-hard and
  untouched.  NO RH claim; no marker moves; no promotion.""")
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed"
          % (time.time() - T0, len(CHECKS), len(CHECKS) - passed))
    if any(not ok for _n, ok in CHECKS):
        print("FAILED: %s" % [nm for nm, ok in CHECKS if not ok])
    return 0 if passed == len(CHECKS) else 1


def main():
    section("PRIME.PORT.W2.CONSUME.01 -- the verified-zero supply "
            "consumed on the W2 pairing split (EXPLORATION ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s"
          % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
    shas = dict(
        w2=hashlib.sha256(w2.__doc__.encode("utf-8")).hexdigest(),
        subgamma=hashlib.sha256(
            subg.__doc__.encode("utf-8")).hexdigest(),
        supply=spec_sha_of_source(SUPPLY_SRC))
    for tag in sorted(shas):
        print("    %-8s SPEC SHA-256 = %s" % (tag, shas[tag]))
    print("    PEDIGREE (EXTERNAL-CITED): gamma_1 = %.6f; "
          "Platt-Trudgian 2021 T0 = %.1e (every summed zero ON "
          "the line);" % (subg.GAMMA1, subg.T0_RH))
    print("      Rosser 1941 N(T) corridor (tail only); Buethe "
          "2016 0.94 sqrt x (old supply, reproduced as demand "
          "baseline);")
    print("      verified ordinates n = 1..%d (CLXXXIX cache, "
          "REUSED, not rebuilt; wards below)." % N_Z)
    if SMOKE:
        print("    *** SMOKE MODE: kz <= %d, DEEP_MAX = %d, "
              "full-only wards deferred ***" % (KZ_TOP, DEEP_MAX))
    check("S0 AST firewall clean (CLXXXV identifier ban)",
          not ast_scan(), kill="K2")
    ok_pref = all(shas[k][:8] == v for k, v in PREFIXES.items())
    check("S0b predecessor SPEC prefixes reproduced (%s)"
          % "/".join(PREFIXES[k] for k in sorted(PREFIXES)),
          ok_pref, kill="K2")

    # ------------------------------------------------------------ Z
    section("Z -- the verified-zero cache and its wards (CLXXXIX "
            "verbatim)")
    check("Z0 cache present (%s)" % os.path.basename(ZC_NPY),
          os.path.exists(ZC_NPY), kill="K1")
    if KILLS:
        return finish({})
    gam = np.load(ZC_NPY)
    t_c = float(gam[-1])
    check("Z1 census %d == %d, strictly increasing, first == "
          "gamma_1 (dev %.1e)"
          % (len(gam), N_Z, abs(gam[0] - subg.GAMMA1)),
          len(gam) == N_Z and bool(np.all(np.diff(gam) > 0.0))
          and abs(gam[0] - subg.GAMMA1) <= 2.0e-6, kill="K2")
    kk = np.arange(1, N_Z + 1, dtype=float)
    up_r = subg.n_up(gam + CORR_EPS)
    lo_r = subg.n_lo(gam + CORR_EPS)
    up_l = subg.n_up(np.maximum(gam - CORR_EPS, 2.0))
    lo_l = subg.n_lo(np.maximum(gam - CORR_EPS, 2.0))
    n_ok = int(np.sum((kk <= up_r) & (kk >= lo_r)
                      & (kk - 1.0 <= up_l) & (kk - 1.0 >= lo_l)))
    check("Z2 Rosser-corridor consistency per index (%d/%d both "
          "sides)" % (n_ok, N_Z), n_ok == N_Z, kill="K2")
    from mpmath import mp as _mp, mpc as _mpc
    from mpmath import zeta as _zf
    _mp.dps = 20
    idx = np.unique(np.geomspace(1, N_Z, NS_ZETA).astype(int)) - 1
    worst_z = max(float(abs(_zf(_mpc(0.5, float(gam[i])))))
                  for i in idx)
    check("Z3 independent zeta spot check <= %.0e at %d ordinates "
          "(worst %.1e)" % (ZETA_TOL, len(idx), worst_z),
          worst_z <= ZETA_TOL, kill="K2")
    check("Z4 T_c = %.4f below T0" % t_c, t_c < subg.T0_RH,
          kill="K2")
    inv2 = float(np.sum(1.0 / gam ** 2))
    inv3 = float(np.sum(1.0 / gam ** 3))
    s2t = subg.s2_tail()

    # ------------------------------------------------------------ W
    section("W -- the CLXXXV ladder (demand machinery verbatim)")
    rungs = []
    for kz in range(2, KZ_TOP + 1):
        r = w2.build_rung(kz)
        if r is not None:
            rungs.append(r)
    rungs.sort(key=lambda r: (r["h"], r["kz"]))
    N = len(rungs)
    check("W1 ladder census %d %s" % (N, "== 67" if not SMOKE
                                      else ">= 8 (smoke)"),
          (N == N_SURF) if not SMOKE else (N >= 8),
          "h %d..%d  [%.1f s]" % (rungs[0]["h"], rungs[-1]["h"],
                                  time.time() - T0), kill="K1")
    if KILLS:
        return finish({})
    sub = [r for r in rungs if r["kz"] in w2.SUBSET]
    pres = max(r["pivres"] for r in sub) if sub else 0.0
    check("W2 WARD m > 0 on %d/%d + pivot collapse %.1e <= %.0e"
          % (sum(1 for r in rungs if r["m"] > 0), N, pres,
             w2.RES_WARD),
          all(r["m"] > 0 for r in rungs) and pres <= w2.RES_WARD,
          kill="K2")
    mm = np.array([r["m"] for r in rungs])
    mu1 = np.array([r["mu1"] for r in rungs])
    shat = mm / mu1
    s3 = (float(shat.min()), float(np.median(shat)),
          float(shat.max()))
    if not SMOKE:
        check("W3 CXLIII band shat %.4f/%.4f/%.4f ~ %s"
              % (s3 + (w2.SHAT_REF,)),
              all(abs(s3[i] - w2.SHAT_REF[i]) <= w2.SHAT_TOL
                  for i in range(3)), kill="K2")
    else:
        print("    (smoke: shat band %.4f/%.4f/%.4f -- full ward "
              "deferred)" % s3)
        check("W3 deferred in smoke (disclosed)", True)

    # ------------------------------------------------------------ E
    section("E -- classical inputs + the 4e6 extension table")
    lam_ext = core.von_mangoldt_table(w2.TAB_EXT)
    ok_pref = bool(np.array_equal(lam_ext[:core.ATOM_MAX + 1],
                                  core.LAM_TAB))
    check("E0 deep-table prefix byte-exact", ok_pref, kill="K2")
    xs = core._NN.astype(float)
    psi_c = np.cumsum(core.LAM_TAB[core._NN])
    kp = xs > 11.0
    env_true = float(np.max(np.abs(psi_c[kp] - xs[kp])
                            / np.sqrt(xs[kp])))
    check("E1 Buethe soundness on the deployed table (%.4f <= "
          "%.2f)" % (env_true, w2.BUETHE_C),
          env_true <= w2.BUETHE_C, kill="K2")
    tg0 = tail_grid(rungs[0]["D"], t_c)
    abel0 = subg.abel_upper(tg0, 1.0 / tg0[:-1] ** 2,
                            n_start=float(N_Z))
    check("E2 Abel tail base %.4e in [%.0e, %.0e] (N(T_c) = N_Z "
          "exact)" % ((abel0,) + ABEL_BAND),
          ABEL_BAND[0] <= abel0 <= ABEL_BAND[1], kill="K2")

    # ------------------------------------------------------------ X
    section("X -- the exact split reproduced (CLXXXV wards)")
    ladders = [w2.cut_ladder(r) for r in rungs]
    SP = []
    dx1 = dx3 = 0.0
    for r, lad in zip(rungs, ladders):
        row = {}
        for nc in lad:
            sp = w2.split_at(r, nc)
            if sp is None:
                continue
            row[nc] = sp
            dx1 = max(dx1, sp["dev_x1"])
            dx3 = max(dx3, sp["dev_x3"])
        SP.append(row)
    check("X1 WARD split identities on the whole ladder: max "
          "%.2e <= %.0e (CLXXXV saw 2.1e-13)"
          % (max(dx1, dx3), w2.ID_WARD),
          max(dx1, dx3) <= w2.ID_WARD, kill="K2")
    ratio_at = np.array([abs(row[r["ncB"]]["par"])
                         / max(abs(row[r["ncB"]]["t_int"]), 1e-300)
                         for r, row in zip(rungs, SP)
                         if r["ncB"] in row])
    if not SMOKE:
        check("X2 ARITH-SMALL med %.4f == %.3f (atol %.3f)"
              % (float(np.median(ratio_at)), ARITH_REF,
                 ARITH_ATOL),
              abs(float(np.median(ratio_at)) - ARITH_REF)
              <= ARITH_ATOL, kill="K2")
    else:
        print("    (smoke: ARITH med %.4f -- full ward deferred)"
              % float(np.median(ratio_at)))
        check("X2 deferred in smoke (disclosed)", True)

    # ------------------------------------------------------------ A
    section("A -- THE TRANSLATION: verified-zero reads of PARITH "
            "at the frozen cuts + heart wards")
    recon_worst = 0.0
    cont_worst = 0.0
    trans_worst = 0.0
    heart_worst = -1e18
    slack = []
    sound_bad = 0
    spots = {0, N // 2, N - 1}
    for i, (r, row) in enumerate(zip(rungs, SP)):
        tg = tail_grid(r["D"], t_c)
        abel = subg.abel_upper(tg, 1.0 / tg[:-1] ** 2,
                               n_start=float(N_Z))
        r["_abel"] = abel
        reads = {}
        for A in CUT_A:
            sp = w2.demand_at_head(r, A)
            if sp is None:
                continue
            reads[("A", A)] = sp
        spB = row.get(r["ncB"]) or w2.split_at(r, r["ncB"])
        if spB is not None:
            reads[("cB", 0)] = spB
        out = {}
        for key, sp in reads.items():
            pc = phi_cont_of(r, sp)
            par_hat, tailb = direct_read(r, sp, pc, gam, abel,
                                         s2t, inv2, inv3)
            recon_worst = max(recon_worst, recon_of(r, sp, pc))
            cont_worst = max(cont_worst, abs(pc["fend"])
                             / max(1.0, pc["fmax"]))
            if i in spots and key == ("cB", 0):
                hj = complex(-np.sum(
                    pc["J"] * np.exp(1j * 25.0 * pc["v"]))
                    / 25.0 ** 2)
                hs = hat_seg_c(pc["edges"], pc["fvals"],
                               pc["slopes"], 1j * 25.0)
                trans_worst = max(trans_worst, abs(hj - hs)
                                  / max(1.0, abs(hj)))
                tb = triv_env_pl(pc["edges"], pc["fvals"])
                if abs(pc["triv"]) > tb * (1 + 1e-9) + 1e-15:
                    cont_worst = max(cont_worst, 1.0)
            resid = sp["par"] - par_hat
            tol_a = RECON_TOL * (1.0 + abs(sp["t_int"]))
            heart_worst = max(heart_worst,
                              (abs(resid) - tailb - tol_a)
                              / max(1.0, abs(sp["t_int"])))
            slack.append(math.log10(tailb / max(abs(resid),
                                                1e-300)))
            m_cert = sp["fc"] + par_hat - tailb
            if m_cert > r["m"] * (1.0 + SOUND_TOL) + 1e-15:
                sound_bad += 1
            out[key] = dict(sp=sp, pc=pc, par_hat=par_hat,
                            tailb=tailb, resid=resid,
                            m_cert=m_cert,
                            sup_vz=abs(par_hat) + tailb)
        r["_reads"] = out
        if (i + 1) % 10 == 0:
            print("    ... %d rungs  [%.1f s]"
                  % (i + 1, time.time() - T0), flush=True)
    check("A1 continuity at the support end (worst %.1e <= %.0e "
          "scaled)" % (cont_worst, CONT_TOL),
          cont_worst <= CONT_TOL, kill="K3")
    check("A2 bookkeeping recon PARITH == phi_cont sides (worst "
          "%.1e <= %.0e scaled, no zeros)"
          % (recon_worst, RECON_TOL), recon_worst <= RECON_TOL,
          kill="K3")
    check("A3 transform ward jump == segment at gamma = 25 "
          "(worst %.1e <= %.0e)" % (trans_worst, TRANS_TOL),
          trans_worst <= TRANS_TOL, kill="K3")
    check("A4 THE HEART: |PARITH - PARITH_hat| <= TAILB on every "
          "rung x cut (worst scaled excess %.1e)" % heart_worst,
          heart_worst <= 0.0, kill="K2")
    check("A5 soundness m_cert <= m on every read (%d violations)"
          % sound_bad, sound_bad == 0, kill="K2")
    sl = np.array(slack)
    print("    heart anatomy: slack log10(TAILB/|resid|) "
          "%+.2f/%+.2f/%+.2f dex over %d reads"
          % (band(sl) + (len(sl),)))
    check("A6 heart anatomy recorded", True)

    # ------------------------------------------------------------ B
    section("B -- (a)+(b) CARRIER RETRY: phase-sensitive reads at "
            "cB and the A = %d head" % A_STR)
    CRB, CRA = [], []
    for r in rungs:
        spfB = w2.split_at(r, r["ncB"], want_pieces=True)
        CRB.append((spfB, w2.carrier_read(r, spfB, w2.OMEGA_MAX))
                   if spfB is not None else None)
        spA = w2.demand_at_head(r, A_STR)
        if spA is None:
            CRA.append(None)
            continue
        spfA = w2.split_at(r, spA["nc"], want_pieces=True)
        CRA.append((spfA, w2.carrier_read(r, spfA, w2.OMEGA_MAX))
                   if spfA is not None else None)
    # CLXXXV/CLXXXVI reproduction at cB
    jst = np.array([c[1]["j_star"] for c in CRB if c])
    trd = np.array([c[1]["tridef"] for c in CRB if c])
    nsel = np.array([int(c[1]["sel_om"].sum()) for c in CRB if c])
    sh_om = np.array([c[1]["share_om"] for c in CRB if c])
    print("    carrier band at cB: K med %d, share med %+.4f, "
          "j* med %d, TRIDEF med %.3e"
          % (int(np.median(nsel)), float(np.median(sh_om)),
             int(np.median(jst)), float(np.median(trd))))
    if not SMOKE:
        check("B1 CLXXXV carrier stats reproduced (K med %d == "
              "%d, j* med %d == %d, TRIDEF med %.2e ~ %.2e)"
              % (int(np.median(nsel)), KCAR_REF,
                 int(np.median(jst)), JSTAR_REF,
                 float(np.median(trd)), TRIDEF_REF),
              int(np.median(nsel)) == KCAR_REF
              and int(np.median(jst)) == JSTAR_REF
              and abs(float(np.median(trd)) / TRIDEF_REF - 1.0)
              <= TRIDEF_RTOL, kill="K2")
    else:
        check("B1 deferred in smoke (disclosed)", True)

    def sup_env(_r, _spf, cr, idx):
        return np.abs(cr["cj"][idx]) * cr["sup_psi"][idx]

    print("    OLD census (absolute Buethe envelopes, CLXXXVI):")
    oB = lemma_census(rungs, lambda r: CRB[rungs.index(r)],
                      sup_env, "cB")
    oA = lemma_census(rungs, lambda r: CRA[rungs.index(r)],
                      sup_env, "A=%d" % A_STR)
    if not SMOKE:
        check("B2 CLXXXVI lemma censuses reproduced (%d/%d, %d/%d"
              " == %d/%d, %d/%d; aggregates %+.2f/%+.2f ~ "
              "+%.2f/+%.2f)"
              % (oB[0], oB[1], oA[0], oA[1], LEMMA_REF[0],
                 LEMMA_REF[1], LEMMA_REF[2], LEMMA_REF[3],
                 oB[2], oA[2], AGG_REF[0], AGG_REF[1]),
              (oB[0], oB[1], oA[0], oA[1]) == LEMMA_REF
              and abs(oB[2] - AGG_REF[0]) <= AGG_ATOL
              and abs(oA[2] - AGG_REF[1]) <= AGG_ATOL, kill="K2")
    else:
        check("B2 deferred in smoke (disclosed)", True)
    # the NEW per-carrier supply
    c_heart_worst = -1e18
    c_slack = []
    c_triv_worst = 0.0
    c_trans_worst = 0.0
    sharp_all = {"cB": [], "A": []}
    NEWSUP = {"cB": {}, "A": {}}
    NEWSIG = {"cB": {}, "A": {}}
    n_cr = 0
    for i, r in enumerate(rungs):
        for tag, pack in (("cB", CRB[i]), ("A", CRA[i])):
            if pack is None:
                continue
            spf, cr = pack
            idx = np.nonzero(cr["sel_om"])[0]
            Lu = spf["Lu"]
            n0 = 1.0 / math.sqrt(Lu)
            n1 = math.sqrt(2.0 / Lu)
            s_new = np.empty(len(idx))
            that_sum = 0.0
            tb_sum = 0.0
            for jj, j in enumerate(idx):
                om = float(cr["om"][j])
                nj = n0 if j == 0 else n1
                ph, tb, _tv, tdev, twd = carrier_supply(
                    r, spf, om, nj, gam, r["_abel"], s2t, inv2,
                    inv3, lam_ext,
                    want_ward=(i in spots and jj < 2))
                c_triv_worst = max(c_triv_worst, tdev)
                c_trans_worst = max(c_trans_worst, twd)
                res = float(cr["Phi"][j]) - ph
                sc = max(1.0, abs(float(cr["Phi"][j])))
                c_heart_worst = max(c_heart_worst,
                                    (abs(res) - tb) / sc)
                c_slack.append(math.log10(
                    tb / max(abs(res), 1e-300)))
                n_cr += 1
                s_new[jj] = abs(cr["cj"][j]) * (abs(ph) + tb)
                that_sum += float(cr["cj"][j]) * ph
                tb_sum += abs(cr["cj"][j]) * tb
                s_env_j = abs(cr["cj"][j]) * cr["sup_psi"][j]
                sharp_all[tag].append(math.log10(
                    max(s_env_j, 1e-300) / max(s_new[jj],
                                               1e-300)))
            NEWSUP[tag][i] = s_new
            NEWSIG[tag][i] = (that_sum, tb_sum)
    check("B3 CARRIER HEART: |Phi_j - Phihat_j| <= TAILB_j on "
          "every carrier read (worst scaled excess %.1e, %d "
          "reads)" % (c_heart_worst, n_cr),
          c_heart_worst <= 0.0, kill="K2")
    check("B4 carrier transform + trivial-term wards (%.1e <= "
          "%.0e, %.1e <= %.0e)"
          % (c_trans_worst, CTRANS_TOL, c_triv_worst, TRIV2_TOL),
          c_trans_worst <= CTRANS_TOL
          and c_triv_worst <= TRIV2_TOL, kill="K3")
    print("    carrier heart slack med %+.2f dex"
          % float(np.median(np.array(c_slack))))
    shB = np.array(sharp_all["cB"])
    shA = np.array(sharp_all["A"])
    print("    PER-CARRIER SHARPENING delivered log10(env/new): "
          "cB %+.2f/%+.2f/%+.2f, A=%d %+.2f/%+.2f/%+.2f dex"
          % (band(shB) + (A_STR,) + band(shA)))
    print("    (the CLXXXVI demand band was +%.1f..+%.1f dex per "
          "carrier)" % (SHARP_FLOOR, SHARP_TOP))

    def sup_new(r, _spf, _cr, idx):
        i = rungs.index(r)
        tag = "A" if (CRA[i] is not None
                      and _spf is CRA[i][0]) else "cB"
        s = NEWSUP[tag].get(i)
        return s if s is not None and len(s) == len(idx) else None

    print("    NEW census (verified-zero phase-sensitive reads):")
    nB = lemma_census(rungs, lambda r: CRB[rungs.index(r)],
                      sup_new, "cB")
    nA = lemma_census(rungs, lambda r: CRA[rungs.index(r)],
                      sup_new, "A=%d" % A_STR)
    # signed aggregates (the phase-sensitive carrier route)
    sig = {"cB": [], "A": []}
    for i, r in enumerate(rungs):
        for tag, pack in (("cB", CRB[i]), ("A", CRA[i])):
            if pack is None or i not in NEWSIG[tag]:
                continue
            spf, _cr = pack
            if spf["fc"] <= 0.0:
                continue
            that_sum, tb_sum = NEWSIG[tag][i]
            sig[tag].append(math.log10(
                max(abs(that_sum) + tb_sum, 1e-300) / spf["fc"]))
    for tag, arr in sig.items():
        if arr:
            print("    SIGNED aggregate log10((|sum c_j "
                  "Phihat_j| + sum |c_j| TAILB_j)/FC) med %+.3f "
                  "dex at %s"
                  % (float(np.median(np.array(arr))),
                     tag if tag == "cB" else "A=%d" % A_STR))
    lab_b = ("LEMMA-RETRY(cB %d/%d was %d/%d, A=%d %d/%d was "
             "%d/%d) + AGG(cB %+.2f -> %+.2f, A %+.2f -> %+.2f "
             "dex)"
             % (nB[0], nB[1], LEMMA_REF[0], LEMMA_REF[1], A_STR,
                nA[0], nA[1], LEMMA_REF[2], LEMMA_REF[3],
                oB[2], nB[2], oA[2], nA[2]))
    check("B5 typed: %s" % lab_b, True)

    # ------------------------------------------------------------ C
    section("C -- (b)+(c) THE FIXED-HEAD LADDER + THE CERTIFICATE"
            " RECOMPOSED")
    print("    A atoms | FC>0 | c_req_old dex med | c_req_new "
          "dex med | signed cert m_cert > 0")
    dex_old_med = {}
    dex_new_by_A = {}
    close_by_A = {}
    for A in CUT_A:
        do, dn, npos, ncl, ntot = [], [], 0, 0, 0
        for r in rungs:
            rd = r["_reads"].get(("A", A))
            if rd is None:
                continue
            ntot += 1
            sp = rd["sp"]
            if rd["m_cert"] > 0.0:
                ncl += 1
            if sp["fc"] > 0:
                npos += 1
                do.append(sp["sup"] / sp["fc"])
                dn.append(rd["sup_vz"] / sp["fc"])
        if not ntot:
            continue
        d_o = math.log10(float(np.median(do))) if do else float(
            "nan")
        d_n = math.log10(float(np.median(dn))) if dn else float(
            "nan")
        dex_old_med[A] = d_o
        dex_new_by_A[A] = d_n
        close_by_A[A] = (ncl, ntot)
        print("    %-7d | %2d/%2d | %+16.3f | %+16.3f | %d/%d"
              % (A, npos, ntot, d_o, d_n, ncl, ntot))
    if not SMOKE:
        ok_dex = all(abs(dex_old_med.get(A, 1e9) - DEX_OLD_REF[A])
                     <= DEX_ATOL for A in DEX_OLD_REF)
        check("C1 CLXXXV fixed-head demand reproduced (A = "
              "9/12/200/400 dex %+.3f/%+.3f/%+.3f/%+.3f ~ refs)"
              % tuple(dex_old_med.get(A, float("nan"))
                      for A in (9, 12, 200, 400)),
              ok_dex, kill="K2")
    else:
        check("C1 deferred in smoke (disclosed)", True)
    # UNCOND-CLOSE reproduction (Buethe route)
    ncs = [w2.close_cut(r) for r in rungs]
    n_close = sum(1 for x in ncs if x is not None)
    hafr = []
    for x, r in zip(ncs, rungs):
        if x is None:
            hafr.append(np.nan)
            continue
        i = int(np.searchsorted(r["nn"], x, side="right"))
        hafr.append(i / r["natom"])
    hafr = np.array(hafr)
    if not SMOKE:
        check("C2 CLXXXV UNCOND-CLOSES reproduced (%d/%d, head "
              "frac med %.4f ~ %.4f)"
              % (n_close, N, float(np.nanmedian(hafr)), HAFR_REF),
              n_close == N
              and abs(float(np.nanmedian(hafr)) - HAFR_REF)
              <= HAFR_ATOL, kill="K2")
    else:
        print("    (smoke: UNCOND closes %d/%d, hafr med %.4f -- "
              "ward deferred)"
              % (n_close, N, float(np.nanmedian(hafr))))
        check("C2 deferred in smoke (disclosed)", True)
    # THE CERTIFICATE: per-rung minimal certifying head
    min_head = []
    head_frac = []
    cert_marg = []
    tb_over_m = []
    need_n = []
    n_any = 0
    print("\n    per-rung certificate: minimal head A* with "
          "m_cert > 0 on the frozen ladder; the blocker in dex:")
    print("      kz    h     m         TAILB(cB)  TAILB/m dex  "
          "A*     zeros needed (anatomy)")
    for r in rungs:
        best = None
        for A in CUT_A:
            rd = r["_reads"].get(("A", A))
            if rd is not None and rd["m_cert"] > 0.0:
                best = A
                head_frac.append(A / r["natom"])
                cert_marg.append(math.log10(rd["m_cert"]
                                            / r["m"]))
                break
        rdB = r["_reads"].get(("cB", 0))
        if best is None and rdB is not None \
                and rdB["m_cert"] > 0.0:
            best = "cB"
            head_frac.append(rdB["sp"]["natom_head"]
                             / r["natom"])
            cert_marg.append(math.log10(rdB["m_cert"] / r["m"]))
        if best is not None:
            n_any += 1
        min_head.append(best)
        if rdB is not None:
            tb_over_m.append(math.log10(rdB["tailb"] / r["m"]))
            t_req, n_req = zeros_needed(
                r["m"], rdB["pc"]["sd"])
            need_n.append(n_req)
            if r["kz"] in w2.SUBSET or len(min_head) <= 2:
                print("      %-5d %-5d %.3e %.3e  %+.2f       "
                      "%-5s  T ~ %.2e, N ~ %.2e"
                      % (r["kz"], r["h"], r["m"], rdB["tailb"],
                         tb_over_m[-1],
                         str(best) if best else "none",
                         t_req, n_req))
    tbm = np.array(tb_over_m)
    nn_arr = np.array(need_n)
    print("    SURFACE census: signed certificate closes on "
          "%d/%d rungs at N_Z = %d" % (n_any, N, N_Z))
    if head_frac:
        print("    MINIMAL CERTIFYING HEAD FRACTION (closing "
              "rungs): %.4f/%.4f/%.4f of the atoms (CLXXXV "
              "Buethe route needed med %.3f); certified margin "
              "log10(m_cert/m) med %+.2f dex"
              % (band(np.array(head_frac))
                 + (HAFR_REF, float(np.median(
                     np.array(cert_marg))))))
    print("    the blocker log10(TAILB/m): %+.2f/%+.2f/%+.2f dex"
          % band(tbm))
    lev = tuple(int(np.sum(nn_arr <= lv)) for lv in NEED_LEVELS)
    print("    ZEROS-NEEDED (anatomy, main-term N(T)): med "
          "%.2e / max %.2e verified zeros; closable with N <= "
          "1e5/1e6/1e7 on %d/%d/%d of %d rungs"
          % (float(np.median(nn_arr)), float(np.max(nn_arr)),
             lev[0], lev[1], lev[2], len(nn_arr)))
    if n_any == N and not SMOKE:
        print("\n  " + "*" * 72)
        print("  THE RECOMPOSED W2 RESULT (finite, per-rung, "
              "direction-conditional):")
        print("  every deployed rung certifies m > 0 from HEAD + "
              "TCONT + verified-zero")
        print("  PARITH read; see the census above.  NO RH claim.")
        print("  " + "*" * 72)
    check("C3 certificate census recorded", True)

    # ------------------------------------------------------------ F
    section("F -- the deep block (FLOAT-LEVEL declared, CLXXXV "
            "frame)")
    NNx = np.nonzero(lam_ext > 0.0)[0]
    EXT = dict(lam=lam_ext, NN=NNx, U=np.log(NNx.astype(float)),
               MU=2.0 * lam_ext[NNx] / np.sqrt(NNx.astype(float)))
    EXT["G"] = np.diff(EXT["U"])
    new_kz = []
    for kz in range(2, min(w2.KZ_SCAN_MAX, len(EXT["NN"]) - 2)):
        a_ = float(EXT["U"][kz])
        Xk = math.exp(2.0 * a_)
        if Xk > w2.TAB_EXT:
            break
        if Xk <= core.ATOM_MAX:
            continue
        D_k = 0.5 * float(EXT["G"][kz]) / float(core.NU_MAIN)
        Mk = int(math.ceil(a_ / D_k - 1.0e-9)) + 1
        if Mk % 2:
            Mk += 1
        if not (w2.H_HOLD[0] <= Mk // 2 <= w2.H_HOLD[1]):
            continue
        new_kz.append(kz)
    deep_rows = []
    if new_kz:
        order = sorted(new_kz)
        pick = sorted(set(int(round(t)) for t in
                          np.linspace(0, len(order) - 1,
                                      min(DEEP_MAX, len(order)))))
        for ii in pick:
            r = w2.build_rung(order[ii], ext=EXT)
            if r is not None:
                deep_rows.append(r)
        deep_rows.sort(key=lambda r: r["h"])
    check("F0 deep census %d %s" % (len(deep_rows),
                                    "== 8" if not SMOKE
                                    else "(smoke)"),
          len(deep_rows) == DEEP_MAX, kill="K1" if not SMOKE
          else None)
    d_heart = -1e18
    d_recon = 0.0
    d_dexo, d_dexn, d_tbm, d_close, d_h = [], [], [], 0, []
    d_hafr = []
    for r in deep_rows:
        tg = tail_grid(r["D"], t_c)
        abel = subg.abel_upper(tg, 1.0 / tg[:-1] ** 2,
                               n_start=float(N_Z))
        spA = w2.demand_at_head(r, A_STR)
        spB = w2.split_at(r, r["ncB"])
        closed = False
        for tag, sp in (("A", spA), ("cB", spB)):
            if sp is None:
                continue
            pc = phi_cont_of(r, sp)
            par_hat, tailb = direct_read(r, sp, pc, gam, abel,
                                         s2t, inv2, inv3)
            d_recon = max(d_recon, recon_of(r, sp, pc))
            resid = sp["par"] - par_hat
            tol_a = RECON_TOL * (1.0 + abs(sp["t_int"]))
            d_heart = max(d_heart, (abs(resid) - tailb - tol_a)
                          / max(1.0, abs(sp["t_int"])))
            m_cert = sp["fc"] + par_hat - tailb
            closed = closed or m_cert > 0.0
            if tag == "A":
                if sp["fc"] > 0:
                    d_dexo.append(math.log10(sp["sup"]
                                             / sp["fc"]))
                    d_dexn.append(math.log10(
                        (abs(par_hat) + tailb) / sp["fc"]))
                else:
                    d_dexo.append(np.nan)
                    d_dexn.append(np.nan)
                d_h.append(float(r["h"]))
            else:
                d_tbm.append(math.log10(tailb / r["m"]))
        if closed:
            d_close += 1
        x = w2.close_cut(r)
        d_hafr.append((int(np.searchsorted(r["nn"], x,
                                           side="right"))
                       / r["natom"]) if x is not None else np.nan)
    if deep_rows:
        print("    deep: heart worst excess %.1e, recon worst "
              "%.1e; certificate closes %d/%d; TAILB/m "
              "%+.2f/%+.2f/%+.2f dex"
              % ((d_heart, d_recon, d_close, len(deep_rows))
                 + band(np.array(d_tbm))))
        check("F1 deep heart + recon wards", d_heart <= 0.0
              and d_recon <= RECON_TOL, kill="K2")
        if not SMOKE:
            check("F2 CLXXXV deep UNCOND reproduced (closes %d/%d,"
                  " head frac med %.4f ~ %.3f)"
                  % (sum(1 for x in d_hafr if np.isfinite(x)),
                     len(deep_rows),
                     float(np.nanmedian(np.array(d_hafr))),
                     HAFR_DEEP_REF),
                  sum(1 for x in d_hafr if np.isfinite(x))
                  == len(deep_rows)
                  and abs(float(np.nanmedian(np.array(d_hafr)))
                          - HAFR_DEEP_REF) <= HAFR_ATOL,
                  kill="K2")
        else:
            check("F2 deferred in smoke (disclosed)", True)
    else:
        check("F1 no deep rows (disclosed)", SMOKE, kill="K1")
        check("F2 no deep rows (disclosed)", SMOKE)

    # ------------------------------------------------------------ D
    section("D -- (d) THE HEAD-SIZE LAW RETEST + the residual "
            "hardness law")
    hh = np.log(np.array([float(r["h"]) for r in rungs]))
    surf_o, surf_n = [], []
    for r in rungs:
        rd = r["_reads"].get(("A", A_STR))
        if rd is None or rd["sp"]["fc"] <= 0:
            surf_o.append(np.nan)
            surf_n.append(np.nan)
            continue
        surf_o.append(math.log10(rd["sp"]["sup"]
                                 / rd["sp"]["fc"]))
        surf_n.append(math.log10(rd["sup_vz"] / rd["sp"]["fc"]))
    xj = np.concatenate([hh, np.log(np.array(d_h))]) \
        if d_h else hh
    yo = np.concatenate([np.array(surf_o), np.array(d_dexo)]) \
        if d_h else np.array(surf_o)
    yn = np.concatenate([np.array(surf_n), np.array(d_dexn)]) \
        if d_h else np.array(surf_n)
    b_o, se_o, r2_o = w2.jack_slope(xj, yo)
    b_n, se_n, r2_n = w2.jack_slope(xj, yn)
    print("    OLD fixed-head demand law (A = %d, joint): %+.3f "
          "dex/log h (2SE %.3f, R^2 %.3f) -- CLXXXV +0.191"
          % (A_STR, b_o, 2 * se_o, r2_o))
    print("    NEW fixed-head demand law (A = %d, joint): %+.3f "
          "dex/log h (2SE %.3f, R^2 %.3f)"
          % (A_STR, b_n, 2 * se_n, r2_n))
    if not SMOKE:
        check("D1 CLXXXV head-size law reproduced (%+.3f ~ "
              "+%.3f, atol %.2f)" % (b_o, SLOPE_OLD_REF,
                                     SLOPE_ATOL),
              abs(b_o - SLOPE_OLD_REF) <= SLOPE_ATOL, kill="K2")
    else:
        check("D1 deferred in smoke (disclosed)", True)
    xt = np.concatenate([hh, np.log(np.array(
        [float(r["h"]) for r in deep_rows]))]) if deep_rows \
        else hh
    yt = np.concatenate([tbm, np.array(d_tbm)]) if deep_rows \
        else tbm
    b_t, se_t, r2_t = w2.jack_slope(xt, yt)
    print("    RESIDUAL TAIL-PRICE LAW: log10(TAILB/m) = %+.3f "
          "dex/log h (2SE %.3f, R^2 %.3f) -- the hardness now "
          "isolated in the tail budget" % (b_t, 2 * se_t, r2_t))
    # CS / UNIF-PATH re-read at NC-OPT (CLXXXV verbatim)
    uloss = []
    for r, lad in zip(rungs, ladders):
        o = w2.nc_opt(r, lad)
        if o[2] is not None:
            uloss.append(o[2]["sup_unif"] / max(o[2]["sup"],
                                                1e-300))
    uloss = np.array(uloss)
    print("    UNIF-PATH re-read: L1 -> L2 Cauchy-Schwarz cost "
          "med %.4f (CLXXXV 1.0518) -- envelope-side algebra, "
          "UNCHANGED by the supply;" % float(np.median(uloss)))
    print("      the verified-zero read is DIRECTION-CONDITIONAL "
          "data; the Loewner/uniformity step is NOT taken here.")
    if not SMOKE:
        check("D2 CLXXXV CS cost reproduced (med %.4f ~ %.4f)"
              % (float(np.median(uloss)), CS_REF),
              abs(float(np.median(uloss)) - CS_REF) <= CS_ATOL,
              kill="K2")
    else:
        check("D2 deferred in smoke (disclosed)", True)

    # ------------------------------------------------------------ S
    section("S -- tau screens (CLXXXV jackknife definitions)")
    lm = np.log(mm)
    scr = []
    y12 = []
    for r in rungs:
        rd = r["_reads"].get(("A", 12))
        y12.append(math.log10(rd["sup_vz"] / rd["sp"]["fc"])
                   if rd is not None and rd["sp"]["fc"] > 0
                   else np.nan)
    for nm, yy in (("c_req_new dex A=%d" % A_STR,
                    np.array(surf_n)),
                   ("c_req_new dex A=12", np.array(y12)),
                   ("log10 TAILB/m at cB", tbm)):
        lab, tag = w2.screen_label(nm, lm, yy)
        scr.append((nm, tag))
        print("    %s" % lab)
    check("S1 screens recorded", True)

    # ------------------------------------------------------------ M
    section("M -- controls (must fire)")
    lam_sm = np.array([r["lam_sm"] for r in rungs])
    check("M1 smooth world breaks the wall on %d/%d (max %+.1e)"
          % (int(np.sum(lam_sm < 0)), N, float(lam_sm.max())),
          bool(np.all(lam_sm < 0)), kill="K2")
    r9 = next((r for r in rungs if r["kz"] == CTRL_KZ), None)
    if r9 is None:
        check("M2 no control rung (kz %d)" % CTRL_KZ, False,
              kill="K1")
        return finish({})
    NE = int(math.floor(math.exp(2.0 * r9["alpha"]))) + 1
    lamE = w2.lambda_eps(NE)
    nz = np.nonzero(np.abs(lamE) > 1e-12)[0]
    cE = (np.log(nz.astype(float)),
          2.0 * lamE[nz] / np.sqrt(nz.astype(float)))
    rE = w2.build_rung(CTRL_KZ, comb=cE)
    rS = w2.build_rung(CTRL_KZ, scramble_seed=1)
    check("M2 Epstein + scramble break lam_min at kz %d "
          "(%+.1e, %+.1e)" % (CTRL_KZ, rE["m"], rS["m"]),
          rE["m"] < 0 and rS["m"] < 0, kill="K2")
    # C-i: the scrambled comb must break the exact prime-side ward
    fired = 0
    tried = 0
    for key in (("cB", 0), ("A", A_STR)):
        rd = r9["_reads"].get(key)
        if rd is None:
            continue
        tried += 1
        sp = rd["sp"]
        keep = rS["uu"] > math.log(sp["nc"]) + 1e-12
        t_scr = float(np.dot(
            np.asarray(rS["mu"], float)[keep],
            w2.q_read(r9["Wv"], rS["uu"][keep], r9["D"],
                      r9["M"])))
        par_scr = t_scr - sp["tcont"]
        exc = abs(par_scr - rd["par_hat"]) / rd["tailb"]
        print("    scramble read at %s: |PARITH_scr - "
              "PARITH_hat| / TAILB = %.1e -> %s"
              % (str(key), exc, "FIRES" if exc > 1 else "silent"))
        if exc > 1.0:
            fired += 1
    check("M3 CONTROL C-i: scramble breaks the heart ward on "
          "%d/%d control cuts" % (fired, tried),
          tried >= 1 and fired == tried, kill="K2")
    # C-ii: the off-line impostor
    rd = r9["_reads"][("cB", 0)]
    pc = rd["pc"]
    g1 = float(gam[0])
    on_pair = 4.0 * float((-np.sum(
        pc["J"] * np.exp(1j * g1 * pc["v"])) / g1 ** 2).real)
    dlt = IMP_BETA - 0.5
    quad = 4.0 * (hat_seg_c(pc["edges"], pc["fvals"],
                            pc["slopes"], dlt + 1j * g1).real
                  + hat_seg_c(pc["edges"], pc["fvals"],
                              pc["slopes"], -dlt + 1j * g1).real)
    shift = abs((-quad) - (-on_pair))
    ratio = shift / max(abs(rd["resid"]), 1e-300)
    check("M4 CONTROL C-ii: off-line impostor (gamma_1 -> beta = "
          "%.2f) shifts PARITH_hat by %.4f = %.1e x the genuine "
          "residual (>= %.0f)"
          % (IMP_BETA, shift, ratio, IMP_RATIO_MIN),
          ratio >= IMP_RATIO_MIN, kill="K2")

    # ------------------------------------------------------ verdicts
    v1 = ("CURRENCY-MATCHED(recon %.1e, heart worst %.1e, slack "
          "med %+.2f dex over %d + %d carrier reads)"
          % (max(recon_worst, d_recon),
             max(heart_worst, d_heart), float(np.median(sl)),
             len(sl), n_cr))
    med_sharp = float(np.median(shA)) if len(shA) else float(
        "nan")
    if med_sharp >= SHARP_FLOOR:
        v2 = ("SHARPENING-DELIVERED(med %+.2f dex at A=%d vs "
              "demand +%.1f..+%.1f; lemma retry cB %d/%d, A "
              "%d/%d; aggregate %+.2f -> %+.2f dex)"
              % (med_sharp, A_STR, SHARP_FLOOR, SHARP_TOP,
                 nB[0], nB[1], nA[0], nA[1], oA[2], nA[2]))
    else:
        v2 = "SHARPENING-SHORT(med %+.2f dex < +%.2f)" \
            % (med_sharp, SHARP_FLOOR)
    n_tot_cert = n_any + d_close
    if n_tot_cert > 0:
        fr = [(A if A != "cB" else 99) for A in min_head
              if A is not None]
        v3 = ("W2VZ-CLOSES(%d/%d surface + %d/%d deep; minimal "
              "head A* med %s = head fraction med %.4f, was "
              "0.953; open rungs tail-priced: TAILB/m max %+.2f "
              "dex, zeros needed max %.1e)"
              % (n_any, N, d_close, max(len(deep_rows), 1),
                 int(np.median(fr)) if fr else "-",
                 float(np.median(np.array(head_frac)))
                 if head_frac else float("nan"),
                 float(np.max(np.concatenate(
                     [tbm, np.array(d_tbm)]) if d_tbm else tbm)),
                 float(np.max(nn_arr))))
    else:
        v3 = ("W2VZ-TAIL-PRICED(0 closed at N_Z = %d; "
              "log10(TAILB/m) %+.2f/%+.2f/%+.2f dex; zeros "
              "needed med %.1e / max %.1e, closable at N <= "
              "1e5/1e6/1e7 on %d/%d/%d of %d)"
              % ((N_Z,) + band(np.concatenate(
                  [tbm, np.array(d_tbm)]) if d_tbm else tbm)
                 + (float(np.median(nn_arr)),
                    float(np.max(nn_arr)), lev[0], lev[1],
                    lev[2], len(nn_arr))))
    if abs(b_n) <= TREND_FLAT:
        v4 = ("HEADLAW-COLLAPSED(new %+.3f dex/log h, was "
              "%+.3f: the growth was envelope looseness) + "
              "TAILLAW(%+.3f dex/log h isolated)"
              % (b_n, b_o, b_t))
    elif b_n >= TREND_FLAT:
        v4 = "HEADLAW-PERSISTS(%+.3f, was %+.3f) + TAILLAW(" \
            "%+.3f)" % (b_n, b_o, b_t)
    else:
        v4 = "HEADLAW-REVERSED(%+.3f, was %+.3f) + TAILLAW(" \
            "%+.3f)" % (b_n, b_o, b_t)
    if fired == tried and tried >= 1 and ratio >= IMP_RATIO_MIN:
        v5 = ("DISCRIMINATION-FIRES(scramble %d/%d, impostor "
              "%.0e x, smooth %d/%d, Epstein+scramble lam < 0) "
              "+ SCREENS(%s)"
              % (fired, tried, ratio, int(np.sum(lam_sm < 0)), N,
                 ", ".join("%s %s" % ab for ab in scr)))
    else:
        v5 = "DISCRIMINATION-UNRESOLVED(scr %d/%d, imp %.1f)" \
            % (fired, tried, ratio)
    check("V1 typed: %s" % v1, True)
    check("V2 typed: %s" % v2, True)
    check("V3 typed: %s" % v3, True)
    check("V4 typed: %s" % v4, True)
    check("V5 typed: %s" % v5, True)
    return finish(dict(v1=v1, v2=v2, v3=v3, v4=v4, v5=v5))


if __name__ == "__main__":
    raise SystemExit(main())
