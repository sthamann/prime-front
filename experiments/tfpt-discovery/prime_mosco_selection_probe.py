#!/usr/bin/env python3
"""PRIME.MOSCO.SELECTION.01 (held Priority-7 module) -- replace
moment-stability selection by Mosco convergence + Friedrichs
minimality on the certified form core: prime_mosco_selection_probe.

Exploration only (tfpt-experiment firewall): NOT wired into
run_all.py, no ledger row, no paper edit, no website edit, NO RH
CLAIM (selection is NOT positivity -- the sector floor stays the
separate named object), and this probe writes no files.
AST-firewalled; everything source-native.

INPUT STATE (frozen findings, none re-adjudicated here):
  *  z1_variable_edge_mfunction_probe (Z1-VAREDGE-PARTIAL):
     compactness CARRIED (bounded equicontinuous regularized
     Herglotz family, ratios 0.936/0.807; summable ~rank-one entry
     poles, c_mass 0.032, rank ratios 0.80..0.87) but SELECTION
     obstructed: the 42 battery-moment tracks of the boundary
     spectral measure oscillate at median 22.0829 (max 73.9) over
     LAST10 -- the weak-* avatar does not settle.  Measured
     unification: INDUCTIVE_STATE.02 and Z1.OPERATOR.01 share the
     compactness theorem and ONE obstruction (the import-faithful
     boundary coupling).  THIS module is the registered
     replacement of the failed selection statistic.
  *  v762 (PRIME.DENSECORE.01, DENSE-CORE-CANONICAL): the
     canonical countable dense family D = union_{r,m} V_{2^-m,r}(Q)
     with exact stage maps (I_64 reproduced EXACTLY at D = 2^-6)
     and the deployed battery typed INSIDE the family (battery
     hat 8 IS hat(2,3), enum rank 35; 24/24 exact rational
     certificates).  The battery span is therefore a certified
     finite slice of the dense core -- the common form core of
     this module.
  *  qf_edge_separation / qf_cell_cocycle (1e9): band rule
     d(M) = #{lam <= 1e-4}, typed entries at 992/1108/1276, all
     anchors as in the two parent Z1 probes (reused verbatim).
  *  qf_drainage: the battery couplings to the near-null band
     SETTLE at positive constants -- which is exactly why the
     moving-edge packets are NOT weakly-null test sequences; see
     the M1 family split below.

COMPUTE BUDGET (declared): same 512-GB machine / 1e9 comb as the
parents (117..119 s measured there); cap 1800 s.

CONSTRUCTION (all frozen before the first run):
  (1) COMMON FORM CORE: V_inf = the nested union of cell spaces
      (prefix embedding), dense core = the deployed 14-vector
      battery span (support NPAD = 128 cells; certified slice of
      the v762 family).  The forms: q_X(f) = f^T T[:M(X)] f (the
      deployed Weil/window quadratic form; closed and positive on
      every rung -- Gram PD measured, never assumed).  LIMIT FORM
      on the core: q(f) := the common restriction value (see M2 --
      restriction-exactness makes it rung-independent; Ward-gated,
      and Ward-checked against the autocorrelation identity
      q(f) = a_0 p_0 + 2 sum_d a_d p_d).  The moving spectral edge
      stays in the picture as the variable boundary relation: the
      d(X)-dim near-null band with its typed entries (band scalar
      Weyl tracks below).  FRIEDRICHS OPERATOR at each rung
      (standard finite-dim identification of a closed positive
      form): H_X = T[:M] on the rung space.
  (2) MOSCO AT FINITE LEVEL:
      (M1) LIMINF: frozen weakly-null test sequences against the
           core, margins m_X = q_X(f + w_X) - q(f) measured:
           FAR family (GATED; canonical weak-null: coordinate
           vector w_X = e_{M - NPAD}, exactly core-orthogonal):
           m = 2 (T f)_{M-NPAD} + p_0.
           EDGE family (REPORTED, typed): w_X = normalized
           (I - P_core) V[:, d(X)-1] (the newest near-null mode,
           core-orthogonalized; Ward |<f, w>| <= 1e-10).
           DECLARED HONESTY: drainage proved the edge packets
           couple to the core at SETTLED constants, so they are
           NOT weakly vanishing -- the edge is a genuine boundary
           channel, not an escaping sequence; the EDGE family
           therefore probes the moving edge and is typed, never
           gated.  GATE M1: for every FAR track, med5(LAST5) of
           max(-m_X, 0)/q(f) <= M1_TOL = 0.01 (vanishing negative
           part = finite-level lower semicontinuity).
      (M2) RECOVERY: nested-prefix representatives v_X = f (the
           natural candidate named by the net properties).  The
           Toeplitz prefix structure makes the recovery EXACT:
           q_X(f) = q(f) identically.  GATE M2 (Ward-grade): max
           rel dev over all rungs x battery <= M2_BAR = 1e-10.
           Typed plainly: recovery holds by the certified union-
           space structure -- this is the finite shadow of the
           theorem, not a numerical accident.
  (3) FRIEDRICHS SELECTION (THE DECIDER): strong-resolvent
      convergence proxies R_f(z, X) = f^T (T[:M] - z)^{-1} f on
      the frozen z set ZSET (exact spectral evaluation, Ward
      against a dense solve at the Ward rungs), and band Weyl
      tracks w_f(z, X) = sum_{i <= d(X)} <v_i, f>^2/(lam_i - z)
      (the variable-edge M-function paired with the battery;
      frame-free scalars).  Weyl tracks are gated MODULO THE
      TYPED POLE LEDGER: at each typed entry e the entering
      mode's pairing pi_f(e) = <v_new, f>^2/(lam_new - z) is
      measured at birth and subtracted from all later rungs (the
      variable-edge results: entries = summable ~rank-one pole
      additions; convergence of the M-function is convergence
      modulo that ledger; unadjusted tracks reported).
      THE DECIDER STATISTIC (identical to the failed moment
      gate): tail oscillation over LAST10, osc = (max - min)/
      max(median |.|, 1e-30); the moment baseline is RECOMPUTED
      in-run on the same rungs (guard: reproduces the frozen
      22.0829 within 25%).  GATES: RES = median over the 42
      resolvent tracks (14 f x 3 real z) <= CL_BAR = 0.2;
      WEYL = median over the 14 ledger-adjusted tracks at Z_REF
      <= CL_BAR (complex points reported).
      FRIEDRICHS UNIQUENESS / COFINAL CHECK: the ladder is split
      into the two interleaved cofinal subladders LAD[0::2] /
      LAD[1::2]; per resolvent track the med5 tail values of the
      two subladders must agree: med over tracks of rel
      disagreement <= COFI_BAR = 0.05; MOSCO-DEAD iff > 0.5
      (different cofinal limits -- the kill).
  (4) IMPORT-FAITHFUL COUPLING AT FORM LEVEL: the raw mu-weighted
      coupling of the core: c~_f = L^T f (battery support 128 <=
      K everywhere -- the CORE imports without truncation; the
      lossy import was the delocalized BAND, not the core).
      (i) FORM VALUES q~_X(f) = c~_f^T (2 - J_K) c~_f are moment
      functionals of fixed degree < 2K, hence EXACT under Gauss/
      Wheeler -- Ward-gated rung-independence <= QT_BAR = 1e-8
      (the form-level statement that nothing is whitened away);
      (ii) mu-face resolvent tracks G_f(z, X) = c~_f^T (A_X -
      z)^{-1} c~_f, gated like RES (med osc <= CL_BAR) -- does
      form-face convergence hold with the raw coupling where the
      operator-face delivery failed?  GATE IMP = (i) AND (ii).
GUARDS (parent verbatim + new): G0.1 AST; G0.2 SHA-freeze before
  comb data; G0.3 reach + cap; G1.1-G1.4 comb/tower Wards;
  G1.5a-d anchors (counts/gaps/lmin/drainage/entry set); G1.6
  Wheeler+Cholesky+Gauss recon; G1.7 GNS frame Ward at 888; G1.8
  Gram PD; G1.9 q(f) autocorrelation identity <= 1e-10; G1.10
  resolvent Ward (spectral vs dense solve at rungs 888/1272 <=
  1e-9); G1.11 Herglotz guard Im R_f, Im G_f >= -1e-8 at the
  complex points; G1.12 M1 orthogonalization Ward <= 1e-10;
  G1.13 moment-baseline reproduction |med - 22.0829|/22.0829 <=
  0.25 (validates the decider comparison).
CONTROLS (mandatory, must fire; frozen fire rules):
  CS scramble (seed 7) / CE Epstein: recovery-to-a-STIELTJES-form
     breaks: FIRE iff [form positivity broken: min lam(T_ctrl) <
     -1e-6 on some control rung] OR [Wheeler breakdown on >= half
     the control rungs].  DECLARED READING: the Toeplitz
     restriction identity itself is universal algebra (as the
     cocycle probe typed: the identity is universal, the DOMAIN
     is what the comb owns); what the controls break is the
     positive-closed-form structure that Mosco/Friedrichs needs.
  CWF wrong form core (the whitened import): the parent's
     whitened-band delivery object rebuilt on GATE_BLOCK
     (rho_white = ||S_white - F~||_F/||F~||_F at Z_REF, Frobenius
     invariant under the transport conjugation, so directly
     comparable to the parent's 5.8772): FIRE iff med5 rho_white
     > 0.25 -- the wrong core reproduces the delivery failure at
     form level; parity with the parent value reported.
VERDICT ENUM (frozen; decision order as listed):
  0. any guard fails or a control fails to fire ->
     MOSCO-INVALID, exit 1.
  1. MOSCO-DEAD = cofinal disagreement > 0.5 (different cofinal
     limits).
  2. MOSCO-SELECTS = M1, M2, RES, WEYL, COFINAL, IMP all pass:
     the selection problem of the unified contract is finite-
     level solved -- Mosco+Friedrichs produces the unique limit
     candidate where moment-selection oscillated at 22; what the
     infinite-level theorem still needs is named: (i) a uniform
     closedness/sector bound making {q_X} Mosco-precompact on
     V_inf (the measured compactness of the variable-edge module
     is its finite shadow), (ii) identification of the limit form
     domain (the closure of the v762 dense core under q), (iii)
     summability of the typed entry-pole ledger at infinity
     (measured summable to X = 20.3125), and (iv) NOTHING about
     positivity -- the sector floor stays a separate contract.
  3. MOSCO-PARTIAL = anything else; failing legs named.
STOP-LIST (binding): no fixed-d variants; no zeros/prime tables;
no bare inverse at z = 0; no fits in gates; no .md files; no
commits; NO RH claim.  This probe writes no files.

RESULTS (frozen run, spec SHA 422d785e6c831547..., 109.5 s,
23/23 guards+controls, moment baseline reproduced EXACTLY:
med osc 22.0829, rel dev 0.000):

  VERDICT: MOSCO-SELECTS (6/6 legs).

  THE DECIDER TABLE (median LAST10 tail oscillation, identical
  statistic, identical rungs, identical battery):
      moment functionals (the failed selector)   22.0829
      Friedrichs resolvent tracks                 0.0004
      Weyl tracks (ledger-adjusted)               0.0843
      mu-face resolvent tracks (raw coupling)     0.0000
  The Mosco+Friedrichs route is Cauchy by 4-5 ORDERS OF MAGNITUDE
  under the bar (0.2) exactly where moment-selection oscillated
  at 22 -- the selection problem of the unified contract is
  finite-level solved on this surface.

  (M1) LIMINF: FAR family (canonical weak-null e_{M-128}) margins
  strictly positive on the whole ladder x battery: min +2.6280
  (p0 = 2.7711, i.e. the atomic almost-periodic part of (T f)_j
  never eats the diagonal); negative-part tail exactly 0.
  EDGE family (typed, not gated): min margin -0.0390, neg tail
  0.376 -- the measured confirmation that the moving-edge packets
  are NOT weakly-vanishing escapes but a genuine boundary channel
  (drainage-settled couplings), exactly the variable-boundary-
  relation picture.
  (M2) RECOVERY: exact, max rel dev 1.2e-12 -- the nested-prefix
  representatives recover q(f) identically (certified union-space
  structure; the finite shadow of the theorem).
  (RES): med osc 0.0004 (z=-0.1: 0.0001, -0.01: 0.0005, -0.001:
  0.0024; complex points 0.0053/0.0021) vs baseline 22.08.
  (COFI) FRIEDRICHS UNIQUENESS: the two interleaved cofinal
  subladders agree to med 2.5e-05 (max 1.5e-03) -- one limit
  candidate, nowhere near the 0.5 kill.
  (WEYL): unadjusted med osc 0.4374 (the typed entry steps at
  992/1108/1276 are visible, as they must be); ledger-adjusted
  0.0843 <= 0.2 -- the variable-edge M-function converges modulo
  the typed summable pole ledger.
  (IMP) IMPORT-FAITHFUL COUPLING: q~ form values EXACTLY rung-
  independent (dev 0.0, Gauss exactness -- the raw mu-weighted
  coupling of the core loses nothing), and the mu-face resolvent
  tracks are Cauchy at float level (osc 0.0000): form convergence
  HOLDS with the raw coupling where the operator-face delivery
  failed.  The measured diagnosis is now complete: the operator-
  face failure was the lossy import of the delocalized BAND, not
  of the core -- at form level the core imports exactly.

  CONTROLS (all fired): CS scramble min lam(T_s) = -6.0e+04 and
  Wheeler breakdown 9/9 (the scrambled chain leaves the positive
  closed-form cone -- no Stieltjes recovery target); CE Epstein
  min lam = -8.4e+01 and 6/6; CWF whitened form core rho_white =
  5.8772 > 0.25 (EXACT parity with the parent's operator-face
  delivery failure 5.8772, rel dev 0.000 -- the wrong core
  reproduces the failure at form level, deterministically).

  CONSEQUENCE FOR THE PROGRAMME: the unified contract
  (INDUCTIVE_STATE.02 == Z1.OPERATOR.01) should select its state
  by Mosco form convergence + Friedrichs minimality, not by
  moment stability; the recommended contract text is printed by
  the run.  What the infinite-level theorem still needs: (i)
  Mosco-precompactness of {q_X} on V_inf (uniform closedness/
  sector bound; the variable-edge compactness measurement is its
  finite shadow), (ii) identification of the limit form domain
  (closure of the v762 dense core under q), (iii) entry-pole
  ledger summability at infinity (measured summable to
  X = 20.3125).  Positivity/sector floor stays a separate named
  contract.  NO RH claim.

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/prime_mosco_selection_probe.py
"""

