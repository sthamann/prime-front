#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""deepcore_anatomy_probe -- PRIME.PORT.DEEPCORE.01 (EXPLORATION
ONLY, experiments/; round 50, follow-up (c) of the Moebius kill
battery: dissect the surviving arithmetic remnant, 2026-08-09).

THE QUESTION (frozen): the round-48 Moebius firewall
(mobius_crossratio_firewall_probe, PRIME.PORT.MOEBIUS.
CRFIREWALL.01) killed the full-coverage cross-ratio invariance
(CR-DEAD) but its report-only DEEP-CORE sub-battery survived at
certificate level: the 8 DEEPEST common port nodes of consecutive
rungs carry cross-ratio coherence med ~ 4.3e-4 in the raw carrier
r = g/f -- fit-free and gauge-free -- while the smooth-mass world
(PNT-mean masses 2 e^{u/2} du on the true prime-power lattice)
loses it (~ 2.7e-2).  This probe dissects the remnant: WHICH
nodes, WHICH Lambda signal, WHAT structure carries it.

THE COMB (frozen, v563 verbatim): atoms at u_n = log n on the
prime powers n = p^k with masses 2 Lambda(n) / sqrt(n); a window
at zone kz covers u in (0, 2 alpha], alpha = U_ALL[kz].  The
carrier pairs (g_j, f_j) are the IIKS generators of the dressed
port commutator [Y, D_P] (port_schur_cocycle / iiks_gauge_firewall
extraction, SPEC v2, verbatim), in the frozen one-point SO(2)
extraction gauge (a chordal isometry: cross-ratios are exactly
gauge-free).  The ladder: all frame-A zones with h <= 900 sorted
by (h, kz); consecutive pairs (k = 1) with >= 8 common port alias
indices.

