#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""moving12_soft17_probe -- E8.MOVING12.SOFT17.01: the hypothesis
17 = 12 + 3 + 1 + 1, audited at SPACE level (projectors, principal
angles, characters), not by number-matching.

EXPLORATION ONLY (experiments/): no ledger row, no paper edit, no
.md, nothing outside experiments/.  NO RH claim.  Frozen (spec +
sha256) before running.

BACKGROUND (read-only): the family 3-cycle sigma splits the 15
nonzero register labels as 3 fixed classes + 4 free 3-orbits =
3 + 12 (exact, v845/finite_compiler); the softport analysis
measured a dimension-independent displacement structure of rank
~12 in the tau coordinate (softport_cauchy_probe, run-1 ranks
12/11/11/12/13 over a 3.9x dimension range) and the pole-port
backflow concentrates on n95 <= 17 coupled bulk modes
(pole_port_kappa_probe).  THE HYPOTHESIS: 12 displacement
generators = the 12 sigma-moved label channels; 3 fixed classes =
the static bulk; + 1 vacuum slot; + 1 pole port.

THE GENERICITY DANGER (pre-typed): 12 = 12 and 17 = 12 + 3 + 1 + 1
as NUMBERS is numerology; the audit must compare SPACES.  The
frozen bridge (the only deployed register -> grid map available):
the DIVISOR MODULAR FRAME -- label S with divisor d(S) (the
divisor-210 register, canonicity probe read-only; the moved/fixed
divisor SETS are chirality-independent, verified) maps to the bin
profile phi_d(j) = d^{-i tau_j / 2} (the KMS/modular frequency of
the deployed half-weight d^{-1/2}, redheffer design (b) phases);
the 17-frame = {vacuum d=1} + {3 fixed divisors 2, 105, 210} +
{12 moved divisors} + {pole profile P_j, closed form}.  If the
angles do NOT close, the honest verdict is the burial, typed.

FROZEN PROTOCOL (2026-08-08, frozen + SHA-hashed before first run):

 S1  REGISTER SIDE (exact, bit model; v845 conventions, the
     Construction-A regressions live in the canonicity probe
     read-only): sigma (f1,f2,f3,a) -> (f3,f1,f2,a); fixed nonzero
     = {A, F_Sigma, F_Sigma + A} (3), moved = 12 in exactly 4 free
     3-orbits; the label projectors on C^15: P_moved (12-dim),
     P_fixed (3-dim), exact; the C3 isotypic dimensions EXACT:
     C^15 = triv^7 + om^4 + ombar^4, moved sector = 4 x regular =
     (4, 4, 4), fixed sector = triv^3; the census divisor maps
     (both gauge classes (3,5,7,2) / (3,7,5,2)) give the SAME
     moved/fixed divisor sets; the identity 17 = 12 + 3 + 1 + 1.

 S2  MEASURED OBJECTS (pole_port/softport machinery imported
     read-only; rungs 9/12/13, displacement-rank series also at
     26/40): REGRESSIONS: lam1(Delta) at anchors == softport refs
     {1.675e-4, 7.647e-5, 7.824e-5} rel 1e-3; kappa_POLE(kz9) in
     [2.6, 2.8]; n95 <= 20 with the kz-9 value reported (the
     measured concentration behind the '17'); displacement
     rank@1e-3 in tau at kz9 in [11, 13] and non-growing over
     {9,12,13,26,40} (max <= min + 3).  Objects kept: U = leading
     left displacement vectors (neg bins), V = right (pos bins),
     the top-17 coupled bulk modes (coupling census ci from the
     exact Feshbach split), each transported to bin space by the
     deployed transform (Delta-coords -> h by G+^{-1/2}, then the
     plain odd-extension transform Fp; frozen choice, typed).

 S3  THE FRAME: the 17 bin profiles as above, each normalized;
     conditioning census (singular values of the 17-frame; the
     frame must be numerically independent, smin >= 1e-3).

 S4  PRINCIPAL ANGLES (the space test; angles via SVD of Qa* Qb):
     (b1) span(U) vs moved-frame restricted to neg bins;
     (b2) span(V) vs moved-frame restricted to pos bins;
     (c)  span(top-17 bulk bin profiles) vs span(17-frame);
     bars for IDENTIFIED (machine-level closure, frozen): max
     angle <= 1e-6 rad on (b1) AND (c).  Angles far from 0 =
     the honest burial, typed with the full tables.  CONTRAST
     controls: the foreign frame (quadruple {2,3,5,11}, frozen
     witness) and the scramble-load generators (seed 1, deployed
     softport convention) -- the truth-vs-control angle gap is
     the information census of the bridge (measured, typed; if
     truth and controls are indistinguishable AND far from 0 the
     bridge carries no displacement information -- typed).

 S5  CHARACTERS: sigma acts on the 12 moved divisors by the
     census 3-cycle (class (3,5,7,2); the character CONTENT is
     chirality-independent); the induced permutation T on the
     moved frame; exact isotypic projectors Pi_j = (1/3) sum_m
     om^{-jm} T^m in coefficient space; for each displacement
     generator, the least-squares coefficients on the moved frame
     split into (triv, om, ombar) energies (frame non-orthogonal:
     fractions normalized over the three isotypic images, typed);
     the moved sector's exact prediction is the regular-rep share
     2/3 nontrivial; bar for IDENTIFIED: aggregate nontrivial
     share in [0.5, 0.85].

 S6  MULTIPLICITIES: each of the top-17 bulk modes least-squares
     decomposed on the 17-frame; per-mode energy fractions on the
     sectors (moved, fixed, vacuum, pole) + the in-frame residual
     (how much of the bulk lies in the frame span at all -- the
     honesty number); effective multiplicities m_sector = sum of
     fractions; bar for IDENTIFIED: rounding gives exactly
     (12, 3, 1, 1) AND the median in-frame residual <= 0.3.

 S7  VERDICT (frozen): AUDIT-BROKEN (any S1/S2 regression fails)
     / MOVING12-IDENTIFIED (S4 angle bars AND S5 character bar
     AND S6 multiplicity bar) / MOVING12-DIMENSION-ONLY (the
     honest burial: same dimensions, different spaces -- the
     angle/multiplicity/character tables typed).

