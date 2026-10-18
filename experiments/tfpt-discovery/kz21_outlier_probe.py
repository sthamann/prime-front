#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""kz21_outlier_probe -- PRIME.PORT.KZ21.01
(EXPLORATION ONLY, experiments/; round 53, named object (b) from
CX: dissect the kz-21 outlier of the soft-flag constant ladder.
2026-08-09.)

THE CONTRACT (frozen).  Round 52 (relative_flag_margin_probe,
PRIME.PORT.RELFLAG.01) measured the soft-flag constant c_h =
d_{12,h}/tau_h on the 37 truth full-window rungs (d_12 the soft
LDL pivot of A_h = I - C_J(h), tau_h = lambda_min(A_h); exact
algebra d_12 = 1/(A_h^{-1})_{12,12} >= tau_h).  ONE rung -- kz 21
(h = 371) -- carries c ~ 50667 against ladder quartiles
1163/2117/2930, and alone blows the spread max c / min c to
124.2 > CSPREAD_BAR = 100, typing the ladder SOFTFLAG-UNTIED.
PRECEDENT (kz19_anomaly_probe, PRIME.PORT.KZ19.01, round 42):
kz 19's kappa outlier was a pivot-seat/COORDINATE artifact -- the
argmax seat jumped to a bulk node with soft-mode overlap 8.5e-8,
not an arithmetic anomaly.  This probe dissects kz 21 with the
same forensic machinery: seat anatomy, neighborhood ledger, and
the exact spectral identity (A^{-1})_{12,12} = sum_r
|psi_r(12)|^2 / lambda_r, with FROZEN decision rules and a
diagnosis-conditioned re-fit of the c-ladder spread (reported as
SENSITIVITY, never as cherry-pick).

FROZEN PROTOCOL (2026-08-09; all 42 reachable frame-A rungs
h <= H_DEEP_MAX = 900; the c-ladder lives on the truth
FULL-WINDOW rungs; neighborhood = the two reachable full-window
ladder rungs on each side of kz 21 in ladder order (h, kz);
controls kz 9):

 K1  REPRODUCE + NEIGHBORHOOD: rebuild the c-ladder on all truth
     full-window rungs (machinery VERBATIM from
     relative_flag_margin_probe: ONE Gram E_h per rung, 12-window
     Schur compression C_J onto JWIN = (2,4,...,24), A = I - C_J,
     d_12 = det_12/det_11 minor quotient).  Print h, tau, d_12, c
     for the kz-21 neighborhood.  WARDS (kill -> WARD-BROKEN):
       W-K1a  EXACT IDENTITY CHAIN on every full rung:
              d_12 == 1/(A^{-1})_{12,12} (rel <= ID_WARD = 1e-9)
              AND (A^{-1})_{12,12} == sum_r |psi_r(12)|^2 /
              lambda_r (rel <= ID_WARD) AND c >= 1 - CGE1_WARD
              (= 1e-9);
       W-K1b  ROUND-52 REPRODUCTION: kz 21 sits at h = 371 with
              c within 2 percent of 50667; ladder quartiles
              q25/med/q75 within 2 percent of 1163/2117/2930;
              spread within 2 percent of 124.2; log-log slope of
              c vs h within 5e-3 of +0.128.

 K2  THE SPECTRAL IDENTITY ANATOMY: expand (A^{-1})_{12,12} =
     sum_r |psi_r(12)|^2 / lambda_r on every neighborhood rung --
     which eigenvalue dominates at kz 21 vs neighbors?  Print the
     full-ladder (kz, h, c, |psi_soft(12)|^2, soft share) table
     and the per-mode expansion (lambda_r, |psi_r(12)|^2,
     contribution, share) at kz 21.  The kz-19 mechanism to test:
     if the soft mode's weight |psi_soft(12)|^2 at window
     coordinate 12 is anomalously SMALL at kz 21 (the coordinate
     decouples from the soft mode), then c = d_12/tau =
     1/(tau (A^{-1})_{12,12}) blows up as a COORDINATE artifact,
     not an arithmetic one.

 K3  SEAT/GEOMETRY ANATOMY (neighborhood): window parameters
     (alpha, D, M, atom count), taper edge u_max = (M-1) D,
     distance from u_max to the nearest atom, largest single-atom
     mass in [u_max - 0.5, u_max] (kz19 A4 verbatim); and the
     12-window composition -- for the window coordinate 12 (fold
     index j = 24): tau_j = (2 pi j / L)/D, the folded node mass
     v_j, and diag(C_J)_{12,12} across the neighborhood, plus the
     full j = 2..24 composition table at kz 21.

 K4  TYPED DIAGNOSIS (frozen rules mirroring kz19, evaluated in
     this order; trend_q(h*) := the LEAVE-KZ21-OUT log-log OLS
     fit of log q on log h over the other 36 full rungs,
     evaluated at h* = 371):
       COORDINATE-ARTIFACT iff |psi_soft(12)|^2 at kz 21 <
              W_COLLAPSE_FAC (= 0.2) x median |psi_soft(12)|^2
              over the 4 neighborhood rungs AND tau(kz21) is on
              trend: tau/trend_tau within [1/10, 10]
              (TAU_TREND_BAR = 10; the tau ladder carries
              order-of-magnitude scatter, round 52);
       ARITHMETIC iff the weight is normal (>= 0.2 x neighbor
              median) AND d_12 itself is off trend:
              d_12/trend_d12 outside [1/10, 10]
              (D12_TREND_BAR = 10);
       MIXED  otherwise.
     THEN THE RE-FIT: the c-ladder spread/slope with kz 21
     EXCLUDED (36 rungs) -- reported as SENSITIVITY if the
     diagnosis is COORDINATE-ARTIFACT, as descriptive otherwise.
     Does SOFTFLAG then type TIED (spread <= CSPREAD_BAR = 100
     AND |slope| <= CSLOPE_BAR = 1.0, round-52 bars verbatim)?
     Print the corrected spread either way.

 C   CONTROLS (kz 9, must fire, kill -> CONTROL-DEAD): Epstein
     x^2+5y^2 comb + scramble (seed 1) -- frame death OR
     neg(A_full) > 0 OR the 12-window base tau_12 <= 0 (the
     identity chain breaks as a VALUE: c = d_12/tau is
     meaningless off the PD cone) while the PIPELINE itself
     persists (the Gram/compression machinery runs); if C_J
     exists the exact identity d_12 = 1/(A^{-1})_{12,12} is
     printed to show the ALGEBRA persists while the value breaks.

