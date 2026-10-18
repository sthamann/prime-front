#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""v877 -- PRIME.DEEPALPHA.SIGN.01 + PRIME.PRUEFER.COMPENSATION.02 + PRIME.TRUNCATION.AUDIT.01: THE ARTIFACT RESOLUTION AND THE COTLAR REVERSAL (the round's headline, 2026-08-08 night) -- the deep-alpha negative floors were a COMB-TRUNCATION ARTIFACT of the deployed atom table, and on complete combs the preregistered Cotlar route REOPENS with bounded sums.  STRAND 1, THE ARTIFACT (8/8, DEEP-ALPHA-ARTIFACT): the negative Krein floors at kz 142/177/243 (lam1 = -331/-135/-215, reported by two independent probes) were ARTIFACTS of core.build_window's SILENT comb truncation -- the deployed von Mangoldt table caps at ATOM_MAX = 400000 (log 12.899) while those windows demand support up to e^{2 alpha} = 4.4e5 / 8.0e5 / 1.8e6; the tent assembly was missing every event beyond the cap, breaking the explicit-formula balance.  With the COMPLETE canonical comb (extended sieve to ceil(e^{2 alpha_max}), same machinery verbatim) the certified 2x2 corner enclosures are STRICTLY POSITIVE (+1.057e-5 / +1.519e-5 / +1.200e-5 within certified interval bounds) and the Cholesky-certified full and Krein floors are positive on all three rungs (Krein cert-lo +1.1e-8 / +1.2e-8 / +6.0e-9); the extended builder is the IDENTITY on the control rungs kz 9/13/121 (bit-equal atoms), the skeleton refs reproduce, and the truncated readouts reproduce the two probes' negatives -- both sides of the artifact typed.  NO negative canonical window exists; the certified skeleton ladder's end at kz 121 was the atom-table DATA boundary, not a structural alpha wall; H_cof is UNAFFECTED (a cofinal sequence draws from complete-comb windows -- a data constraint, not an alpha ceiling).  THE INFRASTRUCTURE NOTE (typed as a bug, ledger note demands the fix): core.build_window MUST fail loudly when a window demands comb support beyond ATOM_MAX -- the silent truncation produced O(-100) floors that two probes booked as physics; an explicit guard is the registered follow-up.  STRAND 2, THE REVERSAL (9/9, COTLAR-BOUNDED-V2): the v2 protocol re-executes the v1 Cotlar contract with cells, pairing, danger geometry and decision bars FROZEN IDENTICALLY (the committed v1 spec SHA 4621b899... re-verified at run time against ppc.FROZEN_SPEC; v2 spec SHA 5fd6bf61... printed and gated) and the SINGLE substantive change warded (complete combs at the deep holdouts only; battery + kz 90/116 bit-identical): the deep sums COLLAPSE INTO THE BATTERY BAND (kz 142: S_U 32.07 -> 5.65, S_C 58.78 -> 4.10; kz 177: 14.29 -> 5.97, 30.76 -> 4.51; kz 243: 13.94 -> 5.87, 44.85 -> 4.31), both channels BOUNDED by the frozen v1 rule (holdout/battery ratios 0.95/0.94 <= 1.2, log-log slopes 0.006/0.007 <= 0.10), the v1 kill was ENTIRELY the artifact; RUN 3 (the analytic envelope candidate, gated on BOUNDED) unlocks and PASSES: K_1 = max_d env_U(d)(1+d) and K_2 = max_d env_C(d)(1+d)^2 are h-STABLE on all five complete-comb holdouts (anchor max 8.36/40.35 vs holdout max 8.14/40.47, bar 1.2x); Epstein/scramble still break the v1 contrast bars (max rel 3927%/314462%, eps ratios 224/1.26e6).  THE TRUNCATION AUDIT (the typed table): pruefer v1 CONFOUNDED -> re-decided by v2; residual_quadrature ROBUST + STRENGTHENED (its 47/47 sign agreement means the horizon detected the truncation-negatives correctly -- a VALIDATED sign detector; its "stall = deep alpha" reading retypes to "stall = truncated comb"); pi_resonance RESONANCE-THICK ROBUST on certified rungs, its alpha-law addendum CONFOUNDED and its quartet test VOID; phase_polygon deep-holdout rows retype NUMERIC-VOID (raw-longdouble machinery out of range at complete-comb mass -- neither confirmed nor refuted; the battery verdict unaffected); softport_radau17 / preconditioned_port / cdcore / jacobi_uvarov / excess_certified_skeleton UNAFFECTED.  THE DATED CORRECTION carried by this module (ledger-wins discipline): the round-35 closing note on PRIME.KREIN.CONTRACTOR.01 ("blockwise Cotlar class closed, stop-listed") receives a dated round-36 correction -- the v1 verdict was CORRECT ON THE DATA AS MEASURED (its own frozen rules, correctly applied), but the data was truncated at the deep holdouts; on complete combs the route REOPENS with bounded sums and h-stable envelope constants; the stop-list entry is AMENDED (the class is NOT closed); the remaining gap: the Cotlar constant B_C ~ 4.1-4.3 vs the needed 1, and the local-dominance defects Sum_r eps_r ~ 7-10.  v873's booking STANDS as the record of the preregistered v1 execution.  ONE module from two probes (re-executed verbatim, embedded BYTE-EXACT, ~17 min).  NO RH claim.  Python-only per GATE.WOLFRAM.02.

PROVENANCE: both probes frozen + SHA-hashed before first run (FROZEN_SPEC
SHA-256 gated below; the cotlar probe QUOTES and re-verifies the v1
contract SHA 4621b89958531d6d3baae9fe762dbd10d23dc22eed77a57aa1c6b179a744
0811 against the committed pruefer_compensation_probe at run time -- the
v1/v2 chain is machine-warded); the cotlar probe carries its ADDENDUM v1.1
typed verbatim (the polygon-audit typing refinement HOLDS/REFUTED/
NUMERIC-VOID; no Cotlar quantity, bar or decision rule touched; the first
execution reproduces bit-identically); the performance substitution
(Gram-identity cross norms) is warded vs ppc.cross_norms at 7.4e-14.
Executed 2026-08-08 night, re-executed verbatim at this promotion in
isolated namespaces with the byte-equality provenance ward.  The probes
import v563_paper2_readouts, gauss_node_unitary_probe,
excess_certified_skeleton_probe, pruefer_compensation_probe (v873) and
phase_polygon_probe (v876) READ-ONLY -- not re-gated here.  NO RH claim
anywhere; the reopening is a route statement, not a positivity claim.
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

EXPECT_SHA_DEEPALPHA = ("fda276babd1c3e4431aeec81e541dab1693e5311"
                        "7318d3b0e016bc6ac1f3d8f7")
EXPECT_SHA_COTLAR = ("5fd6bf61b10e336237286de913e7f7d71cec7169"
                     "91aa3bd75272045b7aa1d9c3")
V1_CONTRACT_SHA = ("4621b89958531d6d3baae9fe762dbd10d23dc22eed"
                   "77a57aa1c6b179a7440811")

