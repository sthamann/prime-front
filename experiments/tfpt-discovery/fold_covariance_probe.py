#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""fold_covariance_probe -- PRIME.BIGPICTURE.FOLDCOV.01
(EXPLORATION ONLY, experiments/; the ONE discriminating probe of the
CCCLI candidate principle: is the 1/2 in the registered HALFGAP target
m_h >= (1/2) mu1(h) the SELF-PAIRING FACTOR of the two-arm fold
(pairing provenance, CCCXXV H1/H2) or just a pattern we like?  The
test PREDICTS a NEW number instead of explaining an old one: for
k = 2 (control), 3, 4 the orbit compression of a k-arm fold of the
SAME deployed window must saturate against a constant c_k and a
symbol mu^(k) that are derived SYMBOLICALLY BEFORE ANY LADDER READ.
2026-08-13.)

NO RH claim.  No marker moves.  verification/ is imported READ-ONLY.
Writes nothing but stdout.
"""

import ast
import hashlib
import inspect
import math
import os
import sys
import time
from fractions import Fraction

import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
_VERIFY = os.path.abspath(os.path.join(_HERE, "..", "..",
                                       "verification"))
sys.path.insert(0, _HERE)
sys.path.insert(0, _VERIFY)

import v563_paper2_readouts as core                  # noqa: E402 RO
import exterior_square_factorization_probe as esq    # noqa: E402 RO

FROZEN_SPEC = """\
PRIME.BIGPICTURE.FOLDCOV.01 -- frozen spec v1 (2026-08-13).

THE QUESTION (CCCLI K1).  The registered HALFGAP target (CLI, CCCXXV)
reads m_h = lam_min(odd_toeplitz(c_ar + c_at, M)) >= (1/2) mu1(h),
mu1(h) = 4 sin^2(pi/(2h+1)).  CCCXXV H1/H2 located the 1/2 on the
representation side: the two-arm fold j <-> L-j of the periodic lag
completion halves the Plancherel identity EXACTLY, and (1/2) mu1 =
1 - cos(2 pi/N) is the second-difference symbol at the fundamental
window frequency.  The CCCLI candidate principle says the 1/2 IS the
self-pairing factor of that fold.  If so, a k-arm fold of the SAME
window must deliver a pre-derivable constant c_k and symbol mu^(k)
against which the saturation transports; if the 1/2 is only a
pattern, some k will need a different constant or break the profile.

THE DEPLOYED FOLD, RESTATED EXACTLY (position side; warded, not
assumed).  With L2 = 2M - 2 and a = the even L2-periodic completion
of the lag vector c (grid_density input, deployed verbatim), the
deployed wall is the orbit compression of the circulant A = Circ(a)
under the order-2 fold group G_2 = {id, rho}, rho(p) = (M-1) - p
(free involution), with the sign character:
    K = (1/2) F_2^T A F_2,   F_2 = E0 - U_rho E0,   F_2^T F_2 = 2 I,
E0 = the one-arm window embedding (identity on positions 0..h-1).
The 1/2 is manifestly 1/|G_2| -- THE SELF-PAIRING FACTOR.  This
reproduces odd_toeplitz(c, M) EXACTLY (ward <= 1e-12) and the CCCXXV
H1 channel identity is re-warded verbatim.

THE k-ARM FOLDS (frozen constructions; the family parameter k =
|fold group| = number of arms).  All use the SAME lag vector c
(deployed, read-only) on a k-compatible even completion a with
a_m = c_|m| for |m| <= M-1 and 0 on padded slots (wall-invariance is
exact by construction and warded):
  k = 2 : L2 = 2M - 2 (deployed, no padded slot), G_2 as above.
          CONTROL: must reproduce the deployed 1/2 and mu1 EXACTLY.
  k = 3 : L3 = smallest multiple of 3 >= 2M - 1; G_3 = the literal
          3rd ROTATION subgroup {id, tau, tau^2}, tau = shift by
          L3/3; character chi(tau) = omega = exp(2 pi i/3) (frozen;
          the conjugate character gives the conjugate spectrum).
          (A 3-arm fold containing the deployed reflection cannot
          exist: any reflection-containing subgroup of the dihedral
          group has even order -- disclosed, one-line group theory.)
  k = 4 : L4 = 2M (one padded slot a_M = 0); G_4 = the Klein group
          {id, sigma, rho, sigma rho}, sigma = shift by L4/2 = M --
          the 2nd rotation subgroup adjoined to the deployed fold;
          character chi(sigma) = -1, chi(rho) = -1 (the fully
          twisted sector; frozen).  All three actions are FREE.
The orbit compression, uniformly:
    K^(k) = (1/k) F_k^H A^(k) F_k,  F_k = sum_g conj(chi(g)) U_g E0,
and the self-pairing normalization F_k^H F_k = k I is EXACT (ward).

PRE-FREEZE SYMBOLIC PREDICTIONS (sympy tier runs BEFORE any ladder
read; closed forms frozen here, certified exactly on small h and
re-tied numerically on the ladder):
    c_k = Fraction(1, k)          (the Plancherel-halving analogue),
    mu^(k)_h = the fundamental eigenvalue of K^(k)[Delta], the
    k-compressed second difference (Delta lags (2, -1, 0, ...)):
      mu^(2)_h = 4 sin^2(pi/(2h+1))   == deployed mu1 (control),
      mu^(3)_h = 4 sin^2(pi/(2h+2)),
      mu^(4)_h = 4 sin^2(pi/(4h)).
