#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""innovation_autocorr_lift_probe -- PRIME.PORT.AUTOCORR.LIFT.01 +
PRIME.PORT.INNOVATION.DILATION.01
(EXPLORATION ONLY, experiments/; round 61, theorem-engineering on
the RH-side wall: TWO lift attempts for the full wall block,
motivated by (i) s = n - q being literally the Levinson/Durbin
prediction-error variance -- the Schur complement of an extended
covariance -- and (ii) the round-59/61 finding that the hub reads
LAGS, i.e. autocorrelation structure (Wiener-Khinchin).
2026-08-10.)

PART A -- THE AUTOCORR LIFT (race surface, odd Toeplitz wall).
The wall K = odd_toeplitz(c_ar + c_at, M) is the odd-sine
compression P Circ(c) P^* of a symmetric circulant on L = 2M - 2
points; the SOURCE-ONLY window/projection P is therefore the
deployed odd-sine compression itself (the natural candidate the
tent/lag assembly suggests -- frozen).  Build the weighted prime
vector a_h from the deployed atom masses in the window (tent
deposit on the M-grid, frozen convention: plain tent, no edge
reflection -- a is a NEW object) in two frozen mass variants,
  A1: a[i] = sum_n mu_n tent_i(u_n)      (deployed masses),
  A2: a[i] = sum_n sqrt(mu_n) tent_i(u_n) (homogeneity-matched:
      the autocorrelation (a*a)[0] = sum mu_n scales LINEARLY in
      the masses like the deployed lag read),
and its circular autocorrelation ac_a = IFFT |FFT a_pad|^2 (two
routes warded).  Then L_a := odd_toeplitz(ac_a, M) = P T(a)^* T(a)
P^* is PSD BY CONSTRUCTION (symbol |a-hat|^2 >= 0; spot-warded),
and the lift question M_h = P T(a)^* T(a) P^* + R_h, R_h >= 0
becomes: for which beta is K - beta L_a >= 0, and what is the
anatomy of the defect?  Frozen targets: TAR-K c = c_ar + c_at (the
full wall) and TAR-AT c = -c_at (the negated atom read -- the pure
Wiener-Khinchin comparison).  MEASURED (typed, never kills):
 A1t lag level (ALL rungs, cheap): cosine similarity cos(c_tar,
     ac_a) ladder per (target, variant) -- is the deployed lag
     read even CLOSE to an autocorrelation of the deployed comb?
 A2t symbol level (ALL rungs): residual density d_R =
     grid_density(c_tar - beta* ac_a) at the Frobenius-projection
     beta* = <c_tar, ac_a>/|ac_a|^2 (a measured projection
     coefficient, FITTED-typed): negative-mass share, the share of
     negative mass in the x > 1 - BAND_DELTA band, peak-x of the
     negative part -- IS THE NON-LIFTABLE PART THE x = +1 BAND
     AGAIN (rounds 59/60)?
 A3t compressed level (SUBSET_C): exact maximal lift coefficient
     beta_max = 1/lam_max(K^{-1/2} L_a K^{-1/2}) (one eigh of the
     TARGET -- a MEASUREMENT, disclosed under anti-circularity,
     never a certificate); the explained share s_expl = beta_max
     tr(L_a)/tr(K); the BINDING vector v0 (kernel of K - beta_max
     L_a): its frequency-band seat (share of |v0-hat|^2 at x >
     1 - BAND_DELTA, peak x); neg index of K - beta* L_a.
     WALL-BLINDNESS CONTROL (the Weyl lesson, frozen): the same
     beta_max with the SMOOTH deposit a_sm (PNT continuum masses,
     same tent rule): if beta_max(prime)/beta_max(smooth) ~ 1 the
     lift never sees the arithmetic -- typed
     WALLBLIND-A(ratio) / WALLSEES-A(ratio).
TYPED: AUTOCORR-LIFT-EXACT (all A2t negative shares ~ 0; not
expected -- the signed symbol IS the wall), else
AUTOCORR-DEFECT-MEASURED(band share, binding seat, beta_max
share); the honest expected outcome is the defect anatomy.