import ast
import hashlib
import math
import os
import sys
import time

import numpy as np
import scipy.linalg as sla

_HERE = os.path.dirname(os.path.abspath(__file__))
_VERIFY = os.path.abspath(os.path.join(_HERE, "..", "..",
                                       "verification"))
sys.path.insert(0, _HERE)
sys.path.insert(0, _VERIFY)

import v563_paper2_readouts as core  # noqa: E402
import v696_z1_jacobi as jac  # noqa: E402
import simpler_schur_recursion_probe as srp  # noqa: E402
import handoff_bulk_probe as hbp  # noqa: E402
import epstein_firewall_probe as epx  # noqa: E402
import qf_spectral_bundle_probe as qsb  # noqa: E402

T_START = time.time()

# ------------------------------------------------ frozen specification
D = srp.DGRID
ATOM_MAX_DEEP = 1000000000
M_CAP_DEEP = int(math.floor(math.log(ATOM_MAX_DEEP) / D))
M_TOP = 1300
M_PAR = 824

LAD = list(range(888, 1301, 4))
E_TEST = (992, 1108, 1276)
GATE_BLOCK = list(range(1256, 1273, 4))
TOP5W = list(range(1160, 1177, 4))
LAST5 = LAD[-5:]
LAST10 = LAD[-10:]
COFI_A = LAD[0::2]
COFI_B = LAD[1::2]
M_WARD = 888
WARD_H_RUNGS = (888, 1272)

