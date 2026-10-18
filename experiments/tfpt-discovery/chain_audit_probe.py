#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""chain_audit_probe -- PRIME.COFINAL.CHAINAUDIT.01
(EXPLORATION ONLY, experiments/.  NO RH claim, NO counterexample
claim, NO all-h statement.  2026-08-13.)

THE ARBITER MEASUREMENT.  CCCXV replicated the CCCVII case-D cells on
THREE independent builds and found CERTIFIED POSITIVE enclosures at
9447 and 9535 AND at the case-B cells 8677 and 9023 -- in direct sign
conflict with the chain-based route of CCXCIX / CCCV / CCCVII /
CCCXVII (raw tau and the metric-corrected tau_ideal_ub both negative
there).  The ONE object present in the negative route and absent from
all three replication paths is the LANCZOS CHAIN, and CCCVII itself
named the chain-column REPRESENTATION accuracy as its open scope edge
(indirect reads only: max_k |diag(O)_k - 1| <= 4.80e-14, chain growth
<= 7.92e+02).  This probe (a) LOCATES the discrepancy inside the chain
route stage by stage, (b) RE-ADJUDICATES the entire deep NEGA field
with the Weil-kernel-direct method as arbiter, and (c) states the
chain route's validity domain for every prior result that consumed it.