PART B -- THE INNOVATION DILATION (tangent surface, pivot ladder).
s_h = n_h - q_h is the Schur pivot = the Levinson/Durbin
prediction-error variance of the extended covariance Mt.  The
static (equal-degree) completion FAILED (round 59/60: Gram
completion fails at the x = +1 edge); the question frozen here:
does ONE (or few) latent boundary state(s) repair it -- the TFPT
parent-compression pattern?  SOURCE-ONLY REALIZATION (fit-free,
derived from the three-term data of the rung's own positive
chain, NO optimization): for latent dimension k in 1..K_MAX, take
A = trailing k x k block of the Jacobi matrix J(al, be) of rung
r2's positive chain, G = be[h - k] e_1 (the bond coupling the
tail block to the interior), C = e_k^T (boundary read-out),
process noise Q = I (w white), no measurement noise; the
discrete algebraic Riccati fixed point P = A P A^T + G G^T -
A P C^T (C P C^T)^{-1} C P A^T gives the innovation variance
sig2_k = C P C^T -- the k-state boundary innovation of the
positive chain's own tail.  MEASURED against the ladder of gaps
s_h (P2 split, 39 steps): per k the correlation R^2 of log s_h
vs log sig2_k, the FITTED scalar (geometric-mean ratio; typed
FITTED, exploratory), the ratio spread; tau-screen of sig2_k
(slope vs tau_1; a positive floor must screen ~ 0 to matter).
TYPED: INNOVATION-REPRO(k) iff R^2 >= 0.90 AND ratio spread
max/min <= 2 (a genuine reproduction); else
INNOVATION-FITTED(k_best, R^2) / INNOVATION-DEAD(counts).
CONTROL (the Weyl lesson): the same construction on the SMOOTH
companion chains -- if sig2_sm tracks the true s_h as well as the
true chain does, the dilation is wall-blind -> WALLBLIND-B /
WALLSEES-B(delta R^2).

FROZEN PROTOCOL:

 W   RACE LADDER (kill -> PIPELINE-BROKEN / WARD-BROKEN): W1 >=
     MIN_RUNGS = 40 faithful rungs (race verbatim); W2 WARD m_h >
     0 everywhere; W3 WARD two-route autocorrelation identity
     (direct correlate vs FFT route) <= AC2_WARD on the spot rung;
     W4 WARD L_a PSD: min symbol >= 0 exactly and
     lam_min(odd_toeplitz(ac_a)) >= -PSD_TOL x scale on the spot
     rung (both variants).

 T   TANGENT LADDER (kill -> PIPELINE-BROKEN): T1 42 rungs,
     chains complete; T2 >= 20 consecutive full-core steps; T3
     truth all-PSD; T4 REPRODUCTION gap min/med == 0.052/0.888
     (rtol 5e-2).

 A/B THE MEASUREMENTS as frozen above (typed, never kill).

 C   CONTROLS (kill -> WARD-BROKEN if silent): C1 Epstein +
     scramble at kz 9 on the race surface fire (lam_min < 0; at
     lam_min < 0 there is NO beta >= 0 with K - beta L_a >= 0 --
     the lift fails on the controls BY the wall violation,
     printed); C2 AST firewall; C3 NO-RH-CLAIM.

KILLS: K1 ladders (W1, T1-T3) -> PIPELINE-BROKEN; K2 wards
(W2-W4, T4, C1/C2) -> WARD-BROKEN.

VERDICT (frozen enum): AUTOCORR-INNOVATION-MEASURED with typed
sublabels AUTOCORR-LIFT-EXACT / AUTOCORR-DEFECT-MEASURED(...),
BAND-SEAT(...), WALLBLIND-A/WALLSEES-A(ratio),
INNOVATION-REPRO/FITTED/DEAD(...), WALLBLIND-B/WALLSEES-B,
SIG2-SCREEN-<PASS|RELOC|AMBIG>; else PIPELINE-BROKEN /
WARD-BROKEN.

FROZEN BARS: KZMAX = 150; MIN_RUNGS = 40; SUBSET_C = (13, 26, 40,
60); SPOT_KZ = 13; BAND_DELTA = 1e-2; AC2_WARD = 1e-10; PSD_TOL =
1e-10; K_MAX = 4; DARE_TOL = 1e-13; DARE_ITMAX = 5000; R2_REPRO =
0.90; SPREAD_REPRO = 2.0; SLOPE_PASS = 0.30; SLOPE_RELOC = 0.70;
CORE_J = (2,...,16); H_LADDER_MAX = 900; GAPMIN_REF = 0.052;
GAPMED_REF = 0.888 (rtol 5e-2); CTRL_KZ = 9; scramble seed 1.

ANTI-CIRCULARITY (frozen): no sigma_h, no defect eigenvector, no
pivot sign as input; K^{-1/2} (a factorization of the target)
appears ONLY inside the beta_max MEASUREMENT and its binding
vector -- disclosed above, never a certificate; a_h, L_a, the
Jacobi realizations and the smooth controls are source-only.

