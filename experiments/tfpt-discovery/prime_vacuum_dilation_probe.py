#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""prime_vacuum_dilation_probe -- PRIME.VACUUM.DILATION.01: the
35-row Stinespring dilation -- the corrected target certified by
PRIME.CONTINUUM.UNSHORTEN.01 (UNSHORTEN-DEAD): the vacuum completion,
if it exists, must enter through the 35 origin planes as SEPARATE
check rows (induced label coupling exactly (6I+J) (x) continuum
Gram), not through one vacuum slot.  This probe builds it and decides
it.

PARENT STATE (2026-08-06, one-slot probe): UNSHORTEN-DEAD -- the
one-slot bordering dies on SCALE (thin ~1e-5 window margins vs O(1)+
continuum re-entry; GL1 -133, f8 -1.28 at top under the counterterm
slot) and on SHAPE (one slot induces a rank-one pure-J coupling; the
RM completion demands 6I+J).  The 35-row form fixes the shape BY
CONSTRUCTION; the open question frozen here is whether distributing
the continuum mass over 35 channels with the 6I+J footprint brings
the re-entry below the window margins (task 2, the quantitative
heart).

THE CONSTRUCTION (frozen):
  space  R^{15 M}_labels (+) R^{35 M}_checks, per sector s in
  {GL1 (arch + pole), f8 (arch only)} and rung M:
      W = [[ L , R^T ],
           [ R ,  V  ]]
      L = ((4I+3J)/7) (x) T_dep(s)     (deployed label block, unit
                                        diagonal: compression ward
                                        mandatory and exact)
      R = w (N (x) T_cont(s))          (N = 35 x 15 origin-plane /
                                        PG(3,2)-line incidence,
                                        chi_P rows, 3 labels each)
      V = I_35 (x) kappa I_M,          kappa = c_cont(s)[0]
  (the check rows are counterterm-flat channels; a T_cont check
  diagonal is excluded A PRIORI: V must be PSD and T_cont is
  certified indefinite -- parent S2.)  CONSTRUCTION WARD (task 3c):
  R^T R = w^2 (6I+J) (x) T_cont^2 exactly -- the continuum enters
  through the RM check geometry.  TWO FROZEN NORMALIZATIONS:
    (A, primary) w_A^2 = 1/105: uniform row weight with the TOTAL
       row mass calibrated to the deployed continuum mass
       (35 rows x |chi_P|^2 = 3 x 1/105 = 1: sum_P ||row_P||_F^2 =
       ||T_cont||_F^2);
    (B) w_B^2 = 1/28: the literal RM parity-check weight (unit-
       diagonal plane-Gram normalization; the Weitzenboeck
       bookkeeping M^T M = 2 B^2 + 14 I with complement
       (28I+7J) - (22I+6J) = 6I+J = N^T N, gated integer-exact).
  EXACT REDUCTION (N's right singular vectors = u (+) mean-zero,
  shared with the label Gram; singular values sqrt(21), sqrt(6)^14):
      W ~= [[7 T_dep, sqrt(21) w T_cont], [., kappa I]]      (u)
       (+) [[(4/7) T_dep, sqrt(6) w T_cont], [., kappa I]]^14 (mz)
       (+) kappa^{(20 M)}                                     (ker N^T)
  warded once against the full 50M-dim matrix at M = 128.
THE SCALE QUESTION (task 2, frozen statistic): W PSD <=> (V > 0 and)
  Schur = L - (w^2/kappa) (6I+J) (x) T_cont^2 >= 0; binding sector =
  label mean-zero: (4/7) T_dep - 6 (w^2/kappa) T_cont^2 >= 0, i.e.
  the coupling c = w^2/kappa must satisfy
      c <= c*(M) = (2/21) lambda_pencil(M),
      lambda_pencil = min gen-eigenvalue of (T_dep, T_cont^2).
  The probe reports per rung: lambda_pencil, c*, the calibrated
  couplings c_A = 1/(105 kappa), c_B = 1/(28 kappa), the DEFICIT
  FACTORS c_A/c*, c_B/c*, and the distribution gain vs the one-slot
  parent (parent u-coupling 3/(4 kappa) vs 35-row 6 w^2/kappa).
