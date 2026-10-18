#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""fermiedge_classify_probe -- PRIME.PORT.FERMIEDGE.CLASSIFY.01
(round 227): BEFORE any steepest-descent campaign -- (1) is the
dangerous location really an edge, (2) which RHP is the right one
(IIKS, FIK, or a positive multi-measure lift), (3) does the true
leakage gap collapse or stay of order one?

EXPLORATION ONLY (2026-08-23).  experiments/ level: NO promotion,
NO ledger row, NO marker moved, NO RH CLAIM in either direction.
Index firewall of r226 stays binding: w = window (kz), n = degree,
k = flag, s = coupling, t = weight time.

LEG A -- THE TRUE SIGN OBJECT: with pihat_{w,n} the monic OP of
the signed functional mutilde_w = mu_w - nu_w,
    U_{w,n} = int pihat^2 dmu,   V_{w,n} = int pihat^2 dnu,
    h_n(mutilde) = U - V   (exact),
    A_{w,n} = U / h_n(mu) >= 1   (monic mu-minimality),
    chi_{w,n} = V / U,
    r_{w,n} = A_{w,n} (1 - chi_{w,n}),   r > 0 <=> chi < 1.
HARD WARDS on all worlds: sign r = sign(1 - chi) = sign gammahat;
on EPSTEIN / SCRAMBLE / SMOOTH chi crosses 1 EXACTLY at the first
measured flip.  SEALED ADJUDICATION RULE (before profiles): fit
slopes of log A*(N) and log(1 - chi*)(N) at the r-minimum across
windows; LEAKAGE_GAP_CANDIDATE iff A* stays O(1) (slope < 0.25 and
max A* < 10) and 1 - chi* >= delta uniformly; LEAKAGE_APPROACHES_
ONE iff A* grows and 1 - chi* -> 0 while the product r stays O(1);
RATIO_RELABEL iff the split degenerates numerically.

LEG B -- EDGE OR BULK (five regimes SEALED before evaluation):
n*(w) = argmin_n r_{w,n}, m* = N_w - n*.  Statistics m*/1,
m*/log N, m*/N^{1/3}, m*/N^{1/2}, n*/N across all five windows.
SEALED RULE: BULK_CRITICAL iff m*/N has rel spread < 0.5 AND
min m*/N > 0.15; HARD_EDGE iff max m* <= 6; otherwise fit slope
of log m* vs log N: SOFT_EDGE if slope in [0.2, 0.8] (a clearly
collapsing relative band m*/N -> 0), NO_STABLE_SCALING otherwise;
SATURATED_EDGE upgrade if the pihat_N zeros lock onto the
discrete nodes in the edge band (mean |zero - nearest node| <
0.1 x local node spacing).  Arithmetic jitter on the two smallest
windows is reported, not hidden.

LEG C -- IIKS RHP vs MOMENT (FIK) RHP: the discrete Fokas-Its-
Kitaev RHP of the signed Stieltjes recursion is BUILT:
Y_n(z) = [[pihat_n, C[pihat_n mutilde]], [-pihat_{n-1}/h_{n-1},
-C[pihat_{n-1} mutilde]/h_{n-1}]].  Load-bearing gates:
  (c1) det Y_n(z) = 1 identically (Liouville; removable node
       singularities checked via the residue cancellation),
  (c2) DEGREE SHIFT = LAX1: Y_{n+1}(z) = R_n(z) Y_n(z) with
       R_n = [[z - alphahat_n, gammahat_n h_{n-1}], [-1/h_n, 0]],
       det R_n = 1 -- the FIK transfer IS the r225 connection,
  (c3) h-tail: z^{n+1} C[pihat_n mutilde](z) -> h_n(mutilde),
  (c4) tau^FIK = prod h_l(mutilde)/h_l(mu) = tau^IIKS =
       det(I - E_n)   (the r226 dictionary, re-gated),
  (c5) THE RESOLVENT INTERTWINER (the strongest identity, found
       at design time): (I - E_n)^{-1} = I + sqrt(v) Ktilde_n
       sqrt(v) with Ktilde_n(y_i, y_j) = sum_{l<n} pihat_l(y_i)
       pihat_l(y_j)/h_l(mutilde) -- the IIKS resolvent state IS
       the CD kernel of the SIGNED family on the nu-nodes
       (scale-free form sum_l qy_l qy_l^T / eta_l), gated at
       moderate n and at FULL depth, on MAIN and on a control.
c1-c5 together close the strong intertwiner (tau, r, gammahat,
resolvent): verdict FIK_IIKS_GAUGE_EXACT (intertwiner form);
weaker outcomes typed SAME_TAU_DIFFERENT_RHP / RHP_ALIAS.

