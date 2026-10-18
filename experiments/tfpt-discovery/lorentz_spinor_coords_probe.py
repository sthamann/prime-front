"""PRIME.LORENTZ.SPINOR.01 -- the null-cone coordinate change for the
open near-collinearity problem (EXPLORATION ONLY, experiments/).

THE NEW EXACT OBSERVATIONS to verify first [E neu]:
  with M(t,x,y) = [[t+x, y],[y, t-x]]  (det = t^2 - x^2 - y^2):
  (1) M(5,-3,4) = [[2,4],[4,8]] = 2 (1,2)^T (1,2) -- the boundary null
      vector (g_car, -N_fam, |mu4|) is a RANK-ONE SPINOR SQUARE with
      spinor (1,2);
  (2) the Euclid parametrization (i,j) |-> (i^2+j^2, -(i^2-j^2), -2ij)
      sends the measured locking direction (2,-1) to exactly (5,-3,4):
      the locking direction IS the spinor square root of the compiler
      vector (M(Eu(i,j)) = 2 (j,-i)^T (j,-i) identically; (j,-i) at
      (2,-1) is (-1,-2) ~ (1,2), orthogonal to (2,-1)).

CORPUS ANCHORS (read-only, cited):
  * T170-TH4 (bilinear_sieve / tfpt_prime_front): the determinant
    polarisation on 2x2 symmetric blocks is the rank-3 form
    [[0,1,0],[1,0,0],[0,0,-2]], signature (1,2) -- Lorentz geometry.
  * v576 C3.1: the leading modes-(1,2) profile [[1,2],[2,4]] has
    Lorentz image L(X) = (X11+X22, X11-X22, 2 X12) = (5,-3,4), the
    Pythagorean triple of (g_car, N_fam, |mu4|), typed COMPRESSION.
  * v586: the pencil locking direction drifts (v2/v1 from -1.73 at
    h = 184 to -1.22 at h = 1445), 1/log h limit -0.551, consistent
    with the (2,-1) null ray (slope -1/2), NOT settled; h = 1292
    anomalous by declaration.
  * v563 build_window / frame_a_zones: the deployed frame-A ladder
    with the near-collinear lock block Ahat = B - S (onem = det/
    (a11 a22) ~ h^-3, T166/T170 -- the NON-UNIFORM raw matrix margin).

THE PROGRAMME (frozen): reparametrize the near-collinear 2x2 blocks
projectively, Ahat = lambda (1,r)^T (1,r)/(1+r^2) + tau P_perp
(eigendecomposition; lambda = lambda_max, r = dominant spinor slope,
tau = lambda_min = transversal energy), plus the Lorentz vector
u = (a11+a22, a11-a22, 2 a12) with Q(u) = t^2-x^2-y^2 = 4 det Ahat
and the projective null-cone distance delta_null = Q/(t^2+x^2+y^2),
and the anchored cross-ratio chain
    q_k = CR(r_k, r_{k+1}; 2, -1/2) = [g(r_{k+1})/g(r_k)],
    g(r) = (r - 2)/(r + 1/2)   (Moebius: boundary spinor slope 2 -> 0,
                                its orthogonal -1/2 -> infinity),
the projective contraction factor per rung.

THE QUESTION (the decider): does the coordinate change turn the
non-uniform matrix estimates into a ONE-DIMENSIONAL monotone
projective quantity?  Measured (frozen, oscillation-aware):
  (a) is r(h) monotone/Cauchy where the raw margins (onem, det) were
      not uniform?
  (b) does the transversal energy tau stay positive on every regular
      rung (the reserve), and what is its decay class?
  (c) does the cross-ratio chain show a stable law (contraction
      q_k < 1 per rung / constant)?

FROZEN BARS AND ENUMS (declared before any number):
  E-part: all integer/symbolic identities EXACT (sympy simplify == 0).
  Q4DET: Q(u) == 4 det Ahat per rung -- the identity is SYMBOLIC
         (E1.1); the float check uses the v692-style conditioning bar
         100 eps (t^2+x^2+y^2)/|4 det| (cancellation-limited quantity)
  BAR_EIG    = 1e-9   rel: eigen-reconstruction residual per rung
  MON_BAR    = 0.90   fraction of increments of r with the majority sign
  KEN_BAR    = 0.80   |Kendall tau| of r vs h
  CAUCHY_BAR = 0.50   range(second half of r) / range(all r)
  FIT_R2     = 0.50   R^2 of the 1/log h fit (v586 convention)
  RHO_TOL    = 0.20   |rho_inf + 1/2| for the null-slope fit (v586 bar)
  R_TOL      = 0.80   |r_inf - 2| for the spinor-slope fit (declared
                      wide: r = -1/rho is nonlinear in the fit variable)
  CR_FRAC    = 0.85   fraction of rungs with strict contraction q_k < 1
  BAR_SCR    = 5.0    scramble must-break factor on |onem| (corpus x49)
  N_RAND     = 200    random-slope control sequences (frozen seed)
  RAND_PCT   = 95     real monotone fraction must exceed this percentile
  Anomalous h = 1292 excluded by declaration (v586); incomplete combs
  (X > ATOM_MAX) flagged and excluded from the trend statistics.

VERDICT ENUM (frozen):
  LORENTZ-COORDS-IMPROVE  -- (a) monotone AND Cauchy AND 1/log h fit
      lands on the spinor axis (rho_inf ~ -1/2 or r_inf ~ 2), (b) tau
      positive on all regular rungs, (c) q_k < 1 on >= CR_FRAC of the
      chain, and all three controls fire.  The named next analytic
      step becomes a 1D monotonicity statement (stated in L5).
  LORENTZ-COORDS-NEUTRAL  -- no improvement: the coordinate change is
      typed decorative.
  LORENTZ-COORDS-REVEAL   -- not IMPROVE, but the new coordinates
      expose a different clean structure (declared: |r - 2| decreasing
      on >= 0.85 of rungs while r itself non-monotone, OR the CR chain
      constant at CV <= 0.10 while monotonicity fails) -- described
      exactly.

HONESTY: this is a COORDINATE-CHANGE DIAGNOSTIC, not a positivity
theorem.  The corpus already states the exact null direction stands
while the measured approach rate (1/log h, v586) misses the success
threshold (v581 transport killed).  The probe decides only whether
the projective coordinates improve the uniformity picture.  NO RH
claim.  Both outcomes are typed.

L3b (POST-FIRST-RUN DESCRIPTION, declared as such -- radical honesty):
the first frozen run (2026-08-06, h-ordered ladder) returned
LORENTZ-COORDS-REVEAL via the declared CV clause (monotone fraction
0.591 / Kendall 0.613 in h-order; anchored-CR CV 0.084 <= 0.10).  Its
per-rung table showed the revealed structure: r appears STRICTLY
MONOTONE in the window width alpha -- the h-order oscillation is the
alpha-vs-h jitter of the frame-A scan.  L3b measures exactly that
(same bars MON_BAR/KEN_BAR/CAUCHY_BAR/CR_FRAC applied to the
alpha-ordered ladder, plus 1/alpha and power-law fits of 2 - r and
the log-linear onem law in alpha).  L3b is the REQUIRED description
of the REVEAL enum, NOT a preregistered discovery, and it does NOT
change the frozen h-order verdict.  Also post-first-run: the Q4DET
float bar was corrected from a mis-specified fixed 1e-9 to the
conditioning-aware bar above (first run measured worst rel 2.1e-9,
exactly the eps ||u||^2 / 4 det cancellation floor; the identity
itself is symbolic).

FIREWALL: v563/v586-machinery imported/reproduced READ-ONLY; no zeta
zero is read anywhere (AST-checked); deterministic (RNG only in the
declared random-slope control, frozen seed); no file outside
experiments/ is touched; no marker moves; the ledger is untouched.
"""
import ast
import math
import os
import sys
import time

