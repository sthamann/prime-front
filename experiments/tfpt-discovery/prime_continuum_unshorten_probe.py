#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""prime_continuum_unshorten_probe -- PRIME.CONTINUUM.UNSHORTEN.01:
does the archimedean/pole continuum act as the RM(2,4) vacuum
completion (the 35 origin planes) of the 15-label window objects, and
does the f8 window stay PSD under the combined structure?

THE READING UNDER TEST ([H], frozen): the RM-cascade claim -- the
15-label event checks (the 105 affine planes of AG(4,2) NOT through
0, four labels each) are completed by the 35 ORIGIN planes (0 + a
PG(3,2) line {x, y, x+y}) to the full RM(2,4) check system, the
origin/zero coordinate being the VACUUM point.  Conjecture: the
continuum leg (arch + pole for GL1, arch-only for cuspidal sectors)
plays exactly this completion role -- entering ON the same label
algebra, repairing cross terms, NOT as an additive block (v758
CERT-CONTINUUM-ROOT-DEAD is the binding contrast: arch+pole is
nowhere PSD alone and the additive montage S = S_cont + Delta is
dead; CITED, re-anchored in S2).

REBUILT CONTEXT (integer-exact, no dependence on parallel workers):
  S1 THE RM LAYER: 140 2-flats of AG(4,2) = 105 avoiding 0 + 35
     through 0; label footprints M^T M = 22I + 6J (event checks),
     N^T N = 6I + J (origin planes = the 35 PG(3,2) lines, 3 labels
     each, 7 per label); THE UNSHORTENING IDENTITY
         A140^T A140 = 28I_16 + 7J_16
                     = [[35, 7*1^T], [7*1, (22I+6J) + (6I+J)]]
     -- the origin planes complete the label Gram ON the label
     algebra (the +6I+J cross-term repair) and add the vacuum row
     7*1.  Code layer: the 140 plane indicators span RM(2,4) (F2-dim
     11); the 105 shortened indicators span the vacuum-vanishing
     subcode (dim 10); ONE origin plane unshortens to 11.  Deployed
     label Gram re-anchored: doily B B^T = 4I + 3J (v752/v756
     convention, rebuilt from the symplectic form).
THE CONSTRUCTION RULE (task 1, frozen -- Candidate A):
  per sector s in {GL1 (arch + pole), f8 (arch only, conductor 8)}
  and rung M, on R^M_vac (+) R^{15 M}_lab:
      W(s, M) = [[ V ,           R^T        ],
                 [ R ,  ((4I+3J)/7) (x) T_dep(s) ]]
      R = c_b (1_15 (x) T_cont(s)),   c_b = 7 / sqrt(35 * 28)
                                          = 1/sqrt(20)
      V = T_cont(s)                       (Candidate A: the full
                                           continuum lag row in the
                                           vacuum slot)
  -- label block = THE DEPLOYED 15-label object (doily Gram, unit
  diagonal) times the certified window; vacuum row/column = the
  continuum lags with the RM border weight G16[0,x]/sqrt(G16[0,0]
  G16[x,x]) = 7/sqrt(35*28).  COMPATIBILITY WARD (exact): the
  compression to any single label reproduces T_dep identically
  (diag((4I+3J)/7) = 1).  PREDECLARED ITERATION (task 3): if GL1
  fails PSD under A, iterate ONCE to
      Candidate B: V = kappa I_M, kappa = c_cont(s)[0]  (the c0 /
      counterterm constant in the vacuum slot instead of the full
      lag row) -- documented, no further iteration.
  EXACT SYMMETRY REDUCTION (S15-equivariance, warded once against
  the full 16M-dim matrix at M = 256):
      W ~= [(4/7) T_dep]^{(+)14}  (+)  [[V, (sqrt3/2) T_cont],
                                        [(sqrt3/2) T_cont, 7 T_dep]]
