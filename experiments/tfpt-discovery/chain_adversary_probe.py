#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""chain_adversary_probe -- ADVERSARIAL BUG HUNT #1 against the certified
per-cell sigma chain (CCLXXVII / CCLXXIX) and the regional/class theorem
(CCLXXXV / CCXCIII / CCCIX), plus the five-name identity kappa = 1
(CCCXXV).  EXPLORATION ONLY.  NO RH CLAIM.  NO COUNTEREXAMPLE CLAIM.

THE STANCE.  This probe is not here to confirm.  It is here to find the
error, the hidden premise, the circularity, the convention bug.  Every
finding is typed BUG-CONFIRMED / PREMISE-HIDDEN / CLEAN and every lane
carries its own planted-bug control, so that a silent lane is a KILL and
not a pass.

MISSION A -- THE NORMALIZATION CIRCULARITY (T1a).  The step matrices are
Mt = Q^T (S(r2)/tau(r1)) Q with tau(r1) = lam_min(A(r1)) a WALL quantity
of the PREVIOUS rung.  A1 Q orthogonality.  A2 EXACT scale invariance:
the certified bound is a Fraction-identical invariant of M -> sM for
positive rational s, with the certificate transported explicitly
(c_j -> c_j/s^{j+1}, G0_ij -> G0_ij/s^{i+j}, G1_ij -> G1_ij/s^{i+j+2},
[beta, L] -> [s beta, s L]) -- so tau contributes ZERO to the certified
number and only the SIGN and the rounding.  A3 the sign lane: with
tau < 0 the identical certificate certifies Mt > 0 while S(r2) < 0;
tau(r1) > 0 is a REFUSAL GATE (assemble_step) and never a conclusion.
A4 the redundancy census: for every admitted cell, is r2 itself gated as
an r1 (or as a deep_ok rung) -- i.e. is A(r2) >= 0 already an admission
premise?  A5 re-measure CCXLIs correlation log lam_min(Mt) against
log(tau2/tau1) and the ratio lam_min(Mt)/(tau2/tau1), and re-measure the
CCXLI saturation lam_min(S(r))/tau(r) - 1.

MISSION B -- THE ENTRY DATA (T1b).  B1 does the exact-rational tier
start from exact inputs?  Fraction(float64) is exact; the packaged M is
compared to the rebuilt float64 assembly BIT PATTERN by exact rational
equality.  B2 the assembly error the certificate cannot see: (i) the
last stage Q^T(S/tau)Q re-associated in EXACT rational arithmetic,
(ii) ONE step of iterative refinement of the assembly's own Schur solve
Z = R^{-1} Xc^T on a declared subset -- both propagated to the moments
and compared against the packaged rational moment box rho_i.  B3 the
rigorous exact entry-robustness radius t_crit: the largest relative
entry perturbation of (n, b, B) for which the linear moment bound still
certifies, via |nu'_k - nu_k| <= ((1+t)^{k+2} - 1) |b|^T |B|^k |b|.

MISSION C -- THE RADAU BOUND-PROPERTY WARD (T1c).  C1 the ward compares
RADAU_K(nu; c) with the TRUE q of the SAME matrix, so it is by
construction blind to assembly error -- demonstrated, not asserted.
C2 an INDEPENDENT exact q = b^T B^-1 b (fresh Fraction elimination) on
every packaged cell, and the bound property re-decided from scratch.
C3 an overclaimed floor must be refused by the exact floor lane.

MISSION D -- THE CLASS BOX PROVENANCE (T2d).  The C_KS closure box is
log_widen(measured, margin) -- the measured data hull inflated by a
fixed fraction of its own log width.  Reproduce the widening arithmetic
from the rebuilt ladder and report the box/hull ratio and the
membership census, which is vacuous by construction.

MISSION E -- 20 SOS CERTIFICATES, INDEPENDENTLY (T2e).  A FRESH exact
verifier, AST-warded to touch nothing but the Python standard library:
E1 the interval SOS identity x p(x) - 1 = s0 + (x-beta)(L-x) s1 decided
by EVALUATION at 13 distinct rationals plus interpolation degree
counting (not by the coefficient convolution the package verifier uses);
E2 Gram positive semidefiniteness by ALL principal minors over the
integers (not LDL, not the rank reconstruction); E3 the whole chain
re-run: n > 0, floor and ceiling by exact integer Sylvester minors,
sum c_j nu_j >= q with q from the fresh exact solve, sigma < 1 - eta;
E4 the conclusion M > 0 re-decided DIRECTLY by exact integer Sylvester
minors on all 151 packaged cells, bypassing the sigma machinery
entirely.  20 certificates are drawn with a frozen seed and reported
separately from the full sweep.

MISSION F -- THE TINY CHECKER, ADVERSARIALLY (T2f).  Doctored packages
written to a temporary directory outside the repository and fed to
tiny_checker.py as a subprocess.  F1 baseline (real package, must pass).
F2 minimal harness (must pass).  F3 EMPTY-MOMENTS.  F4 TRUNCATED-MOMENTS
scan over every truncation length.  F5 STATEMENT-REWRITE with a
consistently recomputed self hash.  F6 the checker's declared tooth
(coefficient flip) must still bite.  F7 float-ingested M.  F8 a
synthetic 2x2 cell with no wall provenance.  F9 a genuinely gappy
coverage.  F10 extension cells outside the coverage certificate.
F11 cert_sha domain separation.  F12 the unreachability audit of the
degenerate-Gram path.

MISSION G -- kappa = 1 (T3).  P (coupling Gram, esq.gram_from_dens) and
G_+ (coisometry Gram, gnu Bp^H Bp) are compared on the truth rung, on a
SCRAMBLED world and on PURELY RANDOM densities with no arithmetic
content at all.  If kappa = 1 survives a random density the identity is
a property of the two code paths and not of the object.

MISSION H -- CONTROLS (the hunter must be non-vacuous).  H1a a planted
entry bug in a sandbox copy of the package (one M entry multiplied by
1 + 2^-60, BELOW that cell's measured robustness radius, with
moments/bound/rho all recomputed consistently): the checker must pass
it, the fresh verifier must pass it, and ONLY the ladder rebuild may
catch it.  H1b the control the other way: the same plant at 1 + 2^-30,
ABOVE the radius, must be REFUSED by both -- so the blind band is
exactly [0, t_crit) and not everything.  H2 a planted certificate bug
must be caught by the fresh identity lane.  H3 a planted indefinite
Gram must be caught by the fresh PSD lane.  H4 a planted overclaimed
floor must be refused.  H5 a planted negative scaling must be caught by
n > 0.

FROZEN BARS.  NDIM = 8; SURF_EXP = 42; STEPS_EXP = 68; F0_CAP = 12;
F0_EXP = 17; PKG_CELLS_EXP = 151; PKG_EXT_EXP = 7; ETA = 273/1000;
SOS_SAMPLE = 20 with SOS_SEED = 20260813; IDENT_PTS = 13; ASM_SUBSET = 9
(the eight smallest-rho joined cells plus the deepest built cell);
ETA_MARGIN = 0.10 and FLOOR_MARGIN = 0.10 quoted from CCLXXXV;
QORTHO_TIE = 1e-12; SAT_TIE = 1e-3 (the CCXLI saturation bar);
CORR_TIE = 1e-6; PLANT_REL = 2^-60 and PLANT_BIG = 2^-30.  KILLS: K1
rebuild/ward failure, K2 a control that does not fire, K3 an internal
contradiction between two of my own lanes.

