#!/usr/bin/env python3
"""v707 -- PRIME.SECTIONEDGE.01: S-E, THE CLOSED FORM OF THE
SECTION-POSITIVITY EDGE: is the exact mass the Christoffel-Darboux /
resolvent edge formula of the predecessor section at the binding
depth?

EXPLORATION ONLY (experiments/ firewall): nothing here is a
verification claim; no verification/, paper, ledger or website surface
is touched; no marker moves; NO RH statement.  File prefix chain_
(round 9 owns the suite surfaces; the beam worker owns z1_*).

FRAME.  S-D ended with: the exact mass characterization is the EDGE
condition of the generalized eigenvalue problem
    T_N(prev) + w T_N(cu)  >= 0   (critical),
not a pointwise m-function evaluation.  S-E derives and machine-
verifies the closed edge formula and measures where the true mass
sits relative to the edge.

STRUCTURAL CAVEAT DECLARED UP FRONT (E1 measures it): the deployed
atom is a SINGLE-LAG (tent) insertion -- the z1_uvarov DUALITY POINT
-- not a circle point mass.  A point mass at theta_0 has moments
~ cos(m theta_0) for ALL m and Toeplitz rank 2 (the classical
Christoffel/Uvarov case, closed 2x2 CD-kernel formula).  The tent
read is lag-sparse, hence frequency-DENSE: its Toeplitz section is
expected HIGH rank.  The closed edge formula survives anyway,
because the edge needs only the EXTREME eigenvalue of the compressed
resolvent, not a low-rank update:

  EDGE FORMULA (derived, then machine-verified as an identity).
  Let A = T_N(prev), B = T_N(cu), and let w_c be any interior
  admissible point (C := A + w_c B > 0).  Then with
  M := C^{-1/2} B C^{-1/2}:
      {w : A + w B >= 0} = [w_c - 1/lambda_max(M),
                            w_c - 1/lambda_min(M)]
  (t = w - w_c: I + t M >= 0 <=> -1/lambda_max <= t <= -1/lambda_min
  for lambda_min < 0 < lambda_max).  For A > 0 one may take w_c = 0:
  the edges are reciprocal extreme eigenvalues of A^{-1/2}BA^{-1/2}
  -- resolvent data of the predecessor section.  For a rank-2 point
  mass B = 2(cc^T + ss^T), the nonzero spectrum of M collapses to the
  2x2 CD-kernel Gram [c^T A^-1 c, c^T A^-1 s; ., s^T A^-1 s] == the
  classical K_N(z0, z0) / K_N(z0, zbar0) formula.

MEASUREMENTS (bars declared BEFORE any number; window 2 primary,
window 0 spot check):
  E1 [M] the rank structure: numerical rank of T_N(cu) for the
     deployed tent read (N = 300) vs the rank of the point-mass
     comparison (must be 2).  Expected: tent rank = N - O(1) -- the
     literal rank-2 premise falls (duality point), the r x r formula
     is replaced by the one-extreme-eigenvalue resolvent formula.
  E2 [E] the edge identities (machine precision, bar 1e-6 rel):
     (a) A > 0 case (pure background below its breakdown, slot-2
         read): closed edges vs direct bisection of
         lambda_min(A + wB) = 0;
     (b) the classical rank-2 CD case (synthetic point mass,
         theta_0 = 0.7): closed 2x2 CD formula vs direct bisection
         (the Christoffel/Uvarov identity, honored exactly);
     (c) A indefinite case (N past the predecessor death, interior
         anchor w_c): same identity.
  E3a [M] slot-local edges with exact past (all 40 slots, window 2),
     TWO horizons kept strictly apart:
     E3a.1 just-in-time horizon N = m0(next slot): the corridor the
        current atom must keep open until the next atom arrives
        (S-A criterion A, now via the CLOSED formula).  Bars: the
        true mass lies INSIDE every corridor (pos in (0,1)); report
        midpoint vs mu (benchmarks: S-B C2 median 0.9947 / max 0.31;
        S-D K2b ~ 0.40x) and the corridor-position statistics.
     E3a.2 death-depth horizon N* = max survival over a w-scan (the
        deepest any single w reaches WITHOUT the next atom): does
        the last surviving island select the true mass?  Typed as
        measured -- S-A predicts NO unique selection (out-of-
        corridor w die downstream at varying depths, so the argmax
        island need not contain mu).
     Plus the N-dependence of the edges on 3 sample slots.
  E3b [M] full-ladder edges (ALL window atoms true, target slot
     free; 6 slots x depths {0.5, 0.75, 0.98} x (M-1)): corridor
     width vs depth (binding = deepest), and the distance of the
     true mass to the full-depth corridor (S-A A2 halfwidths
     ~ 1e-5 -- boundary positivity, CONDITIONED on the future,
     typed circular as prediction).
  E4 verdict (preregistered):
     G1-EDGE-CLOSED       iff E2 passes AND the death-depth edge
                          midpoint hits the mass < 1% uniform;
     EDGE-EXACT-SELECTION-OPEN iff E2 passes AND the full-ladder
                          corridor pins the mass to <= 1e-3 but the
                          slot-local selection does not reach 1%
                          uniform ("Kante exakt, Selektion im
                          Korridor offen" -- with the measured
                          corridor-position law as the residue);
     EDGE-BROKEN          iff any E2 identity fails.

FIREWALL: AST-checked -- no zetazero/nzeros/zeta anywhere.  MU_ALL
enters as exact-past conditioning and as the structural anchor w_c
of the edge computation (the edges are anchor-independent; declared)
and as comparison target.  No prediction claim is made from a path
containing MU_ALL.

Provenance (read-only): v563 core, z1_uvarov (duality point),
chain_tolerance_scaling (S-A corridors/death locations),
chain_mass_law (S-B benchmark), chain_weyl_mass (S-D verdict),
classical Christoffel/Uvarov theory (cited).

PROVENANCE: discovery probe chain_section_edge_probe.py (2026-08-03,
9/9 PASS, verdict EDGE-EXACT-SELECTION-OPEN: the edge formula is a
resolvent identity, exact to 3e-13 [E]; the full-ladder edge pins the
mass to 2.6e-04; the true mass sits at the just-in-time corridor
position median 0.534, IQR [0.511, 0.559] -- the selection principle
stays open).  Promoted verbatim; numbers unchanged.
"""
import ast
import math
import os
import sys
import time

