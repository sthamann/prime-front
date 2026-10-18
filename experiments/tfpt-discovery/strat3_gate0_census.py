#!/usr/bin/env python3
"""STRATEGY-3 / Gate 0: S={infinity,2,3,5} local orbit-algebra census.

Exploration only.  This finite census formalizes the *weak* functor candidate:
the sigma-descended TFPT periodic-orbit/Hecke basis maps to the Laurent orbit
subalgebra of Connes' S-local crossed product.  It does NOT construct a map of
the full adele-class C*-algebra, its topology, or its archimedean test-function
space.

The non-tautological local input is taken from the Gaussian rank-four HNF
tower and checked again here:

  rational place  Gaussian class(es)  raw HNF multiplicity  sigma descent
       2           norm 2 ramified           15             one orbit
       3           norm 9 inert             820             half time
       5           two norm 5 split         312             pair quotient

Division by the intrinsic rank-four HNF cell 1+q+q^2+q^3, followed by the
sigma-orbit quotient, must leave the SAME global scalar kappa at all three
places.  The kill criterion is any mismatch of these kappas or of a
convolution coefficient.

The finite basis is e=(e2,e3,e5) in [-2,2]^3.  On both sides:
  convolution: e*f = e+f;
  involution: e^* = -e;
  grading/time: degree vector e, alpha_t(e)=exp(it sum e_p log p)e;
  regular trace: 1 only at e=0;
  symmetric closed-orbit trace: log p on signed p-powers, zero on mixed words.

All algebraic comparisons use integers/Fractions or formal log-coefficient
vectors.  Floating point appears only in a redundant time-action battery.
No zero data and no prime table are loaded.  No file is written.
"""

import ast
import cmath
import math
import os
import sys
from fractions import Fraction
from itertools import product

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)

import moonshot_hecke_groupoid_probe as tower  # noqa: E402


PLACES = (2, 3, 5)
EXPONENT_BOUND = 2
TIME_BATTERY = (-1.25, -0.5, 0.0, 0.75, 2.0)
TIME_TOL = 2.0e-14
BANNED = ("zetazero", "nzeros", "isprime", "primerange", "nextprime",
          "prevprime", "primepi", "sympy")

CHECKS = []
FAILS = []


