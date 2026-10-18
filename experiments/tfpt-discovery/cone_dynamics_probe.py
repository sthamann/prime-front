"""Discovery probe: CONE DYNAMICS -- the review-7.3 question ("use the
Lorentz form DYNAMICALLY instead of statically") executed on the
prime-front determinant coordinates.

SETUP (all conventions verbatim from the corpus):
  y(a) = (S11, S22, S12)(a) are the three rank-3 functionals (Paper II
  thm:rank3 / v563 assembly); det S = (1/2) y^T J_det y with
  J_det = [[0,1,0],[1,0,0],[0,0,-2]] (v624 C1, signature (1,2));
  P = [[3,0,0],[3,0,2],[-1,1,-1]] with P^T J_det P = J_fix exactly
  (v624 C2, index 6); the cover cone and the ONE-SHEET convention are
  v627's: positive cone of J_fix, sheet read off the J-inner product
  with the positive eigendirection v_plus of J_fix.

THREE SLICES (bars and enums declared BEFORE any number):

C1 [TRAJECTORY].  Order the prime powers by u = log n (the natural
   order of the v563 atom table); after EVERY new atom form the
   cumulative assembly y_k = sum_{j<=k} rho_j X_j (rho_j =
   Lambda(n_j)/sqrt(n_j), X_j the per-atom two-point spline read
   triple of v563) and transport z_k = P^{-1} y_k into the cover
   polarization coordinates.  Measured: first cone entry (atom index
   and n), number of exits after entry, final membership, dwell
   fraction; congruence bookkeeping z^T J_fix z = 2 det S_k checked
   per step.  Checkpoints printed.  NOTE: a partial sum after k atoms
   is a literally truncated comb -- the v619 flip mechanism lives on
   this axis, shown not hidden.

C2 [THE SEMIGROUP TEST -- core].  Honesty first: the atom update is
   y -> y + rho_n x_n, a pure TRANSLATION of the 3 coordinates --
   affine with IDENTITY linear part, NOT linear (demonstrated
   numerically: F(2y) != 2 F(y)); as a matrix it acts only in
   homogeneous 4-coordinates [[I_3, t], [0, 1]].  There is therefore
   NO nontrivial 'Lorentz transformation per prime' on the 3
   coordinates; the correct semigroup statement is the ADDITIVE one:
     T_t(C+) subset of C+   <=>   t in closure(C+)
   (the closed forward cone is an additive semigroup).  Both
   directions of this criterion are verified numerically on a
   DECLARED ray lattice of the cone (N_THETA rays x radii x scales),
   including a spacelike MUST-FAIL translation.  The semigroup
   question then reduces to a measurable pointwise statement:
   does EVERY atom increment t_n = rho_n x_n lie in the closed
   forward cone?  Measured per window: membership fraction (count and
   rho^2-weighted), wedge split (forward / backward / spacelike),
   first violator.  WEAKER DECLARED STATEMENT (path cone-
   monotonicity): the v627 sheet functional ell(z) = z^T J_fix v_plus
   (orientation fixed once, on the first window's final point) grows
   along the path; because ell is linear, ell is monotone iff
   ell(t_n) >= 0 for every atom.  Measured: decreasing-step fraction,
   max single drop, max drawdown / final.

C3 [CONTROLS -- must separate, else the probe measures nothing
   arithmetic].  (a) position scramble (v563 scramble_seed: same
   masses, uniform u -- v627 H4 found the STATIC chamber membership
   survives this; whether the DYNAMICS separates is exactly what is
   measured here); (b) Epstein masses rho_E = Lambda_E(n)/sqrt(n)
   from the RH-violating E(s) of x^2 + 5y^2 (no Euler product;
   machinery verbatim from epstein_firewall_probe.py, division
   validated against the sieve before use).  Separation bar
   (declared): a control separates on a window iff its final point is
   OUT of the cone, or its increment-membership fraction is lower by
   >= BAR_SEP, or its decreasing-step fraction is higher by
   >= BAR_SEP, than the true path on the same window.

VERDICT (frozen enums, precedence top-down):
  SEMIGROUP-ALIVE     -- 100% of true increments in the closed cone on
                         ALL windows AND both control families violate
                         membership by >= BAR_SEP somewhere;
  PATH-MONOTONE-ONLY  -- semigroup fails, but ell has ZERO decreasing
                         steps on ALL true windows AND both control
                         families break the monotone / cone reading;
  CONE-DYNAMICS-DEAD  -- anything else, INCLUDING the case that the
                         controls do not separate (the honest
                         'nothing arithmetic measured' outcome).

FIREWALL: experiments-only; verification/ strictly read-only (v563
import); no marker moves; no positivity claim; no RH statement; no
zero of any L-function is read (AST-checked); deterministic.

Provenance: v624 (congruence), v627 (chamber + sheet convention),
v563 (windows, read-only), rank3_functionals_probe.py (vectorised
spline read), epstein_firewall_probe.py (Lambda_E machinery,
verbatim), external review 2026-08-02 sec. 7.3 (the dynamic-cone
question).
"""
import ast
import math
import os
import sys
import time

