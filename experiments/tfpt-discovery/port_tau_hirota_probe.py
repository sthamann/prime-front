#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""port_tau_hirota_probe -- PRIME.PORT.HIROTA.01
(EXPLORATION ONLY, experiments/; round 44, the first concrete
step of the review's Painleve route PRIME.PORT.PAINLEVE.01:
derive and test the BILINEAR (Desnanot-Jacobi / Hirota-type)
recurrence of the port tau function -- the exact nonlinear
structure that replaces further matrix bounds, 2026-08-09.)

THE EXACT ALGEBRA (frozen).  For ANY square matrix N of size
n >= 2 the Desnanot-Jacobi (Dodgson / Lewis Carroll) identity
holds EXACTLY:

    det(N) det(N^{1,n}_{1,n})
        = det(N^1_1) det(N^n_n) - det(N^1_n) det(N^n_1),

where N^i_j deletes row i and column j (and N^{1,n}_{1,n}
deletes rows 1, n and columns 1, n; det of the empty 0x0
matrix := 1).  Applied to the NESTED LEADING SECTIONS of the
fixed-window operator M_h = I - C_h (12 x 12, the compressed
window of PRIME.PORT.COCYCLE.01 that carries the wall exactly)
with principal minors tau^{(k)}_h := det of the leading k x k
section: the standard OPRL/Toda connection makes the minor
ladder a discrete Toda / Hirota system -- the DJ identity is
the in-rung bilinear skeleton, and the open question (the new
content) is whether an ACROSS-RUNG bilinear closure exists:

    tau^{(k)}_{h+1} tau^{(k)}_{h-1}
        - A_k tau^{(k+1)}_h tau^{(k-1)}_h
        - B_k (tau^{(k)}_h)^2  =  0            (Hirota form)

with h-independent coefficients A_k, B_k.  The review demands
the equation FOLLOW from the IIKS generators, not be assumed:
a fitted closure here is only the EXISTENCE SIGNAL.

MACHINERY (reused verbatim, declared): the Schur-compressed
fixed-window 12 x 12 matrices C_J(h) on J = {2, 4, ..., 24}
(PRIME.PORT.COCYCLE.01 / feshbach_hessian_probe pipeline);
the exact determinant chain and the Jacobi variational ward
d/ds log det(I - s D_P) = -tr[(I - s D_P)^{-1} D_P] were
established in port_tau_determinant_probe (PRIME.PORT.TAU.01).
Known input (feshbach_hessian_probe): the 11-dim complement
block of M_h is near-singular at depth (PD margin is tau-scale)
-- the DJ structure must respect that, so all wards are scaled
by the LARGEST participating term, never by the (near-
cancelling) left side alone.  v563 READ-ONLY.

