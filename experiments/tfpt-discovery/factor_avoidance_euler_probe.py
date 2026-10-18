#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""factor_avoidance_euler_probe -- PRIME.PORT.FACTORAVOID.01
(EXPLORATION ONLY, experiments/; round 50, follow-up (b) of the
tau_mobius_factor run: WHY does the truth ladder keep every
determinant factor away from -1 while every smooth-world control
crosses?  Factor anatomy vs the exact Euler cascade structure.
2026-08-09.)

THE QUESTION (frozen): tau_mobius_factor_probe measured the exact
factorization Q_h = det(W_{h+1})/det(W_h) = prod_i (1 + mu_i),
mu_i = eig(W_h^{-1} Delta C) on the 12x12 window (truth: 0
crossings on 31/31 steps, min 1+mu = 0.0050; smooth-mass world:
crossings on 22/28 steps, first at h 210->218).  The rung
increment Delta C is driven by (i) window geometry change
(alpha, D, M shift) and (ii) the entering/leaving prime atoms
(euler_scattering: the window comb IS the tent-weighted
per-prime Blaschke cascade, bitwise).  Three candidate anatomies
for the truth's factor avoidance: (A) SIZE -- a norm bound
rho(W^{-1} Delta C) < 1 per step; (B) STRUCTURE -- rho > 1
sometimes but the crossings still avoided; (C) CANCELLATION
between the geometry part and the atom part.

THE MINI-THEOREM (stated up front; elementary): let W_h = I - C_J
be symmetric POSITIVE DEFINITE and Delta C symmetric, with
W_{h+1} = W_h + Delta C.  Then W_h^{-1} Delta C is similar to the
SYMMETRIC matrix S = W_h^{-1/2} Delta C W_h^{-1/2}, so its
eigenvalues mu_i are REAL, and W_{h+1} = W_h^{1/2} (I + S)
W_h^{1/2}.  Hence
    rho(W_h^{-1} Delta C) < 1
      ==>  every mu_i lies in (-1, 1)
      ==>  every factor 1 + mu_i > 0
      ==>  Q_h > 0  AND  W_{h+1} is again positive definite --
positivity inheritance in ONE step, from ONE norm bound.
Conversely a factor crossing (some 1 + mu_i < 0) forces
rho >= |mu_i| > 1.  (Remark for the indefinite branch: for REAL
W_h the mu-spectrum is closed under conjugation, so rho < 1
still forces Q_h = prod(1 + mu_i) > 0 -- real mu in (-1, 1) give
positive factors, complex ones pair into |1 + mu|^2 -- but the
PD inheritance needs W_h PD.)  If the truth ladder has rho < 1
on every step, the induction theorem shape is a NORM BOUND on
W^{-1} Delta C; the ONE-SIDED weakening min_i mu_i > -1 is
exactly PD inheritance itself (no norm reduction).

THE LADDER (frozen, tau_mobius_factor verbatim): all frame-A
zones (core.frame_a_zones()) with h <= 900, sorted by (h, kz);
consecutive FULL-WINDOW pairs (both rungs carry all 12 indices
of J = {2, 4, ..., 24}; typed skips counted); truth + smooth-
mass world (B1 LATTICE-SMOOTH masses m_n = 2 e^{u_n/2} du_n,
midpoint cells, lattice_parametrix verbatim); Epstein/scramble
frame status reported (C1).