# ------------- frozen probe sources (embedded BYTE-EXACT, raw strings)
_SRC_DEEPALPHA = r'''
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""deep_alpha_sign_probe -- PRIME.DEEPALPHA.SIGN.01
(EXPLORATION ONLY, experiments/; URGENT verification of the
negative floor readouts at kz 142/177/243, 2026-08-08 night).

THE QUESTION: two independent probes (pi_resonance_anatomy,
residual_quadrature) reported NEGATIVE floors at the deep-alpha
holdouts kz 177/243 (+ stall at 142) -- rungs BEYOND the
certified 67-rung skeleton ladder.  Genuine negative windows,
or a convention artifact?

THE CONVENTION AUDIT (read from the sources BEFORE computing):
(i) both quick probes read the floor through gnu.build_rung ->
core.build_window -> softport lam1(Delta) (the h-dim Krein
floor in the grid frame); (ii) core.build_window draws its
atoms from LAM_TAB = von_mangoldt_table(ATOM_MAX = 400000):
atoms_in(alpha) counts atoms with log n <= 2 alpha ON THE
TABLE -- for rungs with e^{2 alpha} > ATOM_MAX the comb is
SILENTLY TRUNCATED at log(400000) = 12.899 (the tent assembly
is missing every event in (400000, e^{2 alpha}]); (iii) the
certified skeleton ladder (excess_certified_skeleton_probe)
FROZE the filter `exp(2 alpha) > ATOM_MAX + 0.5 -> skip` (plus
the explicit h == 1292 exclusion = kz 243), i.e. the certified
67 rungs are exactly the COMPLETE-COMB windows -- the ladder
end at kz 121 was a DATA boundary (the atom-table cap), not a
structural wall; (iv) the anti-alias condition (v760) is
structural (deployed N_f = 2M+1 >= the sharp minimum 2M-1)
and holds at every frame-A rung -- it is NOT the binding axis.

THE HYPOTHESIS TO DECIDE: the negativity at kz 142/177/243 is
a comb-TRUNCATION artifact (out-of-family windows w.r.t. the
deployed table).  DECISIVE TEST: rebuild those windows with an
EXTENDED von Mangoldt table (sieved to ceil(e^{2 alpha}), i.e.
the complete canonical comb at their own (D, X)) and read the
floor at certificate grade:
  (1) the certified 2x2 corner enclosure tau_X (the skeleton
      machinery VERBATIM: qform/assembly/perturbation budgets,
      closed-form 2x2 enclosure);
  (2) the full h-dim lag floor lambda_min(A), certified sign:
      positive via shifted float Cholesky with rigorous slack
      (successful Cholesky of A - cI implies lambda_min >=
      c - CERT_INFL gamma_{3(n+1)} (||A - cI||_2 + 1), the
      Higham-style budget, typed); negative via a certified
      Rayleigh upper bound (q + E < 0 with the skeleton's
      norm-linear form budget);
  (3) the Krein floor lam1(Delta) through gnu.build_rung with
      the extended comb (same certificates on Delta; data
      convention: certificates cover the linear algebra above
      the deployed float data -- chol_cert discipline).
Controls: kz 9/13/121 (inside the certified range) run through
the IDENTICAL extended path; extension must be the IDENTITY
there (bit-equal atom arrays, equal Ah) and the corner
enclosures must reproduce the skeleton refs.

VERDICT (frozen): DEEP-ALPHA-ARTIFACT (truncated readouts
reproduce the negatives AND every extended certified readout
at kz 142/177/243 is strictly positive -- the artifact typed:
comb truncation at the ATOM_MAX table cap; the rungs are
OUT-OF-FAMILY for the deployed table, IN-FAMILY and positive
for the canonical tower) / DEEP-ALPHA-NEGATIVE-CERTIFIED (an
extended enclosure is strictly negative -- reported with
maximal prominence + admissibility status) / DEEP-ALPHA-
FRONTIER (an extended enclosure straddles zero after one
mp-dps-60 escalation -- typed).  NO RH claim, NO panic claim:
a genuinely negative single window would not contradict H_cof
(cofinal positivity needs only a subsequence).  Writes
nothing; no .md; no commits.

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/deep_alpha_sign_probe.py
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

import v563_paper2_readouts as core                 # noqa: E402
import gauss_node_unitary_probe as gnu              # noqa: E402
import excess_certified_skeleton_probe as esk       # noqa: E402

FROZEN_SPEC = """\
PRIME.DEEPALPHA.SIGN.01 spec v1 (2026-08-08, frozen before
run).  Rungs: DEEP = (142, 177, 243); CONTROLS = (9, 13, 121).
Audit wards: the skeleton frozen filter reproduces 67 rungs;
the truncated Krein floors reproduce the quick-probe values
(kz 177: -134.5, kz 243: -214.7, rel 2e-2; kz 9: +1.675e-4,
rel 1e-2).  Admissibility table per rung: (A1) frame-A
membership; (A2) atom floor N_ATOM_MIN; (A3) COMB COMPLETENESS
e^{2 alpha} <= ATOM_MAX (the binding axis); (A4) anti-alias
N_f = 2M+1 >= 2M-1 (structural, v760); (A5) skeleton-filter
membership.  Extended builder: von_mangoldt_table(ceil(e^{2
alpha kz-max}) + 1); zone geometry (alpha, D, M, t1, t2) from
the ORIGINAL zone list unchanged; atoms = all table events
with log n <= 2 alpha; identity ward on CONTROLS (bit-equal
uu/mm, max|Ah_ext - Ah| == 0).  Certificates: corner tau_X via
esk.assemble_comb/block_enclosure/lam_min_2x2 VERBATIM
(budgets: E_form = gamma_{h+6} absform INFL; e_c assembly
budget; Mabs perturbation; 8u closed-form widening); full-A
and Delta sign: positive cert = shifted Cholesky, lambda_min
>= c - slack, slack = CERT_INFL gamma_{3(n+1)} (||M - cI||_2
+ |c| + 1), c from the geometric ladder {0.9, 0.5, 0.1, 0.01}
x float lambda_min; negative cert = Rayleigh q(v) + E_form <
0 at the float eigenvector.  Data convention (typed): the
certificates cover the linear algebra above the deployed
float data (chol_cert discipline); Delta additionally sits
above the float G_+^{-1/2} chain (control grade, typed).
Escalation on straddle only: mpmath dps 60 corner midpoint
(typed FRONTIER if still straddling).  Skeleton corner refs:
kz 9 tau 5.984165e-4, kz 13 5.637632e-4 (rel 1e-4).  Missing
tail mass reported per deep rung: sum MU over (ATOM_MAX,
e^{2 alpha}].  VERDICTS: DEEP-ALPHA-ARTIFACT / DEEP-ALPHA-
NEGATIVE-CERTIFIED (+ IN-FAMILY / OUT-OF-FAMILY) /
DEEP-ALPHA-FRONTIER.  NO RH claim; NO panic claim; writes
nothing."""

DEEP = (142, 177, 243)
CONTROLS = (9, 13, 121)
KREIN_TRUNC_REFS = {177: -134.5, 243: -214.7}
KREIN_POS_REF = {9: 1.675e-4}
TAU_REFS = {9: 5.984165e-4, 13: 5.637632e-4}
CHOL_FACS = (0.9, 0.5, 0.1, 0.01)
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


def ast_scan(banned):
    src = open(os.path.abspath(__file__), encoding="utf-8").read()
    bad = []
    for node in ast.walk(ast.parse(src)):
        name = None
        if isinstance(node, ast.Name):
            name = node.id
        elif isinstance(node, ast.Attribute):
            name = node.attr
        if name and name.lower() in banned:
            bad.append(name)
    return bad


# ------------------------------------------------ extended builder
def build_window_ext(kz, U_EXT, MU_EXT):
    """core.build_window VERBATIM, with the atom list drawn
    from the EXTENDED table (zone geometry unchanged)."""
    alpha = float(core.U_ALL[kz])
    D_k = 0.5 * float(core.G_ALL[kz]) / float(core.NU_MAIN)
    Mz = int(math.ceil(alpha / D_k - 1.0e-9)) + 1
    if Mz % 2:
        Mz += 1
    hz = Mz // 2
    ka = int(np.searchsorted(U_EXT, 2.0 * alpha + 1.0e-14,
                             side="right"))
    uu = U_EXT[:ka].copy()
    mm = MU_EXT[:ka].copy()
    c_at, D = core.atom_lags_at(alpha, Mz, uu, mm)
    c_ar = core.arch_lags(Mz, D)
    Tb = core.parity_basis(hz, 2)
    t1, t2 = Tb[0].copy(), Tb[1].copy()
    A_full = core.odd_toeplitz(c_ar + c_at, Mz)
    Ah = np.array([[float(t1 @ (A_full @ t1)),
                    float(t1 @ (A_full @ t2))],
                   [float(t1 @ (A_full @ t2)),
                    float(t2 @ (A_full @ t2))]])
    return dict(k=kz, h=hz, M=Mz, D=D, alpha=alpha, uu=uu,
                mm=mm, lam=0.5 * mm, t1=t1, t2=t2, Ah=Ah,
                A_full=A_full, c_ar=c_ar, c_at=c_at)


def corner_enclosure(rrx):
    """The skeleton certificate VERBATIM on one (possibly
    extended) window: certified [lo, hi] of tau_X."""
    M = rrx["M"]
    c_ar = rrx["c_ar"]
    T = core.odd_toeplitz(c_ar, M)
    aT = np.abs(T)
    cc, e_c = esk.assemble_comb(rrx, rrx["uu"], rrx["lam"])
    Tc = core.odd_toeplitz(cc, M)
    aTc = np.abs(Tc)
    h = M // 2
    ri = np.arange(h)
    Mabs = (e_c[np.abs(ri[:, None] - ri[None, :])]
            + e_c[(M - 1) - ri[:, None] - ri[None, :]])
    ent = esk.block_enclosure(rrx, T, aT, Tc, aTc, Mabs)
    return esk.lam_min_2x2(ent)


def sign_cert(Msym):
    """Certified sign of lambda_min of a symmetric float
    matrix (linear algebra above the float data).  Returns
    (float lambda_min, certified lower bound or None,
    certified upper bound)."""
    Msym = 0.5 * (Msym + Msym.T)
    n = Msym.shape[0]
    w, V = np.linalg.eigh(Msym)
    lf = float(w[0])
    v = np.ascontiguousarray(V[:, 0])
    q, E = esk.qform(v, v, Msym, np.abs(Msym))
    hi = q + E                       # certified upper bound
    lo = None
    if lf > 0.0:
        nrm = float(np.max(np.abs(w)))
        for fac in CHOL_FACS:
            c = fac * lf
            slack = esk.CERT_INFL * esk.gamma_fl(3 * (n + 1)) \
                * (nrm + abs(c) + 1.0)
            if c <= slack:
                continue
            try:
                np.linalg.cholesky(Msym - c * np.eye(n))
                lo = c - slack
                break
            except np.linalg.LinAlgError:
                continue
    return lf, lo, hi


def mp_corner(rrx, dps=60):
    """Escalation (straddle only): the corner tau_X midpoint
    at mp dps, data treated as exact floats."""
    import mpmath as mp
    mp.mp.dps = dps
    M = rrx["M"]
    cc = rrx["c_ar"] + rrx["c_at"]
    h = M // 2
    t1, t2 = rrx["t1"], rrx["t2"]
    ri = np.arange(h)
    idx1 = np.abs(ri[:, None] - ri[None, :])
    idx2 = (M - 1) - ri[:, None] - ri[None, :]
    ent = {}
    for key, x, y in (("00", t1, t1), ("11", t2, t2),
                      ("01", t1, t2)):
        acc = mp.mpf(0)
        for i in range(h):
            row = cc[idx1[i]] - cc[idx2[i]]
            acc += mp.fsum([mp.mpf(float(x[i]))
                            * mp.mpf(float(row[j]))
                            * mp.mpf(float(y[j]))
                            for j in range(h)])
        ent[key] = acc
    m = (ent["00"] + ent["11"]) / 2
    d = (ent["00"] - ent["11"]) / 2
    return float(m - mp.sqrt(d * d + ent["01"] * ent["01"]))


# ================================================================= main
def main():
    section("PRIME.DEEPALPHA.SIGN.01 -- are the deep-alpha "
            "floors genuinely negative? (EXPLORATION ONLY)")
    sha = hashlib.sha256(FROZEN_SPEC.encode("utf-8")).hexdigest()
    print("    FROZEN_SPEC SHA-256 = %s" % sha)
    print("    NO RH claim; NO panic claim (H_cof needs only "
          "a subsequence).")
    print("\nS0 -- firewall")
    check("S0.1 AST firewall clean (no zero/prime oracles)",
          not ast_scan(BANNED_IDS))

    # ---------------- S1 convention audit
    section("S1 -- THE CONVENTION AUDIT (typed from the "
            "sources)")
    print("""    QUICK READOUTS (pi_resonance_anatomy,
    residual_quadrature): gnu.build_rung -> core.build_window
    -> lam1(Delta) (h-dim Krein floor, grid frame).
    CERTIFIED LADDER (excess_certified_skeleton): 2x2 corner
    tau_X interval enclosures; FROZEN FILTER `exp(2 alpha) >
    ATOM_MAX + 0.5 -> skip` (+ explicit h == 1292 = kz 243).
    THE TABLE CAP: LAM_TAB = von_mangoldt_table(%d);
    log cap = %.4f.  core.build_window truncates the comb at
    the cap SILENTLY (atoms_in searches the table).  The
    certified ladder end (kz 121) is therefore a DATA
    boundary, not a structural one.""" % (
        core.ATOM_MAX, math.log(core.ATOM_MAX)))
    skel = []
    for kz in core.frame_a_zones():
        rr = core.build_window(kz)
        if rr["h"] == 1292 or math.exp(2.0 * rr["alpha"]) \
                > core.ATOM_MAX + 0.5:
            continue
        skel.append(kz)
    check("S1.1 [SKELETON FILTER REGRESSION] the frozen "
          "filter reproduces the certified ladder: %d rungs "
          "(== 67), last kz %d" % (len(skel), skel[-1]),
          len(skel) == 67 and skel[-1] == 121)
    logcap = math.log(core.ATOM_MAX)
    print("\n    kz    h     alpha   2alpha   X=e^2a     "
          "cap      deficit   atoms  complete")
    audit = {}
    for kz in sorted(set(CONTROLS) | set(DEEP) | {90, 116}):
        rr = core.build_window(kz)
        X = math.exp(2.0 * rr["alpha"])
        deficit = max(0.0, 2.0 * rr["alpha"] - logcap)
        complete = X <= core.ATOM_MAX + 0.5
        audit[kz] = dict(rr=rr, X=X, deficit=deficit,
                         complete=complete)
        print("    %-5d %-5d %-7.3f %-8.3f %-10.3e %-8.0e "
              "%-9.3f %-6d %s"
              % (kz, rr["h"], rr["alpha"], 2 * rr["alpha"],
                 X, float(core.ATOM_MAX), deficit,
                 rr["n_atom"], "YES" if complete
                 else "NO  <- TRUNCATED"))
    check("S1.2 [THE MECHANISM] kz 142/177/243 all demand "
          "comb support beyond the table cap while 9/13/90/"
          "116/121 are complete",
          all(not audit[kz]["complete"] for kz in DEEP)
          and all(audit[kz]["complete"]
                  for kz in (9, 13, 90, 116, 121)))

    # ---------------- S2 admissibility table
    section("S2 -- THE ADMISSIBILITY TABLE")
    print("    conditions: A1 frame-A membership (H_MIN <= h "
          "<= HCAP, D = g/(2 nu)); A2 atom floor >= %d; A3 "
          "COMB COMPLETENESS e^{2a} <= ATOM_MAX; A4 anti-"
          "alias N_f = 2M+1 >= 2M-1 (v760, structural); A5 "
          "skeleton-filter membership." % core.N_ATOM_MIN)
    zones = set(core.frame_a_zones())
    adm_ok = True
    for kz in sorted(set(CONTROLS) | set(DEEP)):
        rr = audit[kz]["rr"]
        a1 = kz in zones
        a2 = rr["n_atom"] >= core.N_ATOM_MIN
        a3 = audit[kz]["complete"]
        a4 = (2 * rr["M"] + 1) >= (2 * rr["M"] - 1)
        a5 = kz in skel
        if kz in CONTROLS:
            adm_ok &= a1 and a2 and a3 and a4 and a5
        print("    kz %-4d: A1 %-5s A2 %-5s A3 %-5s A4 %-5s "
              "A5 %-5s -> %s"
              % (kz, a1, a2, a3, a4, a5,
                 "ADMISSIBLE (canonical family)"
                 if (a1 and a2 and a3 and a5) else
                 "OUT-OF-FAMILY for the deployed table "
                 "(A3/A5 fail)"))
    check("S2.1 [CONTROL ADMISSIBILITY] the control rungs "
          "pass every condition", adm_ok)

    # ---------------- S3 the certified computation
    section("S3 -- THE CERTIFIED COMPUTATION (truncated vs "
            "extended comb)")
    amax = max(audit[kz]["rr"]["alpha"] for kz in DEEP)
    NEXT = int(math.ceil(math.exp(2.0 * amax))) + 1
    print("    extended von Mangoldt table: sieving to %d "
          "..." % NEXT, flush=True)
    LAM_EXT = core.von_mangoldt_table(NEXT)
    NN_EXT = np.nonzero(LAM_EXT > 0.0)[0]
    U_EXT = np.log(NN_EXT.astype(float))
    MU_EXT = 2.0 * LAM_EXT[NN_EXT] / np.sqrt(
        NN_EXT.astype(float))
    print("    table sieved: %d events (%.1f s)"
          % (len(NN_EXT), time.time() - T0))

    ident_ok = True
    ref_ok = True
    krein_reg_ok = True
    results = {}
    for kz in sorted(set(CONTROLS) | set(DEEP)):
        t1_ = time.time()
        rr = audit[kz]["rr"]
        rrx = build_window_ext(kz, U_EXT, MU_EXT)
        tail = float(np.sum(MU_EXT[
            (NN_EXT > core.ATOM_MAX)
            & (U_EXT <= 2.0 * rr["alpha"] + 1e-14)]))
        if kz in CONTROLS:
            # bit-equality against the DIRECT-form corner
            # (rr["Ah_dir"]); rr["Ah"] = B - S is the split
            # form, equal only to the split tolerance ~1e-6
            same = (len(rrx["uu"]) == len(rr["uu"])
                    and np.array_equal(rrx["uu"], rr["uu"])
                    and np.array_equal(rrx["mm"],
                                       2.0 * rr["lam"])
                    and float(np.max(np.abs(
                        rrx["Ah"] - rr["Ah_dir"]))) == 0.0)
            ident_ok &= same
        # corner certificates
        rr_tr = dict(rr)  # truncated window (original data)
        rr_tr["c_ar"] = np.asarray(
            core.arch_lags(rr["M"], rr["D"]), float)
        tr_lo, tr_hi = corner_enclosure(rr_tr)
        ex_lo, ex_hi = corner_enclosure(rrx)
        if kz in TAU_REFS:
            ref_ok &= abs(0.5 * (ex_lo + ex_hi)
                          - TAU_REFS[kz]) / TAU_REFS[kz] \
                <= 1e-4
        # full-A floor (extended)
        lfA, loA, hiA = sign_cert(rrx["A_full"])
        # Krein floor: truncated regression + extended
        bt = gnu.build_rung(kz)
        lam1_tr = float(np.linalg.eigvalsh(bt["Delta"])[0])
        if kz in KREIN_TRUNC_REFS:
            krein_reg_ok &= abs(lam1_tr - KREIN_TRUNC_REFS[kz]
                                ) / abs(KREIN_TRUNC_REFS[kz]) \
                <= 2e-2
        if kz in KREIN_POS_REF:
            krein_reg_ok &= abs(lam1_tr - KREIN_POS_REF[kz]
                                ) / KREIN_POS_REF[kz] <= 1e-2
        bx = gnu.build_rung(kz, comb=(rrx["uu"], rrx["mm"]))
        lfD, loD, hiD = sign_cert(bx["Delta"])
        results[kz] = dict(tr=(tr_lo, tr_hi),
                           ex=(ex_lo, ex_hi), tail=tail,
                           lfA=lfA, loA=loA, hiA=hiA,
                           lam1_tr=lam1_tr, lfD=lfD,
                           loD=loD, hiD=hiD)
        print("\n    kz %-4d (h %d, alpha %.3f, missing tail "
              "mass %.3e) [%.0f s]:"
              % (kz, rr["h"], rr["alpha"], tail,
                 time.time() - t1_))
        print("      corner tau_X truncated [%+.4e, %+.4e]  "
              "extended [%+.4e, %+.4e]"
              % (tr_lo, tr_hi, ex_lo, ex_hi))
        print("      full-A floor extended: float %+.4e, "
              "cert-lo %s, cert-hi %+.4e"
              % (lfA, "%+.4e" % loA if loA is not None
                 else "none", hiA))
        print("      Krein lam1: truncated %+.4e -> extended "
              "float %+.4e, cert-lo %s, cert-hi %+.4e"
              % (lam1_tr, lfD, "%+.4e" % loD
                 if loD is not None else "none", hiD),
              flush=True)
    check("S3.1 [IDENTITY WARD] the extended builder is the "
          "identity on the control rungs (bit-equal atoms, "
          "Ah unchanged)", ident_ok)
    check("S3.2 [SKELETON REGRESSION] extended corner "
          "enclosures reproduce the certified refs at kz "
          "9/13 (rel 1e-4)", ref_ok)
    check("S3.3 [QUICK-READOUT REGRESSION] the truncated "
          "Krein floors reproduce the two probes' negatives "
          "at kz 177/243 and the positive at kz 9",
          krein_reg_ok)

    # decisive sign census on the deep rungs
    frontier = []
    negative = []
    positive = []
    for kz in DEEP:
        r = results[kz]
        pos = (r["ex"][0] > 0.0 and r["loA"] is not None
               and r["loA"] > 0.0 and r["loD"] is not None
               and r["loD"] > 0.0)
        neg = r["ex"][1] < 0.0 or r["hiA"] < 0.0 \
            or r["hiD"] < 0.0
        if pos:
            positive.append(kz)
        elif neg:
            negative.append(kz)
        else:
            mid = mp_corner(build_window_ext(kz, U_EXT,
                                             MU_EXT))
            print("    kz %d straddle -> mp dps-60 corner "
                  "midpoint %+.6e" % (kz, mid))
            frontier.append(kz)
    check("S3.4 [THE DECISIVE SIGN] every deep rung's "
          "extended floor is strictly positive at "
          "certificate grade (positive: %s, negative: %s, "
          "frontier: %s)" % (positive, negative, frontier),
          len(positive) == len(DEEP))
    trunc_neg = all(results[kz]["lam1_tr"] < 0.0
                    or results[kz]["tr"][1] < 0.0
                    for kz in DEEP)

    # ---------------- S4 synthesis
    section("S4 -- SYNTHESIS: the certified sign table")
    print("    kz    admissible(deployed)  truncated-Krein  "
          "extended-tau_X-cert     extended-Krein-cert")
    for kz in sorted(set(CONTROLS) | set(DEEP)):
        r = results[kz]
        print("    %-5d %-21s %+11.4e     [%+.3e, %+.3e]  "
              "lo %s"
              % (kz, "yes" if audit[kz]["complete"]
                 else "NO (comb truncated)", r["lam1_tr"],
                 r["ex"][0], r["ex"][1],
                 "%+.3e" % r["loD"] if r["loD"] is not None
                 else "none"))

    # ---------------- V verdict
    section("V -- FROZEN VERDICT + per-probe consequences")
    if len(positive) == len(DEEP) and trunc_neg and ident_ok \
            and ref_ok and krein_reg_ok:
        verdict = "DEEP-ALPHA-ARTIFACT"
    elif negative:
        fam = "OUT-OF-FAMILY" if all(
            not audit[kz]["complete"] for kz in negative) \
            else "IN-FAMILY"
        verdict = "DEEP-ALPHA-NEGATIVE-CERTIFIED (%s)" % fam
    else:
        verdict = "DEEP-ALPHA-FRONTIER (%s)" % frontier
    print("\n  VERDICT: %s" % verdict)
    if verdict != "DEEP-ALPHA-ARTIFACT":
        print("""
  TYPED (non-artifact outcome): the extended-comb certified
  readouts did NOT come back uniformly positive -- positive
  %s, negative %s, frontier %s.  A certified negative on an
  extended (complete-comb) rung would be the first measured
  negative canonical window (H_cof unaffected: cofinality
  needs only a subsequence); a frontier rung is a precision
  limit, typed above.  The truncation mechanism of S1/S2
  still stands for the DEPLOYED readouts.  NO RH claim."""
              % (positive, negative, frontier))
    else:
        print("""
  THE ARTIFACT, TYPED: the negative floors at kz 142/177/243
  were COMB-TRUNCATION artifacts.  Those windows demand comb
  support up to e^{2 alpha} = 4.4e5 / 8.0e5 / 1.8e6, but the
  deployed table caps at 4.0e5; core.build_window silently
  truncated the tent assembly there (missing Lambda-mass
  typed per rung above), breaking the explicit-formula
  balance and driving the measured floors to O(-100).  With
  the COMPLETE canonical comb the certified corner enclosure
  and the Cholesky-certified full and Krein floors are
  strictly positive on all three rungs.  The certified
  ladder's end at kz 121 was the atom-table data boundary --
  exactly the admissibility line A3.

  PER-PROBE CONSEQUENCES:
  - pi_resonance_anatomy "premise collapse at kz 177/243":
    CONFOUNDED -- the Loewner collapse was the truncation,
    not deep-alpha physics; its certified-rung findings
    (thick resonance, zero soft overlap, excision-blind
    razor) used kz <= 121 + 90/116 readouts and STAND.
  - the Cotlar alpha-law and the neg-mass-vs-alpha law:
    PARTIALLY CONFOUNDED at kz 177/243 (the two deepest
    points mix truncation with alpha); the trends on the
    complete-comb rungs must be re-read before reuse.
  - residual_quadrature "47/47 sign agreement": STRENGTHENED
    -- the residual horizon detected the (truncated) sign
    correctly either way; but its "stall = deep-alpha" law
    must be re-read as "stall = truncated comb".
  - H_cof: UNAFFECTED -- no measured negative window exists
    in the canonical family; the cofinal sequence should be
    drawn from windows satisfying A3 (complete comb), which
    is a DATA constraint, not a structural alpha ceiling.
  NO RH claim.""")
    npass = sum(1 for _n, ok in CHECKS if ok)
    print("\n[TIME] %.1f min   [CHECKS] %d run, %d failed%s"
          % ((time.time() - T0) / 60.0, len(CHECKS),
             len(FAILS),
             ("  " + ",".join(FAILS)) if FAILS else ""))
    return 0 if npass == len(CHECKS) else 1


if __name__ == "__main__":
    raise SystemExit(main())
'''