import numpy as np

# ---------------------------------------------------------------- imports
_here = os.path.dirname(os.path.abspath(__file__))
for _cand in (_here, os.path.join(_here, "..", "..", "verification")):
    if os.path.exists(os.path.join(_cand, "v563_paper2_readouts.py")):
        sys.path.insert(0, os.path.abspath(_cand))
        break

import v563_paper2_readouts as core  # noqa: E402  (READ-ONLY import)
import sympy as sp  # noqa: E402

T0 = time.time()
FAILS = []
N_CHK = 0

# ------------------------------------------------- declared bars / constants
X_CAP = 100000        # Epstein horizon (epstein_firewall_probe N_CAP, verbatim)
TOL_CONG = 1.0e-9     # transport identity z^T J_fix z = 2 det S, relative
TOL_WIRE = 1.0e-10    # cumulative endpoint vs the v563 S matrix, relative
TOL_RAY = 1.0e-9      # ray-lattice membership tolerance, relative
FLOAT_FLOOR = 1.0e-12  # 'zero' floor for increment membership / mono steps
BAR_SEP = 0.05        # control separation margin on fractions
N_THETA = 16          # ray lattice: angles
RAY_R = (0.0, 0.5, 0.999)      # ray lattice: radial positions (1 = boundary)
RAY_SCALE = (1.0e-3, 1.0, 1.0e3)  # ray lattice: scalings (apex proximity)
SCR_SEEDS = (1, 2, 3)  # v627 H4 scramble seeds, verbatim
TOL_DIV = 1.0e-8      # Epstein division machinery vs the sieve
LAM_TOL = 1.0e-9      # Lambda_E support threshold (epstein probe, verbatim)


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
    for node in ast.walk(tree):
        if isinstance(node, ast.Attribute) and node.attr in (
                "zetazero", "nzeros", "second_sheet_zero"):
            return False
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) \
                and node.func.id in ("zetazero", "nzeros"):
            return False
    return True


# ------------------------------------------------- exact congruence (v624)
Jdet_sp = sp.Matrix([[0, 1, 0], [1, 0, 0], [0, 0, -2]])
Jfix_sp = sp.Matrix([[16, 2, 4], [2, -2, 2], [4, 2, -2]])
P_sp = sp.Matrix([[3, 0, 0], [3, 0, 2], [-1, 1, -1]])
PinvN = np.array(P_sp.inv().evalf(20).tolist(), dtype=float)
JfixN = np.array(Jfix_sp.tolist(), dtype=float)


def q_of_y(Y):
    """2 det S = y^T J_det y for row-stacked y = (S11, S22, S12)."""
    Y = np.atleast_2d(Y)
    return 2.0 * (Y[:, 0] * Y[:, 1] - Y[:, 2] ** 2)