import numpy as np
import scipy.linalg as sla

_here = os.path.dirname(os.path.abspath(__file__))
for _cand in (_here, os.path.join(_here, "..", "..", "verification")):
    if os.path.exists(os.path.join(_cand, "v563_paper2_readouts.py")):
        sys.path.insert(0, os.path.abspath(_cand))
        break

T0 = time.time()
FAILS = []
N_CHK = 0

BANNED = ("zetazero", "nzeros", "zeta", "second_sheet_zero")


def check(name, ok, detail=""):
    global N_CHK
    N_CHK += 1
    if not ok:
        FAILS.append(name.split()[0])
    print("[%s] %s%s" % ("PASS" if ok else "FAIL", name,
                         (": " + detail) if detail else ""))


def ast_firewall(src_path):
    with open(src_path, "r", encoding="utf-8") as fh:
        tree = ast.parse(fh.read())
    for node in ast.walk(tree):
        if isinstance(node, ast.Attribute) and node.attr in BANNED:
            return False
        if isinstance(node, ast.Name) and node.id in BANNED:
            return False
    return True


import v563_paper2_readouts as core  # noqa: E402  (READ-ONLY import)

U_SLOTS = math.log(120.0)
BAR_ID = 1e-6
RANK_N = 300
THETA_PM = 0.7
E3B_NS = (2, 5, 9, 23, 53, 101)
E3B_FRACS = (0.5, 0.75, 0.98)


def window_geometry(kz):
    alpha = float(core.U_ALL[kz])
    D_k = 0.5 * float(core.G_ALL[kz]) / float(core.NU_MAIN)
    M = int(math.ceil(alpha / D_k - 1.0e-9)) + 1
    if M % 2:
        M += 1
    return alpha, M


def g_pole(tv):
    tv = abs(tv)
    return -4.0 * (math.exp(tv / 2) + math.exp(-tv / 2) - 2.0)