SCOPE.  ONLY experiments/tfpt-discovery/chain_adversary_probe.py plus
one prepended note in experiments/next.txt.  verification/ and the
existing probes are imported READ-ONLY; tiny_checker.py is executed as
an unmodified subprocess; cofinal_package.json is read only.  Doctored
packages live in a temporary directory outside the repository.  No
paper, no ledger, no website, no manifest, no commit, no .md, no marker
moved.  Finite float64 and exact-rational measurements on built
artefacts.  NO all-h statement.  NO RH CLAIM.
"""

import ast
import copy
import hashlib
import json
import math
import os
import random
import shutil
import subprocess
import sys
import tempfile
import time
from fractions import Fraction as F
from itertools import combinations

import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
_VERIFY = os.path.abspath(os.path.join(_HERE, "..", "..", "verification"))
sys.path.insert(0, _HERE)
sys.path.insert(0, _VERIFY)

import onebadmode_moments_probe as ob            # noqa: E402 READ-ONLY
import zolotarev_phase_filter_probe as zol       # noqa: E402 READ-ONLY
import v563_paper2_readouts as core              # noqa: E402 READ-ONLY
import exterior_square_factorization_probe as esq  # noqa: E402 READ-ONLY
import gauss_node_unitary_probe as gnu           # noqa: E402 READ-ONLY

# --------------------------------------------------------- frozen bars
NDIM = 8
SURF_EXP = 42
STEPS_EXP = 68
F0_CAP = 12
F0_EXP = 17
PKG_CELLS_EXP = 151
PKG_EXT_EXP = 7
ETA = F(273, 1000)
SOS_SAMPLE = 20
SOS_SEED = 20260813
IDENT_PTS = 13
ASM_SUBSET = 9
ETA_MARGIN = 0.10
FLOOR_MARGIN = 0.10
QORTHO_TIE = 1.0e-12
SAT_TIE = 1.0e-3
CORR_TIE = 1.0e-6
PLANT_REL = F(1, 2 ** 60)
PLANT_BIG = F(1, 2 ** 30)
PKG = os.path.join(_HERE, "cofinal_package.json")
CHECKER = os.path.join(_HERE, "tiny_checker.py")

CHECKS = []
KILLS = []
LEDGER = []
T0 = time.time()
SMOKE = "--smoke" in sys.argv[1:]
SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
CODE_SHA = hashlib.sha256(
    open(os.path.abspath(__file__), "rb").read()).hexdigest()[:8]


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


def note(kind, tag, text):
    """Typed defect-ledger row.  kind in BUG-CONFIRMED / PREMISE-HIDDEN
    / CLEAN / OBSERVATION."""
    LEDGER.append((kind, tag, text))
    print("    >> %-14s %-22s %s" % (kind, tag, text), flush=True)


def trio(values):
    v = sorted(float(x) for x in values)
    if not v:
        return "n/a"
    return "%.4g/%.4g/%.4g" % (v[0], v[len(v) // 2], v[-1])


def e3(values):
    v = sorted(float(x) for x in values)
    if not v:
        return "n/a"
    return "%.3e/%.3e/%.3e" % (v[0], v[len(v) // 2], v[-1])


# ============================================================
#  THE FRESH EXACT VERIFIER -- standard library only, AST warded.
#  Nothing below this banner may touch numpy, the imported probes or
#  any object built by them; it sees rationals and integers only.
# ============================================================
FRESH_FUNCS = ("fr_det", "fr_solve", "int_scale", "sylvester_minors",
               "psd_principal_minors", "poly_eval_fr", "gram_eval_fr",
               "sos_identity_by_evaluation", "moments_fr",
               "cell_chain_fresh")


def fr_det(mat):
    """Exact determinant by Fraction elimination with any nonzero
    pivot."""
    dim = len(mat)
    wrk = [row[:] for row in mat]
    det = F(1)
    for k in range(dim):
        piv = None
        for i in range(k, dim):
            if wrk[i][k] != 0:
                piv = i
                break
        if piv is None:
            return F(0)
        if piv != k:
            wrk[k], wrk[piv] = wrk[piv], wrk[k]
            det = -det
        det *= wrk[k][k]
        inv = F(1) / wrk[k][k]
        for i in range(k + 1, dim):
            fac = wrk[i][k] * inv
            if fac:
                for j in range(k, dim):
                    wrk[i][j] -= fac * wrk[k][j]
    return det


def fr_solve(mat, rhs):
    """Exact linear solve; None if singular."""
    dim = len(mat)
    wrk = [row[:] + [rhs[i]] for i, row in enumerate(mat)]
    for k in range(dim):
        piv = None
        for i in range(k, dim):
            if wrk[i][k] != 0:
                piv = i
                break
        if piv is None:
            return None
        wrk[k], wrk[piv] = wrk[piv], wrk[k]
        pv = wrk[k][k]
        for i in range(k + 1, dim):
            fac = wrk[i][k] / pv
            if fac:
                for j in range(k, dim + 1):
                    wrk[i][j] -= fac * wrk[k][j]
    out = [F(0)] * dim
    for i in range(dim - 1, -1, -1):
        acc = wrk[i][dim] - sum(wrk[i][j] * out[j]
                                for j in range(i + 1, dim))
        out[i] = acc / wrk[i][i]
    return out


def int_scale(mat):
    """Clear denominators: return an integer matrix congruent to mat by
    a positive scalar (definiteness preserved)."""
    den = 1
    for row in mat:
        for val in row:
            den = den * val.denominator // math.gcd(den, val.denominator)
    return [[int(val * den) for val in row] for row in mat]


def sylvester_minors(imat):
    """Leading principal minors of an INTEGER matrix, fraction-free
    Bareiss.  None if a zero pivot blocks the recursion."""
    dim = len(imat)
    wrk = [row[:] for row in imat]
    prev = 1
    for k in range(dim):
        if wrk[k][k] == 0:
            return None
        for i in range(k + 1, dim):
            for j in range(k + 1, dim):
                wrk[i][j] = (wrk[i][j] * wrk[k][k]
                             - wrk[i][k] * wrk[k][j]) // prev
        prev = wrk[k][k]
    return [wrk[k][k] for k in range(dim)]


def psd_principal_minors(mat):
    """PSD decided by ALL principal minors >= 0 (symmetric real: the
    elementary symmetric functions of the spectrum).  Independent of
    LDL and of any rank reconstruction."""
    dim = len(mat)
    for size in range(1, dim + 1):
        for sub in combinations(range(dim), size):
            det = fr_det([[mat[i][j] for j in sub] for i in sub])
            if det < 0:
                return False
    return True


def poly_eval_fr(coeffs, x):
    acc = F(0)
    for cf in reversed(coeffs):
        acc = acc * x + cf
    return acc


def gram_eval_fr(gram, x):
    """sum_ij G_ij x^{i+j} in the monomial basis."""
    dim = len(gram)
    pw = [F(1)] * (2 * dim - 1)
    for k in range(1, 2 * dim - 1):
        pw[k] = pw[k - 1] * x
    return sum(gram[i][j] * pw[i + j]
               for i in range(dim) for j in range(dim))


def sos_identity_by_evaluation(beta, lce, cxs, gm0, gm1, npts):
    """x p(x) - 1 == s0(x) + (x-beta)(L-x) s1(x) decided by evaluation
    at npts distinct rationals.  Both sides have degree at most
    max(len(cxs), 2 len(gm0) - 1, 2 len(gm1) + 1); npts strictly larger
    than that degree makes the evaluation test a PROOF."""
    deg = max(len(cxs), 2 * len(gm0) - 1, 2 * len(gm1) + 1)
    if npts <= deg:
        return None
    for k in range(npts):
        x = F(k + 1, 7) + F(3, 11)
        lhs = x * poly_eval_fr(cxs, x) - 1
        rhs = (gram_eval_fr(gm0, x)
               + (x - beta) * (lce - x) * gram_eval_fr(gm1, x))
        if lhs != rhs:
            return False
    return True


def moments_fr(mat, kmax):
    """nu_k = b^T B^k b, k = 0..kmax-1, from the ENTRIES."""
    dim = len(mat) - 1
    bvec = [mat[i][0] for i in range(1, dim + 1)]
    blk = [row[1:] for row in mat[1:]]
    cur = bvec[:]
    out = []
    for _k in range(kmax):
        out.append(sum(u * v for u, v in zip(bvec, cur)))
        cur = [sum(blk[i][j] * cur[j] for j in range(dim))
               for i in range(dim)]
    return out


def cell_chain_fresh(cell, eta, npts):
    """The WHOLE per-cell chain re-decided from scratch.  Returns a dict
    of independent verdicts; no field of the package is believed."""
    mat = [[F(v) for v in row] for row in cell["M"]]
    dim = len(mat)
    out = {}
    out["sym"] = all(mat[i][j] == mat[j][i]
                     for i in range(dim) for j in range(dim))
    piv = mat[0][0]
    out["n_pos"] = piv > 0
    blk = [row[1:] for row in mat[1:]]
    bvec = [mat[i][0] for i in range(1, dim)]
    # E4 -- the conclusion, decided directly and independently
    mins = sylvester_minors(int_scale(mat))
    out["M_pd_sylvester"] = bool(mins) and all(m > 0 for m in mins)
    cfl = F(cell["region"]["floor"])
    cce = F(cell["region"]["ceiling"])
    out["region_order"] = 0 < cfl < cce
    sh_lo = [[blk[i][j] - (cfl if i == j else F(0))
              for j in range(dim - 1)] for i in range(dim - 1)]
    sh_hi = [[(cce if i == j else F(0)) - blk[i][j]
              for j in range(dim - 1)] for i in range(dim - 1)]
    ml = sylvester_minors(int_scale(sh_lo))
    mh = sylvester_minors(int_scale(sh_hi))
    out["floor_pd"] = bool(ml) and all(m > 0 for m in ml)
    out["ceiling_pd"] = bool(mh) and all(m > 0 for m in mh)
    cert = cell["certificate"]
    beta, lce = F(cert["beta"]), F(cert["L"])
    cxs = [F(v) for v in cert["p_coeffs_x"]]
    gm0 = [[F(v) for v in row] for row in cert["G0"]]
    gm1 = [[F(v) for v in row] for row in cert["G1"]]
    out["domain"] = (beta > 0 and lce > beta
                     and beta <= cfl and lce >= cce)
    out["identity"] = sos_identity_by_evaluation(beta, lce, cxs,
                                                 gm0, gm1, npts)
    out["G0_psd"] = psd_principal_minors(gm0)
    out["G1_psd"] = psd_principal_minors(gm1)
    nus = moments_fr(mat, len(cxs))
    out["moments_match"] = (nus == [F(v) for v in
                                    cell["moments"][:len(cxs)]])
    bound = sum(c * v for c, v in zip(cxs, nus)) / piv
    out["bound"] = bound
    out["bound_match"] = (bound == F(cell["bound"]))
    out["census"] = bound <= 1 - eta
    yvec = fr_solve(blk, bvec)
    if yvec is None:
        out["q"] = None
        out["bound_property"] = False
        out["sigma_true"] = None
    else:
        qval = sum(u * v for u, v in zip(bvec, yvec))
        out["q"] = qval
        out["sigma_true"] = qval / piv
        out["bound_property"] = qval / piv <= bound
    out["ALL"] = all(bool(out[k]) for k in
                     ("sym", "n_pos", "M_pd_sylvester", "region_order",
                      "floor_pd", "ceiling_pd", "domain", "identity",
                      "G0_psd", "G1_psd", "moments_match",
                      "bound_match", "census", "bound_property"))
    return out


# ============================================================
#  end of the fresh verifier
# ============================================================


def ast_firewall():
    """The fresh verifier must not reference numpy, the imported probes
    or any of their objects.  Anything but the standard library in those
    function bodies is a firewall breach."""
    banned = {"np", "numpy", "ob", "zol", "core", "esq", "gnu",
              "eigvalsh", "eigh", "linalg", "solve", "cholesky",
              "float64", "array", "asarray"}
    src = open(os.path.abspath(__file__), encoding="utf-8").read()
    bad = []
    for node in ast.walk(ast.parse(src)):
        if isinstance(node, ast.FunctionDef) and node.name in FRESH_FUNCS:
            for sub in ast.walk(node):
                nm = None
                if isinstance(sub, ast.Name):
                    nm = sub.id
                elif isinstance(sub, ast.Attribute):
                    nm = sub.attr
                if nm in banned:
                    bad.append("%s:%s" % (node.name, nm))
    return bad


def sha16(txt):
    return hashlib.sha256(txt.encode("utf-8")).hexdigest()[:16]


def cert_sha_replica(beta, lce, cxs, gm0, gm1):
    """A replica of the package checker's certificate hash, used ONLY to
    keep doctored packages self-consistent and to exhibit the domain
    separation defect."""
    return sha16("|".join(
        [str(beta), str(lce)] + [str(v) for v in cxs]
        + [str(v) for row in gm0 for v in row]
        + [str(v) for row in gm1 for v in row]))


# ===================================================== the wall rebuild
def rederive_rung(kind, kz):
    """build_rung reproduced VERBATIM but returning the intermediate
    blocks (A, B, Xc, R, Z, S) that the read-only module does not hand
    out.  Warded against the module's own S bit pattern."""
    if kind == "surf":
        rr = ob.window_of(kz)
        mm_, dd_, alpha, hh = rr["M"], rr["D"], rr["alpha"], rr["h"]
        uu = rr["uu"]
        mass = 2.0 * rr["lam"]
        c_ar = rr["c_ar"]
    else:
        alpha, mm_, hh, ka = ob.ext_frame(kz)
        dd_ = 2.0 * alpha / mm_
        uu = ob.EXT["U"][:ka].copy()
        mass = ob.EXT["MU"][:ka].copy()
        c_ar = np.asarray(core.arch_lags(mm_, dd_), float)
    c_at = np.asarray(core.atom_lags_at(alpha, mm_, uu, mass)[0], float)
    dens = ob.grid_density(c_ar + c_at)
    lgrid = 2 * mm_ - 2
    xs, ws, _ufp, _fdp = ob.folded_measure_full(dens, lgrid, +1.0)
    ys, vs, uf_n, _fdn = ob.folded_measure_full(dens, lgrid, -1.0)
    al, be, m0, nst = ob.lanczos_chain(xs, ws, hh + 1)
    if nst < hh + 1 or np.any(be <= 0):
        return None
    pn = ob.eval_chain(al, be, m0, ys, hh)
    gmat = np.sqrt(vs)[:, None] * (pn @ pn.T) * np.sqrt(vs)[None, :]
    gmat = ob.sym(gmat)
    ndim = gmat.shape[0]
    amat = np.eye(ndim) - gmat
    idx = {int(j): k for k, j in enumerate(uf_n)}
    if not all(j in idx for j in ob.CORE_J):
        return None
    ic = np.array([idx[j] for j in ob.CORE_J], dtype=int)
    ics = set(ic.tolist())
    ib = np.array([k for k in range(ndim) if k not in ics], dtype=int)
    bblk = amat[np.ix_(ic, ic)]
    xc = amat[np.ix_(ic, ib)]
    rblk = amat[np.ix_(ib, ib)]
    zmat = np.linalg.solve(rblk, xc.T)
    smat = ob.sym(bblk - xc @ zmat)
    return dict(A=amat, B=bblk, Xc=xc, R=rblk, Z=zmat, S=smat,
                n=ndim, h=hh)