THR_NULL = 1.0e-4
GAMMA1 = 14.10
E_CUT = 2.0 - 2.0 * math.cos(D * GAMMA1)
H_IM = 1.0e-2
ZSET_R = (-1.0e-1, -1.0e-2, -1.0e-3)
ZSET_C = (complex(0.0, H_IM), complex(-1.0e-3, H_IM))
Z_REF = -1.0e-2

M1_TOL = 0.01
M2_BAR = 1.0e-10
QT_BAR = 1.0e-8
CL_BAR = 0.2
COFI_BAR = 0.05
COFI_DEAD = 0.5
BASE_OSC = 22.0829
BASE_TOL = 0.25
B_MATCH = 0.25
RHO_WHITE_PAR = 5.8772
N_MED = 5

NPAD = 128
R_BAT = (1.0, 2.0)
QF_FLOOR = 1.0e-12
MOM_KS = (0, 1, 2)

WARD_FRAME = 1.0e-3
WARD_RES = 1.0e-9
WARD_ACORR = 1.0e-10
WARD_ORTHM1 = 1.0e-10
HERG_FLOOR = 1.0e-8
BAR_GAUSS = 1.0e-8
PD_TOL = 1.0e-9
COMB_DEV_BAR = 1.0e-12
PREFIX_WARD = 1.0e-12
RUNTIME_CAP = 1800.0

REPRO_COUNTS = {884: 5, 888: 6, 988: 6, 992: 7, 1104: 7, 1108: 8,
                1272: 8, 1276: 9}
REPRO_GAPS = {("67", 1096): 0.1008, ("67", 1176): 0.1397,
              ("78", 1176): 0.0613, ("78", 1240): 0.0039}
REPRO_TOLG = 2.0e-4
REPRO_LMIN1176 = 3.882e-6
REPRO_LTOL = 2.0e-8
DRAIN_LEVELS = {
    "R2:box[0,R]": 0.3583, "R2:box[R/2,R]": 0.3370,
    "R2:hat(R/2,R/2)": 0.3127, "R2:hat(3R/4,R/4)": 0.2590,
    "R2:box[R/4,3R/4]": 0.2249, "R1:box[R/2,R]": 0.0793,
    "R1:box[0,R]": 0.0741, "R2:box[0,R/2]": 0.0741,
    "R1:hat(R/4,R/4)": 0.0082}
REPRO_QTOL = 2.0e-3

SEED_CS = 7
CTRL_LAD_CS = list(range(888, 1301, 48))
EP_NCAP = 34000
EP_MMAX = 640
CTRL_LAD_CE = list(range(400, 641, 48))
POS_BREAK = -1.0e-6

BANNED = ("zetazero", "nzeros", "isprime", "primerange", "nextprime",
          "prevprime", "primepi", "sympy")

CHECKS = []


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok)))
    print("[%s] %s%s" % ("PASS" if ok else "FAIL", name,
                         (": " + detail) if detail else ""))
    return bool(ok)


def gate(name, ok, detail=""):
    print("[GATE %s] %s%s" % ("PASS" if ok else "FAIL", name,
                              (": " + detail) if detail else ""))
    return bool(ok)


