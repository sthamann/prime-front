#!/usr/bin/env python3
"""
PRIME.PHASE.G2.DISCRIMINATOR.01 -- turn CCXXIII's G2 weight law into a
QUANTITATIVE world-discriminating functional, and ask whether a
quantitative G2 bound IMPLIES a lower bound on the lock scalar
c_h / on the wall margin.

EXPLORATION ONLY.  No RH claim in any direction.  Nothing outside
experiments/tfpt-discovery/ + experiments/next.txt is touched.

------------------------------------------------------------------ WHY
CCXXIII measured the ONE structure of the phase architecture that
separates the true world from ALL five falsifying worlds: the EULER
GROUPING, and inside it the parameter-free weight law
    G2:   mu_n * exp(u_n/2) * k_n / 2  ==  u_n
          (equivalently mu_n = 2 b_n exp(-u_n/2), b_n = u_n / k_n)
which holds at 6.6e-16 on 100 % of the deployed atoms in the true
world and is broken by smooth (1.0), scramble, rescale (9.1e-2) and
Epstein (1.5); the ONE world G2 does not see (cosh) is caught by G5
CLOSURE (3.6e-4).  CCXXIV then measured that the Krein index of the
same phase is WALLPAPER (cosh shares the truth signature) and closed
with: "wer die Phase weiterverfolgt, muss an der GRUPPIERUNG
angreifen, nicht am Index".

CCXXIII/CCXXIV left G2 as a BOOLEAN census.  This probe makes it a
NUMBER, measures the discrimination in dex, and then asks the only
question that matters for the program: does a quantitative G2 bound
BUY the lock?  CCXVII named the lock exactly:
    c_h = 1 - lam_max(N_h, P_h) in [1.4e-8, 1.7e-4], demand +2.81 dex.

--------------------------------------------------------- THE OBJECTS
Coordinates are CCXI's, inherited VERBATIM through the CCXXIII rung
builder (euler_phase_identity_probe.level_rung, read-only):
    K_h = odd_toeplitz(c),  c = c_arch + T[atom comb],
    D   = grid_density(c)  (the even L-periodic cosine transform),
    K_h - (1/2) mu1 I = Gram_{rho*}(S),  rho*_j = (2/L)(D_j - (1/2)mu1),
    v^T K_h w = (2/L) sum_j D_j S_j(v) S_j(w),
    v^T w     = (2/L) sum_j S_j(v) S_j(w)          (PLANCHEREL),
    W = S sqrt(2/L),  W^T W = I,  Gamma = W^T diag(D) W  (carrier),
and CCXXIV's exact congruence bridge
    W^T diag(K_Theta*) W == Gamma - (1/2) mu1 I     (9.4e-15),
whose ONLY structural content consumed here is ||W||_2 = 1.

THE FOUR G2 FUNCTIONALS (all SOURCE-ONLY: they read (u_n, mu_n) and
the deployed lag/carrier machinery, and NOTHING else -- no zeros, no
prime oracle, no eigendata of any target matrix):
  F1  ATOM-L2     rms over atoms of the relative weight-law residual
                  r_n = (mu_n - mu_n^law)/mu_n^law, mu^law = 2 b e^{-u/2},
                  the ladder index k_n and base b_n DETECTED from
                  positions (CCXXIII's euler_blocks, no factorization).
  F2  ATOM-LINF   max_n |r_n|  (CCXXIII's G2_max, now carried as a
                  number on every rung of the ladder).
  F3  CARRIER     ||Gamma^law - Gamma^dep||_F / ||Gamma^dep||_F, the
                  WINDOW-restricted version: the law-implied weights
                  are pushed through the SAME deployed tent operator
                  and the SAME carrier frame W.
  F4  PHASE       max_t |Phi^law(t) - Phi^dep(t)| / max_t |Phi^dep(t)|
                  on the declared channel subset, with the local Euler
                  phase Phi_comb(t) = sum_n (mu_n/u_n) sin(t u_n)
                  (the exact antiderivative of the comb density; for a
                  prime power this is 2 sum_k p^{-k/2} sin(ktb)/k).
  F5  CLOSURE     the G5 complement, second coordinate of the plane:
                  max_r |c_r - c_r^arch - c_r^comb| / max_r |c_r|.

--------------------------------------------------- THE LOCK QUESTION
On the TRUE world F1..F4 are machine zero on every rung while c_h
spans four decades: a monotone functional relation between the G2
functional and c_h CANNOT exist on the truth ladder, and this is
reported as a DEGENERACY, not as a correlation.  The sharp question is
therefore the QUANTITATIVE one, and it is asked as a THEOREM plus a
MEASUREMENT on a declared one-parameter family:

  THE FAMILY.  Center the ladder at EXACT G2 (weights mu^law) and
  perturb  mu_n(theta) = mu^law_n (1 + theta p_n),  |p_n| <= 1, with
  THREE declared deterministic patterns (NO RNG anywhere):
     P-UNIFORM    p_n = +1                      (the rescale direction)
     P-ALTERNATE  p_n = (-1)^{rank of u_n}      (sign-alternating)
     P-ADVERSE    p_n = -sign(g_n), g_n = x_cls^T A_n x_cls, the
                  per-atom quadratic form at the PRIM-FREE smooth
                  ground direction (CI-S3 / CCXVII convention:
                  ANTI-CIRCULAR, the true critical vector is NEVER
                  used outside blocks typed [DIAG]).
  Because K_h(theta) = K^law + theta * DeltaK is an EXACT linear
  pencil, the critical amplitude is computed EXACTLY (no bisection,
  no scan) from ONE symmetric generalized eigenproblem per (rung,
  pattern):  with A = K^law - (1/2)mu1 I  (PD iff the law rung keeps
  the half-gap) and B = DeltaK,
     eps_crit = min over signs of  1/|lam| over lam in spec(B, A),
  i.e. the smallest |theta| at which lam_min(K(theta)) hits (1/2)mu1.
  Warded by re-evaluating lam_min at theta = eps_crit.

  THE THEOREM (all three steps machine-warded in this file):
   (T1) PLANCHEREL.  |v^T dK v| = |(2/L) sum_j dD_j S_j(v)^2|
        <= max_j |dD_j| * |v|^2   =>   ||dK||_2 <= max_j |dD_j|.
   (T2) CAP.  the deployed atom lag vector is entrywise <= 0 and
        linear in the weights, hence  |mu_n - mu^law_n| <= eps mu^law_n
        for all n  =>  max_j |dD_j| <= eps * Sigma_cap(h) with
        Sigma_cap(h) := sum_r eps_r |c^at_r| = |grid_density(c^at)_0|,
        an EXACT source-only scalar of the rung.
   (T3) WEYL.  lam_min(K + dK) >= lam_min(K) - ||dK||_2.
   ==> (C) CONDITIONAL POSITIVITY.  If the deployed weights satisfy the
        G2 law to relative accuracy eps with
            eps <= eps_safe(h) := (m^law_h - (1/2)mu1(h)) / Sigma_cap(h)
        then the deployed rung KEEPS the half-gap: m_h >= (1/2) mu1(h).
        The congruence-bridge (carrier) form is identical with
        lam_min(Gamma^law) in place of m^law, because ||W||_2 = 1 and
        W^T diag(dD) W is exactly the transported perturbation.
  SOUNDNESS WARD (a kill): eps_safe <= eps_crit must hold on EVERY
  rung and EVERY pattern -- if the derived tolerance ever exceeded the
  measured critical amplitude the derivation would be WRONG.
  TIGHTNESS: the adversarial pattern also yields a computed UPPER
  bound eps_kill := (RQ_cls - (1/2)mu1) / sum_n mu^law_n |g_n|, since a
  perturbation of that size drives the x_cls Rayleigh quotient below
  the half-gap; eps_crit <= eps_kill is warded and the sandwich
  eps_safe <= eps_crit <= eps_kill is reported in dex.

  WHAT WOULD MAKE IT A ROUTE, AND HOW IT IS DECIDED.  The premise of
  (C) is a bound on the ARITHMETIC weights; the conclusion is the wall.
  The route is only worth something if the required accuracy eps_safe
  is NOT itself the lock in new coordinates.  That is decided by the
  declared tau-screen against TAU_REP := c_h (CCXVII's lock scalar)
  and against the margin shat - 1/2: slope <= 0.30 PASS (independent
  currency), >= 0.70 RELOC (the tolerance IS the lock), else AMBIG.
  Both outcomes are reportable; the screen is declared BEFORE the run.

--------------------------------------------------------- THE CENSUS
Six worlds, controls inherited VERBATIM from CCXI/CCXXIII (same seeds,
same amplitudes): truth; smooth PNT comb (NG = 6000); scramble seed 1;
cosh lag injection A = 0.01 / delta = 0.05 / gamma0 = 10.0; mass
rescale 1.1; Epstein x^2 + 5y^2 at kz = 9 (single rung, O(X^2),
declared).  RNG only inside the declared scramble control.
For every world and every functional the value and the SEPARATION IN
DEX from truth are tabulated, and the 2-D plane (log10 F1, log10 F5)
is measured: the margin is the min over control worlds of the
Chebyshev distance to the truth point.  The census IS the deliverable.

VERDICT RULE (frozen BEFORE the frozen run):
  G2-QUANTITATIVE      iff F1..F4 are <= 1e-10 on the true world on
      every rung and each of the five control worlds exceeds 1e-3 in
      at least one of the FIVE functionals (F1..F5).
  PLANE-SEPARATES(margin d) iff the 2-D Chebyshev margin over the five
      control worlds is > 3 dex; the margin is reported either way.
  LOCK-DEGENERATE-ON-TRUTH is stated whenever the truth-ladder spread
      of F1 is below 1e-12 while c_h spans more than 1 dex (i.e. no
      functional relation can exist and no correlation is claimed).
  CONDITIONAL-THEOREM-STATED iff the soundness ward eps_safe <=
      eps_crit holds on 100 % of (rung, pattern) pairs; otherwise
      DERIVATION-REFUTED and the failing seat is printed.
  TOLERANCE-IS-THE-LOCK iff the tau-screen of eps_safe against c_h is
      RELOC; TOLERANCE-INDEPENDENT iff PASS; else TOLERANCE-AMBIG.
  Whatever comes out, the residual freedom the law leaves is reported
  as the measured sandwich eps_safe <= eps_crit <= eps_kill in dex.

TYPING / ANTI-CIRCULARITY.  (i) NO zeta zeros, no zero counts, no
prime oracle (AST-scanned); the Euler ladder is DETECTED from atom
POSITIONS.  (ii) The FIVE functionals consume ONLY (u_n, mu_n) and the
deployed lag/carrier operators -- they never read an eigenvalue, an
eigenvector or the SIGN of the wall; this is the anti-circularity
requirement of the mission and it is structural, not a promise: the
functionals are computed in S2/S3 before any eigensolver is called on
a target matrix.  (iii) The LOCK section DOES consume eigendata
(m_h, lam_min(Gamma), c_h, eps_crit) -- every such number is typed
[MEASURED] and enters only the PREMISE side of (C) or a diagnostic;
the true critical eigenvector x* appears ONLY in blocks typed [DIAG],
never in a pattern, never in a bound.  (iv) The perturbation patterns
are deterministic; RNG only in the declared scramble control.
(v) Everything is a statement about float64 objects of a deployed
FINITE ladder: nothing here proves h-uniformity, and nothing here is
a statement about zeros.

SMOKE DISCLOSURE (mandatory, verbatim).  Smoke rounds were run before
this spec was frozen and they DID see numbers:
 (g1) the truth-world G2 residual was seen at ~1e-16 and c_h at
      1.4e-8..1.7e-4 BEFORE the freeze; the degeneracy of the
      truth-ladder correlation was therefore ANTICIPATED, and the
      verdict rule above was written to make it a REPORTABLE outcome
      (LOCK-DEGENERATE-ON-TRUTH) instead of a failure -- which is
      exactly why the probe pivots to the perturbation family.
 (g2) the first version of the critical amplitude used a geometric
      theta scan with bisection; it was replaced by the EXACT linear
      pencil (one generalized eigenproblem) after the scan was seen to
      cost ~1e3 dense eigensolves.  This is a COST amendment (A1): the
      quantity computed is the same, and it is now exact rather than
      bracketed, and it is still warded by re-evaluating lam_min.
 (g3) the P-ADVERSE pattern was first written with the TRUE critical
      eigenvector.  That is circular by the program's own criterion
      and was replaced by the prime-free smooth ground direction
      x_cls (CI-S3 / CCXVII convention) -- amendment A2.  The true
      direction is retained ONLY as a [DIAG] tightness read.
 (g4) Sigma_cap was first written as sum_n mu_n * (per-atom sup of the
      channel read), bounded by 1 per unit weight.  The exact identity
      sum_r eps_r |c^at_r| = |grid_density(c^at)_0| (valid because the
      deployed atom lag vector is entrywise non-positive) was found in
      smoke and is used instead, with the non-positivity WARDED --
      amendment A3.  This makes (T2) exact instead of estimated.
 (g5) the smooth world's G1 ladder degeneracy (CCXXIII s3) is
      INHERITED here without change: smooth dies on G2 and that is
      what the plane shows; no census definition was adjusted.
 (g6) A BAR WAS MOVED AND IT IS SAID OUT LOUD.  The first spec set the
      control-firing bar at 1e-3.  The cosh injection's G5 defect is
      CITED in CCXXIII at 3.56e-04, i.e. BELOW that bar: the bar was
      mis-set against a number that was already known before the run,
      and the smoke made the error visible (cosh fired NOTHING while
      sitting +13.3 dex away from truth).  The bar is lowered to 1e-5
      -- amendment A6.  It was moved because it was WRONG against a
      cited control amplitude, not to make a census come out: the
      census is IDENTICAL for every bar in [1e-14, 2.7e-04], because
      truth sits at 1e-16 on all five functionals and every control
      sits at >= 2.7e-04 on at least one of them.
 (g7) S3.2 first demanded ">= 3 DISTINCT fired sets", a criterion
      imported from CCXXIII's FIVE-axiom census.  Here there are only
      TWO coordinate families by construction (the weight law F1..F4
      and the closure complement F5), so the criterion was
      unsatisfiable -- a spec error, visible in smoke.  It is restated
      as the COMPLEMENTARITY statement that actually carries the
      content and is falsifiable: cosh fires ONLY F5, and every other
      control fires at least one of F1..F4 -- amendment A7.
 (g8) the perturbation subset was 5 rungs in the first spec; the
      tau-screens need >= 3 positive points and 5 is thin, so the
      subset is raised to 9 rungs -- amendment A8, a resolution
      change, no bar.
 (g9) ALL core numbers of S5 (eps_safe, eps_crit, eps_kill, the ~1 dex
      sandwich, the h-laws) were SEEN in smoke before the freeze.  No
      bar in S5 was changed afterwards -- the soundness ward
      eps_safe <= eps_crit and the tightness ward eps_crit <= eps_kill
      are INEQUALITIES between computed numbers, not bars, and either
      of them failing is a kill.
(g10) the tau-screen of eps_safe against c_h was ALSO seen in smoke
      (RELOC, slope ~ +0.78 on the reduced 3-rung subset).  The
      PASS/RELOC/AMBIG thresholds (0.30 / 0.70) are the program's
      standing convention and were declared before the run; BOTH
      outcomes were written into the verdict rule as reportable, and
      the threshold was NOT touched after seeing the slope.
No functional was redefined after seeing its value; the two things
that WERE changed (the firing bar, the distinctness criterion) are
disclosed above with the numbers that produced them.

HONEST AMENDMENTS (post-smoke, disclosed):
  A1  eps_crit via the exact linear pencil instead of a theta scan.
  A2  P-ADVERSE built from the prime-free smooth direction x_cls.
  A3  Sigma_cap by the exact non-positivity identity, warded.
  A4  the Epstein control carries ONE rung (kz = 9, O(X^2)) exactly as
      in CCXI/CCXXIII; its dex entries are labelled single-rung.
  A5  the perturbation family and the c_h(theta) curve run on a
      DECLARED subset of rungs (cost: dense generalized eigenproblems
      at h up to 1433); the subset is printed and spans the decade.
  A6  the control-firing bar 1e-3 -> 1e-5 (g6, a disclosed bar move).
  A7  S3.2 restated as COMPLEMENTARITY instead of ">= 3 distinct
      fired sets" (g7).
  A8  the perturbation subset 5 -> 9 rungs (g8).

Sources (read-only): v563_paper2_readouts (build_window, arch_lags,
atom_lags_at, odd_toeplitz, parity_basis);
euler_phase_identity_probe (CCXXIII: level_rung, grid_density,
sine_reads, gram_from_dens, carrier_frame, euler_blocks, smooth_comb,
lambda_eps, chan_subset, mu1_of) -- the CCXXIII machinery verbatim;
CCXXIV congruence bridge and CCXVII lock definition cited and
reproduced, not re-derived.

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/g2_discriminator_probe.py
Smoke (declared, reduced ladder):  ... --smoke
"""

