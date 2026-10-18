#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""kernel_sos_probe -- PRIME.CASE.KERNEL.SOS.01
(EXPLORATION ONLY, experiments/; round 55, reviewer priority 4:
compute the NEGATIVE INDEX of the extracted pair-correlation kernel
EXACTLY and test the Gram-difference (sum-of-squares) decomposition
-- the attempt to convert the conditional pair contract into an
unconditional finite-rank correction.  2026-08-09.)

CONTEXT (machinery verbatim from paircorr_contract_probe /
signed_homotopy_probe / christoffel_pnt_gamma_probe): round 50
extracted the exact node kernel of the conditional contract
PRIME.CASE.PAIRCORR.CONTRACT.01,
    K_{h,m}(u) = -(1/2) sum_i tent_i(u) w_i
                 sum_f W_{f,m} cos(2 pi i f / L),
band-limited (n90 = 7..26 modes), with the contract
sum_n mu_n K_{h,m}(log n) - K0 >= deficit_{h,m}.  CAREFUL (the
reviewer's frame): the contract's first-order form is LINEAR in the
comb masses mu; the pair kernel enters only through the quadratic
remainder / the variance reading.  THE CLEAN OBJECT for the SOS
question is therefore the FREQUENCY-SIDE WEIGHT of the linear
functional: Fourier-analyze K exactly over its own band and ask
whether the cosine-coefficient structure is one-signed (then the
functional is a positive-frequency-weight pairing of the explicit-
formula spectral density -- the classical Weil-positivity shape) or
signed (then the negative index r = the number of negative
frequency weights obstructs the SOS reading).

THE EXACT ALGEBRA (frozen; all finite linear algebra on the
deployed v563 family): the node samples are K_i := K_{h,m}(iD)
= -(1/2) w_i sum_g W_{g,m} cos(i theta_g), theta_g = 2 pi g / L,
L = 2M - 2, w_i = 2 - delta_{i,0} - delta_{i,M-1}.  Writing the
DCT-I inversion -K_i = sum_{f=0}^{M-1} ctil_f cos(i theta_f)
(orientation frozen: ctil = the cosine weights of -K, so that the
constructional weights W enter with a PLUS sign), the endpoint
deficit of w_i gives the CLOSED FORM
    ctil_f = W_{f,m} - (mult_f / (2L)) (T0 + (-1)^f T1),
    T0 = sum_g W_{g,m},  T1 = sum_g (-1)^g W_{g,m},
mult_f = 1 at f in {0, M-1} else 2.  W_{f,m} >= 0 EXACTLY by
construction (qt >= 0 times a square, plus a nonnegative diagonal
term), so every negative coefficient is the flat (rank-2 in i)
boundary leakage of the symmetric extension.  In u-space the same
identity reads (the u < D mirror of the deployed assembly exactly
restores the i = 0 endpoint deficit, checked as a ward):
    -K(u) = sum_f W_{f,m} phi_f(u) - (T1/2) tent_{M-1}(u)
on [0, 2 alpha], phi_f(u) = sum_i tent_i(u) cos(i theta_f): the
sole u-space defect is the single top-edge tent -- the minimal
Gram-difference has negative rank r_min <= 1, and its functional on
the truth comb is (T1/2) E, E = sum_n mu_n tent_{M-1}(log n).

FROZEN PROTOCOL (2026-08-09; constants frozen before the first
measurement run; heavy rungs + the deepest 3; budget < 15 min):

 RUNGS: heavy kz {9, 12, 13, 26, 40} + the deepest 3 with complete
   atom tables, kz {88, 90, 116} (verbatim eligibility and
   selection from christoffel_pnt_gamma_probe; X <= 4e5).
 ALIASES: all port aliases in the frozen critical zone -- truth
   neg nodes (d1(f) < 0, f >= 1) with a_{h,f} = 2 h^2 (1 - x_f)
   <= h^{2 theta*}, theta* = 0.700 (verbatim round-45/50
   bookkeeping); detail profiles at the critical alias
   m* = argmin_m (lambda_1 - nu_1)_m and at the a-closest alias.

 S1 THE EXACT SPECTRAL DECOMPOSITION (every rung, every zone
   alias): build W_{f,m} / chat / K at the atoms verbatim
   (kernel_block of paircorr_contract_probe) with the two round-50
   wards kept: (W1) prime-side form == grid form, rel <= 1e-10;
   (W2) K0 route a == route b, rel <= 1e-12.  Then the DCT over
   the exact band f = 0..M-1 by TWO exact routes: (route a) FFT of
   the symmetric extension of -K_i = chat_i/2; (route b) the
   closed form above.  NEW WARDS: (W3) constructional positivity
   min_{f,m} W_{f,m} >= 0 (exact); (W4) route a == route b, rel
   sup <= 1e-10 of max |ctil| (FFT imag residue <= 1e-9 rel).
   THE NEGATIVE INDEX: r(h, m) = #{f : ctil_f < -TOL_NEG max_f
   |ctil_f|}, TOL_NEG = 1e-12 (float-dust floor; the exact-sign
   count printed alongside), and the negative-mass fraction
   sum |ctil_-| / sum |ctil|.  Frequency-weight profiles printed
   at m* and rank 1: ctil at the f-deciles, the top-5 positive and
   top-5 negative modes (f, tau_f = 2 pi f/(L D), ctil, a_f,
   sector flags), n90 of |W|.  TYPING (frozen): INDEX-ZERO iff
   r = 0 at every (rung, zone alias); INDEX-SMALL iff max r <= 3;
   else INDEX-LARGE.

 S2 THE GRAM-DIFFERENCE + THE ABSORPTION TEST (if r > 0): the
   positive/negative frequency split IS the decomposition for a
   cosine kernel: with the variance-reading pair kernel
   Kpair(u,u') = sum_f ctil_f phi_f(u) phi_f(u') the explicit
   Gram difference is Kpair = Phi^T Phi - Psi^T J_r Psi,
   Phi = [sqrt(ctil_f^+) phi_f], Psi = [sqrt(|ctil_f^-|) phi_f],
   J_r = I_r, r = the negative index (printed).  MINIMAL reading:
   the exact boundary identity above, ward (W5) per alias at the
   functional level: |S1 + W.Chat - (T1/2) E| <= 1e-10 x scale,
   Chat_g = sum_i t_i cos(i theta_g), t_i = sum_n mu_n
   tent_i(log n) -- r_min <= 1 with the explicit edge functional
   (T1/2) E.  ABSORPTION: the exact repartition (ward W6, rel <=
   1e-10) J1 = sum_f ctil_f r(f) + B0 + B1, B0 = T0 (sum_f mult_f
   r_f)/(2L), B1 = T1 (sum_f mult_f (-1)^f r_f)/(2L); the
   negative-mode functional on the truth comb N_m = sum_{f:
   ctil < -bar} ctil_f r(f).  OVERLAP CENSUS of the negative-mode
   frequencies vs (a) the pole/arch layer {f : |d_ar(f)| >=
   |d0at(f)|} (arch density dominates the PNT-atom density),
   (b) the exterior zone a_f > h^{2 theta*}, (c) the 8 a-closest
   truth-neg core aliases; per-alias negative-mass shares, the
   union share, counts.  TYPED (frozen): ABSORBABLE(where) iff
   every measured margin (lambda_1 - nu_1)_m > 0 AND max_m
   |N_m| / margin_m <= 1 AND the mean union negative-mass share
   >= 0.90 (aliases with r = 0 vacuous, excluded from the mean);
   where = the dominant sector if its mean share >= 0.50, else
   UNION.  Else NOT-ABSORBED.

 S3 THE UNCONDITIONAL READING (deliverable): if INDEX-ZERO or
   ABSORBABLE, print the theorem-shaped statement -- the contract
   becomes a POSITIVE-weight band-limited explicit-formula
   positivity (weights W_{f,m} >= 0, even test functions phi_f
   supported in [-2 alpha, 2 alpha]) with one explicit rank-<=-1
   edge defect: a Weil-positivity instance on a FINITE band with
   positive weight.  THE HONEST CLASSICAL ASSESSMENT printed:
   unconditional Weil positivity is classical exactly when the
   test support fits inside (-log 2, log 2) (the prime side is
   empty and the archimedean side is positive); our band 2 alpha
   >> log 2 on every rung (printed per rung with X = e^{2 alpha}),
   so this is NOT a known unconditional case -- the named partial
   inputs (zero-free-region error, short-interval asymptotics for
   widths >= x^{0.525}) are NOT applicable at these finite X; the
   route REMAINS CONDITIONAL, but the hypothesis moves from a
   generically signed form into the classical positive-weight
   Weil class (+ the measured edge defect).  If INDEX-LARGE and
   NOT-ABSORBED: state plainly that the pair route stays
   conditional and genuinely pair-correlation strong.

 C  CONTROLS (kz 9, scramble seed 1, verbatim round-50 mirror:
   positions uniform on (0, 2 alpha), same masses): the scramble
   must flip the finite margins -- min_m (lambda_scr - nu_scr)_m
   <= 0 on the scramble zone aliases (fallback, disclosed if the
   zone set is empty: the 8 a-closest scramble neg nodes).
   Silent -> CONTROL-DEAD.

 SELF-TESTS (S0, kill PIPELINE on failure): (i) AST firewall
   clean; (ii) endpoint reconstruction (kz 9): the qt-route
   lambda/nu at the zone aliases vs the verbatim folded_measure
   route, rel <= 1e-8, at both t = 0 and t = 1; (iii) quadratic-
   form self-test per rung at both endpoints: sum_j w_j p*^2 ==
   lambda to rel 1e-8 (verbatim TOL_QF).