W   PIPELINE WARDS (kill -> PIPELINE-BROKEN): W0 truth ladder ==
    42 rungs (deepcore reachable census); W0c truth full-window
    census == 37 (hirota); W0d kz 21 is a full-window rung with
    >= 2 full-window ladder neighbors on each side.

KILLS: KP a W ward breaks -> PIPELINE-BROKEN; KW a K1 ward
breaks -> WARD-BROKEN; KC controls silent -> CONTROL-DEAD.
K2/K3/K4 are typed forensics, never kill.

VERDICT (frozen enum): KZ21-DIAGNOSED (+ typed cause
COORDINATE-ARTIFACT / ARITHMETIC / MIXED) / PIPELINE-BROKEN /
WARD-BROKEN / CONTROL-DEAD.

FROZEN BARS: H_DEEP_MAX = 900; JWIN = (2,4,...,24); NW = 12;
N_RUNGS_EXP = 42; N_FULLWIN_FROZEN = 37; KZ_STAR = 21; H_STAR =
371; NEIGH_HALF = 2; REF_C21 = 50667 (rtol 2e-2); REF_Q25/MED/Q75
= 1163/2117/2930 (rtol 2e-2); REF_SPREAD = 124.2 (rtol 2e-2);
REF_SLOPE = +0.128 (atol 5e-3); ID_WARD = 1e-9; CGE1_WARD = 1e-9;
W_COLLAPSE_FAC = 0.2; TAU_TREND_BAR = 10; D12_TREND_BAR = 10;
CSPREAD_BAR = 100; CSLOPE_BAR = 1.0; CTRL_KZ = 9; scramble seed 1.