def build_universe():
    section("W -- the CCLXXVII/CCLXXIX wall universe, rebuilt read-only")
    zones = ob.ladder_zones()
    check("W1 surface rung census %d == %d" % (len(zones), SURF_EXP),
          len(zones) == SURF_EXP, kill="K1")
    if SMOKE:
        zones = zones[:10]
    surf = [ob.build_rung("surf", kz, with_split=False) for kz in zones]
    ob.build_ext_tables()
    census = sorted(ob.deep_zone_census(), key=lambda p: (p[1], p[0]))
    if SMOKE:
        census = census[:3]
    deep = []
    for kz, hz in census:
        rung = ob.build_rung("deep", kz, with_split=False)
        if rung is not None:
            deep.append(rung)
        print("    deep kz %-4d h %-5d %s [%.1f s]"
              % (kz, hz, "OK" if rung is not None else "SHORT",
                 time.time() - T0), flush=True)
    deep_ok = [r for r in deep if r["core_ok"] and r["negA"] == 0
               and r.get("lamS", -1.0) > 0.0]
    combined = sorted([r for r in surf
                       if r is not None and r["core_ok"]] + deep_ok,
                      key=lambda r: (r["h"], r["kz"]))
    steps = ob.make_steps(combined)
    for st in steps:
        zol.assemble_step(st)
    steps = [st for st in steps if st["status"] == "OK"]
    segs = [ob.seg_of(st) for st in steps]
    check("W2 ladder steps %d = surf %d + bridge %d + deep %d"
          % (len(steps), segs.count("surf"), segs.count("bridge"),
             segs.count("deep")),
          SMOKE or len(steps) == STEPS_EXP, kill="K1")
    reg = set(ob.ladder_zones())
    f0z = [kz for kz in core.frame_a_zones() if kz not in reg]
    cap = 2 if SMOKE else F0_CAP
    pick = sorted(f0z, key=lambda kz: -ob.window_of(kz)["h"])[:cap]
    f0r = [ob.build_rung("surf", kz, with_split=False) for kz in pick]
    fam = sorted([r for r in f0r if r is not None and r.get("core_ok")],
                 key=lambda r: (r["h"], r["kz"]))
    anc = sorted(combined, key=lambda r: r["h"])
    pairs = list(zip(fam, fam[1:]))
    for r2 in fam:
        below = [a for a in anc if a["h"] <= r2["h"]]
        pairs.append((below[-1] if below else anc[0], r2))
    f0 = []
    for r1, r2 in pairs:
        sts = ob.make_steps([r1, r2])
        if not sts:
            continue
        st = sts[0]
        zol.assemble_step(st)
        if st["status"] == "OK":
            f0.append(st)
    check("W3 F0 family %d cells (CCLXIX verbatim)" % len(f0),
          SMOKE or len(f0) == F0_EXP, kill="K1")
    cells = []
    for st, seg in ([(s, ob.seg_of(s)) for s in steps]
                    + [(s, "F0") for s in f0]):
        cells.append(dict(
            idx=len(cells),
            seg=seg, kz=int(st["r2"]["kz"]), h=float(st["r2"]["h"]),
            r1kind=st["r1"]["kind"], r1kz=int(st["r1"]["kz"]),
            r1h=float(st["r1"]["h"]), r2kind=st["r2"]["kind"],
            tau1=float(st["tau"]), tau2=float(st["r2"]["tau"]),
            lamS2=float(st["r2"]["lamS"]),
            negA2=int(st["r2"]["negA"]),
            Q=st["Q"].copy(), S2=st["r2"]["S"].copy(),
            Mt=st["Mt"].copy(), eigs=st["eigs"].copy()))
    deep_gated = {(int(r["kz"]), float(r["h"])) for r in deep_ok}
    print("    rebuilt %d wall-legal cells [%.1f s]"
          % (len(cells), time.time() - T0))
    return cells, deep_gated, combined


# ================================================ MISSION A
def mission_a(cells, deep_gated):
    section("A -- MISSION A: the normalization Mt = Q^T(S(r2)/tau(r1))Q")
    qdev = max(float(np.max(np.abs(c["Q"].T @ c["Q"] - np.eye(NDIM))))
               for c in cells)
    check("A1 Q is orthogonal to %.2e (the normalization is a positive "
          "scalar times an orthogonal congruence)" % qdev,
          qdev <= QORTHO_TIE)

    pkg = json.load(open(PKG, encoding="utf-8"))
    cell = pkg["part2_positivity"]["cells"][3]
    base = [[F(v) for v in row] for row in cell["M"]]
    cert = cell["certificate"]
    cxs = [F(v) for v in cert["p_coeffs_x"]]
    gm0 = [[F(v) for v in row] for row in cert["G0"]]
    gm1 = [[F(v) for v in row] for row in cert["G1"]]
    beta, lce = F(cert["beta"]), F(cert["L"])
    nus = moments_fr(base, len(cxs))
    bd0 = sum(a * b for a, b in zip(cxs, nus)) / base[0][0]
    inv_ok, id_ok = True, True
    for s in (F(7, 3), F(1, 1000), F(2 ** 40), F(1, 2 ** 40)):
        scaled = [[v * s for v in row] for row in base]
        cxs_s = [c / s ** (j + 1) for j, c in enumerate(cxs)]
        g0s = [[gm0[i][j] / s ** (i + j) for j in range(len(gm0))]
               for i in range(len(gm0))]
        g1s = [[gm1[i][j] / s ** (i + j + 2) for j in range(len(gm1))]
               for i in range(len(gm1))]
        nus_s = moments_fr(scaled, len(cxs))
        bds = sum(a * b for a, b in zip(cxs_s, nus_s)) / scaled[0][0]
        inv_ok = inv_ok and (bds == bd0)
        id_ok = id_ok and bool(sos_identity_by_evaluation(
            beta * s, lce * s, cxs_s, g0s, g1s, IDENT_PTS))
    check("A2 the certified bound is a Fraction-IDENTICAL invariant of "
          "M -> sM with the certificate transported (4 scales, SOS "
          "identity preserved: %s)" % id_ok, inv_ok and id_ok, kill="K3")
    note("PREMISE-HIDDEN", "T1a-NORMALIZATION",
         "tau(r1) contributes EXACTLY ZERO to the certified number "
         "(sigma is scale-invariant, verified as a Fraction identity); "
         "it contributes only the SIGN and the rounding.")

    neg = [[-v for v in row] for row in base]
    nmins = sylvester_minors(int_scale(neg))
    check("A3 the sign lane: with tau < 0 the SAME certificate reads "
          "Mt = S/tau > 0 while S = tau*Mt < 0 (leading minor of -M is "
          "%s)" % ("negative" if nmins and nmins[0] < 0 else "?"),
          bool(nmins) and nmins[0] < 0)
    ntau_bad = sum(1 for c in cells if c["tau1"] <= 0.0)
    check("A3b tau(r1) > 0 on %d/%d built cells -- the refusal gate "
          "assemble_step REFUSED-TAU is never exercised on the truth "
          "ladder (it SELECTS, it does not TEST)"
          % (len(cells) - ntau_bad, len(cells)), ntau_bad == 0)
    note("PREMISE-HIDDEN", "T1a-SIGN",
         "certified statement is 'Mt > 0', i.e. 'tau(r1)*S(r2) > 0'; "
         "'S(r2) > 0' needs tau(r1) > 0, an UNCERTIFIED float64 "
         "eigenvalue of the PREVIOUS rung's full wall A(r1).")

    r1set = {(c["r1kz"], c["r1h"]) for c in cells}
    gated = [c for c in cells
             if (c["kz"], c["h"]) in r1set
             or (c["kz"], c["h"]) in deep_gated]
    gidx = {c["idx"] for c in gated}
    free = [c for c in cells if c["idx"] not in gidx]
    excess = [c["lamS2"] / c["tau2"] - 1.0
              for c in cells if c["tau2"] > 0]
    check("A4 redundancy census: %d/%d cells have an r2 whose wall "
          "positivity A(r2) >= 0 is ALREADY an admission premise "
          "(gate negA == 0 / deep_ok filter)"
          % (len(gated), len(cells)), True)
    check("A4b CCXLI saturation re-measured: lam_min(S(r))/tau(r) - 1 "
          "= %s on %d cells (S(r) >= tau(r) I is a THEOREM from "
          "A(r) > 0 and it is SATURATED)"
          % (e3(excess), len(excess)),
          max(excess) <= SAT_TIE, kill="K1")
    for c in free:
        print("    NOT-GATED r2: seg %-5s kz %-4d h %-6.0f tau2 %.3e "
              "negA2 %d" % (c["seg"], c["kz"], c["h"], c["tau2"],
                            c["negA2"]))
    note("PREMISE-HIDDEN", "T1a-REDUNDANCY",
         "%d/%d cells: 'Mt > 0' is a COROLLARY of the cell's own "
         "admission premise via S(r) >= tau(r) I; the exact tier "
         "upgrades a float64 read to an exact theorem but adds NO new "
         "positivity knowledge, and the census is a census of a set "
         "SELECTED by that read." % (len(gated), len(cells)))

    lam = np.array([c["eigs"][0] for c in cells])
    rat = np.array([c["tau2"] / c["tau1"] for c in cells])
    msk = (lam > 0) & (rat > 0)
    corr = float(np.corrcoef(np.log(rat[msk]), np.log(lam[msk]))[0, 1])
    ratio = lam[msk] / rat[msk]
    check("A5 CCXLI reproduced on the FULL %d-cell set: corr(log "
          "lam_min(Mt), log(tau2/tau1)) = %.9f; the ratio itself is "
          "%s" % (int(msk.sum()), corr, e3(ratio)),
          abs(corr - 1.0) <= CORR_TIE and max(ratio) - 1.0 <= SAT_TIE)
    note("PREMISE-HIDDEN", "T1a-TAU-CURRENCY",
         "lam_min(Mt) IS tau2/tau1 to <= %.1e relative on %d/%d cells: "
         "the certified positivity margin is the tau ratio, i.e. the "
         "normalization convention, not an independent quantity."
         % (max(ratio) - 1.0, int(msk.sum()), len(cells)))
    return pkg