PSD TESTS (task 2, frozen bars -1e-10 ||block||_2, rungs X = 4..10):
  (a) GL1 unshortened window PSD + the compression ward;
  (b) f8 unshortened window PSD (arch-only vacuum slot) -- the kill
      test: measured exactly;
  (c) THE SHAPE DIAGNOSTIC ([H] identification): the vacuum-induced
      label coupling s[x,y] = tr((R R^T)_{xy})/M, fitted to
      a I + b J (frozen least squares); the RM completion demands
      shape 6I + J (a/b = 6, residual 0).  A SINGLE vacuum slot
      induces a rank-one label coupling (pure J, a = 0): if measured
      so, the identification FAILS with a structural lesson -- the
      6I component requires the 35 origin planes as 35 SEPARATE
      check rows (N (x) legs, induced coupling N^T N = 6I + J), a
      35-row Stinespring dilation, not a one-slot bordering; named
      as the corrected target.
CONTROLS (must fire):
  K1 scrambled vacuum row (independent LCG lag permutation per
     label): the induced-coupling shape residual jumps > 0.05;
  K2 the Epstein x^2+5y^2 window in the vacuum slot: the vacuum
     principal block breaks PSD (lambda_min < -10; corpus analogue
     -156);
  K3 a random 16th row (LCG uniform lags per label): fails the
     shape statistic (residual > 0.1).
VERDICT ENUM (frozen):
  UNSHORTEN-CARRIES  : GL1 compatible + f8 PSD + shape matches
                       (res <= 1e-10 and 5.5 <= a/b <= 6.5) -- the
                       vacuum-completion reading gains measured
                       support; the path-state construction then
                       needs the stated dilation data.
  UNSHORTEN-PSD-ONLY : PSD holds, the 6I+J shape fails -- the
                       completion reading stays [H].
  UNSHORTEN-DEAD     : f8 or the GL1 ward/PSD fails after the
                       documented B iteration -- the route's kill,
                       typed plainly.
RESULTS (2026-08-06, first run after freeze, no repairs; 17/19
checks with the two FAILs being the PSD deciders themselves;
controls 3/3; 17.7 s; VERDICT: UNSHORTEN-DEAD -- the route's kill,
typed plainly):
  *  RM layer integer-exact ([E]): 140 = 105 + 35; M^T M = 22I+6J,
     N^T N = 6I+J, A^T A = 28I+7J; code dims 11 / 10 / 11; doily
     B B^T = 4I+3J rebuilt.  The UNSHORTENING IDENTITY holds: the
     origin planes complete ON the label algebra (+6I+J) plus the
     vacuum row 7*1.
  *  v758 contrast re-anchored: bare T_cont nowhere PSD (GL1
     arch+pole -4.97 -> -141 over X = 4..10; f8 arch -0.58 ->
     -0.72); certified T_dep thin-PSD (GL1 +1.2e-5, f8 +3.2e-5 at
     top).
  *  Candidate A: GL1 -7.4 -> -212, f8 -1.24 -> -1.89 (all rungs
     NEG; the vacuum principal block is the bare continuum -- the
     v758 kill transfers verbatim).  Documented single iteration to
     Candidate B (kappa I vacuum slot; kappa = 2.771 GL1 / 7.590
     f8): GL1 -5.6 -> -133, f8 -0.52 -> -1.28 -- STILL NEG on every
     rung; the u-sector Schur object 7 T_dep - (3/(4 kappa))
     T_cont^2 reaches -6.5e+3 (GL1; ||T_cont||^2 = 2.4e+4) against
     ~1e-5 margins.  The wall is SCALE: thin-PSD windows cannot
     absorb any O(1)+ continuum re-entry through a single vacuum
     coordinate.
  *  Shape diagnostic: the vacuum-induced label coupling fits
     a = -4.7e-16, b = +3.876, res = 3.0e-17 -- a RANK-ONE pure-J
     coupling; the RM demand 6I+J is unreachable from one slot (the
     6I component needs 35 separate origin-check rows: N (x) legs
     give N^T N = 6I+J exactly -- the corrected target, a 35-row
     Stinespring dilation, named as the next falsifier).
  *  Reduction ward: full 4096-dim matrix == S15 block reduction to
     6.3e-16 rel.  Compression ward exact (label diag = T_dep).
  *  Controls: K1 scrambled border res 0.066 > 0.05; K2 Epstein
     vacuum block -156 < -10; K3 random row res 0.186 > 0.1.