# ------------------------------------------------- spline read (rank3 probe)
def spline_read_vec(W, u, D):
    """Vectorised two-point read (prop:split), rank3_functionals_probe
    verbatim; reflection branch asserted dead (u_min > D everywhere)."""
    Mz = len(W)
    q = np.asarray(u, dtype=float) / D
    i0 = np.floor(q).astype(np.int64)
    f = q - i0
    v = np.zeros_like(q)
    ok0 = (i0 >= 0) & (i0 < Mz)
    v[ok0] = (1.0 - f[ok0]) * W[i0[ok0]]
    ok1 = (i0 + 1 >= 0) & (i0 + 1 < Mz)
    v[ok1] += f[ok1] * W[i0[ok1] + 1]
    return v


# ------------------------------------------------- Epstein machinery
# (epstein_firewall_probe.py, verbatim -- the negative-control arithmetic)
def lattice_r1(N):
    """r_{Q1}(n), Q1 = x^2 + 5y^2, exact count over Z^2."""
    r = np.zeros(N + 1, dtype=np.int64)
    for x in range(0, int(math.isqrt(N)) + 1):
        x2 = x * x
        wx = 2 if x > 0 else 1
        ymax = int(math.isqrt((N - x2) // 5)) if x2 <= N else -1
        for y in range(0, ymax + 1):
            n = x2 + 5 * y * y
            if n == 0 or n > N:
                continue
            r[n] += wx * (2 if y > 0 else 1)
    return r


def dirichlet_vonmangoldt(a, N):
    """Coefficients Lambda_F(n) of -F'/F for F = sum a_n n^{-s}, a_1 = 1."""
    lam = np.zeros(N + 1)
    S = np.zeros(N + 1)
    logs = np.zeros(N + 1)
    logs[1:] = np.log(np.arange(1, N + 1, dtype=float))
    af = a.astype(float)
    for n in range(2, N + 1):
        lam[n] = af[n] * logs[n] - S[n]
        k = N // n
        if k >= 2:
            S[2 * n::n] += lam[n] * af[2:k + 1]
    return lam


# ------------------------------------------------- path statistics
def path_stats(label, uu, rho, Xn, Jfvp, ell_scale):
    """Cumulative cone trajectory + increment / monotonicity statistics.

    Increments in z-coordinates are t_z = P^{-1} (rho_n x_n); because
    ell is LINEAR, the ell-step of atom n equals ell(t_z) exactly.
    """
    T_y = rho[:, None] * Xn                       # increments, y-coords
    T_z = T_y @ PinvN.T                           # increments, z-coords
    Y = np.cumsum(T_y, axis=0)
    Z = np.cumsum(T_z, axis=0)
    K = len(rho)
    q = q_of_y(Y)                                 # 2 det S_k (exact intent)
    q_z = np.einsum("ki,ij,kj->k", Z, JfixN, Z)   # transported form
    cong = float(np.max(np.abs(q_z - q) / np.maximum(1.0, np.abs(q))))
    ell = Z @ Jfvp
    in_cone = (q > 0.0) & (ell > 0.0)
    # increments
    q_t = q_of_y(T_y)
    ell_t = T_z @ Jfvp
    nt = np.linalg.norm(T_z, axis=1)
    tol_q = FLOAT_FLOOR * np.maximum(1e-300, nt ** 2) * float(
        np.linalg.norm(JfixN))
    tol_l = FLOAT_FLOOR * np.maximum(1e-300, nt) * ell_scale
    inc_fwd = (q_t >= -tol_q) & (ell_t >= -tol_l)
    inc_bwd = (q_t >= -tol_q) & (ell_t < -tol_l)
    inc_spc = q_t < -tol_q
    w2 = rho ** 2
    frac_in = float(np.mean(inc_fwd))
    frac_in_w = float(np.sum(w2[inc_fwd]) / np.sum(w2))
    first_bad = int(np.argmin(inc_fwd)) if not inc_fwd.all() else -1
    # ell monotonicity (exact: step = ell_t)
    decr = ell_t < -tol_l
    n_decr = int(np.sum(decr))
    max_drop = float(-np.min(ell_t)) if n_decr else 0.0
    runmax = np.maximum.accumulate(ell)
    drawdown = float(np.max(runmax - ell))
    dq = np.diff(np.concatenate([[0.0], q]))
    n_decr_q = int(np.sum(dq < 0.0))
    # entry / exits
    if in_cone.any():
        k_in = int(np.argmax(in_cone))
        exits = int(np.sum(in_cone[:-1] & ~in_cone[1:]))
        last_out = int(np.where(~in_cone)[0][-1]) if not in_cone.all() \
            else -1
    else:
        k_in, exits, last_out = -1, 0, K - 1
    st = dict(label=label, K=K, cong=cong, q=q, ell=ell, in_cone=in_cone,
              frac_in=frac_in, frac_in_w=frac_in_w, first_bad=first_bad,
              inc_fwd=inc_fwd, frac_bwd=float(np.mean(inc_bwd)),
              frac_spc=float(np.mean(inc_spc)),
              n_decr=n_decr, frac_decr=n_decr / K, max_drop=max_drop,
              drawdown=drawdown, n_decr_q=n_decr_q,
              k_in=k_in, exits=exits, last_out=last_out,
              final_in=bool(in_cone[-1]),
              dwell=float(np.mean(in_cone)),
              Y_end=Y[-1], T_z=T_z, q_t=q_t, ell_t=ell_t, uu=uu)
    return st


def print_path(st, nn=None):
    K = st["K"]
    nrep = (lambda k: "n=%d" % nn[k]) if nn is not None else \
        (lambda k: "u=%.3f" % st["uu"][k])
    print("    %-22s K=%5d  entry k=%s%s  exits-after-entry=%d "
          "(last out k=%s)  final-in-cone=%s  dwell=%.4f"
          % (st["label"], K,
             st["k_in"], " (%s)" % nrep(st["k_in"]) if st["k_in"] >= 0
             else "", st["exits"],
             st["last_out"] if st["last_out"] >= 0 else "-",
             st["final_in"], st["dwell"]))
    fb = st["first_bad"]
    print("      increments: forward-cone %.4f (rho^2-weighted %.4f), "
          "backward %.4f, spacelike %.4f; first violator %s"
          % (st["frac_in"], st["frac_in_w"], st["frac_bwd"],
             st["frac_spc"],
             ("k=%d (%s), q_t=%+.3e, ell_t=%+.3e"
              % (fb, nrep(fb), st["q_t"][fb], st["ell_t"][fb]))
             if fb >= 0 else "NONE"))
    print("      ell steps: decreasing %d/%d (%.4f), max single drop "
          "%.4e, max drawdown %.4e (final ell %.4f); q steps "
          "decreasing %d" % (st["n_decr"], K, st["frac_decr"],
                             st["max_drop"], st["drawdown"],
                             st["ell"][-1], st["n_decr_q"]))
    ks = sorted({0, 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048,
                 4096, 8192, K - 1} & set(range(K)))
    print("      checkpoints:  k | %s | 2detS_k | ell_k | in-cone"
          % ("n" if nn is not None else "u"))
    for k in ks:
        print("        %6d | %9s | %+12.5e | %+12.5e | %s"
              % (k, (str(int(nn[k])) if nn is not None
                     else "%.3f" % st["uu"][k]),
                 st["q"][k], st["ell"][k],
                 "IN" if st["in_cone"][k] else "out"))


def run():
    global N_CHK, FAILS
    N_CHK = 0
    FAILS = []
    print("=" * 78)
    print("CONE DYNAMICS -- the Lorentz form used dynamically "
          "(cone_dynamics_probe)")
    print("=" * 78)

    # ============================================================== S0
    print("\nS0 -- firewall, exact congruence, ray-lattice semigroup lemma")
    check("S0.AST no zeta-zero loader in this module",
          ast_zero_firewall(os.path.abspath(__file__)))
    cong_exact = sp.simplify(P_sp.T * Jdet_sp * P_sp - Jfix_sp) \
        == sp.zeros(3, 3)
    check("S0.CONG P^T J_det P = J_fix EXACT (sympy), det P = %s, "
          "det J_fix = %s (v624 C2 reproduced)"
          % (P_sp.det(), Jfix_sp.det()),
          cong_exact and P_sp.det() == -6 and Jfix_sp.det() == 72)
    P_wrong = sp.Matrix(P_sp)
    P_wrong[0, 0] = 4
    res_mut = sp.Matrix(P_wrong.T * Jdet_sp * P_wrong - Jfix_sp)
    check("S0.MUT [must-fail control] a mutated transport (P[0,0]=4) "
          "BREAKS the congruence (max |residual entry| = %s != 0)"
          % max(abs(x) for x in res_mut),
          max(abs(x) for x in res_mut) > 0)

    # eigen-split of J_fix and the (orientation-pending) sheet direction
    w_, V_ = np.linalg.eigh(JfixN)
    lam1, lam2, lamp = float(w_[0]), float(w_[1]), float(w_[2])
    v1, v2, vp = V_[:, 0].copy(), V_[:, 1].copy(), V_[:, 2].copy()
    check("S0.SIG J_fix eigenvalues (%.4f, %.4f, %.4f): signature (1,2)"
          % (lam1, lam2, lamp), lam1 < 0 < lamp and lam2 < 0)

    # ============================================================== windows
    print("\nC1 -- cumulative determinant trajectories (declared windows: "
          "first / v563 reference h=540 / last of the complete-comb "
          "frame-A windows with X = e^{2a} <= %d)" % X_CAP)
    KZ = core.frame_a_zones()
    elig = []
    for kz in KZ:
        n_zone = int(round(math.exp(float(core.U_ALL[kz]))))
        if n_zone * n_zone <= X_CAP:
            elig.append((kz, n_zone))
    kz_ref = next(kz for kz, nz in elig if nz == 157)
    picks = [elig[0][0], kz_ref, elig[-1][0]]
    wins = [core.build_window(kz) for kz in picks]
    check("C1.PICK %d eligible windows (n_zone %d..%d); picks h = %s "
          "(middle IS the v563 reference h = 540)"
          % (len(elig), elig[0][1], elig[-1][1],
             [r["h"] for r in wins]),
          wins[1]["h"] == 540 and len(picks) == 3)

    # orient the sheet functional ONCE on the first window's final point
    r0 = wins[0]
    y_end0 = np.array([r0["S"][0, 0], r0["S"][1, 1], r0["S"][0, 1]])
    z_end0 = PinvN @ y_end0
    if float(z_end0 @ (JfixN @ vp)) < 0.0:
        vp = -vp
    Jfvp = JfixN @ vp
    ell_scale = float(np.linalg.norm(Jfvp))
    print("    sheet orientation fixed: ell(z) = z^T J_fix v_plus with "
          "v_plus = %s (v627 convention, sign fixed on window h=%d)"
          % (np.round(vp, 6).tolist(), r0["h"]))

    # ray lattice of the (closed) forward cone, sheet +
    pts = []
    for a in RAY_SCALE:
        for rr in RAY_R:
            for th in np.linspace(0.0, 2.0 * math.pi, N_THETA,
                                  endpoint=False):
                pts.append(a * (vp + rr * (
                    math.cos(th) * math.sqrt(lamp / -lam1) * v1
                    + math.sin(th) * math.sqrt(lamp / -lam2) * v2)))
    pts = np.array(pts)
    q_pts = np.einsum("ki,ij,kj->k", pts, JfixN, pts)
    l_pts = pts @ Jfvp
    check("S0.LAT ray lattice of the forward cone: %d points, all with "
          "q >= %.1e and ell > 0 (min q = %.3e, min ell = %.3e)"
          % (len(pts), -TOL_RAY, float(np.min(q_pts)),
             float(np.min(l_pts))),
          float(np.min(q_pts)) >= -TOL_RAY * float(np.max(pts ** 2))
          and float(np.min(l_pts)) > 0.0)

    def preserves(t):
        P2 = pts + t[None, :]
        q2 = np.einsum("ki,ij,kj->k", P2, JfixN, P2)
        l2 = P2 @ Jfvp
        sc = np.maximum(1.0, np.sum(P2 ** 2, axis=1))
        return bool(np.all(q2 >= -TOL_RAY * sc)
                    and np.all(l2 >= -TOL_RAY * np.sqrt(sc)))

    t_time = 0.7 * vp
    t_space = math.sqrt(lamp / -lam1) * v1
    check("S0.RAY translation semigroup lemma on the lattice: a forward "
          "timelike t preserves C+ (%s -- must hold), a SPACELIKE t "
          "does NOT (%s -- must-fail control fires)"
          % (preserves(t_time), preserves(t_space)),
          preserves(t_time) and not preserves(t_space))

    # ============================================================== C1/C2
    stats_true = []
    cong_worst = 0.0
    wire_worst = 0.0
    for r in wins:
        nn = np.round(np.exp(r["uu"])).astype(np.int64)
        st = path_stats("TRUE h=%d" % r["h"], r["uu"], r["lam"],
                        r["Xn"], Jfvp, ell_scale)
        S = r["S"]
        y_ref = np.array([S[0, 0], S[1, 1], S[0, 1]])
        wire = float(np.max(np.abs(st["Y_end"] - y_ref))
                     / max(1.0, float(np.max(np.abs(y_ref)))))
        wire_worst = max(wire_worst, wire)
        cong_worst = max(cong_worst, st["cong"])
        stats_true.append((r, st, nn))
        print()
        print_path(st, nn)
    check("C1.WIRE cumulative endpoint equals the v563 S matrix on all "
          "3 windows (worst rel dev %.1e <= %.0e)"
          % (wire_worst, TOL_WIRE), wire_worst <= TOL_WIRE)
    check("C1.CONG transport identity z^T J_fix z = 2 det S_k along ALL "
          "trajectory points (worst rel residual %.1e <= %.0e)"
          % (cong_worst, TOL_CONG), cong_worst <= TOL_CONG)
    check("C1.V627 all 3 true final points lie IN the positive cone on "
          "the + sheet (final 2 det S = %s) -- the static v627 chamber "
          "statement reproduced at the path endpoints"
          % (["%.3f" % st["q"][-1] for _, st, _ in stats_true]),
          all(st["final_in"] for _, st, _ in stats_true))

    print("\nC2 -- the semigroup test")
    # linearity check of the update map on the reference window, atom 0
    r_ref, st_ref, nn_ref = stats_true[1]
    t0 = r_ref["lam"][0] * r_ref["Xn"][0]
    y_probe = np.array([1.0, 2.0, 0.5])
    dev_lin = float(np.max(np.abs((2.0 * y_probe + t0)
                                  - 2.0 * (y_probe + t0))))
    check("C2.LIN the atom update y -> y + rho_n x_n is NOT linear in "
          "the 3 coordinates: F(2y) - 2F(y) = -t_n != 0 (|dev| = %.3e "
          "= |t_%d|); it is a pure TRANSLATION (affine, identity "
          "linear part) -- 'Lorentz transformation per prime' does NOT "
          "exist on this surface; the semigroup question is the "
          "ADDITIVE forward-cone question" % (dev_lin, int(nn_ref[0])),
          dev_lin > 0.0)

    # ray-lattice equivalence on actual atom increments (sampled)
    Tz = st_ref["T_z"]
    inc = st_ref["inc_fwd"]
    idx_in = np.where(inc)[0][:2]
    idx_out = np.where(~inc)[0][:2]
    equiv_ok = True
    for k in idx_in:
        equiv_ok &= preserves(Tz[k])
    for k in idx_out:
        equiv_ok &= (not preserves(Tz[k]))
    check("C2.EQ criterion equivalence on ACTUAL atom increments "
          "(h=540): in-cone increments %s preserve the lattice, "
          "out-of-cone increments %s do not"
          % ([int(nn_ref[k]) for k in idx_in],
             [int(nn_ref[k]) for k in idx_out]),
          equiv_ok and len(idx_in) > 0)

    sem_alive = all(st["frac_in"] == 1.0 for _, st, _ in stats_true)
    mono_true = all(st["n_decr"] == 0 for _, st, _ in stats_true)
    check("C2.SEM semigroup measurement: increment forward-cone "
          "fractions %s (rho^2-weighted %s) -- the per-prime updates "
          "are %s"
          % (["%.4f" % st["frac_in"] for _, st, _ in stats_true],
             ["%.4f" % st["frac_in_w"] for _, st, _ in stats_true],
             "ALL cone-preserving translations (semigroup ALIVE)"
             if sem_alive else
             "NOT all cone-preserving (semigroup fails pointwise)"),
          True)
    check("C2.MONO path-monotonicity measurement: ell decreasing-step "
          "fractions %s, drawdown/final %s -- %s"
          % (["%.4f" % st["frac_decr"] for _, st, _ in stats_true],
             ["%.2e" % (st["drawdown"] / abs(st["ell"][-1]))
              for _, st, _ in stats_true],
             "ell is exactly monotone" if mono_true else
             "ell is NOT monotone (measured fractions above)"),
          True)

    # ============================================================== C3
    print("\nC3 -- controls (scramble + Epstein); separation bar "
          "BAR_SEP = %.2f declared" % BAR_SEP)

    # Epstein arithmetic + guards
    t_ep = time.time()
    r1 = lattice_r1(X_CAP)
    check("C3.EP0 Epstein input: r_Q1 lattice count to %d, r_Q1(1) = %d "
          "(b_1 = 1 after /2), all even: %s (%.1f s)"
          % (X_CAP, int(r1[1]), bool(np.all(r1[1:] % 2 == 0)),
             time.time() - t_ep),
          r1[1] == 2 and bool(np.all(r1[1:] % 2 == 0)))
    ones = np.ones(X_CAP + 1, dtype=np.int64)
    lam_chk = dirichlet_vonmangoldt(ones, X_CAP)
    dev_div = float(np.max(np.abs(lam_chk - core.LAM_TAB[:X_CAP + 1])))
    check("C3.EP1 division machinery validated on zeta: rebuilt Lambda "
          "vs the v563 sieve table, max dev %.1e < %.0e"
          % (dev_div, TOL_DIV), dev_div < TOL_DIV)
    lam_E = dirichlet_vonmangoldt((r1 // 2).astype(np.int64), X_CAP)
    ispp = core.LAM_TAB[:X_CAP + 1] > 0.0
    neg_idx = np.where(lam_E < -LAM_TOL)[0]
    offpp = np.where((~ispp) & (np.abs(lam_E) > LAM_TOL))[0]
    offpp = offpp[offpp >= 2]
    check("C3.EP2 Lambda_E is a genuine non-Euler control: %d negative "
          "sites (first n = %d), %d non-prime-power support points "
          "(first n = %d)"
          % (len(neg_idx), int(neg_idx[0]) if len(neg_idx) else -1,
             len(offpp), int(offpp[0]) if len(offpp) else -1),
          len(neg_idx) > 0 and len(offpp) > 0)

    logn = np.zeros(X_CAP + 1)
    logn[1:] = np.log(np.arange(1, X_CAP + 1, dtype=float))
    sqn = np.sqrt(np.arange(X_CAP + 1, dtype=float))
    sqn[0] = 1.0

    def epstein_inputs(r):
        a2 = 2.0 * r["alpha"]
        idx = np.where(np.abs(lam_E) > LAM_TOL)[0]
        idx = idx[(idx >= 2) & (logn[idx] <= a2 + 1.0e-14)]
        uE = logn[idx]
        rhoE = lam_E[idx] / sqn[idx]
        assert uE[0] > r["D"], "reflection branch would be live"
        XnE = np.stack([spline_read_vec(r["W11"], uE, r["D"]),
                        spline_read_vec(r["W22"], uE, r["D"]),
                        spline_read_vec(r["W12"], uE, r["D"])], axis=1)
        return idx, uE, rhoE, XnE

    sep_scr = {s: False for s in SCR_SEEDS}
    sep_eps = False
    for (r, stT, _nn) in stats_true:
        print("\n  window h = %d controls:" % r["h"])
        for s in SCR_SEEDS:
            rs = core.build_window(r["k"], scramble_seed=s)
            stS = path_stats("SCRAMBLE seed=%d" % s, rs["uu"], rs["lam"],
                             rs["Xn"], Jfvp, ell_scale)
            print_path(stS)
            sep = ((not stS["final_in"])
                   or stS["frac_in"] <= stT["frac_in"] - BAR_SEP
                   or stS["frac_decr"] >= stT["frac_decr"] + BAR_SEP)
            sep_scr[s] |= sep
            print("      -> separates from TRUE (bar %.2f): %s"
                  % (BAR_SEP, sep))
        idxE, uE, rhoE, XnE = epstein_inputs(r)
        stE = path_stats("EPSTEIN Lambda_E", uE, rhoE, XnE, Jfvp,
                         ell_scale)
        print_path(stE, nn=idxE)
        sep = ((not stE["final_in"])
               or stE["frac_in"] <= stT["frac_in"] - BAR_SEP
               or stE["frac_decr"] >= stT["frac_decr"] + BAR_SEP)
        sep_eps |= sep
        print("      -> separates from TRUE (bar %.2f): %s"
              % (BAR_SEP, sep))

    scr_all = all(sep_scr.values())
    check("C3.SEP separation ledger: scramble seeds separate on >= 1 "
          "window each: %s; Epstein separates on >= 1 window: %s -- %s"
          % (dict(sep_scr), sep_eps,
             "both control families separate" if (scr_all and sep_eps)
             else "NOT all controls separate -- the cone dynamics reads "
             "the DENSITY layer, not the arithmetic (v627 H4 one level "
             "deeper)"), True)

    # ============================================================== verdict
    print("\n" + "=" * 78)
    if sem_alive and scr_all and sep_eps:
        VERDICT = "SEMIGROUP-ALIVE"
        why = ("every prime increment is a cone-preserving translation "
               "AND both control families break that")
    elif (not sem_alive) and mono_true and scr_all and sep_eps:
        VERDICT = "PATH-MONOTONE-ONLY"
        why = ("increments leave the cone pointwise, but the sheet "
               "functional is exactly monotone on the true paths and "
               "the controls break the reading")
    else:
        VERDICT = "CONE-DYNAMICS-DEAD"
        parts = []
        if not sem_alive:
            parts.append("increments are NOT all cone-preserving "
                         "(fractions %s)"
                         % ["%.3f" % st["frac_in"]
                            for _, st, _ in stats_true])
        if not mono_true:
            parts.append("ell is NOT monotone on the true path "
                         "(decreasing fractions %s)"
                         % ["%.3f" % st["frac_decr"]
                            for _, st, _ in stats_true])
        if not (scr_all and sep_eps):
            parts.append("controls do not fully separate (scramble %s, "
                         "Epstein %s) -- the dynamics reads density, "
                         "not arithmetic" % (dict(sep_scr), sep_eps))
        why = "; ".join(parts)
    print("VERDICT: %s -- %s" % (VERDICT, why))
    print("checks: %d, failures: %d %s" % (N_CHK, len(FAILS),
                                           FAILS or ""))
    print("elapsed: %.1f s" % (time.time() - T0))
    return len(FAILS)


if __name__ == "__main__":
    raise SystemExit(1 if run() else 0)
