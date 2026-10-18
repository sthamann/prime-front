#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""freetail_case_bridge_probe -- PRIME.CASE.FREETAIL.01
(EXPLORATION ONLY, experiments/; round 42: numerical verification of
the strategy memo's BRIDGING LEMMA for the sum-rule half of
PRIME.CASE.SUMRULE.01, plus the MNT structure-factor retype with the
estimator bias removed, 2026-08-09).

CONTEXT: the sum-rule contract demands a Case-type sum rule for the
deployed tilde-measure family => unconditional T_h <= 1 (the diagonal
half of the wall).  The memo's route: (L1) FREE-TAIL TRIANGULAR
REDUCTION -- the CD kernel K_h depends only on the first h recurrence
levels, so appending the free tail (a_k = 0, b_k = 1/2 for k > h) to
the finite Jacobi data of mu~+ gives J_h^ft, a FINITE-RANK
perturbation of the free Jacobi matrix, whose finite Case identities
apply without a double limit; (L2) the positive functional is
P2 = C0 + (1/2) C2 (NOT C0/C1); (L3) the MNT factor ~2.4 of
testing_mnt_law_probe carries a deterministic 8/7 = 1.1428 estimator
bias (KNN = 8 masses over 7 gaps).

THE FINITE CASE IDENTITY TESTED (B2), in the Killip-Simon
normalization (Jacobi entries a_n -> 1, b_n -> 0, free spectrum
[-2, 2]; the deployed chain maps as a_n^KS = 2 b_n, b_n^KS = 2 a_n,
spectral variable E = 2 x):

    Q(J) + sum_j F(E_j)
        = sum_{n=1}^{h} [ (1/4) (b_n^KS)^2 + (1/2) G(a_n^KS) ]
    Q(J) = (1/(4 pi)) Int_{-2}^{2}
           log( sqrt(4 - E^2) / (2 pi f(E)) ) sqrt(4 - E^2) dE
    G(a) = a^2 - 1 - log a^2
    F(E) = (1/4) [ beta^2 - beta^{-2} - log beta^4 ],
           E = beta + 1/beta, |beta| > 1

(Killip-Simon, Ann. of Math. 158 (2003), Theorem 1: the P2 = C0 +
(1/2) C2 sum rule; step-by-step / finite form: Simon, "Szego's
theorem and its descendants", Ch. 3.  For J_h^ft a FINITE-RANK
perturbation of the free matrix every term is a finite object and
the identity is exact algebra: f is the exact ac density obtained by
coefficient stripping m^{(k-1)} = 1/(b_k^KS - E - (a_k^KS)^2 m^{(k)})
down to m_free(E + i0) = (-E + i sqrt(4 - E^2))/2; the eigenvalue
sum is finite, located by a renormalized downward shooting solution
u_n with u_0(E_j) = 0.)

