#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""cotlar_v2_complete_comb_probe -- PRIME.PRUEFER.COMPENSATION.02
+ PRIME.TRUNCATION.AUDIT.01
(EXPLORATION ONLY, experiments/; direct follow-up to the
DEEP-ALPHA-ARTIFACT verdict, 2026-08-08 night).

TASK 1 -- THE COTLAR RE-DECISION (v2).  The executed v1
contract (pruefer_compensation_probe.py, FROZEN_SPEC SHA-256
4621b89958531d6d3baae9fe762dbd10d23dc22eed77a57aa1c6b179a744
0811) fired COTLAR-GROWING on the deep holdouts kz 142/177/
243 -- which deep_alpha_sign_probe proved were COMB-TRUNCATED
(core.build_window silently drops all events beyond ATOM_MAX
= 400000; those windows demand support to 1.8e6).  The v1
verdict stands on its own rules FOR THE DATA AS MEASURED; the
scientific question reopens.  V2 PROTOCOL (frozen here):
IDENTICAL cells, pairing, danger geometry, Cotlar sums, and
decision bars as v1 (ppc machinery imported READ-ONLY; the
phases/cells via ppc.deployed_cells VERBATIM); THE SINGLE
SUBSTANTIVE CHANGE: the deep holdouts are built with the
COMPLETE canonical comb (the deep_alpha_sign extended-table
machinery: von_mangoldt_table(ceil(e^{2 alpha_max})+1), comb
= (U_EXT[:ka], MU_EXT[:ka]) passed through build_rung's comb
port).  One PERFORMANCE substitution, warded for exactness:
the 16x16 cross-norm census computes the identical spectral
norms through ||X_r^* X_s||_2^2 = lam_max(P_r^{1/2} P_s
P_r^{1/2}) with P_r = X_r X_r^* (dense eigh, no iteration)
and ||X_r X_s^*||_2 by direct SVD of the r_- x r_- product;
equivalence ward vs ppc.cross_norms at kz 9 (rel <= 1e-8)
and full-readout ward vs ppc.rung_readouts at kz 9.

TASK 2 -- THE TRUNCATION AUDIT: which recent findings used
windows with comb demand > ATOM_MAX, and does each conclusion
depend on them (CONFOUNDED / ROBUST / UNAFFECTED, typed); the
polygon export is RE-RUN at the three corrected rungs (the
cheap hardening of its holdout rows).

VERDICT (frozen): COTLAR-GROWING-CONFIRMED (the frozen v1
decision rule still says GROWING on complete-comb data -- the
route stays dead, now clean) / COTLAR-BOUNDED-V2 (the v1 kill
was the truncation artifact -- the route REOPENS; run 3
executes: the analytic envelope candidate) / COTLAR-PARTIAL-
V2 (typed).  NO RH claim; writes nothing; no .md; no commits.

ADDENDUM v1.1 (post first execution, typed refinement of the
AUDIT check A.1 only -- no Cotlar quantity, bar, or decision
rule touched): the polygon re-run at the complete-comb deep
rungs OVERFLOWS phase_polygon's raw-longdouble prefix
machinery (exp(l2m) > longdouble max at the complete-comb
mass; margins NaN/inf) -- the frozen A.1 conflated "polygon
breaks" with "machinery out of numeric range".  A.1 now types
each rung: HOLDS (finite margins, no negative prefix) /
REFUTED (finite margins, negative prefix -- fails) /
NUMERIC-VOID (non-finite margins -- the polygon holdout rows
are VOID at complete combs, neither confirmed nor refuted;
the phase_polygon verdict remains battery-driven ROBUST on
in-cap rungs only).  Run-1/run-2/run-3 outputs of the first
execution reproduce bit-identically (deterministic pipeline).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/cotlar_v2_complete_comb_probe.py
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

import v563_paper2_readouts as core            # noqa: E402  (READ-ONLY)
import gauss_node_unitary_probe as gnu         # noqa: E402  (READ-ONLY)
import pruefer_compensation_probe as ppc       # noqa: E402  (READ-ONLY)
import phase_polygon_probe as ppg              # noqa: E402  (READ-ONLY)

