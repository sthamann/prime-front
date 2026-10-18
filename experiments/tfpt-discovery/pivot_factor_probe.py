#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""pivot_factor_probe -- PRIME.PORT.PIVOTFACTOR.01
(EXPLORATION ONLY, experiments/; round 51, reviewer priority 2:
the pivot factorization of PD inheritance -- do the 12 LDL^T
pivots of A_h = I - C_h factor rung-to-rung as d_{k,h+1} =
d_{k,h} (1 + mu_{k,h}) with every 1 + mu_{k,h} > 0 on truth?
Potentially the SHORTEST real induction of the program.
2026-08-09.)

THE ALGEBRA (frozen; elementary and exact).  For symmetric A
with nonvanishing leading principal minors tau^(k), the
unpivoted LDL^T factorization exists and its pivots are the
minor quotients
    d_k = tau^(k) / tau^(k-1),        tau^(0) := 1.
Between consecutive rungs the pivot ratio is therefore
    r_{k,h} := d_{k,h+1} / d_{k,h}
             = ( tau^(k)_{h+1} tau^(k-1)_h )
               / ( tau^(k)_h tau^(k-1)_{h+1} )
             = Q_k / Q_{k-1},
    Q_k := tau^(k)_{h+1} / tau^(k)_h    (leading-minor quotient,
                                         Q_0 := 1),
so with mu_{k,h} := r_{k,h} - 1 the factorization
    d_{k,h+1} = d_{k,h} (1 + mu_{k,h})
is an IDENTITY (warded, never the content).  The CONTENT is the
sign: since Q_k = prod_{j<=k} r_j,
    1 + mu_{k,h} > 0 for ALL k   <=>   Q_k > 0 for ALL k
(the FLAG QUOTIENT CHAIN), and then d > 0 and r > 0 imply
d' > 0 for every k SIMULTANEOUSLY -- PD inheritance by pure
algebra, no norm bound, no spectral gauge.  THE PIVOT INDUCTION
(P5, statement): base d_{k,H0} > 0 at the first rung (v884 /
v887 certify A = I - C PD at the base -- declared input, not
re-run) + Q_{k,h} > 0 for all k on all steps h  =>  d_{k,h} > 0
on the whole ladder.  Its finite shadow is the P2 census; the
single open inequality is min_k Q_{k,h} > 0.  This is the
per-flag strengthening of the round-CVII scalar Q_12 > 0
(tau_mobius_factor: truth Q_12 > 0 on 31/31; smooth-mass world
Q_12 < 0 on 16/28).

THE LADDER (frozen, factor_avoidance_euler verbatim): all
frame-A zones (core.frame_a_zones()) with h <= 900, sorted by
(h, kz); consecutive FULL-WINDOW pairs (both rungs carry all 12
indices of J = {2, 4, ..., 24}; typed skips counted); truth +
smooth-mass world (B1 LATTICE-SMOOTH masses m_n = 2 e^{u_n/2}
du_n, midpoint cells, lattice_parametrix verbatim);
Epstein/scramble frame status reported (C1).  v563 READ-ONLY.

