#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""christoffel_zone_envelope_probe -- PRIME.CASE.ZONESPLIT.01
(EXPLORATION ONLY, experiments/; round 43: freeze the smallest valid
critical-zone exponent theta for the repaired Christoffel domination
theorem, 2026-08-09).

CONTEXT (machinery verbatim from christoffel_hypotheses_probe /
freetail_case_bridge_probe): the deployed tilde-measures carry atoms
nu~_m at neg nodes y_m; T_m = nu~_m K_h(y_m, y_m); the port scale is
a_m = 2 h^2 (1 - y_m).  The repaired theorem splits the band into a
critical zone C_h = {a <= h^(2 theta)} -- inside which all measured
criticality lives -- and its complement, on which the testing margin
1 - T_m must stay uniformly positive.  Measured margin minimizers
sit at a = 89..3754 (kz 26 at a = 3754 ~ h^1.40, i.e. theta ~ 0.70
there); the strategy memo proposes theta = 3/4 as the frozen safety
split.  This probe measures the outside envelope on ALL 42 reachable
rungs and freezes the smallest grid theta that confines the
difficulty.

THE LADDER (frozen, verbatim from certified_ladder_probe):
core.frame_a_zones() restricted to h <= 900 -- the 42 reachable
rungs (h 142..878), sorted by (h, kz); the deep half = the 21
highest-h rungs.

