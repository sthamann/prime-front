#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""v890 -- PRIME.PORT.HIROTA.01 + PRIME.PORT.SFLOW.01 + PRIME.PORT.TAU.MOEBIUS.01: THE SURVIVING POSITIVITY ARCHITECTURE -- flag positivity (Sylvester) of the section family, the pole-free s-corridor, and the multi-factor tau anatomy, ONE module from three probes (10/10 + 7/7 + 14/14 checks, zero fails, verdicts HIROTA-MEASURED (MINORS-POSITIVE / HIROTA-OPEN) + SFLOW-MEASURED (TODA-VARYING(t = s) / CORRIDOR-CLEAR) + TAUMOEBIUS-MEASURED (BRIDGE-DIFFUSE / LINK-POSITIVE / SMOOTH-FLIP-DETECTED); discovery probes port_tau_hirota_probe.py, port_sflow_toda_probe.py, tau_mobius_factor_probe.py (SPEC v2), rounds 44/48, 2026-08-09, re-run identically at promotion, embedded BYTE-EXACT and executed verbatim, ~15 s).  (1) FLAG POSITIVITY OF THE SECTION FAMILY (hirota; Sylvester: all leading principal minors positive; typing corrected per the round-51 review -- classical total positivity of ALL minors is NOT claimed and untested): on all 37 full-window rungs EVERY nested leading principal minor tau^(k)_h of M_h = I - C_h (k = 1..12) is positive -- MINORS-POSITIVE, a strictly STRONGER finite statement than the wall scalar tau^(12) > 0 (and strictly weaker than classical total positivity); the Desnanot-Jacobi (Dodgson) bilinear identity holds EXACTLY on every rung, every section size and every s of the s-family (scaled residual <= 1e-9, the near-singular-complement scaling lesson of the Feshbach anatomy applied); the across-rung h-direction closure is typed HIROTA-OPEN honestly (median relative residual 0.655 vs the 0.1 bar, coefficients unstable across the half-split, and the trivial-closure referee finds the tau^(k +/- 1) coupling NOT detected -- what closes on the non-uniform h-grid is ladder smoothness only; the derivation from the IIKS generators remains the named contract PRIME.PORT.PAINLEVE.01), and the positive-cone reading is stated as the named candidate PRIME.PORT.HIROTA.POSCONE.01.  (2) THE POLE-FREE s-CORRIDOR (sflow): the per-section Jacobi variational identity d/ds log tau^(k) = -tr[M_k^{-1} C_k] is warded exactly (trace vs 4th-order FD rel <= 1e-8, spectral route <= 1e-9); on every full-window rung NO section minor crosses zero on the whole corridor s in [0, 1] from the trivial point to the wall (CORRIDOR-CLEAR), while the Epstein and scramble controls pull their pole INSIDE (s* <= 1); and the organizing pole identity is exact: by Cauchy interlacing the first zero of ANY section minor is s*_h = 1/lam_max(C_h), so s*_h - 1 = tau_h/(1 - tau_h) -- THE WALL MARGIN IS THE POLE DISTANCE of the s-flow, with the measured h-trend LS slope of log(s*_h - 1) against log h = -2.90; the Toda test itself selects the time t = s with best median residual 0.001 (well under the 0.05 bar) but the coefficients a_k drift across rungs -- typed TODA-VARYING(t = s), measured, not derived.  (3) THE MULTI-FACTOR TAU ANATOMY (tau moebius, reviewer probe 5 -- the key run): the exact factorization ledger Q_h = det(W_{h+1})/det(W_h) = prod_i (1 + mu_i) (mu_i the exactly-real eigenvalues of W_h^{-1} Delta C via the symmetric similarity; ward rel <= 1e-10 on every step) shows the TRUTH ladder keeping EVERY factor off -1 (Q_h > 0 and 1 + mu_soft > 0 on all 31 full-window truth steps, no sign flip anywhere), while the frame-surviving SMOOTH-MASS control world crosses factors on 22 of its 28 full-window steps (first factor crossing already at h 210 -> 218; its wall itself violated from the shallowest rung h 142 -- SMOOTH-FLIP-DETECTED, the arithmetic detector fires); the reviewer's one-scalar reduction is honestly CLOSED: BRIDGE-DIFFUSE (ladder-wide bulk factor margin 0.005 vs the frozen 0.5 bar -- the bulk product is NOT uniformly harmless, so sign(Q_h) does NOT reduce to one scalar per step), the contraction link is LINK-POSITIVE only (J_h > 0 on every step but neither lawful nor source-interpretable: sign(J_h - 1) constant on 0.58 vs the 0.90 bar), and the fitted Moebius datum carries essentially none of the determinant load (|alpha_h| ~ 0.002 inside identity noise, stated) -- POSITIVITY INHERITANCE IS A MULTI-FACTOR / TOTAL-POSITIVITY STATEMENT, exactly the object the hirota/sflow halves measure, not a scalar cocycle.  NET: the surviving architecture after the round-48 Moebius kills (v891) is the positive cone of the section family under the s-flow with the wall margin as pole distance -- the named open piece is the derivation of the bilinear/Toda closure from the IIKS generators.  NO RH claim; no marker moves; an exact factorization of window-determinant quotients on compressed truncations is a numerical measurement, not a theorem about zeros.  Float64 on the deployed v563 machinery (READ-ONLY); no zeros, no prime oracles (AST firewalls inside the probes); RNG only in declared scramble controls.  Python-only per GATE.WOLFRAM.02.

PROVENANCE: discovery probes port_tau_hirota_probe.py (10/10,
HIROTA-MEASURED (MINORS-POSITIVE, HIROTA-OPEN)),
port_sflow_toda_probe.py (7/7, SFLOW-MEASURED (TODA-VARYING(t=s),
CORRIDOR-CLEAR)), tau_mobius_factor_probe.py (14/14,
TAUMOEBIUS-MEASURED / BRIDGE-DIFFUSE / LINK-POSITIVE /
SMOOTH-FLIP-DETECTED, SPEC v2:
the C2 smooth-mass bookkeeping sizes W by the available window --
mechanical shape repair after run 1 crashed BEFORE any C2 typing;
every truth-side number unchanged by construction; plus the SPEC
v1 bookkeeping note: build_window called once per zone, comb
substitution after the build, predecessor code paths bit for bit),
all 2026-08-09, re-run identically at promotion.  ROUND-31
EMBEDDING CONVENTION: frozen sources embedded BYTE-EXACT, executed
verbatim in isolated namespaces; printed spec SHAs reproduce;
byte-equality ward vs experiments/tfpt-discovery/ inside the
pattern gates.  All probes consume the READ-ONLY deployed core
v563_paper2_readouts.py.