FROZEN PROTOCOL (2026-08-09; all bars frozen before the run):

 P1  THE PIVOT LADDERS: per truth full-window rung the 12
     unpivoted-LDL^T pivots d_{k,h} of A_h = I - C_h (own
     factorization routine).  Ward W1 (kill -> WARD-BROKEN):
     d_{k,h} == tau^(k)_h / tau^(k-1)_h against the hirota-
     probe minor ladder (np.linalg.det of the nested leading
     sections, the port_tau_hirota object) -- scaled deviation
     |d_ldl - d_minor| / max(|d_ldl|, |d_minor|, 1e-300)
     <= 1e-10 on every rung and every k.  Pivot sign census
     printed (hirota reproduction: all 12 pivots positive on
     37/37 rungs <=> MINORS-POSITIVE).  Per step the ratios
     r_{k,h} = d_{k,h+1} / d_{k,h}; the 12 ratio ladders
     printed compactly (min / q25 / med / q75 / max per k over
     the truth steps).

 P2  THE IDENTITY + THE FLAG CENSUS (the new content): per
     truth step and per k, Q_k from slogdet of the leading
     k x k sections (sign * exp(logdet difference); numerically
     independent route).  Ward W2 (kill -> WARD-BROKEN): the
     EXACT identity r_{k,h} = Q_k / Q_{k-1} -- scaled deviation
     <= 1e-9 on every step and every k.  CENSUS (typed, never
     kills): FLAG-POSITIVE iff Q_{k,h} > 0 for EVERY k = 1..12
     on EVERY truth step (then the pivot induction closes over
     the measured ladder); else FLAG-VIOLATED with the (step,
     k) census.  Per-k margins printed: min_h Q_{k,h} and
     quartiles.

 P3  THE SMOOTH CONTRAST: the same flag census on the smooth-
     mass world.  Reproduction ward A0 (kill -> WARD-BROKEN):
     truth pairs == 31, smooth pairs == 28, truth Q_12 > 0 on
     31/31, smooth Q_12 < 0 on exactly 16/28 (tau_mobius /
     factor_avoidance printed ledgers).  At every smooth flag-
     crossing step the CROSSING DEPTH PROFILE: the violated
     flag set {k : Q_k <= 0}, its minimal element (does the
     violation enter at the soft flag k = 12 or in the bulk?),
     the census over steps printed.  Truth-vs-smooth contrast:
     min_k min_h Q_{k,h} per world.

 P4  THE PER-PRIME QUESTION (report only): at the 3 frozen
     MEDIUM truth steps (the middle three of the truth full-
     window step list sorted by h), the LEAVE-ONE-PRIME-OUT
     response of the pivot ratios: for each of the NP_TOP = 6
     largest in-window-mass base primes p (atoms grouped by own
     trial division, v882 own-sieve precedent; every atom must
     parse as a prime power -- ward, kill -> WARD-BROKEN),
     rebuild BOTH rungs without p's full atom group (deployed
     builder, comb override, truth masses) and form the pivot-
     ratio response R_p = max_k |r^{-p}_{k} / r_{k} - 1|.
     Frozen reading bars (round-50 finding of frame leverage is
     the declared prior): step scale s0 = max_k |r_{k} - 1|;
     PIVOT-GRAIN-NONDECOMPOSITIONAL iff sum_p R_p > 10 * s0
     (the responses are frame leverage, not increment grain);
     PIVOT-GRAIN-UNDERSAMPLED iff < 3 leave-outs survive
     (LEAVEOUT-DEAD typed, counted); else the share reading
     (top share > 0.8 coherent / < 0.5 diffuse).  If
     nondecompositional on the modal step, SAY SO and close the
     per-prime reading for pivots too.

 P5  THE INDUCTION STATEMENT (print): base + flag chain =>
     ladder positivity (the algebra above); its finite shadow
     is the P2 census.  The open inequality min_k Q_{k,h} > 0
     printed as a ladder (per step: min_k Q_k and argmin k)
     with the margin trend (median of min_k Q_k, first half vs
     second half of the steps in h-order).

 C   CONTROLS: (C2, PRIMARY, kill -> CONTROL-DEAD) the smooth-
     mass world must show flag violations (the detector must
     fire on the control world; anchored numerically in A0).
     (C1, kz 9, must fire, kill -> CONTROL-DEAD) Epstein
     (lambda_eps recursion comb) + scramble (seed 1): the
     compressed frame must die (exterior supercritical OR
     lam(C_J) > 1 OR window unavailable); channel reported.

 W   PIPELINE WARDS (kill -> PIPELINE-BROKEN): W0 >= 30 truth
     rungs; W0b the atom prefix law exact; W0c truth full-
     window rung census == 37 (hirota census).

KILLS: KP pipeline ward breaks -> PIPELINE-BROKEN; KW ward
breaks (W1 pivot==minor / W2 identity / A0 reproduction / P4
prime parse) -> WARD-BROKEN; KC controls silent ->
CONTROL-DEAD.  P2/P3 censuses and P4 readings are TYPED /
reported, never kill.

VERDICT (frozen enum): PIVOTFACTOR-MEASURED (+ typed:
FLAG-POSITIVE / FLAG-VIOLATED(k-profile) /
FLAG-UNDECIDABLE(ratio) per world (SPEC v2 (ii)), the P4
grain label) / PIPELINE-BROKEN / WARD-BROKEN / CONTROL-DEAD.

SPEC v2 (2026-08-09, after runs 1-2; fail-first preserved --
every run-1/2 raw number stands and is reprinted unchanged; no
bar was moved to rescue a failing measurement):

 (i)   DISPLAY ONLY: the P2/P5 margin prints moved from fixed
       (%.4f) to scientific notation after run 1 printed the
       load-bearing ladder minimum (min_k min_h Q =
       2.059e-14 > 0) as "0.0000".  No bar, no object changed.

 (ii)  SIGN DECIDABILITY PRECONDITION added after run 2: the
       ladder min Q_12 = 2.1e-14 is a quotient of determinants
       14 orders apart, so the census sign is trustworthy only
       if every participating minor's sign sits above the
       floating-point noise floor.  New diagnostic (printed +
       typing precondition, frozen): per full-window rung,
       lam_min(A_h) from eigh (backward stable; absolute
       eigenvalue error ~ eps ||A||) against the floor
       NW * eps * lam_max(A_h); by Cauchy interlacing
       lam_min(A[:k,:k]) >= lam_min(A) for every leading
       section, so ONE floor per rung covers all 12 flags.
       The truth census is typed FLAG-POSITIVE only if the
       minimal decidability ratio over the truth rungs
       >= DECIDE_BAR = 1e3; else FLAG-UNDECIDABLE(ratio).
       (Smooth world: A indefinite, interlacing gives no
       |lambda| floor per section -- the smooth min |lambda|
       ratio is REPORTED, the smooth typing keeps its census.)
       Measured out-of-band before freezing: worst truth ratio
       6.4e9 -- decisively decidable.

HONEST FRAME: the factorization d' = d (1 + mu) is an identity
-- warded bookkeeping, zero content.  The content is the SIGN
census of the flag quotient chain Q_k on the measured ladder,
and the census is FINITE: it certifies the deployed rungs, it
does NOT prove the open inequality min_k Q_{k,h} > 0 beyond
them.  NO RH claim.  No marker moves.

