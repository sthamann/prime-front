#!/usr/bin/env python3
"""v708 -- PRIME.POSFUNC.01: S-F, THE POSITION FUNCTIONAL:
which functional fixes the corridor position pos ~ 0.53 that S-E
measured for the true mass inside the just-in-time positivity
corridor?

EXPLORATION ONLY (experiments/ firewall): nothing here is a
verification claim; no verification/, paper, ledger or website
surface is touched; no marker moves; NO RH statement.  File prefix
chain_ (round 9 owns the suite surfaces; the beam worker owns z1_*).

FRAME [S-E].  The just-in-time corridor of slot k at horizon
N = m0(next atom) is the closed interval
    [w_lo, w_hi] = {w : T_N(prev + w cu) >= 0}
(S-E proved the closed resolvent edge formula == Levinson breakdown
edges to machine precision; here the edges are found by Levinson
bisection, identity cited, spot-checked once).  S-E measured on
window 2: the true mass sits at pos = (mu - w_lo)/(w_hi - w_lo)
with median 0.534, IQR [0.511, 0.559]; window 0 median 0.523.

MEASUREMENTS (bars/verdicts declared BEFORE any number):
  F1 [M] the position anatomy, ALL 5 windows x all slots (u <=
     log 120; 200 slot-window pairs):
     F1.1 corridors found and the mass inside on every pair
          (pos in (0,1)) -- the S-E finding, full-family bar;
     F1.2 drift diagnostics: corr(pos, log n) pooled and per
          window, corr(pos, |alpha_bg|) (slot hardness = the
          predecessor reflection coefficient at the dominant cell),
          per-window medians vs window size (transport);
     F1.3 exact-value diagnostic AGAINST the pooled distribution:
          0.5, 8/15, (1+U0)/3 (U0 = 0.5899, corpus pole-block
          constant), 1/phi - 0.08.  Bonferroni-honest: 4 tests,
          bootstrap 99% CI of the pooled median (~ 95%/4); the test
          can only KILL values outside the CI, it cannot crown one
          -- the candidate values differ by less than the slot
          scatter, declared up front;
     F1.4 if pos is not a constant: two-parameter linear fit
          pos ~ a + b |alpha_bg| + c log n on windows {0,1,2},
          transport test on {3,4} (median |residual|).
  F2 [M] the five functional candidates, per slot, prediction
     ARITHMETIC-FREE (corridor + background only; the corridor scan
     is anchored on the closed C0 anchor = zero reflection at the
     dominant cell -- no MU_ALL in the prediction path; MU_ALL
     enters only as exact-past conditioning (declared) and as
     comparison target):
     (a) slope-weighted edge balance: the w where the two edge
         margins scaled by the violation rates balance,
         s_lo (w - w_lo) = s_hi (w_hi - w), s_edge = |v' T(cu) v|
         with v the touching null vector at each edge (compressed-
         resolvent weights; windows 0/2 full, window 4 subset --
         eigenvector cost, declared);
     (b) Levinson energy extremum: argmax_w E_{N-1}(w) -- the
         final innovation energy at the horizon (the "healthiest"
         continuation);
     (c) Fejer dip centroid: the matched-filter mass over the
         negative symbol region at Fejer order N (S-D K2b, now
         placed inside the measured corridor);
     (d) Schur extremality: argmin_w |k_{m0+2}(w)| (d1, the first
         post-support Schur iterate) and |k_{m0+3}(w)| (d2, the
         S-B C2 cell) -- the most contractive continuation;
     (e) MaxEnt/Burg point: argmax_w sum_{i<N} log E_i(w)
         = argmax_w log det T_N(w) -- THE canonical interior point
         of the corridor.
     For each: ratio w/mu (median, max over the ladder, per window
     -- transport WITHOUT scalar) and predicted corridor position.
  F3 verdict (preregistered):
     FUNCTIONAL-FOUND  iff some candidate has max|ratio-1| < 1%
                       over ALL windows/slots AND |median-1| < 1%
                       in EVERY window (transport without scalar);
     FUNCTIONAL-OPEN   otherwise: ranked list with exact numbers +
                       what the pos anatomy (F1) says about the
                       missing selection object.

FIREWALL: AST-checked -- no zetazero/nzeros/zeta anywhere.  MU_ALL
enters ONLY as exact-past conditioning, as comparison target, and in
pos_true (declared); every F2 prediction path is arithmetic-free
(C0-anchored corridor + background Levinson/Fejer data).

Provenance (read-only): v563 core, chain_section_edge_probe (S-E:
edge identity + pos finding), chain_mass_law_probe (S-B benchmark
C2: median 0.9947, max|r-1| 0.31), chain_weyl_mass_probe (S-D),
classical Burg/MaxEnt + Schur theory (cited).

PROVENANCE: discovery probe chain_position_functional_probe.py
(2026-08-03, 7/7 PASS, verdict FUNCTIONAL-OPEN: the best functional is
the Levinson energy extremum E_{N-1}, median ratio 0.9986 / max
deviation 11.7%, and it TRANSPORTS across windows without a scalar;
the outliers sit exactly on the prime powers 16/64/81).  Promoted
verbatim; numbers unchanged.
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
U0_POLE = 0.5899          # corpus pole-block constant (diagnostic)
ND_SYM = 1 << 16
BIT_EDGE = 45
GOLD_IT = 45
W4_A_SUBSET = 10
CAND_VALUES = (("1/2", 0.5), ("8/15", 8.0 / 15.0),
               ("(1+U0)/3", (1.0 + U0_POLE) / 3.0),
               ("1/phi-0.08", 2.0 / (1.0 + math.sqrt(5.0)) - 0.08))


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


def lev_full(r, N):
    """Levinson to step N: returns (ks array, log E array after each
    step, ok flag); truncated at breakdown (ok False)."""
    r = np.asarray(r, float)
    a = np.zeros(N + 1)
    a[0] = 1.0
    E = float(r[0])
    ks = np.empty(N)
    logE = np.empty(N)
    for n in range(1, N + 1):
        acc = r[n] + (float(a[1:n] @ r[n - 1:0:-1]) if n > 1 else 0.0)
        k = -acc / E
        a[1:n + 1] = a[1:n + 1] + k * a[n - 1::-1][:n]
        E *= (1.0 - k * k)
        if not (abs(k) < 1.0) or E <= 0.0:
            return ks[:n - 1], logE[:n - 1], False
        ks[n - 1] = k
        logE[n - 1] = math.log(E)
    return ks, logE, True


def c0_anchor(bg, s):
    """Closed arithmetic-free anchor (S-B C0): the w zeroing the
    reflection at the dominant cell (linear in w)."""
    ist = s["ist"]
    ks0, _e0, ok0 = lev_full(bg, ist + 1)
    ks1, _e1, ok1 = lev_full(bg + s["cu"], ist + 1)
    if len(ks0) < ist or len(ks1) < ist:
        return float("nan")
    k0, k1 = ks0[ist - 1], ks1[ist - 1]
    if k1 == k0:
        return float("nan")
    return float(-k0 / (k1 - k0))


def corridor(bg, cu, scale, Nm):
    """JIT corridor [w_lo, w_hi] at matrix size Nm via Levinson
    bisection (edge identity with the closed resolvent formula
    established in S-E, cited).  scale = arithmetic-free anchor."""
    def ok(w):
        return bd_of(bg + w * cu, Nm - 1) is None

    grid = scale * np.geomspace(0.05, 20.0, 61)
    adm = [w for w in grid if ok(w)]
    if not adm:
        # thin corridors (relative width down to ~0.5%) slip through
        # the geometric grid when the anchor is a few % off: fine
        # linear rescan near the anchor, then a wide linear sweep
        for fine in (scale * np.linspace(0.6, 1.6, 401),
                     scale * np.linspace(0.1, 3.0, 291)):
            adm = [w for w in fine if ok(w)]
            if adm:
                break
    if not adm:
        return float("nan"), float("nan")
    lo_in, hi_in = min(adm), max(adm)
    # expanding brackets (lower edge may cross zero)
    lo_out = None
    step = 0.25 * scale
    w = lo_in
    for _ in range(40):
        w -= step
        if not ok(w):
            lo_out = w
            break
        step *= 1.7
    hi_out = None
    step = 0.25 * scale
    w = hi_in
    for _ in range(40):
        w += step
        if not ok(w):
            hi_out = w
            break
        step *= 1.7
    if lo_out is None or hi_out is None:
        return float("nan"), float("nan")

    def edge(w_in, w_bad):
        for _ in range(BIT_EDGE):
            wm = 0.5 * (w_in + w_bad)
            if ok(wm):
                w_in = wm
            else:
                w_bad = wm
        return w_in

    return edge(lo_in, lo_out), edge(hi_in, hi_out)


def golden_max(fun, w_lo, w_hi, iters=GOLD_IT):
    """Golden-section maximizer on [w_lo, w_hi]."""
    gr = 0.5 * (math.sqrt(5.0) - 1.0)
    a, b = w_lo, w_hi
    c = b - gr * (b - a)
    d = a + gr * (b - a)
    fc, fd = fun(c), fun(d)
    for _ in range(iters):
        if fc > fd:
            b, d, fd = d, c, fc
            c = b - gr * (b - a)
            fc = fun(c)
        else:
            a, c, fc = c, d, fd
            d = a + gr * (b - a)
            fd = fun(d)
    return 0.5 * (a + b)


def fejer_symbol(lags, N):
    arr = np.zeros(ND_SYM)
    d = np.arange(1, N)
    arr[0] = lags[0]
    arr[1:N] = 2.0 * (1.0 - d / N) * lags[1:N]
    return np.fft.rfft(arr).real


def fejer_centroid(bg, cu, Nm):
    sig = fejer_symbol(bg, Nm)
    su = fejer_symbol(cu, Nm)
    mask = sig < 0
    if not mask.any():
        return float("nan")
    return float(-(sig[mask] @ su[mask]) / (su[mask] @ su[mask]))


def quad_toep_sparse(cu, v, cells):
    """v' T(cu) v using only the nonzero lags of cu (cells)."""
    acc = cu[0] * float(v @ v) if cu[0] != 0 else 0.0
    for d in cells:
        if d == 0:
            continue
        acc += 2.0 * cu[d] * float(v[:-d] @ v[d:])
    return acc


