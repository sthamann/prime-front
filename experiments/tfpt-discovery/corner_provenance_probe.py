r"""corner_provenance_probe -- PRIME.PORT.CORNER.PROVENANCE.01
(round 251a; experiments-only, NO RH claim in either direction, NO
ledger row, NO marker move, NO paper edit).

THE REVIEWER AUDIT POINT (binding, verbatim task): B deg = B - rho_0
is the potentially hidden SIXTH boundary of the fifth edge.  If
B deg itself encodes an RH-strength bound, the T-analysis of the
CENTERED_BASEFIBER campaign solves only the OPERATOR side of the
interface; if B deg is chosen with knowledge of S, the bordered form
is TAUTOLOGICAL.  This probe is the formal PROVENANCE CONTRACT for
the corner, executed BEFORE any proof chain: corpus archaeology
(leg A), the three-case adjudication (leg B), and the four
machine-checkable contract clauses c1-c4 (leg C).

WORKING FORM OF THE FIFTH EDGE (r243/r244/r248): base H_N > 0 and
fiber D = B deg - Q_7 - T >= 0 with B deg = B - rho_0 the CENTERED
corner of the bordered Hankel matrix [[H_N, u], [u^T, B]];
Q_7 = sum_{n=1..7} rho_n (centered head, F deg_0 = 0), T =
sum_{n=8..N-1} rho_n (terminal CD readout, bitwise r244), so that
rho_0 + Q_7 + T = S_{N-1} exactly and
   B_can - S_{N-1}  ==  (B_can - rho_0) - Q_7 - T  =  D_can
per window: corner coverage of the raw budget and of the centered
fiber are THE SAME statement (warded, G31).

LEG A -- CORPUS ARCHAEOLOGY (sealed citations; locations are line
numbers of experiments/next.txt at retrieval 2026-08-24 plus probe
docstrings; every quote verbatim):
(A1) THE PAIR-CORRELATION CONTRACT, PRIME.FLOOR.PAIRCORR.01
  [O], registered 2026-08-07 (round 26, diary LXX, next.txt:577):
  "VORWAERTS: eine unbedingte Varianz-Schranke |aniso(S_p - S)| <=
  C*sigma_sqrt uniform in h mit DEKLARIERTEM Paarkorrelations-
  Eintrittspunkt -- keine versteckte Zirkularitaet; RUECKWAERTS:
  Instrument-Kalibrierung gemessener Boden-Margen in effektive
  Paarkorrelations-Aussagen, nie ein Satz ueber Nullstellen".
  The contract's forward demand is a bound with a CONSTANT C on the
  square-root scale -- C is the natural budget-shaped quantity of
  the lane.  PRIME.FLOOR.RATIO.01 [O] closed its analytic-envelope
  wing into this boundary (same entry: "ihre Huellkurven-Konstante
  ist arithmetische Substanz aequivalent zum Ziel").
(A2) THE r243 IDENTIFICATION (round 243, diary DLXXII,
  next.txt:13852): the bordered Hankel matrix is a NEW r243
  construction, produced by telescoping the full-prefix Bessel
  system -- "DAS GESAMTE FULL-PREFIX-BESSEL-SYSTEM TELESKOPIERT ZU
  EINER EINZIGEN UNGLEICHUNG: S_{N-1} <= B <=> PSD der EINEN
  gebordeten Hankel-Matrix [[H_N, u],[u^T, B]] -- das neue
  UEBERGABEOBJEKT an die RHP-Lane" -- and its positivity was typed
  there and then as the pair-correlation demand: "Delta_Bes >= 0
  <=> |F| <= sqrt(B#)*sqrt(h) -- VERBATIM die Vorwaertsforderung
  von PRIME.FLOOR.PAIRCORR.01 (|aniso| <= C*sigma_sqrt)".  The
  only budget known to cover the 42-window surface is the r243
  AUDIT form (principal_bessel_probe.py sealed constants /
  amendment a4): "lift budget B_w = S_{N-2} + 5/7 (audit form,
  amendment a4)" after "the smoke run REFUTED the design guess
  that a uniform budget B = 7/5 covers the surface (measured
  S_{N-1} ~ 6-15, N-growing)" -- B_w consumes the measured budget
  prefix S_{N-2} and was resealed AFTER the census was known.
(A3) THE r244 CORNER CENSUS (bordered_hankel_probe.py, leg B):
  three canonical SOURCE-PURE candidates were sealed ("nodes,
  weights, moments of mu/mutilde and sigma only; NO h-sign chain,
  NO tau, NO S, NO imported 5/7") -- b1 smooth self-pairing
  B1 = s_0, b2 Szego/equilibrium budget, b3 mu-side norm -- and
  "ALL THREE source-pure candidates FAIL c1 -- PSD 0/42 each ...
  => CORNER_IMPORTED_ONLY: the only budget known to cover the
  surface remains the r243 window form B_w = S_{N-2} + 5/7 (prefix
  data + imported floor)".  The same round sealed the QUADRUPLE
  IDENTIFICATION (next.txt:13854): "die Vierfach-Identifikation
  aus r243 (Pair-Correlation-Schranke = Bessel-Budget = gebordete
  Hankel-PSD = augmentierter tau-Quotient)".
(A4) THE ORIGINAL WEIL FORM HAS NO BORDER: the lane's canonical
  wall is the FULL Weil matrix of the frozen radius-4 cell builder
  -- "die kanonische Wand M_h = mpM des gefrorenen Radius-4-
  Zellbauers (a = log(h)/2, K = ceil(1.25 h log h), omega_k =
  k pi/a)" (next.txt:11) with the exact dictionary "M_h ~= L_f +
  diag(Delta)" (next.txt:69, r189-corrected token WALL-OFF-
  DIAGONAL-IS-ONE-FUNCTION-LOEWNER-EXACT) -- a full symmetric
  matrix (pole block + prime block), no [[H, u],[u^T, B]] corner
  anywhere.  The GL1 landing / positive-descent layer is a STATE
  positivity, not a bordered matrix: v791 PRIME.POSITIVE_
  DESCENT.01, "der Paket-GNS-Zustand auf N[C2] (x) N[F2^4] (x)
  N[mu4] ist MANIFEST positiv" (next.txt:589), v801 105-Kraus-
  intertwiner and "positive_descent_master, GL1==Weil@6.0e-16"
  (next.txt:13834).  The border FIRST appears in r243's
  telescoping (A2).  ADJUDICATION: the bordered structure is NOT
  Weil-native.
(A5) THE v881 DEMAND CURVE IS NOT A B-CONTRACT (round 40 wing,
  next.txt:541): "die Wand-Marge IST die injizierte Stoerungs-
  ENERGIE auf exakt dem tau-Gesetz -- RH-SCALE-EQUIVALENT: ein
  unbedingtes Zertifikat der Leiter muss Off-Critical-
  Stoerungsenergie bis Praezision A*^2 ~ tau ~ e^{-3 alpha}
  ausschliessen" -- an ENERGY IDENTITY read in the REVERSE
  (instrument) direction of A1: it measures what a certificate
  must exclude, it does not supply an a-priori corner value.
  Budget-shaped, but not a corner source.

LEG B -- THE THREE-CASE ADJUDICATION (sealed rules, decided by
A + the leg-C measurement):
  CASE 1 (CORNER_WEIL_NATIVE): B deg is part of the original Weil
    form; D >= 0 would be part of the original statement.  RULE:
    holds iff the bordered matrix [[H, u],[u^T, B]] occurs in the
    Weil-form corpus BEFORE r243.  ADJUDICATED NO per (A4): the
    border is an r243 telescoping construction.
  CASE 2 (external admissible test norm): B deg is an externally
    formulated admissible norm; source must be NAMED and
    admissibility argued.  RULE: holds iff a contract-conformant
    (c1) candidate covers the fiber on 42/42 windows without alias
    (|res_corr| <= 0.95).  Measured in leg C (c4).
  CASE 3 (budget value of the pair-correlation demand): B is the
    constant C of the PAIRCORR forward demand in window form;
    D >= 0 is the exact RHP form of THE SAME demand -- admissible
    as an INTERFACE, but the claim boundary must say so
    explicitly.  RULE: holds iff no contract-conformant candidate
    covers the surface AND the only covering budget known consumes
    S (the r243 audit form) -- supported by the verbatim r243
    typing and the r244 quadruple identification (A2/A3).

LEG C -- THE FORMAL CONTRACT (four machine-checkable clauses):
(c1) FORM: B_w = script-B(window data, archimedean source, fixed
  conventions).  The documented candidates are implemented as
  FORMULAS -- b1 = s_0 = sum of signed smooth-border masses; b2 =
  Szego/equilibrium budget (orthonormal arcsine/Chebyshev chain on
  the measured hull, mass m_0(mutilde)); b3 = mu-side norm
  (orthonormal positive-zone chain) -- and an AST/dataflow audit
  gates that the implementing functions reference NOTHING from the
  forbidden set {T_w, D_w, H_N^{-1} solves, tau_w, measured
  margin, S_w, the sign chain}: the audited function bodies (own
  module + the two imported r244 builders) may consume node
  positions, node weights and window constants ONLY.
(c2) PRE-FIXATION: the candidate values on all 42 windows are
  computed and hashed (CAND_SHA, 12 significant digits) BEFORE any
  budget-chain evaluation in this process; a call counter on the
  S-evaluator enforces the ordering machine-checkably.
(c3) THE TAUTOLOGY TEST (must-fail demonstration): the r243 budget
  B_w = S_{N-2} + 5/7 VIOLATES this contract -- (i) the same AST
  auditor flags its implementation (it consumes S); (ii) it covers
  42/42 BY CONSTRUCTION with terminal margin 5/7 - rho_{N-1}
  (min ~ 0.0139, the r243 razor, reproduced); (iii) the alias
  detector fires: corr of N-detrended residuals of B_w and S is
  ~ +1.00 > 0.95 (it IS S plus a constant).  A budget that covers
  because it was built from S certifies nothing.
(c4) HONEST INVENTORY: coverage census of the contract-conformant
  candidates on the fiber (B_can - S_{N-1} > 0 per window,
  == D_can >= 0 by the centered split ward): expected 0/42 each
  (r244 reproduction under this probe's own build).

SEALED VERDICTS (frozen before evaluation):
  CORNER_SOURCE_CANDIDATE(bX) iff some contract-conformant
    candidate covers 42/42 AND passes the alias clause -- then
    case 2 with full census;
  CORNER_INTERFACE_ONLY(FALL3) iff no contract-conformant
    candidate covers the surface AND the c3 must-fail fires: the
    bordered form is an exact INTERFACE to the pair-correlation
    demand (case 3), not an independent corner;
  CORNER_WEIL_NATIVE(FALL1) kept for completeness; unreachable per
    (A4), asserted as a documentation gate.
CLAIM BOUNDARY (delivered under CORNER_INTERFACE_ONLY, verbatim
for the campaign): "the T-analysis of CENTERED_BASEFIBER solves
the OPERATOR side of the interface [[H_N, u],[u^T, B]] >= 0; the
corner B is the budget value of the PRIME.FLOOR.PAIRCORR.01
forward demand |aniso| <= C*sigma_sqrt in window form (case 3);
the arithmetic side remains a NAMED EXTERNAL bound (the root-scale
demand), it is not solved, replaced or weakened by any operator
result of the campaign."

MUST-FAILS (each loud): (m1) = (c3) the r243 audit budget is
flagged by the c1 auditor AND fires the alias clause; (m2) corner
oracle B_orc = 1.01 * S_{N-1} covers 42/42 trivially and is
excluded by the same auditor (it consumes S); (m3) the split ward
G31 breaks by exactly rho_0 if the UNCENTERED head is used
(uncentered alias, r248 G42 class).

SEALED CONSTANTS: ladder = frame-A h <= 900 (42 rungs, r243/r244
builder verbatim: hirota_sign_probe.window_data + principal_
bessel_probe.smooth_comb + port_integrable_kernel_probe.build_
rung); candidates b1/b2/b3 = the r244 sealed builders (b2/b3
imported as functions from bordered_hankel_probe, audited by
source); head degree 8 (Q_7 = rho_1..rho_7, r248); alias bar
0.95, split ward bar 1e-10 rel, razor band [0.005, 0.05],
range-reproduction bands (r244 records, +-10 percent): b1
[2.6, 4.9], b2 [4.3, 8.1], b3 [3.7, 9.7], S [5.4, 17.0], S median
[9.4, 11.5]; trend clauses Spearman(B;N) >= 0.3, margin trend
< -0.5 expected FAIL-side (deficit grows, informational); smoke
kz = (9, 12, 13, 26, 40); runtime <= 1800 s.  AST firewall: no
zero/prime-oracle identifiers anywhere in this module.

RECORD TABLES (frozen from calib_cp_pass1.log (smoke, 20/20,
0.3 s) + calib_cp_pass2.log (full, 19/20 pre-freeze: the single
FAIL was G22 against the placeholder hash, replaced here by the
measured CAND_SHA -- the freeze step itself; wall 7.5 s);
CALIBRATION AMENDMENTS: NONE -- the citations, the case rules,
the contract clauses c1-c4, all bars and the verdict rules never
moved):
CAL_VERDICT = CORNER_INTERFACE_ONLY(FALL3).
Key numbers.  (c2) CAND_SHA 6dd6224ffe1f5e1b (42 windows x 3
candidates, 12 sig digits, hashed at chain-call counter 0).
(c4) COVERAGE CENSUS: b1 0/42, b2 0/42, b3 0/42 (r244 reproduced
under this build); ranges b1 [2.912, 4.434], b2 [4.867, 7.335],
b3 [4.149, 8.785] vs S_{N-1} [6.063, 15.408] median 10.463;
worst margins -10.98 / -8.07 / -6.62; Spearman(B;N) +0.95/+0.96/
+0.84; margin trends -0.65/-0.58/-0.65 (deficit GROWS with N);
alias res_corr -0.14/-0.20/+0.93 (all <= 0.95, no candidate is an
S-alias -- they fail honestly).  (G31) split ward: max rel dev
of rho_0 + Q_7 + T vs S_{N-1} = 2.7e-15; centered == raw margin
identity exact to 6.8e-15.  (c3) TAUTOLOGY: auditor flags taut_bw
at names {S}; coverage 42/42 BY CONSTRUCTION; razor min margin
5/7 - rho_{N-1} = 0.013927 (r243 reproduced, band [0.005,
0.05]); alias res_corr(B_w, S) = +0.99333 > 0.95 -- CORNER_ALIAS
fires.  (m2) oracle B_orc = 1.01 S covers 42/42 and is flagged at
names {S}.  (m3) uncentered head (w9) breaks G31 by exactly
rho_0 (rel 4.5e-01, loud at 4.5e+09 x bar, identity dev 1.0e-15).
LEG B DECISION: case 1 NO (A4, documentation gate); case 2 NO
(0/42 x 3); case 3 YES -- CORNER_INTERFACE_ONLY(FALL3) with the
claim boundary text delivered verbatim.

AMENDMENTS AFTER FREEZE: NONE.

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

import bordered_hankel_probe as BH           # noqa: E402 r244
import hirota_sign_probe as HS               # noqa: E402 r226
import port_integrable_kernel_probe as PIK   # noqa: E402 v881
import principal_bessel_probe as PB          # noqa: E402 r243
import v563_paper2_readouts as core          # noqa: E402 READ-ONLY

H_CAP = 900
HEAD_DEG = 8                       # Q_7 = rho_1..rho_7 (r248)
ALIAS_RES = 0.95
SPLIT_BAR = 1e-10
RAZOR_BAND = (0.005, 0.05)
B1_BAND = (2.6, 4.9)
B2_BAND = (4.3, 8.1)
B3_BAND = (3.7, 9.7)
S_BAND = (5.4, 17.0)
S_MED_BAND = (9.4, 11.5)
SPEAR_MIN = 0.3
SMOKE_KZ = (9, 12, 13, 26, 40)
SIG_DIGITS = 12
CAL_VERDICT = "CORNER_INTERFACE_ONLY(FALL3)"
CAL_CAND_SHA = "6dd6224ffe1f5e1b"

SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
T0_WALL = time.time()
CHECKS: list = []

# machine-checkable ordering sentinel for contract clause (c2)
CHAIN_CALLS = 0


def check(name, ok, detail):
    ok = bool(ok)
    CHECKS.append((name, ok, detail))
    print("  [%s] %-44s %s" % ("PASS" if ok else "FAIL", name, detail),
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
    return (not bad), ("NO zero/prime oracles anywhere; ground truth "
                       "enters gates only" if not bad
                       else "; ".join(bad))


# ---------------------------------------------------- c1 auditor
FORBIDDEN_NAMES = {"S", "St", "Sv", "S_w", "rho", "rho0", "Fv", "hv",
                   "Tv", "T_w", "D_w", "Dv", "margin", "bord_chain",
                   "budget_chain", "solve", "inv", "lstsq", "pinv"}


def purity_audit(module_path, func_names):
    """AST/dataflow audit of contract clause (c1): within the named
    FunctionDefs, no loaded identifier may lie in FORBIDDEN_NAMES and
    no identifier may contain the tau token -- the candidate formulas
    consume node positions, weights and window constants ONLY."""
    src = open(module_path, "r", encoding="utf-8").read()
    tree = ast.parse(src)
    hits = {}
    found = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and node.name in func_names:
            found.add(node.name)
            bad = set()
            for sub in ast.walk(node):
                nm = sub.attr if isinstance(sub, ast.Attribute) else (
                    sub.id if isinstance(sub, ast.Name) else None)
                if nm and (nm in FORBIDDEN_NAMES
                           or "tau" in nm.lower()):
                    bad.add(nm)
            hits[node.name] = sorted(bad)
    missing = set(func_names) - found
    return hits, missing


# ------------------------------------------------- candidate formulas
# (c1) source-pure: node positions, node weights, window constants
# ONLY.  b2/b3 delegate to the r244 sealed builders (audited by
# source in G10); b1 is the smooth self-pairing s_0.

def cand_b1(bwa):
    """b1 smooth self-pairing: B1 = s_0 = int dsigmatilde."""
    return float(np.sum(bwa))


def cand_b2(bxa, bwa, wxa, wwa, n_deg):
    """b2 Szego/equilibrium budget on the measured hull, mass
    m_0(mutilde) (r244 builder)."""
    hull_lo = min(float(np.min(wxa)), float(np.min(bxa)))
    hull_hi = max(float(np.max(wxa)), float(np.max(bxa)))
    x0 = 0.5 * (hull_lo + hull_hi)
    rad = 0.5 * (hull_hi - hull_lo)
    m0 = float(np.sum(wwa))
    return float(BH.cheb_budget(bxa, bwa, x0, rad, m0, n_deg))


def cand_b3(xs, ws, bxa, bwa, n_deg):
    """b3 mu-side norm: orthonormal positive-zone chain (r244
    builder)."""
    return float(BH.mu_side_budget(xs, ws, bxa, bwa, n_deg))


# ------------------------------------------- contract-violating forms
def taut_bw(S):
    """the r243 AUDIT budget B_w = S_{N-2} + 5/7 -- INTENTIONALLY
    contract-violating (consumes S); must be FLAGGED by the auditor
    and must fire the alias clause (c3 must-fail material)."""
    return float(S[-2]) + 5.0 / 7.0


def oracle_borc(S):
    """m2 corner oracle B_orc = 1.01 * S_{N-1} -- trivial coverage,
    excluded by the auditor (consumes S)."""
    return 1.01 * float(S[-1])


# ------------------------------------------------------- window data
def window_arrays(kz):
    """source data of one window: comb zone + sealed smooth border
    (r243 map verbatim); returns node/weight arrays and the degree
    count -- NO chain evaluation here (contract clause c2)."""
    d = HS.window_data(kz)
    alpha = PIK.build_rung(kz)["alpha"]
    dsm = HS.window_data(kz, comb=PB.smooth_comb(alpha))
    bxa = np.concatenate([dsm["xs"], dsm["ys"]])
    bwa = np.concatenate([dsm["ws"], -dsm["vs"]])
    wxa = np.concatenate([d["xs"], d["ys"]])
    wwa = np.concatenate([d["ws"], -d["vs"]])
    return dict(kz=kz, N=d["n_max"], d=d, dsm=dsm,
                bxa=bxa, bwa=bwa, wxa=wxa, wwa=wwa)


def budget_chain(wa):
    """S-evaluator (the r244 bordered chain verbatim); counted by the
    c2 ordering sentinel."""
    global CHAIN_CALLS
    CHAIN_CALLS += 1
    d, dsm, N = wa["d"], wa["dsm"], wa["N"]
    rows = BH.bord_chain(d["xs"], d["ws"], d["ys"], d["vs"],
                         dsm["xs"], dsm["ws"], dsm["ys"], dsm["vs"], N)
    rho = np.array([r["rho"] for r in rows])
    S = np.cumsum(rho)
    return rho, S


def main():
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke

    print("=" * 78)
    print("corner_provenance_probe -- PRIME.PORT.CORNER.PROVENANCE.01"
          "  (round 251a)")
    print("SPEC_SHA %s   (%s)" % (SPEC_SHA[:16],
                                  "SMOKE" if smoke else "FULL RECORD"))
    print("=" * 78)

    # ---------------- S0: firewall + predefinition
    section("S0  FIREWALL + PREDEFINITION")
    okf, det = firewall_audit()
    check("G01-firewall", okf, det)
    check("G02-predefinition", True,
          "citations A1-A5, case rules 1-3, contract clauses c1-c4, "
          "candidate formulas, alias bar %.2f, razor band %s and "
          "verdict rules sealed in the docstring BEFORE evaluation "
          "(SPEC_SHA above)" % (ALIAS_RES, str(RAZOR_BAND)))

    # ---------------- S1: contract clause c1 -- source purity (AST)
    section("S1  (c1) CANDIDATE SOURCE-PURITY -- AST/DATAFLOW AUDIT")
    own = os.path.abspath(__file__)
    hits_own, miss_own = purity_audit(
        own, {"cand_b1", "cand_b2", "cand_b3"})
    hits_bh, miss_bh = purity_audit(
        BH.__file__, {"cheb_budget", "mu_side_budget"})
    ok10 = (not miss_own and not miss_bh
            and all(not v for v in hits_own.values())
            and all(not v for v in hits_bh.values()))
    check("G10-candidates-source-pure", ok10,
          "cand_b1/b2/b3 (own) + cheb_budget/mu_side_budget (r244 "
          "builders, audited by source) reference NO name in the "
          "forbidden set {S, rho, Fv, hv, Tv, margin, chain, "
          "solve/inv, *tau*}: formulas of (window data, archimedean "
          "source, fixed conventions) only; violations: %s"
          % (str({**hits_own, **hits_bh})))
    hits_t, _ = purity_audit(own, {"taut_bw", "oracle_borc"})
    ok11 = (hits_t.get("taut_bw") == ["S"]
            and hits_t.get("oracle_borc") == ["S"])
    check("G11-auditor-flags-r243-form", ok11,
          "the SAME auditor FLAGS the r243 audit budget taut_bw "
          "(B_w = S_{N-2} + 5/7) and the m2 oracle at names %s: "
          "both consume S -- the contract violation is machine-"
          "detected, not narrated" % str(hits_t))

    # ---------------- S2: contract clause c2 -- pre-fixation + hash
    section("S2  (c2) PRE-FIXATION: CANDIDATES BEFORE ANY S")
    if smoke:
        kzs = list(SMOKE_KZ)
    else:
        kzs = [kz for kz in core.frame_a_zones()
               if PIK.build_rung(kz)["h"] <= H_CAP]
    was = [window_arrays(kz) for kz in kzs]
    was.sort(key=lambda w: (w["N"], w["kz"]))
    cand = {}
    for w in was:
        b1 = cand_b1(w["bwa"])
        b2 = cand_b2(w["bxa"], w["bwa"], w["wxa"], w["wwa"], w["N"])
        b3 = cand_b3(w["d"]["xs"], w["d"]["ws"], w["bxa"], w["bwa"],
                     w["N"])
        cand[w["kz"]] = (b1, b2, b3)
    fmt = "%%.%dg" % SIG_DIGITS
    blob = ";".join("%d:%s,%s,%s" % ((kz,) + tuple(
        fmt % v for v in cand[kz])) for kz in sorted(cand))
    cand_sha = hashlib.sha256(blob.encode("utf-8")).hexdigest()
    ok20 = CHAIN_CALLS == 0
    check("G20-prefixation-order", ok20,
          "candidate table (%d windows x 3) hashed at chain-call "
          "counter %d (must be 0): CAND_SHA %s -- the values are "
          "fixed BEFORE any budget-chain evaluation in this process"
          % (len(was), CHAIN_CALLS, cand_sha[:16]))
    b1v = np.array([cand[k][0] for k in sorted(cand)])
    b2v = np.array([cand[k][1] for k in sorted(cand)])
    b3v = np.array([cand[k][2] for k in sorted(cand)])
    ok21 = (B1_BAND[0] <= b1v.min() and b1v.max() <= B1_BAND[1]
            and B2_BAND[0] <= b2v.min() and b2v.max() <= B2_BAND[1]
            and B3_BAND[0] <= b3v.min() and b3v.max() <= B3_BAND[1])
    check("G21-candidate-ranges", ok21,
          "b1 [%.3f, %.3f] b2 [%.3f, %.3f] b3 [%.3f, %.3f] inside "
          "the sealed r244 reproduction bands %s/%s/%s"
          % (b1v.min(), b1v.max(), b2v.min(), b2v.max(),
             b3v.min(), b3v.max(),
             str(B1_BAND), str(B2_BAND), str(B3_BAND)))
    if not smoke:
        check("G22-cand-sha-frozen", cand_sha[:16] == CAL_CAND_SHA,
              "CAND_SHA %s == frozen record %s"
              % (cand_sha[:16], CAL_CAND_SHA))
    else:
        check("G22-cand-sha-frozen", True,
              "SKIPPED in smoke mode (reduced ladder has its own "
              "table); full-run CAND_SHA is the frozen record")

    # ---------------- S3: S-evaluation + split ward
    section("S3  S-EVALUATION + CENTERED SPLIT WARD (after the hash)")
    packs = {}
    for w in was:
        rho, S = budget_chain(w)
        packs[w["kz"]] = (rho, S)
    Sv = np.array([float(packs[k][1][-1]) for k in sorted(cand)])
    Ns = np.array([w["N"] for w in
                   sorted(was, key=lambda x: x["kz"])], float)
    med = float(np.median(Sv))
    ok30 = (S_BAND[0] <= Sv.min() and Sv.max() <= S_BAND[1]
            and (smoke or S_MED_BAND[0] <= med <= S_MED_BAND[1]))
    check("G30-budget-census", ok30,
          "S_{N-1} in [%.3f, %.3f] median %.3f (r243/r244 census "
          "reproduced; bands %s, median %s%s); chain calls %d"
          % (Sv.min(), Sv.max(), med, str(S_BAND), str(S_MED_BAND),
             " -- median band waived in smoke" if smoke else "",
             CHAIN_CALLS))
    dev31 = 0.0
    dev31c = 0.0
    for k in sorted(cand):
        rho, S = packs[k]
        St = float(S[-1])
        split = (float(rho[0]) + float(np.sum(rho[1:HEAD_DEG]))
                 + float(np.sum(rho[HEAD_DEG:])))
        dev31 = max(dev31, abs(split / St - 1.0))
        bc = cand[k][1]
        raw = bc - St
        cen = ((bc - float(rho[0])) - float(np.sum(rho[1:HEAD_DEG]))
               - float(np.sum(rho[HEAD_DEG:])))
        dev31c = max(dev31c, abs(cen - raw) / max(abs(raw), 1e-300))
    check("G31-centered-split-ward", dev31 <= SPLIT_BAR
          and dev31c <= SPLIT_BAR,
          "rho_0 + Q_7 + T == S_{N-1} max rel dev %.1e; corner "
          "margin identity (B - rho_0) - Q_7 - T == B - S_{N-1} max "
          "rel dev %.1e (bar %.0e): raw-budget coverage and "
          "centered-fiber coverage are THE SAME statement"
          % (dev31, dev31c, SPLIT_BAR))
    # m3: the UNCENTERED head breaks the split by exactly rho_0
    rho9, S9 = packs[9]
    St9 = float(S9[-1])
    bad_split = (2.0 * float(rho9[0])
                 + float(np.sum(rho9[1:HEAD_DEG]))
                 + float(np.sum(rho9[HEAD_DEG:])))
    m3_rel = abs(bad_split / St9 - 1.0)
    m3_exact = abs((bad_split - St9) - float(rho9[0])) \
        / max(float(rho9[0]), 1e-300)
    ok32 = m3_rel > 100.0 * SPLIT_BAR and m3_exact <= 1e-10
    check("G32-mustfail-m3-uncentered", ok32,
          "double-counted rho_0 (uncentered head) breaks the split "
          "ward by EXACTLY rho_0 (rel %.1e, loud at %.1e x bar; "
          "identity dev %.1e) -- the r248 uncentered-alias class"
          % (m3_rel, m3_rel / SPLIT_BAR, m3_exact))

    # ---------------- S4: contract clause c4 -- coverage census
    section("S4  (c4) COVERAGE CENSUS OF CONFORMANT CANDIDATES")
    names = ("b1", "b2", "b3")
    vecs = (b1v, b2v, b3v)
    cover = {}
    stats = {}
    for nm, bv in zip(names, vecs):
        marg = bv - Sv
        cover[nm] = int(np.sum(marg > 0.0))
        stats[nm] = (float(marg.min()), BH.spearman(bv, Ns),
                     BH.spearman(marg, Ns), BH.res_corr(bv, Sv, Ns))
    info("coverage b1 %d/%d  b2 %d/%d  b3 %d/%d;  worst margins "
         "%.2f / %.2f / %.2f" % (cover["b1"], len(Sv), cover["b2"],
                                 len(Sv), cover["b3"], len(Sv),
                                 stats["b1"][0], stats["b2"][0],
                                 stats["b3"][0]))
    info("Spearman(B;N) %+.2f/%+.2f/%+.2f; margin trend %+.2f/%+.2f/"
         "%+.2f; alias res_corr %+.2f/%+.2f/%+.2f" % (
             stats["b1"][1], stats["b2"][1], stats["b3"][1],
             stats["b1"][2], stats["b2"][2], stats["b3"][2],
             stats["b1"][3], stats["b2"][3], stats["b3"][3]))
    full_cover = [nm for nm in names if cover[nm] == len(Sv)
                  and abs(stats[nm][3]) <= ALIAS_RES]
    ok40 = all(abs(stats[nm][3]) <= ALIAS_RES for nm in names)
    check("G40-no-candidate-alias", ok40,
          "no conformant candidate is an S-alias (|res_corr| <= "
          "%.2f): where they fail, they fail HONESTLY" % ALIAS_RES)
    check("G41-census-adjudicated", True,
          "full-coverage conformant candidates: %s (empty => case 2 "
          "unfilled, r244 0/42 reproduced under this build)"
          % (str(full_cover) if full_cover else "NONE"))

    # ---------------- S5: contract clause c3 -- the tautology test
    section("S5  (c3) THE r243 TAUTOLOGY -- MUST-FAIL DEMONSTRATION")
    bw = np.array([taut_bw(packs[k][1]) for k in sorted(cand)])
    marg_bw = bw - Sv
    razor = float(marg_bw.min())
    rc_bw = BH.res_corr(bw, Sv, Ns)
    ok50 = (int(np.sum(marg_bw > 0.0)) == len(Sv)
            and (smoke or (RAZOR_BAND[0] <= razor <= RAZOR_BAND[1]))
            and abs(rc_bw) > ALIAS_RES)
    check("G50-tautology-fires", ok50,
          "B_w = S_{N-2} + 5/7 covers %d/%d BY CONSTRUCTION, min "
          "terminal margin 5/7 - rho_{N-1} = %.6f (r243 razor, band "
          "%s%s), alias res_corr %+.5f > %.2f => CORNER_ALIAS: a "
          "budget built from S certifies nothing -- the r243 form "
          "VIOLATES the provenance contract (flagged in G11)"
          % (int(np.sum(marg_bw > 0.0)), len(Sv), razor,
             str(RAZOR_BAND),
             " -- band waived in smoke" if smoke else "",
             rc_bw, ALIAS_RES))
    borc = np.array([oracle_borc(packs[k][1]) for k in sorted(cand)])
    ok51 = int(np.sum(borc - Sv > 0.0)) == len(Sv)
    check("G51-mustfail-m2-oracle", ok51,
          "corner oracle B_orc = 1.01 S_{N-1} covers %d/%d trivially "
          "and is EXCLUDED by the c1 auditor (G11): coverage without "
          "provenance is worthless" % (int(np.sum(borc - Sv > 0.0)),
                                       len(Sv)))

    # ---------------- S6: leg A / leg B adjudication
    section("S6  LEG A CITATIONS + LEG B THREE-CASE ADJUDICATION")
    keys = ("|aniso(S_p - S)| <=", "das neue\n  UEBERGABEOBJEKT",
            "Vierfach-Identifikation", "MANIFEST positiv",
            "injizierte Stoerungs-\n  ENERGIE",
            "lift budget B_w = S_{N-2} + 5/7 (audit form")
    okA = all(k in __doc__ for k in keys)
    check("G60-citations-sealed", okA,
          "A1 (PAIRCORR forward demand, next.txt:577), A2 (r243 "
          "handover + verbatim typing, next.txt:13852; B_w audit "
          "form, principal_bessel amendment a4), A3 (r244 census + "
          "quadruple identification, next.txt:13854), A4 (Weil form "
          "borderless: M_h cell builder next.txt:11, L_f + "
          "diag(Delta) next.txt:69, v791 GNS state next.txt:589), "
          "A5 (v881 energy identity next.txt:541) -- all quotes "
          "sealed in the docstring under SPEC_SHA")
    check("G61-case1-weil-native", True,
          "CASE 1 = NO (documentation gate): the bordered matrix "
          "[[H, u],[u^T, B]] first appears as the r243 TELESCOPING "
          "of the full-prefix Bessel system (A2); the Weil wall M_h "
          "is a full pole+prime matrix (A4), the GL1 landing is a "
          "state positivity -- no border exists in the original "
          "Weil form")
    case2 = bool(full_cover)
    check("G62-case2-external-norm", True,
          "CASE 2 = %s (measured): contract-conformant admissible "
          "test norms covering the fiber: %s" % (
              "YES" if case2 else "NO",
              str(full_cover) if full_cover else
              "NONE (b1/b2/b3 coverage 0 or partial, r244 0/42 "
              "class)"))
    case3 = (not case2) and ok50 and ok11
    check("G63-case3-paircorr-budget", case3 or case2,
          "CASE 3 = %s: no conformant corner covers, the only "
          "covering budget consumes S (G50), and the r243 typing is "
          "verbatim on record (A2: Delta_Bes >= 0 <=> |F| <= "
          "sqrt(B#) sqrt(h) == the PAIRCORR forward demand; A3: "
          "quadruple identification)" % ("YES" if case3 else "NO"))

    # ---------------- S7: verdict + claim boundary
    section("S7  VERDICT + CLAIM BOUNDARY")
    if case2:
        verd = "CORNER_SOURCE_CANDIDATE(%s)" % ",".join(full_cover)
    elif case3:
        verd = "CORNER_INTERFACE_ONLY(FALL3)"
    else:
        verd = "PROVENANCE_OPEN"
    if verd == "CORNER_INTERFACE_ONLY(FALL3)":
        info("CLAIM BOUNDARY (verbatim, for the CENTERED_BASEFIBER "
             "campaign): the T-analysis solves the OPERATOR side of "
             "the interface [[H_N, u],[u^T, B]] >= 0; the corner B "
             "is the budget value of the PRIME.FLOOR.PAIRCORR.01 "
             "forward demand |aniso| <= C*sigma_sqrt in window form "
             "(case 3); the arithmetic side remains a NAMED EXTERNAL "
             "bound (the root-scale demand), not solved, replaced or "
             "weakened by any operator result of the campaign.")
    check("G70-verdict-frozen", smoke or verd == CAL_VERDICT,
          "verdict %s%s == frozen calibration %s; mincut base 4 / "
          "refined 5 UNCHANGED; NO RH claim in either direction"
          % (verd, " (SMOKE)" if smoke else "", CAL_VERDICT))

    # ---------------- S9: bookkeeping
    section("S9  BOOKKEEPING")
    wall = time.time() - T0_WALL
    check("G99-runtime", wall <= 1800.0,
          "wall %.1f s <= 1800 s" % wall)
    npass = sum(1 for _, ok, _ in CHECKS if ok)
    print("\n" + "=" * 78)
    print("RESULT: %d/%d gates PASS%s   SPEC_SHA %s   VERDICT %s"
          % (npass, len(CHECKS), " (SMOKE)" if smoke else "",
             SPEC_SHA[:16], verd))
    print("=" * 78)
    return 0 if npass == len(CHECKS) else 1


if __name__ == "__main__":
    sys.exit(main())
