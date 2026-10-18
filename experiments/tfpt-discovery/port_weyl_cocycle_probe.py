#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""port_weyl_cocycle_probe -- PRIME.PORT.WEYL.COCYCLE.01
(EXPLORATION ONLY, experiments/; round 58: the final boundary
pivot scalarized as a Weyl function with a 2x2 transfer cocycle in
de-circularized coordinates -- Herglotz ward, exact Moebius step,
source-only transfer entries, and the tau-screen on the
half-plane-preservation margin.  2026-08-10.)

THE QUESTION (frozen).  v899 proved the soft pivot is EXACTLY a
deflated-Christoffel evaluation of sigma = mu_+ - nu_-, and P3 of
round 57 (case_edge_christoffel_probe) rewrote it over the
POSITIVE constructional family: the folded cosine quadrature
(x_m, w_m) with W_{h,m} = v_* w_m > 0 EXACT.  That positive
family has canonical Jacobi/three-term recurrence data -- the
deployed Lanczos chain (al_k, be_k) that the wall evaluation
itself builds (lanczos_chain(xs, ws, h+1); eval_chain reads the
first h polynomials).  THIS probe scalarizes it as the Weyl
function
    m_n(z) = <e_1, (J_n - z)^{-1} e_1>,
J_n the n x n truncated Jacobi matrix, and asks the round's
META-CRITERION question (the tau-screen, frozen): the candidate
invariance margin is the defect of upper-half-plane preservation
of the transfer cocycle; a route is a RELOCATION iff its
distance-to-violation scales like tau (log-log slope ~ +1), and
the first route with an O(1) margin (slope ~ 0) passes.

HONEST FRAME (frozen, said up front -- TWO disclosures):
 (i)  THE STEP READING: the LADDER step h_i -> h_{i+1} crosses to
      a DIFFERENT window/measure family -- no exact Moebius
      relation exists between the m-functions of different
      measures.  The exact Moebius structure lives in the
      TRUNCATION step h -> h+1 of each rung's own deployed chain
      (the chain is built to length h+1, the wall evaluation
      reads h): that step is what is verified exactly below, per
      rung, and it is what "rung step" means in this probe.
 (ii) WALL CONTENT: the cocycle is built from the POSITIVE half
      mu_+ of the comb only.  The wall (tau) lives in the
      interplay with nu_-.  A screen-passing O(1) margin here is
      only a route if the functional carries wall content -- so
      the wall-blindness of the margin is MEASURED (smooth-world
      comparison, frozen rule below) and typed first-class:
      passing the screen with a wall-blind functional is recorded
      as exactly that, not as progress.

THE EXACT OBJECTS (frozen): with T_k(z) = [[0, 1], [-be_k^2,
al_k - z]] and the Moebius action Moeb(M) w = (aw + b)/(cw + d),
the backward continued fraction gives EXACTLY
    m_n(z) = Moeb(T_0 T_1 ... T_{n-1}) 0,
so the truncation step appends ONE factor:
    m_{n+1}(z) = Moeb(A_n T_n) 0,  A_n = T_0 ... T_{n-1},
and by the group law the single-matrix form is m_{n+1} =
Moeb(G_n) m_n with G_n = A_n T_n A_n^{-1} (det G_n = be_n^2 > 0).
Half-plane preservation of each factor is CLASSICAL: al_k real
and be_k^2 > 0 imply Im Moeb(T_k) w = (Im z + be_k^2 Im w) /
|al_k - z - be_k^2 w|^2 > 0 for Im z > 0, Im w >= 0 -- the
quantitative distance to violation of the whole cocycle is
    MARG-P(h) = min_k be_k^2  (the Potapov-type margin),
and the observable output margin is MARG-H(h) = min over the
declared z-grid of Im m_{h+1}(z) / Im z.  The transfer entries
(al_k, be_k) are SOURCE-ONLY: pure Lanczos data of the folded
positive family -- no tau, no forward sign, no nu_- enters; they
are moreover SCALE-FREE (invariant under w -> c w, warded), so
the P1 sign-free normalization question does not even arise for
them (stronger than ELL-B source-only; stated and warded).