Certification: exact charpoly membership (sympy, Rational/omega
arithmetic) on h in {4, 5, 6} plus 40-digit smallest-root isolation
(mpmath); per ladder rung the numeric fundamental eigenvalue of
K^(k)[Delta] must tie the closed form to <= 1e-10 relative on the
declared subset.  The derivation source is hashed (SYMB_SHA printed;
the run fails if it does not match the frozen value below).
    SYMB_SHA (frozen) = 056b5f81e331fd68

THE LADDER READS (only AFTER the symbolic tier).  Faithful rungs
verbatim from the registered halfgap surface (v563 build_window,
kz 2..150, H_MIN/HCAP/ATOM_MAX filters).  Read subset, frozen: the
NREAD = 40 faithful rungs of smallest h, in (h, kz) order, PLUS the
registered tightest rung kz 98 if faithful (depth witness).  Per
rung and per k:
    s^(k)_h = lam_min(K^(k)[c]) / mu^(k)_h,
    q^(k)_h = s^(k)_h / c_k      (normalized saturation ratio;
    q^(2) = 2 shat reproduces the deployed read EXACTLY -- ward).
SATURATION TRANSPORT, frozen BEFORE any k >= 3 read (no refit):
    SAT(k)  iff  min_h q^(k) >= 1   AND   trio(q^(k)) (min/med/max
    over the subset) lies elementwise in [REF_TRIO/2, REF_TRIO*2],
    REF_TRIO = 2 x (0.502, 1.027, 2.185) = (1.004, 2.054, 4.370)
    (the registered CXLIII shat band in q units -- the k = 2 margin
    profile; declared in advance, from the REGISTERED numbers, not
    from this run).

WARDS (all frozen; kill -> WARD-BROKEN unless typed per-k):
  F1 fold identity per k <= 1e-12: (a) F_k^H F_k == k I; (b) the
     O(k^2 h^2) lag-formula build == the independent FFT/circulant
     build on the declared subset; (c) k = 2 build == deployed
     odd_toeplitz; (d) CCCXXV H1 arm identity verbatim at k = 2;
     (e) Hermiticity <= 5e-13.
  F2 AST scan, source-only: the PREDICTION path (c_pair, mu_closed,
     fold_group, exact_fold_matrix, symbolic_tier) sees no tau, no
     shat, no margin, no m_h, no atom/prime/comb name.
  F3 the symbolic derivation is SHA-frozen (SYMB_SHA above).
  F4 DOCTORED FOLD (non-vacuity): a wrong orbit representative
     (k = 2: reflection center M for M-1; k = 3: second arm at
     L3/3 + 1; k = 4: sigma at M + 1) must shift the measured
     lam_min by >= 1e-6 relative at the declared doctor rung
     (kz 26); silence -> VACUOUS-INSTRUMENT (kill).
  W  deployed reproduction: >= 40 faithful rungs; m_h > 0
     everywhere; mu1 closed form == core.parity_mu on the subset
     (<= 1e-12); margin exponent in [-2.5, -1.5]; full-ladder shat
     trio == (0.502, 1.027, 2.185) (rtol 2e-2).
  P  precision tier (declared): reads are float64-assembly reads on
     the deployed surface (CCCXXIII disclosure applies); for the 3
     tightest rungs per k the eigenpair residual r = ||Kv - lam v||
     is printed and the margin must exceed 100 r / (c_k mu^(k))
     (typed CERT-OK / CERT-THIN, never kill: these reads are not
     sign(Delta_h)-bearing).

CONTROLS (must break saturation in EVERY k, as they do for k = 2):
Epstein x^2 + 5y^2 comb and position scramble (seed 1) at kz 9;
smooth world (2 e^{u/2} du) at kz in {9, 26, 60}.  Required:
q^(k)_ctrl < 1 for every control and every k.  A control that
SATISFIES the target types CONTROLS-NON-DISCRIMINATING(k) -- a
first-class finding; that k is excluded from the verdict census.

KILL CRITERIA (frozen enum, CCCLI):
  PAIRING-PROVENANCE  iff k = 3 AND k = 4 both admit the fold
      construction (wards F1 pass) and SAT(3) and SAT(4) hold with
      clean controls -- the 1/2 transports as the self-pairing
      factor of the fold family;
  PATTERN-ONLY (the principle is DEAD)  iff some admitted k >= 3
      with clean controls fails SAT(k) -- that k needs a different
      constant or breaks the k = 2 saturation profile;
  INSTRUMENT-EDGE  iff a fold construction refuses (ward F1 fails
      structurally for that k) -- documented per k, no verdict from
      that k; overall INSTRUMENT-EDGE if no k >= 3 admits.
Hard kills: PIPELINE-BROKEN (< 40 rungs), WARD-BROKEN (W wards,
k = 2 control wards), VACUOUS-INSTRUMENT (F4 silent).