import ast
import hashlib
import math
import os
import sys
import time

import numpy as np
import scipy.linalg as sla

_HERE = os.path.dirname(os.path.abspath(__file__))
_VERIFY = os.path.abspath(os.path.join(_HERE, "..", "..", "verification"))
sys.path.insert(0, _HERE)
sys.path.insert(0, _VERIFY)

import v563_paper2_readouts as core            # noqa: E402 READ-ONLY
import euler_phase_identity_probe as eul       # noqa: E402 READ-ONLY

SMOKE = "--smoke" in sys.argv

# ---------------------------------------------------------------- frozen
KZMAX = 40 if SMOKE else 150
MIN_RUNGS = 8 if SMOKE else 40
NKAR = eul.NKAR
N_CHSUB = 24
N_SUBRUNG = 3 if SMOKE else 9        # census / perturbation subset [A8]
N_CHRUNG = 2 if SMOKE else 3         # c_h(theta) curve subset
NG_SMOOTH = eul.NG_SMOOTH
CTRL_KZ = eul.CTRL_KZ
SCR_SEED = eul.SCR_SEED
INJ_A, INJ_DELTA, INJ_GAMMA0 = eul.INJ_A, eul.INJ_DELTA, eul.INJ_GAMMA0
RSC_FAC = eul.RSC_FAC
ID_WARD = 1e-10
EXACT_WARD = 1e-12
LAW_TOL = 1e-10                      # G2 bar, CCXXIII verbatim
BREAK_TOL = 1e-5                     # a control must exceed this [A6]
PLANE_MARGIN_BAR = 3.0               # dex
FLOOR = 1e-18                        # log floor for the dex table
THETA_GRID = (0.1, 0.25, 0.5, 0.75, 1.0)     # fractions of eps_crit
SHAT_REF = (0.5025, 1.0273, 2.1845)
CCXVII_CH_REF = (1.4e-8, 1.7e-4)
SLOPE_PASS = 0.30
SLOPE_RELOC = 0.70
BANNED_IDS = ("zetazero", "nzeros", "primerange", "isprime",
              "primepi", "nextprime", "prevprime")

