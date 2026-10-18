"""v686 -- PRIME.GEOMSOS.01: OFFENSIVE 3 -- the FIRST FEASIBILITY
STRIKE at the geometric positivity source -- the contract
"Q_a^W(v) = sum_j |l_{a,j}(v)|^2 from TFPT geometry, without zeta,
without zeros".  This module takes stock of the four demanded
ingredients (H, Phi, <,>, Tr), executes the first construction attempt
for each, and checks EVERY construct immediately against the user's
five kill criteria (quoted verbatim, German, in the G4 fence):

  K1: zeta als Determinante/Spektrum hineindefiniert
  K2: Metrik nachtraeglich passend gewaehlt
  K3: Spurformel nur fuer endlich viele Primzahlen
  K4: Positivitaet nur auf zertifizierten Fenstern
  K5: Polarisierungs-Beweis selbst RH-aequivalent

THE FOUR INGREDIENTS, what this module establishes:

G1 [Tr, the trace-formula ingredient -- STRONGEST EXISTING BLOCK]:
  the E8 shell counts r(2n) = 240 sigma_3(n) (v625: pure lattice-point
  counting through the glue decomposition (theta2^8+theta3^8+theta4^8)/2)
  DEFINE, through the Dirichlet log-derivative recursion
      a(n) log n = sum_{d|n} Lambda_L(d) a(n/d),   a(n) = r(2n)/240,
  a von Mangoldt analogue Lambda_L with NO zeta input; the identity
  Lambda_L(n) = Lambda(n)(1+n^3) then gives the CIRCLE-FREE
  reconstruction
      Lambda_geo(n) := Lambda_L(n) / (1 + n^3)  ==  Lambda(n)  EXACTLY,
  where the normalizer 1+n^3 is itself lattice data: the Satake pair
  {1, p^3} of the p-local Hecke polynomial X^2 - a(p) X + p^3 built
  from the SHELL COUNT a(p) = r(2p)/240 (and the weight constant
  p^{k-1} = p^3 from the rank-8 = weight-4 bookkeeping), with
  1 + n^3 = alpha^k + beta^k for n = p^k.  The TFPT atom layer
  Lambda(n)/sqrt(n) at u = log n is the s = 1/2 weight map applied to
  the shell data: Lambda_L(n)/sqrt(n) = Lambda(n)/sqrt(n) (the Re=1/2
  line) + Lambda(n) n^{5/2} (the shifted Re=7/2 line); the projection
  is the Hecke normalization.  zeta appears ONLY as verification
  target (Dirichlet locks), never in the construction: K1 passes.
  K3 typing: the machine certificate is finite (n <= 512 by unique
  recursion at 30 digits), the identity itself is Hecke's theorem
  (dim M_4(SL2(Z)) = 1, complete Euler product) -- typed honestly.
  Residue bookkeeping (v673/li_e4): Res_{s=4} Lambda(E_4,s) = 1/240
  EXACTLY -- the shell normalizer IS the completed-form residue.

G2 [<,>, the polarization ingredient]: the cover carries J = -h per
  character (v613: Hodge-Riemann, h explicit Gamma monomials,
  signature (2,1), J signature (1,2)), and the v624 Lorentz congruence
  P^T J_det P = J_fix (exact, index 6) identifies the cover
  polarization lattice with the prime-front determinant form.  WHAT
  the Hodge positivity actually makes positive: the rank-3 Hermitian
  form on H^1(cover) -- per character line, in the CANONICAL period
  eigenframe (K2 passes there: the frame is computed from period
  integrals, not chosen).  THE GAP, measured: the window form lives on
  the odd hat sector (this module's miniature: h = 23 odd modes -> 276
  independent quadratic-form entries); what is certified on the window
  side today is TWO scalars per window (det S > 0 + one sheet sign,
  v627, 67 windows).  The missing functor Phi is named as a precise
  construction task (window vectors as sections of a rank-3 bundle
  over a modular base, image in the positive sheet, base integration
  load-bearing -- a rank-3 fiber alone cannot carry the form: the
  top-3 eigenvalue mass fraction of the miniature form is measured).

G3 [Frobenius candidate]: the Hecke operators T_p ARE the natural
  Frobenius analogues: commuting channels, Theta_E8 simultaneous
  eigenvector, eigenvalue 1 + p^3 = a(p) = r(2p)/240 -- the eigenvalue
  IS a normalized shell COUNT, so eigenvalue positivity is a zeta-free
  lattice-counting fact (all p, via sigma_3(p) > 0).  HOW FAR it
  carries: the space on which the T_p act diagonally is
  M_4(SL2(Z)) = C E_4 (dim 1) -- the window form (dim ~M) does not
  live there; no lag-lattice shift realizes T_p on the window space
  (log p / D incommensurable, 2^k != 3^m census); and pointwise
  positivity of the prime weights does NOT make the atom layer PSD
  (min eig of the atom-only odd form is measured NEGATIVE): the SOS
  is an interference statement between layers (Bochner positive-
  definiteness), not a per-prime sum -- exactly the K5 boundary.

W [the miniature window form -- the honest state of the art]: a
  self-contained Weil/window quadratic form is built end to end from
  (i) the G1-reconstructed Lambda_geo atoms (E8 lattice data), (ii)
  the closed archimedean screw layers (Suzuki's true g, v643
  formulas: pole block -4(e^{t/2}+e^{-t/2}-2), smooth layer with
  Lerch, density rho(t) = e^{-t/2}/(1-e^{-2t})), assembled as the
  hat-Galerkin matrix B(d) = poleK(d) - <W, K_d> (v643 THEOREM (iii)
  route, closed/quadrature layers), and VALIDATED against the zero
  comb: Q_gal(V) = 2 sum_{gamma>0} |Phi_V^hat(gamma)|^2 on the shared
  2000-zero cache (the Weil explicit formula on the window).  This
  demonstrates LITERALLY: the only SOS decomposition available today
  has l_j(v) = Phi_v^hat(gamma_j) -- ZERO EVALUATIONS (K1/K5 as
  construction; allowed here as verification), and the positivity
  certificate is comb + window (K4 fires on the current state, typed
  honestly).  The contract's entire content is replacing these l_j by
  geometric functionals.

Verdict enums (frozen; the EXPECTED verdict of this module is
GEOMSOS-TRACE-EXACT-TRANSPORT-OPEN -- Tr exact and circle-free, the
transport Phi missing, K4 firing honestly):
GEOMSOS-TRACE-EXACT-TRANSPORT-OPEN (all
structural identities pass; gaps typed), GEOMSOS-STRUCTURE-FAILS (a
structural identity fails), MIXED.

FIREWALL: standalone (NO cross-module import; the v625 theta glue, the
v643 screw layers and the v624/v613 matrices are re-implemented /
hard-coded inline with provenance); zero data = the shared zetazero
cache (declared, dps 15), used ONLY as verification target; finite
statements only; NO RH claim; no marker moves.

PROVENANCE: discovery probe geometric_sos_probe.py (2026-08-03, 19/19
PASS, verdict GEOMSOS-TRACE-EXACT-TRANSPORT-OPEN);
v625_prime_shadow (Theta_E8 = E_4, Hecke channels),
v673_li_e4 / li_e4_probe (Lambda_L recursion, +-1/240 residues),
v643_w1_theorem (Weil measure, screw layers, Galerkin dictionary),
v613_canonical_periods (J = -h, Gamma monomials),
v624_external_lattice_audit (Lorentz congruence P),
v627_hodge_chamber (positive cone, one sheet, 67 windows).
Python-only (numpy + sympy + mpmath), counted per GATE.WOLFRAM.02.
"""
import json
import math
import os
import time

