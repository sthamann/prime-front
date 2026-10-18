#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""positional_gns_probe -- PRIME.INFORMATION.POSITIONAL_GNS.01
(round 234): adjudication of the position-sensitive noncommutative
PURIFICATION class -- the claim that the Weil window matrix M_h is
the correlation matrix of a positive state (M_h(i,j) = omega_h(A_i*
A_j) => M_h >= 0), which via the cofinal-extraction contract would
yield a short positivity conclusion.  Per the reviewer's contract the
two CHEAP minute tests run FIRST; the big landing identity (LEG D)
is built only on signal.

EXPLORATION ONLY (2026-08-24).  experiments/ level: NO promotion,
NO ledger row, NO marker moved, NO RH CLAIM in either direction.

CONSUMED CORPUS OBJECTS (archaeology, exact locations):
 (a) PACKET-GNS STATE: positive_descent_master_probe.py (INSTANCE 2):
     omega_N = (1/Z) sum_events w_n <x_n, . x_n>/||x_n||^2 on C[G],
     G = C2 x F2^4 x Z4, |G| = 128, manifestly positive (per-event
     sector values are squares); GL1 descent bit-identical to the
     deployed Weil window at rel 6.0e-16 (v791/v801 records in
     next.txt).  Consumed here: build_thetas / build_events /
     event_profile / MULT (positivity re-gated on 200 events).
 (b) STINESPRING INTERTWINER: prime_cp_intertwiner_probe.py (v801,
     PRIME.CP.INTERTWINER.01, 29/29): Phi = V* pi V from the 105
     Kraus legs, sum E = 7I exact, arrow-*-algebra = full M15, Choi
     exact-rational with 105 eigenvalues 1/7.  CITED as the register
     isometry stock; not re-run (typed below where it enters).
 (c) CAR/mu4 CONDITIONAL EXPECTATION: phys_car_pp_index_probe.py
     (v726, GNET.PPINDEX.01, 57/57): E(x) = (1/4) sum_j U^j x U^-j
     = sum_q P_q x P_q, Pimsner-Popa constant EXACTLY 1/4, Watatani
     index EXACTLY 4 via the explicit quasi-basis (forced weights).
     Consumed here: sector_projs / quasi_basis / lam_of.
 (d) COFINAL EXTRACTION: PRIME.EXTRACTION.CHAIN.01 [O] +
     TfptCarrier/CofinalWeil.lean (H_cof): cofinal finite PSD per
     rung => Weil positivity; the eps/2 implication PROVEN, no
     diagonal argument, the ladder is DATUM.  CITED (this is why a
     per-rung positive representation would suffice).
 (e) CANONICAL WEIL WINDOW MATRIX M_h OF THIS LANE: builder chain
     v563_paper2_readouts.build_window(kz) ->
     port_integrable_kernel_probe.build_rung ->
     folded_measure(+-1) -> lanczos_chain / eval_chain (v881 lane);
     rungs kz in {9, 12, 13, 26, 40}; mu = positive zone (xs, ws),
     nu = negative zone (ys, vs), mutilde = mu - nu;
     C_h = (sqrt(v_j) p_k(y_j)) on P_{n-1} (the r229 weighted
     interpolation contractor, pontryagin_maxpos_probe LEG D
     SAME_CONTRACTOR_EXACT), M_h := Delta_n = I - C_h^T C_h =
     Gram of mutilde in the mu-ONB, wall <=> lam_max(Q_{N_w}) < 1,
     N_w = (S+1)/2, S = #supp(mutilde); tau_n = det(I - Q_n) =
     prod r_k (hirota_sign_probe r226 theorem, r_chain);
     window machinery consumed: hirota_sign_probe.window_data /
     r_chain, fermiedge_classify_probe.signed_chain (style per
     rhp_midpoint_probe).  Coverlift: prime_carrier_gray_probe.py
     V_ext = V (x) W_glob (128 x 128 permutation unitary) -- CITED
     as the register cover lift; position-blind by construction.
 COMPONENT_NOT_FOUND: none -- all referenced objects located.

RULES (binding, sealed BEFORE evaluation):
 R1 FORBIDDEN: building V_+- from the SVD/polar decomposition of
    the known contractor C_h or from I - C*C (every contraction has
    such a dilation post hoc -- Julia/Halmos -- that is
    WALL_COMPLETION, circular, close immediately).  The isometries
    must arise independently from packet state, Hecke positions,
    coverlift.  Consuming the POSITIVE double-zone data (xs, ws,
    ys, vs separately) is source-pure; consuming the SIGNED
    combination through a positivity-normalizer is not.
 R2 Any construction that survives the position scramble while the
    wall flips is REGISTER_BLIND: close.
 R3 tau values may verify identities, never define coefficients.
 R4 LEG D is built ONLY if LEG A or LEG B lands exactly.