KILLS: chain short anywhere needed / self-test failure / zone
alias set empty on a rung -> PIPELINE-BROKEN; any ward W1..W6
failure -> WARD-BROKEN; value control silent -> CONTROL-DEAD.
S1 typing, S2 absorption and S3 outcomes are MEASUREMENTS, never
kills.

VERDICT (frozen enum): KERNELSOS-MEASURED (+ INDEX=<INDEX-ZERO |
INDEX-SMALL | INDEX-LARGE> + RMIN=<0 | 1> + ABSORB=<ABSORBABLE(
where) | NOT-ABSORBED | VACUOUS> + LEDGER=<CONSISTENT |
INCONSISTENT k/N>) / PIPELINE-BROKEN / WARD-BROKEN / CONTROL-DEAD.

SPEC AMENDMENTS (fail-first preserved):
  v1 (2026-08-09): initial freeze.  All kernel/endpoint machinery
  and tolerances are the round-50 frozen values, reused verbatim;
  the DCT orientation, TOL_NEG = 1e-12, the typing bars (0 / 3),
  the absorption bars (margin ratio 1, union share 0.90, dominance
  0.50) and the sector definitions (a)/(b)/(c) are frozen a
  priori, before any coefficient was computed.

NO RH claim: everything here is exact finite linear algebra on
the deployed v563 window family plus measured finite shadows; the
classical statement in S3 is NAMED and assessed, not proved; no
bound, no rate, no uniformity in h.  No marker moves.

FIREWALL: no zeros, no prime oracles beyond the deployed table
(AST scan: zetazero/nzeros/primerange/isprime/primepi/nextprime/
prevprime banned); v563 READ-ONLY; RNG only in the scramble
control; stdout only.

Sources (read-only): paircorr_contract_probe (node kernel,
kernel_block, wards W1/W2, margin ledger, control -- verbatim);
signed_homotopy_probe / christoffel_pnt_gamma_probe (rung set,
folded measures, Lanczos chain, closed-form PNT lags -- verbatim);
christoffel_zone_envelope_probe (theta* = 0.700), declared inputs.

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/kernel_sos_probe.py
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
DEEP3 = (88, 90, 116)          # frozen (christoffel_pnt_gamma_probe)
RUNGS = tuple(sorted(set(HEAVY) | set(DEEP3)))
THETA_STAR = 0.700             # frozen zone exponent (ZONESPLIT.01)
TOL_WARD_PRIME = 1.0e-10       # W1: prime-side form == grid form
TOL_WARD_K0 = 1.0e-12          # W2: K0 route a == route b
TOL_WARD_DCT = 1.0e-10         # W4: FFT route == closed form
TOL_WARD_IMAG = 1.0e-9         # W4: FFT imag residue (rel)
TOL_WARD_FUNC = 1.0e-10        # W5: u-space boundary identity
TOL_WARD_SPLIT = 1.0e-10       # W6: repartition of J1
TOL_SELF_END = 1.0e-8          # S0.2 endpoint reconstruction
TOL_QF = 1.0e-8                # S0.3 quadratic-form self-test
TOL_NEG = 1.0e-12              # negative-index float-dust floor
IDX_SMALL = 3                  # typing bar: INDEX-SMALL iff r <= 3
ABS_RATIO = 1.0                # absorption: |N| / margin bar
ABS_UNION = 0.90               # absorption: mean union share bar
ABS_DOM = 0.50                 # where-tag: dominant-sector bar
CORE_AL = 8                    # (c): the 8 a-closest core aliases
FRAC_MASS = 0.90               # n90 mass fraction (verbatim)
NDEC = 11                      # profile: f-decile sample count
NTOP = 5                       # profile: top +/- modes printed
SCRAMBLE_SEED = 1
CTRL_FALLBACK_AL = 8           # C: a-closest neg nodes fallback
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
# (grid density, folded measures, Lanczos chain, closed-form PNT lags:
#  verbatim from paircorr_contract_probe / christoffel_pnt_gamma_probe)

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


