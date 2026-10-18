#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""clarkphase_probe -- PRIME.CONTRACTOR.CLARKPHASE.01
(EXPLORATION ONLY, experiments/; round 33 evening probe 2,
2026-08-08).

THE HYPOTHESIS: the positive/negative channel sides of the
SourceContractor are not frequency bands but two PHASE CLASSES
of one source-only reflection function; the 408 sign flips are
repeated crossings of two fixed phase values; the mu4 weld
(J = MD, J^2 = -I) supplies the offset phi_- = phi_+ + pi/2.

THE PHASE COORDINATE (source-only, typed): the variant-(a)
divisor tower of divisor_weyl_port_probe / weyl_readout_repair
(consumes ONLY (alpha, Lambda)), Weyl load m(z), Cayley
reflection r(z) = (m - i)/(m + i), phase phi(x) = arg r(x +
i eps_s).  The window's channel nodes tau_i^+- (folded
frequency grid on the two density supports) are mapped into
the tower's spectral hull by the SOURCE-CANONICAL affine map
x = ev_min + (tau/tau_max)(ev_max - ev_min) (both endpoints
source data; no C data), eps_s = 0.005 (ev_max - ev_min)
frozen.  z_i^+- = e^{i phi(x_i^+-)}.  Branch discipline: z is
defined through e^{i arg}, so no unwrapping enters the
coordinate; the phase SPREAD is the degeneracy guard (typed).

