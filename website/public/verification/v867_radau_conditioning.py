#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""v867 -- PRIME.SOFTPORT.RADAU.01 + PRIME.PORT.CONDITIONING.01: the quadrature reach and the intrinsic conditioning -- Gauss-Radau certificates for the pole-port scalar s > 0 EXIST on EVERY rung (the Golub-Meurant two-sided enclosure L_m <= r'G^{-1}r <= U_m is warded at every rung and depth with monotone bounds; a - U_m >= 1e-8 a certifies s > 0 by quadrature alone at m* <= 426 -- killing the kz-16 Neumann frontier of v864: positivity IS provable pointwise from the source side on the whole reachable ladder h <= 900) but the needed depth GROWS with the certified law m* ~ sqrt(cond(G)) (Spearman(m*, cond(G)) = +0.99 at log-log slope +0.43; Spearman(m*, h) = +0.91; cond(G) runs 8.5e2 -> 1.5e6), the m ~ 17 prediction FAILED as stated (0/7 rungs certify at m <= 17: the 17-mode concentration of the backflow VALUE does not equal a 17-step quadrature CERTIFICATE -- the certificate needs the resolvent, not just the sum), and the preconditioned retry closes the escape: all three source preconditioners (a: Krylov-head deflation, b: smooth-geometry, c: diagonal) are PD on every rung, congruence-invariant (rt'Gt^{-1}rt == r'G^{-1}r at 1e-8) -- and NONE bounds the effective condition number (medians first -> last third: raw 6.2e3 -> 3.7e5, a 6.2e3 -> 3.7e5, b 1.1e5 -> 8.1e6, c 6.5e3 -> 3.8e5; the retry still grows, 3/42 rungs at m* <= 17): THE CONDITIONING IS INTRINSIC at this ingredient list -- the soft end of the bulk is not the smooth geometry (else (b) would flatten it) and not the 17-mode Krylov head (else (a) would deflate it): it is DISTRIBUTED arithmetic structure that any certificate must resolve mode by mode -- in quadrature coordinates the wall is: the certificate depth is the price of the cancellation, and no source-side change of metric waives it, ONE module from two probes (7 checks with the frozen-honest FAIL S2.G2 + 8 checks with the frozen-honest FAIL S3.G, both kept and pattern-gated, NOT refit; verdicts RADAU-DEPTH-GROWS and CONDITIONING-INTRINSIC + J-INFINITY-NAMED; discovery probes softport_radau17_probe.py and preconditioned_port_probe.py, 2026-08-08, re-run identically at promotion, embedded BYTE-EXACT and executed verbatim, ~42 s).  THE POSITIVE STRUCTURAL FINDING (secondary, typed): the Lanczos/Jacobi chain of the bulk is NEAR-STATIONARY (14/17 coefficients drift <= 5 percent; tail sd/mean alpha 0.018, beta 0.029) and the limiting chain J_inf is NAMED -- the FREE (Chebyshev) Jacobi chain on the bulk support (support match + free-tail test pass; typed Rakhmanov-generic: the chain carries the bulk support geometry, not the arithmetic -- named, not oversold).  THE SYLVESTER CONTROL: congruence preserves the negativity of both controls (Epstein/scramble: the (a) preconditioner is itself INDEFINITE on those combs, lam_min(M) = -2.2e3/-1.4e7 -- the frame cannot even be built: no healing, negativity visible at the preconditioner); the Stieltjes frames of both controls COLLAPSE at the premise (gmin(G) < 0: no positive measure, no valid bounds) -- the discriminators fire before any bound is quoted.  The two source-side assets left on the table are typed: the closed-form a-term (v864) and the near-stationary Jacobi head.  NO RH claim.  Python-only per GATE.WOLFRAM.02.

PROVENANCE: discovery probes softport_radau17_probe.py (7 checks, 1
frozen-honest FAIL S2.G2, verdict RADAU-DEPTH-GROWS with the v1.1
extended-depth law typed in the frozen spec) and
preconditioned_port_probe.py (8 checks, 1 frozen-honest FAIL S3.G,
verdict CONDITIONING-INTRINSIC + J-INFINITY-NAMED), 2026-08-08,
re-run identically at promotion.  ROUND-31 EMBEDDING CONVENTION:
frozen sources embedded BYTE-EXACT and executed verbatim in isolated
namespaces; printed spec SHAs reproduce; byte-equality ward vs
experiments/tfpt-discovery/ inside the pattern gates.  Both probes
import the READ-ONLY v563_paper2_readouts.py and
pole_port_kappa_probe.py (gated in v864); the preconditioner probe
additionally imports softport_radau17_probe.py READ-ONLY -- none
re-gated here.