FROZEN PROTOCOL (2026-08-09; all bars frozen before the run):

 A0  REPRODUCTION WARD (kill -> WARD-BROKEN): the tau_mobius
     T1/C2 census must reproduce at print precision: truth 31
     full-window pairs, 0 crossing steps, ladder min(1 + mu) =
     0.0050 (tol 5.001e-5); smooth 28 full-window pairs, 22
     crossing steps (Q < 0 or a real factor < 0), first
     crossing at h 210 -> 218, Q < 0 count == predecessor
     ledger.  Factorization ward |prod(1 + mu) - Q| <= 1e-10
     rel on truth (kill), <= 1e-8 on smooth (report).

 A1  THE NORM LEDGER: per full-window step, in the exact
     symmetric gauge (truth; PD branch) or the general eigen
     branch (smooth, W possibly indefinite):
       rho = rho(W_h^{-1} Delta C),  ||W_h^{-1}||_2,
       ||Delta C||_2, and the naive product bound
       ||W_h^{-1}||_2 ||Delta C||_2 >= rho;
     plus the atom-flow direction of the step (ENTER/LEAVE,
     from the deployed prefix law).  CENSUS: (i) truth -- is
     rho < 1 on ALL steps (then Q > 0 AND PD inheritance follow
     algebraically per step by the mini-theorem)?  The
     ONE-SIDED census printed separately: max_steps(-min mu)
     (the dangerous side) vs max_steps(max mu) (the harmless
     side).  (ii) smooth -- the crossing correspondence table:
     per step, rho vs the crossing flag; the 2x2 census
     (crossing x rho >= 1).  Crossing ==> rho > 1 is automatic
     (theorem); the informative cell is rho >= 1 WITHOUT
     crossing (the harmless mu > +1 side, counted per world).

 A2  THE DECOMPOSITION (geometry vs atoms): the deployed atom
     set at zone kz is the exact PREFIX U_ALL[:ka(alpha)], so
     between consecutive rungs a suffix block of prime-power
     atoms ENTERS (alpha up) or LEAVES (alpha down).  FROZEN
     CONSTRUCTION: hybrid H = rung (h+1)'s window geometry
     (alpha, M, D of zone b) with rung h's atom SET (comb
     override, deployed builder path bit for bit); split
       Delta_geom  := C_J(a) - C_J(H)
       Delta_atoms := C_J(H) - C_J(b);
     TELESCOPING WARD (kill -> WARD-BROKEN): ||Delta_geom +
     Delta_atoms - Delta C||_F <= 1e-10 * max(1, ||C_J(a)||_F)
     on every step where H builds.  Per step where both parts
     are nonzero: rho_geom, rho_atoms (A1 gauge), alignment
     cos<S_geom, S_atoms>_F in the symmetric gauge, and the
     cancellation index rho_tot / (rho_geom + rho_atoms).

 A3  THE PER-PRIME GRAIN (the Euler question): frozen step
     subset = the 5 MEDIUM truth steps (the middle five of the
     truth full-window step list sorted by h) + the smooth
     world's FIRST crossing step.  Atoms grouped by base prime
     p (positions are log p^k; base recovered by own trial
     division -- v882 own-sieve precedent; every atom MUST
     parse as a prime power, ward).  Per-prime anatomy of the
     step increment (SPEC v2 object, see amendments): the
     LEAVE-ONE-PRIME-OUT response
       Delta_p := (C_a - C_b) - (C_a^{-p} - C_b^{-p}),
     C^{-p} = the rung rebuilt with prime p's full atom group
     deleted (deployed builder, comb override; each world's
     mass convention), for the NP_TOP = 8 largest in-window-
     mass primes of the union prefix; rho_p in the A1 gauge vs
     the step's W_a; the additivity defect ||Delta C - sum_p
     Delta_p||_F / ||Delta C||_F reported (nonlinear
     interaction share, no exactness claimed).  GRAIN TYPE per
     step (frozen bars, SPEC v3 validity precondition): the
     typing REQUIRES a decompositional response -- at least
     NP_TOP/2 = 4 surviving leave-outs (else
     GRAIN-UNDERSAMPLED) and additivity defect <= 1 (else
     GRAIN-NONDECOMPOSITIONAL: the responses are then a
     LEVERAGE census of the window operators, not a
     decomposition of the increment, and are reported as
     such).  Where valid: with top share = max_p rho_p /
     sum_p rho_p over the resolved primes -- GRAIN-DIFFUSE iff
     top share <= 0.5; GRAIN-COHERENT iff >= 0.8; else
     GRAIN-INTERMEDIATE; single share = max_p rho_p / rho_tot
     printed.  Leave-out builds that die are typed
     LEAVEOUT-DEAD (skipped, counted).

 A4  TYPED VERDICT SUBLABELS (frozen bars): with f = fraction
     of truth steps with rho < 1:  AVOIDANCE-NORM iff f = 1
     (the theorem shape exists); AVOIDANCE-MIXED iff
     0.9 <= f < 1; AVOIDANCE-STRUCTURAL iff f < 0.9 (avoided
     without the norm bound -- subtler); plus the A2 split
     labels and the A3 grain labels.

 C   CONTROLS: (C1, kz 9, must fire, kill -> CONTROL-DEAD)
     Epstein (lambda_eps recursion comb) + scramble (seed 1):
     the compressed frame must die (exterior supercritical OR
     lam(C_J) > 1 OR window unavailable); channel reported.
     (C2) the SMOOTH-MASS world is the PRIMARY embedded control
     here; its detection (crossings present) is ward-anchored
     in A0 -- if the smooth ladder shows no crossing the probe
     is CONTROL-DEAD.

 W   PIPELINE WARDS (kill -> PIPELINE-BROKEN): W1 >= 30 truth
     rungs; W1b the atom prefix law exact; W2 det(W) > 0 on
     every truth full-window rung; W3 >= 20 truth full-window
     pairs; W4 the A2 construction DECIDED on every truth step
     (exact split computed, or hybrid frame death recorded
     with its channel).

KILLS: K1 pipeline ward breaks -> PIPELINE-BROKEN; KW the
factorization / reproduction / telescoping / grain-parse ward
breaks -> WARD-BROKEN; K3 controls silent -> CONTROL-DEAD.

VERDICT (frozen enum): FACTORAVOID-MEASURED with typed sublabels
AVOIDANCE-NORM / AVOIDANCE-MIXED / AVOIDANCE-STRUCTURAL (A4),
the A2 split labels, the A3 grain labels; else PIPELINE-BROKEN /
WARD-BROKEN / CONTROL-DEAD.

