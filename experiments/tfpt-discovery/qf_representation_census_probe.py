#!/usr/bin/env python3
"""QF-OFFENSIVE strand 2 -- the REPRESENTATION CENSUS of the 6-dim
near-kernel: is E_qf the canonical E8 defect space E_7 (+) E_{-2}?
qf_representation_census_probe (exploration only).

Exploration only (tfpt-experiment firewall): NOT wired into run_all.py,
no ledger row, no paper edit, no website edit, NO RH CLAIM, and this
probe writes no files.  Every candidate, lift, bar and control below is
frozen in this docstring BEFORE the first run; the near-kernel is
computed only AFTER the candidate battery hash is printed.

INPUT STATE (frozen findings, none re-adjudicated here):
  *  yosida_handoff_probe / yosida_qf_convergence_probe -- the
     diagonal-gram wall lives in a stable near-kernel of the source
     window operator: on the extended tower (ATOM_MAX_EXT = 4e6,
     M_TOP = 972) the near-null count (lam <= 1e-4) is 6 from M = 888
     on, constant over 22 rungs, consecutive subspace alignment
     >= 0.9996 (mean last 4 = 0.99969); a single deep mode
     (lam <= 1e-5) persists.  The OBJECT converges; its battery
     pairing does not (QF-DEAD there).
  *  v752 (PROJ-HAMMING-EXACT) -- on the 15 nonzero points of
     V = L/(1+i)L: B B^T = 4I + 3J exact, eigenvalues
     {7 (x1, constant vector), +2 (x9), -2 (x5)}: the exact
     decomposition R^15 = E_7 (+) E_{+2}^(9) (+) E_{-2}^(5).
  *  v753 (POLARITY-MATCH) -- the 15 ramified Hecke hyperplanes are
     the hbar-orthogonal spaces; canonicity census: of 64 alternating
     forms 28 are nondegenerate and EXACTLY 1 is sigma-invariant (the
     canonical hbar from h = H/4).  Deck commutes with chi_par.
  *  v756 (KMS-INCIDENCE-CP-COVARIANT) -- K = B/7 as a CP-unital
     channel with 105 explicit Kraus terms, sigma-covariant, KMS
     half-weight (2^{-m/2} on the degree tower) compatible.
  *  simpler_schur_recursion_probe -- the deployed comb splits
     zeta-free into channels ct(=arch+pole) / ro / re / sp / in;
     ram-odd (ro) is the unique negative-pressure channel on every
     Schur rung; the v742 dictionary: odd places + arch act V-scalar,
     ram-even -> chi_0, ram-odd -> chi_par.

HYPOTHESIS UNDER TEST (new, explicitly falsifiable, NOT established
anywhere): E_qf ~ E_7 (+) E_{-2}: the 6 near-null modes are the
canonical E8 defect space -- 1 trivial mode (pole/normalization
channel) + 5 negative incidence modes (carrier defect space),
6 = 1 + 5, with the 9-dim +2 sector as stable bulk.  A pure dimension
match counts for NOTHING: only symmetry characters, principal angles
and exact multiplicities count.

THE THREE FROZEN CANDIDATES (subspaces of R^15, all fully specified
here; label order = the 15 nonzero bit-4-tuples of ram.ALL_V):
  C1 (1 (+) 5, incidence spectrum): E_7 = span(1) (+) E_{-2} = the
      5-dim eigenvalue-(-2) eigenspace of the canonical incidence B.
  C2 (3 (x) 2, deck channels x boundary modes): the 3 sigma-FIXED
      labels y_f (the "three deck channels"; v752 P0.2: sigma has
      3 fixed classes + 4 three-orbits) each contribute the two
      boundary modes  e_{y_f}  (point mode)  and
      h_{y_f} = unit indicator of H_{y_f} \\ {y_f}  (hyperplane mode,
      6 points; y_f lies on its own polar since hbar is alternating).
      Predeclared exactly: channels = the 3 sigma-fixed labels, modes
      = (point, punctured polar hyperplane).
  C3 (complexified rank-3): the v739 rank-3 jet reading (three linear
      functionals = value + first-jet reads of one complex function)
      is bridged to the incidence layer as THREE COMPLEX LINES: the
      sigma-rotation planes (sum-zero 2-dim planes, sigma acts by
      order-3 rotation = multiplication by a primitive cube root:
      a complex structure) of the 3 moved sigma-orbits whose orbit
      sum is a NONZERO fixed label (v752 P5.4: the 4 moved orbits sum
      bijectively onto {0} + the 3 fixed labels; the orbit summing to
      0 is excluded -- no choice).  Predeclared complexification:
      per selected orbit (o1, o2, o3) = (lb, sig lb, sig^2 lb), the
      plane span{(e_{o1}-e_{o2})/sqrt2, (e_{o1}+e_{o2}-2e_{o3})/sqrt6}.
      HONESTY: the v739 functionals live on the jet surface, not on
      V; this is the predeclared incidence-layer avatar.

THE FROZEN LIFT (source-native; the rank bottleneck stated plainly):
  The deployed scalar comb realizes EXACTLY TWO characters of V
  (v742 dictionary: chi_0 on ct/re/sp/in, chi_par on ro).  Any lift
  of label structure into the window space therefore factors through
  the frozen CHANNEL SECTORS -- a literal rank-6 embedding of R^15
  does not exist on the deployed surface (this bottleneck is itself a
  finding of the census and is measured, not assumed).  The
  predeclared lift maps each candidate to a rank-6 window frame built
  from sector spectral data only (source data, never near-kernel
  data), per rung M:
    L1 (for C1):  [ top eigenvector of T_pole ]  (the pole/
        normalization channel <- E_7, the trivial character)  (+)
        [ the 5 MOST NEGATIVE eigenvectors of T_ro ]  (the ram-odd =
        deck-odd sector's negative frame <- E_{-2}, the NEGATIVE
        incidence modes; sign dictated by the srp finding that ro is
        THE negative-pressure channel).
    L2 (for C2):  for each of the 3 lowest deck-odd levels
        m in {1, 3, 5} (the three dominant KMS weights <- the three
        deck channels): the most negative + most positive eigenvector
        of the single-atom sector T^(m) (the two boundary modes).
    L3 (for C3):  the 6 most negative eigenvectors of T_sp (the
        SPLIT sector: p = 1 mod 4 are the complexified Gaussian
        places -- 3 conjugate pairs <- rank-3 complexified).
  ALTERNATIVE natural lifts (listed, reported-not-gated): (i) the
  rank-3 character-shadow frame (pole + KMS-weighted even/odd ram
  footprints); (ii) the v742 label-extended operator
  T_even (x) I + T_ro (x) D_chi (block-diagonal over labels -- cannot
  resolve a 6-dim label subspace, documented); (iii) arch+pole
  instead of pole-only as the normalization channel; (iv) other level
  triples for L2.  Only L1/L2/L3 above are gated.

PROTOCOL (extended-comb machinery of yosida_qf_convergence_probe,
ATOM_MAX_EXT = 4e6, all reused verbatim where it exists):
  ladder   NK_LAD = 888..972 step 4 (22 rungs; the frozen surface on
           which the 6-count was measured).  LAST5 = final 5 rungs,
           HALF2 = final 11 rungs.  Near-null threshold THR_NULL =
           1e-4 (parent policy, gated); counts at (3e-4, 1e-4, 3e-5)
           reported.
  step 1   spectral projector P_X^(6) onto the near-null modes of
           T[:M,:M] (thr policy frozen; modes by threshold only,
           never by target deviation).
  step 2   lift frames L1/L2/L3 per rung (above, frozen).
  step 3   the SIX PRINCIPAL ANGLES between P_X^(6) and each lifted
           candidate per rung (singular values of V_N^T Q_L); the
           gate statistic is D_X = ||P_X^(6) - P_X^(cand)||_2
           = sin(theta_max) (equal rank 6).
  step 4   character checks (sharp vs shadow stated honestly):
           - sigma: candidates carry EXACT sigma data (gate A1:
             sigma-invariance of the candidate projector +
             integrality of the fixed/rotation multiplicities,
             tol 1e-9).  The measured near-kernel carries NO direct
             sigma action (the scalar window is sigma-blind) -- the
             sigma character is where the 27 wrong forms and the
             wrong labelings die (canonicity census).
           - Deck / NS-R (chi_par; identical grading by v752 P5 +
             v753 P4): measured per-mode ro-DOMINANCE
             (|<v, T_ro v>| > |<v,T_re v>| + |<v,T_sp v>| +
             |<v,T_in v>|).  Predicted counts (frozen): C1: 5 (the
             five defect modes are ro-dominant, the pole mode is
             continuum-dominated), C2: 6, C3: 0.  Gate A2: measured
             count == prediction on >= 4 of the LAST5 rungs.
           - pole/normalization multiplicity: measured count of
             pole-dominant modes (|<v, w_pole>|^2 > 0.5; at most one
             mode can exceed 1/2).  Predicted (frozen): C1: 1,
             C2: 0, C3: 0.  Gate A3: == on >= 4 of LAST5 rungs.
           - KMS half-weight: GUARD (exact): the deployed ramified
             masses are the v756 KMS half-weights,
             mu_m 2^{m/2} / (2 ln 2) = 1 to 1e-12; the per-mode ram
             level profiles q_m = v^T T^(m) v are REPORTED (no
             preregistered rate exists for them).
  step 5   rate gate (frozen; the ideal ||P^(6)-P^(cand)|| -> 0 is
           replaced by level + monotonicity bars because the
           character bottleneck makes exact 0 unreachable in
           principle at rank 6 -- stated before the run):
           B: median(D_X over LAST5) <= D_LEVEL = 0.70  AND
              linear slope of D_X vs X over HALF2 <= +0.005 per X
              unit (non-increasing within tolerance).
           Comparative (frozen): the winning candidate must beat
           each other candidate by D_MARGIN = 0.02 in LAST5-median
           D_X, unless that other candidate already fails a gate.

CONTROLS (must fire, else QF-CENSUS-INVALID):
  CF  the 27 OTHER nondegenerate alternating forms (v753 census;
      full census, they fall in sigma-orbits reported): their
      E'_7 (+) E'_{-2} candidates must FAIL gate A1 (sigma
      sharpness) -- fire iff 27/27 fail.
  CP  wrong labelings: 5 frozen permutations of the 15 labels
      (numpy default_rng(20260805)) applied to C1 -- each must fail
      A1; fire iff 5/5 fail.
  CS/CE  scramble source (positions uniform (0.5, 2 alpha), masses
      kept, seed 7, extended comb) and Epstein x^2+5y^2 source:
      parent fire rule verbatim (yosida_handoff_probe.control_yosida
      at M_CTRL = 512: sandwich break / eps-monotonicity break /
      singular Yosida) + negative-spectrum census printed (the
      near-kernel construction breaks: lam < -THR_NULL counts).

VERDICT ENUM (frozen):
  QF-IS-INCIDENCE-DEFECT  = guards + controls ok AND C1 passes
      A1+A2+A3+B AND C2, C3 each fail a gate or are strictly worse
      (LAST5-median D >= C1's + 0.02): the near-kernel IS the
      canonical E8 defect space on the deployed surface.
  QF-CANDIDATE-C2 / QF-CANDIDATE-C3 = analogous for C2 / C3.
  QF-REPRESENTATION-OPEN  = guards + controls ok, no candidate
      passes all gates (the 6 = 1 + 5 match stays typed DECORATIVE).
  QF-CENSUS-INVALID       = a guard fails or a control does not fire.

STOP-LIST (binding): candidates + lifts + bars frozen before any
near-kernel data (hash printed first); no selection of modes by
target deviation; no fits inside gates (the slope is a declared gate
statistic); no bare A^{-1}; no PD-margin assumption; no Riemann
zeros; NO RH claim.  This probe writes no files.  Runtime cap 600 s.

RESULTS (2026-08-05, first and only preregistered run, 11.6 s;
GATES 6/12, GUARDS+CONTROLS 26/26, verdict QF-REPRESENTATION-OPEN --
the 6 = 1 + 5 dimension match stays typed DECORATIVE):
  *  LABEL SIDE ALL SHARP: anchors exact (B B^T = 4I + 3J, spectrum
     (1, 9, 5); census 64 -> 28 -> exactly 1 sigma-invariant = the
     canonical hbar; chi_par 7/8, y0 unique and sigma-fixed).  All
     three candidates pass A1 with EXACT sigma multiplicities:
     C1 (n_fix, n_pair) = (4, 1) (E_{-2} = 3 fixed + 1 rotation
     pair), C2 = (6, 0), C3 = (0, 3); deck contents 3.2 / 3.5 / 4.0;
     pole contents 1.0 / 0.8 / 0.0.  The census DISCRIMINATES on the
     label side: the three candidates carry pairwise different
     sigma/deck/pole character data.
  *  CONTROLS ALL FIRE: CF 27/27 wrong forms fail sigma sharpness
     (all by non-commutation; 9 sigma-orbits; E'_{-2} vs E_{-2}
     smallest principal cosine 0.000..0.500); CP 5/5 wrong labelings
     fail; CS scramble lambda_min = -3.33e+3 (246/512 negative,
     sandwich break); CE Epstein lambda_min = -3.32e+1 (189/512
     negative).  The near-kernel reading is destroyed on indefinite
     sources; the canonical form is the only sigma-sharp one.
  *  NEAR-KERNEL REPRODUCED: count 6 on 22/22 rungs (M = 888..972),
     deep count 1 throughout, alignment mean last 4 = 0.999695,
     lambda_min 7.44e-6 -> 6.46e-6.
  *  THE MEASURED ANGLE STRUCTURE (the honest finding): the near-
     kernel shares EXACTLY ONE direction with the C1 lift frame --
     cos theta_1 = 0.992..0.999 on every one of the 22 rungs (the
     ram-odd most-negative wavepacket direction, also contained in
     the C2 level frame: cos_1 = 0.985..0.999 there); a second
     direction sits at cos theta_2 = 0.614..0.648 (X-stable, slowly
     rising 0.617 -> 0.640 over the second half); the remaining four
     angles are ~90 deg (cos <= 0.02).  C3 (split sector): single
     partial contact cos_1 = 0.69..0.72.  D_X = sin theta_max =
     1.0000 for all candidates on all rungs: B fails everywhere --
     no predeclared rank-6 lift captures more than 1 + 1 partial of
     the 6 modes.
  *  THE MEASURED CHARACTER ANATOMY CONTRADICTS THE C1 SIGNATURE:
     ro-dominant mode count 0/6 on every LAST5 rung (predicted 5 for
     C1, 6 for C2, 0 for C3 -- only C3's A2 and the trivial A3
     zeros pass); pole-dominant count 0 (max pole overlap^2 = 0.31
     at the 0.5 bar).  The mode table shows what the near-kernel
     actually is on this surface: each mode balances a LARGE pole
     term against LARGE split+inert terms of opposite sign (e.g.
     mode 2: pole +6.1e+2 vs sp -3.0e+2, in -3.0e+2) with ram
     pairings two to three orders smaller (|ro| <= 1.7) -- the
     near-kernel is a CONTINUUM-vs-ODD-PLACES balance; the ramified
     (deck/NS-R-graded) channel is an energetic spectator at mode
     level.  Deck-flip confirms from the other side: T - 2 T_ro is
     massively indefinite (193 negative directions) while the
     near-null modes barely see ro -- ram-odd is load-bearing for
     GLOBAL positivity, not for the near-kernel's internal balance.
  *  KMS REPORT: the deployed ram masses ARE the v756 half-weights
     (guard exact, dev 0.0); the deep mode's level profile decays
     with ratio ~0.67..0.69 per level (2^{-1/2} = 0.707 -- suggestive
     KMS-half-weight decay, reported not gated); shallower modes
     change sign across levels.
  *  HONEST CONSEQUENCE (stated plainly): on the deployed surface
     the identification E_qf ~ E_7 (+) E_{-2} FAILS the preregistered
     census -- not because the incidence layer is wrong (it is exact
     and uniquely canonical, and the wrong-form/wrong-labeling
     controls die precisely on its sigma character) but because the
     deployed scalar comb realizes only two V-characters and the
     near-kernel's measured anatomy is a pole-vs-split/inert balance
     rather than a ramified defect.  What survives positively: ONE
     near-null direction is, rung-stably to cos = 0.997, the ram-odd
     negative wavepacket -- a genuine 1-dimensional contact between
     the qf wall and the deck-odd sector (a candidate avatar of ONE
     defect direction, not five); and a second partial contact at
     cos ~ 0.64.  The boundary-triple route does NOT get its
     geometry fixed by projective Hamming on this evidence.  Named
     next surfaces (not probed here): a window operator that
     actually couples the label fiber (incidence/Kraus mixing terms,
     the v756 "still missing" list) so that a rank-6 lift EXISTS;
     and the character census of the sp/in (odd-places) balance that
     the modes really live on.  NO RH claim, no X -> infinity claim.

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/qf_representation_census_probe.py
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
_VERIFY = os.path.abspath(os.path.join(_HERE, "..", "..",
                                       "verification"))
sys.path.insert(0, _HERE)
sys.path.insert(0, _VERIFY)

import v563_paper2_readouts as core  # noqa: E402
import v738_hecke_mod_ramified as ram  # noqa: E402
import simpler_schur_recursion_probe as srp  # noqa: E402
import moonshot_arch_glue_probe as stage2  # noqa: E402
import handoff_bulk_probe as hbp  # noqa: E402
import yosida_handoff_probe as yhp  # noqa: E402
import epstein_firewall_probe as epx  # noqa: E402

T_START = time.time()

# ------------------------------------------------ frozen specification
D = srp.DGRID                        # 1/64, dyadic float-exact
ATOM_MAX_EXT = 4000000               # extended comb cap (frozen)
M_CAP_EXT = int(math.floor(math.log(ATOM_MAX_EXT) / D))   # 972
M_TOP = 972                          # deepest rung
M_PAR = 824                          # parent cap (prefix Ward)
NK_LAD = list(range(888, 973, 4))    # 22 rungs, count-6 surface
LAST5 = NK_LAD[-5:]                  # M = 956..972
HALF2 = NK_LAD[11:]                  # M = 932..972 (slope window)

THR_NULL = 1.0e-4                    # gated near-null threshold
THR_ROB = (3.0e-4, 1.0e-4, 3.0e-5)   # reported thresholds
THR_DEEP = 1.0e-5                    # deep-mode census (reported)

TOL_SHARP = 1.0e-9                   # A1 integrality / commutation
POLE_DOM = 0.5                       # A3 pole-dominance bar
A_MAJOR = 4                          # A2/A3: >= 4 of LAST5 rungs
D_LEVEL = 0.70                       # B: LAST5-median D_X bar
D_SLOPE = 0.005                      # B: slope bar per X unit
D_MARGIN = 0.02                      # comparative margin
RO_LEVELS_C2 = (1, 3, 5)             # L2 deck-channel levels (frozen)
N_RAM_LEV = 21                       # ram levels m = 1..21 (2^21<4e6)
PRED_RO_DOM = dict(C1=5, C2=6, C3=0)  # frozen A2 predictions
PRED_POLE = dict(C1=1, C2=0, C3=0)    # frozen A3 predictions

REPRO_COUNT = 6                      # near-kernel reproduction (qf)
REPRO_MIN_RUNGS = 20                 # count == 6 on >= 20 of 22
ALIGN_BAR = 0.9977                   # mean align last 4 (0.99969-tol)
COMB_DEV_BAR = 1.0e-12               # sieve == deployed masses
PREFIX_WARD = 1.0e-12                # extended vs parent tower
ADD_WARD = 1.0e-12                   # sector additivity
KMS_TOL = 1.0e-12                    # mu_m 2^{m/2} == 2 ln 2
SANDWICH_TOL = 1.0e-9                # PD sandwich slack
BOUND_TOL = 1.0e-9                   # cos^2 in [0, 1] audit
RUNTIME_CAP = 600.0                  # seconds, predeclared

N_PERMS = 5                          # CP wrong-labeling controls
SEED_PERM = 20260805                 # frozen perm rng seed
M_CTRL = 512                         # CS/CE spectral rung
EP_NCAP = 34000                      # Epstein Lambda_E table reach
EP_MMAX = 640                        # Epstein control tower cap
SEED = 7                             # scramble seed (parent)

BANNED = ("zetazero", "nzeros", "isprime", "primerange", "nextprime",
          "prevprime", "primepi", "sympy")

CHECKS = []       # guards + controls: all must pass, else invalid run
GATES = []        # candidate gates: feed the verdict only


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok)))
    print("[%s] %s%s" % ("PASS" if ok else "FAIL", name,
                         (": " + detail) if detail else ""))
    return bool(ok)


def gate(name, ok, detail=""):
    GATES.append((name, bool(ok)))
    print("[GATE %s] %s%s" % ("PASS" if ok else "FAIL", name,
                              (": " + detail) if detail else ""))
    return bool(ok)


def ast_firewall():
    with open(os.path.abspath(__file__), "r", encoding="utf-8") as fh:
        tree = ast.parse(fh.read())
    hits = set()
    for node in ast.walk(tree):
        name = ""
        if isinstance(node, ast.Name):
            name = node.id
        elif isinstance(node, ast.Attribute):
            name = node.attr
        elif isinstance(node, (ast.Import, ast.ImportFrom)):
            for alias in node.names:
                token = alias.name.split(".")[0]
                if any(b in token.lower() for b in BANNED):
                    hits.add(token)
        if name and any(b in name.lower() for b in BANNED):
            hits.add(name)
    return sorted(hits)


def lin_slope(xs, ys):
    A = np.vstack([np.ones_like(xs), xs]).T
    coef, *_ = np.linalg.lstsq(A, np.asarray(ys), rcond=None)
    return float(coef[1])


# ==================================================== label layer (exact)
def build_label_layer():
    """The exact incidence layer: canonical form, B, sigma, chi_par --
    v753 recipe on the v738 machinery, all integer/F2, no comb data."""
    L = ram.Lmodule()
    E4 = [tuple((1 if j == k else 0, 0) for j in range(4))
          for k in range(4)]
    Bamb = [L.to_ambient(e) for e in E4]

    def gconj(z):
        return (z[0], -z[1])

    def herm_amb(z, zp):
        s = (0, 0)
        for c in range(4):
            s = ram.gadd(s, ram.gmul(z[c], gconj(zp[c])))
        return s

    H = [[herm_amb(Bamb[k], Bamb[l]) for l in range(4)]
         for k in range(4)]
    div4 = all(H[k][l][0] % 4 == 0 and H[k][l][1] % 4 == 0
               for k in range(4) for l in range(4))
    G = [[(H[k][l][0] // 4, H[k][l][1] // 4) for l in range(4)]
         for k in range(4)]
    Gbar = np.array([[ram.par(G[k][l]) for l in range(4)]
                     for k in range(4)], dtype=np.uint8)

    Smat = [L.coords(ram.pack(ram.sig8(ram.unpack(L.to_ambient(
        E4[k]))))) for k in range(4)]
    S2 = np.array([[ram.par(Smat[k][j]) for j in range(4)]
                   for k in range(4)], dtype=np.uint8)

    NZ = [v for v in ram.ALL_V if any(v)]          # 15 labels, frozen

    def bform(x, y):
        return int(sum(x[k] * int(Gbar[k, l]) * y[l]
                       for k in range(4) for l in range(4))) & 1

    def sigbar(v):
        return tuple(int(sum(v[k] * int(S2[k, j]) for k in range(4)))
                     & 1 for j in range(4))

    def chi_amb(x):
        return ram.unpack(L.to_ambient(x))[0] & 1

    a_par = tuple(chi_amb(E4[k]) for k in range(4))

    def chi(v):
        return int(sum(a * c for a, c in zip(a_par, v))) & 1

    B15 = np.array([[1 if bform(x, y) == 0 else 0 for y in NZ]
                    for x in NZ], dtype=np.int64)
    check("G0.2 label anchors: h = H/4 Z[i]-valued (div-4 exact %s); "
          "B B^T = 4I + 3J exact; B symmetric, diag 1, row sums 7"
          % div4,
          div4
          and np.array_equal(B15 @ B15.T,
                             4 * np.eye(15, dtype=np.int64)
                             + 3 * np.ones((15, 15), np.int64))
          and np.array_equal(B15, B15.T)
          and all(int(B15[i, i]) == 1 for i in range(15))
          and all(int(B15[i].sum()) == 7 for i in range(15)))

    lamB, VB = np.linalg.eigh(B15.astype(float))
    mult = (int(np.sum(np.abs(lamB - 7.0) < 1e-9)),
            int(np.sum(np.abs(lamB - 2.0) < 1e-9)),
            int(np.sum(np.abs(lamB + 2.0) < 1e-9)))
    check("G0.3 incidence spectrum exact: multiplicities (7, +2, -2) "
          "= %s == (1, 9, 5)" % (mult,), mult == (1, 9, 5))

    sidx = [NZ.index(sigbar(v)) for v in NZ]
    fixed = [i for i in range(15) if sidx[i] == i]
    ok3 = all(sidx[sidx[sidx[i]]] == i for i in range(15))
    ok_sym = all(bform(sigbar(x), sigbar(y)) == bform(x, y)
                 for x in NZ for y in NZ)
    check("G0.4 sigma on labels: order 3, 3 fixed + 4 three-orbits, "
          "symplectic for hbar (all 225 pairs)",
          ok3 and len(fixed) == 3 and ok_sym)

    chi_vec = np.array([chi(v) for v in NZ], dtype=np.int64)
    ok_chi = (int(np.sum(chi_vec == 0)) == 7
              and int(np.sum(chi_vec == 1)) == 8
              and all(chi(sigbar(v)) == chi(v) for v in NZ))
    y0 = [i for i, y in enumerate(NZ)
          if all(bform(x, y) == chi(x) for x in NZ)]
    check("G0.5 NS/R bit: chi_par has 7 zeros + 8 ones on the labels, "
          "sigma-invariant; chi = hbar(., y0) for a UNIQUE sigma-fixed "
          "y0 (index %s)" % y0,
          ok_chi and len(y0) == 1 and y0[0] in fixed)

    # canonicity census: 64 alternating forms, 28 nondeg, 1 sigma-inv
    forms = []
    pairs = [(i, j) for i in range(4) for j in range(i + 1, 4)]
    for bits in range(64):
        Mf = np.zeros((4, 4), dtype=np.uint8)
        for b, (i, j) in enumerate(pairs):
            if (bits >> b) & 1:
                Mf[i, j] = Mf[j, i] = 1
        cols = [tuple(int(Mf[i, j]) for i in range(4))
                for j in range(4)]
        rk, _k, _i = ram.f2_rank_ker_inv(cols)
        if rk == 4:
            forms.append(Mf)
    sig_inv = [Mf for Mf in forms
               if np.array_equal((S2 @ Mf @ S2.T) % 2, Mf)]
    is_canon = (len(sig_inv) == 1
                and np.array_equal(sig_inv[0], Gbar))
    check("G0.6 canonicity census: 64 alternating forms, %d "
          "nondegenerate, %d sigma-invariant; the unique invariant "
          "form IS the canonical hbar: %s"
          % (len(forms), len(sig_inv), is_canon),
          len(forms) == 28 and is_canon)
    wrong_forms = [Mf for Mf in forms
                   if not np.array_equal(Mf, Gbar)]

    return dict(NZ=NZ, B15=B15, lamB=lamB, VB=VB, sidx=sidx,
                fixed=fixed, chi_vec=chi_vec, y0=y0[0],
                bform=bform, sigbar=sigbar, S2=S2, Gbar=Gbar,
                wrong_forms=wrong_forms)


def build_candidates(lab):
    """The three frozen candidate subspaces (orthonormal 15x6)."""
    NZ, B15 = lab["NZ"], lab["B15"]
    lamB, VB = lab["lamB"], lab["VB"]
    ones = np.ones(15) / math.sqrt(15.0)
    Vm2 = VB[:, np.abs(lamB + 2.0) < 1e-9]           # 5 cols
    C1 = np.column_stack([ones, Vm2])
    dev1 = float(np.max(np.abs(C1.T @ C1 - np.eye(6))))

    fixed = lab["fixed"]
    cols2 = []
    for i in fixed:
        e = np.zeros(15)
        e[i] = 1.0
        cols2.append(e)
        h = np.zeros(15)
        for j in range(15):
            if j != i and B15[j, i] == 1:
                h[j] = 1.0
        cols2.append(h / math.sqrt(6.0))
    C2raw = np.column_stack(cols2)
    Q2, R2 = np.linalg.qr(C2raw)
    rank2 = int(np.sum(np.abs(np.diag(R2)) > 1e-10))
    C2 = Q2[:, :6]

    sidx = lab["sidx"]
    orbits, seen = [], set()
    for i in range(15):
        if i in seen or sidx[i] == i:
            continue
        o = (i, sidx[i], sidx[sidx[i]])
        seen |= set(o)
        orbits.append(o)
    sel = []
    for o in orbits:
        xor = tuple((NZ[o[0]][k] + NZ[o[1]][k] + NZ[o[2]][k]) & 1
                    for k in range(4))
        if any(xor):
            sel.append(o)
    cols3 = []
    for (a, b, c) in sel:
        u1 = np.zeros(15)
        u1[a], u1[b] = 1.0, -1.0
        u2 = np.zeros(15)
        u2[a], u2[b], u2[c] = 1.0, 1.0, -2.0
        cols3.append(u1 / math.sqrt(2.0))
        cols3.append(u2 / math.sqrt(6.0))
    C3 = np.column_stack(cols3)
    dev3 = float(np.max(np.abs(C3.T @ C3 - np.eye(6))))
    check("G0.7 candidate construction: C1 orthonormal (dev %.1e); "
          "C2 rank %d == 6 (3 fixed labels x point/hyperplane); C3 "
          "from %d moved orbits with nonzero orbit-sum == 3, "
          "orthonormal (dev %.1e)"
          % (dev1, rank2, len(sel), dev3),
          dev1 <= 1e-12 and rank2 == 6 and len(sel) == 3
          and dev3 <= 1e-12)
    return dict(C1=C1, C2=C2, C3=C3)


def sigma_character(lab, V):
    """(commutation dev, n_fix, n_pair, sharp) of a candidate frame."""
    sidx = lab["sidx"]
    Ps = np.zeros((15, 15))
    for i, j in enumerate(sidx):
        Ps[j, i] = 1.0
    P = V @ V.T
    comm = float(np.max(np.abs(Ps @ P - P @ Ps)))
    Pfix = (np.eye(15) + Ps + Ps @ Ps) / 3.0
    n_fix = float(np.trace(P @ Pfix))
    n_pair = (V.shape[1] - n_fix) / 2.0
    sharp = (comm <= TOL_SHARP
             and abs(n_fix - round(n_fix)) <= TOL_SHARP
             and abs(n_pair - round(n_pair)) <= TOL_SHARP)
    return comm, n_fix, n_pair, sharp


def character_table(lab, cands):
    """Exact label-side character data per candidate + gate A1."""
    print("\n-- label-side character table (exact; sigma is GATED, "
          "deck/pole/B contents reported -- the scalar window is "
          "sigma-blind, so sigma is where wrong forms/labelings die)")
    chi_vec = lab["chi_vec"].astype(float)
    Pi0 = np.ones((15, 15)) / 15.0
    lamB, VB = lab["lamB"], lab["VB"]
    P7 = VB[:, np.abs(lamB - 7.0) < 1e-9]
    P2 = VB[:, np.abs(lamB - 2.0) < 1e-9]
    Pm2 = VB[:, np.abs(lamB + 2.0) < 1e-9]
    a1 = {}
    for nm in ("C1", "C2", "C3"):
        V = cands[nm]
        comm, n_fix, n_pair, sharp = sigma_character(lab, V)
        P = V @ V.T
        deck = float(np.trace(P @ np.diag(chi_vec)))
        pole = float(np.trace(P @ Pi0))
        b7 = float(np.linalg.norm(P7.T @ V) ** 2)
        b2 = float(np.linalg.norm(P2.T @ V) ** 2)
        bm2 = float(np.linalg.norm(Pm2.T @ V) ** 2)
        print("  %s: sigma comm dev %.1e, n_fix = %.6f, n_pair = "
              "%.6f; deck(chi_par) content = %.4f; pole(Pi0) content "
              "= %.4f; B-spectral content (7/+2/-2) = "
              "%.4f/%.4f/%.4f (reported)"
              % (nm, comm, n_fix, n_pair, deck, pole, b7, b2, bm2))
        a1[nm] = gate("A1.%s sigma sharpness: candidate is sigma-"
                      "invariant with integer multiplicities "
                      "(n_fix = %d, n_pair = %d)"
                      % (nm, round(n_fix), round(n_pair)), sharp)
    return a1


def freeze_spec(lab, cands):
    hsh = hashlib.sha256()
    hsh.update(("qf-representation-census spec: D=%.10f cap=%d "
                "M_TOP=%d NK_LAD=%s LAST5=%s HALF2=%s thr=%g rob=%s "
                "deep=%g; A1 tol=%g; A2 pred=%s; A3 pred=%s dom=%g "
                "major=%d/5; B level=%g slope=%g margin=%g; L1=pole-"
                "top+ro-neg5, L2=levels%s x (min,max), L3=sp-neg6; "
                "repro count=%d minrungs=%d align=%g; wards comb=%g "
                "prefix=%g add=%g kms=%g sandwich=%g bound=%g "
                "runtime=%g; controls: 27 forms all-fail-A1, perms "
                "n=%d seed=%d, CS seed=%d M=%d, CE cap=%d M=%d"
                % (D, ATOM_MAX_EXT, M_TOP, NK_LAD, LAST5, HALF2,
                   THR_NULL, THR_ROB, THR_DEEP, TOL_SHARP,
                   sorted(PRED_RO_DOM.items()),
                   sorted(PRED_POLE.items()), POLE_DOM, A_MAJOR,
                   D_LEVEL, D_SLOPE, D_MARGIN, RO_LEVELS_C2,
                   REPRO_COUNT, REPRO_MIN_RUNGS, ALIGN_BAR,
                   COMB_DEV_BAR, PREFIX_WARD, ADD_WARD, KMS_TOL,
                   SANDWICH_TOL, BOUND_TOL, RUNTIME_CAP, N_PERMS,
                   SEED_PERM, SEED, M_CTRL, EP_NCAP,
                   EP_MMAX)).encode())
    hsh.update(lab["B15"].tobytes())
    hsh.update(lab["chi_vec"].tobytes())
    hsh.update(np.array(lab["sidx"], dtype=np.int64).tobytes())
    for nm in ("C1", "C2", "C3"):
        hsh.update(nm.encode())
        hsh.update(cands[nm].tobytes())
    return hsh.hexdigest()


# ================================================ label-side controls
def control_forms(lab):
    print("\n-- CF control: the 27 other nondegenerate alternating "
          "forms (wrong hyperplane systems must fail A1)")
    NZ = lab["NZ"]
    S2 = lab["S2"]
    Vm2_true = lab["VB"][:, np.abs(lab["lamB"] + 2.0) < 1e-9]
    n_fail = 0
    n_comm = 0
    orbits = 0
    seen = set()
    min_angles = []
    for Mf in lab["wrong_forms"]:
        key = Mf.tobytes()
        if key not in seen:
            o = {key}
            cur = Mf
            for _ in range(2):
                cur = (S2 @ cur @ S2.T) % 2
                o.add(cur.tobytes())
            seen |= o
            orbits += 1
        Bw = np.array([[1 if int(sum(x[k] * int(Mf[k, l]) * y[l]
                                     for k in range(4)
                                     for l in range(4))) % 2 == 0
                        else 0 for y in NZ] for x in NZ], float)
        lw, Vw = np.linalg.eigh(Bw)
        Vm2w = Vw[:, np.abs(lw + 2.0) < 1e-9]
        Cw = np.column_stack([np.ones(15) / math.sqrt(15.0), Vm2w])
        comm, n_fix, n_pair, sharp = sigma_character(lab, Cw)
        if not sharp:
            n_fail += 1
            if comm > TOL_SHARP:
                n_comm += 1
        sv = np.linalg.svd(Vm2w.T @ Vm2_true, compute_uv=False)
        min_angles.append(float(np.min(sv)))
    check("CF wrong-form census fires: %d/27 wrong-form candidates "
          "fail A1 sigma sharpness (%d by non-commutation); sigma "
          "orbits among the 27: %d; E'_{-2} vs true E_{-2} smallest "
          "principal cosine range %.3f..%.3f (genuinely different "
          "spaces)"
          % (n_fail, n_comm, orbits, min(min_angles),
             max(min_angles)),
          n_fail == 27)


def control_perms(lab, cands):
    print("\n-- CP control: wrong labelings (frozen permutations)")
    rng = np.random.default_rng(SEED_PERM)
    n_fail = 0
    for k in range(N_PERMS):
        perm = rng.permutation(15)
        Cp = cands["C1"][perm, :]
        _c, _f, _p, sharp = sigma_character(lab, Cp)
        if not sharp:
            n_fail += 1
    check("CP wrong-labeling control fires: %d/%d frozen label "
          "permutations of C1 fail A1 sigma sharpness"
          % (n_fail, N_PERMS), n_fail == N_PERMS)


# ==================================================== comb + towers
def build_extended_comb():
    lam_ext = core.von_mangoldt_table(ATOM_MAX_EXT)
    dev = float(np.max(np.abs(lam_ext[:core.ATOM_MAX + 1]
                              - core.LAM_TAB)))
    check("G1.1 extended-table overlap: extended von Mangoldt table "
          "== deployed core table on [0, %d] EXACTLY"
          % core.ATOM_MAX, dev == 0.0, "max abs dev %.1e" % dev)
    nn = np.nonzero(lam_ext > 0.0)[0]
    u_ext = np.log(nn.astype(float))
    mu_ext = 2.0 * lam_ext[nn] / np.sqrt(nn.astype(float))
    psi = np.cumsum(lam_ext[nn])
    keep = nn.astype(float) >= core.KAPPA_X0
    kappa = float(np.max(np.abs(psi[keep] - nn[keep].astype(float))
                         / nn[keep].astype(float)))
    check("G1.2 extended-range Chebyshev envelope: kappa = %.6f <= "
          "KAPPA_REF + %.0e = %.6f"
          % (kappa, core.TOL_KAPPA, core.KAPPA_REF + core.TOL_KAPPA),
          kappa <= core.KAPPA_REF + core.TOL_KAPPA)

    base = np.rint(np.exp(lam_ext[nn])).astype(np.int64)
    mexp = np.rint(u_ext / math.log(2.0)).astype(np.int64)
    is2 = base == 2
    masks = dict(ro=np.nonzero(is2 & (mexp % 2 == 1))[0],
                 re=np.nonzero(is2 & (mexp % 2 == 0))[0],
                 sp=np.nonzero(~is2 & (base % 4 == 1))[0],
                 iq=np.nonzero(~is2 & (base % 4 == 3))[0])
    return nn, u_ext, mu_ext, masks


def build_parent_tower():
    alpha = 0.5 * M_PAR * D
    ka, masks_par, dev_m = srp.channel_masks(alpha)
    check("G1.3 parent tower comb consistency (zeta-free Gauss double "
          "sieve == deployed masses, rel dev <= %.0e)" % COMB_DEV_BAR,
          dev_m <= COMB_DEV_BAR,
          "rel dev %.1e, ka=%d atoms to e^%.4f"
          % (dev_m, ka, 2.0 * alpha))
    c = srp.continuum_lags(M_PAR)
    for cnl in ("ro", "re", "sp", "in"):
        c = c + srp.atom_channel_lags(alpha, M_PAR, masks_par[cnl])
    return sla.toeplitz(c[:M_PAR]), ka, masks_par


def build_extended_tower(nn, u_ext, mu_ext, masks, T_par, ka_par,
                         masks_par):
    alpha = 0.5 * M_TOP * D
    ka = int(np.searchsorted(u_ext, 2.0 * alpha + 1.0e-14,
                             side="right"))
    # channel split consistency vs srp on the parent prefix
    dev_ch = 0
    par_map = {"ro": "ro", "re": "re", "sp": "sp", "iq": "in"}
    for c_ext, c_par in par_map.items():
        mine = set(int(nn[i]) for i in masks[c_ext] if i < ka_par)
        theirs = set(int(round(math.exp(float(core.U_ALL[i]))))
                     for i in masks_par[c_par])
        dev_ch += len(mine.symmetric_difference(theirs))
    check("G1.4 sigma-descended channel split: extended ro/re/sp/in "
          "classification == srp.channel_masks on the parent prefix "
          "(symmetric difference %d == 0)" % dev_ch, dev_ch == 0)

    c_arch = core.arch_lags(M_TOP, D)
    c_pole = stage2.pole_lags_closed(M_TOP, D)
    sec = {}
    for cnl, idx in masks.items():
        idx_in = idx[idx < ka]
        sec[cnl], _dd = core.atom_lags_at(alpha, M_TOP, u_ext[idx_in],
                                          mu_ext[idx_in])
    c_at_all, _dd = core.atom_lags_at(alpha, M_TOP, u_ext[:ka],
                                      mu_ext[:ka])
    dev_add = float(np.max(np.abs(sec["ro"] + sec["re"] + sec["sp"]
                                  + sec["iq"] - c_at_all)))
    check("G1.5 sector additivity: ro + re + sp + in lags == total "
          "atom lags (max abs dev %.1e <= %.0e)"
          % (dev_add, ADD_WARD), dev_add <= ADD_WARD)

    c_full = c_arch + c_pole + c_at_all
    T = sla.toeplitz(c_full[:M_TOP])
    dev_pre = float(np.max(np.abs(T[:M_PAR, :M_PAR] - T_par)))
    check("G1.6 prefix Ward: extended tower leading %d x %d block == "
          "parent tower, max abs dev %.1e <= %.0e"
          % (M_PAR, M_PAR, dev_pre, PREFIX_WARD),
          dev_pre <= PREFIX_WARD)
    print("  extension census: ka = %d atoms to e^%.4f" % (ka,
                                                           2 * alpha))

    # KMS half-weight guard on the ramified masses
    ram_idx = np.concatenate([masks["ro"], masks["re"]])
    ram_idx = ram_idx[ram_idx < ka]
    mm = np.rint(u_ext[ram_idx] / math.log(2.0))
    dev_kms = float(np.max(np.abs(mu_ext[ram_idx] * 2.0 ** (mm / 2.0)
                                  / (2.0 * math.log(2.0)) - 1.0)))
    check("G1.7 KMS half-weight guard (exact): the deployed ramified "
          "masses ARE the v756 half-weights, "
          "max |mu_m 2^{m/2} / (2 ln 2) - 1| = %.1e <= %.0e over %d "
          "ram atoms" % (dev_kms, KMS_TOL, len(ram_idx)),
          dev_kms <= KMS_TOL)

    # single-atom ram level lag vectors (m = 1..N_RAM_LEV)
    lev = {}
    for m in range(1, N_RAM_LEV + 1):
        i = np.searchsorted(nn, 2 ** m)
        if i >= len(nn) or nn[i] != 2 ** m or u_ext[i] > 2 * alpha:
            continue
        lev[m], _dd = core.atom_lags_at(alpha, M_TOP,
                                        u_ext[i:i + 1],
                                        mu_ext[i:i + 1])
    dev_lev = float(np.max(np.abs(sum(lev.values())
                                  - (sec["ro"] + sec["re"]))))
    check("G1.8 level additivity: sum of %d single-level ram lags == "
          "ro + re sector lags (max abs dev %.1e <= %.0e)"
          % (len(lev), dev_lev, ADD_WARD), dev_lev <= ADD_WARD)
    return dict(T=T, alpha=alpha, ka=ka, c_arch=c_arch,
                c_pole=c_pole, sec=sec, lev=lev, c_full=c_full)


# ==================================================== spectral census
def spectral_census(tw):
    """Per NK_LAD rung: near-kernel, lift frames, principal angles,
    per-mode deck/pole classification."""
    T = tw["T"]
    Tsec = {c: sla.toeplitz(tw["sec"][c][:M_TOP])
            for c in ("ro", "re", "sp", "iq")}
    Tpole = sla.toeplitz(tw["c_pole"][:M_TOP])
    Tlev = {m: sla.toeplitz(v[:M_TOP]) for m, v in tw["lev"].items()}

    out = []
    prev_blk = None
    aligns = []
    cos2_max = -np.inf
    for M in NK_LAD:
        lam, V = np.linalg.eigh(T[:M, :M])
        idx = np.nonzero(lam <= THR_NULL)[0]
        VN = V[:, idx]
        nn_c = len(idx)
        blk = dict(M=M, lam0=float(lam[0]), nn=nn_c,
                   nn_deep=int(np.sum(lam <= THR_DEEP)),
                   lam_null=lam[idx].copy(), VN=VN)

        # lift frames (source sector data only)
        lam_p, V_p = np.linalg.eigh(Tpole[:M, :M])
        w_pole = V_p[:, -1]
        lam_r, V_r = np.linalg.eigh(Tsec["ro"][:M, :M])
        L1raw = np.column_stack([w_pole, V_r[:, :5]])
        cols2 = []
        for m in RO_LEVELS_C2:
            lm, Vm = np.linalg.eigh(Tlev[m][:M, :M])
            cols2 += [Vm[:, 0], Vm[:, -1]]
        L2raw = np.column_stack(cols2)
        lam_s, V_s = np.linalg.eigh(Tsec["sp"][:M, :M])
        L3raw = np.column_stack([V_s[:, :6]])
        frames = {}
        for nm, raw in (("C1", L1raw), ("C2", L2raw), ("C3", L3raw)):
            Q, R = np.linalg.qr(raw)
            frames[nm] = Q[:, :6]
            blk["rank_" + nm] = int(np.sum(np.abs(np.diag(R))
                                           > 1e-10))

        # six principal angles + D_X per candidate
        for nm in ("C1", "C2", "C3"):
            sv = np.linalg.svd(VN.T @ frames[nm], compute_uv=False)
            sv = np.clip(sv, 0.0, 1.0)
            cos2_max = max(cos2_max, float(np.max(sv)) ** 2)
            blk["cos_" + nm] = sv
            blk["D_" + nm] = (float(math.sqrt(1.0 - sv[-1] ** 2))
                              if nn_c == 6 else None)

        # per-mode deck (ro-dominance) + pole classification
        ro_dom = 0
        pole_dom = 0
        pairs = []
        for j in range(nn_c):
            v = VN[:, j]
            pr = {c: float(v @ Tsec[c][:M, :M] @ v)
                  for c in ("ro", "re", "sp", "iq")}
            po2 = float(np.dot(w_pole, v)) ** 2
            if abs(pr["ro"]) > (abs(pr["re"]) + abs(pr["sp"])
                                + abs(pr["iq"])):
                ro_dom += 1
            if po2 > POLE_DOM:
                pole_dom += 1
            pairs.append((pr, po2))
        blk["ro_dom"] = ro_dom
        blk["pole_dom"] = pole_dom
        blk["pairs"] = pairs
        blk["w_pole"] = w_pole

        if prev_blk is not None and prev_blk["nn"] > 0 and nn_c > 0:
            Vp = np.zeros((M, prev_blk["nn"]))
            Vp[:prev_blk["M"]] = prev_blk["VN"]
            aligns.append(float(np.sum((VN.T @ Vp) ** 2)
                                / prev_blk["nn"]))
        prev_blk = blk
        out.append(blk)

    check("G2.4 boundedness audit: every principal cosine^2 in "
          "[0, 1 + %.0e] (max %.6f) -- bounded overlaps of "
          "orthonormal frames, no 1/eps anywhere"
          % (BOUND_TOL, cos2_max), cos2_max <= 1.0 + BOUND_TOL)
    return out, aligns, Tsec, Tlev, Tpole


def guards_on_census(spec, aligns):
    nns = [b["nn"] for b in spec]
    n6 = sum(1 for n in nns if n == REPRO_COUNT)
    last5_ok = all(spec[NK_LAD.index(M)]["nn"] == REPRO_COUNT
                   for M in LAST5)
    deep_ok = all(spec[NK_LAD.index(M)]["nn_deep"] == 1
                  for M in LAST5)
    print("  near-null count along NK_LAD: %s"
          % "/".join(str(n) for n in nns))
    print("  deep count (lam <= %g): %s"
          % (THR_DEEP, "/".join(str(b["nn_deep"]) for b in spec)))
    print("  PD margins (measured, never gated): lambda_min = %.3e "
          "(M %d) -> %.3e (M %d)"
          % (spec[0]["lam0"], NK_LAD[0], spec[-1]["lam0"], NK_LAD[-1]))
    check("G2.1 near-kernel reproduction Ward: count == %d on %d/%d "
          "rungs (>= %d) and on all LAST5; deep count == 1 on LAST5"
          % (REPRO_COUNT, n6, len(NK_LAD), REPRO_MIN_RUNGS),
          n6 >= REPRO_MIN_RUNGS and last5_ok and deep_ok)
    a4 = aligns[-4:]
    mean_a4 = float(np.mean(a4)) if len(a4) == 4 else -1.0
    check("G2.2 near-kernel stability: mean consecutive subspace "
          "alignment last 4 = %.6f >= %g (parent formula verbatim)"
          % (mean_a4, ALIGN_BAR), mean_a4 >= ALIGN_BAR)
    print("  threshold robustness (reported, never gated): counts at "
          "%s on M = %d given in the mode-report section"
          % (THR_ROB, spec[-1]["M"]))


# ==================================================== gates + tables
def angle_tables(spec):
    print("\n-- principal-angle tables (six cosines per candidate "
          "and rung; D_X = ||P^(6) - P^(cand)||_2 = sin theta_max)")
    for nm in ("C1", "C2", "C3"):
        print("  candidate %s (lift %s):"
              % (nm, dict(C1="pole-top + ro-neg5",
                          C2="levels (1,3,5) x (min,max)",
                          C3="sp-neg6")[nm]))
        for b in spec:
            cs = "/".join("%.3f" % c for c in b["cos_" + nm])
            dd = ("%.4f" % b["D_" + nm]) if b["D_" + nm] is not None \
                else "-"
            print("    M=%3d X=%.4f nn=%d cos=[%s] D=%s"
                  % (b["M"], b["M"] * D, b["nn"], cs, dd))


def rate_gates(spec, a1):
    xs = np.array([b["M"] * D for b in spec])
    results = {}
    med5 = {}
    for nm in ("C1", "C2", "C3"):
        ds = [b["D_" + nm] for b in spec]
        d_l5 = [d for b, d in zip(spec, ds)
                if b["M"] in LAST5 and d is not None]
        d_h2 = [(x, d) for x, b, d in zip(xs, spec, ds)
                if b["M"] in HALF2 and d is not None]
        med = float(np.median(d_l5)) if d_l5 else 1.0
        slope = lin_slope(np.array([x for x, _d in d_h2]),
                          [d for _x, d in d_h2]) if len(d_h2) >= 3 \
            else np.inf
        med5[nm] = med
        ok_b = gate("B.%s rate: LAST5-median D = %.4f <= %g AND "
                    "second-half slope = %+.4f/X <= +%g"
                    % (nm, med, D_LEVEL, slope, D_SLOPE),
                    med <= D_LEVEL and slope <= D_SLOPE)
        # A2 / A3 multiplicity gates
        ro_counts = [spec[NK_LAD.index(M)]["ro_dom"] for M in LAST5]
        po_counts = [spec[NK_LAD.index(M)]["pole_dom"] for M in LAST5]
        n_ro = sum(1 for c in ro_counts if c == PRED_RO_DOM[nm])
        n_po = sum(1 for c in po_counts if c == PRED_POLE[nm])
        ok_a2 = gate("A2.%s deck/NS-R multiplicity: measured "
                     "ro-dominant count %s vs predicted %d -- match "
                     "on %d/5 LAST5 rungs (>= %d)"
                     % (nm, ro_counts, PRED_RO_DOM[nm], n_ro,
                        A_MAJOR), n_ro >= A_MAJOR)
        ok_a3 = gate("A3.%s pole multiplicity: measured pole-dominant"
                     " count %s vs predicted %d -- match on %d/5 "
                     "LAST5 rungs (>= %d)"
                     % (nm, po_counts, PRED_POLE[nm], n_po, A_MAJOR),
                     n_po >= A_MAJOR)
        results[nm] = a1[nm] and ok_a2 and ok_a3 and ok_b
    return results, med5


def mode_reports(spec, tw, Tsec, Tlev, Tpole):
    top = spec[-1]
    M = top["M"]
    T = tw["T"]
    lam, V = np.linalg.eigh(T[:M, :M])
    for thr in THR_ROB:
        print("  near-null count at thr %g (M=%d): %d (reported)"
              % (thr, M, int(np.sum(lam <= thr))))
    Tar = sla.toeplitz(tw["c_arch"][:M])
    print("\n-- mode table at M = %d (reported): eigenvalue, pole "
          "overlap^2, channel pairings (arch/pole/ro/re/sp/in)" % M)
    for j in range(top["nn"]):
        v = top["VN"][:, j]
        pr, po2 = top["pairs"][j]
        a = float(v @ Tar @ v)
        p = float(v @ Tpole[:M, :M] @ v)
        print("    mode %d: lam = %.3e  pole^2 = %.4f  arch %+.2e  "
              "pole %+.2e  ro %+.2e  re %+.2e  sp %+.2e  in %+.2e"
              % (j, top["lam_null"][j], po2, a, p, pr["ro"],
                 pr["re"], pr["sp"], pr["iq"]))
    print("  KMS level profiles q_m = v^T T^(m) v (m = 1..10, "
          "reported; half-weight reference 2^{-m}):")
    for j in range(top["nn"]):
        v = top["VN"][:, j]
        qs = []
        for m in range(1, 11):
            if m in Tlev:
                qs.append("%+.1e" % float(v @ Tlev[m][:M, :M] @ v))
        print("    mode %d: %s" % (j, "  ".join(qs)))

    # deck-flip report (T - 2 T_ro) at the top rung
    Tf = T[:M, :M] - 2.0 * Tsec["ro"][:M, :M]
    lam_f, V_f = np.linalg.eigh(Tf)
    nn_f = int(np.sum(lam_f <= THR_NULL))
    neg_f = int(np.sum(lam_f < -THR_NULL))
    if nn_f > 0:
        sv = np.linalg.svd(top["VN"].T @ V_f[:, lam_f <= THR_NULL],
                           compute_uv=False)
        cs = "/".join("%.3f" % c for c in sv[:6])
    else:
        cs = "-"
    print("  deck-flip report (T - 2 T_ro, reported not gated): "
          "near-null count %d, negative count %d, principal cosines "
          "vs N = [%s]" % (nn_f, neg_f, cs))


# ==================================================== source controls
def run_source_controls(tw, u_ext, mu_ext):
    print("\n-- CS/CE controls (must fire: indefinite sources destroy "
          "the near-kernel reading; parent fire rule verbatim)")
    bats = {R: hbp.battery(R) for R in (1.0, 2.0)}
    rng = np.random.default_rng(SEED)
    ka = tw["ka"]
    pos = np.sort(rng.uniform(0.5, 2.0 * tw["alpha"], ka))
    cat_s, _dd = core.atom_lags_at(tw["alpha"], M_TOP, pos,
                                   mu_ext[:ka])
    Ts = sla.toeplitz((tw["c_arch"] + tw["c_pole"] + cat_s)[:M_TOP])
    lam_s = np.linalg.eigvalsh(Ts[:M_CTRL, :M_CTRL])
    print("  CS census: %d/%d eigenvalues below -THR_NULL = -%g "
          "(near-kernel reading destroyed)"
          % (int(np.sum(lam_s < -THR_NULL)), M_CTRL, THR_NULL))
    fire_s, det_s = yhp.control_yosida(Ts, bats, "scramble")
    check("CS position-scramble control (extended comb, %d atoms) "
          "fires" % ka, fire_s, det_s)

    r1 = epx.lattice_r1(EP_NCAP)
    bb = np.asarray(r1, float) / 2.0
    lamE = epx.dirichlet_vonmangoldt(bb, EP_NCAP)
    supp = np.nonzero(np.abs(lamE) > 1.0e-9)[0]
    supp = supp[supp >= 2]
    posE = np.log(supp.astype(float))
    masE = 2.0 * lamE[supp] / np.sqrt(supp.astype(float))
    catE, _dd = core.atom_lags_at(0.5 * EP_MMAX * D, EP_MMAX, posE,
                                  masE)
    cont = srp.continuum_lags(EP_MMAX)
    TE = sla.toeplitz((cont + catE)[:EP_MMAX])
    lam_e = np.linalg.eigvalsh(TE[:M_CTRL, :M_CTRL])
    print("  CE census: %d/%d eigenvalues below -THR_NULL = -%g"
          % (int(np.sum(lam_e < -THR_NULL)), M_CTRL, THR_NULL))
    fire_e, det_e = yhp.control_yosida(TE, bats, "epstein")
    check("CE Epstein control (x^2+5y^2, %d negative atom sites) "
          "fires" % int(np.sum(lamE[2:] < -1.0e-9)), fire_e, det_e)


# ==================================================== run
def run():
    print("=" * 78)
    print("QF OFFENSIVE strand 2 -- representation census of the "
          "6-dim near-kernel")
    print("(is E_qf the canonical E8 defect space E_7 (+) E_{-2}?)")
    print("=" * 78)

    hits = ast_firewall()
    check("G0.1 AST firewall", not hits, str(hits))

    # ---- label layer + candidates (exact, no comb data)
    lab = build_label_layer()
    cands = build_candidates(lab)
    a1 = character_table(lab, cands)

    # ---- freeze BEFORE any comb / near-kernel data
    sha = freeze_spec(lab, cands)
    check("G0.8 candidate battery + lifts + ladders + bars "
          "SHA-256-frozen BEFORE any comb data is built",
          True, "SHA256 %s..." % sha[:16])
    check("G0.9 reach census: M_TOP = %d <= floor(64 ln %d) = %d; "
          "sieve cover exp(X_top) + 2 = %d <= %d; runtime cap %.0f s"
          % (M_TOP, ATOM_MAX_EXT, M_CAP_EXT,
             int(math.exp(M_TOP * D)) + 2, ATOM_MAX_EXT, RUNTIME_CAP),
          M_TOP <= M_CAP_EXT
          and int(math.exp(M_TOP * D)) + 2 <= ATOM_MAX_EXT)

    # ---- label-side controls (no comb data either)
    control_forms(lab)
    control_perms(lab, cands)

    # ---- comb + towers strictly after the freeze
    nn, u_ext, mu_ext, masks = build_extended_comb()
    T_par, ka_par, masks_par = build_parent_tower()
    tw = build_extended_tower(nn, u_ext, mu_ext, masks, T_par,
                              ka_par, masks_par)

    # PD sandwich at control + top rung (measured, never assumed)
    gmin, gmax = np.inf, -np.inf
    for M in (M_CTRL, M_TOP):
        lam = np.linalg.eigvalsh(tw["T"][:M, :M])
        for e in yhp.EPS_LADDER:
            g = lam / (lam + e)
            gmin = min(gmin, float(np.min(g)))
            gmax = max(gmax, float(np.max(g)))
    check("G2.3 real-data operator sandwich at M = %d and %d: all "
          "Yosida eigenvalues in [%.1e, 1 - %.1e] (bars -%.0e / "
          "1+%.0e)" % (M_CTRL, M_TOP, gmin, 1.0 - gmax, SANDWICH_TOL,
                       SANDWICH_TOL),
          gmin >= -SANDWICH_TOL and gmax <= 1.0 + SANDWICH_TOL)

    # ---- spectral census (near-kernel first computed HERE)
    spec, aligns, Tsec, Tlev, Tpole = spectral_census(tw)
    guards_on_census(spec, aligns)
    angle_tables(spec)
    results, med5 = rate_gates(spec, a1)
    mode_reports(spec, tw, Tsec, Tlev, Tpole)

    # ---- source controls
    run_source_controls(tw, u_ext, mu_ext)

    dt = time.time() - T_START
    check("G3.1 runtime %.1f s <= predeclared cap %.0f s"
          % (dt, RUNTIME_CAP), dt <= RUNTIME_CAP)

    # ---- verdict (preregistered rules)
    guards_ok = all(ok for (n, ok) in CHECKS
                    if not n.startswith(("CF", "CP", "CS", "CE")))
    controls_ok = all(ok for (n, ok) in CHECKS
                      if n.startswith(("CF", "CP", "CS", "CE")))

    def others_beaten(win):
        for o in ("C1", "C2", "C3"):
            if o == win:
                continue
            if results[o] and med5[o] < med5[win] + D_MARGIN:
                return False
        return True

    if not (guards_ok and controls_ok):
        verdict = "QF-CENSUS-INVALID"
    elif results["C1"] and others_beaten("C1"):
        verdict = "QF-IS-INCIDENCE-DEFECT"
    elif results["C2"] and others_beaten("C2"):
        verdict = "QF-CANDIDATE-C2"
    elif results["C3"] and others_beaten("C3"):
        verdict = "QF-CANDIDATE-C3"
    else:
        verdict = "QF-REPRESENTATION-OPEN"

    n_gate = sum(1 for (_n, ok) in GATES if ok)
    n_chk = sum(1 for (_n, ok) in CHECKS if ok)
    print("\nVERDICT: %s" % verdict)
    print("GATES %d/%d, GUARDS+CONTROLS %d/%d, LAST5-median D: "
          "C1 = %.4f, C2 = %.4f, C3 = %.4f, runtime %.1f s"
          % (n_gate, len(GATES), n_chk, len(CHECKS), med5["C1"],
             med5["C2"], med5["C3"], time.time() - T_START))
    if verdict == "QF-IS-INCIDENCE-DEFECT":
        print("CONSEQUENCE: the 6-dim near-kernel carries the "
              "predeclared window signature of E_7 (+) E_{-2} (pole "
              "mode + 5 ro-dominant defect modes) with the frozen "
              "angle rate, and only the canonical sigma-invariant "
              "form survives the census -- the boundary-triple route "
              "gets its geometry fixed by projective Hamming.  NOT "
              "claimed: a literal rank-6 embedding of R^15 in the "
              "window (the deployed comb realizes exactly two "
              "V-characters -- documented bottleneck), X -> infinity, "
              "RH.")
    elif verdict in ("QF-CANDIDATE-C2", "QF-CANDIDATE-C3"):
        print("CONSEQUENCE: a non-incidence candidate carries the "
              "measured signature; the E_7 (+) E_{-2} identification "
              "fails honestly on this surface.")
    elif verdict == "QF-REPRESENTATION-OPEN":
        print("CONSEQUENCE: no candidate passes the frozen character "
              "+ rate bars -- the 6 = 1 + 5 dimension match stays "
              "typed DECORATIVE; the near-kernel is not (yet) "
              "identified with the canonical E8 defect space through "
              "any predeclared source-native lift.")
    else:
        print("KILL: a guard failed or a control did not fire -- no "
              "statement about E_qf follows from this run.")
    return 0 if (guards_ok and controls_ok) else 1


if __name__ == "__main__":
    sys.exit(run())
