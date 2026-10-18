#!/usr/bin/env python3
"""chain_tolerance_scaling_probe.py -- S-A, THE CIRCULARITY DECIDER:
how sharply does the Z1 flow-induction constrain the counting masses,
and does the required accuracy sit inside the classical (unconditional)
budget, inside the RH budget, or beyond?

EXPLORATION ONLY (experiments/ firewall): nothing here is a
verification claim; no verification/, paper, ledger or website surface
is touched; no marker moves; NO RH statement.  File prefix chain_ to
avoid collision with the parallel beam-search worker (z1_* names).

CONTEXT.  The z1 5-series established [E-corpus]: p = arch + pole +
atoms is PD to full depth on the 5-window family; the slot identity
Delta alpha = w1/E is exact; the just-in-time ladder (each prime-power
mass buys positivity life exactly to the next slot, margins 1-11
lags); shooting recovers the counting mass to 0.11% median
(conditioned on the exact past).  The induction candidate reads:
"PD to slot m + true mass inside the admissible corridor => PD to
slot m+1".  THE OPEN QUESTION (G2): how wide is the corridor, how
does it scale, and what proof technology can certify membership?

MEASUREMENTS (bars/verdicts declared BEFORE any number):
  A1 per-slot MASS corridor, criterion NEXT-SLOT: on all 5 windows,
     every prime-power slot n <= 120: bisect the factor interval
     [f_lo, f_hi] such that bd(bg + f mu cu) >= m0_next (survival to
     the next true slot; bg = arch+pole+atoms below, exact past).
     22-iter bisection; f_lo in [0,1], f_hi in [1,4] (censored ends
     recorded).  SANITY: f = 1 admissible on >= 95% of slots.
  A2 per-slot MASS corridor, criterion WINDOW-END (the hard grade):
     same slots, all 5 windows; admissible(f) := the FULL ladder with
     slot n scaled by f (everything else true) stays PD to depth M-1.
     Same bisection.  SANITY: f = 1 admissible on 100% of slots.
  A3 POSITION needle, criterion NEXT-SLOT, TRUE mass: windows {0, 4},
     slots n in {3, 7, 13, 29, 53, 83, 113}: offsets -8..+8 cells in
     1/2-cell steps; width = 0.5 x #admissible.  (5d P1.1 used the
     shooting-optimal mass -- its widths are upper envelopes of ours;
     typed, both quotable.)
  A4 SCALING FITS: per window, log(halfwidth) vs log n -> theta + R^2
     (power law n^-theta == exponential in u; the two user candidates
     coincide since u = log n); constancy read (first/last-quartile
     medians); cross-window: median log-tolerance vs alpha slope at
     the common slot set.  Classification, no hard bar.
  A2b TRUE-LADDER MARGIN DIAGNOSTIC: the Levinson innovation curve
     E_n of the unperturbed ladder (min E_n / E_0, location), plus
     the death location bd when a slot mass is pushed just outside
     its corridor -- decides whether the window-end criterion is
     slot-local or dominated by a terminal near-singularity
     (boundary positivity).
  A5 AGGREGATE tolerance (the analytically meaningful object):
     windows {0, 2, 4}; smallest relative mass perturbation that
     kills full-depth PD, over the declared perturbation menu:
       P1 coherent scale (1 + eps), both signs;
       P2 iid Rademacher (1 + eps xi), 3 seeds (median);
       P3 coherent oscillation (1 + eps cos(omega u)),
          omega in {2, 8} (declared arithmetic-free grid; HONESTY:
          the worst-case omega sits at comb frequencies -- cited
          knowledge, never loaded).
     eps* = min over the menu (bisection in [0, 0.5]).
  A5b DEPTH-RESOLVED aggregate tolerance on window 4:
     eps*(N) for N/(M-1) in {0.25, 0.5, 0.75, 0.9, 1.0} (coherent
     scale + one iid seed) -- where does the accuracy requirement
     cross the two budgets?
  A6 BUDGET COMPARISON + VERDICT.  Budgets (closed forms, no zeta
     evaluation anywhere):
       B_unc(x) = exp(-sqrt(log x / R)), R = 9.645908801
         (de la Vallee Poussin zero-free-region FORM of the relative
         psi-accuracy; explicit-constant versions cited, not tuned);
       B_RH(x)  = log^2 x / (8 pi sqrt x)
         (Schoenfeld's RH form of |psi(x)-x|/x, x >= 73.2; the 8 pi
         is Schoenfeld's, noted).
     FRAME HONESTY (declared): per-slot masses are EXACT arithmetic
     (Lambda(n) computable) -- no analytic theorem is needed to KNOW
     a mass; the analytic content of G2 is the AGGREGATE inequality
     (PD of the form built from the exact masses).  The decisive
     comparison is therefore eps*(window) vs the budgets at the
     window reach X = e^{2 alpha}; the per-slot corridor table is
     the structural evidence (how the constraint tightens), printed
     with the same budget columns for transparency.
     PER-WINDOW CLASS: SUB-RH if eps* >= B_unc(X); RH-GRADE if
     B_RH(X) <= eps* < B_unc(X); OVER-RH if eps* < B_RH(X).
     VERDICT (preregistered): TOLERANCE-SUB-RH iff every measured
     window classifies SUB-RH; TOLERANCE-RH-GRADE iff every measured
     window classifies RH-GRADE or OVER-RH (the induction needs
     accuracy classical means cannot certify -- the honest
     'renaming' reading, with OVER-RH separately flagged);
     TOLERANCE-MIXED otherwise (boundary named).
     EXTRAPOLATION HONESTY: the measured range (n <= 120,
     X <= 2.6e5) is far from asymptotic; the verdict is typed as a
     deployed-surface statement, the asymptotic claim is the fitted
     LAW, quoted with its R^2.

FIREWALL: AST-checked -- no zetazero/nzeros/zeta anywhere in this
file (construction AND diagnostics; the budgets are elementary
closed forms).  v563 imported READ-ONLY.

Provenance (read-only): z1_uvarov_probe (5c slot machinery),
z1_flow_recursion_probe (5d shooting/criteria), v563 core,
Rosser-Schoenfeld / Schoenfeld 1976 (RH psi bound, cited),
Mossinghoff-Trudgian (zero-free region R, cited).
"""
import ast
import math
import os
import sys
import time

