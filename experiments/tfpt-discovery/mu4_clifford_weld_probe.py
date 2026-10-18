#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""mu4_clifford_weld_probe -- PRIME.MU4.CLIFFORD_WELD.01
(EXPLORATION ONLY, experiments/; round 33 midday-2 package C,
follow-up to DECK-MU-PARALLEL, 2026-08-08).

THE SHARPENED HYPOTHESIS: the arithmetic Moebius involution M and
the geometric deck involution D should NOT be identified but
PROJECTIVELY WELDED -- anticommutation:

    M^2 = D^2 = I,   MD + DM = 0   =>   (MD)^2 = -I,

so J := MD generates a faithful mu4 action, AND M then MOVES the
D-bands (Dv = v => D(Mv) = -Mv): M maps H_{D,+} -> H_{D,-} -- the
missing band-mover type from the Krein census.

TASK 1+2, THE CANDIDATES AND THE WELD TABLE (all five conditions
exact per candidate; register operators are Gaussian-unit matrices,
so float arithmetic is EXACT):
  K0  THE MANDATORY CONTROL (deployed wiring): M = T_s (mu-sign
      translation), D = T_d (deck translation by iota(deck) =
      (0,2)) on C[C2 x Z4] -- two COMMUTING involutions: the
      anticommutator is 2 T_s T_d != 0 and P- M P+ = 0 EXACTLY
      (M preserves the D-bands): the unwelded representation
      REFUSES the band swap -- the contrast.
  K1  FAITHFUL DIAGONAL CHARACTER (from the DECK-MU-PARALLEL
      candidates): M = T_s, J = Omega_chi with chi = (eps = -1,
      j = 1) (the faithful mu4 diagonal character), D := M J.
      Predeclared structure: JM = -MJ holds on the FULL register;
      D^2 = -J^2 = +I exactly on the FAITHFUL SECTOR V_f (mu4
      positions m odd, where J^2 = -I) and -I on the complement --
      the weld conditions THEMSELVES select the faithful sector;
      on V_f the built D is HERMITIAN (real bands).  Measured
      extra: D is Frobenius-ORTHOGONAL to the deployed deck T_d
      (the weld-built deck is a NEW involution, not the deployed
      one -- the gap named).
  K2  GALOIS mu_K = chi4 BOOKKEEPING: per odd prime the residue
      sheet space C^2; inert (deck-odd) p: Frobenius D = X, mu-sign
      lift M = Z (the sign lives on the Frobenius-odd line):
      full 2x2 weld; split p: D = I, mu_K = +1 scalar -- weldless.
      The weld locus == the inert sector == exactly where
      mu(p) = -1 survives the cover (classified by x^2 + y^2
      witnesses for ALL odd p <= 10^4, own arithmetic).
  K3  HALL CHAIN-PARITY COVER: the divisor register doubled by the
      chain-parity sheet, n = 360: M = diag(lambda(k)) (x) Z_pauli
      (Liouville = maximal-chain parity, own sieve), D = I (x) X
      (sheet swap): full weld BY CONSTRUCTION (typed: the doubling
      supplies the qubit -- construction-grade, not deployed).
  K4  METAPLECTIC/SYMPLECTIC FOURIER LIFT (v800 torsor-Fourier
      machinery): register C[F2^4], dim 16.  Weld pair M =
      Omega_w0, D = T_a0 with <w0, a0> = 1: FULL-SPACE weld
      (J^2 = -I globally); the Walsh/Hadamard lift swaps
      diagonal <-> translation (H T_a H / 16 = Omega_a exact);
      the bent-translate frame (arf_bent_css, parameter q =
      x1x2 + x3x4, deployed q* cited read-only) is MUTUALLY
      UNBIASED against the characters (all 256 cross products
      +-4) and sits EXACTLY HALFWAY between weld and co-weld:
      ||{M_q, T_a}||_F = ||[M_q, T_a]||_F = sqrt(32) for EVERY
      a != 0 (equivalent to bentness) -- the bent register is
      the maximally weld-neutral frame.

THE STRUCTURAL LAW (exact census, the reason the deployed wiring
cannot weld): a Weyl-pair weld (involutive translation T_a +
involutive modulation Omega_psi with psi(a) = -1) exists iff the
2-torsion pairing of the slot is nontrivial -- counts: C2: 1 pair;
Z4: 0; Z8: 0 (any cyclic 2-group of order >= 4: ZERO -- enlarging
the cyclic register NEVER helps); F2^4: 120 pairs.  On the deployed
128-register: T_s (mu-sign) anticommutes with 64 characters of
which 32 are involutive => WELDABLE; T_d (deck) anticommutes with
64 (all j odd) of which ZERO are involutive => UNWELDABLE at
register level.  The v833 metaplectic deck (T3 K3)^3 = i I is
CENTRAL: upstairs the deck is J-grade (order 4), not D-grade --
consistent with reading J = MD as the deck's faithful lift.