SMOKE-RUN DISCLOSURE (2026-08-10, before freezing): one smoke run
of this script (14/14 with the identical bars; NO bar, band,
count, rule or enum was moved after it; one mechanical numpy-2
scalar fix and the disclosed reachability-Gramian DARE start were
made during the smoke -- pure mechanics, no rule touched)
measured, recorded as the honest context the frozen run must
confirm: 67 faithful race rungs (17.4 s); two-route
autocorrelation 4.1e-16; L_a PSD (min symbol +2.5e-03, spot
lam_min +4.5 > 0).  LAG LEVEL: the deployed lag read is nearly
ORTHOGONAL to the comb autocorrelation -- cos(c_K, ac_a) med
-0.040 (A1) / -0.024 (A2), cos(-c_at, ac_a) med +0.049 (A1) /
+0.032 (A2): NOT an autocorrelation shape at all (the a priori
hope that A2 is a strong Wiener-Khinchin match is dead on
arrival).  SYMBOL LEVEL -- THE HEADLINE: the non-liftable part IS
THE x = +1 BAND AGAIN: residual neg-mass share med 0.20 (TAR-K),
band share (x > 1 - 1e-2) med 0.53 with peak-x med +1.0000 on
BOTH variants (TAR-AT: neg share 0.50, band share 0.24, peak-x
+1.0000) -- the same edge seat as the round-59/60 moment/Gram
obstruction.  COMPRESSED LEVEL (subset): beta_max > 0 on 4/4 but
VACUOUS -- explained share beta_max tr(L_a)/tr(K) med 2.5e-07;
the BINDING vector is entirely in the band (band share
0.998..1.000, peak x +1.000 on 4/4): what stops the lift is
exactly the +1-edge channel; negidx(K - beta* L_a) = 0 on 4/4
(beta* is tiny/negative since cos ~ 0 -- recorded, near-vacuous);
WALL-BLINDNESS: beta_max(prime)/beta_max(smooth) med 1.45 (range
0.25..12.6, falling with depth) -> WALLBLIND-A typed (the lift
coefficient barely distinguishes the true comb from PNT).
INNOVATION: the tail-Jacobi DARE converges on 39/39 steps for
every k = 1..4 but the innovation variance is a near-CONSTANT
per k (k = 1: 0.238 in [0.203, 0.284]; k = 4: 0.0037 narrow)
while s_h spans 0.052..3.4 -- R^2(log-log) <= 0.07 for all k,
ratio spread ~ 340: the few-latent-state boundary innovation
does NOT reproduce the pivot ladder ->
INNOVATION-FITTED-EXPLORATORY(k = 4, R^2 = 0.069) = effectively
DEAD; the smooth-chain control is equally uninformative (R^2 <=
0.024) -> WALLBLIND-B (the tail three-term data is classical --
consistent with rounds 59-61); sig2 tau-screens PASS trivially
(slopes +0.002..+0.007) BUT as near-constants they carry no wall
content (said plainly).  Fail-first preserved: nothing was
weakened; all typed outcomes are measurements.

SPEC v1 (2026-08-10, frozen + SHA-hashed before the frozen run):
everything above.  Mechanical concretizations frozen with v1: (i)
race ladder verbatim (arithmetic_lift_race machinery), eigvalsh
for m_h on all rungs, eigh only on SUBSET_C; (ii) tent deposit
a[i] = sum w_n max(0, 1 - |i D - u_n|/D); circular padding to L =
2M - 2; (iii) beta_max via eigh(K) -> K^{-1/2}, lam_max of the
symmetrized W = K^{-1/2} L_a K^{-1/2}; binding vector v0 =
K^{-1/2} u_max, normalized; band shares via |FFT(v0 pad)|^2 on
the folded x grid; (iv) tangent pipeline verbatim from the v900
chain (probe-2 file of this round); (v) DARE fixed-point from a
200-step reachability-Gramian start (the plain G G^T start has
C P C^T = 0 for k > 1), convergence in relative Frobenius norm,
cpc guard 1e-300; (vi) OLS
population statistics; screens read positive subsets.

NO RH claim: a beta_max > 0 or a reproduced innovation law would
certify nothing about tau_h > 0 for all h; all outcomes are typed
measurements on the deployed family.  No marker moves.

FIREWALL: no zeros, no prime oracles (AST scan; banned ids
zetazero / nzeros / primerange / isprime / primepi / nextprime /
prevprime); v563 READ-ONLY; RNG only inside the declared scramble
control; stdout only.

Sources (read-only): v563_paper2_readouts; race machinery from
arithmetic_lift_race_probe.py; tangent machinery verbatim from
bfloor_node_congruence_probe.py (= v900 chain); the LAGS-NOT-
POSITIONS reading from the race probe and schur_envelope_identity_
probe (round 61, declared inputs).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/innovation_autocorr_lift_probe.py
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

KZMAX = 150
MIN_RUNGS = 40
SUBSET_C = (13, 26, 40, 60)
SPOT_KZ = 13
BAND_DELTA = 1e-2
AC2_WARD = 1e-10
PSD_TOL = 1e-10
K_MAX = 4
DARE_TOL = 1e-13
DARE_ITMAX = 5000
R2_REPRO = 0.90
SPREAD_REPRO = 2.0
SLOPE_PASS = 0.30
SLOPE_RELOC = 0.70
CORE_J = (2, 4, 6, 8, 10, 12, 14, 16)
H_LADDER_MAX = 900
GAPMIN_REF = 0.052
GAPMED_REF = 0.888
GAP_RTOL = 5e-2
CTRL_KZ = 9
NG_SMOOTH = 6000
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