import numpy as np
import sympy as sp

_here = os.path.dirname(os.path.abspath(__file__))
for _cand in (os.path.join(_here, "..", "..", "verification"), _here):
    if os.path.exists(os.path.join(_cand, "v563_paper2_readouts.py")):
        sys.path.insert(0, os.path.abspath(_cand))
        break

import v563_paper2_readouts as core     # noqa: E402  (READ-ONLY)
import tfpt_constants as tc             # noqa: E402  (READ-ONLY)

T0 = time.time()
FAILS = []
N_CHK = 0

# ------------------------------------------------- frozen bars / constants
Q4_COND_FAC = 100.0           # v692-style conditioning factor on eps
BAR_EIG = 1.0e-9
MON_BAR = 0.90
KEN_BAR = 0.80
CAUCHY_BAR = 0.50
FIT_R2 = 0.50
RHO_TOL = 0.20
R_TOL = 0.80
CR_FRAC = 0.85
CR_CONST_CV = 0.10
REVEAL_FRAC = 0.85
BAR_SCR = 5.0
N_RAND = 200
RAND_PCT = 95
SEED_RAND = 20260806          # frozen; used ONLY in the random control
SCR_SEEDS = (1, 2, 3)         # v586 D5.1 scramble seeds, verbatim
ANOMALOUS_H = 1292            # v586 declaration
ABS_MU4 = 4                   # |mu4| = |Z/4| (v576 C3.1 / tfpt_1 convention)


def check(name, ok, detail=""):
    global N_CHK
    N_CHK += 1
    if not ok:
        FAILS.append(name.split()[0])
    print("[%s] %s%s" % ("PASS" if ok else "FAIL", name,
                         (": " + detail) if detail else ""))


def ast_zero_firewall(src_path):
    with open(src_path, "r", encoding="utf-8") as fh:
        tree = ast.parse(fh.read())
    hits = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            f = node.func
            if isinstance(f, ast.Attribute) and f.attr in (
                    "zetazero", "nzeros", "second_sheet_zero", "find_zeros"):
                hits.append(f.attr)
            if isinstance(f, ast.Name) and f.id in ("zetazero", "nzeros",
                                                    "find_zeros"):
                hits.append(f.id)
    return not hits


def kendall_tau(x, y):
    n = len(x)
    conc = disc = 0
    for i in range(n):
        for j in range(i + 1, n):
            s = (x[j] - x[i]) * (y[j] - y[i])
            if s > 0:
                conc += 1
            elif s < 0:
                disc += 1
    tot = n * (n - 1) // 2
    return (conc - disc) / max(tot, 1)