FIREWALL: no zeros, no prime oracles (AST scan; banned ids
zetazero / nzeros / primerange / isprime / primepi / nextprime /
prevprime); the P4 grouping uses an OWN trial-division
smallest-prime-factor routine (v882 own-sieve precedent);
v563 READ-ONLY; RNG only inside the declared scramble control;
stdout only.

Sources (read-only): v563_paper2_readouts (build_window,
atom_lags_at, arch_lags, U_ALL / MU_ALL prefix law -- verbatim);
window compression + ladder scope + smooth-mass world verbatim
from factor_avoidance_euler_probe.py (PRIME.PORT.FACTORAVOID.01)
via tau_mobius_factor_probe / port_schur_cocycle_probe /
lattice_parametrix_probe; port_tau_hirota_probe
(PRIME.PORT.HIROTA.01: the minor ladder object + the 37-rung
census + MINORS-POSITIVE, the P1 ward anchor); v884/v887
(base-rung PD certificate -- declared input, not re-run).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/pivot_factor_probe.py
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
MIN_RUNGS = 30
N_FULLWIN_FROZEN = 37       # hirota-probe truth census
MIN_COMMON_J = 8
PIV_WARD = 1e-10            # W1 pivot == minor quotient (kill)
ID_WARD = 1e-9              # W2 r_k == Q_k/Q_{k-1} (kill)
NP_TOP = 6                  # P4 leave-out primes
MEDIUM_N = 3                # P4 medium truth steps
LEV_BAR = 10.0              # P4 leverage bar (vs step scale)
MIN_LO_ALIVE = 3            # P4 undersampling bar
GRAIN_DIFFUSE_BAR = 0.5     # P4 share bars (where valid)
GRAIN_COHERENT_BAR = 0.8
DECIDE_BAR = 1e3            # SPEC v2 (ii) sign decidability
CTRL_KZ = 9
BANNED_IDS = ("zetazero", "nzeros", "primerange", "isprime",
              "primepi", "nextprime", "prevprime")

# A0 reproduction anchors (tau_mobius_factor /
# factor_avoidance_euler printed ledgers, re-verified there)
REF_N_TRUTH_PAIRS = 31
REF_N_SMOOTH_PAIRS = 28
REF_TRUTH_Q12_NEG = 0
REF_SMOOTH_Q12_NEG = 16

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


# --------- pipeline, verbatim from factor_avoidance_euler_probe
def grid_density(c):
    c = np.asarray(c, float)
    a = np.concatenate([c, c[-2:0:-1]])
    d = np.fft.fft(a)
    assert float(np.max(np.abs(d.imag))) <= 1e-9 * max(
        1.0, float(np.max(np.abs(d.real))))
    return d.real


def lambda_eps(N):
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


def build_rung(kz, scramble_seed=None, comb=None, rr_cache=None):
    rr = (rr_cache if rr_cache is not None
          else core.build_window(kz, scramble_seed=scramble_seed))
    h, M, D, alpha = rr["h"], rr["M"], rr["D"], rr["alpha"]
    uu = np.asarray(rr["uu"], float)
    mm = 2.0 * np.asarray(rr["lam"], float)
    if comb is not None:
        uu, mm = comb
    c_at, _ = core.atom_lags_at(alpha, M, uu, mm)
    c_ar = np.asarray(core.arch_lags(M, D), float)
    d = grid_density(c_ar + c_at)
    return dict(d=d, L=2 * M - 2, D=D, alpha=alpha, h=h)


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


def rung_win(kz, scramble_seed=None, comb=None, rr_cache=None):
    """One rung -> 12x12 window compression (factor_avoidance
    verbatim)."""
    b = build_rung(kz, scramble_seed=scramble_seed, comb=comb,
                   rr_cache=rr_cache)
    h, L = b["h"], b["L"]
    if h > H_DEEP_MAX:
        return "TOO-DEEP"
    xs, ws, _ = folded_measure(b["d"], L, +1.0)
    ys, vs, uf_n = folded_measure(b["d"], L, -1.0)
    al, be, m0, steps = lanczos_chain(xs, ws, h + 1)
    if steps < h + 1 or np.any(be <= 0):
        return None
    Pn = eval_chain(al, be, m0, ys, h)
    E = np.sqrt(vs)[:, None] * (Pn @ Pn.T) * np.sqrt(vs)[None, :]
    E = 0.5 * (E + E.T)
    out = dict(kz=kz, h=h, alpha=b["alpha"],
               lamE=float(np.linalg.eigvalsh(E)[-1]))
    idx = {int(j): k for k, j in enumerate(uf_n)}
    jav = [j for j in JWIN if j in idx]
    out["full"] = (len(jav) == len(JWIN))
    if len(jav) >= MIN_COMMON_J:
        iw = [idx[j] for j in jav]
        io = [k for k in range(E.shape[0]) if k not in set(iw)]
        Eo = E[np.ix_(io, io)]
        IO = np.eye(len(io)) - Eo
        CJ = (E[np.ix_(iw, iw)]
              + E[np.ix_(iw, io)] @ np.linalg.solve(
                  IO, E[np.ix_(io, iw)]))
        CJ = 0.5 * (CJ + CJ.T)
        out["CJ"] = CJ
        out["jav"] = jav
        out["lamO"] = float(np.linalg.eigvalsh(Eo)[-1])
        out["lamC"] = float(np.linalg.eigvalsh(CJ)[-1])
    return out