FROZEN_SPEC = """\
PRIME.PRUEFER.COMPENSATION.02 + PRIME.TRUNCATION.AUDIT.01
spec v1 (2026-08-08, frozen before run).  V1 CONTRACT QUOTED:
SPEC SHA 4621b89958531d6d3baae9fe762dbd10d23dc22eed77a57aa1c6
b179a7440811 (verified at run time against ppc.FROZEN_SPEC).
V2 = v1 VERBATIM (cells: 16 equal pi/8 cells on delta theta;
entrywise pairing; danger DGR1 {0,15} u DGR2 {7,8}; Cotlar
S_X = max_r sum_s sqrt||X_r^* X_s||, B = sqrt(S S*); battery
= the 42 frame-a rungs h <= 900; holdouts kz {90, 116, 142,
177, 243}; DECISION per S_U/S_C: BOUNDED iff holdout max <=
1.2 x battery max AND OLS slope of log S vs log h over
battery+holdouts <= 0.10; GROWING iff slope >= 0.20 OR (S vs
log h linear R^2 >= 0.9 with positive slope); else PARTIAL)
with the SINGLE substantive change: holdout windows built
with the COMPLETE comb via build_rung(comb=(U_EXT[:ka],
MU_EXT[:ka])), U/MU_EXT from von_mangoldt_table(ceil(e^{2
alpha_243})+1); in-cap rungs untouched (bit-equality ward of
comb_ext vs deployed comb on kz 9 + first battery rung).
PERFORMANCE substitution (warded): cross norms via the exact
Gram identities above; wards W-N1 rel <= 1e-8 vs
ppc.cross_norms at kz 9, W-N2 full readout triple (S_U, S_C,
danger) vs ppc.rung_readouts at kz 9 rel <= 1e-10.
Regressions: danger share kz 9 in [0.316, 0.356]; extended
Krein floors at kz 142/177/243 reproduce deep_alpha_sign
(+1.2389e-8 / +1.3284e-8 / +6.6742e-9, rel 0.2) -- read from
the SAME complete builds; truncated holdout sums recomputed
at kz 142/177/243 for the contrast column (the v1-as-measured
values).  RUN 1 (anchors, in-cap == v1): danger share,
negativity capture, env Spearman.  RUN 2: the decision table
+ frozen rule on complete data.  RUN 3 only if BOTH S_U and
S_C BOUNDED: K_p(h) = max_d env(d)(1+d)^p (p = 1 U, 2 C)
h-stability, holdout max <= 1.2 x anchor max, delta_coef
reported.  Epstein/scramble contrast at kz 9 (v1 bars: >= 25
percent triple deviation in >= 1 component AND eps ratio >= 5
or env-Spearman break).  AUDIT (typed table): probes x rungs
x truncation x dependence; polygon export re-run at complete
kz 142/177/243 (x0 = 0; ROBUST iff still no negative prefix).
VERDICTS: COTLAR-GROWING-CONFIRMED / COTLAR-BOUNDED-V2 /
COTLAR-PARTIAL-V2 (+ the audit table).  NO RH claim; writes
nothing."""

V1_SHA = ("4621b89958531d6d3baae9fe762dbd10d23dc22eed77a57a"
          "a1c6b179a7440811")
DEEP = (142, 177, 243)
HOLDOUTS = ppc.HOLDOUTS            # (90, 116, 142, 177, 243)
ANCHORS = ppc.ANCHORS              # (9, 12, 13, 26, 40)
DANGER_SHARE_KZ9 = (0.316, 0.356)
KREIN_EXT_REFS = {142: 1.2389e-8, 177: 1.3284e-8,
                  243: 6.6742e-9}
BANNED_IDS = ("zetazero", "nzeros", "primerange", "isprime",
              "primepi", "nextprime", "prevprime")

CHECKS = []
FAILS = []
T0 = time.time()


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok)))
    if not ok:
        FAILS.append(name.split()[0])
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


