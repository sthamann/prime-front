#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""deepcore_bent_code_probe -- PRIME.PORT.BENTCODE.01 (EXPLORATION
ONLY, experiments/; round 58, strategy S3 of the cross-front memo:
read the deep-core fingerprint as an EXPLICIT CODE on 16 points and
test it against the compiler's pre-registered BENT predictions,
2026-08-09).

THE QUESTION (frozen): deepcore_anatomy_probe
(PRIME.PORT.DEEPCORE.01, round 50) measured the arithmetic remnant
as the FIXED even alias set {2, 4, ..., 16} = the port core at the
Bessel coordinates a_m = pi^2 m^2, with a coherence knee at k* = 10
and all four surgical mass controls killing.  The compiler's finite
side (CFIN.ANCHOR.HADAMARD.01, promoted v888 / discovery
s6_plucker_hadamard_probe) carries a (16, 6, 2) Hadamard difference
set whose indicator is a BENT function on F_2^4: Walsh spectrum
identically |W| = 4 = 2^{e1/2}, perfect off-peak autocorrelation 0,
and distance 6 = nonlinearity to the 32 affine functions.  IF the
deep-core fingerprint is a message written in the compiler's code
alphabet, its binarization on 16 natural addresses should reproduce
these three invariants.  This probe freezes TWO independent
binarization rules, measures the three invariants exactly (integer
arithmetic on the boolean tables), and runs the four surgical
control worlds through the identical rules.

THE PRE-REGISTERED PREDICTIONS (CFIN.ANCHOR.HADAMARD.01, stated
BEFORE any measurement below; these numbers are frozen inputs, not
outputs):
    (P1) Walsh spectrum W_f(u) = sum_x (-1)^{f(x) + u.x} satisfies
         |W_f(u)| = 4 on ALL 16 characters u (bent; flatness ratio
         max|W| / min|W| = 1);
    (P2) autocorrelation r_f(a) = sum_x s(x) s(x+a), s = (-1)^f,
         equals 0 on ALL 15 nonzero shifts a (perfect
         nonlinearity);
    (P3) minimal Hamming distance of f to the 32 affine functions
         equals 6 (the bent nonlinearity 2^3 - 2^1 on F_2^4).
    (P4, honesty bar) the two independent binarization rules agree
         on >= 12 of the 16 points -- else the code reading is
         typed artifact-risky regardless of the spectra.