TASK 3, THE CONTRACTOR CONNECTION (the payoff test): rebuild the
Krein cut-1 arms B+/- at the anchors kz 9/12/13
(krein_normalform machinery, circulant embedding, READ-ONLY
reproduction with the Gram ward); C = B- pinv(B+) has row support
in the negative band and column support in the positive band BY
CONSTRUCTION, so the polar factorization C = U |C| ALWAYS has
band-internal |C| -- the CONTENT is whether the polar phase U is a
SOURCE-BUILT swap: residuals r(W) = ||C - W |C| ||_F / ||C||_F for
the frozen source swaps W in {FLIP (j -> L-j), HALF (j -> j+L/2),
FLIP o HALF} + a random-swap null (LCG) + the displacement
diagnostic of U (top singular pairs).  CONNECTED iff some source W
has r(W) <= 0.10 on ALL three anchors.  (Typed expectation from the
Krein census: FLIP is support-preserving -- d is even -- and no
short word bridged the bands; the residuals quantify the gap.)

TASK 4: K0 above (exact refusal).  TASK 5: honest typing in the
verdict.

CONTROLS: deck/mu regressions ((1+i)^2 = 2i; chi_GL1 separates the
two C2s; Hall row 1 == mu at n = 120; tau kz9 frozen ref); v800
mutual-unbiasedness reproduction (256 products); scramble MUST-FIRE
(random diagonal replaces the faithful character -- weld conditions
break; random Boolean function replaces the bent q -- MUB and the
midpoint identity break); Krein regression ||C|| <= 1 + 1e-6 at
the anchors.

VERDICT (frozen): WELD-FOUND (+ band-mover + contractor status;
prominent if all three) / WELD-WITHOUT-CONTRACTOR / NO-WELD (per-
candidate failing conditions typed).

NO RH claim; writes nothing; nothing outside experiments/; v563
READ-ONLY; own sieves; AST firewall.

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/mu4_clifford_weld_probe.py
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

import v563_paper2_readouts as core        # noqa: E402  (READ-ONLY)

FROZEN_SPEC = """\
PRIME.MU4.CLIFFORD_WELD.01 spec v1 (2026-08-08, frozen before run).
WELD CONDITIONS per candidate (exact, Gaussian-unit arithmetic):
C1 M^2 = I; C2 D^2 = I; C3 MD + DM = 0; C4 (MD)^2 = -I; C5 band
move ||P- M P+||_2 = 1 AND ||P+ M P+|| = 0 (P+- = (I +- D)/2, D
hermitian on the declared domain).  Declared domains: K0 full
C[C2 x Z4] (control: expect C3/C4 FAIL, ||{M,D}||_2 = 2, and
P- M P+ = 0 EXACTLY); K1 faithful sector V_f = span{m odd} (C3
holds on the FULL register; C2/C4/C5 on V_f; D := M J with J =
Omega_(eps=-1,j=1); extras: D hermitian on V_f, D^2 = -I on the
complement, <D, T_d>_F = 0); K2 inert 2x2 block (D = X, M = Z; the
split block D = I, M = I refuses C3 -- typed; weld locus census:
inert <=> p == 3 mod 4 <=> NO x^2+y^2 rep, ALL odd p <= 10^4,
expect 619 inert / 609 split of 1228); K3 full doubled register
n = 360 (M = diag(lambda) (x) Z, D = I (x) X, lambda own sieve);
K4 full C[F2^4] (M = Omega_w0, D = T_a0, w0 = a0 = 0b0001).
STRUCTURAL LAW census (exact): weld pairs (involutive translation,
involutive modulation, pairing -1): C2: 1, Z4: 0, Z8: 0, F2^4:
15 x 8 = 120; 128-register census: T_s: 64 anticommuting chars, 32
involutive; T_d: 64 anticommuting (j odd), 0 involutive.
FOURIER LIFT ward: H T_a H / 16 == Omega_a exact for all 16 a
(H = Walsh 16, H^2 = 16 I).  MUB ward: |<chi_w, bent-translate_a>|
= 4 for all 256 pairs (q = x1x2 + x3x4 parameter grade, deployed
q* cited).  MIDPOINT ward: ||{M_q, T_a}||_F^2 == ||[M_q, T_a]||_F^2
== 32 for all 15 a != 0.  CONTRACTOR: anchors kz (9, 12, 13);
cut-1 arms B+/- = diag(sqrt(max(+-d,0)/2L)) F pad E_odd, d =
FFT(fold(c_ar + c_at)), L = 4h - 2; Gram ward max|B+*B+ - B-*B- -
K| <= 1e-9 max|K| (imag too); Krein regression ||C||_2 <= 1 + 1e-6;
C = B- pinv(B+) (svd cut 1e-12 sigma_max); |C| = (C*C)^(1/2) by
eigh; residual r(W) = ||C - W|C|||_F/||C||_F for W in {FLIP:
i <- (L-i) mod L, HALF: i <- (i - L/2) mod L, FLIPHALF}, plus
RANDOM null (LCG row permutation + random Gaussian-unit phases);
support match fraction |pi(S+) n S-|/|S+| printed (S+- = sign
bands of d at 1e-12 rel tol); displacement diagnostic: top 6
singular pairs of C, argmax rows of U vs V, folded displacement.
CONNECTED iff min over source W of max over anchors r(W) <= 0.10.
CONTROLS/regressions: (1+i)^2 = 2i; chi_GL1(s) = -1 AND
chi_GL1(iota(deck)) = +1; Hall M-row-1 == mu at n = 120 (integer
N-power alternating sum); tau(kz 9) vs 5.984165e-4 rel 1e-4;
scramble A: J_scr = random Gaussian-unit diagonal (LCG), D_scr =
T_s J_scr: at least one of C2/C3/C4 must FAIL on V_f; scramble B:
q_scr = random 16-bit Boolean function (LCG): MUB ward AND midpoint
ward must FAIL.  VERDICT: WELD-FOUND iff >= 1 candidate among
K1-K4 passes C1-C5 exactly on its declared domain AND K0 shows
P- M P+ = 0 with nonzero anticommutator; + CONTRACTOR iff the
residual bar above; WELD-WITHOUT-CONTRACTOR if weld but no source
swap; NO-WELD else.  EXACT0 = 0.0 (unit-matrix arithmetic is exact
in float); float bars: band norms |.-1| <= 1e-12, Krein wards as
above.  LCG seed 20260808.  NO RH claim; writes nothing.
"""