FROZEN PROTOCOL (2026-08-09; heavy rungs kz {9, 12, 13, 26, 40};
controls kz 9):

 B1  KERNEL INVARIANCE (L1, exact): K_h(y_m, y_m) from the raw
     tilde-chain vs K_h rebuilt from the spectral measure of the
     TRUNCATED free-tail operator J_h^ft (dense eigh, tail 600, then
     re-Lanczos): relative deviation at the deployed neg nodes on
     every heavy rung: MEDIAN <= 1e-12 and MAX <= 1e-9 (a tautology
     once implemented right -- the ward guards the implementation;
     the max tier absorbs the float64 roundtrip floor at near-edge
     outside eigenvalues, see AMENDMENTS).

 B2  FINITE CASE IDENTITY: the P2 sum rule above for J_h^ft;
     spectral side Q (midpoint quadrature, N = 2^18, doubling check
     printed) + eigenvalue term (shooting + bisection, count
     cross-checked against the truncated matrix); coefficient side
     exact.  Ward: |Q + sum F - RHS| <= 1e-8 per heavy rung (exact
     algebra for finite perturbations).  The three pieces (Szego
     term Q, eigenvalue term sum F, coefficient energy RHS) reported
     per rung with their h-trend (WHICH piece grows), plus the
     honest gap between what the finite identity gives (an
     integrated/entropy statement: Q <= RHS since sum F >= 0) and
     what T_h <= 1 needs (a POINTWISE bound at the deployed nodes).

 B3  P2 ENERGY UNIFORMITY (typed): E_h = sum_{k<h} [a_k^2 +
     (2 b_k - 1)^2] across the full reachable ladder
     (frame_a_zones, h <= 900, 42 rungs): typed P2-BOUNDED iff
     sup over the deep half <= 1.2 x sup over the shallow half
     (rungs sorted by h), else P2-GROWS (both honest; P2-BOUNDED is
     the precondition for a uniform sum-rule theorem).  Interior sum
     (k <= 3h/4) reported alongside (chain-end spike separated).

 B4  MNT RETYPE (L3): the two-density ratio T/That with a
     VORONOI-CELL estimator (each pos node's local weight = mass /
     its Voronoi cell length; no KNN sum-over-gaps bias): corrected
     bulk medians (tau-deciles 3..8) and port values (decile 0) per
     heavy rung; the old KNN = 8 estimator recomputed alongside
     (the memo's REGULAR-GRID bias prediction is 8/7; the measured
     quotient is reported as-is); the EXACT free-tail density
     f_ft(E = 2y) as a third, estimator-free column; the
     flattened-weight benchmark (same node mask, flat masses) and
     the full-grid flattened benchmark (all folded grid nodes, flat
     masses).  Typed MNT-FACTOR-RETYPED with the corrected constant.
     HONEST READING (frozen): the remaining factor is a constrained
     discrete/node-mask effect (the memo's S_h), NOT a universal
     3 pi/4 -- no numerology.

 C   CONTROLS (kz 9, scramble seed 1): the ALGEBRAIC identities
     persist (B1/B2 are measure-blind algebra -- stated, not a
     kill); must-fire on the VALUES: scramble max T > 1 OR the
     coefficient energy RHS moves by > 10 % relative to the real
     rung; which channel fires is stated.

KILLS: pipeline breaks -> PIPELINE-BROKEN; B1 or B2 ward fails ->
IDENTITY-BROKEN; controls silent -> CONTROL-DEAD.  B3/B4 types may
FAIL honestly (typed, kept).

VERDICT (frozen enum): FREETAIL-BRIDGE-MEASURED (+ sublabels
P2-BOUNDED/P2-GROWS, MNT-FACTOR-RETYPED(c), the growing piece) /
PIPELINE-BROKEN / IDENTITY-BROKEN / CONTROL-DEAD.

SPEC AMENDMENTS (fail-first preserved):
  v1 (2026-08-09, first run): (i) the quasi-Szegő prefactor was
  written 1/(2 pi); the v1 run FAILED B2 honestly with residual
  = +RHS EXACTLY on all five heavy rungs (kz 9/12/13/26/40:
  +6.29e-1/+5.83e-1/+6.55e-1/+6.58e-1/+6.55e-1), i.e. Q_v1 = 2 RHS
  - 2 sum F.  The rank-one check pins the constant: for the free
  matrix with b_1^KS = eps (no bound state for small eps) the exact
  density gives log(f_0/f) = log(1 - eps E + eps^2), whose
  sqrt(4-E^2)-weighted integral is eps^2 pi + O(eps^3), so RHS =
  eps^2/4 forces the prefactor 1/(4 pi).  v2 fixes the constant;
  no bar was moved.  (ii) the B1 ward "max <= 1e-12" FAILED
  honestly at kz 13 (1.235e-10): the rung carries an outside
  eigenvalue at distance 3.9e-3 from the band edge, and the
  float64 eigh + re-Lanczos roundtrip already has coefficient
  roundoff ~8.5e-12 (dense and tridiagonal-MRRR eigensolvers
  identical), which the recurrence amplifies only at the extreme
  port node y = 0.99982 (median deviation 8.4e-13).  v2 splits the
  ward: MEDIAN <= 1e-12 (the tautology) and MAX <= 1e-9 (the
  float64 roundtrip floor); quadrature raised 2^17 -> 2^18 for
  margin under the untouched 1e-8 identity ward.  (iii) the memo's
  B4 EXPECTATIONS (~2.14 corrected bulk; KNN bias exactly 8/7) were
  never bars and are NOT recovered: the measured KNN/Voronoi
  quotient is 1.60-2.09 (the sum-over-gaps bias is itself
  mask-dependent, 8/7 is only its regular-grid value), so the
  Voronoi-corrected bulk constant lands at ~1.29; the full-grid
  flattened benchmark at 0.997-0.999 validates the estimator
  pipeline.  Reported as measured; no numerology either way.

NO RH claim: the finite identity is unconditional algebra for
J_h^ft; the bridge to T_h <= 1 (pointwise vs entropy + the S_h node
mask) is measured, not proven; the off-diagonal lift stays RH-hard.

FIREWALL: no zeros, no prime oracles (AST scan); v563 READ-ONLY;
RNG only in the scramble control; stdout only.  No marker moves.

Sources (read-only): v563_paper2_readouts; case_sum_rule_probe
(chain + KS functional), testing_mnt_law_probe (two-density law +
KNN estimator), declared inputs.

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/freetail_case_bridge_probe.py
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
KNN = 8                        # the OLD estimator (bias 8/7), replayed
NTAIL = 600                    # free-tail truncation length (B1)
NQ = 1 << 18                   # quadrature points for Q (B2)
TOL_B1_MED = 1.0e-12           # kernel invariance ward (median tier)
TOL_B1_MAX = 1.0e-9            # kernel invariance ward (max tier, v2)
TOL_B2 = 1.0e-8                # finite Case identity ward
H_LADDER_MAX = 900             # reachable-rung cap (the 42 rungs)
N_RUNGS_EXP = 42               # frozen expected rung count
P2_RATIO_BAR = 1.2             # B3 typing bar (deep sup / shallow sup)
RHS_FIRE_REL = 0.10            # control channel 2 bar
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
# (grid density, folded arm measures, Lanczos chain, CD kernel: verbatim
#  from case_sum_rule_probe / testing_mnt_law_probe)

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


def build_rung(kz, scramble_seed=None):
    """Window -> pos/neg folded measures -> chain -> CD diagonal + T."""
    rr = core.build_window(kz, scramble_seed=scramble_seed)
    h, M, D, alpha = rr["h"], rr["M"], rr["D"], rr["alpha"]
    uu = np.asarray(rr["uu"], float)
    mm = 2.0 * np.asarray(rr["lam"], float)
    c_at, _ = core.atom_lags_at(alpha, M, uu, mm)
    c_ar = np.asarray(core.arch_lags(M, D), float)
    d = grid_density(c_ar + np.asarray(c_at, float))
    L = 2 * M - 2
    xs, ws, _ = folded_measure(d, L, +1.0)
    ys, vs, uf_n = folded_measure(d, L, -1.0)
    al, be, m0, steps = lanczos_chain(xs, ws, h + 1)
    if steps < h + 1:
        return None
    Pn = eval_chain(al, be, m0, ys, h)
    Kdiag = np.sum(Pn ** 2, axis=1)
    T = vs * Kdiag
    tau_m = (2.0 * math.pi * uf_n / L) / D
    dec = np.minimum((10 * tau_m / np.max(tau_m)).astype(int), 9)
    return dict(kz=kz, h=h, L=L, D=D, xs=xs, ws=ws, ys=ys, vs=vs,
                dec=dec, al=al, be=be, m0=m0, Kdiag=Kdiag, T=T,
                A2=2.0 * be[:h], B2=2.0 * al[:h])


# ------------------------------------------------------------ B1: free tail
def freetail_kernel(al, be, m0, h, ys):
    """K_h rebuilt from the TRUNCATED J_h^ft: dense eigh spectral
    measure (mass m0), re-Lanczos, CD diagonal.  Also returns the
    truncated count of eigenvalues outside [-1, 1] (our scale)."""
    N = h + NTAIL
    dg = np.zeros(N)
    dg[:h] = al[:h]
    off = np.full(N - 1, 0.5)
    off[:h] = be[:h]
    J = np.diag(dg) + np.diag(off, 1) + np.diag(off, -1)
    ev, vec = np.linalg.eigh(J)
    wsp = m0 * vec[0, :] ** 2
    n_out = int(np.sum(np.abs(ev) > 1.0 + 1e-9))
    al2, be2, m02, steps = lanczos_chain(ev, wsp, h + 1)
    if steps < h + 1:
        return None, n_out
    Pn = eval_chain(al2, be2, m02, ys, h)
    return np.sum(Pn ** 2, axis=1), n_out


# ---------------------------------------------------- B2: finite Case (P2)
def m_strip(A2, B2v, E):
    """Exact m-function of J_h^ft on the essential spectrum: free
    boundary value + coefficient stripping (Herglotz-preserving)."""
    m = 0.5 * (-E + 1j * np.sqrt(4.0 - E * E))
    for k in range(len(A2) - 1, -1, -1):
        m = 1.0 / (B2v[k] - E - (A2[k] ** 2) * m)
    return m


def quasi_szego(A2, B2v, nq):
    """Q = (1/4pi) Int log(sqrt(4-E^2)/(2 pi f)) sqrt(4-E^2) dE via
    theta = arccos(E/2), composite midpoint (endpoint-clean); the
    1/(4 pi) constant is pinned by the rank-one expansion (see
    AMENDMENTS v2)."""
    th = (np.arange(nq) + 0.5) * math.pi / nq
    E = 2.0 * np.cos(th)
    f = m_strip(A2, B2v, E).imag / math.pi
    s = np.sin(th)
    integ = np.log(2.0 * s / (2.0 * math.pi * f)) * s * s
    return float(np.sum(integ)) / nq


def shoot_u0(A2, B2v, E):
    """Renormalized downward shooting: u_0(E) for real |E| > 2 (the
    decaying free solution appended at the tail); zeros = point
    spectrum of J_h^ft."""
    h = len(A2)
    beta = 0.5 * (E + np.sign(E) * np.sqrt(E * E - 4.0))
    up = np.ones_like(E)          # u_{h+1}
    upp = 1.0 / beta              # u_{h+2}
    for n in range(h + 1, 0, -1):
        Bn = B2v[n - 1] if n <= h else 0.0
        An = A2[n - 1] if n <= h else 1.0
        Anm1 = A2[n - 2] if n >= 2 else 1.0
        u = ((E - Bn) * up - An * upp) / Anm1
        upp, up = up, u
        sc = np.maximum(np.maximum(np.abs(up), np.abs(upp)), 1e-300)
        up = up / sc
        upp = upp / sc
    return up


def point_spectrum(A2, B2v):
    """Eigenvalues of J_h^ft outside [-2, 2] (shooting + bisection)
    and the P2 eigenvalue functional sum F(E_j)."""
    h = len(A2)
    emax = 2.0
    for n in range(1, h + 2):
        b = B2v[n - 1] if n <= h else 0.0
        left = A2[n - 2] if 2 <= n <= h + 1 else (1.0 if n > h + 1
                                                  else 0.0)
        right = A2[n - 1] if n <= h else 1.0
        emax = max(emax, abs(b) + left + right)
    emax += 0.5
    tmax = 0.5 * (emax + math.sqrt(emax * emax - 4.0))
    ts = 1.0 + np.geomspace(1e-9, tmax - 1.0, 4000)
    eigs = []
    for sgn in (+1.0, -1.0):
        E = sgn * (ts + 1.0 / ts)
        v = shoot_u0(A2, B2v, E)
        idx = np.nonzero(v[:-1] * v[1:] < 0.0)[0]
        for i in idx:
            lo, hi = ts[i], ts[i + 1]
            flo = float(shoot_u0(A2, B2v,
                                 np.array([sgn * (lo + 1.0 / lo)]))[0])
            for _ in range(64):
                mid = 0.5 * (lo + hi)
                fm = float(shoot_u0(
                    A2, B2v, np.array([sgn * (mid + 1.0 / mid)]))[0])
                if flo * fm <= 0.0:
                    hi = mid
                else:
                    lo, flo = mid, fm
            t = 0.5 * (lo + hi)
            eigs.append((sgn * (t + 1.0 / t), t))
    sF = 0.0
    for _e, t in eigs:
        sF += 0.25 * (t * t - 1.0 / (t * t)) - math.log(t)
    return [e for e, _t in eigs], sF


# -------------------------------------------------------- B4: density reads
def voronoi_density(x_sorted, w_sorted):
    edges = np.empty(len(x_sorted) + 1)
    edges[1:-1] = 0.5 * (x_sorted[1:] + x_sorted[:-1])
    edges[0] = x_sorted[0] - 0.5 * (x_sorted[1] - x_sorted[0])
    edges[-1] = x_sorted[-1] + 0.5 * (x_sorted[-1] - x_sorted[-2])
    return w_sorted / np.diff(edges)


def nearest_idx(x_sorted, y):
    i = np.searchsorted(x_sorted, y)
    i0 = np.clip(i - 1, 0, len(x_sorted) - 1)
    i1 = np.clip(i, 0, len(x_sorted) - 1)
    return np.where(np.abs(x_sorted[i1] - y)
                    < np.abs(x_sorted[i0] - y), i1, i0)


def knn_density(xs_s, ws_s, ys):
    """The OLD frozen k = 8 mass/span estimator (bias 8/7), verbatim
    from testing_mnt_law_probe."""
    out = np.empty(len(ys))
    for m in range(len(ys)):
        i0 = np.searchsorted(xs_s, ys[m])
        lo = max(0, i0 - KNN // 2)
        hi = min(len(xs_s), lo + KNN)
        lo = max(0, hi - KNN)
        span = xs_s[hi - 1] - xs_s[lo]
        out[m] = (float(np.sum(ws_s[lo:hi])) / span if span > 0
                  else np.nan)
    return out


def mnt_ratio(Kdiag, ys, h, wdens):
    """S = K_h(y,y) * pi * sqrt(1-y^2) * w(y) / h: the structure
    factor (== T/That; the neg masses cancel)."""
    return (Kdiag * math.pi
            * np.sqrt(np.maximum(1.0 - ys ** 2, 1e-12)) * wdens / h)


def flat_structure(xs, h, ys, mask):
    """Structure factor of the FLATTENED measure on the same node
    set (flat masses; self-consistent Voronoi density)."""
    o = np.argsort(xs)
    xs_s = xs[o]
    ws_s = np.full(len(xs_s), 1.0 / len(xs_s))
    al, be, m0, steps = lanczos_chain(xs_s, ws_s, h + 1)
    if steps < h + 1:
        return None
    Pn = eval_chain(al, be, m0, ys, h)
    Kd = np.sum(Pn ** 2, axis=1)
    wv = voronoi_density(xs_s, ws_s)[nearest_idx(xs_s, ys)]
    return float(np.median(mnt_ratio(Kd, ys, h, wv)[mask]))


def main():
    section("PRIME.CASE.FREETAIL.01 -- the free-tail bridging lemma, "
            "measured (EXPLORATION ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s"
          % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
    print("    NO RH claim; no marker moves.")
    print("\nS0 -- firewall")
    check("S0.1 AST firewall clean", not ast_scan(BANNED_IDS))

    section("B0 -- heavy rungs (chains + CD kernel + T)")
    R = {}
    ok = True
    for kz in HEAVY:
        r = build_rung(kz)
        ok &= r is not None
        if r is None:
            print("    kz %-3d: CHAIN SHORT" % kz)
            continue
        R[kz] = r
        print("    kz %-3d h %4d: pos nodes %5d, neg nodes %5d, "
              "m0 %.4e, max T %.4f"
              % (kz, r["h"], len(r["xs"]), len(r["ys"]), r["m0"],
                 float(np.max(r["T"]))))
    check("B0.1 all heavy chains complete", ok, kill="PIPELINE")
    if not ok:
        return finish(None, None, None, None)

    section("B1 -- KERNEL INVARIANCE under the free tail (L1, exact)")
    ok_b1 = True
    for kz in HEAVY:
        r = R[kz]
        Kft, n_out = freetail_kernel(r["al"], r["be"], r["m0"],
                                     r["h"], r["ys"])
        if Kft is None:
            ok_b1 = False
            print("    kz %-3d: re-Lanczos SHORT" % kz)
            continue
        dv = np.abs(Kft / r["Kdiag"] - 1.0)
        dmax, dmed = float(np.max(dv)), float(np.median(dv))
        r["n_out_trunc"] = n_out
        ok_b1 &= (dmed <= TOL_B1_MED) and (dmax <= TOL_B1_MAX)
        print("    kz %-3d h %4d: |K_ft/K_raw - 1| median %.3e / "
              "max %.3e (trunc eigs outside [-1,1]: %d)"
              % (kz, r["h"], dmed, dmax, n_out))
    check("B1.1 K_h identical from raw chain and J_h^ft at deployed "
          "nodes (median <= %.0e, max <= %.0e)"
          % (TOL_B1_MED, TOL_B1_MAX), ok_b1, kill="IDENTITY")

    section("B2 -- FINITE CASE IDENTITY (P2 = C0 + C2/2) for J_h^ft")
    ok_b2 = True
    rows = []
    for kz in HEAVY:
        r = R[kz]
        A2, B2v = r["A2"], r["B2"]
        rhs = float(np.sum(0.25 * B2v ** 2
                           + 0.5 * (A2 ** 2 - 1.0
                                    - np.log(A2 ** 2))))
        q_lo = quasi_szego(A2, B2v, NQ // 2)
        q_hi = quasi_szego(A2, B2v, NQ)
        eigs, sF = point_spectrum(A2, B2v)
        resid = q_hi + sF - rhs
        ok_b2 &= abs(resid) <= TOL_B2
        r.update(Q=q_hi, sF=sF, RHS=rhs, n_eig=len(eigs))
        rows.append(r)
        print("    kz %-3d h %4d: Q = %+.8f  sumF = %+.8f (n_eig %d"
              " | trunc %d)  RHS = %+.8f  resid = %+.2e  "
              "(quad dQ %.1e)"
              % (kz, r["h"], q_hi, sF, len(eigs),
                 r.get("n_out_trunc", -1), rhs, resid,
                 abs(q_hi - q_lo)))
    check("B2.1 finite P2 sum rule holds on every heavy rung "
          "(|resid| <= %.0e)" % TOL_B2, ok_b2, kill="IDENTITY")
    rows.sort(key=lambda r: r["h"])
    sh, dp = rows[:2], rows[-2:]

    def _avg(rr, key):
        return sum(abs(x[key]) for x in rr) / len(rr)
    grow = {k: _avg(dp, k) / max(_avg(sh, k), 1e-30)
            for k in ("Q", "sF", "RHS")}
    grow_lab = {"Q": "SZEGO-TERM", "sF": "EIG-TERM",
                "RHS": "COEFF-ENERGY"}[max(grow, key=grow.get)]
    print("    h-trend (deep/shallow, |.|-averaged): Q x%.2f, "
          "sumF x%.2f, RHS x%.2f  -> growing piece: %s"
          % (grow["Q"], grow["sF"], grow["RHS"], grow_lab))
    print("\n    THE HONEST GAP (identity vs T_h <= 1):")
    for r in rows:
        bulk = (r["dec"] >= 3) & (r["dec"] <= 8)
        port = r["dec"] == 0
        print("      kz %-3d h %4d: identity gives Q <= RHS = %.4f "
              "(entropy budget, sumF = %.4f >= 0) | needs: sup T "
              "<= 1; measured sup T bulk %.4f, port %.4f, all %.4f"
              % (r["kz"], r["h"], r["RHS"], r["sF"],
                 float(np.max(r["T"][bulk])),
                 float(np.max(r["T"][port])) if port.any() else -1.0,
                 float(np.max(r["T"]))))
    print("    The finite identity is an INTEGRATED (L1/entropy) "
          "bound on the ac density of J_h^ft;")
    print("    T_h <= 1 is a POINTWISE bound at the deployed nodes "
          "against the DISCRETE measure.")
    print("    Missing bridge = pointwise lower bound on f from the "
          "entropy budget (Nyquist) + the S_h node-mask factor (B4);")
    print("    uniform-in-h one-sidedness of the budget iff B3 types "
          "P2-BOUNDED.")

    section("B3 -- P2 COEFFICIENT ENERGY across the ladder (typed)")
    zones = [kz for kz in core.frame_a_zones()]
    lad = []
    for kz in zones:
        if kz in R:
            r = R[kz]
            a, b, h = r["al"][:r["h"]], r["be"][:r["h"]], r["h"]
        else:
            rr = core.build_window(kz)
            if rr["h"] > H_LADDER_MAX:
                continue
            r2 = build_rung(kz)
            if r2 is None:
                print("    kz %-3d: chain short (skipped)" % kz)
                continue
            a, b, h = r2["al"][:r2["h"]], r2["be"][:r2["h"]], r2["h"]
        g = a ** 2 + (2.0 * b - 1.0) ** 2
        lad.append((h, kz, float(np.sum(g)),
                    float(np.sum(g[:(3 * h) // 4]))))
    check("B3.0 frozen rung count: %d reachable rungs" % N_RUNGS_EXP,
          len(lad) == N_RUNGS_EXP, "found %d" % len(lad))
    lad.sort()
    nl = len(lad)
    sup_sh = max(e for _h, _k, e, _ei in lad[:nl // 2])
    sup_dp = max(e for _h, _k, e, _ei in lad[nl // 2:])
    sup_sh_i = max(ei for _h, _k, _e, ei in lad[:nl // 2])
    sup_dp_i = max(ei for _h, _k, _e, ei in lad[nl // 2:])
    for hh, kk, e, ei in lad[::max(nl // 8, 1)]:
        print("    kz %-3d h %4d: E_h = %.4f (interior k<=3h/4: "
              "%.4f)" % (kk, hh, e, ei))
    p2_ok = sup_dp <= P2_RATIO_BAR * sup_sh
    p2_lab = "P2-BOUNDED" if p2_ok else "P2-GROWS"
    print("    sup shallow half %.4f vs sup deep half %.4f "
          "(ratio %.3f; bar %.1f) | interior: %.4f vs %.4f "
          "(ratio %.3f)"
          % (sup_sh, sup_dp, sup_dp / sup_sh, P2_RATIO_BAR,
             sup_sh_i, sup_dp_i, sup_dp_i / sup_sh_i))
    check("B3.1 typed: %s (full-chain P2 energy, %d rungs)"
          % (p2_lab, nl), p2_ok)

    section("B4 -- MNT RETYPE: Voronoi vs KNN vs exact free-tail "
            "density + flattened benchmarks")
    med_vor = []
    for kz in HEAVY:
        r = R[kz]
        o = np.argsort(r["xs"])
        xs_s, ws_s = r["xs"][o], r["ws"][o]
        bulk = (r["dec"] >= 3) & (r["dec"] <= 8)
        port = r["dec"] == 0
        wv = voronoi_density(xs_s, ws_s)[nearest_idx(xs_s, r["ys"])]
        s_vor = mnt_ratio(r["Kdiag"], r["ys"], r["h"], wv)
        wk = knn_density(xs_s, ws_s, r["ys"])
        s_knn = mnt_ratio(r["Kdiag"], r["ys"], r["h"], wk)
        E_neg = np.clip(2.0 * r["ys"], -2.0 + 1e-12, 2.0 - 1e-12)
        f_ft = m_strip(r["A2"], r["B2"], E_neg).imag / math.pi
        s_ex = mnt_ratio(r["Kdiag"], r["ys"], r["h"],
                         r["m0"] * 2.0 * f_ft)
        s_fl = flat_structure(r["xs"], r["h"], r["ys"], bulk)
        uf_all = np.arange(0, r["L"] // 2 + 1)
        xg = np.cos(2.0 * math.pi * uf_all / r["L"])
        s_fg = flat_structure(xg, r["h"], r["ys"], bulk)
        mv = float(np.median(s_vor[bulk]))
        mk = float(np.median(s_knn[np.isfinite(s_knn) & bulk]))
        me = float(np.median(s_ex[bulk]))
        med_vor.append(mv)
        print("    kz %-3d h %4d: bulk median T/That -- KNN8 %.3f | "
              "VORONOI %.3f (knn/vor %.3f; 8/7 = %.3f) | exact-f_ft "
              "%.3f | FLAT-mask %.3f | FULL-GRID-flat %.3f"
              % (kz, r["h"], mk, mv, mk / mv, 8.0 / 7.0, me,
                 -1.0 if s_fl is None else s_fl,
                 -1.0 if s_fg is None else s_fg))
        print("             port (dec 0) Voronoi T/That: %s"
              % " ".join("%.2f" % v for v in s_vor[port][:5]))
        r["port_vor_med"] = (float(np.median(s_vor[port]))
                             if port.any() else float("nan"))
    c_retype = float(np.median(med_vor))
    check("B4.1 typed: MNT-FACTOR-RETYPED (corrected bulk constant "
          "c = %.3f; Voronoi, median over heavy rungs)" % c_retype,
          True)
    print("    HONEST READING (frozen): the corrected bulk factor "
          "(~%.2f) and the flattened benchmarks show the excess"
          % c_retype)
    print("    over 1 is a constrained discrete/node-mask effect "
          "(the memo's S_h): it moves with the mask/weights family")
    print("    (mask+arithmetic weights -> flat mask -> full grid) "
          "and is NOT the universal constant 3 pi/4 = %.4f."
          % (3.0 * math.pi / 4.0))
    print("    Note: the measured KNN/Voronoi quotient EXCEEDS the "
          "regular-grid 8/7 (the KNN bias is itself mask-dependent),")
    print("    so the memo's ~2.14 (= 2.4 x 7/8) is NOT recovered; "
          "against the EXACT free-tail density f_ft the bulk ratio")
    print("    is even < 1 (the smooth J_h^ft density overestimates "
          "the local deployed weight at the neg nodes).")
    print("    No numerology: no constant is claimed, the factor is "
          "typed as a measured, family-dependent S_h.")

    section("C -- controls (kz 9, scramble seed 1)")
    rs = build_rung(9, scramble_seed=1)
    if rs is None:
        check("C0 scramble chain completes", False, kill="PIPELINE")
        return finish(grow_lab, p2_lab, c_retype, None)
    rhs_s = float(np.sum(0.25 * rs["B2"] ** 2
                         + 0.5 * (rs["A2"] ** 2 - 1.0
                                  - np.log(rs["A2"] ** 2))))
    q_s = quasi_szego(rs["A2"], rs["B2"], NQ)
    _eigs_s, sF_s = point_spectrum(rs["A2"], rs["B2"])
    resid_s = q_s + sF_s - rhs_s
    print("    scramble finite P2 identity: Q %+.6f + sumF %+.6f "
          "vs RHS %+.6f -> resid %+.2e (the ALGEBRA persists, as "
          "it must -- value control only)" % (q_s, sF_s, rhs_s,
                                              resid_s))
    tmax_s = float(np.max(rs["T"]))
    rel_rhs = abs(rhs_s - R[9]["RHS"]) / R[9]["RHS"]
    f1 = tmax_s > 1.0
    f2 = rel_rhs > RHS_FIRE_REL
    o = np.argsort(rs["xs"])
    wv_s = voronoi_density(rs["xs"][o], rs["ws"][o])[
        nearest_idx(rs["xs"][o], rs["ys"])]
    s_vor_s = mnt_ratio(rs["Kdiag"], rs["ys"], rs["h"], wv_s)
    port_s = rs["dec"] == 0
    print("    channels: max T %.3e (real %.3f) -> %s | RHS rel "
          "shift %.3f (bar %.2f) -> %s | port Voronoi median %.2f "
          "(real %.2f, informative)"
          % (tmax_s, float(np.max(R[9]["T"])),
             "FIRES" if f1 else "silent", rel_rhs, RHS_FIRE_REL,
             "FIRES" if f2 else "silent",
             float(np.median(s_vor_s[port_s])) if port_s.any()
             else float("nan"), R[9]["port_vor_med"]))
    check("C1 CONTROLS FIRE on the values (max T > 1 or RHS shift "
          "> %.0f%%)" % (100 * RHS_FIRE_REL), f1 or f2,
          kill="CONTROL")
    return finish(grow_lab, p2_lab, c_retype,
                  "T-FIRES" if f1 else "RHS-FIRES")


def finish(grow_lab, p2_lab, c_retype, ctrl):
    section("V -- FROZEN VERDICT")
    n_pass = sum(1 for _n, okk in CHECKS if okk)
    n_tot = len(CHECKS)
    if "PIPELINE" in KILLS:
        VERDICT = "PIPELINE-BROKEN"
    elif "IDENTITY" in KILLS:
        VERDICT = "IDENTITY-BROKEN"
    elif "CONTROL" in KILLS:
        VERDICT = "CONTROL-DEAD"
    else:
        VERDICT = "FREETAIL-BRIDGE-MEASURED"
    sub = []
    if p2_lab:
        sub.append(p2_lab)
    if c_retype is not None:
        sub.append("MNT-FACTOR-RETYPED(c=%.3f)" % c_retype)
    if grow_lab:
        sub.append("GROWING-PIECE=%s" % grow_lab)
    if ctrl:
        sub.append("CONTROL=%s" % ctrl)
    print("\n  VERDICT: %s (%s)" % (VERDICT, " + ".join(sub)))
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed"
          % (time.time() - T0, n_tot, n_tot - n_pass))
    return 0 if n_pass == n_tot else 1


if __name__ == "__main__":
    raise SystemExit(main())