def pole_lags(M, D):
    return np.array([-(g_pole((d - 1) * D) - 2.0 * g_pole(d * D)
                       + g_pole((d + 1) * D)) / D for d in range(M)])


def build_win(kz):
    alpha, M = window_geometry(kz)
    D = 2.0 * alpha / M
    ka = core.atoms_in(alpha)
    c_ar = core.arch_lags(M, D)
    cp = pole_lags(M, D)
    return dict(kz=kz, alpha=alpha, M=M, D=D, ka=ka, p_sm=c_ar + cp)


def unit_read(w, u):
    c1, _ = core.atom_lags_at(w["alpha"], w["M"],
                              np.array([u]), np.array([1.0]))
    return c1


def slot_list(w):
    out = []
    for i in range(w["ka"]):
        u = float(core.U_ALL[i])
        if u > U_SLOTS:
            break
        cu = unit_read(w, u)
        nz = np.nonzero(cu)[0]
        out.append(dict(i=i, n=int(round(math.exp(u))), u=u,
                        mu=float(core.MU_ALL[i]), cu=cu,
                        ist=int(nz[np.argmax(np.abs(cu[nz]))]),
                        m0=int(nz[0])))
    return out


def bd_of(r, N):
    r = np.asarray(r, float)
    a = np.zeros(N + 1)
    a[0] = 1.0
    E = float(r[0])
    for n in range(1, N + 1):
        acc = r[n] + (float(a[1:n] @ r[n - 1:0:-1]) if n > 1 else 0.0)
        k = -acc / E
        a[1:n + 1] = a[1:n + 1] + k * a[n - 1::-1][:n]
        E *= (1.0 - k * k)
        if not (abs(k) < 1.0) or E <= 0.0:
            return n
    return None


def toep(r, N):
    return sla.toeplitz(r[:N])


def edges_anchored(prev, cu, Nm, w_c):
    """Closed edge formula: [w_lo, w_hi] of {w : T(prev + w cu) >= 0}
    anchored at interior w_c.  Returns (w_lo, w_hi, lam_min_C)."""
    C = toep(prev + w_c * cu, Nm)
    B = toep(cu, Nm)
    lam, V = np.linalg.eigh(C)
    if lam[0] <= 0:
        return float("nan"), float("nan"), float(lam[0])
    Ci = V * (1.0 / np.sqrt(lam))[None, :]
    Mres = Ci.T @ B @ Ci
    mu_ = np.linalg.eigvalsh(0.5 * (Mres + Mres.T))
    lo, hi = float(mu_[0]), float(mu_[-1])
    w_lo = w_c - 1.0 / hi if hi > 0 else -np.inf
    w_hi = w_c - 1.0 / lo if lo < 0 else np.inf
    return w_lo, w_hi, float(lam[0])


def edge_direct(prev, cu, Nm, w_in, w_out, iters=50):
    """Direct bisection of lambda_min(T(prev + w cu)) = 0 between an
    admissible w_in and inadmissible w_out."""
    def lmin(w):
        return float(np.linalg.eigvalsh(toep(prev + w * cu, Nm))[0])
    for _ in range(iters):
        wm = 0.5 * (w_in + w_out)
        if lmin(wm) >= 0:
            w_in = wm
        else:
            w_out = wm
    return w_in