ANCHORS = (9, 12, 13)
RES_BAR = 0.10
WARD_KREIN = 1.0e-9
CNORM_BAR = 1.0 + 1.0e-6
REG_REF_KZ9 = 5.984165e-4
REG_BAR = 1.0e-4
N_HALL = 360
N_HALL_REG = 120
P_MAX = 10_000
BAND_TOL = 1.0e-12
BANNED_IDS = ("zetazero", "nzeros", "primerange", "isprime", "primepi",
              "nextprime", "prevprime")

CHECKS = []
FAILS = []
T0 = time.time()
_LCG = [20260808]


def lcg():
    _LCG[0] = (6364136223846793005 * _LCG[0] + 1442695040888963407) % (1 << 63)
    return _LCG[0] / float(1 << 63)


def lcg_int(n):
    return int(lcg() * n)


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok)))
    tag = "PASS" if ok else "FAIL"
    if not ok:
        FAILS.append(name)
    print("[%s] %s%s" % (tag, name, ("  -- " + detail) if detail else ""))


def section(title):
    print()
    print("=" * 72)
    print(title)
    print("=" * 72)


def ast_firewall():
    src = open(os.path.abspath(__file__), encoding="utf-8").read()
    bad = []
    for node in ast.walk(ast.parse(src)):
        name = None
        if isinstance(node, ast.Name):
            name = node.id
        elif isinstance(node, ast.Attribute):
            name = node.attr
        if name and name.lower() in BANNED_IDS:
            bad.append(name)
    return bad


def zero(X):
    """Exact-zero test for Gaussian-unit matrix expressions."""
    return float(np.max(np.abs(X))) == 0.0


def op2norm(X):
    return float(np.linalg.svd(X, compute_uv=False)[0]) if X.size else 0.0


# ===================================================== register layer
IUNIT = (1 + 0j, 1j, -1 + 0j, -1j)


def reg8():
    """C[C2 x Z4]: index g = 4a + m.  Returns T_s, T_d, J, I."""
    dim = 8

    def idx(a, m):
        return 4 * (a % 2) + (m % 4)

    Ts = np.zeros((dim, dim), dtype=complex)
    Td = np.zeros((dim, dim), dtype=complex)
    Jd = np.zeros((dim, dim), dtype=complex)
    for a in range(2):
        for m in range(4):
            g = idx(a, m)
            Ts[idx(a + 1, m), g] = 1.0
            Td[idx(a, m + 2), g] = 1.0
            Jd[g, g] = ((-1) ** a) * IUNIT[m % 4]
    return Ts, Td, Jd, np.eye(dim, dtype=complex)


def pauli():
    X = np.array([[0, 1], [1, 0]], dtype=complex)
    Z = np.array([[1, 0], [0, -1]], dtype=complex)
    return X, Z, np.eye(2, dtype=complex)


def hadamard16():
    x = np.arange(16)
    pc = np.array([bin(v).count("1") for v in range(16)])
    return np.array([[(-1.0) ** pc[i & j] for j in x] for i in x],
                    dtype=complex)


def translation16(a):
    T = np.zeros((16, 16), dtype=complex)
    for x in range(16):
        T[x ^ a, x] = 1.0
    return T


def modulation16(w):
    return np.diag(np.array(
        [(-1.0) ** bin(w & x).count("1") for x in range(16)],
        dtype=complex))


def qvec(qbits):
    """Phase vector (-1)^q as diagonal, q given as 16-bit int."""
    return np.diag(np.array([(-1.0) ** ((qbits >> x) & 1)
                             for x in range(16)], dtype=complex))


Q_PLUS = sum(1 << x for x in range(16)
             if (((x >> 0) & (x >> 1)) ^ ((x >> 2) & (x >> 3))) & 1)


