#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""debranges_index_probe --
PRIME.RDAGGER.DEBRANGES_CONTINUATION.01 (round 416):
is P1 a de Branges / Potapov index theorem on the two
finite OP systems (X = mu-chain on X-nodes with u^vee,
Y = hole measure) -- contractive embedding of H(E_Y)
into H(E_X) up to one mode, equivalently kappa(Theta) <= 1,
equivalently Pruefer phase dominance with total deficit
< 2 pi (one winding, basis-free)?

THE OBJECTS (Leg A).  E = A - i B with A = p_n first kind,
B = q_n second kind, Jacobi data of each positive discrete
measure.  Y-degree n_Y = q-1; X-degree n_X = min(d0, |X|-1)
with d0 = N_w-3 the dual interpolating depth (documented
balance: on w9, |X|=263 so n_X = d0 = 181 < |X|-1, the
X-chain is truncated to the interpolant; n_Y = 103).

THE INDEX (Legs B, C).  Three equivalent forms of the
candidate lemma: (i) H(E_Y^lower) hookrightarrow H(E_X) up
to one mode; (ii) rational transfer Theta = M_X M_Y^{-1}
with Potapov index kappa <= 1 (product index, not
per-step positivity); (iii) phi_X' >= phi_Y' except one
deficit interval of total drop < 2 pi.  The basis-free
counter is the number of YY-adjacencies in the merged
sorted zeros (Gauss_X(d0) vs Y-ATOMS = combinatorial
Ruecklauf; same-degree Gauss_X(q-1) vs Gauss_Y(q-1) as
the equal-dimension control).  One mode = at most one YY.

CALIBRATION DISCLOSURE.  HB interlacing, degree balance,
Wronskian, YY-census (MAIN-42 / chi 78+6 / permute /
scramble), localisation vs T0-SV, Herglotz of the two
Stieltjes transforms, and the nneg(T0) mismatch were first
measured in /tmp (r416_cal.py, r416_cal2.py, r416_cal3.py,
r416_cal4.py, r416_cal5.py) on the r409 constructors,
2026-08-29.  Frozen floors below are that measurement,
sealed as gates.  Pins disclosed.  Builder fallback NOT
taken: full census wall 10.0 s (bar 120 s).

FROZEN FROM /tmp (live re-gated, not fitted):
  * SATZ over Q: monic 3-atom X, W(p2,q2) = -gamma_1
    independent of z; gamma_1 > 0 implies the unique
    q2-zero strictly interlaces the two p2-zeros.
  * SATZ: HB interlacing of (p_n, q_n) on every measured
    positive system (MAIN 42/42, chi 84/84, toy, permute,
    scramble).  Classical for positive Jacobi; gated.
  * w9 balance: |X|=263 |Y|=104 d0=181 n_X=181 n_Y=103.
    Both HB.  Herglotz Im m_X, Im m_Y > 0 at 0.3+0.7i.
    nneg(I-T0*T0)=1, ||T0||=1.08014 (r409 pin).
  * PRIMARY FAILS: combinatorial Ruecklauf yyA = # of
    consecutive Y-atoms with no X-Gauss node between
    them equals 3 on flagship MAIN (not <= 1).  Same-
    degree yyS=24 >> 1.  nnegT=1 != yyA.  Dominant YY
    interval vs T0-SV peak loc=0.092 on w9 is luck:
    MAIN loc spans [0.059, 1.000].
  * MAIN-42: HB 42/42; yyA min/med/max 0/4/15;
    P1 28 windows, yyA<=1 only 3/28; PD 14, yyA==0
    only 3/14; corr(yyA, nnegT)=-0.17.
  * chi live 78 yyA 0/7/26; dead 6 yyA 0/2/4 -- death
    is NOT a phase overflow (dead has fewer, not more).
  * KILLS: PERM yyA=4 (same as MAIN median) with
    nnegT=20 -- the world-separator does NOT fire on
    the phase counter; SCR yyA=16 (elevated) still
    != 21.  B=A mutant: interlacing FAILS.  Full-measure
    Uvarov/Herglotz path has index 0 (both measures
    positive) and cannot see the truncated interpolant
    defect.  Constructor: HB from (x, w, n) only.