SPEC v1 (2026-08-09, frozen + SHA-hashed before the first run):
everything above.  Mechanical concretizations frozen with v1:
(i) core.build_window results are memoized per (kz, seed)
(round-52 verbatim); (ii) truth rungs run LIGHT (no full-wall
eigendecomposition -- only the 12-window compression C_J is
needed for the c-ladder); controls run with the full-wall
neg-count; (iii) C_J is built only on FULL windows (all 12 JWIN
indices present) -- partial windows carry no c and are outside
the round-52 ladder by construction; (iv) quartiles use
np.percentile linear interpolation (round-52 verbatim); (v) the
neighborhood median in K4 is over the 4 non-kz21 neighborhood
rungs (kz19 SIGMA-GEOMETRY precedent).

HONEST FRAME: this is single-rung forensics on a measured
37-rung finite ladder; the exact identity chain is warded
bookkeeping, zero content; the re-fit is a SENSITIVITY statement
about the finite ladder, NOT a repair of the SOFTFLAG typing and
NOT an asymptotic claim.  The round-52 raw numbers stand
unchanged.  NO RH claim.  No marker moves.

FIREWALL: no zeros, no prime oracles (AST scan; banned ids
zetazero / nzeros / primerange / isprime / primepi / nextprime /
prevprime); v563 READ-ONLY; RNG only inside the declared
scramble control; stdout only.

Sources (read-only): v563_paper2_readouts (build_window,
atom_lags_at, arch_lags -- verbatim); c-ladder machinery VERBATIM
from relative_flag_margin_probe.py (PRIME.PORT.RELFLAG.01: the
c-ladder, spread 124.2, kz 21 the outlier) via
factor_avoidance_euler_probe.py / pivot_factor_probe.py
(12-window compression, soft flag k = 12); forensic template
from kz19_anomaly_probe.py (PRIME.PORT.KZ19.01: seat anatomy,
typed diagnosis, sensitivity re-fit).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/kz21_outlier_probe.py
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
NEIGH_HALF = 2
ID_WARD = 1e-9
CGE1_WARD = 1e-9
W_COLLAPSE_FAC = 0.2
TAU_TREND_BAR = 10.0
D12_TREND_BAR = 10.0
CSPREAD_BAR = 100.0        # round-52 typing bars, verbatim
CSLOPE_BAR = 1.0
CTRL_KZ = 9
BANNED_IDS = ("zetazero", "nzeros", "primerange", "isprime",
              "primepi", "nextprime", "prevprime")

# round-52 reproduction anchors (relative_flag_margin printed)
REF_C21 = 50667.0
REF_C21_RTOL = 2e-2
REF_Q25, REF_MED, REF_Q75 = 1163.0, 2117.0, 2930.0
REF_Q_RTOL = 2e-2
REF_SPREAD = 124.2
REF_SPREAD_RTOL = 2e-2
REF_SLOPE = 0.128
REF_SLOPE_ATOL = 5e-3

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


# --------- pipeline, verbatim (relative_flag_margin chain)
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
    """SPEC v1 (i): pure memoization of core.build_window."""
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


def anatomy(kz, scramble_seed=None, comb=None, need_full=False):
    """One rung -> ONE Gram E on the folded neg nodes -> the
    12-window compression C_J (relative_flag_margin verbatim).
    LIGHT on truth rungs (SPEC v1 (ii)); need_full adds the
    full-wall neg-count for controls."""
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
    xs, ws, _ = folded_measure(d, L, +1.0)
    ys, vs, uf_n = folded_measure(d, L, -1.0)
    al, be, m0, steps = lanczos_chain(xs, ws, h + 1)
    if steps < h + 1 or np.any(be <= 0):
        return None
    Pn = eval_chain(al, be, m0, ys, h)
    E = np.sqrt(vs)[:, None] * (Pn @ Pn.T) * np.sqrt(vs)[None, :]
    E = 0.5 * (E + E.T)
    n = E.shape[0]
    out = dict(kz=kz, h=h, n=n, M=M, D=D, L=L, alpha=alpha,
               n_atom=rr["n_atom"], uf=uf_n, vs=vs)
    if need_full:
        evA = np.linalg.eigvalsh(np.eye(n) - E)
        out["tau_full"] = float(evA[0])
        out["negA"] = int(np.sum(evA < 0.0))
    idx = {int(j): k for k, j in enumerate(uf_n)}
    out["idx"] = idx
    jav = [j for j in JWIN if j in idx]
    out["full"] = (len(jav) == len(JWIN))
    if out["full"]:                       # SPEC v1 (iii)
        iw = [idx[j] for j in jav]
        io = [k for k in range(n) if k not in set(iw)]
        IO = np.eye(len(io)) - E[np.ix_(io, io)]
        try:
            CJ = (E[np.ix_(iw, iw)]
                  + E[np.ix_(iw, io)] @ np.linalg.solve(
                      IO, E[np.ix_(io, iw)]))
            out["CJ"] = 0.5 * (CJ + CJ.T)
        except np.linalg.LinAlgError:
            pass
    return out


