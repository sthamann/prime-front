#!/usr/bin/env python3
"""STRATEGY-3 / L1: finite Sonin--prolate compression on TFPT windows.

Exploration only.  This is a finite, zero-free operator experiment inspired by
Connes--Consani (2021); it is not their theorem and it makes no RH claim.

For every window in the nine-member frame-A ladder, construct on the full
piecewise-linear u grid

  P_h      = multiplication by 1_{|u| <= U0},
  P_hat_h  = Fourier-band projection 1_{|tau| <= T0},

with U0 = log(2)/2 and T0 = pi/(2 U0), so that 2 U0 T0 / pi = 1: one
self-dual phase-space cell.  Restrict both projections to the odd window
sector.  Their common kernel is the finite Sonin complement.

Let B_h be the deployed positive Weil window form and S_h the orthogonal
projection onto that complement.  The part not supplied by the compression is

    R_h = B_h - S_h B_h S_h.

Whitening by B_h turns this into I-K_h, where the generalized eigenvalues of

    S_h B_h S_h v = lambda B_h v

above one are precisely the non-positive directions of R_h.  Since R_h has
rank at most twice the number of projection constraints, all nontrivial
eigenvalues are recovered from the top 2r+8 generalized eigenpairs.

Preregistered interpretation:
  * FINITE-RANK-WALL if bad_rank <= 4 uniformly over all nine windows.
  * RANK-GROWS (kill) if bad_rank grows beyond 4.
  * DEFECT-PERSISTS (kill) if lambda_max-1 does not decrease and is still
    above 0.05 on the largest window.
  * POLE-CONDITIONABLE only if the bad subspace remaining after one condition
    along the closed rank-one E8/pole boundary vector has no Rayleigh quotient
    above 1+5e-8, pole overlap is >= 0.70, and adjacent-window bad-direction
    fidelity is >= 0.80.  The conditioned number computed here is a rigorous
    lower bound inside the measured bad eigenspace: if it remains above one,
    one pole condition definitely cannot cure the remainder; if it falls below
    one, a full-space theorem is still required.

The construction path loads no zeros and no prime table.  Verification tables
enter only through the already-declared frame constructor used by the moonshot
probes.  No file is written by this script.
"""

import ast
import math
import os
import sys
import time

import numpy as np
import scipy.linalg as sla

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)
sys.path.insert(0, os.path.abspath(os.path.join(_HERE, "..", "..",
                                                "verification")))

import v563_paper2_readouts as core  # noqa: E402
import moonshot_arch_glue_probe as stage2  # noqa: E402
import moonshot_spectral_probe as stage4  # noqa: E402


U_CUT = 0.5 * math.log(2.0)
T_CUT = math.pi / (2.0 * U_CUT)
PHASE_CELLS = 2.0 * U_CUT * T_CUT / math.pi

SVD_TOL = 1.0e-10
EXACT_TOL = 2.0e-10
BAD_TOL = 5.0e-8
RANK_CAP = 4
FINAL_EXCESS_BAR = 5.0e-2
POLE_OVERLAP_BAR = 0.70
DRIFT_FIDELITY_BAR = 0.80
PROFILE_N = 2048

BANNED = ("zetazero", "nzeros", "isprime", "primerange", "nextprime",
          "prevprime", "primepi", "sympy")

CHECKS = []
FAILS = []


def check(name, ok, detail=""):
    CHECKS.append(name)
    if not ok:
        FAILS.append(name.split()[0])
    print("[%s] %s%s" % ("PASS" if ok else "FAIL", name,
                         (": " + detail) if detail else ""))
    return bool(ok)


def outcome(name, ok, detail=""):
    print("[%s] %s%s" % ("PASS" if ok else "FAIL", name,
                         (": " + detail) if detail else ""))
    return bool(ok)


def ast_firewall():
    with open(os.path.abspath(__file__), "r", encoding="utf-8") as fh:
        tree = ast.parse(fh.read())
    hits = set()
    for node in ast.walk(tree):
        name = ""
        if isinstance(node, ast.Name):
            name = node.id
        elif isinstance(node, ast.Attribute):
            name = node.attr
        elif isinstance(node, (ast.Import, ast.ImportFrom)):
            for alias in node.names:
                token = alias.name.split(".")[0]
                if any(b in token.lower() for b in BANNED):
                    hits.add(token)
        if name and any(b in name.lower() for b in BANNED):
            hits.add(name)
    return sorted(hits)


def odd_basis(M):
    h = M // 2
    U = np.zeros((M, h))
    j = np.arange(h)
    U[j, j] = 1.0 / math.sqrt(2.0)
    U[M - 1 - j, j] = -1.0 / math.sqrt(2.0)
    return U


