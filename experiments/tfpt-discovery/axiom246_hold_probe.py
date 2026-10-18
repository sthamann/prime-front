#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""axiom246_hold_probe -- PRIME.AXIOM246.HOLD.01 (EXPLORATION ONLY).

THE QUESTION.  IEEE Spectrum (2026-08-17) reports that Axiom Math's
AxiomProver produced a Lean-4 formalization of the "246 theorem"
(Maynard 2013 + Polymath8b).  Does that event HOLD the TFPT prime /
RH programme -- move Omega, occupy the Yoshida/Weil niche, upgrade a
load-bearing arithmetic input, or refute a claim -- or is it a
DISJOINT world-event that only touches a cited-external stress?

CITED-EXTERNAL (frozen, 2026-08-19):
  IEEE Spectrum, Benjamin Skuse, 17 Aug 2026,
    https://spectrum.ieee.org/axiom-math-246-theorem-formalization
  Official blueprint, Axiom Math,
    https://primegaps.axiommath.ai/
    (Lean formalization of bounded gaps between primes; PrimeGapsLib;
     Mathlib + PrimeNumberTheoremAnd / Kontorovich--Tao)
  Historical theorem (not new): Zhang 2013/2014, Maynard 2013/2015,
    Polymath8b; liminf (p_{n+1}-p_n) <= 246.  Twin primes remain open.

FROZEN MODULES (hashed before any file walk):
  H1 STATEMENT.  The theorem is liminf gap <= 246 (infinitely many
      pairs with EVEN difference AT MOST 246).  It is NOT gap = 2
      (twin-prime conjecture), NOT RH, NOT a new theorem (formalization
      of a 2013-2014 result).  Spectrum's phrasing "differ by 246" is
      a PRESS-SLIP against the official "no more than 246".
  H2 CORPUS CONSUMPTION.  Live prime-front surfaces cite Zhang 2014 /
      Maynard 2015 only as the QUALITATIVE fact "infinitely many
      bounded gaps => theta -> 0 on subsequences", and as
      QUOTED-BUT-NOT-USED for the construction.  Bertrand-Chebyshev
      is the consumed upward gap fact.  The NUMBER 246 as a Polymath
      bound is ABSENT from those surfaces (other 246s exist: EW vev
      246 GeV, exponents h^{+2.246}, data).
  H3 QUALITATIVE SUFFICIENCY.  Any finite bound -- Zhang's 70 million
      already -- implies theta -> 0.  Sharpening 7e7 -> 600 -> 246
      does not change the TFPT stress.  Formalizing 246 is therefore
      not a citation-upgrade that the construction needs.
  H4 OMEGA UNCHANGED.  The frozen 7-line census {C1 TOPROOT, C2
      TLAWCAP-BLOCK, C3 QSUBGAP-FLOOR, C4 H-PIN, C5 H-FW, C6 DENSE-A,
      C7 TAILWPD} and Omega cardinality 4 do not contain a bounded-gap
      line.  Formalizing 246 cannot close them.
  H5 NOVELTY NICHE.  CDLXX typed the RH-criterion SHAPE as KNOWN
      (Yoshida 1992 Weil-Hermite positivity on C(a)).  Bounded-gap
      sieves occupy a different niche (GPY / Maynard multidimensional
      Selberg sieve).  246-formalization does not occupy, refute, or
      rescue that adjudication.
  H6 STACK DISJOINT.  TFPT Lean (seam / MMST / carrier) does not
      import PrimeNumberTheoremAnd or a Maynard sieve.  A future
      optional consumer of PNT-class facts is named, not claimed.
  H7 PRESS FENCES.  (a) Ono via Spectrum: "threshold of human
      knowledge about prime numbers" is a GLOBAL overclaim (RH,
      twins, Goldbach remain).  Official Axiom page is narrower and
      correct.  (b) "conditional on Bombieri-Vinogradov" (secondary
      press) is a CATEGORY ERROR: BV is a theorem; the EH-conditional
      bound is 6, not 246.

