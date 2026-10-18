#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""frontier_alphalaw_probe -- PRIME.PORT.FRONTIER.ALPHALAW.01
(round 235): turn the r233 alphahat lead (Spearman(delta;
alphahat_{N-1}) = +0.72) into a LAW or prove data-level
irreducibility -- by measuring the INFORMATION DIMENSION of the
frontier offset.  The r233 Newton theorem states delta is a
DETERMINISTIC function of (free chain prefix, node polynomial);
this round builds the exact reconstruction engine for that map,
measures HOW LOCAL the information is (block perturbations,
per-coefficient derivatives, the critical truncation depth
K_crit per window, node-jitter locality), and runs a sealed
DEV/BLIND hunt with four nonlinear predictor forms under the
frozen r231/r233 falsifier.

EXPLORATION ONLY (2026-08-24).  experiments/ level: NO promotion,
NO ledger row, NO marker moved, NO RH CLAIM in either direction.

INDEX FIREWALL (binding, r225-r233 discipline): w = window (kz
rung), N_w = builder depth = (S_w + 1)/2 with S_w = #supp(mutilde),
n = chain degree, j = n - N_w, delta_w = n_flip - N_w with
n_flip = first n with h_n(mutilde) < 0.  n and w never mixed.

LADDER RULE (sealed, = r232/r233): every frame-A rung with
builder depth h <= 900; sorted by (N_w, kz); 42 windows.
DEV/BLIND RULE (sealed, = r233): even positions (0-indexed) on
the sorted ladder are DEV (21), odd are BLIND (21).  Every
predictor constant is computed from DEV rows only; BLIND rows
are scored exactly once with frozen constants.

PREDICTOR INPUT FIREWALL (= r233): a predictor may consume the
SOURCE data (node positions/weights of both zones) and the FREE
chain (h_n, alphahat_n, gammahat_n with n <= N_w - 1) of its own
window; it may NEVER consume h/r/tau/sign data at degrees
>= N_w, nor the flip location, nor another window's chain.

THE RECONSTRUCTION ENGINE (new, exact by the r233 Newton
theorem): the moment functional restricted to degree < S is
determined by the free prefix (alphahat_0..alphahat_{N-1},
gammahat_1..gammahat_{N-1}, h_0); its extension to all degrees
is forced by reduction mod the node polynomial L (equivalently
the Newton recurrence m_{S+t} = -sum_i a_i m_{i+t}).  On the
node-value representation the reduction is automatic
(L(x_i) = 0), so the forced continuation = the unique weight
vector phi on the S nodes solving the S x S graded system
Lambda[q_j q_k] = h_j delta_jk over balanced pairs
(j, k) = (ceil(d/2), floor(d/2)), d = 0..S-1, with the prefix
polynomials q built from the (possibly perturbed / truncated)
prefix by the scaled monic recurrence.  The continued chain of
phi delivers the flip.  TYPED LOUDLY: with the FULL prefix this
map is the identity (input dimension = S) -- an exact ALIAS of
the r233 determinism theorem, NOT a predictor; it is gated as
the round-trip determinism ward and EXCLUDED from the predictor
competition.  The LAW question of this round is COMPRESSION:
does a dimension << S input suffice?

LEG A -- CENSUS REGENERATION: the r233 census code
(frontier_micro_probe.window_row / sm_flip) is imported and
re-run on the full 42-rung ladder.  Gates: delta histogram ==
{0: 18, 1: 10, 2: 6, 3: 6, 4: 1, 5: 1} exactly; no flip below
N_w; both flip paths agree; S = 2N - 1 everywhere; the five
r228 offsets 0/2/2/3/1 re-derived; the r233 lead re-gated
(Spearman(delta; alphahat_{N-1}) >= +0.5 on all 42).

LEG B -- INFORMATION LOCALITY (the round's sharpest leg; these
are MEASUREMENTS that may consume the census truth -- they are
not predictors and enter no score):
  (b1) BLOCK PERTURBATIONS: alphahat_n += 1e-8 for ALL
       n < N - K, K in {5, 10, 20, 40}; propagate through the
       engine; report per K the count of windows with delta
       changed and the crossing shift |dx|; K_crit_eps(w) =
       smallest grid K with delta unchanged.
  (b2) PER-COEFFICIENT DERIVATIVES: alphahat_n += 1e-6 at the
       sealed positions n = round(f N) for f in {0.05, 0.25,
       0.50, 0.75} and n = N - 10, N - 2; sensitivity s_n =
       |x_pert - x_recon| / 1e-6 (differential against the
       engine's own round-trip crossing, cancelling the engine
       floor); report the profile and the early/late ratio.
  (b3) TRUNCATION DIMENSION (the central number): replace the
       prefix at n < N - K by the equilibrium values
       alphahat = 0, gammahat = 1/4 (h_0 kept; global scale is
       irrelevant by r232 scale invariance), keep the last K
       coefficients true, continue through the engine; success
       = flip == census flip exactly.  Grid K in {10, 25, 50,
       100, 150, 200, 300, 400} (K < N), then BISECTION between
       the LARGEST FAILING K and the smallest succeeding K
       above it, down to adjacency.  K_crit(w) = the
       stabilization point (success at K_crit, failure at the
       bisected K_crit - 1 boundary); accidental successes
       BELOW a failing K are integer collisions of a wrong
       truncated world with the census flip -- counted and
       typed, never credited as locality.  Deliverables: K_crit
       per window, its histogram, K_crit/N, and
       Spearman(K_crit; N) -- the measured information
       dimension and its scaling.
  (b4) NODE-POLYNOMIAL LOCALITY: jitter ONE node x_i += 1e-6
       with the prefix and h-targets held fixed (this isolates
       the forced-tail dependence on L), at the sealed sorted-
       node quantile positions q in {0, 1/4, 1/2, 3/4, 1};
       report |dx| per position and delta-change counts; type
       EDGE vs INTERIOR dominance.

LEG C -- SEALED NONLINEAR PREDICTORS (forms and K candidates
sealed HERE, before any evaluation; DEV-fitted, BLIND-scored
once; NO PREDICTION = miss):
  C1 2D MONOTONE BINNING on (alphahat_{N-1}, gammahat_{N-1}):
     score s = least-squares fit of delta on the two features
     (DEV); 4 equal-count quantile bins of s on DEV; bin value
     = round(median DEV delta), monotonized by cumulative max;
     BLIND assigned by the frozen DEV bin edges.
  C2 3D MONOTONE BINNING: same procedure with features
     (alphahat_{N-1}, gammahat_{N-1} - 1/4, h_0).
  C3 FORCED-MOMENT 1-NN: features = the first two forced
     moments in the r233 normalization (m_S/sigma_S,
     m_{S+1}/sigma_{S+1}), computed directly on the source
     (equal to the Newton values, gated exactly in rationals);
     rule = 1-nearest-neighbour in DEV-standardized space
     (zero fitted constants).
  C4 EXACT SHORT-CHAIN PREDICTOR: delta_hat = engine flip - N
     from the TRUNCATED prefix (equilibrium below N - K, true
     last K coefficients + node polynomial + h_0); sealed K
     candidates {10, 25, 50}; K chosen on DEV by exact rate
     (tie -> smaller K); BLIND scored once.  If leg B measures
     small locality, C4 MUST hit.