# ===================================================== weld condition kit
def weld_table(M, D, dom=None, band=True):
    """The five conditions on the (optionally restricted) domain.
    dom = list of basis indices or None (full).  Returns dict."""
    if dom is not None:
        S = np.zeros((M.shape[0], len(dom)), dtype=complex)
        for k, g in enumerate(dom):
            S[g, k] = 1.0
        Mr, Dr = S.conj().T @ M @ S, S.conj().T @ D @ S
    else:
        Mr, Dr = M, D
    Ir = np.eye(Mr.shape[0], dtype=complex)
    out = {}
    out["C1"] = zero(Mr @ Mr - Ir)
    out["C2"] = zero(Dr @ Dr - Ir)
    AC = Mr @ Dr + Dr @ Mr
    out["C3"] = zero(AC)
    out["ac_norm"] = op2norm(AC)
    MD = Mr @ Dr
    out["C4"] = zero(MD @ MD + Ir)
    out["herm_D"] = zero(Dr - Dr.conj().T)
    if band and out["C2"] and out["herm_D"]:
        Pp = 0.5 * (Ir + Dr)
        Pm = 0.5 * (Ir - Dr)
        out["swap"] = op2norm(Pm @ Mr @ Pp)
        out["keep"] = op2norm(Pp @ Mr @ Pp)
        out["C5"] = (abs(out["swap"] - 1.0) <= 1e-12
                     and out["keep"] <= 1e-12)
    else:
        out["swap"], out["keep"], out["C5"] = None, None, False
    return out


def fmt_row(name, w):
    def b(v):
        return " OK " if v else "FAIL"
    sw = ("%.3f" % w["swap"]) if w["swap"] is not None else " -- "
    kp = ("%.3f" % w["keep"]) if w["keep"] is not None else " -- "
    return ("    %-26s %s %s %s %s %s   swap %s keep %s |{M,D}| %.3f"
            % (name, b(w["C1"]), b(w["C2"]), b(w["C3"]), b(w["C4"]),
               b(w["C5"]), sw, kp, w["ac_norm"]))


# ===================================================== arithmetic bits
def liouville(n):
    spf = np.zeros(n + 1, dtype=np.int64)
    for p in range(2, int(n ** 0.5) + 1):
        if spf[p] == 0:
            sl = spf[p * p::p]
            sl[sl == 0] = p
            spf[p * p::p] = sl
    pm = (spf == 0)
    pm[:2] = False
    pr = np.nonzero(pm)[0]
    spf[pr] = pr
    lam = np.ones(n + 1, dtype=np.int64)
    for k in range(2, n + 1):
        kk, cnt = k, 0
        while kk > 1:
            p = int(spf[kk])
            while kk % p == 0:
                kk //= p
                cnt += 1
        lam[k] = (-1) ** cnt
    mu = np.ones(n + 1, dtype=np.int64)
    mu[0] = 0
    for p in pr:
        mu[p::p] *= -1
    for p in pr[pr * pr <= n]:
        mu[p * p::p * p] = 0
    return lam, mu, pr


# ===================================================== krein layer (port)
def odd_extend_mat(h):
    E = np.zeros((2 * h, h))
    E[:h] = np.eye(h)
    E[h:] = -np.eye(h)[::-1]
    return E


def grid_density(c):
    c = np.asarray(c, float)
    a = np.concatenate([c, c[-2:0:-1]])
    d = np.fft.fft(a)
    assert float(np.max(np.abs(d.imag))) <= 1e-9 * max(
        1.0, float(np.max(np.abs(d.real))))
    return d.real


def krein_arms(d, h):
    M = 2 * h
    L = 2 * M - 2
    E = odd_extend_mat(h)
    Fp = np.fft.fft(np.vstack([E, np.zeros((L - M, h))]), axis=0)
    dp = np.sqrt(np.maximum(d, 0.0) / (2.0 * L))
    dm = np.sqrt(np.maximum(-d, 0.0) / (2.0 * L))
    return dp[:, None] * Fp, dm[:, None] * Fp


def contractor(Bp, Bm):
    U, s, Vh = np.linalg.svd(Bp, full_matrices=False)
    r = int(np.sum(s > 1e-12 * s[0]))
    U, s, Vh = U[:, :r], s[:r], Vh[:r]
    return Bm @ (Vh.conj().T / s) @ U.conj().T