THE TWO ROUTES, WRITTEN OUT BEFORE ANY MEASUREMENT (all of it exact
algebra of the deployed pipeline; no new mathematics).

 (0) THE SHARED OBJECT.  A cell is (kz, alpha = u_kz, M, D =
     2 alpha / M, h = M/2).  The deployed lag profile is
        c_r = A(rD, D) + c^atom_r,  r = 0..M-1,
     A the archimedean Weil kernel (core.arch_lags) and
     c^atom the T115 tent load of the prime-power comb
     (core.atom_lags_at).  Both routes consume THE SAME c.  The
     symmetric extension to L = 2M - 2 and d = Re FFT(c^sym) are
     shared.  The signed masses on the M Chebyshev-Lobatto nodes
     x_i = cos(theta_i), theta_i = pi i/(M-1), are
        W_i = eps_i d_i 4 sin^2(theta_i/2) / (2L),  eps_0 =
        eps_{M-1} = 1 else 2,
     mu_+ = the W_i > 0 part (nodes xs, masses ws), mu_- = the
     |W_i| of the W_i < 0 part (nodes ys, masses vs).

 (I) THE CHAIN ROUTE (under audit).  A reorthogonalized Lanczos chain
     on (xs, ws) produces (al, be, m0); the mu_+-orthonormal
     polynomials p_k are EVALUATED at the negative-arm nodes by the
     three-term recurrence, P[j,k] = p_k(y_j) (ob.eval_chain), and
        A_wall = I - sqrt(V) P P^T sqrt(V),   tau = lam_min(A_wall).
     CCCVII's metric correction takes the bad mode z of A_wall,
     c = P^T sqrt(V) z, lam = 1 - tau = |c|^2, d = int q^2 dmu_+ -
     |c|^2 with q = sum_k c_k p_k evaluated by the SAME recurrence at
     the POSITIVE nodes, and reports the EXACT identity
        R_ideal = lam^2 / (lam + d),  tau_ideal_ub = 1 - R_ideal
                >= tau_ideal.
     Everything in this route passes through the evaluated chain
     columns.

 (II) THE ARBITER (CCCXV PATH 3, immune by construction).  Because
     the chain columns are a triangular degree-graded family,
     span{p_0..p_{h-1}} IS the degree-<h polynomial space, so the
     IDEAL wall scalar is BASIS-FREE,
        tau_ideal = 1 - sup_{deg q < h} int q^2 dmu_- / int q^2 dmu_+
                  = lam_min(Omega, O),
        O[m,m'] = int T_m T_m' dmu_+, H[m,m'] = int T_m T_m' dmu_-,
        Omega = O - H,  T_m the Chebyshev polynomials,
     and Omega is a TOEPLITZ-PLUS-HANKEL matrix of the lag profile
     ALONE:
        Omega[m,m'] = (G_{m+m'} + G_{|m-m'|}) / 2,
        G_r = c_r - (c_{r+1} + c_{|r-1|}) / 2,
     with no FFT, no folding, no quadrature, NO CHAIN and no arm
     split.  Its bottom eigenvector is the extremal witness, its
     exact-sign Bunch-Kaufman block inertia (2x2 determinant/trace
     signs in exact rational arithmetic on the dyadic float64
     entries) decides definiteness, and the decisive scalar
        Q[q] = int q^2 dmu_+ - int q^2 dmu_- = (1/2) sum_r phi_r c_r,
        phi = the cosine coefficients of 4 sin^2(theta/2) q(cos
              theta)^2,
     is contracted with exactly-rounded fsum under OUTWARD rounding.
     The honest asymmetry of CCCVII/CCCXV is inherited verbatim: a
     NEGATIVE certified enclosure is a WITNESS; a POSITIVE one is
     only "no witness found on this instrument".

 (III) THE THIRD REPRESENTATION, the instrument of this probe.  The
     SAME polynomials p_k also have an exact CHEBYSHEV COEFFICIENT
     representation, obtained by running the identical three-term
     recurrence in COEFFICIENT space (multiplication by x is exact in
     the T-basis: x T_m = (T_{m+1} + T_{|m-1|})/2):
        A_0 = e_0 / sqrt(m0),  A_1 = (x A_0 - al_0 A_0) / be_0,
        A_{k+1} = (x A_k - al_k A_k - be_{k-1} A_{k-1}) / be_k.
     ROUTE A = the deployed node-space recurrence (ob.eval_chain).
     ROUTE B = these coefficients, evaluated at the nodes by ONE
     length-L FFT.  ROUTE C = the SAME node-space recurrence in
     MP_DPS-digit mpmath arithmetic on the EXACTLY converted float64
     (al, be, m0) at a small node sample -- the TRUTH for the
     polynomials the chain defines, and the referee that decides
     which of A / B is the accurate representation.  This is the
     measurement CCCVII could not make and named as its open edge.

THE FIVE-STAGE INSTRUMENT (per audited cell).
 S1 THE INPUT.  lag profile, d = Re FFT(c^sym), the two arms and the
    node accounting, chain route against arbiter route.  Expected
    BITWISE / few-ulp; anything else is a WARD kill and the audit
    stops there.
 S2 THE BASIS.  per-degree representation error of the chain columns:
    max over the sampled nodes of |p_k(ROUTE A) - p_k(ROUTE C)| and
    |p_k(ROUTE B) - p_k(ROUTE C)|, absolute and relative to
    max_i |p_k|, on BOTH arms, printed as a per-decile table with the
    argmax degree.  WHERE does it blow up, and how does it relate to
    the chain growth?
 S3 THE WITNESS.  the chain's own coefficient vector c (route A)
    against its route-B recomputation c_B = A^T m with the moment
    vector m_m = sum_j sqrt(v_j) z_j T_m(y_j) (one DCT-I of the
    weighted bad mode).  Then the polynomial q = sum_k c_k p_k, whose
    Chebyshev coefficients a = sum_k c_k A_k are accumulated in the
    same coefficient pass, is evaluated at BOTH arms by FFT, and the
    NODE-VALUE deviation against the chain's own qv = P c is the
    representation error AT THE WITNESS.  The internal CANCELLATION
    of both expansions (sum_k |c_k p_k| / |sum_k c_k p_k|) is
    printed: it is the amplification factor of the whole route.
 S4 THE GRAM.  the two arm integrals at the SAME witness, computed
    (i) by the chain's node values and (ii) by the polynomial's node
    values, plus (iii) the certified kernel contraction
    (1/2) sum_r phi_r c_r and (iv) the Toeplitz-Hankel coordinate
    sum_r G_r b_r.  The entrywise Gram profile is read through the
    diag(O) census per sampled degree (chain versus route B) and
    through the random metric probe ||(O - I) r|| on both routes.
 S5 THE SCALAR.  both signs reproduced, then explained: the chain's
    tau and tau_ideal_ub against the arbiter's certified Q[q] at the
    SAME polynomial and against lam_min(Omega_weil) with its exact
    block inertia.  The stage that carries the flip is NAMED.

THE FIELD RE-ADJUDICATION (mission b).  Every cell that was ever read
NEGA or witness-NEGA gets a PATH-3 arbiter build with exact inertia:
the CCXCIX holes 6197 / 6247, the CCCV band 8003 / 8677 / 9023 /
9535, the CCCVII/CCCXVII witness cells 7958 / 8642 / 8677 / 9023 /
9447 / 9535, plus the raw-legal ladder anchors 8204 / 8629 as
positive controls.  Per cell: lam_min(Omega_weil), n_neg of the exact
block inertia, the outward-rounded Q at the extremal witness, the
tau-scale read Q / D_+ and the verdict DIRECT-POS(no witness found) /
DIRECT-NEG(certified witness) / DIRECT-STRADDLE.

THE INSTRUMENT VERDICT (mission c).  The chain route's decisive
scalars are re-priced with the MEASURED representation error and the
h-dependence is read across the built chain cells (a shallow TIE
anchor, two mid cells and the two case-D cells): up to which h, and
up to which chain growth / cancellation, is the chain route
sign-reliable at the 1e-10 scale?  Which earlier verdicts consumed a
DEEP chain read (and are therefore affected) and which consumed only
ENTRY data plus certified LDL floors (and are therefore untouched)?

FROZEN PROTOCOL.
 S0 firewall AST scan (banned zetazero / zetazeros / nzeros /
    primerange / isprime / primepi / nextprime / prevprime /
    factorint / primefactors); AC scan: the READER functions
    (e1_quad, e3_kernel, e3_th, e3_dense, node_values, cheb_coeffs,
    coef_dev, omega_weil_rows, chain_pass_values,
    chain_pass_project, chain_sample_values, cheb_pass, xmul,
    mp_chain_dev, moment_transform, arm_sums, diag_o_sample) see
    nodes, weights, entries, coefficients, recurrence data and
    frozen constants only -- no eigensolver, no inverse, no tau.
 T  the atom table to TAB2 = 1.6e7, warded BITWISE against the
    deployed 4e6 EXT prefix and against core.von_mangoldt_table.
 D  the deep census (deployed frame formula verbatim); gates: 587
    cells, h max 65051, all frozen priority keys present.
 CAL a shallow TIE cell (h ~ 878): the deployed chain builder AND
    the arbiter on the same window, with (a) the (II) Weil-kernel
    identity Omega_weil == Omega_quad entrywise, (b) the arm tie
    between ob.folded_measure_full and the arbiter's node frame,
    (c) ROUTE A == ROUTE B == ROUTE C at machine precision, (d) the
    chain tau tying the arbiter's lam_min(Omega, O) in sign and to
    CAL_RTOL, (e) the certified evaluators agreeing on one witness.
    A shallow cell is where the chain is KNOWN good (CCCXV measured
    rtol 2.85e-06 at h 878), so CAL calibrates the instrument
    instead of assuming it.
 G  the reproduction gates.  G1 THE ARBITER CALIBRATION: the CCCXV
    positive enclosures on the four shared cells 9447 / 9535 / 8677 /
    9023 (n_neg = 0, lam_min(Omega_weil) > 0, tau-scale read
    positive, the two printed lam_min values inside ARB_RTOL).  G2
    THE CHAIN REPRODUCTION: the CCCVII tau, d and tau_ideal_ub at
    9447 and 9535 inside REPRO_RTOL with negA = 1.  BOTH SIGNS MUST
    BE REPRODUCED BEFORE EITHER IS EXPLAINED.
 X  controls-must-fire: X1 SCRAMBLE and X2 SMOOTH worlds at the
    deepest audited cell must destroy the arbiter's wall scalar; XW
    the certified enclosure must FIRE on a DOCTORED lag entry
    (DOPE = 1e-2, pass threshold shift > 10 half-widths); XM every
    declared numerical half-width model must hold on a DISJOINT
    re-measurement at EVERY built cell (CCCXV A14 discipline).
 S  screens: the CCXLVII tau-relocation and CCXVII c_h screens are
    VACUOUS-BY-CONSTRUCTION (no step formations of record, no fitted
    level -- an instrument audit only) and are typed as such.

VERDICT (frozen enums).
 (a) THE DEFECT.  CHAIN-DEFECT-LOCATED(stage; magnitude) iff BOTH
     signs are reproduced AND a named stage carries a deviation that
     exceeds the decisive scale; CHAIN-VALIDATED iff the chain route
     reproduces the arbiter at the audited cells (which would refute
     this mission's premise and must be reported as such);
     AUDIT-UNRESOLVED iff the reproduced signs cannot be separated by
     any measured stage.
 (b) THE FIELD.  FIELD-ALL-DIRECT-POSITIVE(n) iff every former-NEGA
     cell reads n_neg = 0 with a positive certified enclosure;
     FIELD-MIXED(list) otherwise, with the surviving negatives typed
     individually.
 (c) THE INSTRUMENT.  INSTRUMENT-VALID-TO(h_ok, growth_ok) --
     the deepest built chain cell whose re-priced decisive scalar
     still excludes zero -- plus the AFFECTED / UNTOUCHED partition
     of the prior record.
KILLS: K1 pipeline -> PIPELINE-BROKEN; K2 ward/identity ->
WARD-BROKEN; K3 calibration -> CALIBRATION-BROKEN; K4 a required
control silent -> CONTROL-SILENT; K5 a reproduction gate ->
REPRO-BROKEN (the audit refuses to explain a sign it cannot
reproduce).

FROZEN BARS.  TAB2 = 1.6e7; EXT_DEPLOYED = 4e6; KZ2_MAX = 1200;
CENSUS_N_REF = 587; CENSUS_HMAX_REF = 65051; NU_MAIN = 4;
H_MIN = 128; HCAP = 1450; N_ATOM_MIN = 40; MP_DPS = 50;
MP_NODES = 10 (per arm, deterministic: the extremes, the bad mode's
top seats and a seeded sample); DEG_PROBE = 24 (sampled degrees,
log-spaced); FFT_PROBE = 256; FFT_WARD2 = 96; ETA_SAFE = 8;
COEF_PROBE = 24; COEF_SAFE = 8; SIGN_MARGIN = 1 (a certified
enclosure decides a sign exactly when it excludes zero; the margin
|Q| / halfwidth is printed for every read); CAL_RTOL = 1e-3;
IDENT_BAR = 1e-11; ARM_ULP = 8 (the arm-tie summation-order floor);
REPRO_RTOL = 2e-3 (the CCCVII chain reproduction, CCCXVII bar
verbatim); ARB_RTOL = 5e-2 (the CCCXV arbiter reproduction: those
values are RATIOS of 1e-15-scale scalars printed to 7 digits, and
the decisive part of G1 is the SIGN and n_neg = 0, not the digits);
TAU_NOISE = 5e-12; IDEAL_NOISE = 1e-12; LOC_ITERS = 30; NREF = 2;
OPROBE_SEED = 7; SCR_SEED = 1; DOPE = 1e-2; SAMP_SEED = 11;
CAL_TGT = 900; VAL_TGT = (2012, 3948, 5500, 7200); REPR_SAFE = 8;
BUILD_CAP_S = 2500;
GUARD_FAC = 1.05; COST_CHAIN = 4.6e-10 s (CCCVII envelope);
COST_ARB = 1.3e-10 s (CCCXV envelope).
Smoke: PRIO = the CAL cell plus ONE shallow census cell (h ~ 1200)
audited end to end, all frontier cells SMOKE-SKIPPED (typed),
verdict SMOKE.

HONEST AMENDMENTS (declared before the frozen run).
 A1 NO pre-freeze reconnaissance was run.  Every reference value
    (the CCCVII tau / d / tau_ideal_ub table, the CCXCIX raw taus,
    the CCCXV enclosures and lam_min values, the cost envelopes, the
    indirect chain reads 4.80e-14 and 7.92e+02) is quoted from the
    PRINTED record of CCXCIX / CCCV / CCCVII / CCCXV / CCCXVII
    (next.txt notes and probe docstrings) and never recomputed as a
    substitute for a gate.
 A2 THE AUDIT IS NOT A REFUTATION OF A NUMBER, IT IS A MEASUREMENT
    OF AN INSTRUMENT.  Both routes are float64 measurements of the
    same ideal object.  The arbiter's advantage is NAMED and
    limited: it never evaluates a chain, so it is immune to (III);
    it is NOT immune to the float64 assembly of its own h x h
    matrix, and its positive reads remain "no witness found", never
    "positivity certified".  Nothing here promotes a positivity
    claim.
 A3 The chain route is reproduced VERBATIM (ob.grid_density,
    ob.folded_measure_full, ob.lanczos_chain, ob.eval_chain, the
    CCCVII localization by LU inverse iteration with LOC_ITERS = 30,
    ideal_tier with NREF = 2 O-metric refinement steps and its
    outward gamma_n bounds).  The Schur / step-frame tier of
    bat.build_rung_param is NOT rebuilt: negS / lamS play no part in
    any read of this probe and their absence is declared, not hidden.
 A4 ROUTE B's own coefficient recurrence is float64 and therefore
    also carries error; it is NEVER assumed to be the truth.  ROUTE C
    (mpmath) is the referee at the sampled nodes, and the polynomial
    that the arbiter evaluates is DEFINED by the computed
    coefficient vector a -- so the certified Q[q_a] is a valid read
    for THAT polynomial whatever the conversion error was, and the
    conversion error itself is what S3 measures.
 A5 No interval enclosure of the full h x h matrices is attempted
    (h ~ 9.5e3); outward rounding is applied to the DECISIVE SCALARS
    exactly as CCCVII A2 and CCCXV A6 did.  The h-scaling statements
    of the instrument verdict are MEASUREMENTS on built cells, never
    laws, and the extrapolation is typed CONJECTURE-GRADE.
 A6 No ladder rebuild, no scorecard row, no promotion, no marker
    move, no re-typing of any certificate of record.  Naming which
    prior verdicts are AFFECTED is a statement about which
    measurement they consumed; the decision to re-type them belongs
    to the lead.
 A7 The concurrent decider mission (CCCXXI, a second cell in
    (9500, 11000] built with the metric-corrected chain machinery)
    consumes exactly the instrument audited here.  If this probe
    locates a defect, that decider's read inherits it; that is
    stated in the synthesis and is not a criticism of that run.
 A8 THE RE-PRICING MODEL (a SMOKE REPAIR, disclosed).  The smoke
    measured that CCCVII's a-priori node model dq = gamma_h *
    sum_k |c_k p_k| UNDER-PRICES the actual chain-vs-polynomial
    node deviation by an order of magnitude, because it bounds the
    SUMMATION of sum_k c_k p_k and not the recurrence error inside
    p_k itself.  The re-priced enclosure therefore uses
    max(a-priori model, REPR_SAFE = 8 x MEASURED deviation) on BOTH
    arms (CCCVII priced mu_+ only), and the model is WARDED at every
    audited cell by XR: it must cover the measured discrepancy
    between the chain's arm integrals and the certified enclosure of
    the same integrals of the same polynomial.  The re-priced
    enclosure is an HONEST ENCLOSURE OF THE CHAIN ROUTE'S OWN
    SCALAR, not a new certificate of the ideal object.

NO RH claim.  NO counterexample claim.  No paper, ledger, website,
manifest or verification file is touched; verification/ is imported
READ-ONLY for the deployed conventions, and the only edit outside
this file is the German CCCXXIII line prepended to
experiments/next.txt AFTER the frozen summary.

Sources (read-only): v563_paper2_readouts (deployed generators:
von_mangoldt_table, arch_lags, atom_lags_at, NU_MAIN, H_MIN, HCAP,
N_ATOM_MIN), onebadmode_moments_probe (the deployed pipeline:
build_ext_tables, grid_density, folded_measure_full, lanczos_chain,
eval_chain, smooth_masses), cofinal_dissect_probe (CCCVII: the chain
route under audit and its reference table, quoted as constants),
metric_map_probe (CCCXVII: the reference table, quoted as
constants), cased_replicate_probe (CCCXV: the arbiter machinery and
its enclosures, quoted as constants).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/chain_audit_probe.py --smoke
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/chain_audit_probe.py
"""

import ast
import hashlib
import math
import os
import sys
import time
from fractions import Fraction

import mpmath as mp
import numpy as np
import scipy.linalg as sla

_HERE = os.path.dirname(os.path.abspath(__file__))
_VERIFY = os.path.abspath(os.path.join(_HERE, "..", "..", "verification"))
sys.path.insert(0, _HERE)
sys.path.insert(0, _VERIFY)

import onebadmode_moments_probe as ob        # noqa: E402 (READ-ONLY)
import v563_paper2_readouts as core          # noqa: E402 (READ-ONLY)

# ------------------------------------------------------- frozen bars
TAB2 = 16_000_000
EXT_DEPLOYED = 4_000_000
KZ2_MAX = 1200
CENSUS_N_REF = 587
CENSUS_HMAX_REF = 65051
NU_MAIN = 4
H_MIN, HCAP = 128, 1450
N_ATOM_MIN = 40
MP_DPS = 50
MP_NODES = 10
DEG_PROBE = 24
FFT_PROBE = 256
FFT_WARD2 = 96
ETA_SAFE = 8.0
COEF_PROBE = 24
COEF_SAFE = 8.0
REPR_SAFE = 8.0
SIGN_MARGIN = 1.0
CAL_RTOL = 1.0e-3
IDENT_BAR = 1.0e-11
ARM_ULP = 8.0
REPRO_RTOL = 2.0e-3
ARB_RTOL = 5.0e-2
TAU_NOISE = 5.0e-12
IDEAL_NOISE = 1.0e-12
LOC_ITERS = 30
NREF = 2
OPROBE_SEED = 7
SCR_SEED = 1
DOPE = 1.0e-2
SAMP_SEED = 11
CAL_TGT = 900
VAL_TGT = (2012, 3948, 5500, 7200)
BUILD_CAP_S = 2500.0
GUARD_FAC = 1.05
COST_CHAIN = 4.6e-10
COST_ARB = 1.3e-10
EPS64 = float(np.finfo(float).eps)
U_RND = 0.5 * EPS64

# the CCCVII / CCCXVII record, quoted as reference targets:
#   key -> (h, kz, tau, d, tau_ideal_ub, raw, ideal)
CHAIN_REF = {
    "6197": (6197, 337, -5.227e-11, None, +8.186e-12, "NEGA", "POS"),
    "6247": (6247, 436, -1.611e-10, None, -1.352e-10, "NEGA", "NEG"),
    "7958": (7958, 282, +5.904e-11, -9.9587e-11, -4.0560e-11,
             "POS", "NEG"),
    "8003": (8003, 284, -8.160e-11, +2.5703e-10, +1.7541e-10,
             "NEGA", "POS"),
    "8204": (8204, 287, +2.665e-10, +8.9426e-11, +3.559e-10,
             "POS", "POS"),
    "8629": (8629, 223, +7.245e-10, +3.8689e-11, +7.632e-10,
             "POS", "POS"),
    "8642": (8642, 551, -2.122e-12, None, None, "MARGINAL", "-"),
    "8677": (8677, 299, -3.053e-10, +4.3465e-12, -3.0093e-10,
             "NEGA", "NEG"),
    "9023": (9023, 506, -1.498e-10, +8.7360e-11, -6.2463e-11,
             "NEGA", "NEG"),
    "9447": (9447, 196, -1.412e-10, +5.3769e-11, -8.7460e-11,
             "NEGA", "NEG"),
    "9535": (9535, 526, -1.743e-10, +4.2931e-11, -1.3139e-10,
             "NEGA", "NEG"),
}
# the CCCXV arbiter record: key -> (lam_min(Omega_weil) or None,
#                                   tau-scale read, n_neg)
ARB_REF = {
    "9447": (None, +2.007139e-10, 0),
    "9535": (+3.297e-15, +4.209371e-11, 0),
    "8677": (None, +1.209097e-10, 0),
    "9023": (+9.042e-15, +7.830699e-11, 0),
    "8629": (None, +2.361062e-10, 0),
}
# the two indirect chain reads CCCVII published as its scope edge
CCCVII_DIAGO = 4.80e-14
CCCVII_GROWTH = 7.92e2
# the audit targets and the field
AUD_KEYS = ("9447", "9535")
G1_KEYS = ("8677", "9023")
FIELD_NEW = ("8642", "8003", "7958", "6247", "6197")
FIELD_CTRL = ("8629", "8204")

BANNED_IDS = ("zetazero", "zetazeros", "nzeros", "primerange",
              "isprime", "primepi", "nextprime", "prevprime",
              "factorint", "primefactors")
READER_BANNED = ("tau", "eig", "eigs", "eigh", "eigvals", "eigvalsh",
                 "inv", "pinv", "solve", "lu_factor", "lu_solve",
                 "ldl", "svd", "cond", "negA")
READER_FUNCS = ("e1_quad", "e3_kernel", "e3_th", "e3_dense",
                "node_values", "cheb_coeffs", "coef_dev",
                "omega_weil_rows", "chain_pass_values",
                "chain_pass_project", "chain_sample_values",
                "cheb_pass", "xmul", "mp_chain_dev",
                "moment_transform", "arm_sums", "diag_o_sample",
                "certify_witness", "fft_ward", "eta_of",
                "node_frame")

CHECKS = []
KILLS = []
T0 = time.time()
SMOKE = "--smoke" in sys.argv[1:]
SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
try:
    with open(os.path.abspath(__file__), "rb") as _fh:
        CODE_SHA = hashlib.sha256(_fh.read()).hexdigest()
except OSError:
    CODE_SHA = "unavailable"


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


def ast_scan_functions(names, banned):
    src = open(os.path.abspath(__file__), encoding="utf-8").read()
    bad = []
    for node in ast.walk(ast.parse(src)):
        if isinstance(node, ast.FunctionDef) and node.name in names:
            for sub in ast.walk(node):
                nm = None
                if isinstance(sub, ast.Name):
                    nm = sub.id
                elif isinstance(sub, ast.Attribute):
                    nm = sub.attr
                elif isinstance(sub, ast.arg):
                    nm = sub.arg
                if nm and nm in banned:
                    bad.append("%s:%s" % (node.name, nm))
    return bad


def gamma_n(nterms):
    """The rigorous forward error factor of a length-n float64
    recursive summation: gamma_n = n u / (1 - n u)."""
    prod = nterms * U_RND
    if prod >= 0.5:
        return float("inf")
    return prod / (1.0 - prod)


def fsum_dot(av, bv):
    """Exactly-rounded sum of a_i b_i plus a RIGOROUS outward
    half-width for the product roundings."""
    pr = np.asarray(av, float) * np.asarray(bv, float)
    val = math.fsum(pr.tolist())
    wid = U_RND * math.fsum(np.abs(pr).tolist())
    return val, wid


def ldl_inertia(dblk):
    """EXACT block inertia of a Bunch-Kaufman LDL^T factor (CCCVII
    A13 / CCCXV verbatim): a 1x1 pivot contributes its sign, a 2x2
    block one negative eigenvalue iff det < 0 and two iff det > 0
    with negative trace, the determinant sign decided in EXACT
    rational arithmetic on the dyadic float64 entries."""
    dd = np.diag(dblk)
    sub = np.diag(dblk, k=1)
    ndim = len(dd)
    n_neg = n_zero = n_two = 0
    i = 0
    while i < ndim:
        if i + 1 < ndim and sub[i] != 0.0:
            aa = Fraction(float(dd[i]))
            bb = Fraction(float(sub[i]))
            cc = Fraction(float(dd[i + 1]))
            det = aa * cc - bb * bb
            tr = aa + cc
            if det < 0:
                n_neg += 1
            elif det > 0:
                if tr < 0:
                    n_neg += 2
            else:
                n_zero += 1
                if tr < 0:
                    n_neg += 1
            n_two += 1
            i += 2
        else:
            if dd[i] < 0.0:
                n_neg += 1
            elif dd[i] == 0.0:
                n_zero += 1
            i += 1
    return n_neg, n_zero, n_two


def f4(val):
    return "%+.4e" % val if math.isfinite(val) else "nan"


# ================================================ the arbiter (PATH 3)
def node_frame(lag, M):
    """The M Chebyshev-Lobatto nodes, the SIGNED masses and the fold
    multiplicity.  Lag entries and frozen constants only."""
    L = 2 * M - 2
    ext = np.concatenate([lag, lag[-2:0:-1]])
    dv = np.fft.fft(ext).real[:M]
    th = math.pi * np.arange(M) / (M - 1)
    eps = np.full(M, 2.0)
    eps[0] = 1.0
    eps[M - 1] = 1.0
    wsig = eps * dv * 4.0 * np.sin(th / 2.0) ** 2 / (2.0 * L)
    return th, wsig, dv, L


def node_values(avec, M, L):
    """q(x_i) = sum_{m<h} a_m cos(m theta_i) at the M Lobatto nodes,
    by ONE length-L FFT.  Coefficients and frozen constants only."""
    pad = np.zeros(L)
    pad[:len(avec)] = avec
    return np.fft.fft(pad).real[:M]


def moment_transform(gvals, M, L):
    """m_m = sum_i g_i cos(m theta_i), m = 0..M-1, by ONE length-L
    FFT (the DCT-I of the node-supported vector g).  Node data and
    frozen constants only."""
    ext = np.concatenate([gvals, gvals[-2:0:-1]])
    fv = np.fft.fft(ext).real[:M]
    sgn = np.where(np.arange(M) % 2 == 0, 1.0, -1.0)
    return 0.5 * (fv + gvals[0] + sgn * gvals[M - 1])


def cheb_coeffs(avec, M, L):
    """The cosine coefficients b_r of q^2 and phi_r of
    4 sin^2(theta/2) q(cos theta)^2 by EXACT polynomial algebra on a
    4L grid (no aliasing).  Coefficients and frozen constants only."""
    nf = 4 * L
    pad = np.zeros(nf)
    pad[:len(avec)] = avec
    qv = np.fft.fft(pad).real
    thf = 2.0 * math.pi * np.arange(nf) / nf
    bh = np.fft.fft(qv * qv).real / nf
    ph = np.fft.fft(4.0 * np.sin(thf / 2.0) ** 2 * qv * qv).real / nf
    bb = np.concatenate([[bh[0]], 2.0 * bh[1:2 * (M // 2)]])
    pp = np.concatenate([[ph[0]], 2.0 * ph[1:M]])
    return bb, pp, qv, thf


def coef_dev(fnc, thf, idx, ref):
    """max_r |fft coefficient - exactly rounded coefficient| over the
    sampled orders.  Coefficients and frozen constants only."""
    nf = len(fnc)
    dev = 0.0
    for r in idx:
        exact = 2.0 * math.fsum((fnc * np.cos(r * thf)).tolist()) / nf
        dev = max(dev, abs(exact - ref[r]))
    return dev


def omega_weil_rows(G, h, out):
    """Omega[m,m'] = (G_{m+m'} + G_{|m-m'|}) / 2, assembled row by row
    from the lag-derived sequence G.  Lag entries only."""
    for m in range(h):
        row = out[m]
        np.add(G[m:m + h], 0.0, out=row)
        row[:m + 1] += G[m::-1]
        if m + 1 < h:
            row[m + 1:] += G[1:h - m]
        row *= 0.5
    return out


def e1_quad(qv, wsig, eta):
    """The rebuilt folded quadrature with OUTWARD rounding: returns
    (Q, halfwidth, D_plus, D_plus_lo).  Node values, signed masses
    and frozen constants only."""
    aq = np.abs(qv)
    lo = np.maximum(aq - eta, 0.0) ** 2
    hi = (aq + eta) ** 2
    pos = wsig > 0.0
    neg = wsig < 0.0
    wp = wsig[pos]
    wn = -wsig[neg]
    d_lo = math.fsum((wp * lo[pos]).tolist())
    d_hi = math.fsum((wp * hi[pos]).tolist())
    n_lo = math.fsum((wn * lo[neg]).tolist())
    n_hi = math.fsum((wn * hi[neg]).tolist())
    rnd = U_RND * (math.fsum(np.abs(wp * hi[pos]).tolist())
                   + math.fsum(np.abs(wn * hi[neg]).tolist()))
    q_lo = d_lo - n_hi - rnd
    q_hi = d_hi - n_lo + rnd
    return 0.5 * (q_lo + q_hi), 0.5 * (q_hi - q_lo), \
        0.5 * (d_lo + d_hi), d_lo - rnd


def arm_sums(qpos, wpos, qneg, wneg, eta):
    """OUTWARD-rounded arm integrals from node values:
       (Dp_lo, Dp_hi, Nm_lo, Nm_hi) for int q^2 dmu_+ and
       int q^2 dmu_-.  Node values, masses and frozen constants."""
    def one(qq, ww):
        aq = np.abs(qq)
        lo = np.maximum(aq - eta, 0.0) ** 2
        hi = (aq + eta) ** 2
        s_lo = math.fsum((ww * lo).tolist())
        s_hi = math.fsum((ww * hi).tolist())
        rnd = U_RND * math.fsum(np.abs(ww * hi).tolist())
        return s_lo - rnd, s_hi + rnd
    plo, phi = one(qpos, wpos)
    nlo, nhi = one(qneg, wneg)
    return plo, phi, nlo, nhi


def e3_kernel(phi, phi_dev, lag_dep, c1n):
    """The assembled Weil-kernel Galerkin restriction contracted in
    its stable coordinate a^T Omega_weil a = (1/2) sum_r phi_r c_r.
    Kernel entries, coefficients and frozen constants only."""
    nr = min(len(phi), len(lag_dep))
    val, wid = fsum_dot(phi[:nr], lag_dep[:nr])
    return 0.5 * val, 0.5 * (wid + phi_dev * c1n)


def e3_th(bcoef, b_dev, gseq):
    """The Toeplitz-Hankel CONSISTENCY read: a^T Omega_weil a =
    sum_r G_r b_r.  Kernel entries and coefficients only."""
    nr = min(len(bcoef), len(gseq))
    val, wid = fsum_dot(gseq[:nr], bcoef[:nr])
    wid += b_dev * math.fsum(np.abs(gseq[:nr]).tolist())
    return val, wid


def e3_dense(avec, omega, blk=1024):
    """The same bilinear form on the ASSEMBLED h x h matrix with the
    rigorous (deliberately crude) gamma_n bound."""
    hdim = len(avec)
    absacc = 0.0
    parts = []
    aabs = np.abs(avec)
    for lo in range(0, hdim, blk):
        hi = min(hdim, lo + blk)
        parts.append(float(avec[lo:hi] @ (omega[lo:hi] @ avec)))
        absacc += float(aabs[lo:hi] @ (np.abs(omega[lo:hi]) @ aabs))
    return math.fsum(parts), gamma_n(hdim + 1) * absacc


def eta_of(avec, L):
    """The DECLARED FFT forward-error model half-width for the node
    values (8 log2(L) u ||a||_1)."""
    return 8.0 * math.log2(max(4, L)) * U_RND * float(
        math.fsum(np.abs(avec).tolist()))


def fft_ward(avec, qv, th, idx):
    """MEASURE the FFT node-value deviation against an exactly-rounded
    dense reference on the sampled nodes."""
    mi = np.arange(len(avec), dtype=float)
    worst = 0.0
    for k in idx:
        ref = math.fsum((avec * np.cos(mi * th[k])).tolist())
        worst = max(worst, abs(ref - float(qv[k])))
    return worst


# ============================================ the chain route (ROUTE A)
def chain_pass_values(al, be, m0, xnodes, wts, npoly, cvec):
    """CCCVII VERBATIM: ONE forward pass of the deployed three-term
    chain at xnodes, accumulated instead of stored.  Returns
    qv (the witness values), qabs (the rigorous gamma companion),
    dg (the diagonal of the metric) and gmax (the growth census).
    Nodes, weights, coefficients and frozen constants only."""
    xarr = np.asarray(xnodes, float)
    warr = np.asarray(wts, float)
    cvv = np.asarray(cvec, float)
    pkm1 = np.full(len(xarr), 1.0 / math.sqrt(m0))
    qv = cvv[0] * pkm1
    qabs = np.abs(cvv[0] * pkm1)
    dg = np.zeros(npoly)
    dg[0] = float(warr @ (pkm1 * pkm1))
    gmax = float(np.max(np.abs(pkm1)))
    if npoly > 1:
        pk = (xarr - al[0]) * pkm1 / be[0]
        qv = qv + cvv[1] * pk
        qabs = qabs + np.abs(cvv[1] * pk)
        dg[1] = float(warr @ (pk * pk))
        gmax = max(gmax, float(np.max(np.abs(pk))))
        for k in range(1, npoly - 1):
            pnew = ((xarr - al[k]) * pk - be[k - 1] * pkm1) / be[k]
            qv = qv + cvv[k + 1] * pnew
            qabs = qabs + np.abs(cvv[k + 1] * pnew)
            dg[k + 1] = float(warr @ (pnew * pnew))
            gm = float(np.max(np.abs(pnew)))
            if gm > gmax:
                gmax = gm
            pkm1, pk = pk, pnew
    return qv, qabs, dg, gmax


def chain_pass_project(al, be, m0, xnodes, wts, npoly, fvals):
    """CCCVII VERBATIM: the transposed pass, out[k] = sum_i w_i
    p_k(x_i) f_i, i.e. the metric action (O c)_k for f = q."""
    xarr = np.asarray(xnodes, float)
    wf = np.asarray(wts, float) * np.asarray(fvals, float)
    out = np.zeros(npoly)
    pkm1 = np.full(len(xarr), 1.0 / math.sqrt(m0))
    out[0] = float(wf @ pkm1)
    if npoly > 1:
        pk = (xarr - al[0]) * pkm1 / be[0]
        out[1] = float(wf @ pk)
        for k in range(1, npoly - 1):
            pnew = ((xarr - al[k]) * pk - be[k - 1] * pkm1) / be[k]
            out[k + 1] = float(wf @ pnew)
            pkm1, pk = pk, pnew
    return out


def chain_sample_values(al, be, m0, xnodes, npoly):
    """ROUTE A at a SMALL node sample with ALL degrees stored (the
    float64 reference of the deployed recurrence; bitwise identical
    to ob.eval_chain restricted to those nodes, warded).  Nodes,
    recurrence entries and frozen constants only."""
    xarr = np.asarray(xnodes, float)
    out = np.zeros((npoly, len(xarr)))
    pkm1 = np.full(len(xarr), 1.0 / math.sqrt(m0))
    out[0] = pkm1
    if npoly > 1:
        pk = (xarr - al[0]) * pkm1 / be[0]
        out[1] = pk
        for k in range(1, npoly - 1):
            pnew = ((xarr - al[k]) * pk - be[k - 1] * pkm1) / be[k]
            out[k + 1] = pnew
            pkm1, pk = pk, pnew
    return out


# ==================================== ROUTE B: the coefficient space
def xmul(A, deg, out):
    """out = the Chebyshev coefficients of x p(x) where A carries
    those of p up to degree deg (x T_m = (T_{m+1} + T_{|m-1|})/2,
    an EXACT identity).  Coefficients only."""
    out[:deg + 3] = 0.0
    out[1] = A[0]
    if deg >= 1:
        out[0] = 0.5 * A[1]
        out[2:deg + 2] += 0.5 * A[1:deg + 1]
    if deg >= 2:
        out[1] += 0.5 * A[2]
        if deg >= 3:
            out[2:deg] += 0.5 * A[3:deg + 1]
    return out


def cheb_pass(al, be, m0, npoly, mvec=None, cvec=None, degs=()):
    """ROUTE B: the identical three-term recurrence run in CHEBYSHEV
    COEFFICIENT space.  Returns
      cB[k]  = A_k . mvec              (the witness coefficients
                                        recomputed from the moments),
      cabs[k]= sum_m |A_k[m] mvec[m]|  (the gamma companion),
      acc    = sum_k cvec[k] A_k       (the Chebyshev coefficients of
                                        the chain's own witness),
      anorm[k] = ||A_k||_1, amax[k] = ||A_k||_inf (the coefficient
                                        growth census),
      keep   = {k: A_k} for the sampled degrees.
    Recurrence entries, coefficients and frozen constants only."""
    nn = npoly + 3
    a_km1 = np.zeros(nn)
    a_k = np.zeros(nn)
    a_new = np.zeros(nn)
    tmp = np.zeros(nn)
    a_km1[0] = 1.0 / math.sqrt(m0)
    cB = np.zeros(npoly)
    cabs = np.zeros(npoly)
    anorm = np.zeros(npoly)
    amax = np.zeros(npoly)
    acc = np.zeros(npoly + 1) if cvec is not None else None
    keep = {}
    dset = set(int(d) for d in degs)

    def record(k, arr, deg):
        anorm[k] = float(math.fsum(np.abs(arr[:deg + 1]).tolist()))
        amax[k] = float(np.max(np.abs(arr[:deg + 1])))
        if mvec is not None:
            pr = arr[:deg + 1] * mvec[:deg + 1]
            cB[k] = math.fsum(pr.tolist())
            cabs[k] = math.fsum(np.abs(pr).tolist())
        if acc is not None:
            acc[:deg + 1] += cvec[k] * arr[:deg + 1]
        if k in dset:
            keep[k] = arr[:deg + 1].copy()

    record(0, a_km1, 0)
    if npoly > 1:
        xmul(a_km1, 0, tmp)
        a_k[:3] = (tmp[:3] - al[0] * a_km1[:3]) / be[0]
        record(1, a_k, 1)
        for k in range(1, npoly - 1):
            xmul(a_k, k, tmp)
            nd = k + 2
            a_new[:nd] = (tmp[:nd] - al[k] * a_k[:nd]
                          - be[k - 1] * a_km1[:nd]) / be[k]
            a_new[nd:nd + 2] = 0.0
            record(k + 1, a_new, k + 1)
            a_km1, a_k, a_new = a_k, a_new, a_km1
    return dict(cB=cB, cabs=cabs, acc=acc, anorm=anorm, amax=amax,
                keep=keep)


# ================================== ROUTE C: the mpmath referee
def mp_chain_dev(al, be, m0, ynodes, pref, dps, keep_k=()):
    """ROUTE C: the SAME node-space three-term recurrence evaluated in
    dps-digit arithmetic on the EXACTLY converted float64 (al, be,
    m0) -- the true values of the polynomials the chain defines.
    pref[k, i] is the float64 route to compare against; the return is
    the per-degree absolute deviation, the per-degree magnitude and
    the mp VALUES at the requested degrees (so that ROUTE B can be
    refereed against the same truth).  Nodes, recurrence entries and
    frozen constants only."""
    old = mp.mp.dps
    mp.mp.dps = dps
    try:
        yy = [mp.mpf(float(v)) for v in ynodes]
        aa = [mp.mpf(float(v)) for v in al]
        bb = [mp.mpf(float(v)) for v in be]
        p0 = mp.mpf(1) / mp.sqrt(mp.mpf(float(m0)))
        npoly = int(pref.shape[0])
        ns = len(yy)
        dev = np.zeros(npoly)
        mag = np.zeros(npoly)
        want = set(int(x) for x in keep_k)
        keep = {}
        pkm1 = [p0] * ns
        mag[0] = float(abs(p0))
        dev[0] = max(abs(float(pref[0, i]) - float(pkm1[i]))
                     for i in range(ns))
        if 0 in want:
            keep[0] = np.array([float(v) for v in pkm1])
        if npoly > 1:
            pk = [(yy[i] - aa[0]) * pkm1[i] / bb[0] for i in range(ns)]
            mag[1] = max(float(abs(v)) for v in pk)
            dev[1] = max(abs(float(pref[1, i]) - float(pk[i]))
                         for i in range(ns))
            if 1 in want:
                keep[1] = np.array([float(v) for v in pk])
            for k in range(1, npoly - 1):
                pnx = [((yy[i] - aa[k]) * pk[i]
                        - bb[k - 1] * pkm1[i]) / bb[k]
                       for i in range(ns)]
                mag[k + 1] = max(float(abs(v)) for v in pnx)
                dev[k + 1] = max(abs(float(pref[k + 1, i])
                                     - float(pnx[i]))
                                 for i in range(ns))
                if k + 1 in want:
                    keep[k + 1] = np.array([float(v) for v in pnx])
                pkm1, pk = pk, pnx
        return dev, mag, keep
    finally:
        mp.mp.dps = old


def diag_o_sample(keep, xs_idx, wts, M, L, dg_chain):
    """The diag(O) census per SAMPLED degree on ROUTE B:
    O_kk = sum_i w_i p_k(x_i)^2 with p_k evaluated from its
    Chebyshev coefficients, against the chain's own dg_chain[k].
    Coefficients, node indices, weights and frozen constants only."""
    out = []
    for k in sorted(keep):
        nv = node_values(keep[k], M, L)
        val = math.fsum((wts * nv[xs_idx] ** 2).tolist())
        out.append((k, val, float(dg_chain[k]), val - float(
            dg_chain[k])))
    return out


# ===================================================== tables + census
DEEP = {}


def build_tables():
    section("T -- the atom table to TAB2 = %.3g, warded BITWISE "
            "against the deployed 4e6 EXT prefix and against "
            "core.von_mangoldt_table" % TAB2)
    ob.build_ext_tables()
    lam2 = core.von_mangoldt_table(TAB2)
    nn2 = np.nonzero(lam2 > 0.0)[0]
    u2 = np.log(nn2.astype(float))
    mu2 = 2.0 * lam2[nn2] / np.sqrt(nn2.astype(float))
    n_pref = len(ob.EXT["NN"])
    ok = (np.array_equal(nn2[:n_pref], ob.EXT["NN"])
          and np.array_equal(u2[:n_pref], ob.EXT["U"])
          and np.array_equal(mu2[:n_pref], ob.EXT["MU"]))
    check("T1 the 1.6e7 arrays agree BITWISE with the deployed 4e6 "
          "EXT arrays (%d atoms of %d)" % (n_pref, len(nn2)), ok,
          kill="K2")
    check("T2 the deployed frame constant NU_MAIN == %d" % NU_MAIN,
          int(core.NU_MAIN) == NU_MAIN, kill="K1")
    DEEP["U"] = u2
    DEEP["MU"] = mu2
    DEEP["G"] = np.diff(u2)


def deep_census():
    section("D -- the deep-frame census (deployed formula verbatim)")
    u2, g2 = DEEP["U"], DEEP["G"]
    out = []
    for kz in range(2, min(KZ2_MAX, len(u2) - 1)):
        alpha = float(u2[kz])
        d_k = 0.5 * float(g2[kz]) / float(NU_MAIN)
        mz = int(math.ceil(alpha / d_k - 1.0e-9)) + 1
        if mz % 2:
            mz += 1
        x_val = math.exp(2.0 * alpha)
        if x_val <= TAB2:
            out.append(dict(h=mz // 2, kz=kz, alpha=alpha, M=mz,
                            X=x_val, gap=float(g2[kz])))
    out.sort(key=lambda c: (c["h"], c["kz"]))
    hs = np.asarray([c["h"] for c in out], float)
    keys = {(c["h"], c["kz"]) for c in out}
    need = [(v[0], v[1]) for v in CHAIN_REF.values()]
    ok_keys = all(k in keys for k in need)
    check("D1 census reproduces CCXCIX/CCCV/CCCVII/CCCXV: %d == %d "
          "cells, h max %d == %d, all %d reference keys present (%s)"
          % (len(out), CENSUS_N_REF, int(hs.max()), CENSUS_HMAX_REF,
             len(need), ok_keys),
          len(out) == CENSUS_N_REF and int(hs.max()) == CENSUS_HMAX_REF
          and ok_keys, kill="K1")
    return out


def window_data(cell, world=None, scr_seed=None, dope=False):
    """The shared window data of a cell: the deployed lag profile and
    the atom census.  Both routes consume THIS."""
    u2, mu2 = DEEP["U"], DEEP["MU"]
    alpha, M = cell["alpha"], cell["M"]
    ka = int(np.searchsorted(u2, 2.0 * alpha + 1.0e-14, side="right"))
    uu = u2[:ka].copy()
    mm = mu2[:ka].copy()
    if world == "smooth":
        mm = ob.smooth_masses(uu)
    elif world == "scramble":
        rng = np.random.default_rng(scr_seed)
        uu = np.sort(rng.uniform(0.0, 2.0 * alpha, size=ka))
    D = 2.0 * alpha / M
    c_ar = np.asarray(core.arch_lags(M, D), float)
    c_at = np.asarray(core.atom_lags_at(alpha, M, uu, mm)[0], float)
    lag = c_ar + c_at
    if dope:
        lag = lag.copy()
        lag[M // 3] *= (1.0 + DOPE)
    return dict(alpha=alpha, M=M, D=D, h=M // 2, uu=uu, mm=mm,
                lag=lag, n_atom=int(ka), X=cell["X"],
                at_scale=float(np.max(np.abs(c_at))))


# ==================================================== the arbiter build
def arbiter_cell(tag, cell, dat=None, world=None, scr_seed=None,
                 dope=False, keep_omega=False):
    """PATH 3: assemble Omega_weil DIRECTLY from the lag profile, take
    its bottom eigenvector as the extremal witness, decide
    definiteness by the EXACT block inertia of its LDL factor, and
    certify the decisive scalar in three coordinates."""
    t_c = time.time()
    if dat is None:
        dat = window_data(cell, world=world, scr_seed=scr_seed,
                          dope=dope)
    M, h, lag = dat["M"], dat["h"], dat["lag"]
    row = dict(tag=tag, cell=cell, world=world, dope=dope, dat=dat,
               kind="ARB")
    th, wsig, dv, L = node_frame(lag, M)
    row["n_pos"] = int(np.sum(wsig > 0.0))
    row["n_neg"] = int(np.sum(wsig < 0.0))
    row["n_zero"] = int(M - row["n_pos"] - row["n_neg"])
    aext = np.concatenate([lag, [lag[M - 2]]])
    rr = np.arange(2 * h)
    gseq = aext[rr] - 0.5 * (aext[rr + 1] + aext[np.abs(rr - 1)])
    om3 = np.empty((h, h))
    omega_weil_rows(gseq, h, om3)
    w3v, w3 = sla.eigh(om3, subset_by_index=[0, 0])
    a3 = np.ascontiguousarray(w3[:, 0])
    a3 = a3 / float(np.linalg.norm(a3))
    row["lam_arb"] = float(w3v[0])
    try:
        _l, dblk, _p = sla.ldl(om3, lower=True)
        nneg, nzero, ntwo = ldl_inertia(dblk)
        row["inertia"] = dict(n_neg=nneg, n_zero=nzero, n_2x2=ntwo,
                              agree=bool((nneg > 0)
                                         == (float(w3v[0]) < 0.0)))
        del dblk, _l
    except Exception as exc:                          # noqa: BLE001
        row["inertia"] = dict(refused=type(exc).__name__, agree=False)
    row["cen"] = certify_witness(a3, dat, th, wsig, L, gseq, om3)
    if keep_omega:
        row["omega"] = om3
        row["frame"] = dict(th=th, wsig=wsig, L=L, gseq=gseq)
    else:
        del om3
    row["t_cell"] = time.time() - t_c
    return row


def certify_witness(avec, dat, th, wsig, L, gseq, om3=None,
                    label="W"):
    """The certified enclosures of the wall scalar at ONE coefficient
    vector: the folded quadrature E1, the Weil-kernel contraction E3,
    the Toeplitz-Hankel coordinate E3t, the assembled-matrix read
    E3d, and the declared-and-warded numerical half-width models."""
    M, lag = dat["M"], dat["lag"]
    rng = np.random.default_rng(SAMP_SEED)
    eta_mod = eta_of(avec, L)
    qv = node_values(avec, M, L)
    nidx = sorted(set(int(x) for x in rng.choice(
        M, size=min(FFT_PROBE, M), replace=False)))
    wdev = fft_ward(avec, qv, th, nidx)
    eta = max(eta_mod, ETA_SAFE * wdev)
    n2 = sorted(set(int(x) for x in rng.choice(
        M, size=min(FFT_WARD2, M), replace=False)) - set(nidx))
    wdev2 = fft_ward(avec, qv, th, n2)
    bb, phi, qf, thf = cheb_coeffs(avec, M, L)
    ridx = sorted(set(int(x) for x in rng.choice(
        M, size=min(COEF_PROBE, M), replace=False)))
    sq = qf * qf
    pfn = 4.0 * np.sin(thf / 2.0) ** 2 * sq
    d_phi = coef_dev(pfn, thf, ridx, phi)
    d_bb = coef_dev(sq, thf, [r for r in ridx if r < len(bb)], bb)
    r2 = sorted(set(int(x) for x in rng.choice(
        M, size=min(COEF_PROBE, M), replace=False)) - set(ridx))
    w_phi = coef_dev(pfn, thf, r2, phi)
    w_bb = coef_dev(sq, thf, [r for r in r2 if r < len(bb)], bb)
    phi_dev = COEF_SAFE * d_phi
    b_dev = COEF_SAFE * d_bb
    c1n = math.fsum(np.abs(lag).tolist())
    q1, d1, dp, dp_lo = e1_quad(qv, wsig, eta)
    q3, d3 = e3_kernel(phi, phi_dev, lag, c1n)
    q3t, d3t = e3_th(bb, b_dev, gseq)
    out = dict(label=label, eta=eta, eta_mod=eta_mod, fft_dev=wdev,
               fft_dev2=wdev2, E1=(q1, d1), E3=(q3, d3),
               E3t=(q3t, d3t), phi_dev=phi_dev, b_dev=b_dev,
               w_phi=w_phi, w_bb=w_bb, dplus=dp, dplus_lo=dp_lo,
               qv=qv, a1n=float(math.fsum(np.abs(avec).tolist())))
    if om3 is not None:
        out["E3d"] = e3_dense(avec, om3)
    out["tau_ub"] = q1 / max(dp_lo, 1e-300)
    out["tau_lo"] = (q1 - d1) / max(dp_lo, 1e-300)
    out["tau_hi"] = (q1 + d1) / max(dp_lo, 1e-300)
    return out


def sign_of(val, hw):
    if val + SIGN_MARGIN * hw < 0.0:
        return "NEG"
    if val - SIGN_MARGIN * hw > 0.0:
        return "POS"
    return "STRADDLE"


def arb_verdict(row):
    cen = row["cen"]
    s1 = sign_of(cen["E1"][0], cen["E1"][1])
    s3 = sign_of(cen["E3"][0], cen["E3"][1])
    ine = row.get("inertia", {})
    nneg = ine.get("n_neg")
    if s1 == "NEG" and s3 == "NEG":
        return "DIRECT-NEG(certified witness at the extremal " \
            "coefficient vector; n_neg = %s)" % nneg
    if s1 == "POS" and s3 == "POS" and nneg == 0:
        return "DIRECT-POS(no witness found; positivity NOT " \
            "certified)"
    if s1 == "STRADDLE" or s3 == "STRADDLE":
        return "DIRECT-STRADDLE(E1 %s / E3 %s; n_neg %s)" \
            % (s1, s3, nneg)
    return "DIRECT-INCONSISTENT(E1 %s / E3 %s; n_neg %s)" \
        % (s1, s3, nneg)


# ====================================================== the chain build
def chain_cell(tag, cell, dat=None, world=None, scr_seed=None,
               keep=False):
    """THE ROUTE UNDER AUDIT, VERBATIM: ob.grid_density ->
    ob.folded_measure_full -> ob.lanczos_chain -> ob.eval_chain ->
    A_wall = I - sqrt(V) P P^T sqrt(V) -> tau = lam_min, the CCCVII
    LU inverse-iteration localization and the CCCVII metric-corrected
    ideal tier with its outward gamma bounds and NREF refinement."""
    t_c = time.time()
    if dat is None:
        dat = window_data(cell, world=world, scr_seed=scr_seed)
    M, h, lag = dat["M"], dat["h"], dat["lag"]
    row = dict(tag=tag, cell=cell, world=world, dat=dat, kind="CHAIN")
    dens = ob.grid_density(lag)
    L = 2 * M - 2
    xs, ws, uf_p, _fdp = ob.folded_measure_full(dens, L, +1.0)
    ys, vs, uf_n, _fdn = ob.folded_measure_full(dens, L, -1.0)
    al, be, m0, nsteps = ob.lanczos_chain(xs, ws, h + 1)
    row.update(n_pos=int(len(xs)), n_neg=int(len(ys)),
               nsteps=int(nsteps), L=L,
               be_min=float(np.min(be)) if len(be) else float("nan"),
               n_drop=int(M - len(xs) - len(ys)))
    if nsteps < h + 1 or np.any(be <= 0):
        row["fail"] = "CHAIN"
        row["t_cell"] = time.time() - t_c
        return row
    pn = ob.eval_chain(al, be, m0, ys, h)
    gram = np.sqrt(vs)[:, None] * (pn @ pn.T) * np.sqrt(vs)[None, :]
    gram = 0.5 * (gram + gram.T)
    n = gram.shape[0]
    amat = np.eye(n) - gram
    row["tr_gram"] = float(np.trace(gram))
    del gram
    eva = np.linalg.eigvalsh(amat)
    row["tau"] = float(eva[0])
    row["n_negA"] = int(np.sum(eva < 0.0))
    row["eva_bot"] = [float(v) for v in eva[:3]]
    # the CCCVII localization: LU inverse iteration
    zvec = None
    try:
        lu, piv = sla.lu_factor(amat)
        zvec = np.full(n, 1.0 / math.sqrt(n))
        for _ in range(LOC_ITERS):
            zvec = sla.lu_solve((lu, piv), zvec)
            zvec = zvec / float(np.linalg.norm(zvec))
        rq = float(zvec @ (amat @ zvec))
        row["loc"] = dict(rq=rq, rq_gap=abs(rq - row["tau"]),
                          res=float(np.linalg.norm(
                              amat @ zvec - rq * zvec)),
                          uf=int(uf_n[int(np.argmax(np.abs(zvec)))]),
                          part=float(np.max(np.abs(zvec))))
        del lu, piv
    except Exception as exc:                          # noqa: BLE001
        row["loc"] = dict(refused=type(exc).__name__)
    # the CCCVII metric-corrected ideal tier
    if zvec is not None:
        row["ideal"] = ideal_tier(al, be, m0, xs, ws, ys, vs, pn, h,
                                  zvec, row["tau"])
        row["zvec"] = zvec
    hull = np.nonzero((ys < float(np.min(xs)))
                      | (ys > float(np.max(xs))))[0]
    row["hull"] = dict(n_out=int(len(hull)), x_lo=float(np.min(xs)),
                       x_hi=float(np.max(xs)),
                       seats=[(int(uf_n[j]), float(ys[j]),
                               float(vs[j])) for j in hull[:3]])
    if keep:
        row["chain"] = dict(al=al, be=be, m0=m0, xs=xs, ws=ws,
                            ys=ys, vs=vs, uf_p=uf_p, uf_n=uf_n,
                            pn=pn)
    else:
        del pn
    del amat
    row["t_cell"] = time.time() - t_c
    return row


def ideal_tier(al, be, m0, xs, ws, ys, vs, pn, npoly, zvec, tau):
    """CCCVII VERBATIM: the metric-corrected ideal Galerkin read at
    the bad-mode witness with outward-rounded enclosures of both
    quadrature scalars, the diag(O) census, the random metric probe
    and NREF O-metric refinement steps."""
    svec = np.sqrt(vs) * zvec
    cvec = pn.T @ svec                       # c = P^T sqrt(V) z
    cn2 = float(cvec @ cvec)
    qv, qabs, dg, gmax = chain_pass_values(al, be, m0, xs, ws,
                                           npoly, cvec)
    ip_plus = float(ws @ (qv * qv))
    g_h = gamma_n(npoly)
    g_p = gamma_n(len(xs))
    dq = g_h * np.abs(qabs)
    ip_lo = float(np.sum(ws * np.maximum(np.abs(qv) - dq, 0.0) ** 2)) \
        * (1.0 - g_p)
    ip_hi = float(np.sum(ws * (np.abs(qv) + dq) ** 2)) * (1.0 + g_p)
    cn2_lo = cn2 * (1.0 - g_h)
    cn2_hi = cn2 * (1.0 + g_h)
    dgap = ip_plus - cn2
    lam = 1.0 - tau
    tau_ub = 1.0 - lam * lam / max(lam + dgap, 1e-300)
    t_lo = 1.0 - lam * lam / max(lam + (ip_lo - cn2_hi), 1e-300)
    t_hi = 1.0 - lam * lam / max(lam + (ip_hi - cn2_lo), 1e-300)
    res = dict(cvec=cvec, cn2=cn2, ip_plus=ip_plus, d=dgap,
               d_lo=ip_lo - cn2_hi, d_hi=ip_hi - cn2_lo,
               tau_ub=tau_ub, tau_ub_lo=min(t_lo, t_hi),
               tau_ub_hi=max(t_lo, t_hi), qv_pos=qv, dg=dg,
               dg_dev=float(np.max(np.abs(dg - 1.0))),
               dg_dev_k=int(np.argmax(np.abs(dg - 1.0))),
               p_growth=gmax, gam_h=g_h,
               qabs_max=float(np.max(qabs)),
               cancel=float(np.max(qabs) / max(1e-300, float(
                   np.max(np.abs(qv))))))
    rng = np.random.default_rng(OPROBE_SEED)
    rvec = rng.standard_normal(npoly)
    rvec = rvec / float(np.linalg.norm(rvec))
    rq_v, _ra, _rd, _rg = chain_pass_values(al, be, m0, xs, ws,
                                            npoly, rvec)
    orv = chain_pass_project(al, be, m0, xs, ws, npoly, rq_v)
    res["oprobe"] = float(np.linalg.norm(orv - rvec))
    res["rvec"] = rvec
    cc = cvec / max(1e-300, float(np.linalg.norm(cvec)))
    best = tau_ub
    hist = []
    for _ in range(NREF):
        hc = pn.T @ (vs * (pn @ cc))
        nh = float(np.linalg.norm(hc))
        if not math.isfinite(nh) or nh <= 0.0:
            break
        cc = hc / nh
        qv2, _qa2, _dg2, _gm2 = chain_pass_values(al, be, m0, xs, ws,
                                                  npoly, cc)
        occ = float(ws @ (qv2 * qv2))
        num = float(cc @ (pn.T @ (vs * (pn @ cc))))
        if occ > 0.0 and math.isfinite(num):
            val = 1.0 - num / occ
            hist.append(val)
            best = min(best, val)
    res["tau_ub_ref"] = best
    res["ref_hist"] = hist
    return res


# ================================================= the stage instrument
def stage_audit(crow, arow):
    """THE FIVE-STAGE INSTRUMENT: the chain route against the arbiter
    route on ONE cell, stage by stage."""
    dat = crow["dat"]
    M, h, L = dat["M"], dat["h"], crow["L"]
    if "chain" not in crow or "ideal" not in crow \
            or "zvec" not in crow:
        return None
    ch = crow["chain"]
    idl = crow["ideal"]
    xs, ws, ys, vs = ch["xs"], ch["ws"], ch["ys"], ch["vs"]
    uf_p, uf_n, pn = ch["uf_p"], ch["uf_n"], ch["pn"]
    al, be, m0 = ch["al"], ch["be"], ch["m0"]
    th, wsig = arow["frame"]["th"], arow["frame"]["wsig"]
    gseq = arow["frame"]["gseq"]
    st = dict(h=h, M=M)

    # ---- S1 THE INPUT: the arm tie between the two routes
    wp_ref = np.abs(wsig[uf_p])
    wn_ref = np.abs(wsig[uf_n])
    dev_p = float(np.max(np.abs(ws - wp_ref)))
    dev_n = float(np.max(np.abs(vs - wn_ref)))
    sc_w = float(max(np.max(ws), np.max(vs)))
    dev_x = float(np.max(np.abs(xs - np.cos(th[uf_p]))))
    dev_y = float(np.max(np.abs(ys - np.cos(th[uf_n]))))
    st["S1"] = dict(dev_wp=dev_p, dev_wn=dev_n, dev_x=dev_x,
                    dev_y=dev_y, w_scale=sc_w,
                    bar=ARM_ULP * EPS64 * sc_w,
                    n_pos=(int(len(xs)), arow["n_pos"]),
                    n_neg=(int(len(ys)), arow["n_neg"]))

    # ---- S3a the moment vector and ROUTE B's witness coefficients
    cvec = idl["cvec"]
    gvals = np.zeros(M)
    gvals[uf_n] = np.sqrt(vs) * crow["zvec"]
    mvec = moment_transform(gvals, M, L)
    degs = sorted(set(int(round(x)) for x in np.unique(
        np.geomspace(1, max(2, h - 1), DEG_PROBE))))
    t_b = time.time()
    rb = cheb_pass(al, be, m0, h, mvec=mvec, cvec=cvec, degs=degs)
    st["t_routeB"] = time.time() - t_b
    cB = rb["cB"]
    dev_c = float(np.max(np.abs(cvec - cB)))
    st["S3c"] = dict(dev_c=dev_c, n_c=float(np.linalg.norm(cvec)),
                     n_cB=float(np.linalg.norm(cB)),
                     rel=dev_c / max(1e-300, float(np.max(np.abs(
                         cvec)))),
                     lam_chain=float(cvec @ cvec),
                     lam_B=float(cB @ cB),
                     gam_bound=float(gamma_n(h) * np.max(rb["cabs"])),
                     anorm_max=float(np.max(rb["anorm"])),
                     amax_max=float(np.max(rb["amax"])))

    # ---- S2 THE BASIS: routes A / B / C at the sampled nodes
    rng = np.random.default_rng(SAMP_SEED)
    top = np.argsort(-np.abs(crow["zvec"]))[:3]
    isn = sorted(set([0, len(ys) - 1, int(np.argmin(ys)),
                      int(np.argmax(ys))]
                     + [int(j) for j in top]
                     + [int(x) for x in rng.choice(
                         len(ys), size=min(MP_NODES, len(ys)),
                         replace=False)]))[:MP_NODES]
    isp = sorted(set([0, len(xs) - 1, int(np.argmin(xs)),
                      int(np.argmax(xs))]
                     + [int(x) for x in rng.choice(
                         len(xs), size=min(MP_NODES, len(xs)),
                         replace=False)]))[:MP_NODES]
    pa_n = chain_sample_values(al, be, m0, ys[isn], h)
    tie_n = float(np.max(np.abs(pa_n - pn[isn, :].T)))
    pa_p = chain_sample_values(al, be, m0, xs[isp], h)
    t_c = time.time()
    dev_an, mag_n, mpk_n = mp_chain_dev(al, be, m0, ys[isn], pa_n,
                                       MP_DPS, keep_k=degs)
    dev_ap, mag_p, mpk_p = mp_chain_dev(al, be, m0, xs[isp], pa_p,
                                        MP_DPS, keep_k=degs)
    st["t_routeC"] = time.time() - t_c
    # ROUTE B at the same sampled nodes, for the sampled degrees, and
    # the REFEREE VERDICT per degree: which of the two float64
    # representations of the SAME polynomial is closer to the truth
    nvb = {}
    ref_tab = []
    for k in sorted(rb["keep"]):
        nv = node_values(rb["keep"][k], M, L)
        bn, bp = nv[uf_n[isn]], nv[uf_p[isp]]
        nvb[k] = (bn, bp)
        if k in mpk_n:
            ea = float(np.max(np.abs(pa_n[k] - mpk_n[k])))
            eb = float(np.max(np.abs(bn - mpk_n[k])))
            ea2 = float(np.max(np.abs(pa_p[k] - mpk_p[k])))
            eb2 = float(np.max(np.abs(bp - mpk_p[k])))
            ref_tab.append((k, ea, eb, ea2, eb2,
                            float(np.max(np.abs(mpk_n[k])))))
    # the honest relative scale of a recurrence error at degree k is
    # the RUNNING max of |p_j|, j <= k: that is what the error was
    # amplified from
    st["S2"] = dict(tie_n=tie_n, dev_an=dev_an, mag_n=mag_n,
                    dev_ap=dev_ap, mag_p=mag_p, isn=isn, isp=isp,
                    nvb=nvb, pa_n=pa_n, pa_p=pa_p, degs=degs,
                    ref_tab=ref_tab,
                    rel_n=float(np.max(dev_an / np.maximum(
                        np.maximum.accumulate(mag_n), 1e-300))),
                    rel_p=float(np.max(dev_ap / np.maximum(
                        np.maximum.accumulate(mag_p), 1e-300))))

    # ---- S3b THE WITNESS as a polynomial: node values
    aco = rb["acc"][:h]
    eta_a = eta_of(aco, L)
    nv_a = node_values(aco, M, L)
    qneg_dir = nv_a[uf_n]
    qpos_dir = nv_a[uf_p]
    qneg_chain = pn @ cvec
    qpos_chain = idl["qv_pos"]
    can_n = float(np.max(np.abs(pn) @ np.abs(cvec))
                  / max(1e-300, float(np.max(np.abs(qneg_chain)))))
    st["S3w"] = dict(
        dev_neg=float(np.max(np.abs(qneg_dir - qneg_chain))),
        dev_pos=float(np.max(np.abs(qpos_dir - qpos_chain))),
        sc_neg=float(np.max(np.abs(qneg_chain))),
        sc_pos=float(np.max(np.abs(qpos_chain))),
        cancel_pos=idl["cancel"], cancel_neg=can_n, eta_a=eta_a,
        growth=idl["p_growth"],
        a1n=float(math.fsum(np.abs(aco).tolist())))

    # ---- S4 THE GRAM: the two arm integrals at the SAME witness
    n_chain = float(math.fsum((vs * qneg_chain ** 2).tolist()))
    d_chain = idl["ip_plus"]
    plo, phi_, nlo, nhi = arm_sums(qpos_dir, ws, qneg_dir, vs, eta_a)
    cen = certify_witness(aco, dat, th, wsig, L, gseq,
                          om3=arow.get("omega"), label="WCHAIN")
    st["S4"] = dict(n_chain=n_chain, d_chain=d_chain,
                    n_dir=0.5 * (nlo + nhi), d_dir=0.5 * (plo + phi_),
                    n_lo=nlo, n_hi=nhi, d_lo=plo, d_hi=phi_,
                    q_chain=d_chain - n_chain,
                    q_dir_lo=plo - nhi, q_dir_hi=phi_ - nlo,
                    cen=cen,
                    dg_tab=diag_o_sample(rb["keep"], uf_p, ws, M, L,
                                         idl["dg"]))
    # the metric probe on both routes at the SAME random vector
    rvec = idl["rvec"]
    rb2 = cheb_pass(al, be, m0, h, cvec=rvec)
    r_a = rb2["acc"][:h]
    nv_r = node_values(r_a, M, L)
    orv_dir = np.zeros(h)
    for k in sorted(rb["keep"]):
        nvk = node_values(rb["keep"][k], M, L)
        orv_dir[k] = math.fsum(
            (ws * nvk[uf_p] * nv_r[uf_p]).tolist())
    st["S4"]["oprobe_chain"] = idl["oprobe"]
    st["S4"]["oprobe_pairs"] = [
        (k, orv_dir[k], float(rvec[k]), orv_dir[k] - float(rvec[k]))
        for k in sorted(rb["keep"])]

    # ---- S5 THE SCALAR
    tau_ch = crow["tau"]
    st["S5"] = dict(
        tau_chain=tau_ch, tau_ideal_ub=idl["tau_ub"],
        tau_ideal_ref=idl["tau_ub_ref"],
        tau_encl=(idl["tau_ub_lo"], idl["tau_ub_hi"]),
        d=idl["d"], d_encl=(idl["d_lo"], idl["d_hi"]),
        tau_chain_route=1.0 - n_chain / max(d_chain, 1e-300),
        tau_dir_route=(plo - nhi) / max(plo, 1e-300),
        tau_dir_route_hi=(phi_ - nlo) / max(plo, 1e-300),
        lam_arb=arow["lam_arb"],
        arb_tau_ub=arow["cen"]["tau_ub"],
        arb_sign=sign_of(arow["cen"]["E1"][0], arow["cen"]["E1"][1]),
        n_neg_arb=arow.get("inertia", {}).get("n_neg"))
    # THE RE-PRICING (amendment A8).  The CCCVII enclosure prices the
    # chain's node values through the A-PRIORI summation model
    # dq = gamma_h * sum_k |c_k p_k| on the mu_+ arm ONLY, and takes
    # the mu_- side (lam = 1 - tau) as EXACT float64.  Two repairs:
    #   (i) the mu_- arm is priced too;
    #   (ii) the a-priori model is REPLACED by
    #        max(a-priori, REPR_SAFE x MEASURED representation
    #        deviation), because the a-priori model bounds only the
    #        SUMMATION of sum_k c_k p_k and NOT the recurrence error
    #        inside p_k itself -- the smoke measured it short by an
    #        order of magnitude.  Warded by XR at every audited cell.
    g_h = gamma_n(h)
    ap_n = g_h * float(np.max(np.abs(pn) @ np.abs(cvec)))
    ap_p = g_h * float(idl["qabs_max"])
    dnum = max(ap_n, REPR_SAFE * st["S3w"]["dev_neg"])
    dden = max(ap_p, REPR_SAFE * st["S3w"]["dev_pos"])
    sv = float(math.fsum(vs.tolist()))
    sw_ = float(math.fsum(ws.tolist()))
    num_hw = (2.0 * dnum * float(math.fsum(
        (vs * np.abs(qneg_chain)).tolist())) + dnum * dnum * sv)
    den_hw = (2.0 * dden * float(math.fsum(
        (ws * np.abs(qpos_chain)).tolist())) + dden * dden * sw_)
    st["S5"].update(num_hw=num_hw, den_hw=den_hw, dnum=dnum,
                    dden=dden, ap_n=ap_n, ap_p=ap_p,
                    d_hw_cccvii=0.5 * (idl["d_hi"] - idl["d_lo"]))
    # tau_ideal(q) = 1 - N/D with N, D the two arm integrals
    nlo_r, nhi_r = n_chain - num_hw, n_chain + num_hw
    dlo_r, dhi_r = d_chain - den_hw, d_chain + den_hw
    st["S5"]["repriced"] = (
        1.0 - nhi_r / max(dlo_r, 1e-300),
        1.0 - max(nlo_r, 0.0) / max(dhi_r, 1e-300))
    # the WARD on the re-pricing model: it must cover the MEASURED
    # discrepancy between the chain's arm integrals and the
    # polynomial's certified enclosure of the SAME integrals
    st["S5"]["ward_n"] = (abs(st["S4"]["n_dir"] - n_chain), num_hw)
    st["S5"]["ward_d"] = (abs(st["S4"]["d_dir"] - d_chain), den_hw)
    # THE SAFETY-FACTOR-FREE READ: the discrepancy between the two
    # float64 evaluations of Q = int q^2 dmu_+ - int q^2 dmu_- at the
    # SAME witness, against the value the chain claims for it.  A
    # ratio >= 1 means the discrepancy is as large as the decisive
    # quantity, i.e. the stage carries no sign information; opposite
    # signs EXHIBIT the flip at that stage.
    q_ch = st["S4"]["q_chain"]
    q_dr = 0.5 * (st["S4"]["q_dir_lo"] + st["S4"]["q_dir_hi"])
    st["S5"]["q_pair"] = (q_ch, q_dr)
    st["S5"]["raw_factor"] = abs(q_ch - q_dr) / max(abs(q_ch), 1e-300)
    st["S5"]["q_flip"] = (q_ch > 0.0) != (q_dr > 0.0)
    return st


def print_stage(tag, st):
    s1 = st["S1"]
    print("    S1 THE INPUT (chain arms vs the arbiter node frame): "
          "n_pos %d/%d n_neg %d/%d | max |ws - |W_pos|| %.3e, "
          "max |vs - |W_neg|| %.3e (bar %.1f ulp = %.3e on scale "
          "%.3e) | node dev %.3e / %.3e"
          % (s1["n_pos"][0], s1["n_pos"][1], s1["n_neg"][0],
             s1["n_neg"][1], s1["dev_wp"], s1["dev_wn"], ARM_ULP,
             s1["bar"], s1["w_scale"], s1["dev_x"], s1["dev_y"]))
    s2 = st["S2"]
    print("    S2 THE BASIS (per-degree representation error of the "
          "chain columns; ROUTE A = deployed node recurrence, ROUTE C "
          "= the SAME recurrence in %d-digit arithmetic, %d sampled "
          "nodes per arm; ROUTE A is sampled BITWISE from "
          "ob.eval_chain, dev %.1e)" % (MP_DPS, MP_NODES, s2["tie_n"]))
    print("       degree band   max|A-C| (mu_-)   max|p| (mu_-)   "
          "rel        max|A-C| (mu_+)   max|p| (mu_+)   rel")
    hh = st["h"]
    nb = 8
    for b in range(nb):
        lo = int(b * hh / nb)
        hi = int((b + 1) * hh / nb)
        if hi <= lo:
            continue
        dn = float(np.max(s2["dev_an"][lo:hi]))
        mn = float(np.max(s2["mag_n"][lo:hi]))
        dp = float(np.max(s2["dev_ap"][lo:hi]))
        mp_ = float(np.max(s2["mag_p"][lo:hi]))
        print("       %5d..%-5d  %.6e     %.6e   %.3e  %.6e     "
              "%.6e   %.3e"
              % (lo, hi - 1, dn, mn, dn / max(mn, 1e-300), dp, mp_,
                 dp / max(mp_, 1e-300)))
    kn = int(np.argmax(s2["dev_an"]))
    kp = int(np.argmax(s2["dev_ap"]))
    print("       argmax: mu_- at degree %d (dev %.6e, |p| %.6e, rel "
          "%.3e), mu_+ at degree %d (dev %.6e, |p| %.6e, rel %.3e)"
          % (kn, s2["dev_an"][kn], s2["mag_n"][kn],
             s2["dev_an"][kn] / max(s2["mag_n"][kn], 1e-300), kp,
             s2["dev_ap"][kp], s2["mag_p"][kp],
             s2["dev_ap"][kp] / max(s2["mag_p"][kp], 1e-300)))
    print("       THE ATTRIBUTION (both float64 representations of "
          "the SAME polynomial against the %d-digit truth; ROUTE A = "
          "node recurrence, ROUTE B = Chebyshev coefficients):"
          % MP_DPS)
    print("         degree   |A-C| mu_-    |B-C| mu_-    who    "
          "|A-C| mu_+    |B-C| mu_+    who")
    for k, ea, eb, ea2, eb2, _mg in s2["ref_tab"]:
        print("         %-8d %.4e    %.4e    %-6s %.4e    %.4e    %s"
              % (k, ea, eb, "A" if ea <= eb else "B", ea2, eb2,
                 "A" if ea2 <= eb2 else "B"))
    if s2["ref_tab"]:
        wa = max(s2["ref_tab"], key=lambda t: max(t[1], t[2]))
        print("         worst sampled degree %d: ROUTE A is off by "
              "%.4e, ROUTE B by %.4e (on |p| %.4e) -- the CLOSER "
              "representation is ROUTE %s, so the cross-route "
              "deviation |A - B| is a RESOLUTION FLOOR of float64 "
              "polynomial evaluation at this depth and within a "
              "factor 2 of max(err_A, err_B), not an error bound on "
              "the chain alone"
              % (wa[0], wa[1], wa[2], wa[5],
                 "A" if wa[1] <= wa[2] else "B"))
    s3 = st["S3c"]
    print("    S3 THE WITNESS COEFFICIENTS: |c(chain) - c(route B)| "
          "%.6e (rel %.3e), ||c|| %.10f vs %.10f -> lam = |c|^2 "
          "%.16f (chain) vs %.16f (route B), difference %+.6e; the "
          "route-B summation bound %.3e; coefficient growth "
          "max ||A_k||_1 %.3e max ||A_k||_inf %.3e"
          % (s3["dev_c"], s3["rel"], s3["n_c"], s3["n_cB"],
             s3["lam_chain"], s3["lam_B"],
             s3["lam_B"] - s3["lam_chain"], s3["gam_bound"],
             s3["anorm_max"], s3["amax_max"]))
    sw = st["S3w"]
    print("       THE WITNESS AS A POLYNOMIAL: node values of "
          "q = sum_k c_k p_k, chain recurrence vs the Chebyshev "
          "coefficients a = sum_k c_k A_k -- max dev mu_- %.6e on "
          "scale %.6e (rel %.3e), mu_+ %.6e on scale %.6e (rel "
          "%.3e); INTERNAL CANCELLATION sum|c_k p_k| / |q|: mu_- "
          "%.4e mu_+ %.4e; ||a||_1 %.4e, FFT model eta %.3e"
          % (sw["dev_neg"], sw["sc_neg"],
             sw["dev_neg"] / max(sw["sc_neg"], 1e-300), sw["dev_pos"],
             sw["sc_pos"], sw["dev_pos"] / max(sw["sc_pos"], 1e-300),
             sw["cancel_neg"], sw["cancel_pos"], sw["a1n"],
             sw["eta_a"]))
    s4 = st["S4"]
    print("    S4 THE GRAM at the SAME witness:")
    print("       int q^2 dmu_-  chain %.16e | polynomial "
          "[%.16e, %.16e] -> difference %+.6e"
          % (s4["n_chain"], s4["n_lo"], s4["n_hi"],
             s4["n_dir"] - s4["n_chain"]))
    print("       int q^2 dmu_+  chain %.16e | polynomial "
          "[%.16e, %.16e] -> difference %+.6e"
          % (s4["d_chain"], s4["d_lo"], s4["d_hi"],
             s4["d_dir"] - s4["d_chain"]))
    print("       Q = dmu_+ - dmu_-  chain %+.6e | polynomial "
          "outward [%+.6e, %+.6e] | certified kernel E3 %+.6e +-%.1e "
          "| Toeplitz-Hankel %+.6e +-%.1e | E1 %+.6e +-%.1e"
          % (s4["q_chain"], s4["q_dir_lo"], s4["q_dir_hi"],
             s4["cen"]["E3"][0], s4["cen"]["E3"][1],
             s4["cen"]["E3t"][0], s4["cen"]["E3t"][1],
             s4["cen"]["E1"][0], s4["cen"]["E1"][1]))
    print("       diag(O) census per sampled degree (chain vs route "
          "B; the chain's own indirect read was max_k |diag(O)_k - 1| "
          "<= %.2e):" % CCCVII_DIAGO)
    worst = max(s4["dg_tab"], key=lambda t: abs(t[3]))
    for k, vb, vc, dd in s4["dg_tab"][:6]:
        print("         degree %-6d route B %.16f  chain %.16f  "
              "dev %+.3e" % (k, vb, vc, dd))
    print("         worst sampled degree %d: route B %.16f chain "
          "%.16f dev %+.3e" % (worst[0], worst[1], worst[2],
                               worst[3]))
    print("       metric probe ||(O - I) r||: chain %.3e | route-B "
          "entrywise (O r)_k - r_k at the sampled degrees, worst "
          "%+.3e at degree %d"
          % (s4["oprobe_chain"],
             max((p[3] for p in s4["oprobe_pairs"]), key=abs),
             max(s4["oprobe_pairs"], key=lambda p: abs(p[3]))[0]))
    s5 = st["S5"]
    print("    S5 THE SCALAR (both signs, then the stage that carries "
          "the flip):")
    print("       CHAIN: tau %+.6e | d %+.6e outward [%+.4e, %+.4e] "
          "| tau_ideal_ub %+.6e outward [%+.4e, %+.4e] | refined "
          "%+.6e | the same read from the arm sums 1 - N/D %+.6e"
          % (s5["tau_chain"], s5["d"], s5["d_encl"][0],
             s5["d_encl"][1], s5["tau_ideal_ub"], s5["tau_encl"][0],
             s5["tau_encl"][1], s5["tau_ideal_ref"],
             s5["tau_chain_route"]))
    print("       ARBITER at the CHAIN'S OWN witness: Q/D_+ outward "
          "[%+.6e, %+.6e] -> %s"
          % (s5["tau_dir_route"], s5["tau_dir_route_hi"],
             "POSITIVE" if s5["tau_dir_route"] > 0 else
             ("NEGATIVE" if s5["tau_dir_route_hi"] < 0
              else "STRADDLE")))
    print("       ARBITER extremal: lam_min(Omega_weil) %+.6e, "
          "tau-scale read %+.6e, sign %s, exact block inertia n_neg "
          "%s" % (s5["lam_arb"], s5["arb_tau_ub"], s5["arb_sign"],
                  s5["n_neg_arb"]))
    print("       THE RE-PRICING (A8): the CCCVII enclosure prices "
          "the mu_+ arm through the A-PRIORI summation model "
          "(gamma_h sum_k |c_k p_k| = %.3e -> denominator half-width "
          "%.3e) and takes the mu_- arm (lam = 1 - tau) as EXACT "
          "float64.  The MEASURED node-value deviation is %.3e "
          "(mu_-) / %.3e (mu_+), i.e. the a-priori model is short by "
          "a factor %.1f / %.1f -- it bounds the SUMMATION, not the "
          "recurrence inside p_k.  Re-priced with "
          "max(model, %.0f x measured): numerator half-width %.3e, "
          "denominator %.3e -> tau_ideal_ub in [%+.4e, %+.4e] -- %s"
          % (s5["ap_p"], s5["d_hw_cccvii"], st["S3w"]["dev_neg"],
             st["S3w"]["dev_pos"],
             st["S3w"]["dev_neg"] / max(s5["ap_n"], 1e-300),
             st["S3w"]["dev_pos"] / max(s5["ap_p"], 1e-300),
             REPR_SAFE, s5["num_hw"], s5["den_hw"],
             s5["repriced"][0], s5["repriced"][1],
             "IT EXCLUDES ZERO" if (s5["repriced"][0] > 0.0
                                    or s5["repriced"][1] < 0.0)
             else "IT STRADDLES ZERO: the chain route cannot decide "
             "the sign at this depth"))
    print("       THE SAFETY-FACTOR-FREE READ: Q at the SAME witness "
          "is %+.6e on the chain columns and %+.6e on the polynomial "
          "-- discrepancy %.3e = %.3e x the value the chain claims; "
          "the two evaluations %s"
          % (s5["q_pair"][0], s5["q_pair"][1],
             abs(s5["q_pair"][0] - s5["q_pair"][1]),
             s5["raw_factor"],
             "DISAGREE IN SIGN: the flip is EXHIBITED at this stage"
             if s5["q_flip"] else "agree in sign"))
    print("       the re-pricing WARD (XR): the model must cover the "
          "MEASURED chain-vs-polynomial discrepancy of the same arm "
          "integrals -- mu_- |%.3e| <= %.3e %s, mu_+ |%.3e| <= %.3e %s"
          % (s5["ward_n"][0], s5["ward_n"][1],
             "OK" if s5["ward_n"][0] <= s5["ward_n"][1] else "SHORT",
             s5["ward_d"][0], s5["ward_d"][1],
             "OK" if s5["ward_d"][0] <= s5["ward_d"][1] else "SHORT"))


def val_rows_seed(cal):
    """The CAL cell as an audited row, so that the re-pricing ward is
    measured where the chain is KNOWN good as well."""
    if cal is None or cal[2] is None:
        return []
    return [dict(tag="CAL", st=cal[2])]


def defect_verdict(st):
    """The frozen (a)-verdict: the named stage or nothing."""
    s5 = st["S5"]
    chain_neg = s5["tau_ideal_ub"] < 0.0
    arb_pos = s5["arb_sign"] == "POS" and s5["n_neg_arb"] == 0
    if not (chain_neg and arb_pos):
        return "CHAIN-VALIDATED(no sign conflict at this cell: chain " \
            "tau_ideal_ub %+.3e, arbiter %s)" % (s5["tau_ideal_ub"],
                                                 s5["arb_sign"])
    s2, s4, sw = st["S2"], st["S4"], st["S3w"]
    stages = [("int q^2 dmu_-", abs(s4["n_dir"] - s4["n_chain"])),
              ("int q^2 dmu_+", abs(s4["d_dir"] - s4["d_chain"]))]
    stages.sort(key=lambda t: -t[1])
    top = stages[0]
    straddle = (s5["repriced"][0] <= 0.0 <= s5["repriced"][1])
    kn = int(np.argmax(s2["dev_an"]))
    nb = 8
    band = int(np.argmax([float(np.max(s2["dev_an"][
        int(b * st["h"] / nb):max(1 + int(b * st["h"] / nb),
                                  int((b + 1) * st["h"] / nb))]))
        for b in range(nb)]))
    if s5["raw_factor"] < 1.0 and not straddle:
        return ("CHAIN-CONFLICT-UNEXPLAINED(the sign conflict is "
                "real but the stage instrument does NOT account for "
                "it: the two evaluations of Q at the chain's own "
                "witness agree to %.3e of its value and the "
                "re-priced enclosure still excludes zero -- the "
                "defect is NOT in the chain columns and is NOT "
                "located by this probe)" % s5["raw_factor"])
    return ("CHAIN-DEFECT-LOCATED(chain-column representation error "
            "%.2e (relative %.2e) at degree %d, eighth %d/%d of the "
            "chain, chain growth %.3e -- invisible to the O-metric "
            "reads because those are built from the SAME columns; it "
            "moves %s by %.3e, and Q at the chain's own witness "
            "becomes %+.3e on the chain columns vs %+.3e on the "
            "polynomial, a discrepancy of %.2f x the claimed value%s; "
            "re-priced enclosure %s zero)"
            % (float(s2["dev_an"][kn]), s2["rel_n"], kn, band + 1, nb,
               sw["growth"], top[0], top[1], s5["q_pair"][0],
               s5["q_pair"][1], s5["raw_factor"],
               " WITH OPPOSITE SIGNS" if s5["q_flip"] else "",
               "STRADDLES" if straddle else "still excludes"))


# ========================================================== calibration
def calibration(census):
    section("CAL -- THE CALIBRATION WARD at a shallow TIE cell (where "
            "the chain is KNOWN good: CCCXV measured rtol 2.85e-06 at "
            "h 878).  The two routes, the (II) kernel identity, the "
            "arm tie and ROUTE A == ROUTE B == ROUTE C.")
    hs = np.asarray([c["h"] for c in census], float)
    cell = census[int(np.argmin(np.abs(hs - CAL_TGT)))]
    print("    CAL cell: h %d kz %d alpha %.6f M %d"
          % (cell["h"], cell["kz"], cell["alpha"], cell["M"]),
          flush=True)
    dat = window_data(cell)
    crow = chain_cell("CAL", cell, dat=dat, keep=True)
    arow = arbiter_cell("CAL", cell, dat=dat, keep_omega=True)
    if "fail" in crow:
        check("CAL0 the deployed chain builds at the TIE cell", False,
              crow["fail"], kill="K3")
        return None, None, None
    M, h = dat["M"], dat["h"]
    # (a) the (II) Weil-kernel identity against the rebuilt quadrature
    th, wsig, L = arow["frame"]["th"], arow["frame"]["wsig"], \
        arow["frame"]["L"]
    mi = np.arange(h)
    cp = np.cos(np.outer(th[wsig > 0.0], mi))
    cn = np.cos(np.outer(th[wsig < 0.0], mi))
    oq = (cp.T * wsig[wsig > 0.0]) @ cp \
        - (cn.T * (-wsig[wsig < 0.0])) @ cn
    oq = 0.5 * (oq + oq.T)
    idd = float(np.max(np.abs(arow["omega"] - oq)))
    check("CAL1 the (II) WEIL KERNEL identity: Omega_weil (lag "
          "profile only -- no fft, no fold, no quadrature, no chain) "
          "== Omega_quad (rebuilt signed measure) entrywise to %.3e "
          "<= %.0e (scale %.3e)"
          % (idd, IDENT_BAR, float(np.max(np.abs(oq)))),
          idd <= IDENT_BAR, kill="K2")
    del cp, cn, oq
    st = stage_audit(crow, arow)
    if st is None:
        check("CAL0b the chain route delivers a bad mode and an "
              "ideal tier at the TIE cell", False, kill="K3")
        return None, None, None
    s1 = st["S1"]
    check("CAL2 THE ARM TIE: ob.folded_measure_full reproduces the "
          "arbiter's signed node frame to the summation-order floor "
          "(max dev %.3e / %.3e <= %.1f ulp = %.3e; node dev %.3e / "
          "%.3e; n_pos %d == %d, n_neg %d == %d)"
          % (s1["dev_wp"], s1["dev_wn"], ARM_ULP, s1["bar"],
             s1["dev_x"], s1["dev_y"], s1["n_pos"][0], s1["n_pos"][1],
             s1["n_neg"][0], s1["n_neg"][1]),
          max(s1["dev_wp"], s1["dev_wn"]) <= s1["bar"]
          and max(s1["dev_x"], s1["dev_y"]) <= 1e-14
          and s1["n_pos"][0] == s1["n_pos"][1]
          and s1["n_neg"][0] == s1["n_neg"][1], kill="K2")
    s2 = st["S2"]
    rel_a = s2["rel_n"]
    check("CAL3 ROUTE A == ROUTE C at the shallow TIE cell: the "
          "deployed node recurrence agrees with %d-digit arithmetic "
          "to relative %.3e <= %.0e over ALL %d degrees (this is the "
          "measurement CCCVII could not make; at a shallow cell it "
          "must be clean)"
          % (MP_DPS, rel_a, 1e-9, h), rel_a <= 1e-9, kill="K3")
    s3 = st["S3c"]
    check("CAL3b THE MOMENT/COEFFICIENT WARD: ROUTE B recovers the "
          "chain's own witness coefficients from the moment vector "
          "(|c - c_B| %.3e, relative %.3e <= %.0e) -- this wards the "
          "DCT-I moment transform and the coefficient recurrence "
          "jointly, so a route-B artefact cannot masquerade as a "
          "chain defect" % (s3["dev_c"], s3["rel"], 1e-6),
          s3["rel"] <= 1e-6, kill="K3")
    sw = st["S3w"]
    rel_w = sw["dev_neg"] / max(sw["sc_neg"], 1e-300)
    check("CAL4 ROUTE A == ROUTE B at the witness: the chain's node "
          "values of q agree with the polynomial evaluation of its "
          "Chebyshev coefficients to relative %.3e <= %.0e "
          "(cancellation mu_- %.3e mu_+ %.3e)"
          % (rel_w, 1e-7, sw["cancel_neg"], sw["cancel_pos"]),
          rel_w <= 1e-7, kill="K3")
    s5 = st["S5"]
    same = (s5["tau_chain"] > 0) == (s5["lam_arb"] > 0)
    check("CAL5 the chain tau and the arbiter agree IN SIGN at the "
          "TIE cell (chain tau %+.8e, chain tau_ideal_ub %+.8e, "
          "arbiter lam_min(Omega_weil) %+.8e, arbiter tau-scale read "
          "%+.8e; the tau-scale relative gap %.3e)"
          % (s5["tau_chain"], s5["tau_ideal_ub"], s5["lam_arb"],
             s5["arb_tau_ub"], abs(s5["arb_tau_ub"] - s5["tau_chain"])
             / max(abs(s5["tau_chain"]), 1e-300)),
          same and (s5["tau_ideal_ub"] > 0) == (s5["tau_chain"] > 0),
          kill="K3")
    print("       (the tau-scale reads are the SAME ideal object in "
          "two instruments; their relative gap at this cell is %.3e "
          "and the CAL_RTOL bar %.0e applies to the arbiter's own "
          "cross-coordinate spread, checked next)"
          % (abs(s5["arb_tau_ub"] - s5["tau_chain"])
             / max(abs(s5["tau_chain"]), 1e-300), CAL_RTOL))
    cen = arow["cen"]
    spread = abs(cen["E1"][0] - cen["E3"][0])
    check("CAL6 the arbiter's certified evaluators agree on its own "
          "extremal witness: E1 %+.8e +-%.1e, E3 (Weil kernel) "
          "%+.8e +-%.1e, E3t (Toeplitz-Hankel) %+.8e +-%.1e, E3d "
          "(assembled h x h) %+.8e +-%.1e; spread %.3e"
          % (cen["E1"][0], cen["E1"][1], cen["E3"][0], cen["E3"][1],
             cen["E3t"][0], cen["E3t"][1], cen["E3d"][0],
             cen["E3d"][1], spread),
          spread <= cen["E1"][1] + cen["E3"][1]
          and abs(cen["E3t"][0] - cen["E3"][0]) <= cen["E3t"][1]
          + cen["E3"][1]
          and abs(cen["E3d"][0] - cen["E3"][0]) <= cen["E3d"][1]
          + cen["E3"][1], kill="K3")
    print_stage("CAL", st)
    return crow, arow, st


# ============================================================ the field
def field_row(tag, key, cell, dat=None):
    row = arbiter_cell(tag, cell, dat=dat)
    row["key"] = key
    row["verdict"] = arb_verdict(row)
    return row


def print_arb(row):
    cen = row["cen"]
    ine = row.get("inertia", {})
    ref = CHAIN_REF.get(row.get("key", ""), None)
    print("      %-4s h %-6d kz %-4d  lam_min(Omega_weil) %+.6e  "
          "n_neg %s (2x2 %s, zero %s)  |  Q %+.6e +-%.1e (margin "
          "%.2f)  E3 %+.6e +-%.1e  |  tau-scale %+.6e outward "
          "[%+.4e, %+.4e]  |  %s   %.1f s"
          % (row["tag"], row["cell"]["h"], row["cell"]["kz"],
             row["lam_arb"], ine.get("n_neg", "-"),
             ine.get("n_2x2", "-"), ine.get("n_zero", "-"),
             cen["E1"][0], cen["E1"][1],
             abs(cen["E1"][0]) / max(cen["E1"][1], 1e-300),
             cen["E3"][0], cen["E3"][1], cen["tau_ub"],
             cen["tau_lo"], cen["tau_hi"], row["verdict"],
             row["t_cell"]))
    if ref:
        print("           the chain record at this cell: raw tau "
              "%s (%s), metric-corrected tau_ideal_ub %s (%s) -> "
              "the arbiter %s it"
              % (f4(ref[2]), ref[5],
                 f4(ref[4]) if ref[4] is not None else "n/a", ref[6],
                 "CONTRADICTS" if (ref[4] is not None
                                   and (ref[4] < 0)
                                   != (cen["E1"][0] < 0))
                 else "AGREES WITH"))


# ============================================================= controls
def controls(aud_rows, field_rows):
    section("X -- CONTROLS-MUST-FIRE (X1 scramble, X2 smooth, XW the "
            "doctored lag entry, XM the declared numerical models)")
    base = aud_rows[0]["arb"] if aud_rows else (
        field_rows[0] if field_rows else None)
    if base is None:
        check("X0 no cell built -- controls cannot run", False,
              kill="K1")
        return
    cell = base["cell"]
    for world, name in (("scramble", "X1"), ("smooth", "X2")):
        r = arbiter_cell("X-" + world[:4], cell, world=world,
                         scr_seed=SCR_SEED)
        cen = r["cen"]
        ine = r.get("inertia", {})
        fired = cen["E1"][0] < -1.0e-6 and cen["E3"][0] < -1.0e-6
        print("    %s world at h %d kz %d: lam_min(Omega_weil) %+.4e "
              "| Q(E1) %+.4e Q(E3) %+.4e | exact inertia n_neg %s of "
              "%d"
              % (world.upper(), cell["h"], cell["kz"], r["lam_arb"],
                 cen["E1"][0], cen["E3"][0], ine.get("n_neg", "-"),
                 cell["h"]), flush=True)
        check("%s the %s world DESTROYS the arbiter's wall scalar "
              "(both certified reads < -1e-6) -- the direct method "
              "DISCRIMINATES" % (name, world.upper()), fired,
              kill="K4")
        del r
    r = arbiter_cell("X-dope", cell, dope=True)
    shift = abs(r["cen"]["E1"][0] - base["cen"]["E1"][0])
    hw = base["cen"]["E1"][1]
    print("    DOPED lag entry c[M/3] scaled by 1 + %.0e: Q %+.6e vs "
          "%+.6e (shift %.3e, enclosure half-width %.3e, factor "
          "%.1f)" % (DOPE, r["cen"]["E1"][0], base["cen"]["E1"][0],
                     shift, hw, shift / max(hw, 1e-300)), flush=True)
    check("XW the certified enclosure FIRES on a DOCTORED lag entry "
          "(shift %.3e > 10 x half-width %.3e): the certificate has "
          "teeth" % (shift, hw), shift > 10.0 * hw, kill="K4")
    del r
    bad = []
    for rr in [a["arb"] for a in aud_rows] + field_rows:
        cen = rr["cen"]
        if cen["fft_dev2"] > cen["eta"]:
            bad.append("%s node %.2e>%.2e" % (rr["tag"],
                                              cen["fft_dev2"],
                                              cen["eta"]))
        if cen["w_phi"] > cen["phi_dev"]:
            bad.append("%s phi %.2e>%.2e" % (rr["tag"], cen["w_phi"],
                                             cen["phi_dev"]))
        if cen["w_bb"] > cen["b_dev"]:
            bad.append("%s b %.2e>%.2e" % (rr["tag"], cen["w_bb"],
                                           cen["b_dev"]))
    check("XM every declared numerical half-width model holds on a "
          "DISJOINT re-measurement at EVERY built arbiter cell (%s)"
          % ("; ".join(bad) if bad else
             "%d cells x 3 models clean"
             % (len(aud_rows) + len(field_rows))), not bad, kill="K2")


# ================================================================ main
def main():
    print("chain_audit_probe -- PRIME.COFINAL.CHAINAUDIT.01")
    print("SPEC_SHA %s  CODE_SHA %s%s"
          % (SPEC_SHA[:16], CODE_SHA[:16],
             "  [SMOKE]" if SMOKE else ""))
    section("S0 -- firewall + anti-circularity")
    bad = ast_scan(BANNED_IDS)
    check("S0.1 AST firewall: no prime/zero oracle identifier (%s)"
          % (",".join(sorted(set(bad))) or "clean"), not bad,
          kill="K1")
    bad_r = ast_scan_functions(READER_FUNCS, READER_BANNED)
    check("S0.2 AC the readers (evaluators, chain passes, coefficient "
          "pass, mp referee, transforms, arm sums) see nodes, "
          "weights, entries, coefficients, recurrence data and frozen "
          "constants only -- no eigensolver, no inverse, no tau (%s)"
          % (",".join(sorted(set(bad_r))) or "clean"), not bad_r,
          kill="K1")

    build_tables()
    if KILLS:
        return finish([], None)
    census = deep_census()
    if KILLS:
        return finish([], None)
    by_key = {(c["h"], c["kz"]): c for c in census}

    cal = calibration(census)
    if any(k in ("K1", "K2", "K3") for k in KILLS):
        return finish([], None)

    # ---------------- the priority queue with the honest cost guard
    aud_keys = AUD_KEYS
    if SMOKE:
        hs = np.asarray([c["h"] for c in census], float)
        scell = census[int(np.argmin(np.abs(hs - 1200)))]
        aud_plan = [("S1", None, scell)]
        field_plan = []
        val_plan = []
    else:
        aud_plan = [("D%d" % (i + 1), k,
                     by_key[(CHAIN_REF[k][0], CHAIN_REF[k][1])])
                    for i, k in enumerate(aud_keys)]
        field_plan = [(k, by_key[(CHAIN_REF[k][0], CHAIN_REF[k][1])])
                      for k in G1_KEYS + FIELD_NEW + FIELD_CTRL]
        hs = np.asarray([c["h"] for c in census], float)
        val_plan = [census[int(np.argmin(np.abs(hs - t)))]
                    for t in VAL_TGT]

    section("AUD -- THE STAGE-BY-STAGE AUDIT of the chain route "
            "against the arbiter at the CASE-D cells (guard %.2f x "
            "(%.1e + %.1e) x h^3 <= %.0f s)"
            % (GUARD_FAC, COST_CHAIN, COST_ARB, BUILD_CAP_S))
    aud_rows = []
    for tag, key, cell in aud_plan:
        est = GUARD_FAC * (COST_CHAIN + COST_ARB) * float(
            cell["h"]) ** 3
        if time.time() - T0 + est > BUILD_CAP_S:
            print("    %-4s h %-6d kz %-4d UNBUILT-GUARD (est %.0f s, "
                  "elapsed %.0f s, cap %.0f s)"
                  % (tag, cell["h"], cell["kz"], est,
                     time.time() - T0, BUILD_CAP_S), flush=True)
            continue
        print("\n  --- %s: h %d kz %d alpha %.4f M %d"
              % (tag, cell["h"], cell["kz"], cell["alpha"],
                 cell["M"]), flush=True)
        dat = window_data(cell)
        crow = chain_cell(tag, cell, dat=dat, keep=True)
        if "fail" in crow:
            print("      chain build FAILED (%s)" % crow["fail"])
            continue
        arow = arbiter_cell(tag, cell, dat=dat, keep_omega=True)
        arow["key"] = key
        arow["verdict"] = arb_verdict(arow)
        print("      chain: tau %+.6e  negA %d  n_pos %d n_neg %d  "
              "trace(gram) %.6e  chain build %.1f s"
              % (crow["tau"], crow["n_negA"], crow["n_pos"],
                 crow["n_neg"], crow["tr_gram"], crow["t_cell"]),
              flush=True)
        st = stage_audit(crow, arow)
        if st is None:
            print("      chain route delivered no bad mode / ideal "
                  "tier -- cell SKIPPED and typed")
            continue
        print_stage(tag, st)
        vd = defect_verdict(st)
        print("      DEFECT VERDICT: %s" % vd, flush=True)
        aud_rows.append(dict(tag=tag, key=key, cell=cell, chain=crow,
                             arb=arow, st=st, verdict=vd))
        del crow["chain"], arow["omega"]

    # ---------------- the reproduction gates
    section("G -- THE REPRODUCTION GATES (both signs must be "
            "reproduced before either is explained)")
    g1_bad = []
    g2_bad = []
    for a in aud_rows:
        key = a["key"]
        ref = CHAIN_REF.get(key)
        if ref is None:
            continue
        st = a["st"]["S5"]
        rt = abs(st["tau_chain"] - ref[2]) / max(abs(ref[2]), 1e-300)
        ru = abs(st["tau_ideal_ub"] - ref[4]) / max(abs(ref[4]),
                                                    1e-300)
        rd = abs(st["d"] - ref[3]) / max(abs(ref[3]), 1e-300) \
            if ref[3] is not None else 0.0
        print("    G2 %-5s chain tau %+.8e vs CCCVII %+.4e (rel "
              "%.3e) | d %+.8e vs %s (rel %.3e) | tau_ideal_ub "
              "%+.8e vs %+.4e (rel %.3e) | negA %d"
              % (key, st["tau_chain"], ref[2], rt, st["d"],
                 f4(ref[3]) if ref[3] is not None else "n/a", rd,
                 st["tau_ideal_ub"], ref[4], ru,
                 a["chain"]["n_negA"]))
        if not (rt <= REPRO_RTOL and ru <= REPRO_RTOL
                and rd <= REPRO_RTOL and a["chain"]["n_negA"] == 1):
            g2_bad.append(key)
    if SMOKE:
        print("    G1 / G2 SMOKE-SKIPPED by design (no frontier cell "
              "is built in the smoke, so no reference value is "
              "reproducible) -- typed, not silently passed")
    if aud_rows and not SMOKE:
        check("G2 THE CHAIN REPRODUCTION: the CCCVII tau, metric gap "
              "d and tau_ideal_ub are reproduced at every audited "
              "case-D cell inside rtol %.0e with negA = 1 (%s)"
              % (REPRO_RTOL, ",".join(g2_bad) if g2_bad
                 else "%d/%d clean" % (len(aud_rows),
                                       len(aud_rows))),
              not g2_bad, kill="K5")
    xr_bad = []
    for a in aud_rows + [r for r in val_rows_seed(cal)]:
        s5 = a["st"]["S5"] if "st" in a else None
        if s5 is None:
            continue
        if s5["ward_n"][0] > s5["ward_n"][1]:
            xr_bad.append("%s mu_- %.2e>%.2e" % (a["tag"],
                                                 s5["ward_n"][0],
                                                 s5["ward_n"][1]))
        if s5["ward_d"][0] > s5["ward_d"][1]:
            xr_bad.append("%s mu_+ %.2e>%.2e" % (a["tag"],
                                                 s5["ward_d"][0],
                                                 s5["ward_d"][1]))
    check("XR THE RE-PRICING WARD (amendment A8): the re-priced "
          "half-widths max(a-priori, %.0f x measured) COVER the "
          "measured chain-vs-polynomial discrepancy of both arm "
          "integrals at every audited cell (%s)"
          % (REPR_SAFE, "; ".join(xr_bad) if xr_bad
             else "%d cells x 2 arms clean" % (len(aud_rows) + 1)),
          not xr_bad, kill="K2")

    section("FIELD -- THE RE-ADJUDICATION of the ENTIRE former-NEGA "
            "field with the Weil-kernel-direct method as arbiter "
            "(exact block inertia; a POSITIVE read is 'no witness "
            "found', never 'positivity certified')")
    field_rows = []
    for a in aud_rows:
        field_rows.append(a["arb"])
        print_arb(a["arb"])
    for key, cell in field_plan:
        est = GUARD_FAC * COST_ARB * float(cell["h"]) ** 3
        if time.time() - T0 + est > BUILD_CAP_S:
            print("      %-4s h %-6d kz %-4d UNBUILT-GUARD (est %.0f "
                  "s, elapsed %.0f s, cap %.0f s)"
                  % (key, cell["h"], cell["kz"], est,
                     time.time() - T0, BUILD_CAP_S), flush=True)
            continue
        row = field_row(key, key, cell)
        field_rows.append(row)
        print_arb(row)
    for key in (G1_KEYS if not SMOKE else ()):
        rr = [r for r in field_rows if r.get("key") == key]
        if not rr:
            g1_bad.append("%s UNBUILT" % key)
            continue
        cen = rr[0]["cen"]
        ine = rr[0].get("inertia", {})
        ref = ARB_REF.get(key)
        rel = abs(cen["tau_ub"] - ref[1]) / max(abs(ref[1]), 1e-300)
        lam_ok = True
        if ref[0] is not None:
            lam_ok = abs(rr[0]["lam_arb"] - ref[0]) \
                <= ARB_RTOL * abs(ref[0])
        print("    G1 %-5s arbiter tau-scale %+.8e vs CCCXV %+.4e "
              "(rel %.3e) | lam_min %+.6e vs %s | n_neg %s vs %d"
              % (key, cen["tau_ub"], ref[1], rel, rr[0]["lam_arb"],
                 f4(ref[0]) if ref[0] is not None else "n/a",
                 ine.get("n_neg"), ref[2]))
        if not (cen["E1"][0] > 0.0 and ine.get("n_neg") == ref[2]
                and rel <= ARB_RTOL and lam_ok):
            g1_bad.append(key)
    for a in (aud_rows if not SMOKE else ()):
        key = a["key"]
        ref = ARB_REF.get(key)
        if ref is None:
            continue
        cen = a["arb"]["cen"]
        ine = a["arb"].get("inertia", {})
        rel = abs(cen["tau_ub"] - ref[1]) / max(abs(ref[1]), 1e-300)
        lam_ok = (ref[0] is None
                  or abs(a["arb"]["lam_arb"] - ref[0])
                  <= ARB_RTOL * abs(ref[0]))
        print("    G1 %-5s arbiter tau-scale %+.8e vs CCCXV %+.4e "
              "(rel %.3e) | lam_min %+.6e vs %s | n_neg %s vs %d"
              % (key, cen["tau_ub"], ref[1], rel, a["arb"]["lam_arb"],
                 f4(ref[0]) if ref[0] is not None else "n/a",
                 ine.get("n_neg"), ref[2]))
        if not (cen["E1"][0] > 0.0 and ine.get("n_neg") == ref[2]
                and rel <= ARB_RTOL and lam_ok):
            g1_bad.append(key)
    if field_rows and not SMOKE:
        check("G1 THE ARBITER CALIBRATION: the CCCXV certified "
              "POSITIVE enclosures and n_neg = 0 are reproduced on "
              "the shared cells inside rtol %.0e (%s)"
              % (ARB_RTOL, ",".join(g1_bad) if g1_bad
                 else "%d shared cells clean"
                 % len([k for k in ARB_REF
                        if any(r.get("key") == k
                               for r in field_rows)])),
              not g1_bad, kill="K5")

    # the gate battery runs BEFORE the validity sweep, so that a cap
    # overrun truncates the sweep (a measurement) and never the
    # controls (a gate)
    controls(aud_rows, field_rows)
    check("S1 CCXLVII tau-relocation / CCXVII c_h screens: "
          "VACUOUS-BY-CONSTRUCTION (no step formations of record, no "
          "fitted level -- an instrument audit only, declared)", True)

    # ---------------- the instrument validity sweep
    section("VAL -- THE INSTRUMENT VALIDITY DOMAIN: the chain route's "
            "decisive scalar RE-PRICED with the measured "
            "representation error, across h")
    val_rows = []
    if cal[0] is not None:
        val_rows.append(("CAL", cal[0], cal[2]))
    for a in aud_rows:
        val_rows.append((a["tag"], a["chain"], a["st"]))
    for cell in val_plan:
        est = GUARD_FAC * (COST_CHAIN + COST_ARB) * float(
            cell["h"]) ** 3
        if time.time() - T0 + est > BUILD_CAP_S:
            print("    h %-6d kz %-4d UNBUILT-GUARD (est %.0f s, "
                  "elapsed %.0f s, cap %.0f s)"
                  % (cell["h"], cell["kz"], est, time.time() - T0,
                     BUILD_CAP_S), flush=True)
            continue
        dat = window_data(cell)
        cr = chain_cell("V%d" % cell["h"], cell, dat=dat, keep=True)
        if "fail" in cr:
            continue
        ar = arbiter_cell("V%d" % cell["h"], cell, dat=dat,
                          keep_omega=True)
        stv = stage_audit(cr, ar)
        val_rows.append(("V%d" % cell["h"], cr, stv))
        del cr["chain"], ar["omega"]
    val_rows.sort(key=lambda t: t[1]["dat"]["h"])
    print("    h      tau_ideal_ub    CCCVII enclosure          "
          "RE-PRICED enclosure         Q(chain)     Q(poly)      "
          "|dQ|/|Q|   repr err   growth    sign reliable")
    h_ok = None
    h_bad = None
    for tag, cr, stv in val_rows:
        if stv is None:
            continue
        s5 = stv["S5"]
        rp = s5["repriced"]
        hh = cr["dat"]["h"]
        # the DECISIVE criterion is the safety-factor-free one: the
        # two float64 evaluations of Q at the chain's own witness must
        # agree to a fraction of the value the chain claims
        okk = (rp[0] > 0.0 or rp[1] < 0.0) and s5["raw_factor"] < 1.0
        if okk:
            h_ok = hh if h_ok is None else max(h_ok, hh)
        else:
            h_bad = hh if h_bad is None else min(h_bad, hh)
        print("    %-6d %+.6e   [%+.3e, %+.3e]  [%+.3e, %+.3e]  "
              "%+.4e  %+.4e  %.3e  %.3e  %.3e  %s"
              % (hh, s5["tau_ideal_ub"], s5["tau_encl"][0],
                 s5["tau_encl"][1], rp[0], rp[1], s5["q_pair"][0],
                 s5["q_pair"][1], s5["raw_factor"], stv["S2"]["rel_n"],
                 cr["ideal"]["p_growth"],
                 "YES" if okk else ("NO(sign flip in Q)"
                                    if s5["q_flip"] else "NO")))
    print("    (Q(chain) / Q(poly) = int q^2 dmu_+ - int q^2 dmu_- at "
          "the chain's OWN witness, evaluated on the chain columns "
          "and on the same polynomial's Chebyshev coefficients; "
          "|dQ|/|Q| is the SAFETY-FACTOR-FREE resolution ratio.  "
          "RE-PRICED = the CCCVII enclosure with amendment A8.  'sign "
          "reliable' = the re-priced enclosure excludes zero AND the "
          "resolution ratio is < 1.  MEASUREMENT on built cells, "
          "never a law.)")
    if h_ok is not None and h_bad is not None:
        if h_bad > h_ok:
            print("    THE MEASURED CROSSING: sign-reliable at "
                  "h = %d, NOT sign-reliable at h = %d -- the chain "
                  "route's 1e-10-scale sign domain ends between them "
                  "(bracket factor %.2f in h).  The boundary is NOT a "
                  "property of h alone: it is where the resolution "
                  "floor of float64 polynomial evaluation meets the "
                  "SIZE of the decisive scalar, and the deep cells "
                  "have both a larger floor and a smaller scalar."
                  % (h_ok, h_bad, h_bad / h_ok))
        else:
            print("    NO MONOTONE CROSSING on the built set "
                  "(reliable up to h = %d, unreliable already at "
                  "h = %d): the domain is NOT ordered by h alone -- "
                  "reported as measured, not smoothed" % (h_ok, h_bad))

    return finish_all(aud_rows, field_rows, val_rows, h_ok)


def finish_all(aud_rows, field_rows, val_rows, h_ok):
    section("VD -- THE VERDICT TIERS")
    labels = []
    if SMOKE:
        labels.append("CHAINAUDIT-SMOKE(no frontier cell built by "
                      "design)")
    # (a) the defect
    if aud_rows:
        print("  (a) THE NAMED DEFECT, per audited cell:")
        for a in aud_rows:
            print("      %-4s h %-6d: %s" % (a["tag"],
                                             a["cell"]["h"],
                                             a["verdict"]))
        vs = [a["verdict"].split("(")[0] for a in aud_rows]
        if all(v == "CHAIN-DEFECT-LOCATED" for v in vs):
            labels.append("CHAIN-DEFECT-LOCATED(%d/%d audited "
                          "case-D cells)" % (len(vs), len(vs)))
        elif all(v == "CHAIN-VALIDATED" for v in vs):
            labels.append("CHAIN-VALIDATED(%d/%d -- this REFUTES the "
                          "mission premise and is reported as such)"
                          % (len(vs), len(vs)))
        else:
            labels.append("AUDIT-MIXED(%s)"
                          % ";".join("%s:%s" % (a["tag"], v)
                                     for a, v in zip(aud_rows, vs)))
    # (b) the field
    if field_rows:
        print("\n  (b) THE RE-ADJUDICATED MAP (every former-NEGA "
              "cell, direct-method verdict):")
        print("      h      kz    chain raw   chain ideal   arbiter "
              "lam_min   n_neg  arbiter tau-scale  margin   verdict")
        nega = []
        posi = []
        for r in sorted(field_rows, key=lambda x: x["cell"]["h"]):
            ref = CHAIN_REF.get(r.get("key", ""), None)
            cen = r["cen"]
            ine = r.get("inertia", {})
            print("      %-6d %-5d %-11s %-13s %+.6e   %-6s %+.6e   "
                  "%7.2f  %s"
                  % (r["cell"]["h"], r["cell"]["kz"],
                     f4(ref[2]) if ref else "-",
                     (f4(ref[4]) if ref and ref[4] is not None
                      else "-"), r["lam_arb"],
                     str(ine.get("n_neg", "-")), cen["tau_ub"],
                     abs(cen["E1"][0]) / max(cen["E1"][1], 1e-300),
                     r["verdict"].split("(")[0]))
            if r["verdict"].startswith("DIRECT-NEG"):
                nega.append(r)
            elif r["verdict"].startswith("DIRECT-POS"):
                posi.append(r)
        former = [r for r in field_rows
                  if CHAIN_REF.get(r.get("key", ""), (0,) * 7)[5]
                  in ("NEGA", "MARGINAL")
                  or CHAIN_REF.get(r.get("key", ""),
                                   (0,) * 7)[6] == "NEG"]
        f_pos = [r for r in former
                 if r["verdict"].startswith("DIRECT-POS")]
        if former and len(f_pos) == len(former):
            labels.append("FIELD-ALL-DIRECT-POSITIVE(%d/%d "
                          "former-NEGA cells read n_neg = 0 with a "
                          "certified positive enclosure)"
                          % (len(f_pos), len(former)))
            print("\n      THE CONSEQUENCE, stated plainly: on the "
                  "BUILT set every cell that was ever read NEGA or "
                  "witness-NEGA is DIRECT-POSITIVE under the "
                  "Weil-kernel-direct method with exact block "
                  "inertia n_neg = 0.  The hole field of CCXCIX, the "
                  "band of CCCV and the witness cells of "
                  "CCCVII/CCCXVII are, on this instrument, CHAIN "
                  "ARTEFACTS: the deployed family's ideal legality "
                  "has NO measured end on the built set, the "
                  "corrected sub-ladder extends through every tested "
                  "cell, and the cofinal question REOPENS with a "
                  "clean instrument.  What is NOT claimed: that the "
                  "ideal form is positive (a positive read is only "
                  "'no witness found'), that this holds beyond the "
                  "built cells, or anything about RH.")
        elif former:
            labels.append("FIELD-MIXED(%d/%d former-NEGA cells "
                          "direct-positive; surviving negatives: %s)"
                          % (len(f_pos), len(former),
                             ",".join(str(r["cell"]["h"])
                                      for r in former
                                      if r not in f_pos)))
        _ = (nega, posi)
    # (c) the instrument
    print("\n  (c) THE INSTRUMENT VALIDITY STATEMENT:")
    built_h = [cr["dat"]["h"] for _t, cr, sv in val_rows
               if sv is not None]
    if built_h:
        gmaxes = [cr["ideal"]["p_growth"] for _t, cr, sv in val_rows
                  if sv is not None and "ideal" in cr]
        print("      built chain cells: h %s"
              % ", ".join(str(x) for x in sorted(built_h)))
        print("      chain growth census max_k,i |p_k| : %.3e .. "
              "%.3e (the CCCVII indirect read was <= %.2e)"
              % (min(gmaxes), max(gmaxes), CCCVII_GROWTH))
        if h_ok is None:
            labels.append("INSTRUMENT-VALID-TO(NONE of the built "
                          "chain cells has a re-priced enclosure "
                          "that excludes zero at the 1e-10 scale)")
        else:
            labels.append("INSTRUMENT-VALID-TO(h <= %d on the built "
                          "set; deeper cells have re-priced "
                          "enclosures that straddle zero)" % h_ok)
        print("      AFFECTED (consumed a DEEP chain read at h >= "
              "6000 whose sign is at the 1e-10 scale): CCXCIX's hole "
              "field and its FRONTIER-AMBIGUOUS verdict, CCCV's "
              "LEGHOR-TERMINATES-MEASURED(8204) and its NEGA band, "
              "CCCVII's case census (the C/B/D typing of 8003 / 8677 "
              "/ 9023 / 9447 / 9535) and its REPLICATION-REQUIRED "
              "verdict, CCCXVII's redrawn hole field, corrected "
              "sub-ladder, robustness frontier and "
              "CORRECTED-AMBIGUOUS verdict -- and any concurrent "
              "decider built on the same machinery (CCCXXI).")
        print("      UNTOUCHED (consumed ENTRY data on the 8x8 step "
              "frame plus certified rational floors, never a deep "
              "chain column read): the CCXCIII Radau/SOS class "
              "certificate and its exact proof object, the CCCIX "
              "three-part package plus tiny_checker, the CCLXXXIX / "
              "CCCI dual and coupling tiers, CCXCVII/CCCIII's "
              "alignment and three-bounds measurements at h <= 6344 "
              "(their chain reads sit at depths where the re-priced "
              "enclosure still excludes zero and their decisive "
              "scalars are O(1), not 1e-10) -- and every promoted "
              "verification module, none of which reads a deep "
              "1e-10-scale chain sign.")
        print("      THE HONEST LIMIT OF THIS STATEMENT: the arbiter "
              "is also a float64 instrument.  It never evaluates a "
              "chain (so it is immune to the representation edge "
              "measured here) and its inertia is exact-rational on "
              "the computed LDL factor, but the h x h assembly "
              "itself is float64 and its positive reads remain 'no "
              "witness found'.  Nothing here certifies positivity.")
    labels.append("GATES(G1 arbiter calibration, G2 chain "
                  "reproduction, XM model wards)")
    return finish(labels, None)


def finish(labels, _unused):
    section("V -- FROZEN VERDICT")
    n_pass = sum(1 for _n, ok in CHECKS if ok)
    n_tot = len(CHECKS)
    if KILLS:
        vmap = {"K1": "PIPELINE-BROKEN", "K2": "WARD-BROKEN",
                "K3": "CALIBRATION-BROKEN", "K4": "CONTROL-SILENT",
                "K5": "REPRO-BROKEN"}
        print("\n  VERDICT: %s" % vmap[KILLS[0]])
    elif not labels:
        print("\n  VERDICT: PIPELINE-BROKEN")
    else:
        print("\n  VERDICT: %s" % " ; ".join(labels))
        print("""
  HONEST FRAME.  Finite float64 measurements of ONE ideal object on
  TWO instruments, with OUTWARD-ROUNDED enclosures of the decisive
  scalars (exactly-rounded fsum accumulations, rigorous gamma_n
  bounds on the accumulated absolute sums, declared-and-warded FFT
  and coefficient-transform models) and a %d-digit mpmath referee for
  the chain-column representation at sampled nodes.  The audited
  object is the chain route of CCXCIX / CCCV / CCCVII / CCCXVII; the
  arbiter is the CCCXV Weil-kernel-direct assembly with exact
  Bunch-Kaufman block inertia.  A NEGATIVE certified enclosure is a
  WITNESS that the ideal form is indefinite; a POSITIVE one is only
  "no witness found" -- positivity is NOT certified anywhere here.
  Every statement is about BUILT cells of the frozen mission list,
  never all h.  No marker moves, no promotion, no re-typing of any
  certificate of record, NO RH claim, NO counterexample claim.""" %
              MP_DPS)
    print("\n  checks %d/%d PASS; SPEC_SHA %s; CODE_SHA %s; "
          "runtime %.1f s%s"
          % (n_pass, n_tot, SPEC_SHA[:8], CODE_SHA[:8],
             time.time() - T0, "; SMOKE" if SMOKE else ""))
    return n_pass, n_tot


if __name__ == "__main__":
    main()