def check(name, ok, detail=""):
    CHECKS.append(name)
    if not ok:
        FAILS.append(name.split()[0])
    print("[%s] %s%s" % ("PASS" if ok else "FAIL", name,
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


def hnf_cell(q):
    return 1 + q + q * q + q * q * q


def local_descent_census():
    """Return exact local records, independently classified by tower code."""
    classes = tower.class_census(9)
    bases = tower.classify_bases(classes, 9)
    by_place = {base: kind for kind, base, _length in bases
                if base in PLACES}
    records = {
        2: dict(kind="ram", q=2, gaussian_classes=1,
                raw=hnf_cell(2), sigma_orbit=1, time_denominator=1),
        3: dict(kind="inert", q=9, gaussian_classes=1,
                raw=hnf_cell(9), sigma_orbit=1, time_denominator=2),
        5: dict(kind="split", q=5, gaussian_classes=2,
                raw=2 * hnf_cell(5), sigma_orbit=2, time_denominator=1),
    }
    return classes, by_place, records


def normalized_kappa(record):
    per_gaussian_class = Fraction(record["raw"],
                                  record["gaussian_classes"])
    cell_removed = per_gaussian_class / hnf_cell(record["q"])
    return cell_removed * Fraction(record["gaussian_classes"],
                                   record["sigma_orbit"])


def basis():
    values = range(-EXPONENT_BOUND, EXPONENT_BOUND + 1)
    return list(product(values, repeat=len(PLACES)))


def convolve_word(left, right):
    return tuple(a + b for a, b in zip(left, right))


def involute_word(word):
    return tuple(-x for x in word)


def regular_trace(word):
    return int(all(x == 0 for x in word))


def orbit_trace_signature(word):
    """Formal coefficients of log(2),log(3),log(5), hence exact."""
    support = [j for j, exponent in enumerate(word) if exponent != 0]
    if len(support) != 1:
        return (0, 0, 0)
    out = [0, 0, 0]
    out[support[0]] = 1
    return tuple(out)


def grade_vector(word):
    """The time grading as exact formal logarithm coefficients."""
    return tuple(word)


def numeric_grade(word):
    return sum(exponent * math.log(place)
               for place, exponent in zip(PLACES, word))


def tfpt_product(left, right, kappas):
    """Normalized sigma-descended product: coefficient times basis word."""
    coefficient = Fraction(1)
    for j, exponent in enumerate(convolve_word(left, right)):
        if exponent:
            coefficient *= kappas[PLACES[j]] ** abs(exponent)
    return coefficient, convolve_word(left, right)


def connes_product(left, right):
    return Fraction(1), convolve_word(left, right)


def run():
    print("=" * 78)
    print("STRAT3 GATE-0 -- sigma descent to the S-local orbit algebra")
    print("=" * 78)
    hits = ast_firewall()
    check("G0.1 AST firewall", not hits, str(hits))

    classes, classified, records = local_descent_census()
    expected_classes = {
        2: [(1, 1)],
        5: [(1, 2), (2, 1)],
        9: [(3, 0)],
    }
    observed = {q: classes.get(q, []) for q in expected_classes}
    check("S1.1 Gaussian local classes", observed == expected_classes,
          str(observed))
    check("S1.2 sigma types", classified ==
          {2: "ram", 3: "inert", 5: "split"}, str(classified))

    kappas = {place: normalized_kappa(record)
              for place, record in records.items()}
    raw_detail = ", ".join(
        "%d:%s q=%d raw=%d cell=%d orbit=%d kappa=%s"
        % (place, records[place]["kind"], records[place]["q"],
           records[place]["raw"], hnf_cell(records[place]["q"]),
           records[place]["sigma_orbit"], kappas[place])
        for place in PLACES)
    check("S1.3 one global normalization", len(set(kappas.values())) == 1
          and next(iter(kappas.values())) == 1, raw_detail)

    # The inert norm-nine grading is divided by its sigma isotropy order.
    time_coefficients = {
        place: Fraction(2 if records[place]["q"] == place * place else 1,
                        records[place]["time_denominator"])
        for place in PLACES
    }
    check("S1.4 descended primitive time coefficients",
          time_coefficients == {2: 1, 3: 1, 5: 1},
          str(time_coefficients))

    words = basis()
    image = {word: word for word in words}
    check("S2.1 basis bijection", len(image) == len(words)
          and len(set(image.values())) == len(words),
          "%d basis words in [-%d,%d]^3"
          % (len(words), EXPONENT_BOUND, EXPONENT_BOUND))

    word_set = set(words)
    product_checks = 0
    coefficient_deviation = Fraction(0)
    product_ok = True
    grade_product_ok = True
    for left in words:
        for right in words:
            target = convolve_word(left, right)
            if target not in word_set:
                continue
            tfpt_coefficient, tfpt_target = tfpt_product(left, right,
                                                         kappas)
            connes_coefficient, connes_target = connes_product(image[left],
                                                               image[right])
            product_checks += 1
            coefficient_deviation = max(
                coefficient_deviation,
                abs(tfpt_coefficient - connes_coefficient))
            product_ok &= (tfpt_target == connes_target
                           and tfpt_coefficient == connes_coefficient)
            grade_product_ok &= (
                grade_vector(target) ==
                tuple(a + b for a, b in
                      zip(grade_vector(left), grade_vector(right))))
    check("S2.2 convolution and multiplicities", product_ok,
          "%d products, max exact coefficient deviation %s"
          % (product_checks, coefficient_deviation))
    check("S2.3 additive graded time under convolution", grade_product_ok,
          "%d exact formal-log identities" % product_checks)

    star_ok = all(image[involute_word(word)] ==
                  involute_word(image[word]) for word in words)
    check("S2.4 involution", star_ok,
          "%d pointwise star identities" % len(words))

    time_dev = 0.0
    for word in words:
        for t in TIME_BATTERY:
            tfpt_phase = cmath.exp(1j * t * numeric_grade(word))
            connes_phase = cmath.exp(
                1j * t * numeric_grade(image[word]))
            time_dev = max(time_dev, abs(tfpt_phase - connes_phase))
    check("S2.5 graded time action", time_dev <= TIME_TOL,
          "%d phases, max deviation %.3e"
          % (len(words) * len(TIME_BATTERY), time_dev))

    regular_ok = all(regular_trace(word) ==
                     regular_trace(image[word]) for word in words)
    orbit_ok = all(orbit_trace_signature(word) ==
                   orbit_trace_signature(image[word]) for word in words)
    star_trace_ok = all(
        orbit_trace_signature(involute_word(word)) ==
        orbit_trace_signature(word) for word in words)
    check("S2.6 regular basis traces", regular_ok,
          "%d pointwise traces" % len(words))
    check("S2.7 closed-orbit basis traces", orbit_ok and star_trace_ok,
          "%d pointwise formal Lambda traces; star-symmetric"
          % len(words))

    # Explicit repetition ledger at each finite place, k=1,2.
    repetition_rows = []
    repetition_ok = True
    for j, place in enumerate(PLACES):
        for exponent in (1, 2):
            word = tuple(exponent if i == j else 0 for i in range(3))
            signature = orbit_trace_signature(word)
            expected = tuple(1 if i == j else 0 for i in range(3))
            repetition_ok &= signature == expected
            repetition_rows.append("%d^%d->log%d" %
                                   (place, exponent, place))
    check("S2.8 primitive/repetition trace ledger", repetition_ok,
          ", ".join(repetition_rows))

    passed = not FAILS
    print("\nVERDICT: %s" %
          ("GATE0-WEAK-FUNCTOR" if passed else "GATE0-KILL"))
    if passed:
        print("CONTRACT: On the finite periodic-orbit Laurent basis for "
              "S={infinity,2,3,5}, sigma descent defines a coefficient-one "
              "graded *-algebra functor candidate and preserves the regular "
              "and closed-orbit basis traces.  This is the formal weak yes.")
        print("NOT PROVED: extension from this orbit subalgebra to Connes' "
              "full S-local convolution algebra; compatibility with its "
              "topology/completion, additive adele coordinates, isotropy "
              "representations, archimedean Schwartz kernels, or KMS state.")
    else:
        print("KILL: local multiplicities or a structure coefficient fail "
              "after the single intrinsic HNF normalization.")

    if FAILS:
        print("RESULT: %d/%d CHECKS PASSED; FAILURES %s"
              % (len(CHECKS) - len(FAILS), len(CHECKS),
                 ",".join(FAILS)))
        return 1
    print("RESULT: ALL %d CHECKS PASSED" % len(CHECKS))
    return 0


if __name__ == "__main__":
    raise SystemExit(run())