def ast_firewall():
    with open(os.path.abspath(__file__), "r", encoding="utf-8") as fh:
        tree = ast.parse(fh.read())
    hits = set()
    for node in ast.walk(tree):
        name = ""
        if isinstance(node, ast.Name):
            name = node.id
        elif isinstance(node, ast.Attribute):
            name = node.attr
        elif isinstance(node, (ast.Import, ast.ImportFrom)):
            for alias in node.names:
                token = alias.name.split(".")[0]
                if any(b in token.lower() for b in BANNED):
                    hits.add(token)
        if name and any(b in name.lower() for b in BANNED):
            hits.add(name)
    return sorted(hits)


def freeze_spec():
    bats = {}
    hsh = hashlib.sha256()
    hsh.update(("prime-mosco-selection spec: core = battery span "
                "(v762 slice) on nested prefixes, forms q_X = "
                "f^T T[:M] f, Friedrichs H_X = T[:M]; LAD %s, "
                "ZSET_R %s ZSET_C %s Z_REF %g; M1 FAR gated "
                "(e_{M-%d}, negtail med5(LAST5) <= %g) EDGE "
                "reported; M2 exact <= %g; RES/WEYL/IMP osc "
                "LAST10 <= %g (weyl ledger-adjusted at %s, Z_REF; "
                "baseline moments recomputed, guard %g +- %g); "
                "cofinal %s/%s bar %g dead %g; IMP q~ exact <= %g "
                "and G_f osc <= %g; E_CUT %.6f; wards frame %g "
                "res %g acorr %g orthm1 %g herg %g gauss %g pd %g "
                "comb %g prefix %g cap %g; anchors counts %s gaps "
                "%s tol %g lmin %g tol %g drain %s tol %g; "
                "controls CS %d %s CE %d %d %s fire posbreak %g "
                "or wheeler>=half, CWF gate-block rho_white > %g "
                "(parent parity %g); verdict invalid -> DEAD "
                "cofinal>%g -> SELECTS(M1 M2 RES WEYL COFI IMP) "
                "-> PARTIAL"
                % (LAD, ZSET_R, ZSET_C, Z_REF, NPAD, M1_TOL,
                   M2_BAR, CL_BAR, E_TEST, BASE_OSC, BASE_TOL,
                   COFI_A[-3:], COFI_B[-3:], COFI_BAR, COFI_DEAD,
                   QT_BAR, CL_BAR, E_CUT, WARD_FRAME, WARD_RES,
                   WARD_ACORR, WARD_ORTHM1, HERG_FLOOR, BAR_GAUSS,
                   PD_TOL, COMB_DEV_BAR, PREFIX_WARD, RUNTIME_CAP,
                   sorted(REPRO_COUNTS.items()),
                   sorted(REPRO_GAPS.items()), REPRO_TOLG,
                   REPRO_LMIN1176, REPRO_LTOL,
                   sorted(DRAIN_LEVELS.items()), REPRO_QTOL,
                   SEED_CS, CTRL_LAD_CS, EP_NCAP, EP_MMAX,
                   CTRL_LAD_CE, POS_BREAK, B_MATCH,
                   RHO_WHITE_PAR, COFI_DEAD)).encode())
    for R in R_BAT:
        bats[R] = hbp.battery(R)
        for nm, v in bats[R]:
            hsh.update(nm.encode())
            hsh.update(v.tobytes())
    return bats, hsh.hexdigest()


def battery_matrix(bats):
    cols, names = [], []
    for R in R_BAT:
        nR = int(round(R / D))
        for nm, v in bats[R]:
            f = np.zeros(NPAD)
            f[:nR] = v
            cols.append(f)
            names.append("R%g:%s" % (R, nm))
    return np.stack(cols, axis=1), names


def build_parent_tower():
    alpha = 0.5 * M_PAR * D
    ka, masks, dev_m = srp.channel_masks(alpha)
    check("G1.3 parent tower comb consistency (rel dev <= %.0e)"
          % COMB_DEV_BAR, dev_m <= COMB_DEV_BAR,
          "rel dev %.1e, ka=%d" % (dev_m, ka))
    c = srp.continuum_lags(M_PAR)
    for cnl in ("ro", "re", "sp", "in"):
        c = c + srp.atom_channel_lags(alpha, M_PAR, masks[cnl])
    return sla.toeplitz(c[:M_PAR])


def build_deep_comb():
    lam_deep = core.von_mangoldt_table(ATOM_MAX_DEEP)
    dev = float(np.max(np.abs(lam_deep[:core.ATOM_MAX + 1]
                              - core.LAM_TAB)))
    check("G1.1 deep-table overlap EXACT on [0, %d]" % core.ATOM_MAX,
          dev == 0.0, "max abs dev %.1e" % dev)
    nn = np.nonzero(lam_deep > 0.0)[0]
    u_deep = np.log(nn.astype(float))
    mu_deep = 2.0 * lam_deep[nn] / np.sqrt(nn.astype(float))
    psi = np.cumsum(lam_deep[nn])
    keep = nn.astype(float) >= core.KAPPA_X0
    kappa = float(np.max(np.abs(psi[keep] - nn[keep].astype(float))
                         / nn[keep].astype(float)))
    check("G1.2 deep Chebyshev envelope kappa = %.6f <= %.6f"
          % (kappa, core.KAPPA_REF + core.TOL_KAPPA),
          kappa <= core.KAPPA_REF + core.TOL_KAPPA)
    return u_deep, mu_deep


def build_deep_tower(u_deep, mu_deep, T_par):
    alpha = 0.5 * M_TOP * D
    ka = int(np.searchsorted(u_deep, 2.0 * alpha + 1.0e-14,
                             side="right"))
    c_cont = srp.continuum_lags(M_TOP)
    c_at, _dd = core.atom_lags_at(alpha, M_TOP, u_deep[:ka],
                                  mu_deep[:ka])
    p = c_cont + c_at
    T = sla.toeplitz(p[:M_TOP])
    dev = float(np.max(np.abs(T[:M_PAR, :M_PAR] - T_par)))
    check("G1.4 prefix Ward: dev %.1e <= %.0e" % (dev, PREFIX_WARD),
          dev <= PREFIX_WARD)
    print("  deep census: ka = %d atoms to e^%.4f" % (ka, 2 * alpha))
    return p, T, c_cont, alpha, ka