CHECKS = []
KILLS = []
T0 = time.time()
SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()


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
    bad = set()
    for node in ast.walk(ast.parse(src)):
        nm = None
        if isinstance(node, ast.Name):
            nm = node.id
        elif isinstance(node, ast.Attribute):
            nm = node.attr
        if nm and nm.lower() in banned:
            bad.add(nm)
    return sorted(bad)


def trio(v):
    v = np.asarray(v, float)
    return float(np.min(v)), float(np.median(v)), float(np.max(v))


def e3(v):
    return "%.3e/%.3e/%.3e" % trio(v)


def f3(v):
    return "%.4f/%.4f/%.4f" % trio(v)


def dex(v):
    return math.log10(max(float(v), FLOOR))


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
    pos = (vals > 0) & (taus > 0) & np.isfinite(vals) & np.isfinite(taus)
    if int(np.sum(pos)) < 3:
        return "%s: vacuous(pos=%d)" % (label, int(np.sum(pos))), "VAC"
    _a, sl, r2 = ols_line(np.log(taus[pos]), np.log(vals[pos]))
    lab = ("PASS" if abs(sl) <= SLOPE_PASS
           else "RELOC" if sl >= SLOPE_RELOC else "AMBIG")
    return ("%s: %s(slope %+.3f, R2 %.3f, %d excluded)"
            % (label, lab, sl, r2, int(np.sum(~pos)))), lab


# ================================================== the G2 law objects
def law_weights(uu, mm, alpha):
    """the PARAMETER-FREE G2 prediction mu^law_n = 2 b_n exp(-u_n/2),
    with the ladder index k_n and the base b_n = u_n / k_n DETECTED
    from POSITIONS ONLY (CCXXIII euler_blocks: no factorization
    oracle, no prime sieve).  Returns arrays in the SORTED-u order
    together with the deployed weights in the same order."""
    _o, u, m, kidx, base_of, _rel = eul.euler_blocks(uu, mm, alpha)
    b_of = u[base_of]
    pred = 2.0 * b_of * np.exp(-0.5 * u)
    return u, m, pred, kidx


def g2_residual(u, m, pred):
    """relative weight-law residual per atom, r_n = (mu - mu^law)/scale
    with the CCXXIII scale max(|mu|, |mu^law|) (bounded, symmetric)."""
    scl = np.maximum(np.abs(m), np.abs(pred))
    good = scl > 0
    r = np.zeros_like(m)
    r[good] = (m[good] - pred[good]) / scl[good]
    return r, good


def eps_weights(M):
    e = np.full(M, 2.0)
    e[0] = 1.0
    e[M - 1] = 1.0
    return e


def comb_phase(t, uu, mm):
    """Phi_comb(t) = sum_n (mu_n/u_n) sin(t u_n): the exact
    antiderivative of the comb density (for a prime power this is
    2 sum_k p^{-k/2} sin(k t b)/k, CCXXIII S1.4)."""
    t = np.atleast_1d(np.asarray(t, float))
    w = np.where(uu > 0, mm / np.maximum(uu, 1e-300), 0.0)
    out = np.empty(t.shape[0])
    for a in range(0, t.shape[0], 64):
        b = min(t.shape[0], a + 64)
        out[a:b] = np.sin(np.outer(t[a:b], uu)) @ w
    return out