AUSGANG PHASE_DOMINANCE_REFUTED / HB_CENSUS.
SATZ: HB interlacing of each finite positive OP system;
Wronskian constancy over Q; degree balance.
REFUTED: kappa_phase <= 1 as a P1 equivalent (clean
flagship yyA=3; MAIN P1 25/28 have yyA>=2); the
counting argument (X/Y-zero interlacing via the fold
partition) is closed -- the fold does not force at-most-
one YY of Gauss_X(d0) against the hole atoms.
CENSUS: the YY table.  The Potapov index of T0 itself
remains nneg(I-T*T) (r409 dictionary, not a new HB
theorem).  Does not move the mincut.  No RH claim.

MACHINERY: r409 B.pack_graph / toy_dual / dual_split;
r407 DI (import SHA only); r403 P1.reweight; r226 V
mu_chain / build_measures; r356 dual weights via
dual_split; r392 Uvarov cited as the elementary
Stieltjes step (Herglotz of the finite measures).

NO RH CLAIM.  Finite identities, one named refutation,
one named census.  Research documentation, not a
theorem of RH.  No L* claim.  No R-dagger claim.
"""
from __future__ import annotations

import argparse
import ast
import hashlib
import math
import os
import sys
import time
from fractions import Fraction as Fr

import numpy as np

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DISC = os.path.dirname(os.path.abspath(__file__))
PROB = os.path.join(REPO, "rh", "problem")
for p in (DISC, PROB):
    if p not in sys.path:
        sys.path.insert(0, p)

import borodin_birkhoff_intertwiner_probe as B  # noqa: E402
import dual_intertwiner_probe as DI  # noqa: E402
import high_moment_inertia_probe as HM  # noqa: E402
import p1_construction_probe as P1  # noqa: E402
import dirichlet_matched_frame_probe as DMF  # noqa: E402
import verify_lstar_instance as V  # noqa: E402

B_SHA_PREFIX = "baee9fc5"
DI_SHA_PREFIX = "2ee74c59"
HM_SHA_PREFIX = "bb1dcf6a"
P1_SHA_PREFIX = "ba6817f5"

HB_TOL = 1.0e-8
W9_NX, W9_NY, W9_D0, W9_X, W9_Y = 181, 103, 181, 263, 104
W9_YYA, W9_YYS = 3, 24
W9_OP = 1.080138437
W9_LOC_HI = 0.15
PERM_YYA, SCR_YYA = 4, 16
PERM_NNEG_LO, SCR_NNEG = 15, 21
CORE_N, PD_N, P1_N = 42, 14, 28
P1_LE1 = 3
PD_ZERO = 3
YYA_MED, YYA_MAX = 4, 15
CORR_HI = 0.0
CHI_LIVE, CHI_DEAD = 78, 6
CHI_LIVE_MED, CHI_DEAD_MED = 7, 2
CHI_LIVE_MAX, CHI_DEAD_MAX = 26, 4
HOLD_IM = 1.0e-12

SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
CHECKS = []
T0 = time.time()


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok)))
    print("  [%s] %-44s %s" % ("PASS" if ok else "FAIL", name, detail),
          flush=True)
    return bool(ok)


def section(t):
    print("\n" + "=" * 78)
    print(t)
    print("=" * 78, flush=True)


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
    return (not bad), ("NO zero/prime oracles; HB from Jacobi "
                       "of (x,w); YY-count of Gauss zeros"
                       if not bad else "; ".join(bad))


def antigate_fragment_audit():
    frags = ("poly" + "fit", "curve_" + "fit", "lst" + "sq",
             "mini" + "mize", "Line" + "arRegression")
    src = open(os.path.abspath(__file__), "r", encoding="utf-8").read()
    tree = ast.parse(src)
    hits = []
    for node in ast.walk(tree):
        nm = None
        if isinstance(node, ast.Attribute):
            nm = node.attr
        elif isinstance(node, ast.Name):
            nm = node.id
        elif isinstance(node, ast.FunctionDef):
            nm = node.name
        if nm and any(f in nm for f in frags):
            hits.append("%s@%d" % (nm, node.lineno))
    return hits


def scope_audit(funcname):
    """HB constructors: no target R/A0, no SVD of T0,
    no pack_graph / pack_C."""
    src = open(os.path.abspath(__file__), "r", encoding="utf-8").read()
    tree = ast.parse(src)
    fn = None
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and node.name == funcname:
            fn = node
            break
    if fn is None:
        return ["MISSING:%s" % funcname]
    banned = {"svd", "cholesky", "lstsq", "pinv", "pack_C",
              "chain_C", "r_nm3", "aug_rung", "pack_graph"}
    hits = []
    for sub in ast.walk(fn):
        nm = sub.attr if isinstance(sub, ast.Attribute) else (
            sub.id if isinstance(sub, ast.Name) else None)
        if nm in banned:
            hits.append("%s@%d" % (nm, sub.lineno))
    return hits


# ---------- Q SATZ (Leg A, 3-atom X) ----------
def monic_X_Q():
    """3-atom X from the r409 toy, monic first/second kind
    over Q.  Returns a0, a1, gamma_1, h0, h1 as Fractions."""
    xs, _u, ud, iX, _iY, _d0 = B.toy_dual()
    nodes = [xs[i] for i in iX]
    wts = [ud[i] for i in iX]
    h0 = sum(wts)
    a0 = sum(w * x for w, x in zip(wts, nodes)) / h0
    p1 = [(x - a0) for x in nodes]
    h1 = sum(w * p * p for w, p in zip(wts, p1))
    a1 = sum(w * x * p * p for w, x, p in zip(wts, nodes, p1)) / h1
    g1 = h1 / h0
    return a0, a1, g1, h0, h1


def wronskian_Q(a0, a1, g1, z):
    """p2 = (z-a1)(z-a0) - g1, q1 = 1, p1 = z-a0, q2 = z-a1.
    W = p2 q1 - p1 q2 = -g1 (independent of z)."""
    p2 = (z - a1) * (z - a0) - g1
    p1 = z - a0
    q1 = Fr(1)
    q2 = z - a1
    return p2 * q1 - p1 * q2


# ---------- f64 HB / YY ----------
def degree_balance(xp, yn, d0):
    n_X = min(int(d0), len(xp) - 1)
    n_Y = len(yn) - 1
    return n_X, n_Y


def J_n(a, b, n):
    J = np.diag(np.asarray(a[:n], float))
    if n > 1:
        bb = np.asarray(b[:n - 1], float)
        J = J + np.diag(bb, 1) + np.diag(bb, -1)
    return J


def zeros_A(a, b, n):
    """Gauss zeros of p_n = eigenvalues of the n x n Jacobi."""
    return np.sort(np.linalg.eigvalsh(J_n(a, b, n)))


def zeros_B(a, b, n):
    """Zeros of q_n (second kind) = trailing Jacobi n-1."""
    if n <= 1:
        return np.array([])
    return np.sort(np.linalg.eigvalsh(J_n(a[1:], b[1:], n - 1)))


def interlacing_ok(zA, zB, tol=HB_TOL):
    zA = np.sort(np.asarray(zA, float))
    zB = np.sort(np.asarray(zB, float))
    if len(zB) == 0:
        return True, 0.0, 0
    if len(zA) != len(zB) + 1:
        return False, 99.0, 99
    viol = 0
    gaps = []
    n = len(zB)
    for i in range(n):
        g = min(zB[i] - zA[i], zA[i + 1] - zB[i])
        gaps.append(g)
        if g < -tol:
            viol += 1
    return viol == 0, (float(min(gaps)) if gaps else 0.0), viol


def merge_yy(zX, zY):
    """YY-adjacencies in the merged sorted zeros.  The
    basis-free Ruecklauf counter: one mode <=> yy <= 1."""
    zX = np.sort(np.asarray(zX, float))
    zY = np.sort(np.asarray(zY, float))
    tagged = ([(float(x), "X") for x in zX]
              + [(float(y), "Y") for y in zY])
    tagged.sort(key=lambda u: u[0])
    yy = xx = 0
    yy_int = []
    prev = None
    for t, lab in tagged:
        if prev is not None:
            if lab == prev[1] == "Y":
                yy += 1
                yy_int.append((prev[0], t))
            if lab == prev[1] == "X":
                xx += 1
        prev = (t, lab)
    if yy_int:
        best = max(yy_int, key=lambda r: r[1] - r[0])
        tmid = 0.5 * (best[0] + best[1])
    else:
        tmid = float("nan")
    return yy, xx, tmid


def hb_of(x, w, n):
    """SOURCE-PURE HB pair of a positive discrete measure
    at degree n: Jacobi -> (p_n, q_n) zeros.  No T0, no R."""
    a, b, h0 = V.mu_chain(x, w, n)
    zA = zeros_A(a, b, n)
    zB = zeros_B(a, b, n)
    ok, gap, viol = interlacing_ok(zA, zB)
    return dict(a=a, b=b, h0=h0, zA=zA, zB=zB, ok=ok,
                gap=gap, viol=viol, n=n)


def hb_pair(xp, wX, yn, wY, d0):
    """E_X, E_Y and the two YY counters.  Constructor:
    nodes and u^vee-weights only."""
    n_X, n_Y = degree_balance(xp, yn, d0)
    X = hb_of(xp, wX, n_X)
    Y = hb_of(yn, wY, n_Y)
    yyA, xxA, tmidA = merge_yy(X["zA"], yn)
    nS = min(n_X, n_Y)
    zXs = X["zA"] if n_X == nS else hb_of(xp, wX, nS)["zA"]
    yyS, xxS, tmidS = merge_yy(zXs, Y["zA"])
    return dict(n_X=n_X, n_Y=n_Y, X=X, Y=Y,
                yyA=yyA, xxA=xxA, tmidA=tmidA,
                yyS=yyS, xxS=xxS, tmidS=tmidS)


def stieltjes_m(x, w, z):
    x = np.asarray(x, float)
    w = np.asarray(w, float)
    return complex(np.sum(w / (x - z)))


def pack_row(mz):
    """HB pair plus the r409 T0 readout (measurement, not
    a constructor of E_X / E_Y)."""
    xp, wX, yn, wY, _ud = B.dual_split(mz)
    d0 = int(mz["Nw"]) - 3
    hb = hb_pair(xp, wX, yn, wY, d0)
    g = B.pack_graph(mz)
    _U, _s, Vt = np.linalg.svd(g["T0"], full_matrices=False)
    y_peak = float(yn[int(np.argmax(np.abs(Vt[0])))])
    span = float(xp.max() - xp.min()) + 1e-30
    loc = (abs(hb["tmidA"] - y_peak) / span
           if np.isfinite(hb["tmidA"]) else 1.0)
    z_test = 0.3 + 0.7j
    mX = stieltjes_m(xp, wX, z_test)
    mY = stieltjes_m(yn, wY, z_test)
    hb.update(dict(
        d0=d0, nX=len(xp), nY=len(yn), xp=xp, yn=yn,
        wX=wX, wY=wY, nnegT=g["nneg"], op=g["opnorm"],
        y_peak=y_peak, loc=loc,
        imX=float(mX.imag), imY=float(mY.imag),
    ))
    return hb


# ---------- parts ----------
def part_satz():
    section("S1  LEG A -- HB / WRONSKIAN OVER Q + TOY")
    a0, a1, g1, h0, h1 = monic_X_Q()
    w0 = wronskian_Q(a0, a1, g1, Fr(0))
    w1 = wronskian_Q(a0, a1, g1, Fr(1))
    w2 = wronskian_Q(a0, a1, g1, Fr(-3, 5))
    check("G01-wronskian-constant-Q",
          w0 == w1 == w2 == -g1 and g1 > 0,
          "W=-gamma_1=%s at z=0,1,-3/5" % (-g1,))
    disc = (a0 - a1) * (a0 - a1) + Fr(4) * g1
    check("G02-interlacing-disc-Q",
          disc > 0 and g1 > 0,
          "disc(p2)=%s > 0; q2-zero=a1 sits in (z-,z+) "
          "because p2(a1)=-gamma_1<0" % disc)
    xs, _u, ud, _iX, iY, d0 = B.toy_dual()
    yn = [xs[i] for i in iY]
    wY = [ud[i] for i in iY]
    hY = sum(wY)
    aY = sum(w * y for w, y in zip(wY, yn)) / hY
    check("G03-Y-degree-q-minus-1-Q",
          len(yn) == 2 and aY != 0 and d0 == 3,
          "Y: q=2, n_Y=1, mean=%s (HB of degree 1, B constant)"
          % aY)
    xp = np.array([float(xs[i]) for i in _iX])
    wX = np.array([float(ud[i]) for i in _iX])
    yn_f = np.array([float(y) for y in yn])
    wY_f = np.array([float(w) for w in wY])
    toy = hb_pair(xp, wX, yn_f, wY_f, d0)
    check("G04-toy-HB-both",
          toy["X"]["ok"] and toy["Y"]["ok"]
          and toy["n_X"] == 2 and toy["n_Y"] == 1,
          "toy n_X=%d n_Y=%d HB X/Y=%s/%s yyA=%d"
          % (toy["n_X"], toy["n_Y"], toy["X"]["ok"],
             toy["Y"]["ok"], toy["yyA"]))


def part_w9():
    section("S2  LEG B -- w9 PHASE INDEX (PRIMARY TEST)")
    mz = V.build_measures(9)
    d = pack_row(mz)
    check("G10-degree-balance-w9",
          d["nX"] == W9_X and d["nY"] == W9_Y
          and d["d0"] == W9_D0 and d["n_X"] == W9_NX
          and d["n_Y"] == W9_NY
          and d["n_X"] == d["d0"] < d["nX"] - 1,
          "|X|=%d |Y|=%d d0=%d n_X=%d=d0 < |X|-1; n_Y=%d=q-1"
          % (d["nX"], d["nY"], d["d0"], d["n_X"], d["n_Y"]))
    check("G11-HB-interlacing-w9",
          d["X"]["ok"] and d["Y"]["ok"]
          and d["X"]["viol"] == 0 and d["Y"]["viol"] == 0,
          "X gap=%.3e Y gap=%.3e (positive Jacobi => HB)"
          % (d["X"]["gap"], d["Y"]["gap"]))
    check("G12-herglotz-both-measures",
          d["imX"] > HOLD_IM and d["imY"] > HOLD_IM
          and d["nnegT"] == 1
          and abs(d["op"] - W9_OP) <= 1e-8,
          "Im m_X=%.3e Im m_Y=%.3e > 0 at 0.3+0.7i; "
          "nnegT=%d ||T||=%.6f -- full-measure Uvarov path "
          "is index 0 and cannot see the interpolant defect"
          % (d["imX"], d["imY"], d["nnegT"], d["op"]))
    check("G13-w9-yyA-not-at-most-one",
          d["yyA"] == W9_YYA and d["yyA"] > 1,
          "yyA=%d (Gauss_X(d0) vs Y-atoms) -- PRIMARY FAIL: "
          "not <= 1 winding.  PHASE_DOMINANCE_REFUTED on "
          "flagship MAIN" % d["yyA"])
    check("G14-w9-same-degree-yyS",
          d["yyS"] == W9_YYS and d["yyS"] > 5,
          "yyS=%d (equal-dimension Gauss_X(q-1) vs Gauss_Y) "
          ">> 1 -- the dim-matched control also fails"
          % d["yyS"])
    check("G15-index-mismatch-nneg",
          d["nnegT"] == 1 and d["yyA"] != d["nnegT"],
          "nneg(I-T*T)=%d != yyA=%d -- the HB phase counter "
          "is NOT the Potapov index of T0" % (d["nnegT"], d["yyA"]))
    check("G16-loc-not-a-law",
          d["loc"] <= W9_LOC_HI,
          "w9 loc=%.3f (YY-interval vs T0-SV); MAIN range "
          "is [0.059, 1.000] -- not a walking defect coordinate"
          % d["loc"])
    return d


def part_kills(w9):
    section("S3  KILLS -- PERMUTE / SCRAMBLE / MUTANT")
    dP = pack_row(P1.reweight(V.build_measures(9), "permute", 1000))
    dS = pack_row(HM.scramble_mz())
    check("G20-kill-permute-not-many-YY",
          dP["yyA"] == PERM_YYA and dP["nnegT"] >= PERM_NNEG_LO
          and dP["yyA"] <= YYA_MED + 1,
          "PERM yyA=%d (MAIN median %d) nnegT=%d -- the "
          "world-separator does NOT fire on the phase counter"
          % (dP["yyA"], YYA_MED, dP["nnegT"]))
    check("G21-kill-scramble",
          dS["yyA"] == SCR_YYA and dS["nnegT"] == SCR_NNEG
          and dS["yyA"] != dS["nnegT"]
          and dS["X"]["ok"] and dS["Y"]["ok"],
          "SCR yyA=%d != nnegT=%d (elevated vs MAIN, still "
          "not the operator index); HB still holds"
          % (dS["yyA"], dS["nnegT"]))
    zA = w9["X"]["zA"]
    ok_mut, _g, viol = interlacing_ok(zA, zA)
    check("G22-mutant-B-equals-A",
          (not ok_mut) and viol > 0,
          "B:=p_n (not q_n): interlacing FAILS viol=%d -- "
          "second kind is load-bearing for the HB pair"
          % viol)
    dL = pack_row(HM.chi_mz(9, DMF.Q_CHI3, DMF.LPQ3))
    dD = pack_row(HM.chi_mz(15, DMF.Q_CHI3, DMF.LPQ3))
    check("G23-chi-death-not-phase-overflow",
          dL["nnegT"] == 0 and dD["nnegT"] == 1
          and dL["yyA"] >= dD["yyA"]
          and dL["X"]["ok"] and dD["X"]["ok"],
          "live-9 yyA=%d nnegT=%d; dead-15 yyA=%d nnegT=%d "
          "-- death is NOT more Ruecklaeufe (bulk phase "
          "does not carry the edge)"
          % (dL["yyA"], dL["nnegT"], dD["yyA"], dD["nnegT"]))
    return dP, dS


def part_census(smoke):
    section("S4  CENSUS -- MAIN 42 + living chi 78 + dead chi 6")
    if smoke:
        section("S4b  core/chi skipped (--smoke)")
        return
    core = list(V.admissible_indices())
    rec = []
    n_hb = 0
    for kz in core:
        d = pack_row(V.build_measures(kz))
        rec.append(d)
        n_hb += int(d["X"]["ok"] and d["Y"]["ok"])
    yya = [d["yyA"] for d in rec]
    nneg = [d["nnegT"] for d in rec]
    loc = [d["loc"] for d in rec]
    p1 = [d for d in rec if d["op"] > 1.0 + 1e-9]
    pd = [d for d in rec if d["op"] <= 1.0 + 1e-9]
    le1 = sum(1 for d in p1 if d["yyA"] <= 1)
    pd0 = sum(1 for d in pd if d["yyA"] == 0)
    corr = float(np.corrcoef(yya, nneg)[0, 1])
    check("G30-main42-HB",
          n_hb == CORE_N and len(rec) == CORE_N,
          "HB interlacing %d/%d (classical, gated)"
          % (n_hb, CORE_N))
    check("G31-main-P1-yyA-le1-rare",
          len(p1) == P1_N and le1 == P1_LE1
          and min(yya) == 0 and max(yya) == YYA_MAX
          and YYA_MED - 1 <= float(np.median(yya)) <= YYA_MED + 1,
          "P1 yyA<=1 only %d/%d; yyA min/med/max %d/%.0f/%d"
          % (le1, len(p1), min(yya), float(np.median(yya)), max(yya)))
    check("G32-main-PD-yyA-zero-rare",
          len(pd) == PD_N and pd0 == PD_ZERO,
          "PD yyA==0 only %d/%d -- PD is not the 0-Ruecklauf "
          "world (the counter is not P1)" % (pd0, len(pd)))
    check("G33-yyA-uncorrelated-with-nneg",
          corr <= CORR_HI
          and min(loc) <= 0.08 and max(loc) >= 0.6,
          "corr(yyA,nnegT)=%.3f; loc in [%.3f, %.3f] -- "
          "neither a dictionary nor a walking coordinate"
          % (corr, min(loc), max(loc)))
    live, dead = [], []
    for q, lpq, deadset in ((DMF.Q_CHI3, DMF.LPQ3, HM.DEAD_CHI3),
                            (DMF.Q_CHI4, DMF.LPQ4, HM.DEAD_CHI4)):
        for kz in core:
            mz = HM.chi_mz(kz, q, lpq)
            if mz is None:
                continue
            d = pack_row(mz)
            (dead if kz in deadset else live).append(d["yyA"])
    check("G34-chi-live-dead",
          len(live) == CHI_LIVE and len(dead) == CHI_DEAD
          and CHI_LIVE_MED - 1 <= float(np.median(live)) <= CHI_LIVE_MED + 1
          and CHI_DEAD_MED - 1 <= float(np.median(dead)) <= CHI_DEAD_MED + 1
          and max(live) == CHI_LIVE_MAX
          and max(dead) == CHI_DEAD_MAX
          and float(np.median(dead)) < float(np.median(live)),
          "live %d yyA med %.0f max %d; dead %d yyA med %.0f "
          "max %d -- death is fewer, not more, Ruecklaeufe"
          % (len(live), float(np.median(live)), max(live),
             len(dead), float(np.median(dead)), max(dead)))


def main():
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke

    print("=" * 78)
    print("debranges_index_probe -- "
          "PRIME.RDAGGER.DEBRANGES_CONTINUATION.01 (round 416)")
    print("SPEC_SHA %s   (B %s / DI %s / HM %s / P1 %s)"
          % (SPEC_SHA[:16], B.SPEC_SHA[:16], DI.SPEC_SHA[:16],
             HM.SPEC_SHA[:16], P1.SPEC_SHA[:16]))
    print("mode: %s" % ("SMOKE" if smoke else
                        "FULL (core-42 + chi3-42 + chi4-42)"))
    print("=" * 78)

    section("S0  FIREWALL + IMPORT SHA + CONSTRUCTOR AUDIT")
    okf, det = firewall_audit()
    check("G00-firewall", okf, det)
    sha_ok = (B.SPEC_SHA.startswith(B_SHA_PREFIX)
              and DI.SPEC_SHA.startswith(DI_SHA_PREFIX)
              and HM.SPEC_SHA.startswith(HM_SHA_PREFIX)
              and P1.SPEC_SHA.startswith(P1_SHA_PREFIX))
    check("G00b-import-sha", sha_ok,
          "B %s / DI %s / HM %s / P1 %s"
          % (B.SPEC_SHA[:8], DI.SPEC_SHA[:8],
             HM.SPEC_SHA[:8], P1.SPEC_SHA[:8]))
    ag = antigate_fragment_audit()
    check("G00c-no-fit", not ag,
          "no fit primitives" if not ag else "; ".join(ag))
    leak = scope_audit("hb_pair") + scope_audit("hb_of")
    check("G00d-constructor-no-T0-target",
          leak == [],
          "hb_of / hb_pair clean (Jacobi of (x,w) only)"
          if not leak else "; ".join(leak))

    part_satz()
    w9 = part_w9()
    part_kills(w9)
    part_census(smoke)

    section("S5  VERDICT")
    prev_ok = all(ok for _n, ok in CHECKS)
    check("G40-verdict",
          prev_ok,
          "PHASE_DOMINANCE_REFUTED / HB_CENSUS: HB SATZ; "
          "yyA=3 on flagship MAIN (not <=1); permute does "
          "not inflate the phase counter; T0-index stays "
          "r409 nneg(I-TT).  no RH / L* / R-dagger")

    n_fail = sum(1 for _n, ok in CHECKS if not ok)
    n_ok = len(CHECKS) - n_fail
    verd = "PHASE_DOMINANCE_REFUTED / HB_CENSUS"
    print("\nRESULT: %d/%d gates PASS   SPEC_SHA %s   (%.1fs)  %s" % (
        n_ok, len(CHECKS), SPEC_SHA[:16], time.time() - T0, verd))
    if n_fail == 0:
        print("DEBRANGES INDEX %sVERIFIED" % ("SMOKE " if smoke else ""))
        return 0
    print("DEBRANGES INDEX FAILED %d" % n_fail)
    return 1


if __name__ == "__main__":
    sys.exit(main())