def fit_invlog(h, y):
    """y = y_inf + b / log h  (v586 D4.1 convention): (y_inf, b, R^2)."""
    h = np.asarray(h, float)
    y = np.asarray(y, float)
    A = np.column_stack([1.0 / np.log(h), np.ones(len(h))])
    coef, *_ = np.linalg.lstsq(A, y, rcond=None)
    resid = y - A @ coef
    r2 = 1.0 - float((resid ** 2).sum()) \
        / max(float(((y - y.mean()) ** 2).sum()), 1e-300)
    return float(coef[1]), float(coef[0]), r2


def ols_loglog(x, y):
    lx, ly = np.log(np.asarray(x, float)), np.log(np.abs(np.asarray(y)))
    b, q = np.polyfit(lx, ly, 1)
    pred = b * lx + q
    r2 = 1.0 - float(((ly - pred) ** 2).sum()) \
        / max(float(((ly - ly.mean()) ** 2).sum()), 1e-300)
    return float(b), float(math.exp(q)), r2


def moebius_g(r):
    """g(r) = (r - 2)/(r + 1/2): boundary spinor slope 2 -> 0, its
    orthogonal (the null-ray slope) -1/2 -> infinity."""
    return (r - 2.0) / (r + 0.5)


def spinor_coords(Ah):
    """Projective spinor coordinates of one 2x2 symmetric block."""
    w, V = np.linalg.eigh(Ah)                   # w[0] <= w[1]
    lam, tau = float(w[1]), float(w[0])
    v = V[:, 1].copy()
    if v[0] < 0:
        v = -v
    r = float(v[1] / v[0])
    t = float(Ah[0, 0] + Ah[1, 1])
    x = float(Ah[0, 0] - Ah[1, 1])
    y = float(2.0 * Ah[0, 1])
    Q = t * t - x * x - y * y
    dnull = Q / (t * t + x * x + y * y)
    return dict(lam=lam, tau=tau, r=r, rho=-1.0 / r if r != 0 else
                float("inf"), t=t, x=x, y=y, Q=Q, dnull=dnull)