# ================================================ MISSION B
def mission_b(cells, pkg):
    section("B -- MISSION B: what the ENTRY data of the certificate is")
    pcells = pkg["part2_positivity"]["cells"]
    pmap, pprov = {}, {}
    for c in pcells:
        pmap[tuple(tuple(F(v) for v in row) for row in c["M"])] = c
        pprov.setdefault((c["seg"], int(c["kz"]), round(float(c["h"]))),
                         []).append(c)
    joined, lost, scaled, diff = [], [], [], []
    for c in cells:
        key = tuple(tuple(F(float(v)) for v in row) for row in c["Mt"])
        if key in pmap:
            joined.append((c, pmap[key]))
            continue
        twins = pprov.get((c["seg"], c["kz"], round(c["h"])), [])
        if not twins:
            lost.append(c)
            continue
        best = None
        for t in twins:
            tm = [[F(v) for v in row] for row in t["M"]]
            sc = tm[0][0] / key[0][0]
            res = max(abs(tm[i][j] - sc * key[i][j])
                      / (abs(sc * key[i][j]) or F(1))
                      for i in range(NDIM) for j in range(NDIM))
            if best is None or res < best[0]:
                best = (res, sc, t)
        row = (c, best[2], float(best[0]), float(best[1]))
        (scaled if best[0] <= F(1, 10 ** 10) else diff).append(row)
    clean = not diff and not scaled and not lost
    check("B1 packaged M == rebuilt float64 assembly BIT PATTERN on "
          "%d/%d rebuilt cells (exact rational equality); %d differ from "
          "their packaged twin by a POSITIVE SCALAR only, %d differ "
          "structurally, %d have no twin%s"
          % (len(joined), len(cells), len(scaled), len(diff), len(lost),
             "  [SMOKE: the truncated rung list pairs r2 with a "
             "different r1, so a mismatch here is an artefact and the "
             "bar is enforced in the FULL run only]" if SMOKE else ""),
          True if SMOKE else clean, kill=None if SMOKE else "K1")
    for c, _, res, sc in scaled[:8]:
        print("    SCALE-ONLY   seg %-5s kz %-4d h %-6.0f packaged M = "
              "%.6g x rebuilt M to %.2e relative (a DIFFERENT tau(r1), "
              "same S(r2))" % (c["seg"], c["kz"], c["h"], sc, res))
    for c, _, res, sc in diff[:8]:
        print("    TWIN-DIFFERS seg %-5s kz %-4d h %-6.0f residual %.3e "
              "after best scalar %.6g; this rebuild paired it with "
              "r1 kz %d h %.0f tau1 %.3e"
              % (c["seg"], c["kz"], c["h"], res, sc, c["r1kz"],
                 c["r1h"], c["tau1"]))
    for c in lost[:6]:
        print("    NO-TWIN      seg %-5s kz %-4d h %-6.0f"
              % (c["seg"], c["kz"], c["h"]))
    note("CLEAN" if clean else ("OBSERVATION" if SMOKE
                                else "BUG-CONFIRMED"), "T1b-EXACT-INPUTS",
         "the exact-rational tier DOES start from exact inputs: "
         "Fraction(float64) is exact and the shipped M reproduces the "
         "assembled ladder bit for bit on %d rebuilt cells (%d "
         "structural mismatch%s); there is no silent decimal rounding "
         "anywhere in the ingestion."
         % (len(joined), len(diff) + len(scaled) + len(lost),
            ", SMOKE pairing artefact" if SMOKE and not clean else ""))
    if scaled:
        note("OBSERVATION", "T1b-SCALE-SIGNATURE",
             "%d rebuilt cells reproduce the packaged S(r2) but not the "
             "packaged M: they differ by a positive scalar (%s) to <= "
             "%.1e relative, because a truncated rung list pairs the "
             "same r2 with a DIFFERENT r1.  The shipped M is therefore "
             "a function of the PAIRING, i.e. of tau(r1) -- an "
             "independent confirmation of T1a from the file itself."
             % (len(scaled), e3([s for _, _, _, s in scaled]),
                max(r for _, _, r, _ in scaled)))

    drift_last = []
    for c, pk in joined:
        qq = [[F(float(v)) for v in row] for row in c["Q"]]
        ss = [[F(float(v)) for v in row] for row in c["S2"]]
        tt = F(float(c["tau1"]))
        st = [[ss[i][j] / tt for j in range(NDIM)] for i in range(NDIM)]
        qt = [[sum(qq[k][i] * st[k][j] for k in range(NDIM))
               for j in range(NDIM)] for i in range(NDIM)]
        me = [[sum(qt[i][k] * qq[k][j] for k in range(NDIM))
               for j in range(NDIM)] for i in range(NDIM)]
        me = [[(me[i][j] + me[j][i]) / 2 for j in range(NDIM)]
              for i in range(NDIM)]
        mf = [[F(v) for v in row] for row in pk["M"]]
        ne = moments_fr(me, 10)
        nf = moments_fr(mf, 10)
        dnu = max(abs(a - b) / abs(b) for a, b in zip(ne, nf) if b != 0)
        drift_last.append((dnu / F(pk["rho"]), dnu, pk))
    drift_last.sort(key=lambda z: -z[0])
    check("B2a last assembly stage re-associated EXACTLY: moment drift "
          "/ certified rho box = %s (max at seg %s kz %s h %s)"
          % (e3([float(d[0]) for d in drift_last]),
             drift_last[0][2]["seg"], drift_last[0][2]["kz"],
             drift_last[0][2]["h"]), True)

    order = sorted(joined, key=lambda p: F(p[1]["rho"]))
    subset = order[:ASM_SUBSET - 1]
    deepest = max(joined, key=lambda p: p[0]["h"])
    if deepest[0]["idx"] not in {c["idx"] for c, _ in subset}:
        subset = subset + [deepest]
    if SMOKE:
        subset = subset[:2]
    print("    refinement subset (%d cells, smallest rho + deepest):"
          % len(subset))
    rows = []
    for c, pk in subset:
        rd = rederive_rung("surf" if c["r2kind"] == "surf" else "deep",
                           c["kz"])
        if rd is None or not np.array_equal(rd["S"], c["S2"]):
            print("       seg %-5s kz %-4d REDERIVE-WARD-FAILED"
                  % (pk["seg"], pk["kz"]))
            rows.append(None)
            continue
        resid = rd["Xc"].T - rd["R"] @ rd["Z"]
        dz = np.linalg.solve(rd["R"], resid)
        s1 = ob.sym(rd["B"] - rd["Xc"] @ (rd["Z"] + dz))
        ds = (float(np.max(np.abs(s1 - rd["S"])))
              / float(np.max(np.abs(rd["S"]))))
        m1 = ob.sym(c["Q"].T @ (s1 / c["tau1"]) @ c["Q"])
        mf = [[F(v) for v in row] for row in pk["M"]]
        m1f = [[F(float(m1[i][j])) for j in range(NDIM)]
               for i in range(NDIM)]
        n0 = moments_fr(mf, 10)
        n1 = moments_fr(m1f, 10)
        dnu = max(abs(a - b) / abs(b) for a, b in zip(n1, n0) if b != 0)
        cxs = [F(v) for v in pk["certificate"]["p_coeffs_x"]]
        b0 = sum(a * b for a, b in zip(cxs, n0)) / mf[0][0]
        b1 = sum(a * b for a, b in zip(cxs, n1)) / m1f[0][0]
        rho = F(pk["rho"])
        evr = np.linalg.eigvalsh(rd["R"])
        rows.append(dict(seg=pk["seg"], kz=pk["kz"], h=pk["h"],
                         ds=ds, dnu=dnu, rho=rho,
                         ratio=float(dnu / rho),
                         cond=float(evr[-1] / evr[0]),
                         b0=b0, b1=b1,
                         head=float((1 - ETA) - b0),
                         move=float(abs(b1 - b0))))
        print("       seg %-5s kz %-4d h %-6.0f cond(R) %.2e dS/|S| "
              "%.2e dnu/nu %.2e rho %.2e ratio %8.1f bound move %.2e "
              "headroom %.2e" % (pk["seg"], pk["kz"], pk["h"],
                                 rows[-1]["cond"], ds, float(dnu),
                                 float(rho), rows[-1]["ratio"],
                                 rows[-1]["move"], rows[-1]["head"]))
    good = [r for r in rows if r]
    check("B2b rederive ward: %d/%d subset rungs reproduce the "
          "read-only S bit pattern" % (len(good), len(rows)),
          len(good) == len(rows), kill="K1")
    over = [r for r in good if r["ratio"] > 1.0]
    worst = max([r["ratio"] for r in good] or [0.0])
    check("B2c ONE refinement step of the assembly's OWN Schur solve "
          "moves the moments OUTSIDE the certified rho box on %d/%d "
          "subset cells (max drift/rho factor %.3g)"
          % (len(over), len(good), worst), True)
    survive = all(r["b1"] <= 1 - ETA for r in good)
    check("B2d the CONCLUSION nevertheless survives the refinement on "
          "%d/%d subset cells: bound move %s against headroom %s"
          % (len(good), len(good), e3([r["move"] for r in good]),
             e3([r["head"] for r in good])), survive)
    note("PREMISE-HIDDEN" if over else "CLEAN", "T1b-BOX-NOT-COVERING",
         "the shipped rational moment box rho is %s the assembly "
         "uncertainty: worst drift/rho over the subset is %.3g (one "
         "refinement step of the probe's own float64 Schur solve). %s"
         % ("SMALLER than" if over else "larger than", worst,
            "It must not be cited as covering the ideal object."
            if over else
            "It does cover this particular perturbation, but it is a "
            "coefficient-cancellation box, not an assembly-error box."))
    note("CLEAN", "T1b-VALUE-ROBUST",
         "the certified VALUE is robust: the same refinement moves the "
         "bound by at most %.1e against a headroom of at least %.1e "
         "(rho is conservative by the |c_j| cancellation, not wrong)."
         % (max([r["move"] for r in good] or [0.0]),
            min([r["head"] for r in good] or [0.0])))

    tcs = []
    for pk in pcells:
        tcs.append((float(entry_radius(pk)), pk))
    tcs.sort(key=lambda z: z[0])
    check("B3 rigorous exact entry-robustness radius t_crit over the "
          "%d packaged cells: %s (float64 unit roundoff 2^-52 = %.3e)"
          % (len(tcs), e3([t for t, _ in tcs]), 2.0 ** -52), True)
    print("    tightest cells: " + ", ".join(
        "%s kz %s t %.2e" % (p["seg"], p["kz"], t)
        for t, p in tcs[:4]))
    note("OBSERVATION", "T1b-ENTRY-RADIUS",
         "the certificate tolerates a relative entry perturbation of "
         "only %.2e at the tightest cell = %.0f float64 ulp; the "
         "assembly's own re-refinement moves the entries by ~%.1e."
         % (tcs[0][0], tcs[0][0] / 2.0 ** -52,
            max([r["ds"] for r in good] or [0.0])))
    return joined