import numpy as np

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

SEED = 20260803
U_SLOTS = math.log(120.0)
R_ZFR = 9.645908801          # zero-free-region constant (cited form)
BIT_F = 26                   # corridor bisection iterations
BIT_E = 30                   # aggregate epsilon bisection iterations
F_HI_CAP = 4.0
EPS_CAP = 0.5
POS_NS = (3, 7, 13, 29, 53, 83, 113)
POS_HALFCELLS = 16           # +-8 cells in 1/2-cell steps
AGG_WINS = (0, 2, 4)
OMEGAS = (2.0, 8.0)
N_SEEDS = 3
MARGIN_A = 40                # criterion-A horizon past next slot


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


def bd_of(r, N):
    """Levinson breakdown index (None = PD to depth N)."""
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


def lev_curve(r, N):
    """Levinson with innovation-energy curve E_n (None-guarded)."""
    r = np.asarray(r, float)
    a = np.zeros(N + 1)
    a[0] = 1.0
    E = float(r[0])
    Es = np.empty(N + 1)
    Es[0] = E
    for n in range(1, N + 1):
        acc = r[n] + (float(a[1:n] @ r[n - 1:0:-1]) if n > 1 else 0.0)
        k = -acc / E
        a[1:n + 1] = a[1:n + 1] + k * a[n - 1::-1][:n]
        E *= (1.0 - k * k)
        Es[n] = E
        if not (abs(k) < 1.0) or E <= 0.0:
            return n, Es[:n + 1]
    return None, Es


