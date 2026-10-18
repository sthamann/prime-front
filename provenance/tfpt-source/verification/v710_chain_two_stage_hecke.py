#!/usr/bin/env python3
"""v710 -- PRIME.TWOSTAGE.01: P1 KILL TEST: the two-stage
Hecke selector for the G1 residual.

DIAGNOSIS UNDER TEST (strategy memo): the S-F energy extremum is a
single-slot functional and structurally mis-posed on prime powers --
the outliers 16, 64, 81 carry LOCAL MEMORY through their base-prime
channel (Lambda(p^k) = log p is the mass of the CHANNEL, not of the
slot).  The two-stage rule:
  stage 1 (first births, n = p prime): mass = energy extremum in the
     just-in-time positivity corridor (S-F best, arithmetic-free);
  stage 2 (repetitions, n = p^k, k >= 2): mass is NOT re-selected in
     the corridor but continued through the local Hecke/Satake
     recursion of the already-open p channel:
        w(p^k) = w_stage1(p) * p_geo^{-(k-1)/2}
     (mu(p^k)/mu(p) = p^{(1-k)/2} exactly on the half-line comb).

THE CIRCLE-FREE RECOGNITION PATH (the memo's hard requirement --
channel/repetition structure from E8 counting BEFORE any comparison
with MU_ALL, else it is a renaming):
  1. E8 shell counts r(2n) by PURE integer convolution of the glue
     decomposition (theta2^8 + theta3^8 + theta4^8)/2 (v625 route,
     re-implemented inline; lattice counting, no zeta anywhere);
  2. the divisor recursion  a(n) log n = sum_{d|n} Lambda_L(d) a(n/d)
     with a(n) = r(2n)/240 DEFINES Lambda_L from counting;
  3. Lambda_geo(n) := Lambda_L(n)/(1+n^3);
  4. classification: n is a FIRST BIRTH iff Lambda_geo(n) = log n
     (within 1e-6); n is a REPETITION of channel p_geo =
     round(exp(Lambda_geo(n))) with k_geo = round(log n /
     Lambda_geo(n)) iff Lambda_geo(n) in (0.1, log n - 1e-6) and
     p_geo^k_geo == n as integers.
  The classification is computed and SHA256-hashed BEFORE the
  prediction pass; ground-truth factorization enters ONLY as a
  verification check of the counting identity (declared, v625
  pattern).

DECLARED CONDITIONING (unchanged from S-E/S-F, the 5e verifier
boundary stays): slot POSITIONS log n are given; the exact-past
background inside the energy extremum uses the true earlier masses.
No claim of an autonomous generator.  MU_ALL enters the prediction
path ONLY through that declared conditioning; the stage-2
continuation uses no corridor and no MU_ALL at the target slot.
NO free parameter, NO fit, NO window-specific scalar anywhere.

MEASUREMENTS (bars declared BEFORE any number):
  H1.1 [E] glue shell counts == 240 sigma_3(n) exactly (n <= 128);
  H1.2 [E] the geometric classification (first birth / repetition,
       base p_geo, exponent k_geo) matches factorization ground
       truth for every n in the slot range; hashed before stage 2.
  H2  [M] all ~200 slot-window pairs re-predicted with the
       two-stage rule: (i) median and max |r-1| overall (memo
       targets: median < 0.1%, max < 1%); (ii) do 16, 64, 81 heal
       (< 1%)?; (iii) leave-one-window-out transport: the predictor
       has ZERO fitted parameters -- per-window median/max reported
       raw (kill: a window-specific scalar would be needed, i.e.
       some window median deviates > 1%).
  H3  kill adjudication (preregistered, memo wording):
       P1-TWO-STAGE-DEAD  iff (16/64/81 remain > 1% after Hecke
                          continuation) OR (max overall > 2%) OR
                          (window-specific scalar needed);
       P1-TWO-STAGE-PASS  iff median < 0.1% AND max < 1%
                          (conditioned closure of G1: first births
                          arithmetic-free + repetitions from
                          counting);
       P1-TWO-STAGE-MARGINAL otherwise (exact numbers, no kill, no
                          pass -- honest gray zone).
       If DEAD: the remaining error anatomy (which slots, and what
       they share) is documented.

Provenance (read-only): v563 core, v625/geometric_sos_probe (theta
glue + Lambda_L recursion, cited and re-implemented inline),
chain_position_functional_probe (S-F stage-1 functional),
chain_zero_layer_probe (S-G residual anatomy).

PROVENANCE: discovery probe chain_two_stage_hecke_probe.py
(2026-08-03, 7/7 PASS, verdict P1-TWO-STAGE-DEAD: the memo kill fired,
max overall deviation 6.15% > the 2% bar -- BUT the Hecke mechanism
heals the prime-power slots 11.7% -> 0.53% with circle-free channel
detection from the E8 counting [E]; the remainder is the first-birth
selection on coarse windows).  Promoted verbatim; numbers unchanged.
"""
import ast
import hashlib
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