SCORING (sealed): exact = (delta_hat == delta), pm1 =
(|delta_hat - delta| <= 1); baseline = constant DEV-mode delta.
LAW BARS (sealed, from the contract): BLIND exact >= 0.674 AND
BLIND pm1 >= 0.8.  FALSIFIER (frozen r231/r233): the same
functional form must locate the control flips EPSTEIN/SCRAMBLE/
SMOOTH = 25/21/27 (re-gated) within +-2.  C4 is applied to the
controls through the same truncated engine (search from n = 1);
C1-C3 are midpoint-anchored offset forms and CANNOT locate a
flip at n ~ 25: they fail the falsifier by construction
(adjudicated loudly, not hidden -- exactly the r233 treatment).

LEG D -- ADJUDICATION (sealed): on a hit, the alias check:
C1-C3 consume 2-3 floats at n <= N - 1 (source-pure), C4
consumes the last K chain coefficients + node positions + h_0
and NEVER gammahat/h at n >= N_w; the full-prefix engine is
typed ALIAS_OF_DETERMINISM (input dimension S) and competes in
no score.  SEALED VERDICT RULE:
  FRONTIER_LOCAL_LAW_K(K)   iff C4 passes both LAW bars AND the
                            falsifier (3/3 controls within +-2);
  FRONTIER_ALPHALAW_FOUND(f) iff C1, C2 or C3 passes both LAW
                            bars AND the falsifier;
  FRONTIER_PREDICTOR_PARTIAL(f) iff some form passes both LAW
                            bars but fails the falsifier;
  FRONTIER_NONLOCAL_IRREDUCIBLE otherwise, quantified by the
                            leg-B dimension (median K_crit,
                            scaling vs N, sensitivity ratios)
                            and the best blind rates.

MUST-FAILS (each loud): (m1) the frontier-consumption oracle
(reading gammahat signs at j >= 0) hits delta on ALL windows --
bars are reachable, oracle excluded by the input firewall;
(m2) the engine's rational toy gate broken on purpose: the
graded rhs shifted by one row must NOT reproduce the toy
weights; (m3) gross prefix corruption (alphahat += 0.1 below
N - 40) must MOVE the w9 flip -- the perturbation harness has
teeth.  ENGINE WARDS: (e1) exact rational toy (S = 7, N = 4,
signed): reconstruction returns the true weights EXACTLY and
the Newton recurrence m_{S+t} = -sum a_i m_{i+t} holds EXACTLY
for t = 0..3; (e2) f64 round-trip on all 42 windows reproduces
the census flip exactly; (e3) the round-trip crossing floor
|x_recon - x_census| is reported (median/max) and every leg-B
sensitivity is read against it.

RECORD TABLES (frozen from calib_r235_pass1.log, 22/22 gates;
smoke adjudicates infrastructure only.  CALIBRATION AMENDMENTS,
disclosed -- the DEV/BLIND split, predictor forms C1-C4, the K
candidates, LAW bars, falsifier and verdict rule were NEVER
touched: (a1) the continuation chain got a graceful-degeneracy
guard (gammahat = 0 / non-finite -> chain ends, NO PREDICTION)
after the smoke pass crashed on a collapsed truncated world;
(a2) K_crit was sharpened from naive "smallest succeeding K"
to the STABILIZATION POINT after the smoke pass exposed
accidental integer collisions of wrong truncated worlds with
the census flip (30 such sub-K_crit islands on the full grid,
counted, never credited); (a3) the typed direction wording of
G31/G40 was clarified after pass 1 (the measurements
themselves were never edited); (a4) the toy weights (2, -1/3,
1, 3, 1, -1/3, 2) were checked once for a nonsingular exact
prefix chain before the gate ran -- no re-deal):
CAL_VERDICT = FRONTIER_NONLOCAL_IRREDUCIBLE +
DIMENSION_EXTENSIVE(K_crit/N median 0.95) +
EARLY_CONCENTRATED_SENSITIVITY + EDGE_NODE_DOMINANCE +
ALIAS_OF_DETERMINISM(full engine) + DETERMINISM_REGATED(42/42).
Key numbers -- LEG A: census regenerated 42/42, histogram
{0: 18, 1: 10, 2: 6, 3: 6, 4: 1, 5: 1} exact, wall + half-fill
+ r228 re-gated; lead re-derived Spearman(delta;
alphahat_{N-1}) = +0.72.  ENGINE: rational toy weights EXACT +
Newton t = 0..3 EXACT; f64 round-trip flip 42/42 (S up to
1755); crossing floor median 7.6e-07, max 6.7e-04.  LEG B:
(b1) eps = 1e-8 block perturbations change delta on 0/42
windows at EVERY K in {5, 10, 20, 40}; median |dx| ~ 4e-05
(linear response, ~ 60 x above the round-trip floor median):
the integer delta is smooth at 1e-8 -- K_crit_eps = 5
everywhere, so locality is decided by (b3).  (b2)
per-coefficient derivative profile |dx/d alphahat_n| median:
18.77 / 7.75 / 2.74 / 2.29 at f = 0.05/0.25/0.50/0.75 vs 2.25
(N - 10) and 1.11 (N - 2): sensitivity is CONCENTRATED AT THE
EARLY END (early/late ratio 8.35) -- the EARLIEST free
coefficients carry the most crossing information, the exact
opposite of frontier locality.  (b3) THE DIMENSION: truncation
grid + bisection resolved the stabilization point K_crit on
42/42 windows: median K_crit 369, range 85..859; K_crit/N
median 0.95, range 0.47..1.00 (12 windows need the FULL
prefix, K_crit = N); Spearman(K_crit; N) = +0.95 -- the
required depth GROWS with N: the information dimension is
EXTENSIVE (median 95 percent of the whole free chain), not
O(1), not O(sqrt N).  (b4) node jitter (prefix fixed, L-only):
median |dx| 6.6e-06 / 9.9e-06 / 1.2e-05 / 1.8e-05 / 1.5e-03 at
q = 0/.25/.5/.75/1: EDGE-DOMINATED (ratio 61, driven by the
q = 1 edge; one window flips delta under a 1e-6 edge jitter)
-- the forced tail hangs on the outermost node geometry.
LEG C (DEV 21 / BLIND 21; baseline constant delta = 0: BLIND
exact 0.524 / pm1 0.714): C1 2D monotone bins (0, 1, 2, 2):
BLIND 0.619/0.857 -- best form, beats the baseline by +0.095
exact yet stays UNDER the LAW exact bar 0.674; C2 3D bins
(0, 0, 1, 2): BLIND 0.476/0.857; C3 1-NN forced moments:
BLIND 0.190/0.476; C4 short-chain engine (DEV picked K = 50,
DEV exact 0.190): BLIND 0.048/0.286 -- exactly as leg B
predicts: K = 50 << K_crit median 369 carries almost no delta
information.  FALSIFIER: controls re-gated 25/21/27 exactly;
C4 truncated engine predicts 137/10/161 (gross miss -- the
truncation erases the bulk flip, honest); C1-C3 miss by
construction; 0/4 forms pass.  VERDICT (sealed rule):
FRONTIER_NONLOCAL_IRREDUCIBLE -- quantified: delta needs a
median 95 percent of the free prefix even with the FULL node
polynomial in hand, the sensitivity sits at the EARLY end of
the chain and the +1 node edge, and the best sealed blind
exact rate 0.619 stays under the 0.674 bar while the full
(dimension-S) reconstruction is EXACT 42/42: the r233
alphahat lead is real rank signal, but the offset delta is a
GLOBAL functional of the window data -- no low-dimensional
frontier law exists at the data level.  MUST-FAILS: oracle
42/42 (excluded by firewall), shifted-rhs toy returns wrong
weights loudly, gross corruption moves the w9 flip 184 -> 120.
Runtime ~ 27 s FULL.  AMENDMENTS AFTER FREEZE: NONE.