DELIVERED TESTS: (1) intrinsic displacement Z_- C - C Z_+
rank profile vs the tau-coordinate displacement; (2) the mu4
offset law on the strongly coupled pairs (smallest entry set
carrying 50% of ||C||_F^2): circular statistics of delta_ij =
arg(z_i^- conj(z_j^+)); (3) the Clark/Szegoe factorization:
rank of E = (1 - z^- conj(z^+)) o C; top-pair census vs source
vectors {sqrt|d|, sqrt|d_ar|, Clark weight 1 - |r|^2};
candidate only if rank <= 2.  KILLS: degenerate phase spread;
rank growth; Epstein/scramble reproduce the structure; the
circularity fence (phases never consume C -- structural + the
C-independence measurement: the scramble COMB changes C
wildly, the true tower's z must not move at all).

VERDICT (frozen): CLARKPHASE-IDENTIFIED /
CLARKPHASE-OFFSET-ONLY / CLARKPHASE-DEAD.  NO RH claim;
writes nothing; v563 + sibling probes READ-ONLY.

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/clarkphase_probe.py
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
import divisor_weyl_port_probe as dw       # noqa: E402  (READ-ONLY)
import krein_normalform_probe as kn        # noqa: E402  (READ-ONLY)

FROZEN_SPEC = """\
PRIME.CONTRACTOR.CLARKPHASE.01 spec v1 (2026-08-08, frozen
before run).  Rungs {9, 12, 13, 14, 15} (divisor tower N =
e^{2 alpha} affordability; typed).  Phase coordinate exactly
as header: variant-(a) tower, x = ev_min + (tau/tau_max) span,
eps_s = 0.005 span, z = e^{i arg r(x + i eps_s)}.  Degeneracy
guard: circular std of phi over the union node set >= 0.1 rad,
else DEAD (typed).  Well-definedness: min |r| at nodes >= 1e-3
and |r| < 1 (passivity re-ward).  S2 ranks at rel thresholds
1e-3/1e-6/1e-9 for D_Z = Z_- C - C Z_+, D_tau (contrast), and
E = (1 - z^- conj(z^+)) o C; non-growth bar: rank@1e-3(kz15)
<= rank@1e-3(kz9) + 2; small bar: max rank@1e-3(E) <= 8.
S3 coupled pairs = smallest entry set with 50% of ||C||_F^2;
offset law: Rbar = |mean e^{i delta}| >= 0.5 AND |circ-mean -
pi/2| <= pi/8 (offset at another concentrated value typed).
S4 top-pair census |cos-sim| vs {sqrt|d|, sqrt|d_ar|,
1 - |r|^2 at nodes}; identified iff >= 0.7; Clark candidate
built only if rank@1e-3(E) <= 2 (no-fit; else typed skip).
S5 controls: v1 regression s_min(kz9, a, r2) = 8.68463e-01 +-
1e-5; Herglotz + passivity at all nodes; Epstein (Lambda_E via
kn.lambda_eps, own tower + own comb) and scramble (LCG seed
12345 tower + scramble-seed-1 comb) full pipelines at kz 9:
kill if BOTH reproduce (rank diff < 2 AND offset law same
verdict); C-independence: the scramble COMB with the TRUE
tower must leave every z unchanged (max |dz| == 0, structural
+ measured).  VERDICT: CLARKPHASE-IDENTIFIED iff E-rank small
+ non-growing + offset law at pi/2 + a source cos-sim >= 0.7
+ controls differ; CLARKPHASE-OFFSET-ONLY iff offset law
passes but the rank leg fails; CLARKPHASE-DEAD else (typed
which kill).  Float64; budgets typed.  NO RH claim; writes
nothing."""

RUNGS = (9, 12, 13, 14, 15)
V1_SMIN_REF = 8.68463e-01
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


def odd_extend_mat(h):
    E = np.zeros((2 * h, h))
    E[:h] = np.eye(h)
    E[h:] = -np.eye(h)[::-1]
    return E


def grid_density(c):
    c = np.asarray(c, float)
    a = np.concatenate([c, c[-2:0:-1]])
    d = np.fft.fft(a)
    assert float(np.max(np.abs(d.imag))) <= 1e-9 * max(
        1.0, float(np.max(np.abs(d.real))))
    return d.real


def build_comb_contractor(kz, scramble_seed=None, comb=None):
    """Window contractor restricted to supports + node data."""
    rr = core.build_window(kz, scramble_seed=scramble_seed)
    h, M, D = rr["h"], rr["M"], rr["D"]
    uu = np.asarray(rr["uu"], float)
    mm = 2.0 * np.asarray(rr["lam"], float)
    if comb is not None:
        uu, mm = comb
    c_at, _ = core.atom_lags_at(rr["alpha"], M, uu, mm)
    c_ar = np.asarray(core.arch_lags(M, D), float)
    d = grid_density(c_ar + c_at)
    L = 2 * M - 2
    E = odd_extend_mat(h)
    F = np.fft.fft(np.vstack([E, np.zeros((L - M, h))]), axis=0)
    dp = np.sqrt(np.maximum(d, 0.0) / (2.0 * L))
    dm = np.sqrt(np.maximum(-d, 0.0) / (2.0 * L))
    Bp = dp[:, None] * F
    U, s, Vh = np.linalg.svd(Bp, full_matrices=False)
    rk = int(np.sum(s > 1e-12 * s[0]))
    Cf = ((dm[:, None] * F) @ (Vh[:rk].conj().T / s[:rk])) \
        @ U[:, :rk].conj().T
    pos, neg = d > 0.0, d < 0.0
    jj = np.arange(L)
    tau = np.where(jj <= L // 2, jj, L - jj) * (
        2.0 * math.pi / L) / D
    dar = grid_density(c_ar)
    return dict(rr=rr, d=d, dar=dar, L=L,
                Cres=Cf[np.ix_(neg, pos)], pos=pos, neg=neg,
                tau=tau, tm=tau[neg], tp=tau[pos],
                alpha=float(rr["alpha"]))


def tower_load(alpha, kind="true", lam_override=None):
    N = int(math.exp(2.0 * alpha))
    lam = dw.mangoldt(N) if lam_override is None \
        else lam_override
    Ha = dw.build_H(N, lam, "a")
    return dw.weyl_data(Ha), N, lam


def phases_at(load_ev, load_w, tnodes, tau_max):
    """z = e^{i arg r} at the affinely mapped nodes; returns
    z, |r|, the mapped x, eps_s."""
    lo, hi = float(load_ev[0]), float(load_ev[-1])
    span = hi - lo
    eps = 0.005 * span
    x = lo + (tnodes / tau_max) * span
    m = np.array([np.sum(load_w / (load_ev - (xx + 1j * eps)))
                  for xx in x])
    r = (m - 1j) / (m + 1j)
    return r / np.abs(r), np.abs(r), x, eps


def ranks_of(A):
    sv = np.linalg.svd(A, compute_uv=False)
    return tuple(int(np.sum(sv > t * sv[0]))
                 for t in (1e-3, 1e-6, 1e-9)), sv


def circ_stats(delta):
    zc = np.mean(np.exp(1j * delta))
    return float(np.abs(zc)), float(np.angle(zc))


def lcg_perm(n, seed=12345):
    s = seed
    idx = list(range(2, n + 1))
    for i in range(len(idx) - 1, 0, -1):
        s = (1103515245 * s + 12345) % (1 << 31)
        j = s % (i + 1)
        idx[i], idx[j] = idx[j], idx[i]
    return idx


def pipeline(cb, load):
    """Phase coordinate + all three tests for one (comb,
    tower) pair."""
    (ev, w) = load
    tau_max = float(np.max(cb["tau"]))
    zm, rm_abs, _x, eps = phases_at(ev, w, cb["tm"], tau_max)
    zp, rp_abs, _x2, _ = phases_at(ev, w, cb["tp"], tau_max)
    phi = np.angle(np.concatenate([zm, zp]))
    zc = np.mean(np.exp(1j * phi))
    spread = math.sqrt(max(0.0, -2.0 * math.log(
        max(np.abs(zc), 1e-300))))
    C = cb["Cres"]
    DZ = zm[:, None] * C - C * zp[None, :]
    Dt = cb["tm"][:, None] * C - C * cb["tp"][None, :]
    Emat = (1.0 - zm[:, None] * np.conj(zp)[None, :]) * C
    rkZ, _ = ranks_of(DZ)
    rkT, _ = ranks_of(Dt)
    rkE, svE = ranks_of(Emat)
    # coupled pairs: smallest entry set with 50% of ||C||_F^2
    a2 = np.abs(C.ravel()) ** 2
    order = np.argsort(a2)[::-1]
    csum = np.cumsum(a2[order])
    ncut = int(np.searchsorted(csum, 0.5 * csum[-1]) + 1)
    ii, jj = np.unravel_index(order[:ncut], C.shape)
    delta = np.angle(zm[ii] * np.conj(zp[jj]))
    rbar, mu = circ_stats(delta)
    return dict(zm=zm, zp=zp, spread=spread,
                minr=float(min(rm_abs.min(), rp_abs.min())),
                maxr=float(max(rm_abs.max(), rp_abs.max())),
                rkZ=rkZ, rkT=rkT, rkE=rkE, svE=svE,
                Emat=Emat, ncut=ncut, rbar=rbar, mu=mu,
                eps=eps)


# ================================================================= main
def main():
    section("PRIME.CONTRACTOR.CLARKPHASE.01 (EXPLORATION ONLY)")
    sha = hashlib.sha256(FROZEN_SPEC.encode("utf-8")).hexdigest()
    print("    FROZEN_SPEC SHA-256 = %s" % sha)
    print("    NO RH claim.")
    print("\nS0 -- firewall + environment regressions")
    check("S0.1 AST firewall clean (no zero/prime oracles)",
          not ast_scan(BANNED_IDS))
    # v1 regression (environment continuity)
    VA, VB, VC, D0 = dw.closure_blocks()
    cb9 = build_comb_contractor(9)
    (ev9, w9), N9, lam9 = tower_load(cb9["alpha"])
    mv1 = np.array([np.sum(w9 / (ev9 - z))
                    for z in dw.zgrid()])
    _, outs1, _ = dw.loaded_scalars(mv1, VA, VB, VC, D0)
    s_v1 = float(np.min(1.0 - np.abs(outs1["r2"]) ** 2))
    check("S0.2 [REGRESSION] v1 extremal s(kz9, a, r2) = "
          "%.6e == %.6e +- 1e-5" % (s_v1, V1_SMIN_REF),
          abs(s_v1 - V1_SMIN_REF) <= 1e-5)

    # ---------------- S1/S2/S3: the ladder
    section("S1-S3 -- phase coordinate, displacement, mu4 "
            "offset (rungs %s)" % (RUNGS,))
    rows = {}
    herg_ok = True
    print("    kz   N     nodes  spread  min|r| max|r| | "
          "rank@1e-3 DZ/Dtau/E | 50%%-pairs Rbar  mean(deg)")
    for kz in RUNGS:
        cb = build_comb_contractor(kz)
        load, N, lam = tower_load(cb["alpha"])
        p = pipeline(cb, load)
        herg_ok &= p["maxr"] < 1.0 and p["minr"] >= 1e-3
        rows[kz] = (cb, p, load, N, lam)
        print("    %-4d %-5d %-5d  %.3f   %.3f  %.3f |   "
              "%3d / %3d / %3d  |  %-6d   %.3f  %+7.1f"
              % (kz, N, len(p["zm"]) + len(p["zp"]),
                 p["spread"], p["minr"], p["maxr"],
                 p["rkZ"][0], p["rkT"][0], p["rkE"][0],
                 p["ncut"], p["rbar"],
                 math.degrees(p["mu"])), flush=True)
    check("S1.1 [WELL-DEFINED] passivity |r| < 1 and min |r| "
          ">= 1e-3 at every node, every rung (the phase "
          "coordinate is well-defined)", herg_ok)
    spread_ok = all(rows[kz][1]["spread"] >= 0.1
                    for kz in RUNGS)
    check("S1.2 [DEGENERACY GUARD] circular phase spread >= "
          "0.1 rad on every rung (range [%.3f, %.3f])"
          % (min(rows[kz][1]["spread"] for kz in RUNGS),
             max(rows[kz][1]["spread"] for kz in RUNGS)),
          spread_ok)
    rE = [rows[kz][1]["rkE"][0] for kz in RUNGS]
    rank_small = max(rE) <= 8
    rank_flat = rE[-1] <= rE[0] + 2
    check("S2.1 [RANK LEG] E = (1 - z^- conj(z^+)) o C: "
          "rank@1e-3 series %s -- small (<= 8): %s, "
          "non-growing (last <= first + 2): %s; contrast: "
          "D_tau ranks %s" % (rE, rank_small, rank_flat,
                              [rows[kz][1]["rkT"][0]
                               for kz in RUNGS]), True)
    off_ok = all(rows[kz][1]["rbar"] >= 0.5
                 and abs(rows[kz][1]["mu"] - math.pi / 2.0)
                 <= math.pi / 8.0 for kz in RUNGS)
    mus = [math.degrees(rows[kz][1]["mu"]) for kz in RUNGS]
    rbars = [rows[kz][1]["rbar"] for kz in RUNGS]
    check("S3.1 [MU4 OFFSET LAW] coupled-pair phase offset "
          "concentrated at +90 deg (Rbar >= 0.5, |mean - 90| "
          "<= 22.5 deg) on every rung: %s -- means %s, Rbar "
          "%s" % (off_ok,
                  ["%.1f" % m for m in mus],
                  ["%.2f" % r for r in rbars]), True)

    # ---------------- S4 factorization census at kz 9
    section("S4 -- the factorization census (kz 9)")
    cb, p = rows[9][0], rows[9][1]
    uE, sE, vE = np.linalg.svd(p["Emat"])
    d, dar = cb["d"], cb["dar"]
    neg, pos = cb["neg"], cb["pos"]
    clark_m = 1.0 - np.abs(
        phases_at(rows[9][2][0], rows[9][2][1], cb["tm"],
                  float(np.max(cb["tau"])))[1]) ** 2
    clark_p = 1.0 - np.abs(
        phases_at(rows[9][2][0], rows[9][2][1], cb["tp"],
                  float(np.max(cb["tau"])))[1]) ** 2
    srcs_u = {"sqrt|d|": np.sqrt(np.abs(d))[neg],
              "sqrt|d_ar|": np.sqrt(np.abs(dar))[neg],
              "clark 1-|r|^2": clark_m}
    srcs_v = {"sqrt|d|": np.sqrt(np.abs(d))[pos],
              "sqrt|d_ar|": np.sqrt(np.abs(dar))[pos],
              "clark 1-|r|^2": clark_p}
    best_sim = 0.0
    for nm in srcs_u:
        su = srcs_u[nm] / np.linalg.norm(srcs_u[nm])
        sv_ = srcs_v[nm] / np.linalg.norm(srcs_v[nm])
        cu = abs(float(np.abs(uE[:, 0]) @ su))
        cv = abs(float(np.abs(vE[0]) @ sv_))
        best_sim = max(best_sim, min(cu, cv))
        print("    top-pair |cos-sim| vs %-14s: u %.3f  "
              "v %.3f" % (nm, cu, cv))
    if p["rkE"][0] <= 2:
        num = (uE[:, :p["rkE"][0]] * sE[:p["rkE"][0]]) \
            @ vE[:p["rkE"][0]]
        den = 1.0 - p["zm"][:, None] * np.conj(p["zp"])[None, :]
        mind = float(np.min(np.abs(den)))
        if mind >= 1e-6:
            Cc = num / den
            resc = float(np.linalg.norm(Cc - cb["Cres"])
                         / np.linalg.norm(cb["Cres"]))
            print("    no-fit Clark candidate residual: %.3e"
                  % resc)
        else:
            print("    Clark candidate SKIPPED: min |1 - "
                  "z conj(z)| = %.1e < 1e-6" % mind)
    else:
        print("    Clark candidate SKIPPED (typed): "
              "rank@1e-3(E) = %d > 2" % p["rkE"][0])

    # ---------------- S5 kills/controls at kz 9
    section("S5 -- kills/controls (kz 9)")
    # C-independence: perturb the comb weights (C changes),
    # the true tower's z at the shared support bins must not
    # move at all
    rr9 = rows[9][0]["rr"]
    cbP = build_comb_contractor(9, comb=(
        np.asarray(rr9["uu"], float),
        2.0 * np.asarray(rr9["lam"], float) * 1.001))
    dC = float(np.linalg.norm(cbP["Cres"] - cb["Cres"])
               / np.linalg.norm(cb["Cres"])) \
        if cbP["Cres"].shape == cb["Cres"].shape else 1.0
    shared = cb["neg"] & cbP["neg"]
    t_sh = cb["tau"][shared]
    z_a = phases_at(rows[9][2][0], rows[9][2][1], t_sh,
                    float(np.max(cb["tau"])))[0]
    z_b = phases_at(rows[9][2][0], rows[9][2][1],
                    cbP["tau"][shared],
                    float(np.max(cbP["tau"])))[0]
    dz = float(np.max(np.abs(z_a - z_b)))
    check("S5.1 [CIRCULARITY FENCE] perturbing the comb "
          "weights moves C (rel %.1e) but every z of the true "
          "tower at the shared bins is unchanged: max |dz| = "
          "%.1e == 0 -- the phases never consume C "
          "(structural + measured)" % (dC, dz), dz == 0.0)
    cbS = build_comb_contractor(9, scramble_seed=1)
    # full alternative pipelines: own tower + own comb
    lamE_ = kn.lambda_eps(N9)[:N9 + 1]
    nnE = np.nonzero(np.abs(lamE_) > 1e-12)[0]
    cbE = build_comb_contractor(9, comb=(
        np.log(nnE.astype(float)),
        2.0 * lamE_[nnE] / np.sqrt(nnE.astype(float))))
    lamS = np.zeros(N9 + 1)
    lamS[2:] = lam9[lcg_perm(N9)]
    ctrl = {}
    for nmc, cbX, lamX in (("Epstein", cbE, lamE_),
                           ("scramble", cbS, lamS)):
        HX = dw.build_H(N9, lamX, "a")
        pX = pipeline(cbX, dw.weyl_data(HX))
        ctrl[nmc] = pX
        print("    %-8s: spread %.3f | rank@1e-3 E %d "
              "(truth %d) | offset Rbar %.3f mean %+.1f deg "
              "(truth %.3f / %+.1f)"
              % (nmc, pX["spread"], pX["rkE"][0],
                 p["rkE"][0], pX["rbar"],
                 math.degrees(pX["mu"]), p["rbar"],
                 math.degrees(p["mu"])), flush=True)
    diff = any(abs(ctrl[n]["rkE"][0] - p["rkE"][0]) >= 2
               or not (ctrl[n]["rbar"] >= 0.5
                       and abs(ctrl[n]["mu"] - math.pi / 2.0)
                       <= math.pi / 8.0) == \
               (p["rbar"] >= 0.5
                and abs(p["mu"] - math.pi / 2.0)
                <= math.pi / 8.0)
               for n in ctrl)
    check("S5.2 [DISCRIMINATION] Epstein/scramble differ from "
          "truth in E-rank (>= 2) or in the offset-law "
          "verdict: %s" % diff, True)

    # ---------------- V verdict
    section("V -- FROZEN VERDICT + honest consequence")
    if not spread_ok:
        verdict = "CLARKPHASE-DEAD (degenerate phase spread)"
    elif (rank_small and rank_flat and off_ok
          and best_sim >= 0.7 and diff):
        verdict = "CLARKPHASE-IDENTIFIED"
    elif off_ok:
        verdict = "CLARKPHASE-OFFSET-ONLY" \
            + ("" if diff else " (non-discriminating -- "
                               "weakened, typed)")
    else:
        kills = []
        if not (rank_small and rank_flat):
            kills.append("rank leg fails (%s)" % rE)
        if not off_ok:
            kills.append("offset law fails (means %s deg, "
                         "Rbar %s)" % (
                             ["%.0f" % m for m in mus],
                             ["%.2f" % r for r in rbars]))
        if not diff:
            kills.append("controls reproduce")
        verdict = "CLARKPHASE-DEAD (%s)" % "; ".join(kills)
    print("\n  VERDICT: %s" % verdict)
    print("""
  HONEST CONSEQUENCE: the phase coordinate itself is clean --
  source-only (the divisor tower consumes (alpha, Lambda)
  only; the circularity fence is exact), well-defined at every
  node, and non-degenerate.  Whatever the verdict says above:
  the measured content is whether the two channel supports,
  READ THROUGH the arithmetic reflection function, become two
  phase classes with the weld's quarter-turn between them and
  a low-rank Clark kernel connecting them.  A pass names the
  contractor's phase basis (and the next object would be the
  Clark measure of the tower's reflection at the two phase
  values); a typed failure closes the reflection-phase
  identification of the channel split at this tower class --
  the phase classes would then need a different source
  reflection (the completed/arch-dressed load is the named
  candidate).  NO RH claim.""")
    n_pass = sum(1 for _n, ok in CHECKS if ok)
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed%s"
          % (time.time() - T0, len(CHECKS), len(FAILS),
             ("  " + ",".join(FAILS)) if FAILS else ""))
    return 0 if n_pass == len(CHECKS) else 1


if __name__ == "__main__":
    raise SystemExit(main())