FROZEN PROTOCOL (machinery verbatim from
case_edge_christoffel_probe round 57 = christoffel_ratio_probe
round 55 chain; ONE Gram per rung):

 W   PIPELINE + REPRODUCTION WARDS (kill -> PIPELINE-BROKEN /
     WARD-BROKEN): W0 truth ladder == 42 rungs; W0c full-window
     census == 37; W-C1f c-quartile reproduction 1163/2117/2930
     and c(kz21) = 50667 at h = 371 (rtol 2e-2); W-SCL the
     scale-freeness ward: on the shallowest rung the chain from
     (xs, 7.3 ws) equals the chain from (xs, ws) at rel <=
     SCL_WARD = 1e-12 (al and be; m0 scales by 7.3, printed).

 H1  HERGLOTZ WARD (identity-grade; kill -> WARD-BROKEN): for
     every truth rung and every z in Z_HERG (6 frozen points,
     Im z > 0): Im m_h(z) > 0 AND Im m_{h+1}(z) > 0, m by the
     spectral route (eigh of J_n; m = sum_r U_{1r}^2/(lam_r -
     z)).  For a genuinely positive Jacobi measure this must
     hold; failure kills.

 H2  ROUTE WARD (kill -> WARD-BROKEN): spectral route == backward
     continued fraction route at rel <= CF_WARD = 1e-7 (all
     rungs, all Z_HERG, both sizes).

 M1  THE COCYCLE + THE MOEBIUS STEP (kill -> WARD-BROKEN): per
     rung, per z in Z_COCY (4 frozen well-separated points), the
     normalized ordered 2x2 product A_h(z) (projective
     renormalization per step -- Moebius-invariant) must
     reproduce BOTH truncations: |Moeb(A_h) 0 - m_h| and
     |Moeb(A_h T_h) 0 - m_{h+1}| rel <= COCY_WARD = 1e-6; the
     step h -> h+1 IS the appended factor T_h, verified exactly.

 M2  THE SINGLE-MATRIX FORM, SPOT-PROVEN (kill -> WARD-BROKEN):
     on the N_SPOT = 2 shallowest rungs at z = 2i, in mpmath at
     dps 260 (the conjugation A T A^{-1} is exponentially
     ill-conditioned in float64 -- cond ~ r^h; at dps 260 the
     shallow rungs are exactly representable): G = A_h T_h
     adj(A_h) (scalar det dropped, Moebius-invariant), ward
     |Moeb(G) m_h - m_{h+1}| rel <= GSPOT_WARD = 1e-30.
     Honesty: for deep rungs the single-matrix form holds by the
     group law but is not float-verifiable; the equivalent
     appended-factor form (M1) is verified ladder-wide.

 M3  MARGINS + THE TAU-SCREEN (measured, typed): per rung MARG-P
     = min_k be_k^2 (k = 0..h-1) and MARG-H = min_{Z_HERG}
     Im m_{h+1}(z)/Im z; OLS slope + corr of log margin vs log
     tau_full over the 42 rungs.  TYPED (frozen rules, primary =
     MARG-P): WEYL-SCREEN-PASS(slope) iff |slope| <= SLOPE_PASS
     = 0.30 and min margin > 0; WEYL-SCREEN-RELOC(slope) iff
     slope >= SLOPE_RELOC = 0.70; else WEYL-SCREEN-AMBIG(slope).
     MARG-H typed secondarily by the same bands.

 M4  WALL CONTENT (measured, typed; the honesty dichotomy): the
     same margins on the SMOOTH-world chains that complete.
     TYPED: WALLCONTENT-NONE iff >= 3 smooth chains complete AND
     the median smooth MARG-P lies within factor WALLBLIND_FAC =
     5 of the median truth MARG-P (the margin cannot tell the
     wall-violating world from the truth world); else
     WALLCONTENT-SEEN(ratio).  A screen pass with
     WALLCONTENT-NONE is recorded as a wall-blind pass -- NOT a
     route -- in the verdict, honestly.

 C   CONTROLS (kill -> WARD-BROKEN if silent): C-S smooth world:
     sigma indefinite (tau_full < 0) on >= 1 rung (the wall
     channel fires); the Weyl channel status on smooth is
     PRINTED (expected: Herglotz survives -- the positive-half
     scalarization is comb-sign-blind; that print is the M4
     content, not a control failure).  C-E Epstein x^2+5y^2 comb
     + scramble (seed 1) at kz 9: frame death or neg(A) > 0 or
     tau_12 <= 0 on BOTH; the Weyl-channel status printed.