FROZEN PROTOCOL (2026-08-09; ladder h <= 900; the 37 full-
window rungs exactly as in feshbach_hessian_probe F2.0; frozen
+ SHA-hashed before first run):

 P1  THE MINOR LADDER: per full-window rung compute the nested
     principal minors tau^{(k)}_h, k = 1..12, of M_h = I - C_h
     and ALL DJ corner minors.  Ward W1 (kill KW): the DJ
     identity holds on every rung and every section size
     n = 2..12 at machine precision -- scaled residual
     |lhs - rhs| / max(|t1|, |t2|, |lhs|, 1e-300) <= 1e-9
     (t1, t2 the two right-side products; the scale choice is
     the near-singular-complement lesson above).  SIGN CENSUS
     (typed, never kills): MINORS-POSITIVE iff tau^{(k)}_h > 0
     for EVERY rung and every k (total positivity of the
     leading-section family -- a strictly stronger finite
     statement than the wall scalar tau^{(12)} > 0); else
     MINORS-MIXED (census of negative (kz, k) printed).

 P2  THE h-DIRECTION BILINEAR TEST (the new content): order the
     37 rungs by h (frozen; the h-grid is NON-UNIFORM -- said
     so; A_k, B_k absorb the mean spacing and the non-
     uniformity is a known confounder of this measurement).
     For every k = 2..11 and every interior triple
     (h_{t-1}, h_t, h_{t+1}) form the gauge-normalized
     variables y_t = tau^{(k)}_{t+1} tau^{(k)}_{t-1} /
     (tau^{(k)}_t)^2 and x_t = tau^{(k+1)}_t tau^{(k-1)}_t /
     (tau^{(k)}_t)^2 and fit y = A_k x + B_k by least squares
     over the 35 triples.  Residual per triple: |y - A x - B| /
     (|y| + |A x| + |B| + 1e-300).  STABILITY (frozen): refit
     on the first 17 and last 18 triples; per k the relative
     change max(|dA|, |dB|) / max(|A|, |B|, 1e-30); STABLE iff
     the median over k <= 0.5.  TRIVIAL-CLOSURE REFEREE
     (frozen, honesty): also fit the A = 0 model (y = B only);
     report the improvement ratio median res(B-only) /
     median res(full) per k -- if the full fit does not beat
     the trivial smooth-ladder closure, the tau^{(k +/- 1)}
     coupling is NOT detected and closure is only the
     smoothness of the ladder (printed loudly).  TYPE: HIROTA-
     CLOSED iff overall median relative residual <= 0.1 AND
     STABLE; else HIROTA-OPEN (honest: a fitted closure is
     only the existence signal; the review demands derivation
     from the IIKS generators).

 P3  THE s-DIRECTION FAMILY (IIKS derivation seed, report):
     on the frozen rungs kz {12, 20, 26, 40, 52}, the s-family
     M_h(s) = I - s C_h at s in {0.5, 0.9, 1.0}.  Ward W2
     (kill KW): DJ holds at every s on every frozen rung
     (same bar as W1).  INTEGRABILITY SIGNAL (report): at
     s = 0.9, per k = 2..11, central differences (ds = 1e-3)
     of P(s) = tau^{(k+1)}(s) tau^{(k-1)}(s) and Q(s) =
     (tau^{(k)}(s))^2; the cancellation ratio |P' - Q'| /
     (|P'| + |Q'|) measures whether the s-derivative of the
     bilinear combination P - Q vanishes faster than its parts
     (the Toda-flow compatibility signal); median printed.

 P4  POSITIVE-INVARIANCE READING (report only): IF P1 =
     MINORS-POSITIVE on all rungs, state the finite theorem
     candidate -- 'the leading-section family of M_h is
     totally positive in the window; the Hirota flow preserves
     the positive cone' -- as the named next contract
     PRIME.PORT.HIROTA.POSCONE.01 (NO proof here; the honest
     reading and what it would need are printed).

 C   CONTROLS (kz 9, must fire; value control): Epstein and
     scramble combs -- fires iff the fixed 12-window is
     UNAVAILABLE (frame death) OR the minor ladder is NOT all
     positive (minor positivity is the value content).  The DJ
     identity itself PERSISTS on controls (it is algebra) --
     checked and printed, NOT a firing channel.

KILLS: KP pipeline (full-window census != 37 / Lanczos
breakdown) -> PIPELINE-BROKEN; KW wards (W1/W2 DJ residual) ->
WARD-BROKEN; KC controls silent -> CONTROL-DEAD.  P1/P2 types
and P3 signals are TYPED / reported, never kill.

VERDICT (frozen enum): HIROTA-MEASURED (+ typed sublabels
MINORS-POSITIVE / MINORS-MIXED and HIROTA-CLOSED /
HIROTA-OPEN) / PIPELINE-BROKEN / WARD-BROKEN / CONTROL-DEAD.

HONEST FRAME: this probe MEASURES the bilinear structure; it
does not derive it.  HIROTA-OPEN is a fully honest outcome
(the closure must come from the IIKS generators, contract
PRIME.PORT.PAINLEVE.01).  NO RH claim.  No marker moves.

FIREWALL: no zeros, no prime oracles (AST scan; banned:
zetazero/nzeros/primerange/isprime/primepi/nextprime/prevprime);
v563 READ-ONLY; RNG only in the declared scramble control;
stdout only.

Sources (read-only): v563_paper2_readouts;
port_cocycle_window_probe (C_J machinery, VERBATIM);
feshbach_hessian_probe (pipeline + ladder scope, VERBATIM);
port_tau_determinant_probe (determinant chain, variational
ward -- declared input, not re-run).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/port_tau_hirota_probe.py
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