FENCES: NO RH / GRH claim (finite-level windows); deployed machinery
READ-ONLY; exploration only, ONE new file, writes nothing; no .md,
no commits; AST firewall (no prime tables / zeta symbols).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/prime_continuum_unshorten_probe.py
"""

import ast
import hashlib
import math
import os
import sys
import time
from itertools import combinations

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
PRIME.CONTINUUM.UNSHORTEN.01 spec v1 (frozen 2026-08-06, before the
first run).  Grid D = 1/64, M_TOP = 640, rungs 256..640 step 64
(X = 4..10), N cap 22050, PSD bar -1e-10 ||block||_2.  RM layer:
140 = 105 + 35 flats of AG(4,2), M^T M = 22I+6J, N^T N = 6I+J,
A^T A = 28I+7J, F2-dims 11 / 10 / 11; doily B B^T = 4I+3J.
Construction: label block ((4I+3J)/7) (x) T_dep; border c_b =
1/sqrt(20), R = c_b (1 (x) T_cont); Candidate A vacuum V = T_cont,
Candidate B (one predeclared iteration) V = c_cont[0] I.  Reduction
ward at M = 256 vs the full 16M matrix (<= 1e-8 rel).  Shape
statistic: s[x,y] = tr((R R^T)_{xy})/M, LS fit to aI + bJ;
identification bar res <= 1e-10 and a/b in [5.5, 6.5].  Controls:
K1 scrambled border res > 0.05; K2 Epstein vacuum block < -10;
K3 random row res > 0.1.  LCG seed 20260806.  Verdict enum
UNSHORTEN-CARRIES / -PSD-ONLY / -DEAD.  NO RH/GRH claim; deployed
objects read-only; writes nothing.
"""

DGRID = 1.0 / 64.0
M_TOP = 640
ALPHA_TOP = 0.5 * M_TOP * DGRID
RUNGS = (256, 320, 384, 448, 512, 576, 640)
N_CAP = 22050
PSD_BAR = 1.0e-10
EULER = 0.5772156649015328606
C_BORDER = 7.0 / math.sqrt(35.0 * 28.0)          # = 1/sqrt(20)
CU = math.sqrt(15.0) * C_BORDER                  # = sqrt(3)/2
WARD_M = 256
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


# ============================================= S1 the RM(2,4) layer
def gf2_rank(vectors, width=16):
    rows = [int(v) for v in vectors]
    rank = 0
    for bit in range(width):
        piv = None
        for i, r in enumerate(rows):
            if (r >> bit) & 1:
                piv = i
                break
        if piv is None:
            continue
        pv = rows.pop(piv)
        rows = [r ^ pv if (r >> bit) & 1 else r for r in rows]
        rank += 1
    return rank


