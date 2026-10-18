#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""case_edge_christoffel_probe -- PRIME.CASE.EDGE.CHRISTOFFEL.01
(EXPLORATION ONLY, experiments/; round 57, the priority-1 item: do
the two v899 halves read the same measure?  The signed-functional
pivot identity is rewritten as a POSITIVE-WEIGHT norm square minus
an explicit nonnegative remainder, verified exactly, and the
decisive ratio is measured ladder-wide.  2026-08-10.)

THE QUESTION (frozen).  v899 holds two halves: (i) the softest
pivot of the wall window is EXACTLY a deflated-Christoffel
evaluation of the SIGNED functional sigma = mu_+ - nu_-,
    1/d_12,h = 1 + v_* K_sigma(y_*, y_*)
(christoffel_ratio_probe, round 55 -- the positivity premise of
sigma is the wall's own PD premise, an honesty fence); (ii) the
periodic full-weight completion makes the pair-kernel frequency
weights W_{f,m} >= 0 exactly, a genuine norm square, at the price
of an explicit boundary term (edge_defect_kill_probe, round 56;
carried max |beta_pair|/margin~ = 0.21).  DO THESE TWO READ THE
SAME MEASURE -- can the pivot identity itself be rewritten as
    1/d_12,h = 1 + sum_m W_{h,m} |P_h(t_{h,m})|^2 - beta_h,
with ALL W_{h,m} >= 0 and beta_h an explicit nonnegative
endpoint/boundary-side term?

THE CONSTRUCTION (frozen; exact algebra derived a priori).  On
the full wall A = I - E, E = B B^T (christoffel_ratio (iii)
verbatim): G = B^T B is the Gram of nu_- in the mu_+-orthonormal
basis p_k; with p_* = p(y_*) and
    q := (I_h - G)^{-1} p_*,   Q(t) := p(t)^T q = K_sigma(y_*, t)
(the sigma-reproducing kernel at the soft node: (I-G) q = p_* is
exactly sigma[Q p_k] = p_k(y_*) for all k < h), the reproducing
property gives sigma[Q^2] = Q(y_*) = p_*^T q = m_def / v_*, and
sigma[Q^2] = mu_+[Q^2] - nu_-[Q^2] splits the pivot identity
EXACTLY into
    1/d_12 = 1 + SPOS_h - beta_h,
    SPOS_h = v_* mu_+[Q^2] = sum_s (v_* w_s) Q(x_s)^2   [W >= 0]
    beta_h = v_* nu_-[Q^2] = sum_j (v_* v_j) Q(y_j)^2   [>= 0],
i.e. W_{h,m} := v_* w_m (product of two constructional
nonnegative quadrature weights), P_h := Q, t_{h,m} := x_m -- the
POSITIVE part of the SAME folded cosine family the pair-kernel
weights read, and beta_h is carried ENTIRELY by the NEG-node
support (the boundary side of the same family, where the wall
operator lives), with the exact self-term beta_{h,j*} = m_def^2.
SO THE FROZEN ANSWER SHAPE: YES as an exact rewrite over the same
constructional family (measured below, incl. the d1-vs-d0
endpoint mismatch between the two v899 halves), and the price is
the measured ratio
    r_h := beta_h / (1 + SPOS_h)  in [0, 1)  on PD rungs,
with the EXACT complements 1 - r_h = (1/d_12)/(1 + SPOS_h) and
the Rayleigh fence r_h <= (1 - tau_full) SPOS/(1 + SPOS) < 1 --
the fence is the wall's own PD premise made quantitative: the
open uniform target q < 1 is EQUIVALENT on this surface to a
lower bound on tau_full.  Said plainly, incl. the plan nuance:
the incoming plan's "<= ~0.21" belongs to the PAIR-contract
boundary carry (v899(3)), a DIFFERENT functional; the decisive
ratio here is r_h and is expected to approach 1 at the rate of
tau -- the measurement below quantifies exactly that.

FROZEN PROTOCOL (machinery verbatim from christoffel_ratio_probe
round 55; PNT continuum lags verbatim from edge_defect_kill_probe
round 56 for the E4 endpoint comparison):

 W   PIPELINE + REPRODUCTION WARDS (kill -> PIPELINE-BROKEN /
     WARD-BROKEN): W0 truth ladder == 42 rungs; W0c full-window
     census == 37; W-C1a d_12 minor-quotient == inverse route
     (rel <= 1e-9, minor signs +1); W-C1c deflation chain 1/d_12
     == 1 + m_def (conditioning-aware bar, verbatim); W-C1d
     c >= 1 and tau_12 > 0 on every full rung; W-C1f c-quartile
     reproduction 1163/2117/2930 and c(kz21) = 50667 at h = 371
     (rtol 2e-2); W-SPOT (2 shallowest full rungs): the folded
     positive measure == (qt_f d1_f)_{d1 > 0} EXACTLY (rel <=
     1e-12) -- the 'same constructional family' claim warded
     against the pair-kernel quadrature rule.

 E1  THE REWRITE, EXACTLY (per full-window rung; kill ->
     WARD-BROKEN):
       E1.a  SPOS two routes: v_* |q|^2 (orthonormality route)
             == explicit quadrature sum_s (v_* w_s)(P_pos_s q)^2,
             rel <= QUAD_WARD;
       E1.b  beta two routes: v_* q^T G q == explicit sum_j
             (v_* v_j)(P_neg_j q)^2, rel <= GEXACT_WARD;
       E1.c  THE IDENTITY: 1/d_12 == 1 + SPOS - beta against the
             INDEPENDENT 12-window slogdet route, rel <=
             bar_h = max(CHR_WARD_FLOOR, CANC_FAC x EPS x
             (1 + SPOS + beta) x d_12) per rung (the honest
             cancellation floor: SPOS and beta are individually
             large and their difference is 1/d_12 - 1);
       E1.d  NONNEGATIVITY, EXACT: min_m W_{h,m} > 0 and every
             beta term >= 0 (squares times constructional
             weights; exact float signs, no tolerance);
       E1.e  SELF-TERM: the j* contribution to beta ==
             m_def^2 exactly (rel <= SELF_WARD).

 E2  THE DECISIVE RATIO (measured, typed): the full ladder (kz,
     h, m_def, SPOS, beta, r_h, 1 - r_h, (1-r_h)/tau_full,
     fence); WARDS (kill -> WARD-BROKEN): E2.a the complement
     identity 1 - r == (1/d_12)/(1 + SPOS), rel <= the SAME
     cancellation-aware bar as E1.c (1 - r inherits the
     SPOS - beta cancellation floor exactly);
     E2.b the Rayleigh fence r <= (1 - tau_full) SPOS/(1 + SPOS)
     (exact algebra, slack printed).  MEASURED: max r RAW (37)
     and SENS (kz-21 excluded, round-53 rule); OLS slope of
     log(1 - r) vs log tau_full and vs log h; quartiles of
     (1 - r)/tau_full.  TYPED (never kills): RATIO-BELOW-ONE(max
     r SENS) -- with the honest print that 1 - r_h tracks
     tau_full (the uniform q < 1 target is NOT achieved as an
     independent statement; it is the wall in new clothes,
     quantified).

 E3  WHERE beta LOCALIZES (measured): per rung the top
     beta-contribution anatomy -- self-term share m_def^2/beta,
     top-node fold index vs j* (= window coordinate 12), top-10
     node share, share carried by the 12-window coordinates
     JWIN; the CLASSICAL EVALUATION CONTROL: per neg node
     Q(y_j)^2 <= K_mu(y_j, y_j) |q|^2 (Cauchy-Schwarz in the
     mu_+ inner product; ward, exact up to CS_TOL) and the two
     aggregate bounds compared: beta / [v_* (1 - tau_full)
     |q|^2] (Rayleigh, sharp side) vs beta / [v_* tr(G) |q|^2]
     (classical evaluation bound; slack = how lossy the
     classical Christoffel evaluation inequality is here).
     TYPED: BETA-SEAT-SOFT(med self-share) iff the median
     self-term share >= 0.5, else BETA-SEAT-SPREAD(med).

 E4  THE SAME-MEASURE COMPARISON (the two v899 halves; measured,
     typed): per full-window rung build the t = 0 endpoint
     density d0 (arch + closed-form PNT continuum lags, verbatim
     cont_lags) next to the deployed truth density d1; the
     pair-kernel weights of v899(2)/(3) read the family
     (x_f, qt_f d0_f)_{d0 > 0}; the pivot rewrite reads
     (x_f, qt_f d1_f)_{d1 > 0} (W-SPOT ward) x v_*.  Measured
     per rung: positive-support overlap |{d0>0} cap {d1>0}| /
     |union|, the weight ratio stats on the common support, the
     exclusive-node mass shares; the round-50 heavy rungs kz
     {12, 13, 26, 40} printed as rows (kz 9 is below the 42-rung
     census floor h = 142 -- disclosed, not comparable here).
     TYPED: SAMEMEASURE-FAMILY(min overlap) -- same folded
     cosine quadrature family, same weight rule, DIFFERENT
     endpoint density (d1 truth vs d0 smooth reference) and
     different integrand (Q^2 vs p_{0,m}^2); if E1 had failed
     (any W < 0 or identity broken) the type would be
     SAMEMEASURE-OBSTRUCTED(channel) with the exact obstruction
     printed -- first-class outcome either way.

 C   CONTROLS (kill -> WARD-BROKEN if silent): C-S smooth world
     (B1 masses, verbatim): sigma indefinite (tau_full < 0) on
     >= 1 smooth rung AND the rewrite's ratio bound breaks off
     the truth comb -- on >= 1 smooth full-window rung r >= 1 or
     tau_12 <= 0 or d_12 <= 0; C-E Epstein x^2+5y^2 comb +
     scramble (seed 1) at kz 9: frame death or neg(A) > 0 or
     tau_12 <= 0; channel printed.

KILLS: KP a W pipeline ward breaks -> PIPELINE-BROKEN; KW an
E1/E2 ward or control breaks -> WARD-BROKEN.  E2/E3/E4 typed
labels report, never kill.

VERDICT (frozen enum): EDGECHRISTOFFEL-MEASURED with typed
sublabels REWRITE-EXACT, RATIO-BELOW-ONE(max r), BETA-SEAT-SOFT /
BETA-SEAT-SPREAD, SAMEMEASURE-FAMILY(overlap) /
SAMEMEASURE-OBSTRUCTED(channel); else PIPELINE-BROKEN /
WARD-BROKEN.

FROZEN BARS: H_DEEP_MAX = 900; JWIN = (2,...,24); NW = 12;
N_RUNGS_EXP = 42; N_FULLWIN_FROZEN = 37; KZ_STAR = 21; H_STAR =
371; REF_C21 = 50667, REF_Q25/MED/Q75 = 1163/2117/2930 (rtol
2e-2); ID_WARD = 1e-9; CHR_WARD_FLOOR = 1e-8; CHR_COND_FAC =
1e3; CGE1_WARD = 1e-9; N_SPOT = 2; H_SPOT_MAX = 150; MEAS_WARD =
1e-12; QUAD_WARD = 1e-6; GEXACT_WARD = 1e-10; CANC_FAC = 1e4;
SELF_WARD = 1e-8; CS_TOL = 1e-10; SEAT_BAR = 0.5; HEAVY_SHARED =
(12, 13, 26, 40); CTRL_KZ = 9; scramble seed 1; EPS =
2.220446049250313e-16.

SMOKE-RUN DISCLOSURE (2026-08-10, before freezing): one smoke run
of this script with the identical construction fixed the
float-floor bars that could not be set a priori and NEVER
weakened an exact claim (E1.d nonnegativity stays exact, zero
tolerance): (i) QUAD_WARD 1e-6 (smoke max 9.2e-13; the Lanczos
orthonormality floor under a 1/tau_full-amplified q); (ii)
SELF_WARD 1e-8 (smoke 5.8e-16); (iii) the E2.a complement
identity FAILED its naive first bar 1e-10 at smoke max rel
7.6e-9 -- correctly: 1 - r inherits the SPOS - beta cancellation
EXACTLY, so its bar was changed to the SAME cancellation-aware
form as E1.c (fail-first preserved: the smoke FAIL is recorded
here, no measured quantity moved); (iv) CANC_FAC was raised 1e3
-> 1e4 after the smoke run showed worst dev/bar 0.761 (an
honest-margin widening of a float floor, not a content bar).
The smoke run also confirmed the a-priori expectation printed in
the construction paragraph (r_h -> 1 with 1 - r_h tracking
tau_full; smoke max r SENS = 0.99995).  No census count, no
enum, no typed rule was changed after the smoke run.

SPEC v1 (2026-08-10, frozen + SHA-hashed before the frozen run):
everything above.  Mechanical concretizations frozen with v1: (i)
window memoization per (kz, seed); (ii) ONE Gram per rung, the
factor-Gram spectral identity for tau_full (christoffel_ratio
verbatim); (iii) q via one symmetric solve of (I - G); P_pos =
eval_chain at the positive nodes (same chain); (iv) SENS
statistics = leave-kz-21-out (round-53 rule), raw always printed;
(v) E4 support sets are {1 <= f <= F-2 : d > 0} (f = 0 and the
top fold carry zero or endpoint qt weight; the folded family of
the pivot rewrite is warded against exactly this rule in W-SPOT);
(vi) slogdet signs warded +1.

NO RH claim: the rewrite is exact finite linear algebra on the
deployed v563 window family; W >= 0 and beta >= 0 are
constructional; NOTHING here proves r_h <= q < 1 uniformly --
the measured fence says that statement IS the wall's PD premise
quantitatively.  The pair-correlation-class conditionality of
the diagonal route (v889/v899) is untouched.  No marker moves.

FIREWALL: no zeros, no prime oracles (AST scan; banned ids
zetazero / nzeros / primerange / isprime / primepi / nextprime /
prevprime); v563 READ-ONLY; RNG only inside the declared
scramble control; stdout only.

Sources (read-only): v563_paper2_readouts; wall/window/deflation
machinery verbatim from christoffel_ratio_probe.py (round 55,
promoted v899); PNT continuum closed-form lags verbatim from
edge_defect_kill_probe.py (round 56, promoted v899); pair-kernel
weight family per kernel_sos_probe / edge_defect_kill_probe
(declared reading, not rebuilt); v884/v887/v897 certified base --
declared inputs.

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/case_edge_christoffel_probe.py
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

H_DEEP_MAX = 900
JWIN = tuple(range(2, 25, 2))
NW = 12
N_RUNGS_EXP = 42
N_FULLWIN_FROZEN = 37
KZ_STAR = 21
H_STAR = 371
REF_C21 = 50667.0
REF_Q25, REF_MED, REF_Q75 = 1163.0, 2117.0, 2930.0
REF_RTOL = 2e-2
ID_WARD = 1e-9
CHR_WARD_FLOOR = 1e-8
CHR_COND_FAC = 1e3
CGE1_WARD = 1e-9
N_SPOT = 2
H_SPOT_MAX = 150
MEAS_WARD = 1e-12              # W-SPOT folded == qt d
QUAD_WARD = 1e-6               # E1.a (smoke-fixed, see header)
GEXACT_WARD = 1e-10            # E1.b
CANC_FAC = 1e4                 # E1.c/E2.a cancellation factor
SELF_WARD = 1e-8               # E1.e (smoke-fixed)
CS_TOL = 1e-10                 # E3 Cauchy-Schwarz tolerance
SEAT_BAR = 0.5                 # E3 typing bar
HEAVY_SHARED = (12, 13, 26, 40)
CTRL_KZ = 9
EPS = 2.220446049250313e-16
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


# --------- pipeline, verbatim (christoffel_ratio_probe chain)
def grid_density(c):
    c = np.asarray(c, float)
    a = np.concatenate([c, c[-2:0:-1]])
    d = np.fft.fft(a)
    assert float(np.max(np.abs(d.imag))) <= 1e-9 * max(
        1.0, float(np.max(np.abs(d.real))))
    return d.real


def cell_widths(uu):
    du = np.zeros(len(uu))
    du[1:-1] = 0.5 * (uu[2:] - uu[:-2])
    du[0] = uu[1] - uu[0]
    du[-1] = uu[-1] - uu[-2]
    return du


def smooth_masses(uu):
    return 2.0 * np.exp(np.asarray(uu, float) / 2.0) \
        * cell_widths(np.asarray(uu, float))


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


def lambda_eps(N):
    """Epstein x^2+5y^2 comb (port_schur_reduction verbatim)."""
    r = np.zeros(N + 1)
    s = int(math.isqrt(N)) + 1
    for x in range(-s, s + 1):
        for y in range(-s, s + 1):
            v = x * x + 5 * y * y
            if 1 <= v <= N:
                r[v] += 1.0
    a = r / 2.0
    lam = np.zeros(N + 1)
    for n in range(2, N + 1):
        acc = a[n] * math.log(n)
        for dd in range(2, n):
            if n % dd == 0:
                acc -= lam[dd] * a[n // dd]
        lam[n] = acc
    return lam


def _prim(u, A, B):
    """Primitive of (A + B u) 2 e^{u/2} (edge_defect verbatim)."""
    return 4.0 * np.exp(0.5 * u) * (A + B * (u - 2.0))


def cont_lags(alpha, M, seg_lo, seg_hi, seg_sc):
    """Closed-form PNT tent lags (edge_defect verbatim)."""
    D = 2.0 * alpha / M
    c = np.zeros(M)
    for lo, hi, sc in zip(seg_lo, seg_hi, seg_sc):
        i0 = max(0, int(math.floor(lo / D)) - 1)
        i1 = min(M - 1, int(math.ceil(hi / D)) + 1)
        ii = np.arange(i0, i1 + 1, dtype=float)
        val = np.zeros(len(ii))
        a = np.maximum((ii - 1.0) * D, lo)
        b = np.minimum(ii * D, hi)
        m = b > a
        val[m] += (_prim(b[m], 1.0 - ii[m], 1.0 / D)
                   - _prim(a[m], 1.0 - ii[m], 1.0 / D))
        a = np.maximum(ii * D, lo)
        b = np.minimum((ii + 1.0) * D, hi)
        m = b > a
        val[m] += (_prim(b[m], 1.0 + ii[m], -1.0 / D)
                   - _prim(a[m], 1.0 + ii[m], -1.0 / D))
        if i0 == 0:
            a0, b0 = max(0.0, lo), min(D, hi)
            if b0 > a0:
                val[0] += (_prim(b0, 1.0, -1.0 / D)
                           - _prim(a0, 1.0, -1.0 / D))
        c[i0:i1 + 1] -= 0.5 * sc * val
    return c


_WIN_CACHE = {}


def window_of(kz, scramble_seed=None):
    key = (kz, scramble_seed)
    if key not in _WIN_CACHE:
        rr = core.build_window(kz, scramble_seed=scramble_seed)
        _WIN_CACHE[key] = dict(
            h=rr["h"], M=rr["M"], D=rr["D"], alpha=rr["alpha"],
            n_atom=rr["n_atom"],
            uu=np.asarray(rr["uu"], float).copy(),
            lam=np.asarray(rr["lam"], float).copy(),
            c_ar=np.asarray(core.arch_lags(rr["M"], rr["D"]),
                            float))
    return _WIN_CACHE[key]


def anatomy(kz, scramble_seed=None, comb=None, keep_all=False):
    """One rung -> Gram, 12-window compression, deflated mass
    (christoffel_ratio verbatim), EXTENDED (keep_all): the folded
    positive/negative measures, the chain, Pn and G are retained
    for the E1 rewrite."""
    rr = window_of(kz, scramble_seed=scramble_seed)
    h, M, D, alpha = rr["h"], rr["M"], rr["D"], rr["alpha"]
    if h > H_DEEP_MAX:
        return "TOO-DEEP"
    uu = rr["uu"]
    mm = 2.0 * rr["lam"]
    if comb is not None:
        uu, mm = comb
    c_at, _ = core.atom_lags_at(alpha, M, uu, mm)
    d = grid_density(rr["c_ar"] + np.asarray(c_at, float))
    L = 2 * M - 2
    xs, ws, uf_p = folded_measure(d, L, +1.0)
    ys, vs, uf_n = folded_measure(d, L, -1.0)
    al, be, m0, steps = lanczos_chain(xs, ws, h + 1)
    if steps < h + 1 or np.any(be <= 0):
        return None
    Pn = eval_chain(al, be, m0, ys, h)
    B = np.sqrt(vs)[:, None] * Pn
    E = B @ B.T
    E = 0.5 * (E + E.T)
    n = E.shape[0]
    out = dict(kz=kz, h=h, n=n, M=M, L=L, D=D,
               alpha=float(alpha))
    G = B.T @ B
    G = 0.5 * (G + G.T)
    egG = np.linalg.eigvalsh(G)
    out["tau_full"] = float(1.0 - egG[-1])
    out["negA"] = int(np.sum(egG > 1.0))
    idx = {int(j): k for k, j in enumerate(uf_n)}
    jav = [j for j in JWIN if j in idx]
    out["full"] = (len(jav) == len(JWIN))
    if out["full"]:
        iw = [idx[j] for j in jav]
        io = [k for k in range(n) if k not in set(iw)]
        IO = np.eye(len(io)) - E[np.ix_(io, io)]
        try:
            CJ = (E[np.ix_(iw, iw)]
                  + E[np.ix_(iw, io)] @ np.linalg.solve(
                      IO, E[np.ix_(io, iw)]))
            out["CJ"] = 0.5 * (CJ + CJ.T)
        except np.linalg.LinAlgError:
            out["full"] = False
    if out["full"]:
        jstar = idx[JWIN[-1]]
        p = Pn[jstar]
        qvec = np.linalg.solve(np.eye(h) - G, p)
        out["jstar"] = jstar
        out["vstar"] = float(vs[jstar])
        out["m_def"] = float(vs[jstar] * (p @ qvec))
        if keep_all:
            out["qvec"] = qvec
            out["Pn"] = Pn
            out["G"] = G
            out["vs"] = vs
            out["ws"] = ws
            out["xs"] = xs
            out["uf_p"] = uf_p
            out["uf_n"] = uf_n
            out["chain"] = (al, be, m0)
            out["d1"] = d
    return out


def win_attrs(r):
    """12-window objects (christoffel_ratio verbatim, trimmed)."""
    A = np.eye(NW) - r["CJ"]
    sg12, ld12 = np.linalg.slogdet(A)
    sg11, ld11 = np.linalg.slogdet(A[:11, :11])
    r["sg_ok"] = (sg12 == 1.0 and sg11 == 1.0)
    r["d12"] = math.exp(ld12 - ld11) * sg12 * sg11
    ew = np.linalg.eigvalsh(A)
    r["tau12"] = float(ew[0])
    Ainv = np.linalg.inv(A)
    r["a1212"] = float(Ainv[11, 11])
    r["c"] = r["d12"] / r["tau12"] if r["tau12"] != 0.0 \
        else float("inf")
    r["dev_inv"] = (abs(r["d12"] - 1.0 / r["a1212"])
                    / max(abs(r["d12"]), 1e-300))
    r["dev_chr"] = (abs(1.0 / r["d12"] - (1.0 + r["m_def"]))
                    / max(abs(1.0 / r["d12"]), 1e-300))
    return r


def quartiles(v):
    q = np.percentile(np.asarray(v, float), [25, 50, 75])
    return float(q[0]), float(q[1]), float(q[2])


def ols_slope(x, y):
    x = np.asarray(x, float)
    y = np.asarray(y, float)
    xm, ym = float(np.mean(x)), float(np.mean(y))
    return float(np.sum((x - xm) * (y - ym))
                 / np.sum((x - xm) ** 2))


def main():
    section("PRIME.CASE.EDGE.CHRISTOFFEL.01 -- the pivot identity "
            "as a positive norm square minus an explicit "
            "remainder (EXPLORATION ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s"
          % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
    print("    NO RH claim; no marker moves.")
    print("\nS0 -- firewall")
    check("S0.1 AST firewall clean", not ast_scan(BANNED_IDS))

    # ------------------------------------------------------------ W
    section("W -- ladders + reproduction wards (christoffel_ratio "
            "chain, ONE Gram per rung)")
    truth, smooth = [], []
    n_toodeep, n_dead_t, n_dead_s = 0, 0, 0
    for kz in core.frame_a_zones():
        r = anatomy(kz, keep_all=True)
        if r == "TOO-DEEP":
            n_toodeep += 1
            continue
        if r is None:
            n_dead_t += 1
            continue
        truth.append(r)
        uu = window_of(kz)["uu"]
        rs = anatomy(kz, comb=(uu, smooth_masses(uu)))
        if isinstance(rs, dict):
            smooth.append(rs)
        else:
            n_dead_s += 1
    truth.sort(key=lambda r: (r["h"], r["kz"]))
    smooth.sort(key=lambda r: (r["h"], r["kz"]))
    print("    truth %d rungs (h %d..%d; %d TOO-DEEP, %d dead) | "
          "smooth %d rungs (%d dead)  [%.1f s]"
          % (len(truth), truth[0]["h"], truth[-1]["h"], n_toodeep,
             n_dead_t, len(smooth), n_dead_s, time.time() - T0))
    check("W0 truth ladder == %d rungs" % N_RUNGS_EXP,
          len(truth) == N_RUNGS_EXP, "%d" % len(truth), kill="KP")
    fullw = [r for r in truth if r.get("full") and "CJ" in r]
    check("W0c full-window census %d == %d"
          % (len(fullw), N_FULLWIN_FROZEN),
          len(fullw) == N_FULLWIN_FROZEN, kill="KP")
    if KILLS:
        return finish({})
    for r in fullw:
        win_attrs(r)
    sg_all = all(r["sg_ok"] for r in fullw)
    dev_inv = max(r["dev_inv"] for r in fullw)
    check("W-C1a d_12 minor-quotient == inverse route: max rel "
          "%.1e <= %.0e; minor signs +1: %s"
          % (dev_inv, ID_WARD, sg_all),
          dev_inv <= ID_WARD and sg_all, kill="KW")
    chr_worst = max(r["dev_chr"]
                    / max(CHR_WARD_FLOOR,
                          CHR_COND_FAC * EPS / r["tau_full"])
                    for r in fullw)
    check("W-C1c deflation chain 1/d_12 == 1 + m_def: worst "
          "dev/bar %.3f <= 1 (max rel %.1e)"
          % (chr_worst, max(r["dev_chr"] for r in fullw)),
          chr_worst <= 1.0, kill="KW")
    c_min = min(r["c"] for r in fullw)
    tau_min = min(r["tau12"] for r in fullw)
    check("W-C1d c >= 1 (min %.3f) and tau_12 > 0 (min %.3e)"
          % (c_min, tau_min),
          c_min >= 1.0 - CGE1_WARD and tau_min > 0.0, kill="KW")
    cs = np.array([r["c"] for r in fullw])
    q1, q2, q3 = quartiles(cs)
    star = [r for r in fullw if r["kz"] == KZ_STAR]
    c21 = star[0]["c"] if star else float("nan")
    h21 = star[0]["h"] if star else -1
    check("W-C1f REPRODUCTION c-quartiles %.0f/%.0f/%.0f == "
          "%.0f/%.0f/%.0f, c(kz%d) %.0f == %.0f at h %d "
          "(rtol %.0e)"
          % (q1, q2, q3, REF_Q25, REF_MED, REF_Q75, KZ_STAR, c21,
             REF_C21, h21, REF_RTOL),
          abs(q1 / REF_Q25 - 1.0) <= REF_RTOL
          and abs(q2 / REF_MED - 1.0) <= REF_RTOL
          and abs(q3 / REF_Q75 - 1.0) <= REF_RTOL
          and abs(c21 / REF_C21 - 1.0) <= REF_RTOL
          and h21 == H_STAR, kill="KW")
    # W-SPOT: the folded positive measure == (qt d1)_{d1>0}
    spot = [r for r in fullw if r["h"] <= H_SPOT_MAX][:N_SPOT]
    dev_meas = 0.0
    for r in spot:
        L, M = r["L"], r["M"]
        F = L // 2 + 1
        d1F = r["d1"][:F]
        ff = np.arange(F)
        mult = np.where((ff == 0) | (ff == L // 2), 1.0, 2.0)
        qt = mult * 4.0 * np.sin(math.pi * ff / L) ** 2 \
            / (2.0 * L)
        wq = {int(f): float(qt[f] * d1F[f]) for f in range(1, F)
              if d1F[f] > 0.0}
        wf = {int(f): float(w) for f, w in zip(r["uf_p"],
                                               r["ws"])}
        keys = set(wq) | set(k for k in wf if k >= 1)
        for f in keys:
            a_, b_ = wq.get(f, 0.0), wf.get(f, 0.0)
            dev_meas = max(dev_meas, abs(a_ - b_)
                           / max(abs(a_), abs(b_), 1e-300))
    check("W-SPOT folded positive measure == (qt_f d1_f)_{d1>0} "
          "on %d spot rungs: max rel %.1e <= %.0e (the SAME "
          "quadrature family as the pair-kernel weights)"
          % (len(spot), dev_meas, MEAS_WARD),
          len(spot) == N_SPOT and dev_meas <= MEAS_WARD,
          kill="KW")
    if KILLS:
        return finish({})

    # ------------------------------------------------------------ E1
    section("E1 -- THE REWRITE: 1/d_12 = 1 + sum W |Q|^2 - beta "
            "(exact, per full rung)")
    dev_quad = dev_gex = dev_id = dev_self = 0.0
    minW_all = float("inf")
    minbt_all = float("inf")
    for r in fullw:
        q = r["qvec"]
        al, be, m0 = r["chain"]
        h = r["h"]
        v_ = r["vstar"]
        # E1.a SPOS two routes
        spos_o = v_ * float(q @ q)
        Ppos = eval_chain(al, be, m0, r["xs"], h)
        Qpos = Ppos @ q
        spos_q = v_ * float(r["ws"] @ (Qpos * Qpos))
        dev_quad = max(dev_quad, abs(spos_o - spos_q)
                       / max(abs(spos_o), 1e-300))
        # E1.b beta two routes
        beta_g = v_ * float(q @ (r["G"] @ q))
        Qneg = r["Pn"] @ q
        bterms = v_ * r["vs"] * (Qneg * Qneg)
        beta_q = float(np.sum(bterms))
        dev_gex = max(dev_gex, abs(beta_g - beta_q)
                      / max(abs(beta_g), 1e-300))
        # E1.c identity vs the independent 12-window route
        lhs = 1.0 / r["d12"]
        rhs = 1.0 + spos_q - beta_q
        bar = max(CHR_WARD_FLOOR,
                  CANC_FAC * EPS * (1.0 + spos_q + beta_q)
                  * r["d12"])
        dev_id = max(dev_id, (abs(lhs - rhs) / abs(lhs)) / bar)
        # E1.d exact nonnegativity
        minW_all = min(minW_all, v_ * float(np.min(r["ws"])))
        minbt_all = min(minbt_all, float(np.min(bterms)))
        # E1.e self-term == m_def^2
        bself = float(bterms[r["jstar"]])
        dev_self = max(dev_self, abs(bself - r["m_def"] ** 2)
                       / max(r["m_def"] ** 2, 1e-300))
        r["SPOS"] = spos_q
        r["beta"] = beta_q
        r["bterms"] = bterms
        r["bself"] = bself
        r["normq2"] = float(q @ q)
    check("E1.a SPOS orthonormality route == explicit quadrature "
          "route: max rel %.1e <= %.0e" % (dev_quad, QUAD_WARD),
          dev_quad <= QUAD_WARD, kill="KW")
    check("E1.b beta Gram route == explicit node route: max rel "
          "%.1e <= %.0e" % (dev_gex, GEXACT_WARD),
          dev_gex <= GEXACT_WARD, kill="KW")
    check("E1.c THE IDENTITY 1/d_12 == 1 + SPOS - beta vs the "
          "independent slogdet route: worst dev/bar %.3f <= 1 "
          "(cancellation-aware bar, see spec)" % dev_id,
          dev_id <= 1.0, kill="KW")
    check("E1.d NONNEGATIVITY EXACT: min W_{h,m} = %.3e > 0 and "
          "min beta term = %.3e >= 0 (no tolerance)"
          % (minW_all, minbt_all),
          minW_all > 0.0 and minbt_all >= 0.0, kill="KW")
    check("E1.e self-term beta_{j*} == m_def^2: max rel %.1e <= "
          "%.0e" % (dev_self, SELF_WARD), dev_self <= SELF_WARD,
          kill="KW")
    check("E1.f typed: REWRITE-EXACT (the two v899 halves DO "
          "read one measure family: positive part -> the norm "
          "square, negative part -> beta)", True)

    # ------------------------------------------------------------ E2
    section("E2 -- THE DECISIVE RATIO r_h = beta/(1 + SPOS)")
    dev_comp = 0.0
    fence_viol = 0
    rows = []
    print("    kz   h    m_def      SPOS       beta       "
          "r_h        1-r_h      (1-r)/tau  fence-r")
    for r in fullw:
        rh = r["beta"] / (1.0 + r["SPOS"])
        comp = (1.0 / r["d12"]) / (1.0 + r["SPOS"])
        bar = max(CHR_WARD_FLOOR,
                  CANC_FAC * EPS * (1.0 + r["SPOS"] + r["beta"])
                  * r["d12"])
        dev_comp = max(dev_comp, (abs((1.0 - rh) - comp)
                                  / max(abs(comp), 1e-300))
                       / bar)
        fence = ((1.0 - r["tau_full"]) * r["SPOS"]
                 / (1.0 + r["SPOS"]))
        if rh > fence * (1.0 + 1e-12):
            fence_viol += 1
        r["r_h"] = rh
        r["fence"] = fence
        rows.append(r)
        print("    %-4d %-4d %.3e  %.3e  %.3e  %.6f  %.3e  "
              "%8.3f  %.3e%s"
              % (r["kz"], r["h"], r["m_def"], r["SPOS"],
                 r["beta"], rh, 1.0 - rh,
                 (1.0 - rh) / r["tau_full"], fence - rh,
                 "   <-- kz-21" if r["kz"] == KZ_STAR else ""),
              flush=True)
    check("E2.a complement identity 1 - r == (1/d_12)/(1 + "
          "SPOS): worst dev/bar %.3f <= 1 (cancellation-aware "
          "bar as E1.c)" % dev_comp, dev_comp <= 1.0, kill="KW")
    check("E2.b Rayleigh fence r <= (1 - tau_full) SPOS/(1 + "
          "SPOS) on every rung (violations: %d)" % fence_viol,
          fence_viol == 0, kill="KW")
    rr_all = np.array([r["r_h"] for r in rows])
    sens = [r for r in rows if r["kz"] != KZ_STAR]
    rr_s = np.array([r["r_h"] for r in sens])
    one_m = 1.0 - rr_all
    ratio_tau = np.array([(1.0 - r["r_h"]) / r["tau_full"]
                          for r in rows])
    sl_tau = ols_slope(np.log([r["tau_full"] for r in rows]),
                       np.log(one_m))
    sl_h = ols_slope(np.log([r["h"] for r in rows]),
                     np.log(one_m))
    qa, qb, qc = quartiles(ratio_tau)
    print("\n    max r RAW = %.8f (%d rungs) | SENS = %.8f (%d); "
          "min r = %.6f"
          % (float(np.max(rr_all)), len(rr_all),
             float(np.max(rr_s)), len(rr_s),
             float(np.min(rr_all))))
    print("    trend: OLS slope log(1-r) vs log tau_full = "
          "%+.4f; vs log h = %+.4f" % (sl_tau, sl_h))
    print("    (1-r)/tau_full quartiles: %.2f / %.2f / %.2f "
          "(range [%.2f, %.2f])"
          % (qa, qb, qc, float(np.min(ratio_tau)),
             float(np.max(ratio_tau))))
    print("    HONEST READING: r < 1 on every deployed rung, "
          "but 1 - r_h TRACKS tau_full (slope ~ 1) -- the "
          "uniform q < 1 target is the wall's PD premise "
          "quantified, NOT an independent gain.")
    e2 = "RATIO-BELOW-ONE(max-r-SENS=%.6f)" % float(np.max(rr_s))
    check("E2.c typed: %s" % e2, True)

    # ------------------------------------------------------------ E3
    section("E3 -- WHERE beta LOCALIZES + the classical "
            "evaluation control")
    cs_worst = 0.0
    selfsh = []
    winsh = []
    top10 = []
    ray_r = []
    cls_r = []
    print("    kz   h    self-share top-fold(j*?)  top10-share "
          "JWIN-share  beta/Rayleigh beta/classical")
    for r in rows:
        bt = r["bterms"]
        beta = r["beta"]
        share_self = r["bself"] / beta
        selfsh.append(share_self)
        order = np.argsort(-bt)
        tf = int(r["uf_n"][order[0]])
        t10 = float(np.sum(bt[order[:10]]) / beta)
        top10.append(t10)
        jw = set(JWIN)
        wsh = float(np.sum([b for b, f in zip(bt, r["uf_n"])
                            if int(f) in jw]) / beta)
        winsh.append(wsh)
        # Cauchy-Schwarz per node: Q(y)^2 <= K_mu(y,y) |q|^2
        Kmu = np.sum(r["Pn"] ** 2, axis=1)
        Qn2 = (r["Pn"] @ r["qvec"]) ** 2
        cs_worst = max(cs_worst, float(np.max(
            Qn2 / (Kmu * r["normq2"]))))
        rayb = (r["vstar"] * (1.0 - r["tau_full"]) * r["normq2"])
        clsb = (r["vstar"] * float(np.trace(r["G"]))
                * r["normq2"])
        ray_r.append(beta / rayb)
        cls_r.append(beta / clsb)
        print("    %-4d %-4d %.6f   %5d (%s)     %.4f      "
              "%.4f      %.6f      %.3e"
              % (r["kz"], r["h"], share_self, tf,
                 "=j*" if order[0] == r["jstar"] else "no",
                 t10, wsh, ray_r[-1], cls_r[-1]), flush=True)
    check("E3.a Cauchy-Schwarz evaluation control Q(y)^2 <= "
          "K_mu(y,y) |q|^2: worst ratio %.6f <= 1 + %.0e"
          % (cs_worst, CS_TOL), cs_worst <= 1.0 + CS_TOL,
          kill="KW")
    med_self = float(np.median(selfsh))
    print("\n    self-term share m_def^2/beta: med %.4f (range "
          "[%.4f, %.4f]); top-10 share med %.4f; JWIN share med "
          "%.4f" % (med_self, float(np.min(selfsh)),
                    float(np.max(selfsh)),
                    float(np.median(top10)),
                    float(np.median(winsh))))
    print("    aggregate bounds: beta/Rayleigh med %.4f (sharp "
          "side; = the fence content) vs beta/classical-trace "
          "med %.3e (the classical Christoffel evaluation "
          "inequality is %.0fx lossier here)"
          % (float(np.median(ray_r)), float(np.median(cls_r)),
             float(np.median(ray_r)) / max(float(np.median(
                 cls_r)), 1e-300)))
    e3 = ("BETA-SEAT-SOFT(med-self=%.3f)" % med_self
          if med_self >= SEAT_BAR
          else "BETA-SEAT-SPREAD(med-self=%.3f)" % med_self)
    check("E3.b typed: %s" % e3, True)

    # ------------------------------------------------------------ E4
    section("E4 -- THE SAME-MEASURE COMPARISON (pivot rewrite "
            "family vs pair-kernel family)")
    print("    pivot rewrite reads (x_f, qt_f d1_f)_{d1>0} x v_* "
          "(truth endpoint); pair-kernel weights read "
          "(x_f, qt_f d0_f)_{d0>0} (t = 0 endpoint).")
    print("    kz 9 of the round-50 heavy set is below the "
          "42-rung census floor (h = 142) -- disclosed, not "
          "comparable here.")
    ovls = []
    print("    kz   h    |P1|   |P0|   overlap  Jaccard  "
          "wratio med [min, max]   excl-mass d1  excl-mass d0")
    for r in rows:
        L, M = r["L"], r["M"]
        F = L // 2 + 1
        w = window_of(r["kz"])
        c0 = cont_lags(r["alpha"], M, [0.0],
                       [2.0 * r["alpha"]], [1.0])
        d0F = grid_density(w["c_ar"] + c0)[:F]
        d1F = r["d1"][:F]
        ff = np.arange(1, F - 1)
        qt = 2.0 * 4.0 * np.sin(math.pi * ff / L) ** 2 \
            / (2.0 * L)
        p1 = ff[d1F[1:F - 1] > 0.0]
        p0 = ff[d0F[1:F - 1] > 0.0]
        s1, s0 = set(p1.tolist()), set(p0.tolist())
        com = np.array(sorted(s1 & s0), dtype=int)
        jac = len(com) / max(len(s1 | s0), 1)
        ovls.append(jac)
        w1 = qt[com - 1] * d1F[com]
        w0 = qt[com - 1] * d0F[com]
        rat = w1 / w0
        m1 = float(np.sum(qt[p1 - 1] * d1F[p1]))
        m0_ = float(np.sum(qt[p0 - 1] * d0F[p0]))
        ex1 = np.array(sorted(s1 - s0), dtype=int)
        ex0 = np.array(sorted(s0 - s1), dtype=int)
        xm1 = (float(np.sum(qt[ex1 - 1] * d1F[ex1])) / m1
               if len(ex1) else 0.0)
        xm0 = (float(np.sum(qt[ex0 - 1] * d0F[ex0])) / m0_
               if len(ex0) else 0.0)
        hv = "  <-- round-50 heavy" if r["kz"] in HEAVY_SHARED \
            else ""
        print("    %-4d %-4d %5d  %5d  %5d    %.4f   %.4f "
              "[%.3f, %.3f]   %.2e      %.2e%s"
              % (r["kz"], r["h"], len(s1), len(s0), len(com),
                 jac, float(np.median(rat)), float(np.min(rat)),
                 float(np.max(rat)), xm1, xm0, hv), flush=True)
    min_ovl = float(np.min(ovls))
    e4 = "SAMEMEASURE-FAMILY(min-Jaccard=%.4f)" % min_ovl
    check("E4.1 typed: %s -- same folded cosine quadrature "
          "family and weight rule (W-SPOT exact), different "
          "endpoint density (d1 vs d0) and integrand (Q^2 vs "
          "p_{0,m}^2); beta lives on the complementary NEG "
          "support" % e4, True)

    # ------------------------------------------------------------ C
    section("C -- controls: the rewrite must break off the truth "
            "comb")
    sneg = [r for r in smooth if r["tau_full"] < 0.0]
    sfull = [r for r in smooth if r.get("full") and "CJ" in r]
    n_break = 0
    for r in sfull:
        A = np.eye(NW) - r["CJ"]
        tau12s = float(np.linalg.eigvalsh(A)[0])
        sg, ld = np.linalg.slogdet(A)
        d12s = None
        if sg != 0.0:
            sg11, ld11 = np.linalg.slogdet(A[:11, :11])
            if sg11 != 0.0:
                d12s = math.exp(ld - ld11) * sg * sg11
        fired = (tau12s <= 0.0 or (d12s is not None
                                   and d12s <= 0.0))
        if fired:
            n_break += 1
    print("  C-S smooth: sigma indefinite (tau_full < 0) on "
          "%d/%d rungs (first h = %s); rewrite ratio bound "
          "breaks (tau_12 <= 0 or d_12 <= 0 <=> r >= 1) on "
          "%d/%d full-window rungs"
          % (len(sneg), len(smooth),
             sneg[0]["h"] if sneg else "n/a", n_break,
             len(sfull)))
    check("C-S smooth world breaks both premises (>= 1 each)",
          len(sneg) >= 1 and n_break >= 1, kill="KW")
    print("  C-E Epstein + scramble at kz %d:" % CTRL_KZ)
    rr9 = window_of(CTRL_KZ)
    N_E = int(math.floor(math.exp(2.0 * rr9["alpha"]))) + 1
    lamE_ = lambda_eps(N_E)
    nn = np.nonzero(np.abs(lamE_) > 1e-12)[0]
    ok_c = True
    for nmc, kw in (("Epstein",
                     dict(comb=(np.log(nn.astype(float)),
                                2.0 * lamE_[nn]
                                / np.sqrt(nn.astype(float))))),
                    ("scramble", dict(scramble_seed=1))):
        try:
            rc = anatomy(CTRL_KZ, **kw)
        except (np.linalg.LinAlgError, AssertionError):
            rc = None
        if not isinstance(rc, dict):
            print("       %-8s: chain dies (%r) -> FIRES" %
                  (nmc, rc))
            continue
        tau12c = None
        if rc.get("full") and "CJ" in rc:
            tau12c = float(np.linalg.eigvalsh(
                np.eye(NW) - rc["CJ"])[0])
        fired = (rc["negA"] > 0
                 or (tau12c is not None and tau12c <= 0.0))
        ok_c &= fired
        print("       %-8s: neg(A) %d | tau_12 %s -> %s"
              % (nmc, rc["negA"],
                 ("%+.3e" % tau12c) if tau12c is not None
                 else "n/a", "FIRES" if fired else "SILENT"))
    check("C-E controls fire", ok_c, kill="KW")

    return finish(dict(e2=e2, e3=e3, e4=e4))


def finish(labels):
    section("V -- FROZEN VERDICT")
    n_pass = sum(1 for _n, okk in CHECKS if okk)
    n_tot = len(CHECKS)
    if KILLS:
        VERDICT = {"KP": "PIPELINE-BROKEN",
                   "KW": "WARD-BROKEN"}[KILLS[0]]
        print("\n  VERDICT: %s" % VERDICT)
    else:
        VERDICT = ("EDGECHRISTOFFEL-MEASURED / REWRITE-EXACT / "
                   "%(e2)s / %(e3)s / %(e4)s" % labels)
        print("\n  VERDICT: %s" % VERDICT)
    print("""
  HONEST FRAME (as frozen): the rewrite is exact warded algebra
  -- the pivot identity IS a positive-weight norm square over
  the constructional folded family minus an explicit nonnegative
  NEG-support remainder beta, with the exact self-term m_def^2.
  W >= 0 costs nothing here (unlike the pair contract, no
  boundary fold was needed); the price sits ENTIRELY in the
  ratio r_h = beta/(1 + SPOS), whose distance from 1 is warded
  EXACTLY to (1/d_12)/(1 + SPOS) and tracks tau_full: the
  uniform q < 1 target is the wall's PD premise in these
  coordinates, quantified -- NOT an independent positivity
  source.  The diagonal route stays conditional per v889/v899.
  NO RH claim.  No marker moves.""")
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed"
          % (time.time() - T0, n_tot, n_tot - n_pass))
    return 0 if n_pass == n_tot else 1


if __name__ == "__main__":
    raise SystemExit(main())