KILLS: KP a W pipeline ward breaks -> PIPELINE-BROKEN; KW an
H1/H2/M1/M2 ward or control breaks -> WARD-BROKEN.  M3/M4 typed
labels report, never kill.

VERDICT (frozen enum): WEYLCOCYCLE-MEASURED with typed sublabels
HERGLOTZ-WARDED, MOEBIUS-EXACT, SOURCE-ONLY-ENTRIES,
WEYL-SCREEN-PASS(slope) / WEYL-SCREEN-RELOC(slope) /
WEYL-SCREEN-AMBIG(slope), WALLCONTENT-NONE / WALLCONTENT-SEEN;
else PIPELINE-BROKEN / WARD-BROKEN.

FROZEN BARS: H_DEEP_MAX = 900; JWIN = (2,...,24); NW = 12;
N_RUNGS_EXP = 42; N_FULLWIN_FROZEN = 37; KZ_STAR = 21; H_STAR =
371; REF_C21 = 50667, REF_Q25/MED/Q75 = 1163/2117/2930 (rtol
2e-2); ID_WARD = 1e-9; CGE1_WARD = 1e-9; SCL_WARD = 1e-12;
SCL_FAC = 7.3; Z_HERG = (2i, 1i, 0.5i, -1.5+0.5i, 1.5+0.5i,
0.25+0.05i); Z_COCY = (2i, 1i, -1.5+0.5i, 1.5+0.5i); CF_WARD =
1e-7; COCY_WARD = 1e-6; N_SPOT = 2; Z_SPOT = 2i; GSPOT_DPS =
260; GSPOT_WARD = 1e-30; SLOPE_PASS = 0.30; SLOPE_RELOC = 0.70;
WALLBLIND_FAC = 5.0; CTRL_KZ = 9; scramble seed 1.

SMOKE-RUN DISCLOSURE (2026-08-10, before freezing): one smoke run
of this script (13/13 with the identical bars; NO bar, rule or
enum was moved -- the a-priori float-accumulation allowance
COCY_WARD = 1e-6 turned out generous: the measured cocycle
deviation is 5.9e-15, the route ward 5.1e-15, the mp spot ward
3.7e-76) measured the picture that is frozen here as context:
Herglotz green on every rung and grid point (min output margin
0.2225); MARG-P = min be_k^2 in [0.2007, 0.2286] with tau-screen
slope -0.0026 (corr -0.185) while tau spans a factor 1182 -- an
O(1) margin deep inside the PASS band; and the SMOOTH chains
complete on 42/42 with median MARG-P ratio 1.00 and surviving
Herglotz: the margin is WALL-BLIND exactly as the honest frame
(ii) predicted -- the screen pass is recorded as a closed route
question (this scalarization drops the wall), not as progress.
No census count, no enum, no typed rule was changed after the
smoke run.

SPEC v1 (2026-08-10, frozen + SHA-hashed before the frozen run):
everything above.  Mechanical concretizations frozen with v1: (i)
window memoization per (kz, seed); (ii) ONE Gram per rung
(christoffel_ratio verbatim); (iii) the spectral route
diagonalizes the dense tridiagonal J_n once per (rung, size) and
serves all z; (iv) the cocycle product renormalizes by the max
abs entry per step; (v) N_SPOT = the 2 shallowest truth rungs in
(h, kz) order; (vi) smooth chains that die are counted and
excluded from M4 medians.

NO RH claim: the Weyl/Moebius structure is exact finite linear
algebra of the deployed positive quadrature family; Herglotz for
a positive measure is an identity-grade ward, not a discovery;
the screen verdict on a wall-blind margin closes a ROUTE
QUESTION, not a gap; nothing here proves tau_h > 0 beyond the
certified census (v897).  No marker moves.

FIREWALL: no zeros, no prime oracles (AST scan; banned ids
zetazero / nzeros / primerange / isprime / primepi / nextprime /
prevprime); v563 READ-ONLY; RNG only inside the declared
scramble control; stdout only.