def eps_comb(kz):
    rr = core.build_window(kz)
    N_E = int(math.floor(math.exp(2.0 * rr["alpha"]))) + 1
    lamE_ = lambda_eps(N_E)
    nn = np.nonzero(np.abs(lamE_) > 1e-12)[0]
    return (np.log(nn.astype(float)),
            2.0 * lamE_[nn] / np.sqrt(nn.astype(float)))


# ------------------------------------------- smooth-mass world (B1)
def cell_widths(uu):
    du = np.zeros(len(uu))
    du[1:-1] = 0.5 * (uu[2:] - uu[:-2])
    du[0] = uu[1] - uu[0]
    du[-1] = uu[-1] - uu[-2]
    return du


def smooth_masses(uu):
    """B1 LATTICE-SMOOTH masses m_n = 2 e^{u_n/2} du_n (verbatim)."""
    return 2.0 * np.exp(np.asarray(uu, float) / 2.0) \
        * cell_widths(np.asarray(uu, float))


# ------------------------------------------- own prime machinery
def spf_own(n):
    """Own trial-division smallest prime factor (v882 own-sieve
    precedent; no oracle imports)."""
    if n % 2 == 0:
        return 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return d
        d += 2
    return n


def prime_power_base(u):
    """Base prime p of the atom at position u = log(p^k); None if
    the recovered integer is not a prime power (ward)."""
    n = int(round(math.exp(u)))
    if n < 2 or abs(math.exp(u) - n) > 1e-6 * n:
        return None
    p = spf_own(n)
    m = n
    while m % p == 0:
        m //= p
    return p if m == 1 else None


def comb_of(idx_set, world):
    """Comb arrays for an index set into U_ALL (truth = deployed
    masses; smooth = B1 masses on the set's own lattice)."""
    ii = np.array(sorted(idx_set), dtype=int)
    uu = np.asarray(core.U_ALL, float)[ii]
    if world == "truth":
        return uu, np.asarray(core.MU_ALL, float)[ii]
    return uu, smooth_masses(uu)


def death_channel(hy):
    """Classify a failed rebuild."""
    if not isinstance(hy, dict):
        return "CHAIN-DEATH"
    if "CJ" not in hy:
        return "WINDOW-LOST"
    if not hy.get("full"):
        return "PARTIAL-WINDOW"
    return None


# ------------------------------------------- pivot machinery (new)
def ldl_pivots(A):
    """Unpivoted LDL^T pivots of symmetric A (own routine); None
    on an exactly-zero pivot."""
    n = A.shape[0]
    L = np.zeros((n, n))
    d = np.zeros(n)
    for j in range(n):
        d[j] = A[j, j] - float(np.sum(L[j, :j] ** 2 * d[:j]))
        if d[j] == 0.0:
            return None
        L[j, j] = 1.0
        for i in range(j + 1, n):
            L[i, j] = (A[i, j] - float(
                np.sum(L[i, :j] * L[j, :j] * d[:j]))) / d[j]
    return d


def lead_minors(A):
    """tau^(k), k = 0..NW (tau^(0) = 1), np.linalg.det route --
    the port_tau_hirota minor-ladder object."""
    t = [1.0]
    for k in range(1, NW + 1):
        t.append(float(np.linalg.det(A[:k, :k])))
    return np.array(t)


def lead_slogdets(A):
    """(sign, logdet) of the leading k x k sections, k = 0..NW
    (numerically independent route for the Q_k quotients)."""
    out = [(1.0, 0.0)]
    for k in range(1, NW + 1):
        sg, ld = np.linalg.slogdet(A[:k, :k])
        out.append((float(sg), float(ld)))
    return out


def rung_pivots(r):
    """Attach A = I - C_J, minors, pivots, slogdets to a rung."""
    A = np.eye(NW) - r["CJ"]
    taus = lead_minors(A)
    dmin = taus[1:] / taus[:-1]         # minor-quotient pivots
    dldl = ldl_pivots(A)
    dev = (float(np.max(np.abs(dldl - dmin)
                        / np.maximum(np.maximum(np.abs(dldl),
                                                np.abs(dmin)),
                                     1e-300)))
           if dldl is not None else float("inf"))
    ew = np.linalg.eigvalsh(A)
    r["A"] = A
    r["taus"] = taus
    r["piv"] = dmin
    r["piv_dev"] = dev
    r["sld"] = lead_slogdets(A)
    r["lam_min"] = float(ew[0])
    r["lam_absmin"] = float(np.min(np.abs(ew)))
    r["lam_max"] = float(ew[-1])
    return r