def s1_rm_layer():
    section("S1 -- the RM(2,4) unshortening layer (integer-exact)")
    pts = list(range(16))
    subs = set()
    for x in range(1, 16):
        for y in range(x + 1, 16):
            subs.add(frozenset({0, x, y, x ^ y}))
    subs = sorted(tuple(sorted(s)) for s in subs)
    flats = set()
    for U in subs:
        for a in pts:
            flats.add(frozenset(a ^ u for u in U))
    flats = sorted(tuple(sorted(f)) for f in flats)
    origin = [f for f in flats if 0 in f]
    event = [f for f in flats if 0 not in f]
    check("S1.1 census: 35 subspaces, 140 2-flats = 105 event (0 "
          "avoided, 4 labels) + 35 origin (0 + a PG(3,2) line, 3 "
          "labels)",
          len(subs) == 35 and len(flats) == 140
          and len(event) == 105 and len(origin) == 35
          and all(len(set(f) - {0}) == 3 for f in origin)
          and all(len(f) == 4 for f in event))

    N = np.zeros((35, 15), dtype=np.int64)
    for i, f in enumerate(origin):
        for x in f:
            if x:
                N[i, x - 1] = 1
    M = np.zeros((105, 15), dtype=np.int64)
    for i, f in enumerate(event):
        for x in f:
            M[i, x - 1] = 1
    NtN = N.T @ N
    MtM = M.T @ M
    I15 = np.eye(15, dtype=np.int64)
    J15 = np.ones((15, 15), dtype=np.int64)
    check("S1.2 footprints EXACT: N^T N = 6I + J (origin planes / "
          "PG lines) and M^T M = 22I + 6J (event checks)",
          np.array_equal(NtN, 6 * I15 + J15)
          and np.array_equal(MtM, 22 * I15 + 6 * J15))

    A = np.zeros((140, 16), dtype=np.int64)
    for i, f in enumerate(flats):
        for x in f:
            A[i, x] = 1
    G16 = A.T @ A
    check("S1.3 THE UNSHORTENING IDENTITY: A140^T A140 = 28I + 7J "
          "= [[35, 7*1],[7*1, (22I+6J) + (6I+J)]] -- the 35 origin "
          "planes complete the label Gram ON the label algebra "
          "(cross-term repair +6I+J) and add the vacuum row",
          np.array_equal(G16, 28 * np.eye(16, dtype=np.int64)
                         + 7 * np.ones((16, 16), dtype=np.int64))
          and G16[0, 0] == 35 and np.all(G16[0, 1:] == 7))

    def mask(f):
        m = 0
        for x in f:
            m |= 1 << x
        return m

    mon = [0xFFFF]                                   # the constant 1
    for i in range(4):
        mon.append(sum(1 << p for p in pts if (p >> i) & 1))
    for i, j in combinations(range(4), 2):
        mon.append(sum(1 << p for p in pts
                       if ((p >> i) & 1) and ((p >> j) & 1)))
    rk_code = gf2_rank(mon)
    all_words = mon + [mask(f) for f in flats]
    rk_planes = gf2_rank([mask(f) for f in flats])
    rk_joint = gf2_rank(all_words)
    rk_short = gf2_rank([mask(f) for f in event])
    rk_unsh = gf2_rank([mask(f) for f in event] + [mask(origin[0])])
    check("S1.4 code layer: dim RM(2,4) = 11 (monomials deg <= 2); "
          "the 140 plane indicators SPAN it (rank 11, membership "
          "exact); the 105 shortened checks span the vacuum-"
          "vanishing subcode (rank 10); ONE origin plane unshortens "
          "to 11",
          rk_code == 11 and rk_planes == 11 and rk_joint == 11
          and rk_short == 10 and rk_unsh == 11)

    B = np.zeros((15, 15), dtype=np.int64)
    for x in range(1, 16):
        for y in range(1, 16):
            x1, x2, x3, x4 = (x >> 0) & 1, (x >> 1) & 1, \
                (x >> 2) & 1, (x >> 3) & 1
            y1, y2, y3, y4 = (y >> 0) & 1, (y >> 1) & 1, \
                (y >> 2) & 1, (y >> 3) & 1
            pair = (x1 * y2 + x2 * y1 + x3 * y4 + x4 * y3) % 2
            B[x - 1, y - 1] = int(pair == 0)
    check("S1.5 deployed label Gram re-anchored: doily B (symplectic "
          "perp incidence) has row degree 7, diag 1, B B^T = 4I + 3J "
          "(v752/v756 [E+Lean] convention rebuilt)",
          np.array_equal(B @ B.T, 4 * I15 + 3 * J15)
          and np.all(np.diag(B) == 1)
          and np.all(B.sum(axis=1) == 7))
    return NtN


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
    dev = float(np.max(np.abs(cdep - c_ref)))
    return dict(cont=ccont, dep=cdep, dev=dev)