def ols_line(x, y):
    x = np.asarray(x, float)
    y = np.asarray(y, float)
    vx = float(np.var(x))
    if vx == 0.0:
        return float(np.mean(y)), 0.0, float("nan")
    b = float(np.cov(x, y, bias=True)[0, 1] / vx)
    a = float(np.mean(y) - b * np.mean(x))
    ss = float(np.sum((y - a - b * x) ** 2))
    st = float(np.sum((y - np.mean(y)) ** 2))
    return a, b, (1.0 - ss / st if st > 0 else float("nan"))


def smooth_comb(alpha, ng=NG_SMOOTH):
    ug = (np.arange(ng) + 0.5) * (2.0 * alpha / ng)
    mg = 2.0 * np.exp(ug / 2.0) * (2.0 * alpha / ng)
    return ug, mg


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


def tent_deposit(uu, w, M, D):
    """a[i] = sum_n w_n max(0, 1 - |i D - u_n| / D) (frozen: plain
    tent, no edge reflection -- a is a new object)."""
    a = np.zeros(M)
    for u_j, w_j in zip(uu, w):
        i0 = int(math.floor(u_j / D))
        for i in range(max(0, i0 - 1), min(M, i0 + 2)):
            v = 1.0 - abs(i * D - u_j) / D
            if v > 0.0:
                a[i] += w_j * v
    return a


def circ_autocorr(a, L):
    ap = np.zeros(L)
    ap[:len(a)] = a
    F = np.fft.fft(ap)
    ac = np.fft.ifft(np.abs(F) ** 2)
    assert float(np.max(np.abs(ac.imag))) <= 1e-9 * max(
        1.0, float(np.max(np.abs(ac.real))))
    return ac.real, float(np.min(np.abs(F) ** 2))


def grid_density(c):
    c = np.asarray(c, float)
    a = np.concatenate([c, c[-2:0:-1]])
    d = np.fft.fft(a)
    assert float(np.max(np.abs(d.imag))) <= 1e-9 * max(
        1.0, float(np.max(np.abs(d.real))))
    return d.real


def band_anatomy(d_R, L):
    """negative-part anatomy of a symbol on the folded x grid."""
    xg = np.cos(2.0 * math.pi * np.arange(L) / L)
    neg = d_R < 0.0
    mneg = float(np.sum(-d_R[neg]))
    mtot = float(np.sum(np.abs(d_R)))
    if mneg <= 0.0:
        return 0.0, 0.0, float("nan")
    band = neg & (xg > 1.0 - BAND_DELTA)
    bsh = float(np.sum(-d_R[band])) / mneg
    xpk = float(xg[int(np.argmin(d_R))])
    return mneg / max(mtot, 1e-300), bsh, xpk


def vec_band_seat(v0, M, L):
    """frequency-band seat of a model vector via |FFT|^2 on the
    folded x grid."""
    vp = np.zeros(L)
    vp[:len(v0)] = v0
    P = np.abs(np.fft.fft(vp)) ** 2
    xg = np.cos(2.0 * math.pi * np.arange(L) / L)
    tot = float(np.sum(P))
    bsh = float(np.sum(P[xg > 1.0 - BAND_DELTA])) / max(tot,
                                                        1e-300)
    xpk = float(xg[int(np.argmax(P))])
    return bsh, xpk


def dare_sig2(al, be, k):
    """innovation variance of the trailing-k Jacobi tail
    realization (A = tail block, G = coupling bond e_1, C = e_k)."""
    h1 = len(al)
    if k >= h1 or len(be) < k:
        return float("nan"), False
    A = np.zeros((k, k))
    for i in range(k):
        A[i, i] = al[h1 - k + i]
    for i in range(k - 1):
        A[i, i + 1] = be[h1 - k + i]
        A[i + 1, i] = be[h1 - k + i]
    g = np.zeros((k, 1))
    g[0, 0] = be[h1 - k - 1] if h1 - k - 1 >= 0 else 1.0
    Cv = np.zeros((1, k))
    Cv[0, k - 1] = 1.0
    # start from a finite-horizon reachability Gramian (the plain
    # G G^T start has C P C^T = 0 for k > 1)
    P = np.zeros((k, k))
    Xj = g @ g.T
    for _ in range(200):
        P = P + Xj
        Xj = A @ Xj @ A.T
    P = 0.5 * (P + P.T)
    for _ in range(DARE_ITMAX):
        cpc = float((Cv @ P @ Cv.T)[0, 0])
        if not np.isfinite(cpc) or cpc <= 1e-300:
            return float("nan"), False
        Kg = (P @ Cv.T) / cpc
        Pn = A @ (P - Kg @ (Cv @ P)) @ A.T + g @ g.T
        Pn = 0.5 * (Pn + Pn.T)
        dv = float(np.linalg.norm(Pn - P)
                   / max(np.linalg.norm(P), 1e-300))
        P = Pn
        if dv <= DARE_TOL:
            return float((Cv @ P @ Cv.T)[0, 0]), True
    return float((Cv @ P @ Cv.T)[0, 0]), False


