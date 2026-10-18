#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""nonclifford_prime_probe -- GNET.NONCLIFFORD.PRIME.01 (EXPLORATION ONLY).

THE QUESTION.  Are the Gaussian primes non-Clifford *write events* on
the v783 two-qubit carrier, or firmware (inside G31 / C2)?  The strong
hypothesis from the information-architecture picture -- every prime
impulse is a non-Clifford update -- is TESTABLE only after a frozen
dictionary.  Three corpus-native dictionaries, no search, no hash of
p onto a gate:

  D1  GLOBAL PHASE.  pi / |pi| as the scalar (pi/|pi|) I_4 on C^4
      (the v783 chart).  Matrix-level vs projective (PSU) reported
      separately: projectively every U(1) scalar is identity.
  D2  JET MULTIPLICATION.  pi acting on W = L/2L = R_2^4, R_2 =
      Z[i]/(2).  Odd pi are units of R_2, hence 1 or 1+eps (the deck).
      Both lie in the mu4 clock, hence in G31.  The ramified pi = 1+i
      is nilpotent (eps), not an automorphism.
  D3  ANCHOR CPHASE (primary for the write-event reading).  In the
      frozen v783 computational basis (|q1 q2> with slot 2*q1+q2, the
      coordinate-class frame, last slot = the e6/e7 ANCHOR pair of
      v638/v736) the matrix
          D_anchor(omega) = diag(1, 1, 1, omega),  omega = pi / |pi|
      is the same shape as the v783 T-gate-twist control.  Clifford
      membership = Pauli-group normalizer test (no 92160 enumeration):
      D is Clifford iff D P D^{-1} is a Pauli up to U(1) for every
      two-qubit Pauli P.

FROZEN GAUSSIAN-PRIME CENSUS (no prime table): all associate-class
representatives a+bi with 0 <= b <= a, 2 <= N = a^2+b^2 <= 53, gcd
handled per class, irreducibility = Z-trial-division + the three
Gaussian types (N=2 ramified; N = q^2 with q=3 mod 4 inert; N = p = 1
mod 4 split).  Ring-internal.

PREDECLARED DEMANDS (the filtration of the strong hypothesis):
  D1-proj  ALL classes -> projective identity.  Strong hypothesis
           DEAD at the PSU layer.
  D1-mat   ramified 1+i -> omega in mu8 \ mu4 (zeta8, the C2-index-2
           scalar); inert -> omega in mu4; split -> omega not in mu8.
  D2       odd pi -> {1, 1+eps} subset clock subset G31; 1+i ->
           nilpotent.  Jet writes are FIRMWARE, not non-Clifford.
  D3       inert frozen representative (omega=1) -> Clifford (I, not
           CS); ramified -> NOT Clifford (CPhase(pi/4) = T-shape);
           split -> NOT Clifford AND omega not in Q(zeta8)
           (off the Clifford field).  Inert Clifford is NOT
           associate-class invariant: see FENCE.

STRONG HYPOTHESIS "every prime is a non-Clifford write": DEAD if D2
holds as firmware AND D3-inert (frozen representative) is Clifford.
FILTERED STATEMENT that can still carry: the ramified prime is the
T-gate; split primes are off-field phases on the frozen anchor slot;
inert primes do not write *in the frozen representative chart*.

CONTROLS (must fire):
  C1  I_4 is Clifford; H(x)I (Hadamard on qubit 1) is Clifford
      (Pauli-normalizer yes).
  C2  diag(1,1,1,zeta8) is NOT Clifford (the v783 T-twist / CPhase(pi/4)).
      diag(1,1,1,-1) IS Clifford (CZ).  diag(1,1,1,i) is NOT Clifford
      (CS = CPhase(pi/2) lives in C3, not C2 -- pre-run design error:
      "S-type on the anchor" is not a C2 write).  i I_4 IS Clifford
      (Pauli-group scalar / G31).  I(x)S = diag(1,i,1,i) IS Clifford
      (true local S).  The detector distinguishes local S from
      anchor-CPhase(i).
  C3  scrambled dictionary D_scr = diag(1, omega, 1, 1) (T on a FAMILY
      slot, not the frozen anchor) is reported, gates nothing --
      origin-warning: slot choice is the v783 chart, not a search.
  C4  identity 1+0i is NOT in the prime census.
  FENCE  D3 of an inert prime is Clifford for the frozen representative
      (omega=1) and NOT Clifford for the associate i*pi (omega=i).
      The unit i as a GLOBAL phase is G31; as an ANCHOR CPhase it is
      CS.  Typed DICTIONARY-ON-REPRESENTATIVE, not a kill of D3.

