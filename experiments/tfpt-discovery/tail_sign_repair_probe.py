#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""tail_sign_repair_probe -- PRIME.PORT.TAILSIGN.02
(EXPLORATION ONLY, experiments/; round 62, theorem-engineering on
the RH-side wall; TRIGGERED successor of tail_sign_mechanism_probe
(PRIME.PORT.TAILSIGN.01), whose levels (b) POINTWISE and (c)
CLASSICAL-POINTWISE both FAILED: sup_{u > cut} q > 0 on 67/67 at
every cut (shared 9, per-rung A-cut, per-rung B-cut), positive
knot share med 0.65, terminal lobe POSITIVE on 67/67 with onset
u_last/(2 alpha) med 0.752.  THE QUESTION: where EXACTLY does
pointwise negativity fail (u-region geography, atom census,
magnitude), does a SMALL EXPLICIT set of exceptional atoms carry
all deep positivity (then the head can be enlarged by finitely
many NAMED atoms), what is the MINIMAL enlargement that restores
the deterministic-sign mechanism, and what do the head-floor
tau-screen (d) and the uniformity boundary (e) look like for the
enlarged head.  2026-08-10.)

THE ENLARGED BOOKKEEPING (frozen; exact, warded).  Probe-1
bookkeeping B at the per-rung first B-covering cut cB(h):
m = head_B(cB) + tail_B(cB), tail_B = sum of DEEP atom reads
mu_n q_v(u_n).  The deep positive REGION R+ = {u > u_cB : q_v(u)
> 0} is a finite union of intervals (q_v is piecewise linear on
the lag knots; interval endpoints exact).  Enlarged head:
    head2 = head_B(cB) + sum_{u_n in R+} mu_n q_v(u_n),
    tail2 = sum_{u_n > u_cB, u_n not in R+} mu_n q_v(u_n),
    m = head2 + tail2 EXACTLY (warded), and tail2 <= 0 holds
    DETERMINISTICALLY for ANY nonnegative comb (every remaining
    tail atom sits where the weight is <= 0) -- R+ is WEIGHT
    geometry (classical per probe 1's (c)), not comb data.
cert2 = head2 - |tail2| = m exactly when tail2 <= 0 (same algebra
as rounds 60/62).  The REPAIR PRICE is head2's atom support: the
atoms inside R+.  If R+ reaches the window edge (probe-1 terminal
lobe), that support contains every atom with u_n > u_term -- a
POSITIVE SHARE of all atoms by count -- and the repair is NOT
uniformly finite; measured, not assumed.

WHAT IS MEASURED (frozen; typed, never kills):
 (1) FAILURE GEOGRAPHY: per rung, the positive intervals of q_v
     beyond u_cB: count, endpoints in the scaled variable
     u/(2 alpha), the terminal-lobe onset law (jackknife vs
     alpha), and the mass anatomy: atom count N+, von-Mangoldt
     mass share, positive contribution P+ = sum_{R+} mu_n q^+,
     split terminal lobe vs interior lobes.  CLASSICAL cross-
     check: same intervals from q_{v_sm} (prime-free): interval-
     count agreement share, terminal-onset |Delta| med (kz 97 on
     its carrier branch, disclosed).  Typed FAILGEO(int med,
     terminal share of P+).
 (2) THE EXCEPTIONAL-SET CENSUS: concentration of P+ across
     atoms: per rung the minimal k for 50/90/99% of P+ (sorted
     contributions), the top-N_TOP named atoms (deployed values,
     integer-root prime-power labels), and the STABILITY of the
     named set across the ladder (share of rungs whose top-1
     atom value repeats; union size of the top-k90 sets).  Typed
     SET-SMALL(k90max) iff k90 <= K_SMALL on every rung AND the
     union of top-k90 atom VALUES across rungs has size <=
     K_UNION (a finite NAMED set carries the positivity), else
     SET-DIFFUSE(k90 med, union size).
 (3) THE MINIMAL ENLARGEMENT + (d)/(e) RE-RUN: the atomwise
     repair must absorb ALL of R+ (every positive-weight deep
     atom individually breaks tail2 <= 0 for some nonnegative
     comb); its price N+ vs X: jackknife slope of log N+ vs
     log X (typed REPAIR-FINITE iff slope <= GROW_BAR, else
     REPAIR-GROWING(X^s)); the share N+ / N_deep.  (d) re-run:
     head2 med/min/max, jackknife slope of log head2 vs log m --
     bands PASS |s| <= 0.30 (HEADFLOOR2-O1) / RELOC s >= 0.70 /
     else AMBIG; |tail2| = head2 - m likewise.  (e) named: the
     enlarged head is explicit but its support grows with the
     window; the deterministic-sign statement it buys (tail2 <=
     0) holds for any nonnegative comb, while head2 > |tail2|
     (equivalently head2 > -tail2, gap m) remains the open
     arithmetic content -- now carried by an O(?) head measured
     here.

FROZEN PROTOCOL (pipeline verbatim from
tail_sign_mechanism_probe; ladder, wards and cut conventions
identical):

 W   LADDER + WARDS (kill -> PIPELINE-BROKEN / WARD-BROKEN): W1
     faithful ladder >= MIN_RUNGS = 40; W2 WARD m_h > 0; W3 WARD
     exact bookkeepings (lift - demand = m, e_ar + E_at = m, rel
     <= ID_WARD); W4 REPRODUCTION of probe-1 headline facts:
     B-covering cuts exist on N/N with n_minB med in [NB_LO,
     NB_HI]; pointwise fails beyond u_cB on 0/N; terminal sign
     positive on N/N; W5 WARD enlarged split exactness: |head2 +
     tail2 - m| rel <= ID_WARD on every rung AND tail2 <= 0 on
     every rung (construction: only q <= 0 atoms remain) AND
     cert2 = m to ID_WARD (the tail2 <= 0 algebra).

 H   H1 FAILURE GEOGRAPHY; H2 EXCEPTIONAL-SET CENSUS; H3 MINIMAL
     ENLARGEMENT + (d)/(e) RE-RUN (typed as frozen above).

 C   CONTROLS (kill -> WARD-BROKEN if silent): scramble (seed 1)
     and smooth comb at kz 9: m < 0 AND cert2 < 0 at every cut
     (tail2 <= 0 still holds by construction -- the repair
     cannot manufacture a certificate without the wall, cert2 =
     m exactly); Epstein x^2+5y^2 at kz 9: m < 0 AND cert2 < 0
     at every cut, with the DECLARED different anatomy recorded:
     the Epstein comb has NEGATIVE masses, so the nonnegative-
     comb premise of the deterministic tail sign does not even
     apply there (tail2 <= 0 is checked as measured fact, not
     construction).

KILLS: K1 ladder (W1) -> PIPELINE-BROKEN; K2 wards (W2-W5, C) ->
WARD-BROKEN.  All H-typed outcomes are measurements, never kills.

VERDICT (frozen enum): TAILREPAIR-MEASURED with typed sublabels
FAILGEO(int med, term share), SET-SMALL(kmax)/SET-DIFFUSE(k90,
union), REPAIR-FINITE(slope)/REPAIR-GROWING(X^slope),
HEADFLOOR2-O1/RELOC/AMBIG(slope); else PIPELINE-BROKEN /
WARD-BROKEN.

FROZEN BARS: KZMAX = 150; MIN_RUNGS = 40; NB_LO, NB_HI = 5, 47
(probe-1 measured n_minB band, med-ward: med in band); ID_WARD =
1e-10; NG_SMOOTH = 6000; OV_MIN = 0.8; MAX_CROSS = 2; K_SMALL =
16; K_UNION = 32; N_TOP = 8; GROW_BAR = 0.10; SLOPE_PASS = 0.30;
SLOPE_RELOC = 0.70; CTRL_KZ = 9; scramble seed 1; jackknife =
full leave-one-out, CI = +- 2SE; interval endpoints from exact
knot crossings (piecewise-linear interpolation, no tolerance).

SMOKE-RUN DISCLOSURE (2026-08-10, before freezing): ONE smoke run
(10/10, 17.6 s) on SPEC v0; NO code, bar, band, count, enum or
typed rule was changed after the smoke (the freeze adds only this
disclosure).  Smoke facts frozen as the context the frozen run
must confirm: (1) FAILGEO: 2 positive intervals med (2..3);
terminal-lobe onset u/(2 alpha) med 0.752 and FLAT vs alpha
(slope +0.0026 +- 0.0151, R^2 0.00) -- a stable scaled position;
terminal lobe carries med 0.46 of P+; classical cross-check:
interval-count agreement 66/67, terminal-onset |Delta| med 0.335;
(2) SET-DIFFUSE: k90 med 646 (max 7711), top-k90 union 10649 --
NO small named set; the largest individual positive atoms are the
primes just beyond the cut (mid-ladder: 19, 23, 29, 31, 37, 41,
43, 47); (3) REPAIR-GROWING: N+ med 1969 ~ X^0.890 +- 0.007 (R^2
1.00), med 0.89 of ALL deep atoms; head2 med 17.3 (2.8..65.1) and
ANTI-tau (slope of log head2 vs log m = -0.395 +- 0.072, R^2
0.62 = HEADFLOOR2-AMBIG: the enlarged head GROWS as the margin
shrinks); controls all fire (cert2 = m < 0 at every cut; Epstein
negative-mass anatomy disclosed, tail2 <= 0 there measured, not
construction).

SPEC v1 (2026-08-10, frozen + SHA-hashed before the frozen run):
everything above.  Mechanical concretizations: (i) R+ intervals built from the knot
sign pattern beyond u_cB, clipped at u_cB and at the window edge
2 alpha; an interval is TERMINAL iff its right endpoint is the
window edge; (ii) atom membership u_n in R+ decided by q_v(u_n)
> 0 (equivalent for atoms, exact); (iii) concentration ranks by
the atom contribution mu_n q_v(u_n) descending; (iv) the v_sm
cross-check reads the crossing rung (|<v, v_sm>| < OV_MIN) on
its carrier branch among the 4 lowest smooth branches
(disclosed); (v) X = e^{2 alpha}.

NO-GO COMPLIANCE (frozen): no certified-bound retry, no rank-1
approximation, no Herglotz; identities are exact wards, laws are
typed trends with jackknife error bars.

NO RH claim: the enlarged head restores a deterministic tail
sign at a measured price; the one-sided bound head2 > |tail2|
remains the open arithmetic content at every depth, and nothing
here bounds it.  No marker moves.

FIREWALL: no zeros, no prime oracles (AST scan; banned ids
zetazero / nzeros / primerange / isprime / primepi / nextprime /
prevprime); v563 READ-ONLY; RNG only inside the declared
scramble control; stdout only.

Sources (read-only): v563_paper2_readouts; machinery verbatim
from tail_sign_mechanism_probe.py (round 62, PRIME.PORT.
TAILSIGN.01) and wall_cut_schedule_probe.py (round 60); probe-1
headline facts as declared reproduction targets.

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/tail_sign_repair_probe.py
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

KZMAX = 150
MIN_RUNGS = 40
NB_LO, NB_HI = 5, 47
ID_WARD = 1e-10
NG_SMOOTH = 6000
OV_MIN = 0.8
MAX_CROSS = 2
K_SMALL = 16
K_UNION = 32
N_TOP = 8
GROW_BAR = 0.10
SLOPE_PASS = 0.30
SLOPE_RELOC = 0.70
CTRL_KZ = 9
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


def ols_line(x, y):
    x = np.asarray(x, float)
    y = np.asarray(y, float)
    vx = float(np.var(x))
    if vx == 0.0:
        return float(np.mean(y)), 0.0, float("nan")
    b = float(np.cov(x, y, bias=True)[0, 1] / vx)
    a = float(np.mean(y) - b * np.mean(x))
    ss = float(np.sum((y - a - b * x) ** 2))
    st = float(np.sum((y - np.mean(y)) ** 2))
    return a, b, (1.0 - ss / st if st > 0 else float("nan"))


def jack_slope(x, y):
    x = np.asarray(x, float)
    y = np.asarray(y, float)
    _a, b, r2 = ols_line(x, y)
    n = len(x)
    bb = []
    for i in range(n):
        m = np.ones(n, bool)
        m[i] = False
        bb.append(ols_line(x[m], y[m])[1])
    bb = np.array(bb)
    se = math.sqrt((n - 1) / n * float(np.sum((bb - bb.mean())
                                              ** 2)))
    return b, se, r2


def q_read(W, u, D, M):
    u = np.asarray(u, float)
    i0 = np.floor(u / D).astype(int)
    f = u / D - i0
    val = np.zeros_like(u)
    ok0 = (i0 >= 0) & (i0 < M)
    val[ok0] += (1.0 - f[ok0]) * W[i0[ok0]]
    ok1 = (i0 + 1 >= 0) & (i0 + 1 < M)
    val[ok1] += f[ok1] * W[i0[ok1] + 1]
    refl = u < D
    val[refl] += (1.0 - u[refl] / D) * W[0]
    return -0.5 * val


def smooth_comb(alpha, ng=NG_SMOOTH):
    ug = (np.arange(ng) + 0.5) * (2.0 * alpha / ng)
    mg = 2.0 * np.exp(ug / 2.0) * (2.0 * alpha / ng)
    return ug, mg


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


def pp_label(n):
    """Prime-power structure of a deployed atom value by integer
    roots (no primality oracle; the table IS the comb)."""
    for k in range(int(math.log2(max(n, 2))), 1, -1):
        b = int(round(n ** (1.0 / k)))
        for bb in (b - 1, b, b + 1):
            if bb >= 2 and bb ** k == n:
                return "%d^%d" % (bb, k)
    return "%d" % n


def pos_intervals(W, D, M, u_cut):
    """Positive intervals of the piecewise-linear weight beyond
    u_cut, from the exact knot sign pattern (crossings by linear
    interpolation), clipped at u_cut and the window edge M*D."""
    uk = np.arange(M + 1) * D
    ue = uk.copy()
    ue[0] = 1e-12
    qk = q_read(W, ue, D, M)
    # boundary points: crossings + cut + edge
    pts = [u_cut]
    for i in np.nonzero(qk[:-1] * qk[1:] < 0.0)[0]:
        uc = uk[i] + D * qk[i] / (qk[i] - qk[i + 1])
        if uc > u_cut:
            pts.append(float(uc))
    pts.append(float(M * D))
    pts = sorted(set(pts))
    out = []
    for a, b in zip(pts[:-1], pts[1:]):
        if b <= a:
            continue
        um = 0.5 * (a + b)
        if float(q_read(W, np.array([um]), D, M)[0]) > 0.0:
            out.append((a, b, b >= M * D - 1e-12))
    return out


def build_rung(kz, comb=None, scramble_seed=None,
               smooth_world=False, need_sm=True):
    """One rung: lift-race surface, both bookkeepings, first
    B-covering cut, enlarged split (verbatim probe-1 machinery +
    the R+ enlargement)."""
    try:
        rr = core.build_window(kz, scramble_seed=scramble_seed)
    except Exception:
        return None
    if not (core.H_MIN <= rr["h"] <= core.HCAP):
        return None
    if rr["X"] > core.ATOM_MAX:
        return None
    alpha, M, D, h = rr["alpha"], rr["M"], rr["D"], rr["h"]
    uu = np.asarray(rr["uu"], float)
    mu = 2.0 * np.asarray(rr["lam"], float)
    if smooth_world:
        du = np.zeros(len(uu))
        du[1:-1] = 0.5 * (uu[2:] - uu[:-2])
        du[0] = uu[1] - uu[0]
        du[-1] = uu[-1] - uu[-2]
        mu = 2.0 * np.exp(uu / 2.0) * du
    if comb is not None:
        uu, mu = comb
    c_at = core.atom_lags_at(alpha, M, uu, mu)[0]
    c_ar = np.asarray(core.arch_lags(M, D), float)
    w, V = np.linalg.eigh(core.odd_toeplitz(c_ar + c_at, M))
    v = V[:, 0]
    ug, mg = smooth_comb(alpha)
    c_sm = core.atom_lags_at(alpha, M, ug, mg)[0]
    Wv = core.lag_weights_from_v(v, h)
    e_ar = float(c_ar @ Wv)
    e_t = float(c_at @ Wv)
    e_s = float(c_sm @ Wv)
    qan = q_read(Wv, uu, D, M)
    qa = mu * qan
    row = dict(kz=kz, alpha=float(alpha), h=h, M=M, D=D,
               m=float(w[0]), uu=uu, mu=mu, e_ar=e_ar, e_t=e_t,
               lift=e_t - e_s, demand=-(e_ar + e_s), qa=qa,
               qan=qan, Wv=Wv)
    cq = np.cumsum(qa)
    head_B = e_ar + cq
    tail_B = float(qa.sum()) - cq
    cert_B = head_B - np.abs(tail_B)
    row.update(head_B=head_B, tail_B=tail_B, cert_B=cert_B)
    covB = cert_B > 0.0
    if bool(np.any(covB)):
        icB = int(np.argmax(covB))
        row["icB"] = icB
        row["n_minB"] = int(round(math.exp(uu[icB])))
        row["u_cB"] = float(uu[icB])
    else:
        row["icB"] = -1
        row["n_minB"] = -1
        row["u_cB"] = 0.0
    if need_sm:
        ws, Vs = np.linalg.eigh(core.odd_toeplitz(c_ar + c_sm, M))
        vsm = Vs[:, 0]
        if float(v @ vsm) < 0:
            vsm = -vsm
        ov4 = [abs(float(v @ Vs[:, j])) for j in range(4)]
        jcar = int(np.argmax(ov4))
        vcar = Vs[:, jcar] * (1.0 if float(v @ Vs[:, jcar]) >= 0
                              else -1.0)
        row.update(ov=float(abs(v @ vsm)), ov4=ov4, jcar=jcar,
                   Wsm=core.lag_weights_from_v(vsm, h),
                   Wcar=core.lag_weights_from_v(vcar, h))
    return row


def enlarged_split(row):
    """head2/tail2 at the first B-covering cut: absorb all
    positive-weight deep atoms into the head (atom membership by
    q_v(u_n) > 0, exact for atoms)."""
    icB = row["icB"]
    deep = np.arange(len(row["uu"])) > icB
    pos = deep & (row["qan"] > 0.0)
    neg = deep & ~ (row["qan"] > 0.0)
    P = float(np.sum(row["qa"][pos]))
    head2 = float(row["head_B"][icB]) + P
    tail2 = float(np.sum(row["qa"][neg]))
    return dict(pos=pos, neg=neg, P=P, head2=head2, tail2=tail2,
                Npos=int(np.sum(pos)), Ndeep=int(np.sum(deep)))


def main():
    section("PRIME.PORT.TAILSIGN.02 -- the repair of the "
            "pointwise tail-sign mechanism (EXPLORATION ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s"
          % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
    print("    NO RH claim; no marker moves.")
    print("\nS0 -- firewall")
    check("S0.1 AST firewall clean", not ast_scan(BANNED_IDS))

    # ------------------------------------------------------------ W
    section("W -- the faithful ladder + wards")
    rungs = []
    for kz in range(2, KZMAX + 1):
        row = build_rung(kz)
        if row is not None:
            rungs.append(row)
    rungs.sort(key=lambda r: (r["h"], r["kz"]))
    check("W1 faithful ladder >= %d rungs" % MIN_RUNGS,
          len(rungs) >= MIN_RUNGS,
          "%d rungs, h %d..%d  [%.1f s]"
          % (len(rungs), rungs[0]["h"], rungs[-1]["h"],
             time.time() - T0), kill="K1")
    if KILLS:
        return finish({})
    N = len(rungs)
    check("W2 WARD truth margin m_h > 0 on every rung (min %.3e)"
          % min(r["m"] for r in rungs),
          all(r["m"] > 0 for r in rungs), kill="K2")
    dev_bk = max(max(abs((r["lift"] - r["demand"]) - r["m"]),
                     abs((r["e_ar"] + r["e_t"]) - r["m"]))
                 / max(1.0, abs(r["m"])) for r in rungs)
    check("W3 WARD exact bookkeepings (lift - demand = m, "
          "e_ar + E_at = m): max dev %.2e <= %.0e"
          % (dev_bk, ID_WARD), dev_bk <= ID_WARD, kill="K2")
    n_covB = sum(1 for r in rungs if r["icB"] >= 0)
    nB = [r["n_minB"] for r in rungs if r["icB"] >= 0]
    # probe-1 headline reproduction: pointwise fail + terminal +
    u9 = None
    n_pwB = 0
    n_endpos = 0
    IV = []
    for r in rungs:
        iv = pos_intervals(r["Wv"], r["D"], r["M"], r["u_cB"])
        IV.append(iv)
        if len(iv) == 0:
            n_pwB += 1
        if any(t for _a, _b, t in iv):
            n_endpos += 1
    ok_rep = (n_covB == N and NB_LO <= int(np.median(nB)) <= NB_HI
              and n_pwB == 0 and n_endpos == N)
    check("W4 REPRODUCTION probe-1 headline: B-covering cuts on "
          "%d/%d (n_minB med %d in [%d, %d]); pointwise holds "
          "beyond u_cB on %d/%d (must be 0); terminal lobe "
          "positive on %d/%d"
          % (n_covB, N, int(np.median(nB)), NB_LO, NB_HI,
             n_pwB, N, n_endpos, N), ok_rep, kill="K2")
    ES = [enlarged_split(r) for r in rungs]
    dev_e = max(abs((e["head2"] + e["tail2"]) - r["m"])
                / max(1.0, abs(r["e_t"]))
                for e, r in zip(ES, rungs))
    t2max = max(e["tail2"] for e in ES)
    dev_c = max(abs((e["head2"] - abs(e["tail2"])) - r["m"])
                / max(1.0, abs(r["e_t"]))
                for e, r in zip(ES, rungs))
    check("W5 WARD enlarged split: head2 + tail2 = m (max rel "
          "dev %.2e), tail2 <= 0 on %d/%d (max %+.3e), cert2 = m "
          "(max rel dev %.2e); all <= %.0e"
          % (dev_e, sum(1 for e in ES if e["tail2"] <= 0), N,
             t2max, dev_c, ID_WARD),
          dev_e <= ID_WARD and t2max <= 0 and dev_c <= ID_WARD,
          kill="K2")
    n_cross = sum(1 for r in rungs if r["ov"] < OV_MIN)
    if KILLS:
        return finish({})

    # ------------------------------------------------------------ H1
    section("H1 -- FAILURE GEOGRAPHY: the positive intervals of "
            "q_v beyond u_cB")
    aa = np.array([r["alpha"] for r in rungs])
    n_int = np.array([len(iv) for iv in IV])
    term_on = np.array([[a for a, _b, t in iv if t][0]
                        for iv in IV])
    x_on = term_on / (2.0 * aa)
    sl_on, se_on, r2_on = jack_slope(aa, x_on)
    # mass anatomy
    term_share, int_share = [], []
    for r, iv, e in zip(rungs, IV, ES):
        uT = [a for a, _b, t in iv if t][0]
        posm = e["pos"]
        Pt = float(np.sum(r["qa"][posm & (r["uu"] >= uT)]))
        term_share.append(Pt / max(e["P"], 1e-30))
    term_share = np.array(term_share)
    print("    interval count beyond u_cB: med %d (%d..%d); "
          "terminal-lobe onset u/(2 alpha): med %.3f "
          "(%.3f..%.3f), trend vs alpha %+.4f +- %.4f (R^2 %.2f)"
          % (int(np.median(n_int)), int(n_int.min()),
             int(n_int.max()), float(np.median(x_on)),
             float(np.min(x_on)), float(np.max(x_on)),
             sl_on, 2 * se_on, r2_on))
    print("    P+ split: terminal lobe carries med %.2f "
          "(%.2f..%.2f) of P+; interior lobes the rest"
          % (float(np.median(term_share)),
             float(np.min(term_share)),
             float(np.max(term_share))))
    # classical cross-check
    agree_int, d_on = 0, []
    for r, iv in zip(rungs, IV):
        Wq = r["Wcar"] if r["ov"] < OV_MIN else r["Wsm"]
        ivs = pos_intervals(Wq, r["D"], r["M"], r["u_cB"])
        agree_int += (len(ivs) == len(iv))
        tS = [a for a, _b, t in ivs if t]
        tV = [a for a, _b, t in iv if t]
        if tS and tV:
            d_on.append(abs(tS[0] - tV[0]))
    print("    CLASSICAL cross-check (v_sm, %d crossing rung(s) "
          "on carrier branch): interval-count agreement %d/%d; "
          "terminal-onset |Delta| med %.3f (%.1e..%.3f)"
          % (n_cross, agree_int, N, float(np.median(d_on)),
             float(np.min(d_on)), float(np.max(d_on))))
    h1 = ("FAILGEO(int med %d, term share med %.2f)"
          % (int(np.median(n_int)), float(np.median(term_share))))
    check("H1.1 typed (1): %s -- the failure region is weight "
          "geometry (classical), a terminal lobe + interior "
          "lobes, not an atom accident" % h1, True)

    # ------------------------------------------------------------ H2
    section("H2 -- THE EXCEPTIONAL-SET CENSUS: concentration of "
            "P+")
    k50s, k90s, k99s = [], [], []
    top1_vals, u90 = [], set()
    for r, e in zip(rungs, ES):
        contrib = r["qa"][e["pos"]]
        vals = np.round(np.exp(r["uu"][e["pos"]])).astype(int)
        o = np.argsort(contrib)[::-1]
        cs = np.cumsum(contrib[o]) / max(e["P"], 1e-30)
        k50 = int(np.searchsorted(cs, 0.50) + 1)
        k90 = int(np.searchsorted(cs, 0.90) + 1)
        k99 = int(np.searchsorted(cs, 0.99) + 1)
        k50s.append(k50)
        k90s.append(k90)
        k99s.append(k99)
        top1_vals.append(int(vals[o[0]]))
        u90.update(int(x) for x in vals[o[:k90]])
    k50s, k90s, k99s = map(np.array, (k50s, k90s, k99s))
    vals_c, cnt_c = np.unique(top1_vals, return_counts=True)
    jtop = int(np.argmax(cnt_c))
    print("    minimal k for 50/90/99%% of P+: med %d / %d / %d "
          "(max %d / %d / %d); top-1 atom value repeats: n = %d "
          "(%s) on %d/%d rungs; union of top-k90 atom values "
          "across the ladder: %d"
          % (int(np.median(k50s)), int(np.median(k90s)),
             int(np.median(k99s)), int(k50s.max()),
             int(k90s.max()), int(k99s.max()),
             int(vals_c[jtop]), pp_label(int(vals_c[jtop])),
             int(cnt_c[jtop]), N, len(u90)))
    r_mid = rungs[N // 2]
    e_mid = ES[N // 2]
    contrib = r_mid["qa"][e_mid["pos"]]
    vals = np.round(np.exp(r_mid["uu"][e_mid["pos"]])).astype(int)
    o = np.argsort(contrib)[::-1][:N_TOP]
    print("    mid-ladder rung kz %d top-%d positive atoms: %s"
          % (r_mid["kz"], N_TOP,
             ", ".join("n=%d (%s) %+0.3f" % (vals[i],
                                             pp_label(int(
                                                 vals[i])),
                                             contrib[i])
                       for i in o)))
    small = (int(k90s.max()) <= K_SMALL and len(u90) <= K_UNION)
    h2 = ("SET-SMALL(k90max=%d, union=%d)" % (int(k90s.max()),
                                              len(u90))
          if small else
          "SET-DIFFUSE(k90 med %d, union %d)"
          % (int(np.median(k90s)), len(u90)))
    check("H2.1 typed (2): %s (bars K_SMALL = %d, K_UNION = %d)"
          % (h2, K_SMALL, K_UNION), True)

    # ------------------------------------------------------------ H3
    section("H3 -- THE MINIMAL ENLARGEMENT + (d)/(e) RE-RUN")
    mm = np.array([r["m"] for r in rungs])
    XX = np.exp(2.0 * aa)
    Npos = np.array([e["Npos"] for e in ES], float)
    Ndeep = np.array([e["Ndeep"] for e in ES], float)
    h2v = np.array([e["head2"] for e in ES])
    sl_N, se_N, r2_N = jack_slope(np.log(XX), np.log(Npos))
    sl_H, se_H, r2_H = jack_slope(np.log(mm), np.log(h2v))
    print("    minimal atomwise enlargement = ALL positive-"
          "weight deep atoms: N+ med %d (%d..%d), share of deep "
          "atoms med %.2f; growth log N+ vs log X: slope %+.3f "
          "+- %.3f (R^2 %.2f)"
          % (int(np.median(Npos)), int(Npos.min()),
             int(Npos.max()),
             float(np.median(Npos / Ndeep)), sl_N, 2 * se_N,
             r2_N))
    print("    enlarged head head2 = head_B(cB) + P+: med %.3f "
          "(%.3f..%.3f); |tail2| = head2 - m med %.3f; "
          "P+ med %.3f"
          % (float(np.median(h2v)), float(np.min(h2v)),
             float(np.max(h2v)),
             float(np.median(h2v - mm)),
             float(np.median([e["P"] for e in ES]))))
    print("    (d) re-run TYPED tau-screen log head2 vs log m: "
          "slope %+.3f +- 2SE %.3f (R^2 %.2f)"
          % (sl_H, 2 * se_H, r2_H))
    rep = ("REPAIR-FINITE(slope=%+.3f)" % sl_N
           if sl_N <= GROW_BAR else
           "REPAIR-GROWING(X^%.2f)" % sl_N)
    if abs(sl_H) <= SLOPE_PASS:
        hf = "HEADFLOOR2-O1(slope=%+.3f)" % sl_H
    elif sl_H >= SLOPE_RELOC:
        hf = "HEADFLOOR2-RELOC(slope=%+.3f)" % sl_H
    else:
        hf = "HEADFLOOR2-AMBIG(slope=%+.3f)" % sl_H
    print("    (e) named: tail2 <= 0 is deterministic for ANY "
          "nonnegative comb, but the head that buys it carries "
          "med %d atoms and grows ~ X^%.2f -- the enlarged head "
          "is explicit yet NOT uniformly finite; the open "
          "arithmetic content head2 > |tail2| (gap m_h) now "
          "lives on that growing support"
          % (int(np.median(Npos)), sl_N))
    check("H3.1 typed (3): %s + %s (bands PASS |s| <= %.2f, "
          "RELOC s >= %.2f; GROW_BAR %.2f)"
          % (rep, hf, SLOPE_PASS, SLOPE_RELOC, GROW_BAR), True)

    # ------------------------------------------------------------ C
    section("C -- controls on this surface at kz %d" % CTRL_KZ)
    rr9 = core.build_window(CTRL_KZ)
    N_E = int(math.floor(math.exp(2.0 * rr9["alpha"]))) + 1
    lamE_ = lambda_eps(N_E)
    nnE = np.nonzero(np.abs(lamE_) > 1e-12)[0]
    ctl = {}
    ctl["Epstein"] = build_rung(CTRL_KZ, comb=(
        np.log(nnE.astype(float)),
        2.0 * lamE_[nnE] / np.sqrt(nnE.astype(float))),
        need_sm=False)
    ctl["scramble"] = build_rung(CTRL_KZ, scramble_seed=1,
                                 need_sm=False)
    ctl["smooth"] = build_rung(CTRL_KZ, smooth_world=True,
                               need_sm=False)
    fired = True
    for name, r in ctl.items():
        if r is None:
            print("    %-9s: rung dies -> fires" % name)
            continue
        # cert2 at every cut: head2(c) - |tail2(c)| with the same
        # R+ absorption applied at each cut
        pos_all = r["qan"] > 0.0
        cqp = np.cumsum(np.where(pos_all, r["qa"], 0.0))
        Pdeep = float(np.sum(np.where(pos_all, r["qa"], 0.0))) \
            - cqp
        h2c = r["head_B"] + Pdeep
        t2c = r["tail_B"] - Pdeep
        cert2 = h2c - np.abs(t2c)
        nc2 = int(np.sum(cert2 > 0))
        f = (r["m"] < 0) and nc2 == 0
        fired &= f
        extra = ""
        if name == "Epstein":
            extra = ("  [negative masses: tail2 <= 0 measured "
                     "%s, premise n/a]"
                     % ("yes" if float(np.max(t2c)) <= 0
                        else "NO (max %+.2e)"
                        % float(np.max(t2c))))
        print("    %-9s: m %+.3e  cert2 > 0 cuts %d -> %s%s"
              % (name, r["m"], nc2,
                 "FIRES" if f else "SILENT", extra), flush=True)
    check("C1 WARD all three controls fire (m < 0 and cert2 < 0 "
          "at every cut -- the repair cannot manufacture a "
          "certificate without the wall)", fired, kill="K2")

    return finish(dict(h1=h1, h2=h2, rep=rep, hf=hf))


def finish(labels):
    section("V -- FROZEN VERDICT")
    n_pass = sum(1 for _n, okk in CHECKS if okk)
    n_tot = len(CHECKS)
    if KILLS:
        VERDICT = {"K1": "PIPELINE-BROKEN",
                   "K2": "WARD-BROKEN"}[KILLS[0]]
        print("\n  VERDICT: %s" % VERDICT)
    else:
        VERDICT = ("TAILREPAIR-MEASURED / %(h1)s / %(h2)s / "
                   "%(rep)s / %(hf)s" % labels)
        print("\n  VERDICT: %s" % VERDICT)
    print("""
  HONEST FRAME (as frozen): the repair is MEASURED SURFACE
  STRUCTURE.  Absorbing the positive-weight region restores a
  deterministic tail sign for any nonnegative comb, at the
  measured price of a head support that grows with the window;
  the one-sided bound head2 > |tail2| (gap m_h) remains the open
  arithmetic content at every depth.  NO RH claim.  No marker
  moves.""")
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed"
          % (time.time() - T0, n_tot, n_tot - n_pass))
    return 0 if n_pass == n_tot else 1


if __name__ == "__main__":
    raise SystemExit(main())