FROZEN PROTOCOL (2026-08-09, frozen + SHA-hashed before first
run; all bars frozen before the run):

 D1  NODE IDENTIFICATION: per k = 1 step print the 8 deepest
     common alias indices (the deep core) -- the census along the
     ladder; the alias frequency table; the modal deep-8 set and
     the fraction of steps whose deep core equals it exactly.
     TYPED: ALIAS-FIXED iff >= 90% of steps carry the identical
     modal set; ALIAS-DRIFTING otherwise.  Explicitly compared to
     the even set {2, 4, ..., 16}.  ANATOMY on three
     representative rungs (shallowest / middle / deepest): alias
     j, y_j, tau_j, and the Bessel-normal coordinate a_m =
     2 h^2 (1 - y_m) against pi^2 m^2 (christoffel H5
     cross-reference: on the folded grid y = cos(2 pi j / L),
     L ~ 4h, so alias j = 2m sits at a_m ~ pi^2 m^2 -- the port
     core).  TYPED (deepest rung): PORTCORE-MATCH iff
     max_m |a_m / (pi^2 m^2) - 1| <= 0.10 over m = 1..8;
     PORTCORE-OFF otherwise.

 D2  COHERENCE PROFILE: the deep-core cross-ratio battery
     (machinery verbatim from the firewall probe: conditioning
     min pairwise chordal >= 1e-3 x within-quadruple spread on
     both rungs, |cr| in [1e-3, 1e3] both rungs, top 200
     best-conditioned survivors, Dcr = |cr' - cr| / (1 + |cr|))
     as a function of the node-set size k in {4, 6, 8, 10, 12,
     16} (the k deepest common nodes; steps with < k common
     nodes are typed skips for that k).  Pooled ladder median
     per k, plus the per-ladder-third medians (steps split into
     three contiguous thirds).  TYPED: CORE-SHARP iff some
     consecutive pooled-median jump med(k_{i+1}) / med(k_i) >=
     5.0 with med(k_i) <= 0.02 (a clear knee; k* = k_i is the
     last coherent size); CORE-GRADED otherwise.

 D3  LAMBDA SIGNAL (perturbation anatomy): rebuild the FULL
     ladder under frozen surgical modifications of the comb and
     recompute the deep-core (k = 8) defect pooled median:
       (i)   EDGE-SMOOTH: masses replaced by the PNT-mean
             2 e^{u/2} du ONLY in the last log-unit of the
             window support, u > 2 alpha - 1 (du = midpoint cell
             widths of the full lattice, lattice_parametrix B1
             verbatim); interior masses kept.
       (ii)  INTERIOR-SMOOTH: the complement -- masses smoothed
             for u <= 2 alpha - 1, the last log-unit kept true.
       (iii) ATOMS-ONLY: prime-power tails removed -- keep only
             the k = 1 atoms (n prime), drop all p^k with k >= 2
             (the Euler-echo test: euler_scattering_source typed
             the powers as the ECHOES of the per-prime
             scatterers; if the coherence needs them it is a
             genuinely multiplicative signal).
       (iv)  WRONG-LAMBDA: masses 2 log(n) / sqrt(n) at every
             prime power -- the freeze Lambda(p^k) -> log(p^k) =
             log n (positions and rough size preserved, the
             arithmetic value log p destroyed; differs from
             truth only on the k >= 2 atoms, by the factor k).
     Prime identification WITHOUT any oracle: n is a k = 1 atom
     iff Lambda(n) = log n (|LAM_TAB[n] - log n| < 1e-9 on the
     pipeline's own von-Mangoldt table).  Per world the frozen
     reading: KEEPS iff pooled med <= 2e-3 (certificate level,
     the truth reproduction bar); KILLS iff pooled med > 0.02
     (the firewall's reading bar); DEGRADED otherwise.  The
     typed table is the signal's address.

 D4  MINIMAL OBJECT (report, assembled from D1-D3 flags): the
     smallest frozen object that carries the coherence -- the
     named contract candidate for the next round.

 C   CONTROLS/WARDS: (C1, decisive ward) the SMOOTH-MASS world
     (all masses 2 e^{u/2} du): its deep-core (k = 8) median
     must reproduce the round-48 kill, > 0.02 (observed 2.7e-2);
     the TRUTH deep-core median must reproduce the certificate,
     <= 2e-3 (observed 4.3e-4).  Either side failing ->
     WARD-BROKEN (the probe does not reproduce the object it
     claims to dissect).  (C2, must fire) scramble (seed 1, kz
     9): frame death (window unavailable or lam out-block > 1 or
     lam(C_J) > 1), channel reported; silent -> WARD-BROKEN.

 W   PIPELINE WARDS: W1 >= 30 truth rungs built; W2 [Y, D_P]
     rank 2 on every truth rung (s3/s1 <= 1e-10); W3 >= 30
     k = 1 steps with >= 8 common port aliases.

KILLS: K1 pipeline ward breaks -> PIPELINE-BROKEN; K2 a C ward
breaks (truth not certificate / smooth not dead / scramble
silent) -> WARD-BROKEN.

VERDICT (frozen enum): DEEPCORE-MEASURED with typed sublabels
ALIAS-FIXED / ALIAS-DRIFTING (D1), PORTCORE-MATCH / PORTCORE-OFF
(D1), CORE-SHARP(k*) / CORE-GRADED (D2), and the D3 kill list
(per world KEEPS / DEGRADED / KILLS); else PIPELINE-BROKEN /
WARD-BROKEN.

FROZEN BARS: DC_CERT = 2e-3; DC_DEAD = 0.02; KNEE_FACTOR = 5.0;
ALIAS_FIXED_FRAC = 0.90; PORTCORE_TOL = 0.10; EDGE_LOGU = 1.0;
K_PROFILE = (4, 6, 8, 10, 12, 16); PRIME_ID_TOL = 1e-9; battery
conditioning / caps verbatim from the firewall probe.

SPEC v2 AMENDMENTS (documented before the run; fail-first
preserved): (i) core.build_window(kz) results are MEMOIZED per
(kz, seed) as a slim dict (h, M, D, alpha, uu, lam) plus the
deterministic archimedean lag vector -- pure memoization of a
deterministic function, bit-identical physics, needed because six
ladders (truth + 4 surgeries + smooth) share the same windows;
(ii) the frame channel (window compression lamO / lamC and
lam(E)) is computed ONLY for the declared scramble control -- it
never feeds the carrier, and the firewall probe used it only for
its controls; (iii) the D2 battery at size k admits only steps
with >= k common nodes (else 'the k deepest' is undefined);
per-k step counts printed; (iv) prime/prime-power identification
uses the pipeline's own LAM_TAB (Lambda(n) = log n test) -- no
sieve and no oracle identifiers; (v) the knee rule and all
reading bars are concretized numerically above, frozen before
the first run.

NO RH claim -- deep-core cross-ratio coherence of a compressed-
truncation carrier is a numerical measurement, not a theorem
about zeros.

FIREWALL: no zeros, no prime oracles (AST scan; banned ids
zetazero / nzeros / primerange / isprime / primepi / nextprime /
prevprime); v563 READ-ONLY; RNG only inside the declared
scramble control; stdout only.  No marker moves.

Sources (read-only): v563_paper2_readouts; carrier extraction
verbatim from port_schur_cocycle_probe.py / iiks_gauge_firewall_
probe.py; deep-core sub-battery verbatim from mobius_crossratio_
firewall_probe.py (PRIME.PORT.MOEBIUS.CRFIREWALL.01); smooth-mass
B1 world from lattice_parametrix_probe.py; per-prime comb reading
from euler_scattering_source_probe.py; port-alias Bessel profile
from christoffel_hypotheses_probe.py (H5).  IIKS =
Its-Izergin-Korepin-Slavnov.

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/deepcore_anatomy_probe.py
"""

import ast
import hashlib
import math
import os
import sys
import time
from collections import Counter
from itertools import combinations

import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
_VERIFY = os.path.abspath(os.path.join(_HERE, "..", "..",
                                       "verification"))
sys.path.insert(0, _HERE)
sys.path.insert(0, _VERIFY)

import v563_paper2_readouts as core        # noqa: E402  (READ-ONLY)

H_DEEP_MAX = 900
JWIN = tuple(range(2, 25, 2))
MIN_RUNGS = 30
MIN_STEPS = 30
MIN_COMMON_J = 8
RANK_BAR = 1e-10
CTRL_KZ = 9

COND_SEP_FRAC = 1e-3              # within-tuple conditioning
CR_ABS_LO, CR_ABS_HI = 1e-3, 1e3  # |cr| window (both rungs)
QUAD_ACCEPT_CAP = 200             # best-conditioned survivors
DEEP_CORE_N = 8                   # the round-48 deep core
K_PROFILE = (4, 6, 8, 10, 12, 16)
DC_CERT = 2e-3                    # certificate reproduction bar
DC_DEAD = 0.02                    # the firewall's reading bar
KNEE_FACTOR = 5.0                 # D2 knee jump factor
ALIAS_FIXED_FRAC = 0.90           # D1 modal-set fraction
PORTCORE_TOL = 0.10               # D1 a_m vs pi^2 m^2 (deepest)
EDGE_LOGU = 1.0                   # D3 edge = last log-unit
PRIME_ID_TOL = 1e-9               # Lambda(n) = log n test
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


# --------- pipeline, verbatim from the firewall probe (memoized)
def grid_density(c):
    c = np.asarray(c, float)
    a = np.concatenate([c, c[-2:0:-1]])
    d = np.fft.fft(a)
    assert float(np.max(np.abs(d.imag))) <= 1e-9 * max(
        1.0, float(np.max(np.abs(d.real))))
    return d.real


def cell_widths(uu):
    """Midpoint cells (lattice_parametrix verbatim; smooth mass)."""
    du = np.zeros(len(uu))
    du[1:-1] = 0.5 * (uu[2:] - uu[:-2])
    du[0] = uu[1] - uu[0]
    du[-1] = uu[-1] - uu[-2]
    return du


_WIN_CACHE = {}


def window_of(kz, scramble_seed=None):
    """SPEC v2 amendment (i): pure memoization of the
    deterministic core.build_window(kz) -- slim dict + the
    archimedean lag vector; physics bit-identical."""
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


def build_rung(kz, scramble_seed=None, world_fn=None):
    rr = window_of(kz, scramble_seed=scramble_seed)
    M, D, alpha = rr["M"], rr["D"], rr["alpha"]
    uu = rr["uu"]
    mm = 2.0 * rr["lam"]
    if world_fn is not None:
        uu, mm = world_fn(uu, mm, rr)
    c_at, _ = core.atom_lags_at(alpha, M, uu, mm)
    d = grid_density(rr["c_ar"] + c_at)
    return dict(d=d, L=2 * M - 2, D=D, alpha=alpha, h=rr["h"])


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


def antisym_generators(C):
    """Canonical (f, g) with C = f g^T - g f^T (SPEC v2 extraction,
    verbatim)."""
    U, sv, _Vh = np.linalg.svd(C)
    s1 = sv[0]
    f = math.sqrt(s1) * U[:, 0]
    g = math.sqrt(s1) * U[:, 1]
    Ct = np.outer(f, g) - np.outer(g, f)
    if np.linalg.norm(Ct + C) < np.linalg.norm(Ct - C):
        g = -g
    return f, g, sv


def gauge_fix(f, g, jp):
    """FROZEN EXTRACTION GAUGE (lax2 verbatim): SO(2) rotation
    pinning the deepest port node -- a chordal isometry, so the
    cross-ratio battery is exactly gauge-free."""
    m0 = int(np.argmin(jp))
    r = math.hypot(f[m0], g[m0])
    c, s = f[m0] / r, g[m0] / r
    return c * f + s * g, -s * f + c * g


def rung_all(kz, need_frame=False, **kw):
    """One heavy build per rung (firewall verbatim; SPEC v2
    amendment (ii): the frame channel only for the declared
    control)."""
    b = build_rung(kz, **kw)
    h, L, D = b["h"], b["L"], b["D"]
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
    out = dict(kz=kz, h=h, L=L, D=D, alpha=b["alpha"])
    if need_frame:
        out["lamE"] = float(np.linalg.eigvalsh(E)[-1])
        idx = {int(j): k for k, j in enumerate(uf_n)}
        jav = [j for j in JWIN if j in idx]
        if len(jav) >= MIN_COMMON_J:
            iw = [idx[j] for j in jav]
            io = [k for k in range(E.shape[0])
                  if k not in set(iw)]
            Eo = E[np.ix_(io, io)]
            IO = np.eye(len(io)) - Eo
            CJ = (E[np.ix_(iw, iw)]
                  + E[np.ix_(iw, io)] @ np.linalg.solve(
                      IO, E[np.ix_(io, iw)]))
            CJ = 0.5 * (CJ + CJ.T)
            out["lamO"] = float(np.linalg.eigvalsh(Eo)[-1])
            out["lamC"] = float(np.linalg.eigvalsh(CJ)[-1])
    tau_m = (2.0 * math.pi * uf_n / L) / D
    port = tau_m <= float(np.max(tau_m)) / 10.0
    ip, ib = np.where(port)[0], np.where(~port)[0]
    if len(ip) >= 4 and len(ib) >= 1:
        P = E[np.ix_(ip, ip)]
        X = E[np.ix_(ip, ib)]
        R = E[np.ix_(ib, ib)]
        IR = np.eye(len(ib)) - R
        DP = P + X @ np.linalg.solve(IR, X.T)
        DP = 0.5 * (DP + DP.T)
        Y = np.diag(ys[ip])
        C = Y @ DP - DP @ Y
        f, g, sv = antisym_generators(C)
        f, g = gauge_fix(f, g, uf_n[ip])
        out["f"], out["g"] = f, g
        out["jp"], out["yp"] = uf_n[ip], ys[ip]
        out["taup"] = tau_m[ip]
        out["rk"] = float(sv[2] / sv[0]) if len(sv) > 2 else 0.0
    return out


# ------------------------------------------- RP^1 machinery (verbatim)
def unit_pairs(g, f):
    P = np.stack([np.asarray(g, float), np.asarray(f, float)],
                 axis=1)
    return P / np.linalg.norm(P, axis=1)[:, None]


def chord_mat(P):
    return np.abs(P[:, None, 0] * P[None, :, 1]
                  - P[:, None, 1] * P[None, :, 0])


def sdet(p, q):
    return float(p[0] * q[1] - p[1] * q[0])


def cross_ratio(P, i, j, k, l):
    den = sdet(P[i], P[l]) * sdet(P[j], P[k])
    if abs(den) < 1e-300:
        return None
    return (sdet(P[i], P[k]) * sdet(P[j], P[l])) / den


def pair_pairs(ra, rb):
    """Raw unit pairs on the sorted common port alias indices."""
    com, ia, ib = np.intersect1d(ra.get("jp", []),
                                 rb.get("jp", []),
                                 return_indices=True)
    if len(com) < MIN_COMMON_J:
        return None
    Pa = unit_pairs(ra["g"][ia], ra["f"][ia])
    Pb = unit_pairs(rb["g"][ib], rb["f"][ib])
    return Pa, Pb, com


def core_battery(Pa, Pb, core_n):
    """The deep-core quadruple battery (firewall verbatim,
    core_n deepest common nodes): full enumeration, conditioning
    on both rungs, top QUAD_ACCEPT_CAP survivors."""
    nodes = np.arange(core_n)
    Da, Db = chord_mat(Pa), chord_mat(Pb)
    cands = []
    for q in combinations(nodes.tolist(), 4):
        qi = list(q)
        score = 1.0
        ok = True
        for Dm in (Da, Db):
            sub = Dm[np.ix_(qi, qi)]
            vals = sub[np.triu_indices(4, 1)]
            spread = float(np.max(vals))
            if spread < 1e-300 or float(np.min(vals)) \
                    < COND_SEP_FRAC * spread:
                ok = False
                break
            score = min(score, float(np.min(vals)))
        if not ok:
            continue
        cra = cross_ratio(Pa, *q)
        crb = cross_ratio(Pb, *q)
        if (cra is None or crb is None
                or not (CR_ABS_LO <= abs(cra) <= CR_ABS_HI)
                or not (CR_ABS_LO <= abs(crb) <= CR_ABS_HI)):
            continue
        cands.append((score, q,
                      abs(crb - cra) / (1.0 + abs(cra))))
    cands.sort(key=lambda sqd: (-sqd[0], sqd[1]))
    return [d for _s, _q, d in cands[:QUAD_ACCEPT_CAP]]


def deep_battery(rungs, core_n):
    """Pooled deep-core cr-defects over all k = 1 steps with
    >= core_n common nodes (SPEC v2 amendment (iii))."""
    pooled, per_step, n_skip = [], [], 0
    for i in range(len(rungs) - 1):
        pp = pair_pairs(rungs[i], rungs[i + 1])
        if pp is None or len(pp[2]) < core_n:
            n_skip += 1
            continue
        dfs = core_battery(pp[0], pp[1], core_n)
        if not dfs:
            n_skip += 1
            continue
        pooled.extend(dfs)
        per_step.append((rungs[i]["h"], rungs[i + 1]["h"], dfs))
    return pooled, per_step, n_skip


def q_stats(v):
    a = np.asarray(v, float)
    return (float(np.median(a)), float(np.percentile(a, 90)),
            float(np.max(a)))


def build_ladder(world_fn=None):
    rungs = []
    rk_max = 0.0
    for kz in core.frame_a_zones():
        r = rung_all(kz, world_fn=world_fn)
        if not isinstance(r, dict) or "f" not in r:
            continue
        rk_max = max(rk_max, r.get("rk", 1.0))
        rungs.append(r)
    rungs.sort(key=lambda r: (r["h"], r["kz"]))
    return rungs, rk_max


# ------------------------------------------- D3 frozen mass worlds
def atoms_of(rr):
    """The prime-power values n of the window's atoms (READ-ONLY
    v563 table; positions are u = log n)."""
    return core._NN[:rr["n_atom"]].astype(float)


def k1_mask(nn):
    """k = 1 atoms: n prime iff Lambda(n) = log n on the
    pipeline's own von-Mangoldt table (no oracle)."""
    lam_n = core.LAM_TAB[nn.astype(int)]
    return np.abs(lam_n - np.log(nn)) < PRIME_ID_TOL


def smooth_masses(uu):
    """PNT-mean masses 2 e^{u/2} du (lattice_parametrix B1)."""
    return 2.0 * np.exp(uu / 2.0) * cell_widths(uu)


def world_edge_smooth(uu, mm, rr):
    mm2 = mm.copy()
    sel = uu > 2.0 * rr["alpha"] - EDGE_LOGU
    mm2[sel] = smooth_masses(uu)[sel]
    return uu, mm2


def world_interior_smooth(uu, mm, rr):
    mm2 = mm.copy()
    sel = uu <= 2.0 * rr["alpha"] - EDGE_LOGU
    mm2[sel] = smooth_masses(uu)[sel]
    return uu, mm2


def world_atoms_only(uu, mm, rr):
    keep = k1_mask(atoms_of(rr))
    return uu[keep], mm[keep]


def world_wrong_lambda(uu, mm, rr):
    nn = atoms_of(rr)
    return uu, 2.0 * np.log(nn) / np.sqrt(nn)


def world_smooth(uu, mm, rr):
    return uu, smooth_masses(uu)


D3_WORLDS = (("EDGE-SMOOTH", world_edge_smooth),
             ("INTERIOR-SMOOTH", world_interior_smooth),
             ("ATOMS-ONLY", world_atoms_only),
             ("WRONG-LAMBDA", world_wrong_lambda))


def world_label(med):
    if med <= DC_CERT:
        return "KEEPS"
    if med > DC_DEAD:
        return "KILLS"
    return "DEGRADED"


def main():
    section("PRIME.PORT.DEEPCORE.01 -- anatomy of the surviving "
            "deep-core cross-ratio coherence (EXPLORATION ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s"
          % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
    print("    NO RH claim; fit-free, gauge-free battery; no "
          "marker moves.")
    print("\nS0 -- firewall")
    check("S0.1 AST firewall clean", not ast_scan(BANNED_IDS))

    # ------------------------------------------------------------ W
    section("W -- build the truth ladder (all frame-A zones, "
            "h <= %d; machinery verbatim)" % H_DEEP_MAX)
    rungs, rk_max = build_ladder()
    print("    %d rungs, h %d .. %d; worst [Y,D_P] s3/s1 %.1e  "
          "(%.1f s)"
          % (len(rungs), rungs[0]["h"] if rungs else -1,
             rungs[-1]["h"] if rungs else -1, rk_max,
             time.time() - T0))
    check("W1 >= %d rungs built" % MIN_RUNGS,
          len(rungs) >= MIN_RUNGS, "%d rungs" % len(rungs),
          kill="K1")
    check("W2 rank-2 exact on every rung (max s3/s1 %.1e <= %.0e)"
          % (rk_max, RANK_BAR), rk_max <= RANK_BAR, kill="K1")

    # ------------------------------------------------------------ D1
    section("D1 -- NODE IDENTIFICATION: the deep-core census "
            "along the ladder")
    step_cores = []
    print("    per-step deep core (8 smallest common aliases):")
    for i in range(len(rungs) - 1):
        pp = pair_pairs(rungs[i], rungs[i + 1])
        if pp is None:
            continue
        com = pp[2]
        core8 = tuple(int(j) for j in com[:DEEP_CORE_N])
        step_cores.append(core8)
        print("    h %3d->%3d  n_com %2d  deep-8 %s"
              % (rungs[i]["h"], rungs[i + 1]["h"], len(com),
                 list(core8)))
    check("W3 >= %d k=1 steps with >= %d common aliases"
          % (MIN_STEPS, MIN_COMMON_J),
          len(step_cores) >= MIN_STEPS,
          "%d steps" % len(step_cores), kill="K1")
    freq = Counter(j for c8 in step_cores for j in c8)
    print("\n    alias frequency in the deep-8 (over %d steps):"
          % len(step_cores))
    for j, n in sorted(freq.items()):
        print("      alias j = %3d : %3d / %d steps"
              % (j, n, len(step_cores)))
    modal = tuple(sorted(j for j, _n in freq.most_common(
        DEEP_CORE_N)))
    frac_modal = (sum(1 for c8 in step_cores if c8 == modal)
                  / max(len(step_cores), 1))
    evens = tuple(range(2, 2 * DEEP_CORE_N + 1, 2))
    d1_alias = ("ALIAS-FIXED" if frac_modal >= ALIAS_FIXED_FRAC
                else "ALIAS-DRIFTING")
    print("    modal deep-8 set: %s  (exact in %.0f%% of steps; "
          "bar %.0f%%)"
          % (list(modal), 100 * frac_modal,
             100 * ALIAS_FIXED_FRAC))
    print("    even set {2..16}? %s"
          % ("YES -- the j = 2..16 evens" if modal == evens
             else "no"))
    check("D1.1 typed: %s" % d1_alias, True)

    print("\n    anatomy at three representative rungs "
          "(a_m = 2 h^2 (1 - y_m) vs pi^2 m^2):")
    reps = [rungs[0], rungs[len(rungs) // 2], rungs[-1]]
    dev_deepest = float("inf")
    for r in reps:
        h = r["h"]
        n8 = min(DEEP_CORE_N, len(r["jp"]))
        print("    kz %-3d h %4d (L %5d, D %.4f):"
              % (r["kz"], h, r["L"], r["D"]))
        devs = []
        for m in range(1, n8 + 1):
            j = int(r["jp"][m - 1])
            y = float(r["yp"][m - 1])
            tau = float(r["taup"][m - 1])
            a = 2.0 * h * h * (1.0 - y)
            ref = (math.pi ** 2) * m * m
            devs.append(abs(a / ref - 1.0))
            print("      m %d  alias j %3d  y %.6f  tau %8.4f  "
                  "a_m %9.3f  a_m/(pi^2 m^2) %.4f"
                  % (m, j, y, tau, a, a / ref))
        if r is rungs[-1]:
            dev_deepest = max(devs) if devs else float("inf")
    d1_core = ("PORTCORE-MATCH" if dev_deepest <= PORTCORE_TOL
               else "PORTCORE-OFF")
    print("    deepest rung: max_m |a_m/(pi^2 m^2) - 1| = %.3f "
          "(bar %.2f)" % (dev_deepest, PORTCORE_TOL))
    check("D1.2 typed: %s (the a_m = pi^2 m^2 port core)"
          % d1_core, True)

    # ------------------------------------------------------------ D2
    section("D2 -- COHERENCE PROFILE vs node-set size k "
            "(deepest k common nodes)")
    meds_k = {}
    truth_dc_med = float("inf")
    for kn in K_PROFILE:
        pooled, per_step, n_skip = deep_battery(rungs, kn)
        if not pooled:
            print("    k = %2d : no measurable steps" % kn)
            continue
        m, q90, mx = q_stats(pooled)
        meds_k[kn] = m
        thirds = np.array_split(np.arange(len(per_step)), 3)
        tmeds = []
        for t in thirds:
            vals = [d for ii in t for d in per_step[ii][2]]
            tmeds.append(float(np.median(vals)) if vals
                         else float("nan"))
        print("    k = %2d : %3d steps (%2d skips)  %5d quads  "
              "med %.2e  q90 %.2e  max %.2e | thirds %s"
              % (kn, len(per_step), n_skip, len(pooled), m, q90,
                 mx, "  ".join("%.2e" % v for v in tmeds)))
        if kn == DEEP_CORE_N:
            truth_dc_med = m
    knee_k, knee_ratio = None, 0.0
    ks = [k for k in K_PROFILE if k in meds_k]
    for a, b in zip(ks, ks[1:]):
        r = meds_k[b] / max(meds_k[a], 1e-300)
        if (r >= KNEE_FACTOR and meds_k[a] <= DC_DEAD
                and r > knee_ratio):
            knee_k, knee_ratio = a, r
    d2_type = ("CORE-SHARP(k*=%d)" % knee_k if knee_k is not None
               else "CORE-GRADED")
    print("    knee scan (jump >= x%.0f with coherent pre-knee "
          "<= %.2f): %s%s"
          % (KNEE_FACTOR, DC_DEAD, d2_type,
             ("  (jump x%.1f at k %d -> %d)"
              % (knee_ratio, knee_k,
                 ks[ks.index(knee_k) + 1]))
             if knee_k is not None else ""))
    check("D2.1 typed: %s" % d2_type, True)

    # ------------------------------------------------------------ D3
    section("D3 -- LAMBDA SIGNAL: surgical mass worlds, deep-core "
            "(k = %d) defect" % DEEP_CORE_N)
    d3 = {}
    rows = [("TRUTH", truth_dc_med, len(rungs), "reference")]
    for name, fn in D3_WORLDS:
        t1 = time.time()
        w_rungs, w_rk = build_ladder(world_fn=fn)
        pooled, per_step, n_skip = deep_battery(w_rungs,
                                                DEEP_CORE_N)
        med = q_stats(pooled)[0] if pooled else float("inf")
        d3[name] = med
        rows.append((name, med, len(w_rungs),
                     "%d steps, %d skips, worst s3/s1 %.1e, "
                     "%.0f s" % (len(per_step), n_skip, w_rk,
                                 time.time() - t1)))
        print("    %-16s med %.2e  (%s)"
              % (name, med, rows[-1][3]), flush=True)
    print("\n    THE SURGICAL TABLE (bars: KEEPS <= %.0e / "
          "KILLS > %.2f):" % (DC_CERT, DC_DEAD))
    print("    %-16s %-10s %s" % ("world", "dc-median", "reading"))
    d3_labels = {}
    for name, med, _nr, _det in rows:
        lab = ("reference" if name == "TRUTH"
               else world_label(med))
        if name != "TRUTH":
            d3_labels[name] = lab
        print("    %-16s %.2e   %s" % (name, med, lab))
    killers = [n for n, l in d3_labels.items() if l == "KILLS"]
    keepers = [n for n, l in d3_labels.items() if l == "KEEPS"]
    check("D3.1 surgical table typed (killers: %s)"
          % (", ".join(killers) if killers else "none"), True)

    # ------------------------------------------------------------ C
    section("C -- controls / wards")
    print("  C1 the smooth-mass world (all masses 2 e^{u/2} du) "
          "-- the round-48 ward:")
    sm_rungs, sm_rk = build_ladder(world_fn=world_smooth)
    sm_pooled, sm_steps, sm_skip = deep_battery(sm_rungs,
                                                DEEP_CORE_N)
    sm_med = q_stats(sm_pooled)[0] if sm_pooled else float("inf")
    print("    smooth ladder: %d rungs (worst s3/s1 %.1e); "
          "deep-core med %.2e over %d steps (%d skips)"
          % (len(sm_rungs), sm_rk, sm_med, len(sm_steps),
             sm_skip))
    print("    round-48 reproduction: truth %.2e (was 4.3e-4) vs "
          "smooth %.2e (was 2.7e-2)" % (truth_dc_med, sm_med))
    check("C1.1 WARD truth deep-core certificate (med %.2e <= "
          "%.0e)" % (truth_dc_med, DC_CERT),
          truth_dc_med <= DC_CERT, kill="K2")
    check("C1.2 WARD smooth deep-core dead (med %.2e > %.2f)"
          % (sm_med, DC_DEAD), sm_med > DC_DEAD, kill="K2")

    print("\n  C2 scramble (seed 1, kz %d) -- frame death must "
          "fire:" % CTRL_KZ)
    rc = rung_all(CTRL_KZ, scramble_seed=1, need_frame=True)
    if not isinstance(rc, dict):
        fired = True
        print("    scramble: rung not built (%r) -> FRAME DIES"
              % (rc,))
    elif "lamC" not in rc:
        fired = True
        print("    scramble: window unavailable -> FRAME DIES")
    else:
        fired = (rc["lamO"] > 1.0) or (rc["lamC"] > 1.0)
        print("    scramble: lam(out) %.3e | lam(C_J) %.3e | "
              "lam(E) %.3e -> %s"
              % (rc["lamO"], rc["lamC"], rc["lamE"],
                 "fires via %s" % ("EXTERIOR" if rc["lamO"] > 1.0
                                   else "WINDOW")
                 if fired else "SILENT"))
    check("C2.1 WARD scramble frame death fires", fired,
          kill="K2")

    # ------------------------------------------------------------ D4
    section("D4 -- THE MINIMAL OBJECT (report)")
    ek = d3_labels.get("EDGE-SMOOTH") == "KILLS"
    ik = d3_labels.get("INTERIOR-SMOOTH") == "KILLS"
    if ek and ik:
        region = ("the true Lambda masses across the WHOLE comb "
                  "(both partial smoothings kill)")
    elif ek:
        region = ("the true Lambda masses in the LAST LOG-UNIT "
                  "u in (2 alpha - 1, 2 alpha] (edge smoothing "
                  "kills, interior smoothing does not)")
    elif ik:
        region = ("the true Lambda masses in the INTERIOR u <= "
                  "2 alpha - 1 (interior smoothing kills, edge "
                  "smoothing does not)")
    else:
        region = ("no single radial region (neither partial "
                  "smoothing alone kills)")
    if d3_labels.get("ATOMS-ONLY") == "KEEPS":
        mult = ("the k = 1 prime atoms SUFFICE (the p^k echoes "
                "are not load-bearing)")
    elif d3_labels.get("ATOMS-ONLY") == "KILLS":
        mult = ("the p^k (k >= 2) Euler echoes are REQUIRED -- a "
                "genuinely multiplicative signal")
    else:
        mult = ("the p^k echoes matter but do not fully kill "
                "(ATOMS-ONLY degraded)")
    if d3_labels.get("WRONG-LAMBDA") == "KEEPS":
        val = ("the Lambda VALUES are not load-bearing beyond "
               "position + rough size (wrong-Lambda keeps)")
    elif d3_labels.get("WRONG-LAMBDA") == "KILLS":
        val = ("the exact Lambda(p^k) = log p values are "
               "load-bearing (wrong-Lambda kills)")
    else:
        val = "the Lambda values matter partially (degraded)"
    node_txt = ("the FIXED alias set %s" % (list(modal),)
                if d1_alias == "ALIAS-FIXED"
                else "a drifting deep-8 alias set")
    core_txt = ("%s port core (a_m = pi^2 m^2, m = 1..8)"
                % ("the" if d1_core == "PORTCORE-MATCH"
                   else "NOT the"))
    print("    nodes   : %s = %s" % (node_txt, core_txt))
    print("    profile : %s" % d2_type)
    print("    region  : %s" % region)
    print("    atoms   : %s" % mult)
    print("    values  : %s" % val)
    print("\n    MINIMAL OBJECT (contract candidate for the next "
          "round):")
    print("      the cross-ratio coherence of the carrier r = "
          "g/f on %s,"
          % ("the deep-8 port aliases %s" % (list(modal),)
             if d1_alias == "ALIAS-FIXED" else
             "the 8 deepest common port aliases"))
    print("      carried by %s;" % region)
    print("      %s; %s." % (mult, val))
    check("D4.1 minimal object stated", True)

    # ------------------------------------------------------------ V
    section("V -- FROZEN VERDICT")
    n_pass = sum(1 for _n, okk in CHECKS if okk)
    n_tot = len(CHECKS)
    if KILLS:
        VERDICT = {"K1": "PIPELINE-BROKEN",
                   "K2": "WARD-BROKEN"}[KILLS[0]]
        print("\n  VERDICT: %s" % VERDICT)
    else:
        d3_str = ", ".join("%s=%s" % (n, d3_labels[n])
                           for n, _f in D3_WORLDS)
        VERDICT = ("DEEPCORE-MEASURED / %s / %s / %s / [%s]"
                   % (d1_alias, d1_core, d2_type, d3_str))
        print("\n  VERDICT: %s" % VERDICT)
        print("  (truth dc med %.2e; smooth ward %.2e; modal "
              "deep-8 %s)"
              % (truth_dc_med, sm_med, list(modal)))
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed"
          % (time.time() - T0, n_tot, n_tot - n_pass))
    return 0 if n_pass == n_tot else 1


if __name__ == "__main__":
    raise SystemExit(main())