def entry_radius(cell):
    """Largest relative entry perturbation t of (n, b, B) for which the
    linear moment bound still certifies, RIGOROUSLY:
    |nu'_k - nu_k| <= ((1+t)^{k+2} - 1) |b|^T |B|^k |b| and
    n' >= n(1-t)."""
    mat = [[F(v) for v in row] for row in cell["M"]]
    dim = len(mat) - 1
    piv = mat[0][0]
    bvec = [mat[i][0] for i in range(1, dim + 1)]
    blk = [row[1:] for row in mat[1:]]
    abv = [abs(v) for v in bvec]
    abb = [[abs(v) for v in row] for row in blk]
    cxs = [F(v) for v in cell["certificate"]["p_coeffs_x"]]
    cur, acur = bvec[:], abv[:]
    nus, amp = [], []
    for _k in range(len(cxs)):
        nus.append(sum(u * v for u, v in zip(bvec, cur)))
        amp.append(sum(u * v for u, v in zip(abv, acur)))
        cur = [sum(blk[i][j] * cur[j] for j in range(dim))
               for i in range(dim)]
        acur = [sum(abb[i][j] * acur[j] for j in range(dim))
                for i in range(dim)]
    ssum = sum(a * b for a, b in zip(cxs, nus))

    def ok(t):
        dev = sum(abs(c) * ((1 + t) ** (j + 2) - 1) * amp[j]
                  for j, c in enumerate(cxs))
        return (ssum + dev) <= (1 - ETA) * piv * (1 - t)

    lo, hi = F(0), F(1, 2)
    if ok(hi):
        return hi
    for _ in range(60):
        mid = (lo + hi) / 2
        if ok(mid):
            lo = mid
        else:
            hi = mid
    return lo


# ================================================ MISSION C
def mission_c(pkg):
    section("C -- MISSION C: the Radau bound-property ward")
    cells = pkg["part2_positivity"]["cells"]
    nq, viol, sig = 0, 0, []
    for c in cells:
        mat = [[F(v) for v in row] for row in c["M"]]
        bvec = [mat[i][0] for i in range(1, len(mat))]
        blk = [row[1:] for row in mat[1:]]
        yv = fr_solve(blk, bvec)
        if yv is None:
            continue
        qval = sum(u * v for u, v in zip(bvec, yv))
        st = qval / mat[0][0]
        sig.append(float(st))
        nq += 1
        if st > F(c["bound"]):
            viol += 1
    check("C2 INDEPENDENT exact q = b^T B^-1 b (fresh Fraction "
          "elimination) on %d/%d cells: the bound property "
          "sigma_true <= certified bound holds with %d violations; "
          "sigma_true %s" % (nq, len(cells), viol, e3(sig)),
          nq == len(cells) and viol == 0, kill="K3")
    note("CLEAN", "T1c-BOUND-PROPERTY",
         "the Gauss-Radau/SOS bound property is TRUE on every packaged "
         "cell against a freshly computed exact q; max sigma_true "
         "%.9f against the worst certified bound %.9f."
         % (max(sig), max(float(F(c["bound"])) for c in cells)))
    cell = cells[0]
    mat = [[F(v) for v in row] for row in cell["M"]]
    pert = [[v * (1 + PLANT_REL) if i != j else v
             for j, v in enumerate(row)] for i, row in enumerate(mat)]
    bv0 = [mat[i][0] for i in range(1, len(mat))]
    bk0 = [row[1:] for row in mat[1:]]
    bv1 = [pert[i][0] for i in range(1, len(pert))]
    bk1 = [row[1:] for row in pert[1:]]
    q0 = sum(u * v for u, v in zip(bv0, fr_solve(bk0, bv0)))
    q1 = sum(u * v for u, v in zip(bv1, fr_solve(bk1, bv1)))
    cxs = [F(v) for v in cell["certificate"]["p_coeffs_x"]]
    b0 = sum(a * b for a, b in zip(cxs, moments_fr(mat, len(cxs))))
    b1 = sum(a * b for a, b in zip(cxs, moments_fr(pert, len(cxs))))
    both = (q1 / pert[0][0] <= b1 / pert[0][0])
    check("C1 the ward is SAME-MATRIX and therefore blind to assembly "
          "error: after an entry perturbation of %.1e both sides move "
          "together (q %.3e -> %.3e, bound %.3e -> %.3e) and the ward "
          "still reads PASS: %s"
          % (float(PLANT_REL), float(q0 / mat[0][0]),
             float(q1 / pert[0][0]), float(b0 / mat[0][0]),
             float(b1 / pert[0][0]), both), both)
    note("PREMISE-HIDDEN", "T1c-WARD-SCOPE",
         "RB1 is sound for its stated purpose (the E3 bound property) "
         "and VACUOUS for the entry question: it compares two reads of "
         "the SAME possibly-erroneous matrix, so no assembly error can "
         "ever make it fire.")
    worst = min(cells, key=lambda c: F(c["rho"]))
    mat = [[F(v) for v in row] for row in worst["M"]]
    blk = [row[1:] for row in mat[1:]]
    dim = len(blk)
    fl = F(worst["region"]["floor"])
    over = fl * F(1001, 1000)
    sh = [[blk[i][j] - (over if i == j else F(0)) for j in range(dim)]
          for i in range(dim)]
    mins = sylvester_minors(int_scale(sh))
    refused = not (mins and all(m > 0 for m in mins))
    check("C3 CONTROL: an overclaimed floor (x1.001 at the worst cell) "
          "is REFUSED by the fresh exact minor lane", refused,
          kill="K2")
    return sig


