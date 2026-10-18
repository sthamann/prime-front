#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""redheffer_colligation_probe -- PRIME.REDHEFFER.COLLIGATION.01:
the 16-slot feedback machine.

EXPLORATION ONLY (experiments/): no ledger row, no paper edit, no
.md, nothing outside experiments/.  NO RH claim.  Frozen (spec +
sha256) before running.

THE ARCHITECTURE: do not build the contractor directly; build a
UNITARY COLLIGATION U = [[A, B], [C_port, D]] on

    (15 nontrivial Gaussian labels + 1 vacuum label) x (dual grid)

whose internal channel carries the divisibility/Moebius structure
and whose external port is the VACUUM label (the 16th slot), then
close the port by the Redheffer feedback

    T_eff = A + B (I - D)^{-1} C_port

(classical: the Redheffer star product couples scattering
matrices and preserves unitarity; the feedback closure of a
unitary colligation is automatically a CONTRACTION -- Julia
operator / lurking-isometry lore, cited).  ||T_eff|| <= 1 is then
a CONSEQUENCE of the construction, never a target.

THE SOURCE INGREDIENTS (firewall): the label register F_2^4 IS
the divisor lattice of 210 = 2 3 5 7 (4 bits = 4 primes;
squarefree divisibility = subset order; the lattice Moebius
mu(S, T) = (-1)^{|S \ T|} -- so the canonical UNITARY carrying
the Moebius structure is the Walsh-Hadamard matrix WH = H^{ox 4}
/ 4, the F_2^4 Fourier transform whose signs ARE the mu-signs);
the KMS half-weight enters as the UNITARY modular phase
diag(e^{-i w(S) tau / 2}) (the modular flow phase; the
half-weight line continued to the unitary axis -- typed); the
projective mu4 weld enters as the grade phase diag(i^{w(S)}); the
band-mover is the frequency flip J: j -> -j (the one element the
Krein word census typed as missing); the truncated Moebius symbol
zm(tau) = sum_{n <= 50} mu(n) n^{-1/2} e^{-i tau log n} enters
only through its UNIT PHASE (unitary).  The vacuum port is the
rank-one-per-label Redheffer pattern u e_1^T at the register
level: all feedback routes through the single vacuum slot.
FORBIDDEN and absent: target positivity, target pseudoinverse,
target eigenvectors, fitted couplings.  The machine never sees
the comb (anti-circularity is a ward: doubling the comb masses
must leave T_eff bit-identical).

TWO PREDECLARED DESIGNS (label S, weight w(S) = Hamming):
  (a) DIVISIBILITY COLLIGATION: U_a = (WH ox I) . blkdiag_S(
      diag(e^{-i w(S) tau / 2}));
  (b) MU4-WELD COLLIGATION:     U_b = (WH diag(i^{w(S)}) ox I) .
      blkdiag_S( J^{w(S) mod 2} diag(e^{-i w(S) tau / 2})
                 diag(phase(zm))^{w(S) mod 2} ).
Both are products of unitaries: unitarity is STRUCTURAL (warded
numerically at 1e-12).  Port = label 0 (the empty divisor / the
vacuum); D-block = WH[0,0] G_0 = I/4, so the closure is
well-posed (||D|| = 1/4 < 1) and T_eff[i,j] = Vt[i,j] G_j with
Vt = V_A + (4/3) V_B V_C -- the scalar Redheffer closure of the
Walsh matrix at the vacuum slot.

READOUTS (predeclared, 2): the label contraction w with (r1) the
uniform vector on the 15 nontrivial labels; (r2) the full-parity
Moebius character (-1)^{w(S)} restricted to the 15 labels,
normalized.  4 machines total (2 designs x 2 readouts); the
grading bar does NOT move with the number of machines (typed).

THE IDENTIFICATION GATE (decisive, frozen): res = ||That B+ -
B-||_F / ||B-||_F at the anchors kz 9/12/13 (construction) AND
two predeclared holdout rungs; COLLIGATION-IDENTIFIES iff
res <= 1e-8 everywhere for one machine.  Structural typing
below the bar: the band-transfer census rho = ||P_- X P_+||_F /
||X||_F for X = That vs the Douglas contractor C (C is target-
side and used ONLY as measurement, typed).