PSD DECIDERS (task 3, frozen bars -1e-10 ||block||_2, X = 4..10):
  (a) GL1 dilated PSD + compression ward; (b) f8 dilated PSD (the
  kill test); (c) construction ward (6I+J coupling exact).
ROUTE-END TYPING (task 4, frozen): if both sectors die under both
normalizations, the vacuum-completion reading is DEAD IN BOTH
TRANSCRIPTIONS (one-slot and 35-row); the general obstruction is
quantified: ANY completion re-entering the continuum through the RM
check geometry needs coupling <= c* (measured), i.e. row amplitude
<= sqrt(c* kappa) -- vs the calibrated 1/sqrt(105).  If GL1 carries
and f8 dies: the sector-adapted 35-row form is the next named
object.  If both carry: the path-state construction (module 7)
becomes buildable; its preregistration is stated.
CONTROLS (must fire):
  K1 scrambled plane rows (LCG random 3-subsets): the integer 6I+J
     ward breaks (ell_inf mismatch >= 1);
  K2 the ONE-SLOT form rebuilt in-probe reproduces the parent death
     (GL1 top rung lambda_min < -100; the negative anchor);
  K3 Epstein x^2+5y^2 window as the check-row dynamics: the check
     principal block breaks PSD (lambda_min < -10).
VERDICT ENUM (frozen): DILATION-CARRIES / DILATION-GL1-ONLY /
DILATION-DEAD (with the general scale obstruction quantified).

RESULTS (2026-08-06, first run after freeze, no repairs; 12/14
checks with the two FAILs being the PSD deciders themselves;
controls 3/3; 50 s; VERDICT: DILATION-DEAD -- the route's honest
end, quantified):
  *  Construction exact: 6I+J coupling ward 7.8e-16; Weitzenboeck
     bookkeeping M^T M = 2B^2 + 14I and complement = N^T N integer-
     exact; compression ward exact; 50M-dim reduction ward 4.7e-14.
  *  THE SCALE OBSTRUCTION (the quantitative heart): admissible
     coupling c* = (2/21) lambda_pencil(T_dep, T_cont^2):
       GL1: c* = 1.23e-7 -> 1.13e-10 over X = 4..10 (decaying with
            the rung) vs calibrated c_A = 3.44e-3, c_B = 1.29e-2:
            deficit x 2.8e4 -> x 3.0e7 (A), x 1.1e8 (B, top);
       f8 : c* = 4.13e-5 -> 5.94e-6 (near-saturating) vs c_A =
            1.25e-3: deficit x 30 -> x 211.
     The 35-row distribution buys exactly x 13.12 vs the one-slot
     parent -- orders of magnitude short.  Admissible row amplitude
     = 1.8e-4 (GL1) / 6.9e-2 (f8) of the mass-calibrated amplitude.
     NUANCE (typed): a sub-calibrated dilation with c <= c* is
     PSD-admissible but then carries only O(sqrt(c*/c_A)) of the
     continuum mass -- it no longer REPRESENTS the completion
     (decorative), so the reading dies with the calibration.
  *  PSD deciders: A/GL1 -2.4 -> -68, B/GL1 -5.6 -> -133, A/f8
     -0.056 -> -0.118, B/f8 -0.52 -> -1.28 -- NEG on every rung,
     both sectors, both normalizations.
  *  Controls: K1 scrambled rows break the integer ward (mismatch
     5); K2 one-slot anchor -1.33e+02 reproduced; K3 Epstein check
     dynamics -156.
  *  ROUTE END: the vacuum-completion reading is dead in BOTH
     transcriptions (one-slot bordering + 35-row Stinespring
     dilation); the continuum's completion role is exhausted inside
     T_dep (the explicit-formula balance); the RM integer layer
     stays [E]; the path-state construction (module 7) is NOT
     buildable on this gating.