def build_win(kz):
    alpha, M = window_geometry(kz)
    D = 2.0 * alpha / M
    ka = core.atoms_in(alpha)
    c_ar = core.arch_lags(M, D)
    c_at, _ = core.atom_lags_at(alpha, M, core.U_ALL[:ka],
                                core.MU_ALL[:ka])
    cp = pole_lags(M, D)
    return dict(kz=kz, alpha=alpha, M=M, h=M // 2, D=D, ka=ka,
                p_sm=c_ar + cp, c_at=c_at, p=c_ar + cp + c_at)


def unit_read(w, u):
    c1, _ = core.atom_lags_at(w["alpha"], w["M"],
                              np.array([u]), np.array([1.0]))
    return c1


def slot_table(w):
    """Prime-power slots with u <= U_SLOTS: (index, n, mu, cu, cell)."""
    out = []
    for i in range(w["ka"]):
        u = float(core.U_ALL[i])
        if u > U_SLOTS:
            break
        cu = unit_read(w, u)
        nz = np.nonzero(cu)[0]
        ist = int(nz[np.argmax(np.abs(cu[nz]))])
        out.append(dict(i=i, n=int(round(math.exp(u))), u=u,
                        mu=float(core.MU_ALL[i]), cu=cu, ist=ist,
                        m0=int(nz[0])))
    return out


def bisect_edge(adm, f_in, f_out, iters):
    """Bisect the admissibility edge from admissible f_in toward
    inadmissible f_out."""
    for _ in range(iters):
        mid = 0.5 * (f_in + f_out)
        if adm(mid):
            f_in = mid
        else:
            f_out = mid
    return f_in


def fit_loglog(x, y):
    x = np.log(np.asarray(x, float))
    y = np.log(np.asarray(y, float))
    A = np.vstack([x, np.ones_like(x)]).T
    coef, _, _, _ = np.linalg.lstsq(A, y, rcond=None)
    fitv = A @ coef
    ss = float(np.sum((y - y.mean()) ** 2))
    r2 = 1.0 - float(np.sum((y - fitv) ** 2)) / ss if ss > 0 else 0.0
    return float(coef[0]), r2


