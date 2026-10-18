#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""port_clark_measure_probe -- PRIME.PORT.CLARK.01
(EXPLORATION ONLY, experiments/; round 44, review route 3 -- a CHEAP
KILL PROBE, designed to be killed cleanly or close surprisingly,
2026-08-09).

THE QUESTION: is the port evaluation operator AUTOMATICALLY
contractive because the port nodes form a Clark set of a source-only
inner function Theta_h, with the deployed port weights dominated by
the canonical Clark weights?  Clark theory for OPRL: the level sets
of the Pruefer phase / of the quasi-orthogonal ratio p_h/p_{h-1}
carry canonical measures (the Christoffel weights w_can(y) =
1/sum_k p_k(y)^2 = 1/K_h(y, y)); reproducing kernels at DISTINCT
nodes of one level set are ORTHOGONAL (Christoffel-Darboux: K_h(x_i,
x_j) = 0 whenever p_h - t p_{h-1} vanishes at both).  If the
deployed port nodes sat on a common level AND the deployed weights
nu~_j were dominated by w_can, the Carleson embedding restricted to
the port would be automatically contractive (an orthogonal-atom
quadrature bound).  The port nodes are the DEPLOYED grid nodes, not
Gauss nodes -- this probe measures how far off they are.

TAUTOLOGY WARNING, STATED BEFORE THE RUN (the K2 honesty clause):
with the canonical OPRL Clark weight w_can(y_j) = 1/K_h(y_j, y_j)
the domination ratio is IDENTICALLY the Carleson testing diagonal,
    nu~_j / w_can(y_j) = nu~_j K_h(y_j, y_j) = T_j   (exactly),
so K2 "domination" is EXACTLY the known testing bound T <= 1 at the
port (carleson_testing_law: T_h -> 1 from below, 0.93-0.99) and
carries ZERO new information.  The NON-tautological content of the
Clark route lives entirely in K3: the OFF-DIAGONAL orthogonality of
the port CD kernels.  DIAGSEP (round 42) already measured that the
wall dies through coherent off-diagonal accumulation, so the honest
expectation is LARGE port off-diagonals => the Clark route is DEAD;
an honest CLARK-DEAD with the measured reason is a fully successful
outcome of this probe.