_SRC_COTLAR = r'''
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""cotlar_v2_complete_comb_probe -- PRIME.PRUEFER.COMPENSATION.02
+ PRIME.TRUNCATION.AUDIT.01
(EXPLORATION ONLY, experiments/; direct follow-up to the
DEEP-ALPHA-ARTIFACT verdict, 2026-08-08 night).

TASK 1 -- THE COTLAR RE-DECISION (v2).  The executed v1
contract (pruefer_compensation_probe.py, FROZEN_SPEC SHA-256
4621b89958531d6d3baae9fe762dbd10d23dc22eed77a57aa1c6b179a744
0811) fired COTLAR-GROWING on the deep holdouts kz 142/177/
243 -- which deep_alpha_sign_probe proved were COMB-TRUNCATED
(core.build_window silently drops all events beyond ATOM_MAX
= 400000; those windows demand support to 1.8e6).  The v1
verdict stands on its own rules FOR THE DATA AS MEASURED; the
scientific question reopens.  V2 PROTOCOL (frozen here):
IDENTICAL cells, pairing, danger geometry, Cotlar sums, and
decision bars as v1 (ppc machinery imported READ-ONLY; the
phases/cells via ppc.deployed_cells VERBATIM); THE SINGLE
SUBSTANTIVE CHANGE: the deep holdouts are built with the
COMPLETE canonical comb (the deep_alpha_sign extended-table
machinery: von_mangoldt_table(ceil(e^{2 alpha_max})+1), comb
= (U_EXT[:ka], MU_EXT[:ka]) passed through build_rung's comb
port).  One PERFORMANCE substitution, warded for exactness:
the 16x16 cross-norm census computes the identical spectral
norms through ||X_r^* X_s||_2^2 = lam_max(P_r^{1/2} P_s
P_r^{1/2}) with P_r = X_r X_r^* (dense eigh, no iteration)
and ||X_r X_s^*||_2 by direct SVD of the r_- x r_- product;
equivalence ward vs ppc.cross_norms at kz 9 (rel <= 1e-8)
and full-readout ward vs ppc.rung_readouts at kz 9.

TASK 2 -- THE TRUNCATION AUDIT: which recent findings used
windows with comb demand > ATOM_MAX, and does each conclusion
depend on them (CONFOUNDED / ROBUST / UNAFFECTED, typed); the
polygon export is RE-RUN at the three corrected rungs (the
cheap hardening of its holdout rows).

VERDICT (frozen): COTLAR-GROWING-CONFIRMED (the frozen v1
decision rule still says GROWING on complete-comb data -- the
route stays dead, now clean) / COTLAR-BOUNDED-V2 (the v1 kill
was the truncation artifact -- the route REOPENS; run 3
executes: the analytic envelope candidate) / COTLAR-PARTIAL-
V2 (typed).  NO RH claim; writes nothing; no .md; no commits.

ADDENDUM v1.1 (post first execution, typed refinement of the
AUDIT check A.1 only -- no Cotlar quantity, bar, or decision
rule touched): the polygon re-run at the complete-comb deep
rungs OVERFLOWS phase_polygon's raw-longdouble prefix
machinery (exp(l2m) > longdouble max at the complete-comb
mass; margins NaN/inf) -- the frozen A.1 conflated "polygon
breaks" with "machinery out of numeric range".  A.1 now types
each rung: HOLDS (finite margins, no negative prefix) /
REFUTED (finite margins, negative prefix -- fails) /
NUMERIC-VOID (non-finite margins -- the polygon holdout rows
are VOID at complete combs, neither confirmed nor refuted;
the phase_polygon verdict remains battery-driven ROBUST on
in-cap rungs only).  Run-1/run-2/run-3 outputs of the first
execution reproduce bit-identically (deterministic pipeline).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/cotlar_v2_complete_comb_probe.py
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

import v563_paper2_readouts as core            # noqa: E402  (READ-ONLY)
import gauss_node_unitary_probe as gnu         # noqa: E402  (READ-ONLY)
import pruefer_compensation_probe as ppc       # noqa: E402  (READ-ONLY)
import phase_polygon_probe as ppg              # noqa: E402  (READ-ONLY)

FROZEN_SPEC = """\
PRIME.PRUEFER.COMPENSATION.02 + PRIME.TRUNCATION.AUDIT.01
spec v1 (2026-08-08, frozen before run).  V1 CONTRACT QUOTED:
SPEC SHA 4621b89958531d6d3baae9fe762dbd10d23dc22eed77a57aa1c6
b179a7440811 (verified at run time against ppc.FROZEN_SPEC).
V2 = v1 VERBATIM (cells: 16 equal pi/8 cells on delta theta;
entrywise pairing; danger DGR1 {0,15} u DGR2 {7,8}; Cotlar
S_X = max_r sum_s sqrt||X_r^* X_s||, B = sqrt(S S*); battery
= the 42 frame-a rungs h <= 900; holdouts kz {90, 116, 142,
177, 243}; DECISION per S_U/S_C: BOUNDED iff holdout max <=
1.2 x battery max AND OLS slope of log S vs log h over
battery+holdouts <= 0.10; GROWING iff slope >= 0.20 OR (S vs
log h linear R^2 >= 0.9 with positive slope); else PARTIAL)
with the SINGLE substantive change: holdout windows built
with the COMPLETE comb via build_rung(comb=(U_EXT[:ka],
MU_EXT[:ka])), U/MU_EXT from von_mangoldt_table(ceil(e^{2
alpha_243})+1); in-cap rungs untouched (bit-equality ward of
comb_ext vs deployed comb on kz 9 + first battery rung).
PERFORMANCE substitution (warded): cross norms via the exact
Gram identities above; wards W-N1 rel <= 1e-8 vs
ppc.cross_norms at kz 9, W-N2 full readout triple (S_U, S_C,
danger) vs ppc.rung_readouts at kz 9 rel <= 1e-10.
Regressions: danger share kz 9 in [0.316, 0.356]; extended
Krein floors at kz 142/177/243 reproduce deep_alpha_sign
(+1.2389e-8 / +1.3284e-8 / +6.6742e-9, rel 0.2) -- read from
the SAME complete builds; truncated holdout sums recomputed
at kz 142/177/243 for the contrast column (the v1-as-measured
values).  RUN 1 (anchors, in-cap == v1): danger share,
negativity capture, env Spearman.  RUN 2: the decision table
+ frozen rule on complete data.  RUN 3 only if BOTH S_U and
S_C BOUNDED: K_p(h) = max_d env(d)(1+d)^p (p = 1 U, 2 C)
h-stability, holdout max <= 1.2 x anchor max, delta_coef
reported.  Epstein/scramble contrast at kz 9 (v1 bars: >= 25
percent triple deviation in >= 1 component AND eps ratio >= 5
or env-Spearman break).  AUDIT (typed table): probes x rungs
x truncation x dependence; polygon export re-run at complete
kz 142/177/243 (x0 = 0; ROBUST iff still no negative prefix).
VERDICTS: COTLAR-GROWING-CONFIRMED / COTLAR-BOUNDED-V2 /
COTLAR-PARTIAL-V2 (+ the audit table).  NO RH claim; writes
nothing."""

V1_SHA = ("4621b89958531d6d3baae9fe762dbd10d23dc22eed77a57a"
          "a1c6b179a7440811")
DEEP = (142, 177, 243)
HOLDOUTS = ppc.HOLDOUTS            # (90, 116, 142, 177, 243)
ANCHORS = ppc.ANCHORS              # (9, 12, 13, 26, 40)
DANGER_SHARE_KZ9 = (0.316, 0.356)
KREIN_EXT_REFS = {142: 1.2389e-8, 177: 1.3284e-8,
                  243: 6.6742e-9}
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


def ast_scan(banned):
    src = open(os.path.abspath(__file__), encoding="utf-8").read()
    bad = []
    for node in ast.walk(ast.parse(src)):
        name = None
        if isinstance(node, ast.Name):
            name = node.id
        elif isinstance(node, ast.Attribute):
            name = node.attr
        if name and name.lower() in banned:
            bad.append(name)
    return bad


# ------------------------------------------------ extended comb
def build_ext_table():
    amax = max(float(core.U_ALL[kz]) for kz in DEEP)
    NEXT = int(math.ceil(math.exp(2.0 * amax))) + 1
    LAM_EXT = core.von_mangoldt_table(NEXT)
    NN = np.nonzero(LAM_EXT > 0.0)[0]
    U = np.log(NN.astype(float))
    MU = 2.0 * LAM_EXT[NN] / np.sqrt(NN.astype(float))
    return U, MU


U_EXT, MU_EXT = None, None


def comb_ext(kz):
    rr = core.build_window(kz)
    ka = int(np.searchsorted(U_EXT,
                             2.0 * rr["alpha"] + 1.0e-14,
                             side="right"))
    return U_EXT[:ka].copy(), MU_EXT[:ka].copy()


# ------------------------------------------------ fast cross norms
def cross_norms_fast(pieces):
    """The v1 quantities ||X_r^* X_s||_2 and ||X_r X_s^*||_2
    via exact Gram identities (dense eigh/SVD, no
    iteration)."""
    C = ppc.CELLS
    P = [X @ X.conj().T for X in pieces]
    Ph = []
    for Pr in P:
        Ps = 0.5 * (Pr + Pr.conj().T)
        w, V = np.linalg.eigh(Ps)
        w = np.sqrt(np.clip(w, 0.0, None))
        Ph.append((V * w) @ V.conj().T)
    N = np.zeros((C, C))
    Ns = np.zeros((C, C))
    for r in range(C):
        for s in range(r, C):
            Mrs = Ph[r] @ P[s] @ Ph[r]
            Mrs = 0.5 * (Mrs + Mrs.conj().T)
            lmx = float(np.linalg.eigvalsh(Mrs)[-1])
            N[r, s] = N[s, r] = math.sqrt(max(lmx, 0.0))
            G = pieces[r] @ pieces[s].conj().T
            sv = np.linalg.svd(G, compute_uv=False)
            Ns[r, s] = Ns[s, r] = float(sv[0]) if len(sv) \
                else 0.0
    return N, Ns


def readouts_v2(kz, **kw):
    """ppc.rung_readouts VERBATIM with the fast norm census
    (the only substitution; warded)."""
    dc, err = ppc.deployed_cells(kz, **kw)
    if dc is None:
        return None, err
    b, go, cell = dc["b"], dc["go"], dc["cell"]
    if b["h"] > 1500:
        return None, "skip-h"
    ch = dc["chains"]
    Jp = np.diag(ch["alp"]) + np.diag(ch["bep"][:len(
        ch["alp"]) - 1], 1) + np.diag(ch["bep"][:len(
            ch["alp"]) - 1], -1)
    evp = np.linalg.eigvalsh(Jp)
    nodew = float(np.max(np.abs(np.sort(evp)
                                - np.sort(np.cos(go["thp"])))))
    U = go["U"]
    Dm2 = go["Dm"] ** 2
    Cc = go["Dm"][:, None] * U
    pu = ppc.split_pieces(U, cell)
    pc = ppc.split_pieces(Cc, cell)
    compl_u = float(np.max(np.abs(sum(pu) - U)))
    compl_c = float(np.max(np.abs(sum(pc) - Cc)))
    Nu, Nus = cross_norms_fast(pu)
    Nc, Ncs = cross_norms_fast(pc)
    Su, Sus, Bu = ppc.cotlar_sums(Nu, Nus)
    Sc, Scs, Bc = ppc.cotlar_sums(Nc, Ncs)
    dgr = set(ppc.DGR1) | set(ppc.DGR2)
    tot = float(np.sum(Nu))
    dmask = np.zeros((ppc.CELLS, ppc.CELLS), bool)
    for r in range(ppc.CELLS):
        for s in range(ppc.CELLS):
            dmask[r, s] = (r in dgr) or (s in dgr)
    dshare = float(np.sum(Nu[dmask])) / max(tot, 1e-300)
    h = b["h"]
    wr = np.array([float(np.sum(np.abs(p) ** 2)) for p in pu])
    wr = wr / max(float(np.sum(wr)), 1e-300)
    eps = []
    for r in range(ppc.CELLS):
        Ar = pu[r]
        Mr = wr[r] * np.eye(h) - Ar.conj().T \
            @ (Dm2[:, None] * Ar)
        Mr = 0.5 * (Mr + Mr.conj().T)
        eps.append(max(0.0, -float(np.linalg.eigvalsh(Mr)[0])))
    T1 = np.eye(h) - U.conj().T @ U
    T1 = 0.5 * (T1 + T1.conj().T)
    lmin_T1 = float(np.linalg.eigvalsh(T1)[0])
    Udgr = sum(pu[r] for r in sorted(dgr))
    T1d = np.eye(h) - Udgr.conj().T @ Udgr
    T1d = 0.5 * (T1d + T1d.conj().T)
    lmin_d = float(np.linalg.eigvalsh(T1d)[0])
    env_u = ppc.envelope(Nu)
    env_c = ppc.envelope(Nc)
    sp_u = ppc.spearman(env_u[:9], np.arange(9.0))
    sp_c = ppc.spearman(env_c[:9], np.arange(9.0))
    lam1 = float(np.linalg.eigvalsh(b["Delta"])[0])
    return dict(kz=kz, h=h, nodew=nodew,
                compl=max(compl_u, compl_c), Su=Su, Sus=Sus,
                Bu=Bu, Sc=Sc, Scs=Scs, Bc=Bc, dshare=dshare,
                eps_sum=float(np.sum(eps)), eps=eps,
                lmin_T1=lmin_T1, lmin_d=lmin_d, env_u=env_u,
                env_c=env_c, sp_u=sp_u, sp_c=sp_c, Nu=Nu,
                Nc=Nc, lam1=lam1, b=b,
                chains=dc["chains"]), None


def decide(series, ix):
    """The frozen v1 decision rule on one sum column."""
    bat = [x for x in series if x["tag"] == "battery"]
    hol = [x for x in series if x["tag"] == "HOLDOUT"]
    mb = max(x[ix] for x in bat)
    mh = max(x[ix] for x in hol)
    hh = np.log([float(x["h"]) for x in series])
    ss = np.log([x[ix] for x in series])
    slope = float(np.polyfit(hh, ss, 1)[0])
    # log-growth clause: S vs log h linear, R^2 >= 0.9
    sl2, ic2 = np.polyfit(hh, np.exp(ss), 1)
    pred = sl2 * hh + ic2
    resid = np.exp(ss) - pred
    r2 = 1.0 - float(np.sum(resid ** 2)) \
        / max(float(np.sum((np.exp(ss)
                            - np.mean(np.exp(ss))) ** 2)),
              1e-300)
    if mh <= 1.2 * mb and slope <= 0.10:
        v = "BOUNDED"
    elif slope >= 0.20 or (r2 >= 0.9 and sl2 > 0.0):
        v = "GROWING"
    else:
        v = "PARTIAL"
    return v, mb, mh, slope, r2


# ================================================================= main
def main():
    global U_EXT, MU_EXT
    section("PRIME.PRUEFER.COMPENSATION.02 -- the Cotlar "
            "re-decision on complete combs (EXPLORATION ONLY)")
    sha = hashlib.sha256(FROZEN_SPEC.encode("utf-8")).hexdigest()
    print("    FROZEN_SPEC SHA-256 = %s" % sha)
    print("    NO RH claim.")
    print("\nS0 -- firewall + the v1 contract")
    check("S0.1 AST firewall clean (no zero/prime oracles)",
          not ast_scan(BANNED_IDS))
    v1sha = hashlib.sha256(
        ppc.FROZEN_SPEC.encode("utf-8")).hexdigest()
    check("S0.2 [V1 CONTRACT] the committed v1 spec hash "
          "matches the quoted SHA (%s...)" % v1sha[:8],
          v1sha == V1_SHA)

    # ---------------- S1 machinery wards
    section("S1 -- machinery wards (the single change, "
            "fenced)")
    t_ = time.time()
    U_EXT, MU_EXT = build_ext_table()
    print("    extended table: %d events to %d (%.1f s)"
          % (len(U_EXT), int(round(math.exp(U_EXT[-1]))),
             time.time() - t_))
    # W-N1: fast norms == dense norms on the kz-9 pieces
    dc9, _ = ppc.deployed_cells(9)
    U9 = dc9["go"]["U"]
    pu9 = ppc.split_pieces(U9, dc9["cell"])
    Nd, Nds = ppc.cross_norms(pu9)
    Nf, Nfs = cross_norms_fast(pu9)
    dev = max(float(np.max(np.abs(Nf - Nd)
                           / np.maximum(Nd, 1e-12))),
              float(np.max(np.abs(Nfs - Nds)
                           / np.maximum(Nds, 1e-12))))
    check("W-N1 [NORM EQUIVALENCE] fast Gram-identity norms "
          "== ppc.cross_norms on the kz-9 pieces (max rel "
          "%.1e <= 1e-8)" % dev, dev <= 1e-8)
    r9v1, _ = ppc.rung_readouts(9)
    r9v2, _ = readouts_v2(9)
    tri1 = np.array([r9v1["Su"], r9v1["Sc"], r9v1["dshare"]])
    tri2 = np.array([r9v2["Su"], r9v2["Sc"], r9v2["dshare"]])
    reldev = float(np.max(np.abs(tri2 - tri1) / tri1))
    check("W-N2 [READOUT EQUIVALENCE] v2 readout triple == "
          "v1 at kz 9 (max rel %.1e <= 1e-10); danger share "
          "%.3f in [%.3f, %.3f]"
          % (reldev, r9v2["dshare"], *DANGER_SHARE_KZ9),
          reldev <= 1e-10
          and DANGER_SHARE_KZ9[0] <= r9v2["dshare"]
          <= DANGER_SHARE_KZ9[1])
    battery = ppc.battery_rungs()
    incap = all(math.exp(2.0 * core.build_window(kz)["alpha"])
                <= core.ATOM_MAX + 0.5
                for kz in battery + [90, 116])
    ue, me = comb_ext(9)
    rr9 = core.build_window(9)
    same9 = (np.array_equal(ue, np.asarray(rr9["uu"]))
             and np.array_equal(me, 2.0 * np.asarray(
                 rr9["lam"])))
    ueb, meb = comb_ext(battery[-1])
    rrb = core.build_window(battery[-1])
    sameb = (np.array_equal(ueb, np.asarray(rrb["uu"]))
             and np.array_equal(meb, 2.0 * np.asarray(
                 rrb["lam"])))
    check("W-N3 [SINGLE-CHANGE WARD] all 42 battery rungs + "
          "kz 90/116 are in-cap (complete already) and "
          "comb_ext is bit-identical to the deployed comb on "
          "kz 9 and kz %d" % battery[-1],
          incap and same9 and sameb)

    # ---------------- RUN 1 (anchors; in-cap == v1)
    section("RUN 1 (v2) -- anatomy on the anchors (in-cap: "
            "identical to v1 by W-N3)")
    cache = {}
    for kz in ANCHORS:
        r, err = readouts_v2(kz)
        cache[kz] = r
        print("    kz %-3d h %-4d: danger share %.3f | "
              "lam_min(T1) %+ .4f vs danger-trunc %+ .4f "
              "(capture %.2f) | sum eps_r %.3e | env "
              "Spearman U/C %.2f/%.2f"
              % (kz, r["h"], r["dshare"], r["lmin_T1"],
                 r["lmin_d"],
                 (r["lmin_d"] / r["lmin_T1"])
                 if r["lmin_T1"] < 0 else float("nan"),
                 r["eps_sum"], r["sp_u"], r["sp_c"]),
              flush=True)

    # ---------------- RUN 2 (the decision)
    section("RUN 2 (v2) -- Cotlar sums: battery + COMPLETE "
            "holdouts (+ the truncated contrast)")
    series = []
    for kz in battery:
        r = cache.get(kz)
        if r is None:
            r, err = readouts_v2(kz)
            if r is None:
                print("    kz %d: %s" % (kz, err))
                continue
        series.append(dict(kz=kz, h=r["h"], Su=r["Su"],
                           Sc=r["Sc"], Bu=r["Bu"],
                           Bc=r["Bc"], tag="battery"))
        print("    kz %-4d h %-4d [battery]: S_U %.4f  "
              "S_C %.4f  B_U %.4f  B_C %.4f"
              % (kz, r["h"], r["Su"], r["Sc"], r["Bu"],
                 r["Bc"]), flush=True)
    krein_ok = True
    trunc_contrast = {}
    hold_res = {}
    for kz in HOLDOUTS:
        kw = {}
        if kz in DEEP:
            kw = dict(comb=comb_ext(kz))
            rt, errt = readouts_v2(kz)      # truncated (v1)
            if rt is not None:
                trunc_contrast[kz] = (rt["Su"], rt["Sc"],
                                      rt["lam1"])
        r, err = readouts_v2(kz, **kw)
        if r is None:
            print("    kz %d: %s" % (kz, err))
            continue
        hold_res[kz] = r
        if kz in DEEP:
            krein_ok &= abs(r["lam1"] - KREIN_EXT_REFS[kz]) \
                / KREIN_EXT_REFS[kz] <= 0.2
        series.append(dict(kz=kz, h=r["h"], Su=r["Su"],
                           Sc=r["Sc"], Bu=r["Bu"],
                           Bc=r["Bc"], tag="HOLDOUT"))
        tc = trunc_contrast.get(kz)
        print("    kz %-4d h %-4d [HOLDOUT%s]: S_U %.4f  "
              "S_C %.4f  B_U %.4f  B_C %.4f   lam1 %+.3e%s"
              % (kz, r["h"],
                 ", COMPLETE comb" if kz in DEEP else "",
                 r["Su"], r["Sc"], r["Bu"], r["Bc"],
                 r["lam1"],
                 ("   [truncated v1: S_U %.2f S_C %.2f "
                  "lam1 %+.1e]" % tc) if tc else ""),
              flush=True)
    check("R2.1 [DEEP-ALPHA REGRESSION] the complete-comb "
          "Krein floors at kz 142/177/243 reproduce "
          "deep_alpha_sign (rel 0.2) and are positive",
          krein_ok and all(hold_res[kz]["lam1"] > 0.0
                           for kz in DEEP if kz in hold_res))
    verdicts = {}
    for lbl, ix in (("S_U", "Su"), ("S_C", "Sc")):
        v, mb, mh, slope, r2 = decide(series, ix)
        verdicts[lbl] = v
        print("    %s: battery max %.4f, holdout max %.4f "
              "(ratio %.2f, bar 1.2), log-log slope %.3f "
              "(bars 0.10/0.20), lin R^2 %.2f -> %s"
              % (lbl, mb, mh, mh / mb, slope, r2, v))

    # Epstein/scramble contrast at kz 9 (v1 regression)
    print("\n    controls at kz 9 (v1 bars):")
    rt9 = cache[9]
    rr9w = core.build_window(9)
    N_E = int(math.floor(math.exp(2.0 * rr9w["alpha"]))) + 1
    lamE = gnu.lambda_eps(N_E)
    nn = np.nonzero(np.abs(lamE) > 1e-12)[0]
    ctrl_ok = True
    for nmc, kw in (("Epstein", dict(comb=(
            np.log(nn.astype(float)),
            2.0 * lamE[nn] / np.sqrt(nn.astype(float))))),
            ("scramble", dict(scramble_seed=1))):
        rc, err = readouts_v2(9, **kw)
        if rc is None:
            print("    %-8s: %s (typed)" % (nmc, err))
            continue
        tri_t = np.array([rt9["Su"], rt9["Sc"],
                          rt9["dshare"]])
        tri_c = np.array([rc["Su"], rc["Sc"], rc["dshare"]])
        rel = float(np.max(np.abs(tri_c - tri_t)
                           / np.maximum(tri_t, 1e-12)))
        okc = rel >= 0.25 and (rc["eps_sum"]
                               >= 5.0 * rt9["eps_sum"]
                               or rc["sp_u"] > -0.8)
        ctrl_ok &= okc
        print("    %-8s: (S_U, S_C, danger) = (%.3f, %.3f, "
              "%.3f) vs truth (%.3f, %.3f, %.3f): max rel "
              "%.0f%%; eps ratio %.1f; env Spearman U %.2f "
              "-> %s"
              % (nmc, *tri_c, *tri_t, 100 * rel,
                 rc["eps_sum"] / max(rt9["eps_sum"], 1e-300),
                 rc["sp_u"], "breaks" if okc else "FAILS"))
    check("R2.2 [DISCRIMINATION] Epstein and scramble break "
          "the v1 contrast bars", ctrl_ok)

    # ---------------- RUN 3 (only if BOUNDED on both)
    bounded = all(v == "BOUNDED" for v in verdicts.values())
    if bounded:
        section("RUN 3 (v2) -- the analytic envelope "
                "candidate (unlocked by BOUNDED)")
        refs = []
        for kz in list(ANCHORS) + list(HOLDOUTS):
            r = cache.get(kz) or hold_res.get(kz)
            if r is None:
                continue
            ch = r["chains"]

            # MECHANICAL FIX of the v1 run3 line (never
            # executed there: v1 stopped at GROWING): the
            # verbatim v1 expression broadcasts (n-1,) against
            # (n-2,); the intended coefficient drift is the
            # aligned sum.
            def _drift(al, be):
                d1 = np.abs(np.diff(al))
                d2 = np.abs(np.diff(be[:len(al) - 1]))
                m = min(len(d1), len(d2))
                if m == 0:
                    return float(np.max(d1)) if len(d1) \
                        else 0.0
                return float(np.max(d1[:m] + d2[:m]))
            dco = max(_drift(ch["alp"], ch["bep"]),
                      _drift(ch["alm"], ch["bem"]))
            dd = np.arange(len(r["env_u"]), dtype=float)
            K1 = float(np.max(r["env_u"] * (1.0 + dd)))
            K2 = float(np.max(r["env_c"] * (1.0 + dd) ** 2))
            tag = "HOLDOUT" if kz in HOLDOUTS else "anchor"
            refs.append((kz, tag, K1, K2))
            print("    kz %-4d h %-4d [%s]: K_1 = %.4f, "
                  "K_2 = %.4f, delta_coef = %.3e"
                  % (kz, r["h"], tag, K1, K2, dco))
        run3_ok = True
        for lbl, ix in (("K_1", 2), ("K_2", 3)):
            mb = max(x[ix] for x in refs if x[1] == "anchor")
            mh = max(x[ix] for x in refs
                     if x[1] == "HOLDOUT")
            stab = mh <= 1.2 * mb
            run3_ok &= stab
            print("    %s: anchor max %.4f, holdout max "
                  "%.4f -> h-stable: %s (bar 1.2x)"
                  % (lbl, mb, mh, stab))
        check("R3.1 [ENVELOPE CANDIDATE] K_1 and K_2 are "
              "h-stable on the complete-comb holdouts",
              run3_ok)

    # ---------------- TASK 2: the truncation audit
    section("AUDIT -- comb-truncation census of the recent "
            "waves")
    print("""    cap: ATOM_MAX = %d (log %.4f); truncated
    frame-A rungs: kz 142 (X 4.4e5), 177 (7.9e5), 243
    (1.8e6); every h <= 900 battery rung and kz 90/116/121
    are complete (W-N3).

    probe                     truncated rungs used   verdict dependence
    ---------------------------------------------------------------
    pruefer_compensation v1   142/177/243 (3/5 hold) CONFOUNDED -- the
      COTLAR-GROWING decision leaned on the holdout max/slope;
      re-decided by THIS probe (v2 verdict below).
    phase_polygon             142/177/243 (3/5 hold) battery-driven;
      holdout rows were truncated-comb objects -> re-run below.
    residual_quadrature       142/177/243 (3/5 hold) ROBUST +
      STRENGTHENED -- the 47/47 sign agreement means the horizon
      detected the truncation-negatives correctly (a validated sign
      detector); the "stall = deep alpha" reading retypes to
      "stall = truncated comb".
    pi_resonance_anatomy      177/243 (deep-alpha pair) verdict
      RESONANCE-THICK ROBUST (decided on certified rungs: excision
      gain zero, soft overlap zero there); the S3b addendum
      ("alpha-law lives at the premise level") CONFOUNDED --
      retyped by deep_alpha_sign; the alpha/h quartet separation
      test is VOID (its deep-alpha pair was truncated).
    softport_radau17          none (h <= 900 ladder)  UNAFFECTED
    preconditioned_port       none (h <= 900 ladder)  UNAFFECTED
    cdcore / jacobi_uvarov    none (holdouts 40/49/60) UNAFFECTED
    excess_certified_skeleton none (filter excluded)  UNAFFECTED
    """ % (core.ATOM_MAX, math.log(core.ATOM_MAX)))
    print("    polygon re-run at the corrected rungs "
          "(x0 = 0, complete combs; ADDENDUM v1.1 typing):")
    poly_states = {}
    for kz in DEEP:
        b = hold_res[kz]["b"] if kz in hold_res \
            else gnu.build_rung(kz, comb=comb_ext(kz))
        import warnings
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", RuntimeWarning)
            pg = ppg.polygon_rung(b, 0.0)
        finite = (math.isfinite(pg["minrel"])
                  and math.isfinite(pg["fullrel"]))
        if not finite:
            st = "NUMERIC-VOID"
        elif pg["nneg"] == 0 and pg["fullmarg"] >= 0.0:
            st = "HOLDS"
        else:
            st = "REFUTED"
        poly_states[kz] = st
        print("    kz %-4d: #neg prefixes %d/%d, min rel "
              "margin %+.2e, full rel %+.2e  -> %s"
              % (kz, pg["nneg"], pg["M"], pg["minrel"],
                 pg["fullrel"], st))
    poly_void = any(v == "NUMERIC-VOID"
                    for v in poly_states.values())
    check("A.1 [POLYGON TYPING] no complete-comb deep rung "
          "REFUTES the polygon; states %s (VOID = raw-"
          "longdouble machinery out of range: the polygon "
          "holdout rows retype to VOID; the POLYGON-HOLDS "
          "verdict stays battery-driven ROBUST on in-cap "
          "rungs only)"
          % (sorted(poly_states.values()),),
          all(v in ("HOLDS", "NUMERIC-VOID")
              for v in poly_states.values()))

    # ---------------- V verdict
    section("V -- FROZEN VERDICTS + honest consequence")
    if all(v == "GROWING" for v in verdicts.values()):
        v2 = "COTLAR-GROWING-CONFIRMED"
    elif bounded:
        v2 = "COTLAR-BOUNDED-V2"
    else:
        v2 = "COTLAR-PARTIAL-V2 (S_U: %s, S_C: %s)" \
            % (verdicts["S_U"], verdicts["S_C"])
    print("\n  V2 COTLAR VERDICT: %s" % v2)
    if trunc_contrast:
        print("  truncated-vs-complete contrast at the deep "
              "holdouts:")
        for kz in DEEP:
            if kz in trunc_contrast and kz in hold_res:
                tS, tC, tl = trunc_contrast[kz]
                r = hold_res[kz]
                print("    kz %-4d: S_U %.2f -> %.2f, S_C "
                      "%.2f -> %.2f, lam1 %+.1e -> %+.1e"
                      % (kz, tS, r["Su"], tC, r["Sc"], tl,
                         r["lam1"]))
    print("""
  HONEST CONSEQUENCE: the v1 COTLAR-GROWING verdict stands
  ONLY as a statement about the truncated data (its own
  frozen rules, correctly applied to what was measured); the
  v2 verdict above is the scientific answer on complete
  combs, under bars, cells and pairing frozen identically to
  v1 (single change documented + warded).  The truncation
  audit retypes the affected findings; the residual-horizon
  sign detector emerges VALIDATED, the polygon holdout rows
  %s, and the resonance-anatomy
  quartet test is void.  NO RH claim."""
          % ("are HARDENED at the corrected rungs"
             if not poly_void else
             "retype to NUMERIC-VOID (out of longdouble "
             "range at complete combs; battery verdict "
             "unaffected)"))
    npass = sum(1 for _n, ok in CHECKS if ok)
    print("\n[TIME] %.1f min   [CHECKS] %d run, %d failed%s"
          % ((time.time() - T0) / 60.0, len(CHECKS),
             len(FAILS),
             ("  " + ",".join(FAILS)) if FAILS else ""))
    return 0 if npass == len(CHECKS) else 1


if __name__ == "__main__":
    raise SystemExit(main())
'''