def flag_rows(rungs):
    """Consecutive full-window pairs -> pivot ratios r_k, flag
    quotients Q_k, identity deviation, violated-flag set."""
    rows = []
    n_skip = 0
    for t, (ra, rb) in enumerate(zip(rungs[:-1], rungs[1:])):
        if not (ra.get("full") and rb.get("full")):
            n_skip += 1
            continue
        rk = rb["piv"] / ra["piv"]
        Q = np.zeros(NW + 1)
        Q[0] = 1.0
        for k in range(1, NW + 1):
            sga, lda = ra["sld"][k]
            sgb, ldb = rb["sld"][k]
            Q[k] = sga * sgb * math.exp(ldb - lda)
        dev = 0.0
        for k in range(1, NW + 1):
            qq = Q[k] / Q[k - 1] if Q[k - 1] != 0.0 else float(
                "inf")
            dev = max(dev, abs(rk[k - 1] - qq)
                      / max(abs(rk[k - 1]), abs(qq), 1e-300))
        viol = [k for k in range(1, NW + 1) if Q[k] <= 0.0]
        rows.append(dict(t=t, ra=ra, rb=rb, ha=ra["h"],
                         hb=rb["h"], kza=ra["kz"], kzb=rb["kz"],
                         rk=rk, Q=Q[1:], id_dev=dev, viol=viol,
                         minQ=float(np.min(Q[1:])),
                         argminQ=int(np.argmin(Q[1:])) + 1))
    return rows, n_skip


def quart_row(v):
    v = np.asarray(v, float)
    q = np.percentile(v, [25, 50, 75])
    return (float(np.min(v)), q[0], q[1], q[2],
            float(np.max(v)))