def build_f8():
    a = cfp.eta_f8(N_CAP)
    spf = np.zeros(N_CAP + 1, dtype=np.int64)
    for p in range(2, N_CAP + 1):
        if spf[p] == 0:
            spf[p::p] = np.where(spf[p::p] == 0, p, spf[p::p])
    primes = [p for p in range(3, N_CAP + 1, 2) if spf[p] == p]
    pos, mas = [], []
    for p in primes:
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
    section("S2 -- the window legs + the v758 contrast (re-anchored)")
    gl1 = build_gl1()
    f8 = build_f8()
    check("S2.1 GL1 deployed window rebuilt == v755 channel build "
          "(max dev %.1e <= 1e-9)" % gl1["dev"], gl1["dev"] <= 1e-9)
    rows = {}
    for nm, d in (("GL1", gl1), ("f8", f8)):
        dep = [lam_min_mat(sla.toeplitz(d["dep"][:M]))
               for M in RUNGS]
        con = [lam_min_mat(sla.toeplitz(d["cont"][:M]))
               for M in RUNGS]
        rows[nm] = (dep, con)
        print("      %-4s T_dep  lambda_min: %s"
              % (nm, " | ".join("%+.2e" % l for l, _ in dep)))
        print("      %-4s T_cont lambda_min: %s   ||T_cont||(top) "
              "= %.2e" % (nm, " | ".join("%+.2e" % l
                                         for l, _ in con),
                          con[-1][1]))
    ok_dep = all(all(l >= -PSD_BAR * n for l, n in rows[nm][0])
                 for nm in ("GL1", "f8"))
    check("S2.2 certified legs re-anchored: T_dep(GL1) and T_dep(f8) "
          "PSD on all rungs (thin margins)", ok_dep)
    neg_cont = all(rows[nm][1][-1][0] < 0 for nm in ("GL1", "f8"))
    check("S2.3 THE v758 CONTRAST (cited, re-anchored): the bare "
          "continuum Toeplitz is NOT PSD (GL1 arch+pole "
          "lambda_min(top) = %+.2e, f8 arch %+.2e) -- the additive-"
          "block route stays dead; the unshortening must do better "
          "through the vacuum structure"
          % (rows["GL1"][1][-1][0], rows["f8"][1][-1][0]), neg_cont)
    return gl1, f8


# ============================== S3 construction + reduction + ward
def u_block(V, Tc, Td):
    top = np.hstack([V, CU * Tc])
    bot = np.hstack([CU * Tc.T, 7.0 * Td])
    return np.vstack([top, bot])


def sector_ladder(d, cand):
    """lambda_min of W(s, M) per rung by the exact S15 reduction:
    min( (4/7) lam(T_dep), lam(u-block) )."""
    out = []
    for M in RUNGS:
        Td = sla.toeplitz(d["dep"][:M])
        Tc = sla.toeplitz(d["cont"][:M])
        V = Tc if cand == "A" else float(d["cont"][0]) * np.eye(M)
        lu, nu = lam_min_mat(u_block(V, Tc, Td))
        lp, npn = lam_min_mat(Td)
        out.append((min(4.0 / 7.0 * lp, lu), max(nu, 7.0 * npn),
                    lu, 4.0 / 7.0 * lp))
    return out


def s3_construction(gl1):
    section("S3 -- the construction rule, compression ward, "
            "reduction ward")
    print("    RULE (Candidate A): W = [[V, R^T],[R, ((4I+3J)/7) (x) "
          "T_dep]], R = (1/sqrt20)(1_15 (x) T_cont), V = T_cont;")
    print("    Candidate B (predeclared single iteration): V = "
          "c_cont[0] I.  Border weight = G16[0,x]/sqrt(G16[0,0] "
          "G16[x,x]) = 7/sqrt(980).")
    check("S3.1 COMPRESSION WARD (exact): the restriction of the "
          "label block to any single label is 1.0 * T_dep "
          "(diag((4I+3J)/7) = 1) -- the deployed window reproduced "
          "identically", abs((4.0 + 3.0) / 7.0 - 1.0) == 0.0)
    # full-matrix reduction ward at M = 256, candidate B, GL1
    M = WARD_M
    Td = sla.toeplitz(gl1["dep"][:M])
    Tc = sla.toeplitz(gl1["cont"][:M])
    kap = float(gl1["cont"][0])
    G = (4.0 * np.eye(15) + 3.0 * np.ones((15, 15))) / 7.0
    W = np.zeros((16 * M, 16 * M))
    W[:M, :M] = kap * np.eye(M)
    for x in range(15):
        W[:M, (1 + x) * M:(2 + x) * M] = C_BORDER * Tc
        W[(1 + x) * M:(2 + x) * M, :M] = C_BORDER * Tc.T
        for y in range(15):
            W[(1 + x) * M:(2 + x) * M, (1 + y) * M:(2 + y) * M] = \
                G[x, y] * Td
    lam_full, _n = lam_min_mat(W)
    lu, _ = lam_min_mat(u_block(kap * np.eye(M), Tc, Td))
    lp, _ = lam_min_mat(Td)
    lam_red = min(4.0 / 7.0 * lp, lu)
    rel = abs(lam_full - lam_red) / max(abs(lam_full), 1e-300)
    check("S3.2 REDUCTION WARD: full 16M = %d matrix lambda_min = "
          "%+.6e == blockwise reduction %+.6e (rel dev %.1e <= 1e-8) "
          "-- the S15 symmetry reduction is exact"
          % (16 * M, lam_full, lam_red, rel), rel <= 1e-8)
    del W