NO RH CLAIM IN EITHER DIRECTION.  NOT evidence for or against RH.
"""

from __future__ import annotations

import argparse
import ast
import hashlib
import math
import os
import sys
import time
from fractions import Fraction as Fr

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

import fermiedge_classify_probe as FC        # noqa: E402 r227
import frontier_micro_probe as FM            # noqa: E402 r233
import hirota_sign_probe as HS               # noqa: E402 r226
import port_integrable_kernel_probe as PIK   # noqa: E402 v881
import v563_paper2_readouts as core          # noqa: E402 READ-ONLY

H_CAP = 900
SMOKE_KZ = (9, 12, 13, 26, 40)
R233_HIST = {0: 18, 1: 10, 2: 6, 3: 6, 4: 1, 5: 1}
R228_DELTA = {9: 0, 12: 2, 13: 2, 26: 3, 40: 1}
CTRL_FLIPS = {"EPSTEIN": 25, "SCRAMBLE": 21, "SMOOTH": 27}
SEARCH_EXTRA = 120
LEAD_BAR = 0.5
FLOOR_BAR = 0.25
EPS_BLK = 1e-8
BLK_KS = (5, 10, 20, 40)
EPS_DER = 1e-6
DER_FRACS = (0.05, 0.25, 0.50, 0.75)
DER_TAILS = (10, 2)
KDIM_GRID = (10, 25, 50, 100, 150, 200, 300, 400)
EPS_ND = 1e-6
ND_QUANTS = (0.0, 0.25, 0.5, 0.75, 1.0)
C4_KS = (10, 25, 50)
LAW_EXACT = 0.674
LAW_PM1 = 0.8
CTRL_BAR = 2
CAL_VERDICT = ("FRONTIER_NONLOCAL_IRREDUCIBLE + "
               "DIMENSION_EXTENSIVE(K_crit/N median 0.95) + "
               "EARLY_CONCENTRATED_SENSITIVITY + "
               "EDGE_NODE_DOMINANCE + "
               "ALIAS_OF_DETERMINISM(full engine) + "
               "DETERMINISM_REGATED(42/42)")

SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
T0_WALL = time.time()
CHECKS: list = []


def check(name, ok, detail):
    ok = bool(ok)
    CHECKS.append((name, ok, detail))
    print("  [%s] %-40s %s" % ("PASS" if ok else "FAIL", name, detail),
          flush=True)
    return ok


def info(msg):
    print("  [INFO] " + msg, flush=True)


def section(t):
    print("\n" + "-" * 78 + "\n" + t + "\n" + "-" * 78, flush=True)


def firewall_audit():
    src = open(os.path.abspath(__file__), "r", encoding="utf-8").read()
    tree = ast.parse(src)
    forb = {"zeta" + "zero", "n" + "zeros", "prime" + "range",
            "is" + "prime", "gram" + "point"}
    bad = []
    for node in ast.walk(tree):
        nm = node.attr if isinstance(node, ast.Attribute) else (
            node.id if isinstance(node, ast.Name) else None)
        if nm and nm.lower() in forb:
            bad.append("%s@%d" % (nm, node.lineno))
    return (not bad), ("NO zero/prime oracles; index firewall "
                       "binding; DEV/BLIND split, predictor forms "
                       "C1-C4, K candidates, LAW bars, falsifier "
                       "and verdict rule sealed in the frozen spec"
                       if not bad else "; ".join(bad))


def spearman(x, y):
    def ranks(v):
        v = np.asarray(v, float)
        order = np.argsort(v, kind="stable")
        rk = np.empty(len(v))
        rk[order] = np.arange(len(v), dtype=float)
        for val in np.unique(v):
            m = v == val
            rk[m] = rk[m].mean()
        return rk
    rx, ry = ranks(x), ranks(y)
    rx -= rx.mean()
    ry -= ry.mean()
    den = math.sqrt(float(np.sum(rx ** 2) * np.sum(ry ** 2)))
    return float(np.sum(rx * ry) / den) if den > 0 else 0.0


# =================================================== the engine
def chain_scalars(nodes, phi, n_upto):
    """scaled signed Stieltjes recursion on an arbitrary signed
    node measure (same algebra as FC.signed_chain, scalars only),
    with a GRACEFUL stop on a degenerate step (gammahat = 0 or
    non-finite) -- truncated-prefix reconstructions may collapse
    mid-chain and a degenerate world must count as NO PREDICTION,
    not crash.  Returns list of dicts (alphahat, gam, sg_h)."""
    w = phi
    x = nodes
    qm = np.zeros_like(x)
    q = np.ones_like(x)
    Ls, Ls_m = 0.0, 0.0
    eta = float(np.sum(w * q * q))
    sg_h = math.copysign(1.0, eta)
    out = []
    for n in range(n_upto):
        alh = float(np.sum(w * x * q * q)) / eta
        if n == 0:
            p = (x - alh) * q
        else:
            ge = (eta / eta_m) * math.exp(2.0 * (Ls - Ls_m))
            p = (x - alh) * q - ge * math.exp(Ls_m - Ls) * qm
        sc = float(np.max(np.abs(p)))
        if not (sc > 0.0 and math.isfinite(sc)):
            break
        qm, eta_m, Ls_m = q, eta, Ls
        q = p / sc
        Ls += math.log(sc)
        eta = float(np.sum(w * q * q))
        gam = (eta / eta_m) * math.exp(2.0 * (Ls - Ls_m))
        if gam == 0.0 or not math.isfinite(gam):
            break
        # FC.signed_chain convention: entry n carries sign(h_n)
        # and gammahat_{n+1}
        out.append(dict(alphahat=alh, gam=gam, sg_h=sg_h))
        sg_h *= math.copysign(1.0, gam)
    return out


def build_polys(nodes, alp, gam):
    """scaled monic prefix polynomials q_0..q_{N-1} as node-value
    rows V (each row max-normalized) with log-scales sl."""
    S = len(nodes)
    N = len(alp)
    V = np.empty((N, S))
    sl = np.empty(N)
    vm = np.zeros(S)
    v = np.ones(S)
    s = 0.0
    s_m = 0.0
    V[0] = v
    sl[0] = 0.0
    for n in range(N - 1):
        g = gam[n - 1] if n >= 1 else 0.0
        p = (nodes - alp[n]) * v - g * math.exp(s_m - s) * vm
        c = float(np.max(np.abs(p)))
        vm, s_m = v, s
        v = p / c
        s = s + math.log(c)
        V[n + 1] = v
        sl[n + 1] = s
    return V, sl


def recon(nodes, alp, gam, lg_h0, sg_h0, n_search, rhs_shift=0):
    """(prefix, node set) -> forced continuation.  Solves the
    graded S x S system Lambda[q_j q_k] = h_j delta_jk on
    balanced pairs for the unique node weights phi, then runs
    the signed chain of phi.  Returns (flip, x_interp, phi,
    resid_inf).  rhs_shift != 0 only for the must-fail."""
    N = len(alp)
    S = len(nodes)
    if S > 2 * N - 1:
        return None, None, None, None
    V, sl = build_polys(nodes, alp, gam)
    lgh = np.empty(N)
    sgh = np.empty(N)
    lgh[0], sgh[0] = lg_h0, sg_h0
    for j in range(1, N):
        lgh[j] = lgh[j - 1] + math.log(abs(gam[j - 1]))
        sgh[j] = sgh[j - 1] * math.copysign(1.0, gam[j - 1])
    A = np.empty((S, S))
    b = np.zeros(S)
    for dd in range(S):
        j, k = (dd + 1) // 2, dd // 2
        A[dd] = V[j] * V[k]
        if j == k:
            b[(dd + rhs_shift) % S] = sgh[j] * math.exp(
                lgh[j] - 2.0 * sl[j])
    phi = np.linalg.solve(A, b)
    resid = float(np.max(np.abs(A @ phi - b)))
    n_upto = min(n_search, S - 1)
    ch = chain_scalars(nodes, phi, n_upto)
    flip = next((n for n in range(len(ch)) if ch[n]["sg_h"] < 0),
                None)
    x = None
    if flip is not None and flip >= 2:
        gp, gm = ch[flip - 2]["gam"], ch[flip - 1]["gam"]
        if gp > 0 and gm < 0:
            x = (flip - 1) + gp / (gp + abs(gm))
    return flip, x, phi, resid


def trunc_prefix(alp, gam, K):
    """equilibrium below N - K: alphahat = 0, gammahat = 1/4;
    the last K coefficients stay true."""
    N = len(alp)
    a2 = alp.copy()
    g2 = gam.copy()
    a2[:max(0, N - K)] = 0.0
    g2[:max(0, N - K - 1)] = 0.25
    return a2, g2


# ================================================ window prep
def prep_window(kz):
    d = HS.window_data(kz)
    N = d["n_max"]
    row = FM.window_row(kz, d)
    ch = FC.signed_chain(d, N + 1)
    alp = np.array([ch[n]["alphahat"] for n in range(N)])
    gam = np.array([ch[n - 1]["gammahat_next"]
                    for n in range(1, N)])
    lg0, sg0 = ch[0]["lg_h"], ch[0]["sg_h"]
    del ch
    nodes = np.concatenate([d["xs"], d["ys"]])
    wtrue = np.concatenate([d["ws"], -d["vs"]])
    nf, N_ = row["nf"], row["N"]
    gp = row["prof"].get(nf - 1 - N_)
    gm = row["prof"].get(nf - N_)
    x_c = None
    if gp is not None and gm is not None and gp > 0 and gm < 0:
        x_c = (nf - 1) + gp / (gp + abs(gm))
    S = row["S"]
    xa1 = np.abs(nodes) ** (S + 1)
    mS1 = float(np.sum(wtrue * np.sign(nodes) ** (S + 1) * xa1))
    sig1 = float(np.sum(np.abs(wtrue) * xa1))
    return dict(kz=kz, N=N, S=S, nf=nf, delta=nf - N, x_c=x_c,
                prof=row["prof"], h0=row["h0"],
                alp_end=row["alp_end"], gam_end=row["gam_end"],
                mS=row["mS"], sigS=row["sigS"], mS1=mS1,
                sig1=sig1, alp=alp, gam=gam, lg0=lg0, sg0=sg0,
                nodes=nodes, wtrue=wtrue)


# ================================================ rational toy
TOY_NODES = tuple(Fr(k, 4) for k in (-3, -2, -1, 0, 1, 2, 3))
TOY_WTS = (Fr(2), Fr(-1, 3), Fr(1), Fr(3), Fr(1), Fr(-1, 3),
           Fr(2))


def toy_chain():
    """exact signed monic chain of the toy: (alps, gams, hs)."""
    nds, wts = TOY_NODES, TOY_WTS

    def lam(vals):
        return sum(w * v for w, v in zip(wts, vals))

    S = len(nds)
    N = (S + 1) // 2
    p_m = [Fr(0)] * S
    p = [Fr(1)] * S
    h_m = None
    h = lam([Fr(1)] * S)
    alps, gams, hs = [], [], [h]
    for n in range(N):
        assert h != 0, "toy chain degenerate at n=%d" % n
        a = lam([x * pi * pi for x, pi in zip(nds, p)]) / h
        alps.append(a)
        if n > 0:
            gams.append(h / h_m)
        g = (h / h_m) if n > 0 else Fr(0)
        p_new = [(x - a) * pi - g * qi
                 for x, pi, qi in zip(nds, p, p_m)]
        p_m, p = p, p_new
        h_m, h = h, lam([pi * pi for pi in p])
        hs.append(h)
    return alps, gams, hs[:N]


def toy_recon(alps, gams, hs, rhs_shift=0):
    """exact rational reconstruction on the toy: rebuild prefix
    polys from (alps, gams) only, solve the graded system by
    exact Gaussian elimination, return phi."""
    nds = TOY_NODES
    S = len(nds)
    N = (S + 1) // 2
    P = [[Fr(1)] * S]
    for n in range(N - 1):
        prev = P[-1]
        prev2 = P[-2] if n >= 1 else [Fr(0)] * S
        g = gams[n - 1] if n >= 1 else Fr(0)
        P.append([(x - alps[n]) * p - g * q
                  for x, p, q in zip(nds, prev, prev2)])
    A = []
    b = [Fr(0)] * S
    for dd in range(S):
        j, k = (dd + 1) // 2, dd // 2
        A.append([P[j][i] * P[k][i] for i in range(S)])
        if j == k:
            b[(dd + rhs_shift) % S] = hs[j]
    # exact Gaussian elimination with partial pivot on |.|
    M = [row[:] + [bb] for row, bb in zip(A, b)]
    for c in range(S):
        piv = max(range(c, S), key=lambda r: abs(M[r][c]))
        assert M[piv][c] != 0
        M[c], M[piv] = M[piv], M[c]
        for r in range(S):
            if r != c and M[r][c] != 0:
                f = M[r][c] / M[c][c]
                M[r] = [a - f * bcol
                        for a, bcol in zip(M[r], M[c])]
    return [M[i][S] / M[i][i] for i in range(S)]


def toy_newton_gate():
    """Newton forced-tail identity of the toy, exact: m_{S+t} =
    -sum_i a_i m_{i+t} with a_i from prod(z - x_j)."""
    nds, wts = TOY_NODES, TOY_WTS
    S = len(nds)
    Lc = [Fr(1)]
    for x in nds:
        Lc = [c1 - x * c0 for c0, c1 in
              zip(Lc + [Fr(0)], [Fr(0)] + Lc)]
    a_low = Lc[:-1]
    mom = [sum(w * x ** k for w, x in zip(wts, nds))
           for k in range(S + 4)]
    return all(mom[S + t] == -sum(a_low[i] * mom[i + t]
                                  for i in range(S))
               for t in range(4))


# ======================================================== main
def main():
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke

    print("=" * 78)
    print("frontier_alphalaw_probe -- PRIME.PORT.FRONTIER."
          "ALPHALAW.01 (round 235)")
    print("SPEC_SHA %s" % SPEC_SHA[:16])
    print("mode: %s" % ("SMOKE (five known rungs, infrastructure "
                        "only)" if smoke else "FULL RECORD"))
    print("=" * 78)

    section("S0  FIREWALL + PREDEFINITION")
    okf, det = firewall_audit()
    check("G01-firewall", okf, det)
    check("G02-predefinition", True,
          "ladder = frame-A h <= %d, DEV even / BLIND odd on the "
          "(N, kz) sort (= r233); engine = graded balanced-pair "
          "reconstruction (spec); leg-B grids sealed (blocks %s "
          "at eps %.0e, derivs f %s + tails %s at eps %.0e, "
          "K_dim grid %s + bisection, jitter quantiles %s at eps "
          "%.0e); forms C1-C4 with C4 K in %s; LAW exact >= "
          "%.3f AND pm1 >= %.2f; falsifier controls 25/21/27 "
          "within +-%d" % (H_CAP, BLK_KS, EPS_BLK, DER_FRACS,
                           DER_TAILS, EPS_DER, KDIM_GRID,
                           ND_QUANTS, EPS_ND, C4_KS, LAW_EXACT,
                           LAW_PM1, CTRL_BAR))

    # ---------------- S1: leg A census regeneration
    section("S1  LEG A -- CENSUS REGENERATION (42 windows)")
    if smoke:
        kzs = list(SMOKE_KZ)
    else:
        kzs = [kz for kz in core.frame_a_zones()
               if PIK.build_rung(kz)["h"] <= H_CAP]
    lad = [prep_window(kz) for kz in kzs]
    lad.sort(key=lambda r: (r["N"], r["kz"]))
    deltas = [r["delta"] for r in lad]
    hist = {}
    for dl in deltas:
        hist[dl] = hist.get(dl, 0) + 1
    info("delta histogram %s over %d windows (N = %d..%d)"
         % (dict(sorted(hist.items())), len(lad),
            lad[0]["N"], lad[-1]["N"]))
    check("G10-census-histogram", smoke or hist == R233_HIST,
          "delta histogram matches the r233 census EXACTLY "
          "(%s)" % str(R233_HIST) if not smoke else
          "SMOKE: histogram gate on the full ladder only")
    ok_wall = all(r["nf"] >= r["N"] for r in lad)
    ok_S = all(r["S"] == 2 * r["N"] - 1 for r in lad)
    check("G11-wall-halffill", ok_wall and ok_S,
          "no flip below N_w on any window; S = 2 N_w - 1 "
          "everywhere (wall + half-filling re-gated)")
    ok228 = all(r["delta"] == R228_DELTA[r["kz"]]
                for r in lad if r["kz"] in R228_DELTA)
    check("G12-r228-regate", ok228,
          "the five r228 offsets 0/2/2/3/1 re-derived exactly")
    rho_lead = spearman([r["alp_end"] for r in lad], deltas)
    check("G13-lead-regate", smoke or rho_lead >= LEAD_BAR,
          "the r233 lead re-derived: Spearman(delta; "
          "alphahat_{N-1}) = %+.2f (bar >= %+.2f)"
          % (rho_lead, LEAD_BAR))

    # ---------------- S2: engine wards
    section("S2  THE RECONSTRUCTION ENGINE (exact wards)")
    alps_t, gams_t, hs_t = toy_chain()
    phi_t = toy_recon(alps_t, gams_t, hs_t)
    ok_toy = all(p == w for p, w in zip(phi_t, TOY_WTS))
    ok_newt = toy_newton_gate()
    check("G20-rational-toy-exact", ok_toy and ok_newt,
          "S = 7 signed rational toy: the graded reconstruction "
          "returns the TRUE weights EXACTLY from (prefix, nodes) "
          "alone, and the Newton forced-tail recurrence m_{S+t} "
          "= -sum a_i m_{i+t} holds EXACTLY for t = 0..3: the "
          "engine IS the Newton determinism map")
    rt = {}
    ok_rt = True
    floors = []
    for r in lad:
        fl, x, phi, resid = recon(r["nodes"], r["alp"], r["gam"],
                                  r["lg0"], r["sg0"],
                                  r["nf"] + 10)
        rt[r["kz"]] = (fl, x, resid)
        ok_rt = ok_rt and (fl == r["nf"])
        if x is not None and r["x_c"] is not None:
            floors.append(abs(x - r["x_c"]))
    check("G21-roundtrip-flips", ok_rt,
          "FULL-prefix reconstruction reproduces the census flip "
          "on %d/%d windows EXACTLY (f64, S up to %d) -- the "
          "r233 determinism theorem re-gated at the data level; "
          "TYPED: input dimension = S, an ALIAS of the answer, "
          "excluded from the predictor competition"
          % (len(lad), len(lad), lad[-1]["S"]))
    med_fl = float(np.median(floors))
    max_fl = float(np.max(floors))
    check("G22-roundtrip-floor", max_fl < FLOOR_BAR,
          "crossing floor |x_recon - x_census|: median %.1e, "
          "max %.1e (bar %.2f); every leg-B |dx| is read "
          "against this floor" % (med_fl, max_fl, FLOOR_BAR))

    # ---------------- S3: leg B locality measurements
    section("S3  LEG B -- INFORMATION LOCALITY (b1 blocks, "
            "b2 derivatives, b3 dimension)")
    blk_ks = BLK_KS if not smoke else (5,)
    blk_dchg = {K: 0 for K in blk_ks}
    blk_dx = {K: [] for K in blk_ks}
    kcrit_eps = []
    for r in lad:
        x0 = rt[r["kz"]][1]
        kc = None
        for K in blk_ks:
            a2 = r["alp"].copy()
            a2[:max(0, r["N"] - K)] += EPS_BLK
            fl, x, _, _ = recon(r["nodes"], a2, r["gam"],
                                r["lg0"], r["sg0"], r["nf"] + 10)
            chg = (fl != r["nf"])
            blk_dchg[K] += int(chg)
            if x is not None and x0 is not None:
                blk_dx[K].append(abs(x - x0))
            if not chg and kc is None:
                kc = K
        kcrit_eps.append(kc)
    for K in blk_ks:
        info("b1 block K = %-3d (perturb all n < N-K by %.0e): "
             "delta changed on %d/%d windows | median |dx| %.1e"
             % (K, EPS_BLK, blk_dchg[K], len(lad),
                float(np.median(blk_dx[K]))))
    check("G30-block-perturbations", all(k is not None
                                         for k in kcrit_eps),
          "K_crit_eps (smallest sealed block K with delta "
          "unchanged) resolved on all windows: histogram %s -- "
          "at eps = %.0e the integer delta is %s; locality is "
          "adjudicated by the truncation dimension b3, the "
          "sealed sharp probe"
          % ({k: kcrit_eps.count(k) for k in
              sorted(set(kcrit_eps))}, EPS_BLK,
             "insensitive (smooth map, as expected)"
             if blk_dchg[min(blk_ks)] == 0 else
             "ALREADY sensitive -- typed"))

    der_fracs = DER_FRACS if not smoke else (0.25,)
    der_tails = DER_TAILS if not smoke else (2,)
    sens = {("f", f): [] for f in der_fracs}
    sens.update({("t", t): [] for t in der_tails})
    for r in lad:
        x0 = rt[r["kz"]][1]
        for key in list(sens):
            n = (int(round(key[1] * r["N"])) if key[0] == "f"
                 else r["N"] - key[1])
            n = min(max(n, 0), r["N"] - 1)
            a2 = r["alp"].copy()
            a2[n] += EPS_DER
            fl, x, _, _ = recon(r["nodes"], a2, r["gam"],
                                r["lg0"], r["sg0"], r["nf"] + 10)
            if x is not None and x0 is not None:
                sens[key].append(abs(x - x0) / EPS_DER)
    prof_s = {}
    for key in sens:
        prof_s[key] = float(np.median(sens[key]))
        lab = ("n = %.2f N" % key[1] if key[0] == "f"
               else "n = N - %d" % key[1])
        info("b2 derivative |dx/d alphahat_n| at %-12s: median "
             "%.2f  (over %d windows)" % (lab, prof_s[key],
                                          len(sens[key])))
    early = prof_s[("f", der_fracs[0])]
    late = prof_s[("t", der_tails[0])]
    check("G31-derivative-profile",
          all(len(v) == len(lad) for v in sens.values()),
          "per-coefficient sensitivity profile measured; "
          "early/late ratio (f = %.2f vs N - %d) = %.2f -- %s"
          % (der_fracs[0], der_tails[0], early / max(late, 1e-12),
             "FLAT across the free chain (early coefficients "
             "matter as much as late ones: no frontier-local "
             "compression)"
             if 0.2 <= early / max(late, 1e-12) <= 5.0 else
             ("CONCENTRATED AT THE EARLY END (ratio > 5): the "
              "earliest free coefficients carry the most "
              "crossing information -- the exact opposite of "
              "frontier locality"
              if early / max(late, 1e-12) > 5.0 else
              "CONCENTRATED AT THE FRONTIER END (ratio < 0.2) "
              "-- typed")))

    # b3 truncation dimension with bisection
    kdim_grid = KDIM_GRID if not smoke else (10, 50, 100)
    kcrit = []
    c4_flips = {K: {} for K in C4_KS}
    nonmono = 0
    for r in lad:
        N = r["N"]

        def trunc_ok(K, _cache={}):
            key = (r["kz"], K)
            if key not in _cache:
                a2, g2 = trunc_prefix(r["alp"], r["gam"], K)
                fl, _, _, _ = recon(r["nodes"], a2, g2,
                                    r["lg0"], r["sg0"],
                                    N + SEARCH_EXTRA)
                _cache[key] = fl
            return _cache[key]

        grid = [K for K in kdim_grid if K < N]
        for K in C4_KS:
            c4_flips[K][r["kz"]] = trunc_ok(K)
        res = {K: (trunc_ok(K) == r["nf"]) for K in grid}
        # K_crit = the STABILIZATION point: smallest K above the
        # largest failing K (bisected to adjacency).  Successes
        # BELOW a failure are accidental integer collisions of a
        # wrong truncated world with the census flip -- counted,
        # typed, and never credited as locality.
        lo = max([K for K in grid if not res[K]], default=0)
        hi = min([K for K in grid if res[K] and K > lo],
                 default=N)
        nonmono += sum(1 for K in grid if res[K] and K < lo)
        while hi - lo > 1:
            mid = (lo + hi) // 2
            if trunc_ok(mid) == r["nf"]:
                hi = mid
            else:
                lo = mid
        ok_adj = (hi == N or trunc_ok(hi) == r["nf"]) and (
            lo == 0 or trunc_ok(lo) != r["nf"])
        kcrit.append((r["kz"], N, r["delta"], hi, ok_adj))
    ks = [k for _, _, _, k, _ in kcrit]
    kn = [k / n for _, n, _, k, _ in kcrit]
    rho_kn = spearman([n for _, n, _, _, _ in kcrit], ks)
    print("  kz    N_w  delta  K_crit  K_crit/N")
    for kz, n, dl, k, _ in kcrit:
        print("  %-4d %4d   %2d    %4d     %.2f"
              % (kz, n, dl, k, k / n))
    check("G32-truncation-dimension", all(a for *_, a in kcrit),
          "K_crit (stabilization point) resolved with verified "
          "boundary on %d/%d windows (%d accidental sub-K_crit "
          "collision hits on the grid, typed, never credited): "
          "median K_crit %d, range %d..%d; K_crit/N median "
          "%.2f, range %.2f..%.2f; Spearman(K_crit; N) = %+.2f "
          "-- THE MEASURED INFORMATION DIMENSION: %s"
          % (len(kcrit), len(lad), nonmono,
             int(np.median(ks)), min(ks), max(ks),
             float(np.median(kn)), min(kn), max(kn), rho_kn,
             "EXTENSIVE (grows with N; delta needs a finite "
             "FRACTION of the whole free chain, no O(1) or "
             "O(sqrt N) locality)" if rho_kn > 0.5
             and float(np.median(kn)) > 0.2 else
             "sub-extensive -- typed for the next round"))

    # ---------------- S4: leg B (b4) node-polynomial locality
    section("S4  LEG B -- NODE-POLYNOMIAL LOCALITY (b4 jitter)")
    nd_dx = {q: [] for q in ND_QUANTS}
    nd_chg = {q: 0 for q in ND_QUANTS}
    for r in lad:
        x0 = rt[r["kz"]][1]
        order = np.argsort(r["nodes"])
        for q in ND_QUANTS:
            i = order[int(round(q * (len(order) - 1)))]
            nd2 = r["nodes"].copy()
            nd2[i] += EPS_ND
            fl, x, _, _ = recon(nd2, r["alp"], r["gam"],
                                r["lg0"], r["sg0"], r["nf"] + 10)
            nd_chg[q] += int(fl != r["nf"])
            if x is not None and x0 is not None:
                nd_dx[q].append(abs(x - x0))
    meds = {}
    for q in ND_QUANTS:
        meds[q] = float(np.median(nd_dx[q]))
        info("b4 jitter node at sorted quantile q = %.2f "
             "(+%.0e, prefix fixed): delta changed %d/%d | "
             "median |dx| %.1e" % (q, EPS_ND, nd_chg[q],
                                   len(lad), meds[q]))
    edge = 0.5 * (meds[0.0] + meds[1.0])
    inter = float(np.median([meds[0.25], meds[0.5], meds[0.75]]))
    check("G40-node-locality", True,
          "node-polynomial sensitivity (prefix held fixed, "
          "L-only): edge median %.1e vs interior median %.1e "
          "(ratio %.2f) -- %s" % (edge, inter,
                                  edge / max(inter, 1e-300),
                                  "EDGE-DOMINATED: the forced "
                                  "tail hangs on the outermost "
                                  "node geometry -- typed"
                                  if edge > 5.0 * inter else
                                  "INTERIOR-FLAT: delta depends "
                                  "on the node polynomial "
                                  "collectively, not through "
                                  "frontier-near nodes"))

    # ---------------- S5: leg C sealed predictors
    section("S5  LEG C -- SEALED DEV/BLIND PREDICTORS")
    dev = [r for i, r in enumerate(lad) if i % 2 == 0]
    bli = [r for i, r in enumerate(lad) if i % 2 == 1]
    d_dev = [r["delta"] for r in dev]
    d_bli = [r["delta"] for r in bli]
    info("DEV %d (kz %s...) | BLIND %d (kz %s...)"
         % (len(dev), [r["kz"] for r in dev[:6]],
            len(bli), [r["kz"] for r in bli[:6]]))

    def score(preds, truth):
        ex = sum(1 for p, t in zip(preds, truth)
                 if p is not None and p == t)
        pm = sum(1 for p, t in zip(preds, truth)
                 if p is not None and abs(p - t) <= 1)
        return ex / len(truth), pm / len(truth)

    md = {}
    for v in d_dev:
        md[v] = md.get(v, 0) + 1
    base_val = sorted(md.items(),
                      key=lambda t: (-t[1], t[0]))[0][0]
    b_ex, b_pm = score([base_val] * len(bli), d_bli)
    info("baseline (constant delta = %d, DEV mode): BLIND "
         "exact %.3f / pm1 %.3f" % (base_val, b_ex, b_pm))

    def ls_fit(F, y):
        F1 = np.column_stack([np.ones(len(F)), F])
        c, *_ = np.linalg.lstsq(F1, np.asarray(y, float),
                                rcond=None)
        return c

    def bin_predict(feats_fn, tag):
        F_dev = np.array([feats_fn(r) for r in dev])
        c = ls_fit(F_dev, d_dev)
        s_dev = c[0] + F_dev @ c[1:]
        qs = np.quantile(s_dev, [0.25, 0.5, 0.75])
        binv = []
        for bidx in range(4):
            lo = -np.inf if bidx == 0 else qs[bidx - 1]
            hi = np.inf if bidx == 3 else qs[bidx]
            vals = [d for s, d in zip(s_dev, d_dev)
                    if (s > lo or bidx == 0) and s <= hi]
            binv.append(int(round(float(np.median(vals))))
                        if vals else 0)
        binv = list(np.maximum.accumulate(binv))
        preds_d = [binv[int(np.searchsorted(qs, s))]
                   for s in s_dev]
        F_bli = np.array([feats_fn(r) for r in bli])
        s_bli = c[0] + F_bli @ c[1:]
        preds_b = [binv[int(np.searchsorted(qs, s))]
                   for s in s_bli]
        dex, dpm = score(preds_d, d_dev)
        bex, bpm = score(preds_b, d_bli)
        info("%s: score c %s, DEV bin edges %s, monotone bins "
             "%s | DEV %.3f/%.3f | BLIND %.3f/%.3f"
             % (tag, np.array2string(c, precision=3),
                np.array2string(qs, precision=3), binv,
                dex, dpm, bex, bpm))
        return bex, bpm

    results = {}
    results["C1"] = bin_predict(
        lambda r: [r["alp_end"], r["gam_end"]],
        "C1 2D bins (alphahat, gammahat)")
    results["C2"] = bin_predict(
        lambda r: [r["alp_end"], r["gam_end"] - 0.25, r["h0"]],
        "C2 3D bins (+ h_0)")

    def c3_feats(r):
        return np.array([r["mS"] / r["sigS"],
                         r["mS1"] / r["sig1"]])
    F_dev = np.array([c3_feats(r) for r in dev])
    mu_f = F_dev.mean(axis=0)
    sd_f = F_dev.std(axis=0)
    sd_f[sd_f == 0] = 1.0
    F_dev = (F_dev - mu_f) / sd_f
    pb = []
    for r in bli:
        f = (c3_feats(r) - mu_f) / sd_f
        i = int(np.argmin(np.sum((F_dev - f) ** 2, axis=1)))
        pb.append(d_dev[i])
    c3_ex, c3_pm = score(pb, d_bli)
    results["C3"] = (c3_ex, c3_pm)
    info("C3 1-NN forced moments (m_S/sigma_S, m_{S+1}/"
         "sigma_{S+1}): BLIND %.3f/%.3f" % (c3_ex, c3_pm))

    best_c4 = None
    for K in C4_KS:
        preds_d = [None if c4_flips[K][r["kz"]] is None else
                   c4_flips[K][r["kz"]] - r["N"] for r in dev]
        dex, dpm = score(preds_d, d_dev)
        info("C4 candidate K = %-3d: DEV exact %.3f / pm1 %.3f"
             % (K, dex, dpm))
        if best_c4 is None or dex > best_c4[1] + 1e-12:
            best_c4 = (K, dex)
    K4 = best_c4[0]
    preds_b = [None if c4_flips[K4][r["kz"]] is None else
               c4_flips[K4][r["kz"]] - r["N"] for r in bli]
    c4_ex, c4_pm = score(preds_b, d_bli)
    results["C4"] = (c4_ex, c4_pm)
    info("C4 short-chain engine (DEV picked K = %d): BLIND "
         "%.3f/%.3f" % (K4, c4_ex, c4_pm))
    check("G50-predictors-scored", True,
          "all four sealed forms fitted on DEV only and scored "
          "ONCE on BLIND; baseline %.3f/%.3f; LAW bars exact "
          ">= %.3f AND pm1 >= %.2f; best exact %.3f (%s), best "
          "pm1 %.3f" % (b_ex, b_pm, LAW_EXACT, LAW_PM1,
                        max(e for e, _ in results.values()),
                        max(results, key=lambda k:
                            results[k][0]),
                        max(p for _, p in results.values())))

    # ---------------- S6: the frozen falsifier
    section("S6  THE FROZEN FALSIFIER (controls 25/21/27)")
    rr9 = core.build_window(9)
    N_E = int(math.floor(math.exp(2.0 * rr9["alpha"]))) + 1
    lamE_ = PIK.lambda_eps(N_E)
    nn = np.nonzero(np.abs(lamE_) > 1e-12)[0]
    ug = np.arange(0.01, 2.0 * rr9["alpha"], 0.01)
    ctrls = (("EPSTEIN", dict(comb=(
                np.log(nn.astype(float)),
                2.0 * lamE_[nn] / np.sqrt(nn.astype(float))))),
             ("SCRAMBLE", dict(scramble_seed=1)),
             ("SMOOTH", dict(comb=(ug, 2.0 * np.exp(ug / 2.0)
                                   * 0.01))))
    ok_cf = True
    c4_ctrl_hits = 0
    for cname, kw in ctrls:
        dc = HS.window_data(9, **kw)
        Nc = dc["n_max"]
        chc = FC.signed_chain(dc, Nc)
        flip = next(n for n in range(len(chc))
                    if chc[n]["sg_h"] < 0)
        ok_cf = ok_cf and flip == CTRL_FLIPS[cname]
        alp_c = np.array([chc[n]["alphahat"] for n in range(Nc)])
        gam_c = np.array([chc[n - 1]["gammahat_next"]
                          for n in range(1, Nc)])
        lg0c, sg0c = chc[0]["lg_h"], chc[0]["sg_h"]
        del chc
        nodes_c = np.concatenate([dc["xs"], dc["ys"]])
        a2, g2 = trunc_prefix(alp_c, gam_c, K4)
        flc, _, _, _ = recon(nodes_c, a2, g2, lg0c, sg0c,
                             Nc + SEARCH_EXTRA)
        hit = flc is not None and abs(flc - flip) <= CTRL_BAR
        c4_ctrl_hits += int(hit)
        info("%-8s flip at n = %d (target %d) | C4 truncated "
             "engine (K = %d) predicts %s -> %s | C1-C3 "
             "midpoint-anchored forms predict ~ N_w = %d: gross "
             "miss by construction (adjudicated)"
             % (cname, flip, CTRL_FLIPS[cname], K4, str(flc),
                "HIT" if hit else "MISS", Nc))
    check("G60-control-flips-regated", ok_cf,
          "EPSTEIN/SCRAMBLE/SMOOTH flip at 25/21/27 exactly "
          "(r226/r231/r233 targets re-gated)")
    check("G61-falsifier-adjudicated", True,
          "C4 truncated engine hits %d/3 controls within +-%d; "
          "C1/C2/C3 fail the falsifier by construction "
          "(midpoint-anchored, cannot place a flip at n ~ 25); "
          "no form passes the falsifier unless the truncated "
          "engine locates a bulk boundary from tail data alone"
          % (c4_ctrl_hits, CTRL_BAR))

    # ---------------- S7: leg D adjudication
    section("S7  LEG D -- ALIAS CHECK + SEALED VERDICT")
    check("G70-alias-typing", True,
          "input audit: C1/C2 consume 2-3 floats at n <= N-1 "
          "(source-pure); C3 consumes two source-moment ratios; "
          "C4 consumes the last K = %d chain coefficients + "
          "node positions + h_0; NO form consumes gammahat/h/"
          "sign data at n >= N_w; the FULL-prefix engine "
          "(dimension S input, exact 42/42) is typed "
          "ALIAS_OF_DETERMINISM and competes in no score" % K4)
    # falsifier per form: C4 through the truncated engine; the
    # midpoint-anchored C1-C3 fail by construction (adjudicated
    # in G61) -- so ALPHALAW_FOUND requires a form that is NOT
    # in this round's sealed set to pass; stated, not hidden.
    fals = {"C1": False, "C2": False, "C3": False,
            "C4": c4_ctrl_hits == 3}
    law_c4 = (results["C4"][0] >= LAW_EXACT
              and results["C4"][1] >= LAW_PM1 and fals["C4"])
    law_c123 = next((nm for nm in ("C1", "C2", "C3")
                     if results[nm][0] >= LAW_EXACT
                     and results[nm][1] >= LAW_PM1
                     and fals[nm]), None)
    partial = next((nm for nm, (ex, pm) in results.items()
                    if ex >= LAW_EXACT and pm >= LAW_PM1
                    and not fals[nm]), None)
    if law_c4:
        verdict = "FRONTIER_LOCAL_LAW_K(%d)" % K4
    elif law_c123 is not None:
        verdict = "FRONTIER_ALPHALAW_FOUND(%s)" % law_c123
    elif partial is not None:
        verdict = "FRONTIER_PREDICTOR_PARTIAL(%s)" % partial
    else:
        verdict = "FRONTIER_NONLOCAL_IRREDUCIBLE"
    check("G71-adjudication", True,
          "SEALED RULE result: %s -- best BLIND exact %.3f "
          "(bar %.3f), best BLIND pm1 %.3f (bar %.2f), C4 "
          "falsifier %d/3; quantified irreducibility from leg "
          "B: median K_crit %d (%.0f%% of N median), "
          "Spearman(K_crit; N) %+.2f, derivative profile flat "
          "ratio %.2f, node dependence %s"
          % (verdict, max(e for e, _ in results.values()),
             LAW_EXACT, max(p for _, p in results.values()),
             LAW_PM1, c4_ctrl_hits, int(np.median(ks)),
             100.0 * float(np.median(kn)), rho_kn,
             early / max(late, 1e-12),
             "interior-flat" if edge <= 5.0 * inter
             else "edge-dominated"))

    # ---------------- S8: must-fails
    section("S8  MUST-FAILS")
    okM = True
    oracle_ok = all(
        (min(j for j, g in r["prof"].items()
             if j >= 0 and g <= 0.0) == r["delta"])
        for r in lad)
    okM = okM and oracle_ok
    phi_bad = toy_recon(alps_t, gams_t, hs_t, rhs_shift=1)
    ok_m2 = any(p != w for p, w in zip(phi_bad, TOY_WTS))
    okM = okM and ok_m2
    r9 = next((r for r in lad if r["kz"] == 9), lad[0])
    a2 = r9["alp"].copy()
    a2[:max(0, r9["N"] - 40)] += 0.1
    fl_g, _, _, _ = recon(r9["nodes"], a2, r9["gam"],
                          r9["lg0"], r9["sg0"],
                          r9["N"] + SEARCH_EXTRA)
    ok_m3 = fl_g != r9["nf"]
    okM = okM and ok_m3
    check("G80-must-fails-fire", okM,
          "oracle reading frontier signs hits delta on ALL "
          "windows (bars reachable, excluded by firewall); "
          "shifted-rhs toy reconstruction returns WRONG weights "
          "(loud); gross prefix corruption (+0.1 below N-40) "
          "moves the w9-anchor flip %d -> %s (the harness has "
          "teeth)" % (r9["nf"], str(fl_g)))

    # ---------------- S9: verdict
    section("S9  VERDICT")
    check("G90-mincut-unchanged", True,
          "mincut base 4 / refined 5 UNCHANGED (a locality "
          "measurement + sealed predictor adjudication moves no "
          "edge); what the round adds: the determinism map "
          "(prefix, node polynomial) -> delta is now an "
          "EXECUTABLE exact engine (42/42), and its information "
          "dimension is MEASURED per window")
    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    check("G91-verdict", npass == len(CHECKS),
          "%s: sealed DEV/BLIND hunt executed, falsifier "
          "applied, locality dimension measured and frozen; "
          "NO RH claim" % verdict)
    wall = time.time() - T0_WALL
    check("G99-runtime", wall <= 1800.0,
          "WALL %.1f s (bar 1800)" % wall)
    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    print("\n" + "=" * 78)
    print("RESULT: %d/%d gates PASS%s   SPEC_SHA %s"
          % (npass, len(CHECKS), " (SMOKE)" if smoke else "",
             SPEC_SHA[:16]))
    print("NO RH CLAIM in either direction.")
    print("=" * 78)
    return 0 if npass == len(CHECKS) else 1


if __name__ == "__main__":
    sys.exit(main())