FIREWALL: no zeros, no prime-table oracles; all fail-first spec
amendments preserved; fitted closures typed as existence signals
only -- the IIKS derivation stays the named open contract.
NO RH claim.
"""

import contextlib
import io
import os
import re
import sys
import time
import types

_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)

# ------------- frozen probe source port_tau_hirota_probe (embedded BYTE-EXACT, raw string)
_SRC_0 = r'''
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
'''

# ------------- frozen probe source port_sflow_toda_probe (embedded BYTE-EXACT, raw string)
_SRC_1 = r'''
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""port_sflow_toda_probe -- PRIME.PORT.SFLOW.01
(EXPLORATION ONLY, experiments/; round 44, the continuation of
PRIME.PORT.HIROTA.01: derive and verify the EXACT s-direction
flow equations of the port tau minors from the IIKS/resolvent
structure and measure the positive-cone invariance from s = 0
(trivial, tau = 1) to s = 1 (the wall), 2026-08-09.)

THE EXACT MATH (frozen).  For the s-family M(s) = I - s C on
the fixed 12-window (C = C_J(h), the Schur-compressed window of
PRIME.PORT.COCYCLE.01) with nested leading principal minors
tau^{(k)}(s) := det(M(s)[:k, :k]) = det(I_k - s C_k):

 (i)  JACOBI, PER SECTION, EXACT:
          d/ds tau^{(k)}(s)
              = -tau^{(k)}(s) * tr[(M_k(s))^{-1} C_k],
      equivalently d/ds log tau^{(k)} = -tr[M_k^{-1} C_k]
      =: L_k(s), and d^2/ds^2 log tau^{(k)}
      = -tr[(M_k^{-1} C_k)^2] =: L'_k(s).  In the spectral
      form (lambda_i the eigenvalues of the SYMMETRIC C_k):
      log tau^{(k)} = sum_i log(1 - s lambda_i),
      L_k = -sum_i lambda_i / (1 - s lambda_i),
      L'_k = -sum_i lambda_i^2 / (1 - s lambda_i)^2.

 (ii) THE CLASSICAL TODA CONNECTION: the ratios
          r_k(s) := tau^{(k+1)} tau^{(k-1)} / (tau^{(k)})^2
      (tau^{(0)} := 1) are the standard tau-function variables;
      IF the section family follows a Toda-lattice flow in a
      time t(s), then the Toda bilinear identity holds:
          d^2/dt^2 log tau^{(k)} = a_k * r_k(s) + b_k
      with CONSTANT a_k, b_k along the flow.  Time candidates
      (frozen): t = s; t = log(1/(1-s)); t = log s, with the
      exact chain rule d^2/dt^2 f = (ds/dt)^2 f'' +
      (d^2 s/dt^2) f', i.e.
          t = s:            D2 = f''
          t = log(1/(1-s)): D2 = (1-s)^2 f'' - (1-s) f'
          t = log s:        D2 = s^2 f'' + s f''*0 + s f'
                               = s^2 f'' + s f'   (s > 0 only).

 (iii) THE POLE IDENTITY (elementary but organizing): by Cauchy
      interlacing lam_max(C_k) <= lam_max(C_12) = lam_max(C),
      so the FIRST zero of ANY section minor on s > 0 is the
      zero of tau^{(12)}:  s*_h = 1 / lam_max(C_h) EXACTLY
      (when lam_max > 0).  Hence s*_h - 1 = tau_h/(1 - tau_h)
      with the wall margin tau_h := 1 - lam_max(C_h): the wall
      margin IS the pole distance of the s-flow.  RH on the
      ladder = the pole of the s-flow stays outside [0, 1]
      uniformly.  NO RH claim follows from any finite window.

MACHINERY (reused VERBATIM, declared): the Schur-compressed
fixed-window 12 x 12 matrices C_J(h) on J = {2, 4, ..., 24}
(PRIME.PORT.COCYCLE.01 / feshbach_hessian_probe pipeline); the
Jacobi variational identity was established scalar-globally in
port_tau_determinant_probe (PRIME.PORT.TAU.01) -- here it is
verified PER SECTION.  Known input (port_tau_hirota_probe):
MINORS-POSITIVE at s = 1 on all 37 full-window rungs; DJ exact
in the s-family; the bilinear cancellation ratio in s improves
with depth (0.010 -> 0.000) -- the Toda compatibility lives in
the s-direction.  v563 READ-ONLY.

FROZEN PROTOCOL (2026-08-09; ladder h <= 900; the 37 full-
window rungs exactly as in feshbach_hessian_probe F2.0; frozen
+ SHA-hashed before first run):

 S1  EXACT VARIATIONAL WARD (kill KW): on the frozen heavy
     rungs kz {12, 20, 26, 40, 52} PLUS the 3 deepest full-
     window rungs by h (dedup), per section k = 1..12 and per
     s in {0.3, 0.6, 0.9}: the analytic derivative
     L_k = -tr[M_k^{-1} C_k] (trace route) against a 4th-order
     central finite difference of log tau^{(k)} (slogdet route,
     step 1e-3): rel = |L - FD| / max(|L|, 1e-30) <= 1e-8.
     Ward W2 (kill KW): the spectral route for L_k agrees with
     the trace route, rel <= 1e-9 (guards the S2 machinery).
     This is algebra; the ward guards the bookkeeping.

 S2  THE TODA TEST (the substance): on the frozen fine s-grid
     s_j = 0.999 * (1 - (1 - u_j)^2), u_j = j/199, j = 0..199
     (200 points, denser near 1), compute log tau^{(k)}(s) for
     k = 1..12 on the S1 rung set; per rung, per time candidate
     and per k = 1..11 (k = 12 has no right neighbor) fit
     D2_t log tau^{(k)} = a_k r_k + b_k by least squares over
     the grid (t = log s: s > 0 points only).  Residual per
     point: |y - a x - b| / (|y| + |a x| + |b| + 1e-300).
     Candidate score = median residual over (rungs, k, points);
     best candidate t* = argmin.  CROSS-RUNG STABILITY
     (frozen): per k the spread of a_k across rungs,
     (max - min) / max(|median|, 1e-30); STABLE iff the median
     over k <= 0.5.  TYPE: TODA-CLOSED(t*) iff best median
     residual <= 0.05 AND STABLE; TODA-VARYING(t*) iff best
     median residual <= 0.05 but coefficients drift across
     rungs; TODA-OPEN otherwise (all honest; a fitted closure
     is only the existence signal).

 S3  POLE-FREE CORRIDOR (the positivity reading): per full-
     window rung (all 37) track min_k tau^{(k)}(s) on the
     frozen grid UNION {1.0}: NO section minor may cross zero
     on [0, 1] (the s-deformation statement of the wall: the
     corridor from the trivial point to the wall is pole-free/
     sign-stable).  Print the closest approach min_{k,s}
     tau^{(k)} and where.  TYPE: CORRIDOR-CLEAR iff positive
     throughout on every tested rung; else CORRIDOR-CROSSED
     (census printed).  THEN the decisive structural readout:
     the same corridor for the EPSTEIN and SCRAMBLE controls
     (kz 9) -- the controls MUST cross before (or at) s = 1
     since their walls are violated; print s* per control
     (the 'pole position' that distinguishes truth from
     controls: the truth keeps the pole beyond s = 1, the
     controls pull it inside).

 S4  THE POLE-DISTANCE LAW (report only): per truth rung the
     EXACT pole s*_h = 1/lam_max(C_h) (symmetric eig; identity
     (iii)), the wall margin tau_h = 1 - lam_max, the exact
     relation s*_h - 1 = tau_h/(1 - tau_h), and the h-trend
     (LS slope of log(s*_h - 1) against log h).  The identity
     is elementary but organizing; stated honestly, no bar.

 C   CONTROLS (kz 9, must fire; kill KC): Epstein and scramble
     combs, covered structurally in S3 -- fires iff the fixed
     12-window is UNAVAILABLE (frame death) OR the control pole
     s* <= 1 (corridor crossed).  Pipeline persistence printed.

KILLS: KP pipeline (full-window census != 37 / Lanczos
breakdown) -> PIPELINE-BROKEN; KW wards (S1 variational /
spectral-trace agreement) -> WARD-BROKEN; KC controls silent ->
CONTROL-DEAD.  S2/S3 types and S4 are TYPED / reported, never
kill.

VERDICT (frozen enum): SFLOW-MEASURED (+ typed sublabels
TODA-CLOSED(t*) / TODA-VARYING(t*) / TODA-OPEN and
CORRIDOR-CLEAR / CORRIDOR-CROSSED) / PIPELINE-BROKEN /
WARD-BROKEN / CONTROL-DEAD.

HONEST FRAME: S1 and the pole identity are exact algebra --
their wards protect the bookkeeping, they prove nothing about
the wall.  The value content is (a) whether a Toda time
EXISTS in which the section flow closes bilinearly (measured,
not derived -- derivation from the IIKS generators remains
PRIME.PORT.PAINLEVE.01), and (b) the pole-free corridor with
the control pole positions.  NO RH claim.  No marker moves.

FIREWALL: no zeros, no prime oracles (AST scan; banned:
zetazero/nzeros/primerange/isprime/primepi/nextprime/prevprime);
v563 READ-ONLY; RNG only in the declared scramble control;
stdout only.

Sources (read-only): v563_paper2_readouts;
port_cocycle_window_probe (C_J machinery, VERBATIM);
feshbach_hessian_probe (pipeline + ladder scope, VERBATIM);
port_tau_determinant_probe (scalar variational ward, declared
input); port_tau_hirota_probe (minor ladder + s-family seed,
VERBATIM machinery).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/port_sflow_toda_probe.py
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
HEAVY_RUNGS = (12, 20, 26, 40, 52)
N_DEEPEST = 3
S_WARD = (0.3, 0.6, 0.9)
FD_H = 1e-3
WARD_BAR = 1e-8
SPEC_BAR = 1e-9
NGRID = 200
S_MAX = 0.999
TODA_RES_BAR = 0.05
TODA_STAB_BAR = 0.5
BANNED_IDS = ("zetazero", "nzeros", "primerange", "isprime",
              "primepi", "nextprime", "prevprime")

CHECKS = []
KILLS = []
AMENDMENTS = []
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


# ---- shared machinery, VERBATIM from the round-39/44 chain ----

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


# ---- s-flow machinery -----------------------------------------

def s_grid():
    """Frozen fine grid on [0, S_MAX], denser near 1."""
    u = np.linspace(0.0, 1.0, NGRID)
    return S_MAX * (1.0 - (1.0 - u) ** 2)


def section_eigs(CJ):
    """Eigenvalues of every leading section C_k, k = 1..NW."""
    return [np.linalg.eigvalsh(CJ[:k, :k]) for k in range(1, NW + 1)]


def spectral_flow(evs, ss):
    """Exact spectral route on the grid ss:
    logtau[k-1, j] = log tau^{(k)}(s_j),
    L[k-1, j]      = d/ds log tau^{(k)},
    Lp[k-1, j]     = d^2/ds^2 log tau^{(k)}.
    Returns (logtau, L, Lp, pos) -- pos = all 1 - s lam > 0."""
    G = len(ss)
    logtau = np.full((NW, G), np.nan)
    L = np.full((NW, G), np.nan)
    Lp = np.full((NW, G), np.nan)
    pos = True
    for k in range(NW):
        ev = np.asarray(evs[k], float)[:, None]
        q = 1.0 - ss[None, :] * ev
        if np.any(q <= 0.0):
            pos = False
            continue
        logtau[k] = np.sum(np.log(q), axis=0)
        L[k] = np.sum(-ev / q, axis=0)
        Lp[k] = np.sum(-(ev ** 2) / q ** 2, axis=0)
    return logtau, L, Lp, pos


def tau_grid(evs, ss):
    """tau^{(k)}(s_j) exactly (spectral product), (NW, G)."""
    T = np.empty((NW, len(ss)))
    for k in range(NW):
        ev = np.asarray(evs[k], float)[:, None]
        T[k] = np.prod(1.0 - ss[None, :] * ev, axis=0)
    return T


def d2_of_candidate(name, ss, L, Lp):
    """Exact chain rule: D2_t log tau from f' = L, f'' = Lp."""
    if name == "t=s":
        return Lp, np.ones(len(ss), bool)
    if name == "t=log(1/(1-s))":
        w = 1.0 - ss
        return (w ** 2)[None, :] * Lp - w[None, :] * L, \
            np.ones(len(ss), bool)
    if name == "t=log s":
        m = ss > 0.0
        return (ss ** 2)[None, :] * Lp + ss[None, :] * L, m
    raise ValueError(name)


def fit_affine(y, x):
    """LS fit y = a x + b; per-point relative residuals."""
    G = np.column_stack([x, np.ones(len(x))])
    coef, *_ = np.linalg.lstsq(G, y, rcond=None)
    a, b = float(coef[0]), float(coef[1])
    res = np.abs(y - G @ coef) / (np.abs(y) + np.abs(a * x)
                                  + abs(b) + 1e-300)
    return a, b, res


TIME_CANDIDATES = ("t=s", "t=log(1/(1-s))", "t=log s")