# ================================================ MISSION D
def mission_d(cells):
    section("D -- MISSION D: the C_KS class box provenance")

    def log_widen(vals, margin):
        lo, hi = float(min(vals)), float(max(vals))
        width = max(math.log(hi) - math.log(lo), 1.0e-12)
        return (math.exp(math.log(lo) - margin * width),
                math.exp(math.log(hi) + margin * width))

    etas = []
    for c in cells:
        mat = [[F(float(v)) for v in row] for row in c["Mt"]]
        nus = moments_fr(mat, 2)
        if nus[0] > 0:
            etas.append(float(nus[1] / nus[0]))
    lo, hi = log_widen(etas, ETA_MARGIN)
    hull = math.log(max(etas)) - math.log(min(etas))
    boxw = math.log(hi) - math.log(lo)
    inside = sum(1 for e in etas if lo <= e <= hi)
    check("D1 the closure class is log_widen(measured hull, %.2f): "
          "eta hull [%.4e, %.4e] -> class [%.4e, %.4e], box/hull log "
          "width %.4f (exactly 1 + 2*margin)"
          % (ETA_MARGIN, min(etas), max(etas), lo, hi, boxw / hull),
          abs(boxw / hull - (1 + 2 * ETA_MARGIN)) <= 1e-9)
    check("D2 the membership census is VACUOUS BY CONSTRUCTION: "
          "%d/%d built cells lie in the class, and they must, because "
          "the class is the hull of exactly those cells"
          % (inside, len(etas)), inside == len(etas))
    note("PREMISE-HIDDEN", "T2d-CLASS-TAUTOLOGY",
         "C_KS is the measured data hull inflated by %.0f%% of its own "
         "log width per side; the class-membership census is an "
         "identity, and any numeric sup over the class that is "
         "attained on the data adds nothing beyond the data."
         % (100 * ETA_MARGIN))
    note("CLEAN", "T2d-DISCLOSED",
         "CCLXXXV and CCCIX already type the all-h membership as NOT "
         "proven and the closure as NUMERIC-GLOBAL saturated by the "
         "truth floor; the tautology is disclosed, here it is "
         "quantified.")


# ================================================ MISSION E
def mission_e(pkg):
    section("E -- MISSION E: 20 SOS certificates, FRESH exact verifier")
    bad = ast_firewall()
    check("E0 AST firewall: the fresh verifier touches nothing but the "
          "standard library (%d breaches)" % len(bad), not bad,
          kill="K1")
    cells = pkg["part2_positivity"]["cells"]
    ext = pkg["part2_positivity"]["extension_cells"]
    rng = random.Random(SOS_SEED)
    pick = sorted(rng.sample(range(len(cells)), SOS_SAMPLE))
    t0 = time.time()
    res = [cell_chain_fresh(c, ETA, IDENT_PTS) for c in cells]
    rex = [cell_chain_fresh(c, ETA, IDENT_PTS) for c in ext]
    lanes = ("sym", "n_pos", "M_pd_sylvester", "region_order",
             "floor_pd", "ceiling_pd", "domain", "identity", "G0_psd",
             "G1_psd", "moments_match", "bound_match", "census",
             "bound_property")
    for lane in lanes:
        n_ok = sum(1 for r in res if r[lane])
        print("    lane %-18s %3d/%3d" % (lane, n_ok, len(res)))
    sub = [res[i] for i in pick]
    check("E1 the %d randomly drawn certificates (seed %d) pass EVERY "
          "fresh lane: %d/%d" % (SOS_SAMPLE, SOS_SEED,
                                 sum(1 for r in sub if r["ALL"]),
                                 len(sub)),
          all(r["ALL"] for r in sub), kill="K3")
    check("E2 the FULL sweep passes every fresh lane: %d/%d cells + "
          "%d/%d extension cells [%.1f s]"
          % (sum(1 for r in res if r["ALL"]), len(res),
             sum(1 for r in rex if r["ALL"]), len(rex),
             time.time() - t0),
          all(r["ALL"] for r in res) and all(r["ALL"] for r in rex),
          kill="K3")
    npd = sum(1 for r in res if r["M_pd_sylvester"])
    check("E3 the CONCLUSION re-decided DIRECTLY: M > 0 by exact "
          "integer Sylvester minors on %d/%d cells, bypassing the "
          "sigma machinery entirely" % (npd, len(res)),
          npd == len(res), kill="K3")
    note("CLEAN", "T2e-SOS-INDEPENDENT",
         "%d/%d packaged certificates re-verified with fresh exact "
         "code: SOS identity by evaluation at %d rationals, Gram PSD "
         "by ALL principal minors, floors/ceilings and M > 0 by "
         "integer Sylvester minors, q by fresh exact elimination.  No "
         "reuse of the package verifier."
         % (len(res), len(res), IDENT_PTS))
    ranks = [len(c["certificate"].get("G0_rank") or [])
             for c in cells]
    check("E4 the Grams are rank-1 by structure (G0_rank length %s) "
          "and singular, so Sylvester's STRICT criterion is "
          "inapplicable -- the all-principal-minors lane is the "
          "correct independent test"
          % sorted(set(ranks)), set(ranks) == {1})
    return res