JWIN = tuple(range(2, 25, 2))
N_FULLWIN_FROZEN = 37
NW = 12
S_RUNGS = (12, 20, 26, 40, 52)
S_FAMILY = (0.5, 0.9, 1.0)
DS = 1e-3
DJ_BAR = 1e-9
RES_BAR = 0.1
STAB_BAR = 0.5
BANNED_IDS = ("zetazero", "nzeros", "primerange", "isprime",
              "primepi", "nextprime", "prevprime")

CHECKS = []
KILLS = []
T0 = time.time()


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


# ---- shared machinery, VERBATIM from the round-39/42 chain ----

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


def rung_data(kz, scramble_seed=None, comb=None):
    rr = core.build_window(kz, scramble_seed=scramble_seed)
    h, M, D, alpha = rr["h"], rr["M"], rr["D"], rr["alpha"]
    uu = np.asarray(rr["uu"], float)
    mm = 2.0 * np.asarray(rr["lam"], float)
    if comb is not None:
        uu, mm = comb
    c_at, _ = core.atom_lags_at(alpha, M, uu, mm)
    c_ar = np.asarray(core.arch_lags(M, D), float)
    d = grid_density(c_ar + np.asarray(c_at, float))
    return dict(d=d, L=2 * M - 2, h=h, alpha=alpha)


def pipeline(d_total, h):
    """Folded measure -> Lanczos -> E -> 12-window Schur C_J.
    Returns C_J or a typed string (VERBATIM structure of the
    feshbach_hessian_probe pipeline, C_J only)."""
    L = len(d_total)
    xs, ws, _ = folded_measure(d_total, L, +1.0)
    ys, vs, uf_n = folded_measure(d_total, L, -1.0)
    al, be, m0, steps = lanczos_chain(xs, ws, h + 1)
    if steps < h + 1 or np.any(be <= 0):
        return "LANCZOS-BREAK"
    Pn = eval_chain(al, be, m0, ys, h)
    E = np.sqrt(vs)[:, None] * (Pn @ Pn.T) * np.sqrt(vs)[None, :]
    E = 0.5 * (E + E.T)
    idx = {int(j): k for k, j in enumerate(uf_n)}
    jav = [j for j in JWIN if j in idx]
    if len(jav) < NW:
        return "WINDOW-SHORT:%d" % len(jav)
    iw = [idx[j] for j in jav]
    io = [k for k in range(E.shape[0]) if k not in set(iw)]
    Eo = E[np.ix_(io, io)]
    IO = np.eye(len(io)) - Eo
    Ex = E[np.ix_(iw, io)]
    CJ = E[np.ix_(iw, iw)] + Ex @ np.linalg.solve(IO, Ex.T)
    return 0.5 * (CJ + CJ.T)


# ---- the minor ladder + Desnanot-Jacobi ----

def minors_of(Mh):
    """Leading principal minors tau^{(k)}, k = 1..NW."""
    return np.array([float(np.linalg.det(Mh[:k, :k]))
                     for k in range(1, NW + 1)])


def dj_residual(Mh):
    """Max scaled Desnanot-Jacobi residual over the leading
    sections n = 2..NW of Mh.  Scale = max(|t1|, |t2|, |lhs|)
    (frozen: never the near-cancelling left side alone)."""
    worst = 0.0
    for n in range(2, NW + 1):
        N = Mh[:n, :n]
        inner = (float(np.linalg.det(N[1:-1, 1:-1]))
                 if n > 2 else 1.0)
        lhs = float(np.linalg.det(N)) * inner
        t1 = (float(np.linalg.det(N[1:, 1:]))
              * float(np.linalg.det(N[:-1, :-1])))
        t2 = (float(np.linalg.det(N[1:, :-1]))
              * float(np.linalg.det(N[:-1, 1:])))
        scale = max(abs(t1), abs(t2), abs(lhs), 1e-300)
        worst = max(worst, abs(lhs - (t1 - t2)) / scale)
    return worst