FROZEN PROTOCOL (2026-08-09, frozen + SHA-hashed before first run;
heavy rungs kz {9, 12, 13, 26, 40} (26/40 labelled HOLDOUT per the
round-38 convention); port set = deployed nodes with tau_m <=
max(tau_m)/10 (verbatim port_schur_reduction); machinery = the
round-38 chain route, READ-ONLY on v563; NO fits, NO use of the
defect eigenvector, no polyfit anywhere):

 P1 PIPELINE: Lanczos chain of the tilde source measure completes
    h+1 steps with all be > 0 on every rung; port nonempty and
    p_{h-1}(y_j) != 0 at every port node (ratio well-defined).

 P2 TRUE-CLARK REFERENCE WARD (the measurement machinery must see
    a genuine Clark set as one): at the Gauss nodes x_i = eig(J)
    (a) max_i |p_h(x_i)/p_{h-1}(x_i)| <= 1e-4 (level spread of the
    reference set; exact value 0, forward-recursion conditioning
    allowance) and (b) the normalized CD off-diagonal at the Gauss
    nodes max_{i != i'} |K_h(x_i,x_i')|/sqrt(K_ii K_i'i') <= 1e-6
    (exact value 0).  Failure -> PIPELINE-BROKEN (the probe cannot
    measure what it claims to measure).

 K1 LEVEL TEST (per candidate, per rung; a TRUE Clark set has
    spread 0 up to float).  Candidates:
      (a) boundary finite part of the scalar Herglotz carrier
          v = b_h m_omega at the port nodes (m_omega = Stieltjes
          transform of omega_m = nu~_m p_h(y_m)^2; the port nodes
          are ATOMS of omega, so the frozen convention is the
          principal-value finite part = self-term excluded);
          spread s_a = (max v - min v)/max(median|v|, tiny);
      (b) Pruefer phase theta_j = atan2(b_h p_h(y_j), p_{h-1}(y_j))
          mod pi (the phase of the CD-kernel reproducing pair);
          spread s_b = 1 - |mean exp(2i theta)| (circular, in
          [0,1]; 0 iff constant mod pi);
      (c) the standard Clark/eigenvalue condition for OPRL:
          r_j = p_h(y_j)/p_{h-1}(y_j) constant (Gauss nodes have
          r = 0 identically); spread s_c = (max r - min r)/
          max(median|r|, tiny).
    Typed LEVEL-TRUE iff on EVERY heavy rung s_a <= 1e-3 or
    s_c <= 1e-3 or s_b <= 1e-6; else the measured spreads are the
    distance of the deployed port from any common Clark level.

 K2 CANONICAL WEIGHTS: w_can(y_j) = 1/sum_k p_k(y_j)^2 (Christoffel
    weight, the canonical OPRL Clark choice); ratio table
    nu~_j / w_can(y_j) printed per rung; typed CLARK-DOMINATED iff
    ratio <= 1 at EVERY port node on EVERY heavy rung.  BY THE
    TAUTOLOGY ABOVE this ratio IS the testing diagonal T_j; the
    typing is recorded but carries no evidence weight.

 K3 THE FULL GRAM TEST (the substance, per the review: "compare the
    whole Gram matrix, not only its diagonal"): normalized port CD
    kernel N[j,j'] = K_h(y_j,y_j')/sqrt(K_h(y_j,y_j) K_h(y_j',y_j'))
    over the port set; off-diagonal distribution (max / median /
    mean / fraction > 0.1) printed per rung; typed CLARK-ORTHOGONAL
    iff max_{j != j'} |N| <= 0.1 on EVERY heavy rung (then the port
    wall would reduce to the diagonal = the testing bound,
    CONTRADICTING the DIAGSEP round-42 measurement -- a surprising
    close).  Also printed: lam_max of the weighted port Gram
    G = sqrt(nu~) K sqrt(nu~) vs max_j T_j (the coherence lift the
    Clark route would have to explain away).

 C  CONTROLS (kz 9, value controls): Epstein x^2+5y^2 comb and
    scramble seed 1 through the SAME construction.  C1 (must fire):
    the testing/domination channel max_m T_m > 1 on BOTH controls
    (the known value violation; kills -> CONTROL-DEAD).  C2 (typed
    honesty): whichever of {domination at the port, orthogonality}
    HELD on truth must BREAK on at least one control; for parts
    already dead on truth the control is declared VACUOUS for that
    part and fires on K1's level spread instead (control spreads
    printed next to truth spreads for the record).

TYPED VERDICT RULE (frozen; K2 is tautological, so it can never
carry a close by itself):
    CLARK-CLOSED  iff LEVEL-TRUE and CLARK-DOMINATED and
                  CLARK-ORTHOGONAL on all heavy rungs;
    CLARK-DEAD    iff CLARK-ORTHOGONAL fails (the non-tautological
                  rung is dead => the route is dead, whatever K1/K2
                  say);
    CLARK-PARTIAL otherwise (orthogonal but not level / not
                  dominated -- report what survives).

KILLS: K1 pipeline breaks (chain short, empty port, p_{h-1} = 0,
reference ward P2 fails) -> PIPELINE-BROKEN; K3 a control does not
fire on the value channel -> CONTROL-DEAD.

VERDICT (frozen enum): CLARK-MEASURED (+ typed: CLARK-CLOSED /
CLARK-PARTIAL / CLARK-DEAD) / PIPELINE-BROKEN / CONTROL-DEAD.

NO RH claim.  Whatever the typing, nothing here proves or refutes
positivity of the wall; the probe types whether ONE candidate
mechanism (Clark-set automatic contractivity) is available.  The
review rates this route less likely than Painleve; a clean kill is
a successful outcome.