# ============================================ S4 the PSD deciders
def s4_deciders(gl1, f8):
    section("S4 -- PSD deciders (Candidate A, then the predeclared "
            "B iteration)")
    print("      rung ladder X = 4..10; entries = lambda_min(W) "
          "[u-block | (4/7)T_dep sector]")
    results = {}
    for cand in ("A", "B"):
        for nm, d in (("GL1", gl1), ("f8", f8)):
            lad = sector_ladder(d, cand)
            psd = all(l >= -PSD_BAR * n for l, n, _u, _p in lad)
            results[(cand, nm)] = (psd, lad)
            print("      %s/%-4s: %s  [%s]"
                  % (cand, nm,
                     " | ".join("%+.2e" % l for l, _n, _u, _p in lad),
                     "PSD" if psd else "NEG"))
            print("               u-block leg: %s"
                  % " | ".join("%+.2e" % u for _l, _n, u, _p in lad))
    a_gl1 = results[("A", "GL1")][0]
    check("S4.1 Candidate A / GL1 (full continuum lag row in the "
          "vacuum slot): PSD = %s%s" % (
              a_gl1, "" if a_gl1 else
              " -- the vacuum principal block IS the bare arch+pole "
              "Toeplitz: the v758 kill transfers verbatim; "
              "iterating ONCE to Candidate B as predeclared"),
          True)
    b_gl1, b_f8 = results[("B", "GL1")][0], results[("B", "f8")][0]
    final_gl1 = a_gl1 or b_gl1
    final_f8 = results[("A", "f8")][0] or b_f8
    check("S4.2 FINAL GL1 PSD after the documented iteration "
          "(A: %s, B: %s)" % (a_gl1, b_gl1), final_gl1)
    check("S4.3 FINAL f8 PSD -- the kill test (A: %s, B: %s)"
          % (results[("A", "f8")][0], b_f8), final_f8)
    # anatomy readout: the candidate-B Schur object on the u-sector
    for nm, d in (("GL1", gl1), ("f8", f8)):
        M = M_TOP
        Td = sla.toeplitz(d["dep"][:M])
        Tc = sla.toeplitz(d["cont"][:M])
        kap = float(d["cont"][0])
        S = 7.0 * Td - (CU * CU / kap) * (Tc @ Tc)
        lS, _ = lam_min_mat(S)
        print("    ANATOMY %-4s: kappa = c_cont[0] = %+.4f; u-sector "
              "Schur 7 T_dep - (3/(4 kappa)) T_cont^2: lambda_min = "
              "%+.3e (||T_cont||^2 = %.2e vs thin T_dep margins "
              "~1e-5)" % (nm, kap, lS,
                          float(sla.norm(Tc, 2)) ** 2))
    return results, final_gl1, final_f8


# ============================================= S5 the shape test
def shape_fit(s):
    """LS fit s ~ a I + b J on 15x15; returns (a, b, rel residual)."""
    I15 = np.eye(15)
    J15 = np.ones((15, 15))
    Gm = np.array([[15.0, 15.0], [15.0, 225.0]])
    rhs = np.array([float(np.sum(s * I15)), float(np.sum(s))])
    ab = np.linalg.solve(Gm, rhs)
    fit = ab[0] * I15 + ab[1] * J15
    res = float(np.linalg.norm(s - fit) / max(np.linalg.norm(s),
                                              1e-300))
    return float(ab[0]), float(ab[1]), res