Sources (read-only): pole_port_kappa_probe (build_rung,
feshbach_pole, pole_transform_closed), softport_cauchy_probe
(contractor, LAM1_REFS, displacement construction conventions),
divisor210_canonicity_probe results (census classes, cited),
v845 register conventions.  Float64 SVD/eigh; the register side
exact integer.  NO RH claim; report only.

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/moving12_soft17_probe.py
"""

import ast
import hashlib
import itertools
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

import pole_port_kappa_probe as pp         # noqa: E402 (READ-ONLY)
import softport_cauchy_probe as sc         # noqa: E402 (READ-ONLY)

T0 = time.time()
CHECKS = []
KILLS = []

ANCHORS = (9, 12, 13)
RANK_RUNGS = (9, 12, 13, 26, 40)
ANGLE_BAR = 1e-6
FOREIGN_QUAD = (2, 3, 5, 11)
BANNED_IDS = ("zetazero", "nzeros", "primerange", "isprime",
              "primepi", "nextprime", "prevprime")


def check(name, ok, detail="", kill=None):
    CHECKS.append((name, bool(ok)))
    if kill and not ok:
        KILLS.append(kill)
    print("  [%s] %s%s" % ("PASS" if ok else "FAIL", name,
                           ("  -- " + detail) if detail else ""),
          flush=True)
    return bool(ok)


def section(title):
    print("\n== %s ==  (t=%.1fs)" % (title, time.time() - T0),
          flush=True)


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


def orth(A, tol=1e-12):
    u, s, _ = np.linalg.svd(np.asarray(A, complex),
                            full_matrices=False)
    r = int(np.sum(s > tol * s[0]))
    return u[:, :r]


def principal_angles(A, B):
    Qa, Qb = orth(A), orth(B)
    sv = np.linalg.svd(Qa.conj().T @ Qb, compute_uv=False)
    return np.arccos(np.clip(sv, -1.0, 1.0))


print("E8.MOVING12.SOFT17.01 -- the 17 = 12 + 3 + 1 + 1 hypothesis, "
      "space level")
print("FROZEN_SPEC SHA-256: %s"
      % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
print("\nS0 -- firewall")
check("S0.1 AST firewall clean (no zero/prime oracles)",
      not ast_scan())

# ======================================================================
section("S1: the register side -- exact projectors and characters")
# ======================================================================
W16 = [tuple(b) for b in itertools.product((0, 1), repeat=4)]
WIDX = {w: i for i, w in enumerate(W16)}


def sig_bits(v):
    return (v[2], v[0], v[1], v[3])


A_BIT = (0, 0, 0, 1)
FSIG = (1, 1, 1, 0)
fixed_nz = [w for w in W16 if w != (0, 0, 0, 0) and sig_bits(w) == w]
moved = [w for w in W16 if w != (0, 0, 0, 0) and sig_bits(w) != w]
orbits = set()
for w in moved:
    orbits.add(frozenset({w, sig_bits(w), sig_bits(sig_bits(w))}))
check("S1.1 sigma label split: 3 fixed nonzero %s + 12 moved in "
      "exactly 4 free 3-orbits"
      % sorted(fixed_nz),
      sorted(fixed_nz) == sorted([A_BIT, FSIG, (1, 1, 1, 1)])
      and len(moved) == 12 and len(orbits) == 4
      and all(len(o) == 3 for o in orbits), kill="AUDIT-BROKEN")

nz = [w for w in W16 if w != (0, 0, 0, 0)]
S15 = np.zeros((15, 15))
nz_idx = {w: i for i, w in enumerate(nz)}
for w in nz:
    S15[nz_idx[sig_bits(w)], nz_idx[w]] = 1.0
om = np.exp(2j * math.pi / 3.0)
dims = []
for j in range(3):
    Pi = (np.eye(15) + om ** (-j) * S15
          + om ** (-2 * j) * (S15 @ S15)) / 3.0
    dims.append(int(round(float(np.trace(Pi).real))))
mv_mask = np.array([w in moved for w in nz])
dims_mv = []
for j in range(3):
    Pi = (np.eye(15) + om ** (-j) * S15
          + om ** (-2 * j) * (S15 @ S15)) / 3.0
    dims_mv.append(int(round(float(
        np.trace(Pi[np.ix_(mv_mask, mv_mask)]).real))))
check("S1.2 EXACT isotypic dimensions: C^15 = triv^%d + om^%d + "
      "ombar^%d; moved sector (%d,%d,%d) = 4 x regular; fixed "
      "sector triv^3"
      % tuple(dims + dims_mv),
      dims == [7, 4, 4] and dims_mv == [4, 4, 4],
      kill="AUDIT-BROKEN")

CLASS1 = {"F1": 3, "F2": 5, "F3": 7, "A": 2}
CLASS2 = {"F1": 3, "F2": 7, "F3": 5, "A": 2}


def divisor_map(cls):
    p1, p2, p3, pa = cls["F1"], cls["F2"], cls["F3"], cls["A"]
    return {w: (p1 ** w[0]) * (p2 ** w[1]) * (p3 ** w[2])
            * (pa ** w[3]) for w in W16}


D1 = divisor_map(CLASS1)
D2 = divisor_map(CLASS2)
mvset1 = sorted(D1[w] for w in moved)
mvset2 = sorted(D2[w] for w in moved)
fxset1 = sorted(D1[w] for w in fixed_nz)
check("S1.3 census divisor maps (both gauge classes): moved sets "
      "EQUAL %s...; fixed set %s; 17 = 12 + 3 + 1 + 1 == %d"
      % (mvset1[:4], fxset1, 12 + 3 + 1 + 1),
      mvset1 == mvset2 and fxset1 == sorted(D2[w] for w in fixed_nz)
      and fxset1 == [2, 105, 210] and 12 + 3 + 1 + 1 == 17,
      kill="AUDIT-BROKEN")

# ======================================================================
section("S2: the measured objects (pole-port + softport, read-only)")
# ======================================================================
DATA = {}
reg_lam = True
for kz in sorted(set(ANCHORS) | set(RANK_RUNGS)):
    out = pp.build_rung(kz)
    rr, d, Bp, Bm, Fp, K, Gp, Rp, Delta, c_ar = out
    h, D = rr["h"], rr["D"]
    if h > 900:
        continue
    lam, W = np.linalg.eigh(Delta)
    if kz in ANCHORS:
        reg_lam &= abs(lam[0] - sc.LAM1_REFS[kz]) \
            / sc.LAM1_REFS[kz] <= 1e-3
    # displacement structure (softport conventions, inline)
    U_, s_, Vh_, A2_ = sc.contractor(Bp, Bm)
    Cf = A2_ @ U_.conj().T
    L = Cf.shape[0]
    jj = np.arange(L)
    tau = np.where(jj <= L // 2, jj, L - jj) * (
        2.0 * math.pi / L) / D
    pos, neg = d > 0.0, d < 0.0
    Cres = Cf[np.ix_(neg, pos)]
    R = tau[neg][:, None] * Cres - Cres * tau[pos][None, :]
    uR, sR, vRh = np.linalg.svd(R)
    rk = int(np.sum(sR > 1e-3 * sR[0]))
    DATA[kz] = dict(rr=rr, d=d, Fp=Fp, Gp=Gp, Rp=Rp, Delta=Delta,
                    lam=lam, tau=tau, pos=pos, neg=neg, rk=rk,
                    uR=uR, vRh=vRh, h=h, D=D, L=L)
    print("    kz %-3d h %-4d L %-5d lam1 %.3e rank@1e-3 %d"
          % (kz, h, L, lam[0], rk), flush=True)
check("S2.1 REGRESSION lam1(Delta) at anchors == softport refs "
      "(rel 1e-3)", reg_lam, kill="AUDIT-BROKEN")
ranks = [DATA[kz]["rk"] for kz in RANK_RUNGS if kz in DATA]
check("S2.2 REGRESSION displacement rank@1e-3(tau): kz9 = %d in "
      "[11, 13]; series %s non-growing (max <= min + 3)"
      % (DATA[9]["rk"], ranks),
      11 <= DATA[9]["rk"] <= 13
      and max(ranks) <= min(ranks) + 3, kill="AUDIT-BROKEN")

kz = 9
dd = DATA[9]
h9, D9, L9 = dd["h"], dd["D"], dd["L"]
v_pole = np.exp(0.5 * np.arange(h9) * D9)
v_pole = v_pole / np.linalg.norm(v_pole)
fp = pp.feshbach_pole(dd["Delta"], dd["Gp"], dd["Rp"], v_pole)
kap9 = fp["s"] / fp["lam1"]
check("S2.3 REGRESSION pole port kz9: kappa = %.3f in [2.6, 2.8]; "
      "n95 = %d <= 20 (the measured bulk concentration behind "
      "the '17')" % (kap9, fp["n95"]),
      2.6 <= kap9 <= 2.8 and fp["n95"] <= 20, kill="AUDIT-BROKEN")

# top-17 coupled bulk modes (exact Feshbach split, coupling census)
w9 = fp["w"]
e1 = np.zeros(h9)
e1[0] = 1.0
u_h = e1 - w9
nu = np.linalg.norm(u_h)
Hh = np.eye(h9) - 2.0 * np.outer(u_h / nu, u_h / nu) \
    if nu > 1e-12 else np.eye(h9)
Bc = Hh[:, 1:]
G9, rv9 = fp["G"], fp["rv"]
gam, Gv = np.linalg.eigh(G9)
ci = (Gv.T @ rv9) ** 2 / gam
order = np.argsort(ci)[::-1]
K17 = 17
modes_delta = Bc @ Gv[:, order[:K17]]           # Delta coords, h x 17
evG, VpG = np.linalg.eigh(dd["Gp"])
Rm9 = VpG @ np.diag(evG ** -0.5) @ VpG.T
modes_h = Rm9 @ modes_delta                     # h-space vectors
modes_bin = dd["Fp"] @ modes_h                  # L x 17 complex
frac95 = float(np.sum(np.sort(ci)[::-1][:K17]) / np.sum(ci))
print("    top-17 coupled bulk modes carry %.4f of r'G^-1 r "
      "(n95 = %d)" % (frac95, fp["n95"]))

# ======================================================================
section("S3: the divisor modular frame (the frozen bridge)")
# ======================================================================
tau9 = dd["tau"]


def profile(dv):
    ph = np.exp(-0.5j * math.log(dv) * tau9) if dv > 1 \
        else np.ones(L9, complex)
    return ph / np.linalg.norm(ph)


def frame_for(dmap):
    mv_cols = [profile(dmap[w]) for w in moved]
    fx_cols = [profile(dmap[w]) for w in fixed_nz]
    vac = profile(1)
    return np.array(mv_cols).T, np.array(fx_cols).T, \
        vac.reshape(-1, 1)


F_mv, F_fx, F_vac = frame_for(D1)
Pc = pp.pole_transform_closed(h9, L9, D9)
F_pole = (Pc / np.linalg.norm(Pc)).reshape(-1, 1)
F17 = np.hstack([F_vac, F_fx, F_mv, F_pole])
sv17 = np.linalg.svd(F17, compute_uv=False)
check("S3.1 frame conditioning: 17 columns, smin/smax = %.3e "
      "(bar >= 1e-3: numerically independent)"
      % (sv17[-1] / sv17[0]),
      F17.shape[1] == 17 and sv17[-1] / sv17[0] >= 1e-3)

# ======================================================================
section("S4: principal angles -- the space test")
# ======================================================================
rk9 = dd["rk"]
U12 = dd["uR"][:, :rk9]                 # neg-bin space
V12 = dd["vRh"][:rk9].conj().T          # pos-bin space
neg9, pos9 = dd["neg"], dd["pos"]


def ang_stats(A, B):
    a = principal_angles(A, B)
    return float(np.max(a)), float(np.min(a)), \
        float(np.median(a)), len(a)


b1 = ang_stats(U12, F_mv[neg9])
b2 = ang_stats(V12, F_mv[pos9])
c17 = ang_stats(modes_bin, F17)
print("    (b1) span(U%d) vs moved-frame|neg  : max %.4f min %.4f "
      "med %.4f rad (%d angles)" % ((rk9,) + b1))
print("    (b2) span(V%d) vs moved-frame|pos  : max %.4f min %.4f "
      "med %.4f rad (%d angles)" % ((rk9,) + b2))
print("    (c)  span(bulk-17) vs 17-frame     : max %.4f min %.4f "
      "med %.4f rad (%d angles)" % c17)

# contrast controls
DF = divisor_map({"F1": FOREIGN_QUAD[1], "F2": FOREIGN_QUAD[2],
                  "F3": FOREIGN_QUAD[3], "A": FOREIGN_QUAD[0]})
Ff_mv, _, _ = frame_for(DF)
b1f = ang_stats(U12, Ff_mv[neg9])
outS = pp.build_rung(9, scramble_seed=1)
dS, BpS, BmS = outS[1], outS[2], outS[3]
US_, sS_, VhS_, A2S_ = sc.contractor(BpS, BmS)
CfS = A2S_ @ US_.conj().T
posS, negS = dS > 0.0, dS < 0.0
CresS = CfS[np.ix_(negS, posS)]
RS = tau9[negS][:, None] * CresS - CresS * tau9[posS][None, :]
uRS, sRS, _ = np.linalg.svd(RS)
rkS = int(np.sum(sRS > 1e-3 * sRS[0]))
b1s = ang_stats(uRS[:, :max(rkS, 1)], F_mv[negS])
print("    contrast: foreign frame {2,3,5,11} max angle %.4f "
      "(truth %.4f, gap %+.4f); scramble generators (rank %d) "
      "max angle %.4f" % (b1f[0], b1[0], b1f[0] - b1[0], rkS,
                          b1s[0]))
angles_close = b1[0] <= ANGLE_BAR and c17[0] <= ANGLE_BAR
check("S4.1 THE ANGLE TEST (frozen bar: max angle <= 1e-6 rad on "
      "(b1) and (c)): %s -- max(b1) = %.4f, max(c) = %.4f rad "
      "(90 deg = 1.5708: orthogonal)"
      % ("CLOSED" if angles_close else
         "NOT CLOSED (the honest burial)", b1[0], c17[0]),
      True)
check("S4.2 contrast census TYPED: |truth - foreign| = %.4f, "
      "|truth - scramble| = %.4f in max angle -- the bridge's "
      "information content (near 0 with angles far from 0 = the "
      "frame does not see the displacement structure at all)"
      % (abs(b1[0] - b1f[0]), abs(b1[0] - b1s[0])), True)

# ======================================================================
section("S5: characters -- the sigma content of the generators")
# ======================================================================
perm12 = np.zeros((12, 12))
for i, w in enumerate(moved):
    j = moved.index(sig_bits(w))
    perm12[j, i] = 1.0
T = perm12
Fn = F_mv[neg9]
coef, *_ = np.linalg.lstsq(Fn, U12, rcond=None)
iso_energy = np.zeros(3)
for j in range(3):
    Pi = (np.eye(12) + om ** (-j) * T
          + om ** (-2 * j) * (T @ T)) / 3.0
    proj = Fn @ (Pi @ coef)
    iso_energy[j] = float(np.sum(np.abs(proj) ** 2))
iso_frac = iso_energy / max(float(np.sum(iso_energy)), 1e-300)
resid = float(np.linalg.norm(Fn @ coef - U12)
              / np.linalg.norm(U12))
nontriv = float(iso_frac[1] + iso_frac[2])
print("    isotypic energy fractions of proj(U) on the moved "
      "frame: triv %.3f, om %.3f, ombar %.3f; in-frame residual "
      "%.3f (regular-rep prediction: 1/3 each, nontrivial 2/3)"
      % (iso_frac[0], iso_frac[1], iso_frac[2], resid))
char_ok = 0.5 <= nontriv <= 0.85
check("S5.1 THE CHARACTER TEST (frozen bar: nontrivial share in "
      "[0.5, 0.85]): share = %.3f -> %s (typed: residual %.3f "
      "says how much of span(U) the moved frame captures at all)"
      % (nontriv, "carries the C3 characters" if char_ok
         else "does NOT verify the regular-rep content", resid),
      True)

# ======================================================================
section("S6: multiplicities -- the bulk-17 sector census")
# ======================================================================
coef17, *_ = np.linalg.lstsq(F17, modes_bin, rcond=None)
sect = {"vac": [0], "fix": [1, 2, 3],
        "mov": list(range(4, 16)), "pole": [16]}
mult = dict.fromkeys(sect, 0.0)
resids = []
print("    mode  in-frame-resid  vac    fix    mov    pole")
for m in range(K17):
    cm = coef17[:, m]
    tot = 0.0
    en = {}
    for snm, cols in sect.items():
        cpart = np.zeros_like(cm)
        cpart[cols] = cm[cols]
        en[snm] = float(np.linalg.norm(F17 @ cpart) ** 2)
        tot += en[snm]
    rm = float(np.linalg.norm(F17 @ cm - modes_bin[:, m])
               / np.linalg.norm(modes_bin[:, m]))
    resids.append(rm)
    for snm in sect:
        mult[snm] += en[snm] / max(tot, 1e-300)
    if m < 5 or m == K17 - 1:
        print("    %-4d  %.3f          %.3f  %.3f  %.3f  %.3f"
              % (m, rm, *(en[s] / max(tot, 1e-300)
                          for s in ("vac", "fix", "mov", "pole"))))
med_resid = float(np.median(resids))
eff = tuple(int(round(mult[s])) for s in ("mov", "fix", "vac",
                                          "pole"))
mult_ok = eff == (12, 3, 1, 1) and med_resid <= 0.3
print("    effective multiplicities (mov, fix, vac, pole) = "
      "(%.2f, %.2f, %.2f, %.2f) -> rounded %s; median in-frame "
      "residual %.3f"
      % (mult["mov"], mult["fix"], mult["vac"], mult["pole"],
         eff, med_resid))
check("S6.1 THE MULTIPLICITY TEST (frozen bar: rounded == "
      "(12, 3, 1, 1) AND median residual <= 0.3): %s"
      % ("matches" if mult_ok else "does NOT match (typed)"),
      True)

# ======================================================================
section("S7: verdict (frozen)")
# ======================================================================
if KILLS:
    verdict = KILLS[0]
elif angles_close and char_ok and mult_ok:
    verdict = "MOVING12-IDENTIFIED"
else:
    verdict = "MOVING12-DIMENSION-ONLY"
n_pass = sum(1 for _, ok in CHECKS if ok)
print("\n" + "=" * 70)
print("CHECKS: %d/%d passed" % (n_pass, len(CHECKS)))
if n_pass != len(CHECKS):
    print("FAILED: %s" % [nm for nm, ok in CHECKS if not ok])
print("VERDICT: %s" % verdict)
print("=" * 70)
print("""
HONEST CONSEQUENCE (measured): the register split 3 + 12 and the
isotypic structure (moved = 4 x regular) are EXACT; the measured
displacement rank (%d at kz9, non-growing) and the bulk
concentration (n95 = %d) reproduce the deployed numbers.  The
space-level identification through the only deployed bridge (the
divisor modular frame) gives max principal angles %.4f (b1) /
%.4f (c) rad against the frozen 1e-6 bar, nontrivial character
share %.3f, effective multiplicities (%.1f, %.1f, %.1f, %.1f).
If the verdict above is DIMENSION-ONLY: the 17 = 12 + 3 + 1 + 1
arithmetic stands as a COUNT but the softport displacement
generators are NOT the Gaussian label channels under this bridge
-- the identification hypothesis is buried at space level unless
a different (not yet deployed) intertwiner is exhibited; typed,
not smoothed.  NO RH claim.""" % (rk9, fp["n95"], b1[0], c17[0],
                                  nontriv, mult["mov"],
                                  mult["fix"], mult["vac"],
                                  mult["pole"]))
print("runtime: %.1f s" % (time.time() - T0))
sys.exit(0 if n_pass == len(CHECKS) else 1)
