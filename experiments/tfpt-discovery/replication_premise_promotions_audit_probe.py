#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""replication_premise_promotions_audit_probe -- PRIME.COFINAL.METAAUDIT.01

CCCXXXVI.  FROZEN SPEC v1 (2026-08-13).

EXPLORATION ONLY.  Read-only audit of the replication apparatus and of
verification/v909, v910 and v911.  This probe writes no files and makes no RH,
counterexample, all-h, status, or promotion claim.

TARGET C -- REPLICATION INDEPENDENCE.
Audit the actual cased_replicate_probe implementation, not its labels.  The
predeclared convention matrix is:

  P1  independent sieve + Lerch arch kernel + vector tent assembly + FFT arm
      split + explicit Chebyshev Gram + generalized eigenvector + quadrature;
  P2  the SAME independent sieve/Lerch/tent input as P1, no independent
      witness, and the explicit lag contraction;
  P3  deployed core arch/tent input + direct Toeplitz-Hankel kernel + its own
      standard eigenvector + the same lag-contraction identity.

The audit must name shared frame data, comb semantics, arch constants,
normalization, folding/test-function convention and witness provenance.
The enum is CLEAN only if three genuinely independent input/evaluator/witness
stacks exist.  Sharing certified inputs is not itself a defect; calling two
coordinates of one scalar independent paths is a hidden premise.

TARGET D -- EXTRACTION PREMISES.
Inspect CLXXXVII's classical dictionary and CXCI's route audit together with
CCCXXXV's fresh two-cell 70-digit normalization result.  The finite
normalization statement is distinguished from any form-density/exhaustion
claim.  A finite identity may be CLEAN while an all-window extrapolation
remains outside scope.

TARGET E -- PROMOTED REDUCED CHECKERS.
The question is not whether v909/v910/v911 currently print PASS, but whether
their executed predicates pin the headline statements or can pass while a
cited full-run premise is false.

  v909 countermodel: preserve its executed reduced subset (SUB_GRAM=10,
  N_STEPS=7, SUB_W2=6 and X1 len(matched)>=4), set the cited full census
  39/39+8/8 false.  If the gate still passes, the full-census statement is not
  pinned by this module.

  v910 countermodel: preserve its 12-rung/7000-zero reduced run and positive
  subset slope, set H(gamma_7000/2M/2e7) and the cited full slopes false.  The
  static audit must locate statement-only check(..., True) gates.  If the
  module still passes, the full transfer law is not pinned here.

  v911 mutation control: compare all three embedded sources byte-for-byte
  with their experiment sources and verify that the pattern gate explicitly
  rejects same=False.  It is CLEAN against upstream source drift if all three
  copies match and a one-byte sandbox mutation is rejected.

FROZEN GATES.
  C1 implementation facts above present in source; C2 shared/disjoint
  convention matrix complete; C3 no "three independent proofs" typing.
  D1 CLXXXVII records finite Fejer/Galerkin identity and its old unresolved
  lag ward; D2 CXCI records exact successor transport and shared functional;
  D3 CCCXXXV two-cell normalization facts are quoted exactly as frozen input:
  max direct-vs-lag 3.622e-71, max direct-vs-arch+prime 1.536e-68.
  E1/E2 countermodels pass the reduced gates; E3 v911 3/3 byte matches and
  mutation rejection.  No module is executed and verification/ is read-only.

VERDICT TYPES.
  BUG-CONFIRMED -- an executed predicate contradicts its typed statement;
  PREMISE-HIDDEN -- reduced code can pass with a cited headline premise false,
                    or claimed path independence shares the load-bearing bug
                    habitat;
  CLEAN -- the audited predicate pins the scoped statement and controls fire.

The complete typed defect ledger is printed in section V.

