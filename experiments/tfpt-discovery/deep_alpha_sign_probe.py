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