HONEST FRAME, frozen with the spec: even PAIRING-PROVENANCE supplies
NO independent source for sign(Delta_h) and falls under the frozen
gate rule -- it would type the CCCLI principle as a PROGRAM
ORGANIZER, not as progress; PATTERN-ONLY kills the principle.  The
k >= 3 folds are NEW objects built by this probe from the deployed
window; the deployed surface itself is untouched and read-only.

SMOKE DISCLOSURE.  Smoke rounds (TFPT_FC_SMOKE=1, reduced kz range,
8 read rungs) were run before freezing to shake out build errors.
No bar, band, constant, enum or verdict rule was changed after
seeing a frozen number.  Runtime cap declared: 30 min.
"""

# ---------------------------------------------------------------- frozen
SMOKE = bool(os.environ.get("TFPT_FC_SMOKE"))
KZMAX = 40 if SMOKE else 150
MIN_RUNGS = 4 if SMOKE else 40
NREAD = 8 if SMOKE else 40
TIGHT_KZ = 98            # registered tightest rung (halfgap R3)
SUBSET_KZ = (9, 13, 26, 40, 60, 90, 121)
CTRL_KZ = 9
CTRL_SMOOTH_KZ = (9, 26, 60)
DOCTOR_KZ = 26
SCR_SEED = 1
NG_SMOOTH = 6000
MU_WARD = 1.0e-12
FOLD_WARD = 1.0e-12
HERM_WARD = 5.0e-13
MU_TIE = 1.0e-10
DOCT_BAR = 1.0e-6
RESID_FACTOR = 100.0
EXPO_BAND = (-2.5, -1.5)
SHAT_REF = (0.502, 1.027, 2.185)
SHAT_RTOL = 2.0e-2
REF_TRIO = (1.004, 2.054, 4.370)   # 2 x SHAT_REF, the k=2 profile
BAND_FAC = 2.0
KLIST = (2, 3, 4)
SYMB_SHA_FROZEN = "056b5f81e331fd68"
RUNTIME_CAP = 1800.0
BANNED_IDS = ("zetazero", "nzeros", "primerange", "isprime",
              "primepi", "nextprime", "prevprime")
PRED_BANNED = ("tau", "shat", "margin", "m_h", "lam_min", "atom",
               "prime", "comb", "osc", "c_at", "verdict", "target")
PRED_FNS = ("c_pair", "mu_closed", "fold_group",
            "exact_fold_matrix", "symbolic_tier")

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


def pred_path_scan():
    """F2: the prediction path may not mention tau/shat/margin or any
    prime-side name (source-only, exact-identifier match)."""
    src = open(os.path.abspath(__file__), encoding="utf-8").read()
    bad = []
    for node in ast.walk(ast.parse(src)):
        if not isinstance(node, ast.FunctionDef):
            continue
        if node.name not in PRED_FNS:
            continue
        for sub in ast.walk(node):
            nm = None
            if isinstance(sub, ast.Name):
                nm = sub.id
            elif isinstance(sub, ast.Attribute):
                nm = sub.attr
            if nm and nm.lower() in PRED_BANNED:
                bad.append("%s:%s" % (node.name, nm))
    return bad


def trio(v):
    v = np.asarray(v, float)
    return float(np.min(v)), float(np.median(v)), float(np.max(v))


def jack_fit(x, y):
    x = np.asarray(x, float)
    y = np.asarray(y, float)
    vx = float(np.var(x))
    b = float(np.cov(x, y, bias=True)[0, 1] / vx)
    return b


# ==================================================== PREDICTION PATH
# (AST-warded: sees only k, h, M -- pure fold geometry, no window
#  data, no arithmetic, no measured object.)
def c_pair(k):
    """The Plancherel-halving analogue: the self-pairing factor of
    the k-arm fold, 1/|G_k| as an exact Fraction."""
    return Fraction(1, k)


def mu_closed(k, h):
    """The frozen closed form of the fundamental symbol of the
    k-compressed second difference (certified by symbolic_tier)."""
    den = {2: 2 * h + 1, 3: 2 * h + 2, 4: 4 * h}[k]
    return 4.0 * math.sin(math.pi / den) ** 2


def fold_group(k, M):
    """The frozen k-arm fold group on the k-compatible completion:
    a list of affine maps p -> (s p + t) mod L with characters chi.
    k = 2 is the deployed two-arm fold (control)."""
    if k == 2:
        L = 2 * M - 2
        G = ((1, 0), (-1, M - 1))
        chi = (1.0 + 0.0j, -1.0 + 0.0j)
    elif k == 3:
        L = 3 * ((2 * M - 1 + 2) // 3)
        w = complex(math.cos(2.0 * math.pi / 3.0),
                    math.sin(2.0 * math.pi / 3.0))
        G = ((1, 0), (1, L // 3), (1, 2 * L // 3))
        chi = (1.0 + 0.0j, w, w * w)
    elif k == 4:
        L = 2 * M
        G = ((1, 0), (1, M), (-1, M - 1), (-1, 2 * M - 1))
        chi = (1.0 + 0.0j, -1.0 + 0.0j, -1.0 + 0.0j, 1.0 + 0.0j)
    else:
        raise ValueError(k)
    return G, chi, L


def exact_fold_matrix(k, h, sp):
    """K^(k)[Delta] built EXACTLY (sympy Rational / omega arithmetic)
    with the identical group logic -- the symbolic-tier object."""
    M = 2 * h
    if k == 2:
        L = 2 * M - 2
        G = ((1, 0), (-1, M - 1))
        chi = (sp.Integer(1), sp.Integer(-1))
    elif k == 3:
        L = 3 * ((2 * M - 1 + 2) // 3)
        w = sp.exp(2 * sp.pi * sp.I / 3)
        G = ((1, 0), (1, L // 3), (1, 2 * L // 3))
        chi = (sp.Integer(1), w, w ** 2)
    else:
        L = 2 * M
        G = ((1, 0), (1, M), (-1, M - 1), (-1, 2 * M - 1))
        chi = (sp.Integer(1), sp.Integer(-1), sp.Integer(-1),
               sp.Integer(1))
    a = {0: sp.Integer(2), 1: sp.Integer(-1),
         L - 1: sp.Integer(-1)}

    def aval(m):
        return a.get(int(m) % L, sp.Integer(0))

    K = sp.zeros(h, h)
    for (s1, t1), x1 in zip(G, chi):
        for (s2, t2), x2 in zip(G, chi):
            cc = sp.simplify(x1 * sp.conjugate(x2))
            for p in range(h):
                gp = (s1 * p + t1) % L
                for q in range(h):
                    gq = (s2 * q + t2) % L
                    K[p, q] += cc * aval(gp - gq)
    K = (K / k).applyfunc(sp.simplify)
    return K


def symbolic_tier():
    """Certify c_k and mu^(k) BEFORE any ladder read: exact charpoly
    membership of the closed form on h in {4, 5, 6} plus 40-digit
    smallest-root isolation.  Returns (ok, detail lines)."""
    import sympy as sp
    import mpmath as mp
    lines = []
    ok = True
    x = sp.symbols("x")
    for k in (2, 3, 4):
        for h in (4, 5, 6):
            den = {2: 2 * h + 1, 3: 2 * h + 2, 4: 4 * h}[k]
            root = 2 - 2 * sp.cos(2 * sp.pi / den)
            K = exact_fold_matrix(k, h, sp)
            herm = sp.simplify(K - K.H)
            ok &= herm == sp.zeros(h, h)
            p = K.charpoly(x).as_expr()
            val = sp.simplify(p.subs(x, root))
            member = sp.simplify(sp.nsimplify(val)) == 0 or \
                sp.simplify(val) == 0
            if not member:
                member = abs(complex(val.evalf(50))) < 1e-40
            ok &= bool(member)
            mp.mp.dps = 45
            coeffs = [mp.mpf(str(c)) for c in
                      sp.Poly(p, x).all_coeffs()]
            roots = [r.real for r in mp.polyroots(coeffs, maxsteps=200,
                                                  extraprec=200)
                     if abs(r.imag) < mp.mpf("1e-35")]
            small = min(roots)
            closed = 4 * mp.sin(mp.pi / den) ** 2
            iso = abs(small - closed) < mp.mpf("1e-35")
            ok &= bool(iso)
            lines.append("k=%d h=%d: charpoly(mu^(k)) == 0 %s, "
                         "smallest root == closed form to 1e-35 %s"
                         % (k, h, member, iso))
    return ok, lines


# ================================================== MEASUREMENT PATH
def lag_completion(cvec, M, L):
    """Even completion of the lag vector on Z_L: a_m = c_|m| for
    |m| <= M-1, zero on padded slots."""
    a = np.zeros(L)
    a[:M] = cvec
    a[L - M + 1:] = cvec[1:][::-1]
    return a


def fold_wall(cvec, M, k, doctor=False):
    """K^(k) = (1/k) F^H A F via the O(k^2 h^2) lag formula.
    doctor=True plants the wrong orbit representative (F4)."""
    h = M // 2
    G, chi, L = fold_group(k, M)
    if doctor:
        G = list(G)
        if k == 2:
            G[1] = (-1, M)
        elif k == 3:
            G[1] = (1, L // 3 + 1)
        else:
            G[1] = (1, M + 1)
        G = tuple(G)
    a = lag_completion(cvec, M, L)
    pp = np.arange(h)
    K = np.zeros((h, h), complex)
    for (s1, t1), x1 in zip(G, chi):
        gp = (s1 * pp + t1) % L
        for (s2, t2), x2 in zip(G, chi):
            gq = (s2 * pp + t2) % L
            K += (x1 * np.conj(x2)) * a[(gp[:, None] - gq[None, :]) % L]
    K /= k
    herm = float(np.max(np.abs(K - K.conj().T))) / max(
        float(np.max(np.abs(K))), 1e-300)
    K = 0.5 * (K + K.conj().T)
    if float(np.max(np.abs(K.imag))) <= 1e-14 * max(
            float(np.max(np.abs(K.real))), 1e-300):
        K = K.real.copy()
    return K, herm


def fold_wall_fft(cvec, M, k):
    """Independent route: dense F on Z_L, circulant apply by FFT."""
    h = M // 2
    G, chi, L = fold_group(k, M)
    a = lag_completion(cvec, M, L)
    F = np.zeros((L, h), complex)
    pp = np.arange(h)
    for (s, t), x in zip(G, chi):
        F[(s * pp + t) % L, pp] += np.conj(x)
    AF = np.fft.ifft(np.fft.fft(a)[:, None]
                     * np.fft.fft(F, axis=0), axis=0)
    K = (F.conj().T @ AF) / k
    gram = (F.conj().T @ F) / k
    return K, gram


def delta_lags(M):
    c = np.zeros(M)
    c[0], c[1] = 2.0, -1.0
    return c


def smooth_comb(alpha, ng=NG_SMOOTH):
    ug = (np.arange(ng) + 0.5) * (2.0 * alpha / ng)
    return ug, 2.0 * np.exp(ug / 2.0) * (2.0 * alpha / ng)


def lambda_eps(N):
    r = np.zeros(N + 1)
    s = int(math.isqrt(N)) + 1
    for xx in range(-s, s + 1):
        for yy in range(-s, s + 1):
            v = xx * xx + 5 * yy * yy
            if 1 <= v <= N:
                r[v] += 1.0
    aa = r / 2.0
    lam = np.zeros(N + 1)
    for n in range(2, N + 1):
        acc = aa[n] * math.log(n)
        for dd in range(2, n):
            if n % dd == 0:
                acc -= lam[dd] * aa[n // dd]
        lam[n] = acc
    return lam


def build_rung(kz, scramble_seed=None):
    """One faithful halfgap rung, machinery verbatim (CXLIII /
    halfgap_registration): returns lag vector + deployed read."""
    try:
        rr = core.build_window(kz, scramble_seed=scramble_seed)
    except Exception:
        return None
    if not (core.H_MIN <= rr["h"] <= core.HCAP):
        return None
    if rr["X"] > core.ATOM_MAX:
        return None
    alpha, M, D, h = rr["alpha"], rr["M"], rr["D"], rr["h"]
    uu = np.asarray(rr["uu"], float)
    mm = 2.0 * np.asarray(rr["lam"], float)
    c_at = np.asarray(core.atom_lags_at(alpha, M, uu, mm)[0], float)
    c_ar = np.asarray(core.arch_lags(M, D), float)
    return dict(kz=kz, alpha=float(alpha), h=h, M=M,
                c=c_ar + c_at, c_ar=c_ar)


def q_read(cvec, M, h, k):
    """The k-fold ladder read: q^(k) = lam_min(K^(k)) / (c_k mu^(k))."""
    K, herm = fold_wall(cvec, M, k)
    lam = float(np.linalg.eigvalsh(K)[0])
    tgt = float(c_pair(k)) * mu_closed(k, h)
    return lam / tgt, lam, herm


def main():
    section("PRIME.BIGPICTURE.FOLDCOV.01 -- fold covariance of the "
            "HALFGAP 1/2: pairing provenance vs pattern "
            "(EXPLORATION ONLY)")
    spec_sha = hashlib.sha256(FROZEN_SPEC.encode("utf-8")).hexdigest()
    print("    FROZEN_SPEC SHA-256 = %s" % spec_sha)
    print("    NO RH claim; no marker moves.  Budget %.0f s.%s"
          % (RUNTIME_CAP, "  [SMOKE]" if SMOKE else ""))

    # ------------------------------------------------------------ S0
    section("S0 -- firewalls")
    check("S0.1 AST zero/prime-oracle firewall clean",
          not ast_scan(BANNED_IDS), kill="K2")
    bad = pred_path_scan()
    check("S0.2 F2 AST prediction-path scan: %s see no tau, no "
          "shat, no margin, no prime-side name" % (PRED_FNS,),
          not bad, ("" if not bad else "hits: %s" % bad), kill="K2")
    src = "".join(inspect.getsource(f) for f in
                  (c_pair, mu_closed, fold_group, exact_fold_matrix,
                   symbolic_tier))
    symb_sha = hashlib.sha256(src.encode("utf-8")).hexdigest()[:16]
    print("    SYMB_SHA (derivation source) = %s" % symb_sha)
    check("S0.3 F3 symbolic derivation hash matches the frozen spec "
          "value %s" % SYMB_SHA_FROZEN, symb_sha == SYMB_SHA_FROZEN,
          kill="K2")

    # ------------------------------------------------------------ S1
    section("S1 -- SYMBOLIC TIER (before any ladder read): c_k and "
            "mu^(k) certified exactly")
    print("    predictions, frozen: c_k = 1/k;  mu^(2) = "
          "4 sin^2(pi/(2h+1)) (deployed mu1),")
    print("    mu^(3) = 4 sin^2(pi/(2h+2)),  mu^(4) = "
          "4 sin^2(pi/(4h));  targets c_k mu^(k).")
    ok_sym, lines = symbolic_tier()
    for ln in lines:
        print("      " + ln)
    check("S1.1 exact charpoly membership + 40-digit smallest-root "
          "isolation on h in {4,5,6} for k in {2,3,4}", ok_sym,
          kill="K2")

    # ------------------------------------------------------------ S2
    section("S2 -- the deployed ladder (halfgap surface, verbatim) "
            "+ reproduction wards")
    rungs = []
    for kz in range(2, KZMAX + 1):
        r = build_rung(kz)
        if r is not None:
            r["m"] = float(np.linalg.eigvalsh(
                core.odd_toeplitz(r["c"], r["M"]))[0])
            r["mu1"] = mu_closed(2, r["h"])
            r["shat"] = r["m"] / r["mu1"]
            rungs.append(r)
    rungs.sort(key=lambda r: (r["h"], r["kz"]))
    check("W1 faithful ladder >= %d rungs" % MIN_RUNGS,
          len(rungs) >= MIN_RUNGS,
          "%d rungs, h %d..%d  [%.1f s]"
          % (len(rungs), rungs[0]["h"], rungs[-1]["h"],
             time.time() - T0), kill="K1")
    if KILLS:
        return finish("PIPELINE-BROKEN")
    ms = np.array([r["m"] for r in rungs])
    check("W2 WARD m_h > 0 everywhere (min %.3e)" % ms.min(),
          bool(np.all(ms > 0)), kill="K2")
    sub = [r for r in rungs if r["kz"] in SUBSET_KZ]
    tie = max(abs(r["mu1"] - float(core.parity_mu(r["h"])[0]))
              / r["mu1"] for r in sub) if sub else 1.0
    check("W3 WARD mu1 closed form == core.parity_mu on the subset "
          "(max rel %.2e <= %.0e)" % (tie, MU_WARD), tie <= MU_WARD,
          kill="K2")
    hh = np.array([float(r["h"]) for r in rungs])
    p_exp = jack_fit(np.log(hh), np.log(ms))
    check("W5 margin exponent %+.3f in [%.1f, %.1f]"
          % (p_exp, *EXPO_BAND),
          EXPO_BAND[0] <= p_exp <= EXPO_BAND[1] or SMOKE, kill="K2")
    shat = np.array([r["shat"] for r in rungs])
    tr = trio(shat)
    ok_band = all(abs(a / b - 1.0) <= SHAT_RTOL
                  for a, b in zip(tr, SHAT_REF))
    check("W6 full-ladder shat trio %.3f/%.3f/%.3f == "
          "%.3f/%.3f/%.3f (rtol %.0e)" % (tr + SHAT_REF + (SHAT_RTOL,)),
          ok_band or SMOKE, kill="K2")
    if KILLS:
        return finish("WARD-BROKEN")

    reads = rungs[:NREAD]
    if not any(r["kz"] == TIGHT_KZ for r in reads):
        tightr = [r for r in rungs if r["kz"] == TIGHT_KZ]
        reads = reads + tightr
    print("    read subset: %d rungs, h %d..%d (frozen rule: %d "
          "smallest-h + registered tightest kz %d)"
          % (len(reads), reads[0]["h"],
             max(r["h"] for r in reads), NREAD, TIGHT_KZ))

    # ------------------------------------------------------------ S3
    section("S3 -- F1 fold-identity wards per k (<= %.0e)"
            % FOLD_WARD)
    admitted = {}
    ward_sub = [r for r in reads if r["kz"] in SUBSET_KZ] or reads[:3]
    for k in KLIST:
        dev_gram = dev_fft = dev_dep = dev_mu = herm_max = 0.0
        okk = True
        for r in ward_sub:
            M, h = r["M"], r["h"]
            Kfft, gram = fold_wall_fft(r["c"], M, k)
            dev_gram = max(dev_gram, float(np.max(np.abs(
                gram - np.eye(h)))))
            Klag, herm = fold_wall(r["c"], M, k)
            herm_max = max(herm_max, herm)
            sc = max(float(np.max(np.abs(Klag))), 1e-300)
            dev_fft = max(dev_fft, float(np.max(np.abs(
                Klag - Kfft))) / sc)
            if k == 2:
                Kdep = core.odd_toeplitz(r["c"], M)
                dev_dep = max(dev_dep, float(np.max(np.abs(
                    Klag - Kdep))) / sc)
            KD, _ = fold_wall(delta_lags(M), M, k)
            mu_num = float(np.linalg.eigvalsh(KD)[0])
            dev_mu = max(dev_mu, abs(mu_num - mu_closed(k, h))
                         / mu_closed(k, h))
        okk &= check("F1.%d.a F^H F == %d I (self-pairing "
                     "normalization; max dev %.2e)"
                     % (k, k, dev_gram), dev_gram <= FOLD_WARD)
        okk &= check("F1.%d.b lag build == FFT build (max rel %.2e)"
                     % (k, dev_fft), dev_fft <= FOLD_WARD)
        okk &= check("F1.%d.e Hermiticity (max rel %.2e)"
                     % (k, herm_max), herm_max <= HERM_WARD)
        if k == 2:
            okk &= check("F1.2.c k=2 fold == deployed odd_toeplitz "
                         "(max rel %.2e) -- THE CONTROL IS THE "
                         "DEPLOYED WALL" % dev_dep,
                         dev_dep <= FOLD_WARD, kill="K2")
        okk &= check("F1.%d.mu ladder tie of mu^(%d) closed form "
                     "(max rel %.2e <= %.0e)" % (k, k, dev_mu, MU_TIE),
                     dev_mu <= MU_TIE)
        admitted[k] = okk
        if not okk:
            print("    -> k = %d: INSTRUMENT-EDGE (fold construction "
                  "refuses; documented, no verdict from this k)" % k)
    # H1 verbatim at k = 2 (channel side, CCCXXV)
    dev_h1 = 0.0
    for r in ward_sub:
        M, h = r["M"], r["h"]
        L = 2 * M - 2
        Tb = core.parity_basis(h, 2).T
        S = esq.sine_reads(Tb, M)
        jj = np.arange(1, L // 2)
        arm = (S[jj] * (2.0 / L)).T @ S[jj]
        nyq = (2.0 / L) * np.outer(S[L // 2], S[L // 2])
        dev_h1 = max(dev_h1, float(np.max(np.abs(
            arm - 0.5 * (np.eye(2) - nyq)))))
    check("F1.2.d CCCXXV H1 verbatim: one arm == (1/2)(I - nyq) "
          "(max dev %.2e)" % dev_h1, dev_h1 <= FOLD_WARD, kill="K2")
    if KILLS:
        return finish("WARD-BROKEN")

    # ------------------------------------------------------------ S4
    section("S4 -- THE LADDER READS: q^(k) = lam_min(K^(k)) / "
            "(c_k mu^(k)) on %d rungs" % len(reads))
    print("    frozen band (declared in advance, no refit): "
          "min q >= 1 AND trio in [%.3f/%.3f/%.3f, %.3f/%.3f/%.3f]"
          % (tuple(t / BAND_FAC for t in REF_TRIO)
             + tuple(t * BAND_FAC for t in REF_TRIO)))
    qs = {k: [] for k in KLIST}
    for r in reads:
        row = "    kz %4d h %5d :" % (r["kz"], r["h"])
        for k in KLIST:
            if not admitted[k]:
                continue
            if k == 2:
                q = r["shat"] / float(c_pair(2))
                lam = r["m"]
            else:
                q, lam, _ = q_read(r["c"], r["M"], r["h"], k)
            qs[k].append((q, lam, r))
            row += "  q(%d) %+9.4f" % (k, q)
        print(row, flush=True)
    # control ward: q(2) == 2 shat bit-for-bit
    dev_q2 = max(abs(q - 2.0 * r["shat"]) for q, _l, r in qs[2])
    check("S4.0 CONTROL: q^(2) == 2 shat on every read rung "
          "(max dev %.1e) -- the k=2 read IS the deployed read"
          % dev_q2, dev_q2 == 0.0, kill="K2")
    sat = {}
    for k in KLIST:
        if not admitted[k]:
            continue
        qv = np.array([q for q, _l, _r in qs[k]])
        tq = trio(qv)
        in_band = all(REF_TRIO[i] / BAND_FAC <= tq[i]
                      <= REF_TRIO[i] * BAND_FAC for i in range(3))
        sat[k] = bool(np.min(qv) >= 1.0) and in_band
        n_pass = int(np.sum(qv >= 1.0))
        print("    k=%d: q trio %+.4f/%+.4f/%+.4f, %d/%d rungs "
              "saturate (q >= 1), band %s"
              % (k, tq[0], tq[1], tq[2], n_pass, len(qv),
                 "IN" if in_band else "OUT"))
        check("S4.%d typed: %s" % (k, "SAT(%d)" % k if sat[k]
                                   else "NO-SAT(%d)" % k), True)
        # precision tier: residual certificate on 3 tightest rungs
        order = np.argsort(qv)[:3]
        worst = 0.0
        for i in order:
            q, lam, r = qs[k][i]
            K, _ = fold_wall(r["c"], r["M"], k) if k != 2 else (
                core.odd_toeplitz(r["c"], r["M"]), 0.0)
            w, V = np.linalg.eigh(K)
            v = V[:, 0]
            resid = float(np.linalg.norm(K @ v - w[0] * v))
            tgt = float(c_pair(k)) * mu_closed(k, r["h"])
            need = RESID_FACTOR * resid / tgt
            worst = max(worst, need / max(abs(q - 1.0), 1e-300))
            print("      tight kz %d h %d: q %+/.10f"
                  .replace("+/", "+") % (r["kz"], r["h"], q)
                  + "  resid %.2e  (100 r / target = %.2e)"
                  % (resid, need))
        check("P.%d typed: %s (margins vs 100x eigen-residual)"
              % (k, "CERT-OK" if worst < 1.0 else "CERT-THIN"), True)

    # ------------------------------------------------------------ S5
    section("S5 -- CONTROLS: Epstein / scramble / smooth must break "
            "the saturation in EVERY k")
    r9 = build_rung(CTRL_KZ)
    alpha9, M9, h9 = r9["alpha"], r9["M"], r9["h"]
    c_ar9 = r9["c_ar"]
    N_E = int(math.floor(math.exp(2.0 * alpha9))) + 1
    lamE = lambda_eps(N_E)
    nn = np.nonzero(np.abs(lamE) > 1e-12)[0]
    c_E = np.asarray(core.atom_lags_at(
        alpha9, M9, np.log(nn.astype(float)),
        2.0 * lamE[nn] / np.sqrt(nn.astype(float)))[0], float)
    rs = core.build_window(CTRL_KZ, scramble_seed=SCR_SEED)
    c_s = np.asarray(core.atom_lags_at(
        rs["alpha"], rs["M"], np.asarray(rs["uu"], float),
        2.0 * np.asarray(rs["lam"], float))[0], float)
    ctrls = [("Epstein", c_ar9 + c_E, M9, h9),
             ("scramble", c_ar9 + c_s, M9, h9)]
    for kzs in CTRL_SMOOTH_KZ:
        rr = build_rung(kzs)
        if rr is None:
            continue
        ug, mg = smooth_comb(rr["alpha"])
        c_sm = np.asarray(core.atom_lags_at(
            rr["alpha"], rr["M"], ug, mg)[0], float)
        ctrls.append(("smooth@kz%d" % kzs, rr["c_ar"] + c_sm,
                      rr["M"], rr["h"]))
    disc = {k: True for k in KLIST}
    for name, cv, Mc, hc in ctrls:
        row = "    %-12s:" % name
        for k in KLIST:
            if not admitted[k]:
                continue
            q, lam, _ = q_read(cv, Mc, hc, k)
            fired = q < 1.0
            disc[k] &= fired
            row += "  q(%d) %+.3e %s" % (k, q,
                                         "FIRES" if fired else "SILENT")
        print(row, flush=True)
    clean = {}
    for k in KLIST:
        if not admitted[k]:
            continue
        clean[k] = disc[k]
        check("C.%d typed: %s" % (k, "CONTROLS-DISCRIMINATE(k=%d)" % k
                                  if disc[k] else
                                  "CONTROLS-NON-DISCRIMINATING(k=%d) "
                                  "-- FIRST-CLASS FINDING" % k), True)
        if k == 2 and not disc[k]:
            check("C.2 WARD deployed controls must fire at k = 2",
                  False, kill="K2")
    if KILLS:
        return finish("WARD-BROKEN")

    # ------------------------------------------------------------ S6
    section("S6 -- F4 DOCTORED FOLD (non-vacuity): wrong orbit "
            "representative must shift the measured constant")
    rd = next((r for r in reads if r["kz"] == DOCTOR_KZ), reads[0])
    ok_doc = True
    for k in KLIST:
        if not admitted[k]:
            continue
        Kt, _ = fold_wall(rd["c"], rd["M"], k)
        Kd, _ = fold_wall(rd["c"], rd["M"], k, doctor=True)
        l0 = float(np.linalg.eigvalsh(Kt)[0])
        l1 = float(np.linalg.eigvalsh(Kd)[0])
        shift = abs(l1 - l0) / max(abs(l0), 1e-300)
        ok_doc &= check("F4.%d doctored fold shifts lam_min by rel "
                        "%.3e >= %.0e (kz %d)"
                        % (k, shift, DOCT_BAR, rd["kz"]),
                        shift >= DOCT_BAR, kill="K3")
    if KILLS:
        return finish("VACUOUS-INSTRUMENT")

    # ------------------------------------------------------------ V
    n_adm = [k for k in (3, 4) if admitted[k]]
    if not n_adm:
        verdict = "INSTRUMENT-EDGE (no k >= 3 admits the fold)"
    elif any(admitted[k] and clean.get(k, False) and not sat[k]
             for k in (3, 4)):
        bad_k = [k for k in (3, 4) if admitted[k]
                 and clean.get(k, False) and not sat[k]]
        verdict = ("PATTERN-ONLY (k = %s needs a different constant "
                   "or breaks the k=2 saturation profile while its "
                   "controls stay clean) -- THE CCCLI SELF-PAIRING "
                   "PRINCIPLE IS DEAD AS STATED"
                   % ",".join(map(str, bad_k)))
    elif all(admitted[k] and clean.get(k, False) and sat[k]
             for k in (3, 4)):
        verdict = ("PAIRING-PROVENANCE (all k saturate against the "
                   "predicted c_k mu^(k) with the k=2 margin "
                   "profile; no refit)")
    else:
        part = ", ".join("k=%d %s" % (k, "SAT" if sat.get(k) else
                                      ("NON-DISC" if not clean.get(k, True)
                                       else "EDGE"))
                         for k in (3, 4))
        verdict = "INSTRUMENT-EDGE-PARTIAL (%s)" % part
    return finish(verdict)


def finish(verdict):
    section("V -- FROZEN VERDICT")
    n_pass = sum(1 for _n, okk in CHECKS if okk)
    n_tot = len(CHECKS)
    print("\n  VERDICT: %s" % verdict)
    print("""
  HONEST FRAME (as frozen): even PAIRING-PROVENANCE supplies NO
  independent source for sign(Delta_h) and falls under the frozen
  gate rule -- it types the CCCLI principle as a PROGRAM ORGANIZER,
  not as progress; PATTERN-ONLY kills the principle as stated.  The
  k >= 3 folds are new objects built from the deployed window; the
  deployed surface is read-only and untouched.  NO RH claim.  No
  marker moves.""")
    print("\n[TIME] %.1f s (cap %.0f)   [CHECKS] %d run, %d failed"
          % (time.time() - T0, RUNTIME_CAP, n_tot, n_tot - n_pass))
    return 0 if (n_pass == n_tot and time.time() - T0 <= RUNTIME_CAP) \
        else 1


if __name__ == "__main__":
    raise SystemExit(main())