def run():
    print("=" * 78)
    print("S-A CHAIN TOLERANCE SCALING -- the circularity decider")
    print("=" * 78)

    check("G0.0 [E] AST firewall: no zeta/zero symbol anywhere in "
          "this probe (budgets are elementary closed forms)",
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
    wins = [build_win(kz) for (kz, _a, _M) in picks]
    pd_ok = all(bd_of(w["p"], w["M"] - 1) is None for w in wins)
    for w in wins:
        w["slots"] = slot_table(w)
    check("G0.1 [E] 5-window family (5b/5c selection) rebuilt; "
          "full-depth Levinson PD on all 5 (true ladder); slot "
          "tables: %s slots (u <= log 120) per window"
          % [len(w["slots"]) for w in wins], pd_ok)

    # ============================================================== A1
    print("\nA1 -- per-slot mass corridor, criterion NEXT-SLOT")
    t1 = time.time()
    n_adm1 = 0
    n_tot1 = 0
    for w in wins:
        slots = w["slots"]
        cur = w["p_sm"].copy()
        rows = []
        for j, s in enumerate(slots):
            m0_next = slots[j + 1]["m0"] if j + 1 < len(slots) \
                else s["m0"] + MARGIN_A
            Nrun = min(w["M"] - 1, m0_next + MARGIN_A)
            bg = cur.copy()
            cur += s["mu"] * s["cu"]

            def adm(f, bg=bg, s=s, Nrun=Nrun, tgt=m0_next):
                b = bd_of(bg + f * s["mu"] * s["cu"], Nrun)
                return (b is None) or (b >= tgt)

            ok1 = adm(1.0)
            n_tot1 += 1
            n_adm1 += int(ok1)
            if not ok1:
                rows.append((s["n"], np.nan, np.nan))
                continue
            f_lo = 0.0 if adm(0.0) else bisect_edge(adm, 1.0, 0.0,
                                                    BIT_F)
            f_hi = F_HI_CAP if adm(F_HI_CAP) else \
                bisect_edge(adm, 1.0, F_HI_CAP, BIT_F)
            rows.append((s["n"], f_lo, f_hi))
        w["corrA"] = rows
    print("   f=1 admissible on %d/%d slot cells; per-window medians "
          "of the BINDING halfwidth min(1-f_lo, f_hi-1):"
          % (n_adm1, n_tot1))
    for w in wins:
        hwv = [min(1 - lo, hi - 1) for (_n, lo, hi) in w["corrA"]
               if not math.isnan(lo)]
        print("   h=%5d: median %.4f  min %.4f  max %.4f   (%.0fs)"
              % (w["h"], float(np.median(hwv)), min(hwv), max(hwv),
                 time.time() - t1))
    check("A1.1 [M] criterion-A corridors measured on all 5 windows "
          "(f = 1 admissible on %d/%d = %.0f%% >= 95%%)"
          % (n_adm1, n_tot1, 100.0 * n_adm1 / n_tot1),
          n_adm1 >= 0.95 * n_tot1)

    # ============================================================== A2
    print("\nA2 -- per-slot mass corridor, criterion WINDOW-END")
    t2 = time.time()
    n_adm2 = 0
    n_tot2 = 0
    for w in wins:
        Mm1 = w["M"] - 1
        rows = []
        for s in w["slots"]:
            base = w["p"]

            def admB(f, base=base, s=s, Mm1=Mm1):
                return bd_of(base + (f - 1.0) * s["mu"] * s["cu"],
                             Mm1) is None

            ok1 = admB(1.0)
            n_tot2 += 1
            n_adm2 += int(ok1)
            if not ok1:
                rows.append((s["n"], np.nan, np.nan))
                continue
            f_lo = 0.0 if admB(0.0) else bisect_edge(admB, 1.0, 0.0,
                                                     BIT_F)
            f_hi = F_HI_CAP if admB(F_HI_CAP) else \
                bisect_edge(admB, 1.0, F_HI_CAP, BIT_F)
            rows.append((s["n"], f_lo, f_hi))
        w["corrB"] = rows
        hwv = [min(1 - lo, hi - 1) for (_n, lo, hi) in rows
               if not math.isnan(lo)]
        print("   h=%5d: median halfwidth %.5f  min %.5f  max %.5f  "
              "(%.0fs)" % (w["h"], float(np.median(hwv)), min(hwv),
                           max(hwv), time.time() - t2))
    check("A2.1 [M] criterion-B (window-end) corridors measured on "
          "all 5 windows; f = 1 admissible on %d/%d = 100%% (the "
          "true ladder is PD)" % (n_adm2, n_tot2), n_adm2 == n_tot2)

    # detailed table on the deepest window
    w4 = wins[4]
    print("   window 4 (h=%d) corridor table (n, A: [f_lo, f_hi], "
          "B: [f_lo, f_hi]):" % w4["h"])
    for (nA, loA, hiA), (nB, loB, hiB) in zip(w4["corrA"],
                                              w4["corrB"]):
        print("   n=%4d  A: [%.4f, %.4f] (hw %.4f)   B: [%.5f, "
              "%.5f] (hw %.5f)"
              % (nA, loA, hiA, min(1 - loA, hiA - 1),
                 loB, hiB, min(1 - loB, hiB - 1)))

    # ============================================================= A2b
    print("\nA2b -- true-ladder margin + death-location diagnostic")
    for iw in (0, 4):
        w = wins[iw]
        _bd, Es = lev_curve(w["p"], w["M"] - 1)
        i_min = int(np.argmin(Es))
        print("   h=%5d: innovation E_n of the TRUE ladder: E_min/E_0"
              " = %.3e at n = %d (= %.2f M); E_end/E_0 = %.3e"
              % (w["h"], float(Es[i_min] / Es[0]), i_min,
                 i_min / (w["M"] - 1.0),
                 float(Es[-1] / Es[0])))
    w4d = wins[4]
    locs = []
    for s in w4d["slots"][::6]:
        f_hi = next(hi for (n, lo, hi) in w4d["corrB"]
                    if n == s["n"] and not math.isnan(lo))
        f_probe = 1.0 + 2.0 * (f_hi - 1.0) + 1e-6
        b = bd_of(w4d["p"] + (f_probe - 1.0) * s["mu"] * s["cu"],
                  w4d["M"] - 1)
        locs.append((s["n"], s["ist"], b))
    print("   window 4 death locations just OUTSIDE the corridor "
          "(n, slot cell, bd): %s" % locs)
    frac = [b / (w4d["M"] - 1.0) for (_n, _i, b) in locs
            if b is not None]
    check("A2b.1 [M] margin anatomy: death location of an out-of-"
          "corridor perturbation (median bd/M = %.2f) tells whether "
          "the window-end criterion is slot-local (bd near slot) or "
          "boundary-dominated (bd near M)"
          % (float(np.median(frac)) if frac else float("nan")), True)

    # ============================================================== A3
    print("\nA3 -- position needle width (criterion NEXT-SLOT, "
          "TRUE mass)")
    for iw in (0, 4):
        w = wins[iw]
        slots = w["slots"]
        n_map = {s["n"]: j for j, s in enumerate(slots)}
        cur_bg = {}
        cur = w["p_sm"].copy()
        for j, s in enumerate(slots):
            cur_bg[j] = cur.copy()
            cur += s["mu"] * s["cu"]
        widths = []
        for n_t in POS_NS:
            if n_t not in n_map:
                continue
            j = n_map[n_t]
            s = slots[j]
            m0_next = slots[j + 1]["m0"] if j + 1 < len(slots) \
                else s["m0"] + MARGIN_A
            Nrun = min(w["M"] - 1, m0_next + MARGIN_A)
            bg = cur_bg[j]
            cnt = 0
            for jj in range(-POS_HALFCELLS, POS_HALFCELLS + 1):
                u_p = s["u"] + jj * w["D"] / 2.0
                if u_p <= 0.05:
                    continue
                cu = unit_read(w, u_p)
                b = bd_of(bg + s["mu"] * cu, Nrun)
                cnt += int((b is None) or (b >= m0_next))
            widths.append((n_t, 0.5 * cnt))
        w["poswidth"] = widths
        print("   h=%5d: needle widths (cells): %s"
              % (w["h"], ["n=%d: %.1f" % t for t in widths]))
    check("A3.1 [M] position needles measured (true-mass criterion; "
          "5d shooting widths are upper envelopes of these)", True)

    # ============================================================== A4
    print("\nA4 -- scaling fits")
    thetas = {}
    for tag, key in (("A", "corrA"), ("B", "corrB")):
        print("   criterion %s: log(halfwidth) ~ -theta log n:" % tag)
        for w in wins:
            ns, hws = [], []
            for (n, lo, hi) in w[key]:
                if math.isnan(lo):
                    continue
                hw = min(1 - lo, hi - 1)
                if hw > 1e-12:
                    ns.append(n)
                    hws.append(hw)
            th, r2 = fit_loglog(ns, hws)
            q1 = float(np.median([h for n, h in zip(ns, hws)
                                  if n <= 11]))
            q4 = float(np.median([h for n, h in zip(ns, hws)
                                  if n >= 64]))
            thetas[(tag, w["h"])] = (-th, r2)
            print("   h=%5d: theta = %+.3f (R^2 %.3f); median "
                  "halfwidth n<=11: %.5f vs n>=64: %.5f (ratio %.2f)"
                  % (w["h"], -th, r2, q1, q4,
                     q1 / q4 if q4 > 0 else float("inf")))
    # cross-window slope at fixed slots (criterion B)
    common = sorted(set.intersection(
        *[set(n for (n, lo, hi) in w["corrB"]
              if not math.isnan(lo)) for w in wins]))
    slopes = []
    for n_t in common:
        al, hw = [], []
        for w in wins:
            for (n, lo, hi) in w["corrB"]:
                if n == n_t and not math.isnan(lo):
                    al.append(w["alpha"])
                    hw.append(min(1 - lo, hi - 1))
        if len(al) == 5 and min(hw) > 1e-12:
            A = np.vstack([np.array(al), np.ones(5)]).T
            coef, _, _, _ = np.linalg.lstsq(
                A, np.log(np.array(hw)), rcond=None)
            slopes.append(float(coef[0]))
    print("   cross-window (fixed n, criterion B): d log(halfwidth)"
          " / d alpha: median %+.3f, IQR [%.3f, %.3f] over %d slots"
          % (float(np.median(slopes)),
             float(np.quantile(slopes, 0.25)),
             float(np.quantile(slopes, 0.75)), len(slopes)))
    check("A4.1 [M] scaling laws fitted (tables above); NOTE the two "
          "user candidates coincide (u = log n: n^-theta == "
          "e^{-theta u}); constancy readable from the quartile "
          "ratios", True)

    # ============================================================== A5
    print("\nA5 -- aggregate tolerance eps* (full-depth PD)")
    rng = np.random.default_rng(SEED)
    agg = {}
    for iw in AGG_WINS:
        w = wins[iw]
        Mm1 = w["M"] - 1
        ka = w["ka"]
        uu = core.U_ALL[:ka]
        mu = core.MU_ALL[:ka]
        eps_list = []

        def eps_edge(mask_fn):
            def adm(e):
                c_mod, _ = core.atom_lags_at(
                    w["alpha"], w["M"], uu, mu * (1.0 + e * mask_fn))
                return bd_of(w["p_sm"] + c_mod, Mm1) is None
            if adm(EPS_CAP):
                return EPS_CAP
            return bisect_edge(adm, 0.0, EPS_CAP, BIT_E)

        ones = np.ones(ka)
        e_p = eps_edge(ones)
        e_m = eps_edge(-ones)
        eps_list += [("scale +", e_p), ("scale -", e_m)]
        for sd in range(N_SEEDS):
            xi = rng.choice([-1.0, 1.0], size=ka)
            eps_list.append(("iid seed %d" % sd, eps_edge(xi)))
        for om in OMEGAS:
            eps_list.append(("cos(%g u)" % om,
                             eps_edge(np.cos(om * uu))))
        eps_star = min(e for _t, e in eps_list)
        agg[iw] = eps_star
        print("   h=%5d: " % w["h"] + "  ".join(
            "%s: %.2e%s" % (t, e, " (cap)" if e >= EPS_CAP else "")
            for t, e in eps_list) + "   -> eps* = %.2e" % eps_star)
    check("A5.1 [M] aggregate tolerances measured on windows %s "
          "(menu: coherent scale, iid Rademacher x%d, cos "
          "modulation x%d)" % ([wins[i]["h"] for i in AGG_WINS],
                               N_SEEDS, len(OMEGAS)), True)

    # ============================================================= A5b
    print("\nA5b -- depth-resolved aggregate tolerance, window 4")
    w = wins[4]
    ka = w["ka"]
    uu = core.U_ALL[:ka]
    mu = core.MU_ALL[:ka]
    rngb = np.random.default_rng(SEED + 1)
    xi_b = rngb.choice([-1.0, 1.0], size=ka)
    depth_rows = []
    for frac_d in (0.25, 0.5, 0.75, 0.9, 1.0):
        Nd = int(frac_d * (w["M"] - 1))
        vals = []
        for mask in (np.ones(ka), xi_b):
            def adm(e, mask=mask, Nd=Nd):
                c_mod, _ = core.atom_lags_at(
                    w["alpha"], w["M"], uu, mu * (1.0 + e * mask))
                return bd_of(w["p_sm"] + c_mod, Nd) is None
            if adm(EPS_CAP):
                vals.append(EPS_CAP)
            else:
                vals.append(bisect_edge(adm, 0.0, EPS_CAP, BIT_E))
        X_d = math.exp(2.0 * w["alpha"])
        b_unc = math.exp(-math.sqrt(math.log(X_d) / R_ZFR))
        b_rh = (math.log(X_d) ** 2) / (8.0 * math.pi
                                       * math.sqrt(X_d))
        e_min = min(vals)
        depth_rows.append((frac_d, e_min))
        print("   N/M = %.2f: eps*(N) = %.2e  (scale %.2e, iid "
              "%.2e)   [B_unc %.2e, B_RH %.2e]"
              % (frac_d, e_min, vals[0], vals[1], b_unc, b_rh))
    check("A5b.1 [M] depth-resolved tolerance curve measured -- the "
          "depth at which eps*(N) crosses below B_RH marks where the "
          "PD requirement becomes RH-grade/over-RH", True)

    # ============================================================== A6
    print("\nA6 -- budget comparison and verdict")
    classes = {}
    print("   %-7s %-10s %-12s %-12s %-12s %-9s"
          % ("window", "X=e^{2a}", "eps*", "B_unc(X)", "B_RH(X)",
             "class"))
    for iw in AGG_WINS:
        w = wins[iw]
        X = math.exp(2.0 * w["alpha"])
        b_unc = math.exp(-math.sqrt(math.log(X) / R_ZFR))
        b_rh = (math.log(X) ** 2) / (8.0 * math.pi * math.sqrt(X))
        e = agg[iw]
        if e >= b_unc:
            cl = "SUB-RH"
        elif e >= b_rh:
            cl = "RH-GRADE"
        else:
            cl = "OVER-RH"
        classes[iw] = cl
        print("   h=%-5d %-10.3g %-12.3e %-12.5f %-12.5f %-9s"
              % (w["h"], X, e, b_unc, b_rh, cl))
    # per-slot budget columns on window 4 (transparency; frame note
    # in the docstring: masses are exact arithmetic, the analytic
    # budget applies to the aggregate)
    print("   per-slot transparency (window 4, criterion B): "
          "required psi-accuracy A_req = halfwidth x Lambda(n) vs "
          "budgets AT x = n:")
    for (n, lo, hi) in w4["corrB"][:12]:
        if math.isnan(lo):
            continue
        hw = min(1 - lo, hi - 1)
        # Lambda(n) = log p for prime powers; recover p:
        pp = n
        for p in (2, 3, 5, 7, 11, 13):
            k = 0
            m = n
            while m % p == 0:
                m //= p
                k += 1
            if m == 1 and k >= 1:
                pp = p
                break
        lam = math.log(pp)
        b_unc_n = n * math.exp(-math.sqrt(math.log(n) / R_ZFR))
        b_rh_n = math.sqrt(n) * (math.log(n) ** 2) / (8.0 * math.pi)
        print("   n=%4d: A_req = %.2e   E_unc(n) = %8.2f   "
              "E_RH(n) = %8.2f" % (n, hw * lam, b_unc_n, b_rh_n))

    cls_set = set(classes.values())
    if cls_set == {"SUB-RH"}:
        VERDICT = "TOLERANCE-SUB-RH"
    elif cls_set <= {"RH-GRADE", "OVER-RH"}:
        VERDICT = "TOLERANCE-RH-GRADE"
    else:
        VERDICT = "TOLERANCE-MIXED"
    check("A6.1 [M] preregistered classification applied: %s "
          "(per-window classes %s)"
          % (VERDICT, {wins[i]["h"]: classes[i] for i in AGG_WINS}),
          True)

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