def _prim(u, A, B):
    """Primitive of (A + B u) 2 e^{u/2}: 4 e^{u/2} (A + B (u - 2))."""
    return 4.0 * np.exp(0.5 * u) * (A + B * (u - 2.0))


def cont_lags(alpha, M, seg_lo, seg_hi, seg_sc):
    """W2 closed-form PNT tent lags (verbatim, incl. i=0 mirror)."""
    D = 2.0 * alpha / M
    c = np.zeros(M)
    for lo, hi, sc in zip(seg_lo, seg_hi, seg_sc):
        i0 = max(0, int(math.floor(lo / D)) - 1)
        i1 = min(M - 1, int(math.ceil(hi / D)) + 1)
        ii = np.arange(i0, i1 + 1, dtype=float)
        val = np.zeros(len(ii))
        a = np.maximum((ii - 1.0) * D, lo)          # rising piece
        b = np.minimum(ii * D, hi)
        m = b > a
        val[m] += (_prim(b[m], 1.0 - ii[m], 1.0 / D)
                   - _prim(a[m], 1.0 - ii[m], 1.0 / D))
        a = np.maximum(ii * D, lo)                  # falling piece
        b = np.minimum((ii + 1.0) * D, hi)
        m = b > a
        val[m] += (_prim(b[m], 1.0 + ii[m], -1.0 / D)
                   - _prim(a[m], 1.0 + ii[m], -1.0 / D))
        if i0 == 0:                                 # i = 0 reflection
            a0, b0 = max(0.0, lo), min(D, hi)
            if b0 > a0:
                val[0] += (_prim(b0, 1.0, -1.0 / D)
                           - _prim(a0, 1.0, -1.0 / D))
        c[i0:i1 + 1] -= 0.5 * sc * val
    return c