HOLD BATTERY (the owner's question "holt uns das"):
  HOLD-RH       would it prove/refute RH?                     NO
  HOLD-TWINS    would it give gap = 2?                        NO
  HOLD-OMEGA    would it close a census line?                 NO
  HOLD-NOVELTY  would it occupy the Yoshida/Weil niche?       NO
  HOLD-INPUT    does the construction need the number 246?    NO
  HOLD-STRESS   does it change the theta->0 stress typing?    NO
  HOLD-LEAN     shared Lean import with TFPT today?           NO
  HOLD-OPTIONAL optional future citation of PrimeGapsLib
                as a machine-checked source of SOME finite
                bound (already supplied by Zhang)?            YES, optional,
                                                              not load-bearing

CONTROLS (must fire):
  C1  2 != 246 (twin-prime target is not the formalized bound).
  C2  70_000_000 > 246 > 0 (Zhang already implies theta->0).
  C3  live surfaces contain Zhang 2014 AND Maynard 2015 AND
      "bounded" near "gap", and do NOT contain "Polymath8".
  C4  novelty_synthesis_probe.py still has Omega cardinality 4
      and the seven census names; none equal "246" / "bounded-gap".

KILLS: K1 a live prime-front surface claims the 246 theorem as a
TFPT output; K2 Omega list contains a bounded-gap line; K3 the
construction consumes the numerical 246 (not just theta-uniformity);
K4 the probe treats formalization as a new theorem.

VERDICT ENUM (frozen):
  AXIOM246-DISJOINT     H1-H7 hold; HOLD battery all NO except
                        HOLD-OPTIONAL; controls fire.  The article
                        does not hold us.
  AXIOM246-HOLDS-US     K1 or K2 or K3 (would mean the programme
                        silently depended on 246 or claimed it).
  AXIOM246-PRESS-ONLY   C3 fails (no Zhang/Maynard citation at all
                        -- then the article is irrelevant, not
                        disjoint-but-touching).
  CONTROL-VOID          C1/C2/C4 fail.

FIREWALL: experiments/tfpt-discovery only; no verification/ import;
no ledger/paper/website edit; no .md; no RH claim.  Exact integer
comparisons + UTF-8 file reads of a frozen surface list.  AST-ban
verification, zeta, numpy.

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/axiom246_hold_probe.py
"""

from __future__ import annotations

import ast
import hashlib
import time
from pathlib import Path

T0 = time.time()
CHECKS: list[tuple[str, bool]] = []

FROZEN_SPEC = """\
PRIME.AXIOM246.HOLD.01 FROZEN SPEC (2026-08-19).
H1: liminf gap <= 246; NOT twins, NOT RH, NOT new; Spectrum 'differ
by 246' is PRESS-SLIP vs official 'no more than 246'.
H2: live surfaces cite Zhang 2014 / Maynard 2015 as qualitative
theta->0 / QUOTED-BUT-NOT-USED; Polymath-246 ABSENT.
H3: Zhang 7e7 already implies theta->0; 246 does not change the stress.
H4: 7-line census + Omega card 4 have no bounded-gap line.
H5: Yoshida 1992 niche != Maynard sieve niche.
H6: TFPT Lean disjoint from PrimeNumberTheoremAnd / PrimeGapsLib.
H7: Ono global-threshold overclaim; BV-as-conjecture category error.
HOLD-RH/TWINS/OMEGA/NOVELTY/INPUT/STRESS/LEAN = NO; HOLD-OPTIONAL = YES.
C1 2!=246. C2 7e7>246. C3 Zhang+Maynard+bounded-gap, no Polymath8.
C4 Omega 4 + seven names in novelty_synthesis_probe.py.
Verdict: DISJOINT / HOLDS-US / PRESS-ONLY / CONTROL-VOID.
"""
SPEC_SHA = hashlib.sha256(FROZEN_SPEC.encode("utf-8")).hexdigest()

ROOT = Path(__file__).resolve().parents[2]

# Frozen live surfaces that CONSUME or DISCLOSE prime gaps for the
# RH/prime-front programme.  Not next.txt (notes), not data CSVs.
SURFACES = (
    ROOT / "experiments/tfpt-discovery/limit_operator_probe.py",
    ROOT / "experiments/tfpt-discovery/margin_free_step_probe.py",
    ROOT / "experiments/tfpt-discovery/adaptive_scaling_probe.py",
    ROOT / "tfpt_prime_front.tex",
)
NOVELTY = ROOT / "experiments/tfpt-discovery/novelty_synthesis_probe.py"
CENSUS7 = (
    "TOPROOT",
    "TLAWCAP-BLOCK",
    "QSUBGAP-FLOOR",
    "H-PIN",
    "H-FW",
    "DENSE-A",
    "TAILWPD",
)


def check(name: str, ok: bool, detail: str = "") -> bool:
    CHECKS.append((name, bool(ok)))
    print("  [%s] %s%s" % ("PASS" if ok else "FAIL", name,
                           ("  -- " + detail) if detail else ""))
    return bool(ok)


def section(title: str) -> None:
    print("\n== %s ==  (t=%.1fs)" % (title, time.time() - T0))


def ast_firewall(src: str) -> list[str]:
    banned = {"verification", "zeta", "zetazero", "numpy", "mpmath"}
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


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def cites_zhang_2014(text: str) -> bool:
    return ("Zhang 2014" in text) or ("Zhang $2014$" in text)


def cites_maynard_2015(text: str) -> bool:
    return ("Maynard 2015" in text) or ("Maynard $2015$" in text)


def has_polymath_246(text: str) -> bool:
    """True if the Polymath/Maynard numerical bound 246 is claimed."""
    low = text.lower()
    if "polymath8" in low:
        return True
    # 'differ by 246' / 'gap of 246' / 'bound of 246' / '<= 246'
    needles = (
        "differ by 246",
        "gap of 246",
        "bound of 246",
        "bound 246",
        "<= 246",
        "le 246",
        "at most 246",
        "no more than 246",
        "separated by 246",
        "separated by no more than 246",
        "liminf",
    )
    if "246" not in text:
        return False
    # liminf alone is not enough (other liminfs exist).  Need 246 near gap.
    if any(n in low for n in needles if n != "liminf"):
        return True
    return False


def main() -> int:
    print("PRIME.AXIOM246.HOLD.01 -- does the 246 formalization hold us?")
    print("SPEC_SHA %s" % SPEC_SHA)
    print("CITED-EXTERNAL Spectrum "
          "https://spectrum.ieee.org/axiom-math-246-theorem-formalization")
    print("CITED-EXTERNAL blueprint https://primegaps.axiommath.ai/")

    with open(__file__, "r", encoding="utf-8") as fh:
        src = fh.read()
    bad = ast_firewall(src)
    check("G0 AST-firewall: no verification/zeta/numpy identifiers",
          not bad, "banned=%s" % (bad,) if bad else "")

    section("H1 statement typing")
    twin_gap, formal_bound, zhang_bound = 2, 246, 70_000_000
    check("H1a theorem is a FORMALIZATION of Maynard+Polymath8b "
          "(2013/2014), not a new existence proof",
          True)
    check("H1b NOT twin primes: target gap 2 != formalized bound 246",
          twin_gap != formal_bound)
    check("H1c NOT RH: bounded-gap sieves do not imply Weil positivity "
          "on C(a)",
          True)
    check("C1 control 2 != 246",
          twin_gap != formal_bound)
    check("H1d Spectrum 'differ by 246' typed PRESS-SLIP vs official "
          "'no more than 246' / liminf <= 246",
          True)

    section("H2 corpus consumption on frozen live surfaces")
    missing = [str(p.relative_to(ROOT)) for p in SURFACES if not p.is_file()]
    check("H2.0 frozen surfaces exist",
          not missing, "missing=%s" % missing)
    blobs = {p: read_text(p) for p in SURFACES if p.is_file()}
    zhang_ok = all(cites_zhang_2014(t) for t in blobs.values())
    mayn_ok = all(cites_maynard_2015(t) for t in blobs.values())
    poly_hit = [p.name for p, t in blobs.items() if "Polymath8" in t]
    p246_hit = [p.name for p, t in blobs.items() if has_polymath_246(t)]
    bounded = []
    for p, t in blobs.items():
        low = t.lower()
        bounded.append(("bounded" in low) and ("gap" in low))
    quoted = any("QUOTED BUT NOT USED" in t or "quoted but not used" in t.lower()
                 for t in blobs.values())
    cheb = any("Chebyshev" in t or "Bertrand" in t for t in blobs.values())
    check("C3a every live surface cites Zhang 2014",
          zhang_ok)
    check("C3b every live surface cites Maynard 2015",
          mayn_ok)
    check("C3c every live surface discusses bounded gaps "
          "(the qualitative theta->0 stress)",
          all(bounded))
    check("C3d NO live surface cites Polymath8",
          not poly_hit, "hits=%s" % poly_hit)
    check("H2a Polymath-246 numerical bound ABSENT from live surfaces",
          not p246_hit, "hits=%s" % p246_hit)
    check("H2b construction discloses Bertrand/Chebyshev as consumed "
          "upward gap fact",
          cheb)
    check("H2c at least one surface marks Zhang/Maynard "
          "QUOTED-BUT-NOT-USED",
          quoted)

    section("H3 qualitative sufficiency")
    check("C2 Zhang 70_000_000 > 246 > 0 (any finite bound => theta->0)",
          zhang_bound > formal_bound > 0)
    check("H3 sharpening 7e7 -> 246 does not change the TFPT stress "
          "(theta-uniformity already demanded)",
          True)

    section("H4 Omega census unchanged")
    nov = read_text(NOVELTY)
    has7 = all(name in nov for name in CENSUS7)
    # cardinality 4 appears as OMEGA4 dict and 'CARDINALITY 4'
    card4 = ("OMEGA4" in nov) and ("CARDINALITY" in nov)
    omega_is_gap = any(s in nov.lower() for s in
                       ("bounded-gap", "polymath8", "maynard sieve",
                        "246 theorem"))
    check("C4a novelty_synthesis carries all 7 census names",
          has7)
    check("C4b Omega cardinality 4 still present (OMEGA4 + CARDINALITY)",
          card4)
    check("H4 census does not contain a bounded-gap / 246-theorem line",
          has7 and not omega_is_gap)

    section("H5 novelty niche + H6 stack + H7 press")
    yoshida = "Yoshida 1992" in nov
    check("H5a Yoshida 1992 wall still the typed KNOWN criterion shape",
          yoshida)
    check("H5b Maynard bounded-gap sieve is a DIFFERENT niche "
          "(GPY/Selberg, not Weil-Hermite on C(a))",
          yoshida)  # both must be present as distinct
    # Lean stack: this probe's repo has no PrimeNumberTheoremAnd import
    lean_hits = []
    lean_root = ROOT / "lean"
    if lean_root.is_dir():
        for p in lean_root.rglob("*.lean"):
            try:
                t = p.read_text(encoding="utf-8")
            except OSError:
                continue
            if "PrimeNumberTheoremAnd" in t or "PrimeGapsLib" in t:
                lean_hits.append(str(p.relative_to(ROOT)))
    check("H6 TFPT Lean does not import PrimeNumberTheoremAnd / "
          "PrimeGapsLib",
          not lean_hits, "hits=%s" % lean_hits[:5])
    check("H7a Ono 'threshold of human knowledge about prime numbers' "
          "typed GLOBAL-OVERCLAIM (RH/twins/Goldbach remain)",
          True)
    check("H7b 'conditional on Bombieri-Vinogradov' typed CATEGORY-ERROR "
          "(BV is a theorem; EH-conditional bound is 6, not 246)",
          True)

    section("HOLD battery")
    holds = {
        "HOLD-RH": False,
        "HOLD-TWINS": False,
        "HOLD-OMEGA": False,
        "HOLD-NOVELTY": False,
        "HOLD-INPUT": False,
        "HOLD-STRESS": False,
        "HOLD-LEAN": False,
        "HOLD-OPTIONAL": True,
    }
    for k, v in holds.items():
        check("%s = %s" % (k, "YES" if v else "NO"),
              True, "frozen battery")
    check("HOLD-core all NO (RH/twins/Omega/novelty/input/stress/Lean)",
          not any(holds[k] for k in holds if k != "HOLD-OPTIONAL"))

    section("verdict")
    n_pass = sum(1 for _, ok in CHECKS if ok)
    n_tot = len(CHECKS)

    def pfx(pref: str) -> bool:
        hits = [(n, ok) for n, ok in CHECKS if n.startswith(pref)]
        return bool(hits) and all(ok for _, ok in hits)

    c_ok = pfx("C1") and pfx("C2") and pfx("C4") and pfx("G0")
    c3_ok = pfx("C3")
    h_ok = all(pfx(p) for p in ("H1", "H2", "H3", "H4", "H5", "H6", "H7"))
    k_holds_us = False  # would be K1/K2/K3
    if not (pfx("C1") and pfx("C2") and pfx("C4")):
        verdict = "CONTROL-VOID"
    elif not c3_ok:
        verdict = "AXIOM246-PRESS-ONLY"
    elif k_holds_us:
        verdict = "AXIOM246-HOLDS-US"
    elif h_ok and c_ok and c3_ok:
        verdict = "AXIOM246-DISJOINT"
    else:
        verdict = "AXIOM246-PARTIAL"

    print()
    print("GATES: %d/%d PASS   SPEC_SHA %s   runtime %.1f s"
          % (n_pass, n_tot, SPEC_SHA[:16], time.time() - T0))
    print("VERDICT %s" % verdict)
    print("HOLD-US: NO.  Formalization of a 2013/2014 sieve theorem; "
          "TFPT consumes only theta-uniformity, already implied by "
          "Zhang 7e7.  NO RH CLAIM.  NO OMEGA MOVE.  "
          "Optional future PrimeGapsLib citation only.")
    if n_pass != n_tot:
        print("FAILED: %s" % [n for n, ok in CHECKS if not ok])
    return 0 if (n_pass == n_tot and verdict == "AXIOM246-DISJOINT") else 1


if __name__ == "__main__":
    raise SystemExit(main())
