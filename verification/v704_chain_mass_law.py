#!/usr/bin/env python3
"""v704 -- PRIME.CHAINMASS.01: S-B, THE G1 EXACTNESS HUNT: does a
CLOSED formula (no per-slot fit, no per-window scalar) predict the
counting mass w_n = 2 Lambda(n)/sqrt(n) from the background flow
alone?

EXPLORATION ONLY (experiments/ firewall): nothing here is a
verification claim; no verification/, paper, ledger or website surface
is touched; no marker moves; NO RH statement.  File prefix chain_ to
avoid collision with the parallel beam-search worker (z1_* names).

CONTEXT [E-corpus].  z1_uvarov/z1_flow established: the slot identity
Delta alpha_{m0-1} = w1/E_{m0-1} is exact; the NAIVE stabilization law
mu_C0 = "the mass that zeroes the slot reflection" recovers the true
mass with median ratio ~1.026 (window 4); the SHOOTING mass (survival
bisection) recovers it to ~0.11% median.  Gap G1: close 1.026 -> 1.000
with a closed formula.

CANDIDATES (all closed characterizations of mu, conditioned on the
exact past; m_lo = first cell touched by the atom read, m_hi = last):
  C0 zero the reflection at the DOMINANT cell step ist
     (the 5c/5d naive law -- baseline, must reproduce ~1.026);
  C1 zero the reflection at step m_hi + 1 (first step past the full
     atom support: the next-Levinson-order law, includes the
     second-cell mass split exactly);
  C2 zero the reflection at step m_hi + 2 (one order further);
  C5 zero the SUM of reflections over steps ist .. m_hi + 1
     (balanced-divergence law);
  C7 C0 x (1 - alpha_bg^2) (algebraic E-update correction,
     closed guess);
  C3 MINIMAX: minimize max |k_n| over the ramp to the NEXT slot
     (the flow-optimum re-characterized as a closed variational
     principle; needs the future only through the ramp WINDOW,
     no future atom data -- the background between slots is
     arch+pole only).

BARS (declared before any number):
  B0 baseline sanity: median ratio mu_C0/mu_true on window 4 in
     [1.00, 1.06] (5d reproduction band).
  B1 G1-CLOSED iff some candidate has max |ratio - 1| < 0.1%
     UNIFORMLY over all slots (u <= log 120) on window 4 AND its
     window-0/2 medians agree with window 4 within a factor 2 of
     the deviation (transportability, no per-window scalar).
  B2 otherwise G1-OPEN: report the best closed law, its residual
     characteristics (median/IQR/max), and the residual correlation
     DIAGNOSTIC against closed flow quantities (alpha_bg^2,
     E-gradient, slot-gap term, second-cell ratio) -- typed as
     diagnostic, NOT as a fitted law.

FIREWALL: AST-checked -- no zetazero/nzeros/zeta anywhere; the true
masses MU_ALL enter ONLY as the comparison target (they are exact
arithmetic Lambda(n), not zero data).  v563 imported READ-ONLY.

Provenance (read-only): z1_uvarov_probe (slot identity),
z1_flow_recursion_probe (shooting 0.11%, naive 1.026), v563 core.

PROVENANCE: discovery probe chain_mass_law_probe.py (2026-08-03,
5/5 PASS, verdict G1-OPEN: the best closed law is C2 (the next
Levinson order), median ratio 0.9947, max|ratio-1| = 0.3130 on the
soft slots -- no closed formula reaches the 0.1% bar; the residual
strata are declared).  Promoted verbatim; numbers unchanged.
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

U_SLOTS = math.log(120.0)
BAR_CLOSED = 1e-3            # 0.1% uniform => G1 closed
BASE_BAND = (1.00, 1.06)     # 5d naive-law reproduction band
WIN_SET = (0, 2, 4)


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
    c_at, _ = core.atom_lags_at(alpha, M, core.U_ALL[:ka],
                                core.MU_ALL[:ka])
    cp = pole_lags(M, D)
    return dict(kz=kz, alpha=alpha, M=M, D=D, ka=ka,
                p_sm=c_ar + cp, p=c_ar + cp + c_at)


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
                        m_lo=int(nz[0]), m_hi=int(nz[-1])))
    return out


class LevSnap:
    """Levinson state snapshot at step n0 (a-vector, E, k-history);
    supports cheap re-extension with modified lags."""

    def __init__(self, r, n0):
        r = np.asarray(r, float)
        a = np.zeros(n0 + 1)
        a[0] = 1.0
        E = float(r[0])
        ks = []
        for n in range(1, n0 + 1):
            acc = r[n] + (float(a[1:n] @ r[n - 1:0:-1])
                          if n > 1 else 0.0)
            k = -acc / E
            a[1:n + 1] = a[1:n + 1] + k * a[n - 1::-1][:n]
            E *= (1.0 - k * k)
            ks.append(k)
            if not (abs(k) < 1.0) or E <= 0.0:
                raise RuntimeError("background breakdown at %d" % n)
        self.a = a
        self.E = E
        self.n0 = n0

    def extend(self, r_mod, n_steps):
        """Extend with modified lags; returns list of k values (may
        stop early on breakdown, padded with +-2 sentinels)."""
        n0 = self.n0
        a = np.zeros(n0 + n_steps + 1)
        a[:n0 + 1] = self.a
        E = self.E
        ks = []
        for n in range(n0 + 1, n0 + n_steps + 1):
            acc = r_mod[n] + float(a[1:n] @ r_mod[n - 1:0:-1])
            k = -acc / E
            ks.append(k)
            a[1:n + 1] = a[1:n + 1] + k * a[n - 1::-1][:n]
            E *= (1.0 - k * k)
            if not (abs(k) < 1.0) or E <= 0.0:
                ks += [2.0] * (n0 + n_steps - n)
                break
        return ks


def root_secant(fun, x0, x1, iters=60, tol=1e-14):
    f0, f1 = fun(x0), fun(x1)
    for _ in range(iters):
        if f1 == f0:
            break
        x2 = x1 - f1 * (x1 - x0) / (f1 - f0)
        x0, f0, x1, f1 = x1, f1, x2, fun(x2)
        if abs(x1 - x0) <= tol * max(1.0, abs(x1)):
            break
    return x1


def golden_min(fun, lo, hi, iters=48):
    g = (math.sqrt(5.0) - 1.0) / 2.0
    a, b = lo, hi
    c, d = b - g * (b - a), a + g * (b - a)
    fc, fd = fun(c), fun(d)
    for _ in range(iters):
        if fc < fd:
            b, d, fd = d, c, fc
            c = b - g * (b - a)
            fc = fun(c)
        else:
            a, c, fc = c, d, fd
            d = a + g * (b - a)
            fd = fun(d)
    return 0.5 * (a + b)


def measure_window(w, verbose_tag):
    """All candidate masses per slot; returns dict cand -> ratios."""
    slots = slot_list(w)
    cur = w["p_sm"].copy()
    res = {c: [] for c in ("C0", "C1", "C2", "C5", "C7", "C3")}
    diag = []
    for j, s in enumerate(slots):
        bg = cur.copy()
        cur += s["mu"] * s["cu"]
        m_lo, m_hi, ist = s["m_lo"], s["m_hi"], s["ist"]
        gap_next = (slots[j + 1]["m_lo"] - m_hi) \
            if j + 1 < len(slots) else 40
        n_ext = min(gap_next + 2, w["M"] - 1 - m_lo)
        snap = LevSnap(bg, m_lo - 1)

        def kseq(mu_val, n_steps=n_ext):
            r_mod = bg + mu_val * s["cu"]
            return snap.extend(r_mod, n_steps)

        # step offsets inside kseq: entry 0 == step m_lo
        off_ist = ist - m_lo
        off_h1 = m_hi + 1 - m_lo
        off_h2 = m_hi + 2 - m_lo

        # C0: zero k at the dominant-cell step (linear in mu -> two
        # evaluations give the exact root)
        k_a = kseq(0.0, off_ist + 1)[off_ist]
        k_b = kseq(1.0, off_ist + 1)[off_ist]
        mu_c0 = -k_a / (k_b - k_a) if k_b != k_a else float("nan")
        res["C0"].append(mu_c0 / s["mu"])

        # C1/C2: zero k one/two steps past the atom support
        def make_f(off):
            def f(mu_val):
                ks = kseq(mu_val, off + 1)
                return ks[off]
            return f
        mu_c1 = root_secant(make_f(off_h1), 0.9 * mu_c0, 1.1 * mu_c0)
        mu_c2 = root_secant(make_f(off_h2), 0.9 * mu_c0, 1.1 * mu_c0)
        res["C1"].append(mu_c1 / s["mu"])
        res["C2"].append(mu_c2 / s["mu"])

        # C5: zero the summed reflection over ist .. m_hi+1
        def f_sum(mu_val):
            ks = kseq(mu_val, off_h1 + 1)
            return sum(ks[off_ist:off_h1 + 1])
        mu_c5 = root_secant(f_sum, 0.9 * mu_c0, 1.1 * mu_c0)
        res["C5"].append(mu_c5 / s["mu"])

        # C7: algebraic E-update correction of C0
        alpha_bg = k_a
        res["C7"].append(mu_c0 * (1.0 - alpha_bg ** 2) / s["mu"])

        # C3: minimax |k| over the ramp to the next slot
        def f_mm(mu_val):
            ks = kseq(mu_val, n_ext)
            return max(abs(x) for x in ks)
        mu_c3 = golden_min(f_mm, 0.5 * mu_c0, 1.5 * mu_c0)
        res["C3"].append(mu_c3 / s["mu"])

        diag.append(dict(n=s["n"], alpha_bg=alpha_bg,
                         r2=(s["cu"][m_hi] / s["cu"][ist]
                             if m_hi != ist else 0.0),
                         gap=gap_next,
                         resid=s["mu"] / mu_c3 - 1.0 if mu_c3 else
                         float("nan")))
    print("   %s: %d slots" % (verbose_tag, len(slots)))
    return res, diag


def stats(v):
    v = np.asarray(v, float)
    dev = np.abs(v - 1.0)
    return (float(np.median(v)), float(np.quantile(v, 0.25)),
            float(np.quantile(v, 0.75)), float(np.max(dev)))


def run():
    print("=" * 78)
    print("S-B CHAIN MASS LAW -- the G1 exactness hunt")
    print("=" * 78)

    check("G0.0 [E] AST firewall: no zeta/zero symbol anywhere "
          "(true masses enter only as the arithmetic comparison "
          "target Lambda(n))", ast_firewall(os.path.abspath(__file__)))

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
    wins = {i: build_win(kz) for i, (kz, _a, _M) in enumerate(picks)
            if i in WIN_SET}
    check("G0.1 [E] windows %s of the 5-window family rebuilt "
          "(h = %s)" % (list(WIN_SET),
                        [wins[i]["M"] // 2 for i in WIN_SET]), True)

    # ============================================================== B0
    print("\nB0 -- candidate laws on window 4 (all closed, no fit)")
    res4, diag4 = measure_window(wins[4], "window 4")
    print("   %-4s %-38s %-9s %-19s %-9s"
          % ("law", "definition", "median", "IQR", "max|r-1|"))
    DEFS = {"C0": "zero k at dominant cell (naive 5c/5d)",
            "C1": "zero k at m_hi+1 (next Levinson order)",
            "C2": "zero k at m_hi+2",
            "C5": "zero sum k over ist..m_hi+1",
            "C7": "C0 x (1 - alpha_bg^2)",
            "C3": "minimax |k| over ramp to next slot"}
    tab4 = {}
    for cd in ("C0", "C1", "C2", "C5", "C7", "C3"):
        md, q1, q3, mx = stats(res4[cd])
        tab4[cd] = (md, q1, q3, mx)
        print("   %-4s %-38s %-9.4f [%.4f, %.4f]  %-9.4f"
              % (cd, DEFS[cd], md, q1, q3, mx))
    md0 = tab4["C0"][0]
    check("B0.1 [M] baseline reproduction: naive-law median ratio "
          "%.4f inside the 5d band [%.2f, %.2f]"
          % (md0, BASE_BAND[0], BASE_BAND[1]),
          BASE_BAND[0] <= md0 <= BASE_BAND[1])

    # ============================================================== B1
    print("\nB1 -- G1 closure bar (0.1%% uniform) + transport")
    best = min(tab4, key=lambda c: tab4[c][3])
    closed4 = tab4[best][3] < BAR_CLOSED
    resT = {}
    for iw in (0, 2):
        resT[iw], _ = measure_window(wins[iw], "window %d" % iw)
    trans_ok = True
    for cd in ("C0", "C1", "C2", "C5", "C7", "C3"):
        m4 = tab4[cd][0]
        m0_, _, _, x0_ = stats(resT[0][cd])
        m2_, _, _, x2_ = stats(resT[2][cd])
        d4, d0, d2 = abs(m4 - 1), abs(m0_ - 1), abs(m2_ - 1)
        okc = (d0 <= 2 * max(d4, 1e-4) + 1e-4) and \
              (d2 <= 2 * max(d4, 1e-4) + 1e-4)
        if cd == best:
            trans_ok = okc
        print("   %-4s medians: win0 %.4f  win2 %.4f  win4 %.4f  "
              "(max|r-1| win0 %.4f, win2 %.4f)%s"
              % (cd, m0_, m2_, m4, x0_, x2_,
                 "   <- best" if cd == best else ""))
    verdict_closed = closed4 and trans_ok
    check("B1.1 [M] G1 bar: best closed law %s has max|ratio-1| = "
          "%.4f on window 4 (bar %.4f) with transport %s -> %s"
          % (best, tab4[best][3], BAR_CLOSED,
             "OK" if trans_ok else "BROKEN",
             "G1-CLOSED" if verdict_closed else "G1-OPEN"),
          True)

    # ============================================================== B2
    print("\nB2 -- residual characteristics of the best law "
          "(diagnostic, not a fitted law)")
    resid = np.array([1.0 / r - 1.0 for r in res4[best]])
    print("   residual (mu_true/mu_%s - 1): median %+.5f  IQR "
          "[%+.5f, %+.5f]  max|.| %.5f"
          % (best, float(np.median(resid)),
             float(np.quantile(resid, 0.25)),
             float(np.quantile(resid, 0.75)),
             float(np.max(np.abs(resid)))))
    quants = {
        "alpha_bg^2": np.array([d["alpha_bg"] ** 2 for d in diag4]),
        "|alpha_bg|": np.array([abs(d["alpha_bg"]) for d in diag4]),
        "cell ratio r2": np.array([d["r2"] for d in diag4]),
        "1/gap_next": np.array([1.0 / d["gap"] for d in diag4]),
        "log n": np.array([math.log(d["n"]) for d in diag4]),
    }
    for nameq, q in quants.items():
        if np.std(q) == 0 or np.std(resid) == 0:
            continue
        cc = float(np.corrcoef(q, resid)[0, 1])
        print("   corr(residual, %-13s) = %+.3f" % (nameq, cc))
    # conditioning stratification: the law target k = 0 is soft where
    # the background reflection is small (wide S-A corridor); split by
    # |alpha_bg| tertiles and report the uniform error per stratum
    ab = np.array([abs(d["alpha_bg"]) for d in diag4])
    t1, t2 = np.quantile(ab, [1.0 / 3.0, 2.0 / 3.0])
    for lab, mask in (("weak  |a_bg| (soft slots)", ab <= t1),
                      ("mid   |a_bg|", (ab > t1) & (ab <= t2)),
                      ("tight |a_bg| (hard slots)", ab > t2)):
        rr = np.abs(np.array(res4[best])[mask] - 1.0)
        print("   stratum %-26s: median|r-1| %.4f  max|r-1| %.4f "
              "(%d slots)" % (lab, float(np.median(rr)),
                              float(np.max(rr)), int(mask.sum())))
    worst = np.argsort(-np.abs(np.array(res4[best]) - 1.0))[:5]
    print("   worst slots (n, ratio, |alpha_bg|): %s"
          % [(diag4[i]["n"], round(res4[best][i], 4),
              round(abs(diag4[i]["alpha_bg"]), 5)) for i in worst])
    check("B2.1 [M] residual diagnostic printed (correlations against "
          "closed flow quantities; any exact second term must "
          "reproduce these signs)", True)

    print("\nVERDICT: %s" % ("G1-CLOSED via %s" % best
                             if verdict_closed else
                             "G1-OPEN (best closed law: %s, "
                             "max|ratio-1| %.4f)"
                             % (best, tab4[best][3])))
    dt = time.time() - T0
    if FAILS:
        print("RESULT: %d/%d checks passed -- FAILURES: %s  (%.1f s)"
              % (N_CHK - len(FAILS), N_CHK, ", ".join(FAILS), dt))
        return 1
    print("RESULT: ALL %d CHECKS PASSED  (%.1f s)" % (N_CHK, dt))
    return 0


if __name__ == "__main__":
    raise SystemExit(run())