FROZEN PROTOCOL (2026-08-09; constants frozen before the first run:
theta grid {0.50, 0.60, 2/3, 0.70, 0.75, 0.80}; deep-half margin
bar 0.02; cut-stability tolerance 30 %; materiality factor 1/2;
alias index = rank inward from x = +1 in a-ascending order; H1
oscillation constants verbatim A_h = 20 two-sided, C = 2, 33
samples, top-3; heavy rungs kz {9, 12, 13, 26, 40}; Z4 fit split
leave-last-third-out 28/14 by ascending h; control kz 9 scramble
seed 1 at the memo cut theta = 3/4):

 Z1  ENVELOPE TABLE: eta_out(h, theta) = min over deployed neg
     nodes with a_m > h^(2 theta) of (1 - T_m), plus the minimizing
     alias m*(h, theta); the full 42 x 6 table (compact), and per
     theta the inf over the deep half and the inf over all rungs.

 Z2  FREEZE DECISION (typed): theta* = the smallest grid theta with
     (i)   inf over the deep half of eta_out(theta) >= 0.02,
     (ii)  cut stability: moving the cut by ONE alias in both
           directions (the outside set starts one node earlier /
           later in a-order, per rung) keeps the deep-half inf the
           same sign and within 30 % of the base value,
     (iii) sharpness: the next-smaller grid theta FAILS (i) or has
           materially less deep-half margin (< 1/2 of the
           candidate's); vacuously true at the grid minimum 0.50.
     Typed ZONE-FROZEN(theta*) with the numbers.  ZONE-OPEN iff no
     grid theta (even 0.80) passes (i), or none passes (i)+(ii)
     (the difficulty is not confinable STABLY at any tested
     exponent -- honest).  If the three-criteria set is empty while
     (i)+(ii) holds somewhere, freeze the smallest theta passing
     (i)+(ii) and print the (iii) plateau flag honestly (the grid
     does not resolve sharpness).

 Z3  OUTLIER SEPARATION (the H1/H2 question): per heavy rung the
     top-3 bulk oscillation nodes (oscillation of log w_h over
     I_h(x), verbatim H1: two-sided bulk min(1 -+ x) >= A_h/h^2,
     C = 2, 33 samples) vs the margin minimizer m*(h, theta_Z3);
     typed OUTLIERS-HARMLESS iff the two node sets are disjoint on
     EVERY heavy rung (the density defects are measure-zero for the
     margin -- the H1/H2 failures are the wrong tool, not theorem
     killers), else OUTLIERS-DANGEROUS (they coincide somewhere --
     the defects DO carry margin risk).  theta_Z3 = theta* if
     frozen, else the memo 3/4 (for the record).

 Z4  MARGIN LAW INSIDE (report): inside C_h(theta_Z3) the min
     margin per rung eta^C_h = min_{a <= h^(2 theta)} (1 - T_m);
     the h-trend (shallow/deep pair medians), and envelope fits
     eta^C_h ~ c, c/log h, c/log^2 h, c h^-p -- trained on the 28
     lowest-h rungs, scored by held-out RMSE on the 14 deepest
     (leave-last-third-out); the power law needs positive train
     margins (else typed n/a).  This eta^C_h is the quantity the
     arithmetic input must beat; report which envelope fits best.

 C   CONTROLS (kz 9, scramble seed 1): the scrambled window must
     drive eta_out(theta = 3/4) NEGATIVE (value control) while the
     pipeline persists (chain completes).

FROZEN CONCRETIZATIONS (pre-registered with the protocol, before
the first run):
  (i)   alias index m = 1, 2, ... = neg nodes ranked by a ascending
        (m = 1 closest to x = +1), extending the port-alias
        numbering of christoffel_hypotheses_probe to all nodes.
  (ii)  an empty outside set (cut above max a) would print n/a and
        be excluded from the infs; it cannot occur on this ladder
        (max a ~ 4 h^2 >> h^1.6 for all h <= 900).
  (iii) Z2 (iii) is vacuous at the grid minimum 0.50 (no smaller
        grid point exists).
  (iv)  Z3/Z4 run at the memo theta = 3/4 when Z2 types ZONE-OPEN,
        purely for the record; the typed labels stand either way.
  (v)   all Z1/Z2 infs are over the FULL deployed neg node set
        (bulk AND the -1 edge); no bulk restriction -- the envelope
        is the honest two-edge quantity the theorem needs.

KILLS: pipeline breaks (wrong rung count, chain short on any rung,
non-finite T or margins, heavy rung missing from the ladder) ->
PIPELINE-BROKEN; control silent -> CONTROL-DEAD.  The Z2/Z3/Z4
labels are MEASUREMENTS, never kills: ZONE-OPEN or
OUTLIERS-DANGEROUS is a finding.

VERDICT (frozen enum): ZONESPLIT-MEASURED (+ typed sublabels
ZONE-FROZEN(theta*) / ZONE-OPEN, OUTLIERS-HARMLESS /
OUTLIERS-DANGEROUS, INSIDE-LAW=<c | c/log | c/log^2 | c*h^-p |
n/a>) / PIPELINE-BROKEN / CONTROL-DEAD.

SPEC AMENDMENTS (fail-first history preserved):
  v1 (2026-08-09): initial freeze, everything above.
  v2 (2026-08-09, after the first run -- which already returned
     ZONE-FROZEN(0.700) + OUTLIERS-DANGEROUS + INSIDE-LAW=c/log^2
     with all checks green): two transparency fixes, neither moves
     a number or a bar: (a) a dead pre-assignment in the Z1 table
     loop removed (the global minimum was always read from the
     suffix structure); (b) Z2 criterion (ii) is now EVALUATED
     independently of (i) so the per-theta table prints the honest
     stability status of every grid point (v1 gated (ii) on (i),
     printing "fail" for thetas whose cut was in fact stable).  The
     freeze rule itself is unchanged (theta* still needs all three
     criteria), and theta* = 0.700 is unchanged.

NO RH claim: eta_out and eta^C_h are measured finite-h envelopes of
the deployed v563 window family; a frozen theta* is a zone split
for the finite ladder, not a proof of the domination theorem, and
no marker moves.

FIREWALL: no zeros, no prime oracles (AST scan: zetazero, nzeros,
primerange, isprime, primepi, nextprime, prevprime); v563
READ-ONLY; RNG only in the scramble control; stdout only.

Sources (read-only): v563_paper2_readouts; christoffel_hypotheses_
probe (chain + free-tail density machinery, verbatim), declared
inputs.

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/christoffel_zone_envelope_probe.py
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

H_LADDER_MAX = 900             # reachable-rung cap (the 42 rungs)
N_RUNGS_EXP = 42               # frozen expected rung count
HEAVY = (9, 12, 13, 26, 40)    # heavy rungs (Z3 + context)
THETAS = (0.50, 0.60, 2.0 / 3.0, 0.70, 0.75, 0.80)
MARGIN_BAR = 0.02              # Z2 (i): deep-half inf bar
STAB_REL = 0.30                # Z2 (ii): 30 % cut-shift tolerance
HALF_FACTOR = 0.5              # Z2 (iii): materiality factor
THETA_MEMO = 0.75              # the memo split (control + fallback)
A_H = 20.0                     # H1 bulk cut (two-sided), verbatim
C_OSC = 2.0                    # H1 interval half-width factor
N_OSC = 33                     # H1 samples per interval
TOP_K = 3                      # Z3 top oscillation nodes per rung
N_TRAIN = 28                   # Z4 leave-last-third-out split
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


# ------------------------------------------------------------------ pipeline
# (grid density, folded arm measures, Lanczos chain, CD kernel, free-tail
#  m-function: verbatim from christoffel_hypotheses_probe)

def grid_density(c):
    c = np.asarray(c, float)
    a = np.concatenate([c, c[-2:0:-1]])
    d = np.fft.fft(a)
    assert float(np.max(np.abs(d.imag))) <= 1e-9 * max(
        1.0, float(np.max(np.abs(d.real))))
    return d.real


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


def build_rung(kz, scramble_seed=None):
    """Window -> pos/neg folded measures -> chain -> CD diagonal + T."""
    rr = core.build_window(kz, scramble_seed=scramble_seed)
    h, M, D, alpha = rr["h"], rr["M"], rr["D"], rr["alpha"]
    uu = np.asarray(rr["uu"], float)
    mm = 2.0 * np.asarray(rr["lam"], float)
    c_at, _ = core.atom_lags_at(alpha, M, uu, mm)
    c_ar = np.asarray(core.arch_lags(M, D), float)
    d = grid_density(c_ar + np.asarray(c_at, float))
    L = 2 * M - 2
    xs, ws, _ = folded_measure(d, L, +1.0)
    ys, vs, _ = folded_measure(d, L, -1.0)
    al, be, m0, steps = lanczos_chain(xs, ws, h + 1)
    if steps < h + 1:
        return None
    Pn = eval_chain(al, be, m0, ys, h)
    Kdiag = np.sum(Pn ** 2, axis=1)
    T = vs * Kdiag
    return dict(kz=kz, h=h, L=L, xs=xs, ws=ws, ys=ys, vs=vs,
                m0=m0, Kdiag=Kdiag, T=T,
                A2=2.0 * be[:h], B2=2.0 * al[:h])


def m_strip(A2, B2v, E):
    """Exact m-function of J_h^ft on the essential spectrum: free
    boundary value + coefficient stripping (Herglotz-preserving)."""
    m = 0.5 * (-E + 1j * np.sqrt(4.0 - E * E))
    for k in range(len(A2) - 1, -1, -1):
        m = 1.0 / (B2v[k] - E - (A2[k] ** 2) * m)
    return m


def w_ft(r, x):
    """The exact free-tail ac density w_h at x (any shape)."""
    E = np.clip(2.0 * np.asarray(x, float), -2.0 + 1e-15, 2.0 - 1e-15)
    return 2.0 * r["m0"] * m_strip(r["A2"], r["B2"], E).imag / math.pi


# ------------------------------------------------------- zone machinery
def ladder_zones():
    """The 42 reachable rungs: frame_a_zones with h <= H_LADDER_MAX
    (h from the same closed formula frame_a_zones uses)."""
    out = []
    for kz in core.frame_a_zones():
        D_k = 0.5 * float(core.G_ALL[kz]) / float(core.NU_MAIN)
        M_k = int(math.ceil(float(core.U_ALL[kz]) / D_k - 1.0e-9)) + 1
        if M_k % 2:
            M_k += 1
        if M_k // 2 <= H_LADDER_MAX:
            out.append(kz)
    return out


def zone_scan(r):
    """a-ascending order + suffix/prefix minima of the margin, so
    every cut position is answered in O(1)."""
    h = r["h"]
    a = 2.0 * h * h * (1.0 - r["ys"])
    o = np.argsort(a, kind="stable")
    a_s = a[o]
    marg = 1.0 - r["T"][o]
    n = len(a_s)
    suf = np.empty(n + 1)
    sufi = np.empty(n + 1, dtype=int)
    suf[n] = np.inf
    sufi[n] = -1
    for j in range(n - 1, -1, -1):
        if marg[j] <= suf[j + 1]:
            suf[j], sufi[j] = marg[j], j
        else:
            suf[j], sufi[j] = suf[j + 1], sufi[j + 1]
    pre = np.empty(n)
    prei = np.empty(n, dtype=int)
    best, bi = np.inf, -1
    for j in range(n):
        if marg[j] < best:
            best, bi = marg[j], j
        pre[j], prei[j] = best, bi
    r.update(a_s=a_s, marg_s=marg, order=o, suf=suf, sufi=sufi,
             pre=pre, prei=prei, n_neg=n)


def cut_index(r, theta):
    """First a-ascending index OUTSIDE the zone {a <= h^(2 theta)}."""
    return int(np.searchsorted(r["a_s"], r["h"] ** (2.0 * theta),
                               side="right"))


def eta_out(r, theta, shift=0):
    """(eta_out, alias m*, global neg index) at the (shifted) cut."""
    j = min(max(cut_index(r, theta) + shift, 0), r["n_neg"])
    if j >= r["n_neg"]:
        return float("inf"), -1, -1
    ji = int(r["sufi"][j])
    return float(r["suf"][j]), ji + 1, int(r["order"][ji])


def eta_in(r, theta):
    """(eta^C_h, alias, a at the minimizer) inside the zone."""
    j = cut_index(r, theta)
    if j == 0:
        return None
    ji = int(r["prei"][j - 1])
    return float(r["pre"][j - 1]), ji + 1, float(r["a_s"][ji])


def top_osc_nodes(r):
    """Verbatim H1: top-K bulk oscillation nodes of log w_h over
    I_h(x) (two-sided bulk, C = C_OSC, N_OSC samples)."""
    h = r["h"]
    bulk = np.minimum(1.0 - r["ys"], 1.0 + r["ys"]) >= A_H / h ** 2
    bi = np.nonzero(bulk)[0]
    yb = r["ys"][bi]
    dx = C_OSC * (np.sqrt(1.0 - yb ** 2) / h + 1.0 / h ** 2)
    tt = np.linspace(-1.0, 1.0, N_OSC)
    pts = np.clip(yb[:, None] + dx[:, None] * tt[None, :],
                  -1.0 + 1e-15, 1.0 - 1e-15)
    lw = np.log(np.maximum(w_ft(r, pts.ravel()), 1e-300))
    lw = lw.reshape(pts.shape)
    osc = lw.max(axis=1) - lw.min(axis=1)
    top = bi[np.argsort(-osc)[:TOP_K]]
    return top, osc[np.argsort(-osc)[:TOP_K]]


def fit_envelopes(hs, ys):
    """Z4: four candidate envelopes, leave-last-third-out."""
    hs = np.asarray(hs, float)
    ys = np.asarray(ys, float)
    out = {}
    regs = (("c", np.ones_like(hs)),
            ("c/log", 1.0 / np.log(hs)),
            ("c/log^2", 1.0 / np.log(hs) ** 2))
    for name, reg in regs:
        c = float(np.sum(ys[:N_TRAIN] * reg[:N_TRAIN])
                  / np.sum(reg[:N_TRAIN] ** 2))
        rmse = float(np.sqrt(np.mean(
            (ys[N_TRAIN:] - c * reg[N_TRAIN:]) ** 2)))
        out[name] = ("c=%.5f" % c, rmse)
    if np.all(ys[:N_TRAIN] > 0.0):
        A = np.vstack([np.ones(N_TRAIN), -np.log(hs[:N_TRAIN])]).T
        sol, *_ = np.linalg.lstsq(A, np.log(ys[:N_TRAIN]),
                                  rcond=None)
        c, p = math.exp(float(sol[0])), float(sol[1])
        rmse = float(np.sqrt(np.mean(
            (ys[N_TRAIN:] - c * hs[N_TRAIN:] ** (-p)) ** 2)))
        out["c*h^-p"] = ("c=%.5f p=%.3f" % (c, p), rmse)
    else:
        out["c*h^-p"] = ("n/a (nonpositive train margin)", None)
    return out


def main():
    section("PRIME.CASE.ZONESPLIT.01 -- critical-zone envelope + "
            "freeze of theta (EXPLORATION ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s"
          % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
    print("    NO RH claim; no marker moves.")
    print("\nS0 -- firewall")
    check("S0.1 AST firewall clean", not ast_scan(BANNED_IDS))

    section("B0 -- the ladder (all reachable rungs, h <= %d)"
            % H_LADDER_MAX)
    zones = ladder_zones()
    check("B0.1 frozen rung count: %d reachable rungs" % N_RUNGS_EXP,
          len(zones) == N_RUNGS_EXP, "found %d" % len(zones),
          kill="PIPELINE")
    check("B0.2 heavy rungs on the ladder",
          all(kz in zones for kz in HEAVY), kill="PIPELINE")
    if "PIPELINE" in KILLS:
        return finish(None, None, None, None)
    R = []
    ok = True
    fin = True
    for kz in zones:
        r = build_rung(kz)
        ok &= r is not None
        if r is None:
            print("    kz %-3d: CHAIN SHORT" % kz, flush=True)
            continue
        fin &= bool(np.all(np.isfinite(r["T"])))
        zone_scan(r)
        R.append(r)
    R.sort(key=lambda r: (r["h"], r["kz"]))
    check("B0.3 all %d chains complete" % len(zones), ok,
          kill="PIPELINE")
    check("B0.4 all T finite", fin, kill="PIPELINE")
    if "PIPELINE" in KILLS:
        return finish(None, None, None, None)
    deep = R[N_RUNGS_EXP // 2:]
    print("    h range %d..%d; deep half = %d rungs (h >= %d); "
          "[%.1f s]" % (R[0]["h"], R[-1]["h"], len(deep),
                        deep[0]["h"], time.time() - T0))

    # ---------------------------------------------------------- Z1
    section("Z1 -- THE ENVELOPE TABLE eta_out(h, theta) = min over "
            "{a > h^(2 theta)} of (1 - T), with minimizing alias")
    th_lab = ["%.3f" % th for th in THETAS]
    print("\n    kz   h    glob-min(1-T)@a      "
          + " ".join("th=%s      " % s for s in th_lab))
    table = {th: [] for th in THETAS}
    for r in R:
        # global min = suffix min at j = 0 (all nodes outside)
        g_eta = float(r["suf"][0])
        g_a = float(r["a_s"][int(r["sufi"][0])])
        cells = []
        for th in THETAS:
            e, m_star, _gi = eta_out(r, th)
            table[th].append(e)
            cells.append("%+.3f/%-5d" % (e, m_star))
        print("    %-4d %-4d %+.4f@%-10.1f " % (r["kz"], r["h"],
                                                g_eta, g_a)
              + " ".join(cells), flush=True)
    print("\n    per theta:  inf(all 42)   inf(deep half)")
    inf_all = {}
    inf_deep = {}
    for th in THETAS:
        inf_all[th] = min(table[th])
        inf_deep[th] = min(table[th][N_RUNGS_EXP // 2:])
        print("      theta=%.3f  %+.4f       %+.4f"
              % (th, inf_all[th], inf_deep[th]))
    check("Z1.1 envelope table complete (finite where the outside "
          "set is nonempty)",
          all(np.isfinite(v) for v in inf_all.values()),
          kill="PIPELINE")

    # ---------------------------------------------------------- Z2
    section("Z2 -- FREEZE DECISION: smallest theta with (i) deep "
            "inf >= %.2f, (ii) cut-stable 30%%, (iii) sharp"
            % MARGIN_BAR)
    rows = {}
    for idx, th in enumerate(THETAS):
        base = inf_deep[th]
        e_min = min(eta_out(r, th, shift=-1)[0] for r in deep)
        e_plu = min(eta_out(r, th, shift=+1)[0] for r in deep)
        c1 = base >= MARGIN_BAR
        same_sign = ((base > 0.0) == (e_min > 0.0)
                     and (base > 0.0) == (e_plu > 0.0))
        c2 = (same_sign
              and abs(e_min - base) <= STAB_REL * abs(base)
              and abs(e_plu - base) <= STAB_REL * abs(base))
        if idx == 0:
            c3 = True                       # vacuous at grid minimum
        else:
            prev = inf_deep[THETAS[idx - 1]]
            c3 = (prev < MARGIN_BAR) or (prev < HALF_FACTOR * base)
        rows[th] = (base, e_min, e_plu, c1, c2, c3)
        print("    theta=%.3f: deep inf %+.4f | cut-1 %+.4f cut+1 "
              "%+.4f | (i)%s (ii)%s (iii)%s"
              % (th, base, e_min, e_plu,
                 "PASS" if c1 else "fail",
                 "PASS" if c2 else "fail",
                 "PASS" if c3 else "fail"), flush=True)
    full = [th for th in THETAS if all(rows[th][3:6])]
    stab = [th for th in THETAS if rows[th][3] and rows[th][4]]
    plateau = False
    if full:
        theta_star = full[0]
    elif stab:
        theta_star = stab[0]
        plateau = True
        print("    (iii) PLATEAU: no grid theta is sharp; frozen at "
              "the smallest theta passing (i)+(ii) -- the grid does "
              "not resolve sharpness (concretization, honest).")
    else:
        theta_star = None
    if theta_star is not None:
        b, em, ep, *_ = rows[theta_star]
        zone_label = "ZONE-FROZEN(theta*=%.3f)" % theta_star
        print("\n    FROZEN: theta* = %.3f  (deep inf %+.4f >= "
              "%.2f; cut shifts %+.4f/%+.4f within %.0f%%; %s)"
              % (theta_star, b, MARGIN_BAR, em, ep,
                 100 * STAB_REL,
                 "(iii) plateau-flagged" if plateau else
                 "next-smaller theta fails/half"))
    else:
        zone_label = "ZONE-OPEN"
        print("\n    ZONE-OPEN: no grid theta (even 0.80) passes "
              "(i)+(ii) -- the difficulty is not confinable at any "
              "tested exponent (honest).")
    check("Z2.1 typed: %s" % zone_label, True)
    theta_z3 = theta_star if theta_star is not None else THETA_MEMO

    # ---------------------------------------------------------- Z3
    section("Z3 -- OUTLIER SEPARATION: H1 top-%d oscillation nodes "
            "vs the margin minimizer at theta=%.3f (heavy rungs)"
            % (TOP_K, theta_z3))
    harmless = True
    for r in R:
        if r["kz"] not in HEAVY:
            continue
        top, oscv = top_osc_nodes(r)
        h = r["h"]
        _e, m_star, gi = eta_out(r, theta_z3)
        a_min = 2.0 * h * h * (1.0 - r["ys"][gi])
        a_top = 2.0 * h * h * (1.0 - r["ys"][top])
        clash = gi in set(int(t) for t in top)
        harmless &= not clash
        print("    kz %-3d h %4d: osc top-%d nodes a = %s (osc %s)"
              % (r["kz"], h, TOP_K,
                 " ".join("%.1f" % v for v in a_top),
                 " ".join("%.2f" % v for v in oscv)))
        print("                 margin minimizer m*=%d at a = %.1f "
              "(1-y = %.3e) -> %s"
              % (m_star, a_min, 1.0 - r["ys"][gi],
                 "CLASH" if clash else "disjoint"), flush=True)
    out_label = ("OUTLIERS-HARMLESS" if harmless
                 else "OUTLIERS-DANGEROUS")
    check("Z3.1 typed: %s (oscillation sups vs margin minimizers)"
          % out_label, True)

    # ---------------------------------------------------------- Z4
    section("Z4 -- MARGIN LAW INSIDE C_h(theta=%.3f): eta^C_h = "
            "min_{a <= h^(2 theta)} (1 - T)" % theta_z3)
    hs, es = [], []
    ok_z4 = True
    for r in R:
        v = eta_in(r, theta_z3)
        ok_z4 &= v is not None
        if v is None:
            print("    kz %-3d h %4d: EMPTY ZONE" % (r["kz"], r["h"]))
            continue
        e, m_star, a_at = v
        hs.append(r["h"])
        es.append(e)
        print("    kz %-3d h %4d: eta^C_h %+.5f at alias %-4d "
              "(a = %.1f)" % (r["kz"], r["h"], e, m_star, a_at),
              flush=True)
    check("Z4.0 inside zone nonempty on every rung", ok_z4,
          kill="PIPELINE")
    law_label = "n/a"
    if ok_z4:
        sh = float(np.median(es[:2]))
        dp = float(np.median(es[-2:]))
        print("\n    h-trend: shallow-pair median %+.5f -> deep-pair "
              "median %+.5f (%s)"
              % (sh, dp, "shrinking" if dp < sh else
                 "non-shrinking"))
        fits = fit_envelopes(hs, es)
        best, best_rmse = None, None
        for name in ("c", "c/log", "c/log^2", "c*h^-p"):
            par, rmse = fits[name]
            print("    fit %-8s: %-22s held-out RMSE %s"
                  % (name, par,
                     "%.5f" % rmse if rmse is not None else "n/a"))
            if rmse is not None and (best_rmse is None
                                     or rmse < best_rmse):
                best, best_rmse = name, rmse
        law_label = best if best is not None else "n/a"
        print("    best envelope (leave-last-third-out): %s"
              % law_label)
    check("Z4.1 typed: INSIDE-LAW=%s (the quantity the arithmetic "
          "input must beat)" % law_label, True)

    # ------------------------------------------------------------ C
    section("C -- controls (kz 9, scramble seed 1): eta_out at the "
            "memo cut theta = %.2f must flip negative" % THETA_MEMO)
    rs = build_rung(9, scramble_seed=1)
    if not check("C0 scramble chain completes (pipeline persists)",
                 rs is not None, kill="PIPELINE"):
        return finish(zone_label, out_label, law_label, None)
    zone_scan(rs)
    e_s, m_s, _ = eta_out(rs, THETA_MEMO)
    r9 = next(r for r in R if r["kz"] == 9)
    e_r, _m, _ = eta_out(r9, THETA_MEMO)
    print("    scramble eta_out(%.2f) = %+.4f at alias %d "
          "(real kz 9: %+.4f) -> %s"
          % (THETA_MEMO, e_s, m_s, e_r,
             "FIRES" if e_s < 0.0 else "silent"), flush=True)
    ctrl = "eta_out<0" if e_s < 0.0 else None
    check("C1 CONTROL FIRES: scrambled eta_out negative",
          e_s < 0.0, kill="CONTROL")
    return finish(zone_label, out_label, law_label, ctrl)


def finish(zone_label, out_label, law_label, ctrl):
    section("V -- FROZEN VERDICT")
    n_pass = sum(1 for _n, okk in CHECKS if okk)
    n_tot = len(CHECKS)
    if "PIPELINE" in KILLS:
        VERDICT = "PIPELINE-BROKEN"
    elif "CONTROL" in KILLS:
        VERDICT = "CONTROL-DEAD"
    else:
        VERDICT = "ZONESPLIT-MEASURED"
    sub = []
    if zone_label:
        sub.append(zone_label)
    if out_label:
        sub.append(out_label)
    if law_label:
        sub.append("INSIDE-LAW=%s" % law_label)
    if ctrl:
        sub.append("CONTROL=%s" % ctrl)
    print("\n  VERDICT: %s%s" % (VERDICT,
                                 (" (%s)" % " + ".join(sub))
                                 if sub else ""))
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed"
          % (time.time() - T0, n_tot, n_tot - n_pass))
    return 0 if n_pass == n_tot else 1


if __name__ == "__main__":
    raise SystemExit(main())