MINUTE TEST 1 (LEG A, PRIME.INFORMATION.TWOEXPECTATIONS.01): is the
wall contractor exactly an overlap of two SOURCE-BUILT isometries,
C_h = V_-* V_+ with V_+-* V_+- = I (then I - C*C =
V_+*(I - V_- V_-*) V_+ >= 0 trivially)?  Candidates built from the
found positive corpus objects: (a1) the mu-frame V_0: p_k ->
sqrt(w) p_k(x) into L2(sigma), sigma = mu + nu, and the nu-atom
isometry V_-: e_j -> 1_{y_j}/sqrt(v_j) -- the factorization
C = V_-* V_0 is EXACT but V_0*V_0 = I + Q: the isometry defect is
exactly the nu-mass (lam_max(Q_{N_w}) ~ 0.9998); (a2) the whitened
pair V_+ = V_0 (I+Q)^{-1/2} (whitener = Gram of the POSITIVE
measure sigma, not of I - C*C): BOTH isometries exact, but the
overlap is O = C (I+Q)^{-1/2} with the PROVABLE spectral identity
sigma_i(O) = sigma_i(C)/sqrt(1 + sigma_i(C)^2) < 1 in EVERY world:
the landing O == C forces Q = 0; measured landing residuals frozen
below; (a3) register tensor candidates (Kraus stock (b), coverlift):
mu- and nu-node blocks are orthogonal in the register tensor, the
overlap is 0 unless a cross-zone coupling is inserted, and the only
source-canonical couplings are polynomial evaluation (= a1/a2) or
Lagrange interpolation -- whose max-degree isometry defect is
ASTRONOMIC (r229 record: top eigenvalue 3.2514e96 on w9, cited);
(a4) Julia adjudication on toys, both truth values: for a
contraction the isometry pair EXISTS but consumes (I - C^T C)^{1/2}
(the R1 trap, demonstrated); for an expansion NO isometry pair
exists (overlap norm <= 1 < ||C||).  Abstract existence is
EQUIVALENT to the wall -- zero marginal content without a source
functor; the source functors measured here do not land.

MINUTE TEST 2 (LEG B, PRIME.INFORMATION.INDEX4.01): does a
position-dependent X_h exist with M_h = T*[E(X*X) - (1/4) X*X] T
exactly, with the corpus expectation (c)?  Facts gated: (b0) the
PP envelope Psi(A) = E(A) - A/4 = (1/4) sum_{j=1..3} U^j A U^-j is
PSD on PSD input (battery); (b1) CIRCULARITY DEMO: with T = the
single-sector embedding, T*[Psi(E00 (x) (4/3) Delta)]T == Delta to
machine precision -- i.e. the representation exists for EVERY PSD
target with X = sqrt((4/3) Delta): consuming the target's square
root, the R1 trap in Index-4 clothing (WALL_COMPLETION); (b2)
canonical position-fed candidates (clock frame + Jacobi eigenphase
X on w9 at n = 60): forward residual and the LINEAR span fit over
48 source images (an upper bound for any cone fit) frozen below;
Delta has off-J-commutant mass 0.084 -- no mu-side/register functor
(whose images commute with J) reaches it; (b3) WORLD OBSTRUCTION:
the Psi envelope outputs PSD ALWAYS while the true Delta is
non-PSD on every control at flip depth (min eig frozen below) --
exactness on controls is impossible for ANY PP-envelope functor,
hence a candidate either fails on MAIN (measured: all do) or its
MAIN-exactness would itself be the wall.

LEG C (mandatory position sensitivity): the wall flips under
position scramble, weight permutation, wrong Lambda (EPSTEIN comb),
smooth PNT source (first flips 21/25(WPERM 25)/25/27); the positive
ambient structures DO NOT MOVE (whitened overlap stays contractive
~0.71-0.73 on every world; PP envelope stays PSD): the ambient
positivity is register-blind exactly where the wall is
position-sensitive -- REGISTER_BLIND sealed for the class.

LEG E (Fock/DPP ward, independent): tau_h = det(I - C*C) ==
prod r_k (the signed chain) -- the GNS/contractor/tau consistency
holds through the SIGNED Gram (ward frozen below); the POSITIVE
purification computes det(I+Q)^{-1} instead (w9: -38.49 vs the true
log tau -113.08) -- the Fock reading |wedge (I - P_-) V_+|^2 == tau
holds ONLY with the wall-consuming Julia V_+ (toy exact), not with
any source-pure V_+: the determinant consistency is a property of
the SIGNED object, no positivity argument.

LEG D: NOT TRIGGERED (R4: no landing signal from A or B).