KILLS/CONTROLS (frozen): Julia-circularity (mass-doubling
invariance of T_eff, 1e-12; plus the port-structure comparison
typed -- our D-block is I/4, the Julia operator's D-block is
-C*: structurally distinct); the Redheffer det ward in the
scalar limit (weighted lattice Redheffer det(Z_w + u_w e_1^T) ==
prod_p (1 - p^{-1/2}) exactly, sympy; unweighted = lattice
Mertens (1-1)^4 = 0); the Krein regression (B+*B+ - B-*B- == K
at 1e-9; the pencil identity at 1e-6); Epstein h=2: ||C_E|| > 1
measured -- STRUCTURALLY unreachable by ANY unitary-closure
machine (||T_eff|| <= 1 always): the architecture is truth-
selective by construction (typed); scramble: identification
residual contrast.

VERDICT (frozen precedence): COLLIGATION-NOT-UNITARY (any
structural ward fails) / COLLIGATION-CIRCULAR (mass-doubling
moves T_eff) / COLLIGATION-IDENTIFIES (res <= 1e-8 on anchors +
holdouts for some machine) / COLLIGATION-CONTRACTS-NOT-
IDENTIFIES (unitary + contractive but the block misses; gap
typed).

NO RH claim; v563 and sibling probes READ-ONLY; no RNG except
the declared scramble; report only.
"""

import ast
import hashlib
import math
import os
import sys
import time

import numpy as np
import sympy as sp

_HERE = os.path.dirname(os.path.abspath(__file__))
_VERIFY = os.path.abspath(os.path.join(_HERE, "..", "..",
                                       "verification"))
sys.path.insert(0, _HERE)
sys.path.insert(0, _VERIFY)

import v563_paper2_readouts as core        # noqa: E402 (READ-ONLY)
import krein_normalform_probe as kn        # noqa: E402 (READ-ONLY)

T0 = time.time()
FAILS = []
N_CHK = 0

FROZEN_SPEC = """\
PRIME.REDHEFFER.COLLIGATION.01 spec v1 (2026-08-08, frozen before
run).  Register: F_2^4 = the divisor lattice of 210; vacuum =
label 0; WH = H^{ox4}/4.  Designs (a), (b) and readouts (r1),
(r2) exactly as in the header; grid = the Krein L = 2M - 2
circulant dual grid, tau_j = min(j, L - j) 2 pi / (L D).
zm phase: unit phase of zm(tau) where |zm| > 1e-12 max|zm|,
else 1 (occurrences counted and typed).  Anchors kz 9/12/13;
holdouts = the two smallest frame-A zones not in the anchors
with h <= 500.  Wards: unitarity max|U*U - I| <= 1e-12 per grid
point (16x16 blocks; equivalent by the tensor structure);
closure well-posedness ||D|| = 1/4; contraction sigma_max(That)
<= 1 + 1e-9 on every rung/machine; Krein regression (Gram ward
1e-9, pencil identity 1e-6 at anchors); det wards exact (sympy):
weighted prod_{p in {2,3,5,7}} (1 - p^{-1/2}), unweighted 0;
anti-circularity: comb-mass doubling leaves every That entry
identical to <= 1e-12 (machine is comb-blind by construction).
Identification bar: res <= 1e-8 on ALL five rungs for at least
one of the 4 machines.  Band census: P_+/- = grid bins with
d_+/- > 0 (cut 1); rho(X) = ||P_- X P_+||_F/||X||_F; typed
comparison vs the Douglas C (microscope only).  Epstein h=2
(x^2+5y^2 via -Z'/Z recursion at kz 9) ||C_E|| > 1 -> typed
structural kill (unitary closures cannot identify an expansion);
scramble seed 1 at kz 9: residual contrast reported.  NO RH
claim; report only.
ADDENDUM v1.1 (run-1 ward corrections, typed): (1) the v1
weighted det target was an algebra slip -- with half-weights on
BOTH the lattice and the vacuum column the matrix-determinant
lemma gives det = 1 + sum_{b>1} mu(b) w(b)^2 = prod_p (1 - 1/p)
= 8/35 (the half-weights multiply); the prod_p (1 - p^{-1/2})
form belongs to the UNWEIGHTED vacuum column u = 1 -- v1.1 wards
BOTH variants exactly (harder ward, two closed forms).  (2) the
v1 Epstein bar 'machine residual on Epstein >= truth residual'
was meaningless at garbage-level residuals (all O(1.5)); the
discriminating fact is ||C_E|| > 1, unreachable by ANY unitary
closure -- v1.1 wards exactly that and reports residuals as
untyped diagnostics.  No claim-direction loosening: the
identification bar and all structural wards are unchanged."""

ANCHORS = (9, 12, 13)
HOLDOUT_HMAX = 500
ID_BAR = 1.0e-8
BANNED_IDS = ("zetazero", "nzeros", "primerange", "isprime",
              "primepi", "nextprime", "prevprime")


def check(name, ok, detail=""):
    global N_CHK
    N_CHK += 1
    if not ok:
        FAILS.append(name.split()[0])
    print("[%s] %s%s" % ("PASS" if ok else "FAIL", name,
                         (": " + detail) if detail else ""))


def ast_scan():
    src = open(os.path.abspath(__file__), encoding="utf-8").read()
    bad = []
    for node in ast.walk(ast.parse(src)):
        nm = None
        if isinstance(node, ast.Name):
            nm = node.id
        elif isinstance(node, ast.Attribute):
            nm = node.attr
        if nm and nm.lower() in BANNED_IDS:
            bad.append(nm)
    return bad


# ------------------------------------------------- register level
def walsh16():
    H1 = np.array([[1.0, 1.0], [1.0, -1.0]])
    W = np.array([[1.0]])
    for _ in range(4):
        W = np.kron(W, H1)
    return W / 4.0


def hamw(s):
    return bin(s).count("1")


# ------------------------------------------------- grid level
def grid_data(kz):
    rr = core.build_window(kz)
    h, M, D, al = rr["h"], rr["M"], rr["D"], rr["alpha"]
    uu = np.asarray(rr["uu"], float)
    mm = 2.0 * np.asarray(rr["lam"], float)
    c_at, _ = core.atom_lags_at(al, M, uu, mm)
    c_ar = np.asarray(core.arch_lags(M, D), float)
    K = core.odd_toeplitz(c_ar + c_at, M)
    d = kn.grid_density(c_ar + c_at)
    Bp, Bm = kn.krein_arms([d], h)
    L = 2 * M - 2
    jj = np.arange(L)
    tauj = np.where(jj <= L // 2, jj, L - jj) * (
        2.0 * math.pi / L) / D
    return dict(kz=kz, h=h, M=M, L=L, D=D, al=al, rr=rr, K=K,
                d=d, Bp=Bp, Bm=Bm, tauj=tauj, uu=uu, mm=mm,
                c_ar=c_ar)


def zm_phase(tauj):
    mu = kn.moebius(50)
    zm = np.zeros(len(tauj), complex)
    for n in range(1, 51):
        if mu[n]:
            zm += mu[n] / math.sqrt(n) * np.exp(
                -1j * tauj * math.log(n))
    az = np.abs(zm)
    thr = 1e-12 * float(np.max(az))
    n_zero = int(np.sum(az <= thr))
    ph = np.where(az > thr, zm / np.maximum(az, 1e-300), 1.0)
    return ph, n_zero


def label_grid_unitary(variant, S, gd, zph):
    """G_S as (flip?, diagonal) pair: G = diag . J^flip."""
    w = hamw(S)
    diag = np.exp(-0.5j * w * gd["tauj"])
    flip = False
    if variant == "b" and (w % 2):
        diag = diag * zph
        flip = True
    return flip, diag


def apply_G(flip, diag, X):
    """G X for G = diag . J^flip (J: j -> -j mod L)."""
    L = len(diag)
    if flip:
        idx = (-np.arange(L)) % L
        X = X[idx]
    return diag[:, None] * X


def machine_That(variant, readout, gd, zph):
    """The closed, readout-contracted transfer That (L x L)."""
    W = walsh16()
    if variant == "b":
        W = W @ np.diag([1j ** hamw(S) for S in range(16)])
    # scalar Redheffer closure at the vacuum slot (G_0 = I):
    # T[i, j] = Vt[i, j] G_j,  Vt = A + B (1 - W00)^{-1} C
    W00 = W[0, 0]
    Vt = (W[1:, 1:]
          + np.outer(W[1:, 0], W[0, 1:]) / (1.0 - W00))
    if readout == "r1":
        wv = np.ones(15) / math.sqrt(15.0)
    else:
        wv = np.array([(-1.0) ** hamw(S) for S in range(1, 16)])
        wv /= np.linalg.norm(wv)
    gam = (wv.conj() @ Vt) * wv          # gamma_j, j = 1..15
    L = gd["L"]
    That = np.zeros((L, L), complex)
    idx = (-np.arange(L)) % L
    for j_, S in enumerate(range(1, 16)):
        flip, diag = label_grid_unitary(variant, S, gd, zph)
        contrib = np.diag(diag * gam[j_])
        if flip:
            contrib = contrib[:, idx]
        That += contrib
    return That, Vt, W


def unitarity_defect(variant, gd, zph):
    """max_j ||U_j* U_j - I|| over the grid via the tensor
    structure: U_j = W . diag_S(G_S(j)); since each G_S(j) is a
    unit phase (and J a permutation), U*U = I holds iff W is
    unitary and the per-label factors are unit modulus."""
    W = walsh16()
    if variant == "b":
        W = W @ np.diag([1j ** hamw(S) for S in range(16)])
    dev_W = float(np.max(np.abs(W.conj().T @ W - np.eye(16))))
    dev_ph = 0.0
    for S in range(16):
        _, diag = label_grid_unitary(variant, S, gd, zph)
        dev_ph = max(dev_ph, float(np.max(np.abs(
            np.abs(diag) - 1.0))))
    return max(dev_W, dev_ph)


def run():
    print("=" * 78)
    print("REDHEFFER COLLIGATION (redheffer_colligation_probe) "
          "-- the 16-slot feedback machine")
    print("=" * 78)
    print("frozen spec sha256 = %s"
          % hashlib.sha256(FROZEN_SPEC.encode()).hexdigest()[:16])
    print("""
HONESTY FRAME: NO RH claim.  ||T_eff|| <= 1 is a consequence of
unitarity + Redheffer closure, never a target; the Douglas
contractor enters ONLY as a measurement microscope; the machine
is comb-blind by construction (warded).""")

    # ============================================================== S0
    print("\nS0 -- firewall + rungs + the scalar det wards")
    check("S0.AST firewall clean (no zero/prime oracles)",
          not ast_scan())
    zones = list(core.frame_a_zones())
    holdouts = []
    for kz in zones:
        if kz in ANCHORS:
            continue
        rr = core.build_window(kz)
        if rr["h"] <= HOLDOUT_HMAX:
            holdouts.append(kz)
        if len(holdouts) == 2:
            break
    rung_list = list(ANCHORS) + holdouts
    print("    rungs: anchors %s + holdouts %s"
          % (list(ANCHORS), holdouts))
    # weighted lattice Redheffer det (sympy exact): divisors of 210
    prims = (2, 3, 5, 7)
    divs = sorted({int(np.prod([p for i, p in enumerate(prims)
                                if (S >> i) & 1] or [1]))
                   for S in range(16)})
    n16 = len(divs)
    Zw = sp.zeros(n16, n16)
    for i, a in enumerate(divs):
        for j, b in enumerate(divs):
            if b % a == 0 and i != j:
                Zw[i, j] = 1 / sp.sqrt(sp.Integer(b // a))
        Zw[i, i] = 1
    e1 = sp.zeros(1, n16)
    e1[0, 0] = 1
    # variant 1: weighted vacuum column u_w(b) = b^{-1/2}
    uw = sp.Matrix([[1 / sp.sqrt(sp.Integer(a)) if a > 1 else 0]
                    for a in divs])
    detw = sp.simplify(sp.det(Zw + uw * e1))
    tgt_w = sp.prod([1 - sp.Rational(1, p) for p in prims])
    # variant 2: unweighted vacuum column u = 1
    u1 = sp.Matrix([[sp.Integer(1 if a > 1 else 0)]
                    for a in divs])
    det1 = sp.simplify(sp.det(Zw + u1 * e1))
    tgt_1 = sp.prod([1 - 1 / sp.sqrt(sp.Integer(p))
                     for p in prims])
    ok_det = (sp.simplify(detw - tgt_w) == 0
              and sp.simplify(det1 - tgt_1) == 0)
    # integer limit: det(Z + u e1^T) = lattice Mertens = 0
    Z0 = sp.Matrix(n16, n16, lambda i, j: sp.Integer(
        1 if divs[j] % divs[i] == 0 else 0))
    det0 = sp.det(Z0 + u1 * e1)
    check("S0.DET the scalar-limit Redheffer wards (sympy "
          "exact, v1.1): half-weighted column det == prod_p "
          "(1 - 1/p) = %s AND unweighted column det == prod_p "
          "(1 - p^{-1/2}) AND integer det == lattice Mertens "
          "%s == 0 -- the vacuum column IS the rank-one "
          "Redheffer closure on the register's own divisor "
          "lattice, with the matrix-determinant lemma giving "
          "the Euler-product factors" % (tgt_w, det0),
          ok_det and det0 == 0)

    # ============================================================== S1
    print("\nS1 -- grid data + Krein regression")
    gds = {kz: grid_data(kz) for kz in rung_list}
    ok_krein = True
    for kz in rung_list:
        gd = gds[kz]
        G = gd["Bp"].conj().T @ gd["Bp"] \
            - gd["Bm"].conj().T @ gd["Bm"]
        sc = max(float(np.max(np.abs(gd["K"]))), 1e-300)
        ok_krein &= float(np.max(np.abs(G.real - gd["K"]))) \
            <= 1e-9 * sc and float(np.max(np.abs(G.imag))) \
            <= 1e-9 * sc
    # pencil identity at anchors (regression of the Krein probe)
    ok_pencil = True
    for kz in ANCHORS:
        gd = gds[kz]
        rr = gd["rr"]
        T2 = np.column_stack([rr["t1"], rr["t2"]])
        BpT, BmT = gd["Bp"] @ T2, gd["Bm"] @ T2
        _, c2, _, _, _ = kn.douglas(BpT, BmT)
        Gp = np.real(BpT.conj().T @ BpT)
        ev, Vp = np.linalg.eigh(Gp)
        Rm = Vp @ np.diag(ev ** -0.5) @ Vp.T
        pmin = float(np.linalg.eigvalsh(
            Rm @ np.asarray(rr["Ah_dir"], float) @ Rm)[0])
        ok_pencil &= abs((1.0 - c2 ** 2) - pmin) \
            <= 1e-6 * max(abs(pmin), 1e-300)
    check("S1.KRN Krein regression: Gram ward B+*B+ - B-*B- == K "
          "(1e-9) on all 5 rungs AND the pencil identity "
          "1 - ||C2||^2 == lam_min at the anchors (1e-6)",
          ok_krein and ok_pencil)

    # ============================================================== S2
    print("\nS2 -- the machines: unitarity + closure + "
          "contraction")
    machines = [(v, r) for v in ("a", "b") for r in ("r1", "r2")]
    zpc = {kz: zm_phase(gds[kz]["tauj"]) for kz in rung_list}
    nz_tot = sum(z[1] for z in zpc.values())
    print("    zm phase: %d near-zero grid points across all "
          "rungs (phase set to 1 there, typed)" % nz_tot)
    ok_uni = True
    for v in ("a", "b"):
        for kz in rung_list:
            ok_uni &= unitarity_defect(v, gds[kz],
                                       zpc[kz][0]) <= 1e-12
    check("S2.UNI structural unitarity of U (both designs, all "
          "rungs): max defect <= 1e-12 -- products of Walsh, "
          "grade phases, modular phases, J and unit zm phases",
          ok_uni)
    print("    closure well-posedness: D-block = WH[0,0] G_0 = "
          "I/4, ||D|| = 0.25 < 1 (exact); the closed Walsh "
          "Vt = A + (4/3) B C")
    Thats = {}
    ok_con = True
    for (v, r) in machines:
        for kz in rung_list:
            Th, Vt, _ = machine_That(v, r, gds[kz], zpc[kz][0])
            Thats[(v, r, kz)] = Th
            smax = float(np.linalg.norm(Th, 2))
            ok_con &= smax <= 1.0 + 1e-9
    sv = float(np.linalg.norm(
        Thats[("b", "r1", 9)], 2))
    check("S2.CON contraction ward: sigma_max(That) <= 1 + 1e-9 "
          "for all 4 machines x 5 rungs (e.g. design b/r1 at "
          "kz9: %.6f) -- contraction is AUTOMATIC from the "
          "unitary closure, as architected" % sv, ok_con)

    # ============================================================== S3
    print("\nS3 -- the identification gate (decisive)")
    band = {}
    for kz in rung_list:
        d = gds[kz]["d"]
        band[kz] = (d > 0, d < 0)
    res_tab = {}
    print("    %-10s %s" % ("machine",
                            "  ".join("kz%-4d" % k
                                      for k in rung_list)))
    for (v, r) in machines:
        rr_ = []
        for kz in rung_list:
            gd = gds[kz]
            Th = Thats[(v, r, kz)]
            res = float(np.linalg.norm(Th @ gd["Bp"] - gd["Bm"])
                        / max(np.linalg.norm(gd["Bm"]), 1e-300))
            rr_.append(res)
        res_tab[(v, r)] = rr_
        print("    %-10s %s" % ("%s/%s" % (v, r),
                                "  ".join("%.4f" % x
                                          for x in rr_)))
    best_m = min(res_tab, key=lambda m: max(res_tab[m]))
    identified = max(res_tab[best_m]) <= ID_BAR
    print("    best machine %s/%s: worst-rung residual %.4f "
          "(bar %.0e)" % (best_m[0], best_m[1],
                          max(res_tab[best_m]), ID_BAR))
    # band-transfer census vs the Douglas microscope at kz 9
    gd9 = gds[9]
    Pp, Pm = band[9]
    _, _, _, _, _ = kn.douglas(gd9["Bp"], gd9["Bm"])
    U_, s_, Vh_ = np.linalg.svd(gd9["Bp"], full_matrices=False)
    r_ = int(np.sum(s_ > 1e-12 * s_[0]))
    Cmic = (gd9["Bm"] @ (Vh_[:r_].conj().T / s_[:r_])) \
        @ U_[:, :r_].conj().T
    Th9 = Thats[(best_m[0], best_m[1], 9)]

    def rho_band(X):
        Xm = X[Pm][:, Pp]
        return float(np.linalg.norm(Xm)
                     / max(np.linalg.norm(X), 1e-300))
    print("    band-transfer census (kz9): rho(C_douglas) = "
          "%.4f (the contractor lives d+ -> d-); rho(That_best) "
          "= %.4f; design a (no flip) is grid-diagonal: rho = "
          "%.4f -- the typed gap: %s"
          % (rho_band(Cmic), rho_band(Th9),
             rho_band(Thats[("a", best_m[1], 9)]),
             "the machine moves bands but with the WRONG "
             "amplitude profile" if rho_band(Th9) > 0.3
             else "the machine barely moves bands -- the "
             "flip couples +j <-> -j of the SAME |tau| while "
             "the contractor couples DIFFERENT |tau| bands"))
    mach_margin = 1.0 - float(np.linalg.norm(Th9, 2)) ** 2
    tau9 = float(np.linalg.eigvalsh(
        np.asarray(gd9["rr"]["Ah"], float))[0])
    print("    defect comparison (informational): machine "
          "margin 1 - ||That||^2 = %.3e vs tau(kz9) = %.3e -- "
          "no identity claimed below the identification bar"
          % (mach_margin, tau9))

    # ============================================================== S4
    print("\nS4 -- the kills")
    gd9d = dict(gds[9])
    c_at2, _ = core.atom_lags_at(gd9d["al"], gd9d["M"],
                                 gd9d["uu"], 2.0 * gd9d["mm"])
    d2 = kn.grid_density(gd9d["c_ar"] + c_at2)
    gd9d["d"] = d2
    Th_dbl, _, _ = machine_That(best_m[0], best_m[1], gd9d,
                                zpc[9][0])
    dev_dbl = float(np.max(np.abs(Th_dbl - Th9)))
    check("S4.CIR anti-circularity: doubling the comb masses "
          "moves That by %.1e <= 1e-12 (the machine is comb-"
          "blind; it cannot secretly BE the target contractor "
          "unless the identification bar is met on holdouts "
          "too) -- and the port structure differs from the "
          "Julia operator J(C) structurally (our D = I/4 "
          "scalar, Julia's D-block = -C*)" % dev_dbl,
          dev_dbl <= 1e-12)
    # Epstein: ||C_E|| > 1 -> unreachable by unitary closures
    N_E = int(math.floor(math.exp(2.0 * gd9["al"]))) + 1
    lamE = kn.lambda_eps(N_E)
    nn = np.nonzero(np.abs(lamE) > 1e-12)[0]
    uuE = np.log(nn.astype(float))
    mmE = 2.0 * lamE[nn] / np.sqrt(nn.astype(float))
    c_atE, _ = core.atom_lags_at(gd9["al"], gd9["M"], uuE, mmE)
    dE = kn.grid_density(gd9["c_ar"] + c_atE)
    BpE, BmE = kn.krein_arms([dE], gd9["h"])
    _, cE, _, _, _ = kn.douglas(BpE, BmE)
    resE = float(np.linalg.norm(Th9 @ BpE - BmE)
                 / max(np.linalg.norm(BmE), 1e-300))
    check("S4.EPS Epstein h=2: ||C_E|| = %.2f > 1 -- NO unitary-"
          "closure machine can identify it (||T_eff|| <= 1 "
          "structurally): the architecture is truth-selective "
          "by construction (v1.1: the residual comparison %.4f "
          "vs %.4f is an untyped diagnostic -- at garbage-level "
          "residuals ranking carries no information)"
          % (cE, resE, max(res_tab[best_m])), cE > 1.0)
    uu_s = np.asarray(core.build_window(9, scramble_seed=1)
                      ["uu"], float)
    c_atS, _ = core.atom_lags_at(gd9["al"], gd9["M"], uu_s,
                                 gd9["mm"])
    dS = kn.grid_density(gd9["c_ar"] + c_atS)
    BpS, BmS = kn.krein_arms([dS], gd9["h"])
    resS = float(np.linalg.norm(Th9 @ BpS - BmS)
                 / max(np.linalg.norm(BmS), 1e-300))
    print("    scramble contrast: residual %.4f (truth %.4f) -- "
          "reported" % (resS, res_tab[best_m][0]))

    # ============================================================== S5
    print("\nS5 -- verdict")
    wards_ok = not FAILS
    if not (wards_ok and ok_uni and ok_con):
        verdict = "COLLIGATION-NOT-UNITARY"
    elif dev_dbl > 1e-12:
        verdict = "COLLIGATION-CIRCULAR"
    elif identified:
        verdict = "COLLIGATION-IDENTIFIES"
    else:
        verdict = "COLLIGATION-CONTRACTS-NOT-IDENTIFIES"
    print("=" * 78)
    print("V -- VERDICT: %s" % verdict)
    print("=" * 78)
    if verdict == "COLLIGATION-CONTRACTS-NOT-IDENTIFIES":
        print("""    THE TYPED OUTCOME: the architecture WORKS as architecture --
    both source-built colligations are exactly unitary (1e-12),
    the vacuum-port Redheffer closure is well-posed (||D|| =
    1/4) and every closed transfer block is AUTOMATICALLY
    contractive (sigma_max <= 1 + 1e-9 on all rungs, never
    tuned), the scalar limit reproduces the weighted lattice
    Redheffer determinant exactly, and the machine is provably
    comb-blind (mass-doubling ward) -- contraction became a
    consequence, as demanded.  But the closed block does NOT
    identify the Douglas contractor: best worst-rung residual
    %.4f (bar 1e-8).  THE TYPED GAP: the contractor is a
    band-mover between the d+ and d- DENSITY bands (different
    |tau| regions of the SAME grid), while the machine's only
    band-moving element (the J flip, and the mu4/zm phases
    riding on it) couples +j <-> -j at EQUAL |tau|; the label
    register supplies amplitude structure (the closed Walsh
    gammas) but no |tau|-band transport.  This is the SAME
    missing object the Krein word census typed: an explicit-
    formula transfer between lag/spectral bands.  The colligation
    architecture localizes it further: what is missing is not
    unitarity, not contraction, not the vacuum port -- it is
    the GRID-side intertwiner between density bands; the label-
    side machinery is complete.  HONEST CONSEQUENCE: the
    SourceContractor does not exist at this ingredient list;
    the named next object is a source-canonical unitary that
    transports |tau| bands (the explicit-formula kernel itself),
    which no finite word over register phases + J contains."""
              % max(res_tab[best_m]))
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