import numpy as np
import sympy as sp
from mpmath import mp, mpf

T0 = time.time()
FAILS = []
N_CHK = 0

HERE = os.path.dirname(os.path.abspath(__file__))
# shared zero-comb cache: lives in experiments/tfpt-discovery/ (repo
# tree); fall back to a local copy next to this module (website mirror
# / standalone use).
_REPO_CACHE = os.path.join(os.path.dirname(HERE), "experiments",
                           "tfpt-discovery",
                           "zero_comb_cache_n2000.json")
_LOCAL_CACHE = os.path.join(HERE, "zero_comb_cache_n2000.json")
CACHE = _REPO_CACHE if os.path.exists(_REPO_CACHE) else _LOCAL_CACHE

# ---------------- declared constants (before any number) ----------------
NMAX_Q = 1024             # theta glue checked to q^1024 (shells n <= 512)
N_REC = 512               # exact-recursion horizon (30 digits)
DPS_REC = 30              # recursion precision
DPS_WIN = 30              # window-layer quadrature precision
TOL_REC = 1e-20           # Lambda_L vs Lambda(n)(1+n^3), relative
TOL_SPLIT = 1e-25         # two-line split identity, relative
TAIL_FACTOR = 3.0         # Dirichlet locks: |abs dev| < factor * tail
TOL_POLE = 1e-20          # closed poleK vs heavy route, relative
TOL_ATOM = 1e-8           # closed atom read vs kink-split, relative
TOL_ZERO = 1e-3           # miniature form vs zero comb, |ratio-1|
N_ZEROS = 2000            # shared comb cache
DPS_ZEROS = 15
D_WIN = 0.13              # miniature window lattice spacing
M_WIN = 46                # hats (odd sector h = 23)
SEED = 20260803
N_RAND = 4                # random odd test vectors (+ 4 sine modes)
EIG_FLOOR = 1e-10         # numeric floor for the PD statement
HECKE_PS = (2, 3, 5, 7, 11, 13)
RANK_TOL = 1e-10          # relative eigenvalue floor for rank counts


def check(name, ok, detail=""):
    global N_CHK
    N_CHK += 1
    if not ok:
        FAILS.append(name.split()[0])
    print("[%s] %s%s" % ("PASS" if ok else "FAIL", name,
                         (": " + detail) if detail else ""))