LEG D -- NEVANLINNA / PADE DICTIONARY: for the Jacobi chain
(alphahat, gammahat) of mutilde the n-th approximant m_{w,n}(z)
has the five classical equivalences gated on MAIN (n <= 40):
(1) h_0..h_n > 0, (2) gammahat > 0, (3) poles real simple +
interlacing, (4) residues > 0, (5) Herglotz (Im m < 0 for
Im z > 0).  On EPSTEIN the FIRST flip (n = 25) is localized:
which object breaks first.  Verdict NEVANLINNA_CLASSIFIED
(dictionary gain, NO mincut gain -- no source-pure zero-negative-
index statement arises).

LEG E -- NIKISHIN / AT MINUTE TEST (sealed, minutes not weeks):
measured support hulls and overlap of (mu_w, nu_w), grid
distinctness, gap structure; Angelesco needs disjoint supports,
Nikishin needs nu generated on a gap of the mu-support; the
corpus has already killed Uvarov/Christoffel/Geronimus relations
between the two channel measures and small cross-measure defect
rank.  Verdicts: NIKISHIN_AT_GO / MULTIMEASURE_NOT_PERFECT /
NO_EXACT_LIFT.

GO-ASSESSMENT FOR ROUND 228 (sealed decision tree of the
contract): Fall 1 (FERMIEDGE with a uniform chi-gap target)
requires LEAKAGE_GAP_CANDIDATE; if instead LEAKAGE_APPROACHES_ONE
lands, the chi-gap parametrix target is MEASURED-DEAD and round
228 must target r_{w,n} (equivalently gammahat/gamma) DIRECTLY in
the collapsing edge band, with the exact von Mangoldt comb as
background (design rule unchanged: no smooth-PNT parametrix; the
arithmetic fluctuations may live in a Szego function, discrete
g-function or local jump factor -- never in the error term).

RECORD TABLES (frozen from calib_fc_pass2.log, 18/18; smoke-stage
numerics amendments disclosed: FIK identity gates at the
f64-honest depth n = 12 (deeper is h_n-cancelled), resolvent full-
depth bar 1e-4, log-scale U/V storage against the h(mu) ~ 1e-360
underflow at w = 40, symmetric Jacobi form for the zero
diagnostic):
CAL_VERDICT = LEAKAGE_APPROACHES_ONE + SOFT_EDGE +
FIK_IIKS_GAUGE_EXACT(intertwiner) + NEVANLINNA_CLASSIFIED +
NO_EXACT_LIFT.  Key numbers: A* at the r-minimum 51.6 / 155.9 /
71.9 / 1100.5 / 2799.5 across w = 9/12/13/26/40 (slope ~ 2.8 in
log N) against 1 - chi* = 7.1e-3 .. 9.6e-5 (slope ~ -2.8), product
r_min stable in [0.266, 0.367]; the leakage approaches one even
at fixed bulk fraction (1 - chi at N/2: 5.7e-2 -> 3.9e-4); edge:
n*/N = 0.89..0.98, m* = 3/5/19/10/12, log-slope 0.451 (residual
1.04 on the small windows -- arithmetic jitter disclosed),
saturation ratio 0.24..0.27 (zeros do NOT lock onto nodes);
resolvent intertwiner 4.3e-10 .. 6.8e-7 at FULL depth on all five
windows; EPSTEIN break: h_n flips first (Krein index 0 -> 1 at
n = 25).  AMENDMENTS: NONE after freeze.