def win_attrs(r):
    """Per-rung 12-window objects: minor-quotient d_12, tau,
    c, the resolvent entry and its exact spectral expansion."""
    A = np.eye(NW) - r["CJ"]
    det12 = float(np.linalg.det(A))
    det11 = float(np.linalg.det(A[:11, :11]))
    d12 = det12 / det11
    ew, Vw = np.linalg.eigh(A)
    Ainv = np.linalg.inv(A)
    a1212 = float(Ainv[11, 11])
    wgt = Vw[11, :] ** 2                 # |psi_r(12)|^2
    contrib = wgt / ew                   # per-mode contribution
    exp1212 = float(np.sum(contrib))
    r["A12"] = A
    r["d12"] = d12
    r["tau12"] = float(ew[0])
    r["c"] = d12 / r["tau12"]
    r["ew"] = ew
    r["wgt"] = wgt
    r["contrib"] = contrib
    r["a1212"] = a1212
    r["w_soft"] = float(wgt[0])
    r["soft_share"] = float(contrib[0] / exp1212)
    rd = int(np.argmax(contrib))
    r["dom_r"] = rd
    r["dom_share"] = float(contrib[rd] / exp1212)
    r["dev_inv"] = (abs(d12 - 1.0 / a1212)
                    / max(abs(d12), 1e-300))
    r["dev_exp"] = (abs(a1212 - exp1212)
                    / max(abs(a1212), 1e-300))
    return r


def ols_ab(x, y):
    """OLS y = a + b x -> (a, b)."""
    x = np.asarray(x, float)
    y = np.asarray(y, float)
    xm, ym = float(np.mean(x)), float(np.mean(y))
    b = float(np.sum((x - xm) * (y - ym))
              / np.sum((x - xm) ** 2))
    return ym - b * xm, b


def trend_at(hs, qs, h_star):
    """Leave-out log-log trend of q vs h, evaluated at h_star."""
    a, b = ols_ab(np.log(np.asarray(hs, float)),
                  np.log(np.asarray(qs, float)))
    return math.exp(a + b * math.log(h_star))


def quart_row(v):
    v = np.asarray(v, float)
    q = np.percentile(v, [25, 50, 75])
    return (float(np.min(v)), float(q[0]), float(q[1]),
            float(q[2]), float(np.max(v)))