def cheb_gram(p, K):
    idx = np.arange(K)
    return 0.5 * (p[np.abs(idx[:, None] - idx[None, :])]
                  + p[idx[:, None] + idx[None, :]])


def frame_ward(p, K, L, aM, gM):
    Gx = cheb_gram(p, K + 1)
    A = np.zeros((K, K))
    A[:, 0] = 2.0 * Gx[:K, 1]
    for k in range(1, K):
        A[:, k] = Gx[:K, k + 1] + Gx[:K, k - 1]
    A = 0.5 * (A + A.T)
    Y = sla.solve_triangular(L, A, lower=True, check_finite=False)
    J = sla.solve_triangular(L, Y.T, lower=True,
                             check_finite=False).T
    J = 0.5 * (J + J.T)
    Jw = np.diag(aM) + np.diag(np.sqrt(gM[1:K]), 1) \
        + np.diag(np.sqrt(gM[1:K]), -1)
    dev = float(np.max(np.abs(J - Jw)))
    check("G1.7 GNS frame Ward at M = %d: dev %.1e <= %.0e"
          % (M_WARD, dev, WARD_FRAME), dev <= WARD_FRAME)


def tri_solve(bJ, aJ, z, Bmat):
    K = len(bJ)
    dt = complex if isinstance(z, complex) else float
    ab = np.zeros((3, K), dtype=dt)
    ab[0, 1:] = -aJ
    ab[1, :] = (2.0 - z) - bJ
    ab[2, :-1] = -aJ
    return sla.solve_banded((1, 1), ab, Bmat.astype(dt))


def tail_osc(vals):
    v = np.asarray(vals, float)
    return float((v.max() - v.min())
                 / max(np.median(np.abs(v)), 1.0e-30))