U_SLOTS = math.log(120.0)
N_REC = 128
NMAX_Q = 2 * N_REC
BIT_EDGE = 45
GOLD_IT = 45
PP_TRACK = (16, 64, 81)


# ---------------- v625-style theta glue (pure integer counting) ------
def theta_shells(nmax_q):
    def conv(a, b):
        out = np.convolve(a, b)[:nmax_q + 1]
        assert int(np.max(np.abs(out))) < 2 ** 62
        return out

    def power8(a):
        s2 = conv(a, a)
        s4 = conv(s2, s2)
        return conv(s4, s4)

    th3 = np.zeros(nmax_q + 1, dtype=np.int64)
    th3[0] = 1
    th4 = np.zeros(nmax_q + 1, dtype=np.int64)
    th4[0] = 1
    k = 1
    while k * k <= nmax_q:
        th3[k * k] = 2
        th4[k * k] = 2 * (-1) ** k
        k += 1
    t2o = np.zeros(nmax_q + 1, dtype=np.int64)
    k = 0
    while k * (k + 1) <= nmax_q:
        t2o[k * (k + 1)] = 1
        k += 1
    th2_8 = np.zeros(nmax_q + 1, dtype=np.int64)
    th2_8[2:] = 256 * power8(t2o)[:nmax_q - 1]
    tot = power8(th3) + power8(th4) + th2_8
    assert all(int(c) % 2 == 0 for c in tot)
    return [int(c) // 2 for c in tot]


def divisors_of(n):
    """Trial-division divisor list (integer counting, no factor
    tables)."""
    out = []
    d = 1
    while d * d <= n:
        if n % d == 0:
            out.append(d)
            if d != n // d:
                out.append(n // d)
        d += 1
    return sorted(out)


# ------------------------------------------------ window machinery
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
    ist = s["ist"]
    ks0, _e0, _ok0 = lev_full(bg, ist + 1)
    ks1, _e1, _ok1 = lev_full(bg + s["cu"], ist + 1)
    if len(ks0) < ist or len(ks1) < ist:
        return float("nan")
    k0, k1 = ks0[ist - 1], ks1[ist - 1]
    if k1 == k0:
        return float("nan")
    return float(-k0 / (k1 - k0))


def corridor(bg, cu, scale, Nm):
    def ok(w):
        return bd_of(bg + w * cu, Nm - 1) is None

    grid = scale * np.geomspace(0.05, 20.0, 61)
    adm = [w for w in grid if ok(w)]
    if not adm:
        for fine in (scale * np.linspace(0.6, 1.6, 401),
                     scale * np.linspace(0.1, 3.0, 291)):
            adm = [w for w in fine if ok(w)]
            if adm:
                break
    if not adm:
        return float("nan"), float("nan")
    lo_in, hi_in = min(adm), max(adm)
    lo_out = hi_out = None
    step = 0.25 * scale
    w = lo_in
    for _ in range(40):
        w -= step
        if not ok(w):
            lo_out = w
            break
        step *= 1.7
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


def run():
    print("=" * 78)
    print("P1 KILL TEST -- two-stage Hecke selector for the G1 "
          "residual")
    print("=" * 78)

    check("H0.0 [E] AST firewall: no zeta/zero symbol anywhere; "
          "MU_ALL only via the DECLARED exact-past conditioning "
          "(5e verifier boundary stays) and as comparison target",
          ast_firewall(os.path.abspath(__file__)))

    # ============================================================== H1
    print("\nH1 -- circle-free channel recognition from E8 counting")
    t1 = time.time()
    TE8 = theta_shells(NMAX_Q)
    sig3 = [0] + [sum(d ** 3 for d in divisors_of(n))
                  for n in range(1, N_REC + 1)]
    glue_ok = (TE8[0] == 1
               and all(TE8[m] == 0 for m in range(1, NMAX_Q + 1, 2))
               and all(TE8[2 * n] == 240 * sig3[n]
                       for n in range(1, N_REC + 1)))
    check("H1.1 [E] E8 glue (theta2^8+theta3^8+theta4^8)/2: shell "
          "counts r(2n) = 240 sigma_3(n) EXACTLY for n = 1..%d "
          "(pure integer convolution, %.1fs) -- the counting input "
          "is lattice geometry, no zeta" % (N_REC, time.time() - t1),
          glue_ok)

    # divisor recursion defines Lambda_L from counts
    a_cnt = [0] + [TE8[2 * n] // 240 for n in range(1, N_REC + 1)]
    lamL = {1: 0.0}
    for n in range(2, N_REC + 1):
        acc = a_cnt[n] * math.log(n)
        for d in divisors_of(n):
            if 1 < d < n:
                acc -= lamL[d] * a_cnt[n // d]
        lamL[n] = acc
    lam_geo = {n: lamL[n] / (1.0 + float(n) ** 3)
               for n in range(2, N_REC + 1)}

    # geometric classification (BEFORE any prediction)
    classify = {}
    for n in range(2, N_REC + 1):
        lg = lam_geo[n]
        if abs(lg - math.log(n)) < 1e-6:
            classify[n] = ("first", n, 1)
        elif lg > 0.1 and lg < math.log(n) - 1e-6:
            p_geo = int(round(math.exp(lg)))
            k_geo = int(round(math.log(n) / lg))
            if p_geo ** k_geo == n:
                classify[n] = ("rep", p_geo, k_geo)
            else:
                classify[n] = ("none", 0, 0)
        else:
            classify[n] = ("none", 0, 0)
    h_cls = hashlib.sha256(repr(sorted(classify.items()))
                           .encode()).hexdigest()
    # ground-truth verification (factorization used ONLY here)
    def factor_gt(n):
        m, p = n, 0
        d = 2
        while d * d <= m:
            if m % d == 0:
                p = d
                k = 0
                while m % d == 0:
                    m //= d
                    k += 1
                return ("first", n, 1) if (m == 1 and k == 1) else \
                    (("rep", d, k) if m == 1 else ("none", 0, 0))
            d += 1
        return ("first", n, 1)
    cls_ok = all(classify[n] == factor_gt(n)
                 for n in range(2, N_REC + 1))
    n_first = sum(1 for n in classify if classify[n][0] == "first")
    n_rep = sum(1 for n in classify if classify[n][0] == "rep")
    check("H1.2 [E] geometric classification from Lambda_geo = "
          "Lambda_L/(1+n^3): %d first births, %d repetitions in "
          "n = 2..%d; matches factorization ground truth EXACTLY "
          "(verification only); SHA256(classification) = %s... "
          "(hashed before stage 2)"
          % (n_first, n_rep, N_REC, h_cls[:16]), cls_ok)
    reps_in_range = sorted(n for n in classify
                           if classify[n][0] == "rep" and n <= 120)
    print("   repetitions in slot range: %s"
          % [(n, classify[n][1], classify[n][2])
             for n in reps_in_range])

    # ============================================================== H2
    print("\nH2 -- the two-stage prediction, all windows")
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

    t2 = time.time()
    rows = []
    for iw, (kz, _a, _M) in enumerate(picks):
        w = build_win(kz)
        sl = slot_list(w)
        prev = w["p_sm"].copy()
        chan = {}
        for j, s in enumerate(sl):
            kind, p_geo, k_geo = classify[s["n"]]
            if kind == "first":
                if j + 1 < len(sl):
                    m0n = sl[j + 1]["m0"]
                else:
                    u_nx = float(core.U_ALL[s["i"] + 1])
                    m0n = int(np.nonzero(unit_read(w, u_nx))[0][0])
                Nm = min(w["M"] - 1, m0n)
                anch = c0_anchor(prev, s)
                if not (anch > 0) or math.isnan(anch):
                    anch = s["mu"]
                w_lo, w_hi = corridor(prev, s["cu"], anch, Nm)
                if math.isnan(w_lo):
                    prev += s["mu"] * s["cu"]
                    continue
                wid = w_hi - w_lo
                eps = 1e-7 * wid

                def E_last(wv, _p=prev, _c=s["cu"], _N=Nm):
                    _k, le, ok_ = lev_full(_p + wv * _c, _N - 1)
                    return le[-1] if ok_ else -1e18

                w_pred = golden_max(E_last, w_lo + eps, w_hi - eps)
                chan[p_geo] = w_pred
                stage = 1
            else:
                if p_geo not in chan:
                    prev += s["mu"] * s["cu"]
                    continue
                w_pred = chan[p_geo] * p_geo ** (-(k_geo - 1) / 2.0)
                stage = 2
            rows.append(dict(iw=iw, n=s["n"], stage=stage,
                             ratio=w_pred / s["mu"]))
            prev += s["mu"] * s["cu"]
    print("   %d predictions (%.0fs); ZERO fitted parameters, no "
          "window scalar" % (len(rows), time.time() - t2))
    rat = np.array([r["ratio"] for r in rows])
    med_all = float(np.median(rat))
    max_all = float(np.max(np.abs(rat - 1.0)))
    r1 = np.array([r["ratio"] for r in rows if r["stage"] == 1])
    r2 = np.array([r["ratio"] for r in rows if r["stage"] == 2])
    print("   overall: median %.5f  max|r-1| %.5f" % (med_all,
                                                      max_all))
    print("   stage 1 (first births, %d): median %.5f  max|r-1| "
          "%.5f" % (len(r1), float(np.median(r1)),
                    float(np.max(np.abs(r1 - 1)))))
    print("   stage 2 (repetitions, %d): median %.5f  max|r-1| "
          "%.5f" % (len(r2), float(np.median(r2)),
                    float(np.max(np.abs(r2 - 1)))))
    pp_dev = {}
    for n_t in PP_TRACK:
        devs = [abs(r["ratio"] - 1) for r in rows if r["n"] == n_t]
        pp_dev[n_t] = max(devs) if devs else float("nan")
        print("   outlier n=%3d: |r-1| across windows max %.5f  %s"
              % (n_t, pp_dev[n_t],
                 ["%.4f" % (r["ratio"]) for r in rows
                  if r["n"] == n_t]))
    per_w = []
    for iw in range(5):
        rw = np.array([r["ratio"] for r in rows if r["iw"] == iw])
        per_w.append((float(np.median(rw)),
                      float(np.max(np.abs(rw - 1.0)))))
        print("   window %d: median %.5f  max|r-1| %.5f  (%d slots)"
              % (iw, per_w[-1][0], per_w[-1][1], len(rw)))
    worst = sorted(rows, key=lambda r: -abs(r["ratio"] - 1.0))[:8]
    print("   worst remaining: %s"
          % [(r["iw"], r["n"], "S%d" % r["stage"],
              round(r["ratio"], 4)) for r in worst])
    check("H2.1 [M] two-stage prediction measured on %d pairs: "
          "median %.5f (memo target |med-1| < 0.1%%), max|r-1| "
          "%.5f (target < 1%%); stage-2 max %.5f"
          % (len(rows), med_all, max_all,
             float(np.max(np.abs(r2 - 1)))), len(rows) >= 190)
    heal_ok = all(pp_dev[n_t] < 0.01 for n_t in PP_TRACK)
    check("H2.2 [M] outlier healing: 16/64/81 max deviations "
          "%.5f / %.5f / %.5f (kill bar 1%%) -> %s"
          % (pp_dev[16], pp_dev[64], pp_dev[81],
             "HEALED" if heal_ok else "NOT healed"), True)
    scalar_needed = any(abs(m - 1.0) > 0.01 for (m, _mx) in per_w)
    check("H2.3 [M] leave-one-window-out transport: no fitted "
          "parameter exists; per-window medians %s -- a "
          "window-specific scalar would be needed: %s"
          % (["%.4f" % m for (m, _mx) in per_w],
             "YES" if scalar_needed else "NO"), True)

    # ============================================================== H3
    print("\nH3 -- kill adjudication (memo wording)")
    kill_pp = not heal_ok
    kill_max = max_all > 0.02
    kill_scal = scalar_needed
    passed = (abs(med_all - 1.0) < 0.001) and (max_all < 0.01)
    if kill_pp or kill_max or kill_scal:
        reasons = []
        if kill_pp:
            reasons.append("16/64/81 remain > 1%")
        if kill_max:
            reasons.append("max overall %.4f > 2%%" % max_all)
        if kill_scal:
            reasons.append("window scalar needed")
        VERDICT = "P1-TWO-STAGE-DEAD (%s)" % "; ".join(reasons)
    elif passed:
        VERDICT = ("P1-TWO-STAGE-PASS (median %.5f, max %.5f -- "
                   "conditioned closure: first births arithmetic-"
                   "free + repetitions from counting; NOT an "
                   "autonomous generator, 5e verifier boundary "
                   "declared)" % (med_all, max_all))
    else:
        VERDICT = ("P1-TWO-STAGE-MARGINAL (median %.5f, max %.5f: "
                   "no memo kill fires, pass bars not all met)"
                   % (med_all, max_all))
    check("H3.1 [M] preregistered adjudication: %s" % VERDICT, True)

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