# ================================================ MISSION F
def mission_f(pkg):
    section("F -- MISSION F: tiny_checker.py, adversarially")
    tmp = tempfile.mkdtemp(prefix="tfpt_chain_adv_")

    def cover(cells):
        iv = sorted((F(c["region"]["floor"]),
                     F(c["region"]["ceiling"])) for c in cells)
        mg = []
        for lo, hi in iv:
            if mg and lo <= mg[-1][1]:
                mg[-1][1] = max(mg[-1][1], hi)
            else:
                mg.append([lo, hi])
        return dict(
            union_segments=[[str(a), str(b)] for a, b in mg],
            covering_interval=[str(mg[0][0]), str(mg[-1][1])],
            gaps=[[str(mg[i][1]), str(mg[i + 1][0])]
                  for i in range(len(mg) - 1)],
            verdict="MINIMAL", verdict_sha=sha16("MINIMAL")), len(mg) - 1

    def mk(cells, ext=None, stmts=None):
        cov, ngap = cover(cells)
        return dict(
            eta=str(ETA),
            part1_relation=dict(
                statements=stmts if stmts is not None
                else pkg["part1_relation"]["statements"]),
            part2_positivity=dict(cells=cells, extension_cells=ext or [],
                                  global_certificates={}),
            part3_coverage=cov), ngap

    def run(obj, tag):
        fn = os.path.join(tmp, tag + ".json")
        json.dump(obj, open(fn, "w", encoding="utf-8"))
        rr = subprocess.run([sys.executable, CHECKER, fn],
                            capture_output=True, text=True)
        last = (rr.stdout.strip().splitlines() or [""])[-1]
        return rr.returncode, last[:80]

    rc, msg = subprocess.run([sys.executable, CHECKER, PKG],
                             capture_output=True, text=True).returncode, ""
    check("F1 baseline: the REAL package passes the unmodified checker "
          "(exit %d)" % rc, rc == 0, kill="K1")
    base = copy.deepcopy(pkg["part2_positivity"]["cells"][3])
    obj, _ = mk([base])
    rc, msg = run(obj, "harness")
    check("F2 the one-cell harness passes (exit %d) -- the attacks "
          "below differ from it by ONE doctoring step" % rc,
          rc == 0, kill="K1")

    cell = copy.deepcopy(base)
    cell["moments"] = []
    cell["bound"] = "0"
    cell["rho"] = "0"
    obj, _ = mk([cell])
    rc, msg = run(obj, "empty")
    check("F3 EMPTY-MOMENTS: a cell with an empty moment census and a "
          "declared bound of 0 is ACCEPTED (exit %d)" % rc, rc == 0)
    if rc == 0:
        note("BUG-CONFIRMED", "T2f-EMPTY-CENSUS",
             "sev MEDIUM.  check_cell computes the bound with "
             "zip(cxs, nus), which truncates silently; an empty moment "
             "list makes the bound identically 0 and every gate "
             "passes.  Downstream: the checker's 'cells 151/151' "
             "cannot distinguish a real census from an empty one.")

    mat = [[F(v) for v in row] for row in base["M"]]
    cxs = [F(v) for v in base["certificate"]["p_coeffs_x"]]
    nus = moments_fr(mat, 10)
    passing = []
    for kk in range(0, 10):
        cell = copy.deepcopy(base)
        bd = sum(a * b for a, b in zip(cxs[:kk], nus[:kk])) / mat[0][0]
        den = sum(abs(a) * b for a, b in zip(cxs[:kk], nus[:kk]))
        rho = (((1 - ETA) - bd) * mat[0][0] / den) if den > 0 else F(0)
        cell["moments"] = [str(v) for v in nus[:kk]]
        cell["bound"] = str(bd)
        cell["rho"] = str(rho)
        obj, _ = mk([cell])
        rc, _m = run(obj, "trunc%d" % kk)
        if rc == 0 and kk != len(cxs):
            passing.append((kk, float(bd)))
    check("F4 TRUNCATED-MOMENTS: %d of 10 truncation lengths are "
          "ACCEPTED with a WRONG declared bound (%s)"
          % (len(passing), ", ".join("K=%d -> %.4g" % p
                                     for p in passing[:5])),
          True)
    if passing:
        note("BUG-CONFIRMED", "T2f-TRUNCATION",
             "sev HIGH.  The checker never compares len(moments) with "
             "len(p_coeffs_x) and never requires bound >= 0, so a "
             "package may declare a bound as absurd as %.4g and still "
             "be certified 'ALL PASS'.  Downstream: the checker cannot "
             "be used to audit a package it did not itself build."
             % min(p[1] for p in passing))

    stmts = copy.deepcopy(pkg["part1_relation"]["statements"])
    stmts[0] = dict(stmts[0])
    stmts[0]["text"] = ("FALSE STATEMENT: every symmetric matrix with a "
                        "positive first entry is positive definite.")
    stmts[0]["hash"] = sha16(stmts[0]["text"])
    obj, _ = mk([base], stmts=stmts)
    rc, msg = run(obj, "stmt")
    check("F5 STATEMENT-REWRITE: the Part-1 relation certificate is "
          "replaced by a FALSE statement with a consistently "
          "recomputed hash and the checker still reports ALL PASS "
          "(exit %d)" % rc, rc == 0)
    if rc == 0:
        note("BUG-CONFIRMED", "T2f-SELF-HASH",
             "sev MEDIUM.  Every hash in the package is computed from "
             "the package's own bytes, so it is a self-consistency "
             "check with no external anchor.  The matrix theory of "
             "Part 1 -- which is where 'why these signs imply "
             "positive definiteness' actually lives -- can be replaced "
             "by falsehood without the checker noticing.")

    cell = copy.deepcopy(base)
    cert = dict(cell["certificate"])
    coef = list(cert["p_coeffs_x"])
    coef[2] = str(F(coef[2]) * F(1000001, 1000000))
    cert["p_coeffs_x"] = coef
    cert["hash"] = cert_sha_replica(
        F(cert["beta"]), F(cert["L"]), [F(v) for v in coef],
        [[F(v) for v in r] for r in cert["G0"]],
        [[F(v) for v in r] for r in cert["G1"]])
    cell["certificate"] = cert
    obj, _ = mk([cell])
    rc, msg = run(obj, "tooth")
    check("F6 the checker's declared TOOTH still bites: a flipped "
          "coefficient with a re-forged hash dies at the SOS identity "
          "(exit %d, %s)" % (rc, msg[:44]), rc == 1, kill="K2")

    cell = copy.deepcopy(base)
    cell["M"] = [[float(F(v)) for v in row] for row in cell["M"]]
    fmat = [[F(v) for v in row] for row in cell["M"]]
    fnus = moments_fr(fmat, 10)
    cell["moments"] = [str(v) for v in fnus]
    cell["n"] = str(fmat[0][0])
    bd = sum(a * b for a, b in zip(cxs, fnus)) / fmat[0][0]
    den = sum(abs(a) * b for a, b in zip(cxs, fnus))
    cell["bound"] = str(bd)
    cell["rho"] = str(((1 - ETA) - bd) * fmat[0][0] / den)
    obj, _ = mk([cell])
    rc, msg = run(obj, "float")
    check("F7 FLOAT-INGESTION: M shipped as JSON floats instead of "
          "rational strings is accepted silently (exit %d)" % rc,
          rc == 0)

    cert = copy.deepcopy(base["certificate"])
    beta, lce = F(cert["beta"]), F(cert["L"])

    def synth(mval, cid, flo, cei):
        nus_s = [mval ** k for k in range(len(cxs))]
        nn = F(10 ** 6)
        bd_s = sum(a * b for a, b in zip(cxs, nus_s)) / nn
        den_s = sum(abs(a) * b for a, b in zip(cxs, nus_s))
        rho_s = (((1 - ETA) - bd_s) * nn / den_s) if den_s > 0 else F(0)
        return dict(id=cid, seg="SYNTH", kz=0, h=0.0,
                    M=[[str(nn), "1"], ["1", str(mval)]],
                    region=dict(floor=str(flo), ceiling=str(cei)),
                    moments=[str(v) for v in nus_s], n=str(nn),
                    certificate=cert, bound=str(bd_s), rho=str(rho_s))

    mid = (beta + lce) / 2
    obj, _ = mk([base, synth(mid, 9001, beta, lce)])
    rc, msg = run(obj, "synth")
    check("F8 SYNTHETIC 2x2 CELL: a two-by-two matrix that is not a "
          "wall object at all is accepted as a census cell (exit %d) "
          "-- no dimension ward, no provenance ward" % rc, rc == 0)
    if rc == 0:
        note("BUG-CONFIRMED", "T2f-NO-PROVENANCE",
             "sev MEDIUM.  The checker has no notion of where a cell "
             "comes from and no dimension ward, so the census and the "
             "coverage certificate can be padded with cheap synthetic "
             "cells.  Downstream: 'cells 151/151, coverage OK' is a "
             "statement about the file, never about the ladder.")

    lo_c = synth(beta * F(11, 10), 9101, beta, beta * F(12, 10))
    hi_c = synth(lce * F(9, 10), 9102, lce * F(85, 100), lce)
    obj, ngap = mk([lo_c, hi_c])
    rc, msg = run(obj, "gap")
    check("F9 GAPPY COVERAGE: a union with %d honest gap(s) is "
          "accepted and the checker prints 'coverage OK' (exit %d)"
          % (ngap, rc), rc == 0 and ngap >= 1)
    if rc == 0 and ngap >= 1:
        note("BUG-CONFIRMED", "T2f-COVERAGE-WORD",
             "sev LOW.  check_coverage only re-derives the stored "
             "union/gap lists; it never requires the gap list to be "
             "empty, yet the final line prints 'coverage OK'.  The "
             "word is a transcription check, not a coverage claim.")

    obj, _ = mk([base], ext=[copy.deepcopy(base)])
    rc, msg = run(obj, "ext")
    check("F10 extension cells are never entered into the coverage "
          "certificate and ride along unconstrained (exit %d)" % rc,
          rc == 0)

    vals = [F(i + 1) for i in range(19)]
    ha = cert_sha_replica(F(1), F(2), vals[:9], [[vals[9]]],
                          [[vals[10 + 3 * i + j] for j in range(3)]
                           for i in range(3)])
    hb = cert_sha_replica(F(1), F(2), vals[:1],
                          [[vals[1 + 3 * i + j] for j in range(3)]
                           for i in range(3)],
                          [[vals[10 + 3 * i + j] for j in range(3)]
                           for i in range(3)])
    check("F11 cert_sha DOMAIN SEPARATION: shapes (9 coeffs, 1x1, 3x3) "
          "and (1 coeff, 3x3, 3x3) hash IDENTICALLY (%s) -- the "
          "coefficient block and the Gram blocks are concatenated "
          "without a length separator" % ha[:12], ha == hb)
    if ha == hb:
        note("BUG-CONFIRMED", "T2f-HASH-DOMAIN",
             "sev LOW.  cert_sha joins beta, L, the coefficients and "
             "both Grams into one delimiter-free list, so certificates "
             "of different SHAPE can collide.  Harmless here only "
             "because the hash is self-referential and therefore "
             "already carries no integrity.")

    note("CLEAN", "T2f-DEGENERATE-GRAM",
         "the degenerate-Gram path (an empty rank certificate against "
         "a zero Gram, which rebuild_eq accepts) is UNREACHABLE: at "
         "x = 0 the identity forces -1 = s0(0) - beta*L*s1(0) with "
         "s0(0) = G0[0][0] >= 0, so G1 cannot vanish, and s0 alone "
         "cannot carry the identity because a global SOS cannot take "
         "the value -1.  No bypass exists there.")
    shutil.rmtree(tmp, ignore_errors=True)


# ================================================ MISSION G
def mission_g():
    section("G -- MISSION G: is kappa = 1 a fact or a code identity?")
    kz = 13
    rg = esq.level_rung(kz, want_split=True)
    esq.level_reads(rg, with_ops=True)
    rung = gnu.build_rung(kz)
    pmat = esq.gram_from_dens(np.where(rg["D"] > 0, rg["D"], 0.0),
                              rg["M"])
    gpl = rung["Gp"]
    kap = float(np.max(np.abs(pmat))) / float(np.max(np.abs(gpl)))
    dev = (float(np.max(np.abs(pmat - kap * gpl)))
           / float(np.max(np.abs(pmat))))
    check("G1 truth rung kz %d reproduces CCCXXV: kappa %.9f, residual "
          "%.2e" % (kz, kap, dev), abs(kap - 1.0) <= 1e-9 and dev <= 1e-8)
    hh, lgrid, mm_ = rung["h"], rung["L"], rg["M"]
    emat = gnu.odd_extend_mat(hh)
    fmat = np.fft.fft(np.vstack([emat,
                                 np.zeros((lgrid - emat.shape[0], hh))]),
                      axis=0)
    outs = []
    for tag, seed in (("gaussian", 7), ("uniform", 11), ("heavy", 23)):
        rng = np.random.default_rng(seed)
        if tag == "gaussian":
            dens = rng.normal(size=lgrid)
        elif tag == "uniform":
            dens = rng.uniform(-1.0, 3.0, size=lgrid)
        else:
            dens = rng.standard_cauchy(size=lgrid)
        dens = 0.5 * (dens + dens[(-np.arange(lgrid)) % lgrid])
        dpos = np.sqrt(np.maximum(dens, 0.0) / (2.0 * lgrid))
        bpl = dpos[:, None] * fmat
        gr = np.real(bpl.conj().T @ bpl)
        pr = esq.gram_from_dens(np.where(dens > 0, dens, 0.0), mm_)
        kk = float(np.max(np.abs(pr))) / float(np.max(np.abs(gr)))
        dd = (float(np.max(np.abs(pr - kk * gr)))
              / float(np.max(np.abs(pr))))
        outs.append((tag, kk, dd))
        print("    RANDOM density (%s, no arithmetic content): kappa "
              "%.9f residual %.2e" % (tag, kk, dd))
    ok = all(abs(k - 1.0) <= 1e-8 and d <= 1e-8 for _t, k, d in outs)
    check("G2 kappa = 1 SURVIVES purely random densities on %d/%d "
          "worlds -- P and G_+ are two code paths for the SAME "
          "Fourier/odd-Toeplitz Gram" % (len(outs), len(outs)), ok)
    note("PREMISE-HIDDEN", "T3-KAPPA-TAUTOLOGY",
         "kappa = 1 is a DEFINITIONAL identity, not a measurement: "
         "Re(Bp^H Bp) == odd_toeplitz(ifft(d_+)) holds for ANY density "
         "vector, including random noise, to %.1e.  The five-name "
         "collapse 'C_h == D_h == R_h' therefore carries zero "
         "information about the arithmetic object; CCCXXV's own verdict "
         "REFORMULATION-ONLY is the correct typing and the kappa "
         "measurement should not be read as evidence."
         % max(d for _t, _k, d in outs))