FIREWALL: no zeros, no prime-table oracles; bounds via classical
Golub-Meurant Gauss/Gauss-Radau (the budgets ARE the enclosure and
monotonicity wards, typed); the Jacobi census is descriptive only;
Sylvester's law is the structural control (no preconditioner can
heal negativity); the two FAILS are preregistered-honest
adjudications on record, bars NOT refit.  NO RH claim.
"""

import contextlib
import io
import math
import os
import re
import sys
import time
import types

_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)

# ------------- frozen probe source softport_radau17_probe (embedded BYTE-EXACT, raw string)
_SRC_0 = r'''
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""softport_radau17_probe -- PRIME.SOFTPORT.RADAU17.01: certify
the soft-port backflow by Gauss/Gauss-Radau quadrature.

EXPLORATION ONLY (experiments/): no ledger row, no paper edit, no
.md, nothing outside experiments/.  NO RH claim.  Frozen (spec +
sha256) before running.

THE MOVE: the pole-port skeleton (softport_cauchy_probe +
pole_port_kappa_probe, read-only) is s = a - r' G^{-1} r with a
CLOSED FORM (the Poisson average of the signed density at the
pole point) and the backflow r' G^{-1} r concentrated on <= 17
bulk modes; the certified-Neumann tail died at the kz 16
frontier because the triangle inequality murders the 99.9%
cancellation.  The classical repair (Golub-Meurant):
r' G^{-1} r = ||r||^2 int dmu(lam)/lam with mu the spectral
measure of the bulk G at the port direction -- a Stieltjes
integral; Lanczos from r gives the Jacobi chain (alpha_k,
beta_k) and:
  GAUSS (m nodes):      L_m  <=  int f dmu   (f = 1/lam, all
      even derivatives positive on (0, inf) => the Gauss error
      is positive: LOWER bound, monotone in m);
  GAUSS-RADAU (node prescribed at 0 < c <= lam_min(G)): U_m >=
      int f dmu (the odd-derivative error term is negative on
      [c, inf): UPPER bound, monotone in m).
Then a - U_m > 0 CERTIFIES s > 0 -- the positivity certificate
via quadrature instead of eigensolve of the cancellation.  The
17-mode finding predicts m ~ 17 should suffice.

THE CONSTRUCTION (sibling machinery verbatim): Delta =
G+^{-1/2} K G+^{-1/2}; pole port v = e^{rD/2}; w = G+^{1/2} v
normalized; Householder split on C w (+) w-perp gives a, r, G.
The Radau node c = 0.999 lam_min(G) (the bulk floor's own
certification carried over from the softport probe, where
gmin >= 0.3 lam2 was the premise ward; recomputed and
re-warded here per rung).  Lanczos with FULL
reorthogonalization; breakdown typed (beta_m <= 1e-13 scale =>
the measure is exhausted; then Gauss is exact).

THE GATES (frozen):
  G1 ENCLOSURE per rung/depth: L_m <= r'G^{-1}r_direct <= U_m
     (ward, tol 1e-9 rel) and monotone: L_m nondecreasing, U_m
     nonincreasing (tol 1e-12 rel).
  G2 THE DECISIVE TABLE: m*(kz) = minimal m with a - U_m >=
     1e-8 a (the certificate margin).  RADAU-CERTIFIES-FIXED-
     DEPTH iff every rung with h <= 900 certifies at m* <= 24
     AND the last-third max m* <= first-two-thirds max + 2 (no
     growth); the m ~ 17 prediction checked verbatim.
  G3 DEPTH LAW: m*(h) series + Spearman(m*, h) reported; if
     certificates exist everywhere but the depth grows ->
     RADAU-DEPTH-GROWS with the typed law; if some rung cannot
     certify at m <= 40 -> RADAU-BLIND (typed: the enclosure
     cannot see the cancellation either).
  G4 JACOBI STRUCTURE (bonus, descriptive only, Bonferroni-
     honest: NO verdict weight): the (alpha_k, beta_k) chains
     along the ladder -- per-coefficient h-drift (first 17
     coefficients, last-third vs first-third rel drift), the
     candidate limit chain, and the trivial recognizable laws
     (alpha_k -> const?, beta_k -> const? -- a limiting Jacobi
     operator would be the soft-port's canonical model).
KILLS (frozen): depth grows with h (G3); the bulk floor
degrades (gmin/lam2 < 0.3 on some rung -- recheck, the premise
ward); U_m stays above a at m = 40 (RADAU-BLIND).
CONTROLS: regressions vs the pole-port probe (kappa(kz9) in
[2.6, 2.8], kappa(kz40) in [1.5, 1.7]); Epstein x^2+5y^2 at kz
9: its s < 0 must be VISIBLE in the enclosure -- either the
premise breaks (gmin < 0: the Stieltjes frame collapses, typed)
or the Gauss LOWER bound certifies negativity (L_m > a);
scramble seed 1 likewise.

VERDICT (frozen): RADAU-CERTIFIES-FIXED-DEPTH /
RADAU-DEPTH-GROWS / RADAU-BLIND, with the kills typed.

NO RH claim; v563 + sibling probes READ-ONLY; no RNG; report
only.
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

import v563_paper2_readouts as core            # noqa: E402 (READ-ONLY)
import pole_port_kappa_probe as pp             # noqa: E402 (READ-ONLY)

T0 = time.time()
FAILS = []
N_CHK = 0

FROZEN_SPEC = """\
PRIME.SOFTPORT.RADAU17.01 spec v1 (2026-08-08, frozen before
run).  Machinery: pole_port_kappa_probe build_rung +
feshbach_pole read-only (krein cut 1 verbatim); ladder = ALL
frame_a_zones with h <= 900 (skips typed).  Lanczos on the bulk
G from r/||r||, full reorthogonalization, depth <= 40,
breakdown bar beta <= 1e-13 * beta_1.  Gauss L_m = ||r||^2
[J_m^{-1}]_11; Radau node c = 0.999 gmin(G); U_m = ||r||^2
[Jtilde_{m+1}^{-1}]_11 with alphatilde = c + x_m,
(J_m - cI) x = beta_m^2 e_m.  Wards: enclosure L_m <= direct <=
U_m (rel 1e-9, direct = a - s via the Schur identity);
monotonicity (rel 1e-12); premise gmin >= 0.3 lam2 every rung;
regressions kappa(kz9) in [2.6, 2.8], kappa(kz40) in [1.5,
1.7].  Certificate: m* = min m with a - U_m >= 1e-8 a.  Verdict
bars: FIXED-DEPTH iff all rungs certify with max m* <= 24 and
last-third max <= first-two-thirds max + 2; DEPTH-GROWS iff all
certify but bars above fail; BLIND iff some rung fails at m <=
40.  Controls: Epstein/scramble at kz 9 (premise break typed OR
L_m > a negativity certificate).  Jacobi drift: descriptive
only.  Float64 + full reorth; budgets = the enclosure +
monotonicity wards themselves (typed).  NO RH claim; writes
nothing.
ADDENDUM v1.1 (run-1 verdict sharpening, typed; the FIXED-DEPTH
bar and all run-1 numbers unchanged): the v1 depth budget M_MAX
= 40 CONFLATES the two failure enums -- 35 deep rungs fail at m
<= 40 while the enclosure is still converging (U_17 off by up
to 5e-2 where s ~ 1e-5: consistent with Lanczos convergence at
the bulk's condition number, not with a loose enclosure).  v1.1
extends the depth for the FAILING rungs to m <= min(dim G, 600)
to separate the enums honestly: RADAU-BLIND iff some rung
cannot certify even at extended depth; RADAU-DEPTH-GROWS iff
all certify but the depth grows (the typed law: m* vs h and vs
cond(G) = lam_max(G)/gmin, Spearman + log-log slope).  The
strong claim (FIXED-DEPTH) stays failed by the frozen v1 bar;
no bar is loosened in the claim direction."""

KAPPA_REFS = {9: (2.6, 2.8), 40: (1.5, 1.7)}
M_MAX = 40
M_FIX = 24
CERT_MARGIN = 1e-8
BANNED_IDS = ("zetazero", "nzeros", "primerange", "isprime",
              "primepi", "nextprime", "prevprime")


def check(name, ok, detail=""):
    global N_CHK
    N_CHK += 1
    if not ok:
        FAILS.append(name.split()[0])
    print("[%s] %s%s" % ("PASS" if ok else "FAIL", name,
                         (": " + detail) if detail else ""))


def ast_scan():
    src = open(os.path.abspath(__file__), encoding="utf-8").read()
    bad = []
    for node in ast.walk(ast.parse(src)):
        nm = None
        if isinstance(node, ast.Name):
            nm = node.id
        elif isinstance(node, ast.Attribute):
            nm = node.attr
        if nm and nm.lower() in BANNED_IDS:
            bad.append(nm)
    return bad


def spearman(x, y):
    def rk(v):
        o = np.argsort(v)
        r = np.empty(len(v))
        r[o] = np.arange(len(v))
        return r
    a, b = rk(np.asarray(x, float)), rk(np.asarray(y, float))
    a -= a.mean()
    b -= b.mean()
    den = math.sqrt(float(a @ a) * float(b @ b))
    return float(a @ b) / max(den, 1e-300)


# ---------------------------------------------------- Lanczos + quadrature
def lanczos(G, q1, m_max):
    """Full-reorthogonalized Lanczos: returns (alphas, betas,
    m_done, breakdown)."""
    n = len(q1)
    Q = np.zeros((n, m_max + 1))
    Q[:, 0] = q1 / np.linalg.norm(q1)
    alphas, betas = [], []
    beta_scale = None
    for k in range(m_max):
        v = G @ Q[:, k]
        if k > 0:
            v -= betas[-1] * Q[:, k - 1]
        a_ = float(Q[:, k] @ v)
        v -= a_ * Q[:, k]
        # full reorthogonalization (twice for safety)
        for _ in range(2):
            v -= Q[:, :k + 1] @ (Q[:, :k + 1].T @ v)
        b_ = float(np.linalg.norm(v))
        alphas.append(a_)
        if beta_scale is None:
            beta_scale = max(b_, 1e-300)
        if b_ <= 1e-13 * beta_scale:
            return np.array(alphas), np.array(betas), k + 1, True
        betas.append(b_)
        Q[:, k + 1] = v / b_
    return np.array(alphas), np.array(betas), m_max, False


def jac_inv11(alphas, betas):
    """[J^{-1}]_11 for the tridiagonal J via the backward
    continued fraction (numerically stable for J > 0)."""
    m = len(alphas)
    t = alphas[m - 1]
    for k in range(m - 2, -1, -1):
        t = alphas[k] - betas[k] ** 2 / t
    return 1.0 / t


def gauss_bounds(alphas, betas, c, m):
    """(L_m, U_m) for int dmu/lam with total mass 1: Gauss and
    Gauss-Radau (node at c)."""
    al = alphas[:m]
    be = betas[:m - 1] if m > 1 else np.array([])
    L = jac_inv11(al, be)
    # Radau: solve (J_m - c I) x = beta_m^2 e_m
    if m <= len(betas):
        bm2 = betas[m - 1] ** 2
        # tridiagonal solve via Thomas
        n = m
        aa = al - c
        cprime = np.zeros(n)
        dprime = np.zeros(n)
        rhs = np.zeros(n)
        rhs[-1] = bm2
        cp = 0.0
        dp = 0.0
        for i in range(n):
            lo = be[i - 1] if i > 0 else 0.0
            up = be[i] if i < n - 1 else 0.0
            denom = aa[i] - lo * cp
            cprime[i] = up / denom
            dprime[i] = (rhs[i] - lo * dp) / denom
            cp, dp = cprime[i], dprime[i]
        x = np.zeros(n)
        x[-1] = dprime[-1]
        for i in range(n - 2, -1, -1):
            x[i] = dprime[i] - cprime[i] * x[i + 1]
        al_t = np.concatenate([al, [c + x[-1]]])
        be_t = np.concatenate([be, [betas[m - 1]]])
        U = jac_inv11(al_t, be_t)
    else:
        U = L                       # breakdown: Gauss exact
    return L, U


def port_split(Delta, Gp, Rp, h, D):
    v = np.exp(0.5 * np.arange(h) * D)
    v = v / np.linalg.norm(v)
    fp = pp.feshbach_pole(Delta, Gp, Rp, v)
    return fp


def run():
    print("=" * 78)
    print("SOFTPORT RADAU-17 (softport_radau17_probe) -- the "
          "quadrature positivity certificate")
    print("=" * 78)
    print("frozen spec sha256 = %s"
          % hashlib.sha256(FROZEN_SPEC.encode()).hexdigest()[:16])
    print("""
HONESTY FRAME: NO RH claim.  Bounds via Golub-Meurant Gauss/
Gauss-Radau (classical); the budgets ARE the enclosure and
monotonicity wards (typed); the Jacobi census is descriptive
only.""")

    # ============================================================== S0
    print("\nS0 -- firewall")
    check("S0.AST firewall clean", not ast_scan())

    zones = list(core.frame_a_zones())

    # ============================================================== S1
    print("\nS1 -- the ladder: Lanczos chains + two-sided "
          "enclosures")
    rows = []
    skipped = []
    ok_encl = True
    ok_mono = True
    ok_floor = True
    jac_store = {}
    print("    kz    h    kappa  a          rGr(dir)   gmin/l2 "
          " m*  L17-gap    U17-gap    cert")
    for kz in zones:
        out = pp.build_rung(kz)
        rr, Delta, Gp, Rp = out[0], out[8], out[6], out[7]
        h, D = rr["h"], rr["D"]
        if h > 900:
            skipped.append(kz)
            continue
        fp = port_split(Delta, Gp, Rp, h, D)
        a_, s_, gmin = fp["a"], fp["s"], fp["gmin"]
        lam2 = fp["lam2"]
        G, rv = fp["G"], fp["rv"]
        ok_floor &= gmin >= 0.3 * lam2
        nr2 = float(rv @ rv)
        direct = a_ - s_                     # == r'G^-1 r (Schur)
        alphas, betas, m_done, brk = lanczos(G, rv, M_MAX)
        c_node = 0.999 * gmin
        Ls, Us = [], []
        m_star = None
        for m in range(1, m_done + 1):
            L_, U_ = gauss_bounds(alphas, betas, c_node, m)
            L_, U_ = nr2 * L_, nr2 * U_
            Ls.append(L_)
            Us.append(U_)
            ok_encl &= (L_ <= direct * (1 + 1e-9) + 1e-15
                        and direct <= U_ * (1 + 1e-9) + 1e-15)
            if m > 1:
                ok_mono &= (L_ >= Ls[-2] * (1 - 1e-12) - 1e-15
                            and U_ <= Us[-2] * (1 + 1e-12)
                            + 1e-15)
            if m_star is None and a_ - U_ >= CERT_MARGIN * a_:
                m_star = m
        i17 = min(17, m_done) - 1
        # v1.1: extended depth for rungs failing at m <= M_MAX
        m_ext = m_star
        if m_star is None:
            dimG = G.shape[0]
            m_lim = min(dimG - 1, 600)
            al_e, be_e, md_e, brk_e = lanczos(G, rv, m_lim)
            for m in range(M_MAX + 1, md_e + 1):
                L_, U_ = gauss_bounds(al_e, be_e, c_node, m)
                if a_ - nr2 * U_ >= CERT_MARGIN * a_:
                    m_ext = m
                    break
        cond = float(np.linalg.eigvalsh(G)[-1]) / gmin
        rows.append(dict(kz=kz, h=h, kap=fp["s"] / fp["lam1"],
                         a=a_, direct=direct, gf=gmin / lam2,
                         mstar=m_star, mext=m_ext, cond=cond,
                         brk=brk, mdone=m_done,
                         L17=Ls[i17], U17=Us[i17],
                         alphas=alphas, betas=betas))
        jac_store[kz] = (alphas, betas, h)
        print("    %-4d  %-4d %5.2f  %.4e %.4e %.2f    %-3s "
              "%+.3e %+.3e %s"
              % (kz, h, fp["s"] / fp["lam1"], a_, direct,
                 gmin / lam2,
                 str(m_star) if m_star else "--",
                 a_ - Ls[i17], a_ - Us[i17],
                 "YES" if m_star else "NO"), flush=True)
    print("    (skipped h > 900: %s)" % (skipped or "none"))
    check("S1.ENC [THE ENCLOSURE WARD] L_m <= r'G^-1r(direct, "
          "Schur) <= U_m at every rung and depth (rel 1e-9)",
          ok_encl)
    check("S1.MON [MONOTONICITY] L_m nondecreasing, U_m "
          "nonincreasing in m everywhere (rel 1e-12)", ok_mono)
    check("S1.FLR [THE PREMISE RECHECK] the bulk floor holds on "
          "every rung: gmin(G) >= 0.3 lam2 (min ratio %.2f) -- "
          "the Radau node stands on certified ground"
          % min(r["gf"] for r in rows), ok_floor)
    kaps = {r["kz"]: r["kap"] for r in rows}
    reg_ok = all(KAPPA_REFS[k][0] <= kaps[k] <= KAPPA_REFS[k][1]
                 for k in KAPPA_REFS if k in kaps)
    check("S1.REG regressions vs the pole-port probe: "
          "kappa(kz9) = %.3f in [2.6, 2.8], kappa(kz40) = %.3f "
          "in [1.5, 1.7]"
          % (kaps.get(9, -1.0), kaps.get(40, -1.0)), reg_ok)

    # ============================================================== S2
    print("\nS2 -- the decisive table: m*(h) and the depth law")
    cert_all = all(r["mstar"] is not None for r in rows)
    mstars = [r["mstar"] for r in rows if r["mstar"]]
    hs = [r["h"] for r in rows if r["mstar"]]
    if mstars:
        third = max(1, len(mstars) // 3)
        head_max = max(mstars[:-third])
        tail_max = max(mstars[-third:])
        sp_mh = spearman(mstars, hs)
        fixed = (cert_all and max(mstars) <= M_FIX
                 and tail_max <= head_max + 2)
        print("    m* range [%d, %d]; last-third max %d vs "
              "first-two-thirds max %d; Spearman(m*, h) = "
              "%+.2f; the m ~ 17 prediction: %d/%d rungs "
              "certify at m <= 17"
              % (min(mstars), max(mstars), tail_max, head_max,
                 sp_mh, sum(1 for m in mstars if m <= 17),
                 len(mstars)))
    else:
        fixed = False
    check("S2.G2 [THE CERTIFICATE] every rung h <= 900 "
          "certifies s > 0 by a - U_m >= 1e-8 a at depth m* <= "
          "%d with NO depth growth (last-third bar): %s"
          % (M_FIX, fixed), fixed)
    # v1.1: the extended-depth law for the failing rungs
    cert_ext = all(r["mext"] is not None for r in rows)
    mexts = [r["mext"] for r in rows if r["mext"]]
    hexts = [r["h"] for r in rows if r["mext"]]
    cexts = [r["cond"] for r in rows if r["mext"]]
    if cert_ext:
        sp_h = spearman(mexts, hexts)
        sp_c = spearman(mexts, cexts)
        sl_h = float(np.polyfit(np.log(hexts),
                                np.log(mexts), 1)[0])
        sl_c = float(np.polyfit(np.log(cexts),
                                np.log(mexts), 1)[0])
        print("    v1.1 EXTENDED DEPTH: every rung certifies "
              "at m* <= %d; the depth law: Spearman(m*, h) = "
              "%+.2f (log-log slope %+.2f), Spearman(m*, "
              "cond(G)) = %+.2f (slope %+.2f); cond(G) range "
              "[%.1e, %.1e]"
              % (max(mexts), sp_h, sl_h, sp_c, sl_c,
                 min(cexts), max(cexts)))
    else:
        nfail = sum(1 for r in rows if r["mext"] is None)
        print("    v1.1 EXTENDED DEPTH: %d rungs STILL fail at "
              "m <= min(dim G, 600) -- the enclosure cannot "
              "see the cancellation there" % nfail)

    # ============================================================== S3
    print("\nS3 -- the Jacobi coefficient structure "
          "(descriptive, Bonferroni-honest: no verdict weight)")
    kzs = sorted(jac_store)
    third = max(1, len(kzs) // 3)
    first_k, last_k = kzs[:third], kzs[-third:]
    kmaxc = min(17, min(len(jac_store[k][0]) for k in kzs))
    drift = []
    for j in range(kmaxc):
        af = np.mean([jac_store[k][0][j] for k in first_k])
        al_ = np.mean([jac_store[k][0][j] for k in last_k])
        drift.append(abs(al_ - af) / max(abs(af), 1e-300))
    a_last = np.array([jac_store[kzs[-1]][0][j]
                       for j in range(kmaxc)])
    b_last = np.array([jac_store[kzs[-1]][1][j]
                       for j in range(min(kmaxc,
                                          len(jac_store[kzs[-1]][1])))])
    print("    deepest-rung chain: alpha_1..%d in [%.3f, %.3f] "
          "(mean %.3f, sd %.3f); beta_1..%d in [%.3f, %.3f] "
          "(mean %.3f, sd %.3f)"
          % (kmaxc, a_last.min(), a_last.max(), a_last.mean(),
             a_last.std(), len(b_last), b_last.min(),
             b_last.max(), b_last.mean(), b_last.std()))
    print("    per-coefficient ladder drift (first vs last "
          "third), alpha_1..%d: median %.3f, max %.3f -- %s"
          % (kmaxc, float(np.median(drift)), float(np.max(drift)),
             "the chain drifts along the ladder (no fixed "
             "limit operator at this depth)" if
             np.median(drift) > 0.05 else
             "the chain is near-stationary: a candidate "
             "limiting Jacobi operator exists"))

    # ============================================================== S4
    print("\nS4 -- the discriminators (kz 9)")
    rr9 = core.build_window(9)
    a9 = rr9["alpha"]
    N_E = int(math.floor(math.exp(2.0 * a9))) + 1
    lamE = pp.lambda_eps(N_E)
    nn = np.nonzero(np.abs(lamE) > 1e-12)[0]
    disc_ok = True
    for nmc, kw in (("Epstein", dict(comb=(
            np.log(nn.astype(float)),
            2.0 * lamE[nn] / np.sqrt(nn.astype(float))))),
            ("scramble", dict(scramble_seed=1))):
        out = pp.build_rung(9, **kw)
        rr, Delta, Gp, Rp = out[0], out[8], out[6], out[7]
        fp = port_split(Delta, Gp, Rp, rr["h"], rr["D"])
        if fp["gmin"] <= 0:
            print("    %-8s: gmin(G) = %+.3e <= 0 -- the "
                  "Stieltjes frame COLLAPSES (typed premise "
                  "break: no positive measure, no valid "
                  "bounds): the negativity is visible at the "
                  "premise" % (nmc, fp["gmin"]))
            continue
        G, rv = fp["G"], fp["rv"]
        nr2 = float(rv @ rv)
        alphas, betas, m_done, brk = lanczos(G, rv, M_MAX)
        neg_m = None
        for m in range(1, m_done + 1):
            L_, _ = gauss_bounds(alphas, betas,
                                 0.999 * fp["gmin"], m)
            if nr2 * L_ > fp["a"]:
                neg_m = m
                break
        vis = neg_m is not None
        disc_ok &= vis
        print("    %-8s: s = %+.3e, gmin = %+.3e > 0; Gauss "
              "LOWER bound certifies s < 0 (L_m > a) at m = %s"
              % (nmc, fp["s"], fp["gmin"],
                 str(neg_m) if vis else "NEVER (<= %d)"
                 % m_done))
    check("S4.DIS the negativity of both controls is VISIBLE "
          "in the enclosure (premise break typed, or the Gauss "
          "lower bound certifies s < 0)", disc_ok)

    # ============================================================== S5
    print("\nS5 -- verdict")
    if fixed and not FAILS:
        verdict = "RADAU-CERTIFIES-FIXED-DEPTH"
    elif cert_ext:
        verdict = "RADAU-DEPTH-GROWS"
    else:
        verdict = "RADAU-BLIND"
    print("=" * 78)
    print("V -- VERDICT: %s" % verdict)
    print("=" * 78)
    if verdict == "RADAU-CERTIFIES-FIXED-DEPTH":
        med_d = float(np.median(drift))
        print("""    THE RESULT: the certified two-sided quadrature enclosure
    proves s > 0 -- hence tau > 0 via the warded Feshbach
    premise -- at bounded Lanczos depth m* <= %d on EVERY rung
    of the ladder (h <= 900), replacing the eigensolve of the
    cancellation with %d source-side Jacobi coefficients per
    rung; the Neumann frontier at kz 16 is GONE (the triangle
    inequality was the obstruction, not the cancellation).
    THE UNIFORM-COEFFICIENT STATEMENT (what a cofinal theorem
    needs): the certificate family is (alpha_1..alpha_m*,
    beta_1..beta_m*-1, c) per rung with the SAME acceptance
    inequality a - U_m* > 0; a cofinal statement needs (i) the
    closed-form a-term (already source-closed, the Poisson
    average), (ii) a uniform-in-h lower bound on the bulk
    floor c, and (iii) the convergence of the truncated Jacobi
    chain along the ladder -- measured here: median
    per-coefficient drift %.3f (%s).  The wall, in quadrature
    coordinates: prove those three uniformities from the
    source side.  NO RH claim.""" % (
            max(mstars), max(mstars), med_d,
            "near-stationary -- the limiting Jacobi operator "
            "is a real candidate object" if med_d <= 0.05 else
            "still drifting -- uniformity (iii) is the open "
            "leg"))
    elif verdict == "RADAU-DEPTH-GROWS":
        print("""    THE TYPED LAW (v1.1): certificates EXIST on every rung --
    the quadrature route does prove s > 0 pointwise, killing
    the kz-16 Neumann frontier -- but the needed depth grows:
    m* up to %d, Spearman(m*, h) = %+.2f (log-log slope
    %+.2f), Spearman(m*, cond(G)) = %+.2f (slope %+.2f).  The
    driver is the CONDITION of the bulk relative to the
    certificate margin s/a (~1e-5 at depth): Lanczos must
    resolve the soft end of the bulk spectrum before the
    Radau upper bound tightens below a.  The m ~ 17
    prediction FAILED as stated (0 rungs at m <= 17): the
    17-mode concentration of the backflow VALUE does not
    equal a 17-step quadrature CERTIFICATE -- the certificate
    needs the resolvent, not just the sum.  HONEST
    CONSEQUENCE: in quadrature coordinates the wall is the
    depth-growth law above -- a cofinal certificate family
    needs either a uniform bulk-conditioning bound or a
    preconditioned port (the closed-form a-term and the
    near-stationary Jacobi head measured in S3 are the two
    source-side assets this leaves on the table).""" % (
            max(mexts), sp_h, sl_h, sp_c, sl_c))
    dt = time.time() - T0
    print("-" * 78)
    print("checks: %d run, %d failed%s | runtime %.1f min"
          % (N_CHK, len(FAILS),
             (" [" + ", ".join(FAILS) + "]") if FAILS else "",
             dt / 60.0))
    print("NO RH claim; report only; nothing outside "
          "experiments/ touched.")


if __name__ == "__main__":
    run()
'''
# ------------- frozen probe source preconditioned_port_probe (embedded BYTE-EXACT, raw string)
_SRC_1 = r'''
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""preconditioned_port_probe -- PRIME.SOFTPORT.PRECOND.01: the
preconditioned port.

EXPLORATION ONLY (experiments/): no ledger row, no paper edit, no
.md, nothing outside experiments/.  NO RH claim.  Frozen (spec +
sha256) before running.

THE TARGET (from RADAU-DEPTH-GROWS, softport_radau17_probe): the
quadrature certificate a - U_m > 0 exists on every rung but the
depth grows as the textbook Lanczos law m* ~ cond(G)^{0.43}
(Spearman +0.99); the Jacobi chain head is near-stationary
(median drift 0.036/coefficient).  THE HOPE: a source-built
preconditioner M bounds cond(M^{-1/2} G M^{-1/2}), making the
certificate depth uniform -- the fixed-depth family exists after
all.  The Stieltjes problem transforms covariantly:

    r' G^{-1} r = rt' Gt^{-1} rt,   Gt = M^{-1/2} G M^{-1/2},
    rt = M^{-1/2} r   (exact congruence invariance, warded),

and Sylvester's law of inertia guarantees congruence CANNOT heal
a negative bulk -- the Epstein/scramble premise collapse must
survive every preconditioner (structural control, verified).

TASK 1 -- J_INFINITY: the ladder-limit of the Jacobi chains
(alpha_k, beta_k): per-coefficient last-third medians + drift
bands; stationarity depth profile (#coefficients with last-vs-
first-third drift <= 5% / 10%); head-only limit typed where the
chains diverge.  IDENTIFICATION (fit-free, frozen bars,
Bonferroni-honest): (i) the free/Chebyshev test -- if the tail
coefficients are constant (sd/mean <= 5% for alpha_{5..17} and
beta_{5..17}) the chain is the FREE Jacobi chain of an interval
[A, B] = [alpha - 2 beta, alpha + 2 beta]; named only if
additionally the induced support matches the measured bulk
support [gmin, lam_max] to <= 10% per endpoint.  TYPED: by
Rakhmanov, the free chain is GENERIC for measures with a.c.
support on one interval -- a name of the SUPPORT GEOMETRY, not
of the arithmetic; (ii) the period-2 alternation diagnostic
(two-interval measures), reported.

TASK 2 -- THE PRECONDITIONER FAMILY (predeclared, source-only):
  (a) J-HEAD DEFLATION: M_a = Q_17 J_17 Q_17' + alpha_inf (I -
      Q_17 Q_17') from the rung's own depth-17 Lanczos data
      (source: G and r) with the ladder-limit tail value
      alpha_inf;
  (b) PNT-GRADE BULK: M_b = the bulk block (same port frame,
      same positive-metric embedding) of the ABS form of the
      SMOOTH window density |d_pnt| = |FFT lags(arch + smooth
      comb)| where the smooth comb is the PNT integral dpsi =
      dx (atom grid u_i = i D/8, masses 2 e^{u_i/2} D/8 --
      source-closed, no Lambda) -- precondition by the smooth
      geometry, leave the arithmetic fluctuation;
  (c) DIAGONAL scaling M_c = diag(G) (the cheap control).
THE DECISIVE NUMBER per preconditioner: cond(Gt) along the
ladder -- bounded (Spearman(cond, rung) <= 0.3 OR last-third
median <= 1.5 x first-third median) vs still growing.

TASK 3 -- THE CERTIFICATE RETRY for the best preconditioner
(smallest last-third median cond): full Golub-Meurant in the
preconditioned frame (Lanczos on Gt from rt, Radau node ct =
0.999 lam_min(Gt), enclosure + monotonicity + congruence-
invariance wards); m*(h) law with extended depth (<= 600) built
in.  PASS: every rung certifies with m* <= 24 and last-third
max <= first-two-thirds max + 2.

CONTROLS: Radau regressions (m*(kz9) == 20, kappa refs);
firewall (no zero/prime oracles; the preconditioners consume
only source objects -- structural); Epstein/scramble premise
collapse SURVIVES the preconditioned frame (Sylvester,
verified numerically); budgets = the wards (typed).

VERDICT (frozen): PRECONDITIONED-FIXED-DEPTH (the retry PASS --
the fixed-depth certificate family; the cofinal shape stated
verbatim with named remaining hypotheses) / CONDITIONING-
INTRINSIC (all three preconditioners leave cond growing -- the
wall in conditioning form, typed).  SECONDARY (reported
regardless): J-INFINITY-NAMED iff the identification bars pass.

NO RH claim; v563 + sibling probes READ-ONLY; no RNG; report
only.
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

import v563_paper2_readouts as core            # noqa: E402 (READ-ONLY)
import pole_port_kappa_probe as pp             # noqa: E402 (READ-ONLY)
import softport_radau17_probe as sr            # noqa: E402 (READ-ONLY)

T0 = time.time()
FAILS = []
N_CHK = 0

FROZEN_SPEC = """\
PRIME.SOFTPORT.PRECOND.01 spec v1 (2026-08-08, frozen before
run).  Ladder = ALL frame_a_zones h <= 900.  Chains: Lanczos
depth 17 with Q kept, full reorth.  J_inf: per-coefficient
last-third median; drift = |last-third mean - first-third
mean| / |first-third mean|; stationarity profile at 5%/10%.
Identification bars: free/Chebyshev iff sd/mean(alpha_{5..17})
<= 0.05 AND sd/mean(beta_{5..17}) <= 0.05; named iff also
[alpha - 2 beta, alpha + 2 beta] matches [gmin, lam_max(G)]
per endpoint rel <= 0.10 (deepest rung); period-2 diagnostic
reported.  Preconditioners (a)/(b)/(c) exactly as header;
bounded-cond bar: Spearman(cond, rung index) <= 0.3 OR
last-third median <= 1.5 x first-third median.  Retry: best =
smallest last-third median cond; Lanczos <= 600 on Gt from rt;
node 0.999 lam_min(Gt); cert margin a - U >= 1e-8 a; wards:
congruence invariance rel <= 1e-8, enclosure (rel 1e-9),
monotone (rel 1e-12), M PD (lam_min > 0).  PASS bars: all
rungs m* <= 24 AND last-third max <= first-two-thirds max + 2.
Regressions: m*(kz9) raw == 20; kappa(kz9) in [2.6, 2.8].
Sylvester control: gmin(Gt_Epstein) < 0 and gmin(Gt_scramble)
< 0 under the best preconditioner rebuilt on their rungs.
Verdict enum as header.  NO RH claim; writes nothing."""

M_HEAD = 17
M_FIX = 24
M_EXT = 600
CERT_MARGIN = 1e-8
KAPPA_REF9 = (2.6, 2.8)
MSTAR9_REF = 20
BANNED_IDS = ("zetazero", "nzeros", "primerange", "isprime",
              "primepi", "nextprime", "prevprime")


def check(name, ok, detail=""):
    global N_CHK
    N_CHK += 1
    if not ok:
        FAILS.append(name.split()[0])
    print("[%s] %s%s" % ("PASS" if ok else "FAIL", name,
                         (": " + detail) if detail else ""))


def ast_scan():
    src = open(os.path.abspath(__file__), encoding="utf-8").read()
    bad = []
    for node in ast.walk(ast.parse(src)):
        nm = None
        if isinstance(node, ast.Name):
            nm = node.id
        elif isinstance(node, ast.Attribute):
            nm = node.attr
        if nm and nm.lower() in BANNED_IDS:
            bad.append(nm)
    return bad


def lanczos_q(G, q1, m_max):
    """Full-reorth Lanczos keeping the basis Q."""
    n = len(q1)
    Q = np.zeros((n, m_max + 1))
    Q[:, 0] = q1 / np.linalg.norm(q1)
    alphas, betas = [], []
    for k in range(m_max):
        v = G @ Q[:, k]
        if k > 0:
            v -= betas[-1] * Q[:, k - 1]
        a_ = float(Q[:, k] @ v)
        v -= a_ * Q[:, k]
        for _ in range(2):
            v -= Q[:, :k + 1] @ (Q[:, :k + 1].T @ v)
        b_ = float(np.linalg.norm(v))
        alphas.append(a_)
        if b_ <= 1e-13:
            return (np.array(alphas), np.array(betas),
                    Q[:, :k + 1], True)
        betas.append(b_)
        Q[:, k + 1] = v / b_
    return np.array(alphas), np.array(betas), Q[:, :m_max], False


def inv_sqrt(M):
    ev, V = np.linalg.eigh(M)
    assert ev[0] > 0
    return V @ np.diag(ev ** -0.5) @ V.T, float(ev[0]), \
        float(ev[-1])


def cert_depth(G, rv, a_, m_max):
    """(m*, cond, gmin) for the Gauss-Radau certificate on
    (G, rv) with target scalar a_."""
    ev0 = np.linalg.eigvalsh(G)
    gmin, gmax = float(ev0[0]), float(ev0[-1])
    if gmin <= 0:
        return None, float("inf"), gmin, None, None
    nr2 = float(rv @ rv)
    alphas, betas, _, brk = lanczos_q(G, rv, m_max)
    m_done = len(alphas)
    direct = float(rv @ np.linalg.solve(G, rv))
    ok_e = True
    ok_m = True
    Lp = Up = None
    m_star = None
    for m in range(1, m_done + 1):
        L_, U_ = sr.gauss_bounds(alphas, betas, 0.999 * gmin, m)
        L_, U_ = nr2 * L_, nr2 * U_
        ok_e &= (L_ <= direct * (1 + 1e-9) + 1e-15
                 and direct <= U_ * (1 + 1e-9) + 1e-15)
        if Lp is not None:
            ok_m &= (L_ >= Lp * (1 - 1e-12) - 1e-15
                     and U_ <= Up * (1 + 1e-12) + 1e-15)
        Lp, Up = L_, U_
        if m_star is None and a_ - U_ >= CERT_MARGIN * a_:
            m_star = m
            break
    return m_star, gmax / gmin, gmin, ok_e, ok_m


def smooth_bulk_M(rr, Rm, Bc):
    """Preconditioner (b): the ABS form of the smooth (PNT)
    window density in the same port frame.  Source-closed: arch
    + the PNT integral comb (no Lambda)."""
    h, M, D, al = rr["h"], rr["M"], rr["D"], rr["alpha"]
    du = D / 8.0
    ug = np.arange(du, 2.0 * al, du)
    mm_s = 2.0 * np.exp(0.5 * ug) * du
    c_s, _ = core.atom_lags_at(al, M, ug, mm_s)
    c_ar = np.asarray(core.arch_lags(M, D), float)
    d_pnt = pp.grid_density(c_ar + c_s)
    L = 2 * M - 2
    E = pp.odd_extend_mat(h)
    Fp = np.fft.fft(np.vstack([E, np.zeros((L - M, h))]),
                    axis=0)
    Kabs = np.real(Fp.conj().T @ (np.abs(d_pnt)[:, None] * Fp)
                   ) / (2.0 * L)
    Dl = Rm @ Kabs @ Rm
    Dl = 0.5 * (Dl + Dl.T)
    Mb = Bc.T @ (Dl @ Bc)
    return 0.5 * (Mb + Mb.T)


def port_frame(Delta, Gp, Rp, h, D):
    """The pole-port Feshbach frame + the Householder basis."""
    v = np.exp(0.5 * np.arange(h) * D)
    v = v / np.linalg.norm(v)
    fp = pp.feshbach_pole(Delta, Gp, Rp, v)
    w = fp["w"]
    e1 = np.zeros(h)
    e1[0] = 1.0
    u = e1 - w
    nu = np.linalg.norm(u)
    H = np.eye(h) - 2.0 * np.outer(u / nu, u / nu) \
        if nu > 1e-12 else np.eye(h)
    return fp, H[:, 1:]


def run():
    print("=" * 78)
    print("PRECONDITIONED PORT (preconditioned_port_probe) -- "
          "defeating the sqrt-cond depth law")
    print("=" * 78)
    print("frozen spec sha256 = %s"
          % hashlib.sha256(FROZEN_SPEC.encode()).hexdigest()[:16])
    print("""
HONESTY FRAME: NO RH claim.  Congruence invariance is exact and
warded; Sylvester's law is the structural control (no
preconditioner can heal negativity); the J_inf identification is
typed Rakhmanov-generic if it fires.""")

    # ============================================================== S0
    print("\nS0 -- firewall + the ladder frames")
    check("S0.AST firewall clean", not ast_scan())
    zones = [kz for kz in core.frame_a_zones()]
    frames = {}
    for kz in zones:
        out = pp.build_rung(kz)
        rr, Delta, Gp, Rp = out[0], out[8], out[6], out[7]
        if rr["h"] > 900:
            continue
        fp, Bc = port_frame(Delta, Gp, Rp, rr["h"], rr["D"])
        frames[kz] = dict(rr=rr, Delta=Delta, Rm=None, fp=fp,
                          Bc=Bc)
        # Rm for the smooth preconditioner (same embedding)
        ev, Vp = np.linalg.eigh(Gp)
        frames[kz]["Rm"] = Vp @ np.diag(ev ** -0.5) @ Vp.T
    kzs = sorted(frames)
    kap9 = frames[9]["fp"]["s"] / frames[9]["fp"]["lam1"]
    m9, c9, _, _, _ = cert_depth(frames[9]["fp"]["G"],
                                 frames[9]["fp"]["rv"],
                                 frames[9]["fp"]["a"], 40)
    check("S0.REG Radau regressions: kappa(kz9) = %.3f in "
          "[2.6, 2.8] AND raw m*(kz9) = %s == %d"
          % (kap9, m9, MSTAR9_REF),
          KAPPA_REF9[0] <= kap9 <= KAPPA_REF9[1]
          and m9 == MSTAR9_REF)

    # ============================================================== S1
    print("\nS1 -- J_INFINITY: the limiting Jacobi chain")
    chains = {}
    for kz in kzs:
        fp = frames[kz]["fp"]
        al, be, Q, _ = lanczos_q(fp["G"], fp["rv"], M_HEAD)
        chains[kz] = (al, be, Q)
    third = max(1, len(kzs) // 3)
    fk, lk = kzs[:third], kzs[-third:]
    kmax = min(M_HEAD, min(len(chains[k][0]) for k in kzs))
    al_inf, be_inf, drifts = [], [], []
    for j in range(kmax):
        af = float(np.mean([chains[k][0][j] for k in fk]))
        al_ = float(np.median([chains[k][0][j] for k in lk]))
        al_inf.append(al_)
        drifts.append(abs(float(np.mean(
            [chains[k][0][j] for k in lk])) - af)
            / max(abs(af), 1e-300))
        if j < kmax - 1:
            be_inf.append(float(np.median(
                [chains[k][1][j] for k in lk])))
    al_inf = np.array(al_inf)
    be_inf = np.array(be_inf)
    n5 = sum(1 for d_ in drifts if d_ <= 0.05)
    n10 = sum(1 for d_ in drifts if d_ <= 0.10)
    print("    stationarity profile: %d/%d coefficients drift "
          "<= 5%%, %d/%d <= 10%% (head-only limit typed beyond)"
          % (n5, kmax, n10, kmax))
    a_t = al_inf[4:]
    b_t = be_inf[4:]
    sd_a = float(np.std(a_t) / max(abs(np.mean(a_t)), 1e-300))
    sd_b = float(np.std(b_t) / max(abs(np.mean(b_t)), 1e-300))
    A_ind = float(np.mean(a_t) - 2.0 * np.mean(b_t))
    B_ind = float(np.mean(a_t) + 2.0 * np.mean(b_t))
    Gdeep = frames[kzs[-1]]["fp"]["G"]
    evd = np.linalg.eigvalsh(Gdeep)
    gmin_d, gmax_d = float(evd[0]), float(evd[-1])
    supp_ok = (abs(A_ind - gmin_d) / gmax_d <= 0.10
               and abs(B_ind - gmax_d) / gmax_d <= 0.10)
    cheb = sd_a <= 0.05 and sd_b <= 0.05
    named = cheb and supp_ok
    ev_al = float(np.std(a_t[::2]) + np.std(a_t[1::2])) / 2.0
    print("    tail constancy: sd/mean alpha = %.3f, beta = "
          "%.3f (bar 0.05); induced support [%.3f, %.3f] vs "
          "measured bulk [%.4f, %.3f] (deepest rung); "
          "period-2 diagnostic: split-sd %.3f vs joint %.3f"
          % (sd_a, sd_b, A_ind, B_ind, gmin_d, gmax_d,
             ev_al, float(np.std(a_t))))
    print("    J_inf head (alpha): %s"
          % " ".join("%.3f" % x for x in al_inf))
    print("    J_inf head (beta):  %s"
          % " ".join("%.3f" % x for x in be_inf))
    check("S1.JID J_INFINITY identification (secondary): "
          "free/Chebyshev tail %s + support match %s -> %s "
          "(typed: Rakhmanov-generic if named -- the chain "
          "carries the bulk support geometry, not the "
          "arithmetic)"
          % (cheb, supp_ok,
             "J-INFINITY-NAMED (free chain on the bulk "
             "support)" if named else "not named"), True)

    # ============================================================== S2
    print("\nS2 -- the preconditioner family: cond trends")
    al_tail = float(np.mean(a_t))
    conds = {"raw": [], "a": [], "b": [], "c": []}
    ok_pd = True
    for kz in kzs:
        fr = frames[kz]
        fp = fr["fp"]
        G, rv = fp["G"], fp["rv"]
        ev = np.linalg.eigvalsh(G)
        conds["raw"].append(float(ev[-1] / ev[0]))
        # (a) J-head deflation
        al, be, Q = chains[kz]
        m = len(al)
        J = np.diag(al)
        for i in range(m - 1):
            J[i, i + 1] = J[i + 1, i] = be[i]
        Ma = Q @ J @ Q.T + al_tail * (np.eye(len(rv))
                                      - Q @ Q.T)
        Ma = 0.5 * (Ma + Ma.T)
        # (b) PNT smooth bulk
        Mb = smooth_bulk_M(fr["rr"], fr["Rm"], fr["Bc"])
        # (c) diagonal
        Mc = np.diag(np.diag(G))
        for nm, M_ in (("a", Ma), ("b", Mb), ("c", Mc)):
            evm = np.linalg.eigvalsh(M_)
            if evm[0] <= 0:
                ok_pd = False
                conds[nm].append(float("inf"))
                continue
            Vm, _, _ = inv_sqrt(M_)
            Gt = Vm @ G @ Vm
            Gt = 0.5 * (Gt + Gt.T)
            evt = np.linalg.eigvalsh(Gt)
            conds[nm].append(float(evt[-1] / max(evt[0],
                                                 1e-300)))
    check("S2.PD every preconditioner is PD on every rung "
          "(M^{-1/2} well-defined)", ok_pd)
    idx = np.arange(len(kzs), dtype=float)
    best_nm, best_med = None, float("inf")
    for nm in ("raw", "a", "b", "c"):
        cv = np.array(conds[nm])
        sp_ = sr.spearman(cv, idx)
        med_f = float(np.median(cv[:third]))
        med_l = float(np.median(cv[-third:]))
        bounded = sp_ <= 0.3 or med_l <= 1.5 * med_f
        print("    %-4s cond: median first/last third %.2e / "
              "%.2e (ratio %.2f), Spearman(cond, rung) = "
              "%+.2f -> %s"
              % (nm, med_f, med_l, med_l / max(med_f, 1e-300),
                 sp_, "BOUNDED" if bounded else "GROWING"))
        if nm != "raw" and med_l < best_med:
            best_nm, best_med = nm, med_l
    print("    best preconditioner: (%s), last-third median "
          "cond %.2e" % (best_nm, best_med))

    # ============================================================== S3
    print("\nS3 -- the certificate retry (preconditioner %s)"
          % best_nm)
    ok_inv = True
    ok_e_all = True
    ok_m_all = True
    mstars = []
    hs_ = []
    for kz in kzs:
        fr = frames[kz]
        fp = fr["fp"]
        G, rv, a_ = fp["G"], fp["rv"], fp["a"]
        if best_nm == "a":
            al, be, Q = chains[kz]
            m = len(al)
            J = np.diag(al)
            for i in range(m - 1):
                J[i, i + 1] = J[i + 1, i] = be[i]
            M_ = Q @ J @ Q.T + al_tail * (np.eye(len(rv))
                                          - Q @ Q.T)
        elif best_nm == "b":
            M_ = smooth_bulk_M(fr["rr"], fr["Rm"], fr["Bc"])
        else:
            M_ = np.diag(np.diag(G))
        M_ = 0.5 * (M_ + M_.T)
        Vm, _, _ = inv_sqrt(M_)
        Gt = Vm @ G @ Vm
        Gt = 0.5 * (Gt + Gt.T)
        rt = Vm @ rv
        direct_raw = float(rv @ np.linalg.solve(G, rv))
        direct_t = float(rt @ np.linalg.solve(Gt, rt))
        ok_inv &= abs(direct_t - direct_raw) \
            / max(abs(direct_raw), 1e-300) <= 1e-8
        m_star, cnd, gmin_t, ok_e, ok_m = cert_depth(
            Gt, rt, a_, M_EXT)
        ok_e_all &= bool(ok_e)
        ok_m_all &= bool(ok_m)
        mstars.append(m_star)
        hs_.append(fr["rr"]["h"])
    check("S3.INV congruence invariance: rt' Gt^{-1} rt == "
          "r' G^{-1} r (rel 1e-8) on every rung", ok_inv)
    check("S3.WRD enclosure + monotonicity wards in the "
          "preconditioned frame", ok_e_all and ok_m_all)
    cert_all = all(m is not None for m in mstars)
    if cert_all:
        mv = np.array(mstars, float)
        tmax = int(np.max(mv[-third:]))
        hmax_ = int(np.max(mv[:-third]))
        sp_mh = sr.spearman(mv, np.array(hs_, float))
        fixed = bool(np.max(mv) <= M_FIX
                     and tmax <= hmax_ + 2)
        print("    m* range [%d, %d]; last-third max %d vs "
              "first-two-thirds max %d; Spearman(m*, h) = "
              "%+.2f; %d/%d rungs at m* <= 17"
              % (int(np.min(mv)), int(np.max(mv)), tmax,
                 hmax_, sp_mh,
                 int(np.sum(mv <= 17)), len(mv)))
    else:
        fixed = False
        print("    %d rungs fail to certify at m <= %d in the "
              "preconditioned frame"
              % (sum(1 for m in mstars if m is None), M_EXT))
    check("S3.G [THE RETRY] fixed-depth certificate family in "
          "the preconditioned frame (all rungs m* <= %d, no "
          "growth): %s" % (M_FIX, fixed), fixed)

    # ============================================================== S4
    print("\nS4 -- Sylvester control (the frame must NOT heal "
          "negativity)")
    rr9 = core.build_window(9)
    a9 = rr9["alpha"]
    N_E = int(math.floor(math.exp(2.0 * a9))) + 1
    lamE = pp.lambda_eps(N_E)
    nn = np.nonzero(np.abs(lamE) > 1e-12)[0]
    syl_ok = True
    for nmc, kw in (("Epstein", dict(comb=(
            np.log(nn.astype(float)),
            2.0 * lamE[nn] / np.sqrt(nn.astype(float))))),
            ("scramble", dict(scramble_seed=1))):
        out = pp.build_rung(9, **kw)
        rrX, DeltaX, GpX, RpX = out[0], out[8], out[6], out[7]
        fpX, BcX = port_frame(DeltaX, GpX, RpX, rrX["h"],
                              rrX["D"])
        GX = fpX["G"]
        gminX = fpX["gmin"]
        if best_nm == "b":
            evX, VpX = np.linalg.eigh(GpX)
            RmX = VpX @ np.diag(evX ** -0.5) @ VpX.T
            MX = smooth_bulk_M(rrX, RmX, BcX)
        elif best_nm == "a":
            alX, beX, QX, _ = lanczos_q(GX, fpX["rv"], M_HEAD)
            mX = len(alX)
            JX = np.diag(alX)
            for i in range(mX - 1):
                JX[i, i + 1] = JX[i + 1, i] = beX[i]
            MX = QX @ JX @ QX.T + al_tail * (
                np.eye(GX.shape[0]) - QX @ QX.T)
        else:
            MX = np.diag(np.abs(np.diag(GX)))
        MX = 0.5 * (MX + MX.T)
        evM = np.linalg.eigvalsh(MX)
        if evM[0] <= 0:
            print("    %-8s: raw gmin = %+.3e; the (%s) "
                  "preconditioner itself is INDEFINITE on this "
                  "comb (lam_min(M) = %+.3e) -- the frame "
                  "cannot even be built: negativity visible at "
                  "the preconditioner (typed)"
                  % (nmc, gminX, best_nm, float(evM[0])))
            continue
        VmX, _, _ = inv_sqrt(MX)
        GtX = VmX @ GX @ VmX
        gtmin = float(np.linalg.eigvalsh(
            0.5 * (GtX + GtX.T))[0])
        heal = gtmin >= 0 and gminX < 0
        syl_ok &= not heal
        print("    %-8s: raw gmin = %+.3e -> preconditioned "
              "gmin = %+.3e (inertia preserved: %s)"
              % (nmc, gminX, gtmin, not heal))
    check("S4.SYL Sylvester: congruence preserves the "
          "negativity of both controls (no healing)", syl_ok)

    # ============================================================== S5
    print("\nS5 -- verdict")
    if fixed and not FAILS:
        verdict = "PRECONDITIONED-FIXED-DEPTH"
    else:
        verdict = "CONDITIONING-INTRINSIC"
    sec = " + J-INFINITY-NAMED" if named else ""
    print("=" * 78)
    print("V -- VERDICT: %s%s" % (verdict, sec))
    print("=" * 78)
    if verdict == "PRECONDITIONED-FIXED-DEPTH":
        print("""    THE COFINAL SHAPE (every arrow typed): source window
    (arch + comb, source-built) -> pole port (closed-form
    a-term, source-built) -> %s preconditioner (SOURCE-BUILT:
    %s) -> Lanczos on the preconditioned bulk (structural) ->
    fixed-depth Gauss-Radau certificate a - U_m* > 0 with m*
    <= %d uniformly (MEASURED on the full ladder) -> s > 0 ->
    tau > 0 (exact Feshbach, warded premise gmin > 0).  THE
    NAMED REMAINING HYPOTHESES for a cofinal statement: (i)
    the uniform validity of the preconditioner construction
    (lam_min of the preconditioned bulk bounded below
    uniformly in h -- measured bounded here, not proven); (ii)
    the J_inf convergence / the stationarity of the
    certificate data along the ladder (measured: %d/%d
    coefficients stable at 5%%); (iii) the closed-form floor
    of the a-term (already source-closed).  NO RH claim.""" % (
            best_nm,
            "the rung's own depth-17 Krylov head + the ladder "
            "tail value" if best_nm == "a" else
            "the PNT-smooth ABS bulk in the same port frame"
            if best_nm == "b" else "diagonal scaling",
            int(np.max(np.array([m for m in mstars]))),
            n5, kmax))
    else:
        grow_txt = ", ".join(
            "%s %.1e->%.1e" % (nm, float(np.median(
                np.array(conds[nm])[:third])),
                float(np.median(np.array(conds[nm])[-third:])))
            for nm in ("raw", "a", "b", "c"))
        print("""    THE TYPED WALL (conditioning form): none of the three
    source preconditioners bounds the effective condition
    number (medians first->last third: %s), %s.  The
    conditioning of the soft port is INTRINSIC at this
    ingredient list: the soft end of the bulk is not the
    smooth geometry (else (b) would flatten it) and not the
    17-mode Krylov head (else (a) would deflate it) -- it is
    distributed arithmetic structure that any certificate
    must resolve mode by mode.  In quadrature coordinates the
    wall is: the certificate depth is the price of the
    cancellation, and no source-side change of metric waives
    it.  NO RH claim.""" % (
            grow_txt,
            "and the retry still shows growing depth"
            if cert_all else
            "and some rungs no longer certify at all in the "
            "best frame"))
    dt = time.time() - T0
    print("-" * 78)
    print("checks: %d run, %d failed%s | runtime %.1f min"
          % (N_CHK, len(FAILS),
             (" [" + ", ".join(FAILS) + "]") if FAILS else "",
             dt / 60.0))
    print("NO RH claim; report only; nothing outside "
          "experiments/ touched.")


if __name__ == "__main__":
    run()
'''

# --------------------------------------------------------------- harness
_PF_RE = re.compile(r"^\s*\[(PASS|FAIL)\]\s+(\S+)", re.M)
_VD_RE = re.compile(r"VERDICT[^\n]*:")


def _probe_file(name):
    cand = os.path.abspath(os.path.join(
        _HERE, os.pardir, "experiments", "tfpt-discovery", name + ".py"))
    return cand if os.path.isfile(cand) else None


def _census(out):
    marks = _PF_RE.findall(out)
    fails = sorted({tok for st, tok in marks if st == "FAIL"})
    verdicts = [ln.strip() for ln in out.splitlines()
                if _VD_RE.search(ln)]
    return len(marks), fails, " | ".join(verdicts)


def _exec_probe(name, src, run_entry=True):
    """Execute one embedded frozen probe source BYTE-EXACT in its own
    module namespace, registered in sys.modules under the probe's
    canonical import name; capture and re-emit stdout; return
    (stdout, exit_code, byte_equal_to_source_file_or_None)."""
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
            entry = mod.__dict__.get("main") or mod.__dict__.get("run")
            if run_entry and callable(entry):
                rc = entry()
                code = 0 if rc is None else int(rc)
        except SystemExit as exc:
            code = 0 if exc.code is None else int(exc.code)
        except Exception:                            # regression guard
            import traceback
            traceback.print_exc(file=sys.stdout)
            code = 99
    out = buf.getvalue()
    sys.stdout.write(out)
    sys.stdout.flush()
    return out, code, same


def _gate(name, out, code, same, exp_n, exp_fails, exp_verdicts,
          exp_code, gates):
    n, fails, verdict = _census(out)
    ok = (n == exp_n and fails == list(exp_fails)
          and all(v in verdict for v in exp_verdicts)
          and code == exp_code and same is not False)
    gates.append(ok)
    prov = ("byte-exact vs experiments source" if same is True else
            "embedded copy (source file not present)" if same is None
            else "SOURCE MISMATCH")
    print("\n[%s] PATTERN GATE %s: %d checks (exp %d) | FAILs %s "
          "(exp %s) | exit %d (exp %d) | %s\n      verdict line(s): %s"
          % ("PASS" if ok else "FAIL", name, n, exp_n,
             ",".join(fails) if fails else "none",
             ",".join(exp_fails) if exp_fails else "none",
             code, exp_code, prov, verdict), flush=True)
    return ok

_PLAN = (
    ('softport_radau17_probe', _SRC_0, 7, ('S2.G2',),
     ('RADAU-DEPTH-GROWS',), 0),
    ('preconditioned_port_probe', _SRC_1, 8, ('S3.G',),
     ('CONDITIONING-INTRINSIC', 'J-INFINITY-NAMED'), 0),
)


def run():
    t0 = time.time()
    print("=" * 74)
    print('v867 -- PRIME.SOFTPORT.RADAU.01 + PRIME.PORT.CONDITIONING.01')
    print('(the quadrature reach: Gauss-Radau certificates for s > 0')
    print('EXIST on EVERY rung -- the kz-16 Neumann frontier killed --')
    print('but the depth grows as m* ~ sqrt(cond(G)) (Spearman +0.99);')
    print('all three source preconditioners fail informatively: the')
    print('conditioning is INTRINSIC -- the soft end is a continuum')
    print('edge of distributed arithmetic structure; NO RH claim)')
    print("=" * 74, flush=True)
    gates = []
    for name, src, exp_n, exp_fails, exp_verdicts, exp_code in _PLAN:
        print("\n" + "-" * 74)
        print("EMBEDDED FROZEN PROBE: %s" % name)
        print("-" * 74, flush=True)
        out, code, same = _exec_probe(name, src)
        _gate(name, out, code, same, exp_n, exp_fails,
              exp_verdicts, exp_code, gates)
    ok = all(gates)
    print("\n" + "=" * 74)
    print("v867: %d/%d probe pattern gates passed | runtime %.1f s"
          % (sum(gates), len(gates), time.time() - t0))
    print('Two frozen-honest FAILs kept and pattern-gated (the m ~ 17')
    print('prediction failed as stated; the preconditioned retry still')
    print('grows): in quadrature coordinates the wall is the depth-')
    print('growth law -- the certificate depth is the price of the')
    print('cancellation, and no source-side change of metric waives it.')
    print('J_inf is NAMED: the free Chebyshev chain on the bulk support')
    print('(Rakhmanov-generic typed).')
    print("[%s] v867 VERDICT GATE: RADAU-DEPTH-GROWS + CONDITIONING-INTRINSIC (both FAILs frozen-honest)"
          % ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(run())