# --------------------------------------------------------------- harness
_PF_RE = re.compile(r"^\s*\[(PASS|FAIL)\]\s+(\S+)", re.M)
_VD_RE = re.compile(r"VERDICT[:\]]")
_SHA_RE = re.compile(r"FROZEN_SPEC SHA-256[ :=]+([0-9a-f]{64})")


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


def _exec_probe(name, src):
    """Execute one embedded frozen probe source BYTE-EXACT in its own
    module namespace, registered under the probe's canonical import name;
    call its main(); capture and re-emit stdout."""
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
            entry = mod.__dict__.get("main")
            if callable(entry):
                rc = entry()
                code = 0 if rc is None else int(rc)
        except SystemExit as exc:
            code = 0 if exc.code is None else int(exc.code)
        except Exception:
            import traceback
            traceback.print_exc(file=sys.stdout)
            code = 99
    out = buf.getvalue()
    sys.stdout.write(out)
    sys.stdout.flush()
    return out, code, same


def _gate(name, out, code, same, exp_n, exp_fails, exp_verdict, exp_code,
          exp_sha, gates, extra=()):
    n, fails, verdict = _census(out)
    m = _SHA_RE.search(out)
    sha_ok = m is not None and m.group(1) == exp_sha
    ok = (n == exp_n and fails == list(exp_fails)
          and exp_verdict in verdict and code == exp_code
          and same is not False and sha_ok)
    for tag, pat in extra:
        hit = re.search(pat, out) is not None
        ok &= hit
        print("  [%s] EXTRA %s: /%s/" % ("PASS" if hit else "FAIL",
                                         tag, pat), flush=True)
    gates.append(ok)
    prov = ("byte-exact vs experiments source" if same is True else
            "embedded copy (source file not present)" if same is None
            else "SOURCE MISMATCH")
    print("\n[%s] PATTERN GATE %s: %d checks (exp %d) | FAILs %s (exp %s) "
          "| exit %d (exp %d) | spec SHA %s | %s\n      verdict line: %s"
          % ("PASS" if ok else "FAIL", name, n, exp_n,
             ",".join(fails) if fails else "none",
             ",".join(exp_fails) if exp_fails else "none",
             code, exp_code, "ok" if sha_ok else "MISMATCH", prov,
             verdict[:140]), flush=True)
    return ok