THE ADDRESSING (frozen choice of ONE of the two contract options):
the 16 EVEN ALIASES J16 = (2, 4, ..., 32) of the folded negative
grid, alias j = 2m addressed by x = m - 1 in F_2^4 (bit i of x =
((m-1) >> i) & 1, the register bit-model convention 'words are
ints 0..15').  JUSTIFICATION: the deep core {2..16} IS the port
core a_m = pi^2 m^2 at m = 1..8 (deepcore_anatomy D1, PORTCORE-
MATCH), so the Bessel index m is the compiler-native coordinate
and m = 1..16 is its unique parameter-free continuation; the
rejected alternative (8 deep aliases x 2 sheets) would inject the
sheet bit BY HAND -- an addressing artifact the honesty bar P4
could not detect.  The alias windows, the port cut and the carrier
extraction are v563/anatomy verbatim.

THE COMB (frozen, v563 verbatim): atoms at u_n = log n on the
prime powers n = p^k with masses 2 Lambda(n) / sqrt(n); windows =
all frame-A zones with h <= 900 sorted by (h, kz); consecutive
pairs (k = 1).  Carriers (g_j, f_j) = IIKS generators of the
dressed port commutator [Y, D_P] in the frozen one-point SO(2)
gauge (deepcore_anatomy / iiks_gauge_firewall verbatim).

FROZEN PROTOCOL (2026-08-09, frozen + SHA-hashed before the first
run; all bars frozen before the run):

 B1  THE BINARIZATION (two independent frozen rules; the honest
     mitigation against rule-does-the-work):
     RULE A (wall side -- sign of the per-alias contribution to
     the dangerous-direction quadratic form): per rung the 16x16
     window compression A_h = I - C_J16 (Schur compression of the
     folded-neg Carleson Gram E_h onto the J16 aliases,
     port_schur_reduction / relative_congruence machinery
     verbatim); per consecutive full-window pair the increment
     Delta_h = A_{h+1} - A_h in the shared alias coordinates; the
     dangerous direction v_h = unit eigenvector of A_h at
     lambda_min (the wall soft mode -- the round-51/52 dangerous
     direction of the congruence flow); the per-alias contribution
     c_j = v_j (Delta_h v)_j (sums to the round-52 increment scale
     v^T Delta v; invariant under v -> -v, so no eigenvector sign
     convention is needed).  Aggregation: med_j = median of c_j
     over the pair ladder; BIT f_A(x(j)) = 1 iff med_j < 0 (the
     destabilizing sign).
     RULE B (carrier side -- threshold of the coherence profile at
     the measured knee): the deep-core cross-ratio battery
     (anatomy verbatim: conditioning >= 1e-3 x spread both rungs,
     |cr| in [1e-3, 1e3] both rungs, top 200 survivors, Dcr =
     |cr' - cr| / (1 + |cr|)) on the NAMED alias prefixes
     J16[:m] = (2, ..., 2m) for every m in 4..16 (steps missing an
     alias of the prefix in the common port set are typed skips);
     prof(m) = pooled ladder median at size m -- the coherence
     profile.  Knee scan (anatomy rule on the integer grid):
     k* = the m with the largest jump prof(m+1)/prof(m) >=
     KNEE_FACTOR = 5.0 among those with prof(m) <= DC_DEAD = 0.02;
     frozen threshold THR = sqrt(prof(k*) prof(k*+1)) (the
     geometric midpoint of the knee jump); if NO knee fires, the
     fallback THR = DC_CERT = 2e-3 (the corpus certificate bar).
     BIT f_B(x(2m)) = 1 iff prof(entry(m)) <= THR with entry(m) =
     max(m, 4) (aliases entering below the smallest quadruple size
     inherit prof(4)); an unmeasurable entry size gives bit 0
     (not certified coherent).  Both boolean tables printed in
     full; AGREEMENT census (P4): agree = #{x : f_A(x) = f_B(x)},
     bar >= 12/16; typed CODE-CONSISTENT(agree) /
     CODE-ARTIFACT(agree).

 B2  THE THREE INVARIANTS (exact integers, per rule, truth world):
     (a) the full Walsh spectrum W_f(u) on all 16 characters, the
         flatness ratio max|W| / min|W|, and the census of
         characters with |W| = 4 -- BENT iff 16/16 (P1);
     (b) the autocorrelation r_f(a) on all 15 nonzero shifts --
         perfect iff all 0 (P2);
     (c) the minimal Hamming distance to the 32 affine functions
         (P3: 6 predicted).
     TYPED: a rule is BENT iff (a) holds 16/16; NEAR iff >= 12/16
     characters carry |W| = 4 (the deviating characters printed);
     DEAD otherwise.  The probe label: BENT-EXACT iff BOTH rules
     BENT and agree >= 12/16; BENT-NEAR(per-rule labels +
     deviations) iff at least one rule is BENT or NEAR; BENT-DEAD
     otherwise.

 B3  THE STRUCTURAL FOLLOW-ON (only if BENT-EXACT or BENT-NEAR;
     descriptive, exact counts, no claim upgrades): per qualifying
     rule -- level-set sizes |f^{-1}(0)|, |f^{-1}(1)|; for a
     level set of size 6 the (16, 6, 2) difference-set census
     (# ordered representations of every nonzero d; biplane-block
     test) and the set comparison against Z(q*) (the deployed
     compiler selector, v845/v880 rebuilt inline: unique
     sigma-invariant refinement with q(A) = 1, q(FSum) = 0) and
     against all six Arf-1 zero sets; the algebraic degree of f
     (Moebius/ANF transform), the associated bilinear form
     b_f(x,y) = f(x+y)+f(x)+f(y) vs the register form hb (v834
     identity), and -- Sp(4,2)-orbit reading consistent with the
     k6_pfaffian data -- whether f is one of the 16 quadratic
     refinements (all Arf-1 refinements are ONE Sp(4,2) orbit,
     v888); Hamming distances of f to q* and min distance to the
     16 refinements; if f is exactly bent, the dual f~ from
     W(u) = 4 (-1)^{f~(u)} with the same censuses (the Walsh
     support/sign pattern as a code object).

 C   CONTROLS (decisive; identical frozen rules, world-local knee
     with the same fallback): the four surgical control worlds
     (i) SMOOTH-MASS (all masses 2 e^{u/2} du, lattice_parametrix
     B1), (ii) WRONG-LAMBDA (masses 2 log(n)/sqrt(n)),
     (iii) ATOMS-ONLY (k = 1 prime atoms only; prime
     identification via the pipeline's own Lambda(n) = log n
     table, no oracle), (iv) SCRAMBLE (scramble_seed = 1 on every
     zone; additionally the anatomy frame-death ward at kz 9 must
     fire).  Each world is binarized by BOTH rules and its
     flatness ratios are printed.  FROZEN PREDICTION: the truth
     ratio is 1 (or the minimum of the table) and EVERY control
     ratio is > 1 (non-bent).  A control world producing an
     EXACTLY BENT table under either rule -> CONTROL-DEAD (the
     binarization is doing the work).  A control world that
     cannot produce >= CTRL_MIN_STEPS = 5 measurable steps for a
     rule is typed FRAME-DEAD for that rule (counts as fired /
     non-bent; reported).

 W   PIPELINE WARDS: W1 >= 30 truth rungs, worst [Y, D_P] rank
     ratio s3/s1 <= 1e-10; W2 >= 15 truth full-J16 window pairs
     (rule A); W3 >= 8 truth steps carrying the full J16 prefix in
     the common port set (rule B, m = 16); W4 the deep-core
     certificate reproduces: prof(8) <= DC_CERT = 2e-3 (anatomy
     C1.1 on the named core {2..16}); W5 the smooth world
     reproduces the round-48/50 kill: smooth prof(8) > DC_DEAD =
     0.02 or unmeasurable; W6 the scramble frame death fires at
     kz 9 (lam out-block > 1 or lam(C_J16) > 1 or window
     unavailable).

KILLS: K1 a W ward breaks -> PIPELINE-BROKEN; K2 a control world
is exactly bent under either rule -> CONTROL-DEAD.  B1/B2/B3
labels are TYPED, never kill.

VERDICT (frozen enum): BENTCODE-MEASURED / BENT-EXACT or
BENT-NEAR(...) or BENT-DEAD / CODE-CONSISTENT(n) or
CODE-ARTIFACT(n); else PIPELINE-BROKEN / CONTROL-DEAD.

FROZEN BARS: J16 = (2, 4, ..., 32); H_DEEP_MAX = 900; MIN_RUNGS =
30; RANK_BAR = 1e-10; MIN_PAIRS_A = 15; MIN_STEPS_B16 = 8;
CTRL_MIN_STEPS = 5; AGREE_BAR = 12; NEAR_BAR = 12 (characters with
|W| = 4); DC_CERT = 2e-3; DC_DEAD = 0.02; KNEE_FACTOR = 5.0;
battery conditioning COND_SEP_FRAC = 1e-3, |cr| window
[1e-3, 1e3], QUAD_ACCEPT_CAP = 200 (anatomy verbatim); CTRL_KZ =
9; scramble seed 1; MIN_COMMON_J = 8 (pair admission, anatomy
verbatim); PRIME_ID_TOL = 1e-9.

SPEC v1 (2026-08-09, frozen + SHA-hashed before the first run):
everything above.  Mechanical concretizations frozen with v1:
(i) core.build_window results are MEMOIZED per (kz, seed) exactly
as in deepcore_anatomy_probe (pure memoization of a deterministic
function, bit-identical physics; five ladders share windows);
(ii) a rung whose window / chain / compression construction fails
mechanically (Lanczos breakdown, singular exterior block, raised
error) carries no rule-A matrix and no carrier -- a typed skip,
never a silent pass; (iii) the rule-A eigenpair uses
numpy.linalg.eigh (ascending), dangerous direction = column 0;
(iv) prime identification in ATOMS-ONLY uses the pipeline's own
LAM_TAB (|Lambda(n) - log n| < 1e-9) -- no sieve, no oracle;
(v) the scramble world reuses the anatomy scramble channel
(build_window(kz, scramble_seed=1)) on every zone, and the kz-9
frame-death ward uses the J16 window compression of THIS probe
(lamO / lamC > 1 or window unavailable); (vi) B3's q* rebuild is
the v845 selector verbatim (2^16 refinement census, sigma
invariance, q(A) = 1, q(FSum) = 0).  Any post-run amendment is
documented here with the fail-first output preserved.

NO RH claim: boolean tables, integer Walsh spectra and Hamming
distances of a binarized finite-h fingerprint are numerical
measurements on the deployed v563 ladder, not theorems about
zeros.  NO claim upgrades: the (16,6,2) anchor stays where v888
put it; this probe only measures whether the deep-core remnant
REPRODUCES its invariants.  No marker moves.

FIREWALL: no zeros, no prime oracles (AST scan; banned ids
zetazero / nzeros / primerange / isprime / primepi / nextprime /
prevprime); v563 READ-ONLY; RNG only inside the declared scramble
control; stdout only.

Sources (read-only, machinery verbatim): v563_paper2_readouts;
deep-core extraction / battery / mass worlds from
deepcore_anatomy_probe.py (PRIME.PORT.DEEPCORE.01); window
compression from port_schur_reduction_probe.py via
relative_congruence_probe.py / eta_margin_source_probe.py
(PRIME.PORT.ETASOURCE.01, the dangerous-direction object); exact
Walsh conventions from register_frobenius_walsh_probe.py
(E8.DIVISOR210.FROBWALSH.01); the (16,6,2) anchor + q* selector
from s6_plucker_hadamard_probe.py (CFIN.ANCHOR.HADAMARD.01,
promoted v888).  IIKS = Its-Izergin-Korepin-Slavnov.

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/deepcore_bent_code_probe.py
"""

import ast
import hashlib
import itertools
import math
import os
import sys
import time
from itertools import combinations

import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
_VERIFY = os.path.abspath(os.path.join(_HERE, "..", "..",
                                       "verification"))
sys.path.insert(0, _HERE)
sys.path.insert(0, _VERIFY)

import v563_paper2_readouts as core        # noqa: E402  (READ-ONLY)

# ------------------------------------------------------ frozen bars
J16 = tuple(range(2, 34, 2))          # the 16 even aliases 2..32
H_DEEP_MAX = 900
MIN_RUNGS = 30
RANK_BAR = 1e-10
MIN_COMMON_J = 8                      # pair admission (anatomy)
MIN_PAIRS_A = 15                      # W2: truth rule-A pairs
MIN_STEPS_B16 = 8                     # W3: truth m=16 steps
CTRL_MIN_STEPS = 5                    # control worlds, both rules
AGREE_BAR = 12                        # P4 honesty bar
NEAR_BAR = 12                         # chars with |W| = 4 for NEAR

COND_SEP_FRAC = 1e-3                  # battery conditioning
CR_ABS_LO, CR_ABS_HI = 1e-3, 1e3      # |cr| window (both rungs)
QUAD_ACCEPT_CAP = 200                 # best-conditioned survivors
DC_CERT = 2e-3                        # certificate bar
DC_DEAD = 0.02                        # firewall reading bar
KNEE_FACTOR = 5.0                     # knee jump factor
PRIME_ID_TOL = 1e-9
CTRL_KZ = 9

# pre-registered (CFIN.ANCHOR.HADAMARD.01) -- inputs, not outputs
PRED_W_ABS = 4                        # |W| identically
PRED_AC_OFFPEAK = 0                   # off-peak autocorrelation
PRED_AFF_DIST = 6                     # distance to affine class

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


# --------- pipeline, verbatim from deepcore_anatomy (memoized)
def grid_density(c):
    c = np.asarray(c, float)
    a = np.concatenate([c, c[-2:0:-1]])
    d = np.fft.fft(a)
    assert float(np.max(np.abs(d.imag))) <= 1e-9 * max(
        1.0, float(np.max(np.abs(d.real))))
    return d.real


def cell_widths(uu):
    """Midpoint cells (lattice_parametrix verbatim)."""
    du = np.zeros(len(uu))
    du[1:-1] = 0.5 * (uu[2:] - uu[:-2])
    du[0] = uu[1] - uu[0]
    du[-1] = uu[-1] - uu[-2]
    return du


_WIN_CACHE = {}


def window_of(kz, scramble_seed=None):
    """SPEC v1 (i): pure memoization of the deterministic
    core.build_window(kz); physics bit-identical."""
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
    U, sv, _Vh = np.linalg.svd(C)
    s1 = sv[0]
    f = math.sqrt(s1) * U[:, 0]
    g = math.sqrt(s1) * U[:, 1]
    Ct = np.outer(f, g) - np.outer(g, f)
    if np.linalg.norm(Ct + C) < np.linalg.norm(Ct - C):
        g = -g
    return f, g, sv


def gauge_fix(f, g, jp):
    m0 = int(np.argmin(jp))
    r = math.hypot(f[m0], g[m0])
    c, s = f[m0] / r, g[m0] / r
    return c * f + s * g, -s * f + c * g


def rung_all(kz, need_frame=False, **kw):
    """One heavy build per rung (anatomy verbatim) + the rule-A
    16x16 window compression A16 = I - C_J16 (port_schur /
    relative_congruence machinery on the J16 aliases)."""
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
    idx = {int(j): k for k, j in enumerate(uf_n)}
    jav = [j for j in J16 if j in idx]
    if len(jav) == len(J16):
        iw = [idx[j] for j in J16]
        io = [k for k in range(E.shape[0]) if k not in set(iw)]
        Eo = E[np.ix_(io, io)]
        IO = np.eye(len(io)) - Eo
        try:
            CJ = (E[np.ix_(iw, iw)]
                  + E[np.ix_(iw, io)] @ np.linalg.solve(
                      IO, E[np.ix_(io, iw)]))
            CJ = 0.5 * (CJ + CJ.T)
            out["A16"] = np.eye(len(J16)) - CJ
            if need_frame:
                out["lamO"] = float(np.linalg.eigvalsh(Eo)[-1])
                out["lamC"] = float(np.linalg.eigvalsh(CJ)[-1])
        except np.linalg.LinAlgError:
            pass                       # SPEC v1 (ii): typed skip
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
        out["rk"] = float(sv[2] / sv[0]) if len(sv) > 2 else 0.0
    return out


# ------------------------------------------- RP^1 battery (verbatim)
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
    com, ia, ib = np.intersect1d(ra.get("jp", []),
                                 rb.get("jp", []),
                                 return_indices=True)
    if len(com) < MIN_COMMON_J:
        return None
    Pa = unit_pairs(ra["g"][ia], ra["f"][ia])
    Pb = unit_pairs(rb["g"][ib], rb["f"][ib])
    return Pa, Pb, com


def core_battery(Pa, Pb, core_n):
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


def build_ladder(world_fn=None, scramble_seed=None):
    rungs = []
    rk_max = 0.0
    n_err = 0
    for kz in core.frame_a_zones():
        try:
            r = rung_all(kz, world_fn=world_fn,
                         scramble_seed=scramble_seed)
        except Exception:
            n_err += 1                 # SPEC v1 (ii): typed skip
            continue
        if not isinstance(r, dict):
            continue
        if "f" in r or "A16" in r:
            rk_max = max(rk_max, r.get("rk", 0.0))
            rungs.append(r)
    rungs.sort(key=lambda r: (r["h"], r["kz"]))
    return rungs, rk_max, n_err


# ------------------------------------------- frozen mass worlds
def atoms_of(rr):
    return core._NN[:rr["n_atom"]].astype(float)


def k1_mask(nn):
    lam_n = core.LAM_TAB[nn.astype(int)]
    return np.abs(lam_n - np.log(nn)) < PRIME_ID_TOL


def smooth_masses(uu):
    return 2.0 * np.exp(uu / 2.0) * cell_widths(uu)


def world_smooth(uu, mm, rr):
    return uu, smooth_masses(uu)


def world_wrong_lambda(uu, mm, rr):
    nn = atoms_of(rr)
    return uu, 2.0 * np.log(nn) / np.sqrt(nn)


def world_atoms_only(uu, mm, rr):
    keep = k1_mask(atoms_of(rr))
    return uu[keep], mm[keep]


# ---------------------------------------------------- rule A / rule B
def rule_a(rungs):
    """Sign of the per-alias contribution to the dangerous-direction
    quadratic form (frozen: v = soft mode of A16, c_j = v_j
    (Delta v)_j, median over the pair ladder, bit = 1 iff < 0)."""
    per = {j: [] for j in J16}
    n_pairs = 0
    for i in range(len(rungs) - 1):
        A0 = rungs[i].get("A16")
        A1 = rungs[i + 1].get("A16")
        if A0 is None or A1 is None:
            continue
        Dlt = A1 - A0
        _w, V = np.linalg.eigh(A0)
        v = V[:, 0]
        c = v * (Dlt @ v)
        for k, j in enumerate(J16):
            per[j].append(float(c[k]))
        n_pairs += 1
    med = {j: (float(np.median(per[j])) if per[j] else None)
           for j in J16}
    bits = [1 if (med[j] is not None and med[j] < 0.0) else 0
            for j in J16]
    return bits, med, n_pairs


def rule_b(rungs):
    """Threshold of the coherence profile at the measured knee
    (frozen: prof(m) on named prefixes J16[:m], knee scan, THR =
    geometric knee midpoint, fallback DC_CERT)."""
    pool = {m: [] for m in range(4, 17)}
    used = {m: 0 for m in range(4, 17)}
    for i in range(len(rungs) - 1):
        pp = pair_pairs(rungs[i], rungs[i + 1])
        if pp is None:
            continue
        Pa, Pb, com = pp
        pos = {int(j): k for k, j in enumerate(com)}
        for m in range(4, 17):
            need = J16[:m]
            if not all(j in pos for j in need):
                continue
            sel = [pos[j] for j in need]
            dfs = core_battery(Pa[sel], Pb[sel], m)
            if dfs:
                pool[m].extend(dfs)
                used[m] += 1
    prof = {m: float(np.median(pool[m]))
            for m in range(4, 17) if pool[m]}
    kstar, ratio = None, 0.0
    for m in range(4, 16):
        if m in prof and (m + 1) in prof:
            r = prof[m + 1] / max(prof[m], 1e-300)
            if r >= KNEE_FACTOR and prof[m] <= DC_DEAD \
                    and r > ratio:
                kstar, ratio = m, r
    if kstar is not None:
        thr = math.sqrt(prof[kstar] * prof[kstar + 1])
    else:
        thr = DC_CERT
    bits = []
    for m in range(1, 17):
        e = max(m, 4)
        v = prof.get(e)
        bits.append(1 if (v is not None and v <= thr) else 0)
    return bits, prof, used, kstar, ratio, thr


# ---------------------------------------------------- exact invariants
def parity(n):
    return bin(n).count("1") & 1


def walsh_spec(f):
    """W_f(u) = sum_x (-1)^{f(x) + u.x} (register conventions)."""
    return [sum(-1 if (f[x] ^ parity(u & x)) else 1
                for x in range(16)) for u in range(16)]


def autocorr(f):
    s = [(-1) ** f[x] for x in range(16)]
    return [sum(s[x] * s[x ^ a] for x in range(16))
            for a in range(16)]


def affine_dist(f):
    best = 16
    for u in range(16):
        for e in (0, 1):
            d = sum(1 for x in range(16)
                    if f[x] != (parity(u & x) ^ e))
            best = min(best, d)
    return best


def flatness(W):
    a = [abs(w) for w in W]
    return (float(max(a)) / float(min(a))) if min(a) > 0 \
        else float("inf")


def spectrum_label(W):
    n4 = sum(1 for w in W if abs(w) == PRED_W_ABS)
    if n4 == 16:
        return "BENT", n4
    if n4 >= NEAR_BAR:
        return "NEAR", n4
    return "DEAD", n4


def fmt_flat(r):
    return ("%.3f" % r) if isinstance(r, float) else str(r)


# ---------------------------------------------------- B3 finite side
def pc(v):
    return bin(v).count("1")


HT = [[(pc(v) * pc(w) - pc(v & w)) % 2 for w in range(16)]
      for v in range(16)]
A_BIT = 0b1000
FSIG = 0b0111


def sig_deck(v):
    b = [(v >> i) & 1 for i in range(4)]
    n = (b[2], b[0], b[1], b[3])
    return sum(bit << i for i, bit in enumerate(n))


def refinement_census():
    out = []
    for mask in range(1 << 16):
        q = [(mask >> i) & 1 for i in range(16)]
        ok = True
        for x in range(16):
            hx = HT[x]
            qx = q[x]
            for y in range(16):
                if q[x ^ y] ^ qx ^ q[y] != hx[y]:
                    ok = False
                    break
            if not ok:
                break
        if ok:
            out.append(tuple(q))
    return out


def qstar_selector():
    refs = refinement_census()
    siginv = [q for q in refs
              if all(q[sig_deck(v)] == q[v] for v in range(16))]
    cand = [q for q in siginv if q[A_BIT] == 1 and q[FSIG] == 0]
    return refs, (cand[0] if len(cand) == 1 else None)


def anf_degree(f):
    a = list(f)
    for i in range(4):
        for x in range(16):
            if x & (1 << i):
                a[x] ^= a[x ^ (1 << i)]
    degs = [pc(x) for x in range(16) if a[x]]
    return (max(degs) if degs else 0), a


def diffset_census(S):
    reps = {}
    for d in range(1, 16):
        reps[d] = sum(1 for x in S for y in S if x ^ y == d)
    return reps


def b3_report(f, tag, refs, qstar, is_bent, W):
    print("\n    B3 [%s] structural follow-on:" % tag)
    z0 = [x for x in range(16) if f[x] == 0]
    z1 = [x for x in range(16) if f[x] == 1]
    print("      level sets: |f^-1(0)| = %d %s, |f^-1(1)| = %d %s"
          % (len(z0), z0, len(z1), z1))
    for lev, S in (("0", z0), ("1", z1)):
        if len(S) == 6:
            reps = diffset_census(S)
            vals = sorted(set(reps.values()))
            is_ds = vals == [2]
            print("      level-%s set (size 6): (16,6,2) "
                  "difference set? %s (rep counts %s)"
                  % (lev, "YES" if is_ds else "NO", vals))
            if qstar is not None:
                zq = set(v for v in range(16) if qstar[v] == 0)
                print("        equals Z(q*)? %s"
                      % ("YES" if set(S) == zq else "no"))
            arf1z = [set(v for v in range(16) if q[v] == 0)
                     for q in refs if q.count(0) == 6]
            nhit = sum(1 for z in arf1z if z == set(S))
            print("        equals an Arf-1 zero set? %d / 6 hit"
                  % nhit)
    deg, _anf = anf_degree(f)
    bf_is_hb = all(f[x ^ y] ^ f[x] ^ f[y] == HT[x][y]
                   for x in range(16) for y in range(16))
    print("      algebraic degree (ANF) = %d; bilinear form "
          "b_f == hb (register form)? %s"
          % (deg, "YES" if bf_is_hb else "no"))
    in_refs = tuple(f) in set(refs)
    print("      f is one of the 16 quadratic refinements "
          "(one Sp(4,2)/translate family, v888)? %s"
          % ("YES" if in_refs else "no"))
    if qstar is not None:
        dq = sum(1 for x in range(16) if f[x] != qstar[x])
        dmin = min(sum(1 for x in range(16) if f[x] != q[x])
                   for q in refs)
        print("      Hamming distance: d(f, q*) = %d; min over "
              "the 16 refinements = %d" % (dq, dmin))
    if is_bent:
        fdual = [0 if W[u] == 4 else 1 for u in range(16)]
        print("      Walsh sign pattern -> dual bent f~ = %s"
              % fdual)
        zd = [u for u in range(16) if fdual[u] == 0]
        print("      dual level set |f~^-1(0)| = %d %s"
              % (len(zd), zd))
        if len(zd) == 6:
            repsd = diffset_census(zd)
            valsd = sorted(set(repsd.values()))
            print("        dual (16,6,2) difference set? %s "
                  "(rep counts %s)"
                  % ("YES" if valsd == [2] else "NO", valsd))
    else:
        print("      (rule not exactly bent -- no dual bent "
              "function exists; dual census skipped)")


# --------------------------------------------------------------- main
def binarize_world(rungs, label, min_steps):
    """Both rules on one world; returns the typed summary."""
    out = dict(label=label)
    bits_a, med_a, n_pairs = rule_a(rungs)
    bits_b, prof, used, kstar, kratio, thr = rule_b(rungs)
    out["n_pairs_a"] = n_pairs
    out["used_b"] = used
    out["n_steps_b16"] = used.get(16, 0)
    out["dead_a"] = n_pairs < min_steps
    out["dead_b"] = used.get(16, 0) < min_steps
    out["bits_a"], out["bits_b"] = bits_a, bits_b
    out["med_a"], out["prof"] = med_a, prof
    out["kstar"], out["thr"] = kstar, thr
    out["kratio"] = kratio
    Wa, Wb = walsh_spec(bits_a), walsh_spec(bits_b)
    out["Wa"], out["Wb"] = Wa, Wb
    out["flat_a"] = flatness(Wa) if not out["dead_a"] else None
    out["flat_b"] = flatness(Wb) if not out["dead_b"] else None
    out["bent_a"] = (not out["dead_a"]
                     and all(abs(w) == PRED_W_ABS for w in Wa))
    out["bent_b"] = (not out["dead_b"]
                     and all(abs(w) == PRED_W_ABS for w in Wb))
    return out


def main():
    section("PRIME.PORT.BENTCODE.01 -- the deep-core fingerprint "
            "as an explicit 16-point code vs the (16,6,2) bent "
            "predictions (EXPLORATION ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s"
          % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
    print("    PRE-REGISTERED (frozen inputs): |W| = %d on all 16 "
          "characters; off-peak autocorrelation = %d on all 15 "
          "shifts; affine distance = %d; rule agreement >= %d/16."
          % (PRED_W_ABS, PRED_AC_OFFPEAK, PRED_AFF_DIST,
             AGREE_BAR))
    print("    NO RH claim; no marker moves; no claim upgrades.")
    print("\nS0 -- firewall")
    check("S0.1 AST firewall clean", not ast_scan(BANNED_IDS))

    # ------------------------------------------------------------ W
    section("W -- pipeline wards (truth ladder, machinery "
            "verbatim; J16 = %s)" % (list(J16),))
    rungs, rk_max, n_err = build_ladder()
    print("    %d truth rungs, h %d .. %d; worst [Y,D_P] s3/s1 "
          "%.1e; %d construction skips  (%.1f s)"
          % (len(rungs), rungs[0]["h"] if rungs else -1,
             rungs[-1]["h"] if rungs else -1, rk_max, n_err,
             time.time() - T0))
    check("W1 >= %d truth rungs, rank-2 exact (max s3/s1 %.1e <= "
          "%.0e)" % (MIN_RUNGS, rk_max, RANK_BAR),
          len(rungs) >= MIN_RUNGS and rk_max <= RANK_BAR,
          "%d rungs" % len(rungs), kill="K1")

    truth = binarize_world(rungs, "TRUTH", 1)
    check("W2 >= %d truth full-J16 window pairs (rule A)"
          % MIN_PAIRS_A, truth["n_pairs_a"] >= MIN_PAIRS_A,
          "%d pairs" % truth["n_pairs_a"], kill="K1")
    check("W3 >= %d truth steps with the full J16 port prefix "
          "(rule B, m = 16)" % MIN_STEPS_B16,
          truth["n_steps_b16"] >= MIN_STEPS_B16,
          "%d steps" % truth["n_steps_b16"], kill="K1")
    p8 = truth["prof"].get(8)
    check("W4 deep-core certificate reproduces: prof(8) = %s <= "
          "%.0e (anatomy C1.1 on the named core {2..16})"
          % ("%.2e" % p8 if p8 is not None else "n/a", DC_CERT),
          p8 is not None and p8 <= DC_CERT, kill="K1")

    # ------------------------------------------------------------ B1
    section("B1 -- THE BINARIZATION (two independent frozen "
            "rules)")
    print("  RULE A (dangerous-direction increment sign; %d "
          "pairs):" % truth["n_pairs_a"])
    print("    %-8s %-8s %-14s %s"
          % ("alias j", "addr x", "median c_j", "bit"))
    for m, j in enumerate(J16, start=1):
        mv = truth["med_a"][j]
        print("    %-8d %-8s %-14s %d"
              % (j, format(m - 1, "04b"),
                 "%+.3e" % mv if mv is not None else "n/a",
                 truth["bits_a"][m - 1]))
    print("\n  RULE B (coherence profile / knee threshold):")
    print("    %-4s %-10s %-8s" % ("m", "prof(m)", "steps"))
    for m in range(4, 17):
        v = truth["prof"].get(m)
        print("    %-4d %-10s %-8d"
              % (m, "%.2e" % v if v is not None else "n/a",
                 truth["used_b"].get(m, 0)))
    print("    knee: k* = %s (jump x%.1f)   THR = %.3e "
          "(anatomy cross-ref: k* = 10 on the coarse grid)"
          % (truth["kstar"], truth["kratio"], truth["thr"]))
    print("    %-8s %-8s %-12s %s"
          % ("alias j", "addr x", "prof(entry)", "bit"))
    for m, j in enumerate(J16, start=1):
        e = max(m, 4)
        v = truth["prof"].get(e)
        print("    %-8d %-8s %-12s %d"
              % (j, format(m - 1, "04b"),
                 "%.2e" % v if v is not None else "n/a",
                 truth["bits_b"][m - 1]))
    fa = "".join(str(b) for b in truth["bits_a"])
    fb = "".join(str(b) for b in truth["bits_b"])
    agree = sum(1 for a, b in zip(truth["bits_a"],
                                  truth["bits_b"]) if a == b)
    print("\n    boolean tables (address order x = 0..15):")
    print("      f_A = %s  (weight %d)" % (fa, fa.count("1")))
    print("      f_B = %s  (weight %d)" % (fb, fb.count("1")))
    print("      complement agreement (report only): %d/16"
          % (16 - agree))
    code_lbl = ("CODE-CONSISTENT(%d)" % agree if agree >= AGREE_BAR
                else "CODE-ARTIFACT(%d)" % agree)
    check("B1.1 typed: %s (agreement %d/16, bar %d)"
          % (code_lbl, agree, AGREE_BAR), True)

    # ------------------------------------------------------------ B2
    section("B2 -- THE THREE INVARIANTS (exact integers) vs the "
            "pre-registered %d / %d / %d"
            % (PRED_W_ABS, PRED_AC_OFFPEAK, PRED_AFF_DIST))
    rule_labels = {}
    for tag, bits, W in (("A", truth["bits_a"], truth["Wa"]),
                         ("B", truth["bits_b"], truth["Wb"])):
        lbl, n4 = spectrum_label(W)
        rule_labels[tag] = (lbl, n4)
        ac = autocorr(bits)
        ad = affine_dist(bits)
        dev = [u for u in range(16) if abs(W[u]) != PRED_W_ABS]
        print("  RULE %s:" % tag)
        print("    Walsh spectrum W(u), u = 0..15: %s" % (W,))
        print("    |W| = %d census: %d/16; flatness ratio "
              "max|W|/min|W| = %s; deviating characters %s"
              % (PRED_W_ABS, n4, fmt_flat(flatness(W)), dev))
        offp = ac[1:]
        print("    autocorrelation r(a), a = 1..15: %s" % (offp,))
        print("    off-peak zero census: %d/15 (predicted 15/15)"
              % sum(1 for r in offp if r == PRED_AC_OFFPEAK))
        print("    affine distance = %d (predicted %d)"
              % (ad, PRED_AFF_DIST))
        check("B2.%s typed: rule %s spectrum %s (%d/16 at |W|=%d)"
              % (tag, tag, lbl, n4, PRED_W_ABS), True)
    if (rule_labels["A"][0] == "BENT"
            and rule_labels["B"][0] == "BENT"
            and agree >= AGREE_BAR):
        bent_lbl = "BENT-EXACT"
    elif "BENT" in (rule_labels["A"][0], rule_labels["B"][0]) \
            or "NEAR" in (rule_labels["A"][0],
                          rule_labels["B"][0]):
        bent_lbl = ("BENT-NEAR(A=%s:%d, B=%s:%d)"
                    % (rule_labels["A"][0], rule_labels["A"][1],
                       rule_labels["B"][0], rule_labels["B"][1]))
    else:
        bent_lbl = "BENT-DEAD"
    check("B2.3 typed: %s" % bent_lbl, True)

    # ------------------------------------------------------------ B3
    section("B3 -- STRUCTURAL FOLLOW-ON (only if BENT-EXACT / "
            "BENT-NEAR)")
    if bent_lbl != "BENT-DEAD":
        refs, qstar = qstar_selector()
        print("    q* selector rebuilt (v845 verbatim): %d "
              "refinements, q* %s"
              % (len(refs), "unique" if qstar else "NOT unique"))
        for tag, bits, W in (("A", truth["bits_a"], truth["Wa"]),
                             ("B", truth["bits_b"], truth["Wb"])):
            if rule_labels[tag][0] in ("BENT", "NEAR"):
                b3_report(bits, tag, refs, qstar,
                          rule_labels[tag][0] == "BENT", W)
        check("B3.1 structural follow-on reported", True)
    else:
        print("    skipped (frozen: B3 only on BENT-EXACT or "
              "BENT-NEAR; verdict is BENT-DEAD)")
        check("B3.1 skipped per frozen rule", True)

    # ------------------------------------------------------------ C
    section("C -- CONTROLS (four surgical worlds, identical "
            "frozen rules)")
    worlds = []
    for name, wfn, sseed in (("SMOOTH-MASS", world_smooth, None),
                             ("WRONG-LAMBDA", world_wrong_lambda,
                              None),
                             ("ATOMS-ONLY", world_atoms_only,
                              None),
                             ("SCRAMBLE", None, 1)):
        t1 = time.time()
        w_rungs, _rk, w_err = build_ladder(world_fn=wfn,
                                           scramble_seed=sseed)
        w = binarize_world(w_rungs, name, CTRL_MIN_STEPS)
        w["n_rungs"] = len(w_rungs)
        w["n_err"] = w_err
        worlds.append(w)
        print("    %-13s %d rungs (%d skips), ruleA %d pairs%s, "
              "ruleB %d m16-steps%s  (%.0f s)"
              % (name, len(w_rungs), w_err, w["n_pairs_a"],
                 " FRAME-DEAD" if w["dead_a"] else "",
                 w["n_steps_b16"],
                 " FRAME-DEAD" if w["dead_b"] else "",
                 time.time() - t1), flush=True)

    print("\n  C2 scramble frame death (kz %d, seed 1) -- must "
          "fire:" % CTRL_KZ)
    try:
        rc = rung_all(CTRL_KZ, scramble_seed=1, need_frame=True)
    except Exception as exc:
        rc = "RAISED(%s)" % type(exc).__name__
    if not isinstance(rc, dict):
        fired = True
        print("    scramble: rung not built (%r) -> FRAME DIES"
              % (rc,))
    elif "lamC" not in rc:
        fired = True
        print("    scramble: J16 window unavailable -> FRAME DIES")
    else:
        fired = (rc["lamO"] > 1.0) or (rc["lamC"] > 1.0)
        print("    scramble: lam(out) %.3e | lam(C_J16) %.3e -> %s"
              % (rc["lamO"], rc["lamC"],
                 "fires" if fired else "SILENT"))
    check("W6 scramble frame death fires", fired, kill="K1")

    sm = next(w for w in worlds if w["label"] == "SMOOTH-MASS")
    sm8 = sm["prof"].get(8)
    check("W5 smooth kill reproduces: smooth prof(8) = %s > %.2f "
          "or unmeasurable"
          % ("%.2e" % sm8 if sm8 is not None else "n/a", DC_DEAD),
          sm8 is None or sm8 > DC_DEAD, kill="K1")

    print("\n    THE CONTROL TABLE (flatness ratio max|W|/min|W|; "
          "frozen prediction: truth minimal, every control "
          "non-bent):")
    print("    %-13s %-6s %-10s %-6s %-10s %s"
          % ("world", "fA", "flat(A)", "fB", "flat(B)", "bent?"))
    print("    %-13s %-6s %-10s %-6s %-10s A:%s B:%s"
          % ("TRUTH", "w%d" % sum(truth["bits_a"]),
             fmt_flat(truth["flat_a"]),
             "w%d" % sum(truth["bits_b"]),
             fmt_flat(truth["flat_b"]),
             truth["bent_a"], truth["bent_b"]))
    any_ctrl_bent = False
    for w in worlds:
        fl_a = "FRAME-DEAD" if w["dead_a"] \
            else fmt_flat(w["flat_a"])
        fl_b = "FRAME-DEAD" if w["dead_b"] \
            else fmt_flat(w["flat_b"])
        print("    %-13s %-6s %-10s %-6s %-10s A:%s B:%s"
              % (w["label"], "w%d" % sum(w["bits_a"]), fl_a,
                 "w%d" % sum(w["bits_b"]), fl_b,
                 w["bent_a"], w["bent_b"]))
        any_ctrl_bent = any_ctrl_bent or w["bent_a"] \
            or w["bent_b"]
    check("C1 no control world is exactly bent under either rule",
          not any_ctrl_bent, kill="K2")

    # ------------------------------------------------------------ V
    section("V -- FROZEN VERDICT")
    n_pass = sum(1 for _n, okk in CHECKS if okk)
    n_tot = len(CHECKS)
    if KILLS:
        VERDICT = {"K1": "PIPELINE-BROKEN",
                   "K2": "CONTROL-DEAD"}[KILLS[0]]
        print("\n  VERDICT: %s" % VERDICT)
    else:
        VERDICT = ("BENTCODE-MEASURED / %s / %s"
                   % (bent_lbl, code_lbl))
        print("\n  VERDICT: %s" % VERDICT)
        print("  (f_A = %s, f_B = %s; agreement %d/16; truth "
              "flatness A %s / B %s; predictions |W|=%d / ac=%d "
              "/ dist=%d)"
              % (fa, fb, agree, fmt_flat(truth["flat_a"]),
                 fmt_flat(truth["flat_b"]), PRED_W_ABS,
                 PRED_AC_OFFPEAK, PRED_AFF_DIST))
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed"
          % (time.time() - T0, n_tot, n_tot - n_pass))
    return 0 if n_pass == n_tot else 1


if __name__ == "__main__":
    raise SystemExit(main())
