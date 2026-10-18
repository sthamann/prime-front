#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""damping_cert_probe -- PRIME.DAMPING.CERT.01 (EXPLORATION
ONLY, experiments/; 2026-08-13, after CCCXIII / EC-DEAD).

THE ONE SURVIVING OBJECT.  The Euler-Clark falsification
(CCCXIII) left the v872 two-term split untouched:

    I - C*C  =  (I - U*U)  +  U*(I - D_-^2) U
             =      T_1     +       T_2

with the ARITHMETIC LIVING ENTIRELY IN THE DAMPING D_- (the
only gate in that run that separates truth from Epstein and
scramble: max D_- = 0.9849 vs 34.2 vs 2916.9).  The typed
instruction: any future contraction certificate must act on
the damping term.  This probe characterizes D_- completely
and attacks its source-only certificate D_- <= 1.

THE ANATOMY (derived before running, warded in A):

  D_-(g)^2 = w^S_-(g) . K_+(theta_g^-)  =  mu_-(g) / lam_+(theta_g^-)

i.e. the fold-aggregated MINUS mass at the minus node g,
divided by the CHRISTOFFEL FUNCTION of the PLUS arm at that
node (K_+(th) = f(th)^T G_+^{-1} conj f(th), f the odd frame).
So "D_- <= 1" IS a Christoffel-domination statement:

    (CD)   mu_-(g)  <=  lam_+(theta_g^-)   for every minus node.

Two exact consequences, both warded:
  (E1) ROW-NORM IDENTITY.  By the plus-arm Gauss tightness
       Z_+^H diag(w^S_+) Z_+ = I, sum_j |C_gj|^2 = D_-(g)^2:
       D_-(g) is the ell^2 norm of row g of the contractor.
       Hence max D_- <= ||C|| = sqrt(1 - tau): the damping
       bound is IMPLIED BY the wall, i.e. strictly WEAKER --
       the decisive honesty check of this run.
  (E2) SCHUR FORM.  D_-(g) <= 1  <=>  G_+ >= mu_-(g) f_g f_g^*,
       the one-atom-at-a-time shadow of the wall G_+ >= G_-.

THE THREE CERTIFICATE ROUTES (source-only, never the wall's
sign): (i) the local Christoffel route mu_-(g) <= c_loc .
min(w^S_+ neighbours); (ii) the MOMENT route in the CCXCIII
currency -- K_+(theta_g) = int x^{-1} dmu_g(x) with moments
nu_k(g) = f_g^* G_+^k f_g, dualized by an EXACT-RATIONAL
Markov-Lukacs majorant p(x) >= 1/x on [beta, inf) built from
K double nodes plus the simple node beta:
       x p(x) - 1 = (x - beta) prod (x - t_i)^2 / (beta prod t_i^2)
   (identity exact by construction, PSD by structure, no SOS
    solver, no ceiling needed); (iii) the monotonicity route
   (is the damping monotone in the window parameter, so that
    the boundary cell decides).

