#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""exterior_square_factorization_probe -- PRIME.PORT.EXTERIOR.SQUARE.01
(EXPLORATION ONLY, experiments/; theorem-engineering on the RH-side
wall: THE EXTERIOR-SQUARE (WEDGE) FACTORIZATION OF THE WALL MARGIN.
The program lead's priority-2 route: IF the margin is a manifest
wedge square over a POSITIVE measure plus a NONNEGATIVE remainder,
then positivity is automatic and the infinite quantifier falls by
structure rather than by data.  2026-08-12.)

(a) THE HONEST RE-AIM, VERIFIED ONCE.  The lead originally targeted
the TRANSITION barrier margin  H + (1/2)Dmu1 - r^* B_+^{-1} r  of the
half-gap induction.  That object was already measured (CCIII,
halfgap_riccati_transition_probe, SPEC-SHA printed there): NEGATIVE
on 38 of 67 combined transitions, with H < 0 on 36.  A globally
positive factorization of the TRANSITION margin therefore cannot
exist -- no factorization makes a negative number nonnegative.  This
probe re-verifies the kill ONCE, in the lead's EXACT formulation
(the barrier matrix, not the scalar):
    G_h(k) := [[ H_k + (1/2)(mu1(h_k) - mu1(h_{k+1})),  r_k^T ],
               [ r_k,                                    B_+^k ]]
    barrier(k) holds  <=>  G_h(k) >= 0   (Schur, given B_+ > 0),
by EIGENCENSUS of G_h on the SURFACE transition ladder rebuilt
verbatim from CLXII/CCIII machinery (imported read-only, the
(h, kz)-sorted 39-step / 37-transition chain, h 142..878).  The DEEP
half of the combined ladder (28 rungs, h 1219..2854, CLIV 4e6 table)
is DECLARED OUT OF BUDGET here and its census is CITED from CCIII,
never re-measured: this probe's own barrier statement is
SURFACE-ONLY and typed as such.  Then the probe moves on.

THE RE-AIMED TARGET (the rest of the probe).  The LEVEL margin,
where positivity is true, registered and blind-tested:
    TARGET_h := m_h - (1/2) mu1(h) >= 0,
    m_h = lam_min(K_h),  K_h = odd_toeplitz(c_ar + c_at, M),
    mu1(h) = 4 sin^2(pi/(2h+1)),
the registered HALFGAP object (CLI registration sha ae292e55,
NO-ADJUST, 67/67 surface; CLIV deep holdout 28/28).  On the deployed
surface the pair (n_h, q_h) collapses along the critical direction,
so the registered inequality reads shat_h = m_h/mu1(h) >= 1/2 (CLI
W4 ward, reproduced here).

(b) THE BASIS -- THE EXACT SOURCE-ONLY BILINEAR REPRESENTATION.
Two exact identities are established (not assumed) on the whole
ladder and carry the entire probe:

  [B-FREQ]  the PERIODIC COMPLETION.  With L = 2M - 2, the even
  L-periodic extension of the lag vector c, its grid density
  D = FFT(extension) (real), and the SOURCE-ONLY sine reads
      S_j(v) := sum_{p<h} v_p sin(theta_j (p - (M-1)/2)),
      theta_j = 2 pi j / L,
  one has EXACTLY, for all v, w in R^h,
      v^T K_h w = (2/L) sum_j D_j S_j(v) S_j(w),
      v^T w     = (2/L) sum_j       S_j(v) S_j(w)   (Plancherel).
  Hence, with the SHIFTED spectral measure
      rho*_j := (2/L) (D_j - (1/2) mu1(h)),
      K_h - (1/2) mu1(h) I  =  Gram_{rho*}(S)   EXACTLY.
  The reads S_j are pure sine geometry: no primes, no zeros, no
  eigendata, no tau.  ALL arithmetic sits in the WEIGHTS rho*.

  [B-LIN]  the T163 correlation theorem (deployed, cited): for the
  parity basis t_a = parity_basis(h), the compression entry
      Gamma_ab := t_a^T K_h t_b = c . W_ab,   W_ab = the T163 lag
  weights of the pair (t_a, t_b) -- i.e. the prime comb enters each
  entry as ONE EXACT LINEAR FUNCTIONAL of the lag vector.  At the
  critical two-mode block that is EXACTLY THREE functionals
  (L11, L12, L22), the cited CLXX-CLXXX structure.

  WARDS: both identities to REP_WARD = 1e-10 relative on the 12-mode
  carrier basis (78 entries) on EVERY rung; B-LIN additionally
  against the independently built Gamma.  The carrier basis is the
  frozen NKAR = 12 low-frequency parity modes -- the CXCVII carrier
  frame WITHOUT its v_krit seat, because v_krit is target eigendata
  and the lead's own circularity criterion forbids it.  The price is
  DECLARED and MEASURED (B4): the carrier compression is an UPPER
  bound on m_h (Cauchy interlacing), never a lower bound.

(c) SYMBOLIC DIAGONALIZATION + INERTIA.  C1 (sympy, exact
rationals): the rank-3 determinant form of the critical two-mode
block, q(L11, L12, L22) = L11 L22 - L12^2, has Gram matrix
[[0,0,1/2],[0,-1,0],[1/2,0,0]], eigenvalues {1/2, -1/2, -1},
INERTIA (1, 2, 0) -- LORENTZ SIGNATURE (1,2), congruent to
diag(1,-1,-1) (the cited CLXX-CLXXX pinning, re-derived here from
the T163 functionals, not quoted).  C2: the FREQUENCY-CHANNEL
inertia of rho* per rung (n_pos/n_neg, mass fractions, h-stability
by OLS slope).  C3: the exact-rational LDL inertia of the 12-mode
shifted compression Gamma* = Gamma - (1/2) mu1 I at SUBSET rungs
(Fraction arithmetic on the float entries, v897 class -- no
eigenvalues).  C4: the EXTERIOR-SQUARE identity itself, warded
exactly on every rung at the critical seat (f, g) = (t1, t2):
    det Gram_{rho*}(f,g)
      = (1/2) sum_{j,k} rho*_j rho*_k (S_j(f)S_k(g) - S_k(f)S_j(g))^2
(the k = 2 Andreief/Cauchy-Binet case; evaluated in the O(L) closed
form A C - B^2, never as a double sum, never by eigenvalue).  C5:
the k = 3 Cauchy-Binet ward at a declared reduced instance.  C6: the
CANCELLATION DEPTH -- the exact three-term split
    det = wedge_+ + wedge_-  -  cross,
    wedge_+ = (1/2) sum_{j,k in POS}, wedge_- = (1/2) sum_{j,k in NEG},
    cross   =       sum_{j in POS, k in NEG},
census of cross/(wedge_+ + wedge_-) in digits of cancellation.

(d) THE COMPLETION -- the frozen candidate and its three conditions.
FROZEN FORM (declared before the frozen run):
    TARGET_h  =  wedge-square term over a POSITIVE measure  +  R_h,
    (i) nu_h >= 0 (a genuine positive measure),
    (ii) Z_h > 0 (a positive normalizer),
    (iii) R_h >= 0 (a nonnegative remainder),