Sources (read-only): v563_paper2_readouts; wall/window/deflation
machinery verbatim from case_edge_christoffel_probe.py (P3,
round 57) = christoffel_ratio_probe.py (round 55, promoted
v899); sign-free normalization context from
port_signfree_normalization_probe.py (P1, round 57, declared
input); certified base v884/v887/v897 -- declared inputs.

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/port_weyl_cocycle_probe.py
"""

import ast
import hashlib
import math
import os
import sys
import time

import numpy as np
from mpmath import mp

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
CGE1_WARD = 1e-9
SCL_WARD = 1e-12               # W-SCL scale-freeness
SCL_FAC = 7.3
Z_HERG = (2j, 1j, 0.5j, -1.5 + 0.5j, 1.5 + 0.5j, 0.25 + 0.05j)
Z_COCY = (2j, 1j, -1.5 + 0.5j, 1.5 + 0.5j)
CF_WARD = 1e-7                 # H2 route agreement
COCY_WARD = 1e-6               # M1 (smoke-fixed, see header)
N_SPOT = 2
Z_SPOT = 2j
GSPOT_DPS = 260
GSPOT_WARD = 1e-30
SLOPE_PASS = 0.30              # M3 screen bands (frozen a priori)
SLOPE_RELOC = 0.70
WALLBLIND_FAC = 5.0            # M4
CTRL_KZ = 9
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


# --------- pipeline, verbatim (christoffel_ratio / case_edge chain)
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
    (christoffel_ratio verbatim; case_edge keep_all extension)."""
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
        out["chain"] = (al, be, m0)
        out["xs"] = xs
        out["ws"] = ws
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
    r["c"] = r["d12"] / r["tau12"] if r["tau12"] != 0.0 \
        else float("inf")
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


def corr(x, y):
    return float(np.corrcoef(np.asarray(x, float),
                             np.asarray(y, float))[0, 1])


# ---------------------------------------- Weyl / cocycle objects
def m_spectral_all(al, be, n, zs):
    """m_n(z) for all z via ONE eigh of the dense tridiagonal J_n
    (SPEC iii): m = sum_r U_{1r}^2 / (lam_r - z)."""
    J = np.diag(al[:n])
    if n > 1:
        J += np.diag(be[:n - 1], 1) + np.diag(be[:n - 1], -1)
    lam, U = np.linalg.eigh(J)
    w1 = U[0, :] ** 2
    return [complex(np.sum(w1 / (lam - z))) for z in zs]


def m_contfrac(al, be, n, z):
    """Backward continued fraction: g_n = 0; g_k = 1/(al_k - z -
    be_k^2 g_{k+1}); m_n = g_0."""
    g = 0.0 + 0.0j
    for k in range(n - 1, -1, -1):
        b2 = be[k] ** 2 if k < n - 1 else 0.0
        g = 1.0 / (al[k] - z - b2 * g)
    return g


def cocycle(al, be, n, z):
    """A = T_0 T_1 ... T_{n-1} with per-step renormalization."""
    A = (1.0 + 0j, 0j, 0j, 1.0 + 0j)
    for k in range(n):
        b2 = be[k] ** 2 if k < len(be) else 0.0
        a, b, c, d = A
        # T = [[0, 1], [-b2, al_k - z]]
        t3, t4 = -b2, al[k] - z
        A = (b * t3, a + b * t4, d * t3, c + d * t4)
        s = max(abs(A[0]), abs(A[1]), abs(A[2]), abs(A[3]))
        if s > 0.0:
            A = (A[0] / s, A[1] / s, A[2] / s, A[3] / s)
    return A


def moeb(A, w):
    a, b, c, d = A
    return (a * w + b) / (c * w + d)