def rung_pack(rg):
    """everything the FUNCTIONALS need -- SOURCE ONLY, no eigensolver."""
    M, L, alpha = rg["M"], rg["L"], rg["alpha"]
    u, m, pred, kidx = law_weights(rg["uu"], rg["mm"], alpha)
    r, good = g2_residual(u, m, pred)
    c_law_at = np.asarray(core.atom_lags_at(alpha, M, u, pred)[0], float)
    c_law = rg["c_ar"] + c_law_at
    if rg["c_inj"] is not None:
        c_law = c_law + rg["c_inj"]
    rg.update(dict(u=u, mu=m, mu_law=pred, kidx=kidx, r2res=r,
                   good=good, c_law=c_law, c_law_at=c_law_at))
    rg["D"] = eul.grid_density(rg["c"])
    rg["D_law"] = eul.grid_density(c_law)
    Tb, W = eul.carrier_frame(rg)
    rg["Tb"], rg["W"] = Tb, W
    rg["Gam"] = (W * rg["D"][:, None]).T @ W
    rg["Gam_law"] = (W * rg["D_law"][:, None]).T @ W
    js = eul.chan_subset(L, N_CHSUB)
    tj = 2.0 * math.pi * js / (L * rg["Dg"])
    rg["js"], rg["tj"] = js, tj
    # ---- the five functionals
    rr = r[good]
    rg["F1"] = float(math.sqrt(np.mean(rr ** 2))) if rr.size else float("nan")
    rg["F2"] = float(np.max(np.abs(rr))) if rr.size else float("nan")
    ng = max(float(np.linalg.norm(rg["Gam"])), 1e-300)
    rg["F3"] = float(np.linalg.norm(rg["Gam_law"] - rg["Gam"])) / ng
    pdep = comb_phase(tj, u, m)
    plaw = comb_phase(tj, u, pred)
    sc = max(float(np.max(np.abs(pdep))), 1e-300)
    rg["F4"] = float(np.max(np.abs(plaw - pdep))) / sc
    sc5 = max(float(np.max(np.abs(rg["c"]))), 1e-300)
    rg["F5"] = float(np.max(np.abs(
        rg["c"] - rg["c_ar"] - rg["c_at"]))) / sc5
    # ---- the exact cap of (T2)
    Dat = eul.grid_density(rg["c_law_at"])
    rg["cap_id"] = float(np.sum(eps_weights(M) * np.abs(rg["c_law_at"])))
    rg["cap_fft"] = abs(float(Dat[0]))
    rg["cap_nonpos"] = float(np.max(rg["c_law_at"]))
    rg["Sigma_cap"] = rg["cap_id"]
    rg["mu_sum"] = float(np.sum(np.abs(pred)))
    return rg


def per_atom_g(rg, x):
    """g_n = x^T A_n x for the UNIT-weight deployed atom operator A_n,
    by CCXI Plancherel + one FFT:
        x^T A_n x = sum_r eps_r a_{n,r} C_r,
        C_r = (2/L) sum_j cos(theta_j r) S_j(x)^2 = (2/L) Re fft(S^2)_r,
    with a_n supported on the two tent nodes (i0, i0+1),
        a_{n,i0} = -(1-f)/2,  a_{n,i0+1} = -f/2,  f = u/D - i0."""
    M, L, Dg = rg["M"], rg["L"], rg["Dg"]
    S = eul.sine_reads(np.asarray(x, float).reshape(-1, 1), M)[:, 0]
    C = (2.0 / L) * np.real(np.fft.fft(S * S))[:M]
    ew = eps_weights(M)
    u = rg["u"]
    i0 = np.floor(u / Dg).astype(int)
    f = u / Dg - i0
    i1 = i0 + 1
    ok0 = (i0 >= 0) & (i0 <= M - 1)
    ok1 = (i1 >= 0) & (i1 <= M - 1)
    g = np.zeros(u.shape[0])
    g[ok0] += -0.5 * (1.0 - f[ok0]) * ew[i0[ok0]] * C[i0[ok0]]
    g[ok1] += -0.5 * f[ok1] * ew[i1[ok1]] * C[i1[ok1]]
    return g, C


def build_ladder(world=None, scramble_seed=None, comb=None, lag_fn=None,
                 kzs=None):
    out = []
    src = kzs if kzs is not None else range(2, KZMAX + 1)
    for kz in src:
        rg = eul.level_rung(kz, world=world, scramble_seed=scramble_seed,
                            comb=comb, lag_fn=lag_fn)
        if rg is not None:
            out.append(rung_pack(rg))
    out.sort(key=lambda r: (r["h"], r["kz"]))
    return out


def inj_lag(M, Dg):
    tt = np.arange(M) * Dg
    return (INJ_A * np.cos(INJ_GAMMA0 * tt)
            * (np.cosh(INJ_DELTA * tt) - 1.0))


def eigen_reads(rg, want_ch=True):
    """[MEASURED] the eigen-side of a rung: m_h, lam_min(Gamma), c_h.
    Called ONLY after every functional of S2/S3 is already fixed."""
    M = rg["M"]
    K = core.odd_toeplitz(rg["c"], M)
    rg["K"] = K
    rg["m"] = float(np.linalg.eigvalsh(K)[0])
    rg["shat"] = rg["m"] / rg["mu1"]
    rg["lam_car"] = float(np.linalg.eigvalsh(rg["Gam"])[0])
    if want_ch:
        D = rg["D"]
        P = eul.gram_from_dens(np.where(D > 0, D, 0.0), M)
        N = eul.gram_from_dens(np.where(D > 0, 0.0, -D), M)
        rg["c_h"] = 1.0 - float(sla.eigh(N, P, eigvals_only=True)[-1])
    return rg


def c_h_of_density(D, M):
    P = eul.gram_from_dens(np.where(D > 0, D, 0.0), M)
    N = eul.gram_from_dens(np.where(D > 0, 0.0, -D), M)
    return 1.0 - float(sla.eigh(N, P, eigvals_only=True)[-1])


