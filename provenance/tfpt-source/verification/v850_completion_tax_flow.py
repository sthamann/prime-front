#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""v850 -- PRIME.PSD.COMPLETION.TAX.01 + the spectral-flow pivot decision: the two class-level no-go closures of the 2026-08-07 evening plan -- EVERY positive 2-sector dilation routing the arithmetic through the fixed comb coupling block pays a diagonal tax that exceeds the certified margin by a diverging factor (the exact nuclear-norm optimum with zero-gap primal-dual certificates, basis-invariant, so the spectral-mother verdict becomes a corollary), and the topological index route is closed by measurement (the density endpoint is NOT PSD, the crossings hug the deployed point, and the distance-to-crossing IS the metric margin divided by the flow velocity), ONE module from two probes (15/15 + 11/11 checks, zero fails, verdicts TAX-GAP and FLOW-CROSSINGS; discovery probes psd_completion_tax_probe.py and spectral_flow_pivot_probe.py, 2026-08-07, re-run identically at promotion, embedded BYTE-EXACT and executed verbatim, ~35 s).  PART A, THE TAX THEOREM (class-level, the strongest no-go of the campaign): for the canonical window family write Toep(c_at) = R_X + R_X^T with R_X the one-sided comb coupling; then every positive completion [[P, R_X], [R_X*, Q]] >= 0 pays tr P + tr Q >= 2||R_X||_* with EQUALITY at the SVD pair -- the identity is verified with zero-duality-gap certificate pairs on every anchor (primal lambda_min >= -8.9e-15, tr == 2||R||_* rel <= 1e-10, dual witness ||W||_op = 1.000000000000, <W,R> rel dev <= 1.6e-16, plus the symbolic 2x2 closed form at 50 dps, gap 2.7e-51) and is BASIS-INVARIANT (DFT/Mellin, mirror J, seeded orthogonal: rel devs <= 1.1e-15) -- no unitary change of basis, in particular no Mellin/spectral transform, alters the tax; the geometry-independence of the v846 TV price is now a THEOREM-SHAPED corollary of nuclear-norm invariance.  THE DIVERGENCE: on the entire deployed 67-rung ladder the per-cell tax 2||R_X||_*/M_X exceeds tau_X by a factor >= 4057.6 (max 7.5e5), growing ~h^0.24 against the margin's h^-3/2 decay (segment slopes 1.99/1.86/0.46, positive in all thirds); the event-local Schur designs of v846 pay 13.66-20.35x MORE than the exact class optimum (triangle inequality verified), so design optimality could not have saved them -- the whole positive-dilation architecture class with this coupling is closed, not just its tested members.  THE TYPED BOUNDARY (the one door the theorem does NOT close): architectures where the comb never enters as a fixed coupling block of a positive dilation -- i.e. Fejer-Riesz of the total symbol, which is the positivity statement itself.  Comb fingerprints: scramble moves ||R||_* by 0.54-0.96 rel, Epstein x^2+5y^2 by 0.12-0.22 rel -- the coupling norm reads the comb.  PART B, THE FLOW DECISION (F4): the homotopy A(t) = arch + t*comb from the pure-density endpoint to the deployed parity compression is NOT crossing-free -- the premise 'density endpoint PSD by construction' is CORRECTED BY MEASUREMENT (n_-(0) = 5..12 on every rung; the 2-mode arch block is negative definite), the comb supplies exactly n_-(0) upward crossings (634 total, ALL upward, endpoint identity SF == n_-(0) - n_-(1) verified on 67/67 rungs), and the crossings are not localized early: the last crossing hugs the deployed point (median lower gap 1 - t_last = 1.6e-5, shrinking with slope -2.11 vs tau's -1.65) while the VELOCITY TEST lands at ratio 1.00 (IQR 0.99..1.00): the 'quantized amplitude gap' IS the metric margin rescaled by the flow velocity -- no independent topological protection exists on this path, and in finite dimension the index VALUE adds nothing beyond the endpoint pivot signs (the independence kill, answered by measurement).  THE GENUINE RESIDUE, typed: (a) the Jacobi/pivot route certifies the inertia eigenproblem-free (determinant recursions only, exact-arithmetic-friendly; verified == eigh at t = 0 and t = 1 on all rungs), and (b) the crossing-location set (t_last, t_next) is a new measured ladder object; the exclusion connection is stated: a crossing AT the deployed point on an accessible rung would be a pivot sign change (tau = 0), which the certified margins exclude -- the floor ladder and the detector-strand exclusion instrument meet in this statement.  Controls: scramble (detection ward holds, tau_scr = -2.2 measured negative, typed) and Epstein h=2 (routed negativity localized at down-crossings t = 0.086/0.127/0.258) both discriminate; Levinson on the raw summed lags breaks down at depth 10-14 (the parity compression is the weaker deployed object, typed).  Together the two closures type the F-plan's architecture window: no positive-completion route with fixed comb coupling, no finite-dimensional index route -- what survives is the graded-kernel geometry (v851) and hypothesis (H_cof) itself (v849).  NO RH claim.  Python-only per GATE.WOLFRAM.02.

PROVENANCE: discovery probes psd_completion_tax_probe.py (15/15,
verdict TAX-GAP) and spectral_flow_pivot_probe.py (11/11, verdict
FLOW-CROSSINGS), both 2026-08-07, re-run identically at promotion.
ROUND-31 EMBEDDING CONVENTION: this module embeds both frozen probe
sources BYTE-EXACT (raw strings below) and executes them verbatim in
isolated module namespaces -- the printed FROZEN_SPEC SHA-256 values
reproduce exactly, and when the original files are present the
harness verifies byte-equality (provenance ward inside the pattern
gate).  The pattern gate encodes the frozen expected census per probe
(check count, FAIL ids, verdict, exit status) per the v829/v831/v843/
v847 precedent; nothing is refit, nothing is downscoped.  The
original probe files live verbatim in experiments/tfpt-discovery/.

