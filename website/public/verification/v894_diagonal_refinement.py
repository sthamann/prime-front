#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""v894 -- PRIME.CASE.PAIRCORR.CONTRACT.01 + PRIME.CASE.ENDPOINT.01 + PRIME.CASE.INNERLINEAR.01: THE CONDITIONAL DIAGONAL CONTRACT MADE CONCRETE -- the exact weighted prime-pair kernel extracted and frozen, the one-sided endpoint bracket measured, and the inner-zone accounting of the linear route, ONE module from three probes (11/11 + 13/13 + 12/12 checks, zero fails, verdicts PAIRCONTRACT-EXTRACTED (KERNEL-BANDLIMITED) + ENDPOINT-MEASURED (ENDPOINT-PARTIAL) + INNERLINEAR-MEASURED (INNER-EMPTY); discovery probes paircorr_contract_probe.py, endpoint_bracket_probe.py (SPEC v2), inner_zone_linear_probe.py (SPEC v2), rounds 50/51/52, 2026-08-09, re-run identically at promotion, embedded BYTE-EXACT and executed verbatim, ~45 s).  THE ROUTE TYPING STANDS: per v889 the diagonal route is CONDITIONAL on a pair-correlation-class arithmetic input -- nothing in this module moves that; the module makes the CONDITION concrete.  (1) THE EXACT CONTRACT (paircorr, follow-up (e) of the route decision): the weighted prime-pair correlation functional whose nonnegativity implies the diagonal testing bound T_h <= 1 on the critical zone is extracted EXACTLY -- the prime kernel K_{h,m} regroups the alias sum at defect 4.5e-15 (machine-exact regrouping ward), the kernel is KERNEL-BANDLIMITED (compact spectral support, printed), ALL 79 finite deficit margins on the frozen rung/alias census are positive, and the LaTeX contract statement is FROZEN INSIDE the probe -- the conditional reduction is now a precise registered statement with a printable formula, not prose.  (2) THE ENDPOINT BRACKET (endpoint, reviewer priority 6): by the concavity bracket F(1) - F(0) >= F'(1) a ONE-SIDED lower bound on the endpoint derivative -- a LINEAR signed-Lambda functional evaluated AT THE TRUTH, much weaker than the full pair-correlation input -- would suffice; measured: F'(1) >= deficit on 142 of 227 cells -- the GLOBAL linear collapse of the contract FAILS (typed ENDPOINT-PARTIAL, honestly), but the deep small-a cells pass with MONOTONE margins, so the linear route is real exactly where the theorem must live (deep) and dies at shallow rungs and the zone edge a ~ h^1.4.  (3) THE INNER-ZONE ACCOUNTING (innerlinear, named object (c)): under the FROZEN absolute eligibility rule the inner zone is EMPTY -- INNER-EMPTY, criterion (iii) fails at absolute min-margin h-trend -1.05 -- but the DISCLOSED scale-normalized diagnostic (SPEC v2, pure measurement: every scale of the problem -- deficit, F'(0), F'(1) -- itself shrinks like ~h^-1, so the absolute trend conflates global shrinkage with genuine decay) is FLAT at slope -0.052; the genuinely hard middle band retains ~20 percent of the aliases carrying 38..56 percent of the mass, NON-SHRINKING with depth; and the pass/fail stability is a-graded on a mid shell a/h^1.4 in 0.02..0.07.  NET: the diagonal half is now a concrete conditional contract -- an exact frozen kernel, an endpoint bracket that works on the deep half, and a measured non-shrinking hard band where the pair-correlation input (v889) is genuinely needed; the condition is localized, not removed.  NO RH claim; no marker moves; the route stays CONDITIONAL (pair-correlation class) exactly as v889 typed it.  Float64 on the deployed v563 machinery (READ-ONLY); no zeros, no prime oracles (AST firewalls inside the probes); RNG only in declared scramble controls.  Python-only per GATE.WOLFRAM.02.