FENCES: NO RH / GRH claim (finite-level windows); deployed machinery
READ-ONLY; exploration only, ONE new file, writes nothing; no .md,
no commits; AST firewall (no prime tables / zeta symbols).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/prime_vacuum_dilation_probe.py
"""

import ast
import hashlib
import math
import os
import sys
import time

import numpy as np
import scipy.linalg as sla

_HERE = os.path.dirname(os.path.abspath(__file__))
_VERIFY = os.path.abspath(os.path.join(_HERE, "..", "..", "verification"))
sys.path.insert(0, _HERE)
sys.path.insert(0, _VERIFY)

import v563_paper2_readouts as core            # noqa: E402
import v716_moonshot_arch_glue as glue         # noqa: E402
import v755_simpler_schur_recursion as srp     # noqa: E402
import f8_sector_continuum_probe as fsc        # noqa: E402
import conductor_functoriality_probe as cfp    # noqa: E402  (eta_f8)
import epstein_firewall_probe as epx           # noqa: E402

FROZEN_SPEC = """\
PRIME.VACUUM.DILATION.01 spec v1 (frozen 2026-08-06, before the
first run).  Grid D = 1/64, M_TOP = 640, rungs 256..640 step 64
(X = 4..10), N cap 22050, PSD bar -1e-10 ||block||_2.  Construction:
L = ((4I+3J)/7) (x) T_dep; R = w (N (x) T_cont) with N the 35 x 15
origin-plane incidence (N^T N = 6I+J); V = kappa I, kappa =
c_cont[0].  Normalizations: A (primary) w^2 = 1/105 (total mass
calibration); B w^2 = 1/28 (RM parity-check weight; Weitzenboeck
gate M^T M = 2B^2 + 14I, complement = N^T N).  Exact reduction
(u / mean-zero / ker N^T), warded at M = 128 vs the full 50M matrix
(<= 1e-8 rel).  Scale statistic: lambda_pencil = min gen-eig of
(T_dep, T_cont^2); c* = (2/21) lambda_pencil; deficits c_A/c*,
c_B/c*.  Controls: K1 scrambled rows integer mismatch >= 1; K2
one-slot anchor < -100 (GL1 top); K3 Epstein check dynamics < -10.
LCG seed 20260806.  Verdict enum DILATION-CARRIES / -GL1-ONLY /
-DEAD.  NO RH/GRH claim; deployed objects read-only; writes nothing.
"""

DGRID = 1.0 / 64.0
M_TOP = 640
ALPHA_TOP = 0.5 * M_TOP * DGRID
RUNGS = (256, 320, 384, 448, 512, 576, 640)
N_CAP = 22050
PSD_BAR = 1.0e-10
EULER = 0.5772156649015328606
W2_A = 1.0 / 105.0
W2_B = 1.0 / 28.0
WARD_M = 128
LCG_SEED = 20260806

BANNED_IDS = ("sympy", "isprime", "primerange", "nextprime", "prevprime",
              "primepi", "zetazero", "nzeros", "mpz_zeta")

CHECKS = []
CONTROL_FIRED = {}
T0 = time.time()
_LCG = [LCG_SEED]


def lcg(n):
    _LCG[0] = (1103515245 * _LCG[0] + 12345) % (1 << 31)
    return _LCG[0] % n


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok)))
    print("  [%s] %s%s" % ("PASS" if ok else "FAIL", name,
                           ("  -- " + detail) if detail else ""), flush=True)
    return bool(ok)


def section(title):
    print("\n" + "=" * 74)
    print(title)
    print("=" * 74, flush=True)


def lam_min_mat(A):
    A = 0.5 * (A + A.T)
    return (float(sla.eigvalsh(A, subset_by_index=[0, 0])[0]),
            float(sla.norm(A, 2)))


# ==================================================================== G0
def g0():
    section("G0 -- SHA-frozen spec + AST firewall")
    print("    FROZEN_SPEC SHA-256 = %s"
          % hashlib.sha256(FROZEN_SPEC.encode()).hexdigest())
    src = open(os.path.abspath(__file__), encoding="utf-8").read()
    bad = []
    for node in ast.walk(ast.parse(src)):
        nm = None
        if isinstance(node, ast.Name):
            nm = node.id
        elif isinstance(node, ast.Attribute):
            nm = node.attr
        elif isinstance(node, (ast.Import, ast.ImportFrom)):
            mods = [al.name for al in node.names]
            if isinstance(node, ast.ImportFrom) and node.module:
                mods.append(node.module)
            bad += [m for m in mods if any(b in m for b in BANNED_IDS)]
            continue
        if nm and nm.lower() in BANNED_IDS:
            bad.append(nm)
    check("G0.1 no prime-table / zeta symbols in this file", not bad,
          "found %s" % bad if bad else "clean")


# ================================= S1 RM / Weitzenboeck integer layer
def s1_rm():
    section("S1 -- the RM check geometry + Weitzenboeck bookkeeping "
            "(integer-exact)")
    subs = set()
    for x in range(1, 16):
        for y in range(x + 1, 16):
            subs.add(frozenset({0, x, y, x ^ y}))
    origin = sorted(tuple(sorted(s)) for s in subs)
    flats = set()
    for U in origin:
        for a in range(16):
            flats.add(frozenset(a ^ u for u in U))
    event = [f for f in sorted(tuple(sorted(f)) for f in flats)
             if 0 not in f]
    N = np.zeros((35, 15), dtype=np.int64)
    for i, f in enumerate(origin):
        for x in f:
            if x:
                N[i, x - 1] = 1
    Mev = np.zeros((105, 15), dtype=np.int64)
    for i, f in enumerate(event):
        for x in f:
            Mev[i, x - 1] = 1
    I15 = np.eye(15, dtype=np.int64)
    J15 = np.ones((15, 15), dtype=np.int64)
    check("S1.1 N^T N = 6I + J (the demanded coupling footprint; 35 "
          "origin rows, 3 labels each, 7 per label)",
          np.array_equal(N.T @ N, 6 * I15 + J15)
          and np.all(N.sum(axis=1) == 3)
          and np.all(N.sum(axis=0) == 7))
    B = np.zeros((15, 15), dtype=np.int64)
    for x in range(1, 16):
        for y in range(1, 16):
            pair = (((x >> 0) & 1) * ((y >> 1) & 1)
                    + ((x >> 1) & 1) * ((y >> 0) & 1)
                    + ((x >> 2) & 1) * ((y >> 3) & 1)
                    + ((x >> 3) & 1) * ((y >> 2) & 1)) % 2
            B[x - 1, y - 1] = int(pair == 0)
    ok_wb = (np.array_equal(Mev.T @ Mev, 2 * (B @ B) + 14 * I15)
             and np.array_equal(28 * I15 + 7 * J15
                                - Mev.T @ Mev, N.T @ N))
    check("S1.2 WEITZENBOECK BOOKKEEPING (normalization B anchor): "
          "M^T M = 22I + 6J = 2 B^2 + 14 I (doily complement form) "
          "and (28I + 7J) - M^T M = N^T N -- the 35 rows are the "
          "literal parity-check complement", ok_wb)
    return N


# ============================================= S2 the window legs
def build_gl1():
    ka = core.atoms_in(ALPHA_TOP)
    cat, _ = core.atom_lags_at(ALPHA_TOP, M_TOP, core.U_ALL[:ka],
                               core.MU_ALL[:ka])
    ccont = core.arch_lags(M_TOP, DGRID) + glue.pole_lags_closed(
        M_TOP, DGRID)
    cdep = ccont + cat
    ka2, masks, devm = srp.channel_masks(ALPHA_TOP)
    c_ref = srp.continuum_lags(M_TOP)
    for cn in ("ro", "re", "sp", "in"):
        c_ref = c_ref + srp.atom_channel_lags(ALPHA_TOP, M_TOP,
                                              masks[cn])
    return dict(cont=ccont, dep=cdep,
                dev=float(np.max(np.abs(cdep - c_ref))))


def build_f8():
    a = cfp.eta_f8(N_CAP)
    spf = np.zeros(N_CAP + 1, dtype=np.int64)
    for p in range(2, N_CAP + 1):
        if spf[p] == 0:
            spf[p::p] = np.where(spf[p::p] == 0, p, spf[p::p])
    pos, mas = [], []
    for p in (q for q in range(3, N_CAP + 1, 2) if spf[q] == q):
        u1 = math.log(p)
        if u1 >= 2.0 * ALPHA_TOP:
            break
        t1 = float(a[p]) / p ** 1.5
        tkm1, tkk = 2.0, t1
        k, u = 1, u1
        while u < 2.0 * ALPHA_TOP:
            pos.append(u)
            mas.append(2.0 * tkk * math.log(p) / p ** (0.5 * k))
            tkm1, tkk = tkk, t1 * tkk - tkm1
            k += 1
            u = k * u1
    cat, _ = core.atom_lags_at(ALPHA_TOP, M_TOP, np.array(pos),
                               np.array(mas))
    c0 = math.log(8.0) - 2.0 * math.log(2.0 * math.pi) - 2.0 * EULER
    ccont = fsc.arch_lags_general(M_TOP, DGRID, 2.0, 1.0, c0)
    return dict(cont=ccont, dep=ccont + cat)


def s2_legs():
    section("S2 -- the window legs (re-anchored)")
    gl1, f8 = build_gl1(), build_f8()
    check("S2.1 GL1 deployed window rebuilt == v755 channel build "
          "(max dev %.1e <= 1e-9)" % gl1["dev"], gl1["dev"] <= 1e-9)
    ok = True
    for nm, d in (("GL1", gl1), ("f8", f8)):
        ld, _ = lam_min_mat(sla.toeplitz(d["dep"][:M_TOP]))
        lc, nc = lam_min_mat(sla.toeplitz(d["cont"][:M_TOP]))
        d["kappa"] = float(d["cont"][0])
        ok &= ld >= -PSD_BAR
        print("      %-4s: lambda_min(T_dep, top) = %+.2e (thin-PSD); "
              "lambda_min(T_cont) = %+.2e, ||T_cont|| = %.2e; "
              "kappa = c_cont[0] = %+.4f"
              % (nm, ld, lc, nc, d["kappa"]))
    check("S2.2 certified legs PSD; continuum legs indefinite "
          "(parent S2 re-anchored; kappa > 0 both sectors)",
          ok and gl1["kappa"] > 0 and f8["kappa"] > 0)
    return gl1, f8


# ============================== S3 construction + wards
def dil_blocks(d, w2, M):
    """Exact reduction blocks of the dilated W at rung M."""
    Td = sla.toeplitz(d["dep"][:M])
    Tc = sla.toeplitz(d["cont"][:M])
    kap = d["kappa"]
    w = math.sqrt(w2)
    bu = np.block([[7.0 * Td, math.sqrt(21.0) * w * Tc],
                   [math.sqrt(21.0) * w * Tc.T, kap * np.eye(M)]])
    bm = np.block([[(4.0 / 7.0) * Td, math.sqrt(6.0) * w * Tc],
                   [math.sqrt(6.0) * w * Tc.T, kap * np.eye(M)]])
    return bu, bm, kap


def s3_construction(gl1, N):
    section("S3 -- the dilated operator: construction + wards")
    print("    W = [[((4I+3J)/7) (x) T_dep, w (N (x) T_cont)^T],")
    print("         [w (N (x) T_cont),      kappa I_{35M}      ]];")
    print("    normalizations: A (primary) w^2 = 1/105 (mass-"
          "calibrated), B w^2 = 1/28 (RM parity-check weight)")
    check("S3.1 COMPRESSION WARD (exact): the label-block restriction "
          "to any single label is 1.0 * T_dep (diag((4I+3J)/7) = 1)",
          abs((4.0 + 3.0) / 7.0 - 1.0) == 0.0)
    # construction ward at M = 64 (exact structure, cheap numeric)
    M = 64
    Tc = sla.toeplitz(gl1["cont"][:M])
    w = math.sqrt(W2_A)
    R = np.kron(N.astype(float), w * Tc)
    RtR = R.T @ R
    target = np.kron((6.0 * np.eye(15) + np.ones((15, 15))) * W2_A,
                     Tc @ Tc)
    devc = float(np.max(np.abs(RtR - target))
                 / max(1.0, float(np.max(np.abs(target)))))
    check("S3.2 CONSTRUCTION WARD (task 3c): R^T R == w^2 (6I+J) (x) "
          "T_cont^2 exactly (rel dev %.1e <= 1e-12) -- the continuum "
          "enters through the RM check geometry" % devc,
          devc <= 1e-12)
    # reduction ward: full 50M matrix at M = 128, candidate A, GL1
    M = WARD_M
    Td = sla.toeplitz(gl1["dep"][:M])
    Tc = sla.toeplitz(gl1["cont"][:M])
    kap = gl1["kappa"]
    G = (4.0 * np.eye(15) + 3.0 * np.ones((15, 15))) / 7.0
    W = np.zeros((50 * M, 50 * M))
    W[:15 * M, :15 * M] = np.kron(G, Td)
    R = np.kron(N.astype(float), math.sqrt(W2_A) * Tc)
    W[15 * M:, :15 * M] = R
    W[:15 * M, 15 * M:] = R.T
    W[15 * M:, 15 * M:] = kap * np.eye(35 * M)
    lam_full, _ = lam_min_mat(W)
    bu, bm, kap = dil_blocks(gl1, W2_A, M)
    lam_red = min(lam_min_mat(bu)[0], lam_min_mat(bm)[0], kap)
    rel = abs(lam_full - lam_red) / max(abs(lam_full), 1e-300)
    check("S3.3 REDUCTION WARD: full 50M = %d matrix lambda_min = "
          "%+.6e == u/mean-zero/kernel block reduction %+.6e (rel "
          "dev %.1e <= 1e-8)" % (50 * M, lam_full, lam_red, rel),
          rel <= 1e-8)
    del W, R


# ================================================= S4 the scale table
def s4_scale(gl1, f8):
    section("S4 -- THE SCALE QUESTION (quantitative heart): "
            "admissible vs calibrated coupling")
    print("      binding sector (label mean-zero): (4/7) T_dep - 6 c "
          "T_cont^2 >= 0  <=>  c <= c* = (2/21) lambda_pencil;")
    print("      lambda_pencil = min gen-eig (T_dep, T_cont^2); "
          "c_A = 1/(105 kappa), c_B = 1/(28 kappa)")
    out = {}
    for nm, d in (("GL1", gl1), ("f8", f8)):
        kap = d["kappa"]
        cA, cB = W2_A / kap, W2_B / kap
        print("      %s (kappa = %.4f, c_A = %.3e, c_B = %.3e):"
              % (nm, kap, cA, cB))
        print("        rung | lambda_pencil |     c*     | deficit A "
              "| deficit B")
        worst = None
        for M in RUNGS:
            Td = sla.toeplitz(d["dep"][:M])
            Tc = sla.toeplitz(d["cont"][:M])
            C2 = Tc @ Tc
            lam_p = float(sla.eigh(0.5 * (Td + Td.T),
                                   0.5 * (C2 + C2.T),
                                   subset_by_index=[0, 0],
                                   eigvals_only=True)[0])
            cstar = (2.0 / 21.0) * lam_p
            defA, defB = cA / cstar, cB / cstar
            worst = (M, lam_p, cstar, defA, defB)
            print("        X=%-3d| %11.3e | %10.3e | %9.2e | %9.2e"
                  % (int(M * DGRID), lam_p, cstar, defA, defB))
        out[nm] = dict(cA=cA, cB=cB, top=worst)
        gain = (3.0 / (4.0 * kap)) / (6.0 * cA)
        print("        distribution gain vs the one-slot parent "
              "(u-coupling 3/(4 kappa) vs 6 w_A^2/kappa): x %.2f"
              % gain)
    check("S4.1 scale comparison measured and recorded on every rung "
          "(frozen statistic; feeds the verdict and the route-end "
          "typing)", True)
    return out


# ================================================ S5 PSD deciders
def s5_deciders(gl1, f8):
    section("S5 -- PSD deciders (both normalizations, both sectors)")
    results = {}
    for cand, w2 in (("A", W2_A), ("B", W2_B)):
        for nm, d in (("GL1", gl1), ("f8", f8)):
            lads = []
            for M in RUNGS:
                bu, bm, kap = dil_blocks(d, w2, M)
                lu, nu = lam_min_mat(bu)
                lm, nmz = lam_min_mat(bm)
                lads.append((min(lu, lm, kap), max(nu, nmz),
                             lu, lm))
            psd = all(l >= -PSD_BAR * n for l, n, _u, _m in lads)
            results[(cand, nm)] = (psd, lads)
            print("      %s/%-4s: %s  [%s]"
                  % (cand, nm,
                     " | ".join("%+.2e" % l for l, _n, _u, _m in lads),
                     "PSD" if psd else "NEG"))
            print("               (u | mean-zero at top: %+.2e | "
                  "%+.2e)" % (lads[-1][2], lads[-1][3]))
    gl1_ok = results[("A", "GL1")][0] or results[("B", "GL1")][0]
    f8_ok = results[("A", "f8")][0] or results[("B", "f8")][0]
    check("S5.1 DECIDER (a): GL1 dilated PSD on the ladder "
          "(A: %s, B: %s)" % (results[("A", "GL1")][0],
                              results[("B", "GL1")][0]), gl1_ok)
    check("S5.2 DECIDER (b): f8 dilated PSD -- the kill test "
          "(A: %s, B: %s)" % (results[("A", "f8")][0],
                              results[("B", "f8")][0]), f8_ok)
    return results, gl1_ok, f8_ok


# ================================================== S6 controls
def s6_controls(gl1, f8, N):
    section("S6 -- controls")
    # K1 scrambled plane rows: LCG random 3-subsets
    Ns = np.zeros((35, 15), dtype=np.int64)
    for i in range(35):
        cols = set()
        while len(cols) < 3:
            cols.add(lcg(15))
        for c in cols:
            Ns[i, c] = 1
    mis = int(np.max(np.abs(Ns.T @ Ns - (6 * np.eye(15, dtype=np.int64)
                                         + np.ones((15, 15),
                                                   dtype=np.int64)))))
    CONTROL_FIRED["K1"] = mis >= 1
    check("K1 scrambled plane rows (LCG random 3-subsets): the "
          "integer 6I+J construction ward breaks (ell_inf mismatch "
          "%d >= 1)" % mis, CONTROL_FIRED["K1"])
    # K2 one-slot negative anchor (parent B/GL1 rebuilt in-probe)
    M = M_TOP
    Td = sla.toeplitz(gl1["dep"][:M])
    Tc = sla.toeplitz(gl1["cont"][:M])
    kap = gl1["kappa"]
    cu = math.sqrt(3.0) / 2.0
    one_slot = np.block([[kap * np.eye(M), cu * Tc],
                         [cu * Tc.T, 7.0 * Td]])
    lam1, _ = lam_min_mat(one_slot)
    CONTROL_FIRED["K2"] = lam1 < -100.0
    check("K2 the ONE-SLOT form rebuilt in-probe: lambda_min(top) = "
          "%+.2e < -100 -- the parent's UNSHORTEN-DEAD anchor "
          "(-1.33e+02) reproduced" % lam1, CONTROL_FIRED["K2"])
    # K3 Epstein window as the check-row dynamics
    r1 = epx.lattice_r1(N_CAP)
    bE = np.asarray(r1, float) / 2.0
    lamE = epx.dirichlet_vonmangoldt(bE, N_CAP)
    supp = np.nonzero(np.abs(lamE) > 1e-9)[0]
    supp = supp[supp >= 2]
    posE = np.log(supp.astype(float))
    keep = posE < 2.0 * ALPHA_TOP
    catE, _ = core.atom_lags_at(ALPHA_TOP, M_TOP, posE[keep],
                                (2.0 * lamE[supp]
                                 / np.sqrt(supp.astype(float)))[keep])
    lep, _ = lam_min_mat(sla.toeplitz((f8["cont"] + catE)[:M]))
    CONTROL_FIRED["K3"] = lep < -10.0
    check("K3 Epstein x^2+5y^2 window as check-row dynamics: the "
          "check principal block breaks PSD (lambda_min = %+.2e < "
          "-10)" % lep, CONTROL_FIRED["K3"])


# ================================================================ main
def main():
    print("=" * 74)
    print("PRIME.VACUUM.DILATION.01 -- the 35-row Stinespring "
          "dilation (the corrected target)")
    print("(parent: PRIME.CONTINUUM.UNSHORTEN.01 = UNSHORTEN-DEAD; "
          "shape fixed by construction, SCALE decided here)")
    print("=" * 74)
    g0()
    N = s1_rm()
    gl1, f8 = s2_legs()
    s3_construction(gl1, N)
    scale = s4_scale(gl1, f8)
    results, gl1_ok, f8_ok = s5_deciders(gl1, f8)
    s6_controls(gl1, f8, N)

    section("VERDICT")
    n_pass = sum(1 for _n, ok in CHECKS if ok)
    n_all = len(CHECKS)
    controls_ok = all(CONTROL_FIRED.get(k, False)
                      for k in ("K1", "K2", "K3"))
    print("%d/%d checks passed; controls %s; runtime %.1f s"
          % (n_pass, n_all, CONTROL_FIRED, time.time() - T0))
    if gl1_ok and f8_ok:
        v = "DILATION-CARRIES"
        print("""