def induced_coupling(blocks, M):
    """s[x,y] = tr(B_x B_y^T)/M for 15 border blocks (M x M)."""
    s = np.zeros((15, 15))
    for x in range(15):
        for y in range(x, 15):
            v = float(np.sum(blocks[x] * blocks[y])) / M
            s[x, y] = s[y, x] = v
    return s


def s5_shape(gl1, NtN):
    section("S5 -- the shape diagnostic ([H] identification test)")
    M = M_TOP
    Tc = sla.toeplitz(gl1["cont"][:M])
    blocks = [C_BORDER * Tc for _ in range(15)]
    s = induced_coupling(blocks, M)
    a, b, res = shape_fit(s)
    ratio = a / b if b != 0 else float("inf")
    match = (res <= 1e-10 and 5.5 <= ratio <= 6.5)
    print("      vacuum-induced label coupling: fit a = %+.4e, "
          "b = %+.4e, a/b = %.3f, residual = %.2e" % (a, b, ratio,
                                                      res))
    print("      RM demand: 6I + J (a/b = 6, residual 0)")
    check("S5.1 shape statistic measured and recorded (frozen "
          "identification bar: res <= 1e-10 AND a/b in [5.5, 6.5]) "
          "-- result: %s" % ("MATCH" if match else
                             "NO MATCH (a = 0: a single vacuum slot "
                             "induces a RANK-ONE pure-J coupling; "
                             "the 6I component is unreachable)"),
          True)
    # the corrected target (readout): 35 separate origin-check rows
    a2, b2, res2 = shape_fit(NtN.astype(float))
    check("S5.2 CORRECTED TARGET (named): 35 origin-check ROWS "
          "(N (x) legs) induce coupling N^T N with fit a = %.1f, "
          "b = %.1f, res = %.1e -- EXACTLY the demanded 6I + J: the "
          "vacuum completion, if it exists, is a 35-row Stinespring "
          "dilation (35 vacuum checks = the origin planes), not a "
          "one-slot bordering" % (a2, b2, res2),
          abs(a2 - 6.0) <= 1e-12 and abs(b2 - 1.0) <= 1e-12
          and res2 <= 1e-12)
    return match


# ================================================== S6 controls
def s6_controls(gl1, f8):
    section("S6 -- controls")
    M = M_TOP
    ccont = gl1["cont"]
    # K1 scrambled vacuum row: independent lag permutation per label
    blocks = []
    for x in range(15):
        cp = ccont[:M].copy()
        for i in range(M - 1, 0, -1):
            j = lcg(i + 1)
            cp[i], cp[j] = cp[j], cp[i]
        blocks.append(C_BORDER * sla.toeplitz(cp))
    a, b, res = shape_fit(induced_coupling(blocks, M))
    CONTROL_FIRED["K1"] = res > 0.05
    check("K1 scrambled vacuum row (independent LCG lag permutation "
          "per label): shape residual %.3f > 0.05 -- the exact "
          "J-structure of the true border is destroyed" % res,
          CONTROL_FIRED["K1"])
    # K2 Epstein window in the vacuum slot
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
    cep = f8["cont"] + catE
    lep, _ = lam_min_mat(sla.toeplitz(cep[:M]))
    CONTROL_FIRED["K2"] = lep < -10.0
    check("K2 the Epstein x^2+5y^2 window in the vacuum slot: the "
          "vacuum principal block breaks PSD (lambda_min = %+.2e < "
          "-10; corpus analogue -156) -- a wrong vacuum object is "
          "detected" % lep, CONTROL_FIRED["K2"])
    # K3 random 16th row
    blocks = []
    for x in range(15):
        rr = np.array([(lcg(2000001) - 1000000) / 1.0e6
                       for _ in range(M)])
        blocks.append(C_BORDER * sla.toeplitz(rr))
    a3, b3, res3 = shape_fit(induced_coupling(blocks, M))
    CONTROL_FIRED["K3"] = res3 > 0.1
    check("K3 random 16th row (LCG uniform lags per label): shape "
          "residual %.3f > 0.1 -- fails the shape statistic as it "
          "must" % res3, CONTROL_FIRED["K3"])