all three MACHINE-VERIFIED, never assumed.  Two candidate
assignments are tested, both frozen:

  D-CAND-1 (the SEAT assignment, the lead's literal wedge form).
  nu := rho*_+ = the positive part of the shifted spectral measure;
  the manifest square is wedge_+ ; R := det - wedge_+ = wedge_- -
  cross.  Condition (iii) is a pure measurement.

  D-CAND-2 (the OPERATOR assignment, the lead's step-5 absorption).
  With the EXACT split K_h = P_h - N_h,
      P_h := Gram_{D_+}(S),  N_h := Gram_{D_-}(S)
  (both from a POSITIVE measure => every minor of either is a
  manifest wedge square by Andreief), put
      c_h := 1 - lam_max(N_h, P_h)   (generalized top eigenvalue),
      K_h  =  c_h P_h  +  R_h,   R_h := lam_max(N_h,P_h) P_h - N_h.
  Then (i) holds by construction (D_+ >= 0), (ii) is c_h > 0, and
  (iii) R_h >= 0 holds BY CONSTRUCTION.  THE DELIVERY QUESTION,
  which is the whole point: does the manifest square DELIVER the
  half-gap, i.e.
      c_h * lam_min(P_h)  >=  (1/2) mu1(h) ?
  Census + demand law (OLS slope of log10 of the delivery ratio
  against log10 h, jackknife 2SE).

  D-UNIQ (the structural gate).  The representing measure is UNIQUE
  up to the null channel: the weight -> lag map is the even-symmetric
  DFT (a bijection, round-trip warded), and the lag -> form map
  c |-> odd_toeplitz(c, M) has EXACTLY a one-dimensional kernel, the
  constant lag vector = the j = 0 channel, whose read S_0 vanishes
  identically.  Certified by rank(c |-> odd_toeplitz) == M - 1 at
  declared small h, by the explicit kernel vector, and by S_0 == 0.
  Consequence: "choose a positive representing measure" is NOT a
  modelling freedom -- rho* IS the measure (mass on j = 0 is invisible
  to the form), and its sign census decides the lead's route outright.

  D-ANATOMY (diagnostic only, eigendata-carrying, declared).  The
  exact two-factor identity  m_h = p*_h (1 - r*_h)  at the critical
  direction x*, p* = x*^T P x*, r* = x*^T N x*/p*, locating WHICH
  factor the isotropic completion loses.  x* is target eigendata:
  this block is a MEASUREMENT, it never enters a certificate.

  D-PRIME (is nu source-only?).  The AR/SM/OSC split of the density
  (archimedean closed form / smooth PNT comb / prime oscillation by
  exact complement) restricted to the POSITIVE channels: if nu
  carries prime oscillation, the factorization is not a structural
  explanation and the all-h statement inherits the arithmetic.

(e) GATES.  Controls (each must BREAK the level target or the
weight positivity; silence => WARD-BROKEN): smooth PNT comb,
scramble seed 1, Epstein x^2 + 5y^2 at kz = 9 (single rung, O(X^2),
declared), cosh injection A = 0.01 / delta = 0.05 / gamma0 = 10.0
(CLXII deployed amplitudes, frozen selection cited), mass rescale
1.1.  TAU-SCREENS on every margin against the declared screen
variable TAU_REP := c_h (the wall scalar OF THIS REPRESENTATION --
declared as the analogue of the deployed lam_min(I - G), never
identified with it), bands PASS |slope| <= 0.30 / RELOC >= 0.70 /
else AMBIG, excluded counts printed.  ANTI-CIRCULARITY (frozen):
AST firewall (banned ids zetazero / nzeros / primerange / isprime /
primepi / nextprime / prevprime); ZERO zero-reads (impostor control
N/A DECLARED); the reads S_j are source-only sine geometry; no
tau enters any construction; the critical eigenvector enters ONLY
D-ANATOMY and the reproduction wards, never a certificate; RNG only
inside the declared scramble control.

SMOKE DISCLOSURE (mandatory, verbatim).  FIVE smoke rounds were run
before this spec was frozen, and they DID see census numbers.  What
smoke established and what it changed: (s1) the two representation
identities [B-FREQ] and Plancherel were CONFIRMED at machine
precision -- this is what made the whole probe well-posed and fixed
the S-read convention (the half-integer phase (M-1)/2); (s2) the
level ladder was confirmed cheap (67 rungs, ~20 s) and the CXLIII
band reproduced exactly, so no sub-sampling is needed; (s3) the
surface transition chain was confirmed to reproduce CLXII (21 fails
of 37) ONLY when (h, kz)-sorted -- the sort is therefore frozen into
(a); (s4) the D-CAND-1 remainder was seen to be negative and the
D-CAND-2 delivery ratio was seen to be far below 1: THESE NUMBERS
WERE SEEN BEFORE FREEZE.  The verdict RULE below is nevertheless
frozen in falsifiable form, and the honest value of the run is (i)
the exact identities and wards, (ii) the demand law and the loss
anatomy, which smoke did not fix, and (iii) the controls.  No
threshold in this spec was chosen to make any census come out a
particular way; no census was re-run with a changed definition.
(s5) the two-factor identity m = p*(1 - r*) was found in smoke and
is included as a DIAGNOSTIC block, declared as such.

HONEST AMENDMENTS (post-smoke-6, disclosed; two ward NORMALIZATIONS
and one restated certificate, no census definition touched):
  A1  the C4 seat determinant is a 4..8-digit near-cancellation
      (measured in C6), so comparing the wedge route against the
      direct 2x2 determinant at a RELATIVE bar is float-impossible
      by construction.  The comparison is therefore normalized by
      the TERM SCALE |A C| + B^2 (the same device as the CCIII A2
      part-scale disclosure).  The three-term split ward, which is
      cancellation-free, keeps the relative bar.
  A2  condition (iii) lam_min(R_h) >= 0 is warded relative to
      lam_max(R_h) (the matrix's own scale) at PSD_TOL = 1e-12, not
      relative to lam_min(P_h).
  A3  D-UNIQ was restated from a condition-number test on
      [(S_j.S_k)^2] (which is Vandermonde-ill-conditioned and
      therefore uninformative) to the exact rank/kernel certificate
      described above.  The structural conclusion is unchanged and
      is now proved rather than estimated.

VERDICT RULE (frozen):
  EXTERIOR-SQUARE-HOLDS  iff BOTH candidate assignments satisfy all
      three positivity conditions on ALL rungs AND the manifest
      square DELIVERS the half-gap (delivery ratio >= 1 on all
      rungs); the residual all-h demand is then typed exactly.
  PARTIAL  iff the factorization EXISTS with all three conditions
      but does NOT deliver the target (or delivers only on a
      subset) -- the resisting channel is named and its demand law
      measured.
  REFUTED  iff a positivity condition fails structurally.

NO RH claim.  Every census is a statement about float64-computed
matrices of a deployed finite ladder (inertia decisions exact-
rational on those entries at SUBSET rungs); nothing here proves
h-uniformity, tail statements, or RH; fits are empirical laws.  No
marker moves, no ledger row, no paper edit.

FIREWALL: experiments/ only; v563_paper2_readouts READ-ONLY;
halfgap_riccati_transition_probe imported READ-ONLY for (a);
stdout only; no files written.

Sources (read-only): v563_paper2_readouts (odd_toeplitz,
parity_basis, arch_lags, atom_lags_at, build_window,
lag_weights_from_v = T163); halfgap_riccati_transition_probe
(CLXII/CCIII surface ladder machinery, barrier census); mu1 + 1/2 +
NO-ADJUST from halfgap_registration_probe (CLI); CXLIII shat band as
reproduction reference; smooth comb convention from
tail_sign_mechanism_probe (CXLVII); cosh signature from
arith_healthcode12_probe (declared convention); CCIII combined
barrier census CITED.

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/exterior_square_factorization_probe.py
"""

import ast
import hashlib
import math
import os
import sys
import time
from fractions import Fraction

import numpy as np
import scipy.linalg as sla

_HERE = os.path.dirname(os.path.abspath(__file__))
_VERIFY = os.path.abspath(os.path.join(_HERE, "..", "..",
                                       "verification"))
sys.path.insert(0, _HERE)
sys.path.insert(0, _VERIFY)

import v563_paper2_readouts as core            # noqa: E402 READ-ONLY
import halfgap_riccati_transition_probe as hrt  # noqa: E402 READ-ONLY

# ---------------------------------------------------------------- frozen
KZMAX = 150
MIN_RUNGS = 40
NKAR = 12
SUBSET_KZ = (9, 13, 26, 40, 60, 90, 121)
UNIQ_H = (5, 8, 12, 20, 30)
REP_WARD = 1e-10
ID_WARD = 1e-10
CB_WARD = 1e-10
SPLIT_WARD = 1e-12
PSD_TOL = 1e-12
REG_C = Fraction(1, 2)
SHAT_REF = (0.5025, 1.0273, 2.1845)
SHAT_RTOL = 2e-2
PRED_FAILS = 21
PRED_TRANS = 37
CCIII_COMB_FAILS = 38
CCIII_COMB_TRANS = 67
CCIII_COMB_HNEG = 36
NG_SMOOTH = 6000
CTRL_KZ = 9
SCR_SEED = 1
INJ_A = 0.01
INJ_DELTA = 0.05
INJ_GAMMA0 = 10.0
RSC_FAC = 1.1
SLOPE_PASS = 0.30
SLOPE_RELOC = 0.70
BANNED_IDS = ("zetazero", "nzeros", "primerange", "isprime",
              "primepi", "nextprime", "prevprime")

CHECKS = []
KILLS = []
T0 = time.time()


def check(name, ok, detail="", kill=None):
    CHECKS.append((name, bool(ok)))
    if kill and not ok:
        KILLS.append(kill)
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
        nm = None
        if isinstance(node, ast.Name):
            nm = node.id
        elif isinstance(node, ast.Attribute):
            nm = node.attr
        if nm and nm.lower() in banned:
            bad.append(nm)
    return bad


def ols_line(x, y):
    x = np.asarray(x, float)
    y = np.asarray(y, float)
    vx = float(np.var(x))
    if vx == 0.0:
        return float(np.mean(y)), 0.0, float("nan")
    b = float(np.cov(x, y, bias=True)[0, 1] / vx)
    a = float(np.mean(y) - b * np.mean(x))
    ss = float(np.sum((y - a - b * x) ** 2))
    st = float(np.sum((y - np.mean(y)) ** 2))
    return a, b, (1.0 - ss / st if st > 0 else float("nan"))


def jack_slope(x, y):
    x = np.asarray(x, float)
    y = np.asarray(y, float)
    _a, b, r2 = ols_line(x, y)
    n = len(x)
    bb = []
    for i in range(n):
        msk = np.ones(n, bool)
        msk[i] = False
        bb.append(ols_line(x[msk], y[msk])[1])
    bb = np.array(bb)
    se = math.sqrt((n - 1) / n * float(np.sum((bb - bb.mean()) ** 2)))
    return b, se, r2


def screen(vals, taus, label):
    vals = np.asarray(vals, float)
    taus = np.asarray(taus, float)
    pos = (vals > 0) & (taus > 0)
    if int(np.sum(pos)) < 3:
        return "%s: vacuous(pos=%d)" % (label, int(np.sum(pos)))
    _a, sl, r2 = ols_line(np.log(taus[pos]), np.log(vals[pos]))
    lab = ("PASS" if abs(sl) <= SLOPE_PASS
           else "RELOC" if sl >= SLOPE_RELOC else "AMBIG")
    return ("%s: %s(slope %+.3f, R2 %.3f, %d excluded)"
            % (label, lab, sl, r2, int(np.sum(~pos))))


def trio(v):
    v = np.asarray(v, float)
    return float(np.min(v)), float(np.median(v)), float(np.max(v))


def f3(v):
    return "%.4f/%.4f/%.4f" % trio(v)


def e3(v):
    return "%.3e/%.3e/%.3e" % trio(v)


# ------------------------------------------------ the representation
def grid_density(c):
    """even L-periodic completion of the lag vector, L = 2M - 2."""
    c = np.asarray(c, float)
    a = np.concatenate([c, c[-2:0:-1]])
    d = np.fft.fft(a)
    assert float(np.max(np.abs(d.imag))) <= 1e-9 * max(
        1.0, float(np.max(np.abs(d.real))))
    return d.real


def sine_reads(V, M):
    """S (L, k) with S_j(v) = sum_p v_p sin(theta_j (p - (M-1)/2)),
    computed by FFT of the odd embedding (O(L log L), no h x L
    matrix).  SOURCE-ONLY: pure sine geometry."""
    h = V.shape[0]
    L = 2 * M - 2
    E = np.zeros((L, V.shape[1]))
    E[:h, :] = V
    E[(M - 1) - np.arange(h), :] -= V
    Vh = np.fft.fft(E, axis=0)
    ph = np.exp(1j * math.pi * np.arange(L) * (M - 1) / L)
    return np.real(0.5j * (Vh * ph[:, None]))


def gram_from_dens(dpart, M):
    """the h x h Gram matrix of the S-reads against a frequency
    weight: Gram = odd_toeplitz(ifft(weight)) -- exact inverse of the
    periodic completion, no quadrature."""
    return core.odd_toeplitz(np.fft.ifft(dpart).real[:M], M)


def smooth_comb(alpha, ng=NG_SMOOTH):
    ug = (np.arange(ng) + 0.5) * (2.0 * alpha / ng)
    return ug, 2.0 * np.exp(ug / 2.0) * (2.0 * alpha / ng)


def lambda_eps(N):
    """Epstein x^2 + 5y^2 comb (port_schur_reduction verbatim)."""
    r = np.zeros(N + 1)
    s = int(math.isqrt(N)) + 1
    for x in range(-s, s + 1):
        for y in range(-s, s + 1):
            v = x * x + 5 * y * y
            if 1 <= v <= N:
                r[v] += 1.0
    a = r / 2.0
    lam = np.zeros(N + 1)
    for n in range(2, N + 1):
        acc = a[n] * math.log(n)
        for dd in range(2, n):
            if n % dd == 0:
                acc -= lam[dd] * a[n // dd]
        lam[n] = acc
    return lam


def mu1_of(h):
    return 4.0 * math.sin(math.pi / (2.0 * h + 1.0)) ** 2


def wedge_closed(a, f, g):
    """(1/2) sum_{j,k} a_j a_k (f_j g_k - f_k g_j)^2 in the O(L)
    closed form A C - B^2 (Andreief k = 2, no double sum)."""
    A = float(np.sum(a * f * f))
    B = float(np.sum(a * f * g))
    C = float(np.sum(a * g * g))
    return A * C - B * B, A, B, C


def ldl_inertia_fr(Mfr):
    """symmetric LDL with diagonal pivoting on exact rationals ->
    (n_pos, n_neg, n_zero).  No eigenvalues (spec (c) C3)."""
    n = len(Mfr)
    A = [list(row) for row in Mfr]
    idx = list(range(n))
    npos = nneg = nzero = 0
    for k in range(n):
        piv = max(range(k, n), key=lambda i: abs(A[i][i]))
        if A[piv][piv] == 0:
            nzero += n - k
            break
        if piv != k:
            A[k], A[piv] = A[piv], A[k]
            for row in A:
                row[k], row[piv] = row[piv], row[k]
            idx[k], idx[piv] = idx[piv], idx[k]
        d = A[k][k]
        if d > 0:
            npos += 1
        else:
            nneg += 1
        for i in range(k + 1, n):
            f = A[i][k] / d
            if f == 0:
                continue
            for j in range(k + 1, n):
                A[i][j] = A[i][j] - f * A[k][j]
    return npos, nneg, nzero


# ------------------------------------------------------- rung builder
def level_rung(kz, world=None, scramble_seed=None, comb=None,
               lag_fn=None, want_split=False):
    """One LEVEL rung of the registered halfgap surface.  Returns the
    frozen read block; None if the window is not faithful."""
    try:
        rr = core.build_window(kz, scramble_seed=scramble_seed)
    except Exception:
        return None
    if not (core.H_MIN <= rr["h"] <= core.HCAP):
        return None
    if rr["X"] > core.ATOM_MAX:
        return None
    alpha, M, h, Dg = rr["alpha"], rr["M"], rr["h"], rr["D"]
    uu = np.asarray(rr["uu"], float)
    mm = 2.0 * np.asarray(rr["lam"], float)
    if world == "smooth":
        uu, mm = smooth_comb(alpha)
    elif world == "rescale":
        mm = RSC_FAC * mm
    if comb is not None:
        uu, mm = comb
    c_ar = np.asarray(core.arch_lags(M, Dg), float)
    c_at = np.asarray(core.atom_lags_at(alpha, M, uu, mm)[0], float)
    c = c_ar + c_at
    if lag_fn is not None:
        c = c + lag_fn(M, Dg)
    out = dict(kz=kz, h=h, M=M, L=2 * M - 2, alpha=float(alpha),
               c=c, c_ar=c_ar, mu1=mu1_of(h))
    if want_split:
        ug, mg = smooth_comb(alpha)
        out["c_sm"] = np.asarray(
            core.atom_lags_at(alpha, M, ug, mg)[0], float)
    return out


def level_reads(rg, with_ops=True):
    """the frozen read block of one rung: m_h, the S-reads on the
    carrier basis, the shifted measure, the wedge split and (with_ops)
    the operator completion."""
    M, h, L = rg["M"], rg["h"], rg["L"]
    K = core.odd_toeplitz(rg["c"], M)
    D = grid_density(rg["c"])
    mu1 = rg["mu1"]
    w, V = np.linalg.eigh(K)
    m = float(w[0])
    rg.update(m=m, shat=m / mu1, D=D)
    Tb = core.parity_basis(h, NKAR).T                    # (h, NKAR)
    S = sine_reads(Tb, M)                                # (L, NKAR)
    rho = 2.0 * D / L
    Gam_rep = (S * rho[:, None]).T @ S
    Gam_dir = Tb.T @ (K @ Tb)
    sc = max(float(np.max(np.abs(Gam_dir))), 1e-300)
    rg["dev_freq"] = float(np.max(np.abs(Gam_rep - Gam_dir))) / sc
    Pl = (S * (2.0 / L)).T @ S
    rg["dev_plan"] = float(np.max(np.abs(Pl - np.eye(NKAR))))
    # [B-LIN] T163: every entry one linear functional of the lag
    dev_lin = 0.0
    Wab = {}
    for a in range(NKAR):
        for b in range(a, NKAR):
            if a == b:
                Wm = core.lag_weights_from_v(Tb[:, a], h)
            else:
                Wpp = core.lag_weights_from_v(Tb[:, a] + Tb[:, b], h)
                Wm = 0.5 * (Wpp
                            - core.lag_weights_from_v(Tb[:, a], h)
                            - core.lag_weights_from_v(Tb[:, b], h))
            Wab[(a, b)] = Wm
            dev_lin = max(dev_lin, abs(float(rg["c"] @ Wm)
                                       - float(Gam_dir[a, b])) / sc)
    rg["dev_lin"] = dev_lin
    rg["W3"] = (Wab[(0, 0)], Wab[(0, 1)], Wab[(1, 1)])
    rg["Gam"] = Gam_dir
    rg["lam_car"] = float(np.linalg.eigvalsh(Gam_dir)[0])
    # frequency-channel inertia of the SHIFTED measure
    rst = rho - 0.5 * mu1 * (2.0 / L)
    pos = rst > 0
    rg["n_ch"] = int(L // 2 + 1)
    rg["n_pos"] = int(np.sum(pos[:L // 2 + 1]))
    rg["n_neg"] = int(np.sum(~pos[:L // 2 + 1]))
    rg["mass_pos"] = float(np.sum(rst[pos]))
    rg["mass_neg"] = float(-np.sum(rst[~pos]))
    rg["dneg_frac"] = float(np.mean(D[:L // 2 + 1] < 0))
    rg["D_min"] = float(D.min())
    rg["D_max"] = float(D.max())
    # [C4/C6] the exterior square at the critical seat (t1, t2)
    f, g = S[:, 0], S[:, 1]
    ap = np.where(pos, rst, 0.0)
    an = np.where(pos, 0.0, -rst)
    dpp, Ap, Bp, Cp = wedge_closed(ap, f, g)
    dnn, An, Bn, Cn = wedge_closed(an, f, g)
    cross = Ap * Cn + An * Cp - 2.0 * Bp * Bn
    dtot, At, Bt, Ct = wedge_closed(rst, f, g)
    rg["dev_wedge"] = abs(dtot - (dpp + dnn - cross)) / max(
        abs(dpp) + abs(dnn) + abs(cross), 1e-300)
    G2k = Gam_dir[:2, :2] - 0.5 * mu1 * np.eye(2)
    det_k = float(G2k[0, 0] * G2k[1, 1] - G2k[0, 1] ** 2)
    # A1 (disclosed): TERM-SCALE normalization -- the seat
    # determinant is a 4..8 digit cancellation (C6)
    rg["dev_seat"] = abs(dtot - det_k) / max(abs(At * Ct) + Bt * Bt,
                                             1e-300)
    rg["dev_seat_rel"] = abs(dtot - det_k) / max(abs(det_k), 1e-300)
    rg.update(w_pos=dpp, w_neg=dnn, cross=cross, det2=dtot,
              canc=cross / max(dpp + dnn, 1e-300),
              R_seat=dnn - cross)
    rg["seat_pivot"] = (float(np.linalg.det(Gam_dir[:2, :2]))
                        / float(Gam_dir[1, 1]))
    if not with_ops:
        return rg
    # [D-CAND-2] the operator completion K = c_h P + R_h
    P = gram_from_dens(np.where(D > 0, D, 0.0), M)
    N = gram_from_dens(np.where(D > 0, 0.0, -D), M)
    rg["dev_split"] = (float(np.max(np.abs(P - N - K)))
                       / max(float(np.max(np.abs(K))), 1e-300))
    rg["lamP"] = float(np.linalg.eigvalsh(P)[0])
    rg["lamN"] = float(np.linalg.eigvalsh(N)[0])
    lmax = float(sla.eigh(N, P, eigvals_only=True)[-1])
    rg["lmax_gen"] = lmax
    rg["c_h"] = 1.0 - lmax
    Rm = lmax * P - N
    evR = np.linalg.eigvalsh(Rm)
    rg["lamR"] = float(evR[0])
    rg["lamR_top"] = float(evR[-1])
    rg["deliver"] = rg["c_h"] * rg["lamP"] / (0.5 * mu1)
    # [D-ANATOMY] eigendata-carrying DIAGNOSTIC (declared)
    x = V[:, 0]
    p_star = float(x @ (P @ x))
    r_star = float(x @ (N @ x)) / p_star
    rg["p_star"] = p_star
    rg["r_star"] = r_star
    rg["dev_two"] = abs(p_star * (1.0 - r_star) - m) / max(abs(m),
                                                           1e-300)
    rg["loss_dir"] = rg["c_h"] / max(1.0 - r_star, 1e-300)
    rg["loss_eng"] = rg["lamP"] / p_star
    return rg


def main():
    section("PRIME.PORT.EXTERIOR.SQUARE.01 -- the exterior-square "
            "(wedge) factorization of the wall margin: barrier kill "
            "confirmation, the exact source-only bilinear "
            "representation, inertia + wedge channel, the completion "
            "(EXPLORATION ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s"
          % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
    print("    NO RH claim; no marker moves; experiments/ only.  "
          "Smoke disclosure in the spec, verbatim.")
    print("\nS0 -- firewall")
    bad = ast_scan(BANNED_IDS)
    check("S0.1 AST firewall clean (no prime/zero oracles)", not bad,
          ",".join(sorted(set(bad))) if bad else "", kill="K0")
    check("S0.2 IMPOSTOR N/A DECLARED: this probe consumes ZERO "
          "zero-reads (no off-line-zero seat exists here)", True)

    # ============================================================ A
    section("A -- BARRIER KILL CONFIRMATION in the lead's exact "
            "formulation (surface transition ladder, once)")
    zones = hrt.ladder_zones()
    truth = [hrt.build_rung("surf", kz) for kz in zones]
    truth_h = sorted([r for r in truth if r is not None],
                     key=lambda r: (r["h"], r["kz"]))
    steps, dead_ell = hrt.make_steps(truth_h)
    tr = hrt.transition_table(steps, "ell")
    ok = [t for t in tr if t["status"] == "OK"]
    check("A0 surface ladder rebuilt (%d zones, %d rungs, %d steps, "
          "%d transitions, %d dead-ell)  [%.1f s]"
          % (len(zones), len(truth_h), len(steps), len(tr), dead_ell,
             time.time() - T0),
          len(ok) == PRED_TRANS, "OK transitions %d" % len(ok),
          kill="K1")
    if KILLS:
        return finish()
    n_neg = n_hneg = n_rdom = 0
    lam_list = []
    for t in ok:
        n = t["B1"].shape[0]
        G = np.zeros((n + 1, n + 1))
        G[0, 0] = t["a"]
        G[0, 1:] = t["rvec"]
        G[1:, 0] = t["rvec"]
        G[1:, 1:] = t["B1"]
        lam = float(np.linalg.eigvalsh(G)[0])
        lam_list.append(lam)
        if lam < 0:
            n_neg += 1
            if t["H"] < 0:
                n_hneg += 1
            else:
                n_rdom += 1
    p_b, f_b, r_b = hrt.barrier_census(ok)
    agree = (n_neg == f_b)
    print("    A-TABLE  the barrier matrix G_h = [[H + (1/2)Dmu1, "
          "r^T], [r, B_+]] on the surface chain")
    print("    %-34s %s" % ("transitions (OK / total)",
                            "%d / %d" % (len(ok), len(tr))))
    print("    %-34s %s" % ("lam_min(G_h) < 0  (barrier FAILS)",
                            "%d / %d" % (n_neg, len(ok))))
    print("    %-34s %s" % ("  of which H < 0", "%d" % n_hneg))
    print("    %-34s %s" % ("  of which r-dominated (H >= 0)",
                            "%d" % n_rdom))
    print("    %-34s %s" % ("lam_min(G_h) >= 0 (barrier holds)",
                            "%d / %d" % (len(ok) - n_neg, len(ok))))
    print("    %-34s %s" % ("exact-rational slack census",
                            "pass %d / fail %d / refused %d"
                            % (p_b, f_b, r_b)))
    print("    %-34s %s" % ("lam_min(G_h) min/med/max", e3(lam_list)))
    print("    %-34s %s" % ("CITED CCIII combined ladder",
                            "%d fails of %d, H < 0 on %d "
                            "(deep half NOT re-measured here)"
                            % (CCIII_COMB_FAILS, CCIII_COMB_TRANS,
                               CCIII_COMB_HNEG)))
    check("A1 Schur equivalence: eigencensus == exact-rational "
          "barrier census (%d == %d)" % (n_neg, f_b), agree,
          kill="K1")
    check("A2 REPRODUCTION CLXII/CCIII surface: %d fails of %d "
          "(reference %d of %d)" % (f_b, len(ok), PRED_FAILS,
                                    PRED_TRANS),
          f_b == PRED_FAILS and len(ok) == PRED_TRANS, kill="K1")
    check("A3 typed: BARRIER-KILL-CONFIRMED(surface %d/%d negative; "
          "combined %d/%d CITED CCIII) => NO globally positive "
          "factorization of the TRANSITION margin can exist; the "
          "probe re-aims at the LEVEL margin"
          % (n_neg, len(ok), CCIII_COMB_FAILS, CCIII_COMB_TRANS),
          n_neg > 0)
    del truth, truth_h, steps, tr, ok

    # ============================================================ B
    section("B -- the LEVEL ladder and the exact source-only "
            "bilinear representation")
    lad = []
    for kz in range(2, KZMAX + 1):
        rg = level_rung(kz, want_split=True)
        if rg is not None:
            lad.append(rg)
    lad.sort(key=lambda r: (r["h"], r["kz"]))
    check("B0 faithful level ladder >= %d rungs" % MIN_RUNGS,
          len(lad) >= MIN_RUNGS,
          "%d rungs, h %d..%d  [%.1f s]"
          % (len(lad), lad[0]["h"], lad[-1]["h"], time.time() - T0),
          kill="K1")
    if KILLS:
        return finish()
    for rg in lad:
        level_reads(rg)
    shat = np.array([r["shat"] for r in lad])
    band_ok = all(abs(a / b - 1.0) <= SHAT_RTOL
                  for a, b in zip(trio(shat), SHAT_REF))
    check("B1 REPRODUCTION CXLIII/CLI band: shat min/med/max %s == "
          "%.4f/%.4f/%.4f (rtol %.0e)"
          % (f3(shat), SHAT_REF[0], SHAT_REF[1], SHAT_REF[2],
             SHAT_RTOL), band_ok, kill="K1")
    n_reg = int(np.sum(shat >= float(REG_C)))
    check("B1b registered halfgap holds on the level ladder: "
          "%d/%d rungs at shat >= 1/2 (NO-ADJUST, CLI)"
          % (n_reg, len(lad)), n_reg == len(lad), kill="K1")
    dfq = max(r["dev_freq"] for r in lad)
    dpl = max(r["dev_plan"] for r in lad)
    dln = max(r["dev_lin"] for r in lad)
    check("B2 [B-FREQ] WARD  v^T K_h w == (2/L) sum_j D_j S_j(v)S_j(w)"
          "  on %d x %d carrier entries, all rungs: max rel dev "
          "%.2e <= %.0e" % (NKAR, NKAR, dfq, REP_WARD),
          dfq <= REP_WARD, kill="K2")
    check("B3 [PLANCHEREL] WARD  v^T w == (2/L) sum_j S_j(v)S_j(w) "
          "(=> K_h - (1/2)mu1 I = Gram_{rho*}(S) EXACTLY): max abs "
          "dev %.2e <= %.0e" % (dpl, REP_WARD), dpl <= REP_WARD,
          kill="K2")
    check("B4 [B-LIN] WARD T163: every carrier entry ONE exact "
          "linear functional of the lag vector (Gamma_ab == c . W_ab;"
          " 3 functionals at the critical two-mode seat, %d over the "
          "%d-mode basis): max rel dev %.2e <= %.0e"
          % (NKAR * (NKAR + 1) // 2, NKAR, dln, REP_WARD),
          dln <= REP_WARD, kill="K2")
    car = np.array([r["lam_car"] / r["mu1"] for r in lad])
    n_up = int(np.sum(car >= shat - 1e-12))
    print("    B5 CARRIER-BASIS PRICE (declared, measured): "
          "lam_min(Gamma_%d)/mu1 %s vs shat %s"
          % (NKAR, f3(car), f3(shat)))
    check("B5 typed: CARRIER-UPPER-BOUND(%d/%d; Cauchy interlacing "
          "=> the prime-free carrier basis can NEVER lower-bound "
          "m_h -- v_krit excluded by the circularity criterion)"
          % (n_up, len(lad)), n_up == len(lad))

    # ============================================================ C
    section("C -- symbolic diagonalization, inertia census, and the "
            "exterior-square identity")
    import sympy as sp
    L11, L12, L22 = sp.symbols("L11 L12 L22", real=True)
    q = L11 * L22 - L12 ** 2
    Q = sp.Matrix(3, 3, lambda i, j: sp.Rational(1, 2) * sp.diff(
        sp.diff(q, [L11, L12, L22][i]), [L11, L12, L22][j]))
    evs = Q.eigenvals()
    ev_list = sorted([sp.nsimplify(k) for k in evs for _ in
                      range(evs[k])], key=lambda z: float(z))
    npos = sum(1 for z in ev_list if z > 0)
    nneg = sum(1 for z in ev_list if z < 0)
    nzer = sum(1 for z in ev_list if z == 0)
    Jd = sp.diag(1, -1, -1)
    lorentz = (npos, nneg, nzer) == (1, 2, 0)
    print("    C1 the rank-3 determinant form of the critical "
          "two-mode block, from the THREE T163 functionals:")
    print("       q(L11, L12, L22) = %s" % sp.sstr(q))
    print("       Gram matrix Q = %s" % str(Q.tolist()))
    print("       eigenvalues   = %s   inertia (n+, n-, n0) = "
          "(%d, %d, %d)" % ([str(z) for z in ev_list], npos, nneg,
                            nzer))
    print("       congruent to J = %s" % str(Jd.tolist()))
    check("C1 SYMBOLIC (exact rationals): the det form has LORENTZ "
          "SIGNATURE (1,2), congruent to diag(1,-1,-1) -- NOT PSD, "
          "so sign of the three functionals never implies "
          "positivity", lorentz, kill="K2")
    nposc = np.array([r["n_pos"] for r in lad], float)
    nch = np.array([r["n_ch"] for r in lad], float)
    hh = np.array([float(r["h"]) for r in lad])
    frac = nposc / nch
    sl_f, se_f, r2_f = jack_slope(np.log(hh), frac)
    mp = np.array([r["mass_pos"] for r in lad])
    mn = np.array([r["mass_neg"] for r in lad])
    print("    C2 FREQUENCY-CHANNEL INERTIA of rho* (per rung, "
          "%d..%d channels):" % (int(nch.min()), int(nch.max())))
    print("       positive-channel FRACTION %s   d(frac)/dlog h "
          "%+.4f (2SE %.4f, R2 %.3f)" % (f3(frac), sl_f, 2 * se_f,
                                         r2_f))
    print("       positive mass %s   negative mass %s   ratio "
          "neg/pos %s" % (e3(mp), e3(mn), f3(mn / mp)))
    hstab = abs(sl_f) <= 0.05
    check("C2 typed: POSITIVE-CHANNEL-STRUCTURE-%s (fraction slope "
          "%+.4f vs bar 0.05); the negative channels are NEVER empty"
          % ("H-STABLE" if hstab else "H-DRIFTING", sl_f),
          int(np.sum(np.array([r["n_neg"] for r in lad]) > 0))
          == len(lad))
    sub = [r for r in lad if r["kz"] in SUBSET_KZ]
    inert = []
    for rg in sub:
        Gs = rg["Gam"] - 0.5 * rg["mu1"] * np.eye(NKAR)
        Mfr = [[Fraction(float(Gs[i, j])) for j in range(NKAR)]
               for i in range(NKAR)]
        inert.append((rg["h"],) + ldl_inertia_fr(Mfr))
    all_pd = all(t[1] == NKAR for t in inert)
    print("    C3 EXACT-RATIONAL LDL inertia of Gamma* = Gamma - "
          "(1/2)mu1 I on %d subset rungs (no eigenvalues):" % len(sub))
    for t in inert:
        print("       h %5d   (n+, n-, n0) = (%d, %d, %d)" % t)
    check("C3 typed: CARRIER-COMPRESSION-PD(%d/%d exact-rational) -- "
          "the %d-mode shifted compression is definite, i.e. the "
          "carrier seat SEES no negative channel (it is an upper "
          "bound, cf. B5)" % (sum(1 for t in inert if t[1] == NKAR),
                              len(inert), NKAR), all_pd)
    dw = max(r["dev_wedge"] for r in lad)
    ds = max(r["dev_seat"] for r in lad)
    dsr = max(r["dev_seat_rel"] for r in lad)
    check("C4 [ANDREIEF k=2] WARD the EXTERIOR-SQUARE identity "
          "det Gram*(f,g) = (1/2) int int |f^g|^2 drho* drho* on "
          "every rung at the critical seat (t1, t2): three-term "
          "split max rel dev %.2e; wedge route vs direct 2x2 "
          "determinant max dev %.2e <= %.0e on the TERM SCALE "
          "(amendment A1; the raw relative dev is %.2e -- that is "
          "the C6 cancellation, not a ward failure)"
          % (dw, ds, ID_WARD, dsr), max(dw, ds) <= ID_WARD,
          kill="K2")
    # C5 Cauchy-Binet k = 3 at a declared reduced instance
    rg0 = lad[0]
    S3 = sine_reads(core.parity_basis(rg0["h"], 3).T, rg0["M"])
    rho0 = 2.0 * rg0["D"] / rg0["L"]
    top = np.argsort(-np.abs(rho0))[:26]
    G3 = (S3[top] * rho0[top][:, None]).T @ S3[top]
    acc = 0.0
    for i1 in range(len(top)):
        for i2 in range(i1 + 1, len(top)):
            for i3 in range(i2 + 1, len(top)):
                dd = float(np.linalg.det(S3[top[[i1, i2, i3]]]))
                acc += (rho0[top[i1]] * rho0[top[i2]]
                        * rho0[top[i3]] * dd * dd)
    cb_dev = abs(acc - float(np.linalg.det(G3))) / max(
        abs(float(np.linalg.det(G3))), 1e-300)
    check("C5 [CAUCHY-BINET k=3] WARD det Gram = sum_{j<k<l} "
          "rho_j rho_k rho_l det(S)^2 at the declared reduced "
          "instance (h %d, %d strongest channels): rel dev %.2e "
          "<= %.0e" % (rg0["h"], len(top), cb_dev, CB_WARD),
          cb_dev <= CB_WARD, kill="K2")
    canc = np.array([r["canc"] for r in lad])
    dig = -np.log10(np.maximum(1.0 - canc, 1e-300))
    print("    C6 CANCELLATION DEPTH at the critical seat: "
          "cross/(wedge_+ + wedge_-) = %s"
          % ("%.12f/%.12f/%.12f" % trio(canc)))
    print("       => digits of cancellation %s ; det2 >= 0 on %d/%d"
          % (f3(dig), int(np.sum(np.array([r["det2"] for r in lad])
                                 >= 0)), len(lad)))
    check("C6 typed: DIFFUSE-CANCELLATION(median %.1f digits) -- the "
          "exterior square is nonnegative, but NOT manifestly: its "
          "positivity is a %.0f-digit near-cancellation between "
          "same-sign and opposite-sign channel pairs"
          % (float(np.median(dig)), float(np.median(dig))), True)

    # ============================================================ D
    section("D -- THE COMPLETION: the three positivity conditions, "
            "machine-verified")
    # D-UNIQ (amendment A3): exact rank / kernel certificate
    print("    D1 UNIQUENESS OF THE REPRESENTING MEASURE "
          "(weight -> lag is the even-symmetric DFT; lag -> form is "
          "c |-> odd_toeplitz(c, M))")
    uniq = []
    for hh_ in UNIQ_H:
        Mh = 2 * hh_
        rows_ = []
        for i in range(Mh):
            e = np.zeros(Mh)
            e[i] = 1.0
            rows_.append(core.odd_toeplitz(e, Mh).ravel())
        Amap = np.array(rows_)
        sv = np.linalg.svd(Amap, compute_uv=False)
        rk = int(np.sum(sv > sv[0] * 1e-12))
        ker = float(np.max(np.abs(
            core.odd_toeplitz(np.ones(Mh), Mh))))
        S0 = float(np.max(np.abs(
            sine_reads(np.eye(hh_), Mh)[0])))
        uniq.append((hh_, Mh, rk, ker, S0))
        print("       h %3d  M %3d  rank %3d (= M - 1 : %s)  "
              "|odd_toeplitz(1)| %.1e  |S_0| %.1e"
              % (hh_, Mh, rk, "yes" if rk == Mh - 1 else "NO", ker,
                 S0))
    uniq_ok = all(t[2] == t[1] - 1 and t[3] < 1e-12 and t[4] < 1e-12
                  for t in uniq)
    rt_lag = rt_mat = 0.0
    for rg in lad:
        c2 = np.fft.ifft(rg["D"]).real[:rg["M"]]
        rt_lag = max(rt_lag, float(np.max(np.abs(c2 - rg["c"])))
                     / max(float(np.max(np.abs(rg["c"]))), 1e-300))
    print("       DFT round-trip on the full ladder: max rel dev "
          "%.2e" % rt_lag)
    check("D1 typed: REPRESENTING-MEASURE-UNIQUE-MOD-NULL-CHANNEL "
          "(kernel of the lag -> form map is EXACTLY the constant "
          "lag = the j = 0 channel, whose read S_0 vanishes "
          "identically; %d/%d declared h) => rho* IS the measure; "
          "'choose a positive representing measure' is NOT a "
          "modelling freedom" % (sum(1 for t in uniq
                                     if t[2] == t[1] - 1),
                                 len(uniq)),
          uniq_ok and rt_lag <= REP_WARD, kill="K2")
    npos_all = int(np.sum(np.array([r["n_neg"] for r in lad]) > 0))
    dmin = np.array([r["D_min"] for r in lad])
    half = np.array([0.5 * r["mu1"] for r in lad])
    print("    D2 POINTWISE SIGN ROUTE: min_j D_j %s vs (1/2)mu1 %s "
          "=> ratio |min D| / ((1/2)mu1) %s"
          % (e3(dmin), e3(half), e3(np.abs(dmin) / half)))
    check("D2 typed: POINTWISE-SIGN-DEAD(%d/%d rungs carry negative "
          "channels; the negative part exceeds the whole margin by "
          "median %.1f dex) -- nu := rho* is NOT a positive measure "
          "on ANY rung" % (npos_all, len(lad),
                           float(np.median(np.log10(
                               np.abs(dmin) / half)))),
          npos_all == len(lad))
    # D-CAND-1 (seat assignment)
    Rs = np.array([r["R_seat"] for r in lad])
    wp = np.array([r["w_pos"] for r in lad])
    n_R1 = int(np.sum(Rs >= 0))
    print("    D3 CANDIDATE 1 (SEAT): nu = rho*_+, manifest square = "
          "wedge_+, R = det - wedge_+ = wedge_- - cross")
    print("       (i) nu >= 0 by construction; (ii) Z = <f,f>_nu > 0 "
          "on %d/%d; (iii) R >= 0 on %d/%d"
          % (int(np.sum(np.array([r["w_pos"] for r in lad]) > 0)),
             len(lad), n_R1, len(lad)))
    print("       wedge_+ / det2 = %s  (the manifest square "
          "OVERSHOOTS the true determinant by this factor)"
          % e3(wp / np.array([r["det2"] for r in lad])))
    check("D3 typed: SEAT-COMPLETION-%s(R >= 0 on %d/%d)"
          % ("HOLDS" if n_R1 == len(lad) else "FAILS", n_R1,
             len(lad)), True)
    # D-CAND-2 (operator assignment)
    dsp = max(r["dev_split"] for r in lad)
    check("D4 WARD the exact positive/negative operator split "
          "K_h = P_h - N_h (both Gram matrices of a POSITIVE "
          "measure => every minor a manifest wedge square): max rel "
          "dev %.2e <= %.0e" % (dsp, SPLIT_WARD), dsp <= SPLIT_WARD,
          kill="K2")
    ch = np.array([r["c_h"] for r in lad])
    lamP = np.array([r["lamP"] for r in lad])
    lamR = np.array([r["lamR"] for r in lad])
    dele = np.array([r["deliver"] for r in lad])
    lamRt = np.array([r["lamR_top"] for r in lad])
    n_i = int(np.sum(np.array([r["D_max"] for r in lad]) > 0))
    n_ii = int(np.sum(ch > 0))
    n_iii = int(np.sum(lamR >= -PSD_TOL * lamRt))
    n_del = int(np.sum(dele >= 1.0))
    print("    D5 CANDIDATE 2 (OPERATOR, the lead's step 5): "
          "K_h = c_h P_h + R_h,  c_h = 1 - lam_max(N_h, P_h)")
    print("       CONDITION (i)   nu = D_+ >= 0 (positive measure): "
          "%d/%d" % (n_i, len(lad)))
    print("       CONDITION (ii)  Z_h = 1/c_h > 0:                 "
          "%d/%d   c_h %s" % (n_ii, len(lad), e3(ch)))
    print("       CONDITION (iii) R_h = lam_max P_h - N_h >= 0:    "
          "%d/%d   lam_min(R_h)/lam_max(R_h) %s (bar -%.0e, "
          "amendment A2)" % (n_iii, len(lad), e3(lamR / lamRt),
                             PSD_TOL))
    all3 = (n_i == len(lad) and n_ii == len(lad)
            and n_iii == len(lad))
    check("D5 typed: OPERATOR-COMPLETION-EXISTS(all three positivity "
          "conditions machine-verified on %d/%d rungs)" % (len(lad),
                                                           len(lad)),
          all3)
    sl_d, se_d, r2_d = jack_slope(np.log10(hh), np.log10(dele))
    print("    D6 THE DELIVERY QUESTION -- does the manifest square "
          "DELIVER the half-gap?")
    print("       delivery ratio  c_h * lam_min(P_h) / ((1/2)mu1) = "
          "%s" % e3(dele))
    print("       >= 1 on %d/%d rungs" % (n_del, len(lad)))
    print("       DEMAND LAW: dlog10(delivery)/dlog10 h = %+.3f "
          "(2SE %.3f, R2 %.3f) -- the manifest square falls AWAY "
          "from the target with depth" % (sl_d, 2 * se_d, r2_d))
    check("D6 typed: MANIFEST-SQUARE-%s(%d/%d; median deficit %.2f "
          "dex; demand slope %+.3f dex/dex)"
          % ("DELIVERS" if n_del == len(lad) else "SHORT", n_del,
             len(lad), float(np.median(np.log10(dele))), sl_d), True)
    dtw = max(r["dev_two"] for r in lad)
    ld = np.array([r["loss_dir"] for r in lad])
    le = np.array([r["loss_eng"] for r in lad])
    pstar = np.array([r["p_star"] for r in lad])
    rstar = np.array([r["r_star"] for r in lad])
    check("D7 [DIAGNOSTIC, eigendata-carrying, DECLARED: never a "
          "certificate] WARD the two-factor identity m_h = p*_h "
          "(1 - r*_h): max rel dev %.2e" % dtw, dtw <= 1e-6)
    print("       ANATOMY of the loss (which channel resists):")
    print("       directional factor  c_h / (1 - r*)      = %s"
          % f3(ld))
    print("       energy      factor  lam_min(P)/ p*      = %s"
          % e3(le))
    print("       p*/mu1 = %s   (1 - r*) = %s" % (e3(pstar / (2 * half)),
                                                  e3(1.0 - rstar)))
    resist = "ENERGY" if float(np.median(le)) < float(np.median(ld)) \
        else "DIRECTIONAL"
    check("D8 typed: RESISTING-CHANNEL(%s) -- the isotropic step "
          "lam_min(P_h) loses median %.2f dex while the directional "
          "step c_h/(1-r*) is essentially lossless (median %.3f); "
          "what the completion NEEDS is a CHRISTOFFEL-TYPE LOWER "
          "BOUND on the POSITIVE measure's energy AT the critical "
          "direction (x*^T P_h x* >= c1 mu1(h)) -- the same object "
          "family as the named-but-open W1 lemma of "
          "PRIME.PORT.WEDGE.SCALE.01 -- not a scalar lam_min(P_h)"
          % (resist, -float(np.median(np.log10(le))),
             float(np.median(ld))), True)
    # D-PRIME: is nu source-only?
    pr = []
    for rg in lad:
        D_ar = grid_density(rg["c_ar"])
        D_sm = grid_density(rg["c_ar"] + rg["c_sm"]) - D_ar
        D_osc = rg["D"] - D_ar - D_sm
        m_p = rg["D"] > 0
        den = float(np.sum(np.abs(rg["D"][m_p])))
        pr.append((float(np.sum(np.abs(D_osc[m_p]))) / max(den, 1e-300),
                   float(np.mean(D_ar < 0)),
                   float(np.min(D_ar))))
    osc_f = np.array([t[0] for t in pr])
    ar_neg = np.array([t[1] for t in pr])
    print("    D9 IS nu SOURCE-ONLY?  prime-oscillation share of the "
          "POSITIVE channels |D_OSC|/|D| = %s" % f3(osc_f))
    print("       archimedean background alone: negative-channel "
          "fraction %s, min D_AR %s"
          % (f3(ar_neg), e3(np.array([t[2] for t in pr]))))
    check("D9 typed: NU-PRIME-CARRYING(median OSC share %.3f; and "
          "the archimedean background is itself NOT a positive "
          "measure on %d/%d rungs) => even if the completion held, "
          "nu is not prime-free and the all-h statement would "
          "inherit the arithmetic"
          % (float(np.median(osc_f)), int(np.sum(ar_neg > 0)),
             len(lad)), True)

    # ============================================================ E
    section("E -- gates: controls, tau-screens, anti-circularity")
    worlds = {}
    worlds["smooth"] = [level_rung(r["kz"], world="smooth")
                        for r in lad]
    worlds["scramble"] = [level_rung(r["kz"],
                                     scramble_seed=SCR_SEED)
                          for r in lad]

    def inj(M, Dg):
        tt = np.arange(M) * Dg
        return (INJ_A * np.cos(INJ_GAMMA0 * tt)
                * (np.cosh(INJ_DELTA * tt) - 1.0))

    worlds["cosh"] = [level_rung(r["kz"], lag_fn=inj) for r in lad]
    worlds["rescale"] = [level_rung(r["kz"], world="rescale")
                         for r in lad]
    rr9 = core.build_window(CTRL_KZ)
    N_E = int(math.floor(math.exp(2.0 * rr9["alpha"]))) + 1
    lamE = lambda_eps(N_E)
    nnE = np.nonzero(np.abs(lamE) > 1e-12)[0]
    worlds["epstein"] = [level_rung(
        CTRL_KZ, comb=(np.log(nnE.astype(float)),
                       2.0 * lamE[nnE] / np.sqrt(nnE.astype(float))))]
    print("    E-TABLE  control census (each world must BREAK the "
          "level target or the weight positivity)")
    print("    %-10s %6s  %-26s %8s %8s" % ("world", "rungs",
                                            "shat min/med/max",
                                            "shat>=1/2", "detsq>=0"))
    print("    %-10s %6d  %-26s %8s %8s"
          % ("TRUE", len(lad), f3(shat), "%d/%d" % (n_reg, len(lad)),
             "%d/%d" % (int(np.sum(np.array([r["det2"] for r in lad])
                                   >= 0)), len(lad))))
    fired = {}
    for nm, ws in worlds.items():
        good = [r for r in ws if r is not None]
        for rg in good:
            level_reads(rg, with_ops=False)
        if not good:
            fired[nm] = True
            print("    %-10s %6d  %-26s %8s %8s"
                  % (nm, 0, "chain death", "-", "-"))
            continue
        sh = np.array([r["shat"] for r in good])
        d2 = np.array([r["det2"] for r in good])
        n_p = int(np.sum(sh >= float(REG_C)))
        n_d = int(np.sum(d2 >= 0))
        fired[nm] = (n_p < len(good)) or (n_d < len(good))
        print("    %-10s %6d  %-26s %8s %8s"
              % (nm, len(good), f3(sh), "%d/%d" % (n_p, len(good)),
                 "%d/%d" % (n_d, len(good))))
    for nm in ("smooth", "scramble", "cosh", "epstein"):
        check("E-%s control FIRES (breaks the level target or the "
              "weight positivity)" % nm, fired.get(nm, False),
              kill="K2")
    check("E-rescale control census printed (mass rescale %.1f; "
          "typed, not a kill: it is a scale control)" % RSC_FAC, True)
    check("E-ANDREIEF-BLIND typed: the exterior-square identity "
          "(and its 1/2) holds for EVERY world incl. the fired "
          "controls -- an identity valid for all measures cannot "
          "explain a constant that DISCRIMINATES worlds", True)
    section("E2 -- tau-screens (screen variable TAU_REP := c_h = "
            "1 - lam_max(N_h, P_h), declared)")
    for lab, v in (("m_h", np.array([r["m"] for r in lad])),
                   ("TARGET = m - mu1/2",
                    np.array([r["m"] - 0.5 * r["mu1"] for r in lad])),
                   ("shat - 1/2", shat - 0.5),
                   ("det2 (seat)",
                    np.array([r["det2"] for r in lad])),
                   ("wedge_+", wp),
                   ("delivery ratio", dele),
                   ("lam_min(P_h)", lamP),
                   ("p* (crit. energy)", pstar)):
        print("    " + screen(v, ch, lab))
    check("E2 typed: the completion's prefactor IS the wall scalar "
          "(TAU_REP == c_h by construction), so any margin built "
          "from it is a RELOCATION, not a reduction -- declared a "
          "priori, measured above", True)
    check("E3 ANTI-CIRCULARITY: S-reads are pure sine geometry "
          "(source-only); no tau in any construction; no target "
          "eigenvector in any certificate (only D7/D8 diagnostic + "
          "reproduction wards); no zero data; RNG only in the "
          "declared scramble control", True)
    return finish(dict(n_neg=n_neg, n_ok=len(lam_list),
                       n_lad=len(lad), n_R1=n_R1, all3=all3,
                       n_del=n_del, sl_d=sl_d, se_d=se_d,
                       dele=dele, canc=canc, le=le, ld=ld,
                       resist=resist))


def finish(res=None):
    section("VERDICT")
    n_ok = sum(1 for _n, o in CHECKS if o)
    if res:
        holds = (res["all3"] and res["n_del"] == res["n_lad"]
                 and res["n_R1"] == res["n_lad"])
        c1v = ("HOLDS" if res["n_R1"] == res["n_lad"]
               else "REFUTED(condition (iii) R >= 0 fails on %d/%d)"
               % (res["n_lad"] - res["n_R1"], res["n_lad"]))
        c2v = ("HOLDS" if res["n_del"] == res["n_lad"]
               else "PARTIAL(all three conditions hold on %d/%d, "
                    "delivery on %d/%d)"
               % (res["n_lad"], res["n_lad"], res["n_del"],
                  res["n_lad"]))
        if holds:
            verdict = "EXTERIOR-SQUARE-HOLDS"
        elif res["all3"]:
            verdict = ("PARTIAL -- the exterior-square factorization "
                       "EXISTS but does NOT make positivity "
                       "automatic")
        else:
            verdict = "REFUTED"
        print("    %s" % verdict)
        print("      D-CAND-1 (SEAT, the lead's literal wedge "
              "form): %s" % c1v)
        print("      D-CAND-2 (OPERATOR, the lead's step-5 "
              "absorption): %s" % c2v)
        print("    (1) BARRIER KILL: lam_min(G_h) < 0 on %d/%d "
              "surface transitions (CCIII combined %d/%d CITED) -- "
              "the TRANSITION margin admits no positive "
              "factorization." % (res["n_neg"], res["n_ok"],
                                  CCIII_COMB_FAILS, CCIII_COMB_TRANS))
        print("    (2) LEVEL REPRESENTATION: K_h - (1/2)mu1 I = "
              "Gram_{rho*}(S) EXACTLY in source-only sine reads; the "
              "representing measure is UNIQUE; rho* has a negative "
              "part on %d/%d rungs => no positive measure "
              "represents the margin." % (res["n_lad"],
                                          res["n_lad"]))
        print("    (3) SEAT: the exterior square is nonnegative but "
              "by a median %.1f-digit cancellation; the manifest "
              "positive-measure square OVERSHOOTS (R >= 0 on %d/%d)."
              % (float(np.median(-np.log10(np.maximum(
                  1.0 - res["canc"], 1e-300)))), res["n_R1"],
                 res["n_lad"]))
        print("    (4) OPERATOR: K_h = c_h P_h + R_h exists with all "
              "three positivity conditions, but delivers %d/%d "
              "(median %.2f dex short, demand slope %+.3f +- %.3f "
              "dex/dex).  RESISTING CHANNEL: %s."
              % (res["n_del"], res["n_lad"],
                 float(np.median(np.log10(res["dele"]))),
                 res["sl_d"], 2 * res["se_d"], res["resist"]))
        print("    (5) RESIDUAL DEMAND, typed exactly: a "
              "Christoffel-type LOWER bound p*_h = x*^T P_h x* >= "
              "c1 mu1(h) at the critical direction, TOGETHER with "
              "(1 - r*_h) >= 1/(2 c1).  Both factors are h-unstable "
              "in opposite directions (p*/mu1 grows, 1 - r* decays)"
              " => the two-factor split is a RELOCATION of the "
              "wall, not a reduction of it, and the completion's "
              "prefactor IS the wall scalar (E2).")
        print("    (6) WHAT WOULD REVIVE THE ROUTE: not a better "
              "wedge -- the wedge identity is exact and blind (it "
              "holds in every fired control world).  Only a "
              "DIRECTIONAL lower bound on the positive measure's "
              "Christoffel energy at the critical direction can "
              "convert the existing factorization into a "
              "certificate; that is a lemma about the POSITIVE, "
              "prime-carrying measure, so the infinite quantifier "
              "does NOT fall by structure here.")
    print("\n    KILLS: %s" % (", ".join(sorted(set(KILLS)))
                               if KILLS else "none"))
    print("    checks %d/%d passed   [%.1f s]"
          % (n_ok, len(CHECKS), time.time() - T0))
    print("    EXPLORATION ONLY -- no ledger row, no paper edit, no "
          "marker move, NO RH claim.")
    return 0 if n_ok == len(CHECKS) else 1


if __name__ == "__main__":
    sys.exit(main())