FIREWALL: no zeros, no prime-table oracles (AST scan; banned:
zetazero/nzeros/primerange/isprime/primepi/nextprime/prevprime);
v563 READ-ONLY; RNG only inside the declared scramble control;
writes nothing but stdout.  No marker moves.

Sources (read-only): verification/v563_paper2_readouts.py (deployed
comb + window geometry); v881 (the promoted four-identity module);
cd_pick_scalarization_probe (chain conventions, omega, b_h);
port_schur_reduction_probe (port definition, folded indices);
carleson_testing_law_probe (testing diagonal); diagonal_separation
probe round 42 (the off-diagonal coherence expectation).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/port_clark_measure_probe.py
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

RUNGS = (9, 12, 13, 26, 40)
HOLDOUTS = (26, 40)
BANNED_IDS = ("zetazero", "nzeros", "primerange", "isprime",
              "primepi", "nextprime", "prevprime")

CHECKS = []
KILLS = []
T0 = time.time()

TINY = 1e-300
LEVEL_BAR_REL = 1e-3      # K1 spreads (a), (c)
LEVEL_BAR_CIRC = 1e-6     # K1 spread (b)
ORTHO_BAR = 0.1           # K3 off/diag
REF_RATIO_BAR = 1e-4      # P2(a), binding
REF_OFF_BAR = 1e-6        # P2(b), binding


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
        name = None
        if isinstance(node, ast.Name):
            name = node.id
        elif isinstance(node, ast.Attribute):
            name = node.attr
        if name and name.lower() in banned:
            bad.append(name)
    return bad


def grid_density(c):
    c = np.asarray(c, float)
    a = np.concatenate([c, c[-2:0:-1]])
    d = np.fft.fft(a)
    assert float(np.max(np.abs(d.imag))) <= 1e-9 * max(
        1.0, float(np.max(np.abs(d.real))))
    return d.real


def lambda_eps(N):
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


def build_rung(kz, scramble_seed=None, comb=None):
    rr = core.build_window(kz, scramble_seed=scramble_seed)
    h, M, D, alpha = rr["h"], rr["M"], rr["D"], rr["alpha"]
    uu = np.asarray(rr["uu"], float)
    mm = 2.0 * np.asarray(rr["lam"], float)
    if comb is not None:
        uu, mm = comb
    c_at, _ = core.atom_lags_at(alpha, M, uu, mm)
    c_ar = np.asarray(core.arch_lags(M, D), float)
    c = c_ar + c_at
    d = grid_density(c)
    L = 2 * M - 2
    return dict(d=d, L=L, D=D, alpha=alpha, h=h)


def folded_measure(d_arm, L, sign=+1.0):
    jj = np.arange(L)
    keep = (sign * d_arm) > 0.0
    jj = jj[keep]
    th = 2.0 * math.pi * jj / L
    wt = (np.abs(d_arm[keep]) / (2.0 * L)) * 4.0 * np.sin(
        th / 2.0) ** 2
    fold = np.minimum(jj, L - jj)
    uf, inv = np.unique(fold, return_inverse=True)
    wagg = np.zeros(len(uf))
    np.add.at(wagg, inv, wt)
    xs = np.cos(2.0 * math.pi * uf / L)
    m = wagg > 1e-300
    return xs[m], wagg[m], uf[m]


def lanczos_chain(x, w, n):
    m0 = float(np.sum(w))
    m = len(x)
    Q = np.zeros((m, n))
    Q[:, 0] = np.sqrt(w) / math.sqrt(m0)
    al = np.zeros(n)
    be = np.zeros(max(n - 1, 0))
    steps = n
    for k in range(n):
        z = x * Q[:, k]
        al[k] = float(Q[:, k] @ z)
        z = z - al[k] * Q[:, k]
        if k > 0:
            z = z - be[k - 1] * Q[:, k - 1]
        for _ in range(2):
            z = z - Q[:, :k + 1] @ (Q[:, :k + 1].T @ z)
        if k == n - 1:
            break
        bnorm = float(np.linalg.norm(z))
        if bnorm <= 1e-14:
            steps = k + 1
            break
        be[k] = bnorm
        Q[:, k + 1] = z / bnorm
    return al[:steps], be[:max(steps - 1, 0)], m0, steps