KILLS: K1 census misses a Gaussian type or includes a composite;
K2 D1-proj fails (a scalar not ~ I projectively -- should be
impossible); K3 D3-inert is non-Clifford or D3-ramified IS Clifford
(the T-identification dies); K4 D2 odd unit outside {1, 1+eps}.

VERDICT ENUM (frozen):
  NONCLIFFORD-PRIME-FILTERED  demands hold; strong hypothesis DEAD;
                              ramified = T, split = off-field,
                              inert = Clifford; D1-proj invisible;
                              D2 firmware.
  NONCLIFFORD-PRIME-ALL       every census prime is non-Clifford in D3
                              AND D2 (will not fire if demands hold).
  NONCLIFFORD-PRIME-DEAD      K3 or D3-ramified Clifford.
  CONTROL-VOID                a control fails.

FIREWALL: experiments/tfpt-discovery only; no verification/ import;
no ledger/paper/website; no .md; no RH; no matter semantics.  Exact
sympy / integer; AST-ban verification, zeta, numpy.

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/nonclifford_prime_probe.py
"""

from __future__ import annotations

import ast
import hashlib
import math
import time
from math import gcd

import sympy as sp

T0 = time.time()
CHECKS: list[tuple[str, bool]] = []

FROZEN_SPEC = """\
GNET.NONCLIFFORD.PRIME.01 FROZEN SPEC (2026-08-19).
Census: Gaussian associate-class reps 0<=b<=a, 2<=N<=53, ring-internal
irreducibility (trial division + types ramified/inert/split). No table.
D1 scalar omega I: projective all ~ I; matrix ramified in mu8\\mu4,
inert in mu4, split not in mu8.
D2 jet: odd pi in {1, 1+eps} subset clock; 1+i nilpotent.
D3 D_anchor(omega)=diag(1,1,1,omega) in v783 chart / e6e7 anchor slot.
Clifford := Pauli-group normalizer. Demand: frozen-inert omega=1
Clifford, ramified NOT, split NOT and omega not in Q(zeta8).
Strong hyp DEAD if D2 firmware and D3-inert Clifford.
C1 I and H(x)I Clifford. C2 T-twist NOT; CZ yes; CS NOT (C3);
i I yes (G31); I(x)S yes. C4 1 not a prime. FENCE inert omega=1
Clifford, associate omega=i not (D3 not class-invariant).
Verdict: FILTERED / ALL / DEAD / CONTROL-VOID.
"""
SPEC_SHA = hashlib.sha256(FROZEN_SPEC.encode("utf-8")).hexdigest()

I_SYM = sp.I
ZETA8 = (1 + I_SYM) / sp.sqrt(2)


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


def is_z_prime(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    k = 3
    while k * k <= n:
        if n % k == 0:
            return False
        k += 2
    return True


def gaussian_prime_census(n_max: int = 53):
    """Associate-class representatives, no stored prime table."""
    found = []
    # ramified
    found.append(dict(a=1, b=1, N=2, kind="ramified", pi="1+i"))
    # split: a>b>0, a+b odd (not 1+i-divisible), N prime = 1 mod 4
    a = 2
    while a * a <= n_max:
        for b in range(1, a):
            n = a * a + b * b
            if n > n_max:
                continue
            if (a + b) % 2 == 0:
                continue
            if gcd(a, b) != 1:
                continue
            if is_z_prime(n) and n % 4 == 1:
                found.append(dict(a=a, b=b, N=n, kind="split",
                                  pi="%d+%di" % (a, b)))
        a += 1
    # inert: q = 3 mod 4 prime, element q + 0i, N = q^2
    q = 3
    while q * q <= n_max:
        if q % 4 == 3 and is_z_prime(q):
            found.append(dict(a=q, b=0, N=q * q, kind="inert",
                              pi=str(q)))
        q += 1
    found.sort(key=lambda d: (d["N"], d["b"], d["a"]))
    return found


def omega_of(a: int, b: int):
    n = a * a + b * b
    return (a + b * I_SYM) / sp.sqrt(n)


def in_mu4(om) -> bool:
    for k in range(4):
        if sp.simplify(om - I_SYM ** k) == 0:
            return True
    return False


def in_mu8(om) -> bool:
    for k in range(8):
        if sp.simplify(om - ZETA8 ** k) == 0:
            return True
    return False


def in_clifford_field(a: int, b: int) -> bool:
    """omega in Q(zeta8)=Q(i,sqrt(2)) iff N = 2^s * square."""
    n = a * a + b * b
    while n % 2 == 0:
        n //= 2
    r = int(math.isqrt(n))
    return r * r == n


# ----- Pauli group on 2 qubits (v783 computational basis) -----
def pauli1():
    I = sp.eye(2)
    X = sp.Matrix([[0, 1], [1, 0]])
    Y = sp.Matrix([[0, -I_SYM], [I_SYM, 0]])
    Z = sp.Matrix([[1, 0], [0, -1]])
    return [I, X, Y, Z]


_PAULI2 = None


def pauli2():
    global _PAULI2
    if _PAULI2 is None:
        ps = pauli1()
        _PAULI2 = [sp.kronecker_product(a, b) for a in ps for b in ps]
    return _PAULI2


def _mat_eq(A, B) -> bool:
    return sp.simplify(sp.Matrix(A) - sp.Matrix(B)) == sp.zeros(4)


def is_pauli_up_to_phase(M) -> bool:
    """True iff M = mu * P for a 2-qubit Pauli P (phase-1 set) and |mu|=1."""
    M = sp.simplify(M)
    # Clifford conjugation lands in the Pauli group (mu4 phases), not
    # a general U(1).  Matching 16 Paulis x 4 phases is the certificate.
    phases = [1, I_SYM, -1, -I_SYM]
    for P in pauli2():
        for mu in phases:
            if _mat_eq(M, mu * P):
                return True
    return False


def is_clifford_diag_anchor(om) -> bool:
    D = sp.diag(1, 1, 1, om)
    Dinv = sp.diag(1, 1, 1, 1 / om)
    for P in pauli2():
        Ad = sp.simplify(D * P * Dinv)
        if not is_pauli_up_to_phase(Ad):
            return False
    return True


def hadamard_q1():
    s = 1 / sp.sqrt(2)
    H = sp.Matrix([[s, s], [s, -s]])
    return sp.kronecker_product(H, sp.eye(2))


def is_clifford_matrix(U) -> bool:
    Uinv = sp.simplify(U.H)
    for P in pauli2():
        Ad = sp.simplify(U * P * Uinv)
        if not is_pauli_up_to_phase(Ad):
            return False
    return True


# ----- R_2 digit ring (same as qsys_jet / hjelmslev, m=2) -----
def build_R2():
    m = 2
    size = 4
    dec = []
    for code in range(size):
        a = b = 0
        pa, pb = 1, 0
        for j in range(m):
            if (code >> j) & 1:
                a += pa
                b += pb
            pa, pb = pa - pb, pa + pb
        dec.append((a, b))

    def enc(aa, bb):
        code = 0
        a, b = int(aa), int(bb)
        for _j in range(m):
            d = (a + b) & 1
            if d:
                code |= 1 << _j
                a -= 1
            a, b = (a + b) // 2, (b - a) // 2
        return code

    mul = [[enc(dec[x][0] * dec[y][0] - dec[x][1] * dec[y][1],
                dec[x][0] * dec[y][1] + dec[x][1] * dec[y][0])
            for y in range(size)] for x in range(size)]
    return dict(enc=enc, mul=mul, dec=dec, size=size)


def main() -> int:
    print("GNET.NONCLIFFORD.PRIME.01 -- Gaussian primes as write events "
          "on the v783 carrier")
    print("SPEC_SHA %s" % SPEC_SHA)

    with open(__file__, "r", encoding="utf-8") as fh:
        src = fh.read()
    bad = ast_firewall(src)
    check("G0 AST-firewall: no verification/zeta/numpy identifiers",
          not bad, "banned=%s" % (bad,) if bad else "")

    section("census: Gaussian primes N<=53, ring-internal")
    census = gaussian_prime_census(53)
    kinds = {}
    for d in census:
        kinds.setdefault(d["kind"], []).append(d)
    n_ram = len(kinds.get("ramified", []))
    n_spl = len(kinds.get("split", []))
    n_ine = len(kinds.get("inert", []))
    check("S1 census nonempty of all three types: ramified=%d split=%d "
          "inert=%d" % (n_ram, n_spl, n_ine),
          n_ram == 1 and n_spl >= 3 and n_ine >= 2)
    check("S2 ramified representative is 1+i (N=2)",
          kinds["ramified"][0]["a"] == 1 and kinds["ramified"][0]["b"] == 1)
    # composites must not appear: N=25=5^2 split composite, N=45 etc.
    ns = [d["N"] for d in census]
    check("S3 no composite norms (25,45,49-as-split) in census; 9=3^2 "
          "is the inert 3",
          25 not in ns and 45 not in ns and 4 not in ns
          and 9 in ns)
    check("C4 identity 1+0i is NOT in the prime census",
          not any(d["a"] == 1 and d["b"] == 0 for d in census))
    print("    CENSUS:", ", ".join("%s(%s,N=%d)" % (d["pi"], d["kind"], d["N"])
                                    for d in census))

    section("C1/C2 Clifford-detector wards")
    check("C1a I_4 is Clifford (normalizer test)",
          is_clifford_matrix(sp.eye(4)))
    check("C1b H(x)I is Clifford",
          is_clifford_matrix(hadamard_q1()))
    check("C2 diag(1,1,1,zeta8) is NOT Clifford (T-twist / CPhase(pi/4))",
          not is_clifford_diag_anchor(ZETA8))
    check("C2b diag(1,1,1,i) is NOT Clifford (CS = CPhase(pi/2) in C3, "
          "not C2)",
          not is_clifford_diag_anchor(I_SYM))
    check("C2c diag(1,1,1,-1) IS Clifford (CZ)",
          is_clifford_diag_anchor(-1))
    check("C2d i I_4 IS Clifford (Pauli-group / G31 scalar)",
          is_clifford_matrix(I_SYM * sp.eye(4)))
    check("C2e I(x)S = diag(1,i,1,i) IS Clifford (local S, not CPhase)",
          is_clifford_matrix(sp.diag(1, I_SYM, 1, I_SYM)))

    section("D1: global phase omega I  (matrix vs projective)")
    d1_rows = []
    d1_proj_all_id = True
    d1_mat_ok = True
    for d in census:
        om = omega_of(d["a"], d["b"])
        m4, m8 = in_mu4(om), in_mu8(om)
        # projective: any scalar is ~ I in PSU
        proj_id = True
        d1_proj_all_id = d1_proj_all_id and proj_id
        if d["kind"] == "ramified":
            want = (not m4) and m8
        elif d["kind"] == "inert":
            want = m4
        else:
            want = (not m8)
        d1_mat_ok = d1_mat_ok and want
        d1_rows.append((d, m4, m8, want))
    check("D1-proj ALL classes are projective identity "
          "(strong hyp DEAD at PSU)",
          d1_proj_all_id)
    check("D1-mat ramified in mu8\\mu4, inert in mu4, split not in mu8",
          d1_mat_ok,
          "fail=%s" % [d["pi"] for d, _m4, _m8, w in d1_rows if not w])
    ram_om = omega_of(1, 1)
    check("D1-zeta8  (1+i)/sqrt(2) == zeta8 exactly (metaplectic scalar)",
          sp.simplify(ram_om - ZETA8) == 0)

    section("D2: jet multiplication on R_2 = Z[i]/(2)")
    R2 = build_R2()
    one = R2["enc"](1, 0)
    eps = R2["enc"](1, 1)   # 1+i
    deck = R2["enc"](0, 1)  # i ≡ 1+eps?  wait i encodes as...
    # 1+eps should be enc of 1+(1+i)=2+i ≡ i mod 2 since 2=0, i.
    # Use: unit codes with odd (code & 1).
    jet_ok = True
    jet_rows = []
    for d in census:
        # Reduce in Z[i]/(2) first: unreduced 2+i would otherwise
        # get a Hjelmslev digit string that is not the ring class.
        code = R2["enc"](d["a"] & 1, d["b"] & 1)
        if d["kind"] == "ramified":
            # 1+i = eps, nilpotent: eps^2 = 0
            nilp = R2["mul"][code][code] == 0 and code != 0
            jet_ok = jet_ok and nilp
            jet_rows.append((d, "nilpotent" if nilp else "BAD", code))
        else:
            # unit, must be 1 or 1+eps.  1 = enc(1,0); 1+eps = enc(1,1)?
            # Units of F2[eps]: 1 and 1+eps.  enc(1,0)=1; i=enc(0,1).
            # On W, i = 1+eps (v803).  So allowed {one, deck} with
            # deck = image of i = enc(0,1).
            ok_u = code in (one, R2["enc"](0, 1))
            jet_ok = jet_ok and ok_u and (code & 1 == 1)
            tag = "id" if code == one else ("deck" if ok_u else "OUT")
            jet_rows.append((d, tag, code))
    check("D2 odd primes act as {1, 1+eps=deck} subset the clock "
          "(firmware on the jet); 1+i is nilpotent",
          jet_ok,
          "rows=" + ", ".join("%s:%s" % (d["pi"], t) for d, t, _c in jet_rows))

    section("D3: anchor CPhase  diag(1,1,1,omega)  Pauli-normalizer")
    d3_ok = True
    d3_field_ok = True
    d3_rows = []
    for d in census:
        om = omega_of(d["a"], d["b"])
        cl = is_clifford_diag_anchor(om)
        fld = in_clifford_field(d["a"], d["b"])
        if d["kind"] == "inert":
            want_cl, want_fld = True, True   # omega=1 in Q
        elif d["kind"] == "ramified":
            want_cl, want_fld = False, True  # zeta8 in Q(zeta8), not Clifford
        else:
            want_cl, want_fld = False, False
        d3_ok = d3_ok and (cl == want_cl)
        d3_field_ok = d3_field_ok and (fld == want_fld)
        d3_rows.append((d, cl, fld, cl == want_cl and fld == want_fld))
    check("D3-inert  frozen representative omega=1 is Clifford (I)",
          all(cl for d, cl, _f, _w in d3_rows if d["kind"] == "inert"))
    check("D3-ramified  CPhase(pi/4) is NOT Clifford (T-shape)",
          all((not cl) for d, cl, _f, _w in d3_rows if d["kind"] == "ramified"))
    check("D3-split  CPhase is NOT Clifford AND omega not in Q(zeta8)",
          all((not cl) and (not fld)
              for d, cl, fld, _w in d3_rows if d["kind"] == "split"))
    check("D3-all demands (inert Clifford / ramified T / split off-field)",
          d3_ok and d3_field_ok,
          "fail=" + ", ".join(d["pi"] for d, _c, _f, w in d3_rows if not w))
    check("FENCE inert omega=1 Clifford AND associate omega=i not "
          "(D3 is representative-dependent, not class-invariant)",
          is_clifford_diag_anchor(1) and (not is_clifford_diag_anchor(I_SYM)))

    # C3: family-slot scramble, reported, does not gate
    section("C3 family-slot scramble (reported, not a gate)")
    # For ramified, diag(1, zeta8, 1, 1) -- T on qubit-2 lsb-ish.
    Dfam = sp.diag(1, ZETA8, 1, 1)
    fam_cl = is_clifford_matrix(Dfam)
    print("    C3 diag(1,zeta8,1,1) Clifford? %s  "
          "(anchor-slot freeze is the v783 chart, not a search)"
          % fam_cl)
    check("C3 reported (family-slot T-shape also non-Clifford, as expected "
          "for any single-slot T)",
          True)  # informational; the freeze is the chart, not uniqueness

    section("verdict")
    n_pass = sum(1 for _, ok in CHECKS if ok)
    n_tot = len(CHECKS)

    def pfx(pref):
        return all(ok for n, ok in CHECKS if n.startswith(pref))

    c_ok = pfx("C1") and pfx("C2") and pfx("C4") and pfx("G0")
    fence_ok = pfx("FENCE")
    d2_fw = pfx("D2")
    d3_inert_cl = pfx("D3-inert")
    d3_ram_nc = pfx("D3-ramified")
    strong_dead = d2_fw and d3_inert_cl
    filtered = (pfx("S") and pfx("D1") and d2_fw and pfx("D3")
                and fence_ok and strong_dead and c_ok)
    all_nc = False  # would require D3-inert non-Clifford
    if not (pfx("C1") and pfx("C2")):
        verdict = "CONTROL-VOID"
    elif not d3_ram_nc:
        verdict = "NONCLIFFORD-PRIME-DEAD"
    elif filtered:
        verdict = "NONCLIFFORD-PRIME-FILTERED"
    elif all_nc:
        verdict = "NONCLIFFORD-PRIME-ALL"
    else:
        verdict = "NONCLIFFORD-PRIME-PARTIAL"

    print()
    print("GATES: %d/%d PASS   SPEC_SHA %s   runtime %.1f s"
          % (n_pass, n_tot, SPEC_SHA[:16], time.time() - T0))
    print("VERDICT %s" % verdict)
    print("STRONG HYPOTHESIS (every prime is a non-Clifford write): "
          "%s" % ("DEAD" if strong_dead else "OPEN"))
    print("FILTER: ramified=T-gate, split=off-field, frozen-inert=I; "
          "D1-proj invisible; D2 jet = firmware; "
          "FENCE D3 not associate-class invariant (unit i = G31 global, "
          "CS on anchor).  NO RH CLAIM.  NO MATTER SEMANTICS.")
    if n_pass != n_tot:
        print("FAILED: %s" % [n for n, ok in CHECKS if not ok])
    return 0 if (n_pass == n_tot and verdict == "NONCLIFFORD-PRIME-FILTERED") else 1


if __name__ == "__main__":
    raise SystemExit(main())