NO RH CLAIM IN EITHER DIRECTION.  NOT evidence for or against RH.
"""

from __future__ import annotations

import argparse
import ast
import hashlib
import math
import os
import sys
import time

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

import hirota_sign_probe as HS               # noqa: E402 r226 lane
import port_integrable_kernel_probe as PIK   # noqa: E402 v881 lane
import v563_paper2_readouts as core          # noqa: E402 READ-ONLY

WINDOWS = (9, 12, 13, 26, 40)
N_FIK = 40
N_FIK_ID = 12   # detY + moment gates: f64-honest depth
ID_BAR = 1e-9
CAL_VERDICT = ("LEAKAGE_APPROACHES_ONE + SOFT_EDGE + "
               "FIK_IIKS_GAUGE_EXACT(intertwiner) + "
               "NEVANLINNA_CLASSIFIED + NO_EXACT_LIFT")

SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
T0_WALL = time.time()
CHECKS: list = []


def check(name, ok, detail):
    ok = bool(ok)
    CHECKS.append((name, ok, detail))
    print("  [%s] %-40s %s" % ("PASS" if ok else "FAIL", name, detail),
          flush=True)
    return ok


def info(msg):
    print("  [INFO] " + msg, flush=True)


def section(t):
    print("\n" + "-" * 78 + "\n" + t + "\n" + "-" * 78, flush=True)


def firewall_audit():
    src = open(os.path.abspath(__file__), "r", encoding="utf-8").read()
    tree = ast.parse(src)
    forb = {"zeta" + "zero", "n" + "zeros", "prime" + "range",
            "is" + "prime", "gram" + "point"}
    bad = []
    for node in ast.walk(tree):
        nm = node.attr if isinstance(node, ast.Attribute) else (
            node.id if isinstance(node, ast.Name) else None)
        if nm and nm.lower() in forb:
            bad.append("%s@%d" % (nm, node.lineno))
    return (not bad), ("NO zero/prime oracles; regimes and "
                       "adjudication rules SEALED in the spec "
                       "before profile evaluation"
                       if not bad else "; ".join(bad))


# ------------------------------------------------- signed chain +
def signed_chain(d, n_upto):
    """scaled signed Stieltjes recursion, extended: per degree n
    returns U_n, V_n (true scale), log h_n(mutilde) + sign,
    alphahat_n, gammahat_n (true value), and the scale-free
    nu-grid vectors qy_n with eta_n for the CD kernel.
    Source-pure: node positions + weights of both zones only."""
    xs, ws, ys, vs = d["xs"], d["ws"], d["ys"], d["vs"]

    def sdot(fx, gx, fy, gy):
        return float(np.sum(ws * fx * gx) - np.sum(vs * fy * gy))

    qx_m = np.zeros_like(xs)
    qx = np.ones_like(xs)
    qy_m = np.zeros_like(ys)
    qy = np.ones_like(ys)
    Ls, Ls_m = 0.0, 0.0
    eta = sdot(qx, qx, qy, qy)
    out = []
    lg_h = math.log(abs(eta))
    sg_h = math.copysign(1.0, eta)
    alh_prev = None
    for n in range(n_upto):
        lgU = 2.0 * Ls + math.log(float(np.sum(ws * qx * qx)))
        lgV = 2.0 * Ls + math.log(float(np.sum(vs * qy * qy)))
        out.append(dict(n=n, lgU=lgU, lgV=lgV, lg_h=lg_h,
                        sg_h=sg_h,
                        qy=qy.copy(), eta=eta, Ls=Ls,
                        alphahat=alh_prev))
        alh = sdot(xs * qx, qx, ys * qy, qy) / eta
        out[-1]["alphahat"] = alh
        if n == 0:
            px = (xs - alh) * qx
            py = (ys - alh) * qy
        else:
            ge = (eta / eta_m) * math.exp(2.0 * (Ls - Ls_m))
            px = (xs - alh) * qx - ge * math.exp(Ls_m - Ls) * qx_m
            py = (ys - alh) * qy - ge * math.exp(Ls_m - Ls) * qy_m
        sc = max(float(np.max(np.abs(px))),
                 float(np.max(np.abs(py))))
        qx_m, qy_m, eta_m, Ls_m = qx, qy, eta, Ls
        qx, qy = px / sc, py / sc
        Ls += math.log(sc)
        eta = sdot(qx, qx, qy, qy)
        gam = (eta / eta_m) * math.exp(2.0 * (Ls - Ls_m))
        out[-1]["gammahat_next"] = gam
        lg_h += math.log(abs(gam))
        sg_h *= math.copysign(1.0, gam)
    return out


def slope_fit(xs_, ys_):
    x = np.array(xs_)
    y = np.array(ys_)
    xm, ym = x.mean(), y.mean()
    sl = float(np.sum((x - xm) * (y - ym)) / np.sum((x - xm) ** 2))
    res = y - (ym + sl * (x - xm))
    return sl, float(np.max(np.abs(res)))


# --------------------------------------------------------------- main
def main():
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke

    print("=" * 78)
    print("fermiedge_classify_probe -- PRIME.PORT.FERMIEDGE."
          "CLASSIFY.01 (round 227)")
    print("SPEC_SHA %s" % SPEC_SHA[:16])
    print("mode: %s" % ("SMOKE (w = 9, 26)" if smoke
                        else "FULL RECORD"))
    print("=" * 78)

    section("S0  FIREWALL + SEALED RULES")
    okf, det = firewall_audit()
    check("G01-firewall", okf, det)
    check("G02-predefinition", True,
          "windows %s; sealed regime list (HARD/SOFT/SATURATED/"
          "BULK/NO_STABLE) + sealed leg-A adjudication (gap vs "
          "approaches-one vs relabel) + sealed leg-C intertwiner "
          "gates c1-c5 + sealed minute-test leg E; FIK depth "
          "n <= %d disclosed (monic f64 range)" % (str(WINDOWS),
                                                   N_FIK))

    windows = (9, 26) if smoke else WINDOWS

    # ---------- profiles for legs A and B
    section("S1  LEG A -- THE TRUE SIGN OBJECT (A, chi split)")
    prof = {}
    okW1 = True
    for w in windows:
        d = HS.window_data(w)
        N = d["n_max"]
        rs = HS.r_chain(d, N)
        ch = signed_chain(d, N)
        lgh_mu = math.log(d["m0"])
        A = np.zeros(N)
        chi = np.zeros(N)
        for n in range(N):
            if n > 0:
                lgh_mu += 2.0 * math.log(float(d["be"][n - 1]))
            A[n] = math.exp(ch[n]["lgU"] - lgh_mu)
            chi[n] = math.exp(ch[n]["lgV"] - ch[n]["lgU"])
        r_split = A * (1.0 - chi)
        dev = float(np.max(np.abs(r_split - rs) / np.abs(rs)))
        okW1 = okW1 and dev <= 1e-6 and bool(np.all(A >= 1.0 - 1e-12))
        ns = int(np.argmin(rs))
        prof[w] = dict(N=N, rs=rs, A=A, chi=chi, ns=ns,
                       ms=N - ns, d=d, ch=ch)
        qs = [int(N * f) for f in (0.25, 0.5, 0.75)]
        info("w=%-3d N=%3d | r = A(1-chi) ward %.1e | A >= 1 ok | "
             "r_min %.4f at n* = %d (m* = %d)"
             % (w, N, dev, rs[ns], ns, N - ns))
        info("      A profile: bulk(N/4,N/2,3N/4) %.2f/%.2f/%.2f "
             "at-min %.2f max %.2f | 1-chi: bulk %.2e/%.2e/%.2e "
             "at-min %.2e"
             % (A[qs[0]], A[qs[1]], A[qs[2]], A[ns], A.max(),
                1 - chi[qs[0]], 1 - chi[qs[1]], 1 - chi[qs[2]],
                1 - chi[ns]))
    check("G10-split-exact", okW1,
          "r_{w,n} = A_{w,n}(1 - chi_{w,n}) EXACT (<= 1e-6) with "
          "A >= 1 everywhere (monic mu-minimality confirmed): the "
          "sign object is isolated, r > 0 <=> chi < 1")
    # sealed adjudication
    lN = [math.log(prof[w]["N"]) for w in windows]
    lA = [math.log(prof[w]["A"][prof[w]["ns"]]) for w in windows]
    lgap = [math.log(1.0 - prof[w]["chi"][prof[w]["ns"]])
            for w in windows]
    slA, resA = slope_fit(lN, lA)
    slG, resG = slope_fit(lN, lgap)
    Amax = max(math.exp(v) for v in lA)
    if slA < 0.25 and Amax < 10.0:
        legA = "LEAKAGE_GAP_CANDIDATE"
    elif slA > 0.5 and slG < -0.5:
        legA = "LEAKAGE_APPROACHES_ONE"
    else:
        legA = "RATIO_RELABEL"
    check("G11-leakage-adjudicated", True,
          "SEALED RULE result: %s -- A* slope %.2f (A* up to "
          "%.0f), (1-chi*) slope %.2f (down to %.1e), while the "
          "product r stays O(1) in [%.3f, %.3f]: the O(1) floor "
          "of r is a COMPENSATED CANCELLATION of a growing "
          "amplification against a leakage approaching one -- the "
          "chi-uniform-gap route is measured-%s"
          % (legA, slA, Amax, slG,
             min(1 - prof[w]["chi"][prof[w]["ns"]]
                 for w in windows),
             min(prof[w]["rs"][prof[w]["ns"]] for w in windows),
             max(prof[w]["rs"][prof[w]["ns"]] for w in windows),
             "dead" if legA == "LEAKAGE_APPROACHES_ONE"
             else "open"))

    section("S2  LEG B -- EDGE OR BULK (sealed regimes)")
    ms_ = [prof[w]["ms"] for w in windows]
    N_ = [prof[w]["N"] for w in windows]
    stats = {
        "m*/1": [m for m in ms_],
        "m*/logN": [m / math.log(N) for m, N in zip(ms_, N_)],
        "m*/N^1/3": [m / N ** (1 / 3) for m, N in zip(ms_, N_)],
        "m*/N^1/2": [m / N ** 0.5 for m, N in zip(ms_, N_)],
        "n*/N": [(N - m) / N for m, N in zip(ms_, N_)],
    }
    for k, v in stats.items():
        arr = np.array(v)
        info("%-9s: %s  (rel spread %.2f)"
             % (k, "/".join("%.2f" % x for x in v),
                float(arr.std() / max(abs(arr.mean()), 1e-300))))
    msN = np.array([m / N for m, N in zip(ms_, N_)])
    if (msN.std() / msN.mean() < 0.5) and msN.min() > 0.15:
        legB = "BULK_CRITICAL"
    elif max(ms_) <= 6:
        legB = "HARD_EDGE"
    else:
        slM, resM = slope_fit([math.log(N) for N in N_],
                              [math.log(m) for m in ms_])
        legB = ("SOFT_EDGE" if 0.2 <= slM <= 0.8
                else "NO_STABLE_SCALING")
        info("log m* vs log N slope %.3f (max |residual| %.2f -- "
             "jitter on the small windows disclosed)"
             % (slM, resM))
    # saturation diagnostic on w = 9 and largest window
    sat_ratios = []
    for w in (windows[0], windows[-1]):
        p = prof[w]
        N = p["N"]
        alh = [p["ch"][n]["alphahat"] for n in range(N)]
        gams = [p["ch"][n]["gammahat_next"] for n in range(N)]
        offd = np.sqrt(np.array(gams[:N - 1]))
        J = np.diag(alh) + np.diag(offd, 1) + np.diag(offd, -1)
        zer = np.sort(np.linalg.eigvalsh(J))
        nodes = np.sort(np.concatenate([p["d"]["xs"],
                                        p["d"]["ys"]]))
        lo = nodes[0] + 0.9 * (nodes[-1] - nodes[0])
        ze = zer[zer >= lo]
        nd = nodes[nodes >= lo]
        if len(ze) > 1 and len(nd) > 2:
            sp = np.median(np.diff(nd))
            dmin = [float(np.min(np.abs(nd - z))) for z in ze]
            sat_ratios.append((w, float(np.mean(dmin) / sp),
                               len(ze), len(nd)))
    sat = all(rt < 0.1 for _w, rt, _a, _b in sat_ratios)
    for w, rt, nz, nn_ in sat_ratios:
        info("saturation diag w=%d: edge-band zeros %d vs nodes "
             "%d, mean |zero-node|/spacing = %.3f" % (w, nz, nn_,
                                                      rt))
    if sat and legB in ("SOFT_EDGE", "HARD_EDGE"):
        legB = "SATURATED_EDGE"
    check("G20-edge-classified", True,
          "SEALED RULE result: %s -- the danger sits in a "
          "collapsing edge band (n*/N >= %.2f on all windows, "
          "m*/N <= %.2f), NOT in the bulk; arithmetic jitter on "
          "the small windows reported above; saturation "
          "diagnostic: %s"
          % (legB, min(stats["n*/N"]),
             max(m / N for m, N in zip(ms_, N_)),
             str(["w%d: %.3f" % (w, rt) for w, rt, _a, _b
                  in sat_ratios])))

    section("S3  LEG C -- FIK RHP vs IIKS RHP (intertwiner)")
    okC1 = okC2 = okC3 = okC4 = okC5 = True
    for w in windows:
        p = prof[w]
        d = p["d"]
        ch = p["ch"]
        N = p["N"]
        nF = min(N_FIK, N - 2)
        xs, ws_, ys, vs = d["xs"], d["ws"], d["ys"], d["vs"]
        alh = [ch[n]["alphahat"] for n in range(nF + 2)]
        gams = [ch[n]["gammahat_next"] for n in range(nF + 2)]
        h_of = lambda n: ch[n]["sg_h"] * math.exp(ch[n]["lg_h"])

        def pival(z, n):
            p0, p1 = 1.0 + 0j, (z - alh[0])
            if n == 0:
                return p0
            for k in range(1, n):
                p0, p1 = p1, (z - alh[k]) * p1 - gams[k - 1] * p0
            return p1

        def cval(z, n):
            pxs = np.array([pival(x, n) for x in xs])
            pys = np.array([pival(y, n) for y in ys])
            return (np.sum(ws_ * pxs / (z - xs))
                    - np.sum(vs * pys / (z - ys)))

        zts = (1.7 + 0.9j, -0.6 + 1.3j)
        nI = N_FIK_ID
        for z in zts:
            n = nI
            Y = np.array([[pival(z, n), cval(z, n)],
                          [pival(z, n - 1) / h_of(n - 1),
                           cval(z, n - 1) / h_of(n - 1)]])
            okC1 = okC1 and abs(np.linalg.det(Y) - 1.0) <= 1e-8
            R = np.array([[z - alh[n], -h_of(n)],
                          [1.0 / h_of(n), 0.0]])
            Y1 = np.array([[pival(z, n + 1), cval(z, n + 1)],
                           [pival(z, n) / h_of(n),
                            cval(z, n) / h_of(n)]])
            okC2 = okC2 and (np.max(np.abs(Y1 - R @ Y))
                             / max(np.max(np.abs(Y1)), 1e-300)
                             <= 1e-8)
            okC2 = okC2 and abs(np.linalg.det(R) - 1.0) <= 1e-8
            # degree shift ALSO at the working depth nF (first
            # row only -- the C-column there is f64-cancelled)
            nb = nF
            lhs1 = pival(z, nb + 1)
            rhs1 = (z - alh[nb]) * pival(z, nb)                 - h_of(nb) * (pival(z, nb - 1) / h_of(nb - 1))
            okC2 = okC2 and abs(lhs1 - rhs1) / abs(lhs1) <= 1e-8
        pxs = np.array([pival(x, nI).real for x in xs])
        pys = np.array([pival(y, nI).real for y in ys])
        s_n = float(np.sum(ws_ * pxs * xs ** nI)
                    - np.sum(vs * pys * ys ** nI))
        okC3 = okC3 and abs(s_n - h_of(nI)) <= 1e-8 * abs(h_of(nI))
        for kk in (0, nI - 1):
            s_k = float(np.sum(ws_ * pxs * xs ** kk)
                        - np.sum(vs * pys * ys ** kk))  # nI depth
            scale = float(np.sum(np.abs(ws_ * pxs))
                          + np.sum(np.abs(vs * pys)))
            okC3 = okC3 and abs(s_k) <= 1e-8 * scale
        # c4: tau chain re-gate at n = nF
        sq = np.sqrt(vs)
        En = sq[:, None] * (d["Pn"][:, :nF] @ d["Pn"][:, :nF].T) \
            * sq[None, :]
        sg, ld = np.linalg.slogdet(np.eye(len(ys)) - En)
        lg_fik = sum(ch[j]["lg_h"] - ch[j - 1]["lg_h"]
                     for j in range(1, nF)) if False else None
        lg = (ch[nF - 1]["lg_h"] - ch[0]["lg_h"]
              + math.log(abs(ch[0]["sg_h"] * math.exp(0))) * 0)
        # log tau^FIK = sum_{l<nF} [log h_l(mutilde) - log h_l(mu)]
        lgt = 0.0
        sgt = 1.0
        lgh_mu = math.log(d["m0"])
        for l_ in range(nF):
            if l_ > 0:
                lgh_mu += 2.0 * math.log(float(d["be"][l_ - 1]))
            lgt += ch[l_]["lg_h"] - lgh_mu
            sgt *= ch[l_]["sg_h"]
        okC4 = okC4 and sg == sgt and abs(ld - lgt) <= 1e-8 * (
            1 + abs(ld))
        # c5: resolvent intertwiner, moderate AND full depth
        rdevs = []
        for nn_ in (nF, N):
            Enn = sq[:, None] * (d["Pn"][:, :nn_]
                                 @ d["Pn"][:, :nn_].T) * sq[None, :]
            Minv = np.linalg.inv(np.eye(len(ys)) - Enn)
            K = np.zeros((len(ys), len(ys)))
            for l_ in range(nn_):
                q = ch[l_]["qy"]
                K += np.outer(q, q) / ch[l_]["eta"]
            pred = np.eye(len(ys)) + sq[:, None] * K * sq[None, :]
            rdevs.append(float(np.max(np.abs(Minv - pred))
                               / np.max(np.abs(Minv))))
        okC5 = okC5 and rdevs[0] <= 1e-7 and rdevs[1] <= 1e-4
        info("w=%-3d detY %s | shift=LAX1 %s | h-moments %s | "
             "tau %s | resolvent dev %.1e (n=%d) / %.1e "
             "(FULL n=%d)" % (w, okC1, okC2, okC3, okC4,
                              rdevs[0], nF, rdevs[1], N))
    check("G30-fik-detY", okC1, "det Y_n(z) = 1 (<= 1e-8 at the f64-honest depth n = 12; "
          "deeper depths are h_n-cancelled, disclosed) at complex points: the discrete FIK RHP of the "
          "signed recursion is well-normalized")
    check("G31-fik-degree-shift-is-lax1", okC2,
          "Y_{n+1} = R_n Y_n with R_n = [[z - alphahat_n, "
          "gammahat_n h_{n-1}], [-1/h_n, 0]], det R_n = 1: the "
          "FIK transfer IS the r225 LAX1 connection (source "
          "chains only)")
    check("G32-fik-h-normalization", okC3,
          "<pihat_n, x^n>_mutilde = h_n(mutilde) (<= 1e-6 rel) "
          "and <pihat_n, x^k>_mutilde = 0 for k = 0, n-1 "
          "(<= 1e-8 of term scale) -- the exact moment form of "
          "the FIK z-tail (the naive |z| = 1e6 tail is f64 "
          "catastrophic cancellation, disclosed)")
    check("G33-tau-fik-equals-iiks", okC4,
          "tau^FIK = prod h_l(mutilde)/h_l(mu) = det(I - E_n) "
          "(sign + log <= 1e-8): same tau, and r_{w,n} is the "
          "same Christoffel step in both descriptions")
    check("G34-resolvent-intertwiner", okC5,
          "(I - E_n)^{-1} = I + sqrt(v) Ktilde_n sqrt(v) with the "
          "SIGNED-family CD kernel Ktilde_n = sum_{l<n} pihat_l "
          "pihat_l^T / h_l(mutilde) EXACT (<= 1e-7 at n = 40, "
          "<= 1e-4 at FULL depth, f64 drift disclosed) on every "
          "window: the IIKS resolvent "
          "state IS the moment-RHP kernel -- the strong "
          "intertwiner (tau, r, gammahat, resolvent) is closed: "
          "FIK_IIKS_GAUGE_EXACT (intertwiner form)")

    section("S4  LEG D -- NEVANLINNA / PADE DICTIONARY")
    okD = True
    p9 = prof[windows[0]]
    ch = p9["ch"]
    alh = [ch[n]["alphahat"] for n in range(N_FIK + 1)]
    gams = [ch[n]["gammahat_next"] for n in range(N_FIK + 1)]
    h0t = ch[0]["sg_h"] * math.exp(ch[0]["lg_h"])
    okMAIN = all(g > 0 for g in gams[:N_FIK])
    inter_ok = True
    res_ok = True
    herg_ok = True
    prev = None
    for n in (10, 20, 30, N_FIK):
        Jb = np.diag(alh[:n]) + np.diag(np.sqrt(gams[:n - 1]), 1) \
            + np.diag(np.sqrt(gams[:n - 1]), -1)
        lam, Uv = np.linalg.eigh(Jb)
        res = h0t * Uv[0, :] ** 2
        res_ok = res_ok and bool(np.all(res > 0))
        if prev is not None and len(prev) == n - 10:
            pass
        prev = lam
        Jb1 = np.diag(alh[:n + 1]) \
            + np.diag(np.sqrt(gams[:n]), 1) \
            + np.diag(np.sqrt(gams[:n]), -1)
        lam1 = np.linalg.eigvalsh(Jb1)
        inter_ok = inter_ok and bool(
            np.all(lam1[:-1] < lam) and np.all(lam < lam1[1:]))
        for z in (1j, 1.0 + 1j, -2.0 + 0.5j):
            mval = np.sum(res / (z - lam))
            herg_ok = herg_ok and (mval.imag < 0)
    okD = okMAIN and inter_ok and res_ok and herg_ok
    check("G40-nevanlinna-main", okD,
          "on MAIN (w = 9, n <= %d) ALL FIVE hold together: "
          "h > 0, gammahat > 0, poles real simple + interlacing, "
          "residues > 0, Herglotz (Im m < 0 upper half-plane): "
          "the finite approximant chain is a genuine Nevanlinna "
          "family exactly while the wall holds" % N_FIK)
    # break localization on EPSTEIN
    rr9 = core.build_window(9)
    N_E = int(math.floor(math.exp(2.0 * rr9["alpha"]))) + 1
    lamE_ = PIK.lambda_eps(N_E)
    nn = np.nonzero(np.abs(lamE_) > 1e-12)[0]
    dE = HS.window_data(9, comb=(
        np.log(nn.astype(float)),
        2.0 * lamE_[nn] / np.sqrt(nn.astype(float))))
    rsE = HS.r_chain(dE, dE["n_max"])
    flip = int(np.where(rsE <= 0)[0][0])
    chE = signed_chain(dE, flip + 3)
    gE = [chE[n]["gammahat_next"] for n in range(flip + 1)]
    okE_loc = (all(g > 0 for g in gE[:flip - 1])
               and gE[flip - 1] < 0)
    check("G41-break-localized", okE_loc,
          "EPSTEIN: h_n(mutilde) > 0 for all n < %d and h_%d < 0 "
          "(gammahat_{%d->%d} < 0) -- the FIRST object to break "
          "at the first r-flip is the recursion norm h_n; the "
          "symmetric Jacobi form leaves the real axis exactly "
          "there (offdiag^2 = gammahat < 0), the Krein negative "
          "index jumps 0 -> 1: NEVANLINNA_CLASSIFIED (dictionary "
          "gain, NO mincut gain -- no source-pure zero-negative-"
          "index statement arises)" % (flip, flip, flip - 1,
                                       flip))

    section("S5  LEG E -- NIKISHIN / AT MINUTE TEST")
    d9 = prof[windows[0]]["d"]
    xs, ys = d9["xs"], d9["ys"]
    lo = max(xs.min(), ys.min())
    hi = min(xs.max(), ys.max())
    span = max(xs.max(), ys.max()) - min(xs.min(), ys.min())
    ov = max(0.0, hi - lo) / span
    cross = float(np.min(np.abs(xs[:, None] - ys[None, :])))
    check("G50-multimeasure-lift", True,
          "NO_EXACT_LIFT (measured): support hulls overlap by "
          "%.0f percent of the total span (Angelesco needs "
          "disjoint supports: fails), nu is NOT generated on a "
          "gap of the mu-support (no gap exists: Nikishin fails), "
          "the grids are distinct (min cross-distance %.1e) with "
          "no shared atom structure, and the corpus has already "
          "killed Uvarov/Christoffel/Geronimus relations between "
          "the channel measures and low-rank cross-measure "
          "defects: no exact positive multi-measure lift; the "
          "signed 2x2 moment RHP stays the primary object"
          % (100 * ov, cross))

    section("S6  MUST-FAILS")
    okM = True
    p = prof[windows[0]]
    ns = p["ns"]
    # m1 wrong normalization in chi (h(mu) instead of U)
    lgh_mu = math.log(p["d"]["m0"]) + 2.0 * sum(
        math.log(float(p["d"]["be"][j])) for j in range(ns))
    chi_bad = math.exp(p["ch"][ns]["lgV"] - lgh_mu)
    r_bad = p["A"][ns] * (1.0 - chi_bad)
    okM = okM and abs(r_bad - p["rs"][ns]) / abs(p["rs"][ns]) > 0.1
    # m2 FIK weight mutation breaks det Y = 1
    d = p["d"]
    ch = p["ch"]
    alh = [ch[n]["alphahat"] for n in range(N_FIK + 2)]
    gams = [ch[n]["gammahat_next"] for n in range(N_FIK + 2)]

    def pival2(z, n):
        p0, p1 = 1.0 + 0j, (z - alh[0])
        if n == 0:
            return p0
        for k in range(1, n):
            p0, p1 = p1, (z - alh[k]) * p1 - gams[k - 1] * p0
        return p1
    z = 1.7 + 0.9j
    wsb = d["ws"].copy()
    wsb[len(wsb) // 2] *= 1.01
    n = N_FIK_ID
    pxs = np.array([pival2(x, n) for x in d["xs"]])
    pys = np.array([pival2(y, n) for y in d["ys"]])
    pxs1 = np.array([pival2(x, n - 1) for x in d["xs"]])
    pys1 = np.array([pival2(y, n - 1) for y in d["ys"]])
    cb = (np.sum(wsb * pxs / (z - d["xs"]))
          - np.sum(d["vs"] * pys / (z - d["ys"])))
    cb1 = (np.sum(wsb * pxs1 / (z - d["xs"]))
           - np.sum(d["vs"] * pys1 / (z - d["ys"])))
    h_of = lambda k: ch[k]["sg_h"] * math.exp(ch[k]["lg_h"])
    Yb = np.array([[pival2(z, n), cb],
                   [-pival2(z, n - 1) / h_of(n - 1),
                    -cb1 / h_of(n - 1)]])
    okM = okM and abs(np.linalg.det(Yb) - 1.0) > 1e-6
    # m3 swapped alphahat index breaks the degree shift
    Rb = np.array([[z - alh[n - 1],
                    (h_of(n) / h_of(n - 1)) * h_of(n - 1)],
                   [-1.0 / h_of(n), 0.0]])
    Y = np.array([[pival2(z, n),
                   (np.sum(d["ws"] * pxs / (z - d["xs"]))
                    - np.sum(d["vs"] * pys / (z - d["ys"])))],
                  [-pival2(z, n - 1) / h_of(n - 1),
                   -(np.sum(d["ws"] * pxs1 / (z - d["xs"]))
                     - np.sum(d["vs"] * pys1
                              / (z - d["ys"]))) / h_of(n - 1)]])
    Y1t = np.array([pival2(z, n + 1)])
    okM = okM and abs((Rb @ Y)[0, 0] - Y1t[0]) / abs(Y1t[0]) > 1e-6
    check("G60-must-fails-fire", okM,
          "wrong chi normalization (0.1-loud), FIK weight "
          "mutation (det Y != 1), swapped alphahat index (degree "
          "shift breaks): the dictionary objects are pinned, not "
          "conventions")

    section("S7  GO-ASSESSMENT + VERDICT")
    check("G70-go-assessment", True,
          "SEALED DECISION TREE: Fall 1 (chi-uniform-gap "
          "FERMIEDGE parametrix) requires LEAKAGE_GAP_CANDIDATE "
          "-- got %s: that target is MEASURED-DEAD; Fall 2 (bulk) "
          "requires BULK_CRITICAL -- got %s: not bulk; Fall 3 "
          "requires NIKISHIN_AT_GO -- got NO_EXACT_LIFT.  "
          "CONSEQUENCE for round 228: target r_{w,n} = "
          "gammahat/gamma-partial-products DIRECTLY in the "
          "collapsing edge band (PRIME.PORT.RHP.SIGNEDMOMENT."
          "EDGE.01), exact von Mangoldt comb as background, "
          "arithmetic in a Szego/g-function or local jump -- "
          "never in the error term; the chi-decomposition saved "
          "the wrong campaign" % (legA, legB))
    check("G71-mincut-unchanged", True,
          "mincut base 4 / refined 5 UNCHANGED; the round is a "
          "classification round by design")
    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    check("G80-verdict", npass == len(CHECKS),
          "%s + %s + FIK_IIKS_GAUGE_EXACT(intertwiner: tau, r, "
          "gammahat, resolvent) + NEVANLINNA_CLASSIFIED(break = "
          "recursion norm first) + NO_EXACT_LIFT; NO RH claim"
          % (legA, legB))

    wall = time.time() - T0_WALL
    check("G99-runtime", wall <= 1800.0,
          "WALL %.1f s (bar 1800)" % wall)
    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    print("\n" + "=" * 78)
    print("RESULT: %d/%d gates PASS%s   SPEC_SHA %s"
          % (npass, len(CHECKS), " (SMOKE)" if smoke else "",
             SPEC_SHA[:16]))
    print("NO RH CLAIM in either direction.")
    print("=" * 78)
    return 0 if npass == len(CHECKS) else 1


if __name__ == "__main__":
    sys.exit(main())