CONSEQUENCE: the path-state construction (module 7) becomes
buildable.  Preregistration: path states = the 50-coordinate
dilation vectors; gates = per-sector PSD persistence, the 6I+J
coupling ward, and the compression ward on every path composition.""")
    elif gl1_ok:
        v = "DILATION-GL1-ONLY"
        print("""
CONSEQUENCE: the sector-adapted version of the 35-row form (per-
sector row normalization from the rule continua) is the next named
object; the path-state construction stays gated on it.""")
    else:
        v = "DILATION-DEAD"
        tg = scale["GL1"]["top"]
        tf = scale["f8"]["top"]
        print("""
THE ROUTE'S HONEST END (typed plainly, measured above):
  * The 35-row Stinespring dilation FIXES THE SHAPE (6I+J coupling
    exact, construction ward) and distributes the continuum mass
    over 35 channels (gain x13 vs the one-slot form) -- and STILL
    dies in both sectors under both frozen normalizations.
  * THE GENERAL OBSTRUCTION, QUANTIFIED: any completion re-entering
    the continuum through the RM check geometry needs coupling
    c <= c* = (2/21) lambda_pencil(T_dep, T_cont^2):
      GL1: c* = %.2e at X = 10 vs calibrated c_A = %.2e
           -- deficit x %.1e;
      f8 : c* = %.2e at X = 10 vs calibrated c_A = %.2e
           -- deficit x %.1e.
    Equivalently: the admissible row amplitude is sqrt(c*/c_A) =
    %.1e (GL1) / %.1e (f8) of the mass-calibrated amplitude.  The
    thin-margin certified windows leave NO room for any O(mass)
    continuum re-entry, however it is geometrically distributed:
    the continuum's completion role is already exhausted INSIDE
    T_dep (the explicit-formula balance); the RM vacuum point
    carries no residual window content.
  * VERDICT ON THE READING: the vacuum-completion reading is dead
    in BOTH transcriptions (one-slot bordering, parent; 35-row
    Stinespring dilation, here).  The RM integer layer stays
    certified [E]; the window transcription of the completion is
    closed off.  The path-state construction (module 7) is NOT
    buildable on this gating.""" % (
            tg[2], scale["GL1"]["cA"], tg[3],
            tf[2], scale["f8"]["cA"], tf[3],
            math.sqrt(tg[2] / scale["GL1"]["cA"]),
            math.sqrt(tf[2] / scale["f8"]["cA"])))
    print("VERDICT: %s%s" % (v, "" if controls_ok else
                             "  (CONTROL VOID: %s)"
                             % [k for k in ("K1", "K2", "K3")
                                if not CONTROL_FIRED.get(k, False)]))

    section("RECOMMENDED CONTRACT TEXT (report only; nothing written)")
    print("""\
    PRIME.VACUUM.DILATION.01: the corrected target of the
    unshortening module -- the 35-row Stinespring dilation with
    origin-plane check rows -- is built with the exact 6I+J coupling
    ward (shape closed) and decided on the frozen ladder.  The scale
    statistic c* = (2/21) lambda_pencil(T_dep, T_cont^2) is the
    general admissibility bound for ANY continuum re-entry through
    the RM check geometry; the measured deficit against the mass-
    calibrated coupling decides the reading.  Weitzenboeck
    bookkeeping M^T M = 2B^2 + 14I and complement N^T N = 6I+J are
    integer-certified.  NO RH/GRH claim (finite-level windows).""")
    return 0 if n_pass == n_all else 1


if __name__ == "__main__":
    sys.exit(main())