def main():
    section("PRIME.PORT.SFLOW.01 -- the exact s-direction flow "
            "of the port tau minors: variational ward, Toda "
            "time test, pole-free corridor (EXPLORATION ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s"
          % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
    print("    NO RH claim; no marker moves.")
    print("\nS0 -- firewall")
    check("S0.1 AST firewall clean", not ast_scan(BANNED_IDS))

    # ---------------- P0: build the ladder ---------------------
    section("P0 -- the fixed-window ladder (all full-window "
            "rungs, h <= 900; pipeline VERBATIM)")
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
        rungs[kz] = dict(b=b, CJ=CJ, evs=section_eigs(CJ))
    print("    full-window rungs: %d | window-short (typed, "
          "excluded): %s"
          % (len(rungs), ["kz%d %s" % t for t in short]))
    check("P0.1 ladder census %d == %d (frozen)"
          % (len(rungs), N_FULLWIN_FROZEN),
          len(rungs) == N_FULLWIN_FROZEN, kill="KP")
    if len(rungs) < 6:
        return finish("n/a", "n/a")
    order = sorted(rungs, key=lambda k: rungs[k]["b"]["h"])
    deepest = list(order[-N_DEEPEST:])
    s1_set = sorted(set(HEAVY_RUNGS) | set(deepest),
                    key=lambda k: rungs[k]["b"]["h"])
    print("    S1/S2 rung set (frozen rule: heavy %s + %d "
          "deepest by h, dedup): %s"
          % (list(HEAVY_RUNGS), N_DEEPEST,
             ["kz%d(h%d)" % (kz, rungs[kz]["b"]["h"])
              for kz in s1_set]))

    # ---------------- S1: exact variational ward ---------------
    section("S1 -- EXACT VARIATIONAL WARD: d/ds log tau^(k) = "
            "-tr[M_k(s)^{-1} C_k] per section, trace route vs "
            "4th-order FD of slogdet, at s in %s" % (S_WARD,))
    worst_fd = 0.0
    worst_sp = 0.0
    print("\n    %-4s %-5s %-11s %-11s" % (
        "kz", "h", "max|L-FD|/L", "max|L-spec|/L"))
    for kz in s1_set:
        r = rungs[kz]
        CJ = r["CJ"]
        w_fd = 0.0
        w_sp = 0.0
        for s0 in S_WARD:
            for k in range(1, NW + 1):
                Ck = CJ[:k, :k]
                Mk = np.eye(k) - s0 * Ck
                Lan = -float(np.trace(np.linalg.solve(Mk, Ck)))

                def f(s, Ck=Ck, k=k):
                    sg, ld = np.linalg.slogdet(np.eye(k) - s * Ck)
                    assert sg > 0.0
                    return ld

                fd = (-f(s0 + 2 * FD_H) + 8.0 * f(s0 + FD_H)
                      - 8.0 * f(s0 - FD_H) + f(s0 - 2 * FD_H)) \
                    / (12.0 * FD_H)
                sc = max(abs(Lan), 1e-30)
                w_fd = max(w_fd, abs(Lan - fd) / sc)
                ev = r["evs"][k - 1]
                Lsp = -float(np.sum(ev / (1.0 - s0 * ev)))
                w_sp = max(w_sp, abs(Lan - Lsp) / sc)
        worst_fd = max(worst_fd, w_fd)
        worst_sp = max(worst_sp, w_sp)
        print("    %-4d %-5d %-11.1e %-11.1e"
              % (kz, r["b"]["h"], w_fd, w_sp))
    check("W1 JACOBI PER SECTION: analytic vs FD4, worst rel "
          "%.1e <= %.0e (k = 1..12, s in %s, %d rungs)"
          % (worst_fd, WARD_BAR, S_WARD, len(s1_set)),
          worst_fd <= WARD_BAR, kill="KW")
    check("W2 SPECTRAL = TRACE route, worst rel %.1e <= %.0e "
          "(guards the S2 machinery)" % (worst_sp, SPEC_BAR),
          worst_sp <= SPEC_BAR, kill="KW")

    # ---------------- S2: the Toda test -------------------------
    section("S2 -- THE TODA TEST: D2_t log tau^(k) = a_k r_k + "
            "b_k with constant a_k, b_k?  (frozen grid, %d "
            "points on [0, %.3f], denser near 1; candidates %s)"
            % (NGRID, S_MAX, list(TIME_CANDIDATES)))
    ss = s_grid()
    flows = {}
    for kz in s1_set:
        lt, L, Lp, pos = spectral_flow(rungs[kz]["evs"], ss)
        flows[kz] = dict(lt=lt, L=L, Lp=Lp, pos=pos)
        if not pos:
            print("    NOTE kz %d: nonpositive section minor on "
                  "the grid -- excluded from the fit (corridor "
                  "census in S3)" % kz)
    fit_rungs = [kz for kz in s1_set if flows[kz]["pos"]]
    cand_stats = {}
    for cname in TIME_CANDIDATES:
        res_all = []
        a_by_k = {k: [] for k in range(1, NW)}
        med_by_rung = []
        for kz in fit_rungs:
            fl = flows[kz]
            D2, m = d2_of_candidate(cname, ss, fl["L"], fl["Lp"])
            # log tau^(0) := 0 row prepended for r_k, k = 1..11
            LT = np.vstack([np.zeros(len(ss)), fl["lt"]])
            res_rung = []
            for k in range(1, NW):        # tau^(k), k = 1..11
                x = np.exp(LT[k + 1, m] + LT[k - 1, m]
                           - 2.0 * LT[k, m])
                y = D2[k - 1, m]
                a, b, res = fit_affine(y, x)
                a_by_k[k].append(a)
                res_all.extend(res.tolist())
                res_rung.extend(res.tolist())
            med_by_rung.append(float(np.median(res_rung)))
        spreads = []
        for k in range(1, NW):
            av = np.asarray(a_by_k[k], float)
            spreads.append(
                float(av.max() - av.min())
                / max(abs(float(np.median(av))), 1e-30))
        cand_stats[cname] = dict(
            med=float(np.median(res_all)),
            mx=float(np.max(res_all)),
            med_rung=med_by_rung,
            spread=float(np.median(spreads)),
            a_by_k=a_by_k)
    print("\n    %-16s %-9s %-9s %-11s %s" % (
        "candidate", "med res", "max res", "a_k spread",
        "per-rung median residuals"))
    for cname in TIME_CANDIDATES:
        st = cand_stats[cname]
        print("    %-16s %-9.3f %-9.3f %-11.3f %s"
              % (cname, st["med"], st["mx"], st["spread"],
                 " ".join("%.3f" % v for v in st["med_rung"])))
    best = min(TIME_CANDIDATES, key=lambda c: cand_stats[c]["med"])
    bst = cand_stats[best]
    stable = bst["spread"] <= TODA_STAB_BAR
    print("\n    best candidate: %s (median residual %.3f; "
          "cross-rung a_k spread %.3f, bar %.1f)"
          % (best, bst["med"], bst["spread"], TODA_STAB_BAR))
    print("    %-3s %-13s %-11s" % ("k", "median a_k", "spread"))
    for k in range(1, NW):
        av = np.asarray(bst["a_by_k"][k], float)
        print("    %-3d %+.6e %-11.3f"
              % (k, float(np.median(av)),
                 float(av.max() - av.min())
                 / max(abs(float(np.median(av))), 1e-30)))
    if bst["med"] <= TODA_RES_BAR and stable:
        sub_toda = "TODA-CLOSED(%s)" % best
    elif bst["med"] <= TODA_RES_BAR:
        sub_toda = "TODA-VARYING(%s)" % best
    else:
        sub_toda = "TODA-OPEN"
    check("S2.s Toda bilinear form typed %s (best median "
          "residual %.3f vs bar %.2f; a fitted closure is only "
          "the existence signal -- derivation from the IIKS "
          "generators is PRIME.PORT.PAINLEVE.01)"
          % (sub_toda, bst["med"], TODA_RES_BAR), True)

    # ---------------- S3: the pole-free corridor ----------------
    section("S3 -- POLE-FREE CORRIDOR: min_k tau^(k)(s) on "
            "[0, 1] (grid + s = 1.0 exactly) on ALL %d rungs; "
            "then the control corridors + crossing points s*"
            % len(rungs))
    ss1 = np.append(ss, 1.0)
    crossed = []
    closest = (float("inf"), None, None, None)  # val, kz, k, s
    for kz in order:
        T = tau_grid(rungs[kz]["evs"], ss1)
        i_min = int(np.argmin(T))
        kmin, jmin = divmod(i_min, len(ss1))
        vmin = float(T[kmin, jmin])
        if vmin < closest[0]:
            closest = (vmin, kz, kmin + 1, float(ss1[jmin]))
        if np.any(T <= 0.0):
            kk, jj = np.nonzero(T <= 0.0)
            crossed.append((kz, int(kk[0]) + 1,
                            float(ss1[jj[0]])))
    corridor_clear = len(crossed) == 0
    sub_corr = ("CORRIDOR-CLEAR" if corridor_clear
                else "CORRIDOR-CROSSED")
    check("S3.s truth corridor typed %s -- crossings (kz, k, "
          "s): %s" % (sub_corr, crossed if crossed else "none"),
          True)
    print("    closest approach: min_{k,s} tau^(k) = %.6e at "
          "kz %d, k = %d, s = %.4f"
          % (closest[0], closest[1], closest[2], closest[3]))
    print("    (the corridor from tau = 1 at s = 0 to the wall "
          "at s = 1 is %s on every tested rung)"
          % ("pole-free/sign-stable"
             if corridor_clear else "NOT pole-free"))

    # controls: the decisive structural readout
    print("\n    CONTROLS (kz 9): the control walls are "
          "violated, so their corridors MUST cross before "
          "(or at) s = 1 -- the pole position s* separates "
          "truth from controls.")
    rr9 = core.build_window(9)
    N_E = int(math.floor(math.exp(2.0 * rr9["alpha"]))) + 1
    lamE_ = lambda_eps(N_E)
    nn = np.nonzero(np.abs(lamE_) > 1e-12)[0]
    ok_ctl = True
    ctl_report = []
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
            ctl_report.append((nmc, "frame-death"))
            continue
        evc = section_eigs(CJ)
        lam_mx = float(np.max(evc[-1]))
        s_star = (1.0 / lam_mx) if lam_mx > 0 else float("inf")
        # grid confirmation of the first crossing
        sg = np.linspace(0.0, 1.2, 1201)
        Tc = tau_grid(evc, sg)
        neg = np.nonzero(np.any(Tc <= 0.0, axis=0))[0]
        s_grid_cross = float(sg[neg[0]]) if len(neg) else None
        fired = s_star <= 1.0
        ok_ctl &= fired
        ctl_report.append((nmc, s_star))
        print("    %-8s: lam_max(C) = %.6f -> pole s* = %.6f "
              "(exact 1/lam_max; grid-confirmed first crossing "
              "at s = %s) -> %s"
              % (nmc, lam_mx, s_star,
                 ("%.3f" % s_grid_cross)
                 if s_grid_cross is not None else ">1.2",
                 "FIRES (pole inside [0,1])" if fired
                 else "silent"))
    check("C1 CONTROLS FIRE (frame death / pole s* <= 1): %s"
          % (["%s: %s" % (n, v if isinstance(v, str)
                          else "%.4f" % v)
              for n, v in ctl_report]), ok_ctl, kill="KC")

    # ---------------- S4: the pole-distance law -----------------
    section("S4 -- THE POLE-DISTANCE LAW (report only): s*_h = "
            "1/lam_max(C_h) EXACTLY; s*_h - 1 = tau_h/(1 - "
            "tau_h) with the wall margin tau_h = 1 - lam_max")
    print("\n    %-4s %-5s %-10s %-11s %-11s %-11s" % (
        "kz", "h", "lam_max", "tau_h", "s*_h", "s*_h - 1"))
    hs, margins = [], []
    all_out = True
    for kz in order:
        r = rungs[kz]
        lam_mx = float(np.max(r["evs"][-1]))
        tau_h = 1.0 - lam_mx
        s_star = 1.0 / lam_mx if lam_mx > 0 else float("inf")
        all_out &= s_star > 1.0
        print("    %-4d %-5d %-10.6f %-11.4e %-11.6f %-11.4e"
              % (kz, r["b"]["h"], lam_mx, tau_h, s_star,
                 s_star - 1.0))
        if s_star > 1.0 and math.isfinite(s_star):
            hs.append(float(r["b"]["h"]))
            margins.append(s_star - 1.0)
    if len(margins) >= 3:
        slope = float(np.polyfit(np.log(hs),
                                 np.log(margins), 1)[0])
        print("\n    h-trend: LS slope of log(s*_h - 1) vs "
              "log h = %+.3f  (s*_h - 1 = tau_h/(1 - tau_h) "
              "~ tau_h for small tau_h: the wall margin IS "
              "the pole distance)" % slope)
    print("""
    HONEST STATEMENT (elementary but organizing): tau^{(12)}(s)
    = prod_i (1 - s lam_i(C_h)) has its first positive zero at
    s*_h = 1/lam_max(C_h) exactly, and by Cauchy interlacing no
    section minor crosses earlier.  So the wall margin tau_h =
    1 - lam_max and the pole distance s*_h - 1 carry the SAME
    information: RH on the ladder = the pole of the s-flow
    stays outside [0, 1] uniformly in h.  The truth keeps the
    pole beyond s = 1 on every tested rung%s; the controls pull
    it inside (S3).  This is a finite-window measurement, NOT
    an RH claim.""" % ("" if all_out else
                       " -- EXCEPT the crossings censused in S3"))

    return finish(sub_toda, sub_corr)


def finish(sub_toda, sub_corr):
    section("V -- FROZEN VERDICT")
    n_pass = sum(1 for _n, okk in CHECKS if okk)
    n_tot = len(CHECKS)
    if KILLS:
        VERDICT = {"KP": "PIPELINE-BROKEN", "KW": "WARD-BROKEN",
                   "KC": "CONTROL-DEAD"}[KILLS[0]]
    else:
        VERDICT = "SFLOW-MEASURED"
    print("\n  VERDICT: %s (%s, %s)" % (VERDICT, sub_toda,
                                        sub_corr))
    print("\n  SPEC v2 amendments (fail-first preserved): %s"
          % ("; ".join(AMENDMENTS) if AMENDMENTS else "none"))
    print("""
  HONEST FRAME (as frozen): the per-section Jacobi identity and
  the pole identity s* = 1/lam_max are exact algebra -- their
  wards protect the bookkeeping.  The value content is (a) the
  measured Toda time (if any) in which the section flow closes
  bilinearly with constant coefficients, and (b) the pole-free
  corridor [0, 1] on the truth against the control poles pulled
  inside.  The flow equations must FOLLOW from the IIKS
  generators (PRIME.PORT.PAINLEVE.01) before anything is
  claimed.  NO RH claim.  No marker moves.""")
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed"
          % (time.time() - T0, n_tot, n_tot - n_pass))
    return 0 if n_pass == n_tot else 1