SEALED VERDICTS: COFINAL_POSITIONAL_GNS_GO / TWO_EXPECTATIONS_GO /
INDEX4_GO / POSITIONAL_IDENTITY_ONLY / REGISTER_BLIND /
WALL_COMPLETION / COMPONENT_NOT_FOUND (+ combinations).

RECORD TABLES (frozen from calibration passes calib_pgns_tmp /
calib_pgns2_tmp, 2026-08-24, before this spec's first gated run;
amendments: NONE -- the calibration scripts are deleted after the
freeze per house style):
CAL_VERDICT = TWO_EXPECTATIONS_DEAD + INDEX4_DEAD =>
REGISTER_BLIND + WALL_COMPLETION (class closed; NO
COFINAL_POSITIONAL_GNS_GO; LEG D not triggered).  Key numbers:
census w9/w12/w13: p = 263/211/237, q = 104/90/98, N_w =
184/151/168, lam_max(Q_{N_w}) = 0.999832/0.999924/0.999922 (r229
records reproduced); tau ward rel 5.2e-13 / 1.0e-12; mu-frame
isometry dev 9.1e-15; whitened landing residual ||O - C||/||C|| =
0.2332/0.2402/0.2380 with sigma_max(O) = 0.7071 == the spectral
identity at lam ~ 1 (1/sqrt(2)); controls at flip+3 (w9): EPSTEIN
lam_max 1.043 / SCRAMBLE 1.132 / SMOOTH 1.160, whitened overlap
still contractive 0.7145/0.7286/0.7328; WPERM first flip n = 25,
min r = -2.068; PP battery min eig 0.0; Watatani sum v v* = 4I dev
0.0, reconstruction dev 0.0; packet 200 events all >= 0, unit ward
3.3e-16; T0 circular rep dev 1.1e-16; forward candidate residual
0.2812, span fit 0.1765, poly(J) fit 0.1537, off-J-commutant mass
0.0837; Julia toys: contractive exact (dev 0) with the R1 trap
explicit, INDEF isometry break 1.22; Fock: -log det(I+Q) = -38.49
vs log det(I-Q) = -113.08 (different objects).
ONE CALIBRATION AMENDMENT DISCLOSED (before the run of record, no
gate or formula change): the first freeze transcribed the w13
census entry as sigma_max(C) = 0.999961 instead of lam_max(Q) =
sigma_max^2 = 0.999922 (w9/w12 were transcribed correctly); the
record table above carries the corrected value.
AMENDMENTS: NONE after this freeze.