_PLAN = (
    ("deep_alpha_sign_probe", _SRC_DEEPALPHA, 8, (),
     "DEEP-ALPHA-ARTIFACT", 0, EXPECT_SHA_DEEPALPHA, (
         ("MECHANISM",
          r"kz 142/177/243 all demand comb support beyond the table cap "
          r"while 9/13/90/116/121 are complete"),
         ("DECISIVE-SIGN",
          r"every deep rung's extended floor is strictly positive at "
          r"certificate grade \(positive: \[142, 177, 243\], negative: "
          r"\[\], frontier: \[\]\)"),
         ("IDENTITY-WARD",
          r"the extended builder is the identity on the control rungs "
          r"\(bit-equal atoms, Ah unchanged\)"),
         ("TRUNCATED-REPRODUCED",
          r"the truncated Krein floors reproduce the two probes' "
          r"negatives at kz 177/243"),
     )),
    ("cotlar_v2_complete_comb_probe", _SRC_COTLAR, 9, (),
     "COTLAR-BOUNDED-V2", 0, EXPECT_SHA_COTLAR, (
         ("V1-CONTRACT-SHA",
          r"the committed v1 spec hash matches the quoted SHA "
          r"\(4621b899\.\.\.\)"),
         ("SU-BOUNDED",
          r"S_U: battery max 6\.\d+, holdout max 5\.9\d+ \(ratio 0\.9\d, "
          r"bar 1\.2\), log-log slope 0\.00\d \(bars 0\.10/0\.20\), lin "
          r"R\^2 0\.0\d -> BOUNDED"),
         ("SC-BOUNDED",
          r"S_C: battery max 4\.\d+, holdout max 4\.5\d+ \(ratio 0\.9\d, "
          r"bar 1\.2\), log-log slope 0\.00\d \(bars 0\.10/0\.20\), lin "
          r"R\^2 0\.0\d -> BOUNDED"),
         ("REVERSAL-CONTRAST",
          r"kz 142 : S_U 32\.07 -> 5\.6\d, S_C 58\.78 -> 4\.1\d, lam1 "
          r"-3\.3e\+02 -> \+1\.2e-08"),
         ("RUN3-UNLOCKED",
          r"\[PASS\] R3\.1 \[ENVELOPE CANDIDATE\] K_1 and K_2 are "
          r"h-stable on the complete-comb holdouts"),
         ("AUDIT-POLYGON-VOID",
          r"states \['NUMERIC-VOID', 'NUMERIC-VOID', 'NUMERIC-VOID'\]"),
         ("AUDIT-RESIDUAL-STRENGTHENED",
          r"residual_quadrature .*ROBUST \+"),
     )),
)