def main():
    section("PRIME.PORT.KZ21.01 -- anatomy of the kz 21 "
            "soft-flag-constant outlier (EXPLORATION ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s"
          % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
    print("    NO RH claim; single-rung forensics on the finite "
          "37-rung c-ladder; no marker moves.")
    print("\nS0 -- firewall")
    check("S0.1 AST firewall clean (no zero/prime oracles)",
          not ast_scan(BANNED_IDS))

    # ------------------------------------------------------------ W
    section("W -- build the truth ladder (frame-A zones, h <= %d;"
            " LIGHT mode, ONE Gram per rung)" % H_DEEP_MAX)
    truth = []
    n_toodeep, n_dead = 0, 0
    for kz in core.frame_a_zones():
        r = anatomy(kz)
        if r == "TOO-DEEP":
            n_toodeep += 1
            continue
        if r is None:
            n_dead += 1
            continue
        truth.append(r)
    truth.sort(key=lambda r: (r["h"], r["kz"]))
    print("    truth: %d rungs (h %d..%d; %d TOO-DEEP zones, %d "
          "chain deaths)  [%.1f s]"
          % (len(truth), truth[0]["h"], truth[-1]["h"],
             n_toodeep, n_dead, time.time() - T0))
    check("W0 truth ladder == %d rungs (deepcore census)"
          % N_RUNGS_EXP, len(truth) == N_RUNGS_EXP,
          "%d" % len(truth), kill="KP")
    fullw = [r for r in truth if r.get("full") and "CJ" in r]
    check("W0c truth full-window census %d == %d (hirota frozen)"
          % (len(fullw), N_FULLWIN_FROZEN),
          len(fullw) == N_FULLWIN_FROZEN, kill="KP")
    kz_full = [r["kz"] for r in fullw]
    star_ok = (KZ_STAR in kz_full
               and NEIGH_HALF <= kz_full.index(KZ_STAR)
               < len(kz_full) - NEIGH_HALF)
    if star_ok:
        i_star = kz_full.index(KZ_STAR)
        NEIGH = fullw[i_star - NEIGH_HALF:
                      i_star + NEIGH_HALF + 1]
    else:
        NEIGH = []
    check("W0d kz %d is a full-window rung with %d ladder "
          "neighbors each side: %s"
          % (KZ_STAR, NEIGH_HALF,
             [r["kz"] for r in NEIGH]), star_ok, kill="KP")
    if KILLS:
        return finish(None)
    r_star = fullw[i_star]

    # ------------------------------------------------------------ K1
    section("K1 -- reproduce the c-ladder + the kz-21 "
            "neighborhood (round-52 machinery verbatim)")
    for r in fullw:
        win_attrs(r)
    dev_inv = max(r["dev_inv"] for r in fullw)
    dev_exp = max(r["dev_exp"] for r in fullw)
    c_min_all = min(r["c"] for r in fullw)
    check("W-K1a EXACT IDENTITY CHAIN: d_12 == 1/(A^-1)_{12,12} "
          "(max rel %.1e) AND resolvent == spectral expansion "
          "(max rel %.1e) <= %.0e AND min c = %.3f >= 1"
          % (dev_inv, dev_exp, ID_WARD, c_min_all),
          dev_inv <= ID_WARD and dev_exp <= ID_WARD
          and c_min_all >= 1.0 - CGE1_WARD, kill="KW")
    print("\n    the kz-21 neighborhood (full-window ladder "
          "order):")
    print("    %-4s %-5s %-11s %-11s %-11s"
          % ("kz", "h", "tau_h", "d_12", "c_h"))
    for r in NEIGH:
        print("    %-4d %-5d %-11.3e %-11.3e %-11.3f%s"
              % (r["kz"], r["h"], r["tau12"], r["d12"], r["c"],
                 "   <-- OUTLIER" if r["kz"] == KZ_STAR else ""))
    cs = np.array([r["c"] for r in fullw])
    hs = np.array([r["h"] for r in fullw], float)
    mn, q1, q2, q3, mx = quart_row(cs)
    spread = mx / mn
    _, b_c = ols_ab(np.log(hs), np.log(cs))
    print("\n    c quartiles: min %.3f q25 %.3f med %.3f q75 "
          "%.3f max %.3f | spread %.2f | slope %+.3f"
          % (mn, q1, q2, q3, mx, spread, b_c))
    check("W-K1b ROUND-52 REPRODUCTION: h(kz21) == %d; c(kz21) "
          "%.1f == %.0f (rtol %.0e); q25/med/q75 %.0f/%.0f/%.0f "
          "== %.0f/%.0f/%.0f; spread %.2f == %.1f; slope %+.3f "
          "== %+.3f (atol %.0e)"
          % (H_STAR, r_star["c"], REF_C21, REF_C21_RTOL,
             q1, q2, q3, REF_Q25, REF_MED, REF_Q75, spread,
             REF_SPREAD, b_c, REF_SLOPE, REF_SLOPE_ATOL),
          r_star["h"] == H_STAR
          and abs(r_star["c"] / REF_C21 - 1.0) <= REF_C21_RTOL
          and abs(q1 / REF_Q25 - 1.0) <= REF_Q_RTOL
          and abs(q2 / REF_MED - 1.0) <= REF_Q_RTOL
          and abs(q3 / REF_Q75 - 1.0) <= REF_Q_RTOL
          and abs(spread / REF_SPREAD - 1.0) <= REF_SPREAD_RTOL
          and abs(b_c - REF_SLOPE) <= REF_SLOPE_ATOL, kill="KW")

    # ------------------------------------------------------------ K2
    section("K2 -- the spectral identity (A^-1)_{12,12} = sum_r "
            "|psi_r(12)|^2 / lambda_r: who carries coordinate 12?")
    print("    full ladder (the soft-mode weight at window "
          "coordinate 12):")
    print("    %-4s %-5s %-11s %-11s %-11s %-6s %s"
          % ("kz", "h", "c_h", "w_soft", "soft-share", "dom-r",
             "dom-share"))
    for r in fullw:
        print("    %-4d %-5d %-11.3f %-11.3e %-11.3e %-6d %.3f%s"
              % (r["kz"], r["h"], r["c"], r["w_soft"],
                 r["soft_share"], r["dom_r"], r["dom_share"],
                 "   <-- OUTLIER" if r["kz"] == KZ_STAR else ""))
    print("\n    NEIGHBORHOOD SPECTRAL-WEIGHT TABLE (the "
          "deliverable):")
    print("    %-4s %-5s %-11s %-11s %-11s %-11s %-6s %s"
          % ("kz", "h", "tau_h", "c_h", "w_soft",
             "soft-share", "dom-r", "lam_dom"))
    for r in NEIGH:
        print("    %-4d %-5d %-11.3e %-11.3f %-11.3e %-11.3e "
              "%-6d %.4f%s"
              % (r["kz"], r["h"], r["tau12"], r["c"],
                 r["w_soft"], r["soft_share"], r["dom_r"],
                 float(r["ew"][r["dom_r"]]),
                 "   <-- OUTLIER" if r["kz"] == KZ_STAR else ""))
    print("\n    the full 12-mode expansion at kz %d (h %d):"
          % (KZ_STAR, r_star["h"]))
    print("    %-3s %-12s %-12s %-12s %s"
          % ("r", "lambda_r", "|psi_r(12)|^2", "contrib",
             "share"))
    for rr_ in range(NW):
        print("    %-3d %-12.4e %-12.4e %-12.4e %.4f"
              % (rr_, float(r_star["ew"][rr_]),
                 float(r_star["wgt"][rr_]),
                 float(r_star["contrib"][rr_]),
                 float(r_star["contrib"][rr_]
                       / r_star["a1212"])))
    w_nb = [r["w_soft"] for r in NEIGH if r["kz"] != KZ_STAR]
    w_med_nb = float(np.median(w_nb))
    check("K2.1 anatomy recorded (report): w_soft(kz21) %.3e vs "
          "neighborhood median %.3e (ratio %.3e); soft-mode "
          "share of (A^-1)_{12,12} at kz21 %.3e"
          % (r_star["w_soft"], w_med_nb,
             r_star["w_soft"] / w_med_nb, r_star["soft_share"]),
          True)

    # ------------------------------------------------------------ K3
    section("K3 -- seat/geometry anatomy: window parameters + "
            "the 12-window composition")
    print("    %-4s %-5s %-8s %-9s %-6s %-7s %-9s %-10s %-12s"
          % ("kz", "h", "alpha", "D", "M", "n_atom", "u_max",
             "d(edge,n)", "max-mass@.5"))
    for r in NEIGH:
        w = window_of(r["kz"])
        u_edge = (w["M"] - 1) * w["D"]
        dist = float(np.min(np.abs(u_edge - w["uu"])))
        last = w["uu"] >= u_edge - 0.5
        mmax = (float(np.max(2.0 * w["lam"][last]))
                if np.any(last) else 0.0)
        print("    %-4d %-5d %-8.3f %-9.5f %-6d %-7d %-9.3f "
              "%-10.4f %-12.4e%s"
              % (r["kz"], r["h"], w["alpha"], w["D"], w["M"],
                 w["n_atom"], u_edge, dist, mmax,
                 "   <-- OUTLIER" if r["kz"] == KZ_STAR else ""))
    print("\n    window coordinate 12 (fold index j = 24) across "
          "the neighborhood:")
    print("    %-4s %-9s %-12s %-12s"
          % ("kz", "tau_24", "node mass", "diag(C_J)_12"))
    for r in NEIGH:
        j = JWIN[-1]
        tau_j = (2.0 * math.pi * j / r["L"]) / r["D"]
        print("    %-4d %-9.4f %-12.4e %-12.4e%s"
              % (r["kz"], tau_j, float(r["vs"][r["idx"][j]]),
                 float(r["CJ"][NW - 1, NW - 1]),
                 "   <-- OUTLIER" if r["kz"] == KZ_STAR else ""))
    print("\n    the full 12-window composition at kz %d:"
          % KZ_STAR)
    print("    %-4s %-9s %-12s %-12s"
          % ("j", "tau_j", "node mass", "diag(C_J)"))
    for k, j in enumerate(JWIN):
        tau_j = (2.0 * math.pi * j / r_star["L"]) / r_star["D"]
        print("    %-4d %-9.4f %-12.4e %-12.4e"
              % (j, tau_j,
                 float(r_star["vs"][r_star["idx"][j]]),
                 float(r_star["CJ"][k, k])))
    check("K3.1 seat/geometry recorded (report)", True)

    # ------------------------------------------------------------ K4
    section("K4 -- TYPED DIAGNOSIS (frozen rules) + the "
            "diagnosis-conditioned re-fit")
    oth = [r for r in fullw if r["kz"] != KZ_STAR]
    tr_tau = trend_at([r["h"] for r in oth],
                      [r["tau12"] for r in oth], H_STAR)
    tr_d12 = trend_at([r["h"] for r in oth],
                      [r["d12"] for r in oth], H_STAR)
    rat_w = r_star["w_soft"] / w_med_nb
    rat_tau = r_star["tau12"] / tr_tau
    rat_d12 = r_star["d12"] / tr_d12
    tau_on_trend = (1.0 / TAU_TREND_BAR <= rat_tau
                    <= TAU_TREND_BAR)
    d12_off_trend = not (1.0 / D12_TREND_BAR <= rat_d12
                         <= D12_TREND_BAR)
    print("    leave-kz21-out trends at h = %d: tau %.3e "
          "(measured %.3e, ratio %.3f -> %s within [1/%.0f, "
          "%.0f]) | d_12 %.3e (measured %.3e, ratio %.3f -> %s)"
          % (H_STAR, tr_tau, r_star["tau12"], rat_tau,
             "ON trend" if tau_on_trend else "OFF trend",
             TAU_TREND_BAR, TAU_TREND_BAR, tr_d12,
             r_star["d12"], rat_d12,
             "OFF trend" if d12_off_trend else "on trend"))
    print("    weight test: w_soft(kz21)/neighborhood-median = "
          "%.3e vs collapse bar %.1f" % (rat_w, W_COLLAPSE_FAC))
    if rat_w < W_COLLAPSE_FAC and tau_on_trend:
        cause = "COORDINATE-ARTIFACT"
    elif rat_w >= W_COLLAPSE_FAC and d12_off_trend:
        cause = "ARITHMETIC"
    else:
        cause = "MIXED"
    check("K4.1 typed cause: %s (frozen rules: weight < %.1f x "
          "neighbor median & tau on trend -> COORDINATE-"
          "ARTIFACT; weight normal & d_12 off trend -> "
          "ARITHMETIC; else MIXED)" % (cause, W_COLLAPSE_FAC),
          True)
    cs2 = np.array([r["c"] for r in oth])
    hs2 = np.array([r["h"] for r in oth], float)
    mn2, q12_, q22, q32, mx2 = quart_row(cs2)
    spread2 = mx2 / mn2
    _, b_c2 = ols_ab(np.log(hs2), np.log(cs2))
    tied2 = (spread2 <= CSPREAD_BAR and abs(b_c2) <= CSLOPE_BAR)
    mode = ("SENSITIVITY (diagnosis COORDINATE-ARTIFACT: the "
            "outlier is a coordinate, not an arithmetic, "
            "statement)" if cause == "COORDINATE-ARTIFACT"
            else "descriptive only (diagnosis %s)" % cause)
    print("\n    THE CORRECTED LADDER (kz 21 excluded, 36 rungs;"
          " %s):" % mode)
    print("    c quartiles: min %.3f q25 %.3f med %.3f q75 %.3f"
          " max %.3f" % (mn2, q12_, q22, q32, mx2))
    print("    corrected spread %.2f (bar %.0f) | corrected "
          "slope %+.3f (bar %.1f) -> SOFTFLAG would type %s"
          % (spread2, CSPREAD_BAR, b_c2, CSLOPE_BAR,
             "TAU-TIED" if tied2 else "UNTIED"))
    check("K4.2 RE-FIT: spread %.2f -> %.2f, slope %+.3f -> "
          "%+.3f; SOFTFLAG-%s without kz 21 (%s)"
          % (spread, spread2, b_c, b_c2,
             "TIED" if tied2 else "UNTIED",
             "SENSITIVITY" if cause == "COORDINATE-ARTIFACT"
             else "descriptive"), True)

    # ------------------------------------------------------------ C
    section("C -- controls (kz %d): the value chain must break "
            "off the truth comb; pipeline persists" % CTRL_KZ)
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
            rc = anatomy(CTRL_KZ, need_full=True, **kw)
        except (np.linalg.LinAlgError, AssertionError):
            rc = None
        if not isinstance(rc, dict):
            print("    %-8s: chain dies (%r) -> FIRES (frame "
                  "death; pipeline story over)" % (nmc, rc))
            continue
        tau12c = None
        idc = None
        if rc.get("full") and "CJ" in rc:
            win_attrs(rc)
            tau12c = rc["tau12"]
            idc = rc["dev_inv"]
        fired = (rc["negA"] > 0
                 or (tau12c is not None and tau12c <= 0.0))
        ok_c &= fired
        print("    %-8s: neg(A_full) %d | tau_12 %s | identity "
              "d_12 == 1/(A^-1)_{12,12} rel dev %s (ALGEBRA "
              "persists; the VALUE breaks) -> %s"
              % (nmc, rc["negA"],
                 ("%+.3e" % tau12c) if tau12c is not None
                 else "n/a (window not full)",
                 ("%.1e" % idc) if idc is not None else "n/a",
                 "FIRES" if fired else "SILENT"))
    check("C1 CONTROLS FIRE (frame death or neg(A) > 0 or "
          "tau_12 <= 0; pipeline persists)", ok_c, kill="KC")

    return finish(dict(cause=cause, spread=spread,
                       spread2=spread2, b_c2=b_c2, tied2=tied2,
                       w21=r_star["w_soft"], wmed=w_med_nb,
                       c21=r_star["c"]))


def finish(labels):
    section("V -- FROZEN VERDICT")
    n_pass = sum(1 for _n, okk in CHECKS if okk)
    n_tot = len(CHECKS)
    if KILLS:
        VERDICT = {"KP": "PIPELINE-BROKEN",
                   "KW": "WARD-BROKEN",
                   "KC": "CONTROL-DEAD"}[KILLS[0]]
        print("\n  VERDICT: %s" % VERDICT)
    else:
        VERDICT = "KZ21-DIAGNOSED (%(cause)s)" % labels
        print("\n  VERDICT: %s" % VERDICT)
        print("  (c(kz21) = %(c21).1f; w_soft(kz21) = %(w21).3e "
              "vs neighborhood median %(wmed).3e; spread "
              "%(spread).2f -> %(spread2).2f without kz 21, "
              "slope %(b_c2)+.3f -> SOFTFLAG-%(t)s)"
              % dict(labels,
                     t="TIED" if labels["tied2"] else "UNTIED"))
    print("""
  HONEST FRAME (as frozen): single-rung forensics on the finite
  37-rung c-ladder; the identity chain is exact warded
  bookkeeping; the re-fit is a SENSITIVITY statement about the
  finite ladder, NOT a repair of the round-52 SOFTFLAG typing
  and NOT an asymptotic claim.  The round-52 raw numbers stand
  unchanged.  NO RH claim.  No marker moves.""")
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed"
          % (time.time() - T0, n_tot, n_tot - n_pass))
    return 0 if n_pass == n_tot else 1


if __name__ == "__main__":
    raise SystemExit(main())