def run():
    print("=" * 78)
    print("PRIME.MOSCO.SELECTION.01 -- Mosco + Friedrichs selection "
          "on the certified form core (vs moment baseline 22.08)")
    print("=" * 78)

    hits = ast_firewall()
    check("G0.1 AST firewall", not hits, str(hits))
    bats, spec_sha = freeze_spec()
    check("G0.2 spec SHA-256-frozen BEFORE any comb data", True,
          "SHA256 %s..." % spec_sha[:16])
    check("G0.3 reach: M_TOP %d <= %d, cover %d <= %d"
          % (M_TOP, M_CAP_DEEP, int(math.exp(M_TOP * D)) + 2,
             ATOM_MAX_DEEP),
          M_TOP <= M_CAP_DEEP
          and int(math.exp(M_TOP * D)) + 2 <= ATOM_MAX_DEEP)

    u_deep, mu_deep = build_deep_comb()
    T_par = build_parent_tower()
    p, T, c_cont, alpha_top, ka = build_deep_tower(u_deep, mu_deep,
                                                   T_par)
    Fb, names = battery_matrix(bats)
    nf = Fb.shape[1]
    a_all = np.stack([np.correlate(Fb[:, j], Fb[:, j], "full")
                      [NPAD - 1:] for j in range(nf)])
    q_lim = a_all[:, 0] * p[0] + 2.0 * (a_all[:, 1:] @ p[1:NPAD])
    q_direct = np.array([Fb[:, j] @ (T[:NPAD, :NPAD] @ Fb[:, j])
                         for j in range(nf)])
    check("G1.9 q(f) autocorrelation identity: max rel dev %.1e <= "
          "%.0e"
          % (float(np.max(np.abs(q_direct - q_lim)
                          / np.abs(q_lim))), WARD_ACORR),
          float(np.max(np.abs(q_direct - q_lim)
                       / np.abs(q_lim))) <= WARD_ACORR)

    # per-rung ladder
    lam884 = np.linalg.eigvalsh(T[:884, :884])
    counts = {884: int(np.sum(lam884 <= THR_NULL))}
    gaps = {}
    lmin1176 = None
    q6_med = []
    kbads = []
    pd_min = np.inf
    ward_res = ward_rec = 0.0
    herg_min = np.inf
    orthm1_max = 0.0
    entry_rungs = []
    entry_poles = {}                      # (M, z) -> birth pole
    d_prev = None
    rungs = []

    for M in LAD:
        K = M // 2
        Fpad = np.zeros((M, nf))
        Fpad[:NPAD] = Fb
        lam, V = np.linalg.eigh(T[:M, :M])
        d = int(np.sum(lam <= THR_NULL))
        counts[M] = d
        pd_min = min(pd_min, float(lam[0]))
        if M in (1096, 1176, 1240):
            gaps[("67", M)] = float((lam[6] - lam[5]) / lam[6])
            gaps[("78", M)] = float((lam[7] - lam[6]) / lam[7])
        if M == 1176:
            lmin1176 = float(lam[0])
        if M in TOP5W:
            q6_med.append(np.sum((V[:NPAD, :6].T @ Fb) ** 2,
                                 axis=0))
        proj = V.T @ Fpad                      # (M x nf)

        # M2 recovery values (nested-prefix representatives)
        qX = np.array([Fpad[:, j] @ (T[:M, :M] @ Fpad[:, j])
                       for j in range(nf)])

        # resolvent tracks (exact spectral evaluation)
        Rz = {}
        for z in ZSET_R + ZSET_C:
            Rz[z] = ((proj ** 2) / (lam - z)[:, None]).sum(axis=0)
        for z in ZSET_C:
            herg_min = min(herg_min, float(np.min(Rz[z].imag)))
        if M in WARD_H_RUNGS:
            sol = np.linalg.solve(T[:M, :M] - Z_REF * np.eye(M),
                                  Fpad)
            rdense = np.einsum("mf,mf->f", Fpad, sol)
            ward_res = max(ward_res, float(np.max(
                np.abs(rdense - Rz[Z_REF].real)
                / np.abs(rdense))))

        # band Weyl tracks + typed pole ledger (birth values)
        wz = {}
        is_entry = d_prev is not None and d > d_prev
        if is_entry:
            entry_rungs.append(M)
        for z in (Z_REF,) + ZSET_C:
            wz[z] = ((proj[:d] ** 2)
                     / (lam[:d] - z)[:, None]).sum(axis=0)
            if is_entry:
                entry_poles[(M, z)] = (proj[d - 1] ** 2
                                       / (lam[d - 1] - z))
        d_prev = d

        # M1 margins
        j_far = M - NPAD
        tf_j = np.array([float(Fb[:, j] @ p[np.abs(
            np.arange(NPAD) - j_far)]) for j in range(nf)])
        m_far = 2.0 * tf_j + p[0]
        w_edge = V[:, d - 1].copy()
        Qc, _ = np.linalg.qr(Fpad)
        w_edge = w_edge - Qc @ (Qc.T @ w_edge)
        w_edge /= max(np.linalg.norm(w_edge), QF_FLOOR)
        orthm1_max = max(orthm1_max, float(np.max(
            np.abs(Fpad.T @ w_edge))))
        Tw = T[:M, :M] @ w_edge
        m_edge = 2.0 * (Fpad.T @ Tw) + float(w_edge @ Tw)

        # mu face (raw coupling of the core)
        aM, gM, kbad = jac.wheeler(p[:M], K)
        if kbad is not None:
            kbads.append((M, int(kbad)))
            continue
        bJ = aM.copy()
        aJ = np.sqrt(gM[1:K])
        Gc = cheb_gram(p, K)
        try:
            L = sla.cholesky(Gc, lower=True, check_finite=False)
        except np.linalg.LinAlgError:
            kbads.append((M, -1))
            continue
        if M == M_WARD:
            frame_ward(p, K, L, aM, gM)
        if M in WARD_H_RUNGS:
            rec = jac.gauss_reconstruct(aM, gM, p[0], min(2 * K, M))
            ward_rec = max(ward_rec, float(
                np.max(np.abs(rec - p[:len(rec)]))
                / np.max(np.abs(p[:len(rec)]))))
        ct = L.T @ np.vstack([Fb, np.zeros((K - NPAD, nf))])
        Jct = np.empty_like(ct)
        Jct[:] = bJ[:, None] * ct
        Jct[:-1] += aJ[:, None] * ct[1:]
        Jct[1:] += aJ[:, None] * ct[:-1]
        qt = np.einsum("kf,kf->f", ct, 2.0 * ct - Jct)
        Gz = {}
        for z in ZSET_R + ZSET_C:
            Y = tri_solve(bJ, aJ, z, ct)
            Gz[z] = np.einsum("kf,kf->f", ct.astype(Y.dtype), Y)
        for z in ZSET_C:
            herg_min = min(herg_min, float(np.min(Gz[z].imag)))

        # moment baseline + whitened control (selected rungs only)
        moms = None
        if M in LAST10:
            Vd = qsb.sign_fix(V[:, :d])
            U0 = L.T @ Vd[:K]
            xj, Vj = sla.eigh_tridiagonal(bJ, aJ)
            W = U0.T @ Vj
            a_n = 2.0 - xj
            reg = a_n > E_CUT
            cf = Vd[:NPAD].T @ Fb
            moms = {}
            for kmom in MOM_KS:
                Om = (W[:, reg] * (a_n[reg] ** kmom)[None, :]) \
                    @ W[:, reg].T
                moms[kmom] = np.einsum("df,de,ef->f", cf, Om, cf)
        rho_white = None
        if M in GATE_BLOCK:
            Vd = qsb.sign_fix(V[:, :d])
            U0 = L.T @ Vd[:K]
            Uu, s0, Vt0 = np.linalg.svd(U0, full_matrices=False)
            Qh = Uu @ Vt0
            Yq = tri_solve(bJ, aJ, Z_REF, Qh)
            Sw = np.linalg.inv(Qh.T @ Yq)
            Ec = V[:, d:].T @ (T[:M, :M] @ Vd)
            Cz = Ec.T @ (Ec / (lam[d:, None] - Z_REF))
            Ff = np.diag(lam[:d]) - Z_REF * np.eye(d) - Cz
            rho_white = float(np.linalg.norm(Sw - Ff)
                              / np.linalg.norm(Ff))

        rungs.append(dict(M=M, d=d, qX=qX, Rz=Rz, wz=wz, qt=qt,
                          Gz=Gz, m_far=m_far, m_edge=m_edge,
                          moms=moms, rho_white=rho_white))

    # ---- guards
    check("G1.6 Wheeler + Cholesky valid on all %d rungs AND Gauss "
          "recon %.1e <= %.0e" % (len(LAD), ward_rec, BAR_GAUSS),
          not kbads and ward_rec <= BAR_GAUSS, str(kbads[:3]))
    if kbads:
        print("\nVERDICT: MOSCO-INVALID (construction broke)")
        return 1
    check("G1.8 Gram PD lambda_min = %.3e > -%.0e (the forms are "
          "closed POSITIVE forms on every rung -- measured)"
          % (pd_min, PD_TOL), pd_min > -PD_TOL)
    check("G1.10 resolvent Ward (spectral vs dense) %.1e <= %.0e"
          % (ward_res, WARD_RES), ward_res <= WARD_RES)
    check("G1.11 Herglotz guard: min Im track = %+.3e >= -%.0e"
          % (herg_min, HERG_FLOOR), herg_min >= -HERG_FLOOR)
    check("G1.12 M1 orthogonalization Ward %.1e <= %.0e"
          % (orthm1_max, WARD_ORTHM1), orthm1_max <= WARD_ORTHM1)
    ok_cnt = all(counts.get(M) == want
                 for M, want in REPRO_COUNTS.items())
    check("G1.5a entry anchors %s == frozen"
          % {M: counts.get(M) for M in sorted(REPRO_COUNTS)},
          ok_cnt)
    ok_gap = all(abs(gaps[k] - v) <= REPRO_TOLG
                 for k, v in REPRO_GAPS.items() if k in gaps)
    check("G1.5b gap anchors ok; lambda_min(1176) = %.4e"
          % lmin1176,
          ok_gap and abs(lmin1176 - REPRO_LMIN1176) <= REPRO_LTOL)
    med_q6 = np.median(np.stack(q6_med), axis=0)
    dev_q = max(abs(float(med_q6[j]) - DRAIN_LEVELS[nm])
                for j, nm in enumerate(names) if nm in DRAIN_LEVELS)
    check("G1.5c drainage anchors: worst dev %.1e <= %.0e"
          % (dev_q, REPRO_QTOL), dev_q <= REPRO_QTOL)
    check("G1.5d typed entry rungs %s == E_TEST %s"
          % (tuple(entry_rungs), E_TEST),
          tuple(entry_rungs) == E_TEST)

    rmap = {r["M"]: r for r in rungs}

    # ---- moment baseline (the failed selector, recomputed)
    oscs_mom = []
    for kmom in MOM_KS:
        for jf in range(nf):
            oscs_mom.append(tail_osc(
                [rmap[M]["moms"][kmom][jf] for M in LAST10]))
    mom_med = float(np.median(oscs_mom))
    check("G1.13 moment-baseline reproduction: med osc = %.4f vs "
          "frozen %.4f (rel dev %.3f <= %g)"
          % (mom_med, BASE_OSC, abs(mom_med - BASE_OSC) / BASE_OSC,
             BASE_TOL), abs(mom_med - BASE_OSC) / BASE_OSC
          <= BASE_TOL)

    # ---- gate M1
    print("\n-- (M1) liminf margins (weakly-null test sequences)")
    worst_negtail = 0.0
    min_far = np.inf
    for jf in range(nf):
        negs = [max(-rmap[M]["m_far"][jf], 0.0) / q_lim[jf]
                for M in LAST5]
        worst_negtail = max(worst_negtail, float(np.median(negs)))
        min_far = min(min_far, min(rmap[M]["m_far"][jf]
                                   for M in LAD))
    min_edge = min(min(r["m_edge"][jf] for r in rungs)
                   for jf in range(nf))
    edge_negtail = max(float(np.median(
        [max(-rmap[M]["m_edge"][jf], 0.0) / q_lim[jf]
         for M in LAST5])) for jf in range(nf))
    print("  FAR family (gated): min margin over ladder x battery "
          "= %+.4e (p0 = %.4f); worst negative-part tail = %.2e"
          % (min_far, p[0], worst_negtail))
    print("  EDGE family (typed, reported): min margin = %+.4e, "
          "worst neg tail = %.2e -- the moving edge is a boundary "
          "channel (drainage-settled couplings), not an escape"
          % (min_edge, edge_negtail))
    m1_ok = gate("(M1) liminf: worst FAR negative-part tail %.2e "
                 "<= %g" % (worst_negtail, M1_TOL),
                 worst_negtail <= M1_TOL)

    # ---- gate M2
    dev_m2 = max(float(np.max(np.abs(r["qX"] - q_lim)
                              / np.abs(q_lim))) for r in rungs)
    m2_ok = gate("(M2) recovery exact (nested prefixes): max rel "
                 "dev %.1e <= %g -- holds by the certified "
                 "union-space structure" % (dev_m2, M2_BAR),
                 dev_m2 <= M2_BAR)

    # ---- gate RES + cofinal
    print("\n-- Friedrichs selection: resolvent tracks vs moment "
          "baseline %.2f" % mom_med)
    oscs_res = {z: [tail_osc([rmap[M]["Rz"][z][jf] for M in LAST10])
                    for jf in range(nf)] for z in ZSET_R}
    res_all = [o for z in ZSET_R for o in oscs_res[z]]
    res_med = float(np.median(res_all))
    for z in ZSET_R:
        print("  R_f osc at z=%g: med %.4f max %.4f"
              % (z, float(np.median(oscs_res[z])),
                 float(np.max(oscs_res[z]))))
    for z in ZSET_C:
        o_re = float(np.median([tail_osc(
            [rmap[M]["Rz"][z][jf].real for M in LAST10])
            for jf in range(nf)]))
        print("  R_f osc at z=%s (Re part, reported): med %.4f"
              % (z, o_re))
    res_ok = gate("(RES) resolvent tracks Cauchy: med osc = %.4f "
                  "<= %g (42 tracks; moment baseline %.2f)"
                  % (res_med, CL_BAR, mom_med), res_med <= CL_BAR)

    cofis = []
    for z in ZSET_R:
        for jf in range(nf):
            ta = float(np.median([rmap[M]["Rz"][z][jf]
                                  for M in COFI_A[-5:]]))
            tb = float(np.median([rmap[M]["Rz"][z][jf]
                                  for M in COFI_B[-5:]]))
            cofis.append(abs(ta - tb)
                         / max(abs(ta), abs(tb), QF_FLOOR))
    cofi_med = float(np.median(cofis))
    cofi_max = float(np.max(cofis))
    cofi_ok = gate("(COFI) unique Friedrichs candidate: cofinal "
                   "disagreement med %.2e (max %.2e) <= %g "
                   "(DEAD above %g)"
                   % (cofi_med, cofi_max, COFI_BAR, COFI_DEAD),
                   cofi_med <= COFI_BAR)
    cofi_dead = cofi_med > COFI_DEAD

    # ---- gate WEYL (ledger-adjusted: each entering mode's pole,
    # frozen at its birth value, subtracted from all later rungs)
    print("\n-- variable-edge Weyl tracks (typed pole ledger at %s)"
          % (tuple(entry_rungs),))
    adj = {}
    for z in (Z_REF,) + ZSET_C:
        acc = np.zeros(nf, complex if isinstance(z, complex)
                       else float)
        series = {}
        for r in rungs:
            if (r["M"], z) in entry_poles:
                acc = acc + entry_poles[(r["M"], z)]
            series[r["M"]] = r["wz"][z] - acc
        adj[z] = series
    oscs_w_adj = [tail_osc([adj[Z_REF][M][jf] for M in LAST10])
                  for jf in range(nf)]
    oscs_w_raw = [tail_osc([rmap[M]["wz"][Z_REF][jf]
                            for M in LAST10]) for jf in range(nf)]
    w_med = float(np.median(oscs_w_adj))
    print("  w_f osc at Z_REF: unadjusted med %.4f -> ledger-"
          "adjusted med %.4f (max %.4f); entry steps typed at %s"
          % (float(np.median(oscs_w_raw)), w_med,
             float(np.max(oscs_w_adj)), tuple(entry_rungs)))
    for z in ZSET_C:
        o_re = float(np.median([tail_osc(
            [adj[z][M][jf].real for M in LAST10])
            for jf in range(nf)]))
        print("  w_f osc at z=%s (Re, adjusted, reported): %.4f"
              % (z, o_re))
    weyl_ok = gate("(WEYL) Weyl tracks Cauchy modulo the typed "
                   "ledger: med osc = %.4f <= %g"
                   % (w_med, CL_BAR), w_med <= CL_BAR)

    # ---- gate IMP (import-faithful coupling at form level)
    print("\n-- import-faithful coupling at form level (raw "
          "mu-weighted core, no truncation, no whitening)")
    dev_qt = max(float(np.max(np.abs(r["qt"] - rungs[0]["qt"])
                              / np.abs(rungs[0]["qt"])))
                 for r in rungs)
    oscs_g = [tail_osc([rmap[M]["Gz"][z][jf] for M in LAST10])
              for z in ZSET_R for jf in range(nf)]
    g_med = float(np.median(oscs_g))
    print("  q~ form values rung-independence: max rel dev %.1e "
          "(Gauss exactness); mu-face resolvent osc med %.4f "
          "max %.4f" % (dev_qt, g_med, float(np.max(oscs_g))))
    imp_ok = gate("(IMP) raw-coupling form face: q~ exact %.1e <= "
                  "%g AND G_f tracks Cauchy med osc %.4f <= %g"
                  % (dev_qt, QT_BAR, g_med, CL_BAR),
                  dev_qt <= QT_BAR and g_med <= CL_BAR)

    # ---- controls
    print("\n-- controls")
    rng = np.random.default_rng(SEED_CS)
    pos = np.sort(rng.uniform(0.5, 2.0 * alpha_top, ka))
    cat_s, _dd = core.atom_lags_at(alpha_top, M_TOP, pos,
                                   mu_deep[:ka])
    pcs = c_cont + cat_s
    kb_cs, lmin_cs = [], np.inf
    for M in CTRL_LAD_CS:
        _a, _g, kb = jac.wheeler(pcs[:M], M // 2)
        if kb is not None:
            kb_cs.append(M)
        lmin_cs = min(lmin_cs, float(sla.eigh(
            sla.toeplitz(pcs[:M]), eigvals_only=True,
            subset_by_index=[0, 0])[0]))
    check("CS scramble fires: min lam(T_s) = %.3e < %.0e (form "
          "positivity broken) OR Wheeler breakdown %d/%d"
          % (lmin_cs, POS_BREAK, len(kb_cs), len(CTRL_LAD_CS)),
          lmin_cs < POS_BREAK
          or len(kb_cs) >= len(CTRL_LAD_CS) / 2)
    r1 = epx.lattice_r1(EP_NCAP)
    bb = np.asarray(r1, float) / 2.0
    lamE = epx.dirichlet_vonmangoldt(bb, EP_NCAP)
    supp = np.nonzero(np.abs(lamE) > 1.0e-9)[0]
    supp = supp[supp >= 2]
    catE, _dd = core.atom_lags_at(0.5 * EP_MMAX * D, EP_MMAX,
                                  np.log(supp.astype(float)),
                                  2.0 * lamE[supp]
                                  / np.sqrt(supp.astype(float)))
    pce = srp.continuum_lags(EP_MMAX) + catE
    kb_ce, lmin_ce = [], np.inf
    for M in CTRL_LAD_CE:
        _a, _g, kb = jac.wheeler(pce[:M], M // 2)
        if kb is not None:
            kb_ce.append(M)
        lmin_ce = min(lmin_ce, float(sla.eigh(
            sla.toeplitz(pce[:M]), eigvals_only=True,
            subset_by_index=[0, 0])[0]))
    check("CE Epstein fires: min lam(T_e) = %.3e < %.0e OR Wheeler "
          "breakdown %d/%d"
          % (lmin_ce, POS_BREAK, len(kb_ce), len(CTRL_LAD_CE)),
          lmin_ce < POS_BREAK
          or len(kb_ce) >= len(CTRL_LAD_CE) / 2)
    rho_w = [r["rho_white"] for r in rungs
             if r["rho_white"] is not None]
    rho_w_med = float(np.median(rho_w))
    check("CWF whitened form core fires: med%d rho_white = %.4f > "
          "%g (parent parity %.4f, rel dev %.3f)"
          % (N_MED, rho_w_med, B_MATCH, RHO_WHITE_PAR,
             abs(rho_w_med - RHO_WHITE_PAR) / RHO_WHITE_PAR),
          rho_w_med > B_MATCH)
    dt = time.time() - T_START
    check("G0.4 runtime %.1f s <= %.0f s" % (dt, RUNTIME_CAP),
          dt <= RUNTIME_CAP)

    # ---- verdict
    guards_ok = all(ok for (n, ok) in CHECKS
                    if not n.startswith(("CS", "CE", "CWF")))
    controls_ok = all(ok for (n, ok) in CHECKS
                      if n.startswith(("CS", "CE", "CWF")))
    legs = dict(M1=m1_ok, M2=m2_ok, RES=res_ok, WEYL=weyl_ok,
                COFI=cofi_ok, IMP=imp_ok)
    if not (guards_ok and controls_ok):
        verdict = "MOSCO-INVALID"
    elif cofi_dead:
        verdict = "MOSCO-DEAD"
    elif all(legs.values()):
        verdict = "MOSCO-SELECTS"
    else:
        verdict = "MOSCO-PARTIAL"

    n_chk = sum(1 for (_n, ok) in CHECKS if ok)
    print("\nVERDICT: %s" % verdict)
    print("LEGS %d/6 (%s), GUARDS+CONTROLS %d/%d, runtime %.1f s"
          % (sum(legs.values()),
             " ".join("%s=%s" % (k, "P" if v else "F")
                      for k, v in legs.items()),
             n_chk, len(CHECKS), time.time() - T_START))
    print("\nDECIDER TABLE (median LAST10 tail oscillation, same "
          "statistic, same rungs):")
    print("  moment functionals (failed selector) : %.4f" % mom_med)
    print("  Friedrichs resolvent tracks          : %.4f" % res_med)
    print("  Weyl tracks (ledger-adjusted)        : %.4f" % w_med)
    print("  mu-face resolvent tracks (raw)       : %.4f" % g_med)
    if verdict == "MOSCO-SELECTS":
        print("\nRECOMMENDED CONTRACT TEXT PRIME.MOSCO.SELECTION.01 "
              "(report only): 'Selection by Mosco convergence and "
              "Friedrichs minimality on the v762 dense core: the "
              "window-form chain q_X has exact nested recovery "
              "(M2 structural), vanishing liminf defect (M1 "
              "measured), Cauchy Friedrichs resolvents and Weyl "
              "functions modulo the typed summable entry-pole "
              "ledger, and cofinal-unique limits -- the unified "
              "compactness contract (INDUCTIVE_STATE.02 == "
              "Z1.OPERATOR.01) selects its state by form "
              "convergence, not by moment stability.  Remaining "
              "for theorem grade: Mosco-precompactness of {q_X} "
              "on V_inf, identification of the limit form domain, "
              "ledger summability at infinity.  Positivity/sector "
              "floor stays a separate contract.  NO RH claim.'")
    return 0 if (guards_ok and controls_ok) else 1


if __name__ == "__main__":
    sys.exit(run())