# --------------------------------------------------------- rung construction
def build_rung(kz):
    """Folded d_PNT, d_truth, residual, weights, zone aliases, arch
    density, core aliases and the lag blocks c0/c1 of one rung."""
    rr = core.build_window(kz)
    alpha, M, h, D = rr["alpha"], rr["M"], rr["h"], rr["D"]
    assert abs(D - 2.0 * alpha / M) <= 1e-12 * D
    uu = np.asarray(rr["uu"], float)
    mm = 2.0 * np.asarray(rr["lam"], float)
    c_ar = np.asarray(core.arch_lags(M, D), float)
    c1 = np.asarray(core.atom_lags_at(alpha, M, uu, mm)[0], float)
    c0 = np.asarray(cont_lags(alpha, M, [0.0], [2.0 * alpha],
                              [1.0]), float)
    L = 2 * M - 2
    F = L // 2 + 1
    d1 = grid_density(c_ar + c1)[:F]
    d0 = grid_density(c_ar + c0)[:F]
    d0at = grid_density(c0)[:F]
    d_ar = grid_density(c_ar)[:F]
    r = d1 - d0
    ff = np.arange(F)
    x = np.cos(2.0 * math.pi * ff / L)
    a = 2.0 * h * h * (1.0 - x)
    mult = np.where((ff == 0) | (ff == L // 2), 1.0, 2.0)
    qt = mult * 4.0 * np.sin(math.pi * ff / L) ** 2 / (2.0 * L)
    neg_all = ff[(ff >= 1) & (d1 < 0.0)]
    neg_all = neg_all[np.argsort(a[neg_all], kind="stable")]
    al_f = neg_all[a[neg_all] <= h ** (2.0 * THETA_STAR)]
    core8 = neg_all[:CORE_AL]
    return dict(kz=kz, alpha=alpha, M=M, h=h, L=L, F=F, D=D,
                c_ar=c_ar, c0=c0, c1=c1, uu=uu, mm=mm,
                x=x, a=a, qt=qt, mult=mult, d0=d0, d1=d1,
                d0at=d0at, d_ar=d_ar, r=r, al_f=al_f,
                y_al=x[al_f], core8=core8,
                X=math.exp(2.0 * alpha))


def gap_at(R, dv, al_f, qf=False):
    """Chain of the positive part of dv; per alias the Christoffel
    lambda, target mass nu, gap G (qt route, S0.2-pinned)."""
    pos = (dv > 0.0) & (R["qt"] > 0.0)
    xs = R["x"][pos]
    ws = (R["qt"] * dv)[pos]
    h = R["h"]
    al, be, m0, steps = lanczos_chain(xs, ws, h + 1)
    if steps < h + 1:
        return None
    Phi = eval_chain(al, be, m0, R["x"][al_f], h)   # n_al x h
    K = np.sum(Phi ** 2, axis=1)
    lam = 1.0 / K
    nu = R["qt"][al_f] * np.maximum(-dv[al_f], 0.0)
    out = dict(lam=lam, nu=nu, G=lam - nu, chain=(al, be, m0),
               Phi=Phi, Kdiag=K, pos=pos)
    if qf:
        Ppos = eval_chain(al, be, m0, xs, h)
        U = Ppos @ Phi.T
        out["qf_dev"] = float(np.max(np.abs(
            (ws @ (U * U)) / K - 1.0)))
    return out


# --------------------------------------- the node kernel (round-50 verbatim)
def kernel_block(R, e0):
    """W, chat, K at the atoms, prime sum, smooth subtraction, wards
    W1/W2, plus the comb tent sums t_i, Chat_g and the edge mass E
    needed by the W5 boundary identity (all exact algebra)."""
    al, be, m0 = e0["chain"]
    h, F, M, L = R["h"], R["F"], R["M"], R["L"]
    Pall = eval_chain(al, be, m0, R["x"], h)        # F x h
    U0 = Pall @ e0["Phi"].T                         # F x n_al
    P2 = (U0 * U0) / e0["Kdiag"] ** 2               # p_{0,m}(x_f)^2
    af = R["al_f"]
    W = (R["qt"] * (R["d0"] > 0.0))[:, None] * P2   # F x n_al
    W[af, np.arange(len(af))] += (R["qt"][af]
                                  * (R["d0"][af] < 0.0))
    A_grid = W.T @ R["r"]
    ii = np.arange(M)
    cosIF = np.cos((2.0 * math.pi / L)
                   * np.outer(ii, np.arange(F).astype(float)))
    w_i = np.where((ii == 0) | (ii == M - 1), 1.0, 2.0)
    chat = (cosIF @ W) * w_i[:, None]               # M x n_al
    # comb tent sums t_i (plain full-weight binning; the deployed
    # u < D mirror is exactly the identity's i = 0 restoration)
    uu, D, mm = R["uu"], R["D"], R["mm"]
    i0 = np.floor(uu / D).astype(int)
    fr = uu / D - i0
    t = np.zeros(M)
    ok0 = (i0 >= 0) & (i0 <= M - 1)
    np.add.at(t, i0[ok0], (mm * (1.0 - fr))[ok0])
    ok1 = (i0 + 1 >= 0) & (i0 + 1 <= M - 1)
    np.add.at(t, (i0 + 1)[ok1], (mm * fr)[ok1])
    Chat = t @ cosIF                                # F-vector
    E = float(t[M - 1])
    del cosIF
    # K at the atoms: tent interpolation of -chat/2 (+ u<D mirror)
    v0 = np.where((i0 >= 0) & (i0 <= M - 1), 1.0 - fr, 0.0)
    v1 = np.where((i0 + 1 >= 0) & (i0 + 1 <= M - 1), fr, 0.0)
    Kat = -0.5 * (v0[:, None] * chat[np.clip(i0, 0, M - 1)]
                  + v1[:, None] * chat[np.clip(i0 + 1, 0, M - 1)])
    mir = uu < D
    if np.any(mir):
        Kat[mir] += -0.5 * ((1.0 - uu[mir] / D)[:, None]
                            * chat[0][None, :])
    S1 = R["mm"] @ Kat
    K0a = W.T @ R["d0at"]
    K0b = R["c0"] @ chat
    A_prime = S1 - K0a
    Sabs = np.abs(R["mm"]) @ np.abs(Kat) + np.abs(K0a)
    ward1 = float(np.max(np.abs(A_prime - A_grid)
                         / np.maximum(np.maximum(np.abs(A_grid),
                                                 Sabs), 1e-300)))
    ward2 = float(np.max(np.abs(K0b - K0a)
                         / np.maximum(np.abs(R["c0"])
                                      @ np.abs(chat), 1e-300)))
    return dict(W=W, chat=chat, Kat=Kat, S1=S1, K0=K0a,
                A_grid=A_grid, A_prime=A_prime, Sabs=Sabs,
                ward1=ward1, ward2=ward2, P2=P2,
                t=t, Chat=Chat, E=E)


# ------------------------------------------- S1/S2: the spectral side
def spectral_block(R, kb):
    """Exact DCT of the node kernel per alias (two routes), the
    negative index, the repartition of J1, and ward material."""
    F, L, M = R["F"], R["L"], R["M"]
    assert F == M
    ff = np.arange(F)
    multF = np.where((ff == 0) | (ff == F - 1), 1.0, 2.0)
    par = np.where(ff % 2 == 0, 1.0, -1.0)
    W = kb["W"]
    T0 = np.sum(W, axis=0)
    T1 = par @ W
    # route b: closed form
    ctil_cf = W - (multF[:, None] / (2.0 * L)) * (
        T0[None, :] + par[:, None] * T1[None, :])
    # route a: FFT of the symmetric extension of -K_i = chat_i/2
    v = 0.5 * kb["chat"]                            # M x n_al
    a_ext = np.concatenate([v, v[-2:0:-1]], axis=0)
    A = np.fft.fft(a_ext, axis=0)
    imag_rel = float(np.max(np.abs(A.imag))
                     / max(float(np.max(np.abs(A.real))), 1e-300))
    ctil_fft = multF[:, None] * A[:F].real / L
    scale4 = max(float(np.max(np.abs(ctil_cf))), 1e-300)
    ward4 = float(np.max(np.abs(ctil_fft - ctil_cf))) / scale4
    ctil = ctil_cf
    # negative index per alias
    bar = TOL_NEG * np.maximum(np.max(np.abs(ctil), axis=0),
                               1e-300)
    negm = ctil < -bar[None, :]
    r_al = np.sum(negm, axis=0).astype(int)
    r_exact = np.sum(ctil < 0.0, axis=0).astype(int)
    mass_all = np.sum(np.abs(ctil), axis=0)
    mass_neg = np.sum(np.abs(ctil) * negm, axis=0)
    negfrac = mass_neg / np.maximum(mass_all, 1e-300)
    # repartition of J1 = W.r (ward W6) and the negative functional
    rv = R["r"]
    B0 = (T0 / (2.0 * L)) * float(multF @ rv)
    B1 = (T1 / (2.0 * L)) * float((multF * par) @ rv)
    lin = ctil.T @ rv
    ward6 = float(np.max(
        np.abs(lin + B0 + B1 - kb["A_grid"])
        / np.maximum(np.abs(ctil).T @ np.abs(rv)
                     + np.abs(B0) + np.abs(B1), 1e-300)))
    Nfun = np.sum(ctil * rv[:, None] * negm, axis=0)
    # W5: u-space boundary identity at the functional level
    S1id = -(W.T @ kb["Chat"]) + 0.5 * T1 * kb["E"]
    sc5 = (np.abs(kb["S1"]) + np.abs(W.T @ np.abs(kb["Chat"]))
           + np.abs(0.5 * T1 * kb["E"]))
    ward5 = float(np.max(np.abs(kb["S1"] - S1id)
                         / np.maximum(sc5, 1e-300)))
    # sectors (frozen definitions)
    arch = np.abs(R["d_ar"]) >= np.abs(R["d0at"])
    ext = R["a"] > R["h"] ** (2.0 * THETA_STAR)
    ext = ext & (ff >= 1)
    core8 = np.zeros(F, bool)
    core8[R["core8"]] = True
    union = arch | ext | core8
    return dict(ctil=ctil, T0=T0, T1=T1, r_al=r_al,
                r_exact=r_exact, negfrac=negfrac, negm=negm,
                B0=B0, B1=B1, lin=lin, Nfun=Nfun,
                ward4=ward4, ward5=ward5, ward6=ward6,
                imag_rel=imag_rel, minW=float(np.min(W)),
                arch=arch, ext=ext, core8m=core8, union=union,
                multF=multF, par=par)


def profile_print(R, kb, sb, m_idx, tag):
    """S1 frequency-weight profile at one alias column."""
    F, L, D = R["F"], R["L"], R["D"]
    ct = sb["ctil"][:, m_idx]
    ff = np.arange(F)
    tauv = 2.0 * math.pi * ff / (L * D)
    aw = np.abs(kb["W"][1:, m_idx])
    o = np.argsort(-aw)
    cs = np.cumsum(aw[o])
    n90 = int(np.searchsorted(cs, FRAC_MASS * cs[-1]) + 1)
    f_m = int(R["al_f"][m_idx])
    print("      ctil profile %s (alias %2d, f %4d, a %8.1f, "
          "tau_m %.2f): r %d (exact-sign %d), negmass %.3e, "
          "n90(|W|) %d"
          % (tag, m_idx + 1, f_m, float(R["a"][f_m]),
             2.0 * math.pi * f_m / (L * D),
             int(sb["r_al"][m_idx]), int(sb["r_exact"][m_idx]),
             float(sb["negfrac"][m_idx]), n90))
    dec = [min(F - 1, int(round(k * (F - 1) / (NDEC - 1))))
           for k in range(NDEC)]
    print("        ctil at f-deciles f=%s:"
          % ",".join("%d" % d for d in dec))
    print("          %s" % " ".join("%+.1e" % ct[d] for d in dec))
    op = np.argsort(-ct)[:NTOP]
    print("        top +modes: %s"
          % "  ".join("f%d(tau %.2f, c %+.2e)"
                      % (int(f), tauv[f], ct[f]) for f in op))
    on = np.argsort(ct)[:NTOP]
    on = [int(f) for f in on if ct[f] < 0.0]
    if on:
        def flags(f):
            s = ""
            s += "A" if sb["arch"][f] else "."
            s += "X" if sb["ext"][f] else "."
            s += "C" if sb["core8m"][f] else "."
            return s
        print("        top -modes: %s"
              % "  ".join("f%d(tau %.2f, c %+.2e, a %.0f, %s)"
                          % (f, tauv[f], ct[f], R["a"][f],
                             flags(f)) for f in on))
    else:
        print("        top -modes: none (one-signed at this "
              "alias)")


def main():
    section("PRIME.CASE.KERNEL.SOS.01 -- the negative index of the "
            "contract kernel + Gram-difference (EXPLORATION ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s"
          % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
    print("    NO RH claim; no marker moves.")

    print("\nS0 -- firewall + self-tests")
    check("S0.1 AST firewall clean", not ast_scan(BANNED_IDS),
          kill="PIPELINE")

    section("B0 -- rungs (geometry + zone aliases)")
    RG = {}
    for kz in RUNGS:
        R = build_rung(kz)
        RG[kz] = R
        print("    kz %-3d h %4d M %4d F %5d: atoms %5d, "
              "X %.3e, 2a %.2f, zone aliases %3d "
              "(a <= h^1.4 = %8.0f)"
              % (kz, R["h"], R["M"], R["F"], len(R["uu"]),
                 R["X"], 2.0 * R["alpha"], len(R["al_f"]),
                 R["h"] ** 1.4), flush=True)
    order = sorted(RUNGS, key=lambda kz: RG[kz]["h"])
    ok_al = all(len(RG[kz]["al_f"]) > 0 for kz in RUNGS)
    check("B0.1 zone alias sets nonempty on every rung", ok_al,
          kill="PIPELINE")
    if not ok_al:
        return finish(None, None, None, None)

    # S0.2 endpoint reconstruction vs verbatim folded route (kz 9)
    R9 = RG[9]
    dev_end = 0.0
    for tv in (0.0, 1.0):
        dv = R9["d0"] if tv == 0.0 else R9["d1"]
        d_full = np.concatenate([dv, dv[-2:0:-1]])
        xs, ws, _uf = folded_measure(d_full, R9["L"], +1.0)
        ys, vs, uf_n = folded_measure(d_full, R9["L"], -1.0)
        al, be, m0, steps = lanczos_chain(xs, ws, R9["h"] + 1)
        if steps < R9["h"] + 1:
            check("S0.2 endpoint chain (verbatim route)", False,
                  kill="PIPELINE")
            return finish(None, None, None, None)
        Pn = eval_chain(al, be, m0, R9["y_al"], R9["h"])
        lam_ref = 1.0 / np.sum(Pn ** 2, axis=1)
        pos_map = {int(f): float(v) for f, v in zip(uf_n, vs)}
        nu_ref = np.array([pos_map.get(int(f), 0.0)
                           for f in R9["al_f"]])
        e = gap_at(R9, dv, R9["al_f"])
        if e is None:
            check("S0.2 endpoint chain (qt route)", False,
                  kill="PIPELINE")
            return finish(None, None, None, None)
        dev_end = max(dev_end, float(np.max(
            np.abs(e["lam"] / lam_ref - 1.0))))
        dev_end = max(dev_end, float(np.max(
            np.abs(e["nu"] - nu_ref)
            / np.maximum(np.abs(nu_ref), 1e-300))))
    check("S0.2 endpoint reconstruction == verbatim folded route "
          "(kz 9, t = 0 and 1)", dev_end <= TOL_SELF_END,
          "rel sup dev %.2e" % dev_end, kill="PIPELINE")

    section("E -- exact endpoints per rung: deficit, margin "
            "(lambda_1 - nu_1)_m, critical alias m*")
    RES = {}
    ok_e = True
    qf_worst = 0.0
    n_bad = 0
    n_all = 0
    for kz in order:
        R = RG[kz]
        e0 = gap_at(R, R["d0"], R["al_f"], qf=True)
        e1 = gap_at(R, R["d1"], R["al_f"], qf=True)
        if e0 is None or e1 is None:
            ok_e = False
            print("    kz %-3d: CHAIN SHORT at an endpoint" % kz)
            break
        qf_worst = max(qf_worst, e0["qf_dev"], e1["qf_dev"])
        ms = int(np.argmin(e1["G"]))
        margin = e1["G"]
        n_all += len(margin)
        n_bad += int(np.sum(margin <= 0.0))
        RES[kz] = dict(e0=e0, e1=e1, ms=ms)
        print("    kz %-3d h %4d (n_al %2d): deficit max %+.3e | "
              "min margin %+.3e | m* %d (f %d, a %.1f)"
              % (kz, R["h"], len(R["al_f"]),
                 float(np.max(-e0["G"])), float(np.min(margin)),
                 ms + 1, int(R["al_f"][ms]),
                 float(R["a"][R["al_f"][ms]])), flush=True)
    check("E0 endpoint chains complete on all rungs", ok_e,
          kill="PIPELINE")
    check("S0.3 quadratic-form self-test (sum w p*^2 == lambda, "
          "both endpoints, all rungs)", ok_e
          and qf_worst <= TOL_QF, "worst rel dev %.2e" % qf_worst,
          kill="PIPELINE")
    if not ok_e:
        return finish(None, None, None, None)
    ledger = ("CONSISTENT" if n_bad == 0
              else "INCONSISTENT %d/%d" % (n_bad, n_all))
    print("    margin ledger: %s" % ledger)

    section("S1 -- THE EXACT SPECTRAL DECOMPOSITION: DCT of the "
            "node kernel over its band + THE NEGATIVE INDEX")
    w_worst = dict(w1=0.0, w2=0.0, w4=0.0, w5=0.0, w6=0.0,
                   im=0.0, minW=0.0)
    r_max = 0
    negfrac_max = 0.0
    rows = []                      # (kz, m, r, negfrac, N, margin)
    share_pool = []
    for kz in order:
        R = RG[kz]
        t_a = time.time()
        kb = kernel_block(R, RES[kz]["e0"])
        sb = spectral_block(R, kb)
        RES[kz]["kb"] = kb
        RES[kz]["sb"] = sb
        w_worst["w1"] = max(w_worst["w1"], kb["ward1"])
        w_worst["w2"] = max(w_worst["w2"], kb["ward2"])
        w_worst["w4"] = max(w_worst["w4"], sb["ward4"])
        w_worst["w5"] = max(w_worst["w5"], sb["ward5"])
        w_worst["w6"] = max(w_worst["w6"], sb["ward6"])
        w_worst["im"] = max(w_worst["im"], sb["imag_rel"])
        w_worst["minW"] = min(w_worst["minW"], sb["minW"])
        ms = RES[kz]["ms"]
        margin = RES[kz]["e1"]["G"]
        r_max = max(r_max, int(np.max(sb["r_al"])))
        negfrac_max = max(negfrac_max,
                          float(np.max(sb["negfrac"])))
        for m in range(len(R["al_f"])):
            rows.append((kz, m, int(sb["r_al"][m]),
                         float(sb["negfrac"][m]),
                         float(sb["Nfun"][m]),
                         float(margin[m])))
        for sh in spectral_shares(sb):
            share_pool.append(sh)
        print("    kz %-3d h %4d (F %5d, n_al %2d): "
              "r range %d..%d (exact-sign %d..%d), "
              "negmass max %.3e | T1/T0 at m* %+.3f  [%.1f s]"
              % (kz, R["h"], R["F"], len(R["al_f"]),
                 int(np.min(sb["r_al"])), int(np.max(sb["r_al"])),
                 int(np.min(sb["r_exact"])),
                 int(np.max(sb["r_exact"])),
                 float(np.max(sb["negfrac"])),
                 float(sb["T1"][ms]
                       / max(sb["T0"][ms], 1e-300)),
                 time.time() - t_a), flush=True)
        for tag, mi in (("m*", ms), ("m1", 0)):
            if tag == "m1" and ms == 0:
                continue
            profile_print(R, kb, sb, mi, tag)
    check("S1.W1 prime-side form == grid form (max rel %.2e <= "
          "%.0e)" % (w_worst["w1"], TOL_WARD_PRIME),
          w_worst["w1"] <= TOL_WARD_PRIME, kill="WARD")
    check("S1.W2 smooth subtraction route a == route b (max rel "
          "%.2e <= %.0e)" % (w_worst["w2"], TOL_WARD_K0),
          w_worst["w2"] <= TOL_WARD_K0, kill="WARD")
    check("S1.W3 constructional positivity min W_{f,m} >= 0 "
          "(exact; min %.2e)" % w_worst["minW"],
          w_worst["minW"] >= 0.0, kill="WARD")
    check("S1.W4 DCT route a (FFT) == route b (closed form) "
          "(max rel %.2e <= %.0e; imag %.2e <= %.0e)"
          % (w_worst["w4"], TOL_WARD_DCT, w_worst["im"],
             TOL_WARD_IMAG),
          w_worst["w4"] <= TOL_WARD_DCT
          and w_worst["im"] <= TOL_WARD_IMAG, kill="WARD")
    if r_max == 0:
        idx_type = "INDEX-ZERO"
    elif r_max <= IDX_SMALL:
        idx_type = "INDEX-SMALL"
    else:
        idx_type = "INDEX-LARGE"
    print("\n    NEGATIVE-INDEX CENSUS over all (rung, zone "
          "alias): max r = %d, max negative-mass fraction = %.3e"
          % (r_max, negfrac_max))
    print("    every negative coefficient is the closed-form "
          "boundary leakage ctil_f = W_f - mult_f (T0 + (-1)^f "
          "T1)/(2L) with W_f >= 0 (W3): the negativity is NOT "
          "arithmetic, it is the symmetric-extension edge.")
    check("S1.T typed %s (bars: 0 / <= %d)" % (idx_type,
                                               IDX_SMALL), True)

    section("S2 -- GRAM-DIFFERENCE + ABSORPTION (the negative "
            "modes vs the controlled sectors)")
    print("    Gram difference (explicit, per alias): with "
          "phi_f(u) = sum_i tent_i(u) cos(2 pi i f/L),")
    print("      Kpair(u,u') = sum_f ctil_f phi_f(u) phi_f(u') "
          "= Phi^T Phi - Psi^T I_r Psi,")
    print("      Phi = [sqrt(ctil_f^+) phi_f]_{ctil_f > 0}, "
          "Psi = [sqrt(|ctil_f^-|) phi_f]_{ctil_f < 0}, "
          "r = the negative index above.")
    print("    MINIMAL reading (exact boundary identity, ward "
          "W5): -K(u) = sum_f W_f phi_f(u) - (T1/2) tent_{M-1}(u)")
    print("      on [0, 2 alpha] -- the u < D mirror restores the "
          "i = 0 endpoint; r_min <= 1 (the single top-edge tent).")
    check("S2.W5 u-space boundary identity at the functional "
          "level (max rel %.2e <= %.0e)"
          % (w_worst["w5"], TOL_WARD_FUNC),
          w_worst["w5"] <= TOL_WARD_FUNC, kill="WARD")
    check("S2.W6 repartition J1 == sum ctil r + B0 + B1 (max rel "
          "%.2e <= %.0e)" % (w_worst["w6"], TOL_WARD_SPLIT),
          w_worst["w6"] <= TOL_WARD_SPLIT, kill="WARD")
    rmin_any = 0
    print("\n    edge functional (T1/2) E and boundary parts at "
          "m* per rung:")
    for kz in order:
        R = RG[kz]
        sb, kb = RES[kz]["sb"], RES[kz]["kb"]
        ms = RES[kz]["ms"]
        edge = 0.5 * float(sb["T1"][ms]) * kb["E"]
        if abs(edge) > 0.0:
            rmin_any = 1
        print("      kz %-3d: E %.3e, (T1/2)E %+.3e, B0 %+.3e, "
              "B1 %+.3e, N(m*) %+.3e, J1(m*) %+.3e"
              % (kz, kb["E"], edge, float(sb["B0"][ms]),
                 float(sb["B1"][ms]), float(sb["Nfun"][ms]),
                 float(kb["A_grid"][ms])), flush=True)
    print("\n    overlap census of the negative modes at m* "
          "(A = arch layer, X = exterior zone, C = 8 core "
          "aliases; counts and negative-mass shares):")
    for kz in order:
        R = RG[kz]
        sb = RES[kz]["sb"]
        ms = RES[kz]["ms"]
        nm = sb["negm"][:, ms]
        n_neg = int(np.sum(nm))
        w_neg = np.abs(sb["ctil"][:, ms]) * nm
        mn = max(float(np.sum(w_neg)), 1e-300)
        print("      kz %-3d: n_neg %5d | in A %5d (%.2f) | "
              "in X %5d (%.2f) | in C %d (%.2f) | union %5d "
              "(%.2f)"
              % (kz, n_neg,
                 int(np.sum(nm & sb["arch"])),
                 float(np.sum(w_neg[sb["arch"]]) / mn),
                 int(np.sum(nm & sb["ext"])),
                 float(np.sum(w_neg[sb["ext"]]) / mn),
                 int(np.sum(nm & sb["core8m"])),
                 float(np.sum(w_neg[sb["core8m"]]) / mn),
                 int(np.sum(nm & sb["union"])),
                 float(np.sum(w_neg[sb["union"]]) / mn)),
              flush=True)
    # absorption ledger: |N_m| vs margin_m over all (rung, alias)
    worst_ratio = 0.0
    worst_at = None
    any_nonpos = False
    for (kz, m, r_m, nf, N_m, mg) in rows:
        if mg <= 0.0:
            any_nonpos = True
            continue
        ratio = abs(N_m) / mg
        if ratio > worst_ratio:
            worst_ratio = ratio
            worst_at = (kz, m)
    if share_pool:
        mean_sh = {k: float(np.mean([s[k] for s in share_pool]))
                   for k in ("arch", "ext", "core", "union")}
    else:
        mean_sh = None
    print("\n    ABSORPTION LEDGER: |N_m| vs measured margin "
          "(lambda_1 - nu_1)_m over all %d (rung, alias) pairs:"
          % len(rows))
    print("      worst |N|/margin = %.3e%s | margins all "
          "positive: %s"
          % (worst_ratio,
             " at kz %d alias %d" % (worst_at[0],
                                     worst_at[1] + 1)
             if worst_at else "", "yes" if not any_nonpos
             else "NO"))
    if mean_sh:
        print("      mean negative-mass shares over aliases with "
              "r > 0: arch %.3f, exterior %.3f, core8 %.3f, "
              "union %.3f"
              % (mean_sh["arch"], mean_sh["ext"],
                 mean_sh["core"], mean_sh["union"]))
    if r_max == 0:
        absorb = "VACUOUS"
    elif (not any_nonpos and worst_ratio <= ABS_RATIO
          and mean_sh and mean_sh["union"] >= ABS_UNION):
        dom = max(("arch", "ext", "core"),
                  key=lambda k: mean_sh[k])
        where = ({"arch": "ARCH", "ext": "EXTERIOR",
                  "core": "CORE"}[dom]
                 if mean_sh[dom] >= ABS_DOM else "UNION")
        absorb = "ABSORBABLE(%s)" % where
    else:
        absorb = "NOT-ABSORBED"
    check("S2.T absorption typed %s (bars: ratio <= %.1f, union "
          "share >= %.2f)" % (absorb, ABS_RATIO, ABS_UNION), True)

    section("S3 -- THE UNCONDITIONAL READING (deliverable)")
    if idx_type == "INDEX-ZERO" or absorb.startswith("ABSORB") \
            or absorb == "VACUOUS":
        print("    THEOREM-SHAPED STATEMENT (exact finite "
              "calculus on the deployed v563 family):")
        print("      For every deployed rung h and critical alias "
              "m (a_m <= h^{1.4}), the contract functional")
        print("      J1_{h,m} = sum_f W_{f,m} r(f) has "
              "constructionally NONNEGATIVE frequency weights "
              "W_{f,m} (W3),")
        print("      and in u-space  -K_{h,m}(u) = sum_f W_{f,m} "
              "phi_f(u) - (T1/2) tent_{M-1}(u)  exactly (W5):")
        print("      the conditional contract  J1 + R >= deficit  "
              "is a POSITIVE-WEIGHT band-limited explicit-formula")
        print("      positivity (even test functions phi_f, "
              "support <= 2 alpha) with ONE explicit rank-<=-1 "
              "edge defect,")
        print("      whose negative-mode functional is measured "
              "%s (worst |N|/margin %.2e)."
              % (absorb, worst_ratio))
    else:
        print("    The negative index is large and the negative-"
              "mode functional is NOT dominated by the measured")
        print("    margins: the route stays conditional and "
              "genuinely pair-correlation strong (Fall 3).")
    print("\n    HONEST CLASSICAL ASSESSMENT of what remains:")
    print("      the remaining hypothesis is a Weil-positivity "
          "instance on a FINITE band with positive weight:")
    print("      band 2 alpha per rung = %s log-units "
          "(X = %.1e .. %.1e),"
          % ("/".join("%.2f" % (2.0 * RG[kz]["alpha"])
                      for kz in order),
             min(RG[kz]["X"] for kz in RUNGS),
             max(RG[kz]["X"] for kz in RUNGS)))
    print("      vs the classical unconditional window: Weil "
          "positivity is unconditional exactly for even test")
    print("      functions supported in (-log 2, log 2) = "
          "(-0.693, 0.693) (empty prime side, positive "
          "archimedean side);")
    print("      every deployed band exceeds log 2 by a factor "
          "%.1f .. %.1f -> NOT a known unconditional case."
          % (min(2.0 * RG[kz]["alpha"] for kz in RUNGS)
             / math.log(2.0),
             max(2.0 * RG[kz]["alpha"] for kz in RUNGS)
             / math.log(2.0)))
    print("      Named partial inputs (zero-free-region error "
          "exp(-c (log x)^{3/5}); short-interval asymptotics for")
    print("      widths >= x^{0.525}) are NAMED, not proved here, "
          "and not applicable at these finite X: the route")
    print("      REMAINS CONDITIONAL; the structural gain is the "
          "move from a generically signed pair form into the")
    print("      classical positive-weight Weil class with a "
          "single measured edge defect.")
    check("S3.1 unconditional reading printed (measurement)",
          True)

    section("C -- controls (kz 9, scramble seed %d)"
            % SCRAMBLE_SEED)
    rng = np.random.default_rng(SCRAMBLE_SEED)
    us = np.sort(rng.uniform(0.0, 2.0 * R9["alpha"],
                             size=len(R9["uu"])))
    c_s = np.asarray(core.atom_lags_at(R9["alpha"], R9["M"], us,
                                       R9["mm"])[0], float)
    d_s = grid_density(R9["c_ar"] + c_s)[:R9["F"]]
    ff9 = np.arange(R9["F"])
    neg_s = ff9[(ff9 >= 1) & (d_s < 0.0)]
    neg_s = neg_s[np.argsort(R9["a"][neg_s], kind="stable")]
    al_zone = neg_s[R9["a"][neg_s]
                    <= R9["h"] ** (2.0 * THETA_STAR)]
    fell_back = len(al_zone) == 0
    al_use = al_zone if not fell_back else neg_s[:CTRL_FALLBACK_AL]
    es = gap_at(R9, d_s, al_use)
    e0s = gap_at(R9, R9["d0"], al_use)
    if es is None or e0s is None:
        check("C0 scramble chains complete", False,
              kill="PIPELINE")
        return finish(idx_type, absorb, ledger, rmin_any)
    lhs_s = es["G"] - e0s["G"]
    dfc_s = -e0s["G"]
    worst = float(np.min(lhs_s - dfc_s))       # == min (lam - nu)_s
    fires = worst <= 0.0
    print("    scramble aliases: %d%s | min (LHS_scr - deficit) "
          "= min (lambda - nu)_scr = %+.3e (real kz 9 min margin "
          "%+.3e) -> %s"
          % (len(al_use),
             " (zone empty -> frozen fallback: %d a-closest neg "
             "nodes)" % CTRL_FALLBACK_AL if fell_back else
             " (zone aliases)",
             worst, float(np.min(RES[9]["e1"]["G"])),
             "FIRES" if fires else "SILENT"), flush=True)
    check("C1 value control fires (scrambled comb: the finite "
          "margins flip)", fires, kill="CONTROL")

    return finish(idx_type, absorb, ledger, rmin_any)


def spectral_shares(sb):
    """The per-alias sector shares with r > 0 (census pool)."""
    out = []
    n_al = sb["ctil"].shape[1]
    for m in range(n_al):
        if sb["r_al"][m] == 0:
            continue
        w_neg = np.abs(sb["ctil"][:, m]) * sb["negm"][:, m]
        mn = float(np.sum(w_neg))
        if mn <= 0.0:
            continue
        out.append(dict(
            arch=float(np.sum(w_neg[sb["arch"]]) / mn),
            ext=float(np.sum(w_neg[sb["ext"]]) / mn),
            core=float(np.sum(w_neg[sb["core8m"]]) / mn),
            union=float(np.sum(w_neg[sb["union"]]) / mn)))
    return out


def finish(idx_type, absorb, ledger, rmin_any):
    section("V -- FROZEN VERDICT")
    n_pass = sum(1 for _n, okk in CHECKS if okk)
    n_tot = len(CHECKS)
    if "PIPELINE" in KILLS:
        VERDICT = "PIPELINE-BROKEN"
    elif "WARD" in KILLS:
        VERDICT = "WARD-BROKEN"
    elif "CONTROL" in KILLS:
        VERDICT = "CONTROL-DEAD"
    else:
        VERDICT = "KERNELSOS-MEASURED"
    sub = []
    if idx_type:
        sub.append("INDEX=%s" % idx_type)
    if rmin_any is not None:
        sub.append("RMIN=%d" % rmin_any)
    if absorb:
        sub.append("ABSORB=%s" % absorb)
    if ledger:
        sub.append("LEDGER=%s" % ledger)
    print("\n  VERDICT: %s%s"
          % (VERDICT, (" (%s)" % "; ".join(sub)) if sub else ""))
    if VERDICT == "KERNELSOS-MEASURED":
        print("  PLAIN ANSWER: the frequency weights of the "
              "contract kernel are W_{f,m} >= 0 EXACTLY; every "
              "negative DCT coefficient is closed-form boundary "
              "leakage of the symmetric extension, and in u-space "
              "the whole negative content collapses to ONE edge "
              "tent (r_min <= 1).  Typed %s / %s: the contract "
              "is a positive-weight finite-band Weil-positivity "
              "instance, NOT a known unconditional case -- the "
              "route stays conditional, with the negativity "
              "structure now exact and measured."
              % (idx_type or "n/a", absorb or "n/a"))
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed"
          % (time.time() - T0, n_tot, n_tot - n_pass))
    return 0 if n_pass == n_tot else 1


if __name__ == "__main__":
    raise SystemExit(main())