# ================================================================ main
def main():
    print("=" * 74)
    print("PRIME.CONTINUUM.UNSHORTEN.01 -- the continuum as the "
          "RM(2,4) vacuum completion?")
    print("(contrast: v758 CERT-CONTINUUM-ROOT-DEAD; deployed legs: "
          "Gamma_R rule continua + certified windows)")
    print("=" * 74)
    g0()
    NtN = s1_rm_layer()
    gl1, f8 = s2_legs()
    s3_construction(gl1)
    results, final_gl1, final_f8 = s4_deciders(gl1, f8)
    shape_match = s5_shape(gl1, NtN)
    s6_controls(gl1, f8)

    section("VERDICT")
    n_pass = sum(1 for _n, ok in CHECKS if ok)
    n_all = len(CHECKS)
    controls_ok = all(CONTROL_FIRED.get(k, False)
                      for k in ("K1", "K2", "K3"))
    print("%d/%d checks passed; controls %s; runtime %.1f s"
          % (n_pass, n_all, CONTROL_FIRED, time.time() - T0))
    if not (final_gl1 and final_f8):
        v = ("UNSHORTEN-DEAD (GL1 PSD: %s, f8 PSD: %s after the "
             "documented A -> B iteration)" % (final_gl1, final_f8))
        print("""
THE KILL, TYPED PLAINLY (measured above):
  * Candidate A dies by the v758 mechanism VERBATIM: the vacuum
    slot's principal block is the bare continuum Toeplitz, which is
    nowhere PSD (arch+pole for GL1; the arch-only f8 leg measured
    alongside).
  * Candidate B (counterterm constant in the vacuum slot) dies in
    the u-sector Schur object 7 T_dep - (3/(4 kappa)) T_cont^2: the
    certified windows are THIN-PSD (margins ~1e-5) while the border
    re-injects the continuum at O(||T_cont||^2) -- no O(1)-or-larger
    continuum re-entry through a single vacuum coordinate can be
    absorbed.  The scale gap, not the shape, is the wall.
  * The shape diagnostic sharpens the lesson: ONE vacuum slot can
    only induce a rank-one (pure J) label coupling; the RM
    completion demands 6I + J.  The 6I component -- the identity
    part of the repair -- requires the 35 origin planes as 35
    SEPARATE check rows (a Stinespring dilation with border N (x)
    legs, induced coupling N^T N = 6I + J exactly).  The RM integer
    layer itself is EXACT ([E]: 105 + 35 unshortening identity,
    28I + 7J); only its one-slot window transcription is dead.""")
    elif shape_match and controls_ok and n_pass == n_all:
        v = ("UNSHORTEN-CARRIES (GL1 compatible + f8 PSD + 6I+J "
             "shape matched)")
    else:
        v = ("UNSHORTEN-PSD-ONLY (PSD holds; shape %s; the "
             "completion reading stays [H])"
             % ("matched" if shape_match else "FAILS"))
    print("VERDICT: %s" % v)

    section("RECOMMENDED CONTRACT TEXT (report only; nothing written)")
    print("""\
    PRIME.CONTINUUM.UNSHORTEN.01: the RM(2,4) unshortening
    combinatorics is certified integer-exact (140 = 105 event + 35
    origin planes; footprints 22I+6J and 6I+J; completion identity
    28I+7J; code dims 11/10/11; doily 4I+3J re-anchored).  The
    window transcription with the continuum as ONE vacuum
    coordinate is measured as above; the v758 contrast (no additive
    continuum block) is re-anchored and extends: a single-slot
    vacuum bordering re-injects the continuum against thin-margin
    certified windows and cannot carry the 6I component of the
    demanded 6I+J label repair (rank-one obstruction).  NAMED NEXT
    FALSIFIER: the 35-ROW STINESPRING DILATION -- 35 origin-check
    rows N (x) (continuum legs) with induced label coupling
    (6I+J) (x) (leg Gram), where the per-row legs must come from a
    35-fold splitting of the continuum (the Gamma_R rule data per
    origin plane); its PSD question is open and is the corrected
    target shape, exactly parallel to v758's 'cell-wise cascade
    factorization' ending.  NO RH/GRH claim.""")
    return 0 if n_pass == n_all else 1


if __name__ == "__main__":
    sys.exit(main())