def fit_bilinear(y, x):
    """LS fit y = A x + B; returns A, B, per-triple residuals."""
    G = np.column_stack([x, np.ones(len(x))])
    coef, *_ = np.linalg.lstsq(G, y, rcond=None)
    A, B = float(coef[0]), float(coef[1])
    res = np.abs(y - G @ coef) / (np.abs(y) + np.abs(A * x)
                                  + abs(B) + 1e-300)
    return A, B, res


def main():
    section("PRIME.PORT.HIROTA.01 -- the bilinear (Desnanot-"
            "Jacobi / Hirota) recurrence of the port tau "
            "function (EXPLORATION ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s"
          % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
    print("    NO RH claim; no marker moves.")
    print("\nS0 -- firewall")
    check("S0.1 AST firewall clean", not ast_scan(BANNED_IDS))

    # ---------------- P1: the minor ladder ---------------------
    section("P1 -- the minor ladder: nested principal minors of "
            "M_h = I - C_h + the DJ ward (all 37 full-window "
            "rungs)")
    rungs = {}
    short = []
    for kz in core.frame_a_zones():
        b = rung_data(kz)
        if b["h"] > 900:
            continue
        CJ = pipeline(b["d"], b["h"])
        if isinstance(CJ, str):
            short.append((kz, CJ))
            continue
        Mh = np.eye(NW) - CJ
        rungs[kz] = dict(b=b, CJ=CJ, Mh=Mh, taus=minors_of(Mh),
                         dj=dj_residual(Mh))
    print("    full-window rungs: %d | window-short (typed, "
          "excluded): %s"
          % (len(rungs), ["kz%d %s" % t for t in short]))
    check("P1.0 ladder census %d == %d (frozen)"
          % (len(rungs), N_FULLWIN_FROZEN),
          len(rungs) == N_FULLWIN_FROZEN, kill="KP")
    if len(rungs) < 6:
        return finish("n/a", "n/a")

    order = sorted(rungs, key=lambda k: rungs[k]["b"]["h"])
    print("\n    %-4s %-5s %-7s %-12s %-12s %-9s  %s"
          % ("kz", "h", "alpha", "tau^(12)", "min minor",
             "DJ resid", "sign ladder k=1..12"))
    dj_max = 0.0
    neg_census = []
    for kz in order:
        r = rungs[kz]
        taus = r["taus"]
        dj_max = max(dj_max, r["dj"])
        signs = "".join("+" if t > 0 else "-" for t in taus)
        for k in np.nonzero(taus <= 0)[0]:
            neg_census.append((kz, int(k) + 1))
        print("    %-4d %-5d %-7.3f %-12.3e %-12.3e %-9.1e  %s"
              % (kz, r["b"]["h"], r["b"]["alpha"],
                 taus[-1], float(np.min(taus)), r["dj"], signs))
    check("W1 DESNANOT-JACOBI EXACT on every rung and every "
          "section n = 2..12: max scaled residual %.1e <= %.0e"
          % (dj_max, DJ_BAR), dj_max <= DJ_BAR, kill="KW")
    minors_pos = len(neg_census) == 0
    sub1 = "MINORS-POSITIVE" if minors_pos else "MINORS-MIXED"
    check("P1.s sign census typed %s -- negative (kz, k): %s"
          % (sub1, neg_census if neg_census else "none"), True)

    # ---------------- P2: h-direction bilinear test ------------
    section("P2 -- the h-direction bilinear (Hirota-form) test: "
            "tau^(k)_{h+1} tau^(k)_{h-1} = A_k tau^(k+1)_h "
            "tau^(k-1)_h + B_k (tau^(k)_h)^2  (fitted; "
            "NON-UNIFORM h-grid, said so)")
    T = np.array([rungs[kz]["taus"] for kz in order])  # (37, 12)
    hs = [rungs[kz]["b"]["h"] for kz in order]
    print("    ladder: %d rungs, h = %d .. %d (non-uniform)"
          % (len(hs), hs[0], hs[-1]))
    print("\n    %-3s %-11s %-11s %-9s %-9s %-9s %-8s"
          % ("k", "A_k", "B_k", "med res", "max res",
             "stab dev", "triv/full"))
    all_res = []
    stab_devs = []
    improve = []
    for k in range(2, NW):          # tau^(k), k = 2..11 (1-based)
        i = k - 1                   # 0-based column of tau^(k)
        y = T[2:, i] * T[:-2, i] / T[1:-1, i] ** 2
        x = T[1:-1, i + 1] * T[1:-1, i - 1] / T[1:-1, i] ** 2
        A, B, res = fit_bilinear(y, x)
        nh = len(y) // 2
        A1, B1, _ = fit_bilinear(y[:nh], x[:nh])
        A2, B2, _ = fit_bilinear(y[nh:], x[nh:])
        sc = max(abs(A), abs(B), 1e-30)
        dev = max(abs(A1 - A2), abs(B1 - B2)) / sc
        # trivial-closure referee: A = 0 model
        Bt = float(np.mean(y))
        res_t = np.abs(y - Bt) / (np.abs(y) + abs(Bt) + 1e-300)
        imp = (float(np.median(res_t))
               / max(float(np.median(res)), 1e-300))
        all_res.extend(res.tolist())
        stab_devs.append(dev)
        improve.append(imp)
        print("    %-3d %+.4e %+.4e %-9.2e %-9.2e %-9.2f %-8.2f"
              % (k, A, B, float(np.median(res)),
                 float(np.max(res)), dev, imp))
    med_res = float(np.median(all_res))
    med_stab = float(np.median(stab_devs))
    stable = med_stab <= STAB_BAR
    med_imp = float(np.median(improve))
    check("P2.1 overall median relative residual %.2e (bar %.1f "
          "for closure)" % (med_res, RES_BAR), True)
    check("P2.2 coefficient stability: median half-split dev "
          "%.2f <= %.1f -> %s" % (med_stab, STAB_BAR,
                                  "STABLE" if stable else
                                  "UNSTABLE"), True)
    check("P2.3 trivial-closure referee: median improvement of "
          "the full fit over the A = 0 (smooth-ladder) model = "
          "%.2f x -- the tau^(k+/-1) coupling is %s"
          % (med_imp, "DETECTED" if med_imp >= 2.0 else
             "NOT detected (closure = ladder smoothness only)"),
          True)
    sub2 = ("HIROTA-CLOSED" if (med_res <= RES_BAR and stable)
            else "HIROTA-OPEN")
    check("P2.s bilinear closure typed %s (fitted closure is "
          "only the existence signal; derivation from the IIKS "
          "generators is PRIME.PORT.PAINLEVE.01)" % sub2, True)

    # ---------------- P3: s-direction family -------------------
    section("P3 -- the s-family M_h(s) = I - s C_h (IIKS "
            "derivation seed): DJ ward at s in %s + the "
            "integrability signal at s = 0.9" % (S_FAMILY,))
    dj_s_max = 0.0
    print("\n    %-4s %-5s | %-27s | %-9s" % (
        "kz", "h", "DJ resid at s = 0.5 / 0.9 / 1.0",
        "med cancel"))
    for kz in S_RUNGS:
        r = rungs[kz]
        djs = []
        for s in S_FAMILY:
            dv = dj_residual(np.eye(NW) - s * r["CJ"])
            djs.append(dv)
            dj_s_max = max(dj_s_max, dv)
        # integrability signal at s = 0.9 (central differences)
        tp = minors_of(np.eye(NW) - (0.9 + DS) * r["CJ"])
        tm = minors_of(np.eye(NW) - (0.9 - DS) * r["CJ"])
        cancels = []
        for k in range(2, NW):
            i = k - 1
            dP = ((tp[i + 1] * tp[i - 1])
                  - (tm[i + 1] * tm[i - 1])) / (2.0 * DS)
            dQ = (tp[i] ** 2 - tm[i] ** 2) / (2.0 * DS)
            cancels.append(abs(dP - dQ)
                           / (abs(dP) + abs(dQ) + 1e-300))
        print("    %-4d %-5d | %.1e / %.1e / %.1e         | "
              "%.3f"
              % (kz, r["b"]["h"], djs[0], djs[1], djs[2],
                 float(np.median(cancels))))
    check("W2 DJ EXACT along the s-family on every frozen rung: "
          "max scaled residual %.1e <= %.0e"
          % (dj_s_max, DJ_BAR), dj_s_max <= DJ_BAR, kill="KW")
    print("    (cancel = |P' - Q'| / (|P'| + |Q'|) at s = 0.9, "
          "P = tau^(k+1) tau^(k-1), Q = (tau^(k))^2; small = "
          "the s-derivative of the bilinear combination "
          "vanishes faster than its parts -- reported, no bar)")

    # ---------------- P4: positive-invariance reading ----------
    section("P4 -- positive-invariance reading (report only)")
    if minors_pos:
        print("""
    FINITE THEOREM CANDIDATE (named next contract
    PRIME.PORT.HIROTA.POSCONE.01, NO proof here): 'the leading-
    section family of M_h = I - C_h is totally positive in the
    fixed 12-window on every reachable rung; the Hirota flow
    preserves the positive cone.'  What it would need: (a) the
    across-rung bilinear closure DERIVED from the IIKS
    generators (PRIME.PORT.PAINLEVE.01), (b) positivity of the
    derived coefficients A_k, B_k (then tau^(k) > 0 propagates
    rung-to-rung by induction from one anchor rung), (c) the
    anchor-rung minors certified in interval arithmetic.  This
    would replace all further matrix bounds by a one-rung
    certificate + an algebraic invariance.""")
    else:
        print("    minor ladder is MIXED -- the positive-cone "
              "invariance reading does not apply (census in "
              "P1.s); the wall statement stays with tau^(12).")

    # ---------------- C: controls (kz 9) -----------------------
    section("C -- controls (kz 9; value control: minor "
            "positivity; DJ persists by algebra, not a firing "
            "channel)")
    rr9 = core.build_window(9)
    N_E = int(math.floor(math.exp(2.0 * rr9["alpha"]))) + 1
    lamE_ = lambda_eps(N_E)
    nn = np.nonzero(np.abs(lamE_) > 1e-12)[0]
    ok_ctl = True
    for nmc, kw in (("Epstein", dict(comb=(
            np.log(nn.astype(float)),
            2.0 * lamE_[nn] / np.sqrt(nn.astype(float))))),
            ("scramble", dict(scramble_seed=1))):
        b_c = rung_data(9, **kw)
        CJ = pipeline(b_c["d"], b_c["h"])
        if isinstance(CJ, str):
            print("    %-8s: %s -> fires via FRAME DEATH (the "
                  "fixed 12-window does not exist on this comb)"
                  % (nmc, CJ))
            continue
        Mh = np.eye(NW) - CJ
        taus = minors_of(Mh)
        djv = dj_residual(Mh)
        n_neg = int(np.sum(taus <= 0))
        fired = n_neg > 0
        ok_ctl &= fired
        print("    %-8s: negative minors %d/12 | min minor "
              "%+.3e | DJ resid %.1e (algebra persists: %s) "
              "-> %s"
              % (nmc, n_neg, float(np.min(taus)), djv,
                 djv <= DJ_BAR, "FIRES" if fired else "silent"))
    check("C1 CONTROLS FIRE (frame death / minor positivity "
          "broken)", ok_ctl, kill="KC")

    return finish(sub1, sub2)


def finish(sub1, sub2):
    section("V -- FROZEN VERDICT")
    n_pass = sum(1 for _n, okk in CHECKS if okk)
    n_tot = len(CHECKS)
    if KILLS:
        VERDICT = {"KP": "PIPELINE-BROKEN", "KW": "WARD-BROKEN",
                   "KC": "CONTROL-DEAD"}[KILLS[0]]
    else:
        VERDICT = "HIROTA-MEASURED"
    print("\n  VERDICT: %s (%s, %s)" % (VERDICT, sub1, sub2))
    print("""
  HONEST FRAME (as frozen): the DJ identity is algebra -- its
  ward protects the bookkeeping, it proves nothing about the
  wall.  The value content is (a) the minor-ladder sign census
  and (b) whether an across-rung bilinear closure EXISTS as a
  measurement.  The equation itself must FOLLOW from the IIKS
  generators (PRIME.PORT.PAINLEVE.01) before anything is
  claimed.  NO RH claim.  No marker moves.""")
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed"
          % (time.time() - T0, n_tot, n_tot - n_pass))
    return 0 if n_pass == n_tot else 1


if __name__ == "__main__":
    raise SystemExit(main())