if __name__ == "__main__":
    raise SystemExit(main())
'''

# ------------- frozen probe source tau_mobius_factor_probe (embedded BYTE-EXACT, raw string)
_SRC_2 = r'''
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""tau_mobius_factor_probe -- PRIME.PORT.TAU.MOEBIUS.01
(EXPLORATION ONLY, experiments/; round 48, reviewer probe 5 --
THE KEY RUN: does the tau quotient factor through the Moebius/
transfer step as tau_{h+1}/tau_h = F(step data) with F > 0
following ALGEBRAICALLY from a contractivity condition?
2026-08-09.)

THE QUESTION (frozen): port_schur_cocycle_probe warded the exact
quotient identity det(W_{h+1})/det(W_h) = det(I + W_h^{-1} Delta C)
on the 12x12 window W = I - C_J, but the naive low-rank alpha
reduction FAILS because W is near-singular at the soft mode -- the
sv tail of the increment is determinant-relevant.  The reviewer's
target shape: tau_{h+1} = q_h (1 - |alpha_h|^2) tau_h with q_h > 0
source-positive, or any equivalent positive factorization where
sign(tau_{h+1}) = sign(tau_h) follows from the step algebra.
Without such an identity there is no positivity inheritance.

THE LADDER (frozen, port_schur_cocycle verbatim): all frame-A
zones (core.frame_a_zones()) with h <= 900, sorted by (h, kz);
consecutive rung pairs.  T1/T2 run on FULL-WINDOW pairs (both
rungs carry all 12 indices of J = {2, 4, ..., 24}; typed skips
counted); the fitted-step reproduction (T3/T4) runs on pairs with
>= 8 common port alias indices.