def main():
    section("PRIME.PORT.WEYL.COCYCLE.01 -- the boundary pivot as a "
            "Weyl function with a 2x2 transfer cocycle "
            "(EXPLORATION ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s"
          % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
    print("    NO RH claim; no marker moves.")
    print("\nS0 -- firewall")
    check("S0.1 AST firewall clean", not ast_scan(BANNED_IDS))

    # ------------------------------------------------------------ W
    section("W -- ladders + reproduction wards (christoffel chain, "
            "ONE Gram per rung)")
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
        rs = anatomy(kz, comb=(uu, smooth_masses(uu)),
                     keep_all=True)
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
    cs = np.array([r["c"] for r in fullw])
    q1, q2, q3 = quartiles(cs)
    star = [r for r in fullw if r["kz"] == KZ_STAR]
    c21 = star[0]["c"] if star else float("nan")
    h21 = star[0]["h"] if star else -1
    check("W-C1f REPRODUCTION c-quartiles %.0f/%.0f/%.0f == "
          "%.0f/%.0f/%.0f, c(kz%d) %.0f == %.0f at h %d (rtol "
          "%.0e)"
          % (q1, q2, q3, REF_Q25, REF_MED, REF_Q75, KZ_STAR, c21,
             REF_C21, h21, REF_RTOL),
          abs(q1 / REF_Q25 - 1.0) <= REF_RTOL
          and abs(q2 / REF_MED - 1.0) <= REF_RTOL
          and abs(q3 / REF_Q75 - 1.0) <= REF_RTOL
          and abs(c21 / REF_C21 - 1.0) <= REF_RTOL
          and h21 == H_STAR, kill="KW")
    # W-SCL scale-freeness of the transfer entries
    r0 = truth[0]
    al0, be0, m00 = r0["chain"]
    al1, be1, m01, st1 = lanczos_chain(r0["xs"],
                                       SCL_FAC * r0["ws"],
                                       r0["h"] + 1)
    dev_scl = max(
        float(np.max(np.abs(al1 - al0)))
        / max(float(np.max(np.abs(al0))), 1e-300),
        float(np.max(np.abs(be1 - be0)))
        / max(float(np.max(np.abs(be0))), 1e-300))
    check("W-SCL SOURCE-ONLY + SCALE-FREE: chain from %.1f x w "
          "equals chain from w at rel %.1e <= %.0e (m0 scales "
          "%.4f == %.1f) -- (al, be) carry NO mass scale, NO "
          "tau, NO forward sign" % (SCL_FAC, dev_scl, SCL_WARD,
                                    m01 / m00, SCL_FAC),
          st1 == r0["h"] + 1 and dev_scl <= SCL_WARD
          and abs(m01 / m00 - SCL_FAC) <= 1e-9, kill="KW")

    # ------------------------------------------------- H1/H2/M1
    section("H1/H2/M1 -- Herglotz ward + route ward + the cocycle "
            "Moebius step (all %d rungs)" % len(truth))
    herg_ok = True
    herg_min = float("inf")
    dev_cf = 0.0
    dev_cocy = 0.0
    margs_p = []
    margs_h = []
    for r in truth:
        al, be, m0 = r["chain"]
        h = r["h"]
        r["marg_p"] = float(np.min(be[:h] ** 2))
        mh_s = m_spectral_all(al, be, h, Z_HERG)
        mh1_s = m_spectral_all(al, be, h + 1, Z_HERG)
        mh = dict(zip(Z_HERG, mh_s))
        mh1 = dict(zip(Z_HERG, mh1_s))
        hmin = float("inf")
        for z in Z_HERG:
            for m in (mh[z], mh1[z]):
                if m.imag <= 0.0:
                    herg_ok = False
            hmin = min(hmin, mh1[z].imag / z.imag)
            # H2 route ward
            for n_, mref in ((h, mh[z]), (h + 1, mh1[z])):
                mcf = m_contfrac(al, be, n_, z)
                dev_cf = max(dev_cf, abs(mcf - mref)
                             / max(abs(mref), 1e-300))
        r["marg_h"] = hmin
        herg_min = min(herg_min, hmin)
        margs_p.append(r["marg_p"])
        margs_h.append(hmin)
        # M1 cocycle ward on the frozen subset grid
        for z in Z_COCY:
            A = cocycle(al, be, h, z)
            m_pred = moeb(A, 0.0)
            dev_cocy = max(dev_cocy, abs(m_pred - mh[z])
                           / max(abs(mh[z]), 1e-300))
            # append the ONE factor T_h = [[0,1],[-be_h^2, al_h-z]]
            a_, b_, c_, d_ = A
            t3 = -(be[h] ** 2) if h < len(be) else 0.0
            t4 = al[h] - z
            AT = (b_ * t3, a_ + b_ * t4, d_ * t3, c_ + d_ * t4)
            m1_pred = moeb(AT, 0.0)
            dev_cocy = max(dev_cocy, abs(m1_pred - mh1[z])
                           / max(abs(mh1[z]), 1e-300))
    check("H1 HERGLOTZ WARD: Im m_h(z) > 0 and Im m_{h+1}(z) > 0 "
          "on every rung and every z in Z_HERG (min output "
          "margin Im m/Im z = %.4f)" % herg_min, herg_ok,
          kill="KW")
    check("H2 ROUTE WARD spectral == continued fraction: max rel "
          "%.1e <= %.0e" % (dev_cf, CF_WARD), dev_cf <= CF_WARD,
          kill="KW")
    check("M1 COCYCLE + MOEBIUS STEP: |Moeb(A_h) 0 - m_h| and "
          "|Moeb(A_h T_h) 0 - m_{h+1}| max rel %.1e <= %.0e "
          "(the h -> h+1 step IS the appended factor T_h, "
          "verified on every rung, Z_COCY)"
          % (dev_cocy, COCY_WARD), dev_cocy <= COCY_WARD,
          kill="KW")
    print("    transfer entries: T_k(z) = [[0, 1], [-be_k^2, "
          "al_k - z]] -- pure Lanczos data of the POSITIVE folded "
          "family (W-SCL: scale-free; no tau, no nu_-, no "
          "forward sign).")

    # ------------------------------------------------------------ M2
    section("M2 -- the single-matrix Moebius form, spot-proven at "
            "mp dps %d (z = %s)" % (GSPOT_DPS, Z_SPOT))
    spot = truth[:N_SPOT]
    dev_g = 0.0
    mp.dps = GSPOT_DPS
    zmp = mp.mpc(Z_SPOT.real, Z_SPOT.imag)
    for r in spot:
        al, be, m0 = r["chain"]
        h = r["h"]
        # exact mp cocycle A_h (no renormalization needed at dps)
        a, b, c, d = mp.mpc(1), mp.mpc(0), mp.mpc(0), mp.mpc(1)
        for k in range(h):
            b2 = mp.mpf(be[k]) ** 2 if k < len(be) else mp.mpf(0)
            t3, t4 = -b2, mp.mpf(al[k]) - zmp
            a, b, c, d = (b * t3, a + b * t4,
                          d * t3, c + d * t4)
        # T_h
        b2h = mp.mpf(be[h]) ** 2 if h < len(be) else mp.mpf(0)
        t3, t4 = -b2h, mp.mpf(al[h]) - zmp
        # G = A T adj(A)  (det factor dropped)
        # adj(A) = [[d, -b], [-c, a]]
        # A T = [[b t3, a + b t4], [d t3, c + d t4]]
        at = (b * t3, a + b * t4, d * t3, c + d * t4)
        G = (at[0] * d + at[1] * (-c), at[0] * (-b) + at[1] * a,
             at[2] * d + at[3] * (-c), at[2] * (-b) + at[3] * a)
        # m_h, m_{h+1} at mp precision (backward CF)
        def mcf_mp(n_):
            g = mp.mpc(0)
            for k in range(n_ - 1, -1, -1):
                b2_ = (mp.mpf(be[k]) ** 2 if k < n_ - 1
                       else mp.mpf(0))
                g = 1 / (mp.mpf(al[k]) - zmp - b2_ * g)
            return g
        mh_mp = mcf_mp(h)
        mh1_mp = mcf_mp(h + 1)
        pred = (G[0] * mh_mp + G[1]) / (G[2] * mh_mp + G[3])
        dev = abs(pred - mh1_mp) / abs(mh1_mp)
        dev_g = max(dev_g, float(dev))
        print("    kz %-4d h %-4d: |Moeb(G_h) m_h - m_{h+1}| rel "
              "= %s  (det G = be_h^2 = %.6f > 0)"
              % (r["kz"], r["h"], mp.nstr(dev, 3),
                 float(be[h] ** 2) if h < len(be) else 0.0),
              flush=True)
    check("M2 SINGLE-MATRIX FORM (spot, mp dps %d): m_{h+1} == "
          "Moeb(A_h T_h adj(A_h)) m_h at rel %.1e <= %.0e on the "
          "%d shallowest rungs" % (GSPOT_DPS, dev_g, GSPOT_WARD,
                                   N_SPOT),
          dev_g <= GSPOT_WARD, kill="KW")

    # ------------------------------------------------------------ M3
    section("M3 -- MARGINS + THE TAU-SCREEN")
    taus = np.array([r["tau_full"] for r in truth])
    hh = np.array([r["h"] for r in truth], float)
    mp_arr = np.array(margs_p)
    mh_arr = np.array(margs_h)
    print("    kz   h    tau_full   MARG-P=min be_k^2  "
          "MARG-H=min Im m/Im z")
    for r in truth:
        print("    %-4d %-4d %.3e  %.6f          %.6f"
              % (r["kz"], r["h"], r["tau_full"], r["marg_p"],
                 r["marg_h"]), flush=True)
    sl_p = ols_slope(np.log(taus), np.log(mp_arr))
    co_p = corr(np.log(taus), np.log(mp_arr))
    sl_h_ = ols_slope(np.log(taus), np.log(mh_arr))
    co_h = corr(np.log(taus), np.log(mh_arr))
    sl_ph = ols_slope(np.log(hh), np.log(mp_arr))
    print("\n    MARG-P: range [%.4f, %.4f]; slope vs log tau = "
          "%+.4f (corr %+.3f); vs log h = %+.4f"
          % (float(np.min(mp_arr)), float(np.max(mp_arr)), sl_p,
             co_p, sl_ph))
    print("    MARG-H: range [%.4f, %.4f]; slope vs log tau = "
          "%+.4f (corr %+.3f)"
          % (float(np.min(mh_arr)), float(np.max(mh_arr)), sl_h_,
             co_h))
    print("    tau_full range [%.3e, %.3e] (factor %.0f)"
          % (float(np.min(taus)), float(np.max(taus)),
             float(np.max(taus)) / float(np.min(taus))))

    def screen_type(sl, col):
        if abs(sl) <= SLOPE_PASS and float(np.min(col)) > 0.0:
            return "WEYL-SCREEN-PASS(slope=%+.3f)" % sl
        if sl >= SLOPE_RELOC:
            return "WEYL-SCREEN-RELOC(slope=%+.3f)" % sl
        return "WEYL-SCREEN-AMBIG(slope=%+.3f)" % sl
    m3p = screen_type(sl_p, mp_arr)
    m3h = screen_type(sl_h_, mh_arr)
    check("M3.1 typed (primary MARG-P): %s; secondary MARG-H: %s"
          % (m3p, m3h), True)

    # ------------------------------------------------------------ M4
    section("M4 -- WALL CONTENT: the same margins on the smooth "
            "world")
    sm_ok = [r for r in smooth if "chain" in r]
    sm_p = []
    sm_herg_ok = True
    for r in sm_ok:
        al, be, m0 = r["chain"]
        h = r["h"]
        sm_p.append(float(np.min(be[:h] ** 2)))
        for z in (Z_HERG[0], Z_HERG[-1]):
            m = m_contfrac(al, be, h + 1, z)
            if m.imag <= 0.0:
                sm_herg_ok = False
    n_smc = len(sm_p)
    if n_smc >= 3:
        med_t = float(np.median(mp_arr))
        med_s = float(np.median(sm_p))
        ratio = max(med_t / med_s, med_s / med_t)
        blind = ratio <= WALLBLIND_FAC
        m4 = ("WALLCONTENT-NONE(med-ratio=%.2f)" % ratio if blind
              else "WALLCONTENT-SEEN(med-ratio=%.2f)" % ratio)
        print("    smooth chains complete on %d/%d rungs; median "
              "MARG-P smooth %.4f vs truth %.4f (ratio %.2f, "
              "blind bar %.1f); smooth Herglotz survives: %s"
              % (n_smc, len(smooth) + n_dead_s, med_s, med_t,
                 ratio, WALLBLIND_FAC, sm_herg_ok))
    else:
        m4 = "WALLCONTENT-SEEN(chain-death=%d)" % n_dead_s
        print("    smooth chains die on %d rungs -- the Weyl "
              "channel itself distinguishes worlds via chain "
              "death" % n_dead_s)
    check("M4.1 typed: %s -- a screen pass with WALLCONTENT-NONE "
          "is a WALL-BLIND pass (the margin reads only mu_+), "
          "recorded as a closed route question, NOT progress"
          % m4, True)

    # ------------------------------------------------------------ C
    section("C -- controls")
    sneg = [r for r in smooth if r["tau_full"] < 0.0]
    print("  C-S smooth: sigma indefinite (tau_full < 0) on %d/%d "
          "rungs (first h = %s); Weyl channel on smooth: "
          "Herglotz %s (the positive-half scalarization is "
          "comb-sign-blind -- the M4 content)"
          % (len(sneg), len(smooth),
             sneg[0]["h"] if sneg else "n/a",
             "SURVIVES" if sm_herg_ok else "BREAKS"))
    check("C-S smooth world fires at the wall channel (>= 1 rung "
          "with tau_full < 0)", len(sneg) >= 1, kill="KW")
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
            rc = anatomy(CTRL_KZ, keep_all=True, **kw)
        except (np.linalg.LinAlgError, AssertionError):
            rc = None
        if not isinstance(rc, dict):
            print("       %-8s: chain dies (%r) -> FIRES (the "
                  "Weyl channel dies with it)" % (nmc, rc))
            continue
        tau12c = None
        if rc.get("full") and "CJ" in rc:
            tau12c = float(np.linalg.eigvalsh(
                np.eye(NW) - rc["CJ"])[0])
        fired = (rc["negA"] > 0
                 or (tau12c is not None and tau12c <= 0.0))
        ok_c &= fired
        alc, bec, m0c = rc["chain"]
        mtest = m_contfrac(alc, bec, rc["h"] + 1, Z_HERG[0])
        print("       %-8s: neg(A) %d | tau_12 %s | Weyl channel: "
              "Herglotz at z=%s %s -> %s"
              % (nmc, rc["negA"],
                 ("%+.3e" % tau12c) if tau12c is not None
                 else "n/a", Z_HERG[0],
                 "holds" if mtest.imag > 0 else "BREAKS",
                 "FIRES" if fired else "SILENT"))
    check("C-E controls fire (wall channel or chain death)", ok_c,
          kill="KW")

    return finish(dict(m3p=m3p, m3h=m3h, m4=m4))


def finish(labels):
    section("V -- FROZEN VERDICT")
    n_pass = sum(1 for _n, okk in CHECKS if okk)
    n_tot = len(CHECKS)
    if KILLS:
        VERDICT = {"KP": "PIPELINE-BROKEN",
                   "KW": "WARD-BROKEN"}[KILLS[0]]
        print("\n  VERDICT: %s" % VERDICT)
    else:
        VERDICT = ("WEYLCOCYCLE-MEASURED / HERGLOTZ-WARDED / "
                   "MOEBIUS-EXACT / SOURCE-ONLY-ENTRIES / "
                   "%(m3p)s / %(m4)s" % labels)
        print("\n  VERDICT: %s" % VERDICT)
        print("    secondary: %(m3h)s" % labels)
    print("""
  HONEST FRAME (as frozen): the Weyl/Moebius structure is exact
  warded algebra of the deployed POSITIVE quadrature family; the
  Herglotz ward is identity-grade for a positive measure; the
  transfer entries are source-only and scale-free.  The screen
  verdict must be read TOGETHER with the wall-content type: an
  O(1) preservation margin that cannot distinguish the truth
  comb from the wall-violating smooth world is a WALL-BLIND
  functional -- the honest finding is then that THIS
  scalarization drops the wall, and the route needs the signed
  functional sigma (where the margin IS tau, i.e. relocation) or
  a genuinely new object.  NO RH claim.  No marker moves.""")
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed"
          % (time.time() - T0, n_tot, n_tot - n_pass))
    return 0 if n_pass == n_tot else 1


if __name__ == "__main__":
    raise SystemExit(main())