# ---------------- v625-style theta glue, re-implemented inline ----------
# (exact int64 convolution: all coefficients and pair products stay far
# below 2**62 at NMAX_Q = 1024 -- guarded by the assert in power8)
def theta_shells(nmax_q):
    def conv(a, b):
        out = np.convolve(a, b)[:nmax_q + 1]
        assert int(np.max(np.abs(out))) < 2 ** 62
        return out

    def power8(a):
        s2 = conv(a, a)
        s4 = conv(s2, s2)
        return conv(s4, s4)

    th3 = np.zeros(nmax_q + 1, dtype=np.int64)
    th3[0] = 1
    th4 = np.zeros(nmax_q + 1, dtype=np.int64)
    th4[0] = 1
    k = 1
    while k * k <= nmax_q:
        th3[k * k] = 2
        th4[k * k] = 2 * (-1) ** k
        k += 1
    t2o = np.zeros(nmax_q + 1, dtype=np.int64)
    k = 0
    while k * (k + 1) <= nmax_q:
        t2o[k * (k + 1)] = 1
        k += 1
    th2_8 = np.zeros(nmax_q + 1, dtype=np.int64)
    th2_8[2:] = 256 * power8(t2o)[:nmax_q - 1]
    tot = power8(th3) + power8(th4) + th2_8
    assert all(int(c) % 2 == 0 for c in tot)
    return [int(c) // 2 for c in tot]


def odd_toeplitz(c, M):
    """v563-verbatim odd-sector projection of a Toeplitz lag form."""
    h = M // 2
    rr = np.arange(h)
    return (np.asarray(c)[np.abs(rr[:, None] - rr[None, :])]
            - np.asarray(c)[(M - 1) - rr[:, None] - rr[None, :]])


def run():
    global N_CHK, FAILS
    N_CHK = 0
    FAILS = []
    print("=" * 78)
    print("GEOMETRIC SOS -- feasibility strike for PRIME.GEOMSOS.01")
    print("(H, Phi, <,>, Tr) inventory + first construction, K1..K5-audited")
    print("=" * 78)

    # ============================================================== G0
    print("\nG0 -- the lattice counting data (zeta-free input)")
    t_g0 = time.time()
    TE8 = theta_shells(NMAX_Q)
    sig3 = [0] + [int(sum(d ** 3 for d in sp.divisors(n)))
                  for n in range(1, N_REC + 1)]
    glue_ok = (TE8[0] == 1
               and all(TE8[m] == 0 for m in range(1, NMAX_Q + 1, 2))
               and all(TE8[2 * n] == 240 * sig3[n]
                       for n in range(1, N_REC + 1)))
    print("   theta glue to q^%d in %.1f s" % (NMAX_Q, time.time() - t_g0))
    check("G0.1 [E] the E8 glue (theta2^8 + theta3^8 + theta4^8)/2 has "
          "shell counts r(2n) = 240 sigma_3(n) for n = 1..%d EXACTLY "
          "(first shells %s; odd norms empty): the counting input of "
          "everything below is PURE lattice geometry -- integer "
          "convolution of the glue decomposition, no zeta anywhere"
          % (N_REC, [TE8[2], TE8[4], TE8[6]]), glue_ok)

    # ============================================================== G1
    print("\nG1 -- Tr: the trace-formula ingredient (circle-free "
          "von Mangoldt from shells)")
    mp.dps = DPS_REC
    a_norm = {n: sp.Integer(TE8[2 * n]) / 240 for n in range(1, N_REC + 1)}
    assert all(a_norm[n] == sig3[n] for n in range(1, N_REC + 1))

    # the recursion DEFINES Lambda_L from counting data (no zeta)
    t_rec = time.time()
    lamL = {1: mpf(0)}
    for n in range(2, N_REC + 1):
        acc = mpf(sig3[n]) * mp.log(n)
        for d in sp.divisors(n):
            if 1 < d < n:
                acc -= lamL[d] * sig3[n // d]
        lamL[n] = acc
    print("   recursion to n = %d at %d digits in %.1f s"
          % (N_REC, DPS_REC, time.time() - t_rec))

    # reference von Mangoldt (sympy factorization, verification only)
    lam_ref = {}
    for n in range(2, N_REC + 1):
        fac = sp.factorint(n)
        lam_ref[n] = (mp.log(list(fac)[0]) if len(fac) == 1 else mpf(0))

    worst_rec = mpf(0)
    for n in range(2, N_REC + 1):
        tgt = lam_ref[n] * (1 + mpf(n) ** 3)
        dev = (abs(lamL[n] - tgt) / abs(tgt) if tgt != 0
               else abs(lamL[n]) / (mp.log(n) * (1 + mpf(n) ** 3)))
        worst_rec = max(worst_rec, dev)
    check("G1.1 [E] the Dirichlet log-derivative recursion a(n) log n = "
          "sum_{d|n} Lambda_L(d) a(n/d) on a(n) = r(2n)/240 yields "
          "Lambda_L(n) = Lambda(n)(1 + n^3) for n = 2..%d (worst rel dev "
          "%s < %.0e): the von-Mangoldt-type data is DEFINED by lattice "
          "counting alone -- the recursion is the trace-formula-side "
          "identity, zeta-free by construction"
          % (N_REC, mp.nstr(worst_rec, 3), TOL_REC), worst_rec < TOL_REC)

    # the circle-free normalizer: Satake pair from shell counts
    X = sp.symbols("X")
    satake_ok = True
    for p in (2, 3, 5, 7):
        ap = int(a_norm[p])                      # = r(2p)/240, a COUNT
        roots = sp.roots(X ** 2 - ap * X + p ** 3, X)
        satake_ok &= (set(roots) == {sp.Integer(1), sp.Integer(p) ** 3})
        kmax = int(math.log(N_REC) / math.log(p))
        for k in range(1, kmax + 1):
            n = p ** k
            satake_ok &= (1 + n ** 3 == 1 ** k + (p ** 3) ** k)
        for k in range(1, kmax):                  # weight-4 Hecke recursion
            lhs = sig3[p ** (k + 1)]
            rhs = ap * sig3[p ** k] - p ** 3 * sig3[p ** (k - 1)]
            satake_ok &= (lhs == rhs)
    lam_geo = {n: lamL[n] / (1 + mpf(n) ** 3) for n in range(2, N_REC + 1)}
    worst_geo = mpf(0)
    for n in range(2, N_REC + 1):
        if lam_ref[n] != 0:
            worst_geo = max(worst_geo,
                            abs(lam_geo[n] - lam_ref[n]) / lam_ref[n])
        else:
            worst_geo = max(worst_geo, abs(lam_geo[n]) / mp.log(n))
    check("G1.2 [E] THE CIRCLE-FREE RECONSTRUCTION: Lambda_geo(n) := "
          "Lambda_L(n)/(1 + n^3) == Lambda(n) EXACTLY for n = 2..%d "
          "(worst rel dev %s; non-prime-powers vanish), and the "
          "normalizer is itself lattice data: the p-local polynomial "
          "X^2 - a(p) X + p^3 with the COUNT a(p) = r(2p)/240 has Satake "
          "roots {1, p^3} exactly, 1 + n^3 = alpha^k + beta^k for "
          "n = p^k, and the weight-4 Hecke recursion a(p^{k+1}) = "
          "a(p) a(p^k) - p^3 a(p^{k-1}) holds on the raw counts "
          "(census p = 2, 3, 5, 7 to n <= %d): the prime weights of the "
          "Weil form are reconstructible from E8 counting alone"
          % (N_REC, mp.nstr(worst_geo, 3), N_REC),
          satake_ok and worst_geo < TOL_REC)

    # the s = 1/2 weight map and the two-line split
    worst_split = mpf(0)
    for n in range(2, N_REC + 1):
        lhs = lamL[n] / mp.sqrt(n)
        rhs = lam_geo[n] / mp.sqrt(n) + lam_geo[n] * mpf(n) ** mpf("2.5")
        den = abs(lhs) if lhs != 0 else mpf(1)
        worst_split = max(worst_split, abs(lhs - rhs) / den)
    res4 = sp.gamma(4) * sp.zeta(4) / (2 * sp.pi) ** 4
    check("G1.3 [E] THE s = 1/2 WEIGHT MAP: Lambda_L(n)/sqrt(n) = "
          "Lambda(n)/sqrt(n) + Lambda(n) n^{5/2} EXACTLY (worst rel "
          "dev %s): the shell data at the s = 1/2 evaluation contains "
          "the TFPT atom layer (Re = 1/2 line) PLUS the shifted line "
          "(Re = 7/2); the projection onto the atom layer IS the Hecke "
          "normalization 1/(1+n^3).  Honest typing: sum Lambda(n) "
          "n^{-1/2} diverges -- s = 1/2 is a TERMWISE weight map (the "
          "atom masses at u = log n), not a convergent evaluation, and "
          "the exponent 1/2 is the unitary FE normalization (declared "
          "bookkeeping, not a lattice output).  Residue lock (v673): "
          "Res_{s=4} (2pi)^{-s} Gamma(s) zeta(s) zeta(s-3) = %s = 1/240 "
          "exactly -- the shell normalizer IS the completed-form residue"
          % (mp.nstr(worst_split, 3), res4),
          worst_split < TOL_SPLIT and res4 == sp.Rational(1, 240))

    # Dirichlet locks -- zeta ONLY as verification target
    mp.dps = DPS_REC
    S6 = mp.fsum(lam_geo[n] / mpf(n) ** 6 for n in range(2, N_REC + 1))
    S3 = mp.fsum(lam_geo[n] / mpf(n) ** 3 for n in range(2, N_REC + 1))
    tgt6 = -mp.zeta(6, derivative=1) / mp.zeta(6)
    tgt3 = -mp.zeta(3, derivative=1) / mp.zeta(3)
    dev6 = abs(S6 - tgt6)
    dev3 = abs(S3 - tgt3)
    tail6 = mpf(N_REC) ** -5 / 5       # ~ int_N x^-s dpsi = N^{1-s}/(s-1)
    tail3 = mpf(N_REC) ** -2 / 2
    check("G1.4 [E-float] Dirichlet locks from RECURSION-ONLY data: "
          "sum_{n<=%d} Lambda_geo(n) n^-6 vs -(zeta'/zeta)(6): abs dev "
          "%s (PNT tail budget ~%s); n^-3 vs -(zeta'/zeta)(3): abs dev "
          "%s (budget ~%s); both within %.0fx of the truncation tail -- "
          "zeta enters ONLY as the verification target of the "
          "lattice-defined data, never as input (K1)"
          % (N_REC, mp.nstr(dev6, 3), mp.nstr(tail6, 2),
             mp.nstr(dev3, 3), mp.nstr(tail3, 2), TAIL_FACTOR),
          dev6 < TAIL_FACTOR * tail6 and dev3 < TAIL_FACTOR * tail3)

    check("G1.5 [C] K1/K3 AUDIT of the Tr ingredient: construction chain "
          "= glue convolution (integers) -> recursion -> Satake "
          "normalization from counts -> termwise s = 1/2 weight; no "
          "zeta, no zeros, no primes as input (K1 PASSES; the prime "
          "NOTION enters only through unique factorization of the "
          "address space, v625 P2).  K3: the machine certificate is "
          "FINITE (n <= %d); the identity Lambda_L = Lambda (1+n^3) is "
          "Hecke's theorem for ALL n (E_4 spans M_4, complete Euler "
          "product) -- the construction is not truncated, only this "
          "module's certificate is; typed, not hidden" % N_REC, True)

    # ============================================================== G2
    print("\nG2 -- <,>: the polarization ingredient (Hodge cover, "
          "Lorentz congruence, the gap)")
    P = sp.Matrix([[3, 0, 0], [3, 0, 2], [-1, 1, -1]])
    Jfix = sp.Matrix([[16, 2, 4], [2, -2, 2], [4, 2, -2]])
    Jdet = sp.Matrix([[0, 1, 0], [1, 0, 0], [0, 0, -2]])
    cong = sp.simplify(P.T * Jdet * P - Jfix) == sp.zeros(3, 3)
    sig_det = np.sign(np.linalg.eigvalsh(
        np.array(Jdet.tolist(), dtype=float)))
    sig_fix = np.sign(np.linalg.eigvalsh(
        np.array(Jfix.tolist(), dtype=float)))
    check("G2.1 [E] the v624 Lorentz congruence re-verified standalone: "
          "P^T J_det P = J_fix EXACTLY (integer), det J_det = %s, "
          "det J_fix = %s = (det P)^2 * 2 with det P = %s (index 6); "
          "signatures J_det %s, J_fix %s: the prime-front determinant "
          "form and the cover polarization lattice are the SAME rational "
          "Lorentz form (1,2)"
          % (Jdet.det(), Jfix.det(), P.det(),
             tuple(int(s) for s in sig_det),
             tuple(int(s) for s in sig_fix)),
          cong and Jdet.det() == 2 and Jfix.det() == 72
          and P.det() == -6
          and int(np.sum(sig_det > 0)) == 1 and int(np.sum(sig_fix > 0)) == 1)

    # the compiler polarization J (v613, hard-coded with provenance)
    s3 = math.sqrt(3.0)
    Jc = np.array([[0, 1 + s3 * 1j, -1 + s3 * 1j],
                   [1 - s3 * 1j, 2, 1 + s3 * 1j],
                   [-1 - s3 * 1j, 1 - s3 * 1j, 0]], dtype=complex)
    evJ = np.linalg.eigvalsh(Jc)
    mp.dps = DPS_WIN
    g = mp.gamma
    h0 = (mpf(3) / 4 * mp.pi * g(mpf(1) / 4) * g(mpf(1) / 3)
          * g(mpf(5) / 12) / (g(mpf(3) / 4) * g(mpf(2) / 3)
                              * g(mpf(7) / 12)))
    h1 = (3 * mp.sqrt(3) / (16 * mp.pi) * g(mpf(1) / 3) ** 2
          * g(mpf(1) / 6) ** 2)
    h2 = (mpf(3) / 4 * mp.pi * g(mpf(1) / 4) * g(mpf(2) / 3)
          * g(mpf(1) / 12) / (g(mpf(3) / 4) * g(mpf(1) / 3)
                              * g(mpf(11) / 12)))
    check("G2.2 [E] WHAT the Hodge positivity actually makes positive: "
          "the rank-3 Hermitian form on H^1(cover), per character line, "
          "in the CANONICAL period eigenframe -- the compiler "
          "polarization J (v613 matrix) is Hermitian with eigenvalues "
          "%s: signature (1,2), i.e. J = -h with h of Hodge signature "
          "(2,1) (v613 [E]: sign bridge per character, unique negative "
          "h-line = unique positive J-line = zeta_12 / antihol); the "
          "Hodge weights are explicit Gamma monomials |h| = (%s, %s, %s) "
          "-- so on dim 3 the SOS EXISTS CANONICALLY: J = +|l_1|^2 - "
          "|l_2|^2 - |l_3|^2 with l_i from PERIOD ROWS, nothing chosen "
          "(K2 passes on the cover)"
          % (["%.4f" % e for e in evJ], mp.nstr(h0, 8), mp.nstr(h1, 8),
             mp.nstr(h2, 8)),
          int(np.sum(evJ > 0)) == 1 and int(np.sum(evJ < 0)) == 2
          and h0 > 0 and h1 > 0 and h2 > 0)

    h_odd = M_WIN // 2
    n_entries = h_odd * (h_odd + 1) // 2
    n_cert = 2
    check("G2.3 [C, THE GAP -- honest] cover positivity lives on dim 3; "
          "the window form lives on the odd hat sector (miniature below: "
          "h = %d modes -> %d independent quadratic-form entries; v563 "
          "windows are larger).  Certified on the window side today: %d "
          "scalars per window (det S > 0 + one sheet sign; v627, 67 "
          "windows) = %.2f%% of ONE miniature form.  THE MISSING FUNCTOR "
          "Phi, named as construction task: a linear map from the odd "
          "H^1_0 window sector into SECTIONS of a rank-3 bundle over a "
          "modular base with (i) fiber metric J (the v613 form, frozen), "
          "(ii) image in the POSITIVE sheet (the v627 chamber), (iii) "
          "Q_a^W(v) = integral_base <Phi v, Phi v>_J -- the base "
          "integration is forced: a rank-3 fiber alone cannot carry a "
          "rank-%d form (K2 checkpoint: the base measure must be "
          "DERIVED, not fitted)"
          % (h_odd, n_entries, n_cert, 100.0 * n_cert / n_entries, h_odd),
          n_entries == 276)

    # ============================================================== G3
    print("\nG3 -- Frobenius: the Hecke channels and how far their "
          "positivity carries")
    a_int = {n: (1 if n == 0 else 240 * sig3[n]) for n in range(N_REC + 1)}

    def Tp_arr(arr, p, nmax, k=4):
        out = {}
        for n in range(nmax + 1):
            if n == 0:
                out[n] = arr[0] + p ** (k - 1) * arr[0]
            else:
                out[n] = arr[p * n] + (p ** (k - 1) * arr[n // p]
                                       if n % p == 0 else 0)
        return out

    eig_ok = True
    for p in HECKE_PS:
        Ta = Tp_arr(a_int, p, N_REC // p)
        eig_ok &= all(Ta[n] == (1 + p ** 3) * a_int[n]
                      for n in range(N_REC // p + 1))
        eig_ok &= (1 + p ** 3 == TE8[2 * p] // 240)   # eigenvalue = COUNT
    comm_ok = True
    for (p, q) in ((2, 3), (2, 5), (3, 5)):
        nmax = N_REC // (p * q)
        Tq = Tp_arr(a_int, q, N_REC // q)
        Tp_ = Tp_arr(a_int, p, N_REC // p)
        comm_ok &= all(Tp_arr(Tq, p, nmax)[n] == Tp_arr(Tp_, q, nmax)[n]
                       for n in range(nmax + 1))
    check("G3.1 [E] the Frobenius candidates: T_p Theta_E8 = (1 + p^3) "
          "Theta_E8 for p = %s (n <= %d/p), [T_p, T_q] = 0 for (2,3), "
          "(2,5), (3,5), and the eigenvalue IS a count: 1 + p^3 = "
          "r(2p)/240 = sigma_3(p) -- POSITIVITY OF ALL HECKE EIGENVALUES "
          "IS A LATTICE-COUNTING FACT (zeta-free, all p: sigma_3(p) "
          "counts vectors)" % (list(HECKE_PS), N_REC),
          eig_ok and comm_ok)

    def dimMk(k):
        if k < 0 or k % 2:
            return 0
        return k // 12 + (0 if k % 12 == 2 else 1)

    check("G3.2 [C, honest] the space the T_p act on diagonally is "
          "dim M_4(SL2(Z)) = %d (classical dimension formula; controls: "
          "dim M_12 = %d, dim M_2 = %d): Theta_E8 = E_4 SPANS it -- "
          "diagonal positivity is real but lives on a ONE-dimensional "
          "space; the window form (dim %d in the miniature) does not "
          "live there.  A window-side T_p would have to be: self-adjoint "
          "for Q, commuting, with p-local spectral data -- it DOES NOT "
          "EXIST in the corpus (named task M1 of the contract)"
          % (dimMk(4), dimMk(12), dimMk(2), h_odd),
          dimMk(4) == 1 and dimMk(12) == 2 and dimMk(2) == 0)

    pow_ok = all(2 ** k != 3 ** m
                 for k in range(1, 41) for m in range(1, 41))
    fracs = [math.log(p) / D_WIN % 1.0 for p in (2, 3, 5, 7)]
    check("G3.3 [E] NO lag-lattice shift realizes T_p on the window "
          "space: frac(log p / D) = %s for p = 2, 3, 5, 7 (D = %.2f) -- "
          "no shift by an integer number of cells; and no D fixes it "
          "for two primes at once: 2^k != 3^m for all k, m <= 40 "
          "(exact integers), i.e. log 2 / log 3 is not rational at this "
          "census depth -- the Frobenius action on windows needs the "
          "CONTINUUM object (dilation u -> u + log p on the measure), "
          "not the lattice"
          % (["%.3f" % f for f in fracs], D_WIN), pow_ok
          and all(1e-6 < f < 1 - 1e-6 for f in fracs))

    # ============================================================== W
    print("\nW -- the miniature window form: E8 atoms + closed screw "
          "layers, validated against the zero comb")
    mp.dps = DPS_WIN
    Dm = mpf(repr(D_WIN))
    Xp = mp.e ** (Dm / 2) + mp.e ** (-Dm / 2) - 2

    # ---- atoms from the G1 reconstruction (floats for the assembly)
    atoms = [(math.log(n), float(lam_geo[n] / mp.sqrt(n)))
             for n in range(2, N_REC + 1) if lam_ref[n] != 0]
    uu = np.array([u for u, _ in atoms])
    ww = np.array([w for _, w in atoms])
    print("   atoms: %d prime powers n <= %d from Lambda_geo "
          "(E8 recursion), u_max = %.4f, form reach (M+1)D = %.4f"
          % (len(atoms), N_REC, uu[-1], (M_WIN + 1) * D_WIN))

    # ---- pole layer: closed poleK vs heavy double-integral route
    def g_pole_mp(tv):
        tv = abs(tv)
        return -4 * (mp.e ** (tv / 2) + mp.e ** (-tv / 2) - 2)

    def II_layer(k, gfun):
        return mp.quad(lambda s: gfun(abs(k * Dm + s)) * (Dm - abs(s)),
                       [-Dm, 0, Dm])

    def poleK(d):
        return 32 * mp.cosh(d * Dm / 2) * Xp ** 2 / Dm ** 2

    dev_pole = mpf(0)
    for d in (0, 1, 5):
        IIm = II_layer(d - 1, g_pole_mp) if d >= 1 else II_layer(1, g_pole_mp)
        heavy = (2 * II_layer(d, g_pole_mp) - IIm
                 - II_layer(d + 1, g_pole_mp)) / Dm ** 2
        dev_pole = max(dev_pole, abs(heavy - poleK(d)) / abs(poleK(d)))
    check("W1.1 [E] the pole block is CLOSED: the hat-Galerkin read of "
          "g_pole = -4(e^{t/2} + e^{-t/2} - 2) equals poleK(d) = "
          "32 cosh(dD/2) X^2/D^2, X = e^{D/2}+e^{-D/2}-2, at d = 0, 1, 5 "
          "(worst rel dev %s < %.0e) -- the zeta-pole layer (s = 0, 1) "
          "is finite-rank bookkeeping, not a leak"
          % (mp.nstr(dev_pole, 3), TOL_POLE), dev_pole < TOL_POLE)

    # ---- smooth layer (Suzuki true g, v643 formulas)
    LLm = mp.log(mp.pi) - mp.digamma(mpf(1) / 4)
    PHI1 = mp.lerchphi(1, 2, mpf(1) / 4)

    def g_sm_mp(tv):
        tv = mpf(tv)
        if tv == 0:
            return mpf(0)
        return (LLm * tv / 2 - PHI1 / 4
                + mp.e ** (-tv / 2)
                * mp.lerchphi(mp.e ** (-2 * tv), 2, mpf(1) / 4) / 4)

    def rho_mp(x):
        return mp.e ** (-x / 2) / (-mp.expm1(-2 * x))

    def K_mp(x):
        u = abs(x) / Dm
        if u >= 2:
            return mpf(0)
        if u <= 1:
            return Dm * (mpf(2) / 3 - u ** 2 + u ** 3 / 2)
        return Dm * (2 - u) ** 3 / 6

    t_sm = time.time()
    II_b = {k: II_layer(k, g_sm_mp) for k in range(4)}

    def cgal_sm(d):
        if d <= 2:
            return (2 * II_b[d] - II_b[abs(d - 1)] - II_b[d + 1]) / Dm ** 2
        return -mp.quad(lambda x: rho_mp(x) * K_mp(x - d * Dm),
                        [(d + j) * Dm for j in (-2, -1, 0, 1, 2)])

    c_sm = np.array([float(cgal_sm(d)) for d in range(M_WIN)])
    print("   smooth layer: %d lags (d <= 2 exact double route, d >= 3 "
          "density read) in %.1f s" % (M_WIN, time.time() - t_sm))

    # ---- atom layer: closed B-spline read vs exact kink-split route
    def K_f(x):
        u = np.abs(x) / D_WIN
        return np.where(u <= 1.0,
                        D_WIN * (2.0 / 3.0 - u ** 2 + u ** 3 / 2.0),
                        np.where(u < 2.0, D_WIN * (2.0 - u) ** 3 / 6.0,
                                 0.0))

    dd_grid = np.arange(M_WIN) * D_WIN
    c_at = np.zeros(M_WIN)
    for u_j, w_j in atoms:
        c_at -= w_j * (K_f(u_j - dd_grid) + K_f(u_j + dd_grid))

    cw_pref = np.cumsum(ww)
    cs_pref = np.cumsum(ww * uu)

    def g_prime_f(tv):
        tv = abs(float(tv))
        k = int(np.searchsorted(uu, tv, side="right"))
        if k == 0:
            return 0.0
        return tv * float(cw_pref[k - 1]) - float(cs_pref[k - 1])

    def II_prime(k):
        pts = [-D_WIN, 0.0, D_WIN]
        for u_j in uu:
            sk = u_j - k * D_WIN
            if -D_WIN < sk < D_WIN:
                pts.append(float(sk))
        return mp.quad(lambda s: g_prime_f(k * D_WIN + float(s))
                       * (D_WIN - abs(float(s))), sorted(pts))

    dev_at = 0.0
    for d in (20, 40):
        heavy = float((2 * II_prime(d) - II_prime(d - 1)
                       - II_prime(d + 1)) / D_WIN ** 2)
        dev_at = max(dev_at, abs(heavy - c_at[d]) / abs(heavy))
    check("W1.2 [E] the atom layer is CLOSED: the B-spline read "
          "c_at(d) = -sum_n w_n [K(u_n - dD) + K(u_n + dD)] with the E8 "
          "weights w_n = Lambda_geo(n)/sqrt(n) equals the exact "
          "kink-split Galerkin route at d = 20, 40 (worst rel dev "
          "%.1e < %.0e): the prime side of the window form is assembled "
          "ENTIRELY from lattice-reconstructed data" % (dev_at, TOL_ATOM),
          dev_at < TOL_ATOM)

    # ---- the full miniature form and the zero-comb identity
    c_pole = np.array([float(poleK(d)) for d in range(M_WIN)])
    B_lags = c_pole + c_sm + c_at
    T_full = B_lags[np.abs(np.arange(M_WIN)[:, None]
                           - np.arange(M_WIN)[None, :])]
    A_odd = odd_toeplitz(B_lags, M_WIN)
    A_pole = odd_toeplitz(c_pole, M_WIN)
    A_sm = odd_toeplitz(c_sm, M_WIN)
    A_at = odd_toeplitz(c_at, M_WIN)

    with open(CACHE, "r", encoding="utf-8") as fh:
        cache = json.load(fh)
    assert cache["n_zeros"] == N_ZEROS and cache["dps"] == DPS_ZEROS
    gam = np.array([float(x) for x in cache["gammas"]])
    pj = (np.arange(M_WIN) - (M_WIN - 1) / 2.0) * D_WIN
    hat_hat = D_WIN * (np.sin(gam * D_WIN / 2)
                       / (gam * D_WIN / 2)) ** 2
    E = np.exp(-1j * np.outer(gam, pj))          # 2000 x M

    rng = np.random.default_rng(SEED)
    vecs = []
    for k in range(1, 5):
        v = np.sin(np.pi * k * (np.arange(h_odd) + 1.0) / (h_odd + 1))
        vecs.append(("sine-%d" % k, v / np.linalg.norm(v)))
    for r in range(N_RAND):
        v = rng.standard_normal(h_odd) / (1.0 + np.arange(h_odd))
        vecs.append(("rand-%d" % (r + 1), v / np.linalg.norm(v)))

    dens_tail = 2 * 16 / D_WIN ** 2 * float(mp.quad(
        lambda t: (mp.log(t / (2 * mp.pi)) / (2 * mp.pi)) / t ** 4,
        [float(gam[-1]), mp.inf]))
    rows = []
    worst_ratio = 0.0
    worst_pair = 0.0
    for lab, v in vecs:
        V = np.concatenate([v, -v[::-1]])
        q_gal = float(V @ (T_full @ V))
        q_odd = 2.0 * float(v @ (A_odd @ v))
        worst_pair = max(worst_pair, abs(q_gal - q_odd) / abs(q_gal))
        phi_hat = hat_hat * (E @ V)
        q_zero = 2.0 * float(np.sum(np.abs(phi_hat) ** 2))
        tail_b = dens_tail * float(np.sum(np.abs(V))) ** 2
        rows.append((lab, q_gal, q_zero, q_gal / q_zero - 1.0, tail_b))
        worst_ratio = max(worst_ratio, abs(q_gal / q_zero - 1.0))
    print("   vector     Q_galerkin      Q_zerocomb      ratio-1"
          "    tail budget")
    for lab, qg, qz, r1, tb in rows:
        print("   %-8s  %14.10f  %14.10f  %9.2e  %8.1e"
              % (lab, qg, qz, r1, tb))
    check("W2.1 [E-float, CENTRAL] THE EXPLICIT FORMULA ON THE WINDOW: "
          "Q_gal(V) = V^T B V (pole + smooth + E8 atoms) equals "
          "2 sum_{gamma>0} |Phi_V^hat(gamma)|^2 over the %d-zero comb "
          "on all %d odd test vectors (worst |ratio-1| = %.2e < %.0e; "
          "truncation tail budgets printed; odd-projection consistency "
          "%.1e): the miniature IS the Weil form -- and its only "
          "available SOS has l_j(v) = Phi_v^hat(gamma_j), ZERO "
          "EVALUATIONS: using them as DEFINITION is exactly what K1/K5 "
          "forbid; the contract must replace them"
          % (N_ZEROS, len(vecs), worst_ratio, TOL_ZERO, worst_pair),
          worst_ratio < TOL_ZERO and worst_pair < 1e-10)

    evA = np.linalg.eigvalsh(A_odd)
    ev_at = np.linalg.eigvalsh(A_at)
    ev_sm = np.linalg.eigvalsh(A_sm)
    evP = np.linalg.eigvalsh(A_pole)
    rankP = int(np.sum(np.abs(evP) > RANK_TOL * np.max(np.abs(evP))))
    pos_mass = float(np.sum(evA[evA > 0]))
    top3 = float(np.sum(np.sort(evA)[-3:]))
    print("   full-form spectrum: 5 smallest eigenvalues %s, max %.4f"
          % (["%.3e" % e for e in evA[:5]], float(evA[-1])))
    check("W2.2 [MEASURED, honest] the positivity anatomy of the "
          "miniature: FULL form min eig = %.3e > %s = declared numeric "
          "floor (assembly layers exact/30-digit) -- positive-definite "
          "ON THIS WINDOW, certificate = the zero comb (K4 fires on "
          "the current state: window + comb, nothing more); ATOM layer "
          "alone min eig = %.4f < 0 (pointwise-positive lattice "
          "weights do NOT make the prime layer PSD: the needed notion "
          "is Bochner positive-definiteness of the full measure -- an "
          "interference statement between layers, the exact K5 "
          "boundary); smooth layer min eig = %.4f; pole block rank %d "
          "<= 2 (declared finite-rank freedom); TOP-3 EIGENVALUE MASS "
          "= %.1f%% of the positive mass: a rank-3 pointwise transport "
          "captures at most this -- the G2 base integration is "
          "load-bearing, quantified"
          % (float(evA[0]), EIG_FLOOR, float(ev_at[0]),
             float(ev_sm[0]), rankP, 100.0 * top3 / pos_mass),
          float(evA[0]) > EIG_FLOOR and float(ev_at[0]) < 0
          and rankP <= 2)

    # ============================================================== G4
    print("\nG4 -- the feasibility verdict and the contract fence")
    check("G4.1 [C] INGREDIENT INVENTORY (the four demanded pieces): "
          "Tr VORHANDEN [E] (G1: circle-free Lambda_geo from E8 "
          "counting; the strongest block); <,> VORHANDEN-AUF-DIM-3 [E] "
          "(G2: canonical SOS on H^1(cover) via the period eigenframe; "
          "Lorentz congruence to the prime front exact) -- transport to "
          "the window form FEHLT (named task, K2 checkpoint); H "
          "KONSTRUIERBAR-MIT-BENANNTER-AUFGABE (G3: the only existing "
          "T_p-diagonal space is dim 1; needed: a bundle over a modular "
          "base whose sections carry the windows); Phi FEHLT-FUNDAMENTAL "
          "(nothing in the corpus maps windows isometrically into "
          "geometric sections; W2.2 quantifies why rank 3 alone cannot)",
          True)
    check("G4.2 [C] KILL-CRITERIA AUDIT of everything built here: "
          "K1 PASS (G1 construction zeta-free; zeta/zeros only as "
          "verification targets, G1.4/W2.1); K2 PASS-SO-FAR (all forms "
          "frozen with provenance v613/v624, congruence exact-integer "
          "-- no fit freedom; the DANGER POINT is the future transport "
          "Phi and base measure, named); K3 TYPED (identity = Hecke "
          "theorem for all n, machine certificate finite n <= 512); "
          "K4 FIRES on the current positivity surface (min eig > 0 "
          "certified only on THIS window via the 2000-zero comb; v627: "
          "67 windows, 2 scalars each) -- the honest center of the "
          "whole feasibility question; K5 CHECKPOINT (Hodge-Riemann on "
          "the cover is an RH-independent theorem -- the transport "
          "proof must stay on that side; any step needing zero "
          "localization kills the route)", True)

    print("""
   ------------------------------------------------------------------
   VERTRAG (ENTWURF) PRIME.GEOMSOS.01 -- die geometrische
   Positivitaetsquelle (der 15%-Strom, TFPT-Moonshot)
   ------------------------------------------------------------------
   INPUT (vorhanden, maschinell):
     - E8-Schalenzaehlung r(2n) = 240 sigma_3(n) und die zirkelfreie
       Rekonstruktion Lambda_geo(n) = Lambda_L(n)/(1+n^3) [G1, E]
     - Hecke-Kanaele T_p, Eigenwert = Zaehldatum 1+p^3 = r(2p)/240,
       Satake {1, p^3} aus Zaehlung [G3, E]
     - Cover-Polarisierung J = -h (Hodge-Riemann, kanonischer
       Perioden-Eigenrahmen, dim 3) + Lorentz-Kongruenz
       P^T J_det P = J_fix (Index 6) [G2, E; v613/v624]
     - Weil-Mass W und Galerkin-Woerterbuch (v643-Schichten); die
       Fensterform ist auf dem Fenster positiv-definit, Zertifikat =
       Nullstellen-Kamm [W, E-float/MEASURED]
   OUTPUT (Ziel):
     Q_a^W(v) = sum_j |l_{a,j}(v)|^2 mit GEOMETRISCHEN Funktionalen
     l_{a,j} (Perioden-/Schnitt-Auswertungen), ohne zeta, ohne
     Nullstellen -- fuer ALLE Fenster a (nicht nur zertifizierte).
   MEILENSTEINE (benannte Aufgaben):
     M1: T_p-Aktion auf dem Fensterraum (Q-selbstadjungiert,
         kommutierend, p-lokal; das Kontinuum-Objekt u -> u + log p,
         nicht der Lag-Gitter-Shift [G3.3])
     M2: der Transport Phi: odd-H^1_0 -> Schnitte eines Rang-3-
         Buendels (Faser (H^1(Cover), J), Bild im positiven Blatt
         [v627]), Q = Basis-Integral der Fasernorm; erste Etappe:
         die 2x2-Frontmatrix-Reduktion y_h zur vollen 3x3-Faser
         erweitern (v624-Kongruenz als Faser-Identifikation)
     M3: das Basis-Mass DERIVIEREN (nicht waehlen -- K2); Kandidat:
         die Modulflaeche der v625-Kette (Theta/Hecke-Seite)
     M4: der Spur-Abgleich: Basis-Integral der Faser-Spuren ==
         G1-Zaehlformel (die (1+n^3)-Normierung als Faser-Gewicht)
   KILL-KRITERIEN (woertlich, User):
     K1 zeta als Determinante/Spektrum hineindefiniert
     K2 Metrik nachtraeglich passend gewaehlt
     K3 Spurformel nur fuer endlich viele Primzahlen
     K4 Positivitaet nur auf zertifizierten Fenstern
     K5 Polarisierungs-Beweis selbst RH-aequivalent
   EHRLICHE EINSCHAETZUNG (User-Fence, woertlich): der 15%-Strom;
   das wahrscheinlichste Ergebnis ist "jahrelang schoene Mathematik
   ohne RH-Beweis" -- dieser Vertrag produziert dann trotzdem
   Theoreme (G1 ist bereits eines auf Suite-Ebene).
   ------------------------------------------------------------------""")
    check("G4.3 [C] the contract draft PRIME.GEOMSOS.01 is printed with "
          "the user's kill criteria and probability fence VERBATIM; no "
          "marker moves, no ledger row, no paper edit from this module "
          "-- experiments-only", True)

    structural = [f for f in FAILS
                  if f in ("G0.1", "G1.1", "G1.2", "G1.3", "G1.4",
                           "G2.1", "G2.2", "G3.1", "W1.1", "W1.2",
                           "W2.1")]
    if not FAILS:
        VERDICT = "GEOMSOS-TRACE-EXACT-TRANSPORT-OPEN"
    elif structural:
        VERDICT = "GEOMSOS-STRUCTURE-FAILS"
    else:
        VERDICT = "MIXED"
    print("\nVERDICT: %s -- Tr exact and circle-free from E8 counting "
          "(Lambda_geo == Lambda, n <= %d); canonical dim-3 SOS on the "
          "cover; Hecke eigenvalue positivity = lattice counting; the "
          "miniature window form validated against the comb (worst "
          "|ratio-1| %.1e) and PD there; missing: H (bundle), Phi "
          "(transport) -- named as M1..M4 of PRIME.GEOMSOS.01"
          % (VERDICT, N_REC, worst_ratio))
    print("checks: %d, failures: %d %s" % (N_CHK, len(FAILS), FAILS or ""))
    print("elapsed: %.1f s" % (time.time() - T0))
    print("FIREWALL: standalone module (no cross-module import); zero "
          "cache dps %d as verification target only; finite statements; "
          "NO RH claim" % DPS_ZEROS)
    print("--- geometric_sos_probe: %d passed, %d failed ---"
          % (N_CHK - len(FAILS), len(FAILS)))
    return len(FAILS)


if __name__ == "__main__":
    raise SystemExit(1 if run() else 0)