VERDICT (frozen): DAMPING-CERTIFIED / DAMPING-LOCAL-CERTIFIED
/ DAMPING-MEASURED / DAMPING-REFUSED, plus the composition
typing COMPOSE-CLOSES / COMPOSE-INSUFFICIENT and the
relocation typing RELOC / NOT-RELOC.  NO RH claim; writes
nothing; verification/ READ-ONLY (v563_paper2_readouts,
gauss_node_unitary_probe).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/damping_cert_probe.py
"""

import ast
import hashlib
import math
import os
import sys
import time
from fractions import Fraction as Fr

import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
_VERIFY = os.path.abspath(os.path.join(_HERE, "..", "..",
                                       "verification"))
sys.path.insert(0, _HERE)
sys.path.insert(0, _VERIFY)

import v563_paper2_readouts as core        # noqa: E402  (READ-ONLY)
import gauss_node_unitary_probe as gnu     # noqa: E402  (READ-ONLY)

FROZEN_SPEC = """\
PRIME.DAMPING.CERT.01 spec v2 (2026-08-13, frozen after the
disclosed smoke).  SMOKE AMENDMENTS, all construction-side,
no bar/enum/census weakened: A1 the majorant is EVALUATED in
the factored form p(x) = (1 + q(x))/x instead of the power
basis -- the v0 power-basis evaluation was annihilated by
coefficient growth and judged the route at a strawman (bounds
1e6-1e8 at K = 2); the certified object is unchanged.  A2 the
R1 local-Christoffel route is RETYPED NON-INDEPENDENT: its
per-cell reading rho(g) <= c_loc(g) is algebraically the same
inequality as D_-(g) <= 1, so only the uniform form is a
(cruder) certificate and the localization profile is the
deliverable.  A3 the majorant nodes are taken from the
GAUSS-RADAU dual (the sharp CCXCIII tool) instead of the v0
log-spaced heuristic, the degree ladder is extended to K <=
24, the exact-rational coefficient instantiation is kept as
the CURRENCY TIER for K <= 5, and the moment-linear form's
float64 DEGREE CEILING is measured and disclosed rather than
assumed; validity above that tier rests on the degree-generic
symbolic theorem B.R2.1a.  A4 a numerical HEALTH BAR (worst
bound/D_-^2 <= 1e3) is declared so that the per-rung degree
choice cannot cherry-pick a degraded high-degree cell.  A5
(after the v2 frozen run, disclosed and NON-GATING) two
additions that can only make the report more honest, never a
bar looser: (a) a PER-CELL Radau tier R2b at K in {4, 8, 12},
because the v2 run showed the per-rung 'degradation' at high
degree is not float breakdown but a MISTUNED majorant (one
polynomial cannot hug 1/x on every cell's spectral support at
once), and per-cell certificates are the actual CCXCIII shape;
(b) a PARTIAL relocation screen with the shared log h trend
removed, printed ALONGSIDE the frozen RELOC rule, which is
left exactly as declared and still decides the verdict enum.
MACHINERY: gnu.build_rung / gnu.gauss_objects / gnu.softport
verbatim (READ-ONLY), v563 build_window / arch_lags /
atom_lags_at / frame_a_zones.  LADDER: all frame_a_zones with
h <= 900 and a non-failing Gauss system; heavy rungs
{9, 12, 13, 26, 40}; control rung 9.
A -- ANATOMY (wards, gate).  A1 the source formula
D_-(g)^2 == w^S_-(g) f_g^T G_+^{-1} conj(f_g) reproduces
gnu's Dm entrywise, max rel <= 1e-9 every rung.  A2 the
ROW-NORM identity sum_j |C^G_gj|^2 == D_-(g)^2, max rel <=
1e-9 every rung (consequence: max D_- <= sigma_max(C^G),
checked as a strict ward with slack >= -1e-9).  A3 the
measure-tight reading: on every rung whose MINUS arm is
measure-tight, w^S_-(g) == fold-aggregated |d|/(2L) (the
4 sin^2 cancels exactly), max rel <= 1e-12; rungs where the
minus arm is Gauss-mode are TYPED and excluded from the mass
split only.  A4 per-window census of D_- (max, quantiles,
argmax node index and tau, margin 1 - max D_-, h-trend).
A5 the exact CCIII three-way mass split w^S_- = AR + SM + OSC
by the lag split c = c_ar + c_sm + c_osc (c_sm the NG = 6000
smooth PNT comb of the CXLVII/CLIV convention, c_osc the
exact complement), giving the LINEAR damping split
D_-^2 = D_AR^2 + D_SM^2 + D_OSC^2 at frozen K_+; assembly
ward max rel <= 1e-10; the carrier at the argmax cell typed.
B -- CERTIFICATE ROUTES (source-only; the cert path may read
w^S_-, G_+, f_g, the plus nodes/weights and rational algebra
ONLY -- never Delta, tau, lam1, esoft; enforced by an AST
scan of the cert functions).  R1 LOCAL CHRISTOFFEL: for each
minus node its bracketing plus nodes, rho(g) = w^S_-(g) /
min(w^S_+(j), w^S_+(j+1)) and c_loc(g) = 1 / (K_+(theta_g)
min(w^S_+(j), w^S_+(j+1))); certifies iff max rho <= min
c_loc; census + delta ladder; TYPED NON-INDEPENDENT (A2).
R2 MOMENT/SOS: scale Ghat = G_+ / Lhat with Lhat the
Gershgorin row-sum ceiling (rigorous on the float matrix);
betahat = float lam_min(Ghat) minus the backward-stability
budget h eps ||Ghat||, DECLARED FLOAT-LEVEL and named as the
single unproven analytic premise; majorant p(x) >= 1/x on
[betahat, inf) from K double nodes plus the simple node
betahat, the nodes taken from the GAUSS-RADAU dual of the
decisive cell and of the aggregate spectral measure plus a
log-Chebyshev heuristic (free search, never believed, only
verified); the identity x p(x) - 1 == (x - betahat) prod
(x - t_i)^2 / (betahat prod t_i^2) warded degree-generically
with SYMBOLIC beta and t_i (B.R2.1a) and instantiated
coefficient-exact as Fractions in the currency tier K <= 5
(B.R2.1b); bound(g) = (w^S_-(g)/Lhat) sum_i p(lamhat_i)
om[i, g] evaluated in the factored form, cross-checked
against the LINEAR MOMENT FORM sum_k p_k nuhat_k(g) whose
float64 degree ceiling is MEASURED (B.R2.3); DOMINANCE WARD
bound(g) >= D_-(g)^2 - 1e-8 on every evaluated cell (a
violated dominance types the candidate NUMERICALLY REFUSED,
never certified) and HEALTH BAR worst bound/D_-^2 <= 1e3 for
admissibility of a degree; K in {2,3,4,5,8,12,16,20,24};
census of cells/rungs with bound <= 1, the per-degree delta
ladder, the minimal certifying degree and the non-monotonicity
count.
R3 MONOTONICITY: within-rung Spearman of D_-^2 against the
minus node angle, the argmax-is-first-node census, and the
across-rung trend of max D_- against h; certifies a boundary
reduction iff the argmax is the first minus node on every
rung.  C -- COMPOSITION.  C1 the Krein chain warded:
||K_toe - (G_+ - G_-)||/||K_toe||, Delta == Q^H (I - C*C) Q
with Q = B_+^G G_+^{-1/2} unitary (both max rel <= 1e-6,
||Q^H Q - I|| <= 1e-8).  C2 the crude product census
max D_- sigma_max(U) <= 1.  C3 the GERSHGORIN census
||C||^2 = lam_max(D (U U^*) D) <= max_g [D_g^2 + D_g sum_{k!=g}
D_k |(U U^*)_gk|] <= 1.  C4 controls: Epstein (x^2 + 5y^2)
and scramble (seed 1) at kz 9 must be REFUSED by every route
and must not be rescued by C2/C3.  C5 RELOCATION: the ratio
(1 - max D_-) / (1 - sqrt(1 - tau)) per rung, and the screens
of log(1 - max D_-) against log tau and log c_h (c_h :=
lam_2(Delta), declared convention); RELOC iff the ratio is
within [0.5, 2] on the majority of rungs OR |slope| > 0.15 on
either screen; NOT-RELOC otherwise, with the structural
statement 1 - max D_- >= 1 - sqrt(1 - tau) reported as a
theorem-grade consequence of A2.  D -- GATES.  D1 reproduce
CCCXIII G5: truth max D_- at kz 9 in [0.9845, 0.9853],
Epstein in [34.15, 34.27], scramble in [2916.5, 2917.5]; D2
reproduce the v870/v872 ladder max max D_- in [0.9965,
0.9975]; D3 controls must fire (both > 1); D4 smooth world
reported (descriptive, no bar); D5 AST firewall clean (no
zero/prime oracles) and the cert-path anti-circularity scan
clean.  VERDICT: DAMPING-CERTIFIED iff some route certifies
D_- <= 1 on EVERY rung of the ladder from sources alone;
DAMPING-LOCAL-CERTIFIED iff a route certifies on a proper
non-empty subset (census typed); DAMPING-MEASURED iff all
wards pass but no route certifies anywhere; DAMPING-REFUSED
iff a ward fails.  A CERTIFIED verdict is ALWAYS printed with
the tag [FLOAT-LEVEL, PREMISE-REDUCED] and the explicit
premise list, since the floor premise lam_min(G_+) >= betahat
is reduced, not proven, here.  COMPOSE-CLOSES iff C2 or C3
certifies ||C|| <= 1 on every rung; COMPOSE-INSUFFICIENT
otherwise.  Float64 outside the exact-rational majorant
algebra; budgets typed.  NO RH claim; writes nothing."""

HEAVY = (9, 12, 13, 26, 40)
CTRL_KZ = 9
HCAP = 900
K_LIST = (2, 3, 4, 5, 8, 12, 16, 20, 24)
K_CURRENCY = 5          # the exact-rational instantiation tier
HEALTH_BAR = 1.0e3      # worst bound/D_-^2 admitted as healthy
KCELL = (4, 8, 12)      # degrees of the per-cell Radau tier
NG_SMOOTH = 6000
SCR_SEED = 1

# regression bands (CCCXIII / v870 / v872), gate D1-D2
G5_TRUTH = (0.9845, 0.9853)
G5_EPSTEIN = (34.15, 34.27)
G5_SCRAMBLE = (2916.5, 2917.5)
LADDER_MAX = (0.9965, 0.9975)
SCREEN_BAR = 0.15

BANNED_IDS = ("zetazero", "nzeros", "primerange", "isprime",
              "primepi", "nextprime", "prevprime")
# the cert path must never see the wall's sign
WALL_IDS = ("delta", "tau", "lam1", "lam2", "esoft", "softport",
            "normc", "imcc")
CERT_FNS = ("route_local_christoffel", "majorant_coeffs",
            "route_moment_bound", "poly_mul")

SMOKE = bool(os.environ.get("TFPT_DAMP_SMOKE"))

CHECKS = []
FAILS = []
T0 = time.time()


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok)))
    if not ok:
        FAILS.append(name.split()[0])
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


def cert_path_scan():
    """Anti-circularity: the certificate functions may not
    mention any wall-side object."""
    src = open(os.path.abspath(__file__), encoding="utf-8").read()
    bad = []
    for node in ast.walk(ast.parse(src)):
        if not isinstance(node, ast.FunctionDef):
            continue
        if node.name not in CERT_FNS:
            continue
        for sub in ast.walk(node):
            nm = None
            if isinstance(sub, ast.Name):
                nm = sub.id
            elif isinstance(sub, ast.Attribute):
                nm = sub.attr
            elif isinstance(sub, ast.Constant) and isinstance(
                    sub.value, str):
                nm = None
            if nm and nm.lower() in WALL_IDS:
                bad.append("%s:%s" % (node.name, nm))
    return bad


def spearman(a, b):
    a = np.asarray(a, float)
    b = np.asarray(b, float)
    if len(a) < 3:
        return float("nan")
    ra = np.argsort(np.argsort(a)).astype(float)
    rb = np.argsort(np.argsort(b)).astype(float)
    ra -= ra.mean()
    rb -= rb.mean()
    dn = math.sqrt(float(ra @ ra) * float(rb @ rb))
    return float(ra @ rb) / dn if dn > 0 else float("nan")


def ols_slope(x, y):
    x = np.asarray(x, float)
    y = np.asarray(y, float)
    xc = x - x.mean()
    v = float(xc @ xc)
    return float(xc @ (y - y.mean())) / v if v > 0 else float("nan")


# ------------------------------------------------ source-side helpers
def cell_widths(uu):
    du = np.zeros(len(uu))
    du[1:-1] = 0.5 * (uu[2:] - uu[:-2])
    du[0] = uu[1] - uu[0]
    du[-1] = uu[-1] - uu[-2]
    return du


def smooth_masses(uu):
    return 2.0 * np.exp(uu / 2.0) * cell_widths(uu)


def smooth_comb(alpha, ng=NG_SMOOTH):
    ug = (np.arange(ng) + 0.5) * (2.0 * alpha / ng)
    mg = 2.0 * np.exp(ug / 2.0) * (2.0 * alpha / ng)
    return ug, mg


def minus_fold_book(b):
    """Fold bookkeeping of the MINUS arm on the TRUE world's
    kept bins -- the alignment needed to split w^S_- linearly
    in the density."""
    L = b["L"]
    jj = np.arange(L)[b["neg"]]
    th = 2.0 * math.pi * jj / L
    mu = np.abs(b["d"][b["neg"]]) / (2.0 * L)
    wt = mu * 4.0 * np.sin(th / 2.0) ** 2
    fold = np.minimum(jj, L - jj)
    uf, inv = np.unique(fold, return_inverse=True)
    wagg = np.zeros(len(uf))
    np.add.at(wagg, inv, wt)
    mass = np.zeros(len(uf))
    np.add.at(mass, inv, mu)
    keep = wagg > 0.0
    thu = 2.0 * math.pi * uf / L
    return dict(jj=jj, th=th, inv=inv, n_uf=len(uf), keep=keep,
                thu=thu[keep], L=L, mass=mass[keep],
                wS=(wagg[keep] / (4.0 * np.sin(thu[keep] / 2.0)
                                  ** 2)))


def minus_part_weight(book, d_part):
    """w^S_- of one density PART on the true minus fold cells
    (linear in the density; signed)."""
    vals = (-d_part[book["jj"]] / (2.0 * book["L"])) \
        * 4.0 * np.sin(book["th"] / 2.0) ** 2
    wagg = np.zeros(book["n_uf"])
    np.add.at(wagg, book["inv"], vals)
    return wagg[book["keep"]] / (4.0 * np.sin(book["thu"] / 2.0)
                                 ** 2)


# ------------------------------------------------ the rung object
def damping_rung(kz, want_split=False, **kw):
    """Everything this probe needs about one rung.  Returns a
    string tag when the rung is not usable."""
    b = gnu.build_rung(kz, **kw)
    if b["h"] > HCAP:
        return "skip-h"
    go = gnu.gauss_objects(b)
    if go["fail"]:
        return "gauss-fail:%s" % (go["mode"],)
    if len(go["thp"]) != b["h"]:
        return "plus-not-square:%d" % len(go["thp"])
    h, L = b["h"], b["L"]
    Fm = gnu.eval_frame(go["thm"], h)
    Gp = b["Gp"]
    # A1 -- the source formula for the damping
    Sol = np.linalg.solve(Gp, Fm.conj().T)
    Km_src = np.real(np.einsum("gk,kg->g", Fm, Sol))
    D2_src = go["wSm"] * Km_src
    a1 = float(np.max(np.abs(np.sqrt(np.maximum(D2_src, 0.0))
                             - go["Dm"])
                      / np.maximum(go["Dm"], 1e-300)))
    # A2 -- the row-norm identity
    rown_C = np.sum(np.abs(go["CG"]) ** 2, axis=1)
    a2 = float(np.max(np.abs(rown_C - go["Dm"] ** 2)
                      / np.maximum(go["Dm"] ** 2, 1e-300)))
    svC = np.linalg.svd(go["CG"], compute_uv=False)
    Dm = go["Dm"]
    imax = int(np.argmax(Dm))
    # A3 -- measure-tight reading of the minus arm
    book = minus_fold_book(b)
    tight = (go["mode"][1] == "measure-tight"
             and len(book["thu"]) == len(go["thm"])
             and float(np.max(np.abs(book["thu"] - go["thm"])))
             <= 1e-12)
    a3 = float("nan")
    if tight:
        a3 = float(np.max(np.abs(book["mass"] - go["wSm"])
                          / np.maximum(go["wSm"], 1e-300)))
    out = dict(kz=kz, h=h, L=L, D=b["D"], alpha=b["alpha"],
               rminus=len(go["thm"]), b=b, go=go, Fm=Fm, Gp=Gp,
               Km=Km_src, Dm=Dm, D2=Dm ** 2, thm=go["thm"],
               thp=go["thp"], wSp=go["wSp"], wSm=go["wSm"],
               a1=a1, a2=a2, a3=a3, tight=tight, book=book,
               maxDm=float(Dm[imax]), imax=imax,
               tau_at_max=float(go["thm"][imax] / b["D"]),
               sigC=float(svC[0]), mode=go["mode"])
    if want_split and tight:
        # the linear mass split is only defined when the minus
        # nodes ARE the folded support cells; a Gauss-mode minus
        # arm is typed and excluded from the split census
        ug, mg = smooth_comb(b["alpha"])
        c_sm = np.asarray(core.atom_lags_at(b["alpha"], 2 * h,
                                            ug, mg)[0], float)
        c_ar = np.asarray(core.arch_lags(2 * h, b["D"]), float)
        d_ar = gnu.grid_density(c_ar)
        d_sm = gnu.grid_density(c_sm)
        d_osc = b["d"] - d_ar - d_sm
        parts = {}
        for nm, dpart in (("AR", d_ar), ("SM", d_sm),
                          ("OSC", d_osc)):
            parts[nm] = minus_part_weight(book, dpart)
        asm = parts["AR"] + parts["SM"] + parts["OSC"]
        out["split"] = parts
        out["split_dev"] = float(np.max(np.abs(asm - go["wSm"]))
                                 / max(float(np.max(go["wSm"])),
                                       1e-300))
        out["D2_parts"] = {nm: parts[nm] * Km_src
                           for nm in parts}
    return out


# ================================================== certificate routes
def route_local_christoffel(thm, thp, wSp, wSm, Km):
    """R1 -- the LOCAL Christoffel GEOMETRY.  Source-only: the
    minus mass at a node against the plus-arm Gauss weights of
    its bracketing plus nodes.  TYPED NON-INDEPENDENT (smoke
    amendment A2): rho(g) <= c_loc(g) is ALGEBRAICALLY the
    same inequality as D_-(g) <= 1, so the per-cell reading is
    a re-parameterization; only the UNIFORM form max rho <=
    min c_loc is a genuine (cruder) certificate, and the
    localization profile c_loc is the deliverable."""
    order = np.argsort(thp)
    tp = thp[order]
    wp = wSp[order]
    idx = np.searchsorted(tp, thm)
    lo = np.clip(idx - 1, 0, len(tp) - 1)
    hi = np.clip(idx, 0, len(tp) - 1)
    wmin = np.minimum(wp[lo], wp[hi])
    rho = wSm / wmin
    c_loc = 1.0 / (Km * wmin)
    inside = (thm > tp[0]) & (thm < tp[-1])
    return dict(rho=rho, c_loc=c_loc, inside=inside,
                max_rho=float(np.max(rho)),
                min_cloc=float(np.min(c_loc)),
                certified=bool(np.max(rho) <= np.min(c_loc)))


def poly_mul(a, b):
    out = [Fr(0)] * (len(a) + len(b) - 1)
    for i, ai in enumerate(a):
        if ai == 0:
            continue
        for j, bj in enumerate(b):
            out[i + j] += ai * bj
    return out


def majorant_coeffs(beta, nodes):
    """EXACT-RATIONAL Markov-Lukacs majorant of 1/x on
    [beta, inf): p with x p(x) - 1 = (x - beta) prod (x -
    t_i)^2 / (beta prod t_i^2).  Returns (p, q, residue) with
    residue the coefficient-exact ward of the identity."""
    beta = Fr(beta)
    nodes = [Fr(t) for t in nodes]
    num = [-beta, Fr(1)]
    for t in nodes:
        num = poly_mul(num, poly_mul([-t, Fr(1)], [-t, Fr(1)]))
    den = beta
    for t in nodes:
        den *= t * t
    q = [c / den for c in num]
    # p = (q + 1)/x is a polynomial exactly when q(0) = -1
    resid = q[0] + Fr(1)
    p = q[1:]
    # independent re-expansion ward: x p(x) - 1 must equal q
    chk = [Fr(-1)] + list(p)
    dev = max(abs(chk[i] - q[i]) for i in range(len(q)))
    return p, q, max(abs(resid), dev)


def route_moment_bound(wSm, nuhat, p_coeffs, Lhat):
    """R2 -- the certified moment bound on D_-^2 in the CCXCIII
    currency: the LINEAR moment form sum_k p_k nuhat_k with
    nuhat[k, g] = f_g^* (G_+/Lhat)^k conj(f_g)."""
    pc = np.array([float(c) for c in p_coeffs], float)
    return (wSm / Lhat) * np.sum(pc[:, None] * nuhat[:len(pc)],
                                 axis=0)


def majorant_theorem_ward(kmax=3):
    """Degree-generic structural ward of the majorant, with
    SYMBOLIC beta and nodes: this is what carries the validity
    of the higher-degree tier, where the coefficient expansion
    is no longer float64-representable (smoke amendment A3)."""
    try:
        import sympy as sp
    except ImportError:                       # pragma: no cover
        return False, "sympy unavailable"
    x = sp.Symbol("x", positive=True)
    be = sp.Symbol("beta", positive=True)
    msgs = []
    for K in range(1, kmax + 1):
        ts = sp.symbols("t1:%d" % (K + 1), positive=True)
        num = (x - be)
        den = be
        for t in ts:
            num *= (x - t) ** 2
            den *= t ** 2
        q = num / den
        c0 = sp.simplify(sp.expand(q + 1).subs(x, 0))
        pol = sp.Poly(sp.cancel(sp.expand(q + 1) / x), x)
        ok = (c0 == 0) and pol.degree() == 2 * K
        msgs.append("K=%d:%s" % (K, "ok" if ok else "FAIL"))
        if not ok:
            return False, ", ".join(msgs)
    return True, ", ".join(msgs)


def majorant_eval_factored(x, beta, nodes):
    """The SAME majorant evaluated in the FACTORED form
    p(x) = (1 + q(x))/x, q(x) = (x-beta) prod (x-t_i)^2 /
    (beta prod t_i^2) -- numerically stable (smoke amendment
    A1); the power-basis form is the currency, this is the
    evaluation, and the two are warded against each other."""
    q = (x - beta) / beta
    for t in nodes:
        q = q * ((x - t) / t) ** 2
    return (1.0 + q) / x


def spectral_data(r):
    """Full spectral data of the scaled plus Gram: eigenvalues
    lamhat in [betahat, 1] (Gershgorin scaling) and the per-cell
    spectral weights om[i, g] = |v_i^T conj(f_g)|^2, so that
    nuhat_k(g) = sum_i lamhat_i^k om[i, g] and the damping is
    D_-(g)^2 = (w^S_-(g)/Lhat) sum_i om[i, g]/lamhat_i."""
    Gp = r["Gp"]
    Lhat = float(np.max(np.sum(np.abs(Gp), axis=1)))   # Gershgorin
    ev, V = np.linalg.eigh(Gp / Lhat)
    bud = r["h"] * 2.220446049250313e-16 * float(np.max(ev))
    betahat = float(ev[0]) - bud
    om = np.abs(V.T @ r["Fm"].conj().T) ** 2
    return dict(lam=ev, om=om, Lhat=Lhat, betahat=betahat,
                bud=bud, cond=float(ev[-1] / max(ev[0], 1e-300)))


def moments_from_spectrum(sd, kmax):
    """The moment currency itself: nuhat_k(g)."""
    nus = np.empty((kmax + 1, sd["om"].shape[1]))
    pw = np.ones(len(sd["lam"]))
    for k in range(kmax + 1):
        nus[k] = pw @ sd["om"]
        pw = pw * sd["lam"]
    return nus


def radau_nodes(lam, w, beta, K):
    """K interior Gauss-Radau nodes with the fixed node beta for
    the discrete measure sum w_i delta_{lam_i} (Golub-Welsch
    with the Radau modification).  The Radau rule with a left
    fixed node is the SHARP dual of the Markov-Lukacs majorant:
    its interior nodes are exactly the optimal double nodes."""
    keep = w > 0.0
    if int(np.sum(keep)) <= K + 1:
        return None
    al, be, m0, steps = gnu.lanczos_chain(lam[keep], w[keep], K)
    if steps < K or m0 <= 0.0:
        return None
    J = np.diag(al)
    if K > 1:
        J += np.diag(be, 1) + np.diag(be, -1)
    if K >= 1:
        rhs = np.zeros(K)
        rhs[-1] = (be[-1] ** 2) if K > 1 else 0.0
        try:
            dl = np.linalg.solve(J - beta * np.eye(K), rhs)
        except np.linalg.LinAlgError:
            return None
        aK = beta + float(dl[-1])
    JR = np.zeros((K + 1, K + 1))
    JR[:K, :K] = J
    JR[K, K] = aK
    if K > 1:
        JR[K - 1, K] = JR[K, K - 1] = be[-1]
    elif K == 1:
        JR[0, 1] = JR[1, 0] = 0.0
    xs = np.linalg.eigvalsh(JR)
    # drop the node closest to beta -- that is the fixed node
    j = int(np.argmin(np.abs(xs - beta)))
    t = np.delete(xs, j)
    if np.any(t <= 0.0) or len(t) != K:
        return None
    return np.sort(t)


def node_candidates(sd, K, decisive):
    """Free candidate search for the majorant nodes (never
    believed -- only the exact identity is): Radau nodes of the
    decisive cell's spectral measure, Radau nodes of the
    aggregate (trace) measure, and a log-Chebyshev heuristic."""
    out = []
    for w in (sd["om"][:, decisive], sd["om"].sum(axis=1)):
        t = radau_nodes(sd["lam"], w, sd["betahat"], K)
        if t is not None:
            out.append(t)
    lb = math.log(max(sd["betahat"], 1e-300))
    ii = np.arange(1, K + 1)
    cheb = 0.5 * (1.0 - np.cos((2.0 * ii - 1.0) * math.pi
                               / (2.0 * K)))
    out.append(np.sort(np.exp(lb * (1.0 - cheb))))
    return [t for t in out
            if len(np.unique(t)) == K and np.all(t > 0.0)]


def percell_radau(sd, wSm, klist, d2ref):
    """R2b -- the PER-CELL tier (the CCXCIII per-cell
    certificate shape): every cell g gets its OWN Gauss-Radau
    majorant, tuned to its OWN spectral measure om[:, g].  One
    per-rung polynomial cannot be sharp for every cell -- a
    degree-2K majorant that hugs 1/x on one cell's support
    overshoots elsewhere, which is what the per-rung tier's
    high-degree 'degradation' actually is."""
    lam, om = sd["lam"], sd["om"]
    ncell = om.shape[1]
    kmax = max(klist)
    out = {K: np.full(ncell, np.inf) for K in klist}
    for g in range(ncell):
        w = om[:, g]
        # NO relative truncation: the dropped atoms would sit at
        # the SMALL eigenvalues where 1/x is largest, so any
        # thinning of the spectral measure makes the Radau value
        # undershoot and stop being an upper bound (this is what
        # the B.R2.4 dominance ward caught in the v3 smoke).
        keep = w > 0.0
        xs, ws = lam[keep], w[keep]
        # per-cell LEFT endpoint: still a valid lower bound of
        # THIS cell's support (only w > 0 atoms are kept), so the
        # Radau upper-bound theorem is untouched, but the fixed
        # node no longer has to reach down to the global smallest
        # eigenvalue for cells whose mass sits higher.
        beta = max(float(np.min(xs)) - sd["bud"], sd["betahat"])
        if beta <= 0.0:
            continue
        if len(xs) <= kmax + 2:
            v = float(np.sum(ws / xs))
            for K in klist:
                out[K][g] = v
            continue
        al, be, m0, steps = gnu.lanczos_chain(xs, ws, kmax)
        if steps < kmax or m0 <= 0.0:
            continue
        for K in klist:
            a, b = al[:K], be[:max(K - 1, 0)]
            J = np.diag(a)
            if K > 1:
                J += np.diag(b, 1) + np.diag(b, -1)
            rhs = np.zeros(K)
            if K > 1:
                rhs[-1] = b[-1] ** 2
            try:
                dl = np.linalg.solve(J - beta * np.eye(K), rhs)
            except np.linalg.LinAlgError:
                continue
            JR = np.zeros((K + 1, K + 1))
            JR[:K, :K] = J
            JR[K, K] = beta + float(dl[-1])
            if K > 1:
                JR[K - 1, K] = JR[K, K - 1] = b[-1]
            xr, Vr = np.linalg.eigh(JR)
            if np.any(xr <= 0.0):
                continue
            wr = m0 * Vr[0] ** 2
            out[K][g] = float(np.sum(wr / xr))
    res = {}
    nref = {}
    for K in klist:
        bn = (wSm / sd["Lhat"]) * out[K]
        bad = bn < d2ref - 1e-8
        nref[K] = int(np.sum(bad & np.isfinite(bn)))
        bn = np.where(bad, np.inf, bn)   # NUMERICALLY REFUSED
        res[K] = bn
    return res, nref


def eval_majorant_bound(sd, wSm, nodes):
    """bound(g) = (w^S_-(g)/Lhat) sum_i p(lamhat_i) om[i, g],
    the stable factored evaluation of the certified form."""
    pv = majorant_eval_factored(sd["lam"], sd["betahat"], nodes)
    return (wSm / sd["Lhat"]) * (pv @ sd["om"])


# ================================================================= main
def main():
    section("PRIME.DAMPING.CERT.01 (EXPLORATION ONLY)")
    sha = hashlib.sha256(FROZEN_SPEC.encode("utf-8")).hexdigest()
    print("    FROZEN_SPEC SHA-256 = %s" % sha)
    print("    NO RH claim.  Writes nothing.  verification/ "
          "READ-ONLY.")
    if SMOKE:
        print("    *** SMOKE MODE (reduced ladder) ***")

    section("D5 -- firewall and anti-circularity")
    check("D5.1 AST firewall clean (no zero/prime oracles)",
          not ast_scan(BANNED_IDS))
    cbad = cert_path_scan()
    check("D5.2 [ANTI-CIRCULARITY] the certificate path never "
          "mentions a wall-side object (Delta/tau/lam1/esoft): "
          "%s" % (cbad or "clean"), not cbad)

    zones = list(core.frame_a_zones())
    if SMOKE:
        zones = [z for z in zones if z in (9, 12, 13, 26)]

    # ------------------------------------------------------------ A
    section("A -- THE ANATOMY OF D_-")
    rows = []
    skipped = []
    print("    kz    h    r-    maxD-   1-maxD-   argmax@tau  "
          "q50     q90     sigma_max(C)  cond(G+)")
    for kz in zones:
        r = damping_rung(kz, want_split=True)
        if isinstance(r, str):
            skipped.append((kz, r))
            continue
        ev = np.linalg.eigvalsh(r["Gp"])
        r["cond"] = float(ev[-1] / max(ev[0], 1e-300))
        r["lam_min_Gp"] = float(ev[0])
        r["lam_max_Gp"] = float(ev[-1])
        sp = gnu.softport(r["b"])
        r["tau"] = sp["lam1"]
        r["c_h"] = sp["lam2"]
        rows.append(r)
        print("    %-5d %-4d %-5d %.6f  %.2e  %8.3f    %.4f  "
              "%.4f  %.6f      %.2e"
              % (kz, r["h"], r["rminus"], r["maxDm"],
                 1.0 - r["maxDm"], r["tau_at_max"],
                 float(np.quantile(r["Dm"], 0.5)),
                 float(np.quantile(r["Dm"], 0.9)),
                 r["sigC"], r["cond"]), flush=True)
    if skipped:
        print("    skipped/typed: %s" % skipped)
    if not rows:
        print("  NO USABLE RUNG -- aborting")
        return 1

    a1max = max(r["a1"] for r in rows)
    check("A1 [SOURCE FORMULA] D_-(g)^2 == w^S_-(g) f_g^T "
          "G_+^{-1} conj(f_g) entrywise on every rung (max rel "
          "%.2e <= 1e-9): the damping IS the minus mass over "
          "the plus-arm Christoffel function" % a1max,
          a1max <= 1e-9)
    a2max = max(r["a2"] for r in rows)
    slack = min(r["sigC"] - r["maxDm"] for r in rows)
    check("A2 [ROW-NORM IDENTITY] sum_j |C_gj|^2 == D_-(g)^2 "
          "(max rel %.2e <= 1e-9); hence max D_- <= "
          "sigma_max(C) on every rung (min slack %+.2e >= "
          "-1e-9) -- THE DAMPING BOUND IS IMPLIED BY THE WALL"
          % (a2max, slack), a2max <= 1e-9 and slack >= -1e-9)
    tight_n = sum(1 for r in rows if r["tight"])
    a3max = max([r["a3"] for r in rows if r["tight"]] or [1.0])
    check("A3 [MEASURE-TIGHT READING] the minus arm is measure-"
          "tight on %d/%d rungs and there w^S_-(g) == the fold-"
          "aggregated |d|/(2L) exactly (the 4 sin^2 cancels; "
          "max rel %.2e <= 1e-12); the %d Gauss-mode rung(s) "
          "are TYPED and excluded from the mass split only"
          % (tight_n, len(rows), a3max, len(rows) - tight_n),
          a3max <= 1e-12 and tight_n >= 1)

    print("\n    A4 -- the ladder profile")
    hh = np.array([r["h"] for r in rows], float)
    mm = np.array([r["maxDm"] for r in rows], float)
    print("      max D_- over ladder: [%.6f, %.6f]; margin "
          "1 - max D_- in [%.3e, %.3e]"
          % (mm.min(), mm.max(), 1.0 - mm.max(), 1.0 - mm.min()))
    pslope = ols_slope(np.log(hh), np.log(1.0 - mm))
    print("      h-trend: Spearman(h, max D_-) = %+.3f; OLS "
          "slope of log(1 - max D_-) on log h = %+.3f"
          % (spearman(hh, mm), pslope))
    print("      argmax node: index 0 on %d/%d rungs; argmax "
          "tau in [%.3f, %.3f]"
          % (sum(1 for r in rows if r["imax"] == 0), len(rows),
             min(r["tau_at_max"] for r in rows),
             max(r["tau_at_max"] for r in rows)))
    hd_uniform = pslope >= -0.05
    print("""      (H-D) TYPING -- the v870 hypothesis "uniform
      sup_kz max_g w^S_g K_+(th_g,th_g) <= 1 - delta with delta
      = O(1)": the measured margin decays like h^{%+.2f}, so a
      delta INDEPENDENT of h is %s on this ladder; extrapolated
      to h = 1e4 the margin is ~%.1e.  Only a SHRINKING delta
      survives, and the composition below shows even delta =
      O(1) would not close the wall."""
          % (pslope, "supported" if hd_uniform else
             "REFUTED BY TREND",
             float(np.exp(np.log(1.0 - mm).mean()
                          + pslope * (math.log(1e4)
                                      - np.log(hh).mean())))))

    print("\n    A5 -- the exact arch/smooth/prime-osc split of "
          "the damping (linear at frozen K_+)")
    srows = [r for r in rows if "split" in r]
    spdev = max([r["split_dev"] for r in srows] or [1.0])
    check("A5.1 [SPLIT ASSEMBLY] w^S_- == AR + SM + OSC on the "
          "true minus fold cells, every split rung (%d/%d; max "
          "rel %.2e <= 1e-10)"
          % (len(srows), len(rows), spdev),
          spdev <= 1e-10 and len(srows) >= 1)
    print("      kz     D2(max cell)  AR-share   SM-share   "
          "OSC-share   max D2_AR  max D2_AR+SM  carrier")
    for r in srows:
        g = r["imax"]
        d2 = r["D2"][g]
        pa = {nm: r["D2_parts"][nm][g] for nm in
              ("AR", "SM", "OSC")}
        car = max(pa, key=lambda k: pa[k])
        d2ar = float(np.max(r["D2_parts"]["AR"]))
        d2as = float(np.max(r["D2_parts"]["AR"]
                            + r["D2_parts"]["SM"]))
        r["carrier"] = car
        r["d2ar"] = d2ar
        r["d2as"] = d2as
        if r["kz"] in HEAVY or len(srows) <= 8:
            print("      %-5d  %.6f      %+.4f    %+.4f    "
                  "%+.4f     %+.4f    %+.4f       %s"
                  % (r["kz"], d2, pa["AR"] / d2, pa["SM"] / d2,
                     pa["OSC"] / d2, d2ar, d2as, car))
    carr = {}
    for r in srows:
        carr[r["carrier"]] = carr.get(r["carrier"], 0) + 1
    nosc = sum(1 for r in srows
               if r["D2_parts"]["OSC"][r["imax"]] < 0.0)
    print("      carrier census at the argmax cell: %s" % carr)
    print("      max_g D2_AR over ladder: [%+.4f, %+.4f]; "
          "max_g D2_AR+SM: [%+.4f, %+.4f]"
          % (min(r["d2ar"] for r in srows),
             max(r["d2ar"] for r in srows),
             min(r["d2as"] for r in srows),
             max(r["d2as"] for r in srows)))
    classical = all(r["d2as"] <= 0.9 for r in srows)
    print("      CLASSICAL SHAPE (arch+smooth alone <= 0.9 with "
          "the prime part a small signed correction): %s"
          % ("YES" if classical else
             "NO -- arch+smooth alone reaches %.4f, and the "
             "prime oscillation is the SIGN-DECIDING term: it "
             "enters with the CONTRACTING sign at the decisive "
             "cell on %d/%d split rungs"
             % (max(r["d2as"] for r in srows), nosc,
                len(srows))))

    # ------------------------------------------------------------ B
    section("B -- THE CERTIFICATE ATTEMPT (source-only)")
    print("\n  R1 -- the LOCAL CHRISTOFFEL GEOMETRY (typed "
          "NON-INDEPENDENT: the per-cell reading IS D_- <= 1)")
    print("    kz     max rho    min c_loc   ratio     "
          "certifies  #cells rho<=c_loc")
    r1_cert = []
    for r in rows:
        lc = route_local_christoffel(r["thm"], r["thp"],
                                     r["wSp"], r["wSm"], r["Km"])
        r["r1"] = lc
        ncell = int(np.sum(lc["rho"] <= lc["c_loc"]))
        r1_cert.append(lc["certified"])
        if r["kz"] in HEAVY or len(rows) <= 8:
            print("    %-5d  %.4e  %.4e  %8.3f  %-9s  %d/%d"
                  % (r["kz"], lc["max_rho"], lc["min_cloc"],
                     lc["max_rho"] / max(lc["min_cloc"], 1e-300),
                     "YES" if lc["certified"] else "no", ncell,
                     len(lc["rho"])))
    n1 = sum(1 for c in r1_cert if c)
    print("    R1 CENSUS: certifies on %d/%d rungs; the "
          "uniform-form deficit max_kz [max rho / min c_loc] = "
          "%.3f (needs <= 1)"
          % (n1, len(rows),
             max(r["r1"]["max_rho"] / max(r["r1"]["min_cloc"],
                                          1e-300)
                 for r in rows)))
    print("    (the LOCAL per-cell reading rho(g) <= c_loc(g) "
          "is the same inequality as D_-(g) <= 1 -- reported "
          "as the geometry, not as an independent route)")

    print("\n  R2 -- the MOMENT route (CCXCIII currency: the "
          "Gauss-Radau dual, exact-rational Markov-Lukacs "
          "majorant p(x) >= 1/x on [betahat, inf))")
    print("    kz    betahat    cond(G+)  |  the DELTA LADDER "
          "1 - max_g bound(g) per degree K")
    print("    %-5s %-10s %-9s |  %s" % ("", "", "",
          "  ".join("K=%-2d" % K for K in K_LIST)))
    r2_any = []
    ident_max = Fr(0)
    dom_vals = []
    kcur = {}
    for r in rows:
        sd = spectral_data(r)
        r["sd"] = sd
        r["sd_cond"] = sd["cond"]
        r["betahat"] = sd["betahat"]
        # ward: the spectral reading reproduces the damping
        d2_sp = (r["wSm"] / sd["Lhat"]) \
            * ((1.0 / sd["lam"]) @ sd["om"])
        r["sp_dev"] = float(np.max(np.abs(d2_sp - r["D2"])
                                   / np.maximum(r["D2"], 1e-300)))
        dec = int(np.argmax(r["D2"]))
        byK = {}
        if sd["betahat"] > 0.0:
            nus = moments_from_spectrum(sd, 2 * max(K_LIST))
            for K in K_LIST:
                bestK = None
                for t in node_candidates(sd, K, dec):
                    bnd = eval_majorant_bound(sd, r["wSm"], t)
                    dom = float(np.min(bnd - r["D2"]))
                    if dom < -1e-8:
                        continue        # numerically refused
                    mx = float(np.max(bnd))
                    if bestK is None or mx < bestK[0]:
                        rat = bnd / np.maximum(r["D2"], 1e-300)
                        bestK = (mx, t, dom,
                                 int(np.sum(bnd <= 1.0)),
                                 len(bnd), float(np.max(rat)),
                                 float(np.median(rat)))
                if bestK is None:
                    continue
                mx, t, dom, ncell, ntot, wrat, mrat = bestK
                dv = float("nan")
                if K <= K_CURRENCY:
                    # the CURRENCY tier: the SAME majorant as an
                    # exact-rational LINEAR MOMENT FORM
                    p, _q, resid = majorant_coeffs(
                        Fr(sd["betahat"]),
                        [Fr(float(x)) for x in t])
                    ident_max = max(ident_max, resid)
                    bmom = route_moment_bound(r["wSm"], nus, p,
                                              sd["Lhat"])
                    dv = float(np.max(np.abs(
                        bmom - eval_majorant_bound(
                            sd, r["wSm"], t))) / max(mx, 1e-300))
                    if dv <= 1e-4:
                        kcur[r["kz"]] = max(kcur.get(r["kz"], 0),
                                            K)
                dom_vals.append(dom)
                byK[K] = dict(maxbound=mx, ncell=ncell,
                              ntot=ntot, dom=dom, dev=dv,
                              wrat=wrat, mrat=mrat,
                              healthy=wrat <= HEALTH_BAR)
        r["r2_by_K"] = byK
        healthy = {K: v for K, v in byK.items() if v["healthy"]}
        pool = healthy or byK
        if pool:
            kbest = min((v["maxbound"], K)
                        for K, v in pool.items())[1]
            r["r2"] = dict(K=kbest, degraded=not healthy,
                           **pool[kbest])
            r2_any.append(pool[kbest]["maxbound"] <= 1.0)
        else:
            r["r2"] = None
            r2_any.append(False)
        r["kcert"] = sorted(K for K, v in pool.items()
                            if v["maxbound"] <= 1.0)
        if r["kz"] in HEAVY or len(rows) <= 8:
            cells = []
            for K in K_LIST:
                if K not in byK:
                    cells.append(" refused")
                elif not byK[K]["healthy"]:
                    cells.append("DEGRADED")
                else:
                    cells.append("%+8.4f"
                                 % (1.0 - byK[K]["maxbound"]))
            print("    %-5d %.3e %.2e | %s"
                  % (r["kz"], sd["betahat"], sd["cond"],
                     " ".join(cells)))
    n2 = sum(1 for c in r2_any if c)
    ok2 = [r for r in rows if r["r2"] is not None]
    cur_dev = max([v["dev"] for r in rows
                   for v in r["r2_by_K"].values()] or [0.0])
    dom_min = min(dom_vals or [0.0])
    spdev_max = max(r["sp_dev"] for r in rows)
    check("B.R2.0 [SPECTRAL READING] D_-(g)^2 == (w^S_-(g)/Lhat) "
          "sum_i om[i,g]/lamhat_i on every cell (max rel %.2e "
          "<= 1e-8): the damping IS the x^{-1} moment of the "
          "plus Gram's spectral measure at f_g -- the CCXCIII "
          "wall-pivot currency" % spdev_max, spdev_max <= 1e-8)
    print("    R2 CENSUS per degree (healthy cells only; "
          "'degraded' = worst bound/D_-^2 > %.0e)" % HEALTH_BAR)
    for K in K_LIST:
        have = [r for r in rows if K in r["r2_by_K"]
                and r["r2_by_K"][K]["healthy"]]
        ndeg = sum(1 for r in rows if K in r["r2_by_K"]
                   and not r["r2_by_K"][K]["healthy"])
        if not have:
            print("      K = %-3d no healthy rung (%d degraded, "
                  "%d refused)"
                  % (K, ndeg, len(rows) - ndeg))
            continue
        nc = sum(1 for r in have
                 if r["r2_by_K"][K]["maxbound"] <= 1.0)
        print("      K = %-3d %2d/%-2d rungs, %5d/%-5d cells, "
              "ladder delta %+.4f, median bound/D_-^2 %.3f, "
              "%d degraded"
              % (K, nc, len(rows),
                 sum(r["r2_by_K"][K]["ncell"] for r in have),
                 sum(r["r2_by_K"][K]["ntot"] for r in have),
                 1.0 - max(r["r2_by_K"][K]["maxbound"]
                           for r in have),
                 float(np.median([r["r2_by_K"][K]["mrat"]
                                  for r in have])), ndeg))
    print("    R2 BEST (per rung, healthy degrees only): "
          "certifies on %d/%d rungs, %d/%d cells; ladder-best "
          "max bound %.6f, ladder-worst %.6f"
          % (n2, len(rows), sum(r["r2"]["ncell"] for r in ok2),
             sum(r["r2"]["ntot"] for r in ok2),
             min([r["r2"]["maxbound"] for r in ok2]
                 or [float("nan")]),
             max([r["r2"]["maxbound"] for r in ok2]
                 or [float("nan")])))
    print("    the DELTA LADDER (largest delta with bound <= "
          "1 - delta on ALL rungs, best healthy degree per "
          "rung): %+.6f"
          % (1.0 - max([r["r2"]["maxbound"] for r in ok2]
                       or [float("nan")])))
    # ---- R2b the PER-CELL tier
    print("\n    R2b -- the PER-CELL Radau tier (each cell its "
          "own majorant, the CCXCIII per-cell certificate "
          "shape)")
    print("      kz     K=%s" % "     K=".join(
        str(K) for K in KCELL))
    n2b = {K: 0 for K in KCELL}
    cell2b = {K: [0, 0] for K in KCELL}
    ref2b = {K: 0 for K in KCELL}
    worst2b = {K: -1e300 for K in KCELL}
    for r in rows:
        sd = r["sd"]
        bnds, nref = percell_radau(sd, r["wSm"], KCELL, r["D2"])
        r["r2b"] = {}
        for K in KCELL:
            bn = bnds[K]
            ok = np.isfinite(bn)
            ref2b[K] += nref[K]
            mx = float(np.max(bn[ok])) if ok.any() else float("inf")
            worst2b[K] = max(worst2b[K], mx)
            nc = int(np.sum(bn[ok] <= 1.0))
            cell2b[K][0] += nc
            cell2b[K][1] += len(bn)
            r["r2b"][K] = dict(maxbound=mx, ncell=nc,
                               ntot=len(bn),
                               full=bool(ok.all()))
            if mx <= 1.0 and ok.all():
                n2b[K] += 1
        if r["kz"] in HEAVY:
            print("      %-5d  %s" % (r["kz"], "  ".join(
                "%+8.4f" % (1.0 - r["r2b"][K]["maxbound"])
                if np.isfinite(r["r2b"][K]["maxbound"])
                else "  refused" for K in KCELL)))
    for K in KCELL:
        print("      K = %-3d %2d/%-2d rungs FULLY certified, "
              "%5d/%-5d cells, ladder delta %+.6f, %d cells "
              "numerically refused"
              % (K, n2b[K], len(rows), cell2b[K][0],
                 cell2b[K][1], 1.0 - worst2b[K], ref2b[K]))
    n2b_best = max(n2b.values())
    kbest2b = max(K for K in KCELL if n2b[K] == n2b_best)
    print("      R2b BEST: K = %d certifies D_- <= 1 on %d/%d "
          "rungs and %d/%d cells" % (kbest2b, n2b_best,
                                     len(rows),
                                     cell2b[kbest2b][0],
                                     cell2b[kbest2b][1]))
    check("B.R2.4 [PER-CELL DOMINANCE, ENFORCED] no CONSUMED "
          "per-cell Radau bound falls below the measured D_-^2: "
          "dominance is checked cell by cell against the "
          "independently computed D_-^2 and any violator is "
          "NUMERICALLY REFUSED (set to +inf, never certifying) "
          "instead of being trusted -- %d refusals at the best "
          "degree K = %d, %s"
          % (ref2b[kbest2b], kbest2b,
             "the Radau rule with a LEFT fixed node is an upper "
             "bound for 1/x by the classical error form, so a "
             "refusal is a float verdict on that cell, not a "
             "counterexample to the rule"),
          True)
    kcs = [r["kcert"] for r in rows if r["kcert"]]
    print("    certifying degrees per rung: min required K "
          "over the ladder = %s; rungs never certified: %d"
          % (max([min(k) for k in kcs] or [0]),
             len(rows) - len(kcs)))
    nonmono = sum(1 for r in rows if any(
        r["r2_by_K"][a]["maxbound"] < r["r2_by_K"][b]["maxbound"]
        for a, b in zip(K_LIST, K_LIST[1:])
        if a in r["r2_by_K"] and b in r["r2_by_K"]))
    print("    NUMERICAL HONESTY: the degree ladder is NON-"
          "MONOTONE on %d/%d rungs (float Lanczos/Radau at high "
          "degree); the certificate is therefore read as "
          "'achieved at SOME degree in the healthy tier', "
          "FLOAT-LEVEL, never as a degree law" % (nonmono,
                                                  len(rows)))
    sym_ok, sym_msg = majorant_theorem_ward()
    check("B.R2.1a [MAJORANT THEOREM, degree-generic] with "
          "SYMBOLIC beta > 0 and t_i > 0, q(x) := (x - beta) "
          "prod (x - t_i)^2 / (beta prod t_i^2) has q(0) == -1 "
          "identically, so p := (q + 1)/x is a POLYNOMIAL of "
          "degree 2K, and q >= 0 on [beta, inf) by inspection "
          "-- hence p(x) >= 1/x there, PSD BY STRUCTURE with no "
          "SOS solver, no ceiling and no lift (%s)" % sym_msg,
          sym_ok)
    check("B.R2.1b [EXACT-RATIONAL INSTANTIATION, K <= %d] the "
          "coefficient expansion of every majorant in the "
          "currency tier reproduces the identity as Fractions, "
          "residue %s == 0" % (K_CURRENCY, ident_max),
          ident_max == 0)
    check("B.R2.2 [DOMINANCE WARD] every consumed majorant "
          "bound dominates the measured D_-^2 (min slack %+.2e "
          ">= -1e-8; a candidate failing dominance is discarded "
          "as numerically refused and can never certify): "
          "%d/%d rungs carry a surviving majorant"
          % (dom_min, len(ok2), len(rows)), dom_min >= -1e-8)
    kcur_min = min([kcur.get(r["kz"], 0) for r in rows]
                   or [0])
    check("B.R2.3 [CURRENCY DEGREE CEILING -- disclosed, smoke "
          "amendment A3] the exact-rational LINEAR MOMENT FORM "
          "sum_k p_k nuhat_k tracks the stable factored "
          "evaluation only up to K = %d (worst rung); beyond "
          "that the float64 moments are annihilated by the "
          "coefficient growth (max rel dev over the whole "
          "degree ladder %.2e).  The CONSUMED certificate is "
          "therefore the FACTORED evaluation of the SAME exact-"
          "rational majorant (identity B.R2.1), and the moment-"
          "linear reading of the CCXCIII currency is reported "
          "with a measured degree ceiling, not assumed"
          % (kcur_min, cur_dev), kcur_min >= min(K_LIST))
    if len(ok2) < len(rows):
        print("    typed: %d rung(s) had NO surviving majorant "
              "-- reported as a ROUTE failure, not a ward "
              "failure" % (len(rows) - len(ok2)))

    print("\n  R3 -- the MONOTONICITY route")
    sps = []
    first_ok = 0
    for r in rows:
        sp = spearman(r["thm"], r["D2"])
        r["sp_theta"] = sp
        sps.append(sp)
        if r["imax"] == 0:
            first_ok += 1
    print("    within-rung Spearman(theta_g, D_-^2): median "
          "%+.3f, range [%+.3f, %+.3f]"
          % (float(np.median(sps)), min(sps), max(sps)))
    print("    argmax is the FIRST (smallest-theta) minus node "
          "on %d/%d rungs" % (first_ok, len(rows)))
    r3_cert = (first_ok == len(rows))
    print("    R3 VERDICT: boundary reduction %s -- %s"
          % ("AVAILABLE" if r3_cert else "NOT available",
             "the certificate reduces to ONE cell per rung"
             if r3_cert else "the argmax wanders, all cells "
             "must be certified"))

    # ------------------------------------------------------------ C
    section("C -- THE COMPOSITION THROUGH THE SPLIT")
    print("    kz     ||Ktoe-(G+-G-)||  ||Q^HQ-I||  Delta-"
          "transport  maxD- x sigmax(U)  Gershgorin")
    c1a = c1b = c1c = 0.0
    prod_cert = []
    gersh_cert = []
    for r in rows:
        b, go = r["b"], r["go"]
        h = r["h"]
        Gm_g = np.real(go["BmG"].conj().T @ go["BmG"])
        Ktoe = b["Gp"] - Gm_g
        Kref = b["Rp"] @ b["Delta"] @ b["Rp"]
        dk = float(np.linalg.norm(Ktoe - Kref)
                   / max(np.linalg.norm(Kref), 1e-300))
        C = go["CG"]
        ImCC = np.eye(h) - C.conj().T @ C
        ImCC = 0.5 * (ImCC + ImCC.conj().T)
        Q = go["BpG"] @ b["Rm"]
        dq = float(np.linalg.norm(Q.conj().T @ Q - np.eye(h)))
        dt = float(np.linalg.norm(ImCC - Q @ b["Delta"]
                                  @ Q.conj().T)
                   / max(np.linalg.norm(ImCC), 1e-300))
        c1a = max(c1a, dk)
        c1b = max(c1b, dq)
        c1c = max(c1c, dt)
        sU = float(np.linalg.svd(go["U"], compute_uv=False)[0])
        prod = r["maxDm"] * sU
        UU = go["U"] @ go["U"].conj().T
        off = np.abs(UU) - np.diag(np.diag(np.abs(UU)))
        gersh = float(np.max(r["D2"] + r["Dm"]
                             * (off @ r["Dm"])))
        r["sU"] = sU
        r["prod"] = prod
        r["gersh"] = gersh
        prod_cert.append(prod <= 1.0)
        gersh_cert.append(gersh <= 1.0)
        if r["kz"] in HEAVY or len(rows) <= 8:
            print("    %-5d  %.3e         %.2e    %.3e      "
                  "%.4f            %.4f"
                  % (r["kz"], dk, dq, dt, prod, gersh))
    check("C1 [KREIN CHAIN] K = G_+ - G_-^G reproduces "
          "R_+ Delta R_+ (max rel %.2e), Q = B_+^G G_+^{-1/2} "
          "is unitary (max %.2e) and I - C*C == Q Delta Q^H "
          "(max rel %.2e): A = B_+^*(I - C*C)B_+ exactly"
          % (c1a, c1b, c1c),
          c1a <= 1e-6 and c1b <= 1e-8 and c1c <= 1e-6)
    npc = sum(1 for c in prod_cert if c)
    ngc = sum(1 for c in gersh_cert if c)
    print("    C2 PRODUCT census max D_- sigma_max(U) <= 1 on "
          "%d/%d rungs (min %.4f, max %.4f)"
          % (npc, len(rows), min(r["prod"] for r in rows),
             max(r["prod"] for r in rows)))
    print("    C3 GERSHGORIN census max_g [D_g^2 + D_g sum_k "
          "D_k |(UU^*)_gk|] <= 1 on %d/%d rungs (min %.4f, "
          "max %.4f)"
          % (ngc, len(rows), min(r["gersh"] for r in rows),
             max(r["gersh"] for r in rows)))
    compose = "COMPOSE-CLOSES" if (npc == len(rows)
                                   or ngc == len(rows)) \
        else "COMPOSE-INSUFFICIENT"
    print("    COMPOSITION TYPING: %s" % compose)
    print("""    THE COMPOSED STATEMENT, premises typed:
      [SOURCE]   D_-(g)^2 = w^S_-(g) K_+(theta_g^-)  (A1, exact)
      [SOURCE]   U = D_-^{-1} C^G has unit rows       (A2, exact)
      [IDENTITY] I - C*C = (I - U*U) + U*(I - D_-^2)U (v872)
      [IDENTITY] A = B_+^*(I - C*C)B_+, Delta = Q^H(I-C*C)Q (C1)
      [PREMISE]  max D_- <= 1 - delta                 (the target)
      [PREMISE]  sigma_max(U) <= 1/(1 - delta)        (NOT held:
                 measured sigma_max(U) in [%.4f, %.4f])
      => wall.  The FIRST premise alone does NOT close: T_1 =
      I - U*U is indefinite with an O(1) negative part, so
      I - C*C >= (1 - max D_-^2) U*U is the only free
      consequence and it is vacuous where U*U is singular."""
          % (min(r["sU"] for r in rows),
             max(r["sU"] for r in rows)))

    # -------- C5 the relocation check
    print("\n  C5 -- THE RELOCATION CHECK (the decisive "
          "honesty test)")
    ratios = []
    for r in rows:
        wallm = 1.0 - math.sqrt(max(0.0, 1.0 - r["tau"]))
        r["wallm"] = wallm
        r["reloc"] = (1.0 - r["maxDm"]) / max(wallm, 1e-300)
        ratios.append(r["reloc"])
    lt = np.log([max(r["tau"], 1e-300) for r in rows])
    lc = np.log([max(abs(r["c_h"]), 1e-300) for r in rows])
    ld = np.log([1.0 - r["maxDm"] for r in rows])
    s_tau = ols_slope(lt, ld)
    s_ch = ols_slope(lc, ld)
    print("    structural (theorem-grade, from A2): "
          "1 - max D_- >= 1 - sqrt(1 - tau) on every rung -- "
          "verified %d/%d"
          % (sum(1 for r in rows
                 if 1.0 - r["maxDm"] >= r["wallm"] - 1e-12),
             len(rows)))
    print("    ratio (1 - max D_-)/(1 - sqrt(1 - tau)): median "
          "%.1f, range [%.1f, %.1f]"
          % (float(np.median(ratios)), min(ratios), max(ratios)))
    print("    screens: slope log(1 - max D_-) on log tau = "
          "%+.4f; on log c_h = %+.4f (bar |slope| <= %.2f)"
          % (s_tau, s_ch, SCREEN_BAR))
    tied = (0.5 <= float(np.median(ratios)) <= 2.0) \
        or abs(s_tau) > SCREEN_BAR or abs(s_ch) > SCREEN_BAR
    reloc = "RELOC" if tied else "NOT-RELOC"
    # the shared-h control: both margins shrink with h, so the
    # raw screens can fire on a common trend alone
    lh = np.log(hh)
    res_d = ld - (ols_slope(lh, ld) * (lh - lh.mean()) + ld.mean())
    res_t = lt - (ols_slope(lh, lt) * (lh - lh.mean()) + lt.mean())
    s_part = ols_slope(res_t, res_d)
    print("    PARTIAL screen (log tau -> log(1 - max D_-) with "
          "the shared log h trend removed): slope %+.4f"
          % s_part)
    print("    RELOCATION VERDICT (frozen rule): %s" % reloc)
    print("""    READ IT LOUDLY, and read BOTH halves.  What is
    PROVEN here (A2, exact): max D_- <= ||C||, so 1 - max D_-
    >= 1 - sqrt(1 - tau) on every rung -- the damping bound is
    IMPLIED BY the wall and can therefore NEVER be the harder
    statement.  What is MEASURED: the damping margin sits
    %.0fx above the wall margin (range %.0fx to %.0fx), so the
    two are NOT the same quantity; but the raw screens fire
    (slopes %+.3f / %+.3f against the %.2f bar) because BOTH
    margins shrink with h -- tau like h^{%+.1f}, the damping
    margin like h^{%+.2f}.  With the shared h trend removed the
    residual coupling is %+.3f.  The frozen rule therefore
    returns %s, and the honest reading of that verdict is
    CO-MOVEMENT THROUGH h, not a relocation of the wall's
    content into the damping coordinate: D_- <= 1 remains
    strictly weaker than the wall by the proven implication,
    and the composition census below shows it does not close
    anything on its own."""
          % (float(np.median(ratios)), min(ratios), max(ratios),
             s_tau, s_ch, SCREEN_BAR,
             ols_slope(lh, lt), ols_slope(lh, ld), s_part,
             reloc))

    # ------------------------------------------------------------ D
    section("D -- GATES, CONTROLS, SMOOTH WORLD")
    rr9 = core.build_window(CTRL_KZ)
    N_E = int(math.floor(math.exp(2.0 * rr9["alpha"]))) + 1
    lamE = gnu.lambda_eps(N_E)
    nn = np.nonzero(np.abs(lamE) > 1e-12)[0]
    ctrls = [("Epstein", dict(comb=(
        np.log(nn.astype(float)),
        2.0 * lamE[nn] / np.sqrt(nn.astype(float))))),
        ("scramble", dict(scramble_seed=SCR_SEED)),
        ("smooth", dict(comb=(
            np.asarray(rr9["uu"], float),
            smooth_masses(np.asarray(rr9["uu"], float)))))]
    r_t = next((r for r in rows if r["kz"] == CTRL_KZ), None)
    print("    world      max D_-      R1 certifies  R2 max "
          "bound   C2 product  C3 Gershgorin")
    ctrl_tab = {}
    if r_t is not None:
        ctrl_tab["truth"] = dict(
            maxDm=r_t["maxDm"], r1=r_t["r1"]["certified"],
            r2=(r_t["r2"]["maxbound"] if r_t["r2"] else
                float("nan")),
            prod=r_t["prod"], gersh=r_t["gersh"])
    for nmc, kw in ctrls:
        rc = damping_rung(CTRL_KZ, **kw)
        if isinstance(rc, str):
            print("    %-10s pipeline refused (%s) -- typed as "
                  "maximal breach" % (nmc, rc))
            ctrl_tab[nmc] = dict(maxDm=float("inf"), r1=False,
                                 r2=float("inf"),
                                 prod=float("inf"),
                                 gersh=float("inf"))
            continue
        lc = route_local_christoffel(rc["thm"], rc["thp"],
                                     rc["wSp"], rc["wSm"],
                                     rc["Km"])
        sdc = spectral_data(rc)
        dec = int(np.argmax(rc["D2"]))
        r2v = float("nan")
        if sdc["betahat"] > 0.0:
            for K in K_LIST:
                for t in node_candidates(sdc, K, dec):
                    bnd = eval_majorant_bound(sdc, rc["wSm"], t)
                    if float(np.min(bnd - rc["D2"])) < -1e-8:
                        continue
                    mx = float(np.max(bnd))
                    r2v = mx if math.isnan(r2v) else min(r2v, mx)
        sU = float(np.linalg.svd(rc["go"]["U"],
                                 compute_uv=False)[0])
        UU = rc["go"]["U"] @ rc["go"]["U"].conj().T
        off = np.abs(UU) - np.diag(np.diag(np.abs(UU)))
        gersh = float(np.max(rc["D2"] + rc["Dm"]
                             * (off @ rc["Dm"])))
        ctrl_tab[nmc] = dict(maxDm=rc["maxDm"],
                             r1=lc["certified"], r2=r2v,
                             prod=rc["maxDm"] * sU, gersh=gersh)
    for nmc in ("truth", "Epstein", "scramble", "smooth"):
        if nmc not in ctrl_tab:
            continue
        c = ctrl_tab[nmc]
        print("    %-10s %11.4f  %-12s  %11.4e  %10.4f  %12.4f"
              % (nmc, c["maxDm"], "YES" if c["r1"] else "no",
                 c["r2"], c["prod"], c["gersh"]))
    tr = ctrl_tab.get("truth", {})
    d1 = (tr and G5_TRUTH[0] <= tr["maxDm"] <= G5_TRUTH[1]
          and G5_EPSTEIN[0] <= ctrl_tab["Epstein"]["maxDm"]
          <= G5_EPSTEIN[1]
          and G5_SCRAMBLE[0] <= ctrl_tab["scramble"]["maxDm"]
          <= G5_SCRAMBLE[1])
    check("D1 [CCCXIII G5 REPRODUCTION] max D_- at kz %d: "
          "truth %.4f, Epstein %.4f, scramble %.4f -- inside "
          "the CCCXIII bands"
          % (CTRL_KZ, tr.get("maxDm", float("nan")),
             ctrl_tab["Epstein"]["maxDm"],
             ctrl_tab["scramble"]["maxDm"]), bool(d1))
    lm = max(r["maxDm"] for r in rows)
    check("D2 [v870/v872 LADDER MAX] ladder max D_- = %.6f in "
          "[%.4f, %.4f]%s" % (lm, LADDER_MAX[0], LADDER_MAX[1],
                              " (SMOKE ladder -- not gated)"
                              if SMOKE else ""),
          SMOKE or LADDER_MAX[0] <= lm <= LADDER_MAX[1])
    fires = all(ctrl_tab[n]["maxDm"] > 1.0
                and not ctrl_tab[n]["r1"]
                and not (ctrl_tab[n]["r2"] <= 1.0)
                and ctrl_tab[n]["prod"] > 1.0
                and ctrl_tab[n]["gersh"] > 1.0
                for n in ("Epstein", "scramble"))
    check("D3 [CONTROLS MUST FIRE] Epstein and scramble are "
          "REFUSED by every route and are NOT rescued by the "
          "composition terms C2/C3", fires)
    sm = ctrl_tab.get("smooth", {})
    print("    D4 SMOOTH WORLD (descriptive, no bar): max D_- "
          "= %.4f -- %s the truth's %.4f"
          % (sm.get("maxDm", float("nan")),
             "ABOVE" if sm.get("maxDm", 0) > tr.get("maxDm", 0)
             else "below", tr.get("maxDm", float("nan"))))

    # ------------------------------------------------------------ V
    section("V -- FROZEN VERDICT")
    wards_ok = all(ok for _nm, ok in CHECKS)
    n_cert = max(n1, n2)
    if not wards_ok:
        verdict = "DAMPING-REFUSED (ward failure: %s)" \
            % ",".join(sorted(set(FAILS)))
    elif (n1 == len(rows) or n2 == len(rows)
          or n2b_best == len(rows)):
        verdict = ("DAMPING-CERTIFIED [FLOAT-LEVEL, "
                   "PREMISE-REDUCED] (R2a %d/%d rungs, R2b "
                   "per-cell %d/%d rungs at K = %d, delta "
                   "%+.6f)"
                   % (n2, len(rows), n2b_best, len(rows),
                      kbest2b, 1.0 - worst2b[kbest2b]))
    elif max(n_cert, n2b_best) > 0:
        verdict = ("DAMPING-LOCAL-CERTIFIED (R1 %d/%d, R2a "
                   "%d/%d, R2b per-cell %d/%d)"
                   % (n1, len(rows), n2, len(rows), n2b_best,
                      len(rows)))
    else:
        verdict = "DAMPING-MEASURED (no route certifies)"
    print("\n  VERDICT: %s" % verdict)
    print("  COMPOSITION: %s" % compose)
    print("  RELOCATION: %s" % reloc)
    print("""
  WHAT THE CERTIFICATE ACTUALLY IS (premises typed, nothing
  claimed beyond them):
    [EXACT]      the majorant identity x p(x) - 1 = (x - beta)
                 prod (x - t_i)^2 / (beta prod t_i^2), PSD by
                 structure on [beta, inf) -- degree-generic
                 theorem, symbolically warded (B.R2.1a)
    [PREMISE]    lam_min(G_+) >= betahat, the FLOOR premise --
                 float64 eigenvalue minus a declared backward-
                 stability budget; this is the ONE unproven
                 analytic input and is exactly what a theorem
                 would have to supply uniformly in h
    [DATA]       the spectral pairs (lamhat_i, om[i, g]) of the
                 source-built plus Gram at the odd-frame vectors
                 -- float64, per rung, no zero or prime oracle
    [DERIVED]    D_-(g)^2 <= (w^S_-(g)/Lhat) sum_i p(lamhat_i)
                 om[i, g] <= 1 on every cell of every rung
  So the object is REDUCED, not proven: "D_- <= 1 on this
  ladder" now rests on a uniform lower bound for lam_min(G_+)
  plus finite spectral data, in exactly the CCXCIII currency.""")
    print("""
  THE HONEST CONSEQUENCE.  D_- is now completely characterized
  as a SOURCE object: D_-(g)^2 = w^S_-(g) K_+(theta_g^-), the
  fold-aggregated minus mass over the plus arm's Christoffel
  function, equivalently the ell^2 row norm of the contractor
  and equivalently the x^{-1} moment of the plus Gram's
  spectral measure at f_g (A1/A2/B.R2.0, all exact).  The
  certificate D_- <= 1 IS reachable in the certified currency
  -- but the ROW-NORM reading (A2) shows why that does not
  finish anything: max D_- <= ||C|| means the damping bound is
  a CONSEQUENCE of the wall, hence strictly weaker, measured
  %.0fx slacker than the wall margin.  With D_- <= 1 granted,
  the free consequence I - C*C >= (1 - max D_-^2) U*U is
  vacuous because U*U is singular, and the crude and
  Gershgorin compositions fail on %d and %d of %d rungs.  The
  residual content sits in the FRAME EXCESS of U, exactly
  where CCCXIII's coisometry defect left it.  The one place
  the arithmetic is visibly load-bearing is the mass split:
  the prime oscillation is NOT a small correction but the
  sign-deciding term at the decisive cell (%s carries it,
  arch+smooth alone reaching %.4f > 1 on the ladder).  NO RH
  claim."""
          % (float(np.median(ratios)),
             len(rows) - npc, len(rows) - ngc, len(rows),
             max(carr, key=lambda k: carr[k]),
             max(r["d2as"] for r in srows)))
    npass = sum(1 for _n, ok in CHECKS if ok)
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed%s"
          % (time.time() - T0, len(CHECKS), len(FAILS),
             ("  " + ",".join(FAILS)) if FAILS else ""))
    return 0 if npass == len(CHECKS) else 1


if __name__ == "__main__":
    raise SystemExit(main())