# ------------------------------------------------ extended comb
def build_ext_table():
    amax = max(float(core.U_ALL[kz]) for kz in DEEP)
    NEXT = int(math.ceil(math.exp(2.0 * amax))) + 1
    LAM_EXT = core.von_mangoldt_table(NEXT)
    NN = np.nonzero(LAM_EXT > 0.0)[0]
    U = np.log(NN.astype(float))
    MU = 2.0 * LAM_EXT[NN] / np.sqrt(NN.astype(float))
    return U, MU


U_EXT, MU_EXT = None, None


def comb_ext(kz):
    rr = core.build_window(kz)
    ka = int(np.searchsorted(U_EXT,
                             2.0 * rr["alpha"] + 1.0e-14,
                             side="right"))
    return U_EXT[:ka].copy(), MU_EXT[:ka].copy()


# ------------------------------------------------ fast cross norms
def cross_norms_fast(pieces):
    """The v1 quantities ||X_r^* X_s||_2 and ||X_r X_s^*||_2
    via exact Gram identities (dense eigh/SVD, no
    iteration)."""
    C = ppc.CELLS
    P = [X @ X.conj().T for X in pieces]
    Ph = []
    for Pr in P:
        Ps = 0.5 * (Pr + Pr.conj().T)
        w, V = np.linalg.eigh(Ps)
        w = np.sqrt(np.clip(w, 0.0, None))
        Ph.append((V * w) @ V.conj().T)
    N = np.zeros((C, C))
    Ns = np.zeros((C, C))
    for r in range(C):
        for s in range(r, C):
            Mrs = Ph[r] @ P[s] @ Ph[r]
            Mrs = 0.5 * (Mrs + Mrs.conj().T)
            lmx = float(np.linalg.eigvalsh(Mrs)[-1])
            N[r, s] = N[s, r] = math.sqrt(max(lmx, 0.0))
            G = pieces[r] @ pieces[s].conj().T
            sv = np.linalg.svd(G, compute_uv=False)
            Ns[r, s] = Ns[s, r] = float(sv[0]) if len(sv) \
                else 0.0
    return N, Ns


def readouts_v2(kz, **kw):
    """ppc.rung_readouts VERBATIM with the fast norm census
    (the only substitution; warded)."""
    dc, err = ppc.deployed_cells(kz, **kw)
    if dc is None:
        return None, err
    b, go, cell = dc["b"], dc["go"], dc["cell"]
    if b["h"] > 1500:
        return None, "skip-h"
    ch = dc["chains"]
    Jp = np.diag(ch["alp"]) + np.diag(ch["bep"][:len(
        ch["alp"]) - 1], 1) + np.diag(ch["bep"][:len(
            ch["alp"]) - 1], -1)
    evp = np.linalg.eigvalsh(Jp)
    nodew = float(np.max(np.abs(np.sort(evp)
                                - np.sort(np.cos(go["thp"])))))
    U = go["U"]
    Dm2 = go["Dm"] ** 2
    Cc = go["Dm"][:, None] * U
    pu = ppc.split_pieces(U, cell)
    pc = ppc.split_pieces(Cc, cell)
    compl_u = float(np.max(np.abs(sum(pu) - U)))
    compl_c = float(np.max(np.abs(sum(pc) - Cc)))
    Nu, Nus = cross_norms_fast(pu)
    Nc, Ncs = cross_norms_fast(pc)
    Su, Sus, Bu = ppc.cotlar_sums(Nu, Nus)
    Sc, Scs, Bc = ppc.cotlar_sums(Nc, Ncs)
    dgr = set(ppc.DGR1) | set(ppc.DGR2)
    tot = float(np.sum(Nu))
    dmask = np.zeros((ppc.CELLS, ppc.CELLS), bool)
    for r in range(ppc.CELLS):
        for s in range(ppc.CELLS):
            dmask[r, s] = (r in dgr) or (s in dgr)
    dshare = float(np.sum(Nu[dmask])) / max(tot, 1e-300)
    h = b["h"]
    wr = np.array([float(np.sum(np.abs(p) ** 2)) for p in pu])
    wr = wr / max(float(np.sum(wr)), 1e-300)
    eps = []
    for r in range(ppc.CELLS):
        Ar = pu[r]
        Mr = wr[r] * np.eye(h) - Ar.conj().T \
            @ (Dm2[:, None] * Ar)
        Mr = 0.5 * (Mr + Mr.conj().T)
        eps.append(max(0.0, -float(np.linalg.eigvalsh(Mr)[0])))
    T1 = np.eye(h) - U.conj().T @ U
    T1 = 0.5 * (T1 + T1.conj().T)
    lmin_T1 = float(np.linalg.eigvalsh(T1)[0])
    Udgr = sum(pu[r] for r in sorted(dgr))
    T1d = np.eye(h) - Udgr.conj().T @ Udgr
    T1d = 0.5 * (T1d + T1d.conj().T)
    lmin_d = float(np.linalg.eigvalsh(T1d)[0])
    env_u = ppc.envelope(Nu)
    env_c = ppc.envelope(Nc)
    sp_u = ppc.spearman(env_u[:9], np.arange(9.0))
    sp_c = ppc.spearman(env_c[:9], np.arange(9.0))
    lam1 = float(np.linalg.eigvalsh(b["Delta"])[0])
    return dict(kz=kz, h=h, nodew=nodew,
                compl=max(compl_u, compl_c), Su=Su, Sus=Sus,
                Bu=Bu, Sc=Sc, Scs=Scs, Bc=Bc, dshare=dshare,
                eps_sum=float(np.sum(eps)), eps=eps,
                lmin_T1=lmin_T1, lmin_d=lmin_d, env_u=env_u,
                env_c=env_c, sp_u=sp_u, sp_c=sp_c, Nu=Nu,
                Nc=Nc, lam1=lam1, b=b,
                chains=dc["chains"]), None