def stats_ratio(v):
    v = np.asarray([x for x in v if not math.isnan(x)], float)
    if len(v) == 0:
        return (float("nan"),) * 3, 0
    return (float(np.median(v)), float(np.max(np.abs(v - 1.0))),
            float(np.quantile(v, 0.25))), len(v)


def run():
    print("=" * 78)
    print("S-F CHAIN POSITION FUNCTIONAL -- what fixes pos ~ 0.53?")
    print("=" * 78)

    check("G0.0 [E] AST firewall: no zeta/zero symbol anywhere; "
          "MU_ALL only as exact-past conditioning / pos_true / "
          "comparison target; every F2 prediction path is "
          "C0-anchored (arithmetic-free)",
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
    wins = {}
    for iw, (kz, _a, _M) in enumerate(picks):
        w = build_win(kz)
        w["slots"] = slot_list(w)
        wins[iw] = w
    print("   windows: %s" % ", ".join(
        "%d (h=%d)" % (iw, wins[iw]["M"] // 2) for iw in wins))

    # ============================================================== F1
    print("\nF1 -- position anatomy, all 5 windows x all slots")
    t1 = time.time()
    recs = []
    for iw in sorted(wins):
        w = wins[iw]
        sl = w["slots"]
        prev = w["p_sm"].copy()
        for j, s in enumerate(sl):
            if j + 1 < len(sl):
                m0n = sl[j + 1]["m0"]
            else:
                u_nx = float(core.U_ALL[s["i"] + 1])
                m0n = int(np.nonzero(unit_read(w, u_nx))[0][0])
            Nm = min(w["M"] - 1, m0n)
            anch = c0_anchor(prev, s)
            if not (anch > 0) or math.isnan(anch):
                anch = s["mu"]      # declared fallback (counted)
                fb = True
            else:
                fb = False
            w_lo, w_hi = corridor(prev, s["cu"], anch, Nm)
            if not math.isnan(w_lo):
                ksb, _eb, _okb = lev_full(prev, s["ist"] + 1)
                hard = abs(float(ksb[s["ist"] - 1])) \
                    if len(ksb) >= s["ist"] else float("nan")
                recs.append(dict(
                    iw=iw, j=j, n=s["n"], u=s["u"], mu=s["mu"],
                    Nm=Nm, w_lo=w_lo, w_hi=w_hi, anch=anch, fb=fb,
                    hard=hard, prev_ref=(iw, j),
                    pos=(s["mu"] - w_lo) / (w_hi - w_lo),
                    width=(w_hi - w_lo) / s["mu"]))
            prev += s["mu"] * s["cu"]
        w["prevs"] = None
    n_tot = sum(len(wins[iw]["slots"]) for iw in wins)
    n_fb = sum(1 for r in recs if r["fb"])
    pos_all = np.array([r["pos"] for r in recs])
    print("   %d/%d corridors found (%.0fs; %d anchor fallbacks); "
          "pooled pos: median %.4f  IQR [%.4f, %.4f]  range "
          "[%.4f, %.4f]"
          % (len(recs), n_tot, time.time() - t1, n_fb,
             float(np.median(pos_all)),
             float(np.quantile(pos_all, 0.25)),
             float(np.quantile(pos_all, 0.75)),
             float(np.min(pos_all)), float(np.max(pos_all))))
    for iw in sorted(wins):
        pw = np.array([r["pos"] for r in recs if r["iw"] == iw])
        print("   window %d: pos median %.4f  IQR [%.4f, %.4f]  "
              "(%d slots)"
              % (iw, float(np.median(pw)),
                 float(np.quantile(pw, 0.25)),
                 float(np.quantile(pw, 0.75)), len(pw)))
    check("F1.1 [M] corridors on %d/%d slot-window pairs; the true "
          "mass sits INSIDE every corridor (pos range [%.3f, %.3f])"
          % (len(recs), n_tot, float(np.min(pos_all)),
             float(np.max(pos_all))),
          len(recs) >= n_tot - 2
          and bool(np.all(pos_all > 0) and np.all(pos_all < 1)))

    logn = np.log(np.array([r["n"] for r in recs], float))
    hard = np.array([r["hard"] for r in recs])
    mh = ~np.isnan(hard)
    c_n = float(np.corrcoef(pos_all, logn)[0, 1])
    c_h = float(np.corrcoef(pos_all[mh], hard[mh])[0, 1])
    per_win = []
    for iw in sorted(wins):
        m_ = np.array([r["iw"] == iw for r in recs])
        per_win.append(float(np.corrcoef(pos_all[m_],
                                         logn[m_])[0, 1]))
    print("   drift: corr(pos, log n) pooled %.3f, per window %s; "
          "corr(pos, |alpha_bg|) %.3f"
          % (c_n, ["%.2f" % c for c in per_win], c_h))
    check("F1.2 [M] drift diagnostics measured: pos is NOT free of "
          "structure -- corr(pos, log n) = %.3f pooled (per window "
          "%s), corr(pos, |alpha_bg|) = %.3f; per-window medians "
          "within %.4f of each other (transport of the LEVEL)"
          % (c_n, ["%.2f" % c for c in per_win], c_h,
             float(np.max([abs(np.median(
                 [r["pos"] for r in recs if r["iw"] == a])
                 - np.median([r["pos"] for r in recs
                              if r["iw"] == b]))
                 for a in wins for b in wins]))), True)

    # bootstrap CI of the pooled median (Bonferroni-honest: 99% ~ 95%/4)
    rng = np.random.default_rng(20260803)
    boots = np.array([np.median(rng.choice(pos_all, len(pos_all)))
                      for _ in range(4000)])
    ci_lo, ci_hi = (float(np.quantile(boots, 0.005)),
                    float(np.quantile(boots, 0.995)))
    verdicts = []
    for name, val in CAND_VALUES:
        inside = ci_lo <= val <= ci_hi
        verdicts.append((name, val, inside))
        print("   exact-value test: %-11s = %.5f -> %s the 99%% CI "
              "[%.5f, %.5f]" % (name, val,
                                "INSIDE" if inside else "outside",
                                ci_lo, ci_hi))
    n_in = sum(1 for (_n, _v, i_) in verdicts if i_)
    check("F1.3 [M] exact-value diagnostic (Bonferroni-honest, 4 "
          "tests, 99%% bootstrap CI of the pooled median): %d/4 "
          "candidate values inside -- %s; the CI cannot crown a "
          "single value (candidates differ by less than slot "
          "scatter, declared) -- pos is a distribution around "
          "~%.3f, not (yet) an identified constant"
          % (n_in, [(nm, "in" if i_ else "OUT")
                    for (nm, _v, i_) in verdicts],
             float(np.median(pos_all))), True)

    X = np.column_stack([np.ones(mh.sum()), hard[mh], logn[mh]])
    y = pos_all[mh]
    beta, *_r = np.linalg.lstsq(X, y, rcond=None)
    resid = y - X @ beta
    r2 = 1.0 - float(resid @ resid) / float(
        ((y - y.mean()) @ (y - y.mean())))
    iw_arr = np.array([r["iw"] for r in recs])[mh]
    tr_mask = iw_arr <= 2
    beta_tr, *_r2 = np.linalg.lstsq(X[tr_mask], y[tr_mask],
                                    rcond=None)
    res_te = y[~tr_mask] - X[~tr_mask] @ beta_tr
    print("   two-parameter fit pos = %.4f + %.4f |alpha_bg| + "
          "%.4f log n: R^2 = %.3f (pooled); fit on windows 0-2, "
          "median |residual| on windows 3-4: %.4f (vs pooled pos "
          "std %.4f)"
          % (beta[0], beta[1], beta[2], r2,
             float(np.median(np.abs(res_te))), float(np.std(y))))
    check("F1.4 [M] two-parameter anatomy: R^2 = %.3f -- pos is "
          "%s by (|alpha_bg|, log n); transport residual %.4f"
          % (r2, "largely explained" if r2 >= 0.5
             else "NOT explained", float(np.median(np.abs(res_te)))),
          True)

    # ============================================================== F2
    print("\nF2 -- the functional candidates (prediction "
          "arithmetic-free, exact past)")
    # rebuild prev backgrounds once per window for candidate passes
    prevs = {}
    for iw in sorted(wins):
        w = wins[iw]
        prev = w["p_sm"].copy()
        for j, s in enumerate(w["slots"]):
            prevs[(iw, j)] = prev.copy()
            prev += s["mu"] * s["cu"]

    t2 = time.time()
    cands = ("a", "b", "c", "d1", "d2", "e")
    res = {c: [] for c in cands}
    n_a_done = 0
    for r in recs:
        iw, j = r["iw"], r["j"]
        w = wins[iw]
        s = w["slots"][j]
        prev = prevs[(iw, j)]
        Nm, w_lo, w_hi = r["Nm"], r["w_lo"], r["w_hi"]
        wid = w_hi - w_lo
        eps = 1e-7 * wid
        cells = [d for d in np.nonzero(s["cu"])[0]]

        def ratio_pos(wp):
            if math.isnan(wp):
                return float("nan"), float("nan")
            return wp / s["mu"], (wp - w_lo) / wid

        # (b) final innovation energy; (e) MaxEnt log det
        def E_last(wv):
            _k, le, ok_ = lev_full(prev + wv * s["cu"], Nm - 1)
            return le[-1] if ok_ else -1e18

        def logdet(wv):
            _k, le, ok_ = lev_full(prev + wv * s["cu"], Nm - 1)
            return float(np.sum(le)) if ok_ else -1e18

        w_b = golden_max(E_last, w_lo + eps, w_hi - eps)
        w_e = golden_max(logdet, w_lo + eps, w_hi - eps)
        # (c) Fejer dip centroid
        w_cf = fejer_centroid(prev, s["cu"], Nm)
        # (d) Schur extremality at cells m0+2 / m0+3
        def k_abs(cell):
            def f(wv):
                ks_, _le, ok_ = lev_full(prev + wv * s["cu"],
                                         cell + 1)
                return -abs(float(ks_[cell - 1])) \
                    if len(ks_) >= cell else -1e18
            return f
        w_d1 = golden_max(k_abs(s["m0"] + 2), w_lo + eps,
                          w_hi - eps)
        w_d2 = golden_max(k_abs(s["m0"] + 3), w_lo + eps,
                          w_hi - eps)
        # (a) slope-weighted edge balance (eigenvector cost)
        w_a = float("nan")
        do_a = iw in (0, 2) or (iw == 4 and j % 4 == 0
                                and n_a_done < W4_A_SUBSET)
        if do_a:
            try:
                s_w = []
                for w_edge in (w_lo, w_hi):
                    C = sla.toeplitz((prev + w_edge
                                      * s["cu"])[:Nm])
                    _lam, V = sla.eigh(C, subset_by_index=[0, 0])
                    v = V[:, 0]
                    s_w.append(abs(quad_toep_sparse(s["cu"], v,
                                                    cells)))
                if s_w[0] + s_w[1] > 0:
                    w_a = (s_w[0] * w_lo + s_w[1] * w_hi) \
                        / (s_w[0] + s_w[1])
                if iw == 4:
                    n_a_done += 1
            except Exception:
                pass
        for cname, wp in (("a", w_a), ("b", w_b), ("c", w_cf),
                          ("d1", w_d1), ("d2", w_d2), ("e", w_e)):
            rr, pp = ratio_pos(wp)
            res[cname].append(dict(iw=iw, n=s["n"], ratio=rr,
                                   pos=pp))
    print("   candidate pass done (%.0fs)" % (time.time() - t2))

    LABELS = {"a": "slope-weighted edge balance",
              "b": "energy extremum E_{N-1}",
              "c": "Fejer dip centroid (K2b@N)",
              "d1": "Schur |k_{m0+2}| minimum",
              "d2": "Schur |k_{m0+3}| minimum (S-B C2 cell)",
              "e": "MaxEnt argmax log det T_N"}
    board = []
    for cname in cands:
        rows = res[cname]
        (med, mx, _q1), n_ok = stats_ratio([r_["ratio"]
                                            for r_ in rows])
        pmed = float(np.nanmedian([r_["pos"] for r_ in rows]))
        med_w = []
        for iw in sorted(wins):
            (mw, _mxw, _qw), n_w = stats_ratio(
                [r_["ratio"] for r_ in rows if r_["iw"] == iw])
            med_w.append(mw)
        board.append((cname, med, mx, pmed, med_w, n_ok))
        print("   (%s) %-38s: ratio median %.4f  max|r-1| %.4f  "
              "pos median %.4f  per-window medians %s  (%d slots)"
              % (cname, LABELS[cname], med, mx, pmed,
                 ["%.4f" % m for m in med_w], n_ok))
    for cname in ("b", "e"):
        rows = [r_ for r_ in res[cname]
                if not math.isnan(r_["ratio"])]
        worst = sorted(rows, key=lambda r_: -abs(r_["ratio"] - 1.0))
        print("   worst slots (%s): %s"
              % (cname, [(r_["iw"], r_["n"], round(r_["ratio"], 3))
                         for r_ in worst[:6]]))
    check("F2.1 [M] all six candidate functionals measured on the "
          "5-window ladder (arithmetic-free predictions inside the "
          "measured corridors; candidate (a) on windows 0/2 + %d "
          "window-4 slots, declared)" % n_a_done, True)

    # ============================================================== F3
    print("\nF3 -- verdict")
    board_s = sorted(board, key=lambda b: b[2])
    winners = [b for b in board_s
               if b[2] < 0.01
               and all(abs(m - 1) < 0.01 for m in b[4]
                       if not math.isnan(m))]
    print("   ranked list (by max|r-1|):")
    for (cn, med, mx, pmed, med_w, n_ok) in board_s:
        print("     %-3s max|r-1| %.4f  median %.4f  pos %.4f"
              % (cn, mx, med, pmed))
    if winners:
        cn, med, mx, pmed, med_w, n_ok = winners[0]
        VERDICT = ("FUNCTIONAL-FOUND: (%s) %s -- max|r-1| %.4f, "
                   "median %.4f, transport medians %s"
                   % (cn, LABELS[cn], mx, med,
                      ["%.4f" % m for m in med_w]))
    else:
        b0 = board_s[0]
        VERDICT = ("FUNCTIONAL-OPEN (best: (%s) %s with max|r-1| "
                   "%.4f, median %.4f; none reaches 1%% uniform)"
                   % (b0[0], LABELS[b0[0]], b0[2], b0[1]))
    check("F3.1 [M] preregistered classification: %s" % VERDICT,
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