FROZEN PROTOCOL (2026-08-09; all bars frozen before the run):

 T1  THE EXACT FACTORIZATION LEDGER: per full-window step compute
     the exact quotient Q_h = det(W_{h+1})/det(W_h) (slogdet) and
     decompose it EXACTLY along the eigen structure:
       Q_h = prod_i (1 + mu_i),
       mu_i = eigenvalues of W_h^{-1} Delta C,
       Delta C = C_J(h) - C_J(h+1)  (so W_{h+1} = W_h + Delta C).
     On truth W_h is PD (minors-positive, re-warded), so the mu_i
     are computed EXACTLY REAL via the symmetric similarity
     W^{-1/2} Delta C W^{-1/2} (eigh); WARD (kill -> WARD-BROKEN):
     |prod(1 + mu_i) - Q_h| <= 1e-10 relative on every step.
     THE MU-SPECTRUM ANATOMY per step: number of factors with
     mu_i < -1 (negative factor = sign flip), number with
     |1 + mu_i| < 0.1 (near-crossing, frozen NEAR_BAR), the census
     min_i (1 + mu_i), and the soft-mode projection: the soft mode
     s_h = eigenvector of W_h at its SMALLEST eigenvalue (= top
     eigenvector of C_J); per eigenvalue mu_i the overlap
     |<v_i, s_h>| of its (W^{-1/2}-transported, normalized)
     eigenvector; reported for the dangerous factor
     (argmin |1 + mu_i|) -- is the dangerous direction always the
     soft mode?  MEASURED FACT to establish: Q_h > 0 on every
     truth step (tau never flips; census reported, not killed --
     a flip would be a discovery, not a breakage).

 T2  THE ONE-DANGEROUS-FACTOR REDUCTION (the candidate bridge):
     typed test -- define mu_soft = the eigenvalue whose
     eigenvector has the LARGEST soft-mode overlap (frozen
     selector).  Q_h = (bulk product over i != soft) x
     (1 + mu_soft) holds exactly by T1; the BRIDGE question is
     whether the bulk is uniformly harmless: typed BRIDGE-SCALAR
     iff min over the ladder of min_{i != soft} (1 + mu_i) >=
     BULK_MARGIN = 0.5 (then sign(Q_h) = sign(1 + mu_soft) and
     the determinant bridge reduces to ONE scalar per step);
     BRIDGE-DIFFUSE otherwise.  Reported: the mu_soft ladder, its
     sign census, its size law (corr(log|mu_soft|, log tau_h) and
     corr(log|mu_soft|, log ||Delta C||_F)), the census of
     soft == dangerous coincidences, and -- if BRIDGE-SCALAR --
     the new contract candidate stated plainly: the induction
     demand becomes the SINGLE explicit inequality
     1 + mu_soft(h) > 0 for all h.

 T3  THE CONTRACTION LINK (the reviewer's demanded coupling):
     reproduce the fitted per-step Moebius maps of
     port_schur_cocycle S2 (machinery verbatim; REPRODUCTION WARD
     kill -> WARD-BROKEN: 41 steps, per-step residual table match
     within the print rounding 5.001e-5, |alpha| < 1 on 100% --
     moebius_source_step_probe precedent).  On steps that are BOTH
     full-window AND fitted, compute (fit NOTHING new):
       J_h := (1 + mu_soft) / (1 - |alpha_h|^2)
     and examine: (a) J_h > 0 on all steps; (b) lawful vs h: the
     sign of (J_h - 1) constant on >= 0.90 of steps; (c) source-
     interpretable: corr(log|J_h - 1|, log ||Delta C||_F) >= 0.8.
     TYPED: LINK-LAWFUL iff (a)+(b)+(c); LINK-POSITIVE iff (a)
     only; LINK-OPEN otherwise (honest -- if J_h is wild the link
     is not this simple).  KNOWN CONTEXT, declared: round 46
     measured the fitted steps INSIDE the identity noise
     (CARRIER-INVARIANT, |alpha_h| ~ 0.002), so 1 - |alpha_h|^2 =
     1 - O(1e-5) and J_h ~ 1 + mu_soft is the expected outcome;
     the probe measures whether the Moebius datum carries ANY of
     the determinant load, and reports plainly if it does not.

 T4  J-CONTRACTIVITY IN THE CANONICAL GAUGE (report only): frozen
     det-normalized convention (own; coordinated with, but not
     dependent on, the parallel iiks_gauge_firewall_probe): the
     step transfer A_h = T_h / |det T_h|^{1/2} from the fitted
     anchored map T_h (three-anchor (0,1,inf) gauge), Cayley disk
     conjugation U_h = K A_h K^{-1}, K = [[1, -i], [1, i]];
     compute the eigenvalues of J - U_h^* J U_h with J =
     diag(1, -1); census of J-contractive steps (min eig >=
     -1e-9 ||U||_F^2) on truth AND on the SMOOTH-MASS world.
     ALGEBRA, declared up front: a real A_h with det = +1 gives
     U_h in SU(1,1), i.e. an EXACT J-isometry -- the census
     therefore separates orientation (det sign) and quantifies
     the numerical deviation; contractivity in this gauge lives
     in the Cayley datum |alpha_h| < 1, not in the matrix
     quadratic form, and the probe says so plainly.

 C   CONTROLS: (C1, kz 9, must fire, kill -> CONTROL-DEAD)
     Epstein (lambda_eps recursion comb) + scramble (seed 1): the
     compressed frame must die (I - E_out indefinite OR
     lam(C_J) > 1 OR window unavailable); channel reported.
     (C2, the arithmetic detector, kill -> CONTROL-DEAD if
     silent) THE SMOOTH-MASS WORLD: the full ladder rebuilt with
     the actual atom positions u_n carrying the SMOOTH masses
     m_n = 2 e^{u_n/2} du_n (midpoint cells; lattice_parametrix
     B1 LATTICE-SMOOTH verbatim -- the FLUCTUATIONS-REQUIRED
     world whose floor is violated).  Its Q_h ladder MUST show
     the violation: typed SMOOTH-FLIP-DETECTED iff some smooth
     rung has det(W) <= 0 or min eig(W) < 0, or some smooth step
     has Q_h < 0 or a real factor 1 + mu < 0 (first crossing
     LOCATED and printed); SMOOTH-FRAME-DIES iff the smooth frame
     itself dies (exterior supercritical / window unavailable /
     chain death -- detection via frame, reported against the
     'frame survives' premise); SMOOTH-UNDETECTED (control
     silent) -> CONTROL-DEAD.  The smooth factor anatomy uses the
     general (complex-capable) eigensolver since W need not stay
     PD there; its factorization ward is 1e-8 (reported).

 W   PIPELINE WARDS (kill -> PIPELINE-BROKEN): W1 >= 30 truth
     rungs; W2 [Y, D_P] rank 2 on every truth rung (s3/s1 <=
     1e-10); W3 >= 20 full-window T1 pairs AND det(W_h) > 0 on
     every truth full-window rung; W4 >= 30 fitted steps.

KILLS: K1 pipeline ward breaks -> PIPELINE-BROKEN; KW the T1
factorization ward or the T3 reproduction ward breaks ->
WARD-BROKEN; K3 controls silent (C1 or C2) -> CONTROL-DEAD.

VERDICT (frozen enum): TAUMOEBIUS-MEASURED with typed sublabels
BRIDGE-SCALAR / BRIDGE-DIFFUSE (T2), LINK-LAWFUL / LINK-POSITIVE
/ LINK-OPEN (T3), and SMOOTH-FLIP-DETECTED / SMOOTH-FRAME-DIES
(C2); else PIPELINE-BROKEN / WARD-BROKEN / CONTROL-DEAD.

SPEC v1 BOOKKEEPING NOTE (documented before the first run;
physics verbatim): core.build_window(kz) is called ONCE per zone
and its output dict is passed to both the truth rung and the
smooth-mass rung (the comb substitution happens after the build
exactly as in the predecessors); this is bookkeeping only -- the
per-world lag assembly, fold, chain and compressions are the
predecessor code paths bit for bit.

SPEC v2 (2026-08-09, after run 1; fail-first preserved -- run 1
passed S0/W/T1-T4/C1 and crashed on a SHAPE slip in the C2
bookkeeping BEFORE any C2 typing: smooth-mass rungs may carry a
PARTIAL window (>= 8 but < 12 of the J indices; the truth ladder
always carries all 12), and the per-rung wall diagnostic sized
W = I - C_J by the full 12.  v2 sizes W by the available window
(mechanical), reports the partial-window count, and restricts the
per-rung wall census to the available indices.  Every T1-T4
number of run 1 is unchanged by construction (the truth-side code
path is untouched).

NO RH claim -- an exact factorization of window-determinant
quotients on compressed truncations is a numerical measurement,
not a theorem about zeros.

FIREWALL: no zeros, no prime oracles (AST scan; banned ids
zetazero / nzeros / primerange / isprime / primepi / nextprime /
prevprime); v563 READ-ONLY; RNG only inside the declared scramble
control; stdout only.  No marker moves.

Sources (read-only): v563_paper2_readouts; window compression +
exact quotient identity + fitted-step machinery verbatim from
port_schur_cocycle_probe.py (PRIME.PORT.SCHURSTEP.01) via
moebius_source_step_probe.py (PRIME.PORT.MOEBIUS.SOURCE.01,
reproduction table); smooth-mass world verbatim from
lattice_parametrix_probe.py (PRIME.PORT.LATTICE.PARAMETRIX.01,
B1); port_kyp_storage_probe.py (KYP storage: wall-blind,
context).  IIKS = Its-Izergin-Korepin-Slavnov.

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/tau_mobius_factor_probe.py
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

H_DEEP_MAX = 900
JWIN = tuple(range(2, 25, 2))
HEAVY = (9, 12, 13, 26, 40)
MIN_RUNGS = 30
MIN_PAIRS_T1 = 20
MIN_PAIRS_FIT = 30
MIN_COMMON_J = 8
RANK_BAR = 1e-10
FACT_WARD = 1e-10           # T1 truth factorization ward (kill)
FACT_WARD_SMOOTH = 1e-8     # C2 smooth factorization ward (report)
NEAR_BAR = 0.1              # |1 + mu| < NEAR_BAR = near-crossing
BULK_MARGIN = 0.5           # T2 BRIDGE-SCALAR bar
LINK_SIGN_FRAC = 0.90       # T3 (b)
LINK_CORR_BAR = 0.8         # T3 (c)
JCON_TOL = 1e-9             # T4 relative tolerance
REF_SEP_MIN = 1e-6
CTRL_KZ = 9
BANNED_IDS = ("zetazero", "nzeros", "primerange", "isprime",
              "primepi", "nextprime", "prevprime")

# T3 reproduction ward: the predecessor's printed per-step residual
# table (41 steps, print precision 1e-4) and headline stats
# (moebius_source_step_probe precedent, verbatim).
REF_RES = (0.0011, 0.0024, 0.0150, 0.0035, 0.0097, 0.0102, 0.0015,
           0.0028, 0.0022, 0.0012, 0.0008, 0.0007, 0.0011, 0.0016,
           0.0006, 0.0005, 0.0003, 0.0001, 0.0013, 0.0005, 0.0002,
           0.0036, 0.0122, 0.0010, 0.0002, 0.0001, 0.0012, 0.0005,
           0.0017, 0.0032, 0.0019, 0.0005, 0.0077, 0.0015, 0.0024,
           0.0215, 0.0118, 0.0063, 0.0011, 0.0043, 0.0005)
REF_N_STEPS = 41
REF_MED_RES = 0.0015
ROUND_TOL = 5.001e-5

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


# --------- pipeline, verbatim from port_schur_cocycle_probe
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


def build_rung(kz, scramble_seed=None, comb=None, rr_cache=None):
    rr = (rr_cache if rr_cache is not None
          else core.build_window(kz, scramble_seed=scramble_seed))
    h, M, D, alpha = rr["h"], rr["M"], rr["D"], rr["alpha"]
    uu = np.asarray(rr["uu"], float)
    mm = 2.0 * np.asarray(rr["lam"], float)
    if comb is not None:
        uu, mm = comb
    c_at, _ = core.atom_lags_at(alpha, M, uu, mm)
    c_ar = np.asarray(core.arch_lags(M, D), float)
    d = grid_density(c_ar + c_at)
    return dict(d=d, L=2 * M - 2, D=D, alpha=alpha, h=h)


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


def antisym_generators(C):
    """Canonical (f, g) with C = f g^T - g f^T (SPEC v2 extraction,
    verbatim)."""
    U, sv, _Vh = np.linalg.svd(C)
    s1 = sv[0]
    f = math.sqrt(s1) * U[:, 0]
    g = math.sqrt(s1) * U[:, 1]
    Ct = np.outer(f, g) - np.outer(g, f)
    if np.linalg.norm(Ct + C) < np.linalg.norm(Ct - C):
        g = -g
    return f, g, sv


def gauge_fix(f, g, jp):
    """FROZEN GAUGE (lax2 verbatim; the anchored normalization
    quotients it out exactly)."""
    m0 = int(np.argmin(jp))
    r = math.hypot(f[m0], g[m0])
    c, s = f[m0] / r, g[m0] / r
    return c * f + s * g, -s * f + c * g


def rung_all(kz, scramble_seed=None, comb=None, rr_cache=None):
    """One heavy build per rung (port_schur_cocycle verbatim): the
    negative-arm Gram E feeds BOTH the 12-index window compression
    and the dressed-port IIKS generators."""
    b = build_rung(kz, scramble_seed=scramble_seed, comb=comb,
                   rr_cache=rr_cache)
    h, L, D = b["h"], b["L"], b["D"]
    if h > H_DEEP_MAX:
        return "TOO-DEEP"
    xs, ws, _ = folded_measure(b["d"], L, +1.0)
    ys, vs, uf_n = folded_measure(b["d"], L, -1.0)
    al, be, m0, steps = lanczos_chain(xs, ws, h + 1)
    if steps < h + 1 or np.any(be <= 0):
        return None
    Pn = eval_chain(al, be, m0, ys, h)
    E = np.sqrt(vs)[:, None] * (Pn @ Pn.T) * np.sqrt(vs)[None, :]
    E = 0.5 * (E + E.T)
    out = dict(kz=kz, h=h, alpha=b["alpha"],
               lamE=float(np.linalg.eigvalsh(E)[-1]))
    # ---- window compression (port_cocycle_window verbatim)
    idx = {int(j): k for k, j in enumerate(uf_n)}
    jav = [j for j in JWIN if j in idx]
    out["full"] = (len(jav) == len(JWIN))
    if len(jav) >= MIN_COMMON_J:
        iw = [idx[j] for j in jav]
        io = [k for k in range(E.shape[0]) if k not in set(iw)]
        Eo = E[np.ix_(io, io)]
        IO = np.eye(len(io)) - Eo
        CJ = (E[np.ix_(iw, iw)]
              + E[np.ix_(iw, io)] @ np.linalg.solve(
                  IO, E[np.ix_(io, iw)]))
        CJ = 0.5 * (CJ + CJ.T)
        out["CJ"] = CJ
        out["jav"] = jav
        out["lamO"] = float(np.linalg.eigvalsh(Eo)[-1])
        out["lamC"] = float(np.linalg.eigvalsh(CJ)[-1])
    # ---- dressed port + IIKS generators (lax2 verbatim)
    tau_m = (2.0 * math.pi * uf_n / L) / D
    port = tau_m <= float(np.max(tau_m)) / 10.0
    ip, ib = np.where(port)[0], np.where(~port)[0]
    if len(ip) >= 4 and len(ib) >= 1:
        P = E[np.ix_(ip, ip)]
        X = E[np.ix_(ip, ib)]
        R = E[np.ix_(ib, ib)]
        IR = np.eye(len(ib)) - R
        DP = P + X @ np.linalg.solve(IR, X.T)
        DP = 0.5 * (DP + DP.T)
        Y = np.diag(ys[ip])
        C = Y @ DP - DP @ Y
        f, g, sv = antisym_generators(C)
        f, g = gauge_fix(f, g, uf_n[ip])
        out["f"], out["g"] = f, g
        out["jp"], out["yp"] = uf_n[ip], ys[ip]
        out["rk"] = float(sv[2] / sv[0]) if len(sv) > 2 else 0.0
    return out


# ------------------------------------------- homogeneous RP^1 machinery
def unit_pairs(g, f):
    P = np.stack([np.asarray(g, float), np.asarray(f, float)],
                 axis=1)
    return P / np.linalg.norm(P, axis=1)[:, None]


def chordal(P, Q):
    """Chordal distance on RP^1 between unit pair rows."""
    return np.abs(P[:, 0] * Q[:, 1] - P[:, 1] * Q[:, 0])


def norm_map(p0, p1, p2):
    """The unique PSL(2, R) map sending p0 -> 0, p1 -> 1,
    p2 -> infinity (homogeneous); None if degenerate (verbatim)."""
    M = np.stack([p2, p0], axis=1)
    if abs(float(np.linalg.det(M))) < 1e-12:
        return None
    T0 = np.linalg.inv(M)
    s, t = T0 @ p1
    if abs(s) < 1e-10 or abs(t) < 1e-10:
        return None
    return np.diag([1.0 / s, 1.0 / t]) @ T0


def apply_hom(T, P):
    Q = (T @ P.T).T
    n = np.linalg.norm(Q, axis=1)
    n[n < 1e-300] = 1.0
    return Q / n[:, None]


def moebius_fit(P, Q):
    """TLS Moebius fit (verbatim)."""
    rows = np.stack([P[:, 0] * Q[:, 1], P[:, 1] * Q[:, 1],
                     -P[:, 0] * Q[:, 0], -P[:, 1] * Q[:, 0]],
                    axis=1)
    _u, _s, Vh = np.linalg.svd(rows)
    a, b, c, d = Vh[-1]
    T = np.array([[a, b], [c, d]])
    return T, chordal(apply_hom(T, P), Q)


def cayley_alpha(T):
    den = T[1, 0] * 1j + T[1, 1]
    if abs(den) < 1e-300:
        return float("inf")
    z = (T[0, 0] * 1j + T[0, 1]) / den
    return abs((z - 1j) / (z + 1j))


def quart(v):
    q = np.percentile(np.asarray(v, float), [25, 50, 75])
    return "q25 %.4f  med %.4f  q75 %.4f" % tuple(q)


def eps_comb(kz):
    rr = core.build_window(kz)
    N_E = int(math.floor(math.exp(2.0 * rr["alpha"]))) + 1
    lamE_ = lambda_eps(N_E)
    nn = np.nonzero(np.abs(lamE_) > 1e-12)[0]
    return (np.log(nn.astype(float)),
            2.0 * lamE_[nn] / np.sqrt(nn.astype(float)))


# ------------------------------------------- smooth-mass world (B1)
def cell_widths(uu):
    """Midpoint cell widths (lattice_parametrix verbatim)."""
    du = np.zeros(len(uu))
    du[1:-1] = 0.5 * (uu[2:] - uu[:-2])
    du[0] = uu[1] - uu[0]
    du[-1] = uu[-1] - uu[-2]
    return du


def smooth_masses(uu):
    """B1 LATTICE-SMOOTH masses m_n = 2 e^{u_n/2} du_n (verbatim)."""
    return 2.0 * np.exp(np.asarray(uu, float) / 2.0) \
        * cell_widths(np.asarray(uu, float))


# ------------------------------------------- factorization machinery
def logdet_sgn(W):
    sgn, ld = np.linalg.slogdet(W)
    return float(sgn), float(ld)


def factor_step_pd(Wa, DC):
    """Truth branch: Wa symmetric PD.  Exact real mu spectrum of
    Wa^{-1} DC via the symmetric similarity, plus transported
    normalized eigenvectors and the soft mode of Wa."""
    ew, Vw = np.linalg.eigh(Wa)
    if ew[0] <= 0.0:
        return None
    Wisq = Vw @ np.diag(ew ** -0.5) @ Vw.T
    Msym = Wisq @ DC @ Wisq
    mu, Us = np.linalg.eigh(0.5 * (Msym + Msym.T))
    vecs = Wisq @ Us
    vecs = vecs / np.linalg.norm(vecs, axis=0)[None, :]
    soft = Vw[:, 0]
    return dict(mu=mu, vecs=vecs, soft=soft, tau=float(ew[0]))


def factor_step_general(Wa, DC):
    """Smooth-world branch: W need not be PD; general (complex-
    capable) eigen decomposition of Wa^{-1} DC."""
    try:
        M = np.linalg.solve(Wa, DC)
    except np.linalg.LinAlgError:
        return None
    mu, V = np.linalg.eig(M)
    ews, Vw = np.linalg.eigh(0.5 * (Wa + Wa.T))
    isoft = int(np.argmin(ews))
    return dict(mu=mu, vecs=V, soft=Vw[:, isoft],
                tau=float(ews[isoft]))


def corr_or_nan(x, y):
    x = np.asarray(x, float)
    y = np.asarray(y, float)
    m = np.isfinite(x) & np.isfinite(y)
    if int(np.sum(m)) < 3 or np.std(x[m]) == 0 or np.std(y[m]) == 0:
        return float("nan")
    return float(np.corrcoef(x[m], y[m])[0, 1])


K_HD = np.array([[1.0, -1j], [1.0, 1j]], dtype=complex)   # H -> D
K_DH = np.linalg.inv(K_HD)
J2 = np.diag([1.0, -1.0]).astype(complex)


def j_contract_eigs(T):
    """T4: det-normalized disk conjugation; eigenvalues of
    J - U^* J U (2, ascending) plus det sign and ||U||_F^2."""
    dt = float(np.linalg.det(T))
    if abs(dt) < 1e-300:
        return None
    A = T / math.sqrt(abs(dt))
    U = K_HD @ A.astype(complex) @ K_DH
    Mj = J2 - U.conj().T @ J2 @ U
    ev = np.linalg.eigvalsh(0.5 * (Mj + Mj.conj().T))
    return dict(ev=ev, sgn=(1.0 if dt > 0 else -1.0),
                n2=float(np.linalg.norm(U) ** 2))


def fit_steps(rungs):
    """The port_schur_cocycle S2 fitted steps (verbatim), indexed by
    the consecutive-pair position k.  Returns (steps, skips)."""
    steps = []
    n_skip_j = n_skip_ref = 0
    for k, (ra, rb) in enumerate(zip(rungs[:-1], rungs[1:])):
        com, ia, ib = np.intersect1d(ra.get("jp", []),
                                     rb.get("jp", []),
                                     return_indices=True)
        if len(com) < MIN_COMMON_J:
            n_skip_j += 1
            continue
        Pa = unit_pairs(ra["g"][ia], ra["f"][ia])
        Pb = unit_pairs(rb["g"][ib], rb["f"][ib])
        order = np.argsort(com)
        i0, i1, i2 = order[0], order[1], order[2]
        seps = [chordal(Pa[[u]], Pa[[v]])[0]
                for u, v in ((i0, i1), (i0, i2), (i1, i2))] \
            + [chordal(Pb[[u]], Pb[[v]])[0]
               for u, v in ((i0, i1), (i0, i2), (i1, i2))]
        Ta = norm_map(Pa[i0], Pa[i1], Pa[i2])
        Tb = norm_map(Pb[i0], Pb[i1], Pb[i2])
        if min(seps) <= REF_SEP_MIN or Ta is None or Tb is None:
            n_skip_ref += 1
            continue
        Na, Nb = apply_hom(Ta, Pa), apply_hom(Tb, Pb)
        T, res = moebius_fit(Na, Nb)
        keep = np.ones(len(com), dtype=bool)
        keep[[i0, i1, i2]] = False
        steps.append(dict(k=k, ra=ra, rb=rb, T=T,
                          res=float(np.median(res[keep])),
                          alpha=cayley_alpha(T)))
    return steps, n_skip_j, n_skip_ref


def factor_pairs(rungs, general=False):
    """T1 ledger rows on the full-window consecutive pairs of a
    rung list.  Truth: PD branch (real mu); general=True: smooth
    branch."""
    rows = []
    n_skip = 0
    for k, (ra, rb) in enumerate(zip(rungs[:-1], rungs[1:])):
        if not (ra.get("full") and rb.get("full")):
            n_skip += 1
            continue
        n = len(JWIN)
        Wa = np.eye(n) - ra["CJ"]
        Wb = np.eye(n) - rb["CJ"]
        sga, lda = logdet_sgn(Wa)
        sgb, ldb = logdet_sgn(Wb)
        Q = sga * sgb * math.exp(ldb - lda)
        DC = ra["CJ"] - rb["CJ"]         # W_b = W_a + DC
        fs = (factor_step_general(Wa, DC) if general
              else factor_step_pd(Wa, DC))
        if fs is None:
            fs = factor_step_general(Wa, DC)
            if fs is None:
                n_skip += 1
                continue
            fs["forced_general"] = True
        mu = fs["mu"]
        prod = complex(np.prod(1.0 + mu.astype(complex)))
        dev = abs(prod - Q) / max(abs(Q), 1e-300)
        real_m = np.abs(np.imag(mu.astype(complex))) \
            <= 1e-9 * (1.0 + np.abs(mu))
        mur = np.real(mu.astype(complex))
        fac_r = 1.0 + mur[real_m]
        ovl = np.abs(np.real(
            fs["vecs"].astype(complex)).T @ fs["soft"])
        nv = np.linalg.norm(np.real(fs["vecs"].astype(complex)),
                            axis=0)
        ovl = ovl / np.maximum(nv, 1e-300)
        i_soft = int(np.argmax(ovl))
        i_dang = int(np.argmin(np.abs(1.0 + mu.astype(complex))))
        mu_soft = complex(mu[i_soft])
        bulk = np.abs(1.0 + np.delete(mu.astype(complex), i_soft))
        bulk_signed = np.delete(1.0 + mur, i_soft) \
            if np.all(real_m) else None
        rows.append(dict(
            k=k, ha=ra["h"], hb=rb["h"], kza=ra["kz"], Q=Q,
            dev=dev, mu=mu, n_real=int(np.sum(real_m)),
            n_neg=int(np.sum(fac_r < 0.0)),
            n_near=int(np.sum(np.abs(fac_r) < NEAR_BAR)),
            min_fac=(float(np.min(fac_r)) if len(fac_r)
                     else float("nan")),
            i_soft=i_soft, i_dang=i_dang,
            mu_soft=mu_soft, ovl_soft=float(ovl[i_soft]),
            ovl_dang=float(ovl[i_dang]),
            bulk_min=(float(np.min(bulk_signed))
                      if bulk_signed is not None
                      else float(np.min(bulk))),
            all_real=bool(np.all(real_m)),
            tau=fs["tau"], dmass=float(np.linalg.norm(DC)),
            sga=sga, sgb=sgb))
    return rows, n_skip


def main():
    section("PRIME.PORT.TAU.MOEBIUS.01 -- the exact determinant "
            "bridge of the tau quotient (EXPLORATION ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s"
          % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
    print("    NO RH claim; no marker moves.")
    print("\nS0 -- firewall")
    check("S0.1 AST firewall clean", not ast_scan(BANNED_IDS))

    # ------------------------------------------------------------ W
    section("W -- build the truth + smooth-mass ladders (all "
            "frame-A zones, h <= %d)" % H_DEEP_MAX)
    rungs, srungs = [], []
    rk_max = 0.0
    n_smooth_dead = 0
    for kz in core.frame_a_zones():
        rr = core.build_window(kz)
        r = rung_all(kz, rr_cache=rr)
        if not isinstance(r, dict):
            continue
        rk_max = max(rk_max, r.get("rk", 1.0))
        rungs.append(r)
        uu = np.asarray(rr["uu"], float)
        rs = rung_all(kz, comb=(uu, smooth_masses(uu)),
                      rr_cache=rr)
        if isinstance(rs, dict):
            srungs.append(rs)
        else:
            n_smooth_dead += 1
        if kz in HEAVY and "lamC" in r:
            print("    kz %-3d h %4d truth lam(C_J) %.6f | smooth "
                  "%s"
                  % (kz, r["h"], r["lamC"],
                     ("lam(C_J) %.6f lam(out) %.3f"
                      % (rs["lamC"], rs["lamO"]))
                     if isinstance(rs, dict) and "lamC" in rs
                     else "window unavailable / chain dead"))
    rungs.sort(key=lambda r: (r["h"], r["kz"]))
    srungs.sort(key=lambda r: (r["h"], r["kz"]))
    print("    truth: %d rungs, h %d .. %d; worst [Y,D_P] s3/s1 "
          "%.1e" % (len(rungs), rungs[0]["h"], rungs[-1]["h"],
                    rk_max))
    print("    smooth-mass: %d rungs built, %d chain/window "
          "deaths" % (len(srungs), n_smooth_dead))
    check("W1 >= %d truth rungs built" % MIN_RUNGS,
          len(rungs) >= MIN_RUNGS, "%d rungs" % len(rungs),
          kill="K1")
    check("W2 rank-2 exact on every truth rung (max s3/s1 %.1e "
          "<= %.0e)" % (rk_max, RANK_BAR), rk_max <= RANK_BAR,
          kill="K1")

    # ------------------------------------------------------------ T1
    trows, n_skip_full = factor_pairs(rungs, general=False)
    section("T1 -- THE EXACT FACTORIZATION LEDGER (%d full-window "
            "pairs; %d typed skips)" % (len(trows), n_skip_full))
    print("    Q_h = det(W_{h+1})/det(W_h) = prod_i (1 + mu_i), "
          "mu_i = eig(W_h^{-1} Delta C)  [ward %.0e]" % FACT_WARD)
    print("    step         Q        min(1+mu)  n<-1 near  "
          "mu_soft    1+mu_soft  ovl(soft) s==d ovl(dang) "
          "bulk_min")
    pd_ok = all(r["sga"] > 0 and r["sgb"] > 0 for r in trows)
    for r in trows:
        print("    h %3d->%3d %+.4e  %+.4f     %d    %d   "
              "%+.2e  %+.6f  %.3f     %-5s %.3f     %+.4f"
              % (r["ha"], r["hb"], r["Q"], r["min_fac"],
                 r["n_neg"], r["n_near"], r["mu_soft"].real,
                 1.0 + r["mu_soft"].real, r["ovl_soft"],
                 str(r["i_soft"] == r["i_dang"]), r["ovl_dang"],
                 r["bulk_min"]))
    check("W3 >= %d full-window pairs and det(W) > 0 on every "
          "truth full-window rung" % MIN_PAIRS_T1,
          len(trows) >= MIN_PAIRS_T1 and pd_ok,
          "%d pairs, PD %s" % (len(trows), pd_ok), kill="K1")
    dev_max = (float(np.max([r["dev"] for r in trows]))
               if trows else float("inf"))
    check("T1.1 FACTORIZATION WARD: max rel dev %.2e <= %.0e "
          "(exact algebra)" % (dev_max, FACT_WARD),
          dev_max <= FACT_WARD, kill="KW")
    all_real = all(r["all_real"] for r in trows)
    check("T1.2 truth mu-spectra all real (PD symmetric "
          "similarity)", all_real)
    n_qpos = sum(1 for r in trows if r["Q"] > 0)
    n_flip = sum(1 for r in trows if r["n_neg"] > 0)
    n_near_any = sum(1 for r in trows if r["n_near"] > 0)
    n_coin = sum(1 for r in trows if r["i_soft"] == r["i_dang"])
    print("\n    MEASURED FACTS: Q_h > 0 on %d/%d steps; steps "
          "with a negative factor: %d; steps with a"
          % (n_qpos, len(trows), n_flip))
    print("    near-crossing factor (|1+mu| < %.1f): %d; "
          "dangerous == soft-mode factor on %d/%d steps"
          % (NEAR_BAR, n_near_any, n_coin, len(trows)))
    print("    min(1+mu) ladder: %s"
          % quart([r["min_fac"] for r in trows]))
    print("    soft-mode overlap of the dangerous eigenvector: %s"
          % quart([r["ovl_dang"] for r in trows]))
    check("T1.3 census reported (Q > 0 on %d/%d, %d negative-"
          "factor steps)" % (n_qpos, len(trows), n_flip), True)

    # ------------------------------------------------------------ T2
    section("T2 -- THE ONE-DANGEROUS-FACTOR REDUCTION (the "
            "candidate bridge)")
    bulk_lad = [r["bulk_min"] for r in trows]
    bulk_min_all = float(np.min(bulk_lad)) if bulk_lad else -1.0
    bridge = ("BRIDGE-SCALAR" if bulk_min_all >= BULK_MARGIN
              else "BRIDGE-DIFFUSE")
    musoft = np.array([r["mu_soft"].real for r in trows])
    n_soft_pos = int(np.sum(1.0 + musoft > 0.0))
    taus = np.array([r["tau"] for r in trows])
    dms = np.array([r["dmass"] for r in trows])
    c_tau = corr_or_nan(np.log(np.abs(musoft) + 1e-300),
                        np.log(taus))
    c_dm = corr_or_nan(np.log(np.abs(musoft) + 1e-300),
                       np.log(dms))
    print("    bulk-min ladder (min over i != soft of (1+mu_i)): "
          "%s" % quart(bulk_lad))
    print("    ladder-wide bulk margin: min %.4f vs frozen bar "
          "%.2f" % (bulk_min_all, BULK_MARGIN))
    print("    mu_soft ladder: %s" % quart(musoft))
    print("    sign census: 1 + mu_soft > 0 on %d/%d steps"
          % (n_soft_pos, len(trows)))
    print("    size law: corr(log|mu_soft|, log tau_h) = %s | "
          "corr(log|mu_soft|, log||Delta C||_F) = %s"
          % ("%.3f" % c_tau if np.isfinite(c_tau) else "n/a",
             "%.3f" % c_dm if np.isfinite(c_dm) else "n/a"))
    check("T2.1 typed: %s (bulk margin %.4f vs %.2f)"
          % (bridge, bulk_min_all, BULK_MARGIN), True)
    if bridge == "BRIDGE-SCALAR":
        print("    CONTRACT CANDIDATE (stated, not claimed): "
              "sign(Q_h) = sign(1 + mu_soft) on the whole")
        print("    ladder -- the induction demand is the SINGLE "
              "inequality  1 + mu_soft(h) > 0  per step,")
        print("    mu_soft = the soft-mode eigenvalue of "
              "W_h^{-1}(C_J(h) - C_J(h+1)).")

    # ------------------------------------------------------------ T3
    steps, n_skip_j, n_skip_ref = fit_steps(rungs)
    section("T3 -- THE CONTRACTION LINK (fitted steps reproduced: "
            "%d; skips %d common-j, %d reference)"
            % (len(steps), n_skip_j, n_skip_ref))
    check("W4 >= %d fitted steps" % MIN_PAIRS_FIT,
          len(steps) >= MIN_PAIRS_FIT, "%d steps" % len(steps),
          kill="K1")
    res_v = np.array([s["res"] for s in steps])
    al_v = np.array([s["alpha"] for s in steps])
    med_res = float(np.median(res_v)) if len(res_v) else 1.0
    frac_al = float(np.mean(al_v < 1.0)) if len(al_v) else 0.0
    tab_dev = (float(np.max(np.abs(res_v - np.array(REF_RES))))
               if len(res_v) == REF_N_STEPS else float("inf"))
    check("T3.0 REPRODUCTION WARD: %d steps == %d; residual "
          "table max dev %.1e <= %.1e; |median - %.4f| <= "
          "%.1e; |alpha| < 1 on %.2f == 1.00"
          % (len(steps), REF_N_STEPS, tab_dev, ROUND_TOL,
             REF_MED_RES, ROUND_TOL, frac_al),
          len(steps) == REF_N_STEPS and tab_dev <= ROUND_TOL
          and abs(med_res - REF_MED_RES) <= ROUND_TOL
          and frac_al == 1.0, kill="KW")
    by_k = {s["k"]: s for s in steps}
    link = [(r, by_k[r["k"]]) for r in trows if r["k"] in by_k]
    print("\n    J_h := (1 + mu_soft)/(1 - |alpha_h|^2)  "
          "(NOTHING fitted here; %d joint steps)" % len(link))
    print("    step        1+mu_soft   |alpha|   1-|a|^2    "
          "J_h        J_h - 1")
    jvals, jm1, ldm = [], [], []
    for r, s in link:
        one_m = 1.0 - s["alpha"] ** 2
        Jh = (1.0 + r["mu_soft"].real) / one_m
        jvals.append(Jh)
        jm1.append(Jh - 1.0)
        ldm.append(math.log(max(r["dmass"], 1e-300)))
        print("    h %3d->%3d  %+.6f   %.4f    %.6f   %+.6f  "
              "%+.2e"
              % (r["ha"], r["hb"], 1.0 + r["mu_soft"].real,
                 s["alpha"], one_m, Jh, Jh - 1.0))
    jvals = np.array(jvals)
    jm1 = np.array(jm1)
    all_pos = bool(len(jvals)) and bool(np.all(jvals > 0.0))
    sgn_frac = (max(float(np.mean(jm1 > 0.0)),
                    float(np.mean(jm1 < 0.0)))
                if len(jm1) else 0.0)
    c_link = corr_or_nan(np.log(np.abs(jm1) + 1e-300),
                         np.array(ldm))
    lawful = (all_pos and sgn_frac >= LINK_SIGN_FRAC
              and np.isfinite(c_link) and c_link >= LINK_CORR_BAR)
    link_label = ("LINK-LAWFUL" if lawful else
                  "LINK-POSITIVE" if all_pos else "LINK-OPEN")
    print("    J_h ladder: %s" % quart(jvals))
    print("    (a) J_h > 0 on %s steps; (b) sign(J_h - 1) "
          "constant on %.2f (bar %.2f); (c) corr(log|J_h-1|,"
          % ("all" if all_pos else "NOT all", sgn_frac,
             LINK_SIGN_FRAC))
    print("        log||Delta C||_F) = %s (bar %.2f)"
          % ("%.3f" % c_link if np.isfinite(c_link) else "n/a",
             LINK_CORR_BAR))
    print("    PLAIN STATEMENT: |alpha_h| ~ %.0e (round-46 "
          "identity noise), so 1 - |alpha_h|^2 deviates"
          % float(np.median(al_v)))
    print("    from 1 by O(1e-5) -- the Moebius datum carries "
          "essentially NONE of the determinant load;")
    print("    J_h is 1 + mu_soft up to that correction, and the "
          "link content is (b)+(c) alone.")
    check("T3.1 typed: %s" % link_label, True)

    # ------------------------------------------------------------ T4
    section("T4 -- J-contractivity census in the det-normalized "
            "disk gauge (report only)")
    ssteps, sn_j, sn_ref = fit_steps(srungs)

    def jcensus(name, stps):
        n_iso = n_con = n_ind = n_neg_det = 0
        evmax = 0.0
        for s in stps:
            jc = j_contract_eigs(s["T"])
            if jc is None:
                continue
            tol = JCON_TOL * max(jc["n2"], 1.0)
            if jc["sgn"] < 0:
                n_neg_det += 1
            evmax = max(evmax, float(np.max(np.abs(jc["ev"]))))
            if float(np.max(np.abs(jc["ev"]))) <= tol:
                n_iso += 1
            elif float(jc["ev"][0]) >= -tol:
                n_con += 1
            else:
                n_ind += 1
        print("    %-12s: %d steps | J-isometric %d | strictly "
              "J-contractive %d | indefinite %d | det<0 %d | "
              "max|eig| %.1e"
              % (name, len(stps), n_iso, n_con, n_ind,
                 n_neg_det, evmax))
        return n_iso, n_con, n_ind

    tj = jcensus("truth", steps)
    sj = jcensus("smooth-mass", ssteps)
    sal = np.array([s["alpha"] for s in ssteps])
    print("    smooth-mass fitted |alpha| < 1 on %s of %d steps "
          "(skips %d common-j, %d reference)"
          % ("%.2f" % float(np.mean(sal < 1.0)) if len(sal)
             else "n/a", len(ssteps), sn_j, sn_ref))
    print("    ALGEBRA, stated plainly: det-normalized real "
          "steps with det > 0 are EXACT J-isometries")
    print("    (SL(2,R) ~ SU(1,1)); the census above measures "
          "orientation + numerical deviation only --")
    print("    in this gauge the contraction lives in the "
          "Cayley datum |alpha_h| < 1, not in J - A*JA.")
    check("T4.1 census reported (truth iso/con/ind = %d/%d/%d; "
          "smooth = %d/%d/%d)" % (tj + sj), True)

    # ------------------------------------------------------------ C
    section("C -- controls")
    print("  C1 -- Epstein/scramble (kz %d, frame must die):"
          % CTRL_KZ)
    ok1 = True
    for nmc, kw in (("Epstein", dict(comb=eps_comb(CTRL_KZ))),
                    ("scramble", dict(scramble_seed=1))):
        try:
            rc = rung_all(CTRL_KZ, **kw)
        except (np.linalg.LinAlgError, AssertionError):
            rc = None
        if not isinstance(rc, dict):
            print("    %-8s: rung not built (%r) -> FRAME DIES"
                  % (nmc, rc))
            continue
        if "lamC" not in rc:
            print("    %-8s: window unavailable -> FRAME DIES"
                  % nmc)
            continue
        fired = (rc["lamO"] > 1.0) or (rc["lamC"] > 1.0)
        ok1 &= fired
        print("    %-8s: lam(out) %.3e | lam(C_J) %.3e -> fires "
              "via %s"
              % (nmc, rc["lamO"], rc["lamC"],
                 "EXTERIOR" if rc["lamO"] > 1.0 else
                 "WINDOW" if rc["lamC"] > 1.0 else "NOTHING"))
    check("C1 CONTROLS FIRE (frame death or supercriticality)",
          ok1, kill="K3")

    print("\n  C2 -- the SMOOTH-MASS world (arithmetic detector):")
    sfull = [r for r in srungs if r.get("full")]
    first_rung_viol = None
    n_partial = sum(1 for r in srungs
                    if "CJ" in r and not r.get("full"))
    for r in srungs:
        if "CJ" not in r:
            continue
        W = np.eye(r["CJ"].shape[0]) - r["CJ"]
        ew = np.linalg.eigvalsh(W)
        r["minW"] = float(ew[0])
        r["detW_sgn"] = float(np.prod(np.sign(ew)))
        if r["minW"] < 0.0 and first_rung_viol is None:
            first_rung_viol = r
    srows, sn_skip = factor_pairs(srungs, general=True)
    print("    %d smooth rungs with window (%d full, %d partial "
          "< 12 indices); %d full-window pairs (%d skips); %d "
          "chain deaths"
          % (sum(1 for r in srungs if "CJ" in r), len(sfull),
             n_partial, len(srows), sn_skip, n_smooth_dead))
    first_pair_viol = None
    sdev_max = 0.0
    for r in srows:
        sdev_max = max(sdev_max, r["dev"])
        flag = (r["Q"] < 0.0
                or (np.isfinite(r["min_fac"])
                    and r["min_fac"] < 0.0))
        if flag and first_pair_viol is None:
            first_pair_viol = r
        print("    h %3d->%3d kz %-3d  Q %+.4e  min(1+mu) %s  "
              "n<-1 %d  near %d  ovl(dang) %.3f%s"
              % (r["ha"], r["hb"], r["kza"], r["Q"],
                 ("%+.4f" % r["min_fac"])
                 if np.isfinite(r["min_fac"]) else "  n/a ",
                 r["n_neg"], r["n_near"], r["ovl_dang"],
                 "  <-- CROSSING" if flag else ""))
    print("    smooth factorization ward (general eig): max rel "
          "dev %.2e vs %.0e (%s)"
          % (sdev_max, FACT_WARD_SMOOTH,
             "ok" if sdev_max <= FACT_WARD_SMOOTH else
             "EXCEEDED -- reported"))
    if sfull:
        deep = max(sfull, key=lambda r: r["h"])
        print("    ENDPOINT: deepest full-window smooth rung "
              "h %d kz %d: min eig(W) %+.4e, det sign %+.0f "
              "(wall %s)"
              % (deep["h"], deep["kz"], deep["minW"],
                 deep["detW_sgn"],
                 "VIOLATED" if deep["minW"] < 0 else "holds"))
    if first_rung_viol is not None:
        print("    FIRST WALL VIOLATION on the rung ladder: "
              "h %d kz %d (min eig(W) %+.4e)"
              % (first_rung_viol["h"], first_rung_viol["kz"],
                 first_rung_viol["minW"]))
    if first_pair_viol is not None:
        print("    FIRST FACTOR CROSSING on the step ladder: "
              "h %d -> %d (Q %+.3e, min(1+mu) %+.4f)"
              % (first_pair_viol["ha"], first_pair_viol["hb"],
                 first_pair_viol["Q"], first_pair_viol["min_fac"]))
    detected = (first_rung_viol is not None
                or first_pair_viol is not None
                or any(r["Q"] < 0 for r in srows))
    frame_died = (n_smooth_dead > 0
                  or any("CJ" not in r for r in srungs)
                  or any(r.get("lamO", 0.0) > 1.0
                         for r in srungs))
    if detected:
        smooth_label = "SMOOTH-FLIP-DETECTED"
    elif frame_died:
        smooth_label = "SMOOTH-FRAME-DIES"
        print("    NOTE: the smooth frame itself dies (against "
              "the 'frame survives' premise) -- detection")
        print("    fires via the frame channel; reported "
              "honestly.")
    else:
        smooth_label = "SMOOTH-UNDETECTED"
    check("C2 SMOOTH-MASS DETECTION: %s" % smooth_label,
          smooth_label != "SMOOTH-UNDETECTED", kill="K3")

    # ------------------------------------------------------------ V
    section("V -- FROZEN VERDICT")
    n_pass = sum(1 for _n, okk in CHECKS if okk)
    n_tot = len(CHECKS)
    if KILLS:
        VERDICT = {"K1": "PIPELINE-BROKEN",
                   "KW": "WARD-BROKEN",
                   "K3": "CONTROL-DEAD"}[KILLS[0]]
        print("\n  VERDICT: %s" % VERDICT)
    else:
        VERDICT = ("TAUMOEBIUS-MEASURED / %s / %s / %s"
                   % (bridge, link_label, smooth_label))
        print("\n  VERDICT: %s" % VERDICT)
        print("  (Q > 0 on %d/%d truth steps; bulk margin %.4f; "
              "1 + mu_soft > 0 on %d/%d; J_h census"
              % (n_qpos, len(trows), bulk_min_all, n_soft_pos,
                 len(trows)))
        print("   (a) %s (b) %.2f (c) %s; smooth detection: %s)"
              % (all_pos, sgn_frac,
                 "%.3f" % c_link if np.isfinite(c_link)
                 else "n/a", smooth_label))
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed"
          % (time.time() - T0, n_tot, n_tot - n_pass))
    return 0 if n_pass == n_tot else 1


if __name__ == "__main__":
    raise SystemExit(main())
'''

# --------------------------------------------------------------- harness
_PF_RE = re.compile(r"^\s*\[(PASS|FAIL)\]\s+(\S+)", re.M)
_VD_RE = re.compile(r"VERDICT[:\]]")


def _probe_file(name):
    cand = os.path.abspath(os.path.join(
        _HERE, os.pardir, "experiments", "tfpt-discovery", name + ".py"))
    return cand if os.path.isfile(cand) else None


def _census(out):
    marks = _PF_RE.findall(out)
    fails = sorted({tok for st, tok in marks if st == "FAIL"})
    verdict = ""
    for line in out.splitlines():
        if _VD_RE.search(line):
            verdict = line.strip()
    return len(marks), fails, verdict


def _exec_probe(name, src, run_entry=True):
    """Execute one embedded frozen probe source BYTE-EXACT in its own
    module namespace (round-31 convention); capture and re-emit
    stdout; return (stdout, exit_code, byte_equal_or_None)."""
    if src[:1] == "\n":
        src = src[1:]
    path = _probe_file(name)
    same = None
    if path is not None:
        with open(path, encoding="utf-8") as fh:
            same = (fh.read() == src)
    fname = path or os.path.abspath(__file__)
    mod = types.ModuleType(name)
    mod.__file__ = fname
    sys.modules[name] = mod
    buf = io.StringIO()
    code = 0
    with contextlib.redirect_stdout(buf):
        try:
            exec(compile(src, fname, "exec"), mod.__dict__)
            entry = mod.__dict__.get("main") or mod.__dict__.get("run")
            if run_entry and callable(entry):
                rc = entry()
                code = 0 if rc is None else int(rc)
        except SystemExit as exc:
            code = 0 if exc.code is None else int(exc.code)
        except Exception:                            # regression guard
            import traceback
            traceback.print_exc(file=sys.stdout)
            code = 99
    out = buf.getvalue()
    sys.stdout.write(out)
    sys.stdout.flush()
    return out, code, same


def _gate(name, out, code, same, exp_n, exp_fails, exp_verdict,
          exp_code, gates):
    n, fails, verdict = _census(out)
    ok = (n == exp_n and fails == list(exp_fails)
          and exp_verdict in verdict and code == exp_code
          and same is not False)
    gates.append(ok)
    prov = ("byte-exact vs experiments source" if same is True else
            "embedded copy (source file not present)" if same is None
            else "SOURCE MISMATCH")
    print("\n[%s] PATTERN GATE %s: %d checks (exp %d) | FAILs %s "
          "(exp %s) | exit %d (exp %d) | %s\n      verdict line: %s"
          % ("PASS" if ok else "FAIL", name, n, exp_n,
             ",".join(fails) if fails else "none",
             ",".join(exp_fails) if exp_fails else "none",
             code, exp_code, prov, verdict), flush=True)
    return ok


_PLAN = (
    ('port_tau_hirota_probe', _SRC_0, 10, (), 'HIROTA-MEASURED', 0),
    ('port_sflow_toda_probe', _SRC_1, 7, (), 'SFLOW-MEASURED', 0),
    ('tau_mobius_factor_probe', _SRC_2, 14, (), 'TAUMOEBIUS-MEASURED', 0),
)


def run():
    t0 = time.time()
    print("=" * 74)
    print('v890 -- PRIME.PORT.HIROTA.01 + PRIME.PORT.SFLOW.01 + PRIME.PORT.TAU.MOEBIUS.01: the surviving positivity architecture -- flag positivity (Sylvester) of the section family, the pole-free s-corridor, and the multi-factor tau anatomy')
    print("(frozen probes embedded byte-exact and executed verbatim; NO RH claim)")
    print("=" * 74, flush=True)
    gates = []
    for name, src, exp_n, exp_fails, exp_verdict, exp_code in _PLAN:
        print("\n" + "-" * 74)
        print("EMBEDDED FROZEN PROBE: %s" % name)
        print("-" * 74, flush=True)
        out, code, same = _exec_probe(name, src)
        _gate(name, out, code, same, exp_n, exp_fails,
              exp_verdict, exp_code, gates)
    ok = all(gates)
    print("\n" + "=" * 74)
    print("v890: %d/%d pattern gates passed | runtime %.1f s"
          % (sum(gates), len(gates), time.time() - t0))
    print('positivity inheritance is a multi-factor/total-positivity statement; the one-scalar Moebius bridge is honestly closed BRIDGE-DIFFUSE')
    print("[%s] v890 VERDICT GATE" % ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(run())