def run():
    print("=" * 78)
    print("S-E CHAIN SECTION EDGE -- the closed form of the "
          "positivity edge")
    print("=" * 78)

    check("G0.0 [E] AST firewall: no zeta/zero symbol anywhere; "
          "MU_ALL as declared conditioning/anchor/target only",
          ast_firewall(os.path.abspath(__file__)))

    zones = core.frame_a_zones()
    fam = []
    for kz in zones:
        alpha, M = window_geometry(kz)
        if math.exp(2.0 * alpha) <= core.ATOM_MAX + 0.5:
            fam.append((kz, alpha, M))
    hs = np.array([t[2] // 2 for t in fam], float)
    picks = [fam[0]]
    for qq in (0.25, 0.5, 0.75, 1.0):
        tgt = float(np.quantile(hs, qq))
        cand = min(fam, key=lambda t_: abs(t_[2] // 2 - tgt))
        if all(cand[0] != p_[0] for p_ in picks):
            picks.append(cand)
    picks = sorted(picks, key=lambda t_: t_[2])
    w0 = build_win(picks[0][0])
    w2 = build_win(picks[2][0])
    for w in (w0, w2):
        w["slots"] = slot_list(w)
    check("G0.1 [E] windows 0 (h=%d) and 2 (h=%d) rebuilt, %d slots "
          "each (u <= log 120)" % (w0["M"] // 2, w2["M"] // 2,
                                   len(w2["slots"])), True)

    # ============================================================== E1
    print("\nE1 -- rank structure of the deployed insertion")
    s5 = next(s for s in w2["slots"] if s["n"] == 5)
    Bt = toep(s5["cu"], RANK_N)
    ev_t = np.linalg.eigvalsh(Bt)
    tol = RANK_N * np.finfo(float).eps * np.max(np.abs(ev_t))
    rank_t = int(np.sum(np.abs(ev_t) > tol))
    jj = np.arange(RANK_N)
    cvec = np.cos(jj * THETA_PM)
    svec = np.sin(jj * THETA_PM)
    Bpm = 2.0 * (np.outer(cvec, cvec) + np.outer(svec, svec))
    ev_pm = np.linalg.eigvalsh(Bpm)
    rank_pm = int(np.sum(np.abs(ev_pm)
                         > RANK_N * np.finfo(float).eps
                         * np.max(np.abs(ev_pm))))
    nzc = int(np.sum(s5["cu"] != 0))
    check("E1.1 [M] RANK STRUCTURE: the deployed tent read (slot "
          "n=5, %d nonzero lags) has Toeplitz rank %d of N=%d "
          "(frequency-dense, NOT low rank -- the z1_uvarov duality "
          "point: single-lag insertion != circle point mass, whose "
          "comparison rank is %d == 2); the literal rank-2 CD "
          "premise falls, the closed edge survives via the "
          "one-extreme-eigenvalue resolvent formula (E2)"
          % (nzc, rank_t, RANK_N, rank_pm),
          rank_pm == 2 and rank_t > 10)

    # ============================================================== E2
    print("\nE2 -- the edge identities")
    # (a) A > 0: pure background below its breakdown, slot-2 read.
    # Levinson step n validates the (n+1)x(n+1) section, so matrix
    # size Nm is PD iff Nm <= bd_bg; bd_bg lies past the n=2 tent
    # cells (S-D G0.1), so Nm_a = bd_bg is PD AND sees the insertion.
    s2 = w2["slots"][0]
    bd_bg = bd_of(w2["p_sm"], w2["M"] - 1)
    Nm_a = bd_bg
    assert Nm_a >= s2["m0"] + 2, "PD section below slot-2 cells"
    w_lo_c, w_hi_c, lminC = edges_anchored(w2["p_sm"], s2["cu"],
                                           Nm_a, 0.0)
    # direct: from w = 0 (admissible) outward both sides
    w_hi_d = edge_direct(w2["p_sm"], s2["cu"], Nm_a, 0.0,
                         max(4.0 * abs(w_hi_c), 1.0))
    w_lo_d = edge_direct(w2["p_sm"], s2["cu"], Nm_a, 0.0,
                         -max(4.0 * abs(w_lo_c), 1.0))
    dev_a = max(abs(w_hi_c - w_hi_d) / abs(w_hi_d),
                abs(w_lo_c - w_lo_d) / abs(w_lo_d))
    print("   (a) A>0, N=%d: closed [%.6f, %.6f] vs direct "
          "[%.6f, %.6f]  rel dev %.1e"
          % (Nm_a, w_lo_c, w_hi_c, w_lo_d, w_hi_d, dev_a))

    # (b) rank-2 CD case: point mass, closed 2x2 CD formula
    A_pd = toep(w2["p_sm"], Nm_a)
    cv = np.cos(np.arange(Nm_a) * THETA_PM)
    sv = np.sin(np.arange(Nm_a) * THETA_PM)
    Xc = np.linalg.solve(A_pd, cv)
    Xs = np.linalg.solve(A_pd, sv)
    G2 = np.array([[cv @ Xc, cv @ Xs], [sv @ Xc, sv @ Xs]])
    lam_G = np.linalg.eigvalsh(0.5 * (G2 + G2.T))
    w_lo_cd = -1.0 / (2.0 * float(lam_G[-1]))   # B_pm psd: lower edge
    pm_lags = np.zeros(w2["M"])
    pm_lags[:Nm_a] = 2.0 * np.cos(np.arange(Nm_a) * THETA_PM)
    w_lo_cd_d = edge_direct(w2["p_sm"], pm_lags, Nm_a, 0.0,
                            4.0 * w_lo_cd)
    dev_b = abs(w_lo_cd - w_lo_cd_d) / abs(w_lo_cd_d)
    print("   (b) rank-2 CD (point mass theta0=%.1f): closed "
          "w_lo = -1/(2 lam_max(CD-Gram)) = %.6f vs direct %.6f  "
          "rel dev %.1e" % (THETA_PM, w_lo_cd, w_lo_cd_d, dev_b))

    # (c) A indefinite: N past the predecessor death, anchored w_c
    Nm_c = s2["m0"] + 40       # beyond bd_bg
    w_c = s2["mu"]             # structural anchor (edges independent)
    w_lo_i, w_hi_i, lminC2 = edges_anchored(w2["p_sm"], s2["cu"],
                                            Nm_c, w_c)
    w_hi_id = edge_direct(w2["p_sm"], s2["cu"], Nm_c, w_c,
                          w_c + 4.0 * abs(w_hi_i - w_c) + 0.1)
    w_lo_id = edge_direct(w2["p_sm"], s2["cu"], Nm_c, w_c,
                          w_c - 4.0 * abs(w_c - w_lo_i) - 0.1)
    dev_c = max(abs(w_hi_i - w_hi_id) / abs(w_hi_id),
                abs(w_lo_i - w_lo_id) / abs(w_lo_id))
    # anchor independence: second anchor inside
    w_c2 = 0.5 * (w_lo_i + w_hi_i)
    w_lo_i2, w_hi_i2, _l = edges_anchored(w2["p_sm"], s2["cu"],
                                          Nm_c, w_c2)
    dev_anch = max(abs(w_lo_i2 - w_lo_i) / abs(w_lo_i),
                   abs(w_hi_i2 - w_hi_i) / abs(w_hi_i))
    print("   (c) A indefinite, N=%d: closed [%.6f, %.6f] vs direct "
          "[%.6f, %.6f]  rel dev %.1e; anchor independence %.1e"
          % (Nm_c, w_lo_i, w_hi_i, w_lo_id, w_hi_id, dev_c,
             dev_anch))
    check("E2.1 [E] EDGE IDENTITIES: closed resolvent formula == "
          "direct lambda_min root in all three regimes (A>0 dev "
          "%.1e; rank-2 CD dev %.1e -- the classical Christoffel/"
          "Uvarov 2x2; A indefinite dev %.1e; anchor independence "
          "%.1e; bar %.0e)"
          % (dev_a, dev_b, dev_c, dev_anch, BAR_ID),
          max(dev_a, dev_b, dev_c, dev_anch) <= BAR_ID)

    # ============================================================= E3a
    print("\nE3a -- slot-local edges, window 2, exact past")
    sl = w2["slots"]
    n_map = {s["n"]: j for j, s in enumerate(sl)}
    prev = w2["p_sm"].copy()
    bgs = {}
    for j, s in enumerate(sl):
        bgs[j] = prev.copy()
        prev += s["mu"] * s["cu"]

    def next_atom_cell(j):
        """First tent cell of the NEXT atom in the FULL atom list
        (the u <= log 120 slot list is truncated; the last slot's
        true successor n = 121 lives beyond it)."""
        if j + 1 < len(sl):
            return sl[j + 1]["m0"]
        u_next = float(core.U_ALL[sl[j]["i"] + 1])
        return int(np.nonzero(unit_read(w2, u_next))[0][0])

    def interior_anchor(bg, s, Nm):
        """Deep-interior admissible w at matrix size Nm: midpoint of
        the Levinson-admissible fw range on a log scan (razor-thin
        corridors need a well-centered anchor for the eigh step)."""
        adm = [fw for fw in np.geomspace(0.05, 20.0, 81)
               if bd_of(bg + fw * s["mu"] * s["cu"], Nm - 1) is None]
        if not adm:
            return float("nan")
        return 0.5 * (min(adm) + max(adm)) * s["mu"]

    # ---- E3a.1: just-in-time horizon N = m0(next slot)
    print("  E3a.1 -- just-in-time horizon N = m0(next)")
    rows = []
    skips = []
    t3 = time.time()
    for j, s in enumerate(sl):
        Nm = min(w2["M"] - 1, next_atom_cell(j))
        w_a = interior_anchor(bgs[j], s, Nm)
        if math.isnan(w_a):
            skips.append((s["n"], "no admissible anchor"))
            continue
        w_lo, w_hi, _l = edges_anchored(bgs[j], s["cu"], Nm, w_a)
        if math.isnan(w_lo):
            skips.append((s["n"], "eigh anchor not PD"))
            continue
        rows.append(dict(n=s["n"], Nm=Nm,
                         mid=0.5 * (w_lo + w_hi) / s["mu"],
                         pos=(s["mu"] - w_lo) / (w_hi - w_lo),
                         width=(w_hi - w_lo) / s["mu"]))
    mids = np.array([r["mid"] for r in rows])
    poss = np.array([r["pos"] for r in rows])
    wids = np.array([r["width"] for r in rows])
    print("   %d/%d slots (%.0fs): midpoint/mu median %.4f  IQR "
          "[%.4f, %.4f]  max|r-1| %.4f"
          % (len(rows), len(sl), time.time() - t3,
             float(np.median(mids)), float(np.quantile(mids, 0.25)),
             float(np.quantile(mids, 0.75)),
             float(np.max(np.abs(mids - 1)))))
    print("   mass position pos = (mu-w_lo)/(w_hi-w_lo): median "
          "%.4f  IQR [%.4f, %.4f]  range [%.4f, %.4f]"
          % (float(np.median(poss)), float(np.quantile(poss, 0.25)),
             float(np.quantile(poss, 0.75)), float(np.min(poss)),
             float(np.max(poss))))
    print("   corridor width / mu: median %.4f  [%.4f, %.4f]"
          % (float(np.median(wids)), float(np.min(wids)),
             float(np.max(wids))))
    print("   detail (n, N, mid, pos): %s"
          % [(r["n"], r["Nm"], round(r["mid"], 3),
              round(r["pos"], 3)) for r in rows[:12]])
    if skips:
        print("   SKIPPED: %s" % skips)
    # window-0 spot check (pos as a function of the WINDOW)
    sl0 = w0["slots"]
    prev0 = w0["p_sm"].copy()
    poss0 = []
    for j, s in enumerate(sl0):
        if j + 1 < len(sl0):
            m0n0 = sl0[j + 1]["m0"]
        else:
            u_nx = float(core.U_ALL[s["i"] + 1])
            m0n0 = int(np.nonzero(unit_read(w0, u_nx))[0][0])
        Nm0 = min(w0["M"] - 1, m0n0)
        adm0 = [fw for fw in np.geomspace(0.05, 20.0, 81)
                if bd_of(prev0 + fw * s["mu"] * s["cu"],
                         Nm0 - 1) is None]
        if adm0:
            w_a0 = 0.5 * (min(adm0) + max(adm0)) * s["mu"]
            wl0, wh0, _ = edges_anchored(prev0, s["cu"], Nm0, w_a0)
            if not math.isnan(wl0):
                poss0.append((s["mu"] - wl0) / (wh0 - wl0))
        prev0 += s["mu"] * s["cu"]
    poss0 = np.array(poss0)
    print("   window-0 spot check (%d slots): pos median %.4f  IQR "
          "[%.4f, %.4f]  range [%.4f, %.4f]"
          % (len(poss0), float(np.median(poss0)),
             float(np.quantile(poss0, 0.25)),
             float(np.quantile(poss0, 0.75)),
             float(np.min(poss0)), float(np.max(poss0))))
    check("E3a.1 [M] just-in-time corridors on %d/%d slots via the "
          "closed formula: the true mass sits INSIDE every corridor "
          "(window 2 pos in [%.3f, %.3f], median %.3f; window 0 "
          "median %.3f -- the corridor-position law transports "
          "across windows); midpoint median %.4f, max|r-1| %.4f "
          "(benchmarks: S-B C2 0.9947/0.31, S-D K2b ~0.40x)"
          % (len(rows), len(sl), float(np.min(poss)),
             float(np.max(poss)), float(np.median(poss)),
             float(np.median(poss0)), float(np.median(mids)),
             float(np.max(np.abs(mids - 1)))),
          len(rows) == len(sl)
          and bool(np.all(poss > 0) and np.all(poss < 1))
          and bool(np.all(poss0 > 0) and np.all(poss0 < 1)))

    # ---- E3a.2: death-depth horizon (max survival without next atom)
    print("  E3a.2 -- death-depth horizon (last surviving island)")
    rows_d = []
    n_skip = 0
    for j, s in enumerate(sl):
        cap = min(w2["M"] - 1, next_atom_cell(j) + 80)
        best = (0, float("nan"))
        for fw in np.linspace(0.3, 3.0, 41):
            b = bd_of(bgs[j] + fw * s["mu"] * s["cu"], cap)
            sv_ = cap + 1 if b is None else b
            if sv_ > best[0]:
                best = (sv_, fw * s["mu"])
        Nstar, w_a = best
        Nm = min(Nstar, cap)
        w_lo, w_hi, _l = edges_anchored(bgs[j], s["cu"], Nm, w_a)
        if math.isnan(w_lo):
            n_skip += 1
            continue
        m0n = next_atom_cell(j)
        rows_d.append(dict(n=s["n"], Nstar=Nm, over=Nm - m0n,
                           mid=0.5 * (w_lo + w_hi) / s["mu"],
                           pos=(s["mu"] - w_lo) / (w_hi - w_lo)))
    mids_d = np.array([r["mid"] for r in rows_d])
    poss_d = np.array([r["pos"] for r in rows_d])
    n_out = int(np.sum((poss_d < 0) | (poss_d > 1)))
    print("   %d slots (%d anchor-skips): island midpoint/mu median "
          "%.4f  max|r-1| %.4f; mass OUTSIDE the last island on "
          "%d/%d slots; island depth beyond next-slot cell: median "
          "%.0f lags [%.0f, %.0f]"
          % (len(rows_d), n_skip, float(np.median(mids_d)),
             float(np.max(np.abs(mids_d - 1))), n_out, len(rows_d),
             float(np.median([r["over"] for r in rows_d])),
             float(np.min([r["over"] for r in rows_d])),
             float(np.max([r["over"] for r in rows_d]))))
    print("   detail (n, N*, mid, pos): %s"
          % [(r["n"], r["Nstar"], round(r["mid"], 3),
              round(r["pos"], 3)) for r in rows_d[:12]])
    check("E3a.2 [M] death-depth selection measured: the last "
          "surviving island's midpoint has median %.4f, max|r-1| "
          "%.4f; the TRUE mass falls outside the last island on "
          "%d/%d slots -- the death-depth edge does NOT uniquely "
          "select the mass (typed as measured; S-A's varying "
          "downstream death depths, reproduced)"
          % (float(np.median(mids_d)),
             float(np.max(np.abs(mids_d - 1))), n_out, len(rows_d)),
          len(rows_d) >= 30)

    # ---- N-dependence of the edges on 3 sample slots
    for n_t in (5, 23, 101):
        j = n_map[n_t]
        s = sl[j]
        m0n = sl[j + 1]["m0"] if j + 1 < len(sl) else s["m0"] + 40
        Ns = sorted(set(max(s["m0"] + 6, int(f * m0n))
                        for f in (0.5, 0.7, 0.85, 1.0)))
        parts = []
        for Nm in Ns:
            w_a = interior_anchor(bgs[j], s, Nm)
            if math.isnan(w_a):
                parts.append("N=%d: empty" % Nm)
                continue
            wl, wh, _ = edges_anchored(bgs[j], s["cu"], Nm, w_a)
            parts.append("N=%d: [%.4f, %.4f]"
                         % (Nm, wl / s["mu"], wh / s["mu"]))
        print("   n=%3d edge ladder (units of mu): %s"
              % (n_t, "; ".join(parts)))

    # ============================================================= E3b
    print("\nE3b -- full-ladder edges (ALL window atoms true, "
          "target slot free; window 2)")
    ka2 = w2["ka"]
    c_at_all, _tt = core.atom_lags_at(
        w2["alpha"], w2["M"],
        np.array(core.U_ALL[:ka2], float),
        np.array(core.MU_ALL[:ka2], float))
    full = w2["p_sm"] + c_at_all
    bd_full = bd_of(full, w2["M"] - 1)
    check("E3b.0 [E] the FULL ladder (all %d window atoms) is PD to "
          "window end (Levinson breakdown: %s)"
          % (ka2, bd_full), bd_full is None)
    t3b = time.time()
    rows_b = []
    for n_t in E3B_NS:
        j = n_map[n_t]
        s = sl[j]
        rest = full - s["mu"] * s["cu"]
        parts = []
        for fr in E3B_FRACS:
            Nm = int(fr * (w2["M"] - 1))
            wl, wh, lmc = edges_anchored(rest, s["cu"], Nm, s["mu"])
            parts.append((fr, wl / s["mu"], wh / s["mu"], lmc))
        rows_b.append((n_t, parts))
        print("   n=%3d: " % n_t + "  ".join(
            "N=%.2fM: [%.6f, %.6f]" % (fr, wl, wh)
            for (fr, wl, wh, _lm) in parts) + "   (%.0fs)"
            % (time.time() - t3b))
    devs_full = [max(abs(p[-1][1] - 1), abs(p[-1][2] - 1))
                 for (_n, p) in rows_b]
    wid_half = [0.5 * (p[-1][2] - p[-1][1]) for (_n, p) in rows_b]
    mono_ok = all(p[0][1] <= p[-1][1] + 1e-12
                  and p[0][2] >= p[-1][2] - 1e-12
                  for (_n, p) in rows_b)
    check("E3b.1 [M] full-ladder edge at depth 0.98M pins the true "
          "mass: max |edge - mu|/mu = %.2e over %d slots (S-A A2 "
          "reproduction via the CLOSED formula, no Levinson "
          "bisection); halfwidths %.1e..%.1e; corridors shrink "
          "monotonically with depth (binding = deepest): %s; typed "
          "HONESTLY: conditioned on all other true masses -- "
          "boundary positivity, circular as prediction"
          % (float(np.max(devs_full)), len(rows_b),
             float(np.min(wid_half)), float(np.max(wid_half)),
             mono_ok),
          float(np.max(devs_full)) <= 1e-3 and mono_ok)

    # ============================================================== E4
    print("\nE4 -- verdict")
    uniform_ok = float(np.max(np.abs(mids_d - 1))) < 0.01
    id_ok = max(dev_a, dev_b, dev_c, dev_anch) <= BAR_ID
    pin_ok = float(np.max(devs_full)) <= 1e-3
    if id_ok and uniform_ok:
        VERDICT = "G1-EDGE-CLOSED"
    elif id_ok and pin_ok:
        VERDICT = ("EDGE-EXACT-SELECTION-OPEN (edge formula exact "
                   "[E]; full-ladder edge pins mass to %.1e; "
                   "death-depth selection max dev %.3f; jit "
                   "midpoint max dev %.3f; jit corridor position "
                   "median %.3f IQR [%.3f, %.3f])"
                   % (float(np.max(devs_full)),
                      float(np.max(np.abs(mids_d - 1))),
                      float(np.max(np.abs(mids - 1))),
                      float(np.median(poss)),
                      float(np.quantile(poss, 0.25)),
                      float(np.quantile(poss, 0.75))))
    else:
        VERDICT = "EDGE-BROKEN"
    check("E4.1 [M] preregistered classification: %s" % VERDICT,
          id_ok)

    print("\nVERDICT: %s" % VERDICT)
    dt = time.time() - T0
    if FAILS:
        print("RESULT: %d/%d checks passed -- FAILURES: %s  (%.1f s)"
              % (N_CHK - len(FAILS), N_CHK, ", ".join(FAILS), dt))
        return 1
    print("RESULT: ALL %d CHECKS PASSED  (%.1f s)" % (N_CHK, dt))
    return 0


if __name__ == "__main__":
    raise SystemExit(run())