SPEC v2 (2026-08-09, after run 1; fail-first preserved -- every
run-1 measurement stands, no bar was moved to rescue a failing
measurement; two ward anchors and one degenerate-object
bookkeeping were amended, documented here):

 (i)   A0.3 Q < 0 count: the round-50 brief said "Q flips 13x";
       the predecessor's PRINTED C2 ledger (re-run, matched row
       for row against this probe's smooth table, identical Q
       values) has Q < 0 on 16 of 28 steps.  The ward is
       anchored to the verified predecessor output:
       REF_SMOOTH_QNEG = 16.  All other reference numbers
       (31/0/0.0050; 28/22/210->218) confirmed unchanged.

 (ii)  A2 DEGENERACY DISCOVERED (run 1, kept as the measured
       answer): the deployed atoms_in cutoff (u <= 2 alpha) is
       SLAVED to the tent support edge (atom_lags_at uses
       D = 2 alpha / M, so cells cover exactly [0, 2 alpha],
       and an atom at u > 2 alpha contributes EXACTLY ZERO
       weight).  Consequences, both measured in run 1: on every
       LEAVING step Delta_atoms == 0 BITWISE (the moving atoms
       are invisible to the smaller window -- hybrid H equals
       rung b's build bit for bit), and on every ENTERING step
       the hybrid H (grown window WITHOUT its new atoms) FRAME-
       DIES -- the grown window cannot even be built without
       its new atoms.  There is NO separable atom channel:
       option (C) CANCELLATION is structurally dead; the whole
       increment is the geometry re-test of the full comb.  v2
       therefore replaces the v1 dominance/alignment/
       cancellation ladder labels (meaningless on a one-channel
       ladder) by the per-step trichotomy ATOM-NIL /
       FRAME-REQUIRES-ATOMS / SPLIT-NONDEGENERATE with
       censuses (any nondegenerate step still gets the full v1
       row), and W4 becomes the decision census above.  Run-1
       v1-W4 ("split available on >= 0.8") is superseded as a
       bookkeeping error: hybrid frame death IS a decision, not
       a pipeline failure.

 (iii) A3 OBJECT REPLACED (documented): the v1 cumulative
       per-prime ladder of the moving block is answered
       EXACTLY by (ii): the moving atoms carry ZERO of the
       increment through their own tents (leaving steps:
       bitwise zero, verified in run 1 -- all rho_p = 0,
       endpoint dev 0.0e0; entering steps: baseline frame-
       dead).  That IS the Euler-grain answer to the as-posed
       question, and it is printed.  The per-prime anatomy is
       re-posed in the one surviving nondegenerate sense: the
       LEAVE-ONE-PRIME-OUT step response defined in A3 above.
       The v1 cumulative machinery and its telescoping ward
       are retired with it; the parse ward stays.

SPEC v3 (2026-08-09, after run 2; fail-first preserved -- every
run-2 raw number stands and is reprinted unchanged):

 (iv)  A3 GRAIN TYPING gains the decomposition-validity
       precondition stated in A3 above.  Run 2 measured the
       leave-out responses to be NON-DECOMPOSITIONAL: on the
       truth steps sum_p rho_p ~ 1e4 against rho_tot ~ 1-4 and
       additivity defect ~ 1e3 (removing ONE small prime moves
       the window operators by orders of magnitude more than
       the whole step increment -- the response is frame
       leverage, not increment grain), and on the smooth
       crossing step 5 of 8 leave-outs frame-died (defect 8.2,
       3 survivors).  The v2 labels GRAIN-DIFFUSE /
       GRAIN-COHERENT computed on these responses are VOIDED
       as bookkeeping (they typed shares of the wrong object);
       v3 types them GRAIN-NONDECOMPOSITIONAL /
       GRAIN-UNDERSAMPLED and keeps the numbers as a leverage
       census.  THE HONEST A3 ANSWER: the per-prime grain of
       the step increment is NOT accessible in the deployed
       nonlinear pipeline -- the moving-block channel is
       exactly nil (v1/A2), and single-prime deletions do not
       linearize; avoidance and crossing are properties of the
       COLLECTIVE window re-test, not of any single prime's
       move.

 (v)   A2 smooth-world bookkeeping note: 5 smooth LEAVING
       steps type SPLIT-NONDEGENERATE with a TINY atom part
       (||Delta_atoms||_F ~ 1e-12..1e-11, rho_atom ~ 1e-10..
       1e-8): the
       B1 smooth masses are recomputed per lattice (midpoint
       cells), so deleting the moving suffix shifts the LAST
       retained cell's width -- a boundary-cell mass artifact
       of the smooth convention, not a tent contribution of
       the moving atoms (truth masses are per-atom, hence
       bitwise ATOM-NIL there).  Printed with ||Delta_atoms||
       so the scale is visible.

NO RH claim -- a per-step spectral measurement on compressed
window truncations is a statement about the deployed ladder,
not a theorem about zeros.

FIREWALL: no zeros, no prime oracles (AST scan; banned ids
zetazero / nzeros / primerange / isprime / primepi / nextprime /
prevprime); the A3 grouping uses an OWN trial-division smallest-
prime-factor routine (allowed, v882 own-sieve precedent),
documented here; v563 READ-ONLY; RNG only inside the declared
scramble control; stdout only.  No marker moves.

Sources (read-only): v563_paper2_readouts (U_ALL / MU_ALL prefix
law, build_window, atom_lags_at, arch_lags -- read verbatim);
window compression + exact quotient factorization + smooth-mass
world verbatim from tau_mobius_factor_probe.py
(PRIME.PORT.TAU.MOEBIUS.01) via port_schur_cocycle_probe.py and
lattice_parametrix_probe.py (B1); euler_scattering_source_probe
(PRIME.EULER.SCATTER.01: the atom table IS the Euler grouping,
exact -- the license for the per-prime grain).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/factor_avoidance_euler_probe.py
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
MIN_RUNGS = 30
MIN_PAIRS_T1 = 20
MIN_COMMON_J = 8
FACT_WARD = 1e-10           # truth factorization ward (kill)
FACT_WARD_SMOOTH = 1e-8     # smooth factorization ward (report)
SPLIT_WARD = 1e-10          # A2 telescoping ward (kill)
NP_TOP = 8                  # A3 leave-out primes
MEDIUM_N = 5                # A3 medium truth steps
GRAIN_DIFFUSE_BAR = 0.5     # A3
GRAIN_COHERENT_BAR = 0.8    # A3
DEFECT_BAR = 1.0            # A3 v3 decomposition-validity bar
MIN_LO_ALIVE = NP_TOP // 2  # A3 v3 undersampling bar
MIXED_FRAC = 0.9            # A4
CTRL_KZ = 9
BANNED_IDS = ("zetazero", "nzeros", "primerange", "isprime",
              "primepi", "nextprime", "prevprime")

# A0 reproduction ward (tau_mobius_factor_probe printed ledger,
# re-verified; SPEC v2 (i))
REF_N_TRUTH_PAIRS = 31
REF_TRUTH_CROSS = 0
REF_TRUTH_MINFAC = 0.0050
REF_N_SMOOTH_PAIRS = 28
REF_SMOOTH_CROSS = 22
REF_SMOOTH_FIRST = (210, 218)
REF_SMOOTH_QNEG = 16
ROUND_TOL = 5.001e-5

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


# --------- pipeline, verbatim from tau_mobius_factor_probe
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
    """One rung -> 12x12 window compression (tau_mobius_factor
    rung_all verbatim, MINUS the dressed-port/IIKS block which
    does not feed C_J)."""
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


# ------------------------------------------- factor machinery
def logdet_sgn(W):
    sgn, ld = np.linalg.slogdet(W)
    return float(sgn), float(ld)


def pd_gauge(Wa):
    """W_a^{-1/2} for symmetric PD W_a, else None."""
    ew, Vw = np.linalg.eigh(Wa)
    if ew[0] <= 0.0:
        return None, ew
    return Vw @ np.diag(ew ** -0.5) @ Vw.T, ew


def sym_mu(Wisq, D):
    """Exact real spectrum of W^{-1}D in the symmetric gauge."""
    S = Wisq @ D @ Wisq
    return np.linalg.eigvalsh(0.5 * (S + S.T))


def gen_mu(Wa, D):
    """General (complex-capable) spectrum of Wa^{-1} D."""
    try:
        return np.linalg.eig(np.linalg.solve(Wa, D))[0]
    except np.linalg.LinAlgError:
        return None


def mu_stats(mu):
    """(rho, min real factor, max real mu, n real fac < 0, near)."""
    mu = np.asarray(mu, complex)
    rho = float(np.max(np.abs(mu))) if len(mu) else 0.0
    real_m = np.abs(mu.imag) <= 1e-9 * (1.0 + np.abs(mu))
    mur = mu.real[real_m]
    fac_r = 1.0 + mur
    mn = float(np.min(fac_r)) if len(fac_r) else float("nan")
    mx = float(np.max(mur)) if len(mur) else float("nan")
    return (rho, mn, mx, int(np.sum(fac_r < 0.0)),
            int(np.sum(np.abs(fac_r) < 0.1)))


def quart(v):
    q = np.percentile(np.asarray(v, float), [25, 50, 75])
    return "q25 %.4f  med %.4f  q75 %.4f" % tuple(q)


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


# ------------------------------------------------------------- pairs
def factor_pairs(rungs, rrs, general=False):
    """Consecutive full-window pairs with the exact factorization
    + the A1 norm ledger.  Rows keep rung references for A2/A3."""
    rows = []
    n_skip = 0
    for k, (ra, rb) in enumerate(zip(rungs[:-1], rungs[1:])):
        if not (ra.get("full") and rb.get("full")):
            n_skip += 1
            continue
        n = len(JWIN)
        Wa = np.eye(n) - ra["CJ"]
        Wb = np.eye(n) - rb["CJ"]
        sga, lda = logdet_sgn(Wa)
        sgb, ldb = logdet_sgn(Wb)
        Q = sga * sgb * math.exp(ldb - lda)
        DC = ra["CJ"] - rb["CJ"]           # W_b = W_a + DC
        Wisq, ewa = pd_gauge(Wa)
        if general or Wisq is None:
            mu = gen_mu(Wa, DC)
            if mu is None:
                n_skip += 1
                continue
            gauge = "GEN"
        else:
            mu = sym_mu(Wisq, DC)
            gauge = "SYM"
        prod = complex(np.prod(1.0 + np.asarray(mu, complex)))
        dev = abs(prod - Q) / max(abs(Q), 1e-300)
        rho, min_fac, max_mu, n_neg, n_near = mu_stats(mu)
        winv = 1.0 / float(np.min(np.abs(ewa)))
        dcn = float(np.max(np.abs(np.linalg.eigvalsh(
            0.5 * (DC + DC.T)))))
        ka = int(rrs[ra["kz"]]["n_atom"])
        kb = int(rrs[rb["kz"]]["n_atom"])
        rows.append(dict(
            k=k, ra=ra, rb=rb, ha=ra["h"], hb=rb["h"],
            kza=ra["kz"], kzb=rb["kz"], ka=ka, kb=kb,
            flow=("ENTER" if kb > ka else
                  "LEAVE" if kb < ka else "NONE"),
            Q=Q, dev=dev, rho=rho, min_fac=min_fac,
            max_mu=max_mu, n_neg=n_neg, n_near=n_near,
            winv=winv, dcn=dcn, bound=winv * dcn,
            Wisq=Wisq, Wa=Wa, DC=DC, gauge=gauge,
            pd=bool(Wisq is not None),
            cross=bool(Q < 0.0 or (np.isfinite(min_fac)
                                   and min_fac < 0.0))))
    return rows, n_skip


def part_rho(row, D):
    """rho of W_a^{-1} D in the row's A1 gauge."""
    if row["gauge"] == "SYM":
        mu = sym_mu(row["Wisq"], D)
    else:
        mu = gen_mu(row["Wa"], D)
        if mu is None:
            return float("nan")
    return float(np.max(np.abs(mu))) if len(mu) else 0.0


def align_cos(row, Dg, Da):
    """Alignment cosine (symmetric gauge if PD, else raw)."""
    if row["gauge"] == "SYM":
        Sg = row["Wisq"] @ Dg @ row["Wisq"]
        Sa = row["Wisq"] @ Da @ row["Wisq"]
    else:
        Sg, Sa = Dg, Da
    ng = float(np.linalg.norm(Sg))
    na = float(np.linalg.norm(Sa))
    if ng <= 0.0 or na <= 0.0:
        return float("nan")
    return float(np.sum(Sg * Sa) / (ng * na))


def comb_of(idx_set, world):
    """Comb arrays for an index set into U_ALL (frozen: truth =
    deployed masses; smooth = B1 masses recomputed on the set's
    own lattice, the per-rung smooth convention)."""
    ii = np.array(sorted(idx_set), dtype=int)
    uu = np.asarray(core.U_ALL, float)[ii]
    if world == "truth":
        return uu, np.asarray(core.MU_ALL, float)[ii]
    return uu, smooth_masses(uu)


def death_channel(hy):
    """Classify a failed hybrid/leave-out build."""
    if not isinstance(hy, dict):
        return "CHAIN-DEATH"
    if "CJ" not in hy:
        return "WINDOW-LOST"
    if not hy.get("full"):
        return "PARTIAL-WINDOW"
    return None


def main():
    section("PRIME.PORT.FACTORAVOID.01 -- factor avoidance vs the "
            "Euler cascade anatomy (EXPLORATION ONLY)")
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
    check("W1 >= %d truth rungs built" % MIN_RUNGS,
          len(rungs) >= MIN_RUNGS, "%d rungs" % len(rungs),
          kill="K1")
    check("W1b atom prefix law exact (max |mm - MU_ALL prefix| "
          "%.1e == 0)" % pref_dev, pref_dev == 0.0, kill="K1")

    # ------------------------------------------------------- A0/A1
    trows, n_skip_t = factor_pairs(rungs, rrs, general=False)
    srows, n_skip_s = factor_pairs(srungs, rrs, general=True)
    section("A1 -- THE NORM LEDGER, truth (%d full-window pairs; "
            "%d typed skips)" % (len(trows), n_skip_t))
    print("    rho = rho(W_h^{-1} Delta C) in the exact "
          "symmetric gauge; bound = ||W^{-1}||_2 ||Delta C||_2")
    print("    step        flow    rho     rho<1  ||W^-1||    "
          "||dC||    bound     bnd<1  min(1+mu) max(mu)  near")
    for r in trows:
        print("    h %3d->%3d %-5s %8.4f  %-5s  %9.1f   %.5f  "
              "%9.1f  %-5s  %+.4f   %+8.3f   %d"
              % (r["ha"], r["hb"], r["flow"], r["rho"],
                 str(r["rho"] < 1.0), r["winv"], r["dcn"],
                 r["bound"], str(r["bound"] < 1.0),
                 r["min_fac"], r["max_mu"], r["n_near"]))
    pd_ok = all(r["pd"] for r in trows)
    check("W2 det(W) > 0 and W PD on every truth full-window "
          "rung (all pairs SYM gauge)", pd_ok, kill="K1")
    check("W3 >= %d truth full-window pairs" % MIN_PAIRS_T1,
          len(trows) >= MIN_PAIRS_T1, "%d" % len(trows),
          kill="K1")
    dev_max = float(np.max([r["dev"] for r in trows]))
    check("A0.1 truth factorization ward: max rel dev %.2e <= "
          "%.0e" % (dev_max, FACT_WARD), dev_max <= FACT_WARD,
          kill="KW")
    n_cross_t = sum(1 for r in trows if r["cross"])
    minfac_t = float(np.min([r["min_fac"] for r in trows]))
    check("A0.2 REPRODUCTION (truth): %d pairs == %d, %d "
          "crossings == %d, ladder min(1+mu) %.4f == %.4f "
          "(tol %.1e)"
          % (len(trows), REF_N_TRUTH_PAIRS, n_cross_t,
             REF_TRUTH_CROSS, minfac_t, REF_TRUTH_MINFAC,
             ROUND_TOL),
          len(trows) == REF_N_TRUTH_PAIRS
          and n_cross_t == REF_TRUTH_CROSS
          and abs(minfac_t - REF_TRUTH_MINFAC) <= ROUND_TOL,
          kill="KW")
    rho_t = np.array([r["rho"] for r in trows])
    n_lt1 = int(np.sum(rho_t < 1.0))
    n_bnd = sum(1 for r in trows if r["bound"] < 1.0)
    frac_lt1 = n_lt1 / float(len(trows))
    neg_side = float(np.max([1.0 - r["min_fac"] for r in trows]))
    pos_side = float(np.max([r["max_mu"] for r in trows]))
    n_harmless = sum(1 for r in trows
                     if r["rho"] >= 1.0 and r["min_fac"] > 0.0)
    print("\n    TRUTH CENSUS: rho < 1 on %d/%d steps (max rho "
          "%.4f); naive product bound < 1 on %d/%d"
          % (n_lt1, len(trows), float(np.max(rho_t)), n_bnd,
             len(trows)))
    print("    ONE-SIDED CENSUS: dangerous side max(-min mu) = "
          "%.4f (< 1 on ALL steps: %s); harmless side"
          % (neg_side, neg_side < 1.0))
    print("    max(mu) up to %+.3f; ALL %d rho >= 1 steps are "
          "harmless-side (min factor > 0 there: %s)"
          % (pos_side, len(trows) - n_lt1,
             n_harmless == len(trows) - n_lt1))
    print("    rho ladder: %s" % quart(rho_t))
    check("A1.1 truth rho census reported (rho < 1 on %d/%d)"
          % (n_lt1, len(trows)), True)

    section("A1 -- THE NORM LEDGER, smooth-mass world (%d pairs; "
            "%d typed skips) + crossing correspondence"
            % (len(srows), n_skip_s))
    print("    step        flow    rho     rho<1  W_a PD  "
          "min(1+mu)  cross  Q")
    for r in srows:
        print("    h %3d->%3d %-5s %9.4f %-5s  %-5s   %s   "
              "%-5s  %+.3e%s"
              % (r["ha"], r["hb"], r["flow"], r["rho"],
                 str(r["rho"] < 1.0), str(r["pd"]),
                 ("%+9.4f" % r["min_fac"])
                 if np.isfinite(r["min_fac"]) else "    n/a  ",
                 str(r["cross"]), r["Q"],
                 "  <-- CROSSING" if r["cross"] else ""))
    sdev_max = float(np.max([r["dev"] for r in srows]))
    print("    smooth factorization ward (general eig): max rel "
          "dev %.2e vs %.0e (%s)"
          % (sdev_max, FACT_WARD_SMOOTH,
             "ok" if sdev_max <= FACT_WARD_SMOOTH
             else "EXCEEDED -- reported"))
    n_cross_s = sum(1 for r in srows if r["cross"])
    n_qneg = sum(1 for r in srows if r["Q"] < 0.0)
    first_s = next((r for r in srows if r["cross"]), None)
    first_hh = ((first_s["ha"], first_s["hb"])
                if first_s is not None else (-1, -1))
    check("A0.3 REPRODUCTION (smooth): %d pairs == %d, %d "
          "crossing steps == %d, first at h %d->%d == %d->%d, "
          "Q < 0 on %d == %d (predecessor ledger, SPEC v2 (i))"
          % (len(srows), REF_N_SMOOTH_PAIRS, n_cross_s,
             REF_SMOOTH_CROSS, first_hh[0], first_hh[1],
             REF_SMOOTH_FIRST[0], REF_SMOOTH_FIRST[1],
             n_qneg, REF_SMOOTH_QNEG),
          len(srows) == REF_N_SMOOTH_PAIRS
          and n_cross_s == REF_SMOOTH_CROSS
          and first_hh == REF_SMOOTH_FIRST
          and n_qneg == REF_SMOOTH_QNEG, kill="KW")
    c11 = sum(1 for r in srows if r["cross"] and r["rho"] >= 1.0)
    c10 = sum(1 for r in srows if r["cross"] and r["rho"] < 1.0)
    c01 = sum(1 for r in srows
              if not r["cross"] and r["rho"] >= 1.0)
    c00 = sum(1 for r in srows
              if not r["cross"] and r["rho"] < 1.0)
    print("\n    2x2 CENSUS (smooth): cross & rho>=1: %d | cross "
          "& rho<1: %d | no-cross & rho>=1: %d | no-cross & "
          "rho<1: %d" % (c11, c10, c01, c00))
    print("    (crossing ==> rho > 1 is the theorem direction; "
          "the harmless cell is no-cross & rho>=1.)")
    check("A1.2 smooth correspondence: every crossing step has "
          "rho >= 1 (%d/%d)" % (c11, n_cross_s), c10 == 0)

    print("\n    THE MINI-THEOREM (stated): W_h symmetric PD + "
          "Delta C symmetric ==> mu real (symmetric")
    print("    similarity), and rho(W_h^{-1} Delta C) < 1 ==> "
          "every 1 + mu_i > 0 ==> Q_h > 0 AND W_{h+1} PD.")
    print("    A crossing forces rho > 1.  Truth rho < 1 "
          "everywhere would make avoidance a NORM BOUND.")

    # ------------------------------------------------------------ A2
    section("A2 -- THE DECOMPOSITION Delta C = Delta_geom + "
            "Delta_atoms (hybrid builds; SPEC v2 trichotomy)")
    print("    hybrid H = geometry(b) + atom set(a); Delta_geom "
          "= C(a) - C(H); Delta_atoms = C(H) - C(b)")

    def split_decide(rows, world):
        dec = []
        tel_max = 0.0
        for r in rows:
            ka = r["ka"]
            hy = rung_win(r["kzb"],
                          comb=comb_of(range(ka), world),
                          rr_cache=rrs[r["kzb"]])
            ch = death_channel(hy)
            if ch is not None:
                dec.append(dict(r=r, typ="FRAME-REQUIRES-ATOMS",
                                chan=ch))
                continue
            Dg = r["ra"]["CJ"] - hy["CJ"]
            Da = hy["CJ"] - r["rb"]["CJ"]
            tel_max = max(tel_max, float(
                np.linalg.norm(Dg + Da - r["DC"]))
                / max(1.0, float(np.linalg.norm(r["ra"]["CJ"]))))
            if float(np.linalg.norm(Da)) == 0.0:
                dec.append(dict(r=r, typ="ATOM-NIL", hyCJ=hy["CJ"],
                                Dg=Dg, Da=Da))
            else:
                dec.append(dict(
                    r=r, typ="SPLIT-NONDEGENERATE", hyCJ=hy["CJ"],
                    Dg=Dg, Da=Da, rg=part_rho(r, Dg),
                    ra_=part_rho(r, Da), al=align_cos(r, Dg, Da)))
        return dec, tel_max

    def split_report(name, rows, world):
        dec, tel_max = split_decide(rows, world)
        n_nil = sum(1 for d in dec if d["typ"] == "ATOM-NIL")
        n_dead = sum(1 for d in dec
                     if d["typ"] == "FRAME-REQUIRES-ATOMS")
        n_non = len(dec) - n_nil - n_dead
        print("\n    %s: %d steps -> ATOM-NIL %d | FRAME-"
              "REQUIRES-ATOMS %d | SPLIT-NONDEGENERATE %d"
              % (name, len(dec), n_nil, n_dead, n_non))
        for d in dec:
            r = d["r"]
            if d["typ"] == "FRAME-REQUIRES-ATOMS":
                print("    h %3d->%3d %-5s FRAME-REQUIRES-ATOMS "
                      "(%s): grown window w/o its new atoms "
                      "does not build"
                      % (r["ha"], r["hb"], r["flow"], d["chan"]))
            elif d["typ"] == "ATOM-NIL":
                print("    h %3d->%3d %-5s ATOM-NIL: "
                      "||Delta_atoms||_F == 0 bitwise; "
                      "rho_geom = rho_tot = %.4f"
                      % (r["ha"], r["hb"], r["flow"], r["rho"]))
            else:
                print("    h %3d->%3d %-5s NONDEGENERATE: "
                      "rho_geom %.4f rho_atom %.2e "
                      "(||Da|| %.1e) align %+.3f"
                      % (r["ha"], r["hb"], r["flow"], d["rg"],
                         d["ra_"],
                         float(np.linalg.norm(d["Da"])),
                         d["al"]))
        if n_non and world == "smooth":
            print("    (smooth NONDEGENERATE rows: boundary-"
                  "cell mass artifact of the per-lattice B1 "
                  "convention, SPEC v3 (v).)")
        return dec, tel_max, (n_nil, n_dead, n_non)

    tdec, tel_t, tcns = split_report("TRUTH", trows, "truth")
    sdec, tel_s, scns = split_report("SMOOTH", srows, "smooth")
    n_flow_mismatch = sum(
        1 for d in tdec + sdec
        if (d["typ"] == "ATOM-NIL" and d["r"]["flow"] == "ENTER")
        or (d["typ"] == "FRAME-REQUIRES-ATOMS"
            and d["r"]["flow"] == "LEAVE"))
    print("\n    STRUCTURAL STATEMENT (exact): the deployed atom "
          "cutoff u <= 2 alpha is SLAVED to the tent")
    print("    support edge M*D = 2 alpha, so a LEAVING block is "
          "invisible to the smaller window (atom part")
    print("    exactly zero) and an ENTERING block is load-"
          "bearing for the grown window (hybrid frame dies).")
    print("    There is NO separable atom channel; option (C) "
          "CANCELLATION is structurally dead.  Type/flow")
    print("    correspondence violated on %d steps."
          % n_flow_mismatch)
    check("W4 A2 decided on every step (truth %d + smooth %d)"
          % (len(tdec), len(sdec)),
          len(tdec) == len(trows) and len(sdec) == len(srows),
          kill="K1")
    tel_max = max(tel_t, tel_s)
    check("A2.1 TELESCOPING WARD (where H builds): max rel "
          "|Dg + Da - DC| %.2e <= %.0e" % (tel_max, SPLIT_WARD),
          tel_max <= SPLIT_WARD, kill="KW")
    a2_lab_t = ("SPLIT-DEGENERATE(nil %d, framedead %d)"
                % tcns[:2] if tcns[2] == 0
                else "SPLIT-PARTLY-NONDEGENERATE(%d)" % tcns[2])
    check("A2.2 truth split typed: %s" % a2_lab_t, True)

    # ------------------------------------------------------------ A3
    section("A3 -- THE PER-PRIME GRAIN (5 medium truth steps + "
            "the smooth first crossing step; SPEC v2 leave-out)")
    print("    v1 answer (kept, exact): the moving block carries "
          "ZERO of the increment through its own tents")
    print("    (LEAVE: bitwise zero; ENTER: baseline frame-dead)."
          "  v2 object: Delta_p = (C_a - C_b) -")
    print("    (C_a^{-p} - C_b^{-p}), leave-one-prime-out of the "
          "%d largest in-window-mass primes." % NP_TOP)
    tdec_by_k = {d["r"]["k"]: d for d in tdec}
    i0 = (len(trows) - MEDIUM_N) // 2
    a3_jobs = [("truth", trows[i]) for i in
               range(i0, i0 + MEDIUM_N)]
    if first_s is not None:
        a3_jobs.append(("smooth", first_s))
    grain_truth, grain_smooth = [], []
    parse_ok = True
    for world, r in a3_jobs:
        d2 = tdec_by_k.get(r["k"]) if world == "truth" else None
        ka, kb = r["ka"], r["kb"]
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
        mtot = sum(masses.values())
        print("\n  %s h %d->%d (kz %d->%d, %s %d atoms; v1 "
              "moving-block answer: %s)"
              % (world.upper(), r["ha"], r["hb"], r["kza"],
                 r["kzb"], r["flow"], abs(kb - ka),
                 (d2["typ"] if d2 is not None else
                  "see A2 smooth census")))
        rows_p = []
        n_lo_dead = 0
        for p in order:
            gset = set(groups[p])
            ca = rung_win(r["kza"],
                          comb=comb_of(
                              [i for i in range(ka)
                               if i not in gset], world),
                          rr_cache=rrs[r["kza"]])
            cb = rung_win(r["kzb"],
                          comb=comb_of(
                              [i for i in range(kb)
                               if i not in gset], world),
                          rr_cache=rrs[r["kzb"]])
            if (death_channel(ca) is not None
                    or death_channel(cb) is not None):
                n_lo_dead += 1
                print("    p %-6d LEAVEOUT-DEAD (a: %s, b: %s)"
                      % (p, death_channel(ca) or "ok",
                         death_channel(cb) or "ok"))
                continue
            Dp = r["DC"] - (ca["CJ"] - cb["CJ"])
            rows_p.append((p, len(groups[p]),
                           masses[p] / mtot, part_rho(r, Dp),
                           Dp))
        if not rows_p:
            print("    A3-UNAVAILABLE (all leave-outs dead)")
            continue
        sum_p = sum(x[3] for x in rows_p)
        top = max(x[3] for x in rows_p)
        top_share = top / sum_p if sum_p > 0 else float("nan")
        single = top / r["rho"] if r["rho"] > 0 else float("nan")
        resid = r["DC"] - sum((x[4] for x in rows_p),
                              np.zeros_like(r["DC"]))
        resid_share = (float(np.linalg.norm(resid))
                       / max(float(np.linalg.norm(r["DC"])),
                             1e-300))
        print("    p       n_pow  mass%%   rho_p     rho_p/sum")
        for p, npow, ms, rp, _ in rows_p:
            print("    %-7d %4d   %5.1f   %8.4f  %.3f"
                  % (p, npow, 100.0 * ms, rp,
                     rp / sum_p if sum_p > 0 else 0.0))
        if len(rows_p) < MIN_LO_ALIVE:
            gtype = "GRAIN-UNDERSAMPLED"
        elif resid_share > DEFECT_BAR:
            gtype = "GRAIN-NONDECOMPOSITIONAL"
        else:
            gtype = ("GRAIN-DIFFUSE"
                     if top_share <= GRAIN_DIFFUSE_BAR
                     else "GRAIN-COHERENT"
                     if top_share >= GRAIN_COHERENT_BAR
                     else "GRAIN-INTERMEDIATE")
        print("    sum_p rho_p %.4f | rho_tot %.4f | top share "
              "%.3f | single share %.3f | additivity defect "
              "||resid||/||DC|| %.3f | leave-out dead %d -> %s"
              % (sum_p, r["rho"], top_share, single,
                 resid_share, n_lo_dead, gtype))
        if gtype in ("GRAIN-NONDECOMPOSITIONAL",
                     "GRAIN-UNDERSAMPLED"):
            print("    (v3: responses are frame LEVERAGE, not "
                  "increment grain -- shares not typed as "
                  "anatomy.)")
        (grain_truth if world == "truth"
         else grain_smooth).append(gtype)
    check("A3.1 grain parse ward: every window atom is a prime "
          "power (own trial division)", parse_ok, kill="KW")
    gt = (max(set(grain_truth), key=grain_truth.count)
          if grain_truth else "GRAIN-UNAVAILABLE")
    gs = grain_smooth[0] if grain_smooth else "GRAIN-UNAVAILABLE"
    print("\n    GRAIN ANSWER (v3): moving-block channel = "
          "EXACTLY NIL (v1, A2); leave-out anatomy: truth")
    print("    (modal of %d steps) = %s | smooth crossing "
          "step = %s" % (len(grain_truth), gt, gs))
    print("    PLAIN: the per-prime grain of the step increment "
          "is NOT accessible -- no single prime's move")
    print("    carries the avoidance or the crossing; both live "
          "in the COLLECTIVE window re-test.")
    check("A3.2 grain typed: truth %s, smooth-cross %s"
          % (gt, gs), True)

    # ------------------------------------------------------------ A4
    section("A4 -- TYPED AVOIDANCE")
    avoid = ("AVOIDANCE-NORM" if frac_lt1 == 1.0 else
             "AVOIDANCE-MIXED" if frac_lt1 >= MIXED_FRAC else
             "AVOIDANCE-STRUCTURAL")
    print("    truth rho < 1 on %d/%d (frac %.3f; bars: NORM = "
          "1.0, MIXED >= %.2f)" % (n_lt1, len(trows), frac_lt1,
                                   MIXED_FRAC))
    check("A4.1 typed: %s" % avoid, True)
    if avoid == "AVOIDANCE-NORM":
        print("\n    PLAIN STATEMENT (typed, not claimed): the "
              "induction theorem shape is a NORM BOUND --")
        print("    rho(W_h^{-1} Delta C_h) < 1 per step forces "
              "1 + mu_i > 0 for every factor, hence Q_h > 0")
        print("    and W_{h+1} PD, by the symmetric-similarity "
              "mini-theorem above.")
    else:
        print("\n    PLAIN STATEMENT (typed, not claimed): the "
              "norm-bound theorem shape FAILS -- rho is >= 1")
        print("    on %d/%d truth steps, always via the HARMLESS "
              "side (max mu up to %+.2f, min factor still"
              % (len(trows) - n_lt1, len(trows), pos_side))
        print("    > 0 there).  The avoidance is ONE-SIDED: "
              "max(-min mu) = %.4f < 1 across the ladder."
              % neg_side)
        print("    The inheritance statement is the one-sided "
              "bound lambda_min(W^{-1/2} DC W^{-1/2}) > -1,")
        print("    which IS PD inheritance itself -- no "
              "reduction to a two-sided operator norm.")

    # ------------------------------------------------------------ C
    section("C -- controls")
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
          ok1, kill="K3")
    print("  C2 -- smooth-mass world: PRIMARY embedded control; "
          "crossings ward-anchored in A0.3 (%d crossing steps)."
          % n_cross_s)
    check("C2 smooth detector fired (%d crossings)" % n_cross_s,
          n_cross_s > 0, kill="K3")

    # ------------------------------------------------------------ V
    section("V -- FROZEN VERDICT")
    n_pass = sum(1 for _n, okk in CHECKS if okk)
    n_tot = len(CHECKS)
    if KILLS:
        VERDICT = {"K1": "PIPELINE-BROKEN",
                   "KW": "WARD-BROKEN",
                   "K3": "CONTROL-DEAD"}[KILLS[0]]
        print("\n  VERDICT: %s" % VERDICT)
    else:
        VERDICT = ("FACTORAVOID-MEASURED / %s / %s / "
                   "GRAIN(truth=%s, smoothcross=%s)"
                   % (avoid, a2_lab_t, gt, gs))
        print("\n  VERDICT: %s" % VERDICT)
        print("  (truth rho < 1 on %d/%d, max rho %.4f, one-"
              "sided margin max(-min mu) %.4f; smooth 2x2 = "
              "%d/%d/%d/%d)"
              % (n_lt1, len(trows), float(np.max(rho_t)),
                 neg_side, c11, c10, c01, c00))
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed"
          % (time.time() - T0, n_tot, n_tot - n_pass))
    return 0 if n_pass == n_tot else 1


if __name__ == "__main__":
    raise SystemExit(main())