def run():
    global N_CHK, FAILS
    N_CHK = 0
    FAILS = []
    print("=" * 78)
    print("PRIME.LORENTZ.SPINOR.01 -- null-cone coordinates for the "
          "near-collinearity (lorentz_spinor_coords_probe)")
    print("=" * 78)

    # ============================================================== S0
    print("\nS0 -- firewall")
    check("S0.AST no zeta-zero loader in this module (zetazero/nzeros/"
          "find_zeros absent); zeros are NOT an input of this probe",
          ast_zero_firewall(__file__))

    # ============================================================== E1
    print("\nE1 -- THE NEW EXACT OBSERVATIONS [E neu] (sympy, exact)")
    t_, x_, y_, i_, j_ = sp.symbols("t x y i j", real=True)
    a_, b_, c_ = sp.symbols("a b c", real=True)
    Msym = sp.Matrix([[t_ + x_, y_], [y_, t_ - x_]])
    detM = sp.simplify(Msym.det() - (t_**2 - x_**2 - y_**2))
    q4id = sp.simplify((a_ + c_)**2 - (a_ - c_)**2 - (2 * b_)**2
                       - 4 * (a_ * c_ - b_**2))
    check("E1.1 [E neu] det M(t,x,y) = t^2 - x^2 - y^2 IDENTICALLY for "
          "M = [[t+x, y],[y, t-x]] (residual %s), and inversely "
          "Q(L(A)) = (a+c)^2 - (a-c)^2 - (2b)^2 = 4 det A IDENTICALLY "
          "(residual %s) -- the T170-TH4 signature-(1,2) form IS the "
          "determinant in these coordinates" % (detM, q4id),
          detM == 0 and q4id == 0)

    M534 = Msym.subs({t_: 5, x_: -3, y_: 4})
    spin = sp.Matrix([1, 2])
    dev = sp.simplify(M534 - 2 * spin * spin.T)
    check("E1.2 [E neu] M(5,-3,4) = [[2,4],[4,8]] = 2 (1,2)^T (1,2) "
          "EXACTLY: rank one (det = %s), trace 10 -- the boundary null "
          "vector is a RANK-ONE SPINOR SQUARE with spinor (1,2)"
          % sp.simplify(M534.det()),
          dev == sp.zeros(2, 2) and sp.simplify(M534.det()) == 0
          and M534[0, 0] == 2 and M534[0, 1] == 4 and M534[1, 1] == 8)

    Eu = (i_**2 + j_**2, -(i_**2 - j_**2), -2 * i_ * j_)
    Eu_null = sp.simplify(Eu[0]**2 - Eu[1]**2 - Eu[2]**2)
    Eu21 = tuple(e.subs({i_: 2, j_: -1}) for e in Eu)
    check("E1.3 [E neu] the Euclid parametrization (i,j) |-> (i^2+j^2, "
          "-(i^2-j^2), -2ij) is null IDENTICALLY (residual %s) and "
          "sends the measured locking direction (2,-1) to %s = (5,-3,4) "
          "EXACTLY" % (Eu_null, Eu21),
          Eu_null == 0 and Eu21 == (5, -3, 4))

    MEu = Msym.subs({t_: Eu[0], x_: Eu[1], y_: Eu[2]})
    spin_ij = sp.Matrix([j_, -i_])
    dev_ij = sp.simplify(MEu - 2 * spin_ij * spin_ij.T)
    s21 = spin_ij.subs({i_: 2, j_: -1})           # (-1, -2) ~ (1, 2)
    ortho = 2 * 1 + (-1) * 2                      # (2,-1) . (1,2)
    check("E1.4 [E neu] the SPINOR-SQUARE IDENTITY: M(Eu(i,j)) = "
          "2 (j,-i)^T (j,-i) for ALL (i,j) (residual %s); at (2,-1) the "
          "spinor is %s ~ (1,2) -- the locking direction IS the spinor "
          "square root of the compiler vector, and (2,-1) . (1,2) = %d "
          "(the null ray is EXACTLY orthogonal to the spinor)"
          % (dev_ij, tuple(s21), ortho),
          dev_ij == sp.zeros(2, 2) and tuple(s21) == (-1, -2)
          and ortho == 0)

    X12 = sp.Matrix([[1, 2], [2, 4]])
    Lmap = (X12[0, 0] + X12[1, 1], X12[0, 0] - X12[1, 1], 2 * X12[0, 1])
    LM = tuple(sp.simplify(e) for e in
               (Msym[0, 0] + Msym[1, 1], Msym[0, 0] - Msym[1, 1],
                2 * Msym[0, 1]))
    anchor = (int(tc.g_car), -int(tc.N_fam), ABS_MU4)
    check("E1.5 [E, corpus anchor] conventions agree: the v576 C3.1 "
          "Lorentz map L(X) = (X11+X22, X11-X22, 2 X12) gives "
          "L([[1,2],[2,4]]) = %s and L(M(t,x,y)) = %s = 2 (t,x,y); the "
          "compiler triple (g_car, -N_fam, |mu4|) = %s = (5,-3,4) with "
          "g_car, N_fam from tfpt_constants (5^2 - 3^2 - 4^2 = 0)"
          % (Lmap, LM, anchor),
          Lmap == (5, -3, 4) and LM == (2 * t_, 2 * x_, 2 * y_)
          and anchor == (5, -3, 4)
          and 5 ** 2 - 3 ** 2 - 4 ** 2 == 0)

    M543 = Msym.subs({t_: 5, x_: -4, y_: 3})
    w543, V543 = np.linalg.eigh(np.array(M543.tolist(), float))
    v543 = V543[:, 1] / V543[0, 1]
    check("E1.6 [must-break, wrong null vector] (5,-4,3) is also null "
          "(M(5,-4,3) = [[1,3],[3,9]], det = %s) BUT its spinor is "
          "(1, %.0f) != (1,2): the Euclid preimage is (3,-1), NOT the "
          "measured locking direction (2,-1), and its second entry 4 "
          "!= N_fam = %d -- the spinor-square anchoring BREAKS for the "
          "permuted triple exactly as it must"
          % (sp.simplify(M543.det()), v543[1], int(tc.N_fam)),
          sp.simplify(M543.det()) == 0 and abs(v543[1] - 3.0) < 1e-12
          and int(tc.N_fam) == 3)

    # ============================================================== L2
    print("\nL2 -- the ladder extraction (deployed frame-A windows, "
          "v563 read-only)")
    zones = core.frame_a_zones()
    rows, anom, incomplete = [], [], []
    q4_worst = eig_worst = 0.0
    for kz in zones:
        rr = core.build_window(kz)
        Ah = rr["Ah"]
        sc = spinor_coords(Ah)
        # exact identity Q(u) = 4 det Ahat (symbolic, E1.1); float dev
        # measured against the conditioning bar of the cancellation
        q4dev = abs(sc["Q"] - 4.0 * rr["det"]) \
            / max(abs(4.0 * rr["det"]), 1e-300)
        q4bar = Q4_COND_FAC * np.finfo(float).eps \
            * (sc["t"]**2 + sc["x"]**2 + sc["y"]**2) \
            / max(abs(4.0 * rr["det"]), 1e-300)
        q4 = q4dev / max(q4bar, 1e-300)
        # eigen-reconstruction residual
        v1 = np.array([1.0, sc["r"]])
        v1 /= np.linalg.norm(v1)
        v2 = np.array([-v1[1], v1[0]])
        rec = sc["lam"] * np.outer(v1, v1) + sc["tau"] * np.outer(v2, v2)
        er = float(np.max(np.abs(rec - Ah))) / max(
            float(np.max(np.abs(Ah))), 1e-300)
        complete = math.exp(2.0 * rr["alpha"]) <= core.ATOM_MAX + 0.5
        row = dict(kz=kz, h=rr["h"], alpha=rr["alpha"],
                   a11=rr["a11"], a22=rr["a22"], a12=rr["a12"],
                   det=rr["det"], onem=rr["onem"], complete=complete,
                   dir_raw=rr["a12"] / rr["a11"], **sc)
        if rr["h"] == ANOMALOUS_H:
            anom.append(row)
            continue
        if not complete:
            incomplete.append(row)
            continue
        q4_worst = max(q4_worst, q4)
        eig_worst = max(eig_worst, er)
        rows.append(row)
    rows.sort(key=lambda w: w["h"])
    check("L2.SET the deployed ladder: %d regular complete windows "
          "(h = %d..%d), %d anomalous (h = %d, v586 declaration), %d "
          "incomplete-comb (excluded from trends, listed)"
          % (len(rows), rows[0]["h"], rows[-1]["h"], len(anom),
             ANOMALOUS_H, len(incomplete)),
          len(rows) >= 30)
    check("L2.Q4D the Lorentz norm IS the margin: Q(u) = t^2-x^2-y^2 = "
          "4 det Ahat per rung (symbolic identity E1.1; float dev "
          "within %.3f of the conditioning bar %d eps ||u||^2/|4 det| "
          "on every rung -- cancellation-limited, as declared)"
          % (q4_worst, int(Q4_COND_FAC)), q4_worst <= 1.0)
    check("L2.EIG the projective reparametrization Ahat = lambda "
          "P_(1,r) + tau P_perp is exact per rung (worst eigen-"
          "reconstruction residual %.1e <= %.0e)"
          % (eig_worst, BAR_EIG), eig_worst <= BAR_EIG)

    print("\n    per-rung table (regular complete ladder):")
    print("    %5s %7s | %10s %10s %8s %8s | %10s %10s | %10s %8s"
          % ("h", "alpha", "lambda", "tau", "r", "rho", "dnull",
             "onem", "det", "q_k"))
    rs = [w["r"] for w in rows]
    gs = [moebius_g(r) for r in rs]
    qs = [gs[k + 1] / gs[k] for k in range(len(gs) - 1)]
    for k, w in enumerate(rows):
        print("    %5d %7.3f | %10.3e %10.3e %8.4f %8.4f | %10.3e "
              "%10.3e | %10.3e %8s"
              % (w["h"], w["alpha"], w["lam"], w["tau"], w["r"],
                 w["rho"], w["dnull"], w["onem"], w["det"],
                 ("%8.4f" % qs[k]) if k < len(qs) else "--"))
    for w in anom + incomplete:
        print("    %5d %7.3f | %10.3e %10.3e %8.4f %8.4f | %10.3e "
              "%10.3e | %10.3e %8s   <-- %s"
              % (w["h"], w["alpha"], w["lam"], w["tau"], w["r"],
                 w["rho"], w["dnull"], w["onem"], w["det"], "--",
                 "ANOMALOUS (excluded)" if w["h"] == ANOMALOUS_H
                 else "incomplete comb (excluded)"))

    # corpus anchoring of the extracted coordinates
    dir_dev = max(abs(w["dir_raw"] - w["r"]) for w in rows)
    ang = [math.degrees(math.acos(min(1.0, abs(
        (np.array([1.0, w["rho"]]) / np.linalg.norm([1.0, w["rho"]]))
        @ (np.array([2.0, -1.0]) / math.sqrt(5.0)))))) for w in rows]
    check("L2.ANCH corpus anchoring: near rank-one the raw direction "
          "a12/a11 equals the spinor slope r (max dev %.2e); the null "
          "slope rho = -1/r sits %.1f..%.1f deg from the exact (2,-1) "
          "ray (median %.1f; v577 measured 23.5..33.8 on its surface) "
          "-- same objects, same regime"
          % (dir_dev, min(ang), max(ang), float(np.median(ang))),
          dir_dev < 0.05)

    # ============================================================== L3
    print("\nL3 -- frozen oscillation-aware trend statistics")
    hs = [w["h"] for w in rows]
    dr = np.diff(rs)
    nz = dr[dr != 0.0]
    mon_frac = max(float((nz > 0).mean()), float((nz < 0).mean())) \
        if len(nz) else 0.0
    ktau = kendall_tau(hs, rs)
    half = len(rs) // 2
    rng_full = max(rs) - min(rs)
    rng_half = max(rs[half:]) - min(rs[half:])
    cauchy = rng_half / max(rng_full, 1e-300)
    # Aitken Delta^2 limit census (descriptive)
    aik = []
    for k in range(len(rs) - 2):
        d1, d2 = rs[k + 1] - rs[k], rs[k + 2] - rs[k + 1]
        den = d2 - d1
        if abs(den) > 1e-12:
            aik.append(rs[k + 2] - d2 * d2 / den)
    aik = np.array(aik)
    r_inf, r_b, r_r2 = fit_invlog(hs, rs)
    rhos = [w["rho"] for w in rows]
    rho_inf, rho_b, rho_r2 = fit_invlog(hs, rhos)
    print("    r: min %.4f max %.4f; increments: %d up / %d down; "
          "Aitken limit census median %.3f (IQR %.3f..%.3f, %d pts)"
          % (min(rs), max(rs), int((nz > 0).sum()), int((nz < 0).sum()),
             float(np.median(aik)), float(np.percentile(aik, 25)),
             float(np.percentile(aik, 75)), len(aik)))
    print("    1/log h fits: r_inf = %.3f (b = %.2f, R^2 = %.3f); "
          "rho_inf = %.3f (b = %.2f, R^2 = %.3f)  [v586 quote: -0.551]"
          % (r_inf, r_b, r_r2, rho_inf, rho_b, rho_r2))
    mono_ok = mon_frac >= MON_BAR and abs(ktau) >= KEN_BAR
    cauchy_ok = cauchy <= CAUCHY_BAR
    fit_ok = (rho_r2 >= FIT_R2 and abs(rho_inf + 0.5) <= RHO_TOL) \
        or (r_r2 >= FIT_R2 and abs(r_inf - 2.0) <= R_TOL)
    check("L3.MON (a) MONOTONE: the spinor slope r moves with majority-"
          "sign fraction %.3f (bar %.2f) and Kendall tau %.3f vs h "
          "(bar %.2f) across %d rungs -- %s"
          % (mon_frac, MON_BAR, ktau, KEN_BAR, len(rs),
             "a 1D monotone projective quantity" if mono_ok
             else "NOT monotone at the declared bars"), mono_ok)
    check("L3.CAUCHY (a) CAUCHY/settling: the second-half range of r "
          "is %.3f of the full range (bar <= %.2f); Aitken census "
          "median %.3f" % (cauchy, CAUCHY_BAR, float(np.median(aik))),
          cauchy_ok)
    check("L3.FIT (a) the 1/log h extrapolation lands on the spinor "
          "axis: rho_inf = %.3f vs -1/2 (tol %.2f, R^2 %.3f) / r_inf "
          "= %.3f vs 2 (tol %.2f, R^2 %.3f) -- v586's drift law seen "
          "in the block's OWN eigencoordinates"
          % (rho_inf, RHO_TOL, rho_r2, r_inf, R_TOL, r_r2), fit_ok)

    # comparator: the raw matrix margins (the non-uniform side)
    e_onem, _, r2_onem = ols_loglog(hs, [w["onem"] for w in rows])
    e_det, _, r2_det = ols_loglog(hs, [abs(w["det"]) for w in rows])
    e_dn, _, r2_dn = ols_loglog(hs, [abs(w["dnull"]) for w in rows])
    onems = [w["onem"] for w in rows]
    check("L3.RAW the raw-margin comparator: onem ~ h^%.2f (R^2 %.2f, "
          "max/min = %.1e -- NO uniform floor), det ~ h^%.2f (R^2 "
          "%.2f); the null-cone distance dnull ~ h^%.2f is the SAME "
          "vanishing object (Q = 4 det) -- while r stays in the "
          "bounded interval [%.3f, %.3f]: the coordinate change "
          "separates the bounded projective coordinate from the "
          "vanishing radial one"
          % (e_onem, r2_onem, max(onems) / min(onems), e_det, r2_det,
             e_dn, min(rs), max(rs)), r2_onem > 0.5)

    # (b) the transversal reserve
    taus = [w["tau"] for w in rows]
    tau_pos = all(tt > 0.0 for tt in taus)
    e_tau, _, r2_tau = ols_loglog(hs, taus)
    e_rat, _, r2_rat = ols_loglog(hs, [w["tau"] / w["lam"] for w in rows])
    check("L3.TAU (b) the transversal energy tau = lambda_min is "
          "POSITIVE on all %d regular rungs (min %.3e) -- the reserve "
          "exists pointwise; honest decay class: tau ~ h^%.2f (R^2 "
          "%.2f), tau/lambda ~ h^%.2f (R^2 %.2f) -- %s"
          % (len(rows), min(taus), e_tau, r2_tau, e_rat, r2_rat,
             "NO uniform positive floor (the reserve vanishes along "
             "the ladder; positivity per rung only)" if e_tau < -0.5
             else "bounded"), tau_pos)

    # (c) the cross-ratio chain
    qs_arr = np.array(qs)
    contr_frac = float((qs_arr < 1.0).mean())
    cv_q = float(np.std(qs_arr) / abs(np.mean(qs_arr)))
    tot_contr = float(np.prod(qs_arr))
    cr_ok = contr_frac >= CR_FRAC
    check("L3.CR (c) the anchored cross-ratio chain q_k = CR(r_k, "
          "r_{k+1}; 2, -1/2): strict contraction q_k < 1 on %.3f of "
          "%d rungs (bar %.2f), median %.4f, CV %.3f, total "
          "contraction prod q = %.3f -- %s"
          % (contr_frac, len(qs), CR_FRAC, float(np.median(qs_arr)),
             cv_q, tot_contr,
             "a stable per-rung projective contraction law" if cr_ok
             else "no stable contraction law"), cr_ok)

    # ============================================================== L3b
    print("\nL3b -- the revealed structure, described exactly "
          "(POST-FIRST-RUN description of the REVEAL enum, declared "
          "in the header; same bars, ladder re-parametrized by alpha)")
    arows = sorted(rows, key=lambda w: w["alpha"])
    aas = [w["alpha"] for w in arows]
    ras = [w["r"] for w in arows]
    dra = np.diff(ras)
    nza = dra[dra != 0.0]
    mon_a = max(float((nza > 0).mean()), float((nza < 0).mean())) \
        if len(nza) else 0.0
    n_strict = int((dra > 0).sum())
    ktau_a = kendall_tau(aas, ras)
    halfa = len(ras) // 2
    cauchy_a = (max(ras[halfa:]) - min(ras[halfa:])) \
        / max(max(ras) - min(ras), 1e-300)
    ga = moebius_g(np.array(ras))
    qa = ga[1:] / ga[:-1]
    contr_a = float((qa < 1.0).mean())
    cv_qa = float(np.std(qa) / abs(np.mean(qa)))
    # fits in alpha: r = r_inf + b/alpha; power law 2 - r ~ alpha^s;
    # onem log-linear in alpha
    Aa = np.column_stack([1.0 / np.asarray(aas), np.ones(len(aas))])
    coefa, *_ = np.linalg.lstsq(Aa, np.asarray(ras), rcond=None)
    resa = np.asarray(ras) - Aa @ coefa
    r2_inva = 1.0 - float((resa ** 2).sum()) \
        / float(((np.asarray(ras) - np.mean(ras)) ** 2).sum())
    r_inf_a, b_a = float(coefa[1]), float(coefa[0])
    s_pow, c_pow, r2_pow = ols_loglog(aas, [2.0 - r for r in ras])
    lo_fit = np.polyfit(aas, np.log([w["onem"] for w in arows]), 1)
    lo_pred = np.polyval(lo_fit, aas)
    lo_y = np.log([w["onem"] for w in arows])
    r2_lo = 1.0 - float(((lo_y - lo_pred) ** 2).sum()) \
        / float(((lo_y - lo_y.mean()) ** 2).sum())
    check("L3b.MON [MEASURED, the revealed 1D structure] in the "
          "alpha-ordered ladder the spinor slope r is monotone: "
          "%d/%d increments strictly positive (majority fraction "
          "%.3f, bar %.2f), Kendall tau %.3f vs alpha (bar %.2f) -- "
          "the h-order oscillation of L3.MON is the alpha-vs-h jitter "
          "of the frame-A scan, NOT noise in r"
          % (n_strict, len(dra), mon_a, MON_BAR, ktau_a, KEN_BAR),
          mon_a >= MON_BAR and abs(ktau_a) >= KEN_BAR)
    check("L3b.CR [MEASURED] the anchored cross-ratio chain in alpha "
          "order contracts on %.3f of %d rungs (bar %.2f; median q "
          "%.4f, CV %.3f): the per-rung projective contraction law "
          "the h-order chain missed"
          % (contr_a, len(qa), CR_FRAC, float(np.median(qa)), cv_qa),
          contr_a >= CR_FRAC)
    print("    Cauchy (alpha order): second-half range / full range = "
          "%.3f (h-order was %.3f; the settling is toward the LARGE-"
          "alpha end, approach still slow)" % (cauchy_a, cauchy))
    print("    fits in alpha: r = %.3f %+.3f/alpha (R^2 %.3f); "
          "2 - r ~ %.3f alpha^%.3f (R^2 %.3f); onem ~ %.2e "
          "exp(%.3f alpha) (R^2 %.3f)"
          % (r_inf_a, b_a, r2_inva, c_pow, s_pow, r2_pow,
             math.exp(lo_fit[1]), lo_fit[0], r2_lo))
    print("    HONESTY: the approach 2 - r is GLACIAL (power ~ "
          "alpha^%.2f; the 1/alpha extrapolant %.3f does NOT reach 2 "
          "on this surface) -- the monotone 1D structure exists, the "
          "rate question stays open exactly as the corpus states"
          % (s_pow, r_inf_a))

    # ============================================================== L4
    print("\nL4 -- controls")
    # C1: scramble destroys the rank-one dominance
    kz_mid = rows[len(rows) // 2]["kz"]
    scr_fac, scr_rat = [], []
    w_real = next(w for w in rows if w["kz"] == kz_mid)
    for sd in SCR_SEEDS:
        rr_s = core.build_window(kz_mid, scramble_seed=sd)
        sc_s = spinor_coords(rr_s["Ah"])
        scr_fac.append(abs(rr_s["onem"]) / abs(w_real["onem"]))
        scr_rat.append(abs(sc_s["tau"] / sc_s["lam"])
                       / abs(w_real["tau"] / w_real["lam"]))
    check("L4.C1 [must-break] the position scramble destroys the "
          "rank-one dominance at h = %d: |onem| moves by x%.1f..x%.1f "
          "(bar >= %.0f) and the eccentricity tau/lambda by "
          "x%.1f..x%.1f -- the near-collinearity is REAL placement "
          "content, not a coordinate artifact"
          % (w_real["h"], min(scr_fac), max(scr_fac), BAR_SCR,
             min(scr_rat), max(scr_rat)), min(scr_fac) >= BAR_SCR)
    # C2: the wrong null vector fails the ladder anchoring too
    d2 = abs(float(np.median(aik)) - 2.0)
    d3 = abs(float(np.median(aik)) - 3.0)
    check("L4.C2 [must-break] wrong null vector (5,-4,3): its spinor "
          "slope is 3 (E1.6); the measured ladder extrapolant (Aitken "
          "median %.3f, 1/log h r_inf %.3f) is closer to the TRUE "
          "spinor slope 2 than to 3 (|.-2| = %.3f < |.-3| = %.3f and "
          "|r_inf-2| = %.3f < |r_inf-3| = %.3f)"
          % (float(np.median(aik)), r_inf, d2, d3,
             abs(r_inf - 2.0), abs(r_inf - 3.0)),
          d2 < d3 and abs(r_inf - 2.0) < abs(r_inf - 3.0))
    # C3: random slopes show no cross-ratio law / no monotonicity
    rng = np.random.default_rng(SEED_RAND)
    mon_rand, contr_rand = [], []
    for _ in range(N_RAND):
        rr_seq = rng.uniform(min(rs), max(rs), size=len(rs))
        d = np.diff(rr_seq)
        d = d[d != 0.0]
        mon_rand.append(max(float((d > 0).mean()),
                            float((d < 0).mean())) if len(d) else 0.0)
        gg = moebius_g(rr_seq)
        qq = gg[1:] / gg[:-1]
        contr_rand.append(float((qq < 1.0).mean()))
    mon_p = float(np.percentile(mon_rand, RAND_PCT))
    con_p = float(np.percentile(contr_rand, RAND_PCT))
    check("L4.C3 [must-break] random slopes (N = %d, frozen seed %d, "
          "same range/length): monotone fraction %dth pct = %.3f and "
          "contraction fraction %dth pct = %.3f -- the real h-order "
          "ladder (%.3f / %.3f) exceeds both, and the alpha-order "
          "ladder (%.3f / %.3f) exceeds them massively: the observed "
          "law is not a property of arbitrary slope sequences"
          % (N_RAND, SEED_RAND, RAND_PCT, mon_p, RAND_PCT, con_p,
             mon_frac, contr_frac, mon_a, contr_a),
          mon_frac > mon_p and contr_frac > con_p
          and mon_a > mon_p and contr_a > con_p)

    # ============================================================== L5
    print("\n" + "=" * 78)
    print("L5 -- VERDICT + recommended contract text (chat report is "
          "the deliverable; nothing outside experiments/ is touched)")
    print("=" * 78)
    controls_ok = (min(scr_fac) >= BAR_SCR and d2 < d3
                   and mon_frac > mon_p and contr_frac > con_p)
    improve = (mono_ok and cauchy_ok and fit_ok and tau_pos and cr_ok
               and controls_ok)
    # REVEAL structure (declared): |r - 2| decreasing while r itself
    # non-monotone, or CR chain constant while monotonicity fails
    dabs = np.diff(np.abs(np.array(rs) - 2.0))
    dec_frac = float((dabs[dabs != 0.0] < 0).mean()) if len(dabs) else 0.0
    reveal = (not improve) and (
        (dec_frac >= REVEAL_FRAC and not mono_ok)
        or (cv_q <= CR_CONST_CV and not mono_ok))
    if improve:
        verdict = "LORENTZ-COORDS-IMPROVE"
    elif reveal:
        verdict = "LORENTZ-COORDS-REVEAL"
    else:
        verdict = "LORENTZ-COORDS-NEUTRAL"
    print("""
  VERDICT: %s

  EXACT PART [E neu] (E1, all sympy-exact):
    * M(5,-3,4) = 2 (1,2)^T (1,2) -- the compiler triple
      (g_car, -N_fam, |mu4|) is a rank-one SPINOR SQUARE, spinor (1,2).
    * Euclid (2,-1) |-> (5,-3,4) exactly; M(Eu(i,j)) = 2 (j,-i)^T (j,-i)
      identically: the locking direction IS the spinor square root of
      the compiler vector, orthogonal to the (1,2) spinor.
    * The permuted triple (5,-4,3) is null too but its spinor is (1,3),
      preimage (3,-1) != (2,-1): the anchoring is direction-specific.

  MEASURED PART (L2/L3, %d regular rungs h = %d..%d):
    * monotone fraction %.3f, Kendall tau %.3f, Cauchy %.3f;
      1/log h: rho_inf = %.3f (R^2 %.3f), r_inf = %.3f (R^2 %.3f).
    * reserve: tau > 0 on all rungs (min %.2e), decay class h^%.2f --
      pointwise positive, NOT uniformly bounded below.
    * cross-ratio chain: contraction on %.3f of rungs, median q %.4f,
      CV %.3f, total contraction %.3f.
    * raw comparator: onem ~ h^%.2f, det ~ h^%.2f, dnull ~ h^%.2f
      (all vanishing, no uniform floor); dnull = Q/(t^2+x^2+y^2) with
      Q = 4 det EXACT -- the radial coordinate is the old margin.

  HONESTY: coordinate-change diagnostic only.  The exact null
  direction stands; the approach rate along the ladder remains the
  v586 1/log h drift, which misses the previously declared transport
  bar (v581) -- NO positivity theorem, NO RH claim.
""" % (verdict, len(rows), rows[0]["h"], rows[-1]["h"], mon_frac,
       ktau, cauchy, rho_inf, rho_r2, r_inf, r_r2, min(taus), e_tau,
       contr_frac, float(np.median(qs_arr)), cv_q, tot_contr,
       e_onem, e_det, e_dn))
    if improve or reveal:
        print("""  THE REVEALED STRUCTURE (exact description, L3b): the spinor
  slope r is a MONOTONE FUNCTION OF THE WINDOW WIDTH alpha
  (%d/%d strict increments, Kendall tau %.3f, anchored-CR
  contraction on %.3f of alpha-rungs) -- the h-ordered oscillation
  was the alpha-vs-h jitter of the frame-A scan.  The named 1D
  candidate statement (NOT proven, NOT preregistered -- next
  probe's contract): the dominant-eigenvector slope r(alpha) of the
  lock block Ahat is strictly increasing in alpha with the Moebius
  coordinate g(r) = (r-2)/(r+1/2) contracting per rung (equiv.: the
  null slope rho = -1/r increases toward -1/2 along alpha); the
  measured approach is glacial (2 - r ~ alpha^%.2f) -- the rate,
  i.e. WHETHER the limit is reached, remains the open problem the
  corpus already names."""
              % (n_strict, len(dra), ktau_a, contr_a, s_pow))

    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed%s"
          % (time.time() - T0, N_CHK, len(FAILS),
             ("  " + ",".join(FAILS)) if FAILS else ""))
    return 0 if not FAILS else 1


if __name__ == "__main__":
    raise SystemExit(run())