def run():
    t0 = time.time()
    print("=" * 74)
    print("v877 -- PRIME.DEEPALPHA.SIGN.01 + PRIME.PRUEFER.COMPENSATION.02")
    print("+ PRIME.TRUNCATION.AUDIT.01 (the artifact resolution and the "
          "Cotlar")
    print("REVERSAL: the deep-alpha negatives were ATOM_MAX comb-truncation")
    print("artifacts; on complete combs the preregistered route REOPENS "
          "with bounded")
    print("sums; the dated round-36 correction on PRIME.KREIN.CONTRACTOR.01 "
          "is carried")
    print("by this module; v873's v1 booking stands as-measured; NO RH "
          "claim)")
    print("=" * 74, flush=True)
    gates = []
    for (name, src, exp_n, exp_fails, exp_verdict, exp_code, exp_sha,
         extra) in _PLAN:
        print("\n" + "-" * 74)
        print("EMBEDDED FROZEN PROBE: %s" % name)
        print("-" * 74, flush=True)
        out, code, same = _exec_probe(name, src)
        _gate(name, out, code, same, exp_n, exp_fails, exp_verdict,
              exp_code, exp_sha, gates, extra)
    ok = all(gates)
    print("\n" + "=" * 74)
    print("v877: %d/%d probe pattern gates passed | runtime %.1f min"
          % (sum(gates), len(gates), (time.time() - t0) / 60.0))
    print("The discipline worked end to end: the residual horizon flagged "
          "the stall,")
    print("the artifact probe typed the silent truncation, the frozen v1 "
          "bars re-ran on")
    print("complete data and REVERSED the closure -- the correction is "
          "booked dated,")
    print("the v1 record stands as-measured, and the remaining gap is "
          "typed (B_C ~ 4")
    print("vs 1; local defects ~ 7-10).  NO RH claim.")
    print("[%s] v877 VERDICT GATE: DEEP-ALPHA-ARTIFACT + COTLAR-BOUNDED-V2 "
          "(the route reopens)" % ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(run())