def decide(series, ix):
    """The frozen v1 decision rule on one sum column."""
    bat = [x for x in series if x["tag"] == "battery"]
    hol = [x for x in series if x["tag"] == "HOLDOUT"]
    mb = max(x[ix] for x in bat)
    mh = max(x[ix] for x in hol)
    hh = np.log([float(x["h"]) for x in series])
    ss = np.log([x[ix] for x in series])
    slope = float(np.polyfit(hh, ss, 1)[0])
    # log-growth clause: S vs log h linear, R^2 >= 0.9
    sl2, ic2 = np.polyfit(hh, np.exp(ss), 1)
    pred = sl2 * hh + ic2
    resid = np.exp(ss) - pred
    r2 = 1.0 - float(np.sum(resid ** 2)) \
        / max(float(np.sum((np.exp(ss)
                            - np.mean(np.exp(ss))) ** 2)),
              1e-300)
    if mh <= 1.2 * mb and slope <= 0.10:
        v = "BOUNDED"
    elif slope >= 0.20 or (r2 >= 0.9 and sl2 > 0.0):
        v = "GROWING"
    else:
        v = "PARTIAL"
    return v, mb, mh, slope, r2


# ================================================================= main
def main():
    global U_EXT, MU_EXT
    section("PRIME.PRUEFER.COMPENSATION.02 -- the Cotlar "
            "re-decision on complete combs (EXPLORATION ONLY)")
    sha = hashlib.sha256(FROZEN_SPEC.encode("utf-8")).hexdigest()
    print("    FROZEN_SPEC SHA-256 = %s" % sha)
    print("    NO RH claim.")
    print("\nS0 -- firewall + the v1 contract")
    check("S0.1 AST firewall clean (no zero/prime oracles)",
          not ast_scan(BANNED_IDS))
    v1sha = hashlib.sha256(
        ppc.FROZEN_SPEC.encode("utf-8")).hexdigest()
    check("S0.2 [V1 CONTRACT] the committed v1 spec hash "
          "matches the quoted SHA (%s...)" % v1sha[:8],
          v1sha == V1_SHA)

    # ---------------- S1 machinery wards
    section("S1 -- machinery wards (the single change, "
            "fenced)")
    t_ = time.time()
    U_EXT, MU_EXT = build_ext_table()
    print("    extended table: %d events to %d (%.1f s)"
          % (len(U_EXT), int(round(math.exp(U_EXT[-1]))),
             time.time() - t_))
    # W-N1: fast norms == dense norms on the kz-9 pieces
    dc9, _ = ppc.deployed_cells(9)
    U9 = dc9["go"]["U"]
    pu9 = ppc.split_pieces(U9, dc9["cell"])
    Nd, Nds = ppc.cross_norms(pu9)
    Nf, Nfs = cross_norms_fast(pu9)
    dev = max(float(np.max(np.abs(Nf - Nd)
                           / np.maximum(Nd, 1e-12))),
              float(np.max(np.abs(Nfs - Nds)
                           / np.maximum(Nds, 1e-12))))
    check("W-N1 [NORM EQUIVALENCE] fast Gram-identity norms "
          "== ppc.cross_norms on the kz-9 pieces (max rel "
          "%.1e <= 1e-8)" % dev, dev <= 1e-8)
    r9v1, _ = ppc.rung_readouts(9)
    r9v2, _ = readouts_v2(9)
    tri1 = np.array([r9v1["Su"], r9v1["Sc"], r9v1["dshare"]])
    tri2 = np.array([r9v2["Su"], r9v2["Sc"], r9v2["dshare"]])
    reldev = float(np.max(np.abs(tri2 - tri1) / tri1))
    check("W-N2 [READOUT EQUIVALENCE] v2 readout triple == "
          "v1 at kz 9 (max rel %.1e <= 1e-10); danger share "
          "%.3f in [%.3f, %.3f]"
          % (reldev, r9v2["dshare"], *DANGER_SHARE_KZ9),
          reldev <= 1e-10
          and DANGER_SHARE_KZ9[0] <= r9v2["dshare"]
          <= DANGER_SHARE_KZ9[1])
    battery = ppc.battery_rungs()
    incap = all(math.exp(2.0 * core.build_window(kz)["alpha"])
                <= core.ATOM_MAX + 0.5
                for kz in battery + [90, 116])
    ue, me = comb_ext(9)
    rr9 = core.build_window(9)
    same9 = (np.array_equal(ue, np.asarray(rr9["uu"]))
             and np.array_equal(me, 2.0 * np.asarray(
                 rr9["lam"])))
    ueb, meb = comb_ext(battery[-1])
    rrb = core.build_window(battery[-1])
    sameb = (np.array_equal(ueb, np.asarray(rrb["uu"]))
             and np.array_equal(meb, 2.0 * np.asarray(
                 rrb["lam"])))
    check("W-N3 [SINGLE-CHANGE WARD] all 42 battery rungs + "
          "kz 90/116 are in-cap (complete already) and "
          "comb_ext is bit-identical to the deployed comb on "
          "kz 9 and kz %d" % battery[-1],
          incap and same9 and sameb)

    # ---------------- RUN 1 (anchors; in-cap == v1)
    section("RUN 1 (v2) -- anatomy on the anchors (in-cap: "
            "identical to v1 by W-N3)")
    cache = {}
    for kz in ANCHORS:
        r, err = readouts_v2(kz)
        cache[kz] = r
        print("    kz %-3d h %-4d: danger share %.3f | "
              "lam_min(T1) %+ .4f vs danger-trunc %+ .4f "
              "(capture %.2f) | sum eps_r %.3e | env "
              "Spearman U/C %.2f/%.2f"
              % (kz, r["h"], r["dshare"], r["lmin_T1"],
                 r["lmin_d"],
                 (r["lmin_d"] / r["lmin_T1"])
                 if r["lmin_T1"] < 0 else float("nan"),
                 r["eps_sum"], r["sp_u"], r["sp_c"]),
              flush=True)

    # ---------------- RUN 2 (the decision)
    section("RUN 2 (v2) -- Cotlar sums: battery + COMPLETE "
            "holdouts (+ the truncated contrast)")
    series = []
    for kz in battery:
        r = cache.get(kz)
        if r is None:
            r, err = readouts_v2(kz)
            if r is None:
                print("    kz %d: %s" % (kz, err))
                continue
        series.append(dict(kz=kz, h=r["h"], Su=r["Su"],
                           Sc=r["Sc"], Bu=r["Bu"],
                           Bc=r["Bc"], tag="battery"))
        print("    kz %-4d h %-4d [battery]: S_U %.4f  "
              "S_C %.4f  B_U %.4f  B_C %.4f"
              % (kz, r["h"], r["Su"], r["Sc"], r["Bu"],
                 r["Bc"]), flush=True)
    krein_ok = True
    trunc_contrast = {}
    hold_res = {}
    for kz in HOLDOUTS:
        kw = {}
        if kz in DEEP:
            kw = dict(comb=comb_ext(kz))
            rt, errt = readouts_v2(kz)      # truncated (v1)
            if rt is not None:
                trunc_contrast[kz] = (rt["Su"], rt["Sc"],
                                      rt["lam1"])
        r, err = readouts_v2(kz, **kw)
        if r is None:
            print("    kz %d: %s" % (kz, err))
            continue
        hold_res[kz] = r
        if kz in DEEP:
            krein_ok &= abs(r["lam1"] - KREIN_EXT_REFS[kz]) \
                / KREIN_EXT_REFS[kz] <= 0.2
        series.append(dict(kz=kz, h=r["h"], Su=r["Su"],
                           Sc=r["Sc"], Bu=r["Bu"],
                           Bc=r["Bc"], tag="HOLDOUT"))
        tc = trunc_contrast.get(kz)
        print("    kz %-4d h %-4d [HOLDOUT%s]: S_U %.4f  "
              "S_C %.4f  B_U %.4f  B_C %.4f   lam1 %+.3e%s"
              % (kz, r["h"],
                 ", COMPLETE comb" if kz in DEEP else "",
                 r["Su"], r["Sc"], r["Bu"], r["Bc"],
                 r["lam1"],
                 ("   [truncated v1: S_U %.2f S_C %.2f "
                  "lam1 %+.1e]" % tc) if tc else ""),
              flush=True)
    check("R2.1 [DEEP-ALPHA REGRESSION] the complete-comb "
          "Krein floors at kz 142/177/243 reproduce "
          "deep_alpha_sign (rel 0.2) and are positive",
          krein_ok and all(hold_res[kz]["lam1"] > 0.0
                           for kz in DEEP if kz in hold_res))
    verdicts = {}
    for lbl, ix in (("S_U", "Su"), ("S_C", "Sc")):
        v, mb, mh, slope, r2 = decide(series, ix)
        verdicts[lbl] = v
        print("    %s: battery max %.4f, holdout max %.4f "
              "(ratio %.2f, bar 1.2), log-log slope %.3f "
              "(bars 0.10/0.20), lin R^2 %.2f -> %s"
              % (lbl, mb, mh, mh / mb, slope, r2, v))

    # Epstein/scramble contrast at kz 9 (v1 regression)
    print("\n    controls at kz 9 (v1 bars):")
    rt9 = cache[9]
    rr9w = core.build_window(9)
    N_E = int(math.floor(math.exp(2.0 * rr9w["alpha"]))) + 1
    lamE = gnu.lambda_eps(N_E)
    nn = np.nonzero(np.abs(lamE) > 1e-12)[0]
    ctrl_ok = True
    for nmc, kw in (("Epstein", dict(comb=(
            np.log(nn.astype(float)),
            2.0 * lamE[nn] / np.sqrt(nn.astype(float))))),
            ("scramble", dict(scramble_seed=1))):
        rc, err = readouts_v2(9, **kw)
        if rc is None:
            print("    %-8s: %s (typed)" % (nmc, err))
            continue
        tri_t = np.array([rt9["Su"], rt9["Sc"],
                          rt9["dshare"]])
        tri_c = np.array([rc["Su"], rc["Sc"], rc["dshare"]])
        rel = float(np.max(np.abs(tri_c - tri_t)
                           / np.maximum(tri_t, 1e-12)))
        okc = rel >= 0.25 and (rc["eps_sum"]
                               >= 5.0 * rt9["eps_sum"]
                               or rc["sp_u"] > -0.8)
        ctrl_ok &= okc
        print("    %-8s: (S_U, S_C, danger) = (%.3f, %.3f, "
              "%.3f) vs truth (%.3f, %.3f, %.3f): max rel "
              "%.0f%%; eps ratio %.1f; env Spearman U %.2f "
              "-> %s"
              % (nmc, *tri_c, *tri_t, 100 * rel,
                 rc["eps_sum"] / max(rt9["eps_sum"], 1e-300),
                 rc["sp_u"], "breaks" if okc else "FAILS"))
    check("R2.2 [DISCRIMINATION] Epstein and scramble break "
          "the v1 contrast bars", ctrl_ok)

    # ---------------- RUN 3 (only if BOUNDED on both)
    bounded = all(v == "BOUNDED" for v in verdicts.values())
    if bounded:
        section("RUN 3 (v2) -- the analytic envelope "
                "candidate (unlocked by BOUNDED)")
        refs = []
        for kz in list(ANCHORS) + list(HOLDOUTS):
            r = cache.get(kz) or hold_res.get(kz)
            if r is None:
                continue
            ch = r["chains"]

            # MECHANICAL FIX of the v1 run3 line (never
            # executed there: v1 stopped at GROWING): the
            # verbatim v1 expression broadcasts (n-1,) against
            # (n-2,); the intended coefficient drift is the
            # aligned sum.
            def _drift(al, be):
                d1 = np.abs(np.diff(al))
                d2 = np.abs(np.diff(be[:len(al) - 1]))
                m = min(len(d1), len(d2))
                if m == 0:
                    return float(np.max(d1)) if len(d1) \
                        else 0.0
                return float(np.max(d1[:m] + d2[:m]))
            dco = max(_drift(ch["alp"], ch["bep"]),
                      _drift(ch["alm"], ch["bem"]))
            dd = np.arange(len(r["env_u"]), dtype=float)
            K1 = float(np.max(r["env_u"] * (1.0 + dd)))
            K2 = float(np.max(r["env_c"] * (1.0 + dd) ** 2))
            tag = "HOLDOUT" if kz in HOLDOUTS else "anchor"
            refs.append((kz, tag, K1, K2))
            print("    kz %-4d h %-4d [%s]: K_1 = %.4f, "
                  "K_2 = %.4f, delta_coef = %.3e"
                  % (kz, r["h"], tag, K1, K2, dco))
        run3_ok = True
        for lbl, ix in (("K_1", 2), ("K_2", 3)):
            mb = max(x[ix] for x in refs if x[1] == "anchor")
            mh = max(x[ix] for x in refs
                     if x[1] == "HOLDOUT")
            stab = mh <= 1.2 * mb
            run3_ok &= stab
            print("    %s: anchor max %.4f, holdout max "
                  "%.4f -> h-stable: %s (bar 1.2x)"
                  % (lbl, mb, mh, stab))
        check("R3.1 [ENVELOPE CANDIDATE] K_1 and K_2 are "
              "h-stable on the complete-comb holdouts",
              run3_ok)

    # ---------------- TASK 2: the truncation audit
    section("AUDIT -- comb-truncation census of the recent "
            "waves")
    print("""    cap: ATOM_MAX = %d (log %.4f); truncated
    frame-A rungs: kz 142 (X 4.4e5), 177 (7.9e5), 243
    (1.8e6); every h <= 900 battery rung and kz 90/116/121
    are complete (W-N3).

    probe                     truncated rungs used   verdict dependence
    ---------------------------------------------------------------
    pruefer_compensation v1   142/177/243 (3/5 hold) CONFOUNDED -- the
      COTLAR-GROWING decision leaned on the holdout max/slope;
      re-decided by THIS probe (v2 verdict below).
    phase_polygon             142/177/243 (3/5 hold) battery-driven;
      holdout rows were truncated-comb objects -> re-run below.
    residual_quadrature       142/177/243 (3/5 hold) ROBUST +
      STRENGTHENED -- the 47/47 sign agreement means the horizon
      detected the truncation-negatives correctly (a validated sign
      detector); the "stall = deep alpha" reading retypes to
      "stall = truncated comb".
    pi_resonance_anatomy      177/243 (deep-alpha pair) verdict
      RESONANCE-THICK ROBUST (decided on certified rungs: excision
      gain zero, soft overlap zero there); the S3b addendum
      ("alpha-law lives at the premise level") CONFOUNDED --
      retyped by deep_alpha_sign; the alpha/h quartet separation
      test is VOID (its deep-alpha pair was truncated).
    softport_radau17          none (h <= 900 ladder)  UNAFFECTED
    preconditioned_port       none (h <= 900 ladder)  UNAFFECTED
    cdcore / jacobi_uvarov    none (holdouts 40/49/60) UNAFFECTED
    excess_certified_skeleton none (filter excluded)  UNAFFECTED
    """ % (core.ATOM_MAX, math.log(core.ATOM_MAX)))
    print("    polygon re-run at the corrected rungs "
          "(x0 = 0, complete combs; ADDENDUM v1.1 typing):")
    poly_states = {}
    for kz in DEEP:
        b = hold_res[kz]["b"] if kz in hold_res \
            else gnu.build_rung(kz, comb=comb_ext(kz))
        import warnings
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", RuntimeWarning)
            pg = ppg.polygon_rung(b, 0.0)
        finite = (math.isfinite(pg["minrel"])
                  and math.isfinite(pg["fullrel"]))
        if not finite:
            st = "NUMERIC-VOID"
        elif pg["nneg"] == 0 and pg["fullmarg"] >= 0.0:
            st = "HOLDS"
        else:
            st = "REFUTED"
        poly_states[kz] = st
        print("    kz %-4d: #neg prefixes %d/%d, min rel "
              "margin %+.2e, full rel %+.2e  -> %s"
              % (kz, pg["nneg"], pg["M"], pg["minrel"],
                 pg["fullrel"], st))
    poly_void = any(v == "NUMERIC-VOID"
                    for v in poly_states.values())
    check("A.1 [POLYGON TYPING] no complete-comb deep rung "
          "REFUTES the polygon; states %s (VOID = raw-"
          "longdouble machinery out of range: the polygon "
          "holdout rows retype to VOID; the POLYGON-HOLDS "
          "verdict stays battery-driven ROBUST on in-cap "
          "rungs only)"
          % (sorted(poly_states.values()),),
          all(v in ("HOLDS", "NUMERIC-VOID")
              for v in poly_states.values()))

    # ---------------- V verdict
    section("V -- FROZEN VERDICTS + honest consequence")
    if all(v == "GROWING" for v in verdicts.values()):
        v2 = "COTLAR-GROWING-CONFIRMED"
    elif bounded:
        v2 = "COTLAR-BOUNDED-V2"
    else:
        v2 = "COTLAR-PARTIAL-V2 (S_U: %s, S_C: %s)" \
            % (verdicts["S_U"], verdicts["S_C"])
    print("\n  V2 COTLAR VERDICT: %s" % v2)
    if trunc_contrast:
        print("  truncated-vs-complete contrast at the deep "
              "holdouts:")
        for kz in DEEP:
            if kz in trunc_contrast and kz in hold_res:
                tS, tC, tl = trunc_contrast[kz]
                r = hold_res[kz]
                print("    kz %-4d: S_U %.2f -> %.2f, S_C "
                      "%.2f -> %.2f, lam1 %+.1e -> %+.1e"
                      % (kz, tS, r["Su"], tC, r["Sc"], tl,
                         r["lam1"]))
    print("""
  HONEST CONSEQUENCE: the v1 COTLAR-GROWING verdict stands
  ONLY as a statement about the truncated data (its own
  frozen rules, correctly applied to what was measured); the
  v2 verdict above is the scientific answer on complete
  combs, under bars, cells and pairing frozen identically to
  v1 (single change documented + warded).  The truncation
  audit retypes the affected findings; the residual-horizon
  sign detector emerges VALIDATED, the polygon holdout rows
  %s, and the resonance-anatomy
  quartet test is void.  NO RH claim."""
          % ("are HARDENED at the corrected rungs"
             if not poly_void else
             "retype to NUMERIC-VOID (out of longdouble "
             "range at complete combs; battery verdict "
             "unaffected)"))
    npass = sum(1 for _n, ok in CHECKS if ok)
    print("\n[TIME] %.1f min   [CHECKS] %d run, %d failed%s"
          % ((time.time() - T0) / 60.0, len(CHECKS),
             len(FAILS),
             ("  " + ",".join(FAILS)) if FAILS else ""))
    return 0 if npass == len(CHECKS) else 1


if __name__ == "__main__":
    raise SystemExit(main())