def projection_data(M, D):
    """Return the odd-sector finite Sonin projector and diagnostics."""
    h = M // 2
    U = odd_basis(M)
    u = (np.arange(M) - 0.5 * (M - 1)) * D
    k = np.arange(-M // 2, M // 2)
    tau = 2.0 * math.pi * k / (M * D)
    mt = np.abs(u) <= U_CUT + 1.0e-14
    mf = np.abs(tau) <= T_CUT + 1.0e-14

    At = U[mt, :]
    Fband = np.exp(-1j * np.outer(tau[mf], u)) / math.sqrt(M)
    Af = Fband @ U
    A = np.vstack((At, Af.real, Af.imag))
    _uu, sv, vh = sla.svd(A, full_matrices=False,
                          lapack_driver="gesdd", check_finite=False)
    rank = int(np.sum(sv > SVD_TOL * sv[0])) if len(sv) else 0
    Q = vh[:rank, :].T
    S = np.eye(h) - Q @ Q.T

    P = np.diag(mt.astype(float))
    Ph = Fband.conj().T @ Fband
    po = U.T @ P @ U
    pho = np.real_if_close(U.T @ Ph @ U).real
    proj_dev = max(float(np.linalg.norm(P @ P - P, ord=2)),
                   float(np.linalg.norm(Ph @ Ph - Ph, ord=2)),
                   float(np.linalg.norm(S @ S - S, ord=2)))
    annih = float(np.linalg.norm(A @ S, ord=2))
    parity_imag = float(np.max(np.abs(np.imag(U.T @ Ph @ U))))
    trace_overlap = float(np.trace(po @ pho))
    return dict(U=U, u=u, S=S, Q=Q, constraint_rank=rank,
                n_time=int(np.sum(mt)), n_band=int(np.sum(mf)),
                proj_dev=proj_dev, annih=annih,
                parity_imag=parity_imag, trace_overlap=trace_overlap)


def bad_space_measure(window):
    M = window["M"]
    h = M // 2
    pd = projection_data(M, window["D"])
    B = core.odd_toeplitz(window["car"] + window["cat"], M)
    B = 0.5 * (B + B.T)
    pole = -core.odd_toeplitz(window["cp"], M)
    pole = 0.5 * (pole + pole.T)
    lmin_B = float(sla.eigvalsh(B, subset_by_index=[0, 0],
                                check_finite=False)[0])
    check("S1.BPOS.h%d" % h, lmin_B > 0.0,
          "lambda_min(B)=%.6e" % lmin_B)

    S = pd["S"]
    SBS = S @ B @ S
    SBS = 0.5 * (SBS + SBS.T)
    nontrivial_cap = min(h, 2 * pd["constraint_rank"] + 8)
    lo = h - nontrivial_cap
    ev, vec = sla.eigh(SBS, B, subset_by_index=[lo, h - 1],
                       driver="gvx", check_finite=False)
    bad_mask = ev > 1.0 + BAD_TOL
    bad_ev = ev[bad_mask]
    bad_vec = vec[:, bad_mask]
    bad_rank = len(bad_ev)
    lammax = float(ev[-1])
    top = vec[:, -1]

    ep, Up = sla.eigh(pole, subset_by_index=[h - 1, h - 1],
                      check_finite=False)
    bvec = Up[:, 0]
    binv_b = sla.solve(B, bvec, assume_a="pos", check_finite=False)
    dual_norm = math.sqrt(max(0.0, float(bvec @ binv_b)))
    pole_overlap = abs(float(bvec @ top)) / max(dual_norm, 1.0e-300)

    conditioned_bad = 1.0
    if bad_rank >= 2:
        a = (bad_vec.T @ bvec) / max(dual_norm, 1.0e-300)
        Z = sla.null_space(a.reshape(1, -1), rcond=SVD_TOL)
        if Z.shape[1]:
            conditioned_bad = float(np.max(sla.eigvalsh(
                Z.T @ np.diag(bad_ev) @ Z, check_finite=False)))
    elif bad_rank == 1 and pole_overlap < 1.0 - 1.0e-8:
        # There is no nonzero vector inside a one-dimensional bad subspace
        # satisfying the condition.  Record one; the full-space problem is
        # deliberately not certified by this favorable branch.
        conditioned_bad = 1.0

    profile = pd["U"] @ top
    return dict(h=h, M=M, D=window["D"], alpha=window["alpha"],
                bad_rank=bad_rank, lammax=lammax,
                excess=lammax - 1.0, pole_overlap=pole_overlap,
                conditioned_bad=conditioned_bad, pole_eval=float(ep[0]),
                profile_u=pd["u"], profile=profile, lmin_B=lmin_B,
                **{k: pd[k] for k in ("constraint_rank", "n_time",
                                      "n_band", "proj_dev", "annih",
                                      "parity_imag", "trace_overlap")})


def profile_fidelities(rows):
    edge = min(float(np.max(np.abs(r["profile_u"]))) for r in rows)
    grid = np.linspace(-edge, edge, PROFILE_N)
    profiles = []
    for r in rows:
        v = np.interp(grid, r["profile_u"], r["profile"])
        nrm = math.sqrt(float(np.trapezoid(v * v, grid)))
        profiles.append(v / max(nrm, 1.0e-300))
    out = []
    for a, b in zip(profiles[:-1], profiles[1:]):
        out.append(abs(float(np.trapezoid(a * b, grid))))
    return out


def run():
    t0 = time.time()
    print("=" * 78)
    print("STRAT3 SONIN/PROLATE -- finite-rank test of the L1 remainder")
    print("=" * 78)
    hits = ast_firewall()
    check("G0.1 AST firewall", not hits, str(hits))
    check("G0.2 self-dual cutoff", abs(PHASE_CELLS - 1.0) < 1.0e-14,
          "U0=%.12f, T0=%.12f, 2U0T0/pi=%.16f"
          % (U_CUT, T_CUT, PHASE_CELLS))

    windows = stage4.family_ext()
    check("G0.3 nine-window family", len(windows) == 9,
          ", ".join("h=%d" % (w["M"] // 2) for w in windows))

    rows = []
    for w in windows:
        r = bad_space_measure(w)
        rows.append(r)
        exact = max(r["proj_dev"], r["annih"], r["parity_imag"])
        check("S1.PROJ.h%d" % r["h"], exact <= EXACT_TOL,
              "rank(C)=%d, nt=%d, nf=%d, dev=%.2e, AS=%.2e, "
              "Im(P_hat_odd)=%.2e, Tr(PP_hat)=%.6f"
              % (r["constraint_rank"], r["n_time"], r["n_band"],
                 r["proj_dev"], r["annih"], r["parity_imag"],
                 r["trace_overlap"]))
        print("  h=%4d  bad_rank=%3d  lambda_max=%.9f  excess=%+.3e  "
              "pole_overlap=%.4f  cond_bad_lb=%.9f"
              % (r["h"], r["bad_rank"], r["lammax"], r["excess"],
                 r["pole_overlap"], r["conditioned_bad"]))

    fids = profile_fidelities(rows)
    ranks = [r["bad_rank"] for r in rows]
    excess = np.array([max(r["excess"], 1.0e-300) for r in rows])
    hs = np.array([r["h"] for r in rows], float)
    excess_slope = float(np.polyfit(np.log(hs), np.log(excess), 1)[0])
    uniform_rank = max(ranks) <= RANK_CAP
    defect_closes = excess_slope < -0.10 and rows[-1]["excess"] \
        <= FINAL_EXCESS_BAR
    pole_conditions = all(r["conditioned_bad"] <= 1.0 + BAD_TOL
                          for r in rows) \
        and min(r["pole_overlap"] for r in rows) >= POLE_OVERLAP_BAR \
        and min(fids) >= DRIFT_FIDELITY_BAR

    print("\nS2 -- preregistered outcome gates")
    outcome("S2.1 UNIFORM FINITE BAD RANK <= %d" % RANK_CAP, uniform_rank,
            "ranks=" + "/".join(str(x) for x in ranks))
    outcome("S2.2 LARGEST DEFECT CLOSES TO ONE", defect_closes,
            "excess %.3e -> %.3e, log-log slope %.3f, final bar %.2f"
            % (rows[0]["excess"], rows[-1]["excess"], excess_slope,
               FINAL_EXCESS_BAR))
    outcome("S2.3 ONE E8/POLE CONDITION IS STABLE AND SUFFICIENT",
            pole_conditions,
            "min pole overlap %.4f, min adjacent fidelity %.4f, "
            "max conditioned-bad lower bound %.9f"
            % (min(r["pole_overlap"] for r in rows), min(fids),
               max(r["conditioned_bad"] for r in rows)))

    if uniform_rank and defect_closes and pole_conditions:
        verdict = "SONIN-POLE-CONDITIONED"
    elif uniform_rank:
        verdict = "SONIN-FINITE-RANK-WALL"
    else:
        verdict = "SONIN-RANK-GROWS"

    print("\nVERDICT: %s" % verdict)
    if uniform_rank:
        print("THEOREM STILL NEEDED: prove that these finite Sonin projectors "
              "form a covariant semi-local inductive system, that the measured "
              "bad subspace has the same uniform finite dimension for every "
              "window/support, and that explicit arithmetic boundary "
              "conditions push all its generalized eigenvalues below one.  "
              "This is the finite-place analogue of the Connes--Consani "
              "archimedean conditioning step; the present computation alone "
              "does not provide the global quantifier.")
    else:
        print("KILL: the chosen canonical one-cell Sonin compression does not "
              "reduce the TFPT remainder to uniformly few directions.  A "
              "different cutoff may be studied only with a new preregistered "
              "geometric reason; tuning U0/T0 after this result is forbidden.")

    elapsed = time.time() - t0
    if FAILS:
        print("RESULT: %d/%d construction checks passed; FAILURES %s (%.1fs)"
              % (len(CHECKS) - len(FAILS), len(CHECKS),
                 ",".join(FAILS), elapsed))
        return 1
    print("RESULT: ALL %d CONSTRUCTION CHECKS PASSED (%.1fs)"
          % (len(CHECKS), elapsed))
    return 0


if __name__ == "__main__":
    raise SystemExit(run())