PROVENANCE: discovery probes paircorr_contract_probe.py (11/11,
PAIRCONTRACT-EXTRACTED, round 50, machinery verbatim from
signed_homotopy_probe / christoffel_pnt_gamma_probe),
endpoint_bracket_probe.py (13/13, ENDPOINT-MEASURED
(ENDPOINT-PARTIAL), round 51, SPEC v2: run 1 returned WARD-BROKEN
on exactly one W-C cell (kz 88, rel 1.16e-3 vs the 1e-3 bar at
|F'(1)| = 9.2e-11); the disclosed eps-scan diagnosis identifies
the lambda-evaluation NOISE floor (abs defect x eps ~ 1e-17
constant), not stencil truncation -- fail-first output preserved,
denominator amended, no census rule moved),
inner_zone_linear_probe.py (12/12, INNERLINEAR-MEASURED
(INNER-EMPTY), round 52, SPEC v2: run 1 was green with the same
verdict; v2 ADDS two disclosed scale-normalized diagnostics to the
Z1 print -- the frozen absolute rule and its INNER-EMPTY outcome
stand unchanged), all 2026-08-09, re-run identically at promotion.
ROUND-31 EMBEDDING CONVENTION: frozen sources embedded BYTE-EXACT,
executed verbatim in isolated namespaces; printed spec SHAs
reproduce; byte-equality ward vs experiments/tfpt-discovery/
inside the pattern gates.  All probes consume the READ-ONLY
deployed core v563_paper2_readouts.py.

FIREWALL: no zeros, no prime-table oracles; all fail-first spec
amendments preserved; the extracted contract is a REDUCTION
TARGET, its nonnegativity is NOT claimed -- the diagonal route
stays typed CONDITIONAL (pair-correlation class) per v889.
NO RH claim.
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

# ------------- frozen probe source paircorr_contract_probe (embedded BYTE-EXACT, raw string)
_SRC_0 = r'''
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""paircorr_contract_probe -- PRIME.CASE.PAIRCORR.CONTRACT.01
(EXPLORATION ONLY, experiments/; round 50, follow-up (e): make the
CONDITIONAL diagonal theorem concrete -- extract, print and freeze
the EXACT weighted prime-pair correlation functional whose
nonnegativity implies T_h <= 1 on the critical zone, so the
contract can be registered as a precise conditional reduction.
2026-08-09.)

CONTEXT (machinery verbatim from signed_homotopy_probe /
christoffel_pnt_gamma_probe): round 45 measured the exact envelope
identity (lambda_1 - nu_1) - (lambda_0 - nu_0) = Int_0^1 J_{h,m} dt,
J = sum_f qt_f r_f 1{d_t(f) > 0} p_{t,m}(x_f)^2
    + qt_m r_m 1{d_t(m) < 0},
and typed the gain HOMOTOPY-INDEFINITE-ARITHMETIC with the scaling
control FIRST-ORDER-DOMINATED: the only arithmetic input is
r = the grid residual of the von Mangoldt comb vs PNT.
christoffel_pnt_gamma_probe measured the PNT reference gap NEGATIVE
on every rung, so the needed inequality is
Int_0^1 J dt >= (nu_0 - lambda_0)_m -- the gain must beat the
reference deficit.  christoffel_zone_envelope_probe froze the
critical zone a <= h^{2 theta*}, theta* = 0.700.  THIS probe
regroups the first-order gain into an explicit smoothed prime sum
(the windowed-sum linearity of port_atom_numerator_probe / v882),
extracts the second-order pair kernel on the port-mode subspace,
prints the LaTeX-ready conditional contract, and measures its
finite shadow (the margin ledger).

THE ALGEBRA (exact, frozen): the deployed atom assembly is LINEAR
in the von Mangoldt masses.  With tent_i(u) = (1 - |iD - u|/D)_+
(plus the u < D mirror of the deployed assembly), the symmetric-
extension cosine weights w_i = 1 at i in {0, M-1} else 2, and
theta_f = 2 pi f / L, the per-atom grid response is
    g_f(u) = -(1/2) sum_i tent_i(u) w_i cos(i theta_f),
so the grid residual is r(f) = sum_n mu_n g_f(u_n) - d0at(f)
(mu_n = 2 Lambda(n)/sqrt(n), u_n = log n; d0at = the grid density
of the closed-form PNT lags c0).  Regrouping the fixed-mask first
variation
    J1_{h,m} = sum_f W_{f,m} r(f),
    W_{f,m} = qt_f 1{d0(f) > 0} p_{0,m}(x_f)^2
              + qt_m 1{d0(m) < 0} delta_{fm},
gives the PRIME-SIDE FORM with the explicit node kernel
    K_{h,m}(u) = -(1/2) sum_i tent_i(u) chat_i(m),
    chat_i(m)  = w_i sum_f W_{f,m} cos(i theta_f):
    J1_{h,m} = sum_{n <= X} mu_n K_{h,m}(log n) - K0_{h,m},
    K0_{h,m} = sum_f W_{f,m} d0at(f) = sum_i c0_i chat_i(m).
K_{h,m} is THE WEIGHT the contract needs; everything above is
finite exact linear algebra on the deployed v563 window family.

FROZEN PROTOCOL (2026-08-09; constants frozen before the first
measurement run; heavy rungs only -- the deep rungs add no new
object here and the round-45 pre-sizing already showed their chain
cost; budget < 20 min):

 RUNGS: heavy kz {9, 12, 13, 26, 40} (verbatim selection).
 ALIASES: all port aliases in the frozen critical zone -- truth
   neg nodes (d1(f) < 0, f >= 1) with a_{h,f} = 2 h^2 (1 - x_f)
   <= h^{2 theta*}, theta* = 0.700, ranked by a ascending
   (verbatim round-45 bookkeeping).

 P1 THE FUNCTIONAL, EXPLICITLY (every heavy rung, every zone
   alias): build W_{f,m} from the t = 0 chain (P2 = p_{0,m}^2 by
   the CD identity, verbatim decompose route), the lag transform
   chat = w * (cos(i theta_f) @ W), the node kernel at the atoms
   K_{h,m}(u_n) (tent interpolation of -chat/2, incl. the u < D
   mirror), the prime sum S1 = sum_n mu_n K(u_n) and the smooth
   subtraction K0.  WARDS (exact algebra, float-route only):
   (W1) prime-side form == grid form:
        |S1 - K0 - W.r| / max(|W.r|, sum_n mu_n |K(u_n)| + |K0|)
        <= 1e-10 per alias;
   (W2) K0 route a (W.d0at) == route b (c0.chat), rel <= 1e-12
        against sum_i |c0_i chat_i|.
   PROFILES printed at the critical alias m* = argmin_m G_1(m)
   and at the a-closest alias (rank 1): K(u) samples on
   u/(2 alpha) in {0.10, 0.30, 0.50, 0.70, 0.85, 0.95, 1.00},
   peak location, the smallest contiguous u-window carrying 90%
   of sum_i |K(iD)| (support width), the number n90 of f-modes
   carrying 90% of sum_f |W_{f,m}| (f >= 1), the |W|-weighted
   mean alias frequency tau = 2 pi f/(L D), and the shape
   correlations corr(K, cos(tau_{m} u)) (Fejer reading) and
   corr(K, 1_window) (short-interval reading).

 P2 THE PAIR PART (frozen rungs kz {9, 40}, verbatim round-45 M4
   machinery): FD Hessian H of Phi(s) = (lambda - nu)_{m*} at
   d0 + sum_i s_i r(f_i) delta_{f_i} on the K_SUB = 12 top-|qt r|
   mask-safe grid modes (eta = 0.05, MASK_SAFE = 4, central FD,
   eta/2 diagonal drift reported); the grid-residual Hessian
   Hg_{ik} = H_{ik} / (r_i r_k) and the effective PRIME PAIR
   KERNEL C_{h,m*}(u, u') = sum_{ik} g_{f_i}(u) Hg_{ik}
   g_{f_k}(u') on a frozen 13 x 13 u-grid over [0, 2 alpha]:
   eigen-signature of H (tol 1e-3 relative), the subspace
   frequencies tau_{f_i}, the ASCII sign map of C (tol 1e-3 of
   max |C|), the diagonal profile C(u, u), and the truth-
   direction quadratic (1/2) 1.H.1 against the measured response
   remainder Delta - A - B at m* (B = the exact crossing part,
   closed form via the occupation times tau_f; reported, never a
   kill -- the subspace captures only the dominant modes).

 P3 THE CONTRACT STATEMENT (the deliverable): print the LaTeX-
   ready conditional theorem block (every object defined by the
   deployed constructions; the implication is exact finite
   calculus, see below) + the HONEST CLASSIFICATION: kernel
   typing per rung at m* by the frozen rules
     KERNEL-SHORTINTERVAL iff width90/(2 alpha) <= 0.25
                          AND n90 > 32
     KERNEL-BANDLIMITED   iff n90 <= 32
                          AND width90/(2 alpha) > 0.25
     KERNEL-MIXED         otherwise;
   contract typing = the majority over the 5 heavy rungs (tie ->
   KERNEL-MIXED).  The classical-family reading printed with the
   measured branch marked: (i) SHORTINTERVAL -> a one-sided
   short-interval prime bound at scale X = e^{2 alpha}, window
   width90 (the needed strength named against the known
   unconditional landscape -- psi(x) short-interval asymptotics
   for widths >= x^{0.525}, zero-free-region error
   exp(-c (log x)^{3/5}) -- named, NOT proved, NOT applicable at
   our tiny X); (ii) BANDLIMITED -> a Fejer-type band-limited
   one-sided explicit-formula positivity at the port frequencies
   (the pair-correlation class).  The demanded relative
   cancellation eps_need = deficit_{h,m*} / (sum_n mu_n |K(u_n)|
   + |K0|) printed per rung (the strength gauge).

 P4 THE NUMERICAL MARGIN LEDGER (every heavy rung, every zone
   alias): LHS(truth) = Delta_m = (lambda_1 - nu_1)_m -
   (lambda_0 - nu_0)_m (the measured total gain; its first-order
   part A_m = J1 printed alongside), RHS = deficit_{h,m} =
   (nu_0 - lambda_0)_m, margin = LHS - RHS = (lambda_1 - nu_1)_m
   (exact identity).  All margins positive = the finite shadow is
   CONSISTENT (measurement, never a kill; the LEDGER flag is
   attached to the verdict).

 C  CONTROLS (kz 9, scramble seed 1, the deployed mirror:
   positions uniform on (0, 2 alpha), same masses): the scramble
   LHS must fall below the deficit -- min_m (LHS_scr - deficit)
   = min_m (lambda_scr - nu_scr)_m <= 0 on the scramble zone
   aliases (fallback, disclosed if the zone set is empty: the 8
   a-closest scramble neg nodes).  Silent -> CONTROL-DEAD.

 SELF-TESTS (S0, kill PIPELINE on failure): (i) AST firewall
   clean; (ii) endpoint reconstruction (kz 9): the qt-route
   lambda/nu at the zone aliases vs the verbatim folded_measure
   route, rel <= 1e-8, at both t = 0 and t = 1; (iii) quadratic-
   form self-test per rung at both endpoints: sum_j w_j p*^2 ==
   lambda to rel 1e-8 (verbatim TOL_QF).

KILLS: chain short anywhere needed / self-test failure / zone
alias set empty on a rung -> PIPELINE-BROKEN; W1 or W2 ward
failure -> WARD-BROKEN; value control silent -> CONTROL-DEAD.
P2/P3/P4 outcomes are MEASUREMENTS, never kills.

VERDICT (frozen enum): PAIRCONTRACT-EXTRACTED (+ KERNEL=<typing>
+ LEDGER=<CONSISTENT | INCONSISTENT k/N>) / PIPELINE-BROKEN /
WARD-BROKEN / CONTROL-DEAD.

SPEC AMENDMENTS (fail-first preserved):
  v1 (2026-08-09): initial freeze.  The M4 constants (K_SUB = 12,
  eta = 0.05, MASK_SAFE = 4, EIG_TOL = 1e-3) are the round-45
  frozen values, reused verbatim; the typing thresholds (0.25 /
  32 / 90%) and the 13 x 13 pair grid are frozen a priori, before
  any kernel was computed.

NO RH claim: the conditional theorem printed here is EXACT finite
calculus on the deployed v563 window family -- the implication
"functional >= deficit => T_h <= 1 at (h, m)" is an identity-level
restatement, and the CONTENT is the extraction and typing of the
explicit kernel K_{h,m} and pair kernel C_{h,m}; the hypothesis
itself is measured (finite shadow), not proved, with no bound, no
rate, no uniformity in h.  No marker moves.

FIREWALL: no zeros, no prime oracles beyond the deployed table
(AST scan: zetazero/nzeros/primerange/isprime/primepi/nextprime/
prevprime banned); v563 READ-ONLY; RNG only in the scramble
control; stdout only.

Sources (read-only): v563_paper2_readouts (window geometry, tent
assembly, arch lags, deployed atom table); signed_homotopy_probe
(envelope identity, decompose, M4 Hessian machinery -- verbatim);
christoffel_pnt_gamma_probe (W2 closed-form PNT lags, folded
measures, Lanczos chain -- verbatim); christoffel_zone_envelope_
probe (theta* = 0.700); port_atom_numerator_probe / v882
(windowed-sum linearity), declared inputs.

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/paircorr_contract_probe.py
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
THETA_STAR = 0.700             # frozen zone exponent (ZONESPLIT.01)
PAIR_RUNGS = (9, 40)           # frozen P2 rungs (round-45 M4 rungs)
K_SUB = 12                     # P2 residual subspace dimension
FD_ETA = 0.05                  # P2 central-difference step
MASK_SAFE = 4.0                # P2 chamber-wall safety factor
EIG_TOL = 1.0e-3               # P2 eigen-signature tolerance
TOL_WARD_PRIME = 1.0e-10       # W1: prime-side form == grid form
TOL_WARD_K0 = 1.0e-12          # W2: K0 route a == route b
TOL_SELF_END = 1.0e-8          # S0.2 endpoint reconstruction
TOL_QF = 1.0e-8                # S0.3 quadratic-form self-test
FRAC_MASS = 0.90               # profile mass fraction (frozen)
SHORT_FRAC = 0.25              # typing: support width bar
BAND_N90 = 32                  # typing: mode count bar
NU_PAIR = 13                   # P2 pair-kernel u-grid size
SIGN_TOL = 1.0e-3              # P2 sign-map tolerance (of max |C|)
PROF_FRACS = (0.10, 0.30, 0.50, 0.70, 0.85, 0.95, 1.00)
SCRAMBLE_SEED = 1
CTRL_FALLBACK_AL = 8           # C: a-closest neg nodes fallback
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
# (grid density, folded measures, Lanczos chain, CD kernel, W2 closed-form
#  PNT lags: verbatim from signed_homotopy_probe / christoffel_pnt_gamma)

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


# --------------------------------------------------------- rung construction
def build_rung(kz):
    """Folded d_PNT, d_truth, residual, weights, zone aliases, the
    exact occupation times, and the lag blocks c0/c1 of one rung."""
    rr = core.build_window(kz)
    alpha, M, h, D = rr["alpha"], rr["M"], rr["h"], rr["D"]
    assert abs(D - 2.0 * alpha / M) <= 1e-12 * D
    uu = np.asarray(rr["uu"], float)
    mm = 2.0 * np.asarray(rr["lam"], float)
    c_ar = np.asarray(core.arch_lags(M, D), float)
    c1 = np.asarray(core.atom_lags_at(alpha, M, uu, mm)[0], float)
    c0 = np.asarray(cont_lags(alpha, M, [0.0], [2.0 * alpha],
                              [1.0]), float)
    L = 2 * M - 2
    F = L // 2 + 1
    d1 = grid_density(c_ar + c1)[:F]
    d0 = grid_density(c_ar + c0)[:F]
    d0at = grid_density(c0)[:F]
    r = d1 - d0
    ff = np.arange(F)
    x = np.cos(2.0 * math.pi * ff / L)
    a = 2.0 * h * h * (1.0 - x)
    mult = np.where((ff == 0) | (ff == L // 2), 1.0, 2.0)
    qt = mult * 4.0 * np.sin(math.pi * ff / L) ** 2 / (2.0 * L)
    al_f = ff[(ff >= 1) & (d1 < 0.0)
              & (a <= h ** (2.0 * THETA_STAR))]
    al_f = al_f[np.argsort(a[al_f], kind="stable")]
    up = (d0 < 0.0) & (d1 > 0.0) & (qt > 0.0)
    dn = (d0 > 0.0) & (d1 < 0.0) & (qt > 0.0)
    ts = np.full(F, np.nan)
    ts[up | dn] = -d0[up | dn] / r[up | dn]
    tau = np.where(d0 > 0.0, 1.0, 0.0)
    z0 = d0 == 0.0
    tau[z0] = np.where(d1[z0] > 0.0, 1.0, 0.0)
    tau[up] = 1.0 - ts[up]
    tau[dn] = ts[dn]
    return dict(kz=kz, alpha=alpha, M=M, h=h, L=L, F=F, D=D,
                c_ar=c_ar, c0=c0, c1=c1, uu=uu, mm=mm,
                x=x, a=a, qt=qt, d0=d0, d1=d1, d0at=d0at, r=r,
                al_f=al_f, y_al=x[al_f], tau=tau,
                X=math.exp(2.0 * alpha))


def gap_at(R, dv, al_f, qf=False):
    """Chain of the positive part of dv; per alias the Christoffel
    lambda, target mass nu, gap G (qt route, S0.2-pinned)."""
    pos = (dv > 0.0) & (R["qt"] > 0.0)
    xs = R["x"][pos]
    ws = (R["qt"] * dv)[pos]
    h = R["h"]
    al, be, m0, steps = lanczos_chain(xs, ws, h + 1)
    if steps < h + 1:
        return None
    Phi = eval_chain(al, be, m0, R["x"][al_f], h)   # n_al x h
    K = np.sum(Phi ** 2, axis=1)
    lam = 1.0 / K
    nu = R["qt"][al_f] * np.maximum(-dv[al_f], 0.0)
    out = dict(lam=lam, nu=nu, G=lam - nu, chain=(al, be, m0),
               Phi=Phi, Kdiag=K, pos=pos)
    if qf:
        Ppos = eval_chain(al, be, m0, xs, h)
        U = Ppos @ Phi.T
        out["qf_dev"] = float(np.max(np.abs(
            (ws @ (U * U)) / K - 1.0)))
    return out


# ----------------------------------------------------- P1: the prime kernel
def kernel_block(R, e0):
    """W, chat, K at the atoms, prime sum, smooth subtraction, and
    the two wards (all exact algebra; floats route-tested)."""
    al, be, m0 = e0["chain"]
    h, F, M, L = R["h"], R["F"], R["M"], R["L"]
    Pall = eval_chain(al, be, m0, R["x"], h)        # F x h
    U0 = Pall @ e0["Phi"].T                         # F x n_al
    P2 = (U0 * U0) / e0["Kdiag"] ** 2               # p_{0,m}(x_f)^2
    af = R["al_f"]
    W = (R["qt"] * (R["d0"] > 0.0))[:, None] * P2   # F x n_al
    W[af, np.arange(len(af))] += (R["qt"][af]
                                  * (R["d0"][af] < 0.0))
    A_grid = W.T @ R["r"]
    ii = np.arange(M)
    cosIF = np.cos((2.0 * math.pi / L)
                   * np.outer(ii, np.arange(F).astype(float)))
    w_i = np.where((ii == 0) | (ii == M - 1), 1.0, 2.0)
    chat = (cosIF @ W) * w_i[:, None]               # M x n_al
    del cosIF
    # K at the atoms: tent interpolation of -chat/2 (+ u<D mirror)
    uu, D = R["uu"], R["D"]
    i0 = np.floor(uu / D).astype(int)
    fr = uu / D - i0
    v0 = np.where((i0 >= 0) & (i0 <= M - 1), 1.0 - fr, 0.0)
    v1 = np.where((i0 + 1 >= 0) & (i0 + 1 <= M - 1), fr, 0.0)
    Kat = -0.5 * (v0[:, None] * chat[np.clip(i0, 0, M - 1)]
                  + v1[:, None] * chat[np.clip(i0 + 1, 0, M - 1)])
    mir = uu < D
    if np.any(mir):
        Kat[mir] += -0.5 * ((1.0 - uu[mir] / D)[:, None]
                            * chat[0][None, :])
    S1 = R["mm"] @ Kat
    K0a = W.T @ R["d0at"]
    K0b = R["c0"] @ chat
    A_prime = S1 - K0a
    Sabs = np.abs(R["mm"]) @ np.abs(Kat) + np.abs(K0a)
    ward1 = float(np.max(np.abs(A_prime - A_grid)
                         / np.maximum(np.maximum(np.abs(A_grid),
                                                 Sabs), 1e-300)))
    ward2 = float(np.max(np.abs(K0b - K0a)
                         / np.maximum(np.abs(R["c0"])
                                      @ np.abs(chat), 1e-300)))
    return dict(W=W, chat=chat, Kat=Kat, S1=S1, K0=K0a,
                A_grid=A_grid, A_prime=A_prime, Sabs=Sabs,
                ward1=ward1, ward2=ward2, P2=P2)


def min_window(mass, frac):
    """Smallest contiguous index window with >= frac of sum(mass)."""
    tot = float(np.sum(mass))
    target = frac * tot
    jl, csum, best = 0, 0.0, None
    for jr in range(len(mass)):
        csum += mass[jr]
        while csum - mass[jl] >= target:
            csum -= mass[jl]
            jl += 1
        if csum >= target and (best is None
                               or jr - jl < best[1] - best[0]):
            best = (jl, jr)
    return best


def profile(R, kb, m_idx):
    """P1 profile of K_{h,m} at one alias column m_idx."""
    M, D, F, L = R["M"], R["D"], R["F"], R["L"]
    Ki = -0.5 * kb["chat"][1:, m_idx]        # K(iD), i = 1..M-1
    ug = np.arange(1, M) * D
    jl, jr = min_window(np.abs(Ki), FRAC_MASS)
    width = (jr - jl + 1) * D
    u_frac = width / (2.0 * R["alpha"])
    aw = np.abs(kb["W"][1:, m_idx])
    o = np.argsort(-aw)
    cs = np.cumsum(aw[o])
    n90 = int(np.searchsorted(cs, FRAC_MASS * cs[-1]) + 1)
    tauv = 2.0 * math.pi * np.arange(1, F) / (L * D)
    tau_mean = float((aw @ tauv) / max(float(np.sum(aw)), 1e-300))
    f_m = int(R["al_f"][m_idx])
    tau_m = 2.0 * math.pi * f_m / (L * D)
    cw = np.cos(tau_m * ug)
    corr_fej = float((Ki @ cw) / max(
        float(np.linalg.norm(Ki) * np.linalg.norm(cw)), 1e-300))
    ind = ((ug >= ug[jl]) & (ug <= ug[jr])).astype(float)
    corr_short = float((Ki @ ind) / max(
        float(np.linalg.norm(Ki)
              * math.sqrt(max(float(np.sum(ind)), 1.0))), 1e-300))
    ipk = int(np.argmax(np.abs(Ki)))
    samp = []
    for frc in PROF_FRACS:
        i = min(M - 2, max(0, int(round(frc * (M - 2)))))
        samp.append(float(Ki[i]))
    return dict(Ki=Ki, ug=ug, u_lo=float(ug[jl]), u_hi=float(ug[jr]),
                width=float(width), u_frac=float(u_frac), n90=n90,
                tau_mean=tau_mean, tau_m=tau_m, corr_fej=corr_fej,
                corr_short=corr_short, u_pk=float(ug[ipk]),
                K_pk=float(Ki[ipk]), samp=samp, f_m=f_m)


def type_kernel(u_frac, n90):
    if u_frac <= SHORT_FRAC and n90 > BAND_N90:
        return "KERNEL-SHORTINTERVAL"
    if n90 <= BAND_N90 and u_frac > SHORT_FRAC:
        return "KERNEL-BANDLIMITED"
    return "KERNEL-MIXED"


# --------------------------------------------------- P2: the pair kernel
def g_of_u(R, f, ug):
    """The per-atom grid response g_f(u) on a u-grid (tent + mirror,
    exactly the deployed assembly's linearity)."""
    M, L, D = R["M"], R["L"], R["D"]
    th = 2.0 * math.pi * f / L
    i0 = np.floor(ug / D).astype(int)
    fr = ug / D - i0

    def w_of(i):
        return np.where((i == 0) | (i == M - 1), 1.0, 2.0)

    out = np.zeros(len(ug))
    for i_at, v in ((i0, 1.0 - fr), (i0 + 1, fr)):
        ok = (i_at >= 0) & (i_at <= M - 1) & (v > 0.0)
        out += np.where(ok, v * w_of(i_at) * np.cos(i_at * th),
                        0.0)
    m = ug < D
    out[m] += 1.0 - ug[m] / D
    return -0.5 * out


def pair_hessian(R, m_f):
    """FD Hessian of the gap at the PNT point in the K_SUB residual
    subspace at alias grid index m_f (round-45 M4, verbatim)."""
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
    diag2 = np.zeros(K)
    for i in range(K):
        for eta in (FD_ETA, 0.5 * FD_ETA):
            sp = np.zeros(K)
            sp[i] = eta
            fp, fm = phi(sp), phi(-sp)
            if fp is None or fm is None:
                return None
            if eta == FD_ETA:
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
    return dict(idx=idx, skipped=skipped, H=H, eig=eig,
                drift_med=float(np.median(drift)))


# ------------------------------------------------------------------ P3 text
CONTRACT_TEX = r"""
  %% ---- LaTeX-ready conditional contract (stdout deliverable) ----
  \noindent\textbf{Conditional contract
  (PRIME.CASE.PAIRCORR.CONTRACT.01).}
  Fix a rung of the deployed ladder: window length $\alpha$, lag
  grid $M$, $D = 2\alpha/M$, $L = 2M-2$, degree $h = M/2$, cutoff
  $X = e^{2\alpha}$; nodes $x_f = \cos(2\pi f/L)$ and folded
  weights $\tilde q_f = m_f\,4\sin^2(\pi f/L)/(2L)$ ($m_f$ the
  fold multiplicity), $f = 0,\dots,L/2$.  Let $c^{\mathrm{ar}}$ be
  the archimedean lags, $c^{1}$ the deployed tent lags of the von
  Mangoldt comb $\{(\log n,\,2\Lambda(n)/\sqrt n)\}_{n\le X}$,
  $c^{0}$ the closed-form tent lags of the PNT density
  $2e^{u/2}\,du$ on $[0,2\alpha]$, and
  $d^{\,t} = \mathcal F[c^{\mathrm{ar}}+c^{0}+t(c^{1}-c^{0})]$ the
  grid densities, $r = d^{\,1}-d^{\,0}$.  For an alias node $y_m$
  ($d^{\,1}_m<0$) let $\lambda_{t,m}$ be the Christoffel minimum
  of $\int|p|^2\,d\mu_t$ over $\deg p<h$, $p(y_m)=1$,
  $\mu_t=\sum_f \tilde q_f\,[d^{\,t}_f]_+\,\delta_{x_f}$, let
  $\nu_{t,m}=\tilde q_m\,[-d^{\,t}_m]_+$, and let $p_{0,m}$ be the
  $t=0$ minimizer.  Define the node weight
  $W_{f,m}=\tilde q_f\,\mathbf 1\{d^{\,0}_f>0\}\,p_{0,m}(x_f)^2
  +\tilde q_m\,\mathbf 1\{d^{\,0}_m<0\}\,\delta_{fm}$
  and the \emph{prime kernel}
  \[
    K_{h,m}(u) \;=\; -\tfrac12\sum_{i=0}^{M-1}
    \mathrm{tent}_i(u)\,w_i\sum_{f} W_{f,m}\cos(2\pi i f/L),
  \]
  with $\mathrm{tent}_i(u)=(1-|iD-u|/D)_+$ plus the $u<D$ mirror
  of the deployed assembly and $w_i\in\{1,2\}$ the symmetric-
  extension cosine weights.  Then the first-order (fixed-mask)
  gain is \emph{exactly} the smoothed one-sided prime sum
  \[
    J^{(1)}_{h,m} \;=\; \sum_{n\le X}\frac{2\Lambda(n)}{\sqrt n}
    \,K_{h,m}(\log n)\;-\;\int_0^{2\alpha}2e^{u/2}K_{h,m}(u)\,du,
  \]
  and with the response remainder
  $R_{h,m} := \bigl[(\lambda_{1,m}-\nu_{1,m})
  -(\lambda_{0,m}-\nu_{0,m})\bigr]-J^{(1)}_{h,m}$, whose leading
  (quadratic) term is the pair form
  $\tfrac12\sum_{n,n'\le X}\delta\mu_n\,\delta\mu_{n'}
  \,C_{h,m}(\log n,\log n')$ with the measured response kernel
  $C_{h,m}$ (this probe, P2), the following holds by exact finite
  calculus on the deployed family:
  \medskip

  \noindent\textbf{IF} for every rung $h \ge H_0$ of the deployed
  ladder and every critical alias $m$ with
  $a_m = 2h^2(1-y_m) \le h^{1.4}$
  \[
    J^{(1)}_{h,m} \;+\; R_{h,m} \;\;\ge\;\;
    \nu_{0,m}-\lambda_{0,m}
    \qquad\text{(the PNT-reference deficit, computable from
    $d^{\,0}$ alone),}
  \]
  \textbf{THEN} $\lambda_{1,m}\ge\nu_{1,m}$ for all such $(h,m)$,
  i.e.\ the port testing ratio satisfies $T_h \le 1$ on the
  critical zone of the ladder.
  %% ---- end contract block ----"""


def main():
    section("PRIME.CASE.PAIRCORR.CONTRACT.01 -- the explicit "
            "prime-pair correlation contract (EXPLORATION ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s"
          % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
    print("    NO RH claim; no marker moves.")

    print("\nS0 -- firewall + self-tests")
    check("S0.1 AST firewall clean", not ast_scan(BANNED_IDS),
          kill="PIPELINE")

    section("B0 -- rungs (geometry + zone aliases)")
    RG = {}
    for kz in HEAVY:
        R = build_rung(kz)
        RG[kz] = R
        print("    kz %-3d h %4d M %4d F %5d: atoms %5d, X %.3e, "
              "zone aliases %3d (a <= h^1.4 = %8.0f)"
              % (kz, R["h"], R["M"], R["F"], len(R["uu"]),
                 R["X"], len(R["al_f"]), R["h"] ** 1.4),
              flush=True)
    order = sorted(HEAVY, key=lambda kz: RG[kz]["h"])
    ok_al = all(len(RG[kz]["al_f"]) > 0 for kz in HEAVY)
    check("B0.1 zone alias sets nonempty on every rung", ok_al,
          kill="PIPELINE")
    if not ok_al:
        return finish(None, None)

    # S0.2 endpoint reconstruction vs verbatim folded route (kz 9)
    R9 = RG[9]
    dev_end = 0.0
    for tv in (0.0, 1.0):
        dv = R9["d0"] if tv == 0.0 else R9["d1"]
        d_full = np.concatenate([dv, dv[-2:0:-1]])
        xs, ws, _uf = folded_measure(d_full, R9["L"], +1.0)
        ys, vs, uf_n = folded_measure(d_full, R9["L"], -1.0)
        al, be, m0, steps = lanczos_chain(xs, ws, R9["h"] + 1)
        if steps < R9["h"] + 1:
            check("S0.2 endpoint chain (verbatim route)", False,
                  kill="PIPELINE")
            return finish(None, None)
        Pn = eval_chain(al, be, m0, R9["y_al"], R9["h"])
        lam_ref = 1.0 / np.sum(Pn ** 2, axis=1)
        pos_map = {int(f): float(v) for f, v in zip(uf_n, vs)}
        nu_ref = np.array([pos_map.get(int(f), 0.0)
                           for f in R9["al_f"]])
        e = gap_at(R9, dv, R9["al_f"])
        if e is None:
            check("S0.2 endpoint chain (qt route)", False,
                  kill="PIPELINE")
            return finish(None, None)
        dev_end = max(dev_end, float(np.max(
            np.abs(e["lam"] / lam_ref - 1.0))))
        dev_end = max(dev_end, float(np.max(
            np.abs(e["nu"] - nu_ref)
            / np.maximum(np.abs(nu_ref), 1e-300))))
    check("S0.2 endpoint reconstruction == verbatim folded route "
          "(kz 9, t = 0 and 1)", dev_end <= TOL_SELF_END,
          "rel sup dev %.2e" % dev_end, kill="PIPELINE")

    section("E -- exact endpoints per rung: G_m(t) = lambda - nu, "
            "gain Delta_m, deficit (nu_0 - lambda_0)_m")
    RES = {}
    ok_e = True
    qf_worst = 0.0
    for kz in order:
        R = RG[kz]
        e0 = gap_at(R, R["d0"], R["al_f"], qf=True)
        e1 = gap_at(R, R["d1"], R["al_f"], qf=True)
        if e0 is None or e1 is None:
            ok_e = False
            print("    kz %-3d: CHAIN SHORT at an endpoint" % kz)
            break
        qf_worst = max(qf_worst, e0["qf_dev"], e1["qf_dev"])
        delta = e1["G"] - e0["G"]
        ms = int(np.argmin(e1["G"]))
        RES[kz] = dict(e0=e0, e1=e1, delta=delta, ms=ms)
        print("    kz %-3d h %4d (n_al %2d): deficit max %+.3e | "
              "Delta min %+.3e | margin min %+.3e | m* %d "
              "(f %d, a %.1f)"
              % (kz, R["h"], len(R["al_f"]),
                 float(np.max(-e0["G"])), float(np.min(delta)),
                 float(np.min(e1["G"])), ms + 1,
                 int(R["al_f"][ms]), float(R["a"][R["al_f"][ms]])),
              flush=True)
    check("E0 endpoint chains complete on all rungs", ok_e,
          kill="PIPELINE")
    check("S0.3 quadratic-form self-test (sum w p*^2 == lambda, "
          "both endpoints, all rungs)", ok_e
          and qf_worst <= TOL_QF, "worst rel dev %.2e" % qf_worst,
          kill="PIPELINE")
    if not ok_e:
        return finish(None, None)

    section("P1 -- THE FUNCTIONAL: J1 = sum_n mu_n K_{h,m}(log n) "
            "- K0 (regrouped prime-side form + wards)")
    w1_max = w2_max = 0.0
    types = []
    for kz in order:
        R = RG[kz]
        t_a = time.time()
        kb = kernel_block(R, RES[kz]["e0"])
        RES[kz]["kb"] = kb
        w1_max = max(w1_max, kb["ward1"])
        w2_max = max(w2_max, kb["ward2"])
        ms = RES[kz]["ms"]
        print("    kz %-3d h %4d: ward1(prime==grid) %.2e  "
              "ward2(K0 a==b) %.2e  [%.1f s]"
              % (kz, R["h"], kb["ward1"], kb["ward2"],
                 time.time() - t_a), flush=True)
        for tag, mi in (("m*", ms), ("m1", 0)):
            if tag == "m1" and ms == 0:
                continue
            pr = profile(R, kb, mi)
            lab = type_kernel(pr["u_frac"], pr["n90"])
            if tag == "m*":
                types.append(lab)
                RES[kz]["prof"] = pr
                RES[kz]["ktype"] = lab
            print("      K profile %s (alias %2d, f %4d, a %7.1f):"
                  " J1 %+.3e" % (tag, mi + 1, pr["f_m"],
                                 float(R["a"][R["al_f"][mi]]),
                                 float(kb["A_prime"][mi])))
            print("        K(u) at u/2a %s: %s"
                  % ("/".join("%.2f" % f for f in PROF_FRACS),
                     " ".join("%+.1e" % v for v in pr["samp"])))
            print("        peak |K| %.2e at u %.2f (2a = %.2f) | "
                  "90%% support [%.2f, %.2f] width %.2f "
                  "(frac %.3f) | n90 modes %d | mean tau %.2f "
                  "(alias tau %.2f)"
                  % (abs(pr["K_pk"]), pr["u_pk"],
                     2.0 * R["alpha"], pr["u_lo"], pr["u_hi"],
                     pr["width"], pr["u_frac"], pr["n90"],
                     pr["tau_mean"], pr["tau_m"]))
            print("        shape corr: cos(tau_m u) %+.3f | "
                  "window indicator %+.3f -> %s"
                  % (pr["corr_fej"], pr["corr_short"], lab),
                  flush=True)
    check("P1.W1 prime-side form == grid form (max rel %.2e <= "
          "%.0e)" % (w1_max, TOL_WARD_PRIME),
          w1_max <= TOL_WARD_PRIME, kill="WARD")
    check("P1.W2 smooth subtraction route a == route b (max rel "
          "%.2e <= %.0e)" % (w2_max, TOL_WARD_K0),
          w2_max <= TOL_WARD_K0, kill="WARD")

    section("P2 -- THE PAIR PART: effective prime pair kernel "
            "C_{h,m*}(u, u') on the K_SUB = %d port-mode subspace"
            % K_SUB)
    for kz in PAIR_RUNGS:
        R = RG[kz]
        t_a = time.time()
        ms = RES[kz]["ms"]
        m_f = int(R["al_f"][ms])
        out = pair_hessian(R, m_f)
        if out is None:
            check("P2 chains complete (kz %d)" % kz, False,
                  kill="PIPELINE")
            return finish(None, None)
        H, idx, eig = out["H"], out["idx"], out["eig"]
        emx = float(np.max(np.abs(eig)))
        n_pos = int(np.sum(eig > EIG_TOL * emx))
        n_neg = int(np.sum(eig < -EIG_TOL * emx))
        Hg = H / np.outer(R["r"][idx], R["r"][idx])
        ugp = np.linspace(0.0, 2.0 * R["alpha"], NU_PAIR)
        Gp = np.column_stack([g_of_u(R, int(f), ugp)
                              for f in idx])
        Cp = Gp @ Hg @ Gp.T
        tau_i = 2.0 * math.pi * idx / (R["L"] * R["D"])
        # exact crossing part B at m* (closed form, round-45 M3)
        P2c = RES[kz]["kb"]["P2"][:, ms]
        qr = R["qt"] * R["r"]
        A_ms = float(RES[kz]["kb"]["A_grid"][ms])
        FP = float((qr * R["tau"]) @ P2c
                   + qr[m_f] * (1.0 - R["tau"][m_f]))
        B_ms = FP - A_ms
        C_ms = float(RES[kz]["delta"][ms]) - FP
        quad = 0.5 * float(np.ones(len(idx)) @ H @ np.ones(len(idx)))
        mx = float(np.max(np.abs(Cp)))
        frac_pos = float(np.mean(Cp > SIGN_TOL * mx))
        frac_neg = float(np.mean(Cp < -SIGN_TOL * mx))
        print("    kz %-3d (m* %d, f %d; subspace f = %s; %d "
              "skipped mask-unsafe; FD eta/2 med drift %.3f):"
              % (kz, ms + 1, m_f,
                 [int(f) for f in idx], out["skipped"],
                 out["drift_med"]))
        print("      H spectrum: %s" % " ".join("%+.2e" % v
                                                for v in eig))
        print("      signature (tol %.0e rel): %d pos / %d neg "
              "of %d -> %s" % (EIG_TOL, n_pos, n_neg, len(eig),
                               "INDEFINITE" if n_pos and n_neg
                               else ("NSD" if n_neg else "PSD")))
        print("      subspace frequencies tau_i: %s"
              % " ".join("%.2f" % t for t in tau_i))
        print("      pair kernel C on the %d x %d u-grid: "
              "max |C| %.2e, sign census +%.0f%% / -%.0f%% "
              "(|.| > %.0e max)"
              % (NU_PAIR, NU_PAIR, mx, 100 * frac_pos,
                 100 * frac_neg, SIGN_TOL))
        print("      sign map (rows/cols u = 0 .. 2 alpha):")
        for row in Cp:
            print("        " + "".join(
                "+" if v > SIGN_TOL * mx else
                "-" if v < -SIGN_TOL * mx else "." for v in row))
        dg = np.diag(Cp)
        print("      diagonal C(u,u): %s"
              % " ".join("%+.1e" % v for v in dg[::2]))
        print("      truth-direction quadratic (1/2) 1.H.1 %+.3e "
              "vs measured response C_m* %+.3e (Delta %+.3e = A "
              "%+.3e + B %+.3e + C %+.3e)  [%.1f s]"
              % (quad, C_ms, float(RES[kz]["delta"][ms]), A_ms,
                 B_ms, C_ms, time.time() - t_a), flush=True)
    check("P2.1 pair kernel extracted on the frozen rungs "
          "(measurement)", True)

    section("P3 -- THE CONTRACT STATEMENT (LaTeX-ready) + honest "
            "classification")
    H0 = min(RG[kz]["h"] for kz in HEAVY)
    print(CONTRACT_TEX)
    print("\n  Deployed instantiation: H_0 = %d (the shallowest "
          "deployed rung), theta* = %.3f (zone a <= h^{1.4}), "
          "ladder = the frame-A zones of v563." % (H0, THETA_STAR))
    from collections import Counter
    cnt = Counter(types)
    top, ntop = cnt.most_common(1)[0]
    ktype = top if ntop > len(types) // 2 else "KERNEL-MIXED"
    print("\n  HONEST CLASSIFICATION of the hypothesis:")
    print("    kernel typing at m* per rung: %s -> majority %s"
          % (", ".join("kz%d:%s" % (kz, RES[kz]["ktype"])
                       for kz in order), ktype))
    print("    the functional is a smoothed ONE-SIDED weighted "
          "sum of Lambda(n) - PNT-share at scale X = e^{2 alpha}"
          " (X = %.1e .. %.1e on the heavy rungs);"
          % (min(RG[kz]["X"] for kz in HEAVY),
             max(RG[kz]["X"] for kz in HEAVY)))
    mark = ("(i) MEASURED BRANCH" if ktype == "KERNEL-SHORTINTERVAL"
            else "(i)")
    print("    %s short-interval reading: weight concentrated on "
          "a u-window of width %s log-units -> a one-sided "
          "short-interval prime bound; the known unconditional "
          "landscape (psi asymptotics for widths >= x^{0.525}; "
          "zero-free-region error exp(-c (log x)^{3/5})) is "
          "NAMED, not proved, and not applicable at our tiny X."
          % (mark, "/".join("%.2f" % RES[kz]["prof"]["width"]
                            for kz in order)))
    mark = ("(ii) MEASURED BRANCH" if ktype == "KERNEL-BANDLIMITED"
            else "(ii)")
    print("    %s Fejer/band-limited reading: n90 = %s modes, "
          "mean tau = %s -> a band-limited one-sided explicit-"
          "formula positivity at the port frequencies: the "
          "PAIR-CORRELATION class (consistent with the round-45 "
          "HOMOTOPY-INDEFINITE-ARITHMETIC typing)."
          % (mark, "/".join("%d" % RES[kz]["prof"]["n90"]
                            for kz in order),
             "/".join("%.2f" % RES[kz]["prof"]["tau_mean"]
                      for kz in order)))
    print("    demanded relative cancellation eps_need = "
          "deficit / (sum_n mu_n |K| + |K0|) at m*:")
    for kz in order:
        ms = RES[kz]["ms"]
        dfc = float(-RES[kz]["e0"]["G"][ms])
        eps = dfc / max(float(RES[kz]["kb"]["Sabs"][ms]), 1e-300)
        print("      kz %-3d h %4d: deficit %+.3e  scale %.3e  "
              "eps_need %+.3e"
              % (kz, RG[kz]["h"], dfc,
                 float(RES[kz]["kb"]["Sabs"][ms]), eps))
    check("P3.1 contract printed; kernel typed %s" % ktype, True)

    section("P4 -- THE MARGIN LEDGER (finite shadow): LHS(truth) "
            "vs deficit, margin = (lambda_1 - nu_1)_m")
    n_bad = 0
    n_all = 0
    for kz in order:
        R = RG[kz]
        e0, e1 = RES[kz]["e0"], RES[kz]["e1"]
        A = RES[kz]["kb"]["A_prime"]
        delta = RES[kz]["delta"]
        deficit = -e0["G"]
        margin = e1["G"]
        n_all += len(margin)
        n_bad += int(np.sum(margin <= 0.0))
        print("    kz %-3d h %4d (n_al %d):" % (kz, R["h"],
                                                len(margin)))
        print("      %-4s %-5s %-9s %-11s %-11s %-11s %-11s"
              % ("m", "f", "a_m", "J1(A_m)", "LHS=Delta",
                 "deficit", "margin"))
        show = list(range(min(8, len(margin))))
        im = int(np.argmin(margin))
        if im not in show:
            show.append(im)
        for i in show:
            print("      %-4d %-5d %-9.1f %+.3e  %+.3e  %+.3e  "
                  "%+.3e%s"
                  % (i + 1, int(R["al_f"][i]),
                     float(R["a"][R["al_f"][i]]), float(A[i]),
                     float(delta[i]), float(deficit[i]),
                     float(margin[i]),
                     "  <- min margin" if i == im else ""))
        print("      min margin %+.3e | margins > 0: %d/%d"
              % (float(np.min(margin)),
                 int(np.sum(margin > 0.0)), len(margin)),
              flush=True)
    ledger = ("CONSISTENT" if n_bad == 0
              else "INCONSISTENT %d/%d" % (n_bad, n_all))
    print("    ledger: %s (all margins positive = the finite "
          "shadow of the contract holds on the deployed rungs)"
          % ledger)
    check("P4.1 margin ledger recorded: %s (measurement)"
          % ledger, True)

    section("C -- controls (kz 9, scramble seed %d)"
            % SCRAMBLE_SEED)
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
    fell_back = len(al_zone) == 0
    al_use = al_zone if not fell_back else neg_s[:CTRL_FALLBACK_AL]
    es = gap_at(R9, d_s, al_use)
    e0s = gap_at(R9, R9["d0"], al_use)
    if es is None or e0s is None:
        check("C0 scramble chains complete", False,
              kill="PIPELINE")
        return finish(ktype, ledger)
    lhs_s = es["G"] - e0s["G"]
    dfc_s = -e0s["G"]
    worst = float(np.min(lhs_s - dfc_s))       # == min (lam - nu)_s
    fires = worst <= 0.0
    print("    scramble aliases: %d%s | min (LHS_scr - deficit) "
          "= min (lambda - nu)_scr = %+.3e (real kz 9 min margin "
          "%+.3e) -> %s"
          % (len(al_use),
             " (zone empty -> frozen fallback: %d a-closest neg "
             "nodes)" % CTRL_FALLBACK_AL if fell_back else
             " (zone aliases)",
             worst, float(np.min(RES[9]["e1"]["G"])),
             "FIRES" if fires else "SILENT"), flush=True)
    check("C1 value control fires (scrambled comb: LHS falls "
          "below the deficit)", fires, kill="CONTROL")

    return finish(ktype, ledger)


def finish(ktype, ledger):
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
        VERDICT = "PAIRCONTRACT-EXTRACTED"
    sub = []
    if ktype:
        sub.append("KERNEL=%s" % ktype)
    if ledger:
        sub.append("LEDGER=%s" % ledger)
    print("\n  VERDICT: %s%s"
          % (VERDICT, (" (%s)" % "; ".join(sub)) if sub else ""))
    if VERDICT == "PAIRCONTRACT-EXTRACTED":
        print("  PLAIN ANSWER: the conditional reduction is now "
              "concrete -- T_h <= 1 on the critical zone follows "
              "from the printed one-sided prime-sum inequality "
              "with the explicit kernel K_{h,m} (typed %s) plus "
              "the pair remainder; the contract can be "
              "registered as PRIME.CASE.PAIRCORR.CONTRACT.01."
              % (ktype or "n/a"))
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed"
          % (time.time() - T0, n_tot, n_tot - n_pass))
    return 0 if n_pass == n_tot else 1


if __name__ == "__main__":
    raise SystemExit(main())
'''

# ------------- frozen probe source endpoint_bracket_probe (embedded BYTE-EXACT, raw string)
_SRC_1 = r'''
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""endpoint_bracket_probe -- PRIME.CASE.ENDPOINT.01
(EXPLORATION ONLY, experiments/; round 51, reviewer priority 6: the
concavity bracket of the diagonal-half homotopy -- does the ONE-SIDED
ENDPOINT DERIVATIVE F'(1) already clear the PNT-reference deficit,
collapsing the pair-correlation contract to a LINEAR signed-Lambda
functional evaluated AT THE TRUTH?  2026-08-09.)

CONTEXT (machinery verbatim from signed_homotopy_probe /
paircorr_contract_probe): with F_m(t) = lambda_{t,m} - nu_{t,m}
along d_t = d_PNT + t (d_truth - d_PNT), the exact envelope identity
gives F'_m(t) = J_{h,m}(t) = sum_f qt_f r_f 1{d_t(f) > 0}
p_{t,m}(x_f)^2 + qt_m r_m 1{d_t(m) < 0} a.e. t; within a fixed mask
chamber lambda_t is CONCAVE in t (a minimum of linear functionals of
mu_t) and the nu side is linear, so F is concave per chamber and
J decreases within each chamber; at a mask crossing J JUMPS (an
entering node has r > 0, a leaving node removes an r < 0 term, an
alias-side nu switch flips the linear term), so the GLOBAL bracket
    F'(1^-)  <=  F(1) - F(0)  <=  F'(0^+)
holds exactly on crossing-free rungs and only up to the (measured)
crossing corrections otherwise.  paircorr_contract_probe froze the
contract: the gain must beat the PNT-reference deficit,
F(1) - F(0) >= deficit_m := (nu_0 - lambda_0)_m, and regrouped the
t = 0 derivative F'(0) = J^(1)_{h,m} into the explicit one-sided
prime sum sum_n mu_n K^(0)_{h,m}(log n) - K0.  THE REVIEWER'S POINT
(this probe): IF F'(1) >= deficit_m already, then by the concavity
bracket F(1) - F(0) >= F'(1) >= deficit -- a ONE-SIDED LOWER BOUND
on the ENDPOINT derivative, a LINEAR signed-Lambda functional
evaluated AT THE TRUTH, suffices, which is much weaker than the
pair-correlation input.  If only F'(0) > deficit but F'(1) <
deficit, the genuine pair-correlation input stands.

THE CIRCULARITY NOTE (frozen up front, honest): F'(1) is linear in
the von Mangoldt masses ONLY AT FIXED KERNEL -- the truth-side
kernel K^(1)_{h,m} carries the truth mask 1{d_1(f) > 0} and the
truth extremizer p_{1,m}, both functionals of the comb itself.  A
theorem from a positive census here would additionally need either
(a) a STABILITY LEMMA p_{1,m} ~ p_{0,m} (and mask stability)
transferring the bound to the PNT-computable K^(0) -- E3 measures
exactly that kernel distance -- or (b) a self-consistent bound: the
one-sided inequality holds for every admissible density in a
neighbourhood class containing d_1.  Stated, not assumed.

FROZEN PROTOCOL (2026-08-09; constants frozen before the first
measurement run; budget < 20 min):

 RUNGS: heavy kz {9, 12, 13, 26, 40} + the deepest 3 with complete
   atom tables kz {88, 90, 116} (verbatim eligibility and selection
   from christoffel_pnt_gamma_probe / signed_homotopy_probe;
   X <= 4e5).
 ALIASES: all port aliases in the frozen critical zone -- truth neg
   nodes (d_1(f) < 0, f >= 1) with a_{h,f} = 2 h^2 (1 - x_f) <=
   h^{2 theta*}, theta* = 0.700, ranked by a ascending (verbatim).

 E1 THE THREE NUMBERS (every rung, every zone alias):
   F'(0) = J at t = 0 (PNT-side extremal polynomial p_{0,m} + PNT
   masks), F'(1) = J at t = 1 (TRUTH-side extremal polynomial
   p_{1,m} + truth masks -- exact, same envelope formula), and the
   exact endpoint difference Delta_m = F(1) - F(0).  WARDS (kill
   WARD-BROKEN on failure):
     (W-A) prime-side regrouping == grid form at BOTH endpoints:
           F'(0) vs paircorr_contract's J^(1) = S1 - K0 built from
           W^(0), and F'(1) vs the same regrouping built from the
           truth-side W^(1) (masks d_1, weights p_{1,m}^2); rel
           <= 1e-10 per alias against max(|W.r|, sum_n mu_n |K| +
           |K0|) (verbatim W1 denominator);
     (W-B) smooth-subtraction route a (W.d0at) == route b (c0.chat)
           at both endpoints, rel <= 1e-12 (verbatim W2);
     (W-C) endpoint FD ward: second-order one-sided Richardson
           differences inside the first/last crossing-free chamber,
           F'(0) ~ (-3F(0) + 4F(e) - F(2e))/(2e) and F'(1) ~
           (3F(1) - 4F(1-e) + F(1-2e))/(2e), chamber-safe step
           e = min(1e-4, t_first/4, (1 - t_last)/4) per rung (if
           e < 1e-6 the ward is SKIPPED and disclosed); PASS per
           alias iff |FD - F'| <= max(1e-3 |F'|, 1e-9 lambda_end /
           e) -- the relative bar with the additive FD noise
           allowance 1e-9 lambda / e (the lambda evaluation noise
           floor at h ~ 1400, the round-44 v2 lesson; the additive
           form is the v2 amendment below).
   THE BRACKET DEFECT (MEASUREMENT, never a kill -- crossings can
   honestly break the global bracket): per alias the relative
   defects max(0, Delta - F'(0))/s and max(0, F'(1) - Delta)/s,
   s = max(|F'(0)|, |F'(1)|, |Delta|); per rung the max defect, the
   count of aliases with defect > 1e-9, the mask-crossing count in
   (0,1) and the count of alias-side nu crossings (d_0(m) > 0).
   BRACKET-CLEAN flag iff max rel defect <= 1e-9 over all cells.

 E2 THE DECISIVE CENSUS (the deliverable): per (rung, alias) cell:
   PASS iff F'(1) >= deficit_m = (nu_0 - lambda_0)_m = -F_m(0).
   Margin ladder printed per rung (margin = F'(1) - deficit; first
   6 aliases + the argmin row; min/median/pass count).  TYPED:
     ENDPOINT-SUFFICES      iff PASS on ALL critical cells;
     ENDPOINT-PARTIAL       iff PASS on some but not all (failing
                            cells listed);
     ENDPOINT-INSUFFICIENT  iff PASS nowhere (the pair route
                            stands).
   The F'(0) census (F'(0) >= deficit) is printed alongside for the
   reviewer's contrast reading (measurement only).

 E3 THE LINEAR FUNCTIONAL (printed iff E2 passes anywhere; the
   truth-side regrouping itself is always computed for W-A):
   F'(1) = sum_n mu_n K^(1)_{h,m}(log n) - K0^(1) with
   K^(1)_{h,m}(u) = -(1/2) sum_i tent_i(u) w_i sum_f W^(1)_{f,m}
   cos(2 pi i f / L), W^(1)_{f,m} = qt_f 1{d_1(f) > 0}
   p_{1,m}(x_f)^2 + qt_m 1{d_1(m) < 0} delta_{fm} (the same
   regrouping as paircorr_contract P1 with truth-side weights).
   KERNEL COMPARISON per rung at m* = argmin_m F_m(1) and at the
   a-closest alias: cosine corr(K^(0), K^(1)) on the lag grid
   i = 1..M-1, rel L2 distance ||K^(1) - K^(0)|| / ||K^(0)||, both
   peak locations, and the J-value pair.  The circularity statement
   (header) reprinted with the measured kernel distance filled in.

 E4 THE BRACKET LADDER (report): per rung (h ascending) the medians
   over aliases of F'(0), F'(1), Delta, the concavity drop
   gap = F'(0) - F'(1) and gap/|Delta|; the h-trend: log-log slope
   of the median gap vs h (shrinking iff slope < 0).

 C  CONTROLS (kz 9, scramble seed 1, the deployed mirror: positions
   uniform on (0, 2 alpha), same masses): the scramble endpoint
   derivative must go negative -- min over the scramble zone
   aliases (fallback, disclosed if empty: the 8 a-closest scramble
   neg nodes) of F'_scr(1) (residual r_s = d_scr - d_0, truth-side
   formula at d_scr) must be <= 0.  Silent -> CONTROL-DEAD.

 SELF-TESTS (S0, kill PIPELINE on failure): (i) AST firewall clean;
   (ii) endpoint reconstruction (kz 9): the qt-route lambda/nu at
   the zone aliases vs the verbatim folded_measure route, rel
   <= 1e-8, at both t = 0 and t = 1; (iii) quadratic-form self-test
   per rung at both endpoints: sum_j w_j p*^2 == lambda to rel 1e-8
   (verbatim TOL_QF).

KILLS: chain short anywhere needed / self-test failure / zone alias
set empty on a rung -> PIPELINE-BROKEN; W-A / W-B / W-C ward
failure -> WARD-BROKEN; value control silent -> CONTROL-DEAD.
E1 bracket defect, E2 census, E3, E4 are MEASUREMENTS, never kills.

VERDICT (frozen enum): ENDPOINT-MEASURED (+ TYPE=<ENDPOINT-SUFFICES
| ENDPOINT-PARTIAL | ENDPOINT-INSUFFICIENT> + BRACKET=<CLEAN |
CROSSING-CORRECTED max defect>) / PIPELINE-BROKEN / WARD-BROKEN /
CONTROL-DEAD.

SPEC AMENDMENTS (fail-first preserved):
  v1 (2026-08-09): initial freeze.  The alias bookkeeping, chain,
  regrouping algebra and scramble mirror are verbatim round-45/50
  machinery; the census rule (all / some / none) and the
  bracket-defect bar 1e-9 were frozen before any number was
  computed.  The v1 W-C pass rule was rel <= 1e-3 against the
  denominator max(|F'|, 1e-9 lambda / e).
  v2 (2026-08-09, after the first full run; fail-first preserved):
  the first run returned WARD-BROKEN on exactly one cell -- W-C at
  kz 88, t = 1, alias 1 measured rel 1.16e-3 vs the 1e-3 bar, with
  |F'(1)| = 9.2e-11 at that alias; every other ward passed (W-A
  <= 9.8e-15, W-B <= 1.1e-14, all other W-C <= 2.2e-4).  Diagnosis
  (run before amending, disclosed): the eps-scan 1e-4 / 5e-5 /
  2.5e-5 gives abs defect 1.06e-13 / 1.65e-13 / 4.09e-13 -- the
  defect GROWS as e shrinks (abs defect x e ~ 1e-17 constant), the
  signature of the lambda evaluation NOISE floor, not of stencil
  truncation (a Richardson-extrapolated stencil makes it worse,
  2.0e-3, as extrapolation amplifies noise); across all deep
  rungs/endpoints the measured abs defect is 0.02..0.13 of the
  modeled floor 1e-9 lambda / e.  The v1 rule put the floor INSIDE
  a max() denominator, so whenever floor < |F'| < 1000 floor it
  still demanded certifying the FD below its own noise -- exactly
  the failing cell.  v2 makes the allowance ADDITIVE: PASS iff
  |FD - F'| <= max(1e-3 |F'|, 1e-9 lambda / e) per alias (the
  measured worst cell sits at 0.02 of the allowance).  The bar
  1e-3, the step rule, the stencil and every other ward are
  untouched; every E1/E2/E3/E4/C number of the first run is
  unchanged by this amendment (the ward is a pass/fail gate only).

NO RH claim: every number is finite exact linear algebra /
calculus on the deployed v563 window family; a positive census is
a MEASURED finite shadow of a would-be linear reduction, not a
bound, no rate, no uniformity in h, and carries the circularity
caveat verbatim.  No marker moves.

FIREWALL: no zeros, no prime oracles beyond the deployed table
(AST scan: zetazero/nzeros/primerange/isprime/primepi/nextprime/
prevprime banned); v563 READ-ONLY; RNG only in the scramble
control; stdout only.

Sources (read-only): v563_paper2_readouts (window geometry, tent
assembly, arch lags, deployed atom table); signed_homotopy_probe
(envelope identity, eval machinery, crossing bookkeeping --
verbatim); paircorr_contract_probe (kernel regrouping W/chat/K,
wards W1/W2, deficit ledger -- verbatim); christoffel_pnt_gamma_
probe (W2 closed-form PNT lags, folded measures, Lanczos chain);
christoffel_zone_envelope_probe (theta* = 0.700), declared inputs.

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/endpoint_bracket_probe.py
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
TOL_WARD_PRIME = 1.0e-10       # W-A: prime-side form == grid form
TOL_WARD_K0 = 1.0e-12          # W-B: K0 route a == route b
TOL_FD_WARD = 1.0e-3           # W-C: endpoint FD relative bar
EPS_FD = 1.0e-4                # W-C: reference FD step
EPS_FD_MIN = 1.0e-6            # W-C: below this, skip + disclose
NOISE_REL = 1.0e-9             # W-C: lambda evaluation noise floor
TOL_SELF_END = 1.0e-8          # S0.2 endpoint reconstruction
TOL_QF = 1.0e-8                # S0.3 quadratic-form self-test
BRACKET_CLEAN = 1.0e-9         # E1: rel defect bar for CLEAN flag
SHOW_ROWS = 6                  # E2: ladder rows shown per rung
SCRAMBLE_SEED = 1
CTRL_FALLBACK_AL = 8           # C: a-closest neg nodes fallback
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
# (grid density, folded measures, Lanczos chain, CD kernel, W2 closed-form
#  PNT lags: verbatim from signed_homotopy_probe / paircorr_contract_probe)

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


# --------------------------------------------------------- rung construction
def build_rung(kz):
    """Folded d_PNT, d_truth, residual, weights, zone aliases and the
    exact crossing bookkeeping of one rung (verbatim round-45/50)."""
    rr = core.build_window(kz)
    alpha, M, h, D = rr["alpha"], rr["M"], rr["h"], rr["D"]
    assert abs(D - 2.0 * alpha / M) <= 1e-12 * D
    uu = np.asarray(rr["uu"], float)
    mm = 2.0 * np.asarray(rr["lam"], float)
    c_ar = np.asarray(core.arch_lags(M, D), float)
    c1 = np.asarray(core.atom_lags_at(alpha, M, uu, mm)[0], float)
    c0 = np.asarray(cont_lags(alpha, M, [0.0], [2.0 * alpha],
                              [1.0]), float)
    L = 2 * M - 2
    F = L // 2 + 1
    d1 = grid_density(c_ar + c1)[:F]
    d0 = grid_density(c_ar + c0)[:F]
    d0at = grid_density(c0)[:F]
    r = d1 - d0
    ff = np.arange(F)
    x = np.cos(2.0 * math.pi * ff / L)
    a = 2.0 * h * h * (1.0 - x)
    mult = np.where((ff == 0) | (ff == L // 2), 1.0, 2.0)
    qt = mult * 4.0 * np.sin(math.pi * ff / L) ** 2 / (2.0 * L)
    al_f = ff[(ff >= 1) & (d1 < 0.0)
              & (a <= h ** (2.0 * THETA_STAR))]
    al_f = al_f[np.argsort(a[al_f], kind="stable")]
    up = (d0 < 0.0) & (d1 > 0.0) & (qt > 0.0)
    dn = (d0 > 0.0) & (d1 < 0.0) & (qt > 0.0)
    ts = np.full(F, np.nan)
    ts[up | dn] = -d0[up | dn] / r[up | dn]
    breaks = np.unique(ts[up | dn])
    return dict(kz=kz, alpha=alpha, M=M, h=h, L=L, F=F, D=D,
                c_ar=c_ar, c0=c0, c1=c1, uu=uu, mm=mm,
                x=x, a=a, qt=qt, d0=d0, d1=d1, d0at=d0at, r=r,
                al_f=al_f, y_al=x[al_f], breaks=breaks,
                X=math.exp(2.0 * alpha))


def eval_state(R, dv, resid, al_f, need_J=True, qf=False):
    """Chain of the positive part of dv; per alias the Christoffel
    lambda, target mass nu, gap F = lambda - nu, and (optionally) the
    envelope derivative J built with residual `resid` and the masks
    of dv (at dv = d_t, resid = r this is F'_m(t) exactly)."""
    pos = (dv > 0.0) & (R["qt"] > 0.0)
    xs = R["x"][pos]
    ws = (R["qt"] * dv)[pos]
    h = R["h"]
    al, be, m0, steps = lanczos_chain(xs, ws, h + 1)
    if steps < h + 1:
        return None
    Phi = eval_chain(al, be, m0, R["x"][al_f], h)   # n_al x h
    K = np.sum(Phi ** 2, axis=1)
    lam = 1.0 / K
    nu = R["qt"][al_f] * np.maximum(-dv[al_f], 0.0)
    out = dict(lam=lam, nu=nu, G=lam - nu, chain=(al, be, m0),
               Phi=Phi, Kdiag=K, pos=pos)
    if need_J or qf:
        Ppos = eval_chain(al, be, m0, xs, h)
        U = Ppos @ Phi.T                            # n_pos x n_al
        if need_J:
            S = ((R["qt"] * resid)[pos] @ (U * U)) / K ** 2
            out["J"] = S + (R["qt"][al_f] * resid[al_f]
                            * (dv[al_f] < 0.0))
        if qf:
            out["qf_dev"] = float(np.max(np.abs(
                (ws @ (U * U)) / K - 1.0)))
    return out


# --------------------------------------- the prime-side regrouping (P1 alg.)
def kernel_block(R, e, dm):
    """W_{f,m} from the state e (chain/extremizer of the density with
    mask dm), chat, kernel at the atoms, prime sum, smooth
    subtraction and the two wards (paircorr_contract P1, verbatim,
    generalized to either endpoint via dm)."""
    al, be, m0 = e["chain"]
    h, F, M, L = R["h"], R["F"], R["M"], R["L"]
    Pall = eval_chain(al, be, m0, R["x"], h)        # F x h
    U0 = Pall @ e["Phi"].T                          # F x n_al
    P2 = (U0 * U0) / e["Kdiag"] ** 2                # p_m(x_f)^2
    af = R["al_f"]
    W = (R["qt"] * (dm > 0.0))[:, None] * P2        # F x n_al
    W[af, np.arange(len(af))] += (R["qt"][af] * (dm[af] < 0.0))
    A_grid = W.T @ R["r"]
    ii = np.arange(M)
    cosIF = np.cos((2.0 * math.pi / L)
                   * np.outer(ii, np.arange(F).astype(float)))
    w_i = np.where((ii == 0) | (ii == M - 1), 1.0, 2.0)
    chat = (cosIF @ W) * w_i[:, None]               # M x n_al
    del cosIF
    uu, D = R["uu"], R["D"]
    i0 = np.floor(uu / D).astype(int)
    fr = uu / D - i0
    v0 = np.where((i0 >= 0) & (i0 <= M - 1), 1.0 - fr, 0.0)
    v1 = np.where((i0 + 1 >= 0) & (i0 + 1 <= M - 1), fr, 0.0)
    Kat = -0.5 * (v0[:, None] * chat[np.clip(i0, 0, M - 1)]
                  + v1[:, None] * chat[np.clip(i0 + 1, 0, M - 1)])
    mir = uu < D
    if np.any(mir):
        Kat[mir] += -0.5 * ((1.0 - uu[mir] / D)[:, None]
                            * chat[0][None, :])
    S1 = R["mm"] @ Kat
    K0a = W.T @ R["d0at"]
    K0b = R["c0"] @ chat
    A_prime = S1 - K0a
    Sabs = np.abs(R["mm"]) @ np.abs(Kat) + np.abs(K0a)
    ward1 = float(np.max(np.abs(A_prime - A_grid)
                         / np.maximum(np.maximum(np.abs(A_grid),
                                                 Sabs), 1e-300)))
    ward2 = float(np.max(np.abs(K0b - K0a)
                         / np.maximum(np.abs(R["c0"])
                                      @ np.abs(chat), 1e-300)))
    return dict(chat=chat, A_grid=A_grid, A_prime=A_prime,
                Sabs=Sabs, ward1=ward1, ward2=ward2)


def fd_endpoint(R, res, side):
    """W-C: chamber-safe second-order one-sided Richardson FD of F'
    at t = 0 (side 0) or t = 1 (side 1).  Returns (max ratio
    |FD - F'| / allowance, eps, skipped) with the v2 additive
    allowance max(TOL_FD_WARD |F'|, NOISE_REL lambda / eps); pass
    iff the ratio <= 1."""
    br = R["breaks"]
    t_first = float(br[0]) if len(br) else 1.0
    t_last = float(br[-1]) if len(br) else 0.0
    gap = t_first if side == 0 else (1.0 - t_last)
    eps = min(EPS_FD, gap / 4.0)
    if eps < EPS_FD_MIN:
        return None, eps, True
    if side == 0:
        e1 = eval_state(R, R["d0"] + eps * R["r"], R["r"],
                        R["al_f"], need_J=False)
        e2 = eval_state(R, R["d0"] + 2.0 * eps * R["r"], R["r"],
                        R["al_f"], need_J=False)
        if e1 is None or e2 is None:
            return None, eps, None
        fd = (-3.0 * res["e0"]["G"] + 4.0 * e1["G"]
              - e2["G"]) / (2.0 * eps)
        Jref, lam_end = res["J0"], res["e0"]["lam"]
    else:
        e1 = eval_state(R, R["d1"] - eps * R["r"], R["r"],
                        R["al_f"], need_J=False)
        e2 = eval_state(R, R["d1"] - 2.0 * eps * R["r"], R["r"],
                        R["al_f"], need_J=False)
        if e1 is None or e2 is None:
            return None, eps, None
        fd = (3.0 * res["e1"]["G"] - 4.0 * e1["G"]
              + e2["G"]) / (2.0 * eps)
        Jref, lam_end = res["J1"], res["e1"]["lam"]
    allow = np.maximum(TOL_FD_WARD * np.abs(Jref),
                       NOISE_REL * lam_end / eps)
    return float(np.max(np.abs(fd - Jref) / allow)), eps, False


def main():
    section("PRIME.CASE.ENDPOINT.01 -- the concavity bracket + the "
            "one-sided endpoint derivative census (EXPLORATION "
            "ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s"
          % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
    print("    NO RH claim; no marker moves.")

    print("\nS0 -- firewall + self-tests")
    check("S0.1 AST firewall clean", not ast_scan(BANNED_IDS),
          kill="PIPELINE")

    section("B0 -- rungs (geometry, zone aliases, crossing "
            "bookkeeping)")
    RG = {}
    for kz in RUNGS:
        R = build_rung(kz)
        RG[kz] = R
        br = R["breaks"]
        print("    kz %-3d h %4d F %5d: atoms %5d, X %.3e, zone "
              "aliases %3d (a <= h^1.4 = %8.0f), crossings %4d "
              "in [%.4f, %.4f]"
              % (kz, R["h"], R["F"], len(R["uu"]), R["X"],
                 len(R["al_f"]), R["h"] ** 1.4, len(br),
                 float(br[0]) if len(br) else float("nan"),
                 float(br[-1]) if len(br) else float("nan")),
              flush=True)
    order = sorted(RUNGS, key=lambda kz: RG[kz]["h"])
    ok_al = all(len(RG[kz]["al_f"]) > 0 for kz in RUNGS)
    check("B0.1 zone alias sets nonempty on every rung", ok_al,
          kill="PIPELINE")
    if not ok_al:
        return finish(None, None)

    # S0.2 endpoint reconstruction vs verbatim folded route (kz 9)
    R9 = RG[9]
    dev_end = 0.0
    for tv in (0.0, 1.0):
        dv = R9["d0"] if tv == 0.0 else R9["d1"]
        d_full = np.concatenate([dv, dv[-2:0:-1]])
        xs, ws, _uf = folded_measure(d_full, R9["L"], +1.0)
        ys, vs, uf_n = folded_measure(d_full, R9["L"], -1.0)
        al, be, m0, steps = lanczos_chain(xs, ws, R9["h"] + 1)
        if steps < R9["h"] + 1:
            check("S0.2 endpoint chain (verbatim route)", False,
                  kill="PIPELINE")
            return finish(None, None)
        Pn = eval_chain(al, be, m0, R9["y_al"], R9["h"])
        lam_ref = 1.0 / np.sum(Pn ** 2, axis=1)
        pos_map = {int(f): float(v) for f, v in zip(uf_n, vs)}
        nu_ref = np.array([pos_map.get(int(f), 0.0)
                           for f in R9["al_f"]])
        e = eval_state(R9, dv, R9["r"], R9["al_f"], need_J=False)
        if e is None:
            check("S0.2 endpoint chain (qt route)", False,
                  kill="PIPELINE")
            return finish(None, None)
        dev_end = max(dev_end, float(np.max(
            np.abs(e["lam"] / lam_ref - 1.0))))
        dev_end = max(dev_end, float(np.max(
            np.abs(e["nu"] - nu_ref)
            / np.maximum(np.abs(nu_ref), 1e-300))))
    check("S0.2 endpoint reconstruction == verbatim folded route "
          "(kz 9, t = 0 and 1)", dev_end <= TOL_SELF_END,
          "rel sup dev %.2e" % dev_end, kill="PIPELINE")

    section("E1 -- THE THREE NUMBERS: F'(0), F'(1), Delta = F(1) - "
            "F(0) per (rung, alias) + wards + bracket defect")
    RES = {}
    ok_e = True
    qf_worst = 0.0
    wA_max = wB_max = 0.0
    fdC_worst = 0.0            # max over rungs of (dev / bar), W-C
    fd_skipped = []
    defect_max = 0.0
    for kz in order:
        R = RG[kz]
        t_a = time.time()
        e0 = eval_state(R, R["d0"], R["r"], R["al_f"], need_J=True,
                        qf=True)
        e1 = eval_state(R, R["d1"], R["r"], R["al_f"], need_J=True,
                        qf=True)
        if e0 is None or e1 is None:
            ok_e = False
            print("    kz %-3d: CHAIN SHORT at an endpoint" % kz)
            break
        qf_worst = max(qf_worst, e0["qf_dev"], e1["qf_dev"])
        J0, J1 = e0["J"], e1["J"]
        delta = e1["G"] - e0["G"]
        res = dict(e0=e0, e1=e1, J0=J0, J1=J1, delta=delta,
                   ms=int(np.argmin(e1["G"])))
        RES[kz] = res
        # W-A / W-B: prime-side regrouping at both endpoints
        kb0 = kernel_block(R, e0, R["d0"])
        kb1 = kernel_block(R, e1, R["d1"])
        res["kb0"], res["kb1"] = kb0, kb1
        wa0 = float(np.max(np.abs(J0 - kb0["A_prime"])
                           / np.maximum(np.maximum(
                               np.abs(kb0["A_grid"]),
                               kb0["Sabs"]), 1e-300)))
        wa1 = float(np.max(np.abs(J1 - kb1["A_prime"])
                           / np.maximum(np.maximum(
                               np.abs(kb1["A_grid"]),
                               kb1["Sabs"]), 1e-300)))
        wA_max = max(wA_max, wa0, wa1)
        wB_max = max(wB_max, kb0["ward2"], kb1["ward2"])
        # W-C: endpoint FD wards (chamber-safe, additive allowance)
        fd_txt = ""
        for side in (0, 1):
            dev, eps, skip = fd_endpoint(R, res, side)
            if skip is None:
                check("E1 FD chains complete (kz %d)" % kz, False,
                      kill="PIPELINE")
                return finish(None, None)
            if skip:
                fd_skipped.append((kz, side, eps))
                fd_txt += "  FD t=%d SKIPPED (e %.1e)" % (side, eps)
            else:
                fdC_worst = max(fdC_worst, dev)
                fd_txt += ("  FD t=%d dev/allow %.2e (e %.1e)"
                           % (side, dev, eps))
        # bracket defect (measurement)
        scale = np.maximum(np.maximum(np.abs(J0), np.abs(J1)),
                           np.abs(delta))
        d_hi = np.maximum(delta - J0, 0.0) / np.maximum(scale,
                                                        1e-300)
        d_lo = np.maximum(J1 - delta, 0.0) / np.maximum(scale,
                                                        1e-300)
        dmax = float(max(np.max(d_hi), np.max(d_lo)))
        defect_max = max(defect_max, dmax)
        n_bad = int(np.sum((d_hi > BRACKET_CLEAN)
                           | (d_lo > BRACKET_CLEAN)))
        n_nu_cross = int(np.sum(R["d0"][R["al_f"]] > 0.0))
        res["defect"] = dmax
        ms = res["ms"]
        print("    kz %-3d h %4d (n_al %2d): F'(0) med %+.3e | "
              "F'(1) med %+.3e | Delta med %+.3e | m* %d: "
              "F'(0) %+.3e  F'(1) %+.3e  Delta %+.3e"
              % (kz, R["h"], len(R["al_f"]),
                 float(np.median(J0)), float(np.median(J1)),
                 float(np.median(delta)), ms + 1,
                 float(J0[ms]), float(J1[ms]),
                 float(delta[ms])))
        print("      wards: W-A t0 %.2e t1 %.2e | W-B %.2e/%.2e |"
              "%s" % (wa0, wa1, kb0["ward2"], kb1["ward2"],
                      fd_txt))
        print("      bracket F'(1) <= Delta <= F'(0): max rel "
              "defect %.2e | aliases beyond %.0e: %d/%d | mask "
              "crossings %d, alias nu-crossings %d  [%.1f s]"
              % (dmax, BRACKET_CLEAN, n_bad, len(R["al_f"]),
                 len(R["breaks"]), n_nu_cross,
                 time.time() - t_a), flush=True)
    check("E0 endpoint chains complete on all rungs", ok_e,
          kill="PIPELINE")
    check("S0.3 quadratic-form self-test (sum w p*^2 == lambda, "
          "both endpoints, all rungs)", ok_e
          and qf_worst <= TOL_QF, "worst rel dev %.2e" % qf_worst,
          kill="PIPELINE")
    if not ok_e:
        return finish(None, None)
    check("E1.W-A prime-side regrouping == envelope F' at both "
          "endpoints (max rel %.2e <= %.0e)"
          % (wA_max, TOL_WARD_PRIME), wA_max <= TOL_WARD_PRIME,
          kill="WARD")
    check("E1.W-B smooth subtraction route a == route b (max rel "
          "%.2e <= %.0e)" % (wB_max, TOL_WARD_K0),
          wB_max <= TOL_WARD_K0, kill="WARD")
    check("E1.W-C endpoint FD wards (worst dev/allowance %.2e <= "
          "1; %d skipped-disclosed)" % (fdC_worst,
                                        len(fd_skipped)),
          fdC_worst <= 1.0, kill="WARD")
    bracket_flag = ("CLEAN" if defect_max <= BRACKET_CLEAN
                    else "CROSSING-CORRECTED max %.1e" % defect_max)
    check("E1.1 bracket defect measured: %s (measurement, never a "
          "kill)" % bracket_flag, True)

    section("E2 -- THE DECISIVE CENSUS: F'(1) >= deficit_m = "
            "(nu_0 - lambda_0)_m per critical cell")
    n_pass = n_all = 0
    fails = []
    pass0 = 0
    for kz in order:
        R = RG[kz]
        res = RES[kz]
        deficit = -res["e0"]["G"]
        margin = res["J1"] - deficit
        margin0 = res["J0"] - deficit
        ok_cells = margin >= 0.0
        n_pass += int(np.sum(ok_cells))
        n_all += len(margin)
        pass0 += int(np.sum(margin0 >= 0.0))
        for i in np.nonzero(~ok_cells)[0]:
            fails.append((kz, int(i) + 1, int(R["al_f"][i]),
                          float(margin[i])))
        print("    kz %-3d h %4d (n_al %d): pass %d/%d | margin "
              "F'(1)-deficit min %+.3e med %+.3e | F'(0)-deficit "
              "min %+.3e (contrast)"
              % (kz, R["h"], len(margin), int(np.sum(ok_cells)),
                 len(margin), float(np.min(margin)),
                 float(np.median(margin)), float(np.min(margin0))))
        print("      %-4s %-5s %-9s %-11s %-11s %-11s %-11s"
              % ("m", "f", "a_m", "F'(1)", "deficit", "margin",
                 "F'(0)"))
        show = list(range(min(SHOW_ROWS, len(margin))))
        im = int(np.argmin(margin))
        if im not in show:
            show.append(im)
        for i in show:
            print("      %-4d %-5d %-9.1f %+.3e  %+.3e  %+.3e  "
                  "%+.3e%s"
                  % (i + 1, int(R["al_f"][i]),
                     float(R["a"][R["al_f"][i]]),
                     float(res["J1"][i]), float(deficit[i]),
                     float(margin[i]), float(res["J0"][i]),
                     "  <- min margin" if i == im else ""),
                  flush=True)
    if n_pass == n_all:
        etype = "ENDPOINT-SUFFICES"
    elif n_pass > 0:
        etype = "ENDPOINT-PARTIAL"
    else:
        etype = "ENDPOINT-INSUFFICIENT"
    print("    census: %d/%d cells pass (F'(0) contrast census: "
          "%d/%d) -> %s" % (n_pass, n_all, pass0, n_all, etype))
    if fails and etype == "ENDPOINT-PARTIAL":
        print("    failing cells (kz, m, f, margin): %s"
              % "; ".join("(%d, %d, %d, %+.2e)" % c
                          for c in fails[:20])
              + (" ... +%d more" % (len(fails) - 20)
                 if len(fails) > 20 else ""))
    check("E2.1 decisive census typed: %s (measurement)" % etype,
          True)

    section("E3 -- THE LINEAR FUNCTIONAL: truth-side kernel K^(1) "
            "vs PNT-side K^(0) + the circularity statement")
    if n_pass > 0:
        for kz in order:
            R = RG[kz]
            res = RES[kz]
            ms = res["ms"]
            for tag, mi in (("m*", ms), ("m1", 0)):
                if tag == "m1" and ms == 0:
                    continue
                K0i = -0.5 * res["kb0"]["chat"][1:, mi]
                K1i = -0.5 * res["kb1"]["chat"][1:, mi]
                ug = np.arange(1, R["M"]) * R["D"]
                den = max(float(np.linalg.norm(K0i)
                                * np.linalg.norm(K1i)), 1e-300)
                corr = float((K0i @ K1i) / den)
                rel = float(np.linalg.norm(K1i - K0i)
                            / max(np.linalg.norm(K0i), 1e-300))
                p0 = float(ug[int(np.argmax(np.abs(K0i)))])
                p1 = float(ug[int(np.argmax(np.abs(K1i)))])
                print("    kz %-3d %s (alias %2d, f %4d): "
                      "corr(K0,K1) %+.4f | ||K1-K0||/||K0|| %.3f |"
                      " peaks u %.2f -> %.2f (2a %.2f) | J: "
                      "F'(0) %+.3e -> F'(1) %+.3e"
                      % (kz, tag, mi + 1, int(R["al_f"][mi]),
                         corr, rel, p0, p1, 2.0 * R["alpha"],
                         float(res["J0"][mi]),
                         float(res["J1"][mi])), flush=True)
        print("\n    CIRCULARITY (what a theorem would need): "
              "F'(1) = sum_n mu_n K^(1)(log n) - K0^(1) is linear "
              "in the masses ONLY AT FIXED KERNEL; K^(1) carries "
              "the truth mask and the truth extremizer p_{1,m} -- "
              "both functionals of the comb.  Needed: (a) a "
              "stability lemma p_{1,m} ~ p_{0,m} + mask stability "
              "(the measured kernel distances above gauge it), "
              "transferring the census to the PNT-computable "
              "K^(0); or (b) a self-consistent one-sided bound "
              "over an admissible density class containing d_1.")
    else:
        print("    census empty (no cell passes) -> E3 comparison "
              "suppressed per the frozen spec; the pair route "
              "stands.")
    check("E3.1 linear-functional reading recorded (measurement)",
          True)

    section("E4 -- THE BRACKET LADDER (medians over aliases; h "
            "ascending) + the h-trend of the concavity drop")
    print("    %-5s %-5s %-4s %-11s %-11s %-11s %-11s %-9s"
          % ("kz", "h", "n_al", "F'(0)", "F'(1)", "Delta",
             "gap=F'0-F'1", "gap/|D|"))
    hh, gg = [], []
    for kz in order:
        R = RG[kz]
        res = RES[kz]
        gap = res["J0"] - res["J1"]
        mg = float(np.median(gap))
        md = float(np.median(np.abs(res["delta"])))
        print("    %-5d %-5d %-4d %+.3e  %+.3e  %+.3e  %+.3e  "
              "%7.3f"
              % (kz, R["h"], len(R["al_f"]),
                 float(np.median(res["J0"])),
                 float(np.median(res["J1"])),
                 float(np.median(res["delta"])), mg,
                 mg / max(md, 1e-300)))
        if mg > 0.0:
            hh.append(math.log(R["h"]))
            gg.append(math.log(mg))
    if len(hh) >= 3:
        slope = float(np.polyfit(hh, gg, 1)[0])
        print("    h-trend of the median gap: log-log slope %+.3f "
              "-> the concavity drop is %s with depth"
              % (slope, "SHRINKING" if slope < 0.0 else
                 "NOT shrinking"))
    else:
        slope = float("nan")
        print("    h-trend: fewer than 3 rungs with positive "
              "median gap -- no slope fitted (disclosed).")
    check("E4.1 bracket ladder recorded (measurement)", True)

    section("C -- controls (kz 9, scramble seed %d)"
            % SCRAMBLE_SEED)
    rng = np.random.default_rng(SCRAMBLE_SEED)
    us = np.sort(rng.uniform(0.0, 2.0 * R9["alpha"],
                             size=len(R9["uu"])))
    c_s = np.asarray(core.atom_lags_at(R9["alpha"], R9["M"], us,
                                       R9["mm"])[0], float)
    d_s = grid_density(R9["c_ar"] + c_s)[:R9["F"]]
    r_s = d_s - R9["d0"]
    ff9 = np.arange(R9["F"])
    neg_s = ff9[(ff9 >= 1) & (d_s < 0.0)]
    neg_s = neg_s[np.argsort(R9["a"][neg_s], kind="stable")]
    al_zone = neg_s[R9["a"][neg_s]
                    <= R9["h"] ** (2.0 * THETA_STAR)]
    fell_back = len(al_zone) == 0
    al_use = al_zone if not fell_back else neg_s[:CTRL_FALLBACK_AL]
    es = eval_state(R9, d_s, r_s, al_use, need_J=True)
    if es is None:
        check("C0 scramble chain completes", False,
              kill="PIPELINE")
        return finish(etype, bracket_flag)
    j1s = float(np.min(es["J"]))
    fires = j1s <= 0.0
    print("    scramble aliases: %d%s | min F'_scr(1) = %+.3e "
          "(real kz 9 min F'(1) = %+.3e) -> %s"
          % (len(al_use),
             " (zone empty -> frozen fallback: %d a-closest neg "
             "nodes)" % CTRL_FALLBACK_AL if fell_back else
             " (zone aliases)",
             j1s, float(np.min(RES[9]["J1"])),
             "FIRES" if fires else "SILENT"), flush=True)
    check("C1 value control fires (scramble drives the endpoint "
          "derivative negative)", fires, kill="CONTROL")

    return finish(etype, bracket_flag)


def finish(etype, bracket_flag):
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
        VERDICT = "ENDPOINT-MEASURED"
    sub = []
    if etype:
        sub.append("TYPE=%s" % etype)
    if bracket_flag:
        sub.append("BRACKET=%s" % bracket_flag)
    print("\n  VERDICT: %s%s"
          % (VERDICT, (" (%s)" % "; ".join(sub)) if sub else ""))
    if VERDICT == "ENDPOINT-MEASURED" and etype:
        if etype == "ENDPOINT-SUFFICES":
            print("  PLAIN ANSWER: YES on the finite shadow -- the "
                  "one-sided endpoint derivative F'(1) clears the "
                  "deficit on EVERY critical cell, so the contract "
                  "collapses to a LINEAR signed-Lambda functional "
                  "at the truth, modulo the measured bracket/"
                  "crossing corrections and the circularity caveat "
                  "(E3).")
        elif etype == "ENDPOINT-PARTIAL":
            print("  PLAIN ANSWER: PARTLY -- F'(1) clears the "
                  "deficit on some cells only; the linear route "
                  "covers those, the genuine pair-correlation "
                  "input stands on the listed failing cells.")
        else:
            print("  PLAIN ANSWER: NO -- F'(1) clears the deficit "
                  "nowhere; the one-sided endpoint bound is too "
                  "weak and the pair-correlation contract stands "
                  "as the needed input.")
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed"
          % (time.time() - T0, n_tot, n_tot - n_pass))
    return 0 if n_pass == n_tot else 1


if __name__ == "__main__":
    raise SystemExit(main())
'''

# ------------- frozen probe source inner_zone_linear_probe (embedded BYTE-EXACT, raw string)
_SRC_2 = r'''
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""inner_zone_linear_probe -- PRIME.CASE.INNERLINEAR.01
(EXPLORATION ONLY, experiments/; round 52, named object (c): the
INNER-ZONE LINEAR ROUTE of the diagonal half -- the refinement
opened by ENDPOINT-PARTIAL.  2026-08-09.)

CONTEXT (machinery verbatim from endpoint_bracket_probe /
paircorr_contract_probe / signed_homotopy_probe): round 51 measured
the one-sided endpoint derivative F'(1) of the diagonal-half
homotopy against the PNT-reference deficit and typed the census
ENDPOINT-PARTIAL: F'(1) >= deficit passes on ALL small-a cells of
the deep rungs with monotone margins, fails at shallow rungs and at
the zone edge a ~ h^{1.4}; the truth/PNT kernel distance
||K^(1) - K^(0)|| / ||K^(0)|| is 0.16..0.4 deep (p1 ~ p0 stability
plausible) and 0.89 shallow; the concavity drop F'(0) - F'(1)
shrinks at log-log slope -1.5.  christoffel_zone_envelope_probe
froze the critical zone a <= h^{2 theta*}, theta* = 0.700;
paircorr_contract_probe froze the kernel regrouping
J = sum_n mu_n K_{h,m}(log n) - K0 and the deficit ledger.  THIS
probe asks: is there an INNER exponent theta_in < theta* such that
on the inner zone {a <= h^{2 theta_in}} the LINEAR route (the
one-sided endpoint bound F'(1) >= deficit) covers EVERYTHING on the
deep half -- so the genuinely hard part (the pair-correlation
input) contracts from the whole zone to the MIDDLE BAND
h^{2 theta_in} < a <= h^{1.4}?

FROZEN PROTOCOL (2026-08-09; constants frozen before the first
measurement run; budget < 20 min):

 RUNGS: heavy kz {9, 12, 13, 26, 40} + the deepest 3 with complete
   atom tables kz {88, 90, 116} (verbatim round-51 selection;
   X <= 4e5).  DEEP HALF = the 4 highest-h rungs of the 8 (sorted
   by (h, kz) ascending).
 ALIASES: all port aliases in the frozen critical zone -- truth
   neg nodes (d_1(f) < 0, f >= 1) with a_{h,f} = 2 h^2 (1 - x_f)
   <= h^{2 theta*}, theta* = 0.700, ranked by a ascending
   (verbatim).  Per rung: deficit_m = (nu_0 - lambda_0)_m =
   -F_m(0), the endpoint derivatives F'(0) = J at t = 0 and
   F'(1) = J at t = 1 (exact envelope formula, verbatim round-51),
   the exact full difference Delta_m = F(1) - F(0), the linear
   margin margin1 = F'(1) - deficit and the full margin
   marginF = Delta - deficit = (lambda_1 - nu_1)_m (exact
   identity).

 Z1 THE INNER EXPONENT: for theta_in in the frozen grid
   {0.40, 0.50, 0.60, 2/3, 0.70} restrict to the inner cells
   a_m <= h^{2 theta_in}; census per rung: pass iff margin1 >= 0
   on every inner cell.  ELIGIBILITY of a grid theta_in
   (pre-registered): (i) the inner set is NONEMPTY on every
   deep-half rung (a vacuous census does not count), (ii) 100%
   pass on every deep-half rung, (iii) POSITIVE MARGIN TREND: all
   deep-half inner min margins > 0 and the least-squares slope of
   log(min margin) vs log(h) over the 4 deep-half rungs is > 0.
   theta_in* = the LARGEST eligible grid theta_in.  Census table
   printed for ALL 8 rungs (the shallow failures stay disclosed).
   TYPED: INNER-ZONE(theta_in*) iff some grid point is eligible,
   else INNER-EMPTY.

 Z2 THE MIDDLE-BAND ACCOUNTING (at theta_in*; if INNER-EMPTY, at
   the frozen fallback 2/3, disclosed, for the record): the BAND =
   zone cells with h^{2 theta_in*} < a_m <= h^{1.4}.  Per rung:
   n_band, n_zone, the band fraction n_band/n_zone, the band
   census under the FULL nonlinear difference (pass iff
   marginF >= 0 -- the homotopy truth; this is where the
   pair-correlation input remains), min/median band marginF, the
   per-cell table (first 6 + argmin).  The h-trend of the band
   fraction: least-squares slope of log(fraction) vs log(h) over
   the rungs with a nonempty band (SHRINKING iff slope < 0;
   n/a if < 3 usable rungs, disclosed).

 Z3 THE STABILITY LEMMA SHADOW (deep-half rungs): per INNER-zone
   alias (not just the critical one) the kernel distance
   relK_m = ||K^(1)_m - K^(0)_m|| / ||K^(0)_m|| and the cosine
   corr(K^(0)_m, K^(1)_m) on the lag grid i = 1..M-1 (verbatim
   round-51 E3 comparison, extended to the full inner profile);
   per rung the profile rows (first 10 + argmax relK), max and
   median relK.  THE LINEAR-ROUTE THEOREM SKELETON printed with
   the measured numbers filled in: IF (i) p1 ~ p0 stability at the
   measured level on the inner zone (kernel transfer error
   controlled by the printed relK profile), AND (ii) the ONE-SIDED
   linear bound sum_n mu_n K^(0)_{h,m}(log n) - K0 >= deficit_m +
   stability-error on the inner zone, THEN T_h <= 1 on the inner
   zone; the remaining hard part is the BAND, not the zone.  The
   K^(0) census (F'(0) >= deficit, the PNT-computable side) is
   printed alongside on the inner cells; the transfer gap
   F'(0) - F'(1) per inner cell is the measured stability-error
   scale.  THE BAND SIZE, honestly: per deep rung the band alias
   fraction n_band/n_zone, the band nu_1-mass fraction
   sum_band nu_1 / sum_zone nu_1 and the band deficit fraction
   sum_band deficit / sum_zone deficit.

 Z4 THE CLASSICAL FORM OF THE INNER HYPOTHESIS (report; all 8
   rungs): the PNT-side kernels K^(0)_m restricted to the inner
   zone, profiled exactly as paircorr_contract P1/P3: per alias
   n90 = the number of f-modes carrying 90% of sum_f |W_{f,m}|
   (f >= 1), the 90%-mass support width fraction u_frac =
   width90/(2 alpha) (smallest contiguous u-window carrying 90%
   of sum_i |K(iD)|), and the |W|-weighted mean alias frequency
   tau_mean.  Printed per rung: inner rows (first 8) and band
   rows (first 6) + the inner/band medians.  FROZEN comparative
   reading per rung (needs both sets nonempty): the inner kernels
   are SOFTER iff median u_frac(inner) <= median u_frac(band) AND
   median tau_mean(inner) <= median tau_mean(band).  TYPED:
   CLASSICAL=INNER-SOFTER iff softer on a strict majority of the
   comparable rungs, INNER-NOT-SOFTER else, n/a iff < 2 rungs
   comparable (band empty almost everywhere).

 C  CONTROLS (kz 9, scramble seed 1, the deployed mirror:
   positions uniform on (0, 2 alpha), same masses; frozen control
   exponent theta_ctrl = 2/3, frozen BEFORE theta_in* is known):
   the scramble INNER census must BREAK -- with scramble aliases
   = scramble neg nodes with a <= h^{2 theta_ctrl} (fallback,
   disclosed if empty: the 8 a-closest scramble neg nodes), the
   min over them of F'_scr(1) - deficit_scr must be < 0
   (deficit_scr = (nu_0 - lambda_0) at the scramble alias nodes;
   F'_scr(1) = the truth-side envelope formula at d_scr with
   residual r_s = d_scr - d_0, verbatim round-51 control).
   Silent -> CONTROL-DEAD.

 WARDS (kill WARD-BROKEN on failure; verbatim round-50/51):
   (W-A) prime-side regrouping == grid form at BOTH endpoints,
         rel <= 1e-10 per alias against max(|W.r|, sum_n mu_n |K|
         + |K0|);
   (W-B) smooth-subtraction route a (W.d0at) == route b (c0.chat)
         at both endpoints, rel <= 1e-12.
   (The round-51 W-C endpoint FD ward is NOT repeated here: the
   identical F' values were FD-certified in round 51; dropping a
   passed ward adds no risk and saves 16 chain builds.)

 SELF-TESTS (S0, kill PIPELINE on failure): (i) AST firewall
   clean; (ii) endpoint reconstruction (kz 9): the qt-route
   lambda/nu at the zone aliases vs the verbatim folded_measure
   route, rel <= 1e-8, at both t = 0 and t = 1; (iii) quadratic-
   form self-test per rung at both endpoints: sum_j w_j p*^2 ==
   lambda to rel 1e-8 (verbatim TOL_QF).

KILLS: chain short anywhere needed / self-test failure / zone
alias set empty on a rung -> PIPELINE-BROKEN; W-A / W-B ward
failure -> WARD-BROKEN; value control silent -> CONTROL-DEAD.
Z1 / Z2 / Z3 / Z4 outcomes are MEASUREMENTS, never kills:
INNER-EMPTY is a finding.

VERDICT (frozen enum): INNERLINEAR-MEASURED (+ TYPE=<INNER-
ZONE(theta_in*) | INNER-EMPTY> + BAND=<n cells, SHRINKING |
NON-SHRINKING | n/a> + STABILITY=<max inner relK deep> +
CLASSICAL=<INNER-SOFTER | INNER-NOT-SOFTER | n/a>) /
PIPELINE-BROKEN / WARD-BROKEN / CONTROL-DEAD.

SPEC AMENDMENTS (fail-first preserved):
  v1 (2026-08-09): initial freeze.  The rung set, alias
  bookkeeping, envelope formula, kernel regrouping, wards and the
  scramble mirror are verbatim round-50/51 machinery; the inner
  grid {0.40, 0.50, 0.60, 2/3, 0.70}, the eligibility rule
  (nonempty + 100% deep pass + positive trend), the Z2 fallback
  2/3, the Z4 softness rule and the control exponent 2/3 were all
  frozen before any number was computed.
  v2 (2026-08-09, after the first full run; fail-first preserved):
  the first run returned INNERLINEAR-MEASURED with TYPE=INNER-EMPTY
  and every ward green -- the deep-half census is 100% at theta_in
  = 0.40 and 0.50 but the ABSOLUTE min-margin h-trend is -1.05, so
  criterion (iii) fails.  Because every scale of the problem
  (deficit, F'(0), F'(1)) itself shrinks like ~ h^-1 on this
  ladder, the absolute trend conflates the global scale shrinkage
  with a genuine margin decay.  v2 ADDS two DISCLOSED diagnostics
  to the Z1 print for census-passing grid points, both pure
  measurements: (a) the scale-normalized trend, the least-squares
  slope of log(h x min margin) vs log(h) over the deep half, and
  (b) the round-51-style within-rung monotonicity flag per deep
  rung (margin1 non-increasing along a ascending).  The
  ELIGIBILITY RULE AND THE TYPED OUTCOME ARE UNCHANGED (v1 rule;
  the first-run verdict INNER-EMPTY stands); no bar moved, no
  measured number changed.

NO RH claim: every number is finite exact linear algebra /
calculus on the deployed v563 window family; a frozen theta_in*
is an inner-zone split of the finite ladder shadow, not a bound,
no rate, no uniformity in h, and the linear route carries the
round-51 circularity caveat verbatim (K^(1) is truth-built; the
transfer to K^(0) NEEDS the stability lemma whose measured shadow
Z3 prints).  No marker moves.

FIREWALL: no zeros, no prime oracles beyond the deployed table
(AST scan: zetazero/nzeros/primerange/isprime/primepi/nextprime/
prevprime banned); v563 READ-ONLY; RNG only in the scramble
control; stdout only.

Sources (read-only): v563_paper2_readouts (window geometry, tent
assembly, arch lags, deployed atom table); endpoint_bracket_probe
(endpoint derivatives, wards, deep-rung selection -- verbatim);
signed_homotopy_probe (envelope identity, eval machinery --
verbatim); paircorr_contract_probe (kernel regrouping W/chat/K,
profile machinery n90/width90/tau, deficit ledger -- verbatim);
christoffel_pnt_gamma_probe (W2 closed-form PNT lags, folded
measures, Lanczos chain); christoffel_zone_envelope_probe
(theta* = 0.700), declared inputs.

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/inner_zone_linear_probe.py
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
DEEP3 = (88, 90, 116)          # frozen (round-51 selection)
RUNGS = tuple(sorted(set(HEAVY) | set(DEEP3)))
THETA_STAR = 0.700             # frozen zone exponent (ZONESPLIT.01)
INNER_GRID = (0.40, 0.50, 0.60, 2.0 / 3.0, 0.70)   # Z1 frozen grid
THETA_FALLBACK = 2.0 / 3.0     # Z2 fallback iff INNER-EMPTY
THETA_CTRL = 2.0 / 3.0         # C: frozen control exponent
TOL_WARD_PRIME = 1.0e-10       # W-A: prime-side form == grid form
TOL_WARD_K0 = 1.0e-12          # W-B: K0 route a == route b
TOL_SELF_END = 1.0e-8          # S0.2 endpoint reconstruction
TOL_QF = 1.0e-8                # S0.3 quadratic-form self-test
FRAC_MASS = 0.90               # Z4 profile mass fraction (frozen)
SHOW_Z1 = 8                    # Z1: all 8 rungs printed
SHOW_BAND = 6                  # Z2: band rows shown per rung
SHOW_STAB = 10                 # Z3: inner profile rows per rung
SHOW_IN = 8                    # Z4: inner rows shown per rung
MIN_TREND_RUNGS = 3            # Z2: rungs needed for a slope
SCRAMBLE_SEED = 1
CTRL_FALLBACK_AL = 8           # C: a-closest neg nodes fallback
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
# (grid density, folded measures, Lanczos chain, CD kernel, W2 closed-form
#  PNT lags: verbatim from endpoint_bracket_probe / paircorr_contract_probe)

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


# --------------------------------------------------------- rung construction
def build_rung(kz):
    """Folded d_PNT, d_truth, residual, weights and zone aliases of
    one rung (verbatim round-51)."""
    rr = core.build_window(kz)
    alpha, M, h, D = rr["alpha"], rr["M"], rr["h"], rr["D"]
    assert abs(D - 2.0 * alpha / M) <= 1e-12 * D
    uu = np.asarray(rr["uu"], float)
    mm = 2.0 * np.asarray(rr["lam"], float)
    c_ar = np.asarray(core.arch_lags(M, D), float)
    c1 = np.asarray(core.atom_lags_at(alpha, M, uu, mm)[0], float)
    c0 = np.asarray(cont_lags(alpha, M, [0.0], [2.0 * alpha],
                              [1.0]), float)
    L = 2 * M - 2
    F = L // 2 + 1
    d1 = grid_density(c_ar + c1)[:F]
    d0 = grid_density(c_ar + c0)[:F]
    d0at = grid_density(c0)[:F]
    r = d1 - d0
    ff = np.arange(F)
    x = np.cos(2.0 * math.pi * ff / L)
    a = 2.0 * h * h * (1.0 - x)
    mult = np.where((ff == 0) | (ff == L // 2), 1.0, 2.0)
    qt = mult * 4.0 * np.sin(math.pi * ff / L) ** 2 / (2.0 * L)
    al_f = ff[(ff >= 1) & (d1 < 0.0)
              & (a <= h ** (2.0 * THETA_STAR))]
    al_f = al_f[np.argsort(a[al_f], kind="stable")]
    return dict(kz=kz, alpha=alpha, M=M, h=h, L=L, F=F, D=D,
                c_ar=c_ar, c0=c0, c1=c1, uu=uu, mm=mm,
                x=x, a=a, qt=qt, d0=d0, d1=d1, d0at=d0at, r=r,
                al_f=al_f, y_al=x[al_f], a_al=a[al_f],
                X=math.exp(2.0 * alpha))


def eval_state(R, dv, resid, al_f, need_J=True, qf=False):
    """Chain of the positive part of dv; per alias the Christoffel
    lambda, target mass nu, gap F = lambda - nu, and (optionally)
    the envelope derivative J built with residual `resid` and the
    masks of dv (verbatim round-51)."""
    pos = (dv > 0.0) & (R["qt"] > 0.0)
    xs = R["x"][pos]
    ws = (R["qt"] * dv)[pos]
    h = R["h"]
    al, be, m0, steps = lanczos_chain(xs, ws, h + 1)
    if steps < h + 1:
        return None
    Phi = eval_chain(al, be, m0, R["x"][al_f], h)   # n_al x h
    K = np.sum(Phi ** 2, axis=1)
    lam = 1.0 / K
    nu = R["qt"][al_f] * np.maximum(-dv[al_f], 0.0)
    out = dict(lam=lam, nu=nu, G=lam - nu, chain=(al, be, m0),
               Phi=Phi, Kdiag=K, pos=pos)
    if need_J or qf:
        Ppos = eval_chain(al, be, m0, xs, h)
        U = Ppos @ Phi.T                            # n_pos x n_al
        if need_J:
            S = ((R["qt"] * resid)[pos] @ (U * U)) / K ** 2
            out["J"] = S + (R["qt"][al_f] * resid[al_f]
                            * (dv[al_f] < 0.0))
        if qf:
            out["qf_dev"] = float(np.max(np.abs(
                (ws @ (U * U)) / K - 1.0)))
    return out


# --------------------------------------- the prime-side regrouping (P1 alg.)
def kernel_block(R, e, dm):
    """W_{f,m}, chat, kernel at the atoms, prime sum, smooth
    subtraction and the two wards, from the state e (chain of the
    density with mask dm); verbatim paircorr_contract P1,
    generalized to either endpoint via dm (round-51)."""
    al, be, m0 = e["chain"]
    h, F, M, L = R["h"], R["F"], R["M"], R["L"]
    Pall = eval_chain(al, be, m0, R["x"], h)        # F x h
    U0 = Pall @ e["Phi"].T                          # F x n_al
    P2 = (U0 * U0) / e["Kdiag"] ** 2                # p_m(x_f)^2
    af = R["al_f"]
    W = (R["qt"] * (dm > 0.0))[:, None] * P2        # F x n_al
    W[af, np.arange(len(af))] += (R["qt"][af] * (dm[af] < 0.0))
    A_grid = W.T @ R["r"]
    ii = np.arange(M)
    cosIF = np.cos((2.0 * math.pi / L)
                   * np.outer(ii, np.arange(F).astype(float)))
    w_i = np.where((ii == 0) | (ii == M - 1), 1.0, 2.0)
    chat = (cosIF @ W) * w_i[:, None]               # M x n_al
    del cosIF
    uu, D = R["uu"], R["D"]
    i0 = np.floor(uu / D).astype(int)
    fr = uu / D - i0
    v0 = np.where((i0 >= 0) & (i0 <= M - 1), 1.0 - fr, 0.0)
    v1 = np.where((i0 + 1 >= 0) & (i0 + 1 <= M - 1), fr, 0.0)
    Kat = -0.5 * (v0[:, None] * chat[np.clip(i0, 0, M - 1)]
                  + v1[:, None] * chat[np.clip(i0 + 1, 0, M - 1)])
    mir = uu < D
    if np.any(mir):
        Kat[mir] += -0.5 * ((1.0 - uu[mir] / D)[:, None]
                            * chat[0][None, :])
    S1 = R["mm"] @ Kat
    K0a = W.T @ R["d0at"]
    K0b = R["c0"] @ chat
    A_prime = S1 - K0a
    Sabs = np.abs(R["mm"]) @ np.abs(Kat) + np.abs(K0a)
    ward1 = float(np.max(np.abs(A_prime - A_grid)
                         / np.maximum(np.maximum(np.abs(A_grid),
                                                 Sabs), 1e-300)))
    ward2 = float(np.max(np.abs(K0b - K0a)
                         / np.maximum(np.abs(R["c0"])
                                      @ np.abs(chat), 1e-300)))
    return dict(W=W, chat=chat, A_grid=A_grid, A_prime=A_prime,
                Sabs=Sabs, ward1=ward1, ward2=ward2)


# ----------------------------------------------- Z4 profiles (paircorr P1)
def min_window(mass, frac):
    """Smallest contiguous index window with >= frac of sum(mass)."""
    tot = float(np.sum(mass))
    target = frac * tot
    jl, csum, best = 0, 0.0, None
    for jr in range(len(mass)):
        csum += mass[jr]
        while csum - mass[jl] >= target:
            csum -= mass[jl]
            jl += 1
        if csum >= target and (best is None
                               or jr - jl < best[1] - best[0]):
            best = (jl, jr)
    return best


def profile(R, kb, m_idx):
    """n90 / width90 / tau_mean of K^(0)_{h,m} at one alias column
    (verbatim paircorr_contract profile, reduced to the three
    numbers Z4 needs)."""
    M, D, F, L = R["M"], R["D"], R["F"], R["L"]
    Ki = -0.5 * kb["chat"][1:, m_idx]        # K(iD), i = 1..M-1
    jl, jr = min_window(np.abs(Ki), FRAC_MASS)
    u_frac = ((jr - jl + 1) * D) / (2.0 * R["alpha"])
    aw = np.abs(kb["W"][1:, m_idx])
    o = np.argsort(-aw)
    cs = np.cumsum(aw[o])
    n90 = int(np.searchsorted(cs, FRAC_MASS * cs[-1]) + 1)
    tauv = 2.0 * math.pi * np.arange(1, F) / (L * D)
    tau_mean = float((aw @ tauv) / max(float(np.sum(aw)), 1e-300))
    return n90, float(u_frac), tau_mean


def loglog_slope(hs, ys):
    """Least-squares slope of log(y) vs log(h); None if unusable."""
    hs = [h for h, y in zip(hs, ys) if y > 0.0]
    yy = [y for y in ys if y > 0.0]
    if len(yy) < 2 or len(yy) < len(ys):
        return None
    return float(np.polyfit(np.log(hs), np.log(yy), 1)[0])


def main():
    section("PRIME.CASE.INNERLINEAR.01 -- the inner-zone linear "
            "route of the diagonal half (EXPLORATION ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s"
          % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
    print("    NO RH claim; no marker moves.")

    print("\nS0 -- firewall + self-tests")
    check("S0.1 AST firewall clean", not ast_scan(BANNED_IDS),
          kill="PIPELINE")

    section("B0 -- rungs (geometry, zone aliases, deep half)")
    RG = {}
    for kz in RUNGS:
        R = build_rung(kz)
        RG[kz] = R
        print("    kz %-3d h %4d F %5d: atoms %5d, X %.3e, zone "
              "aliases %3d (a <= h^1.4 = %8.0f)"
              % (kz, R["h"], R["F"], len(R["uu"]), R["X"],
                 len(R["al_f"]), R["h"] ** 1.4), flush=True)
    order = sorted(RUNGS, key=lambda kz: (RG[kz]["h"], kz))
    deep = tuple(order[len(order) // 2:])
    print("    deep half (4 highest-h rungs): kz %s"
          % ", ".join(str(kz) for kz in deep))
    ok_al = all(len(RG[kz]["al_f"]) > 0 for kz in RUNGS)
    check("B0.1 zone alias sets nonempty on every rung", ok_al,
          kill="PIPELINE")
    if not ok_al:
        return finish({})

    # S0.2 endpoint reconstruction vs verbatim folded route (kz 9)
    R9 = RG[9]
    dev_end = 0.0
    for tv in (0.0, 1.0):
        dv = R9["d0"] if tv == 0.0 else R9["d1"]
        d_full = np.concatenate([dv, dv[-2:0:-1]])
        xs, ws, _uf = folded_measure(d_full, R9["L"], +1.0)
        ys, vs, uf_n = folded_measure(d_full, R9["L"], -1.0)
        al, be, m0, steps = lanczos_chain(xs, ws, R9["h"] + 1)
        if steps < R9["h"] + 1:
            check("S0.2 endpoint chain (verbatim route)", False,
                  kill="PIPELINE")
            return finish({})
        Pn = eval_chain(al, be, m0, R9["y_al"], R9["h"])
        lam_ref = 1.0 / np.sum(Pn ** 2, axis=1)
        pos_map = {int(f): float(v) for f, v in zip(uf_n, vs)}
        nu_ref = np.array([pos_map.get(int(f), 0.0)
                           for f in R9["al_f"]])
        e = eval_state(R9, dv, R9["r"], R9["al_f"], need_J=False)
        if e is None:
            check("S0.2 endpoint chain (qt route)", False,
                  kill="PIPELINE")
            return finish({})
        dev_end = max(dev_end, float(np.max(
            np.abs(e["lam"] / lam_ref - 1.0))))
        dev_end = max(dev_end, float(np.max(
            np.abs(e["nu"] - nu_ref)
            / np.maximum(np.abs(nu_ref), 1e-300))))
    check("S0.2 endpoint reconstruction == verbatim folded route "
          "(kz 9, t = 0 and 1)", dev_end <= TOL_SELF_END,
          "rel sup dev %.2e" % dev_end, kill="PIPELINE")

    section("E -- endpoints, derivatives, margins + wards "
            "(verbatim round-51 quantities)")
    RES = {}
    ok_e = True
    qf_worst = 0.0
    wA_max = wB_max = 0.0
    for kz in order:
        R = RG[kz]
        t_a = time.time()
        e0 = eval_state(R, R["d0"], R["r"], R["al_f"], need_J=True,
                        qf=True)
        e1 = eval_state(R, R["d1"], R["r"], R["al_f"], need_J=True,
                        qf=True)
        if e0 is None or e1 is None:
            ok_e = False
            print("    kz %-3d: CHAIN SHORT at an endpoint" % kz)
            break
        qf_worst = max(qf_worst, e0["qf_dev"], e1["qf_dev"])
        kb0 = kernel_block(R, e0, R["d0"])
        kb1 = kernel_block(R, e1, R["d1"])
        wa0 = float(np.max(np.abs(e0["J"] - kb0["A_prime"])
                           / np.maximum(np.maximum(
                               np.abs(kb0["A_grid"]),
                               kb0["Sabs"]), 1e-300)))
        wa1 = float(np.max(np.abs(e1["J"] - kb1["A_prime"])
                           / np.maximum(np.maximum(
                               np.abs(kb1["A_grid"]),
                               kb1["Sabs"]), 1e-300)))
        wA_max = max(wA_max, wa0, wa1)
        wB_max = max(wB_max, kb0["ward2"], kb1["ward2"])
        deficit = -e0["G"]
        RES[kz] = dict(e0=e0, e1=e1, kb0=kb0, kb1=kb1,
                       deficit=deficit,
                       margin1=e1["J"] - deficit,
                       margin0=e0["J"] - deficit,
                       marginF=e1["G"])
        print("    kz %-3d h %4d (n_al %2d): F'(0) med %+.3e | "
              "F'(1) med %+.3e | deficit med %+.3e | W-A %.1e/"
              "%.1e W-B %.1e/%.1e  [%.1f s]"
              % (kz, R["h"], len(R["al_f"]),
                 float(np.median(e0["J"])),
                 float(np.median(e1["J"])),
                 float(np.median(deficit)), wa0, wa1,
                 kb0["ward2"], kb1["ward2"],
                 time.time() - t_a), flush=True)
    check("E0 endpoint chains complete on all rungs", ok_e,
          kill="PIPELINE")
    check("S0.3 quadratic-form self-test (sum w p*^2 == lambda, "
          "both endpoints, all rungs)", ok_e
          and qf_worst <= TOL_QF, "worst rel dev %.2e" % qf_worst,
          kill="PIPELINE")
    if not ok_e:
        return finish({})
    check("E.W-A prime-side regrouping == envelope F' at both "
          "endpoints (max rel %.2e <= %.0e)"
          % (wA_max, TOL_WARD_PRIME), wA_max <= TOL_WARD_PRIME,
          kill="WARD")
    check("E.W-B smooth subtraction route a == route b (max rel "
          "%.2e <= %.0e)" % (wB_max, TOL_WARD_K0),
          wB_max <= TOL_WARD_K0, kill="WARD")

    labels = {}

    # ------------------------------------------------------------ Z1
    section("Z1 -- THE INNER EXPONENT: census F'(1) >= deficit on "
            "{a <= h^(2 theta_in)}, theta_in in the frozen grid")
    elig = {}
    for th in INNER_GRID:
        rows = []
        deep_ok = True
        deep_h, deep_min, deep_mono = [], [], []
        for kz in order:
            R, res = RG[kz], RES[kz]
            sel = R["a_al"] <= R["h"] ** (2.0 * th)
            n_in = int(np.sum(sel))
            mg = res["margin1"][sel]
            npass = int(np.sum(mg >= 0.0)) if n_in else 0
            mn = float(np.min(mg)) if n_in else float("nan")
            rows.append((kz, R["h"], n_in, npass, mn))
            if kz in deep:
                if n_in == 0 or npass < n_in:
                    deep_ok = False
                deep_h.append(R["h"])
                deep_min.append(mn if n_in else float("nan"))
                deep_mono.append(bool(np.all(np.diff(mg) <= 0.0))
                                 if n_in >= 2 else None)
        trend = None
        if all(np.isfinite(v) and v > 0.0 for v in deep_min):
            trend = float(np.polyfit(np.log(deep_h),
                                     np.log(deep_min), 1)[0])
        ok = deep_ok and trend is not None and trend > 0.0
        elig[th] = ok
        print("\n    theta_in = %.3f  (inner cut a <= h^%.3f):"
              % (th, 2.0 * th))
        for kz, h, n_in, npass, mn in rows:
            tagd = " deep" if kz in deep else ""
            print("      kz %-3d h %4d: inner %2d cells, pass "
                  "%2d/%-2d, min margin %s%s"
                  % (kz, h, n_in, npass, n_in,
                     "%+.3e" % mn if np.isfinite(mn) else "  n/a ",
                     tagd))
        print("      deep half: 100%% pass %s | margin trend "
              "slope %s | ELIGIBLE %s"
              % ("YES" if deep_ok else "no",
                 "%+.3f" % trend if trend is not None else "n/a",
                 "YES" if ok else "no"), flush=True)
        if deep_ok:                       # v2 disclosed diagnostics
            tnorm = None
            if all(np.isfinite(v) and v > 0.0 for v in deep_min):
                tnorm = float(np.polyfit(
                    np.log(deep_h),
                    np.log(np.array(deep_h)
                           * np.array(deep_min)), 1)[0])
            print("      v2 diagnostics (measurement only, rule "
                  "untouched): normalized slope of log(h x min "
                  "margin) %s | within-rung margin1 monotone "
                  "along a (deep): %s"
                  % ("%+.3f" % tnorm if tnorm is not None
                     else "n/a",
                     " ".join(("yes" if m else "no")
                              if m is not None else "n/a"
                              for m in deep_mono)), flush=True)
    cand = [th for th in INNER_GRID if elig[th]]
    theta_in = max(cand) if cand else None
    if theta_in is not None:
        z1_label = "INNER-ZONE(theta_in*=%.3f)" % theta_in
        print("\n    FROZEN: theta_in* = %.3f -- the largest grid "
              "exponent with a 100%% deep-half linear census and a "
              "positive margin trend." % theta_in)
    else:
        z1_label = "INNER-EMPTY"
        print("\n    INNER-EMPTY: no grid theta_in is eligible -- "
              "the linear route covers no stable inner zone on the "
              "deep half (honest).")
    labels["TYPE"] = z1_label
    check("Z1.1 typed: %s (measurement)" % z1_label, True)
    th_use = theta_in if theta_in is not None else THETA_FALLBACK
    if theta_in is None:
        print("    Z2/Z3/Z4 run at the frozen fallback theta_in = "
              "%.3f, purely for the record (disclosed)."
              % THETA_FALLBACK)

    # ------------------------------------------------------------ Z2
    section("Z2 -- THE MIDDLE-BAND ACCOUNTING: cells with "
            "h^(2 x %.3f) < a <= h^1.4 under the FULL difference"
            % th_use)
    n_band_tot = 0
    hs_frac, fr_frac = [], []
    band_bad = 0
    for kz in order:
        R, res = RG[kz], RES[kz]
        band = R["a_al"] > R["h"] ** (2.0 * th_use)
        res["band"] = band
        n_zone = len(R["al_f"])
        n_band = int(np.sum(band))
        n_band_tot += n_band
        frac = n_band / n_zone
        hs_frac.append(R["h"])
        fr_frac.append(frac)
        if n_band == 0:
            print("    kz %-3d h %4d: band EMPTY (zone %d cells "
                  "all inner)" % (kz, R["h"], n_zone))
            continue
        mgF = res["marginF"][band]
        mg1 = res["margin1"][band]
        npass = int(np.sum(mgF >= 0.0))
        band_bad += n_band - npass
        print("    kz %-3d h %4d: band %2d/%2d cells (frac %.2f) | "
              "FULL margin: pass %2d/%-2d min %+.3e med %+.3e | "
              "linear margin min %+.3e"
              % (kz, R["h"], n_band, n_zone, frac, npass, n_band,
                 float(np.min(mgF)), float(np.median(mgF)),
                 float(np.min(mg1))))
        idx = np.nonzero(band)[0]
        show = list(idx[:SHOW_BAND])
        im = int(idx[np.argmin(mgF)])
        if im not in show:
            show.append(im)
        print("      %-4s %-5s %-9s %-11s %-11s %-11s"
              % ("m", "f", "a_m", "marginF", "margin1", "deficit"))
        for i in show:
            print("      %-4d %-5d %-9.1f %+.3e  %+.3e  %+.3e%s"
                  % (i + 1, int(R["al_f"][i]), float(R["a_al"][i]),
                     float(res["marginF"][i]),
                     float(res["margin1"][i]),
                     float(res["deficit"][i]),
                     "  <- min marginF" if i == im else ""),
                  flush=True)
    n_frac_pos = sum(1 for v in fr_frac if v > 0.0)
    slope = (loglog_slope(hs_frac, fr_frac)
             if n_frac_pos >= MIN_TREND_RUNGS else None)
    if slope is not None:
        band_trend = "SHRINKING" if slope < 0.0 else "NON-SHRINKING"
        print("\n    band fraction h-trend: log-log slope %+.3f "
              "-> %s with depth" % (slope, band_trend))
    else:
        band_trend = "n/a"
        print("\n    band fraction h-trend: n/a (%d rungs with a "
              "nonempty band, or empty-band rungs break the "
              "log fit -- disclosed)" % n_frac_pos)
    labels["BAND"] = "%d cells, %s" % (n_band_tot, band_trend)
    print("    band total: %d cells over the 8 rungs; FULL-margin "
          "failures in the band: %d (the nonlinear truth ledger)"
          % (n_band_tot, band_bad))
    check("Z2.1 band accounting recorded (measurement)", True)

    # ------------------------------------------------------------ Z3
    section("Z3 -- THE STABILITY LEMMA SHADOW: ||K^(1) - K^(0)|| / "
            "||K^(0)|| per inner-zone alias (deep half)")
    stab_max = 0.0
    gap_max_deep = 0.0
    for kz in deep:
        R, res = RG[kz], RES[kz]
        inner = ~res["band"]
        idx = np.nonzero(inner)[0]
        relv, corrv = [], []
        for i in idx:
            K0i = -0.5 * res["kb0"]["chat"][1:, i]
            K1i = -0.5 * res["kb1"]["chat"][1:, i]
            den = max(float(np.linalg.norm(K0i)), 1e-300)
            relv.append(float(np.linalg.norm(K1i - K0i)) / den)
            cd = max(float(np.linalg.norm(K0i)
                           * np.linalg.norm(K1i)), 1e-300)
            corrv.append(float((K0i @ K1i) / cd))
        relv = np.array(relv)
        corrv = np.array(corrv)
        stab_max = max(stab_max, float(np.max(relv)))
        gap = res["e0"]["J"][idx] - res["e1"]["J"][idx]
        gap_max_deep = max(gap_max_deep,
                           float(np.max(np.abs(gap))))
        n_pass0 = int(np.sum(res["margin0"][idx] >= 0.0))
        print("    kz %-3d h %4d: inner %d aliases | relK max %.3f "
              "med %.3f | corr min %+.4f | K^(0) census F'(0) >= "
              "deficit: %d/%d"
              % (kz, R["h"], len(idx), float(np.max(relv)),
                 float(np.median(relv)), float(np.min(corrv)),
                 n_pass0, len(idx)))
        show = list(range(min(SHOW_STAB, len(idx))))
        ix = int(np.argmax(relv))
        if ix not in show:
            show.append(ix)
        print("      %-4s %-5s %-9s %-7s %-8s %-11s %-11s"
              % ("m", "f", "a_m", "relK", "corr", "F'(0)-F'(1)",
                 "margin1"))
        for j in show:
            i = idx[j]
            print("      %-4d %-5d %-9.1f %-7.3f %+.4f  %+.3e  "
                  "%+.3e%s"
                  % (i + 1, int(R["al_f"][i]), float(R["a_al"][i]),
                     float(relv[j]), float(corrv[j]),
                     float(gap[j]), float(res["margin1"][i]),
                     "  <- max relK" if j == ix else ""),
                  flush=True)
    labels["STABILITY"] = "max inner relK %.3f (deep)" % stab_max
    print("\n    THE LINEAR-ROUTE THEOREM SKELETON (measured "
          "shadow filled in):")
    print("      IF   (i)  p_{1,m} ~ p_{0,m} + mask stability on "
          "the inner zone {a <= h^%.3f} at the measured level "
          "(kernel distance <= %.3f, deep half)," % (2.0 * th_use,
                                                     stab_max))
    print("           (ii) the ONE-SIDED linear bound  sum_n mu_n "
          "K^(0)_{h,m}(log n) - K0 >= deficit_m + stability-error "
          "there (measured transfer gap |F'(0) - F'(1)| <= %.3e "
          "on the deep inner cells)," % gap_max_deep)
    print("      THEN T_h <= 1 on the inner zone of the ladder; "
          "the pair-correlation input is needed only on the BAND "
          "h^%.3f < a <= h^1.4 -- the hard part is now a BAND, "
          "not the zone." % (2.0 * th_use))
    print("      (Circularity caveat verbatim round-51: K^(1) is "
          "truth-built; without (i) the census does not transfer "
          "to the PNT-computable K^(0).)")
    print("\n    THE BAND SIZE, honestly (deep half):")
    for kz in deep:
        R, res = RG[kz], RES[kz]
        band = res["band"]
        nu1 = res["e1"]["nu"]
        dfc = res["deficit"]
        fr_al = float(np.mean(band))
        s_nu = float(np.sum(nu1))
        s_df = float(np.sum(dfc))
        fr_nu = float(np.sum(nu1[band])) / max(s_nu, 1e-300)
        fr_df = float(np.sum(dfc[band])) / max(abs(s_df), 1e-300)
        print("      kz %-3d h %4d: alias fraction %.3f | nu_1-"
              "mass fraction %.3f | deficit fraction %.3f"
              % (kz, R["h"], fr_al, fr_nu, fr_df))
    check("Z3.1 stability profile + skeleton recorded "
          "(measurement)", True)

    # ------------------------------------------------------------ Z4
    section("Z4 -- THE CLASSICAL FORM: n90 / width90 / tau of the "
            "inner K^(0) kernels vs the band (all rungs)")
    softer_votes = []
    for kz in order:
        R, res = RG[kz], RES[kz]
        band = res["band"]
        idx_in = np.nonzero(~band)[0]
        idx_bd = np.nonzero(band)[0]
        prof = {}
        for i in np.concatenate([idx_in, idx_bd]):
            prof[int(i)] = profile(R, res["kb0"], int(i))
        print("    kz %-3d h %4d (2 alpha = %.2f): inner %d, band "
              "%d aliases" % (kz, R["h"], 2.0 * R["alpha"],
                              len(idx_in), len(idx_bd)))
        print("      %-6s %-4s %-5s %-9s %-5s %-7s %-6s"
              % ("set", "m", "f", "a_m", "n90", "u_frac", "tau"))
        for tag, ids, nshow in (("inner", idx_in, SHOW_IN),
                                ("band", idx_bd, SHOW_BAND)):
            for i in ids[:nshow]:
                n90, uf, tm = prof[int(i)]
                print("      %-6s %-4d %-5d %-9.1f %-5d %-7.3f "
                      "%-6.2f" % (tag, i + 1, int(R["al_f"][i]),
                                  float(R["a_al"][i]), n90, uf,
                                  tm))
            if len(ids) > nshow:
                print("      %-6s ... +%d more rows"
                      % (tag, len(ids) - nshow))
        if len(idx_in) and len(idx_bd):
            med = {}
            for tag, ids in (("in", idx_in), ("bd", idx_bd)):
                med[tag] = tuple(float(np.median(
                    [prof[int(i)][k] for i in ids]))
                    for k in range(3))
            softer = (med["in"][1] <= med["bd"][1]
                      and med["in"][2] <= med["bd"][2])
            softer_votes.append(softer)
            print("      medians: inner n90 %.0f u_frac %.3f tau "
                  "%.2f | band n90 %.0f u_frac %.3f tau %.2f -> "
                  "inner %s"
                  % (med["in"][0], med["in"][1], med["in"][2],
                     med["bd"][0], med["bd"][1], med["bd"][2],
                     "SOFTER" if softer else "not softer"),
                  flush=True)
        else:
            print("      medians: n/a (inner or band empty on "
                  "this rung)", flush=True)
    if len(softer_votes) >= 2:
        n_soft = sum(softer_votes)
        # strict majority per the frozen rule
        cls = ("INNER-SOFTER" if n_soft * 2 > len(softer_votes)
               else "INNER-NOT-SOFTER")
        print("\n    reading: inner kernels softer on %d/%d "
              "comparable rungs -> %s (a %s classical hypothesis "
              "on the inner zone than on the band)"
              % (n_soft, len(softer_votes), cls,
                 "potentially WEAKER" if cls == "INNER-SOFTER"
                 else "NOT visibly weaker"))
    else:
        cls = "n/a"
        print("\n    reading: fewer than 2 comparable rungs -> "
              "CLASSICAL=n/a (disclosed)")
    labels["CLASSICAL"] = cls
    check("Z4.1 classical-form profiles recorded: %s "
          "(measurement)" % cls, True)

    # ------------------------------------------------------------ C
    section("C -- controls (kz 9, scramble seed %d, theta_ctrl = "
            "%.3f frozen)" % (SCRAMBLE_SEED, THETA_CTRL))
    rng = np.random.default_rng(SCRAMBLE_SEED)
    us = np.sort(rng.uniform(0.0, 2.0 * R9["alpha"],
                             size=len(R9["uu"])))
    c_s = np.asarray(core.atom_lags_at(R9["alpha"], R9["M"], us,
                                       R9["mm"])[0], float)
    d_s = grid_density(R9["c_ar"] + c_s)[:R9["F"]]
    r_s = d_s - R9["d0"]
    ff9 = np.arange(R9["F"])
    neg_s = ff9[(ff9 >= 1) & (d_s < 0.0)]
    neg_s = neg_s[np.argsort(R9["a"][neg_s], kind="stable")]
    al_inner = neg_s[R9["a"][neg_s]
                     <= R9["h"] ** (2.0 * THETA_CTRL)]
    fell_back = len(al_inner) == 0
    al_use = al_inner if not fell_back else neg_s[:CTRL_FALLBACK_AL]
    es = eval_state(R9, d_s, r_s, al_use, need_J=True)
    e0s = eval_state(R9, R9["d0"], r_s, al_use, need_J=False)
    if es is None or e0s is None:
        check("C0 scramble chains complete", False,
              kill="PIPELINE")
        return finish(labels)
    mg_s = es["J"] - (-e0s["G"])
    worst = float(np.min(mg_s))
    fires = worst < 0.0
    sel9 = RG[9]["a_al"] <= R9["h"] ** (2.0 * THETA_CTRL)
    real9 = (float(np.min(RES[9]["margin1"][sel9]))
             if np.any(sel9) else float("nan"))
    print("    scramble inner aliases: %d%s | min (F'_scr(1) - "
          "deficit_scr) = %+.3e (real kz 9 inner min margin1 "
          "%+.3e) -> %s"
          % (len(al_use),
             " (inner empty -> frozen fallback: %d a-closest neg "
             "nodes)" % CTRL_FALLBACK_AL if fell_back else
             " (inner zone)",
             worst, real9, "FIRES" if fires else "SILENT"),
          flush=True)
    check("C1 value control fires (scramble breaks the inner "
          "linear census)", fires, kill="CONTROL")

    return finish(labels)


def finish(labels):
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
        VERDICT = "INNERLINEAR-MEASURED"
    sub = ["%s=%s" % (k, labels[k]) for k in
           ("TYPE", "BAND", "STABILITY", "CLASSICAL")
           if k in labels]
    print("\n  VERDICT: %s%s"
          % (VERDICT, (" (%s)" % "; ".join(sub)) if sub else ""))
    if VERDICT == "INNERLINEAR-MEASURED" and "TYPE" in labels:
        if labels["TYPE"].startswith("INNER-ZONE"):
            print("  PLAIN ANSWER: YES on the finite shadow -- an "
                  "inner zone exists on which the LINEAR endpoint "
                  "route covers the deep half with growing "
                  "margins; the genuinely hard (pair-correlation) "
                  "part contracts to the printed middle BAND, "
                  "modulo the p1 ~ p0 stability lemma whose "
                  "measured shadow Z3 prints.")
        else:
            print("  PLAIN ANSWER: NO -- no grid inner exponent "
                  "gives a stable 100% deep-half linear census; "
                  "the pair-correlation input stands on the whole "
                  "zone.")
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
    ('paircorr_contract_probe', _SRC_0, 11, (), 'PAIRCONTRACT-EXTRACTED', 0),
    ('endpoint_bracket_probe', _SRC_1, 13, (), 'ENDPOINT-MEASURED', 0),
    ('inner_zone_linear_probe', _SRC_2, 12, (), 'INNERLINEAR-MEASURED', 0),
)


def run():
    t0 = time.time()
    print("=" * 74)
    print('v894 -- PRIME.CASE.PAIRCORR.CONTRACT.01 + PRIME.CASE.ENDPOINT.01 + PRIME.CASE.INNERLINEAR.01: the conditional diagonal contract made concrete -- the exact prime-pair kernel, the one-sided endpoint bracket, and the inner-zone accounting (route stays CONDITIONAL per v889)')
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
    print("v894: %d/%d pattern gates passed | runtime %.1f s"
          % (sum(gates), len(gates), time.time() - t0))
    print('the diagonal condition is localized, not removed: exact frozen kernel, deep endpoint bracket, and a measured non-shrinking hard band -- pair-correlation class input still required')
    print("[%s] v894 VERDICT GATE" % ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(run())