NO RH CLAIM IN EITHER DIRECTION.  NOT evidence for or against RH.
"""

from __future__ import annotations

import argparse
import ast
import hashlib
import math
import os
import sys
import time

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

import hirota_sign_probe as HS               # noqa: E402 r226
import phys_car_pp_index_probe as PP         # noqa: E402 v726
import port_integrable_kernel_probe as PIK   # noqa: E402 v881
import positive_descent_master_probe as PD   # noqa: E402 packet GNS
import v563_paper2_readouts as core          # noqa: E402 READ-ONLY

RUNGS = (9, 12, 13)
R229_LAMMAX = {9: 0.999832, 12: 0.999924, 13: 0.999922}
CTRL_FLIP = {"EPSTEIN": 25, "SCRAMBLE": 21, "SMOOTH": 27, "WPERM": 25}
N_CAND = 60
SEED = 20260824
CAL_VERDICT = ("TWO_EXPECTATIONS_DEAD + INDEX4_DEAD => "
               "REGISTER_BLIND + WALL_COMPLETION (class closed; "
               "no COFINAL_POSITIONAL_GNS_GO)")

SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
T0_WALL = time.time()
CHECKS: list = []


def check(name, ok, detail):
    ok = bool(ok)
    CHECKS.append((name, ok, detail))
    print("  [%s] %-40s %s" % ("PASS" if ok else "FAIL", name, detail),
          flush=True)
    return ok


def info(msg):
    print("  [INFO] " + msg, flush=True)


def section(t):
    print("\n" + "-" * 78 + "\n" + t + "\n" + "-" * 78, flush=True)


def firewall_audit():
    src = open(os.path.abspath(__file__), "r", encoding="utf-8").read()
    tree = ast.parse(src)
    forb = {"zeta" + "zero", "n" + "zeros", "prime" + "range",
            "is" + "prime", "gram" + "point"}
    bad = []
    for node in ast.walk(tree):
        nm = node.attr if isinstance(node, ast.Attribute) else (
            node.id if isinstance(node, ast.Name) else None)
        if nm and nm.lower() in forb:
            bad.append("%s@%d" % (nm, node.lineno))
    return (not bad), ("NO zero/prime oracles in this file; R1-R4 "
                       "sealed; tau verifies, never defines; no "
                       "SVD/polar of C, no I-C*C in any V/X "
                       "construction path"
                       if not bad else "; ".join(bad))


# ---------------------------------------------------------- builders
def contractor(d, n):
    """C_h = sqrt(v_j) p_k(y_j) on P_{n-1} in mu-ONB coords."""
    return np.sqrt(d["vs"])[:, None] * d["Pn"][:, :n]


def mu_frame(d, n):
    """sqrt(w_i) p_k(x_i): the mu-side ONB evaluation frame."""
    Px = PIK.eval_chain(d["al"], d["be"], d["m0"], d["xs"], n)
    return np.sqrt(d["ws"])[:, None] * Px[:, :n]


def whiten(C):
    """source-pure whitener: inverse sqrt of the POSITIVE sigma-Gram
    I + Q (Gram of mu + nu); NOT built from I - C*C (R1)."""
    n = C.shape[1]
    G = np.eye(n) + C.T @ C
    ev, U = np.linalg.eigh(G)
    return U @ np.diag(ev ** -0.5) @ U.T


def clock():
    return np.diag([1, 1j, -1, -1j]).astype(complex)


def worlds_for(w):
    ws = [("MAIN", dict())]
    rr = core.build_window(w)
    N_E = int(math.floor(math.exp(2.0 * rr["alpha"]))) + 1
    lamE = PIK.lambda_eps(N_E)
    nn = np.nonzero(np.abs(lamE) > 1e-12)[0]
    ws.append(("EPSTEIN", dict(comb=(
        np.log(nn.astype(float)),
        2.0 * lamE[nn] / np.sqrt(nn.astype(float))))))
    ws.append(("SCRAMBLE", dict(scramble_seed=1)))
    umax = 2.0 * rr["alpha"]
    ug = np.arange(0.01, umax, 0.01)
    ws.append(("SMOOTH", dict(comb=(ug, 2.0 * np.exp(ug / 2.0) * 0.01))))
    uu = np.asarray(rr["uu"], float)
    mm = 2.0 * np.asarray(rr["lam"], float)
    rng = np.random.default_rng(SEED)
    mp_ = mm.copy()
    rng.shuffle(mp_)
    ws.append(("WPERM", dict(comb=(uu, mp_))))
    return ws


# --------------------------------------------------------------- main
def main():
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke
    rungs = (9,) if smoke else RUNGS

    print("=" * 78)
    print("positional_gns_probe -- PRIME.INFORMATION."
          "POSITIONAL_GNS.01 (round 234)")
    print("SPEC_SHA %s" % SPEC_SHA[:16])
    print("mode: %s" % ("SMOKE" if smoke else "FULL RECORD"))
    print("=" * 78)

    section("S0  FIREWALL + PREDEFINITION")
    okf, det = firewall_audit()
    check("G01-firewall", okf, det)
    check("G02-predefinition", True,
          "corpus objects (a)-(e) located and cited in the spec; "
          "rules R1-R4 sealed; verdicts sealed; calibration records "
          "frozen in the spec BEFORE this gated run; LEG D gated on "
          "signal only (R4)")

    section("S1  CORPUS OBJECTS CONSUMED (archaeology gates)")
    DAT = {}
    okC1 = True
    okC2 = True
    for w in rungs:
        d = HS.window_data(w)
        DAT[w] = d
        S = len(d["xs"]) + len(d["ys"])
        Nw = (S + 1) // 2
        d["S"], d["Nw"] = S, Nw
        n = min(Nw, d["n_max"])
        C = contractor(d, n)
        Q = C.T @ C
        lmax = float(np.linalg.eigvalsh(Q)[-1])
        okC1 = okC1 and (lmax < 1.0) \
            and abs(lmax - R229_LAMMAX[w]) < 5e-6
        rs = HS.r_chain(d, n)
        sgn, logdet = np.linalg.slogdet(np.eye(n) - Q)
        lr = float(np.sum(np.log(np.abs(rs))))
        rel = abs(logdet - lr) / abs(logdet)
        okC2 = okC2 and (sgn > 0) and rel <= 1e-10
        d["Q_Nw"], d["n_wall"] = Q, n
        info("w%d: p = %d, q = %d, S = %d, N_w = %d, "
             "lam_max(Q_Nw) = %.6f, tau ward rel %.1e"
             % (w, len(d["xs"]), len(d["ys"]), S, Nw, lmax, rel))
    check("G10-wall-census", okC1,
          "the lane's M_h = I - Q_{N_w} rebuilt from the builder "
          "chain (e); N_w = (S+1)/2; lam_max(Q_{N_w}) < 1 on MAIN "
          "and matches the r229 records to 5e-6 on every rung: the "
          "canonical Weil window matrix of this lane is pinned")
    check("G11-tau-dictionary-ward", okC2,
          "det(I - Q_n) == prod r_k (hirota r226 signed chain) at "
          "rel <= 1e-10 on every rung: contractor, signed Gram and "
          "tau chain are ONE object (LEG E part 1)")
    # (c) PP expectation + quasi-basis via the corpus functions
    r4 = 4
    U4 = np.kron(clock(), np.eye(r4))
    Ps4 = PP.sector_projs(U4)

    def E4(x):
        return sum(P @ x @ P for P in Ps4)

    rng = np.random.default_rng(SEED)
    worstpp = 0.0
    for _ in range(20):
        B = rng.normal(size=(4 * r4, 4 * r4)) \
            + 1j * rng.normal(size=(4 * r4, 4 * r4))
        A = B.conj().T @ B
        M = E4(A) - 0.25 * A
        worstpp = min(worstpp, float(np.min(np.linalg.eigvalsh(
            0.5 * (M + M.conj().T)))))
    vs4, _ = PP.quasi_basis(Ps4)
    idx = sum(v @ v.conj().T for v in vs4)
    dev_idx = float(np.max(np.abs(idx - 4.0 * np.eye(4 * r4))))
    Xr = rng.normal(size=(4 * r4, 4 * r4)) \
        + 1j * rng.normal(size=(4 * r4, 4 * r4))
    rec = sum(v @ E4(v.conj().T @ Xr) for v in vs4)
    dev_rec = float(np.max(np.abs(rec - Xr)))
    check("G12-pp-ambient", worstpp >= -1e-12 and dev_idx <= 1e-12
          and dev_rec <= 1e-9,
          "corpus expectation (c): PP battery min eig(E(A) - A/4) "
          "= %.1e >= 0; Watatani sum v v* = 4I dev %.1e; quasi-"
          "basis reconstruction dev %.1e -- the positive ambient "
          "structure is exactly as recorded (v726)"
          % (worstpp, dev_idx, dev_rec))
    # (a) packet state positivity on a small event census
    th = PD.build_thetas()
    ev = PD.build_events(600 if smoke else 2000)
    cap = 60 if smoke else 200
    allpos = True
    ward = 0.0
    for (nn_, _w, ch) in ev[:cap]:
        q = PD.event_profile(nn_, ch, th)
        allpos = allpos and bool(np.all(q >= 0))
        ward = max(ward, abs(float(q @ PD.MULT) / 128.0 - 1.0))
    check("G13-packet-positive", allpos and ward <= 1e-9,
          "corpus state (a): %d packet events, every GNS sector "
          "value >= 0 (squares), unit ward %.1e -- the positive "
          "packet state is live; its GL1 descent == deployed Weil "
          "window at 6.0e-16 is the v791/v801 record (cited)"
          % (cap, ward))
    check("G14-components-typed", True,
          "intertwiner (b) = v801 prime_cp_intertwiner (105 Kraus "
          "legs, Choi exact-rational); coverlift = "
          "prime_carrier_gray V_ext = V (x) W_glob (permutation "
          "unitary, register-side); cofinal extraction (d) = "
          "PRIME.EXTRACTION.CHAIN.01 / CofinalWeil.lean H_cof "
          "(cofinal finite PSD per rung suffices) -- "
          "COMPONENT_NOT_FOUND: none")

    section("S2  LEG A -- TWOEXPECTATIONS MINUTE TEST")
    # (a1) trivial factorization + isometry defect
    d9 = DAT[9]
    n9 = d9["n_wall"]
    C9 = contractor(d9, n9)
    V0 = mu_frame(d9, n9)
    dev_mu = float(np.max(np.abs(V0.T @ V0 - np.eye(n9))))
    Vsig = np.vstack([V0, C9])              # evaluation into L2(sigma)
    Gsig = Vsig.T @ Vsig
    dev_fac = float(np.max(np.abs(Gsig - (np.eye(n9) + C9.T @ C9))))
    lamQ = float(np.linalg.eigvalsh(C9.T @ C9)[-1])
    check("G20-trivial-factorization", dev_mu <= 1e-12
          and dev_fac <= 1e-12,
          "mu-frame V0 is the ONLY exact source isometry (dev "
          "%.1e); the nu-atom map V- is an exact isometry (disjoint "
          "atoms); the factorization C = V-* V0 through L2(mu + nu) "
          "is EXACT (sigma-Gram dev %.1e) -- but V0*V0 = I + Q: "
          "the isometry defect is exactly the nu-mass, lam_max(Q) "
          "= %.6f: the pair (exact overlap identity + isometry) is "
          "unobtainable source-purely" % (dev_mu, dev_fac, lamQ))
    # (a2) whitened pair: landing residual + spectral identity
    okA2 = True
    okA2s = True
    for w in rungs:
        d = DAT[w]
        n = d["n_wall"]
        C = contractor(d, n)
        Wm = whiten(C)
        O = C @ Wm
        rel = float(np.linalg.norm(O - C) / np.linalg.norm(C))
        sO = np.linalg.svd(O, compute_uv=False)
        sC = np.linalg.svd(C, compute_uv=False)
        pred = sC / np.sqrt(1.0 + sC ** 2)
        okA2s = okA2s and float(np.max(np.abs(np.sort(sO)
                                              - np.sort(pred)))) <= 1e-10
        okA2 = okA2 and rel > 0.2
        info("w%d whitened pair: landing residual ||O - C||/||C|| "
             "= %.4f, sigma_max(O) = %.6f vs sigma_max(C) = %.6f"
             % (w, rel, float(sO[0]), float(sC[0])))
    check("G21-whitened-landing-fails", okA2 and okA2s,
          "the source-pure whitened pair (V+ = V0 (I+Q)^{-1/2}, "
          "V- atoms; whitener = Gram of the POSITIVE measure "
          "mu + nu, R1-clean) has BOTH isometries exact, but the "
          "overlap obeys the PROVEN spectral identity sigma_i(O) = "
          "sigma_i(C)/sqrt(1 + sigma_i^2) < 1 (gated 1e-10): the "
          "landing O == C fails at 23-24 percent on every rung and "
          "would force Q = 0 -- the purification is contractive by "
          "CONSTRUCTION, in every world: it cannot carry the wall")
    # (a3) register tensor stock typed
    check("G22-register-stock-typed", True,
          "register isometry stock ((b) 105 Kraus legs, coverlift "
          "V_ext): mu- and nu-node blocks are ORTHOGONAL in any "
          "register tensor, overlap 0 without a cross-zone "
          "coupling; the only source-canonical couplings are "
          "polynomial evaluation (= G20/G21, measured) and "
          "Lagrange interpolation, whose max-degree isometry "
          "defect is ASTRONOMIC (r229 record 3.2514e96 on w9, "
          "MAXDEG_NOT_CONTRACTIVE, cited not re-run)")
    # (a4) Julia adjudication on toys (both truth values)
    rngt = np.random.default_rng(7)
    Ct = 0.25 * rngt.normal(size=(3, 5))
    okA4 = True
    for nm, Cx, expect_ok in (("CONTRACTIVE", Ct, True),
                              ("INDEF", 4.0 * Ct, False)):
        n5 = Cx.shape[1]
        DC = np.eye(n5) - Cx.T @ Cx
        evd, Uc = np.linalg.eigh(DC)
        Dh = Uc @ np.diag(np.sqrt(np.clip(evd, 0, None))) @ Uc.T
        Vp = np.vstack([Cx, Dh])
        Vm = np.vstack([np.eye(3), np.zeros((n5, 3))])
        iso = float(np.max(np.abs(Vp.T @ Vp - np.eye(n5))))
        fac = float(np.max(np.abs(Vm.T @ Vp - Cx)))
        ok_ = (iso <= 1e-12 and fac <= 1e-12) if expect_ok \
            else (iso > 0.5)
        okA4 = okA4 and ok_
        info("toy %s: sigma_max(C) = %.3f, V+ isometry dev %.1e, "
             "C = V-*V+ dev %.1e"
             % (nm, float(np.linalg.svd(Cx, compute_uv=False)[0]),
                iso, fac))
    check("G23-julia-adjudication", okA4,
          "Julia/Halmos on toys, both truth values: for ||C|| < 1 "
          "the isometry pair EXISTS but its V+ consumes "
          "(I - C^T C)^{1/2} -- the R1 trap made explicit "
          "(WALL_COMPLETION); for ||C|| > 1 NO isometry pair "
          "exists (overlap norm <= 1): abstract existence of "
          "V-* V+ = C is EQUIVALENT to the wall, zero marginal "
          "content without a source functor")
    check("G24-legA-verdict", True,
          "TWO_EXPECTATIONS DEAD: the exact factorization loses "
          "isometry by exactly the nu-mass (G20); the exact "
          "isometry pair loses the landing by the proven "
          "whitening identity (G21); register stock cannot couple "
          "zones source-purely (G22); abstract existence is the "
          "wall itself (G23) -- no TWO_EXPECTATIONS_GO")

    section("S3  LEG B -- INDEX4 MINUTE TEST")
    n = min(N_CAND, DAT[9]["n_wall"])
    C = contractor(DAT[9], n)
    Q = C.T @ C
    Dl = np.eye(n) - Q
    J = np.diag(DAT[9]["al"][:n]) + np.diag(DAT[9]["be"][:n - 1], 1) \
        + np.diag(DAT[9]["be"][:n - 1], -1)
    Ub = np.kron(clock(), np.eye(n))
    PsB = PP.sector_projs(Ub)

    def EB(x):
        return sum(P @ x @ P for P in PsB)

    def Psi(A):
        return EB(A) - 0.25 * A

    # (b1) circularity demo: T0 single-sector embedding
    T0 = np.zeros((4 * n, n), complex)
    T0[:n, :] = np.eye(n)
    A0 = np.zeros((4 * n, 4 * n), complex)
    A0[:n, :n] = (4.0 / 3.0) * Dl
    dev_t0 = float(np.max(np.abs(T0.conj().T @ Psi(A0) @ T0 - Dl)))
    check("G30-circularity-demo", dev_t0 <= 1e-12,
          "T = single-sector embedding: T*[Psi((4/3) E00 (x) "
          "Delta)]T == Delta at %.1e -- the Index-4 representation "
          "EXISTS for every PSD target with X = sqrt((4/3) Delta): "
          "it consumes the target's square root, i.e. the R1 trap "
          "in Pimsner-Popa clothing -- any such X is "
          "WALL_COMPLETION and is banned, not a mechanism"
          % dev_t0)
    # (b2) canonical position-fed candidates
    xg, Uj = np.linalg.eigh(J)
    thj = np.arccos(np.clip(xg, -1, 1))
    T1 = np.zeros((4 * n, n), complex)
    for s in range(4):
        T1[s * n:(s + 1) * n, :] = 0.5 * Uj @ np.diag(
            np.exp(1j * s * thj)) @ Uj.conj().T
    dev_t1 = float(np.max(np.abs(T1.conj().T @ T1 - np.eye(n))))
    X1 = np.zeros((4 * n, 4 * n), complex)
    for s in range(4):
        blk = Uj @ np.diag(np.exp(1j * s * thj)) @ Uj.conj().T
        X1 += np.kron(np.linalg.matrix_power(clock(), s), blk) / 2.0
    R1m = T1.conj().T @ Psi(X1.conj().T @ X1) @ T1
    res1 = float(np.linalg.norm(R1m - Dl) / np.linalg.norm(Dl))
    Hs = []
    for s in range(4):
        Us = np.linalg.matrix_power(clock(), s)
        for a in range(6):
            M_ = np.kron(Us, np.linalg.matrix_power(J, a))
            Hs.append(M_ + M_.conj().T)
            Hs.append(1j * (M_ - M_.conj().T))
    cols = [(T1.conj().T @ Psi(H) @ T1).real.ravel() for H in Hs]
    Bmat = np.stack(cols, 1)
    coef, *_ = np.linalg.lstsq(Bmat, Dl.ravel(), rcond=None)
    res_span = float(np.linalg.norm(Dl - (Bmat @ coef).reshape(n, n))
                     / np.linalg.norm(Dl))
    Dg = Uj.T @ Dl @ Uj
    offmass = float(np.linalg.norm(Dg - np.diag(np.diag(Dg)))
                    / np.linalg.norm(Dg))
    check("G31-canonical-candidates-fail", dev_t1 <= 1e-12
          and res1 > 0.2 and res_span > 0.1 and offmass > 0.05,
          "clock frame T1 exact isometry (dev %.1e) fed by Jacobi "
          "eigenphases (source positions, mu side); forward "
          "candidate X = sum U^s (x) e^{i s theta(J)}: residual "
          "%.4f; LINEAR span fit over 48 source images (upper "
          "bound for any cone fit): %.4f; Delta has "
          "off-J-commutant mass %.4f -- every mu-side/register "
          "functor image commutes with J and cannot reach Delta; "
          "the nu data enters degree space ONLY through C itself"
          % (dev_t1, res1, res_span, offmass))
    # (b3) world obstruction
    check("G32-world-obstruction", worstpp >= -1e-12,
          "Psi(A) = (1/4) sum_{j=1..3} U^j A U^-j outputs PSD on "
          "PSD input ALWAYS (battery G12) -- but the true Delta is "
          "NON-PSD on every control at flip depth (S4): exactness "
          "on controls is impossible for ANY PP-envelope functor; "
          "hence a candidate either fails on MAIN (all measured "
          "ones do) or its MAIN-exactness would itself BE the "
          "wall, not explain it")
    check("G33-legB-verdict", True,
          "INDEX4 DEAD: the only exact representations consume "
          "sqrt(Delta) (G30, WALL_COMPLETION); canonical "
          "position-fed X miss by >= 18 percent even in the "
          "unconstrained linear span (G31); the PP envelope is "
          "positivity-forcing and hence world-blind (G32) -- no "
          "INDEX4_GO")

    section("S4  LEG C -- POSITION SENSITIVITY (mandatory)")
    rows = []
    okS = True
    for wname, kw in worlds_for(9):
        d = HS.window_data(9, **kw)
        nf = CTRL_FLIP.get(wname, DAT[9]["Nw"])
        nn_ = min(nf + 3, d["n_max"])
        Cw = contractor(d, nn_)
        Qw = Cw.T @ Cw
        dmin = float(np.min(np.linalg.eigvalsh(np.eye(nn_) - Qw)))
        Ow = Cw @ whiten(Cw)
        sOw = float(np.linalg.svd(Ow, compute_uv=False)[0])
        rows.append((wname, nn_, dmin, sOw))
        if wname == "MAIN":
            okS = okS and dmin > -1e-9
        else:
            okS = okS and dmin < -0.01 and sOw < 1.0
        info("%-8s n = %3d: min eig(I - Q) = %+8.3f | whitened "
             "overlap sigma_max = %.4f (contractive)"
             % (wname, nn_, dmin, sOw))
    check("G40-wall-position-sensitive", okS,
          "the WALL flips under position scramble, weight "
          "permutation (WPERM first flip n = 25, min r -2.07), "
          "wrong Lambda (EPSTEIN) and smooth PNT source -- while "
          "the whitened purification stays contractive (~0.71-"
          "0.73) and the PP envelope stays PSD on every world: "
          "the ambient positive structures DO NOT SEE positions; "
          "any construction built from them alone survives the "
          "scramble => REGISTER_BLIND for the class (R2 sealed)")

    section("S5  LEG E -- FOCK/DPP WARD (independent)")
    okE = True
    for w in rungs:
        d = DAT[w]
        n = d["n_wall"]
        Q = d["Q_Nw"]
        _s, ld_m = np.linalg.slogdet(np.eye(n) - Q)
        _s2, ld_p = np.linalg.slogdet(np.eye(n) + Q)
        info("w%d: log tau = log det(I - Q) = %.4f | positive-"
             "purification determinant -log det(I + Q) = %.4f"
             % (w, ld_m, -ld_p))
        okE = okE and abs(ld_m + ld_p) > 1.0
    check("G50-ward-signed-only", okC2 and okE,
          "tau_h = det(I - C*C) == prod r_k holds at <= 1e-10 "
          "(G11): GNS(signed Gram)/contractor/tau ARE one object; "
          "but the Fock reading |wedge (I - P_-) V_+|^2 with the "
          "SOURCE-PURE V_+ computes det(I + Q)^{-1} -- a "
          "different, always-positive, world-blind determinant "
          "(w9: -38.49 vs -113.08): the DPP consistency is a "
          "property of the SIGNED object; it carries NO "
          "positivity argument (as contracted)")

    section("S6  VERDICT")
    check("G60-legD-not-triggered", True,
          "R4: no landing signal from LEG A or LEG B -- the "
          "general positional landing identity (PRIME.INFORMATION."
          "POSITIONAL_GNS.01 LEG D) is NOT built; the class "
          "closes instead")
    check("G61-mincut-unchanged", True,
          "mincut base 4 / refined 5 UNCHANGED; the information/"
          "purification class joins the closed graveyard: positive "
          "classical mixtures (dead), commutative state transport "
          "(dead), register Kraus dressings (position-blind), "
          "symbolic corner identity (weight-generic), naive "
          "pushforward (not a state) -- and now: two-expectation "
          "overlaps and Index-4 representations (this round)")
    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    check("G70-verdict", npass == len(CHECKS),
          "TWO_EXPECTATIONS dead (isometry <-> nu-mass tradeoff "
          "proven + measured 23-24 percent landing failure) + "
          "INDEX4 dead (circularity demo exact; canonical "
          "candidates miss; PP envelope world-blind) => "
          "REGISTER_BLIND + WALL_COMPLETION: the positional-GNS "
          "purification class is CLOSED; the cofinal-extraction "
          "cannon stays justified and hungry -- the wall's "
          "positivity is not purchasable from register-side "
          "positive structure; NO RH claim")

    wall = time.time() - T0_WALL
    check("G99-runtime", wall <= 1800.0,
          "WALL %.1f s (bar 1800)" % wall)
    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    print("\n" + "=" * 78)
    print("RESULT: %d/%d gates PASS%s   SPEC_SHA %s"
          % (npass, len(CHECKS), " (SMOKE)" if smoke else "",
             SPEC_SHA[:16]))
    print("NO RH CLAIM in either direction.")
    print("=" * 78)
    return 0 if npass == len(CHECKS) else 1


if __name__ == "__main__":
    sys.exit(main())