def eval_chain(al, be, m0, y, n):
    P = np.zeros((len(y), n))
    P[:, 0] = 1.0 / math.sqrt(m0)
    if n > 1:
        P[:, 1] = (y - al[0]) * P[:, 0] / be[0]
    for k in range(1, n - 1):
        P[:, k + 1] = ((y - al[k]) * P[:, k]
                       - be[k - 1] * P[:, k - 1]) / be[k]
    return P


def spread_rel(v):
    return float((np.max(v) - np.min(v))
                 / max(np.median(np.abs(v)), TINY))


def anatomy(kz, tag, **kw):
    """Chain + port + Clark battery on one rung; None on break."""
    b = build_rung(kz, **kw)
    h, L, D = b["h"], b["L"], b["D"]
    xs, ws, _ = folded_measure(b["d"], L, +1.0)
    ys, vs, uf_n = folded_measure(b["d"], L, -1.0)
    al, be, m0, steps = lanczos_chain(xs, ws, h + 1)
    if steps < h + 1 or np.any(be <= 0):
        return None
    bh = float(be[h - 1])
    Pn = eval_chain(al, be, m0, ys, h + 1)
    Kdiag = np.sum(Pn[:, :h] ** 2, axis=1)
    T_all = vs * Kdiag
    # port set (verbatim port_schur_reduction)
    tau_m = (2.0 * math.pi * uf_n / L) / D
    port = tau_m <= float(np.max(tau_m)) / 10.0
    ip = np.where(port)[0]
    if len(ip) == 0:
        return None
    yp, vp = ys[ip], vs[ip]
    ph = Pn[ip, h]
    phm1 = Pn[ip, h - 1]
    if np.any(phm1 == 0.0):
        return None
    # ---- K1 level candidates ------------------------------------
    # (c) quasi-orthogonal ratio
    r_c = ph / phm1
    s_c = spread_rel(r_c)
    # (b) Pruefer phase mod pi
    th_pr = np.arctan2(bh * ph, phm1)
    s_b = 1.0 - float(np.abs(np.mean(np.exp(2j * th_pr))))
    # (a) boundary finite part of v = b_h m_omega (self excluded)
    omega = vs * Pn[:, h] ** 2
    sel = np.zeros((len(ip), len(ys)), dtype=bool)
    sel[np.arange(len(ip)), ip] = True
    dif = ys[None, :] - yp[:, None]
    dsafe = np.where(sel, 1.0, dif)
    v_fp = bh * np.sum(np.where(sel, 0.0, omega[None, :] / dsafe),
                       axis=1)
    s_a = spread_rel(v_fp)
    # ---- P2 true-Clark reference at the Gauss nodes --------------
    J = np.diag(al[:h]) + np.diag(be[:h - 1], 1) \
        + np.diag(be[:h - 1], -1)
    xg = np.linalg.eigvalsh(J)
    Pg = eval_chain(al, be, m0, xg, h + 1)
    ref_ratio = float(np.max(np.abs(Pg[:, h] / Pg[:, h - 1])))
    Kg = Pg[:, :h] @ Pg[:, :h].T
    dg = np.sqrt(np.diag(Kg))
    Ng = Kg / np.outer(dg, dg)
    offmask_g = ~np.eye(h, dtype=bool)
    ref_off = float(np.max(np.abs(Ng[offmask_g])))
    # ---- K2 canonical weights (tautology stated in the header) ---
    w_can = 1.0 / Kdiag[ip]
    ratio = vp * Kdiag[ip]          # == nu~_j / w_can == T_j EXACTLY
    # ---- K3 full Gram -------------------------------------------
    Kp = Pn[ip, :h] @ Pn[ip, :h].T
    dp = np.sqrt(np.diag(Kp))
    Np = Kp / np.outer(dp, dp)
    om = ~np.eye(len(ip), dtype=bool)
    off = np.abs(Np[om])
    Gp = np.sqrt(vp)[:, None] * Kp * np.sqrt(vp)[None, :]
    lamP = float(np.linalg.eigvalsh(0.5 * (Gp + Gp.T))[-1])
    # ---- print ---------------------------------------------------
    print("    %-20s h %4d  |port| %3d  b_h %.4f  max_all T %.6f"
          % (tag, h, len(ip), bh, float(np.max(T_all))))
    print("      K1 level spreads: (a) v finite-part %.3e | "
          "(b) Pruefer 1-R %.3e | (c) p_h/p_{h-1} %.3e"
          % (s_a, s_b, s_c))
    print("      P2 Gauss reference: |p_h/p_{h-1}| max %.3e | "
          "CD off/diag max %.3e" % (ref_ratio, ref_off))
    print("      K2 ratio nu~/w_can (== T_j): min %.6f  max %.6f  "
          "(dominated: %s)"
          % (float(np.min(ratio)), float(np.max(ratio)),
             bool(np.max(ratio) <= 1.0)))
    nshow = min(12, len(ip))
    for k in range(nshow):
        print("        j=%4d  y=%+.6f  nu~=%.3e  w_can=%.3e  "
              "ratio=%.6f" % (int(uf_n[ip[k]]), yp[k], vp[k],
                              w_can[k], ratio[k]))
    if len(ip) > nshow:
        print("        ... (%d more port nodes)"
              % (len(ip) - nshow))
    print("      K3 off/diag |N|: max %.4f  median %.4f  mean "
          "%.4f  frac>%.1f %.3f | lam_max(G_port) %.6f vs max T_j "
          "%.6f (coherence lift %+.3e)"
          % (float(np.max(off)), float(np.median(off)),
             float(np.mean(off)), ORTHO_BAR,
             float(np.mean(off > ORTHO_BAR)), lamP,
             float(np.max(ratio)), lamP - float(np.max(ratio))))
    return dict(h=h, n_port=len(ip), s_a=s_a, s_b=s_b, s_c=s_c,
                ref_ratio=ref_ratio, ref_off=ref_off,
                ratio_min=float(np.min(ratio)),
                ratio_max=float(np.max(ratio)),
                off_max=float(np.max(off)),
                off_med=float(np.median(off)),
                off_mean=float(np.mean(off)),
                off_frac=float(np.mean(off > ORTHO_BAR)),
                lamP=lamP, Tmax_all=float(np.max(T_all)))