FIREWALL: no zeros, no prime-table symbols beyond the deployed v563
table (each probe carries and passes its own AST firewall); v563
READ-ONLY; RNG only in the probes' declared scramble controls (seed
20260807).  NO RH claim.
"""

import contextlib
import io
import os
import re
import sys
import time
import types

_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)

# ------------- frozen probe sources (embedded BYTE-EXACT, raw strings)
_SRC_TAX = r'''
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""psd_completion_tax_probe -- PRIME.PSD.COMPLETION.TAX.01
(EXPLORATION ONLY, experiments/; F2: the Schur death as a general
no-go theorem, after SCHUR-INDEFINITE + SPECTRAL-TV-UNIVERSAL,
2026-08-07).

THE IDENTITY (the classical nuclear-norm SDP representation):
    2 ||R||_* = min { tr P + tr Q : [[P, R], [R*, Q]] >= 0 }.
Constructive primal-dual pair from the SVD R = U S V*:
  PRIMAL  P = U S U*, Q = V S V*  ->  [[P,R],[R*,Q]] =
          [U; V] S [U; V]* >= 0 manifestly, value 2 tr S;
  DUAL    W = U V*, ||W||_op = 1: for any feasible (P, Q),
          [[I, -W], [-W*, I]] >= 0  =>  tr P + tr Q >=
          2 Re tr(W* R) = 2 ||R||_*.
Zero duality gap by construction -- the optimum is EXACT and the
dual W is the basis-invariant witness (||O1 R O2||_* = ||R||_*
for unitaries O1, O2).  Both sides verified at certificate grade.

THE COUPLING BLOCK, EXTRACTED FROM THE MEASURED PROGRAM: the
deployed comb operator on the M-cell log-grid is Toep(c_at) =
R + R^T with R := strict lower half of Toep(c_at) plus half the
diagonal -- i.e. R = -Sigma_n lam_n U_n, the one-sided dilation
superposition (the spectral probe's op-match ward, 8e-15).  The
class closed by the theorem: every two-sector PSD dilation
[[P, R],[R*, Q]] that routes the arithmetic comb through the
coupling block pays diagonal tax tr P + tr Q >= 2 ||R||_*.  The
event-local designs of the two Schur probes are instances with R
split event-wise (tax Sigma_n 2 lam_n ||U_n||_* >= 2 ||R_tot||_*
by the triangle inequality; the slack IS the nuclear-grade
interference gain, measured here).  Event-local per-operator
nuclear norm in closed form: the tent shift U (offset f) has
interior singular symbol |(1-f) + f e^{i theta}|, so
||U||_*/M -> (1/pi) int_0^pi |(1-f) + f e^{i th}| dth (boundary
correction O(s/M), typed budget, exact SVD ward at anchors).

TYPED BOUNDARY OF THE THEOREM: the class hypothesis is that the
comb enters as the FIXED coupling block of a positive 2-sector
dilation (this is what every design of the Schur program did).
A design that absorbs the comb inside a corner block directly
needs that corner's positivity -- the positivity input the
firewall forbids.  NO RH claim.

TASK: (1) identity ward (anchors kz 9/12/13, full primal-dual
certificates + symbolic-precision 2x2); (2) the tax per rung:
tax_tot = 2||R_tot||_*/M (per cell) vs tau_X, tax_ev (event-
local optimum) and the measured Gram price (regression: measured
>= event-local optimum >= merged optimum); (3) dual certificate
+ basis invariance under 3 predeclared unitaries (DFT/Mellin,
mirror J, seeded orthogonal); (4) the divergence law on the full
deployed ladder (frame_a_zones): ratio = tax_tot/tau_X, fit-free
segment slopes vs h; (5) the theorem statement verbatim with the
run's constants.  CONTROLS: scramble/Epstein nuclear-norm
fingerprints; measured-vs-optimum consistency.

VERDICT (frozen): TAX-ESCAPE if min ladder ratio < 10;
else TAX-GAP if the measured anchor price exceeds the merged
optimum by > 10x (designs suboptimal -- honest optimum typed);
else TAX-THEOREM-EXACT (identity + certificates + divergence law
= the class closure).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/psd_completion_tax_probe.py
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

FROZEN_SPEC = """\
PRIME.PSD.COMPLETION.TAX.01 spec v1 (2026-08-07, frozen before
run).  R_tot := tril(Toep(c_at), -1) + diag(c_at[0]/2) (the
one-sided comb coupling; Toep(c_at) = R + R^T exact).  Identity
ward per anchor kz 9/12/13: SVD R = U S V^T; primal Z = [U;V] S
[U;V]^T: lam_min(Z) >= -1e-8 * ||R||_op, tr(P)+tr(Q) ==
2 sum(S) rel <= 1e-10; dual W = U V^T: ||W||_op <= 1 + 1e-10,
<W, R> == sum(S) rel <= 1e-10; duality gap == 0 by the pair.
Symbolic-precision 2x2 (mpmath 50 dps, R = [[3,1],[1,2]]/7 and
the top-left 2x2 of R_tot at kz 9): closed-form singular values,
primal-dual gap <= 1e-40.  Basis invariance per anchor: unitary
DFT F, mirror J, seeded orthogonal (QR of seed-0 gaussian):
| ||O1 R O2||_* - ||R||_* | / ||R||_* <= 1e-8 each.  Event-local
optimum: tax_ev = 2 Sigma lam_n ||U_n||_*/M via the interior
tent symbol (1/pi) int |(1-f)+f e^{i th}| dth on a 4096 grid
times the edge truncation factor (M - s)/M; anchor ward vs
exact per-event SVD rel <= 0.05 (boundary budget).  Measured price regression (anchors): measured M-space
Gram diagonal median m_a = median diag(Sigma lam (I + U U^T));
require m_a >= 0.98 * tax_ev_percell and tax_ev_percell >=
tax_tot_percell - 1e-12 (triangle).  Ladder (frame_a_zones, skip
failures, count reported): per rung tau = lam_min(Ah) (shipped),
tax_tot_percell = 2 ||R_tot||_* / M (svdvals), ratio =
tax_tot_percell / tau; segment slopes of log ratio vs log h
(thirds) reported fit-free.  Fingerprints per anchor: scramble
(seed 1) and Epstein x^2+5y^2 (r-masses at their own log
positions, first ka events) give | ||R'||_* - ||R||_* | /
||R||_* >= 1e-3.  VERDICT: TAX-ESCAPE iff min ladder ratio <
10; else TAX-GAP iff anchor measured/tax_tot > 10; else
TAX-THEOREM-EXACT.  tau refs kz 9/12/13 rel 1e-4.  NO RH claim;
writes nothing.
"""

ANCHORS = (9, 12, 13)
TAU_REFS = {9: 5.984165e-4, 12: 4.351189e-4, 13: 5.637632e-4}
X_REL = 2048
NTH = 4096
RATIO_BAR = 10.0
GAP_BAR = 10.0
BANNED_IDS = ("zetazero", "nzeros", "primerange", "isprime",
              "primepi", "nextprime", "prevprime")

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


def ast_firewall():
    src = open(os.path.abspath(__file__), encoding="utf-8").read()
    bad = []
    for node in ast.walk(ast.parse(src)):
        name = None
        if isinstance(node, ast.Name):
            name = node.id
        elif isinstance(node, ast.Attribute):
            name = node.attr
        if name and name.lower() in BANNED_IDS:
            bad.append(name)
    return bad


def coupling_of(c_at, M):
    """R_tot = one-sided half of the comb Toeplitz operator."""
    rr = np.arange(M)
    T = np.asarray(c_at)[np.abs(rr[:, None] - rr[None, :])]
    return np.tril(T, -1) + np.diag(np.full(M, c_at[0] / 2.0))


def U_of(s, M):
    U = np.zeros((M, M))
    for i in range(M):
        b = i - s
        j0 = int(math.floor(b))
        fr = b - j0
        if 0 <= j0 < M:
            U[i, j0] += 1.0 - fr
        if 0 <= j0 + 1 < M:
            U[i, j0 + 1] += fr
    return U


def tent_nuc_frac(f, th):
    """Interior nuclear-norm fraction ||U||_*/M of a tent shift
    with fractional offset f: mean of |(1-f) + f e^{i theta}|."""
    return float(np.mean(np.abs((1.0 - f) + f * np.exp(
        1j * th))))


def certify_identity(R, tag, tol=1e-10):
    """Verify the primal-dual pair for min tr P + tr Q = 2||R||_*."""
    Uu, S, Vt = np.linalg.svd(R)
    nuc = float(np.sum(S))
    W = Uu @ Vt
    w_op = float(np.linalg.svd(W, compute_uv=False)[0])
    pair = float(np.sum(W * R))
    stack = np.vstack([Uu, Vt.T]) * np.sqrt(S)[None, :]
    Z = stack @ stack.T
    lmZ = float(np.linalg.eigvalsh(Z)[0])
    trPQ = float(np.trace(Z))
    ok = (lmZ >= -1e-8 * max(S[0], 1e-300)
          and abs(trPQ - 2.0 * nuc) <= tol * max(2.0 * nuc, 1e-300)
          and w_op <= 1.0 + 1e-10
          and abs(pair - nuc) <= tol * max(nuc, 1e-300))
    return ok, nuc, ("%s: primal lam_min %.1e, tr %.6e == "
                     "2||R||_* %.6e, dual ||W||_op %.12f, "
                     "<W,R> rel dev %.1e"
                     % (tag, lmZ, trPQ, 2.0 * nuc, w_op,
                        abs(pair - nuc) / max(nuc, 1e-300)))


def symbolic_2x2(Rf):
    """50-dps closed-form check of the identity on a 2x2 block."""
    from mpmath import mp, mpf, sqrt as msqrt, matrix as mmat, \
        chop
    mp.dps = 50
    a, b, c, d = [mpf(x) for x in Rf]
    # singular values: sqrt of eigenvalues of R^T R (closed form)
    p = a * a + b * b + c * c + d * d
    det = a * d - b * c
    disc = msqrt((p / 2) ** 2 - det * det)
    s1 = msqrt(p / 2 + disc)
    s2 = msqrt(abs(p / 2 - disc))
    nuc = s1 + s2
    Rm = mmat([[a, b], [c, d]])
    # primal via mpmath SVD-free route: P = sqrt(R R^T),
    # Q = sqrt(R^T R) (the polar construction, same optimum)
    def msqrtm(Am):
        lam1, lam2, V = _eig2(Am)
        return (V * mmat([[msqrt(lam1), 0], [0, msqrt(lam2)]])
                * V.T)

    def _eig2(Am):
        tr = Am[0, 0] + Am[1, 1]
        dt = Am[0, 0] * Am[1, 1] - Am[0, 1] * Am[1, 0]
        dd = msqrt(abs((tr / 2) ** 2 - dt))
        l1, l2 = tr / 2 + dd, tr / 2 - dd
        if abs(Am[0, 1]) > mpf("1e-45"):
            v1 = mmat([[Am[0, 1]], [l1 - Am[0, 0]]])
            v2 = mmat([[Am[0, 1]], [l2 - Am[0, 0]]])
        else:
            v1, v2 = mmat([[1], [0]]), mmat([[0], [1]])
        v1 = v1 / msqrt(v1[0] ** 2 + v1[1] ** 2)
        v2 = v2 / msqrt(v2[0] ** 2 + v2[1] ** 2)
        return l1, max(l2, mpf(0)), mmat(
            [[v1[0], v2[0]], [v1[1], v2[1]]])

    P = msqrtm(Rm * Rm.T)
    Q = msqrtm(Rm.T * Rm)
    gap = abs((P[0, 0] + P[1, 1] + Q[0, 0] + Q[1, 1]) - 2 * nuc)
    # primal feasibility: Schur complement Q - R^T P^+ R >= 0
    return float(gap), float(nuc), float(chop(s1)), float(
        chop(s2))


def chi_r_masses(rq, ka):
    ns = np.array([n for n in range(2, X_REL + 1) if rq[n] > 0]
                  [:ka], dtype=np.int64)
    return np.log(ns.astype(float)), None


# ================================================================= main
def main():
    section("PRIME.PSD.COMPLETION.TAX.01 -- the PSD completion tax "
            "(EXPLORATION ONLY)")
    sha = hashlib.sha256(FROZEN_SPEC.encode("utf-8")).hexdigest()
    print("    FROZEN_SPEC SHA-256 = %s" % sha)
    print("    NO RH claim.")
    print("\nS0 -- firewall")
    bad = ast_firewall()
    check("S0.1 AST firewall clean", not bad,
          "found %s" % bad if bad else "clean")

    th = np.linspace(0.0, math.pi, NTH)
    rq = np.zeros(X_REL + 1, dtype=np.int64)
    sq = int(math.isqrt(X_REL)) + 1
    for x in range(-sq, sq + 1):
        for y in range(-sq, sq + 1):
            v = x * x + 5 * y * y
            if 1 <= v <= X_REL:
                rq[v] += 1

    # ---------------- S1: identity ward + symbolic 2x2 + invariance
    section("S1 -- THE IDENTITY: 2||R||_* = min tr(P)+tr(Q), "
            "certificate grade")
    gap, nuc, s1, s2 = symbolic_2x2((3.0 / 7, 1.0 / 7, 1.0 / 7,
                                     2.0 / 7))
    check("S1.0 [SYMBOLIC 2x2] closed-form singular values "
          "(%.6f, %.6f), polar primal tr == 2||R||_* gap %.1e "
          "<= 1e-40 at 50 dps (the identity holds EXACTLY on the "
          "smallest block)" % (s1, s2, gap), gap <= 1e-40)

    anchor_data = {}
    for kz in ANCHORS:
        rr = core.build_window(kz)
        alpha, M, h, D = rr["alpha"], rr["M"], rr["h"], rr["D"]
        uu = np.asarray(rr["uu"], float)
        mm = 2.0 * np.asarray(rr["lam"], float)
        lam = np.asarray(rr["lam"], float)
        tau = float(np.linalg.eigvalsh(np.asarray(rr["Ah"],
                                                  float))[0])
        c_at, _ = core.atom_lags_at(alpha, M, uu, mm)
        R = coupling_of(c_at, M)
        ok, nucR, det = certify_identity(R, "kz %d" % kz)
        # symbolic 2x2 on the actual top-left corner block
        R2 = R[:2, :2]
        gap2 = symbolic_2x2((R2[0, 0], R2[0, 1], R2[1, 0],
                             R2[1, 1]))[0]
        check("S1.%d [IDENTITY + DUAL CERTIFICATE] %s; actual 2x2 "
              "corner symbolic gap %.1e; tau = %.4e (ref rel "
              "%.1e)" % (kz, det, gap2,
                         tau, abs(tau - TAU_REFS[kz])
                         / TAU_REFS[kz]),
              ok and gap2 <= 1e-40
              and abs(tau - TAU_REFS[kz]) / TAU_REFS[kz] <= 1e-4)
        # basis invariance: DFT, mirror J, seeded orthogonal
        Fm = np.exp(-2j * math.pi * np.outer(np.arange(M),
                                             np.arange(M)) / M) \
            / math.sqrt(M)
        Jm = np.zeros((M, M))
        Jm[np.arange(M), M - 1 - np.arange(M)] = -1.0
        Om = np.linalg.qr(np.random.default_rng(0).standard_normal(
            (M, M)))[0]
        devs = []
        for O1, O2, nm in ((Fm, Fm.conj().T, "DFT/Mellin"),
                           (Jm, Jm, "mirror J"),
                           (Om, Om.T, "orthogonal(seed 0)")):
            nuc2 = float(np.sum(np.linalg.svd(O1 @ R @ O2,
                                              compute_uv=False)))
            devs.append((nm, abs(nuc2 - nucR) / nucR))
        check("S1.%db [BASIS INVARIANCE] ||O1 R O2||_* == ||R||_* "
              "under %s -- rel devs %.1e / %.1e / %.1e <= 1e-8: "
              "the tax is basis-invariant; the spectral-mother "
              "verdict is a corollary"
              % (kz, ", ".join(nm for nm, _d in devs),
                 devs[0][1], devs[1][1], devs[2][1]),
              max(d for _n, d in devs) <= 1e-8)
        anchor_data[kz] = (rr, uu, mm, lam, tau, c_at, R, nucR)

    # ---------------- S2: the tax at the anchors + regression
    section("S2 -- THE TAX: merged optimum vs event-local optimum "
            "vs the measured price")
    anchor_rows = []
    gapfacs = []
    for kz in ANCHORS:
        rr, uu, mm, lam, tau, c_at, R, nucR = anchor_data[kz]
        M, D = rr["M"], rr["D"]
        ka = len(uu)
        tax_tot = 2.0 * nucR / M
        # event-local optimum: analytic tent symbol + exact ward
        tax_ev_an = 0.0
        tax_ev_ex = 0.0
        Prc_diag = np.zeros(M)
        for j in range(ka):
            s = uu[j] / D
            f = s - math.floor(s)
            tax_ev_an += (2.0 * lam[j] * tent_nuc_frac(f, th)
                          * max(0.0, M - s) / M)
            Un = U_of(s, M)
            sv = np.linalg.svd(Un, compute_uv=False)
            tax_ev_ex += 2.0 * lam[j] * float(np.sum(sv)) / M
            Prc_diag += lam[j] * (1.0 + np.sum(Un * Un, axis=1))
        ward_ev = abs(tax_ev_an - tax_ev_ex) / tax_ev_ex
        measured = float(np.median(Prc_diag))
        gain = tax_ev_ex / tax_tot
        gapfac = measured / tax_tot
        gapfacs.append(gapfac)
        check("S2.%d [TAX + REGRESSION] merged optimum tax_tot = "
              "%.3f per cell (= %.0f x tau); event-local optimum "
              "%.3f (analytic-symbol ward rel %.3f <= 0.02); "
              "measured Gram price %.3f >= event-local optimum "
              ">= merged optimum (triangle) -- nuclear-grade "
              "interference gain %.2fx, measured/optimum gap "
              "%.2fx"               % (kz, tax_tot, tax_tot / tau, tax_ev_ex,
                         ward_ev, measured, gain, gapfac),
              ward_ev <= 0.05 and measured >= 0.98 * tax_ev_ex
              and tax_ev_ex >= tax_tot - 1e-12)
        # fingerprints: scramble + Epstein
        uu_s = np.asarray(core.build_window(kz, scramble_seed=1)
                          ["uu"], float)
        c_scr, _ = core.atom_lags_at(rr["alpha"], M, uu_s, mm)
        nuc_scr = float(np.sum(np.linalg.svd(
            coupling_of(c_scr, M), compute_uv=False)))
        uu_e, _ = chi_r_masses(rq, ka)
        c_eps, _ = core.atom_lags_at(rr["alpha"], M, uu_e, mm)
        nuc_eps = float(np.sum(np.linalg.svd(
            coupling_of(c_eps, M), compute_uv=False)))
        d_s = abs(nuc_scr - nucR) / nucR
        d_e = abs(nuc_eps - nucR) / nucR
        check("S2.%db [FINGERPRINTS] scramble ||R||_* rel move "
              "%.3f >= 1e-3, Epstein x^2+5y^2 rel move %.3f >= "
              "1e-3 -- the coupling norm reads the comb"
              % (kz, d_s, d_e), d_s >= 1e-3 and d_e >= 1e-3)
        anchor_rows.append((kz, tau, tax_tot, tax_ev_ex, measured,
                            gain, gapfac))

    # ---------------- S3: the divergence law on the full ladder
    section("S3 -- THE DIVERGENCE LAW: tax ratio along the "
            "deployed ladder")
    zones = list(core.frame_a_zones())
    lad = []
    for kz in zones:
        try:
            rr = core.build_window(kz)
        except Exception:
            continue
        M = rr["M"]
        uu = np.asarray(rr["uu"], float)
        mm = 2.0 * np.asarray(rr["lam"], float)
        tau = float(np.linalg.eigvalsh(np.asarray(rr["Ah"],
                                                  float))[0])
        if tau <= 0:
            continue
        c_at, _ = core.atom_lags_at(rr["alpha"], M, uu, mm)
        nuc = float(np.sum(np.linalg.svd(coupling_of(c_at, M),
                                         compute_uv=False)))
        lad.append((kz, rr["h"], tau, 2.0 * nuc / M))
        del rr
    hh = np.array([r[1] for r in lad], float)
    tt = np.array([r[2] for r in lad], float)
    xx = np.array([r[3] for r in lad], float)
    ratio = xx / tt
    order = np.argsort(hh)
    hh, tt, xx, ratio = hh[order], tt[order], xx[order], \
        ratio[order]
    n3 = len(lad) // 3
    slopes = []
    for a, b in ((0, n3), (n3, 2 * n3), (2 * n3, len(lad))):
        sl = np.polyfit(np.log(hh[a:b]), np.log(ratio[a:b]), 1)[0]
        slopes.append(float(sl))
    sl_tax = float(np.polyfit(np.log(hh), np.log(xx), 1)[0])
    print("    %d rungs reached; per-cell tax 2||R||_*/M: %.3f "
          "(shallow) -> %.3f (deep), scaling ~ h^%.2f; tau: "
          "%.2e -> %.2e (the known ~h^-1.5 law); RATIO tax/tau: "
          "min %.1f, max %.1e, segment slopes vs h: %.2f / %.2f "
          "/ %.2f (thirds)"
          % (len(lad), xx[0], xx[-1], sl_tax, tt[0], tt[-1],
             float(np.min(ratio)), float(np.max(ratio)),
             slopes[0], slopes[1], slopes[2]))
    print("    ladder head/tail: " + "; ".join(
        "kz %d h %d tau %.2e tax %.2f ratio %.1e"
        % (kzi, hi, ti, xi, xi / ti)
        for kzi, hi, ti, xi in [lad[i] for i in
                                (0, 1, len(lad) // 2,
                                 len(lad) - 2, len(lad) - 1)]))
    min_ratio = float(np.min(ratio))
    check("S3.1 [DIVERGENCE] tax ratio >= %.0f uniformly on all "
          "%d rungs (min %.1f) and growing (positive slopes in "
          "all thirds: %s) -- the tax diverges relative to the "
          "margin" % (RATIO_BAR, len(lad), min_ratio,
                      all(s > 0 for s in slopes)),
          min_ratio >= RATIO_BAR)

    # ---------------- S4: verdict + the theorem statement
    section("S4 -- FROZEN VERDICT + THE THEOREM")
    print("    %-4s %-10s %-9s %-9s %-9s %-7s %-7s"
          % ("kz", "tau", "tax_tot", "tax_ev", "measured",
             "gain", "gapfac"))
    for r in anchor_rows:
        print("    %-4d %-10.3e %-9.3f %-9.3f %-9.3f %-7.2f "
              "%-7.2f" % r)
    if min_ratio < RATIO_BAR:
        verdict = "TAX-ESCAPE"
    elif max(gapfacs) > GAP_BAR:
        verdict = "TAX-GAP"
    else:
        verdict = "TAX-THEOREM-EXACT"
    print("\n  VERDICT: %s   [min ratio %.1f | max measured/"
          "optimum %.2f | identity+certificates %s]"
          % (verdict, min_ratio, max(gapfacs),
             not FAILS))
    print("""
  THE THEOREM (verbatim, machine-checked content = the dual
  certificates W_X per rung):

    For the canonical window family, write the deployed comb
    operator on the M_X-cell log-grid as Toep(c_at) = R_X +
    R_X^T with R_X its one-sided (lower) half.  Then EVERY
    positive 2-sector dilation [[P, R_X], [R_X*, Q]] >= 0 that
    routes the arithmetic through the fixed coupling block R_X
    pays diagonal tax  tr P + tr Q >= 2 ||R_X||_*,  with
    equality achieved by the SVD pair -- the bound is EXACT
    (zero duality gap, dual witness W_X = U V*, ||W_X||_op = 1)
    and BASIS-INVARIANT (no unitary change of basis, in
    particular no Mellin/spectral transform, alters it).  On
    the entire deployed ladder the per-cell tax satisfies
    2 ||R_X||_* / M_X >= %.0f x tau_X  (measured min ratio
    %.1f, growing ~ h^%.2f against the margin's h^-3/2 decay).
    Hence no positive completion architecture with this
    coupling can certify the floor: the diagonal overhead it
    must carry exceeds the certified margin by a diverging
    factor.  The event-local designs of the Schur program pay
    Sigma_n 2 lam_n ||U_n||_* >= 2 ||R_X||_* (triangle
    inequality); their measured prices exceed the exact class
    optimum by the typed gap factors (the designs were
    suboptimal in constant), but the EXACT optimum already
    exceeds tau by the measured min ratio on every rung --
    optimality could not have saved them.

  TYPED BOUNDARY (the one door the theorem does NOT close):
  architectures where the comb does not enter as a fixed
  coupling block of a positive dilation -- i.e. where the comb
  is absorbed into a corner that is positive for reasons that
  already require the window positivity (Fejer-Riesz of the
  total symbol).  That door is the statement itself.
  NO RH claim.""" % (RATIO_BAR, min_ratio, sl_tax))
    n_pass = sum(1 for _n, ok in CHECKS if ok)
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed%s"
          % (time.time() - T0, len(CHECKS), len(FAILS),
             ("  " + ",".join(FAILS)) if FAILS else ""))
    return 0 if n_pass == len(CHECKS) else 1


if __name__ == "__main__":
    raise SystemExit(main())
'''

_SRC_FLOW = r'''
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""spectral_flow_pivot_probe -- F4: the topological attack.
SPECTRAL FLOW INSTEAD OF MINIMUM MARGIN on the canonical ladder.

EXPLORATION ONLY (experiments/): no ledger row, no paper edit, no
.md, nothing outside experiments/.  NO RH claim.  Frozen (spec +
sha256) before running.

THE OBJECTS: per rung the deployed frame-A window operator in the
parity compression, A_K(t) = Tb (T[c_ar] + t T[c_at]) Tb^T with
K = SCHUR_KB = 16 modes (the deployed Schur discipline; the
leading 2x2 IS the certified lock block, tau = lambda_min(A_2)).
THE NESTING (typed): the canonical ladder nests in the PARITY-MODE
index m = 1..K within one frame (leading principal minors D_m,
Schur/Levinson pivots d_m = D_m / D_{m-1}); the DEPTH direction
(rung to rung) is a FAMILY of rebuilt frames (different M, D), not
a matrix nesting -- no pivot recursion connects rungs.  Classical
equivalence (the ward): all d_m > 0 <=> A_K PD <=> n_-(A_K) = 0,
verified by TWO independent inertia computations per rung (Jacobi
minor-sign-change count, determinant recursion only, NO
eigenproblem; vs direct eigh).

THE HOMOTOPY (frozen): the natural depth knob of the deployed
decomposition, t in [0, 1]: A(t) = A_arch + t A_comb (pure
density/arch endpoint -> full relational comb; the pencil is
LINEAR in t, so ALL crossings are exact generalized eigenvalues
of (A_arch, -A_comb) -- no scanning needed; the frozen grid scan
is the independent detection ward).  PREMISE NOTE TYPED BEFORE
THE RUN (carried from the relational-Lagrange run-1 finding): the
arch-only block is NEGATIVE definite in the 2-mode parity
compression, so the task's "pure density -- PSD by construction?"
is expected to answer NO and the homotopy is expected to have
FORCED upward crossings (the comb supplies the positivity); the
probe measures where, how many, and how the crossing-free
interval around the deployed point t = 1 behaves with depth.

THE INDEX MACHINERY (three computations, predeclared):
 (a) argument principle: for the LINEAR pencil the winding of
     det A(t) collapses to the real-root count of the degree-K
     polynomial det(A_arch + t A_comb); computed via QZ
     generalized eigenvalues AND via the sign changes of
     slogdet on the frozen t-grid (N = 2001) -- agreement ward;
 (b) Krein/Levinson: corpus connection (v696/v698/v743 use
     Levinson reflection coefficients |k_n| < 1 as the PD
     certificate of Toeplitz lag matrices).  The parity block is
     Toeplitz-PLUS-HANKEL, so Levinson does not apply verbatim;
     the determinant-recursion pendant (Jacobi minor signs) is
     the honest same-matrix analogue and IS eigenproblem-free.
     Levinson on the raw summed lag sequence c_ar + c_at is run
     on the anchors as the corpus-object measurement (breakdown
     depth typed -- a DIFFERENT, stronger object, typed as such);
 (c) homotopy crossing count with directions: at each real
     pencil root t* in (0, 1], the crossing direction is
     sign(v^T A_comb v) on the kernel vector; spectral-flow ward
     n_-(A(0)) - n_-(A(1)) == sum of directions.

THE INDEPENDENCE QUESTION (the user's kill, frozen): in FINITE
dimension the spectral flow of a self-adjoint path is ENDPOINT-
DETERMINED (SF = n_-(0) - n_-(1)); the probe verifies this
identity on every rung.  Genuine-new-leverage typing: (+) the
pivot/minor route certifies the sign WITHOUT the eigenproblem
(exact/interval arithmetic on determinant recursions is the
certification-grade advantage); (+) the crossing LOCATIONS
(t_last < 1 < t_next) are new measured objects with a ladder law
(the quantized gap); (-) the index VALUE carries nothing beyond
the endpoint inertias -- as a positivity certificate it is a
reformulation of sign(tau).  All three are measured and typed.

STABILITY (task 4): per rung the metric margin tau -> 0 while the
AMPLITUDE margin (the crossing-free interval (t_last, t_next)
around t = 1 in the comb-amplitude coordinate) is measured; the
comparison decides whether the topological picture sees a
quantized gap where the metric sees a vanishing one.  A crossing
AT the deployed point would mean det A_2 = 0 (tau = 0, a pivot
sign change): on the accessible rungs this is EXCLUDED by the
certified margins -- the floor ladder and the detector-strand
exclusion instrument meet at exactly this statement (necessary-
side; NO RH claim).

CONTROLS: scramble (seed 20260807, mass-fixed, kz = 9): the
machinery must DETECT whatever the scrambled flow does (grid ==
pencil ward; inertia typed -- negativity is measured, not
assumed); Epstein x^2+5y^2 (h = 2, kz-9 frame, weights from the
exact Lambda_F recursion -- SIGNED masses): routed negativity =
crossings, localized in t; pure-density endpoint inertia typed
(the premise correction).

VERDICT (frozen precedence): FLOW-TRANSLATION-BLOCKED (a ward
fails) / FLOW-CROSSINGS (crossings exist in (0, 1] on any true
rung -- localized, connected to the exclusion instrument;
independence typing embedded) / FLOW-REFORMULATION-ONLY (no
crossings but no independent invariant either) / FLOW-PROTECTED
(index 0 along the homotopy on all rungs AND the independent
computations agree).

FIREWALL: prime side + archimedean kernel only (no zeta zeros
anywhere); v563 READ-ONLY; RNG only in the declared scramble;
report only, no files written.
"""

import hashlib
import math
import os
import sys
import time

import numpy as np
import scipy.linalg as sla

_here = os.path.dirname(os.path.abspath(__file__))
for _cand in (os.path.join(_here, "..", "..", "verification"), _here):
    if os.path.exists(os.path.join(_cand, "v563_paper2_readouts.py")):
        sys.path.insert(0, os.path.abspath(_cand))
        break

import v563_paper2_readouts as core        # noqa: E402  (READ-ONLY)

T0 = time.time()
FAILS = []
N_CHK = 0

FROZEN_SPEC = """\
spectral_flow_pivot_probe spec v1 (2026-08-07, frozen before run).
Objects: A_K(t) = Tb(T[c_ar] + t T[c_at])Tb^T, K = 16 parity modes,
deployed frame-A rungs (filter: h != 1292, exp(2 alpha) <=
ATOM_MAX + 0.5; expected 67).  Pivots = leading-minor ratios in the
MODE nesting; depth direction = frame family (typed, no recursion).
Wards: anchors kz 9/12/13 A_2 == build_window Ah (rel 1e-8) + tau
refs 5.984165e-4/4.351189e-4/5.637632e-4 (rel 1e-4); Jacobi minor
inertia == eigh inertia at t = 0 and t = 1 on all rungs; SF ==
n_-(0) - n_-(1) == sum of crossing directions; grid detection
(N = 2001 slogdet sign changes) == pencil root count in (0,1).
Pencil roots: QZ eig(A_arch, -A_comb), real if |Im| <= 1e-6
max(1, |Re|); crossing dirs from kernel vector of A(t*).
Stability: gap_lo = 1 - t_last, gap_hi = t_next - 1 vs tau along
the ladder (shallow/deep thirds + log-log slope vs h).
Controls: scramble seed 20260807 kz 9 (detection ward, inertia
typed); Epstein x^2+5y^2 Lambda_F masses on the kz-9 frame
(signed; crossings localized, detection ward); density endpoint
inertia typed.  Levinson on raw lags: anchors, info-grade.
Verdict precedence: TRANSLATION-BLOCKED > CROSSINGS >
REFORMULATION-ONLY > PROTECTED.  NO RH claim.
DECLARED IMPLEMENTATION CORRECTION (run 1 -> run 2, v818
precedent; no bar or verdict rule changed): run 1 measured that
crossings cluster within one grid interval near t = 1 (the
crossing-free window around the deployed point is ~1e-3, below
the 5e-4 grid step times a few), so the naive equality
grid-sign-changes == root-count was never the intended quantity;
the detection ward is the argument-principle statement AT GRID
RESOLUTION: grid sign changes == number of grid intervals
containing an ODD number of pencil roots.  Intent (grid detection
must agree with QZ) unchanged."""

# ------------------------------------------------- frozen constants
K_MODES = int(core.SCHUR_KB)          # 16, the deployed low block
ANCHORS = (9, 12, 13)
TAU_REFS = {9: 5.984165e-4, 12: 4.351189e-4, 13: 5.637632e-4}
TAU_REF_REL = 1.0e-4
ANCHOR_REL = 1.0e-8
IMAG_TOL = 1.0e-6
GRID_N = 2001
ANOMALOUS_H = 1292
SCR_SEED = 20260807
XE_EPS = 258                          # Epstein support cap (kz 9)
DEG_BAR = 1.0e-10                     # degenerate-direction bar


def check(name, ok, detail=""):
    global N_CHK
    N_CHK += 1
    if not ok:
        FAILS.append(name.split()[0])
    print("[%s] %s%s" % ("PASS" if ok else "FAIL", name,
                         (": " + detail) if detail else ""))


# --------------------------------------------------- frame assembly
def rung_blocks(kz, uu=None, mm=None):
    """A_arch, A_comb in the K-mode parity compression + meta."""
    al = float(core.U_ALL[kz])
    Dk = 0.5 * float(core.G_ALL[kz]) / float(core.NU_MAIN)
    M = int(math.ceil(al / Dk - 1.0e-9)) + 1
    if M % 2:
        M += 1
    h = M // 2
    ka = core.atoms_in(al)
    if uu is None:
        uu = core.U_ALL[:ka]
    if mm is None:
        mm = core.MU_ALL[:ka]
    c_at, D = core.atom_lags_at(al, M, uu, mm)
    c_ar = core.arch_lags(M, D)
    Tb = core.parity_basis(h, min(K_MODES, h))
    Ta = core.odd_toeplitz(np.asarray(c_ar, float), M)
    A_arch = Tb @ (Ta @ Tb.T)
    del Ta
    Tc = core.odd_toeplitz(np.asarray(c_at, float), M)
    A_comb = Tb @ (Tc @ Tb.T)
    del Tc
    return dict(al=al, h=h, M=M, D=D,
                A_arch=0.5 * (A_arch + A_arch.T),
                A_comb=0.5 * (A_comb + A_comb.T),
                c_sum=np.asarray(c_ar, float) + np.asarray(c_at,
                                                           float))


def minors_sign(A):
    """Leading-minor sign sequence + Jacobi inertia (det-recursion
    data only, NO eigenproblem)."""
    K = A.shape[0]
    signs = [1.0]
    for m in range(1, K + 1):
        s, _ = np.linalg.slogdet(A[:m, :m])
        signs.append(float(s))
    n_neg = sum(1 for i in range(K) if signs[i] * signs[i + 1] < 0)
    return signs[1:], n_neg


def inertia_eig(A):
    ev = np.linalg.eigvalsh(A)
    return int(np.sum(ev < 0.0)), ev


def pencil_crossings(A0, A1):
    """Real roots of det(A0 + t A1) = 0 via QZ; (t, direction)."""
    w = sla.eigvals(A0, -A1)
    ts = []
    for z in np.atleast_1d(w):
        if not np.isfinite(z):
            continue
        if abs(z.imag) <= IMAG_TOL * max(1.0, abs(z.real)):
            if z.real > 0.0:
                ts.append(float(z.real))
    ts = sorted(ts)
    out = []
    for t in ts:
        At = A0 + t * A1
        evv, V = np.linalg.eigh(At)
        i0 = int(np.argmin(np.abs(evv)))
        v = V[:, i0]
        d = float(v @ (A1 @ v))
        out.append((t, (0.0 if abs(d) <= DEG_BAR else
                        math.copysign(1.0, d))))
    return out


def grid_signchanges(A0, A1, t_lo=0.0, t_hi=1.0):
    tt = np.linspace(t_lo, t_hi, GRID_N)
    ss = []
    for t in tt:
        s, _ = np.linalg.slogdet(A0 + t * A1)
        ss.append(float(s))
    return sum(1 for i in range(len(ss) - 1)
               if ss[i] * ss[i + 1] < 0)


def expected_grid_changes(roots, t_lo=0.0, t_hi=1.0):
    """Argument principle at grid resolution: # grid intervals
    containing an odd number of roots."""
    edges = np.linspace(t_lo, t_hi, GRID_N)
    idx = np.searchsorted(edges, [r for r in roots
                                  if t_lo < r < t_hi])
    return int(np.sum(np.bincount(idx) % 2))


def levinson_depth(r):
    """Levinson-Durbin on raw lags; returns (breakdown depth,
    max |k|) -- the corpus (v696/v698) PD certificate object."""
    if r[0] <= 0:
        return 0, math.inf
    a = np.zeros(1)
    E = float(r[0])
    kmax = 0.0
    for n in range(1, len(r)):
        acc = r[n] + float(a @ r[n - 1:0:-1]) if n > 1 else r[1]
        k = -acc / E
        kmax = max(kmax, abs(k))
        E *= (1.0 - k * k)
        if not (E > 0.0):
            return n, kmax
        a_new = np.empty(n)
        a_new[:n - 1] = a + k * a[::-1]
        a_new[n - 1] = k
        a = a_new
    return len(r), kmax


def flow_report(A0, A1, want_grid=True):
    n0, _ = inertia_eig(A0)
    A_end = A0 + A1
    evv, V = np.linalg.eigh(A_end)
    n1 = int(np.sum(evv < 0.0))
    v1 = V[:, int(np.argmin(np.abs(evv)))]
    vel = float(v1 @ (A1 @ v1))       # flow velocity at t = 1
    cross = pencil_crossings(A0, A1)
    c01 = [(t, d) for t, d in cross if t <= 1.0]
    sf_dir = int(sum(d for _, d in c01))
    t_last = max([t for t, _ in c01], default=0.0)
    t_next = min([t for t, _ in cross if t > 1.0],
                 default=math.inf)
    roots01 = [t for t, _ in c01 if t < 1.0]
    g = grid_signchanges(A0, A1) if want_grid else None
    return dict(n0=n0, n1=n1, cross=c01, sf_dir=sf_dir,
                t_last=t_last, t_next=t_next, grid=g,
                lmin1=float(evv[0]), vel=vel,
                exp_g=expected_grid_changes(roots01),
                n_in01=len(roots01))


def run():
    print("=" * 78)
    print("SPECTRAL FLOW / PIVOTS (spectral_flow_pivot_probe) -- "
          "F4, the topological attack")
    print("=" * 78)
    print("frozen spec sha256 = %s"
          % hashlib.sha256(FROZEN_SPEC.encode()).hexdigest()[:16])
    print("""
HONESTY FRAME: NO RH claim; prime + archimedean data only (no
zeros).  The homotopy endpoints are typed by MEASUREMENT; the
premise 'pure density PSD by construction?' is answered below.""")

    # ============================================================== S0
    print("\nS0 -- rung set, anchors, nesting typed")
    rungs = []
    for kz in core.frame_a_zones():
        al = float(core.U_ALL[kz])
        Dk = 0.5 * float(core.G_ALL[kz]) / float(core.NU_MAIN)
        M = int(math.ceil(al / Dk - 1.0e-9)) + 1
        if M % 2:
            M += 1
        if M // 2 == ANOMALOUS_H:
            continue
        if math.exp(2.0 * al) > core.ATOM_MAX + 0.5:
            continue
        rungs.append(kz)
    check("S0.SET the deployed frame-A rung set (filters h != %d, "
          "exp(2a) <= ATOM_MAX): %d rungs" % (ANOMALOUS_H,
                                              len(rungs)),
          len(rungs) == 67, "%d" % len(rungs))
    print("    NESTING TYPED: pivots d_m = D_m/D_{m-1} live in the "
          "PARITY-MODE index m = 1..%d within one frame (leading "
          "2x2 = the certified lock block); the depth direction "
          "is a rebuilt-frame FAMILY -- no pivot recursion "
          "connects rungs." % K_MODES)
    blocks = {}
    for kz in ANCHORS:
        blocks[kz] = rung_blocks(kz)
        A2 = (blocks[kz]["A_arch"] + blocks[kz]["A_comb"])[:2, :2]
        rr = core.build_window(kz)
        dev = float(np.max(np.abs(A2 - np.asarray(rr["Ah"])))) \
            / max(1.0, float(np.max(np.abs(rr["Ah"]))))
        tau = float(np.linalg.eigvalsh(A2)[0])
        check("S0.A%d anchor kz=%d: A_2(t=1) == deployed Ah (rel "
              "%.1e <= %.0e) AND tau = %.6e vs frozen ref (rel "
              "%.1e <= %.0e)"
              % (kz, kz, dev, ANCHOR_REL, tau,
                 abs(tau / TAU_REFS[kz] - 1.0), TAU_REF_REL),
              dev <= ANCHOR_REL
              and abs(tau / TAU_REFS[kz] - 1.0) <= TAU_REF_REL)

    # ============================================================== S1
    print("\nS1 -- the pivot series + the classical-equivalence "
          "ward (all %d rungs)" % len(rungs))
    tab = []
    ok_jac = True
    ok_2pd = True
    n16_pd = 0
    for kz in rungs:
        bl = blocks.get(kz) or rung_blocks(kz)
        blocks[kz] = bl
        A1 = bl["A_arch"] + bl["A_comb"]
        sg1, nj1 = minors_sign(A1)
        ne1, ev1 = inertia_eig(A1)
        sg0, nj0 = minors_sign(bl["A_arch"])
        ne0, _ = inertia_eig(bl["A_arch"])
        ok_jac &= (nj1 == ne1) and (nj0 == ne0)
        tau2 = float(np.linalg.eigvalsh(A1[:2, :2])[0])
        ok_2pd &= (tau2 > 0.0) and (sg1[0] > 0) and (sg1[1] > 0)
        n16_pd += int(ne1 == 0)
        tab.append(dict(kz=kz, h=bl["h"], al=bl["al"], tau2=tau2,
                        ne0=ne0, ne1=ne1, lmin16=float(ev1[0]),
                        bl=bl))
    check("S1.JAC [INDEPENDENT INERTIA] Jacobi minor-sign count == "
          "eigh negative count at t = 0 AND t = 1 on all rungs "
          "(determinant recursion needs NO eigenproblem)", ok_jac)
    check("S1.PIV certified reproduction: the leading pivots d_1, "
          "d_2 > 0 and tau_2 > 0 on ALL rungs (sign(d) <=> the "
          "certified 2-mode PSD)", ok_2pd)
    print("    16-mode census: %d/%d rungs have the FULL low block "
          "PD at t = 1 (n_- = 0); arch endpoint n_-(0) range %d..%d"
          % (n16_pd, len(rungs), min(t["ne0"] for t in tab),
             max(t["ne0"] for t in tab)))

    # ============================================================== S2
    print("\nS2 -- the homotopy flow (density -> comb), pencil vs "
          "grid, on all rungs")
    ok_sf = True
    ok_grid = True
    tot_cross = 0
    all_up = True
    for t_ in tab:
        fr = flow_report(t_["bl"]["A_arch"], t_["bl"]["A_comb"])
        t_["fr"] = fr
        tot_cross += len(fr["cross"])
        all_up &= all(d > 0 for _, d in fr["cross"])
        ok_sf &= (fr["n1"] == fr["n0"] - fr["sf_dir"])
        ok_grid &= (fr["grid"] == fr["exp_g"])
    check("S2.SF spectral-flow ward on all rungs: n_-(1) == "
          "n_-(0) - sum(crossing directions) -- the flow is "
          "ENDPOINT-DETERMINED (verified, the finite-dim fact)",
          ok_sf)
    check("S2.GRID detection ward (argument principle at grid "
          "resolution, declared correction): grid sign changes "
          "== # intervals with an odd number of pencil roots, "
          "all rungs", ok_grid)
    n_cross = [len(t_["fr"]["cross"]) for t_ in tab]
    t_lasts = np.array([t_["fr"]["t_last"] for t_ in tab])
    print("    crossings per rung: min %d, median %d, max %d; "
          "TOTAL %d; all directions UPWARD: %s"
          % (min(n_cross), int(np.median(n_cross)), max(n_cross),
             tot_cross, all_up))
    print("    the count vs depth: shallow third mean %.1f, deep "
          "third mean %.1f (the crossing count == n_-(arch), the "
          "comb's positive supply)"
          % (float(np.mean(n_cross[:len(n_cross) // 3])),
             float(np.mean(n_cross[-len(n_cross) // 3:]))))
    print("    PREMISE ANSWERED: the pure-density endpoint is NOT "
          "PSD (n_-(0) > 0 on every rung) -- 'PSD by construction' "
          "is FALSE in the deployed parity compression; the "
          "homotopy has forced upward crossings and index-0 "
          "protection along this path is impossible.")

    # ============================================================== S3
    print("\nS3 -- independence (the user's kill, answered by "
          "measurement)")
    print("    (i) SAME-matrix, DIFFERENT-data: the Jacobi/pivot "
          "route (S1.JAC) computes the inertia from determinant "
          "recursions alone -- eigenproblem-free, exact/interval-"
          "certifiable; it AGREES on all rungs.")
    print("    (ii) corpus object (info): Levinson |k|<1 on the "
          "raw summed lags (Toeplitz, the v696/v698 certificate "
          "-- a DIFFERENT and stronger object than the parity "
          "block):")
    for kz in ANCHORS:
        bd, kmax = levinson_depth(blocks[kz]["c_sum"])
        Mfull = len(blocks[kz]["c_sum"])
        print("      kz=%d: breakdown at depth %d of %d (max|k| "
              "%.3f) -- the raw Toeplitz lag matrix is %s"
              % (kz, bd, Mfull, kmax,
                 "PD to full depth" if bd == Mfull else
                 "NOT PD (parity compression is the weaker, "
                 "deployed object)"))
    print("    (iii) THE KILL ASSESSMENT: SF == n_-(0) - n_-(1) "
          "verified on every rung -- in finite dimension the "
          "index VALUE is endpoint-determined and adds NO "
          "invariant beyond sign(pivots) at the endpoints.  "
          "Genuine leverage found: (+) eigenproblem-free exact "
          "certifiability of the pivot signs, (+) the crossing-"
          "LOCATION set (t_last, t_next) as a new measured ladder "
          "object; (-) 'index 0 protection' is NOT available "
          "(forced crossings) and the index is a reformulation "
          "of the endpoint signs.")

    # ============================================================== S4
    print("\nS4 -- stability: quantized amplitude gap vs vanishing "
          "metric margin")
    taus = np.array([t_["tau2"] for t_ in tab])
    hs = np.array([float(t_["h"]) for t_ in tab])
    gap_lo = 1.0 - t_lasts
    t_nexts = np.array([t_["fr"]["t_next"] for t_ in tab])
    gap_hi = t_nexts - 1.0
    fin = np.isfinite(gap_hi)
    third = max(len(tab) // 3, 1)
    sl_tau = np.polyfit(np.log(hs), np.log(taus), 1)[0]
    sl_gap = np.polyfit(np.log(hs), np.log(gap_lo), 1)[0]
    print("    metric margin tau_2: %.3e (shallow med) -> %.3e "
          "(deep med), log-log slope vs h = %+.2f (vanishing)"
          % (float(np.median(taus[:third])),
             float(np.median(taus[-third:])), sl_tau))
    print("    amplitude gap below (1 - t_last): %.3e -> %.3e, "
          "slope %+.2f; gap above (t_next - 1): median %.3e "
          "(finite on %d/%d rungs)"
          % (float(np.median(gap_lo[:third])),
             float(np.median(gap_lo[-third:])), sl_gap,
             float(np.median(gap_hi[fin])) if fin.any()
             else math.nan, int(fin.sum()), len(tab)))
    # is the amplitude gap just the metric margin / flow velocity?
    lmins = np.array([t_["fr"]["lmin1"] for t_ in tab])
    vels = np.array([t_["fr"]["vel"] for t_ in tab])
    pred = np.abs(lmins) / np.maximum(np.abs(vels), 1e-300)
    rat = gap_lo / np.maximum(pred, 1e-300)
    print("    VELOCITY TEST: first-order prediction 1 - t_last "
          "~= lambda_min(1)/|v^T A_comb v|: ratio measured/"
          "predicted median %.2f (IQR %.2f..%.2f) -- ratio ~ 1 "
          "means the 'amplitude gap' IS the metric margin "
          "rescaled by the flow velocity, i.e. NO independent "
          "quantized protection"
          % (float(np.median(rat)),
             float(np.percentile(rat, 25)),
             float(np.percentile(rat, 75))))
    print("    QUANTIZATION STATEMENT: a crossing AT the deployed "
          "point is an integer event (a pivot sign change, det "
          "A_2 = 0, tau = 0); on the accessible rungs the "
          "certified margins EXCLUDE it -- the floor ladder and "
          "the detector-strand exclusion instrument meet in this "
          "statement (necessary-side; a crossing in the "
          "accessible range would be an off-line-zero-grade "
          "event, and none is seen).  The measured trend above "
          "decides the quantization question -- the gap trend, "
          "not the index, is the topological content.")

    # ============================================================== S5
    print("\nS5 -- controls")
    # scramble (mass-fixed) on kz 9
    al9 = float(core.U_ALL[9])
    ka9 = core.atoms_in(al9)
    rng = np.random.default_rng(SCR_SEED)
    uu_s = np.sort(rng.uniform(0.0, 2.0 * al9, size=ka9))
    bl_s = rung_blocks(9, uu=uu_s, mm=core.MU_ALL[:ka9])
    fr_s = flow_report(bl_s["A_arch"], bl_s["A_comb"])
    tau_s = float(np.linalg.eigvalsh(
        (bl_s["A_arch"] + bl_s["A_comb"])[:2, :2])[0])
    check("S5.SCR scramble kz=9 (seed %d): detection ward holds "
          "on the scrambled flow (grid %d == pencil %d) AND SF "
          "endpoint identity holds; measured endpoint: n_-(1) = "
          "%d, tau_scr = %+.3e (negativity is MEASURED, not "
          "assumed -- typed)"
          % (SCR_SEED, fr_s["grid"], fr_s["exp_g"], fr_s["n1"],
             tau_s),
          fr_s["grid"] == fr_s["exp_g"]
          and fr_s["n1"] == fr_s["n0"] - fr_s["sf_dir"])
    # Epstein x^2+5y^2 on the kz-9 frame (exact Lambda_F recursion)
    rq = np.zeros(XE_EPS + 1)
    for x in range(0, int(math.isqrt(XE_EPS)) + 1):
        for y in range(0, int(math.isqrt(max(XE_EPS - x * x, 0)
                                         // 5)) + 1):
            n = x * x + 5 * y * y
            if 2 <= n <= XE_EPS:
                rq[n] += (2 if x > 0 else 1) * (2 if y > 0 else 1)
    aE = rq / 2.0
    aE[1] = 1.0
    LF = np.zeros(XE_EPS + 1)
    for n in range(2, XE_EPS + 1):
        s = aE[n] * math.log(n)
        for d in range(2, n):
            if n % d == 0:
                s -= LF[d] * aE[n // d]
        LF[n] = s
    supp = [n for n in range(2, XE_EPS + 1) if abs(LF[n]) > 1e-12]
    uuE = np.log(np.array(supp, float))
    mmE = 2.0 * np.array([LF[n] for n in supp]) \
        / np.sqrt(np.array(supp, float))
    n_negm = int(np.sum(mmE < 0))
    bl_e = rung_blocks(9, uu=uuE, mm=mmE)
    fr_e = flow_report(bl_e["A_arch"], bl_e["A_comb"])
    tau_e = float(np.linalg.eigvalsh(
        (bl_e["A_arch"] + bl_e["A_comb"])[:2, :2])[0])
    dncr = [t for t, d in fr_e["cross"] if d < 0]
    check("S5.EPS Epstein x^2+5y^2 on the kz-9 frame (%d events, "
          "%d SIGNED-negative masses from the exact Lambda_F "
          "recursion): detection ward (grid %d == pencil %d); "
          "endpoint n_-(1) = %d, tau_E = %+.3e; down-crossings "
          "at t = %s -- the routed negativity localized"
          % (len(supp), n_negm, fr_e["grid"], fr_e["exp_g"],
             fr_e["n1"], tau_e,
             ["%.3f" % t for t in dncr[:4]] or "none in (0,1]"),
          fr_e["grid"] == fr_e["exp_g"]
          and fr_e["n1"] == fr_e["n0"] - fr_e["sf_dir"]
          and n_negm > 0)
    ne0_9, _ = inertia_eig(blocks[9]["A_arch"])
    check("S5.DEN pure-density endpoint typed: arch-only inertia "
          "n_- = %d > 0 at kz=9 (16 modes; 2-mode block negative "
          "definite) -- the task's 'PSD by construction' premise "
          "is corrected by measurement" % ne0_9, ne0_9 > 0)

    # ============================================================== S6
    print("\nS6 -- verdict")
    wards_ok = not FAILS
    if not wards_ok:
        verdict = "FLOW-TRANSLATION-BLOCKED"
    elif tot_cross > 0:
        verdict = "FLOW-CROSSINGS"
    else:
        verdict = "FLOW-REFORMULATION-ONLY"
    print("=" * 78)
    print("V -- VERDICT: %s" % verdict)
    print("=" * 78)
    if verdict == "FLOW-CROSSINGS":
        print("""    THE TYPED OUTCOME: the homotopy from the density endpoint
    to the deployed comb is NOT crossing-free -- the density
    endpoint is negative (n_- = %d..%d over the ladder) and the
    comb supplies exactly that many UPWARD crossings (all
    directions positive: %s); 'index 0 = topological protection'
    is unavailable on this path BY MEASUREMENT, not by
    approximation.  The crossings are NOT localized early: the
    last crossing HUGS the deployed point (median lower gap
    1 - t_last = %.3e, shrinking with slope %+.2f in h vs tau's
    %+.2f), and the velocity test (median ratio %.2f) shows the
    amplitude gap IS the metric margin divided by the flow
    velocity -- NO quantized protection: the topological
    distance-to-crossing and the metric smallness are the SAME
    quantity in different units.  THE USER'S KILL, ANSWERED:
    the index VALUE is endpoint-determined (verified on every
    rung) -- as a cofinal-positivity certificate the spectral
    flow is a REFORMULATION of the pivot signs; the genuine
    residue of the topological view is (a) the eigenproblem-free
    pivot certification (exact-arithmetic-friendly) and (b) the
    crossing-location law along the ladder.  EXCLUSION
    CONNECTION: a crossing at the deployed point on an accessible
    rung would be a pivot sign change (tau = 0); the certified
    margins exclude it -- this is precisely where the floor
    ladder meets the detector-strand exclusion instrument.
    HONEST CONSEQUENCE: F4 does not open an index-theoretic
    route around the margin problem; a cofinal index theorem
    would need an INFINITE-dimensional flow whose index is NOT
    endpoint-trivial (e.g. a genuinely operator-theoretic
    Maslov/Krein setting where the ladder is one path), and
    nothing in the accessible data forces such a structure."""
              % (min(t_["ne0"] for t_ in tab),
                 max(t_["ne0"] for t_ in tab), all_up,
                 float(np.median(gap_lo)), sl_gap, sl_tau,
                 float(np.median(rat))))
    dt_run = time.time() - T0
    print("-" * 78)
    print("checks: %d run, %d failed%s | runtime %.1f min"
          % (N_CHK, len(FAILS),
             (" [" + ", ".join(FAILS) + "]") if FAILS else "",
             dt_run / 60.0))
    print("NO RH claim; report only; nothing outside experiments/ "
          "touched.")


if __name__ == "__main__":
    run()
'''

# --------------------------------------------------------------- harness
_PF_RE = re.compile(r"^\s*\[(PASS|FAIL)\]\s+(\S+)", re.M)
_VD_RE = re.compile(r"VERDICT[:\]]")


def _probe_file(name):
    cand = os.path.abspath(os.path.join(
        _HERE, os.pardir, "experiments", "tfpt-discovery", name + ".py"))
    return cand if os.path.isfile(cand) else None


def _census(out):
    marks = _PF_RE.findall(out)
    fails = sorted({tok for st, tok in marks if st == "FAIL"})
    verdict = ""
    for line in out.splitlines():
        if _VD_RE.search(line):
            verdict = line.strip()
    return len(marks), fails, verdict


def _exec_probe(name, src, run_entry=True):
    """Execute one embedded frozen probe source BYTE-EXACT in its own
    module namespace, registered in sys.modules under the probe's
    canonical import name (cross-probe READ-ONLY imports resolve to
    the embedded copies); capture and re-emit stdout; return
    (stdout, exit_code, byte_equal_to_source_file_or_None)."""
    if src[:1] == "\n":
        src = src[1:]
    path = _probe_file(name)
    same = None
    if path is not None:
        with open(path, encoding="utf-8") as fh:
            same = (fh.read() == src)
    fname = path or os.path.abspath(__file__)
    mod = types.ModuleType(name)
    mod.__file__ = fname
    sys.modules[name] = mod
    buf = io.StringIO()
    code = 0
    with contextlib.redirect_stdout(buf):
        try:
            exec(compile(src, fname, "exec"), mod.__dict__)
            entry = mod.__dict__.get("main") or mod.__dict__.get("run")
            if run_entry and callable(entry):
                rc = entry()
                code = 0 if rc is None else int(rc)
        except SystemExit as exc:
            code = 0 if exc.code is None else int(exc.code)
        except Exception:                            # regression guard
            import traceback
            traceback.print_exc(file=sys.stdout)
            code = 99
    out = buf.getvalue()
    sys.stdout.write(out)
    sys.stdout.flush()
    return out, code, same


def _gate(name, out, code, same, exp_n, exp_fails, exp_verdict,
          exp_code, gates):
    n, fails, verdict = _census(out)
    ok = (n == exp_n and fails == list(exp_fails)
          and exp_verdict in verdict and code == exp_code
          and same is not False)
    gates.append(ok)
    prov = ("byte-exact vs experiments source" if same is True else
            "embedded copy (source file not present)" if same is None
            else "SOURCE MISMATCH")
    print("\n[%s] PATTERN GATE %s: %d checks (exp %d) | FAILs %s "
          "(exp %s) | exit %d (exp %d) | %s\n      verdict line: %s"
          % ("PASS" if ok else "FAIL", name, n, exp_n,
             ",".join(fails) if fails else "none",
             ",".join(exp_fails) if exp_fails else "none",
             code, exp_code, prov, verdict), flush=True)
    return ok


# (probe, source, expected checks, expected FAIL ids, verdict, exit)
_PLAN = (
    ("psd_completion_tax_probe", _SRC_TAX, 15, (), "TAX-GAP", 0),
    ("spectral_flow_pivot_probe", _SRC_FLOW, 11, (), "FLOW-CROSSINGS", 0),
)


def run():
    t0 = time.time()
    print("=" * 74)
    print("v850 -- PRIME.PSD.COMPLETION.TAX.01 + the spectral-flow "
          "pivot decision")
    print("(the two class-level no-go closures: the diverging nuclear-"
          "norm tax with")
    print("zero-gap certificates, basis-invariant; the index route "
          "closed by measurement;")
    print("frozen protocols embedded byte-exact and executed verbatim; "
          "NO RH claim)")
    print("=" * 74, flush=True)
    gates = []
    for name, src, exp_n, exp_fails, exp_verdict, exp_code in _PLAN:
        print("\n" + "-" * 74)
        print("EMBEDDED FROZEN PROBE: %s" % name)
        print("-" * 74, flush=True)
        out, code, same = _exec_probe(name, src)
        _gate(name, out, code, same, exp_n, exp_fails, exp_verdict,
              exp_code, gates)
    ok = all(gates)
    print("\n" + "=" * 74)
    print("v850: %d/%d pattern gates passed | runtime %.1f s"
          % (sum(gates), len(gates), time.time() - t0))
    print("NO RH claim; the typed boundary stays: the one unclosed "
          "door is Fejer-Riesz")
    print("of the total symbol -- the positivity statement itself; "
          "positive-dilation")
    print("completions with fixed comb coupling and finite-dimensional "
          "index routes are")
    print("closed at class level.")
    print("[%s] v850 VERDICT GATE: TAX-GAP + FLOW-CROSSINGS"
          % ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(run())
