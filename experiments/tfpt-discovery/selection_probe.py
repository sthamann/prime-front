#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""selection_probe -- PRIME.CCM.SELECTION.01

FROZEN SPEC (2026-08-16).  EXPLORATION ONLY.  This probe writes no
verification module, paper, ledger, website, manifest, Lean file or
status marker.  It makes NO RH claim, NO positivity claim, NO
counterexample claim.  It closes no gate and narrows no gate.

=======================================================================
MISSION
=======================================================================
Round 124 (cluster_mixing_probe, verdict KMIX-OBSTRUCTED(selection-
only)) distilled the CCM omega into a SELECTION obstruction: the true
Weil ground state xi_lambda (= v_0 of the even-sector Weil matrix
Q_lambda) sits inside the Connes-degenerate band-zero annihilator
cluster, and the Rayleigh/energy selector needs to resolve the doublet
gap ~ e^{-c lambda^2} to pick it.  But selection != energy resolution:
this probe builds and adjudicates a ZOO of source-only selector
candidates S (operators/functionals built ONLY from Lambda(n), Gamma,
pi, prolate/Legendre, frame data -- no zero ordinate anywhere outside
ward_/screen namespaces) and asks, per candidate:
  (1) does S SPLIT the cluster (doublet split + full-cluster split)?
  (2) is its v_0 branch STABLE and ALIGNED (orientation frozen on the
      gate rungs x = 5, 8; deep rungs x = 13, 18 are out-of-sample)?
  (3) what is the split's decay law vs lambda (poly / e^{-c lambda} /
      Connes e^{-c lambda^2})?
  (4) what accuracy floor does it reach (error angle phi vs the
      round-122/124 mixing number beta = the k-hat selector's floor)?
  (5) screens: does it secretly transcribe zeros (Z1), reconstruct the
      de Branges/canonical completion norm (r121 disguise), or
      relocate the problem into inverse-Connes conditioning?

THE EXACT TRADE-OFF LAW (the no-go skeleton, machine-gated):  for ANY
symmetric selector S with doublet elements s00 = <v0,S v0>, s01 =
<v0,S v1>, s11 = <v1,S v1>:
  (i)   the S-eigenbasis is rotated from the (v0,v1) truth basis by
        phi with tan(2 phi) = 2 s01/(s00 - s11)  (exact 2x2 algebra,
        G10) -- the achievable selection accuracy is phi ~= |s01| /
        split and the certification cost is ~ log(1/split) digits;
  (ii)  (E0 - E1) s01 = <v0, [Q, S] v1>  (exact commutator identity,
        G11): the doublet off-diagonal of ANY selector is its
        Q-commutator matrix element AMPLIFIED BY 1/gap -- selection to
        accuracy delta with split g requires a commutator element
        <= delta * g * gap, i.e. AT the Connes scale;
  (iii) BLOCK-COLLAPSE (exact, G12 + G31): Q = Mpole + March - Mprime
        and Q diagonal on the doublet imply s01(Mprime) ==
        s01(Mpole + March) exactly and split(Mprime) = split(arch
        block) - gap: the ARITHMETIC block selects exactly as its
        ARCHIMEDEAN complement beyond the Connes scale -- the prime
        side carries NO extra selection information on the doublet;
  (iv)  POLY-FILTER NO-GO (proven, cited): for p a real polynomial of
        degree d with |p| <= 1 on the spectral hull [m, M], Markov's
        inequality (A. A. Markov 1889) gives |p'| <= 2 d^2/(M - m), so
        the doublet split of p(Q) obeys split <= 2 d^2 gap/(M - m):
        amplifying the Connes gap e^{-c lambda^2} to a target split s
        needs degree d >= sqrt(s (M-m)/(2 gap)) ~ e^{c lambda^2 / 2}
        -- EXPONENTIAL COST for the whole f(Q) class (Krylov /
        Chebyshev / power filters; the round-124 S_KRY uselessness in
        theorem form).  Sharpness instance (Chebyshev T_3, equality at
        the endpoint) gated exactly in sympy (G13).

=======================================================================
LADDERS AND FROZEN NUMERICS
=======================================================================
MAIN even cells (KFAC 1.25, round-122 builder R4.build_cell, want_mp):
  RUNGS = ((5, 60), (8, 80), (13, 120), (18, 160)).
GATE_RUNGS = (5, 8) (orientation freezing); DEEP2 = (13, 18)
(out-of-sample adjudication).  Enriched frame KFAC 2.00 at x = 5, 8
(selector floors at the matched enriched frame; the deep enriched
builds are cited from round 124, not rebuilt).  Worlds: SMOOTH /
SCRARITH / EPSTEIN x = 8, EPSTEIN x = 13 (all want_mp).  Candidate
k_lambda via R4.prolate_kvec (NGRID 20001) -- the round-122 object
bit-for-bit.  SOFT_BAR = 1e-2 (cluster definition).  All mp work
under explicit mp.workdps at the cell dps (round-118/120 unary-
negation lesson); templates are FROZEN f64 unit vectors (their mp
lifts via repr are exact, so doublet elements are noise-free).
Deterministic: no RNG anywhere.  Sign conventions as round 124:
v0 fixed by <v0,k> > 0, all other cluster vectors by largest-|entry|
positive.

ROUND-124 REGRESSION PINS (run2 log, run of record):
  eps:  x5 1.6065833e-16, x8 3.7726342e-30, x13 2.4990356e-54,
        x18 5.2197362e-79
  gap:  x5 3.5754401e-11, x8 3.7542422e-24, x13 2.6537408e-47,
        x18 1.6962473e-71
  beta: x5 +1.848362e-3, x8 +3.569411e-3, x13 +2.522642e-3,
        x18 +1.878721e-3   (bar 2e-2 rel)
  nsoft: 3 / 5 / 10 / 15
  mode-scan |<v1, E(phi_8)-hat>|: 0.9953 / 0.9867 / 0.9727 / 0.9602
  mode-scan |<v0, E(phi_4)-hat>|: 0.985 / 0.966 / 0.936 / 0.910
  (bar 2e-2 abs on the mode pins)
Connes reference slope: OLS log10(gap) vs x over the pins ~ -4.66.

=======================================================================
THE SELECTOR ZOO (14 members; class tag in brackets)
=======================================================================
Rank-1 / template selectors (S = t t^T, t a frozen f64 unit vector):
  S_K     [ARCH]  t = k-hat, the CCM prolate candidate (R4 recipe).
  S_E4    [ARCH]  t = E(phi_4)-hat, the n = 4 prolate-mode Poisson
                  lift (v0's dominant mode per round 124).
  S_DC    [FRAME] t = delta_0 (the DC / integral functional: the
                  z = 0 evaluation vector is exactly the first
                  coordinate direction in this basis).
  S_GAUSS [FRAME] t = projection of exp(-8 v^2/a^2) (positive cone
                  template).
  S_TOP   [FRAME] t = delta_{K-1} (band-edge coefficient functional).
  S_BEV   [FRAME] t = e_z at real z = (K - 1/2) pi / a (band-EDGE
                  evaluation, generic off-lattice point).
  S_KLAM  [ARITH] t = k_Lambda-hat = sum_{q <= x} (Lambda(q)/sqrt q)
                  (shift_{+log q} + shift_{-log q}) k  (round-124
                  S_LAM vector).
Rank-2:
  S_EU    [FRAME] e_z at the Euler point z = 2.5 - 1.2i (Re s > 1;
                  round-122 Z_EULER[2]), real + imaginary parts.
                  (The originally drafted point -0.9i sits on the
                  imaginary axis where even real entire functions
                  are real, so its imaginary part is the exact zero
                  vector -- found and repaired pre-freeze, smoke
                  disclosure (ii).)
Weighted-frame operator:
  S_NUM   [ARCH]  sum_{n=0..15} n * e-hat_n e-hat_n^T (prolate-lift
                  NUMBER operator; the doublet-label candidate:
                  v0 ~ n = 4 content, v1 ~ n = 8 content).
Matrix selectors:
  S_FREQ  [FRAME] diag((omega_k/omega_max)^2): the dilation-
                  generator-squared compressed to the even sector.
  S_PAR   [FRAME] diag((-1)^k): the half-period translation
                  involution (discrete symmetry candidate).
  S_POS2  [FRAME] multiplication by v^2 on [-a, a] in the cos basis
                  (closed form; localization selector -- v0 is
                  inner-localized, v1 delocalized per round 124).
  S_ARCHOP[ARCH]  Mpole + March (the archimedean Q-block).
  S_PRIME [ARITH] Mprime (the arithmetic Q-block; tied to S_ARCHOP by
                  the exact BLOCK-COLLAPSE identity).
COMPARATORS (typed, not zoo): S_E8 (anti-selector, targets v1),
S_ORACLE (v0 v0^T, instrument sanity: phi = 0, split_rel = 1),
S_ZAB*ward (above-band zero-evaluation Gram, the de Branges
canonical-norm proxy = the DISGUISE REFERENCE, ward namespace),
POLY-FILTER class (analytic, Markov).  The in-band zero Gram acts as
~0 on the cluster (annihilator law, gated) -- the zero-transcription
class is dead on arrival at the cluster.

ORIENTATION PROTOCOL (frozen): at the gate rungs x = 5 and 8 each
selector's v0 branch is identified on the doublet (MAX or MIN
eigenvalue; the doublet error angle phi is the PRINCIPAL angle of
the v0-nearest S-eigenvector, |phi| <= pi/4, and the branch is
MAX iff s00 > s11 -- exact 2x2 fact) and on the cluster (TOP / BOT /
MID rank).  If the two gate rungs disagree the selector is typed
SEL-UNSTABLE and excluded from adjudication.  The frozen branch is
applied unchanged at x = 13, 18; achieved overlap there is
out-of-sample.

READS per selector per rung: doublet (s00, s01, s11) in mp; split =
sqrt((s00-s11)^2 + 4 s01^2); error angle phi (exact 2x2); identity
residual of (ii); cluster compression (dim nsoft+1) eigendecomposition
with rank of the v0 branch, achieved overlap ov0, split_rel = (chosen
eigenvalue's isolation)/(cluster spread); f64 PIPELINE: the same
selection run entirely at f64 spectral cost (np.linalg.eigh cluster
basis of the f64 matrix copy + f64 compression), overlap vs the mp
truth -- the cost demonstration (matrix ASSEMBLY precision is
polynomial and not part of the claim; typed).

BARS (frozen; calibrated only on round-124 record + the disclosed
smoke): SPLIT_BAR = 0.05 (split_rel at both deep rungs); ALIGN_BAR =
0.30 rad; BEATS-BETA iff phi_achieved <= |beta(x)|/2 at both deep
rungs; RATE bands on rho = slope(log10 split_rel vs x)/slope(log10
gap vs x): CONNES-RIDING rho >= 0.70, FREE rho <= 0.30, else MID;
DISGUISE_CORR = 0.95 (traceless Frobenius correlation vs the
above-band canonical Gram); annihilator gate max in-band
|<e_gamma, v_0/v_1>| <= 1e-3 (x=5) / 1e-6 (x>=8) on the DOUBLET (the
selection target; the shallow cluster edge at gap ~1e-2 is energy-
resolvable and excluded -- smoke disclosure (iii); the smoke-only
x=3 rung, whose 'doublet partner' IS the shallow edge, gets 1e-1);
f64 pipeline hard
gate: ov(S_K, f64) >= 1 - 1e-4 at x = 13 and 18; conditioning gate
(x = 5, 8): measured selector-error response to a delta-perturbation
of Q[j*,j*] within [1/3, 3] of the doublet law theta = delta
|v0_j v1_j| alpha / gap and strictly nonzero (round-118 red flag);
block identity bars 10^(-dps/3); v^2 closed form vs 40001-grid
quadrature <= 1e-6 rel; eigen-residuals <= 10^(-dps/2); runtime bar
7200 s.

VERDICT ENUMS (frozen): per selector SEL-{SPLITS+ALIGNED, SPLITS-
MISALIGNED, NOSPLIT, UNSTABLE}; RATE-{FREE, MID, CONNES}(rho);
SCREEN-{CLEAN, DB-DISGUISE}; BEATS-BETA(yes/no).  Composite:
SELECTION-SOLVED (exists SPLITS+ALIGNED+CLEAN+FREE+BEATS-BETA at both
deep rungs) / SELECTION-SECTOR-ONLY (exists SPLITS+ALIGNED+CLEAN+FREE
but no BEATS-BETA: selection to the beta floor is poly-cost, sub-beta
selection remains Connes-priced) / SELECTION-NOGO-MEASURED (no
selector SPLITS+ALIGNED).  Always stated: POLYFILTER-NOGO-PROVEN
(cited Markov), BLOCK-COLLAPSE-EXACT, TRADEOFF-IDENTITY-EXACT,
ANNIHILATOR-ZERO-CLASS.  MINCUT (round-116 replica + round-122
extension, flows 4/5 expected, census {MEAS, OMEGA-POS} cardinality 4
expected unchanged; the selection outcome is MEAS data on the
LANEACONV omega edge).

SMOKE DISCLOSURE (pre-freeze, two smokes at x = (3, 5), ~5 s each,
scratch logs deleted; THREE instrument findings, all repaired
PRE-FREEZE): (i) the G13 draft expected T_3'(-1) = -9, but the
Chebyshev derivative 12z^2 - 3 is EVEN (= +9 at both endpoints) --
spec-side arithmetic slip, fixed; (ii) the drafted Euler point
z = -0.9i lies on the imaginary axis where the even real entire
B_k are real, so the imaginary-part template was the exact zero
vector (NaN propagated into eigsy) -- point moved to the round-122
Z_EULER[2] = 2.5 - 1.2i; (iii) the annihilator gate as drafted
bound the FULL cluster, but the shallow cluster edge (gap ~ 1e-2,
in-band evaluation measured 2.0e-2 at x = 5) is not part of the
degenerate selection target -- gate restricted to the doublet
(x = 5 doublet measured 1.3e-7, bar 1e-3 kept; full-cluster max
still printed).  Smoke calibrations: v^2 closed-form ward 2.7e-8
(bar 1e-6); block-identity residual 0.0 / 5.7e-62 at x = 5 (bar
10^-(dps/3) comfortable); S_ORACLE exact (phi -1.4e-17, ov0 1.0);
S_K doublet phi == beta (1.848e-3 at x = 5) exactly as the rank-1
algebra predicts; mode-scan pins reproduced (0.9953/0.9851).
Pre-freeze observations disclosed for honesty (smoke, x = 5 only,
NOT out-of-sample): S_GAUSS read phi = 5.8e-3 and S_E4 phi =
8.4e-2 at x = 5; no bar or rule was tuned to favor or disfavor
them -- the deep rungs adjudicate.  Amendments after the frozen
run, if any, are appended as numbered AMENDMENT blocks.

AST FIREWALL: no zetazero/siegelz/siegeltheta/nzeros/grampoint
anywhere; no zeta anywhere in this probe; np.load only inside ward_
functions; no import of verification/.  Zero cache
verified_zeros_n7000.npy READ-ONLY in ward_ namespace (X5:
instrument/comparator/screen, never construction).
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

import radius4_an_probe as R4          # round-122 pipeline (verbatim)
import blockreal_lemma_probe as BR     # round-114 machinery
import semilocal_realroot_limit_probe as SL  # ward builder
import cluster_mixing_probe as CM      # round-124 machinery (verbatim)

# ---------------------------------------------------------------- frozen
KFAC1 = 1.25
KFAC_ENR = 2.00
RUNGS = ((5, 60), (8, 80), (13, 120), (18, 160))
GATE_RUNGS = (5, 8)
DEEP2 = (13, 18)
ENR_RUNGS = ((5, 60), (8, 80))
WORLD_R = (("SMOOTH", 8, 80), ("SCRARITH", 8, 80), ("EPSTEIN", 8, 80),
           ("EPSTEIN", 13, 120))
SOFT_BAR = 1e-2
NGRID = 20001
MODE_N = 16
ZAB_N = 40
Z_EU = (2.5, -1.2)

R124_EPS = {5: 1.6065833e-16, 8: 3.7726342e-30, 13: 2.4990356e-54,
            18: 5.2197362e-79}
R124_GAP = {5: 3.5754401e-11, 8: 3.7542422e-24, 13: 2.6537408e-47,
            18: 1.6962473e-71}
R124_BETA = {5: 1.848362e-3, 8: 3.569411e-3, 13: 2.522642e-3,
             18: 1.878721e-3}
R124_NSOFT = {5: 3, 8: 5, 13: 10, 18: 15}
R124_V1E8 = {5: 0.9953, 8: 0.9867, 13: 0.9727, 18: 0.9602}
R124_V0E4 = {5: 0.985, 8: 0.966, 13: 0.936, 18: 0.910}
REG_BAR = 2e-2
MODE_PIN_BAR = 2e-2

SPLIT_BAR = 0.05
ALIGN_BAR = 0.30
BEATS_BETA_FAC = 0.5
RATE_FREE, RATE_CONNES = 0.30, 0.70
DISGUISE_CORR = 0.95
ANNIH_BAR_X5 = 1e-3
ANNIH_BAR_DEEP = 1e-6
F64_SK_BAR = 1e-4
COND_RATIO = (1.0 / 3.0, 3.0)
PERT_THETA_TGT = 1e-6
V2_WARD_BAR = 1e-6
RUNTIME_BAR = 7200.0
GAMMA1_LIT = 14.134725141734693790   # ward only

ZOO = ("S_K", "S_E4", "S_NUM", "S_KLAM", "S_EU", "S_DC", "S_GAUSS",
       "S_TOP", "S_BEV", "S_FREQ", "S_PAR", "S_POS2", "S_ARCHOP",
       "S_PRIME")
CLASS_TAG = {"S_K": "ARCH", "S_E4": "ARCH", "S_NUM": "ARCH",
             "S_KLAM": "ARITH", "S_EU": "FRAME", "S_DC": "FRAME",
             "S_GAUSS": "FRAME", "S_TOP": "FRAME", "S_BEV": "FRAME",
             "S_FREQ": "FRAME", "S_PAR": "FRAME", "S_POS2": "FRAME",
             "S_ARCHOP": "ARCH", "S_PRIME": "ARITH",
             "S_E8": "ARCH*anti", "S_ORACLE": "*oracle",
             "S_ZAB": "*ward"}

SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
T0_WALL = time.time()
CACHE_N7000 = os.path.join(HERE, "verified_zeros_n7000.npy")

CHECKS: list[tuple[str, bool, str]] = []
INFO: list[str] = []


def check(name: str, ok: bool, detail: str) -> bool:
    ok = bool(ok)
    CHECKS.append((name, ok, detail))
    print("  [%s] %-38s %s" % ("PASS" if ok else "FAIL", name, detail),
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
            "n" + "zeros", "gram" + "point", "zeta"}
    bad = []
    for node in ast.walk(tree):
        nm = None
        if isinstance(node, ast.Attribute):
            nm = node.attr
        elif isinstance(node, ast.Name):
            nm = node.id
        if nm is None:
            continue
        if nm.lower() in forb:
            bad.append("forbidden %s @%d" % (nm, node.lineno))
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
                       "no zero-oracle, no zeta anywhere, cache in ward_")


# --------------------------------------------------------------- wards
def ward_cache() -> np.ndarray:
    return np.asarray(np.load(CACHE_N7000), float)


def ward_band_split(gam: np.ndarray, edge: float,
                    nab: int) -> tuple[np.ndarray, np.ndarray]:
    """(in-band gammas, first nab above-band gammas).  WARD ONLY."""
    inb = gam[gam <= edge]
    abv = gam[gam > edge][:nab]
    return inb, abv


def ward_evec_gamma(cell: dict, g: float) -> np.ndarray:
    """Zero-evaluation vector at cache ordinate g (WARD/screen only)."""
    with mp.workdps(cell["dps"]):
        ez = R4.evec_euler(complex(float(g), 0.0), cell["om"],
                           cell["a"], cell["K"])
        return np.array([float(mp.re(t)) for t in ez])


# --------------------------------------------------- source machinery
def evec_real_f64(cell: dict, z: float) -> np.ndarray:
    """Evaluation vector at REAL source point z (frame data, no zero
    ordinate).  Returned as frozen f64."""
    with mp.workdps(cell["dps"]):
        ez = R4.evec_euler(complex(z, 0.0), cell["om"], cell["a"],
                           cell["K"])
        return np.array([float(mp.re(t)) for t in ez])


def evec_cplx_f64(cell: dict, zr: float, zi: float) -> tuple:
    with mp.workdps(cell["dps"]):
        ez = R4.evec_euler(complex(zr, zi), cell["om"], cell["a"],
                           cell["K"])
        return (np.array([float(mp.re(t)) for t in ez]),
                np.array([float(mp.im(t)) for t in ez]))


def unit(v: np.ndarray) -> np.ndarray:
    n = float(np.linalg.norm(v))
    if n < 1e-300:
        raise ValueError("zero template vector (illegal selector)")
    return v / n


def v2_matrix(cell: dict) -> np.ndarray:
    """Multiplication by v^2 on [-a,a] in the normalized cos basis
    (exact closed form; frozen f64)."""
    a = cell["a"]
    K = cell["K"]
    M = np.zeros((K, K))
    M[0, 0] = a * a / 3.0
    for k in range(1, K):
        M[0, k] = M[k, 0] = (2.0 * math.sqrt(2.0) * a * a
                             * (-1.0) ** k / (k * k * math.pi ** 2))
        M[k, k] = a * a / 3.0 + a * a / (2.0 * k * k * math.pi ** 2)
        for j in range(1, k):
            d, s = k - j, k + j
            M[k, j] = M[j, k] = (2.0 * a * a / math.pi ** 2
                                 * (-1.0) ** d
                                 * (1.0 / (d * d) + 1.0 / (s * s)))
    return M


def build_templates(cell: dict, x: int) -> dict:
    """All frozen f64 template vectors + the S_NUM term list."""
    L = cell["a"]
    K = cell["K"]
    vg = np.linspace(-L, L, NGRID)
    kd = CM.kfun_data(x)
    pro = kd["pro"]
    out: dict = {}
    out["kd"] = kd
    # prolate-lift modes e-hat_n
    ehat = []
    for n in range(MODE_N):
        en = CM.esum_on_grid(lambda xx, n=n: pro.eval_mode(n, xx),
                             vg, int(x) + 2, pro.lam)
        pe = CM.project_cell(en, vg, cell)
        npe = float(np.linalg.norm(pe))
        ehat.append(pe / npe if npe > 0 else pe)
    out["ehat"] = ehat
    # Gaussian positive template
    gsp = CM.project_cell(np.exp(-8.0 * vg * vg / (L * L)), vg, cell)
    out["t_gauss"] = unit(gsp)
    # coordinate templates
    tdc = np.zeros(K)
    tdc[0] = 1.0
    out["t_dc"] = tdc
    ttop = np.zeros(K)
    ttop[K - 1] = 1.0
    out["t_top"] = ttop
    # band-edge evaluation (generic half-integer point)
    out["t_bev"] = unit(evec_real_f64(cell, (K - 0.5) * math.pi / L))
    # Euler-point evaluation (rank 2)
    er, ei = evec_cplx_f64(cell, Z_EU[0], Z_EU[1])
    out["t_eu"] = (unit(er), unit(ei))
    # Lambda-shift templates
    sh = {}
    for p in (2, 3):
        s = (CM.k_vals_on(kd, vg - math.log(p), int(x) * p + 2)
             + CM.k_vals_on(kd, vg + math.log(p), int(x) + 2))
        sh[p] = unit(CM.project_cell(s, vg, cell))
    out["t_sh"] = sh
    klam = np.zeros_like(vg)
    for q, lq in CM.prime_power_atoms(x):
        klam = klam + (lq / math.sqrt(q)) * (
            CM.k_vals_on(kd, vg - math.log(q), int(x) * q + 2)
            + CM.k_vals_on(kd, vg + math.log(q), int(x) + 2))
    out["t_klam"] = unit(CM.project_cell(klam, vg, cell))
    return out


def selector_specs(cell: dict, tp: dict, kt: np.ndarray) -> dict:
    """name -> ('terms', [(w, vec_f64)]) or ('mat64', M) or
    ('mpblock', key or tuple of keys)."""
    K = cell["K"]
    om = cell["om"]
    sp: dict = {}
    sp["S_K"] = ("terms", [(1.0, kt)])
    sp["S_E4"] = ("terms", [(1.0, tp["ehat"][4])])
    sp["S_NUM"] = ("terms", [(float(n) / (MODE_N - 1.0), tp["ehat"][n])
                             for n in range(1, MODE_N)])
    sp["S_KLAM"] = ("terms", [(1.0, tp["t_klam"])])
    sp["S_EU"] = ("terms", [(1.0, tp["t_eu"][0]),
                            (1.0, tp["t_eu"][1])])
    sp["S_DC"] = ("terms", [(1.0, tp["t_dc"])])
    sp["S_GAUSS"] = ("terms", [(1.0, tp["t_gauss"])])
    sp["S_TOP"] = ("terms", [(1.0, tp["t_top"])])
    sp["S_BEV"] = ("terms", [(1.0, tp["t_bev"])])
    sp["S_FREQ"] = ("mat64", np.diag((om / om[K - 1]) ** 2))
    sp["S_PAR"] = ("mat64", np.diag(np.array(
        [(-1.0) ** k for k in range(K)])))
    sp["S_POS2"] = ("mat64", v2_matrix(cell))
    sp["S_ARCHOP"] = ("mpblock", ("mpPole", "mpArch"))
    sp["S_PRIME"] = ("mpblock", ("mpPrime",))
    # comparators
    sp["S_E8"] = ("terms", [(1.0, tp["ehat"][8])])
    return sp


def spec_f64_matrix(cell: dict, kind: str, payload) -> np.ndarray:
    K = cell["K"]
    if kind == "terms":
        M = np.zeros((K, K))
        for w, v in payload:
            M += w * np.outer(v, v)
        return M
    if kind == "mat64":
        return payload
    blocks = {"mpPole": cell["blk_pole"], "mpArch": cell["blk_arch"],
              "mpPrime": cell["blk_prime"]}
    M = np.zeros((K, K))
    for key in payload:
        M += blocks[key]
    return M


# ------------------------------------------------------------ mp core
def cluster_basis_mp(cell: dict, kt: np.ndarray) -> dict:
    """mp cluster eigenbasis (sign-fixed as round 124) + spectra."""
    K = cell["K"]
    out: dict = {}
    with mp.workdps(cell["dps"]):
        E, V = cell["mpE"], cell["mpV"]
        eps = E[0]
        soft = [0] + [i for i in range(1, K)
                      if E[i] - eps <= mp.mpf(repr(SOFT_BAR))]
        kv = CM.lift_vec(kt)
        vecs = []
        for i in soft:
            vi = R4.matcol(V, i, K)
            if i == 0:
                if R4.mp_dot(vi, kv) < 0:
                    vi = [-t for t in vi]
            else:
                vi = CM.sign_fix(vi)
            vecs.append(vi)
        out["soft"] = soft
        out["vecs"] = vecs
        out["Evals"] = [E[i] for i in soft]
        out["eps"] = float(eps)
        out["gap"] = float(E[1] - E[0])
        out["Emax"] = float(E[K - 1])
        out["vecs_f64"] = [np.array([float(t) for t in v])
                           for v in vecs]
    return out


def compress_selector(cell: dict, cb: dict, kind: str, payload):
    """Cluster compression Sc (mp matrix, dim = len(soft)) computed
    exactly in mp from the frozen selector."""
    K = cell["K"]
    vecs = cb["vecs"]
    d = len(vecs)
    with mp.workdps(cell["dps"]):
        Sc = mp.zeros(d, d)
        if kind == "terms":
            for w, t in payload:
                tm = CM.lift_vec(t)
                c = [R4.mp_dot(v, tm) for v in vecs]
                wm = mp.mpf(repr(float(w)))
                for i in range(d):
                    for j in range(i, d):
                        val = Sc[i, j] + wm * c[i] * c[j]
                        Sc[i, j] = val
                        Sc[j, i] = val
        else:
            if kind == "mat64":
                Mm = mp.zeros(K, K)
                for i in range(K):
                    for j in range(K):
                        if payload[i, j] != 0.0:
                            Mm[i, j] = mp.mpf(repr(float(payload[i, j])))
            else:
                Mm = None
                for key in payload:
                    Mm = cell[key] if Mm is None else Mm + cell[key]
            Sv = [R4.matvec(Mm, v, K) for v in vecs]
            for i in range(d):
                for j in range(i, d):
                    val = (R4.mp_dot(vecs[i], Sv[j])
                           + R4.mp_dot(vecs[j], Sv[i])) / 2
                    Sc[i, j] = val
                    Sc[j, i] = val
    return Sc


def dblt_read(cell: dict, Sc) -> dict:
    """Doublet 2x2 exact reads (indices 0, 1 of the cluster basis).
    phi = PRINCIPAL error angle of the v0-nearest S-eigenvector
    (|phi| <= pi/4); branch = which eigenvalue that eigenvector
    carries (MAX iff s00 > s11, exact 2x2 fact)."""
    with mp.workdps(cell["dps"]):
        s00, s01, s11 = Sc[0, 0], Sc[0, 1], Sc[1, 1]
        dd = s00 - s11
        split = mp.sqrt(dd * dd + 4 * s01 * s01)
        if dd == 0:
            phi = (mp.pi / 4 if s01 > 0 else
                   (-mp.pi / 4 if s01 < 0 else mp.mpf(0)))
        else:
            phi = mp.atan(2 * s01 / dd) / 2
        return {"s00": float(s00), "s01": float(s01),
                "s11": float(s11), "split": float(split),
                "phi": float(phi),
                "branch": "MAX" if dd > 0 else "MIN"}


def cluster_read(cell: dict, Sc, d: int) -> dict:
    """Full-cluster eigendecomposition reads (v0 = basis index 0)."""
    with mp.workdps(cell["dps"]):
        Ec, Vc = mp.eigsy(Sc)
        order = sorted(range(d), key=lambda i: Ec[i])
        ovs = [abs(Vc[0, i]) for i in range(d)]
        istar = max(range(d), key=lambda i: ovs[i])
        rank = order.index(istar)
        evs = [float(Ec[order[i]]) for i in range(d)]
        spread = max(evs) - min(evs)
        iso = min([abs(evs[rank] - evs[r]) for r in range(d)
                   if r != rank], default=0.0)
        pos = ("BOT" if rank == 0 else
               ("TOP" if rank == d - 1 else "MID%d" % rank))
        return {"evs": evs, "rank": rank, "pos": pos,
                "ov0": float(ovs[istar]),
                "split_rel": iso / max(spread, 1e-300),
                "spread": spread}


def cluster_read_at(cell: dict, Sc, d: int, pos: str) -> dict:
    """Achieved reads when the FROZEN branch pos is applied."""
    with mp.workdps(cell["dps"]):
        Ec, Vc = mp.eigsy(Sc)
        order = sorted(range(d), key=lambda i: Ec[i])
        rank = 0 if pos == "BOT" else (d - 1 if pos == "TOP"
                                       else int(pos[3:]))
        rank = min(max(rank, 0), d - 1)
        istar = order[rank]
        evs = [float(Ec[order[i]]) for i in range(d)]
        spread = max(evs) - min(evs)
        iso = min([abs(evs[rank] - evs[r]) for r in range(d)
                   if r != rank], default=0.0)
        return {"ov0": float(abs(Vc[0, istar])),
                "split_rel": iso / max(spread, 1e-300)}


def f64_select(cell: dict, ncl: int, M64: np.ndarray, pos: str,
               v0mp_f64: np.ndarray) -> float:
    """The f64-cost pipeline: f64 eigh cluster basis, f64 compression,
    frozen branch, overlap vs the mp truth ground state."""
    w, U = np.linalg.eigh(cell["m_tilde"])
    B = U[:, :ncl]
    Sc = B.T @ M64 @ B
    Sc = (Sc + Sc.T) / 2
    ws, Us = np.linalg.eigh(Sc)
    rank = 0 if pos == "BOT" else (ncl - 1 if pos == "TOP"
                                   else int(pos[3:]))
    rank = min(max(rank, 0), ncl - 1)
    wstar = B @ Us[:, rank]
    return float(abs(np.dot(wstar, v0mp_f64)))


# --------------------------------------------------------- symbolic S1
def symbolic_gates() -> list[tuple[str, bool, str]]:
    import sympy as spy
    out = []
    # G10: exact 2x2 rotation law tan(2 phi) = 2 s01/(s00 - s11)
    s00, s01, s11 = spy.symbols("s00 s01 s11", real=True)
    dd = s00 - s11
    t2 = 2 * s01 / dd
    c2 = 1 / spy.sqrt(1 + t2 ** 2)
    s2 = t2 * c2
    off = s01 * c2 - dd / 2 * s2
    ok10 = spy.simplify(off) == 0
    out.append(("G10-eigenangle-exact", ok10,
                "rotation by phi with tan(2phi) = 2 s01/(s00-s11) "
                "kills the 2x2 off-diagonal exactly: selector error "
                "angle phi ~= |s01|/split, certification cost ~ "
                "log(1/split) digits"))
    # G11: commutator identity on an exact rational spectral example
    S3 = spy.Matrix([[0, spy.Rational(1, 2), spy.Rational(-1, 3)],
                     [spy.Rational(-1, 2), 0, spy.Rational(1, 5)],
                     [spy.Rational(1, 3), spy.Rational(-1, 5), 0]])
    I3 = spy.eye(3)
    R = (I3 - S3).inv() * (I3 + S3)
    lam = spy.diag(spy.Rational(1, 7), spy.Rational(3, 5),
                   spy.Integer(2))
    Q3 = R * lam * R.T
    v0 = R.col(0)
    v1 = R.col(1)
    Sarb = spy.Matrix([[1, spy.Rational(2, 3), spy.Rational(-1, 5)],
                       [spy.Rational(2, 3), spy.Rational(1, 2),
                        spy.Rational(1, 7)],
                       [spy.Rational(-1, 5), spy.Rational(1, 7), 3]])
    lhs = (lam[0, 0] - lam[1, 1]) * (v0.T * Sarb * v1)[0, 0]
    rhs = (v0.T * (Q3 * Sarb - Sarb * Q3) * v1)[0, 0]
    ok11 = spy.simplify(lhs - rhs) == 0
    out.append(("G11-commutator-identity-exact", ok11,
                "(E0 - E1) <v0,S v1> == <v0,[Q,S] v1> exactly on a "
                "rational orthogonal spectral example: the doublet "
                "off-diagonal of ANY selector is a Q-commutator "
                "element amplified by 1/gap"))
    # G12: block-collapse on the same example
    Parb = spy.Matrix([[2, spy.Rational(-1, 4), spy.Rational(1, 6)],
                       [spy.Rational(-1, 4), 1, spy.Rational(2, 7)],
                       [spy.Rational(1, 6), spy.Rational(2, 7), -1]])
    A3 = Q3 + Parb    # 'arch' block when Q = A - P
    s01A = (v0.T * A3 * v1)[0, 0]
    s01P = (v0.T * Parb * v1)[0, 0]
    dA = (v0.T * A3 * v0)[0, 0] - (v1.T * A3 * v1)[0, 0]
    dP = (v0.T * Parb * v0)[0, 0] - (v1.T * Parb * v1)[0, 0]
    ok12 = (spy.simplify(s01A - s01P) == 0
            and spy.simplify((dA - dP) - (lam[0, 0] - lam[1, 1])) == 0)
    out.append(("G12-block-collapse-exact", ok12,
                "Q = A - P diagonal on the doublet => s01(A) == s01(P) "
                "exactly and split(A) - split(P) == E0 - E1: the "
                "arithmetic block selects exactly as the archimedean "
                "complement beyond the Connes scale"))
    # G13: Markov sharpness + poly-filter split law (exact instance)
    z = spy.symbols("z", real=True)
    T3 = 4 * z ** 3 - 3 * z
    dT3 = spy.diff(T3, z)
    ok13a = dT3.subs(z, 1) == 9 and dT3.subs(z, -1) == 9
    # |T3'| <= 9 on [-1,1]: T3' = 12 z^2 - 3, max at |z| = 1
    ok13b = spy.maximum(dT3, z, spy.Interval(-1, 1)) == 9
    E0r, E1r = spy.Rational(1, 10 ** 7), spy.Rational(2, 10 ** 7)
    m, M = spy.Integer(0), spy.Integer(2)
    u = (2 * z - (M + m)) / (M - m)
    p = T3.subs(z, u)
    splt = spy.Abs(p.subs(z, E1r) - p.subs(z, E0r))
    bound = (E1r - E0r) * 9 * spy.Rational(2, 2)   # gap * d^2 * 2/(M-m)
    ok13c = bool(splt <= bound)
    out.append(("G13-markov-filter-law", ok13a and ok13b and ok13c,
                "Chebyshev T_3 sharpness max|T3'| = 9 = d^2 exact; "
                "exact instance |p(E1)-p(E0)| <= gap * 2 d^2/(M-m): "
                "POLY-FILTER NO-GO (cited A.A. Markov 1889): any "
                "degree-d filter of Q splits the doublet by <= "
                "2 d^2 gap/(M-m); split s needs d >= sqrt(s(M-m)/"
                "(2 gap)) ~ e^{c lambda^2/2}"))
    # G14: rank-1 selector exact solution
    t0, t1 = spy.symbols("t0 t1", positive=True)
    M2 = spy.Matrix([[t0 ** 2, t0 * t1], [t0 * t1, t1 ** 2]])
    vec = spy.Matrix([t0, t1])
    ok14 = (spy.simplify(M2 * vec - (t0 ** 2 + t1 ** 2) * vec)
            == spy.zeros(2, 1))
    out.append(("G14-rank1-exact", ok14,
                "t t^T on the doublet has eigenvector (t0, t1) with "
                "eigenvalue t0^2 + t1^2 (other 0): the rank-1 "
                "selector's error angle is exactly atan(|t1/t0|) -- "
                "for t = k-hat that is atan|beta/alpha| == the "
                "round-122 mixing number"))
    return out


# ---------------------------------------------------------------- main
def main() -> int:
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke

    print("selection_probe -- PRIME.CCM.SELECTION.01")
    print("SPEC_SHA %s" % SPEC_SHA[:16])
    print("mode: %s" % ("SMOKE (NOT-VERDICT-BEARING)" if smoke
                        else "FULL"))
    print("NO RH CLAIM.  EXPLORATION ONLY.")

    rungs = ((3, 45), (5, 60)) if smoke else RUNGS
    gate_rungs = (3, 5) if smoke else GATE_RUNGS
    deep2 = (5,) if smoke else DEEP2
    enr = () if smoke else ENR_RUNGS
    worlds = () if smoke else WORLD_R

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
    section("S1  EXACT GATES (sympy): the trade-off / no-go skeleton")
    for name, okg, detg in symbolic_gates():
        check(name, okg, detg)

    # ---------------------------------------------------------- S2
    section("S2  INSTRUMENT (round-122 builder reused + wards)")
    cells: dict[int, dict] = {}
    for x, dps in rungs:
        t0 = time.time()
        cells[x] = R4.build_cell(x, KFAC1, "MAIN", dps, want_mp=True)
        print("  MAIN x=%-2d built (K=%d, dps=%d, %.1f s, tau=%s "
              "gap=%s)" % (x, cells[x]["K"], dps, time.time() - t0,
                           cells[x]["tau_str"], cells[x]["gap_str"]),
              flush=True)
    if 3 not in cells:
        ce3 = R4.build_cell(3, KFAC1, "MAIN", 45)
    else:
        ce3 = cells[3]
    sl3 = SL.build_trig_cell_hp(3, KFAC1, "MAIN", 45)
    dev_m = float(np.max(np.abs(ce3["m_tilde"] - sl3["m_tilde"])))
    check("G20-ward-x3-even", dev_m <= 1e-8,
          "own even x=3 matrix vs SL HP: max dev %.1e" % dev_m)
    cellsE: dict[int, dict] = {}
    for x, dps in enr:
        t0 = time.time()
        cellsE[x] = R4.build_cell(x, KFAC_ENR, "MAIN", dps,
                                  want_mp=True)
        print("  ENRICHED (KFAC %.2f) x=%d built (K=%d, %.1f s)"
              % (KFAC_ENR, x, cellsE[x]["K"], time.time() - t0),
              flush=True)
    cw: dict[tuple, dict] = {}
    for wnm, x, dps in worlds:
        t0 = time.time()
        cw[(wnm, x)] = R4.build_cell(x, KFAC1, wnm, dps, want_mp=True)
        print("  %s x=%d built (%.1f s)" % (wnm, x, time.time() - t0),
              flush=True)
    # v^2 closed form ward (grid quadrature)
    xw = rungs[0][0]
    cellw = cells[xw]
    Lw = cellw["a"]
    vgw = np.linspace(-Lw, Lw, 40001)
    V2 = v2_matrix(cellw)
    worst = 0.0
    for (k, j) in ((0, 0), (0, 3), (2, 2), (1, 4)):
        bk = (np.full_like(vgw, 1.0 / math.sqrt(2 * Lw)) if k == 0
              else np.cos(cellw["om"][k] * vgw) / math.sqrt(Lw))
        bj = (np.full_like(vgw, 1.0 / math.sqrt(2 * Lw)) if j == 0
              else np.cos(cellw["om"][j] * vgw) / math.sqrt(Lw))
        qv = float(np.trapezoid(vgw * vgw * bk * bj, vgw))
        worst = max(worst, abs(qv - V2[k, j])
                    / max(abs(V2[k, j]), 1e-12))
    check("G21-v2-closed-form", worst <= V2_WARD_BAR,
          "v^2 multiplication matrix closed form vs 40001-grid "
          "quadrature: worst rel %.1e (bar %.0e)"
          % (worst, V2_WARD_BAR))

    # ---------------------------------------------------------- S3
    section("S3  TRUTH ANATOMY (doublet, cascade, annihilator, signs)")
    core: dict[int, dict] = {}
    cbs: dict[int, dict] = {}
    kts: dict[int, np.ndarray] = {}
    tps: dict[int, dict] = {}
    okreg = True
    okeig = True
    regd = []
    for x, dps in rungs:
        kt = R4.prolate_kvec(x, cells[x])
        kts[x] = kt
        rc = CM.rung_core(cells[x], kt)
        core[x] = rc
        cb = cluster_basis_mp(cells[x], kt)
        cbs[x] = cb
        okeig = okeig and rc["eigres"] <= 10.0 ** (-(dps // 2))
        if x in R124_BETA:
            rel = abs(abs(rc["beta"]) / R124_BETA[x] - 1)
            gr = abs(rc["gap"] / R124_GAP[x] - 1)
            regd.append("x%d:b%.1e,g%.1e" % (x, rel, gr))
            okreg = okreg and rel <= REG_BAR and gr <= 1e-4 \
                and rc["nsoft"] == R124_NSOFT[x]
        print("  x=%-2d eps %s gap %s ncl %-2d alpha %.8f "
              "beta %+.6e" % (x, rc["eps_str"], rc["gap_str"],
                              len(cb["soft"]), rc["alpha"],
                              rc["beta"]), flush=True)
        print("       cascade gaps %s"
              % ["%.2e" % g for g in rc["cl_gaps"][:7]])
    check("G22-eigen-residuals", okeig,
          "||Q v_i - lam_i v_i|| <= 10^-(dps/2) at every rung (max "
          "%.1e)" % max(core[x]["eigres"] for x, _d in rungs))
    check("G23-r124-regression", okreg or smoke,
          "beta / gap / nsoft match the round-124 run2 pins: %s"
          % ", ".join(regd))
    # templates + mode-scan pins
    okpin = True
    pind = []
    for x, _d in rungs:
        tps[x] = build_templates(cells[x], x)
        if x not in R124_V1E8:
            continue
        with mp.workdps(cells[x]["dps"]):
            v1m = cbs[x]["vecs"][1]
            v0m = cbs[x]["vecs"][0]
            o18 = abs(float(R4.mp_dot(v1m, CM.lift_vec(
                tps[x]["ehat"][8]))))
            o04 = abs(float(R4.mp_dot(v0m, CM.lift_vec(
                tps[x]["ehat"][4]))))
        d1 = abs(o18 - R124_V1E8[x])
        d0 = abs(o04 - R124_V0E4[x])
        pind.append("x%d:%.4f/%.4f" % (x, o18, o04))
        okpin = okpin and d1 <= MODE_PIN_BAR and d0 <= MODE_PIN_BAR
    check("G24-mode-scan-pins", okpin or smoke,
          "|<v1,e8>| / |<v0,e4>| = %s vs round-124 pins (bar %.0e "
          "abs): the doublet's prolate-mode labels reproduce"
          % (", ".join(pind), MODE_PIN_BAR))
    # annihilator gate + above-band profile (ward)
    okann = True
    for x, _d in rungs:
        cell = cells[x]
        edge = cell["K"] * math.pi / cell["a"]
        inb, abv = ward_band_split(gam, edge, ZAB_N)
        vdb = []
        vcl = []
        for g in inb[:6]:
            ev = ward_evec_gamma(cell, float(g))
            ev = ev / np.linalg.norm(ev)
            with mp.workdps(cell["dps"]):
                ovv = [abs(float(R4.mp_dot(cbs[x]["vecs"][i],
                                           CM.lift_vec(ev))))
                       for i in range(len(cbs[x]["vecs"]))]
            vdb.append(max(ovv[:2]))
            vcl.append(max(ovv))
        mxd = max(vdb) if vdb else 0.0
        mxc = max(vcl) if vcl else 0.0
        bar = (1e-1 if x == 3 else       # smoke-only shallow rung
               (ANNIH_BAR_X5 if x <= 5 else ANNIH_BAR_DEEP))
        okann = okann and mxd <= bar
        ev0 = ward_evec_gamma(cell, float(abv[0]))
        ev0 = ev0 / np.linalg.norm(ev0)
        with mp.workdps(cell["dps"]):
            a0 = abs(float(R4.mp_dot(cbs[x]["vecs"][0],
                                     CM.lift_vec(ev0))))
            a1 = abs(float(R4.mp_dot(cbs[x]["vecs"][1],
                                     CM.lift_vec(ev0))))
        print("  x=%-2d in-band max DOUBLET evaluation %.1e (bar "
              "%.0e; full-cluster max %.1e, the loose member is the "
              "shallow cluster edge only); first above-band "
              "|<e,v0>| %.2e |<e,v1>| %.2e"
              % (x, mxd, bar, mxc, a0, a1))
    check("G30-annihilator-zero-class", okann,
          "max in-band |<e_gamma, v_0/v_1>| <= bar at every rung: "
          "the in-band zero-evaluation class acts as ~0 on the "
          "DEGENERATE DOUBLET by the annihilator law -- no zero-"
          "transcribing selector exists in evaluation form on the "
          "selection target (the shallow cluster edge at gap ~1e-2 "
          "is energy-resolvable anyway); above-band evaluations are "
          "measured and live in the DISGUISE SCREEN")
    # exact block identity on the doublet (mp, every rung)
    okblk = True
    blkd = []
    for x, dps in rungs:
        cell = cells[x]
        cb = cbs[x]
        with mp.workdps(dps):
            v0m, v1m = cb["vecs"][0], cb["vecs"][1]
            K = cell["K"]
            Aop = cell["mpPole"] + cell["mpArch"]
            sA = R4.mp_dot(v0m, R4.matvec(Aop, v1m, K))
            sP = R4.mp_dot(v0m, R4.matvec(cell["mpPrime"], v1m, K))
            dev = float(abs(sA - sP))
            dA = (R4.mp_dot(v0m, R4.matvec(Aop, v0m, K))
                  - R4.mp_dot(v1m, R4.matvec(Aop, v1m, K)))
            dP = (R4.mp_dot(v0m, R4.matvec(cell["mpPrime"], v0m, K))
                  - R4.mp_dot(v1m, R4.matvec(cell["mpPrime"], v1m,
                                             K)))
            gdev = float(abs((dA - dP) - (cb["Evals"][0]
                                          - cb["Evals"][1])))
        bar = 10.0 ** (-(dps // 3))
        okblk = okblk and dev <= bar and gdev <= bar
        blkd.append("x%d:%.1e/%.1e" % (x, dev, gdev))
        print("  x=%-2d s01(arch) %+.6e == s01(prime) %+.6e "
              "(dev %.1e); split shift == -gap (dev %.1e)"
              % (x, float(sA), float(sP), dev, gdev))
    check("G31-block-collapse-mp", okblk,
          "s01(Mpole+March) == s01(Mprime) and split difference == "
          "E0-E1 at every rung (devs %s, bar 10^-(dps/3)): the "
          "arithmetic block carries NO selection information beyond "
          "the archimedean complement on the doublet, exactly"
          % ", ".join(blkd))
    # sign anatomy + Lambda pairing table
    for x in deep2:
        cell = cells[x]
        L = cell["a"]
        vg = np.linspace(-L, L, NGRID)
        negm = []
        for i, vf in enumerate(cbs[x]["vecs_f64"][:4]):
            f = CM.cell_fn_on_grid(vf, cell, vg)
            neg = float(np.trapezoid(np.where(f < 0, f * f, 0.0), vg))
            tot = float(np.trapezoid(f * f, vg))
            negm.append(neg / tot)
        print("  x=%-2d negative-mass fraction v0/v1/v2/v3: %s"
              % (x, ["%.3f" % t for t in negm]))
    for x, _d in rungs:
        with mp.workdps(cells[x]["dps"]):
            v0m, v1m = cbs[x]["vecs"][0], cbs[x]["vecs"][1]
            r = []
            for nm, t in (("klam", tps[x]["t_klam"]),
                          ("sh2", tps[x]["t_sh"][2]),
                          ("sh3", tps[x]["t_sh"][3])):
                a0 = float(R4.mp_dot(v0m, CM.lift_vec(t)))
                a1 = float(R4.mp_dot(v1m, CM.lift_vec(t)))
                r.append("%s: %+.3f/%+.3f" % (nm, a0, a1))
        print("  x=%-2d Lambda pairing <v0,t>/<v1,t>: %s"
              % (x, "; ".join(r)))
    check("G32-anatomy-reads", True,
          "sign anatomy + Lambda-pairing table printed (T1c/T1e "
          "measured data; positivity and arithmetic-pairing "
          "selectors adjudicated in S4 on these objects)")

    # ---------------------------------------------------------- S4
    section("S4  THE SELECTOR ZOO (doublet + cluster + f64 pipeline)")
    zoo_all = list(ZOO) + ["S_E8"]
    dbl: dict[str, dict[int, dict]] = {nm: {} for nm in zoo_all}
    clu: dict[str, dict[int, dict]] = {nm: {} for nm in zoo_all}
    f64ov: dict[str, dict[int, float]] = {nm: {} for nm in zoo_all}
    Scs: dict[str, dict[int, object]] = {nm: {} for nm in zoo_all}
    specs_by_x: dict[int, dict] = {}
    for x, _d in rungs:
        cell = cells[x]
        cb = cbs[x]
        d = len(cb["soft"])
        specs = selector_specs(cell, tps[x], kts[x])
        specs_by_x[x] = specs
        for nm in zoo_all:
            kind, payload = specs[nm]
            Sc = compress_selector(cell, cb, kind, payload)
            Scs[nm][x] = Sc
            dbl[nm][x] = dblt_read(cell, Sc)
            clu[nm][x] = cluster_read(cell, Sc, d)
            M64 = spec_f64_matrix(cell, kind, payload)
            f64ov[nm][x] = f64_select(cell, d, M64, clu[nm][x]["pos"],
                                      cb["vecs_f64"][0])
        # oracle sanity
        ScO = compress_selector(cell, cb, "terms",
                                [(1.0, cb["vecs_f64"][0])])
        dO = dblt_read(cell, ScO)
        cO = cluster_read(cell, ScO, d)
        okO = abs(dO["phi"]) <= 1e-10 and cO["ov0"] >= 1.0 - 1e-12
        Scs.setdefault("S_ORACLE", {})[x] = ScO
        if x == rungs[0][0]:
            check("G40-oracle-sanity", okO,
                  "S_ORACLE = v0 v0^T: phi %.1e, cluster ov0 %.12f "
                  "(instrument exactness)" % (dO["phi"], cO["ov0"]))
        for nm in zoo_all:
            db = dbl[nm][x]
            cl = clu[nm][x]
            print("  x=%-2d %-9s dblt: s01 %+.2e split %.2e phi "
                  "%+.2e [%s] | cluster: pos %-5s ov0 %.6f "
                  "split_rel %.2e | f64 ov %.6f"
                  % (x, nm, db["s01"], db["split"], db["phi"],
                     db["branch"], cl["pos"], cl["ov0"],
                     cl["split_rel"], f64ov[nm][x]), flush=True)
    # orientation freezing on the gate rungs
    orient: dict[str, tuple] = {}
    unstable: list[str] = []
    for nm in zoo_all:
        brs = [dbl[nm][x]["branch"] for x in gate_rungs]
        pss = [clu[nm][x]["pos"] for x in gate_rungs]
        if brs[0] == brs[-1] and pss[0] == pss[-1]:
            orient[nm] = (brs[0], pss[0])
        else:
            unstable.append(nm)
    check("G41-orientation-protocol", True,
          "frozen v0-branches from gate rungs x=%s: %s; UNSTABLE "
          "(gate rungs disagree, excluded): %s"
          % (str(gate_rungs),
             ", ".join("%s:%s/%s" % (nm, orient[nm][0], orient[nm][1])
                       for nm in zoo_all if nm in orient),
             ", ".join(unstable) if unstable else "none"))
    # achieved out-of-sample reads at the deep rungs
    ach: dict[str, dict[int, dict]] = {nm: {} for nm in zoo_all}
    for nm in zoo_all:
        if nm not in orient:
            continue
        br, pos = orient[nm]
        for x in deep2:
            cell = cells[x]
            d = len(cbs[x]["soft"])
            db = dbl[nm][x]
            phi = db["phi"]
            match = (db["branch"] == br)
            ovd = math.cos(phi) if match else abs(math.sin(phi))
            ca = cluster_read_at(cell, Scs[nm][x], d, pos)
            ach[nm][x] = {"ov_dblt": ovd, "ov_clu": ca["ov0"],
                          "split_rel": ca["split_rel"],
                          "phi_ach": math.acos(min(ovd, 1.0))}
    check("G42-f64-pipeline", all(
        f64ov["S_K"][x] >= 1.0 - F64_SK_BAR for x in deep2),
        "S_K at f64 spectral cost: ov(w*_f64, v0_mp) = %s at the "
        "deep rungs (bar >= 1 - %.0e): the SECTOR selection runs "
        "entirely at f64 eigensolve cost -- no Connes-precision "
        "eigensolve needed for the k-hat direction"
        % (["x%d:%.8f" % (x, f64ov["S_K"][x]) for x in deep2],
           F64_SK_BAR))
    # enriched-frame selector floors at the gate rungs
    if enr:
        rows = []
        for x, _d in enr:
            cellE = cellsE[x]
            ktE = R4.prolate_kvec(x, cellE)
            cbE = cluster_basis_mp(cellE, ktE)
            ScE = compress_selector(cellE, cbE, "terms", [(1.0, ktE)])
            dbE = dblt_read(cellE, ScE)
            rows.append((x, dbE["phi"]))
        check("G43-enriched-frame-floor", True,
              "S_K error angle at the matched enriched frame (KFAC "
              "%.2f): %s vs KFAC 1.25 %s -- the selector floor IS "
              "the frame-dependent beta (falls ~x^-2.8 at matched "
              "enriched frames per round 124, cited not re-fit here)"
              % (KFAC_ENR, ["x%d:%+.2e" % r for r in rows],
                 ["x%d:%+.2e" % (x, dbl["S_K"][x]["phi"])
                  for x, _d in enr]))

    # ---------------------------------------------------------- S5
    section("S5  RATES (split + error laws vs lambda)")
    xs = [x for x, _d in rungs]
    gap_sl = CM.ols_slope([float(x) for x in xs],
                          [math.log10(cbs[x]["gap"]) for x in xs])[0]
    print("  Connes reference: slope log10(gap) vs x = %.3f" % gap_sl)
    rate_ty: dict[str, str] = {}
    rate_rho: dict[str, float] = {}
    for nm in zoo_all:
        srs = [max(clu[nm][x]["split_rel"], 1e-300) for x in xs]
        phs = [max(abs(dbl[nm][x]["phi"]), 1e-300) for x in xs]
        sl_s = CM.ols_slope([float(x) for x in xs],
                            [math.log10(t) for t in srs])[0]
        sl_p = CM.ols_slope([float(x) for x in xs],
                            [math.log10(t) for t in phs])[0]
        rho = sl_s / gap_sl
        rate_rho[nm] = rho
        rate_ty[nm] = ("CONNES" if rho >= RATE_CONNES else
                       ("FREE" if rho <= RATE_FREE else "MID"))
        print("  %-9s split_rel %s slope %.3f rho %.3f [%s] | "
              "phi %s slope %.3f"
              % (nm, ["%.1e" % t for t in srs], sl_s, rho,
                 rate_ty[nm], ["%.1e" % t for t in phs], sl_p))
    check("G50-rate-table", True,
          "rate typing rho = slope(log10 split_rel)/slope(log10 "
          "gap): %s (FREE <= %.2f, CONNES >= %.2f)"
          % (", ".join("%s:%s" % (nm, rate_ty[nm])
                       for nm in zoo_all), RATE_FREE, RATE_CONNES))
    # poly-filter class: measured degree price at the deep rungs
    for x in deep2:
        cb = cbs[x]
        spread = cb["Emax"] - cb["eps"]
        dstar = math.sqrt(1e-6 * spread / (2.0 * cb["gap"]))
        print("  x=%-2d f(Q) class: gap %.2e, hull %.2f -> degree "
              "needed for split 1e-6: d* = %.1e (PROVEN bound, G13)"
              % (x, cb["gap"], spread, dstar))
    check("G51-polyfilter-price", True,
          "the Markov degree price d* ~ e^{c lambda^2/2} printed at "
          "the deep rungs: the energy/filter class pays the Connes "
          "scale PROVABLY (cited Markov 1889 + exact instance G13)")

    # ---------------------------------------------------------- S6
    section("S6  DISGUISE SCREENS (Z1 / de Branges / conditioning)")
    # above-band canonical Gram, compressed (ward/screen)
    corr_ab: dict[str, float] = {}
    for x in deep2:
        cell = cells[x]
        cb = cbs[x]
        d = len(cb["soft"])
        edge = cell["K"] * math.pi / cell["a"]
        _inb, abv = ward_band_split(gam, edge, ZAB_N)
        G = np.zeros((d, d))
        for g in abv:
            ev = ward_evec_gamma(cell, float(g))
            ev = ev / np.linalg.norm(ev)
            with mp.workdps(cell["dps"]):
                c = np.array([float(R4.mp_dot(cb["vecs"][i],
                                              CM.lift_vec(ev)))
                              for i in range(d)])
            G += np.outer(c, c)
        G0 = G - np.trace(G) / d * np.eye(d)
        nG0 = np.linalg.norm(G0)
        for nm in zoo_all:
            Sf = np.array([[float(Scs[nm][x][i, j])
                            for j in range(d)] for i in range(d)])
            S0 = Sf - np.trace(Sf) / d * np.eye(d)
            nS0 = np.linalg.norm(S0)
            cc = (float(np.sum(S0 * G0)) / (nS0 * nG0)
                  if nS0 > 1e-300 and nG0 > 1e-300 else 0.0)
            corr_ab[nm] = max(corr_ab.get(nm, 0.0), abs(cc))
        print("  x=%-2d above-band canonical Gram (N=%d, ward) "
              "compressed: trace %.3f, spread %.3f"
              % (x, len(abv), float(np.trace(G)),
                 float(np.max(np.linalg.eigvalsh(G))
                       - np.min(np.linalg.eigvalsh(G)))))
    screen_ty = {nm: ("DB-DISGUISE" if corr_ab.get(nm, 0.0)
                      >= DISGUISE_CORR else "CLEAN")
                 for nm in zoo_all}
    check("G60-db-disguise-screen", True,
          "max traceless correlation vs the above-band canonical "
          "Gram (r121 de Branges proxy): %s (flag >= %.2f); the "
          "IN-band Gram is ~0 on the cluster (G30) so no selector "
          "can be an in-band zero transcription"
          % (", ".join("%s:%.2f" % (nm, corr_ab.get(nm, 0.0))
                       for nm in zoo_all), DISGUISE_CORR))
    # conditioning screen (gate rungs): does the truth rotate under
    # a Connes-scale perturbation while the selector output stands?
    okc = True
    okz = True
    for x in gate_rungs:
        if x not in cells or smoke and x == 3:
            continue
        cell = cells[x]
        K = cell["K"]
        cb = cbs[x]
        v0f, v1f = cb["vecs_f64"][0], cb["vecs_f64"][1]
        jstar = int(np.argmax(np.abs(v0f * v1f)))
        with mp.workdps(cell["dps"]):
            v00 = mp.mpf(repr(float(v0f[jstar])))
            v10 = mp.mpf(repr(float(v1f[jstar])))
            gapm = cell["mpE"][1] - cell["mpE"][0]
            tgt = mp.mpf(repr(PERT_THETA_TGT))
            den = max(abs(v00 * v10), mp.mpf("1e-30"))
            delta = max(min(tgt * gapm / den, mp.mpf("1e-8")),
                        mp.mpf("1e-45"))
            Qp = cell["mpM"].copy()
            Qp[jstar, jstar] = Qp[jstar, jstar] + delta
            Ep, Vp = mp.eigsy(Qp)
            order = sorted(range(K), key=lambda i: Ep[i])
            v0p = R4.matcol(Vp, order[0], K)
            kv = CM.lift_vec(kts[x])
            if R4.mp_dot(v0p, kv) < 0:
                v0p = [-t for t in v0p]
            # S_K output is FROZEN (source template): its error angle
            # vs the perturbed truth
            nk = R4.mp_norm(kv)
            ovp = abs(R4.mp_dot(v0p, kv) / nk)
            phi_p = mp.acos(min(ovp, mp.mpf(1)))
            phi_0 = mp.mpf(repr(abs(dbl["S_K"][x]["phi"])))
            dphi = float(abs(phi_p - phi_0))
            theta = float(abs(delta * v00 * v10 / gapm))
        ratio = dphi / max(theta, 1e-300)
        okc = okc and COND_RATIO[0] <= ratio <= COND_RATIO[1]
        okz = okz and dphi > 0
        print("  x=%-2d delta %.2e theta_pred %.2e dphi(S_K vs "
              "perturbed truth) %.3e ratio %.2f"
              % (x, float(delta), theta, dphi, ratio))
    check("G61-conditioning-screen", okc and okz,
          "a Connes-scale operator perturbation rotates the TRUE "
          "ground state by theta = delta|v00 v10|/gap while every "
          "source template stands still: measured dphi/theta in "
          "[%.2f, %.2f], strictly nonzero -- ANY selector's "
          "certified accuracy is bounded by (source-data "
          "uncertainty)/gap: the conditioning leg of the "
          "obstruction is selector-independent" % COND_RATIO)

    # ---------------------------------------------------------- S7
    section("S7  WORLDS (controls: the cluster is the arithmetic)")
    okw = True
    for wnm, x, _d in worlds:
        cellq = cw[(wnm, x)]
        K = cellq["K"]
        with mp.workdps(cellq["dps"]):
            E = cellq["mpE"]
            eps = float(E[0])
            ns = len([i for i in range(1, K)
                      if E[i] - E[0] <= mp.mpf(repr(SOFT_BAR))])
            V = cellq["mpV"]
            g0 = CM.sign_fix(R4.matcol(V, 0, K))
            ok4 = abs(float(R4.mp_dot(g0, CM.lift_vec(
                tps[x]["ehat"][4]))))
            ok8 = abs(float(R4.mp_dot(g0, CM.lift_vec(
                tps[x]["ehat"][8]))))
            okk = abs(float(R4.mp_dot(g0, CM.lift_vec(kts[x]))))
        okw = okw and ns == 0
        print("  %-8s x=%-2d eps %+.3e nsoft %d |<g0,e4>| %.3f "
              "|<g0,e8>| %.3f |<g0,k>| %.3f"
              % (wnm, x, eps, ns, ok4, ok8, okk))
    check("G70-world-separation", okw or not worlds,
          "SMOOTH / SCRARITH / EPSTEIN controls: nsoft == 0 at every "
          "control (round-124 replication) -- the Connes-degenerate "
          "annihilator cluster EXISTS ONLY in the true prime world: "
          "the selectors are archimedean/frame templates (world-"
          "blind objects) and the WORLD supplies the selection "
          "target; a selection problem without a cluster is empty, "
          "so the selectors' world-typing is: templates ARCH/FRAME "
          "= world-blind, the cluster itself = the arithmetic")

    # ---------------------------------------------------------- S8
    section("S8  ADJUDICATION (frozen rules)")
    verdict_rows = []
    solved = []
    sector = []
    for nm in ZOO:
        if nm not in orient:
            verdict_rows.append((nm, "UNSTABLE", "-", "-",
                                 rate_ty.get(nm, "-"),
                                 screen_ty.get(nm, "-")))
            continue
        splits = all(ach[nm][x]["split_rel"] >= SPLIT_BAR
                     for x in deep2)
        aligned = all(ach[nm][x]["ov_dblt"] >= math.cos(ALIGN_BAR)
                      for x in deep2)
        beats = aligned and all(
            ach[nm][x]["phi_ach"] <= BEATS_BETA_FAC
            * abs(R124_BETA.get(x, core[x]["beta"])) for x in deep2)
        st = ("SPLITS+ALIGNED" if (splits and aligned) else
              ("SPLITS-MISALIGNED" if splits else "NOSPLIT"))
        verdict_rows.append((nm, st,
                             "yes" if beats else "no",
                             "/".join("%.4f" % ach[nm][x]["ov_dblt"]
                                      for x in deep2),
                             rate_ty[nm], screen_ty[nm]))
        if (splits and aligned and screen_ty[nm] == "CLEAN"
                and rate_ty[nm] == "FREE"):
            (solved if beats else sector).append(nm)
    print("  %-9s %-18s %-5s %-14s %-6s %s"
          % ("selector", "status", "beats", "ov_dblt(deep)", "rate",
             "screen"))
    for row in verdict_rows:
        print("  %-9s %-18s %-5s %-14s %-6s %s" % row)
    if solved:
        composite = "SELECTION-SOLVED(%s)" % ",".join(solved)
    elif sector:
        best = min(sector, key=lambda nm: max(
            ach[nm][x]["phi_ach"] for x in deep2))
        composite = ("SELECTION-SECTOR-ONLY(best %s, floor %s)"
                     % (best, ["x%d:%.2e" % (x, ach[best][x]
                                             ["phi_ach"])
                               for x in deep2]))
    else:
        composite = "SELECTION-NOGO-MEASURED"
    check("G80-composite-adjudication", True, composite)
    # trade-off identity audit: phi*split vs |s01| (small-angle)
    devs = []
    for nm in ("S_K", "S_E4", "S_POS2"):
        for x in deep2:
            db = dbl[nm][x]
            if abs(db["phi"]) < 0.1 and db["split"] > 0:
                r = abs(math.tan(2 * db["phi"]) * (db["s00"]
                                                   - db["s11"])
                        / (2 * db["s01"]) - 1.0) \
                    if db["s01"] != 0 else 0.0
                devs.append(r)
    check("G81-tradeoff-identity-mp", all(r <= 1e-6 for r in devs),
          "tan(2 phi)(s00-s11) == 2 s01 on the measured doublets "
          "(max dev %.1e): the exact accuracy-split trade-off "
          "delta*split = |s01| = |<v0,[Q,S]v1>|/gap holds on the "
          "data" % (max(devs) if devs else 0.0))

    # ---------------------------------------------------------- S9
    section("S9  MIN-CUT + COMPOSITE VERDICT")
    INF = 10 ** 6
    base = {("UNC", "HCELLS"): INF, ("HCELLS", "FORMA"): 1,
            ("FORMA", "RH"): INF,
            ("UNC", "PICK"): INF, ("PICK", "SV"): 1, ("SV", "RH"): INF,
            ("UNC", "R4HYP"): 1, ("R4HYP", "RH"): INF,
            ("UNC", "WEYLM"): INF, ("WEYLM", "WEYLH"): 1,
            ("WEYLH", "RH"): INF}
    f_base = CM.maxflow(dict(base), "UNC", "RH")
    ext = dict(base)
    ext.update({("UNC", "BLKREAL"): INF, ("BLKREAL", "NFCLOS"): INF,
                ("NFCLOS", "LANEACONV"): 1,
                ("LANEACONV", "R4HYP"): INF})
    f_ext = CM.maxflow(dict(ext), "UNC", "RH")
    check("G90-mincut", f_base == 4 and f_ext == 5,
          "flows UNC->RH: base %d, extended %d -- the selection "
          "outcome is MEAS data ON the LANEACONV omega edge (it "
          "prices the k_lambda ~= xi_lambda tracking); no capacity "
          "change, class census {MEAS, OMEGA-POS} cardinality 4 "
          "unchanged" % (f_base, f_ext))
    verdicts = [
        composite,
        "POLYFILTER-NOGO-PROVEN(split(p(Q)) <= 2 d^2 gap/(M-m), "
        "cited Markov 1889, exact instance G13; d* ~ e^{c lambda^2"
        "/2} measured at the deep rungs)",
        "BLOCK-COLLAPSE-EXACT(s01(prime) == s01(arch) at every rung, "
        "G12+G31)",
        "TRADEOFF-IDENTITY-EXACT((E0-E1) s01 = <v0,[Q,S]v1>, "
        "G10+G11+G81)",
        "ANNIHILATOR-ZERO-CLASS(in-band evaluations ~0 on the "
        "cluster, G30)",
        "CONDITIONING(selector-independent: certified accuracy <= "
        "data-uncertainty/gap, G61)",
        "RATE(best split laws: %s)" % ", ".join(
            "%s:rho=%.2f" % (nm, rate_rho[nm])
            for nm in ("S_K", "S_E4", "S_POS2", "S_ARCHOP")),
        "MINCUT(4 base / 5 ext, census {MEAS, OMEGA-POS} unchanged)",
    ]
    for v in verdicts:
        print("  " + v)

    dt = time.time() - T0_WALL
    check("G99-runtime", dt <= RUNTIME_BAR,
          "%.1f s (bar %.0f)" % (dt, RUNTIME_BAR))
    print("\n" + "=" * 78)
    npass = sum(1 for _n, okc_, _d in CHECKS if okc_)
    print("GATES: %d/%d PASS   SPEC_SHA %s   runtime %.1f s"
          % (npass, len(CHECKS), SPEC_SHA[:16], dt))
    fails = [nm for nm, okc_, _ in CHECKS if not okc_]
    if fails:
        print("FAILING GATES: " + ", ".join(fails))
    if smoke:
        print("SMOKE MODE -- NOT-VERDICT-BEARING")
    print("NO RH CLAIM.  EXPLORATION ONLY.")
    return 0 if not fails else 1


if __name__ == "__main__":
    sys.exit(main())