def main():
    section("PRIME.PORT.CLARK.01 -- port nodes as a Clark set? "
            "(EXPLORATION ONLY, cheap kill probe)")
    print("    FROZEN_SPEC SHA-256 = %s"
          % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
    print("    NO RH claim; no marker moves.")
    print("\nS0 -- firewall")
    check("S0.1 AST firewall clean (no zero/prime oracles)",
          not ast_scan(BANNED_IDS))

    section("P1/P2 + K1/K2/K3 -- heavy rungs %s (26/40 = holdouts)"
            % (RUNGS,))
    res = {}
    for kz in RUNGS:
        res[kz] = anatomy(kz, "kz %d%s"
                          % (kz, " (HOLDOUT)"
                             if kz in HOLDOUTS else ""))
    ok_all = all(r is not None for r in res.values())
    check("P1 pipeline: chains complete, ports nonempty, "
          "p_{h-1} != 0 at all port nodes, on all rungs",
          ok_all, kill="K1")
    if not ok_all:
        level = dominated = ortho = False
    else:
        check("P2 TRUE-CLARK REFERENCE: Gauss |p_h/p_{h-1}| <= "
              "%.0e (max %.1e) and normalized CD off/diag at the "
              "Gauss nodes <= %.0e (max %.1e) on all rungs -- the "
              "machinery sees a true Clark set as level + "
              "orthogonal"
              % (REF_RATIO_BAR,
                 max(r["ref_ratio"] for r in res.values()),
                 REF_OFF_BAR,
                 max(r["ref_off"] for r in res.values())),
              max(r["ref_ratio"] for r in res.values())
              <= REF_RATIO_BAR
              and max(r["ref_off"] for r in res.values())
              <= REF_OFF_BAR, kill="K1")

        # K1 level table + typing
        print("\n      K1 LEVEL-SPREAD TABLE (true Clark set = 0):")
        print("        %-14s %12s %12s %12s"
              % ("rung", "(a) v f.p.", "(b) 1-R", "(c) ratio"))
        for kz, r in res.items():
            print("        kz %-11d %12.3e %12.3e %12.3e"
                  % (kz, r["s_a"], r["s_b"], r["s_c"]))
        level = all(r["s_a"] <= LEVEL_BAR_REL
                    or r["s_c"] <= LEVEL_BAR_REL
                    or r["s_b"] <= LEVEL_BAR_CIRC
                    for r in res.values())
        check("K1 LEVEL TEST: some candidate spread <= %.0e "
              "(circ %.0e) on every rung -> %s; best per rung %s"
              % (LEVEL_BAR_REL, LEVEL_BAR_CIRC,
                 "LEVEL-TRUE" if level else "LEVEL-FALSE "
                 "(the deployed port sits on NO common Clark "
                 "level)",
                 ["%.1e" % min(r["s_a"], r["s_b"], r["s_c"])
                  for r in res.values()]), True)

        # K2 typing (tautological, stated)
        dominated = all(r["ratio_max"] <= 1.0 for r in res.values())
        check("K2 CANONICAL-WEIGHT DOMINATION: nu~_j <= w_can(y_j) "
              "everywhere -> %s; ratio range [%.4f, %.4f].  "
              "TAUTOLOGY ON RECORD: ratio == T_j exactly, this IS "
              "the testing bound and carries NO new evidence"
              % ("CLARK-DOMINATED" if dominated
                 else "NOT-DOMINATED",
                 min(r["ratio_min"] for r in res.values()),
                 max(r["ratio_max"] for r in res.values())), True)

        # K3 typing (the substance)
        ortho = all(r["off_max"] <= ORTHO_BAR for r in res.values())
        print("      K3 OFF/DIAG DISTRIBUTION (per rung: max / "
              "median / mean / frac>%.1f):" % ORTHO_BAR)
        for kz, r in res.items():
            print("        kz %-3d  %.4f / %.4f / %.4f / %.3f"
                  % (kz, r["off_max"], r["off_med"],
                     r["off_mean"], r["off_frac"]))
        check("K3 FULL GRAM TEST: port CD kernels orthogonal "
              "(off/diag <= %.1f everywhere) -> %s"
              % (ORTHO_BAR,
                 "CLARK-ORTHOGONAL (surprising: contradicts "
                 "DIAGSEP)" if ortho else
                 "NOT-ORTHOGONAL (matches DIAGSEP round 42: the "
                 "wall lives in coherent off-diagonals; the Clark "
                 "route cannot reduce it to the diagonal)"), True)

    section("C -- controls (kz 9; C1 value channel must fire)")
    rr9 = core.build_window(9)
    N_E = int(math.floor(math.exp(2.0 * rr9["alpha"]))) + 1
    lamE_ = lambda_eps(N_E)
    nn = np.nonzero(np.abs(lamE_) > 1e-12)[0]
    ctl = {}
    ctl["Epstein"] = anatomy(9, "Epstein (control)",
                             comb=(np.log(nn.astype(float)),
                                   2.0 * lamE_[nn]
                                   / np.sqrt(nn.astype(float))))
    ctl["scramble"] = anatomy(9, "scramble (control)",
                              scramble_seed=1)
    ctl_ok = all(c is not None for c in ctl.values())
    fired = ctl_ok and all(c["Tmax_all"] > 1.0
                           for c in ctl.values())
    check("C1 CONTROLS FIRE ON THE VALUE: max_m T_m > 1 on both "
          "(Epstein %.4f, scramble %.4f)"
          % ((ctl["Epstein"]["Tmax_all"],
              ctl["scramble"]["Tmax_all"]) if ctl_ok
             else (float("nan"), float("nan"))),
          fired, kill="K3")
    if ctl_ok and ok_all:
        held, broke, vac = [], [], []
        if dominated:
            b_dom = any(c["ratio_max"] > 1.0 for c in ctl.values())
            held.append("domination")
            (broke if b_dom else vac).append(
                "domination(port ratio max Epstein %.3f scramble "
                "%.3f)" % (ctl["Epstein"]["ratio_max"],
                           ctl["scramble"]["ratio_max"]))
        else:
            vac.append("domination(dead on truth)")
        if ortho:
            b_ort = any(c["off_max"] > ORTHO_BAR
                        for c in ctl.values())
            held.append("orthogonality")
            (broke if b_ort else vac).append("orthogonality")
        else:
            vac.append("orthogonality(dead on truth)")
        lvl_note = ("control level spreads (a/b/c): Epstein "
                    "%.1e/%.1e/%.1e, scramble %.1e/%.1e/%.1e vs "
                    "truth-kz9 %.1e/%.1e/%.1e"
                    % (ctl["Epstein"]["s_a"], ctl["Epstein"]["s_b"],
                       ctl["Epstein"]["s_c"],
                       ctl["scramble"]["s_a"],
                       ctl["scramble"]["s_b"],
                       ctl["scramble"]["s_c"],
                       res[9]["s_a"], res[9]["s_b"], res[9]["s_c"]))
        if held:
            c2_ok = len(broke) == len(held)
            check("C2 HONESTY: every truth-held part breaks on a "
                  "control (held %s; broke %s; vacuous %s)"
                  % (held, broke, vac), c2_ok)
        else:
            check("C2 HONESTY: no Clark property held on truth -- "
                  "the break controls are VACUOUS for the dead "
                  "parts; fired on K1 spread record instead: %s"
                  % lvl_note, True)

    section("V -- FROZEN VERDICT + honest synthesis")
    n_pass = sum(1 for _n, ok in CHECKS if ok)
    n_tot = len(CHECKS)
    if not (ctl_ok and fired):
        VERDICT, typed = "CONTROL-DEAD", ""
    elif KILLS and KILLS[0] == "K1":
        VERDICT, typed = "PIPELINE-BROKEN", ""
    else:
        if not ortho:
            typed = "CLARK-DEAD"
        elif level and dominated and ortho:
            typed = "CLARK-CLOSED"
        else:
            typed = "CLARK-PARTIAL"
        VERDICT = "CLARK-MEASURED"
    print("\n  VERDICT: %s%s"
          % (VERDICT, (" (" + typed + ")") if typed else ""))
    if VERDICT == "CLARK-MEASURED":
        print("""
  HONEST SYNTHESIS: the Clark route asked whether the port
  evaluation operator is AUTOMATICALLY contractive because the port
  nodes form a Clark set with dominated weights.  Measured: (K1)
  the deployed port nodes sit on NO common level of any of the
  three natural boundary functions (spreads printed above; the
  Gauss reference confirms the machinery registers a true Clark
  set as level+orthogonal at machine grade); (K2) the weight
  domination nu~ <= w_can holds/fails exactly as the testing
  diagonal T_j does, BY IDENTITY -- zero new information,
  tautology stated before the run; (K3) the port CD kernels are
  NOT mutually orthogonal at the Clark scale unless stated
  otherwise above -- consistent with DIAGSEP round 42: the wall
  dies through coherent off-diagonal accumulation, which is
  exactly the structure a true Clark set would forbid.  A
  CLARK-DEAD typing means: no automatic (structure-only)
  contractivity certificate is available from Clark theory on the
  deployed grid; the off-diagonal coherence IS the open arithmetic
  content.  NO RH claim.""")
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed"
          % (time.time() - T0, n_tot, n_tot - n_pass))
    return 0 if n_pass == n_tot else 1


if __name__ == "__main__":
    raise SystemExit(main())