def main():
    section("PRIME.PORT.PIVOTFACTOR.01 -- the pivot factorization "
            "d_{k,h+1} = d_{k,h}(1 + mu_{k,h}) of PD inheritance "
            "(EXPLORATION ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s"
          % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
    print("    NO RH claim; no marker moves.")
    print("\nS0 -- firewall")
    check("S0.1 AST firewall clean (own trial division, no "
          "oracles)", not ast_scan(BANNED_IDS))

    # ------------------------------------------------------------ W
    section("W -- build the truth + smooth-mass ladders (all "
            "frame-A zones, h <= %d)" % H_DEEP_MAX)
    rungs, srungs = [], []
    rrs = {}
    n_smooth_dead = 0
    for kz in core.frame_a_zones():
        rr = core.build_window(kz)
        r = rung_win(kz, rr_cache=rr)
        if not isinstance(r, dict):
            continue
        rrs[kz] = rr
        rungs.append(r)
        uu = np.asarray(rr["uu"], float)
        rs = rung_win(kz, comb=(uu, smooth_masses(uu)),
                      rr_cache=rr)
        if isinstance(rs, dict):
            srungs.append(rs)
        else:
            n_smooth_dead += 1
    rungs.sort(key=lambda r: (r["h"], r["kz"]))
    srungs.sort(key=lambda r: (r["h"], r["kz"]))
    print("    truth: %d rungs, h %d .. %d | smooth-mass: %d "
          "rungs, %d chain/window deaths"
          % (len(rungs), rungs[0]["h"], rungs[-1]["h"],
             len(srungs), n_smooth_dead))
    pref_dev = max(float(np.max(np.abs(
        2.0 * np.asarray(rr["lam"], float)
        - np.asarray(core.MU_ALL, float)[:int(rr["n_atom"])])))
        for rr in rrs.values())
    check("W0 >= %d truth rungs built" % MIN_RUNGS,
          len(rungs) >= MIN_RUNGS, "%d rungs" % len(rungs),
          kill="KP")
    check("W0b atom prefix law exact (max |mm - MU_ALL prefix| "
          "%.1e == 0)" % pref_dev, pref_dev == 0.0, kill="KP")
    n_full_t = sum(1 for r in rungs if r.get("full"))
    check("W0c truth full-window census %d == %d (hirota frozen)"
          % (n_full_t, N_FULLWIN_FROZEN),
          n_full_t == N_FULLWIN_FROZEN, kill="KP")

    # ------------------------------------------------------------ P1
    section("P1 -- THE PIVOT LADDERS: unpivoted LDL^T pivots "
            "d_{k,h} of A_h = I - C_h + ward vs the minor "
            "quotients (truth)")
    w1_max = 0.0
    n_piv_neg = 0
    for r in rungs:
        if not r.get("full"):
            continue
        rung_pivots(r)
        w1_max = max(w1_max, r["piv_dev"])
        n_piv_neg += int(np.sum(r["piv"] <= 0.0))
    for r in srungs:
        if r.get("full"):
            rung_pivots(r)
    s_dev = max((r["piv_dev"] for r in srungs if r.get("full")),
                default=0.0)
    check("W1 PIVOT == MINOR QUOTIENT on every truth full-window "
          "rung and every k: max scaled dev %.1e <= %.0e"
          % (w1_max, PIV_WARD), w1_max <= PIV_WARD, kill="KW")
    print("    (smooth-world LDL vs minors, reported: max dev "
          "%.1e -- indefinite unpivoted LDL, no bar)" % s_dev)
    check("P1.0 pivot sign census (hirota MINORS-POSITIVE "
          "reproduction): nonpositive pivots %d == 0 on %d/%d "
          "rungs" % (n_piv_neg, n_full_t, n_full_t),
          n_piv_neg == 0)

    trows, n_skip_t = flag_rows(rungs)
    srows, n_skip_s = flag_rows(srungs)
    print("\n    truth steps: %d full-window pairs (%d typed "
          "skips) | smooth steps: %d (%d skips)"
          % (len(trows), n_skip_t, len(srows), n_skip_s))
    print("\n    THE 12 RATIO LADDERS r_{k,h} = d_{k,h+1} / "
          "d_{k,h} (truth, %d steps):" % len(trows))
    print("    %-3s %-9s %-9s %-9s %-9s %-9s %s"
          % ("k", "min", "q25", "med", "q75", "max", "min>0"))
    for k in range(NW):
        vv = [row["rk"][k] for row in trows]
        mn, q1, q2, q3, mx = quart_row(vv)
        print("    %-3d %-9.4f %-9.4f %-9.4f %-9.4f %-9.4f %s"
              % (k + 1, mn, q1, q2, q3, mx, mn > 0.0))

    # ------------------------------------------------------------ P2
    section("P2 -- THE IDENTITY r_k = Q_k / Q_{k-1} (warded) + "
            "THE FLAG QUOTIENT CENSUS Q_k > 0 (truth)")
    id_max_t = max(row["id_dev"] for row in trows)
    id_max_s = max(row["id_dev"] for row in srows)
    check("W2 IDENTITY r_{k,h} == Q_k / Q_{k-1} on every truth "
          "step and every k: max scaled dev %.1e <= %.0e"
          % (id_max_t, ID_WARD), id_max_t <= ID_WARD, kill="KW")
    print("    (smooth identity dev, same algebra: max %.1e -- "
          "reported)" % id_max_s)
    print("\n    per-k flag-quotient margins over the %d truth "
          "steps:" % len(trows))
    print("    %-3s %-11s %-11s %-11s %-11s %s"
          % ("k", "min Q_k", "q25", "med", "q75", "min>0"))
    for k in range(NW):
        vv = [row["Q"][k] for row in trows]
        mn, q1, q2, q3, _ = quart_row(vv)
        print("    %-3d %-11.3e %-11.3e %-11.3e %-11.3e %s"
              % (k + 1, mn, q1, q2, q3, mn > 0.0))
    eps = float(np.finfo(float).eps)
    dec_t = min(r["lam_min"] / (NW * eps * r["lam_max"])
                for r in rungs if r.get("full"))
    print("\n    SIGN DECIDABILITY (SPEC v2 (ii)): min over "
          "truth rungs of lam_min(A) / (12 eps lam_max(A)) = "
          "%.1e (bar %.0e; Cauchy interlacing covers all 12 "
          "flags per rung)" % (dec_t, DECIDE_BAR))
    t_viol = [(row["ha"], row["hb"], row["viol"])
              for row in trows if row["viol"]]
    if dec_t < DECIDE_BAR:
        flag_t = "FLAG-UNDECIDABLE(ratio=%.1e)" % dec_t
    elif not t_viol:
        flag_t = "FLAG-POSITIVE"
    else:
        flag_t = "FLAG-VIOLATED(%s)" % t_viol
    minQ_t = float(np.min([row["minQ"] for row in trows]))
    check("P2.s truth flag census typed %s -- Q_k > 0 for all "
          "k = 1..12 on %d/%d steps; min_k min_h Q = %.3e"
          % (flag_t, len(trows) - len(t_viol), len(trows),
             minQ_t), True)

    # ------------------------------------------------------------ P3
    section("P3 -- THE SMOOTH CONTRAST: the same flag census on "
            "the smooth-mass world + the crossing depth profile")
    n_q12neg_t = sum(1 for row in trows if row["Q"][NW - 1] < 0.0)
    n_q12neg_s = sum(1 for row in srows if row["Q"][NW - 1] < 0.0)
    check("A0 REPRODUCTION: truth pairs %d == %d, smooth pairs "
          "%d == %d, truth Q_12 < 0 on %d == %d, smooth Q_12 < 0 "
          "on %d == %d (predecessor ledgers)"
          % (len(trows), REF_N_TRUTH_PAIRS, len(srows),
             REF_N_SMOOTH_PAIRS, n_q12neg_t, REF_TRUTH_Q12_NEG,
             n_q12neg_s, REF_SMOOTH_Q12_NEG),
          len(trows) == REF_N_TRUTH_PAIRS
          and len(srows) == REF_N_SMOOTH_PAIRS
          and n_q12neg_t == REF_TRUTH_Q12_NEG
          and n_q12neg_s == REF_SMOOTH_Q12_NEG, kill="KW")
    s_cross = [row for row in srows if row["viol"]]
    print("\n    smooth flag-crossing steps: %d/%d"
          % (len(s_cross), len(srows)))
    print("    step        min_k Q_k  argmin  violated flags "
          "{k : Q_k <= 0}")
    for row in s_cross:
        print("    h %3d->%3d  %+9.3e  k=%-4d %s"
              % (row["ha"], row["hb"], row["minQ"],
                 row["argminQ"], row["viol"]))
    depth = {}
    for row in s_cross:
        kmin = min(row["viol"])
        depth[kmin] = depth.get(kmin, 0) + 1
    n_soft = sum(1 for row in s_cross if row["viol"] == [NW])
    print("\n    CROSSING DEPTH PROFILE (minimal violated flag "
          "per step): %s"
          % (sorted(depth.items()) if depth else "none"))
    print("    soft-flag-only steps (violated set == {12}): "
          "%d/%d -- the violation %s"
          % (n_soft, len(s_cross),
             "enters at the soft flag k = 12 only"
             if n_soft == len(s_cross) else
             "reaches the BULK flags (k < 12)"))
    dec_s = min(r["lam_absmin"] / (NW * eps * r["lam_max"])
                for r in srungs if r.get("full"))
    print("\n    (smooth sign decidability, REPORTED per SPEC "
          "v2 (ii): min |lambda|(A) / (12 eps lam_max) = %.1e "
          "-- no interlacing floor on indefinite A)" % dec_s)
    minQ_s = (float(np.min([row["minQ"] for row in srows]))
              if srows else float("nan"))
    flag_s = ("FLAG-POSITIVE" if not s_cross else
              "FLAG-VIOLATED(depth=%s)" % sorted(depth.items()))
    check("P3.s smooth flag census typed %s -- %d/%d crossing "
          "steps" % (flag_s, len(s_cross), len(srows)), True)
    print("\n    TRUTH-vs-SMOOTH CONTRAST: min_k min_h Q_k = "
          "%+.3e (truth, positive) vs %+.3e (smooth)"
          % (minQ_t, minQ_s))

    # ------------------------------------------------------------ P4
    section("P4 -- THE PER-PRIME QUESTION (report only): leave-"
            "one-prime-out response of the pivot ratios at %d "
            "frozen medium truth steps" % MEDIUM_N)
    print("    (declared prior: round-50 factor_avoidance found "
          "leave-out responses to be FRAME LEVERAGE, not")
    print("    increment grain -- sum_p rho_p ~ 1e4 vs rho_tot "
          "~ 1-4.  Frozen bar here: NONDECOMPOSITIONAL iff")
    print("    sum_p R_p > %.0f x step scale s0 = max_k "
          "|r_k - 1|.)" % LEV_BAR)
    i0 = (len(trows) - MEDIUM_N) // 2
    parse_ok = True
    grain = []
    for row in trows[i0:i0 + MEDIUM_N]:
        ka = int(rrs[row["kza"]]["n_atom"])
        kb = int(rrs[row["kzb"]]["n_atom"])
        ku = max(ka, kb)
        groups = {}
        for i in range(ku):
            p = prime_power_base(float(core.U_ALL[i]))
            if p is None:
                parse_ok = False
                continue
            groups.setdefault(p, []).append(i)
        masses = {p: float(np.sum(np.abs(
            np.asarray(core.MU_ALL, float)[g])))
            for p, g in groups.items()}
        order = sorted(groups, key=lambda p: -masses[p])[:NP_TOP]
        s0 = float(np.max(np.abs(row["rk"] - 1.0)))
        print("\n  TRUTH h %d->%d (kz %d->%d; step scale s0 = "
              "max_k |r_k - 1| = %.4f)"
              % (row["ha"], row["hb"], row["kza"], row["kzb"],
                 s0))
        print("    p       n_pow  R_p = max_k |r^-p_k / r_k - 1|"
              "   sign flips")
        resp = []
        n_dead = 0
        for p in order:
            gset = set(groups[p])
            ca = rung_win(row["kza"],
                          comb=comb_of([i for i in range(ka)
                                        if i not in gset],
                                       "truth"),
                          rr_cache=rrs[row["kza"]])
            cb = rung_win(row["kzb"],
                          comb=comb_of([i for i in range(kb)
                                        if i not in gset],
                                       "truth"),
                          rr_cache=rrs[row["kzb"]])
            if (death_channel(ca) is not None
                    or death_channel(cb) is not None):
                n_dead += 1
                print("    %-7d LEAVEOUT-DEAD (a: %s, b: %s)"
                      % (p, death_channel(ca) or "ok",
                         death_channel(cb) or "ok"))
                continue
            rung_pivots(ca)
            rung_pivots(cb)
            rkp = cb["piv"] / ca["piv"]
            n_flip = int(np.sum((rkp > 0) != (row["rk"] > 0)))
            Rp = float(np.max(np.abs(rkp / row["rk"] - 1.0)))
            resp.append((p, Rp))
            print("    %-7d %4d   %-32.4f %d"
                  % (p, len(groups[p]), Rp, n_flip))
        if len(resp) < MIN_LO_ALIVE:
            gt = "PIVOT-GRAIN-UNDERSAMPLED"
        else:
            sum_R = sum(x[1] for x in resp)
            top = max(x[1] for x in resp)
            lev = sum_R / max(s0, 1e-300)
            if lev > LEV_BAR:
                gt = "PIVOT-GRAIN-NONDECOMPOSITIONAL"
            else:
                share = top / sum_R
                gt = ("PIVOT-GRAIN-DIFFUSE"
                      if share <= GRAIN_DIFFUSE_BAR
                      else "PIVOT-GRAIN-COHERENT"
                      if share >= GRAIN_COHERENT_BAR
                      else "PIVOT-GRAIN-INTERMEDIATE")
            print("    sum_p R_p = %.4f | s0 = %.4f | leverage "
                  "ratio %.1f (bar %.0f) | dead %d -> %s"
                  % (sum_R, s0, lev, LEV_BAR, n_dead, gt))
        grain.append(gt)
    check("P4.1 prime parse ward: every window atom is a prime "
          "power (own trial division)", parse_ok, kill="KW")
    gmodal = (max(set(grain), key=grain.count)
              if grain else "PIVOT-GRAIN-UNAVAILABLE")
    check("P4.s pivot grain typed (modal of %d steps): %s"
          % (len(grain), gmodal), True)
    if gmodal == "PIVOT-GRAIN-NONDECOMPOSITIONAL":
        print("""
    THE PER-PRIME READING IS CLOSED FOR PIVOTS TOO: exactly as
    in round 50, removing ONE prime moves the window operators
    (and hence every pivot ratio) by far more than the whole
    step does -- the leave-out response is FRAME LEVERAGE of
    the collective window re-test, not a per-prime
    decomposition of the flag increments mu_{k,h}.  The flag
    chain Q_k is a property of the collective comb; no
    single-prime channel carries it.""")

    # ------------------------------------------------------------ P5
    section("P5 -- THE PIVOT INDUCTION (statement + the open "
            "inequality's ladder)")
    print("""
    STATEMENT (algebra, no proof of the open part): base
    d_{k,H0} > 0 (v884/v887 certify A = I - C PD at the base
    rung -- declared input) + Q_{k,h} > 0 for all k = 1..12 on
    every step h  =>  d_{k,h} = d_{k,H0} prod_h (1 + mu_{k,h})
    > 0 for all k on the whole ladder -- PD inheritance by pure
    algebra.  The P2 census is the FINITE SHADOW of this
    induction on the measured ladder; the OPEN INEQUALITY is
    min_k Q_{k,h} > 0 beyond it.""")
    print("    the open inequality's ladder (truth, per step):")
    print("    %-12s %-11s %s" % ("step", "min_k Q_k", "argmin"))
    mins = []
    for row in trows:
        mins.append(row["minQ"])
        print("    h %3d->%3d   %-11.3e k=%d"
              % (row["ha"], row["hb"], row["minQ"],
                 row["argminQ"]))
    nh = len(mins) // 2
    m1 = float(np.median(mins[:nh]))
    m2 = float(np.median(mins[nh:]))
    print("\n    MARGIN TREND: median min_k Q_k = %.3e (first "
          "%d steps) vs %.3e (last %d) -- %s with depth; "
          "ladder min %.3e"
          % (m1, nh, m2, len(mins) - nh,
             "tightening" if m2 < m1 else "stable/widening",
             minQ_t))
    check("P5.1 induction shadow reported (min_k min_h Q = %.3e "
          "> 0: %s)" % (minQ_t, minQ_t > 0.0), True)

    # ------------------------------------------------------------ C
    section("C -- controls")
    print("  C2 -- smooth-mass world (PRIMARY): the flag "
          "detector must fire on the control world.")
    check("C2 smooth flag violations present (%d/%d crossing "
          "steps)" % (len(s_cross), len(srows)),
          len(s_cross) > 0, kill="KC")
    print("  C1 -- Epstein/scramble (kz %d, frame must die):"
          % CTRL_KZ)
    ok1 = True
    for nmc, kw in (("Epstein", dict(comb=eps_comb(CTRL_KZ))),
                    ("scramble", dict(scramble_seed=1))):
        try:
            rc = rung_win(CTRL_KZ, **kw)
        except (np.linalg.LinAlgError, AssertionError):
            rc = None
        if not isinstance(rc, dict):
            print("    %-8s: rung not built (%r) -> FRAME DIES"
                  % (nmc, rc))
            continue
        if "lamC" not in rc:
            print("    %-8s: window unavailable -> FRAME DIES"
                  % nmc)
            continue
        fired = (rc["lamO"] > 1.0) or (rc["lamC"] > 1.0)
        ok1 &= fired
        print("    %-8s: lam(out) %.3e | lam(C_J) %.3e -> fires "
              "via %s"
              % (nmc, rc["lamO"], rc["lamC"],
                 "EXTERIOR" if rc["lamO"] > 1.0 else
                 "WINDOW" if rc["lamC"] > 1.0 else "NOTHING"))
    check("C1 CONTROLS FIRE (frame death or supercriticality)",
          ok1, kill="KC")

    # ------------------------------------------------------------ V
    section("V -- FROZEN VERDICT")
    n_pass = sum(1 for _n, okk in CHECKS if okk)
    n_tot = len(CHECKS)
    if KILLS:
        VERDICT = {"KP": "PIPELINE-BROKEN", "KW": "WARD-BROKEN",
                   "KC": "CONTROL-DEAD"}[KILLS[0]]
        print("\n  VERDICT: %s" % VERDICT)
    else:
        VERDICT = ("PIVOTFACTOR-MEASURED / truth %s / smooth %s "
                   "/ %s" % (flag_t, flag_s, gmodal))
        print("\n  VERDICT: %s" % VERDICT)
        print("  (truth min_k min_h Q = %.3e > 0; smooth min "
              "%.3e; smooth crossings %d/%d)"
              % (minQ_t, minQ_s, len(s_cross), len(srows)))
    print("""
  HONEST FRAME (as frozen): the factorization d' = d (1 + mu)
  is an identity -- warded bookkeeping, zero content.  The
  content is the SIGN census of the flag quotient chain Q_k on
  the measured ladder; it is FINITE and certifies only the
  deployed rungs.  The open inequality min_k Q_{k,h} > 0 beyond
  the ladder is NOT proved here.  NO RH claim.  No marker
  moves.""")
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed"
          % (time.time() - T0, n_tot, n_tot - n_pass))
    return 0 if n_pass == n_tot else 1


if __name__ == "__main__":
    raise SystemExit(main())