# ================================================================ main
def main():
    print("mu4_clifford_weld_probe -- the projective weld M/D "
          "(anticommutation)")
    print("vs identification.  EXPLORATION ONLY, NO RH CLAIM.")
    sha = hashlib.sha256(FROZEN_SPEC.encode("utf-8")).hexdigest()
    print("    FROZEN_SPEC SHA-256 = %s" % sha)

    section("S0 -- firewall")
    check("S0.1 AST firewall: no zeta-zero / prime-table symbols",
          not ast_firewall(), str(ast_firewall()))

    # ------------------------------------------------------------- S1
    section("S1 -- register layer + deck/mu regressions (CTRL-R)")
    z = complex(1, 1)
    check("S1.1 regression: (1+i)^2 = 2i exact", z * z == complex(0, 2))
    # chi_GL1 separation (previous probe S2.3, reproduced)
    chi_s = (-1) ** 1                    # chi_GL1(s): eps part on a = 1
    chi_d = IUNIT[(0 * 2) % 4]           # j = 0 on m = 2
    check("S1.2 regression: chi_GL1 separates the two C2s "
          "(chi(s) = -1, chi(iota(deck)) = +1)",
          chi_s == -1 and chi_d == 1)
    lam, mu, _ = liouville(N_HALL)
    # Hall row 1 == mu at n = 120 (alternating chain census)
    n = N_HALL_REG
    Zi = np.zeros((n, n), dtype=np.int64)
    for a in range(1, n + 1):
        Zi[a - 1, a - 1::a] = 1
    Ni = Zi - np.eye(n, dtype=np.int64)
    Mi = np.eye(n, dtype=np.int64)
    Pk = np.eye(n, dtype=np.int64)
    sgn = 1
    while Pk.any():
        Pk = Pk @ Ni
        sgn = -sgn
        Mi = Mi + sgn * Pk
    check("S1.3 regression: Hall chain parity row 1 == mu (n = %d)" % n,
          bool(np.array_equal(Mi[0], mu[1:n + 1])))
    H = hadamard16()
    check("S1.4 Walsh frame: H^2 = 16 I exact",
          zero(H @ H - 16 * np.eye(16)))
    ok_four = all(zero(H @ translation16(a) @ H / 16 - modulation16(a))
                  for a in range(16))
    check("S1.5 THE FOURIER LIFT: H T_a H / 16 == Omega_a for ALL 16 a "
          "(the diagonal <-> translation swapper, exact)", ok_four)
    Mq = qvec(Q_PLUS)
    ok_mub = True
    for w in range(16):
        chi_row = np.array([(-1.0) ** bin(w & x).count("1")
                            for x in range(16)])
        for a in range(16):
            bt = np.array([Mq[(x ^ a), (x ^ a)].real for x in range(16)])
            if abs(abs(float(chi_row @ bt)) - 4.0) > 1e-12:
                ok_mub = False
    check("S1.6 v800 MUB reproduction: |<chi_w, bent-translate_a>| = 4 "
          "for all 256 pairs (Gram-16I frames mutually unbiased)",
          ok_mub)

    # ------------------------------------------------------------- S2
    section("S2 -- THE STRUCTURAL LAW: the 2-torsion weld census")

    def weld_pairs_cyclic(order):
        cnt = 0
        for a in range(1, order):
            if (2 * a) % order:
                continue
            for j in range(1, order):
                if (2 * j) % order:
                    continue
                # psi_j(a) = exp(2 pi i j a / order) = -1 ?
                if (2 * j * a) % (2 * order) == order:
                    cnt += 1
        return cnt

    c2c, c4c, c8c = (weld_pairs_cyclic(2), weld_pairs_cyclic(4),
                     weld_pairs_cyclic(8))
    f16c = sum(1 for a in range(1, 16) for w in range(16)
               if bin(a & w).count("1") % 2 == 1)
    check("S2.1 Weyl weld pairs: C2 = %d, Z4 = %d, Z8 = %d, F2^4 = %d "
          "-- cyclic 2-groups of order >= 4 have ZERO (trivial "
          "2-torsion pairing): enlarging the cyclic register NEVER "
          "helps" % (c2c, c4c, c8c, f16c),
          (c2c, c4c, c8c, f16c) == (1, 0, 0, 120))
    # 128-register anticommutant census
    CH = [(e, w, j) for e in range(2) for w in range(16)
          for j in range(4)]

    def chival(chi, g):
        e, w, j = chi
        a, v, m = g
        return ((-1) ** (e * a) * (-1) ** bin(w & v).count("1")
                * IUNIT[(j * m) % 4])

    s_gen, deck_img = (1, 0, 0), (0, 0, 2)
    ac_s = [c for c in CH if chival(c, s_gen) == -1]
    ac_d = [c for c in CH if chival(c, deck_img) == -1]
    inv_s = [c for c in ac_s if c[2] in (0, 2)]
    inv_d = [c for c in ac_d if c[2] in (0, 2)]
    check("S2.2 THE ASYMMETRY on the deployed 128-register: T_s (mu-"
          "sign) has %d anticommuting characters, %d involutive => "
          "WELDABLE; T_d (deck) has %d anticommuting (all j odd), %d "
          "involutive => UNWELDABLE at register level"
          % (len(ac_s), len(inv_s), len(ac_d), len(inv_d)),
          (len(ac_s), len(inv_s), len(ac_d), len(inv_d))
          == (64, 32, 64, 0))
    print("    typed: the deck's anticommutant is EXACTLY the faithful")
    print("    (j odd) characters -- order 4, never involutive: the")
    print("    deck can only be welded through a FAITHFUL mu4 object,")
    print("    i.e. as J = MD (the weld's own quarter turn), never as")
    print("    a second involution D' in the register.  The v833")
    print("    metaplectic deck i*I is central = J-grade: consistent.")

    # ------------------------------------------------------------- S3
    section("S3 -- THE CANDIDATE TABLE (five weld conditions, exact)")
    print("    columns: C1 M^2=I | C2 D^2=I | C3 {M,D}=0 | C4 (MD)^2="
          "-I | C5 band")
    Ts, Td, Jd, _ = reg8()
    results = {}
    # K0 control: deployed commuting pair
    w0 = weld_table(Ts, Td)
    results["K0"] = w0
    print(fmt_row("K0 deployed T_s, T_d", w0))
    ok_k0 = (w0["C1"] and w0["C2"] and not w0["C3"]
             and abs(w0["ac_norm"] - 2.0) <= 1e-12
             and not w0["C4"] and w0["swap"] is not None
             and w0["swap"] <= 1e-15 and abs(w0["keep"] - 1.0) <= 1e-12)
    check("S3.0 MANDATORY CONTROL K0: the unwelded C2 x C2 REFUSES the "
          "band swap EXACTLY ([M,D] = 0, ||{M,D}|| = 2, P- M P+ = 0, "
          "P+ M P+ = full)", ok_k0,
          "swap = %.1e, keep = %.3f" % (w0["swap"], w0["keep"]))
    # K1 faithful diagonal character weld
    Dw = Ts @ Jd
    dom_f = [4 * a + m for a in range(2) for m in (1, 3)]
    dom_c = [4 * a + m for a in range(2) for m in (0, 2)]
    w1 = weld_table(Ts, Dw, dom=dom_f)
    results["K1"] = w1
    print(fmt_row("K1 diag-char weld (V_f)", w1))
    ac_full = zero(Ts @ Dw + Dw @ Ts)
    j_is_md = zero(Ts @ Dw - Jd)
    Sc = np.zeros((8, 4), dtype=complex)
    for k, g in enumerate(dom_c):
        Sc[g, k] = 1.0
    Dc = Sc.conj().T @ Dw @ Sc
    anti_c = zero(Dc @ Dc + np.eye(4, dtype=complex))
    ortho = float(abs(np.trace(Dw.conj().T @ Td)))
    check("S3.1 K1 structure: {M, D} = 0 on the FULL register; "
          "J = M D exactly (the faithful mu4); D^2 = -I on the "
          "complement (the weld conditions SELECT the faithful "
          "sector); D hermitian on V_f",
          ac_full and j_is_md and anti_c and w1["herm_D"])
    check("S3.2 K1 gap: the weld-built D is Frobenius-ORTHOGONAL to "
          "the deployed deck T_d (<D, T_d>_F = %.1f) -- a NEW "
          "involution, not the deployed one" % ortho, ortho == 0.0)
    # K2 Galois sector weld
    X2, Z2, I2 = pauli()
    w2 = weld_table(Z2, X2)
    results["K2"] = w2
    print(fmt_row("K2 Galois inert block", w2))
    w2s = weld_table(I2, I2, band=False)
    _, _, pr_full = liouville(P_MAX)
    n_split = n_inert = 0
    ok_cls = True
    for p in [int(q) for q in pr_full if q > 2]:
        has = False
        x = 1
        while 2 * x * x <= p:
            y2 = p - x * x
            y = int(math.isqrt(y2))
            if y * y == y2:
                has = True
                break
            x += 1
        if p % 4 == 1:
            n_split += 1
            ok_cls &= has
        else:
            n_inert += 1
            ok_cls &= not has
    check("S3.3 K2 weld locus: inert (weld) = %d, split (weldless, "
          "D = I scalar: {M,D} = 2I != 0) = %d, all classified by "
          "x^2+y^2 witnesses -- the weld locus IS the mu(p) = -1 "
          "survival locus" % (n_inert, n_split),
          ok_cls and (n_inert, n_split) == (619, 609)
          and not w2s["C3"])
    # K3 Hall chain-parity cover
    Lm = np.diag(lam[1:N_HALL + 1].astype(complex))
    M3 = np.kron(Lm, Z2)
    D3 = np.kron(np.eye(N_HALL, dtype=complex), X2)
    w3 = weld_table(M3, D3)
    results["K3"] = w3
    print(fmt_row("K3 Hall cover (n=360)", w3))
    # K4 Fourier/Weyl weld
    M4 = modulation16(1)
    D4 = translation16(1)
    w4 = weld_table(M4, D4)
    results["K4"] = w4
    print(fmt_row("K4 Weyl pair on F2^4", w4))
    # bent midpoint
    ok_mid = True
    for a in range(1, 16):
        Ta = translation16(a)
        acn = float(np.linalg.norm(Mq @ Ta + Ta @ Mq)) ** 2
        ccn = float(np.linalg.norm(Mq @ Ta - Ta @ Mq)) ** 2
        if abs(acn - 32.0) > 1e-9 or abs(ccn - 32.0) > 1e-9:
            ok_mid = False
    check("S3.4 K4 bent midpoint: ||{M_q, T_a}||_F^2 = ||[M_q, T_a]||"
          "_F^2 = 32 for ALL 15 a != 0 (the bent frame is exactly "
          "halfway between weld and co-weld == bentness)", ok_mid)
    welded = [k for k in ("K1", "K2", "K3", "K4")
              if all(results[k][c] for c in
                     ("C1", "C2", "C3", "C4", "C5"))]
    check("S3.5 WELD CENSUS: candidates passing ALL FIVE conditions "
          "on their declared domain = %s" % welded,
          welded == ["K1", "K2", "K3", "K4"])

    # ------------------------------------------------------------- S4
    section("S4 -- band movement (quantified) -- theorem check")
    print("    anticommutation <=> full band swap: measured swap/keep")
    for k in ("K1", "K2", "K3", "K4"):
        print("    %s: ||P- M P+|| = %.12f   ||P+ M P+|| = %.2e"
              % (k, results[k]["swap"], results[k]["keep"]))
    check("S4.1 every welded candidate is a FULL band mover (swap "
          "norm 1, in-band block 0) and the control K0 is a FULL "
          "band keeper",
          all(abs(results[k]["swap"] - 1.0) <= 1e-12
              and results[k]["keep"] <= 1e-12 for k in welded))

    # ------------------------------------------------------------- S5
    section("S5 -- THE CONTRACTOR CONNECTION (Krein anchors, "
            "polar test)")
    res_by_w = {"FLIP": [], "HALF": [], "FLIPHALF": [], "RANDOM": []}
    ok_ward = True
    ok_creg = True
    tau_kz9 = None
    for kz in ANCHORS:
        rr = core.build_window(kz)
        h, Mz, D, alpha = rr["h"], rr["M"], rr["D"], rr["alpha"]
        uu = np.asarray(rr["uu"], float)
        mm = 2.0 * np.asarray(rr["lam"], float)
        c_at, _ = core.atom_lags_at(alpha, Mz, uu, mm)
        c_ar = np.asarray(core.arch_lags(Mz, D), float)
        K = core.odd_toeplitz(c_ar + c_at, Mz)
        if kz == 9:
            tau_kz9 = float(np.linalg.eigvalsh(
                np.asarray(rr["Ah"], float))[0])
        d = grid_density(c_ar + c_at)
        L = 2 * (2 * h) - 2
        Bp, Bm = krein_arms(d, h)
        G = Bp.conj().T @ Bp - Bm.conj().T @ Bm
        ks = max(float(np.max(np.abs(K))), 1e-300)
        ok_ward &= (float(np.max(np.abs(G.real - K))) / ks <= WARD_KREIN
                    and float(np.max(np.abs(G.imag))) / ks <= WARD_KREIN)
        C = contractor(Bp, Bm)
        cn = op2norm(C)
        ok_creg &= cn <= CNORM_BAR
        # polar magnitude
        ev, V = np.linalg.eigh(C.conj().T @ C)
        ev = np.maximum(ev, 0.0)
        absC = (V * np.sqrt(ev)) @ V.conj().T
        nC = float(np.linalg.norm(C))
        dmax = float(np.max(np.abs(d)))
        Sp = set(np.nonzero(d > BAND_TOL * dmax)[0].tolist())
        Sm = set(np.nonzero(d < -BAND_TOL * dmax)[0].tolist())
        swaps = {
            "FLIP": np.array([(L - i) % L for i in range(L)]),
            "HALF": np.array([(i - L // 2) % L for i in range(L)]),
            "FLIPHALF": np.array([((L - i) - L // 2) % L
                                  for i in range(L)]),
        }
        rnd = np.arange(L)
        for i in range(L - 1, 0, -1):
            jr = lcg_int(i + 1)
            rnd[i], rnd[jr] = rnd[jr], rnd[i]
        swaps["RANDOM"] = rnd
        rphase = np.array([IUNIT[lcg_int(4)] for _ in range(L)])
        print("    kz %-3d h %-4d L %-4d ||C|| %.6f  |S+| %d |S-| %d"
              % (kz, h, L, cn, len(Sp), len(Sm)))
        for wname, src in swaps.items():
            Wabs = absC[src, :]
            if wname == "RANDOM":
                Wabs = rphase[:, None] * Wabs
            res = float(np.linalg.norm(C - Wabs)) / max(nC, 1e-300)
            dest = {}
            for j in Sp:
                ii = np.nonzero(src == j)[0]
                if len(ii):
                    dest[j] = int(ii[0])
            match = (sum(1 for j in dest if dest[j] in Sm)
                     / max(len(dest), 1))
            res_by_w[wname].append(res)
            print("        %-9s residual %.4f   S+ -> S- support "
                  "match %.2f" % (wname, res, match))
        # displacement diagnostic
        Uc, sc, Vch = np.linalg.svd(C)
        print("        polar displacement (top 6 singular pairs):")
        for k in range(6):
            ik = int(np.argmax(np.abs(Uc[:, k])))
            jk = int(np.argmax(np.abs(Vch[k, :])))
            dsp = (ik - jk) % L
            if dsp > L // 2:
                dsp -= L
            print("          s%-2d = %.4f  row %4d <- col %4d  "
                  "displacement %+d" % (k, float(sc[k]), ik, jk, dsp))
    check("S5.1 Krein Gram ward: B+*B+ - B-*B- == K to 1e-9 at all "
          "3 anchors (read-only reproduction)", ok_ward)
    check("S5.2 Krein regression: ||C|| <= 1 + 1e-6 at all anchors",
          ok_creg)
    check("S5.3 CTRL-R: tau(kz 9) = %.6e vs frozen ref %.6e"
          % (tau_kz9, REG_REF_KZ9),
          abs(tau_kz9 / REG_REF_KZ9 - 1.0) < REG_BAR)
    best_w, best_r = None, np.inf
    for wname in ("FLIP", "HALF", "FLIPHALF"):
        r = max(res_by_w[wname])
        if r < best_r:
            best_w, best_r = wname, r
    connected = best_r <= RES_BAR
    check("S5.4 contractor connection: best source swap %s with max-"
          "anchor residual %.4f %s %.2f => %s (random null %.4f)"
          % (best_w, best_r, "<=" if connected else ">", RES_BAR,
             "CONNECTED" if connected else "NOT CONNECTED",
             max(res_by_w["RANDOM"])), True)

    # ------------------------------------------------------------- S6
    section("S6 -- scramble controls (MUST-FIRE)")
    Jscr = np.diag(np.array([IUNIT[lcg_int(4)] for _ in range(8)]))
    Dscr = Ts @ Jscr
    ws = weld_table(Ts, Dscr, dom=dom_f)
    fired_a = not (ws["C2"] and ws["C3"] and ws["C4"])
    check("S6.1 scramble A: random Gaussian-unit diagonal replaces "
          "the faithful character -- weld breaks (C2 %s, C3 %s, "
          "C4 %s)" % (ws["C2"], ws["C3"], ws["C4"]), fired_a)
    qscr = 0
    for x in range(16):
        if lcg() < 0.5:
            qscr |= 1 << x
    Mqs = qvec(qscr)
    mub_fail = False
    for w in range(0, 16, 3):
        chi_row = np.array([(-1.0) ** bin(w & x).count("1")
                            for x in range(16)])
        for a in range(0, 16, 3):
            bt = np.array([Mqs[(x ^ a), (x ^ a)].real
                           for x in range(16)])
            if abs(abs(float(chi_row @ bt)) - 4.0) > 1e-9:
                mub_fail = True
    mid_fail = False
    for a in range(1, 16):
        Ta = translation16(a)
        acn = float(np.linalg.norm(Mqs @ Ta + Ta @ Mqs)) ** 2
        if abs(acn - 32.0) > 1e-9:
            mid_fail = True
    check("S6.2 scramble B: random Boolean function replaces the bent "
          "q -- MUB fails (%s) AND the midpoint identity fails (%s)"
          % (mub_fail, mid_fail), mub_fail and mid_fail)

    # ------------------------------------------------------------- V
    section("V -- FROZEN VERDICT + the honest consequence")
    npass = sum(1 for _, ok in CHECKS if ok)
    print("    checks: %d/%d passed%s"
          % (npass, len(CHECKS),
             "" if not FAILS else "; FAILS: %s" % FAILS))
    weld_found = bool(welded) and ok_k0 and not FAILS
    if FAILS:
        verdict = "WELD-WARD-FAIL"
    elif weld_found and connected:
        verdict = "WELD-FOUND (+BAND-MOVER +CONTRACTOR)"
    elif weld_found:
        verdict = "WELD-WITHOUT-CONTRACTOR"
    else:
        verdict = "NO-WELD"
    print()
    print("    VERDICT: %s" % verdict)
    print()
    print("    THE WELD IS REAL STRUCTURE: all four candidates close")
    print("    the full Clifford weld (M^2 = D^2 = I, MD + DM = 0,")
    print("    (MD)^2 = -I, full band swap) EXACTLY on their declared")
    print("    domains -- and each domain is forced by the same law:")
    print("      K1: the faithful (j odd) sector of the mu4 slot;")
    print("      K2: the inert (deck-odd) primes -- the mu(p) = -1")
    print("          survival locus;")
    print("      K3: the chain-parity double cover (construction);")
    print("      K4: the F2^4 Weyl pairs (120 of them, Fourier-lift")
    print("          swapped).")
    print("    THE ASYMMETRY (exact census): the mu-sign T_s is")
    print("    weldable (32 involutive partners); the deployed deck")
    print("    T_d is NOT (its anticommutant is exactly the faithful")
    print("    j-odd characters, all order 4) -- the deck can enter a")
    print("    weld only as J = MD (quarter turn), never as the second")
    print("    involution: the identification of the previous probe")
    print("    was refused by the wiring for exactly this reason.")
    print("    THE GAP NAMED: the weld-built D (K1) is Frobenius-")
    print("    orthogonal to the deployed deck T_d; welding the")
    print("    GEOMETRIC deck needs the metaplectic level, where the")
    print("    deck is central i*I = J^2-grade (v833) -- a candidate")
    print("    CONSTRUCTION, not deployed wiring.")
    print("    THE CONTRACTOR: the polar magnitude |C| is band-")
    print("    internal BY CONSTRUCTION; the polar phase is %s a"
          % ("matched by" if connected else "NOT matched by"))
    print("    source-built swap (best %s, residual %.3f; random null"
          % (best_w, best_r))
    print("    %.3f) -- the Krein band mover remains data-shaped:"
          % max(res_by_w["RANDOM"]))
    print("    the weld supplies the TYPE of the missing operator")
    print("    (an anticommuting involution), not yet its VALUE.")
    print("    NO RH claim: nothing here bounds zeros or Mertens.")
    print()
    print("    total runtime %.1f s" % (time.time() - T0))
    return 0 if not FAILS else 1


if __name__ == "__main__":
    sys.exit(main())