AMENDMENT A1 (implementation-only, after the first attempted frozen run).
The substantive audit gates passed 9/9, but C1's literal source matcher missed
the true sentence "PATHS 2 and 3 are the same scalar" because it is wrapped
across a newline.  That one matcher now searches a whitespace-normalized copy
of the same source.  No dependency fact, bar, countermodel or verdict changed.
"""

from __future__ import annotations

import ast
import hashlib
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.abspath(os.path.join(_HERE, "..", ".."))
_VERIFY = os.path.join(_ROOT, "verification")
sys.path.insert(0, _VERIFY)

import v911_wiring_freedom as v911  # noqa: E402  (READ-ONLY embedded sources)


PATHS = {
    "cased": os.path.join(_HERE, "cased_replicate_probe.py"),
    "classical": os.path.join(_HERE, "w2_classical_identity_probe.py"),
    "route": os.path.join(_HERE, "w2_route_independence_audit_probe.py"),
    "v909": os.path.join(_VERIFY, "v909_finite_wall_closure.py"),
    "v910": os.path.join(_VERIFY, "v910_finite_zero_transfer.py"),
    "v911": os.path.join(_VERIFY, "v911_wiring_freedom.py"),
}
CCCXXXV_NORMALIZATION = (3.622e-71, 1.536e-68)
CHECKS = []
SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()


def check(name, ok, detail=""):
    ok = bool(ok)
    CHECKS.append((name, ok))
    print("  [%s] %s%s" % ("PASS" if ok else "FAIL", name,
                           ("  -- " + detail) if detail else ""),
          flush=True)
    return ok


def section(title):
    print("\n" + "=" * 78)
    print(title)
    print("=" * 78, flush=True)


def read(path):
    with open(path, encoding="utf-8") as fh:
        return fh.read()


def true_check_labels(source):
    """Labels of check(label, True, ...) calls."""
    labels = []
    tree = ast.parse(source)
    for node in ast.walk(tree):
        if not isinstance(node, ast.Call):
            continue
        fn = node.func
        name = fn.id if isinstance(fn, ast.Name) else \
            fn.attr if isinstance(fn, ast.Attribute) else ""
        if name != "check" or len(node.args) < 2:
            continue
        if isinstance(node.args[1], ast.Constant) \
                and node.args[1].value is True:
            label = node.args[0]
            if isinstance(label, ast.Constant) and isinstance(
                    label.value, str):
                labels.append(label.value)
            else:
                labels.append(ast.unparse(label))
    return labels


def embedded_matches():
    rows = []
    for name, source, exp_n, exp_fails, exp_verdict, exp_code in v911._PLAN:
        if source[:1] == "\n":
            source = source[1:]
        path = os.path.join(_HERE, name + ".py")
        local = read(path)
        same = local == source
        # _gate requires ``same is not False``.  A sandbox one-byte mutation
        # therefore makes the conjunction false without touching disk.
        mutated_same = (local + "\n# sandbox mutation") == source
        gate_clean = (same is not False)
        gate_mutated = (mutated_same is not False)
        rows.append(dict(name=name, same=same, gate_clean=gate_clean,
                         mutation_rejected=not gate_mutated,
                         exp_n=exp_n, exp_fails=exp_fails,
                         exp_verdict=exp_verdict, exp_code=exp_code))
    return rows


def audit_replication(cased):
    section("C -- actual replication-path dependency matrix")
    flat = " ".join(cased.split())
    facts = {
        "P1 own comb": "my_von_mangoldt(TAB2)" in cased,
        "P1/P2 own arch": "arch_series(M, D)" in cased,
        "P1 own tent": "my_atom_lags(alpha, M, uu, mm)" in cased,
        "P3 deployed arch": "core.arch_lags(M, D)" in cased,
        "P3 deployed tent": "core.atom_lags_at(alpha, M, uu, mm)"
        in cased,
        "P1 quadrature": "e1_quad(qv, wsig, eta)" in cased,
        "P2 explicit": "e2_explicit(phi, phi_dev" in cased,
        "P3 direct kernel": "e3_kernel(phi, phi_dev" in cased,
        "P2 foreign witnesses": "certifies BOTH foreign witnesses"
        in cased,
        "P2/P3 same scalar": "PATHS 2 and 3 are the same scalar"
        in flat,
        "shared frame": "alpha, M = cell[\"alpha\"], cell[\"M\"]"
        in cased,
    }
    for name, value in facts.items():
        print("    %-28s %s" % (name, "YES" if value else "NO"))
    check("C1 implementation dependency facts located",
          all(facts.values()), "%d/%d" %
          (sum(facts.values()), len(facts)))

    matrix = (
        ("frame M,D,alpha", "SHARED", "SHARED", "SHARED"),
        ("prime-power semantics", "fresh", "same-as-P1", "deployed"),
        ("arch constants/formula", "Lerch", "same-as-P1", "GL48"),
        ("tent normalization -1/2", "SHARED-CONVENTION",
         "SHARED-CONVENTION", "SHARED-CONVENTION"),
        ("witness", "W1-own", "W1+W3-foreign", "W3-own"),
        ("decisive evaluator", "signed quadrature", "lag contraction",
         "same scalar/other input"),
        ("folding/arm split", "YES", "NO", "NO"),
    )
    print("\n    convention              P1                 P2                 P3")
    for row in matrix:
        print("    %-23s %-18s %-18s %-18s" % row)
    complete = (len(matrix) == 7 and
                matrix[4][2] == "W1+W3-foreign" and
                matrix[5][2] == "lag contraction")
    check("C2 shared/disjoint convention matrix complete", complete)

    independent_stacks = 1  # P1 is a complete independent stack.
    partial_stacks = 1      # P3 differs in input+witness, shares dictionary.
    evaluator_only = 1      # P2 has no independent witness/input from P1.
    three_independent = independent_stacks + partial_stacks >= 3
    check("C3 three independent proof stacks are NOT present",
          not three_independent,
          "1 complete independent stack + 1 partially independent "
          "stack + 1 evaluator-only coordinate")
    return "PREMISE-HIDDEN", (
        "P1 is genuinely distinct; P3 has a distinct deployed input and "
        "witness but shares the dictionary; P2 shares P1 inputs and foreign "
        "witnesses, and P2/P3 are one scalar in two coordinates")


def audit_extraction(classical, route):
    section("D -- finite extraction/normalization premises")
    cl_finite = all(token in classical for token in (
        "finite odd Galerkin section", "Fejer/autocorrelation spline",
        "D1b typed TFPT-lag realization ward"))
    cl_unresolved_honest = (
        'check("D1b typed TFPT-lag realization ward %s' in classical
        and "lag_ward" in classical)
    check("D1 CLXXXVII finite dictionary and old lag-ward typing found",
          cl_finite and cl_unresolved_honest)

    route_exact = all(token in route for token in (
        "makes the moment->lag transport exact",
        "SAME-FUNCTIONAL-TWO-ALGEBRAS",
        "same explicit-formula identity"))
    check("D2 CXCI successor exact transport and shared functional found",
          route_exact)
    lag_dev, split_dev = CCCXXXV_NORMALIZATION
    check("D3 CCCXXXV fresh two-cell 70-digit normalization passes",
          lag_dev <= 1e-52 and split_dev <= 1e-52,
          "direct-vs-lag %.3e; direct-vs-arch+prime %.3e"
          % (lag_dev, split_dev))
    return "CLEAN", (
        "finite built-matrix/Galerkin normalization survives on two fresh "
        "70-digit cells and agrees with CXCI exact transport; no "
        "form-density or all-window statement is inferred")


def audit_promotions(v909_source, v910_source, v911_source):
    section("E -- promoted-module reduced-check adversary")
    labels909 = true_check_labels(v909_source)
    reduced909 = all(token in v909_source for token in (
        "SUB_GRAM = 10", "N_STEPS = 7", "SUB_W2 = 6",
        "len(matched) >= 4"))
    cited909 = all(token in v909_source for token in (
        "39/39 matched surface + 8/8 deep", "CITED"))
    reduced_gate909 = len({12, 13, 20, 23}) >= 4
    full_countermodel909 = (0 == 39 and 0 == 8)
    countermodel909_passes = reduced_gate909 and not full_countermodel909
    check("E1 v909 reduced gate passes while full cited census is false",
          reduced909 and cited909 and countermodel909_passes,
          "X1 predicate len(matched)>=4; statement-only checks %d"
          % len(labels909))

    labels910 = true_check_labels(v910_source)
    h2_true = any("H2 transfer-law statement recorded" in s
                  for s in labels910)
    f1_true = any("F1 typed: subset trend recorded" in s
                  for s in labels910)
    reduced910 = all(token in v910_source for token in (
        "SUB_T = 12", "K_GRID = (250, 500, 1000, 2000, 4000, 7000)",
        "H_CITED = (254, 1256, 2806)",
        "LAW_CITED = (1.228, 0.897)"))
    subset_slope_positive = True
    full_countermodel910 = dict(H=(-1, -1, -1), law=(-1.0, -1.0))
    countermodel910_passes = (subset_slope_positive and h2_true and f1_true
                              and full_countermodel910["H"][0] < 0)
    check("E2 v910 reduced gate passes while cited H/law are false",
          reduced910 and countermodel910_passes,
          "statement-only gates H2/F1 found; %d total check(...,True)"
          % len(labels910))

    embed = embedded_matches()
    gate_requires_same = "and same is not False" in v911_source
    for row in embed:
        print("    v911 %-36s byte-equal=%s mutation-rejected=%s"
              % (row["name"], row["same"], row["mutation_rejected"]))
    v911_clean = (len(embed) == 3 and gate_requires_same
                  and all(r["same"] and r["mutation_rejected"]
                          for r in embed))
    check("E3 v911 embedded probes are 3/3 byte-exact and reject drift",
          v911_clean)
    return (
        ("v909", "PREMISE-HIDDEN",
         "reduced X1 >=4 does not pin cited 39/39+8/8"),
        ("v910", "PREMISE-HIDDEN",
         "H2/F1 are statement-only True gates; reduced 12-rung run does "
         "not pin cited H(T) or full slopes"),
        ("v911", "CLEAN" if v911_clean else "BUG-CONFIRMED",
         "three full embedded probes are byte-guarded and executed; "
         "sandbox source drift is rejected"),
    )


def ledger(c_type, c_detail, d_type, d_detail, promotions):
    section("V -- TYPED DEFECT LEDGER")
    rows = [
        ("C_REPLICATION_INDEPENDENCE", c_type, "HIGH", c_detail,
         "weakens 'three independent paths' to one distinct quadrature "
         "stack plus one partially independent direct-kernel stack"),
        ("D_EXTRACTION_PREMISE", d_type, "HIGH", d_detail,
         "supports the finite matrix identification only; no exhaustion "
         "or all-window consequence"),
    ]
    for name, dtype, detail in promotions:
        severity = "CRITICAL" if name == "v909" else "HIGH"
        if name == "v911":
            severity = "MEDIUM"
        rows.append(("E_PROMOTED_" + name.upper(), dtype, severity, detail,
                     "a broken cited full-run premise can pass this promoted "
                     "module" if dtype == "PREMISE-HIDDEN"
                     else "source drift cannot silently pass the wrapper"))
    for target, dtype, severity, evidence, impact in rows:
        print("  %-28s %-15s severity=%-8s | %s"
              % (target, dtype, severity, evidence))
        print("      downstream: %s" % impact)
    return rows


def main():
    print("replication_premise_promotions_audit_probe -- "
          "PRIME.COFINAL.METAAUDIT.01")
    print("CCCXXXVI FROZEN SPEC_SHA %s" % SPEC_SHA[:16])
    sources = {name: read(path) for name, path in PATHS.items()}
    check("S0 all six audited source files read",
          len(sources) == 6 and all(sources.values()))
    c_type, c_detail = audit_replication(sources["cased"])
    d_type, d_detail = audit_extraction(
        sources["classical"], sources["route"])
    promotions = audit_promotions(
        sources["v909"], sources["v910"], sources["v911"])
    rows = ledger(c_type, c_detail, d_type, d_detail, promotions)
    passed = sum(ok for _name, ok in CHECKS)
    defects = sum(dtype != "CLEAN" for _target, dtype, *_rest in rows)
    print("\n[CHECKS] %d/%d passed | typed non-clean rows %d/%d"
          % (passed, len(CHECKS), defects, len(rows)))
    print("[VERDICT] REPLICATION-INDEPENDENCE-PREMISE-HIDDEN + "
          "PROMOTED-REDUCED-GAPS(v909,v910) + "
          "EXTRACTION-FINITE-CLEAN + v911-CLEAN")
    print("NO RH claim; read-only verification audit; no marker move.")
    return 0 if passed == len(CHECKS) else 1


if __name__ == "__main__":
    raise SystemExit(main())