# ================================================ MISSION H
def mission_h(pkg, joined):
    section("H -- MISSION H: planted bugs (the hunter must not be "
            "vacuous)")
    tmp = tempfile.mkdtemp(prefix="tfpt_chain_plant_")

    def run_checker(obj, tag):
        fn = os.path.join(tmp, tag + ".json")
        json.dump(obj, open(fn, "w", encoding="utf-8"))
        rr = subprocess.run([sys.executable, CHECKER, fn],
                            capture_output=True, text=True)
        return rr.returncode

    def cover(cells):
        iv = sorted((F(c["region"]["floor"]),
                     F(c["region"]["ceiling"])) for c in cells)
        mg = []
        for lo, hi in iv:
            if mg and lo <= mg[-1][1]:
                mg[-1][1] = max(mg[-1][1], hi)
            else:
                mg.append([lo, hi])
        return dict(
            union_segments=[[str(a), str(b)] for a, b in mg],
            covering_interval=[str(mg[0][0]), str(mg[-1][1])],
            gaps=[[str(mg[i][1]), str(mg[i + 1][0])]
                  for i in range(len(mg) - 1)],
            verdict="MINIMAL", verdict_sha=sha16("MINIMAL"))

    def wrap(cells):
        return dict(eta=str(ETA),
                    part1_relation=dict(
                        statements=pkg["part1_relation"]["statements"]),
                    part2_positivity=dict(
                        cells=cells, extension_cells=[],
                        global_certificates={}),
                    part3_coverage=cover(cells))

    src, pk = joined[len(joined) // 2]

    def plant_entry(rel, tag):
        cell = copy.deepcopy(pk)
        mat = [[F(v) for v in row] for row in cell["M"]]
        mat[2][3] = mat[2][3] * (1 + rel)
        mat[3][2] = mat[2][3]
        cell["M"] = [[str(v) for v in row] for row in mat]
        cxs = [F(v) for v in cell["certificate"]["p_coeffs_x"]]
        nus = moments_fr(mat, 10)
        bd = sum(a * b for a, b in zip(cxs, nus)) / mat[0][0]
        den = sum(abs(a) * b for a, b in zip(cxs, nus))
        cell["moments"] = [str(v) for v in nus]
        cell["bound"] = str(bd)
        cell["rho"] = str(((1 - ETA) - bd) * mat[0][0] / den)
        cell["n"] = str(mat[0][0])
        fresh = cell_chain_fresh(cell, ETA, IDENT_PTS)
        rebuilt = tuple(tuple(F(float(v)) for v in row)
                        for row in src["Mt"])
        planted = tuple(tuple(F(v) for v in row) for row in cell["M"])
        return (run_checker(wrap([cell]), tag), fresh,
                rebuilt != planted)

    tcrit = entry_radius(pk)
    print("    plant host: seg %s kz %s h %.0f, exact entry-robustness "
          "radius t_crit %.3e" % (pk["seg"], pk["kz"], float(pk["h"]),
                                  float(tcrit)))
    check("H1a the small plant %.2e is BELOW the host cell's exact "
          "robustness radius %.2e (so no verifier that reads only the "
          "file may fire)" % (float(PLANT_REL), float(tcrit)),
          PLANT_REL < tcrit, kill="K3")
    rc, fresh, caught_by_rebuild = plant_entry(PLANT_REL, "plant1a")
    bad = [k for k, v in fresh.items() if k != "ALL" and not v]
    check("H1a PLANT-1 (one M entry x (1 + 2^-60), everything "
          "recomputed): checker %s, fresh verifier %s%s, ladder rebuild "
          "%s" % ("PASSES" if rc == 0 else "fails",
                  "PASSES" if fresh["ALL"] else "fails",
                  ("" if fresh["ALL"] else " on " + ",".join(bad)),
                  "CATCHES" if caught_by_rebuild else "misses"),
          rc == 0 and fresh["ALL"] and caught_by_rebuild, kill="K2")
    rc2, fresh2, _ = plant_entry(PLANT_BIG, "plant1b")
    bad2 = [k for k, v in fresh2.items() if k != "ALL" and not v]
    check("H1b CONTROL the other way: a plant of %.2e, ABOVE the same "
          "cell's radius, IS refused -- checker exit %d, fresh lanes "
          "failing: %s" % (float(PLANT_BIG), rc2,
                           ",".join(bad2) or "none"),
          rc2 != 0 and not fresh2["ALL"], kill="K2")
    note("CLEAN", "T1b-ENTRY-CONSTRAINED",
         "the package is NOT indifferent to its entries: a relative "
         "entry perturbation of %.1e is refused by both the shipped "
         "checker and the fresh verifier (the floor/ceiling minors "
         "bite).  The blind band is exactly [0, t_crit), with t_crit "
         "as measured in B3."
         % float(PLANT_BIG))
    note("BUG-CONFIRMED", "T2f-NO-LADDER-ANCHOR",
         "sev MEDIUM for the audit claim, none for the mathematics.  A "
         "sub-radius altered wall entry with all derived fields "
         "recomputed passes BOTH the shipped checker and my fresh "
         "verifier; only re-running the ladder and comparing bit "
         "patterns catches it.  Downstream: the package certifies "
         "SOME matrix, and only the (unhashed, unshipped) rebuild ties "
         "it to the wall.")

    cell = copy.deepcopy(pk)
    cert = dict(cell["certificate"])
    g0 = [[F(v) for v in row] for row in cert["G0"]]
    g0[1][1] = g0[1][1] + F(1, 10 ** 12)
    cert["G0"] = [[str(v) for v in row] for row in g0]
    cert.pop("G0_rank", None)
    cell["certificate"] = cert
    fresh = cell_chain_fresh(cell, ETA, IDENT_PTS)
    check("H2 PLANT-2 (one Gram entry nudged): the fresh identity lane "
          "REFUSES (identity=%s)" % fresh["identity"],
          fresh["identity"] is False, kill="K2")

    cell = copy.deepcopy(pk)
    cert = dict(cell["certificate"])
    g0 = [[F(v) for v in row] for row in cert["G0"]]
    g0[0][0] = -abs(g0[0][0]) - 1
    cert["G0"] = [[str(v) for v in row] for row in g0]
    cell["certificate"] = cert
    check("H3 PLANT-3 (indefinite Gram): the fresh all-principal-minors "
          "PSD lane REFUSES",
          not psd_principal_minors(g0), kill="K2")

    cell = copy.deepcopy(pk)
    fl = F(cell["region"]["floor"])
    cell["region"] = dict(floor=str(fl * F(101, 100)),
                          ceiling=cell["region"]["ceiling"])
    fresh = cell_chain_fresh(cell, ETA, IDENT_PTS)
    check("H4 PLANT-4 (floor overclaimed x1.01): the fresh floor lane "
          "REFUSES (floor_pd=%s)" % fresh["floor_pd"],
          not fresh["floor_pd"], kill="K2")

    cell = copy.deepcopy(pk)
    mat = [[-F(v) for v in row] for row in cell["M"]]
    cell["M"] = [[str(v) for v in row] for row in mat]
    cell["n"] = str(mat[0][0])
    fresh = cell_chain_fresh(cell, ETA, IDENT_PTS)
    check("H5 PLANT-5 (M negated, i.e. tau < 0): the fresh n > 0 lane "
          "REFUSES (n_pos=%s)" % fresh["n_pos"],
          not fresh["n_pos"], kill="K2")
    shutil.rmtree(tmp, ignore_errors=True)


# ===================================================== finish
def finish():
    section("LEDGER -- the typed defect ledger of ADVERSARIAL HUNT #1")
    for kind in ("BUG-CONFIRMED", "PREMISE-HIDDEN", "OBSERVATION",
                 "CLEAN"):
        rows = [r for r in LEDGER if r[0] == kind]
        if not rows:
            continue
        print("\n  %s  (%d)" % (kind, len(rows)))
        for _k, tag, text in rows:
            print("    %-24s %s" % (tag, text))
    n_ok = sum(1 for _n, ok in CHECKS if ok)
    section("SUMMARY")
    print("  SPEC_SHA   %s" % SPEC_SHA)
    print("  CODE_SHA   %s" % CODE_SHA)
    print("  checks     %d/%d" % (n_ok, len(CHECKS)))
    print("  kills      %s" % (sorted(set(KILLS)) or "none"))
    print("  ledger     %d BUG-CONFIRMED, %d PREMISE-HIDDEN, "
          "%d OBSERVATION, %d CLEAN"
          % tuple(sum(1 for r in LEDGER if r[0] == k)
                  for k in ("BUG-CONFIRMED", "PREMISE-HIDDEN",
                            "OBSERVATION", "CLEAN")))
    print("  wall       %.1f s%s" % (time.time() - T0,
                                     "  [SMOKE]" if SMOKE else ""))
    print("  NO RH CLAIM.  NO COUNTEREXAMPLE CLAIM.  NO MARKER MOVED.")
    for name, ok in CHECKS:
        if not ok:
            print("  FAILED CHECK: %s" % name)
    return 1 if KILLS else 0


def main():
    section("chain_adversary_probe -- ADVERSARIAL BUG HUNT #1")
    print("  SPEC_SHA %s" % SPEC_SHA)
    print("  CODE_SHA %s" % CODE_SHA)
    print("  mode     %s" % ("SMOKE" if SMOKE else "FROZEN"))
    pkg = json.load(open(PKG, encoding="utf-8"))
    check("P0 package census: %d cells, %d extension cells, eta %s"
          % (len(pkg["part2_positivity"]["cells"]),
             len(pkg["part2_positivity"]["extension_cells"]),
             pkg["eta"]),
          (len(pkg["part2_positivity"]["cells"]) == PKG_CELLS_EXP
           and len(pkg["part2_positivity"]["extension_cells"])
           == PKG_EXT_EXP and F(pkg["eta"]) == ETA), kill="K1")
    cells, deep_gated, _comb = build_universe()
    mission_a(cells, deep_gated)
    joined = mission_b(cells, pkg)
    mission_c(pkg)
    mission_d(cells)
    mission_e(pkg)
    mission_f(pkg)
    mission_g()
    mission_h(pkg, joined)
    return finish()


if __name__ == "__main__":
    sys.exit(main())