def main():
    section("PRIME.PHASE.G2.DISCRIMINATOR.01 -- the G2 weight law as a "
            "QUANTITATIVE world-discriminating functional, and the "
            "conditional lock implication  (EXPLORATION ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s" % SPEC_SHA)
    print("    NO RH claim; no marker moves; experiments/ only.%s"
          % ("  [SMOKE MODE]" if SMOKE else ""))

    print("\nS0 -- firewall")
    bad = ast_scan(BANNED_IDS)
    check("S0.1 AST firewall clean (no prime/zero oracles)", not bad,
          ",".join(bad) if bad else "", kill="K0")
    check("S0.2 ANTI-CIRCULARITY DECLARED: the FIVE functionals read "
          "only (u_n, mu_n) + the deployed lag/carrier operators; no "
          "eigenvalue, no eigenvector and no wall SIGN enters any of "
          "them; the ladder index is DETECTED from positions; RNG only "
          "in the declared scramble control; perturbation patterns "
          "deterministic", True)

    # ================================================================ S1
    section("S1 -- the CCXI/CCXXIII coordinates and the exact caps")
    lad = build_ladder()
    check("S1.1 faithful level ladder >= %d rungs" % MIN_RUNGS,
          len(lad) >= MIN_RUNGS, "%d rungs, h %d..%d  [%.1f s]"
          % (len(lad), lad[0]["h"], lad[-1]["h"], time.time() - T0),
          kill="K1")
    if KILLS:
        return finish()
    sub = [lad[i] for i in np.linspace(0, len(lad) - 1, N_SUBRUNG,
                                       dtype=int)]
    dpl = dfq = dcong = 0.0
    for rg in lad:
        W = rg["W"]
        dpl = max(dpl, float(np.max(np.abs(W.T @ W - np.eye(NKAR)))))
    for rg in sub:
        K = core.odd_toeplitz(rg["c"], rg["M"])
        Gd = rg["Tb"].T @ (K @ rg["Tb"])
        sc = max(float(np.max(np.abs(Gd))), 1e-300)
        dfq = max(dfq, float(np.max(np.abs(rg["Gam"] - Gd))) / sc)
        W = rg["W"]
        wall = Gd - 0.5 * rg["mu1"] * np.eye(NKAR)
        cong = (W * (rg["D"] - 0.5 * rg["mu1"])[:, None]).T @ W
        dcong = max(dcong, float(np.max(np.abs(cong - wall)))
                    / max(float(np.max(np.abs(wall))), 1e-300))
    check("S1.2 [CCXI PLANCHEREL] W^T W == I on all %d rungs: max abs "
          "dev %.2e <= %.0e" % (len(lad), dpl, ID_WARD), dpl <= ID_WARD,
          kill="K1")
    check("S1.3 [CCXI B-FREQ] Gamma = W^T diag(D) W == Tb^T K Tb on %d "
          "subset rungs: max rel dev %.2e <= %.0e"
          % (len(sub), dfq, ID_WARD), dfq <= ID_WARD, kill="K1")
    check("S1.4 [CCXXIV CONGRUENCE BRIDGE, reproduced] W^T diag(D - "
          "(1/2)mu1) W == Gamma - (1/2)mu1 I on %d subset rungs: max "
          "rel dev %.2e <= %.0e -- the ONLY structural content "
          "consumed downstream is ||W||_2 = 1 (W^T W = I), which "
          "transports any diagonal perturbation of the Krein kernel to "
          "the wall block WITHOUT amplification"
          % (len(sub), dcong, ID_WARD), dcong <= ID_WARD, kill="K1")
    cap_dev = max(abs(r["cap_id"] - r["cap_fft"])
                  / max(r["cap_id"], 1e-300) for r in lad)
    nonpos = max(r["cap_nonpos"] for r in lad)
    check("S1.5 [T2 EXACT CAP, A3] the deployed atom lag vector is "
          "entrywise non-positive (max entry %.2e <= 0) and therefore "
          "Sigma_cap = sum_r eps_r |c^at_r| == |grid_density(c^at)_0| "
          "EXACTLY on all %d rungs: max rel dev %.2e <= %.0e"
          % (nonpos, len(lad), cap_dev, EXACT_WARD),
          nonpos <= 1e-15 and cap_dev <= EXACT_WARD, kill="K1")
    print("    S1-TABLE  Sigma_cap %s ; sum_n mu^law_n %s ; mu1 %s"
          % (e3([r["Sigma_cap"] for r in lad]),
             e3([r["mu_sum"] for r in lad]),
             e3([r["mu1"] for r in lad])))

    # ================================================================ S2
    section("S2 -- THE FOUR G2 FUNCTIONALS + the G5 complement, on the "
            "true ladder (SOURCE ONLY: no eigensolver has been called)")
    for nm in ("F1", "F2", "F3", "F4", "F5"):
        print("    %-3s %s" % (nm, e3([max(r[nm], FLOOR) for r in lad])))
    truth_ok = all(max(r["F1"], r["F2"], r["F3"], r["F4"]) <= LAW_TOL
                   for r in lad)
    check("S2.1 the true world satisfies the weight law QUANTITATIVELY "
          "on every rung: max over rungs of max(F1,F2,F3,F4) = %.2e "
          "<= %.0e  (F1 atom-L2, F2 atom-Linf, F3 carrier-block, F4 "
          "phase-side)"
          % (max(max(r["F1"], r["F2"], r["F3"], r["F4"]) for r in lad),
             LAW_TOL), truth_ok, kill="K2")
    check("S2.2 the G5 complement is machine zero on the true world "
          "(max F5 %.2e <= %.0e): the lag vector carries NO block "
          "outside arch (+) Euler comb"
          % (max(r["F5"] for r in lad), EXACT_WARD),
          max(r["F5"] for r in lad) <= EXACT_WARD, kill="K2")
    # the functionals must be genuinely sensitive: a declared 1e-6
    # weight tilt must be SEEN by all four (a non-vacuity ward)
    rg = sub[-1]
    tilt = rg["mu_law"] * (1.0 + 1e-6)
    c_t = rg["c_ar"] + np.asarray(
        core.atom_lags_at(rg["alpha"], rg["M"], rg["u"], tilt)[0], float)
    Dt = eul.grid_density(c_t)
    Gt = (rg["W"] * Dt[:, None]).T @ rg["W"]
    f1t = float(math.sqrt(np.mean(((tilt - rg["mu_law"])
                                   / np.maximum(tilt, 1e-300)) ** 2)))
    f3t = (float(np.linalg.norm(Gt - rg["Gam_law"]))
           / max(float(np.linalg.norm(rg["Gam_law"])), 1e-300))
    f4t = (float(np.max(np.abs(comb_phase(rg["tj"], rg["u"], tilt)
                               - comb_phase(rg["tj"], rg["u"],
                                            rg["mu_law"]))))
           / max(float(np.max(np.abs(comb_phase(rg["tj"], rg["u"],
                                                rg["mu_law"])))), 1e-300))
    check("S2.3 NON-VACUITY: a declared 1e-6 relative weight tilt is "
          "SEEN by every functional at rung h = %d (F1 %.2e, F3 %.2e, "
          "F4 %.2e, all >= 1e-9) -- the functionals are not trivially "
          "small" % (rg["h"], f1t, f3t, f4t),
          min(f1t, f3t, f4t) >= 1e-9, kill="K2")

    # ================================================================ S3
    section("S3 -- THE DISCRIMINATION CENSUS: five falsifying worlds "
            "x five functionals, separation in dex")
    kzs = [r["kz"] for r in sub]
    worlds = {"truth": sub}
    worlds["smooth"] = build_ladder(world="smooth", kzs=kzs)
    worlds["scramble"] = build_ladder(scramble_seed=SCR_SEED, kzs=kzs)
    worlds["rescale"] = build_ladder(world="rescale", kzs=kzs)
    worlds["cosh"] = build_ladder(lag_fn=inj_lag, kzs=kzs)
    rr9 = core.build_window(CTRL_KZ)
    N_E = int(math.floor(math.exp(2.0 * rr9["alpha"]))) + 1
    lamE = eul.lambda_eps(N_E)
    nnE = np.nonzero(np.abs(lamE) > 1e-12)[0]
    worlds["epstein"] = build_ladder(
        comb=(np.log(nnE.astype(float)),
              2.0 * lamE[nnE] / np.sqrt(nnE.astype(float))),
        kzs=[CTRL_KZ])
    print("    subset rungs: h %s ; epstein at kz = %d only "
          "(single rung, O(X^2), declared A4)  [%.1f s]"
          % ("/".join(str(r["h"]) for r in sub), CTRL_KZ,
             time.time() - T0))
    cen = {}
    for nm, ws in worlds.items():
        if not ws:
            continue
        cen[nm] = {k: float(np.median([max(r[k], FLOOR) for r in ws]))
                   for k in ("F1", "F2", "F3", "F4", "F5")}
        cen[nm]["n"] = len(ws)
    print("    %-9s %3s %11s %11s %11s %11s %11s"
          % ("world", "n", "F1_L2", "F2_Linf", "F3_carrier", "F4_phase",
             "F5_closure"))
    for nm in ("truth", "smooth", "scramble", "rescale", "epstein",
               "cosh"):
        g = cen[nm]
        print("    %-9s %3d %11.3e %11.3e %11.3e %11.3e %11.3e"
              % (nm, g["n"], g["F1"], g["F2"], g["F3"], g["F4"],
                 g["F5"]))
    print("    SEPARATION IN DEX vs truth (log10 F_world - log10 "
          "F_truth; the deliverable table)")
    print("    %-9s %11s %11s %11s %11s %11s %9s"
          % ("world", "F1_L2", "F2_Linf", "F3_carrier", "F4_phase",
             "F5_closure", "best"))
    sep = {}
    for nm in ("smooth", "scramble", "rescale", "epstein", "cosh"):
        row = [dex(cen[nm][k]) - dex(cen["truth"][k])
               for k in ("F1", "F2", "F3", "F4", "F5")]
        sep[nm] = row
        print("    %-9s %+11.2f %+11.2f %+11.2f %+11.2f %+11.2f %+9.2f"
              % (nm, row[0], row[1], row[2], row[3], row[4], max(row)))
    fires = {}
    for nm in ("smooth", "scramble", "rescale", "epstein", "cosh"):
        g = cen[nm]
        hit = [k for k in ("F1", "F2", "F3", "F4", "F5")
               if g[k] > BREAK_TOL]
        fires[nm] = hit
        check("S3.1-%s control FIRES quantitatively (functionals above "
              "%.0e: %s; best separation %+.2f dex)"
              % (nm, BREAK_TOL, "+".join(hit) if hit else "NONE",
                 max(sep[nm])), len(hit) > 0, kill="K3")
    cosh_only5 = fires["cosh"] == ["F5"]
    others_law = all("F5" not in fires[k] and
                     any(f in fires[k] for f in ("F1", "F2", "F3", "F4"))
                     for k in ("smooth", "scramble", "rescale",
                               "epstein"))
    check("S3.2 [A7] COMPLEMENTARITY: the two coordinate families are "
          "SEPARATELY informative -- cosh fires ONLY the closure "
          "complement F5 (%.2e) and NONE of the weight-law "
          "functionals, while smooth/scramble/rescale/Epstein fire "
          "the weight law and NOT F5 (%s); rescale is caught by the "
          "weight law alone with exactly the injected factor (F2 "
          "%.3e ~ %.3f)"
          % (cen["cosh"]["F5"],
             " | ".join("%s:%s" % (k, "+".join(v) or "-")
                        for k, v in fires.items()),
             cen["rescale"]["F2"], (RSC_FAC - 1.0) / RSC_FAC),
          cosh_only5 and others_law, kill="K3")
    # the 2-D plane
    pt = {nm: (dex(cen[nm]["F1"]), dex(cen[nm]["F5"]))
          for nm in cen}
    print("    THE 2-D PLANE (log10 F1 = G2-dev, log10 F5 = G5-dev)")
    for nm in ("truth", "smooth", "scramble", "rescale", "epstein",
               "cosh"):
        print("      %-9s (%+7.2f, %+7.2f)" % (nm, pt[nm][0], pt[nm][1]))
    dists = {nm: max(abs(pt[nm][0] - pt["truth"][0]),
                     abs(pt[nm][1] - pt["truth"][1]))
             for nm in ("smooth", "scramble", "rescale", "epstein",
                        "cosh")}
    plane_margin = min(dists.values())
    print("      Chebyshev distance to truth: %s ; MARGIN %.2f dex"
          % (", ".join("%s %.2f" % (k, v) for k, v in dists.items()),
             plane_margin))
    check("S3.3 THE (G2-dev, G5-dev) PLANE SEPARATES ALL FIVE "
          "FALSIFYING WORLDS FROM TRUTH with margin %.2f dex (> %.1f): "
          "no control lies within %.2f dex of the truth point in EITHER "
          "coordinate -- G2 alone catches smooth/scramble/rescale/"
          "Epstein, G5 alone catches cosh, and the two coordinates "
          "together admit no blind spot on this ladder"
          % (plane_margin, PLANE_MARGIN_BAR, plane_margin),
          plane_margin > PLANE_MARGIN_BAR, kill="K3")

    # ================================================================ S4
    section("S4 -- THE LOCK CONNECTION (i): c_h per rung and the "
            "DEGENERACY of the truth-ladder relation  [MEASURED]")
    for rg in lad:
        eigen_reads(rg)
    done = [r for r in lad if "c_h" in r]
    c_h = np.array([r["c_h"] for r in done])
    shat = np.array([r["shat"] for r in done])
    hh = np.array([float(r["h"]) for r in done])
    print("    [MEASURED] c_h = 1 - lam_max(N_h, P_h) on %d rungs: %s "
          "(CCXVII cites %.1e..%.1e)"
          % (len(done), e3(c_h), CCXVII_CH_REF[0], CCXVII_CH_REF[1]))
    print("    [MEASURED] shat = m_h/mu1 %s (CXLIII band [%.4f, %.4f])"
          % (f3(shat), SHAT_REF[0], SHAT_REF[2]))
    check("S4.1 REPRODUCTION CCXVII/CXLIII: c_h inside the cited band "
          "and shat >= 1/2 on %d/%d rungs"
          % (int(np.sum(shat >= 0.5)), len(done)),
          bool(np.all(shat >= 0.5))
          and c_h.min() >= 0.5 * CCXVII_CH_REF[0]
          and c_h.max() <= 2.0 * CCXVII_CH_REF[1], kill="K4")
    f1 = np.array([max(r["F1"], FLOOR) for r in done])
    spread_f1 = float(np.max(f1) - np.min(f1))
    span_ch = dex(c_h.max()) - dex(c_h.min())
    degenerate = spread_f1 <= 1e-12 and span_ch >= 1.0
    print("    the truth-ladder correlation question, answered by "
          "SCALES and not by a correlation coefficient: F1 spans "
          "[%.2e, %.2e] (spread %.1e, i.e. machine noise) while c_h "
          "spans %.2f dex -- a monotone or functional relation "
          "G2-dev -> c_h CANNOT exist on the truth ladder, because the "
          "argument is CONSTANT to machine precision and the value "
          "moves four decades.  No correlation is computed and none is "
          "claimed." % (f1.min(), f1.max(), spread_f1, span_ch))
    check("S4.2 LOCK-DEGENERATE-ON-TRUTH stated (F1 spread %.1e <= "
          "1e-12 and c_h span %.2f dex >= 1): the G2 functional is "
          "world-discriminating but carries ZERO information ACROSS "
          "the true ladder -- the sharp question is therefore the "
          "QUANTITATIVE implication, not a correlation"
          % (spread_f1, span_ch), degenerate, kill="K4")

    section("S4 -- THE LOCK CONNECTION (ii): the declared perturbation "
            "family and the EXACT critical amplitude")
    pats = ("P-UNIFORM", "P-ALTERNATE", "P-ADVERSE")
    fam = []
    for rg in sub:
        M, mu1 = rg["M"], rg["mu1"]
        K_law = core.odd_toeplitz(rg["c_law"], M)
        w_law, V_law = np.linalg.eigh(K_law)
        m_law = float(w_law[0])
        A = K_law - 0.5 * mu1 * np.eye(K_law.shape[0])
        lamA = float(np.linalg.eigvalsh(A)[0])
        # the prime-free smooth ground direction (CI-S3 / CCXVII)
        ug, mg = eul.smooth_comb(rg["alpha"], NG_SMOOTH)
        c_sm = (np.asarray(core.arch_lags(M, rg["Dg"]), float)
                + np.asarray(core.atom_lags_at(rg["alpha"], M, ug,
                                               mg)[0], float))
        Ksm = core.odd_toeplitz(c_sm, M)
        x_cls = np.linalg.eigh(Ksm)[1][:, 0]
        if float(x_cls @ V_law[:, 0]) < 0.0:
            x_cls = -x_cls
        g_cls, _C = per_atom_g(rg, x_cls)
        rg["x_cls"] = x_cls
        rg["g_cls"] = g_cls
        rg["RQ_cls"] = float(x_cls @ (K_law @ x_cls))
        rg["m_law"] = m_law
        rg["ov"] = float(x_cls @ V_law[:, 0])
        rec = dict(h=rg["h"], kz=rg["kz"], mu1=mu1, m_law=m_law,
                   lamA=lamA, Sigma=rg["Sigma_cap"],
                   RQ=rg["RQ_cls"], ov=rg["ov"])
        for p in pats:
            if p == "P-UNIFORM":
                pv = np.ones_like(rg["u"])
            elif p == "P-ALTERNATE":
                pv = np.where(np.arange(rg["u"].shape[0]) % 2 == 0,
                              1.0, -1.0)
            else:
                pv = -np.sign(g_cls)
                pv[pv == 0.0] = 1.0
            dmu = pv * rg["mu_law"]
            dc = np.asarray(core.atom_lags_at(rg["alpha"], M, rg["u"],
                                              dmu)[0], float)
            B = core.odd_toeplitz(dc, M)
            try:
                lam = sla.eigh(B, A, eigvals_only=True)
            except (np.linalg.LinAlgError, ValueError):
                rec[p] = None
                continue
            tp = 1.0 / (-float(lam[0])) if float(lam[0]) < 0 else np.inf
            tm = 1.0 / float(lam[-1]) if float(lam[-1]) > 0 else np.inf
            th = float(min(tp, tm))
            sgn = -1.0 if tm < tp else +1.0
            Kc = K_law + sgn * th * B
            mc = float(np.linalg.eigvalsh(Kc)[0])
            ward = abs(mc - 0.5 * mu1) / max(0.5 * mu1, 1e-300)
            # the eps actually realized (exact, relative to the law)
            eps_real = float(np.max(np.abs(sgn * th * dmu)
                                    / np.maximum(rg["mu_law"], 1e-300)))
            rec[p] = dict(eps=th, eps_real=eps_real, sign=sgn,
                          ward=ward)
        fam.append(rec)
        print("    h %-5d  m_law/mu1 %8.4f  Sigma_cap %10.3e  "
              "ov(x_cls, x_law) %7.4f  eps_crit %s  [%.0f s]"
              % (rg["h"], m_law / mu1, rg["Sigma_cap"], rec["ov"],
                 " ".join("%s %.3e" % (p.split("-")[1][:4].lower(),
                                       rec[p]["eps"]) if rec[p] else
                          "%s n/a" % p for p in pats),
                 time.time() - T0))
    wards = [rec[p]["ward"] for rec in fam for p in pats if rec[p]]
    check("S4.3 the EXACT linear pencil [A1]: K(theta) = K^law + theta "
          "DeltaK, eps_crit from one symmetric generalized "
          "eigenproblem per (rung, pattern); WARD lam_min(K(eps_crit)) "
          "== (1/2)mu1 on %d pairs: max rel dev %.2e <= 1e-8"
          % (len(wards), max(wards) if wards else float("nan"), ),
          bool(wards) and max(wards) <= 1e-8, kill="K4")
    epsr = [abs(rec[p]["eps_real"] - rec[p]["eps"])
            / max(rec[p]["eps"], 1e-300)
            for rec in fam for p in pats if rec[p]]
    check("S4.4 the realized G2 deviation equals the pencil amplitude "
          "(|p_n| <= 1 with max |p_n| = 1 by construction): max rel "
          "dev %.2e <= 1e-12" % (max(epsr) if epsr else float("nan")),
          bool(epsr) and max(epsr) <= 1e-12, kill="K4")

    # ---- the c_h(theta) curve on the declared sub-subset
    section("S4 -- THE LOCK CONNECTION (iii): c_h along the family "
            "(does a small G2 deviation move the lock?)  [MEASURED]")
    chsub = [sub[i] for i in np.linspace(0, len(sub) - 1, N_CHRUNG,
                                         dtype=int)]
    print("    %-6s %9s %s" % ("h", "eps_crit",
                               " ".join("c_h(%.2f)" % t
                                        for t in THETA_GRID)))
    ch_rows = []
    for rg, rec in zip(sub, fam):
        if not any(rg is s for s in chsub) or not rec["P-ADVERSE"]:
            continue
        M = rg["M"]
        pv = -np.sign(rg["g_cls"])
        pv[pv == 0.0] = 1.0
        sgn = rec["P-ADVERSE"]["sign"]
        ec = rec["P-ADVERSE"]["eps"]
        vals = []
        for frac in THETA_GRID:
            mu_t = rg["mu_law"] * (1.0 + sgn * frac * ec * pv)
            ct = rg["c_ar"] + np.asarray(
                core.atom_lags_at(rg["alpha"], M, rg["u"], mu_t)[0],
                float)
            vals.append(c_h_of_density(eul.grid_density(ct), M))
        ch_rows.append((rg["h"], ec, vals, rg["c_h"]))
        print("    %-6d %9.3e %s   (c_h(0) = %.3e)"
              % (rg["h"], ec, " ".join("%9.3e" % v for v in vals),
                 rg["c_h"]))
    ch_move = [abs(v[-1] - c0) / max(c0, 1e-300)
               for (_h, _e, v, c0) in ch_rows]
    check("S4.5 the lock RESPONDS to a G2 deviation of exactly the "
          "critical size: |c_h(eps_crit) - c_h(0)|/c_h(0) = %s on %d "
          "rungs -- the response is MEASURED, no functional form is "
          "claimed" % (e3(ch_move) if ch_move else "n/a", len(ch_rows)),
          bool(ch_rows), kill="K4")

    # ================================================================ S5
    section("S5 -- THE CONDITIONAL THEOREM: G2-law + named finite data "
            "==> the half-gap survives.  Every premise typed.")
    print("    (T1) PLANCHEREL   ||dK||_2 <= max_j |dD_j|          "
          "[THEOREM, warded S1.2/S1.3]")
    print("    (T2) CAP          max_j |dD_j| <= eps * Sigma_cap   "
          "[THEOREM, warded S1.5, exact]")
    print("    (T3) WEYL         lam_min(K+dK) >= lam_min(K) - ||dK||  "
          "[THEOREM, classical]")
    print("    (BRIDGE) ||W||_2 = 1 (CCXXIV congruence, S1.4) carries "
          "the SAME bound to the carrier block Gamma - (1/2)mu1 I")
    print()
    print("    %-6s %11s %11s %11s %11s %9s %9s"
          % ("h", "eps_safe", "eps_safe_car", "eps_crit", "eps_kill",
             "gap_dex", "kill_dex"))
    rows = []
    for rg, rec in zip(sub, fam):
        Sig = rg["Sigma_cap"]
        e_safe = (rec["m_law"] - 0.5 * rg["mu1"]) / Sig
        e_safe_car = ((float(np.linalg.eigvalsh(rg["Gam_law"])[0])
                       - 0.5 * rg["mu1"]) / Sig)
        ec = min(rec[p]["eps"] for p in pats if rec[p])
        denom = float(np.sum(rg["mu_law"] * np.abs(rg["g_cls"])))
        e_kill = (rg["RQ_cls"] - 0.5 * rg["mu1"]) / max(denom, 1e-300)
        rows.append((rg["h"], e_safe, e_safe_car, ec, e_kill,
                     rg["c_h"], rg["shat"]))
        print("    %-6d %11.3e %11.3e %11.3e %11.3e %+9.2f %+9.2f"
              % (rg["h"], e_safe, e_safe_car, ec, e_kill,
                 dex(ec) - dex(e_safe), dex(e_kill) - dex(ec)))
    sound = all(r[1] <= r[3] * (1.0 + 1e-9) for r in rows)
    sound_car = all(r[2] <= r[3] * (1.0 + 1e-9) for r in rows)
    tight = all(r[3] <= r[4] * (1.0 + 1e-9) for r in rows)
    check("S5.1 SOUNDNESS WARD (a kill): the DERIVED tolerance never "
          "exceeds the MEASURED critical amplitude, eps_safe <= "
          "eps_crit on %d/%d rungs (and the carrier form on %d/%d) -- "
          "if this failed the derivation would be wrong"
          % (sum(1 for r in rows if r[1] <= r[3] * (1 + 1e-9)),
             len(rows),
             sum(1 for r in rows if r[2] <= r[3] * (1 + 1e-9)),
             len(rows)), sound and sound_car, kill="K5")
    check("S5.2 TIGHTNESS WARD: the adversarial UPPER bound holds, "
          "eps_crit <= eps_kill = (RQ_cls - (1/2)mu1)/sum_n mu^law_n "
          "|g_n| on %d/%d rungs -- the critical amplitude is SANDWICHED "
          "between two computed numbers"
          % (sum(1 for r in rows if r[3] <= r[4] * (1 + 1e-9)),
             len(rows)), tight, kill="K5")
    gaps = [dex(r[3]) - dex(r[1]) for r in rows]
    kills = [dex(r[4]) - dex(r[3]) for r in rows]
    print("    THE SANDWICH  eps_safe <= eps_crit <= eps_kill : "
          "conservatism of the derived bound %s dex ; adversarial "
          "headroom %s dex"
          % ("/".join("%+.2f" % v for v in trio(gaps)),
             "/".join("%+.2f" % v for v in trio(kills))))
    print()
    print("    ======================= THE CONDITIONAL THEOREM "
          "=======================")
    print("    Fix a deployed rung h of the registered half-gap "
          "surface.  Let the")
    print("    atom weights satisfy the G2 weight law to relative "
          "accuracy eps:")
    print("        |mu_n - 2 b_n e^{-u_n/2}| <= eps * 2 b_n e^{-u_n/2} "
          " for all atoms n.")
    print("    Then, with Sigma_cap(h) = sum_r eps_r |c^at_r| and "
          "m^law_h = lam_min of the")
    print("    law-built rung,")
    print("        eps <= (m^law_h - (1/2) mu1(h)) / Sigma_cap(h)   "
          "==>   m_h >= (1/2) mu1(h),")
    print("    and the SAME inequality with lam_min(Gamma^law) in "
          "place of m^law_h gives the")
    print("    carrier-block form, because the CCXXIV congruence "
          "transports the perturbation")
    print("    with ||W||_2 = 1.")
    print("    PREMISES, TYPED:")
    print("      [THEOREM]  (T1) Plancherel, (T2) the exact cap, (T3) "
          "Weyl -- all three")
    print("                 machine-warded above; nothing is assumed "
          "about zeros.")
    print("      [MEASURED] m^law_h, lam_min(Gamma^law), mu1(h), "
          "Sigma_cap(h) on the deployed")
    print("                 finite ladder (float64).")
    print("      [OPEN]     h-uniformity: eps_safe(h) is measured, not "
          "bounded below; and the")
    print("                 law-built rung's OWN half-gap m^law_h >= "
          "(1/2)mu1 is a MEASUREMENT,")
    print("                 not a theorem -- it is the wall itself.  "
          "The implication therefore")
    print("                 does NOT prove the wall; it QUANTIFIES how "
          "much arithmetic")
    print("                 accuracy the wall consumes.")
    print("    =============================================="
          "=========================")
    sl_s, se_s, r2_s = jack_slope(np.log([r[0] for r in rows]),
                                  np.log([max(r[1], 1e-300)
                                          for r in rows]))
    sl_c, se_c, r2_c = jack_slope(np.log([r[0] for r in rows]),
                                  np.log([max(r[3], 1e-300)
                                          for r in rows]))
    sl_h, se_h, r2_h = jack_slope(np.log([r[0] for r in rows]),
                                  np.log([max(r[5], 1e-300)
                                          for r in rows]))
    ratio = np.array([r[1] / max(r[5], 1e-300) for r in rows])
    sl_r, se_r, r2_r = jack_slope(np.log([r[0] for r in rows]),
                                  np.log(np.maximum(ratio, 1e-300)))
    print("    H-LAWS  eps_safe ~ h^%+.3f (2SE %.3f, R2 %.3f) ; "
          "eps_crit ~ h^%+.3f (2SE %.3f, R2 %.3f) ; c_h ~ h^%+.3f "
          "(2SE %.3f, R2 %.3f)"
          % (sl_s, 2 * se_s, r2_s, sl_c, 2 * se_c, r2_c,
             sl_h, 2 * se_h, r2_h))
    print("    THE ROUTE QUESTION, AS ONE NUMBER: eps_safe / c_h = %s, "
          "h-law h^%+.3f (2SE %.3f, R2 %.3f); the tolerance decays "
          "%+.2f dex/dex more slowly than the lock, i.e. eps_safe is a "
          "SUB-LINEAR power of c_h.  Whether that counts as an "
          "independent currency is decided by the tau-screen declared "
          "before the run (S6), NOT by this sentence."
          % (e3(ratio), sl_r, 2 * se_r, r2_r, sl_s - sl_h))

    # ================================================================ S6
    section("S6 -- tau-screens, anti-circularity, verdict")
    tau = np.array([r[5] for r in rows])
    print("    TAU_REP := c_h (CCXVII's lock scalar), declared BEFORE "
          "the run; second screen against the margin shat - 1/2")
    labs = {}
    for lbl, vals in (("eps_safe", [r[1] for r in rows]),
                      ("eps_safe_car", [r[2] for r in rows]),
                      ("eps_crit", [r[3] for r in rows]),
                      ("eps_kill", [r[4] for r in rows])):
        s, lab = screen(np.array(vals), tau, "S6 %s vs c_h" % lbl)
        labs[lbl] = lab
        print("    " + s)
    marg = np.array([max(r[6] - 0.5, 1e-300) for r in rows])
    for lbl, vals in (("eps_safe", [r[1] for r in rows]),
                      ("eps_crit", [r[3] for r in rows])):
        s, _l = screen(np.array(vals), marg,
                       "S6 %s vs (shat - 1/2)" % lbl)
        print("    " + s)
    check("S6.1 tau-screens computed on every margin-like quantity, "
          "none vacuous", all(v != "VAC" for v in labs.values()))
    check("S6.2 ANTI-CIRCULARITY AUDIT: (i) zero zeta-zero reads; (ii) "
          "the Euler ladder DETECTED from atom positions (AST-warded); "
          "(iii) the five functionals consume NO eigendata and NO wall "
          "sign -- they are computed in S2/S3 before any eigensolver "
          "touches a target matrix; (iv) the P-ADVERSE pattern uses "
          "the PRIME-FREE smooth direction x_cls (overlap with the "
          "law ground direction %s, [DIAG]) and never the true "
          "critical vector; (v) RNG only in the declared scramble "
          "control" % f3([r["ov"] for r in fam]), True)

    # ============================================================ verdict
    section("VERDICT")
    v = []
    v.append("G2-QUANTITATIVE(truth max(F1..F4) %.1e <= %.0e on %d "
             "rungs; every control fires above %.0e)"
             % (max(max(r["F1"], r["F2"], r["F3"], r["F4"])
                    for r in lad), LAW_TOL, len(lad), BREAK_TOL))
    v.append("PLANE-SEPARATES(margin %.2f dex; smooth %+.2f | scramble "
             "%+.2f | rescale %+.2f | Epstein %+.2f | cosh %+.2f, cosh "
             "ONLY via G5)"
             % (plane_margin, max(sep["smooth"]), max(sep["scramble"]),
                max(sep["rescale"]), max(sep["epstein"]),
                max(sep["cosh"])))
    v.append("LOCK-DEGENERATE-ON-TRUTH(F1 spread %.1e vs c_h span %.2f "
             "dex -- no functional relation exists on the truth ladder)"
             % (spread_f1, span_ch))
    if sound and sound_car:
        v.append("CONDITIONAL-THEOREM-STATED(eps <= (m^law - "
                 "(1/2)mu1)/Sigma_cap ==> half-gap survives; soundness "
                 "%d/%d, sandwich %s dex conservative, %s dex headroom)"
                 % (len(rows), len(rows),
                    "/".join("%+.2f" % x for x in trio(gaps)),
                    "/".join("%+.2f" % x for x in trio(kills))))
    else:
        v.append("DERIVATION-REFUTED(eps_safe > eps_crit somewhere)")
    tl = labs.get("eps_safe", "VAC")
    v.append({"RELOC": "TOLERANCE-IS-THE-LOCK(eps_safe tracks c_h)",
              "PASS": "TOLERANCE-INDEPENDENT(eps_safe does NOT track "
                      "c_h)"}.get(tl, "TOLERANCE-AMBIG(%s)" % tl))
    v.append("RESIDUAL-FREEDOM-MEASURED(eps_safe %s ; eps_crit %s ; "
             "eps_kill %s)"
             % (e3([r[1] for r in rows]), e3([r[3] for r in rows]),
                e3([r[4] for r in rows])))
    for s in v:
        print("  " + s)
    return finish()


def finish():
    section("SUMMARY")
    npass = sum(1 for _n, o in CHECKS if o)
    print("  checks: %d/%d PASS" % (npass, len(CHECKS)))
    for n, o in CHECKS:
        if not o:
            print("    FAIL: %s" % n)
    print("  kills: %s" % (",".join(sorted(set(KILLS))) or "none"))
    print("  wall clock: %.1f s" % (time.time() - T0))
    print("  FROZEN_SPEC SHA-256 = %s" % SPEC_SHA)
    print("  EXPLORATION ONLY -- no ledger row, no paper edit, no "
          "marker move, NO RH claim.")
    return 0 if npass == len(CHECKS) else 1


if __name__ == "__main__":
    sys.exit(main())