# --------------- tangent pipeline (v900 verbatim, via probe-2)
import bfloor_node_congruence_probe as tang  # noqa: E402


def main():
    section("PRIME.PORT.AUTOCORR.LIFT.01 + "
            "PRIME.PORT.INNOVATION.DILATION.01 (EXPLORATION ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s"
          % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
    print("    NO RH claim; no marker moves.")
    print("\nS0 -- firewall")
    check("S0.1 AST firewall clean (C2)", not ast_scan(BANNED_IDS))

    # ------------------------------------------------------------ W
    section("W -- the race ladder + lift data")
    rungs = []
    for kz in range(2, KZMAX + 1):
        try:
            rr = core.build_window(kz)
        except Exception:
            continue
        if not (core.H_MIN <= rr["h"] <= core.HCAP):
            continue
        if rr["X"] > core.ATOM_MAX:
            continue
        alpha, M, D, h = rr["alpha"], rr["M"], rr["D"], rr["h"]
        uu = np.asarray(rr["uu"], float)
        mu = 2.0 * np.asarray(rr["lam"], float)
        c_at = np.asarray(core.atom_lags_at(alpha, M, uu, mu)[0],
                          float)
        c_ar = np.asarray(core.arch_lags(M, D), float)
        cK = c_ar + c_at
        L = 2 * M - 2
        row = dict(kz=kz, alpha=float(alpha), M=M, D=float(D),
                   h=h, L=L)
        Kt = core.odd_toeplitz(cK, M)
        row["m"] = float(np.linalg.eigvalsh(Kt)[0])
        acs = {}
        for vtag, wts in (("A1", mu), ("A2", np.sqrt(mu))):
            a = tent_deposit(uu, wts, M, D)
            ac, smin = circ_autocorr(a, L)
            acs[vtag] = (ac[:M], smin)
            for ttag, ct in (("K", cK), ("AT", -c_at)):
                acv = ac[:M]
                cosv = float(ct @ acv) / max(
                    float(np.linalg.norm(ct)
                          * np.linalg.norm(acv)), 1e-300)
                bst = float(ct @ acv) / max(float(acv @ acv),
                                            1e-300)
                dR = grid_density(ct - bst * acv)
                nsh, bsh, xpk = band_anatomy(dR, L)
                row["%s_%s" % (ttag, vtag)] = (cosv, bst, nsh,
                                               bsh, xpk)
        row["smin"] = min(acs["A1"][1], acs["A2"][1])
        if kz in SUBSET_C or kz == SPOT_KZ:
            row["_cK"] = cK
            row["_cat"] = c_at
            row["_ac"] = {k: v[0] for k, v in acs.items()}
            row["_uu"] = uu
            row["_mu"] = mu
        del Kt
        rungs.append(row)
    rungs.sort(key=lambda r: (r["h"], r["kz"]))
    check("W1 faithful ladder >= %d rungs" % MIN_RUNGS,
          len(rungs) >= MIN_RUNGS,
          "%d rungs, h %d..%d  [%.1f s]"
          % (len(rungs), rungs[0]["h"], rungs[-1]["h"],
             time.time() - T0), kill="K1")
    if KILLS:
        return finish({})
    ms = np.array([r["m"] for r in rungs])
    check("W2 WARD truth margin m_h > 0 everywhere (min %.3e)"
          % float(ms.min()), bool(np.all(ms > 0)), kill="K2")
    spot = next(r for r in rungs if r["kz"] == SPOT_KZ)
    a_sp = tent_deposit(spot["_uu"], np.sqrt(spot["_mu"]),
                        spot["M"], spot["D"])
    ac_direct = np.array([
        float(np.sum(a_sp * np.roll(np.concatenate(
            [a_sp, np.zeros(spot["L"] - spot["M"])]), -l)[
                :spot["M"]]))
        for l in range(4)])
    ac_fft, _s = circ_autocorr(a_sp, spot["L"])
    dev_ac = float(np.max(np.abs(ac_direct - ac_fft[:4]))
                   / max(abs(ac_fft[0]), 1e-300))
    check("W3 WARD two-route autocorrelation on the spot rung "
          "(first 4 lags): dev %.2e <= %.0e" % (dev_ac, AC2_WARD),
          dev_ac <= AC2_WARD, kill="K2")
    smin_all = min(r["smin"] for r in rungs)
    La_sp = core.odd_toeplitz(ac_fft[:spot["M"]], spot["M"])
    lmin_sp = float(np.linalg.eigvalsh(La_sp)[0])
    sc_sp = float(np.max(np.abs(La_sp)))
    check("W4 WARD L_a PSD: min symbol %.2e >= 0 on all rungs; "
          "spot lam_min(L_a) %.2e >= -%.0e x scale %.1e"
          % (smin_all, lmin_sp, PSD_TOL, sc_sp),
          smin_all >= -1e-300 and lmin_sp >= -PSD_TOL * sc_sp,
          kill="K2")
    del La_sp

    # ------------------------------------------------------------ A
    section("A1t/A2t -- lag + symbol level (all rungs)")
    lab_band = {}
    for ttag in ("K", "AT"):
        for vtag in ("A1", "A2"):
            key = "%s_%s" % (ttag, vtag)
            cosv = np.array([r[key][0] for r in rungs])
            nsh = np.array([r[key][2] for r in rungs])
            bsh = np.array([r[key][3] for r in rungs])
            xpk = np.array([r[key][4] for r in rungs])
            print("    TAR-%s / %s: cos med %+0.3f [%+0.3f, "
                  "%+0.3f]; residual neg-mass share med %.3f; "
                  "band(x > 1-%.0e) share med %.4f; peak-x med "
                  "%+.4f"
                  % (ttag, vtag, float(np.median(cosv)),
                     float(np.min(cosv)), float(np.max(cosv)),
                     float(np.median(nsh)), BAND_DELTA,
                     float(np.median(bsh)),
                     float(np.median(xpk))), flush=True)
            lab_band[key] = (float(np.median(nsh)),
                             float(np.median(bsh)),
                             float(np.median(xpk)))
    exact = all(v[0] <= 1e-6 for v in lab_band.values())
    a_typ = ("AUTOCORR-LIFT-EXACT" if exact else
             "AUTOCORR-DEFECT-MEASURED(negshare=%.2f, "
             "bandshare=%.4f, peakx=%+.3f @ TAR-K/A2)"
             % lab_band["K_A2"])
    check("A.1 typed: %s -- is the non-liftable part the x = +1 "
          "band?" % a_typ, True)

    section("A3t -- compressed level on the subset + "
            "wall-blindness")
    bmaxs, shares, bseats, xseats, negidx, bratio = ([], [], [],
                                                     [], [], [])
    for r in rungs:
        if r["kz"] not in SUBSET_C:
            continue
        M, L, D = r["M"], r["L"], r["D"]
        K = core.odd_toeplitz(r["_cK"], M)
        w, V = np.linalg.eigh(K)
        Ki = (V / np.sqrt(w)) @ V.T
        res = {}
        for atag, ac in (("prime", r["_ac"]["A2"]), ):
            La = core.odd_toeplitz(ac, M)
            Wm = Ki @ La @ Ki
            Wm = 0.5 * (Wm + Wm.T)
            ww, UU = np.linalg.eigh(Wm)
            bmax = 1.0 / float(ww[-1])
            v0 = Ki @ UU[:, -1]
            v0 = v0 / float(np.linalg.norm(v0))
            bsh, xpk = vec_band_seat(v0, M, L)
            res[atag] = bmax
            bmaxs.append(bmax)
            shares.append(bmax * float(np.trace(La))
                          / float(np.trace(K)))
            bseats.append(bsh)
            xseats.append(xpk)
            bst = r["K_A2"][1]
            Rc = K - bst * La
            negidx.append(int(np.sum(np.linalg.eigvalsh(Rc)
                                     < 0.0)))
        ug, mg = smooth_comb(r["alpha"])
        a_smv = tent_deposit(ug, np.sqrt(mg), M, D)
        ac_sm, _ = circ_autocorr(a_smv, L)
        La_s = core.odd_toeplitz(ac_sm[:M], M)
        Wm = Ki @ La_s @ Ki
        Wm = 0.5 * (Wm + Wm.T)
        bmax_s = 1.0 / float(np.linalg.eigvalsh(Wm)[-1])
        bratio.append(res["prime"] / max(bmax_s, 1e-300))
        print("    kz %3d (h %4d): beta_max %.3e; explained share"
              " %.2e; binding band-share %.2e peak-x %+.3f; "
              "negidx(K - beta* L_a) %d/%d; beta_max prime/smooth"
              " %.3f"
              % (r["kz"], r["h"], bmaxs[-1], shares[-1],
                 bseats[-1], xseats[-1], negidx[-1], r["h"],
                 bratio[-1]), flush=True)
        del K, Ki
    wb = float(np.median(bratio))
    a3 = ("WALLSEES-A(ratio=%.2f)" if wb >= 3.0 else
          "WALLBLIND-A(ratio=%.2f)") % wb
    check("A.2 typed: beta_max > 0 on %d/%d, explained share med "
          "%.1e (VACUOUS sliver if << 1); binding seat peak-x med "
          "%+.3f; %s (the prime deposit vs the smooth deposit)"
          % (int(np.sum(np.array(bmaxs) > 0)), len(bmaxs),
             float(np.median(shares)),
             float(np.median(xseats)), a3), True)

    # ------------------------------------------------------------ T/B
    section("T -- the tangent ladder (v900 chain) + B: the "
            "innovation dilation")
    zones = tang.ladder_zones()
    check("T1 tangent rung count 42", len(zones) == 42,
          "found %d" % len(zones), kill="K1")
    truth = []
    sm_map = {}
    for kz in zones:
        r = tang.gram_anatomy(kz, keep_chain=True)
        if r is None:
            truth.append(None)
            continue
        truth.append(r)
        rs = tang.gram_anatomy(kz, world_fn=tang.world_smooth,
                               keep_chain=True)
        if isinstance(rs, dict):
            sm_map[kz] = rs
    ok_chain = all(r is not None for r in truth)
    check("T1b all chains complete", ok_chain, kill="K1")
    if not ok_chain:
        return finish({})
    truth.sort(key=lambda r: (r["h"], r["kz"]))
    full = [r for r in truth if r["core_ok"]]
    ok_psd = all(r["negA"] == 0 and r["negR"] == 0
                 and r["negS"] == 0 for r in full)
    check("T3 WARD truth all-PSD (A, R, S)", ok_psd, kill="K1")
    steps = []
    for r1, r2 in zip(truth, truth[1:]):
        if not (r1.get("core_ok") and r2.get("core_ok")):
            continue
        if r1["lamS"] <= 0.0 or r1["negA"] > 0:
            continue
        steps.append((r1, r2))
    check("T2 >= 20 consecutive full-core steps",
          len(steps) >= 20, "%d steps" % len(steps), kill="K1")
    gaps, taus, sig2 = [], [], {k: [] for k in range(1, K_MAX + 1)}
    sig2_sm = {k: [] for k in range(1, K_MAX + 1)}
    n_dead = 0
    for r1, r2 in steps:
        wS, VS = np.linalg.eigh(r1["S"])
        Q = tang.householder_frame(VS[:, 0])
        Mt = Q.T @ (r2["S"] / r1["tau"]) @ Q
        Mt = 0.5 * (Mt + Mt.T)
        b = Mt[1:, 0]
        B = Mt[1:, 1:]
        gap = float(Mt[0, 0]) - float(b @ np.linalg.solve(B, b))
        gaps.append(gap)
        taus.append(r1["tau"])
        al, be, _m0 = r2["chain"]
        for k in range(1, K_MAX + 1):
            s2, okc = dare_sig2(al, be, k)
            sig2[k].append(s2 if okc else float("nan"))
            if not okc:
                n_dead += 1
        smr = sm_map.get(r2["kz"])
        for k in range(1, K_MAX + 1):
            if smr is None or "chain" not in smr:
                sig2_sm[k].append(float("nan"))
                continue
            als, bes, _m = smr["chain"]
            s2, okc = dare_sig2(als, bes, k)
            sig2_sm[k].append(s2 if okc else float("nan"))
    gaps = np.array(gaps)
    taus = np.array(taus)
    gmin, gmed = float(np.min(gaps)), float(np.median(gaps))
    check("T4 REPRODUCTION gap min/med %.4f/%.4f == %.3f/%.3f"
          % (gmin, gmed, GAPMIN_REF, GAPMED_REF),
          abs(gmin / GAPMIN_REF - 1.0) <= GAP_RTOL
          and abs(gmed / GAPMED_REF - 1.0) <= GAP_RTOL,
          kill="K2")
    best_k, best_r2 = None, -1.0
    scr_lab = "n/a"
    for k in range(1, K_MAX + 1):
        s2 = np.array(sig2[k])
        okm = np.isfinite(s2) & (s2 > 0) & (gaps > 0)
        if int(np.sum(okm)) < 5:
            print("    k = %d: DARE dead on %d steps"
                  % (k, int(np.sum(~okm))))
            continue
        _a, sl, r2f = ols_line(np.log(s2[okm]),
                               np.log(gaps[okm]))
        ratio = gaps[okm] / s2[okm]
        spread = float(np.max(ratio) / np.min(ratio))
        cfit = float(np.exp(np.mean(np.log(ratio))))
        s2s = np.array(sig2_sm[k])
        oks = np.isfinite(s2s) & (s2s > 0) & (gaps > 0)
        r2s = float("nan")
        if int(np.sum(oks)) >= 5:
            _a2, _sl2, r2s = ols_line(np.log(s2s[oks]),
                                      np.log(gaps[oks]))
        _a3, slt, r2t = ols_line(np.log(taus[okm]),
                                 np.log(s2[okm]))
        lab = ("PASS" if abs(slt) <= SLOPE_PASS else
               "RELOC" if slt >= SLOPE_RELOC else "AMBIG")
        print("    k = %d: sig2 med %.4f [%.4f, %.4f]; R^2(log s "
              "vs log sig2) %.3f (smooth-chain %.3f); fitted "
              "scalar %.3f, spread %.1f; tau-screen slope %+.3f "
              "(%s)"
              % (k, float(np.median(s2[okm])),
                 float(np.min(s2[okm])), float(np.max(s2[okm])),
                 r2f, r2s, cfit, spread, slt, lab), flush=True)
        if r2f > best_r2:
            best_r2, best_k = r2f, k
            best = (r2f, r2s, spread, cfit)
            scr_lab = "SIG2-SCREEN-%s(slope=%+.3f)" % (lab, slt)
    if best_k is None:
        b_typ = "INNOVATION-DEAD(DARE dead %d)" % n_dead
        wbB = "n/a"
    else:
        r2f, r2s, spread, cfit = best
        if r2f >= R2_REPRO and spread <= SPREAD_REPRO:
            b_typ = "INNOVATION-REPRO(k=%d, R2=%.3f)" % (best_k,
                                                         r2f)
        else:
            b_typ = ("INNOVATION-FITTED-EXPLORATORY(k=%d, "
                     "R2=%.3f, spread=%.1f)"
                     % (best_k, r2f, spread))
        dwb = r2f - (r2s if np.isfinite(r2s) else 0.0)
        wbB = ("WALLSEES-B(dR2=%.3f)" if dwb >= 0.2 else
               "WALLBLIND-B(dR2=%.3f)") % dwb
    check("B.1 typed: %s / %s / %s -- the static (equal-degree) "
          "completion failure is NOT repaired by %d latent "
          "boundary state(s) unless REPRO"
          % (b_typ, wbB, scr_lab, K_MAX), True)

    # ------------------------------------------------------------ C
    section("C -- controls at kz %d (race surface)" % CTRL_KZ)
    rr9 = core.build_window(CTRL_KZ)
    alpha9, M9, D9 = rr9["alpha"], rr9["M"], rr9["D"]
    c_ar9 = np.asarray(core.arch_lags(M9, D9), float)
    N_E = int(math.floor(math.exp(2.0 * alpha9))) + 1
    lamE_ = lambda_eps(N_E)
    nn = np.nonzero(np.abs(lamE_) > 1e-12)[0]
    c_E = np.asarray(core.atom_lags_at(
        alpha9, M9, np.log(nn.astype(float)),
        2.0 * lamE_[nn] / np.sqrt(nn.astype(float)))[0], float)
    rr_s = core.build_window(CTRL_KZ, scramble_seed=1)
    c_s = np.asarray(core.atom_lags_at(
        rr_s["alpha"], rr_s["M"], np.asarray(rr_s["uu"], float),
        2.0 * np.asarray(rr_s["lam"], float))[0], float)
    fired = True
    for name, c_c in (("Epstein", c_E), ("scramble", c_s)):
        lam_c = float(np.linalg.eigvalsh(core.odd_toeplitz(
            c_ar9 + c_c, M9))[0])
        fired &= lam_c < 0
        print("    %-9s: lam_min %+.3e -> %s (lam_min < 0 => NO "
              "beta >= 0 admits K - beta L_a >= 0: the lift "
              "fails by the wall violation)"
              % (name, lam_c, "FIRES" if lam_c < 0 else
                 "SILENT"))
    check("C1 WARD both controls fire", fired, kill="K2")

    return finish(dict(a=a_typ, a3=a3, b=b_typ, wbB=wbB,
                       scr=scr_lab))


def finish(labels):
    section("V -- FROZEN VERDICT")
    n_pass = sum(1 for _n, okk in CHECKS if okk)
    n_tot = len(CHECKS)
    if KILLS:
        VERDICT = {"K1": "PIPELINE-BROKEN",
                   "K2": "WARD-BROKEN"}[KILLS[0]]
        print("\n  VERDICT: %s" % VERDICT)
    else:
        VERDICT = ("AUTOCORR-INNOVATION-MEASURED / %(a)s / %(a3)s "
                   "/ %(b)s / %(wbB)s / %(scr)s" % labels)
        print("\n  VERDICT: %s" % VERDICT)
    print("""
  HONEST FRAME (as frozen): both lifts are typed measurements --
  the autocorrelation square is PSD by construction and can only
  UNDER-explain the wall (the explained share and the defect
  anatomy are the content); the innovation dilation is fit-free
  from the chain's own three-term data and its failure/fit is
  recorded as such.  NO RH claim.  No marker moves.""")
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed"
          % (time.time() - T0, n_tot, n_tot - n_pass))
    return 0 if n_pass == n_tot else 1


if __name__ == "__main__":
    raise SystemExit(main())
